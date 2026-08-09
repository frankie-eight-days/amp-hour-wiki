---
episode: 590
title: Finding Hardware Flaws with Laura Abbott
url: https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/
---

**Laura Abbott:** This is The Amp Hour Podcast. Released May 22nd, 2022. Episode 590. Finding Hardware Flaws with Laura Abbott.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Laura Abbott:** I'm Laura Abbott. I'm an engineer at Oxide Computer.

**Chris Gammell:** Hello, Laura. How are you? I'm doing well today. How are you? Great. Yeah, I'm excited to talk to you. We got connected because you were giving a talk at the upcoming Hardware I.O. conference, and it actually is about a vulnerability. I think we actually didn't talk about this last security vulnerability, but I think maybe a previous one before that. We didn't really understand it, I don't think, but I remembered Oxide. I remembered vulnerability research and stuff like that, and I'm sure that you were involved there. So what is this talk that you're going to be giving at the upcoming Hardware Conference?

**Laura Abbott:** Yeah, this is a talk about... I sort of stumbled during my time at Oxide into becoming an accidental vulnerability researcher. What Oxide is doing, for those who haven't heard it before, is rethinking the server from the ground up. The server hasn't really been redesigned in many years. So Oxide is thinking about how to make it overall better experience for those who are using it. And one aspect of rebuilding the server is having a better hardware security model to be able to tell what software is actually running on your server. And as part of doing some work for that for our root of trust, I accidentally stumbled upon a buffer overflow in the update mechanism for the chip we're trying to use for our root of trust.

**Chris Gammell:** That seems not very trustworthy. Well, so can you explain root of trust as kind of a basic concept as well?

**Laura Abbott:** Sure. So when I say root of trust, that can mean a lot of different things to many people. I'd say the word TPM, but that sometimes tends to get people to have a lot of emotional responses to that. But for what Oxide is trying to do with the root of trust is the idea is that it's answering the question, what software is running on your machine? So the theory behind here is that if you have a chip or something that executes a known set of code and you can say, we're going to assume that we trust this, if that can take something like a hash of another part of the system and then build up a series of hashes, that can give an answer to what exactly is running on the system. You're able to say, this is what we expect to be running on system versus not. Okay.

**Chris Gammell:** So if someone had somehow been able to come in and place some other software on the system, it wouldn't pass that because they wouldn't necessarily be able to pass the same kind of challenges that are happening by this chip and the root of trust. Is that kind of another way of saying it?

**Laura Abbott:** Yeah, that's a good way of putting on it. The idea is that we'll be checking what we expect to run and then you compare that against what's actually running.

**Chris Gammell:** It seems like a really hard problem to solve, actually. When I think about when I log into a remote system and when I get certain things back from that remote system, a lot of what I as a human would be asking for would be pretty easy to spoof. And I think it would get harder for a computer if a computer was asking for those things from that remote system. But even still, at a certain point, you have to make it unspoofable.

**Laura Abbott:** Yeah, it's a pretty tricky problem for a number of things. And that's also one of the things Oxide is trying to do very carefully is figuring out how to design this such that you can't fake the measurements or have someone else pretend to be the measurements. And then the other thing that's, as we've discovered in building a server, is that when a lot of people think of a server, they think, okay, there's just the main processor that runs your operating system, like say Linux or Windows. But it turns out that there's a whole bunch of other microcontrollers spread all over your system. So there's also the question about how exactly do you make sure all the software that's running on those as well is what you expect.

**Chris Gammell:** Yeah. Yeah. Actually, I was just rewatching a thing about like Stuxnet the other day. And just like, you know, it does feel like when there's vulnerability, I mean, obviously, that was 10 plus years ago now. But like vulnerabilities and stuff like that, it seems like it's down in the firmware these days. You know, the software stuff, there's a lot of testing there. There's a lot of focus on security. But then when people are like, oh, well, yeah, the firmware should just work on the temperature sensor. And like, how could that be a problem? But maybe you could fake it overheating or something like that.

**Laura Abbott:** Yeah, I think there's a growing awareness that any possible software out there can become a vector. Certain people in the security community have certainly been talking about the danger of the firmware for a very long time. But I think there's becoming increasing awareness as you've talked about here more and more about supply chain security for software that firmware itself can be vulnerable to. So it's definitely important to sort of think about every part of your system and exactly what sort of malicious things you could be doing there.

**Chris Gammell:** Right. Yeah. And I always imagine like the folks that are doing software type stuff and they're like, well, wait, how do I update this firmware? It's like, well, you have two choices. We give you just a binary file that we hope works or you can go plug in physically and do the exact same thing. It's like, oh, God. Yeah.

**Laura Abbott:** And it's kind of ironic because the vulnerability I found was actually in the update system for the chip.

**Chris Gammell:** Oh, wow.

**Laura Abbott:** The vulnerability was in the ROM itself to be able to handle an update. So it was designed to be able to potentially let people update the software on there. But it's also the question about, OK, what do you do when there's a bug in your updating system?

**Chris Gammell:** Yeah. Oh, my gosh. Yeah. That's just like turtles all the way down at that point. So what is the what is the part that you found this in?

**Laura Abbott:** It's the LPC 55 S69 from NXP.

**Chris Gammell:** And like give us a relative measure on like, is this like a Cortex M0, Cortex M7, something bigger than that? Again, like I don't really I don't know where where is this? What is the part doing on on the server side of the board? Is it measuring temperature or something like that or something much bigger?

**Laura Abbott:** This is a Cortex M33. So this is an ARM V8M, which is the microcontroller version updated from ARM.

**Chris Gammell:** Yeah. Yeah.

**Laura Abbott:** This is a relatively new version of ARM. And it also this chip also has a trust zone M, which is one of the reasons it was appealing to us. So as for what this chip is doing, this is the root of trust. And the root of trust is designed to be fairly limited. And it is really designed to be just the core security functions related to measurement. Also on the system, we're going to have what we're calling the service processor. This is designed to be a spiritual replacement for a baseband management controller on a typical server. And that is a we're using an STM32H7 for this service processor. So our service processor is the one that's going to be responsible for temperature control and other things like that. Several of my colleagues spent the past two weeks doing bring up on the next revision of our board and they were doing some temperature measurement and settings there. And it was pretty funny to watch the screenshots they would send back and forth of the graphs of the temperature going up, the temperature going down as they tried to put more work on things.

**Chris Gammell:** Yeah, that's great. Yeah, I guess maybe we need to take a step back even because I don't really even know what's on a server board. I don't know what's... So obviously you just listed two things here, right? You have the root of trust chip and the service processor. But like what else... Could you maybe kind of paint a word picture of what else might be on a board in terms of other microcontrollers that are kind of hanging around there?

