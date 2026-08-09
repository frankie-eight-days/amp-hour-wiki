---
episode: 618
title: Refrigerators and Robots with Amitabh Shrivastava
url: https://theamphour.com/618-refrigerators-and-robots-with-amitabh-shrivastava/
---

**Amitabh Shriv:** This is The Amp Hour Podcast. Release February 5th, 2023. Episode 618. Refrigerators and Robots with Amitabh Srivastava. Welcome to the Amp Hour.

**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. Hi, this is Amitabh Srivastava. I'm a maker from Jersey City. Hey, Amitabh. How are you?

**Amitabh Shriv:** Pretty good. How are you doing, Chris? The last time I saw you, you were refrigerating fireball shots on the run. On the run? On the go? Yeah. It was a very impressive setup you had. And I was like, you know, you and I had talked, I think, at Maker Faire or something prior to that about your last project. 2019. 2019. Yeah. So I'm really glad you're here. I'm really glad we're going to be talking about some of this stuff.

**Chris Gammell:** I'm very excited to be here. I mean, I used to listen to the Amp Hour as an undergrad student back when I was studying physics. And, you know, was like deciding on becoming an engineer or not. So.

**Amitabh Shriv:** Tell me about that. So physics and I mean, I'd say you were squarely, you know, I've seen the stuff you build. I'd say you're squarely in the engineering space. You are applying those physics skills. So what what was the switch over? Like what was the interest in studying physics and what was the switch to engineering?

**Chris Gammell:** Yeah. I mean, so I've been interested in like making stuff since childhood. Like, you know, the typical thing of taking toys apart and like, you know, trying to make stuff and. You had the knack. Yeah. Yeah, exactly. But I like, you know, I had a little curiosity for astrophysics in particular. Like, you know, in high school, I did an internship on exoplanet detection. And yeah. So I was like kind of on track to become an astrophysicist. Like, you know, there's this big engineering exam in India. I don't know if you know about it. It's called the IITJE.

**Amitabh Shriv:** OK, no, I don't know about it.

**Chris Gammell:** So it's like the national like imagine like the MITs.

**Amitabh Shriv:** OK.

**Chris Gammell:** And then like a bunch of them in India and like they have like one entrance exam.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** And, you know, it's the dream of every high school student in India.

**Amitabh Shriv:** I've definitely heard of IIT before.

**Chris Gammell:** Yeah, I know. Yeah. Yeah.

**Amitabh Shriv:** I took the exam and. Specific exam just for that university, though, you're saying.

**Chris Gammell:** Yeah. Oh. So, you know, I took the exam and like, you know, I got through and like, you know, and then I was like, no, I don't want to do this. You know, I want to do physics.

**Amitabh Shriv:** Oh, man. Turn it. Turn it down. You got to the gate. You know. Yeah. That's not. I'll play that card. Can you imagine the amount of astrophysicists that are going to pop out of the woodwork after like the James Webb Space Telescope? Like just like like there's just. Obviously, there's a lot of stuff to be done in the space, but like just the images that have come out of that and the interest level. I can only imagine. I would hope that my high school physics teacher was showing those images and inspiring young minds like that. So, yeah, I have to imagine a healthy young crop. You're going to be going into that.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. I mean, but actually, so I got turned off of physics from like through an astrophysics internship, actually. Oh, really? Yeah. I was studying in Bangalore, India. Right. At the Institute of Science. And I was doing an internship at Brandeis University in my third year of college on radio astronomy. Right. And I was like super focused on astrophysics at this point. But I just realized that most of, you know, astronomy is like coding now. It's like running simulations and, you know, just analyzing data and all of that, you know, because you're not actually like, you know, just you have this vision of like, oh, you know, you're in this observatory in Hawaii somewhere with a big telescope and looking at stars and like, you know, kind of like, oh, there's a wobble in that star. You know, that's funky signal or something. It's not that at all. The computer gets to look not at your eyeballs. Even for James Webb. Right. You know, I mean, it's difficult now to tell like, you know, what, you know, what's with cameras in your cell phone, for example. Right. You know, whether it's not actually taking an image, it's creating an image, right. You know, artificial intelligence.

**Amitabh Shriv:** It's averaging and it's, you know, James Webb telescope probably. Right. Right. It's a good point. Yeah. Yeah. I think about the one woman that like revealed the black hole image they did a couple months ago at this point. Right. And she was just talking about her Python script was running for like a really long time to like stitch together all these different images from the different satellites. Right. To make that black hole image. And it just sounds like lots and lots of code. Yeah. Hmm. Interesting. So and radio astronomy, I imagine, too, is like I'm sure there's like the applied aspect of building radio telescopes. But that's probably. Sure. Yeah. Pretty far separated from the physics programs.

**Chris Gammell:** Right. Oh, yeah. Certainly. I think, but also with radio astronomy, like there's one neat trick, which essentially you have multiple radio antennae all over the world. And it's like VLSI array, very large scale interferometry array of radio telescopes. And essentially using like multiple small antennas, you can create like you can essentially emulate an antenna the size of the planet Earth. Yeah. Yeah. And, you know, so at that point, you know, any single antennas data is, you know, is nothing. You know, you have to combine all of that data and that's the only thing that you have. So like, you know, yeah, the computer is doing all the work.

**Amitabh Shriv:** Well, take that college professor who taught me matrix math. I didn't need it after all. Well, so then what was the hop over to engineering? So then you started building stuff instead?

**Chris Gammell:** So I've been building stuff through this while, right? Like, for example, in my first, second year physics lab, every week, you know, we'd have like three days of physics lab. And the first day the experiment experiment would be introduced and like, you know, I'd be like, OK. And then that night and the next day, I would figure out a way to automate that experiment with like an Arduino or some using the audio data in for my laptop as a oscilloscope or something. And then like, you know, pretty much every experiment I ended up automating. And so I had been doing that the whole while. And in fact, my... Was that an ethical question?

**Amitabh Shriv:** Was that cheating? I don't know. I don't actually know. Like, or is that...

**Chris Gammell:** No, I don't like to think that. That's great. I like it. Yeah. No, it was amazing. Yeah. So my physics teacher and a lab professor loved that. And I ended up actually making this kit for training high school teachers in India on kinematics and mechanics, right? So we made this thing like actually used a solder sucker as projectile launcher. Yeah, this is true. The solder sucker, we just remove the tip so it goes faster. We had like just simple, you know, beam splitter kind of timing systems. You know, you study projectile motion. So, you know, you point the solder sucker at different angles and, you know, you see how much time it takes for the steel ball bearing to drop. And like, you know, it was just about enough resolution with the old Arduino Uno that you could actually make out the differences from air resistance, which was very exciting for me.

**Amitabh Shriv:** Yeah, right. That's always the catch that you get with the early physics stuff, right? But you could actually see that. Yeah, gravity is not 11 meters per second squared. It's a little bit less. It's actually 9.8. Yeah, right. Yeah, that's cool. Wow. Okay. And so how far and wide did that spread?

**Chris Gammell:** I'm not sure. We wrote a paper about it. So there might have been some people who replicated it. But this is one particular institute which trains for teachers in Karnataka. So they used it pretty heavily. But after that, you know, I kind of actually ended up through multiple things as the engineering consultant for the ecology department. So as like an undergrad student, I at one point had like a room, like a small office and professors would come up to me and talk to me about their projects. And I would point them to like, you know, open source hardware resources or like if nothing existed, then, you know, we'd make something. Like, so I ended up making all sorts of things like underwater gates to study like fish decision making, a bunch of drones for aerial photography. Did you figure out that fish are pretty, pretty nuts? I think not actually. Pretty much every time we have. So I was in an ecology lab, right? And pretty much every time we've looked at any animal, we found that they're smarter than we thought they were.

**Amitabh Shriv:** Oh, interesting. Okay. That's reassuring. Reassuring. Yeah. If you eat fish, I suppose, but. Yeah, exactly. Yeah. Yeah. Cool. Well, that sounds like a good gig though. Yeah, it was great. Having a range of problems people come to you. I made a wind tunnel.

