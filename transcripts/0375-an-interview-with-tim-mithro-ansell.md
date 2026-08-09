---
episode: 375
title: An Interview with Tim "Mithro" Ansell
url: https://theamphour.com/375-an-interview-with-tim-mithro-ansell/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released January 14th, 2018. Episode 375. An interview with Tim Mithro Anselm. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Tim Mithro Ansell:** And I'm Tim Mithro Anselm of Too Many Projects to Talk About. But I guess we might start with the Tomu, which is a project that...

**Chris Gammell:** Yeah, that's the most recent, yeah.

**Tim Mithro Ansell:** Yeah, and in fact, it's not really my project anymore.

**Chris Gammell:** Oh, wow, okay. Well, that makes it easy. So, coming on here, talking about other people's projects. I could talk about someone else's project too, if you want.

**Tim Mithro Ansell:** It basically, I guess, the interesting thing about it is... It's something that lots of people are really excited about. But it was something I did pretty much on a weekend. Oh, okay. And I did it because everybody was telling me that... This isn't something that a hobbyist can do. I'm not a professional hardware engineer. I'm a software engineer who likes to dabble with hardware. And because of that, I tend to think I can do things that other people who are hardware and a lot more experienced say, no, that's not a good thing to do because I don't know better. Mostly, that's a bad thing.

**Chris Gammell:** That's how you learn, though. That's how you learn. Yeah. Like, either way, either learn, oh, no, they were right or ha-ha, they were wrong. So, yeah, that's great. And this is a common theme with our guest last week, who you also know. So, Clifford was on last week. Yep. And you also know Clifford. So, that's great. Yes. Is this like a thematic of, you know, how dare you challenge me to say that I can't do this thing? I will show you. Yeah. I like it.

**Tim Mithro Ansell:** And so, I should also mention I'm not a security expert. Okay. Me neither. I do, however, believe that you can only trust what you can see. If you can't see it, you can kind of maybe trust it. Maybe. Okay.

**Chris Gammell:** So, you don't trust me right now because we're just doing audio only. Oh, I can hear you. That's close enough to being seen. Okay. Yeah. Seeing with your ears. Yeah.

**Tim Mithro Ansell:** Yeah.

**Chris Gammell:** Yeah. So, what kind of software do you do? I mean, so you dabble in hardware. We're definitely going to talk about the Tomu. Yeah. We're going to talk about some of the other past projects people have probably heard of. But what kind of software day-to-day are you doing?

**Tim Mithro Ansell:** I do...

**Chris Gammell:** Is it like high-level web stuff or, you know, back-end type stuff?

**Tim Mithro Ansell:** I've done a huge wide variety of different types of software. I've done back-end stuff. I've done front-end stuff. Most recently, I've started playing with tooling things. I'm actually a big believer in Python, the programming language. So much so that... We'll get to that too. Yep. I started the PyCon conference here in Australia. Yep. And that's absolutely massive here now. I think it's like 500, 600 people. Yeah, that's great. Yeah. And actually, I think you've had... Have you had Damien on here previously?

**Chris Gammell:** We've not had Damien on, but we've had Tony from Adafruit talking about MicroPython.

**Tim Mithro Ansell:** Ah, yes. So, MicroPython has been actually one of the really big reasons that PyCon AU has grown so substantially. Is like, I was originally very much there. Somebody proposed an Internet of Things track at the PyCon Australia conference. And us as ignorant organizers were very much like, oh, that's going to be a bust. Internet of Things isn't really a thing. And buzzwords. Yep, buzzwords. And we had totally missed the MicroPython craze. And so we put them in the small room. That was a total mistake. They had like... They were busting out of that room. And the year after we learned them, we learned that and put them in the big room. But yeah, especially since Damien's here in Australia, in Melbourne, and PyCon Australia was in Melbourne. So, like, that was kind of a big coincidence.

**Chris Gammell:** I've heard that the PyCon Australia is probably the next time I'll get back down to Australia because of that conference.

**Tim Mithro Ansell:** Yeah, it's in Sydney this year. We've just had the change of year, right? So it's not next year, like I've been saying for the last six months. Yeah, MicroPython's pretty cool. I was... I think Damien's another one of these people. Like, he's a physicist. And he did MicroPython because he didn't know he couldn't do MicroPython, right?

**Chris Gammell:** Right, right. Yep.

**Tim Mithro Ansell:** And I would have told him it was impossible to do MicroPython. But he did it, and it's pretty impressive. And, in fact, one of the big areas that I'm interested in is FPGAs. And I have a project to allow MicroPython to run on soft cores inside FPGAs.

**Chris Gammell:** So we've covered a ton of stuff in just five minutes here. Maybe, I think, yeah, I think we're just... I'm going to take the reins here, Tim. Let's go back to the beginning. How did you get started in all this stuff? Like, the standard taking stuff apart story, or went to school for it, or what was your path in?

**Tim Mithro Ansell:** So back when I was a kid, I actually was a voracious reader. And I read pretty much every book in the library. And had quite a high vocabulary and reading age. This was both really good, but it also hid the fact that I have dyslexia until I was quite late in primary school. And dyslexia is something that if you get some early intervention for, you can actually improve outcomes from that quite a lot. But for me, it was kind of a bit late. I was already past age where they would like to do interventions. And I went to this psychologist who did the evaluation for dyslexia and stuff. And she had this bright idea that said, there are these things called computers that are coming. And they have this thing called spellcheck. Just get him to do everything on the computer. The spellcheck will fix all his spelling for him. And nobody will know the difference. And so my parents took this on board and got me a computer.

**Chris Gammell:** I've never heard that as a solution before. Is that like a generally accepted method these days? Or is that a one-off?

**Tim Mithro Ansell:** I don't know. This was like the late 1980s, early 1990s. And yeah, the only problem though is that my parents got me a word processing computer. IBM XT computer. 8088. This did not play games very well or at all. And again, coming back to this theme of not knowing that you couldn't, I decided that I was going to take the games that ran on all my friends' computers who had things like Commodore 64s and other computers that were really good at playing games. And I was going to run them on my computer by rewriting them from scratch. Nice. And that's how I got into computers. And at some point, I decided this hardware thing looks fun. I'll give that a go. I've kind of played with, if you're an Australian, you'll have known about a thing called Dick Smith's Funway into Electronics.

**Chris Gammell:** Okay. Is that like one of those 99-in-1 or 301 type of kits?

**Tim Mithro Ansell:** Yeah, it was like a little kit that let you build like little circuits like flashes and stuff.

**Chris Gammell:** Yeah, okay.

**Tim Mithro Ansell:** But none of my teachers or none of my family were involved in electronics. So I could never make any of these work. And so it wasn't kind of until university where I actually got contact with people who understood electronics that I was able to do any real hardware. But luckily, I met a couple of people at Adelaide University who were willing to give this green behind the ears, whippersnapper, some training on how to do hardware stuff. And that's kind of how I got into hardware in university. Basically, because I'd already done most of the software stuff. So I had a lot of spare time during university. And so they helped me figure out how to do hardware and learn things like how to program a pick and those type of things.

**Chris Gammell:** Okay. And what kind of what time? So like, was this 90s then? Was the university years?

**Tim Mithro Ansell:** Early 2000s, I think.

**Chris Gammell:** Okay. Okay. Cool. Yeah.

**Tim Mithro Ansell:** It was still dial-up modem. Um, I have the pleasure of being the first person to get ADSL in our suburb when ADSL became in Australia. And the Telstra tech who came out to our house was very confused about it being a residential place and not a business.

**Chris Gammell:** Um, like, like, why would you be paying for this kind of thing? Yes.

**Tim Mithro Ansell:** But my parents wanted their phone line back. So that was how I sold it to them is that they could make telephone calls while I was on the internet. And so, um, yeah, I owe a lot to my parents for being very forgiving of my, um, uh, you know, usage of the internet.

**Chris Gammell:** Um, right. I don't miss the days of, you know, parents picking up the phone line and, and ruining internet sessions. Like, that was always the worst.

**Tim Mithro Ansell:** Yep. I can still hear that modem squeal, um. That's right. When it connected as well. You can always tell whether you're going to get a good connection by the sound, right? Like.

**Chris Gammell:** Nice. Yeah.

**Tim Mithro Ansell:** It'll sound a certain way and you'd know, oh, better disconnect and connect again because you didn't get that, you know, 56k, um, connection.

**Chris Gammell:** Uh, so this is, seems like, this seems like a pretty big jump from, uh, you know, the 56k modem days to, uh, to where you are now. So like, what was in the, in, in between? Cause we're going to get back to the Tomu for sure. Yep. Um, but it seems like, like you said, FPJs and other hardware. So, so what was your, what was your early hardware days?

**Tim Mithro Ansell:** Um, so I think the first big hardware project that I ever took on, um, was my honors project at university. Um, and for that, I decided I was going to build a telephone exchange. Um.

**Chris Gammell:** Oh, okay.

**Tim Mithro Ansell:** And.

**Chris Gammell:** Like an asterisk type server kind of thing, but. Yes. Probably.

**Tim Mithro Ansell:** Um, definitely like an asterisk server. I'd been playing with VoIP a little bit. Um, but the problem with the VoIP stuff I've been playing with is that, um, I wanted every telephone in my house to be a separate line. Um, right. So I could call between, um, the front of the house and the back of the house and that type of thing. Um. Right.

**Chris Gammell:** Right. Not a party line instead of a party line you're saying.

**Tim Mithro Ansell:** Yeah. And however, um, the cards which gave you, um, like telephone lines were like about a hundred bucks each. Um, yeah. And if you've done telephone before, you know that, um, telephones are actually very high data rate, right? They're like eight kilobytes per second. And I was looking at what my computer could do, which was like eight kilobytes per second times four bazillion. And going like, this doesn't make any sense. Um, right. Right. Why is this so expensive? And so for my honors project, I built based around a pick, um, which had a inbuilt USB interface, a, um, eight port telephone exchange. That was about a bomb of between 50 and a hundred dollars, um, depending on how you counted it. This was back in like 2005-ish, maybe a bit earlier than that. Um, I'm hopeless with dates. Um, that's another thing. Yeah, that's right. Dyslexia gives you as order of things as hard.