**Laura Abbott:** I mean, if you think about what an entire server is also involved, it's certainly going to involve some sort of networking. And networking processors are yet another chip on there. Depending on what you might do for temperature control, maybe there's yet another thing on there. There's also going to be a lot of other, say, possibly SPY or just flash storage for holding other details. It's hard to say. And then this also isn't even getting into the microprocessors we might not know about, especially as you look about big chips like, say, from AMD or Intel may have another of other processors in there that are running who knows what, which is slightly terrifying when you think about trying to actually build a product on top of that. If you... We have no idea exactly what might be running on some of those.

**Chris Gammell:** Right, right. Even when you sign the NDA with them, they're like, well, yeah, we're not going to give you everything though. Come on. We can't give you all the secrets. We're just selling you a very, very expensive chip here.

**Laura Abbott:** Trust us. It's fine. Yeah.

**Chris Gammell:** Yeah, yeah, yeah. It'll all work out. We have the top people working on this. Oh my, that's, yeah, that's, that's interesting. I mean, I guess servers like, you know, they crank a lot of juice too, right? So like, is there power management? Like, is there monitoring of power management as well? I would imagine.

**Laura Abbott:** Yes, there's power, power management for being able to have a power control and being able to check to make sure everything's going along there. Gosh, maybe I just need to pull up the schematic here so I can just start looking through everything here, but it's fascinating to see just how many different pieces there are and exactly which parts are. Oxide is a fantastic team of hardware engineers who've worked very hard to try and make sure everything is there in terms of trying to get everything going. Oxide has been doing some Twitter spaces occasionally where people have talked about this and the tales there from the hardware team have been really good about the experience about trying to bring everything up and just debug things, including just down to things about such as spending a multiple ways, figuring out that a pull up resistor was not strong enough.

**Chris Gammell:** Oh, yeah, yeah. So then another thing that kind of just comes up in general is like, I think about other specific servers that I could go buy tomorrow, right? I don't really hear often about, you know, like the companies that are making those, talking about these things publicly. So it seems like Oxide is a little bit more open in this way as well, like talking about vulnerabilities, publishing vulnerabilities, like talking about system architecture. How open is the system that you're designing as well?

**Laura Abbott:** The goal is to have as much stuff be public as possible. This includes making all of our code as open source and sharing as much of our design as we can, just because ultimately we believe that, you know, the value is going to be in, you know, the hardware that we, hardware plus the software we deliver.

**Chris Gammell:** Yeah, I mean, well, and one thing I always think about too is with like, with security, kind of like the cleansing, the cleansing power of sunlight sort of thing of like, well, yeah, we're going to show you everything here, but instead of hiding the firmware away, we're showing you what it does, where it is, what we were allowed to show you, that sort of thing. And that actually could enable others to then analyze it and say like, wait a second, this might be a problem as well. And kind of open it up to the crowd sort of thing.

**Laura Abbott:** Absolutely. And the firmware that we're going to be running on the root of trust and our service processor is an open source operating system that we designed called Hubris. We open sourced it late last year. And so that's all available to review. I think that we, we expect, you know, people, there's been some interest from the community about people who have been interested in poking at it. And all the interest to see is that if it gets a serious look to see if anyone ends up finding any issues. I think about that. I've certainly found vulnerabilities here. And, you know, it's, I think it's inevitably there's going to be issues with Oxide's servers. And I hope we're able to handle them in a way that, you know, satisfies our customers. Yeah.

**Chris Gammell:** I mean, humans are bug making machines, right? I know I am.

**Laura Abbott:** Yeah. The best software and best hardware is, you know, the one that isn't there.

**Chris Gammell:** That's right. Yeah, exactly. I have to say Hubris, naming, naming a project Hubris, that's, that's like, that's like fold, fold back meta kind of thing there. That's, that's great.

**Laura Abbott:** So the story behind Hubris sort of comes to some of the early time at Oxide. So I joined Oxide in January, 2020, and this was pretty early in the time of Oxide. And we were trying to figure out exactly what we were going to do. And we were doing a survey about what was available for operating systems for microcontrollers, just because we knew that was what we wanted to do for the root of trust and service processors. And during the surveys, we had a couple of things that we thought had potential. And as, you know, one of the potential options, I think I wrote up something about, you know, writing our own. And I said, yeah, you know, it's possible for us to write our own, but it doesn't seem like it's a good idea or a good use of our time. And well, of course, I ended up eating my words there a little bit, just because one of my coworkers, Cliff, had sort of this idea bouncing around about what is it, about the ideal operating system for a microcontroller he'd like to see. And so that eventually turned into Hubris. And yes, Hubris was a little bit of a joke about, are we really going to try and write our own operating system? But so far it's been, you know, people have thought it seems fairly interesting.

**Chris Gammell:** So yeah, I feel like on a long enough timeline, you know, any engineer will end up writing their own operating system.

**Laura Abbott:** It's not something to be taken lightly, but I think part of this is also we're hopefully learning from all of our past mistakes about what did and didn't work.

**Chris Gammell:** Yeah, that's interesting. I mean, that's, I guess we'll find out and see how it works. So then what about on, so then on a server, that's another thing I think about with, with kind of secure elements and secure pieces of a system is kind of communication between different parts of the board as well. So like kind of protecting your, your ins and your outs. Does that mean that then the communication between chips also has to be like encrypted or how, how does that end up working like on a board?

**Laura Abbott:** Yeah, it really depends on what, what exactly you're talking to. So as far as, you know, connections on the board, it, most things are probably going to be using protocols you've heard of, say, spy I squared C to be able to do things. But then as far as what goes over that may very well be encrypted or other things like that. Part of the work some other of my teammates have been working on is figuring out how exactly we're going to be sending data back and forth between the root of trust, the surface processor and the host processor to be able to say, do measurements or see exactly what's running on the system. And there's definitely a lot of work out there. And then it takes a lot of thought to make sure you're getting everything right. Just because anything related to encryption has a, it's possible to get it subtly wrong. So.

**Chris Gammell:** Yes. Or, or completely wrong. And then you don't see anything. That's usually how I do it. I'm like, oh, look, that's, that's a lot of garbage there still. I must've gotten the wrong key.

**Laura Abbott:** I mean, I'm always terrified about doing something. It's like, ah, this looks like, you know, random enough. And then it turns out there's something that makes it always predictable. So I think we're taking a, trying to take our time to really make sure what we're doing is correct.

**Chris Gammell:** Yeah. That's really cool that, that you, that you were like digging down and rebuilding the whole thing from the ground up. That's, I mean, you'd said that hasn't been done in many years, but like other, other, I guess I don't even know of other server companies in general too. So like, is this kind of a first in the space?

**Laura Abbott:** There, it sort of depends on what aspect you're thinking about in terms of when I say that the server hasn't really been redesigned. I mean, ultimately a lot of servers still ultimately end up looking like, you know, a PC that would go on your desktop. And there's been some work by say some of the large cloud providers, like related to the open compute project to try and get some specifications for more modern hardware to be able to build some of these things. But there's nothing out there that if you're not one of these large hyperscalers, you can't actually get one of these nice modern machines. So that's sort of the, the space oxide is trying to look at to do.

