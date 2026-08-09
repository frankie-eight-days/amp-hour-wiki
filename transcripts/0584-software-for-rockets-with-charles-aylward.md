---
episode: 584
title: Software for Rockets with Charles Aylward
url: https://theamphour.com/584-software-for-rockets-with-charles-aylward/
---

**Charles Aylward:** This is The Amp Hour Podcast. Released April 3rd, 2022. Episode 584. Software for rockets with Charles Aylward. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Charles Aylward:** And I'm Charles Aylward of Grizzly Peak Systems.

**Charles Aylward:** Hi, Charles. How are you doing? I'm good. How are you doing? I'm good. We know each other from the consulting forum, but also your name has come up a bunch in, you know, like firmware kind of consulting things. And past guest Todd Bailey said he was working with you, I believe, at a new space company.

**Charles Aylward:** That's right. Yeah, we both worked at Astra together. That's actually how we met.

**Charles Aylward:** Oh, cool. Okay. So we met on the job. Yeah. And we have not caught up with Todd in a long time, but he's been doing lots of spacey type things in the meantime. So we were talking about this a little bit before the show, but what is new space? How do you define new space versus just space?

**Charles Aylward:** Right. Yeah. So, I mean, it's certainly not an official term of any kind, but people who work in new space, I think probably sort of differentiate it from old space. Sorry. So it's the difference between maybe like, say if you're taking the extremes, like a sixties or seventies, or even just like eighties, like NASA approach, like kind of a top down design, really using basically.

**Charles Aylward:** Waterfall method and a subcontractor to subcontractor, subcontractor type of thing or.

**Charles Aylward:** Yeah. I mean, maybe, maybe it has less to do with like how deep your contracting goes, but it definitely has to do with like the, basically like the specifications of the parts that you're willing to tolerate. Right. So NASA is not going to take any chances, right. With anything. Right. So I don't, I've never worked at NASA, but I presume they spend a lot of time in analysis. And I've certainly read some papers that lead me to believe they spend a lot of time with lots of really rigorous analysis and they know for sure that their, you know, systems are going to work. And if you're sending something to Mars, right. That has to be the case. It's gotta,

**Charles Aylward:** it's gotta be, yeah. A thousand percent tested. Yeah. Yeah. And I always think about like rad hard parts, you know, you see them on like a DigiKey or Mauser and you're like, Oh, why is that part? Why is that, you know, 20 year old CPLD costs $3,000. And it's because it's rad rad radiation hardened or whatever. And they've done all this pre-testing on it and pre characterization.

**Charles Aylward:** Right. It's like, right. It's like 40 megahertz CPU and it costs like, you know, $12,000 or something.

**Charles Aylward:** Yeah. Z80. It's that, it's the new hotness. Yeah.

**Charles Aylward:** So new space to contrast is sort of taking a slightly different approach. So in the case that you're not sending things to like Mars or even necessarily like the moon or something, you're just sending it to orbit, like generally low earth orbit. The idea there is build smaller, cheaper things. And because they're smaller and cheaper, you can afford to send more of them. And because you can send more of these things, then you don't have to max out all the specs because of one in three fail, maybe, or whatever, whatever it is you decide for your mission. One in three fail, maybe that's still fine.

**Charles Aylward:** Right. Yeah. And we've, we've talked to people on the show before. So we've had Sean on from planet labs. We've had your son from hyper. We've had, I forget the last one, but I think that was all on the payload side. So like things that were going up to space, you guys were working on the thing that was launching. Is that right?

**Charles Aylward:** Correct. Yeah. So we were working on the launch vehicle and I mean, we could talk about like the, the thermal and radiation environment and all that a little bit too. Maybe in general, once you are in LEO, I mean, you have to care about these things, right? You have to care about radiation and the thermal environment. So whether it's a payload or the launch vehicle, you kind of need to care about the same amount.

**Charles Aylward:** Okay. And so this is a launch vehicle. I remember, I only read a couple articles about Astra in general, but a much smaller rocket. Is that right? Like it's kind of like meant to launch small sats or what is, what is the, what is the nature of the launch vehicle?

**Charles Aylward:** I guess. Yeah. You would just call it a smaller launch vehicle. So, you know, it's, they're like in the class of like a rocket lab vehicle. So these things kind of like all feed each other. Right. So I think if we go back, planet labs are now just planet sort of really proved this idea of using a little bit more like commercial software or commercial electronics, you know, commercial level electronics instead of like rad hard systems. And then you can just fly a lot of these things. And so they sort of prove that, you know, this sort of like lots of small systems kind of can compete with, you know, single big expensive system. But then there's still this problem of, well, how do you get it to orbit? Well, you have to like find some massive rocket and maybe try it. Like it's either going to be really, really, really, it's going to be really expensive to send all of your payloads or you can, you know, maybe find a ride share. And then the problem with, you know, finding, finding a, a ride share where you're basically tagging along with other, some other major payload.

**Charles Aylward:** Search pricing. Is it the search pricing? Like, yeah.

**Charles Aylward:** I mean, you're, you're kind of subject to whatever you can get in terms of the availability, but then also you, you have no control over when you're going to launch.

**Charles Aylward:** Yeah. Right. Right.

**Charles Aylward:** So it seemed, I think obvious to quite a few people that there's a niche there. So that's cool. A rocket that is commensurate with small sets and cube sets commensurately sized.

**Charles Aylward:** Yeah. So kind of like shrunk down. Isn't there like a, so I, I remember seeing a talk about the rocket equation. I have no knowledge of the rocket equation other than remembering. I went to a talk about it, so I didn't pay attention very well, but isn't there like a size thing anyways, like where as you get bigger, you need to carry more fuel. That's, that's the main gist of what I remembered. Like, so does that advantage a smaller rocket or does that disadvantage a smaller rocket?

**Charles Aylward:** It's an advantage. Yeah. So, so, so the main gist of like the limit on the rocket equation is that as you get a bigger launch vehicle, most of the weight you're carrying is fuel. Right. So at some point you're, you reach this like lot, there's like, you know, a diminishing return where eventually you're just basically spending all of your energy transporting fuel.

**Charles Aylward:** Yeah. Yeah.

**Charles Aylward:** And so if you, if you, if you're looking at like the ratio of the dry mass of the vehicle to like how much fuel you need to get it to certain orbit, right. You can kind of like graph these things and figure out how big a vehicle you need to get so much mass into orbit at a certain orbit. And then you can kind of, you know, figure out how strong do the engines need to be? That sort of thing. Kind of flow down through the design that way.

**Charles Aylward:** Yeah.

**Charles Aylward:** That makes sense.

**Charles Aylward:** Yeah. I mean, at least, you know, at a very, very high level right now, I'm like, yeah, Charles makes a ton of sense right now. And this is, I think I'm a rocket scientist now.

**Charles Aylward:** Sometimes I haven't tried to actually explain it at any particular level. So it's kind of a, okay. An exercise right now.

**Charles Aylward:** First pass. It was great. It was great. So, I mean, you were not designing the rocket part. You were designing the control piece, I believe.

**Charles Aylward:** Correct. Yeah. So I'm definitely not a mechanical engineer or a propulsion engineer, et cetera. Yeah. Or fluidics engineer. So.

**Charles Aylward:** Yeah.

**Charles Aylward:** There was a team that, you know, is focusing on the propulsion system. So basically the actual engine design. And there's a structural team, you know, working on tank design and basically how the engines get mounted and all that sort of thing. And, uh, I worked on the electronics and software, although originally actually is mostly just software. And there's a couple of different classes of software on the vehicle. So kind of broadly speaking, you would have sort of power management systems and then your sort of flight control systems or avionics systems.

**Charles Aylward:** One thing that I wanted to have is kind of like an overarching topic for this episode, because Charles and I interact on the consulting forum as well. One thing that I admire about him is the level of rigor that he puts toward that you, I'm talking to you, I suppose I'm talking to the audience as well, but like the rigor that you kind of bring to your engineering practice. And I thought that actually plays really well in the, uh, in the big things go boom space, also known as a rocket. Uh, how does, how does that all play together? I mean, like what, what is it? Uh, how the hell do you know that you're ready to hit the big red button and launch that thing into space from a software or hardware space? perspective.

**Charles Aylward:** Yeah. Well, of course they're, they're pretty intimately related. So, right. Yeah. So, yeah, I mean, just like starting from the, the, the main point you made there, uh, right. You're, you're talking about a lot, even a small launch vehicle, you're talking about a lot of energy. You don't want that to fall out of the sky in the wrong place or right. Just chaotically end up somewhere. It's not supposed to. And then even from, even before you hit that big red button, when you're testing the vehicle, there's a lot of things you want to make sure do or do not happen. You know, there's a lot of very strong actuators on there. You want to make sure, you know, if a technician is in there changing or modifying something, something's not going to like suddenly move, rip their, rip their finger off, connect the power to something and an actuator, right. Tears your arm off or something. These are other, other things you don't want.

**Charles Aylward:** That's going to ruin your coding efficiency for sure.

**Charles Aylward:** Right. Yeah. I guess we could, I guess I could start at sort of like maybe a generalized process that I would run through for.

**Charles Aylward:** Sure. I mean, sure. I, I guess one thing is, uh, I mean, how big is it? So you said new space and, you know, I think startup, but like how big is a team that's doing all this stuff? Like how many people are you, is it just you writing software? Are the other people writing stuff? Like how does it all interact? I guess at a very, very high level first.

**Charles Aylward:** So this is probably a unique experience generally, but there was a joke for a long time that I was the software team at Astra. Oh, wow. Okay. Yeah. At least, at least for the vehicle, for like the flight controls software.

**Charles Aylward:** Yeah.

**Charles Aylward:** I mean, there are other software engineers working on, ground systems for sure. For a good chunk of the first one or two launch vehicles, I was sort of the, the single flight control systems, like software engineer with one exception, which would be the actual guidance, navigation and control algorithms. There's a, an engineer who focused on the, the sort of control algorithms. So, you know, let's say two engineers.