**Chris Gammell:** I made like tachometers to study insect wing beat frequency. My thesis project was this 13 foot tall PCB that measured elephant height in the wild. Wait, a PCB? I mean, it was like composed of four separate circuit boards. Still, that's huge.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** Wow. Took me about a dozen movies to solder it at. It was like a very simple circuit. It was essentially beam splitter. You know, I'm sorry, not beam splitter. Beam forming? Not beam forming. Like essentially just had like IR remote LEDs on one side and, you know, IR detectors on the other side. Oh, okay. And.

**Amitabh Shriv:** Oh, I see the photo of it on your LinkedIn. It's like in the shape of an elephant.

**Chris Gammell:** So like if you, if an elephant passes through, then yeah, that's what you just cast. Got it. Cast a shadow of whatever's moving through in between. It's kind of like a line scanner.

**Amitabh Shriv:** That's cool. Yeah. Okay. All right. Yeah. That makes sense. Yeah. That's super cool. And it's like out in the field then too.

**Chris Gammell:** Well, yeah. See, that's what kind of happens with a lot of these projects is like by the time we got to a point where we could actually deploy it, I was, you know, heading out of college and, you know, we didn't have like a lot. Yeah.

**Amitabh Shriv:** Just like the project timeline and stuff. Yeah. I mean, tell me about India. I'm not sure. I think we've had maybe one or two guests from India, but like what's the electronic scene like there?

**Chris Gammell:** Oh, man. Okay. I got to tell you about this one thing. So back in college, right? I was in Bangalore, which is like a big city in India. And for example, there aren't like things like micro center, like even Home Depot for that matter. So the DIY scene is like very spread out. But there is like in every city that one area where you can go to find components. And, you know, it's like a bunch of very small shops with very densely packed stuff. But you can find this one store that sells you like, for example, ball bearings. Okay. And you can just go up to them and be like, hey, I want like this kind of ball bearing, but not in this material, but in that material. And they'll work with you to figure it out. Right. But you don't get to call them up really. You have to go over. But it's great.

**Amitabh Shriv:** But there's one in every big city kind of thing? Pretty much.

**Chris Gammell:** Yeah. Yeah. So in Bangalore, you have like a guy. You got a ball bearing guy, right? Yeah. So like in Bangalore, it was SP Road. And like, you know, once a week, probably at one point, I would like go there and talk about my projects to the shopkeepers that I'd gotten to know. And like, you know, they'd recommend stuff to me. And I learned a lot of stuff that way, honestly.

**Amitabh Shriv:** Yeah, that's awesome. Yeah. You get like the kind of like the knowledge just from all the stuff that they've seen. They're like, well, you could do it that way. But I've always seen it done this other way. Yeah.

**Chris Gammell:** Like all the engineering students who go there and like, you know, also talk to the shopkeeper about their projects. You get to learn that knowledge kind of. Yeah.

**Amitabh Shriv:** Yeah, it's true. And I mean, like the convenience of like the online stores is incredibly high and much less centralized. Right. But the downside is, you know, get that human connection.

**Chris Gammell:** To be honest, I don't know. I think things have probably changed a lot by this time. Yeah. And this was, I was in college in 2013. So it's like 10 years back.

**Amitabh Shriv:** Yeah. Yeah. Yeah. I mean, yeah, exactly. And I think a lot of the distributors that we use here in the States now, I'm sure ship over overseas. Yeah. Yeah. It's just like, it's all open up a lot more. So that's.

**Chris Gammell:** I think. Yeah. But like, for example, 10 years back, I don't think Adafruit was that big either. Right. So like, I'm sure they were like. Not as big as they are now, but yeah, they were, they were. They were around. Yeah, for sure. But like, you know, the amount of stuff and the amount of tutorials and things was much less.

**Amitabh Shriv:** What about industry that's there? So actually I had, when I worked at ABB, we had a factory that was like a CM that was in Bangalore. I never had to go. But like CMs and similar like electronics manufacturing.

**Chris Gammell:** Is there a lot of local stuff? Yeah. I'm not too familiar with that, to be honest with you, because I didn't really work very much as, as an electronics engineer in India, just for a couple of years after college. Also, it's a big place.

**Amitabh Shriv:** So like, I'm sure that there could be, and you just don't expose, you know, exposed to it.

**Chris Gammell:** Oh, no, definitely. There are. And especially now there are more popping up. Like, you know, I've been hearing about people using like manufacturing in India. And in fact, like for the last five years or so, there's been this big move of like making India.

**Amitabh Shriv:** Actually, yeah. Matt Venn, who was just on the show too, he was talking about the RISC-V is really getting big in India as well. And I saw a thing about like India, I think the Indian government pushing for more like semi-manufacturing, stuff like that.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** But I think that one thing that's like importantly, an important distinction, I think is even like, you know, from undergrad, I don't think that people, I think hardware is kind of almost discouraged because there isn't as much money in it for students. In IITs, for example, the top rankers all go to CS and not many people go to EE. Yeah. And.

**Amitabh Shriv:** Well, maybe it'll change, you know, over time because CS is boring. It's so boring. See, we know we're on the right show at this point, you know, that we're both like, yeah, CS is boring. We want to talk about electronics, you know, if you were nodding your head as you're listening to this audience, you're in the right place. Yeah. But we all got our code at some point, so I'm sure we'll get, we'll get back to that stuff too. Yeah. Okay, cool. So, so you're in the States now. What, what brought you stateside?

**Chris Gammell:** So I, I had worked in India for a couple of years, six months of that was actually in California. I was part of this gaming startup. We were making like these vests that you could wear and play laser tag and similar games like anywhere. Like so mesh communication stuff. That was when Laura was just getting started as well. So a lot of like, you know, playing around with that stuff.

**Amitabh Shriv:** And was it fast enough for like gameplay?

**Chris Gammell:** Like, yeah, no, that was definitely one of the issues. I think that we were trying to do five to zero zero bits per second was the total bandwidth across like, you know, multiple suits, which, you know, if you're trying to do simple gameplay, you know, it's one or two packets a second is already what, what you really need. So we were just about able to make it work, but it wasn't seamless.

**Amitabh Shriv:** Yeah. I remember when JP was on the show a couple of years ago at this point, he was like a, he was doing like an alternative to like, like sub gig alternative to Laura, but he had worked in Laura. And one of the, one of the things that he brought up that I had never thought about before was just like the scaling problem. And, you know, there, you'd only have so many things talking to channel. You have so many, you do have more channels, you're more than one channel, but, but they're slow. And as you have more devices in a network, you start to have more collisions and stuff like that too. And so it just, and you start to, you think about network capacity in addition to the, you know, the, the slow, low and slow chirp that a Laura is. And I can imagine that would be a lot to work with.

**Chris Gammell:** I mean, I, I was kind of doing more of the prototyping with XBs and trying to like assume that we'll get the Laura thing going at some point. But yeah. Yeah. I mean, XBs are still out there too. They're, they're really expensive, but like they are rock solid. Yeah. They're really fun to prototype. Yeah. If you can get them to work and like, especially like the GUI stuff is like so neat. You can just set them up and like, you know, then they just work. It's pretty good.

**Amitabh Shriv:** Yeah. Yep. Yep. Yeah. That's another thing that I feel like it's good for, it is good for prototyping. It doesn't scale as well. And for one reason, like just being cost, but especially for like, like, like one of my, one of my friends was doing like just a point to point. And it's just like, yeah, it's just like you put two XBs in between and it's like a serial terminal. It just pops out the other side. It's pretty cool.

**Chris Gammell:** I mean, but, but also I think that now with a bunch of open source tools and like, you know, the, what's the, I'm going to butcher this, that NR, not the NRF, but the. Okay. Like one of those modules. Oh, geez. It was really popular. Nevermind. Okay.

**Amitabh Shriv:** Well, there's like the NRF 24 that that's like, those are like the really cheap ones that like James Bruton. Oh yeah. Yeah. Yeah. No, you're right. You're right. Yeah. They were NRF.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** But I, yeah, those are NRF 24s, but then also then all the Bluetooth stuff and you got Ant and Thread and all the, and like Bluetooth mesh now too, which.

**Chris Gammell:** Does it work? Yeah.

