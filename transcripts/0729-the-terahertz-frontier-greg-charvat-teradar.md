---
episode: 729
title: The Terahertz Frontier with Greg Charvat of Teradar
url: https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released July 22nd, 2026. Episode 729, sponsored by Siemens Xpedition. The Terahertz Frontier with Greg Charvat of Teradar. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Greg Charvat:** And I'm Greg Charvat from Teradar. And Chris just pulled me out of the probe room during this interview.

**Chris Gammell:** That's right. I got a very brief tour of the probe room.

**Greg Charvat:** Weird stuff happens there, Chris. Weird things happen. Stuff happens in the probe room, Greg. Yeah, it does.

**Chris Gammell:** We should say, this is Greg's fifth time on the Amp Hour. So he's joined the Five Timers Club.

**Greg Charvat:** Does that mean, do I get like a participation trophy for that?

**Chris Gammell:** I mean, there's like a Five Timers Club on SNL. So I think that's the same. It's not quite the same level.

**Greg Charvat:** I feel like it is. It's the same. Except unlike SNL, our drug is coffee.

**Chris Gammell:** Our drug is coffee. And our other drug is dopamine from hearing about nerdy stuff, which we will be hearing about from Greg here today. And right up top, we should say, Greg is interested in telling all of you fine folks about the opportunities that await at Teradar. But first, we need to find out what Greg's been up to, what the heck Teradar is, and how terahertz radio works. Because we're starting to get in. I mean, like, at terahertz, isn't that starting to push into the light realm?

**Greg Charvat:** Yes, it is. Okay. It is. It's below visible light, but it's extremely short wavelengths. The wavelengths are in the hundreds of microns. So you're definitely beyond millimeter wave, but you're definitely not visible light either. You're straight in between millimeter wave and visible light. And if you look at the past, they would have called this far infrared, so far IR, like a long wave IR.

**Chris Gammell:** Well, maybe we should remind people what you had been on in the past, and then I think that'll help inform how we got to where we are now. So Greg has been on the show four times previously talking about your work at MIT and Lincoln Lab, your short, or sorry, your book about small radar systems, I believe.

**Greg Charvat:** Yeah, small and short range radar systems. Yeah, yeah.

**Chris Gammell:** And then back in 2018, his obsession with boat anchor radios and fixing them, that's, you know, Greg and I went to Hamvention back in the day.

**Greg Charvat:** We did. Our backs were stronger back then.

**Chris Gammell:** That's right, yes.

**Greg Charvat:** Remember how far we had to drag that stuff back to the car? I do, yes. Yeah.

**Chris Gammell:** That's why my back hurts now. Not because of being out of shape. And then back in 2018, you had three companies that you were working with. And so what were those three companies? And then kind of how did that morph into where we are now?

**Greg Charvat:** Well, I've been through three. I only work on one at a time. And because focus is key with these things. And so I, let's see, I went from Lincoln Laboratory to join Butterfly Network, where we built the first ultrasound system on a single chip, which included the transducers and all the electronics and all that stuff. So that was my first company. The second one was called Hyperfine Research, where we built a bedside MRI machine. So an MRI machine that plugs into the normal 120 wall outlet, and it can be in hospital rooms, wherever. You can check your phone right next to it. You can have car keys in your pocket. It doesn't matter.

**Chris Gammell:** Yeah, exactly. It doesn't suck all the magnetic.

**Greg Charvat:** No, no, no. And you could have, but more importantly, you can have like the tubes and things hooked to the patient so they can be in there and be monitored with it, all kinds of stuff. So that was good stuff. And then after that, I did Humatics, which is an indoor high-precision GPS. We call it microlocation. So it's good to, basically it's indoor GPS, good to 100 micron, 4 Sigma. And that company is still going. And with some of my friends from Humatics and some of the folks that I'd worked with in previous companies, we all kind of banded together and got Teradar going.

**Chris Gammell:** I mean, and so just the thematic things through these are taking your radar knowledge, you know, finding novel ways to put it onto silicon, making it smaller, more efficient, more cost efficient, making novel applications by the way of shrinking it down and making it more accessible. Is that a good assumption?

**Greg Charvat:** No. Well, how I got there was through the school of hard knocks in some sense. So I- Bruises. Bruises. Bruises. Bruises. So I- My PhD was at Michigan State University and at the time there was no like, we weren't doing radar or like hardware systems of any kind. They're doing that stuff today, but they were not in 2000, in the 2000s, right? So I had to teach myself radar imaging and microwave engineering and stuff like that. And my advisors were awesome. They're like, this is great. So let's couple it with EMAG theory, which is what we did. And it was a wonderful experience. But I kind of started there and I felt like I was really hot, hot stuff coming out of Michigan State. And I joined Lincoln Laboratory where I did some cool stuff like the coffee can radar course where you build a radar system out of coffee cans and wood as a project-based electromagnetic, SIGPROG, EM. That class is still going, by the way. They're still running it to this day. Is the kids still for sale?

**Chris Gammell:** I was looking at the notes and there was like, those kids were for sale at one point.

**Greg Charvat:** They were, but just build it yourself. It's faster to do it that way. And so it's on OpenCourseWare, MIT OpenCourseWare. I built this through all imaging radar system, actually brought in from grad school and souped it up at Lincoln Labs. We won some awards for it and got surprised. So I was doing some cool stuff there and kind of like showing my capabilities. And I thought I was hot stuff coming out of Lincoln. Then I went to a startup and I was like, whoa, you need to go even faster at a startup and be more flexible and really, really leave your ego at the door. Okay, so that was the point at which I learned to just drop the ego. It's not worth carrying it forward anymore. And at Butterfly, we started as a tomography company, which is what they're doing with Mid Journey right now, which you've seen the press for lately. They're back to tomography, which is cool. That was what we were going to do originally, except that we were going to do it with like PZT transducers and all this stuff. And it just like didn't scale with that kind of equipment. So the company pivoted toward ultrasound on a chip, which was a hard pivot because none of us were chip designers or MEMS designers or any of that stuff. So that was a shocker, but we kind of like figured out stuff and pushed it ahead. My role was to make the first MEMS CMUTS and get those working and stuff, which I did. And I think that I learned something through the school of hard knocks there, which was a sensor as a chip is a very powerful product for many reasons. Number one, it's inexpensive. Okay. It will be cheap. You turn the crank.

**Chris Gammell:** Relative. Relative. But yeah. Yeah. Relatively cheap. Like mass throughput, that sort of thing. Like you're benefiting from the process automation of a silicon fab.

**Greg Charvat:** Yes. I'm not saying fabs are cheap, but when you, you know, when you're making them at scale, they are very inexpensive. You dice them up. So that is interesting. So that's a way of democratizing a sensor. Number two, you can sense things you can't normally sense because you can do it at such a small pitch. So you can sense fine, things that require extremely fine geometries that there's no way you can machine it with your Bridgeport mill. You could do it with chips, right? And the third thing is there's, there's a big moat of defense around your products. So as a startup and everyone listening needs to consider this unasked for advice. As a startup, what will happen if, if you're successful, if you have a successful product, the calculus will go through all of the competitors and bigger companies than you. And they're going to figure out, do we want to buy this company or copy them? Yeah. Right. And so sure you have patents, but that's a piece of paper, man.

**Chris Gammell:** That's right. Not with much without a team of lawyers. Yeah.

**Greg Charvat:** Are you going to prosecute that thing for the big bucks? It takes, let's say, I don't know. Pick your giant tech company chooses to copy it. Are you going to be able to prosecute that patent against them? Right. I don't know. Maybe, maybe not. Probably not. So patents are a piece of the defense, but that's not the strongest point of defense for a startup. The strongest point of defense is really how hard is it? How long does it take? What I want to say is how long would it take to copy? And when you have a chip as a sensor, and it took you five years to figure that, do we get to swear on this? Do we get to swear?

**Chris Gammell:** Sure. I'll mark it.

**Greg Charvat:** When it takes you five years to figure that shit out. Perfect it. That means they're in a big company. They're going to take more than five years because they weren't hauling ass working, you know, 12 hour, 14 hour days to get there. Right. Yeah. They're making salary. They don't have shares or, or their shares aren't as valuable as, as much of an upsized year. So that is the reality of it. And, and so you want to be heavily on the buy. So what happens is if it, if it takes them, if it's going to take them some amount of time, whether it's four years or five years or 10 years, or who the heck knows how much time to copy your sensor as a chip, then guess what? They don't want to be the last person to market in a competitive market. They want to be first or close to, or not far behind first. And so the calculus favors heavily towards buy. And that's where the sensor is a chip. What I learned at butterfly is key to, to these tough tech companies. If you're doing electronics, I'm not talking about IOT. IOT chips are just grabbing IP cores and stitching them together. Anyone can copy that. Right. That's, that's not the moat I'm talking about. We're talking about like unique stuff,

**Chris Gammell:** three hard science embodied in Silicon and other.

**Greg Charvat:** In Silicon that are on mass production processes. And so that's, that's in my opinion, at least that's key to all this stuff. It buys you time to, to, to develop, to take on hard problems, to square away hard stuff to think. That's the other nice thing about it. So you don't have to hustle like a, like a, like a AI company. You know why those guys have, you know why AI companies have bunk beds in their office? Because their only competition, if you're wrapping a, if you're doing an AI wrapper around Claude, your only competition is hustle. Right. Cause everyone else is just as smart as you. It's hustle, hustle, hustle. Cause they're all using the same thing. Right. Yeah. I think, well, that's kind of interesting.