**Charles Aylward:** So, so then what do, what do design reviews look like then? I mean, is it, that's, that's gotta be kind of crazy. I mean, either, either you're checking your stuff so rigorously or setting up tests or whatever, but like, yeah, what does a design review look like then?

**Charles Aylward:** Yeah, that was, that was quite a, quite a challenge early on. And until, I mean, we later on, of course we did build out the team a little bit, so could actually have a little bit more rigorous, you know, design reviews. And even though you mentioned Todd Bailey, even though Todd Bailey was sort of focusing on electronics at the time, I mean, he knows firmware as well. And, you know, we bounce a lot of ideas off of each other and he certainly helped to review a lot of my work. So it wasn't, it wasn't totally me in terms of like testing and the sort of rigorous part, but in terms of day-to-day typing code into a machine,

**Charles Aylward:** it was definitely mostly me. That's a, that's a lean crew. I mean, that is a lean crew. That's, that's impressive.

**Charles Aylward:** Yeah. It's certainly not advised. Like that was, that was, it was one of these things where when I interviewed, it wasn't hidden from me that I was basically the only person at the time. And, you know, I think when I interviewed, the idea was go from basically zero to launching in six months. And I was like, wow. You know, okay.

**Charles Aylward:** I mean, that's, that is an exciting proposition though. Like that is like, Oh, okay. Yeah.

**Charles Aylward:** And I did make a mistake thinking that, well, I know how stressful this is going to be going in and how, you know, grueling that is going to be. And because I know that that'll help. And it kind of turns out that doesn't help that much.

**Charles Aylward:** Yeah. So still only 168 hours in the week and sleep a little bit, I guess. And your code goes down as your, your sleep goes down and yeah, that sort of thing. Right. Yeah. So is, is there a dev kit that I can buy that like, where, where does one start then in, in the whole, like, all right, we're going to put something in space. It has to be controlled. We're there's no dev kit. I am guessing.

**Charles Aylward:** No, there, there, there definitely is no dev kit. Although there's certainly a lot of like example kind of systems and depending on how you decide to design these things, of course, there's existing software you can kind of maybe build off of, you know, we can maybe get into a little later, but like one of the things that's going to come up is like, well, you have real time constraints. Do you use a, you know, real time operating system or in which one do you use? That sort of thing.

**Charles Aylward:** Yeah.

**Charles Aylward:** Kind of, kind of going back to like, well, if you have a really lean team, how do you structure things so that you can be reasonably sure what the system behavior is going to be? And I think one of the things that Todd and I worked on before we wrote a single line of code, it was really great idea was we kind of came up with a set of what we called, like at the time we called them guiding principles. I've called them other things at other places, but guiding principles with regards to system architecture. So like sort of high level things.

**Charles Aylward:** Give us an example one, maybe.

**Charles Aylward:** Yeah. Yeah. So the first thing, the first thing you want to do is figure out what classes of problems you have. Right. So in something like a launch vehicle, it's not feasible to just have like a single embedded, like compute device with all of the sensors and all of the actuators plugged into like, you know, a single CPU or processor. Right.

**Charles Aylward:** So no Arduinos.

**Charles Aylward:** Right. So it's, you know, it's very likely that when you, you know, like think about these things, you're going to have like these natural sort of boundaries, like, well, you're going to have electronics on a, on a engine and that engine should sort of know how to do engine things. And right. You have a flight computer that knows how to do guidance, navigation things. And then you have different controllers that maybe know how to like open and shut valves and read temperatures, that sort of things. So because you have these different systems, you off the, you sort of off the bat have minimally a distributed systems set of problems. Right. Like what does it mean to have a distributed system? The simplest way to put it would be you have slow or potentially lossy communication channels between systems. Right. There's a, there's a couple of different ways you can best,

**Charles Aylward:** best case is asynchronous, right? Yeah. Perfect. Perfect asynchronous system.

**Charles Aylward:** There's a couple of different ways you can approach thinking about distributed systems. Another one would be like, you have more than one clock on the system. Yeah. Right. So you have a, in the case of like a launch vehicle, you might have a, the flight computer has a clock because it needs to have very precise timing to do all of its guidance algorithms, navigation algorithms, but then engines also need to be able to very precisely synchronize things. So they might need their own clocks. Right. So now you have like two clocks that you need to, you know, deal with that problem. Yeah. But in general, anytime you have a system where communication between two things can either like in terms of like, if you're talking about packets, you can miss a packet, a packet could be delayed. You get two packets out of order. Right. That sort of thing. Or you could get the same packet twice perhaps. Right. So you have to be able to anticipate those things. And then sort of going back to like, what classes of problems do you have? Well, the timing for starting and running a rocket engine is very precise. And sometimes they're very small amounts of time between, you know, actions that need to occur. There can't be like a large variance in those timings because you're controlling valves and there are fluidic effects and that sort of thing. And so, you know, you can't like flood the engine. You can't starve the engine, that sort of thing of just using very general terms. Right. So. Yeah.

**Charles Aylward:** Yeah.

**Charles Aylward:** You need to have precise timing. So you have, and then guidance and navigation as requires precise timing. So you have, you know, a real time, you have real time classes of problems, right? You can't be late solving your navigation solution. Right.

**Charles Aylward:** Okay. So you're saying like you have hard deadlines. You have to meet in addition to lossy comms, you have to be able to synchronize and meet deadlines between different domains.

**Charles Aylward:** Right. Yeah. I mean, if you, if something like on a, you know, if you're like talking about a car or a launch vehicle or whatever it is, of course you, from a physical standpoint, you want to assume that you don't have lossy comms. Let me rephrase that from a physical standpoint, you want to design the system to not have lossy comms, but from a software perspective, you have to design around the fact that you might have lossy comms. Right.

**Charles Aylward:** Yeah. So like acknowledgements and things like that, or ways to tell if you've delivered a message,

**Charles Aylward:** if nothing else, it's a very noisy environment and you might actually just simply have bit errors on the line. Right. So, Oh,

**Charles Aylward:** wow. Yeah.

**Charles Aylward:** Right.

**Charles Aylward:** So then I think CRCs and other ways to validate that a message is legit.

**Charles Aylward:** Yeah, exactly. Yeah. So, so well, that does feed into like, going back up to like this coming up with a guiding principles for your, for your software, for your, actually not even necessarily for your software, but just for like the behavior of the system. Right. So from the highest level, really what you're trying to get is a system that's testable. Right.

**Charles Aylward:** Yeah. Yep.

**Charles Aylward:** But also very importantly that like you can understand it, right. Like you under, you can understand basically somewhat small enough that you could fit it in the human brain. Right. So if you have two systems, you know what the behavior is going to be given any particular, whatever command sequence. Right. So you want, you know, high levels of determinism in your, in your system.

**Charles Aylward:** Oh, okay. So not like, you don't mean like human readable, like it's not like sending Jason packets between, between two domains or something. You're, you just mean that it's not overly complex.

**Charles Aylward:** Yeah. Right. So, I mean, maybe the best thing to do would just be to get into a couple of, of these principles that I've thought about. Sure.

**Charles Aylward:** Yeah. That'd be great. Yeah.

**Charles Aylward:** Yeah. Give you some examples. Right. So the first one I start with usually is no modes. So your software doesn't have basically like fundamentally different operating modes. There's only the mission mode, right? So you don't have like a test mode. You don't have a debug mode. You don't have these different modes. You can put it in where the total system behavior can suddenly be radically different.

**Charles Aylward:** That is a great one. Oh my gosh.

**Charles Aylward:** Yeah. That sometimes even includes like things that seem like they would be a good idea, like safe modes. Right.

**Charles Aylward:** Mm hmm. Yeah. Cause then the question is, well, why isn't everything safe? Why isn't everything safe in some way? Right. Or.

**Charles Aylward:** Right. Like there's, I can't remember the link exactly, but there's, there's a, there's a, there's a gentleman who basically catalogs all of, you know, basically like software failures on space systems and a very large percentage of those failures are from a mode. Basically the system decided something wasn't right and it put itself into a safe mode. Simultaneously some other system put itself into a safe mode. And that second system was the thing that took, should have taken the first one out of safe mode. And then like the, the system is just like permanently safe. Right. That's like a simple. Safe as in like inert. Exactly. Yeah. There's some pretty famous, like high profile systems that have failed for, for, for reasons like that. And so this kind of follows into like some of the other principles you might have, which is like, well, if you don't have modes and you don't have a test mode, well, how do you test it? One principle might be debug data and test data is first class data. There's no difference between test data and like mission data. And so like, well, what does that mean for like a software system? So basically means exposing in your telemetry, however, you're getting that telemetry, basically synthetic sensor data. Right. So generally you're, you already have like a bunch of sensor data and a bunch of commands going out to actuators. So you're already dealing with like sensor data. And I found it somewhat surprising. Some people tend to get hung up on it being like a physical sensor. And, you know, there's no reason you can't just have a synthetic sensor data piggybacking in on this, you know, sensor system you already designed. So, you know, simple things like error counters and, you know, a counter for like CRC failed failures and things like that. Or counters for failed or like missed deadlines, average latency to read, you know, some ADC somewhere way down the line, that kind of thing. You can just pipe all these things in with your sort of mission data, like temperatures and actuator positions.

**Charles Aylward:** So I guess, how do, how does this get treated in other systems that you were kind of not doing it the traditional way, I suppose. Sorry. Like what does test data and debug data look like in, systems that you were not designing?

**Charles Aylward:** Oh, well, I mean, I think just so like, it's a really generalize it. I think it's just sort of approaching the software with the perspective that if something unexpected happens during testing, like from the, from the behavior of the system, something unexpected happens during testing, do you need to like hook up a JTAG connector to figure out what's going on? Right.

**Charles Aylward:** Ah, I see. Okay. So it's about exposing interfaces and data so that it's kind of always available.

**Charles Aylward:** Yeah. It's exposing your internal state as much as possible. Right. In like some meaningful way.

