---
episode: 481
title: An Interview with Paul Thompson
url: https://theamphour.com/481-an-interview-with-paul-thompson/
---

**Paul Thompson:** This is The Amp Hour Podcast. Released February 24th, 2020. Episode 481. Sponsored by Keysight. An interview with Paul Thompson.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Paul Thompson:** G'day. I'm Paul Thompson from Pacton Technologies in Brisbane. Hey, Paul. Thanks for joining us. You're welcome.

**Dave Jones:** This is a rather lucky event, really. I found one of your products in the dumpster, a really old version of your product.

**Paul Thompson:** Yes. I eventually worked out. I think I worked out how it got there. We'd sent it away for testing, for EMC testing many, many years ago. And sometimes you just don't get those things back.

**Dave Jones:** Really? I think we've always gotten ours back, but really, they just keep it for what purpose?

**Paul Thompson:** Yes. It depends how the testing goes. For example, I know of another case where we sent some items off for electrical safety testing, and then there was an earthquake in New Zealand. We didn't get those back.

**Dave Jones:** Oh, okay. Right. That tends to disrupt things a bit.

**Paul Thompson:** Yeah. Yeah. Disruption, change of personnel, that sort of thing.

**Dave Jones:** Tell us about Pacton Technologies and what you guys do and what you do there.

**Paul Thompson:** So Pacton, we're an electronics design and manufacturer. We began in 1995 on the back of an invention, and that invention was an electric fence fault finder. I was the first person to put to market an electric fence fault finder that actually was useful in that it said which way the fault was. It gave the direction to the fault. And it did that by analysing the current flow in the electric fence live wire. So having invented something, like a lot of inventors, I thought, well, I'll just sell the invention. So I found the largest company in the area of electric fencing and tried to sell the invention. But that didn't go very well. So I ended up starting the company.

**Dave Jones:** They just weren't interested or they stole your idea or?

**Paul Thompson:** The latter. They were very interested.

**Dave Jones:** So you started your own company?

**Paul Thompson:** Yes. So in order to exploit the idea, we started Pacton. Really, you know, prior, 12 months prior to starting it, I was happily working for a company in the area of electronics weighing, making digital scales. And we had so much interest in this invention that we started, you know, basically started as a second job. And then when the month that the income from the second job overtook my main job, I thought, well, we probably should make this a serious company.

**Dave Jones:** Uh-huh. That's how all good companies start. They start in the garage as a part-time enterprise. Absolutely. And yeah. And then once it hits that tipping point, yep, see ya. Not working for the man anymore. That's terrific. So Pacton, so that was about mid and mid-90s, was it?

**Paul Thompson:** It was, 95. Yes.

**Dave Jones:** Right. And nobody else had done an electric fence fault monitor before. They just did the controller, which just powers the fence. Is that right?

**Paul Thompson:** There was, the fault finding tool, the best fault finding tool on the mark at the time was just a volt meter. So farmers had in their hand a device that told them what the voltage was on the fence. And they had all sorts of tricks to isolate faults. Basically, divide and conquer. Open a switch that does the voltage on the fence jump up. Okay, then I must have isolated the area of the fence with the fault. Not very intelligent design.

**Dave Jones:** So would they have like these switches installed periodically along the fence?

**Paul Thompson:** Correct.

**Dave Jones:** And they can just go and lift them? Okay, right.

**Paul Thompson:** Cut out switches.

**Dave Jones:** Got it.

**Paul Thompson:** So that was the technique. And basically, you know, looking for a drop in voltage was, you know, people who were a little bit more savvy would know that as they approached the fault, the voltage would drop. And there was all sorts of other crazy ideas. There was AM radios tuned off station to listen to the static of the, you know, basically looking for an arc on the electric fence, which might signify that there was a short.

**Dave Jones:** And you'd hear that, what, arc every couple of seconds or something?

**Paul Thompson:** Every second. So electric fence energizers, the predominant type of electric fence energizer now for many, many years has been a capacitive discharge circuit that pulses about once a second. And all of our safety standards and, you know, all of our design has gone into that type of circuit now for the last 20 years or so. Prior to that, there were some electric fence energizers, in fact, a lot in the US that were a simple step-up transformer. Hence the common knowledge, if you like, which is now wrong, that electric fence is a high voltage, low current. They used to be. It used to be a simple AC step-up transformer. And they were current limited and therefore they were safe because they didn't deliver enough current to cause electrocution. But they were dreadful at their job. It didn't take much load on the fence to drag the voltage down. So the capacity discharge circuit was kind of the third. There was an intermediate where people were using a catering ignition circuit, which is essentially the same as in the old motor car circuit, where you've got points that close on the primary of a transformer. Current builds up, you open the points and you get flyback and hence the spark.

**Dave Jones:** Right.

**Paul Thompson:** But again, the turns ratios on those transformers were such that the output impedance was quite high. So a capacitive discharge circuit's a low impedance output. It can deliver high voltage and high current and that's a much better device to put on an electric fence.

**Dave Jones:** But more dangerous?

**Paul Thompson:** It can be. Hence the rules. So like most engineers, we live in our standards. So there's a base standard for electric appliances under the IEC, which is 60335.1. And then there's our particular derivation for electric fence energizers, which is .2.76. And that's quite a weighty document. And there's a lot of really good science behind, you know, why if we adhere to that document, our products are safe. And that science, you know, that was done, had been done before I left university, which was in 1983. So it was well established.

**Dave Jones:** Are there different standards for like ones for animals, ones for humans, ones for like keeping people inside prisons? Because there's lethal ones as well, isn't there? There's like a dual mode one where it'll zap you first. And then if you keep going, it'll kill you. Is that right? There's. But that's not something you guys do, though. Right. You guys are more into the cattle control kind of field. Is that right?

**Paul Thompson:** Well, we started in the cattle area and then we found the need for security electric fence energizers. And these days, about 75% of our business is the security electric fencing. It's a huge industry. And you're quite right in that there are these well-defined sectors. So there's agricultural electric fencing sector, which is all about keeping animals in. There's security, which is all about keeping the bad guys either out of your house or out of your military establishment or there's prisons where it's about keeping the bad guys in. And you're right there. There is lethal electric fencing. But I think you'd be hard pressed to find any these days. I think South Africa and the US were the last to use lethal electric fencing. And South Africa turned all of theirs off at the end of apartheid. And I don't know of any in the US anymore. So, and you're right, we never touch the lethal electric fencing. We operate in the very safe, mandatedly safe area of electric fencing for humans and security. And it's only talking about the safety standards. The standards for agricultural and security only just diverged very recently. Until then, they were the same standard dictating the same limits for the pulses.

**Dave Jones:** So what made them split it out?

**Paul Thompson:** I was, I'm on the, an advisory group to the, to the IEC committee that, the drafts the standards. And essentially it was the fact that the agric people didn't understand what we were doing in security and why we had this need for a separate standard, doing things differently. And rather than become an argument, we started to diverge parts of the standard to cope with these, you know, two different areas. Just one obvious way that the energizers differ is that in agricultural electric fencing, you rarely use more than one electric fence energizer on a farm. Some farmers might use two, but they'll be on different parts of the farm, they'll be on different fences. Whereas security electric fences are zoned and each zone is powered by a different energizer. And for safety's sake, those energizers need to be synchronized. And that's just one of the small ways that security energizers are a lot more complicated than, than agricultural electric fence energizers.

**Dave Jones:** Do the agricultural ones, do they have more jewels behind them? For example, like does a big cow require, you know, a greater zap than a human? I would presume so. Is that right? Yeah.

**Paul Thompson:** Yeah. So the, there's been something of a, of a competition around the world to, for who can say that they've got the biggest electric fence energizer.

**Dave Jones:** Right.

**Paul Thompson:** And that's been going for quite some time. So the. Who's, who's currently winning that, you guys? Who's, who's the winner? We've, we've never been in that race though. Right.

**Dave Jones:** Okay.

**Paul Thompson:** We've, we didn't really see the point. And.

**Dave Jones:** Got it.

**Paul Thompson:** So engineers will appreciate that as, as you near the edge of, of anything, trying to get the biggest, the biggest, the fastest, the amount of engineering and the amount of costs goes up exponentially.

