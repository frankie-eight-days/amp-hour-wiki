---
episode: 723
title: BeagleBoard's Back with Jason Kridner
url: https://theamphour.com/723-beagleboards-back-with-jason-kridner/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released May 7th, 2026. Episode 723. Beagle Boards Back with Jason Kreitner.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell, Contextual Electronics.

**Jason Kridner:** And I'm Jason Kridner of BeagleBoard.org.

**Chris Gammell:** Welcome back, Jason. How you been?

**Jason Kridner:** Been well. Good to talk to you again.

**Chris Gammell:** Yeah, we were just looking at 2018 was the last time you were here, you and Robert. You were one of our earliest guests as well. I think I remember talking to you from a hotel room, I think, or something like that. But it was with me and Jeff Kaiser. So like a real long time ago. And that was, I think, shortly after we met. So yeah, long time past guest of the show. But you've continued to make lots of things. And I'm excited to talk about them.

**Jason Kridner:** Cool. Yeah, lots of things.

**Chris Gammell:** So what are you most excited about in 2026? The age of AI, the age of cheap hardware, more powerful hardware. What are the Beagles up to?

**Jason Kridner:** Most excited in the age of AI. So we finally got over my pride a little bit and made a Raspberry Pi form factor board. It's like I kind of regretted not doing it before. Because it makes projects super, super easy for me. So because we did the Beagle Y AI. It's in a Raspberry Pi form factor. And it's got a neural net accelerator in it. So it's kind of like if you had like a Pi 3 plus a Coral kind of blended into one. But with PCI Express and USB 3 and some other upgrades. But like it's just been really fun to make stuff out of. So I'd maybe buy off-the-shelf robotic arms that have been made for a Pi and put them in there. The LCD screens. You know, all those sort of things. All the different kit that comes for Pi just made it real easy. So I've been liking that.

**Chris Gammell:** Tapping the ecosystem, yeah.

**Jason Kridner:** Tapping the ecosystem.

**Chris Gammell:** And so is that the one you're sticking with? That form factor you're sticking with? Or you're still doing novel?

**Jason Kridner:** Well, you know, we've gone back to the Pocket Beagle form factor. So I really love that. It's, you know, smaller. So the Beagle Bone and the Pocket Beagle are in like Altoids Mint 10 size form factors, right? Because they're supposed to be 21st century survival kits, right? So like the old meme of making survival kits out of Mint 10s. So yeah, we've gone back and did another Pocket Beagle. Pocket Beagle 2. And now we've also done a Pocket Beagle 2 industrial that includes a bunch of flash on it. 64 gigabytes of flash and industrial temperature rating stuff. And yeah, so we're definitely continuing to do our own form factors in addition to kind of working within the Pi form factor ecosystem. And we've also launched into microcontrollers. You were actually at the spearhead of us getting started with microcontrollers. But the Beagle Connect line lives. And we're actually trying to do right now a $1 board.

**Chris Gammell:** Oh, I have one. I meant to tell you. Oh, did you get one? Robert may have slipped me one at Embedded World. Yeah, excellent.

**Chris Gammell:** Zepto? Is that the name of it? Yeah,

**Jason Kridner:** Beagle Connect Zepto. So it's a small SI unit. You know, it's still bigger than a Yocto, but you know, it's a lot smaller than a Nano.

**Chris Gammell:** Yeah, right. And that one was the $1 price point is just to try and just drive volume up, right? And you can still do quite a bit there, yeah?

**Jason Kridner:** I mean, it's all about access, right? So I'm trying to do more things with, you know, K-12 students, right? Rather than, you know, most of Beagle has kind of lived at the university and professional level. And, you know, we're really trying to make it more accessible in more areas as well as for younger people. So Beagle Connect Zepto is kind of, you know, right at that. So the $1 price point means that, you know, because, well, how many of these do I need for a classroom? And it's like, well, you know, how many kids you got? Multiply it by five, right? You know, everybody, every program should have its own little board, right? So you can just do it that way. And then, you know, making things for them to interact with, right? So I've got really upset with, I mean, I love, you know, Dean Kamen and everything that's happened out of FIRST Robotics and, you know, the US FIRST competitions.

**Chris Gammell:** Yeah, like Lego League, stuff like that, right? There's driving a lot of interest.

**Jason Kridner:** Yeah, I love it. I love it all. But like what I always have seen in mentoring those groups is that there's usually one nerd in the corner that's writing all the program.

**Chris Gammell:** And then there's the one, the management kid who's got the stick and he goes over and pokes that kid and he says, go faster.

**Jason Kridner:** Yeah, yeah, exactly. And he has no idea how to help him go any faster.

**Chris Gammell:** Have you thought about implementing an AI program?

**Jason Kridner:** So I don't necessarily love that. I mean, it's good, right? But, you know, once that kid gets to the point where the remote control actually, you know, is flipping relays and driving, you know, the motors, right? And they have that ability to do the actuation, then they forget about that kid in the corner. And he's like, you go work on the autonomous section. And you're like, we're just going to go over here and, you know, drive our RC car.

**Chris Gammell:** Yeah. Well, I mean, you've been a, you know, what, assembly level up for a long time, right? I mean, this sounds like you're also like interested in fostering the low level control type persona as well.

**Jason Kridner:** Yeah. Back when I was a kid, I programmed in basic. And so, you know, sat down and made it print my name on the screen. And it was like magic, right? It was just magic, right?

**Chris Gammell:** It still is.

**Jason Kridner:** And then, you know, you got Arduino with the blinky LED and everybody does blinky LED. But, like, I don't know that that's really what empowers, you know, kids anymore, right? And, you know, if you make it too easy, it's not, it's kind of missing the point, right? It's actually got to be just hard enough that you actually have to understand something and, you know, then can, you know, do something new and unique in your own with that knowledge. So, I'm obsessed with what's the next blink LED. And a lot of people are. So, I'm just, I'm in the club.

**Chris Gammell:** And so, what is, I'm just looking at the little thing that's in here, the Zepto. Should people listening, should they go pick one up? Are they available yet? Where's the, what's the latest on that?

**Jason Kridner:** Not yet. Not yet. This is one of those cases. We don't really rely on, on, on Kickstarters with BeagleBoard, right? We just, you know, get things into distribution. But, you know, we're not going to, unless we build 100,000 of these, it's not going to be a buck, right? So, so I've got to, I've got to try to drum up a little bit of awareness first, you know, get some, some, some fun applications, like things that you can actually do with it. We're kind of looking at, you know, different development environments, right? MicroBlocks being like one of the, the big ones that we're trying to enable, but you know, other things that we can do off of Zephyr. So we're running Zephyr on it. You've seen mainline patches for, for Zephyr, for BeagleConnect Zepdo.

**Chris Gammell:** So I also saw an announcement that you were one of the newest members. So that, congratulations on that. I'd say welcome to the club, but I'm not really like, it's not me. Just, just a, a friendly observer who hangs out at somebody.

**Jason Kridner:** So BeagleBoard, BeagleBoard.org foundation.

**Chris Gammell:** I should also say, I should also say, this is because of Jason and because of Chris Freed, who was working on BeagleConnect as well. Like that's the only, that's the reason I started looking at it in the first place. Anyways.

**Jason Kridner:** Is that what got you into Zephyr?

**Chris Gammell:** I think that, and then like, I had also asked on people with like an old contextual electronics board, they said like, oh, it works great on the NRF 52840. So you should check that out too. I think it was like concurrent and I kept, you know, hearing about it everywhere. And, but BeagleBoard is definitely why I put click headers on everything too. Oh yeah.

**Jason Kridner:** Well, I mean, and you noticed the Zepdo. Have you noticed what the, what the header? So the, the kind of the fun thing about that is we did friction fit for the, the Microbus connectors. Right. So I just, I mean, I love feather wing, you know, with the Arduino nano form factor, all that stuff is nice. But I think that the Microbus standard is just really clean. And, you know, the one vendor makes more out on boards than the rest of the open source hardware community has managed to put together.

**Chris Gammell:** Yeah. And it's not like it's like locked down either. So anyone else could go build their own click header. It's kind of got the basics of what, maybe we should explain what it is too, for people that don't know. What is a click?

