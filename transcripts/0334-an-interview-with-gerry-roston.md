---
episode: 334
title: An Interview with Gerry Roston
url: https://theamphour.com/334-an-interview-with-gerry-roston/
---

**Gerry Roston:** This is The Amp Hour Podcast. Recorded February 1st, 2017. Episode 334. An interview with Jerry Roston.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Gerry Roston:** And I'm Jerry Roston, CEO of Savionics Incorporated, a University of Michigan spin-out and executive in residence at Tech Town Detroit. Welcome, Jerry.

**Dave Jones:** That was a mouthful.

**Chris Gammell:** Yeah, that's a lot of titles. I think we have an experienced engineer here, Dave. That's what I'm thinking.

**Dave Jones:** I think we might.

**Gerry Roston:** That's two business cards, so I don't have to squeeze them all onto one.

**Chris Gammell:** You could do it like they do with the Chinese business cards, where it's like one side's in Chinese, one side's in English. You could do maybe just have one, you know, the flip card, you know. But, yeah, that's great. So, Jerry, what, well, Savionics is a IoT. Is that a swear word for you or no?

**Gerry Roston:** No, well, I like to say IIoT. We're an industrial internet of things. We are not trying to get into the mass consumer market. Instead, we're focused on applying our technology in various manufacturing settings to try to save the manufacturer's cost by reducing downtime, improving quality, et cetera. Awesome.

**Dave Jones:** Okay, so now you're allowed to stay. It's okay. If it was consumer internet of things, not. Right, right. Right.

**Chris Gammell:** Smart toasters, smart microwaves, all that crap, yeah. So, well, let's take a step back before we get to that, because that stuff's actually very interesting. Can we hear a little bit about, you know, where you're from, how you got started in the space, and, you know, what's your backstory?

**Gerry Roston:** Okay, well, it's long and boring. I'm an engineer by training. So is the show. Sorry. I'm an engineer by training, as you have noted. After I did my master's degree, I did my master's in 1985, and back then, computers are not what they are today. They had significantly less capability, and when we were trying to control robot arms, there were two ways to do it. One is what we call kinematics, where you just tell it where to go, and it gets there. And the other is dynamic, where you tell it how to get there from a force perspective. In other words, you say, you know, apply a force in this direction and get there. And the former, mathematically, is very straightforward. It's, you know, just simple trigonometric equations. The latter, though, gets ugly. And back then, ugly meant that there wasn't enough computing cycles to be able to solve the equations. And there was a fellow at the Jet Propulsion Lab who wrote one of the seminal papers on controlling the Unimate 600 arm, which then got renamed 560 for some reasons I never could figure out. And he basically showed that if you have all these big, ugly equations and get rid of most of it, you wind up with something that works. And so what I did for my master's thesis was I went and I studied what he did, and I found that he actually eliminated a little bit too much. And in my master's thesis, I showed that if you kept a few extra terms, and by a few extra terms, it was something like, you know, eight more multiplies and, you know, seven more additions or something like that. Trust me, back then that mattered. Yeah, of course, of course.

**Gerry Roston:** Yeah, yeah, yeah.

**Gerry Roston:** It made a dramatic improvement in the accuracy of the output. And so when I got done with the master's thesis, I sent the paper to Tony and said, I'm looking for a job. And he said, let's talk. And I wound up working at the Jet Propulsion Lab in the robotics group in the mid-1980s.

**Dave Jones:** Oh, we're going to talk about that.

**Gerry Roston:** Yes, we are.

**Dave Jones:** Yes. Yes. So by accuracy, do you mean, is it like one-time accuracy or repeatability to go back and forth, back and forth between two?

**Gerry Roston:** By accuracy, what I mean is the deviation from the full equation. So in other words, if I could have solved the thing fully, I would have had a certain profile. And then by using this reduced form, I was closer to the actual than what Tony's paper had, by a significant amount with those small changes. Okay.

**Chris Gammell:** Hmm. And so it's like an approximation like any other approximation on, like if you're doing fixed point math versus floating point, you have to cut off the term somewhere or something like that, right? Correct. Correct.

**Gerry Roston:** So, you know, work like that. And again, I don't know that they ever referenced my paper, but, oh gosh, what's his name? Um, 30 years ago, a fellow out of Caltech who then went up to Stanford as faculty actually used that approach so that they actually had a Puma 560 arm wiping a piece of glass that was just supported at the two ends. And they could actually wipe the piece of glass clean without breaking it because they had good force control.

**Chris Gammell:** Uh-huh. Okay. Right. So that's the kind of thing you see when you go, like, so I was at IMTS this year and they, they love showing off their robots of those kinds of things. They're always like super accurate. I used to work for ABB too. They'd have like, oh, we're so accurate, blah, blah, blah. But I'm guessing around this time it was, it was a much chunkier kind of approach. Is that the, is that kind of what you're getting at? It's. Oh yeah. Yeah.

**Gerry Roston:** We had, you know, we had some of the very first six axis forced torque sensors on the wrists. Oh wow. The, uh, the Puma controller was made by a company called Digital Equipment Corporation, which might be before your guys' time. No, I know about that.

**Chris Gammell:** I know the stories of deck at least. Yeah. Yeah.

**Gerry Roston:** But these weren't the big decks. These weren't the, uh, the Vaxes. These were actually the PDP series. Oh really? Yes. The PDP 10. Yep. Yep. No, these were PDP 11, 23s and 73s. Yep. Yeah. Okay.

**Chris Gammell:** So like relative size then. So like how much, how much gear would it take to control this robot arm? Is it like, you know, half a room?

**Gerry Roston:** No, it wasn't that big. The PDP 11 box was 19 inch rack mountable, full depth. And by today's standards, and again, I never put a ruler to it, but by today's standards, you'd probably call it an 8U or a 10U.

**Chris Gammell:** Oh wow. Yeah, it's a wrap about that. Yeah. So. So sizable and it kicked off some, you probably cook a, cook an English muffin on top of it or something. Oh yeah. Yeah.

**Gerry Roston:** And it consumes significant amounts of power and had, I think, 64K of RAM or 128K of RAM or something like that. And I bet it was cheap too.

**Dave Jones:** That was pretty much the go-to industrial computer, control computer back then, wasn't it?

**Gerry Roston:** Absolutely. Everybody had those.

**Chris Gammell:** Interesting. Interesting.

**Gerry Roston:** And so one of the projects that I got involved with at the lab was, so one of the problems with robots when you do kinematic control is you say, I want to go to this position in space. You do the reverse, what's called reverse kinematics, and it tells you what angles to set the joints to. And then you set the joints.

**Chris Gammell:** A couple of people just shuddered right there because they probably had to do that in their classes of doing the equations and the solving for the reverse kinematic stuff.

**Gerry Roston:** Oh, that's the fun stuff.

**Chris Gammell:** We're talking about PhD here, folks. You could tell he's a PhD if he likes the math.

**Gerry Roston:** I mean, doesn't everybody like inverting six by six matrices symbolically? I mean, come on. No. Anyway. No. So the thing is, you say where you want to go in space, you do the reverse kinematics, and then you set your joint angles. But you never wind up where you think you are because of errors in the manufacturing and everything else. And there was a faculty member at one of the – it could have been USC or University or UC Long Beach. I don't remember which. Someplace there who wanted to use one of these robots to hold a probe for doing neurosurgery. And obviously accuracy matters. Accuracy matters. Accuracy matters.

**Dave Jones:** It's unit-specific, wouldn't it? Absolutely. Each one would have to be factory calibrated, maybe even recalibrate on site after you move it, perhaps?

**Gerry Roston:** Perhaps. Perhaps. But we went ahead and did that, and the results were good enough that that robot was actually, I believe, the first robotic use of neurosurgery. And that came out of some work that I was involved with at the lab.

**Chris Gammell:** That's awesome. Yeah.

**Dave Jones:** And why is that better than a human? Well, now it – Is it the repeatability and the accuracy, or do they just need so many – like more hands than what the surgeon has?

**Gerry Roston:** A lot of it has to do with accuracy. And back in the 80s, obviously, it was purely research. But nowadays – one of the issues nowadays actually, just to completely go off subject, is that a lot of hospitals are using robots for surgery when they don't have to because of reimbursement rates. Oh. But what's actually –

**Dave Jones:** Reimbursement? What do you mean reimbursement rates?

**Chris Gammell:** Oh, so like U.S.-based healthcare and stuff like that, right?

**Gerry Roston:** Oh, yeah. U.S.-based healthcare, yes.

**Dave Jones:** Oh, because it's cheaper? Does that mean it's –

**Gerry Roston:** No, what it means is that they get paid more for doing it from the insurance companies than if they do it the other way. And since in this country we have for-profit-based medicine, trust me, nobody outside the U.S. understands this because it doesn't make sense to even people in this country. No, no, no. This is far. So –

**Chris Gammell:** But there's more robots because of it, so that's something. Right. Not good or bad. Right. Right.

**Gerry Roston:** But what's going to happen in the not-too-distant future is that they're not going to need the doctors anymore. Really? Yeah. Yeah. They're surgeries which can actually be done –

**Dave Jones:** So they can slice them open, pull it apart, stitch them back up. The whole works.

