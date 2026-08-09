---
episode: 663
title: Motors on PCBs with Carl Bugeja
url: https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/
---

**Carl Bugeja:** This is The Amp Hour Podcast. Released March 25th, 2024. Episode 663. Motors on PCBs with Carl Bugea.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. Hi, I'm Carl Bugea. I'm an engineer from Moala. Hey, Carl, how are you? Hi, Chris. It's good to chat with you. I have to imagine as you're sitting in your lab right now, when I imagine you in your lab, it's just like flexure circuits just going in the background, almost like cuckoo clocks. Everything's flapping and electronically actuated. Is that correct or not? Sometimes it is, yeah. Okay, all right.

**Dave Jones:** The sound really gets to my head, so.

**Chris Gammell:** Yeah.

**Dave Jones:** They're flapping.

**Chris Gammell:** I guess we would probably hear it. Those are not quiet machines that you build.

**Dave Jones:** Not all of them. Some are quiet. It depends on the speed that you run them with. But they can be quiet. But to test their durability, you have to test them at like 20 hertz. So if it's hitting something, it can get a little bit noisy.

**Chris Gammell:** Yeah. Right. Yeah. So it's already in the audible range. You start getting up into the 60 hertz and above, and you start to hear it pretty easily, huh? Have you created like, you know like how they do the hard drive musical things? Have you tried that, where you have like multiple flappy things, going at different frequencies, to try and like make a little orchestra? Sure.

**Dave Jones:** Yeah. That's a little, I haven't, I haven't done that yet, but I, I, Coming soon from Carl. Yeah. That would be interesting to test out.

**Chris Gammell:** Yeah. Well, that's great. So people should, I guess we should state up front. You have a wonderful YouTube channel, one of my favorite YouTube channels, where you do experiments, or like flex circuits, and electronics, and things like that. And I reached out to you, because you started selling some of your creations recently as well. And I wanted to talk about that, and just your history, and kind of everything you've built. How did you, how did you get started in this space? So,

**Dave Jones:** to start from the beginning, I graduated from university, as an electronics engineer. So it's kind of, my line of work. And all my life, I basically, like to tinker, with wood, with electronics, and building stuff. So it's kind of my hobby, and building robots. So that's, that's kind of my, it's sort of my work, but it's also my passion. And on my YouTube channel, I started experimenting with PCB motors, and PCB actuators. And almost, I think now it's been five years, doing this thing. And it's finally, progressed, into something that, can actually be turned into kits, or products. And, it's been a little bit busy.

**Chris Gammell:** Yeah, I bet. Yeah. And I mean, that is a big switchover too, where it's like, moving from experiments, to productization. It's like, yeah, that's, and I think this, one thing I thought about immediately, is just like the, you know, you document a lot of your, your trials, and tribulations, and failures, and I love that you do that. But I'm not sure that someone purchasing a kit, is going to be as, as forgiving. And be like, I bought this thing from Carl, and it doesn't work. And it's like, well, yeah, you know, you gotta try it out. You gotta try different things, you know.

**Dave Jones:** Yeah, I, we, we do a lot of testing before, because it's, from a prototype to a product, there's a huge difference. You need to, so, for example, for my flappers, I had to make sure that, they don't break after some time, and do all the testing related to that. I mean, it's easy just to make a YouTube video, and show, look, this thing work. And then, there, it's a whole different spectrum, than, selling something, I think.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Well, and so, what is the new company called? The new, where you're selling this stuff? my, our website was, I'm doing it with my cousin, it's called, the microbots.io. And, the aim is, so, we're sort of phase one, where we're, like, releasing, actuators, and, hopefully, soon, there will also be PCB motors. So, the first step is, like, getting, the actuators, and motors, to work reliably, and, good. And, hopefully, the, the stage two, is, integrating them, into robots, and displays. So, we're also working on some, cool interactive displays. I mean, some actuators, are already, like, like, the flipper. I mean, it's already, like, been, been through all, our testing, and, I, I mean, so far, I have no other ideas, on, how to improve it further. So, the next stage, for that is, integrating it, into products, which, we have multiple, projects, related, to that ongoing. That's great.

**Chris Gammell:** Yeah, no, I mean, people can go, to microbots.io, right now, and see, kind of the, I really like that you actually, have the coming soon too, where you've, you're teasing, the new stuff, because then it allows people, to kind of, see what, it's almost like a, quasi roadmap, but then also, like, maybe pre-order, and talk to you about, if they have other ideas, or, hopefully give you money, to help fund, you know, hardware's not cheap, so.

**Dave Jones:** Yeah, hardware's not cheap, no, but the main goal, for the coming soon, is just to show, a little bit of, what we're working on, and, if someone is interested, just, he can just put, his email address, and once, we launch that product, he will get notified, so.

**Chris Gammell:** Yeah. How much do you have to deal, with the, public, misunderstanding, of like, power delivery, in like, these motor type situations? Like, do people like, call you up, and say like, oh, awesome, I'm gonna like, lift my car up, with a, you know, a PCB actuated flap?

**Dave Jones:** So, every time I release a video, I receive a bunch of, DC emails. Oh, really? Yeah. It's either that, or either, companies, want to collaborate, or, of course, yeah. But, I mean, our goal is just, to, to work on, tiny, tiny motors, and actuators, and, I mean, it's, there are other companies, that for example, are working on PCB motors, and integrating, them into, cars, and stuff like that. But, my goal, for example, with the PCB motor, was always to make, like, an easier, to build, and that, a cheaper alternative, than the other motor, than, what's available, commercially, that has, the copper, the coil windings, and stuff like that. It's, it's easy, to drift, from the original goal, because I, I can go, and make a bigger motor, and have it, be, 5x more efficient, or, but, our goal, was always, I mean, ever since I started, my YouTube channel, was always, to create, a tiny motor, that can be used, that, I mean, it's not, an efficient motor, but it's, efficient enough, to be used, in robotics. Right, it won't,

