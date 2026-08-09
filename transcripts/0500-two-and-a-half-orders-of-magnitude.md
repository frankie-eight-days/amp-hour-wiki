---
episode: 500
title: Two and a Half Orders of Magnitude
url: https://theamphour.com/500-two-and-a-half-orders-of-magnitude/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released July 12th, 2020. Episode 500. Two and a half orders of magnitude.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. Does it even matter that we're at 500? I mean, it's fun. It's a shoulder shrug. Come on, 512 is what we're after.

**Chris Gammell:** Okay, 512. I actually did have that thought the other day. 512 would be a little bit more. But, you know, I think the big thing about 500 for us, rather.

**Dave Jones:** Yeah, it's half a decade.

**Chris Gammell:** We average about 50 episodes a year. So this is, we're getting pretty close. It's about, you know, two or three episodes away from our 10-year mark.

**Dave Jones:** Our 10-year. Because when is 10 years?

**Chris Gammell:** Our first show is August 10th, I think.

**Dave Jones:** Oh, August. Really? Okay.

**Chris Gammell:** So it's like about a month away.

**Dave Jones:** Right. 10 years. Jeez, you get less for murder.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. No, but can we name this one? I just, it occurred to me, 500. Half an order of magnitude. Oh, that's good. I like that. Yeah. Yeah, you like that? Okay. Yeah, let's run with that. Because, you know, orders of magnitude, it's a thing.

**Chris Gammell:** Yeah, that's what matters. You know, like that's how you should be estimating stuff. And yeah, that's great. I like that.

**Dave Jones:** For you youngsters out there, I did a video on this, like it was probably 10 years ago. It was one of my like first 30 or something. And yeah, orders of how to impress at a job interview. It's like going there and talk DBs and orders of magnitude. And you'll impress the hell out of people like you know what you're talking about. Now, oh yeah, that's, you know, to the nearest order.

**Chris Gammell:** Yeah, I think when making estimates is good, as long as you, you know, don't show too much, don't show too much bravado about it, you know, and you're like, oh, well, it's definitely this thing, you know.

**Dave Jones:** And you've got to, like engineering's the art of knowing when something doesn't matter and when something matters, right? That's right. Is when you need to be precise and when you don't need to be precise. There's no point. Like I know a lot of engineers who will like be anal retentive about specifying their resistor down to, you know, use the E96 range or something. And like, dude, you don't like it just use a one, just waking a 1k, you know, near enough. Like, yeah.

**Chris Gammell:** Or they're paying a ton for 0.01% or, you know, like, yeah, it's like, yeah. And it doesn't have any impact. And basically then their sourcing sucks and they're, you know, expensive. And yeah, it's a nightmare.

**Dave Jones:** Oh, I didn't. Didn't I recently do a video? You know, I'm always doing my, yeah, I did a recent video. God, I can't remember what it was. I taught, no, I didn't tear it down. I looked at an open source project and looking at how many, they had like 60 different values of resistors on their bill of materials.

**Chris Gammell:** Oh yeah. And you did like a bomb optimization.

**Dave Jones:** A bomb optimization. Yeah. And it was, oh my, yeah. Yeah. Yes. Tutorial PCB bomb consolidation. 1307. Yeah. And yeah, I think it was like 60 different types. And it was like, and that would fill up a pick and place machine. Like a typical, just for the resistors. Yeah.

**Chris Gammell:** Yeah. And you were talking about like lowering the cost of assembly and stuff like that.

**Dave Jones:** Lowering the cost of assembly and lowering the cost, lowering the risk as well of sourcing parts and stuff like that. Because, you know, like you can just risk goofing it up if you can't get these. You're purchasing departments going around like crazy, trying to purchase 60 different reels of resistors. And, you know, oh, they ran out. You know, so you get a phone call at 2 a.m. in the morning from your assembly house because they're urgent, you know, in China. And it's like different time zone or whatever. And you get a call saying, oh, we ran out of 1.02K resistors. You know, and it's like, is it okay if we use a 1K?

**Chris Gammell:** And even if they have to call and ask, that costs time and, you know.

**Dave Jones:** Yeah, of course.

**Chris Gammell:** Your sleep and everything else.

**Dave Jones:** And the lines stop and the production lines stop. And that means you can miss a deadline. And bingo, things just have a cascade, have a way of cascading out of control, you know. And just into big delays and stuff like that.

**Chris Gammell:** Yeah.

**Dave Jones:** Speaking of delays, can we get into the, you cannot buy, apparently, you cannot buy an analog discovery.

**Chris Gammell:** Oh, yeah. Yeah. That's from Vigilant.

**Dave Jones:** You can't get them, apparently.

**Chris Gammell:** Yeah. They wrote an email about it. Did we link this post as well?

**Dave Jones:** Yeah. Yeah. It's on the Reddit.

**Chris Gammell:** Yeah. And so Caitlin is one of the product managers. She is the product manager for analog discovery. And I talked to her about it a little bit. And it's just like all their stuff is tied up in medical and, you know, like a lot of getting the parts. That's one problem. And the other problem is you think about every single engineering department in the country, at least in the US, probably a lot more. There's a ton of educational material around this. And they all basically are like, oh, shit, we need 200 analog discovery twos before September. And they're all trying to buy them at once. So, yeah, I don't know. I actually gave one to, I was working with someone who is a software person and I gave him my analog discovery tube. I used them for contextual electronics.

**Dave Jones:** Yes. I had two of them. I gave one away as well. And yeah.

**Chris Gammell:** So, I gave mine away. This is like my travel scope. You know, like that's what I take and I use a lot. And so, I was like, oh my God. I went on eBay and just like bought one. Just like luckily someone was like, oh, I don't do electronics anymore. And they just sold me cheap. Yeah. Yeah. Yeah. Yeah. And so, keep an eye out on eBay. There's, that's, that's a market. That's my goodness. It's, yeah. I mean, it's just like you think about all the education, right? We're in July, right? So, oh, we're two months away. Two, two months away from what? Two, two months away from a new semester. Maybe even less. I guess even less.

**Dave Jones:** Oh, it's actually less here. Yeah. They start in July here. Yeah.

**Chris Gammell:** Oh, they do. Okay. Okay. Yeah. Yeah. So like.

**Dave Jones:** Unless it's a tri-semester, unless it's a tri-semester based one, which some universities in Australia are. They've moved over to the, like when I was a boy, there was none of this tri-semester rubbish. It was, you know, but no, a lot of courses start in July right now. So. Yeah.

**Chris Gammell:** Yeah. Yeah. Good luck. But like, you think about, you think about the supply chain, even if, even if everything else was good, you've got to get all of these out to all of your students. And it's like, yeah. So we had Brock on the show. Brock Lemaris was on the show three episodes ago and he was talking about some of this stuff and he's doing like embedded remotely. Right. And that's like with dev wars, which is good. But like, when you start to like move out of the digital realm into the analog realm, like, Oh my God, what are you going to do? You know, like you need something like this, or you have to like, then refer people to like to your video and you know, your video about like putting together a lab and be like, well, good luck by all the components too. It's like, Oh, this is a really big ask for students. You know?

**Dave Jones:** Oh, it is. And this is something that David too was into. He used to work at the university of technology. He was a, uh, like he did some tutoring there as, as well as I, he was basically working in a lab. He was actually designing all of the, uh, all of the educational kits and things that these kids, you know, some of them were quite complex, right? They're like, you know, four or six layer boards there, you know, and fairly complicated, lots of parts to do all sorts of various, you know, examples and demos and, and things like that. And he was getting like hundreds of boards made at a time.

**Chris Gammell:** Yeah. I mean, the scale of, of education, you need, you, I mean, you know, you not only need for all the students, but you have to imagine a bunch of students are going to blow them up too. So you need. Oh yeah, exactly. Yeah. Yeah.

**Dave Jones:** You've got to buy more and each student needed one. And it was like, you know, and you got, uh, and especially in the different stages of the courses and things like that. And you needed like, yeah, they were doing like runs of 500 and, and he was saying like, sometimes he was like hand assembling these things working late into the night, you know, hand assembling hundred or hand finalizing or whatever hundreds of these kits and testing them and make sure they work. And, and it's that sort of awkward number where you start putting effort into designing, uh, automated test jigs to actually test the boards and things like that, because you've got to make sure they all work so that, you know, so that the lessons can work. You don't want some student. Well, I do personally. I love it when things fail because that's when you learn the most, of course. So, oh, great. Your board doesn't work. Fantastic. Let's troubleshoot it. You might actually learn something during your degree.

**Chris Gammell:** And yeah, but doing that times a hundred or 200 is, yeah.

**Dave Jones:** I mean like, it's a lot, it's a lot of effort. Yeah.

**Chris Gammell:** Yeah. And, uh, and if it's the equipment that's not working versus like the experiment, that's something else entirely.

**Dave Jones:** So, oh, have I told the story?

**Chris Gammell:** Well, the 500 episodes in.