**Gerry Roston:** Right. You know, take something air quote simple, un-air quote like hip replacement. Right. That's a fairly straightforward procedure that once you have the patient locked in, you really don't need the doctor anymore. You could have the machine do the whole thing. Yeah. And obviously the machine will be repeatable and won't have a hangover, not the doctors ever drink, et cetera. So yeah, it's interesting how that whole field is going. Right.

**Dave Jones:** But isn't there variability in people's bodies and bones? Sure. But that's what sensors are for.

**Gerry Roston:** That's what sensors are for. I mean that –

**Chris Gammell:** Yeah, true. I think it's the psychological aspect. So my buddy is an oral surgeon. He was talking about doing that. He's like, oh, I want to like get robots to drill cavities and stuff like that. And I'm like, look, man, that's going to scare the crap out of some people. You just can't do that. You would have to put everybody under. But like for big surgeries, yeah, of course you would, right? Right.

**Gerry Roston:** I mean it's like airplanes these days. There's no reason that we need pilots in the aircraft.

**Dave Jones:** No, technically.

**Gerry Roston:** Right. Now I take that back. I mean you need the pilots for when unexpected things happen because that's where robots just don't do well. They can't today do things that's unexpected. So the –

**Chris Gammell:** Which is good too.

**Dave Jones:** The problem with that though is that the pilots aren't very good anymore is what I'm hearing is because they're so automated. They don't know what to do in an emergency. That might become the same way with surgery. They rely too much on robotics. Then, well, what happens when shit hits the fan?

**Gerry Roston:** Right. Well, I mean more to the point of the show. That's scary. That's happening with software developers these days. Oh, yeah. Again, as you guys figured, I'm an old man. And back in the day, I actually wrote assembly code. And I remember – So did I. I remember doing a project for a class in my master's program where I wrote self-modifying code. Because again, I was a robotics guy. Every cycle counted and self-modifying code is the absolute most efficient way to do things. Needless to say –

**Chris Gammell:** And one of the best ways to mess things up.

**Gerry Roston:** Yeah, there's that little detail. Yeah. But, you know, the professor had no sense of humor about that. But nowadays you talk to guys who are developing these fancy websites and you say something like assembly code and you get a blank look. Mm-hmm. Yeah. There are some frameworks out there like Laravel, which allows you to build an entire website which is database-driven without ever having to write a single SQL statement because it abstracts all of that. Yeah.

**Dave Jones:** But that's less important because it's not flying – you know, people's lives aren't on the line kind of thing, you know. Whereas, you know, self-driving cars, people's lives are on the line, surgery and all that sort of jazz, planes. Yeah. So – Yeah.

**Chris Gammell:** And I think people dive down through the abstraction when they need to these days too. Like with the timing stuff, you need to have the timing perfect for – so like the people writing assembly still are the ones doing the low-level driver stuff. But then that gets pushed up the chain, right?

**Gerry Roston:** Right. And funny you mentioned drivers because after I got done with that project, I started – I moved over to start working on some of the extraterrestrial exploration projects that we were working on at the lab. Really? Yeah. And –

**Dave Jones:** That's a nice name. What's that name on the door?

**Gerry Roston:** And so I learned how to program C back in 1986. And the very first thing I ever did in the C programming language was write a real-time device driver so that we could interface a PDP 1173 that was running a system that came out of McGill University. Vince Hayward put it together. And we had to interface it with our VAX. And we had a custom FIFO card on both sides. And again, the first thing I ever did in C was write that real-time device driver. That it worked amazes me to this day.

**Chris Gammell:** That's how I feel about my code most of the days. But yeah.

**Dave Jones:** So let's talk JPL.

**Chris Gammell:** Yes. And when you said – sorry, one step back. When you said lab, so I'm looking at your past. Was that – which school was that at that lab was?

**Gerry Roston:** That was at the Jet Propulsion Lab, NASA.

**Chris Gammell:** Oh, that was at – okay, great.

**Gerry Roston:** Great, great. Okay. So we're already there. Okay.

**Dave Jones:** Yep. So you were chosen as the first member of the Mars rover team.

**Gerry Roston:** Yeah. Well, what happened was my – the guy I was working for, Brian Wilcox, who was my manager, was a very savvy guy. And one of the things that disappointed me about JPL was how political it was. Really? Yeah. It was very political at the time. We would have arguments over who gets to develop which part of a system. Where do we draw the line? But Brian was very savvy. And he came up to me one day and he said, Jerry, I have a box here with six gear drives and two worm gears. Mars rover project is coming. Build me a robot so we can have lead on it. And – Oh, nice.

**Chris Gammell:** Start with the prototype, right? Yeah. It's easier to say. Yeah. We already started.

**Gerry Roston:** If you Google Robbie the rover, you will find a picture of Robbie online someplace. And so that's the robot that I built. And that's the robot that all of Sojourner's software was originally developed on. Wow.

**Dave Jones:** Sweet.

**Chris Gammell:** Wow. And so –

**Dave Jones:** So was it advantageous to have that prototype to take the meetings and show, hey, look, we've got something. Pick us. Pick us.

**Gerry Roston:** Yeah.

**Dave Jones:** Is that the –

**Gerry Roston:** Yeah. Well, JPL was the lead on it. But Brian was able to bring most of the work into his group. And then he brought on people like Andy Mishkin who actually wrote a book about this, Donna Pivarata. That's not her name anymore. She got married. I forgot what her new name is. She was sort of the overarching program manager. There was a fellow out of headquarters by the name of Mel Montemurlo. So, you know, the whole thing obviously got quite large when it – you know, as it progressed and as it became an actual flight mission. But we got it all kicked off. You know, in Brian's lab. That's where it all started. That's great.

**Dave Jones:** So what platform, what hardware are we talking about? What process are we talking about for the Sojourner rover? Which I presume your one was the same?

**Gerry Roston:** No. Robbie, it was the terrestrial prototype, if you will. It wasn't even mechanically similar.

**Dave Jones:** But you said you developed the software on it.

**Gerry Roston:** Right. Yeah. So all of the high-level software, the planning stuff.

**Dave Jones:** Oh, okay. Right.

**Gerry Roston:** So Sojourner, for example, used a 3D display. Had two cameras. They would come back. You'd use – we used cross-polarized glasses so that you could see 3D. And the driver would use that image to pick points on the map of where the rover should go. And then it would just go straight line between those waypoints. But all of that was originally developed on Robbie. And all of the testing was done in the Arroyo right outside of the lab.

**Chris Gammell:** Hmm. Dave knows space history much better than I do. Could you explain the Sojourner, too? I actually don't. Yeah, that was before you were born, I think, Chris. I get that stuff. I don't actually know the history of that as well.

**Dave Jones:** It was the first one. It was the first of a proposed fleet of robots. Was it Mars Rovers? Was it not?

**Gerry Roston:** Yes. Yeah, it was followed –

**Dave Jones:** Well, the first one that made it.

**Gerry Roston:** Yes.

**Dave Jones:** Yeah. And the guy who – As in funded and –

**Gerry Roston:** Yeah, the guy who drove it off the lander was Brian Cooper, who was a buddy of mine. And so he's actually the guy who drove it off the lander when it hit the surface.

**Dave Jones:** How much fun would that be? And it's not real time. It's not like you're watching the – Right, it's like push the joystick, you know. It's like go forward the four steps, right? Like, you know, it's – Like, I'm sure it takes a day of, you know, meetings and everything to figure out, okay, we're going to move it half a meter down the ramp, you know.

**Chris Gammell:** Yeah. Yeah. And how did that land – was that the – I remember the one that bounced. I remember that one. Airbags. Yeah. Was this the same thing?

**Gerry Roston:** I don't remember what the touchdown procedure was for Sojourner. I had left the lab by that point. Okay.

**Dave Jones:** Yes, it was. It was the airbags. Okay. You'll see them in the photos deploying. The early ones, because they didn't weigh much, they were tiny Rovers, you know, like they easily fit on your desk there, you know, small little Rovers. And they didn't weigh much, so they could use the airbag system. That's why they didn't use it for the Curiosity Rover, because it's the size of a small car that weighs 1.5 tons, you know. So they just – like, you couldn't make the bags big enough to absorb the impact. So they had to use the Skycrane, you know, power descent thing. But these were small enough that they figured, oh, yeah, we can just bounce it. And, yep. And it was.

**Chris Gammell:** So, Jerry, I'm looking at the picture of Robbie the robot, and we'll link it in, too. I mean, it looks like, like you said, it has some arms, some cameras, stuff like that. But, like, when you build something like this, what do you go and actually – what do you usually test for it? I mean, like, is it just proof of concept or –

**Gerry Roston:** Yeah, that was – again, that one was really for developing the navigation software. So we needed a platform. You know, the thing on the back, there's a 3.5-kilowatt Honda generator, and that's there to power the VAX computer that's in the middle compartment. And those are ATV wheels that I found at some shop someplace in the area. Oh, man.

**Chris Gammell:** So you're like a space prototyper. This is even cooler.

**Gerry Roston:** Yeah.

**Chris Gammell:** And so – and what timeframe is this, too?

**Gerry Roston:** This was – this would have been 87-ish, 87, 88. Okay.

**Chris Gammell:** And so, I mean, like, computers were obviously improving, but this was still VAX. I mean, I don't know what the VAX ran on, but –