**Chris Gammell:** burn itself up, is probably the, the most important thing, in the beginning, right? Yeah. I feel like, one of the problems too, is just like, popular culture, like, like, when I see your stuff, and just like, these kind of like, seemingly, self-driven, obviously there's, intelligence behind them, there's, you know, you're driving them yourself, whatever, but just this kind of like, this realm of things, my mind jumps to, like, Big Hero 6, did you ever watch that movie, from Pixar, with like, the, actually, Microbot, Microbots? What are they called, Nano, no, they called them something like that.

**Dave Jones:** They called Microbots, I mean, they were called Microbots, yeah. That was, I think, one of, of the inspirations, behind the name, because we, we considered like, a couple of names, but, I think, because, when it comes to PCB actuators, I mean, let's put it this way, if, if you have, just one actuator, it's, you need to have, one PCB, components for one, but imagine having, that same PCB, multiplied by, 10x. Yeah, right, right.

**Speaker ?:** So,

**Dave Jones:** it's, it's going to be the same, the PCB, it's going to have the same price, you're just going to pay, extra for the component. So, that is one of our, main things, that we're working on. So, like,

**Chris Gammell:** so like, efficiency of the solution, because it's, because PCB materials is effectively, commodity at this point, you can kind of, start to expand, using that.

**Dave Jones:** Yeah, it's, it's like, I mean, this is still an ongoing thing, that we're currently working on, and nothing is published yet, but having one actuator, or one motor is cool, but, what other applications, could be created, if you have like, 10 motors, on one PCB. Yeah. So, that's some of the things, that we're currently playing, playing with.

**Chris Gammell:** Yeah, yeah, totally. I just feel like the, big hero six ruined my brain, because I'm like, oh yeah, tiny little microbots, that are like, you know, self-powered, and you know, can self-assemble, it's just like, yeah, I mean,

**Dave Jones:** that would be pretty cool, but so far, so far, I think we have to focus, on just one dimension.

**Chris Gammell:** Yeah. Yeah. They might have taken, a couple mental leaps, in a animated film, I gotta say. Yeah. Well, you're fighting a good fight, that's what's important. Let's talk about, some of the, some of the realities, of putting current, through a PCB like this, like, okay, so, let's maybe, paint a picture, for people, with words, you know, we only have words here, but we're painting a picture, someone's going to, like, what is, what is your, kind of common use case, when you're thinking about, maybe we just talk about, like the flat flap, that's a tough one to say, the flat flap, is like a, so it's like a flex PCB, on top of a rigid PCB, is that, is that what that is?

**Dave Jones:** Yeah, so it's, it's basically, one flexible PCB, that have, aluminium stiffeners, okay, it has two aluminium, three sorry, which, fold, which then, folds the PCB together, has a pocket, for a magnet, and the, coil interacts, with the magnet. Got it, okay, and then,

**Chris Gammell:** is it, there's a solid state magnet, on there, or no, or is it only, Yeah,

**Dave Jones:** it's a normal, I mean, an N52 magnet, so it's, the highest grade, of magnets, so when the coil, is energised, it basically creates, a small magnetic field, that is, like strong enough, to move the coil, upwards. Got it, okay,

**Chris Gammell:** all right, and yeah, and so, I'll link to the, you know, I'm gonna have show notes here, I'll link to the, the actual product itself, but this is the one, if people have seen your latest video, where it's, moving like a butterfly wing, like a printed butterfly wing, that's a great example there, so it's, moving paper in that case, and you're showing it, like moving a ping pong ball, as well, and some mirrors, that sort of thing.

**Dave Jones:** Yes, so far, that it's, one of the, most popular applications, for it is, I think, it's mostly used, by artists, so, like, to create, kinetic sculptures, and stuff like that.

**Chris Gammell:** Got it, okay, so then, now we're talking about, this sort of thing, and what is the actual, like what is the current, that's going through a coil, to actually like, make motion happen?

**Dave Jones:** So, the current, that, it obviously depends on, the voltage you run it at, but it's usually around, 180 milliamps. Okay. So, that is the constant, if you drive it at constant power, because you can, like, generate small pulses, to not overheat it, and stuff like that.

**Chris Gammell:** Yeah, so that's another good point, then too, so like, what does it take, like how, do you have monitoring on board, or do you just kind of have, like, a general knowledge of, like, don't overdrive it past this point, like, how much do you have to, like, if someone was implementing, this specific thing, how much did they have to do it, how much did they have to, like, kind of tweak controls, to make sure they don't burn it up, or overdrive it, or anything like that, and then how much, how much then would they have to do, if they weren't using a product like yours?

**Dave Jones:** Yeah, so, I mean, there's obviously, the main limitation, is the temperature rating, of the PCB, which is, I think it's, 130 degrees Celsius. Okay. But, on our website, we listed this as, five volts maximum. Okay. And that rating is derived from, the resistance of, the coil, because the coil itself, has the C resistance, that is dependent, on the length, of the coil. So, depending on how many turns, the coil has it, it will increase, the length, and it would, will add a series, resistance apart, from inductance.

**Chris Gammell:** Okay, so then it's just a, geometry problem at that point, like geometry times, copper thickness, kind of thing, huh?

**Dave Jones:** Yeah, because it, it just depends on the number of turns, and you can easily, derive also the length, and try to estimate it, from a couple of, PCB calculators. But, I mean, there, there are other problems, like, because there's, like, the variation of the trick with, that the, um, PCB manufacturer has, um, so we had to, deal with that, for example, and other things. But, that's, that's mostly, where, where the power rating, comes from.

**Chris Gammell:** Okay. And you said 130, for the PCB temp, what, what, is that just the delamination? How do you determine that, as like a max temp?