**Jason Kridner:** Well, let's, let's, let's get the terminology right here. Cause the click is a, that's a brand from Microelectronica, right? So that's their brand of Microbus add-on boards. So to be, you know, somewhat separate from, from Microbus, which is the, the freely licensable standard that they created. Right. So Microbus is the standard. Click is the, the product line. So you can't say you make a click, you can say you make a Microbus add-on board or something like that. And then you get a free license to the logo. And it kind of has all this stuff that we would expect, all the embedded serial interfaces, embedded interfaces that you'd expect in very normalized spots. Right. So there's an analog input pin for ADCs, right? There's a PWM for pulse width modulation output. There's, you know, I squared C serial. There's, there's a UART serial. There's a SPI, you know, serial peripheral interface. There's interrupt, a spot for the interrupt. There's a spot for reset. There's ground and there's a five volts and three volts. And did I hit all of the, did I hit, got them all the pins?

**Chris Gammell:** Yeah, you got it all. Yeah. And, and there's the three different sizes as well. I think that's another important thing because then there's a standard size profile.

**Jason Kridner:** Yeah. Yeah. So you've got the small, medium and large, right? Sort of form factors, but every, like it kind of pins off this one inch by one inch kind of base where you put the connector and then kind of grow off of that. Right. Small, medium or large off to one side. Yeah. So we've been using that on a bunch of the, you know, the Beagle designs, right? It was on the Beagle Connect Freedom, which you got to work on with us a little bit, which I really appreciate. The also Beagle Play, which talks to Beagle Connect Freedom. So they both have that same long range, low power, wireless connectivity between them. So they both have the Microbus on them. The Pocket Beagle 2 was initially designed to support Microbus. If you look at the, sorry, the original Pocket Beagle and then the Pocket Beagle 2, but we decided to, you know, back in the day we did it, the folks that had some Microbus. Microbus had shipped the little pin headers with you. They didn't actually have them soldered on. Now they have them soldered on. So we ended up putting them on the opposite side, right? So you can't actually plug a click board into the Pocket Beagle 2. So then we finally put the headers on them. I think that was kind of the biggest stumbling block for people starting out with the original Pocket Beagle. And then we ran out of SIPs. So yeah, memory crunch number one.

**Chris Gammell:** Right, right, right. That was a 22, 23 era of shortages or?

**Jason Kridner:** Yeah, the 2020, kind of in that 2020, 2021, when, you know, substrates were short and like just everything, right? The whole supply chain kind of got eaten up and the prices, the SIPs went out of control. And now instead of kind of bringing back Pocket Beagle, we just have Pocket Beagle 2.

**Chris Gammell:** Makes sense. Let's talk a little bit about the, you know, application areas. We've already mentioned like so many different spaces from tiny, tiny low-cost microcontrollers all the way up to these, you know, AI compute engines. So like where are you seeing kind of a lot of them finding purchases as well? So like, you know, we mentioned motor driving and education market, but also maybe some AI processing. So like if you had to rank number of boards and users into application buckets, are they cameras? Are they automotive? Are they, you know, like where do you find them kind of playing in different spaces?

**Jason Kridner:** In particular for what people are using Beagles for?

**Chris Gammell:** Yes, that's right. Yep.

**Jason Kridner:** Because I would think that's kind of like mostly like business automation stuff, I think is what I see the most, right? Sort of anything that needs to be automated in a, like it could be on a factory floor. It could be in an office building or doing different data collection. Less of sort of, you know, internet of toilets sort of thing, you know, there's... That's out there.

**Chris Gammell:** People need to look at their poop, Jason.

**Jason Kridner:** There's hardly, you know, anything that you can't sort of like, you know, make smart, right? You know? Right, right, right.

**Chris Gammell:** So like the Beagle Y AI, right? So like that one, is it running headless or is it running with screens normally? Is it running with cameras or without cameras?

**Jason Kridner:** I think mostly it's going to run headless, although absolutely people are running UI screens. Like I think you'll see some usage in like places on a factory floor where you do have animation. There's a reason there's an OLDI connector on there, right? So like who has OLDI, but if you're making kind of these, you know, resistive touchscreen panels that, you know, are like more heavy duty. Acid free or acid resistant. So it has some, you know, some real usage, right? Most of the customers buy like 100 boards a year. So it's like, it's hard to know what everybody's doing. So you never really hear from them until, you know, it's like they're, you know, concerned about something, you know.

**Chris Gammell:** You don't hear about the good use cases where everything just worked.

**Jason Kridner:** Yeah. It's just like, hey, no problem here. So, you know, every once in a while, some people actually show up on the forums and show off something, but that's rare.

**Chris Gammell:** That's nice. Right.

**Jason Kridner:** Usually.

**Chris Gammell:** Zephyr, I know, has the same problem where they're like, it's out there. We know it's out there. Yeah. Yeah.

**Jason Kridner:** Exactly.

**Chris Gammell:** Who knows? And it's probably the most interesting applications are not necessarily the ones where they want to talk about it, right? It's like, we don't want to talk about everything that's inside of this. So it's like, okay. Yeah.

**Jason Kridner:** Yeah. I mean, like the original BeagleBone, you know, it's been out long enough. I've got a little bit more idea of some of the things that people are using it for, but it's everything from like satellite networks to like used in, I think Fermilab actually standardized it for data acquisition. Data acquisition is real common. We've got an FPGA based board now. Oh, I didn't know that. It's actually part of the SpaceGrade Linux, as well as the civil infrastructure project. So both are too cool.

**Chris Gammell:** So like detecting bridges or like big stress and strain on bridges sort of thing?

**Jason Kridner:** You're already no more, you know, I don't know. I wish I did. Right. But the civil infrastructure project, you know, from my perspective, right, is people worried about having, you know, long term support. And, you know, is it because they want to make sure the bridge doesn't fall? Well, I'm not sure. Hopefully.

**Chris Gammell:** Yeah. As a user of bridges.

**Jason Kridner:** I like bridges to stay. Yeah.

**Chris Gammell:** Yeah. They're doing great. Keep on keeping up there, folks.

**Jason Kridner:** Yeah. That's the Beagle5Fire FPGA base board. Did my video stream done?

**Chris Gammell:** Is that PolarFire?

**Jason Kridner:** Yeah. It's PolarFire SOC. Exactly.

**Chris Gammell:** The Makership one? Yeah.

**Jason Kridner:** You have to make sure to say the SOC because it includes the RISC-V cores in it. Okay. Not just the FPGA fabric, which serves mostly to confuse FPGA developers because they're like, well, like, where's JTAG connection? You know, and it's there, but, you know, it's like, no, you just boot it up and you make a Debian. Like you go to our continuous integration servers, you push your fork to the gateway and you download the .deb. And you install the .deb and there's your gateway, right? Yeah.

**Speaker ?:** Yeah.

**Jason Kridner:** You don't, what's JTAG? You don't need Verilog. You know, you do write your Verilog, right? But you write it on the cloud, right? You write your Verilog in the cloud server and have it do the, or you could do it locally, but you push it. So the big problem we're trying to avoid is people having to install the microchip tools just to get started. Yeah. Right.

**Chris Gammell:** It's, you know. Developer tooling issues. I know this one well.

**Jason Kridner:** And it's, it's nuts, right? So there should be a Docker container for that. And there is.

**Chris Gammell:** Yeah. That's good. That's good. And that can also be local as well. They can like download the Docker container. Yeah, absolutely. Yeah. Yeah. It's interesting how Embedded is still catching up in that way. It's like, well, no, no, no. You're going to like install this massive Windows executable, right? To like have the, you know, 20 gigabyte tool chain. So, yeah. Yeah. You've been ahead of the curve a little while, Jason.

**Jason Kridner:** Just, just, you know, I mean, you probably know this. People aren't as impatient as I am, I guess, enough. And they should expect a little bit more from their tools. SDKs. I'm not going to wait for SDK download. Sorry.

**Chris Gammell:** Yeah.

**Jason Kridner:** Everything I do is in 10 minute spurts. So if it can't do something productive in 10 minutes, it doesn't really happen.

**Chris Gammell:** That's interesting. Interesting frame on things. Yeah. Yeah. Just because of context switching, you mean?

**Jason Kridner:** Yeah. I just, I have too many interests. That's a personal fault. It's not that I don't love to actually sit down and, you know, dive deep in coding, you or other types of, you know, activities in general. I do, but I don't necessarily do a great job of filtering out the distractions. So, so I, I spent a lot of plates. Yeah.