**Chris Gammell:** You don't want to be competing like that. You, you actually are competing. Like you're not owning the Silicon manufacturing though either. So like in a certain way you do have shared infrastructure, but the novelty has to be the, the geography, the geometry, rather the lower level knowledge, the, you know, the patents, like you said in the mix as well, but, and then just kind of locking them down. It's possible to decap chips, but it's maybe not, it's not super convenient.

**Greg Charvat:** Yeah. Well, you, you'd have to go through all the full 3d EM simulations and all the other stuff and understand it. And if, yeah, that's, that's, that's a, that's a lift, right? I'm not saying anything, things aren't possible. They're not, but yeah. Yeah. Yeah. It's not, it's not the same as copying like, um, a bunch of arrays of gates and things like that. That's pretty easy to copy if you want to copy it. Right. Relatives. I mean, it's not hard. It's not easy, but it's a lot easier than a sensor.

**Chris Gammell:** Graspable. Yeah, totally. And well, so then on that, on that note of the Silicon as well. So are you, you said high, high production, high volume. Is it just, is it just Silicon or is it Silicon Germanium? Is it like, in so much as you're allowed to talk about this sort of thing, like the, the novelty is one, the target area. So like ultrasound for the, um, butterfly, but like, where, where there also special processing requirements that were still high enough volume.

**Greg Charvat:** I would say I can't get into too much detail on either company's technical approach, but in both cases, you know, whether it's butterfly or terror or humatics or whatever, these are all, you know, we're using, uh, processes that, that are volume processes that have volume customers. That's what I was getting at. Yeah. I'm thinking like,

**Chris Gammell:** is it TSMC or not? I'm sure you're not allowed to answer that, but that's what, that's what I'm really asking in my head.

**Greg Charvat:** There's a bunch of fabs. TSMC isn't the only one, but of course that's one of, one of the big ones, but there's a bunch of fabs. They make things cheap and they're running all the time. And, you know, depending on like, um, your, your geometry, you might pay a lot for tooling, but it'll be cheap in the long run and all that stuff. So we, we, in all cases, we always, we, you want to go to a, of, you want to constrain your design as your sensor, chip to something that is volume production. You get into dangerous waters. If you're, if you require some, some process development, that, that gets tough. Now you not say you can't do it, but it's, it's, you have to be pragmatic about it. And, uh, the other part where you're in dangerous waters, when you start to do a lot of three, five semiconductor, the more advanced processes that are kind of new in front, you got to be careful with that. Right. And you put bounds around it.

**Chris Gammell:** Can you explain the three, five real quick for people? Three,

**Greg Charvat:** five is, uh, in the periodic table, columns three and five. So that's where you see the, um, the GAN, the GAN, um, if I can, GAN, gallium nitride, you see the gallium arsenide, the gas, you see the, um, indium phosphide and a bunch of interesting semiconductors whose properties are like, they're like, well, GAN is high volume now because of all the LEDs, right? Yeah. Yeah. Thanks. Thanks. Thanks.

**Chris Gammell:** Thanks. Well, thanks. Now we'll speed. Thanks.

**Greg Charvat:** American government investment into GAN to make cheap lighting, right? Like low power lighting. And that's kind of where it came from. And,

**Chris Gammell:** and I think, um, actually NC, NC state, NC state down here. So that's right. That was hell. Yeah. That's where, that's where, uh, Cree now will speed. Now who knows what the hell they're doing there. They are. I think they got over their skis a little bit.

**Greg Charvat:** It's such a great process, but, but GAN was one of those weird processes and they did it. They, it was pulled. They, they got it to cheap high volume. Right. But it's, it's a, it's a lift. I'm sure you should interview someone who worked on that. I mean, that had, that's gotta be a wild story.

**Chris Gammell:** Yeah. Yeah. We had a John, one of the, the CTO of Cree came on a long time ago.

**Greg Charvat:** That must've been. So I tried to get,

**Chris Gammell:** yeah, I knew one of my old bosses at Samsung ended up being the, one of the process leads at the Wolf speed. And then he retired and he's like, I'm, I'm done talking about tech. I'm like, come on. Yeah.

**Greg Charvat:** Cause you burned them out, buddy. Yeah, exactly. Yeah.

**Chris Gammell:** I think it's a tough life. Yeah.

**Greg Charvat:** That's tough life. You're taking a three, five from like a university lab almost or government lab and commercializing it. That's a heavy lift, right? You don't want to be doing that as a startup if that's not your main shtick. So if, if we're, if, you know, if we were a three, five, seven, we're trying to be a three, five, seven, like a doctor company, that's different. That would be our focus. Right.

**Chris Gammell:** That's a pretty deep boat.

**Greg Charvat:** I have to say definitely deep. I, that's, that's an awesome boat. If you can get it, no doubt about it.

**Chris Gammell:** But then the scaling is the hard part in that case. I feel like. So,

**Greg Charvat:** yeah. And I think the upfront cost before you get a ROI is tremendous. That's what's so hard about fabs. That's why there was the chips act because, because that, you know, the ROI is actually.

**Chris Gammell:** So Intel gets lots and lots and lots of money. I think that's really what the chips act was about.

**Greg Charvat:** Yes. And that's it. It's not free.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Greg Charvat:** But those things are expensive. Those are fabs are expensive. You've, you've worked in fabs. I've, I've used fabs, but you've been in the thick.

**Chris Gammell:** It's been a long, long time. Yeah.

**Greg Charvat:** So, Hey, wait, wait, wait, I got a question for you. Where's the, when are we getting the chip printer, man? I've got all these chip printers still on the chip printer. You know, Greg, I was hoping you were going to tell me about that. We really could use one over here at Teradar, you know, we'll buy one if it comes up. You know, a nice $500 chip printer. We'd buy that.

**Chris Gammell:** Put it right on our card credit card. Do you read sci-fi at all? Like is Neil Stevenson diamond days?

**Greg Charvat:** I don't, I just, I only read nonfiction books about the history of technology. That's all. Okay. Well,

**Chris Gammell:** I actually, I love to decouple my brain and Stevenson is, you know, top author for me, but there's one called diamond age, which is weird, but there's basically it's like this molecular age where everything's built, you know, like layer by layer, Adam by Adam, whatever. And it's all about like the feeds. Like, so the, the most rich people are the ones who own the feeds. And basically though, like if you think, if you swap it from Adams to data, basically that's like the model providers in the AI age is like the feeds is basically the clankers that are giving us all the model production and, you know, data centers. So just made that little, you know, just a little,

**Greg Charvat:** but are they right? Do they give good answers? You know, it does the, does it fall apart half the time?

**Chris Gammell:** I'm just saying that that's where the money is. Like, like you said with Claude and like people that are laying on top of Claude, it's like, it's like, unless you own the feed, you're, you're not really making, you know, you're just getting little bits of money on top of the real money, but even, I don't know if they're making money. Let's get off AI. Let's get back to physical stuff. That's, that's way more interesting. There's no way I, AI didn't create any of the stuff I've done. That's good. That's good. Okay. So three, five. So, so what I'm hearing and you can confirm it tonight is, is that this is not bog standard, but like you are on relatively standard high volume processes. And that, that is, that is not part of your moat is, is the absolute custom process.

**Greg Charvat:** I think that I can't get into all the process stuff to 2D. I'm just talking to the highest level. I think, I think for a, for a sensor on chip company, what you want to do is, is you don't want to do some, some custom process stuff. I think you want to kind of avoid that or at least do it. I'm not saying not altogether, but I think you want to like minimize the extent to which you rely on that stuff for success. Because the, the hard part is once you do process development is that, um, it, it's, it takes, it does take time, right? It takes time. And because you've got to make different lots of, and I've been through this before. You have to make lots of, I mean, not lots, but numerously many, and they call it a lot, lots of, and then you, you process them wafer by wafer and the mistakes are, are distributed. You know, you're trying to figure out, is this just, you know, the, like, are we wrong about our design? How we expect that bond to establish itself? Or is this, or are the tools wrong and incorrect? And then you get the metrics on the tool, you know, it kind of goes on and on. It's a very long process because if you don't own the fab, you're dependent on them to fit you in, to do the thing. And these startups aren't buying fabs because they're expensive. They're not going to own fabs. Right. So it's, it's, it's a, it's, it's a tough thing. So I would say that when, you know, as doing, you know, a few sensor on a chip companies, I think the way to go is you want to use stuff, leverage things that other people are using as much as possible.

**Chris Gammell:** I think it's another interesting thing though. It's like, so then the competitive advantage, the things that, that all, all of these companies have in common is like, you're gathering up applications. You're gathering up lots of brain power. You're gathering up really good testing is design. Of course the designs in there and then the testing and the feedback cycle, right? This is encapsulating all electronics design in general, but like, but like, because the process is, is not necessarily the true novelty. There is really just capturing like IP in Silicon. That's, that's cool. I mean, that's great.

**Greg Charvat:** Well, yeah, you're creating IP and while you're creating, I don't really think about like that. I just think about like, what does it take to make it work? Right. Yeah. Right. But you're doing deep, deep EM theory and simulation and, and all of those old textbooks about fields and waves. We use those textbooks for everything we do. We actually have a library full of stuff like that. And similarly at the other companies we did too, because we were doing things from the fundamentals. And that's, that's, that's, that's always interesting. It's fun to do the applied science thing, which is what electrical engineering is. Yeah. Applied. Well,

**Chris Gammell:** and so now, so thinking about like, okay, so now someone listening is like, well, then how the heck do you make just Silicon do, you know, like people think about Silicon. They're like, okay, I can do a microcontroller. I can do a memory structure, whatever. But now you're making structures in Silicon that are doing a physical thing, right? They're emitting waves, capturing those waves back in. What does it take to like, and that's what you said, like going back to the, you know, the first principles as well. Are you just like drawing boxes on a page at that point? Like how does, how does that work?