**Dave Jones:** It does. Yep. Yep. Very diminishing returns, so to speak.

**Paul Thompson:** That's, that's the word. Yes.

**Dave Jones:** Right. So you guys, so you're in Australia, you manufacture all your devices here. Is that right?

**Paul Thompson:** Uh, we try to keep a lot of our manufacturing in Australia, but, um, we have, uh, some customers in very price sensitive markets.

**Dave Jones:** Uh, of course. Yeah.

**Paul Thompson:** About 80% or so of, of, of what, of our turnover is, is actually, uh, exported. And, uh, some of those customers are in, for example, South America. So we sell to, uh, we have a, uh, a customer in Chile and, um, it's a price sensitive market. There are a lot of locally made, uh, products in, in places like, uh, Peru.

**Dave Jones:** Interesting.

**Paul Thompson:** In order to compete on price, we do have to have some of our stuff made in China. Um, it's, it's just a fact of life. The Chinese are very good at making electronics. A lot of our components, uh, come from, uh, China.

**Dave Jones:** What about, um, like, cause there's a few custom, well, custom transformers, uh, for example. Can we talk about, uh, transformer design? That's a good segue into transit. Cause you, you design one of the first, you design the magnetics in your original one. Do you still design your own custom transformers?

**Paul Thompson:** To a certain extent. I work, uh, closely with, uh, transformer specialists on that.

**Dave Jones:** Right.

**Paul Thompson:** It's not my forte. I have been forced to learn a lot more about it. You're right. I guess if you were to say what my specialization is, it's, it's microcontrollers. Before Pacton, I was employed, you know, writing assembly, uh, code in a 6805, uh, Motorola, Motorola microprocessors for, for weighing equipment. You know, 6809s, cut my teeth with HC11s, things like that. And a lot of assembly language, a lot of, a lot of squeezing, um, bites into little micros for low cost mass production. So yeah, magnetics, pulse transformers, um, interesting things because we're trying to get, we're trying to get a lot of power through the transformer equipment. So, uh, basically overall average power, if you like, if you'd look at what power, think about it in terms of the laws of thermodynamics, draw a box around it, what power is going in, what power is going out. And for the typical energizer, it's only about 10 Watts, but the instantaneous power output out of the transformers is, is, is enormous because we're talking about almost 10 kilovolts, you know, reasonable numbers of amps. So it's a instantaneous power wise in the tens of kilowatts. So that transformer is an interesting beast. It has to handle very high current, uh, through the primary. The, the inductance is important because we, we're trying to produce a very, uh, short, sharp, uh, pulse. So we've got to keep the, uh, primary inductance low. Hence the, the turns ratio on the primary is low. We've got to have a reasonable step up, but not too high. We do some of the step up in the primary. So we charge our primary capacitors to a, uh, you know, a reasonably high voltage, approaching 1000 volts on the primary. So our, a separate ratio of our transformer is typically between, uh, 10 to one and 20 to one, uh, depending on the, on the energizer we're producing. And the core, the other thing of course is, is we want the core to not saturate in a hard and sharp way. We want it to be a soft saturating core. So we're using a particular type of, uh, sintered iron core that gives us a, a softer saturation. So, uh, not all of our, uh, power is lost in, in, in I, I squared R losses once the, once the core saturates.

**Dave Jones:** So for those who don't know, it's basically a two-step process, right? There's a, there's a, a, uh, a first step up transformer, um, which is a, you know, switch via a MOSFET and that's intelligently controlled via the micro. And then that charges the capacitor bank on the secondary at, as you said, up to a thousand, 600 to a thousand volts, maybe. Yep. And then after that, you've got the output transformer, which is then driven via a high voltage SCR, which then dumps the energy to the output. Is that correct?

**Paul Thompson:** Absolutely. Yeah. So the, so the DCDCs, uh, PWM, we manage that from the micro. We've been using micros with PWM peripherals built in for a long time, quite successfully. And that reduces the part count, which is nice. The DCDC, of course, that's, it's, it's not, it's not a classic, uh, DCDC in that, that we've got a variable, uh, load, so to speak. When you, you think about a DCDC operating into a capacitor that's just been completely flattened. It's, it's as if it's operating into a short circuit. And at the other end, it's, it's topping up a capacitor that's almost at, um, you know, 900 odd volts. So it's almost like it's operating into an open circuit. So the DCDC transformer design is also a challenge, but not, not as much so as the pulse output transformer. And, um, yeah, capacitive discharge. So high voltage on, uh, on the caps. And then you, you switch on the SCR. Of course, those things switch on, but they don't switch off. They'll dump the whole capacitor straight into the, into the transformer.

**Dave Jones:** It will dump every joule into the fence. Is that the idea? Does it completely discharge or?

**Paul Thompson:** Yep. That's what you're hoping. And this, we managed the, the primary because of course the, we're using very low, uh, ESR capacitors. A pulse capacitor is essentially a metal film capacitor that's been, had its terminations beefed up. So it, it's, um, doesn't shock itself apart when you do this to it.

**Dave Jones:** Yep. In the teardown I did, you were using, um, Australian made, uh, Plesi capacitors. Do you know when they stopped making those here?

**Paul Thompson:** Well, look, it would have been in the late nineties, I believe. So we were still using Ferguson transformers.

**Dave Jones:** Yeah. Ferguson's. Yep. All of the Australians will know Ferguson transformers. Yeah.

**Paul Thompson:** Yes. And then, uh, there was a, there was a, there was another transform manufacturer in Sydney for a while. And I think it was AT something, ATA maybe. And they were taken over by a, a German company that was only interested in their fluorescent ballast transformer design. So they ceased, ceased making transformers for us. And, uh, then we went to New Zealand and, and found a little, uh, transformer specialist in New Zealand. And we were really fortunate that the guy over there was an absolute, uh, legend, uh, designer Bob Smith. You know, one of these, uh, old gray hair guys that, that knew everything from first principles.

**Dave Jones:** That was, uh, Markey Magnetics.

**Paul Thompson:** That's correct.

**Dave Jones:** So he was an old, uh, transformer gray beard.

**Paul Thompson:** Absolutely. Yep.

**Dave Jones:** Yeah.

**Paul Thompson:** The things he, the things he could tell you. I, I, long after he'd retired, I, I sought him out because I had a peculiar problem. Some of our apatrans transformers were, were burning a short circuit through a, through an interlayer winding. And it was happening in a particular part of the transformer. And I thought this can't be coincidence. There's something going on here. So, so I sought Bob out in his retirement and, um, showed in some teardowns and he said, oh yeah, I can see what's going on here. You've got a standing wave.

**Dave Jones:** Oh, a standing wave in the transformer. And then it would, it would, uh, arc over at a certain point, would it?

**Paul Thompson:** Certain point. So yeah, the, the fence, the tune circuit on, on a stub of fence, shooting a high frequency back to the, back to the output of the transformer and, and then just belting a transformer in a particular point of the output where that wave reached a maxima. And I'm glossing over the, the, the serious, um, complexity of that. Um, of course, really these, these old guys who could sit down and sketch out the, the equations, um, and do it all from first principles absolutely had my.

**Dave Jones:** Oh yeah, totally. Well, one other thing in the, uh, tear down of the old prototype unit, I noticed I haven't torn down your new one you sent me by the way. Thanks for that. I haven't torn it down yet, but I'll eventually get around to that. Um, was that, uh, you, because you sense the output voltage on the terminals and you feed that back via an opto coupler and the opto coupler was literally like a, uh, lead and a photo transistor, I presume inside a long, um, heat shrink, a custom, like, you know, just heat shrink tube. Can you tell us the story? I, I, I presumed in the video that you couldn't get an off the shelf opto that was good enough. So you just rolled your own as that.

**Paul Thompson:** Well, it's partially true. We did start with an off the shelf opto, but the, our particular safety standard that I mentioned before dictates that we need to have an isolation barrier between primary and secondary with a creepish distance of not less than 25 millimeters.

**Dave Jones:** Oh, 25.

**Paul Thompson:** Try finding an opto with lead spacing at 25 millimeters.

