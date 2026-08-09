---
episode: 583
title: The Smart Grid with Paul Zawada
url: https://theamphour.com/583-the-smart-grid-with-paul-zawada/
---

**Paul Zawada:** This is The Amp Hour Podcast. Released March 27th, 2022. Episode 583, sponsored by Mauser Electronics. The Smart Grid with Paul Zawada.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Paul Zawada:** And I'm Paul Zawada with Syntonis LLC. Oh, Paul. Thanks, Paul, for joining us. Hey. I am honored to be here. I've been a longtime fan of you guys, so I'm happy to join you and share a little bit on power.

**Dave Jones:** How much have you been pulling your hair out over the years as we talk about, as we attempt to discuss power stuff?

**Paul Zawada:** There might have been a little bit of yelling back to the podcast, but not too much.

**Paul Zawada:** I think it's also a measure of how little we know and how interested we are in this space. So this all came up. We were talking about Smart Grid a couple episodes ago. Yeah. And Paul wrote in and said, actually, I can tell you about this stuff. And Dave and I are both like, well, we got to both be there. Of course. Yeah.

**Dave Jones:** Yeah. When was the last time we did a three-way with the two of us? I think 2016, maybe. I don't know.

**Paul Zawada:** I guess usually Kaiser Miss is the main one. Yeah.

**Dave Jones:** That's it. Yeah. We do that once a year. Yeah. Anyway, so you're going to tell us all about power because us regular EE dummies, EE is not electrical, it's electronics. So basically we know that there's this thing on the wall where power comes out of and there's like- Yeah. It looks different where Dave is than where I am too. Yeah. It does look a little different over there. Like a scream mask, our one. Yeah. Right. And then there's like these transmission-y line things and then there's like spinny things at the end of those. So that's probably, and there's big transformery things. Yeah. So that's probably the limited of our-

**Paul Zawada:** Yeah. So to give you a little information on my background, I am not a hardcore power engineer. So my background originally was in telecommunications, but I became what some people call an operational technology engineer. And operational technology is kind of that computing and communication stuff that gets wired to the physical devices. And it could be in the power industry or transportation or pipelines or what have you. But it's that combination of maybe that hardcore, those big alien things that you guys were talking about last time in the substation yard. And then merging of that stuff with the electronics that have things like embedded systems and network connections and that kind of thing. So that's kind of my area.

**Paul Zawada:** Measurement. And so- Yeah, that makes sense.

**Paul Zawada:** In my work, what I do is I spend a lot of time explaining technology stuff to power people and power stuff to technology people. So I kind of felt that that's one of the reasons I wrote in is because I really felt that that's kind of my niche is sort of straddling that border.

**Paul Zawada:** So- We need you. How do those conversations normally go? Especially like, I'm curious because some of it, well, you're talking to dummies like us. We're going to be like, okay, yeah, megawatts or whatever. And the other direction too, is it kind of like a hard sell or are they excited about implementing new technology? Or is it more like, well, we've always done things this way. What is the appetite for new technology in the-

**Paul Zawada:** Yeah, it's interesting you mentioned that because I wouldn't say the appetite for new technology is not that great. We do adopt new technologies all the time in the utility industry, but once they latch onto something, trying to move that to something more current. So the way we do things, say in the SCADA world, for example, it's the same types of things we were doing 30 years ago. And so it's trying to move, say the power person that has been doing that thing the same way for 30 years is kind of difficult.

**Paul Zawada:** But- Just waiting for them to retire or-

**Paul Zawada:** Right. You're right. Otherwise. The other difficulty tends to be going in the other direction. You have IT people who know IT very well, but they don't necessarily understand the ramifications of say what happens when the network goes away. So in trying to explain how a blackout happens, for example. Right. And why that network service or that computing service that they're providing, why it is so critical to making sure the lights stay on.

**Dave Jones:** A lot of people are going to ask, well, how does a blackout happen? Because a lot of people, like that's something that actually affects all of us. And we don't necessarily understand it. Like, yeah, the grid gets overloaded or there's power shuffling around from state to state and there's load balancing and all that sort of jazz. Should we start there or should we, is there a particular order you want to take us through in terms of like learning this? Should we start with generation and then go through transmission or how do you want to do it?

**Paul Zawada:** I mean, that's a good place to start is, you know, you have in the utility industry, you, in the electric utility industry, you have generation, transmission and distribution. And generation is those bulk power plants, right? That are providing hundreds or some cases, thousands of megawatts of, of power into the system. Transmission is the, the long lines that get it from where those bulk power system to the, to where it's used. And, and I think they found out a long, long time ago, a hundred some years ago, that it's easier to transport coal by wire as, as they, they called it at the time, as opposed to, you know, they could, they could build power plants close to coal mines or close to large bodies of water. Like in the cases like nuclear, you need, you need cooling water and that kind of thing. So, and, and sometimes you don't necessarily want to put a nuclear plant in the middle of a large city either. So, so they have these transmission lines to bring the, the power from where it's more convenient to, to, to generate it to where it's actually needed.

**Dave Jones:** Is there any limit on that, on the length of those these days? Cause we've got a, you know, a 1200 kilometer line from Australia to Singapore, for example, is there, are we getting better at like, like everyone says, Oh, Australia has so much renewable energy. Why don't you just put one big solar farm in the middle of Australia and then farm it out to the, you know, the cities on the edges of Australia. And I'm thinking, well, that's a bit lossy.

**Paul Zawada:** Well, you can, you have limits in two ways, right? You can have distance, which the way you deal with that in terms of loss is you raise the voltage. So higher the voltage, the less current you send through the wire, the less, you know, I squared R losses current, you know, power, you know, consumed by the wire itself, resistance of the wire itself. And so today, most of that transmission for the really long distances are, is in the 500 to a thousand kilovolt range that that's referred to as extra high voltage as opposed to the high voltage, which is considered like a hundred kilovolts to 500 kilovolts. Only a hundred kilovolts. Yeah. Oh, yay. So, and mostly the, the, the, the, the one, the one meg megavolt system, the thousand kilovolt system, uh, those are mostly in China and Russia. I believe we don't have any of those in the U S in the U S in the U S it tops out at, uh, at 765 kilovolts. And then, but if you look at China, you know, China is as much bigger country in terms of, especially where they're bringing power, they're transporting power for further distances than typically we do in the U S. Uh, and, and as you might know,

**Paul Zawada:** They have a newer grid as well, right? I mean, that's kind of like they've, oh, yeah, I'm sure there's some of their tooling is a little bit newer so they could maybe push that a little bit more.

**Paul Zawada:** Yes. They have, they have been spending a lot of money and they've built up quite, quite a grid and they're running into some of the scaling limits that we have not run into to yet. Be interesting what they learn in terms of building the, these large ultra high voltage networks and, and operating them. But then of course the other limit is, is how much can you carry on one line? You know, you can only can make the conductor so big. So if you put all of your generations, let's say in the middle of Australia, you would have to run a lot of, of transmission lines and, and I'm not sure if you want to concentrate all of those in one place either. Right. Because if I'm not sure what you have in terms of storms or whatever, but you know, you want to diversify where your, your generation is as well.

**Paul Zawada:** So yeah, they have a spider storms down there. Sharknado is that sort of thing. Yeah. Everything that messes a weather with a terrible, terrible animals is Australia. Job bears.

**Paul Zawada:** So then once you get to the, say the city or the neighborhood, you, you, you have a, a distribution substation that subs, that steps down the voltage. So you may have gone a long distance, say 500 kilovolts, stepped it down to say 138 kilovolts for say a network around a city. And then those individual 138 kilovolt stations may drop it down to a distribution voltage of, of say 13 kilovolts. Mm-hmm.

**Dave Jones:** And for those who want to identify these as they're driving around, you can just tell by the number of spaces, can't you? Like the number of ceramic spaces. So can you give us like a ballpark number? Yeah. We call it counting the bells. And counting the bells. Okay. Yeah. Right.

**Paul Zawada:** Because a lot of times the insulators look like bells, you know, especially the suspension insulators. Yep. Yeah. So I think the rule of thumb is like 15 kV per bell, if I remember correctly. That's what I thought it was.

**Dave Jones:** I thought it was, yeah, 10 or 15, something like that.

**Paul Zawada:** So if you see, and generally the towers for EHV are much bigger because you want to get those conductors higher off the ground. Right. And reduce the electric fields. Because if you stand under a 500 or a 765 kV line, you know, the weather's right. I mean, you'll get a static shock from touching a car or a truck or something underneath it. Oh, wow. So they have to limit the E field as well.

**Dave Jones:** How much power is lost in that versus I squared R losses? Because we're only talking about 50 hertz, right?

**Paul Zawada:** Or 60. 60 in the US.

**Dave Jones:** Oh, well, 60. Yeah, yeah. Weird, weird, weird yanks. Okay. Yep.

**Paul Zawada:** Off the top of my head, I don't know. I couldn't tell you how many, say, megawatts is lost on a, you know, a 500 kV line, but it's pretty low. I mean, you're not losing, you know, enough to negate, say, a power plant or even a fraction of one. It's pretty low. So, but again, as you get closer, you drop the voltage down. So when you get to the distribution lines, you know, typically a lot of times you see like the mushroom size insulator. And those are pretty small. And although you can tell the difference, at least if you look at them enough, you can tell the difference between, say, a 13 kV line and a 34 kV line because the insulator is big enough. You can kind of visually tell it's a bigger insulator.

**Dave Jones:** Right. So it's actually physically wider so that it has a longer surface path to go over.

**Paul Zawada:** Right. And a lot of times, you know, they, we talked about the alien shapes is, you know, a lot of that is about trying to provide more surface area. So if the insulator gets contaminated, you're not going to have flashover. And so sometimes you get the, they, they have weird shapes or if, if you look underneath the insulator, you'll see that there's what they call a petticoat where. Yes.

**Dave Jones:** The little ridges, little.

**Paul Zawada:** Yeah. Yeah. So that way it, you know, well, one, the water drips off before, you know, the whole surface gets wet. And, but two, it, it reduces it or at least increases the amount of area that has to become contaminated. But even in like in some areas, like coastal areas where you have salt spray, sometimes they do have to, to shut things off and just hose it down with, with distilled water just to, to get all the salt and contamination off, off the equipment.

**Dave Jones:** Ah, that's something I never thought about. Yeah. When you get close to the, close to the ocean, salt water spray gets into everything.

**Paul Zawada:** Mm-hmm.

**Paul Zawada:** Mm. Yeah. So in, in this chain from, you know, generation all the way to home delivery, that sort of thing, you know, one of the, we, we had referred to this, this video about the Ohio Eastern seaboard shutoff. And you and I were talking about that a little bit before we recorded Paul, but like it shows some of the, you know, like breakers and where, you know, how things failed and stuff like that. But like, what are, when you think about the control of quote unquote, the grid, right? You know, it's, it's this big singular thing as is often discussed. Where does, where do those control points happen that, that you think about?

