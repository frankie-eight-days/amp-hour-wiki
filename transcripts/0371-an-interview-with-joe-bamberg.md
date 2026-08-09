---
episode: 371
title: An Interview With Joe Bamberg
url: https://theamphour.com/371-an-interview-with-joe-bamberg/
---

**Joe Bamberg:** This is The Amp Hour Podcast. Released December 10th, 2017. Episode 371. An interview with Joe Bamberg. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. I'm Joe Bamberg from Sense. Hey, Joe. How are you doing? Good. How are you doing, Chris? Good. I'm excited to talk to you. Mostly because, well, so I always love having guests onto the show where there's something me and Dave have been talking about for a long time with really no reference point and no knowledge. And in this case, I would think anytime we talk about power, you will be able to kind of clarify all of the crap that we spout about power unknowingly. Does that? Yeah, hopefully. Can you set us straight here? That would be... Sure. Okay. Obviously, Dave's not here, but I will now be from in a position of power, and I will be like, no, well, Joe said. Yeah, you can put him in his place now. Yeah, exactly. So you've been in the power realm, but in kind of a weird spot of it, right? I mean, so you're using tiny, tiny little electronics to measure and control lots of, you know, like large wall power. I always say wall power. I know that's not the right term, but, you know, AC 120, 240, whatever, right? Yeah, yeah. So how did you get to that point? Obviously, I want to hear about sense. Sense is a... Well, you could tell us about sense, but how did you get to where you are now, you know, kind of starting back from the beginning? Let's see. So I studied at the University of Miami. Okay.

**Joe Bamberg:** And I was actually a biology chemistry major. Really? Okay. And pre-med, and I was kind of... I didn't know what I wanted to do. I was thinking medical school, and I kind of got disillusioned, but depressed at like biology and chemistry. Disenfranchised at the very least. Yeah, disenfranchised. That's the word I was looking for. That you got... You have to... There's just so much memorization, and I wanted to be able to understand some very fundamental things and be able to figure stuff out. And my suite mate was a computer engineer, and he said, you should look into engineering. So I did. Electrical looked the most interesting because it's so broad from communications to robotics to electronics. There's so much to it. And I said, I'll go with that. But I maintained my pre-med. I graduated. Yeah, I took the MCATs. Oh, wow. Got talked out of going to medical school by a buddy's dad who was a doctor. And instead got my master's. And after that, I started at Analog Devices where I had an internship there. And it turns out I grew up in a small town north of Boston called Wilmington. And I went to Miami for college and ended up getting a job right back in Wilmington. Right. You're like, I'm free of the snow. Crap. Yeah, yeah. Unfortunately, there's only a couple of places, big places to work in tech in the country. And Boston is one. Silicon Valley is one.

**Joe Bamberg:** Like Texas is one. I was going to say, I refute that a little bit. I mean, obviously, I was in Cleveland for a long time. But I think there's pockets elsewhere. But it depends. I think it's very industry dependent. So if you want to work in Silicon, for sure, like, yeah, there's, what, four. I mean, that's why I left Silicon in the first place is because there's only so many spots to go.

**Joe Bamberg:** Oh, yeah. Absolutely. That's one of the reasons I got out of it as well. I mean, if you start working for ADI, you can always go to Limerick, right?

**Joe Bamberg:** I mean, like. That's true. I went to Limerick a bunch. Really? That's a fun little town. Yeah. I've always wanted to go over there. And like the, did it start over there? I don't actually know the tie-in, why Limerick is so prominent for ADI.

**Joe Bamberg:** The funny story about that was back in the 80s, the Irish government wanted to increase, like, industry and business over there. So they set up some very advantageous tax rules. Uh-huh.

**Joe Bamberg:** Just like, yeah, that's why Apple's headquartered over there, quote unquote, right?

**Joe Bamberg:** Yeah. So it was, it was pure, back in the 80s, it was purely a, at least from what I understand of the ADI history, it was purely a tax play to be over there. And it kind of grew up to, grew up into be one of their big design centers. Sounds like it worked.

**Joe Bamberg:** Yeah.

**Joe Bamberg:** Go Limerick. That's great. Yeah. Yeah. It's a, it's a fun little, a fun little, little city there.

**Joe Bamberg:** Okay. And so, ADI is a big company. Lots of, I mean, obviously people here, probably fans. I was a fan of, well, I was fans of everything up until they bought LinearTech, of course. But apparently it's good. I have some people write in, they say it's going fine. So, okay. But what, what segment were you in there?

**Joe Bamberg:** So I was in the energy metering group. So, which is how I got tied into sense. So when I was, so when I graduated in 2002, which is kind of right when the tech downturn came. And my options coming out of school were limited. I had interned at Analog in their energy metering group. So I had an offer from them and I had an offer from the CIA. And, and, and, and Analog was paying a lot more than the CIA was. So I, I went with that. And so I ended up working in the energy metering IC group that made the, they were, I think the original first company to make energy metering ICs. Up until that point, it had all been done electromechanically. Oh, really?

**Joe Bamberg:** Okay. I would have expected like discrete op amps too, but.

**Joe Bamberg:** Yeah. It's, I don't know. There's, at least to my knowledge, there, there was not a discrete op amp B type of energy metering system out there. Hmm. Interesting. Yeah. Yeah. So, and this was back in the, that group was started. The guy that started it was this, this designer's name's Eric Nessler, who's absolute genius and one of the nicest guys I've ever met in my entire life. He's a, he's actually a, a fellow at ADI now. Oh yeah. Right. Which is, which is funny because he started this group. I grew it to, I mean, I think it was doing like 40 or $50 million a year or something at one point. And there was creative differences between, and he should have been a fellow long before. Oh. But he, there were differences in the direction they thought they should take the group. He wanted to go simpler because, for developing markets like China and India, where the meter manufacturers over there, they didn't want to spend half a penny for an extra cap. Yeah. And upper management above him wanted to do like this crazy integrated microprocessor with the metrology stuff. Yep.

**Joe Bamberg:** And don't, don't cannibalize your business, right? Yeah.

**Joe Bamberg:** NBA playbook right there. Yep. Yep. And there was a following out and he left and ended up going to a couple of startups. And one of the startups he was at was this, this company called Lyric Labs that was doing like probabilistic hardware. Oh, cool. And they were using it to do like voice separation and things like that. Uh-huh. And he was there and they ended up getting bought by analog devices again. So, he ended up right back in the fold and then they finally smartened up and made him a fellow.

**Joe Bamberg:** Nice.

**Joe Bamberg:** But anyway, this guy, nicest guy and super, super smart. And he kind of started the whole energy metering business at analog and probably, I mean, you could probably make a case to say that he started the smart metering worldwide. Yeah.

**Joe Bamberg:** Yeah. So, could you, could you tell us about, so you said, so mostly mechanical in the past. I've seen it before. Uh, I think, I remember like a rotating disc. Is that the main piece you're talking about? The mechanical? What else? What are you talking about there?

**Joe Bamberg:** So, that's electromechanical and the disc just rotated proportionally to the, the, the power. And it would, uh, there was like a little, uh, pulse counter that would increment as you, uh, you used electricity.

**Joe Bamberg:** So, is the, the disc rotating, it's like, is it like kind of around the main, uh, incoming wire and then it's just using like right hand rule kind of magnetic energy? Is that the idea? Yeah. Okay. So, then pulse counter would be what, like how many steps the disc went past or like an optical or?

**Joe Bamberg:** Yeah. So, in, in the, so it was like, uh, uh, impulses per kilowatt hour. And it's actually the, the very first smart meters, uh, even though they were, uh, they were electronically measuring the, the, uh, the power, there was still like the interface. The, the, the utility still didn't know how to use a different interface to it. Right. So, like the, uh, the very first ones used a, a stepper motor driver and the, uh, the, the chip would just output a pulse proportional to the kilowatt hours. And there was, uh, you could dial it in so you get so many like pulses per kilowatt hour and it would just drive a little stepper motor and flip the little, uh, rotating number thing. Yeah.

**Joe Bamberg:** As I was going to say, the, their, their UI, their UI for many years has been sending you a postcard and mark on this postcard where your, where your arrow is pointing. Right. Yep. Exactly. That's, that's insane. I mean, I guess, I guess I didn't even really think about that, that like, were they dragged kicking and stream screaming into the smart meter market or. Oh yeah.

**Joe Bamberg:** I mean, utilities don't want to change until they're forced to.

**Joe Bamberg:** Right.