**Gerry Roston:** This was pre-Windows. This was pre-Windows, even. Yeah, right, right. The AT came out in – the PCAT came out in 85 or thereabouts, and then in 87 or 86, we upgraded our lab to Sun workstations, the 3-slash-50s. Nice. And they were really spectacular because they had, I think, four megabytes of memory, which – Hey, hey. Oh.

**Dave Jones:** What a beast.

**Chris Gammell:** I don't miss those days at all. I know I wasn't doing much back then, but I even still, like, man, I'll take as much memory as we can get these days, you know?

**Gerry Roston:** And, of course, that wasn't a single chip.

**Chris Gammell:** That was – No, no. That's an array.

**Gerry Roston:** A full quarter of the motherboard. Yeah, it was something.

**Chris Gammell:** Wow. Wow. That's crazy.

**Dave Jones:** Oh, beautiful.

**Gerry Roston:** Yeah, and then from the lab, I then moved to Carnegie Mellon in Pittsburgh and joined the field robotics center there and stayed in the space robotics arena. So the focus there was actually more on walking robots because one of the challenges with wheels and unstructured terrain is that you come across obstacles that are hard to surmount. And one of the two rovers, I don't remember if it was Curiosity or Discovery, actually, I think, got stuck because of the soft sand and it wasn't able to get out. Oh, right.

**Chris Gammell:** Right.

**Gerry Roston:** Yep. That's crazy.

**Dave Jones:** Yeah, I think – Yep. So when – It's still stuck there spinning its wheels. Yeah. Oh.

**Chris Gammell:** Sad. I always get so sad when I think about – there's an XKCD about that where it's just like the robot keeps thinking that it's going to go home. I know it's really stupid anthropomorphized, but I get so sad. It's like these little explorers. It is.

**Dave Jones:** It's like in The Martian, the movie, right? Yeah. You know, that – it's a sad scene. Like he digs up the rover covered in sand, you know?

**Chris Gammell:** It's our science history. It's buried on another planet. It's crazy. Whatever happened to Robbie the robot?

**Gerry Roston:** Do you know? I don't know. I know that some of the earlier robots – we were – there's a museum in Boston called the Boston Computer Museum, and it's right next to the Boston Tea Party on the – what is it called? South Bay there. Ooh. And we actually –

**Chris Gammell:** You know, a little bit of – a little fun fact for you. One of my relatives was throwing tea off of that boat.

**Gerry Roston:** So they actually came and asked us for some of the old robots. I remember prepping a couple of the really, really old ones, which went out to the museum there, but I have no idea where Robbie wound up.

**Chris Gammell:** That would be great to see like one of those – you know, like the evolution of man, that image of like the monkey, like growing up in the man. Right, yeah, yeah. But like with robots or something. That would be interesting to see. Yeah, the same image. Yeah. Yep. So it – That's awesome, though. I mean, and so it had a 3.5 kilowatt generator. It was lugging around a VAX or PDP, whatever – man, that's got to be – that's got to have some curb weight, huh? Yeah.

**Dave Jones:** That's terrific. Do you know how many people in the end, how big the group was who worked on the rover? Not your one, but the actual lander?

**Gerry Roston:** Well, I mean, when you get to a flight mission, it's – I don't want to say a cast of thousands. I don't know that it's that large, but – But it's – It's significant because, you know, they wind up outsourcing a lot of the manufacturing. It's all custom electronics and computing at that point. Yeah. So quite a few people had their hand in that final project. Yeah.

**Dave Jones:** And how many of them do they build? Just two? One flight hardware? And is it an identical one for ground?

**Gerry Roston:** Again, I don't know what they did, but that is what they – you know, that is typically done where they would build a second one for ground, yes.

**Chris Gammell:** Mm-hmm. Yeah. Right. And so I'm looking at the picture here of Robbie the Robot as well. And, like, are these – they're not stepper – are they servos? Are they steppers? Are they –

**Gerry Roston:** Those were servo motors on there.

**Chris Gammell:** Okay. Yeah. So – but did you have to, like, then go and build your own stepper drivers and everything like that too? I mean, like, I kind of take that for granted these days. Yeah.

**Gerry Roston:** No, we – oh, boy. Now you're asking for details. When was – no, that was – Sorry. No, no. I think back then we were using – yeah, so what we were doing back then is we were using single board computers based on the VME bus. Uh-huh. Oh, cool. And so I believe that what was in the rack was a VME-based computer, and we had a tether going back to the VAX and the lab for the high-level control, and the VME computer was running Wind River Systems VXWorks real-time operating system. Oh, yeah.

**Gerry Roston:** As a matter of fact, we were – Jerry Fiddler, who was the founder of the company, is the one who actually came down to make the sale to us, and we were one of his first major customers.

**Chris Gammell:** Wow. And look where they are now. That's crazy. Yeah.

**Gerry Roston:** Yeah. And – but what's crazy is that entire VME computer, which is this, you know, 19-inch rack mount, you know, the –

**Chris Gammell:** Right. Single board. They mean a whole board, right? Yeah, whole board. And Dave, you might remember – No Raspberry Pis here, folks.

**Gerry Roston:** The connectors on the back were, what, 120 pins, and there were two of them, I think? Yeah.

**Dave Jones:** They were – oh, God, what's the number? The 61410.

**Chris Gammell:** The type of the – yeah, I know what you're talking about.

**Dave Jones:** Yeah, the type of the connector. Yeah, 100 pins?

**Gerry Roston:** Yeah, I was thinking 120, but whatever, a large number. All of that these days you can buy on a microcontroller chip from a microchip for $2.50.

**Chris Gammell:** Yep.

**Gerry Roston:** Yeah.

**Chris Gammell:** That's nuts. And run it on a AA battery. Yeah. It's a different world. It's better. I'm just saying, you know, it's better. But the work you did obviously led to that, so that's great. Yeah. So, yeah.

**Dave Jones:** So, robot – so, arms. Can I ask about arms again and the kinematics and going there and, you know, moving from one location to another, accuracy, all that sort of stuff? Does – like, do you have sensor feedback, of positional feedback?

**Gerry Roston:** Yeah, absolutely. All of those robots had optical encoders on the joints.

**Dave Jones:** To make sure they're not slipping, of course. So, you know exactly how many steps you've moved.

**Gerry Roston:** Well, they weren't steppers. They were servos. So, you'd have a closed loop control around the position. The one thing that, you know, people tried to do many times was to basically time differentiate that encoder signal to get a velocity signal. But differentiation is a very noisy process. And so, the results from doing that were always a mixed bag. Interesting.

**Chris Gammell:** Yeah. So, you're saying, like, if from one step to the next on the encoder, trying to just measure time of – the time between them and if there was a little bit of variation in the print or something?

**Gerry Roston:** Yeah. Normally, what you would do is you would measure the number of steps over some period of time as opposed to the time for a single step. But, as I said, it's a – differentiation is a mathematically noisy process versus integration, which isn't. So, you know, that's why you can do things with accelerometers and integrate them to get velocity and position and not have it suck terribly.

**Chris Gammell:** Yeah. But that's still not super fun. That's – yeah. Your boat will – my buddy did that with a boat where he's like, yeah, I'm going to use an accelerometer to know how far my boat drifted. He's like, I don't know where my boat is. Well, yeah.

**Gerry Roston:** Yeah. It depends on the accuracy and everything else. I've seen cases where – god, what project was that on? Some project where we were doing accelerometer integration and we were drifting by, you know, meters per second. Oh, wow.

**Dave Jones:** Which I guess matters if you're doing – it probably doesn't matter too much for space-related stuff, but for terrestrial stuff.

**Gerry Roston:** Yeah. No, it does matter and that's why you have to correct that. I mean, if you're doing stuff like that, you always want some sort of independent way to basically recalibrate your system.

**Chris Gammell:** Yeah. Like sensor fusion stuff that happens these days, right? Yep. Exactly.

**Dave Jones:** That's cool. Is there any other way to – you know, if you've got a robot arm that has a point on it and, you know, it can go anywhere in its three-dimensional envelope space, is there any other way to get feedback of the position of that? Can you do it – like can you add additional sensors to, like, optically sense where the end of the probe is, for example? Sure, absolutely. Any sort of – can you explain some different methods to augment the accuracy, I guess, or maybe verify the accuracy of what those optical encoders are telling you?

**Gerry Roston:** Right. You know. And what you mentioned, you know, doing something optically, you know, again, has been done for a very long time. You know, basically you put cameras in the field of view of where you want to go. Typically, you calibrate the cameras ahead of time.

**Dave Jones:** And they'd have to be stereo too, at least, wouldn't they? I mean, you can't just use a single camera to – Again, it depends on what you're trying to do. What the surface, yeah. But I'm talking about sort of like anywhere in three-dimensional space kind of thing.

**Gerry Roston:** Then you would want two cameras to get stereo. Obviously, if you have a third, you can do a better job. Yep. But, yeah, you use the cameras then, which are calibrated, to basically reverse map where that point is in three-space. And then you can use sensor fusion approaches. For example, something like a common –

**Dave Jones:** Sensor fusion. Right. That's the phrase of the week.

**Gerry Roston:** Yeah, so something like a common filter allows you to take measurements from different systems with different accuracies, if you will, and put it together. And what's interesting about using approaches like that is the accuracy that you get out of the fused is actually better than the accuracy of either of the things coming in, typically. So it really does give some attention.