**Paul Zawada:** So, well, first of all, I think the thing to remember, and I think it's true in Australia, but in the U S there's, there's multiple, not only are there multiple grids, but there's multiple entities that control different parts of those grids. So a lot of the control is happening at the, at those control centers, whether they're sometimes are nonprofit control entities like a company called, or an entity called PJM in, in the, in the Eastern U S sometimes they're, they're still controlled by utilities. A lot of times those are called balancing authorities because they had, they ensure that the balance of generation is matching the, the load that's taking place. So they control at sort of a, at a high level. And then the fine grain sort of minute by minute control of the power being delivered or generated, I should say, is actually done in, in a control system for whatever type of generator it is, whether it's a steam turbine or a, or a wind turbine or, or solar inverter. There is a, there is a bit of a feedback loop in there that sort of, so that generator tracks, it tracks frequency of the grid. So I was explaining earlier that to, to Chris, that the frequency is what determines if you have enough generation or not. And, and Dave, I, I was one of the things I was yelling back at you a couple weeks ago. Just one, Paul, come on. You can be honest. It's fine.

**Paul Zawada:** Just one.

**Paul Zawada:** You mentioned how there was a lot of solar coming on the grid in. Yes. In, in Australia. And it was driving the voltage up. Right. No, it's driving, it's driving the frequency up.

**Dave Jones:** Oh, the frequency up.

**Paul Zawada:** Yeah.

**Dave Jones:** Wow. Okay. I didn't see that coming.

**Paul Zawada:** What is the, what is the mechanism for that too? Is that because like, because of the things that's on our, Dave's garage that pushes it back into the grid?

**Dave Jones:** I know. Can I have a guess? Can I have a guess? Because, oh no, I was going to say. If you generate him more power, you have to spin it a little, maybe a little bit faster. And therefore the frequency is going to go up a little bit more, but that's opposite.

**Paul Zawada:** So think about the, the analogy that I like is think about you're riding a bike. Okay. And you're going down the road and everything. And, and all of a sudden you hit a hill and you're going to start. And so in other words, and that's like adding more load to the system. And what happens to your pedaling? You slow down, right? Yeah. Cause, cause all of a sudden you've got. And so if it's not too steep of a hill, you can, you can just pedal a little harder and you can sort of keep maintain that, that same rate. If it's really steep, you may start slowing and slowing and slowing. Well, then that's when you're in trouble, right? So it's the same thing with the grid. The individual generators, they can kind of track the frequency. And, and if more load comes on the system, you know, like if it's a steam turbine, there's probably a little more steam. They can open the steam valve a little bit and they get more steam and it compensates for that, that, that extra load that came on. At some point though, you can't, right? And so if all the generators, if, if say if one generator drops off somewhere and all of a sudden the, all the other generators around would have to pick it up, you're going to see a dip in frequency. And hopefully there's some spinning reserve somewhere that, that the, the, the grid operator can call upon to, to jump in and help the guys that are still left. And that's really, that's what happened with the Tesla battery in, in Australia. I think you guys talked about that a while ago, right?

**Dave Jones:** Yes.

**Paul Zawada:** Are we talking about the one that caught on fire? No, I don't know if it was, it wasn't the one that caught on fire. There was a large Tesla battery. Yes. The Hornsdale power, power reserve it's called. Right. And there was a massive power plant that, that dropped off. Yes. The grid and, and the Tesla battery was able to, to pick up the difference.

**Paul Zawada:** What happens then? Okay. So say we're living in, you know, sometime in the future and it was a, or maybe not even in the future. Say you're just living completely off grid and you, you have a community of like 1500 houses and you don't have a generator in the system. Then the same thing applies though. Right. It's, it's a, but it's just an all electric version of that. Cause we always talk about it in terms of generators, but like there, there's switching circuits in the, in these things and transformer drivers.

**Paul Zawada:** So that's the challenge as we move to, to a more solar and renewable grid that doesn't, does not rely on big spinning hunks of metal because the grid has what's called inertia. Right. And that's that, that whole concept, right. Where, you know, if, if a bunch of load comes on right away or a bunch of load comes on, things won't just stop right away because things keep spinning, but they will start to slow down. And the problem is, is with a lot of the inverter technologies, they don't have that inertia. So they're actually developing, you know, that's a sort of a research topic is the concept of what they're calling synthetic inertia. Oh, interesting. To deal with that problem and, and sort, you know, at some point you then you're, you're, you're keeping some, some of your energy on the side or you're not necessarily producing energy, but you somehow have to store that or keep it aside so that, that the, when you do have, you know, a disturbance like that, your inverters can compensate for that.

**Dave Jones:** Right.

**Paul Zawada:** A disturbance in the, uh, electromotive force. Exactly. Yeah.

**Dave Jones:** Disturbance in you. Oh, that has to be the name of this episode. Come on. The disturbance in the electromotive force. All right. Yes, please. Okay. But how does the voltage go up if you've got too much solar? Because the voltage definitely goes up when everyone's solar comes on line during the day and then, and then the voltage goes back down. You're saying it's frequency, but there is actually a correlation between, with voltage going up there. Or, or is that just.

**Paul Zawada:** Based on what I did.

**Dave Jones:** A coincidence. I've measured it. And other references I've looked at said, yes, the voltage can get near. In fact, solar inverters trip out because they reach their upper voltage limit because everyone's surrounding solar has come on online during a, you know, a really, you know, hot and sunny day. You know, we've got 30% of the population here. You have solar on their roofs and boom, the voltage goes up and these inverters trip out. How does that work? Or is that. Because I can't imagine that's not a thing because everyone says it's a thing and I've measured it myself.

**Paul Zawada:** Everyone says.

**Paul Zawada:** So this is where you're stretching the limits of my, my power engineer abilities, but I would, I would have to venture part, part of it is, is, is reduced losses in the system.

**Dave Jones:** Oh, okay. Right. That makes sense. Yep.

**Paul Zawada:** Because.

**Dave Jones:** Because it's coming from a more local source, which is everyone's surrounding roof. Correct. Right. So there's less losses directly.

**Paul Zawada:** Yeah. Although to some degree, well, it could also, the other thing, it could be that, that you don't have a terribly high inductive load in the, like in the morning when things are coming up.

**Dave Jones:** Mm-hmm.

**Paul Zawada:** Eventually I would venture to guess, I haven't looked at this myself, but one thing I would tell you to do is take a look like in the afternoon when things are getting really warm and see what the voltage is doing. Because at that point when, when everybody's air conditioner is kicking in and you're, and you're, you're introducing a heavy inductive component that your voltage is, is going to probably drop because of that. And that's the problem.

**Dave Jones:** Well, no, that's when it actually goes up. Curiously in peak afternoon sun, that's when it's, no, at about 6 PM or something like 5 or 6 PM, it starts to, it starts to peak and then taper off, which is interesting.

**Paul Zawada:** 5 or 6 PM is your peak solar? I would have said-

**Dave Jones:** No, no, no, no. Our peak solar would be like, you know, in summer, like, you know, 2 or 3 PM, but then it, it, it, it keeps rising. The voltage keeps rising and then it sort of tapers off around 7 PM, I think, something like that. Huh, because- I, I have to, so it's not entirely correlated. It's weird.

**Paul Zawada:** Like one of the issues they had, they've, they've had in Hawaii, which also has a very, very high solar- Oh yeah. Yeah. Penetration is that they, they have, and I, well, let's take a step back. Let's talk, I told Chris this was going to happen. We need to talk about the power triangle. Okay. Power triangle. Yeah. And so this is the, the concept of, you know, you know, people know power is, is voltage times current.

**Paul Zawada:** That's- Well, maybe we shouldn't assume that. Let's, you know, let's start from basics.

**Paul Zawada:** We'll start, but that's why I mentioned it. We're starting at the basic and especially in the DC power system. If you want to know what we, what we call power.

**Paul Zawada:** It's about where my knowledge starts and stops. Yeah.

**Paul Zawada:** We take the voltage and we multiply times the current. And so when we look at an AC system, when we say voltage or current, we're usually talking about the RMS, you know, a type of average of the voltage and current. So when we say it's 120 volts or 230 volts, that is peak to peak. The AC waveform is bigger than that. So if you're talking about a resistive load, in other words, no inductors or no capacitors, when you can still do that simple calculation, what happens is, is when you, when you introduce an inductive load, like an air conditioner, or you have something on the system that's capacitive, the phase angle between that voltage and current is going to shift, right? So it's no longer valid to just take an RMS value and multiply times the, one times the other. When you do that in an AC system, you have to take the angle between the two into account. And when you do that, you get something called the apparent power. But the parent power is not the power that's actually powering the whatever thing. If it's your air conditioner, which is a, is an inductive load. It's a combination of the power that's cooling your house, as well as some of the energy that is in the, the magnetic field of, of that compressor, of the motor.

**Dave Jones:** Which is lost, which is not doing useful work.

**Paul Zawada:** Is that correct? It's, but see, this is where, this is, this is why I want to talk about this is because it's not necessarily lost. You're true. It's true that it's, it's not doing. It has to be generated, right?

**Dave Jones:** It's got to be generated. Yes. Somebody's got to pay for that somewhere.

**Paul Zawada:** Well, exactly. And when we talk about the, the, and so that component of the energy going into that magnetic field, if it's a, if it's inductive load, if it's a capacitive load, it's the energy going into the elect, the electric field across the capacitor plates, right? Yep. That energy is actually stored and released constantly. And so, but what's, what's happening is, is I could, you know, some folks may have heard of Eli, the Iceman. Voltage leads current in a, in a, an inductive circuit and current leads voltage, I-C-E in a capacitive circuit.

**Dave Jones:** Here, here, we call that civil, C-I-V-I-L, and then current in, in, in, in an inductor, you know, voltage leads. Oh, that's, that's good. Yeah. Yeah.

**Paul Zawada:** I've not heard that one because it actually uses V because E is kind of like the old school symbol for, for voltage. Exactly. I have to remember civil. That is, that's excellent. Yep. Civil. Civil. So, yep. That's, that's how I thought. So anyway, so you have the, the component that is dealing with that energy, whether it's capacitive reactants or inductor reactants, that is what we call the reactive power component. And so if you draw a triangle, that apparent power, which was the, the, the, the voltage times current is going to be longer than the, the real power, which is, which is what your, your, your, your device is consuming. And then the reactive power is, is the short leg. So this is kind of hard to do without drawing it. Yeah.

**Dave Jones:** You've got to, you've got to have the visualization.