**Amitabh Shriv:** The Bluetooth mesh stuff? I've never played around with it. It does. It, I've heard it does. Yeah. I know some people that have deployed systems with it, but it's, I think it's in specific scenarios that it's better. A lot of people end up still going like custom protocol. I feel like, you know, they use the, they use the modems on board basically and either sub gig or 2.4. And then they, and like, you can get it. It's just like a lot more overhead. Then you have to manage a lot more of like the network stack and it's outside of my pay grade. Yeah. For now, I love the loaner. I love the loaner. I love the loaner. I love the loaner. I love the loaner. I love the loaner.

**Amitabh Shriv:** I love the loaner. It's good to go outside and make it have a custom protocol. So gaming startup didn't go?

**Chris Gammell:** Yeah. So then I moved back to India and I was kind of starting slash managing the hardware department for this logistics company. They were like a software company, but they wanted to have like a hardware player, right? Yeah. Yeah. Yeah. Yeah. So it was me and like, you know, a couple of other guys and we were just like kind of throwing whatever at the wall to see what would stick in like, you know, the logistics hardware space. Right. So yeah. So gas tracking and stuff like that. Yeah. Yeah. Bunch of asset tracking, GPS kind of stuff. You know, in India, a lot of delivery people use two wheelers. So, you know, trying to do navigational leads for them, like, you know, battery charging solutions for them.

**Amitabh Shriv:** Oh yeah.

**Chris Gammell:** But what really kind of caught on was I made this handheld laser box size scanner. It's like a very simple laser distance meter essentially, but you could find the size of a box and then, you know, generate a quote for the customer at the point of pickup, which, you know, the way it's typically done is that you measure that with a ruler and then like, you know, write it down and then someone transcribes it at the warehouse and also at the warehouse, like a laser scanner, an actual conveyor belt laser scanner does the scanning. But then of course there's going to be like discrepancy between the actual size and what the ruler measured. Right. Right.

**Amitabh Shriv:** And they paid for it a day ago or whatever.

**Chris Gammell:** Exactly. So there's like, you know, especially with e-commerce giants, right. You can imagine that the actual difference in these little things ends up being like millions of dollars. Oh yeah. All put together. Right. So, yeah. So, so that was something that we worked on, like, you know, we got a patent and stuff and cool, but I don't know. I just felt like the hardware scene in India was too constrained. It was just too small and I kind of peaked where I didn't find many opportunities beyond that. And also I was like, you know, not really too interested in the actual hardcore engineering of it. And I was more interested in creative applications. So, you know, I found this master's program at NYU called ITP. And the best way to describe it is that it's an art school for engineers and an engineer school, engineering school for artists.

**Amitabh Shriv:** Yeah. So. You are our second guest from ITP. Oh really? The other one is Matt Richardson. Yeah. From Raspberry Pi. Now at Raspberry Pi. And yeah, Matt went to ITP as well. That's, I think when I met him, he was at ITP. Nice. Awesome. Awesome program. Like, and like, I got to walk through the workshops and just like weird, awesome things happening there. Yeah. That was a good, good two years for me for sure. Yeah.

**Chris Gammell:** Just let loose, you know, and just let your creative process flow.

**Amitabh Shriv:** Is it uncomfortable? So like, you know, it sounds like engineering background, but then like, is it uncomfortable with the creative aspect or were you already kind of there?

**Chris Gammell:** Definitely. I did feel like sort of, it was like, like reverse imposter syndrome, I guess. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. Like being this guy who's really not that artistic amongst artists.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** But it was great at least from a, that I could work with other artists and like, you know, help people with their problems. And like, you know, that's kind of where also I found that, oh, I really enjoy consulting on cool projects. Like, you know, because then I don't own the project, you know, and someone else can take it forward, but I get to do the cool part of actually making, you know, one-offs for artists, which is great.

**Amitabh Shriv:** Yeah. So then in that space, I'm just doing callback like crazy here. So Todd Bailey, who was on the show also in New York, he did that for a long time. And it's Mike Harrison as well. Both, both of them were like, kind of like doing engineering work for artists. It does seem like that's like short timeline, tight budget type of work though, sometimes like if it's not well-funded. Oh, for sure. It's just fun though.

**Speaker ?:** Okay.

**Amitabh Shriv:** All right.

**Chris Gammell:** So once you take the money out of the equation. Yeah, yeah, exactly. As a student, you know, you don't think about the money as much. That's true. That's true.

**Amitabh Shriv:** Yeah. I made it to ramen. I made it to ramen this week. Yeah. I mean, obviously in New York, it's not a cheap city either. That's true. Yeah. That's, you did have to make compromises there for sure. Yeah. Yeah.

**Chris Gammell:** So, and then did that last? Oh, well, so during college is when I developed programmable air in the soft robotics class at ITP. So for our viewers, our listeners, programmable air is this open source kit that I made for controlling pneumatic soft robots. So it's essentially this, you know, 10 by 10 centimeter PCB with a couple air pumps and a few valves and a pressure sensor so that you can like inject high pressure air or suck air out of a tube and, or like, you know, let air went to the atmosphere and like get pressure feedback while you're doing this. And it's just controlled by an Arduino nano and, you know, a very simple library that controls it all. And, you know, artists and academics love it for soft robotics.

**Amitabh Shriv:** That's awesome. That is, I think that's the context of you and I meeting. You were showing this off at maybe open source, maybe open source hardware summit. Is that possible? I was at open hardware summit 2018. Yeah. Maybe it was there. Yes.

**Chris Gammell:** You were there?

**Amitabh Shriv:** Yeah. I think maybe that's when we met. When did we meet? We met at some point and I, I definitely saw programmable air and you had, you had like tear down 2019 at an after

**Chris Gammell:** party. Oh, I think it was an after party at like some makerspace or something.

**Amitabh Shriv:** Okay. That actually that we just re aired Zach and Joshua who I interviewed at that. They came back on the show five years later or four years later and talked about their grad school experience. Yeah.

**Chris Gammell:** I, I, I remember I listened to that podcast.

**Amitabh Shriv:** Right. You were at the same party. Maybe you were in the background.

**Chris Gammell:** Yeah. Yeah. I remember, I think I met Zach for the first time in that party as well. Wow. Okay.

**Amitabh Shriv:** Wow. I had met Josh before. The Nexus. Yeah. Of The Amp Hour. Yeah. Yeah. And so, so this thing you were showing, you were showing this to me and to expand on the audio picture of what this is, it's not just the pneumatic piece, but then you also had like these kind of flexible, I remember you had like flexible grippers. Yeah.

**Chris Gammell:** It was like, like white, it was like a jamming gripper. So it's essentially like a latex balloon filled with a coffee grain. Yeah. And when you pull a vacuum, it just, all the coffee beans get stuck together, you know, because they're being pressed from outside atmospheric air and between coffee grains, like, you know, it just so happens that there's enough friction to hold a very solid shape. So what you do is remove the vacuum, then you place this thing over an object and it conforms itself around the object and then you pull a vacuum. Yeah. So it becomes like this custom shaped solid. That's just about the shape of the solid that you're trying to pick up. And then you lift the thing and then you...

**Amitabh Shriv:** It's kind of like if you've ever seen someone palming a basketball, if they're just doing with the friction of their hand and not the fingertips, you know, you can kind of imagine that same kind of thing. But yeah, you could pick up pretty big stuff with that. I remember.

**Chris Gammell:** Yeah. Yeah. It's, I mean, so grippers are kind of like the one area where soft robotics is still finding like actual use in industry and warehouse and stuff. Because, you know, you can imagine like for an automated, grossly kind of warehouse, right? It has to pick up like a bag of chips or like, you know, eggs or, you know, all sorts of weird, different shaped objects. And like, you know, soft robotics is the way to do that. Like, you know, a lot of big companies are just making grippers for all these industrial robot arms. And some of them are using vacuum jamming grippers, just like, you know, the one that I was presenting.

**Amitabh Shriv:** So like these would be end effectors on like a KUKA or similar? Yeah. Or like a universal robotics? Huh. Interesting. Those systems are like so expensive and so big that I just really don't have it. Like the fact that there's subcontractors, like why wouldn't just the robot maker make the end effector? But of course not. Like these are huge expensive systems and they can like bear the brunt of the cost. Yeah.