**Dave Jones:** Probably. I've probably stolen. Someone will remember that. I did that in episode 82. And yeah, I was doing like a digital, I think it was a digital. Yeah. It was a digital logic class. And we had this, uh, you know, breadboard. We were building up all this breadboard, you know, breadboarding up some complicated, you know, digital thing with, you know, a dozen TTL chips or whatnot. And, you know, it was adders and divide, you know, it was doing all sorts of stuff. And we were, we were building this up and nobody's worked. And I'm like, and before I build it up, I'm looking at the circuit and I'm going, this probably isn't going to work. And because like, anyway, everyone built it up. It didn't work, but I went like, I, I, so I built it up as per the schematic, but I, I knew this probably wasn't going to work. And sure enough, it didn't work. And then with minutes, I had it fixed and nobody else had this fixed. And mine was the only one working in the end. What was it? It was a fan out. We were using like seven, four, I think we were, might be showing my age, but I think we might've even been using like, like, like seven, four, not, not seven, four LS. I think it was like seven, four series logic. I, you know, anyway, it was a fan out problem. We had what, like one gate driving like, you know, 12 others. And I'm going, I don't think this is going to work. And, um, and sure enough.

**Chris Gammell:** The drive strength, you mean, and like getting all the way across the board. Yeah.

**Dave Jones:** It's like, nobody had tested this and sure enough, it didn't work. And like, it could only, it only had a fan out of like three or four or something like that. And, and it just didn't work. If people don't know what fan out is, it's chips have a certain drive capability. They can drive a certain amount of current whilst keeping a, the minimum low and high threshold levels required. There's high drive and there's low drive from the totem pole output. And, uh, it can drive enough current so that it, uh, can drive all the inputs to all the other chips. And this isn't a problem on CMOS. It only becomes a problem on CMOS when you have actually capacitance on the line where, where the capacitance becomes the load at frequency. You're driving across a big table or something. Yeah. Yeah. Yeah. Alongwise, all the input gates have X amount of capacitance and stuff like that. Cause essentially a CMOS devices, you know, infinite input impedance essentially.

**Chris Gammell:** Right. Except for, uh, with the Miller, the Miller thing we could talk about. Oh, we could talk about the Miller plateau. Yeah. Yeah. Right.

**Dave Jones:** And yeah, we'll segue into that one. And yeah, it's sure enough. It, it, it didn't work. And to my, like, and apparently like we ran out of time or something and like, they just passed everyone. It's like, you gotta be kidding. Mine's the only one that I was pissed off. Mine was the only one that worked. I was the only one that figured it out and it was like, but everyone passed anyway. I was like, come on. Anyway. Yeah. Yeah. So.

**Chris Gammell:** But you're not holding a grudge all these years later. That's the important thing. No, not, not, not holding a grudge.

**Dave Jones:** Anyway, that, that, that one sticks in my mind. Yeah. Right. It was like, and, and they wouldn't believe me. They wouldn't. Uh, yeah. I think the thing why it sticks in the mind is because they wouldn't believe me. They went, oh no, it's a fluke that yours is work. I, we, we don't know why yours is working. And it's like, no, I can tell you it's the fan out. And I tried to explain and they wouldn't believe me that fan out was a thing.

**Chris Gammell:** Who was they in this case? Was it, was it someone who was actually.

**Dave Jones:** Well, I can't remember if it, well, I can't remember if it was the, our actual lecture, our digital electronics lecturer, or whether or not it was like a, you know, a, like assistant, uh, you know, a, a, what, what's the name of the grad student or a teaching assistant. Like a grad said, teaching assistant, grad student or whatever, because it was just a lab. So it might've been just a teaching like, you know, but, but these are graduates, right? These are, you know, usually.

**Chris Gammell:** I don't know. Yes. I mean, I'm not saying they're not capable. I'm saying it's more of a, you know, if you're not writing it, you're just like, just do the lab, man.

**Dave Jones:** I'm just trying to make, I know it's just a, yeah, man, I'm going for a smoko afterwards. Just, just to finish the lab, man. Come on. It's like, I mean, they got, they got other things going on, you know, of course. Yeah. Yeah. Have to get to the uni bar, you know, that's right. That's right.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Oh boy. Anyway. Yep.

**Chris Gammell:** So Miller plateau, this is, this is a, uh, this is a thing that, uh, James, the bald engineer, uh, had, did a video about. It was pretty good. It was, uh, basically showing the, the effects of Miller capacitance. And basically when you don't have any, basically saying, Hey, throw a resistor on the input gate to a capacitor, a, uh, a, a fit, a fat. Yep. And, uh, and yeah, it's, it was interesting to see the actual traces and like, he actually shows the, how the traces change and what the, what the inputs look like as you change the resistance out. So it was a pretty neat, like pretty neat explanation. I guess I, you know, I, I've read about Miller capacitance and I've really looked at it, but I've never really seen it in practice because I usually do have either inline resistance from a PCB or there's actually a resistor there and stuff like that. Or I just.

**Dave Jones:** Most, most people. And it, and it really comes into its play in like power MOSFETs. And so unless you're doing like really power MOSFET-y, you know, big grunty driver type stuff, like motor drivers and stuff like that, you're probably not gonna, that's probably not going to come into play. So anyway, the Miller plateau is where you charge. I'm not big on it, but it's where you, you know, the, the gate charges up and it's at certain VGS like threshold levels that it, instead of continuing to ramp up, it actually plateaus out. The charge actually plateaus out something like that. So yeah, I'm, I'm totally butchering that. I'm totally butchering it. It's been, it's been a long time since I've looked at that. So yeah. And, and, and I haven't seen the video, so I'm sure if you watch the video, I'm sure it's all explained.

**Chris Gammell:** And, you know, the real problem is Dave, that you're spending all your time watching other stuff like Amazon prime movies.

**Dave Jones:** You had to bring this up. You said you'd bring this up at the start of the show. I don't know why.

**Chris Gammell:** I think it's because, well, so here's the thing. I, I catch it on Twitter because you're like, oh, I spotted an oscilloscope and like, that's kind of interesting. But then like, sometimes you post the videos, the movies that you're watching. I'm just like, what the hell is he watching? And I will say, I will tell you, I used to watch stuff like this. I used to go over to my buddy's house. He had, his dad had like a collection of like, like 1980s, like really terrible sci-fi, like like the worst grade stuff you could get, like plan, like plan B from outer space. But like times, you know, like he collected bad stuff. And so we used to go and watch that stuff. So I'm not, I'm not against it per se, but because you do it, you know, in public.

**Dave Jones:** I don't necessarily watch them all. Like, like I, I didn't watch that, like invasion from Mars, this Japanese invasion from Mars from 1970 that I tweeted the other day. I didn't actually watch that one.

**Chris Gammell:** There's some real bad ones out there, you know, like what got funded. I guess they're low budget anyway. So it's not.

**Dave Jones:** Oh, they're super low budget. I wonder how much it cost Amazon prime. Probably nothing like, you know, pennies on the dollar for.

**Chris Gammell:** Oh, I bet. I bet nothing at all. I bet, I bet it gets, I bet, I bet that gets thrown in, but basically it's like the throw away from the, you know, from like. Yeah. Studio.

**Dave Jones:** Because you sign up for studios, don't you? And then you get all the, I think something like that. And you just get all. So they paid the studio X amount and they got a thousand B grade.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Oh man. Just to say, oh yeah, we've got 10,000 titles on our streaming platform. And you go and actually watch. But there's so many now, so many streaming platforms. Like before, like when, you know, like what, five, seven years ago, it was Netflix and that was pretty much it.

**Chris Gammell:** So I saw, I saw an image the other day that, yeah, yes, that's correct. I mean, it was, it was not much. I saw a image the other day that said like, it showed like different streaming platforms and like their various costs. And it was like Netflix, 120 bucks a year, or, you know, Amazon prime 99 bucks a year. And I kept on going down the list. And then at the bottom, it had, it had Harvard $50,493 a year because it's like, because it's true, right? All of these schools is basically like your, this is really, really expensive streaming service, which is like kind of messed up. You know, I don't know. I think if we have students listening out there, I'm sure we do. I feel for you. I don't know what the hell I would do in your scenario. Man, it's just keep making stuff. That's the important thing. You know, that's like all you can do these days because it's.

**Dave Jones:** What situation are you talking about? You're talking about that everyone's doing it. Oh, it's like universities. You know, like I, yeah.

**Chris Gammell:** Like I, I wouldn't have, I would burn out, you know, like I would just end up watching TV all day instead. But like, if, if I was just, if I had to like, if I didn't have the in-person element of it, I would just.

**Dave Jones:** If you physically weren't there, you would. I just wouldn't lock in. I wouldn't. Yeah. Yeah, exactly. Yeah.

**Chris Gammell:** I'd be a slack ass. Yeah. I mean, like, I just. I'm okay now because I'm like in and into it. But like, when I was like, when I was younger and frustrated with a lot of things, like, you know, like not frustrated with a lot of, you know, like when I was learning, like learning is tough when you're, when you're on your own. It's like, it's a difficult thing.

**Dave Jones:** So this spills over to the gym. A lot of people ask, do I do weights like at the gym? No, I do classes because I, if I do, if I just wander in the gym on my own and, and try and do just free weights, I'm just going to be a slack ass, you know? Yep. Whereas if I'm in a class with 10, 20 other people, wow. I just go berserker. Right. It's a, you know, it's an interactive thing. It's like, you know, and, and it's almost a competition too. Yeah.

**Chris Gammell:** There's the competition aspect for sure. Yep. Yeah. It's just a tough time. I mean, I really, I just, I think I feel, especially for people that are getting started, like it's, I don't know. And like, there's so many things that people could learn too. Like that. It's like, there's like this, this like underlying guilt that people, like some people are just like depressed and, you know, it's tough to get anything done these days during, you know, lockdowns if people are still in that. And it's like, you know, I don't know. It's like, it's just a real tough time for, for learning. I think. Okay.

