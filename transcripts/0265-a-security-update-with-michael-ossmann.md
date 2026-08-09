---
episode: 265
title: A Security Update with Michael Ossmann
url: https://theamphour.com/265-a-security-update-with-michael-ossmann/
---

**Michael Ossmann:** This is the F-Hour Podcast, recorded September 2nd, 2015. Episode 265, a security update with Michael Ossman.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Michael Ossman of Grey's Got Gadgets.

**Dave Jones:** For our regular security update.

**Michael Ossmann:** Regular security update? Is this a regular thing now? It's semi-regular. Yes, sir. Quasi-regular. Was I supposed to do homework for this? Yes. You were supposed to attend a crap load of security conferences and tell us what's hot and what's not. And what's going on. Oh, okay.

**Dave Jones:** I think what really happened is that Chris was looking around for someone to have on. And Mike just happened to be standing there. No way, man. Get on. Get on.

**Michael Ossmann:** I've got an email string from like four weeks ago. So I've been wondering about this stuff. It was four weeks ago that I was short on guests. And Mike couldn't do it. And Michael's going, no, not me. Not again. No.

**Chris Gammell:** Yeah, he emailed me right when I was in the middle of the horrible month of conferences.

**Dave Jones:** Tell us about the horrible month of conferences. Where did you go?

**Chris Gammell:** It was actually a wonderful month. Right. A wonderful month of conferences, except that they all were in the same month.

**Dave Jones:** Please make me entirely jealous, because as we were talking about before the show, I get to go to one conference a year.

**Chris Gammell:** Oh, yeah. Yeah. So I did like six or seven events in one month, which was kind of stupid. But they were really good events. I went to Black Hat and B-Sides and DEF CON in Vegas. And I went to...

**Dave Jones:** And those three were in Vegas?

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** They're all in the same week.

**Dave Jones:** Oh, right. Okay. Well, that makes it easy. Yeah. Okay. Right. I thought you were like touring the world, you know.

**Chris Gammell:** No, no, no. And I get there early to teach four days at Black Hat. So I end up being in Vegas for way too long. Yeah. Turns into like fear and loathing. Right. Yeah. Yeah. A lot of cool stuff happened there, though. I mean, tons of great research was presented. Cool. Excellent. And then I was at Usenik's Woot, the workshop on offensive technology.

**Dave Jones:** Offensive technology? Sorry? Yeah. Offensive. Yeah. As in offensive hacking. Right. Not like offensive like Dave. Offensive. No. Yeah. Exactly.

**Chris Gammell:** Right. Offense. Offense versus defense. And that's a wonderful little academic conference in the security, in the academic security community.

**Dave Jones:** Well, tell us what these offensive things are. What constitutes an offensive technology? Well, any kind of. Hack technology.

**Chris Gammell:** Any kind of active attack. A hack on some software or hardware as opposed to.

**Dave Jones:** I thought that's pretty much everything. Every hack, isn't it? Every hack's offensive, isn't it?

**Chris Gammell:** Well, it depends. I mean, the hacker community, like going to DEF CON, for example, has been focused on attack tools and techniques for many years. But the academic community has been focused primarily on defensive research. Right. And so this is sort of a unique conference. Well, it's really a workshop within a larger conference. But it's a unique event in the academic community that it is totally focused on attack research as opposed to defense research.

**Dave Jones:** So this is purely academic. This is like, you know, university professors turning up. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And giving their death by PowerPoint presentation.

**Chris Gammell:** Exactly. But I thought that they were some of the best presentations that I saw all month, actually, were at Usenix Woot.

**Dave Jones:** So do you have to be a professor? Like, do you have to be a researcher to do that? Or can you just be a one-man band in your shed doing research?

**Chris Gammell:** You can be a one-man band in your shed. But you do have to submit a paper. Right. Of course. Yeah. I did not submit a paper. I just got invited to do a talk. He's special, folks. Yeah. He does a security update, Dave. Come on. Right.

**Dave Jones:** On the air power. Of course. He's famous. Yeah.

**Chris Gammell:** That's clearly why.

**Michael Ossmann:** Is this hardware and software at this? I mean, I know that DEF CON has Hardware Hacking Village and Black Hat does because you do that thing there. But is Usenix Woot as well? Is that a... Yeah.

**Chris Gammell:** It's both hardware and software, definitely. Okay. There was an interesting car hacking talk there. And there was something on... There was some stuff on like RFID systems, NFC security, and all kinds of interesting stuff that was actually hardware related.

**Dave Jones:** The car thing was a big deal recently, wasn't it? Because the Chrysler... Was it Chrysler? Jeep? Hack? That was one of them. That made them recall it, didn't it? Oh, made them... Yes. Yes. I actually predicted that. Everyone said... I put that on Twitter. I said they'll have to do a recall. Everyone went, no way. Won't happen. I was right. Thank you.

**Chris Gammell:** They finally did a recall. I think it was 2.5 million vehicles. Wow. So it was a big recall.

**Dave Jones:** It's just like a firmware update though, right? They just bring it back in and plug in the cable and Bob's your uncle, right?

**Chris Gammell:** Yeah. That's correct. Right. And in contrast that with another interesting car hack that was published in Vegas that was on Tesla. And Tesla, before the talk even happened, pushed out an over-the-air firmware update to fix vulnerability in every single car. So they didn't have to do a recall.

**Dave Jones:** But ironically, that is a potential way in for hackers, that over-the-air thing. So it's like... Right? So...

**Chris Gammell:** That is absolutely true.

**Dave Jones:** So what's your gut feeling on that? Is it better to implement these things in hardware or is it better to implement them in software and have cloud updated and all that sort of stuff? What's your...

**Michael Ossmann:** Do you mean like firewalled versus non-firewalled? Yeah.

**Dave Jones:** Well, like, yeah, physical hardware. You're gapped. Like, there is no link between the CAN bus and the internet gizmo in your car kind of thing. Like, there's no physical connection. Can't happen.

**Chris Gammell:** Yeah. Well, unfortunately, I think that ship has sailed. Right. I mean, this debate was happening, you know, internal to the automakers probably 10 years ago. Right. And the cars that are getting exploited today are ones that have already shipped and were designed at least five years ago, you know?

**Dave Jones:** Right. And they couldn't do remote update.

**Chris Gammell:** Well, most of them couldn't.

**Dave Jones:** Right.

**Chris Gammell:** No, I think the only automaker that is doing over-the-air updates is Tesla.

**Dave Jones:** Right. But...

**Chris Gammell:** And in general, I think that's a good way to go. I mean, there are obvious pros and cons, as you point out. But there are always going to be new vulnerabilities discovered in any sufficiently complex piece of software. And we are driving...

**Dave Jones:** Is indistinguishable from magic. Yeah.

**Chris Gammell:** That's right. We are driving, you know, rolling pieces of software. Right. So, it's just inevitable that there are going to be problems, both security-wise and also reliability and safety. And those things...

**Dave Jones:** That's why...

**Chris Gammell:** They need to be fixed as fast as they possibly can.

**Dave Jones:** That's why I would err towards the hardware. Because ultimately, yeah, okay, the Tesla's doing the, you know, over-the-air updates. Okay. But what's to stop anyone hacking into that system and doing their own updates? I mean, it's just an encryption thing that's stopping them.

**Michael Ossmann:** Right? Hear that, Mike? It is. It's just an encryption thing. An authority thing, right?

**Dave Jones:** I mean, come on, right? All you have to do is... You know what I'm talking about? Dave sees movies.

**Michael Ossmann:** You just go clickety-clickety-clack on the keyboard. And then stuff happens on the screen. And boom. Well, I mean...

**Dave Jones:** I've seen 24. I've seen what Chloe can do. Come on. It's too easy.

**Chris Gammell:** Well, you know, encryption is hard to get right. And we've seen all kinds of things that appear to be secure systems deployed. And then somebody pokes a hole in them sooner or later.

**Dave Jones:** Which is why I'm arguing just take it out of the loop.

**Michael Ossmann:** Yeah. Well, but I think that's a design constraint, though, right?

**Dave Jones:** I mean, you think about... And it could be a selling point in your car. No, I don't think so. And my one is not. It's so secure.

**Michael Ossmann:** No, think about the fleet of people you need to maintain, then, in the event... Like, do you know how... I mean, like, recalls are... It's much better to say, okay, well, we can update it later. And it's, like, versus maintaining a workforce or having a recall.

**Dave Jones:** But you don't have to maintain it if you engineer it properly. If you engineer it properly from day one, hardware doesn't change.

**Michael Ossmann:** If you engineer it properly, the OTA works. That's the thing, though. Like, that's what's... I mean, like, that argument always works. Like, oh, if it's perfect, it's perfect. But the OTA...

**Dave Jones:** But the over-the-air is always hackable. Always, by definition. By definition. Oh, yeah.

**Michael Ossmann:** ODB2 ports are accessible, too. Like, why couldn't someone just go in there?