**Charles Aylward:** I always kind of assumed that wasn't the case because there was maybe constrained channels. Like if, so using a very, very simplistic example, if you have a, you aren't running at like 115 K, then like you could only get so much data through that. And if you have to choose between mission data, which you're putting through a UART for some reason, or test and debug data, you would deprioritize the test and debug data. Is that, is that a fair statement?

**Charles Aylward:** I'm not sure because you, when you're doing the system design, you can kind of, it's sort of a, I think that, I think the way you put it presupposes that the electronics are just being dumped on you post-talk. And then you have to like figure out how to get the stuff fit in there.

**Charles Aylward:** Oh, we actually, what I'm really asking is, I was wondering if you had to the kind of up spec communication mechanisms in order to fit a wider volume of traffic or larger volume of traffic. As a result of this.

**Charles Aylward:** Yeah, that's, that's true. So you would, you would, you would, you would need to like, you know, you're definitely not talking about 115, 200 K or 115, 200. Yeah. Yeah. You are.

**Charles Aylward:** It's a bad, bad idea to squeeze it all through that tiny pipe.

**Charles Aylward:** Yeah. So, so, you know, if you have a moderately fast canvas or if you're using ethernet, right, chances are you've got the bandwidth and let's say 10 or 20, you know, synthetic, you know, software sensors is probably not going to kill your budget.

**Charles Aylward:** Yeah.

**Charles Aylward:** Yeah. Or, or you can just approach it from the perspective of making sure you have that bandwidth so that you can include the software. Yeah. Telemetry.

**Charles Aylward:** Right. Well, it sounds like this is an important enough design principle that like, it's something that you want to design in because it, it will save costs later in terms of failures, right? That's basically what you're designing in here. It sounds like.

**Charles Aylward:** Yeah, exactly. But also just, it's sort of, um, fans out into the way that you are managing mission operations. Right. So it, it decreases the difference between running a test campaign and running the mission campaign. Right. So that when, when things are on the bench and you're, you know, running like maybe a fake mission on the bench or something in many respects, you want that to look as minimally different than the actual mission. Right.

**Charles Aylward:** Right. Yeah. You don't want to get on the launch pad and be like, Oh wow, there's a lot more data now.

**Charles Aylward:** Right. Or, or, or the other way around, like, Oh yeah, I guess I was relying on this data that I was getting over J tag or like my debug. You are.

**Chris Gammell:** Yeah. Yeah. Did we, were we not piping that, uh, those four sensors back to the, to the main, uh, control.

**Charles Aylward:** Cause that's kind of important.

**Charles Aylward:** Right. Yeah. So a lot of these things come, come down to making the, the, the final system operate in the same way that you would be doing test or debug. Right. Sort of things. So, so like anytime, so like in the early bring up of your system, you encounter some problem. It might be very tempting to like very quickly, just sort of throw J tag on there, you know, dump some stuff over you are. And, you know, if I was working on a commercial system that like that, that's probably fine. Yeah. Because, you know, once it's in a plastic shell and on a shelf or whatever, you're way past where you're going to care about debug data, but that's not necessarily the case for something like a launch vehicle or something. Anytime you encounter some error or bug early on, figure out how you can get that data in the sort of data stream that you're already consuming. Right.

**Charles Aylward:** Yeah. Yeah.

**Charles Aylward:** And yeah, it takes a little, it takes a little bit more work, but it pays off in the long run because you get that sort of observability into the system.

**Charles Aylward:** When you say, so you're saying some people would, in the absence of having all this sensor data kind of out on the main channels, you're saying they would have it as like, like you're talking about like trace data. Like, so you may be exposed trace data instead of plugging in a J tag. Is that kind of what you're saying? Or why did you, why did you say a J tag on there?

**Charles Aylward:** I use J tag as an example in terms of like the, the richness of the data that you can expose. Right. So let's say you have a real time operating system with a bunch of tasks running. You can instrument when a task was activated, how long it ran, did it like overrun it, it's constraint, it's real time constraint. Yeah. You know, basically failed a deadline. Yep. And you can, so you can either emit that as like a constant stream or you might determine that, well, I don't need to have a stream of every single time this task ran, that, that might be ridiculous, but you can maybe maintain some statistics on it. Right. So minimum runtime, maximum runtime, average runtime, and then like a counter for the number of times you miss the deadline. And that'll help you during your early software implementation, and testing campaigns and such. But obviously the idea is to like make it error free, of course, by the time you're sure. Yeah.

**Charles Aylward:** Yeah. Okay. All right. So we have no modes. We have debug data and test data is first class data. Were there any others? There'd be quite a few.

**Charles Aylward:** yeah. So some, some of the like safety, safety slash. Yeah. Let's call it safety. So some of the safety related ones come down to, I guess you would call it like a, the principle of least surprise. Right. So there's a few principles that are related to that. So one might be that when you power on a system, it causes no action. Oh, right. So going back to like that example with like a technician, you know, you've got the vehicle on a, I don't know, maybe it's like, maybe it's not a, maybe it's not a full vehicle, but maybe you have all the systems or maybe you're testing an engine. You have all the systems like kind of flat out on a bench, or maybe you're actually testing a engine or something like that. You don't want someone hooking up the power and then an actuator moves or a bunch of valves click. Right. Yeah. You could either seriously injure someone or cause a fire in the case of, you know, testing a launch. Oh, sorry. Like a rocket engine. Right. Yeah. So that's like, that's a pretty simple principle. Right. So that feeds into like a noble system. Right. So you've just eliminated a whole class of problems.

**Charles Aylward:** Yeah. How would you test against that then? Is that just a, you just powered on a bunch and you say, Oh, nothing's happened. Or is it more like when you're doing design reviews, it's like, Oh, well this pulldown should be, this should be a pulldown instead of a pullup because of the principle, at least surprise.

**Charles Aylward:** Yeah. That factors both, or that, that feeds into the electronics design and the software design. Right. So the software can, I mean, that's a little, it's simpler from maybe a software perspective where you simply don't do anything. Well,

**Charles Aylward:** it was going to set everything to zero.

**Charles Aylward:** Yeah. The next principle I was going to go into would be like boot, boot up causes no action either. Right. Yeah. So simply having the system power on like the software loads for the first time, you know, like your microcontroller boots up or you reset the microcontroller, right. Those things, Oh, sure. Shouldn't cause any action. And the same thing for the electronics, you can maybe say, you know, the, the electronics have to power on in a known, totally inert state. Right. So, right.

**Charles Aylward:** Right. Even if the wrong firmware gets loaded, it's still like, there's nothing that's like, Oh, well you better set that output to zero at the, you know, early in the code or else. Exactly.

**Charles Aylward:** Yeah. In the, in, in your design reviews, you're just checking that like, right. Everything is bootstrapped correctly in terms of right. Pull up resistors and, and that sort of thing, or outside signals are basically excluded from the system or something, you know, if I don't know, dangerous in some way, all of those things sort of feed into another principle, which is, you know, the, the system is only the way I like to put it is like the system's only hot under control. So basically no physical behavior will happen unless there's a control signal.

**Charles Aylward:** That makes sense.

**Charles Aylward:** Yeah. So unless you're, let's say your primary controlling software has come up and issued commands to something, those things do not do things on their own.

**Charles Aylward:** Okay. That's great. I mean, some of these things, like these seem kind of like not space specific. These are just good design principles as well, right? These are, these are great. These are great actually.

**Charles Aylward:** A lot of these things developed sort of over the years for different systems before I kind of got into the new space stuff.

**Charles Aylward:** I think that's really great. Cause it's then extensible and like people listening are like, Oh yeah, I should be doing that too. You know, I think this is just a good design review and design principles in general. So that's great.

**Charles Aylward:** Yeah. I think they, I think they're mostly generalizable.

**Charles Aylward:** So the only one that maybe not isn't is like the rocket fire part should go down normally. Right.

**Charles Aylward:** Right. Yeah. Pointy side up, fire side down.

**Chris Gammell:** That's right. Yep.

**Charles Aylward:** Yeah. So, and then, well, if you're, if you're talking about, well, if these things should only have behavior, if there's a control signal, then this is, this one's not necessarily a given, but you might want to say, well, there's only a single source of control on the system at a time. So that might be like a, you know, a sink, basically a single process. Only a single process is allowed to emit command signals to your end effectors. Right.

**Charles Aylward:** Is that tied into like RTOS type stuff? So you start talking about like the mutexes and the semaphores of the world?

**Charles Aylward:** Not, not, not exactly. Okay. It's more, this is more related to nodes on a network. Who's allowed to send commands to each other. Right. So you don't want to have a multiple, you don't want to have multiple systems issuing commands at the same time. necessarily.

**Charles Aylward:** Okay. So this is like a, who's in charge here kind of thing.

**Charles Aylward:** Yeah. There, I mean, there are systems where maybe you necessarily need to do that, but generally like those are pretty far out there, complicated systems. You can eliminate a lot of complexity and make it, you know, make it an analyzable behavior by simply knowing that only this one system is this one component is the node that can emit like command messages on the network.

**Charles Aylward:** Yeah. Okay. Yeah. And that, yeah, for my troubleshooting perspective, I can imagine that's super critical as well because then it's like, well, the only thing that could make item B do its thing is item A. And so let's go, item B failed. Let's go look at item A.

**Charles Aylward:** Yeah. Yeah. Like all these things, like these things sort of what they're really doing is like, you're limiting the state space that the whole system could be in. Right. Like, Oh, well in certain, if you have a situation where command and control is being passed around to different nodes, right. That becomes really hard to debug. Right. Like you, like you just said, right. Like, Oh, it's like common tutorial problem of like, based on these set of messages, you know, or each time you run the system, like you might get a different result because based on the timing, a different node was emitting commands at a different time. Right. I mean, you just kind of can eliminate those. Yeah. Yeah. Problems.

**Charles Aylward:** Okay. That's great.

