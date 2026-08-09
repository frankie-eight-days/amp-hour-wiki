---
episode: 425
title: An Interview with Chris Osterwood
url: https://theamphour.com/425-an-interview-with-chris-osterwood/
---

**Chris Osterwood:** This is The Amp Hour Podcast. Released January 13th, 2019. Episode 425. An interview with Chris Osterwood. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Chris Osterwood:** And I'm Chris Osterwood of Capable Robot Components.

**Chris Osterwood:** Welcome, Chris. How are you doing?

**Chris Osterwood:** I'm doing great. How about you?

**Chris Osterwood:** Good. I'm assuming we're going to be talking about robots today. Is that a fair assumption?

**Chris Osterwood:** That is a fair assumption.

**Chris Osterwood:** Is that a fair assumption for you for most days of the week?

**Chris Osterwood:** Yeah. Though differently in the last year than previously in my career. Okay. Taking a slight departure, but we'll get into that, I'm sure. I'm sure we will.

**Chris Osterwood:** So how do you define robots?

**Chris Osterwood:** That's a good question. The kind of robots that I've been working on that I enjoy working on are autonomous ground robots. So things that are 100 pound, 1,000 pound, that do useful things in the real world, that aren't tied to a particular work cell in a factory. So that's what I think of when I think of robots and when I say robots. But there's obviously a huge variety to the term. It's really amorphous.

**Chris Osterwood:** And growing too, it seems like.

**Chris Osterwood:** Oh, yeah. Yeah. Every day.

**Chris Osterwood:** Yeah. I was talking to my girlfriend earlier about robots and I was mentioning that we're going to record about it. And she started talking about something that kind of sounded like automation. And I was like, well, wait. We got to determine between automation and robots. There's all these different terms that kind of get mishmashed together. And so it can be tough.

**Chris Osterwood:** It is. And I actually wrote an article recently about automation versus autonomy. And there's a very subtle difference in those definitions that I think is an important one. Could you define it here quickly? Oh, man. That'll take too long.

**Chris Osterwood:** There's no two-second overview.

**Chris Osterwood:** I need to spend some more time to get it down to two seconds. But CapableRobot.com has the article. So if people are curious. But sort of the high level is things that are autonomous have more agency and more self-governance than things that are automatic. And it's a minor point, but it sort of relates to the depth of understanding and freedom to operate that a system has. So something that's purely reactionary or purely deterministic, I would call automatic. But if there's more freedom of thought and expression in a system or indeterminism, then you start getting into autonomy.

**Chris Osterwood:** Right. So like if-then-else kind of loops are automation. Yeah, that would be automation. Yeah. Right. Yeah. And that seems very common these days, right? But it's not all of it, it seems like.

**Chris Osterwood:** For sure. And you can accomplish great things with things that are just purely automatic. I mean, nearly all robot arms in factories are pure automatic. There's not really a higher level understanding of the world around that arm for it to operate and be very productive and successful in its task.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** But it gets a little bit trickier to sort of classify things when there's randomness in the behavior, but there's not like a depth of understanding. And like the first generations of the Roomba are a good example of that, where it doesn't do the same thing every time. But it doesn't really have great understanding of what it's doing either. Right. And I'm not, I don't, I don't have a great answer of how you would classify that. But the newer systems they're building, I would definitely call autonomous because of the map building and sort of depth of understanding that those systems have.

**Chris Osterwood:** So somewhere between like logic and fuzzy logic and then like actual like neural networks and stuff like that. Are those, did any of those terms actually land or am I just talking about already?

**Chris Osterwood:** Well, I think that those are sort of ways that you would, could implement these sorts of systems, but they're not how you would define the system.

**Chris Osterwood:** Well, let's, maybe let's go back a little bit. So how did you get into the field of robotics in the first place? Because it seems like a big wide field that's growing a lot. And it seems like there's, there's a couple of ways to get into it, but how did you, how did you get into it?

**Chris Osterwood:** I got into it. Um, let's see. So I, in high school, I, uh, I had a summer job at, um, a Java web services company, um, back when Java server pages were the, the enrage. Um, and the guy that ran that was a CMU grad, uh, Carnegie Mellon university and encouraged me to apply there. And that's where I got introduced to robotics and where, you know, the whole trajectory of things that I worked on changed was attending Carnegie Mellon. Um, and what I loved about the school was its focus on practical systems and field robotics, specifically, uh, the robotics Institute there has a field robotics center that, uh, does things that most people would find, uh, not sexy in terms of robotics. But I found fascinating, like autonomous robots that went to the Chilean desert and looked for life and, you know, things that, uh, mapped and monitor coal mines and all sorts of different, uh, autonomous and semi-autonomous systems. Out, uh, in the real world. So that really captivated me. And I was lucky enough to, to get in and, uh, was a mechanical engineering student there, but really active in the robotics club, which saw tremendous growth. Uh, when I was there, we went from like, you know, 20 students to over a hundred, uh, over the four years that I was involved in the club. And, uh, started some student taught classes there. And then connections I made with, uh, the research that I was doing as an undergraduate led into all of the jobs that I've had since then.

**Chris Osterwood:** That's great. And, and, and, and, at CMU, is there a, um, you know, was there a mechatronics type program? I mean, I don't know, it seems like there's a huge robotics focus, but I know a lot of programs are switching over to like mechatronics where there is that combined electrical mechanical kind of stuff.

**Chris Osterwood:** Yeah, I don't, at the time there definitely wasn't. I think there, there's likely more of that now, but at the time, and I, I still basically agree with this, that the field of study of electrical engineering is really large. And computer science is really large and mechanical engineering is also really large and trying to cram practical knowledge of all three of those disciplines. In addition to how do you think, how do you write, you know, into four years as an undergrad, uh, seems like a difficult task for any school. So, um, it was definitely a, a segmented, um, from a class perspective, but there were, uh, there were lots of projects and research happening that would pull people from all disciplines to, you know, to achieve the research aims of whatever was happening. And that's the thing that I really love about robotics is that you can't just solve problems with software. You just can't solve problems with, with the right electronics or with the right mechanism. It's really an integrated design in all three disciplines. So you, you're forced to work in, you know, cross-functional teams to solve the challenges that you're faced with.

**Chris Osterwood:** Right. Right. And I mean, the, so we talked about this with James Bruton a little bit when he was on the show a couple of weeks ago, but the electronics doesn't seem, I mean, I know it changes, but it doesn't seem to change that much from iteration to iteration. It's like, because there's so much software stuff to do and mechanical, you know, linkages and all the things that have to happen when you're making a different type of robot. But do you, do you see a lot of things changing in the electrical side of things?

**Chris Osterwood:** Yeah. But, but maybe not in the ways that, that people who are building consumer electronics or other things that are really electrically heavy. Okay.

**Chris Osterwood:** So there's no, there's no like motor driver chips that are being introduced at CES this week. Is that what I'm hearing?

**Chris Osterwood:** Well, I think, you know, Trinamic's doing some really awesome stuff and I'm excited to see what they come out with in the next couple of years and like the RISC-V processors that they're integrating into their motor controllers. I think that's a really interesting and yeah, really interesting move and I'm really excited to see what they do. So, you know, there's innovation happening everywhere. You know, mobile processing has seen tremendous change in the last decade. You know, what you can get per your dollar or per your watt is hugely different now than it was a couple of years ago. And that's really enabling, you know, a whole new generation of advanced behaviors and robots that have much deeper understanding of the systems that they're interacting with or the world that they're manipulating.

**Chris Osterwood:** Oh, interesting. So you'll see like, so within a robotic system, you would, you would be kind of tracking upgrades based on a new ARM processor coming out and you would just, you would basically use that to make a better motor controller or whatever.

**Chris Osterwood:** Yeah. Or something that has better understanding of the visual field that it's looking at or faster reaction time or just longer operating life. Okay. When you're a mobile system, you carry your own power source. So, you know, if you're a hundred pound robot, you maybe have 10 pounds for batteries, but that might be stretching it. And if you want to run for, you know, you know, two to eight hours, you know, that can be really, really challenging.

**Chris Osterwood:** Yeah. It's almost like the rocket, what's the rocket equation where like you have to kind of carry your own fuel, that kind of idea.

**Chris Osterwood:** It's exactly the same thing, except you're not fighting gravity quite so much. Depends what kind of robot you are. I guess. Yeah. But yeah, there are definitely compounding effects with the physical size and the physical weight of all of these systems. And they do feed on each other and sort of that negative feedback loop.

**Chris Osterwood:** Speaking of loops, let's loop back to your, your history then. So after school you were, you were doing a lot of club stuff, but you kind of got into the world of robotics and did that for work. What did that look like?