**Dave Jones:** But physically, there's a... No, there's a huge differentiation between physical attack and software over-the-air attack.

**Chris Gammell:** There is, absolutely.

**Dave Jones:** Massive difference, Chris.

**Chris Gammell:** And this is one of the biggest kind of headlines about some of the recent car hacking, in particular, the stuff done by Chris Valasek and Charlie Miller on the Jeep and the Chrysler vehicles, is that they published some research a couple of years ago on how they were able to totally take control of a Toyota via physical access. They actually plugged into the CAN bus and showed how... Or do. All these different subsystems in the car, once you gain a foothold, all these different subsystems in the car are vulnerable. And a lot of people kind of poo-pooed that research and said, well, big deal. You had physical access. That's not that exciting. We don't really care about that. And so what they did was they kind of said, well, let's go back to the drawing board and figure out how we can demonstrate the same thing, but with a remote attack where we're anywhere over the internet and we can attack a car. And that's exactly what they did with the Jeep hack.

**Dave Jones:** But they found the only car that was probably vulnerable to that, one of the very few.

**Chris Gammell:** Well, they found 2.5 million vehicles that are vulnerable to the same flaw.

**Dave Jones:** But out of how many model cars are on the market, hundreds and hundreds and hundreds, they happened to find the one that had this vulnerability through the audio system or something. I don't know.

**Chris Gammell:** It was through the infotainment system.

**Dave Jones:** Infotainment system, yep.

**Chris Gammell:** Yep. And so this was a case where I think most people, certainly people in the security industry, understand that this isn't the only vulnerability that exists in cars. It's just the one that they happen to find and publish. And it's an excellent example to everyone to show that these cars are interconnected and they are vulnerable to attack from the outside world over the air, over a network. Because they were poorly engineered. Arguably, yeah. Once somebody gains a foothold, then they can get access to control of the entire vehicle. And that's only going to get worse, most likely, as cars gain more drive-by-wire capabilities. Well, will it?

**Dave Jones:** Because they're so aware of it now. Will they engineer them better? It could get better.

**Chris Gammell:** That's an excellent question. But the development life cycle for cars is so many years. Yes. And the cars that are being engineered today or that were engineered last year aren't going to hit the market for a while. And they're already far more complex with more software, more lines of code, more microcontrollers than the ones that people are looking at and driving today.

**Michael Ossmann:** Scary. So could you explain what you mean by foothold? Because I'm not sure I understand that term.

**Dave Jones:** You haven't watched enough movies, Chris. I guess not.

**Michael Ossmann:** We can go over the list of movies I should watch after the actual explanation.

**Chris Gammell:** Just watch Sneakers. It's the only one you can do. I've seen that one. Love Sneakers. So basically, a car is a network of computers. There might be as many as 200 Turing machines inside your car. And because every single little subsystem in the car has its own microcontroller doing something. And they're all interconnected on a network. So it's kind of like attacking a car is kind of like attacking a corporate network of PCs. And if you can get one person to click on your malicious email, then you might be able to take over that one PC. And once you're there, that's your foothold into the internal network. I see. And you can gain access to other parts of that network. It's the exact same thing in a car. You can gain access to the Arnstar system or the entertainment system. Sorry?

**Dave Jones:** What's that? The Arn?

**Chris Gammell:** One of these remote telemetry and control systems.

**Michael Ossmann:** They have like assistance. Like assistance. Like you can push the button. And they used to give you directions before the mapping programs were out there. That kind of thing.

**Dave Jones:** Sorry, my car's not that advanced.

**Chris Gammell:** Or you could gain access via Wi-Fi, for example. And because a lot of cars have Wi-Fi these days or by Bluetooth or, you know, there are all kinds of different ways that you could potentially gain access to one subsystem in the car. And once you have that, it turns out that pretty much every car is a fairly open network. Or it might be architected so that there are two or three fairly open networks that are somewhat isolated from each other. But it doesn't take much to, generally speaking, it doesn't take much to go from a foothold or control of one device on that CAN bus to gaining access or control over many devices on that CAN bus.

**Michael Ossmann:** Right, because if you get onto the bus, then you could like start putting things into like, oh, well, you should load up new firmware, you know, brake system. And then you push that new firmware system. Then you have control of the brakes. And the brakes take over the windshield wipers. And the windshield wipers take over the engine timing. Exactly. That would be terrible if that was actually the order of things happening. But we have the best windshield wipers in the world. These are so intelligent.

**Chris Gammell:** Well, and the internal network is so wide open or so lacking in security controls because, I don't know if you've ever looked at CAN bus, but it's just a dead simple protocol. It's not much different than like a spy bus. You tug at a line and then you're in control.

**Dave Jones:** If you've got physical access to that line, bam, you're in.

**Michael Ossmann:** Well, that's scary. I was listening to the Tested podcast a while back and they were talking about, you know, they're not worried about the T-1000 or anything like that. They're worried about autonomous cars and then someone having access to the whole fleet of network connected autonomous cars. And then you think about how many people that could hurt at once. And like, of course, that was a doomsday scenario. But, you know, it's even just one is a tragedy, right? It is. And like you said, as cars go more and more towards the drive-by wire, moving away from, you know, physical controls, if your brake doesn't actually push on the hydraulic fluid to actually, you know, close the brake pad anymore and it's controlled by a computer now, you can really be in some shit, you know?

**Chris Gammell:** And we've seen a little of this already. You know, we've seen the dark side of what can happen to some extent with the Toyota unintended acceleration incidents.

**Dave Jones:** Did they finally admit that? I don't think they were a little while.

**Chris Gammell:** That's expensive to admit that. Right.

**Dave Jones:** I didn't, yeah, I didn't get the final lowdown on that.

**Chris Gammell:** But there was a court case in which Toyota was found negligent. Right. In a case of unintended acceleration that featured testimony and analysis, software analysis and embedded system analysis by Michael Barr. Yeah. And he did a wonderful job. I highly recommend looking at his, at the information that he published after that case about the research that he did on figuring out the software flaws that were very easily, you know, he couldn't prove. And no one could prove that these software flaws were the direct cause of this one incident.

**Dave Jones:** I find that amazing that they couldn't prove it. Can't they just order them to hand over the code and then analyze it? Like, it's not fuzzy logic here. It's, you know, it's like code executes in certain ways. Yeah.

**Chris Gammell:** Well, but there are so many different conditions. There's so many different possible input states that you can't fully recreate necessarily. All the states that were.

**Dave Jones:** Okay.

**Chris Gammell:** The state of the system at the time of the accident or something. But you only have to prove one case.

**Dave Jones:** You only have to find and prove one case. That's it.

**Chris Gammell:** And he proved more than one case. He proved very clearly that there were software quality issues that could cause the exact problem that happened in this accident. Right.

**Dave Jones:** So this is in the acceleration control computer or whatever it's called?

**Chris Gammell:** I can't remember exactly which system it was. If it was in the engine control unit or one or two other systems. But it's highly educational. I definitely recommend anybody involved in embedded systems check that out. Yeah. Yeah. Definitely. Let's try to remember to get that into the show notes. Because it shows exactly what can happen when software goes bad. And the automakers have a long history of reliability testing. And they think they know how to test things for reliability. But the problem is they know how to test hardware for reliability. They're having to learn the hard way how to test software for reliability. And it's a much, much harder problem.

**Dave Jones:** Well, that's always the curse of R&D, trying to test your own stuff. You know? Like, it's hard. The best thing you can do is simply give it to the crowd, you know? And, right? Here you go, Grandma. Like, I take my scope, right? I take my scope and give it to my four-year-old, right? And he'll play around with the scope. And he'll put it in modes that I didn't even think existed. That you could possibly put this scope into, you know? Because he's just playing around with the thing. It's incredible. So, yeah. Yeah. You can't beat crowd testing. Passionate crowd testing.

**Michael Ossmann:** Baby testing, really. Right. Yeah. Or toddler or whatever, you know?

**Dave Jones:** Monkeys bashing on keys, you know? That's right. Exactly. I mean, yeah. Yeah.

**Michael Ossmann:** That's a good point. I mean, it is hard to, especially when you are plotting out, you know, you have to have scientific method around, well, we tried A and the result was B. And, you know, that's what we're going to try. And now we go to C.

**Dave Jones:** You always miss something. You always miss something.

**Michael Ossmann:** Right.

**Chris Gammell:** Well, clearly Toyota should let some toddlers loose on their cars for testing. That's the obvious answer here.

**Dave Jones:** So, there is, like, one vulnerability I'm particularly concerned about on the car front is that, you know, you might have some system hooked onto that CAN bus. It might be secure in its own respect, right? But then somebody who actually comes in and re-, like, they might re-flash that thing, either remotely or via some other method and bam, you know, and otherwise safe, you know, thing, be it the entertainment system or be it the, you know, the air conditioner controller or whatever, you know, because they're all micros. There are hundreds and hundreds of micros in a modern car. Yep. So, you can go through any one of them. You know, the flat tyre sensor has a micro in it, you know, and it hooks onto the bus and it reports back. Right? All you've got to do is, you know, put a wheel on there that has that low, you know, that has a hacked sensor in it, you know, and bingo, it's got access to the bus.