**Dave Jones:** So, there's the TG value. So, for normal PCBs, it can go up for, for example, 270 degrees Celsius. And, I think it's, it's common practice, to, to, like, go to, like, 30 to 40 degrees, slower than that one, operating PCBs, at high temperature.

**Chris Gammell:** Cool. Yeah, that's great. I, you know, I, I've never, pushed the bounds, with my stuff like that. You know, like, I always just try and, like, give myself tons of, operating margin. And it's like, by definition, you're trying to do it, at the limits, because it's like, that you get more out of it, in this way, right?

**Dave Jones:** Yeah. I think this is a, a very interesting field. I, I learned those from it, when trying to build PCB heaters. So, yeah,

**Chris Gammell:** the self-soldering circuit, I saw that one.

**Dave Jones:** Yeah. The self-soldering was like, the last, the last step. But, before that, I, I tried to build like, a PCB reflowing quad plate, which didn't work. I mean, it worked. There's, there's a lot of people, I'm trying them right now. But, the main conclusion was, that it wouldn't be reusable. So, after like, five times, you, you could see like, the solder mask, the sculler, and stuff like that. There's obviously, when, when the PCB reaches, around 200 degrees Celsius, for example, just enough for the solder to reflow.

**Chris Gammell:** Just need to start with like, brown solder mask, and then you're, you're set, right? Yeah. I don't see any discoloration. What's the problem here, folks?

**Dave Jones:** Yeah. But, but I mean, after that, I think it, it sort of proven, the self-reflowing PCB idea, was sort of perfect, because, the PCB just had to reflow one time. It had to reach like, 170 degrees Celsius, for just one time. And then, it's done, because, it's a function of time as well.

**Dave Jones:** there's, how, how much, PCB can sustain heat. It's a function of time. And, six minutes, it's like,

**Chris Gammell:** still okay for it. Got it. And then you, so you also made one about, flex PCBs too, because obviously you're, you're doing this on, rigid FR4, but then also, flex. So then like, how do you think about, you know, choosing project types, between those two?

**Dave Jones:** Yeah, it really depends, on the nature of, of the project. If, if there's, for example, something like, mechanically, where the flexible PCB can, for example, avoid wires, or, be like, a little bit simpler. I mean, that's why I like to use, flexible PCBs, because it usually offers, this kind of, opportunity, where you like, instead of using, wires, I know, I mean, it's just wires, but, when you like, consider producing, hundreds of, of this thing, soldering wires, one by one, it's going to be, a little bit of,

**Chris Gammell:** annoying. I feel like that, that same like, truism that like, could be applied, it's just wires, it's, it's just resistors, it's just transistors, it's just billions of transistors, you know what I mean? Like, it's just like, it's just turtles, all the way down. Yeah, I think it also looks neater. Yeah, yeah, totally. I, I always think about, you know, batch processing generally, right? Like, whenever, this always comes up when people are talking about like, well, I want to make like a PCB robot, something that like draws traces on a PCB. And even if it was like perfect copper, drawn on a PCB, like perfectly conductive copper, drawn onto a surface, right? That's like always what these PCB printers look like. it's like,

**Chris Gammell:** you're still rastering versus like batch processing. Just the, the fact that you're doing batch etching on something like a flex PCB or a regular PCB, like that, that's one of the big advantages from my perspective of just like, just the chemical element of it all. When you have to do any kind of like point to point or whatever, you know, however you define that, that, you know, raster kind of process, you, you almost immediately lose out to a batch processing.

**Dave Jones:** Exactly.

**Chris Gammell:** Stamping versus milling. You know, there's all these, always these sorts of things. So it's just, then you really take advantage of a lot of the, a lot of the capabilities with that with flex. So that's great. Okay. So now you're designing FR4 or flex coils. How much, how much math are you doing on a daily basis? Do you math? I don't math anymore, Carl. I, I know you're a little, a little closer to university days, but I am very far from my university days.

**Dave Jones:** Yeah, me too. I mean, I think now it's, I'm, I'm close at being, I think 10 years,

**Chris Gammell:** 10 years. Oh, wow. Yeah. Okay.

**Dave Jones:** Yeah. Cause I graduated in 2016. So, yeah.

**Chris Gammell:** Yep. Yeah. You're getting there. Huh? Yep. So how much do you do? So is it, how much is it like experimental versus like, when's the last time you touched Maxwell's equations? How about that?

**Dave Jones:** Yeah. No, um, basically I started as like doing like, it was like iterative. That's how it started. Then, um, as, as I, I started getting, um, more in depth, I started trying to like estimate the perfect length to get the temperature. Right. Um, because for example, one of the things that a few people notice, flexible PCBs, for example, will get hotter than a far, for PCBs because they have much less area. Um, because they are super tense. So the heat that the coil generates will transfer easily.

**Chris Gammell:** Yeah. Like the heat capacity of the, of the material and stuff like that.

**Dave Jones:** Exactly.

**Dave Jones:** As well. So there was like, um, stuff like this, like for example, the tolerance of the manufacturer, that was one of the things that I didn't even consider in the beginning. Then when I started, um, receiving batches of the same coil, different manufacturing batches of the same coil with different resistance. Um, obviously there, there, there was a, like,

**Chris Gammell:** there's an extra problem that you have to solve. Yeah. And how, how did you get into that? Did you start doing like incoming inspection and stuff like that?

**Dave Jones:** Yeah. So what I started noticing is that if you were there at different batches, I mean, the manufacturer will either use a different factory or a different machine or stuff like that. So there will be a tolerance and, and, uh, even in the copper thickness, there are some tolerances. So, but the main problem I think was the wet. So I was fortunate to, to get to the root of this. The, my local university offered me to inspect, it with the X-ray machine.

**Chris Gammell:** Oh, that's nice.

**Dave Jones:** Um, so I could like measure the sort of not accurately measure, but it was visible that there was a problem with the clearance between the copper traces, copper windings. Oh, really?

**Chris Gammell:** Yeah. So, so this was, this was the trace to trace spacing because of like the etch process versus like,

