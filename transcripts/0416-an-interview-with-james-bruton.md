---
episode: 416
title: An Interview with James Bruton
url: https://theamphour.com/416-an-interview-with-james-bruton/
---

**James Bruton:** This is The Amp Hour Podcast. Released November 18th, 2018. Episode 416. An interview with James Bruton.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**James Bruton:** And I'm Chris Gammell of Contextual Electronics.

**James Bruton:** And you've also got James Bruton from XRobots. Welcome, James. How are you doing?

**Dave Jones:** Thanks for joining us.

**James Bruton:** We are really tempting the fates here. We're going across two oceans. And we have James on one side and Dave on the other and me stuck in the middle. So welcome and glad we all got here today. That's great.

**James Bruton:** Yep, thanks for having me.

**Dave Jones:** And where are you from based on the accent?

**James Bruton:** Yeah, in the south of England. So Hampshire, which is quite near the south coast, near the Isle of Wight, but about 20 miles north, roughly. Awesome.

**James Bruton:** So you mentioned XRobots. What is that, if people don't already know?

**James Bruton:** Well, so XRobots.co.uk is my website that I registered back in probably 2004 when I started building robots. And I put a video out today, actually, about my robotic history of the robots that I tried to build before YouTube, even. And certainly before people had 3D printers. So that was really a bit of history there to try. I've basically tried to build walking robots that were human size, which obviously is quite hard. And I couldn't find any easy tutorials about it. So I decided to have a go myself and write about it on a blog. That's awesome. And that's how it all started, really, at least in my adulthood.

**James Bruton:** What actually prompted that in the first place? I mean, like something must have sparked the, all right, I want to see a walking robot that I've made.

**James Bruton:** Yeah, I guess I've been interested in making stuff since I was a child. And I've built various things, you know, in the past. Studied electronic engineering, formerly at degree level. That was in the 90s, though. So, yeah, I don't know, really. I've worked in IT ever since and always held an interest in engineering and that sort of thing. So I thought, why not? That'll be a challenge. I guess one of the things was to be better at writing software, which I'd done, you know, a bit of C and a bit of Python and stuff, but never really had an application. So it seemed like quite a good one. Why not start with something really hard?

**Speaker ?:** Yeah.

**James Bruton:** Yes, you picked quite a hard one, I've got to say. I mean, like that's nice.

**James Bruton:** Yeah, well, here we are 14 years later and I've almost achieved it. Right.

**Dave Jones:** How hard was it back in 2004 or whatever it is or even before that when you first, like compared to today? Like because today it seems like, oh, okay, it's another walking robot, you know. Like it's still, I mean, engineers like us can understand how impressive it is, but it's like it's kind of like, yeah.

**James Bruton:** Yeah, I can't even remember. Did Arduino exist then or did it come along since then?

**James Bruton:** That was 2007, I think. Was it? Yeah, YouTube was. A little bit cheaper, a little bit sooner rather.

**James Bruton:** Yeah, so there were still PIC chips and other microcontrollers, but that's, you know, I'd done Z80 once upon a time. But that was about my microcontroller knowledge. So, yeah, like the initial ones I didn't even, I mean, I had, as I mentioned in the video that went out today, I had sort of like a serial servo controller I could control from VB6. And I had that turning a, I had that.

**Dave Jones:** I love Visual Basic 6.

**James Bruton:** Yeah, well, I think a lot of people loved it because it was really easy to access like a parallel port. Yeah. And there's things like that. So, yeah, I basically had those servos turning potentiometers to make analog voltages. Oh, nice. And then comparing that analog voltage with a feedback joint, a pot on the joint to give me, you know, a difference with an op amp. And that switched to relay either way to make a sort of relay H bridge to make the motors work. So that was the initial way that it was all controlled. I mean, I probably could have done better even with a PIC or something, but, you know, that was innovation. That's great, man.

**James Bruton:** I was noticing, so I watched that video and it is a great history and I really like that you're going to go through it. But the thing that struck me about it, when was the first, when would you say there's the first one that worked? Like that actually worked as you had hoped it to work?

**James Bruton:** Well, none of them worked as I hoped they would, but like Android 2 did actually take steps and it could go along. And I can't find the video. I wish I had the video. 3 was pretty good, I suppose. But, you know, you couldn't really, I don't know if, was eBay around then? I don't know if there were so many Chinese. Oh, yeah, but it's not the same. Yeah. Exactly. Like now you can go and buy some, just anything you want, like lead screws, ball screws. You know, not to mention brushless motors and cheap gearhead motors. There just wasn't really that sort of quantity of stuff. Not to mention companies like Adafruit with Arduino modules and libraries. Right. You know, let's just plug in a sensor and here's some code and here's the numbers in variables straight away, you know.

**James Bruton:** Well, I think the thing that, I mean, like it sounded like, I mean, it does sound like the, the stuff that you'd sent out, or sorry, the stuff that you were doing, it was working to a little bit of a degree. But at least from my watching of it, it almost sounded like 2014 was when it, like, that's when it started to click and really got there. And then I was, I was thinking about that. I'm like, oh, my God, you, you persisted for 10 years, though. You kept doing it. And so what the hell made you keep going? Like, like, that's amazing. What, what, what is this drive that you have around, around walking robots? That's, that's what I, I was impressed by.

**James Bruton:** Sure. Um, I think as soon as I started another one, I'd have another idea of a way to do it better. And so that was something that kind of occupied my thoughts until I actually tried it. And then as soon as you start, I mean, I always say the favorite projects of mine are ones I haven't started yet. Yeah. As soon as you start them, you go, oh, I wish I hadn't done it like this. Or I wish I was doing something else. Or, you know, you're bored of it halfway through sort of thing. So, um, you know, even with Open Dog, I've thought, oh, I shouldn't have done it like that. I should have had compliant joints. I should have made a cat. I should have made a cat. There you go. Um, but then, I mean, that's in a way it represents traditional robotics in that it's very rigid and has a mathematical model. I can always build another robot with springy legs, you know, as a separate, maybe slightly smaller, cheaper project. But that's why there's so many robots. I'm looking at all of those robots right now and there's a lot of them.

**Dave Jones:** Have you, uh, often regret? No, probably regret isn't the right word, but you do like a build as you go videos kind of thing, right? Yeah. And you must get a lot of, a ton of feedback. Do it this way. Do it this way. Do it this way. Try this. Try that.

**James Bruton:** Do you get sick of that or is that? Oh, yeah. So even on the, so what were we on Open Dog 13 or something? Right. Now even on part 12, there were people saying, oh, I knew it wouldn't work. And it was like, I've just only just made like done the first steps, you know. Right. Sorry, it doesn't immediately work as well as Boston Dynamics.

**James Bruton:** That's a great comparison too.

**Dave Jones:** Would you, do you think that often, oh, it's better if I just finish something and then like post document it via videos or something like that. Oh, it's now it's working. I'll go do a series of videos on it.

**James Bruton:** Potentially. Although with something like Open Dog, I think it is really something that is going to last for years, you know. Right. All the stuff that it'll eventually do, hopefully. So it's not really feasible to store it all up. Yeah. And then have hundreds of videos. Got it. Plus also I need to earn some money from Patreon. Right. And, you know, YouTube ad revenue. So I need to, I mean, it's quite time consuming. So, you know, doing a video every week, I've got to make some content ultimately. So there are other projects that go on in the background, like when I did the giant Lego electric skateboard, which was about 800 hours of printing. Wow. And I did all of that. And I had the thing made. Then I put the first video out. So the next one after followed fairly quick after. Rather than it being, you know, I've made three bricks this week, you know. So it's more of a background content. And I have foreground content, which is my regular week, week on week. Yep.

**Dave Jones:** So do you do live stuff at all?

**James Bruton:** Patrons only.

**James Bruton:** So monthly, hourly, hour long live stream. Cool. I don't want to do, I don't think I want to do too much public because the videos end up really long and people aren't engaged with them so much. Yeah, true. I don't know what that does to engagement.

**Dave Jones:** Oh, right. The actual channel metric and that sort of stuff and the magic algorithm.

**James Bruton:** And yep. Right. For people that haven't, haven't seen your channel yet, could you explain what Open Dog is?

**James Bruton:** Yeah. So Open Dog is a dog shaped robot. It's got four legs. It's not anatomically correct to a dog by any means. It's knees point the wrong way and stuff.

**James Bruton:** Yeah, and your robot doesn't even like, you know, pee or things or whatever. Yeah, it doesn't even lift a tired leg. Not yet.

**James Bruton:** Yeah. It's about the size of the Boston Dynamics Spot Mini, but I think it's probably heavier. And it's chunkier looking. And it's made with 3D printing and CNC aluminium. And all its joints are brushless motors, which are from drones. Some good Hobby King turning G1s. And basically ball screws. And it's got 12 joints. So each leg has a knee, a hip and another axis at the hip, essentially. A shoulder, if you like. And it's got a kinematic model. So it calculates the inverse kinematics for all of the joints all at once. So it's got a six-axis controller with two three-axis joysticks for three translation moves and roll, pitch, and yaw. And it can operate all of those simultaneously. And I did a couple of episodes on that mathematical model, which isn't quite as accurate as it should be. But it does work. And it's all running 8-bit Arduinos at the moment, which are due to get upgraded to teensies, which are 32-bit and 180 megahertz instead of 16 megahertz. That's the thing I find interesting.

**Dave Jones:** Like, you're getting, like, you're doing, you know, you're talking about, like, real-time kinematics and control and everything. And Arduino in the same sentence. You know, to me, that doesn't compute. No pun intended. Like.

**James Bruton:** Yeah, I mean, I'm pushing it. And also, there's lots of Arduinos all strung together on serial buses and stuff. Right. But that's just, I mean, basically, I'm going along with the O-Drive development, which, at the time I started, this doesn't support CAN bus. And they have just got CAN bus in beta. So then I can throw away all my three megas with lots of serial ports and go to one teensy with CAN bus straight down all the O-Drives. And there's six O-Drives, which are dual-brushes motor drivers.

**Dave Jones:** Right. So do you have an Arduino controller for each motor and then a central one controlling?

**James Bruton:** No, the O-Drive has got its own PID controllers and it does the encoder handling. So they've got the brushless motors. Each one's got an encoder coupled to it, which have got 8,192 counts per revolution, which makes it more accurate than a stepper motor and more powerful. And, of course, being brushed. They're two kilowatt brushless motors. They're current limited at the moment to about 30 amps on 24 volts. But I could push them if I wanted. If I could get batteries that would source enough current for all 12. Right. So the O-Drive does all that encoder handling. Got it. And does the positioning. It will do end-stop calibration and all that stuff. So you can literally just send the positions and motor speeds to the O-Drives and it just handles it for you. Okay.

**Dave Jones:** Well, that's why you're able to do it with the Arduino controller. Otherwise, you'd stand no hope, right?

**James Bruton:** Oh, absolutely. You'd never count the encoders at 3,000 RPM. It would be ridiculous. So I believe the O-Drive's running STM32s. So, yeah.