**Dave Jones:** Yeah, it depends on the uncertainties and everything else. Yes. But, yeah. Yeah. It can be. And the more you've got, the better. Yep. Potentially. Yep. The more sensor sources.

**Chris Gammell:** Yes. So you've been in robotics a long time. When did you see this? I mean, so was this kind of – like, was the sensor fusion stuff happening even on the Robby into the field robotics center? I mean, is that –

**Gerry Roston:** Well, back at JPL, one of the projects we worked on was a – it was going to be a free orbiting multi-robotic arm platform for doing satellite repair.

**Gerry Roston:** And we actually had this thing locked up in the lab where we – Sweet. We built a satellite. We built a satellite. It was basically six solar panels that I found and I, you know, arranged them. I don't remember how I did it, but, you know, made them in a hex shape. And we hung it from the ceiling with a counterweight to go up and down and spin around and whatnot. And we had – gosh, we had two Puma arms which could reach out and grapple this thing as it was spinning. And we had another Puma arm with a stereo – with a pair of cameras on it which would capture the position and, you know, extract the velocity of this so the other arms could actually go out and grapple it.

**Dave Jones:** Fascinating.

**Gerry Roston:** That work was led by Don Jennery who was one of the early guys in computer vision, a tremendously bright man.

**Dave Jones:** Are they still looking at doing – because space repairs are done by humans at the moment, aren't they?

**Gerry Roston:** As far as I know, yes.

**Dave Jones:** Yeah, they're still done. I mean, you know, they have the robotic arm, but that's only for, you know, sort of deployment and retrieval type stuff.

**Chris Gammell:** Well, imagine like a surgery day where the patient doesn't die. They burn up in the atmosphere if you mess up. Right. Yeah, having a human there is nice.

**Dave Jones:** Which is worth a lot more money. Humans are cheap. There's plenty of us around.

**Chris Gammell:** I didn't realize – so I was just looking at Puma arm, Jerry. I didn't realize that's actually an acronym, Programmable Universal Machine for assembly. Yep. Yep.

**Gerry Roston:** And that came out of Unimate, which was Engelberger's company. And that was one of the – I think maybe even the first commercial robot company in the world, maybe.

**Dave Jones:** It was, I believe. Yeah.

**Chris Gammell:** Yeah. That's great. That's really cool. So, well, tell us about the robotics center at CMU. So that was where you went to go do your PhD. Is that right? Yes.

**Gerry Roston:** Yep. And so while there, my focus was on walking robots. You guys might know – I think it's called Boston Dynamics these days. Mark Raybert's company. Yep. Yep. He was at Carnegie Mellon. And then he left and went to MIT. I was in Red Whitaker's group. As I said, my focus was on the terrestrial robots, primarily statically stable walking machines. But it was the field robotics center at Carnegie Mellon that actually invented most of the automated driving technologies that are now being commercialized.

**Chris Gammell:** That's right. And then they hired away the whole team. They hired away the whole team. Those are all my colleagues that got hired away by Uber. Really? Yep. Yep. That's crazy. Yeah, we were the first – Right, Uber? Yes. Yeah, Uber. They hired them all the way, Dave. Uber. The entire department.

**Dave Jones:** As in the car company? Yes.

**Gerry Roston:** Yeah, because their biggest cost right now is the drivers. They want to get rid of them.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, okay. I didn't know they were getting into that. Oh, yeah. That's such a big thing. Yes, of course they are. Yeah, yeah, yeah.

**Chris Gammell:** Do you remember when Uber switched from – I remember my friend pointed this out. He's like, remember when the Uber driver stopped asking you where you're going and you're just putting in the address directly? It's like, basically, that's the first step towards removing the driver entirely. Because you never have to talk to anyone at that point. You just get in and it goes. Yep. So, that's crazy.

**Gerry Roston:** Wow. So, we were the first group to ever drive a vehicle autonomously using GPS control. Really? Oh, wow. And when we did it, the GPS constellation wasn't complete. So, we actually had charts up in the lab so we would know when we would have four satellites in view. Yes. Yeah, yeah.

**Dave Jones:** And if you get one satellite right on the horizon, it can throw you out. You actually want to ignore that puppy. You know? Like, it's – I come from a geocaching background and many a time I've stood between a tree and a satellite. I can see the satellite map and I'm like, right, I'm blocking that bastard out. It's affecting my accuracy. So, yeah, you would like – you would block the thing out.

**Chris Gammell:** And was this before the – did you guys have access to the full resolution? I forget what it's called. Dave's talking about it before. No, no. It was the degraded resolution.

**Dave Jones:** Selective availability.

**Gerry Roston:** Yeah, it was the degraded resolution. So, we would normally have two antennas on the vehicle and you would take – you basically did a – I don't remember what we called it, differential GPS or something like that.

**Dave Jones:** That's the wide area augmentation system, the WASS or whatever.

**Gerry Roston:** Yeah. Yeah.

**Dave Jones:** That just allows you extra – they have local transmitters as well as the satellites that allow you to get additional accuracy. I'm not sure if they're still using that or not.

**Gerry Roston:** Yeah, no, this was before that. This was basically just getting two signals from the satellite because of the way they mucked it up. If you had two of them, you could actually improve the accuracy because some of the noise would cancel basically. Oh, really? Yeah. That's interesting. Yeah, but now they've done away with that. I mean they've – I think everybody can get the full accuracy these days.

**Chris Gammell:** Right. Yeah. I'm guessing your antennas are probably a little larger than most cell phones these days too, huh? Oh, yeah.

**Gerry Roston:** Well, the original vehicle was the Humvee. Uh-huh. What do we call it? Like the big one, right? Take a look at – you can Google NavLab and NavLab 2. NavLab 2 was an ambulance model Humvee. And the reason we needed the ambulance model was the entire back of it was packed with computers and there was room for a couple of researchers to sit there. Oh, man. And it would creep along at a mile an hour type thing.

**Chris Gammell:** Uh-huh. That's awesome. Oh, wow. This is a big car.

**Gerry Roston:** Yeah. That's – you know, originally then they got it out on the highway and I assume the statute of limitations is elapsed. But we were also the first group to ever exceed the speed limit. Yeah, because you guys were breaking the law, right? No, we were the first group to exceed the speed limit under autonomous control on a public highway.

**Chris Gammell:** Jerry, there's agents outside your house right now. This has been a sting operation. That's why we needed to know where to send a microphone.

**Dave Jones:** So what is your whole take on this autonomous car revolution? Like, do you think it's going to be as easy as what a lot of people claim? Because I don't think so. I think there's going to be a lot of small issues which – I'm not going to say are showstoppers, but are really going to put a kink in things.

**Gerry Roston:** I think there's really only two big technical issues. And I think one of the technical issues is what happens when you have some vehicles that are autonomous and some that aren't. Because one of the things that you can do with autonomous vehicles is you can do convoying, which greatly reduces fuel consumption for the trailing vehicles and everything else. But when you have non-autonomous vehicles in the mix, you have problems. I think the other real issue is the – what to do in the edge cases. So when the kid – if a kid runs out in front, do you slam on the brakes to save the kid or do you – Yeah, yeah, yeah. And all of those – Rugged ethics. Yeah. Right? Yeah. So technically I think those are the two big problems. I think the much bigger problems are social problems. Yes, totally. In this country, if we have real autonomous driving, we put four million truck drivers out of work.

**Chris Gammell:** Right, right.

**Gerry Roston:** And that's a lot more jobs than have ever gone overseas by the Mexicans or the Chinese or anybody else that Trump wants to blame. Most of those jobs are actually lost to automation. Yeah. And we need to see nothing. I think automation is going to be a huge piece.

**Dave Jones:** The truck drivers is where – like truck haulage is one of the almost ideal – one of the best case scenarios for autonomous stuff. Yeah. Because they can just keep driving all day, all night, and they typically drive in the middle of the night. You know, there's less issue.

**Chris Gammell:** Right. They talk about the last mile where like when you need the human in the loop, you just do it right when the delivery happens. All the highway stuff is taken out, and then you can convoy, like you said, make a train effectively.

**Gerry Roston:** Right. And then think about what happens when we don't need taxi cab drivers anymore. Joney cab. Right. Think about what happens when we don't have to own our own vehicles because when we need to go someplace, it shows up. And what does that mean about –

**Chris Gammell:** Actually, I don't have a car anymore. That's what I do. I just use Uber and public transport. Right.

**Gerry Roston:** And what happens to the parking lot? So, I mean, the societal implications are huge. And unfortunately, with the nonsense that's happening politically in this country right now, we're missing all of the important conversations and focusing on nonsense. And we've got this tidal wave of change coming that we're just not ready to deal with.

**Chris Gammell:** Yeah. That's going to be a big one, the job stuff for sure. I think that's going to be – we've talked about that a bunch of times on the show too. I think it's just –

**Dave Jones:** So, what's your idea of timelines? How do you see this playing out?

**Gerry Roston:** That's a good question.

**Dave Jones:** Have you thought about it?

**Gerry Roston:** You know, I haven't really – you know, again, technically, most of the pieces are in place other than some of the issues. And to your comment about the last mile, yeah, we could have convoy – I mean, right now today, with very little risk, we could have trucks convoying, put a driver in the lead vehicle and have them convoying 10 trucks behind. That could be done today.

**Chris Gammell:** I didn't even think about that. Yeah. Right. Of course you just –

