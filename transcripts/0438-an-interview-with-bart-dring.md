---
episode: 438
title: An Interview with Bart Dring
url: https://theamphour.com/438-an-interview-with-bart-dring/
---

**Bart Dring:** This is The Amp Hour Podcast. Released April 14th, 2019. Episode 438. An interview with Bart Dring. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Bart Dring:** And I'm Bart Dring with BuildLog.net.

**Bart Dring:** Hey, Bart. How are you doing? I'm doing great. This is our, of total, the fifth ever in-person recording. But this is the new rig setup, so I appreciate you being here. Okay. Well, it's my first. Yeah. Okay. Yeah. People probably know you from your robots, right?

**Bart Dring:** Yeah. Mostly CNC and motion control. Things like that.

**Bart Dring:** I know you because we share a locker at M-Up.

**Bart Dring:** We do. I have one-fifth of the locker.

**Bart Dring:** That's right. Right. Right. And so what are the things that you're building here?

**Bart Dring:** Well, I try and build anything that has to do with motion control and CNC. And lately I've been working at a small scale to try and just learn a lot of things without spending a lot of money. And that's sort of what I'm doing lately.

**Bart Dring:** Yeah. Yeah. It's a lot of, it feels like a lot of ESPs and then like plug-in boards, but also they're low cost enough that they seem really accessible.

**Bart Dring:** Yeah. That's the goal. And so I've been doing the ESP32 thing as part of that because it's a really tiny little chip. It's cheap. And the Wi-Fi and Bluetooth make it so that you don't have to lug around the laptop too.

**Bart Dring:** That's great. That's great. Yeah. We'll definitely get back to that stuff too. What, I guess, you know, like you do a lot of motion control stuff. Like what, what is, how did you get into that? Why motion control in the first place?

**Bart Dring:** Um, well, it, uh, started as kind of a hobby. Um, I was working at a company and, uh, just doing some things on my own free time and stumbled across a pile of step promoters and, uh, started looking around. The junk bin problem. The junk bin and, uh, knew that, uh, you know, they rotated. That's about all I knew. Okay.

**Bart Dring:** Yeah.

**Bart Dring:** And accurately. So, uh, started searching around to see what people were doing with them. And at that time, uh, which was about 15, 16 years ago, quite a while ago, uh, noticed a lot of people doing a CNC. And so I built my first CNC and, uh, that's how I got started in it and kind of got hooked on it.

**Bart Dring:** What was your, what was your history prior to the pile of step promoters?

**Bart Dring:** Okay. Um, well, going way back to my first job, I worked at, uh, Williams Electronics, uh, designing pinball machines.

**Bart Dring:** Oh man. I just saw a thing about competitive, uh, pinball here in Chicago too. There's like, there was like an article that was like, if you ever want your palms to sweat while watching someone do pinball,

**Bart Dring:** it's like, okay. But still like, it's, it's a thing here, right? It is. Chicago was kind of the headquarters of pinball back in the day. And, uh, so I got this job at the entry level and was doing all sorts of things. Um, and, uh, but quickly, uh, just cause I was so young and eager, uh, worked my way up, uh, to being able to design anything they were doing. And, uh, they had done some video games, uh, pinball was kind of dying and then videos were video games were coming along. And, uh, but, uh, they did games like defender and joust and robotron. I don't know if you've heard of those.

**Bart Dring:** Well, I've, I've read, uh, a ready player one four times. So yeah, I've definitely heard of at least joust.

**Bart Dring:** Yeah. Um, but then Pac-Man came along and was really just killing everyone else in the industry. So they decided to make a go at it again with pinball machines and tried to, um, uh, put a little more life into them than, uh, they had, uh, where they left off. And, uh, so like electrifying

**Bart Dring:** the play field, playing field more, that kind of thing of like, yeah. And sort of making it more

**Bart Dring:** three dimensional. Now, if you look at a pinball machine, it's almost like three levels with wire racks and stuff like that. And we were the first people to do that. And, uh, we did games like space shuttle and a couple other games, um, which were the first. And, uh, I was right in there working with all that stuff, working with guys like Python Angelo and Steve Kordak. And these are, these are famous names.

**Bart Dring:** I don't know any of these names, but I'm sure the people that are pinball, like I know Jeff Kaiser's a big pinball, a mighty own big pinball guy. I'm sure he's listening like, what?

**Bart Dring:** Yeah. Yeah. So it was fun. I really didn't know what I was doing. You know, these are just other workers there. Um, but, uh, it was fun. I mean, back then companies were so kind of stale and stodgy, but this was more like a startup kind of environment where people like stayed all night and, you know, slept on the floor. Uh, the cultural thing. Yeah. And I was really attracted to that. So, uh, that was a lot of fun. But, uh, after about three years, I kind of got the itch that like, am I really an engineer or I'm, you know, making pinball machines and, um, and decided to look around and got another job. Uh, in hindsight, it was a really stupid, um, way to think about it because, um, you know, sure. I w I was having a great time and I was doing some good stuff and the people that stayed there did some really amazing stuff, but, uh, it was just a, an itch I needed to scratch and get out of there.

**Bart Dring:** I think that's the thing though, like the, that, that quote unquote real engineer thing like that. I've asked that of myself in the past too. It's like, am I doing everything that I, you know, that I have this ideal of what an engineer is out there. And it's like, at the end of the day, it doesn't, it doesn't really matter if you're enjoying what you're building, you're building new things, but right. But I think that that's a common. Yeah. And I

**Bart Dring:** was worried, you know, how it would look on a resume, you know, Oh, I did the pop-up clown and the, and all these funny things. And, uh, tell me about a time that you designed a pop-up clown part, but now in interviews and things like that, you know, when I talk to other engineers, they get all excited about the pinball stuff. So it probably was wrong

**Bart Dring:** about that as well. I just always think about like the current, the current drawn, the solenoids

**Bart Dring:** and everything. Like, it's just like serious. Oh yeah. It dims all the lights and you know, it's, it's, it's pretty, um, pretty crazy. I'd love to get back into designing some of that stuff, but it's crazy expensive. A solenoid for a flipper can cost a hundred dollars, you know? Seriously. Oh wow. And you know, you gotta, you know, maybe two dozen of them when you have all the kickers and all that. So it's pretty unapproachable as, as a hobby. Yeah.

**Bart Dring:** Yeah. I know, uh, Romain, uh, is someone who worked on like an open pinball. He actually came to a, um, a thing here in town and he was doing a, um, it was like an open pinball playing format and it was like lower cost, but it was like the electronics were lower cost. It feels like the components you're saying, it's just a lot of, a lot of copper, a lot of metal, just heavy, heavy duty stuff. Yeah. And low volume now too, right? Yeah. And there's

**Bart Dring:** a lot of wear too. So, you know, the pinball, um, you know, is striking things with a lot of force and the solenoids are cracking into hard end stops and stuff and, uh, things just fall apart if you don't, uh, design them well. Okay. So what'd you do after that then? Then I worked at a company that did, um, high power transmitters, uh, microwave transmitters for, uh, satellite communication and deep space networks and, uh, completely different Let's talk about pinball again. Come on. No, that's, that's super cool. Um, yeah, it was interesting and, um, uh, worked my way up and, uh, probably worked there for over 20 years and, uh, was the, uh, mechanical engineering manager, um, for most of the time. Um, and, uh,

**Bart Dring:** and that probably has like a lot of impact on like, because microwave is so like shape dependent, they always got those crazy ass antennas and doing weird things. It's probably,

**Bart Dring:** it's not just designing a box, I'm guessing. Yeah. It's not just designing a box. We were working with, uh, klystrons and traveling wave tubes. Oh, wow. We were really high power, you know, multi kilowatt. And, um, so, uh, yeah, there's a lot to do with high voltage, um, and, uh, high power dissipations. And then, uh, RF has to be, um, transmitted through waveguide because it's just, it'll smoke a piece of coax. And, uh, so you have, uh, like waveguide switches and all sorts of things that are really exotic. Yeah. What does it, what do those look like? Well, waveguide is like a rectangular cross section tube that is like a proportional to the wavelength. Um, so it's like this rectangle that's going from the transmitter all the way

**Bart Dring:** to the antenna. So like, uh, like almost an extruded piece of copper or something like that? Yeah,

**Bart Dring:** exactly. Um, and, uh, so when you go, let's say you want to switch it for like a redundant system. So if one transmitter goes down, you can bring the other one up. It's done mechanically. It's like this rotating piece of a 90 degree angle of this rectangular waveguide. Oh, that's super cool. Yeah. And some of it, like, um, the lower frequencies, like the two gigahertz stuff can be, oh, three inches by six inches. Holy crap. And then like the, uh, high stuff like 50 gigahertz might be, you know, that same in millimeters, three millimeters by six millimeters. So, uh, it's pretty interesting, but the high voltage was always a big challenge. Um, cause you're basically doing a switching power supply that has like 220 in and 10 kilovolts out. Lost a lot of good men out there. Yeah. We didn't lose anyone. That's good. But, um, uh, doing printed circuit boards that are floating at 10,000 volts is a pretty interesting, a lot of challenges. You know, you talk about creepage and clearance and stuff like that. This is, you know, measured in, um, inches and, uh, everything's potted, but then you've got all this heat, you know, maybe a kilowatt of heat sometimes that you've got to get out of this potting area. Wow. Do you do like heat, like heat guides too then? Or how did you get it out of the potting? Um, well, um, there were some ceramics that were relatively conductive, um, like alumina and beryllium oxide and other exotic ceramics. Um, and they can conduct heat and not, um, the voltage. Um, so we would do it that way. Um, but then sometimes you just need to get a really large heat sink. So we would use a heat pipes to spread it to five points and things like that. And just a ton of air. Yeah. Right. And so

**Bart Dring:** multi horsepower. When you first said satellite, I thought you meant it was going up in the

**Bart Dring:** satellite. I'm guessing this is all terrestrial stuff. Okay. So if you've ever seen, um, the trucks, news trucks with the big antennas on the back, we made a lot of stuff that went in there. Um, and so we did mundane stuff like, you know, the feed for the home shopping network. Not very exciting, but, uh, I thought there was money in it though. Yeah. Oh, the, yeah. These, you know, a little box the size of, uh, you know, uh, audio amplifier would sell for $50,000. Yeah. So, um, yeah, there was money in it. Um, but then we did, uh, deep space networks for, um, you know, deep space probes, things like that. Um, like someone to

**Bart Dring:** the actual, the deep space network, like the three antennas. Yes, exactly. Yeah. I've seen one. Yeah. I've been, I've been to one. Yeah. Canberra. Yeah, that's right. That was, that was,