**Charles Aylward:** Yeah. Like another one, all of your communication channels. So whatever that is like a ethernet or canvas or RS 45, like those packets are, let me, let me rephrase that. Not packets necessarily, but the messages are globally unique. Right. So what that means is if you say, have a command message for a particular actuator, let's say if you took that packet and you sent it to any other node on your network, it would have no effect.

**Charles Aylward:** Ah, yes. Right. Right.

**Charles Aylward:** So you don't want a situation where if you like, say there's an error in the addressing, you know, a particular bit string of information could be misinterpreted by another, by two different systems. Right. So like, let's say you have two microcontrollers on a bus and one of them is controlling an actuator and one of them like a linear actuator of some sort. And one is controlling a valve or a bunch of valves. Let's say you send a message to control this linear actuator, put it in a certain position. You don't want to have a situation where if you sent that same packet accidentally to, because of the address thing got messed up or something.

**Charles Aylward:** Yeah. Like a bit flip, like you were talking about earlier, right? I mean, that's a worst case scenario.

**Charles Aylward:** A bit flip or whatever, or even just configuration error or something like that. Right.

**Chris Gammell:** Sure. Yep.

**Charles Aylward:** Yeah. You don't want that same packet to be interpreted by this other system and have some different effect. You want it to have no effect. Right. I mean, the easiest way to do that would be like, you have like a message ID in the packet structure and those message IDs are unique to the physical system, but globally unique. Right.

**Charles Aylward:** Does that make sense? Yeah. Yeah. Yeah. I think so. Yep. Yeah. Cause you could have like, I think what you're trying to, I think what you're kind of getting at as well is cause you could have like node systems. You could have like a tree where you might have subsystem A, subsystem B, and each of those subsystems has sub subsystems that might be, they, they each have five sub nodes on each of those. And you're trying to send a sub node number one on sub, on tree A, but you send it on tree B and it still shouldn't work. Right. Right.

**Charles Aylward:** Yeah.

**Charles Aylward:** That's the global piece I can imagine. Cause you'd still have, you'd have like inheritance, all that kind of stuff, but it should still be like, there's no way that even if you send it to the wrong, the wrong neighborhood, that the house address should be so unique. It's just not possible to talk to it.

**Charles Aylward:** Exactly. Yeah.

**Charles Aylward:** Yeah. Like another, another kind of follow on principle for that might be that when you are sending commands to subsystems, you are sending sort of the absolute state that you want that thing to be in. Right. So like a fundamentally, like a simple example would be, you're not sending a command that toggles something.

**Charles Aylward:** Ah, interesting. I thought this was going to be like a calibration type of thing. You're just sending raw values, but you're saying, uh, you're not saying switch state. You're saying go off or go on.

**Charles Aylward:** Right. Yeah. You don't want to have some, something that's like, right. Toggle this thing from you toggle it. Right. So in the case that you miss a packet or you get the packet twice on accident, you know, or something like that. Yeah. You don't, you don't want to end up in basically an unknown state.

**Charles Aylward:** Yeah. That is, that is an interesting thing. I mean, like does in these kinds of systems too, do you go out and query all the things that might be on a canvas on a regular basis as well? Or is it more like you have, you have, so you have a controller and the controller assumes what the state is of all its subsystems and all the sensors and stuff like that. But then because of resilience, do you then go and double check it? Or how does it, how does it really, really know what the current state is of the stuff on the other end of a bus?

**Charles Aylward:** Yeah. Yeah. When you're talking about canvas, it's definitely, and there's two ways, there's two ways to approach generally knowing what all the state is, right? Like canvas specifically is sort of like, you know, you're just collecting these streams. Sort of the default way you think about canvas is like sensor systems are emitting sensor data and built into the protocol is sort of like a collision detection mechanism. So it's okay. It's okay that everyone, basically all of your nodes are babbling basically.

**Charles Aylward:** Yeah. Yeah.

**Charles Aylward:** And the other way of maybe thinking about it is you have a system where no one or no, no subsystem is babbling. You have to, you know, explicitly send a request for data and you can do, I mean, you can do that on canvas too. There's like,

**Charles Aylward:** Oh, sorry. Babbling. It would be like emitting packets without, without waiting to be told, or it's just, as soon as there's a opening, it, it, it just starts sending.

**Charles Aylward:** Yeah. Sorry. That's a, that's a, that actually is a, a term like in the literature is like having a babbling node, but yeah, it just means that you have a, a system that is, emitting data without being asked for the data. Got it.

**Charles Aylward:** Okay. Yeah. Cause I, in, when I was working in power systems, it was very much like there was like a master controller and it just said, it did not, it did not allow you to say, I think you could maybe on the bus, you could say like, I have data, but that was it. You couldn't like start sending it. It would be like, you're kind of like raising your hand and then, and then the teacher's calling on you and saying, all right, what's your data? Like that sort of thing.

**Charles Aylward:** Exactly. Yeah. You know, there's a, depending on the system you're building, it's not necessarily obvious that like one of these things is better than the other. Right? Like, obviously like, I think, you know, most, a lot of automotive systems sort of use like a common sort of canvas method of these things are just streaming and the priority of the message deals with collisions. And, and it sort of works itself out. But in the case where you want sort of nearly absolute determinism of the system. So like, if you power the system on and you send it the launch, the vehicle command, you want everything to be as deterministic as possible, including like, you know, just even the ordering of packets on the network. And that might be, I think that's a little unique in terms of approaches to distributed embedded systems. Like that's kind of, yeah, there are a lot of systems where you don't necessarily need to care that deeply about just how deterministic everything is. Right.

**Charles Aylward:** Yeah. I mean, I guess if you were getting in your car and just driving down the block and it had to be the exact same each time, then maybe you would be able to do that. Right. Cause you'd be like, okay, I know what's going to interface here. I know all the things that must go the exact way that we expect it to. Because it's so dangerous to drive it up the block. That's kind of what it comes down to. Right.

**Charles Aylward:** Exactly. And then it depends a little bit on the makeup of the sensor data you're talking about. Like there might be a lot of sensors, like say on a, any system like a car or something where these things are interesting, but they're not mission critical to driving the car. Right. Right. And something like a launch vehicle, you don't really have a lot of extra nice to have sensors necessarily. They might all be sort of critically important sensor data.

**Charles Aylward:** I'm just imagining someone, someone in the control room being like with like a, with like a simulated steering wheel and gas pedal and be like,

**Chris Gammell:** all right, guys, I'm going to floor it. I'm really excited. I really, I really want to see what this, this system can do. I'm going to floor it. It's like, no, it's, it's already floored. Right.

**Charles Aylward:** Right. So, I mean, like a car system is not going to be designed this way, but like, for example, right. you want your accelerator data to always override like some temperature sensor, right. Or your brake, your brake pedal position is always overriding whatever, some temperature sensor. And something like a launch vehicle, the likelihood of you having those two radically different priorities is maybe, you know, smaller. Right. So like your temperature data might be critically important, right. Your pressure data is definitely critically important. If you're talking about like a rocket engine, like chamber pressure or something. Right. So it might not, you might end up with a system where it doesn't make sense that this has a lower priority, right. You have to get all of the data. And so you're kind of in this situation where you may not be able to use like a sort of standard canvas priority way of dealing with your sensor streams. So it might make sense that you just use this sort of request response mechanism for everything where you have some source of control or some controller, whatever your main computer that's requesting all of the data all the time because you need all of it. And you need to have it with a real time constraint for every, like whatever GNC cycle it might be or whatever it is.

**Charles Aylward:** Yeah. That's really interesting. So I guess one thing that's kind of missing for me here. So like, these are really good general, like design. I think like you're saying, these, these are all kinds of constraints and how you're working the constraints within the system that you're building and stuff like that. But for all of this, where, where do you start? Because I mean, I, you were talking about constraints and that makes sense for, you know, this is a differently constrained system, but I, aside from just the, what sensors might need to be in there and all the things that are needed, like, how do you push back in a design meeting and be like, well, no, you can't have 15,000 valves or you can't, you know, like how do you then start to actually interact with a, a team that wants more and more sensing because of all these things? I mean, is there like a general knowledge around what is needed in a rocket? I guess I'm so clueless in this space that I don't know where to, you know, like you start with a blank sheet of paper, but I'm guessing you don't actually start with a blank sheet of paper.

**Charles Aylward:** Well, at Astro, we did, but, uh, you did. Oh,

**Charles Aylward:** okay. That's, so that's really interesting. Yeah. So you start with a blank sheet of paper and then they say, well, a rocket's going to have blank number of valves for the fuel system. Right. That's someone said that.

**Charles Aylward:** Yeah. Well, so, so there is sort of like, uh, I mean, all engineers want more data all the time. Right. So, yeah,

**Charles Aylward:** exactly. Right. Right. So, so, so then what are the constraining elements? Is it just, is it cost? Is it time? Is it complexity? Is it weight? I mean, that's one thing I know about rockets is weight. Weight matters. So like, how, how do you say, no, that's too many, eight, fine. Nine. No, that's too many. You know, I don't know where this comes in. You know, I don't know how I would start that conversation.

**Charles Aylward:** Right. So if you're, if you're going, if you're going back to basic principles and those things can kind of flow into like the system that you want to design from electronics and software perspective. So, okay. Okay. Based on this behavior that we would like from the system, we're going to use ethernet and we're going to use this processor. And, you know, of course, like basic stuff like cost and availability are going to go into like which processor you're selecting and ethernet switches and that sort of thing.

**Charles Aylward:** Never going to be a problem with availability. I mean, yeah. Right. Right.

