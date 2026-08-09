---
episode: 598
title: Best way to find a leak
url: https://theamphour.com/598-best-way-to-find-a-leak/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released August 7th, 2022. Episode 598. Best way to find a leak.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV book.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Not much, nerd. Writing code and trying to avoid the chip shortage and, you know, just the usual 2022 kind of thing, you know?

**Dave Jones:** Right, right. I may or may not be writing code soon. It depends on which way my new project goes. So, in fact, it could go both ways. I could be...

**Chris Gammell:** Code free or coding?

**Dave Jones:** Could be Schrodinger's code. I'm both, you know, writing code and not writing code at the same time.

**Chris Gammell:** Lock Dave into a room with a keyboard. And until you open the door, you do not know if he is coding or not coding. He exists in both states.

**Dave Jones:** Exactly. Simultaneously, yes.

**Chris Gammell:** How much are you releasing about what you're going to be working on?

**Dave Jones:** Oh, well, patrons have already seen the video. But after this, I'm going to go reshoot it. Because it was basically... It's a 50-minute video. We can link it in. It'll now go on my second channel. It's a 50-minute video of me reverse engineering a 10-pin connector. Yeah, the side... Well, there weren't actually that many side tangents. It was all kind of, you know, figuring out what's going on here. Because it was a rather unusual circuit. If you don't know, I'm... Did you see that BOM-looking gas detector device?

**Chris Gammell:** I did see it. Yeah, I watched the video. Yeah, that... I was expecting it directly after you... So Dave had this thing that looked like a big boomy boom boom device in his mailbag. And it looked... I mean, it looked like a landmine. Or like a watermine. Yeah, yeah.

**Dave Jones:** It looks like an underwater mine. Yeah.

**Chris Gammell:** Yeah, yeah. Or like... It looks like a 1990s, like Mario underwater mine. Because it's got like that very 90s teal to it, you know? I got it. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. But very intriguing about what it was. And it turned out it was a... It was a sonar device, right? Or something like that? No, no.

**Dave Jones:** It was an ultrasonic gas leak detector. Ultrasonic. That's right. And all those big protrusions coming out that you thought might be like pressure things. So when you press them, it explodes or whatever. But no, no. They were just piezo-ceramic ultrasonic sensors. And yeah, these are like designed to like sit on top of a pole in like a, you know, a gas plant or something, you know, which has all the gas pipes and everything running everywhere, right? All that, you know, or, you know. Any plant that has any sort of pressurized gas, right? Running through pipes. Because if you get a leak in these pipes, it could be an explosive atmosphere and stuff like that, right? So you want to detect whether or not these pipes are leaking. And apparently, if they do, if they get a really small leak in them, you can't hear it, right? It's, hence, it's in the ultrasonic range. So these things are designed to detect from 20 kilohertz up to 100 kilohertz.

**Chris Gammell:** Oh, so it's like the sound of steam escaping. I thought it was actually detecting gas.

**Dave Jones:** No, well, it's the sound of whatever gas is in there escaping.

**Chris Gammell:** Whatever it is, yeah. But it's like microfracture type stuff.

**Dave Jones:** It's a microfracture, you know, a crack in the pipe, a hole, I don't know. Yeah. Something's happened, right? A seal is, you know, leaky or something like that. And yeah, so depending upon the gas pressure, the type of gas, the temperature, the ambient temperature, the size of the hole and the shape of the hole and everything, you can get anything from an audible, you know, kind of sound up to 100 kilohertz ultrasonic, which you can't hear. And often you can't smell these things.

**Chris Gammell:** Dave's actually going to do this right now. Ready? Three, two, one, go. Oh, wow. That was really good. That was a really good impression. Yeah. Yeah.

**Dave Jones:** That was ultrasonic. I'm able to.

**Chris Gammell:** They say Dave has a squeaky voice. They actually, they didn't even know.

**Dave Jones:** It actually goes up to 100 kilohertz. People don't know this, but yeah.

**Chris Gammell:** Dogs hate him. Dogs hate him.

**Dave Jones:** Right. The number one hated podcast by dogs. The number one downloaded podcast by dogs.

**Chris Gammell:** You know, Jake the dog used to bark a lot, actually, during recording. So yeah.

**Dave Jones:** Yeah. That was it.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh boy. Anyway. Yeah. So these things just hang up on poles and they, you know, go back via an RS, RS 485 line to a control center. And, you know, then the alarms go off if they detect this gas leakage sound or whatever. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Very cool. And then, you know, and then, and it's in a big pressurized vessel. Well, it's not pressurized, but it's designed so that if anything short circuits inside, it doesn't ignite anything outside. So it doesn't escape. Flames don't escape. Nothing escapes. Right. So it can just blow up inside, you know, and absolutely nothing happens. You're not going to blow your entire gas plant up or something like that. So yeah, that's why they're designing this huge, thick steel, you know, round bulbous case. And everything. So anyway, and we'll, we'll link that in. It's, it's amazing engineering that goes into the mechanical design of this thing. Circle wise. Anyway. Yeah.

**Chris Gammell:** I had a, when I was at, when I was at ABB, they, they had a couple of products that were like explosion proof, or maybe we were looking at explode, maybe a competitor. I don't remember, but there's like intrinsically safe, like standards. And I never got that far on it, but it was like, they're like, even like color code. I think they're color yellow, I think, but like circuit boards that are intrinsically safe tested to be. And so that like, basically if they go look in a cabin, they're like, okay, this is going to, this board itself is not going to cause any kind of spark that would set off. If there was gas in the air, it's still not going to blow up. That sort of thing.

**Dave Jones:** You know, if something happens to it, it can cause the, you know, it can cause an explosion inside the mine or whatever. Right. Right.

**Chris Gammell:** I think it's like assuming there is presence of gas versus.

**Dave Jones:** Exactly. But in a fail, but in, when you're analyzing failure modes like this, you have to assume worst case, right? So you've got to assume that there is a gas leak and Murphy's going to get you that at the exact same time there's a gas leak, you're going to get a failure inside your product. Right. Yeah. So which will then cause it to ignite. Yeah. Most of the time there's not a gas leak. It's fine. Right. And you can use your $2 cheapy, you know, meter inside of mine. Right. But no, otherwise.

**Chris Gammell:** You know, you know, the best way to find a gas leak is to light a match.

**Dave Jones:** Yeah. Light a match. Exactly. So you can buy like a Fluke 87 meter, right? Standard Fluke 87 meter. But it also comes in an intrinsically safe version, which is exactly the same meter. I do believe. Please correct me in the comments if I'm wrong, but it's the exact same meter, except it is rated intrinsically safe. So it's gone through the whole certification process. So you can't actually use the standard Fluke 87 multimeter in an intrinsically safe environment. You have to buy the marked intrinsically safe version, which I believe is the same, but it's actually silkscreened on the case that says it's intrinsically safe. Right. So the price is about 3x. I'm sure the price is significantly different. Yeah. So I don't know. Maybe they might do greater production test and maybe each unit's individually tested instead of batch tested or something. I don't know. If you do work in the intrinsically safe industry.

**Chris Gammell:** Oh, there's separate certification.

**Dave Jones:** I'm sure there's different levels of intrinsically safe as well. Yeah. Yeah. So anyway, so you can just buy a standard one.

**Chris Gammell:** So you are not building that right now.

**Dave Jones:** I am not building that right now. No, but what I'm doing is taking the LED display on this thing because it looks like a BOMB, right? It just looks like, and it's got this like five digit LED display on it. And I thought, come on, we've got to put a countdown timer on this, right? And then make it, I don't know, tick or something, right? And then if you try and shake it or something like that, then it actually counts down faster or something. Right.

**Chris Gammell:** There's no game where it's like hot potato, but there's actually a digital version of it or something, you know?

**Dave Jones:** I don't know. But this is every 1980s movie, right? This is like the BOMB and it counts down with two seconds left and you snip the red or black wire.

**Chris Gammell:** Yeah, you have to have wires coming out the side too. Yeah, the wire coming out the side. Many, many colors.

**Dave Jones:** Which wire do I cut? I need to know. Tell me.

**Chris Gammell:** Battery wire?

**Dave Jones:** My favorite one. What's that? Oh, what's the one on the plane?

**Chris Gammell:** There are multiples.

**Dave Jones:** Yeah, I know. They're on the plane. Oh God.

**Chris Gammell:** Snakes on a plane?