**Chris Gammell:** And like, you know, once you make something, you know, why not sell it to the other robotics company as well, right?

**Amitabh Shriv:** Yeah. Yeah. You said soft robotics is not fine. You said the grippers, the jammer gripper is one thing of soft robotics that's finding its place. So is there other stuff that is not finding its place?

**Chris Gammell:** Well, so there's a lot of soft robotics research happening and, you know, there's a lot of art kind of use cases. But in industry, I think that that's where soft robotics is mostly finding its place. I think that eventually soft robotics will find its place in a lot of other places. But there are a lot of interesting challenges because like, for example, soft robots are very difficult to simulate, right? You need. Oh, right. Right. And they always, always. Except in Big Hero 6, they did a good job on that one. Well, to be fair, Baymax, the character is not technically a soft robot because it has a carbon fiber skeleton.

**Amitabh Shriv:** Yeah. The core thing. Yeah. You're a good point. Good point.

**Chris Gammell:** And also like, you know, the characteristics of the robot change with time as it like, you know, wears and tears because, you know, micro cracks develop all over the place and like, you know, the system overall changes. So you need like embedded sensors and you need essentially like active algorithms that are compensating for whatever is happening with the gripper. Like force feedback kind of stuff? Yeah. Yeah. Force feedback kind of stuff. Are they doing that with like vision right now or how do they? Yeah. Yeah. Typically like, you know, you, you just solve it with vision, especially in like, you know, a kind of warehousing kind of thing, you know, if it has caught something or not. Right.

**Amitabh Shriv:** Yeah. Camera says ball, ball dropped or another egg dropped. Yeah. Oh, interesting. Yeah. Yeah. It's, it is. I have seen some, like, I think some research papers on it and I've wondered, I think they always talk about like Mars and like space type stuff too, because you can, because you can inflate it, it's also pretty portable, but interesting. Baymax is my main, my main reference.

**Chris Gammell:** Actually from Baymax, I think that this one thing will happen in not too distant future is like a backpack electric car. Back? Oh, you got to explain that. Okay. Dude. So like you can have an inflatable car, you know, that like a single or two seater kind of thing. No, I know. I did not know that actually. Yeah. I mean, I think, so there's this place called Other Lab. Oh, I know that. Yeah. They're at Berkeley. Yeah. Oh, all right. So, so they actually made a prototype of this, like a car that like flat packs, you know, because you have the battery, which is flat and wheels that are flat, you know, and this is like, you know, bicycle wheels. So we're not talking like, we're talking like smaller than a smart car, ultra compact, but just the fact that you can have something that, you know, you can take backpacking up, you know, to a mountain or something like that. And then like, you know, ride around is amazing.

**Amitabh Shriv:** I want to make one. I mean, if you, yeah. And if you could, if you can build it at the top of the mountain, you actually don't need an engine anymore. You can just get gravity. You need good bearings. Yeah. And a lot of, a lot of personal liability insurance.

**Chris Gammell:** So what is the, so inflatable car though too? So, I mean, the frame essentially can be inflatable. You can mix stuff really rigid with inflatables. Also like you can design and suspension into the inflatable itself. That's, that's pretty cool. Yeah. So then, but the wheels aren't inflatable. No, the wheels are like essentially bicycle wheels, you know, with hub motor and like the battery pack is the bottom kind of thing. Yeah. Huh.

**Amitabh Shriv:** Okay. Like skateboard design sort of thing. Like a skateboard. Yeah. Huh.

**Chris Gammell:** But the roll cage around you is the important thing is that, you know, essentially in terms of like mechanic, like in terms of electrically, it's, it's like an e-bike or something. Right. But it's much safer because you have an actual seat that you're strapped into and there's a roll cage around you. Huh. And that's the real value of a car.

**Amitabh Shriv:** I'm going to remain skeptical about that. I mean, I'm sure safer is a relative. Oh yeah, for sure. I will not be getting in one of these ever in my life. I would love them to work that into like a James Bond plot though. That would be really great. That would be nice. Ta-da, do, ta-da. Yeah, yeah. It'd be even better if he's inflating with his mouth. Oh my God. Yeah. That'd be really good. Cheeks are really good. Yeah. Okay. So, so what, what happened with the project? Is it still being used in like, uh, out in the world?

**Chris Gammell:** I mean, honestly, I've, I've been really bad about like making new batches. I think I've done like three batches so far and they just sell out immediately. Yeah. And in fact, like today I have to put together a kit for this academic who wants to use it for some micro, micro fluidics stuff. And they're like, Oh, we're like on a tight timeline and we can't wait, you know, till June when the next batch is supposed to be like shipped. So, you know, can you, can you help us out? And I'm like, okay, I guess, you know, I'll just make one. Like I, I've sold like, even like before, so I crowdfunded this on crowd supply. And before I ever went to crowd supply, I had like already sold like a few dozen of these things that I had hand soldered.

**Amitabh Shriv:** You're like, Hey buddy, you want to buy a inflatable programmable air kit?

**Chris Gammell:** Unlike the street corner in New York or what? Yeah. No, I had like this Google form. Like I titled it the super secret programmable air. Yeah. Yeah. Because like I presented it at the 2018 maker fair in New York city. And that's where the project really kind of took off. People absolutely loved it. And I didn't realize that, you know, it would get such a good response. And that's how I ended up presenting at the open hardware summit as well, which was actually just three days after the maker fair. So here I am like, you know, in presenting. Right. And I think one of the organizers messages me on Twitter saying that, Hey, look at your DMS. Like, you know, she asked me on like a public Twitter or something because I was not looking at my DMS. I think some presenter had dropped out last minute or something. They were like, can you present this? Like, you know, you've heard good things about your work from maker fair stuff. I'm like, okay. Yeah.

**Amitabh Shriv:** Last minute Grammy nomination right there.

**Chris Gammell:** It was amazing. You know, and I always have this kind of passion for live demos and so I had live demos made for open hardware summit and on stage presenting them. It was great.

**Amitabh Shriv:** That's awesome. And that's a good way to like, yeah, drive interest too, especially when you give a good demo, which I've seen in you do. That's a good way to keep people interested in what you're, what you're working on and stuff.

**Chris Gammell:** The way I see it as like, it's just a challenge and accountability of like, does the stuff work all the time? You know, because if it's not working with me, you know, just by myself on my workbench, you know, that doesn't have quite the impact of it not working in a, you know, showing showcase kind of setting. So if I plan for a live demo, I understand where the system breaks a lot better because every time it breaks, you know, I will go to the actual root cause rather than just be like, oh no, it's fine. You know, probably it won't do that again or whatever. Yeah. What, uh, so you then crowdfunded on CrowdSupply? And, uh, you know, still selling on CrowdSupply. Oh, you are?

**Amitabh Shriv:** Okay, cool.

**Chris Gammell:** I was wondering about that. I think, so now CrowdSupply has been bought by Mouser or something. So it's actually being sold on Mouser. I don't know if there's something happening there, but essentially, yeah, still selling.

**Amitabh Shriv:** They were actually bought in 2019. I looked at it or 2018. Okay. Yeah. It's been a while. It's been longer than I thought. I just saw Josh from CrowdSupply.

**Chris Gammell:** So maybe then the logistics of how they do it has changed because the last time I had to send it to Mouser rather than sending it to CrowdSupply.

**Amitabh Shriv:** Ah, there you go. Yeah. No, that's a pretty cool thing. I, I, that was a good purchase on Mouser's part, I think. Yeah. I like the CrowdSupply folks. Oh, yeah. It's great. But then like the logistics stuff, it does make sense if you're going to keep, you know, like if you're crowdfunding this thing, you probably want to keep selling it. And so, yeah, it's just kind of a natural piece then. So that's great. So that's the, that's the runs you're doing are kind of like just to keep the supply up. Yeah, pretty much. At Mouser.

**Chris Gammell:** I'm lazy about it, to be honest.

**Amitabh Shriv:** Well, it's, you know, it's your product. You get through what you want. And it's open source. So you can just tell people, you'd be like, well, if you want to do it, just do it yourself.