**Dave Jones:** Well, here you go. I didn't say this is not on the list, but I will send you the link to this. There's a, just came out the other day, big news story. It made all the rounds here. Almost half of Australian PhD students considering disengaging from studies due to the pandemic. Wow. This is like, yeah. They, they reckon 5% of PhD students in Australia are currently or about to experience homelessness and 11% are skipping meals. It's like, wow. I mean, yeah.

**Chris Gammell:** I mean, PhD students live on the edge anyway. It's just like such a low payment, you know, like.

**Dave Jones:** It is, but like most, like the, I don't know what it's like in the US, but here in Australia, the tradition is that you, when, when you study, you don't go to university study. We've talked about this many times. You like stay at home with your parents. That is, that's the way it's done. And like the parents are going to feed you and you don't have to worry about getting that second job, you know, to pay for your, you know, rent or whatever. Yeah. But the, the whole dorm thing is not a thing here in Australia. It's only for overseas students. So I find this remarkable.

**Chris Gammell:** Yeah. Is it, is it also the case for PhDs? Do you know? I mean, like, I don't know if you would have.

**Dave Jones:** Well, I assume, well, I don't know, you know, I've never done a PhD. I don't know about that sort of crowd, but.

**Chris Gammell:** I got a PhD in the school of hard knocks. School of hard knocks.

**Dave Jones:** Exactly. Word. Yeah. And I just, yeah. I, I find that really remarkable. These must be overseas students. There I, I, well, no, no, but overseas students, they'd probably have their parents paying them to come here usually. So I, I just find that remarkable because we have such a culture of, of staying at home and that, and that actually determines which university you go to here in Australia. It's like, well, which one's closest to home? Do they have a course I want? Yep. I'll go there.

**Chris Gammell:** That's the thing that I don't get about that whole system is like, what if it sucks?

**Dave Jones:** It doesn't matter. See, people don't get care here because, no, no. Unlike the U S it is not when you go into the job market, it's like, do you have a degree or not? It doesn't matter where you got it. It really, unlike the U S is much more tribal in that respect. Pedigree. Pedigree. Tribal. Well, yeah, here it's like, no, nobody, no one cares. It's, you know.

**Chris Gammell:** I mean, I guess I shouldn't really say that it matters anyways, because I'm kind of like, oh, you shouldn't, school doesn't matter that much. Right. Yeah. I, I guess, yeah. It's so ingrained in my brain, you know, while we've talked about that many times. So, huh. Well, I, I'm feeling bad for all the PhDs out there and I'm sure it's not just Australia either.

**Dave Jones:** So no, it could be, and maybe it's elsewhere as well, but yeah, I do. I just, I don't know if the article, how accurate the article is, you know, the guardian that's like, you know, I don't know, but, um, but yeah, that's, that's really remarkable. So please, if you're a PhD student, leave it in the comments down below. Like, do you know other students struggling to make ends meet?

**Chris Gammell:** Yeah. And I, so like some of it, I think like, you know, people can do amazing things at home and on their own as well. And like, I think I'd like to bring up some of the tools that are, are doing these kind of, that are like enabling these things. But like, like I said, it's still tough to do that. It's still tough to get motivated to actually go out and want to learn these things. But like, it is kind of amazing on the flip side, I suppose. It's kind of amazing what's now available. And so we're going to talk about more about this next week. So Tim Ansell is going to be on the show again next week. But one of the big stories is that Google is the new open source PDK. And then Google's offering free fabbing for 130 nanometer chips. So next week, we're going to talk to Tim about that. What did you think about this whole thing, Dave?

**Dave Jones:** Can we repeat that? Google is offering free semiconductor wafer fabbing for 130 nanometer technology. Free for open source chips. It has to be an open source chip.

**Chris Gammell:** Yep. Yep. And it's got to be on GitHub, I think, or, or GitHub, GitLab or whatever.

**Dave Jones:** Right. And so is this available to anyone? Do you have to be, I haven't looked into the details. Do you have to be like a university department? Like, do you have to be like in, like, no, you can just be in your.

**Chris Gammell:** You have to apply. And then you have to be. Oh, you've got to apply.

**Dave Jones:** Right. So it's not automatic. It's not like, hey, it's, you know, right.

**Chris Gammell:** Yep.

**Dave Jones:** So, and does it have to be substantial? Will they do, hey, I'm going to do an open source triple five wafer chip. And will they accept that or not?

**Chris Gammell:** You have to design it. I mean, I.

**Dave Jones:** Oh, yeah, of course. You've got to use the tools and they're offering the free tools. Right. Because the tools aren't normally free. Is that. The tools are free. I think this is. Tools are free. Right.

**Chris Gammell:** I think so. I think this is using electron. Like I said, we'll find out more next week. Tim will be on the show next week.

**Dave Jones:** Yeah. It's called the Skywater PDK, which is. Yep.

**Chris Gammell:** Which is the fab itself, the foundry rather. So Skywater foundry, the PDK is the process development kit. And so basically we've talked about this a little bit on the show in the past, not the open source nature of it. But basically once you get access to the PDK, that gives you like, oh, here are the standard cell transistors you have access to. And then, you know, you can start to tweak some parameters as far as I understand, at least.

**Dave Jones:** Again, so what software is. Does it come with the software to actually lay out the, you know, components or like, I just don't know. I've never designed a chip. Like I've never actually did the silicon level. I don't know the tools. Is there another tool that is this just like the library and you have to then use your silicon CAD tool of choice or.

**Chris Gammell:** Yeah. I think, I think that would probably be a good way to make an analogy. It's like, this would be like someone handing you a library of footprints and symbols. That's right. Yep. You have to plug it into a layout program. A layout program.

**Dave Jones:** Right.

**Chris Gammell:** That has all of the DRC checking and all the, you know, and it does have parallels as far as I understand it. There is an open source one called, I want to say Electron, but I don't know if that's right. Oh yeah. I think that. We've talked about one of them on the show before and it's real ugly and it, or it was real ugly. Last time I looked at it, it was all Java based and it was real ugly looking.

**Dave Jones:** Right.

**Chris Gammell:** But I think it's still alive. And I think, yeah. So I think that's one. And obviously then there's also like cadence, which is like, okay. Yeah.

**Dave Jones:** But who's got access to that? Who's got 50 grand sitting around. Yeah. Yeah. Exactly. Okay. 50, 50. It'd get you the bare bones. Well, it wouldn't even get you the bare bones, would it?

**Chris Gammell:** Yeah. Yeah. I don't know. I don't know. Yeah. It's like. But I think the PDK is like the plugin piece that then basically is like the footprint library.

**Dave Jones:** Think of it as the footprint and component library. Yeah. Yeah. Which has all the, you know, yes, here's a flip flop. Here's a, you know, here's a MOSFET. Here's a.

**Chris Gammell:** Yep. And here's a single transistor, honestly. I think that's some of it too.

**Dave Jones:** So, so what is this process node capable of? Is it capable of like analogy stuff? Like, is it capable of mixed signal or is it?

**Chris Gammell:** It is not. It is not right now.

**Chris Gammell:** It is not. So it's digital. Tim talks about that a little bit in the dial-up talk. So that's the linked video in there. Yeah. It is digital only right now. I think they're working on an analog solution. Okay. But I think. Right. I'm pretty sure it was no analog. There are, you know, you can have like inductors, capacitors, like all that kind of stuff, but.

**Dave Jones:** Right. But you really wouldn't need those in a digital design anyway. Really. Yeah. Pull ups and stuff like that. And, you know, other open drain outputs and, you know, inputs and things like that. Yeah. So could you take, like, if you had an existing VHDL design, could you just like import that, like, and compile that to your own custom silicon? Is that possible? Do you have to even use? Yeah.

**Chris Gammell:** No, you do have to. I mean, you need a, you need a tool for it. Right. You need some kind of like placement tool. Right. Let's say placement route does. Right. But I don't think, I don't think you would take like a VHDL or sorry, you wouldn't take like a placement file from like a FPGA tool and then be like, oh, I have a chip now. Right. Because.

**Dave Jones:** No, no, no, of course. But, but if you had your VHDL code, right. Could you import that into one of these layout tools? And then it pulled the libraries in that it needed. And, you know, and, and then mapped, you know, oh yeah, here's a shift register and it maps that in. Here's a flip flop. It maps that in. And then we just don't know. We have to use the tool.

**Chris Gammell:** Yeah. You lost me about, you bought it five minutes ago. Yeah. So next week we'll, we'll have all these, all this and more in episode 501. We'll be answering. Right. Yeah. Yeah. Fantastic. But it's interesting. I mean, like it's an interesting time at the very least. I mean, the fact that Google is doing this and the fact that it's, you know, it's driving open source forward, which is interesting. Yep. Someone, oh, who was it talking about it? But it was interesting, like comparing a Google versus an Apple, right? Both are talking about chip design, right? Apple now has, you know, and Google's done chip design as well, I believe, like internally, but like Apple's going like more closed, which is kind of on brand and Google's like,

**Dave Jones:** well, they're switching to arm, but they're doing their own variant. They're doing the design. Right. Exactly.

**Chris Gammell:** It's not like Apple was open ever, but I'm just saying that like, I forget who it was. They were comparing the two and it was interesting, like contrast. Right. So we like the open stuff here. That's great. So we'll see how that all goes. I mean, I don't know.

**Dave Jones:** Can I mention my prediction I put on Twitter here?

**Chris Gammell:** Sure.

**Dave Jones:** I made the prediction that Apple are going to buy a semiconductor company in the next couple of years.

**Chris Gammell:** Oh, interesting. Okay.