**Chris Osterwood:** So I guess my first job in robotics was unpaid in that I started a small company with two friends and we didn't make any money, but we learned a ton. And it was a great experience. I would definitely suggest people do that if they have the inclination. And our, our company was called Botrix and we built a little behavior based robot controller called the cerebellum, which launched around the same time the, the Arduino did. And we were pick based and serial based instead of at mill based and USB based and that, and you know, the fact that you had to buy a hundred dollar compiler to use the chips and a whole bunch of other things meant that, yeah, that went nowhere, but we learned a ton. We built some high-speed mobile diff drive robots as well. And, uh,

**Chris Osterwood:** Is that differential drive?

**Chris Osterwood:** It was sort of, yeah, exactly. Differential drive. Sorry.

**Chris Osterwood:** I'm going to probably try and disambiguate some terms here.

**Chris Osterwood:** Yeah. Perfect. Thank you. Um, yeah. And that led into my first job out of school at a company called red zone robotics, which, uh, was founded to do nuclear, uh, cleanup, uh, power plants and, um, and sites like that. Um, luckily there are very few nuclear disasters, so they didn't have a lot of work and that went, that version of the company sort of went bankrupt and then it was reformed to do sewer inspection robots. You know, that was already dull and dangerous.

**Chris Osterwood:** I was going to say that that could have been with that name. It could have gone one of two ways. It could have been either, uh, you know, nuclear cleanup, or it could have been a robot that, you know, follows the football player as the gets blown the 20, 20 yard line. Yeah.

**Chris Osterwood:** Yeah. That is, uh, when you search for red zone, you get all sorts of, of different, uh, uh, things that pop up. Yeah. And a lot in sports, as you can imagine. Yeah. Um, so when I was there, I worked, uh, first on a robot called responder, which was a 600 pound hydraulically driven robot that was designed for large diameter, deep tunnel sewer pipes, uh, sort of four foot. Yeah, it was, it was pretty neat. I mean, you say it's not sexy, but like, I mean, like that's amazing to me. Like it was really a fascinating design challenge, uh, in many, many respects. And you have a robot that is under 80 feet of head pressure. It's 80 feet underwater. Wow. Um, in a tunnel that is very constrained, uh, that has high flow, high grit environment. Um, and in some of the tunnels that we were operating in, we had to go out a mile or two because the access shafts are, are so far apart because the tunnels are so deep. They don't want to put an access shaft every couple hundred feet. It would be tremendously expensive to do that.

**Chris Osterwood:** And like, um, wait, are you dropping? So you just like kind of lower it down into the shaft or someone has to actually like go down and take it and put it in there.

**Chris Osterwood:** No, you lower it down on a crane. Um, and then when it sort of hit the bottom of the access shaft, uh, you then would drive it out, um, you know, hydraulic, uh, track driven, uh, system. And it would pull the power tether, uh, with communications back to an operating truck that where a remote operator was monitoring sensors, uh, sonar sensors and, uh, IMUs and things like that to understand where the pipes were going and the condition of the, uh, of the sewer pipe that it was inside of.

**Chris Osterwood:** Huh. And that was, and so you're saying this thing is could kind of going upstream, like in a actual water pipe or something? Uh, in a, you know, yeah.

**Chris Osterwood:** In a sewer pipe. Oh, sewer pipe. Which are, yeah.

**Chris Osterwood:** Oh, high grit environment. You mean, you mean things that rhyme with grit.

**Chris Osterwood:** Uh, well, yeah, but that's not the worst part of it. Like asphalt's actually really bad. Um, and in the United States, at least in old cities, most of the sewer infrastructure, uh, is what's called combined sewers. So it's storm sewer and sanitary sewer combined. So it's really nasty down there. And, you know, the stuff that comes out of houses is the, is very minor, um, in terms of like the, the amount of volume that's in these pipes. Uh, it's all pretty diluted when it, you know, once you get to the eight foot diameter pipes.

**Chris Osterwood:** Oh, and it is just like the, it's the, if you'll excuse the term, the Ninja Turtle pipes, as I used to call them.

**Chris Osterwood:** The ones that you can walk in. Yeah, exactly. Yeah. Okay. Yeah. Except, you know, they don't want to tell people don't use the sewer so that we can send a guy in there to inspect it. Right. You send in these robots. That's yeah. So it was a sort of mechanical engineer and system engineer on that system. And then went to the totally opposite end of sewer inspection robots where we built a fully autonomous, uh, small diameter pipe system that was designed for, uh, sewer pipes underneath, uh, residential streets. So sort of a shoebox size robot that was, uh, 10, maybe 15 pounds. Uh, it's been a while, sorry. Uh, designed for eight through 12 inch sewer pipes. And, uh, that one was actually fully autonomous, which, uh, introduced its own set of really interesting design challenges. So the, uh, concept of operation there is that you'd open up a manhole, go over this, uh, robot down, you know, four feet to 20 feet, however deep the manhole is. To the, uh, the invert where the pipe enters and exits, uh, in the bottom of the chamber. And then you attach a line to, uh, near the top of the pipe where you can still reach when you're on the street. And then you close the manhole and you drive away. And then the robot would fully by itself drive down the pipe, collecting video data. And, uh, and again, IMU data and record that internally and automatically detect when it got to the end of that segment of pipe where it had reached the next manhole. And then it would return to where it started. And so you could be operating many of these robots simultaneously, get a lot more footage per day. And also you're not clogging the streets with a truck parked and blocking traffic as you're manually driving a system down the pipe.

**Chris Osterwood:** And then what was, so this was all just, uh, inspect to make sure if the, uh, pipes were intact and have like tree roots going through or something.

**Chris Osterwood:** Exactly. Yeah. Uh, you know, holes, cracks, um, you know, deformation, uh, depending on the different materials, you have different kinds of. You know, uh, failures that can occur in the sewer pipe.

**Chris Osterwood:** Are these like widely deployed? Like, I guess I've, I'm not in this field at all. So it's not like I'd be like, Oh, I've never heard of this. You know, I, I have never heard of it, but I, why would I have, um, are these widely used these days?

**Chris Osterwood:** Uh, there are lots of those robots out there, but, um, I can't get into exactly how many. Um, it's a, it's, you know, fairly, um, you know, this approach to sewer inspection, it happens all the time. Normally it's just sort of a camera attached to some motors. And yeah, the innovation here was that, you know, you weren't dragging a tether behind you, you know, and you didn't have to have a guy sitting in a truck, uh, defect coating while the system was in the pipe.

**Chris Osterwood:** That's super. Yeah. That's great. And I just, I guess I wondered who, who is this? Like, who is the end user of this? Is it like a municipality buys a bunch of robots or is there a service that then sells stuff, sells this service to a municipality? Yeah.

**Chris Osterwood:** It, in this market, it was both, uh, some municipalities had their own hardware and their own operators. And then some would contract with local firms or international firms, um, you know, to come in and do a whole bunch of work all at once. Yeah. And then, you know, use engineering service companies to, you know, triage all of the inspections that had happened and figure out where do my rehabilitation dollars go this year versus next year and prioritize.

**Chris Osterwood:** No, that's, I mean, that's, I assume that the way to do that previously was like, you dig up the pipe and see if the pipes got a hole in it. If it doesn't, you put it back under the ground, you know, like, so that seems like a really good use.

**Chris Osterwood:** Yeah. They, I mean, they've been using cameras, remotely operated cameras for a while, but, um, you know, having, uh, the, the closed manhole during the inspection is really nice from a throughput perspective.

**Chris Osterwood:** Well, that's great. That's great. And so, and you said in this one, you had switched away from the mechanical side of things or what?

**Chris Osterwood:** I, I did some of that. Um, but I, I, I, you know, I guess I designed like the, the whole drivetrain mechanism on that system, sort of the bottom half of the robot. And another mechanical engineer did the camera system there. And then I was also the system engineer and then eventually became the product manager for that product. Cool. Which was neat to, uh, to get more interaction with end users and, uh, you know, go on, uh, you know, field deployments and, and, uh, really see how the system was operating. I have to say one of the, my favorite bug stories of all time came from that period of, of work where we got reports from, from field operators that there was a location specific blue screen of death on the rugged laptop that was used to operate the system. You know, so you needed to tell it what manhole ID was at and things like that. And we told, we scoffed at this cause you know, a location specific blue screen of death.

**Chris Osterwood:** Like you mean like somewhere in a city makes it go to blue screen.

**Chris Osterwood:** Yeah. Like you, you drive down this road and yeah, at this one particular spot, you try to inspect the pipe and the laptop with blue screen. And you know, we, we laughed at this and then we sent our software engineer who was responsible for the operator control unit out to the field. And he reported, yeah, it's a totally repeatable, 100% repeatable. Wow. And it took a little while for us to figure out what was going on, but what had happened was that someone who lived on that road had created an SSID with a null character as the name of the SSID. So it was a zero length SSID.