**Paul Zawada:** Yeah. I mean, I feel like the visualization is tough generally, but like, but some of it is, it's just like, because you're, when you're driving an inductive load, you have to put, you have to like, you have like startup costs, right? Isn't that kind of it? And then it's like getting stored in that magnetic field and then you can kind of harvest that later. Isn't that part of it? Like, it's just kind of time. It's time. Like it's like offset in time.

**Paul Zawada:** Correct. But, but so, so the energy is, is not lost per se, but it has, but your, your generator has to be able to, it has to compensate for, again, if it, if it, in, in, in 99% of the time you're going to, your load is going to be inductive. Typically only it's like weird industrial processes. Do you see like a capacitive load? But I think they, they do happen from time to time. But what happens is the, the, that reactive power, which was measured in volt ampere, we call them volt active, volt ampere reactive VARs. The VARs is what, what tends to control the voltage. The, the real power, like I was saying earlier, that is, that determines the frequency. And so when we look at Hawaii, what was happening in Hawaii, you have inverters that are producing, they're producing only watts. So they're only on that real part of the, the complex number plane that, that the, the real power lies on. They, they are not capable of providing, or at least if they are, many of them are set to only provide watts and not provide the VARs. So what we were seeing in, in Hawaii was they have entire neighborhoods where they have lots of watts. So they're exporting watts out of the neighborhood, but they're having to pull VARs from, from somewhere else. Interesting. Right.

**Paul Zawada:** And how, how would you actually import that then? Like, like, like, is it just a setting somewhere or is it someone else is just generate more?

**Paul Zawada:** There has to be a generator somewhere, somewhere that's, that's capable of lagging. It's, I'm sorry, leading its power factor to make up for the lagging power factor of the.

**Paul Zawada:** Does this mean somewhere there's like a, someone selling like a thing that just takes real power, stores it somewhere and then powers a generator with it again? Is that like a product that's on the market?

**Paul Zawada:** It's called a capacitor. Oh yeah, there we go.

**Dave Jones:** So if you had only, so if you had only real power generators, you couldn't power inductive loads?

**Paul Zawada:** Correct.

**Dave Jones:** Is that really?

**Paul Zawada:** That seems problematic in Hawaii where people want fridges and air conditioners and such.

**Paul Zawada:** That's, that's, that's. And, and so the way to think, but the way you think about that is, is the, it, it's like, it can't, it can't, it's, it's looking at like that, at that, that air conditioner as a short.

**Dave Jones:** Right.

**Paul Zawada:** And so as soon as it, because it's basically whatever it's trying to produce, it, it exceeds the capacity of the generator and the capacity of the generator, you know, essentially stops functioning.

**Dave Jones:** Wow. Wow. So what does a solar, what does my home solar inverter act as? Because it's essentially a generator. What type of generator is it? Or does it vary?

**Paul Zawada:** So, so most likely what you have, and I don't know for sure, but most likely what you have is what's called a grid following inverter. Yes. And it essentially functions, it follows the voltage and essentially is it, it functions as a current source. Okay. Right. And again, that's one of the challenges of the renewables is that we need more devices that have that synthetic inertia. Well, actually, so that's a different concept, but what would have inverters that have what's called dynamic response. And when you hear dynamic response in terms of an inverter, that means it can provide VARs. Got it. When called upon.

**Dave Jones:** When needed or real power if needed.

**Paul Zawada:** Right. And sometimes you'll, you'll hear of it. I don't know if you've heard the term before quadrant inverter.

**Dave Jones:** Yes.

**Paul Zawada:** So if you think about the power plane, which is a complex number plane, there's four, if you think about four quadrants, you have one quadrant where you're, you're supplying VARs and you're supplying Watts. You have another quadrant where you are supplying Watts and maybe absorbing VARs. And so, and again, that doesn't mean you're at your, your inverters actually sucking up power. When we talk about.

**Dave Jones:** Because that's what you, what, that's, what's implied by a four quadrant lab power supply, right? You can get a lab power supply. It's sourcing. I'm sourcing into that thing. Exactly. It's like a battery. It can like absorb energy back in. Yeah. Yeah. It can act like a load.

**Paul Zawada:** And so like a, like a four quadrant power supply for the lab, it can act like a, it can act like a real load or a resistive load, or it can act like a, it can have capacitive reactants or it can have inductive. So the four, four quadrant inverters, the same is the same type of thing. Right. And so most residential solar are not four quadrant inverters. Because of money? Well, I think it probably, it's probably because they're probably simpler to build. Yeah. Which in turn makes them money. Yeah. Yeah.

**Speaker ?:** Yeah.

**Paul Zawada:** I mean, even on the other side of when you're driving like an inverter like that, they're probably just like slamming IGPTs on and off. And then like with this big DC rail, right? I mean, that's probably how they're, I don't know. I've never looked actually. I should look. But yeah.

**Paul Zawada:** But, but basically when you get into trying to adjust things like power factor, you are talking about thyristor type circuits.

**Paul Zawada:** Ah, yeah. Yeah. So higher losses too, I'm sure. Right.

**Paul Zawada:** Yeah.

**Paul Zawada:** Not, not in the generation, but in like the, in the central circuitry. And probably stuff like that.

**Paul Zawada:** But, but one thing I want to make clear though, is like when we talk about the whole concept of, of having the power triangle, it's, it's to simplify the, the math or simplify the, the, the process of compensating, say for the inductive load. So it's easier to say if, since everything is operating at 60 Hertz or 50 Hertz, depending on, on where you are, it's easier to, to think in terms of supplying Watson or supplying VARs or absorbing VARs. And it is to actually always be doing the math to calculate the reactants and, and, and phase angles. If you break, you break things down into a real and imaginary component. And one thing you have to be careful of, you don't call it re-imaginary power to a power person because they may slap you. Because again, it has to be compensated for, but the, the idea behind the, the VAR component is adjusting, being able to, to adjust the phase difference between the voltage and current.

**Paul Zawada:** So what should we say to a, a power engineer is, let's talk about VARs instead.

**Paul Zawada:** You call it VARs or you call it reactive power, but don't call it imaginary power.

**Paul Zawada:** Don't call it imaginary. Right. Okay.

**Paul Zawada:** Noted.

**Paul Zawada:** This week, we're speaking once again with Paul Gulotta from Mauser Electronics. We're going to be talking about digital therapeutics and where they fit in with a modern medicine ecosystem.

**Chris Gammell:** I think we're familiar with digital health. This pandemic has caused us probably to be like, Hey, I can't show up at the doctor's office. Plus just our, our desire for convenience has made us want to get our health in a digital telehealth to make doctor visits. We collect information with our Fitbit, but we're talking about something different than that. You know, we can go in and let's say we have a glucose problem. We can digitally monitor that where I might get a piece of equipment from the doctor or buy it and check myself out and see what my numbers are and do certain actions. But this digital therapeutics is even beyond that. It's kind of really a subset of digital medicine. See this whole transition that we're making with technology, just pervading and invading our lives is giving us lots of things that we kind of didn't have before. You know, you've probably heard the famous expression, physician heal thyself. And kind of what this digital therapeutics is, you called out the difference between monitoring

**Paul Zawada:** and it seems like the monitoring might be the input, but the therapeutics is the output. Could you give us an example of what that, what an output would be? So like, what is the, what is the best case example of a therapeutic?

**Chris Gammell:** So this is being used for people, let's say with something like sleep is common. Things like asthma could be even with cancer patients, ADHD, and those types of things. Well, what they're going to be doing is using some type of software application. And again, often without any external hardware and then doing certain things based on something that's been tested in the software to help them actually treat themselves. So for example, you might have a software program. Let's talk about insomnia. These software applications will somehow help us monitor, not only monitor, but manage by doing some type of treatment where we go in and look at what we're supposed to do and then do these actions, so to speak, in the comfort of our home, maybe pre-bed or something like that of step one, step two, step three.

**Paul Zawada:** And this is almost by definition, it's non-medicinal, right? There's no chemical component. There's no pill that we're swallowing. It's just like actions that a doctor might give you in addition to some kind of other. That is correct.

**Chris Gammell:** And really, it's not only as a doctor giving it to you, but it's, if you will, the program or whatever the information behind that, which of course is put together by the medical community, but also, you know, software people and that type thing. So that when I wake up in the morning and maybe report if I had this many incidents or this is what happened or my Fitbit tracker, you know, recorded all my sleep, it will then tell me and indicate to me what I should be doing that next day so that if things are progressing or regressing, I get different actions of what I should be doing moving forward. And it's going, what am I trying to do in terms of behaviors based on the information that now might be stored in the cloud and how that has been combined with the wisdom of the medical community to provide me with the best actions? How can we make sure that these have good outcomes? All these things have clinical evidence.

**Paul Zawada:** Digital therapeutics have the potential to further extend the digital medicine ecosystem. And Mauser Electronics is covering this and other emerging technology topics. To learn more, go to theamphour.com slash digital health.

**Paul Zawada:** And now back to the show. So the idea behind these inverters has changed over time. So like the reason everything was grid following, like we were saying, was cheaper. But now we're getting into the point where we need more of that reactive power and being able to ride through disturbances with that synthetic inertia. And so if you look at the standard, there's a standard IEEE standard 1547 that deals with interconnecting inverters or actually any distributed resource to the grid.

**Dave Jones:** Can that be solved by government legislation saying, okay, the sales of solar inverters must be half of this type and half of this type? Is that possible?

**Paul Zawada:** Well, so this is where I'm going. So the 1547 standard originally said like in any sort of disturbance, drop off right away.

**Dave Jones:** Got it. Okay.

**Paul Zawada:** If it's changed, so now it's completely 180 degrees different where now the requirements for new 1547 inverters is that you have to be able to ride through some of these disturbances and you have to be able to deal with frequency changes and have the utility say, send you set points for the frequency. Because there's a phenomenon called the 50.2 Hertz problem. I don't know if you've heard of this. Do tell. So in Germany, and was it the 2005, 2007 timeframe? They had a lot of incentives for people to put solar in. So Germany, and you know how far North Germany is, has a lot of solar power. And when these inverters were produced and configured, they were all set to kick off, to disconnect themselves from the grid if the frequency reached 50.2 Hertz. So there were some incidents where there was much more solar generation on the grid that was needed and the frequency kept rising and it hits 50.2 Hertz. Well, it gets what happens. Everything dropped off. Well, what happens when everything drops off? You're in, yeah. It moves.

**Paul Zawada:** Wait, does it go up or go down then? Sorry. I've, I've.

**Paul Zawada:** So, so yeah, the frequency is going to drop, but, but more importantly, all you've lost all your generation. So now you're in a generation deficiency and you'd get these oscillations and oscillations, power flow oscillations in the grid are very bad.