**Chris Gammell:** Oh, that's interesting. Yeah. I had, I had seen some of the open, open compute started at Facebook. Is that right? Yeah. Meta?

**Laura Abbott:** It was a collaboration between a bunch of companies.

**Chris Gammell:** Okay. Okay. Yeah. And I guess it's another thing that I, you know, like, again, just from the very outside to me, you know, yes, the cloud is someone else's computer, but I didn't really care about which computer it was and where it was running or anything like that. But I remember seeing a tour of like a Google data center and I was like, oh my God, they just have like circuit boards hanging out there. I kind of always imagine like, you know, full, full like fan racks and everything like that. It just, it seems like it's a whole different world than I expected. Yeah.

**Laura Abbott:** The, the, the, the design of hardware at say companies like Google or Facebook is drastically different from what you might, might think of. Several of my colleagues at oxide had done previous work with, with Google. So they can definitely have told a lot of, they learned a lot of experience things from their experience there.

**Chris Gammell:** Yeah. That's so then, so oxide is not necessarily building a server to go into this like unified server farm. Like only Google's running within this server facility. It's more like this could then be installed into a more generic facility. Like you buy like the, not the hosting, what's it called? Like a slot in a server center.

**Laura Abbott:** Yeah. The, the, the goal is to deliver an oxide rack. If you, on, on the oxide website, there've been some pictures about what our vision for a server actually looks like. And I think we're going to get the point where we're starting to get some physical pictures of rack back. And it's been very excited to seeing the physical product and putting people next to the racks that we can see just how big this thing is.

**Chris Gammell:** Do you do, how many times have you all watched that, that scene in Silicon Valley where the guy's like, is it more like a cheetah or like a jaguar? You've got like the music playing in the background.

**Laura Abbott:** Several of my colleagues refuse to watch Silicon Valley because they claim it's too accurate.

**Chris Gammell:** It's very accurate. Yeah. Oh God. I love that show. Actually, no, they had this, this, this visual is actually really nice. I'll, I'll, I'll link all this stuff into our show notes as well. And so it seems like it's actually like a full rack. It's not just like a slotting into a standard one, you, two, you, it's actually meant to be the whole thing. Is that kind of the idea? Yes.

**Laura Abbott:** The vision is to deliver a full rack.

**Chris Gammell:** I see.

**Speaker ?:** Okay.

**Chris Gammell:** So you said it's not like a Google or Facebook, but it's like a, like who would buy this? Cause I think about like a lot of smaller companies and a lot of them are like, well, I'm just going to buy from an Amazon or AWS or an Azure or something like that as well. This is kind of targeting them when they're growing out of that as well.

**Laura Abbott:** There's a number of different people who I think are still interested on in having stuff on premises. I, just because, uh, you know, we're building a server, it doesn't necessarily mean the cloud is going away. I think we've definitely shown that there's value in it, but there may be reasons for data integrity, data privacy laws, just a pure speed about not wanting to have things somewhere where people would still want to run things on premises. So I think that there's a lot of reasons why people might think so. And then there's, there's also always the, the cost is that it turns out that, you know, there's sort of a scale thing where maybe in the early days of whatever your company is doing, it makes sense to be able to rent the cloud space. But as you grow bigger, it, you know, makes less sense.

**Chris Gammell:** Yeah. Yeah. That's, that's a really good point about the security too. Like, you know, it's kind of these things that I just, you know, as a. As a person who buys very little cloud space and has very little capabilities in the web world. You know, I just think about like, I don't think about the, the security aspect and the, you know, if you're running, if you're running some kind of like enterprise solution where you need to guarantee to your client that you're secure all the way down to the metal sort of thing that, that could be very, very critical.

**Laura Abbott:** Yeah. And I, sometimes when I talk about this, I start hearing a lot of, okay, so this means the cloud is completely insecure, which again, I don't think is the, is, is, is correct. It's mostly just, we're thinking about what exactly you're doing with this particular set of data and it may ultimately be about use cases as well.

**Chris Gammell:** Yeah. Okay, cool. Well, let's dive all the way back down to the metal. Cause this is, this is a cool part that you've been working on and thank you for giving us that background information. That's really useful. All right. So we're, we're down on this NXP LPC 55 S6. Nine and you found something's wrong. How did you, how did you kind of start digging into this? Like what was your task that, that had you digging into this in the first place?

**Laura Abbott:** Uh, so this, I ended up finding this, I will admit out of a little bit of a procrastination.

**Chris Gammell:** Oh, I know that one.

**Laura Abbott:** So the NXP LPC 55 has a built-in format in the ROM to be able to handle updates. And I was, you know, intending to work on this format to be able to build images ourselves. So the idea is that, that you would be able to package whatever arc software that we wanted to run and put it into this format that the ROM would be able to load as an update. But it turned out that trying to parse this format was kind of a pain and I was getting annoyed with trying to go back and forth. So I kind of started thinking about it, about what exactly this was doing and sort of asking myself, says, okay, parsing, this seems kind of complicated. How well did they actually validate, you know, the various parts of the, of the header? So I started asking this and, you know, playing with it. I ended up, um, you know, somewhat stumbling across it in a way that where it doesn't seem like they were bounds checking something. And I was able to turn that into a, you know, 50 proof of concept for, uh, being able to, you know, do things I wasn't supposed to.

**Chris Gammell:** Uh-huh. So you basically start like, so, so when you're doing this sort of thing, then you start like kind of throwing bogus packets at it or, or what are, what's the nature of that?

**Laura Abbott:** So the, uh, update mechanism works across, is, works across, um, what NXP calls on the ISP protocol in system programming. It can work across URs, I squared C. Um, I was doing it across some UR because that was the most convenient. So I would, the idea is, is that you're supposed to send it a, uh, series of bytes corresponding to the update and it will apply them. And, uh, the way the update works is that there's, the update is supposed to be signed and encrypted, but before, uh, you get everything, there's an, uh, unencrypted header to be able to get some information about where things are going. So essentially what I ended up doing, adjusting with some of the fields in that header and saying, okay, what happens if I set, uh, this value a lot larger than perhaps they're expecting it to be and, uh, starting to do this. And I would also say that I had some assistance in that I was also had a ROM dump of, uh, the LP-75, just, which came about from a previous work I had done somewhat accidentally about trying to that, uh, in finding things with the LP-75.

**Chris Gammell:** Okay. All right. So you basically, you, you tell it, Hey, I've got 2000 bytes for you or something like that. And it's all, it's only really got space for what, like a thousand. And then, so then it starts to write into a, into a different memory space or something like that.