**Dave Jones:** so it's like the, the pitch between the tracks.

**Chris Gammell:** Okay. All right.

**Dave Jones:** Well,

**Chris Gammell:** what was the net result of that? Was that, that was due to,

**Dave Jones:** that was overheating? Yeah. I mean, there's not much you can do about it, but you have to like tell to the manufacturer to measure the resistance and make sure that the same process on this or the same machine is used for different, for the same orders and stuff like that.

**Chris Gammell:** Got it. Got it. So when you send out a, uh, a design, right? So you've, you know, you have sponsors in your, your videos, which is great. And a lot of those are lower cost PCB services, which many of which I use and love. Are you sending really well specified like PCB drawings then as well?

**Dave Jones:** Yeah. I usually write the specifications on the PCB design file itself to make sure that, um, whoever's seeing the files before they get manufactured is well aware of what's being there.

**Chris Gammell:** Yeah. Got it. I just feel like when I, um, you know, when I was starting to use some of the lower cost PCB services, you know, as they were coming up, because I think they rose after I was making PCBs, I was just like, Oh, they got this. No problem. But then it was like, you know, a couple of times I'm like, Oh yeah. Right. Controlled impedance traces or like thicknesses arena, like where it really, at the end of the day, it's, you know, on us as like manufacturing engineers, effectively like switching our hats from design engineering to manufacturing engineering. It's like that incoming inspection and like giving feedback about process type stuff like you're dealing with. It's just, it becomes a whole other job, you know?

**Dave Jones:** Yeah. I mean, it was the same for me. Um, because using like these, these types of manufacturers, some of them are good and some of them are bad. Right. Um, so that's why I picked one and stayed, stayed with, with them for a long time.

**Chris Gammell:** Um, but I should say, I'm not, I'm not picking on the low cost services. I think it's really that I, because there's no way around it with like the, traditional PCBs manufacturers. Like they, they want to accept the files without a drawing with it. Right. Whereas like, you know, low cost manufacturers are just like, yeah, you're using our process. No big deal. It's like, for me, I'm like, oh yeah, you still need to send the file with it. Right. Even if you're, no matter who you're using, that's, that's the big catch that I'm getting at.

**Dave Jones:** Yeah. And, and I think, I think they're, they're improved quite a lot because now there's the, some advanced options and stuff like that. So I don't usually get, um, out of problems, um, from their side. Now that everything is sorted out. So that's great. That's great.

**Chris Gammell:** So now you are moving into the manufacturing stage with, with microbots and stuff like that. Yeah. Do you now have more like test tooling in house? Do you have to do that?

**Dave Jones:** Yeah. We do some testing, but the testing we're doing so far is making sure that the supplier, um, sent us like, we're checking the supplier sort of. So the PCB supplier.

**Chris Gammell:** Okay. Yeah. Doing what they're saying. They're doing that sort of thing.

**Dave Jones:** Because obviously they do, um, their testing as well. And we like to have to make sure that the quality of the, the PCBs that they have sent us is to what we specified.

**Chris Gammell:** Yeah. And I mean, I think you have an interesting, like a new sector, not sector, a new characteristic that I, I've never actually had a test for before, which is like motion, right? Like I've never had a, like a final test stage where I'm like, is this thing moving properly or not? But I would imagine you have to do that sort of thing. Are you, um, do you do that with like vision or just like.

**Dave Jones:** Yeah. So, so for example, with the flaps, it's, it's all it has to do with, um, there is this, with the quality resistance. For example, if it's like, we check if, if it's in, um, within its specified range. And if it's between that range, we know for sure that its motion will be correct. So we're using like, okay. The quality resistance to check for its motion as well. And obviously we, we do also visual inspection and stuff like that.

**Chris Gammell:** Mm hmm. Yeah.

**Dave Jones:** And make sure that for example, the flexible PCB is not, um, banded, like, like folded, for example, in the wrong manner or stuff like that. Right.

**Chris Gammell:** Yeah. I've just, I imagine like, like you have like the time flap, which is like a new kind of persistence of vision thing. And then like a robot as well that are coming. And those kind of have all alternate, like, again, like I've just never dealt anything with motion before as like a, as a final test stage. That's an interesting thing.

**Dave Jones:** Yeah. So the time flap is one of the, I think one of the most, the longest ongoing project that we have, because I think it's, it's been going on since I, I released the first prototype and we're almost there, but, um, the scary thing about it is producing, like when you start thinking about producing hundreds of it, because mechanically the, it will, it will affect the behavior of the, of the screen. Yeah. Um, so we like introduce stuff into, into it, like, um, automatic tuning of the frequency and stuff like that. I'll make sure that, that the flap, um, will continue, um, flapping at the right speed. Um, it, it, it got a bit complicated, but it's, it's one of the, um, fun projects we've been working on.

**Chris Gammell:** The, the flap factor or the, uh, yeah. Flappiness. Is that a, you need, so you need to make up your own terms to start, branding around these sorts of things.

**Dave Jones:** And we also think, because after the engineering gets finished, there's like the, uh, the thing, does it look nice in everyone's eye or, or not? Then there's, those are their aspects as well. So that's true.

**Chris Gammell:** Yeah. I guess when you have like these visual elements, like it's, uh, aesthetics, you know, people always have, uh, I guess opinions are like, uh, belly buttons. Uh, everybody has one. That's not the, not the original phrase, but, uh, modified for family friendliness. Uh, and like, yeah. So you just have to kind of do almost like user testing and just be like, this is like, okay enough to everyone. That's,

**Dave Jones:** I think that's important as well, because I mean, before you, you like, um, go with the, it's not a risk, but it's a huge like headache. Yeah. Um, to release a product. So you, you have to make sure that everything is on point.