**Chris Osterwood:** Oh man.

**Chris Osterwood:** And Windows 95 or 98 or whatever we were using at the time, the wifi driver could not handle that. And blue screen the whole, the whole system. Oh man.

**Chris Osterwood:** That's great. That's great. Is that what you think of this?

**Chris Osterwood:** So, uh, yeah, we, I don't think we managed to, to get that fixed. We just said, well, this pipe can't be inspected.

**Chris Osterwood:** Well, I guess your, guess your house is going to flood. Sorry about that. But it's your fault. You shouldn't use that, that wifi name. Exactly. He's a null character, is it? Anyways. I mean, if you wanted to be hidden. Yeah, I guess so. Yeah. So like on the mechanical side, what does that actually entail too? I mean, is it, is it like specking in components? Is it specking in motors, specking in other stuff? What does that actually look like?

**Chris Osterwood:** Yeah. Uh, it's a, a mix of, um, understanding components that are available and appropriate for use in the system that you're building. Um, in terms of size and power and capability and cost. And, uh, lead time can even be, uh, a way you choose a component. Um, and then also, uh, doing a lot of housing design and drivetrain design, uh, ceiling design, um, thermal considerations. Can you, uh, though? Sorry. Can you, can you define drivetrain here for us too? Sure. Uh, I guess I'd call the drivetrain everything between the motor and the world. Um, so, you know, the gear reduction and the interface between the gearing and the, the real world. Um, so in these systems, they were generally tracked, but you'd have, um, some kind of mini tank. Yeah, exactly. Yeah. Mini tank. Um, but you know, the design of the tracks impacts a lot of, uh, behavior within the pipe and how it interacts with grit and grease and all the things down there. Right. Um, and then there's, uh, you know, anti-clogging things that you need to do. Um, yeah, so you don't throw a track off the system as it's operating. And then, um, you know, gear reductions because motors don't generally have the right torque and speed ratios for most operations. So you need either a motor, um, a gear that's built into the motor or design one yourself that reduces the speed of the motor and increases the torque capability. And, uh, you know, packaging all that, um, in small sealed systems gets really interesting.

**Chris Osterwood:** I was going to say, you got to make sure the grit and the other stuff doesn't get in there too.

**Chris Osterwood:** And yeah. Yeah. Yeah. We spent a lot of time thinking about, uh, seals, uh, static and dynamic seals. Cause you know, if you have rotary motion, you can't use, you generally can't use normal O-rings to seal those, uh, diameters because of the drag coefficients, uh, and the seal life is just really poor. So you have to use, um, things that are designed to seal against rotating shafts.

**Chris Osterwood:** How much of this stuff is, is like learned on the job versus like university style? Cause we'd talked a little bit about mechanical and, you know, the, the, the role of teaching and in robotics and stuff, but like, yeah. How much of that stuff was covered in classes?

**Chris Osterwood:** I think the program that I was in did a pretty good job of, of balancing sort of theoretical mechanical engineering with practical, uh, mechanical engineering. You know, we did things like barren life calculations in class and, uh, drivetrain efficiency, um, experiments and calculations and had a reasonable understanding of, you know, the efficiency of spur gear trains and heel gear trains and bevel gears and, um, you know, worm gears and all the different kinds of ways that you can transform motion. Um, but you know, there's only so much that you can learn in a class and there, you know, there definitely is no replacement for building stuff and it not working or building stuff and it works, but it's too heavy or breaks too much.

**Chris Osterwood:** Iterating and trying again, that kind of thing. Yeah, exactly. Yeah. There was, um, you know, there was a period in this development of this autonomous robot where, uh, you know, the first rounds of prototypes were breaking about every other time that we would deploy them. Um, so, you know, once a day or twice a day. Um, so, you know, we, we, as engineers were out in the field, you know, learning what was working, what wasn't working, repairing things, keeping detailed records of all of the failures that we had over months of operation. And then we use that to triage, you know, the next development phase and figure out here's what we need to fix and how we're going to fix it. And an iteration later on that system. And we could operate for a month without any failures. Oh, nice. And failures in that environment counted, like included things like someone accidentally dropping the robot down a manhole and smashing it. So like anything that caused service on the system, we wanted to record as an incident.

**Chris Osterwood:** I'm just, I'm, I'm wondering because, uh, you know, like I hear this stuff and it seems very foreign to me, the mechanical side of things. And so I wonder about like, if, so if I started from scratch today or if our listeners started from scratch today, you know, what, what is the, you know, like what are the, what are the kind of things that they would need to learn to get the first robot out there, you know, for their, for their basis?

**Chris Osterwood:** Uh, I mean, I guess it really depends on where you want to start. Um, like if you want to build off of an existing platform, or if you really want to start from first principles, you know, you can go all the way to like, you know, understanding magnetic theory and building your own brushless motor. I would not recommend it as a starting point, but like, you know, you can go really to first principles on this stuff if you want to. Um, and you know, I, I guess it all comes down to what problem are you trying to solve and how, how constrained are you in time or money or space? Um, and that sort of make versus buy decision is one of the most important ones that, uh, that I found myself making as an engineer, um, in nearly every project that I've been involved with. You know, do we take something that's been designed for slightly different application or, uh, do we build from scratch? And there's advantages and disadvantages to each, uh, approach as you're building a system. Um, so yeah, there, there's sort of no great starting point from, uh, from knowledge or, uh, building block. You know, it really depends on the particulars of the system you're trying to build.

**Chris Osterwood:** That's not the answer I hope for, but it's a very realistic answer. Yeah. Sorry about that. That's okay. I mean, I think that like starting from a kit makes a lot of sense for a lot of people, I think. And, uh, sure. Yeah. And then from there, you know, learning those other things you're talking about.

**Chris Osterwood:** Yeah. Yeah. Um, but you know, I, you know, a kit isn't going to, uh, you know, a drivetrain kit isn't going to help you if what you care about is a robot that has really good, uh, perception and object recognition, you know? So there's so many facets to robotics that you really need to think about the, the problem that I'm trying to tackle here and what's new and what isn't new where I can just find things that exist and repurpose. Right.

**Chris Osterwood:** Right. What is, I mean, what are some of the challenges that you're seeing? I mean, is it mostly vision these days and similar like processing type things or is it other stuff that's out there?

**Chris Osterwood:** I think there's a whole new world of, of exciting things happening there. Um, I don't know that it's a, I wouldn't call that a problem, but you know, um, it's, uh, it's definitely new fertile ground for people to be exploring. A new problem space. And I'm, yeah, yeah. A new problem space. Yeah. Um, so yeah, there's a lot happening there. Uh, there it's a, it's such a broad field. It's, um, it's sort of hard to pin down, but, uh, the thing that I'm particularly excited about to see in the next couple of years is more systems actually getting, uh, fielded and deployed and there being more, more robots that you see in the, you know, out in the world in your daily life, you know, uh, things that, that help that enable new kinds of mobility that enable, uh, people that have particular challenges, you know, physically or mentally to succeed in the world, uh, things that are, you know, reducing agricultural runoff or efficiency of, uh, manufacturing processes. You know, there's a whole host of challenges and, and things that we can attack with the technology that we have today. And, you know, fundamentally robotics is not an industry. It's more of a approach to developing products, uh, and, you know, a tool set to use in solving problems.

**Chris Osterwood:** Yeah. And I guess it's because, uh, the definition of what a robot is, is kind of flexible anyways, you know, like it's a, is a dishwasher or a robot, you know, like that's a, no. Uh, is a Roomba a robot?

**Chris Osterwood:** Yeah, absolutely. Okay. But if you asked a roboticist to build something to wash dishes, you wouldn't get a dishwasher. You'd get something with many arms and hands and a vision system and it would break all your dishes, um, for a while. Right. Until it learned. But isn't that a bad thing? Yeah. I guess that's my point is that, you know, there, uh, robots are not, it's a technology approach, right? It's not a, um, uh, uh, it's not a, uh, a solution, right? It's a, a way to solve a problem. And there are problems where robotics are definitely not the right solution. And there are other problems where robotics are the only solution. Uh, so, uh, you have to really think about the problem you're tackling and then, um, go back from there. Uh, a great example of that was a system I worked on at Carnegie robotics, uh, which was, uh, two jobs later where, uh, we had, uh, uh, someone who was an agricultural engineer come to us with a new idea or he saw a problem in, uh, fertilizing cornfields and the massive amount of nitrogen runoff that was happening in fields. Because, uh, you know, this is the other thing about robotics is you learn about all these fields that you wouldn't otherwise learn anything about. So in this case, literal field. Yeah. Yeah. Literal field. Yes. Uh, so nitrogen is their fertilizer. It helps corn, uh, mature and grow. And, um, uh, the corn plants actually need nitrogen late in the growing season when they're, you know, eight to 10 feet tall, but applying that nitrogen to the field then is really, uh, tricky and prohibitively expensive because you need tractors that have eight to 10 feet of ground clearance. So you don't, you know, mat down all the corn with your normal tractor. So what ends up happening is farmers apply nitrogen much earlier in the season when the corn is short and then the rainstorms that happen wash most of that nitrogen away and it ends up in rivers and, you know, our groundwater.