**Dave Jones:** What, what talk, what, what frequency of oscillation we talking about? Cause I'm imagining this slow inertia of the generator slowly ramping up again. So I'm talking like subhertz.

**Paul Zawada:** Yeah. They're, you know, well, they're at least sub synchronous is the, is the phenomena. So sub synchronous being at your 50 or 60 Hertz. So you're going to have oscillations that are in, in the order of Hertz of power changing.

**Paul Zawada:** And, and what is, what is the, uh, what is the physical phenomenon that the badness of that happens? Is it like stuff start to blow out or do devices?

**Paul Zawada:** So, yeah. So you get into, you know, dynamics of the power grid and you get, you know, resonances and, and, and, and things like that. And again, you're pushing the limits of my power engineering skills, but that's, those are the types of things that they're looking for now in, in inverters. And I don't know of a government mandate that says you need to have so much dynamic, like voltage support in your inverter yet, but I'm, I think it's coming. And especially as we, again, we have fewer devices with large chunks of spinning metal providing the energy.

**Paul Zawada:** Yeah. So this brings us, this is why I said perfect, uh, before is I wanted to, I think this kind of gets right into the quote unquote smart grid, right?

**Dave Jones:** This is what we were talking about to mention smart grid. Yeah.

**Paul Zawada:** Yep. So now you had said the 1547, they're going to start sending set points and stuff like that. Is, is that part of, I'm going to stop saying quotes, but is that part of the smart grid is, is part of that?

**Paul Zawada:** I don't know what's going on overseas or in Australia, but in California, which of course, as you might imagine, has a large, very large solar penetration.

**Paul Zawada:** There's just for the record, Australia is also overseas.

**Dave Jones:** Yeah. And we, we, we have, I think the world's largest residential uptake of solar. We're like 40% or 50% solar, home solar uptake. It's enormous because we have massive government subsidies here. So everyone jumped on the bandwagon and free solar.

**Paul Zawada:** But a lot of the regulation, so California has had this, this process, it's called rule 21. And if, if you want to research on that rule 21 is what you want to look at. And because as far as I know, they're, they're in the U S at least, they're the ones leading the charge and, and dealing with how to, how the smart grid will interact with people's inverters. But to, to a lesser degree though, I think Dave was talking about a couple of weeks ago about the, the lack of time of use rates. Yes.

**Dave Jones:** Yes.

**Paul Zawada:** And the fact that storing energy at one time doesn't necessarily, you can't make it, there's no, I call that energy arbitrage, right? You, you store it at one time and you sell it when it's more expensive.

**Dave Jones:** Yep. Yep.

**Paul Zawada:** So, uh, things like automated, it's called automated meter infrastructure do enable that type of, of meter where you can do time of day rates because they have essentially the way a smart meter works or what it does is it's, it's recording, uh, it records power just like, or actually it's recording energy, right? It's power over time. And it records typically over some interval. A lot of times it's 15 minute interval. So it's, so in, in a, in a day it's recording 96 intervals of how much energy was being delivered typically, or in the, in the metering side of the house, they always talk about energy delivered, energy received. So energy that you've produced on your, on your solar panels, that would be energy received by the, by the utility. So the meters will keep track for each interval, how much power flowed and in which direction.

**Dave Jones:** And how is this comms going to happen? How is this smart comms going to happen? Is it going to be comms over the transmission line? Just, just like we have for the off peak hot water systems that we have here, the one kilohertz tones, or is it done via the internet?

**Paul Zawada:** And, you know, there's a whole variety of ways it's, it's been done. So when I was involved in the smart metering 15 or so years ago, a lot of the technology was proprietary with the called mesh networks, where packets could hop from, from one meter to another until it reached some kind of a takeout point. Interesting. So you might have a cellular connected device on a pole somewhere that's communicating with internet protocol or some, in some cases, there's a proprietary protocol. A lot of that technology has moved to a variant of 802.15.4 wireless, and it's called YSON, Wireless Smart Utility Networks. However, there is some power line carrier type systems.

**Dave Jones:** Yeah.

**Paul Zawada:** I'm trying to think, COSIM is the standard that's coming to mind. I'm not 100% sure that's the right one, but there are some, I think it's especially popular in Europe because Europe has larger low voltage networks, right? Because the problem is a lot of those signals don't travel through the transformer.

**Dave Jones:** Exactly. Yes.

**Paul Zawada:** So in the US, when you have, say, four houses connected to a transformer, it doesn't, you don't, you have to have a device for every four houses on each transformer.

**Dave Jones:** That's just nuts.

**Paul Zawada:** But if you're in Europe and you have, say, 200, it makes a lot more sense.

**Dave Jones:** Right.

**Paul Zawada:** So there is, PLC is another option. But I think as you, you know, as you get into 5G, you may start to see some 5G services, you know, utilities taking advantage of 5G services. I think in the LTE world, some utilities have done meter, you know, LTE under the glass.

**Paul Zawada:** Yeah. And the IoT is like a definite target for that.

**Paul Zawada:** And some utilities are talking about putting in private LTEs. The problem with private LTE is that it's hard to, the spectrum is hard to get because, you know, the wireless carriers are all, you know, gobbling up the spectrum and paying billions and billions of dollars for licenses. Typically, an electric utility can't really compete. And so, but there are some pockets of private, what they're calling private LTE. So you may have AMI meters that have that private LTE under the glass, as we say.

**Dave Jones:** And then you have the politics of who owns the grid versus the utilities that are, that supply power to it versus the companies that charge individuals. And there's all this mismatch of companies trying to operate on this, like who owns and controls and sets the standard for the whole thing. I think you're talking about like in terms of the wholesale power. The wholesale power, the metering and the distribution and, you know.

**Paul Zawada:** In the U.S. at least, it tends to be divided between what they call the wires business, which is the T&D side of the house, and the generation. So for many years, we had these large, at least many parts of the country, in some cases, maybe not so much. But we have these large independent power producers who can sell wholesale power into a market. And then the utilities themselves can buy it, buy the power to serve their customers. Or they can, in deregulated states in the U.S., you'll have power, like marketing entities, right? I think this is what you're talking about.

**Dave Jones:** Yeah, yeah.

**Paul Zawada:** I actually knew someone down in Florida who was an energy, he still is, I think, but an energy broker. And so he would be calling people up. Evil, ensue. So, I mean, yeah, it sounds, I don't know.

**Dave Jones:** Well, because that's, isn't that how the whole California, the reason the California grid goes down all the time is because of this energy brokerage. It's not a technical thing. It's a. That was the Enron phenomena. That money thing. Right, the Enron thing.

**Paul Zawada:** I don't think that kind of market manipulation is going on, at least to that, to large of a degree. I'm not really familiar with the power markets as much as I am with the technology. But one of the things I was going to mention is this is what ties us back to smart grid and the inverters is that, you know, up until recently, being like the last 10, in terms of 10 years, in terms of whenever the power, I'm sorry, the rooftop solar became, has become a big thing. Everything was these big centralized power plants. But now you're seeing all these generators on the distribution system. And one point I wanted to make about transmission versus distribution is traditionally transmission has been sort of a network. It's a web, power can flow in any direction on any wire. And essentially, it's kind of like a big pool. So you got all these generators dumping water into a pool. Think about it. And then your distribution stations are taking water out of the pool. They're taking energy out of the pool. Right. And so the distribution system traditionally has been one way from the transmission system to the customer. So now the distribution system is starting to look a lot like the transmission system. So now we got power flowing in all different sorts of directions and the system wasn't really engineered for that.

**Paul Zawada:** Which part of that? Is it like the stability or the charging? Well, no. The economics?

**Paul Zawada:** Just in terms of the stability and making sure you have the VARs where you need them and you have the generation where you need them. Because before, everything was these big power producers. And to a certain degree, by adjusting which ones were generating, you could kind of control how the system is functioning.

**Paul Zawada:** Okay. So it's like knobs that you can turn and monitoring on it and stuff like that. Is that right?

**Paul Zawada:** Right. And maybe in a region, you might have had 10 or 20 knobs. Well, now if I got a solar panel on everybody's roof, I have hundreds of knobs I got to manage. Right. And so I can't. Like right now, in terms of trying to control people's inverters with set points, the utility may say, and this is just starting to happen, you need to set your set points for this range. And they may do it once a year or once every couple of years. But now when you have a rooftop solar system on every other rooftop, you might have to do it every hour. Right. And so you can't just email somebody or text them their set point. You need to be able to. Yeah. Please turn it to 22.4.

**Paul Zawada:** Yeah, exactly.

**Paul Zawada:** So that's where the smart grid is going to come in and help us manage. Got it.

**Paul Zawada:** And the set point is then, again, that's changing. That's where the frequency cuts off.

**Speaker ?:** Yeah.

**Paul Zawada:** Is that the idea?

**Paul Zawada:** It's going to be ranges on the voltage and the current in terms of, again, how many VARs need to be produced or it's allowed to produce or absorb. Again, in terms of watts, you know, like if you get to 50.1 hertz, you know, back off by so many percent. So it's a gradual. So it's a gradual. So they don't want everything to just drop off at once. Right. You want things to back off and kind of, you know, have the control algorithm.

**Paul Zawada:** Yeah, that's a lot of sophistication then for each individual box. And you also have to know, like, is there a standard of what they're sending? So a packet they send on the line to, you know, let's just talk about a neighborhood. Neighborhood has 20 houses and 10 of them have solar. And they're monitoring at the entrance to that neighborhood or something like that as this very simple example.

**Paul Zawada:** So there is a standard for that communication. And it's being done by an entity called SunSpec. And so they are working with the inverter manufacturers as well as utilities and as well as folks like cybersecurity people to make sure that people aren't hacking into your. Because, again, I mean, it's the Internet of Things at this point. And it may not be on the Internet per se, but it's communicating.

**Dave Jones:** It's there. Yes.

**Paul Zawada:** Yeah. Yeah, there's info. There's info being passed. So, yeah, you can.

**Dave Jones:** But these inverters, they're, but they're already like mine, like, as you said, they're a grid sensing thing. So can't you just do away with the communications and just have these, just have smarter, like inherently smarter inverters that just watch for the grid? Oh, it's, you know, I know I've got to back off here because it should be 50 hertz as the target. So, you know, it's getting too high in frequency. So I should individually back. I should be a responsible inverter and back off a bit.

**Paul Zawada:** Yeah. And that's, I don't know how smart they can make them. I mean, to a certain degree, I think there has to be some coordination to, because in order to make, say, the power flow balance out and flow in the right direction. Because you may not be able to get power from point A to point B if you don't have enough.

**Dave Jones:** Oh, okay. So you've got to have a higher level authority that monitors and sort of tells things what to do. Because the single inverter doesn't have knowledge of what's happening out on the wider grid.