**Dave Jones:** That is my prediction because they need to vertically integrate more and Apple's all about profit margin, right? They've got $200 billion in cash sitting there, right? And they usually use this cash. The reason that Apple makes such great margins, they're such a profitable company, is that they use that cash that they've built up to buy, you know, 10 or 100 million processors, right? They have 100 million memory chips, right? They buy up years worth it. They buy up entire production lines worth of chips, right? So all these memory makers, they'll just be churning out chips for Apple because they're, you know, so they use it to get volume discounts, right? So the next logical move from that.

**Chris Gammell:** I think this is the opposite of logical. Well, why? Because why would you take on that risk then? I mean, like, basically, you're throwing your weight around. You got this huge club that you can, you know, hit people over the head with cash availability. And then you're like, maybe I should hit myself over the head. You know, I don't know. Like, chip fab suck, man.

**Dave Jones:** Yeah, but the chip fab keeps running. So I'm not talking about them starting up their own chip fab from scratch. I'm talking about buying an interesting player. And because they, and let them run it, continue to run it how they would. But they get, they don't have to pay any margin on top. So it's, you know, Apple's all about margin, right? So they would get the chips cheaper than everyone else because they own the company.

**Chris Gammell:** So you're saying cheap as chips, cheap as chips.

**Dave Jones:** Cheap as chips. Anyway, that's, I would not be surprised if that's happened. I like, you know.

**Chris Gammell:** Okay. It's interesting. I mean, it's an interesting idea. I probably wouldn't bet money on it.

**Dave Jones:** It's very wonky. But it's not wonky. It's like, you know, it'd be a big, it'd be a huge play. No, no, no. Not wonky is bad.

**Chris Gammell:** I mean, it's like, you're like a wonk. Right. You know, like, this is a wonkish opinion.

**Dave Jones:** No, I don't know that too.

**Chris Gammell:** Like a political wonk is someone who like basically analyzes the political spectrum. And then, yeah, it's like a, yeah, wonky is like a, is usually like a negative connotation. But to be like wonkish or to be a wonk is to, you know, someone who like analyzes.

**Dave Jones:** I haven't heard wonk before. I've just heard wonky. You know, it's like. Yeah, yeah.

**Chris Gammell:** That is a negative connotation.

**Dave Jones:** Like it's going to fall apart. It's wonky.

**Chris Gammell:** Right.

**Dave Jones:** So interesting. Okay. Anyway, so that may or may not come true. So if it comes true, damn it. I'm going to say I called it. And if it doesn't come true, I'll do everyone. I'll just forget about it. So the great benefit of making predictions. Who was that?

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Nobody ever looks back and, you know, oh, your prediction was shit. So, yeah. Yeah. Anyway. Yeah. I just think it seems to make sense because Apple's all about screwing those margins. So, yeah. Anyway, that'll be interesting if it happens.

**Chris Gammell:** Yeah. Hmm. What else we got? I'm looking through this thing now. Let's see.

**Dave Jones:** Such professionals here on our 500th episode. Oh, talking about the open source thing. We can segue into the open source thing. There's like what a new DIN standard for open source docu. I don't get this. I downloaded the zip file. I don't either. Okay. It's open source hardware requirements for technical documentation. It's been released. It's the DIN spec 3105 for those playing log at home. And I downloaded the zip file of the, you know, that was posted on Twitter by who posted on Twitter. I can't remember. Sorry.

**Chris Gammell:** Jeremy Bonvoison. Okay.

**Dave Jones:** Good on you, Jeremy. And I downloaded it. And it's got like, well, there's the hardware symbol. And there's this .md file. What's a .md file?

**Chris Gammell:** That is a, that's a documentation file in Git. In Git. Right. So if you have a .md, it'll show as the first, that's like the cover page. So usually it's readme.md.

**Dave Jones:** Okay. So it's just a text file, is it?

**Chris Gammell:** Yep. Yeah. It's like a markdown. That's what it is. .md is markdown. Sorry.

**Dave Jones:** Oh, markdown language. Right. Got it. Got it. Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Yeah. Yeah. Okay. Right. I need to extract this right about now and stick with me for a minute. I'll get it. Yeah. And.

**Chris Gammell:** Well, while you're doing that, it took me a long time to find out that DIN is German coming. Deutsch. Deutsch Institute for Normung. Normung. Sorry. Something like that. I'm sorry. I'm so sorry. But that's what I never knew. So I always knew the term DIN rail, but I didn't realize it's actually a standard that comes from a standards body in Germany. And that's what DIN is. Yes.

**Dave Jones:** And a DIN connector. And, you know, yeah.

**Chris Gammell:** What's a DIN connector? I don't know what that is.

**Dave Jones:** A DIN connector. The five pin DIN connector. You know, the old keyboard connector from, you know, old school PS2. Oh. You know, old PC keyboard. That's a DIN connector.

**Chris Gammell:** Yeah, PS2 would have. I didn't know that.

**Dave Jones:** No, not. Yeah. PS2 is a mini DIN or whatever. Yeah. It's a, no, a DIN connector is your traditional, you know, circular plug. Circular plug.

**Chris Gammell:** It almost looks like a MIDI, like MIDI connection.

**Dave Jones:** It's a MIDI connector is a DIN connector. Yeah. Oh, it is. I think. Yeah. Yeah.

**Chris Gammell:** So it's basically like the outer. So it's got like a circular outer shell and then like. Yes.

**Dave Jones:** And multiple pins in there. Yeah. That's the DIN standard.

**Chris Gammell:** I think this might've been pre, pre-Chris.

**Dave Jones:** Okay. Right. Pre-Chris. Yeah. This was like, yeah. This is like 70s era connectors.

**Chris Gammell:** Chris was too either not existent or too young to. Be allowed to unplug things.

**Dave Jones:** Basically. If you look at every vintage PC from the seventies and probably up to the mid eighties and DIN connectors were the thing. They're there with your keyboards plugged into serial. You'd even get a serial DIN, DIN connector, you know, none of this D9 rubbish. It was, you know, a D, D25. It was. Yeah. Right. Right.

**Chris Gammell:** It was something that could make, make a, make a DB9 look small.

**Dave Jones:** Yeah. Yeah. Exactly. It was, you know, yeah, that was the thing.

**Chris Gammell:** I'm not sure if that's going to hold on. Let's get a little bit more steel on that, you know? Oh, they, DIN 476 is international paper sizes. Wow. They really do a lot of stuff. Oh yeah. That's gotta be, that's gotta be a tight ship. Can you imagine working at a German Institute office? Oh my goodness.

**Dave Jones:** German standards Institute. Oh boy.

**Chris Gammell:** Yeah. I just.

**Dave Jones:** Sorry to all you Germans out there, but we're, we're stereotyping.

**Chris Gammell:** Yeah. We love you. It's like, it's just like, that must be intense. It's not bad. It's just intense.

**Dave Jones:** You know, but I'm sure, I'm sure it actually produces the finest standards out there. I'm sure it does.

**Chris Gammell:** And like, like, so the A series, so DIN 476 is the A series paper sizes, which the U.S. still hasn't adopted, which is stupid, but you know, we still have letter and tabloid.

**Dave Jones:** Oh, that's so retarded. Yeah. Yeah.

**Chris Gammell:** It's not great. It's, you know, eight and a half by 11 though. You know, that's, that's, you know, Yankee units.

**Dave Jones:** Eight and a half by 11. Yeah. What inches? Come on. This is ridiculous. That's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Get with the program. It's just low. And I like, A's are perfect. Like, I, like an A1 is half the size of an A0 and A2 is half the size of an A1.

**Chris Gammell:** I mean, let's just start at metric, Dave. Come on. Let's get that.

**Dave Jones:** Small steps.

**Chris Gammell:** I think we have lots of things we could point to that are a little, little off around, around these parts. So, uh, anyways, uh, you were, you were saying, so, okay. So I think the thing is, I think the reason that this is interesting from a high level is that it's, you know, a German standards body and now it's open source though. Like, so like people can contribute to it.

**Dave Jones:** Yeah. Like, okay. I'm reading it and I do not know what I'm reading. I'm like, I, I seriously, I have no idea what this is trying to do.

**Chris Gammell:** Um, this repository holds open standards in the field of open source hardware. And unambiguous reference to the corresponding documentation. I think this is basically trying to make, you know, so like there's, there's open source hardware summit group, Oshawa. They also have, you know, standards and stuff like that. They've got their own. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** And so I think this is trying to standardize in that same way, but through DIN.

**Dave Jones:** Right. Yeah. It's just like you read it and you got, I like, you just go, what?

**Chris Gammell:** So here we go. DIN spec 3501-2 defines requirements for implementing a community-based certification procedure for open source hardware. Okay. That's cool. DIN spec 3501-1 delivers an unambiguous and operational definition of concept of open source hardware and breaks it into objective criteria for judging the compliance of a piece of hardware with this definition. So basically, yeah, this is just another way to say, is it, or is it not open source hardware? If it is, here's how we certify it, I guess.

**Dave Jones:** Yeah.

**Chris Gammell:** I guess what happens though, if you like, can you like fork, can you fork a DIN spec now? That's kind of interesting.

**Dave Jones:** I don't know. But like, it's just so wordy and weird. And it's like, well, like seriously, people have to go check this out for themselves. Cause it's quite, I, I, like I've got to sit down and actually concert, like you really have to concentrate to read this. It's not something I can do while talking at the same time. My brain just doesn't have the bandwidth to do it. Yeah.