**Chris Gammell:** Yeah. And actually, the tire pressure monitoring systems are one of the more interesting systems from a security and privacy standpoint these days. Tell us why. Well, you've got four sensors, one in each tire, and each one is independently transmitting periodically a radio signal to a centralized controller. I mean, radio is the easiest way to get information out of a…

**Dave Jones:** On a moving wheel, yeah. Right.

**Chris Gammell:** Out of the inside of a moving wheel.

**Michael Ossmann:** The wire keeps getting twisted up every time we put it on there.

**Chris Gammell:** Exactly.

**Dave Jones:** How do they get power for that? Is it like there's an energy harvesting thing there that…

**Michael Ossmann:** No, I think they just have a battery that runs for years. Oh, right. Really? Okay. I remember my mom used to get signals and they'd be like, yeah, you just got to replace the tire sensor. And it's like, that's kind of a crappy design. So, we just never knew if our tires were flat, which is the same as every other car after that, you know.

**Chris Gammell:** Right. Yeah. And these tire pressure monitoring systems, they transmit a unique ID and the pressure and temperature of the tire. And then there's some controller inside the car that's a receiver that gets that information and interprets it and like can tell you if you have a tire that's low and it can tell you which tire is low. And assuming that they were enrolled to the car properly. And it can also do like a flat tire detection or like if you have a blowout.

**Dave Jones:** It's pretty bloody obvious that you've got a blowout. Why do we need a freaking sensor to tell us?

**Michael Ossmann:** What is that noise? Why am I pulling off to the right? Something's wrong.

**Chris Gammell:** Yeah, I think it's primarily so that that blowout information can get stored in a black box or transmitted via telemetry system.

**Dave Jones:** Right, right. So, if you crash and kill somebody, they can get the data and go, yep, okay, it wasn't your fault. The tire burst, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** I've looked a little bit at some of the tire pressure monitoring systems myself and I haven't found any place where it looks like it could be exploited to like gain arbitrary control, like send arbitrary CAN bus messages or gain control of a computer.

**Dave Jones:** Oh, you're talking about the control. I was going to say, is that just because it's a receiver and that's it? And it's just, you know, it ignores everything else except the tire pressure level or whatever?

**Chris Gammell:** Yeah, that's basically true. And also because it's a very simple receiver. Right. Every case that I've looked at, the packet format of these tire pressure monitors is very fixed and it's like a fixed number of bytes and it's a very small number of bytes and there isn't much there. It's not like the tire pressure monitor is transmitting a complete CAN bus packet, for example. So if the tire pressure monitor were transmitting a complete CAN bus packet, then that would be a huge avenue of attack.

**Dave Jones:** Massive, yeah.

**Chris Gammell:** But I haven't found any that do that kind of thing.

**Dave Jones:** All you need is someone from the government to come along and just while you're inside just secretly change your tire and bam, that's it. They're in. They can, yep, cause your car to crash and, yep, oh, you had an accident. Oops.

**Chris Gammell:** Yeah. Well, and it might be possible. I mean, I don't know, especially as we get into more self-driving cars or at least assisted driving, it might be possible to really mess up somebody's vehicle on the highway by spoofing a tire and making the car think that it had a blowout.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. I don't know.

**Michael Ossmann:** I would think it'd be easier to like overload sensors and stuff like that. Like, I mean, I'm sure they test for that stuff, but like thinking, you know, like how a lot of cars are doing like avoidance type stuff. So it'll help you swerve out of the way if it senses there's something there. You know, just faking that thing out. That would be probably the biggest, the easiest way to do that. You know, you know what, I mean, basically you roll a ball in front of a car or something like that and then you just put a barrier next to it. And I don't know.

**Dave Jones:** Why not go the whole hog and just want to use one of those EMP pulse generators like they use in Ocean's 11, you know, when he switches it on and he...

**Chris Gammell:** A pinch.

**Dave Jones:** A pinch. That's it. Right.

**Chris Gammell:** Yeah. Our cars are getting highly vulnerable to those things. I mean, heck, even cars from late 20th century were vulnerable to something like that, potentially.

**Dave Jones:** That they're solar flare vulnerable because that is a modern day disaster scenario that is seriously waiting to happen. Right? Yeah. I mean, you know, I think, was it back in the 30s or something? Solar flare took out the entire power grid in like 10 countries or something. You know, it's like... Yeah. Are they safe because they're shielded inside a car and they haven't got big loop areas in them? They're all tiny surface mount stuff? I don't know. What's the...

**Chris Gammell:** That probably helps. It also helps that cars are so electrically noisy inherently that the electronics inside cars are pretty well engineered against, you know, pretty big electrical pulses. Yeah, load dumps.

**Dave Jones:** They're all pretty much in die-cast boxes, aren't they? Every one of these little controllers I seem to see in a car is like die-cast box.

**Chris Gammell:** Yeah. They're pretty well isolated and they're physically very reliable. So I would guess that our cars, even though they're getting more and more complex and more and more full of computers, I would guess that they're going to be less vulnerable to EMP than most of the other electronics we have in our lives.

**Dave Jones:** Like the lights, like the traffic lights. So you'd probably have more accidents if there was a huge solar flare event or someone let a nuke off nearby or something that, you know, yeah, all the traffic lights go down suddenly.

**Michael Ossmann:** Maybe other problems if someone lets off a nuke off nearby. Yeah, a nuke nearby, but, you know. Right. Yeah.

**Dave Jones:** It's talking technical here.

**Chris Gammell:** Boom. Park. Yeah. But I think the first things to go would be your cell phone and your laptop and all your internet access. Face maker.

**Dave Jones:** Oh, no. Our entire lives are running. The internet, not the internet.

**Michael Ossmann:** So, Mike, what are some other trends you're seeing? I mean, you were talking about cars. Obviously, that's big. Are there other big talks about, you know, other trends and stuff that you saw? Yeah.

**Chris Gammell:** Yeah. I mean, one of the biggest trends in the security industry right now is actually more of a focus on hardware.

**Michael Ossmann:** Oh, yeah?

**Chris Gammell:** And, I mean, there's a whole new conference coming up that I mentioned before the show, hardware.io, H-A-R-D-W-E-A-R.io. That's coming up. And it's just another sign of the times that so many people in the security industry are focused on hardware and are focused on embedded systems, really.

**Dave Jones:** Are we talking about consumer hardware here?

**Chris Gammell:** Yeah. Well, consumer and also industrial and, you know, any place there's an embedded system, there's a potential security problem. And we're seeing a lot of cases where, let's say, the auto industry is a good example. But there are many, many other industries where any industry that makes any physical good is going through a change right now. They're somewhere along this curve of putting microcontrollers into their physical good, right? Well, one of the big ones is smart TVs.

**Dave Jones:** Smart.

**Speaker ?:** Yep.

**Dave Jones:** Everyone is complaining. There are – there's a new movement going, I will not have a smart TV because the government is going to be monitoring me through the camera and the microphone and blah, blah, blah. You know, like there's a huge backlash on smart TVs for that.

**Chris Gammell:** And there was some wonderful research presented a couple of years ago on smart TVs and how, like, based a hacker from South Korea did a wonderful demonstration with a Samsung smart TV where he was able to, you know, remotely take over the TV and run his own code on it and attack other posts on the network from that TV.

**Dave Jones:** I was going to say because it's hooked onto your Wi-Fi network.

**Chris Gammell:** Make you watch the Kardashians.

**Dave Jones:** You're right.

**Chris Gammell:** It could potentially interfere with what you're watching. But the more insidious thing that he was able to do is operate a camera and microphone. Yeah. And what made it particularly insidious is that he was able to power – make the TV look like it was being powered off without actually powering it off.

**Dave Jones:** Oh, and still operating the mic and camera.

**Chris Gammell:** Exactly. Wow. Yeah, security monitoring effectively. Wow, that's a nice hack. Yeah. Yeah. Wow. Yeah. And, you know, since that happened, I don't think it's really gotten any better. There are just more and more smart TVs coming out every day. And there isn't anyone doing comprehensive security audits on all of them and publishing their results. So, it's a dangerous thing, I think, putting one of these smart TVs in your home. There you go, folks. I do not – Yeah. I do not fault people who would refuse to buy one. It's definitely a concern. I mean, honestly, I've unplugged them myself when I find them in a hotel room.

**Dave Jones:** Really? Interesting. Yeah. Yeah. Oh, okay. Right.

**Chris Gammell:** I just unplug them from the wall. Just because – I mean, it's one thing to have one in my own home and under my own control. Right. Yep. If I'm hacking around on it or something. But one that's, you know, that I've never seen before that's just in my hotel room pointed at my bed. I don't really –