**Laura Abbott:** Yeah. So, so something like that. There's a, there's a field in the header that's supposed to point to where the block for a set of encryption keys goes. And it turned out that the bounds check for where it was supposed to copy the header into some global space was based on where that pointer was instead of say, just copying the size of the header. So what it is, is that if I set that pointer, uh, you know, much larger than it should be, it would just, you know, happily continue copying past where I could, where, uh, it was, you know, supposed to go. Oh yeah.

**Chris Gammell:** Okay. That sounds like other things I've heard in the past, or then you can start to use that as your, uh, as your paintbrush to go rewrite memory, huh?

**Laura Abbott:** Yes. And then it was, uh, I also would say I happened to get very lucky that afterwards there were some, uh, convenient, uh, other things in the memory that I was able to manipulate pretty easily to be able to, uh, use that to my advantage.

**Chris Gammell:** Okay. Yeah, no, this is really, I mean, like, so what is, what do you think is happening then on the other side of this interface? I mean, this is, this is the NXP's ROM, or this is actually like a hardware control or in there that's doing that.

**Laura Abbott:** This is NXP's ROM. This is all in software.

**Chris Gammell:** Okay. Interesting. So then it is adjustable or fixable, I guess, is, is the nice thing about that?

**Laura Abbott:** Uh, so the thing about ROMs is, is that if, if it's true mask ROM, you use, you know, can't really fix it without actually getting new hardware.

**Chris Gammell:** Ah, okay. All right. So without just some very fancy laser beams or equivalent.

**Laura Abbott:** Yeah. But it turns out that there, um, is a, uh, the NXP does have the ability to patch the ROM, um, by fixing, uh, individual bytes. And I actually found, uh, in a previous issue with the LPC-55, I discovered this ROM patcher that it turns out can also be used to violate various security boundaries. Wow.

**Chris Gammell:** This is a bountiful product, uh, for, for, uh, conference papers, huh? Apparently. Yeah. Yeah. Wow. What, I mean, so I guess then what, what, what, how did this make the cut in the first place? I, I don't, I don't know what, what the criteria was for the initial part.

**Laura Abbott:** It turns out that we had a fairly specific set of criteria about what we were looking for, especially for the security and what we were looking for as the root of trust. And we were doing all this research and had selected this, I think back in like spring 2000, 2020. And, uh, it turned out that there was actually a very narrow set of candidates we even were able to consider. And then even back then we were still having problems where there were things that sounded great, but then it turned out yet that the silicon wasn't actually still shipping. And for another six months, we couldn't actually get our hands on stuff. So I think the, the LPC-55 at the time was, you know, the, the best, uh, really the best candidate we found.

**Chris Gammell:** I see. Okay. And was some of that tied to having the, the trust M zone?

**Laura Abbott:** That was a, definitely a, a, an appeal of having the, uh, trust zone M available to be able to, uh, do more isolation for things.

**Chris Gammell:** And so could you explain what that is? Cause I, so I've seen that on, uh, it's actually on some parts that I'm using recently because they also have an M33, but I don't really understand what they're for.

**Laura Abbott:** Yeah. So it's a little thing about trust zone as adding a, uh, another layer to the matrix is that typically is that if you think about processors as may have maybe having a, privilege, unprivileged mode, trust zone gives as a secure, non-secure zone. So you can have, then have a code that's a secure and privilege, secure, non-privilege, non-secure and privilege, non-secure, non-privilege. And so the idea is, is that, um, that lets you have a, another set of, uh, code to be able to run in secure mode.

**Chris Gammell:** Okay. And so then you have to kind of specifically give it a key to, I guess the thing I always get confused with, with like a privilege mode or like a, you know, a keyed area or like a encrypted area of code is like, how do then, how then do I, as the programmer of that chip, go and set that up so that other people can or cannot use it?

**Laura Abbott:** That's a very good question. And usually involves reading a lot of documentation, especially for something like a trust zone. And there's a series of registers you can set to be able to, to declare specific registers as regions of memories as, uh, secure or non-secure. And I believe the default configuration can be such that you declare what regions are non-secure so that everything else is secure by default.

**Chris Gammell:** Oh, wow. Okay.

**Laura Abbott:** And then you end up having to do very specific sequences to be able to transition between secure and, uh, non-secure world. And this is actually well-designed, um, on ARM's part to hopefully make it difficult to accidentally transition from secure to non-secure, uh, when you, or non-secure to secure when you don't actually, when you did not intend to.

**Chris Gammell:** Yeah. So, okay. So maybe, maybe to use that, that pointer example you talked about earlier. So like, if I then somehow had control of like a, you know, just an errant pointer and I pointing at a non-secure part of memory, and then I scooted over to the secure part of memory, how does the chip respond to that? Does it just say, no, there's nothing in here or there it's, it's, it's encrypted or something like that?

**Laura Abbott:** It would probably end up being a fault. So especially with, with trust zone, um, you end up having to go through a specific sequences to be able to go through that. Now, if you happen to be able to make the pointer to be able to trigger one of those gateways, you know, you, you would be able to do the transition, but I mean, you know, nothing is perfect, but the goal, I think, especially something like trust zone M is to make it much harder for people to get, get in secure mode, except through very specific entries points.

**Chris Gammell:** Got it. So it's like that, uh, very complicated lock system that you have to kind of go through in order to, uh, to finally reach the other side.

**Laura Abbott:** Yeah. It's a very narrow window, you know, tiny squeeze in like a mouse hole.

**Chris Gammell:** Okay. Oh, interesting. Yeah. I think that I'm using a NRF 9160. It's like a cellular chip quite a bit these days. And it has some of that stuff and it has like, uh, there's an easy way to build for the non secure. I always build for like the non-secure area. That's where like some of the application code runs. It's no big deal. But then I think a lot of like the modem firmware and stuff like that, I think that lives in the more secured areas and it has to be like specially keyed in that sort of thing.

**Laura Abbott:** Yeah. And I think also depending on what exactly you're using to build as well, there may be other things. So I, we've been doing all of our work in Rust and trying to do everything there. And it's been a interesting seeing some of the support for especially TrustZoneM actually come into the tool chain. I think there's a lot of interest in trying to use things like TrustZoneM, but some of this also requires a compiler support to be able to do, to be able to place functions appropriately.

**Chris Gammell:** Okay. So everything, everything in Oxide is using Rust. Is that part of the, is that like a name, play on the name or something? Cause Oxide Rust. Yeah.

**Laura Abbott:** Yeah. So the, the, the term, the name of the computer company Oxide does in fact come, I think Rust was a part of it, but yeah, I think Rust is generally one of our preferred languages. I think especially Brian Cantrell has talked about this in past talks about why he likes Rust. I like it as someone who did C for, who's done C and is, you know, fairly experienced with C is that Rust actually, what I like to think of is it makes it easier for me to be able to do the stuff I, I, I want in terms of being able to solve problems that I don't want to think about.

**Chris Gammell:** Yeah. What's an example of one of those problems?