**Paul Zawada:** Right. Which is exactly the way the bulk power system today with the large generators. Yeah. Each individual generator has a local control system, which is following the grid. But then there's an automatic generation control system that reaches out to these things and tells them where to operate.

**Dave Jones:** Right.

**Paul Zawada:** Yeah. It's all about like remote sensing versus localized sensing, right?

**Paul Zawada:** As I say, you might want your rooftop solar panels in one part of the neighborhood to back off and have them in another part of the neighborhood ramp up in order to balance out where the power is flowing. And I think it'd be very difficult for a rooftop solar at the end of one circuit to know what's going on in other parts of the distribution system.

**Dave Jones:** The limit there would be the transformer, right? Basically, what's beyond the transformer, sort of the individual inverter or generator can't really know as much, I guess.

**Paul Zawada:** Well, I'm thinking of more of the conductors in the middle. I mean, certainly the individual transformers will govern how much, say, a group of houses connected to that transformer can generate. I don't think we're even close to that yet, at least not in the U.S. Maybe you are in Australia. Right. But in terms of being able to balance out and deal with the voltage fluctuations and frequency fluctuations across – so now we've gone down in scale across a neighborhood or maybe across a city, as opposed to traditionally with the bulk power system, it may have been done across the size of a state.

**Paul Zawada:** So what would happen in that bulk power generation scenario? So, like, say a whole section of the city just fell offline, like a huge transmission tower fell off or whatever, and they didn't – they had all this excess power. Do they – they can turn it down at the generation plant, but, like – but there's still, like, excess power in the system still, right? Like, so where does that go?

**Paul Zawada:** Right. Well, so that's where we go – you know, we were starting off, we talked about how does a blackout happen, right? So you're going to have – if you lose a whole city, a whole – maybe not a chunk of a city, it's got to have to be pretty substantial, but you're going to have a whole section of the city drop off. Hopefully, your generators will respond from their control algorithm because actually not producing energy is a lot easier than producing energy – more energy than you're capable of producing. But that's where you get into these oscillations. And so you lose a big chunk of the grid. You could have power flow a different way and maybe trip out a circuit because –

**Paul Zawada:** Because it's going to flow somewhere, you're saying, and it's all connected, so then it just might flow down the big transmission lines to, I guess, in Cleveland examples, down to Toledo or something like that or south to Columbus.

**Paul Zawada:** The way we prevent that is you have your SCADA system, or Dave probably says SCADA because most people I deal with – most people I deal with internationally say SCADA. Yeah. You have these SCADA systems that you're bringing data in from all different points of the grid, and you're bringing back your megawatts, your megavars, your MVA, your voltage, and that goes into a SCADA system. And most people think when they – if they know anything about SCADA, they think of the guys sitting in the control room looking at a big screen with a map on it, right? So – Yeah.

**Dave Jones:** For those who don't know, SCADA is supervisory control and data acquisition.

**Paul Zawada:** Dave has Wikipedia up. There's no way he knew that up. No. There's no –

**Dave Jones:** No way. Yeah.

**Paul Zawada:** Really? Yes. All right. If so, I can't verify. I can't verify. If so, I'm impressed. If so, I'm impressed. I'm impressed. Okay.

**Dave Jones:** I've done a power class. Come on. Haven't you?

**Paul Zawada:** Oh, okay. All right. Come on. Seriously?

**Dave Jones:** Really? You didn't do a power class? I learned a couple of things at least. I – It's one of the things I learned. All right.

**Paul Zawada:** I'll point out though SCADA or SCADA is not limited to the power industry. That term is used in many different industries. Yeah. Oh, it's used everywhere. Yeah.

**Paul Zawada:** They use that at like wastewater plants.

**Paul Zawada:** It just means the ability to control things remotely and monitor them remotely. Yeah. And hack it remotely. Don't forget that. That's a surprising thing too. What I was saying though is like those guys sitting in the control room, they can't possibly watch all these numbers and understand the implications of what happens. So what we do is all that data goes into another system called a state estimator. And the state estimator is a mathematical model of the physical grid. And you can kind of think of it like a crude analogy is it's kind of like spice for the grid. And you know you have your nodes and branches and you're calculating currents and voltages through them. Well, the state estimator is doing that. And it's figuring out where the phase angles between one bus to another indicates where the power is flowing. And so they kind of figure it out in reverse. And they kind of understand how the state of the grid, right? That's exactly what it's called, state estimator, right? So what they do then – So one thing that helps with is like it checks the data in the SCADA system because you may have a piece of equipment in the substation fail and it's telling you there's zero megawatts. Well, the state estimator will say, well, that's not zero megawatts. There's power flowing through there, right? It's kind of like it's doing Kirkhoff, right? You know, right? The sum of the currents in has to be the sum of the currents out. So at a basic level, that's what it's doing. But of course, it's doing it across the entire grid. So it's got the snapshot of the grid. So then what they do is they can run contingency analysis of it. So they start taking – and there's these predefined contingencies like what happens if this generator stops functioning or what happens if this transmission line trips out? And it looks at the resulting change in power flow. And if the resulting change in power flow from – at this point, it's only a hypothetical thing, right? Because it's – they're essentially running like a simulation. It's called real-time contingency analysis. If it's going to cause some other line to overload by their analysis, they have to – the operators have to go and figure out what can they do to prevent that from happening if that contingency happens. So do they open a line somewhere so power won't flow or direction? Or do they tell a generator that they need to start producing more power here and back off another generator there?

**Dave Jones:** Or can they dump it into a load? Are there like loads on the grid that they can dump it into? Yeah, that's what I was wondering too. No, there's not. Because this was one of my – this was one of my questions is like if you've got like a backup generator on the grid, right? If you've got like a gas generator or a coal generator, you know, hydro backup generator and it's always spinning, right? You've got to leave it spinning. Like what happens if that's like what – where does that – does that just not actually produce anything or does it go into a load and then as soon as you need it on the grid, oh, switches it from the load into the grid? How does that work?

**Paul Zawada:** So like a spinning reserve is what they call it?

**Dave Jones:** A spinning reserve, yes.

**Paul Zawada:** So it's a generator that is connected to the grid but is only supplying a small amount of energy. So its control system has been adjusted to not, say, follow the frequency. And it's kind of sitting there.

**Dave Jones:** How does it back off? Does it back off in speed or does it back off like in frequency or does it back off in –

**Paul Zawada:** It's the energy being put into it. So if it's a steam turbine, if it's a steam turbine, they've closed the valve, right?

**Dave Jones:** Okay. Or if it's a hydro, they're just letting a small amount of water fall down through it. Right. Okay.

**Paul Zawada:** You're limiting – and actually, to be honest, I don't know how you do it with an inverter. Maybe you switch out a string.

**Dave Jones:** Hmm. Yeah. Okay.

**Paul Zawada:** But that generator is not – it only reacts to, say, a large change in frequency. So if it sees the frequency drop by, like, say, two tens of a hertz, then it opens the control system. So it basically – its control system is set up to let other – basically to react to slowly accept when it sees a big change. So – but the point – the RTCA, the real-time contingency analysis, is basically you try to eliminate those contingencies that are going to cause something to become overloaded or – so the problem is, is when you get to a contingency of, like, New York City falling off the grid, that's not something they can plan for because that's just a huge amount of energy, right, that all of a sudden you have to go somewhere. And that's when things, you know, trip out and go bad. Or conversely, like – Is that like a – what does rolling blackout mean? Because that's the California thing. Well, a rolling blackout is a controlled thing. So a rolling blackout –

**Paul Zawada:** Oh, okay.

**Paul Zawada:** – is what they tried to do in Texas. But the problem is it's not – it's really hard to make it rolling when you have to take a whole – a big chunk of load off the grid. But rolling blackout is when the operators see – so let's take the Texas example from last winter.

**Paul Zawada:** So – This is when everything iced up and there were problems with that, right?

**Paul Zawada:** Yeah. Right. So they're losing generation and they're watching frequency go down. So they're saying, okay, well, we got to get frequency back up, you know, cut so many hundred megawatts or tens of megawatts. I don't know that – I don't know what granularity they use, but –

**Paul Zawada:** Of consumption.

**Paul Zawada:** Right. So – because they can't – there's no more generation to add in, right? So when you can't add in more generation, the only thing else you can do is, you know, remove load.

**Paul Zawada:** Throw someone over the side of the boat. That's what I know from the movies.

**Paul Zawada:** So the idea of a rolling blackout is you cut the consumption and then you kind of establish some new equilibrium with the generation you have left. And so then you take turns. And so this part of the city, you know, gets their power back on for so much time and the next part of the city loses or maybe it's by circuit, right? You try to –

**Paul Zawada:** Oh, so that's the rolling piece? That's what – I never knew what the rolling was. Like why –

**Dave Jones:** Yes. Was it some human, you know, pushing – oh, this one has to go off. If that one goes off, oh, we've got to push another button.

**Paul Zawada:** But what happened in Texas is it all happened so fast that they were just cutting, cutting, cutting, cutting. And then – and by the time things kind of stabilized, they had large chunks of the grid that were de-energized that you can't really effectively roll it at that point.

**Paul Zawada:** Yeah. So then how do you turn that all back on? It's got to be gradual? Because like then you open up circuits. So you're like ramping your generation back up and you have to open up circuits to like consume that power then? Right.

**Paul Zawada:** And the problem when Texas was there was nothing to ramp back up for a while. So that's why it lasted longer than – if you look at the 2003 blackout, things came back relatively quickly because it was –

**Paul Zawada:** Yeah.

**Paul Zawada:** It was more of a loss of situational awareness and a few things went wrong and caused those power oscillations and that – and things just went south from there.

**Paul Zawada:** So Texas is also a problem because – I remember reading about like they have a more self-contained grid. So like they couldn't import power then from like Oklahoma or – Right. – other states nearby, whereas you might do that otherwise?

**Paul Zawada:** That was a problem. But if you looked at what was going on that day, the areas outside of Texas were having trouble as well. So it's not clear how much –

**Paul Zawada:** Yeah. Yeah. It's not going to import it from Florida or something like that. Like you're just going to have to go a really long distance to get in there, right?

**Paul Zawada:** Yeah. Some people say, well, if Texas didn't have their own grid, that would have never happened. I don't think that's necessarily true because they were having trouble in Oklahoma and other areas as well. So it was –

**Dave Jones:** Here's one thing I don't get though. And maybe I'm just – it comes back to like if you've got like your lab power supplies, right? Or you've got a whole bunch of batteries, for example, right? You can whack all those in parallel, right? So then you've got X amount of power that can be delivered from your source. So let's say you've got a one megawatt power generator, right? That's a turbine generator. Why can't you just stick that onto the grid or 100 of them onto the grid and they only use the – like only if the load requests the power does it use it? Like isn't it like just a voltage thing sitting there waiting to be used? I know the answer is no and you can't just put infinite amount of generators on the grid, right? But I want to understand why if my question is making sense.