**Greg Charvat:** Oh, well, it's, it's without getting into too much detail of the chip designs and stuff. I think we have, I would say these things start out as white drawings on the whiteboard. Really? Okay. Yeah. And, and we're doing things that aren't in the textbook. We use ideas from the textbook, good literature, but we go well beyond that. And we're, we're making a lot of things from first principles to do this. And that goes for all three of those companies where we were building sensors, a chip, right? These are, you know, when you're creating the sensor element, that's in Silicon, you're doing things from first principles. And it's, that is where it gets super, super interesting and extremely challenging as well as stressful and making it work. But yes, and as part of the, all that you, you do full, you know, you're doing full 3d e-mag extractions of the circuits, right? You're not, you're not just doing, and I see where you're going with the question. You're not just doing, like a digital SIM or, yeah,

**Chris Gammell:** you're not dropping in blocks. You have to make the blocks. You have to make the, to make everything. You're starting to, you're minecrafting the, the thing from the bottom up. Yeah, yeah, yeah, yeah, exactly. Yeah.

**Greg Charvat:** You're minecrafting with, with like a full e-mag simulation, like a Mo, like moment method FEM. Usually you'll do both actually. Yeah. And then you do, you like extract the geometry from the chip and you can actually like rotate around it in this, in the simulation software to see where the fields and currents are coming and all this stuff. It's really pretty deep stuff. Yeah. And, and, and, and fortunately these days the SIM software is, is quite good to be, yeah, it's, it's, you know, you gotta know, you gotta know you're not being fed crap back at you, but, you know, but it's, it's fun stuff.

**Chris Gammell:** Do you, do you follow Sam Aldeher on, on LinkedIn or anything like that? He does those like visualizations. He'll like have like RF and then like put a fake hand in it. It was like, he does blender. He just puts blender with, I just love that. Cause it's like making these like invisible ideas, like very, very like. That's. Capturable.

**Greg Charvat:** Yeah. I've seen some of those. I don't know if they're from him, but like, I think that's awesome to visualize what the fields are.

**Greg Charvat:** Yeah. Cause they, they, um, it's hard to really understand intuitively until you see it. Like where does the, where, where does the electromagnetic radiation come from? Well, it's the time varying currents on things. That is to say electrons bouncing back and forth. Well, when electrons bounce back and forth in time, they generate a complimentary magnetic field. And then when the magnetic field bounces back, it regenerates electric field. And that is the self generating electromagnetic field as it radiates outward. Uh, and physicists like to call those photons, by the way, just to add to the confusion.

**Chris Gammell:** Yeah. Yeah. Yeah. Well, and I think that's, I think this, okay. So I, I know that we're, we're really dancing on the edge of what we're allowed to talk about and stuff like that's fine. But like, yeah, when I think about like base blocks, like me 10 years ago, me, I'd be like, yeah, but what makes it go? And I think like the end of the day, it's like, you need transistors to make it go. Right. That's what Silicon's great at. You are doing RF simulation. I'm just saying this, you can correct or not correct. It's fine. But like you have structures that are novel applications of those transitions, but you're just like yanking on things and creating electron flow that then has magnetic flow, like you said. So like that is, and then, and then Maxwell takes over and you know, you figure out what to, what's, what's max up to, you know, like physics and quantum mechanics, right? Yeah. Yeah. Yeah.

**Greg Charvat:** Quantum mechanics and physics. That's it, man.

**Chris Gammell:** Wielding the power of the universe in a tiny, tiny Silicon thing.

**Greg Charvat:** As much of it as we understand, at least.

**Chris Gammell:** Yeah. Right.

**Greg Charvat:** On this planet.

**Chris Gammell:** Okay. So speaking of things, I don't understand how in the, I, I told Greg before the show, I'm going to be a terahertz denier. I don't believe the terahertz actually exist. Cause I, I mean like I have such a hard time with gigahertz. You know, and I'm just like, how the hell does that work? And then now you are another couple of decades up and, uh, why terahertz,

**Greg Charvat:** Greg? Well, the thing is, it's like, if you look at the, the sensors out there, you know, we have, um, our, our market is automotive sensing, long range automotive sensing, but that's, that's what we're, we're in. And so if you look at the sensors where, you know, there's a lidar and, and we have now imaging radar at 77 gigahertz. And so the terahertz right in between it's, it's a wavelength smack in between those. And it's interesting because it has the advantage of both. So it has, uh, the resolution comparable to lidar. And when you see the terahertz data, you'll be like, shit, that looks like, that looks like wider. Right. And so that's one of the fun parts about it. And then the second thing is it, it has the same or very similar electromagnetic properties to radar. So it, um, it goes through weather like the radar does. We see through pea soup fog, no problem. We see through pouring rain, no problem. Uh, we see through the bumper fascias on automobiles, no problem, stuff like that. Oh, really? Yes. The concepts, all the things that make radar really great. We have, except what's the bumper fascia.

**Chris Gammell:** That's like the plastic cover. So you were saying behind a bumper instead of like having it exposed. That's right.

**Greg Charvat:** That's right. Ah,

**Chris Gammell:** that's interesting.

**Greg Charvat:** Doesn't need to have its own, whatever, you know? So, you know, that's, um, it's, it's got the best of both worlds. And that, that's, that's why I think it's a compelling technology and why we have so much market pull.

**Chris Gammell:** Where does the 77 gigahertz come from in the, in the automotive 70, what was the 78 gigahertz? Like why is, why are there different frequency ranges? Cause we've had some people on the show. I mean, you talked about it in the past. I forget. Oh, I forget his name. Who was on the show talking about other automotive radar type things just for like, you know, there's like the, the kind of the rough ones that are like the low cost sensors, just like, Oh, there's someone behind me. There's a cut shopping cart, whatever. Yeah. Like why, how do they choose these, these, um, frequencies?

**Greg Charvat:** Well, they started at 24 gigahertz for the side object detection to tell you if there's someone, your blind spot. Um, then they moved up to 77 gigahertz to do, uh, automated cruise control. So your car's cruise control doesn't keep it going. It just, it tracks the velocity of the car in front of you. Um, that was done with, um, that was done like the late nineties, actually. Really?

**Chris Gammell:** Wow.

**Greg Charvat:** Yeah. Yeah. And then, uh, then what happened was they, they might then over time, this, the, the side object sections migrated up to 77 gigahertz because they had more bandwidth can get better resolution. Uh, and the beams could be tighter so that they're more confident where they're looking as opposed to larger blobs. So they went up in frequency to reduce the blobs and have finer control over what they're looking at.

**Chris Gammell:** And then they started maybe have like one, two, three, like in different angles, you kind of point them with like a narrower beam sort of thing.

**Greg Charvat:** Yeah. I mean, even the cruise control, automatic cruise control, the first one, I think it had like, um, if I recall, I think it had like three beams that went right down the middle.

**Chris Gammell:** Okay.

**Greg Charvat:** And so to ensure that you're not tracking the car in the other lane, you're just getting the one in front of you. And it looked, it used a dielectric lens. So if you see those old, I mean, now they're in junkyards, right. But if you pull an ACC off an old Mercedes AMG, well, you'll see, it looks like the hell 9,000 computer interface with the big, seriously, it's a big red sphere. And underneath that are the receive antenna, like three, I think it's like three or seven, it has one transmitter. So it's something like that linear FM radar. And so they, they actually had three beams to make sure they were tracking the thing in the middle. Yeah. It was really good stuff. Like no doubt about it. And then, so everyone kind of went up in frequency to get the finer beams and finer control. And now you're seeing the MIMO stuff is starting to come out. So, um, we've seen the, the, the lower res MIMO has been out for a while, but we're starting to see the high res MIMO coming out. And, uh, that's just the march of, of progress, right? Everything, uh, in that world is at that frequency.

**Chris Gammell:** Got it. And, and they're not, they're not scanning. They're not rotating like on a LIDAR, like a LIDAR actually is a laser that rotates or a string of lasers that rotates. Yeah. Yeah.

**Greg Charvat:** The LIDAR either will either have like a, a spinning mirror powered by a hard drive motor or, um, or like a, like a MEMS mirror, like those MEMS projectors. So they have some mechanical interface because they have to use a high power laser to go up to two, 300 meters to hit that link budget. So, um, they, they, um, at least the automotive grade LIDARs do that. There's like the, the, the shorter range ones don't need those things, but, um, the automotive ones need to go far, right? They need to hit the distance. Uh, yeah, yeah. Yeah. The, the, the, the 77 gigahertz stuff is monolithic. There's no moving parts. Uh, it's extremely reliable. There's, you know, you're, you're, you're those, those systems, um, you know, they're, they're very robust because of that. The, the, the lack of moving parts allows them to last an enormous amount of time. You have less quality issues. You're not pulling, you're not doing like a quality, you know, you're not bringing your car into the dealership because the, the 77 gig radar died. Right. Okay. Right. Right.

**Chris Gammell:** You can't be doing that. You're probably, you're probably coming to the dealership because you, you didn't know someone was in, you got used to the, the light turning on. And when you were about to change lanes and then you don't have the light and then you crunch into someone as you change lanes.

**Greg Charvat:** Yes. Then the radar got destroyed or something. That's why that's the only time they'll replace it. They just don't know. Yeah, exactly. They just don't know. Yeah.

**Chris Gammell (sponsored segment):** We know the feeling you spent years mastering your current CAD tool. You know, every quirk work around and menu. Switching feels like changing a religion, but what if the friction you're used to isn't required? We talked to past guests of the show, Shruk Al-Attar from episode 549 about her experience, trying out the tooling from today's sponsor, Siemens. You might know their tool Xpedition from their days before the acquisition of mentor graphics.