**Chris Gammell:** Yeah. I mean, the only thing like, for example, is so these valves that I'm using, right, are typically used in these Keurig machines and stuff. And I, so the first several runs that I did, I had to buy like secondhand valves from American Science and Soplus and like, you know, similar stores that, you know, had, these were previously used things that had been taken out of machines. And I had like a bunch of quality assurance issues with that, but I won't like, you know, I think 25% of the valves was just not usable. Yeah. Because I was already running them slightly out of spec of the pressure range.

**Amitabh Shriv:** Yeah. Did you find the quality before it? Yeah. You were like doing in-house testing kind of thing. Yeah. Yeah. So it was just scrap.

**Chris Gammell:** I mean, it's just, so then I just got to like remove the valve and like try another valve. A good way to lose margin. Yeah. So then when I spoke to the supplier, which it was quite difficult, like, you know, just trying to get ahold of them. But when I finally did, they're like, you know, they won't even talk to me for anything less than 2000 pieces. And my runs are like significantly smaller than that. They're like, you know, I'm making like 150, 200 pieces of programware kits at a time. Yeah. So I had to buy like stock in bulk. So like, that's, I think the one thing that I want to in the future change about the project, if I ever get around to it is like, try to get valves that you can, you know, individuals can source as well in case.

**Amitabh Shriv:** Ah, I see. Yeah. Right. Yeah. You could sell a simpler, simpler version of the kit. You can do like a DIY kit and make it more, more sourceable. Yeah. Yeah. That is tough. I mean, especially with mechanical components where like, that is a, I'm sure understanding the, like the nuances of one valve over another, that actually probably matters quite a bit. Oh my God. Yeah. Like when I go and search, when I go and search on like motor sites for like DC motors, I'm like, I don't know. Like, does it go, does it turn around? Like, I think that's important. You know, I just don't have any knowledge. And so then when they present me with like a search matrix, I'm like, the cheapest? I guess maybe the second cheapest, you know, like when I order a bottle of wine, you always do the second cheapest.

**Chris Gammell:** Yeah. Yeah. Oh my God. The whole, and I think that also the thing is like with mechanical components you have typically the spec sheets are a lot shorter. You don't have nearly enough data. Oh, interesting. Why is that? Just because of the manufacturer? Yeah. And I guess like, you know, it's just the way they're expected to be used in, in the way, in kind of like the discipline that they're made for. Right. So these are meant for Keurig machines where you have this kind of thing that's boiling water, steam, like, you know, steam is building up and then you're just going to switch this valve on and it's going to let, you know, the steam into and through your coffee pot or whatever. Right. So that's what the valve is designed for. So in the spec sheet, you know, the data will kind of be depending on that. So for example, like a big one is the valve is never experiencing pressure in the opposite direction. Right.

**Amitabh Shriv:** Uh-huh. Because they design other pieces into the system that don't allow backflow or whatever.

**Chris Gammell:** Right. So that is something that I have to find out myself. So like, you know, and I actually ended up buying like dozens of valves to try to find out something that would work for the kit. I think that was the main work in the project was trying to find stuff that, oh my God, trying to find stuff with the same orifice size so that I could use the same tubes to connect things. That was such a big problem was like, you know, you'd find the perfect valve except that.

**Amitabh Shriv:** Right. You order it and then doesn't, doesn't fit when he gets home, it gets to your house.

**Chris Gammell:** Like, it's just like, yeah, the tubing sizes are like incompatible. And then you don't want like, like five different connectors in, in your kit. Right. So.

**Amitabh Shriv:** Yeah. Yeah. Hmm. I mean, that is the, you know, when you think about like a kit and like one, I think, you know, you've been, it's not like if I could connect the arc of your career, it sounds like you've been kind of helping that interface for people that are not in the electronic space. You basically build like an API for hardware, basically in this case, programmable air and before, like the scientific equipment and stuff like that. But that is the main, that is a huge value. And that's what I look at like some of the scientific equipment that's out there and just the margins they get. And it's like, yeah, it's not the most complex gear, but it's the tested for the scenario that they, that they need. And that is worth paying for.

**Chris Gammell:** Yeah. But I don't think that I should, I do hope, you know, for more open source hardware, scientific equipment stuff, you know, because man, like it's really holding back science is the thing. Right.

**Amitabh Shriv:** Like, oh, sure. Yeah. I'm not saying I agree with the actual output. I'm just saying that like, if, if there is value to be had in those very high prices that they charge, it is, it is definitely like low volume, but then also, you know, it is proven for the scenario. And like when people can get their hard, their scientific electronic equipment onto a paper as well, it's like, that's like another proof point basically in showing that like it has done this experiment and you should also do it. So like there's a lot of weirdness in that space, but also I get some, I get some of it, you know, it's kind of the institutional stuff. Well, I just found the link on Mauser for programmable air. So I will have a link in the, so people can check it out. What do you tell people to build the first time? Like what are people, what are people building with it generally?

**Chris Gammell:** Like it actually ships with the stuff that you need for making a jamming gripper, except for the coffee. Oh, come on, man.

**Amitabh Shriv:** That's where's my own coffee? Where am I going to get that? Just like an entire cabinet in my house. Cool. Yeah.

**Chris Gammell:** I think that's a good way to get started or just like, you know, blow a balloon. You know, that's fun trying to, you know, I think quite a few people have done like balloon as data interface, essentially just kind of.

**Amitabh Shriv:** Oh, that's kind of cool. Yeah.

**Chris Gammell:** Just the size of the balloon represents whatever data. I think that's cute. It's nice. Yeah.

**Amitabh Shriv:** That's fun. Cool. That's great. Okay. Let's move on to your, the thing that I talked about at the top of the show, which was the refrigeration stuff. Now this, it looks like you were wearing a proton pack at Supercon. So I saw you at Supercon 2022. Yeah. That was last November. And yeah, it looked like you were wearing a proton pack. Tell me. Sure. What it was.

**Chris Gammell:** So it's, it's a backpack refrigerator with like a battery powered refrigerator that's dedicated to cooling a single bottle of liquor. Right. So the way it works is it's all the components of a regular refrigerator. So it's a vapor compression based system. There's a compressor, evaporator, condenser. The only key is that the evaporator, which is the part that gets cold is this heat plate exchanger. So you can have refrigerant running through one set of plates and right next to it is another set of plates that you can run a liquid through. And so, you know, your liquid gets cooled. So I'm taking. Right.

**Amitabh Shriv:** And you're not drinking, you're not drinking Freon. That's another important thing.

**Chris Gammell:** It also was using propane as a refrigerator. Ah, propane. Oh, nice. Just for that extra spice.

**Amitabh Shriv:** Also not something I try to drink on a regular basis, but yeah.

**Chris Gammell:** Yeah. So it's very interesting. So it's pulling the liquor from. So the liquor bottle is connected with an umbilical essentially to the evaporator of this backpack. And so it's constantly cycling the alcohol, pulling it up from the bottom of the bottle and then, you know, running it through the evaporator, getting it cold and then pumping it back out. And the reason actually that it ended up being an alcohol based system is that it was too cold for, you know, water based systems. Oh, yeah. It would just freeze immediately. Right. It would just. So I needed like hard liquor so that it does not, because it got too cold. Sorry for party rocking, man.

**Amitabh Shriv:** Just, yeah. I had to bring the party here. Yeah. Yeah. You didn't have to make a fireball. Oh, yeah. No.

**Chris Gammell:** I mean, there were good reasons for it. I just love the pun of a chilled fireball, you know? Yeah, that's pretty good. My girlfriend loves fireball. So what am I going to do? You make it a vodka thing? Yeah.

**Amitabh Shriv:** So there is a Hackaday talk you did on this. So it's called Refrigidiro? Refrigidiro? Refrigidiro? Yeah. Yeah. Yeah. Refrigidiro.

**Chris Gammell:** There's a story behind the name. Okay. So some, yeah. There's going to be like three people who are going to enjoy this, but they're going to enjoy it a lot.

**Amitabh Shriv:** You know what? That's what podcasts are all about.