**Bart Dring:** man, that place has like a football field that they can steer. Exactly. Did you get to go out there? No, I've seen the one in Pasadena though. Okay. Yeah. And I think there's one in Spain. Is that where the other one is? I think so. Yeah. Okay.

**Bart Dring:** I didn't know that there's one in Pasadena. I thought it was somewhere else. There is one. I don't know if it's part of the trial. I thought, yeah, I thought the third one was somewhere else, but maybe I'm wrong. Yeah. But yeah, I'm sure JPL has got a bunch of gear. I think so. Yeah.

**Bart Dring:** Um, and, uh, yeah, that was cool. And then, uh, we also did a lot of, um, military communication stuff. Sure. Um, right after, uh, 9-11, uh, you know, all those wars out in the desert, um, they, uh, had a lot of bandwidth requirements because suddenly, you know, uh, they were in the middle of nowhere and they were having, they want internet. They want internet. Yeah, sure. Yeah. Um, and they use X band and they were using up the satellite capabilities. So, um, they started leasing commercial satellites and that meant they had to have a whole new set of equipment. Got it. And, uh, so that was, uh, uh, a big market for us. And that was interesting because the ambient temperature we had to operate in was 60 C. Oh my God.

**Bart Dring:** It's a 140 F I think. Yeah. Right. Right. Cause you got the, it's 110 degrees outside, 100 or whatever it is. Oh, it's more than that. 30 C outside, but yeah. And then you got a blazing sun. Yep. Yep. And, uh, and you're inside a case then. And yeah.

**Bart Dring:** Oh my God. So, uh, that was a big challenge.

**Bart Dring:** Is that like changing to like silicon carbide and like really exotic materials or what had to change?

**Bart Dring:** Um, yeah, the, the materials you can work with are somewhat limited, you know, you get what you can. Um, but, uh, it was just, uh, increasing the cooling capabilities and, um, you know, increasing the airflow and stuff like that. Yeah. That's crazy. A lot of it was outdoor rated. So it was like on the back of a Humvee. Yeah. Right. Uh, and, uh, that was kind of crazy too, because like those television news gathering trucks, you know, as soon as there's a hurricane, they want to go down there and film it. So you have to be able to have your outdoor equipment just sitting out, you know, on the back of an antenna in hurricane conditions. So what is, uh, what are some things that you could

**Bart Dring:** teach our listening audience about, uh, designing for hurricane and or desert conditions?

**Bart Dring:** Yeah. I don't know. Start with $50,000 or more. Yeah. Well, the thing is, uh, the, uh, the military specs are all published and you can get those and they're really a good place to start with like for exotic environments, you know, let's say, you know, how much rain do I really need to deal with? And you can just look that up and find it. And then, um, you know, it'll tell you that maybe 90% of the, uh, activities are covered by like four inches an hour and 50 mile an hour wind. You know, you can start with that and then, uh, they have tests to find for you and labs set up to do it. So, uh, yeah, just, uh, design, test, iterate, pay money. It's right. Yeah. Yeah. Yeah. Lots of big, thick gaskets. Yeah. Yeah. That's, you know, you want something that's compliant, you know, that, that kind of bends and moves with the weather. Okay, cool. So then how did that,

**Bart Dring:** was that where you found all the, the, uh, the steppers or was it? Yeah. I think I stumbled

**Bart Dring:** across the stepper motors there and started playing with them and, uh, did the CNC machines.

**Bart Dring:** Mm. Um, and so like when you say CNC machines, can you define CNC machine?

**Bart Dring:** Uh, it's basically, uh, you know, computer controlled motion. Um, so anytime you're doing precise motion and multi-axis, that's what I consider CNC coordinated motion. Yeah. You know, so you got to go from X1, Y2 to X5, Y5 and, you know, within a perfectly straight line under, uh, really tight control. Yeah. So it's broad, you know, 3d printers, a CNC machine, um,

**Bart Dring:** Milling, right. We're both at M Hub right now. We're, there may be a milling machine that kicks on at some point and we will definitely hear it if that is the case. Cause they're also, they, they're allowed. And, uh, so John Saunders has also been on the show before, so I'll, I'll call that out too. So he's NYC CNC, same, same kind of things, I guess that he's, he's using it instead of building it, I'm guessing. Right.

**Bart Dring:** Doing the machining piece. Yeah. So like plasma cutters, you know, even pen plotters, Yeah. 3d printers. Yeah. Milling machines. But actually, yeah, I guess Nadia Peek's been

**Bart Dring:** on the show as well. And she does, she was doing the flexible, you see her, her stuff ever where she, like, she makes one axis either rotational or linear, and then she kind of glues them together in different manners and makes different tools. Yeah. I've seen some of her stuff. Yeah. Yeah.

**Bart Dring:** I mean, there's another old thing of robotics, which, um, you know, uh, is very, very similar and use a lot of the same equipment, but it might be a little different. You know, you're trying to get to a target, but you might not really care, you know, as long as it stays within an envelope that it gets there. So you could use vision, you know, to close the loop. But, uh, with CNC, you, you really have to precisely control every little aspect of it.

**Bart Dring:** Mm-hmm. Yeah. And so, okay. So that, and that, that's, that's probably good for talking about where we kind of are in the stack too, because it seems like, so like thinking about like a, a John Saunders, John is basically programming either in G code or some higher level, like cam or yeah, cam, right. The, the tool path, which generates G codes, uh, or then even above that would be like 3d CAD. But now you're talking about even getting down below to like steps and

**Bart Dring:** sending steps to individual. Yeah. In the beginning I was just using programs. There's like Mach 3 and Linux CNC, um, which are, we're basically using the parallel port of a PC.

**Bart Dring:** Mm-hmm. Um, to, you couldn't find computers that had parallel ports anymore.

**Bart Dring:** Yeah. Yeah. Right. Yeah. But back then they, they were everywhere. Yeah. I was using like four 86s and, uh, you know, they were pretty tightly coupled with that parallel port. And I think when they started abstracting a lot of stuff, that's when they lost that tight coupling, um, and parallel ports, uh, you know, you could get a USB parallel port, but it really wasn't the

**Bart Dring:** same old parallel port. Yeah. I had one for my old CNC machine and it, uh, it, that was the thing that crashed every time. Like if it was going to crash, it was going to crash at the USB to parallel.

**Bart Dring:** Yeah. They really weren't, you know, as deterministic as, uh, as the old, like hard wired parallel port, because I think, you know, you send it to USB and USB is like, yeah, okay. I'll get there when I get there. Yeah. Yeah. Uh, so, uh, that's what we were using for that. And, um, and then I got into doing, um, uh, instructables, uh, things. I can't remember how I got started with that. Um, but I did a series of instructables and I think I was making some toys for the kids and stuff like that. Uh, and, uh, then one of them, I can't remember what the topic was, but I made a human powered Segway. Okay. So basically a unicycle that looks like a Segway. It was kind of a lean forward, it goes forward kind of thing or what? No, it was completely human powered. There wasn't a piece of electronics on it. Okay. And it was, it was kind of a joke more than anything else, but it was getting all these votes as like to win this contest, which was a, uh, epilogue laser. Oh, okay. And I'm like, epilogue laser. That sounds great. You know, I'd love one of those. And, uh, so I was getting all my friends to vote for this thing. And, uh, then I looked as I was getting closer to the end, I started looking up, you know, the, the cost of one of these lasers and they were like 18 to $20,000. Mm-hmm. And I was like, holy crap. You know, I could have like a tax bill that would exceed what I even consider the value of this machine. Like if I went bought one at the store, You just bought parts even, right? Yeah. I, I like, if I could go to the store and buy one, I'd probably pay $2,000 for it back, back then. Sure. And then here, you know, this is an $18,000 thing. Yeah. Uh, so I started thinking, well, maybe I can make my own. Yeah. And, uh, So did you, did you win though? I mean, I didn't win. Nah. I didn't deserve to win. It's better if you win and then you're like, I don't want it. I don't want the tax bill. It was awesome though. But, uh, so, uh, that like got me started doing a laser cutter. Okay. And, uh, I started that website, buildlog.net and sort of like build log was, I was going to log the whole process and stuff like that. And, uh, it was really the first comprehensive open source laser. And, uh, that's kind of what I got initially known for. It was called the 2.x laser. And, uh, so then I started selling kits for those and probably sold about 400 kits, laser kits. Wow. Uh, so a lot of people, um, got them and, uh, it was pretty vibrant project. Um,

**Bart Dring:** So people kind of throwing in, throwing in some help and feedback.

**Bart Dring:** Yeah. And that, that was, I really kind of got hooked on that, uh, you know, like creating a community around something and, um, you know, you only have so much time, you know, people have all these great suggestions. You're like, yeah, okay, I'll put it on, uh, you know, The Sunday list. The road map. Yeah. And, uh, but then, you know, someone else on the forum would be like, hey, you know, I had a few minutes, I gave it a try and it really worked kind of cool. I tweaked it like this and, you know, let's, let's, uh, incorporate that into the thing. Um, but, uh, so I did, that was actually the second laser. That was the 2.x. The first one was clunky and made out of like a plywood frame and, uh, I was trying to really simplify it. And the last thing I needed to simplify and lower the cost was, uh, the linear bearings. Yeah. And, um, we were using aluminum extrusions with, um, glued on V rails. Okay. Could you explain what those things are? Um, well, it was like a rectangular cross section, uh, 20 by 40 millimeter, uh, you know, T-slot extrusion and then it did these metal, um, V's that you would glue on. And then, you know, the inverse shape of a wheel, a notched wheel would roll on it. Um, and, uh,

**Bart Dring:** So maybe like, what's a good, um, is there a good product that people could think of that might use these kinds of things?

**Bart Dring:** Make or slide. That's where I'm going. All right. So, uh, what I thought was, well, maybe I can get an extrusion with the thing built in. It's only plastic wheels running on, um, an aluminum extrusion. It can be all aluminum. So I did a Kickstarter for maker slide. And, um, this was back in the early, early days. This is probably like nine years ago. Mm-hmm. So early days of Kickstarter, early days of Kickstarter before there was ever a million dollar Kickstarter or anything like that. Uh, and I was asking for about five or 6,000, got about, I can't remember, maybe 25,000 and, uh, worked out great. Yeah. Um, and made the list.

**Bart Dring:** Which back then was not what people were saying either. Cause it was like a lot of people were starting Kickstarter with much knowledge of what they were doing. Yeah. And I was one of them and,