**Shrouk El Attar (sponsored segment):** I had, I had some issues with my previous tool, to be honest, it was more friction. And I started looking around and I realized that there are other tools that do a lot more. It turns out that an Xpedition standard license was actually cheaper than what I was paying for my previous tool.

**Chris Gammell (sponsored segment):** The biggest hurdle is usually the UI. Where are the buttons? How do I even start a route? With Siemens Xpedition, you don't have to relearn the wheel.

**Shrouk El Attar (sponsored segment):** There is a tool called global search tool. So I don't actually need to know where anything is. I literally just look up import Gerber and then I can import it, export Gerber and I can import, export it. So that's something that's made that convergence. So, so much easier. It's something that I don't really understand why it doesn't exist in other tools.

**Chris Gammell (sponsored segment):** And once you're in the tool works for you, not against you. Instead of dumping a thousand puzzle pieces on the screen, Xpedition uses planning groups.

**Shrouk El Attar (sponsored segment):** I can just import that group at a time. So just import one group at a time. And otherwise it's just so overwhelming having all of these components.

**Chris Gammell (sponsored segment):** As someone not doing layout full time, I was curious to learn about the deep complexity of Xpedition. Higher end tools often are complex because there's so much they can do, but Xpedition is constraint driven as Shouk explains.

**Shrouk El Attar (sponsored segment):** In Xpedition, I define my rules and then when I'm actually designing, it would never allow me to say, put down, you know, a via with an annular ring of size X in a space where that's not allowed. And it does that so beautifully and live and in a way that's so responsive. And it means that at the end, when I'm actually doing my actual DLC checks, the things I'm sorting through are very minimalist things. Like, you know, this, this component is not on the grid or something like that. So it saves a ton of time. And I didn't realize how much time that, um, that took really from, from us. And I didn't realize that we didn't have to spend that time.

**Chris Gammell (sponsored segment):** I also asked about working with a mechanical team. If they're using Siemens NX, you're finally speaking the same language.

**Shrouk El Attar (sponsored segment):** There's no third translation layer. It doesn't go through a third party software. We're using the same digital data and it makes, oh God, like a world of difference. But I would choose a tool that, you know, the biggest companies are using the enterprise version of. And that's a tool that I would know I'd have confidence in and can scale with me. Knowing that I'd be using a tool that scales up to exactly that without having, you know, to change, uh, UIs, learning where the buttons are, just scaling with the tool. That's definitely the tool I would choose.

**Chris Gammell (sponsored segment):** Whether you're a consultant or part of a global enterprise, Xpedition is designed to scale with your career. Listeners of the Amp Hour can try out Xpedition for a free 30-day trial and see the power of CAD tools that power some of the largest electronics companies in the world. To learn more, check out the show notes or go to theamphour.com slash Xpedition. Xpedition. That's X-P-E-D-I-T-I-O-N. And now back to the show.

**Greg Charvat:** you know, you're, it's an evolutionary process. So I, I do like to point to the history of radar world war two, having been a big fan of it, studying it, and also owning two sets of MIT rad lab books, the 28 volume set on, Oh, all the radar they developed. It's, it's,

**Speaker ?:** it's,

**Greg Charvat:** it's, it's interesting. So they started in world war two. I think a great example is the, the Japanese attack on Pearl Harbor. There was a radar station that had, I think it was an SCR two, two 84, which was a UHF radar. And it had, it had what looked like a gigantic bed spring with little dipoles on it. And it was, it could, it would give you, it would project a beam out to, I don't know. I would, I think probably a couple hundred kilometers or so. And it just gave you range. So there's a sil scope screen that you'd look at and it would have range and amplitude, nothing else. Okay.

**Chris Gammell:** And then there's the skill of the operator then. Yeah.

**Greg Charvat:** Skill of the operator. It was the end though. So the, the antenna was on a servo. So the operator underneath that screen, there was a big steering wheel that would tell you angle of the antenna. You turn it and it would automatically go to that angle.

**Chris Gammell:** That's the scan, huh? That's the scans.

**Greg Charvat:** And so what they would do is they would write on paper, plot, start plotting it on paper where stuff was, because you would manually scan it around and look for stuff and plot it on a piece of paper. And so the attack, what happened was, and everyone can go ahead and read the history books, the radar operators picked up the Japanese coming in with all of their airplanes at a very long distance, easily picked them up. And they phoned it in and said, Hey man, there's a big flight of planes coming in. It's, and the guy there and said something like, well, there's a couple of flight of B-17s coming from California. They're like, this isn't in that direction. Yeah. Yeah. Like, yeah, whatever you guys know what you're doing. Click, you know, something like that. So those operators in an effort to cover their ass, took a picture of it, a scope picture. And you can see the scope picture on there. And they annotated like, this is the planes. Right. Right.

**Chris Gammell:** This is the ultimate told you, told you so. Told you so. Yeah. And,

**Greg Charvat:** and then there's a piece of paper, which has their paper track where they drew the track. Right. Yeah. As they came in for the attack. And so that system was at 200 megahertz or so UHF system. So that's, that's, that's earlier in the war.

**Chris Gammell:** You said, you said hundreds of kilometers. Is it doing like, like ionospheric bounce? No, no,

**Greg Charvat:** no. It was line of sight. They're up on a mountain and those things could go pretty far. Those World War II radars weren't shabby.

**Chris Gammell:** I was just thinking horizon. Like how do you get horizon?

**Greg Charvat:** I think it was a couple of, maybe it's 150, something like that. It was pretty, it was far enough. Yeah. Pretty good coverage.

**Chris Gammell:** I guess if you're in Hawaii too, you have, you have mountains at your disposal.

**Greg Charvat:** That's right.

**Chris Gammell:** Yeah.

**Greg Charvat:** That's right. So it was, it was, those systems were pretty good. And now, now backing up even before that, the battle of Britain was the chain home radar system, which was at 26 megahertz. Okay. 26. So that system didn't even have the range. Uh, PPI scope or the servo motor to antenna. What happened with that system was they had transmitters blasting beam, just filling. Everything with a pulse. And then they had received towers that would give you angle of arrival. Oh my gosh. From the pulse. And that's how they did it. So it was even more primitive. So it was chain home.

**Chris Gammell:** Why do I feel funny about every 10 seconds? Yeah.

**Greg Charvat:** Oh yeah. You're getting blasted with a pulse. Yeah. I didn't know. Yeah. Oh, you wouldn't feel it. It's one over R squared and all that. So like they're blasting, you know, these policies, very primitive radar chain on which, which was key to winning the battle of Britain, as we all know, right. The thing of legend. And so then we have the radar SCR, uh, two E four or something like, I forget the part number exactly. UHF radar Pearl Harbor. So that's 10 times higher frequency. You go from 26 to 200 something. Right now, um, fast forward. Um, there's this huge problem that they had, uh, during the bombing campaign and world war two, how do you find cities in Europe when all the lights are off? Okay. And so how do you navigate a plane at night? The British RAF were their special. They, they focused on bombing at night. Okay. Now we can, I don't want to get into the morality of that bombing campaign. That's a very complicated story, but their objective was to, uh, bomb at night because they believe that they had better, uh, cover because the fighters couldn't see him at night. And so, which is true. You couldn't feel as many fighters. You had to use special radar equipped night fighters, intercept the night bombers. So, so they gave them a protection, but the trouble was finding those cities. So the British developed this thing called H two S, which is stands for home suite, home S band, which is three gigahertz. Now another 10 times higher in frequency than the SCR two 84, whatever the heck was. So, and that system was a airborne ground imaging radar with a huge spinning dish. So the dish was on a servo, but it was spinning and it would give you a, uh, map on a, a silscope screen, uh, angle range and magnitude of what's below and around the plane on the crown. So you could actually see the difference between forests, farms, and cities. And so they would navigate from city to city. And what does city look like? It looked like a huge blob. That was really bright. That's it. That's all they saw. Sometimes they would see a river because the river would scatter away and you'd see a dark line where there's no energy, but usually it was just a giant blob in the middle of a bunch of smaller blobs. And that's how they would navigate from city to city to city.

**Chris Gammell:** If you think about this in the forties though, that must've seemed like fricking magic, right? I mean, like, I mean,

**Greg Charvat:** it's early for like 1941, super early. Right. And so tubes and of course, what's wrong with two. You have a problem with two. Nothing wrong with tubes. You can do anything with tubes.

**Chris Gammell:** Come on.

**Greg Charvat:** Tubes in the office at Teradar. Yes. We have lots of tubes in this office. So there's a, um, by the end of the war, they went up again to 12 gigahertz, 10, 12 gigahertz, something like that. I think maybe it's 9.3 is XP is around 10 gigahertz. And so their last version is H2X X band. And that could image the ground so precisely. And you can look at images of H2X, uh, radar, uh, maps and things. You can see it for yourself. You can map perfectly map the contours of the harbor account, the ships in the harbor. You can see if you're over a city, you can count the streets and you can see where the bigger buildings, smaller buildings are and get shapes even of large buildings with this thing. So as you go up in frequency, as the wavelength shrinks, the imagery gets richer, higher resolution.

**Chris Gammell:** There we go. And we we've seen this literally connected the dots and we will connect more dots shortly.

**Greg Charvat:** That's it, baby. That's, that's, and that's all we're doing. Teradar is we're, we're following the same path for automotive. They went from 24 to 77 and we're going up to hundreds of gigahertz. So we are just making the resolution finer and finer on a logical progression technology. Yeah.