**Joe Bamberg:** They're, I mean, it's just so heavily regulated that it's kind of to, to introduce new technology or new ways of doing things. Right. Uh, it's one, they don't want to spend money on, on, they want to get 10, 15, 20 years out of a meter. So they don't want to replace them period. Right. But two, just to get anything up because every state has their own regulatory body governing utilities. So it's just, it's a, it's a huge hassle for them.

**Joe Bamberg:** Right. Right. And so, okay. So that, that moved the measurement piece there, but then I was just thinking about, so a former guest was, uh, Larry Sears, who was a teacher at my, my alma mater, Case West. And he was started hexagram, which was the, uh, basically the RF piece transmitting. I, I assume there must've been transmitting unless it was gas. Oh no, sorry. That was gas meters. So that wasn't even, I was thinking, I was thinking meters, but that was gas meters. So is it to the point now where it's still, is it still arrows or what's.

**Joe Bamberg:** So there's, there's a couple of different ways that they do it. Um, so following the, the stepper motor, uh, then they went to, uh, and I, I could be missing a step or two here cause being at the end utility wasn't exactly where I was. But, um, then it went, uh, uh, optical infrared where there would be like a little, uh, like IR, our LED spot right on the meter. And, uh, somebody would come to your house and they would have this little tool that they connected up to it and they could read it optically.

**Joe Bamberg:** Hopefully a Palm pilot. I mean, that's, uh, what Palm pilots are good for, right? Seriously. IR transmitting a V cards.

**Joe Bamberg:** And then, um, and then after that, so the, now there's, um, they call it machine to machine communications. I've heard of this as kind of my job these days. Yep. Yeah. And it's, uh, sub gigahertz like in the, in the U S it's usually the 900 megahertz range. Okay. All right. And, um, there's a, they'll have a van that drives down the street and just pings all the meters. And pulls the info from it.

**Joe Bamberg:** Nice. Okay. And that's, so it's still just doing the same thing though. There's driving down the street, picking up how much you've used. It's amazing that there's no actual communication method just back on a phone line or back on a cell line or wifi or whatever. Right. I mean, it's still, it's still person in the field.

**Joe Bamberg:** That's one of the, the, the issues that like, uh, I mean, not to jump too far ahead with sense is that we, we work off a wifi or we transmit data back at wifi. And the utilities, um, are very hesitant to do that. They're like wifi. I don't understand. What is this? Yeah. They're like, Oh, it's too unreliable for us. We can't, we couldn't possibly use wifi.

**Joe Bamberg:** Send the message again, guys. Come on. Yeah. Yep. Yeah. Okay. Okay. So, well, so, so now we're at the point where we've gone from dude knocking on your door and going into your house and, or you filling out a card with the arrows where those are pointing. Um, boy, I can't even imagine. They must've had people then who got those cards and had to put them into a system, right? Yeah. Data entry. Yeah. Wow. You guys are killing tons of jobs. What? Jeez, man. You thought about that? No. Uh, okay. So what, so when, when you say smart meters, what else, I mean, is there anything else in there? I mean, it was literally just measure this thing and do the billing.

**Joe Bamberg:** So the very first, um, uh, smart meters at those. So I'm, I'm obviously using ADI as an example. Sure, sure. Yeah. We'll just use it as the default. The very first one. So we're talking late nineties, early two thousands. It was just called a, uh, it was called a watt hour meter. And it basically, all it did was measure active power. So measure Watts and output that pulse. And then, um, subsequent, subsequent generations started adding additional features. So you could do, uh, not only, uh, Watts, but also VARs and, uh, apparent power. And you could get information like, uh, frequency and period. You could get power factor information. You can get, uh, triggered for certain, uh, power, like power events. So like line sag or, or things like that.

**Joe Bamberg:** And you explain what some of those things are.

**Joe Bamberg:** Yeah. So, uh, so in power is the, I, I mean, you know, you're familiar with this stuff, right? Yeah.

**Joe Bamberg:** So yeah, I, I, a little bit, but I'm, you know, like this is the kind of thing where me and Dave were talking about it. We're like, Oh yeah, yeah. Kind of like a lot of hand waving, but nobody can see your hands, you know?

**Joe Bamberg:** So, so there, I mean, power is, is kind of, um, it's a, it's a little bit non-intuitive. Yeah. Uh, and so the, the power that we all know and love and that does work is, uh, is active power, right? And it's what we measure in Watts. But when, uh, when your load is not purely resistive, when there's some kind of capacitive or inductive component to it, then you have what's called VAR. Um, I, it's volts amp, volt amps reactive. And that's, uh, I mean, you, for lack of a better term, it's almost like imaginary power. That's power that. Yeah. See, I think that's where people always get, that's when I always start seeing people's eyes glaze over. Right. So, and I mean, and what it is, is it's, I mean, it's power that has to be generated by the generator. Right. It gets delivered to the load, but then it's power that is not dissipated. So it actually gets sent back from the load to the generator.

**Joe Bamberg:** Right. It's like reflected or it's, it's really just inefficiencies, right? It is. It's basically the inefficiency of, of generating and delivering power.

**Joe Bamberg:** It's power that needs to be generated, but it doesn't get used. Right. So you have to, you have to build power plants that can, so it basically increases the power that needs to be generated without being used.

**Joe Bamberg:** Right. And this is when people talk about load balancing as well, right? Like this is, this is, you can have a, a, a, a, passive load or inductive load, right? And you can leading and lagging and all that stuff. Right.

**Joe Bamberg:** Exactly. So that, the jet normally a purely resistive load has a power factor of one. Yep. And any change in the, the complex impedance makes, drops that from one. And that's not good for utilities because they have to generate more power, but they can't bill you for that. Yeah. Right. They only, they bill off of watt hours, but. Got it.

**Joe Bamberg:** So. Oh, that's interesting then. So then, so, so when, when the reactive power stuff started getting measured, they still don't penalize the user?

**Joe Bamberg:** Yeah. So the, in, in most cases, like residential power, you're, you're going to have a power factor close to one.

**Joe Bamberg:** Okay. Because you don't. Because of the, in the devices in the house, stuff like that. Exactly. You're not running like, like huge, uh, it's not generators. I guess it would be huge motors, right? That would be like a big inductive thing.

**Joe Bamberg:** Yeah. The place where it gets it is a rotating machinery. Got it. So motors, things like that. And that's when, um. So what about like, like AVE shop, right?

**Joe Bamberg:** So he's got tons of like motors in his shop, like a machine shop has tons of motors going.

**Joe Bamberg:** That's exactly where it would be. And what they'll do, usually those loads are, are inductive. So what they'll do is have a huge bank of capacitors at the site to, to correct the power factor.

**Joe Bamberg:** Got it. Okay. And that's, so, so there are different classes of power billing as well, right? Cause like an, an industrial customer would get billed differently than a, than a home customer just because they expect the industrial customer to, to have those inductive loads.

**Joe Bamberg:** Yep, exactly. And, um, you know, it's funny at, uh, at, at, at analog devices, I, I was friendly with one of the facilities guys there and he was telling me their electric bill. Cause there's a, there's a fab at the Wilmington plant. Oh really? I didn't know that. Their electric bill ran between 800 and a million dollars a month.

**Joe Bamberg:** Yeah. Oh yeah. Nine. Yeah. I used to be at Samsung and, uh, yeah, they, they would have some, some serious bills, but they also, I remember this now, they had a, an agreement to where the power company, if they didn't have uptime, the power company had to pay Samsung because it would not only would it potentially be loss of money, but also if the power cut in the middle of processing, you know, all those wafers you get. Yeah, exactly. Cause there's like stuff hanging out up in plasma clouds or whatever. And it just like, or there's robots, you know, moving something and those smashing into the wall, whatever. Right. It's just, yeah, it was a big deal when the power went out. So that's, that's cool though. I didn't, I didn't realize that ADI had on site stuff. I thought I remember, Oh God, how many years ago was this? Two or three years ago I was, I was cursing their name for ADI, uh, you know, pushing all their analog processing to TSMC. I thought that was very, very short sighted and, uh, maybe it wasn't all of it though.

**Joe Bamberg:** I mean, honestly, most of, most of it is fabulous. Sure. Their, um, TSMC, MagnaChip, uh, there's a, there's a few of them where they fab at you. Mostly the stuff that they do in house is proprietary things. So, um, high voltage processes, like really fast stuff. Um, the mem, a lot of the mem stuff, but that's, that's what they, uh, that's what they do in house at the fab there, but like analog, uh, like pretty much vanilla CMOS or any of that kind of stuff is all.

**Joe Bamberg:** Yeah. And it wasn't that it was like the, I think it was because the agreement said that TSMC got to keep all the, the analog, um, uh, IP around it, but I guess it's probably, it was the vanilla stuff that you're talking about now. Now thinking about it like that. Yeah. It was probably anything TSMC was doing on, on their process. They kept.