**Charles Aylward:** No, definitely. Definitely not. Yeah. So if you're designing like the embedded electronics, right, you'll, you'll have some baseline for like, well, I have this much compute power and I have this much network bandwidth. And you do need to like sort of push that. How do I want to say this? The discussion with like the, like the example, like a, a rocket company with the propulsion engineers and all the stuff they want. Right. You can get that information early, but you can't really say yes or no until you've kind of figured out the design space for your own systems a little bit. Right. So you have to, based on some very probably broad requirements at first, you know, you figure out, okay, well, we're going to use one of these three processors and we're going to use ethernet. We're going to use one of these three, you know, ethernet switches or whatever it is. You do need to do a little bit of, you kind of need to create like a, depending on where you're from, this might be called like a walking skeleton or a vertical slice. Right. So it's a, what that means is basically instead of developing one subsystem or implementing one subsystem and like finishing it and then moving on or doing 100% of the design for some system and then implementing it fully and then moving on like kind of like a waterfall approach. Yeah. You do like a walking skeleton, which is just like each, you know, I have a understanding of what this topology is going to look like. There's going to be like this one guidance computer and then a couple of different like controllers that are connected to that, that make things happen on the, on the launch vehicle. So, you know, what is the, the most basic thing I can get implemented on all of those systems that will show sort of like what this, how this system is going to behave and like get some idea of how much extra compute or how much, like how many cycles basically you have to play with on the processor, you know, how much bandwidth does it actually take to send one sensor, you know, data and it could just be a fake sensor, hard coded thing. Right. So you have to have some idea there. Right. And you can't, you can do these things on paper, right? Like you can just look like, Oh, you know, the basic ethernet packet is 1500 bytes and there's this much preamble and then blah, blah, blah. And then, you know, there's these couple other fields in the ethernet packet. And then maybe you have a TCP header or UDP header. And that takes up this much space. And then I have this many bytes left over. You know, I can figure out, Oh, if I'm sending like a 32 bit, a bunch of 32 bit numbers or 64 bit numbers, I know how many sensors I can fit in there. And you can just do that on paper and then figure out what your, basically your link budget is. And then you can come back to your propulsion team or whoever it is. And it's me like, you know, I know you want 200 temperature sensors on here, but that's just not going to happen.

**Charles Aylward:** Also purchasing would like to talk to you. Exactly. So I guess even, even at the level of like knowing that you're going to have ethernet on there, like that also is a, is a system design that has impacts as well. Right.

**Charles Aylward:** Exactly. Right. It kind of comes down to sort of kind of hitting the books. In terms of like how these things work at a low level. Right. So from a desktop user perspective, you get like an ethernet switch and you just plug things into it and you kind of don't care how those packets are flowing around. Right. But if you care about sort of like variant, like your jitter and latency or just wanting to know what they are and what they will be,

**Charles Aylward:** then you sort of collisions in a TCP system might be, might be problematic as well. Right.

**Charles Aylward:** Right. Yeah. I mean like a modern, a modern ethernet switch does a lot of really smart stuff so that chances are you're not going to have a collision or, you know, dropped. I mean, it's a switch. So basically all those different ports coming in, have their own cues. And then internal logic is like, you know, depopulating those cues and sending the packets to the right place, that sort of thing. Mm-hmm. Yep. But even just knowing that is important to, to know like, well, how did these things find each other? Like if you're really looking at bytes on the communication channel, right. From a desktop perspective, there's actually a lot of stuff on your communication channel that, you know, you don't see or it's not related to the webpage you're viewing or whatever it is. There's like a, there's all these like lower level protocols to figure out like, well, which port on the switch is this thing actually connected to? So I send this packet coming in on the right port. Right. So kind of just, that's like maybe getting into the weeds there,

**Charles Aylward:** but you know, you want to know. This all the ties together. I think that that is what it really, to, to, to my ears, this is like each decision has cascading effects, right. Each one,

**Charles Aylward:** you know,

**Charles Aylward:** deciding to use ethernet. Okay. Well now each board has to have ethernet and like, Oh, maybe each one has, maybe it's running embedded Linux or maybe it's running bare metal or maybe it's running in our toss. And like, just like each of those then also has their own effects and on, on, down the line to the eventually at some point you have to tell propulsion engineer. Yeah. No, no, we can't, we can't do that. Sorry. And I think one, one thing it sounds like you're good at is doing that quickly. That sounds like it would be probably, you know, you said you only had six months, so probably pretty important to figure that out pretty fast.

**Charles Aylward:** Yeah. Yeah. One of the things there is we use, you know, like I think generally speaking, we just use the term requirement pretty loosely, right? Like everything, some team, like if you have team boundaries, right? Like some team has a set of requirements that they give you for like, basically what they want from the system, but you kind of really need to be really kind of ruthless in terms of what is a requirement versus, you know, there's a, there's other terms for what's, what's, what's the next in line behind requirement. Like sometimes people I've heard desirement.

**Charles Aylward:** Oh, I haven't heard that one before. That's a good one.

**Charles Aylward:** Yeah. Like you have requirements and desirement. Nice to have. I've heard before. Yeah. But actually there was a propulsion engineer at Astra who had a really good way of putting this. I don't know if I, he'd be comfortable giving his name, but I actually named this after him. I don't know if he even knows it. Oh,

**Charles Aylward:** okay. Got it.

**Charles Aylward:** It's called Judd. I call it Juddson's razor.

**Charles Aylward:** Oh, nice. Instead of, instead of Mr. Occam, it's Mr. Judd's.

**Charles Aylward:** Yeah. Juddson's razor. So what this razor is basically a requirement is something that will cause the schedule to slip indefinitely until it is met. If it doesn't meet that criteria, it's not a requirement. Right. So interesting. Anything else is like a desirement or an objective or, you know, a stretch goal.

**Charles Aylward:** Did you state that one more time? So it will cause the schedule to slip indefinitely until it's met. That is, that's a hard requirement. Is that, is that right?

**Charles Aylward:** Or just in general, like that's what a requirement means, right? Like that was his way of thinking about it. So if you're going to call something a requirement, that means.

**Charles Aylward:** That is the test for it. Yeah. Yeah.

**Charles Aylward:** That's the test for it being a requirement is that the schedule will just slip indefinitely until the requirement is met.

**Charles Aylward:** Right. Right. The main fuel valve has to open. Right. Right. Exactly. That is a hard requirement. Right.

**Charles Aylward:** Yeah. So going, so going back into that, like sort of back and forth with like, how do you design these things? There are going to be some requirements. Like these two valves have to open within 10 milliseconds of each other, which, you know, that might be a little short for fluidics, but whatever it is, right? Like these two things have to happen within 10 milliseconds or something. And you need to be able to do that. So that feeds into like your electronics and software design.

**Charles Aylward:** I mean, you've mentioned meeting timing a couple of times. Does this mean there was an RTOS on board?

**Charles Aylward:** Yes. Yeah.

**Charles Aylward:** Cause we had, we had an RTOS expert on here. So basically I, and all of our listeners are all RTOS experts now. Cause I know what that means.

**Charles Aylward:** Oh yeah. Excellent. Yeah.

**Charles Aylward:** It's interesting too, because like, so I work on Zephyr stuff for some of the networking layer stuff, but it is also an RTOS and I have no, I have no visibility into the actual real time aspect of it, but this is a very good example. It feels like of the need for that real time aspect. You need to meet timing. You need to make sure those two valves open them within 10 milliseconds of each other, or else you're at least going to send a packet. Like you said earlier in the show that, Hey, you missed timing four times in the last minute or whatever the, whatever it is.

**Charles Aylward:** Right. Yeah. So that kind of goes into before you start writing any code or designing anything, figure out what class of problems you have. Right. So in, in our example, you have distributed system problems and you have real time problems. And so, you know, part of that is, is sort of once you know that you have those problems, it's like, those are domains of study and you, you kind of need to suck it up and hit the books a little bit. Right. So what does it mean? Well, first of all, what does it even mean that something is real time? Right. So like the, the basic version of that is if you are relying on a result from something, whether that's reading a sensor or computation, that result has to be available within a certain amount of time, or there's a failure. Right. And then you can kind of, you know, take that a next step. Like, well, there are, there are classes of real time systems. What is, what is like the classes of real time constraints? What are those? Well, there's sort of, this list varies a little bit, but like generally there, you're going to have soft real time constraint, firm real time constraint, or hard real time constraint. So a soft real time constraint might be, if that result is late, then the system performance is degraded. A firm real time constraint would be, if a result is late, that result is no longer useful at all, but the system doesn't fail. And then a hard, you know, real time constraint would be, if that result is late, then the system fails. So once you know, you're dealing with a real time system, it pays to like, start by thumbing through some of the literature on these things, grab a book, et cetera, right? You know?

**Charles Aylward:** Well, I mean, people listening right now, they're, they're just saying, come on, Charles, tell us what is the literature? So what is, what is your go-to on this stuff?

**Charles Aylward:** Excuse me while I rotate around and look at my bookshelf.

**Charles Aylward:** He's a paper person. He needs to look at the paper. Understandable. Yeah.

**Charles Aylward:** So I think the two that kind of got me sort of pretty well bootstrapped are, um, two books that are both by, they're both, uh, published by Springer. One is by Giorgio Boutazzo and the other ones by Hermann Kopetz. One is, uh, the Kopetz one is real time systems. And, uh, the Boutazzo one is hard real time computing systems. And I think if you pick up the Kopetz book, like you will have a really solid foundation of what all this stuff means and how they work together. Like, or how, how does what all work together? Like how do, how do, uh, you know, you know,

**Charles Aylward:** the system pieces.

**Charles Aylward:** Sorry. Sorry. I skipped ahead there. Like, you know, what is, uh, you know, what does the scheduler do? How are the, you know, what are all the different ways a scheduler could work? Right. Got it.

**Charles Aylward:** So this is, this is within the processor itself, not like, not at a system level, but at like a board level almost.

**Charles Aylward:** Yeah. I mean, when we're, we're talking about dealing with tasks that have to do something in a, with a real time constraint, these books are like kind of talking about the general principles that go into, you know, designing like a real time operating system. And of course you probably don't want to bite off developing your own real time system.

**Charles Aylward:** Although people love doing that.

**Charles Aylward:** Although that's not, I mean, there's some people who think that's ludicrous. It's not necessarily as out there as you, as it might seem, but you want to know.

**Charles Aylward:** It does for me, but for some people, I'm sure it's very within grasp. Yeah. It seems like it would be for you.