**Bart Dring:** uh, I learned a lot. Sure. But you also had manufacturing experience, you know what I mean? Yeah. Like that's the, I think the big difference. Right. And, um, yeah, one of the, the things that I learned is if you have a Kickstarter and you're looking for some money, plan for getting more money than you asked for, because you're basically saying, I'm going to work my butt off for these people that give me the money I need. And then I'll have this tool with this extrusion tool that I, you know, wanted. Um, but then, you know, well, if you get more money than the extrusion tool, what are you going to do with it? Um, you're basically working your ass off 4X more than you expected. Right. Right. And, um, so, you know, you, uh, that's something to plan for, plan for too much success. You know, you might've thought that this is a product launching another product. And, uh, so that was a bit of work, um, getting all that stuff out. So what'd you have to do to actually get

**Bart Dring:** Baker slide out? So like, basically you were then sourcing, you basically approached extrusion houses or something like that. And what does maker slide like look like then too?

**Bart Dring:** Baker slide looks like, uh, um, and I'm sure you'll put a link to the Kickstarter. Yeah. Um, it looks like a rectangular extrusion with two of the, uh, adjacent corners having little points on them. Okay. And, um, those points are what the wheels roll on. It's a little like half triangle, well, no triangles, like half diamonds and the wheels roll on those. Um, and it's since been extended, it was one of the first, uh, linear extrusions out there, but now there's like open builds and stuff like that. And, um, they've got a lot of different ways of doing it. They actually did the negative of what I did. They made the, um, the V's go into the extrusion, whereas I had them projecting out. And, um, there's a lot of merit to that because the, the V's that I have are very prone to damage, whereas they haven't protected in a pocket, but now there's a lot of extrusions out there. And the interesting thing about the Kickstarter, it was re kickstarted and Indiegogo because it was open source about five times around the world. Really? So I don't know if that's ever happened before, but, um, there was Australia, the UK, um, all sorts of things where these different Kickstarters and Indiegogos.

**Bart Dring:** So they basically took your files and they're like, I'm going to just do another run of this kind of.

**Bart Dring:** Yeah. Exactly. Yeah. And now you can buy it natively in probably, probably eight to 10 tools around the world where you can buy it.

**Bart Dring:** Wow. That's great. So it's, it's kind of like a viral idea, but kind of actually replicated and manufactured. Yeah. Yeah. True open source idea. You didn't, you let it go to the wild and it's made into things.

**Bart Dring:** Yeah. And, um, what was happening was I was still working 40 hours a week. Um, but I would basically come home and I had these lasers, which I really enjoyed filling the orders for, but now I had maker slide. And, um, so I would buy it. Um, so I would, I got a, uh, company in Michigan to make the tool and, um, they make it. And I think you have to do about a thousand pounds minimum.

**Bart Dring:** So it's a weird, like that sounds very arbitrary, but it, it makes sense probably from a material and cost perspective.

**Bart Dring:** Yeah. There's a lot of waste because they have to, um, push it through the tool and tune it and things like that. And they use these giant billets of aluminum. And so it's a really cool process. Oh yeah. Yeah. It looks like a locomotive with, you know, you know, it's so hot. You can't even approach it, approach this machine. Yeah. And, uh, I was thinking like Play-Doh, but like hot molten metal Play-Doh. Yeah. But it really never like looks liquid. It is kind of like Play-Doh. It, it, it, you can see a little discoloration. Aluminum doesn't get red when it gets hot. Sure. Yeah. And so you really don't notice anything other than you just kind of see it sliding out and it goes along these long tables, uh, really long, like, um, 300 meters long.

**Bart Dring:** Yeah. Whoa.

**Bart Dring:** Really? Wow. And like a whole factory almost then. A whole factory. Yeah. A long factory.

**Bart Dring:** Wow. How do they, they cut it up later? Like what do they do?

**Bart Dring:** Yeah. They cut it up later, but what they, it, when they first push it out, um, there's like a wiggly end bit, you know, and then it goes out and then as it's going down this table, it gets some slight distortions on it and then they want to stretch it, um, to get it straight again. And then they cut it and where they cut it, you know, they kind of bend it a little. So there's a little waste at either end, but that stretching process gets it really straight. Um, and then, uh, they have this table that kind of pushes it off to the side and another piece comes out and then they cut it and they'll cut it to any length you want. Right. Um, but they charge for cutting. Sure. And, um, but like, what is the, so that first piece

**Bart Dring:** after they stretch, like how long is that? Is that like a hundred meters long still?

**Bart Dring:** Yeah. They don't really stretch much length out of it. They're just sort of like, if it's got a, um, uh, you know, if it's got a little bit of a wiggle to it, they're just kind of pulling the wiggle out cause they want it as straight as possible. Uh, so, uh, then, um, but the service I was offering was cut to length. So you say, you know, you're building this laser and you want, uh, a 400 millimeter piece and two, 200 millimeter pieces. I would deliver those to you. So I didn't know what size to order because people were just ordering random sizes. Sure. Sure. Uh, so I ordered the longest piece I could handle, which was 20 feet long. It delivered to your house 20 feet long. Oh, I went and picked it up. Oh my God. In a rented, uh, Ryder van, um, and, uh, drove it home and loaded into my garage and I created a cutting operation there. Oh, wow. Um, which was interesting because to get the best yield, I use some yield software, which basically takes all your orders and puts them into, uh, an optimizer, an optimizer. Yeah. And this was like a one dimensional optimizers. There's 2d and probably 3d,

**Bart Dring:** like for packing a truck optimizers. Sure. Well, uh, Oshpark when Lane was on back, back in the day, he always talked about building an optimizer for, yeah, it's like nesting like

**Bart Dring:** of parts and stuff like that. Um, and it was pretty interesting. So I had like a web store that would take the orders in and then the more orders you process at once, the more optimization you can get. Yeah. Um, and, uh, so it'd print these labels out in, I, you know, totally automated. So it'd print these labels and in order of my cuts, I would cut, stick the label and the label would have the length and who it went to. So I might need to cut 10 or 12 of these 20 foot pieces. And it's actually really easy to cut. You just use a aluminum chop saw. Uh, and, uh, then it might take 12 pieces before one order got filled. So that'd be stacking in these little stacks around the room. Yeah. And then, um, I would, and it would say, you know, one of whatever. So then I would know when one order was filled and then I would ship it off. Uh, but it was literally taking me probably about 25 to 30 hours a week on top of a, Oh my God. Of a management of engineering. Yeah. Right, right, right. Um, so, uh, I was eventually getting kind of burned out and I didn't know what I was going to do. Yeah. Um, and, uh, that's when I approached Inventables to, um, I said, why don't you guys fulfill it for me? And Zach Kaplan, the CEO who I'd known for a while, um, jumped at the opportunity and, uh, said, okay, yeah, we'll fulfill it for you. He was going to do it in a different way. He was just going to get, you know, stock standard pieces, standard links. Cause it really is pretty easy. Yeah. It was a smart move on his part. Um, and, uh, so, uh, you know, that then he started paying me a royalty, um, which was, um, a real success because here it is a fully open source product that anybody could actually use on their own. But Inventables was like, no, we're happy to pay you a royalty, you know, to help us set this up and stuff like that. That's great. And they still pay that royalty. That's great. It's, you know, going on like eight years now. Yeah. Um, cause it's used on the

**Bart Dring:** X-Carve. Okay. Right. And which I'm sure we'll get to as well here. Yeah. Yeah. So, so what is

**Bart Dring:** Inventables for people who don't know? Inventables is a like desktop, uh, 3d carver company. They make, um, the Carvey and the X-Carve. They did the Shapeoko when that first came out. So that's their whole business is just these 3d carvers and all the materials to support that. They also have, um, an online cam program called easel. Yeah. Which, uh, is very popular and, uh, it's great, especially if you're just getting into, um, super simple, super simple and you know, they've got a big team that works on it and, um, you know, it's, it's very quickly catching up to more high, higher power cam. Yeah. It's like a bottom up kind of innovation thing. Yeah. And it's really easy. It's kind of live, you know, you drop a circle on one side and you see your piece of wood suddenly have a circle cut out of it on the other side. So it's really quick, quick feedback like that. Um, and it's more, the way of thinking is not like CAD. It's more like, um, uh, illustrator. Okay. Yeah. Where, you know, instead of like filleting and things like that, you could just move a circle onto a corner, you know, and subtract and stuff like that. So I think a lot of artistic people have, um,

**Bart Dring:** uh, a shorter learning curve. Yeah. That's good. It's interesting too. Cause I feel like tools like that as they move along, that ends up impacting future CAD innovations, right? So like Autodesk in 10, 20 years, right. When people that started in elementary school, potentially using easel, right, they're going to be like, oh, well, all of our users expect this instant feedback type thing. And obviously some of them are gonna learn parametric, but some of them are gonna ask for these features and it'll just eventually start to kind of impact how, how, um, features are

**Bart Dring:** developed. Right. And, um, you know, like their native import is SVG, which is like so far away from the CAD world. Like, you know, yes, I do know this. Like I have, you know, I use a CREO or pro engineer, which has exports like 80 different formats, you know, 2d and 3d and none of them are SVG, you know, but you know, it was, it was a smart move because it's really, you know, the language of artists, right? Right. They don't know what a DXF is or, you know, uh, you know, things like that. So, uh, you know, that's kind of where it's focused. Um, but the way I met Zach was, uh, originally Inventables was selling a lot of materials to laser cutter people and they would give like epilogue, these kits of little samples that people could use. So he reached out to me and he says, yeah, I was looking for, you know, the number one open source laser out there and was surprised to find, you know, it's just two, three miles from our office. Chicago. Chicago. Chicago. Yeah. And, uh, so, you know, he was like, you know, he actually gave me some of these kits and gift certificates for people to get started and things like that. Yeah. And, um, so it was struck up a friendship with him and, uh, you know, one thing led to another and the company I was working for was going through a sale to a competitor. I wasn't really that interested in moving, you know, working for this competitor. And I had this open offer from Zach. Um, so I joined Inventables, um, and that was about seven years ago.

**Bart Dring:** Right. And it dovetailed nicely with your already interest in all the other CNCE things anyway.

**Bart Dring:** So, yeah. So at the same time that, uh, they took on Makerslide, they took on the Shapeoko through Edward Ford. Um, and he, he did the original Shapeoko and he worked there before I did for a while. Um, so as I was coming on, they, uh, they had already got a little start, but they were looking, you know, to, uh, uh, a little more focused. So I came on as, um, I think my title was director of product. Um, but I was basically the engineering director and stuff like that. Yeah. Guy who builds things. Guy who builds things.

**Bart Dring:** Guy who tells other people how to build things too.