**Dave Jones:** 25 millimeters. Ooh. What is the biggest one out of interest? Would you know offhand? What is the biggest clearance one?

**Paul Thompson:** They are available up to about, um, rated at normal, uh, voltage of 4kV and the, the lead, lead spacing is about 13 to 14 millimeter, I believe on those packages. But when, when we looked at that package, we realized that essentially all it was, was the, uh, photo died and photo, uh, LED and photo died or photo transistor in a package. And we thought, well, we can do that. So, but we've, we've, we've made a much prettier one since then. We've, we've, uh, molded our own plastic.

**Dave Jones:** But it's still a custom, it's still a custom made job.

**Paul Thompson:** It is. It is still, uh, a matched, uh, infrared, LED photo transistor. And we're using it, we're using it in a linear part of the curve. So at about 10 milliamps, it's reasonably linear. And, uh, that was, I found that by mistake. I actually did a two opto. Um, I did an opto linearization using opt amps with an opto in either direction. Right.

**Dave Jones:** Because that's important because you actually sense the, sense the actual voltage, right? So it's got to be used. Well, it doesn't have to be linear. You could compensate in software, but it's nicer if it's linear.

**Paul Thompson:** Well, yeah, I did this, you know, complicated circuit. It's, it's probably one that I found in, in one of the old, uh, national linear data books to, to compensate a non-linear device with op amps. And then I, you know, I had the crow out and found that the linearization was doing nothing. I actually hit the, hit the devices in the linear part of their curve. Uh, happy accident.

**Dave Jones:** Uh, crow, crow, just for our, uh, American audience. Um, a crow is an oscilloscope here in Australia. Still is. Thank you very much. I just want to clarify. Yeah. Cathode ray oscilloscope. Crow. Oh, fantastic. So you dump all of the energy from the capacitors into the output once per second. And then how long does it take to recharge? Does it take almost a full second to recharge them?

**Paul Thompson:** Yeah. Well, it turns out the, the most efficient way to run your DC, DC, DC is to give it the maximum amount of time to do its job. Um, and we, on our bigger units, we're also doing intermediate feedback. So we're looking at the, uh, the rate of rise of the voltage on the capacitor. We're making sure that the caps aren't short and we're not going to cause a fire if we try and charge a shorted capacitor. Uh, the capacitors are under a lot of stress. The capacitors and the output transformers are the reason why electric fence energizers don't last forever.

**Dave Jones:** Okay. Right. Of course. Yeah. Cause you're just dumping massive amounts of energy every time. So there's going to be wear and tear on those, not only the caps, but your, uh, output transformer as well.

**Paul Thompson:** And you're correct.

**Dave Jones:** Even your, even your SCR might snot itself eventually, I would presume.

**Paul Thompson:** Yeah.

**Dave Jones:** Well, or are they fairly rugged?

**Paul Thompson:** They're a very rugged device, but you, you've got to turn them on hard. If you underdo the gate current on an SCR and it's presented with a, you know, it's trying to switch a, a, a, a high voltage capacitor and it's going to ramp up its cascade current very quickly. Uh, if you underdo the gate current, um, you'll find that there'll be regional, regional hotspots in the, in the SCR internally and they'll burn out. So yeah, good, good gating circuit. They're also the first in line if a, if a lightning strike comes in for an offense, it'll go through the transformer and, and, and, uh, zap the SCR. So we do, you will, you actually, you correctly pointed out in that one you tore down, you found some spark gaps on the, on the circuit board. So that's the first line of defense for lightning coming in because essentially where, you know, farmers are hanging in the aerial in the field on an electric fence saying, saying, come and zap me.

**Dave Jones:** I know, zap me. Yeah, that's right. Is that common? Like how often would they get zapped? Are they like more, like, does it happen like every, you know, lightning storm or?

**Paul Thompson:** Every lightning season we get a, you know, we get an influx of, of, uh, uh, uh, people presenting us with dead energizers and or wanting to buy new ones. And sometimes it's very obvious. I could send you a picture that shows that there was a lightning strike and an energizer was on the wall. And after the lightning strike, bits of the energizer were all across the floor.

**Dave Jones:** Oh yes. Please send the photo. Everyone loves destruction.

**Paul Thompson:** It was black and charred. Yeah. The good thing was, you know, my comment as, you know, as an engineer involved in the, in the safety center, my comment back to them was, well, you know, I'm really glad to see that everything's self extinguished. Yeah.

**Dave Jones:** Oh, so how, how big do you spark? Do you use MOVs or do you prefer MOVs or spark apps or what, which is better and how big do they have to be? Or is you can't simply can't get them big enough for they're going to eventually.

**Paul Thompson:** Lightning, lightning is a whole area of expertise. And it was, I was lucky enough to do my final thesis at UQ, University of Queensland here in Brisbane on lightning.

**Dave Jones:** Oh, wow.

**Paul Thompson:** The trick is to stop it before it gets into your box. So we encourage farmers to put a lightning diverter out on their fence. If they can divert the energy before it gets to our box, that's great. And then we put, you know, secondary and tertiary on our board. So there's a spark gap near the terminals in case it's coming in. Then there's, then there's MOVs, then there's our transformer. And then on the primary, we're, we're looking to, to capture reverse pulses because of course you can't dictate what polarity the lightning strike is going to come in on the wire. For those of you know a little bit about lightning, there are the majority of lightning pulses are at a particular polarity. And then every now and again, there's one on the opposite and that's usually the worst.

**Dave Jones:** How does it, how does the polar, I didn't know nothing about lightning. I think it's fascinating how, because ones can go from the ground upwards or from the sky down, can't they? Does that determine the polarity? How does that?

**Paul Thompson:** No, no, it's the, it's the shape of the thundercloud. So typically there's a shape. The thundercloud is a dipole. So a big dipole is built up in a thundercloud, the underside of the thundercloud. And forgive me, but I've forgotten the actual polarity. That's all right.

**Dave Jones:** It's about 30 years, right? 40 years.

**Paul Thompson:** It is a while ago. I think the bottom of the cloud is negative. And that then induces charge on the land underneath it. And then you get the leader stroke, which actually comes up from the ground. And no one ever sees that. The start of the leader stroke is also known as St. Elmo's fire. And people do see that. So a corona built up on a sharp object on the ground, a leader stroke or a stream of ions goes up towards the cloud and that opens up a charged path. And then the lightning strike comes down from the bottom of the cloud. But as a thunderstorm passes, sometimes the cloud can be skewed by winds. And that reveals the top charged section of the cloud above ground. And that's the great thumping big strike at the end of the storm that can do a lot of damage.

**Dave Jones:** That's fascinating. How do these lightning arresters work on these fences? Are they just giant spark gaps in their own right?

**Paul Thompson:** The simplest is a spark gap. So the simplest lightning diverter of all is simply a spark gap. So you tune the spark gap so that it won't arc over with our normal electric fence voltages. And then lightning strikes the fence and races down the fence wire, finds the spark gap as the easiest path to ground. And that then limits the voltage surge that can come along the rest of the wire and hits your energizer. But we make a more complex one, which is a multi-stage device. We pot up a three-stage lightning arrestor in epoxy so that we can shrink it down using the epoxy as the insulation. And that one's got a spark gap, an inductor, metal oxide varistors. And in the center, we put an LC circuit. And then we go out the other side with the mirror image. We joke that that's because we can't trust a farmer to put it around the right way on a fence, which is a little bit demeaning to farmers. But in reality, it was the easiest way of making it. We made it as a T filter. And on either end, there's a lightning arrestor. And the other reason for that is that when a farmer puts it out on the fence, it's actually possible for the surge to come in either direction to the lightning arrestor. So we made it symmetric.

**Paul Thompson:** A couple weeks ago, we heard from Daniel from Keysight talking about ESD and test equipment. I was pretty surprised to find out some of the things that could damage equipment, but there's actually more.

**Chris Gammell:** There's other things you can do to keep your stuff safe. So one of the things that people miss is this inductive charging. So if you have materials, often it's packing materials. So you get a box from somewhere. It's either your boards or someone shipped you the equipment or even rolled it down the hallway on a cart. That's all building up charge. So one of the worst culprits is that pink packaging material that you see all the time. If you have those materials around, keep them like a foot or more away from your exposed assemblies. So that just keeps it from inductively charging. So you have this charged up material and it's going to inductively charge things around it. So your boards are included in that. If you're transporting them around, put your boards in static bags, kind of that standard stuff, and then make sure you're grounded and your mats grounded when you're actually handling your boards.