**Chris Osterwood:** Right. Um, and it causes like algal blooms and stuff like that and lots of stuff.

**Chris Osterwood:** Yeah. Yep. Um, and nitrogen is actually the second most costly part of growing corn after, uh, fuel and equipment, uh, combined. So, you know, it's a really, or sorry, no, it's, it's seed. That's the most expensive fuel is third. Um, so it's seed, nitrogen, fuel. Um, so if you can apply nitrogen later, it's good for everyone. Good for the farmer because they're spending less money. Good for the environment because there's less, uh, nitrogen runoff, less algae, less waste, you know, all sorts of good. Um, and the solution that we came up with to solving this wasn't automating existing tractors. It was building a robotic system that, uh, wouldn't be possible, uh, without sort of robotic technology and autonomous, uh, behaviors. So it was a 800 pound, uh, robot that would actually drive down a row of corn. So the system was 20 inches wide, about eight feet long and three or four feet high, uh, hydraulic, um, robot that we purpose built just for this task, uh, four wheel drive and a center body pivot. And, you know, the 200 gallons of nitrogen that it would carry were really low to keep it from tipping over. And we were, you know, width constrained because of how corn is planted. It's a particular center to center distance on every, uh, you know, row of corn and it would, you know, drive down a row and spray nitrogen fertilizer right at the roots of the corn when the corn is eight feet tall. And it doesn't matter that it's eight feet tall because you're driving between the rows of corn, not above the rows of corn.

**Chris Osterwood:** Right. Yeah. And it's, if people have ever walked, like I always love the, when they have corn fields and like, like field of dreams or something, they're like slowly walking through. It's like, man, it doesn't work like that. You get smacked in the face by like some of the strongest standing things ever. There's like those ball roots that are there. Nasty.

**Chris Osterwood:** It's a nasty environment to operate in. Yeah. And, uh, for a small system like this, you know, things that aren't obstacles for, with for a tractor that has four foot diameter tires are definitely obstacles for this sort of system, you know, rocks and roots and branches and all sorts of things that are in there. Spiders. Yeah. Yep. Not a big fan of corn fields if you couldn't tell. Apparently. Yeah. Well, now you don't need to go in them. You can use this system. Yeah. Yeah. Uh, so it was, uh, pretty neat that, uh, you know, you, you have a set of tools and sometimes, you know, those tools like let you create a system that wouldn't make sense in any other environment. Um, and you know, it wouldn't make sense for a person to be operating this because it can only, um, spray nitrogen on two rows of plants at a time. You know, a normal tractor has these giant booms that stretch out and you can, you know, fertilize 30 rows as you drive down with these huge gantry systems. And, you know, one person can, uh, fertilize an acre of corn really, really quickly. Right. When the corn is low, this system took a lot longer because it was going up and down every other row of corn spraying nitrogen. But because it's autonomous, you could have multiple instances of this robot driving around a single field and coordinating. I'm going to go fertilize over here. You go fertilize over there. And when we're all done, we come back to the trailer that has dropped us off and we refill autonomously and, you know, rinse and repeat.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** And, uh, yeah, it was a fantastic system.

**Chris Osterwood:** And is there an uptake of this thing or no?

**Chris Osterwood:** It's, uh, it's still in the, the sort of fielding stage. All the technology has been proven out. And, uh, the, the guy, uh, uh, Kent, whose response for that is, uh, wonderful and I love him. And he unfortunately has not been able to raise the next round of money that he needs to build a whole bunch of systems to, you know, really get it to market. So, you know, many acres of corn have been fertilized, but unfortunately, uh, there are not hundreds of those robots out there yet. Right. Right. There definitely should be.

**Chris Osterwood:** Right. Well, and so like another, I was going to say another thing with the, uh, the nitrogen fertilizer too is like that comes from ammonia, I believe. And that actually is like this really, really intense energy process. And that's like a big contributor to, uh, you know, just carbon emissions and stuff like that for like, because I think a lot of it's done with, with, uh, fossil fuel stuff. So that's like another benefit of it being gone or being lessened at least. So yeah, it's definitely a field. I mean, like, I think the ag tech stuff is super interesting, you know, precision, precision

**Chris Osterwood:** ag is really cool. Yeah. There's a lot of new things happening there. And, you know, when you, when you have robots operating in these fields, you can do all sorts of interesting health monitoring, um, that, you know, there are things that you can do on the ground that you really can't do from the air, uh, from an inspection perspective. And there's really real opportunity there. Um, but there's this, you know, there's a cost to deploying systems. So if you can build a system that's providing multiple, uh, value streams, right. Like fertilization and inspection and a health monitoring, there's the real benefits.

**Chris Osterwood:** Right. Right. But you're also going against lots of traditional methods, you know, things that are newer and traditional. So yeah, it's, that's a tougher sell. Well, that sounds like a cool space. So what, what was this place at? Those Carnegie robotics.

**Chris Osterwood:** Yeah. Carnegie robotics, uh, in Pittsburgh. Uh, yeah, I was there for, uh, about six years, uh, started as a senior robotics engineer. And then a couple of years in, uh, was promoted to be the tooth technology officer there and, uh, helped grow the company from, I guess when I started, we were eight. Um, and then I became CTO and we were about 30 people. And I left a year ago when we were about 60. Wow. That's great. Yeah. It was a fantastic organization.

**Chris Osterwood:** So what, what, what does a, uh, a CTO do of a robotics company?

**Chris Osterwood:** Uh, many things. Uh, so I was doing a mixture of, uh, a sort of product development planning for internally funded sensor, uh, products, uh, uh, mainly, uh, stereo, uh, sensors, you know, 3d vision systems, uh, but also some inertial products that we, uh, that we were working on and, uh, some project management on the custom system developments that Carnegie robotics was doing, uh, some business development, helping to make sure that there are custom system development projects for people to be working on.

**Chris Osterwood:** Right. Um, and then lots of interactions with customers on both, uh, the systems and the products, make sure that we're building the right thing and that it's working and, uh, getting feedback and, you know, figuring out the next version and requirements and features and, uh, you know, deployment strategies and marketing and all of that. Uh, I was also doing, uh, IP strategy and working on a patent portfolio. And, um, also sort of a technical resource for the engineering team in design reviews and getting things unstuck, uh, from time to time, uh, you know, a fresh set of eyes, uh, can really help things move forward. Uh, and it definitely was not the case that I was definitely not the smartest person there or one of the most knowledge, but just having a fresh set of eyes on things was often enough to get things moving forward again.

**Chris Osterwood:** Yeah. Yeah. That's great. That's great. Um, what, what kind of people would come to a, like, so I guess like a four hire robotics company too, I guess I don't understand who would hire that kind of company.

**Chris Osterwood:** Yeah. So it's, it was, I guess to answer that question, I'll start with where the company started from, which is a, the original idea was to be the commercialization partner for the national robotics engineering center. So, uh, the national robotics engineering center or NREC is part of Carnegie Mellon, uh, but it's a research institution and, uh, not an education institution. So it, uh, built advanced ground robotics, uh, for people like Caterpillar and John Deere and the army and a whole bunch of other people. Um, and you know, very, very successful organization. Um, and the thing that they saw was that the prototypes that they were building weren't getting to market because NREC by mission as a research institution could not build product. Like it was actually prohibited from selling product. It could only do research. And the people that were funding that research didn't have the technical capability to take those prototypes and turn them into real producible products.

**Chris Osterwood:** Um, they're in the business of a gap developing new, they're developing like, uh, step-by-step and, and just slightly advanced to their tech instead of introducing a whole new field to their, to their stuff. Yeah.

**Chris Osterwood:** Yeah. Um, and you know, tons of really good engineers at all those places, but they're, you know, this, you know, at the time, um, this was a brand new field and that capability and technology understanding really only existed at the university. So, uh, NREC did lots of wonderful things and most of them didn't see the light of day outside of, uh, tech demos.

**Chris Osterwood:** That's a common thing. Yeah.