**Chris Gammell:** Right, right. 5,002, right? Yeah. Um, so yeah. The, you know, so that's just useful for like understanding, I think, around like what kind of tech was out there. You know, were we into the age of Raspberry Pis and stuff like that? Or, you know, like we're just kind of relative, like even circuit board costs, stuff like that. Obviously in Australia, you know, probably getting, getting stuff there's a little bit more expensive, but overall, you know, same kind of technology available.

**Tim Mithro Ansell:** Yeah. So I don't think the Raspberry Pi was out yet. When was the Raspberry Pi first?

**Chris Gammell:** No, it was like 2010 or something like that.

**Tim Mithro Ansell:** I think this was like five or six years before Raspberry Pi. It was well before Arduino as well. Arduino kind of wasn't really a thing there. Maybe it was just starting to become a thing. Definitely the Arduino boards were like 50 bucks at that time. Um, if anybody remembers the early days of Arduino, the Arduinos were very, very expensive.

**Chris Gammell:** Right. But also for the same reasons of like, you know, circuit boards more expensive, getting parts and distribution was more expensive. It just, yeah, it wasn't as enabled for the maker crowd.

**Tim Mithro Ansell:** Um, yeah. Although at the time, um, microchip and I actually think they still do had this wonderful program. Whereas if you signed up as a student, they would send you samples from their, like their chip line. Um, you got, I think it was like four samples from four different lines every month. Um, um, and they'd ship it to you for free.

**Chris Gammell:** It's like a jam of the month club, right?

**Tim Mithro Ansell:** Yeah. Um, and so I got all these PIC chips with various different functionality, like inbuilt Ethernet and inbuilt USB. Just like the first of the month I'd log into their website and, um, like go through and select a bunch of different, um, uh, chips that looked cool and ordered them. Um, and they just send it to me for free. It was actually pretty awesome. And they actually got a, um, like I still consider myself a, um, PIC person as opposed to Arduino or anything else, um, for that. So like their marketing worked really well. They hooked you young. Yeah.

**Chris Gammell:** Yeah. Right. Cool. That's great. Yeah. Uh, and so, so you had this eight port, uh, phone inter exchange. Um, and so was that using a certain protocol or like, how did that work? How did that actually communicate to each, uh, actual phone?

**Tim Mithro Ansell:** Um, so it just had a standard, um, RJ12 socket, eight RJ12 sockets, which then connected to a little daughter board thing, um, that I designed to do all the analog, um, shifting. The hardest part was actually doing the ringer signal. Um, there's the ringer signal. I believe, I mean, it's been almost 15 years now or something since I, 10 years since I looked at it, but it's like, I think 90 volts RMS, um, very low current, but, um, right. Um, generating that from the five volts I had from the USB, um, while still being within cost was really hard.

**Tim Mithro Ansell:** Yeah. Um, it's very easy to do that if you're willing to pay, um, like $10 per port. But when you've got eight of them, 10 times eight adds up really quickly. Right. Um, right. Yep. And so I had to, um, cut corners wherever I could. And I think that was one of the most interesting learning experiences was how do I build this with the, in the constraints I had. Um, and these were all self-imposed like, um, I was the only one who cared about it costing, um, you know, cheap. My supervisor didn't really care about that, um, at all. He was just very impressed that I was doing a telephone exchange type thing. Right.

**Chris Gammell:** And these were all, so these were all analog telephones too. Yes. Is that right? See, that's, that's not what I expected. I thought you were talking about, so you're talking about doing almost like an old school exchange. Yes. Um, I was thinking, cause you said VoIP, I thought it was going to be a VoIP type thing.

**Tim Mithro Ansell:** Um, well, it had a pick with a USB on it. And so it appeared as like eight sound cards over the USB. And so. Sure, sure. That was kind of how you connected it to Asterix, which was the VoIP thing at the time.

**Chris Gammell:** Um. Oh, okay. So this was just the inner, I'm, what I'm really thinking of is like the inner, you know, all the VoIP phones these days are like ethernet based and they're actually doing it all digital up to the phone. Yeah. But you're, yeah.

**Tim Mithro Ansell:** Okay. That's great. That's really cool. This was all analog stuff. Um, and so, yeah.

**Chris Gammell:** Cool.

**Tim Mithro Ansell:** And so that was kind of my first big hardware project that I did. Um, and I was actually really happy with that. I had to do some cool hacks to make, um, um, I was using a, um, codec for doing the telephone side. Um, the codec did I2S and the pick doesn't have native I2S. Uh-huh. And so I had to connect the I2C, um, UART to the I2, um, the I2S bus and do a couple of bit banging for a couple of other pins to make it all work. And it was kind of this interesting, um, again, nobody told me that I couldn't do this. And so, uh, again, I tried to do it and I actually did succeed. It took me many, um, late nights in the lab with the oscilloscope trying to get it to work because I had, um, very, I think I had like eight instructions that, um, to make like to meet timing on this. And so it was a juggling act of moving things around to try and get it working. Um, but.

**Chris Gammell:** Well, that's a good question too. So this was all assembly?

**Tim Mithro Ansell:** Uh, yes. All the pick code was in assembly. Um, I couldn't afford the pick C code, um, compiler at the time. Right, right. Um, right. And there was no open source SDCC or something like that, that I knew of at the time. Maybe it existed, but I definitely didn't know about it at the time. Right, right.

**Chris Gammell:** And so, yeah. Uh, so, so, uh, so obviously a lot of interest in hardware at this point. So why, why the switch back to software? So it was a kind of like the software jobs were paying out of school or, or why did you, uh, why did you bounce out of hardware or did you not bounce out of hardware? Sure.

**Tim Mithro Ansell:** So I've always kind of been hardware adjacent in some way. Um, but.

**Chris Gammell:** Yeah.

**Tim Mithro Ansell:** Um, I am a software person at heart really. Like if anybody comes and looks at a hard, one of my hardware projects, they'll see I'm a software guy. Like any person who's a hardware person, like I want things like unit tests for my schematics. And that's actually another one of these, um, projects that, um, I would love to get going that, um, I've just never had the time to is to, um, extend KiCAD to do much better design rule checks than just like, is this input or output and these voltage levels matches? Like I would actually like to do real, um, checking that you've got like analog signals connected to analog pins and digital signals. Like your I squared C bus is connected to the I squared C on the device, right? Like many devices have these muxes that let you change what, um, pin functions in which way.

**Chris Gammell:** Oh, right, right, right. Yeah. Like you could have like eight different, uh, you know, the, the spy pins are crossing over the digital IO or a crossing over the serial or whatever. Yeah. Right.

**Tim Mithro Ansell:** Yeah. But frequently they're not a full matrix, right? You can only have spy on like pin one, 10 and 12. Um, right. And so it can be really easy to stuff up your design by putting, thinking you put spy on like eight and it turns out you can't map spy to eight.

**Chris Gammell:** Um, right. So I want you to. See, that really gets me an FPG. We'll get to FPGAs obviously, but like that always gets me an FPGAs when. When they lock some of those pins out too. It's like, come on. Like literally the entire idea of this is to be flexible. And like, there's certain things where it's like, no, you can't, can't do that. You know? And it's never like the top of the data sheet either. That's the other crazy thing. You'd think it'd be like, here's what you absolutely must do no matter what, or else you will mess up your design. And yet they, that's not how they write data sheets. Yep. So, oh well. So how would it work with, uh, so unit testing in KiCad would be, I mean, uh, to be honest, I don't even do the ins and outs stuff. Um, I just ignore all that stuff.

**Tim Mithro Ansell:** Yeah. Most people do because it's not particularly useful, but, um, all it takes is one person to describe the capabilities of the parts. Like this part is an I squared C interface on these pins. And then you could do something as simple as check that I squared C interface is connected to I squared C interface or, um, uh, actually coming back to FPGAs, um, the Spartan six from Xylex has this weird thing that, um, HDMI inputs can only be handled on certain banks of the FPGA, whereas outputs can be only handled on other banks. Um, and so if the, um, KiCad knew that this was a HDMI system, then, um, it could check that you've connected HDMI to the right banks on the FPGA. And so when you're swapping all your pins around to make your, um, PCB routing easier, you could then run your check and make sure that you haven't, you know, screwed up all your, um, requirements because the actual tool understands that, oh, these type of pins can only do this type of functionality. Um, or this type of, um, speed is another one, or this is a differential pair. Is another thing like the, um, make sure you've, your differential pairs are matched and that type of stuff. Um, so.

**Chris Gammell:** See, my thing is always that, uh, a lot of that depends on the idea of like part libraries is actually, it's like software libraries, but that's never really the case because I'm always making my own parts anyways. And, uh, so that's like a systemic level type problem as well.

**Tim Mithro Ansell:** Yeah. And I think it's because part libraries don't really offer you much value these days, right? Like it's just the footprint. I could create the footprint and then I know the footprint is correct, right? There's no other extra value that library is providing. Yeah.

**Chris Gammell:** I think, I think you, yeah, you, you hit it on the head there with, uh, I, I, uh, the, the, you know, it's correct, right? That's like a trust piece. And like, I don't trust you. I don't trust me. I don't trust anyone, you know, but also I don't trust me for the right reasons because I've gotten it wrong in the past, you know?

**Tim Mithro Ansell:** Yes. Um, but if your library came with a lot more functionality or features, um, it then starts becoming a value proposition. Well, I should use, um, I should use this library because, um, it has all these annotations already in it and it automatically checks that my design is actually, you know, correct and will work. Sure. Sure. And like, um, one thing being a software guy is I hate the iteration cycle of, um, hardware. Like.

**Chris Gammell:** Right. Right.

**Tim Mithro Ansell:** Even if you have a meal in your like room, right? The iteration cycle is still hours at best.

**Chris Gammell:** Uh-huh.

**Tim Mithro Ansell:** And. Right.