**Charles Aylward:** You, you, yeah, you, you want to know like how those things work. And even if you choose a specific real time operating system, there are probably different tuning parameters or even schedulers and things that you can choose from.

**Charles Aylward:** Yeah.

**Charles Aylward:** So you might have like a, in terms of getting your tasks done, you know, it might be highest priority first, right? So if you have two tasks that try to activate at the same time, the higher priority one wins, or you could, you know, there, there's tons of different ways these things work, but, you know, it might be earliest deadline first. So whichever task fires up that has the earliest deadline that gets run first, regardless of, right. Some concept of priority and that sort of thing.

**Charles Aylward:** Yeah. Cause I guess you don't, you don't know the length of time it's going to take to do any one task. So that's probably the best guess you could probably do is just like, well, unless you have like a running list of like, well, this task almost always takes 300 milliseconds. So we need to make sure we allot that. And that's what schedulers are for. Right. Yeah.

**Charles Aylward:** Well, that, that feed that kind of ties back to sort of the, those guiding principles that are sort of around, like having a really well, you know, testable system and a knowable system and sort of like test data is first class data. Right. So the first time you run this through, you can get, you know, if you, if you have like these synthetic software sensors coming in your telemetry stream, you can just run it once and, and, and no, like, absolutely. Like, Oh, to send this one command to this actuator, two systems down. I know that it took so many milliseconds on the network to get there. Then it took so many more milliseconds for that system to parse the command, execute the command and respond. Right. Like you, you can get all that instrumentation and then just know how long these things take and then feed that into your sort of analysis of, okay, well, I know this takes 300 milliseconds to run. And I know this has to run within 350 milliseconds or whatever it is, you know, like, and these other things kind of stack up. How do I structure the schedule such that all these things actually occur?

**Charles Aylward:** Yeah. Thread, thread the needle as it were. Yeah. It's interesting. I mean, so when you say, so you have a real time operating system, you have this device that's maybe. So we've already learned that there's a ethernet going to a. End point of some sort. Is that kind of the final stop or other than sub subsystems? So like a, I'm just going to, I have literally no knowledge of what these boards are just to make sure that we're not, you know, giving away any secrets here. But like, if I'm just imagining like some, like LPC 5,500 part or something like that, you know, something like, you know, relatively beefy microcontroller running an RTOS. And then I had said earlier, like, well, it's not really a, there's not like a system view, but it's just a microcontroller view. But then I was thinking, well, maybe you could though, because you could have additional microcontrollers down the line that are maybe on the other side of a spy bus or an I squared C where you actually control sub microcontrollers as well that are just sitting on an actuator, just measuring position and just feeding it back to the real time operating system. Like what is the depth? Like, is it the real time operating system? Is that final stop in the, in the system design or are there sub stops past the real time operating system as well?

**Charles Aylward:** So yeah, a real time system, like adding a, sorry, a real time operating system. I don't want to say this like a, a lot of stuff comes with a real time operating system that seems sort of like, Oh, this is just obviously good. I have these events, like generally speaking, I have, you know, some event driven system and button pushes, you know, have a certain priority and updating the screen as a certain priority, et cetera. And I just want to make sure that the screen always updates. And I, you know, don't care necessarily when the button push is registered because on a human timescale, that doesn't matter. Right. Right.

**Charles Aylward:** Right. 30 milliseconds or 200 milliseconds. Yeah. Who cares?

**Charles Aylward:** Yeah. So the threshold, the threshold for using a real time operating system is a little different, right? Like depending on what kind of system you're dealing with, it doesn't come like, it doesn't come for free. Right. So there is sort of like, you know, some complexity with structuring or code for a real time operating system and knowing how the real time operating system is going to execute that code. Going back to the like kind of guiding principles, right? You're trying to keep the state space as much as you can into something that's like kind of knowable by the best case scenario, one human, but at least like the team, right. Can like know what's going on. And so if you kind of approach it from that perspective, then the threshold for adding like something like a real time operating system might go, might be much higher. Right. So, and, and the, the number of like legs in, like you were talking about, like the number of legs, like how far away you are from the center, the main computer and like the brain and the thing, the brain and the, and like the fingertip, right. Like how many different things are in that path. Yeah.

**Charles Aylward:** That's a good way to visualize it. Yep.

**Charles Aylward:** Yeah. So same, same thing, right. You want to limit the, the amount of stuff that happens between right. The, the brain and that. Yeah.

**Charles Aylward:** The brain says wiggle finger. How many hops does it take to get down to finger? Right. It's just.

**Charles Aylward:** Right. Yeah.

**Charles Aylward:** So,

**Charles Aylward:** so,

**Charles Aylward:** right. So, so I specifically in a, in a rocket, I guess, or maybe a small, let's just say this, this rocket, how, how many steps is it to get to the finger waggle?

**Charles Aylward:** Right. Yeah. So, I mean, that's not talking about like any specific rocket, but generally you want to just limit that to like one major, like network. Okay. Yeah. That's great.

**Charles Aylward:** Okay. Yeah. That's what I was wondering. Yeah. So then you're saying, so I'm just going to extrapolate. So you're not saying anything that you shouldn't be saying, but like, I'm just imagining an actuator in like the, the real time. So this LPC, whatever microcontroller running a real time operating system is directly reading and writing to an actuator instead of writing to a, over a bus to a sub microcontroller that is then updating that actuator. Is that a fair statement?

**Charles Aylward:** That is a fair statement. Yeah. So like the performance of like, say a spy bus, like between your microcontroller and an ADC or something like that is a really, it's pretty easy to understand what that's going to look like from just looking at the data sheet, right? Like, Oh, I can run the spy bus at the speed. And basically I just know that I can get all of the data off that spy bus. You can kind of, at some level, you can assume that's basically like a local interaction and you're not like, it's not like a net. I mean, even though sure it's a communication bus, you don't have to factor that in exactly in the same way as like your primary communication bus. Right. So you can kind of just think of like this subsystem, which is a microcontroller and ADC and like, I don't know, a bunch of like high side switches and stuff like that.

**Charles Aylward:** Yeah.

**Charles Aylward:** Right. You can just think of that as like the, a single like sort of domain of control.

**Charles Aylward:** Yeah. Yeah. That is a subsystem, right? That makes a lot of sense to me. What this really tells me though, is that when the complexity goes up, so it's now the propulsion engineer comes back to you and says, Charles, you know, I don't need eight actuators. I need 16. It's not like if you run out of IO or drivers or whatever is on these, these control boards on the RTOS based control board, it's not like, well, we're going to try and move this down the line and put sub processors off this real-time operating system. It's no, no, no. We just duplicate that board and we say, all right, now there's just a second. There's just a second node on the network that has a similar functionality. And that actually then from a standardization perspective, that makes a ton of sense to me from a, you know, unique devices on an ethernet network. That makes a lot of sense too, because then they're very easily addressable. So like, yeah.

**Charles Aylward:** Yeah. I mean, you're changing the problem from like you add another spoke to a hub and spoke. That's right. Yeah. Versus like, if you have a tree, you have to like potentially rebalance this tree. Because of bandwidth constraints. And it also just makes it harder to visualize like what's going on.

**Charles Aylward:** Yeah. Yeah. So then how do you then handle when you have, so assuming you have standardized hardware where there's the hub and spoke and you're adding, you go from two spokes to five spokes or something like that. But each of those spokes, each of those real-time operating systems might have a completely different function, even if it's a similar hardware. How do you then maintain all the, all of the updates that need to happen from the computer going down to each RTOS based system?

**Charles Aylward:** Right. So some of that, well, first I would say is maybe those sort of nodes on the, on the periphery, the actual end effectors, the end nodes doesn't necessarily need to run a real-time operating system. Oh, okay.

**Charles Aylward:** But then there's more complexity, I would imagine as well as, because then if you have a real-time operating system based version and a non-real-time operating based version, you're saying they're all on the ethernet network, but they're.

**Charles Aylward:** Oh yeah. I certainly, I wouldn't recommend necessarily mixing and matching these things.

**Charles Aylward:** Yeah. Yeah. Yeah.

**Charles Aylward:** But if you have like a situation where the end nodes don't make decisions for themselves necessarily, like high level, like system behavior decisions, they might have like a little small, like they might be running head loops or something like that, you know, PID controllers or something, but they're not making large system decisions. They're only sort of waiting for a request on the network and then responding. That might be a interaction that you don't need to necessarily have a real-time operating system.

**Charles Aylward:** Oh, that's great. Okay.

**Charles Aylward:** In that case, you know, it can make it quite a bit more knowable, right? You know, there's a lot of different stuff you can do between just having a state machine and a real-time operating system, right?

**Charles Aylward:** Yeah. Yeah. Yes. Yeah.

**Charles Aylward:** So you, you can, you can kind of almost fake, not fake, but like there's some, some sort of basic, like real-time operating system, like behavior that you can get without having to run, like a task switching system. Right. Like a simple version might just be like, you have a, you have a standard super loop. And when events come in, you're setting flags. And then you just check those flags in the priority order that you want to get them done. Right. Yeah. You respond to them or you add them to a queue and then you just respond to them.

**Charles Aylward:** And then it's just, you're saying because your system has so much overhead in that scenario that you're not even worrying about timing. It's just like a, not a guaranteed, but it's a, you're, you're not as worried about timing and deterministic type stuff then.

**Charles Aylward:** Yeah. Well, I mean, and you're so close because you don't have the operating system in the way it's actually in some ways a little bit more noble and a little bit more real time. Right. Or, or not real more, not more real time, but the latency is going to be smaller because you don't, you don't have this operating system. It's zippier. It's zippier. Yeah. You don't, you know, like switching out the context for one task and storing that while you load up the new context and like switch this, you know, switch over to a different stack and start executing. Something.

**Charles Aylward:** Mm-hmm. Okay. Well, did the rocket go up? Yeah. What, so what, what was the timeline of this? Like when were you, when are you there and when did it go up?