**Dave Jones:** Until some idiot tries to go, right, I'm going to – I'm not aware these are autonomous. I'm going to merge in the middle of these huge big trucks, you know, and it's like – yeah.

**Chris Gammell:** But still, that's disrupted right there. I mean, that's – I never even thought – I always thought like full autonomy right away. But yeah, that kind of mixed mode. That's kind of like the – you walk into a CVS and now there's two cashiers and 20 – Automated ones. Automated ones, right. Yeah. Instead of 10 automated or whatever, right? That's crazy. Yeah. Wow. That's really crazy.

**Dave Jones:** But like I don't see – like a lot of people saying, oh, it's going to be all over in five years. It's like bullshit. No. You know, like there's – no. It's going to take a generational change. So it's a 20-year thing. It's, you know, at least I think.

**Chris Gammell:** Well, from the society aspect, you're saying.

**Dave Jones:** Yeah. Yeah. Oh, totally.

**Chris Gammell:** Yeah.

**Dave Jones:** The way you think people are just going to give up their cars and get an autonomous car. Yeah. Sign me up.

**Chris Gammell:** I'm ready right now. I can go – I'm going to go to the bar. Yeah.

**Gerry Roston:** It is a generational thing and, you know, a lot of it will be driven by electric vehicles because in a city, electric vehicles make a lot of sense. Totally. You know, when you get out into Kansas or Montana or, you know, the middle of Australia. In the middle of whoop whoop. Yeah. Right. You still need gasoline. And so even though you can do that autonomously, the refueling is going to be trickier. So you might still have some drivers for some of those situations. But in the cities, yeah, it might happen – even though the cities are technically more challenging, it might happen faster because the need is greater. Yeah. In some sense. It could.

**Dave Jones:** Yes. Yeah. I wouldn't disagree with that. But, yeah, it's not going to be as quick and easy as people think.

**Chris Gammell:** So you were working on this kind of stuff at FRC, which is not First Robotics in this case. We did mention that before the show. But at the Field Robotics Center. So this is your PhD. How far did you take it? I mean, like, were you – was that part of your thesis? Well, my PhD – Thesis?

**Gerry Roston:** My PhD actually wound up being about meta design. Basically, my PhD dissertation was a method. It was based on genetic programming to design physical objects. Oh.

**Chris Gammell:** I think I've seen stuff about that before. Yeah. Like –

**Gerry Roston:** Yeah. So, you know, I actually wrote some – I wrote a program to optimally design a walking robot to go – to walk across a random field. And I also co-evolved the controller for it. So it evolved the body and the mind at the same time. Obviously, very simplified representation. But that's what my dissertation topic was.

**Chris Gammell:** Oh, wow. So is someone going to be blaming you for, like, the robot uprising at some point? Yeah. Yeah.

**Gerry Roston:** I mean, Skynet. You know, honestly, when that movie first came out, I was very concerned about that. But it's been long enough ago, so I don't think they'll blame me.

**Chris Gammell:** Oh, okay. Good. I was going to say – or maybe six years of doing a PhD beat it out of you. You're like, this is so hard. No one's ever going to figure this stuff out.

**Dave Jones:** Well, there's some very high-profile people, you know, Stephen Hawking and others, warning about the, you know, artificial intelligence and everything else getting out of control. Do you see that actually being a problem?

**Gerry Roston:** You can argue it either way. You know, and again, I haven't been – you know, for the last 10 or 15 years, my focus has been on startup businesses and things like that. So I haven't been as engaged in the dialogue as I was previously. But I think you can make the argument either way. Either it can go out of control or it can't. And at this point, I just don't think we know enough to be able to know which way it's going to come down.

**Dave Jones:** Well – I'll hang my things on the chopping block. I'm going to say it's not going to be as big a deal as people think. That's Dave's favorite thing to do.

**Chris Gammell:** We should also say it. Dave loves going against the predictions. So, yes, he likes saying I told you so.

**Dave Jones:** No, the doomsay. I don't think it's where – so far – you know, people say, oh, once you reach a critical – what's the word? The critical point in the computer, you know, it gets more powerful than the human brain, et cetera, or 100 times more powerful, blah, blah, blah. Yeah, singularity, you mean, Dave? Yeah, the singularity thing or whatever it is. You know, it'll just magically happen. No, I'm sorry. It's not going to just magically happen. But we're not even close to have it magically happen.

**Chris Gammell:** I have to say, I know you said you're not going to be in charge of the robot uprising, but your next thing on your docket here, cybernet systems, I'm just saying. Well, we're not close.

**Speaker ?:** Yeah, yeah, yeah.

**Chris Gammell:** I saw that. That's a little close.

**Gerry Roston:** Well, let's not talk about that. That was – you know what they say. If you can't say something good, don't say anything at all. So let's just leave that one behind. Okay, we'll just let that go. Right, okay.

**Chris Gammell:** So let's move on to the startup stuff because that's also very interesting, and we want to hear about your current company too. So how did you bounce out? I mean, so you got your PhD, you bounced out of there, and then what?

**Gerry Roston:** Well, you know, one thing I learned, and maybe I can credit cybernet with one good thing, is that – and this might sound strange, but it turns out that technology after a while becomes easy because if you set out to solve a problem using technology, if you're good, you know at the very beginning you're going to be able to solve the problem, and then you just do it, and you go, okay, I've solved this problem. And honestly, after a while, just doing the technology became boring to me, and one of the things I discovered, and maybe it's because I'm an engineer, is that I don't understand people. And every interaction with a person is unique and different, unpredictable, and a whole lot harder to deal with. And so since I like –

**Dave Jones:** So messy. I don't – yeah, I hate dealing with humans. Yeah.

**Gerry Roston:** So I became more interested in that, and again, because of my background in robotics, again, back in those days, we were jack of all trades. You know, you had to do the mechanical stuff, the electrical stuff, the programming stuff, et cetera, et cetera, et cetera. And that was very well suited to startups. You know, I worked for a couple of big companies, and, you know, they try to pigeonhole you to doing one thing, and that did not work well.

**Gerry Roston:** Right. And I sort of migrated to the startup space. I've earned an MBA from the School of Hard Knocks in doing startups.

**Chris Gammell:** Yep, yep.

**Gerry Roston:** But it's a heck of a lot of fun, constantly learning, constantly doing new things. So for today, for example, I wrote a marketing piece. I talked with a supplier. I talked to my CTO about some ideas for product expansion. I took care of some financial stuff in QuickBooks. You know, typical day for an early-stage startup CEO. It's one thing after the next. Right, right. You're doing everything.

**Chris Gammell:** Yep, yep, yep. And you had enough time to talk to us, so that means you're doing something, right? I mean – Well, that means I'm skipping dinner. Oh, okay, sorry. But, yeah.

**Gerry Roston:** Civionics, which is a University of Michigan startup, is an industrial Internet of Things company. And basically what we do is we put intelligent wireless sensor nodes on pieces of manufacturing equipment. We extract information from the sensors. And then we look for changes in the information that's coming back that might suggest that there's a current problem or potentially a future problem with that equipment. And then we can alert the plant personnel that this is happening so they can then take corrective action before there's a downtime.

**Chris Gammell:** Right.

**Dave Jones:** Interesting. How are you powering these sensors?

**Gerry Roston:** I'll answer that in one second. So, for example, in southeast Michigan, we have a lot of automotive. Yes. And that's our first customer is one of the big automotive companies. And we're on several stamping lines in one of their plants. And what I've come to learn is that if one of –

**Dave Jones:** As in stamping metal parts?

**Gerry Roston:** Stamping metal parts. Right. Like the beds of pickup trucks and hoods and things are big stuff. Stamping machines are amazing. Those things are so fun. Yeah. So these stamping lines, every one of them that they have represents about 2% of their entire North American stamping capacity. Holy crap.

**Dave Jones:** Wow. Wow.

**Gerry Roston:** Yeah. And they're 50-year –

**Dave Jones:** They're a big deal. Yeah. If those things go down. Yeah.

**Gerry Roston:** Yeah. Yeah. It's – Yeah. The lost revenue is about a million dollars an hour if one of these lines goes down.

**Chris Gammell:** Oh, yeah.

**Gerry Roston:** Yeah. Yeah. Okay. And the equipment in many cases is 25 and 30 years old.

**Chris Gammell:** Yeah.

**Gerry Roston:** And it doesn't have sensors. So, you know, we've been on some of these lines. We've been credited with saving them three downtime incidents since we deployed a year ago. And that's only on two of their, you know, dozen or so stamping lines. Wow. And so they're quite pleased with it.

**Dave Jones:** How can you convince them to stop it for an hour so you can attach the damn sensor? We don't.

**Gerry Roston:** We don't have to stop. So right now – We're inside the stamping thing, right?

**Chris Gammell:** It's not like you're slipping your hand in, slipping your hand out. Here it comes. Here it comes. Quick.

**Gerry Roston:** Slap it on. Well, so two answers to the question, Dave. First of all, they normally only operate 20 out of 21 shifts a week. So normally – Oh, okay. Yes. Third shift on Sunday morning is available. Third shift, of course, starts at 2 a.m. And it's no fun to be at the plant at 2 a.m. Yes. Been there, done that. Yeah. Yeah. So there's that. And we're not on the dyes yet. But at some point, you know, we probably will have some sensors on those. And so that gets back to your question of how are you powered? And a lot of our stuff right now is battery powered because in a situation like this, we're not talking about closed loop control. We're talking about degradation of systems. So these are things that happen over longer periods of time. Long term.