**Chris Osterwood:** Yeah. Yeah. Unfortunately. Um, so Carnegie robotics was, uh, was started to be the commercialization partner, the bridge for NREC and to take, uh, what had been developed there and to productize it and, uh, did that on a couple of instances. Um, but then, you know, we quickly found our own feet and our own products that we wanted to be building and, um, and sort of, you know, built the business, um, uh, from there. Uh, so we were doing a mix of, uh, custom system development and component product development, as I mentioned, and, uh, working on things like that autonomous agricultural robot. Uh, we worked on industrial floor cleaning, uh, you know, sort of 800 pound Roomba, you know, the things that you see cleaning, uh, hospitals and there's like big green ones that

**Chris Osterwood:** people are pushing that have like the spinners underneath that actually are exactly.

**Chris Osterwood:** Yeah. Or that you ride on top of, um, yeah, yeah. Yeah. For scrubbers, burnishers. So we built a, uh, autonomous, uh, one of those, uh, for a company called Nelfisk. That's really large in that space. And, um, uh, also had a really large, uh, multi-year project with the U S army for, uh, robots that looked for mines and improvised explosive devices. And that was a, a really interesting project and a really, uh, fantastic project to work on, uh, from, uh, you know, getting people out of harm's way perspective.

**Chris Osterwood:** So what, uh, so then you left, you left a year ago. So now you're, you're not a CTO, you're a CEO now.

**Chris Osterwood:** So what are you doing now? The problem that I'm trying to solve with my new company, capable robot, robot components is make it easier for past me to build the systems that past me was building.

**Chris Osterwood:** So this is the, uh, builder by you want to make the things that someone could buy it.

**Chris Osterwood:** Exactly. Yep. So that was continuously frustrating to me was, you know, Oh, well, yeah, we can build this thing, but this thing is not key to the problem that we're trying to solve is, you know, but we have to do it because the things that have been designed for telecom or for, fixed factory automation or for consumer electronics or for agricultural applications aren't appropriate for this task or this platform or this environment or whatever. Um, and your robotics as big as it is, is still a really small industry. So, uh, there isn't the component supplier network there that I believe should be or could be. And that's why I started capable robot components and you know, the whole mission's in the name, building components for capable robots.

**Chris Osterwood:** Yeah. Yeah.

**Chris Osterwood:** So what kind of stuff are you building? I'm, uh, first starting with underlying infrastructure. So, uh, a gigabit ethernet switch on a card that's designed to embed into a larger power or data distribution system, trying to encapsulate all the complexity of that circuit onto, uh, embeddable module and a similar, uh, take on a USB hub, which, you know, doesn't sound very exciting, but most USB hubs don't have any diagnostic or, uh, capability or reporting don't have power monitoring, don't allow you to power cycle downstream devices or disconnect them or understand, um, you know, the health of the system. So, uh, building a USB hub that does that and, uh, some test equipment as well. Uh, and, uh, then next working on some camera systems that I'm excited about.

**Chris Osterwood:** You know, I'm curious about the fact that you couldn't buy this stuff because it's like, so like the gigabit ethernet. So what, what about it? Why weren't you able to just buy something off the shelf? Is it like, it was it, the stuff was there, but it was two extremes of like, one was commercial and super cheap and chintzy. And the other one was like super high end and, you know, bulky and whatever. Like what, why, why does that exist? Yeah.

**Chris Osterwood:** So the, in the embeddable ethernet switches that, um, that I have found, uh, have all been designed for military applications. So they are not cheap. $12,000.

**Speaker ?:** Yeah.

**Chris Osterwood:** Not that expensive, but you're not that far off, you know? And when you look at the capability between them and, you know, a $35 neck gear switch, there's not that big of a difference. Um, but you know, a $35 neck gear switch, you know, it doesn't have the right connectors. Again, it doesn't have the right monitoring. It doesn't have the right control interfaces or, um, you know, you don't want a web-based interface to configure your ethernet switch. If you're a robot, you want to send it to a JSON blob that has all the information on how to operate and, you know, never do that again or send it to it every time it turns on. So there are, there are differences in how you build the product based on the end user and the end application. And, um, yeah, there's a, there's sort of a hole in the middle right now where things that are, uh, in the sort of heavy commercial light industrial, uh, space have a choice of consumer grade products that are cheap and don't last or products that are overkill and too expensive.

**Chris Osterwood:** Right. When I imagine that robot companies of particular sizes, they just, you know, throw someone at the problem, right? They say, well, you're our electrical guy, just go, go make this thing because we can't find it. And then that gets effort gets duplicated at, you know, 40 different robot companies. So hopefully now you're that, that, that person.

**Chris Osterwood:** That's exactly right. I, I know of, uh, three different companies that have built embedded gigabit ethernet switches for robotic systems that they're building. And none of them are offering them as products because they don't sell products. They sell systems.

**Chris Osterwood:** Of course. And so that's an interesting thing though. Is that going to like your sales cycle then, is it going to be based on word of mouth or, uh, knowledge of some of these people or how is that going to work or TBD?

**Chris Osterwood:** Yes. And it's going to be, and it's going to be long, um, because you know, when the, unfortunately with the kinds of products that I'm building, you know, you, you can't just immediately adopt them or you can from a development perspective, but there's definitely two or three years between a product being launched, uh, by me and it being integrated in a high volume production system because someone's not going to retool their, their already certified, already done system to save a couple hundred dollars on an underlying component. Right. Um, it just doesn't make sense. So.

**Chris Osterwood:** Well, then you also have like a obsolescence issues too, right? Cause I mean, if you're doing what is not necessarily bleeding edge now, but even just consumer edge now, and then three to four years from now, you're going to, you're going to have to go through design cycles to maintain your product.

**Chris Osterwood:** And then. Absolutely. And, and that's part of the value that I, that I'm offering, um, that I see offering because, um, you know, the alternative right now is to do this sort of thing yourself. And then you have to go through that obsolescence engineering yourself to keep building the system you want to build. Yeah. Yeah. So unfortunately there's no way around that, you know, you can do what you can to, you know, pick manufacturers of components that have, you know, guaranteed, uh, you know, uh, lifetime guaranteed quote unquote quote unquote. Yeah. Like it changes all the time. Um, you know, I know someone that, you know, bought up the world supply of a particular component because that production line went down and it was, you know, the lead time went from two week to, you know, 30 week.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** And they had to, you know, plan nine months of production all at once and buy, you know, buy the whole, uh, world out. Um, so unfortunately those sorts of things happen. Um, but, uh, you know, the, that pain is being felt everywhere and there is value in sort of consolidating that and having one organization that's, uh, managing it and that has a higher buying power, uh, and hopefully more clout with suppliers as a result of that.

**Chris Osterwood:** Yeah. Yep. One, it kind of also, I mean, you don't have to take this business model, but I always thought like if you actually do make a successful thing and then you do build, out some inventory and then, you know, stockpile, you know, 5,000 units, you know, if you get in the right application and I've always said that like my retirement plan is to like find that one component and then stockpile it and be a broker. It's like a total dick move, but, uh, man, you can make some good money. Just, you know, sell a hundred a year at a, you know, a thousand dollars a component.

**Chris Osterwood:** Yeah. I'm sure you can. I, I, uh, unfortunately I don't think I could sleep at night if I, uh, ran that kind of company. You can sleep like a baby, Chris, like a rich, loud baby. On your giant piles of money. That's right. Yeah. Yep.

**Chris Osterwood:** Yeah. But at this section, there, there is a practical thing I'm getting to here too, is that, uh, is there, is there any thoughts of like standardization too? So like standardizing an interface, because then if you move from, you know, rev one to rev four, but the interface is the same, you know, maybe the end user doesn't care.

**Chris Osterwood:** And there's an easy upgrade path. Yeah, absolutely. Um, that's in ways, you know, defining the interfaces between modules is one of the hardest parts of building a system. You know, you don't want to, uh, sort of over, uh, add too much flexibility or future proof to things because then you're carrying that weight and that burden and you may never need it or use it. Um, but if you design some component and it can only do exactly the thing that you need right now, you're going to be redesigning that component in the future when you need it to do something else. Um, so yeah, that's a big part of, uh, what I'm trying to do here is think through, uh, applications and the future use of things.

**Chris Osterwood:** I always find, uh, the risk of the, the biggest risk is actually, uh, the connector going obsolete.

**Chris Osterwood:** That's, that is a big one. Yeah. And, you know, just choosing the right connector too. Um, yeah, there, there are so many connectors and it is still so hard to find the right one when you need it.