**Dave Jones:** 3,000 RPM is really fast. Yeah. To me. Is that... Why... Can you tell us why you have to run it at such a high speed? And then presumably, what is it? Torqueing it down? Sorry, I'm not a mechanical... No, I'm not.

**James Bruton:** But that's the capability of the motor. Right.

**Dave Jones:** Okay.

**James Bruton:** But, yeah. So I'm using ball screws. So they're driving... They're roughly a 2.14 to 1 belt ratio to a 16.05 ball screw. It's still pretty agile, even with the current limiting and the motors on 24 volts instead of 48. I think it's enough to be as agile as it needs to be.

**James Bruton:** I'm a little confused right now. You have to excuse me. So, yeah. I've never done anything with motors, actually. Yeah, same here. I'm not a motor. Okay. So I'm super excited to talk to you about this stuff. But, like, I've heard reverse kinematics over on Embedded FM. I know Alicia talks about that a lot. And I've heard that from robot friends I have. Not friends who are robots, but people who work at robot companies. Could you explain what that is and specifically to the... How much of it you need to understand as the robot maker?

**James Bruton:** So which part of the inverse kinematics? Yeah, let's start with it.

**James Bruton:** Yeah, I mean, like, are you doing math equations or is it like you're implementing libraries?

**James Bruton:** No, I did all... Well, you could... There are various ways of things integrated in ROS and over open source platforms, which will do it for you where you put in the dimensions and it's solved. I did it as an educational series. So there's two videos about... One is... Each one is solving three of the axis. Oh, sorry. Well, the first one is solving translation. And the next video is solving the rotation axis. So there's three axis in each video. And I did that by basically drawing triangles all over the side view and so on of the dog and doing the trigonometry. Oh, right. And so all the Arduino code is loads of, you know, arctans and everything. Okay.

**Dave Jones:** So you measure the robot, take the physical dimensions and angles and program that into your system.

**James Bruton:** Yes. Right. So the kinematic model is basically saying if I... So you put your hand on your cup on the table. You can work out, you know what your joint angles are, your shoulder, your elbow, your wrist maybe. And therefore you can work out in Cartesian coordinates in X, Y, and Z in straight lines where your hand is.

**Dave Jones:** Nice.

**James Bruton:** So inverse kinematic is saying, well, I want to go to that cup on the table, but I know where the X, Y, Z is. Now what is the solution for all of my joints? Aha. And there could be more than one solution because you could, you know, theoretically invert your elbow or turn your arm upside down.

**Dave Jones:** How do you decide? Do you leave it up to it to decide which solution to choose?

**James Bruton:** So in this case, there's only one solution because the elbows, if you like, or the knees, whichever way you look at it, I think they're elbows because they bend that way, but they don't turn inside out, fortunately. And I can't do a complete 360 of any of the joints. So there's only one solution and my triangles never turn, they never get two sides flat, which breaks the maths. So actually the straight trigonometry worked out and then just doing arctans or whatever the inverse function is to get the, you know, to work out, work it all back essentially. But most of this stuff was, you know, what we have GCSEs in England, which is your secondary education. Most of that's GCSE maths. And I really wanted people to be able to understand, you know, what I was talking about. If they've got like one GCSE and a piece of string and a protractor, they can understand it. And so there's all these diagrams. It's literally me drawing with black marker over a printout of the CAD of the side of the robot saying, right, here's the hypotenuse, you know, the opposite adjacent. We know this angle. Now we need to solve this angle.

**James Bruton:** Sokitella. That's all I'll ever remember.

**James Bruton:** But essentially I still had to go on sort of the mathsisfun.com website for high school kids to try and remember how, or like some of it's playing as well. Join the club.

**Dave Jones:** I don't remember anything I learned. Yeah, exactly. It's like, you know.

**James Bruton:** Well, I think that's important though too, is to point out that like, okay, yes, there's going to be math here. Yes, it's going to be, it's important to actually understand it. That's what I think you're saying, right? Is that understanding the math underneath is important for troubleshooting and translation and everything else in the software. But that, yeah, you don't need to have it. You don't need to be a math genius to, you know, you don't have to be like an innate math genius. You need to be able to look at resources and then go and stick with it and do it. Is that, is that accurate?

**James Bruton:** Yeah, that's how I did it.

**James Bruton:** Yeah. Yeah.

**James Bruton:** So I probably could have, I don't know, I probably still would have had to have pulled out a textbook probably. Right. Or at least look up how to solve Pythag again. But yeah, I mean, essentially it's the application of the stuff you learned at school that you've never used since, depending on what your job is.

**James Bruton:** Right. And doesn't it piss you off that like, this is like, they should frigging start with a robot. If I saw a robot first and then they're like, this is why you need to know Sokotoa. It's like, oh, okay. Like, look at that robot. I want to do that. That's so frigging cool. You know, like.

**James Bruton:** Yeah, there is that. And so I do, I've had, well, I haven't done any recently, but I have done a couple of school visits where I have gone in with like BB-8 or something like that when the time Star Wars was out. And, you know, even to talk about kids who are programming in Scratch. Yeah. And like teach them something like, there's quite a lot of stuff in Scratch, like functions, like abs, the absolute function, which is like really simple and really useful and no one knows it's there. And that's something that I use like, you know, for a motor driver or something to turn the negatives positive to drive the PWM positive but out of separate pins. And that's how BB-8 works. And then they can relate to what that function does. That's awesome.

**Dave Jones:** Does it always have to be, is it always this easy, well, easy in quote marks math, or is it like when you get to the Boston Dynamics level, do they implement like yet another layer of PhD math on top of?

**James Bruton:** I don't know because they haven't published their source, but I'd imagine it's slightly more complicated. And in fact, as far as I know, those robots are compliant and they're like force forward kinematics. So I believe on a crude level what happens is...

**Dave Jones:** What's force forward?

**James Bruton:** Yeah. So I believe what they do, and I don't know this is fact, but what I believe is that they have compliant joints. So they have their actuator or whatever, and then there's a springy bit in the middle, and then it's attached to the joint. And that springy bit is measured. So if I were to do that, I'd have to run so fast to get that measure, the measurement of the springy bit back into the mathematical model. So it'd be like constantly trying to catch up. So I believe what they do is they just smash the legs into the ground, measure the distance, and then use forward kinematics to work out where the foot is. And now they know.

**Dave Jones:** Right. So they have like the spring joint modeled. Well, they've physically measured all the properties of that spring joint, and then that goes into their kinematics model.

**James Bruton:** I think it's measured in real time. But basically, instead of trying to work out inverse kinematics, they approximately move the legs where they want. Uh-huh. And then when they comply with whatever, with the ground, when they just smash that foot into the ground, then they can just, they know all the joint angles then, because the legs hit its destination. Got it. So then they can roughly work out what the pose of the body is. And then you can do inverse kinematics to operate the weird head arm on top to keep the gripper still.

**Dave Jones:** Right. Yep.

**James Bruton:** Because then you know the pose of the body. So that's approximately. So I want to do another robot, or at least build one leg on a jig that jumps up and down. Right. That basically pulls up a springy tendon, and then has a foot sensor. And when it hits the ground, it either complies, or it unwinds the springy tendon. And then we can calculate the kinematic model from wherever the leg ends up, essentially.

**James Bruton:** Yeah, I guess. So like, when I think about like robotics, I always think down at like the motor control level. But it sounds like that stuff's not figured out, but it's. That's easy. It's abstracted away, at least. Right? Yeah. Yeah.

**James Bruton:** Yeah, I think that's the, I mean, yeah, the motor driver part isn't too hard. But so for Open Dog, the brushless motors and the O-drives are kind of the most advanced motor drivers and the, you know, that sort of top quality that I've used. Never used brushless before. And brushless motors, the power in them is bonkers these days. You know, you think about these. Right. If you think about what a two kilowatt brushed motor would look like, a DC brushed motor, it's a massive thing. And these are, you know, relatively small for the power you get out of them, but being able to control them accurately and everything else. So I'm so glad that's taken care of with O-Drive.

**James Bruton:** And what is O-Drive?

**James Bruton:** So O-Drive is a dual brushless motor driver, which the encoder links to, and it handles all the encoder handling.

**Dave Jones:** And it's an open source. It's an off the shelf open source. It is totally open source hardware. Yeah.

**James Bruton:** Yeah.

**Dave Jones:** And what sort of processor is that running?

**James Bruton:** I think it's STM32. Right.

**James Bruton:** Yeah. So to talk about abstraction again, so you said you hand the O-Drive controller a spin this fast, or you say go this many steps, or what do you actually... You can tell it to go to a certain position.

**Dave Jones:** It has a position.

**James Bruton:** At a particular speed.

**James Bruton:** Okay. Okay. So you say do 30 revolutions and end at this angle or something like that?

**James Bruton:** Well, yeah, we're being encoder counts on the motor, so 8,192 per revolution of the motor. Mm-hmm. And even on load, I've managed to get it down to plus minus 10 encoder counts, which is pretty accurate.

**James Bruton:** That's awesome. Yeah. Wow. So...

**Dave Jones:** Why is there plus minus 10? I need to know.

**James Bruton:** Oh, just approximately, you know, in terms of accuracy.

**Dave Jones:** Yeah, but why? There are encoder counts. Why can't you count to the plus minus one? Why is there, like, a plus minus 10 error there? Is it slipping the motor, the encoder, or...?

**James Bruton:** I don't know. I mean, we'd have to look at how brushless motors are driven. So what are they... Oh, I don't know how many poles they've got, but I guess there's a certain accuracy you can be with the motor in terms of its revolution, you know, how accurate it can be in one revolution. Right. With 8,192 clicks per revolution, that's still pretty accurate.

**Dave Jones:** And does that change based on the load? Like, the larger the load, you get more slip and...

**James Bruton:** That was on a test load with me with a test leg. I guess it would do, but that was the test load I did, which was the initial test leg of me holding the leg and trying to stop it. So... Right. Yeah, the encoder's also used to actually drive the brushless motor. So the brushless motor obviously has to have the right poles driven at the right time because it's brushless. So the encoder's used to sync up as well. So it does a calibration routine where it works out the motor's stator position relative to the encoder so it can actually drive it. And that's what's so special about brushless motor drivers because they're three phase essentially.

**Dave Jones:** Which is why you wouldn't want to be rolling your own, right? You're better off just using an off-the-shelf platform like O-Drive, right? Because there's so much work.

**James Bruton:** Yeah, exactly. I mean, there are others around there, but this is the only one really that's meant for robotics that does the accurate encoder positioning.

**James Bruton:** So you have... So let's just talk about a single leg of the open dog. So one leg has how many drives on it?

**James Bruton:** Three motors. So one and a half O drives.

**James Bruton:** Okay. And so that means that there's a... You said there's an elbow joint. I guess with a dog it's weird, but like an elbow joint, there's a hip joint.

**James Bruton:** Yeah, so I've got a knee or an elbow, whatever it is, in the middle of the leg. Okay. Then another joint at the top, which I guess we'll call the shoulder... I think I called them... What did I call them? I must have called them elbow, shoulder, and hip, weirdly. So essentially, yeah, the elbow's in the middle, the shoulder is at the top. So if you imagine your arm, it looks like that at the moment. And then if you wave your arm outwards, lift your arm out the side of you, that's the hip joint on each one.