**Joe Bamberg:** So, yeah, I mean, it's just, it's just too expensive and too difficult to go to like smaller and smaller process nodes that, you know, once you get down, I think they had a, they did a 0.18, I believe at one point themselves. But I mean, after that, it's just, you're talking billions of dollars in a, in equipment for each new process node, you know?

**Joe Bamberg:** Yeah.

**Joe Bamberg:** Well, someone's got to do it.

**Joe Bamberg:** I don't know. Yeah. Okay. So, uh, so, so we were at the point where, so now chips are measuring reactive power. Ah, yes. Yes. So, so what changes about it then? So is it just like you start needing to have more, uh, more measurement line? Obviously you need to measure current and voltage simultaneously, but you probably were doing that with the active power stuff, right? Yeah. Yeah.

**Joe Bamberg:** It's just, it's, uh, it's more of the, the signal processing of it. It's, um, it's a little bit. Mathiness. Funky. Yeah. It's definitely a mathiness. And, um, and one of the, one of the ways that they, they, they actually had to come up with some clever ways of doing it without, um, like that micro, without do it, using a microprocessor to do, to do the math.

**Joe Bamberg:** Interesting. Okay. So it was using like multipliers or something like that? Yeah.

**Joe Bamberg:** It's actually, one of the things that you'll see is it's, they call it like a filter based metering. So it's all like low pass and high pass and multipliers and then, um, uh, Hilbert filter, which like phase shift. Nice. So when you're, when you're measuring, um, reactive power, it's, you basically have to shift the current signal 90 degrees out of phase and multiply it that way. Mm-hmm. And one of the ways they do that is, um, it's like a, like a Hilbert, uh, which is, um, it's flat for the, for the gain, but it's got a 90 degree phase shift in it. Yeah. Yeah. But it's a, there's definitely some, some funkiness to it for sure. And also not doing like RMS, uh, RMS calculations is not trivial in, in hardware filters because you have the, the squaring function and the, and the square root function and things like that.

**Joe Bamberg:** Yeah. Yeah. That's, that's crazy. And I mean, I always think about it just with like a multi analog multiplier, the range you need to have on the output, you know, obviously if you're multiplying two, you know, nominal analog values, you can quickly, you know, start to scale. Is it log output? I mean, like.

**Joe Bamberg:** No, it's, I mean, it's linear. Okay. Cool. They, um, yeah. Well, one of the other things is the, the inputs too, because there's a range of current, a different current sensing that need to be, uh, accounted for, for your, for your inputs too.

**Joe Bamberg:** Okay. So why was it just the timeframe? Like why, why didn't they, or maybe it's changed since, but why did, why didn't they push this all into a analog to digital converter and start, you know, doing DSPs or, you know, micros?

**Joe Bamberg:** Well, I mean, that's really what it is. Cause the, the inputs of, uh, it's, it's all fixed. It's basically just fixed function DSP in, uh, in the, in the, in the hardware chips. They, um, so the, the front end, the AFE, the analog front end, uh, it's like, you're taking the, the current and the voltage inputs and directly, uh, converting them, um, to bits and, uh, and everything is done, uh, done digitally with fixed function DSP and those chips.

**Joe Bamberg:** Oh, it is. Okay. All right. Yeah. Interesting. Yeah. I guess, I guess the thing I think about is like, so if I was going to do this, if I, if I was going to try and start measuring power, obviously I'd be very safe. Everybody out there should be very safe. Uh, but I'd think I would, you know, I would have a current sense, uh, probe. I'd have a voltage probe and I would look at it on a scope and I'd want to see the waveforms. Right. And then, so like in my mind, I'd be like, oh, I could like quantize this waveform and then, you know, push it to an FPGA or DSP or something like that. But, but that, that sounded expensive as I said it. Right. I mean, like, so this is a, this is a cost thing as well. Right.

**Joe Bamberg:** Oh, absolutely. Yeah. So the, the, in the, if you like decap any of these energy metering chips and, um, by the way, we, we, at sense, we don't use actually an energy metering chip because they don't have the capabilities of what we need. But, um, yeah, if you decap them, it'll, it's about one third analog and two thirds digital, which you can, you can see under a, uh, under a microscope, but just the, because of the feature size. Yeah. And it's like your, your voltage comes in on the, on the board. It's basically a, like a voltage divider is all they use for the, for the voltages inputs on that. Oh, really? Okay. And for the current, yeah, it's just directly connected and divided down with a couple of resistors. Hmm. And for the current, there's, um, there's three, three main ways that they, uh, that they, they transduce it. It's either a, a CT current transformer. They use, um, a shunt, um, but shunts have a, have limited current range because there's a, uh, there's one of the regulations is that your energy meter can, is only allowed to consume so much power. And, um, I mean, when you're, when you have a shunt, you're dropping, it's like a really,

**Joe Bamberg:** you either have a low sync, low signal and low and low load, or you have high signal and high load, right? Yeah, exactly.

**Joe Bamberg:** So it's just like a, a million or micro ohm, like resistor that you're just dumping it over and taking the voltage. Usually I think those are only, uh, they usually only use those up to like 80 amp services. And then the, um, the third main way, which is, uh, which is less common is, uh, called the Rogowski coil. So Rogowski. Okay. Yeah. Which is, um, I don't know if you're familiar with it. It's a, uh, it's, it's, it's, it's like a, kind of like a, a CT in that you're, uh, generating a field based on the current, but there's no, uh, there's no core to it. It's an air core. So you don't have any of the saturation problems that you have with a CT. Mm-hmm. Um, the, the little bit is that it generates a signal that's, uh, proportional to the derivative of the current. Oh. So you need, you need an integrator, uh, what you need one additional step on it.

**Joe Bamberg:** So does that like get like, uh, additive errors over time? You have to like do like a reset or something?

**Joe Bamberg:** Uh, no, it doesn't. It's just to add a slight bit of complexity. And the other thing is where, um, in installation, installation matters with a Rogowski coil. So with a CT, as long as your, your, your line is just running through the middle of the CT, it's, uh, it's, it's fine with a Rogowski coil. The, if it's not centered, it'll introduce some error onto it.

**Joe Bamberg:** Oh, okay.

**Joe Bamberg:** So the installation is a little, little trickier. And the other thing is, uh, until fairly recently, uh, P people didn't manufacture Rogowski coils that you had, uh, if you wanted to use it, you basically had to roll your own.

**Joe Bamberg:** Okay.

**Joe Bamberg:** You can, you can buy them now like, uh, off the shelf, but for up, that's only a fairly recent, uh, innovation.

**Joe Bamberg:** Okay. And so what is, what is a, uh, what's a common part number that people could look up? For a Rogowski coil? No, sorry. Of, of like one of the parts that, that you worked on or that ADI makes that, cause that always helps just to look, people are probably listening and, you know, thinking, okay, I can kind of visualize this, but sometimes it's just easier to look at a data sheet.

**Joe Bamberg:** Yes. So, um, God, one of the, uh, the, the analog, they're all the ADE lines. So like the very first one back in the early two thousands was called the, uh, the ADE seven, seven, five, five. And that was your, your very basic watt hour meter. Um, and then the first three phase we did, one we did was called the ADE seven, seven, five, eight. And then, uh, I think the last one that I worked on was a chip called the, the ADE seven, eight, five, eight.

**Joe Bamberg:** Okay. Uh, cool. And that group, let me see. ADE seven, eight, five, eight. Yeah. Yeah. And I'm looking at the seven, eight, five, five right now. And yeah, it looks, I mean, it's exactly what you're talking about. It's got the, the PGA programmable front end, and then it's got two voltage inputs. One of which was ostensibly for current, the current, uh, um, like a, like a CT, like you're saying, and then into the multipliers and then DSP stuff.

**Joe Bamberg:** So if you look at the ADE seven, eight, five, eight, that's a little more, uh, recent one, even though it's still a few years old now. And that was, is kind of more where the energy metering ICs stand these days.

**Joe Bamberg:** Okay. That's cool. And then, so, okay. So people can go and check those out and obviously ask questions if they have them in the comment section of this episode. Uh, but what was after, after this, right? So you left AD, uh, ADI at some point and then you went to somewhere else.

**Joe Bamberg:** So I, I left, uh, ADI a couple of years back and I ended up at, um, at Qualcomm where it was actually a, before they tried to merge with Broadcom. Yeah. Right. Uh, it was a, uh, a, a small, a startup that was bought by Qualcomm called PixTronics. And what they were doing was a, uh, a, a new, a MEMS display technology. So as opposed to using, uh, transistors to control the, the, the light, uh, in a pixel, they actually used a little MEMS shutter to, uh, to, uh, on each pixel. And one of the cool thing was that for, uh, for like the same display brightness, it used, uh, like half the power of, uh, a conventional, a conventional, um, display.