**Dave Jones:** That's interesting. I don't really want to – Do you find yourself – I don't want to use the word paranoid, but you're aware. You're security aware. Yeah.

**Dave Jones:** Do you find yourself doing that for other things or what?

**Chris Gammell:** There's definitely a fine line between security aware and paranoid.

**Michael Ossmann:** You know, Mike, there's people listening to you right now. I don't know if you knew about that. No.

**Chris Gammell:** I may be a little more paranoid than most, but probably not any more than most other folks in the security industry. You know, I just think of it as being sensible. If somebody's – if there's a – if I walk into a room and I'm going to be spending a lot of time in that room on my own, it's my own private space. And there's a computer with a microphone and a camera just sitting there plugged into the wall. And I'm not planning on using it. I'm just going to unplug it.

**Dave Jones:** Oh, interesting. Okay.

**Chris Gammell:** It's easy. It's safe.

**Dave Jones:** So I'm just sitting here wearing this tinfoil hat. No, I'm not crazy. I'm just being sensible.

**Chris Gammell:** Yeah, exactly. Even on my laptop. I mean, and I'm pretty confident in the fact that nobody is running malicious code on my laptop. But even though I'm pretty confident about that, I still have a Band-Aid taped over the camera.

**Dave Jones:** Wow. Okay. Because I never use the camera. As somebody who sits here in a lab with people watching me 24-7, it's like –

**Dave Jones:** It's like care factor. Well, that's a little different.

**Chris Gammell:** Zero. Yeah. Yeah. But, you know, I never use the camera. And if I did, then maybe I wouldn't bother covering it over. But it's one of these things where why would I bother – why would I make that available if I'm not actually going to use it?

**Dave Jones:** Yeah. Okay. Fair enough. Tinfoil hats for everyone, folks. Maybe we can have the official Ampour tinfoil hat.

**Chris Gammell:** Oh, that would be excellent. That would be a great idea.

**Dave Jones:** So does anyone turn up to these conferences with a tinfoil hat? That would be hilarious. I have actually seen that. You have?

**Chris Gammell:** Awesome.

**Dave Jones:** Yes. Photos or it didn't happen? It does happen.

**Chris Gammell:** A photo? I don't think I have a photo.

**Michael Ossmann:** But, no, this is a thing. They get cranky at DEF CON when you take photos. In your show bag. Oh, yeah.

**Dave Jones:** Oh, really? So maybe in your show bag you get a tinfoil hat one year. Oh, that would be good. Yeah. That would be great.

**Chris Gammell:** Hey, we should make something like Teespring but for tinfoil hats.

**Dave Jones:** Oh.

**Chris Gammell:** Branded for your corporation. Yeah, exactly.

**Dave Jones:** I've got an idea. Okay. All right. I'm going to implement it after the show.

**Chris Gammell:** It would be great to have it like an NSA-branded tinfoil hat. That would be great.

**Michael Ossmann:** What's this microphone-looking thing on here? I don't get it.

**Dave Jones:** Oh, boy.

**Michael Ossmann:** Well, so speaking of, I mean, I think Dave said something about a badge as well. We should mention that, so you were at another conference and, well, you should just tell us about the badge because we mentioned it on the show. But tell us all about it.

**Chris Gammell:** Oh, yeah. The radio badge at Chaos Camp. It was amazing. And this was one of the events I went to within the last month. And it was the Chaos Communications Camp in Germany. About 4,500 people. I think it was close to 5,000 people. Wow. All camping in a field.

**Michael Ossmann:** Nerds in tents. Yeah.

**Chris Gammell:** Nerds in tents. It was a lot of nerds in tents. It was a really good time. And the Munich CCC group brought badges for everybody. And they designed this thing, the radio badge. It's spelled R-A-D-1-O. Radio badge. It's kind of designed to look sort of like an AM, FM radio or something like that. And it was actually based on my HackRF1 design. So they gave, they made 4,500 of these. Wow. Gave them away to all these hackers in the field. 4,500 HackRFs. Wow.

**Dave Jones:** How much did they cost to pop?

**Chris Gammell:** It was amazing. So it turns out that they were able to get some significant sponsorship from chip vendors.

**Dave Jones:** Oh, nice. Yeah.

**Chris Gammell:** So for this event. And they were able to, thanks to that sponsorship, they were able to reduce the cost down significantly to the point where they could just roll it into the cost of the camp. Wow. Terrific. And give one away to everybody. Yeah, it was tremendous. And they had to, they had to redesign a few things on the board because they were designing around.

**Michael Ossmann:** Yeah.

**Chris Gammell:** They were designing around the parts that could get donated. Exactly. Yeah. So, you know, there were a few things that when I looked at the design, I was like, why in the world did they do that? And then I realized, oh, it's because they got a chip from this certain vendor.

**Michael Ossmann:** Yep. Use what you got, folks. Yeah.

**Chris Gammell:** Yep. So they did a great job of making that happen at a low cost and giving it away to everybody and kind of promoting software-defined radio in the community, you know, more than I had ever been able to. And like when I first did the HackRF project, when I, when I really started working on the HackRF project and I started working on the, the beta board, which was called Jawbreaker, my original plan for Jawbreaker was to make about 500 of them and give them away to a bunch of hackers in a field. And that was, that was the plan. We were going to do it at Tour Camp in the U.S., which is a, you know, a smaller hacker camp. But due to being behind schedule, we weren't able to actually accomplish that goal. We did make 500 Jawbreakers, actually about 600 Jawbreakers and give them away to people, which was great. But we didn't get to give them away to people who are all in the same place at the same time. And I missed, I missed out on actually making that happen and experiencing that. And so thanks to the Munich CCC crew, I was able to actually finally experience that 10 times the scale and walk around and talk to people about, about what they were doing with the radio badge. And it was amazing. It was a pretty incredible experience.

**Michael Ossmann:** I wonder about that because I've seen, you know, I went to DEF CON, I saw you there a little bit last year. But, you know, that's a much bigger and the badge has stuff, but there's not really, and some people do badge hacking, but I didn't really see too much, like in terms of the scale. And so like, what were people doing and how, like, what percentage would you say?

**Chris Gammell:** So, you know, obviously there are a lot of people who get the thing and don't do anything with it. And hopefully those people will go back after the, after the camp and, and try them out or loan them to a friend who wants to play with it or something, or donate them to their local hacker space. Somehow, you know, get them to somebody who's, who wants to play with them. But there were a lot of people there at camp who were, were working with them and trying new things. There were people who had downloaded my, my instructional videos and were using the radio badge to go through the exercises that are in my videos. There were people who were writing firmware for the badges to do all kinds of fun stuff. Awesome. A little bit of hardware hacking, but I didn't see a whole lot of that. There were some unpopulated components on the board, just like LEDs and stuff and, and LEDs and like a external antenna connector. So a lot of people were soldering, they were soldering on either the antenna connector or they were just soldering on temporary antennas.

**Dave Jones:** Where do they get the power from at these camps? Does everyone bring their own generator or is it one of these powered camp site things?

**Chris Gammell:** They had some very large generators. Right. To power the entire camp.

**Dave Jones:** So that's supplied by the event, is it?

**Chris Gammell:** Exactly.

**Dave Jones:** Right. And everyone could just plug in with a million power boards. Camping? Is that right?

**Michael Ossmann:** Is there, is there, is there, I know there's glamping, which is glamorous camping. Is there like mamping, like for nerd camping where you need to have power and internet?

**Dave Jones:** Wi-Fi and everything. Yeah.

**Michael Ossmann:** Mamping. Why aren't we just at a hotel?

**Chris Gammell:** Exactly. What was going on? Well, I love it. You know what? I think this might have been my favorite event that I've ever been to. Just, and part of that, of course, is influenced by the fact that the radio badge was such an amazing thing for me personally to see come to fruition. But part of that was just the camp itself, nothing to do with the radio badge. I'm sure. You know, I'm not sure that I had any German beer at the camp. But there was alcohol, definitely. And there was plenty of Klubmata. And there was just a lot of really cool, interesting installations, like light shows and stuff. And people doing interesting projects and giving talks about all kinds of cool stuff. And just nerdery all over the place. It was amazing.

**Dave Jones:** It makes me want to, like, run one.

**Michael Ossmann:** Oh, yeah.

**Dave Jones:** Here in Sydney.

**Michael Ossmann:** Chaos Communications Camp, Australia. Now with more spiders and drop bears.

**Dave Jones:** Should I run my own or should I franchise the Chaos Computer Camp? Is it franchisable?

**Chris Gammell:** I don't think it's franchisable exactly. But, you know, what you should do is just come to one of the hacker camps on some other continent and see how it goes. Either come to the Chaos Camp or come to Tour Camp in the U.S. or EMF Camp in the U.K. Go to one of these hacker camps and see what it's like. Because I personally find that these are some of the best events that I go to. I like them a lot more than the conferences that are in hotels and stuff.