**Chris Gammell:** I think, so I think someone brought this, I think when I was in Germany for chaos camp, I think someone brought this up. I remember hearing about this at some point and it was like in process. And I'm sorry if that person's listening and they were telling me and they're like, Chris is going to remember exactly what I'm saying. I did not remember. Yeah. So yeah, it's okay. Well, we'll see, you know, like we'll see. I think it's just like any other open source, whatever open source hardware. It's like, you know, it's only, there's always a lot of like struggle around it. You know, like a lot of like, like people want to get it right. They want to make it standardized. And that's what a standard is. Right. It's like a state, you know, it has a set of definitions and people agree to it. And it's like community certified, blah, blah, blah, blah, blah. You know, like kind of like now that it's there, I kind of forget about it. So like, that's just my personal, like it is important, but it's just like, I've just kind of forgotten about it. And now this is a new one. And I'm sure once it's standardized, I'll be like, Oh, okay. I've forgotten about it.

**Dave Jones:** But as with open source hardware, most people just shrug their shoulders and just don't care. They'll just do whatever they want. You know, it's just like, man, you know, I just throw some random license on it. It's great that people are doing it. Yeah. Yeah. I'm great. It's great that people are doing it.

**Chris Gammell:** And I feel like there's always these things. Like I see this with some of the software podcasts I listen to. And like, and like, sometimes I see this in the, in like the, uh, firmware projects and our software projects that I follow. So there are some very real implications. I never run into them because it's not like I'm not doing big enough software projects that it matters. But like, I can imagine a scenario where it's like, you know, some of the licenses are like, no, if you have this piece of code in your software, the rest of your software is open source. And it's like, it's like, oh my God, that's a huge deal.

**Dave Jones:** You know, that could be a legal minefield for company. And it is like, there's been lawsuits about this sort of stuff, you know? Right. And so I'm just grateful I don't have to deal with it.

**Chris Gammell:** You know, that's, that's what it comes down to.

**Dave Jones:** Yeah. I, I tried to do my own little, I wasn't a standard, but I tried to come up with a new concept. Yeah.

**Chris Gammell:** You had the seven, the seven thingies. What is, what has to be open about it?

**Dave Jones:** Yep. And the creative commons, it was kind of making open hardware, sort of like the creative commons letters, you know, to have it, you know, like the CC BY, you know? Yeah. Yeah. That sort of thing. The same thing for open hardware. And there's quite a few people who have taken that up and actually continue to take that up. They actually put the little letters on their logo and stuff like that. Do I still think it's an excellent idea? Because at a glance, you can tell from the logo what people have given away.

**Chris Gammell:** Do you think your own idea is excellent? Yep. Damn right I do. This is, this is very surprising.

**Dave Jones:** It solves a real problem. Right? It does. You know, the standards are one thing. Standards are one thing. Okay. And then you have real world problems.

**Chris Gammell:** No, no, come on. Iconography. That's what you're talking about. You're talking about iconography.

**Dave Jones:** Yeah. There are real world problems that people need to solve. I have no doubt about it. And one of those is what people are actually releasing and making open. It's like, yeah, they will stick the logo on it.

**Chris Gammell:** Here's where Dave gets his PhD. This is where Dave goes back and he gets his PhD in this thing. Whatever it is. And he just, he just goes to conferences and argues with people for the rest of his frigging life. Dr. Jones. Yeah.

**Dave Jones:** If there's a problem, I'm an engineer. Sue me. If there's a problem out there, I want to solve it. One of the problems is people trying, people, you can't tell what they've actually released. Right. It's like, well, how, how open is it? I've been waiting to say this.

**Chris Gammell:** I've been waiting to say this for years, Dave. I'm going to say it right here. Okie dokie, Dr. Jones.

**Dave Jones:** Oh boy. Anyway. Yeah. So it's a serious problem at which none of the other parties want to address. Quite frankly, they, they, they have the purest approach. Everything must be, you know, it must be completely open or, or, or bust or go away. You're not allowed to have your hardware certification number. Right. And it's like, yep. Yep.

**Chris Gammell:** Yeah. Yep. Okay.

**Dave Jones:** No. Okay. You don't have to agree, but either.

**Chris Gammell:** No, it's, no, it's, it's not, it's not that I, I, Dave, I, I'm not saying that your thing doesn't solve a problem. I'm not saying that, you know, there's a need for all this stuff. It's just like, literally this doesn't, I don't know. Like this is not a hill. This is not a hill I'm willing to die on. I guess that's what it really comes down to. And like, and like you're saying though, some people are right. And some people are like, this fits this criteria and this does not. And the one that does not, does not allow it in our club. And you should not do this and this and this and this, and we're willing to take legal action. And at the end of the day, that's what really matters, right? Is like people are, are not willing to take legal action to do all this other stuff. And it's like, all right, that's when I usually throw my hands up and I'm like, this is not for me. So I love open source hardware. I love people that do it. I think it's an interesting concept because it does add on to stuff. One like more practical high level view I've taken on open source hardware in general is that it's not the most interesting hardware that's usually being open source. There is a lot of interesting open source hardware, but like the most interesting stuff is just not going to be open sourced. And so like, I like it when it's out there and there's, and like, if you look at like, if you looked at like a heat map of like open source hardware and like what's in open source hardware, I would estimate a guess. And I could be very wrong at this, that the, the heat map would be very strong around an eight, the at mega 328. And like that alone is like, all right, well, you know, cool. Like, that's great. It's out there, but like, that's less interesting to me. And so again, I'm glad it's out there. I think that's good for learning. I love that there's open information. I love looking at the schematics, but a lot of the schematics I've looked at have had a lot of at mega 328s and that's less interesting to me these days. So that's all I'm saying.

**Dave Jones:** Right.

**Chris Gammell:** As a result, I am not willing to die on that hill because, okay, 328s.

**Dave Jones:** It's not a hill anyone need die on. It's just a hill that needs to be there. You know, it's a hill that a lot of people want to stand on.

**Chris Gammell:** Sure. That's true.

**Dave Jones:** Not fight, you know, and why fight? It's like, well, you know, there's a lot of people who want to do open source hardware, the purest way. And there's others that want to have more practical oriented open, you know, they want to share some stuff, but they don't want to share all. And there's some very good reasons for that. Right. So, you know, and there's no need for the two camps to even fight at all.

**Chris Gammell:** Okay.

**Dave Jones:** So, yeah, no, it's not a hill that you have to die on.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Chips that I'm not seeing on many open source hardware designs, what are interesting because they're not on any open source hardware designs, mostly yet because this chip just came out is the ESP 32 S2. Have you seen this thing? No, it's... How was that first segue? Was that okay? Right. Yeah, that's fine.

**Dave Jones:** Yeah. But it's like, yeah, okay. Grown. It's yet another thing. What's so special about it?

**Chris Gammell:** So the interesting thing is that it's, it was a downgrade of sorts. I talked to Yerun about this, Sprite TM. He basically, he is one of the firmware, software, hardware guys there. You know, he's the wizard there. One of the wizards there at Espressif. And basically they looked at the market. They looked at the part they had out there. It was, you know, the ESP 32 is a dual core power hungry beast with a ULP, the ultra low power, power processor on it. So basically it's just a beast. It sucks down power, but it can do a lot of interesting things. This one is not dual core. So that's kind of interesting. So it's, that's how it's kind of a downgrade in my opinion, because now you're not running on a second core. You're basically sharing time on the core. That's running the wifi stack. It also has two low power processors in it. Now, one of them is a risk five. That's also interesting to me. What else do I remember from this Andrea Spies video that will, we'll be linking in here. It, Oh, that's the other one. It has a USB hub, not hub, a USB. Help me out here, Dave. What's it called when a USB, when you can just hook a USB with two lines into a chip, not a show. It's a, not a five. It's a, I'm thinking out loud here. Hey, I mean, it is USB host, but it's a, no, it's not a USB host. It's a USB device, but it is the physical stuff you need for USB. Basically just like on other parts where you can just hook up D plus D minus right into the chip. Sure. It has it now. Well, yeah. Okay. USB 32 didn't have that. And so you needed, you needed another chip. So basically now, I got it. Okay. Now you can just drop this, this chip with a USB connector and be ready to go.

**Dave Jones:** It's got a USB hardware core in it. And yeah.

**Chris Gammell:** Yes. Yes. And so, yeah, all those things are interesting, you know, still low power, still, or still a low cost rather. I haven't used it yet, but I think it's an interesting, I think the most interesting thing about it to me is the fact that it went from two cores to one.

**Dave Jones:** Okay.

**Chris Gammell:** And you know, of sorts, right. Of the actual accessible, normal cores that you're going to use. So yeah, we'll see. We'll see how it goes. It's a chips, you know, new chips out there. Yeah. Speaking of chips, former guest of the show, Sam's aloof showed off how he does a photo lithography at home using his projector and does photo lithography using that. That is also very worth using. So talking about, I guess we were talking about resources for building stuff at home. You're looking at the Google PDK and you're like, oh, that's, that's too easy if they just give me answers. So now I should really build my own chips. You could follow the same steps and you can, you can do that at home now too. So, yep. That's another one.

**Dave Jones:** Very cool. I think he's pretty much got that market to himself. I think. Yeah. There's not too many people willing to set up a chip fab in there. Even,

**Chris Gammell:** even Jerry Ellsworth has moved on to greener pastures. Yeah,

**Dave Jones:** exactly. Yeah.