**Chris Gammell:** Right. If you're really good at prototyping and, and your parts are capable, if you're not using BGAs, if you're not using TQFPs or anything like that. Yeah.

**Tim Mithro Ansell:** If you're not using anything useful. Like.

**Chris Gammell:** Or modern. Let's say modern, right? Yeah.

**Tim Mithro Ansell:** Um, and so like it, I don't understand it. Like software, we have an iteration cycle of, you know, seconds mainly. And yet we do all this huge amount of testing to make sure that our software is correct. Right. But like.

**Chris Gammell:** Right.

**Tim Mithro Ansell:** On the hardware side, we have iteration cycle of, you know, weeks or months to get your PCB back from like. Um, if you're like me, a hobbyist, like in Australia, like Australia shipping takes forever. Right. So like iteration cycles on months, yet we do so little testing beforehand. Um, and that's an area I think that one day somebody will crack. Um, I don't know if, I don't think I will, but it's something I'd love to see somebody work on more is this kind of whole, let's take this software approach and apply it to hardware. Let's do checks. So every time I commit something, it tells me, Hey, wait a sec, your schematic's broken. It's not going to work. You've connected this thing. If you try and make it, it will like blow up. That's a much better than when you put all the parts on it and it, um, explodes.

**Chris Gammell:** Yeah. I just think that stuff doesn't change all that much either. That's the other problem is that like with hardware, it's like once it's done, it's usually stays like that for a while. Whereas software, you need those checks because you're changing so many of the underlying pieces that if you didn't have the checks, you would automatically, you would blow up everything all the time because you're always kind of refactoring and, you know, rewriting libraries and whatever else. So you need those unit tests for sure. Whereas hardware, it's like, all right, the interface is done. Don't touch it till the next rev. Yeah.

**Tim Mithro Ansell:** And that like, um, as I said, I do a lot of FPGA stuff and that frustrates me with FPGA designers so much is like they design something in FPGA and then it's like, it works. We don't touch it. And it's like, but I want to add features and like fix bugs. Tinker with it. Yeah. Make it use less resources and make it faster. And do these type of things.

**Chris Gammell:** Right. Like, right. I'm sure there's a heart. There's other, there's other FPGA designers out there listening right now being like, you know why we don't change these things, Tim? It's because of the software people. That's the thing though. It sounds like you're, you're writing the whole stack, right? So you're doing FPGA stuff and then writing software on top of it. You had mentioned before that you're doing like MicroPython and some of these FPGA cores, right? So if you control the whole stack, it's less of a problem than if you're throwing it over the wall to the software people and they're like, don't change anything. I need to write software for, for the existing register set.

**Tim Mithro Ansell:** Yeah. And if you've got a poor method of communicating your register set, then like it's both the hardware and the software guy's fault, right? Like the software guy shouldn't care where in memory your register is, right? They should just write this, call this function or some type of interaction. That's true. Or like, if you think about modern ARM processes, there's things like device tree that just describe where your things are. And like, it doesn't matter if the next version of your chip has the register in a totally different location. If the device tree tells you where that location is, you can just, it just works. You don't need to, you can iterate. And that's something.

**Chris Gammell:** Great in theory. Great in theory. Yes. I think that's the thing. Like you're talking about changing workflows of different people and like, yeah, I think that you're totally right. But yeah, good luck in an organizational standpoint.

**Tim Mithro Ansell:** Well, I think the thing is that once you can iterate fast, it's hard to go back to not iterating fast. And like once hardware people realize that, hey, wait a sec, I can change my PCB at any time and everything still continues to work. Like that's the big thing is like, every time you change something, you're afraid it won't work. Right?

**Chris Gammell:** Oh, no, no, no, no, no. That's not why I, that's not why I prevent changes to my stuff. It's because of the cost and because of the hassle of actually building the thing. That's the real problem.

**Tim Mithro Ansell:** Um, I would say that why is it so costly to change things?

**Chris Gammell:** Um, because FPGAs are expensive and, uh, part placement costs is expensive and the logistics of shipping things is expensive. I mean, things are dropping in price, but the, the problem hasn't gotten any simpler on the assembly side of things.

**Tim Mithro Ansell:** Um, I don't know. I've, I haven't done many major assembly projects and I definitely haven't done a project with, you know, 10,000 units. Um, but if you look at what, um, say Tesla's doing with their cars, um, how they are effectively starting to go with rolling revisions and you just have a new car with a new set of features, it doesn't matter when you buy it. Um, I think that's going to happen everywhere.

**Chris Gammell:** Um, your, this idea of, well, I don't, I don't think so, but maybe, maybe the, if it's good enough, like the, the companies that do it will, will survive and the companies that can't or won't do it won't survive. But I, yeah, I, I, boy, that's an optimistic viewpoint, Tim, I gotta say. Um, it probably is. Um, having, having been around hardware people, I like, they, they don't even like changing like the color of their pants on, you know, between like decades, like. Yeah. Um, yeah. So.

**Tim Mithro Ansell:** But I do think software is kind of eating everything and. I totally agree with that. It will eventually come for hardware. Um, there's no doubt about that. I totally agree with that too.

**Chris Gammell:** Um, yes.

**Tim Mithro Ansell:** It might be five years from now. It might be 30 years from now. I don't know. Um, but I'm looking forward to it because. Yeah.

**Chris Gammell:** No, I, I think that's, that's actually a good bit of optimism and I, I would agree with that. I mean, like, so I remember like tracking in manufacturing. I used to do it where we would have a problem where like, oh, well this new batch of capacitors, um, was giving us issues because of tolerance stuff. Right. So just some random problem. And it's like, oh, well how do we track which capacitor reels was used there? It's like, we don't track that. You know, it wasn't actually tracked all the way back to the system. You think about that in a software context, of course you would know, you'd know, like you'd be able to go back through the repo, see, oh, well, Tim changed the, you know, change the code on this one library. At this point we can go back and revert that or check it or whatever. But I didn't even have any of that data for, you know, with the hardware piece of like, oh, well the capacitor reel just changed. So how do you, you know, like, yeah. Um, the infrastructure wasn't in place. That's what I'm trying to say.

**Tim Mithro Ansell:** Yeah. And it will be a long time before it's everywhere, but I do think it's a big thing that's coming is like, um, being able to understand things like this or like, if you imagine, um, I remember back 10 years ago, there was this like bad batch of capacitors that was causing everybody's motherboards to explode. Um, do you remember that kind of thing? I feel like that we should have been able to understand whose motherboard is going to be out explode, um, because of, we should be able to track where those capacitors were placed on which parts and all that type of thing.

**Chris Gammell:** Right.

**Tim Mithro Ansell:** Um, right.

**Chris Gammell:** But, and then the unit test of did the board explode?

**Tim Mithro Ansell:** Yes. That would go, no. Um, but yeah.

**Chris Gammell:** Um, okay, cool. Well, let's talk about your, uh, FPJ project. Cause this is probably what people know you for among other things, right? The HDMI to USB or is it, or am I getting these backwards? So I know there's, there's two things here, right? Yep. Tim videos. Is it, is that the same stuff?

**Tim Mithro Ansell:** Um, yeah. So Tim videos is, I guess the overarching project. It's a project that is trying to build software and hardware to, um, record conferences and user groups. And the HDMI to USB is basically the first or like one of the major hardware pieces that, um, are involved in that. Um, okay. Um, and so like HDMI to USB is a Tim videos project. Um, but it can be used outside of the, um, um, the Tim videos ecosystem. If you just want to use, um, the HDMI to USB with Google Hangouts, for example, then, um, right. That's quite, um, capable when you can do that.

**Chris Gammell:** So I first came across that when I was looking for my, my home video setup. I, people have watched any of my stuff about how I do my videos. I do it all with webcams. Yep. And people were also talking about, well, you could do it with, you know, HDMI capture type stuff and then, you know, streaming it to an OBS or whatever. Yep. And they had, they had someone at some point had recommended your stuff. So it kind of fits in that as well of like streaming multiple cameras, multiple inputs to a device and then capturing it on a computer. Is that a decent explanation? Yeah.

**Tim Mithro Ansell:** Um, the kind of environment though, that we're targeting is user groups and conferences, um, especially open source conferences, um, which is a very different position to be in than a setup where you can kind of leave it installed and have it, um, uh, like working and then don't touch it. I guess it's kind of exactly what we're talking about previously is like, um, with a conference, for example, like the Linux.conf.au is a conference that we record regularly. Um, and it's coming up in a couple of weeks. Um, we frequently don't get access to the venue until the day before the event. Um, and that's like on a good thing. Sometimes it's like the morning of the event, we get access to it.

**Chris Gammell:** They're like, no, no, no, no. There was, there was a wedding here the week, the night before, there was an event the week before and they're like, yeah, you get here when you get here. You only paid for three days. You only get three days.

**Tim Mithro Ansell:** Um, yeah, that's fun. And so like we have a very short time to deploy and then to make things worse, everybody who's operating this is normally a volunteer and they may have only had like an hour or maybe two hours of training on how to use this stuff. Uh, uh, because like none of these conferences really have a huge amount of budget. And if they were paying like a professional calling, um, for this, they would be, you know, um, ticket prices would be like substantially more. Um, and so one of the things we really need, and this is why we ended up doing our own hardware is the, well, I guess I call extreme debuggability, um, the ability to understand why something is broken, not just that it's broken. Um, and, uh, a really good example of this is, um, some people for some reason like having black backgrounds on their, um, laptop. And it turns out it's very hard to tell the difference between the projector is projecting nothing and the projector is projecting the presentation from the user, but it's just black. Right.

**Chris Gammell:** Right.