**Joe Bamberg:** Interesting. Okay. But obviously there's all the downside of MEMS versus like of the mechanical aspect. Yeah.

**Joe Bamberg:** Which was, which was one of the, uh, uh, one of the, the big issues we were fighting with that was that, um, you get, uh, like it, we were still, it was never released as a, as a product. But it was, um, it was still kind of R and D we had, we had, uh, working stuff, but, um, because it was still R and D we were in this like really crappy fab and like a really dirty fab. It was using a, a, a process called Igzo and, um, it's indium gallium zinc. Some, I don't even remember. Zinc. I don't even remember what, what it was. Zinc oxide. Yeah. I think it was zinc oxide.

**Joe Bamberg:** Um, yeah. God, what? Igzo. That's great. Okay. Yeah. And indium gallium is what's, uh, usually those are the big ones in like solar panels, right?

**Joe Bamberg:** Indium gallium zinc oxide. That's it.

**Joe Bamberg:** So this is like you were putting, uh, like sunscreen onto a solar panel. That sounds what it sounds like. Pretty much.

**Joe Bamberg:** But, uh, it was, it was, uh, it was, uh, an old fab and it was just a very dirty process. So one of the issues we were always dealing with were like particulate matter, jamming the shutters and things like that. Uh-huh. Yeah. And, uh, man, once you, once you work in any kind of display technology and you start like learning to find all the defects in displays, you, you can't. You can't, you can't watch TV anymore. You can't watch TV anymore. You can always see them in any black scenes. You see them. One of the cool things I learned too is that when like all TVs have dead pixels and they, they do what's called inking on them and they, they basically inject like a little bit of dye into the, uh, into the, uh, into the dead pixel.

**Joe Bamberg:** Wait, just to really blank it out then or what? To blank it out. Yeah. Okay. So there's just natural fallout in the process you're saying, but then they, they just kind of remove it. They, it's like, uh, like what they do when they, it's like a final QA step or something.

**Joe Bamberg:** Exactly. They, they, they basically map all the pixels in the display and they go out and ink out all the dead pixels. And, and the reason they do that. So like a black pixel and a bright white screen is actually really hard to see. A one like white pixel in a dark screen like sticks out like a sore thumb.

**Joe Bamberg:** Right. Right. Huh. That's a, that's crazy. So, and I guess that saves money that gets their yields up, right? That kind of thing. Yeah. Oh yeah, absolutely. Absolutely. Okay. So, uh, when you, when you did that MEM stuff, I mean, I guess, I guess I didn't even ask this about the other stuff. Were you, were you designing the silicon? I mean, what, what was your, what was your role there?

**Joe Bamberg:** So at, at analog, uh, I was a, uh, a product engineer. So we kind of, we did all the evaluation and characterization and test development.

**Joe Bamberg:** So you'd be like the guy who came into an engineering energy company and you talk to the engineer and you'd make sure that the product was spec'd out properly and then actually go and work with the silicon designers to make this new product. Is that kind of the idea?

**Joe Bamberg:** Yeah. But part of it, um, and then, but also, uh, like basically running the project. Yeah. Right. Um, getting like all scheduling and all the fab stuff, but then designing the evaluation and bench characterization and actually doing that in the lab. Yeah.

**Joe Bamberg:** Data, data sheet type stuff, right?

**Joe Bamberg:** Like verifying data sheets. And then, um, like failure analysis. So when stuff, especially like preliminary silicon, we would, uh, like go through and when stuff didn't work, get a decapped and like you with the electron microscope and find like bad transistors or things that happened. And then when we, on, on, on some of the stuff, when, when it was, uh, like a, a simple issue to fix, then we would actually go in and do the, the design on the transistor level. If it was easy, if it was, uh, if it was something that like was much more like system propagated, then it would get kicked back to the designers to, uh, to, to rework it. But, um, so we did a little bit of silicon design, but that wasn't like the big part of our job there. That's cool though. I mean, and then designing all the, the evaluation boards and the, the test boards that interfaced with the, the ATE and automated test equipment for people that didn't know.

**Joe Bamberg:** Yes.

**Joe Bamberg:** Yeah. Sorry. Automated test equipment, all the, the dud boards for, uh, for like final test and all the evaluation boards and all the reference designs, all that kind of hardware stuff. We did all those designs.

**Joe Bamberg:** That's a lot of stuff, man. That's like, that's a, that's a long, long journey.

**Joe Bamberg:** It's kind of like the, uh, the, the jack of all trades, uh, job at a, at a silicon company. That sounds fun though. That sounds really fun. Yeah. It was, uh, I, I, I enjoyed it while I was there. Yeah.

**Joe Bamberg:** Okay. Well, let's talk about where you are now. Uh, so you are now at Sense. Could you tell us what Sense is?

**Joe Bamberg:** Yeah. So Sense is a, is a home energy monitor. It tracks your real time energy usage and over time it, it learns your home and it shows you what devices are on in your home and how much energy they're using.

**Joe Bamberg:** Okay. Uh, and this is, if people haven't seen it, it's actually really neat. It's nice, nicely designed little, you know, plastic, uh, enclosure, right? It's got a little wifi antenna on it, but you actually stick it in. I was surprised by this. You actually put it into your junction box, right? Your electrical box.

**Joe Bamberg:** In your, you, it gets installed in your electrical panel. You can actually install it outside too. Uh-huh. That's a, that's actually a more complicated installation to install it outside than inside.

**Joe Bamberg:** Why? Because then the probes have to go back into the box is kind of the idea?

**Joe Bamberg:** Well, not that, but you need to, you need to, uh, install a, uh, a split phase receptacle outside of it because we look at both legs of, uh, of your, your power coming in. So you, you basically need to install like a, like a dryer or oven. Plug next to your, next to your panel. If you want to install it outside.

**Joe Bamberg:** Right. So I, I was talking to a friend about this. We were looking at the, I was looking at the install instructions and I was, I was a little, it wasn't dismayed, but I was surprised that like, okay, so the install process, you actually just run some wires into, uh, you know, not dual gang. What's it called when it's, when you have both phases on it for like, like a, like an oven, right? So an oven is runs on two, at least, and then we're talking about us power here, right? Obviously, you know, Europeans can figure out what the hell they want to do with it, uh, or really anywhere else. But at one 20, right, there's dual phase and you usually have a, a circuit breaker that goes across both. And so you actually plug into both, both phases of a two switch.

**Joe Bamberg:** Yeah. So, I mean, they're both one 20, but they're out of phase. So if you look at both legs together, you can effectively get two 40, which is usually what you run your oven off of or your dryer or big appliances like that.

**Joe Bamberg:** Right. So, and you guys want to watch both of them because you want to see the whole thing in the house. And really that's because most residential power is coming in two phase, right? I mean, that's the idea.

**Joe Bamberg:** Yeah.

**Joe Bamberg:** Cool. Correct. So you want to, so that's watching the, the, it's technically called split phase,

**Joe Bamberg:** split phase. Sorry. You'll absolutely, the, the energy nerds out there go crazy when you, you use the wrong terminology.

**Joe Bamberg:** It's dual phase. Is that right? No. Just really mess with them. Yeah. Okay, cool. But that's good to know though. Split phase. It's square, it's square root of four phase. Whoa. What is that? Two phase. Two, two phase. Got it. Uh, um, so you're monitoring voltage on either of those split phases and then, and then what? Then you have a current transformer elsewhere?

**Joe Bamberg:** Yeah, we have. So there's, uh, it, it, it's really simple where you have the two voltage connections to look at both legs and then you have two current transformers to look at the, the two currents coming in and that's it. And the, the, the current, current transformers are just very easy clamp on. Um, you don't have to shut down power to the house or anything. It's, uh, it's just there. You can install it one handed. Yes. Right.

**Joe Bamberg:** Right. No path across the heart, please. Exactly. Yeah. Okay. So this is an interesting thing because I remember hearing about like, you know, people were doing a lot of DIY stuff that they have for a long time. And I remember always thinking about it and thinking, oh, someone wants to monitor the power in their house. That would get so expensive because you need to monitor every branch. If you really wanted to do this, right, you'd have to monitor every branch coming out of your electrical box, going to each, you know, going up to the kitchen or going up to the bathroom, whatever, and thinking, oh, it's like 15 amp service. You'd have to monitor each one individually. And that's obviously not the case here.