**Paul Zawada:** What's going on though when you're talking about your lab power supply, there is a power source behind the power supply that's regulating how much is going through. So –

**Dave Jones:** No, but your load determines how much power is taken. Right. That's why I'm saying like why isn't the generator viewed as just a voltage source and then the load takes what it takes and you can have an infinite number of sources in parallel on the grid. But I know that you can't.

**Paul Zawada:** I'm going to venture a guess here, Dave. Because money?

**Dave Jones:** Well, I don't know. That's the thing. I want to know why you can't just put an infinite number of generators on the grid and just leave them there and then the loads, us humans who are using – consuming the load just take as much as we need. As long as we don't exceed the maximum capacity, no problem. Well, to a certain degree that does –

**Paul Zawada:** I mean – The thing is is that you have a certain number of generators and like I was saying earlier, there's a control system that is governing how much energy is actually getting converted to electrical energy and being put into the system.

**Dave Jones:** Yeah. The problem – But you can't put energy in – that's what I'm saying. You can't put energy into the system. The energy you put in has to be determined by what the load wants to take. Right? You can't like force energy into the grid. No. Can you? That doesn't seem to make sense. You can't force it. It's what the load determines it needs.

**Paul Zawada:** So Dave, your idea here though would be – so let's just say – okay, so there's a box sitting somewhere that can generate one megawatt. Yes. Most of the time – so you'd have 10 of these available and you're saying when consumption is low, each box is just not – it's just outputting a nominal trickle amount of power and then as everybody's air conditioners come on, then these generators come up in response?

**Dave Jones:** No. I'm saying that they're always generating – there's always that power available, but it's only if the load determines it does it draw it out.

**Paul Zawada:** Well, I think – I mean, I think your analogy is like if you have – if I take three AA cells and I put them in parallel and I put a resistor across those three cells, it's going to draw a certain amount of current and I can put – I can put double the load or half the resistance, right, if I put two resistors and more current is going to flow, right? And I think that in that case, I think it's governed by the chemical reaction going on in the battery.

**Dave Jones:** Yes. Okay. Yes, it is. That's where the energy comes from, but the power is – the instantaneous power is always available because that chemistry is there to be used.

**Paul Zawada:** So if I put a whole string of resistors in parallel, it's going to consume – that chemical reaction is going to happen a lot faster and consume the energy that's stored in that cell, right? Right. So I don't think the analogy quite transfers over to –

**Dave Jones:** Yeah. I'm just wondering how.

**Paul Zawada:** So the point is in that cell, there is a governing mechanism, right, that is controlling.

**Paul Zawada:** Yeah. That is the control system is redox or something.

**Paul Zawada:** So in the grid, in a steam turbine, that control system is the one running the generator because if it runs too fast, it's going to – you can't – it's going to burn up the generator somehow.

**Dave Jones:** Well, that's what I was going to ask. Like, let's say you've got a hydro generator because I'm sure everyone can picture like, you know, water being flowing down the pipe and turning the turbine, right? What happens if you've got that? Like, you've got the maximum – you've opened the valve all the way and you've got the maximum amount of water coming down and it's turning the turbine at its maximum rate, but there's no load that wants that power. What happens? Does the voltage just fly off and blow up the generator? What actually – like, do they have to actively control the amount of water flowing to match the load? Is that –

**Paul Zawada:** Well, there has to be current flowing too, right? So – And not just water current.

**Dave Jones:** Well, there doesn't have to be. What happens – well, see, that's the thing. That's what I'm talking about. If there's no – if there's no load, there's no current flowing, but that turbine is spinning at its full rate. So therefore, does that mean the voltage goes off in the –

**Paul Zawada:** The water will flow through the turbine faster.

**Paul Zawada:** Yeah. And so I think that eventually in that scenario, the turbine – Right. Right. Okay. There'd be no load on the turbine, so it'd be like freewheeling basically and all that water flowing through it. It would basically blow up, right?

**Dave Jones:** It'd be – Right. Right. And it wouldn't – right. The energy wouldn't be extracted out. The energy would be lost in the gravity as it falls through. There'd be no energy being pulled out through the turbine blades because they'd just be freewheeling.

**Paul Zawada:** And you can demonstrate that with a small – like a DC hobby motor. If you take it and spin it and the leads aren't shorted, it'll just – it'll keep spinning. But if you short the leads, it will not – it won't spin freely at that point.

**Dave Jones:** Yeah. Yeah. Yeah. It's tough. Yeah. Yeah. Yeah. I've done that. Yep. Right.

**Paul Zawada:** Well, actually, I had a question about this too because I was just watching – I just saw like a – the video of like arc welding steel. I think it was on the MachinePix channel on Twitter. But it was like, you know, these high, high power industrial processes. And when there are loads available, I would imagine like – aren't there like smelting plants that are often like located near like aluminum smelting and stuff like that that are located near power generation as like they can buy excess power?

**Paul Zawada:** Yep. Or nowadays, it seems to be more like electric steel plants where they melt down. They recycle steel. Yeah. Yep. And those types of facilities, power quality is a real issue because they generate all kinds of harmonics and –

**Paul Zawada:** Oh, interesting.

**Paul Zawada:** And they have to do certain things to filter. I'm not exactly how they – I mean, they may have some large inductor and capacitor banks to deal with some of that. But I think some of it is just how they build the furnace and the electrodes. Okay. To try to limit the harmonics.

**Paul Zawada:** But they don't want to operate just when power is super cheap. They want to just do it all the time. It's just they want to get a good rate as like a – they would probably act as a pretty reliable load even though they have all this weird –

**Paul Zawada:** Oh, yeah. Yeah. And they're probably going to get a rate that's cheaper because they're buying in bulk, right? Just like anything. If you buy a lot of it, you get –

**Paul Zawada:** Yeah. When I worked at Samsung, I remember they got a really, really great deal from the Texas power, whoever they're buying from. But they needed like a – they had a service contract because if the power goes out, all those wafers get destroyed. And I think the power company had some liability in there. And I remember something about that, but I don't know what. So – but they were a very good consumer.

**Paul Zawada:** Yeah. Sometimes there's limits on the liability. I mean, sometimes, you know, certainly contractually they can try to make the power company ensure, you know, 99.99999% availability. But there's only so far the – Acts of God. The power company. Yeah. And in that case, it's probably – the energy provider is not the limiting factor as much as the wires provider, right? Because of the acts of God. Yeah. If an energy provider loses a plant, they can go to the market and buy the power from somebody else who is still producing and cover their – you know, they do have to cover, you know, generation that drops off. But in a market environment like Texas, they can call another energy provider or do energy trading to offset their loss. So in that case, they'll have some kind of commitment of a generating facility that can cover the power requirement. The issue is if the wires go, there's nothing you can do to get the power there, right?

**Paul Zawada:** Ah, I see. And so those are different entities you're saying as well?

**Paul Zawada:** In Texas, definitely. Okay. And Texas, the wires company – well, they can have an energy business, but I think most in Texas, most of the wires companies are not in the energy providing business. And in Ohio, the energy companies or the utilities do not own any of the generation. What they do is for what they call the standard offering, say, if I'm a consumer and I don't want to pick my power provider, the utilities run a reverse auction every so often. And say for the next six months, you know, the energy – the companies that do provide energy, they bid on that and it goes to the cheapest provider for whatever commitment.

**Paul Zawada:** I used to be very confused by – I would get these mailers when I was living in Cleveland that says, you know, switch to us, you know, we'll provide your power. And I just remember thinking, like, how do you get to choose? Like, are you a power plant that's just, like, going to specifically route me power? That doesn't work, you know?

**Paul Zawada:** And it's – No, it's – that's all in accounting exercise, right?

**Paul Zawada:** Yeah, right, right.

**Dave Jones:** So it's all – that's why everyone talks about, you know, eco power, you know, oh, your EV is just powered by coal, right? Well, no, it's not because I actually pay for extra green and power to come from wind to build wind turbines to go onto the grid. So technically, I'm – we had this argument a couple of months back, Chris, didn't we? A while back, how that you said that I can't possibly – that my EV is not being powered by wind energy, but I'm paying for wind energy. Therefore, somewhere on the grid is wind turbines paid for by me.

**Paul Zawada:** Probably partial turbine, let's be honest. You don't buy that much power. You get the very tip of the blade, you know? Come on. One of the blades.

**Dave Jones:** Right, yeah.

**Paul Zawada:** Just the tip. So the idea is, is that, again, you have this big pool, right? And you just have a bunch of energy going into it, and you have a bunch of energy going out of it. You don't – you can't trace a specific jewel of energy provided by one plant. You can't trace it through the – it's just the system just operates as a whole together. You have all – and –

**Paul Zawada:** I only want artisanally generated power by some mustachioed person riding a penny farthing in Brooklyn.

**Paul Zawada:** So really what's happening is there's what's called a settlement process. And so the market operator looks at all the power that came in for a particular interval, who was supposed to provide it, did it go into the system, and then they look at all the power going out. And where did – you know, who provided power to which customers? And then they settle the market is what it's called.

**Paul Zawada:** So if you have any listeners that happen to be any accounting students for God knows what reason, don't go work at a power company because that sounds like a terrible job. I'm sure it's all computers.

**Paul Zawada:** Yeah. The settlement folks at the power companies, they tend to have this job that a lot of people don't fully understand. It's kind of like a black magic in some senses.

**Paul Zawada:** A couple giga bars here, a couple giga bars there. Now we're talking some real power, you know? But – No.

**Paul Zawada:** In the – oh, I caught – oh. You're talking some real – you're talking some reactive power there, Chris.

**Paul Zawada:** Reactive, sorry.

**Paul Zawada:** But in the end, it really does influence – like if you were saying you're buying green power, it does influence the market for more – because if I'm a wind generator, I'm going to get, you know, so much more per megawatt hour that I generate, I'm incented to build more wind turbines, right? And so – and if I'm a coal generator and I can't – if I can't bid into that green power market, then I may not be able to sell energy, right? So – and my power plant may have to be shut down.

**Paul Zawada:** It's like voting with your feet basically but on a bill, right? Or a wallet, I guess. Yeah. That's great.

**Dave Jones:** Yep.

**Paul Zawada:** Nice job, Dave.

**Dave Jones:** Yes, I know. I've been doing that for like 20 plus, 25 years or something. Like as long as it's been available, we've been buying green power, pay like an extra five cents per kilowatt hour or something for that, you know? So I'd like to – and I used to read the audit reports because they used to release these audit reports of, you know, look, we put on X – you know, we built X amount of, you know, turbines this, you know, year or whatever and they've gone online and et cetera, et cetera. So, yeah, it was all above board.