**Dave Jones:** Yeah, at the exhibition centers. And, yeah.

**Chris Gammell:** There's something special about camping with all these people. And even if it's not quite your traditional idea of camping. Like at Chaos Camp, for example, I didn't bring any food. I bought food from food vendors while I was there.

**Dave Jones:** Oh, they got vendors. Well, with 5,000 people, yeah. Exactly. I'm sure the vendors would show up. You know, if I ran one here, yeah, we might get five people to show up.

**Chris Gammell:** So, basically, I just showed up with a tent and a sleeping bag. Actually, I just showed up with a sleeping bag because somebody offered to loan me a tent. So, you just show up with a tent and a sleeping bag in your laptop. And it's amazing for one reason because it's so affordable. Everybody camping in a field is way more affordable than everybody staying in a hotel room.

**Dave Jones:** Yep.

**Chris Gammell:** Totally. And so, you're able to get – it's very, very inclusive. Anybody can show up at this camp. And it's also 24-7. So, like a lot of the most interesting conversations that I had were after dark. And earplugs are pretty much required.

**Dave Jones:** Come on, take a look at this. Come on, 2 a.m. in the morning. Come on. Step into my tent. Come on.

**Chris Gammell:** Right.

**Dave Jones:** Yeah.

**Chris Gammell:** I mean, I was soldering on things and hacking on things and talking to people about their hacks and stuff, you know, well after midnight. Every night while I was there. And a lot of the stuff, a lot of the interesting installations that people have are like lighting displays that only operate at night. Of course. So, it's very much focused on the nighttime. And you just get kind of a different community feeling from folks that you're camping with, even if it is a bit of a non-traditional camp. So, I think they're great events.

**Dave Jones:** Is it mostly like hacking type stuff or is it being taken over by the makers in quote marks?

**Chris Gammell:** I would say that it's a pretty, pretty strong mix. But the security focused people are, I would not say are the majority.

**Dave Jones:** Oh, okay. Right. Yep. As opposed to a lot of the conferences. I wouldn't have imagined with 5,000 people. No, I wouldn't. I thought it'd just get more, it'd just be a popular thing and like you'd just get makers turning up with their flashing LED lights there. You know.

**Chris Gammell:** Yep.

**Dave Jones:** Right. If I'm running one, should I?

**Michael Ossmann:** You put a nugget in Dave's head now. Yeah, yeah. This isn't good.

**Dave Jones:** Should it be focused like that or should it be, you know, come one, come all, you know, kind of thing or, you know, no, you've got to bring a hack.

**Chris Gammell:** I think making it less focused can be a good thing, personally. Right.

**Dave Jones:** Because then you get people that are interested coming in, make it open.

**Michael Ossmann:** Yeah, I think that's a good thing.

**Dave Jones:** Right. So, you'd rather call it like a maker event than a hacker event.

**Michael Ossmann:** Yeah, you could.

**Dave Jones:** Absolutely. Is hacker still a bad word? Is it like, you know, because. Not to me. They used to be hacker spaces, right? Yeah. And now, when they first started, now they're maker spaces, like they're rebranded, right?

**Chris Gammell:** Some have. Some have, yeah. But I think most that have called themselves hacker spaces continue to call themselves hacker spaces. Right. And.

**Michael Ossmann:** I think that's too much navel gazing, to be completely honest. I think like, who cares? You know, like. Right. I like these identities. It's like, you're worried about that. And meanwhile, all these people over here are like actually doing things. Why don't you just do what they're doing? Yeah, yeah, yeah. Right. I mean, like that's, that's the big thing. So, yeah.

**Chris Gammell:** Well, I know one of the things that I love about these hacker camps in general is that they are very inclusive. And that they have more of a focus on the community and on things like art projects. As opposed to the conferences that I go to that tend to be very focused on security only. And the camps, sure, there are people who are presenting interesting security work. But then there are also people who are just building stuff. There are people who are just teaching people how to solder. There are people who are making art installations. There's just a wide variety of people. And generally, those are installations are technological art installations, which is why you see a lot of lighting stuff. But it's very open and inclusive and more community focused than focused on any one topic.

**Michael Ossmann:** That's good. I like that. Yeah. I think the logistics on that stuff must be crazy. I'm very...

**Dave Jones:** Yeah, that's what I'm not looking at. It's just going through my head at the moment going, shit, how do I actually organize an event? Insurance, got to find a space. Is this camp like in a public reserve kind of thing or is it like a private?

**Chris Gammell:** This particular one is in a public space. Right. Okay. But I've been to camps that are in private spaces as well.

**Dave Jones:** I think a private might be easier to get approval for. You just pay somebody. We would love to use your farm, please. Exactly. And here's a couple of grand to use your farm, you know. Like, yeah. Rather than try and go through, you know, council, local council approval and, you know, national. But, you know, I've held it up in the mountains, you know, that'd be a fantastic place. But it'd be in a national or state park, you know. And it's like, oh, you know, can you imagine the red tape to...

**Chris Gammell:** Yeah. Especially in the US, I think that would be hard to do. Right. Whereas in Germany, I don't know, they make it work.

**Dave Jones:** Well, see, that's like, I go to all these obstacle course events, you know, one that, you know, these five, 10 kilometer, 20 kilometer, you know, mud obstacle events, right? They're always on private property because they just pay. It's easier, I think. Oh, definitely. And they're always on private landowner to, yeah, can we use your paddock, you know, and they just turn it into a mud pit. Right. You know, and it's just, yeah, you can't exactly do it in a national park.

**Chris Gammell:** We'll fill the holes in before we go, we promise. And that might be a great place to start if you're looking around for a location to host an event is look for places that have hosted other types of events like that.

**Dave Jones:** Yep. Yep. Yeah, because they'd be, you know, conducive to it. I'm motivated now. You were heard here first, folks.

**Michael Ossmann:** Dave is going to be sitting in the middle of a field with a soldering iron and a guitar on his knees singing Kumbaya.

**Dave Jones:** Kumbaya, that's it.

**Michael Ossmann:** And you know what? I will say this publicly. If Dave actually pulls this stuff together, I will fly out there. I will be there. And I hate camping. Oh, all right. Yeah. And I hate spiders. We know this.

**Dave Jones:** There you go. I'll be there. Chris has, great. Right. We're going to hold you to that.

**Michael Ossmann:** I would like to be there too, but I'm not sure I can commit to it.

**Dave Jones:** All right.

**Michael Ossmann:** Don't do it in the summer. Do it in the high summer. You don't want to sleep in a tent when it's, you know, 40 degrees C.

**Dave Jones:** It's spring here now, you know. Yeah, do it in the fall. That's what I mean.

**Michael Ossmann:** Do the fall. Yeah, perfect.

**Dave Jones:** Hmm.

**Michael Ossmann:** All right. Done. Anyway. So, Mike, what else? I mean, so that's really great, though, about that badge. I mean, I think that that kind of stuff, too. I remember with the Open Hardware Summit badge from two years ago, the Wyolham one, I saw that one kind of popping up in projects a couple times over and over because it's like an e-ink badge, stuff like that. Right. I'm sure that same kind of thing. It just kind of propagates. It's in the, not the junk bin, but it's on the bench. And it's like, oh, I could use this for this. And then it's just kind of there. Right. So, it should be interesting to see what happens with that.

**Chris Gammell:** Yeah. I hope we'll see similar things with the radio badge. Yeah.

**Michael Ossmann:** What about, so you mentioned the hardware conference, the hardware.io conference, and you said there's other ones as well. I mean, I'm always interested in this stuff because, spoilers, I'm kind of setting up one, first off. And I'm not going to talk about it here, but yeah, I'm stupid and setting up something. Nice. Excuse me. I got all choked up just talking about it because of logistics. But, you know, hardware doesn't really seem to have just hardware stuff. You know, you mentioned this hardware security conference, this new one. That's good. But what are some of even the other security ones? Because it seems like those are becoming more and more for hardware. Yeah.

**Chris Gammell:** Well, you know, some stuff that's coming up, of course, you just mentioned the Open Hardware Summit. That's coming up. All right. Yep. And there's an interesting hardware, open source silicon conference coming up. That's the OpenRisk. You guys have talked about the OpenRisk project on the show before. We have. They're making an open source microcontroller, basically, based on the RISC-V platform. And they aspire to be the first open source silicon product that actually, like, is available through traditional electronics distributors. It's a really exciting project. And they're having their conference, ORCONF. If you go to openrisk.io slash ORCONF, O-R-C-O-N-F. That's a conference that's coming up in October at CERN. And it's, you know, started by the OpenRisk group, but they're really trying to make it a more general event for anybody who's interested in open source silicon, which I think is super exciting. I would like, personally, as an open source hardware developer, I would like to have more components that I use be open source silicon. And I'm interested in maybe getting into open source silicon development myself. I think in the long term, it's an area that we as an open source hardware community need to go to. Yeah, I totally agree. So, that's an exciting thing that's coming up. Of course, there's...