**Dave Jones:** No, no, it's not snakes on a plane. There's Con Air. It had Steven Seagal, but he lasted five minutes. Spoiler alert before they kill him off. About the right amount of Steven Seagal. It was Kurt Russell. It was Kurt Russell, I think.

**Chris Gammell:** Executive decision.

**Dave Jones:** Executive decision. Thank you. Executive decision. Yeah.

**Chris Gammell:** Chris is coming in clutch with the bad movie titles. Yeah.

**Dave Jones:** Oh God. The nerdy guy. You've got to watch it. Like the nerdy guy. What's the spoiler?

**Chris Gammell:** This is a brand new movie.

**Dave Jones:** Okay. All right.

**Chris Gammell:** Only 35 years old, right?

**Dave Jones:** I think it's 90s or something. Yeah. Oh, was it? Yeah. Executive decision. Maybe early.

**Chris Gammell:** Let me ask you. You're saying something in the 90s can't be 35 years old because I hate to break it to you, buddy.

**Dave Jones:** I know.

**Chris Gammell:** I know.

**Dave Jones:** All right. Anyway, there's the, you know, the nerd has to go on the mission, right? And he gets caught up in it and he's the one who's got to defuse the bomb, you know, and stuff. Yeah. And he does it. We won't tell you how he does it, but it's just, oh, it's cringe and it's so good. It's so good. So, so bad. It's good. So, yep. Yeah. Classic. I love it. Yeah. 96.

**Chris Gammell:** 96.

**Dave Jones:** 96. There you go. Yep. Yep. Yep. All right.

**Chris Gammell:** There's your homework for tonight. So that's, this is the thing you're building now is going to be that display. That's what you're doing.

**Dave Jones:** I'm starting the project and I don't know where it's going to go. So I'm going to release part one, hopefully today, and then we'll see what people want. Do they want me to do it as a microcontroller based solution? Because we've, we've, we've already got the lead board, right? We've already got the board with the five digit lead display. I've, I've, I've reversed engineered the flat flex interface for it. So we know the pin out and the functionality and how it works. So now we can drive this display because it's already, it's already designed to build and it fits in there and it's got a nice little gasket on it and stuff. So it already fits in there nicely. So I don't want to redesign that. So I'm just going to design a board, which plugs into it. Now, of course, there's two ways that you can drive this sort of thing. You can do it using a, a discrete logic solution. So I can like, you know, have a discrete counter, like a five digit counter and then shift, then latch and shift that because it's a shift register based thing. Spoiler alert. Yeah. Right. So you've got to shift in the serial data to drive all the five digits. Right. So I can then latch counters and shift in and do it all in discrete 7.4 series logic, or maybe do it in a PLD or an FPGA or something like that. Or I can do it, of course, in a microcontroller grown. Yeah. Go with the micro.

**Chris Gammell:** Come on, man. Because then you can also get like a, you can get an accelerometer plugged into it. Then you can say when you shake it, it says like. Yeah.

**Dave Jones:** But you can also do the accelerometer with the discrete logic as well. You can get one with a, you know. Oh my God.

**Chris Gammell:** I mean, you sure you can, but you also could expand that project out quite a bit.

**Speaker ?:** Yeah.

**Dave Jones:** But I don't want, like, this is not, you know, this is like just for funsies, right? This isn't for sale, right? This isn't for, you know, people aren't going to be building this thing.

**Chris Gammell:** Whatever you think the right thing is, is the right thing for the project.

**Dave Jones:** Whatever I think, whatever the people think is the right decision.

**Chris Gammell:** No, the people are wrong. I'm sorry.

**Dave Jones:** The people are wrong. Yeah. They are often wrong. Yeah. I have to agree.

**Chris Gammell:** I mean. Yep. Tried that experiment a couple of times, I think. You're right.

**Dave Jones:** Yep. Yep. Yeah. Yeah. It never kind of works.

**Chris Gammell:** And also, we always talk about, you know, like the design by committee. It's tough. Right. That's a tough road. It's a tough road. Yeah. Yeah. Every time I see that with external projects, you know, like, obviously you and I talk about it, but whatever, when I see like, kind of like open source projects, you know, like, it's just always, it really is the best intentions, but it's just, it's so hard to wrangle people, you know, people are, you know, you can divvy up a design maybe, but even still, like you really just got to have one person that's driving all forward.

**Dave Jones:** It always comes down to one person driving the lot. One, one person doing everything. Yeah. Yep. Totally. I don't care how big the project is, you know. Isn't that the Perito distribution thing? It's like, you know, 80, what is it? 80% of the, no, 20% of the people do 80% of the work or something. It's something like that. Yeah.

**Chris Gammell:** It's like Perito being applied to work. Yeah.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** Yep.

**Dave Jones:** So, yeah.

**Chris Gammell:** Yeah. I think, yeah, I think about it like, it's almost more like a power distribution where it's like, you know, you look at like contributors and Wikipedia and similar like that. It's just, you know, there are, there are very, very small numbers overall compared to the, to the number of readers versus even the number of contributors, you know, like that.

**Dave Jones:** Yeah. It's the same thing on forums and stuff like that as well. Yeah. Exactly. Yep. There's, you know, a handful of people who do most of the posting, you know. Yep. So, there you go. So, you reckon microcontroller, huh?

**Chris Gammell:** How about this? I'm not going to tell you what you should do. I'm going to tell you what I would do. And yes, only because it's, I think a little faster iteration, maybe less fun. Totally less fun. Maybe I'm a little more prone, maybe more prone to mistakes than you are. But I think, I think that would be less frustrating for me at this stage of my life.

**Dave Jones:** Yeah. But this is like supposed to be educational. So, yeah, I could do, this is why I could do both, right? I can do, okay, here's how I solve this with the microcontroller. But here is also how I would solve it with discrete logic. And it actually becomes a nice example of how to design using discrete logic as well. It's a, you know, it's a really nice example.

**Chris Gammell:** I do think it's a good, because it's, you know, driving individual pins at special timings and stuff like that. Actually, yeah, it is. That is a good, often people say like, well, what do you even use an FPGA for, you know, or discrete logic for, I guess, by extension, right? Yeah. So, from that perspective, that makes sense.

**Dave Jones:** Yeah. I think that'd be good. Anyway, I'll put that up maybe as a poll on my YouTube thing. But as you say, yeah, people aren't always right. You know, like, often I've done that, and, oh, you know, I've done polls. I've done my yearly surveys, and people say, I want to see this type of video. So, I do this type of video, and nobody watches it. It's like, you know, it's, yeah. Okay, thanks. Yep. But, yeah, it's hit and miss. I don't know. Can't trust the people. Just trust yourself. Yeah.

**Chris Gammell:** All right. I was actually just today, I was working on refactoring some microcontroller code. And I was working with a mentor, and he was helping me through it and stuff like that. It was basically just, like, chopping up an example to kind of refactor it into more files to make it a little bit easier to read and stuff like that. And, you know, pretty simple kind of concept. But I was talking about it. I was like, this is, I wish that I would have been shown this. I feel like this, you know, I've worked with mentors and other people like that on this kind of thing before as well. But I just feel like refactoring and, like, being able to, like, cogently read code and then move it around and shuffle it to different places. Like, that's something that I wish I would have learned a lot sooner in my career because it's, like, such a time saver. And it makes future Chris so much happier at current Chris, you know? Yeah.

**Dave Jones:** Can you, for those who don't know, can you explain code refactoring?

**Chris Gammell:** Well, in this case, what I'm talking about is I'm taking an example and it's, like, a very, very long example. There's, like, probably 20 functions and there's some, there's a secondary. So there's, they're in main.c. And so, like, everything's kind of in main.c for kind of simplicity of this original example that I'm using. Yeah. And then I'm like, well, I want to, like, take this and I want to use this in my project. Like, I want to take this really good example, but I want to make it kind of more testable and more broken out. So then I would only take, like, two functions, two, two, like, C functions that do feature A and I put that into feature A.C. And then I do the next five functions and those are for feature B and I put those into feature B.C, right? And that kind of thing. And then, but actually then getting it to rebuild and making it, like, so that everything's talking to one another because now you have multiple files.

**Dave Jones:** The first step is to separate it into separate files and then re and then make sure it rebuilds, right? Otherwise you're, otherwise you're screwed from the get go. You've got to make sure it still works.