**Chris Gammell:** Just getting those, you get those three people, you know? So my favorite book of all time is Harry Potter and the Methods of Rationality by Eliezer Yutkowski, who is this AI researcher. And in this fan fiction, Harry's aunt marries a professor. So Harry is raised into this scientifically literate and loving household. And then he goes on to...

**Amitabh Shriv:** You know, this is so refreshing just because most Harry Potter, when you say Harry Potter and fan fiction, it goes a totally different direction in the fact that it's going to rationality and science. Yeah.

**Chris Gammell:** The whole book is like a premiere on like rational thinking and all the psychological experiments. Like there's a whole series of chapters based on like the Stanford person experiments.

**Amitabh Shriv:** Was it widely published or was it like one of those things where it's like just a Word document?

**Chris Gammell:** So it's on... There's a really good dramatized audio podcast of this. But actually, my girlfriend got me this limited printing hard copies of it as well. Hard printing? Oh, man. Absolutely. That's great. One of my most treasured possessions for sure. Wow. That's great. That's really great. But anyway, in this book, there's the spell called Frigidiro, which is like, you know, for cooling things. And from there, I pulled Refigidiro. Yeah.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** I can make that mental. What was the purpose of the cooling spell? And rather, how does a scientist square with the world of Harry Potter?

**Chris Gammell:** Right. I mean, so it mostly doesn't go into like how magic and science like kind of works. It leaves a lot of things like hanging, but, you know, there's parts of it. Like, for example, Harry does these very basic like Mendeleevian experiments to figure out like, you know, magic is decided by just one gene, like whether you're magical or not.

**Amitabh Shriv:** All right. That's great. Okay. So basically, it's a premise to just talk about all the fun stuff. All the rationality stuff. Yeah. Yeah. Yeah. Okay. That sounds cool. I think I might give that. That sounds weird and wonderful. So I think I might give that a shot. Yeah. Okay. So we got the name.

**Chris Gammell:** And so I wanted to, this was right after I had quit my job. I was looking for like, you know, oh, I want to do this experiment, like, you know, this kind of project that has, will have an impact. Right. And I was like, hmm, like, you know, refrigeration industry, like, you know, cost contributes so much to like global warming and stuff, blah, blah, blah. And like, you know, there's very little innovation in the HVAC refrigeration space. Like, you know, it's hasn't really changed significantly since the sixties. So I was like, there must be something, you know, that can be done there. So I actually had this problem that my laser cutter needed a water chiller, right?

**Amitabh Shriv:** Okay. Yeah.

**Chris Gammell:** And everything that I could find was like, you know, 300 onwards dollars, right? You know, 400, $500 for a water chiller. And I could buy an ice maker for $90. So I'm like, why can't I convert this ice maker into a water chiller? Right. So I did that. And, you know, that was pretty easy. And I was like.

**Amitabh Shriv:** It's like dipping the toe. Yeah, exactly. That's interesting.

**Chris Gammell:** And then I found this friend who happens to live like, you know, just a few blocks, just a couple of blocks from my place, actually, who has like 15 years of experience in the HVAC world. And I'm like, hey, do you want to like, you know, kind of do this thing together? And we're like, oh, yeah, sure. So we were looking for something to get the conversation started with people about refrigeration. And we ended up making this backpack like pretty much over a weekend for a party here in New York.

**Amitabh Shriv:** Can you explain the refrigeration cycle? Because I feel like that's a. Sure. You're right that it's this old technology.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** It's very energy hungry. And I remember something about cycles. And like what I really remember is like in the diagram, there was always this. This kind of like sideways hourglass shape. And I never understood what that meant. But that's like the expander or the compressor. I don't know. There's something in there. But I just remember seeing that stuff. And I'm just like, none of this makes sense to me. You know, and then the mechanical engineers came in. They're like, Chris, get out of here. You're never going to get this.

**Chris Gammell:** Let me explain it to you from a very practical perspective.

**Amitabh Shriv:** Okay. Can you do it like Harry Potter? Like can you make it? Don't do that.

**Chris Gammell:** Yeah. So essentially the system is divided into two sides. There's the high pressure side and the low pressure side. Okay. The compressor, it sucks in low pressure refrigerant and spits out high pressure refrigerant. And as you know, like when you compress a gas, it heats up.

**Amitabh Shriv:** PV equals NRT. Yes. That's going to be in here somewhere, right?

**Chris Gammell:** Yeah. Yeah. So the NNR are constant and you're increasing the pressure, decreasing the volume. But yeah, I don't know if PV equals NRT is enough to kind of explain this. Okay. And there might be some non-ideal gas behavior happening as well.

**Amitabh Shriv:** Sure. But essentially. That's literally the only thing I knew in this space. So I'm out of, I'm out.

**Chris Gammell:** But so you're compressing this gas and it gets hot, right? So you then send it to this thing called the condenser, which is this big radiator, right? And you're blowing air across and you cool down this high pressure air. So out from the radiator comes this high pressure room temperature refrigerant. And then it goes through something called the expander, which probably is the hourglass thing that you're talking about.

**Amitabh Shriv:** Okay. Yeah.

**Chris Gammell:** Which can be anything. It can be like a small orifice or like a really long and narrow tube.

**Amitabh Shriv:** Okay.

**Chris Gammell:** When this high pressure gas comes out of there, it finds itself in a low pressure environment. So it immediately like evaporates, boils. And that expansion is what does the refrigeration. So if you actually look at the backpack, right? You see this copper tube, a thick copper tube coming. And then there's this coil of thin, narrow copper tubing and then thick copper tubing again. And one side you can see there's like room temperature. And then immediately after the narrow copper tube, you'd see like ice forming, you know, on the copper tube. Because as soon as the refrigerant gets out and into this low pressure environment, it chills down and cools anything around it. And that is the same as like, you know, the air duster thing or a reference.

**Amitabh Shriv:** Oh, like when you're using like compressed air in order to like cool down a circuit board to test. Yeah. I see what you mean. Okay. Interesting. So maybe we can, can we then, so then like on the, on my fridge, my place, I store food. They have all the same pieces, right? These, these are all the same thing. My air conditioner, my fridge, my. Pretty much. Exactly. It's the same stuff. I don't know. What else has it? My other air conditioner. Other than the Southland. Yeah. Yeah. Okay.

**Chris Gammell:** Yeah. So in, in your fridge, there is a big radiator on the back of the fridge. The entire back of the fridge probably has like copper tubing running and the back of the fridge gets really hot because that's where it's rejecting heat and inside is the evaporator. So copper tubing inside the fridge is where the refrigerator, you know, comes in at room temperature and then expands and then becomes really cold. Yeah.

**Amitabh Shriv:** And then, I mean, the reason it's so energy hungry is because the compressor is just a huge motor, right?

**Chris Gammell:** Yes. So the compressor is the thing that's, yeah, doing the work and, you know, getting the energy and there's many ways like, so the whole refrigeration thing actually is, is actually really neat where you can get more than a hundred percent efficiency and it's kind of like, what are you talking about? Right. Exactly. What I'm saying is that if you put in a hundred watts of energy into a refrigerator, you can move 200 watts of energy from inside the refrigerator to outside the refrigerator.

**Amitabh Shriv:** So if you're counting efficiency. Is that because of the latent energy that's already in the fridge, like the heat coming off of the stuff like from entropy is being captured or what?

**Chris Gammell:** Hmm. No, not quite. Right. I mean, essentially like there's nothing saying, if you think of a refrigerator as an engine in reverse, right? So if let's say you have a 70% efficient engine, right? What that means is that you're putting in a hundred watts. It's radiating 30 watts as heat output and 70 watts is going to mechanical input. So if you run it in reverse, you put in 70 watts of mechanical work. It takes in 30 watts. Yeah.

**Amitabh Shriv:** Yeah. That makes sense. Okay.

**Chris Gammell:** So then it's a hundred watts out. So, yeah, I don't think that quite explains it, but essentially you can move more.

**Amitabh Shriv:** Yeah. It's really because you're transporting energy as well. Yeah.

**Chris Gammell:** You're transporting heat. Yeah. Yeah.