**Bart Dring:** Yeah. And, uh, but it's a fun company to work for. I mean, everybody there is so enthusiastic. Mm-hmm. You know, and, uh, it's not like, you know, it's taking me back to the, the Williams days. Yeah. You know, where it's just fun, you know, interactions in the hall and everybody's excited about everything and hangs out afterwards and plays with the equipment. Mm-hmm. Yeah. So, uh, that was, that was, it was real fun to work there. Yeah. So, uh, what, what are the three?

**Bart Dring:** So there's the, you said the Carvey, the Shapeoko, and then the... X-Carve. X-Carve. So what are the differences between them?

**Bart Dring:** The Shapeoko, um, was, uh, the very first, um, machine made out of Makerslide. Okay. Um, and Edward Ford did a Kickstarter on it at the same time. Uh, he really, his Kickstarter was more like, I want to make an affordable CNC machine, give me some money and I'll figure it out. Oh, wow. Okay. And, um... Real open. Real open. And, um, but he, it resonated with a lot of people. Yeah. Yeah. And he was funded and stuff like that, but halfway through the Kickstarter, he's like trying to figure it out, you know, as the money's coming in. And I had my Kickstarter going on at the same time. Mm-hmm. And he's like, hey, that's exactly what I need to make this thing work. That's a good idea. And he's like, do you mind if I take it and make a router out of it? And, um, a CNC router. And I said, no, no problem. So, uh, that's how the Shapeoko got started. Mm-hmm. Got it. Um, and then, uh, he eventually left Inventables to do a new version of the Shapeoko on his own. Mm-hmm. So we needed to quickly change the Shapeoko to differentiate ourselves. So we did the, um, X-Carve. Mm-hmm. Got it. And, um, just, uh, sort of beefed it up in a lot of areas. And, um, we made it, uh, for sale with a configurator. So you could sort of buy it with all these different options. We vastly improved the electronics. Mm-hmm. Um, and really beefed up the power of it. Mm-hmm. Um, and made it look a little cleaner with the black look and stuff.

**Bart Dring:** Right. And so in both cases, they're like, so it's like an H format, right? So like rails on. Yeah. There's like cores on, if we're the same vertical rails, and then there's like a center, the H piece is like across. And then. Yeah, we call that the gantry. Gantry. That's the word. Thanks, Bart. You know your stuff.

**Bart Dring:** You should get into this. Gantry is like supported on either end and has, um, you know, a moving carriage on it. And, um, it's, uh, it's an easy way to get a stiff machine, um, out of like low cost components. A lot of 3D pinners are that way. Yeah. Um, and a lot of milling machines and even the, um, like the ShopBot is that way. Sure. Yeah. Which is ShopBot is a pro level, um, machine.

**Bart Dring:** Some people don't like the ShopBot software I've heard. So.

**Bart Dring:** Yeah. But I mean, companies buy it.

**Bart Dring:** Yeah. It's big too. And that's the other thing. And so the rigidity matters because you're now spinning a bit and you're pushing it through material. It's milling effectively, right? So you've got that horizontal force. You need it to, to know where it is in 3D space.

**Bart Dring:** Yeah. And you don't, um, you don't want the machine to bend, you know, and, um, you know, flex, things like that. Um, but it's still an entry level machine, you know, it's, uh, made for people to put together on their own and experiment with. Mm-hmm. Cool. Okay. So what are the electronics that drive in that kind of thing? Um, well, uh, there's a, uh, software program that runs on an Arduino called Gerbil. Mm-hmm. Gerbil, garble, gerbil. G-R-B-L is the acronym. I've got it on good authority that it's pronounced every one of those ways. Oh, okay. Like, uh, Kaika. Yeah, exactly. Yeah. Um, and I call it gerbil. And, uh.

**Bart Dring:** People say garble, really?

**Bart Dring:** Garble. Yeah. Garble, gerbil. Yeah. Like I said.

**Bart Dring:** Seems like that's a little more negative connotation.

**Bart Dring:** Yeah. Like I said, I call it gerbil. Yeah. I'll probably call it three different ones throughout this, uh, talk. Yeah. Um, which is, um, was, uh, written by a guy in Europe and, um, he is basically was trying to put a CNC controller onto the Arduino. It was kind of like putting a ship in a bottle. That was his analogy. Okay. Yeah. And like, you know, you can't do this on an 8-bit, uh, 16 megahertz thing. And, and, and he did it and did a good job of it. Um, and then it was picked up by another guy, um, by the name of Sonny, who took it much further, put like a higher level motion planner and stuff like that. And, um, it's, it's really high quality, uh, motion planner on an Arduino. And just about all the rep wrap, Marlin, Repetier and stuff like that took its original motion control from Gerbil.

**Bart Dring:** Oh, interesting. Okay. Um, so these are the firmwares that are written more for 3D printers, but you're saying that like the, the bones of it are.

**Bart Dring:** The bones of it that like, you know, can I get from here to there in a clean and efficient way?

**Bart Dring:** Um, is it written is because you need to have a lot more math functions in there? Like what is, I don't, I don't, I don't know anything about it. So what are the hard parts about doing like a motion controller like this you're talking about?

**Bart Dring:** Um, well it's, um, yeah, it's a lot of math. Um, but like doing a straight line, um, from point A to point B, you have to, um, accelerate, um, and then, um, go to a constant speed and then decelerate. Um, but if you're doing that in three axes with three different motors and each motor might have different, um, max speeds and max accelerations, coordinating that. Um, and then, um, so that's one thing, which really isn't that hard of a problem to solve. But, um, if, if at the end of that line, you're now going to take like a 15 degree angle off of that. Okay. Um, you come into that corner, coming to a complete hard stop and then restarting is, you know, the basic way you would do it. But let's say you're doing, um, a circle. Sure. Things get a lot more complicated. Right. And a lot of these are actually breaking it down into little line segments and doing a motion plan that allows it to not come to that complete stop. And so it's, it's whipping around the circle. It looks like it's just cruising. Um, and it's very accurate. I mean, it's like hundreds of a millimeter accurate that it's breaking it down into. But, um, that's where the big math comes in. Got it. Um, and.

**Bart Dring:** Sines and cosines, huh?

**Bart Dring:** Yeah. Well, you want to, you know, you want to avoid, um, as much floating point math. Sure. And as much canned libraries and things like that. Um, so.

**Bart Dring:** So it's like all lookup tables and stuff like that or.

**Bart Dring:** No, it's just avoiding a lot of that stuff. Okay. Um, and, and, you know, uh, hard coding some stuff and a lot of register level access. You know, there's not, um, digital right, you know, 10 11 high. Right. It's more, you know, poke it right here. Uh huh. You know, add a byte at a time so that you're doing three axis writing at a time and stuff like that. Um, so you're, you're, you're pushing a byte into register that's now handling three, eight outputs, you know. Oh really? Wow. Um, so, uh, that, uh, that's how it's optimized. Um, but they, uh, originally had to do it through, you know, compilers and things like that. Um, but then, uh, they cleaned it up so that it could be compiled right out of the Arduino IDE. Um, so, you know, it, it's, it's pretty accessible that way.

**Bart Dring:** Yeah. So why did it stay? Like it, so it sounds like it was started as like a challenge to get to the something efficient, but why, why did it keep doing that when there was obviously other, it was it just because it was, it was accessible to anyone because of low cost or?

**Bart Dring:** Yeah. Well, so when people were starting to get away from, uh, the Mach three and the Linux CNC and looking for a cheap alternative, you don't want to run Linux CNC and your 3d printer. Yeah. Um, and what accessible hardware is out there? It was the Arduinos and the, um, uh, and the Arduino mega, you know, the, uh, the basic Uno was what was running most, uh, three access CNC and the Megas. I don't know if you've heard of like ramps controllers. Yeah. Yeah. Yep. Um, you know, that's, uh, yeah.

**Bart Dring:** So it's got like 1284 on it or something like that. Right. The mega is a mega 20, 1284. I don't know.

**Bart Dring:** Uh, 26, uh, 50, 25, 60. Yeah. Something like that. Yeah. Yeah. Uh, the mega. Okay. And, uh, so, uh, yeah, that that's, you know, and. Okay.

**Bart Dring:** So it was just to make it low cost and, and widely super low cost.

**Bart Dring:** Yeah. And, um, so that, um, back to like what's in the X controller, um, which is the, the, um, uh, controller for the X carve. Um, it's got that as the, um, sort of the motion planner and then it's got stepper drivers and things like that. And a lot of people use these plug-in stepper drivers that you've seen on rep wraps and things like that, um, which are like, you know, dual eight pin rows and they're available from like Polo Lu and China and stuff. We use, uh, some higher power ones that could do like, um, four and a half amps per motor. Um, and they also did some current control so that when the motors idle, the current drops so the motors don't overheat.

**Bart Dring:** That's good.

**Bart Dring:** Um, so that, that's basically it. I mean, we tweaked Gerbil a little here and there, um, but, uh, you know, that's what it is. You just beefed up Gerbil.

**Bart Dring:** Okay. Yeah, that's good. That's good. Okay. And I mean, so like for someone that's getting started, I hear the sound of, I hear the sound of CNC in the background. Uh, so someone is getting started into motion control. Like, is it something that they need to consider? Like, is, is it like, so if someone's listening right now, they're like, oh, what Bart's saying is interesting. Like, should they, should they feel like they ever need to dig into Gerbil or is it more, are they going to be operating at a higher level, higher level at the beginning?

**Bart Dring:** You can operate at a higher level, um, just through, um, you know, a sender, which is like sending the G code to, um, Gerbil. Cause you know, the, an Uno has very limited RAM. So you're not like, you don't load your job onto the Uno. You're sending it a move at a time and it's buffering them. Got it.

**Bart Dring:** Um, but breaking that out into the actual steps you're saying. Yeah.

**Bart Dring:** So it can like load like 12 moves at a time and then smooth those moves. And as, as one is, is, is, is finishing up, it's loading a new one and replanning and things like that. But you need something to stream the code there. Got it. And that streamer can, um, isolate you from what's going on in Gerbil. And then it, you know, a lot of them look a lot like, um, Mach 3 and Linux CNC.

**Bart Dring:** Okay.

**Bart Dring:** Uh, so you don't need to know that, but, um, you can also treat it just as like a general motion coprocessor. So if you're trying to do something totally different than CNC, you just want to, um, you know, move a pen along the wall or something like that for doing, um, you know, generative art or something like that. And you're like, okay, I can do all this front end stuff, but I, how do I get the pen to move? You can just almost treat it like a black box. And a lot of people do that.