**Chris Gammell:** Yeah. Sam posted the thing on Twitter the other day where he was, he was actually playing a guitar pedal that he. Yes. I saw that. The chip to himself. That was, that was very fun. Yeah. It was very fun.

**Dave Jones:** I like, seriously, like, is he the only one in the world? Really? Like the only like amateur chip maker in the world? Like there's how many.

**Chris Gammell:** Surely there's others, but they're probably not making YouTube videos about it.

**Dave Jones:** No, probably not making. Yeah. They're not hoping.

**Chris Gammell:** I bet there's a lot more after him, you know, like that's, that's kind of interesting. So yeah. Sam, if you're listening, keep going, keep going.

**Dave Jones:** It's still certain. The problem with it is that it's just such a high entry burden. It's just like, it's massive. You've got to have, most people don't even have the space, let alone the ability. Like he's, he's in the U S right. He can get a lot of this gear, right? Me in Australia. Good luck. Right. Even if I wanted to, even if I had the, you know, I've got, maybe I've got the space. You've got the space. Yeah. But you know, like, like I could not get the gear to do it. It'd be so prohibitive. I'd have to import it all from the U S.

**Chris Gammell:** You should do that. Come on, man. What are you even doing here? What are you even doing here? Get on it, Dave.

**Dave Jones:** Yeah. Anyway, that stuff's much more readily available in there. You know, there's all, all sorts of chip fabs closing down and you can get, you know, like old chip fabs and things like that. And you just, at the auction sites, you just get all this gear and yeah,

**Chris Gammell:** I was watching, it was a very promo video. I think it was Kemet. You know, we talk about trade on here and the trade situation has not, has not been getting better. There's a Steve blank episode or a post about the chip wars of 21st century. He's a technologist writer guy. He writes about startups a lot, but he's, you know, writing about this stuff. Right. But anyways, I was thinking about like, okay, so right now, if you wanted to like build a capacitor factory in the U S, what would that take? And then I saw like a Kemet.

**Dave Jones:** Right.

**Chris Gammell:** There's like an actually like how they're made. Like it was like a promo video or something like that. Oh, excellent. Got to see it. Yeah. Oh my God. No, I will not be starting a capacitor factory.

**Dave Jones:** You know, like,

**Chris Gammell:** and it, because like they do like a hundred percent test, like, holy shit. Can you imagine like a hundred percent test on like. Yeah. Oh, one, oh, oh, five capacitors and stuff like that.

**Dave Jones:** Like you have to, because the tolerances are so ridiculously small that the, a production variation, what you, you know, fart halfway across the factory, it's going to change the process, you know? Yeah. It's like, oh yeah. And then you can get a huge number of foes if you're not, of course, you're going to keep on top of that. Yeah.

**Chris Gammell:** You know, and then, you know, schlubs like us were like, oh my God, this, you know, they said it was 7% accurate, but we saw it was seven and a half.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** I mean, caps have like five, 10% tolerance for a reason. Yeah. Yeah.

**Chris Gammell:** Right. Right. Right. Yeah. Yeah. I mean, with resistors, you're just chopping some off, right? It's just like, okay, you get material, you know, mix it up, chop it off, you know, put in there.

**Dave Jones:** Multi-layer ceramic capacitors.

**Chris Gammell:** I don't think I could start a resistor factor. Where the hell do you even start? You know, like you think about like all this conversation about like, okay, so there are some very, very big trade issues and I think they're going to get worse. And yeah, we could talk about that all day long, but let's just say, yes, they are going to get worse. Yes. We, you know, different countries need to have their own resources to do this thing. Where the hell do you start? I could maybe come up with an idea of like, at least with a semiconductor factory, you're like, ah, yeah, I guess, you know, you go buy old stuff. You start from there. Right. And it's like, you could basically go to a, you know, a tell or a, uh, uh, who are the other ship machine makers folks? I don't know. I remember Tokyo electron. I don't, I don't remember. I used to work in this industry, Dave. You could go and get a catalog from one of those though applied materials. God damn it. Got it. Applied materials or tell or whoever. And you could just go buy a, you know, a bunch of machines. Where do you even start with resistors? You know, it's just like, is there like a resistor, like a raw resistor factory? You know, it's just like a catalog of just like, yeah, I need a truck full of resistant material, please. You know,

**Dave Jones:** we have no idea.

**Chris Gammell:** We just like literally every single day. I have no idea how this stuff works, Dave. Yeah. 500 episodes in, this is what I've learned. I have no idea how anything works.

**Dave Jones:** I have no idea how a resistor works.

**Chris Gammell:** I mean, I know that like there's a formula.

**Dave Jones:** Right. It's called Ohm's law. And yeah,

**Chris Gammell:** I guess the first step would be like higher material scientists. That's probably the best first step. You guys know what you're doing, right? Physics and how electrons move. And my goodness, we are dumb. Yeah. Yeah. You know, the thing that I love about electronics, so there is so much shit to learn. I have, I have some, I just got some, I have some, I got some new boards and I got some filters. I got some RF filters in, I got an RF amplifier and it's under like, so I got an RF amplifier. It goes 10 megahertz to eight gigahertz. Right. And it does like 20 DB gain, maybe no 10 DB gain. And okay, cool. I bought it on Tindy works. Great. Looks awesome. It's under a little metal shield. Right. And I'm like thinking about it. I'm like, what the hell is under that shield? I have no idea. How would you amplify that? Is it an op amp? I don't know. I'm going to have to rip this guy name. I'm going to break this thing now because I'm going to have to go rip the shield off, you know, because I'm gonna have to look at this. I don't know. I don't know how to amplify this many, like that, that wider frequencies. And even if I did, I'll tell you exactly what's in it.

**Dave Jones:** If you open it up, there is a transistor,

**Chris Gammell:** right?

**Dave Jones:** No, it'll, it'll, it'll be a, it'll be a most likely a circular plastic package with four pins on it. There'll be power ground. There'll be input and output pin. And they usually fit, sit flat on the board. You know, you often have to do a circular cut out there. I can't remember the name of the package. Right.

**Chris Gammell:** Right. And,

**Dave Jones:** and it's, yeah. And you feed in the power via an inductor.

**Chris Gammell:** Right. That's, that's typically,

**Dave Jones:** you know, because that's, they're designed for masthead amplifiers and stuff like that.

**Chris Gammell:** Like the high frequency. Yep. Yep.

**Dave Jones:** Like the high frequencies and, you know, passes the DC, but doesn't let the RF through. And, and Bob's your uncle. That's it.

**Chris Gammell:** I just feel like, I just feel like when this kind of stuff happens, chip in there after this, you know, like talking about the chip, whatever the hell's in there. And then like, you know, all of this stuff, like, like having a Ming on the show last week too, like so much in electronics and technology too. I'm just like, man, it's, we're like in a cargo cult, you know, like we pay someone money, these little bits of sand show up at our doorstep in little packets. Right. We get upset about how our pick and play, our magic robot doesn't work. Right. There's a video about what's his name. Oh, the charm. Yes. There's a shit robot. It's a bad robot. Right. Yeah. Yeah. Yeah. Yeah. It's yeah. And it's, you know, it's a cargo, we live in a cargo cult. That's what it is, Dave. Right. But it is a wonderful cargo cult. And I, I really enjoy it a lot of times. Sometimes I hate it.

**Dave Jones:** And given that this is the 500th episode, I have to bring it up. Cause back right at the start, you said, Oh yeah, we'll be making these chips with our own chip printer. You knew I was going to bring it up.

**Chris Gammell:** I knew you did. You know, I knew, you know, I knew you were going to bring it up because you said, sometimes people make predictions and it's the best. If you forget them, it's the best. If they forget that, I was thinking in my head, you know, who doesn't, you know, who doesn't forget a prediction that I made. It's Dave, David L Jones. That is, that is the man.

**Dave Jones:** I've got a memory. You're like an elephant. Yep.

**Chris Gammell:** Yeah. That's great. Thanks Dave. Okay. So 10 years later, we're here. I don't remember what the bet was, but double or nothing.

**Dave Jones:** You said 10 years. You said there would be, there would be a chip printer in 10 years. I said, you won't even get it in 20. That's BS. And I still stand behind that. You still won't have one in 20 years time. I'll make, I'll make the call again. You will not have a desktop chip printer.

**Chris Gammell:** Double or nothing. Double or nothing. Here's the thing. Ming was on the show last week and I'd say that counts. What? So basically it's putting silicon onto other silicon and then you can do it via an interface. So it's basically like you're, you're printing a new chip by, I'm just talking on my ass. I don't know. So basically last week, I'm sure you haven't listened to the show yet. Last week, Ming. No, I haven't. Zhang was on the show and he was talking about Z glue. And basically it's basically doing chiplets and then they go on a substrate. And then basically you design the substrate and then they have a tool that lets you make a package out of that. That is interesting. And that's, I'm just going to say that's, that's what I had in mind.

**Dave Jones:** It's interesting. But yeah, the elephant in the room is DigiKey and Mouser who have a couple of hundred thousand off the shelf chips fully qualified in multiple packages that cost cents each. And you think that somebody's going to come up with the chip. It's ridiculous. It's the dumbest idea in history. It's not going to happen.

**Chris Gammell:** That is not the dumbest idea in history. And you know,

**Dave Jones:** you've worked in the chip. It is. No, it's not a dumb idea. It's great. It's not practical.

**Chris Gammell:** You watch, you watch the dumbest idea in history every Saturday, whenever you watch these Amazon prime movies. So let's just get that straight. It is not the dumbest idea in history.