**Chris Gammell:** Yeah. Right. And you think about, like, how data hiding works in a lot of, like, when you have separate files and sometimes you have, you know, if you think of in C++ way, usually there's public private, but in C it's more like, is it a global variable or, you know, is it local? Is it a local only to the, uh, the file that you're in?

**Dave Jones:** Ah, just make everything global. She'll be right. Sure. Yeah. It's easier.

**Chris Gammell:** I did. I did a channel that, that perspective today. Right. Maybe it was traded for it.

**Dave Jones:** Yeah. It's just easier sometimes, you know, if you just, you know, if you just want to get the job done.

**Chris Gammell:** Maybe not the best coding practice as I've known and also re heard today, but, uh, you know, sometimes it helps to get stuff compiling, but it's been really great to, you know, I always say like, so I'm, I'm in my late thirties. I'm working with a mentor still. Like it's, it's important, you know, like, I'm not good at code still. And finding people that are is very important to ask for some of their time and, and get some help. And if you can do that, you're a very lucky person. I think, I think I'm a very lucky person.

**Dave Jones:** Excellent.

**Chris Gammell:** So Dave, if you do write a micro and you need some help, find someone else. Cause I'm not the person for it.

**Dave Jones:** Excellent. No, I'm not. I'm good. Plain vanilla C global variables everywhere. She'll be right, mate. No worries. Yeah, sure.

**Chris Gammell:** Yep. Yep. What would you, if you do go micro, what is your, uh, you're going to go pick? Cause you're. Well, I don't know.

**Dave Jones:** Once again, it's up. It's up to the peeps. Like I don't want to do the STM 32 thing. That's like grown, you know, like you can't get them and everyone's doing the stupid arm thing. So, you know, yeah, I'd be tempted to go.

**Chris Gammell:** Interestingly, you can't get pick either. Really? I think.

**Dave Jones:** Oh yeah.

**Chris Gammell:** Actually you should be doing that. We talked about the raspberry pie 2040 RP 24.

**Dave Jones:** Oh yes. Yeah. Right. Yes. Yes. That could be. I've still got that open in one of my tabs, actually thinking about a video on that.

**Chris Gammell:** So there, there's an interesting thing. That would actually be kind of an interesting because it's the combination as well with like the PIO doing the, uh, PIO, the.

**Dave Jones:** Oh, I could try to do some, I could do shifting in the hardware IO.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Perfect example. Yes. Thanks for reminding me. Yeah. That's.

**Chris Gammell:** I forgot about that too. Yeah. Yeah. Yeah.

**Dave Jones:** I deliberately go still got to open because I'm a tab person, right? I just keep shit open. Totally. Totally. In tabs, right. To actually remind me. And the thing is occasionally I'll like lose all my tabs because I don't know, the browser reset itself or crapped itself or something. And then I'll like, that's like a refresh of like all of my thinking.

**Chris Gammell:** Like it's, you know, it's like, it's more like a, uh, like a email bankruptcy. Yeah. Right. Yeah. Yeah.

**Dave Jones:** I declare bankruptcy. So here it is. Yeah. I still got the tab open for the Raspberry Pi, uh, Pico examples for the PWM PIO for doing the assembly for doing the shifting of the things. Yeah. We, we talked about that a couple of, I think we, how many weeks ago?

**Chris Gammell:** I think we talked about a little bit on the show, but then you and I talked about a lot more after that. We cut off. Okay. I think, I think so. Yeah.

**Dave Jones:** And that's why I kept the tab open. Cause I was kind of excited by that. And I thought, oh yeah, I might be able to do a video on that. So I just kept it open as a, as a reminder for me, but yeah, yeah, you're right. That, that could be the, that could be the example there.

**Chris Gammell:** Plus then you can get a W and you can make it IOT enabled Dave.

**Dave Jones:** No, no, I'm not. No, I refuse.

**Chris Gammell:** Walked right into it, folks.

**Dave Jones:** I refuse to have an internet enabled bomb. No. No, it's just not going to happen. No, no. On principle. On principle. On principle.

**Chris Gammell:** He's a man of principles. Anyways, I did want to bring that up though. There is a teardown of the Pico W, which we talked about two weeks ago, I think. But now there's like a, an electron update, which does some of the teardowns and die shots.

**Dave Jones:** How do you do a teardown? Oh, okay. It's a die shot. Okay. Of the actual module. Yeah. Right. Okay.

**Chris Gammell:** Cool. I mean, like, you know, like they're pointing out different things here, you know, it doesn't really. It doesn't impact me too much, you know? Like, it's like, oh, look. Well, no.

**Dave Jones:** It's just out of interest, you know? It's not useful information. I mean, it's not, you know, no. It's like, yeah. It's just go, oh, look at the nice die. Excellent. You know? But yeah, no, it's not actually useful technical information to store away in your brain space. So yeah, nah. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm. Can we talk about dodgy design? Because when I, spoiler alert, in, in this, in this reverse engineering, this lead, lead display, you would think, you know, this is like in a controlled, you know, this is like in this atmosphere where you don't want things to be overloaded and, you know, like, anyway. Okay.

**Chris Gammell:** So just so we're clear, this isn't a third party. This is the one that's actually built in currently.

**Dave Jones:** This is the one that's built in to the Banshee brand gas, ultrasonic gas leak detector. Right. So I'm reverse engineering this thing. It's got five, seven segment displays. Right. And then it's got a 74HC161 shift, shift register drivers. Okay. Fine. You know, shift in the data and, you know, Bob's your uncle. Right. And they're cascaded together. I wouldn't have done it that way. Anyway, they're all cascaded together. And then there's no lead dropper resistors. Right. So I thought, so I thought what's going on here. Right. There's that, you know, normally if you, if you're designing a seven segment display properly, you have individual lead dropper resistors on each segment. So, you know, so you can calculate exactly how much current is going to flow through each segment. Right.

**Chris Gammell:** So you probably broaden that out to when you're designing anything with LEDs and you're driving with voltage, you probably have a resistor somewhere.

**Dave Jones:** You have a resistor dropper. You're supposed to have a resistor dropper. Right. That is, that is correct design process. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Sure. Right. Sure. So anyway, this doesn't have any lead droppers. Right. So I was, I was reverse engineering the circuit and they had this big 47 ohm resistor on there and I like a big, big through hole jobbing. And I thought, aha, they're, they're using that as one big dropper resistor for the whole lot. And of course that's bad practice. Right. Because then you're going to get different brightness on your display, depending on how many segments you turn on. Right. So basically if you turn on all the segments, then, you know, you're going to get like the, the current, the maximum amount of current has to be shared. So it's going to dim. So all your segments are going to be dim. Whereas if you have just one segment turned on or, you know, just one single digit or something, then, then there's going to be super bright. Right. Because it's only got a 47 ohm dropper in there. Right. So anyway, but, but I was wrong about that. It doesn't even have a freaking dropper resistor. So they're relying on the RDS on of the output MOSFET, the high side output MOSFETs of the 74HC164. Right. Which I did in the video. I actually threw the data sheet. You can actually calculate that with the VOH drop. Right. So based, based on how much the VOH, it tells you that in the data sheet, how much does the VO high drop voltage drop based on X amount of output current. And then you can calculate roughly what the output impedance in quote marks is, right? The output resistance is. And so they're using that. I think it was 40 ohms or something. I don't know. But yeah.

**Chris Gammell:** And so basically it's just that they're not driving when they drive it high, they're not driving it high enough, hard enough to really get a low resistance. And they're just relying on that. Is that it?

**Dave Jones:** Well, no, the, the 74161 is trying to drive it as hard as it can. Right. Because, because it's a digital output. It's either one or a zero. Right. But the, but the, but the inherent nature of the 74 HC logic drive means that they're only wimpy output transistors. Right. These aren't designed for high current. Yeah. That's what I, that's what I meant. Yeah. The maximum output current is like 20 milliamps per pin. Right. And, and, and here's a trap for young players. Right. Go look at any 74 series digital logic, anything. Right. Or it's 4,000 series CMOS or whatever. And they will have, they'll, they'll say, okay, you can do 20 milliamps per pin, per IO pin. So you can go, oh, great. I can drive my leads at 20 milliamps per pin. No, you can't. You can't drive your eight output leads. Right. At, at 20 milliamps each. Because if you look at the maximum specification for the chip, the power pins can only support 50 milliamps maximum. So, oops. So you've only got 50 milliamps total for the whole chip. So you can't drive each individual IO at 20. So, yeah.