**Joe Bamberg:** So we do every, your entire house from just those couple of connections in your panel.

**Joe Bamberg:** So what, what is the missing piece here then? What is, what is the last part that, why aren't you monitoring each individual one?

**Joe Bamberg:** Oh, we don't, we don't need to monitor each individual one because we do what's called disaggregation and we can pick, and that's the, that's the special sauce right there. We can pick out all your individual appliances, uh, from just those connections. And it's, it's kind of like, it's kind of like pulling, uh, like, like a fire hose of energy and teasing out each individual appliances usage from that.

**Joe Bamberg:** Yeah. The way I was thinking about is if you had 10 people on a phone call and one of them was a crazy Australian, like my co-host and you knew his accent, you would be able to say, Oh, I can tell on Dave speaking because of his accent. Right. So like how, how he vocalizes words. There's ways that, uh, different devices in your house vocalize their power usage.

**Joe Bamberg:** Is that a good way to think of it? That's a fantastic analogy. And it's actually even closer than you could possibly even know.

**Joe Bamberg:** It's because it's using like, yeah, that's right. Cause you guys, uh, let's see the founders. I was reading the founders were doing something like that, right? Yeah.

**Joe Bamberg:** So the, um, the founders, uh, the, the guy that's our CEO, Mike Phillip, this is the third company he's founded. And the first two, um, were, uh, were both speech recognition. And it turns out that the, uh, the problem of energy, energy disaggregation is very similar to speech recognition.

**Joe Bamberg:** Right. So Joe, Joe is saying Mike Phillip is a one trick pony. You heard it here first. Joe just lost his job. It's, it's crazy.

**Joe Bamberg:** You know, I, I, I think he would, uh, agree.

**Joe Bamberg:** No, that's great. That's, that's, if you're going to have one trick, that's a hell of a trick, you know? Seriously.

**Joe Bamberg:** And if you, if you're, if your trick is applicable in a lot of different domains. Yeah, exactly.

**Joe Bamberg:** That's great. So, um, so, so, okay. So we were talking a little bit about architecture before as well. So you were saying that ADI does stuff where all that stuff is built in with, you know, fixed DSP, fixed digital signal processing. You know, the filters are in hardware, stuff like that. Fixed function DSP blocks. Right. So I assume now that this is more, uh, translated from, you know, from physical things to bits and then throw it into the machine and then you have lots of processing on it. Is that a safe, a safe assumption? Yes, that is the safe assumption.

**Joe Bamberg:** So the issue with, um, the like fixed function DSP method, the, the, your conventional smart meters, whether it's, um, it's the analog devices or microchip or TI, or they all, they all have variants of the, of the same thing now that you're, it's basically plug and play energy meter. The problem is, uh, the bandwidth that those, those things use. So they're in general, they're somewhere between, uh, a three and six kilohertz bandwidth. And we, uh, we, you guys do 44.1 K, huh? We do up to, um, a mega sample a second. Okay.

**Joe Bamberg:** Great.

**Joe Bamberg:** So, and, and, and in order to do that disaggregation, to be able to see the, the signatures of all the different appliances, you need that, that bandwidth. It's the, the three to six kilohertz is just doesn't give you the resolution that you, that you need to kind of do this, uh, this disaggregation.

**Joe Bamberg:** Okay. So, well, let's talk about the front. So obviously there's a front end here as well. So then, uh, does that significantly change the front end or is it similar like just like PGA is and, and scaling for different, uh, you know, some houses are more powerful than others kind of thing?

**Joe Bamberg:** No, no. No, the, the, the, the front end is, um, is, is, is pretty much the same. So we do this at, we divide down the voltage, uh, to, to look at the voltage and then we use CTs to, to, to look at the current. Okay. Um, no, no significant differences. A little, there's a little, uh, uh, a little signal conditioning going into the, uh, A to

**Joe Bamberg:** Ds, but cleaning up the, the, the buzzy power, right?

**Joe Bamberg:** Or the, yeah, it's, uh, there's nothing, um, earth shattering, earth shattering. Our hardware is, uh, it's just a way to get bits, you know, it's a, it's a means to an end. Like, like, like I said, the special sauce really is in the, uh, in the, in the, in the software.

**Joe Bamberg:** Okay. Interesting.

**Joe Bamberg:** We're a software company that just happens to have some hardware.

**Joe Bamberg:** Right. Yeah. Startups these days are, yeah. Software, but software wrapped in plastic is the phrase that I keep hearing. Yeah. No, that's a very apt description of us. Okay. And so how much of that is happening? Uh, so, I mean, obviously there's different ways that you could do this. How much of that happens directly on, in the, in encased piece of plastic, right? So is it like an FPGA in there? Is it a micro? Is it a full Linux box or what?

**Joe Bamberg:** It's, it's actually, um, a majority of the, the, uh, the processing happens at the edge. So in the box.

**Joe Bamberg:** Okay.

**Joe Bamberg:** Great. We, uh, we have a, it's an IMX seven. Okay. Oh yeah. Nice. Do core one gigahertz. We run a, we run a full Linux box on it.

**Joe Bamberg:** Uh huh. Nice. Which distro are not allowed to say?

**Joe Bamberg:** Uh, we roll our own actually.

**Joe Bamberg:** Okay. Yeah. That makes sense. I mean like, so, but you said full Linux too. So it's got like memory management and all that stuff. It's not doing like, it's not like, um, micro Linux or no, that's not the right one. What am I thinking? Like, like, uh, like an RTOS. It's actually full Linux.

**Joe Bamberg:** No, no, it's not, it's not a, it's not a RTOS. We're not strictly real time, but we're very close to real time.

**Joe Bamberg:** Right. So what I'm hearing here is that you have data scientists and like, I need Python on, on this device. Is that, is that a fair, fair assessment? Yeah.

**Joe Bamberg:** We have, we have, uh, I mean, data scientist is like the biggest. Like component of our company. I think we have, we have 10 or 12 data scientists right now.

**Joe Bamberg:** That's cool.

**Joe Bamberg:** Um, so, hmm.

**Joe Bamberg:** Interesting. So how, how much, how much then does this box need to have regular software updates? Like from, so like it's connected through wifi, uh, from, from a company level, you're like, okay, well, we're going from version 1.6 to 1.7. And then you push these big software updates to each box.

**Joe Bamberg:** Oh yeah. We, I mean, we software update, um, weekly, if not. Oh, great. Okay. Like every couple of weeks, but like weekly is standard because so our mod, basically what happens is, um, we have models, uh, for like different appliances, right? Mm-hmm. Yep. And when the, the monitor first gets installed in, in your house, they have very general models on it. So a very generalized refrigerator model, a very generalized, um, uh, washer model. And as it, once it's installed and it starts observing your electricity, it, the models start to get tailored to your individual, uh, individual appliances. And so those models get updated fairly regularly. Uh, additionally, when we figure out ways to discover new types of appliances, like we push those models to all the units. So yeah, that it gets updated, uh, updated constantly.

**Joe Bamberg:** Interesting. Yeah. So I was wondering about that too. So, so a lot of it, I can imagine that, you know, my brand of fridge has a certain ka-chunk whenever the compressor kicks on. And I, I get that that looks like a certain waveform. That's probably pretty unique, but why not just wait until my fridge turns on and then like press a button and like say, Oh, my fridge just turned on.

**Joe Bamberg:** You know, we, um, uh, at the, like a couple of years ago, very first, uh, we thought about doing that and we actually implemented that in a, in a couple of homes and it was just, it was so tedious and you, you don't want the end user to have to put that much effort into it because it's a, it's a turnoff to some people or they do it in an incorrect manner. So then you have data or it's always just better if, uh, if you can do it on your own. Um, now we've, we've recently introduced a, a feature where, um, so there's certain things that, that look a lot like each other and, and to help the learning process, uh, when sense discovers something that it's not quite sure of now, what it'll do is that it'll give you some options and it'll say, Hey, we think this is either a, uh, one, two or three and with a certain probability. So we think it could be 50% this, or it might be 30% this, or it might be 20% this one and allow you to identify it then. But, um, so it's kind of like that, but you don't, you, we didn't want to do a, because we tried and it just didn't work all that well is that, Hey, go around, flip this, turn this on. Hey, what is it? Okay. Now label it. Yeah. That's just not right.