**Tim Mithro Ansell:** Um, visually a human eye cannot tell the difference very easily. Um, whereas the computer or the hardware knows whether or not it's getting a signal, right? It knows it's getting a black signal. Um, it can tell you this. And we were just not able to buy commercial hardware that would give us that type of information that yes, the person is sending a signal and it's perfectly valid. It's just black. It's working. Tell the presenter to drag something onto that. Um, right. That thing. It's actually working. Please continue. Um, rather than running around headless going, why isn't this working? You really want that type of information. Um, or like another thing we can detect quite easily is bad cables. Um, because we get, um, the way HDMI kind of works is that there are, um, three channels, one for red, green, blue, and then there's a clock. Um, if you get errors on one channel, um, we can actually see that because we keep an error count for each channel independently. And so with this, we've actually been able to see cables where, um, for example, just the red channel is a bit dodgy and is having like one or 2% errors, which is what's causing, um, the, like output to flicker in some way. Um, and we can see that we can actually like debug that and understand what's going on rather than just going, well, it could be the cable or it could be the presenter's laptop or it could be, you know, something else going on. Um, right.

**Chris Gammell:** Right. So just having like small flags of things to like hints really. Right. Yeah. Having details of what's going on. Like, right. Um, well, I would think another thing too. So like, this seems like relatively low cost to some of the commercial stuff you mentioned, uh, just having more places you can do, you know, you can do small conference sessions then, you know, I, I've been like Defcon and they do professional filming there, but you only can see like two or three of the stages, I think on the recordings. And then you have to pay a bunch for them anyways. Right. Yeah. So it's like, in this case, you could have a small, you know, a 30 person session and still film it potentially.

**Tim Mithro Ansell:** Yeah. That's like our eventual goal is I want anybody anywhere to be able to live stream and record their proceedings, um, without having to be a, the expert. Like, um, the only way at the moment we make, um, conferences work is by having people who are experts on, um, uh, like the audio visual stuff and know how to fix various problems. Um, and the reason they can do this is because they're in their head. There's a whole bunch of knowledge about, Oh, I've seen this problem before. I know how to fix that one. Um, right.

**Chris Gammell:** Exactly. Yeah.

**Tim Mithro Ansell:** But, um, with this kind of really advanced debugging information, we should be able to walk through a person who has no AV knowledge about, um, what's gone wrong. Like, um, a classic example is the presenter plugs into the wrong plug. And so, um, uh, back a long time ago, I originally tried to take the, um, system that, uh, we used to record conferences and put it in a box that I could give to someone. And this had like a really nice wizard that would walk you through, like setting up the presenter and setting up the, um, audio and checking the levels and all this type of thing. Um, and basically just followed exactly what it said. Um, the problem I ran into is that there are two ports on it and I lay like, I color coded one red and one yellow, but I couldn't tell when the person, despite me saying, please plug into the yellow port had plugged into the red port. Whereas now we can, we can say, oh, I meant the other yellow port, um, or the other red port type thing. And we can actually like build a system that helps you figure out what's going on and why it's broken and solve that for you, um, without having to have you involved in it. Um, so what is it, what's actually, what is the hardware on there that's enabling all this stuff? Um, so it's an FPGA. Um, like the big thing that, um, makes this all possible is because it's an FPGA, it's reconfigurable, um, and we can continue to improve it. Um, which, which FPGA is it? Um, the current board we're using, um, has a Spartan six on it. Um, but it's likely we'll have some RTX seven based stuff in the near future. Um, but the important part is like we, when we see an issue, we can debug what's going on. We can add new hooks into the, um, system to allow us to understand what this problem is and prevent it from happening again. Next time. Um, we can continually improve the HDMI core with workarounds for various, you know, broken pieces of hardware or, um, stupid things like a projector being 1024 by 768, but 16 by 10, um, resolution, like using non-square pixels and things like that.

**Chris Gammell:** Um, we can kind of. Sounds like you're really, you're really optimizing for a lot of, uh, user error here. I gotta say. I know that there's, there's like a balance point of like, well, you don't want, you don't want to make it easy for the person, but it sounds like you're almost like, babying the person, not babying. That's the wrong term, but you know, like that they're, they're getting an easy way out. Does that sound right or no? Um, well, there's a lot of technical, there's a lot of technical solutions to what could be a little bit of user knowledge would help. But, but I guess it's based on the idea that you said most people won't have any training.

**Tim Mithro Ansell:** Yeah. And it's also like a lot of the problems aren't something that a user can really do things about unless you can tell them exactly what the problem is, right? Like, um, a user can't replace the cable unless you tell them that it's the cable that's dodgy, right? Um, if you say, oh, the problem could be your laptop, the cable, this other cable over here, this other random thing, right? You just kind of got no hope. And like, I'm sure we've all had this problem where like the presenter gets up in front of, um, everybody and then spends like five, 10 minutes getting their laptop to show up onto the projector, right? Um, that is still not an uncommon thing to occur at conferences. And, um, it just boggles my mind that, um, this still happens. And the reason it's happening is because, um, people solve this problem once for the room that that's in and it never gets shared. It never gets, um, propagated to other people or it's locked up in somebody's head and they know that you just have to jiggle this thing in this way to make it work. Um, right, right.

**Chris Gammell:** And that's usually how it goes too. It's like, oh, we'll just do it all over again. Plug it all back in.

**Tim Mithro Ansell:** Yeah. And so I want to move all that into the software because software is, doesn't have a, like imperfect memory and forgets and it can improve continually, right? Like hopefully I mean, software can also say BitRod, BitRod's real, man.

**Chris Gammell:** BitRod is real.

**Tim Mithro Ansell:** Um, yeah, but actively maintained software should continually get better in theory. Um, right, right. But because it's, that's the other thing is like, um, and a perfect example of this is like our Spartan 6 board can only do 720p60. Um, so if a presenter somehow manages to send 1080p60 to it, um, we cannot, um, decode that signal. Um, we advertise to the presenter that the only resolution that we support is 720p60. Um, so like firstly, it's a miracle that they've managed to get 1080p, but you know, um, let's just assume they have. And we have seen cases like this, um, even though we can't decode that, um, we can decode the pixel clock and we can see that the pixel clock is running at twice the frequency that we can, um, decode at and we can provide a useful error message rather than just going nup, no data. Right. And, um, that's because we could put a frequency counter on the pixel clock, even though, um, like that's not something you could change in your, like, HDMI decoder IC after fact, right?

**Chris Gammell:** Like, right. Like some commercial or some, yeah, commercial level chip that's just doing that one, one thing. It's not going to be flexible enough to add a new feature like that.

**Tim Mithro Ansell:** Yeah. And there's a whole bunch of other features like that, that we've gone, well, it's really hard to figure out what the hell's going on here. So let's add a feature that lets us understand what's going on here. And as things go forward, we kind of, um, uh, add new features that help us better understand problems and hopefully fix problems with, um, hardware so that eventually you can get to the state that you just plug in and it works, right? That's the goal. There's eventually you just get up there, you plug in, it works and you don't spend 10 minutes, um, figuring out whether or not your laptop will work. Um, and yeah, um, that's kind of the goal of the project.

**Chris Gammell:** Um, cool. So how did you, how did you get to this point of, uh, I mean, this is obviously a pretty advanced project. So the FPGA stuff, what, what, uh, what made you choose the FPGA in the first place? And like, how did you start, how did you start on the, the, um, the process of, of making this board?

**Tim Mithro Ansell:** Um, so one of the guests you've had on here, I believe is Bunny, um, famous for like Xbox hacking, the Novena and those types of things. Um, he created a product called the, um, any TV. Um, I forget when he created this. It was quite a while ago. He demonstrated this as a, um, like it allowed you to put an overlay over an encrypted HDMI stream. Um, and I looked at that and his device was deliberately designed to not allow you to do capture. Um, because that would be, um, be violating the decryption, um, legal thingy DMCA stuff. Of course.

**Chris Gammell:** And right. So it's, there was like no real complaint again, against it. I remember, I remember when that came out.

**Tim Mithro Ansell:** So, um, but I looked at that and went, I think I can make that do capture. Um, however, I wasn't interested in the, like, um, Bunny was very interested in HDMI, HDCP, um, uh, video. So I'm only uninterested in, you know, unencrypted things that I'm supposed to be able to capture, right? I am interested in recording conferences and user groups. If a person is playing something that is, um, encrypted, like the fact it doesn't work is actually good for us because it means we don't get a copyright strike on YouTube. Um, right.

**Chris Gammell:** Exactly.

**Tim Mithro Ansell:** But yeah, that I looked at that and was like, yeah, I think I can make this do capture. Um, and then, um, at the time I didn't have much time. Um, but I'm lucky enough that I work in IT and I get paid quite a, um, good salary, which, and I have very few expenses. Um, and so I thought, why don't I just hire someone to develop this for me and, um, see if I could, they could get it to work. And so I went on, I think it was a place called V worker at the time. Um, like one of these freelancing. Yeah.

**Chris Gammell:** Like an Elance or whatever they're called these days. Yeah. I know what you're talking about.

**Tim Mithro Ansell:** Um, okay. Went on there and basically wrote up a specification for the type of thing I was after and, um, found a student in London who was doing a PhD, who was interested in doing the project and wanted to make a little bit of extra cash. Um, and, um, told them what I was trying to do and they thought they could do it. And, um, that's kind of how this HDMI capture hardware started.

**Chris Gammell:** And that, and that is the only recorded instance of that ever working. Um, sorry. I just had to make the joke. Yeah. I've seen a lot of people who are like, I have a budget of $20 and I, I know, and I know this isn't new. I have a budget of $20 and I want to make a supercomputer who could do this. Yeah.

**Tim Mithro Ansell:** Um, I think the big, um, advantages I have is like, I'm a software engineer. I can evaluate somebody's software engineering, um, capabilities. We had an existing thing that almost worked. We just wanted to change it slightly. Um, and I was very upfront that like, this would be a collaboration type project. Um, and it took me a couple of attempts to actually, um, get to a stage of getting something. Um, it didn't just kind of, you know, it's kind of that overnight success. Um, it took me five years to do this overnight success type thing. Um, but yeah, um, once I found the right person who was interested, um, it kind of worked pretty well. Um, that's great. But it took me a while to find that.

**Chris Gammell:** What were you specking in that the, I mean, so like, did you basically tell them to look at the NETV? Was it, is it, is it like a, a kind of fork of the NETV or?