**Chris Gammell:** I feel that. Yep. Yep. Yep. So just to go back to the board, kind of just the targeting of different spaces. So we talked about Beagle YAI, Beagle Play, that sort of thing. What about like the Beagle, the Pocket Beagle? Where, where is that used often? Is that kind of just like IoT sensing type stuff or something else?

**Jason Kridner:** Yeah. I mean, it's anytime you kind of need to add like a, a, a Linux system to something and you want to kind of, is it the, the headers are pretty flexible for what you want to integrate it to. So I try to do a little bit of dog fooding. So I've used it as an IoT gateway, right? I mean, just, you know, connect up a cellular modem and then connect up, you know, other data sensors, right? So, so air quality monitoring was, I was doing for a while.

**Chris Gammell:** Good. Well, cause it is kind of interesting too. Like the, the fact that, so like that as a, as a use case could be, you know, that that's like squarely in that like nether region of like, it could be embedded. It could be Linux. It could, it could be full-blown Linux. It could be embedded Linux. It could be, you know, it could be Zephyr. It could be bare metal, right? Like all the way up and down that like certain applications kind of fit that space. So that's really interesting, especially now that, you know, covers a lot of them in, in, in terms of like process nodes and, and capabilities and power envelopes really.

**Jason Kridner:** Yeah. I mean, I, for me having Linux remote, right. It just like having a full shell, I can kind of get in and, you know, and actually just run a Docker container on the, the, the board. You know, I actually kind of learned that trick from the cheeseburger robot guys.

**Chris Gammell:** Like I can't has cheeseburger those guys or something else.

**Jason Kridner:** They were in make magazine once, but they were the world's first cheeseburger robot. I mean, I'm the creator, I think was the name of the, the company. And they had, they had like 14 or 18, you know, BeagleBone black based robots kind of put together into this conveyor belt system to build cheeseburgers.

**Chris Gammell:** Oh, so it's like cheese. Oh, it's not a, it's not, it's not a cheeseburger.

**Jason Kridner:** It's not a robot that looks like a cheeseburger. It looks more like a Rube Goldberg. But it makes, it makes cheeseburgers. It's cheeseburgers. Okay. Got it. It grinds the meats. It has like 27 different seasonings that you could choose. You could choose the, the level of fat in your, your grind of meat. You can, it slices the tomatoes, slices the lettuce.

**Chris Gammell:** Got it. Cause even as, as I searched for this term frantically to try and find this, I also found something that looks like a knockoff transformer. That's a burger, but it turns into like a, like a robot, which is fun in its own right. I mean, honestly.

**Jason Kridner:** You know, that would be, somebody could make that out of a, of a, of a Beagle. That sounds cool.

**Chris Gammell:** I mean, it's, it already exists and it's, it's here. The robots are here. They're just not evenly distributed.

**Jason Kridner:** Yeah. I'm looking, I have these race cars, like I did donkey car stuff with it. So that was another one is I was able to take like a pie racer and do that with a Beagle YAI. So that was fun.

**Chris Gammell:** That's great. Yeah. Just plug right in. Yeah. Yeah.

**Jason Kridner:** But now you don't have to have the accelerator. I don't know. One of the great mysteries for me is like, why does anybody care if it's open hardware, if they're not actually going to make it? I don't know how to get people to, to, to really care about that. I mean, the ones that do do right. I think that's where you see a lot more like the Beagle stuff kind of going into professional things, right? Right. People doing, you know, you know, automation and companies, cause they, they kind of, they have that opportunity to kind of take control over the supply chain. They can get the details and stuff, but individuals for the most part don't seem to really care much about open hardware and makes me sad.

**Chris Gammell:** I mean, from like a long-term partnership with like the TI folks you work with as well, I can imagine they see a lot of benefit of it, like because it's getting designed in. Right. Yeah.

**Jason Kridner:** Yeah, for sure. And when we started this, when I was still at TI, right, I've been out of TI now for about five years. We started this before there was a term open hardware, really. I mean, it was just, you were just doing a, you were just releasing a reference design, right? It was just like, here's a, you know, it's a, it's a, it's a reference design, but you can't call it a reference design. Cause that means when somebody copies it exactly, they can sue you.

**Chris Gammell:** They're going to try more likely to sue you. Yeah. Yeah.

**Jason Kridner:** Well, people can sue you for anything. Right. But you know, yeah, yeah. The more, and so if you, if you, if you directly call it a reference design, it gives them some opportunity to say that, well, this design was validated for some purpose and you just have to tell them, no, it's not validated for any purpose at all whatsoever, but here's all the documentation and you can validate it for that purpose yourself.

**Chris Gammell:** I do think there's still benefit in it. Yeah. I, I, you know, I think the, the fervor around it has died down a little generally too. Right. I mean, like, you know, I think you and I hung out at the open hardware summit multiple years. It's not still out there. Don't get me wrong. It's still out there, but I don't, at least in my own, in my own.

**Jason Kridner:** I thought nobody wanted to come to the United States anymore. I thought that's all.

**Chris Gammell:** It's in Berlin, I believe this year. So it doesn't matter there. Yeah.

**Jason Kridner:** I thought it would still be a good event. Yeah. So I don't know.

**Chris Gammell:** Yeah. And I think, you know, there is still interest in it. I, I don't know if there's as much focus on it. Right. So.

**Jason Kridner:** Well, that's, I think it's silly. You know, it's so easy to make, you know, circuit board stuff, even if you don't want to spend time with a, you know, pick and place machine and a reflow oven. Right. Getting PCBs made. Right. From, from people like just shuttling things like Oshpark or whatnot, or, you know, using, you know, JLC, you know, circuit hub, right. To macro fab, you know, all these guys. Right. And there's, there's more of those popping up. It's just so easy to get something built. Right. Or seed fusion. I didn't mention that one. I don't know why not. KKAD kicks ass now. So it's like, it's really good. I mean, there's still some things that we still use Allegro for that I wish we could get away from. And we're trying, you know, we're trying to make sure if people ask for it, we'll do the stuff to get it out of Allegro, Indica can. I don't know. I'm not sure why. So why do you think they don't care? Do you, do you agree that it's generally not a care about?

**Chris Gammell:** No, no, no. I think what I was trying to say is, is in my own sphere of like media consumption, I hear about it less. Yeah. I think people still care. Like there's still people going to open hardware summit. There's still people marking their stuff, open hardware as they should. I still release open hardware. Like there it's all out there. It could be, it's just normalized, you know, like, you know, eventually people stopped watching the shuttle launches too. Right. Because it just was like, oh, look, another shuttle is going up. It's still amazing technology. It's still this enabling thing, but there was just less like novelty to it. So it could be that. But personally, I just, I hear about it less, but also I'm online less than I used to. So like, it also could be that.

**Jason Kridner:** When I think about the AI overlords taking over, I think, have you seen the movie, Mitchells versus the machines?

**Chris Gammell:** No, there have.

**Jason Kridner:** Oh, I can't make that reference. Oh, man.

**Chris Gammell:** You can. Someone in the listening audience will have heard it.

**Jason Kridner:** So there's, so yeah, the robots take over, but, you know, the, when, when everybody really finally panicked, because the fact that the robots had kind of taken over really wasn't that big of a deal until they turned off the wifi. Yeah. And then everybody panicked. Right. And, and, you know, the, that complicity, that, that sort of comfort with this stuff working that, you know, is supposed to just work. And when it doesn't, oh, unplug the router. It's like, yeah, I don't, don't, don't like, you know, I get on the stupid Comcast, right? You know, why is, why is my modem not working?

**Chris Gammell:** Comcast is a carrier, is a internet provider in the U.S. for people that aren't here, but they are much maligned and they very much deserve it.

**Jason Kridner:** Yeah, that's that, exactly. And, you know, you, you, you, you get a technician, right? And the answer is always, well, did you reboot it? And, and, you know, why does, why do you think that's like, okay to say to me? I mean, I, I get that.

**Chris Gammell:** How dare you, sir?

**Jason Kridner:** I get it. Right. I mean, from a practical standpoint, that's the, the, it fixes 80% plus of the calls that they get. Right. And they, they sit there and they wait, you know, half an hour for the stupid thing to reboot, because that's how bad the code is. It takes half an hour to boot. And, you know, if it wasn't for bugs, there's not a reason that you should run out of route tables. Right. And that's mostly what these things do. They just, they just run out of route table space and you have to reboot them all the time. So, so I have to set mine to reboot at midnight every night. Right. It's just because the, the, the software is so bad.