**Laura Abbott:** I think just, you know, we gave the example, you know, I, the vulnerability I found that the classic buffer overflow Rust has, Rust arrays are checked and everything like that. And it does this in such a way such that means certain classes of problems are just not going to happen. Assuming you're using the, you're not using any, doing anything unsafe.

**Chris Gammell:** Yeah, that's right. That's the keyword that you have to like, you have to like. Block around something. If you're like, I'm about to do something very, very bad. And then you put unsafe around it, then you're allowed to do it. Right. That's, that's what I always think of.

**Laura Abbott:** Yeah. But it turns out actually that using unsafe is not necessarily a bad thing, especially when it comes to things like, like hardware. Unsafe actually has a very particular meaning and especially this sort of, what exactly does memory safety mean? I didn't actually know much Rust before I joined Oxide. So I, and I've been fortunate to work with a lot of colleagues and I've learned a lot of them, especially about how to do some of these lower level things with things like memory safety and learn about exactly what are good practices for actually working with unsafe code. Just because it turns out that especially for things like you might do for embedded things like even just running to a register might be considered unsafe just for, for how the memory model works. But of course you still end up having to do those.

**Chris Gammell:** Yeah. Yeah. That's what I kind of always come back to is just like when you're in C it's like, that's just kind of the, that's the path you're shown. You're like, okay, well you have to go change this register. You need to turn that led on and you have to go and like mask out that one register and you know, flip the one bit. Okay, cool. But that's not, it's probably not the right idea in a lot of ways that you're doing stuff and with C and it's like, and then also just thinking about like, just kind of keeping the memory, keeping all the memory stuff and like allocating memory, deallocating memory. It's just, there's a lot of, a lot of dangerous stuff that happens there.

**Laura Abbott:** Yeah. And, and I definitely think that, that Russ does a fantastic job about being able to do manage it as much as you can behind the scenes. I mean, it's not that, you know, nobody is smart enough to be able to do this. It's that, it's that trying to program is, is that a difficult task as is. And, you know, letting the compiler say, do the analysis to figure out how to do some of this so you don't have to is a great way to focus on other things.

**Chris Gammell:** Yeah. Yeah. That's great. Yeah. So one thing that I've, I've tried, I've done a video about Rust where I was talking someone to someone about it. And, and the thing that I didn't quite understand is kind of like, so if I wanted to go use Rust on just any generic part, there needs to already be like a HAL interface layer that you can talk to, or like, how, how do you know if Rust will work on a part like the LPC 55S 69?

**Laura Abbott:** That's a great question. I think it sort of depends on a couple of different things. I think it ultimately, the first big question about is, is that what chip architecture are you actually running on? And is there a tool chain support in general for that? And I think you find that most of the common ones out there for all the ARM that is, that's a reasonably well supported in Rust and that's available. So that's the first question. And then I think the next question is, is that, is there crate level access to be able to do all the, uh, register manipulation?

**Chris Gammell:** Okay. And crate, what was it? Like you explained crates as well?

**Laura Abbott:** Sure. Uh, crate is sort of like a, a Rust package.

**Chris Gammell:** Got it. So that's basically going to be like, you can go and install a crate and it might be for this LPC 60, uh, 55S 69. I should just have this in front of me. Sorry. I keep switching tabs. Uh, and, and then that basically gives the compiler knowledge of like where an ADC might be so you could start to talk to the ADC without having to go toggle some bits in a register sort of thing.

**Laura Abbott:** Right. And I think especially the, the embedded Rust community is, is, is a fantastic and has done, um, a lot of work out there to try and add support. And there's, uh, crate support out there for all the Cortex-Ms to be able to get stuff up and going for, I think most of the fairly, most of the common chips to be able to do things. And, uh, the nice things about having the Rust crates out there is, is that they've written the abstractions for, to be able to do, um, most of the manipulation for being able to say, access the registers and everything.

**Chris Gammell:** Oh, that's good. Does it, does it end up in a, like, because the abstractions there, you know, one thing I always talk about to people about is like, they're like, well, when there's abstractions, it's kind of slow stuff down or I'm not used to it or whatever. But like, is there any performance hit because of the abstraction layer or is it just kind of seamless to the user?

**Laura Abbott:** Uh, I'd say for the most part, it's pretty seamless. This is that, um, you know, I, I, the compiler is fantastic about being able to figure out the optimizations, I think about being able to really, you know, turn it down to something that ends up looking, uh, fairly similar to, if you were to look at, like I say, a C disassembly. I'm not going to say there's never a cost to the abstractions, but I think that the compiler, you know, does the, the best, uh, it can to be able to make sure it's not there.

**Chris Gammell:** Yeah. I mean, well, I, when I really think about it, it's like, well, I'm not looking at the disassembly of the C stuff that I write either. So it's not like, again, I'm just kind of like saying what I hear, not like what I've experienced. Uh, so it's, it's good to, that's good to know. That's interesting though. So like the, so then as a, at a very, very high level, does using Rust kind of give your clients kind of some more peace of mind or is it just more of a kind of a ethos around the company?

**Laura Abbott:** I, I, I, I'd like to believe it's a little bit of both. I mean, it certainly is an ethos is, is, is that, I mean, the, again, the concept about being able to say, eliminate array out of bounds errors is, uh, or, you know, anything sort of that memory and safe areas is, is a, you know, very strong assertion. And we'd like to believe that, uh, you know, oxide customers, but we'll see this as a valuable as well and understand exactly why we're taking the time to write everything, uh, in Rust.

**Chris Gammell:** Yeah. Back to the, uh, back to the hardware piece. I mean, so, so now you've, you've solved this piece, right? Or you've discovered this piece. Is this something that actually has been patched or you were able to move forward with, with this part?

**Laura Abbott:** So, uh, the NXP, um, has, uh, it has, has plans to release a fixed version, which is great for us, but I, but I think trying to actually agree to fix it and, um, actually getting it to us are two different questions I'd probably say. And so for now, I think we're, hopefully we, we want to be able to get the fixed version, but I think we also did some careful analysis about what exactly we would do if we ended up needing to, you know, potentially work with the buggy chip. And I think our conclusion was, is that we just have to try to, uh, not use, uh, the existing update code path that we had wanted to use, which means we're going to be on our own to be able to write update code.

**Chris Gammell:** Uh, okay. So then that becomes, so I guess is the update code kind of, would you consider it at, at like a firmware level? Like I guess it's in the ROM, but like what, what is going to be ultimate alternate path then?

**Laura Abbott:** So the update code provided in the ROM was, I like to think of it as sort of a, you know, hardware vendor value add as a, as a, as a, as a, as a, as a, as a, as a, update code honestly, isn't usually a, if I'm building a product on top of a chip saying, Hey, we've got, you know, our own custom update code, uh, isn't really a selling point, you know, to try and do that. And that might be able to just go in the ROM is, you know, potentially doing there. So it's certainly possible for us to be able to do our own update code without touching this in the ROM, but it just makes it a little bit, a little bit trickier in some respects for us to be able to think about how exactly we're doing that.