**Chris Gammell:** Yeah. Well, and even like, you know, you obviously you do a lot of videos and like you do your best to make, to be able to show it on video, which is not easy when it's a moving led thing on its own, uh, you know, just like, uh, frame rates and stuff like that. But then just matching people's expectations from seeing it on video versus seeing it in person. That's always tough too.

**Dave Jones:** Exactly. Yeah.

**Chris Gammell:** What about, uh, so you also have like, you use a lot of drivers for these sort of things. I've used like some Allegro parts in the past, like drive circuits. What makes for a good drive circuit for motors or PCBs or things like it?

**Dave Jones:** Yeah. Um, so I've tested a lot of different drivers, but, um, one of the main things that, it's my number one priority is if the driver is small. So for example, um, in my last PCB motor video, I created like a custom for the driver, but the PCB was quite large compared to the motor. So for me, that doesn't make sense. So having like a one chip that could replace this all is, is like a bonus. Yeah. So I think size is, is since, we're like creating tiny robotics and having like, um, flat actuators and stuff like that. I think size is the number one priority when it comes to drivers.

**Chris Gammell:** I always think to myself, I'm like, well, it's like mostly an H bridge. I could like do it myself. Right. I was like, I could buy transistors and build it myself. It's like, that is generally the wrong idea. I feel like, like you could, but should you, right? It's like kind of the other stuff that's in there.

**Dave Jones:** I think all engineers, um, go with this approach.

**Chris Gammell:** Yeah. Yeah. Until they, until they get some shoot through and blow up a board. Right.

**Dave Jones:** Exactly.

**Chris Gammell:** Yeah. I mean like how, how advanced are these chips at this point? Like, are there, are there additional features that are in these driver chips that, that you look for? Or, or is it just kind of a, uh, is it like you said, just size and, and just general, um, efficiency?

**Dave Jones:** So for the PCB motor, there's quite a number of chips that were available. I tested a bunch and just selected, um, the one that performed the best. Um, so, um, but I mean, for the, um, the driver of the actuator, um, it's, it's just an H bridge really. And then we created a library so that, um, people can just use it to control the, and our actuators. Okay. Great. Yeah. So the library has,

**Chris Gammell:** has like an interface in front of it or, or no, like, uh, like a micro control in front of it, or is it just, just driving, driving that specific, um, yeah, it's just, um,

**Dave Jones:** drive the specific waveform. Um, we created multiple examples. So, um, one of them can just use with any Arduino. And then there's one that, it is more specific for the ESP family. Um, because one of our, um, next modules is going to have an ESP 32 C3. So it, it, it's, it integrates with that, um, nicely regarding drivers. There's, there's a ton of options. For example, H bridges, there's ton of options. And like, if you, if you like, see these little Chinese chips, there are sort of like knockoffs, there can be really cheap as well. But I think you also have to select, um, as a safe option as well. So something that, that, so that's one of the things that, that we, that we tested, for example, like there was a chip, a specific Chinese part chip that was like five times cheaper, but I mean, the data sheet was in Chinese. Right. Right. Right. RDS on was not, uh, specified in the data sheet. So there's stuff like this.

**Chris Gammell:** Really? Okay.

**Dave Jones:** Yeah.

**Carl Bugeja:** So like, yeah,

**Dave Jones:** you get what you get, you know, we recommend under driving this chip. I think you, some, so sometimes you also have to favor the quality rather than having everything cheap.

**Chris Gammell:** Yeah. Yeah. And it seems like, like, like you said, with like building a library too, like having the knowledge of a particular family and just the, knowing the corners of operation and where things could go wrong and maybe having that in your library. So you are dealing with a very particular chip. It's not like just the generic, it's not like an overall generic thing. It's more like specific to different drivers. Right. Yeah. What about, um, so you have a project on your YouTube. That's pretty great. The little four wheeled foldable robot. So like that as a, as a project, which I think you might be selling in the future. Is that right? Um,

**Dave Jones:** we're not a hundred percent sure about it because I mean, first we were, we're currently in the final stages of, like, um, finalizing the motor. So, um, once that is finalized, we will take it like to the next step, which would be, um, to wield, um, robots, hopefully. Um, and then we'll see, um, we also test it out with the rover. Um, but the thing is that our goal is to create, um, small, um, robots that could interact with each other someday. And like to do that, you have to bring the price of the robot to a very low price. So having two wheels rather than four would be cheaper. Right. Two fewer wheels is, uh, you know, savings. So that's, that's one of, um, the things that we're still, um, exploring.

**Chris Gammell:** Okay. Yeah, I am really, I mean, I'm amazed at some of the, you know, some of the manufacturers that can do like those little, uh, RF drone, you know, they, they give you like for like $20, they will send you like a little quad copter with a remote and they like talk to each other, you know, they've got RF link and it's just like unbelievable that all that stuff can happen. I see it's a toy, but like that you can get that all working and it actually flies, you know, for 20 bucks and that means they're making it for what? Like four bucks, maybe, you know, like, yeah. So in the case of that sort of thing, like, uh, so you have a controller on board there and that is then driving a couple of motor drivers that then actually drove, drive the coils that are on board, that sort of thing. Right.

**Dave Jones:** Yeah. So the rover is, is, was made from one flexible PCB that folded together to form like a cube shape and a cuboid shape. Sorry. And then the wheels gets bolted onto the sides of the cuboid and it just drives. So it has PCB motors. So the staters are integrated into the PCB and that's, and the magnets of the motor, um, are integrated into the wheels themselves. Uh, I mean, it, it was a very fun project, especially to design the final result. I think was not that great, but I think it can be improved in several ways.

**Chris Gammell:** Yeah. I mean, and yeah, well you said, I mean, it looks like that's a ESP 32 on there, but you said you're switching to the C3 for certain. Yeah.

**Dave Jones:** We're switching to the C3. I mean, it's, it's one of the most popular micro microcontrollers, um, that has wifi and Bluetooth. I think the C3. And it's five. That's cool. Yeah.