**Chris Gammell:** I'm just, I'm in my mind. There's like, you know, the Krizam YouTube channel, you follow those guys. Like there, there's like a bunch of like coding humor type things. Anyways, they're doing really good skits, but I just imagine like a customer support thing in, in Jason's, Jason's world is like, oh, sir, thanks for calling Comcast. Are you a Vim or an Emacs user? We need to know before we start this conversation. Cause we're going to be troubleshooting. Yeah.

**Jason Kridner:** Does anybody still use Emacs?

**Chris Gammell:** Oh yeah. All of it. Oh yeah. Oh boy. Oh boy. Jason shots fired. Shots fired.

**Jason Kridner:** That has spoken from a Vim user.

**Chris Gammell:** Yeah. Yeah.

**Jason Kridner:** Yeah. Yeah. Yeah. So I, I, you know, I agree that I'm not the every user and, um, but I am, I'm also just terrified of a future where when people's routers don't work and, you know, and, and they're relying on AI agents to fix it for them. Yeah. Cause they are now, right? That's not, and the AI agent is going to tell you to reboot it and, you know, and maybe, maybe we'll make some smarter agents that'll actually go in and fix the bugs. Maybe.

**Chris Gammell:** But, um, I, I do, I do find myself, you know, often, I, I, I'm kind of like left wandering, like in my younger days, I'm like, uh, I can't believe, I don't know how this works. And now in my older days, I'm like, I can't believe anything works. Uh, you know, just like, I'm like, there's so much technology layered up. And I, and I do think about, you know, like both, both of the, your Zepto kind of stuff, but really just Beagle generally, like your education focus and your, it's like, we need to at least inspire enough curiosity to, to get people to dive down the stack. Because if there's not people that are out there, you know, trying out, like, I think about like Julia, who was on the show a couple of episodes ago, she's like building open Silicon designs to go in these shuttle runs. It's like, if there's not people like her out there building this stuff, then there, you know, then who the heck does Nvidia hire to, to build their stuff? You know, like, you know, like it's, it's a, it's a feeder, it's a feeder cycle. And if there's not enough people that are interested in the low level stuff, then all the super fancy, high level stuff, like all the LLMs that are built on top of stacks and stacks and stacks of technology, it just, it's just going to stop working, you know, in some, in some, or we're just going to stagnate, which maybe is the worst thing.

**Jason Kridner:** And, and, and all these, like all this, you know, code that all these AI agents are making is, is great until it doesn't work. And then, you know, do you know why it doesn't work? And, and, and, and that's the, and that's the big question, right? I think that, you know, the, the, the folks that are, you know, helping build that the, a lot of the infrastructure and tooling for building silicon, you know, would probably know a little bit about like six sigma and Tamaguchi methods, right? And things that actually, you know, the idea that an electron can be, you know, halfway across the universe at any given time, how is it ever supposed to work? Right. Like there's enough statistics to actually help us get it there.

**Jason Kridner:** It is possible. Right. We experience it all the time. Right. How do we, do we learn those building blocks so that we can actually rebuild them up if we, if we needed to. So I'm hopeful.

**Chris Gammell:** Yeah. And certain depends on the day for me, but generally, you know, things are pushed in the right direction because of, you know, folks like you and the things you're building. So that, that definitely helps. I'd love to keep going on the list of, of boards as well, because, you know, you mentioned the, the Beagle Connect Freedom. This is maybe, I don't know if I mentioned it when I was, I think what, after we were, I was done working on it. I maybe mentioned the show, but what is it and kind of what's it supposed to be?

**Jason Kridner:** Yeah. So for all those internets of toilets, it is a long range, low power, wireless board, right? That, you know, has a micro bus connection on it. And we worked with the folks at Microelectronica to put IDs on the, their click boards. So now that most of the, the, the new board, all the new boards have click ID. The magic of that is you take something like the, the, the Beagle Play that also has that same long range, low power wireless connection on it. And it makes those Beagle Connects show up as like, when one pops up on the network, it looks like you've added a new micro bus to your board using gray bus, which is this stuff that came from a project aura, which was this attempt by Kickstarter. I think to, to make a modular mobile phone that Google then bought out.

**Chris Gammell:** Oh, Kickstarter did that. I knew Google did it at some point. I think it was again.

**Jason Kridner:** I don't know where it's, I don't know where it started, but it started independent before Google bought it. I didn't know that.

**Chris Gammell:** Okay.

**Jason Kridner:** Yeah. And then Google sucked it up and, and, and ended up in, in, you know, the, the moto mods. Right. So the Motorola, yeah, the moto mods, right. Is the, the only kind of, I think real instantiation realize that I'm going to drop 15 more just like random vocabulary words. Yeah.

**Chris Gammell:** Yeah. Moto mods was a pluggable, like module. You could plug to the buy back of your cell phone. Yeah. Your phone could become like a Bluetooth speaker. It could become like a bunch of other things by just plugging these things in.

**Jason Kridner:** How about getting rid of e-waste? Right. I mean, just a little bit of like, you know, I want a new processor. I want a new camera. I want like a new, you know, more memory when you want to upgrade any of these things or replace broken ones. Right. Why do you have to replace your entire phone? Right. You know, if I want to go from 5g to 35g, you know, whatever network, right. Why do I have to replace my, my processor and my, it's just breaking it down into some more manageable chunks. For, for many reasons, right. That you can probably start to surmise. This wasn't necessarily in the interest of the cell phone makers. Right. So it didn't necessarily live very long, even though it was a really great thing for consumers. But yeah, that's what the Beagle Connect Freedom, the concept for Beagle Connect came from. Right. Is this idea of providing a way for the Linux kernel to connect to new things and automatically and discover and use them. Right. So it's, it's because you look at, we talked about the, all those things that are in Microbus. Right. Like SPI and I2C and all the, and the, the funky embedded serial buses. Right. That you need to connect to most of the things that are in embedded electronics. And those things don't dynamically plug into Linux normally. And here you're adding new controllers. Right. So, so Graybus provided a solution for, for doing that.

**Chris Gammell:** Got it. So now someone's like on their Beagle or Beagle Play, which is like another one of the, the various Linux systems that's out there. Right. They, they have a Beagle Connect Freedom with like a BME280 on it or something like it. That just shows up as like a, what's like, like a standard, standard address inside Linux.

**Jason Kridner:** Right. What, what would happen, right? So the Beagle Connect gets on the network and it, the, the Linux driver will go out and actually probe it. So the one wire ID that's on the click board would say, Hey, I'm at BME280. It's that temperature pressure sensor, right? That's an, that's an, yeah. It's a Bosch, Bosch sensor tech.

**Chris Gammell:** Yeah. Yeah. Weather sensor. That's the weather click that I've used many times on, from. Yeah.

**Jason Kridner:** And so it sees the I2C bus that it was connected to as a new bus that's been added to the system. And it's been told that it's, it's the, the BME680 sensor and it loads the Linux driver for it. And then it just sends I2C commands over the long range wireless connection. Yeah.

**Chris Gammell:** And then the, because the drivers are sitting at the, at the Linux level as well, that you don't have to carry all that on the, on the microcontroller side, which is interesting. Right.

**Jason Kridner:** So you just put a, you use the same static firmware load on the microcontroller for all the different sensors, right? Because they are just bus transports, right? It's just, just doing, just translating the wireless commands into the I2C or spy or whatever commands.

**Chris Gammell:** Yeah. I mean, I think my, you know, like similar, similar, like a thing in a similar situation, it's like, I would probably be like, okay, well, if I'm going to have a sensor node talking back to a gateway, I'm probably going to put the intel, like the driver side on the microcontroller itself. But that does not lend itself to dynamic loading, right? If I were like, you know, turn it off, plug a different click in and then turn it back on the light, the likelihood of having all of the sensor drivers on that small microcontroller are very, very low. So like the swappability is very off from this use case.