**Chris Gammell:** Got it. Got it. Okay. And so now it's like, you'll just have to kind of write your own, I guess, do you write your own bootloader then? Is that kind of part of it as well?

**Laura Abbott:** Yeah. So, uh, I've been working on writing a bootloader and trying to figure out that split there. And then of course, figuring out how to divide the, uh, flash up into different spaces to be able to do robust image updates as well. And, um, figuring out, uh, a lot of, a lot of aspects are related to say how we want to, if we want to do image rollback, how do we do versioning? And I'm once again, grateful to work with a lot of some colleagues who have had experience before about this and have a lot of good insight about to how to, you know, make sure this is all correct.

**Chris Gammell:** Yeah. One thing that always scares me about like a firmware updates and rollbacks and stuff like that is just the, what if it, what if the new image, you know, you put all these tasks in place. So you're like, okay, you download this new image and everything, you do some tests on it. You're like, all right. Yeah, it looks good. But it was just, just the, just the important parts, like the, uh, it passes. It only knows how to pass the tests that you've put in front of it. And then there's something else is broken behind it. You know, there's no way to really, to really know that sort of thing. It feels like.

**Laura Abbott:** Yeah. That's definitely one of the nightmare scenarios. Um, and, uh, we, we spent a lot of time in our view about trying to figure out what exactly we would do in that case. And sometimes it ultimately comes down to policy or design decisions about whether you want to, you know, say only a rel, allow rollbacks to an older version, or that might also have a different set of bugs or only allow things to move forward, which might fix some bugs, but then have a different, potentially introduce a different set of bugs.

**Chris Gammell:** Uh, yeah, yeah, yeah, yeah. Hmm. That's an interesting, uh, thing. So then what, so, so you have the server and I assume that you're not plugging in a cable to it. Maybe you are, I'm not sure. But how you actually like, so you have a bootloader on this, this chip that you're, you're writing and how, how does that package of new firmware get delivered to it? If you're allowed to say.

**Laura Abbott:** Yeah, this is something we're definitely still working through the design aspect. And I mean, the, the, ultimately the, what we hope to do is, is that I have everything, um, uh, you know, just happen mostly automatically. They'll, it'll come through the host processor and then the host processor will send everything from the service over to the service processor. And then from the service processor onto the root of trust. Um, one of the ways is that we try and, uh, make sure that the root of trust is isolated from everything else is that, that, but it really, the only connection the root of trust has is to the service processor. So the service processor is going to be responsible for transmitting, um, uh, the update data securely, um, over to the root of trust.

**Chris Gammell:** Got it. And so, because you're not like trying to, you would never try and update the service processor at the same time as the root of trust processor, you'd be fine because it's, it's just passing along this binary or, or whatever it is down to the, down to the root of trust processor. Yeah.

**Laura Abbott:** Yeah. You've definitely hit upon an important aspects about figuring out, um, how exactly you're supposed to sequence updates and about when exactly you want to be applying these updates. I, I was, I think I remember, uh, when we were reviewing the design of some of this, you know, when my colleague asked about, well, well, what if you want to write the update, but then maybe not reboot yet? What if the service processor is busy? There's a lot of different, uh, moving parts to be able to make sure you can actually update the system.

**Chris Gammell:** Yeah. And I guess another question too, is just like, is this a common thing that happens? Like how often does firmware get updated on servers? I don't even know these sorts of things.

**Laura Abbott:** I think the answer is, is that unfortunately less, less, uh, often than anybody would like. It mostly seems like it only gets, uh, for a lot of the major updates, it only seems to come out when there's, you know, some sort of catastrophic bug.

**Chris Gammell:** Oh, got it. Yeah. Like, uh, the server starts on fire. We should probably update servers that are not on fire. Huh? Okay. And then on the, so the host processor, that would be like the thing running Linux or windows or whatever the, the, the server itself is like, basically it can understand kind of, I am a server, but I have these, these sub functions. Is that kind of the idea?

**Laura Abbott:** Yeah. So the idea is, is that, uh, the host processor is going to be running, um, what is essentially our, our, uh, hypervisor. That's going to be able to host virtual machines for the customer to be able to, and then the, uh, virtual machines are going to be running the customer's workloads.

**Chris Gammell:** I see. Okay. So it's like, it's basically like the scaffolding for all these other, these other loads, these other servers on VMs basically. Right. Yeah. Okay. That makes sense. Hmm. And then, so is then there a management program on that hyper on the host processor? So the host processor has its own OS that runs the hypervisor, but it also has like stuff to talk down to lower level firmware. Yeah.

**Laura Abbott:** The host processor definitely has knowledge about the management network to be able to communicate to the service processor. And there are, there are a couple of different ways that the host processor can be able to talk to the service processor. There's a dedicated management network connection. I think it's ethernet. And then there's also your communication. And I think maybe a couple of other different ways where it can, uh, send things back and forth.

**Chris Gammell:** Okay. Yeah, that's great. Okay. So just, just to review the root of trust thing one more time, because I'm not sure I still quite understand it. So we've been talking about the firmware update for the root of trust processor. And that's basically the stuff that you discovered and you found this vulnerability and you're working on a bootloader for that. And that's going to be different in the future probably, but it's still kind of in flight. It sounds like. So now fast forward a couple of months, everything's hunky dory. No firmware updates are applied. The root processor is just sitting there and it's talk and only talks to the service processor. What is an everyday task of the root processor? Like, does the service processor offer challenges? Is that, I remember you said something at the beginning about like, uh, hashes, but like, what, what is the, what is those, what is the root processor sitting there doing on an everyday basis?

**Laura Abbott:** The root of trust is, you know, ultimately just going to be hold the, let's say the, the identity of the server. So it's, I think your idea about challenging responses is, is, is a, you know, good example about what it's doing. So when it comes time to say, take measurements about what's going on, it may, for example, need to remeasure something, or it may actually just be sitting there, um, idle, uh, a lot of the time, depending on what exactly it needs. If there's anything related to the identity of the server, say maybe related to encryption, that's one possibility. Some of this is, is that we're, we're still ultimately designing.

**Chris Gammell:** Oh, sure.

**Laura Abbott:** What the root of trust actually can be. And I think this has been one of the interesting things about working at oxide is that there's such a wide design space and sort of figuring out what exactly it is we want to do.

**Chris Gammell:** Yeah. Yeah. So you, you, you've said a couple of times measuring. So what is the measuring piece? Is it like measuring environmental data or something else?

**Laura Abbott:** It's measuring. I think, uh, I'm just using that term to mean, uh, it's essentially just think of, think of it as reading memory from part of a chip and then doing a hash to be able to see exactly what's there.

**Chris Gammell:** Okay. So if you'll excuse the terrible, terrible analogy, it's like a tiny crypto wallet that lives on your, your board.

**Laura Abbott:** That's a, not a terrible, not the worst analogy.