**Chris Gammell:** But actually that benefits in this scenario too, right? As long as you're. Well, yeah.

**Dave Jones:** Then you're kind of. Yeah. Anyway. So they're using that. Averaging overall eight. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** So anyway, the, the, the common cathode, the common cathode connection on the lead displays, all of them, five of them in parallel, right? All go, all goes to one pin on the connector, which then on the other board I checked out actually goes into an NPN transistor down to ground. So there is, so they're using that as a blanking, right? So the, so that using that, you can actually blank the entire display, but still there is no current limiting. So you could like bias the transistor, like partly on. Right. So it kind of like, you can control it that way, but you still got the brightness problem. And then, oh, it's just, it's, it's, it's bad design. And I'm just surprised to see it in here. And there was just no reason to do this. Right. There was room on the board to put individual, uh, dropper resistance. There was no need to do this. Yeah. Right. So, yeah.

**Chris Gammell:** Just a quick clarification. You said the 74HC161, is that right?

**Dave Jones:** No, the one, no, the 164.

**Chris Gammell:** 164. Okay.

**Dave Jones:** 164. Yep. 74HC164. Serial shift register. Standard jelly bean stuff.

**Chris Gammell:** 161 is a counter. Yes.

**Dave Jones:** 161 is a asynchronous counter. Yeah. Isn't it?

**Chris Gammell:** Yep.

**Dave Jones:** Or am I wrong? Is it synchronous?

**Chris Gammell:** Oh, I don't know. Hang on.

**Dave Jones:** Asynchronous. No, hang on. Hang on. No, synchronous. Yes. Synchronous. Yep.

**Chris Gammell:** I'm really only, yeah. I mean, I'm, I use shift register sometimes. I use 595s. Yep. But like.

**Dave Jones:** Yeah, yeah. 595s is a nice go-to one.

**Chris Gammell:** I'm not using much, uh, I guess there's, what's the double zero? Is it NANDS? Or what is that?

**Dave Jones:** NANDS? Yep.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. And so like once in a while that, but like, man. Right. Not much, not much 7-4 series logic. No, I've just never had it. You know, I was never really, you know, I was just on the trailing edge of that, you know?

**Dave Jones:** Yeah. Right. No, see, see for me, I like memorized all these as a kid, right? Yeah, exactly. You knew data books. Because you had the data books. You had the thousand page TIT. I've still got it, right? The thousand page TITL data book, right? So I, you know, you would remember, you'd memorize all of these chips. And I can remember going for a job interview once. I don't know if I've ever, ever told this story, but, uh, I was going for a job interview at a company that did, they had this idea for like video at the time. And this was pretty novel, right? Uh, video intercoms, like sort of not really because the internet wasn't around then, but

**Chris Gammell:** video, like for like wired, like wired video. Yeah. Yeah. So like coax cables. Each door. Yeah.

**Dave Jones:** Something like that. Anyway. So they had these video things and the guy thought he was going to be, he took quote, I'm going to be richer than Bill Gates. And I went, yeah. Okay. Anyway. So I was offered the job based on my knowledge of 7, 4, 8, C logic. All of his questions were, can you explain what a 7, 4, 8, C, 7, 4, 8, C, uh, 2, 4, 4 does and et cetera. And he rattled off all these numbers and he was stunned that I knew what they were. Right.

**Chris Gammell:** And he was, after a certain time, it was just like, he's just, I got to try and test this guy.

**Dave Jones:** But he was absolutely stunned that, that I actually had chip level knowledge. You know? And, and I knew what these numbers were off the top of my head.

**Chris Gammell:** Was, was he calling them out by memory as well? So like, did he have the same knowledge in his? Oh yeah.

**Dave Jones:** Yeah. Yeah. Yeah. So he was, yeah, that was, well, I don't know if he had the same in-depth.

**Chris Gammell:** He was the hardware guy. Oh, got it. So.

**Dave Jones:** Yeah. Yeah. Well, he was like the company founder and yeah, he was a hardware guy. Yeah. Like it was only a small, like family company. It was only like three or four people working there or something, you know?

**Chris Gammell:** Wait, you mean he didn't get richer than Bill Gates?

**Dave Jones:** No, no, he didn't get richer than Bill Gates. It didn't pan out. So I, I, I actually followed them a few years and it was anyway. So yeah, I was offered a job based on the knowledge of my 7.8, 7.4 logic. It was hilarious. He was stunned. And I guess nobody, nobody had actually, you know, passed his, uh, questions before they go, Oh, I have to look it up, you know? And now I just rattled it off and gave the pros and cons of those chips.

**Chris Gammell:** Which to be fair is a legit answer. Just come on.

**Dave Jones:** Oh yeah. No, totally. Right. Yeah. Yeah. Yep. So yeah. But he was just so used to getting that answer, I guess that he was just, you know, I can't remember exactly what he said. I think I discussed it with like, cause I knew like, like I could see the shock in his face and I was like, wow. You know, like stunned. And then he did more numbers and I rattled them off as well. And, you know, it was just, I think we might've talked about, I don't know, it was so long ago. Can't actually remember. But anyway, there you go. Jeez, that was a tangent.

**Chris Gammell:** Humble brag tangent.

**Dave Jones:** Anyway, for those playing along at home, I didn't take the job. It was like, it was because the, the, the vibe of, oh, and, and also, also, also, also he mentioned, oh, at the end of the interview, oh, do you mind if we, if you work in an environment where we were talking about religion all the time? Oh my. And I kind of said, you know, and yeah, that, you know, the alarm bells start going off. So I think they are a fundamentalist, you know? Wow. Yeah. Yeah. So he actually said that.

**Chris Gammell:** I mean, at least he asked.

**Dave Jones:** Oh yeah, no, he, he, yeah. He told me that that's what they'd be talking about all day is. Yeah. I'd be talking about, talking about religion. I, I might've, I might've taken it maybe like, cause like technically it sounded really interesting, but you know, I didn't take like, it was on the, oh, and, and he offered to, for me to move in with his brother or something like, cause I'm going, oh, you know, it's far. It's on the, you know, like I actually turned down the job and my excuse was, oh no, it's too far. Like it was on the other side of Sydney and it was like, there'd be too much travel and everything. Then you offered, you can, you can, my brother, you can, you can move in with him and he's just down the road, you know? And it was like, and I'm going, nah, nah, nah.

**Chris Gammell:** Okay.

**Dave Jones:** So, yep. All right. Yep. There were too many, too many alarm bells there.

**Chris Gammell:** Too much, too many question marks.

**Dave Jones:** Anyway, where was I?

**Chris Gammell:** Oh my gosh.

**Dave Jones:** I was talking about, yes, overloading these, overloading these damn things. So it was like, so, so this has a, actually, actually a triple, you know, this has like a double whammy problem. At least it could be a triple Lindy. I don't know. For those who've watched Rodney, Rodney Dangerfield. No. Triple Lindy. No. This is way over your.

**Chris Gammell:** No. I mean, I know some of like his standup stuff.

**Dave Jones:** Movie recommendation. Back to school. I believe it's called back to school. And he does the triple Lindy.

**Chris Gammell:** I've seen back to school. Oh, that's the, because he's a diver. That's right.

**Dave Jones:** He's a diver. The triple Lindy. It's like the worst. You have seen it. Oh my God. You have seen it.

**Speaker ?:** I have seen it.

**Dave Jones:** Ah, the triple Lindy. Yes.

**Chris Gammell:** Because he's a real, he decides to go back to school with his son. And he's like the, the street smart real estate developer. Yeah. Yeah. It's basically, he's basically the exact same character as he is in a Caddyshack. And I'm there for it.

**Dave Jones:** It's great. It's just, it's just hilarious.

**Chris Gammell:** A little more humble in back to school. Yeah. Yeah.