**Jason Kridner:** So yeah, the, the thing that I'm trying to sort of fix in this is the, you know, the, the cut and paste, it sort of happens when the, the kind of the typical development cycle of doing exactly what you're doing, which is like, I'm going to go search the internet for an Arduino example of something under setup and loop, right? So that's going to, you know, read that. And then I'm going to try to copy and paste in some networking commands inside of that, you know, and this is maybe where you'd want something like Zephyr and getting a TCP IP stack on it. But that, but like you're writing a lot of new code and the, the, the biggest issue with that is really the number of eyeballs on it, right? The thing I love about the Linux kernel and Zephyr is just how many people get involved in the review and quality control of that software. The best thing is also the worst thing.

**Chris Gammell:** Yeah. Yeah.

**Jason Kridner:** It makes it harder to get it in. Right. But once it's in, right. Yeah. You've got a much better idea that it, that it works. Right. So by pushing this kind of giving a single point for the world to debug, right. Yeah. And work and make it, make it work well. And at least that rapid prototype is possible. I do think like for, for power reasons, there's going to be things that you want to do custom on that sensor that you're probably not going to stay with the fixed firmware load on there for forever. Right. And there's a lot of more intelligence that ultimately needs to be pushed down, you know, and we can talk about maybe how that might make sense to go do in a more scalable way. You know, stuff like if you look inside the Linux kernel, there's this weird, there's this really weird thing of like on any platform, you can run x86 code to help with your networking.

**Chris Gammell:** Okay. Does a lot of good on your arm, on your arm ships. Yeah.

**Jason Kridner:** But so you have to emulate like, like for, for, for networking stacks, you have to emulate this x86. It's sent as kind of like a byte code for accelerating network packet stuff. Right. Push it down with the alert. There's, there's, there's all sorts of these weird kind of cases where people are trying to keep programmability longer than the life cycle. And something like that, I think may ultimately make sense to kind of push into these sensors. I specifically look at WebAssembly.

**Chris Gammell:** Hmm. I have a lot of friends, friends in, in my sphere who like it now. I don't, I don't, I'm not sure it's been mentioned on the show before though. So yeah, maybe explain that.

**Jason Kridner:** Oh, what WebAssembly is?

**Chris Gammell:** Yeah. I mean, I know it's been out there a long time, but I don't think, I, like I said, I don't think we mentioned on The Amp Hour ever before.

**Jason Kridner:** So really? Okay. I thought, cause I, I think there's more and more people doing embedded stuff with, with WebAssembly. So I'm kind of surprised it hasn't come up.

**Chris Gammell:** I just think, you know, think about, think about the, the typical hardware firmware user versus the, you know, like you're up in the Linux land. Right. Yeah. Um, I, so I, maybe I'm wrong though. I also, you know, my sphere has been shrinking as well. So like also. Yeah.

**Jason Kridner:** So just like you could target and, you know, it's, it's a, you think of Java a little bit, right. And like the, the idea of having, you know, bytecode. Um, yeah, yeah. I think I can't think about Java. A lot of the problems that were there with, with there are there still somewhat with, with Java, you know, or fixed. This is it's it's it. WebAssembly primarily targets the browser, right? So it's a, it's a, it's a way, at least in the browser context of having more efficient code, bytecode level, kind of like what Java did for the web, you know, running in the browser. And so most of the browsers have it, have it natively. Now it's a little weird that you actually have to use JavaScript to invoke it, but whatever, but from a, an embedded standpoint, right? So you can run a virtual machine on a, on a microcontroller that you can kind of treat that.

**Chris Gammell:** I think, I think that right there, that assumption, I mean, you can do it, but again, I don't think a lot of the listening audience, there's like, oh yeah, virtual machine on a microcontroller. Like from a battery perspective, that's not like the most likely scenario. I feel like, you know, if you're really optimizing down to the, you know, the micro, microamps and similar. Maybe. Probably not. Yeah.

**Jason Kridner:** Maybe. You know, I do. And some of the stuff I do, I really do care about going into the, to the, to the microamps. And I'm not saying the tooling is quite there yet, but the idea of using high level programming, you know, doesn't preclude you from doing low power stuff. Right. It's just a matter of you, you got to know your tools, right? You got to know what it's actually going to spit out and what it's actually going to do.

**Chris Gammell:** Yes. I think in the general case, the people that are using high level tools are probably not thinking about that first, but they might think about it eventually.

**Jason Kridner:** Yeah.

**Chris Gammell:** Right. So it's not like impossible to do low power, but it's probably impossible to do lowest power. Right. Maybe that's a better way to say it.

**Jason Kridner:** Maybe. But like, are you writing in assembler these days?

**Chris Gammell:** No. Yeah. You're right. I mean, like it can always, you know, like. You're like, how's your hex code these days, Chris? Come on. Yeah. Yeah, exactly.

**Jason Kridner:** You spent too many times like flipping toggle switches. Right. Yeah. The program counter switch.

**Chris Gammell:** I'm a purist. Yeah. Yeah. Of course. You know, I'm not good at any of this stuff, Jason. So like that's, you know, that's couching that.

**Jason Kridner:** The AI will fix it for you.

**Chris Gammell:** Of course. Yeah.

**Jason Kridner:** Sorry. WebAssembly though, you know, sometimes you care about having the code updatable. Right. And so kind of having some clear boundaries in your system. Right. So yeah, I mean, your power management is likely not within that context. Yeah. Although it could be. Sure. It's probably not. But I do kind of toy with remotely managed assets a fair bit. Right. So that's why I really love the Linux stuff. But for, you know, for power reasons, right? Sometimes the Linux machine isn't always the answer. I don't love MCU boot. I don't know about you. It doesn't solve the world for me. Doing over there updates is, can be kind of a pain sometimes. So having a managed system, like a virtual machine.

**Chris Gammell:** Got it. So you're talking more about like having, so you're pushing dynamic code and you're like reconfiguring on the fly, that sort of thing. I see. So it's not, it's running a true, like a software application almost on a microcontroller versus more of a firmware application where there's no container that can be destructed and reconstructed.

**Jason Kridner:** Right. I mean, there's just like sometimes, you know, okay, this is just some remote data collection device, right? Why should I really ever need to change it? Well, like sometimes you understand more or less about, you know, when it should be an energy harvesting mode or when it should it be, you know, how often should be collecting what data? And can you change the data rates, right? And you can parameterize the world, right? And that's probably okay, right? But, you know, you talk about lower power, you know, sometimes the answer to making it, you know, if you just have a generic configurable solution, you can update the firmware. Just make the firmware do what you want it to do and configure it ahead of time, right? Configure it at build time, not at runtime. Like that saves a lot of power and boot time if you're doing your configuration at build time instead of runtime.

**Chris Gammell:** It's the configuration and being in what case, in this case, what is the configuration controlling?

**Jason Kridner:** Like how often, how long is my sleep loop, right? Like that sort of thing, right? Right. If I have to go read some non-volatile values about like how often, like what is my sleep time supposed to be or figuring that stuff out and then just having it. If you have an update solution, right, that's a more generic solution than just making your app configurable at runtime.

**Chris Gammell:** I see. Got it. Got it. And what did you say you didn't like about MC?

**Jason Kridner:** It's a little bit big for just largely AB. It has like, because it has some of the stuff for doing the swaps and doing some more of the basic things you need. But it's certainly not end-to-end over-the-air updates, right, in and of itself. And so you have to put a fair bit of complexity into your application to actually perform the firmware updates. Because it doesn't integrate at the MCU boot level. It's not so much a dig as it is a task left to the user, right? There's still a lot more to do. It doesn't, just because you have MCU boot doesn't mean you have firmware over-the-air updates, right? Yeah. You know a lot more about that.

**Chris Gammell:** That's right. Yeah. But do you wish it would do more or do you wish it would do less, I guess?

**Jason Kridner:** I wish I had a tool that did more, but, you know, was easier to do. So, obviously, the impossible, right?

**Chris Gammell:** Sounds like Goliath is the answer for you. Yeah. Sounds like I need Goliath. That's right.

**Jason Kridner:** Sounds like I need Goliath. It's just to be free with Zephyr, though. It is free.

**Chris Gammell:** I think this actually kind of comes back to your kind of like your 10-minute thing, too, because it's like you are kind of down in the muck and the mire of MCU boot, but then all the way up to the Linux side of things. And I'd love to kind of swoop back up into that in that realm as well, because, you know, like, one, it shows you have a lot of range. But two, I'm kind of curious about your take on, you know, the Linux space these days is like, you know, on these sometimes portable, sometimes powerful, sometimes in between, like, and especially like where you think people should be getting started in that space.