**Chris Gammell:** It's cool. I mean, it really doesn't matter at all from like, you know, like other than like me saying it's first, I was like, Oh, okay. but it's still interact with it through code. So, and it works. It's cheaper. It's packages is really small as well.

**Dave Jones:** Yeah. So for us, it hits all the right boxes. So it, it has a, like an okay price. It was, it has one of the smallest packages available. Um, and it's, it's getting quite popular, um, with, um, Arduino users. So that, that's why we went for it. So, because we would like, to make it like, uh, into a maker kit. So, um, we want to make it as easy as possible for, for people to use.

**Chris Gammell:** Yeah. That's interesting. Are you, so then are you developing when you're developing stuff for Arduino, in that case, are you writing a new library or are you kind of piggybacking off existing libraries?

**Dave Jones:** Yeah. Um, it's kind of, um, the two cases at the moment. So we're using, um, some libraries and we're also creating our own, um, things as well.

**Chris Gammell:** Okay. You doing any ESP IDF or anything like that?

**Dave Jones:** Um, no, not yet.

**Chris Gammell:** No.

**Speaker ?:** Okay.

**Chris Gammell:** Yeah. I've dug into a little bit. I'm, I'm generally very impressed with how advanced the RTOS is. This is, you know, just how it's progressed over time. And that's what I think is running under the hood for all the Arduino port as well, is it's running ESP IDF under the hood. Um, but it's, you know, it's more advanced and I'm still struggling a little bit with it, you know, but yeah, that's nice. And then, so then can you, with the Arduino libraries that you use for it, are you able to have then remote control? Like what does the remote control look like? Are you actually, you're actually using the Bluetooth and wifi in order to control this thing?

**Dave Jones:** Yeah. So for the Rover, um, I connected it to a PlayStation joystick and, uh, just connected through wifi. But in the future, I think we're also experimenting with the idea of connecting, um, ESPs together and using, um, one as the controller and one as the robot. Oh, cool. Okay. Cool. Things like that.

**Chris Gammell:** Yeah, that's cool. That's cool. Yeah. I mean, you could, the, um, ESP link is, I think they have like a pro, their own protocol as well. Yeah, I think so. That sort of thing. That's pretty fun. Any plans to internet connected? Are you going to make it so that you could rove Rover around the, around the internet? Yeah. I think it's like connected to the internet, right?

**Dave Jones:** All the things that's happening with ESP, um, right now, and there's ESP home. And I think all of that stuff is, it's quite interesting to look at. So,

**Chris Gammell:** yeah. Yeah. We had Keith on the show from Nabucasa talking. Yeah. I, I aired the episode yesterday. Yeah. So maybe we'll put you two together and see what, you know, little, little home Rovers. That would be, that's the jam right there. Carl, how long until I get a little, very, very tiny robot Rover to fetch me a beer? That's, that's what we're really need. That's like the, uh, the classic robot thing, right? It's like getting a, getting a soda or a beer out of the fridge.

**Speaker ?:** Yeah. Yeah.

**Dave Jones:** Maybe spot will do that for you someday. Yeah. Yeah. I think that's their goal right now to like go into the domestic things.

**Chris Gammell:** Oh, the, uh, Boston dynamics and like the electric dog. Yeah. As much as I, I have a friend that works there and I love him to death, but, uh, the, uh, everything they do is creepy. I'm so creeped out every time. It's, you know, it's always the uncanny value with those. Cause it's just, they're moving into that space. It's just like, yeah,

**Dave Jones:** I think it's right. The first thing that I've done after I graduated, um, I sent, uh, my CV to them. I said like, this is my only chance. Um, if it's either this or, um, start like my own thing.

**Chris Gammell:** They never got back to me. And I just said, yeah, I guess, you know what? We need you to go make robots on YouTube for everybody to check out. So that's good. I mean, that's the thing though, too. Like I, I love that you're doing this kind of stuff on YouTube because it's just gonna, I have to imagine people contact you who are up and coming through the space and they're just like, yeah, I want to build more stuff like you're building.

**Dave Jones:** Yeah. I think that that's one of, um, the main rewards from making YouTube videos. You inspire others, um, especially young makers and young students. Um, um, I mean, receiving those kinds of emails, um, it's quite rewarding.

**Chris Gammell:** Yeah. That's great. Do you end up, so do you have a, uh, did you build a community with this sort of thing as well then? Like where do, where do people gather to, wow, to gather and agog over your, uh, your creations and, or build their own? Um,

**Dave Jones:** I think it's mostly through social media. So people, um, who follow either my Instagram or my Twitter, Twitter, not that much lately, but, uh,

**Chris Gammell:** more Instagram. I'm sure there's, you know, you're making robots and I'm sure the bots love following you. Onward.

**Dave Jones:** It's mostly, um, through Instagram and email. Um, that's great. It's nice. Nice to see that.

**Chris Gammell:** Have you seen like kind of follow along projects that are like, like, Oh, I saw Carl doing this and now I'm building my own. Do you get to see those as well?

**Dave Jones:** Yeah, I, I do see some of them sometimes. I mean, it's awesome. Some of my builds are, are a little bit of expensive. Um, that's, that's one of the main reasons why we started microbots to make them more accessible. Um, so, yeah. So it's, it's a little bit like, I mean, if, if I was a student back in, in, my student years, I mean, I couldn't afford a flexible PCB or, or I mean, now they're much cheaper than, than what they were before, but. I mean,

**Chris Gammell:** it's almost like standardized components at this point might as well get a jumpstart by using your stuff. And then if they need to like, I don't know. I, I started building a robot at one point and like, I'm like, I need to build everything from the ground up and build every like driver. And it's like, well, I could have gone to, was it Pinoco? There's like, there are a bunch of like DF robot. And like, there's all these other sites too, that like had these components. And I, I should have started there and gotten the end robot working instead of starting at the bottom up. Right. It's like the, you're at the point where you are optimizing for a very specific application, which makes a lot of sense to me, but like, as a beginner, as I was, it, I shouldn't have started at the beginning there. I shouldn't start at the bottom.