**Tim Mithro Ansell:** Originally that was the idea. Um, but it turns out that, um, this group, um, of FPGA manufacturer, uh, FPGA dev board manufacturers, um, called Digilant. Um. Yeah.

**Chris Gammell:** We've had Clint Cole on the show, a founder of Digilant.

**Tim Mithro Ansell:** Ah, cool. Um, I've never actually met anyone in person from them. Um, but they developed a, um, dev board called the Atlas and the Atlas turned out to already have everything we need hardware wise. It had a two HDMI inputs, it had two HDMI outputs and it had a, um, high speed USB connector on it. Um, and so at that point we just decided to, I guess if you're a startup, you'd say you pivot, um, and use that board instead, um, rather than trying to adapt the NETV to, uh, the NETV. And that was kind of like, um, a really good idea because it would have take, like the NETV was specifically designed to make what I wanted to do hard.

**Chris Gammell:** Right. Right. Of course. And so. So it got you in the ballpark, but then you, yeah, you kind of look at the specs more. That makes sense. So what about the, uh, so, uh, what about costs though? I mean, like none of the, I mean, FPGAs aren't known for being particularly low cost. So what is the, what is the rough cost of these boards and like, you know, how much, how much did you end up having to struggle with that part of it?

**Tim Mithro Ansell:** Um, so the Atlas board was definitely more expensive than I would have liked. Um, but at that time we were using these things called, um, Knopsis twin packs for VGA capture. Um, and these things were like rock solid, but they cost about $500, um, each anyway. So it turns out that, uh, FPGA dev board is in that, um, kind of price range. So it wasn't such a big step up, um, to go to the FPGA, um, instead. And as well, I can kind of subsidize this a little bit with, um, my income from, uh, my employment. I don't need to make money. Um, which is very free.

**Chris Gammell:** Yeah, you can be closer to closer to the lower margin overall. You're saying, yeah, I get that.

**Tim Mithro Ansell:** Um, I don't have to, the, all the NRE, um, like I don't have to care about because I'm not in it to turn a profit at the end. And so. Right.

**Chris Gammell:** Well, I just think it's, I always think it's good to call that out though, too, from, uh, because, you know, a lot of our listeners, they look at something, they look at a project like, oh, well, why can this project do it? And I can't. And I always kind of push back on projects that hide the cost because not push back, that's the wrong word, but it's like, I just want to highlight it because it's like, well, some, you know, like when someone goes to build the next thing and they're like, I can't get this bomb under 600 bucks now. It's like, well, here is the constraints that led to that. You know, you just kind of need to call that out sometimes for, yeah. And for more people coming into the hardware space. That's what I really mean.

**Tim Mithro Ansell:** Definitely the, like I'm in a very privileged position, like I'm in a very well high paying job. I don't have any costs, uh, like any major expenses. Um, and so I have this kind of pool of money that, um, I can use to enable people to do cool things. And as well, all my, all the stuff I do is, um, open source. And so like all the designs, uh, up on GitHub, um, all the firmware is available. And so hopefully the idea is that the next board somebody does, they don't have to like, they'll have some NRE, but they don't have to, um, start from scratch again, which is like this other thing in hardware that totally blows my mind is that the amount of time people like start from scratch or take something that used to work and change it slightly, but never contribute back to the original thing and make the original thing better as well. Um, right. And so, um, that's something.

**Chris Gammell:** Well, we've talked about that a ton on here. You know, a lot of that is, uh, you know, uh, not having open standards on the schematic and the layout side of things and, you know, parts changing over time and just lack of openness. So I think, yeah, software is definitely ahead in that, in that regard.

**Tim Mithro Ansell:** Yep. And I'm trying to help there by, um, because I have, I don't have a lot of time, but I do have this kind of, I have access to money. Um, and so what I try and do is if, um, there's somebody contributing to my project who is struggling because they don't have access to the hardware, um, and that made a reasonable commitment to my project. I will just send them hardware. Um, like that's kind of the deal I make with my contributors. If you're contributing to my project and, um, you need hardware, I will figure out a way to, you're helping me. So I should help you. Um, and like, you might be time rich, but, um, financially poor type thing and let's work together and, um, like solve this problem.

**Chris Gammell:** Sure. So why, why in this border, there are only two, two HDMI inputs instead of, so it's two in and two out, right? Um, why, why only two? Cause I can imagine having multiple camera angles.

**Tim Mithro Ansell:** Um, so in a small user group type, um, case, the two inputs, you would use one board in a room and one input would be a camera. One input would be the presenter's laptop. Um, and that's just a way to keep costs down. Um, in a conference, um, situation, we actually generally use two boards per room. Um, and we have one board up the front where the presenter's laptop is going into it. And normally some type of like feed from something like a Raspberry Pi or something like that. That says like, welcome to PyCon. The next thing in this room will be, you know, that type of thing. And then up the back, we have a, say, um, a camera going into a board or maybe a camera going into an SDI capture core, uh, capture card. And then that's all, um, uh, converted to ethernet and trunked to a software mixing, um, solution, which will then mix these incoming streams of ethernet. And so that's kind of obviously a much more advanced setup than, um, like the single user group where you just have one board and you're just capturing exactly, um, what's coming up the USB and sending that to something like YouTube. Um, and I've got diagrams on the website of various different ways you can configure this. Um, uh, but at a conference, we kind of generally the camera and the presenter at like opposite ends of a lecture theater. And so we don't want to run long HDMI cables like that. HDMI has... Right.

**Chris Gammell:** I think they're limited to only like 30 feet usually or 10 meters. Yeah.

**Tim Mithro Ansell:** And they have no type of error correction or any of this type of thing in it. Whereas, you know, ethernet does, you know, um, hundreds of meters of fine. It has error connection, error correction and like gigabit. Every laptop on the sun supports gigabit these days. Um, and so like we...

**Chris Gammell:** That's great. And plus you're not worried about like interference stuff from wifi or anything like that. It's just point to point into a router or switch or something. So that's great.

**Tim Mithro Ansell:** Um, so in a, like a big conference, we will generally convert everything to ethernet as soon as possible. Yep. And then we use software, um, because we can iterate on software much faster than we can iterate in hardware. So... Right.

**Chris Gammell:** No, I think that's good. And that's, and that's kind of akin to a lot of, a lot of like DSP type stuff these days too, right? It's like, you may be of a front end for an audio thing, but then you immediately put it into a A to D, get into a digital signal, and then you could start doing lots of stuff on it. Yep. The only downside, usually the only downside that I ever see is latency stuff. Um, just cause processing on, you know, in digital, usually, you know, you start chunking on something, it's going to take a little bit longer, but the cost is usually so low. It's, it's way worth it.

**Tim Mithro Ansell:** Yeah. And on audio, like if, uh, sorry, on video, if you compare things to audio, you've got like an eternity, like one frame per, um, like one 30th of a second, like that's a long time, 33 milliseconds worth of, um, stuff in audio. You can hear that if that gets out of sync, but in video, um, like one frame latency is not a big problem. Um, yeah.

**Chris Gammell:** And sometimes it's one 24th, right? Yeah. If it's, if it's true film. Yeah. Yeah. So, uh, so you switched over. So then Numato Opsis, I'm not sure if I'm saying that right. That's an open source version of this.

**Tim Mithro Ansell:** Yes. Uh, basically the, um, Atlas was a great dev board, um, but it just isn't designed to be deployed anywhere. And so, um, I went on basically an attempt to create a version of that board, which, um, better suited our needs and better, um, had the type of features and functionality that we cared about in a configuration that we cared about. Um, you might notice that as many of the ports on the Opsis board, uh, on the, um, front of the board, right. Um, whereas on the, um, Atlas, they're kind of all around the board, which makes sense when it's a dev board, right? Um, but if you're trying to rack mount something, um, you want all the ports facing out like the front and back of the thing, you don't want trying to run cables around corners and that type of thing. Right.

**Chris Gammell:** Right. And HDMI cables usually aren't very forgiving and unbends. Yes. Rugged cables.

**Tim Mithro Ansell:** Um, and so, yeah. And one of the best decisions I ever made with, um, the Opsis board is that, um, I decided to make it the same form factor as the mini ITX, um, like PC form factor, which means that

**Chris Gammell:** we can co-opt the cases, huh?

**Tim Mithro Ansell:** Yeah. Um, if you want a fancy, like aluminum case that's all fancy looking, then you can get one. If you want like a cheap press metal thing, that's rack mountable, you can get that and anything in between. And like, we didn't have to do any of that design. We just have to do a little face plate and then we can reuse like the massive PC, um, existing PC industry. Um, we could never make cases for as cheap as, um, they make it for PC stuff because there's just like their volume is, you know, massive.

**Chris Gammell:** Um, so this was just kind of an add on. So this was basically just an open, open version of it, uh, crowdfunded as well. Yep. Looks like it hit its goal pretty well. So that's great. Okay. Um, and so this is still, this is still at 720p 60 frames.

**Tim Mithro Ansell:** Uh, yeah, it can do, um, 720p at 60 or 1080p at 30. Um, it can't do the magical, um, 1080p 60, which is kind of the golden full HD, um, standard. Um, and that's a limitation of the IO on the Spartan 6. Um, got it. The Spartan, uh, the RTX 7, uh, boards can do 1080p 60 on, um, the IO pins. And, um, I've been trying to do basically a new board, um, that is based around RTX 7. And it turns out that there's somebody else who was trying to do a new board based around the RTX 7 because they were frustrated with the same limitations that I was frustrated with on the Spartan 6. And, um, that was Bunny. Um, he wanted to do a new version of the NETV2. Uh, so he developed a thing called the NETV2 and he was showing it off at, um, the, um, Computer Chaos Congress. I can never remember what all the Cs stand for, but, you know.

**Chris Gammell:** Chaos Computer, right. Is it the Chaos Computer Chaos? Is that what it is? I know it's Triple C, but yeah.