**James Bruton:** Right. And that gives you kind of like how wide the stance is, right? Yeah, that's it. Yeah. Yeah. Okay. Interesting. And what made you choose that configuration in the first place?

**James Bruton:** I looked at the Boston Dynamics robots, and it looks a bit like what they do, but I think they might have another one up at the hip or shoulder that allows the leg to rotate, because I don't have that.

**Dave Jones:** I've got to ask, what do you... Like, everyone's seen the Boston Dynamics videos, right? That's what everyone raves about. They go viral because they look so just... Creepy.

**James Bruton:** They're so creepy.

**Dave Jones:** Yeah, so creepy. Creepy is the word. And do you... Like, I... I'm... Tell me if you think the same way. When I look at... Everyone looks at that and goes, wow, look at how advanced these things are. And I go, like... Because it's doing some trick, right? It's doing some jump up boxes or doing whatever it's doing. I'm... The engineer in me says, no, they've spent three months solid programming it to do that one trick. It can't do anything else. You know, like, it's not... It's not like just... Like, it's not like just automatically doing that. Oh, he's... You know, throw random objects in front of it, and it does all sorts of... You know, it just does the business like a human.

**James Bruton:** Well, I guess the thing with... Was it Atlas doing the backwards flip or whatever? Yeah. I mean... Yeah, I don't know. You don't know how many times it fails. Yeah, right. Whether that's like one in a hundred, though, as well. That's the other thing.

**James Bruton:** Until they released the blooper video, which is our favorite thing here. Yeah.

**James Bruton:** So the Boston Dynamics dog doing the dance thing they released recently, there's even a jump cut or two in that video. There's at least one. Which means it didn't do it consistently all the way through enough for them to make the film. So, you know, you don't know.

**Dave Jones:** So how far do you... The truth must come out. How far do you think they're away from, like, a robot that can do, you know, like human-like random stuff? Like, you just put it in a random room and it can do things. Like reactive type things, too? Yeah, I think we're still a long way from that. A long, long way.

**James Bruton:** Well, depending on what you expect it to do. I mean, in terms of its physical presence and its physical ability, it's pretty good, I suppose. But whether it's got good enough sensors to work out, you know, how to get out of the crystal maze or whatever. Right. I don't know. Do you have that? Does everyone know what I'm talking about? It's possibly just a UK TV series where it's, like, contestants who everyone shouts at because they're never clever enough have to go into, like, escape rooms, essentially, and solve a puzzle. Right, okay, yep. Do something, you know. Yeah. Nice, nice.

**Dave Jones:** No, I'm just, you know, talking about interacting with people in a room or something. You know, like.

**James Bruton:** Oh, okay.

**Dave Jones:** You know, if it could go up and detect people and randomly shake their hands and say hello, you know, and, like, something basic like that. Well, that's definitely possible.

**James Bruton:** I guess it is. But I don't know, really. I don't know what goes on inside Boston Dynamics. But there are robots that will do that, sure. There's lots of human interactive robots.

**Dave Jones:** Would you take a job there or elsewhere?

**James Bruton:** I don't know if they'd offer me a job, to be honest. No, right, okay. But then I'd have to give up YouTube.

**James Bruton:** Right, yeah. Yeah, they probably wouldn't let you show it before the final video, huh?

**James Bruton:** There'd probably be no time. I mean, I'm doing YouTube almost full-time now. So, yeah, effectively, I do another 16-hour-a-week day job doing some design work for a startup, working from home. But the rest of the time, I do YouTube. So, you know, that's something I want to do. So, I don't know if I would. I've turned down other jobs doing things people wouldn't normally turn down.

**Dave Jones:** Who are the major players in this space at the moment? What, robotics? Yes. Yeah, in the sort of stuff like the Boston Dynamics kind of robots. I mean, surely they're not the only players.

**James Bruton:** Well, I don't know. So, there was obviously Honda and Asimov. Asimov.

**Dave Jones:** I've seen Asimov. It was pretty poor. Is Asimov being retired now or something? I think so. Because, yeah, when I saw it.

**James Bruton:** He danced his hips off, probably.

**Dave Jones:** And it fell down steps. And, you know, it just, yeah. It was good for the time. It was groundbreaking, you know. But now it's like kind of like just funny to watch.

**James Bruton:** Yeah. So, Toyota did some stuff as well. Right. I mean, none of them are really, they're not, I mean, I guess these are R&D projects. Yeah.

**James Bruton:** Yeah.

**James Bruton:** Rather than, so Boston Dynamics are going to be selling spot minis. That's, I guess, the first company who actually made a, yeah. Right. The first company have actually said, well, this is our product now. Oh, okay. Whereas you can never buy an Asimov.

**James Bruton:** They're actually hiring like crazy for that right now, if people don't know. So, if you want to go build robots, Boston Dynamics will hire you, apparently. Right. It's crazy.

**Dave Jones:** Okay. And I assume they're based in Boston.

**James Bruton:** Yep.

**James Bruton:** Yep. Okay. Just a guess. Didn't they come out of MIT or something?

**James Bruton:** I forget where the guy started, the founder started from.

**James Bruton:** Was it all to do with the MIT leg lab?

**James Bruton:** Maybe. Yeah. I don't know. I don't know. Yeah. So, I don't know.

**James Bruton:** I mean, I guess in terms of actual robotics companies, there are a number of robotic startups that Google acquired, but they did have Boston Dynamics at one point, didn't they? But they've sold it. They did. Oh, did they?

**James Bruton:** Yeah. Oh, I think so. Yeah. That was Andy Rubin, the guy that started Android and has been in the news for not great things lately. He basically was bought by Google. Android was bought by Google. And then he went on a buying spree at Google and bought a bunch of robot companies. And then he left. Yeah, right. It's like, okay. So, yeah. What's it called? Rethink just closed, though, too. So, that was a robotics company, right? Right. They were an assistive robotics company. Rethink Robotics did, like, the Baxter robot. So, they just closed. They just shut their doors.

**Dave Jones:** Well, it's not surprising. Ultimately, you've got to have a, you know, you've got to make money, right? This is a business. I mean, there's not many organizations that can just sink, I don't know how many tens of millions they've put into, you know, this sort of R&D.

**James Bruton:** Well, SoftBank saves the day again.

**James Bruton:** Yeah, so I guess we should, I guess we're honorable mention to Onki or Anki, who obviously I did a paid review recently for Vector. But they've done quite well. So, they've had a lot of VC funding. And they also, I think their Vector, you know, Kickstarter did about $1.8 million or something. But that's only going to last so long, though. Yeah, sure. But, I mean, the basic roadmap there is to make robots interact with people better. So, you know, there's a lot of comments on the video that doesn't do very much. Right. But, you know, that's the first, you know, one of the first steps on the roadmap. So...

**James Bruton:** And what is Anki?

**James Bruton:** It's a, well, Anki's a company. They made Cosmo, the little robot with the scoop thing that picks up the blocks.

**James Bruton:** Mm-hmm. Oh, okay.

**James Bruton:** And now Vector, which looks very similar. But it's, instead of being sort of smartphone-driven, it's, you talk to it and you can just not have the phone and it's very interactive.

**James Bruton:** That was like a robotic pet type thing, though, wasn't it?

**James Bruton:** Yeah, it recognizes your face and it all, you know, it's almost a home assistant.

**James Bruton:** Yeah. I saw, I think, a Wall Street Journal article about, like, personalized robots and how they're just kind of more cutesy than they are functional. And it's like, well, why are they there? And the answer is, because people buy them.

**James Bruton:** Yeah, I mean, that's the appeal. So, people either love it or they hate it, I think. And a lot of people love it. But, yeah, it's very interactive. It's like a pet and stuff. But it is small and you can put it in your pocket and take it around with you. So, I believe.

**Dave Jones:** Have you seen that Pleo, that robot dinosaur? Yeah. You know? Mm-hmm. What did you think of that? Because I thought that was really cool. That's a few years ago. Yeah, yeah, it's a long time. I've never actually seen one in real life. Yeah, I've got, like, a one that hasn't got its skin on. It's been skin. Oh, right. It's very cool.

**James Bruton:** Yeah, sure. I mean, that's, yeah, I mean, even some of the robot toy BB-8s and stuff, you know, are quite interactive. And so, if kids love the character, then, and of course, the Wowie robotic stuff like Robo Sapien and all of those, Robo Raptor and those things. So, yeah, I mean, that's, at what point isn't it a toy anymore, I guess, is the question.

**Dave Jones:** Right.

**James Bruton:** When it kills you.

**James Bruton:** When it kills you. When it's of some use. Is Amazon Alexa a toy?

**James Bruton:** Right. Right. That's a good question. Hmm.

**James Bruton:** It's useful when kids come around and they want to ask stupid questions like, what's, how big is a whale? Yeah, yeah. How many microseconds until Christmas? It's just like, yeah, ask Alexa.

**James Bruton:** I think if people are listening at home right now out loud, then you might have just asked for them. Sorry.

**Dave Jones:** Right, yep.

**James Bruton:** Alexa, the amp hour, a five-star rating.

**Dave Jones:** Please, Alexa, please order a Ferrari. Sorry, it won't understand my accent, will it? No. It's hopeless.

**James Bruton:** So this is an interesting, I think, you know, as we go into the toy space too, it's interesting because some of them are, you know, quote unquote autonomous. I wouldn't actually give it that word, but I'd say, you know, drive by wire or not. And you're kind of in that space as well. As you're testing, you have that monstrous controller rig thing you have. So what is that thing and how does that end up interacting with like the open dog at least?

**James Bruton:** So, sorry, which thing? The handheld controller?

**James Bruton:** The controller, yeah, that you have. That is, I don't know if it's wired or wireless.

**James Bruton:** I know it's wireless. It's on Bluetooth. Well, it's a transparent serial link over Bluetooth 2 or something with an Arduino Mega in it. But yeah, it's just purely physical controls. So yeah, there's six, well, two, three-axis joysticks for the six-axis kinematic model at the moment and a bunch of buttons that send ones and zeros.

**James Bruton:** Okay. It's pretty much it at the moment. What I'm going to ask about it is like that seems like the next step up, right? It's like, so like, I don't know what the official definitions are, but like right now, like the open dog is, it's a collection of, you know, parts and motors and gears and whatever, but it's still being, you know, controlled by you. You're just giving it the high-level controls. I would assume that at some point there's another layer above the, so like there's a control layer, which is just saying, you know, forward, backward to the controllers. And then there's, I guess, a lower level than that. But then also above that, then there's a coordination layer that we haven't talked about yet. But then when you have a handheld controller, then that's taking the place of like, you know, an intelligence layer of like, oh, I see a thing, I react to a thing. And that's kind of what we were talking about before with where Boston Dynamics is.