**Chris Gammell:** Right. And, and eventually you would get to visible light, which is about, like you said, you, you said visible lights up the terahertz range, but you're basically sub infrared, right? Like that's, but you're, you're working your way up there, right? I mean, like without actually generating photons, right?

**Greg Charvat:** Well, at this point, I would say, I would say that, um, I think, I think that this is the last frontier in, in the electromagnetic spectrum, at least below visible light, right? Like, you know, I think this is the last one where, because you want to be able to, another thing, another aspect of like modern sensing technology and stuff like coming from my, my experience at Lincoln laboratory, we could pick almost any wavelength we wanted to operate at. Right. And we would then, because, because microwaves were mature, we could pick anything in the microwave to radio spectrum to sense, whatever problem we're trying to solve. And so, so we are closing the final frontier in terms of auto sensing at least. And that I would, I can't imagine choosing any other wavelength in my opinion, because it does have the best of both worlds of going through weather as well as LIDAR, um, image quality, right? Yeah. So that's, that's the sweet spot.

**Chris Gammell:** Let's, let's talk a little bit more about the problem space as well. So, so we talked a little bit about before the show, I mentioned how much I love Waymo, but what I said is I grew up in Buffalo. I used to live in Chicago. I used to live in Cleveland. I just literally cannot imagine Waymo as it is today, operating in Buffalo, New York in the winter. It would just be like, what, what are you even trying here? Uh, similarly with, so then that's the LIDAR side. Those are all scanning light fields, point clouds, whatever. Um, on the other side, you'd said radars, you'd already said blobs once as well. So like radar blobs is kind of the lower end. So like, can you kind of box in where, why Teradar is in the middle of those two with, with application shortcomings of the, of the, of those. Well, sure.

**Greg Charvat:** I mean, I think, you know, you've kind of nailed it as it's for, for a couple Waymo, which is an amazing service for those who've tried it. And, uh, it's amazing. It's so, it's like,

**Chris Gammell:** it is, it is the best, like low cost way to experience the future. Like it's wild. Yeah. It is so cool. So like people in China have, you know, there's also tons of self driving in China too, whatever. Yeah. So like, yeah. Yep.

**Greg Charvat:** And, and, um, I think, uh, but that there's struggles, right. You know, you, when, when the weather comes, things become a struggle because if you want extremely safe, self driving, like Waymo does, you need all of the sensors seeing stuff, right. Because you, you don't want fatalities. You don't want to injure anyone. You don't want, you don't want to get an accident. So you can't have your sensor all messed up because the weather. Right. And so that's, that's sort of the, the trouble with, with laser radars. It struggles once, once you get into the rain and the snow and the, the fog and any sort of adverse conditions, or even just dried like road crap on the lens, like you're in trouble. Right. And so, so, um, you know, our system, you know, and the, the downside of, of radar, even the newer MIMO large MIMO systems coming out is, is, is 77 gigahertz radar is, has a resolution problem. And so it's, it's, you know, you're interpreting blobology, right. Or, or you need things to move fast enough. You can resolve them. So, uh, our system sits in the middle because we, but let me go back. The strength of, of radar is that it can punch through the weather, right. It doesn't care if there's dirt or film on the, the, it goes through bumpers, you know,

**Chris Gammell:** you don't benefit from this on, uh, when we fly in airplanes and, you know, and other, of course we do, right.

**Greg Charvat:** They don't stop flying airplanes in the weather because you can see them. Right. Right. We can see them. And, uh, thanks to the radar.

**Chris Gammell:** Yeah. And how much, what is like autumn or sorry, um, like airplane radar they have on, on plane radar in addition to ground radar.

**Greg Charvat:** I, you know, this, and I defer to some of your listeners might know more than I do, but my understanding is if they do have radar on the plane, it's mostly for weather radar, but I don't, they, they rely on like ADSB to know where all the other planes are and, and, and also the air traffic controllers. So, um, you know, if, if you've ever flown right seat on a general aviation flight and someone who's instrument qualified, have you done that before?

**Chris Gammell:** Uh, no, I'm, I'm not going up. No, I'm not doing that.

**Greg Charvat:** It's fun, but maybe don't do it. If you have kids like you and I do, but, but if you,

**Chris Gammell:** yeah, no, no, no, no,

**Chris Gammell:** there are YouTube videos you can watch. I, I've listened to traffic and like, it is amazing. It's like, it's a lingo and yeah, it's so, so impressive.

**Greg Charvat:** Well, there you're listening to their traffic controller and they're keeping an eye on everything for you. Right. That's how that's pretty much how it works. Yeah. Um, yeah. And, and they rely on the radars, right? The ARS nines and stuff like that to do it as well as the ADSB system, the, between those two things, they have what they need to keep the skies really, really safe actually. Yeah.

**Chris Gammell:** Exactly.

**Greg Charvat:** And so they, and obviously they punch through all kinds of weather. It doesn't matter. Right. And so that's the strength. That's the superpower of radar, if you will, is it punches through the wet and is, is unperturbed by these things. And so the nice thing of the, the interesting thing about teradars, we have the lidar resolution, but we punch through the weather just like the radar does. And so it's a really strong position to be in terms of a sensor. And of course we don't have any moving parts, just like a radar. We're monolithic, you know, our stuff. I'll tell you what, the first robotics teams, 20 years from now, we're going to go to junkyards and pry teradars off the cars to stick on the robots. I like it. I like that.

**Chris Gammell:** I like that. Yeah. That's great.

**Greg Charvat:** Or actually you and me and the listeners here, we'll be pulling them off and putting them on. Exactly. Projects is what we're going to do.

**Chris Gammell:** Yeah. Be like, Hey Greg, this boat anchor, it's a, you know, it's a modern boat anchor that you built, you know, there's no tubes in it. Just so everyone knows.

**Greg Charvat:** We didn't put tubes in this. We, it was built with tube audio in the lab.

**Chris Gammell:** Well, there you go. It was built with the brains that they're powering the brains of us. IP. Yeah.

**Greg Charvat:** Yeah. But we didn't, we didn't, we didn't put any tubes in it or moving things.

**Chris Gammell:** Yeah. Makes sense. What about the, you know, we've talked a little bit about the fall off of, of signals and stuff like that. Like how does that work in the gigahertz range as well? Because just thinking about like, so I work in the very, very high frequency 2.4 gigahertz range for some of the little tiny IOT things that I do. And you know, there's water absorption in that, in that spectrum. And, but similarly, like at gigahertz up into terahertz, it doesn't just like immediate, how do you get any kind of like, like projection out into space without burning tons and tons and tons of power?

**Greg Charvat:** Yeah. That's, that's, that's interesting question. I would say we're not going, you know, you're, you're, you're, you're, we're going pretty far, but, but you know, we, we have a link budget that supports the atmospheric loss and we have a system architect to take care of it. And so I would say that, that, that is how we did it. You know, we're coming from a background of, you know, my background, I started my career imaging through concrete walls. Okay. And, where you lose 99.9% of the signal one way. And then it, then whatever scatters off, you lose the same amount going back. And so, and similarly with the ultrasound work and the work at Humatics, these were all really challenging link budgets, right? And so normally you think of link budgets in the clear and things are ideal and stuff. And for me personally, I'm, I like working with difficult link budgets and we did that and had to overcome some interesting things to pull off what we're doing. I'll just put it that way.

**Chris Gammell:** I'm sure there's a lot of heat sinking and, you know, you probably are dumping, you know, you're not necessarily battery powering this thing, you know, so running off a double A battery, anything like that. But like, still there's a lot of sensitivity you need in the receivers, I'm sure. And just the cranking, cranking some amount of power out. Yeah. Yeah. But it's,

**Greg Charvat:** it does the business as they say. It does the business.

**Chris Gammell:** When I think about LIDAR, I think about like a sweep of like a line of things and then you're shooting lasers out and you're getting little points back from the laser. And you had mentioned this is monolithic as well. So there's, there's no movement. There's no like motor that's cranking things around. How do you do that all at once? Right. Almost like the, almost like the same, you know, to go back to the Silicon side of things, thinking about like rastering with EUV versus like single shot, like through a mask, that sort of thing.

**Greg Charvat:** Well, I can't dive too deep into architecture, but I'll, I'll say this, you know, we're, we're imaging, we're imaging out to hundreds of meters at multiple hundreds of gigahertz. Okay. With a tear it's digital phased array. The whole thing, it sits in the palm of your hand.

**Chris Gammell:** Yeah.

**Greg Charvat:** And it's, and it's at automotive B sample for those who understand automotive stuff. So it's, it's, it's,

**Speaker ?:** it's,

**Greg Charvat:** um, I would say it was pretty tough to get it to the point of, of doing all that inside meeting size, weight, power, all of those things. But it, it's, it does, it does the business. I'll just put that. Well,

**Chris Gammell:** I think phased, phased array is the answer that I was like, just that's, that is the answer then. So that is how you scan things. So basically it is a scan, but it's done with interference and, uh, constructive, destructive interference. That same, same old song that lots of things use, but it's just so fast and far that you can do that.

**Greg Charvat:** Digital systems are powerful. And, and like the modern direction that all radar systems are going in is digital phased array. And, um, we just skipped right to it here. Yeah. That's what we did. Right.

**Chris Gammell:** I mean,

**Greg Charvat:** that's why I bother.

**Chris Gammell:** So if we've talked about it on the show for before, of course, like when Shari Arzani talked about, you know, he tore down like the Starlink and, you know, all the, exactly. That's a beautiful piece of kit. Oh my gosh. So gorgeous. It's a phased array as well. Yeah. Lots and lots of antennas, constructive, destructive interference, um, that sort of thing. Okay.