**Chris Osterwood:** Yeah. My hope for, uh, the VR systems of the world, I don't give a crap about video games or anything else that's out there. All I want is like a virtual Shenzhen market where I can walk through and just kind of pick up virtual components, look at them. And I know that's not actually a real thing that's going to happen, but damn, would that be great? Just cause like, I want to have like a sense of scale and I want to see, you know, like, you know, like what's the actual height of these things, you know? And like all the things, how it snaps together, whatever, it's just really tough to do in a

**Chris Osterwood:** virtual world, digital world. Yeah. I've, uh, I've heard that. I think it's IDEO. They have, uh, basically a library of materials of samples of, you know, different plastics and composites and rubbers and fabrics. And, you know, they just sort of collect hinges and all these little building blocks to have at your fingertips. And, uh, I think there's huge value in that sort of, uh, collection and, you know, having a couple of every kind of connector that you could possibly use just around. So when you come across that next project, you can look at all of them and say, does this want to feel right? Does this has the right latch? You know? Oh, but I need it to be vertical. Yeah. Button feel. It's a thing.

**Chris Osterwood:** Yeah. Yeah. It's definitely a great way to become a hoarder though, too. Just so you know, I mean, yes, you'd have a lot of storage space. You do lots of bins, lots of bins. Yeah. I think luckily IDEO charges enough that they can have lots of bins. There needs to be like a lending library for these things. Yeah. I think the, the bits versus atom problem there is too, though, of like, yeah, it'd work great if there was, but it's like, at the end of the day, if I'm going to, you know, if I'm going to pay to fly to, you know, Pittsburgh or, you know, California, why not just fly to Shenzhen where it's the actual things that I could buy? There's, there's almost like a, it's almost like a small adder at that point.

**Chris Osterwood:** Yeah. But, you know, I, maybe this is something that a local makerspaces should spend more time thinking about is what component libraries should we have in house? Because, you know, I'd pay 50 bucks a month to have access to, you know, every button and switch and connector and, you know, that would save a lot of space and a lot of time and a lot of money to just like show up and peruse. Have you been to a hackerspace? I've been to ones in Pittsburgh. I recently moved to New England and haven't been to any here. I'm just thinking like how big of a mess that would be.

**Chris Osterwood:** They have trouble keeping like a band saws in order sometimes. So that's, I totally agree. I'm just saying maybe hackerspaces, makerspaces aren't the best place for it. You know, maybe libraries, like library libraries would be great.

**Chris Osterwood:** Yeah. Yeah. Though, I mean, it's a different mission, but yeah, the library model of you check something out and then you bring it back in the exact condition that you. Yeah. Yeah.

**Chris Osterwood:** That's the key thing too.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** Yeah. That's a great idea. So why, why hasn't your, why haven't people done what you do?

**Chris Osterwood:** In ways they have, you know, there are companies that are building some components, you know, generally in a particular, particular area of real difficult technology, like inertial monitoring or, you know, mapping or things like that. But yeah, I guess I'm not aware of someone doing this on sort of an infrastructure play. And, you know, my best guess on why is just the market is still really small. And, you know, I, you know, it doesn't make sense for someone like Vallejo or Bosch or Delphi to pay attention to this market yet. You know, it's, we're just nowhere near the volumes of their existing customers. And even, you know, people that are building components for factories, you know, there's this high volume in comparison to ground robotics. So we're still early days, but at some point, mobile robots are definitely going to be built the way that cars are built today with huge supplier networks supporting those production lines.

**Chris Osterwood:** Oh, okay. Interesting. What, I mean, guess, where else do you see robotics going then on the ground robotics side of things? That's, um, everywhere. Um, I mean, like, cause so like I look at a Roomba and I don't think like, oh, well, that's going to also be doing A, B, C, and D. I think like, oh, maybe like, I don't know, like I have a hard time seeing that, but you obviously are very much into it.

**Chris Osterwood:** Yeah. I guess there's, there's a whole bunch of different ways that this industry can go and, you know, or is going to be going. And it's sort of the value that you're bringing is changing, definitely changes by the end user. But, you know, for instance, like in a house, um, there are all sorts of things that we do right now that, uh, or that we try to do right now that we often aren't doing. Um, and you know, queening is a good one of them, but I often think back to that, um, that moment in fifth element where the guy's choking on the chair and banks his desk. Yeah. The cherry. Yeah. And like all of these robots come out and they all have the, like, they're very specific little tasks that they do. A symphony of robots.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** Right.

**Chris Osterwood:** Each with an engineer back home feeding their little babies so they can, yeah, sorry. Exactly.

**Chris Osterwood:** And none of them are able to save him. And, you know, it's, it's a wonderful scene about, you know, the, the, the glory and the futility of robotics. Yeah. It's true. But, you know, like that is not the world we live in right now. Like you, you couldn't, those things just aren't available. And, you know, at some point, uh, technology gets cheap enough where it makes sense to have a robot that can bring you a glass of water and that's all it does. And it's really inexpensive and why not? Right. Um, you just like you can buy, you know, packaged goods now that you couldn't buy, uh, previously because of cost and infrastructure and all sorts of other things. So, uh, you're saying we're going to end up with a butter robot.

**Chris Osterwood:** Is that what I'm hearing? What is, what is my purpose? Yeah. If you want one.

**Chris Osterwood:** Yeah. If you want one at some point it'll exist. Yeah. Okay. You know, and in terms of, there's lots that are, uh, interesting in mobility and, uh, you know, personal mobility, um, especially for people that have a hard time moving around the world. Um, you know, people with physical ailments and, uh, people that are, uh, uh, you know, elderly or have had physical accidents. Um, you know, exoskeletons are really exciting and interesting. And that right now is, you know, sort of, uh, you know, it feels very far off, but it's not going to be that long before we see people walking around with exoskeletons because that's how they can walk around. And without them, they can't walk around. Yeah. Yeah. A huge value there. Yeah.

**Chris Osterwood:** Cool. So what, uh, what, what are some of the challenges you've run into so far as you're, you're building out these, uh, robot components? Oh, uh, time. Yeah. Yeah. Okay. Yeah. Also, it seems like, I mean, like, it seems like you have a wide background, but it does seem like the stuff you're building so far is very electronically focused.

**Chris Osterwood:** Yeah, it is. So yeah, I've, I've learned a lot of electronics in the last year. Uh, you know, the gigabit ethernet switch was perhaps not the best choice, um, to build first from an electrical complexity perspective. Okay. Uh, first version had some issues. Uh, second one's looking way, way better. Good. Um, but, uh, yeah, I mean, that's part of why I chose it was I wanted to expand my technical skillset and, uh, branch out a little bit more. So, um, you know, learning a lot there. Uh, but yeah, you know, my biggest challenge, um, is, uh, this curse that I have of, you know, way too many ideas on not enough time. And, you know, the list of things that I want to build, uh, grows faster than, uh, my ability to build them.

**Chris Osterwood:** Of course.

**Chris Osterwood:** Of course. Um, so yeah, prioritizing and, uh, you know, the normal time management stuff. Um, you know, it's exciting and fun, but, um, it's, it's also hard to be pushing forward on, you know, four different things all at once. Yeah. Um, so yeah, I need to wrap up a few things.

**Chris Osterwood:** Are you, uh, are you actually interfacing with customers like based on known needs? Like, are you doing this based on your knowledge of the market or are you doing this based on like them asking like a set of customers actually asking for a thing?

**Chris Osterwood:** It's both. Um, and I've been learning about, uh, you know, niches in the robotics market that I haven't personally worked in before, you know, so things like, uh, logistics handling, um, you know, picking and sorting and sort of the package management warehouse management, uh, side of things. There's a lot of interesting work happening there. And I see a lot of opportunity in new sensors and new ways of, of moving goods around. Uh, so that's a, an industry that I'm, uh, excited to help move faster. Um, and also, um, you know, there's a whole bunch of things that I'm excited about in camera systems. Um, you know, the, you know, the amount of GPU power that you can put on a mobile system now is phenomenal. And what you can do with that GPU is really remarkable, but there to date still aren't really good cameras that can feed into those systems. And, um, Oh, interesting.

**Chris Osterwood:** Yeah. So it's all like those two megapixel, like raspberry pie cameras, or what are we looking at these days?

**Chris Osterwood:** Yeah. So there's this interesting thing that I've seen in, in a lot of customers where, um, you they, they give you a long list of here, all, all of my requirements. And then you come back with like, okay, to satisfy all those requirements requires this amount of time and money. And the end unit cost will be X.

**Chris Osterwood:** And there's a lot of zeros on X, I'm guessing. Yeah.