**Dave Jones:** Yeah. So you just like – It's like a heartbeat almost. Like five times a day, it just pings back. And then you – Over a month, probably, right? You might notice. Yeah.

**Gerry Roston:** We're a little bit more frequent than that. You know, right now we're at six times an hour. Right. And once things settle, we'll probably go to once an hour. But yeah. And at that point, we have battery life of five plus years.

**Dave Jones:** Yeah, exactly. Yeah.

**Chris Gammell:** And you could probably send back the battery levels as well, right?

**Gerry Roston:** Yeah, we do that. That's one of the channels that we gather. Yep. Yeah, that's great. That's really good.

**Dave Jones:** So what sort of stuff are you sensing for? You're searching and sensing for vibration, presumably, on something like this. Impact shock. Yeah, we're – To see that – Because it's a stamping machine, right? Right. So you'd want to know the impact force, so you'd be sensing the Gs and –

**Gerry Roston:** Yeah. So we're not doing that yet. I mean, the initial rollout was, you know, as simple as it sounds, just temperatures and currents. Oh, okay. Because that tells them a lot about the health of the machine. Current, so like you're in line.

**Dave Jones:** Yeah, on what, the big stamping coils or what they drive? On everything.

**Gerry Roston:** Yeah, on the main motors, on the – the ones that care about the most, really, are the cooling fans. Because if you see the current to a cooling fan go away when your motor's operating, that tells you you've got a problem.

**Chris Gammell:** Yeah, that's real bad. Yeah. So you have to actually insert in line then, or are you just doing inductive sensing?

**Gerry Roston:** Inductive sensing.

**Chris Gammell:** Okay. Oh, easy. That's great, too, then. Yeah. Yeah. Because I'm not interrupting.

**Gerry Roston:** So you don't have – well, it's like the last line. So I was out there a couple weeks ago. Actually, again, we're small. Also, I'm actually doing the installations myself. As a matter of fact, I'm going to be there 6.30 tomorrow morning doing another one. Hey, hey, nice. But we're actually – Glamour, glamour. For the most part, we do it while the line is hot. Now, on the 900-amp circuits, we have them shut that panel down. I'm not going to go near a 900-amp circuit. Right, right. But the other stuff, when you're doing current clamps, you can do it on a live panel as long as you're careful. Yeah, of course. Yeah. That's great.

**Chris Gammell:** So I used to work in industrial, and I know that they – at least the people that I talked to were incredibly allergic to wireless. Mm-hmm. They wanted – I mean, it was a power plant stuff, but they hated wireless even with like the – I knew some people that were working on the – what's it called? The wireless heart, like the really slow wireless protocol that has all that stuff. What are you using for the wireless stuff?

**Gerry Roston:** We use two. So the way we're configured is we have what we call leaf nodes, which are battery-powered, and then we have what we call a cloud gate node, which is what provides the communication up to the cloud. Okay. So the leaf nodes and the cloud nodes communicate using – what is it? 802 – no. 802.11.4, the Zigbee protocol. Right. Yeah. And then – Is that the 15? Yeah, that's it. I'm sorry. 802.15.4. Thank you. And then to go up to the cloud, we can either slot in Wi-Fi or 3G into our product. Cool. And what's so interesting about the factory is, as you guys were intuiting, there is some hesitance to open up those networks. So for the initial deployment, we did everything with 3G and were able to bypass plant IT. Yep. Exactly.

**Dave Jones:** Ah, yes.

**Gerry Roston:** The engineering managers got what they wanted. They're seeing the value. Now they can go to plant IT and say, this has value. Make it happen. So we're now having those conversations. Obviously, it's in our customer's best interest to be on Wi-Fi, not 3G, because then you don't have to pay for the data plan.

**Chris Gammell:** I would just, well, I just think reliability in the first place. I mean, obviously, you can notice when something's not transmitting, but at some point, they're going to be like, no, no, no. I need to know exactly what's going on here. So I think that's really what it, right now, this is like a value add, it seems like. But I think what you'd hope for is that eventually it's such an integral part of monitoring that they're like, we need to have it. And that's where I'd think it would really become a critical, you know, pinging every 10 minutes or else, you know, or else line shutdown like the Toyota production system type of thing does. Is there plans to move towards that or no?

**Gerry Roston:** Well, again, right now it's monitoring. If something goes wrong, they get alert. One of the reasons they're very comfortable and we're able to deploy quickly is that we don't interface with their programmable logic controllers, their PLCs. We're independent from that.

**Chris Gammell:** Yep.

**Gerry Roston:** When we talk about interfacing with the PLCs, you start seeing some faces get screwed up. Oh, yeah. Because then there's a lot more risk. Because then theoretically somebody can hack your system, push stuff to your node, which can then push it to the PLCs, et cetera, et cetera. Right.

**Chris Gammell:** Yeah. And security is another. I mean, I would think at this point, the stuff you're doing, it's really would be like industrial espionage of like how often something's stamping, that kind of thing. That would be the only piece right now. But what is the security, other security concerns?

**Gerry Roston:** You know, that's one that we talk about internally. And, you know, there was that large DDoS attack recently that was done by usurping a lot of IoT devices.

**Chris Gammell:** Oh, yeah.

**Gerry Roston:** But, you know, I'm not really too concerned about that for a couple of reasons. First of all, we have custom hardware and we don't run an operating system. So the ways into our device are very, very limited. You know, somebody would literally have to know the schematics or data formats and everything else. And even then, they probably aren't going to get very far because, you know, they would have to figure out how to reprogram the thing. And, you know, so it would be an extraordinarily painful thing for them to do. And by the way, that's only...

**Dave Jones:** Is it security by obscurity?

**Gerry Roston:** I mean, in part, it is. In part.

**Chris Gammell:** Not if he says it on the show, Dave.

**Gerry Roston:** You know, it's one of those things where, you know, if you have an operating system on a device or if it's a well-known device, people know how to interact with it. But our devices don't have web interfaces. Right.

**Chris Gammell:** It's not running Linux or anything like that, right? Yeah.

**Gerry Roston:** And they get back packets of a very specific format from our server. But again, that's all basically binary data. And if anything's even one bit off, it gets thrown out because it doesn't pass a checksum. Yeah. So it becomes really hard to hack something like that.

**Chris Gammell:** Well, and it is, I mean, it is sort of one directional, right? I mean, at least right now, it's mostly broadcasting back from the sensor node out. But do you have stuff going the other direction? Do you push firmware?

**Gerry Roston:** Yeah, configuration. There's configuration information that can be sent and stuff like that. Okay.

**Dave Jones:** But you don't want your competitor down the road to be reading your data and, oh, geez, they're stamping it twice the rate we are. Right. You know, like... That would be the SPN. Right.

**Gerry Roston:** Right. But all of the data going up is, you know, over HTTPS. So it's all encrypted in flight. Right. You know, and once you're on the database, yeah, you can be hacked and somebody can steal your data, so you have to use best practices. But it's, you know, our banking stuff is on computers that are cloud accessible, right?

**Dave Jones:** Yes.

**Gerry Roston:** So, you know, if the U.S. Treasury and your bank account and my bank account can be on computers that are in the cloud, I guess their stamping data can be also. So...

**Chris Gammell:** Well, it'll remain to be seen. We'll see. You know, like, yeah. We do have a lot of hardware hacker type listeners. So I'm sure they'll write in if they hear anything that's... You know, I'm really surprised, actually, that there is, you know, an industry for this stuff, though. Like with the penetration testing for hardware, that's becoming bigger. And, you know, that's... I'm sure as you grow, that's something you would do anyways, right? I mean, you would probably hire those people for security audits, stuff like that.

**Gerry Roston:** Again, we've talked about that, and we literally can't figure... You know, the only way we think somebody could really do damage is if they have physical access to our device in a facility. Because then they would theoretically be able to reverse engineer it and figure everything out. But that's such a significant amount of effort versus being able to exploit a known password in a device that's got 5 million of them out there. Why would they bother?

**Chris Gammell:** Right, right. Or if you're going after a big car manufacturer, you go after their SCADA system, which is probably got much more value anyways, or whatever they use for DCS, whatever. So... What is TechTown Detroit?

**Gerry Roston:** TechTown Detroit is the longest established startup incubator and accelerator in the city of Detroit. TechTown basically has three branches. It has a physical plant, the building. The first floor is used for startups. We have co-working space and meeting rooms. The other floors have tenants ranging in size from a two-person law firm up to a publicly traded company. Publicly traded on the London Stock Exchange, that is. And, you know, a lot of different activities happening. We have the Blocks Group, which is actually unique in the entire country. It's a group that specifically focuses on building entrepreneurships in the neighborhoods. So... Oh, that's great. Even in Australia, Dave, I'm sure you've heard that Detroit has had a few challenges recently.

**Dave Jones:** Dave, have you heard that? That's what I was going to ask about. At least we're not Detroit. It's a case. Chris is from Cleveland.

**Chris Gammell:** Yeah, when I was in Cleveland, Dave, you still have the Cleveland promotional video, the hastily made Cleveland promotional video.

**Dave Jones:** Cleveland, at least we're not Detroit. Well, look up...