**Tim Mithro Ansell:** Yeah, um, I can never remember what all the Cs stand for, um, but yeah, he was showing that off and, um. This year or past year? Uh, last year. Sorry, the year before last year. Um, and so I was giving a talk on, um, trying to demystify hardware decoding of HDMI to try and, um, uh, like, a lot of people think that hardware is kind of scary and especially like FPGA stuff is scary and they look at like a HDMI thing and go, wow, this is, um, something that I could never do. Um, and, um, um, I think that if you put in the effort, most people could actually do this reasonably easy. Um, we're just terrible at, um, teaching and explaining this stuff. And so I was giving a talk that was aiming to kind of demystify that somehow I magically read a specification and came up with a perfectly working thing out of the box with no problems, you know, just like that overnight success that took 10 years. Um, right. I wanted to show that, um, people could do this themselves and that, no, that diagram that is confusing in the specification that confused me too. And I went down all these wrong paths as well. It's not, um, unusual for you to take multiple attempts to make this work. And I wanted to like tell people that, yeah, it's okay. This is going to take, this is something that's going to take you a couple attempts to get right. And here's all the ways I failed so that you shouldn't feel bad about failing this way as

**Chris Gammell:** well. Right. Um, so this was the, uh, this was the, uh, uh, dissecting, dissecting HDMI. Yeah.

**Tim Mithro Ansell:** Um, that like they have a diagram in the spec, which was written by a hardware person, um, because it describes exactly in how you would decode HDMI in hardware, in the technology that like HDMI, like when HDMI was first developed. Um, and it's actually like a really simple three-step process, but this diagram makes it totally incomprehensible. Um, anyway, I've totally gotten off topic. Um, I was at the conference because I was giving this talk and then I, um, went and had a chat to the bunny and chatted to him about his any TV to project and showed that I could get, um, our firmware that runs on the HDMI to USB running on his any TV too. Um, and he thought that was pretty cool. Um, and so we started chatting about that, um, and have started collaborating on, um, then a TV to stuff. Um, obviously I'm very interested in, um, having an RTX seven based board and he's also very interested in that. And so, um, um, we're just at the last one, um, the last CCC last, like two weeks ago now, I think. Um, yeah. Yep. Uh, we were there hacking on the V2 of the V2, um, board. Um, and so hopefully he will have something, I don't know, in the next six months that, um, will hopefully be, um, compatible with the firmware that we develop. Um, and so that's kind of been really cool because like he, his any TV one kind of inspired a lot of where, um, this project came from and now he's able to benefit from the, um, expertise and, um, code and all the stuff we've done, like built on from his inspiration. And so like, I feel like this is a really great example of why open source is awesome.

**Chris Gammell:** Um, yeah, definitely. And so, uh, speaking of Bunny, it's a Bunny's, uh, uh, firmware partner is, is, uh, Sean Zob's cross. Yep. Uh, and so he, uh, this tied back to any other projects. So let's go to that.

**Tim Mithro Ansell:** Yeah. Um, so that's the Tomu project. Um, so.

**Chris Gammell:** And so we didn't get this quite at the top, but what, what is it?

**Tim Mithro Ansell:** Um, so the Tomu is basically an arm microprocessor that fits inside your USB port. And I mean, like.

**Chris Gammell:** But, but why?

**Tim Mithro Ansell:** Literally inside your USB port. Like.

**Chris Gammell:** Sure. Um.

**Tim Mithro Ansell:** If you imagine. But why? Um, the like USB connector, if you cut off everything that's inside your port. Um, and the first reason is because, um, people said that you couldn't make something this size, um, as a hobbyist. Um. Got it. Um, the second reason is because, um, there's a group called, um, Ubico that make two factor authentication devices. Oh, yeah. Um. Yeah, the YubiKey. Yes. And so they have a thing called the YubiKey Nano that fits inside your USB port. And the idea is that you put one in every computer that you own and it provides like protection against phishing on, um, because it will only respond to the correct sites and all this type of thing. Um. Yeah. And so I was like, that's pretty cool. Um, my work gives me one for every computer I have. And I was like, my parents and family would be, um, it would be really good for them to be protected as well. And I thought, I looked at this device, you know, there's not much to it and thought, how much could they cost? And then I went to Amazon and was like, okay, how many do I need? I need about 10 to cover all, um, the computers in my family's house and looked at it and went, holy crap, that's going to cost me like a thousand dollars. And I love my family, but I don't love them that much.

**Chris Gammell:** Um, not like a thousand dollars. Can you put a price on love? Apparently you can. Yeah. Um, well, it's just like a extra. No, you're just saying it's not worth the, the, the, the cost does not match with the, the intrinsic value you're saying.

**Tim Mithro Ansell:** Yeah. And then the more I investigated it, the more, um, I came to the conclusion that the Uber keys are like security through obscurity. Um, at some point in the past they were open, um, but all their new stuff is all closed. Um, you have no access to what's running on that key. Um, like there could be back doors galore in there and we would never, never know. Um, and as I kind of said at the beginning is like, I don't really trust things that I can't look at. And like, I don't.

**Chris Gammell:** Well, I was going to ask about that actually, cause I'm looking at your video here and it's like, you can't even look at this thing cause it's shoved so deep inside of a USB port.

**Tim Mithro Ansell:** Um, but the software running on it, you can go and look at and like, you can build one yourself. Um, sure. Sure. The board uses a six mil, six mil process. Um, and so like that can be. Made by pretty much every PCB manufacturer on the sun. Yeah.

**Chris Gammell:** The cheapest, the cheapest ones out there. It can do it. Yep.

**Tim Mithro Ansell:** Yep. And like, because it's so small, I think like if you go to something like dirty PCBs and order their cheapest service, you end up with like a hundred of them. Um, for like five bucks.

**Chris Gammell:** Oh, because it's like a hundred cent, a hundred millimeters or something like that, or whatever the square.

**Tim Mithro Ansell:** It's like a, and they give you like plus or three plus or minus two or something. And so you end up with like a bazillion of them. Um, and yeah, the people were saying like, there's no way somebody, a hobbyist could make a, something like a UbiKey. Um, and I was like, I reckon I can. Um, and so one weekend I got tired of people saying that it couldn't be done and I did it. I created a device. I sat there. It was actually a really fun, um, distraction because it was something I could do in a weekend. Like if you look at my TV videos and HDMI to USB, it's been going on for like seven years or something now. These are long projects. Um, whereas the Tomu was like a project. I sat down, I do the, did the schematic and then I did the PCB and actually had to have them both up, um, uh, side by side at the same time so that I could like swap pins because, um, it's effectively a single layer board because one side has the USB pads on it. So I can't.

**Chris Gammell:** Oh, right. Of course.

**Tim Mithro Ansell:** I can't use vias or anything because the vias would go into the USB pads. Um, right. So I think I get one trace on the top that I get through. Yeah. Um, but it was kind of fun to play that mental puzzle. And yeah, of course.

**Chris Gammell:** Um, so why, why did you choose the part you chose?

**Tim Mithro Ansell:** Um, I went to DTKey and I searched for, um, microprocessors. That had inbuilt USB and did not require crystals and required the smallest amount of, um, supporting parts and then went sought by price and selected the cheapest one.

**Chris Gammell:** We need a, we need a name for that move. I mean, that's a pretty common one. Yeah. That's good.

**Tim Mithro Ansell:** Um, and like the part, like total in individual quantities, it costs between 10 and $20 to make. The whole board. The whole board. Okay. Um, in individual quantities, ordering everything from DigiKey. Um, and that includes like the PCB and the 3D printed spacer that you need and all this type of thing. Um, and so that is. Yeah.

**Chris Gammell:** I was going to ask about the cases too, because it, uh, it seems like this thing, if it's in the USB port and you didn't see it there, if you don't have a case around it, I would probably crunch it to death with the next thing I'm trying to plug in there. Yeah. So that's always the downside to those really tiny USB drives and stuff.

**Tim Mithro Ansell:** Yeah. When developing, I just fold over some paper and shove it in to make sure it has strong contact. Um, but you can 3D printer case. Um, and so, yeah, um, I built the hardware. The problem is that then it didn't do anything right. Um, and so I got a whole bunch made and I started giving them out with the hope somebody would write some cool firmware for it. And, um, a guy in Thailand and a coworker, um, both did some cool, um, software for it. And so a big thank you goes out to, um, Josh and Sergey who actually implemented, um, uh, Fido support for the Tomu. And so you can actually use it like a, um, Ubiki as a two factor authentication device for things like, um, Google and, um, uh, GitHub and anything that supports the Fido standard.

**Chris Gammell:** Um, what is the Fido standard? I don't know that one.

**Tim Mithro Ansell:** Um, it's a U2F standard.

**Chris Gammell:** Um, uh, fewer, fewer acronyms.

**Tim Mithro Ansell:** Um, universal two factor, I think is what the U2F stands for. Um, basically it provides a crypto challenge when you log in and, um, you know, like the token type things.

**Chris Gammell:** Um, yeah, right. Like the RSA tokens are the old ones I used to have that has like a time-based, uh, code that it gives you.

**Tim Mithro Ansell:** Yeah. Uh, Fido, I believe is a standard for that, but again, I'm not a security person. I would not say that the Tomu is a secure device. It is literally just an off the shelf internet of things device. It has no like hardware, random generator or crypto stories.

**Chris Gammell:** Yeah, there's no crypto module.

**Tim Mithro Ansell:** Or anything like this. Um, right. But I actually believe that's a good thing because it's also very unlikely to have a backdoor to steal crypto keys because it's not designed to store crypto keys. Um, and so it's just secure as...

**Chris Gammell:** I mean, it's still, it's still some small thing you're plugging into USB port that, you know, you could have malicious code on there, but at the same time, you know, I plug in keyboards and mice all the time too. So it's like, you know.

**Tim Mithro Ansell:** Um, but what the code on there is what you put on there, right? Um, sure. And so... Right.

**Chris Gammell:** If you go and flash it right before you plug it into your computer. Yeah, of course.