**Paul Thompson:** I'd never heard that about pink foam before, but I thought that was super interesting. And it left me wondering, what else can we be doing to keep ourselves safe?

**Chris Gammell:** When you go to look into ESD best practices, you see a lot of here's how to protect your boards and here's how to protect your manufacturing line. But what you don't see is here's how to protect your equipment. Because what happens is your board gets charged up and maybe that's okay. Often that's not going to be a problem. But as soon as you cable it up and go to connect it into your input, if that center conductor of your cable goes into the center conductor of your input, then all the charge on your board is going right into your equipment. And that's where we're seeing the damage.

**Paul Thompson:** You may remember that all of this information is available as app notes and as videos. And it's also being shared as part of Keysight Wave, which is a contest that's coming up from Keysight starting March 2nd of 2020. You can enter and win a wide range of test equipment from Keysight.

**Chris Gammell:** Make sure I say that's right. Every day we're giving away five 200 megahertz, 1000X series oscilloscopes, four channel. We're also giving away five of the nice handheld DMMs, 1282. And those are great. I have one at home, one on my desk. I use them all the time. And then we also have a sort of grand prize winner each day. And they can choose their pick of like a scope or a DMM or a system, like a power supply system. There's also some RF stuff in there. So there's a signal source, if I recall. And then on Fridays, we have like a big draw. So you can pull one of your choices is a FieldFox, which is like a combo signal analyzer, VNA. And there's also, I think, a USB vector network analyzer, like the P5000. It's really cool. It's super small and it's great.

**Paul Thompson:** Keysight is offering AmpHour listeners two entries for every time they put one entry in. You can enter right now and drawing start on March 2nd of 2020. You'll also get access to app notes and videos and a bunch of other things, not to mention a chance to win all of those great prizes that Daniel just listed. So go check that out. It's bit.ly slash AmpHourWave. That's B-I-T dot L-Y slash AmpHourWave. The A, the H, and the W are all capitalized. And now back to the show.

**Dave Jones:** Back to the transformer design. In one of your emails to me, you mentioned that the design of the transformer, well, the design was all about doing a term I'd never heard before, which is a soliton pulse shape. And I had to look that up and it looks very much like a bell curve. What is a soliton pulse shape? And why do you want, why is that like an, is that an ideal electric fence pulse shape?

**Paul Thompson:** Or so a soliton, I guess if you would define a soliton wave, it's a solitary wave. Solitons in nature, think of tsunami. So a tsunami is a wave that travels across the surface of the ocean for long distances and retains a lot of energy as it travels. And it's, it's almost a singular, singular wave. Another way of defining a soliton is it's the perfect wave shape to travel undiminished in a particular transmission line or on a particular transmission line. Solitons are used in fiber optics. I guess it's remained a bit of a curiosity to, to most people in the world, but it's the perfect wave shape for a pulse of electricity on an electric fence. All things being equal, you can't, we can't dictate how a farmer builds their electric fence. They could use a single wire, two wires, three wires. That changes the characteristics of the electric fence as a transmission line. And electric fences start to attain transmission line characteristics when they, when their length exceeds around five kilometers. And, and again, I've taken an oscilloscope out to electric fences and, and check this. And you really start to get, you start to get a, a, a deterministic, uh, um, input impedance. So even though you might put a short circuit on the fence at a point beyond say six, seven kilometers, you actually don't see any change to the, to the, to the input impedance, the, the looking into the electric fence because it's become a transmission line. It's got a fixed, uh, impedance.

**Dave Jones:** Interesting. Ah, fascinating. And is that based, what's that based on the, what length is that five kilometers based on? Is that based on the, the timing of the pulse or?

**Paul Thompson:** The, the wavelength essentially. So the, the, so if you think about, if you start to think about it in terms of frequencies and frequency response, we're jamming a short, sharp pulse in there. It's got the majority of its power at, at, at a certain frequency and above multiples thereof. And that's, that is high enough for a, for that single wire strung above ground to act as a transmission line at, at around those distances. I mentioned five kilometers and beyond.

**Dave Jones:** Right. What's, uh, five kilometers in weight, in, uh, frequency.

**Paul Thompson:** Oh, goodness.

**Dave Jones:** I could get my calculator out, but I can't see it. Anyway, it's, it's a long wavelength. Anyway, let's put it that way.

**Paul Thompson:** Yeah. Look, it's, it's, it's, it's tens, tens to hundreds of kilohertz. Yeah.

**Dave Jones:** It's, it's, it's, yeah, it's incredible. Right. So that, so that, that sort of bell like, bell curve like is how I'm going to explain it. Cause unless you've, you can see an image, it's almost identical to a bell curve, really. Um, bell shape.

**Paul Thompson:** When, when you, the perfect soliton for an electric fence and a way to analyze or find, find the soliton wave shape is to, is to jam a, uh, an impulse, a perfect impulse into the transmission line and see what got to the end.

**Dave Jones:** Yeah, of course. So you just put a short, sharp pulse in and then check it out. Yep. That's a common way to.

**Paul Thompson:** See what gets to the end because everything else is going to be filtered out. Another way of thinking about, you know, electric fence design is that it's pointless. It's pointless throwing a pulse shape into the start of the fence that doesn't get to the end. So, you know, figure out the pulse shape that's getting to the end. That's the pulse that's traveling. That's, that's what you really want to generate. Any energy that you're, that you're putting into the fence that's outside of that curve is just wasted. It's going to be reflected back, reflected back or soaked up by, uh, uh, capacitive effects.

**Dave Jones:** And that's why you want to shoot for that perfect solitron, solitron shape is because there will be in theory, zero losses, zero energy lost on that transmission line in theory.

**Paul Thompson:** In theory. And of course, going back to what I said before, we can't dictate how they build their fence. And, uh, also the electric fence is a very lossy, um, transmission line. Um, for a start, they're using steel wire, which has an impedance of around 40 ohms per kilometer.

**Dave Jones:** I was going to ask about that. Yeah.

**Paul Thompson:** And then there's, there's grass and cobwebs and dusty insulators and yeah. So, but of course the object is to try and get the highest voltage possible on, on, at the end of the fence. As far as the quality of an electric fence is concerned, the, the measure of quality is, you know, what's the zap like, you know, the far, in terms of a farmer, he says, you know, is it going to zap my cow and keep it in the paddock? And we translate that to how good's the voltage at the end of the fence. So let's, let's make an energizer that does the best at getting the best voltage to the end of the fence.

**Dave Jones:** Got it. So, so do you have a tester that can go on the end of the fence at, at that particular wavelength and well, and, and check that because one of your, you said before, one of your, your first product was literally a, uh, electric fence monitor, like fault monitor kind of thing. And you still make those these days. So an electric fence is capacitively, it's basically a capacitive load. Yep. Right. So can you tell us about how you actually, how can you determine where you said you can determine a fault within one in a thousand or something? So if it's one kilometer long, you can get to a meter. Tell us how you can do that.

**Paul Thompson:** I mentioned before that a lot of our business these days is in security and security electric fencing. Um, there's, there's kind of a crossover between agriculture and security and that's the, um, what they call game parks in South Africa. Um, most of you are probably aware of, uh, a place called Kruger National Park in South Africa. Yes. Where they have rhino, they have the big four, they have, you know, rhinos, uh, lions, elephants. It's a beautiful place to be. I've been fortunate enough that my job has taken me there and I've literally put, you know, through attenuators, put oscilloscopes on the fence at Kruger National Park and had a look at the waveforms.

**Dave Jones:** Fantastic.