**Paul Zawada:** Paul, how does the turbines going on the grid then – so like – sorry, a wind turbine then, that actually is spinny metal. So does that – obviously it's, you know, interspersed for when it's windy. That helps balance out solar?

**Paul Zawada:** So my understanding is that a lot of those wind turbines actually generate into DC, into an inverter system. Oh, interesting. Because – because those turbines don't spin synchronously with the grid. Oh, right, right, yeah.

**Dave Jones:** No, yeah, that's right. If you look at a – yeah, yeah, of course.

**Paul Zawada:** Steam generator, it's going to operate at like 3,600 RPM. That's going to be the – that's going to be the speed that it rotates. And so that's what you're doing when you're adding or subtracting steam from the turbine blades is you're maintaining that 3,600 RPM or 1,800 RPM. It's going to be some multiple of 60. The wind turbines, you can drive down the road, you can see one spinning faster than another one, right?

**Paul Zawada:** Well, they have gearboxes on them, I know, but like that still isn't going to be synchronous with the – it's the wind is the wind, right? You get what you get.

**Paul Zawada:** Yeah, it's not going to be continuously variable though. So, you know, how do you adjust it by, you know, a tenth of a hertz? I think it's done – I think it's done electronically. Yeah. Yeah.

**Dave Jones:** Right. Yeah, I think it must be. What about AC versus DC? You know, Tesla versus Edison here. There's more and more DC, like long-haul DC. Is there any talk about it happening on like the more local scale or is it just for long-haul grids?

**Paul Zawada:** So if you may know or may recall, the reason we use AC is basically because of transformers. So AC –

**Dave Jones:** Yes, exactly. Transformers make it easy.

**Paul Zawada:** It's easy to raise and lower the voltage because actually, you know, there's – as we've been talking about with reactive power and stuff, there's a lot of things about AC that make it really complicated.

**Dave Jones:** And the transformers are very efficient too. Another thing I learned from my class, Chris, not from Wikipedia, is that transformers are incredibly efficient. And if you think about it, they have to be because, you know, the mental exercise we were given is that, well, okay, okay, let's assume it's only 95% efficient transformer. What's the energy loss in that transformer? And you work out, holy shit, it's a lot. So therefore, it'd melt down. So therefore, they must be like 99.9% efficient. They're incredibly efficient devices. Am I wrong?

**Paul Zawada:** Oh, yeah. They're very – I mean, but you still can put your hand on it and you can still feel more. So they're not –

**Dave Jones:** Oh, yeah. Yeah. There's some loss. It's not perfect. But it's not like 95%. It's like, you know, it's pretty close to – it's much more close to 100% than it is to 95%.

**Paul Zawada:** To talk about the DC point. So certainly, DC has been on the radar for transmission for some time. And there's – going back to the 70s, you know, there was a line that's been in place in California that the Pacific-DC inner ties – I don't know if it's Southern California and Northern California or maybe it goes further north into Oregon. I don't remember the details of where it's running, but the limiting factor in that, I think, has been the conversion going from AC to DC and then back to AC. The power electronics is coming around, so it's becoming more feasible and more cost-effective, I think. So in the U.S., we haven't seen a lot come online yet, but there is – there's a lot of proposed DC lines. There's one – I can't – I think they're calling it the Sioux line. It's an underground line that they're talking about building in, like, the Iowa area. No.

**Dave Jones:** And that's because you can put DC underground, whereas AC you can't really, can you? That's why they string in the underground, isn't it?

**Paul Zawada:** Or is it – And that's one of the things that makes this pretty radical, that they are talking about putting it underground. Because, I mean, it's an insulation issue at that point. Yeah, yeah. And being able to build insulation that, you know, that prevents the flashover.

**Dave Jones:** I've heard they pump – they have to pump, like, fluid into them and stuff.

**Paul Zawada:** Some of them – some of the underground – they call it pipe-type cable. And they have that for AC cable. I mean, that's been a technology – tends to be used in cities, right, where you're trying to get transmission through, say, New York City or –

**Dave Jones:** Oh, when – if you're in the city. But out on the huge 500, 750 kV transmission lines, none of those are underground. Is that correct?

**Paul Zawada:** No. Sometimes they'll take, say, a 345 underground.

**Dave Jones:** Oh, really? Okay. Wow.

**Paul Zawada:** And, again, that might be pipe-type cable. I don't know which to have the oil dielectric flowing through it. I know they have 138 that could be solid dielectric. I'm not sure if they're there. They probably are, because that technology has been around long enough.

**Paul Zawada:** Yeah, if you're doing the really high transmission through, you know, from city to city or from plant to city, whatever, just – I assume that just comes to economics, you know? Yeah, it's terribly expensive. And so – And the towers are also expensive, but, like, not as much as digging up that much dirt.

**Paul Zawada:** I don't know how this proposed DC underground line is proposing to do it. But in general, DC is becoming more feasible because of the different types of thyristor technology that you need to do that conversion. I mean, you just couldn't do it at scale to do hundreds of thousands of megawatts before, and now with some of the new technology, it's more feasible. So going back to China, they have a lot of DC transmission there too. And it's typically done with two conductors instead of three. So you have cost savings in only having to run one less conductor, right? And then I believe just DC, there's inherently lower losses because now you're not dealing with – you're losing – you're not losing your VARs because typically VARs don't move as well as through the system as watts. And so overall, the losses in a DC system are much lower.

**Paul Zawada:** And that's assuming you're at the super high voltage though, right? Because you still want to lose – you still want to have that I squared R losses lower.

**Paul Zawada:** So the problem then is when you get to the city and you need to drop it down at the distribution station and you need to drop it down again in your backyard or if you're like in a – in say a European environment where you have, like I was saying earlier, a couple hundred houses on a low voltage circuit. There has been talk about – I think – I forget what they're called, like silicon transformers, which essentially they use power. It's kind of like – I think it's kind of like a switching power supply for 7.2 kV. Oh my gosh. But I haven't heard anything about that lately. That seemed to be kind of a buzz going on in the industry maybe 10, 15 years ago. Right. And I'm not sure what happened with that. And the other thing kind of along those lines, Chris, you mentioned about – I think it was – I'm not sure if it was Dave, but you're talking about batteries in the backyard. I mean local storage.

**Dave Jones:** Oh, local storage for like a single –

**Paul Zawada:** Right, when you don't have solar actually. That was the conversation starter I think.

**Paul Zawada:** Yeah, and that was another technology that was kind of a buzz 10 years ago or so. And it kind of died off. And I think they're looking at more like neighborhood or community scale storage rather than trying to – because think about trying to bury batteries in backyards across an entire city may not be easy to manage.

**Paul Zawada:** Oh, that was a different conversation than what I was talking about. Yeah, okay. I see what you mean. You say like localized storage just for redistribution as needed, that sort of thing.

**Paul Zawada:** But there was talk about putting those – again, I think a lot of those were four-quadrant inverter battery storage systems. So they could provide watts or VARs or they could absorb watts or VARs depending on what was needed on the grid. But I think it was – again, going back to trying to control all that technology, I think it was maybe a little bit ahead of its time in terms of managing those systems as well.

**Paul Zawada:** Available parts and stuff and – yeah.

**Paul Zawada:** Well, no, just building the control systems and the communications you needed to all these systems. Yeah. But I think that technology, maybe not with inverters and storage systems in every backyard, but that overall technology may be coming back around to deal with the rooftop solar and small wind systems. Because I don't know if you see it a lot in your areas, but you do see small wind systems as well. There's a couple of car dealerships around where I live that they have one little wind turbine. Wow.

**Dave Jones:** Really? No, that's not a thing here unless you're out on a farm somewhere.

**Paul Zawada:** I was going to say farms I've seen actually ads towards targeting farmers specifically that are like –

**Paul Zawada:** And when I say little, I'm talking maybe 500 kilowatts or KVA actually. A lot of times – a lot of things are rated in KVA, right, or MVA because at the end of the day, you need to be able to handle the voltage times current going through that device. So you'll see these smaller wind turbines. They're not the little tiny ones for like a single house, but we're seeing more of those in our area where you have just one or two. Or in some cases I've seen like an industrial park where you have several little factories that each have their own one or two wind turbines. And there's a company that manages those for them. And sort of it's a little self-contained community wind system.

**Paul Zawada:** Yeah, that's kind of cool. I mean like this is the thing where like I wouldn't know – You'd notice the spinning maybe, but I wouldn't be like, oh, I wonder if that's for this sort of thing. So –

**Dave Jones:** Hmm. Now you wanted to talk about exploding transformers. Tell us. It's – what, it's a pet peeve? You're not a happy camper?

**Paul Zawada:** Chris and I talked a little bit at the beginning or before we started recording. But yeah, my pet peeve is when somebody in my neighborhood or I hear it on TV, they'll say, boy, did you hear that transformer explode last night? What? And I don't know if you have this phenomena. I would imagine you do, Dave. But, you know, you'll hear these bangs for – like, you know, especially like during windy –

**Dave Jones:** Well, we don't because everything's underground. Everything's underground. Yeah, that's true. Like we'll have transformer boxes, which will sit, you know, big green boxes, but we don't have overhead ones.

**Paul Zawada:** And I don't know the structure of your grid. Maybe you do have it all underground. But like in the U.S. where you have underground, you may have a residential development that is all underground, but around the periphery, you still have overhead to get it from, say, the distribution substation. Oh, yeah, of course. Yep. So that bang is not a transformer explosion.

**Paul Zawada:** And they're usually talking about the trash cans up on the pole. That's what you're talking about.

**Paul Zawada:** Yeah, exactly. Are you talking about an arc over? People don't seem to realize that when you have a 7.2 kV or a 19.9 kV primary touch ground, it's going to make a loud noise. It's not going to be a tiny little – it's going to be – it's an explosion, really. Yeah. Or the other thing, it can be the fuses on the overhead equipment. They are rather big. They're not very big. They're not like what you'd have in a house or in a piece of electronic equipment. You know, they're the size of your arm, right? They – what they are designed, when they – when the fuse blows, it – actually, there's a powder inside the tube. It's called an expulsion fuse. And it makes a rush or an explosion of this material to clear the arc. So there's this rush of gas leaving the tube that contains the fuse. That's what quenches the arc because a lot of times, if you have an arc, it's going to continue – the arc is going to continue to burn. You need something that's going to quench the arc. And in a fuse, it can be this – I think there's boron is in the substance. And it – you know, it's a violent explosion because it's got to clear that arc. In circuit breakers, like in a substation, the smaller ones, it can be a vacuum or oil a lot of times. Or in older times, it was more oil. Nowadays, it's more a dielectric gas like sulfur hexafluoride, SF6. That's a fun one. That's the one that makes your voice real deep. Exactly. Yeah. Yeah. And it's a very dense greenhouse gas. So the environmental regulators have pretty tight controls on – you have to monitor. It's like if you get a leak, it's got to be fixed right away and that kind of thing. But there's always – when you have high power equipment like this or operating at high voltages, you have to have something to quench that arc. And that's the job of the dielectric or –