**Dave Jones:** Most impractical idea in industry. It's in history. It's not going to work.

**Chris Gammell:** I would say,

**Dave Jones:** you know, you've worked in the, you know, what goes into making a qualified chip.

**Chris Gammell:** It is increasingly unlikely that we will get it on our desktop. However, think of the other things we've talked about in this episode, open source PDK. So people have access to chips factories. Yeah. So. Fine. Yeah, of course. There's more of that.

**Dave Jones:** Okay.

**Chris Gammell:** Dave, I'm grasping at straws here. Give me a little five, 500 frigging episodes later. Give me a little, a little wiggle room here.

**Dave Jones:** No, none. You've already said it to yourself. It's acetone. The odds of a chip printer are acetone towards zero. It was already there 10 years ago. You just, no, you just want to hold out. So I'm going to, no, I'm going to rub it in. I'm going to continue to rub it in. I'm not going to give you an inch.

**Chris Gammell:** No. All right. That's fine. But you know what? Here's the thing. Here's the thing. If we hit, if we hit a third of your mark by then, who knows? Who knows, Dave?

**Dave Jones:** No, still cool.

**Chris Gammell:** Here's the other thing. Okay. So let's talk a little sci-fi stuff. People like click and end of episode. Some practical realities, right? So like we're hopefully moving towards being a, you know, multi-planetary species, you know,

**Dave Jones:** Mr. crazy,

**Chris Gammell:** crazy man. Elon Musk is, you know, being crazy, very increasingly crazy. But I think it is likely that, you know, we're going to go back to the moon at some point, Mars and whatever. Okay. So now maybe people are, hanging out around Mars. Let's say a hundred years from now, they're hanging out around Mars. They're maybe not living on Mars, but like, do you have to ship chips there? Like,

**Dave Jones:** yes. Yes. That's the whole point. You got to ship everything there. This is why a Mars colony is not going to work. I've done a video on this. It is because people don't realize that every, just the basic stuff.

**Chris Gammell:** Sci-fi books really gloss over that. Like, so I love the book Seven Eves. I've talked about it many times. They actually, so Stevenson does talk about it.

**Dave Jones:** I've been meaning to read that. Yeah.

**Chris Gammell:** Yeah. Yeah. I think I've been talking about that for about five out of the 10 years here. Yeah. He does talk about it. He talks about like, he does talk about like, like the, the main character, she basically has like a store of chips and she like stores them inside, like a metal asteroid that they're hanging out on that. She has like a little compartment in there to like radiation shielding. That part is fantastic. But then like, then somehow a, you know, culture springs up later. And it's like, okay, well, you know, okay.

**Dave Jones:** Well, the whole chip printer thing, I used to love this series. I can't remember what it was called, but it was where they went back into the time. And there were dinosaurs like, and they went like, and they set up a colony back in land of the lost.

**Chris Gammell:** It's like, you want to watch some bad movies slash TV land of the lost is it?

**Dave Jones:** Right. They had a chip printer. They famously had a chip printer because they took a, you know, because they have to repair stuff back in there. So they could, they had this chip printer that they could chip print replacement chips to keep all this stuff going. And people don't realize a, a Mars colony. It requires people don't appreciate, appreciate the massive, not only the manufacturing infrastructure, but the logistics infrastructure and everything else that goes into just making the bare necessities to keep you alive, let alone all your fancy stuff, like your bloody iPhones. Right. People don't realize you can't replicate that on Mars. Everything still will still have to come from earth. You can't do it. You can't do it. You can't get a self-sustaining colony on Mars. It's not possible. They'll just die out without replacements from earth. Simple as that. And it's going, that's going to be the same. That's going to be like that for hundreds of years. Hundreds. And like, you know, you have to so massively terraform it that then you can produce all the same, even the basic necessities here. People take their clothes for granted. You know, my, you know, how much effort goes into producing clothes, you know, how much infrastructure that goes into producing just the basic stuff. Right. Unless you want to walk around, you know, naked and, and with just your farming and just eating your Mars. No, roam around naked, eating your, eating your, you know, growing your beans. You've grown in your greenhouse or whatever. And that's it. Your crap potatoes.

**Chris Gammell:** Your crap potatoes. Yeah.

**Dave Jones:** Yeah. Exactly. And that's it. I mean, it's just, it's just ludicrous. People aren't practical enough. They don't think about the practicalities of it.

**Chris Gammell:** Well, Dave, we have to drive towards that.

**Dave Jones:** I think anyway,

**Chris Gammell:** I think there's some,

**Dave Jones:** of course we have to drive towards it. I'm not, you know, I'm not saying don't, I'm not saying don't do it. I'm not saying we will probably be on Mars in the next 20 years. I'm not saying we won't, we definitely will. But, you know, I mean, you're just saying they're going to,

**Chris Gammell:** they're going to pack, they're going to pack a lunch. You're saying they're going to bring a picnic.

**Dave Jones:** Yeah. Yeah. It's no, they cannot survive without replenishments from here. It's just not going to happen. So unfortunately I would love, like I'm huge. Like you won't get a bigger space buff than me. Right. Who wants to, you know, I want to believe in the Mars colony. A moon colony will happen before a Mars colony happens because it's so close. We can just get, you know, send freight up there in a couple of days. Right. It's easy.

**Chris Gammell:** Yeah. Yeah. Yeah. Yep. Yep. Well, calm down now. That was, that was a bit of a downer.

**Dave Jones:** What?

**Chris Gammell:** A bit of a downer, Dave.

**Dave Jones:** I'm sorry. I'm a practical engineer. I like, sue me. This is an engineering podcast. It's like practicalities matter. You know, like this isn't fantasy podcast.

**Chris Gammell:** Yes. I know. Hey, look, I will start a fantasy podcast in a second. I will talk about sci-fi all day long. I'll listen to it. Yeah. Go for it. The Baba verse. Read the Baba verse. I love it. The Baba verse.

**Dave Jones:** What's the, what's the Baba verse?

**Chris Gammell:** It's I've told, I've talked about the Baba verse on here before. It's a three book series. It's about a guy that dies in like the first chapter. And then, but his brain, thanks for the spoiler. An AI in the future, basically. And then he kind of goes to like, so basically because he's an AI or he's like a, his brain is like captured in a computer. He can replicate himself. And then he goes and takes over the stars. It's awesome. It's a great book. It's a great three books. I love it. Go read it. Listen to it. It's actually even better as an audio book. Okay. Great book. Great book. Great set of books.

**Dave Jones:** I can't read it at the moment.

**Chris Gammell:** My, my Kindle's dead. Well, yeah, you should listen to them, Dave. Listen to books.

**Dave Jones:** Okay.

**Chris Gammell:** Just especially people listen to this thing. If you like podcasts, you're going to love audio books.

**Dave Jones:** Yep. Agreed. Yeah. I do enjoy audio books. I prefer it when it's spoken by the author though. Yeah.

**Chris Gammell:** Yeah. Sometimes. Not always.

**Dave Jones:** Yeah. Not always. Some authors suck, you know? Yeah.

**Chris Gammell:** I think like nonfiction for sure, but like fiction. No, I want like a voice actor.

**Dave Jones:** All right.

**Chris Gammell:** I talked about on here. I think it was with a guest or maybe it was when just a guest co-host or something, but the idea of like having podcasts where like you read technical papers, like having like audio based, like technical, like not like, not like, not like abstract, you know, see figure 1.4. 4.8, but like, but like actual, like, you know, technical, I don't know. It was like based off the idea of like autumn, which is, uh, uh, I don't think I heard back from anyone about it. I like mentioned it on here. No one said anything. They're interested about it. So I, I kind of dropped it, but I still like that idea of like listening to technical content and like being able to like capture, you know, somewhat complex. It's really going to be pointers towards complex content because I don't think that it's possible to really dig in deep, you know, like I said,

**Dave Jones:** no, but, but, but you need like a summary. You need like a, like if you reckon there's a niche out there for a podcast of like a summary of, well, I kind of watch a guy on YouTube and Anton, uh, Petrov, what the math it's called, what, what the math anyways channels called Anton Petrov. And he basically does that. Like every day he releases like a, a space science related video where he just talks about like a latest, you know, research paper that's been released, but he animates it.

**Chris Gammell:** You fell into Saturn. That's cool.

**Dave Jones:** Yeah. Yeah. Yeah. Like, you know, there's like, and, but, but they're all based every episode is like usually based on like recent research and he links to the publication. So if you want to go read the publication, you can, you know, if you want to go read the paper, you can, but he just gives you like a overall summary and tries to simulate how, you know, this new neutron star, you know, that's cool. Spins and all sorts of stuff. Yeah. I'm totally addicted to that.

**Chris Gammell:** Yeah. That's great. Yeah. So like that kind of thing, like, yeah, basically like reading abstracts and, but also contextualizing. Right. So like, right. Yes. You've got to, you've got to make it exciting. This is interesting. Cause it's, it's, you know, a wide range of topics.

**Dave Jones:** Hard to do it. It's a podcast. It's more easier to do it with visual stuff.

**Chris Gammell:** Especially when we don't read the articles beforehand. Don't forget about that, Dave.

**Dave Jones:** Yeah. Right. So yeah, no, there's, I agree. There could be a niche out there for people reading papers and the latest papers and. Yep. Yeah. And pulling out the interesting stuff, but you've got to make it exciting. So that's, that's the trick. That's the ticket lady. Make it exciting. Anecdotes, Dave. Anecdotes. That's what people like.

**Chris Gammell:** That's what people like.