**Paul Thompson:** Um, but those, those fences are under, uh, a lot of pressure from both directions. So, you know, things like rhinos would like to get out of the, through the fence, especially when there's another rhino on the other side and they want to have a fight. Male rhinos tend to be territorial. And then there's, there's, there's poachers trying to get in. And this is the, the bit that, you know, I guess I'm most passionate about is that, that our technology is being used to protect, uh, rhinos, uh, in South Africa. Nice. Against poaching. So we, we determined that, you know, these, these security electric fences were already being wired in loops, which is something you can't convince an Australian farmer to wire his fence in a big long loop because, you know. Why is that? Well, it just, it's just not convenient for them. It's convenient for them to make a tree shape or, or a grid or a mesh. But, you know, when, when you're talking to installers at places like Kruger, they're listening. They're saying, how can I make the best fence? And we say, well, we need to know that it's working. So you need to wire it out and back in a loop so we can bring the, the, uh, voltage back to the energizer slash monitor to be monitoring that every pulse that we send out is getting, you know, all the way out there and back again. And we can do that on a straight line fence by going, you know, out on some wires, turn around at a certain point and come back again on some other wires on the fence. And these, these game park fences in South Africa.

**Dave Jones:** So you've got to have a, a return wire physically installed on the fence. Okay.

**Paul Thompson:** Feed and, feed and return. And, and for a, for a security application, that return can be a single live wire. So you might, you might have a security electric fence often looks like a massive number of wires. You can have upwards of 20, uh, live wires on a security electric fence that's keeping people out. On these crossover fences in, for game parks, they typically have six to maybe 10 live wires. They're pretty tall fences. They're six foot fences and they'll have live wires on either side and sometimes also on the top, um, because elephants will, um, provide downward pressure on the fence to try and break a fence. So there's a number of live wires that you can then decide, well, okay, I'm going to use, I'm going to use four out, uh, three back. So there's a point, a dividing point on the fence. That's the end of one zone and the start of the next. Once we started looking at the waveforms, we, we realized that if we analyze the current and particularly if we analyze the real current. So now we're getting into real and reactive currents.

**Dave Jones:** Exactly. Yeah. You have to, because it's a capacitive load.

**Paul Thompson:** The reactive currents are circulating. They're there all the time and they're large and they've got nothing to do with faults on the fence. And so reactive currents are because of the capacitance and to a, to a lesser extent, the inductance of these long wires. And we said, well, okay, if we can look at the real current and we can tell where that current is going, we can find a fault, especially if we can, if we look at a big loop of fence and we can ask the, the installer to make that loop, uh, as symmetric as possible. So now we're talking more about having an even number of live wires. So, say, say three going out, three going back, one big loop of, of live wire. And we actually feed, we have, we split our pulse at the start and we feed in two directions. And we look at the, we analyze the signal going in those two directions. And by simple, you know, differential by saying, okay, if there's no fault on the fence, then there's the signals in particular. Now the, the real currents should be equal. There should be a point at exactly 50% along this fence where the current's null. And if there's a fault, that's going to upset that null. And we're going to be able to work out where that fault is. The first time I sketched this out, it was a page of, of math. It's, it's not, it's not rocket science, but it, it is some math. And we've now got that into a device and it's, it's accuracy. It's actually measured accuracy is one part in 10,000. That's the accuracy of the math. Nice. But the, in reality on a fence, it's about one part in 1000. And if we're talking about five to 10 kilometers of fence, that's still only relatively short position on the fence, which means that we can put that up on a mimic screen in a control center for, for, for a park and they get an alarm. And then it says, okay, on the map, it's this point on the fence, sector 19, you know, on this fence, it's just West of such and such gateway. And they send the guys out with the AK 47s, which is when you realize it's serious.

**Dave Jones:** Uh-huh. Wow. So you can detect opens, shorts, heavy loads, maybe how, what different?

**Paul Thompson:** All three by different, by different measurement techniques. We can tell if the fence is completely healthy. That's the easiest thing. We can determine that there's a, there's a hard fault. In other words, there's a short, there's current bleeding out somewhere. Uh-huh. We can determine an open circuit because we lose continuity and we can determine a poor fence. In other words, a maintenance condition. You'll appreciate a lot of, a lot of fences in parks like this. There's a, in the tropics, for example, there's all sorts of succulent weeds that want to grow over your fence.

**Dave Jones:** You're right.

**Paul Thompson:** And, uh, some of those will actually arc. So you need to, uh.

**Dave Jones:** Oh yeah, of course. Yeah.

**Paul Thompson:** Yep.

**Dave Jones:** So, so do you do all of this detection using the actual, uh, pulse itself or do you like switch out the pulse and put in other detection circuitry periodically?

**Paul Thompson:** Now we're getting into some of our secrets, uh, Dave.

**Dave Jones:** Ah, I knew it. I could sense it. My spidey sense went, am I, my, that was my design spidey sense. So yeah, I'd probably do something like that.

**Paul Thompson:** It's probably superimposed, superimposed another signal to, to do another job for you.

**Dave Jones:** I'm sure you've got patents on this and people can read all about it. So it's not secret. You just can't copy it, right?

**Paul Thompson:** Well, the patents, patents give you a degree of time of secrecy. So patent, patent will do things for you. Uh, it's, you, you drop a patent in when you, when you think you've got a good idea in the Australian system. That means we've got 12 months to then put a full provisional in.

**Dave Jones:** Yes.

**Paul Thompson:** To a certain extent, the patent is largely invisible until it starts to be challenged or starts to get to the later stages. So you won't be able to search online for that particular patent. But once it goes through, after about two years, basically, it starts to be revealed. Yeah. So for a while, we've got the best of both worlds. We're keeping it secret and we're patenting it.

**Dave Jones:** Let's just say that you don't just use the pulse. There are other things at play. Okay. Okay. Got it. So what can you do if you've just got a typical farm and all they've got is just one fence that you don't have a return loop? You've just got the one wire going out. Can you do anything to detect? Can you do like a TDR time of flight thing, get the reflection back to determine faults?

**Paul Thompson:** You can. I've still got a box at work from when one of my engineers started down that track of TDR and I pulled the plug on that because it started to get too complicated.

**Dave Jones:** It could quickly, I'm sure. Yeah.

**Paul Thompson:** For those that know TDR, think of a hairy caterpillar.

**Dave Jones:** Hairy caterpillar. Okay. This is a new analogy.

**Paul Thompson:** That was what the signals were looking like. So we weren't getting a clean echo. With TDR, you're looking for a clean echo at a particular time.

**Dave Jones:** Yes, of course. Yep.

**Paul Thompson:** And ours was more like a hairy caterpillar. We were getting echoes and glitches everywhere.

**Dave Jones:** Is that because the nature of the, you know, there's all the poles and there might be a little bit of, you know, loads all the way along? Is that the...

**Paul Thompson:** Farmers tie wires together and each one of those is a reflection.

**Dave Jones:** Yeah, of course. Oh, of course.

**Paul Thompson:** Yep. Got it. Hence, I pulled the plug on that. There's easier ways for doing it. One of the ways is to put a sentinel type device out on the fence to report that the voltage has got to a particular point.

**Dave Jones:** Oh, okay. So that's a wireless thing, is it? Yep.

**Paul Thompson:** Yep. So we've got a, we've got a, what we call an IP monitor, which goes out on the fence. But for the, you know, 99.9% of farmers out there, they'll rely on the reading from the electric fence energizer. So we, we, we've got IP electric fence energizers as well, and they can look on their phone. And if they see a slight drop in the voltage at the energizer, that gives them a clue that perhaps there's a fault on a fence. And then they can go and test, test the fence with their, uh, volt meter. For more serious farmers, we actually do put the, we put the security type, uh, gear to work for them. So we build electric fence stations, which are field cabinets, solar powered, uh, report, uh, um, to the cloud, then to their phone. And, and those fence stations are looking at the, the current. Sometimes, as I said before, it's hard to get Australian farmers to, to put a return wire in. But if they do put the return wire in, because they, they don't want to waste a wire on their fence. Australian farmers are typically going to got four or five wires. They want every one of those to be a wire that zaps the cattle, not, not this, uh, return wire. That's its only job is to tell them that the fence is working good at the end. Until of course, it's not working well at the end.

**Dave Jones:** And then they come back and say, why didn't we do that? Oh boy. Why are there three terminals on your electric fence controllers? There's an earth terminal and there's two other terminals. Why?