**Bart Dring:** Um, so like what would they then pass? Like what's the example high level command they would pass then? Is it basically like XY?

**Bart Dring:** Um, yeah, so there's, it's, it's called G code and, um, like a typical move is like G zero, which means, um, move, uh, in rapid speeds. Uh, and then you give a point to where you want to go. So it's not from here to there. It's like, you already know where you are. And so it'd be like G zero X 10 Y 10, which would move to those coordinates. Um, and then the next move would be off of that. And if you want to move at a specific speed, it's like G one, same X 10 Y 10, and then feed 100. So it'd be 100 units per minute. Got it. Could be millimeters, could be inches. So that's, that's pretty simple. Abstraction.

**Bart Dring:** A little cryptic, but yeah.

**Bart Dring:** A little cryptic, but it's pretty abstract from all this other mess going on behind the scenes of coordinating three axes and stuff like that. So, you know, you could write out, um, by hand on a single sheet of paper, all the codes you need to know. Okay. So it's not, uh, you know, that cryptic. Okay. Yeah. I mean, it's cryptic, but not that. Yeah. Yeah. Okay. It's a, yeah. It's not like a programming language or anything like that. Right.

**Bart Dring:** Okay. Yeah. And I think the other thing too, it's good is to, to walk people like up and down the stack. That always kind of helps me at least is like understanding like, okay, so if I start in SketchUp or Fusion 360 or Blender or whatever, that is a 3d model that's on my screen. And then from there, that's either going to go into like a slicer or a, uh, what's it? Cam tool. That's CAD. And it goes into a cam tool, like a slicer or a motion control type of thing is then that's pushing G code out. Right. Yeah. And that would then go down to a controller. Hopefully that it can. Which executes the motion. Uh-huh. Hopefully everything gets done. Right. Um, but then the, the G code then gets translated into basically step, step, step, step, step, step, step.

**Bart Dring:** Yeah, exactly. Okay. So that's the full stack pretty much. That's the full stack. Now there's programs like a fusion 360, which are, and ESL, which are breaking down that stack to look to less steps. You don't even see some of the, um, transitions of going from my art to my, uh, G code. You're just going from what looks like your art straight to sending. Um, but in the background somewhere is back in the background. All those steps are, are, are happening.

**Bart Dring:** Yeah. Okay. That makes sense. That makes sense. Um, so you then have taken Gerbil and you've put it on a different processor, right?

**Bart Dring:** Yes. I've done that a couple of times. Um, and the first time I did it, I did it on the, uh, PSOC five.

**Bart Dring:** Oh, okay.

**Bart Dring:** Uh, and, um, that, um, that, um, that was so easy. I think I did it in three days. I think I did it in three days. Wow. And, um, why, why PSOC five? Uh, I love the PSOC five. Uh, I love the PSOC five. Um, it's, uh, I don't know if you've ever used it. Um, I've, I've not. It's, uh, I've heard you talk about it a lot. I've heard you talk about it a lot, I think, and other people.

**Bart Dring:** Um, it feels like people that are into it are like really into it.

**Bart Dring:** It's got a great IDE where, um, you visually map out all the peripherals and you can sort of create peripherals on the fly and stuff like that. You know, you started drawing out of pool of resources, creating these different peripherals. Um, so if you want, uh, an interrupt to, um, uh, you know, toggle a pin, you can do that in all in hardware, kind of FPGA like. Um, but it, so what you're doing in Gerbil is you have these interrupts, you've got, um, all these pins doing different things. Like when you send a pulse to a stepper motor driver, it has to be a very specific shape. It might have to have a, uh, a direction first, then a short delay, then a pulse length and stuff like that. That eats up a lot of resources on things like the Arduino and stuff like that. You can just create those pulse shapes right in the, um, so, and also you can do that. You kind of like, what's the code for, um, an interrupt. You just drag an interrupt out on the screen and say, generate an API for that interrupt. I've just pulled out. So it's really, really quick, um, to, um, get up to speed on the, um, hardware. There's no looking up data. Data sheets. It's like that. Yeah. And then if you are, if you do need to know, yeah. If you do need to know like some of the deeper stuff, you just kind of like right click on that thing and it brings up the data sheet.

**Bart Dring:** Got it.

**Bart Dring:** Um, and there's a data sheet for each peripheral, not like this, you know, 1200 page, um, data sheet of everything. Um, so I, I've, I've always used it for prototyping because if you have like, um, ADCs and DTAs and all this stuff, um, you know, you got this breadboard full of all these things in this, you, you, you're breadboarding on the screen, but it's a very expensive chip for a hobbyist. It's like $15 and it's a complicated thing. Um, so I usually prototyped on it and then switched over to real hardware that I could afford in, in quantity. But, uh, so, uh, I ported it to that and it worked great. It was so easy to use and things like that.

**Bart Dring:** Um, so what about the porting process too? Because like, like what, so Gerbil's written just regular code. You said it wasn't, it wasn't compiled anymore. So it wasn't, it was still like Arduino accessible type stuff. So like, like what, what kind of functions do you need to actually move over though?

**Bart Dring:** Like, um, well it's, it's all written in C. So you're working in C in both areas. So like if, like the motion planner, it is almost drag and drop. Um, and, uh, but, um, you can do some optimization because you are working in eight bits versus 32 bits on the, um, PSoC five now. So like, oh, you know, some of the math gyrations are going through. You might be able to simplify some of that. Um, but I worked from the outside in, I needed all these peripherals and I said, okay, I need, you know, three timers. I needed a PWM and, and some of these, um, you know, other interrupt and, and, and pulse, uh, gyrations I had to do. So I got all those, made sure those things worked. And then it was very easy to plug in the rest of, uh, Gerbil. Okay. So it was really, really pretty easy. That's great. Um, but, uh, I didn't get a lot of traction with that project. Um, put it on GitHub. A lot of people were interested, but without any real hardware for anyone to operate it on, it, it really never took off. And, um, then when I started making these smaller devices and putting Bluetooth on them, the PSoC five didn't have Bluetooth. It didn't have wifi. So I'm adding more modules. It's getting more complicated. Um, and that's about the time the ESP 32 came on. And, uh, that seemed like the dream chip for me because it was cheap, super tiny, and had all these radios on it that I could use.

**Bart Dring:** Um, why did you want those? Just for easy access to the thing?

**Bart Dring:** Well, at this point, um, uh, I'd left Inventables, retired. Mm-hmm. Didn't get to that earlier. Blah, blah, blah. Yeah, done with, done with, uh, professional robots. Now I do the consulting and some sales and stuff like that. But, uh, so, uh, I'm self-funded on all these little projects I want to do. And so I'm just tiny, tiny scale and, you know, trying to bring my whole CNC machine to Hardware Happy Hour. Mm-hmm. Yep. So, uh, that's when I wanted to go really small and I did not want to bring a laptop that I would also have to power up and find a plug for and stuff like that. Right. So that if I could just run it off my phone, um, then, um, that would, uh, facilitate these small scale machines. What's the point of a machine that could fit in the palm of your hand if you also need a laptop to run it? Right. Um, so, uh, that's why I started putting Bluetooth on a lot of things. And, uh.

**Bart Dring:** Right. And you started bringing things like the, the little, uh, the Nickelbot and the. Nickelbot, um. The coaster coaster. Yeah. The laser coaster cutter. Things like that. People have probably seen me posting tweets about them incredulously every time. I'm like, look at this thing that Bart brought to another meetup. Makes us all look bad, but it's also awesome. So. Yeah.

**Bart Dring:** There was a lot of pressure. I had to come up with something every month, but, uh, that was the, the impetus for doing the, um, ESP 32 stuff. And, um, but that's a completely different animal than anything I've ever worked on before. When I first jumped into it, um, the documentation wasn't great. Um, they were just bringing it into the, uh, Arduino IDE. Yep. Um. That's right. Angus who was doing that stuff. Yeah. Yeah. And, um, that made it attractive because I've still, you know, wanted to overcome the problem with PSOC, which was people were intimidated to work with it. Um. So to make a community around it. Make a community around it. Um, so it was really important for me to use the Arduino IDE. Uh, and the documentation that was out there was really at the IDE level as if you were like, you know, doing, uh, Arduino blinkies and stuff like that. Sure. Um, so, uh, it was a lot harder, um, for me to port it over. Um, because at this point I'm dealing with multiple cores, RTOS, um, and all this other stuff. So, um, and some of the things that aren't documented are what works in interrupts, what works in the RTOS, what doesn't, uh, the API, um, has, you know, the, uh, public functions defined, but what's going on behind the scenes. Um, right.

**Bart Dring:** So how much, how much did you have to use that stuff? Were you only using APIs or did you have to dig down deeper?

**Bart Dring:** Um, so my, my plan was to use, uh, the primary core that the IDE uses for the Gerbil stuff and then reserve the, um, other core for the wifi and Bluetooth stuff. Yeah. Um, because if you're refreshing web pages from your phone and stuff like that, I did not want that to wreak havoc with the, um, step generation. Right.

**Bart Dring:** Exactly.

**Bart Dring:** It's like halfway through a step. It's like, no, wait, hold on, hold on. Got to do a post. Got to do a get, you know. I was actually doing that. Yeah. It was actually well behaved and everything was coordinated, but it would like, you know, stutter and stuff like that, you know, when I wasn't getting it right. High network traffic. So you could tell real easy. Yeah. Yeah. And, um, so, uh, so by using the one core and avoiding the RTOS for Gerbil, I was using, um, just a primary thread and interrupts. Um, and, um, but the API is very RTOS friendly.

**Bart Dring:** Um, they expect you're going to be using it.

**Bart Dring:** They expect you're, they expect to be dealing with the problems of someone using the RTOS. Yeah. I hope I'm getting all this right. Yeah. But, uh, so, um, when you crack open the API and look at it, you're like, there's all these, um, uh, uh, mutex or whatever you say. Yeah. I said mutex, but yeah. Um, and, uh, things like.

**Bart Dring:** And like mailboxes and all that stuff.

**Bart Dring:** Yeah.

**Bart Dring:** Like everything stop, do this, everything start. And you're like, no, that's, that's not going to work for me.

**Bart Dring:** Right. You want to basically just a straight ahead microcontroller level type of thing.

**Bart Dring:** No. And, and with not having a lot of experience with RTOSes, I'm sure I could have done a better job with the RTOS. Um, but even though I had some help with it, it just wasn't producing what I wanted. Yeah. Um, and, uh, so I worked on it for about two months and kind of shelled it for a while. Went to a super con a couple, uh, years ago, ran into all the, uh, ESP 32 guys like, uh, you ruined. Yeah. And he got me excited about it again. So I gave it another shot.