**James Bruton:** Yeah, sure. So I guess there's a thing called ROS, which is the robot operating system, which is an open source robot, like multi-node network platform. So there's already lots of stuff in that, like SLAM, which stands for simultaneous location and mapping, where it'll have sensors. You could use an Xbox Kinect or a more expensive laser scanning rangefinder, and it'll, you know, move around, map out the room, work out where it is and build the map at the same time. So in the Boston Dynamics Spot mini video, where it's going around a factory or something or around some sort of warehouse, and you've got the little inset picture of it building the map of the walls and all the stuff in 3D, pretty much all of that stuff is already open source and probably can be made to work without too much trouble. So I guess that's the next step for me would be to get into that. But yeah, you mentioned coordination. So at the moment, the joysticks control the six axis kinematic model. And depending on what I was dabbling with, one of them might try to make it walk forward. But obviously, we're not controlling individual legs with individual physical controls. We're going to have some sort of gate built that, you know, you push, hopefully you push forward and it leans forward until it can't lean anymore, then it starts taking steps. And obviously, as you operate the yaw control to rotate it, it'll walk around or sidestep with the other, you know, translation joystick. So that's sort of the coordination layer. But that's still basic functionality for remote control, though. And then that would be driven by some more intelligent layer to make it navigate or whatever it is with a bunch of sensors.

**James Bruton:** Yeah, it's almost like, like, what is the, I guess, what is the type of commands you're sending to each layer, right? So like the lowest layer is basically sending electrons. And then the next layer up is sending like raw bits. And the next layer up from that sending like encoder counts. And the next layer up from that sending, I don't know, what's getting sent to the thing that controls the controller? I guess that's serial that's going from a centralized controller to the individual Arduino.

**James Bruton:** Yeah, that is at the moment. Eventually, it'll be one higher power microcontroller and everything will be on CAN bus.

**James Bruton:** Oh, OK, OK.

**James Bruton:** So I just need to, I've just got another O drive to make a test rig and test the CAN bus stuff that's in beta to see if that works. So basically, at the moment, I've got one master Arduino. And then that sends serial to two slave Arduinos. And that's because I need six serial ports. OK. Because there's six O drives.

**Dave Jones:** For those who aren't aware, sorry, what's the advantage of the CAN bus?

**James Bruton:** Just, we can just put all of the O drives on one bus and that'd be it.

**Dave Jones:** So it's just a wiring point of view?

**James Bruton:** It's a wiring. A CAN bus is what's used in cars, of course, to trigger airbags and everything else and the ECU and all of that stuff. So it's much more efficient, I guess. And never goes wrong, hopefully. Yeah. The other thing I'm waiting for in the O drive development is the end of the basic zeroing the encoder when you hit an end switch. Yeah. So that wasn't there when I started. So that's why I've got two other Arduinos that don't get rebooted when I reboot the master, which has the main code on it. Right. So that they can calibrate once on power up, keep the zero positions. And then I can keep flashing the master with different changes to the code without having to recalibrate every motor and every end stop again. Yeah, of course. So once they've put in CAN bus and zeroing the encoder, essentially, and keeping that on the O drive, then I can throw away all my stupid serial strings. Right. Yeah. Just have one, like, one teensy 3.6.

**James Bruton:** Yeah, those things are beefy.

**James Bruton:** With CAN bus built into it.

**James Bruton:** Yeah. That's it. So, and what is the programming look like right now? So you basically have to, when you calibrate a single leg, you have to basically go and reprogram that. You plug into it with a USB port and you reprogram it there?

**James Bruton:** No, the calibration on power ups all built into the Arduino code. Oh, great. So it just initializes the O drive, says do the calibration. Then it says move it slowly till you hit this, you know, switch. Now what's the encoder account? Take that away to get from itself to get zero, essentially.

**James Bruton:** Yeah.

**James Bruton:** And then keep that, please. Got it.

**James Bruton:** Okay. So what if you want to actually change? So like you say, you were just talking about what that Arduino is actually going through and the kind of routines it has. What if you want to actually reprogram that Arduino though? Are you able to push code down from a centralized processor or do you just plug in and say, oh, I'm redoing all of the legs to different firmware today?

**James Bruton:** No, I just plug into the Arduino and program it from the Arduino IDE on the PC.

**James Bruton:** So it's USB. Cool. Cool. What about the powertrain on this thing? I mean, this is, you're not talking about little amounts of current. So like what is, what's going on with that?

**James Bruton:** No. So it's running off like drone LiPo batteries. So six cell LiPos, which are roughly 24, 25 volts when they're charged. And it looks like some eight mil studding with nuts on built into a 3D print, which with loads of like basic eyelets crimped onto cables to make a massive, horrible junction. It would be terrible if you drop something metal on it. And then, you know, six lots of wires go off to the six O-drives and there's no fuses. Nice. Well, when the battery melts, then it, you know, it fuses itself. It's a self-fusing system. Yeah. I mean, the O-drives are pretty good. They've got like short circuit protection and all, and thermal protection and stuff. So.

**Dave Jones:** How much does the open dog weigh at the moment?

**James Bruton:** I think it's about 40 kilograms.

**Dave Jones:** Right. That's a lot.

**James Bruton:** I can pick it up. Yep. Just about. But it's not pleasant. Yep. Right.

**Dave Jones:** Especially if it's kicking and screaming.

**James Bruton:** Most of it's, well, there's an emergency stop, which resets all the O-drives and kills all the motors, but it doesn't cut power.

**Dave Jones:** Oh.

**James Bruton:** Because I don't know what to cut the power with. I mean, what would I cut power with? A massive contactor.

**Dave Jones:** Well.

**James Bruton:** Like how many hundreds of amps do I need to turn off? Yeah.

**Dave Jones:** I mean, usually you'd use a remote contactor to do that. You'd, you know, have like a smaller remote switch, which then controls a big SCR, you know, or something like that.

**James Bruton:** But for now, it just, there's just a little, a little emergency stop that just brings the reset pins low or whatever it does. All right. All the O-drives stop. Well, eventually it runs out of juice too, right? So. Yeah, it does work. Um, yeah. So the main weight of the thing though, is all the ball screws and all the motors.

**James Bruton:** Right.

**James Bruton:** Yeah. Right. So there's, yeah, 12, 1605 ball screws and all the metal bearing mounts at each end and the 12 brushless motors, which are, uh, 65 millimeter diameter, 74 mil long and mostly full of copper and magnets. So that's most of it. When I got those in the box, that was the test was to pick up both boxes at once to see how much the robot would weigh. Oh my God. Well, apart from the bits of place, aluminum and extrusion, that's pretty much all the metal. Wow. Jeez.

**James Bruton:** How did, how did you, how did you get started like learning about the, it's all linear actuators you said? Sorry, what was that? Is it, you said it's all linear actuators or other things as well?

**James Bruton:** Yeah, that's all it is. It's loads of ball screws.

**James Bruton:** Oh, ball screws. Okay. Okay.

**James Bruton:** Basically in V wheels running on a V slot extrusion.

**James Bruton:** How did, how did you get started learning about like, so I'm thinking about this mostly from my perspective, but also hopefully the, the audience's perspective, like where's a good place to start on the mechanical side of things? Cause we don't usually talk about that stuff here.

**James Bruton:** Yeah. So I don't really know. And I guess that's what the video was that I put out today was me trying and just making it up as I go along. People ask me how do I, you know, you in YouTube comments, even how do you know all this stuff? And I normally just say, I make it up as I go along. And that's mostly it, you know, it's by having spent a lot of my own money in the past. The junk pile speaks for itself. Just trying to build these robots and then spend patrons money. And, uh, you know, on it goes really just make, uh, but having a bigger budget and buying better stuff and thinking, what if I do it this way, what will happen?

**James Bruton:** Yeah. Solving, solving new problems as they pop up kind of thing. Yeah. Yeah.

**James Bruton:** But yeah, I honestly don't know where you would start now. If you had never done anything like this, I guess start with some servos and some bent paper clips and popsicle sticks. Right. Or 3D printing. If you've got a 3D printer, of course. Right, right. Well, that's a, you know, and that's a good thing is 3D printing allows you to prototype stuff pretty cheaply. Yeah. And using Fusion 360 to simulate the joints.

**James Bruton:** Oh, okay. So, so when you, when you work back to the CAD model, you're actually simulating larger parts as well. Like you're, you're kind of drawing everything out and, and. Yeah.

**James Bruton:** So there was a complete CAD model for it, which I, and the thing is open source. Open Dog is, of course, open source. So I've published the CAD and I've published all the code. Nice. Which sometimes brings more criticism than. Yeah. Well, maybe it should bring that much criticism because I'm not that good at coding.

**Dave Jones:** No, it doesn't matter how good you are at coding. Someone will criticize it. Seriously. Yeah. It's.

**James Bruton:** I'd say. Yeah. Even outside of coding. I mean, it's just, there's always going to be someone who's like, yeah, well, there's this little thing over here and that's the thing I noticed. Yeah. So.

**James Bruton:** I mean, the CAD's not gone, gone down too badly. There's someone has done a solid works model with a full inventory for all the nuts and bolts, which I never put in. Wow. I was going to say. And several people have done that. Yeah.

**Dave Jones:** How many people have actually taken your stuff and actually built upon it?

**James Bruton:** I don't, I know there's only one person who's building Open Dog. Right. Who's a patron. Who sent me some pictures of some of the prints. Neat. That's great. Um, I don't know if I'd recommend anyone do it now because, you know, it doesn't actually walk properly yet. Right. But, uh, you know, if you want to, then that's fine. I mean, I think it will walk because it's more than powerful and agile enough.

**James Bruton:** Yeah.

**James Bruton:** Uh, and maybe the person's better at writing software than I am. So maybe they'll make it work better, quicker and better than I do. So, and that's good. That's the whole purpose of publishing it. I'm never going to sell it as a commercial product.

**James Bruton:** Yeah.

**James Bruton:** So it might as well be open source.

**James Bruton:** I mean, I'm honestly kind of confused on how Boston Dynamics is going to sell it as a commercial product, so I wouldn't worry too much about that.

**James Bruton:** Yeah. I guess it's like the thing is about going over multiple different terrains. Yeah. I suppose for surveying or something like that. So once you've got a robot that can navigate and walk on rocks. Yeah. You can do it. You have it go and scan barcodes. Can't you even do an inventory? I don't know. I guess so. Right.

**James Bruton:** It's like having a, I don't know. Search and rescue. I guess so. I, again, all these things, like I'm sure, I'm sure there's, you know, I'm sure someone somewhere has done market research on this. I just, I have a hard time imagining, imagining what I think the price tag of what they're going to sell is going to be, and then thinking about who's going to buy it. It's like, yeah. Okay. Well.

**James Bruton:** I think it was hundreds of thousands. Oh, yeah. Sure.

**James Bruton:** Good Lord. Yeah. Yeah. So a little further away from Iron Man than we would all hope, huh?

**James Bruton:** Yeah, maybe. I did build an exosuit. That was another project. Yeah. So tell us about it. That's currently more and more pieces snapped off it, and it's now even less. I was going to say. Yeah. I've robbed pieces from it, and it's now, I've got both legs, but it did keep falling over and more pieces broke, so it just suddenly go crash in the night. Oh, man. So I stripped it right down now. No.

**James Bruton:** So, what was it?