**Joe Bamberg:** I kind of think about this, like, so this, this piece of like the classification too. So I use like mint.com just for like tracking finances. And it's like, it sounds kind of like that too, where like I go to, uh, you know, Bubba's car wash and it doesn't know what Bubba's car wash is and it tries and it says, you went to bubbles and beyond and no, sorry, man, I didn't go to bubbles and beyond, but I can go and fix it. And then it, it kind of learns that and pushes it back to the system. Um, so it sounds kind of like that as well, where you're, you're doing the, the, the final five, 10% is, is human interaction, but it's most of the time, you know, it's going to figure out chase bank pulling money out is like my credit card payment. Right. So exactly. Yeah.

**Joe Bamberg:** Well, I mean, in most of the, you know, most things we can identify on our own, but there are certain things that kind of look similar to each other. And it just, as a, as opposed to getting like, uh, like incorrect labels on, on things that it, it kind of helps separate that out, you know?

**Joe Bamberg:** Yeah, of course. So that brings me to my next question. So the same question that, you know, family members asked me, they're like, what the hell are you using this for? Right. So why am I actually using mint.com? What are people using this for? Why, why do I, why does anyone need this? Give me the pitch. Okay.

**Joe Bamberg:** So, you know, that's, um, the, the obvious use case, which is the, the least interesting is, uh, uh, like energy monitoring and, uh, energy efficiency. See, it's like, yeah, we, we've kind of found that people, uh, people install scents and they, they're like, oh, this is how much my toaster is using. This is how much whatever. And, and that, that, that, that shininess wears off after two weeks. And I was like, yeah, I don't really care that much.

**Joe Bamberg:** Right. They say it at the first cocktail party, but not the second cocktail party. Yeah, exactly. Oh, I'm monitoring my energy now.

**Joe Bamberg:** The more interesting use cases are, um, uh, thing, situations like, oh, hey, you left your, we send a push notification. Your iron has been on for three hours. Did you mean to leave your iron on? Oh, okay. Oh. That's legit.

**Joe Bamberg:** Yeah.

**Joe Bamberg:** Hey, did I leave my oven on? I can't remember. You look at the, your, your phone on the app and like, no, the oven's off. Okay, good. Okay.

**Joe Bamberg:** So it's a little bit of FUD, you know, like fear, uncertainty, doubt, like, of like, oh, safe, you know, kind of like safety and that kind of thing. Right.

**Joe Bamberg:** Yeah. So we, uh, we could do things like, Hey, you're, you're on vacation. Your garage door just opened. You might want to have somebody check that out or your sump pumps just started firing. You might want to have, uh, which actually happened to, uh, to Mike, the CEO. He was, uh, away on vacation and all of a sudden his sump pump started, uh, started tripping and he had the, uh, the water company cut the water to his house and it turns out his basement had been flooding. Okay. That's, that's legit.

**Joe Bamberg:** Yeah. That's, that's good.

**Joe Bamberg:** Yeah. People with a second home that want to keep tabs on it or, um, now we know, now we know your target audience, people with money and, uh, you know, we get, um, we get users all the time writing in to tell us about things that happened to them. So, uh, like one person, I had, uh, this like, uh, weird, uh, water pump issue that the pump was not I, me, but the, in the, the user's voice and it was costing them like, uh, a hundred bucks a month. They said, they found this and cents paid for itself in the first month. Oh, nice. The, the, the funniest one that, that I've heard so far is that there's somebody that was, um, renting their, their place out on Airbnb and, and they found that, um, they installed sense and they noticed after somebody would leave, the cleaning people would come and then like the TV and the lights and stuff would be on all night. And they were finding that the people cleaning the house were staying over in their, in their Airbnb when it wasn't, when it wasn't booked for the next day.

**Joe Bamberg:** Wow.

**Joe Bamberg:** And they, they found that through, through sentence. They're like, wait, why is the TV on and all? Okay.

**Joe Bamberg:** That's the, that's the best one I've heard so far. That's, that's a good one. Um, yeah, that's kind of creepy actually. Um, okay. So that's a little bit, right? Yeah. That's that, that's, that is great use cases then. I was thinking it was mostly like, you know, oh, I want to know because, okay. It sounds bad, but like power is not that expensive, at least in the States. I mean, yes. You know, you talked to, so, so Dave, obviously he's in Australia, but he pays a lot cause he, him and his wife also pay for green energy credits, which is great, blah, blah, blah. But like, it's expensive there. Like power is, is rather expensive there and now they have solar. Right. So, but in the States it's like, what? I don't, I don't even look at my power bill anymore. Right. It's just like, I, obviously I'm also in an apartment. And so I understand that like, you know, people with like teenagers running hair dryers and, you know, and gadgets and whatever, like that, that's another thing that gets real expensive. But for me, it's, it seems cheap. So this doesn't, that didn't really play into my mind until you said this stuff.

**Joe Bamberg:** Yeah. It's, um, it's, you know, like I said, it's like the non-intuitive use cases that are more interesting. It's like, uh, Hey, since how many, how many hours of TV did I, did I watch last week? You know, and you want, send me an alert after I've watched 10 hours of TV. I want to reduce my TV consumption.

**Joe Bamberg:** Okay. Yeah.

**Joe Bamberg:** That's good.

**Joe Bamberg:** I guess it's one of those things. If you're, if you're not measuring it, it doesn't exist kind of thing. Huh? Exactly. Yeah. Okay. That's, that's good. That's good. So I mentioned solar, uh, you have a separate version for solar. Why?

**Joe Bamberg:** Why is that? So it's not, um, I mean, it's the same unit. It's just you, we, we ship a, an extra set of CTs with it and you can monitor your solar usage as well. So you can see how much, how much of your, how much solar you're generating versus how much of your own solar you're consuming and compared to how much energy you're using from the grid.

**Joe Bamberg:** Okay. Cool. Uh, okay. So now, now it's time for the question about for all of our, uh, privacy freak out there. Uh, where, where's all this data going?

**Joe Bamberg:** Uh, it's nowhere. Are we, that's, that's one of the, the big issues that we really wanted to, to do right. And if you, we have a very clear privacy statement on our website and we, we don't do anything with anybody's data without per, without their permission.

**Joe Bamberg:** Okay.

**Joe Bamberg:** So to the fact that like nobody inside the company, I can't go look at anybody's data in there. There's only. Yeah, I get that.

**Joe Bamberg:** It's all anonymized, all that stuff. What, but, but I guess the main thing is, so, you know, I hope you guys are successful. But, you know, our favorite internet of shit, um, uh, Twitter account, uh, what happens if you guys go away? I guess that's the real question. Is it like, is it like centralized server? So like, so the app, where, where does, where does the app talk to? Is it, is it my server? Is it your server? Is it, you know, an AWS instance? Like where, can I keep it going without you? Yeah.

**Joe Bamberg:** Uh, I mean, you know, you know, I don't actually, as far as the data strategy goes, that's not something that I like to be perfectly honest that I don't have any input on that. Um, I, I do know that the, the guys that are in charge of that are very, very conscious. Oh no, I made Joe uncomfortable. And data. No, no, no. I, I, I, to be honest, I don't have the, the, the, well, here's a, here is a product suggestion

**Joe Bamberg:** because, you know, who doesn't love a unsolicited product suggestion? One thing that you guys promote is no subscription fees. That's great actually. But if you had like a five bucks per month, uh, my own private cloud thing. Yeah. That'd be interesting as well. So, uh, you know, just because it is, I mean, it is centralized, right? That is, that is the downside to any, like, so this, you know, you've made a case that this is actually very useful, uh, but it is also controlled by you. So that, that's the downside, right? Or, or have like a really expensive version where it gets served up directly from the device onto my wifi network, right? Cause it's all this stuff. So like what happens if, so this is going back to a server somewhere and then it gets pushed down to a, an app, right? So there's no way to do local, like my, the sense is on my wifi network. My phone connects to my wifi network. It talks to, you know, a local IP. There's nothing like that, right?

**Joe Bamberg:** Yeah, no, there, I mean, there's too much, um, like processing that, that needs to, to go on. So a lot of the processing happens on board, but then you need to, all the data needs to be stored and, and it's just, it's a lot of data. So we can handle, if you have a, if your wifi goes out, we have enough, uh, enough memory on board where we can capture about eight hours worth of energy usage before data starts getting lost. Really?

**Joe Bamberg:** Oh, interesting. Okay. So like, so that's still pretty raw though. So yeah.

**Joe Bamberg:** So we, if you are, if you're like wifi goes out or something happens to your cable connection, we can cap, we can continue to capture about eight hours worth of your usage before we start to lose stuff.

**Joe Bamberg:** Okay. Yeah. And so this kind of goes back to the edge processing that you mentioned. So I actually didn't know this term until a couple months ago. Uh, so you, when you say edge processing, what do you mean by that?