**Jason Kridner:** You mean, how do you learn about Linux?

**Chris Gammell:** Yeah. Like, well, like, and specifically, like, on a, let's just say on like a Beagle product, right? So, like, I think most people start as a user, but then some of them want to customize and optimize and that sort of thing as well. So, like, where do you think people are entering the ecosystem and where do you recommend they enter the ecosystem?

**Jason Kridner:** You know, for most people, I, you know, when you're getting started, you know, we have Debian, recommended Debian images, and there's an imager tool, BB Imager RS or the Beagle Board Imaging Utility, and that'll program an SD card. And that's really great for starting with the Pocket Beagle 2. And we have this thing called Tech Lab. It's a, I don't know if we're going to show it for your benefit, and you can link to it later. But this thing is the Tech Lab.

**Chris Gammell:** It's like a breakout for the Pocket Beagle. Yeah.

**Jason Kridner:** So we talked about all those embedded serial buses, right? And it's targets that are, like, known working, right? For SPI, I2C, PWM, analog input, right? Kind of all the stuff that you typically use, USB as well, for, you know, connecting to embedded stuff, right? So connecting up to the sensors, actuators, indicators, and networking devices that you typically connect to in an embedded system.

**Chris Gammell:** Yeah, because the Pocket Beagle is, I mean, it's small and it's compact on its own. It's lower cost because it doesn't have all that stuff on it. But then if you don't want to test and exercise, it's like, well, you need to plug it into something to kind of build around it.

**Jason Kridner:** And I would recommend doing the Tech Lab. We initially developed that with the Linux Foundation folks when they were doing some kind of teaser trainings at different trade shows. And so there's videos online of those happening with the original Pocket Beagle. And originally, Michael Welling's Bacon Bits was used, but then we made the Tech Lab. And so I really like that as a base. And they dive into Yocto and Build Root as well. So there's a bunch of materials when you get to that point. But I'd recommend people start with Debian and not be scared to write some kernel modules. PyPy is not your friend. I'm sorry.

**Chris Gammell:** Okay. All right.

**Jason Kridner:** It looks nice and friendly, but there'd be dragons.

**Chris Gammell:** Got it. Like supply chain attacks and similar things that people probably know about. Yeah, yeah.

**Jason Kridner:** I mean, we've seen that repeatedly, right? But I think the quality issue is more fundamental, right? Like you're not... Like nobody's policing it to say that I'm actually documenting all the exceptions that I generate. Yeah.

**Chris Gammell:** Right. And some people just grab it and go, and then they don't think about it until it's broken out in the field, right? That's another issue.

**Jason Kridner:** And that's the big thing. It's like you don't know when you've tested your code enough because you don't know what those lower levels are doing, right? So it looks like, oh, we're great, we're great, we're great, we're great, we're great. And then... Right, right.

**Chris Gammell:** This is in a factory for a million hours. It's like, yeah, it doesn't work great. Yeah.

**Jason Kridner:** I just be, you know, it's not like, you know, it's not like I don't do it. I do it too, right? I just, you know...

**Chris Gammell:** But he knows what he's getting into. Yeah.

**Jason Kridner:** Well, I just discourage, like, you know, depending on it too much, right? It's, you know, when it doesn't work, right? When the router, you know, stops shifting packets, that sort of thing, right? There's just... I trust much more things like the Linux kernel. It's not that you don't get bugs there, but there's also, you know, one place to fix them all and everybody can go to that one place to get them fixed.

**Chris Gammell:** So when you said write kernel modules as well, so like you're expecting... Not expecting. So if I wanted to go and build a kernel module then, like what path should I go down? This is going to be like writing a driver that gets pushed into the kernel or maybe is like out of tree that gets pulled in for my specific build. Is that the thought there?

**Jason Kridner:** That's it. That's it. And I would encourage you to, if you've written something that hasn't been written before, to go ahead and submit it, right? And wear your thick skin and like just put it out there. And I think your code is going to be better for it. It's rather than sitting in PiPi, right? Rather than saying, oh, well, you know, I figured out how to get XYZ sensor to talk over, you know, the Pi SM bus, whatever. And, you know, I don't know which is the current I2C. Yeah, whatever that is. Like, you know where the I2C driver is in Linux, right? Because it's the I2C controller driver. And, yeah, the EAL materials, you know, they're a little bit dated now, but that's something I'm trying to redo. And then something we've leveraged on the BeagleBadge as well.

**Chris Gammell:** That's one of the things we haven't talked about is BeagleBadge. What is BeagleBadge?

**Jason Kridner:** So BeagleBadge, we took e-paper and 4.2-inch e-paper display. We took a new low-power, low-cost processor from TI, our good friends at TI. It's a dual-core A53, just a simple one. And, you know, put it on the e-paper. But then we put a LoRa radio and a Wi-Fi radio on it. So it's not the TI low-power wireless. It's actually the LoRa stuff, right? So we can try to do MeshTastic, right? That's a goal for us is to do MeshTastic. And then, you know, I took the stuff that was on that Tech Lab board and put it directly on there, right? So we can still leverage all that learning for SPI, Analog-In, PWM-Out, I2C, and just kind of leverage those same teaching materials, right, for learning how to write Linux drivers. And then you got MicroBus and USB on there as well. You know, it has a battery charger and a fuel gauge. And yeah, in terms of sensors, right, it's got a light sensor. It's got a accelerometer. I think it's got a temperature humidity sensor built in. But of course, since you've got the MicroBus. And it's also got QUIC, Q-W-I-I-C.

**Chris Gammell:** Oh, yeah. And growth. That's on the Zepto as well, right?

**Jason Kridner:** Yep, yep. And so you can connect Zeptos to it, right? So, like, the things that I'm trying to do with the Zepto mostly involve, like, the interacting with the badge right now, right? So the idea, you make your little controller with a Zepto and you bring it up to a badge, right? So you can program it from the badge. You know, we've got the Visual Studio code stuff, right? So you point your web browser to the badge and you can program it that way. And then, you know, most of the kind of demo apps, right? There's a little badge launcher and things are all written in MicroPython with the LVGL for the UI, if you know LVGL.

**Chris Gammell:** Mm-hmm. Yeah, yeah.

**Jason Kridner:** There's also, just pushed in this last week, a mainline support for BeagleBadge and Zephyr, right? So you can just target, you know, the A53s as if they were just MCUs.

**Chris Gammell:** Yeah, yeah. I've been seeing that a bunch, a bunch of, like, Cortex-A targets in Zephyr, which is surprising.

**Jason Kridner:** Sometimes people don't want Linux, yeah.

**Chris Gammell:** I mean, memory's not getting any cheaper, so it could be that. Certainly not. Yeah, yeah. How are you guys, how are you guys doing with that?

**Jason Kridner:** That's rough. We have a great relationship with Kingston, you know, as our primary memory supplier and they're doing, you know, what they can to kind of keep us moving. We've committed to not doing pricing updates more than once a quarter.

**Speaker ?:** Okay.

**Jason Kridner:** I think that's impressive. You know, I personally am kind of proud of us and we've avoided, like, jacking our prices way up and we're trying to eat what we can and get through it, right? And at least try to give some people, you know, a little bit of, as much predictability in the pricing as we can.

**Chris Gammell:** Especially if you're targeting educational markets, too. It's like, you know, talk about populations that are, like, even more susceptible to pricing sensitivity. It's just like, yeah, it's wild, you know? Yeah. Yeah.

**Jason Kridner:** But it makes it even more important for us to do things at the microcontroller level to keep people on things that they can afford to get a hold of. You know, we've been kind of slow to go to microcontrollers in general, just because, like, we're not just open hardware, like, we're really focused on the open source software stacks, but Zephyr is finally getting to that point, right? And, you know, the Arduino core on Zephyr is really helpful for that. The MicroPython port on Zephyr is really helpful for that. And then, of course, we do microblocks on type of the Arduino core on Zephyr as well. Lots of layers. Lots of layers. I know the power situation, right? Yeah. It's good.