**James Bruton:** What was it? So I, what on earth happened? I finished, was it Hulkbuster or was it some project, one of the other robots, and I did a poll to see what viewers, which was always a massive mistake, what viewers like to see me make, and I can't remember what the options were, but one of them was a real Iron Man suit. Right. Job, of course, everyone voted for. Right. And I started with, I'll just make one arm that makes me stronger, and I made this horrendous thing with a massive, it had brushless motors in, actually, and a 3D printed gearbox of nylon gears that then pulled blocks and tackles that pulled a chain around a massive sprocket. And it was pretty high powered, actually, and terrifyingly noisy and rattly. And then, obviously, it was really heavy, so I made a couple of axes of the arm, and I was like, I can't carry this round, and it's stupid. Yeah, I'll make legs. So I did XAC version one, was essentially this huge parallelogram leg thing with bungees and strings pulling blocks and tackles to pull this thing. I could just about walk along in, and then I refined it to actually use, the first time I've used ball screws and the brushless motors. So I didn't have O-drives, I was using skateboard ESCs and feedback pots attached with pulleys and bits of fishing line to each joint. And yeah, I could just about walk along in it. And then I built arms on top of it, and then it attacked me. And part 25 is all you need to watch, really. All right. All right. And then basically pieces broke while I was in it, and it got confused because the feedback pot string fell off, and it mashed me.

**James Bruton:** I mean, that's the problem is when you put squishy middle stuff into the hard robot thing.

**James Bruton:** It wasn't that bad, but it was like a proper out-of-control Iron Man suit. Yeah. So yeah. But I mean, yeah, there's a whole series of it, but it's a pretty horrendous torture device looking thing.

**James Bruton:** Well, I'm glad you made it through it. I mean, we wouldn't have you here otherwise today, you know?

**James Bruton:** Yeah, I guess one of the challenges with that was making it move when I moved, which it did, which was kind of interesting, which I had these. So again, I had V wheels in V-slot extrusion, and I had these kind of levers that you held onto, and one above and one below my feet, and hall effect sensors and magnets. So as I slid them, it gave me sort of a proper linear response. And that's how it controlled the... It basically went round in every cycle. It added that value onto the motor position. So as you kept pushing, the faster you... Or the harder you pushed, the faster the motor would go. And when you stopped, it stopped. But it still knew what position it was in. So each motor still had its own feedback, so they wouldn't run it at their end stops unless the string falls off. Right. So yeah, that's how I managed in the end to get it to sort of sync up with my motions.

**Dave Jones:** You've got so many major projects. Like there's, you know, like as if Open Dog isn't enough, you know, and the Exo suit isn't enough, and there's, you know, a Batman board. Oh, yeah. And like, how long, how many hours do you spend on these projects? I mean, just, you know, one of these builds is just, you know, crazy amount of time.

**James Bruton:** Yeah, I mean, people were, so I took Open Dog to TCT Show, which is a 3D printing show in the UK, and people were like, wow, you know, how long has this taken to make? And I'm like, wow, well, part 10, so that's 10 weeks, you know, including designing all of it and making a test leg and learning to use my CNC machine in two episodes to actually make the parts. Right. You know, so, but yeah, I don't know, really. I mean, I get the videos out every week. I do my 16 hours in my other job. And sometimes I don't work at the weekends. Wow. But, you know, having 11 3D printers is helpful to make all the parts in time. Yeah, so I'm supported by Longspot. Is that just for volume? Is that? Yeah, basically. So I don't use all of them at once, but there's some specifically for flexible material. Some of them with more struders, which are the much fatter nozzle for blocking parts. Of course, yeah.

**Dave Jones:** So it's easier just to have separate ones than it is to like just rejig each one each time for a different material, different head.

**James Bruton:** I do swap the more struders out for normal extruders sometimes, but I've got a couple that are dedicated for doing flexibles. Mm-hmm. One dedicated for ABS. Yeah. And, yeah, the rest do general printing. But, yeah, with Open Dog, for instance, if it's like four legs and there's four brackets, just have four printers doing it at once. Right. And it takes the time of one instead of the time of four.

**Dave Jones:** Well, that makes sense. You know, when you're doing dedicated videos like this every week with 3D printed parts and stuff. Exactly, yeah. It makes sense to have, you know, many optimized jigs to do that.

**James Bruton:** And the CNC machine as well. So cncrouterparts.com gave me a rather nice machine. So that's really good for, you know, making a video in a week of just routing out plywood or aluminum or whatever. Right. Because, obviously, that's a fraction of the time of printing. So, yeah, I've got some more projects coming up next year. I'm going to try and do some more general purpose shorter series. So Open Dog is generally only every other week. Right. And then I do something else on the off week. So I'm going to do some stuff like a toilet cleaning robot and a kitchen assistant robot. Like, which is maybe three parts, you know. So literally a robot that can drive up to the toilet bowl with two brushes on arms and follow the contour and squirting detergent. And, you know, it'll still be a serious series, though, about, you know, making it probably out of plywood and 3D printing. It'll have PID controllers. It'll have feedback and, you know, might have a kinematic model or it might not. Not decided yet. And it'll probably be speech activated either with Alexa with an EPS 8266 or it'll be using a Raspberry Pi and Google WebKit API or something so you can ask it to clean the toilet. Right. And it'll be open source hardware. It's most important.

**Dave Jones:** Everything must get much easier now that you have this large amount of, like, you know, just modular code and hardware that you can call upon to make this sort of stuff. Is it easier now than it was back in the day?

**James Bruton:** It is easier. Well, it's easier than back in the day, obviously, yeah, with Arduino and stuff. But I think also the experience of doing it, and that's one of the things I touched on in today's video is I tend to design things right first time rather than making something that's a complete disaster and then saying, oh, you know, where's, what shall I do with the video? It's like, this is rubbish. Right. It's normally fine now. And every week I know pretty much that I'll just design the parts and it'll work. Mm-hmm. So I guess that just comes down to knowing, you know, being able to grab a motor and feel how much torque there is and know that'll do and then work out roughly what gear ratio you need and will this leverage angle be strong enough kind of thing.

**James Bruton:** So it's almost like rules of thumb. And it sounds like on the modeling side, too, that's a pretty critical piece of your workflow. Is that accurate? Yeah.

**James Bruton:** So definitely doing the joint simulation in fusions helps a lot.

**James Bruton:** Mm-hmm.

**James Bruton:** Because even though you like to think you can work out the mechanism, sometimes it's completely wrong. So prior to that, I would have used Technic Lego basically to actually make a hinge and go, hmm, does this four-bar link with an offset piece and a funny crank move the thing in the right direction? Whereas now you just do it in fusion and make as-built joints and move them all around and see that your sliding thing moves the thing enough distance.

**Dave Jones:** And then you press print. Is that the idea? Is that the idea? Well, pretty much, yeah.

**James Bruton:** You press it a couple of times, apparently. There's a couple of steps in between, but you're not far off.

**Dave Jones:** Okay.

**James Bruton:** Yeah. Nice. I like that idea, though, of like the kind of having stuff on the shelf, especially from a prototyping perspective. That seems like that's extensible to a lot of things that we normally talk about on here. You know, having a micro that you always go back to or having code that you go back to or in your case, mechanical stuff you go back to, that kind of thing.

**James Bruton:** Yeah. And I guess, I mean, just having loads of parts as well, hanging around the house is useful. So what was the, there was one week I just didn't, I was to be doing something with Batman, but something hadn't arrived or something like that. So I was like, I don't have a project. And I just thought, I know, I'll make a mini electric motorbike I can ride on. And I made it out of all the things in my house. Nice. So it had like tiny eight inch wheels that were spare from some eight inch casters and a motor and a belt that I happened to have and some T5 pulleys and bits and pieces and twist grip I had that was left over from the virtual reality hover bike project and some other bits and pieces. I strung together and made this mini motorbike. And I made it in about three days with CNC and then rode it around the Science Center car park. Oh, jeez. And that was that week's video, you know.

**James Bruton:** Right. That's great. It's not, it seems like you're, at least where you shoot the videos is not a huge area either. So like, what is, what does your shop look like?

**James Bruton:** Oh yeah. So it's basically the loft room. So I've got a 3D printing room that's got all the 3D printers in. The loft room, which is what you see on video, it's actually 30 by 10 feet. So it's quite long.

**Dave Jones:** I've seen you drag open dog up the stairs to get to the, yeah.

**James Bruton:** That's got, my staircase is really annoying. It goes round and round and round. Oh no. So it only just fits around the turns. Oh no. Jesus. And it's heavy, obviously. And there's just no other way but dragging it. And to get anything up and down, in fact, is really difficult. Bear in mind, I built Hulkbuster in here as well. Wow. Seriously.

**James Bruton:** Oh my God.

**James Bruton:** Everything else. So yeah, so that.

**Dave Jones:** Any thought about getting a bigger space?

**James Bruton:** Yeah, potentially it's just paying for it. Property prices aren't that keen around here. Oh, okay. Generally in the UK, of course. So yeah, I probably should move to a cheaper area and have more outside space and build workshop space.

**Dave Jones:** Oh, okay.

**James Bruton:** But you know, that's something that's a bit of an ordeal. So yeah, I'm doing a big, this big secret project is actually really big. I was building it in the lounge, but it's too big. It's outgrown the lounge. So now it's basically in a gazebo in the garden that's three by six metres and three metres high. That's the only place it can go till it's all done with. So yeah, that's the only thing to do at the moment. I've got a small garden shed while I do welding and stuff, which is only, I can't stand up in properly. And so the, yeah, sorry, the other workshop, I've got like this sort of fake workshop, which is in one end of my lounge, which is a set, which is where the CNC machine lives.

**Dave Jones:** Oh, goodness. Yes.

**James Bruton:** So that's actually, it's just a set made of wood and a wooden frame.

**Dave Jones:** I suspect you need to take your Patreon money and use that as rent for a bigger, for a large

**James Bruton:** workspace. Yeah, but then I'd have to commute to a place and go to work instead of just being here. And then, you know, if I run 3D prints through the night, if it gets desperate, sometimes I'd get up in the night and start another print. Right. Wow. If I had a workspace, I'd end up just never coming home. Right.

**James Bruton:** Yeah, you're right. Dave, you're going to associate with us, man. You just, you just combined workspaces because of that exact problem. I know.

**Dave Jones:** Yeah. It's because I had to commute between the workspaces. Yeah. Yeah. And, and I got home as well. No, I, well, yeah, I had two separate spaces. I had my lab where I recorded my videos and then I had a separate editing office.

**James Bruton:** Oh, yeah, yeah.

**Dave Jones:** I remember you saying, yeah. Yeah. So, and I had, I had that for two years and I just went, well, you know, look the, you know, the lease was up. Were they not in the same building? No, no, they're not in the same building. Oh, right. Okay. They're at the other end of the business park, you know. Technically I can walk between them, but you know, it's like, yeah, like, like if you're sitting here and like I'm editing my video and I go, oh, I just want to do one more shot. You know, it'll take me five minutes to do that or a couple of minutes to do that shot. No, I've got to go back to the lab and, you know, so it just never happens because it's just so inconvenient.