**Joe Bamberg:** So that, that means we're doing like, it's not, we're not taking raw data and throwing it up to the cloud and processing in the cloud. The, um, most of the, the processing happens in the box and, uh, we are sending, um, uh, what we, what basically what we call events up to the cloud. So the processing on the, uh, on the, uh, on the monitor looks for events and then we send those events up to, uh, up to the cloud. Got it.

**Joe Bamberg:** And then, then that does the aggregation and all that stuff of like,

**Joe Bamberg:** but all the, all the models, all the machine learning, all that, the neural nets and stuff, those are running on, on the monitor.

**Joe Bamberg:** Right. Yeah. I kind of think about it kind of like, uh, like a stochastic, the looking at like, uh, how close to a certain shape it is. Is that kind of a good way to think about it? So if a compressor on a fridge looks like a spike and then like a trail off, you look for a spike in a trail off and you say, yeah, this is like 70% likely that this is a spike in a trail off.

**Joe Bamberg:** Yeah. So, I mean, we look at things both in the time domain and in the frequency domain.

**Joe Bamberg:** Oh, cool. Okay.

**Joe Bamberg:** So we look at, um, so for example, uh, like, so like a heater, like something with a compressor and then a fan or we, we could see, okay, the compressor comes on and then 10 seconds later, a fan comes on. Um, when the compressor comes on, there's this big of an inrush current, it averages this much wattage. And, um, and, and so like all those factors together, like the, the power, the duration and, uh, the order in which things happens, those help us kind of get a fingerprint of it. On top of that, we also look, um, frequency domain. So what kind of, uh, like this is at a, a 20 kilohertz. This is at a 30 kilohertz. This, this blip. Um, and we do use a, like to kind of look at, uh, like frequency information over time for, for, for different things. Cool.

**Joe Bamberg:** That's great. Uh, is that all done? Is that FFT done internally or in hardware or in software? No, it's done in software. Okay. And so what about, I guess this also kind of comes back to the other question I was going to get to. How do you power this thing? Is it just drawing off those power? Yeah.

**Joe Bamberg:** It's, it's just, it's, uh, we just are connected to the, to the line and we, uh, we pull right from there.

**Joe Bamberg:** Okay. And then you just internally just do like a, like a module, like 120 to five volts or something like that. Yeah. And so I, it's funny, I actually did the design on that. It's a, it's just a isolated flyback. Okay. Oh, great. Yeah. So you're not, I've seen ones with like the modules recently because like modules for me, they're so simple. And I'm, to be honest, I'm still scared of AC wall power. Uh, yeah, I probably shouldn't be, but I still am.

**Joe Bamberg:** And, uh, so the, the problem with, with modules is one, they're expensive and two, they just, their, their footprint is just too big. We have a, we're pretty, we're space constrained with like being able to fit in the panel with like, I mean, I'm sure you've seen some pictures of people's panels with like wires. There's not a ton of space for things. And stuff like that. So, um, yeah, let's do it both, uh, both price and, um, and an air footprint area. Uh, we just want to have our own flyback.

**Joe Bamberg:** Um, that's great. Yeah. Yeah. So, uh, I guess that kind of comes to another question is what about, uh, are there regulations for being in a power box? Like, uh, like NEC, like natural electric code? Yeah.

**Joe Bamberg:** Yep. There, there are. And, um, we, we, we follow them all.

**Joe Bamberg:** So, so what are, I don't actually know any of these, these things.

**Joe Bamberg:** So, I mean, it's, do you have about 15 hours? Yeah. It's, uh. Welcome to the amp hour after dark. Seriously, right?

**Joe Bamberg:** Co-hosted with Joe.

**Joe Bamberg:** Start playing some jazz in the background. Nothing more exciting than 1am NEC discussions.

**Joe Bamberg:** Yeah.

**Joe Bamberg:** Wow. So what is it?

**Joe Bamberg:** Like.

**Joe Bamberg:** So, I mean, it has to do with like sizes of conductors in the raceway and what kind of CTs you can use and double insulation and all these kinds of things. So not only do we have to deal with the NEC, but we also have to deal with like UL rules and we have to deal with FCC rules and we have to deal with, um, like CE. So we're like threading all those needles because we're, uh, I mean, we intend to sell into Europe and not just North America. So we have to, we make sure we comply. So not only do we do the FCC, but we also meet the CISPR rules too for emissions and, uh, because we were on a, just laying all that groundwork. And are you selling into Europe yet or no? We are not selling in Europe yet. We actually just started shipping to Canada and we have a, we have a, we have some trials going on worldwide right now, some pilots.

**Joe Bamberg:** So, um, so what, what changes, I guess, I don't even know, like I kind of alluded to this at the beginning. I don't, I don't even know though, what, um, what their power boxes look like. Are they different? Are they much different or no?

**Joe Bamberg:** They, um, so one of the big things is, um, like whether they're meant to be installed indoors or outdoors. Oh, but there, but there's also, um, uh, like different countries and different regions have different like standards for panel design and things like that. So, um, it's, yeah, it's a, it, it gets, um, a little bit complicated, uh, trying to, like I said, trying to thread that needle. So you have to make, so you can use one, one design to meet all the standards. Yeah. I was going to say, you don't, you don't want to be having like a million different skews because that just becomes obnoxious to manage.

**Joe Bamberg:** How many times have you cursed the, uh, the initial plastics designer? You're like, if I just had two, two more square inches, it'd be so much easier.

**Joe Bamberg:** Yeah. You know, you know, what's funny is that, uh, that Bolt did help us do some of the plastic design. Yeah. Okay.

**Joe Bamberg:** Yeah. We love Bolt around here. Um, that's great. Yeah. They, they, uh, they, so wait, we, would you guys come out of the Bolt accelerator?

**Joe Bamberg:** So no. So Bolt actually invested some money. We never were part of their accelerator, but they invested some money in us in, uh, in our seed round.

**Joe Bamberg:** Hmm. Okay. That's great. Yeah. Um, and then invested some time too, apparently. I mean, it's a, you know, it's a nice design. It looks, it looks friendly. I think that's really important as well. Yeah.

**Joe Bamberg:** There's a couple of issues with it, but overall it's, it's pretty good.

**Joe Bamberg:** Yeah. I mean, yeah. Like anything. It's a design, right? Yeah. Uh, and it's, it's small. That's the main thing, right? I mean, it's, I don't know if there, so you said there's a lot of stuff going on in most electrical boxes, but like, is, is it, does it need to be that small? I mean, like, is it, are there times where people are like, uh, oh yeah, this, this just barely fit.

**Joe Bamberg:** No, there's definitely, yeah, there, there's a lot, uh, there is sometimes when things just barely fit. One of the issues that we're having, um, at a certain amount of installations in California uses a bus bar and our CTs, like some of the buttons just barely fit onto some of the bus bars. Interesting. And so what happens is if it's not closed all the way, that like causes some signal issues if the clamp isn't closed completely.

**Joe Bamberg:** Loops like being loops, right? Exactly. Yeah. Oh wow. Okay. Yeah. That, I guess then you would have, there's all these, all these standards of different boxes, whatever. Right. So. Yeah.

**Joe Bamberg:** But some, some, uh, some like boxes are much tighter. Like a, a box in an apartment is generally going to be smaller than somebody, something on your house. And, and if that, the electrician that wired it, uh, there was a, did it do a great job or was it careful? Like there's like wires everywhere. And so trying to cram something in there or if the, if the box is very shallow, then what can happen is once the, the CTs are connected, when you close the door, it kind of presses on the CT and cause them to open a little bit. So yeah, there are certain areas where it's space constrained. So the smaller we can make this, the better.

**Joe Bamberg:** Got it. Yeah. That's interesting. What about the install? Is it like, so if like my grandmother wanted to install one, would she install it?

**Joe Bamberg:** Um, so by law, we have to say an electrician should do it.

**Joe Bamberg:** Got it.

**Joe Bamberg:** Okay. It's very simple and anecdotally, I think a very good portion of our customers have installed it themselves. Yeah.

**Joe Bamberg:** I mean, I've, I've installed, uh, breakers myself, right? So I probably would feel comfortable enough doing it. Yes.

**Joe Bamberg:** I mean, if you've installed a breaker, I, you would, I would, would feel comfortable, I think installing this. But again, electrician has to do it according to our intertech UL certs.

**Joe Bamberg:** No, that makes sense. And the, I guess the main thing is, so you're not going to shut off power from the street, right? But you will probably turn off the main breaker, like the a hundred amp or service, whatever 200 amp service you have. And you'd be pretty much safe at that point. Right.