**Paul Thompson:** Sure. There's, there's two, two possible ways of using that center terminal. The first is to use it as a lower power output. So for example, if, if, if I owned a farm and I had my farmhouse and I had some, some paddocks and fences that were close to the farmhouse, I might consider running those particular, uh, fences off the lower power. So instead of eight to nine KV, they'd be getting, you know, four, four and a half KV on those wires. And, and that's because if, you know, if, if, uh, my niece or nephew visits, they're not going to get, uh, the full zap of the high voltage. Uh, I'm being kind.

**Dave Jones:** Got it. Right. So that, that's all it is. It's just a divider on the output. It's a tap on the transformer. Is it?

**Paul Thompson:** It's a, we do it. We were the first to do it as a center tap on the output transformer because that actually gives us a second, um, uh, a second thing we can do with the, those three terminals. And I didn't invent this. Uh, I think I called Andrew McKean, an Australian engineer with another company, electric fence, old electric fence company in Australia invented this. And it's a system called bipolar. So the center trap, the center tap, the center terminal, if you like, goes to ground. And then you've got a balanced plus or minus output from the, from the other two. So you can have sets of balanced positive and negative wires on your electric fence. And now the attraction of doing that is that with a normal electric fence, let's call it conventional. You've got, you've got your earth in the ground. So the electric fence energizer at one terminal is earthed in the ground. You've got your live wires on the fence, something walking up to that fence, a cow touches the fence. It's getting a shock from the live wire through its feet and it's an earth return. A slightly more sophisticated method and one that we employ in the game fences and security fences is to have earth wires on the fence and they're wired all the way back to the energizer. So now if somebody is pressing through that fence, they're going to get a shock from the live wire and an earth wire. So that's, you know, that's the best way of doing a conventional electric fence. And a lot of Australian farmers are doing it that way. Now their, their live wires are, are, can give a shock to ground, but they can also give a shock to the non-live wires in the fence. And Australian farmers use a lot of metal in the fence. So farm fences vary drastically around the world and even regionally in Australia. Australian farmers use a thing called a star picket in America. That would be a T post and that's the intermediate post on the fence. And that's good for us for electric fencing because it means any wire touching that steel post can be used as a, as a, an extension of the earth. So those wires can be wired all the way back to the fence earth.

**Dave Jones:** Oh, of course. Yeah. That would give you a much better earthing system, wouldn't it?

**Paul Thompson:** Yep. Distributed. But with bipolar, you're really, there are situations where it's hard for the animal. It's hard for the animal to get a shock with respect to its feet on the ground. And there's, there's two, two reasons for that. You can have dry sandy soil. So you've got a hoothed animal on dry sandy soil and it's not well earthed. So you might, you might have about five, 6,000 volts on that live wire, but it's not going to deliver much of a shock if the animal is not well earthed. The other situation is in, this was brought to my attention by a gentleman in Canada who said that when they're grazing cattle in the winter on icy ground, you've got the same problem. Icy ground is not conductive. And that's kind of counterintuitive, isn't it?

**Dave Jones:** It is. How, how so?

**Paul Thompson:** Well, all the, all of the ions are bound in, in what is essentially a solid ice and they're not available to flow.

**Dave Jones:** So, right.

**Paul Thompson:** So it's, yeah, okay.

**Dave Jones:** Yeah. I've never thought about that. Wow. Wow. That's fascinating.

**Paul Thompson:** Yeah. So bipolar gets around this by having these multiple live wires on the electric fence and, and they don't do a lot when you, they give you a little bit of a shock if you touch either live wire, but if the animal persists and tries to go through the fence, it'll strike two live wires.

**Dave Jones:** They'll touch both. Right.

**Paul Thompson:** Yeah.

**Dave Jones:** Because in, in theory, if you're trying to stop people from getting in and you've only got an earth based system, if they're not touching earth, they're not going to get the zap. So they can, you know, go in with their huge one inch thick rubber sole sneakers, couldn't they? And not in theory and not, not get zapped.

**Paul Thompson:** They could. And this, this area of security electric fencing is an arms race in that, you know, we, we initially, of course, electric fences were put up. They were big and scary. People didn't touch them. And then after a while, our criminals started to work out that they could spread the wires, that, that half the wires were earth so that they could, they could cut the earth wires, reveal a big enough space to crawl through. And there's all sorts of countermeasures that we've now been working into the system. For example, we, we can detect, we can detect when they've cut the earth wires.

**Dave Jones:** Oh, okay. That's interesting. How do you do that? Or is that secret squirrel stuff?

**Paul Thompson:** No, we're just running continuity on the, on the earth wires.

**Dave Jones:** Oh, okay.

**Paul Thompson:** Right.

**Dave Jones:** Okay.

**Paul Thompson:** We can also put sensors on the fence that detect a change in tension on the, on the wires. So if people are attempting to spread the wires to create a space, we can detect the change in tension on those wires.

**Dave Jones:** Oh, how do you do that?

**Paul Thompson:** There's, there's mechanical ways of doing it. So you, you simply rig up. Of course. You rig up a, a, a ferrule, if you like, that, that is bonded to the wire. And if, as they put tension on the wire, it pulls that and shorts it to something. So that's the, that's the, the older method, but we're actually using load cell type technology.

**Dave Jones:** Right. So it's a strain gauge thing. And yeah.

**Paul Thompson:** Yep. Yep. Over tension and, and a white goes.

**Dave Jones:** Cause yeah. Cause I was, the reason I was a bit shocked there is cause I couldn't immediately off the top of my head, figure out how you do that electrically. So yeah, it's about installing stuff on the wires and measuring tension and right.

**Paul Thompson:** Countermeasures, as I said, with, in a lot of countries, there are very rich people living close to very poor people. And, and the differential can be, for example, in Johannesburg, you can have, you know, the average doe has his house in the suburbs like I have here, but he has an electric fence around it because the break-in situation is just so bad that they're, they're stopping them at the, at the fence with an electric fence. It sounds terrible. Yeah. And it's, you know, it's something unconscionable. You know, we wouldn't consider doing it here in Australia, but of course in South Africa, it's a, it's something they've grown up with over the last 10 or 20 years. That's been one of the classic things that they use. Like we use bars on our windows, you know, in places here in Australia where, where break-ins are prevalent, people will put bars and security girls in the windows. In South Africa, they put up a security electric fence and it's not only South Africa, South America, parts of China even. And as I said, big, big market, a little bit sad in a way that there's, there's people that are that desperate that they're, they're trying to steal from the neighbors, but you can understand people attempting to stop that.

**Dave Jones:** Of course. Yeah. So you guys, how many units would you be manufacturing and selling a year? How, how big is the electric fence market and what, what market share do you guys have? I mean, you're one of the biggest.

**Paul Thompson:** Have you got any numbers for that? Interestingly, we're, we're one of the biggest in some countries around the world and in some key markets. We've actually only got a little percentage of our home market in Australia, which is a bit frustrating.

**Dave Jones:** Oh, really? That, that is unusual. Yeah. Why?

**Paul Thompson:** Well, we kind of, we're a born exporter because of the, the nature of the product that we, we made, we were immediately tempted to export and we did. Then, you know, opportunity kept arising outside of Australia and it's only more recently that we started to focus on the Australian market. But the, the Australian market for electric fence energizers is tens of thousands of, of, of units per annum, but mainly, mainly in the agric space. So it's, it's, it's a niche market. You know, those, those in the, in the business of electronics will realize that that doesn't hit the millions that's required.

**Dave Jones:** No, that, no, it's right. You know, thousands, tens of thousands is a decent niche market.

**Paul Thompson:** Correct. And we, so because we're selling all around the world, we're making about 10 to 20,000 units per annum out of our factory in Narangba. And we also arrange for some product to be made in other factories and ship direct to customers. So we're, we're closing in, we've passed our 400,000th product in the life of the company. And we'll, we'll, we'll close in on, on half a million sometime in the next 12 months.

**Dave Jones:** Very nice. Now, one of the things I, uh, uh, sort of, uh, gushed over in my video was that, um, you guys have repair guides for these things. I was stunned. Like it's so like, it's virtually non-existent to get repair guides of stuff these days. Why, why do you offer these very comprehensive repair guides with like, you know, a comprehensive troubleshooting and, and, and all sorts of stuff?