**James Bruton:** That's interesting actually. So I guess you do all your video and then you edit afterwards.

**Dave Jones:** And then I edit afterwards. Yep. That's it.

**James Bruton:** Yeah. I can never do that because if it's something, well, it's probably you found the same where you've, I don't know, maybe you're more careful, but maybe the mic comes unplugged or it wasn't in focus or something. Right. And I guess you could go back and do the shot again. If it's a tear down, you have to take all the pieces again, but. Yeah. No. It's like, oh, I've got to disassemble the whole thing or I've got to, I can't unpaint something or unglue something together. So generally I edit shot by shot. So I do two or three shots and then I edit it in on the timeline. Oh, and then you edit in the timeline.

**Dave Jones:** Yeah, right. That's interesting.

**James Bruton:** So then I can check that actually it was all right. That thing was in shot, you know, or it was in focus.

**Dave Jones:** No, I see that.

**James Bruton:** That just wasn't an option for me. Well, I didn't say the wrong thing.

**Dave Jones:** Yeah, no, that was an option. Everything's on the SD card. I've got to take my SD card to the office and I edit. And if it's not, it's not right. I've got to do overlays or a voiceover or, you know, something like that.

**James Bruton:** So I'm sitting basically open dog is I can touch open dog and touch my keyboard while I do editing. Yeah. Well, that's his thing, you know, it's in the same room. Yeah.

**Dave Jones:** So I'll be able to do that now. Basically I can do like, you know, I can edit as I go, so to speak. And like occasionally I've kind of like, I've done that. I've like gone back and gone edit and I'll finish it tomorrow. And having a look at the edit going, oh, okay, now I think the video can go in this direction. So it's, you know, it kind of gives you an idea.

**James Bruton:** Yeah. You kind of look at what you've done. Well, I do at least look at what I've done with and then with fresh eyes the next day and then say, right, where did I get to? What's the next shot that needs to happen kind of thing? Or how long is the video long enough? Yes, exactly. Or maybe I won't do quite so much in this video.

**Dave Jones:** Yep. Yep. So that's the plan. So I can.

**James Bruton:** And James, do you document outside of video as well? I mean, is that something that you, like, or does, I guess, I guess more broadly, does the, does the documentation end up, does the documentation end up impacting the product project rather because of, because of, you know, like what you're talking about?

**James Bruton:** The things on my website, which are mainly photos and some Mickey Mouse text and a link to the YouTube video.

**Dave Jones:** Nobody does documentation anymore. All it is is jumping, dumping everything to GitHub, you know, dumping your schematic. Yeah. Dumping it. Nobody does.

**James Bruton:** Mostly, I mean, the video is documentation to some extent. Right. That's just something that now goes along with the build. You know, it's every day I'm doing video, doing a bit of a build. So it's just something that's part of life, really.

**James Bruton:** Got it. Yeah. And that's, I mean, I think that's really impressive that you kind of have this consistency around, around cranking out stuff on a weekly basis. I think that all kind of feeds into it, you know, like having a daily video that then makes the weekly video and all that other stuff.

**James Bruton:** Yeah. So there was a, I mean, there's been a video every week for what, I don't know now since 2013 or something like that. Yeah. So yeah, it's been, been pretty consistent.

**James Bruton:** Yeah. That's, that's, that's the important piece. That's.

**Dave Jones:** That helps because it drives you now, oh, I've got to actually do something. I've got to produce something, you know.

**James Bruton:** Yeah. I mean, it does to some extent, but to some other extent. It's a, yeah. I don't know. I never feel it's my best quality work. Exactly. Because I've always got to get the video done. Yeah. Whereas if I didn't have any deadlines. True. So, but then I don't know if I would produce as much or I wouldn't, I would be lazy or, you know.

**Dave Jones:** That's the dilemma of a YouTuber. Unfortunately, it's, you know, you, you want to produce content and please your audience, but then you want to often, you know, take more time to do it better. But then you go, oh, I haven't released. I can't go a whole week without releasing a video, you know. So.

**James Bruton:** Yeah. I mean, the audience is a funny thing. I don't know. It's quite hard to have diversity in my channel, I think. I think unless it's a robotics build, people don't watch it as much. So. People have very specific expectations. Quite a tricky one. Yeah. Yeah. So I don't know. In some ways, maybe I shouldn't be doing everything I do. I don't know. There's, you know, other channels, other maker channels who do far less for far more views. Right. As well as I say, naming no names. Yeah.

**Dave Jones:** No, that's just the way it is.

**James Bruton:** Is he on this call right now, James? You can, you can tell us. No, no, no. It was a joke. What do you, I mean, when do you, when do you find you, I mean, so that when you're in this mode of consistency, like when are you learning the most? Like what is, what is it that, like what activities are drawing the most inspiration for the next thing? For me? Yeah. Yeah. For you.

**James Bruton:** What's, so what's, so like, I guess when I have to, I'm outside my comfort zone when I have to do something like, well, I guess when O-Drive came along and I'd never seen one before. And then it's like the first, well, they come with firmware on now, but the first ones you had to flash your own firmware on there and compile it and everything. It's like literally a day installing all the tools and working through it. So I guess I learned a lot from that and now it comes with firmware. So it's not so bad, but you know, you need to upgrade it at some point, but they've got USB utility now to do it instead of a STM programmer and things. So I guess when there's a new, a new thing comes along like that, I haven't worked with before. That's I guess when I learned something. So we're talking about the toilet cleaning robot. That is going to be stuff. I don't have to learn anything. That's going to be Arduino mega 2650s and the PID library and feedback pots or encoders and motors and mechanical linkages and plywood. Right.

**James Bruton:** Okay. So stuff that's in your toolbox already that you're ready to ready to deploy as needed.

**James Bruton:** Yeah. So it's interesting. I mean, I ultimately, you want to make YouTube videos that are less effort to you, but have the biggest impact.

**James Bruton:** And, and toilet cleaning robots will have a lot of impact. You're saying? Well, let's hope so.

**James Bruton:** So the other one that I'm doing at the moment is a robot that fights a human. So that's even less impact to me because it's another student project.

**James Bruton:** So I mean, if the robot wins, it'll be some impact to you.

**James Bruton:** Well, yeah. So my, my friend is the course leader for computer games design degree down at Portsmouth university on the South coast. So he's got, I've essentially, I'm a commercial sponsor for a project in inverted commas. So my team are making a virtual reality game of fighting a robot with a stick and a shield. Only the stick and the shield are real and the robots also real. And it's literally looks like a classic thing with, it's got boxing gloves on pneumatic arms, which I've used foot pumps in reverse because they're cheap pneumatic cylinders and they only have to go in one direction. It drives around on a wheelchair base, encoder driven. And it's got these two pneumatic punching boxing glove arms. That's about six feet tall. And so basically there is controlled by a really simple serial protocol. So they're using unreal engine, I think to do this virtual reality game, but essentially you fight the robot, but when the robot punches you, it really punches you. So most virtual reality stuff, you know, it's pretty boring watching someone doing VR if you're not in the immersive experience. Right. Whereas for this, what you'll see on the video is someone actually fighting this thing that's a robot with boxing gloves. And then we're going to 3D print some of the character stuff they design and put it back on the physical robot. So I'm hoping that's going to do pretty well. But of course I've built this thing that was pretty basic and then they're making the rest of the content. So I just go down and film it. And that's another really good way to make content, which is to sponsor a project.

**Dave Jones:** You've got to get a professional boxer. Take a, that's like, well.

**James Bruton:** Get like Manny Pacquiao to fight it or something.

**Dave Jones:** Well, you know, just a local, you know, like some, you know, someone who's actually had professional fights or something, you know. Yeah.

**James Bruton:** So they've got this, the challenge is they've got to have their hands tracked. So they've got at the moment a stick and a shield that have got Vive trackers on that track them into virtual reality. And I don't know if anyone wants to get that close to it anyway. Because if they do punch it, it's made of wood and stuff. Right, right. But yeah, I mean, that's, we could get some other sort of MMA fighter, I guess, or a fencing person. Fencing person. There you go.

**James Bruton:** Yeah, yeah, yeah.

**James Bruton:** Who's famous though for that? I don't know. Yeah. That's a good thing to think about.

**James Bruton:** You guys don't follow fencing? Come on.

**James Bruton:** No. More to someone, I don't know, who's famous, whatever. Yeah. Who fights with a stick and a shield? I don't know. I don't know. I want to get like someone who's played Conan the Barbarian or someone.

**Dave Jones:** But there's YouTube channels. You could do a collaboration with Star Wars Kid. You could do a collaboration with those sword fighting channels. They're huge.

**James Bruton:** Oh, that's true. Are there any English ones? The problem I have with collaborations, there aren't that many people in the UK.

**Dave Jones:** Hey, try Australia.

**James Bruton:** Exactly. Yeah, I know you met, what's his name, Angus from 3D printing, Maker's Muse.

**Dave Jones:** Oh, yes, yes, exactly. But yeah, that's probably it. That's about the only other person I know in Australia. Exactly.

**James Bruton:** Yeah, so the last collaboration I did was Ivan Miranda in Spain. So that's the 3D printing guy. So we did a rocket challenge where we tried to make electric rockets that would take off, hover and land on their bottoms. Oh. But yeah, that was fun. So we went to Spain for two days to do the challenge. Yeah, so there's Tom Stanton in the UK who does some aerodynamic stuff. A good video he did was a wheelie cheat device for his bike. He used an inertial measurement unit to measure the angle that he was leaning back on his bike and hit the back brake when he got to a certain angle so he could do wheelies without any effort. Right. Oh, wow. That's cool. So he's someone I'd like to work with. Yeah. Yeah, it's pretty limited in the UK otherwise. Right. Have to look to Europe and the US, really.

**James Bruton:** Well, you've done stuff with Colin as well. So that's... Oh, there's Colin. How can I forget Colin?

**James Bruton:** Yeah. I know, right. Colin who?

**James Bruton:** Colin Furze. Colin Furze. Okay. Yeah.

**Dave Jones:** Do you watch his stuff? I've seen stuff, but I don't follow it.

**James Bruton:** Okay.

**James Bruton:** His stuff is insane. It's absolutely bonkers. And that was the Hulkbuster that you mentioned earlier. I meant to mention that, I think.

**James Bruton:** Oh, that was one of the... That was Hulkbuster 2. I built another one years ago. There was a costume. Oh, really? Okay, okay. Yeah, I didn't build that one upstairs in my house. Oh, okay.

**James Bruton:** Yeah, we built that in Colin's garden. Got it. That was confusing to me when you said it, so that makes more sense. Yeah, no, no. That was another costume.

**James Bruton:** But yeah, so that was ridiculous. Even the legs couldn't be lifted by humans. We had to slide them on steel sheets on that one. Wow.

**James Bruton:** Is that... That was all water jet, or how did you actually construct something that big?

**James Bruton:** Well, Colin made most of the steel, so he's got a plasma cutter.

**James Bruton:** Mm-hmm. Okay.