**Tim Mithro Ansell:** Yeah. And you can put whatever you want on it. Like, um, an example I was thinking of is like, maybe it only responds when you tap your name in Morse code on it or something like that. Right. Like, um, there's no, you could do whatever you want. And, um, I would not, if I was the Dalai Lama or a higher, like the president of the United States or something like that, don't use the Tomu as your security factor authentication. Please do not. If you're a high value target, do not. But for my mum, who is going to get phished by, you know, Nigerian prints scheme, actually it's more likely my dad. My mum's actually pretty tech savvy.

**Chris Gammell:** Um, my dad getting... We all have someone in our lives that are going to, yeah, they're going to get phished at some point.

**Tim Mithro Ansell:** Yeah, this helps prevent that happening. And, um, we can improve and iterate on the software again. Like if somebody wants to go and security order that software, that would be awesome because it allows us to check where those bugs are. It doesn't, um, like the hardware is, we're not dependent on some hardware feature being working some certain way for it to have. It's just software. And as I've been kind of banging on, um, through this whole interview, software is really easy, right? Like, um, you can iterate fast. Yeah.

**Chris Gammell:** Let's just, let's just, uh, go breeze right past that one. But sure. Yeah. Yeah. Software is really easy compared to certain things. Easy to iterate quickly. Let me say. Yes. I do agree with that. Yes.

**Tim Mithro Ansell:** It's not easy to get right, but you know, nothing's easy to get right. Um, right. And like, one thing I try and say is like, I'm a terrible software engineer and I think everybody's a terrible software engineer. We all write bugs, um, all the time. And, um, the only way we're going to write better software is if people work on it together and actually work on improving it and help it trend upwards, um, improve it as they work on it and iterate on it and try new ways. Maybe, um, like the current U2F firmware is written in C. Maybe that's a terrible choice. Maybe it should be written in Rust. Um, and maybe Rust will make it so much more secure. Um, but because this is a something, it's just an ARM microprocessor that you can GCC for, um, somebody could write a Rust two-factor authentication thing for. And I would like to share the Tomu and share it with people and that would be awesome. Um, yeah. So. Right.

**Chris Gammell:** But yeah. Okay. Cool. Um, uh, so what else is, uh, so what else is on your list here? You had, uh, stuff about, uh, sorry, I lost the list too. So the Tomu though, is, uh, funding still or no?

**Tim Mithro Ansell:** Um, it's just about to open funding. Um, okay. So, um, I'm a busy person and I didn't really have time to, um, uh, do anything despite there being a U2F firmware and designs and all that type of stuff. And lots of people don't want to make their own. Like, and I love making hardware, but like, even I don't want to make my own most of the time. Um, and so I emailed, um, Sean Cross, Zobs, um, saying on the off charts, he was interested. I totally expected him to say no. Um, and for some reason he said, yes, I would be interested in taking, I guess, taking this to market. Um, and so I've basically handed over the project reins to him and, um, made suggestions and stuff like this. Um, but he's running the crowd supply campaign and I have like all confidence in him, um, um, uh, making that successful. Um, and kind of. Cool. Um. Do you know when the, the date of that is that it's opening? Um, it'll hopefully be open by the time this goes live. Um, I think in like the next day or two is when they're planning on launching it. Oh, perfect. Perfect. Yeah. Definitely before Linux.com for AU. Um, because.

**Chris Gammell:** And when is, when is that happening?

**Tim Mithro Ansell:** Uh, that's the 26th of January, I believe. Um. Okay. Um, last week, January. Um, because, um, again, um, one of the things I strongly believe in is that Ompasource helped me a lot, um, and got me the high paying job I have today. And so I want to give back to that community. And so we'll be giving everyone who's tending LCA a Tomu board to play with and do with, um, what they want. Um, if they're not going to do anything with it, hopefully they'll hand it on to someone who does. And, um, that's kind of just a thank you to that community for, um, supporting me as I grew as a, um, software engineer. Like, I don't think I would have had the job I have now if it wasn't for, um, all the people who gave time to like review my terrible code that I wrote as a kid. Right. Like, um, right.

**Chris Gammell:** So you're giving a, uh, you're giving a workshop at this though, the, about FPGAs and Linux and Python. Is that right?

**Tim Mithro Ansell:** Yep. Um, lots of things happening at LCA, um, this year, um, moving back to FPGAs, um, again, lots of people are scared of FPGAs and scared of hardware. And I guess because FPGAs are kind of hardware, they're scared of that. And so at LCA, I'm running a day long tutorial where I'm, um, walking people through running Linux on a FPGA using a completely open source, um, soft core. And the basically configuration of this system is all done in Python.

**Chris Gammell:** Oh, interesting. So what, and what is that called? Um, what's the soft core?

**Tim Mithro Ansell:** The soft core, um, is open risk one K, but the Python framework we use, um, allows us to switch between a couple of different soft cores. Um, so there's the lattice micro 32 and actually Clifford's, um, Pico, um, risk 32. Um, and like the open risk one K is probably your best choice if you want to run Linux on it. Um, uh, as you heard from Clifford's talk, um, the Pico risk, um, 32 is a good choice. A good choice. If you want to run your, um, um, soft core in the same, uh, clock domain as your, um, peripherals. And the LM32 is a kind of good choice if you want to run a bare metal, um, uh, type system. The LM32 is a very amazing, um, soft CPU because it uses a, a astonishingly a small amount of resources.

**Chris Gammell:** Um, Oh, it's just like a real tight, real tight configuration within the FPGA.

**Tim Mithro Ansell:** And it has upstream GCC support. Oh, interesting. Um, and so that is kind of why we use the LM32 in most of our projects when we're not targeting Linux, um, because of this upstream GCC support.

**Chris Gammell:** Um, and so this is a lattice soft core. The LM32 is a lattice soft core, but you guys are using the RDA seven. Is that right? Yep.

**Tim Mithro Ansell:** Um, okay.

**Chris Gammell:** So there's no problem retargeting that stuff towards the Xilinx FPGA.

**Tim Mithro Ansell:** Um, it's all released under, I believe, a BSD license. Um, and so we can use it on any FPGA. And in fact, I'm pretty sure people have used it on LADA stuff. They've used it on Atera or Intel stuff. They've used it on Xilinx stuff. Um, so, um, I actually believe, um, Florence, the guy who does a lot of the Litex stuff, um, at CCC got it running on, um, the Ice 40. Um.

**Chris Gammell:** Oh, cool. Yeah. And I believe. Which is what Clifford was talking about.

**Tim Mithro Ansell:** Yeah. I believe it beats out Clifford's Pico risk in terms of, um, size on that. So, um, we'll have to have a little bit more look, but, um, it is actually a pretty awesome piece of technology. It's kind of, um, sad that Lattice hasn't got any more recognition for this awesome thing that produced. Um, but.

**Chris Gammell:** So, so tell me a little bit more about this flow too. So you're, you're using Linux. Yep. To, to implement these different soft cores on the hardware, on the FPGA. Yep. But then, and you said at least the LM32 is GCC compatible. Yep. Do you then write C for it or, and it's targeted with, there's a port for GCC for it or is it, I don't even know if that's the right terminology, but, or, or, and then are you writing Python once again to actually target these processors?

**Tim Mithro Ansell:** Um, so at LCA works explicitly running Linux on the soft core. Um, okay. So they will be writing C code, um, that for basically Linux kernel drivers, um, for hardware they've designed in the FPGA during the tutorial. Um, okay. And so they'll define, design a little crypto accelerator and, um, then write a Linux driver for it and do a, um, uh, like do some crypto acceleration on the FPGA as kind of like a demonstration of what you can do. Um, and trying to make it less scary.

**Chris Gammell:** Um, this sounds like a ton of stuff for a single day course.

**Tim Mithro Ansell:** We are going to have to gloss over a bunch of stuff. Um, but it's not as hard as people kind of, um, uh, if you have your software abstractions at the right level, um, you can get by without having to understand like all the minute details of how Verilog works. Um, right. Okay.

**Chris Gammell:** Like that's, and that's interesting too, because that is usually a tripping point for some people. Yeah. So you don't touch the Verilog at all. It's just all generated or what?

**Tim Mithro Ansell:** Uh, yeah. And so we have Python code that generates Verilog, um, and it actually generates, um, C stubs and device tree as well. Um, and so, um, the idea is that if a peripheral moves, for example, or you add a new peripheral, um, these generated outputs, like the device tree just gets another definition for the new peripheral automatically. Um, and so it becomes very easy to iterate really quickly because, um, you don't have to worry about like, well, where do, what register location do I put this at? It just goes in the next one. Right, right.

**Chris Gammell:** I hard coded this address and now that the thing's not there anymore. Yeah. Well, that's why people shouldn't hard code addresses, but yeah.

**Tim Mithro Ansell:** Yeah. And so that's what we're doing at LCA, but we also have a project to, instead of running Linux, running, um, MicroPython as the firmware running on the soft CPU.

**Chris Gammell:** Oh, interesting.

**Tim Mithro Ansell:** And so in that case, you'd be writing, instead of writing Linux drivers, you'd be writing MicroPython code.

**Chris Gammell:** Um, interesting. Okay. And so that's just a little bit more accessible because you're mostly, um, Python, Pythonistas. Yes. Uh, and there's actually. And so they're, they're used to that as a way to then toggle IO and low level stuff. Right.

**Tim Mithro Ansell:** Yeah. And a really, really interesting thing is we have these, um, what we call bridges that allow you to, on your host computer, talk to the, um, wishbone bus that connects everything together inside the FPGA. Yeah. And so you can write Python scripts on your host computer that read and write registers for the peripherals you've created inside the FPGA. Um, now with MicroPython running on the FPGA, in theory, you should be able to take the same scripts that you're running on your host computer and just run them on the soft core inside the FPGA. And they should do the same thing because the bridge is just basically gone now. Instead of writing to a bridge, you're writing to direct memory locations, but the API looks the same. It's still, you know, right to LED one on type thing.

**Chris Gammell:** Um, so the idea of being that it could just be embedded somewhere without the actual tethering of, to a computer, you just write the code, turn the LED on and off every second or whatever. It sits within the F that soft core. And that's just a very simple example.