**Dave Jones:** That's what the young folks like these days.

**Chris Gammell:** Are there any other anecdotes we should be talking about here on the, or I guess links. We have like four weeks worth of links. So.

**Dave Jones:** We did because we were, I don't know. Yeah. Just didn't do a show for four weeks or something. Don't know why.

**Chris Gammell:** Here's, here's some like, so basically I've been dumping links in here as I find them. So like a lot of them are RF based right now, but there's an RF PCB simulation cookbook from TI. I'll link that. That's pretty cool. I, and you know, some of these are like, I go and look at them to dig in later.

**Dave Jones:** Yep.

**Chris Gammell:** Kycat has some new RF tools because they're not great with RF yet, but those are interesting. What else? Oh, there was the Navy electricity electronics training series. Oh yeah.

**Dave Jones:** Yeah. That, yeah. Yeah. They've got the whole, they've released all the training material or whatever. Yeah.

**Chris Gammell:** That's cool. Yep. And then there was one other one. Oh, it was from Contiki IOT in five days. I thought this was interesting. So it's like a, it's like an ebook almost. And basically Contiki is like one of the, it's a,

**Dave Jones:** it's a tour group as far as I, yeah,

**Chris Gammell:** right. They also do that. Yeah. I mean, that's also the same name. I'm not sure what Contiki stands for, but this is basically like, so like they go through sensors and like, what is, so Contiki is an OS. And then basically it's, they talk about sensors and how to set up wireless and all the different things, but it's like kind of just a good overall look at like building a small wireless system with sensors, including up through like using Contiki to talk over IPv6 and things like that. So like,

**Dave Jones:** right.

**Chris Gammell:** That's a lot of, that's a very tall stack, I think, you know, to go from low level hardware all the way up to sending packets. But I think that that actually resonates a lot with, with that document is very,

**Dave Jones:** very comprehensive.

**Chris Gammell:** Yeah.

**Dave Jones:** It looks very, yeah, yeah. Wow. Someone's put a lot of work into that. Multiple. Yeah.

**Chris Gammell:** Yep. Yep. Yep. Someone, people in Italy, it's a school, I think.

**Dave Jones:** there are Italian names. Yep.

**Chris Gammell:** Yeah. Yeah. Dot. It is the, is the, is the domain. So that, but it's for 2015. So keep that in mind, you know, that it's an old thing, but you know, it checks out. Yeah. So that's, Oh, then here's one other one. I guess it's a video. I mean, we're, I'm always linking to Alan bulky stuff. Alan's been on the show before. I've talked to him about coming back on. He said he's very busy right now. So, but you know, his stuff is amazing.

**Dave Jones:** I know you're fanboying over his V and a stuff.

**Chris Gammell:** I mean, it's great. It's great. Like, I wish it was there. I wish it was there before I bought mine. You know what I mean? Like, that's what I, I've learned this stuff through like talking to Jeff Kaiser a lot. And, uh, you know, just, uh, yeah, just struggling. Someone asked me today, like, how, how have I learned RF? And I was like, Oh, well, usually I buy something and then I struggle to use it. And then I call a friend and then I ask on Twitter and then I go back and like, you know, like just the usual way of learning things. Right. I guess. Yeah.

**Dave Jones:** And there's an interactive guide to Maxwell's equations for all you Maxwell fanboys. If you're, if you just can't get enough of those weird symbols, you know,

**Chris Gammell:** give me the curl, man. Got to do my curls. Hit the Maxwell gym. Yeah.

**Dave Jones:** It's like, yeah, there's fun bedtime reading right there. Maxwell. Yeah.

**Chris Gammell:** Cause you will be out.

**Dave Jones:** Yeah. There's some people who just love that stuff. You know, I was never into, you know, that just wasn't a thing for me.

**Chris Gammell:** Okay. One last thing about books. I'm listening. I'm reading a book right now called ultra learning. And he talks about transference. And this is like an argument against like traditional education. It's, it's the transference has been like disproven actually in different studies.

**Dave Jones:** What transference are we talking about?

**Chris Gammell:** So like transference would be, okay. So you go and sit in a class.

**Dave Jones:** Of the, the, the information into your brain processed. There's that.

**Chris Gammell:** That is a type of transference, but no, this is actually like the assumption that learning, learning the theory and then being able to then take a, so let's talk about Ohm's law, right? You go and sit in the classroom and you do all the math and you learn Ohm's law. And the transference is the assumption that you will then go and be able to use that in the lab and basically apply this abstract concept to a very physical, hard, real world thing. And that has been disproven many things. And I, of course, okay. I'm of course going to talk about books that resonate with me. This book is just like, it's got my, you know, contextual, you know, alarm bells ringing. So like take that with a grain of salt, but it's interesting book. And the thing I like most about it is it's very practical. It gives you like, like different things you can do. Like, like it talks about creating drills, drills for yourself. Like you might with the sport or music or something. Right. Okay. And things that like, you know, with like electronics, what a drills look like for electronics. It's like, Oh, okay. And so I've just been kind of thinking through that and it's, you know, I might become part of contextual electronics at some point, but it's a, it's a very interesting concept that I don't see talked about too much other than like make more circuit boards or do more electronics is like more drills, but that's not very specified. So I think that's a good topic for a future show of like, what are drills and electronics look like? And I'd love to hear from people if they have thoughts.

**Dave Jones:** Well, you dribble the electrons over here and then you dribble this way and you pass that way.

**Chris Gammell:** That's right. Right. Right. You got to do fancy footwork. Don't forget about that. Interesting. Oh, Oh shit. One last thing. I'm sorry. I've been swearing a lot this episode. There is a giveaway. We have a giveaway. So this is actually, this is an interesting, I should have put this on the list, but it is called the quick feather. And this is a new type of chip. I have to send you a link real quick.

**Dave Jones:** I've got it.

**Chris Gammell:** You do. Okay, great. So it's a new type of chip. That's got the chip. Doesn't seem like it's the company. Doesn't seem like it's going to stick around that long. And I hesitate to say that. Just because, just because like quick logic, it just sounds like, I'm sure it just seems like they're not going to be around long. Just given that name, for some reason, it just strikes me as like a, yeah, I mean, like it's a, you know, I'm sure they've been around. I'm sure they're fine. I know. I sound like a, like a, like a mean person, but, but basically it's a dev board for this chip and it's got an integrate. So it's basically a cortex M4 with an FPGA built into it. Right. And so it basically it's like flexible fabric. And the whole idea is it's like a chip that's meant to basically meant to like process. Oh, so the,

**Dave Jones:** so the quick logic, it's the quick logic EOS S3 chip. That's right. So it's a system on chip. Okay. So they've done their own. Right. Okay.

**Chris Gammell:** Exactly. And so like, it's like specified to be like for like machine learning type of thing. So if you had like a microphone, it has like a microphone input for it. Right. And that goes into a, a bit of, I think hard logic. Then then you can then connect to with the FPGA fabric. And basically, so it's like a design that this company had made. The basically is they bought the arm court, they bought the arm car, they core, they put some flexible logic around it and they built these custom blocks that do a bunch of different things. It's meant to be like a, it handles different functions for, you know, IOT type devices and stuff like that. Edge AI and ML, blah, blah, blah, blah. And we're giving one away. Are we? We're giving one away. How do we do that? I'm going to come up with a, a, a questionnaire. And if you fill it out, one person will be sent one of these things. So it'll probably be about learning or something like that. We've done that in the past, but I did say I give one away and we can ship anywhere in the world. So that's not a, that's not a problem. And yeah, it looks like, it looks like a cool board. It's also like a, I think they're on it. This is, I'm interacting with the crowd supply folks. So the crowd supply.

**Dave Jones:** Yes. It's on a crowd supply. Yep. It got funded. Yep. Yes.

**Chris Gammell:** Yep. I think it was a $1, $1, $1, $1. Your goal. Yeah. Goal. Okay. We, we knew what I was going to, yeah. 23,000, you know, 23,000% funded or whatever it is. Yeah.

**Dave Jones:** Nice.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. Okay, cool. That's it. That's it.

**Chris Gammell:** Well, that's it for the show. Half a order of magnitude over.

**Dave Jones:** Yep. Yeah. Half an order. Yep. Near enough.

**Chris Gammell:** Wouldn't order of magnitude be like, if you're going from 10 to a thousand though. Well, it wouldn't be like. Two orders of magnitude. That's two orders of magnitude. And, and,

**Dave Jones:** and an order of magnitude more than 10 times is a hundred. And then two orders of magnitude is a thousand. Right. Right. Right. So like,

**Chris Gammell:** but like 500 wouldn't really be half an order of magnitude, would it? I mean, it's like.

**Dave Jones:** Oh, well, no, well, no, it depends what your baseline is. Right. Right. If your baseline is a thousand.

**Chris Gammell:** This is just me getting, getting back at you for the.

**Dave Jones:** Oh, okay. Oh, I get you. I get you.

**Chris Gammell:** I feel like 450 would have been like. Yeah. Anyways.

**Dave Jones:** But once again, it's, it's, it's, it's, it's, we're going to the order, you know, going to half an order. It's near.

**Chris Gammell:** I think we could just say 500 is pretty cool. So congrats, Dave. We did it. We, we had to five. Let's say 512 though. Let's get.

**Dave Jones:** Yeah. Yes. Woo. Party poppers. The excitement is palpable. It's. That's it. Show over. Catch you next time.

**Chris Gammell:** Yep. See ya. Bye.

**Speaker ?:** !