**Chris Gammell:** It does actually kind of have a good story, though, too, like, from, like, you know, maybe you are, maybe someone is just starting with a Beagle Y AI just because it's what they have on their desk and they're already doing stuff there. But then they, you know, they're going, you know, they're basically, they decide to traverse down the stack to get lower power or faster or just availability or whatever it is, right? Like, having these things in between is actually really interesting and important to, again, just to bring more people into the ecosystem, like, to show that, like, yeah, there's all of these options. You could build this with whatever the hell you want to, but, you know, there's probably going to be a better option than others because of ABC, whatever reasons there are. So.

**Jason Kridner:** Hope so. If you look at the Beagle Connect Zepto, we've also got a friction fit connection for the hat side. Like, so there's, like, it's got the micro bus, but that other edge is actually designed for connecting up to a hat connector on either a Raspberry Pi or Beagle Y AI. So you can program it directly that way. And the SWD pins are brought out there and the bootloader invocation and UART, right? So you can use that as a, like, as a Zephyr development host, right? And just trying to get these normalized environments, right? So that people don't spend all their time. Zephyr is not a simple build system. It's not necessarily in love with that. I love the community. I love, like, all the features and the fact that it's very scalable, right? You can turn off most of the stuff.

**Chris Gammell:** West manifests with the allow list and West update narrow. Those are the two things. That is my Zephyr tip for the day that will save your computer from ingesting the entire universe of Zephyr things. Those are very important.

**Jason Kridner:** Very, very. You're right. You're right. Allow lists are huge, right? So, you know, I typically develop with just two things in my allow list, right? My how, and then like SimSys, right? That's huge, right?

**Chris Gammell:** Yeah. So that'll get you. That'll get you.

**Jason Kridner:** Narrow. You can actually still do like, like shallow. There's like a shallow thing. And then there's also things that you can do for constrained memory environments as well that are increasing the kind of tolerance for the pack, the packing stuff, right? But it's not nearly as bad as working with Linux, right? So cloning the Linux kernel is still much longer than cloning Zephyr.

**Chris Gammell:** It'll eat up your IP tables and have you resetting around them otherwise.

**Jason Kridner:** That's right. That's right.

**Chris Gammell:** Comcast! Comcast. Man. You guys have fiber up in Michigan? I thought you... I'm sure. I'm sure. We've had our fiber knocked out three times because of other fiber installers knocking out fiber installed fiber installed fiber. So, yeah. It's not all roses when you do have fiber coming through the neighborhoods.

**Jason Kridner:** Yeah, I'm jealous. All right. You know, I think it's used to travel to Japan all the time in the 90s when everybody had fiber.

**Chris Gammell:** Right, right. Of course. Of course. We're still behind. Yeah. Even if we're...

**Jason Kridner:** So, it's like, okay. You know, the thing is, I want to plug somebody else's stuff. I don't think we've talked about this on the show yet, right? So, we've got the Beagle Connect Zepto and the Beagle Badge and the Pocket Beagle 2 and the Tech Lab and all that stuff. But I want to plug some...

**Chris Gammell:** Is that all, Jason? Is that all? Yeah.

**Jason Kridner:** We've got lots of stuff.

**Chris Gammell:** All right. Who's the other person?

**Jason Kridner:** I want to plug the bow chip, right? And the dowel bell.

**Chris Gammell:** Oh, yeah.

**Jason Kridner:** Yeah. Do you know much about that thing?

**Chris Gammell:** We've only mentioned it on the show. I haven't asked Bunny and Zobs to come back on. You know, they've been on the show many times before, but haven't had them back since they've announced the bow.

**Jason Kridner:** I think it's, you know, talking about people caring about open hardware and, you know, and how accessible things are. But there's more and more ways that individuals can get involved with open source hardware. And I think that that's a big milestone, honestly, for open source hardware, right? And, you know, I've got some, you know, 10-minute plans for projects on using the bow chip, right? But, you know, because we eventually want to do like a Beagle Connect with the bow chip. The idea is the single-pair Ethernet stuff with the power over data line. And theoretically, you know, in our chats, we think we can kind of bang a Mac layer interface to do, put some single-pair Ethernet PHYs out there and do the, you know, the Beagle play has 10-base T1L, right? So that's the one where you can run like a kilometer of distance off the wire, not the star topology, but just kind of point to point. You know, the idea is we can kind of daisy chain that, right, if you've got two PHYs. And although we put five volts on the wire, it's not going to be useful for running a kilometer. You know, you can probably do the math there and, you know, resistance per foot is probably not going to run a kilometer if you need the power. But for like, you know, short runs, you know, like a meter sort of thing, it'd be pretty nice for doing some powering some sensors. So, you know, just a fun way to get down to just two wires and then doing the Beagle Connect stuff on there, right? So, you know, running Zephyr on the RISC-V core and then having the power over data line and the Ethernet, right? So that's the concept. Yeah, I think I'm excited about having a, like a true open source chip to play with. And then, you know, some of the stuff that he's put in there for accelerating the I.O., right? So he's got this, what do you call it? PIO?

**Chris Gammell:** It's like a PIO. It's like a instruction set.

**Jason Kridner:** I guess PIO is RP24.

**Chris Gammell:** Yeah.

**Jason Kridner:** Yeah. And like with the Pocket Beagle 2, we have the PRUs that people use for stuff, right? You haven't seen Bella yet, have you? Oh my gosh. I can't believe I haven't had a plug for Bella yet.

**Chris Gammell:** Bella's the sound one?

**Jason Kridner:** It's an add-on. It's an audio add-on for Pocket Beagle. They've launched the, when we did the Pocket Beagle 2, they launched this thing called GEM, G-E-M, which is, you know, open source stack for making synthesizers.

**Chris Gammell:** I've heard about it. Maybe not on the show. Maybe even talked about it on the show, but I definitely, maybe Michael Welling told me about it, but I definitely have heard about it in you and I talking about it at some point in the past. I'm not sure if I mentioned the show, so that's cool. So many things.

**Jason Kridner:** So many things.

**Chris Gammell:** Well, and you guys do have done RISC-V before. You've had RISC-V, you have RISC-V boards on your, on your.

**Jason Kridner:** Yeah, the Beagle 5 Fire is RISC-V. We did the Beagle 5 Ahead as well, which is a little higher performing RISC-V. And there's actually, you know, they've released some of the chip, the CPU, they released RTL level simulator, you know, simulator level RTL code for the open C910 from Alibaba on that. You know, it's not the, it's not exactly what you would make the CPU from, but for such a high performing CPU, it's pretty big jump up.

**Chris Gammell:** And this actually is good too, because I feel like it's a really good example of like, like RISC-V open ISA, right? But there's no guarantee of open processor. Exactly. Or open, you know, op codes all the way down, right? But it, like you're saying with the bow, it actually is, right? That is like fully open all the way top to bottom?

**Jason Kridner:** Yeah, the bow chip is actually, the CPU is actually open source, not just the instruction set architecture, right? So with RISC-V, you have that instruction set architecture that's open, but the implementations are, there's no guarantee whatsoever or extensions. So here it's actually an open CPU.

**Chris Gammell:** Claire Wolf had the RV32 that was open, I believe, right? That, and that got used a lot of places, but then that is a little bit different. And that's like the small, very, very small processor as well.

**Jason Kridner:** Oh yeah. I'm not familiar with that one.

**Chris Gammell:** Okay. That was a older one. Yeah. But that's where you see, you see that.

**Jason Kridner:** There's been a bunch of open source RISC-V cores, right? I think it's different when you can actually get ahold of the chips, right? So, so I think that's, that's kind of the milestone here is that it's actually something going to production and that, you know, regular open hardware users can get their hands on without having to tape out, without having to tape out something. So I think it's a big jump. You know, there's, there's, and, you know, I'm cursely aware of other, you know, developments that are as exciting, but the bow chip is actually in my hands and, you know, I'm pretty amazed by it. I have to ask you about the castellated headers. So it's in a form factor, a board. I don't know if it does any good to show anything because you're not, or it's just audio, but so it's got the castellated headers on it. And I kind of repeatedly like BeagleConnect Zepto, we didn't do that, right? We have no bottom side components. And we did the little staggering for the friction fit for the, for the BeagleConnect. I mean, for the, for the, sorry, the, the micro bus, but we didn't do the castellated headers thing. And I feel like that only ever matters if you're actually using an iron and you don't have hot air.