**Greg Charvat:** So you have to, everything is going phased array and, and, and not, we're not talking about like compromise sparse imaging arrays or any of that stuff, like proper lambda over two phased arrays. That's the direction of everything these days.

**Greg Charvat:** you know, chip scale. Just, yeah, you have a lot of channels. Yep. That's, that's the way it is. Figure out how to do thousands of channels. Yes. That's what you have to do to do what we're doing. And I'm sure Starlink is very similar to that. Like you need an uncompromising phased array to do stuff like this. This isn't like a computational, let the AI guess what the imaging looks like stuff. We're pulling signals out of the noise. How do you feel about AI?

**Chris Gammell:** How do you feel about AI?

**Greg Charvat:** AI didn't design anything that I've done.

**Chris Gammell:** Anything. That's right. Well, that's okay. So again, I can, I can piece it together in my mind, but what I'm going to say, knowing, the little that I know about phased array, how about this? I'll say this about the, the Starlink tear down the chariot. It's like lots and lots of antennas that are outputting at different time, times in slices and time. And that is what creates the, the interference constructive, destructive that makes it work. So.

**Greg Charvat:** Yeah.

**Greg Charvat:** Phased array, man. I mean, the books and the theory go back to the 1960s. And the first practical phased array radar ever made was the FPS 85 and Elgin Air Force Base. I believe it's still running. It's job is to scan space objects. It's at UHF. And, and I think that was more or less kind of like, I don't know how B-Muse relates to it, but I think it was, B-Muse seems to be a cousin, a second cousin to that at least, which is the phased array used to scan for Soviet missile attacks. It's a very important phased array. There's lots of them around the planet. And so these phased arrays, you know, they, they were born out of the necessity to see, to, to, to, to scan for things that are coming in fast. Phased arrays are, or a military necessity. So in World War II, we had, you know, propeller planes. Okay. Which drove the development of radar to begin with, because before then you just had people with binoculars and, and giant. That's right. Yeah. Enough time to be like, yes. And call it, dial the phone to whatever, and they could do something about it. But, but that, that those are planes that went 100 knots. Once they got up to 400 knots in World War II, they're too fast to do anything about it. So you needed speed of light, electromagnetic scanning to see them, but you were still using mechanical things that would take four or five seconds to make us a full sweep. Right. Yeah. But, you know, the phased arrays came about during the jet age, as they called it, right? The jet age, things went a lot faster. And so now you need something that can be computer controlled and scanned super fast. And that's kind of where the, the necessity of phased arrays came in. And so I think, you know, going forward, we're now with our advanced technology, we have, you know, we can have lots of data converters and, and Y data pipes, thanks to the very large scale integration, right? We're so-called the riding of Moore's law. Well, that's a very real thing. Right. And that's not just, I mean, Moore's law was created before there were tech bros. Okay. So it's legit. And, uh,

**Chris Gammell:** yeah, yeah. Gordon Moore was the original tech bro.

**Greg Charvat:** Well, yeah, I don't know. I don't think he spent four hours a day in the gym instead of, uh, working at the lab bench, but, uh, you don't know.

**Chris Gammell:** He was jacked, man. He was jacked.

**Greg Charvat:** He was jacked. Yeah. Yeah. Yeah. He was, he was, he was doing plastic surgery, uh, two. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Looks maxing back. Looks maxing.

**Greg Charvat:** He wore, he wore cologne, even though he was married. I wear cologne though.

**Chris Gammell:** I'm married. Hey, look, my wife likes that. I smell decent.

**Greg Charvat:** Okay. Well, you get a pass. Then you get one, one tech bro pass. Okay.

**Chris Gammell:** Everybody gets one.

**Greg Charvat:** Everyone gets one. Well, I'm wearing Hawaiian shirt today, but I don't think they wear. Yeah. The tech bros. I don't know. I hate, I cannot say. I don't know. I don't,

**Chris Gammell:** I actually don't know any tech bros. Um, rational, um, prejudice against them.

**Greg Charvat:** Yes, I do. I do. I think,

**Chris Gammell:** I think you have to, you're on the periphery because you also have to, you know, you're doing these interesting hard science problems, but you also have to then raise money. Right. So like you have to walk into the same offices that, uh, you know, VCs, uh, talk to all, all comers, I'm sure. And so you might pass them in the hallway.

**Greg Charvat:** Well, there are certain VCs that are, that like to do hard tech because the ROI and hard tech is higher. Yeah. And so there is on average over time, the ROI is higher, but the hard thing about hard tech is you need to be in it for the long haul to win the game. Right. Yeah. And so it's a special class of VCs that have deeper pockets than the wrap, a software wrapper around Claude, um, contingent. So we, we talk to a different class of VCs to, to do this stuff. So it's not,

**Chris Gammell:** it's not the same timelines and all that stuff.

**Greg Charvat:** It's not really the same ones doing that stuff.

**Chris Gammell:** You know, as a third party observer, if Teradar wins, you get the whole automotive industry, which is not small. And, uh, you know, the whole self-driving industry, which is not small. Right. And potentially robotics, potentially military, potentially all these things that are down the line that like, you just, you don't know.

**Greg Charvat:** There's a big market opportunity here. We're focused on automotive, but that's, you're right. That's, that's, there's a huge market opportunity. We're doing some, some military work as well, but primarily automotive. And I think, um, I don't know. I, I'm, I, I shamelessly pitching everyone listening that we're hiring. If you'd like to join the pirate ship. Let's get it. Let's get into the pirate ship. Just like I do. We all have stock. We all get a, you know, we all have skin in the game. So let me know if you want to do something crazy.

**Chris Gammell:** So, well, I'm, uh, aside from the program and what people would learn about, uh, as they, like, let's talk a little bit about like,

**Greg Charvat:** that's where we probe chips though. That's where the chip probing happens. So nothing else happens in the program except probing chips.

**Chris Gammell:** I mean, I'm surprised. I was actually surprised it was not a clean room to style environment, but it is a finished chip, I suppose. Right. I mean, yeah, it's a passive, RF connections.

**Greg Charvat:** And you just got to land on the pads. It's not, you don't need a clear room to land on the pads.

**Chris Gammell:** But I imagine that connection between RF test equipment and piece of silicon is quite critical. Like that could be an interface that goes poorly.

**Greg Charvat:** Yes. So, so I, I have advice for anyone who's landing, who's dropping a needle in the program.

**Chris Gammell:** Okay.

**Greg Charvat:** Okay. That that's what, that's what we call it. And so you're dropping needle. And by the way, dropping a needle, it comes from audiophile speak for putting a record on just so you, that's right. That's our joke here. So, um, when you drop a needle in the program, what you want to do is, uh, for RF connection, what you want to do is pipe your VNA into that probe. And then when it drops, you'll see the S one, one scatter energy go down and that's how, you know, you've dropped it correctly. So that's the trick. Cause you don't want to put too much pressure on it. Cause you'll break your probe. And, uh, the chip will win. It'll destroy the probe because it high frequencies. The probe is the, the, the, the point of failure. That's the thing that could break. Yeah.

**Chris Gammell:** That is the discontinuity. That's gonna, it's gonna ruin your afternoon, right?

**Greg Charvat:** Yes. And the higher the frequency of the probes, I mean, our probe room, we can probe up to 750 gigahertz in our probe room next door to this room. And so those, the higher you go, the weirder the probes get in, in the probe room. So those probes have like, like, like MEMS contactors on them. And, and so they really want to break because to fix them, you have to send it back.

**Chris Gammell:** The capacitance of your scope probe was, uh, you know, you're paying a lot for that. I imagine the, the, the investment in that space is probably very significant.

**Greg Charvat:** Well, you're a fan of test equipment. If you notice this correlation. So the, the more expensive the test equipment, the more prone it is to break.

**Chris Gammell:** Oh yeah.

**Greg Charvat:** Did you notice that?

**Chris Gammell:** At the worst at 2 a.m. Right as well. At 2 a.m.

**Greg Charvat:** Yeah. Yeah. At 2 a.m. And what's the lead time to get another one or to fix it? 15 minutes.

**Chris Gammell:** Forever.

**Greg Charvat:** Yes. Yes. Yes. Yeah.

**Chris Gammell:** You might as well, you better have, better have some, uh, some spares, right?

**Greg Charvat:** Oh my gosh. Well, yeah, you do. You need spare. So we always have spare probes and stuff, especially if it's a critical thing, we'll buy a spare in advance or whatever. We, we've, we've broken lots of probes here before, uh, because we might push a measurement or probe a chip too many times. Cause we're trying to do something or learn something and, or recheck it. And, and yeah, we've, we've, we've, we send them. We, we've got a, we've gotten Christmas cards from our probe manufacturers. They love us.

**Chris Gammell:** I believe it. Yeah. Bottle, bottle of wine, right? No,

**Greg Charvat:** they're too cheap for that business. How much might you have to spend to get a bottle of wine? That's what I want to know. No one, no one's answered me that maybe a cheap t-shirt. It's good just to buy your own. It's good. A shitty t-shirt. Yeah. Right. Right. Right. Right. Right. I love all the t-shirts that they give us. Yeah. Yeah. They're nice.

**Chris Gammell:** Um, well, so what is the kind of work that, so first off locations, because you guys are on site and then what is the kind of work and the kind of profile

**Greg Charvat:** people that you're looking to hire? Oh my gosh. All right. Yes. I'm going to, I get to talk about this in front of your, your crowd. Cause you have this, your, your listeners.