**Chris Osterwood:** And they come back a little while later and they say, well, we found something that is X divided by five and only meets two of our requirements. And we're going to go with that. Um, and you know, there's a middle ground where there are, um, there's a place for components that are a little bit more expensive than consumer grade, um, but offer a little bit more functionality than consumer grade. Um, and that's what I'm, that's where I'm aiming and that's what I'm excited about. So, you know, things like the Intel real sense, it's a wonderful piece of technology, a wonderful sensor, you know, it's a low cost, uh, 3d perception system uses active stereo where it's projecting a pattern of infrared dots into the space. And then left and right camera perceiving those dots, just like your eyes perceive texture in the world, generating high density, real time, uh, accurate 3d depth information. But it's really hard to put on a robot because it's not sealed and it's USB three.

**Chris Osterwood:** And, you know, also like how many can you buy at once? And are they actually selling them in quantity and yada, yada, yada?

**Chris Osterwood:** Well, those, those you can actually do. I mean, I've seen production robotic systems with a dozen of them spattered everywhere. Oh, wow. Um, yeah, I mean, they also, they have limited field of view. So you generally need many of them to sort of get a 360 degrees surround view. But yeah, I've seen really big, heavy robots that use lots of those because they're cheap and because you can get them. And, uh, you know, there's, there's a place for a component that offers that kind of capability, but uses better interfaces and a better housing design and costs $50 more. Uh, and people will choose that, but they're not going to choose something that offers a whole bunch more functionality and, you know, a 10 X cost or 20 X cost. Right. You just can't, um, that, you know, that trade-off doesn't, doesn't sell in most markets.

**Chris Osterwood:** Huh. And so like, and how much of it is the mechanical piece? Like, uh, so if you have maybe, maybe that's that level of complexity you were just describing, it seems pretty high, but something like the, the, uh, the USB hub, you know, you talked about switching, you talked about, uh, you know, monitoring and stuff like that, but how much of it is also making it packageable. And, you know, I guess I don't really understand what the mechanical constraints are when you get into the housing of electronics versus the housing of the motors and such.

**Chris Osterwood:** Yeah. So it all depends on the scale of, of the system, but generally something that's using a whole bunch of USB sensors. And I do not recommend people use USB sensors, uh, even though I'm about to start selling a USB based product. It's an in-between product. USB. Yes. Uh, USB is not appropriate for mobile robots. Um, but it's great for many other things, including automated testing of embedded electronics, which is where I'm going to be focusing that USB hub, uh, marketing efforts on. So, uh, but anyway, if you're building a system that uses lots of USB sensors and you're using a USB hub right now, there's generally some kind of, you know, large enclosure that you could open up and has a ton of wires inside and, you know, technicians going in there and rewiring things, you know, and swapping components in and out. So, uh, that component is not going to have a sealed housing and sealed connectors. It's designed to go inside of an existing enclosure that has enough space for it to exist in. Right. Um, but the value that this version, uh, you know, provides, you know, in comparison to something that you would buy from, you know, anchor or Belkin or whatever is locking power connectors, uh, mounting holes, a metal enclosure, higher temp rating power monitoring, you know, and the power monitor chips aren't that expensive, but when you're trying to sell something that has a $5 bill of material, you're not going to spend a dollar on the power monitoring chips. Right. Um, and that's just to tell like if, if it's overcurrent or something like something's wrong, basically. Yeah. And which port is drawing too much power. Right. So the sensor that was drawing a hundred milliamps is now drawing an amp. Uh, something went wrong. Maybe there's a short in the cable. Like let's turn that off. Right. So that the whole USB bus doesn't go down. Um, you know, and also includes a eight amp five volt regulator on board. So each downstream port can draw two amps at five volts, which again, add some costs to the unit, but, um, means that you can basically throw anything you want at it and it'll power it. Yeah. Yeah. Yeah. That's nice. Yeah. There's, um, yeah, there's, you know, with a little bit of additional cost, you can really add some interesting capability. Uh, and the hub chip that I've selected also has a hard fifth endpoint on it that exposes, uh, UART and I squared C and SPI. So, uh, I've put a micro bus header on the, um, on the PCB. So you can actually use this as a USB hub and also a physical world expander. So hook up some sensors to it, you know, hook up relays or an IMU or any other device that operates over your I squared C or SPI. And you can talk to it, uh, through your USB hub without using up one of the USB ports.

**Chris Osterwood:** This is the micro electronica, uh, uh, like 10 pin standard or whatever it is. Exactly. Yeah. Okay. Cool. Yeah. That's a great idea. It's good to make it extensible.

**Chris Osterwood:** Yeah. And there's a whole bunch of different modules available for that. Uh, so a nice way to, uh, offer some flexibility of instead of doing different versions for different customers.

**Chris Osterwood:** Cool. So, uh, I mean, I'm still curious though, about the, uh, the design, like how you're sourcing these ideas is it, so is it, it is, it is like known customers or it's, or it's based on your best past knowledge or what? Or mix? It's both. Okay.

**Chris Osterwood:** Yeah. It's a mix. Um, you know, I've, yeah, I've been in this industry for 15 years now. So, um, built up, uh, you know, a good network of people in all sorts of different little and large, uh, uh, parts of the industry. And, uh, you know, there's, you know, no one, you know, no one building a system really cares about the components that are inside of it. Like they just want to buy and find the right things. You know, they care about the problem they're trying to solve. And, um, you know, if you have a nail and they need a nail, they'll, they'll buy the nail instead of make the nail. Right. Um, yeah.

**Chris Osterwood:** Well, I'm just wondering though, is like, like how you, how you start a conversation like that? Cause I don't think, you know, we've talked about product development before, but I'm not sure we've ever talked about like having a direct insight to a customer like that. Like that's, that's a, that's a very, very valuable thing. I think like you already mentioned that you can ask them everything they want. They might say everything they want, but then, you know, the price balance is there, but like being able to just ask in the first place is pretty valuable.

**Chris Osterwood:** Yeah, it is. Um, and, but you know, there's also this, um, this fallacy, you know, when, when I think about the products that I want, you know, I, I have the same problem where people think they're going to use, uh, features that they don't actually use and that they're not actually willing to pay for. So you have to balance what people say with what everyone else says and, you know, when

**Chris Osterwood:** they pull the wallet out, right. That's right. That's the real, uh, that's the real thing.

**Chris Osterwood:** Yeah. And it's, it's tricky to get them to do that, uh, ahead of time. Right. Um, so, you know, it's a balancing act and you have to definitely use your intuition, uh, and, uh, and, you know, iterate, uh, it's a really big part of this.

**Chris Osterwood:** Um, well, I just wonder too, is like, so one of my friends, it was a sales guy and he used to basically, you know, go to engineers, get them to drop a spec sheet or like a data sheet for a thing. And then he would go and he would actually get sales based on that data sheet. It was kind of insane, but also kind of brilliant, you know, like it was basically selling it before it existed. And then the fact that he sold it, you know, with a very long lead time, uh, meant that it was worth a lot to go build it. Right. And so I wondered if you were doing anything like that.

**Chris Osterwood:** Yeah. I've, I've actually tried that. I've, I've gone to, uh, you know, I mentioned going to, uh, the, uh, factory automation, uh, industry. I went to a trade show there with, uh, six, uh, potential spec flyers to show people and talk about and got some interesting feedback on different versions of different products that I'm considering. And, uh, you know, just get engaging people's reactions, you know, what lights up their, you know, their eye, um, what do they gravitate to? What do they say no about, you know, there's tremendous value in that sort of feedback.

**Chris Osterwood:** Did you bluff though? That's what, that's what I'm really wondering is because as much as I admired my friend for being able to do this, I was just like, man, the stones on this guy. Like, like the fact that like, but people like sales guys do this all the time. Sales people do this all the time, you know? And I can't imagine walking in and being like, yeah, this exists and it's not even close.

**Chris Osterwood:** Yeah. I definitely was not, uh, saying that these things exist. I was saying these are spec sheets for future products. I like, would like feedback on them. I got feedback on them. Okay. That was very valuable. Um, and I think that the, the whole idea of this company, as you say, like, you know, there, there, there isn't an obvious, oh, but these people have done what you're doing. And, um, that's part of why I started with this ether ethernet switch is, uh, it's a way to open the door, the conversation with a potential customer. Everyone knows what an ethernet switch is. And when you say you're making a new kind of ethernet switch that, that perks their interest, you know, wait, what do you mean? How is this different? Like, right. Why do I care about this? Yeah. Why do I care about this? And like, what do you mean you're doing an ethernet switch? Like, what do you mean you're doing a USB hub? Like, but then when you start talking to people about these interfaces, mechanical and electrical and software interfaces that are different on these components versus existing products, then they start to get it and understand that this model can be applied to the problems that they have. Maybe they don't even use ethernet, but it gets them to reconsider what they're buying and, uh, what they're, what they enjoy about that and what they're unhappy with when they're buying or building.