**Chris Gammell:** I actually, I'm going to, just because I have my desk of junk, Jason, I talked about like, he's trying to have a clean desk. Mine is a desk of junk, but I actually have an example directly in front of me where I can, I had an RP 2040. There you go. Yeah. I had an RP 2040 though, where I put, I put one of those with the full, sorry, it's, it's actually the Pico, right? That's what they call this. Yeah. So it's the Pico and I just soldered it down, right? It's, it, it is.

**Jason Kridner:** But did you, but did you just put solder paste and, and hot air? I mean, I feel like, I feel like you'd waste so much time if you sat there and tried to do iron each little spot. I mean, just put a little paste down and run the hot air over it.

**Chris Gammell:** This was done at the fab. I didn't do that. So this comes on tape. Oh, yeah. That's the reason to do it.

**Jason Kridner:** I'm just saying that you don't need castellated headers to do that. If you've got no bottom side components and you've got, you know, gold plated through holes, you know, with a decent amount of like wicking surface, right? You know, if you, you, you're making like, you put paste on a board and you, you, you, you, and you reflow it, you don't need castellated, right? It's, that's an expensive add to the PCB process.

**Chris Gammell:** It is an expensive add. Yes. Right. And especially given the, you know, you talk to the RP team at Raspberry Pi, those guys, I would not say are spendthrifts, right? They're not like, they're not ready to spend extra money for no reason. So, yeah. In fact, I would categorize them and they've categorized themselves as cheapskates, I believe. And I love them for it. You know, that's good. Right. I mean, that's what you should be.

**Jason Kridner:** That's, I think that's respecting the user. Like when you cut the cost out, right? You don't want to cut out functionality, but I'm trying to understand what the real value, that's why I asked you, right? Is like what the real value of castellated headers are, because that's an often requested thing. And, and, and, and it's not needed for reflow. I feel like it's where it's only real.

**Chris Gammell:** It's not for reflow. It is needed for visual inspection of reflow though. Right. That's, I think that's the key thing. You can see when the, you know, you can see the fillet, right? That's, that's the key thing. And if you can't see it because, you know, you've got a full through hole and it's just, you know, you assumed it got sucked up in there and you don't know, cause you can't have like an AOI look at it. It's like, okay, then that's, that's not good enough. I think.

**Jason Kridner:** Okay. I mean, cause you can, you can still get a little bit of wicking on, you know, visible through the hole. Yeah.

**Chris Gammell:** You will get, you will get wicking. Yeah, of course. But it's just not as, it's not as right. And I think it's just expectation. So it's also like a visual indicator to say like, if I look at a Pico or like the bow, it's like, I know that that's meant to, to go on a board, right? Versus a, you know, a through hole. It's like, okay, well maybe it could, I've done it. I've done it with a teensy. Right. But is that the real, is that the intention? Yeah. That's okay. Yeah.

**Jason Kridner:** I mean, cause that was part of like why I didn't put headers on the pocket Beagle originally. It was meant to be solder downable. Right. So I didn't want to put the headers on and like have it be in the way and then trying to manage multiple SKUs for once the header just kind of got to be a headache. So we just, you know, we, we, we ended up making custom headers, unfortunately for the, the, the pocket Beagle too. Right. Because we have this combination of through hole and surface mount that gives it the good retention. Right. So you can't break them off easy.

**Chris Gammell:** Yeah. You know, just like, like linear or like sheer force kind of thing.

**Jason Kridner:** So we've got the through holes to kind of prevent that sheer force and like, and they grab, right? So these, these connections grab, like you wouldn't think, cause we, we made them shallow so we can do the boards a little bit tighter together. Um, and so you can use the shorter pins, but they grab.

**Chris Gammell:** Well, there's some cost right there. You could just do that and switch it over to Castellate. You're good.

**Jason Kridner:** Well, yeah, we have two rows. We can't do that really on the pocket Beagle. Right. And, and, and most of, there's just a lot of situations where we found that people for, for rapid purge, I've been wanting to be able to add and remove the modules and stuff like that, but for, and, and, and so like the, the concept with the Zepto, like you kind of support the rapid prototyping and the quick connection with friction fit. Right. So you just put regular, you know, the DuPont steak pins, right? I don't know how they got named that. Whatever just the, the, the, the stabby kind. The stabby kind. Yeah. You just put the regular stabby steak pins on it, on your board and you can just slide it on and it's going to make contact. Right. And then, you know, and then in the next round, don't populate the stabby things. Just, just a reflow directly on, on, on top of that. You know, you probably want to replace your, your baseboard, you know, through holes with just, you know, pads, surface pads, right. That you can get, get some solder paste on top of and you're done. Right. So I don't know, I'm, I'm, you know, the points that you've made about like, well, it's not obvious, right? I can't see that it's, I'm supposed to be able to solder this or right. I can't necessarily, you know, you've, you've already had to gotten used of not seeing that the solder underneath. Right. You know, I know if you, you may not have an x-ray machine, right. You know, but you know, there's enough, you know, I spend too much time playing with BGAs. Right. So most of the stuff I do is BGAs.

**Chris Gammell:** Take it off and put it back on again. I've had to get used.

**Jason Kridner:** Oh yeah. We've done that too. So yeah. Reballing BGAs and stuff like, you know, doing that, but so I've had to get used to that. And that's where I, like my perspective, right. Might be just kind of off. Right. So that's, that's a, that's a useful lesson for me because I think it's tough to have

**Chris Gammell:** a knowledge of how users are going to use your stuff though. Right. It means, you know, who knows?

**Jason Kridner:** Um, so there's certain, like I gotta get past the, the, the initial rejection of it. Right. It's like cast related headers. Come on. You don't need that.

**Chris Gammell:** Come on, man. Yeah. Yeah. Yeah. Yeah. I don't know. I've used them. I, I think they're okay. I think if you're soldering anything down at that level to a board, you know, you have to be ready to just throw it out anyways. Right.

**Jason Kridner:** It's just, uh, put enough solder on and heat the heat it up. Right. And let her rip. It's going to be okay. Let her rip.

**Chris Gammell:** Yep. Yep. Yep. Well, Jason, where can people find all the BeagleBoard stuff and stuff about you and I'll have links in. Yeah.

**Jason Kridner:** I keep a, I keep a public calendar, calendly.com slash Jay Kreidner. Right. So that's the best way to actually get ahold of me. If it's a technical support question on BeagleBoard, you can send it to me, but you better send it to the forum first. Right. So forum, forum.beagleboard.org. Like if it's a support question, send it there, give it 24 hours. Somebody smarter than me is likely going to reply. If they don't. Yeah. Put something on my calendar and that's the escalation path. You know, I've, I got kind of suckered into starting a discord. Oh no. Somebody, and like pretty quick, like 3000 people popped up on our discord channel. So it's kind of hard to shut it out, but, but I, you know, I hate walled gardens and like, I kind of tolerate, I made the mistake of tolerating it for about a year. So now there's a Zulip.openbeagle.org because I needed to go somewhere that it wasn't and shitified.

**Chris Gammell:** Yeah. It's not going to get better after the IPO as well.

**Jason Kridner:** So, so I, I, I am, I will vocally speak out against discord is a sucky ass walled garden.

**Chris Gammell:** Yes. I'm right there with you. I think it, I don't know if it's grumpy old man syndrome or what it is, but yeah. Yeah. I'm not a fan.

**Jason Kridner:** My, uh, yeah, I don't, I don't expect to be able to get people back to IRC, you know, but, uh, at least Zulip.

**Chris Gammell:** Even IRC, I just, I can't pay attention so long. You know, you mentioned your 10 minute windows. I just can't, you know, 10 minutes later, I'm just like, ah, well then no one's responded. I'll see you later. And then I come back two months later. I'm like, oh, they did respond.

**Jason Kridner:** They did respond. Yeah. Yeah. It was like a day and a half later.

**Chris Gammell:** Yeah. Right. Right. Exactly. So, no. Oh, well.

**Jason Kridner:** Yeah. So the instant stuff, right. If you, you, you might find me on Zulip more likely and you'll find me on, on, on discord, but really like just throw something on the calendar. If it's worth my time, it's worth your time too.

**Chris Gammell:** All right. Well, thank you, Jason, for being back. Uh, it was been very worth my time. I really appreciate it. And, uh, keep going with all the things you're building, um, and all the people you're educating.

**Jason Kridner:** Thanks, Chris.

**Jason Kridner:** Thanks, Chris.