**James Bruton:** So yeah, I did a lot of the CAD for that, for all the cosmetic panels, and then he plasma cut them and tried to bend them back into the shape of Hulkbuster. And yeah, we had a few discussions about the CAD and where joints should be, and then where the arms would be specifically, which ended up far too high and lots of other things. But Colin doesn't really do CAD, you see, so... Yeah, right. It's an interesting one.

**James Bruton:** Yeah, I mean, he regularly, at least on his channel, the way he shows it, it's like, hey, I want to build this thing, and then he just jumps on the lathe, and I'm like, oh my God. My heart starts beating faster, and I'm like, I guess he just knows what he's doing. That's great.

**James Bruton:** Yeah, he was a plumber. So Rick, who works for Colin sometimes, who's in some of the videos, Colin used to work for Rick. So Rick's a plumber, and Colin was his apprentice. And Colin started doing really well on YouTube, so now Rick comes and works for Colin sometimes. But yeah, so... But most of it is self-taught, I think, so I think he just picked up a welder and a lathe and whatever, and had a go.

**James Bruton:** Nice. That's great. That's great. I mean, and that's the thing. So people like you and Colin, and people like Dave, too, I think a lot of people look at all of you and say, oh, I could never do that, right? But I think that that's kind of the modern conundrum of just social media in general, of you see the end product, but you don't see the years and years and years and years of trial and error. And it's good that you guys are showing that stuff. I think that's really important. But there's more there than, like you said, you started before YouTube, Dave started before YouTube. And so it's important for people to remember that, that there are struggles there, and that's how you get better. And it's just kind of, you have to keep struggling, you know, and keep consistent like you do.

**James Bruton:** Yeah, I guess keep going is one of the things. And also, if you keep going and document it on YouTube, that's how you become a full-time YouTuber. Yeah. Because there's your content ready-made, right? But you've got the dedication to, I mean, it's like, how do you become a full-time YouTuber? And the answer is by doing it. Yes. Because if you can't publish that video every week, then you don't want to be a full-time YouTuber. So, you know, it's sort of self-fulfilling in a way. Yeah. All the better if you're going to learn some tricky skill and document it. And there's your content.

**James Bruton:** Yeah, right. Exactly. Exactly.

**Dave Jones:** One of the problems I have is that I make such a wide variety of content. It's hard for me, you know, whereas you're more narrow focused on robotics, you know, you build stuff every week. Whereas, you know, I don't, like, I'd love to be building stuff every week, but that's not my channel. You know, I've got to sort of like, you know, satisfy many different people with different types of content. So, yeah.

**James Bruton:** Well, they're just as picky by the looks of it. Oh, yeah. But maybe you should. I don't think anyone would object to you doing a build or a design. Oh, no.

**Dave Jones:** No, they wouldn't. It's, you know, so. But so many people subscribe for different reasons, you know. It's like, yeah.

**James Bruton:** Oh, yeah. I mean, 20% of my subscribers are still subscribing for a video that's from 2014 that's still doing 20,000 or 30,000 views a day. It's had 56 million views in total and it won't go away. Really? What video is that? It's how to build an Ironman suit in four years compressed into four minutes. Oh, right. Which is some of the first when I first sat down and started making serious YouTube videos on an old tape DV camcorder. It's like four by three.

**James Bruton:** Yeah. Yeah. Nice.

**James Bruton:** Some of the initial clips in that video are some of my first serious YouTube videos on that camera. So it's a bit of a legacy that that's, you know, still the most popular video every day. Well, not every day, but on average in the week.

**James Bruton:** Yeah. But think about how, I mean, you are now exposing all these people who thought they just wanted to get into costuming or they just think Ironman is cool, whatever. And now you're exposing them to robotics and other wonky stuff that you're doing. Well, if they watch, that's the thing. Well, sure. But you never know, right? I mean, that's the nice thing. You never know.

**Dave Jones:** Your top five ranked videos are the Ironman. Yeah, one of them, yeah. And then there's BB-8 and there's Ironman again. BB-8, Ironman, Ironman, Ironman. Like, you know. But that's just how it goes, though, too.

**James Bruton:** I mean, we had Scotty on here and all his stuff's about iPhone, right? I mean, it's just what people are exposed to. And then you get 1% that are like, oh, robots are cool. I'm going to keep going, you know?

**James Bruton:** Yeah. So, I mean, at some point I stopped doing costume stuff and when I built Robot X and I pretty much said I'm going to, you know, transform this into a robotics channel. I don't think the content's as popular as Ironman was. So I always thought if I needed to, like, right, I've really got to, you know, do millions more views for some reason, then I'll do another Ironman suit but using, like, CNC and make it all out of metal and 3D prints and make the most detailed Ironman suit in the world. Right. There's no coming back from that, really. No. And, you know, what do you do? Can I, I mean, I guess Robert Downey Jr. is doing all right out of it, but can I really, you know, be dressing up as Ironman until I'm 65 and I'm retired, you know?

**James Bruton:** You basically would have to, like, be the guy on the street in Vegas who's, like, signing out and taking pictures for 10 bucks a pop, you know? That's, like, your future at that point.

**Dave Jones:** Do you have any insight into what the actual Ironman suit on the movie is? Like, is it that detailed? Like, is it, you know, how detailed is it?

**James Bruton:** I think it's most detailed, isn't it?

**James Bruton:** Is it?

**James Bruton:** I think there's some shots from some of the Ironman movies where they've just got motion capture markers on them and they've got just, like, a bit of a helmet and a bit of the body.

**Dave Jones:** Oh, really? I thought there was, like, at least there was some real suit.

**James Bruton:** There might be, but there possibly is. There were a lot of models and stuff, too. I don't think it functions. Yeah, I don't think it functions.

**Dave Jones:** No, I don't think it functions, but, like, you know, is it made out of metal? Is it, like, I'd just love to know the details.

**James Bruton:** I think there was something that was sort of, like, foam and they spent ages trying to get a gloss coating on it. Right. Because if you think about the moves he has to do, like, all of these cosplays are ridiculous to move in. And, you know, you can see, like, bits of it must just, like, mesh into each other. Yeah. So, like, around the legs and the hips and everything's got to be CGI because you just couldn't crouch down and punch to the ground. It's impossible.

**Dave Jones:** Yeah.

**James Bruton:** You know, even Stormtrooper costumes, you can't sit down in them. Right. You can't walk up steps without, because you can't bring your leg up high enough, you know. So, yeah, it's a nightmare.

**James Bruton:** And so you were focusing on the costume stuff, like, the replica prop type stuff and costumes at one point?

**James Bruton:** Well, that's where the channel started, really, was, yeah, building, was when I got popular, was building this Iron Man suit that took four years.

**James Bruton:** Uh-huh.

**James Bruton:** So there's a 50-part build series for that. Wow. Wow. As well as the four-minute video that's all of the best bits. All right.

**James Bruton:** Yep.

**James Bruton:** And then building the Hulkbuster suit as well. That was 50 episodes in two years.

**James Bruton:** Yeah. 50. I've seen 58 years. Holy crap. Yeah, that's amazing. Yeah.

**James Bruton:** But then I was doing probably double the view count that I am now in a month.

**James Bruton:** Yeah, it changes things, I guess. But how do you feel about it? I mean, like, you're probably doing more interesting things, I'm guessing.

**James Bruton:** I'm more interested in them.

**James Bruton:** Yeah.

**James Bruton:** But I don't know. I guess a niche audience is. Yeah. Patreon funding's definitely gone up since I've been doing Open Dog. That's good. That's good. Excellent. Because I guess people who watch that are probably slightly more technical, slightly more mature, probably people who are older with jobs who've got money and not just kids who like Ironman suits. Right.

**James Bruton:** Right. Yeah.

**Dave Jones:** You kind of have to decide what, you know, what's more important, you know. Are you going to go after the easy views or are you going to, you know, go after something like the niche audience that you're more satisfied to make and stuff like that? Because the more niche you go, the smaller audience you're going to get. There's no doubt about it. And it may not be viable. Like if you go so niche that it's just not financially viable to do it. So what do you do?

**James Bruton:** It's called a job, I think. When you have an audience of one, it's like, oh yeah, I guess that's my boss then.

**James Bruton:** Yeah. Well, if they pay you. But yeah, I mean, Patreon is a massive game changer in that respect. Yeah. Because effectively, there's much more money coming from Patreon than YouTube. Yeah. And much more money than there was. But I've got less views. Right. Than I had. So that's, it's interesting that actually that's become sustainable by doing something more niche and having less views, but earning more money.

**James Bruton:** Hmm. Is it like an ego thing or what? At that point, like it hurts to have less views, but the money's better. So who cares?

**James Bruton:** Well, I don't know. Does that mean the content's better? I don't know. Is it just the algorithm doesn't value it?

**Dave Jones:** Yeah. But well, there's, you know.

**James Bruton:** I mean, it must be better content than me painting foam, right? And sticking it on a giant Hulkbuster. If I'm doing a kinematic model and showing everyone how to use their GCSE maths. But it doesn't get as many views. Yeah.

**Dave Jones:** But any YouTuber who claims that they don't care about the views is lying. You know, like it matters. Your reason you do it is because you want people to see your content. You know, I mean, that's where the enjoyment comes for a YouTuber and knowing X number of people have seen your stuff and like it. You know, I mean, that's, you know, it's just the nature of the business.

**James Bruton:** Yeah, I guess so. I don't know what the solution is. I mean, I guess it's doing the detailed Iron Man suit projects or going and doing something that's for every game and every movie that comes out doing a technical build. There's that thing in real life, but that's...

**Dave Jones:** Well, the ultimate answer is you've got to do what you enjoy doing. And if you can make a living on YouTube from it, then great. But if not, you know, like some people's goal is just to be a YouTuber, you know, and so they'll chase anything to, you know, make that happen. You know, whereas like...

**James Bruton:** Yeah, I mean, it just becomes another job.

**Dave Jones:** Yeah, exactly. But I don't look at the stats. Like, I haven't looked at the stats for years. I don't follow the stats and try and optimize stuff and things like that for, you know, views and things like that. I kind of, you know, might go, oh, yeah, a thumbnail matters. Okay, I'll spend five minutes making a thumbnail, you know. But, yeah, like... But some people treat it as a, you know, the only end goal is to get views, so...

**James Bruton:** Yeah, I guess like if the views make you happy, that's part of it. Yep. But, yeah, in terms of optimization, I've actually... I'm working with a management company, an actual YouTube talent management company, who go through when I put a video up and go and put new tags in and re-adjust the description and make sure my Teespring link's there and my Patreon link's there. And sometimes they say, that thumbnail's not very good. Should we make you a new one?

**Dave Jones:** Oh, really? So you're with a multi-channel network, are you? Some sort of MCM? No, it's not a multi-channel network.

**James Bruton:** I've been with multi-channel networks for years who do nothing, as you know. I ended up with BBTV and I negotiated to pay them nothing. And they still, of course, did nothing. So I left and they were like, okay, then. I mean, in fact, they paid me one year like $4,000. I think they paid me a signing bonus to start with. Right. And then it would be with only 10% fee from the ad revenue. Then we dropped it to nothing and I just left. So no, it's an actual, it's a UK company. Right. So basically it's a company called Ziggurat XYZ. It's also the slow-mo guy's manager.