**Gerry Roston:** The Russian comedian Yakov Shmiernov used to do a routine in which he made fun of Cleveland, so look that one up. Okay.

**Chris Gammell:** Actually, that video was making fun of Cleveland, too.

**Gerry Roston:** But, you know, Detroit is geographically a very large city. And I hate to use such archaic units, but it's 140 square miles. So that's, what, about 450 square kilometers or something? Yes. So it's geographically very large. And the Midtown region and downtown region are booming. They're as vibrant as any city in the world. Yeah. And Corktown, which is next to it, is doing very well. But that's only about 10, 11 square miles out of this very large city. And so the Blocks program is really focused on taking the processes, tools, and methods that we teach to technology startups and going to the neighborhoods and helping the neighborhood businesses, you know, go from three jobs to five jobs and increase foot traffic and actually make vibrant neighborhoods again. And they're just doing fantastic work. It's been recognized. The actual grant money coming in to support it has been growing because people have been seeing the success.

**Dave Jones:** I was going to say, is the state paying for this? Is the city, the county or whatever paying?

**Gerry Roston:** Less and less. Again, don't want to bore you with American politics, but Michigan is now being ruled by the Republicans who basically don't like Detroit because nobody in Detroit votes for Republicans. Oh, really? Okay. And so there have been issues with that. The funding from the state has been, you know, diminishing. But there's a not-for-profit entity in Detroit called the New Economy Initiative, which has been extremely supportive. The Skillman Foundation. Again, I don't work that group, so I can't rattle off all the names. But even some of the big banks, I think Bank of America has even supported that program because of the success that that program is having in the city.

**Chris Gammell:** Yeah. No, these kind of, these like boots on the ground type of organizations are great for funding small startups, small businesses, whatever. It's really good stuff. Yeah.

**Gerry Roston:** And, you know, they have a retail boot camp program, which helps people who are doing garage retail and internet retail actually establish brick and mortar. You know, it puts them to all the paces to understand if it makes sense for them. So some great stuff. And then the group that I work with is called the Labs Group. And we work with early stage tech entrepreneurs. And by early stage, a lot of the ones we work with are, you know, just coming out of the ideation phase. We have an accelerator.

**Dave Jones:** What's the, sorry, the ideation?

**Gerry Roston:** Ideation. So, you know. Ideation? Yes. You know, pre-prototype, pre-revenue.

**Chris Gammell:** So basically pitching on a PowerPoint desk, PowerPoint deck, right? Not with anything else. Yeah. Right? Yeah.

**Dave Jones:** Oh, okay. This is a buzzword I hadn't heard of. Oh, okay. I'm out of the loop, obviously.

**Chris Gammell:** You should ideate on it, Dave. And cogitate.

**Gerry Roston:** Yeah. We run a boot. We run a program in the summer for college students and recent grads based on the lean startup methodology.

**Chris Gammell:** Oh, Eric has been on the show.

**Gerry Roston:** Yep. Yep. I've, I don't know if I've ever met Eric. But yeah, certainly know him. Know of him. And we make them do a lot of customer discovery to figure out if their ideas make sense.

**Chris Gammell:** That's how, that's really healthy, actually. Yeah. Because, yeah, sometimes even when you have a prototype and you show up and you're like, okay, but who's actually going to buy it? Yep. So if you have that up front, that's very valuable. Yep. And that's probably that technology isn't the hard part kind of piece, right? Absolutely. Yeah.

**Dave Jones:** But it's also the, but it's also the killer of dreams. Yes. It's like, you turn up with your widget and you're, oh. Some dreams are meant to be woken up front. That's not going to sell, son. Sorry.

**Gerry Roston:** Yeah. See, and one of the reasons I like facilitating that class is, like I said, I'm a New Yorker by birth. And so for me, killing dreams is part of my, you know, DNA. So I have a reputation of beating on the students.

**Chris Gammell:** Hey, let me tell you how the things really are out here. Yeah. Yeah. Yeah.

**Gerry Roston:** So I've got a reputation for, you know, carrying the big stick. But in the end, the students usually, almost always, I think there's only been one in the last three years out of 90 who didn't see the value in the process. Right.

**Chris Gammell:** And so that means they're actually getting out and talking to potential customers, right? Absolutely. Yeah. That's super important. And if people are listening and they have that widget, go talk to some customers because you'll be surprised what you learned. It's crazy.

**Gerry Roston:** Well, let me make a plug. There's a website called Udacity, U-D-A-C-I-T-Y.com. It's online classes. If you go to Udacity and sign up for an account, which is free, they have a class. And I don't remember what it's called, but just put in the word startup. And it's an entire class by-

**Chris Gammell:** Oh, is it Steve Blank? Steve Blank on startup.

**Gerry Roston:** And there's some extremely good material there.

**Chris Gammell:** Yeah. Steve Blank is a longtime writer. People don't know. He's a longtime writer about startups and stuff like that. And yeah, he does a good class. Yeah.

**Gerry Roston:** So that's good stuff. So that's what we teach. And then we have our incubation program, which is more of a hands-on one-on-one between the two EIRs. The other gentleman is Francis Glory and myself. And we work very closely with a small handful of companies helping them try to figure out what to go next. Yeah, exactly. Oh, we just brought on a new entrepreneur in residence, Marlon Page. That's- oh, she just got married though. I forgot her last name. Darn it. Anyway, Marlon, who was brought on, again, probably the only one like her in the entire country. She's an executive in residence whose focus is on building diversity in the tech startup community.

**Chris Gammell:** That's wonderful. That's really great. Yeah.

**Gerry Roston:** And so she comes out of a corporate career. She also started a program in Detroit called Sister Code, which was to teach coding to women between the ages of 25 and I think she said 85. Oh, nice. A lot of times just so that they know what it's about, so they're not scared by it. Yeah, that's great. And so she's a wonderful addition to the team. Cool.

**Chris Gammell:** And so is that how you- so I mean, you've been in the startup space for a while. Is this kind of how you discover- you've been at a couple different startups. Is this how you kind of find the startups to work with as well?

**Gerry Roston:** Well, technically, that's what it's supposed to be. So traditionally speaking, an EIR works with a source of IP generation. For example, a tech transfer office at a university.

**Chris Gammell:** Okay. Yeah. Ann Arbor, right, where you are. Who's there?

**Gerry Roston:** Well, in Detroit, it's actually Wayne State. Oh, Wayne State. Oh, that's right. Detroit, yeah. But yeah, U of M is right around the corner from where I live. And so, yeah, typically an EIR will find a technology, help it along, and then take the technology out of the university, become CEO, and grow it up. That hasn't happened yet for either Francis or myself at TechTown. Civionics is actually a U of M startup. And I was introduced to them by a colleague of mine who, you know, when they said we want to- the company started by doing a lot of contract engineering and government contracting. Mm-hmm. And what's called the Small Business Innovative Research Grants, SBIR. It's probably been on your show before.

**Chris Gammell:** That's right. Back in show 331, Zach Ferdin was talking about those.

**Gerry Roston:** Dave, I hope he looked that up and didn't know that off the top of his head because if he did, I'm scared. I did actually know that off the top of my head.

**Chris Gammell:** He probably does. Yeah. It was a couple weeks ago. Come on. Give me some break. But yeah, anyway.

**Gerry Roston:** But they said they wanted to try to become more of a product-based company and, you know, be able to have repeatable revenue. So a colleague of mine who knew them introduced me to them, and that's how I got engaged with Civionics. All right.

**Chris Gammell:** That's great. No, that's- At TechTown. I can imagine that's how it usually happens, right? With introductions, knowing people, that kind of thing. Yep. So when the- I mean, so like the tech transfers, I've heard about tech transfers before. I'm usually kind of wary of it, to be honest. Because, you know, like I know that a lot of research happens at schools, but not necessarily like practical, like things that are going to be translate to actual solutions.

**Gerry Roston:** And that's a good point. So let's get back to customer discovery for one second. Yeah. There's sort of two ways that products come to the market. There's what's called customer pull and technology push. So customer pull is when a customer or an entrepreneur sees a need based on their experience, and they go about trying to build a business to solve a specific problem. Technology push, on the other hand, typically happens at universities where some guy with a PhD, and you've got to watch out for guys with PhDs. They're all trouble. Yeah, those guys. Yeah, dodgy. Yeah, dodgy. I've got to remember that word. That's a good one. You know, they think they're going to solve world hunger, and they come up with some wonderful technology, which does something in their lab once. They write a paper about it, and then they're going to start a company, and they don't have to market it because it's so great. Everybody's just going to come to their – Right, right, right.

**Dave Jones:** That's technology. And they'll raise 20 million bucks on Kickstarter. Yeah. Or sorry, Indiegogo, because they don't have a real prototype.

**Gerry Roston:** Yeah, so that's technology push, and that's where Civionics was. It was really a technology push. No, there was this core platform that was actually developed to assess the health of bridges. Oh, okay. And the question was, what can it do? And so the first thing I did for the company was customer discovery, and the original thought was to use it for building energy monitoring. And I found that nobody cares about energy monitoring. A bunch of people cared about energy management, but energy management normally means changing heating, ventilating, air conditioning systems, HVAC systems, and that's not what a tech startup does. But the beauty of customer discovery was while talking to – one of the tracks I went down was seeing if large factories cared about this. Right.