**Dave Jones:** Yeah. I think that, that makes sense because I mean, when I was a student, I, I was doing the same exact thing. Um, so that's the, the main reason why these type of kits make sense. Yeah. And for us to build, because, um, and sell just for others to either test out and perhaps inspire them to create something better. And hopefully, uh, they will. Yeah.

**Chris Gammell:** Yeah. That's great. So after uni, you, you went out into the world as well. Like, what did you end up, what were you doing when you had gone out before, before you started, I guess in conjunction with you, uh, going out into the world or going into the world of YouTube, what, what were you designing when you were in the, in the commercial space?

**Dave Jones:** Yeah. So it's, it's a bit of, um, I mean, not a long story, but, um, after I ended university, I, I sent the CV to Boston dynamics and I didn't go to the flight on them. Um, and so I started a startup with my friend. We work working on, um, drones and Bluetooth tags at the time. The drones were still like getting popular. So it made sense to, to go into that space. Um, but I mean, after a few months, like we couldn't fund it, um, more because we are still like in the R and D stage and it was going to take months or even years, um, for us to turn it into from a prototype to a product because it wasn't just a quadcopter. It was a coaxial type of drone. Um,

**Dave Jones:** um, two propeller drone, uh, like the size of, um, of a tennis ball. Oh, wow. Okay. Yeah.

**Chris Gammell:** That's a lot of control there, huh? Like a lot of feedback and stuff like that.

**Dave Jones:** Exactly. Um, the, the main problem was, um, manufacturing, I think because it had like flaps, um, and stuff like that. And when you compare it to a quadcopter, it's, it's much easier to produce a quadcopter rather than a coaxial drone. Yeah. A lot of,

**Chris Gammell:** uh, a lot of margin in, in the, yeah.

**Dave Jones:** And a lot of plastic things and stuff like that. Yeah. Uh, the time we didn't like, we had a cheap printer and printers were still like, um, starting as well. Yeah. Um, then after, after the startup failed, um, I went into the automotive industry. So I worked there for three and a half years during which time I, I was also, um, doing YouTube videos as well. So during this time I, I was working on designing electronics, um, for concept vehicles. So I, I did this for like six months. but then I, I was switched to, to software. So I was doing like mainly software that goes into devices that connects with like the connect to work of a car and stuff like that.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Cool. I mean, and I learned a lot from the experience, um, because it's, I mean, the, the products that they were making, um, they, they were producing like thousands of them. So I learned a lot from just, uh, the difference of producing one thing and producing a hundred thousand of that. Yeah. Yeah. Uh, that,

**Chris Gammell:** that was quite a learning experience. And that, that was in Malta where you're based. Um, is, is automotive big there? What, what is it? What are you, I mean,

**Dave Jones:** not that there's only one company, um, okay. There's the company, not one company. And, and, and, and, um, it's just one company that designs electronics for automotive.

**Chris Gammell:** Got it. Got it. Okay.

**Dave Jones:** Um, so it's called method electronics. Um, I, I was quite happy for some time then, but then I mean, COVID hit and things were a little bit different. And I decided to, to try and switch full time on YouTube and not just YouTube, just, um, doing, um, what I love doing. Um, just building electronics in my garage. That's great. And that, that's worked pretty well. I think. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. We were talking a little bit about just like what I, I was asking what Malta's like in terms of the electronics industry and stuff like that before the show as well. And it sounds like there's not a lot there, but there is stuff like, you know, but you, you've got some, some folks, you know, in the town and, and stuff like that.

**Dave Jones:** And yeah. So it's a, it's a pretty small Island here. Um, so you cross from one end to the other and like an hour. So, Oh, nice. Okay. It's quite small. Um, but I mean,

**Chris Gammell:** I think the really important thing is like, do the PC, you know, how's DHL service and how does, how, you know, how fast can you get a digi key box? That's my judgment. Okay. And I guess that was import duties too. That's another thing that I don't really think about here, but it is even here. I have to pay them. You know, they're just usually attached.

**Dave Jones:** I mean, the only, I think the only postal service that sucks is UPS here. So, but I mean, for me, it's, it's quite, because I have all my family here. So it's quite nice having to live here. Yeah. And I don't see a reason so far to move to anywhere. Anywhere else.

**Chris Gammell:** No, I think that's, that is really great. I mean, the fact that like, it's gotten so much easier to, to be able to be a, you know, be a manufacturer on your own or just like send, send off design files to have stuff just kind of remote assembled, just thinking about like 20, 30 years ago, the services were there, but they, maybe the communication wasn't. And, you know, I think even just the industry of like being able to, I think even things like Shopify and like similar, like marketplaces for selling gear, it's just so much easier than it used to be. You know, there's logistics and online stuff. All that stuff has really improved the ability to then manufacture somewhere locally in China, somewhere else, have a store of equipment, have a store of merchandise rather. And then like being able to sell it, you could potentially never touch the hardware if you wanted to, and still have an electronic business, you know?

**Dave Jones:** You just, I mean, I, I think the word will, will even makes everything simpler to do something like this. Yeah. Um, I, it's not something that you would be able to do. I think in the, in the early days.

**Chris Gammell:** Yeah. Yeah. It's definitely gotten a little, a little better in that way. So that's, that's really nice. Yeah. What, uh, what's on your, as much as you're willing to share, what's on your, like your project list, uh, other than the stuff, you know, obviously people can go on microbots.io and see kind of the coming soon or the, the, the test stuff. Well, like, what's the thing that you think about? Like, oh, I really, I want to learn that. Or I want to build that. Like what's, what's on your list of, of things to, to do with PCB actuators and motors and things like that. Where, where's the, where's the future of this space?