**Michael Ossmann:** So, you're saying fewer black boxes in the little black boxes that we already use? Is that what you're saying? Yeah, exactly. All right. T-shirt slogan or something.

**Chris Gammell:** Yeah, fewer black boxes in my black box. Something like that. Yeah. I think you're onto something. Hey, maybe...

**Michael Ossmann:** Oh, no, we won't go.

**Chris Gammell:** Maybe... Can I get a custom tinfoil hat with that printed on it?

**Michael Ossmann:** Yeah, that's good. That's good. Yes. Yeah. Yeah. Folds back on itself.

**Chris Gammell:** Yeah, so those are some of the things coming up that I'm excited about. Of course, there are plenty of security conferences. I think the main one that I have on my schedule coming up is TourCon in San Diego. But, yeah, there's always... There's no TourCamp this year? Is that right? Not this year, no. But there should be one next year that's an every other year thing. Oh, okay.

**Michael Ossmann:** And is that the same thing for the Chaos Camp as well? Is that every other?

**Chris Gammell:** It's sort of every other. It's actually every fourth year. But then... Oh. But then there is also a hacker camp in the Netherlands that is every four years. And they're on alternating schedules. So every two years there is a large hacker camp in Europe. Cool. If that makes sense. Okay.

**Michael Ossmann:** Yeah. So 2017, Netherlands. Yeah. Sleep in a tent. Right. Sodder something. Yeah. Don't solder your tent. Yeah.

**Chris Gammell:** But next year there should be... Next summer there should be a TourCamp in the U.S. And there should be an EMF camp in the U.K. Those are the hacker camps that I know of that I expect to happen within the next year.

**Michael Ossmann:** Cool. So how goes the... You've been teaching... You've still been teaching all your SDR stuff. How's that going? I mean, are you still developing a bunch of new content for that and still teaching with the HackRF? Obviously with the HackRF. But like, is there a new HackRF coming out or a Dice show? What's the update on that stuff?

**Chris Gammell:** Yeah. So I've been teaching a lot. I haven't done as many videos as I would like to, but I'm still working on my online video series. And I should be able to get a new episode up this month, definitely. But I think I have nine videos so far. And I'm doing my two-day class a lot. And I've also done some private kind of advanced SDR classes for people who've already been through my two-day class and want to learn more. And those end up being fairly custom depending on the interests of the students. But that's a lot of fun. I just did one of those actually in Germany last week, which was my second trip to Germany this month, which is stupid. But don't do that. Yes. Yeah. Right. Yeah. So it's a lot of fun to talk to some folks who kind of accomplish some things with SDR and work on some more interesting projects, more esoteric things or kind of advanced concepts. And some of that will hopefully eventually make its way into my online video series as well. So it's kind of a good chance when I do those private classes to kind of develop some new content that I can later make available to everyone. But HackerF is going strong. I mean, the biggest news in the HackerF front lately, of course, is the radio badge at CCC. I heard a rumor recently that there's going to be a HackerF too, but I don't know anything about it. I don't know where this rumor came from.

**Michael Ossmann:** So it goes with open source hardware, I guess. Yeah. Yeah. Well, someone's grabbing that ball and running. Maybe.

**Chris Gammell:** I don't know. I mean, if I make a HackerF too, which is an if at this point, it's not a when. It's just a general concept that I have in my head that I've been talking to people about here and there privately.

**Dave Jones:** So it's a different concept or is it just a bigger, beefier HackerF one?

**Chris Gammell:** It's a slightly different concept. The idea with HackerF two, if if it does come to fruition, my my idea that I'm kind of leaning toward this point or my concept that I'm leaning toward is to take the radio that's in HackerF one and and keep it. Don't change it at all. And just change the digital back end section and put in a bigger, beefier microcontroller that can actually run embedded Linux and replace the USB interface with a gigabit Ethernet interface and support power over USB. Sorry, power over Ethernet. So you do USB 3.0 too. You can do that. We could, but that's not what I'm going with right now. So by the time you get to it, right? Well, maybe. Yeah. So I mean, basically, the idea is to have the exact same radio capabilities, but just in an embedded platform as opposed to in a peripheral. And that's because there are a whole lot of people who show up in the HackerF IRC channel who are like, I'm working on this project where I'm connecting my HackerF one to BeagleBone Black or to a Raspberry Pi or to something, some kind of an embedded Linux platform. And it would really make sense to have that all be one board.

**Michael Ossmann:** Huh. That's interesting. Yeah, I guess you could. I mean, because right now that's still USB. It's USB connected. Is that right? It just streams over USB. Because you could also do like, I mean, if you did choose a BeagleBone Black, you could just refactor it onto a, onto a, like a cape. That's what they call those, right?

**Chris Gammell:** You could make sort of a HackerF cape for the BeagleBone Black. And that's basically what I want to make. Except, except BeagleBone Black has a couple of significant limitations for that particular application. And one of them is that BeagleBone Black only has 10100 Ethernet. It doesn't have gigabit Ethernet. And so you would actually have a significant downgrade in speed from USB 2.0 down to gigabit Ethernet or to 10100 Ethernet. And if, so for those cases where you want to do everything on the embedded platform, it should work great. But for a case where you'd prefer to actually stream those, those digitized radio samples over to somewhere else over a network, it's not such a good solution. Right. Yeah, that makes sense. Yeah, so, and that, that's, but that is definitely something that I considered. Like maybe, maybe that, maybe that would make sense. And if somebody wanted to do that, that, that'd be a cool thing. I'd love to see somebody make a HackerF.

**Michael Ossmann:** You could build another cape on top of it because they stack and you could put a, although passing high frequency signals through 0.1 inch headers is not always the best idea.

**Chris Gammell:** Yeah, and I don't think, I mean, because the, the, the, the microcontroller in the BeagleBone Black, which is, I hesitate to even use the word microcontroller because it's so big. Oh, the PRU? It has, well, the, the ARM. Oh, okay. The ARM, it has, it has a gigabit Ethernet Mac. Yeah. But it's just the, the five chip that's on the BeagleBone Black is a 10, is 10, 100. Right, cost savings. Right, because it's like an extra $2 to make a gigabit at least. So, you know, multiply that by your profit margins and your supply chain and, and like, that's a, that's a big, it's a big difference. Right. For a.

**Michael Ossmann:** Especially when they were trying to compete with the, the $35. Exactly. Raspberry Pi. Exactly. So, yeah.

**Chris Gammell:** All right. So, that's what kind of led me to.

**Dave Jones:** Do you have any data on how many HackRF1s you've sold?

**Chris Gammell:** Oh, yeah. I've sold close to 10,000.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah. Wow. Nice.

**Dave Jones:** That's a lot.

**Chris Gammell:** Yeah. So, and then I gave away, you know, about 600 of the beta boards and then the radio badge guys gave away 4,500. And I don't know how many clones have sold, but there are some clones out there. So, all together, there's probably something like, like 20,000 HackRFs in the world, which is pretty cool.

**Dave Jones:** That's very cool. And it's not a particularly cheap product as well. SparkFun sell it for $299. Yeah. It's, you know, it's not like one, it's not, you know, a $30 impulse buy. Right. It's, yeah, that's fantastic. Yeah, it's pretty cool. What's this deal that SparkFun have got on their website here? This product has some level of export control restriction. So, expect delay when shipping outside of the US.

**Chris Gammell:** Yeah, I need to. Is that because of the transmission? I need to check on that with them, actually, because it shouldn't really be an export issue, but it may be an import issue. It certainly is a problem in many countries. Right. For example, I just got an email from SparkFun today about somebody, about a customer who's trying to buy one of these from India. And the Indian government doesn't want to let it in. So...

**Dave Jones:** Is that because it's a hacking device or is that because it's a, it's not an approved transmission ban?

**Chris Gammell:** It's because it's a radio frequency device, right? Right. And so, India is just one of many countries. I mean, every country probably has some amount of regulation about what radio equipment you're allowed to have.

**Dave Jones:** I suspect that if you tried to sell it here and you asked for permission, they'd probably deny it. Yeah. Because it's a broadband transmitter, right? Maybe, yeah. From one meg to six gig.

**Chris Gammell:** Right. Now, in most countries, definitely in the US and throughout Europe, there are exceptions for test equipment. Right. So, as long as I'm able to say that my product is, you know, a test equipment... Yeah.

**Dave Jones:** It isn't consumer. No, it's... Right.

**Chris Gammell:** Then I can legitimately, you know, import that product to a lot of different countries. But there are some countries that may not have that sort of exemption and it could be very difficult to get that kind of equipment into those countries, unfortunately.

**Michael Ossmann:** Right. Yeah. Yeah. Did you guys see this stuff about the FCC? I did not to change the subject too much.

**Chris Gammell:** No, this is a good topic.