**Chris Gammell:** Well, it's only, only because of the implications of what it is.

**Laura Abbott:** Yeah. I hope I'm more secure than a crypto wallet. So.

**Chris Gammell:** Yeah. Right. Of course. Of course. Yeah. Okay. But it does sound like a kind of similar spaces of like challenges and hashes and stuff like that. Yeah. That's basically how my brain's viewing it. It's not right. It's just how I'm visualizing it. So, uh, so you'd mentioned, uh, working at Oxide and we were talking about this a little bit before the show, but like you've been, you started in 2020. Uh, so you've been all remote this whole time and, um, wow, there's a lot of hardware you're talking about here. So how's, how has that been?

**Laura Abbott:** That's been an interesting experience. So yeah, I joined Oxide in 2020 and I always intended to be remote before, you know, everything else with the pandemic happened. But as far as hardware goes, I think we've sort of been able to figure out, uh, I think a good balance between doing stuff just in software and also with hardware. We were very excited to get a, um, our very first, uh, bring up board related to the root of trust in the service processor. And, uh, I think it was December, 2020. And so I've been using some of that. And since then we've also made at least a couple of other, you know, small development boards to be able to test things. And I've also worked a lot with the NXP evaluation boards to be able to do things back and forth and just be able to run as much as we can. And I think that the hardest part sometimes I think is figuring out how to be able to test the communication, say between, uh, the root of trust in the service processor and being able to have a board that has that proper connection.

**Chris Gammell:** Yeah. I mean, I, I think about it. So I've, I'm in a very similar spot. I've been doing hardware remote for consulting companies and now my current employer. And like, it just, it's, it's a lot of FedEx and a lot of, uh, well, do you have the wire plugged in here? Like I have the wire and then you have like a webcam. It's just like, I wish there was better ways of doing this sort of thing though.

**Laura Abbott:** Yeah. It's, it's definitely tricky, especially when it comes to debugging and trying to, uh, figure things out. I think it was a few weeks ago I was working on, um, trying to do some, uh, work on, on a connection from the ROT to the SP for some of the, uh, new work for you to actually be able to do the measurement involving, uh, utilizing the debug port of the service processor. And I had a setup. I was, I've been trying to test this, but I was seeing it occasionally, uh, fail for reasons I couldn't fathom. And now I was, uh, once again, I work with fantastic colleagues and after some back and forth and sending them, uh, screenshots of the logic analyzer, uh, they were able to help track, track things down and, you know, find some, uh, noise coming on my line from my perhaps a little bit janky breadboard setup. So I think it's, it's a little bit difficult when you're remote for trying to debug setup issues.

**Chris Gammell:** So, I mean, yeah, I think that just having a coworker, uh, like look over your shoulder and like be able to be like, Oh, you know, that looks a little weird, you know, try that. You know, like, it's just like, there's, there's just more overhead to that piece of it. And like I said, webcams aren't great. And, uh, and even like just pointing, pointing at different spots on a board. It's just, there's, there's nothing that replicates the, I don't know. I, I don't think VR is a thing, but if there was a thing that might be good for VR or like some kind of AR or something like that, it would maybe be this just so you could get some better annotation around, around different setups.

**Laura Abbott:** Yeah. Or even just being able to help, you know, cross check, check things. I mean, trying to sort through a pile of, uh, resistors. I have, you know, my own pile at home that isn't well sorted. So, you know, trying to sit there, look at the colors and say, huh, is this red or brown there?

**Chris Gammell:** Right. Right. Well, that's, that, that might just be, you know, asking Oxide to pony up for a lab assistant, uh, in your local town. You know, that might be, it's another solution there. Right. Yeah. But yeah, that's, that is, that is tough. What, uh, what is, what is your, what does your setup look like in your, in your home lab?

**Laura Abbott:** I don't have nearly as an impressive, uh, a home lab set up as some people. I mostly just have on top of my, uh, work desk has a spread out with an, uh, ESD mat with a bunch of boards on top of it. Um, my soldering setup is actually, uh, currently downstairs. It's sort of a jointly shared with my husband for both of our projects for whatever, ever, uh, we need it. But I think we're going to end up having to shuffle things around and I really need to buy another table and probably actually invest in a proper power supply to be able to do work.

**Chris Gammell:** Yeah. Yeah. Well, that's, that's still, I mean, I get, you're able to find key vulnerabilities. Like this. So that's, uh, you should, you should do something right there. That's great.

**Laura Abbott:** Yeah. I mean, I, I'd love to learn more how to do some of the hardware glitching attacks as, as well. I, I, I bought, um, one of the, uh, the chip whisperer and I haven't had a chance to sit down and actually try that to be able to see exactly about and learn how to do those glitching attacks. So.

**Chris Gammell:** Yeah. Yeah. I mean, so, so you came from a software background, but now you've kind of come into the security space as well. What is, what has that been like?

**Laura Abbott:** It's been interesting. So I think I've always worked in the, uh, low level. Um, my, uh, my previous work. I involved, uh, Linux kernel development and I'd always sort of had an interest in security. So I think when, um, I joined Oxide, I was, you know, interested in getting a chance to, uh, learn more about that space.

**Chris Gammell:** Yeah. And what is, what does Linux kernel development look like?

**Laura Abbott:** I generally enjoyed, um, my work I did in, uh, Linux kernel. I spent, I did, I worked on a lot of different things. My, uh, first job was working on Android phones for a, uh, chip vendor. Um, I just happened to join at the right time is when Android was becoming super popular. So I got a chance to really, uh, learn a lot about how, uh, low level Android works and got to do things like, uh, related to memory management. And I really learned a lot about, um, debugging things there. And then I spent some time as a kernel main kernel maintainer where, where I learned, I think a different set of skills about, you know, both the community and about how to do, um, uh, debug parts of the system. I had no idea about in terms of, uh, seeing when people would report bugs there. So I think there's a lot of different things of related to kernel development. I think sometimes when people say kernel development, they, they assume it's, you know, one particular thing, but the kernel is also covers such a wide variety of things from drivers all the way to file systems. So I think there's so many different aspects there.

**Chris Gammell:** Yeah. One thing that always amazes me is just the volume of insights and people working on it and just the, the wrangling that must be required around just. Different people wanting different things to happen, you know, like the, Hey, this is broken. Hey, I need this feature. Like, it just seems like that would be over overwhelming to me.

**Laura Abbott:** It can be pretty overwhelming. And I, and I think this is probably one of the biggest thing I think, especially as, is, you know, Linux turned from a small hobbyist project to something that's used by, uh, large companies. I think sometimes, uh, companies, it takes them a while to figure out, has taken a while on to figure out how exactly to work in the community and how exactly to get their code in and figure out, okay, you know, we need to do something, um, that's, uh, beneficial for the, for the community as opposed to just being beneficial for our company.