**Dave Jones:** It's great. Anyway, the triple Lindy. So yeah. Yeah. So we have the problem of not having individual droppers and relying on the RDS on of the transistors. Right. Which is, you know, problem number one. And then problem number two is that because the 74HC164 is not designed to be cascaded, right. It doesn't have a cascade output to go onto the next chip. So you have to tap off the Q8 output. Right. So you've got to tap off the last digital output. But because you're using that last digital output to drive hard the, the, uh, LED display, then is output voltage is going to drop so low that it could actually not then have a high enough logic level to drive the next chip. So what you've got to do, what you probably have to do, like if you drove them at a low enough current level, you could probably get away with it maybe, but it might change based on how many segments you've got turned on. That's the, that's the crazy thing. That's the mind blowing thing. And what's mind blowingly bad about this actual design. This is what I'm going to mention in the video is that now, well, they, they, they have to use that output, which is driving the lead hard to, to then send the data into the next chip. Right. So if you're, so what you have to do is blank the display when you're shifting the data. Well, you would, you, you would do that anyway, because you wouldn't want to see them because they're a non latch shift register. So you wouldn't want to see, you know, if you left these, if you didn't blank the display while you're shifting the data in, you would actually see the data shift across the display and it'd flicker and, you know, do all sorts of weird. Yeah. Right. Yeah. So you'd have to do that really quick if you didn't want to see the flicker, but technically you'd see it. So you have to blank it, not only so you don't see it, but also so that you don't screw up the bloody logic levels when you're shifting. This is like, oh my God, how bad can this design?

**Chris Gammell:** So it's safe to say you're not going to follow the same analog pattern on this one.

**Dave Jones:** Well, I kind of have to, because I'm, I'm reusing the board. I'm, I'm interfacing with this board. That's why I'm talking about it. Cause I, my, my circuit that drives this has to take all this into account.

**Chris Gammell:** Oh wait. So the 7, 4 HC 164s are built onto the, they're built onto the board. They're built onto the board, which I'm reusing. You basically only have like a serial line in.

**Dave Jones:** I just have a serial line in and I have access to the common, you know, the, the common collector pin and stuff like that. But that's it. Right. Yeah. Yeah. So my circuitry, so any design I do has to take this into account. Right. So this, that's why this is such an interesting thing. Right. If, if I was, if I was redesigning from scratch, I wouldn't.

**Chris Gammell:** Yeah. That's what I mean is like, it would be, make sense to like try and replicate the size of the, like even making your own led segments and stuff like that.

**Dave Jones:** I could, but the challenge is to reuse the existing board. I could simply redesign the board and put it and put in my own displays and, you know, but that's kind of like, you know, that's kind of like a copy. Yeah. Yeah. Yeah. I kind of like reusing the, the existing thing has got the foam cut out in there. It's all, you know, but I could, I could reuse it. I could redesign.

**Chris Gammell:** Yeah. I mean, I meant like form fit function type of replacement, you know, so like something that looks as close as possible.

**Dave Jones:** That looks as close as possible. But where's the challenge in that?

**Chris Gammell:** Like, I don't know. I, I kind of like the idea of reusing. I mean, there is some challenge, but it's mostly like sourcing and like, you know, matching behavior and stuff like that. And usually when I've found in my past, when I had to go and replace something like that, the real thing is usually then user perception. So then it's like, oh, well I ordered this bomb ass looking thing last week. And then the one that came this week, because apparently I'm ordering multiples, it looks different. What happened? And then your boss comes, you need to say, you need to make the brand new shiny thing that you sort of spent all the time sourcing. You need to dumb it down and make it look worse. So it looks like the old thing.

**Dave Jones:** Got it.

**Chris Gammell:** I don't blame the boss, but yeah, you know, it's just something that, that happens, you know, part of your life now. So there was challenges. You're right. I think, I think it's a different, different type of challenge and probably not as tough.

**Dave Jones:** So you're going to recommend that I use a microcontroller and I redesign the whole board.

**Chris Gammell:** What if you just threw the whole thing out and started from scratch and build your own bomb looking thing?

**Dave Jones:** Right. Oh yeah. Why even reuse the case? Yeah. Why even? Yeah, exactly. Yeah.

**Chris Gammell:** Couldn't you 3D model your own thing? Yeah. It looks like a crazy ass like mine.

**Dave Jones:** Oh God.

**Chris Gammell:** I mean, I get what you're saying. Yeah. It makes sense. It makes sense.

**Dave Jones:** Yeah. Anyway, that was, and, and, and that's why it was a 50 minute long video. Cause I'm, I'm, I'm kind of like reverse engineering this thing going. What's going on?

**Chris Gammell:** Only reason why Dave.

**Dave Jones:** What? What's the other reason is because I'd like to talk about. Your name is Dave Jones.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. Anyway.

**Chris Gammell:** You know, side of waffle. Right. With most orders.

**Dave Jones:** Yeah. But I go through the video, right? I do a two pass edit. I go through it a second time and I go, can I take out this information? And I go, no, somebody might find it useful.

**Chris Gammell:** Ah, two pass edit. Yeah. Yeah. Editing. Yeah.

**Dave Jones:** Boy, I, I just can't do it. I just can't throw out potentially useful information to someone.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** That's my problem. Anyway. Yeah. Anyway. So I'm going to go after this, I'm going to go actually reshoot that with a simpler version. So the main channel, you just see, here's the reverse engineered circuit and here's what I found rather than the whole process of doing it. So if you want to see the whole process, it'll be on the second channel's 50 minute video. Not knock yourself out. You know? Yeah. So, yeah. Yeah. Because I don't think it, because there's two types of people who want to watch this video. Right. I think there's the one who want to see the reverse engineering process. Right. So those are the ones who want to watch the whole 50 minute version. Right. And then there's others who just want to know, I just want to go along on the journey of this project. Please just give me the summary of what you found and then we'll make a decision where to go on part two and part three, et cetera, which direction to take it. So there's, you know, I've got to cater for two audiences here, I think. So that's why I've decided to split the video. Yep. Makes sense. Yeah. Yep. All right. Enough of that.

**Chris Gammell:** What else do you want to talk about? We have many other news items on the list. Probably most interesting to you personally is that Google begins publicly testing its AR glasses.

**Dave Jones:** I have not seen any info on these. What do they look like? What do they, what application do they have?

**Chris Gammell:** I think the main thing is, Dave, Google Glass is back and I'm vindicated. Right.

**Dave Jones:** Right. Okay. So it's, it's, it's, so it's an upgrade to Google Glass essentially.

**Chris Gammell:** No, it's a new thing. It's a new thing, but I really just want to make a Google Glass joke and that's all I have to say.

**Dave Jones:** Oh, okay. Yep.

**Chris Gammell:** Cause you are the proud owner.

**Dave Jones:** I still am. Yeah.

**Chris Gammell:** I'm staring at the case right now, actually. Yeah. All right. Okay. I turned them on a couple of days ago. Oh, okay. I still have photos from the last time I turned them on and took a photo. So I'll probably do that about every three years.

**Dave Jones:** It'll be like a time capsule on my face. So why did you stop using it? It, there, there was just no, there was no app. Oh, software support. It was what?

**Chris Gammell:** Yeah. Software support fell off.

**Dave Jones:** Right. Okay. Right.

**Chris Gammell:** I did open it up when I opened it up and tried it out. I forgot, I forgot when I, I forgot how it worked. I forgot what was on there or whatever. I did open it up and I was like, what's on this thing? What's on this thing? And like, it doesn't have a connection to the, there's no app anymore. I have a new phone. It doesn't connect to the old phone, whatever. And there's, so there's no way for it to get to the internet. So now it's like a standalone thing. So now it's a device that sits in your face. And I went to the standalone, you know, mind you standalone app for translation. And I turned on the overlay and I said, show me Portuguese. And so I looked at something in English and on, on my face, it did the overlay in Portuguese. I was like, that's not bad. You know, this is technology from 2014. That's eight years ago. That is doing this without a connection to the internet. That is definitely a killer app.

**Dave Jones:** Like if you were, like you wouldn't use it every day, but if you're going overseas or something, you know, like, yeah, that's a killer app. Yeah.

**Chris Gammell:** Yeah. That's. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Nobody needs it really, but yeah.

**Dave Jones:** It's a, so I assume this new one, like, I can't even get, like, they don't even have a real photo of it in this article here. No, this is, this is all. This is just a stock image.

**Chris Gammell:** It's just like, I think, I think what it is, is like, you know, sci-fi never doesn't have, you know, like a display in your face. You know, I'm reading a book right now called a cellarando and it's just like all about that sort of thing in the early chapters. And like, you know, it's always there in, it's always there. It's just always there. And sci-fi can't get away from this concept. And I don't think any big tech company will never stop. I don't think Google will ever stop trying this and Apple's working on it. I'm sure. And, you know, snap has it and whatever. And it's, it's a really hard problem to solve. Not least of all, because you're, you know, it's a screen that's, you know, five centimeters away from your eyeball. Like, you know, it's not like, it's not, it's not an easy focal distance either. And so like, there's a lot of hard problems to solve. Yep. So yeah. Uh, you know, maybe someday, who knows? Uh, but it is also a great way to walk into track oncoming traffic by accident when you're reading text messages.