**Joe Bamberg:** Oh yeah. But I mean, it's meant to be installed without doing that. Oh really? But yeah, but you can, I mean, yes, you, you can turn off the main breaker. I'm a, I'm neurotic. No, I, and I, you know, most people, especially if you don't work with electricity on a daily basis, I mean, it's, I mean, it's definitely an area where it's better to be safe than sorry, especially if you're not comfortable with it. And, and a lot of people aren't. So, um, you know, it's not worth the, it, you know, it shutting power down to your house for five minutes is probably safer than if you're not comfortable with that kind of stuff.

**Joe Bamberg:** Yeah. Yep. Definitely. Interesting. Okay. So I, oh, that, I guess that was the question I was going to ask is the, uh, so in the, in the 240 case, do those power boxes like in Canada or elsewhere? I know Canada's not 240. Canada's not. But when you guys switch to 240, will it just be single voltage input or will you actually need to have two measurements of voltage? Like is there split phase?

**Joe Bamberg:** Well, it depends. So some places have two sides of 240. Some, um, it, it, it's amazing how unstandardized across the world. It is.

**Joe Bamberg:** Yeah. I've looked at that map before too, where like the, there's like a Wikipedia map where there's all the colors, but then they also have like the slashes of lines too for like, oh, this one's 50. This one's 60. Some countries do, but like Brazil does too. Right. And Japan does too. And it's like, but what, what was happening here? Yeah.

**Joe Bamberg:** But so we, uh, so our, the, the model, we just finished a, a rep or just released a new design. And, um, so this one, we just released a manufacturing and this can handle, uh, 120 to 240, 50 to 60. It can, so this can be installed anywhere in the, in the world and handle all those different situations. That's awesome.

**Joe Bamberg:** Wow. Okay. I like it. Uh, so what else should people know about this thing? I mean, we're starting to kind of run up on our time here, but, uh, what are you excited about for power mining for the future? I mean, where do you see it all going?

**Joe Bamberg:** Uh, you know, I, I think, um, eventually.

**Joe Bamberg:** Like I think we reached the peak. We're all good. Yeah. Just keep buying sense.

**Joe Bamberg:** Our capabilities are, I mean, it's going to be integrated directly into either your panel or into your electric meter. I mean, that's where it's headed. No. Uh, so one of the, one of the things is right now, um, uh, like utilities, they need to, they need to build, um, generating plants that can handle peak to load, peak load. Right. But, um, but right now you might hit peak load a couple of times, handful of times, like, you know, uh, mid August, everybody comes home from work and turns on their air conditioning or hitting peak load. Right. But the, the, the power plants need to be designed for that, but that you're never, they're never using. Right.

**Joe Bamberg:** That's a lot of excess capacity just for that one event. Right. Exactly.

**Joe Bamberg:** So I, one of the things that would be interesting is if, uh, and the other thing is nobody wants to engage with your utility. You don't care who your utility is.

**Joe Bamberg:** And yeah, it's not like a nice brand that you're like, Oh, I feel so warm and fuzzy about them. Yeah. Right. Nobody cares about national grid. Yeah. Right. Right. PG&E.

**Joe Bamberg:** And so, and they have no, no user or customer like visibility into how they're, how their customers are using energy or anything like that. So one of the interesting things could be where, you know, that where your, your power company incentivizes you to, Hey, you know what, if in the middle of August, you come home, if you turn your thermostat up a couple of degrees, we'll take, takes, uh, five cents a kilowatt hour off your, off your, your bill this month, you know, or, uh, Hey, if you run your dishwasher three hours later, we'll take a quarter off your electricity bill.

**Joe Bamberg:** So, you know, I've heard, I've heard that one for a long time too. And I just, again, it feels like it's not enough, not enough of an incentive. I'm sure that it is. Right.

**Joe Bamberg:** But it just, it feels like it's like, Oh yeah, no, that's a, that's the thing. It's you're right. You're completely right in that energy is cheap.

**Joe Bamberg:** So, um, so what we should do is raise energy prices and then all the, all the utilities go wild. I mean, yeah, I mean, it's a, it is, it's a touchy issue, I'm sure. And especially because it, I think the real thing is that, and what your product kind of touches on too, is that like, like I don't think about power until something's wrong. Right. And, and, and then you really notice it. Right. I mean, obviously the whole Puerto Rico thing, you know, there's people that are still hurting out there. Yeah. There have been months without power. And like, so it's, obviously it's, it's very front and center for them. And it's, you know, there's other people in other parts of the world that, where it's a very big deal, but like at this point, you know, most people are sitting around, not most people, probably most people listening at least are, are very lucky to have, you know, reliable power that you don't think about it. And so it's, uh, it's, it's interesting because this kind of plays on the whole convenience factor as well.

**Joe Bamberg:** Yeah. Yeah. I mean, I mean, it does. And, and, you know, it's like the big, I guess, like this advantage that sense gives you, it kind of lets you know what's going on with your house. Right. It's like, it's not so much, although it's an important fact, it's not how much energy I'm using. It's, Hey, did I, did I leave my iron on or did that? Like, did the kids get home from school? Oh yeah. I see the, the toaster went on the, uh, the, the microwave went on the bathroom lights went on or, or whatever. It kind of, it, it kind of, we can kind of make dumb up, add a little bit of intelligence to dumb appliances pretty much is kind of how you could say it, you know? And, and the, and the more people that use it, like we, we heavily, uh, take advantage of the network effect in that the more people that use it, the better our models get, which makes, makes us that much more useful, which makes more people want to use it. And, uh, and, uh, and like I said, it's those non-intuitive use cases that are the most interesting and, and who knows what, what else, where, what else we'll discover as far as ways that can be used.

**Joe Bamberg:** So you guys should do like a joint promotion with Amazon key, right? So yes, the Amazon delivery driver, you saw him get into your house, but yes, he's also still watching TV in your house. Oh my God, you couldn't pay me enough to use Amazon key. I'm sure that some people have a similar reaction to sense, to be honest, but yeah, the key is that's, that one is, I, I, very uncomfortable myself.

**Joe Bamberg:** So which is, which is, which is fair.

**Joe Bamberg:** I mean, you know, it's, it's a convenient, it's, it's really is this convenience versus security versus anything else, right? Those are, these are the trade-offs. Some people are going to make them, some people aren't, and that's fine, but it sounds like there's some significant conveniences from, from sense.

**Joe Bamberg:** Yeah. I mean, there are, and it's like, you're, you're absolutely correct. It is a, is it a trade-off? And, and I, I, so far we found most people, most of our customers have been, that's the trade-off they've been willing to make. I think it's much less invasive than a lot of other stuff out there, especially for the, the benefits that, that people have had from using it. But I mean, that's a, that's a, a decision left up to, your mileage may vary, right? Sure.

**Joe Bamberg:** Well, and I think, I think the, the non-contact piece of it, right? That's, that's what's really interesting. You're not, obviously you're not controlling light bulbs, but you're at least telling when they're on. And so it's like the, you know, I think you guys talk about smart home a lot, but it's, I think you, in your, your, your, you have smart home all over your site, but really it's just a, it's like smart home by proxy, right? It's not, you're not like actively controlling things and, you know, putting things like last week or two weeks ago, we were talking about, there was a light socket that was controlled, right? And then you installed that thing. It's like, oh, well that's, that's very invasive.

**Joe Bamberg:** I mean, on a, on our, on our roadmap, I think eventually we'd like to allow the users to be able to have some control and integrate with that. But as of right now, it's a, it's, it's like I said, we're adding a little bit of intelligence to dumb appliances. So you can kind of figure out what's going on. Right.

**Joe Bamberg:** And it's going to happen at an API level versus, you know, direct, like your electrical box talking to a socket, right? Or, or having a relay at the electrical box. So, yeah, cool.

**Joe Bamberg:** But yeah, it's a, it's, it's an interesting space.

**Joe Bamberg:** Yeah, no, this is great, man. So I appreciate you telling us all about it. I, I expect there will be other questions down in the comment section. Where can people find you though, online, if they have direct questions?

**Joe Bamberg:** Uh, so I, I like how, how we came across each other. Twitter is usually a good one. And I'm at the Joe Bamberg. The Joe Bamberg. The one and only. The, the one and only.

**Joe Bamberg:** Yeah.

**Joe Bamberg:** I think it's probably the best way to get ahold of me.

**Joe Bamberg:** Okay, great. Well, we will definitely post that. We'll post links to all of the, uh, well, sense pages and stuff like that. And some of the data sheets that you talked about. So Joe, thanks for being on. And, uh, we look forward to talk to you more about power in the future. Thanks for having me. That's a, this has been fun. All right. Talk to you soon. Okay. Take care.