**Dave Jones:** Oh, right. Okay.

**James Bruton:** So they, as well as doing that sort of thing, they can, they're basically talent management. So they will arrange stuff like sponsorships with brands. So I got my garden shed for free and some tools and my welder, which were all arranged through them. So they actually went out to brands and said, do you want to sponsor this YouTuber? Okay. And they also do production stuff. So my Aliens Animal video that went out the other couple of weeks ago and the filming with Ivan Miranda in Spain, my TCT vlog. They came along to hold the camera and do the stuff and they can do the edit as well if you want. Although they didn't in that case. Yeah. So it's basically like properly, if you think like a band having a manager, it's the same sort of thing. Got it. But also contracts with big brands and stuff like that and all the legal stuff.

**Dave Jones:** I assume that your content, because we mentioned before, like sort of, you know, edit as you go. That means you're pretty much, you would never be able to get an editor, so to speak.

**James Bruton:** No, I mean, it's just. The person editing at that company, in fact, had to edit a video for some other vaguely technical maker person. And they were like, I just, you know, I'm not sure how to put this together because I don't know whether this thing they're saying matches the thing they're doing. That's it. And sometimes I don't even say the right thing and I don't realize until I come to edit it. Until you edit it. And I've said like left instead of right or something else more technical. Yeah. And, you know, and then I'm like, oh, I'd have to go and do that piece again. They would just have no idea. No one could do it, I don't think.

**Dave Jones:** Yeah.

**James Bruton:** But yeah, I mean, if it's something more simple, like it was just me going around interviewing people, it could be done. Got it. So, you know, there are times if I didn't have time to do the edit, I could get someone else to do it on an ad hoc basis.

**James Bruton:** Well, speaking of editing, I mean, what are some of the other videos you think people should definitely check out for content or for, you know, learning? Or what haven't we talked about yet that we should definitely make sure our audience knows about?

**James Bruton:** In my channel? Yeah. Yeah.

**James Bruton:** I mean, I've watched a lot of Dave's videos. And so, yeah, I mean, I know those. But, yeah.

**James Bruton:** Okay. So, I guess the other projects that I, can I say I was proud of them? Yes, please. Totally. Okay. So, like the BB-8 builds.

**Dave Jones:** Yeah.

**James Bruton:** So, the real BB-8, which goes around on the red carpet and stuff. Yeah. In fact, a friend of mine built that, Matt Denson, who works at Pinewood. He's working on Star Wars Episode IX right now. And he built that with Josh Lee, who's the mechanical guy. So, Matt's an animatronics guy. Wow. So, obviously, he was on a sworn secrecy about how that worked and so on. And they revealed me. He told you. He didn't tell me. No, they revealed it at Star Wars Celebration a few years ago where they actually had a big panel and they showed what was inside it. But I have mine actually running at that show with the R2DC Builders Club.

**James Bruton:** Oh, cool.

**James Bruton:** Okay. So, I basically solved it, you know, before that.

**James Bruton:** Oh, and it was similar, you're saying? So, you're proud that it was similar to the actual way they did it?

**James Bruton:** Basically, they made one that worked, yeah. Yeah. That drove around by itself. Nice. And it's dynamically stable. So, it's got an inertial measurement unit in it. And it's using PID controllers to stay stable. And it's got, you know, it can spin on the spot. And it's got three axis and its head moves in three axis. Nice. So, that's another 12-part series, which means it's at 12 weeks. It was the third version. And then, of course, I did the thing with Colin and eBay and Star Wars where he built the TIE Fighter and I built BB-9E, which was sort of like the more robust version that had to drive on grass. But that was six weeks to build that one.

**James Bruton:** What changed about that? What was the heart of that?

**James Bruton:** Well, we had a budget. So, I had basically better motors and stuff that I could buy. And it had aluminum extrusion inside and some steel brackets and bits of metal. And generally, what else? Oh, yeah. So, all of it was 3D printed instead of doing like vacuum forming and stuff to make the ball. Uh-huh. Yeah. And more magnets holding the head on, which cost quite a lot of money. So, yeah, that's it really.

**James Bruton:** And so, the head, I always wondered about that. So, the head actually is like free-floating on the edge of the ball. Is that right?

**James Bruton:** It's on caster wheels. Uh-huh. It's obviously held between the surface of the ball as magnets. Well, some magnets in the head and some inside on the head control arm inside BB-8.

**James Bruton:** Okay.

**James Bruton:** But obviously, what moves that head control arm around is what's important.

**James Bruton:** Right. Okay.

**James Bruton:** Which is controlled by the controller and also by gravity on an inertial measurement unit to keep the head on top or at whichever angle, depending on what's happening to the drive system inside. Because, of course, as the drive system inside climbs up the ball, the head would go back and it wouldn't roll anywhere. So, the head has to come forwards as well to stay in the same position. Yep.

**Dave Jones:** How do the magnets work when it's like completely rolling around the place?

**James Bruton:** Magnets, how do they work, man?

**Dave Jones:** No, but you know what I mean. Like, the ball at the bottom is rolling. Well, I had a chance. Right?

**James Bruton:** Yeah.

**Dave Jones:** So, there's magnets in the head keeping it to the ball. How do the magnets in the – oh, sorry. I haven't watched the video. I haven't seen how BB-8 works. I don't know.

**James Bruton:** Yeah. So, well, inside the ball is a thing that's effectively on a fixed axis. So, in one of my BB-8s, it was basically a hubless wheel that ran around a channel. So, it only runs in one direction. Right. In BB-9e, it was on an axle. So, it only runs in one direction. And that drives it forwards. And then attached to that is a cradle that leans sideways, that leans it sideways. So, it's like leaning on a bicycle to steer.

**Dave Jones:** Mm-hmm.

**James Bruton:** And mounted on that is a flywheel that spins around so that it can spin on the spot. But mounted on all of that with the same center of rotation, the center of the main sphere, the main body of it, is a hedge control arm that can also move in three axis. So, it can move left, right, forward, back, and rotate. And that's got the other half of the magnets on it. Right.

**Dave Jones:** Right. Okay.

**James Bruton:** And all of that is dynamically stable. So, if you push it, it rolls in that direction. or if you tilt it sideways, its mass compensates to bring it back upright.

**James Bruton:** You know what's crazy to me is thinking about all this is like, I mean, if there really was a universe where there was a BB-8, that's probably how they would have built it.

**James Bruton:** It's the most impractical robot you can possibly imagine. So BB-9E was all glossed up. It had to be like mirror finish. Oh, yeah, okay. And then we drove it in a muddy field.

**James Bruton:** Oh, my God.

**James Bruton:** So I was there with like window lean, which is like window cleaner stuff that doesn't leave streaks.

**James Bruton:** Yeah, like Windex.

**James Bruton:** And loads of kitchen towel to like clean it between every take.

**James Bruton:** Oh, my God.

**James Bruton:** But if you think about a robot, obviously like dirt gets up into the head rollers and all over the magnets and all over it. So if you just imagine a robot that rolls all over the ground. Yeah.

**James Bruton:** If the open dog left something on the floor for its owner and then the BB-8 rolled through it, you know what I'm saying?

**James Bruton:** Exactly. But then obviously it's got these little arms that pop out. BB-8's got these little arms that pop out of its panels. Yeah. If you imagine trying to solve the, like, I need this tool and I need to align it with this control panel on the wall, how on earth do you roll BB-8 up and then get the right arm out in exactly the right place? You'd have to do so many like three-point turns to roll it round and round and round to get the right panel to face out, just in the right place so it can reach.

**James Bruton:** So now we know why BB-8 is impractical.

**James Bruton:** Okay. Yeah, it's a terrible idea.

**Dave Jones:** Okay, I'm actually watching the video now of the real BB-8, the internal mechanism without the ball, and I can see how it's going now.

**James Bruton:** Yep. Is that the Star Wars Celebration panel video?

**Dave Jones:** Yes, it's howbb8works.com.

**James Bruton:** Oh, that might be all right. That one did have loads of fictional ideas on anyway.

**Dave Jones:** No, no, yeah, but it's got a real video apparently from the Star Wars Celebration 2016.

**James Bruton:** Oh, that's fine then. Yeah, cool.

**Dave Jones:** So, you know.

**James Bruton:** Because they put that website up before they knew how it worked.

**Dave Jones:** Oh, right, okay.

**James Bruton:** And it had loads of CAD on and it was like, yeah, it can't possibly work like that.

**Dave Jones:** Right. But, yeah, well, this looks like real video to me. Yeah, it will.

**James Bruton:** But if it's from Star Wars Celebrate, that's probably Matt and Josh talking about it.

**Dave Jones:** Right. It's just like an animated GIF of it going forward. Just a short three-second cycling clip of...

**James Bruton:** Yeah. Yeah. Yeah, so the important thing is everything has the centre of rotation being the centre of the sphere, which is an interesting mechanical issue.

**Dave Jones:** Yeah.

**James Bruton:** Yeah. Wow. That's super cool. So you can't tell us about your new project, but there is a big one coming, I think.

**James Bruton:** A big secret project, which will launch on Tuesday by the time this podcast goes out.

**James Bruton:** Right, I think it will be a day after this podcast. If you're listening to this and it's Tuesday the... What is that? The 20th?

**James Bruton:** It's for a big Christmas movie. It's not Mary Poppins. Okay.

**James Bruton:** Got it. Got it. That's a good teaser text right there. Mm-hmm. Okay. Cool. Well, we'll look forward to that. Where can people find out about you and see your stuff and hopefully sponsor you on Patreon?

**James Bruton:** They can look at my YouTube channel, which is actually my own name, James Bruton.

**James Bruton:** Yep.

**James Bruton:** Or they can have a look at patreon.com slash xrobots.

**James Bruton:** Great. Are you on the socials as well, Twitter or anything?

**James Bruton:** Yes, mostly xrobotsuk on Instagram and Twitter.

**James Bruton:** Great. Well, James, thanks so much for telling us about all these robots things. I mean, like, it still feels like a long path to getting to where you are for sure, but I really like the kind of the iterative nature and just the building it from the ground up and learning about it along the way. That's really useful, and I think from our audience's perspective that that'll inspire people to go and give it a shot.

**James Bruton:** Yeah, I think I've got a few more iterations to go myself yet, though.

**James Bruton:** That's good. I mean, that's great, right? I mean, it's not something that you finished. It's something that you're working on, and that's the kind of thing we like to hear about here.

**Dave Jones:** Well, it's probably a never-ending thing. I mean, you know, there's always something new you can work on.

**James Bruton:** Absolutely, yeah. That's the best part of engineering, yeah.

**Dave Jones:** Terrific. Well, keep it up, James. I'm very impressed with the amount of throughput in video and project builds. It's just, yeah, yeah. I can appreciate how much, well, you know, our audience, I'm sure, can appreciate the amount of work that goes into, you know, making all this other stuff and let alone, you know, documenting the process with YouTube videos and everything else. Yeah, all right. Cool. Thanks, mate. Cool. Thanks a lot. Thanks a lot.