**Dave Jones:** But that's right. Right. Okay. Cause you're focusing near field and your, and, and your brain's focusing as well. Yeah.

**Chris Gammell:** Your brain is just, it's just a distraction machine. You know, like, like a phone is, but it's just close to your eyeball.

**Dave Jones:** Yep.

**Chris Gammell:** So.

**Dave Jones:** Yeah.

**Chris Gammell:** I really have nothing else to say about this other than I wanted to make a joke about it.

**Dave Jones:** Will that create a greater problem? Right. Because we, we, we already have the huge problem of people on their phones. Right. I mean, they've even gone to the point of having some cities installed traffic lights on the ground because people are just constantly looking down.

**Chris Gammell:** Oh, I haven't seen that.

**Dave Jones:** Yeah. I'm sure if you Google that, it's, it's, it's somewhere. Right. I'm sure if you Google it on your Google. Yeah. Anyway. You're all week.

**Chris Gammell:** Dutch town now installs traffic lights on the ground for texting pedestrians.

**Dave Jones:** Yeah. And I don't think it's a joke. I think it's, I think it's totally, I think it's totally legit. Right. Everyone's just looking down. Right.

**Chris Gammell:** I mean, this isn't disingenuous though, because everybody knows Dutch people don't walk. They all ride bikes.

**Dave Jones:** Right. Okay. Yeah. Yeah. Got it. Boy. That's kind of cool though. Yeah. Yeah. So it's just not. So is this going to create a greater, a greater distraction because it's in your face? Like at least the phone, you've got to take it out of your pocket. You've got to switch it on, do the swipey bloody thing or whatever you do to unlock your stupid shoe phone. And then you've got to, you know, scroll to the app and then you've got, right. Right. But if it's just pumped, if it's just pumped right in your eyeballs all the time as you're walking around, like, like sure, you can have them up on your head, right. You can actually move them up and it's out, but, but it's like, it is vastly easier. Right.

**Chris Gammell:** It's getting worked up.

**Dave Jones:** It's vastly easier to flip the glasses down. I'm doing it right now. I actually have my glasses up on my forehead and I flip them down. It, it, it takes less than a second. Right. Whereas to open my, get my phone and opened up takes bloody, I don't know, two hours or something to start the damn thing up. So is this going to lead to a greater distraction of people just constantly distracted all the time? I can picture people in the fricking gym class. It already pisses me off when I go to a gym class and every single person is just sitting there looking at the shoe phone. I'm the only one who turns up without a bloody phone. Right.

**Chris Gammell:** We've, we've heard a couple of times here, Dave. We've already heard, we've heard this.

**Dave Jones:** Imagine if they had the glasses, they'd be wearing the fricking glasses.

**Chris Gammell:** I mean, this is actually, I, I, you know, like I'm on a lot of zoom, zoom calls and other things. And like, you know, when someone's like staring off into space, cause they're like on a different screen writing text, like it's, it's going to be that it'll be that. So.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. I'm not saying it's a positive thing. I would try to get back to the point. I was just trying to make a joke about Google last week and move on. Let's find another story to move to. What else would you like to talk about, David?

**Dave Jones:** Oh, we can talk about DigiKey. Cause we were talking about that before the show. I really liked that. We, we, we haven't, you've, you've watched it, but I haven't watched it all. I've just scrolled. I watched some of it. Some of it. Yeah. Yeah. It's a, it is.

**Chris Gammell:** Go ahead.

**Dave Jones:** Yeah. It's an RV SWAT channel and they're nomads or whatever. Right. That traveled around the country in an RV.

**Chris Gammell:** Yeah. So they call this work camping, work camping, which is all one word apparently, but it's like camping and work.

**Dave Jones:** Yeah. Work camping and working. So yeah. So they just go from town to town and they find a job for a month and they stay there for a month and then they move to the next town, I guess. And they turned up in Feith, Iver Falls and they went to work at DigiKey. And this is the video of them. Both of them. Is it? Yeah. Both of them working at, working at DigiKey. And it's good insight into the DigiKey factory.

**Chris Gammell:** Yeah. That's why, that's why my friend sent it to me because it's like, you get a really cool look at like, you know, what it's like just picking parts and, you know, standing on the line and figuring out how to put everything together. And, you know, some people are there permanently. Some people are, you know, temporary labor like this. And yeah, it's.

**Dave Jones:** And it isn't as automated as you think. Like it's, you know. That's right. Yeah. Like it's, there's a, like, it's mostly manual, you know, he's walking up and down. There's little cardboard trays on the shelves, like in some old, you know, a surplus warehouse or whatever, you know, these old cardboard trays.

**Chris Gammell:** The parts room at my old jobs. Yeah. Yeah. Right. It was pretty similar. Yeah.

**Dave Jones:** What was the one that closed down recently? And Jerry, Jerry Ellsworth scored a whole bunch of stuff from there. What was the one in, in California somewhere that closed down? The surplus place? Yeah.

**Chris Gammell:** It was one of the last ones. Yeah. Yeah. It was like practically the last one. I don't remember the name. I didn't know that I didn't know by name because I think Jeff Kaiser also posted about it.

**Dave Jones:** Yep. All right. And yeah. And it's just got these old, rusty steel shelves. They're down to very, very few. Yeah. There's very few in the Bay Area specifically. But this is what it looks like. I'm staring at it right now. Inside DigiCare is very similar. It's got like these steel shelves with these little cardboard trays with a barcode on the front, like, and you just pull them out and it looks messy as, right. And it's just, and they just walk down this aisle, this narrow aisle and they find the one that they want and they pull it out and they get the parts and they push it back in. And then, you know, yeah, really is something.

**Chris Gammell:** Yeah. I can't imagine. Do you ever have to do like inventory counts?

**Dave Jones:** Yes. Yep.

**Chris Gammell:** Yeah. So like, if you don't know, like what you're doing basically is like, you think about all of these dusty trays, like Dave's talking about, right?

**Dave Jones:** Yeah.

**Chris Gammell:** The system thinks that there are 455 individual 7, 4, HC, 1, 4, 6s or 1, 1, 1, 1, 6, 4s. Yes. Nice. 1, 6, 4s. Back there. Yeah. And they think that there's that many, there's 455 of those in that tray and they're working down, working down, working down. You know, like the people are pulling, they pull 10, they pull 150, they pull, you know, whatever it is. And they think they get to the end. And it turns out actually they only had 300 in the bin. And that, that's why you get the notices is, oops, we, we actually don't have this part. I'm sorry about that.

**Dave Jones:** Yep.

**Chris Gammell:** But the bad thing is that, you know, every once in a while you have to go back through and actually count everything that's in each and every container and then update the numbers because of wasted spillage, whatever happened or a lot, you know, something that fell behind.

**Dave Jones:** Oh, just imagine what would be on the floor under those shelves. Just imagine how many, how many parts. Gold, Jerry, gold. Just sweep them up and you can sell them by the bag. Oh God. Digi droppings. Digi droppings. They're officially called Digi droppings. Yes. Oh, this is great. I so want to visit the DigiKey warehouse. It's, it's on my bucket list. You know, that's kind of a sad bucket list, is it not? But you know, oh boy. Yeah.

**Chris Gammell:** Well, you're a simple man with simple taste, Dave. And that's all it takes.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. So it's cool to see you kind of, it's, I was surprised actually by the, just the, you know, like the, I get the bags, I get the labels, right. It's just the label printer. Like, I don't know what I thought it was going to be. It's like, but that's also how they like, they figure out what's kind of up next and stuff like that. And I don't know. Yeah. It all makes a lot of sense when you look at it, but it's like, oh, oh yeah. Okay. All right. Cool. Yeah.

**Dave Jones:** And they're not wearing wireless, uh, anti-static wrist straps.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. I didn't, I understand too.

**Dave Jones:** Unlike LCSC.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** You don't remember that, do you?

**Chris Gammell:** I don't know.

**Dave Jones:** I actually busted them. They actually put out some promo shots of their warehouse and people were using those anti-static wrist and those wireless anti-static wristbands.