**Michael Ossmann:** So, could you explain it for me? Yeah. I keep reading about it. And I'm just like, like, I know you can't... So, like, they're talking about you can't install OpenWRT, which is that open source firmware version that goes onto those blue routers, right? Yeah. So, what is the deal with that? I mean, does that actually affect your product at all or no?

**Chris Gammell:** No. And the reason it doesn't affect my products is because of the test equipment exemption. But this affects everyone who makes or who sells equipment that is radio equipment in the U.S. So, that's a lot of people.

**Dave Jones:** Yeah.

**Chris Gammell:** And what's going on is the FCC has recently published an NPRM, a Notice of Proposed Rulemaking, that totally overhauls their equipment authorization procedures. And this is the first, like, major overhaul of these, of the equipment authorization in, I want to say, in this century. So, you know, it's been quite a few years.

**Michael Ossmann:** Which sounds like not much. And then you're like, oh, shit. Yeah. That's a long time. Yeah. It's been a while. There's kids in high school that were born in this century. Right. Yeah.

**Chris Gammell:** So... Scary. They're really... Like, if you go and you look at an FCC ID on a product, or if you're involved in getting an FCC ID for your product, that ID is something you get with your equipment authorization. And they're totally overhauling the process for equipment authorization. And so they have out right now a proposed rule, which is a large, large document that... And there's an open comment period right now that's only open until the 8th of September. So I highly recommend that anybody who's interested in this, and if you are somebody who works for a company that makes a device that has an FCC ID, then you should be interested in this.

**Michael Ossmann:** Or if you like messing around with stuff that's already been made. That's true. Stuff like that. Yeah. I mean... Absolutely.

**Chris Gammell:** And so one of the things that folks in the open source community have noticed recently that is kind of a big deal in this proposed rule, is that equipment that can have its... That has a radio that is under software control, which of course is most radios these days. Right? Yeah. Every cell phone in everyone's pocket. Yeah. If you have a radio that's under software control, then the FCC says going forward, they want you, the manufacturer, to implement security procedure, some kind of security mechanism to prevent the end user from modifying that software in such a way that it can change the operation of the radio.

**Dave Jones:** I can see why they're doing that. Absolutely. I can totally see why they want to do it. Yeah.

**Chris Gammell:** Yeah. I can see why too. Why? Sorry. Well... Oblivious Chris. The FCC's main job here that they're concerned about, the reason that they're in the equipment authorization business, is to ensure that we all get along and share the spectrum effectively. Right. Right, right, right. Yes.

**Dave Jones:** No, you can't have anyone coming along, you know, just spewing out RF everywhere. Right. And it just ruined everything.

**Chris Gammell:** I was a 900 MHz transmitter, now I'm not. Exactly. Yeah. That's exactly what they're concerned about. And so they have... And interestingly, I made a comment... This is years ago when I was working for the NTIA. I... Who's the NTIA? The National Telecommunication and Information Administration. It's a different government agency in the U.S. And actually, it's one of two agencies that does spectrum management in the U.S. Everybody knows about the FCC doing spectrum management, but the FCC only does spectrum management for non-government users of the spectrum. Oh. The NTIA does the spectrum management for government users of the spectrum. So there's a lot of back and forth between the two agencies.

**Dave Jones:** You don't want them knocking on your door. No.

**Speaker ?:** No.

**Michael Ossmann:** So... Do you guys have softball games against one another? I don't know.

**Chris Gammell:** I mean, I just worked for the remote little research lab of the NTIA. That was not...

**Michael Ossmann:** Whoever scores the next run gets the new white space and gets to manage it for users.

**Chris Gammell:** Yeah. That might help, actually.

**Speaker ?:** Yeah, right.

**Chris Gammell:** Make more sense than legislation around here, right? Yeah, totally. Right. So back when I was working for the NTIA, the FCC introduced a new rule for software-defined radio, where they wanted software-defined radios that were going through equipment authorization. They wanted them to implement some kind of security measure to prevent users from modifying the radio parameters. And I, on behalf of the NTIA at the time, drafted a comment to the FCC saying how horrible this would be for open source. And it really stifles the development of open source software-defined radio systems. Because you can't really be open source and lock out your users at the same time. That's just not possible, right? So, of course, they ignored that. And that rule has been in place for some time for SDR systems. And now, what's happening is that they're taking a similar rule and applying it to non-SDR systems, really, to any radio system that has any kind of software control. So, it's become, it's popped up on the radar of a lot more people, specifically those who make a habit of putting custom software on 802.11 wireless routers, which is an extremely popular thing to do.

**Michael Ossmann:** Yeah.

**Chris Gammell:** Right.

**Michael Ossmann:** For security purposes sometimes, too. Exactly. It's not malicious. It's like, hey, I just want to make this so I actually can control the things that I want to control.

**Chris Gammell:** I want to have more control over my network. And it's not necessarily that people are doing things like running their network on illegal frequencies, although that may be possible in some cases. The vast majority of people who are running open source software on their wireless routers are making absolutely no changes to the radio profile, the spectrum that's being used. They're only making changes that affect the network side of things, higher up in the stack. And it's a wonderful thing that people are able to take off the shelf, low cost equipment and build much better software in some cases, software with better security in many cases, on top of these platforms. And that entire ability to do that is being threatened by this proposed rulemaking. So that's why folks are concerned about it right now. That's a big deal. Yeah. And I definitely recommend it, even if you're not working for a manufacturer that needs to get equipment authorized. If you're just somewhere who cares about open source, I would definitely recommend getting online and checking out this NPRM. And there's an open comment period right now. Anybody can go make a comment on federalregister.gov.

**Dave Jones:** Can I make a – can I actually ask people, if you are going to do that, these government agencies which ask for comment and stuff like that, you have to be professional in your remarks to them, in your comments to them and present a proper sound case. You can't just go in there and comment, oh, this is shit. You know, like you can't just be like a YouTube comment. You've got to do a formal submission. Otherwise, it just ruins the process, ruins it for everyone. Yeah. That's an excellent point.

**Michael Ossmann:** There was a letter on Reddit. Someone had basically said, here's what I'm going to be posting kind of like as a form for it.

**Dave Jones:** Oh, right. Yeah.

**Michael Ossmann:** You know, just like because a lot of people don't know that kind of thing. Yeah. And it's just kind of being able to see that.

**Dave Jones:** Yeah, so a lot of companies do that. A lot of – yeah, they'll put it, here's a form, mail. You know, here's how to write a letter to your local politician. You know, please, look, we'll give you the template. You just, you know, fill it in. And it's like, yeah, how to be nice and polite and, you know, play the system.

**Chris Gammell:** I definitely – and I'm on board with that. There are some other things in this NPRM that I haven't even read yet but that I think are interesting. Potentially. So I have more reading to do before I make my comment but I'll definitely be making a comment at some point within the next few days. But like one thing that apparently is changing is the practices around the confidentiality of information that is submitted to the FCC during equipment authorization. Right. And this is something that, you know, I've noticed for a long time as a reverse engineer and as a user of the public information that the FCC makes available through the equipment authorization database. It's a wonderful resource for –

**Dave Jones:** Oh, it is. Like you get these for like the Macintosh fanboys, for example. Oh, there's a new – like they'll just sit there and, you know, trawl the FCC website to see if they've submitted any new products.

**Chris Gammell:** Right.

**Dave Jones:** You know, try that. Yeah.

**Chris Gammell:** So it's a great resource and if changing the practices about how that information can be kept confidential, that might mean that less information will be available to the public in the future. I don't –

**Dave Jones:** That's good and bad. Right.

**Chris Gammell:** So that's an area of the rules that I intend to take a closer look at before I make my comment.

**Dave Jones:** Right. Well, you can have more than one comment, can't you?

**Chris Gammell:** You know, I suppose I probably could, but I'd rather just keep it to one.

**Dave Jones:** Right. You don't want to flood the system. Yeah. Yeah, right. Right.

**Michael Ossmann:** Is this something – Mike, I actually don't know, but is this something like people outside the states can submit?

**Chris Gammell:** Yeah, I'm looking at it right now on federalregister.gov and on the comment form, it does have a pulldown for country.

**Dave Jones:** Oh, there you go.

**Chris Gammell:** So Australians or other folks are – yep, Australia is in there. So you're –

**Dave Jones:** Yes, we exist.

**Chris Gammell:** In fact, not only is Australia in there, but Australia is in the short list of countries that are at the top of the list. Yeah. You don't have to scroll down past Austria.

**Dave Jones:** Well, come on. We are part of this five eyes agreement. Oh, that's true. That's true. You know, yes, we are – you know, we're way up there. So we're good bosom buddies with the – Right. Yep. Right.

**Michael Ossmann:** I just sent you guys – obviously people can't see this, but I just sent the link over too of a potential – I'll link it in. But basically there's a, you know, a template kind of what to say, that kind of thing. Oh, excellent.

**Dave Jones:** Oh, okay. There's a template. Okay. Excellent. Yes. And it's nice.