**Paul Thompson:** Well, um, being a relatively small company and having customers all around the world, we have to give a lot of long distance tech support. So having, having a good, uh, you know, paper, uh, repair guide, and of course it's on the, on the web these days. Of course it would pay dividends. It does pay dividends. Our distributors like to, to repair the stuff themselves. They don't want to try and send it back because it costs a lot of money.

**Dave Jones:** Okay. Um, yeah.

**Paul Thompson:** And, um, so long as they've got a tech who can read a, a, a multimeter, you might've realized the repair guides were, were quite low level. So they were.

**Dave Jones:** Oh yes, absolutely.

**Paul Thompson:** Yep. We aim them at people who are not engineers, sometimes not even technicians, but are able to use a multimeter. And we insist, we actually test them before we authorize a tech repair that they can use a multimeter. They can do a diode test. They can do continuity. They can look for a short circuit. They can measure voltages of various sorts. And by a step-by-step process, it turns out that you can solve and repair about 80% or so of the faults in the electric vents energizer. If you use those simple techniques, because as I said before, there's some components that are certainly overrepresented in, in the failure modes.

**Dave Jones:** Right. Yep. Well, I'm looking at one of the repair guys now and he is like step nine, check or replace Q4, you know, like check or replace this MOSFET because you've gotten to that point where, aha, it's most likely that's the thing that's failed.

**Paul Thompson:** Yep. So if you.

**Dave Jones:** Fantastic.

**Paul Thompson:** Again, divide and contra is a great way of repairing things. Yeah. So if you, if you start with the most obvious and work through and each one of those steps is attempting to divide down where the fault might be. And then we have a table at the end, which is the, you know, the faults that we've isolated by that method. And it might be only 10 or 11 of the, of the possible, you know, plethora of different faults and electric vents energizer might have, but they are the top, they're the top percentage wise of the faults that those things can have. And thereby if we give people the tools to do those simple checks, they can find and repair the energizers. And it's just remarkable how good these guys get. I've been taught over the years not to judge by somebody's schooling or, you know.

**Dave Jones:** Of course.

**Paul Thompson:** Because I've seen a guy who was a storeman in Texas become a good repair, repair technician for electric fence energizers.

**Dave Jones:** Absolutely.

**Paul Thompson:** He taught himself. And it was.

**Dave Jones:** Yeah.

**Paul Thompson:** Now he does it. And he eats very fast. That's fantastic.

**Dave Jones:** And you sell, and you sell even spare parts on eBay. You sell spare pulse capacitors and spare transformers. And so people really want to repair themselves if they've got a lightning strike and it takes out the transformer.

**Paul Thompson:** Well, individuals shouldn't repair them themselves because they could hurt themselves. Right. Worse still, if they're working on a mains powered energizer, they could make the unit unsafe. But there are a number of qualified technicians around Australia. And we just found it easier than, because these tend to be very small sales for us. We're a wholesaler. We're geared for selling, you know, a thousand energizers at a time. To sell an individual capacitor to Joe Bloggs to repair an energizer costs us more an admin than we're ever going to make in that sale. So putting them up on eBay was just a brilliant move. And it just saved us a lot of time. And there'll be, you know, one or two sales a month of these spare parts. And the guys have told me, the repairers have told me that they appreciate just being able to jump on and order it when they need it.

**Dave Jones:** Oh, absolutely. That's fantastic. I was absolutely amazed about the repair guides and that you had an eBay store selling parts. I just couldn't believe it. I was gobsmacked. But of course, that's what this sort of niche industry sort of, not demands, but sort of real, you know, you sort of work your way into the point where, okay, that makes sense.

**Paul Thompson:** Well, it does because if you, because it's a niche and because we've got so many custom parts, you can't just go to a Farnell Element 14 and buy an output transformer or a pulse capacitor.

**Dave Jones:** No, that's right. So you've got to offer them. And yeah, wow. Swack it on eBay. Absolutely fantastic. Thank you. Well, our hour's almost up, but I'm going to, one last thing is that more towards your expertise is the microcontroller side of things. The original one, the original prototype that I found in the dumpster, it had a PIC micro. Why did you choose PIC back in the day? I think I know the answer. And what are you using these days?

**Paul Thompson:** Very good question. We were one of the first to put a microcontroller into an electric fence energizer. Putting a micro back in the day, back in the mid to late 90s, putting a micro within a few centimeters of a pulse discharge capacitor.

**Dave Jones:** Yeah.

**Paul Thompson:** You know, had the obvious consequence.

**Dave Jones:** Yeah.

**Paul Thompson:** You know, some large manufacturers who I won't name actually went to market with units that were so unstable, they would just regularly reset themselves. One of them even had a reset counter.

**Dave Jones:** Oh, really? It's got an internal reset counter in like E squared prom or something?

**Paul Thompson:** It was actually displayable so that the, I guess because the engineers wanted to know what actually happened when it went to the field. And any sort of arc on the fence would cause it to reset itself each pulse. Not funny when you're the engineer trying to make a product. No, of course. So we lined up a few different brands at the time. I'd been using Motorola since I left university. So as I mentioned before, the venerable old 6.8 series, and we tried to, we tried to, but they, we could not get them stable. We decided our test was that we would take the, a couple of wires from the output of the energizer, create an arc, and we had to make that arc above the microcontroller on the circuit board and, and not have it reset. So that was the, that was the proof. The proof test was if it, if it's stable, it's not going to, it's not going to reset with an arc that close to it. Because that can happen, that can happen.

**Dave Jones:** Yeah. But is this like, but that's going to be layout dependent and decoupling dependent and stuff like that. So how do you.

**Paul Thompson:** We had to start with a micro that was stable enough as well. But yes, then, then it's the, then it's the layout. And I, I was lucky enough to have come out of audio when, when I was a kid, I played with electronics and my first love was, you know, audio amplifiers, guitar amplifiers, that sort of thing. And if you don't get the layout right, you get nothing but hum. So I looked, I learned about, I learned about star earthing and.

**Dave Jones:** Star grounding. Yeah.

**Paul Thompson:** Yep. So look, applying those sort of principles to the, to the circuit board for electric fence energizer is pretty important. You need to know what you're doing with your earthing, where your earth nets are and what they do. Otherwise, yeah, you can end up with part of the, part of the discharge pulse on your five volt rail and then you've got no chance.

**Dave Jones:** I'm, I'm surprised to hear an electric fence guy use the term earth in regards to circuit ground. Is that, is that, is that just a habit? But like, do you call in electric fences, do you call the earth earth or do you call it ground? So there, so the terms are interchangeable.

**Paul Thompson:** We, we feel they're interchangeable and that's just one of the few terms like that in electric fencing. The other one is, you know, ground rod. Is it a ground rod, an earth spike? What is it? There's six, six different ways of talking about the same thing.

**Dave Jones:** Yeah. Right. So you chose a pick. The pick was what was just the best in these tests?

**Paul Thompson:** It survived. It was low cost. At the time we were using the one-time program board. So gee, I can't even remember the numbers. Yeah.

**Dave Jones:** The, the, that would be the pick 16Cs that, that, because they flash hadn't come out then. Yeah.

**Paul Thompson:** 16Cs, 77, 71 rings a bell. So tiny amounts of program space. We're, we're trying to do everything within a couple of K of program space.

**Dave Jones:** 5, 5, 5, 12, one, one K was a lot.

**Paul Thompson:** Yeah. So assembly language. And then we, we, we, we found C. So high tech C, some of the listeners might be.

**Dave Jones:** Oh yeah. That was good.

**Paul Thompson:** Yeah. So yeah. When he made his first C compiler, I was one of these beta testers. And.

**Dave Jones:** Oh, okay. There you go. And he eventually sold that. That's an Australian company for those who don't know. And he eventually sold it to microchip. They still sell it as the, as the high tech C compiler, I think.

**Paul Thompson:** Just phasing it out. They, they, they bought, they bought everything into their XC, their XC compilers now. So the XC was, was basically the, the last of the high tech. And believe it or not, I'm, I think now for a lot of their newer devices, they're using the, the GCU.

**Dave Jones:** Right.