**Chris Gammell:** Yeah. How does it, how does a company navigate that sort of thing? I mean, is that something that like they should hire a consultant to like figure that out or just kind of try it and see how it goes or what?

**Laura Abbott:** I mean, I think there are multiple different, different approaches. I think probably, uh, I'm, I serve on the technical advisory board, um, for the, uh, Linux kernel community as part of the Linux foundation. This is something we've been talking, people have talked a lot about over the time. And I think one of the things is that I think that's definitely out there is, is that, you know, is the Linux kernel community works a lot on, on trust. And that, um, part of the idea of doing trust is, is that you can't actually just submit code and just expect it to go in and do nothing else. So you need to have, uh, make sure that, uh, members of a company are getting a chance to say, do code review reporting bugs. So they're actually giving something back as well and getting their input and getting a chance to learn. Because part of what it is, is that if you're doing the small work for things like say code reviews and bug testing, when it comes time to be able to do, uh, the bigger portions for say larger features, you'll have that cloud to be able to help get things in.

**Chris Gammell:** Yeah. That makes sense. It's like, uh, it's not just a one way vendor relationship. Like I think a lot of companies are used to where it's like, well, I gave you money. So now you give me everything I want. And now it's more like, well, you may have donated some money to the foundation or you may have donated some code or some time, but unless you show that push pull and being able to like validate that and get individuals trust, like you said, that, that can definitely be a culture shift. I imagine.

**Laura Abbott:** Yeah. And, and I, I always like to highlight, you know, the, the graphics community and the, as an example about where I think they've done a lot of work to help, you know, vendors be able to, uh, get things in. And it's been a very slow for some vendors to be able to, you know, understand the importance about being able to get thing things in. But I think they eventually, when they do that, it's, you know, then ultimately a better experience.

**Chris Gammell:** That's great. If someone was like listening right now and they're like, ah, I've always wanted to, you know, work on Linux kernel stuff or Linux generally. Like what, what do you usually tell people in terms of like kind of dipping a toe in or getting started?

**Laura Abbott:** I mean, I, I, I can always point to Linux kernel development can mean a lot of things. So I think ultimately I always encourage people to, you know, figure out what it is exactly they're looking for. And also to think about what exactly it is they already know.

**Chris Gammell:** Yeah.

**Laura Abbott:** Especially if you're coming from a software lounge, something like containers or Kubernetes is, is often a buzzword. So learning a little bit more about how Kubernetes or other things like that works at the kernel level is a great way to, to get started. You know, if you have your own laptop and just testing newer kernels on that and being able to learn how to do a bisect when something doesn't work there to be able to help or help report bugs, that's always something that's a very valuable.

**Chris Gammell:** Got it. Okay. So kind of the start small, do some testing. So like almost like a, like a replicating other people's work first and learning, learning the mechanics and that sort of thing and building, building some skills like that.

**Laura Abbott:** Yeah. There's no one right way to get involved. I mean, there are certainly some people out there who will decide that they want their very first thing to do and be able to like write a big new feature. And I mean, you know, maybe that'll work, but I, but I usually encourage people to like try and know, start small and, you know, think about a small thing they want to try and change. There's also a documentation directory. And I mean, being able to keep parts of that up to date is always very much appreciated.

**Chris Gammell:** Yeah. Yeah. And so you mentioned like in the kernel too, there's, there's like the driver's piece and there's interfaces, networking and stuff like that. What, what were you, what were you mostly kind of focused on when you were doing it or still are doing it? I'm not sure actually. Yeah.

**Laura Abbott:** I'm doing a significantly less of it these days, but when I was doing it, I think I spent a lot of time doing work related to the ARM architecture. So some specific ARM stuff related to just because I was working on Android, which ran mostly on the ARM processors. And then I also did some stuff related to memory management and looking at things related to page allocators and also CMA, the contiguous memory allocator. It turns out that solving the problem about, I want to get a large physical chunk of contiguous memory is actually a pretty difficult problem to solve on a, on a system.

**Chris Gammell:** Why is that?

**Laura Abbott:** I think just because when we say large, it's, it's saying maybe more than a megabyte. It turns out that especially for a system with a virtual memory and the things that you're usually optimized to be able to give out everything in a 4k, say for standard 4k page sizes. So if you need anything larger than that, you end up into fragmentation problems. And you can sometimes end up with a trade-off about, well, if you need a large chunk of memory, you can reserve it, but then you can't, maybe you can't use it for anything else. CMA was a technology developed by, I believe was originally came out of Samsung research that was designed to be able to solve this problem about being able to have the memory available for use in the system. And then also be able to get large contiguous blocks when needed.

**Chris Gammell:** That is, yeah, that's really, I mean, like, that's just kind of stuff that like, that's happening every single day, like right under my nose, everybody's nose. Right. And it's just like, I don't know. It's just like computers just work, but it's like, because people are working on it, you know, of course, like that makes sense. That's, that's really cool. That's really cool. Yeah. So anything else we should know about Oxide or your, your discoveries and the vulnerability arena?

**Laura Abbott:** I hope we're done finding vulnerabilities with this chip. You know, I think I'm, you know, grateful to Oxide that they are, you know, supportive of finding these things, but I think they're, you know, we're looking forward to shipping a product that is, you know, hopefully secure and it's something everybody's going to love.

**Chris Gammell:** That's great. And when is, when are you giving your talk?

**Laura Abbott:** The conference is June 9th and June 10th.

**Chris Gammell:** Okay, great. Yeah. I actually, I will be in the area for the Zephyr developer summit at that same, same time, I think. So.

**Laura Abbott:** Oh, cool. I didn't realize Zephyr was at the same time. That's, that's neat.

**Chris Gammell:** Yeah. That's the 6th to the 8th, I think, at the Computer History Museum. Oh, cool. So I'll be, I'll be down that way. We might be doing, might be doing a meetup. We'll see. I'm not sure if we'll get that all worked out. But yeah, no, I had talked to, when Joe Grand was on the show, he had actually mentioned hardware was happening. I think he might be there. And yeah, I'm excited to, I always love the, you know, like this is just like, it's very adjacent to the stuff I do and it's very important and I'm very clueless about it. So it feels like an area that I, I could learn a lot from. So I really like that.

**Laura Abbott:** Yeah, this will be my first time attending hardware and I'm, you know, looking forward to giving my talk and then also getting a chance to meet other people. And I also hope to learn a lot as well.

**Chris Gammell:** Laura, can people follow you online anywhere? Are you, do you do Twitter or anything like that?

**Laura Abbott:** I do Twitter. I am on Twitter at Open Labbit. My first, first initial, last name.

**Chris Gammell:** Awesome. Well, thanks so much for telling us about this stuff. This has been a really interesting dive into servers and Oxide, the company and your work and your background. I just think it's been really good to learn about this kind of stuff. And we hope to have more security type things on the show in the future. So thanks for being here today.

**Laura Abbott:** Thanks for having me.