**Chris Gammell:** This is symbiotic as well, right? People want to work for cool ass companies. They, they know Greg, they've seen, heard Greg five times now. Uh, they know that they'll be listening to wait. So when you use these vacuum tubes in the shop, it sounds like everybody's got to listen to the same music. What, what is the playlist? We rotate the playlist. Okay. So, so,

**Greg Charvat:** so it goes from metal. Metal play metal to Bob Marley to grateful dead. Uh, and we, of course, of course, classic rock. That's, that's the work in music, classic rock, you know, swing a hammer to that stuff. We like doing that. Um, there's a station on series XM called fly nineties hip hop, which has all the rap from the early nineties.

**Greg Charvat:** that's a fan favorite. That is a, with, with Dr. Dre and Snoop and all, that is a fan. I think, I think,

**Chris Gammell:** I think you're working at a startup, a tech startup, and you just said serious XM that right there might be disqualifying. I think that is like a radio, Greg, like programmable satellite radio. I just, I don't know about that.

**Greg Charvat:** Well, they stream it for one thing, but secondly, there's no advertisements, which, and also no AI thing that, that when your playlist runs out, it starts guessing your music, it just starts the shittiest songs ever. I, well, some of the young people play their play, but we mix it. I always go with the, I go with the turntable or the serious XM. That's what I do. Okay. That's, that's my turn.

**Chris Gammell:** But the young,

**Greg Charvat:** the young people, the young bucks might do the, the whatever, you know, the Spotify or whatever the hell it is.

**Chris Gammell:** The youths these days, you know,

**Greg Charvat:** but they, they, so, so, so we've also done, you know, the beetle, there's a beetle station. We like to listen to. We listen to like all kinds of, it was like, you know, two thousands indie rock. And of course, whatever, not a lot of Taylor Swift in this lab. Okay. Yeah. Not yet. At least I have no opposition to whoever you hire from the empire audience.

**Chris Gammell:** They can bring their own flavor. That's what I'm hearing here. They can. Yeah.

**Greg Charvat:** We rotate, we rotate. Yes.

**Chris Gammell:** Where, where are you guys first? So what are the three offices?

**Greg Charvat:** So we have three offices. We have a Boston office. We have a Guilford Connecticut office and we have a San Jose office. Those are our three offices. So it goes San Jose. Three tech scenes. The three tech scenes.

**Chris Gammell:** The three tech scenes. San Jose, Boston, rural Connecticut.

**Greg Charvat:** Yes. Rural Connecticut.

**Chris Gammell:** Short drive to New York city. How about that? That's, that's what we'll say.

**Greg Charvat:** And Boston. We're actually halfway between the two. And there's actually a lot of little tech companies here because it's a sort of a tech enclave. Okay. And, and we're able to hire lots of people who are involved in join our, to join our pirate ship who are doing the other companies. So we have three spots. How it works is the chips are essentially designed San Jose. Okay. The software is essentially done in Boston. Okay. And we've got like a wide range embedded stack down to like RTL and all that stuff. Right. And the, the systems integration and sort of like the, the over the air and chip tests and all of that stuff where the over the air physics meets putting the chips on the, on the sensor boards and loading up with the software and then testing them, calibrating them, characterizing their basic performance. So they meet the fundamental limits that happens in Connecticut. So we're like the systems integrator between the two. So if you want to see, if you want to touch like all the systems all the time, that's where that generally happens. And then if it's like software touching the software, which is like a big blank space, because you have this digital phase array to do all kinds of cool stuff with that happens in Boston. And then the, the IC design is in California and every site has a lab as well. They all have different levels of laboratory. So we kind of have the biggest mad scientist lab in Connecticut, but there's a lab in Boston and that's mostly focused on like, let's, let's test this thing on the customer performance metrics and KPIs. That's what they're focused on testing. Right. Whereas we're testing against radar, spherical targets and canonical targets and first principles, testings and calibration. That's what we do. We're doing the thing in the EM textbook. Right. But they're testing against the real stuff in Boston and writing the software against that. And then in, in California, they're designing the chips from scratch, which is so good. So that's how, that's the disposition of our company. We're always flying back and forth between all the sites or taking the train. In my case, it's, it's, it's very fluid. We meet the cold company meets twice a year. We have these all hands retreats where we just, just F off. In the middle. Yeah. We don't do any work. We just hang out and socialize. So we all kind of get along and, cause there's a lot of pressure in these companies. You got to make sure we're all human here and we're all trying our hardest. And you know, we do that. And so that, that's how we're set up though.

**Chris Gammell:** That's great. That's great. I mean, what is, what is the profile of a person? Like, do they need to have gigahertz experience? I mean, no, not necessarily. Gigahertz, terahertz.

**Greg Charvat:** Depends on the, the, the job. So there's a few, there's a few openings right now. So we have, um, one of them is head of marketing is open right now. You don't have to touch gigahertz stuff.

**Chris Gammell:** I could do that.

**Greg Charvat:** That, that, that we might be open.

**Chris Gammell:** Not really. I couldn't actually know.

**Greg Charvat:** That might be the only tech bro we hire is head of marketing. I'll, I'll give you that. We'll hire a tech bro for that. That's, that's a very tech bro job. That's fine. That's part of the description. Head of marketing. Um, let's see. Uh, we have a, uh, customer engineer, uh, opening. So an F field engineer, right? So when you're going after customer site, uh, give them the, you might be in Detroit. You might, you might have to hang out in Detroit a little bit. Detroit, Germany, South Korea, or Japan. Yeah, there you go. Yeah. France. What happens there? So there's quite a few, wherever they make cars is where you might be going. Yeah. Which is fun. So F AE. Yeah. That's a good job. Especially. It's a good job for your, your, um, if you're a generalist to some extent and know about sensors, that's, that could be the job for you. Right. And then there's a defense F AE. So applying the terahertz sensing to defense problems and understanding the defense space. So perhaps, uh, someone who may be an engineer, who's also a veteran might be a good fit for that. Right. So just an idea, um, analog mixed signal chip designer. That's California. That's actually California. Or remote because chip people have been working remote for decades before the rest of us. So, right. Exactly. Um, that one can be, I guess, anywhere on the planet engineer. So analog mixed signal.

**Chris Gammell:** It's so specialized too. It's just like, you got to go wherever that town wants to live. They get to live there. Yeah,

**Greg Charvat:** I know a lot of them live in Hawaii. So they can work on stuff at TSMC in between California. I don't know if you know that. That's a thing. I did not know that. That's interesting. Yeah. That's where, uh, the famous, um, Stanford professor Boris Merman went actually. And, uh, he lives. You know, I should probably do great.

**Chris Gammell:** Cause I probably should go record some, some, uh, some record some shows out there, you know, and charge it to the empire credit card. You know what I mean? Yeah.

**Greg Charvat:** Oh yeah, definitely. Write it off on your taxes or something, you know? Yeah. Yeah. Yeah. Yeah. Yeah. I had to go to every meal, every like cocktail you drink on the beach, every bite. Just right on the card. Um, yep. Let's see what else we have data collection engineer. Okay. This is someone who's good at collecting gobs and gobs of like autonomous driving data. We're not in the business of autonomous driving, but you're collecting data like that, like point clouds and stuff like that. And knowing what you're looking at. Let's talk about that real quick.

**Chris Gammell:** So, so that, that was one question I had before we started was like, what is the output of the Teradar? And you said it's point cloud. Just, I mean, not just like, but like a Lidar does. Right. Yeah. Yeah.

**Greg Charvat:** And then there's additional things in the point clouds, like a velocity and whatever else you want. Amplitude loss. It's, it's a pretty nice, it's basically like a Lidar, but it has radar characteristics to the data too, that it's kind of like a, got a couple more dimensions than a normal Lidar data set. It's cool. Interesting.

**Chris Gammell:** Yeah. That's very cool. I mean, yeah. And that's, I think one of the illustrations on the Teradar site shows like a ball bouncing across the street as a car's driving, right? Like, yes,

**Greg Charvat:** we are good at that scenario.

**Chris Gammell:** So like that as like a motion detection, like,

**Greg Charvat:** well, I mean, the sensitivity and resolution is so good. There's nothing, we don't need the motion to see that. So we, but motion is nice, but it doesn't help or hurt us in any way. So we just see it.

**Chris Gammell:** But there's probably novel applications in that space though too. Right? I mean, like just, yeah, it's the kind of thing where like, you don't know if you need it at first, but then like maybe, maybe, maybe it's outside of automotive as well. That's, that's just really interesting. It's another dimension.

**Greg Charvat:** The rich data set coming out of this thing is incredible. It's like, it's like a white space of sensing really. I feel like we're, we're just beginning to learn what we can do with it. I mean, it's a digital phased array imager. We could, you could do all kinds of stuff with it. We're just now scratching the surface. Let's see. In terms of, oh, sorry, go ahead. Well, you've got one more that you might like. RF systems engineer. RF systems engineer. This is a big one. This is someone who, who might have some experience doing radar system design at a big defense contractor or a national lab or at the air force research lab, something like that.

**Chris Gammell:** Is it, is it a Tony long? Is that a Tony?

**Greg Charvat:** Yeah. Tony. Yeah. Tony could probably, I don't know if he wants to move out to one of our sites, but Tony would be, yeah, I think Tony would be a good guy for that. Quite frankly, he knows a lot about that stuff. Then there's, there's another interesting one that might be along Tony's lines, advanced chip packaging engineer. So chip packaging, we do our own package designs in house. Right. And we really need someone to pull the oars on that. Another, another player. So if you are a chip packaging engineer and you want to do tarot's packaging, which is new and no one's really doing, we'll be the first ones to do it in production. If you want to be the first person to make a high volume production tarot's chip package, come join us, join the pirate ship. Our cannons are pointed at all the other sensors. And then second, another one is a DSP software engineer. So this is, yeah, just cranking. So our, we have a really good sig proc team, but they have signal processing. Is that, is that signal processing? Yeah. But they have more work than we have people. And we have lots of really interesting, hard problems. And so if you want to join the sig proc team, which is very close to the tip of the spear, then come on down, send me an email. I will talk to every single person who emails me. So anyway, that's it. That was the opening opening. That's great.