**Chris Gammell:** Also, who's got money to even possibly fund this kind of thing, I'm sure, right?

**Gerry Roston:** Yeah. And so while talking to a guy at a large factory, he said, I don't really care about energy monitoring, but can it tell me about the health of my equipment?

**Chris Gammell:** Oh, that's great. Hmm.

**Gerry Roston:** Let's think about that. Well, guess what we're doing today? We're doing equipment help. And that's the beauty of customer discovery. If you go into that process with an open mind and you really listen to what the customers are telling you, you're going to learn more in a few hours of doing that than you will years sitting in your lab talking to yourself. Right.

**Dave Jones:** And how did you set up those meetings? How easy is it to get that, though? Yeah. Like, can you just call up a company and go, do you have to have contacts? Or you just cold call them and go, hey, we've got – Hello, factory. Some wonderful tech. Can we come and talk to you? I'd like to talk to factory. Like our products.

**Gerry Roston:** Well, so Dave, the answer is cold calls are always harder than getting introduction, but it also has to do with how you preface it. If you pick up the phone and say, I've got this wonderful thing, the first thing going through their mind is sales call and you're not going to get any place. Yeah, yeah. Exactly. But the whole point of customer discovery, it's not about selling. It's about learning. And so that's when you appeal to people's ego. So what I would tell people is I would say, look, I know everything in the world about wireless sensor systems. I know absolutely nothing about building energy management. You know, based on what I've discovered, you're an expert in this field. Can you teach me?

**Chris Gammell:** Stroke, stroke, stroke. Yeah.

**Gerry Roston:** People love – and what's really cool – They do. Yeah. They love to talk about it. And what you find is if you hit upon a pain point, you can't get them to stop talking.

**Chris Gammell:** Yeah. You know, it's funny too because the way you describe this, this is what I tell young engineers. That right there is also networking. Like getting someone to talk about their problems or like what they're working on. Like that's also how you just get to know people that it's like – and then eventually they'll be like, oh, by the way, I need to hire someone to do this stuff anyway. Oh, okay. Yeah, I'm that guy. That's great. No, that's really great. And so it was just – it was cold calling but it was not – but it was like with a purpose, with the ego piece. Yeah?

**Gerry Roston:** Yeah.

**Chris Gammell:** Yeah. Yeah, that's awesome. That's really great. And how many people do you have to talk to in order to kind of finally get to that point of –

**Gerry Roston:** I actually didn't do as much as we normally recommend. I only got through about 75, you know, customer discovery interviews before we discovered that. 75? What do you usually recommend? My goodness. We recommend a minimum of 100 and that's to get started. Holy crap.

**Dave Jones:** Convincing 100 companies to let you come and talk to them, that's a full-time job for a year.

**Gerry Roston:** That's a year's full-time job. Well, we give the students in the summer 10 weeks. They're supposed to be doing a minimum of two a day. Now, obviously, if it's a B2C model, it's much easier to get the interviews but then we tell them they have to do 250.

**Chris Gammell:** Oh, my God. What? Got to set the bar high. That's masochistic. That's sadistic. I don't think it's backwards. Yeah, that's – wow. That's – whoa. So 100 for B2B, which is business to business. 250 for B2C, which is business to consumer.

**Gerry Roston:** Well, I mean the reality is this. If you've never done it before, you're going to screw up the first 10 of them so badly, they don't count. But by the end of the first 10, at least you're going to know the questions to ask.

**Chris Gammell:** Yeah, right. Well, people are going to go listen to our first 10 interviews and, yes, they will agree that they're pretty bad. Wow.

**Gerry Roston:** Wow. So in the next 15 or 20, you're going to figure out that your original idea sucked but you really need to be pivoting and asking about this. By the time you get to number 70, you have got a pretty good idea of what the market wants, what the needs are, what the pains are. And then you can start honing in and asking more detailed questions. You can start figuring out what sort of sales model they want, what sort of distribution channels they want. And so the later calls could get much deeper because you've done a lot of learning and you can at that point speak their language, understand their pains, and have a much better conversation.

**Chris Gammell:** Wow. That – yeah. And you also shifted your targets, right? Oh, yeah. Because I'm guessing at the beginning you were doing the energy people and then you started talking. You're like, oh, I need to talk to factory people. Yeah.

**Gerry Roston:** It was generic buildings. Then I looked at co-working spaces. I looked at large campuses. I had a wonderful conversation with a guy who's responsible for energy management at Microsoft. Wow.

**Chris Gammell:** Like all the servers and stuff too?

**Gerry Roston:** Yeah. Yeah. And the amount of electricity they use there is a mind-boggling number. Yeah. But they do an incredible job of tracking it and being aware of it.

**Chris Gammell:** Mm-hmm. Yeah. A lot of them are switching to renewables too, right? To reduce their costs and stuff like that?

**Speaker ?:** Yeah.

**Chris Gammell:** Man, that's nuts. Could you give us a quick – because we are kind of running out of time. Could you just give us a quick idea of what you say? Is this like an email or is this like a call? Or like what does it sound like when you're starting to do this kind of thing?

**Gerry Roston:** Well, normally I would do an email first before the call and it's typically something to the effect of, you know, I'm an entrepreneur. I have a startup idea in this space. You know, I'd like to get 10 minutes of your time. You know, I'd like to get 10 minutes of your time to learn from you, you know, what some of your challenges are to see if our idea makes sense. But the key thing is you don't tell them your idea because anybody who's nice enough – anybody who's nice enough to say, yes, I'll talk to you, if you tell them your idea, they're going to say, oh, that's nice. And that's not what you want to hear. You want to hear your baby is ugly. Yeah, yeah. And so a lot of this is teaching people, you know, how to have these conversations. And, you know, for many of your listeners who I'm sure are technically inclined and are, you know, probably introverted by nature, it's not impossible because, again, I'm an engineer. I'm as introverted as the next one. But it's a skill that you can learn. And if you learn it, it just allows you to become a much more effective engineer because you actually solve the problems that people care about, not the ones that you think they care about.

**Chris Gammell:** Right. Yep. Yeah, that's great. That's really great. That's brilliant. Yeah. I imagine that people that get good at this too – like I've talked to some business owners, stuff like that, where they're just like, I have so many business ideas that I don't even know what to do with it. Like when you find someone that started a couple of companies and stuff like that, but it's because they understand how to talk to people. They understand how to like figure out what the real pains are. And then they just – they're like, oh, yeah, that's a business. That's a business. That's a business. Right. Yeah.

**Gerry Roston:** And obviously, you know, the longer you're in industry, you know, the better your understanding of these things are because you've just seen it and you know what the challenges are.

**Chris Gammell:** Yeah. Do you do – do you go around and teach this stuff other than at TechTown?

**Gerry Roston:** TechTown? Yeah. Primarily TechTown. You know, Ann Arbor has a boot camp. I've been involved with that. You know, occasionally at U of M, I guest lecture a class here and there in the – I've guest lectured at the engineering school and the law school. So, yeah, a little bit. It's fun. That's great.

**Chris Gammell:** Yeah. Well, I didn't expect it to take this turn, but this has been very interesting stuff. No, that is –

**Dave Jones:** Yeah, that's really – That is very interesting. I don't think we've had anyone talk about that aspect before.

**Chris Gammell:** No, this is really important stuff. Like, yeah.

**Dave Jones:** We have had a lot of similar, like, discussions about this sort of stuff, but that particular aspect has never really come up.

**Chris Gammell:** Yeah. And, Jerry, is that in the Steve Blank course as well? I mean, is that – like, if people sign up for that course, is that the kind of stuff they'll learn there?

**Gerry Roston:** Oh, absolutely. Absolutely. Right. Great. You know, another one, there's a PDF book you can download. It's all of 80 pages. It takes, you know, 30 minutes to read called Talking to Humans.

**Chris Gammell:** I have that one. That's a good book, yeah.

**Gerry Roston:** It's a really good book. And, again, it gives you ideas of how to have these conversations.

**Chris Gammell:** Yeah. That's really – that's smart. Well, Jerry, thank you for being on that we ran through the robots up to startups. Is there anything else people should know about you or what you're working on or what you're interested in?

**Gerry Roston:** Well, I think what people need to know is that you were right because when we were talking about this, I said, you can't get me to talk for more than 10 minutes. And we've been at this for 90. So, well done, gentlemen. We're very good at this.

**Chris Gammell:** Never – yeah, we've done a couple interviews now. So, yeah. Well, Jerry, thanks for being on. Where can people find you and your company stuff online?

**Gerry Roston:** Well, Civionics is www.civionics.com. And that's spelled C-I-V-I-O-N-I-C-S. Sort of like the word avionics, but, you know, civil and electronics. Oh, yeah. TechTownDetroit is TechTownDetroit.org. And then we also have a – you can Google me, Jerry Rosten, R-O-S-T-O-N. One of the advantages of an uncommon name and having been on the internet for as long as I have is if you Google me, the first, I don't know, 50 pages are 90-some percent me. So I'm very easy to find. And then we have a personal website, pairofdocs.net. You can track that one down as well.

**Chris Gammell:** Okay. Sweet. Well, thanks for being on. We appreciate it. And it's been great, Jerry. Hope to talk to you again soon. My pleasure. Really enjoyed it.

**Dave Jones:** Thanks, mate. Catch you next time.