**Dave Jones:** Doesn't the AC help with this because DC arc fires on houses, on solar, of course, on the DC isolator. They're famous for catching on fire and burning down your house because once DC arcs over, it forms a continuous plasma arc. And then it just stays like that until there's no more energy to give. Whereas doesn't AC self-extinguish in boatmarks?

**Paul Zawada:** Yeah, because AC, there's a zero crossing, right? So the voltage is going to go through zero at some point and hopefully it's going to go through long enough for the arc to stop. But that may not necessarily be enough. But you're right. DC is very dangerous that way. And when you go into a substation in the control house, typically that equipment is powered by large DC batteries like 120, 130 volt battery. And some older locations, you don't seem to see it in newer ones, but some of them had 250 volt DC plants. And I've not been around that, but I've been told when one of those 250 volt DC systems shorts out, like in a piece of equipment fails or something, you need to be as far away as you can because it's pretty bad. Lots of energy being discharged.

**Paul Zawada:** You're saying volt, but everything's been kilovolts and megavolts lately. So just wanted to double check. It's 250 volts, but it's because there's a...

**Paul Zawada:** Right. So the protection system has to be designed to operate because it's going to interrupt the AC. In the worst case, it's going to completely de-energize a station. So you need to have a battery system that's powering the trip coils in the circuit breaker that's doing that.

**Paul Zawada:** Got it. So it's like a 250 volt battery that's going to drive a motor or like a relay or something crazy like that to like separate physically?

**Paul Zawada:** Typically, the substation breakers have some kind of stored energy so they can operate really fast. So they charge a spring or they have compressed air or some... So you're not driving a motor to open the breaker because you want that. And typically, like we were talking about the zero crossing, typically they are timed to try to open during that zero crossing to increase the chances that that arc's going to be quenched. But you still have a coil that's kind of like it has a latch, right? So you have like if you have a charged spring and you have some kind of a latch keeping that spring compressed, you have a coil that opens the latch and, you know, that spring, that spring discharges really quickly. And it moves the actuator that actually opened that breaks the circuit.

**Paul Zawada:** Hmm. That's crazy. And so what is the loud part then? So it's the 250 volt shorting to ground when that goes bad, you're saying?

**Paul Zawada:** So, so no, like in your neighborhood, it's the, the, the fuse, it's just a fuse. And again, it's when the fuse burns, when the, when the, when the, when the metal inside the fuse melts, there's this, this substance around it.

**Paul Zawada:** Yeah. It's like a, it's like a bomb or like a firework, right?

**Paul Zawada:** It's basically a small firework. And it, it, it basically clears out that, that, that, that tube that's got the fuse. So, so in a substation, typically they're not that loud except what's called an air blast breaker, which uses. An air blast? Yes. Yeah. So those use, they use compressed air to, to, to both operate the mechanism as well as quench the arc. So that, that rushing air where the electrodes are, you know, basically clears the arc away. Yeah. You don't see air blast breakers as much anymore because they take a lot of maintenance. Again, you see mostly SF6 insulated breakers in, in modern substation designs.

**Paul Zawada:** It's just amazing to me. Like the, I feel like this is half of this stuff is like so mechanically focused, you know, like generators are just, you know, you're putting in mechanical work in order to drive these things and breakers. You're doing all this stuff to clear, you know, you're basically trying to blow away an arc, you know, it's just crazy. Like how that all works.

**Paul Zawada:** Yeah. And, and, you know, this goes back to, you know, what you were talking about the other day about, you know, nobody knows everything. Like there is, there are so many specialties and so many different pieces that somebody has to be an expert on that nobody can be an expert in all of it. And, you know, I, I have a friend, I have friends who have, they'll have a son or a daughter who's like studying mechanical engineering and I'll suggest the electric utility industry. And they're like, well, they're not into electricity.

**Dave Jones:** Right. But it's, yeah, no, there's, there's a heck of a lot of mechanics.

**Paul Zawada:** This is actually a thing that, that Dave says often that I wanted to get your opinion on too. So Dave says it's a good industry to go into. Is that, is that a good statement? I mean, like.

**Dave Jones:** Oh yeah. It's a good industry to go into because it's not sexy. Right. Nobody like gives a toss. Sorry, Paul, but you know, like most, most engineers study.

**Paul Zawada:** It's not Tesla.

**Dave Jones:** It's just not a sexy industry. Right. And they don't, and that leads to less people. And it's a big, you know, it's, it's one of it's, in fact, isn't the, isn't the grid, the largest single construction on earth. I think like if you talk about the entire worldwide grid, I mean, it's the biggest thing that we've ever, ever invented. Physically.

**Paul Zawada:** You hear it's the most complex machine ever built and that, that kind of thing. Yeah.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. Yeah. It's incredible. Yet nobody cares about it. It just, you know, turn on PowerPoint and your light comes on and, you know, and yet that, so obviously that's going to lead to the world. You know, it's, it costs a lot of money to run this. So therefore I think you gotta, is there a decent amount of money? Like if you're a specialist in, you know, a grid distribution, you know, design or something.

**Paul Zawada:** I don't, I don't think it's like going to work for, for a crazy venture. No, it's not Apple. Crazy venture capital fueled enterprises. Right. But no, you can, you can certainly make a very good living at it. And I, I, I'm certainly feel like I, I, I live very comfortably and I, I really like, uh, like the, how I'm compensated. So it's, it's not, uh, it's not a bad industry by any stretch and it's very, it's, it's very dependable. I mean, people need, people need electricity and, and.

**Paul Zawada:** Yeah. I mean, can you work, can you work anywhere? Not like at home, obviously, but like, can you work and can you move to any location in the country?

**Paul Zawada:** No, I was going to say, can you, oh yeah. Yeah. I mean, there's, there's always utilities looking for, for people.

**Dave Jones:** And is it possible to work for yourself, like being an independent contractor or do they just prefer to work with the biggies and then like, or can you work as a subcontractor for like a power utility or something?

**Paul Zawada:** So, so my, my, my, my day job, I do work for a very large electric utility, but I have also had a, I've, at times I've taken what I call my sabbatical and I've gone and done consulting. I've consulted in, in India and the middle East and on, on, on power projects on specifically in those cases, smart grid type deployments or, or planning exercises. So yeah. And there's a lot of engineering consulting firms. So typically you'll find, I think most utilities have a mix of in-house versus you, you know, engaging engineering firms to do their work. So like your smallest utilities are probably not going to have the expertise to, to say, design a substation on their own. They may rely on, on engineering firm, or in some cases they'll rely on your Siemens or ABB or. ABB. Yep. Depending.

**Dave Jones:** ABB. Chris used to work for ABB.

**Paul Zawada:** Not the ones doing the substations though. That's yeah.

**Paul Zawada:** Yeah. And I think, I think that part of ABB has kind of been at least partially spun off to Hitachi. Yeah.

**Paul Zawada:** I think that's right. Yeah.

**Paul Zawada:** Cause you, you see a lot of, of references to ABB slash Hitachi now or Hitachi ABB. But, but anyway, there's a whole range of, you know, different utilities. They have different mixes and some of that goes back to how, how they're funded and how they, how they, they recover their investment through rate recovery. Sometimes it's, it's more advantageous to, to rely on outside sources. Sometimes it's more advantageous to, to rely on inside resources. And, and, and sometimes that changes over time too, depending on how your regulators treating capital work versus operation and maintenance work. O and M utilities tend to make their money on capital by spending money. They get a, they get a rate of return on it. At least the wires business. Yeah. It, it varies on the, the generation side, depending on if the, the generation is integrated with the, the, the wire side of the business. If it's independent, then it tends to be more market-based and they don't, they don't, they're not guaranteed a rate of return like the wires business. One last question.

**Dave Jones:** How do you, how can you stand those scams? You know, there's energy saver scams that are absolutely, those freaking capacitors in a box scams. I no doubt you've seen them. Oh yeah. I've seen them. Come across them.

**Paul Zawada:** And like, I don't, I don't really pay a lot of attention. And like I said earlier, I'm not a hardcore power guy, but still, you know, just write it off as a scam.

**Paul Zawada:** What if they put an Arduino in front of those capacitors though, or some other kind of technology?

**Dave Jones:** Right. Oh, that's going to make the difference. Yeah, of course. Smart grid. There we go. Smart grid. There's a relay. Wait until they catch all those smart grid.

**Paul Zawada:** You got to have something flip the relay. Yep. There's the smarts.

**Dave Jones:** Nope. It's still a capacitor in a box with a lead on.

**Paul Zawada:** Paul, if people want to hire you to design their smart grid, or I have other questions about your consulting services, how can they get in touch with you?

**Paul Zawada:** Well, I am at Engineer Z on Twitter. My company or my side business is Sintinus LLC. It's Sintinus.com, although that haven't been too active on the consulting side because I'm also working on a doctor of technology degree. Oh, wow. Oh, okay. Well, it's technology and it's almost like on the IT side. But of course, my focus is on OT. But again, like I was saying earlier about how do you get utilities to modernize their approach to technology and that kind of thing. Right. It's almost more akin to, say, an MBA, although I shudder to say that because at heart, I am an engineer. Yeah, of course. But it is more about strategies to how to apply technology and things like, you know, how do you get expertise and how do you find people to do that kind of work. And my consulting stuff is not so much these days, you know, with a full-time job and studies. And even when I'm not on sabbatical from my full-time job, I don't do a lot of consulting on the side.

**Paul Zawada:** Okay. Well, they can just reach out on Twitter then, just chat about Smart Grid.

**Paul Zawada:** They can reach out on Twitter. I try to tweet something every once in a while and share my knowledge or wit.

**Paul Zawada:** Well, we appreciate you doing that here. This has been very enlightening. We do. Thank you very much. It's, uh, I think Dave, we're going to be arguing about, we're going to be referring back to this, this, uh, episode often during arguments, I'm sure. Uh, yeah. Yeah.

**Dave Jones:** This will be our go-to episode whenever we goof up. Yeah. Yeah. We're still going to get it wrong. Which we always, you know, it always gets in there somewhere, you know, it's, yeah. So yeah. Thanks, Paul. It's been awesome.

**Paul Zawada:** Great. I was glad, glad to be here.

**Dave Jones:** Thanks, mate. Appreciate it. Catch you next time.

**Speaker ?:** Bye. We'll see you next time.