**Michael Ossmann:** I mean, it's just – it's very – like Dave said, it's very formal. It's not even very formal. It's polite. It's just very polite. Yeah. Yeah. It's professional. And it's very important. Yeah.

**Dave Jones:** And no all caps. No. Okay. Yeah, right.

**Michael Ossmann:** Double check your caps, folks. We're all adults here. Yep. And I – yeah. Spell out the word you. Y-O-U.

**Chris Gammell:** Definitely recommend that people take a look. See what's important to them. Make a comment. And be polite. And, you know, make sure that you – if you're going to make a case about some point in the rules, like let's say that the particular point about open source versus the software security restrictions, if you're going to look at – talk about that point in particular, try to come up with an example of how – you know, what kind of a – what kind of an effect you think that this will have on you or on other people who are citizens of the U.S. or users of the equipment.

**Dave Jones:** I'd argue that your point is pointless without an example. Yeah. It's, you know – Good point. It's just, you know, hot air. You know. Well, that's my opinion. You know. Why is it – Cite an example or, you know, they won't take you seriously.

**Chris Gammell:** Why is it your opinion? How does it affect you? How does it affect other users of the spectrum? And those are the things that they're going to care about.

**Dave Jones:** And that is our community service announcement this week on the AML. Yeah, right. Yeah, I don't think we've done that yet.

**Chris Gammell:** I mean, there's – No, we haven't.

**Dave Jones:** It's a new segment.

**Chris Gammell:** Hey, speaking of segments, do you want to have a chip of the week?

**Dave Jones:** Yeah. Okay, well, we'll wait over time, so we'll finish out the show with a chip of the week.

**Chris Gammell:** So I've been doing a new project with the LPC 4300 series microcontrollers. And – It's at NXP? Yeah, and it's the one that's in Hacker F1. And I've been doing this new project because I've been realizing what a wonderful platform it is. And, like, people need a more general purpose platform for this chip. So this is just a – You know, it's – At first glance, it's not all that special. It's an ARM Cortex M4 microcontroller. An M4 is, you know, pretty upscale microcontroller. But it's – Oh, yay. But it's pretty fast.

**Michael Ossmann:** Dave has yet to program anything on a Cortex anything, so I do know that.

**Chris Gammell:** Well, it's fast. It's 32 bits. It's dual core. It's cheap, probably. It's dual core.

**Dave Jones:** Tell us the price, son. It runs – Sorry, my Australian – the Australian viewers will get that.

**Chris Gammell:** Most of the parts in the family, at least the flashless parts, are, like, in the $5 price range.

**Dave Jones:** $5?

**Chris Gammell:** Dude, that's nothing.

**Dave Jones:** Jesus, you can fly to the moon on $5.

**Chris Gammell:** One of the wonderful things about this is that it has a very high-performing, high-speed USB controller. And it's hard to find microcontrollers in that price range that do not only full-speed USB, but high-speed USB. Right. And have the 5 built in. So you don't have to add an external 5 chip. Oh, yes. Right? This is a rare thing. And it also has some really fascinating programmable peripherals.

**Dave Jones:** And it's got a CAN bus, too. It does. Well, no, there's a CAN bus version. Sorry. There's a CAN bus version. I don't think all of them have the CAN.

**Chris Gammell:** Yeah, maybe not. But some of them do, definitely. Yeah. Yeah. So it has CAN bus. It has, you know, a lot of peripherals. But some of the peripherals that are kind of special are these – there's one called SGPIO and there's one called SCT, the state configurable timer. And they're both these sort of highly configurable state machines that run independently of the CPU. So it kind of gives you the ability to make sort of software-defined peripherals, which – So like it just kind of like watches for a certain bit pattern and stuff like that.

**Dave Jones:** They can make their own decisions. They can run their own – Exactly. They can – you know, it's like a micro within a micro kind of thing.

**Chris Gammell:** Yeah. Which is actually one of the concepts that the low-risk project is really running with. Oh, okay. They're going – one of the things that's cool about low-risk is that they're doing what they call minion cores, which are extra little CPU cores. Extra little CPU cores that have like high-speed access to their – to the GPIO pins and are just there to be like programmable peripherals. So it's a similar sort of concept in the LPC 4300 series. And I think it's a really cool part. So I'm currently building a board that's basically like a glorified breakout board for the LPC 4300 family just so that people can have this part on an easy-to-use board with an expansion interface and a really fast USB interface. Is it done your site anywhere?

**Dave Jones:** You can get some functionality like that on, say, some of the PIC micros, for example, I'm aware of. You can – you know, like they'll just – you don't have to put this in the code on your micro, like – but you can actually read a sample from the analog to digital converter and put it into memory. And then it'll like add a fixed period and it'll do that without any code intervention. You just set it up and it sort of, you know, does that task kind of thing. So, you know, really –

**Chris Gammell:** And that's a big part of why that part ended up in HackerF1 in the first place. Right. Because we have pretty high-speed analog to digital converters and digital to analog converters. And we have them externally clocked. So, we're clocking in and out samples from the microcontroller with an external clock that's not generated and not subject to the jitter that might be produced by the clock generator on the microcontroller.

**Michael Ossmann:** Got it. Which package are you using? Are you doing BGA?

**Chris Gammell:** Are you doing something else? For my projects, I'm using the LQFP. It's a 144 pin QFP. It's kind of big, you know. It's a 144 pin.

**Dave Jones:** Yeah, yeah, physically big. Yeah, that's a disadvantage.

**Chris Gammell:** Yeah, and they do have some BGAs that are smaller. But, you know.

**Dave Jones:** But you can see all the pins.

**Speaker ?:** Right.

**Dave Jones:** You can access them. You can probe them.

**Chris Gammell:** In theory, you can disorder to them. And if you –

**Dave Jones:** You can lift them up, you know, and hack them. In theory.

**Chris Gammell:** I like to make my designs, if possible, I like to make my designs, you know, something you can assemble with an iron. And occasionally, I run into cases where, you know, there really is no solution other than a BGA. Well, that's okay. But if I have the option, I'm going to go with the QFP.

**Dave Jones:** Of course. Good man.

**Chris Gammell:** Nah, man.

**Michael Ossmann:** Embrace the hot plate.

**Dave Jones:** No. It is the future. Chips ain't getting any bigger. I'll tell you that much. No.

**Michael Ossmann:** That's why I learned. It's true.

**Dave Jones:** Self-driving cars and BGAs are not the future. No.

**Michael Ossmann:** BGAs are not the future. Okay. Well, you heard it here first, folks. They're both evil. They're both evil. Yeah. I totally agree with that. Excellent. That's true. Tinfoil hats for everyone.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Thank you very much, Michael, for being on the show again.

**Chris Gammell:** Hey, thanks for having me, guys. It's always great to talk to you.

**Dave Jones:** Where can people follow you?

**Chris Gammell:** Greatscottgadgets.com or –

**Dave Jones:** Oh, that's a great name. Oh, thank you.

**Chris Gammell:** It's just brilliant. Or at Michael Osman on Twitter.

**Dave Jones:** On Twitter. Twitter man.

**Michael Ossmann:** Or find them at any range of security in Harbor Conference in the next year.

**Dave Jones:** All right. Thanks, Mike.

**Michael Ossmann:** See you. Bye-bye.

**Michael Ossmann:** So Mike, what's this, what's this thing you completely forgot to mention on the show when you were on the show? Oh, I have a new product. Hey. I have a new product. It'll be out any day now. Yeah. I'm really good at that self-promotion thing. So you go to lots of conferences, is that right?

**Chris Gammell:** Yeah. Marketing is clearly my strong suit. Right, right. Yeah.

**Dave Jones:** Nerds are just hopeless. They're just not competent to run a business. Yardstick 1.

**Chris Gammell:** Yardstick 1. It's yet another radio dongle. And it's a low, like sub-gigahertz, low-cost wireless interface on a USB dongle. It looks really similar.

**Dave Jones:** Why is it called Yardstick?

**Chris Gammell:** Yard stands for, yeah, yet another radio dongle. It's easier if you look at it.

**Dave Jones:** Oh, right. Oh, okay. Right. No, I'm not looking at it.

**Chris Gammell:** So the number one thing I have to tell people about Yardstick 1 is it's not software-defined radio. Oh. Everybody knows me for doing software-defined radio stuff, but this is not software-defined radio. So it's just a wireless microcontroller on a USB dongle that's super handy for interfacing with all sorts of low-speed digital communication systems like industrial control systems, smart meters, home automation systems, remote keyless entry systems, garage door openers, and all that kind of stuff. So you can actually see Yardstick 1 featured in the DEF CON talk that was done by Sammy Kamkar recently. So Sammy is somebody that maybe you guys should have on the show sometime. But he's done some interesting work actually with one of our Yardstick 1 prototypes. So that's a good example of the kind of stuff that you can do with it. Cool.

**Michael Ossmann:** Nice. Product plug over. Show over. All right. Beep. Beep. Beep. Wah.