**Amitabh Shriv:** Right. Right. Right. Right. Right. Right. Yeah. That's interesting. Yeah. It's not like, it's not like, uh, you know, above zero or what's it called? Uh, above parity. Yeah. Energy transfer. You're still that, that hundred watts you're putting in are still, it's gone. You don't get that back. There's no like, the useful work is moving chemicals basically. Right. But in moving of the chemicals is also heat.

**Chris Gammell:** So you can have like, uh, you know, the coefficient of performance is like this kind of efficiency. You can have that be like, uh, for like really good well-designed systems, like, you know, more than five or 10 even. So, you know, you put in a hundred watts and you're moving a thousand watts off, but, but that's not the reason why I think that, you know, you can design better refrigerators. You know, because that's a whole science in itself, uh, of designing refrigerant loops that are high coefficient of performance. The reason I think that it can be done better is that is, is from design and, uh, designing things from a human kind of perspective, like chest freezers, right. Are wildly more efficient than regular refrigerators. Because when you open a chest freezer, the cold air just stays inside. It doesn't spill out. Yep. Exactly. So I'm like, well, if we can, you know, make refrigeration, like refrigerator prototypes 10 times faster, right. And do a bunch of user testing. That's how I think that we can end up with better, more efficient refrigerators because, you know, you just find efficiency in a different part of the thing.

**Amitabh Shriv:** It does seem so looking, having looked at the backpack prototype, it does seem like because you need to have like a completely closed system, the prototyping would be tough because it's all brazed. I don't know what the.

**Chris Gammell:** It does seem like that. Yeah. And it is, but as I said, like, you know, we made the thing in like a couple of days and, uh, it really doesn't have to, like, especially once you get used to it and you're like, if you're specializing in sort of making refrigerator prototypes, then you can be really fast about it because it's, it's just raising, right. It's, it's kind of like soldering. Yeah. With a torch. Yeah.

**Amitabh Shriv:** Yeah. That's interesting. Uh, I was also, I think we talked about this when we were at the event, but you had mentioned Kip Bradford was on Adam Savage's thing as well. Yeah.

**Chris Gammell:** Uh, yeah. Kip, uh, made this, uh, kind of kit, which was actually using the same compressor. I think that we're using, he made this kit for prototyping refrigeration systems. And it's like, I think it's a compressed, uh, it's a condenser and compressor and maybe an evaporator as well, like all in one compact unit, which I think, you know, it's a great piece of kit. Although I've not actually physically use it because it's quite expensive. It's like, yeah. Right. Right. Right. Right.

**Amitabh Shriv:** Optimizing for different things. Right. And that, yeah, exactly. Adam Savage has some, some budget to spare. So that's good. And he was putting on a costume, one of his like walk around costumes, I think. Right. Yeah. Stay cool. Yeah.

**Chris Gammell:** So that, that's great. Right. You know, you can have a backpack refrigerator that's cooling your body. That's amazing. Like, you know, that's the kind of prototyping, which I think should happen more. Right.

**Amitabh Shriv:** Right. Well, that's, uh, don't they have, they need those in like spacesuits too, don't they? Like to, yeah. To cool them off when they're in the sunny side of the, hitting by the sun.

**Chris Gammell:** Actually, interestingly, uh, I think in the original NASA spacesuits, they were not using a refrigeration system. Oh, really? They were just using compressed refrigerant, which they were just like venting into space. Hope you don't run out. You'll burst into flames. So no one, you were letting out the refrigerant, you know, you were just exposing it to the, low pressure environment of vacuum. Oh, wow. And that cooled down the, you know, can that it's coming out of and, you know, you're.

**Amitabh Shriv:** Then they had like a circulator to.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** Yeah. Huh. Interesting.

**Chris Gammell:** Yeah. So you don't need a compressor at that point. You just come in with compressed refrigerant in your suit.

**Amitabh Shriv:** Right. But that's not a closed system. So you literally run out. Yeah. Not to mention in space. When you let things out a little bit at a time, it's a propellant as well. Yes.

**Chris Gammell:** Well, I mean, you can just, yeah. Have a nozzle that's spreading it out on two directions. Yeah. Then you don't get a net force, but yeah.

**Amitabh Shriv:** Yeah. But still. Yeah. Don't have a clogged nozzle. That'd be bad times. Yeah. Have a good tether, I suppose, the other thing there. Wow. That's crazy. So what do you want to do with this? I mean, like I have read things about like vaccine storage in different parts of the world is difficult because of refrigeration. Is that like a target, intend to target or just kind of more seen where it goes?

**Chris Gammell:** That is something that we will eventually get to for sure. There's some very interesting stuff with like ammonia refrigeration where you can like charge your refrigerator on like a campfire and then, you know, it runs for the whole day.

**Amitabh Shriv:** Wow.

**Chris Gammell:** And stuff like that. Yeah. Yeah. But right now, actually, this backpack might end up, you know, in a liquor company commercial or something like that. Yeah. I'm sure.

**Amitabh Shriv:** I could see that happening for sure. I mean, that's the smart money bet, I'm sure.

**Chris Gammell:** But I mean, it's just fun, right?

**Amitabh Shriv:** Oh, totally. Yeah. No, this is the joy of building. Like the fact that it made a booze gun at the end is inconsequential. The fact that you, you know, like when I saw you showing this thing off, people weren't oohing and aahing at the bottle of booze. They were oohing and aahing at the back of this thing with a bunch of copper pipes that were braised together. You know, like that's...

**Chris Gammell:** It was a very specific audience though, Chris.

**Amitabh Shriv:** It is the best audience.

**Chris Gammell:** That is... That is true. Yeah. Oh, man. People have got to go to Supercon next year. Oh, yeah. It is the best. Yeah. I'm a bit worried. I'm a bit worried. It's like a really well-kept... Yeah. It's a really poorly well-kept secret.

**Amitabh Shriv:** Uh-huh. Yep. Yep.

**Chris Gammell:** Because it's a small conference.

**Amitabh Shriv:** It is.

**Chris Gammell:** But the people are just so high class, like, you know, all the best people.

**Amitabh Shriv:** Yep. Yeah. It's one of my favorites for sure.

**Chris Gammell:** Yeah.

**Amitabh Shriv:** Okay. So one of the things I wonder about, like, so what are the other hard things about... So one is cost you mentioned. Another is energy input that we talked about. But, like, what are the goals? So, like, in the vaccine storage scenario, what are they trying to do? Like, if that is a target for you?

**Chris Gammell:** Right. So I've looked into it a bit, but, you know, I have not worked extensively in this. So I take this with the...

**Amitabh Shriv:** You got to get that Bill and Melinda Gates money, you know?

**Chris Gammell:** So with the vaccine storage stuff, right, the thing is about making a way to transport. So essentially, in the developing world, you don't have good cold supply chain, right? Yeah. So typically, over here, you know, you'd have these... You have these trucks that are refrigerated trucks, you know, and shipping containers that are refrigerated as well. But because, you know, sometimes you might not have... You might only have intermittent electricity. So you might end up, like, for example, you know, you land, right, and the vaccine is in this container with a bunch of ice, right? And you have to refresh the ice. But, you know, wherever you have landed or, like, you know, that you're going through doesn't have ice because, you know, there hasn't been electricity for two days. Right.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** So, right, that's the kind of thing that you have to then solve for, right? Right. And there was this great project, which was this ammonia refrigeration system that I was talking about, where essentially you have this water ammonia mixture. It's essentially called absorption refrigeration. Okay. So when ammonia gets dissolved in water, essentially, that's an endothermic process and that cools down the system. So you have this ammonia water system and two containers connected by a small tube. You boil off the ammonia so that it goes into the other container, right? So now you have ammonia in one container and water in the next container. And then when you turn this kind of upside down so that ammonia starts trickling down into the water, it starts, you know, slowly getting absorbed. And that, I think, is what cools down the system. And that, if designed well, you know, with good insulation can, you know, run for a whole day or like even several days of, you know, keeping the vaccines cold. And then when you need to charge it, you can just keep it on top of a campfire. Yeah. So that the ammonia then evaporates again. Yeah. And, you know, within an hour or so, it's, you know, again, separated and then you can, you know, take it out.