**Charles Aylward:** Oh, I see. Yeah. I joined in the middle of 2017 and the first vehicle launch was 364 days. After I joined.

**Charles Aylward:** Really? That's a nice, that's a nice stat to have. Yeah.

**Charles Aylward:** So it was like one day short of Todd and I's one, uh, one year anniversary.

**Charles Aylward:** You should tell people that the deadline was the one year. And they said we had to get it out in one year.

**Charles Aylward:** I mean, yeah, actually originally, like I said, when I originally joined, it was, the idea was six months, but that's, was just not feasible for. Yeah. The size of team we had at the time.

**Charles Aylward:** So you're saying complete blank sheet of paper on day one, no electronics design, maybe some rocket part design. I don't, I don't know how, I don't know how propulsion engineers work.

**Charles Aylward:** Well, no, from my, so the one year is from my perspective. So coming in with the understanding that I was writing from scratch, the flight control software, that was a year.

**Charles Aylward:** Ah, I see. Okay.

**Charles Aylward:** There was already heritage in terms of the actual rocket engines. And there was actually already some heritage in terms of the electronics.

**Charles Aylward:** Got it. Okay. So like, so some rework maybe, or just, but yeah. Okay. So blank page for you. I get it.

**Charles Aylward:** Yeah.

**Charles Aylward:** Cool. That's, I mean, that's, that's impressive either way. Don't, don't get me wrong. And so like, so what is the scale of how much can this thing take up in terms of like, how many small sats can it carry or weight, I guess?

**Charles Aylward:** So, well, it depends on, yeah, it depends. So there's like, you know, you've heard of the term cube sat potentially. Yeah. That is actually a form factor. So a cube sat is basically a 10 by 10 by 10 centimeter unit. A cube sat might just be that one unit, or you might have a three by one or there's different configurations of these things.

**Charles Aylward:** Yeah. 30 by 10 by 10. Yeah. Well, I think, I think the planet one was 30 by 10 by 10, wasn't it?

**Charles Aylward:** Yeah. I think that's a three by a three by a three by one. Yeah. Or 30 by 10. Yeah. Sorry. So there's, there's some amount of volume constraint, but because cube sats are pretty small, it's, uh, any launched orbit, you're really talking about mass is the thing you care about.

**Chris Gammell:** Got it.

**Charles Aylward:** So I think generally the small launch services are looking at hundreds of kilograms to orbit.

**Charles Aylward:** Mm-hmm.

**Charles Aylward:** The big guys are launching many, many, many tons.

**Charles Aylward:** The space X's of the world and such. Yeah.

**Charles Aylward:** Yeah.

**Charles Aylward:** Yeah. Oh yeah. I guess I could, I could have gone to the Astro homepage, 500 kilograms to 500 kilometers. It says up to 500 kilograms to 500 kilometers.

**Charles Aylward:** Yeah.

**Charles Aylward:** Okay. Yeah.

**Charles Aylward:** Yeah. So the, those orbits I think are generally like, like the small launcher or do space kind of folks are in the 400 to 600 kilometer orbit range generally.

**Charles Aylward:** Yeah. I don't, I don't really get the difference. I know that the James Webb space telescope is at the L2. I think it's at an L point. I know that a Lagrange point. Is that right?

**Charles Aylward:** Yeah. It's a, it's a, it's orbiting, orbiting a Lagrange point.

**Charles Aylward:** Oh, that's right. That's not, it's not at the Lagrange point. Yes. That's.

**Charles Aylward:** Yeah. It's not at, at the, it's nearby though.

**Charles Aylward:** I know that. And it's very far away compared to, it's like past the way past the moon, right? Cause the moon is shading it or the earth shading the sun or something like that.

**Charles Aylward:** Yeah. So it is, yeah, it's, it's, it's quite a ways out. I don't know exactly how far that one is out. The idea is to basically keep it oriented away from the sun and more or less in the shade. Yeah.

**Charles Aylward:** Okay. So we're already pretty deep on, on time wise here, but I, I would like to know, you know, because we talked about rigor and how does this then, so coming out of this experience and going back in the consulting world, do you have to turn down contracts? Because they're like, you know, we just need something really quick. And you'd be like, well, you know, like, do you get asked for fast and dirty engineering? And you're like, eh, it doesn't, that's not my thing. Or like, what, what is, what is your area of focus now that you're back in the consulting world?

**Charles Aylward:** Yeah. Now that I'm consulting, I do get a few like new space contracts. So like, I don't really have to dial that down exactly in terms of like commercial projects that I work on. I think I still, I think that's kind of like one of the values I add is kind of bringing some of that over in terms of, I get a lot of like startups, right? So in,

**Charles Aylward:** in the Bay area, this is, this is shocking.

**Charles Aylward:** So they're, they're introducing some new, new product and they maybe have not done that before, or they don't, they don't really know how far away their prototype is from like being able to go into manufacturing. And so those skills sort of transfer over in terms of, you know, like actually doing design reviews for them and also kind of factors, flows into general process processes that they, might be using for their, you know, development life cycles. Like a lot of this stuff gets a lot of this like rigor, you know, gets kind of a bad rap because of like this focus on agile methodologies, especially here in Silicon Valley. Like it's just like this constant word that's flowing around agile, agile, et cetera. And the worst thing you could ever do is like waterfall, et cetera. I think even waterfall, but in general, like this sort of like more rigorous approaches actually make you go faster.

**Charles Aylward:** Yeah. It's slower at the beginning. Right. I think, I think then it, that's the thing. There's a crossover at some point because you like, okay, you're great. I think about this one, like Philip Johnston was on the show too. And it's like, Philip talks about like, Oh, getting set up at like, yeah, it's just, it sucks at the beginning, but once you're there, then you're so fast because your build system just tests everything for you. Or like you're talking about, like all of your systems test every time they start up or they, you know, all of your data is just there. It's not like you have to go and do things manually each time. I don't know. There's, there's a lot of ways to do it,

**Charles Aylward:** but exactly. So it's, yeah, like we're going back to that example of the you know, your test data is first class data. Like the first time you encounter a bug, it's super tempting to just write, throw, you know, your UART to USB adapter on there and print out some stuff on your UART or hook up JTAG or whatever it is. Like that's certainly easier than like, okay, I'm going to revise the software so that I can actually get that stuff that I'm looking at. Let's,

**Charles Aylward:** let's change our communication standard so that we can have better visibility into what went wrong. It's like, Oh yeah. Okay.

**Charles Aylward:** Exactly. Like that. There's more friction. There's more friction there, but in the long run, I think like those kinds of trade-offs just like really pay off.

**Charles Aylward:** Yeah. I think that's, I think it would be a harder pitch. First off, I think people coming to you probably already know this based on your reputation. So that's good. And hopefully this, this show will help to continue to enhance that. But like, but like, I can imagine that would be a hard pill to swallow when people are like, well, I want to go fast though. All right. Well, no.

**Charles Aylward:** Right. Yeah. I mean, I see, I see this, I see this a lot in the electronics design for like the first, the first like revision of a board. Like, so someone, someone, someone's going from, I have a couple of proto, like a couple raspberry pies or like, you know, Arduino's hooked up that first transition to like, okay, we're going to design a custom board and we want to be able to manufacture this thing. There's, I see this a lot where the pressure is so high to get that out quickly that like these boards just have like no testability, right? Like there's no test points on the things, right? Like all of that. And there's no way to like, basically like if the system doesn't just boot up and work flawlessly the first time, like you have no idea why. Yeah. Right. Yeah. So, yeah, it takes a lot more time to like, think about like which test points you need to bring out and, and you're finding out a BGA and that's a pain. And, you know, it would be a lot quicker if I just didn't fan out this other communication channel for testing and debugging or whatever. And it, it, it always comes back to make these things actually take longer than they would have if they just slow down and paid someone to do a design review, get a third party design review, or, or if you have a, you know, if you have enough people on your team, make, design review a thing and sit down and do the process of like, okay, well once this comes in and it doesn't work, how do we test it? Right. Right.

**Charles Aylward:** Yeah. Having a test plan is pretty important. Right. Yeah. Yeah. It's interesting too, because I, the thing that I've learned in my consulting career is that there are no guardrails. Right. One of the things that like companies give you is someone there who is like, yeah, we've done it this way and yeah, there's, it sucks maybe, but there's guardrails because that's just how we do things. And, and like, you know, I bemoan that that's maybe slower, older process when I was, when I was there, but I didn't realize that then nobody was going to be asking me for that. Like when someone is just like, Chris, I need you to design a thing for me. It's up to me. Like that's on me. Everything that works, everything that doesn't. Right. Yeah. That's, that's all me. And if I then have to say, well, yeah, sorry, I didn't hook up the ground plane or something like that or whatever other stupid thing maybe I, I've done, you know, like it's just that it's all on me. Every check is on me and every, yeah. So.

**Charles Aylward:** Yeah.

**Charles Aylward:** That's why it's, I like the rigor part. That's, that's where the rigor really is important. I think, you know, it allows you to deliver a really good product as a consultant, I think.

**Charles Aylward:** Yeah, I agree. So, right. Like kind of, it's like no process is definitely not the way to go. Like that is not make it faster. You have to have some process. Like there's some terms for this, like the right amount of paper, the right amount of paperwork, right? Like you need to have some, some process in place for like, okay, I finished doing the schematic. What happens next? Oh, I just do layout. And then I send it to the PCB house. No, like there has to be a couple other steps in there. Like check the schematic, you know, like whatever, come up with a checklist of things that you always test for these. You always check your schematic against, then move on to the layout. Right. And then have a checklist or something for things that you always check on a PCB, right? Like,