**Dave Jones:** I think the, the future is like, find a simple way to control multiple actuate, PCB actuators. So actuators on the same PCB. Um, I, this is something I've been trying to do for, I think the last one and a half years. So I've been researching a lot of different options out there and I've always come to the same conclusion. And I think we're finally, um, a step closer at, at, at doing that finally. Um, and that's why we named it micro bots and all that stuff. Um, because it's,

**Chris Gammell:** it's the main goal. And does that mean like, uh, so is each coil going to have his own microcontroller? Like, I guess it's one thing you could do with low cost microcontrollers as well, but then programming becomes an issue. Like what is the, um, what, what is enabling that sort of thing to happen?

**Dave Jones:** Yeah. I think it's like, it's, I don't want to spoil too much, but the way, the way we're thinking about it is like daisy chaining the coils.

**Chris Gammell:** So got it. Okay. Yeah. I mean, cause I mean, even if you had like, so you have your plug and play controller, right? The flex are, and that looks like that's, you know, a way to interface to these different things and like kind of abstract some of the difficulties, but then do you have one per board and you kind of pass the idea down the line?

**Dave Jones:** That's what it stops making sense sort of.

**Chris Gammell:** Yeah. Yeah. I mean, like I've been playing with like low cut, like the CH 32 V double O threes and stuff like that. And those are low cost. And maybe you could put a bunch of those on a board, but it doesn't mean it's easy to do, nor would it be fast to program that. Right. It's still like a, it's almost just a, it's a scaling problem. Right.

**Dave Jones:** Yeah. Because I mean, there's, there's, so what I found, there's a lot of different options and the problem is not just scaling. The problem is like the price per cell sort of. So the price per one coil. Yeah. Because it, it, it would be, I mean, you can do it with like, I mean, just an age bridge, but you would have a lot of wires, but then once you solve the wires problem, like how, how, how expensive is it to drive one coil? And if you find a driver that can drive multiple coils at once, is it like cheap enough to make sense or, or not? So that's one of the main problems we've been trying to solve. Oh, interesting.

**Chris Gammell:** And do you think it'd be possible to drive multiple, maybe this is the thing you didn't want to talk about, but is it possible to drive more than one coil with a single driver to like start to, again, just drop the price per cell?

**Dave Jones:** Yeah, it is possible, but I mean, that's, not the way we decided to go because it compared to the solution we're, we're working on right now. It's, it's, it's, it was, it ended up being more expensive because the, the type of drivers that can drive like six or 12 coils still cost like eight euro when you, you buy them in, in hundreds or thousands. So yeah, it's their price. Like don't drop. Right. Even though they're just one, I see.

**Chris Gammell:** So yeah, it's kind of interesting. It's almost like, you know, like,

**Chris Gammell:** so obviously as LDS were coming up, right. They started to think like, Oh, well we could like use them as backlights for TVs. And then over time, like the reason TV, like flat panels, TVs are so expensive, so cheap these days, because they're effectively not printing, but they're, you know, like the, the array of an led TV is kind of the same problem where they're dropping the price per pixel, right. Or, you know, whatever, does a motor have a pixel equivalent, like a, it's not a voxel. That's a, that's something different. Is there a name for that? A moxel pixel? Maxel? You got to come up with this. You got to coin this term, Carl. I think you got to, you got to make this thing, you know? I mean, I don't think there, there is such a thing. Yeah. But in my mind, it's just like they, they changed, they saw that they, they had that similar problem where they, they were trying to drive down the cost per pixel, right. They still needed to have individualized control over RGB for each pixel. And then, you know, the schemes to do that sort of thing of like, like a cross hatch or a daisy chain or similar, you know, kind of thing where you're, you're trying to drive all this stuff at a high refresh rate. And potentially high current. I mean, LEDs benefit from silicon improvements, but it's like similar. It feels kind of similar in that way. If you're trying to make like a, a large array of, of these actuators.

**Dave Jones:** It is. I mean, it's, it's like our main inspiration from it are like flip dot displays. Yeah. One of, I think one of the main issues with them is that they are pricey. Yeah. So that, that's why, I mean, hopefully we won't go, through the same thing or we, but I mean, Pacificoils offers because they're pricey and they're bulky. Pacificoils would at least offer the, the cool thing that they're very thin. So.

**Chris Gammell:** Yeah. Right. Right. Yeah. I'm looking at your PCB actuator based on the flex are, which is basically it is, I mean, you can, you have a configuration where it is. Basically it's got a googly eye. That is a flip dot basically. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Well, that's what we all want. We want, we more googly eyes and flip dots in our lives.

**Dave Jones:** We're working on making something like a display, a mechanical display. That's much prettier than, than the googly eye thingy, but Hey,

**Chris Gammell:** I love googly eyes. So don't, don't change it too much. Just nicer googly eyes. That's what we need. You know? All right. More, more googly eyes coming our way in 2024. Yeah. Kyle, where can people find you online? And how can they get in touch with you if they need to?

**Dave Jones:** So the easiest way to find me, I think is through YouTube or Instagram. And they can get in touch with me either via email or through the microboards.io website.

**Chris Gammell:** Great. Well, thank you for stopping by and, and telling us about all this stuff. I think it's, you know, like you, you're, you're operating like on the edge of this stuff with the, you know, trying to push PCBs and flex PCBs to the edge of like what they can do. And just like, I really like how you show your experimentation. You share that stuff. You share like, you know, one thing that comes through from your videos, it's just that you do a ton of work to get one video done and it just really shines through. So thanks, thanks for doing that because you're, you're helping all of us. Yeah.

**Dave Jones:** That means a lot because it's really, it's really, um, does take out all the effort. So it's a lot of, it's a lot of,

**Chris Gammell:** yeah. All right. Well, thanks for, thanks for stopping by Carl. Well, we'll talk soon. Thank you very much for having me. Bye. Bye. Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Bye. Thank you.