**Chris Osterwood:** Right. Yeah. And I, I, yeah, I think that's actually a really good point too, because at the end of the day, what you're, what you're, if you, if you talk to the person who's actually in charge, right? Like talking to your former self as CTO, you're basically saying to them, Hey, I'm going to save you a crap ton of money. You know, like you could either pay an engineer and, you know, as an engineer, it hurts me to say that, but like, you know, if, uh, if I can buy a component that is four months of my time and it's guaranteed to work the first time, I, it's stupid not to do that. Yeah. No brainer. Yeah. No brainer. Yeah. And then hopefully you deploy your engineers to go do that next thing.

**Chris Osterwood:** That's interesting, but. That's exactly right. And to tackle the really hard problems in that are specific to the domain that you're, uh, facing. Um, yeah, that's the goal of the company is make it easier for people to get to, to market faster and with a system that is more capable and more effective.

**Chris Osterwood:** That's great. Well, it's like, it is, it's in the name. It's in the name. It's in the name. Yeah.

**Chris Osterwood:** Yeah. It was really funny. I've, uh, I spent a long time thinking about names and, you know, the sort of vision and mission for the company. And, you know, in the history of the internet, no one had ever registered capable robot.com. And because to people outside this industry, or this is my guess, at least people outside this industry, that sounds like a low bar, like capable, like why not a fantastic robot robot, a wondrous robot. Right. And the people in this industry are like, oh, capable, like that's what we need. Right. Right. Yeah. Right.

**Chris Osterwood:** I'm not worried. I'm not worried about any kind of revolution here. I'm just worried for the thing to, you know, last its entire battery life. Exactly. And I, I don't want. When I screw the thing together, you know?

**Speaker ?:** Right.

**Chris Osterwood:** And I don't want the connectors to battle loose inside and so on and so forth.

**Chris Osterwood:** Yeah. Right.

**Chris Osterwood:** Um, running out of Loctite. Yeah. Yep. Yep. Uh, they make a good product.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** Oh yeah. Yeah. So there's a, there's a mismatch between like people's perception of this industry and the reality of it in terms of how difficult this is. And, you know, every part of this is tricky. You know, you're making a system that has to interact with people, move around in the real world, bring its own power, be safe, be big enough to actually do something useful. Not kill the humans, you know, like that's important. Yeah. Or the pets or anyone else. Right. Right. And, you know, be small enough that you can maneuver, but big enough that you can actually do something useful. And, you know, it's just a world of overlapping, uh, incompatible constraints. Uh, that's what robotics is. And that's what makes it really fun and exciting and interesting, but also really difficult. Uh, so I'm trying to make it less difficult.

**Chris Osterwood:** Robotics is a world of overlapping incompatible. I'm going to, I'm going to outline eyes this one.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** Got it. There you go. There's the tagline on your t-shirt right there.

**Chris Osterwood:** I guess so. Yeah. But that's what makes it fun. I mean, sure. Sure. That's a whole world of really interesting engineering challenges. Yeah.

**Chris Osterwood:** I mean, uh, where, where do you see, uh, so I'd ask kind of like where you see ground robotics going and that is the term, right? You're saying ground robotics. Yeah. Ground robotics. Yeah. So what about like, uh, opportunities for people that are listening in terms of maybe not necessarily a company they're going to start that is robotics, but like if they're looking for a job, like where, where should they be looking for a job in robotics or like what skill sets would be useful, you know, as a former CTO and like hiring engineers, what would be useful as a, you know, if an engineer walked in the door for an interview.

**Chris Osterwood:** Yeah. So, uh, to work at a robotics company, you definitely need to know, uh, you don't need to know anything about robotics. Like you just need to be an engineer because again, robotics is a combination of all of these different disciplines. So, you know, there, we hired many, many people who had never worked on any robot ever. And they were fantastic because they were working on the embedded software on the safety system or on, you know, the, um, you know, machine learning system or on data management or, you know, whatever else infrastructure needed to exist, uh, to make the system work. Um, and so, you know, similar, um, skill sets in, uh, in electrical engineering, you know, power systems, uh, sensor design. Um, we didn't do much with, with analog circuitry, but, you know, uh, if you lay out a PCB quickly and it works, you are, uh, you're golden, um, you know, interfacing the processors, interfacing the sensors, understanding, uh, communication over, uh, you know, cabling of up to several feet, uh, understanding, uh, radios. Uh, you know, there's a whole, you know, every kind of electrical engineering technology really goes into these systems. You're talking about power management and, you know, uh, high level computing, you know, we built robots that had, you know, M3 microcontrollers and Xeon processors in them and everything in between. So, um, you know, it's, it's just sort of the entire spectrum of electrical engineering, uh, can be encapsulated in robotics, you know, depending on the kind of system you're building.

**Chris Osterwood:** Well, I was just trying to say with the, uh, the amount of compartmentalization that you're talking about too, it sounds like the ability to work with other groups is probably one of the most critical things as well, because you, you're, you're going to be doing some sub

**Chris Osterwood:** piece. Yeah, absolutely. But you can, yeah, but you, you can definitely learn, you know, you don't need to know or have functional mechanical engineering knowledge if you're a software engineer. Oh, no, no, no.

**Chris Osterwood:** I meant more interpersonal and team, team, team player-ishness.

**Chris Osterwood:** You know, that's, uh, yes. Uh, yeah, that is an absolute requirement. You, you're going to be working with the team. Uh, there's no way to build these systems without, uh, a whole bunch of people. Uh, and that's, you know, to me, that's what makes it a lot of fun.

**Chris Osterwood:** So like some, some amount of, uh, like fluency and mechanical doesn't really matter though.

**Chris Osterwood:** No, uh, not at all. Um, you know, just be upfront about what you're interested in and what your, uh, skill set is and what skill set you want to expand on. And, you know, um, yeah, there's, uh, there's lots of opportunity out there. It's a industry that's, uh, hiring, um, everywhere. Um, so, uh, yeah, I'm happy to, to talk to people if they, if they'd like advice on, um, on where to go, where to apply, you know, particular facets of the industry or, uh, places, uh, in the country that, uh, have lots of, uh, companies and activity.

**Chris Osterwood:** Yeah.

**Chris Osterwood:** Uh, there's, uh, there's a lot going on. Yeah.

**Chris Osterwood:** That's great. Well, how do, uh, how do people get a, get ahold of you? And that's probably a good way for us to wrap up here.

**Chris Osterwood:** Yeah, absolutely. Um, so on Twitter, it's, uh, just my last name, Osterwood, uh, O-S-T-E-R-W-O-O-D. Um, and, uh, Osterwood.com, um, is my personal website and the company website is CapableRobot.com.

**Chris Osterwood:** Nice. Well, Chris, thanks for telling us about all this stuff. It's been a lot of interesting, like in zigs and zags in terms of the, uh, the robot industry. I didn't, I didn't quite know what, uh, you know, like what it all involved, but it seems like there's a lot of fun challenges there.

**Chris Osterwood:** There really are. It's a, it's a great place, uh, to be. And, um, I'm really glad I sort of accidentally landed up, landed in it. And, uh, I would definitely encourage people that are looking for interesting engineering challenges to, uh, to reach out, um, and, uh, you know, look in your, you know, your, uh, your local city to see what robotics companies are there. And I bet they're hiring.

**Chris Osterwood:** Awesome. Awesome. Well, we will, uh, people should definitely check out CapableRobot.com and we'll look forward to seeing your next project.

**Chris Osterwood:** Yeah. Well, actually my next project is launching next week on CrowdSupply. Oh, geez. We didn't get to that.

**Chris Osterwood:** Oh man. What's, so what's that?

**Chris Osterwood:** We didn't even talk about that. Sorry. Uh, that is called SenseTemp. Uh, it is a, uh, small four channel, uh, temperature sensor designed for instrumenting electronics. So this is something I've designed along the way, uh, in testing, uh, other products that I'm developing. Uh, it's designed interface to the Adderfruit feather, uh, host boards and provides, you know, four channels of really accurate temperature monitoring and, uh, small RTDs that you can place right on ICs on your board and understand heat sources and sinks and the thermal path and dissipation of whatever component or product you're working on.

**Chris Osterwood:** That's great. That's great. And so that's going to be on CrowdSupply starting next week, you said?

**Chris Osterwood:** Next week. Yeah. Uh, open source hardware, open software and, uh, yeah, designed to be hackable and extensible and integrate with current and future test orchestration software that you may be using.

**Chris Osterwood:** Awesome. All right. Well, people should definitely check that out too. We'll have a link to all these things in the show notes.

**Chris Osterwood:** Thanks so much, Chris.

**Chris Osterwood:** All right. We'll talk to you soon.

**Chris Osterwood:** Thanks. Bye.