**Chris Gammell:** Oh, that's, and it shows a variety, I think as well. And this is how Greg CEO also said that, yeah, you should go back in the amp hour instead of like, don't talk about anything. He said, go find some nerds, bring them to the pirate ship. Right.

**Greg Charvat:** We love nerds. We're all a bunch of nerds. I'm not the CEO. I'm just the CTO. I have a lot to say.

**Chris Gammell:** We have the nerdiest nerds here at the amp hour as well. So like Greg wants to work with you. In fact, Chris Lafke, listener of the show. What a wonderful nerd. And started as an intern now a full time, right?

**Greg Charvat:** If there's a nerd kingdom, you know, you have the King and Queen of the nerds. He's definitely one of the Dukes at this point. Okay. Okay. All right. He's in the Royal court. Or a Duchess. One or the other. He's in the Royal court. He's in the court of nerds. And so, yeah, he's, he's, he was here from like day one, almost terribly. Well, yeah, pretty much day one when we had a, a warehouse in Clinton, Connecticut, that was full of dust and rats and mice. Yep. Seriously. We are invested with mice. He took some swings. Yeah. He joined it and, and help set the mouse traps, man. And kill the little black flies that would come out of the sewer and fly around the lab so that they wouldn't get in the way of the chip probes. You know,

**Chris Gammell:** it's a startup life. You got to do it all. Right. I mean, you got to, you got to do everything.

**Greg Charvat:** Man, it was, yeah, we took, we take out the trash. Yes, we do that. Yes. You have to do all of it. But he was there from day one. And, and he and another young lady, Salah came from another local university. She, she is incredible too. So we had two, Chris and Salah, young folks started from day one and now they're, they're now leaders in the company. So, that's awesome. Yeah. So it's, it's, it's, it's, yes. So join a startup if you want to move fast. And if you get worn out from a startup, pop out of a startup for a while, then jump back in when, when you're ready for another challenge. A lot of people do that. There's nothing wrong with that.

**Chris Gammell:** Yep. Yeah. I, what else do we have to say here, Greg? Well, I'm not the CEO,

**Greg Charvat:** by the way. I'm not the CEO.

**Chris Gammell:** We,

**Greg Charvat:** I, I don't think anyone. We knew that,

**Chris Gammell:** Greg, we knew you were, you're CTO material. You are, you are CTO cloth. You're a maid of the cloth. You are,

**Greg Charvat:** you know,

**Chris Gammell:** like that is.

**Greg Charvat:** But, but I have something to say about this. Okay. So I see a lot of these, I see this happening all the time. So you get these like smart people come out of like. Grad school or postdoc and they want to do a startup and they're, they're the on the bench people that the geeks like me and you need to be on the bench, but they also want to be CEO. Don't do it. So I'm telling everyone, don't do it. Stay on the bench. I have a, I have a friend who has,

**Chris Gammell:** yeah, he says, he says he wants to be CEO. And like, I'm sure he will be, but like, I tell him the exact same thing. I'm like, do you know how many stupid investor meetings you have to be in? It's going to suck. And like dealing, like the CEO has to deal with people stuff. Ew. Yes. People. Yes.

**Greg Charvat:** Yes. HR.

**Chris Gammell:** You have, you are the, you know, you are the end all be all. You don't get to do the tech stuff. You just get to talk about on fine.

**Greg Charvat:** You don't want to hire an HR team until you're big enough too. So it's going to be a while before you get the HR team. And by the way, they know, you are HR. They're not, you know, they're wonderful, but they're not going to handle all of this stuff. When things get really tough on that front, you're involved. And so like, yeah, you don't want to be that. If you're a technology person, you want to add the value to be added is with the technology. And I just, I don't think you want to do both. I think that the historical example of that was, was Thomas Edison. He had to do both. Right. And he never quite got to the level of his contemporaries like Firestone and Ford and the other folks before it was a little much younger than him, but he never quite got to the contemporaries of, of the industrialists at the time, because in part, not entirely, but in part, because he couldn't let go of, of both what we'd call today, the CEO leadership, as well as the, the intellectual leadership being on the bench, which is what he liked to be at. So he would be on the bench getting bothered to, at, to make executive decisions about, you know, making the first electrical deployment in the city of New York and things like that. Like you don't want to be negotiating with the company that does the sewers in New York and 1880. Right. You want to be making the wires, right. You want to be figuring out the resistance drop and how the grid works instead of doing that.

**Chris Gammell:** So you should have come with AC in the first place. Come on, man.

**Greg Charvat:** Yeah. Yeah. I,

**Speaker ?:** I,

**Greg Charvat:** that's a, that's an interesting one. I, I think, I, I think that was just kind of the, the level of, you know, his understanding and level of everyone's.

**Chris Gammell:** I mean, he was vindicated in HVDC eventually. Right. But yeah, I think back in those days, well,

**Greg Charvat:** the holdup for the deployment, as you know, of very familiar, the history of this is what held up AC from being ubiquitous was spinning motors. Hmm.

**Chris Gammell:** Yeah.

**Greg Charvat:** And, and, and so spinning motors was really, there were AC scaled because you could get lighting out everywhere. Right. It was powering lights, but it still couldn't spin motors. And you really needed to spin motors to, uh, what to power factories and to have fans in people's houses and stuff. Yeah. To make the money. Right. Lights were half of the thing. Lighting was half. At least people's homes weren't burning down anymore because they had open flames everywhere or dying of asphyxiation or whatever.

**Chris Gammell:** So that part was new problems of, uh, fire and wire.

**Greg Charvat:** You still need to spin stuff, right. To make the modern, uh, uh, world. And so Tesla's greatest contribution to this was making the AC motor. And that really was his contribution to it. Everyone saw that AC scaled, but the big Achilles of AC was that motor. Once the motor came, it was game over on that front.

**Chris Gammell:** So it's good stuff. What is your, uh, I know we gotta, we gotta, we gotta wrap this up. I'm sorry. You're a very busy person, but, uh, I feel like your reading list would be very interesting. Can we have a Greg Charvat, Dr. Greg Charvat, a reading list of nonfiction, historical, uh, technology books.

**Greg Charvat:** Let's see right now. I'm reading Carl Sagan's Broca's brain, which is a wonderful book written in the mid 1970s, uh, before, uh, the cosmos and before they even, uh, launched the Voyager spacecraft. Oh, Voyager. So it's, he talks about what the Voyager mission will be like. So that, that is one of my favorites. Uh, I'm getting through it right now. I'm reading this, ah, this book about, um, the history of radio communication in the Vietnam war. Okay.

**Chris Gammell:** There's, there's the Greg. Yeah. Rick.

**Greg Charvat:** Now this book, um, and I, gosh, I can't, I'm terrible at names. I can't remember the name, but this book, it was, it was someone's, um, masters or PhD thesis, uh, at, at, um, at one of the famous, uh, us war colleges. And, and so he turned it into a book and, and it is very, very dry. But if you're a fan of, of, of military surplus radio gear, which I am because I am a ham and I love fixing old stuff. And if you're a boat anchor fan, you have collections of military stuff and you've got civilians, you have a whole mix of vacuum tube stuff. Well, all your favorite radios are the starring characters of this book.

**Chris Gammell:** Nice. Is this the voices of Vietnam by chance? Is that the, no, no, no, no, no. Is it the professionals history of Fulon?

**Speaker ?:** No,

**Greg Charvat:** God, no, none of those interesting books. Uh, it is a little dry. Sorry to the author who wrote it. Um,

**Chris Gammell:** that's okay. It was objective type stuff. It's,

**Greg Charvat:** it's, it's, it's, um, it is by far one of the most interesting books I've ever read on. Well, my Google isn't working right now, but, um, it's, um, it's a great book. We'll, we'll get it for the show notes later. We'll get it. We'll put in the show notes, but man, so this book starts show notes or two stuff.

**Chris Gammell:** Get the book book rec from Greg and then send him your resume. That's, that's going to be the move. That'll be the move here.

**Greg Charvat:** It is. Send me your resume. If you want to join the pirate ship, if you want to do weird stuff, you want to go up to terror. It's going to be at hundreds of gig arts. There's a thing we say, there's a, there's a saying at Teradar and you want to hear it. It'd be a great way to end the show actually. Yeah,

**Chris Gammell:** let's do it. All right.

**Greg Charvat:** So, you know, we're building radar imaging systems here. Okay. And the thing about a normal radar imaging system is you can, you can see the antennas, right? When you do your 2.4 gigahertz stuff, Chris, you can see the antennas, right? You can see them.

**Chris Gammell:** A little tiny chip antenna. Yeah, yeah, of course.

**Greg Charvat:** Well, we like to say at Teradar, if you can see the antennas, you're not high enough yet. Okay.

**Chris Gammell:** Okay. Got it. I like it. I like it. That's right. All right. Thank you, Dr. Greg Charvat. Appearance five, or I guess your, your appearance five on the amp hour. I always love having you on. I love chatting with you. Thanks for being here. We'll have stuff in the show notes about how to get in touch with you and send resumes. Greg's wife.

**Greg Charvat:** Sure. I'll talk to everyone who writes me. We'll chat.

**Speaker ?:** All right.

**Greg Charvat:** Great talking to you again, Chris. Always a pleasure.