**Bart Dring:** And, uh, he gets everybody excited about it. Like that guy is just, he's just an exciting person. You know, he's just, he does some crazy stuff. Yeah. I think he's got access to a lower level documentation. Yeah. Definitely. Well, he works there.

**Bart Dring:** So, you know, he talks to the people down the office, you know? Uh, so, um, yeah, that's when I decided like to, to really, you know, uh, double down on it. And then it took me about another two months to do it. And, um, part-time here and there. Yeah. And, uh, but, uh.

**Bart Dring:** Well, it's interesting too. Cause it, so you're talking about this thing that's running. It's got 12, you'd throw 12 step commands. I think I'm saying that right. Mm-hmm. I'm going to get a 328 style one or mega even, but like, so then what was the, what was the difference in terms of productivity of like now, now it's running an ESP 32 on a single core. Is it like you can do anything with it? Is it like way better or is it just kind of the same and similar?

**Bart Dring:** It's hard to quantify that because I mean, if you add up the numbers, it seems like it would be huge. Sure. Like you've got eight bits versus 32 bits.

**Bart Dring:** 4X. Yeah. I don't know how that math actually works, but you know, I mean, especially when you're trying to do a 32 bit, um, math. Yeah. Um, you know, it's hugely more efficient. Um, it's also got, uh, FPU on there.

**Bart Dring:** Okay.

**Bart Dring:** Um, and, uh, it, uh, has two cores, you know, and the Arduino is running at 16 megahertz. Those cores are running at 240. Yeah.

**Bart Dring:** You know, so like if you start multiplying, it feels like just some horsepower differences, right?

**Bart Dring:** But yeah. Um, so, uh, yeah, it's, it's, it's much, much faster. And then the Ram, the Ram is much, much higher. Um, so, um, you know, these 12 commands that you can put in the planner, I don't know how many, I mean, I, I ramped it up to a hundred, you know, and, um, it just, at that point, it just seems kind of silly to go any further. Um, so yeah. At a certain point you're not even streaming anymore.

**Bart Dring:** You're just storing it.

**Bart Dring:** Yeah. Right. Um, so you're, um, uh, buffering up that much more, you know? Um, so yeah, so it's running, um, so the, the basic step generation, an Arduino Uno or mega is probably gonna max out at about 30 kilohertz. And, um, after that, your, um, uh, your interrupt is almost gonna start stepping on itself, you know, because the, the, the, the divisions, you know, are running out of space there. Uh, now we have the, um, I say we, cause a couple of people helped me out, uh, it running at, uh, 120 kilohertz. So it's 4x faster on the step generation. And at that point, even if you're like 32x micro stepping and stuff like that, stepper motors just don't go that fast.

**Bart Dring:** Sure. Right. There's just physical world limitations. You're saying. Yeah.

**Bart Dring:** Um, you know, when you're running a motor that fast, that the, um, the power starts dropping off on a stepper motor with high step rates. And so then it just runs out of power and just can't keep up. So we really haven't pushed it further than that. Okay. Um, probably could.

**Bart Dring:** Sure. But at this point, who cares, right? I mean, you're, you're, you're at the point where you're, you want to put other functions in it or you have this tool now that feels like you're developing with it.

**Bart Dring:** Right. So that, that was finished in about September of 2018. And so that's been very stable since then. Um, and, uh, you know, demonstrated on a lot of machines, um, started developing. Some, uh, controller boards that people can use it on. I saw those on Tindy and some OEM sales of them with, you know, people putting them in various things. And, uh, which is crazy.

**Bart Dring:** I mean, like you now have an ESP 32, what, like one of those little ESP 32 breakup boards were like six bucks, seven bucks. I mean, they're cheap. Yeah.

**Bart Dring:** I mean, the Amazon price is about 10. Sure. And the, uh, AliExpress price is as low as four. Right.

**Bart Dring:** But if you even just bought a module, you could buy a module for three, you know? And so you could also design into a product if you wanted to. Yeah. I mean, you could buy the module cheaper than that, I think. Yeah. But the accessibility is, is pretty high. That's the thing I was getting at is that like, okay, now you can have motion control without the steppers at least for pretty cheap. And now you're building, you're building robots that are without the steppers themselves now, or what, like 25, 30, what are you selling on four on Tindy for like your controllers now? About $40. Okay. So $40, right. Yeah. Versus 20 years ago, what would that have been?

**Bart Dring:** I don't know. You know? Right. Yeah. It would probably, it cost $150 to $200 or something like that or more. And it wouldn't be as sophisticated. Right. Or accessible. Yeah. So since then, I've been working with some people and we put a complete web UI onto it. So now the sender that, you know, I was talking about how you interface is now a web page. So you run it in your browser that is served from the ESP32 itself. So it's basically just completely collapsed that whole end of the tool chain into on chip. So what would you, what would you put onto the web page then? So the web page is like jogging controls, like a command terminal is on there. The whole, like, I want to change my max speed. You used to have to go to a terminal and type, you know, $3 equal, you know, 1000. But now it's buttons and sliders. Now it's buttons with descriptions and things like that. And, you know, it's giving you a DROs, digital readouts of your position.

**Bart Dring:** Has Mach 3 come for your head yet? Or, I mean, they're charging, what, $600 for whatever that 20 or 5-year-old software is? Yeah. I don't know. But that's like what it would be replacing kind of, right? I mean, like Mach 3 was that software level kind of stuff. Yeah.

**Bart Dring:** It's more replacing the senders because Mach 3 is, you know, it's the step generation. It's all that stuff. And it's, you know, it's a lot deeper than that. Like, even Linux CNC is way, way deeper than that. That's what, like, the Tormach and stuff like that is running on, which is a commercial CNC. I think that's what we actually heard before. It was a Tormach, a PNC 1100, yeah. And so, and the other thing is now there's SD card interface. It's kind of standard on all these cards. So you just, like, through your web page, you upload the code onto the micro SD, which is on the module. And then you can run it from the web page. So you basically have everything right there. Got it. And since we have the SD card and the web UI, we're considering it's a next step is to put, like, an ESL-like program right on there. So now you almost have everything. And it's going to start out simplified by using, like, an SVG to G-code generator. So you bring that in, drop it on the web page. It does a conversion for you, mostly for things like drawing machines and stuff like that, where you don't have, you know, complex feed rates and lead-ins and stuff like that, where you're just, like, touching a pen and drawing. But you have virtually infinite capacity to serve material from an SD card through that web page.

**Bart Dring:** Oh, and you're saying there's, like, enough RAM to actually run, like, a program that could do all that other stuff?

**Bart Dring:** Well, it would be the, it would be just served to the web page and the processing would be done on the browser side.

**Bart Dring:** Oh, interesting. Okay. So, like, it's a JavaScript-based...

**Bart Dring:** Exactly. So you'd serve the JavaScript to your web page. Interesting.

**Bart Dring:** Okay.

**Bart Dring:** So we could do, like, G-code visualization and all that stuff. Yeah. That's cool. So we're pretty excited about that. Most of the web work has been done by a guy named Luke out of, he's in France. And he also is working with some other programs. So it's sort of like a universal web front end for this stuff. And he even has it for the ESP-28266. If you just want, like, to put it on ramps, you know, you just plug in the 8266 put in front end.

**Bart Dring:** Oh, and it's like a retrofit almost.

**Bart Dring:** Yeah.

**Bart Dring:** That's cool. That's a great idea.

**Bart Dring:** Yeah. So now when I demo a machine, I have an SD card with all of the demo code I want to run. I open up my phone. I hit go. And then I can close my phone. And the thing will run totally autonomously. Because the file... You're saying because all the G-code file is on that SD card.

**Bart Dring:** Yeah. Which is being pulled off by the ESP-32. Okay. So if you were going to have... Okay. So if you had the KiCad logo, because you made stuff like this before, the KiCad logo is a G-code. Some point has been converted to G-code. You're saying that this web front end that Luke's doing basically allow you to then on your... Looking at this file, now you'd basically be able to re-render it and say, oh, that is the KiCad logo? Exactly.

**Bart Dring:** Now, he hasn't done any of that yet. Sure. And he might not be the one who does it because he's not... He's an expert in a web UI, but not necessarily SVGs. Sure. But yeah, that could be done. You could just drag and drop an image. And a lot of the stuff like Easel and all this plotter art and stuff like that, their native file is SVG. Uh-huh. So if you have this universal step where it goes to SVG, whatever to SVG to then G-code... Right.

**Bart Dring:** It's like these ad hoc translation layers, effectively. Yeah. Yeah, that's cool.

**Bart Dring:** And then you say, if you create something that goes to SVG, we've got the rest of the chain for you. Nice. That's great. That's really great. So if you can pack it onto the SD card... Right. And then storage capacity is insane, right? You can get 128 gig for pretty cheap. Right. So what's nice about the way it works is I'm taking this machine to an unknown location, like Hardware Happy Hour, some random bar. I have no access to their Wi-Fi, so it's going to come up into an access point mode. And then I can get on that access point with my phone and then work it that way. So at that point, I don't have easy access necessarily, like especially with a phone, to the larger internet. Mm-hmm. So I am trying to get as much as I can right there. You know, like if you get a logo, you might download it and then switch over to this access point. But if it were in your home use, you would immediately put it on your home Wi-Fi. Right. And it works after that. That's great.

**Bart Dring:** So, okay, let's talk about some of the machines you built too. So we've talked about the NickelBot. What is that?

**Bart Dring:** The NickelBot is a wooden nickel engraver, laser engraver. It's about the size of a brick. A little bit bigger.

**Bart Dring:** It's taller, right?

**Bart Dring:** It's half a loaf of bread. Half a loaf of bread.

**Bart Dring:** That's good.

**Bart Dring:** Half a loaf of bread. Yeah. And it's got a hopper. You load the hopper vertically with wooden nickels. And then a little bed moves under, picks up a nickel, clamps it, and then moves it under a laser. And then it laser etches it.

**Bart Dring:** Of course. Yeah.

**Bart Dring:** And then when it's done, it ejects it out the front.

**Bart Dring:** That's right.

**Bart Dring:** So that was a fun one. And it seems like I'm demoing a lot of these things, you know, at events and bars and things like that. So it's always nice to have a worthless tchotchke to take away. And these nickels cost, you know, four or five cents from Amazon if you buy a big bag of them. And they're a pretty uniform size. And that's just a good way of demonstrating it. And I always like to bring something that's kind of a conversation starter. You know, they see the laser blinking in there.