**Amitabh Shriv:** That is an interesting, I mean, especially because you think about like the energy input in that is like pretty. The campfire. That's the key. Pretty hectic, but also like very accessible, right? That's, that's, yeah. Yeah. Because like driving a compressor is not just a heavy load. It's also like a heavily inductive load. So like even driving that from a solar cell, I'd imagine would be difficult.

**Chris Gammell:** Yeah. Essentially you just, there are like RV refrigerators that run the same way as well. You can input either like 12 volt DC or propane. Yeah. And there's a heater like, you know, built in, which just burns propane. Okay. Yeah. And it runs the same way. Yeah. Or, or a similar way that that's actually the cycle is completely different. This is not really a cycle based system. It's like, you know, you physically have to turn the device and stuff, but yeah. Yeah.

**Amitabh Shriv:** Huh. That is. Yeah. I'd seen other things about some refrigeration systems also are going to like really high voltage buses and then they'll do three phase transforms. So what do they do? What is that called? I remember I had a motor kit that was like, don't touch this rail. It's 300 volts. It's 300 volts. It's DC. And interesting. And then it was doing like, I think it was a TI kit and I was doing like, like motor driving off that really high DC rail because that was a more efficient way to do it rather than doing like other AC generation. I'm, I really didn't understand how it worked then as well, obviously. But I have, I have seen fridge makers talk about that too. Like having high voltage rails inside of fridges as well, because even if you got like offline power, you know, you have 120 coming in, you generate a high voltage rail and then you do that. It was still more efficient or something.

**Chris Gammell:** Yeah. No. Talking about it. Yeah. Yeah. Yeah.

**Amitabh Shriv:** So I don't know. It's definitely interesting space. I mean, like, is there a lot of, so like, it seems like form factor and application spaces are there's right for innovation.

**Chris Gammell:** Yeah. I mean, for example, there's this company called a gradient that's making these window ACs that hang on the window. So if you can imagine, so typical window ACs like go on top of the window sill, right? Yeah. Yep. This is the, the actual system itself is hanging on either side of the window sill and you get a flat platform. So you can essentially use your window and you get a table.

**Amitabh Shriv:** Huh? That's pretty cool. Right. So that's. So like passes, it passes like the refrigerant line over top of the sill basically. Like, yeah, that's a cool idea.

**Chris Gammell:** So you just need the tube going to and fro and actually split AC systems are way more efficient than the window AC system. So you get the gain in efficiency as well as, you know, this aesthetic and utilitarian kind of thing. But, so this is the sort of system, which for example, I would say is like, I don't think that you necessarily need to make this, like, you know, you need to design it to the end in terms of efficiency. Just the fact that it is like, you know, a split AC system, it's already more efficient. Right, right, right. So if, you know, someone else.

**Amitabh Shriv:** A design choice that actually just ripples through the whole system, right? Yeah.

**Chris Gammell:** Huh. But I mean, I don't think that they're actually shipping. They're actually based off, or at least they have a team based out of New York as well. But I don't know if they're actually, they've gotten to, you know, ship any significant number

**Amitabh Shriv:** of units. It's not cheap. Just $2,000 for people who are. It is beautiful though. I mean, definitely. Yeah, it says early access still on their site. Yeah. Yeah. I mean, it's really, really nicely designed. Yeah. It's a great idea. Yeah.

**Chris Gammell:** But I don't, yeah, I don't think that it's necessarily, you know, that difficult to make a mediocre version of what they're trying to do. Right. Yep. And I think that that's still better than a typical window AC. Yeah. Yeah. And the other thing that I think is very interesting is like running air conditioners in reverse as heat pumps.

**Amitabh Shriv:** Yep.

**Chris Gammell:** So heat pumps are like this, you know, they're in the US, they're kind of, you know, set as this new thing.

**Amitabh Shriv:** Finally catching on. Yeah. Yeah. The Germans are like, uh, what? It's been around forever. Yeah. Right.

**Chris Gammell:** Right. But, uh, one thing that I kind of am hating is that like, you know, when these new window ACs, uh, come out with the heat pump feature, right. The way they'll probably be marketed is like, you know, oh, you know, this is like, you know, super green and stuff. And like, you know, you should use it to reduce your electricity bill and like, you know, help the environment. Oh, by the way, throughout your current window AC, give it to us and we'll give you a 20%. $25, $50 rebate. Right. Right. And I'm like, but how about, you know, let's look at trying to convert your current window AC into a mediocre heat pump because a mediocre heat pump is way better than an electric heater. Yeah. Right. Yes. So, you know, maybe there's a small percentage of brands of window ACs with the coils in just the right configuration that you can, you know, cut something and add a reversing valve and, and make it into a heat pump.

**Amitabh Shriv:** I don't know. No, those are, they've really, they have squeezed a lot of the money, a lot of the margin out of those things. They're just, they're incredibly cheap for what they are, you know, like just this, like you said with like, yeah, I mean, window ACs are super cheap, you know, like they're just, I can imagine they're not being made to be retrofit of course. And so I, yeah, it would be a very, very small group, unfortunately.

**Chris Gammell:** I mean, for, but I don't think that the ice makers were made to be converted to water shillers either, but that was actually surprisingly easy.

**Amitabh Shriv:** Yeah. What was the, what was the mod?

**Chris Gammell:** Because there was just enough slack in there. Sorry?

**Amitabh Shriv:** What was the mod you have to do to convert an ice chiller? Ice maker.

**Chris Gammell:** Nothing pretty much. I mean, I just removed all the plastic bits and, you know, bent some copper, which was the, which was the part that got cold and dunked it in some water. Okay. That was pretty much it.

**Amitabh Shriv:** Okay.

**Chris Gammell:** The bending of the copper was a difficult bit.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** We had to make sure it doesn't kink and crack. Right. Right. Yep. But there was just enough slack in it that it just worked. It's not highly efficient water chiller, but it's cheap. Yeah. It works. Right. Right. Right. Right.

**Amitabh Shriv:** Yeah. I think it's just a, you know, if we're talking to you, that's totally doable. If we're talking to like my parents, I actually don't want them to do some of that. That's, you know, like that's.

**Chris Gammell:** Oh, no. I don't think that, you know, anyone, anyone who's not like an EPA certified technician should not. Right. Right. Right. But I do think that that should be like, because especially there are a lot of grants.

**Amitabh Shriv:** Yeah. Yeah.

**Chris Gammell:** And the, I mean, the point is that the actual green thing to do is probably to retrofit. I'm not saying it's going to make economic sense. Right. Yeah. But you can probably make it make economic sense through grants that support it. Right. I see.

**Amitabh Shriv:** Yeah.

**Chris Gammell:** And they couldn't be like, you know, city efforts and you can maybe have like a kit, right. You know, that off all the tools and that's, you know, you ship it out or like, you know, a technician comes in.

**Amitabh Shriv:** Yeah. But as a New York resident, wouldn't you really miss all of the, all of the hissing.

**Chris Gammell:** Stuff that I find.

**Amitabh Shriv:** I was going to say the hissing and the squealing and the bumping that New York radiators do as well. I find as a former apartment dweller, not in New York and Chicago, but, uh, you know, there's that comfort in that waking up at two in the morning with, with hot sweats because you have to open your window. Cause you're like, what the hell happened here? Uh, yeah.

**Chris Gammell:** Yeah, I mean, I think my neighbors in my apartment building woke up at 2 a.m. because I was using the table saw.

**Amitabh Shriv:** Different problem, but very, they got a New York story now, you know, that's great. Amitabh, where can people find your work online?

**Chris Gammell:** So I'm on Instagram at Tinkermind underscore, that's T-I-N-K-R-M-I-N-D without the E. And I'm at Tinkermind pretty much everywhere else. Yep. And you're on YouTube now. You have a new YouTube channel doing that stuff. Yeah, it's at Tinkermind as well.

**Amitabh Shriv:** Yeah, that's great. All right. Well, I am very excited to see what you build next. You're always building very interesting things. I hope we see each other outside of conferences, but if not, definitely at Supercon and other fun conferences.

**Chris Gammell:** Sounds great. Always a pleasure to talk to you, Chris. Yeah, thanks for joining today. Thanks. Bye.

**Speaker ?:** Bye.