**Charles Aylward:** yeah. I'm just stuck. I'm just, I'm sitting here thinking about talking to my 20 year old self and be like, Chris, one day in your late thirties, you're going to be on a podcast, nodding along vigorously to the right amount of paperwork. Totally. Right. Yeah. But like, I do, like I, I am nodding, I am nodding vigorously. Like, yes, of course there is. Yeah. It's just, you know, what was the other one? I think it was, Oh, the other day, this is a really stupid example, but it is born from years of experience. I was replugging in my can. I was just changing out some plugs on my camera. Like I was just redoing my camera. And for some reason I like kind of like snapped to, and I realized I was moving all the glasses of like, you know, like the, the last dregs of coffee in coffee mugs and like cans of bubbly water and water bottles. I moved all those to another bench. I had completely cleared them off the bench. And I'm like, this was such a good move. And I'm like, how did I learn this? I'm like, I've learned this because I've spilled coffee on every single schematic I've ever had on my bench ever before. And like, you know, and like, but like that slow, slight movement at the beginning saved all the paper on my, on my desk, you know, like all the stuff on my desk really, you know, it's just, yeah. Very, very stupid version of all the very smart things you're saying here. Yeah. Well,

**Charles Aylward:** well, thank you for saying so, but yeah, like, you know, the, the, it's like a one, and when you encounter those things, you know, I don't want to like go off on like a checklist thing, but like, yeah, put it on the checklist.

**Chris Gammell:** Yeah. That's good. Yeah.

**Charles Aylward:** I still refer to Andrew Zonenberg. So he's got one on GitHub that I will link in here.

**Charles Aylward:** Oh, okay. Great. Yeah.

**Charles Aylward:** Do you have one published somewhere?

**Charles Aylward:** I used to, I probably need to brush it up. Yeah. Maybe. Yeah.

**Charles Aylward:** I could find the hard part about a checklist is there's nothing that forces you to check the checklist. Yeah.

**Charles Aylward:** That's true. Yeah.

**Charles Aylward:** That first step of like, Oh, I have to, someone has to make me go through the checklist. There's, there's, that's all on me. You know, if I skip the checklist, it doesn't matter.

**Charles Aylward:** Like, can I actually fasten this board to something? Does it have fastening holes? Yeah. That's a good one. Yep. Clear, like connector clearance is another one, right? Like,

**Charles Aylward:** Oh yeah.

**Charles Aylward:** Or like, uh, not, I mean, there's hundreds of these things, of course, but like, of course the one that, the one that I screwed up a lot before I put it on the checklist was like failing to, in my footprints to like draw the mating half of the connectors, you know, size, like the footprint, like the keep out for the mating half. Yeah. I'd have this connector that I couldn't connect the cable to because the right connector doesn't fit between the other. Thanks.

**Charles Aylward:** That's a good one.

**Charles Aylward:** Oh, and just one other thing on the, on the testing too. I think a lot of people fail to account for what happens if the test fails, like if the test fails or this test campaign fails, you know, how does that affect the schedule, et cetera? There's a lot of, Oh, well, obviously we're going to test, but then there's not a lot of thinking about, well, what happens if that test actually fails? Right. Like,

**Charles Aylward:** uh, these little tests are big tests. Like, uh,

**Charles Aylward:** like, uh, let's say design level tests, right? So you get your first board in and you schedule in testing because, okay, we have this much time to design the board. We want it out by the end of this quarter, et cetera, et cetera. We have to fit testing in there, et cetera, et cetera. But then there's usually this missing step of, okay, well, we did the testing, but what happens if that board, what if the board doesn't work? Right. Yeah.

**Charles Aylward:** Yeah. Got it. Got it. Got a, got a budget for that second rev. Nobody, nobody likes to tell the client that one. That's why doesn't it work on the first rev? Because reasons, man, just because reasons.

**Charles Aylward:** Yeah. And I mean, yeah, you can make a lot of jokes about it in one way or the other, but the thing I find is you are pretty much not going to go from your Arduinos that are like, you know, breadboarded together to like your first rev. Right. Yeah. Yeah. Even if you get the circuit, right. The, you know, the box that it fits into, et cetera, like it's, it's going to change.

**Charles Aylward:** Yeah, totally. I mean, is, so this rigor checklist, all this stuff. I mean, it sounds like I always hate, like talking to younger engineers. Cause they're like, well, what do I go read? You know, I asked you about books and stuff like that too, but the rigor and the checks and the checklists and things like that. Is there, are there resources out there for that sort of thing? Or is it just school of hard knocks?

**Charles Aylward:** Hmm. I mean, some things you certainly learn the hard way. Yep. I don't know if there's necessarily, I mean, there's definitely like a domain of expertise, which is like testing industrial systems and testing, you know, safety systems and things like that. But in terms of electronics design and software design, I mean, I think it kind of comes down to the part that's hard is figuring out, is this problem? I'm having a domain of expertise. Like, is this actually like, does this problem I have, does it have a name? Is there like a bunch of people that actually study this class of problem? I see. Got it. And like figuring out what those things are and, and, you know, reading through, finding some good books on, on, on the subject. Like that can definitely, that can definitely save you a lot of headache. Like just knowing, like what, knowing what the problems actually are, like, sorry, we were talking about distributed systems. Like what actually are all of the problems with the distributed system? What are all the problems with like a real time system? Like, even if you're not like, you know, studying all the white papers that ever come out and like publishing, like at least knowing what all of the problems that exists are, right. That'll, I think help, help guide your, help guide your thinking.

**Charles Aylward:** It's like a schadenfreude for other people's problems, right? You know, like, you're like going and reading case studies and being like, oh yeah, that sucks. I don't want to do that. You're still going to, you're still going to probably mess it up at some point. Like, that's how I do it. I'm like, oh yeah, I would never do that. And then I go and do it the next week or something like that. You know, I'm just, imagine myself reading a case study of someone spilling coffee all over their schematics over and over again.

**Charles Aylward:** Yeah. Maybe, maybe that, maybe that ties in with like the right amount of paperwork. It's like the right, finding the right amount of studying, right? Like, yeah, you could take the total agile approach of like, I don't even know what my system's going to look like. I'm just going to start writing code and then bounce off the edges until I get there. You can certainly do that, but you know, chances are that actually will be a, you'll learn a lot, but it'll be a painful. And in my experience, actually slower process than finding a couple of good papers and books to read on the subject first.

**Charles Aylward:** Yeah. Yeah. Like well-designed systems have patterns and usually for a reason, usually either historical or, you know, like theoretical and like, yeah, yeah. Maybe like start there instead of just being like, well, let's start with a single processor and see when it fails and then go to two processors or whatever, whatever the equivalent would be. I don't, I don't even know, but yeah, I think it is, it is just in certain spaces where they're aside from just like finding a very, very similar thing and copying it, which valid enough, if it's not filing patents or whatever, if it's just copying a methodology, that's fine. Maybe it's a simple enough problem. But like, I think about like, if I was presented with a blank sheet of paper, like you were, I would, I would be very dismayed.

**Charles Aylward:** Yeah. So, right. Well, I mean, it can, it can be, it can certainly, I mean, it's certainly challenging, but it can be fun, right? Cause it's sort of,

**Charles Aylward:** yeah. I mean, you, you made a thing that you were on a team that made a thing that went to space. That's cool as hell. I mean, like that's, it did eventually go to space. Yeah. Yeah. That's, that's really cool. I have never done that. And like, we never will. So like that is, yeah.

**Charles Aylward:** Oh, never say never. I mean, you mentioned, I think you mentioned Sean from planet or he was at planet maybe when you interviewed him.

**Chris Gammell:** Yeah, that's right.

**Charles Aylward:** I mean, that's how I, I was doing sort of like industrial commercial electronics and software for just a little bit before. I think I heard Sean on a, on a podcast mentioned that he was working for this cool startup and they're in Alameda and I'm like, Oh, I'm close to Alameda. And at the end of the podcast, he's like, Hey, if you, you think you're interested, like hit me up. And I sent an email and that's how I ended up in new space. So, huh? Well, there you go. Never say never. Right.

**Charles Aylward:** Yeah.

**Charles Aylward:** Well, it's sort of like, um, you know, it's, you don't have to, uh, you don't have to have a degree in aerospace engineering for sure to get into new space, but you know, just take it seriously and take studying seriously.

**Charles Aylward:** And yeah,

**Charles Aylward:** it can happen.

**Charles Aylward:** Yeah. I'd say the stakes are higher than the stuff I'm normally doing, but, but not unobtainably higher apparently. So that's good.

**Charles Aylward:** Yeah. It's not like you can, yeah, it rigorous testing can, will certainly catch all of your like, lack of conceptual knowledge. Right. And correct. Yeah. Yeah. Help you correct for it. Like, Oh, there's this edge case. I didn't know about this edge case, but I caught it in testing.

**Charles Aylward:** But my test does.

**Charles Aylward:** That's great.

**Charles Aylward:** Uh, Charles, where can people find out more about you and, uh, how to hire you as a consultant and your background? Where do you hang out?

**Charles Aylward:** So, yeah, if you, if you want to hire me as a consultant or otherwise just talk to me about reviewing things or just talk to me, uh, uh, I have a small presence at, uh, grizzly peak.io. My sort of freelance name is grizzly peak systems. I'm available. Like, I think I'm on LinkedIn. You know, I check that every so often in terms of professional, you know, interactions. Uh, that's probably about it.

**Charles Aylward:** Great. Wow. I'll drop, I'll drop a hint. If people join the consulting forum as consultants, you also might get to cross paths with Charles too. So, Oh, sure. Yeah.

**Charles Aylward:** It's a, it's a great forum. It's a lot of really great people on that forum.

**Charles Aylward:** Yeah. There's a very long running thread about part shortages.

**Charles Aylward:** That might be, I don't, I don't know, but is that maybe the longest one at this point?

**Chris Gammell:** I think so. Yeah. It's been, it's been rough folks.

**Charles Aylward:** My kingdom for some FPGAs. Yeah.

**Charles Aylward:** Oh yeah. All right. Well, thanks Charles. I appreciate it. this has been really interesting and, I'm looking forward to talking to you again soon. Great.

**Charles Aylward:** Thanks for having me. Cheers. Cheers.

**Charles Aylward:** Cheers.