**Tim Mithro Ansell:** But you can do all your development on the host computer initially where you've got your full IDE, you've got your full tab completion, all those type of tools that people like. Um, you can control C it halfway through, um, you know, all this type of niceties. And then once you've got it right, you put it on the FPGA. Um, because, um, like iterating quickly is much easier when you've got a much more powerful computer that you're using rather than, um, trying to, like the soft cores are quite slow. You know, they're talking hundreds of megahertz. Um, you're like even a cheap computer if you know.

**Chris Gammell:** I was going to say, Tim, you and I live in different, different worlds, but yeah. I know, I know what you're saying relatively, but yeah. Yeah.

**Tim Mithro Ansell:** Um, so, um.

**Chris Gammell:** Okay, cool. No, that's, that's actually, that's a great, that's a great use case. So what is, what is all this, uh, are there names for all these projects as well that people might be able to look up?

**Tim Mithro Ansell:** Um, so yes and no. A lot, again, I have a lot of projects. And so a lot of things, um.

**Chris Gammell:** Maybe specifically for that, uh, that MicroPython flow that you're talking about.

**Tim Mithro Ansell:** We're just in the process of renaming it. Um, it used to be called UPy-FPGA, but we realized we could name it FUPY, F-U-P-Y. Um, so we had to change it to FUPY, right? Like, once you've realized that name exists, um, that's such a better name than UPy-FPGA. Is it?

**Chris Gammell:** I'm not sure. Time will tell. Maybe, maybe everybody will be wearing FUPY t-shirts someday. Maybe.

**Tim Mithro Ansell:** Um. Okay. I think, um, the real power of this thing is, like, if you're doing a large scale thing where you're, you know, making thousands of something or hundreds of thousands of something, this isn't the right approach for you. But if you're doing prototyping, um, like lots of us in the hobbyists are doing, we're making like one to ten of it. This is a really powerful way to work because it's a very productive and very quick way to work. And, like... Yeah.

**Chris Gammell:** I've, I've actually been doing, I've been using MicroPython with a, uh, one of the, uh, the Adafruit Trinket M0s. And just, you know, basically, you know, effectively peeking and poking with a serial bus. Um, you know. Yeah. It works great.

**Tim Mithro Ansell:** Um, so the problem you have, though, is that's running on a real CPU. And if that CPU, if you need, like, four spy flash, uh, spy controllers... Yeah.

**Chris Gammell:** Right. Right, right. You can't do that. You gotta go redefine that whole, yeah, the whole stack of everything, right? Because that's, like, the, the board package that usually import in MicroPython. You probably have to rewrite that, right?

**Tim Mithro Ansell:** Yeah, um, but, like, uh, hardware, like, the Core Tech Zero probably doesn't have four spy flash controllers. Whereas... Right. ...in the FPGA land, you can just say, okay, let's just add four of them. If you have one, you can just add four. And so... Right. ...it allows us to do a whole bunch of interesting things that maybe wasn't possible previously.

**Chris Gammell:** So, that's a, that's a good example, though. Like, so, so in that case, so you say you, okay, so now you're targeting FPGA. Okay, it's got the LM32 on it. It's got four spy ports, like you're saying. Everything's reconfigured. It's using that device tree, like you mentioned. Yep. You do have to go rewrite some of the MicroPython code as well, right?

**Tim Mithro Ansell:** Uh, no. Oh, really? Okay. That's the, let me caveat this with the... That's the rub? ...when we eventually get to that stage, um, the, it's very much no, the, um, MicroPython, just like Linux, should see that there are now four spy controllers and just provide four copies of the class there that you can, um, like, use. Um, uh-huh. And, um, that's something that doesn't quite work yet. Um, but it does work with simple things like LEDs at the moment. Like, if you define there to be 12 LEDs, um, MicroPython automatically exposes 12 LEDs. If you define there to be two, MicroPython sees two LEDs.

**Chris Gammell:** Um, so this is almost like at a driver level right now. Yes. Where the LED part is the, yeah, okay, so the little level LED type stuff is good, but the, the higher level I squared C interfacing, spy, whatever.

**Tim Mithro Ansell:** Yeah. We just haven't gotten around to finishing that yet. Um, got it. And that's mainly because we've been concentrating on the Linux stuff because I have to run a tutorial on that in two weeks. And so that needs to be finished.

**Chris Gammell:** Um, it does grab priority at that point, huh? Yeah.

**Tim Mithro Ansell:** Uh, but I definitely want to get back to, um, the MicroPython stuff because there's just, um, Linux is a full operating system and there are lots of places where Linux makes a lot of sense. Um, but there are lots of places where it doesn't make a lot of sense. Um, and Linux needs a, like large spy flash and it needs a, some type of DDR memory and all these types of things, um, which pushes the price up of the dev board that you do. Um, right. Whereas like the LM32 running on MicroPython should work fine on a lattice ICE 40 FPGA that, um, is definitely small enough to run on that. And like, even if the LM32, um, isn't the right choice, maybe you're running the Pico RISC 32 on, um, the ICE 40.

**Chris Gammell:** Um, yeah. Like. No, that's great. I, I like, I really liked that because especially because we just talked to Clifford yesterday, or last week, um, you know, that's a good, that's a nice, that's a nice kind of point of like, well, if you're on the ICE 40, you're using like the, a project ICE storm, you can build all that stuff. You can target it. You can use one of these smaller processor cores and then there's, you know, targeting with MicroPython. That's kind of all the way through. That's, that's very interesting.

**Tim Mithro Ansell:** Yeah. And all the language that is used to define that I have spy, uh, for spy controllers, that's all Python based. It's not like it doesn't take Python and convert it to hardware. That's not what it does, but it's like a templating language that lets you easily template out, um, that I want for spy controllers without having to go into the nitty gritty details of what's inside a spy controller and that type of thing. Um, so it's actually quite accessible at a high level. Um, but unlike the kind of, Vivado has like a GUI that lets you do a lot of these type of things. Like you just drag in a bunch of these things and connect them up with like lines and that. Um, you don't get any of the source code for that.

**Chris Gammell:** The tool if people don't, the Xilex tool if people don't know what that is. Ah, yeah. Sorry.

**Tim Mithro Ansell:** The Xilex FPGA tool line. They're new fancy one. Um, right. And, but the problem is like, if you find a bug in the spy controller, um, maybe you don't have the skills to fix it, but maybe you do. And maybe you want to fix it and then you can fix it and send us a patch and we'll include it. And then it's fixed for everyone. Um, you know, again, the power of open source is having this kind of continual improvement and why I want to continually iterate and improve things is this, um, like when you fix a bug, we shouldn't have to fix it in every single thing. Every time from scratch, we shouldn't be writing yet another I squared C controller or yet another spy controller. There's a good reason to sure, but it shouldn't just be because, well, I feel like it, like you've got better things to do with your time. I hope. Um, right.

**Chris Gammell:** But well, speaking of time, we are running out of it. Uh, where can people, uh, where can people find you at conferences? Because it seems like you're kind of bouncing around to conferences and also where can people find you online?

**Tim Mithro Ansell:** Okay. Um, so I'm pretty much on IRC all the time. Um, for those who don't know, IRC is like what us old fogies use instead of Slack.

**Chris Gammell:** It's like Slack from the old days. Yeah.

**Tim Mithro Ansell:** Yeah. Slack before Slack. Um, right.

**Chris Gammell:** Right. It's almost like Slack just replicated all of the functionality of IRC. Yes. Um, with gifts though, with animated gifts. I mean, come on.

**Tim Mithro Ansell:** Yeah. My client does all that Slack type thing as well. Um, yeah. Anyway, on IRC.freenode, um, dot net, um, on the Tim videos channel.

**Chris Gammell:** Um, oh, you got your own. Okay. Yep. Own channel. Yep.

**Tim Mithro Ansell:** Um, that's where I think we've got about a hundred people in that channel these days. Um, just hanging out, um, people doing recording all different types of, um, conferences around the world and that type of thing. There's a bunch of people from, um, the CCC, um, group there. There's a bunch of people from DebConf and Fosdem and a few other things. Um, so yeah. Are you going to be at, are you going to be at Fosdem coming up? Um, sadly not. Um, I will be at LCA obviously, um, because I'm giving the tutorial there and I don't quite know what conferences I'll be at after that. Um, but if you follow me on Twitter, I'll tweet when I'm going to go to, um, conferences. It's just Mithro on Twitter as well. Um.

**Chris Gammell:** That is the nice thing about handles. They, they usually stay the same place to place. That's good.

**Tim Mithro Ansell:** Yeah. I got lucky in that it seems to be rather unique. Um, or at least it was up until recently. Um. Got it. And yeah, you could also email me. Um, I try and respond as quickly as I can. If you haven't heard back from me after a week, please send me another email because you've probably dropped off the, um. Or send help. One of the two. Yeah. Yeah. One of those two. Um, but yeah. And like, I want to like reiterate is that if you contribute to my projects, um, and I feel that not having access to hardware shouldn't be what prevents you from contributing to my projects. Come along, help out, and I will figure out some way to get you hardware, um, so that you can be more effective. Um, whether it's Tomu or Tim videos or HDMI to USB or just recording conferences or any of these type of things. I very much, um, love it when people are using my stuff to do cool and awesome things. And if it's going to cost like Tomu's a cup of coffee, if I can shout you a cup of coffee in hardware, then, um, that seems like a pretty good deal for me. Um, I think so.

**Chris Gammell:** Yeah, that's great. Yeah. Awesome. Well, Tim, thank you so much for, for being on the show and sharing your projects and, you know, being generous with the hardware too. That's awesome.

**Tim Mithro Ansell:** Yeah. And we only got through like, I think about half of them. Oh, really? Yeah. Okay.

**Chris Gammell:** Well, we'll have to have you back then too. Yeah.

**Tim Mithro Ansell:** Oh, it was really nice chatting with you and, um, thank you for having me on.

**Chris Gammell:** Talk to you soon. Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye. Bye. Thank you.