**Chris Gammell:** Oh, the wireless ones. Oh, got it.

**Dave Jones:** Yeah. So I sent them an email going, hey, I linked them to my debunking video of the wireless anti-static wrist strap. And they went, oh, that's embarrassing. Sorry. We'll fix that. And they actually announced that they're, yep, that they're fixing that. So if you get your parts from LCSC, you're welcome.

**Chris Gammell:** I do. I do. Right. I'm wherever I can these days.

**Dave Jones:** Oh boy. Good stuff. Yep. And you might've seen that I, the JCAR warehouse, I did the JCAR warehouse video there. I did see that. They're relocating. They're actually, their new warehouse, which I have an invite to, actually has robot pick and place. So I'm curious to see what that's like. And the good news is, for those playing along at home, they have not laid off any full-time staff. So all the full-time staff will still be there. Searches for growth. Yeah. Yeah. Yeah. So yeah, the new warehouse is robot pick and place. And they had-

**Chris Gammell:** It's usually how automation goes. It's usually not because you're just wiping out the workers. It's because you're augmenting them or you're growing so much. Or augmenting them or something like that. Yeah. I mean, it's still really tough. I don't know about Australia, but it's still really tough to hire people. Yeah. Yeah. No.

**Dave Jones:** Same here. Yeah. Yep. And the, so I don't know. I, I, I, like, I'm, I'm kind of picturing. I don't know if I'm going to be wrong, but I'm picturing those, you know, robots that like crawl up the sides of the rack in and move across, you know, X, Y, and then pick and get the box and then move it back out. I'm kind of picturing one of those, but I don't know what their robot, all they said is it's a new robotic pick and place warehouse. And some, some goods were too big to go into this new warehouse. And that's why they're actually clearing those out. And they have another warehouse just for the big bulky stuff, which you can't do the pick and place on. So yeah.

**Chris Gammell:** Yeah. I mean, I've seen the Amazon, uh, what do they buy? They bought kind of so many years ago now, but basically that's like where they bring the entire shelf over to an actual.

**Dave Jones:** Yes. Yes. The entire shelf moves, right? The, the robot goes up, picks up the entire shelf and moves the shelf to you. So I don't know.

**Chris Gammell:** And so what you're, what the new, you're basically doing is you're just cutting down on that, walking up the aisle. Like you're cutting down on the time. Yes. Required to walk. So you're not actually. And some more flexibility of storage and stuff like that, but you cut down on. Is like the, if you look at the DigiKey warehouse, those shelves are humongously tall because then you get extra storage for like long-term storage. You know, it's out of reach of any person, but it's, you still get long-term storage up there. So you lose that with a kind of a more mobile, like robot moving the shelves kind of thing. Then I think about like, there's like the.

**Dave Jones:** Well, yeah. Cause there's two ways to do it. You can bring the shelf to you, or you can bring the individual box to you. Or an advanced thing would be bringing an individual part, but then you've got to have like, it'd be like one of those. You know, we, we've talked about that food distribution warehouse that has those XY robots on the roof. And then it, and yeah. And then, then it can drop individual food items into the box. And then the box comes to you and it's already sorted with all the parts. I don't think it's going to be that. I'm not really expecting that. Yeah.

**Chris Gammell:** That's a really complex thing. Yeah. I don't know. It depends how much they're investing too. Like I've also seen, there's a assistant robot that basically like, again, in the room, it's almost more like the digi key case where it's going up the aisle and it's, it's got an arm on it, but it's, it's able to move up and down aisles. And then it, it picks directly off a shelf. Yep. And depending on how the shelves are aligned and stuff like that, but it's tough. It's a tough problem.

**Dave Jones:** Like, you know, every, every product's a different shape and size and weight and everything. So, you know, it's like, it's very difficult. So unless you have everything in like preset, like standardized boxes or bins, it makes the robot pick and place concept very difficult. So yeah. Anyway, I, I, I have been invited for a tour of that. So we might see something interesting there. So stay tuned for that. Yeah. Of course I've tried to get into the Amazon one, but you cannot get into Amazon. That's just, no, no, they're incredible.

**Chris Gammell:** You have to go and work there.

**Dave Jones:** Yeah. You have to go work there or you have to be, you know, you know, one of the major news networks and then they've got to vet all the footage and then, you know, like, yeah, yeah. No, I've, I've been told specifically that no, no, you will get, you will not get your camera in there. It'll be over their dead body that you'll get a camera in the Amazon warehouse. Yeah. Not going to happen. I'm afraid we'll have to settle for a J car. Yep.

**Chris Gammell:** Yeah. Cool. Cool bananas. So where, I would like to get a tour is Skywater, which just announced with Google, they're working, they're moving down to 90 nanometers. So that's the ones that talked about Matt Venn doing the, uh, the zero to ASIC course. And this is Tim Ansel has been on the show a bunch before.

**Dave Jones:** This is the open source.

**Chris Gammell:** This is the open source ASIC. That's right.

**Dave Jones:** Yep.

**Chris Gammell:** Uh, Mohammed from, uh, eFabless has been on the show. So basically all the people working with the kind of the open PDK. And so Skywater open, uh, had an open PDK and Tim's been working on the, from the Google side to do this sort of thing. They're now moving from one 80 down to 90, which is pretty exciting.

**Dave Jones:** Yep.

**Chris Gammell:** I wanted to tell Davis because we were talking a little bit about like thief river falls is in the middle of kind of nowhere, but it is in Minnesota. And Dave's like, well, what else is in Minnesota? And the answer is skywater, actually skywater technology is there too. It's in Minneapolis, which is like the metropolis of the state. But yeah, yeah, it is there. So it's actually, I found out it used to be, I was right next to the Minneapolis St. Paul airport. That makes sense. Cause then you get all of the logistics.

**Dave Jones:** Yeah. But the fab isn't there. Is it, is the actual fab there?

**Chris Gammell:** It is. Oh, right. Right on the lake next to it.

**Dave Jones:** Oh, nice. Well, it, it, it has to be on the lake cause fabs need water. They need lots of water. So I assume that's why it's near.

**Chris Gammell:** Sure they do. But you know, I used to work on a, at a fab in the middle of Austin and there's not a lot of water. Yeah. And also a microchip has a fabs. Yeah. Yeah. I also thought that for a long time and then I'm like, wait a second.

**Dave Jones:** Well, we were just reporting a couple of years ago that Taiwan had to reduce its chip output because of a water shortage. So, you know, sure.

**Chris Gammell:** But that's probably a lot more chips than these guys. So, right. But this used to be, so I found out recently that this used to be a Cypress facility. I didn't realize that.

**Dave Jones:** Right. There you go. Yeah.

**Chris Gammell:** So that's what, so Cypress used to have in-house. Right. Now Infineon. And now they, that expanded with private equity. They, they bought it and.

**Dave Jones:** Cool bananas.

**Chris Gammell:** Now it's Skywater.

**Dave Jones:** Things are happening in the chip business and well, it can't come too soon because we know what's happening at the moment, you know? So. Yeah. Yep. Yep.

**Chris Gammell:** Yeah. And you know, so in the US probably people don't care too much, you know, especially maybe Australian people that I'm talking to right now, but that stuff did pass. The money, the money is in the pipeline. So all those announcements we've been talking about for months and months and months, and there's actually new ones even. So there will be apparently new chip fabs in about two to three years, probably more. They'll probably be up and running. And it'll be interesting to see. Like, so we might have a glut of chips in two to three years, which would be really interesting. Uh, so, you know, we're, we're in a very big dip right now in a sourcing perspective, but what does that mean two to three years from now? Who knows? Aside from the global impacts of, you know, what, what does or doesn't happen, assuming steady state on all other fronts, like Taiwan still outputting what it does now. Now, if like TI and Intel and all these people that said they're opening more and more. Yeah. Yeah. Yeah. If they're all, there's more tabs now. Yeah. Does that mean there's more parts available? Cause like that could mean cheaper parts and it's like, Oh, okay. All right. I'm, I'm down for this, you know, assuming everything goes okay.

**Dave Jones:** Intel ain't making your, uh, little, uh, voltage regulator, you know? Yeah.