**Paul Thompson:** Compiler. Yeah. Skinned underneath. They're MP Lab X. So we're still using microchip picks, but we're not only using microchip picks. We've, we're using some other controllers as well, but yeah, we're a pretty good customer of microchips.

**Dave Jones:** Got it. Because the market has moved towards, everyone wants a smart, you know, internet of things device these days. So I noticed your latest one has wifi and phone app and all that. Cause the farmers just want to see on their, get alerted on their phone. Right.

**Paul Thompson:** It's absolutely. Australian farmers are trying to do more with less resources. Whereas you used to have, you know, farm, a farmer, a farm manager, some farm hands. Right. Now there's typically one guy trying to do everything. And if he can get up in the morning and check his electric fences on his phone over breakfast, he can go and do something else for the day. That's, that's half an hour to an hour.

**Dave Jones:** That's super valuable to them. Yeah.

**Paul Thompson:** Yeah. That's time. So absolutely. So absolutely. We need that. So you'll, you'll be interested to find what, what wifi chip we're using in there. I'm sure you'll recognize it once you see it.

**Dave Jones:** Excellent. Sure. I will.

**Paul Thompson:** And at this stage it is a coprocessor. So we, we, that design still has a microchip pick as the, as the core, if you like the engine.

**Dave Jones:** Right.

**Paul Thompson:** But the, the wifi is another module with its own program on it. And then, yeah, we've got, we've got our cloud server. We've got two of them. In fact, we've got one for the agricultural version of the app and we've got another for the security version. So we've got a paid subscription service that people can use for their, for their security electric fences. And for that matter, lots of other security devices can, can tie into that. But it was built around security electric fencing.

**Dave Jones:** That, that makes complete sense to separate your processes in something like this. You'll just want the controller that just does its job.

**Paul Thompson:** Yep.

**Dave Jones:** Nothing else. And as you say, it's not susceptible, you know, it's more rugged and robust, not susceptible to resets and, you know, due to arc overs and things like that. And then you've got your fancy pantsy whiz bang wifi. And even if that goes down, the control is still going to work.

**Paul Thompson:** Sure. And you'll even find that there's a third microprocessor on that circuit board.

**Dave Jones:** Oh. What does that do? Is that a monitor?

**Paul Thompson:** It's a watchdog. Yep. So it's an intelligent watchdog. Oh, it's a watchdog. Intelligent watchdog.

**Dave Jones:** Right.

**Paul Thompson:** So the, are you familiar with class C code or self-checking code?

**Dave Jones:** No, not really. That's not my forte.

**Paul Thompson:** Okay. So any, any electrical appliance where the safety of the appliance is determined or dependent on the safety of the software, you've got to write the software in a, in a very precise manner, it has to be self-checking. You know, one, one bit error in, in that code will be detected and it'll shut the thing down.

**Dave Jones:** Oh, okay. Got it.

**Paul Thompson:** So, yeah.

**Dave Jones:** And, and you do that. That's the, that software. Where it's not a special, obviously just using a regular pick. It's not like it's a, you know, it's a CRC check-in micro or something like that.

**Paul Thompson:** Yep. Yep. So we're using, we're using a, we off-boarded that to another little pick. And so it does the job. It does the job of sanity checking the other device and making sure that it's not going to do anything stupid. Like, like pulse at five times a second, which could be dangerous.

**Dave Jones:** Right. Is that, so is that part of the regulation and standards and stuff?

**Paul Thompson:** It's, it's a, it's a method that we employed to meet the, the, the clauses of the safety standard. Other people have done it in different ways.

**Dave Jones:** Got it. So it's not strictly required.

**Paul Thompson:** No.

**Dave Jones:** I, I'm curious, do you guys have to meet like FCC requirements and, and other like, you know, EMC requirements, even for something that generates these massive, like older thought, wow, you know, like you might be exempt because it's generating like basically on an antenna is generating these massive pulses.

**Paul Thompson:** Well, of course it's our, it's our electric fence energizer that is, that is tested. And, and yes, they, they, there are some specific clauses and specific tests that they use for the output pulse. But because the output pulse is so short and most EMC testing is done over an average over a timeframe. Um, it's, it's, it's, it's obviously because we do pass, it's not impossible to pass even with something that's generating such a hideously noisy output pulse. But, um, problems start when, when people, uh, then apply it to an electric fence. And if, um, the aforementioned electric fence has those, uh, knotted, uh, wires on it in the live wire and has little arcs on it. And you've got, you've got all frequency transmitters, haven't you?

**Dave Jones:** Of course. Of course. Little, little spark gap transmitters all the way along. Yeah.

**Paul Thompson:** Yeah.

**Dave Jones:** With a giant antenna on it. I mean, that's just, yeah.

**Paul Thompson:** Oh yeah.

**Dave Jones:** That's insane.

**Paul Thompson:** It is. And problems can occur.

**Dave Jones:** But I guess you're out in the middle of a farm and it doesn't, you know, it's not going to interfere with anyone really. Maybe, maybe your neighbor's AM radio is going to pick it up, you know.

**Paul Thompson:** Well, it used to be a big problem with telephones in rural areas before, uh, they went away from copper lines, it, picking on, ticking on rural, uh, telephone lines was, it was a very common problem. And of course that, that got, that started to be a real issue when they started to put things like, uh, fax machines and then modems for, for internet on those lines. And they, they were just dropping out every second.

**Dave Jones:** Right. Yeah, of course. Ah, got it.

**Paul Thompson:** But, you know, the, the telcos fixed that by putting in, in coax and in fiber. And then of course now everything's, uh, on three or four G. So that's a problem of the past, thankfully, but the more later problems have been with digital television. Uh, so occasionally we get somebody ringing up saying, Oh, I've, I've got to do something because my electric fence is resetting my, uh, neighbor's digital television picture. Exactly.

**Dave Jones:** Because you'll see that during a storm, like your, your TV will just glitch and it'll freeze frame because it has to re-error correct because it's just been swamped by the magnetic field of the, yeah.

**Paul Thompson:** Lost a few packets.

**Dave Jones:** The lightning strike. Wow. Yeah. Oh, terrific. Well, thank you very much, Paul. This has been absolutely fascinating. Look at a, a niche market. Most people wouldn't have thought about and, and, and you're one of the leading players in it. It's fantastic. And it's all done here in Australia, which is, well, mostly.

**Paul Thompson:** Yeah.

**Dave Jones:** Which is absolutely fantastic.

**Paul Thompson:** Our engineering group and most of the manufacturing is here.

**Dave Jones:** Fantastic. So where can people check you out? Are you, are you on social media? Can they follow you? Do you tweet? Maybe not.

**Paul Thompson:** Personally, I don't. Um, the company, um, our brand, if you like, so Pacton's the OEM manufacturer and designer, the brand that most people see, uh, our, our own products under is a brand called JVA, uh, short for Jules Volts and Amps.

**Dave Jones:** Nice. Okay. Yeah. I'll take my hat off to that.

**Paul Thompson:** There's, there's Facebook and other social media. Uh, you can tell I'm not a huge user of social media cause I can't even name all of them off the top of my head.

**Dave Jones:** Right. Not a problem. Oh, what I'll find what you do have and I'll link them in down below so that people can check them out. And, uh, hopefully I'll get a tear down of this, uh, new unit as well in due course.

**Paul Thompson:** Have fun with that.

**Dave Jones:** So yeah. Excellent. Will do. Thank you very, and this one works. Whereas the old one I found in the dumpster didn't work, unfortunately. So, you know, yeah. So I'll be able to generate some spark gaps and stuff like that. Do that. Have some fun. Yep.

**Paul Thompson:** Have some fun with creating some.

**Dave Jones:** Even though it scares the crap out of me. Cause anything over two, I always say anything over 12 volts DC scares the crap out of me. I just don't want to.

**Paul Thompson:** Oh, that's, that's called a healthy respect.

**Speaker ?:** Yeah.

**Dave Jones:** It is. All right. Well, thank you very much, Paul.

**Paul Thompson:** You're welcome. It's been good.

**Dave Jones:** All right. Catch you next time. Bye.

**Dave Jones:** Bye. Bye.

**Speaker ?:** Outro Music