**Bart Dring:** Sometimes you see the laser when someone's opening up the thing to do some maintenance during the bar times. And I look straight at it. I'm like, oh, my God. I'm going blind. And then you tell me that that's actually not how it works. That's not how it's going to work.

**Bart Dring:** But, you know, it's definitely I avoid that. All my laser boards have now, like, interlocks on them and stuff like that. So if you open up a door, it's going to shut it off. But, of course, everybody's, like, trying to peek through the cracks and see it and stuff like that. Yeah, you want to see a laser if it's there, right? Which is reasonably safe. You know, it's not going to hurt anyone because the laser diffuses so fast. It's actually defocusing really, really quickly. But I usually put a window on which has a filter for the laser so that, you know, the laser doesn't come out, especially these visible lasers. Like an IR laser is not going to go through glass, but the blue lasers will. So you have a filter. And then they're looking through the window and they see it kind of, like, getting brighter and dimmer and brighter and dimmer. But they can't see the laser. So they're always kind of trying to sneak away in.

**Bart Dring:** Yeah, right, right. And then you do the same thing.

**Bart Dring:** That was the coaster you did as well. So there was another one. Yeah. So another one I did was they cut square coasters. And to make it as small as possible, it was a traction feed. So the width of the machine was actually smaller than the size of the coaster. And it would, you know, poke in and out through the front and the back. And it would cut shapes out of a drink coaster. And then it would pop it out the front and you'd poke out the shapes because they were kind of loosely fit in there. And that was another good demonstration.

**Bart Dring:** Yeah, that was interesting, too, because I had never really thought about a robot having the X, I guess the Y direction in that case was just a roller. And then the X was the actual gantry going back and forth. Yeah. And that's the only two motions that it needed.

**Bart Dring:** A lot of, like, vinyl cutters and things like that worked that way. Okay. Or old, old school, like, HP pen plotters where they would just move the paper back and forth. Yeah. And then they could use roll paper. They could use anything like that. So I took that idea. And the coaster, again, is a very well-controlled size. So I could make it just for that. And that you had to feed it in. But it was kind of cool because it would kind of grab it out of your hand, do this little etching, and then spit it out the front.

**Bart Dring:** Yep, yep.

**Bart Dring:** So that was kind of a crowd pleaser.

**Bart Dring:** Right. Well, it's amazing, too, when you think about it. Like, so many CNC machines. I think this is, like, what Nadia worked on a lot, too, is that, like, so many CNC machines, it's like linear motion, rotational motion. Those are the two things. And it's like you get to have some other more unique, not unique, but, like, exotic-type motions. But most of the time you don't need them, right? It's just replacing, you know, putting these things together. So then you took the rotational and you did another coaster bot.

**Bart Dring:** Yeah. Well, that's sort of, like, what really interests me is exotic kinematics. Mm-hmm. And so a lot of my machines incorporate some weird kinematics. And that was where the polar coaster came in. That was using round coasters, drink coasters.

**Bart Dring:** And we should probably not go to bars as much anymore for these events. You just make all these coasters things. I enjoy it. They do have beer.

**Bart Dring:** And so when I thought of the round coaster, I thought, well, how can I exploit the round shape? And that was by making a polar-based machine. So it's basically spinning the coaster and just moving the pen. And it only has to move from edge to center because it can get anywhere by rotating the coaster to get there.

**Bart Dring:** Yeah. Right. So it's just about breaking up the line segments so that they kind of match that new paradigm. Yeah.

**Bart Dring:** Yeah. There's a lot of crazy kinematics that are involved. And Gerbil doesn't natively handle kinematics. So initially, I would make polar post-processors. So it would break a line into little segments and then do that. And I don't know if I could do a good job of describing the problem, but if you were to draw a square centered on a coaster, you're basically dealing with four points, all equal radii from the center when you're drawing this. Yeah. So if you told a polar machine to draw that, a non-polar machine, it would leave the pen down between those points. Sure. There is no change in radius. The polar machine would basically draw a circle with those four points exactly in the same spot. Right. So I hope I did a good job of explaining the problem. So if you broke that line into two pieces, now you would get a point in between those two points on that square, but it would make a hump between doing the same problem. So you keep breaking it down until the hump is basically below your threshold of, I would say, a quarter millimeter. So it might be 100 lines. But Gerbil loves little lines. He just slams through them like they're not even there.

**Bart Dring:** As long as they're sequential too, it'll actually look pretty smooth.

**Bart Dring:** As long as they're sequential and there's not a strong angle between them. So like if you did a really acute angle, Gerbil will come to a complete stop because it can't effectively round that. But like a square, it actually does a little bit of rounding that you can't see, which cuts down on some of the stop and acceleration.

**Bart Dring:** Interesting. And so that's just what, that's actually a good tie back to the software too because that's what it's actually doing.

**Bart Dring:** Yes, that's the secret sauce of a motion planner is how it enters and exits corners.

**Bart Dring:** Okay. Interesting. All right. So what about some other tools? So then, let's see. So you did some other drawing tools as well. You did the draw badge. Was that next or was that?

**Bart Dring:** Yeah, I did the draw bot badge. That was back when badges took over for fidget spinners. I had to get into the badge life realm and I made a drawing badge, which used hobby servos. And I'd done a couple other hobby servo projects. So I was familiar with that. But that was some crazy kinematics going on there as well. What about that? There's like two, you'll have to like post a link so anyone can see. Tons of links. Yeah. In the show notes. Two servos are adjacent to each other, which moves some arms. So it's like a four bar linkage. Oh, because of the shape of the arm you're saying. Because of the position of the, that I had to put these hobby servos in. And they were cheap hobby servos. They were like $1.10 each from China. So they weren't real accurate. And so it was kind of, I called it adorably wiggly lines that it would make. But that was a fun project. I think I did a workshop at Supercon with that. I think I took on a little too much ambition on that project. Tried to make it a full-fledged CNC controller that could do anything when really it just needed to be a badge. So it was kind of badge life hell for about a month and a half. People doing too much for badge life. Who would have thought? Who would have thought?

**Bart Dring:** But it was a fun project. So before you go on with this stuff. So you mentioned like the breaking it down into lines and like having to do this math, the polar to Cartesian, right? Yeah. What are you doing that with? Is that all like Python?

**Bart Dring:** Or what are you doing that processing with? So I generally do it in Python and it's like a script. But now that it's on the ESP32, I can actually do that in real time. Okay. So when it sees a line, it'll actually break it down in real time. Before Google actually needs it, it'll break it down into the thing. So there's like built-in, I call it like a basic kinematics. It's not like true kinematics where there's inverse, forward kinematics, stuff like that. It's just basically pre-processing it before it gets there.

**Bart Dring:** Okay. So let's go back. So you're saying when it's a line, it would be that same G0, X10, Y10, right? That's the thing you're saying, go 10 units right and 10 units up or whatever it is. That's the line you're talking about?

**Bart Dring:** Yeah. So if it were like, it would break that down to the point where it's not visible anymore. So I would like add in a, it's like, it's going to deviate from the perfect path. And in the kinematics pre-processing, it says don't deviate more than a quarter of a millimeter. It's whatever you want. Sure. You know, it gets more and more lines the deeper you go. But if you've got a pen that's, that's twice that diameter that's doing the drawing, why not use that number? Okay. So that was done in a Python script. It would just take the G code in one end and spit it out the other end. Just same kind of- G code in, but G code out. G code in, G code out. Got it. Okay. But, you know, 400 lines in, 6,000. Yeah. Right. Okay. Yeah.

**Bart Dring:** Just because it says, this doesn't look like it's going to be possible. Exactly. Go do these other sub moves. Right.

**Bart Dring:** But when you're drawing the Kaikad logo, it's already 400 lines. Yeah. You know, because there's so much detail there. So it might only add four or five extra ones for, you know, the asterisk somewhere, you know. Sure, sure. So it doesn't necessarily explode it too high. But ESP32, we'll just do it on the fly. And I've done that as a demonstration project on, I can't remember what, which one I did that on. I think it's the string machine.

**Bart Dring:** Okay.

**Bart Dring:** But, so I have a proof of concept that it works in this sort of pre-processing route. What I'd like to do is a more pure kinematics where it's sort of inverse forward kinematics. I'm probably not going to do a good job of describing this. I'm pretty out of my element right now. So, but, so when you, you're kind of throwing away a lot of what the machine is capable of when you're doing this pre-processing. Because you have these like accelerations, maximum acceleration in any axis and max speeds and things like that. And that's kind of lost in this when you get to exotic kinematics. Gerbil still thinks it's working in, in Cartesian space.

**Bart Dring:** Oh, okay. So is it because like if you were, so if you had a line that was then broken into three segments, right? Right. You would normally, if it was, if it was able to do the whole line, it would accelerate at the beginning, accelerate at the end. But now you're cutting into three, so now you accelerate and de-accelerate three times.

**Bart Dring:** So like if you have a exotic robot arm with six axes, you know, what you really want to deal with is the acceleration and stuff of not only the tip, but each joint has its limitations. So, and, you know, it's non-linear. So as this pen might be moving or whatever your end effector is on the robot, the joints might have to work at the same speed of that end effector. The joint might have to move at different speeds along the way. It definitely will have to. Oh, got it, got it. And so you have to, a true kinematic will also take in account those joints. Got it. So you're no longer talking about axes, you're talking about joints, you know, and so you say move this tip at this speed. Okay, I'll do that, but I'm also going to deal with all these other joints as well.

**Bart Dring:** So then it's optimizing for, you basically bound the problem for a particular joint, you're saying. You can go this fast, you can accelerate this fast. Yeah. And then that has to play back into the model, you're saying. Yeah, yeah.

**Bart Dring:** Now things like Linux CNC do that natively. Got it. And so that is the true way to do it where you just have two equations, a forward equation and a backward equation. You know, there might be, not equation, like, more like methods. Matrix box. Giant long methods. But some of them are pretty trivial. Yeah. But then you can, like, abstract it from the machine a little better. Okay. And, like. That's what I was going to ask, because it seems like. Like, you could do a wall plotter, you could do a string machine, you could do a robot arm, you know, and then everything else stays the same.

**Bart Dring:** Right, because it seems like the. So, like, Boston Dynamics has got really, really optimized joints and everything that's on there, right? Yeah. All their kinematic models are figured out. But they know that machine. And it's like, you're talking about prototyping new machines. You prototype every month or two, you've got a new thing. So, is that what you're saying is being able to abstract this to your next prototype also takes advantage?