**Chris Gammell:** But it's still just interesting, you know, like that could drive, you know, so then you think about the five year at Mark, right? So then five years from, again, this is all assuming everything else doesn't go to crap, which, you know, who knows, but if everything else was stable enough, so then five years from now, there's all of these other chips, like what does that enable? You know, like, it's just, I don't know. It's a, it is an interesting time in the chip industry. Got it. Not least of all, because just today I saw one of the big chip companies that I follow, which is Nordic semiconductor. They have a job opening for risk five designer. Oh, there you go. Oh. Oh, okay. Dokey. So, you know, I know they're like, they're not the only ones. They're not the only like major chip companies look at it and they're fabulous as well. And they're not the only ones looking at it, but like, yeah, yeah. I think we're going to see more stuff like this over time. A lot of the expressive stuff is already risk five.

**Dave Jones:** Yeah.

**Chris Gammell:** I'm sure Nordic's doing that too. And it's just like, all right. So what does that mean then too? I just, I don't, I don't have any kind of crystal ball in this stuff. It's just, it's really, it's an interesting time that we're, we're living in here.

**Dave Jones:** Well, nobody really predicted the risk five thing. Nobody predicted the explosive growth.

**Chris Gammell:** I bet the people in Berkeley that invented it.

**Dave Jones:** Oh, well, yeah. But you can say that with hindsight, right? But it could have completely flopped, right? Yeah.

**Chris Gammell:** You're right. You're right. Yeah. I was talking about the, the researchers who were like inventing it, but yeah, they were probably not like, oh, this will be like a huge deal. Right.

**Dave Jones:** In two to three years, every, every major manufacturer will be having a, you know, a risk five division, you know, like, no. Right. It seems to have just like, I don't know. There's something about people want to jump onto the standardization bandwagon. Maybe, you know, open source, you know, I guess. Well, well, what helps that there's no, 12 years ago, that's when it was first introduced. Well, okay. It's not, it's not an overnight success, right? I guess.

**Chris Gammell:** Sure. Sure.

**Dave Jones:** But still it did like, as far as we're concerned, it seems to have exploded pretty quickly. Like it seems to, you know, one.

**Chris Gammell:** I remember we got in trouble for not understanding it about five years ago. I think that was the first time that we started talking about it on the show and being confused about it. Maybe more than that. Yeah. I bet I can go back and look, but yeah, it's, it's definitely like. It's a lot of places now. And, you know, Dave's perception of this might be just because I talk about it a lot too. So like that could also be the, but you know, I, I whisper in the ears of many powerful people.

**Dave Jones:** Bragging. Chips are hard to get right now. Anyway, yeah. Over time. So we've, we've got the dregs. What are the dregs? Breaking news, breaking news, straight off the teletype, the Facebook-y metaverse. Mark Zuckerberg lost, lost $2.8 billion, not in a year, but in a quarter, $2.8 billion loss on their metaverse division.

**Chris Gammell:** Suck it. Suck it, Zuck. Suck it. I mean, it's a, it's a drop in the bucket for him.

**Dave Jones:** We said it. We, we, we called it the other week when we said it's either, it's either the Oasis or bust.

**Chris Gammell:** That's right. Yeah.

**Dave Jones:** It's either the Oasis or bust. It's like, there's no in between here. Like there's no, I, I, I think you have to go the full Monty or it's, or it's just going

**Chris Gammell:** to, I saw this, I saw this article and I was like, there's, it can't be that bad. And I went and watched a video. Oh my God is so bad.

**Dave Jones:** I've never watched a video of the meta. Well, I've made it. It's so horny. Yeah, I know. Well, I've seen like little snippets of it here and there and it just looks stupid. It just looks so dumb.

**Chris Gammell:** So dumb. It's like, everything's just like, like avatars of like, you know, like, tigers that are a human form and like dancing. It's like, what? No, no. This is so, this is never going to catch on. This is like, you know, like someone like buying, like buying their grandchild, like a toy and thinking it's the hot new thing. It's like, no, you know.

**Dave Jones:** No, it's not, they'll just use it and go, and then, you know, yep. No, no, loser. $2.8 billion loss in one quarter. I sucked in. And I, and what's this about? Tell it and tallies announced the creation of leading Western internet of things, grown solutions provider. I didn't know telly, tellies who's my former employer, technically.

**Chris Gammell:** Yeah, they have an IOT division. And so basically they're, they got absorbed by. Dude, you and who's tell it?

**Dave Jones:** I got no idea. I got no idea.

**Chris Gammell:** Tell us like a cellular module, but kind of like broader than just the chipset. So they kind of make the modules, but then some of the software and services around it, that sort of thing. Got it. I think the bigger one is actually Semtek buying. They actually did. They are, they did announce they're going to be buying Sierra wireless because Semtek are the ones who make LoRa chips.

**Dave Jones:** Right.

**Chris Gammell:** Which goes into every LoRaWAN thing. Remember LoRa is the physical layer and LoRaWAN is the network layer. And they bought a cellular company, which is like a cellular module maker, which is like personally, that's a bad look. Yeah. I mean, like, it's like, oh, maybe we can't make that much money on LoRa. It's like, oh, really? Like, okay, well, wait, should we be using this? And like, there was Stacey from the IoT podcast, Stacey on IoT. She wrote about this thing that about Helium. So Helium, there was. Oh, yes. Someone. Did you see that thing on Twitter? So like Helium has been a bunch of places. They've pitched us before. They've pitched NPR. There was an NPR story recently about being built a miner, being into a house. And like, I will agree that while I hate most cryptocurrency things, you know, Dave likes it a little bit more. While I hate most cryptocurrency things, it is probably the closest use case for a cryptocurrency, which is like basically tracking that packets have been received. But my argument is exactly the argument that the analyst was making. Like, look, there's nobody using the other side of it. And they're like, well, we have to build the market for it. It's like, okay, but like, here's my only proof point. I have never seen a single thing. And I would love to see if anyone has heard this otherwise. I have never heard of a single marketing campaign that says, are you building a LoRa device? You should use the Helium network as your backhaul, right? Like, you would think that if they're spending all this money on, you know, cryptocurrency and all these other things, why aren't the hardware engineers? And I know a lot of them. And, you know, like I'm into the IoT space, whatever. I've never seen a single thing that says, here is what you should do to go and use the actual, you know, proof of coverage, whatever. All of these people that are buying, all of these suckers that are buying these miners. No offense. And like, there's nobody using it. And it's like, so what are you going to do? You're just going to go design it just for the huge customers? Why wouldn't you try and sell it to like the little folks? I just don't get it.

**Dave Jones:** No, there's other, you know, and there's other associated ones like that, like Power, for example, which is an Australian company. And it's a crypto, it's a crypto based thing, but it's designed for power sharing. So if you've got solar power in your house, you can share it with other houses in the street. And then it bills everyone like, you know, you can trade energy kind of thing. Sure, credits.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And they're actually, they've got big deals with, you know, some major energy companies. And they're actually trialing these in, you know, actual locations. You know, people are actually, you know, trading energy. Right. And, you know, so it's all there. It's not just, you know, so they're actually actively creating that market, as you said, which helium's not. So helium's just going to come a gutter. The wheel's going to fall off that billy cart. Guaranteed.

**Chris Gammell:** I think that power thing is a dumb thing too. I mean, like all of these are like really dumb things anyways, because like they're all using this very complex method to then just basically a spreadsheet. Right. That's always like the joke about cryptocurrency. It's like, why isn't that just a spreadsheet or Web3 or whatever you want to say? It's a ledger. Yeah.

**Dave Jones:** Yeah. It's basically a ledger. Yeah.

**Chris Gammell:** It's a ledger. How you can trade. Anywho, I send all of your hate mail to blockchain at theampower.com. That'll go directly to where I keep my cryptocurrency, which is the toilet. I, on the other hand, will happily accept crypto donations.

**Dave Jones:** Thank you very much. I accept library credits. I accept power credits as well. Yeah. I accept everything.

**Chris Gammell:** The toilet is also known as the most recent price on most cryptocurrencies, as in they are in the toilet.

**Dave Jones:** So really, I could have sworn that my portfolio is massively positive. I'm sorry to tell you, but you know, I could have sworn. Good for you, buddy. Just saying. Just saying. All right. Anyway. All right.

**Chris Gammell:** Well, that's all we've got for this week. Well, I'm going to go and do something poor people do. And Dave's going to go and do something rich people do right now.

**Dave Jones:** That's right. Yep.

**Speaker ?:** Yeah.

**Chris Gammell:** All right. Chat with you next week.

**Dave Jones:** Catch you next time.