**Bart Dring:** Yeah. That it's more of a universal solution. Okay. Where it's easy. And then there's, like, a trivial kinematics for Cartesian. It's like X equals X, Y equals Y, Z equals Z, move on. Yeah. And then, like, for a core X, Y machine, which is like an Ultimaker machine or the MPCNC. Oh, sure, sure. Well, that's not core X, Y. It's where the actuator is in the middle. It's like a T-bot. Yeah. Yeah, I probably got a couple of those wrong. But, you know, that's. There's, like, these styles of machines. Yeah. Then you have a set of formulas for that. Got it. It's much more universal solution.

**Bart Dring:** So you don't have to rewrite a new translator until you make up a new weird way of doing things, right?

**Bart Dring:** Yeah. And it's also, you know, it's not so bodged into the code like it is now. Yeah. Yeah.

**Bart Dring:** Okay.

**Bart Dring:** Well, you mentioned the Stringbot. What's that one? The Stringbot was my most recent machine, and that's a string art. And I did a great video on it, which explains it entirely. But basically, and I won't do justice to the video or how I explained it, but basically making art with string. And I saw it on Hackaday a couple of times, and I saw a circular one where it's nails around the perimeter of a disc, and you run the string from nail to nail. And I've always been interested in string art, and I said, I've got to make one of those. And this was an interesting design process I went through. I was swamped with other projects. So I had this in the back of my brain. And I think I almost—

**Bart Dring:** You talked about this at three different lunches. Yeah, yeah.

**Bart Dring:** I keep talking about it. But basically, it never was my fingers on a keyboard or pencil to paper. Like, just months of just running it around my brain. And it was kind of an interesting way because I, like, had the machine, like, completely designed and just never any time to actually make it. And then finally, I got a time to do it. And so basically, I based it on my polar machine because why not spin the bed and make this tiny little mechanism that only has to move in and out of the nails. So you got one accurate axis, which is the spinning of the table. It has to be accurate enough that you get to thread in between the nails. And then all other axes are just dumb. They're just either in or out. So it was a very, very simple machine. There's, like, a drilling rig that drills for the nails. There's a needle that runs it in and out. And that's about as good a job as I'm going to be able to do it describing it.

**Bart Dring:** Yeah, the video image was good for the details. Yeah.

**Bart Dring:** And so it was just a lot of fun to make. Everything went well. And, you know, it looks great. And it was a fun project. The software seemed like it was the tripping point, though. The software—there's a lot of people that had done the software for, like, the string paths and stuff like that. So all I had to do was modify it for my machine, you know, just the basic for the G code that comes out of my machine. Yeah, the software's crazy. It takes, you know, six hours to generate the— Right. To generate it. And that's right. I had to—to make it get down to six hours, I had to take my machine up to 32 gigabytes.

**Bart Dring:** Of RAM.

**Bart Dring:** Of RAM. Yeah. And a state-of-the-art, you know, plug-in SSD because there's still a lot of disk swapping going on. Yeah, right. That's crazy. Yeah.

**Bart Dring:** It's a lot of math. Yeah.

**Bart Dring:** But once you cross that threshold of, like, there's enough RAM, then the time just drops by, you know, a tenth. That's good.

**Bart Dring:** Yeah, it's weird, too. I mean, it's weird to me to think that, like, after all that—so you have these images, right? And now that you've got—you use Matlab for generating this thing. But then at the end of the day, it's still G code that then goes down to, you know, motion steps. And, like, it's that same kind of path each time. Right. Do you ever see that changing? Is there a reason to? I guess I don't even—I don't know if that's a stupid question or not, but, like—

**Bart Dring:** Yeah. There's probably a lot of opportunity for changes. You know, there's, like—these are all stepper motors, which are all open loop. But once you start getting into closed loop, things like that, you know, you still run the same process. But maybe instead of, you know, like getting the needle to run through the nails, you know, in such tight coupling, you just have a camera that watches it. And it's like, oh, it's a little closed. Let's move the thing this way and stuff like that. You could close the loop in different ways. Not everything has to be super accurate. You know, you're trying to get from here to there, like, especially with robots. Like, if you're trying to get a robot to tie a shoe, you really can't program that. It needs to see the lace and, you know, how it's laying and things like that. So, you know, in those type of things, yeah, I see a lot of areas for that to go. So, you know, and then maybe it can make it back into CNC, you know.

**Bart Dring:** Yeah, right. Well, that's what I mean, though. Like, so even—so say you have a vision system today, right? And your thing knows that it's a shoelace. And it says, okay, now flip the shoelace over here. And it even calculates the path. You know, okay, the little arm has to go from X1 to X2 or whatever, right? Yeah. It's still stepper. It's still, like, there's still some G-code-esque command there. And maybe it's just because that's—I don't know. Like, Gerbers are never going away. Probably not going away. You know, G-code doesn't seem like it's going away anytime soon.

**Bart Dring:** Yeah. Well, it's, like, one of the things I think about is, like, jogging a machine. If anybody's used a CNC machine, you know, you hold the key down and it slides left. And then the page up and it slides in the Y. But, like, actually, like, getting it to target, like, right over where you want to be is annoying as hell. You know, you kind of want to just, like—

**Bart Dring:** You know, the picking place that's out here is not too bad on that. It has, like, a picture of the bed. You click on the bed. Exactly. And it goes there, right? Right.

**Bart Dring:** Well, there are some centers that do that. But, you know, more like if you had a joystick, you know, where you're just kind of swinging the joystick around saying, I kind of want to go this way a little here or this. And not that you're swinging the direction around, but you're swinging the target around. And I think that's maybe what the Neoden does where you're, like, this is the place I want to go. Right. And then it's back calculated from there. Yeah. Now, definitely, they're using stuffer motors. They're using probably some G-code behind it. Cheap. That thing is cheap.

**Bart Dring:** The Neoden 4 is not expensive.

**Bart Dring:** You know, so that—and there's senders that do that where you can, like, click on your thing and it'll go there. But, you know, just, you know, getting away from so much hard, you know, exact go this way, go that way, I think there's a lot of opportunity. But I kind of like this, you know, criminalized idea of the motion planner because then I can, like, abstract that away. Sure.

**Bart Dring:** I figured this out once. I'm done with it, right? Yeah.

**Bart Dring:** And, like, that it is now my, you know, motion control little worker that all I have to do is say in this high-level language, do this, do that. Right, right.

**Bart Dring:** I actually would be very surprised if I walked up to the bench and I saw you working with something that was not an ESP32 in the near future. Because it's like, why would you redo that? Unless there's some real reason to do that, you know? Yeah. Because it's done, right? Right. You know?

**Bart Dring:** Well, yeah, unless, you know, unless there's a better one, I guess.

**Bart Dring:** Yeah, of course, of course. But I'm saying that, like, you're saying with the compartmentalized, you know?

**Bart Dring:** Yeah, yeah. But I don't really see the need to get away from the Gerbil-based stuff because it's plenty powerful for what I need to do. Yeah. It's just the, you know, the peripherals around it that I might change. Like, right now, ESP32 doesn't have a native USB. So, like you said, you can get it for $2 and plop it down. But you need the support structure around it and stuff like that. It would be nice if it had native USB.

**Bart Dring:** I've heard rumor that the next, I think I heard rumor at Supercon that Espressif might have one.

**Bart Dring:** I heard a lot of rumors, too. I didn't, you know, they kind of nod, you know. But, you know, this Chip 7 or whatever they call it had no evidence of that. So. Yeah. Plan when we get there, right? Yeah. Yeah. But the nice thing, if it had native USB, is not only, right now it's USB to serial. You could then have, you know, it would mount and look like a flash drive or things like that. Drag and drop. And, you know, everything that USB can do would come into play.

**Bart Dring:** Yeah, that's really nice. Yeah, I do like that on the SamD chips. Yeah. That's real nice.

**Bart Dring:** You know, once it's native, then the USB is free to do what USB does best. Right.

**Bart Dring:** And dropping stuff on boards, too. It's just you drop it down, hook up D+. Dropping firmware. Yeah. Yeah. Right, exactly. Yeah, that's great. Yeah. So that helps a lot. Yeah. Well, what else should we know about you, Bart? I mean, we've been going here for 90 minutes pretty strong, so.

**Bart Dring:** That's about it. You know, I guess I kind of dwelled on that I'm like semi-retired. Like I left Inventables, you know, to just kind of pursue things that I want to do on my own. So a lot of this stuff is kind of fanciful and, you know, not too. For funsies. Funsies, yeah. But I have been like trying to get this going. So, yeah, you know, if you're interested, check out the GitHub for that.

**Bart Dring:** We didn't even bring up Twang. I didn't even think about it.

**Bart Dring:** Ah, Twang. Oh, come on.

**Bart Dring:** It's another project. It's an LED project. Back to your gaming roots, though, too.

**Bart Dring:** Yeah. But, you know, and like to move the project along, I am selling some of the controllers on Tindy. And, you know, looking for any opportunity to move it forward. Yeah. Yeah.

**Bart Dring:** Interesting. Manufacturing stuff coming up, I think, too. Yeah.

**Bart Dring:** Yeah. Yeah. Hopefully I'll do some more OEM stuff. Yeah.

**Bart Dring:** That's good. That's good. Oh, cool. I'm excited. I mean, I'm always excited when you come to meetups and stuff and bring more robots. So it's always good to have that. And I think that this is, you know, like given your background, too, and your software, hardware, software, electronics, and mechanical, it's all together. It's like a really good, you know, meeting point of all those things. I really do. I like that as an example of like, no, no, no. This is like you need all these disciplines, but it's also now it's accessible. It's open source. It's great. I mean, it's really great to see more people doing it.

**Bart Dring:** Right. And a lot of it's self-taught, you know. Yeah. I had some formal training in mechanical engineering, but firmware and electronics and things like that. And there's a lot of things I've done where I was just like intimidated as hell. But, you know, you just push through it. I think like on the Carvey machine, we needed a new bootloader. We were trying to find someone to write a bootloader, and that sounded like the most scary thing in the world. Right, right. And finally, it was like over a weekend, I said, well, how hard can it be, you know. Yeah. You know, and I did it, you know. That's great. It's.

**Bart Dring:** And it is that. I mean, sometimes it's like saying like someone's done it, so I could probably do it, right. And it's like, but it's time and then resources and, you know, everything else and then chunking at it, you know. Right. Yeah.

**Bart Dring:** Like, you know, everybody's got those like, I sure would love to know how to use FPGAs, you know.

**Bart Dring:** Spend some time and. Dive in. Right. And ask for, you know, ask for some help online or whatever, right. That kind of thing. Make a promise you can't keep. Yeah. Right. Start selling a product. Why not? Right. Bart, thanks a lot for joining me here. Okay, it was a great pleasure. All right. Thanks.
