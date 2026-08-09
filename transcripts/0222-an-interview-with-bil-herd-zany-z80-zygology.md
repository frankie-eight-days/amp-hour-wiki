---
episode: 222
title: An Interview With Bil Herd - Zany Z80 Zygology
url: https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/
---

**Bill Hurd:** This is The Amp Hour Podcast, recorded October 27th, 2014. Episode 222, with guest Bill Hurd, Zany, Z80, Zygology.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Bill Hurd, and I'm a recovering Commodore engineer from the old days.

**Dave Jones:** Oh, nailed it. Welcome, Bill.

**Chris Gammell:** How you doing?

**Dave Jones:** Thank you very much for coming on the show, Bill.

**Chris Gammell:** Well, it's my honor. 12-step program to getting out of vitro, huh? Oh, yeah, yeah. You know, you have to help other people and, you know, come to grips with all you've done bad in the world, everything. Yeah. Please, tell us your sins.

**Dave Jones:** You designed that pesky Commodore 128, didn't you?

**Chris Gammell:** Oh, God, we used to get threatened, too, by our own Commodore group. You know, if you do this, we'll do that. Yeah. And, you know, if I throw out one back story, it was I learned to spell my name Bill with one L because one day they had upgraded the report cards at my school. And I'm from a small town in Indiana. And they spelled William with one L. And I'm like, teacher, what's this? They're like, oh, it's easier for the computer. Oh, it's easier for me, too. So I started Bill with one L. Of course, then a math teacher took off some points on my test. And that's all you need to do to a rebellious youth is like, well, I'm spelling it this way forever. Right. Right. So when we're doing like the 128 or even the TED series on the TED, we had included a monitor, a whole ROM monitor. So you had your whole development environment with you. And we actually did it for us, but you got to share it. But we got back a telex. Remember telexes? They were before faxes. Yeah. Chris doesn't hear. No, he's just rolling his eyes. Chris, we used to have to count letters when we sent things. But we got a telex from the head of Commodore England saying, you've now created the perfect machine for piracy. And I sent back a two-word telex that said, thank you. You know, it's like, well, then we're not taking it out. And then we got during the 128, we got a, I forget what it was, telex or effects, but we got a message from Commodore Australia saying that if we ship the 128 with a Z80 in it, they would personally. Z80 here in Australia. Yeah, Z80, right? Yeah. They would personally remove each Z80 out of the board. And we're like, well, then we're definitely leaving it in.

**Speaker ?:** What?

**Chris Gammell:** Yeah.

**Dave Jones:** Why the hell?

**Chris Gammell:** Oh, yeah. See, there was just, well, it was religion, you know? Right. Anti, Z80, anti. So, but that's, you know, anyways, if you tell a Commodore engineer not to do something, unless you're his boss, he's doing it. And even then maybe a friend. Well, I did disobey my boss once, but I knew something he didn't know. And that was that he was going to be fired in three weeks. Ah, there you go. And he had told me on the 128 to make the sync be unique. So we had regular monitors, Taxon, I think, which had the positive going syncs, both horizontal and vertical. And the Apple at the time had two negative going syncs. Right. So he told me to make one positive going sync for, like, horizontal and one negative going sync so that they had to buy a Commodore monitor for the ADCOM.

**Dave Jones:** Oh, you evil, evil man.

**Chris Gammell:** Well, he was the evil one, right? Yeah, I know.

**Dave Jones:** You were just the engineer instructor.

**Chris Gammell:** Well, see, and, you know, I'm known for being really honest, right? You know, so I've never lied to him or anything. And at one point he said, did you take care of it? I said, it's taken care of, meaning I'm doing it my way, not your way. Right. And as time passed, he did leave us. And then our monitor did not ship for about six or seven months. So the only reason we could use an ADCOM monitor was because I disobeyed my boss. Awesome. Well done. That was the one time.

**Dave Jones:** So otherwise, what, it would have been stuck to 40 or what?

**Chris Gammell:** Yeah, you would have had to use just the 40. And, you know, this was kind of, we thought it was kind of cool that you could have a simultaneous 80 column and 40 column mode. And, you know, because it's a time to get off the TV set was here, you know, stop making it. And, you know, when you try and tell somebody that these days, you know, it used to be on the TV and they're like, what, you used to set the computer on the TV? And it's like, no, no, no. We had a little box and we would make it be on channel three. Oh, goodness. Yeah.

**Dave Jones:** So who did, how flat was the structure at Commodore? Who did, did you, who did you, how many layers were there above you being the one, like the head hardware designer?

**Chris Gammell:** It was a strange place. Yes, because it felt like a little big company, I used to call it, because there, when I got there and we were in the MOS building, MOS semiconductor. So there was chip tab, right. Yeah, right below. So you can't get closer than that. And there was about 20 of us, including chip designers and drafts people and stuff. And we worked for Shiraz Shivji, who would go up the mountain to converse with the almighty himself, Jack Tramiel. I mean, so it was very flat. And you knew you worked for Jack Tramiel. You could feel it in everything going on. You know, as we were told, thou shall not have more than nine chips. And we were, oh, yeah, absolutely. So later, when we then moved to a place called Westchester and Mr. Tramiel leaves us, there was just a void, a vacuum. Right. So we worked up to a vice president, but it didn't feel like there was anybody above him. And so there was no coordination with marketing or anything like that. And so it was, we were still flat. It's just there was no top is the way it felt. You got it. Right.

**Bill Hurd:** A dictatorship without a dictator anymore, right? Right, right. So can we take it a little further? So, again, this is going to be the young guy kind of asking for all the other young guys and girls out there. Maybe a little more backstory. How did you get to that point? And who is Commodore? He's got to ask. Who is a computer? Right. At first there were electrons. That's right. And they had spin. Right. That's right.

**Chris Gammell:** So. Well, you have to. Well, Dave, when you were first going to school, had they found the cork yet? Seriously, I went to school. There was no such thing as corks. So that's how old I am. Right. Okay. Now I see. I think we had to make all that up later. Yeah. Okay. That didn't affect the computer too much, though, did it? Well, if you thought you understood things, you found out you didn't. You know. Ah, true. You know, we used to say, or I used to say it's all analog anyways, you know, and it was true about digital. It's not a one or a zero. It's a signal that tried to get to a one, and along the way it did some ringing and stuff like that. But at the heart of it, it's analog. And if you think like that, then you'll be a better troubleshooter. Yeah. And until one day, a guy named Hedley Davis, who went on to do the Xbox, DRAM for the Xbox, he said, well, what about quantums? Okay, it's all analog until you get to quantum effect. Quantum, yeah, yeah. Exactly. And then corks came along. Pesky quarks. Quarks, yeah. So you're asking how I got into Commodore and being in that weird spot where they let me design things?

**Bill Hurd:** Yeah, yeah. So you and I had met at the Hackaday event last month.

**Chris Gammell:** It was a nice event, yes.

**Bill Hurd:** Yeah, it was a lot of fun. And you were telling me about your experience before that, too, and how you kind of worked up as a technician as well. And I thought that was really interesting. So just kind of going backwards and moving forwards.

**Chris Gammell:** Okay, yeah. Well, I'm from a small town in Indiana, and I did learn to speak English once I got out east here because nobody wants to hear you talk about cement and stuff. So, Chris, you're from Ohio, though, right? Yeah, I'm from New York, but, yeah, I've lived in Ohio for a long time. Lived in Ohio. Well, have you noticed that about halfway across Ohio, it becomes cement instead of cement or bag and sack change?

**Bill Hurd:** Yeah, no, there's actually some really good – on the subreddit, data is beautiful. There's actually, like, a post about all the different ways people say stuff, and there's, like, a heat map, and it shows where it changes. And there's all these, like, weird vernacular changes.

**Chris Gammell:** As soon as Ohio gets flat is what I've noticed. Then all those things change. So, anyways, I'm from the part of the country that sounds like our IQ is – I shouldn't say that. I'm denigrating half the – well, what we say is cement and stuff. So I'm in a small town school, and I learned I could get the math teacher off track, and he would talk about anything from math. And so I accidentally ruined my own education, right? Because now I don't know math. I got him a second year. I'm like, oh, I still don't know it because I did the same thing. And during this time, though, I had been fixing anything and everything. I mean, it's just – I had actually kind of left home during the summer. I'd go out and about, and I would fix your – they were called 8-track tape players, Chris. I don't know if you've ever seen one. I've watched popular culture at least. I've watched the 70s show, Bill. Oh, okay. But, yeah, everybody had one, and everybody had shorted their wires together with bad wiring and blown their outputs. And so I would do that. I would fix it. You know, it used to be I'd fix it for a six-pack of beer, and eventually it became I'll fix it for dinner, you know?

**Bill Hurd:** Nice.

**Chris Gammell:** Yeah. So your memory on how to troubleshoot gets really good when food is associated with it. And so, you know, I became really good at troubleshooting. And I had started from one of those little electronics kits with the little springs. Yeah, like the 200 of them. Yeah. Oh, yeah, absolutely. I built every one of those things, and then I remember when I popped a transistor, you know, I gave it too much voltage and stuff. And my dad had one day given me like $4 because I fixed his light organ. Again, a thing from the 70s when you put music on, the lights would flash in time with music. Yeah. And it had popped an SCR. So now it's the association with money is coming in too. Ah, yes. Yeah. And so during high school, which I'm trying to muddle my way through, Indiana High School, I started designing. I was a big Emerson Lake and Palmer fan, and sitting and listening to the music, you could see the electronics behind it, right? And so I started designing a synthesizer to the point where now I'm taking off days from school to, like, cover it with, you know, a nice black felt or something and, you know, put the theremin thing in it. And so I ended up dropping out of school because I had asked for an electronics TV repair course, and they informed me I was not academically inclined enough in an Indiana school to take electronics, right? Which would have been my only thing I could have taken, right? So I literally, I dropped out of high school, and actually I signed up for the Army National Guard at the age of 17, did all of the basic training and everything, and now I'm a teletype repairman. So now I've actually got a certification to me, right? I'm just now turning 18. And they had to put me in the TV repair course then. So that's how I gained the school, right? And as it is, I still owe them, like, an English credit and $4 for a library book. But they did send home a diploma a couple years later. I guess they got tired of it hanging out in the office or something. And that teacher taught me one thing, though, and it was cool because he taught me two things, actually. First, use your eyes to fix something, especially in TVs where things are hot. You know, if you see a resistor color code that doesn't make sense, it's because it got hot and the oranges changed to brown and things like that. Right. Yeah. And if you really can fix it without getting your scope out, why would you get your scope out? Yeah, yeah, exactly.

**Bill Hurd:** Yeah. Especially in repair where time is money. That really matters, yeah.

**Chris Gammell:** If you fix a TV set, if you actually have to fix it, which takes an hour, if you have to troubleshoot a problem you've never seen, you don't make any money, you know, because you get paid $10 a set you fix. Right. If you remember how you fixed it last time and do it in 10 minutes, you just made some money. Yeah. So there's that definite, you know, where it correlates there for you in your head. And I forgot where we're at. We're coming up through, oh, so the other thing he taught me. Yeah. So the other thing he taught me, though, was to shut up and figure it out. And I didn't know I could do that. I thought if I had this idea, I had to go ask the teacher if that's what, and he said, shut up, figure it out. And that's when my electronics career began. Yeah. Because, you know, well, I haven't been trained to, you know, design ICs. Shut up, figure it out. Oh, okay. So that's kind of what happened. So I ended up, you know, doing the repair for a while, and I moved to Pennsylvania. And this is where Commodore had moved to. I didn't know it at the time, of course.

**Dave Jones:** I didn't know they were in Pennsylvania.

**Chris Gammell:** Yeah. They were in Westchester. Jack Tramiel moved them there from the West Coast due to the cost of engineers, quite frankly.

**Dave Jones:** Were they doing PCs back then, or are they still doing their…

**Chris Gammell:** The word PC hadn't even been invented yet.

**Dave Jones:** Programmable calculators. There was those?

**Chris Gammell:** Oh, yeah. That kind of PC, right. Not a personal computer, but yeah. Sorry. Yeah. Yeah. And it was the pets and stuff. You know, so… Oh, okay.

**Dave Jones:** It was the pet. Okay. So they had got into the… Right. They had got into the computer market.

**Chris Gammell:** Right. Right. Most definitely. And Chuck Petal was with them.

**Dave Jones:** So we're talking about 1977 here is when the pet came out, I think.

**Chris Gammell:** Let's see. Yeah. And then the Vic was around… If my memory serves me. See, and I only know the later years. I have to listen to Chuck Petal, who's just great to listen to. He's the father of the 6502 and led the team for the 6502. We'll have to get him on the show. Yes. Yeah. Let's talk about that because he's definitely worth… So, but I ended up at a company that made digital scales, which were basically 6502 computers with a load cell interface. And so the analog on that, we were doing one part in 50,000. And you really did have to fix things like ground loops and understand them and stuff. It's no faking it here. Right. And I had started as a technician in production and I found that, you know, I could go to the box of boards, fix 50% of them without ever turning them on, you know, because I'd learn to use my eyes. And so by lunch, I've actually fixed everything. I've hit quota. So they let me do other things, you know, the second half of the day. Great. And I would do things like I had written up things like we were using a static RAM incorrect. We had to make our own battery backup back then. There was no real flash and stuff. So you… Oh, yeah, of course. Right. You would take a little battery and…

**Dave Jones:** A battery and a diode and on the supply rail. Right.

**Chris Gammell:** Yep. Yep. And if you did it wrong, if you took like a Variac, you know, the variable transformer and put it right at 93 so the reset circuits turning on and off, 60,000. Ah, yeah. You can blow them all up, right? So you had a… It sounds easy and it was… Oh, it was miserable trying to do it. Well, we were using one of the chip enables incorrectly. One chip enable was better for RAM backup than the other one or battery backup, I mean. And so I wrote that up and eventually, you know, I started writing up other things. It was kind of that put up or shut up. They pulled me into engineering as an associate engineer, you know, it's like, now fix these things you've been writing up. So that's kind of how I got my break. So now I'm doing 6502s. I'm doing the programming. One of my first scales was for Hershey candy kisses, you know, to tell you how many candy kisses wide the belt was and how much chocolate's in them and stuff. And then one day, me and my boss stopped getting along. And there was a lot of things going on at the time. But my friend Headley said, hey, there's a company called Commodore hiring tonight. If you want to go. Tonight, okay. Let's go. Yeah. And what it is, and, you know, and I did it later when I was with them. What they would do is just every night, even if you worked a 14 hour day, a bunch of you piled into a car, go to where the headhunters were and interview people till about 11 o'clock, 10 o'clock at night to try and find more people to come in. So, yeah, it was, I mean, so we are dredging the whole Philadelphia area looking for anybody that, you know, we'd rather hire somebody that didn't fit and throw them out later than, you know, miss somebody. It was kind of how it felt.

**Bill Hurd:** Oh, wow. Well, that's interesting, too, because they chose Westchester, but, like, I mean, the Philly area in general, there's, you know, there's probably town around there.

**Chris Gammell:** Well, they used to call it Silicon Valley East because we really did have about five chip fabs up and down Route 30. Oh, interesting. And so MOS wasn't alone in that, you know, so there really was a base. And, you know, you'd walk in a place looking for a job and you'd recognize one out of five people that walked through the lobby, you know, because you'd all incestuous relationship there in Philadelphia. Yeah. All right. But the way I got hired, though, was I, when I was interviewing, the first guy I interviewed with, I blew it. I was like, oh, I couldn't get it. You know, I was trying to, like, you know, synchronize with him, right? Talk about, and I think he thought I was showing off or something. But the second guy, when he was talking, he said something. He said, Lodex 05, which is a 6502 opcode. And I muttered the machine code under my breath. I said, like, A205. And he looked at me. And now he says one out loud in his door came later. And I'm like, 8D03. And he's like, okay, we'll have you come in to talk with us. And that was it. That was that moment when the door opened for me. Nice.

**Dave Jones:** It's just those simple things in the interview, isn't it? Yeah. You know, like, it doesn't have to be complicated. It's just if you know that, then the person instantly goes, right, this person. You must know. It's a signal. Right.

**Chris Gammell:** It's like if you have your towel.

**Dave Jones:** I got offered a, yeah, I got offered a job once because I knew what a 7-4-HC-244 was. Right. You know, he asked me that. And it was stunned that I actually knew off the top of my head what it was. And like, boom.

**Chris Gammell:** And the difference between a 241 and a, yeah.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** So, yeah. Yeah. And so what they were looking for is somebody that went even an inch outside the box, I think. You know, so to know the machine code under the opcode. And actually, then at my time at Commodore, that was vital because, you know, here's the chip guys, or the chips and the chip guys. And to fix things, we had to look inside the chip. We couldn't just, you know, stop at the pin, especially with the schedules we had. And so, yeah. I got a bunch of stories about how the chips messed up and then we would actually, you know, kind of compensate for it.

**Bill Hurd:** Yeah. We complain about like errata and stuff like that these days. But you guys are probably running so hard so fast. Yeah. And it was such crap in processes back then that it was just like.

**Chris Gammell:** Yeah. Oh, and the die in the wafer was what, three and a half inches or something. And, you know. Yeah. Right, right. Here's your two good die off the wafer. And nowadays, what are they? 11 to 12 inches? They're moving to 18, actually. The 450 millimeter. Oh, that's insane.

**Bill Hurd:** Yeah.

**Dave Jones:** That's just nuts. So, for the record, when did you join Commodore? And at what point were they with machines and things?

**Chris Gammell:** Well, I joined in. See, it turns out we didn't tell time very well because we always told time by the CES shows, the consumer electronics shows.

**Dave Jones:** Right, yeah.

**Chris Gammell:** So, you know, 84 is really 85 and stuff. So, I joined around 83, I think. 83, okay. So, the C64 was out. And I think we skipped a CES show where we just did the Commodore 64 again. The big thing, the project at that time was actually to make the C64 better. Because it didn't work on paper and, boy, it barely worked in production. Why is that? Why is that? Well, if you summed it up, it's because we didn't have a high enough frequency to start from to create all of our signals. Okay? So, we did have the ability to make a RAS fall and then switch the row addresses to the column addresses. Of course. Yeah, yeah. And then have a CAS fall.

**Dave Jones:** And so what... Yeah. So, you needed a faster clock so that you could divide it down to do different things to generate those short RAS pulses.

**Chris Gammell:** That's right. Right. And so... Ah, of course. Those are memory things for people that don't know.

**Dave Jones:** Yeah, if they don't know. So, it was running at one point. Was it 1.048 or was it 2.0?

**Chris Gammell:** Well, they came from 14.318. And I think... Oh, okay.

**Dave Jones:** So, the main crystal was 14. Yeah. Right.

**Chris Gammell:** Because of the color burst. But the... Yep, of course. So, they tried to do things like use... You know, a clock is very accurate in its cycle time. But its duty cycle can be, what, 10%, 15% off. You know, the rising edge will always rise at the same time. But the falling edge can move around a bunch. And if you...

**Dave Jones:** And that's going to screw you up. And that, right.

**Chris Gammell:** And they were using that, for example, to switch from row addresses to column addresses in the DRAM. And so, in production, they were doing things like putting capacitors on RAS and CAS.

**Dave Jones:** Oh, no. So...

**Chris Gammell:** The ultimate kludge. Right, right. Oh. So, in... What was cool is I walked down and asked a DRAM designer one day, you know, because I did something illegal too one time. I started a RAS and then I took it back. And he goes, oh, the internal to the chip, the column driver, the row drivers are banging their heads. And so, if you could picture that, oh, now I know why the cells get lost. Every, you know, there's voltage is banging around and stuff. And so, yeah. So, when you slow a signal down like that, all kinds of things go bad. You know, things turn on and... Yeah, yeah. Yeah. You're in the X.

**Bill Hurd:** You probably even... I mean, you start to have probably the threshold issues as well, right? Just because you start to...

**Dave Jones:** The slew rate. Yeah. Right, right, right. Why don't you put a cap on there? You change the slew rate. You haven't got a sharp one. So, the transitions are very slow in digital logic. Oh, yeah. Yeah.

**Chris Gammell:** And I've got a whole thing where I talk about, you know, the unknown. And the moment any one of your inputs clears the bottom, you know, clears one of the margins or the thresholds, the whole device goes into an unknown state or starts to propagate an unknown state, right? And hopefully, you get everything set up before it actually comes out a pin as oscillation or something like that.

**Dave Jones:** Metastability. Yep. Yes. Let's not get it. Yeah, that's a real huge one.

**Chris Gammell:** And that's what caused one of our chips, the 8563. The designer of the chip had not read the book about metastability. So, we had to give them a refresher course with the bottoms of our shoes. But what they were doing in production, they actually had a, the security guards were told to not let the engineers down there because they didn't want us to know they were doing stuff like putting caps on the RAS and CAS. So, they would essentially do anything to ship. And that was the Commodore attitude. If we got it under your Christmas tree and it broke. That's all that mattered. We still got it under your tree. You bring it back and we'll fix it now for you. Yeah, right. And I personally saw where one day, because they, you know, as I started drinking beer with the guys that ran production, then suddenly we started being allowed down there and we started saying, look, we can help. We're not the enemy. Yeah, right. But one time I did see a skid that had a sign on it. You know, it's like bad. And later the sign is laying on the floor and the skid's now good because the sign's been removed and it shipped. That's real. That's all it takes. Yeah, it's Commodore, you know. I love it. Oh, boy. And there was other things. We, you know, the Micron wasn't making DRAMs very well. Well, that's okay. Yeah, right. We weren't using them very well. So, we sued each other, you know. We came to the...

**Bill Hurd:** It was a lot of fun. Oh, that's terrific. I'm really interested in this interplay between you and the chip designers as well because... So, like, was it mostly production side down there or were they actually trying out, like, new types of chips and stuff like that as well?

**Chris Gammell:** Well, there's two kinds of chip guys that I worked with. There was the chip designers who literally sat right in, you know, three rows over from where we're at. And so, the guy who did the VIC chip or who modified the 6502 for whatever we're doing, and he was the guy you'd work with to say, look, we need an extra pen. Give us this. Can you get us that clock? And one of those was the Z80 clock where I sent you the schematic earlier. There's a story behind that. And then the other one was the production engineers at MOS. And their job was to, like, cook the recipe. And, you know, if you cooked it exactly like it's written, you wouldn't get yield. You'd still have to fuddle and fiddle this. And they were doing things like even a run that they thought was okay, they would still vary one of the parameters by a percent or something because they're looking, does it get worse by a percent or better? Well, if it gets better, change it again next time. And they call those schmooze where they would plot two variables against each other and it looked like a schmoo. But Dave, do you remember those from the comics? Chris, I'm not even asking you. You're too young. Oh, I know what it is, though. Do you?

**Bill Hurd:** It's the thing that, like, wanted to be eaten or something, right? No, I don't know that. Oh, it's...

**Dave Jones:** No, maybe that didn't make it to Australia.

**Chris Gammell:** Yeah, it's just... Yeah, probably not. No, it's just... It's this hump-shaped thing. And we had these characters called schmooze. But, you know, it was basically not quite a Gaussian distribution. But they were always plotting yield against these parameters. And they showed me. And so now I was actually designing, knowing some of the things that happened in the chip production and stuff. And so it was really cool to be around, you know, the whole chip fab process and stuff. Though, they got me back. Did you ever hear about the parking lot there? Had you heard about that? No. Tell us. I've never heard of that. Yeah. Well, MOS was dumping its chemicals in the water table into the ground.

**Dave Jones:** Oh, no.

**Chris Gammell:** So they got caught.

**Dave Jones:** Oh, yeah. I've heard, yeah. Yep.

**Chris Gammell:** And they got caught. And so they had to aerate it. Well, it landed on your car when they did that. And so there was a certain side of the building you're supposed to park on. Well, I not only, you know, parked on the wrong one. I parked under a tree. So I had these leaves glued to my car, you know, from the chemicals that are in the ground. And I think the chemicals are kind of still there to some degree.

**Dave Jones:** Yeah. I think it's an abandoned site now. I think I've seen a video of somebody going and there's big warning signs there. This is an abandoned site. Please don't enter dangerous.

**Chris Gammell:** I think they also paid for like the eight people in the area to get like street water or something like that. You know, so it's still poisonous. But here, drink this instead. So Commodore answer.

**Bill Hurd:** I think a lot of the old chip fabs were turned into brownfield sites, though. I think so. Yeah.

**Chris Gammell:** And in New Jersey, it's just illegal to have a PCB house. You can't make prints or reports in New Jersey, from my understanding. Oh, nasty. Yeah. Those guys were doing it, too. You know, dumping all kinds of stuff in the groundwater.

**Dave Jones:** So was the differentiator with Commodore that they had such a close relationship with Moss, you know, basically downstairs, that you would do all your custom chips? Because things like the Apple and the Tandy, they were all doing pretty much off-the-shelf chips, pretty much.

**Chris Gammell:** Yeah, they were using our chips.

**Dave Jones:** Whereas the Commodore was all mostly custom, wasn't it?

**Chris Gammell:** Oh, and that was the wizardry, the magic, right? Right. And like the VIC chip. And there's urban stories that the VIC computer was just really a breadboard to show the VIC chip. And Jack Tramiel says, this is what, no, no, this is the chip. No, no, this is the... And, you know, when I ask around about those urban stories, nobody contradicts it, you know? So it may not have gone exactly like that, but it's not like it didn't either. Yeah.

**Dave Jones:** All right, so that was the VIC-20 they shared because that was their first...

**Bill Hurd:** I need a bell. I need a bell or something. What is a VIC chip? I'm sorry. Sorry, I know I'm not the only one here. I guarantee someone in the audience is happy I said that.

**Chris Gammell:** Yeah, yeah, all right. The video interface chip, so BIC, in the VIC chip one, which is used in the VIC computer. And back then, we used a chip, I know Dave's going to be familiar with it, like the 6845 for CRTs. Yes, absolutely. That was used in everything. Everyone used that. And you could do color with it. You could put color planes and stuff. And then there was a 6847, which was, oh, okay, it's supposed to be doing color, but it's still kind of lame. And the whole problem back then was, how do you talk to the memory that the video chip needs to display? And if you talk to it while it's displaying, you get dots on the screen, right? Because you took over the bus while it's displaying it. So you have to stay out of the time when the video's displaying. So, well, how do you do that? Well, they started doing it during the vertical interface time. So it prints a row across the screen, and then you get this. And then a vertical retrace. Yeah, or horizontal. Yeah, you get like 10, 11, 13 microseconds.

**Dave Jones:** Yeah, you get 30 microseconds during the horizontal retrace. And then a whole 30 at the vial. Wow, yes, score.

**Chris Gammell:** And then we said enough of this. And we started jumping on and off the bus where there's a master clock in the 6502, unlike Z80s. See? See how quick I changed to your personal. Well done.

**Dave Jones:** Well done.

**Chris Gammell:** It's basically Australian now. Yeah, yeah, I'm there. Go check which direction the water in the toilet rolls now. There you go. But the, and now I lost my thought. I thought of a toilet, and it's. It's all gone down there. So what we did is on the 6502, though, there was always this clock low, and then always a clock high. And at the end of that period, you've done something. It's not like sometimes it takes two clocks, and sometimes it takes four. It always takes one. Well, what we did was during the first part of that, we gave up the bus. And we said, video processor, go have at it. It's your DRAM, but we're going to come along in 500 microseconds and want it back. And that's what was the magic of the VIC chip. So suddenly, the processor is running at full speed. And meanwhile, the video chip is getting everything it needs, almost everything it needs, during the second half. And then what the VIC-2 chip did were sprites. And it was like, I think there were 16 of them. And a sprite is that object that moves around on the screen while you're playing a video game. And so. Was that the first one to. What was the first. Who was first to do sprites? Sprite. We weren't supposed to say sprite. We were supposed to say movable object block. Because. Ah, trademark. Yeah, TI. TI was used in sprite. Which. Right. Which we put nails in their coffin. Remind me, before we're out here today, what we did at TI.

**Dave Jones:** And we're talking about the TI.

**Chris Gammell:** TI-99A. 99-4A. Yep. Right. And so, yeah. But a sprite then was that. It's kind of like in Atari, they had player missiles. But they only had like two or something. And here we've got 16.

**Dave Jones:** Yeah, that was the limit.

**Chris Gammell:** Right. Yep. And so the sprites, you didn't have to draw it. You just pointed it. So you drew it once in memory and said, this is what that sprite number one looks like. And all you had to do was move around its XY position on the screen. Nice. So hugely fast for the day. And then there was some automation. Like if two of them overlapped, you'd get an interrupt, you know, for sprite collision.

**Dave Jones:** Which then you could, yeah, yeah. So it gained. Perfect.

**Bill Hurd:** You draw that color difference or whatever it is then. Well, the main thing was. Oh, yeah.

**Dave Jones:** Draw an explosion or something. Right.

**Chris Gammell:** That's how you know you got hit. Right. You didn't have to go around checking everything. You just, oh, hey, I got an interrupt. Somebody got hit. And then you'd go see which sprite set it. And then check, you know, did it, do I explode or whatever. And so that was the big chip. And that was really, you know, the Commodore 64 sold 27 million. And it was the highest selling. Now, this is according to me. The highest selling single computer ever. Everybody agrees with that. But where I change it is I think that the iPad has sold, I think it sold like 30 million. And if you call the iPad a computer, then that's the first thing to break the Commodore 64's record of 27 million. Ah, interesting. Right.

**Bill Hurd:** When you say 27 million, too, what kind of time frame is that over? Is that like in a year of its lifetime? Five years. Five years. Yeah.

**Chris Gammell:** You know, the last couple million were probably way out there, right? Yeah, right. And they had, you know, redone them as cost reduced. So maybe five to seven years. But fairly short. I mean, and so, Chris, you've sat with me. You know how irked I get when people say that they invented the home computer market. I didn't say it. I know this is going. I didn't say it. I was going to say. And the other people. The other guys. And we clearly created the market. But what we did badly was we didn't bring it to the schools and stuff. Whereas the other guys had a school program. Yeah. Yeah, totally. We had one person who worked with schools.

**Dave Jones:** So did the ability to do custom spin, custom chips like this give you a price advantage? Or was it more performance or a combination of both?

**Chris Gammell:** We could do magic. You know, it's just. Yeah. Yep. And there was just nothing that came close. So like when we did. I'll back up a little bit. There was when I first got there. We had a line of computers called the TED. And the TED was named after the chip called TED. And that meant text display. And Jack Tramiel had said, look, you know, I'm not going to compete with myself on the Commodore 64. We've already got that there. Right. We don't need another Commodore 64. We need something that distinguishes itself. Well, the text display was supposed to sell for $79 in 1970. But I mean, that's a whole unit except for the TV, right? Well, and drive. But yeah. Yeah. But it's still kind of a whole unit. And it was meant more for office. We had 121 colors. It would have been 128. But eight shades of black is still black. So it's 121. Right. If you do the Matrix.

**Dave Jones:** I'm looking at the Matrix now on the wiki site. Yeah. Yeah. The blacks all look the same.

**Chris Gammell:** And think about it. Nobody did a single chip home computer. You know. And this came out of Jack. It was in. When I was first.

**Dave Jones:** Weren't Sinclair getting close?

**Chris Gammell:** Well, that's what I was going to say. When I first got pulled in. Sinclair Rainbow. Was it the Rainbow? Spectrum. The Sinclair Spectrum.

**Dave Jones:** The ZX Spectrum.

**Chris Gammell:** And it had the little chiclet keyboards and stuff. I don't know that they had a dedicated chip. But I knew they were in the space that Jack Tramiel wanted to get in. So. Right. And that's where the very first version of it. And I have a video out about the C116. Which is literally the small little work of art. We changed the joystick connectors so they fit the housings. Everybody got mad about it. But meanwhile, it fit the housings and stuff. And it was a $49. 16K back in the days when a tube of 64K DRAMs cost you $99 just for the DRAMs. Right? Yeah. And so it was all based on a single chip. And so that was our magic. So when we did the C128, we did that in about five months from when we kind of started working on it. And management noticed we were working on something. To the CES show. And we had to have, I forget whether it's four or five chips done by then. So we had not just a chip. We had four chips at least. Where there are custom or major reworks of existing chips all running in parallel. Wow. Yeah. And that's how we broke the 64K barrier. It's how we did an 80 column. The 128 was almost the first home computer to have an MMU, a memory management unit in it. Except I screwed up and left out the supervisor mode. You know, the mode that only the kernel can use. And it wasn't until too late in the game where one day I'm in the programmer's office and he's grumbling about it. Somebody said, why don't you punch that in the register? And he's like, no, they're for the user. What? The user can write to those. So? Well, I can't stop him from writing to them. Oh. Yeah. And so it has an MMU, but it's only for the user. It's not for the system. But that's how we bank in 128K and all that stuff. And yeah, and so every chip failed miserably at least once during that five-month period. Five months is insane, though. That's really fast. That's crazy. And we did tricks. Now, remember, you know, learning about how the chips are made, there was a trick we could do called 1-2-3, which there was six layers. Seventh layer was passivation to the NMOS back then. But what you would do is you'd tell them to run a half lot, 1-2-3. And what they would do is they would run half of the lot, which cost about $300,000. They would run it all the way through with all the layers. But they would take the other half, which only had layers 1, 2, and 3, which are the diffusion slugs and all the stuff that's at the bottom of the chip, and they would put that in storage for us. And so if we needed a quick fix, we could come to them by trying to make changes just in the fourth, fifth, and sixth layer and put that on the 1-2-3 and get a quick patch. And we had to do that.

**Bill Hurd:** Yeah. And that's how they do some of those, like some custom chips do that now, right? Like the metalization layer, stuff like that, right? Right. Where they already have the pre-break logic. Right, right, right. So you just – Right.

**Chris Gammell:** Got it. And, you know, we ripped off – I'm sorry, is that the right word? We copied. No, we – Borrowed. Signetics had done the – Liberated. It's free. Signetics had done a PLA, which is different than a PAL. Yeah, yeah. But it's a PLA in and that. It's an and-or array instead of an or-and array. And I know we copied it because you walked in the one lab and there was Polaroid pictures all, you know, up on a piece of cardboard that they had taken. And they reverse engineered it and ours became – I forget what we called it. That's right. But, you know, the great gods of the silicon got us back. That was the chip then that had bad passivation. And for a while, that's one of the reasons the C64s were failing is you take this chip and put it under the microscope and it's got this purple creeping crud up under the passivation. And it's basically – Ah, interesting. It was like being allergic to itself. Yeah.

**Bill Hurd:** Right. So you're saying that there's only seven layers to those – To an NMOS. To those chips? That's right. That's right. Wow. I mean, because now they're like 20, 30-plus layers these days. I mean, it's crazy different.

**Dave Jones:** But still, you can do a lot back. Because how many transistors are we talking about here?

**Chris Gammell:** There was 150,000, I think, on – 150,000. Something like that.

**Dave Jones:** Which isn't a huge amount by modern standards. No, no. I mean, it's nothing.

**Chris Gammell:** Well, the drawers were still full of ruby-less. And the people still talked about the days. So I'll ask Chris. Yeah, a little help. Yeah. Well, time was they took this red material. There was no digital entry. They would hand-draw what the transistor should look like on the chip. And then they would cut the red film that would block the right frequency. And they would cut all those polygons out. And then they would photographically reduce it. And that became the exposure mask.

**Bill Hurd:** Right.

**Dave Jones:** That's the photolithography stuff.

**Speaker ?:** Well, I was going to ask this.

**Dave Jones:** What tools were you using? So you're saying there was no computer-aided design for these chips at all?

**Chris Gammell:** When they did the ruby lift. Now, when I got there – and this was cool. This happened like my second week there. There was the room where the chip designers were working. Now, remember, they've already been working on the TED chip. It was Bruce Ahern's, Dave DiOrio, and Eric Yang were the three fathers of that. And they're clustered around a microscope. And what they're doing is called probing. And they've got these real heavy bases that have this little cat's wire hooked to the oscilloscope. And they would slowly lower it to the surface of the chip and then scritch it back and forth and dig into it until they got to the contact they wanted. And then they'd look at it on the scope. So they're probing manually. So what had happened is we had a design rule check piece of software that would tell you if you got too close to each other. They said, oh, that metal got too close to it. Right. But it wouldn't tell you if the metal went right across the other one. It'd say, yeah, it's a great short. That meets the rules. Congratulations, you have a short. And that's absolutely what happened was the address 10 line shorted across A9 and A8 and A7. So you couldn't talk to the chip. Right? So we had a chip that worked. You just couldn't talk to it. So what they were doing on this thing, I hear the guy goes, okay, turn on the microscope light. Okay, it's an NTSC. Okay, off with the light. I'm like, wait a minute. Did you just flood that with the light, with photons from the microscope light and cause the bit into NTSC mode? He goes, yeah. I'm like, oh, I am so where I want to be. This is a cool place. That's awesome. Imagine not, you can picture a chip when you see people doing stuff like that to, you know, just banging it and stuff. So I also learned not to lean against that table that they were working on. Yeah, I leaned against it. Yes, I did. And like four pairs of eyes all look up at me suddenly and, you know, and I like ruined the entire morning's worth of probing or something.

**Bill Hurd:** Yeah. But what was the process geometry back then?

**Chris Gammell:** Do you know what that was? I mean... I used to know by heart and it was, we were just trying to get under, and I'm going to screw up the magnitude. I want to say one micron. Sounds, yeah. You think we were coming down from 1.6. And we were doing things then to try and make it, make the process work better and to shut off better so that it drew less power. And hang on a second, remind me about the 6502 200 ohm resistor thing here. I'm writing that down. So right in the middle of getting ready for the CES show, one of the chip designers tries to add this back bias generation to the part. And it doesn't work. The part works worse instead of better. We've waited a month and a day for a part that we can't use any. And I noticed that, and what happens is on the very far left, the whole left character column would not display, but then it would come on brighter and brighter as it went to the right. And what was happening was the back bias generator, which is basically a voltage doubler, right, with capacitors and stuff. It changed its voltage during the time you weren't talking to the chip. It would drift. Oh. And so what I did, or while it's outputting the VIC, so what I did was, you know, on the old ceramic chips, how were the pin one indicator, that slot right dead center at the time? Oh, yes. That's connected to the substrate. So I took a wire and I soldered it to the substrate. Oh, so you got access to the substrate. That's right. That little. Yes. And I grounded it. You got a connection. And I got it back to work as good as the rev before it had worked.

**Dave Jones:** So it didn't drift once you grounded the substrate. That's right.

**Chris Gammell:** So he lost his attempt to cut the power, you know, and I didn't care about power reduction, you know, in the middle of a CES cycle. And so that was one of the ways we fixed that one chip. And he's the guy that hadn't read the, you know, hadn't done his work for metastability. He, you know, he had his own clock. He had a 16 megahertz clock. We're running at 14.318. And his work, now this guy was really brilliant. I mean, he had the patent on some of the cells in the Motorola 68000, right? So down at the cell level, this guy, but up at the system level, right? Right. Just a bit. Yeah. So he said to me one day, he said, well, it'll always fail statistically, so it's not worth trying. I'm like, well, there's a big difference between one times 10 to the eighth and one times 10 to the 23rd.

**Dave Jones:** Yeah. Yeah. You could have tried a little bit.

**Chris Gammell:** And so what happened, you'd write to it, and only the data would go in or the address would go in, but the data that was already in the cell would write to the next address. I mean, it was horrible. And they were in denial about it, which there's a whole story about, you know, what he was doing. He was doing it in basic, and it seemed to work better. And then he told us, well, just write the same value twice. And so we started calling that a text and register because that's where he was from. But so what we ended up doing, the guy who wrote CPM, so the C-128 had C-64 Basic, had C-128 Basic, and it had CPM also, and a ROM monitor. So we were trying to really get all that out there. And the guy who had wrote CPM showed up with, like, two weeks to go before the CES show, and it doesn't run at all. The 80 columns just broke. And we were counting on CPM to run WordStar in the booth and all those things. And it turns out he had been using a real old version, and he would put an ice cube in this little cup and set it on the chip, and that's how he got the chip to work. And you said power doesn't matter. Red 7. Right, right. As a matter of fact, it was the buttercup out of a Mr. Hot Air Popcorn Maker is what he was using. So what we did was I built a little tower to phase lock the 80-column chip to the VIC chip. So instead of being at 16 megahertz, we phase locked it to the 14.318 and then took a shift register clock. And so it's like adjusting the dwell on your car. We can move the edge to the left or to the right. And on each one, we found a sweet spot because you couldn't have predicted it, but you tuned for it.

**Dave Jones:** So each one had to be tweaked.

**Bill Hurd:** Yep.

**Dave Jones:** So each unit, like each sold unit you're saying has to be tweaked?

**Bill Hurd:** Well, no, for CES shows. Oh, okay.

**Chris Gammell:** For the CES. Okay. So we got less than an eight-hour turn on those PC boards. And in 1980, that cost like $1,500 a PC board, which today would be like $6,000. How many lights are you talking about? How many lights? Two layers, three inches by two inches. Nice. Yep. It's just the fact they cooked them all off in one day. Yep. And so that was literally one of the ways we got to show the chip was we got in there and phase locked it. Mm-hmm. And that was what was cool there. Again, we're still that company of like the same 20 guys. Now it's grown to like 60 people, but 40 of them are watching us, 20, do the work. Right. And we weren't going to miss CES because the chip was broken. So, well, let's phase lock it to this. And, you know, that's what we fixed on Tuesday. And then Wednesday, I had to fix something else. You know, it was a continuous stream of that kind of stuff. But it worked.

**Dave Jones:** What board layout tools were you using back then? Or was it all type?

**Chris Gammell:** A guy named Terry Fisher was our board layout. But he had just gone to SciCards. And so the way SciCards worked is we actually would plug it into a VAX. We scrapped up one of the VAXes and plugged it into the, what was that called? The Unibus? Something like that. Right. That V-Bus or something. So when we did the TED, the one before it, the Plus 4, the 116, all that, that was hand taped. And the C128 was our first CAD produced PC board. Yep. And then what we did different on that, before, Westchester would make the board. And then Commodore Japan would lay it out again for production. So that would work with the pan assert, auto insertion and stuff.

**Dave Jones:** Oh, okay. Got it. Right.

**Chris Gammell:** So it's this whole unnecessary step. And forget trying to get through FCC and stuff, which I can tell you FCC stories. So one of the things I had done was I taught myself, you know, learned enough Japanese to interact well. And it kind of became our secret language. We could tell a boss right to his face he was a moron. You know, he, what? You know, and he wonders why the Japanese gentlemen are in the corner giggling, right? Yeah, yeah, yeah. So what we did was we laid that board out so it would work with the pan assert, which come in from like the side, and the American universal auto insertion. So it was also our first board that worked on any of the auto insertion tools of the day, whether it was in America or Japan.

**Dave Jones:** And we're talking about dip auto insertion here. Dip. Yeah, so this is like pick and place for through holes? It was actually inserted through holes.

**Bill Hurd:** None of this pick and place for rubbish. SMD. But it is for making through hole boards? Yep. Okay. Yep. Okay.

**Chris Gammell:** Yep. And I hadn't even seen an SMD chip at the time. Mm-hmm. Yeah. So, yeah, so those were the kind of things we were breaking at the same time. And it was also our first switching power supply. And, you know, I get... Ah, interesting. Why is that? Why? Well, it was just the cost.

**Dave Jones:** Why did you go from linear to switching? It was cheaper.

**Chris Gammell:** Yeah, see, so you guys had asked the question, why do your own chips because it's cheap? And, you know, a VEC chip cost us a dollar. Right? Right. And we'll sell it to you for 20. Right. And people used to kid us to say that the road between our two buildings was paved with bad VEC chips, you know? And we were quoted as just silicon. What do we care, you know? So, yeah, we had this tremendous cost savings we would do because we did, you know, the fact we had offices in Germany and if we were making for Europe or in Japan for making for overseas. And then to have such a handle on the production process. So, one of the ways where I learned to be a down-dirty designer, if you see the video on the 116, we sent them over there with, like, your standard three-hole regulator, right? Yep. So, they gave us back a, there was one of those, like, 10-watt resistors in parallel to it. Oh, enough. And I looked at it. And I go, well, it's going to go out of regulation unless you assume there's some, you know, a certain amount of minimum current. And I looked at it. And it's this grin starts coming to my face. And I'm going, that's the cheapest frickin' fix I've ever seen. You know, if you just assume that it always pulls at least 100 milliamps. Yeah, yeah, of course. Right? For the regulation? Yeah. And it's like, at that day, I think I stopped showering. You know, I just became a dirty designer at that point. Right. Yeah. It's like, anything we can do to, you know, get this cost in.

**Dave Jones:** Anything to do to ship and get it working, you know, at the cheapest possible cost.

**Chris Gammell:** Yeah. You know what the real metric was? And, like, I sent you that one schematic page. Let's talk about that next because there's something cool in there. But the real metric was, you know, people would tease us, oh, nobody used your CPM. Do you care? I said, no, because it worked correctly, you know. Oh, people still like the 64 better. Well, good for them. But if they want a second one, they can have one. Well, our only metric was, at these quantities, if you screwed something up, there's no hiding.

**Bill Hurd:** Yeah.

**Chris Gammell:** If you missed a timing, it's going to lay there and, you know, there's going to be a pile of 20,000 of them with your name on it. You know, they're in production. They'll come tell you and say, that's your name on that over there. And, you know, so we had to make sure that what we did do, even when we broke the rules, that we did it in a way that would still work at mass production. Got it. And the, hang on a second. So that Z80 clock I sent you. Right, which we'll post a picture to for everybody listening. Right. So this is an example of something that you should never do.

**Bill Hurd:** Okay.

**Chris Gammell:** Yeah. All right. Let alone the fact that, okay, we're going to make, you know, millions of them, because we made about 5.7 million of the 128. If you look at what had happened was the guy, the VIC chip designer, told me he could give me a Z80 clock, which was different than a 6502 clock. It had to go right to 4.9 volts in 10 nanoseconds.

**Dave Jones:** Oh, why is that? That was just the nitrous.

**Chris Gammell:** That's just the spin of the Z chip. Right. Whereas the 6502, it just had to be like greater than 4. Right. It just regular TTL-ish thing. And he said he could do it. And I know what he was trying to do. He was trying to create a voltage doubler on the NMOS chip to create a higher voltage so he could keep pulling it up past 5. Right. Because NMOS can only pull to 4 volts and then the gate turns off. Now it acts just kind of like a bad pull-up resistor. Well, turns out he couldn't. And so to do the Z80, we had to make our own clock. And at this time, I can't add any chips. I can only add transistors and jumpers. I think we've even already submitted for FCC, even though we haven't been to CES yet. So we're trying to get a jump on the F. And if you look at that circuit, what I did then, you know, if I did an RC, it wouldn't work. You know, it'd tail off too long to 5 volts. Oh, of course.

**Dave Jones:** Yeah.

**Chris Gammell:** So I put 12 volts on the base of that resistor. And so now when the open collector device opens up, it's a 12-volt pull-up. And it goes flying right past 5 volts, right? 5 volts, yep. Yep. And what happens is that transistor gets flipped around backwards. And now you're using the base collector diode in a way that that transistor was never made to do. Right? Yep. It's just, it's not an emitter follower. It's nothing. You dirty dog, you. That's the 1815.

**Bill Hurd:** That's the transistor you're talking about there?

**Chris Gammell:** Yeah. And so I walked around to every person. I mean, theoretical people, the chip design. I said, tell me why I can't do this. Tell me, because I'm going to make a million. Tell me why I can't do this. And we couldn't. We couldn't find anything wrong. But, you know, right up until production, I might have totally screwed the pooch. Not only, you know, I didn't care about being out of a job, but we wouldn't have been able to produce it. Right? Wouldn't have keep FCC if I had to add a chip or something. So that's an example of, like, a problem we would fix, you know, management would leave about 6 o'clock. And by 8 o'clock the next morning, we tried to have the problem fixed so that, you know, the problems wouldn't pile up that way. Right.

**Bill Hurd:** Right. You don't tell them how you did it. You just told them it's done, right?

**Dave Jones:** What's the problem with the FCC where you can't add a chip, but you can add transistors and jumpers and stuff?

**Chris Gammell:** Well, once you already submit your findings for FCC, you know, so you've done your pre-scan and then you've gone to a scan house and they submit it. Then you're allowed to petition it with, like, class 2 permissive changes or class 1, something like that. Right. And it's basically anything that's not rearranging the big things that the guy can see. So it's kind of like assuming he has kind of a little bit of farsightedness and, you know, if he can see the change, it's not allowed. That's how we were treating it.

**Dave Jones:** Right. Even though it could be pumping out. Exactly the same. Tons of crud. It doesn't matter. As long as you can't see it, it's not a problem.

**Chris Gammell:** I added seven transistors to this. I mean, the monochrome stone transistors. I've used it as an inverter, you know. Yeah, yeah. So, and that's why you see lots of little jungle chips like that second example I showed you. The C128 was the first computer in Commodore that had a reset switch. Reset switch sounds like a reasonable thing, right? Shouldn't be any, you know, everything starts from reset. But not if the VIC chip is in the middle of a DMA, right? Because he doesn't reset. Yep. So if you reset it and the VIC chip's in a DMA, the processor will try and start and it will crash. So that back-to-back open collectors, that actually makes a latch. It's like, well, if you're low, I'm low. Well, if you're low, I'm low. Let's both stay low. So look at that. It hurts my head to look at it to this day. And what that was was a latch that said, okay, you know, when the DMA's over with, then we'll go ahead and let the processor start up. But I only had like 6406s and 6407s left to wire together for a class 1 permissive change. So that's why you see those kind of weird chips used that way. It was like, well, we don't want to start over on FCC because we'll miss. Because, you know, if you made CES show in January, you had to ship by May. Wow. Right.

**Bill Hurd:** Right. For Christmas. Right. Yeah. Oh, right, right. You got to get to retailers.

**Chris Gammell:** Oh, it's all about the Christmas. Right. If you're not in the January CES, you've already missed that Christmas. And if you're not shipping by May, you've already missed that Christmas.

**Bill Hurd:** That's bonkers.

**Dave Jones:** Now, on the board, on the C128, which was your main machine that you designed there, which everyone knows about, you've got the two processors by the looks of it under two separate cans. Why is that? Is it the processor? No. You've got two big 40-pin dips under two separate cans. Yes.

**Chris Gammell:** That was mostly the mechanical, guys. Given that we started, you know, we set out what we wanted. Now, see, the Z80 wasn't in there all along, so it got added. And that's kind of a story unto itself.

**Dave Jones:** Well, actually, I want to ask you that after this. So let's, yeah.

**Chris Gammell:** Okay. So, you know, we had done things like one of the things that made the VIC better was when they made the chip for the R7, they put in a beryllium copper lead frame to get the heat out better. And so now that can said, oh, thank you for giving me the heat. I'll keep getting rid of it for you. So it was kind of like everybody had to play to play along with that. And then it was a matter of starting off with relatively good FCC designs. And what made me think of that was when Shiraz, the head of engineering at the time, had called me into his office to hand over the mantle of the FCC. You know, he had done all our FCC before then. So he calls me, and we start talking. And at one point, he stops, and he says, how do you know that? And I pointed, and I said, because I've read that book right there, and it was Henry Ott's book. And I know you guys have talked with Henry Ott. And back then, his book was in three separate books. But that thing was like the Bible for how he did it. So what you'll see is the things that Henry Ott used to talk about, they're in the 128 FCC-ness, if you want to call it that. Right. It's the essence of FCC. Right. And then some things we were just finalizing. Like, are you both familiar, if you have an aperture in a shield? Oh, yeah. Right? Yes. So you get the frequencies to get through the hole. But right next to it, a dipole forms in the metal.

**Bill Hurd:** Yeah.

**Chris Gammell:** Right? So you start seeing those things everywhere you look. You look at your microwave oven, which we didn't have back then. Yeah. And you start seeing Planck's constant. You know, like, oh, the holes in the, that I can see through are too small for 1.2 gigahertz to get out. You know, you start seeing it. So, like, we put, we tied the grounds together at a three-eighths. I won't go into the measurements, but we were just, at that time, figuring out how to make ground be ground at all the different frequencies in all the different places. You know, because, yeah.

**Dave Jones:** And the amazing thing here is that we're not talking hundreds of megahertz or gigahertz like we get these days. We're talking, you know, what, a 16 megahertz clock. And, you know. But there's a lot of lead inductance everywhere. The edge, right. I mean, it's, but it's all about the edge, right?

**Chris Gammell:** It's the rate, the radian frequency. Exactly. Yeah, yeah. Because FCC, actually, I think at one megahertz, we probably could have, like, put an amplifier, you know, a big horn on it and you can hear it. But up at 180 meg, yeah. And it was all about the radian frequency. And in our case, too, since we were jumping on and off the buses very quickly, hopefully, when they were both fighting for a bus, that also had a noise signature. So, yeah. And one of the things I used to do was I'd keep an AM radio on in the room, just real quiet. But I knew what the computer was doing. I could hear it. Like, you'd be over there going, gee, gee, gee, gee, gee, gee, gee. And, you know, it failed its ROM test or something. So people are like, how did you know that crashed? Well, I heard it. You heard it? And, you know, you're doing drugs again.

**Dave Jones:** Oh, goodness.

**Chris Gammell:** Did you notice that big red wire? If you've looked at a C128, there's a big red wire on there. On the bottom?

**Dave Jones:** On the top side? Yes. Oh, right. Yes. That is a component. That is the JW. It goes to a test point called JW?

**Chris Gammell:** Well, it is. You said it when you said there's two processors close by each other. We knew this was our final rev of the board. And it was one of the two times I did get threatened with being fired. So I loved it, right?

**Dave Jones:** You're right. Yeah, yeah.

**Chris Gammell:** Me and my boss started arguing. It's after CES. It's probably like around February. And, you know, so we're doing all the dirty little trick, you know, jobs to get out of production. And a problem cropped up where CPM would freeze while loading. And it was sensitive. The reason I cropped it up earlier is it was sensitive to different brands of chips in different places.

**Dave Jones:** And that's just a fact of life. That's nausea. Yeah.

**Chris Gammell:** Yeah. But I loved it because I like the scary problems, you know, the ground loops, the thresholds. And so what it is is on a Monday, we start talking and we argued. And he said, well, I'll just put somebody else on it. And I said, well, good. I'll just go home and take a shower. You know, so I had a great week, right? I caught up on my sleep, on my hygiene, you know, I got some change orders out. It comes into my office on fake. It goes, fix it or you're fired. And I'm like, okay, yeah, I can do that. And it took me, I lucked out. It took me about an hour to find that when the 6502 was driving the bus in the direction of the DRAMs, everything was good. I mean, if you look on a scope, you have to know what all the crap is on there. But I saw this little ghost of a chip, a little ghost of a spike on A10 when the Z80 was trying to do it. Well, when you look, if you look at the trace of that PCB trace, there's a stub that forms when one processor is driving it.

**Dave Jones:** No way.

**Chris Gammell:** It stands. You can sit there all day long and try it. You're a one. I'm a zero. You're a one. And so the way to get rid of a stub is to connect it back to the beginning. So now it's a loop. It can't reflect off the end because there's no end. Well, they look at me and think I'm nuts because now it's Friday at 1 o'clock, you know, around 1030 or 1130. He said, you know, I'm now fired if I don't. And they didn't blame me. And I'm like, I think it's going to work this way. And, you know, remember that what's at stake are millions. So they do a run of 10,000 over the weekend. So that's like a production run for a lot of people, right? This is the Bill Hurd is insane production run, you know, prove I'm nuts. And so unfortunately, the guy who was supposed to have fixed it instead of me, he had to come in along with the other people. And they had to work all weekend doing the test run. I didn't help. I went in with like a case of beer and handed them out and stuff, you know. But it worked. We didn't get a single failure from that. And so that was a one. And we never changed it because if we hand laid out another or, you know, if we laid out another board, we might just move the problem. So it was cheaper to leave the wire in there and deal with the devil you knew than the devil you didn't. So that became the thing. Of course. Yeah. But that was the, you know, the thing was like, no, you're not serious. A red wire, come on. Yeah, yeah. Actually, it was white when it started.

**Dave Jones:** How did you trace that down in an hour? Did you have a gut feel that it was there or were you just randomly probing around and you went, what's that little ghost pulse there?

**Chris Gammell:** Well, and I've spoken with actually Alan from Tektronix about this. He was at the VCF last year. And I used to do techniques, you know. So to answer your question, I am just going around everything first to make everything look good. But if the Z80 is what's breaking, then let's look at what's happening during the Z80 time, which meant I had to keep rebooting it, you know, because the Z80 fires first. And then the 6502. And so I'm looking at each line to say, well, also, what's different? And I'm going, well, there's a little garbage in here. But back then, you know, the Tektronix 2465, I mean, the best scope we had. Oh, yes. That's a good scope. Very nice. That's still a good scope. Yeah. So what I would do is I would do things like.

**Dave Jones:** That was almost like a storage scope for those who don't know. Is this one with the microplate CRT?

**Chris Gammell:** No, it's the one where you use your retinas like a storage scope.

**Dave Jones:** Ah, yes.

**Chris Gammell:** So what I would do is stare at it, right? You move the main part of the beam down off of it, right, but not where it sprays. And you stare at it, and you stare at it, stare at it. And then you look up at the wall suddenly, and you'll see it in black on white. I'm going, yeah, look, see, it's right there. And they're going, Herd's lost it. And he's staring at the wall. Oh, yes. He's doing drugs again in the 80s. Can I have your office when they fire you? You know, it's like. But that was it. And so what's funny is just about a year and a half ago, I ran into Hedley, who you've heard me mention, went on. And the first thing he said after seeing me after seven, hadn't seen each other in seven, eight years, he goes, Yeah, remember that time you saw that glitch and you tried to show it to me? And, you know, in other words, he didn't believe there was a glitch. So we had a reunion about three months later, and I ran into Frank Pilea, the guy that worked. And he said the same thing, only entirely different. He goes, Hey, remember when you showed me that glitch? And, you know, and this time he could see it. So they both said the same thing. But, you know, one's telling me I'm nuts and the other one's telling me, you know, I fixed it.

**Dave Jones:** Oh, that's brilliant. What's with all these jumpers I see on the board? J10, J11, they're like two exposed pads, like, you know, like a circle. Some are shorted out. Some are, were these for debugging or development?

**Chris Gammell:** I'm not picturing them, but they may have been for PAL versus NTSC, some of those kind of things. I'd have to look. All right.

**Dave Jones:** They look like just little, little jumpers for development. So you can get in there and cut traces and probe things.

**Chris Gammell:** Are they near the ROMs? For also, we were changing size ROMs and stuff.

**Dave Jones:** Oh, yes. Yeah. Yes, they are. Yes. There's some right down near the ROM. Right.

**Chris Gammell:** So, of course, we made our own ROMs. Yeah. And, you know, we made Atari's ROMs.

**Dave Jones:** And mask ROMs. Right.

**Chris Gammell:** And we made Atari's ROMs also. And if you remember that Jack Tramiel said business is war. One summer, I mean, one winter, we kept, yeah, yep, they're coming. Your ROMs are coming, Atari. Yeah. We know it's October. They're coming. Well, yeah, we know it's November. They're coming. You ain't getting them. And we did. We didn't ship Atari's ROMs to them. So, you know, the moral of the story is don't use competition for your critical part.

**Dave Jones:** Ah, yes. Which is still going on today. You know, like Apple will be using Samsung parts. Oh, Samsung memories. Yeah.

**Bill Hurd:** Actually, Bill, that brings up a story that I wanted you to tell that you told me at that event about the barrel of 6502s, I believe it was. Can you tell us that story?

**Chris Gammell:** Oh, yes. Chuck Petal tells the story, who I never met. When I got to Commodore, you could tell some really brilliant people had just sat in the chair before you. And it was like the cigar is still going in the ashtray, is how I used to say. And, you know, because there's these Vic chips and these 6502s, but they're gone. It's us. It's kids like me, right? And so because I was so busy and because I was a kid, I didn't say, well, whose chair is this? Tell me about this man. And I wish I had. Right. So I run into Chuck Petal through the VCF. And then we've done a video together with me and him and Jerry Ellsworth and stuff. And we start learning the backstories behind all this. And Chuck, you know, came from Motorola. And as he said, he's been kicked out of better places. Right. So him and Motorola, you know, kind of stopped getting along. And one of the things was, is he wanted to do a microcontroller. And I don't even think that the word was the vernacular yet. And I don't think it was. No. Or microprocessor. I'm sorry, not microcontroller, but microprocessor. Because a processor was about a 12 by 12 inch square board. And Motorola got to charge like $20,000 for one of those. So they don't want a chip that does anything like that is, you know, how it played out. And so he, you know, they came to, well, they came to MOS. I don't know the full story of who bought when where and who was where what. But to hear Chuck talk about it, then when they go to the to a CES show, they went to sell the 6502s, you know, because their attitude is like, take one home, try it. And, you know, and they got they got blackballed by the CES people. You can't sell out of the booth. Well, OK, we'll sell out of our suite. And they had so much traffic to the suite that when Chuck tells it, he's like, at one point, somebody asked, is this the bus to the commuters or to the MOS suite? You know, thinking, you know, a shuttle for that. It's really just a shuttle to the hotel. And you walk in and they really they had a barrel of chips and they were selling it. Now, they knew which ones were good. They had those off to the side. But, you know, that was the effect they went for is this barrel of chips to give you confidence that it's a real part. And Chuck said his wife would take the money and he'd hand you a 6502. And he gave he sold two, I think, to Steve Jobs at that show. Yes, that's right. Yep. Yep. So it's a and from there, I'll tell you the story offline about how it got so that it actually worked and stuff.

**Bill Hurd:** Oh, God. So a little bit more about the 6502 then as well. So so Chuck, you said Chuck invented that. But so is was MOS the the only maker of that or was that a license?

**Chris Gammell:** Well, originally, I think it was a 6501 and there was five guys. Al Sharpen, not Al Sharpened here. Oh, I should have written the names down. Bill Mensch, I know, is one of them. And Bill's kind of kind of reappeared later. You know, he owns Western Design Center and the arm got its early boost through the WDC thing. So he did. Oh, wow. That's Bill Mensch. So it was a group of five of them. So there was big lawsuits going on. And so part of it was we couldn't call it the 6501 because there was a 6801 in theory. And we had to change the pinout so it couldn't be direct. So so that's part of the early story. But then absolutely Rockwell and Center Tech. And those were the two main ones that that licensed it.

**Bill Hurd:** Gotcha. OK, so there were there were other sources. I was just I don't like I said, I don't I don't I don't know the history back then.

**Chris Gammell:** And so, you know, and the way I learned the the the the 6502 we had in the place, Estonia and Pennsylvania, we had what's called a rock box, a Rockwell system 65. So Rockwell, the people made the I want to say the shuttle. I think it was the shuttle back then, though. But but, you know, that's that's like five, 10, twelve thousand dollars or something. And so what was different between now and then is if you wanted to be an engineer, you couldn't be one out of your basement. You had to have somebody buy you that fifty thousand dollars worth of oscilloscope. You couldn't afford an oscilloscope. There was no eBay or anything like that. And and so to get started in a microprocessor controlled thing, you had to buy a development system. And, you know, twenty thousand dollars of 1970 money is, you know, is probably sixty thousand or eighty thousand. So, yeah, it was hard hard to get started with some of that stuff.

**Dave Jones:** So why did the tell us a story about how the C128 come to be a dual processor solution? Was it always going to be that? Why go the Commodore 64, of course, 6502 based? Why was the next one? I presume it was the next one after that.

**Chris Gammell:** It was the first one. We went to the plus four, you know, the Ted series. And then we came back to that. Yeah. And yeah. So other than to piss off the people from Commodore Australia, what had happened? We had we had a CPM cartridge for the C64. And I had the memo. I should put it up. I guess enough times passed where we had this huge failure mode where they wouldn't work on certain C64s. They thought it was the speed of some address multiplexers or they thought it was the timing of the VIC chip. And we figured out what it was. And what it is is when you have a Z80 on a 6502 bus, what happens is a Z80 goes clock, clock, pause, clock, clock, pause, you know, and does this. And so you'll catch it between it. It might go one, two, three, one, two, one, two, three, four, one. And if you stop and let a DRAM cycle happens, then everybody's happy, right? I mean, go away and eat. If you stop at between clocks one and two on a certain command, the buffers turn on. But internal to the Z80, the internal bus is floating. So now it's putting out an amplified one volt. It's amplified. I couldn't drag it down. I couldn't drag it up. I put a chip, you know, I'd drive right into it with an inverted version and things would get hot. And so it was just, it wasn't going to go anywhere. And we had to do logic to get around. Well, what was happening is one brand of 257 said, that's a low. The other one says, I'm going to oscillate. But everybody assumed a speed, right? Why would one brand work but not there must be speed? So now we've got this mode where, you know, it didn't work on the 64s. But guess what? It doesn't work on the 128 either, right? But nobody wants to hear that because marketing had already gone and said it's 100% compatible. Which I never said. Which, you know, we adopted. Okay, sure. Throw down the gauntlet. So the other thing then was that the CPM cartridge took like 0.6 amps. And on the Commodore 64, which is this big epoxy potted, you know, linear thing with the capacitors are already drying out. So if they dry out a little faster, who cares, right? Yeah, yeah. If the voltage goes down a little, who cares? But I'm on the first switching supply. And if I go over too much, it stops being a power, you know, it'll shut off. And so I didn't want to carry the cost in my 2-amp supply or whatever it was, like 2.2. Now it had to be a 2.8 and almost nobody would use the last, you know, the last of the current, 0.6 amps. So what we did was if by building it in, it only took us like 100 milliamps. So we're starting to go, yeah, we could build this in. We don't have to worry about the cartridge being compatible. We don't have to worry about the power. And then a third thing happened, and this sealed it. And that was that the guys from Magic Voice showed up. We had actually hired the guys away from Speak and Spell, from TI, and they were part of Commodore TI. And they had a product called Magic Voice. And what it would do is right when you went for the reset vector, FFFC, they'd say, we got the bus. Well, no, I'm a C128, not a C64. You don't know what to do with the bus. And it's going, but we got it anyways. Well, then let's just fail. Why don't Anna Wood? It would not start up because they jumped the bus. And what they were doing wasn't illegal because it's Commodore, right? But it didn't help. So what we did, though, and we did this overnight. Again, management leaves at 6 o'clock, and if they come back at 8 in the morning and I'm asleep in my office on my air mattress, they know I fixed it. And what we did was I called somebody up and got the opcodes, and I hand-punched them into the EEPROM. And then I took the inverter out of the reset signal. And so now it started with the reset line high, I think it was, and the Z80 would start first. And he would go, is that chip out there? Oh, bite me. You know, and what it would do then is set it up for C64 mode and then jump C64 and then the chip. So we used the Z80 as kind of a booter to see if there was something that was going to interfere with the 6502 booting. So we accidentally saved our asses, if we're allowed to say asses.

**Bill Hurd:** That's it. So was it that the Z80 was just already in there, though, or that's why you put it in there?

**Chris Gammell:** It was pretty much, if you've seen the computer at the time, it was like half man, half machine, half wire wrap. You know, so it was hard to tell where the experimental parts led off. And see, the way the 128 started, actually, you know, I've said that the 128 is probably the last of the 8-bit computers. You know, as far as I know. And what I mean is kind of add our quantities, right, because I'm sure somebody, you know, did some other ones, right? But the last of the big, of the 8-bitters. But because we had just lost Jack Tramiel and we were no longer getting instructions from top down, we're sitting around in kind of a vacuum. And I took a piece of paper. I had started on the LCD but jumped off to do this. And a guy named Fred Bowen, who's probably the real father of the C128, because he was on the project for at least a month before I was. But it wasn't what we call the C. I think they called it the D128 when he was on it. It was the last time a long-haired kid could take a piece of grid paper and one of those number five medium hardness pencils and basically sit down and do a design. And, you know, because it was. It was hand-designed off the thing. And we just, we built it. And it was when they saw the version that I was telling you about where I think we were running Wizard of War, one of those cool games. That's when management started showing it around to everybody. And they go, oh, you're geniuses. You're brilliant. Well, it's been working in a month. We just didn't tell you. But so what we did was we built it for, you know, got it rolling and then, you know, sought permission. And so what happened is I'd get to add a guy to my team, you know. And we'd hit another milestone. I could add another guy to my team and a programmer, you know. So we actually, we built it as we went along. But I think it was probably the last of a time when, you know, a person could sit down at a desk and do something. Right. Produce like a million, you know, six million or whatever. Nice. So.

**Dave Jones:** So was the driver that you wanted to run CPM? So you needed the Z8?

**Chris Gammell:** Well, we needed to be compatible with the CPM cartridge because marketing had said it's compatible with all of the cartridges.

**Dave Jones:** Right.

**Chris Gammell:** And so there was that.

**Dave Jones:** So just for, just to be compatible with one cartridge, you added a second processor.

**Chris Gammell:** And, and saved 0.5. So then the, the, the argument, you know, the good argument is, hey, look, I'll save half an amp. Okay. And look, it saves. You're right. Okay. So at that point, it's. Now, when we, when we went to do it, see one of the, to put the Z, the Z80s in on all of the units then. Because again, we do it overnight. Commodore, the way we put the nail in the TI-99's coffin was we started this thing that said, send us your, send us your computer and we'll take $100 off your Commodore 64. And people were buying the. The old trading. Yeah. They were buying Sinclair's for 50 bucks just to save a hundred, sending them to us. Well, during that time, the TI-99 had a problem where when the transformer got hot, the insulation would leak out and the, the frame would get energized, you know, like 60 volts.

**Dave Jones:** Oh no. Oops.

**Chris Gammell:** So they had to stop producing. And during the time they produced, we had, you know, we got their computers off the road, you know, they, because people sent them to us for a hundred dollar discount. So when they got it fixed, there was no programmers, no programs, no base. We had, we had absorbed it. So that was kind of how we were doing. So quick story on the compatibility. I forget what we were talking about right before then. But one of the things that we learned. Oh, so yes, because you had asked about the, would I put a chip in just to be compatible? And yes, we really liked CPM because we could, we knew we had 5,000 programs or whatever number off. Right. Right. Yeah. But one of the things we had done was when we started, we said, you know what, let's fix that crappy font ROM that's in the Ciccommonor 64. And we had stolen the ROM from Atari. So we called it the Atari crappy font ROM, you know, internally. And what it was, was it had real bad, um, um, the descenders, you know, the G's and J's underneath. Yeah. And the eye was in a funny place and stuff. So the guys cleaned up the ROM really nice. It was like, oh, hey, that's, that's nice looking. So the, meanwhile, the head of QA, who was a joke, what he would do once each project is he would stand up on a desk and say, it won't work. And then anytime a problem would come along, he'd say, see, I told you. Meanwhile, QA never actually found any of the problems.

**Dave Jones:** Yeah.

**Chris Gammell:** So I get a phone call and it's like, they're coming up for you. Okay. Thanks. You know, so I had a heads up. I knew there was a rabble coming down the hall for me and they had found a cartridge one work. It was called Koala paint. And it was a famous paint cartridge. I mean, you could just. Must've been Australian. Yeah. Right. Yeah. And, and, and, and it didn't work. It was like, I didn't know the details, but meanwhile, the movie dirty Harry is out during this time. And there's a scene where during the shooting and he's still eating a sandwich and stuff. So I grab a sandwich, you know, so what the hell let's, let's have fun with this. So here comes the rabble, but now I'm prepared for it. And one of my guys grabs it. And so now we're in the front of the rabble with the cartridge in its hand. And so we're the ones sliding it into the computer in, in R and D instead of my enemies. Right. And I watch and what it does, it goes Koala paint, you know, and it paints it a big K and a big O and a big A and I, and then it started painting the, the, the K blue and stuff. And you start looking and you realize what they were doing was taking our font ROM and making it real big to make the words Koala. Right. Well, so it paints the O and paints the A. And then it missed the dot on the eye because the eye had moved. Ah. And it did painted the whole background purple and it took three minutes to do it. So what we found was we couldn't even move the dot on the eye to be compatible with the sitcom or 64. Ah, that's crazy. And we fixed it like, you know, two hours later we brick laid you, I'm sure you've done that. You just have another ROM right on top and. Oh yes. And we had one wire. It's high for 64 low for one 28. And that was it. We had to make the font ROM twice as big.

**Dave Jones:** So that went into production like that.

**Chris Gammell:** Well, the ROM then became a, um, a twice as big ROM. So by the next rev of the board. Yeah. Yeah. You, you never saw it, but that was just an example of, of, you know, what we went through to try and try and get the compatibility. And, uh, there was one compatible, one issue that I missed. And I remember the three seconds I made the decision. I think I'd make it the same way where the 6502 had these registers where it could run at twice the speed, two megahertz and stuff like that. And in C64 mode, they had no business being in there. And we did not want to create a super 64. We did not want to screw up the legacy of, of, of our father. Right. So don't make up. So we wanted it out there. And I remember risk is everything. If I had made it so the registers went away and never came back until what a power cycle or a reset. Well, what if when you did that, the register still didn't come back because the way the chip works, you know, the substrate synergized or something like that. Yep. Then I'm totally hosed. Right. And I'm in 128 mode with no registers. And so I decided to leave them in there in an area where you're not supposed to write to, um, rather than make them go away. Well, sure enough, three months after we shipped the, the program escape from fractalus came out. And when I disassembled it, watched it run the person instead of doing a decrement X and transferring like 24, um, values to the VIC chip, it went the wrong way. It incremented. And so it wrote all 256 values, most of them garbage. So what it did was it wrote upwards and it's going garbage, garbage, garbage, garbage, right across our registers and it garbage the rest. And then finally it goes back to zero and then writes to one, two, three, and four, you know, but it literally wrote 300 times to get to two 20 registers. Oh, so they did it wrong. But you know what? We, there was no law against it. So, but with that said, I don't think we sold, you know, two less computers because of it. So, uh, yeah, we weren't going to open it again for that. What was the Commodore LCD? That was probably the computer that should have been made instead of the 128. And I say that as, as the lead, you know, the designer of the 128 and the lead farmer, but I had started on it and we owned our own, uh, LCD company back then. Uh, it was called Eagle Picture and we were the only people that made LCD glass in the States. Again, cheapness, right? We can do stuff. Nobody else can.

**Dave Jones:** And this was going to be a laptop. I have one.

**Chris Gammell:** And even the keyboards. Oh, you've, you've got one. Is there any video of this? Uh, yes, there is. Go, go to c128.com. You'll, you'll see some. Now it's not working because I won't turn it on because as long as I never powered up, it might still work. Right? The moment I do, it will collapse the wave function and it'll either be a water. Schrodinger's laptop. Schrodinger's laptop. You got that exactly right. So I don't turn it on. But even the keyboard was like, it's beveled and it has this real cool feel of which for, you know, the early eighties, you didn't have this pop feel, you know, when you press the keys. Well, um, so I had been working on, and that's where I actually got the MMU from that I used in the 128. Because, um, we knew word editing and stuff would be the kind of things you do on this. And I didn't like the amount of time it takes for you to see, to see you paint the characters into the screen. Right? Like when you scroll, it'd go, you know, at one megahertz. Um, so what I wanted was that you just slid a window around in memory and displayed it. So that, you know, if you're on the 300th line of the editor, right, you set the pointer to 300. And, and so that's kind of what I was working on at the time. And then I jumped to the 128 and a guy named, um, uh, Jeff took over the, uh, the LCD. And we had hired Jeff for, um, from Bell Labs because we knew we were going to have a modem in it. And, and Jeff knew all about part 68 to part J and stuff. And, and so, um, uh, so he, he took that over and they did, they developed considering that they, that I was getting the bulk of the resources. And then they got, you know, kind of what was left. Um, it was, it was ingenious compared to the 128. The 128 was just, I used to call it nine pounds of poop in a 10, in a five pound bag. Cause, cause I couldn't quite fit 10 pounds of poop in a five pound bag. Right. I'm sure you always say poop too. Yeah, right. I had to practice that one, you know, it's like C-mail. Yeah, right, right. Um, yeah.

**Dave Jones:** I gotta say, it's not a bad looking machine at all. I know, it really is nice. I do like the keyboard. Oh yeah, it was a winner.

**Chris Gammell:** Yeah, absolutely. And, and, uh, so, so Jeff Porter takes it to, um, CES. He gets orders for 15,000 and then our new CEO, um, Irving, no, Smith. I, I, I've forgotten his name. I'm sure it's, uh, due to therapy. Um, but he had been like head of U.S. Steel supposedly. And so now he's head of our company. I bet that translates well. Of course. So you know how to make steel, you know how to make computers. Yeah. Yeah.

**Bill Hurd:** Playbook stuff.

**Chris Gammell:** And then later U.S. Steel said, no, he never worked here, but that was after he was gone, you know? Um, and in Brian Bagnell's book, you'll find an episode where supposedly I punched him during a Christmas party. Um, there's a lot of exaggeration in that. Uh, but the, but what he did do was he, um, talked with the president of Tandy and the president of Tandy told him that there's no money in portable computers. And he canned the project in a way that only the top guy could can it, meaning you won't get anybody to help you make the box. You won't get anybody to shoot the plan. You know, all those things won't be available to you. And so I had outside my office, I had that article and the article that said the highest selling Tandy product that year was their little stupid black and gold. If you remember that old, uh, um, um, LCD machine Radio Shack had, it was this flat little limp stupid thing. Oh, the 100. Yeah.

**Dave Jones:** The model 100, that was a step was like one of the highest selling.

**Chris Gammell:** It was the highest selling that year, according to the article. Portable computers ever. So, so it was massively successful. And so I had under it, it said, this is what you get for listening to your competition.

**Dave Jones:** Yeah, exactly. I've got two of those sitting right behind me. Oh, do you? Yeah. I've actually done some videos on those. Yeah.

**Chris Gammell:** And see, we were talking with Mitsumi about this little technology nobody had heard about called a CD-ROM. Oh, man. Oh, man. And we were all real big fans of the Hitchhiker's Guide of the Galaxy. You know, Douglas Adams has some great books. Yeah. All right. And, um, the, so we were going to couple the LCD with this massive storage device, much like a Hitchhiker's Guide and, you know, like having an encyclopedia in your pocket. Right. Who, who, who'd have guessed? And all that just kind of went up in smoke when the, when the, the, the head guy, Marshall Smith, that's his name, uh, pulled the plug on that. Gosh darn it. Yeah. So, yeah, that's crazy.

**Dave Jones:** That was, yeah. And that, and that didn't happen because a, the head of Tandy told, told somebody at a

**Chris Gammell:** party. Right. Right. I think it was dinner. Yeah.

**Dave Jones:** At, at a party that there's no money in laptop. Was this before or after Tandy had actually released the Model 100?

**Chris Gammell:** It was selling. So, because it wasn't long after that.

**Dave Jones:** So he came along, so he, so he bullshitted him and said, we are, we're not making any money on that. Right. Right. He's useless. Don't bother. Right.

**Chris Gammell:** Because it was only a couple months later that the, that the, uh, that the report came out.

**Bill Hurd:** Yeah.

**Chris Gammell:** So, yeah. And, you know, this is when we're missing Jack Tremiel about this time, you know, it's just because we were from a company where, like I said, you know, who you worked for, you know, it was, he, you, you didn't have to report to him to know he was your boss. And then, and then here we are inventing our own computers and stuff like that. And, you know, so it turns out about 50% of us, you know, ended up being alcoholics and the stuff, you know, myself included. Yeah. I, when I tell the story, you know, I, if I get to say, and I haven't had a drink in 24 years, then I, then I'm okay telling about all the crazy stuff. That came first. Right. Right. And, and, and, but if 50% of us ended up that way, you know, and I'm the only one counting because I know everybody, um, it's like, well, did you have to be an alcoholic to do well to work there or did working there make you an alcoholic? Yeah. Right. Cause or effect. Right. Right. Right. Yeah. And one thing I know though, if you've ever seen the movie Deer Hunter and that's that we're going way back. It's, it's about some guys that went to Vietnam and came back and were addicted to like playing Russian roulette. Right. Yeah. Had to have that stress. Well, that happened to us. I mean, I ended up working in like a trauma center and stuff in my spare time. And it's just like, it's, why are you here? Cause I used to work at Commodore. Need the juice. Oh yeah. Yeah. Yeah. You know, I've done thousands of ambulance calls and stuff. And you know, what's cool about it is you get to troubleshoot people. You know, if you're into troubleshooting a computer now, now put a 15 minute clock on it and the guy just rolled his car on the turnpike. Go. You know, and there was one time I got to use the line where, um, we'd had like two mass casualties in a row, which meant the second one we had no equipment for cause we'd used it on the first one. So somebody else, somebody's like quite a morning. Right. And I'm like, ah, I used to work at Commodore. Yeah. No biggie.

**Dave Jones:** Oh, I love it.

**Chris Gammell:** But you can only do it once. How many, how many Commodore LCDs are there out there? Um, Jeff Porter has two and I have one. That's all we know of.

**Dave Jones:** Is that it? Yeah. Is that all you know of?

**Chris Gammell:** I had the only one till, till, till the, till the guy doing, um, um, the Viva Amiga, um, film that's going to come out at some point. All right. He was at Jeff's house and Jeff had the batteries in it from 1986. So there's that corrosion. Oh, he turns it on with like 24 year old batteries in it.

**Dave Jones:** Oh no.

**Chris Gammell:** Yeah.

**Dave Jones:** Cause I'm, I'm looking at what, what looks like an article for it from some magazine, presumably. Right. And it was actually announced and shown, wasn't it? And then you just didn't go ahead. Yeah.

**Chris Gammell:** Well, I've got pictures of the booth was half the booth at 85 CES was the 128 and the other half was the LCD. Ah, that's right. So we pulled the plug after we'd already done all the hard work. I'll tell you, you know, for Commodore, that's the hard work, you know, cause the easy work, the distribution chains and stuff, they were just huge, you know?

**Dave Jones:** Yeah.

**Chris Gammell:** So.

**Dave Jones:** What a shame.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, so you worked on the, so you worked on the, uh, 128, the Commodore LCD, the plus four.

**Chris Gammell:** The plus four had started as the 116 and then the 264, which was supposed to cost $79 and didn't have silly software. And the 364, which talked, and that's where we had the TI speak and spell guys that come out. Got it. And, and so what there was there was a desktop, you know, we, in other words, we'd have beat Apple to the desktop motif. If, if, if I were to say that's what it was supposed to do, cause then it would talk to you as you moused over things and stuff. So I got it. So then they marketing sat there and goes, well, we know how to sell a C64. Can't we make the plus four into a C64 or, you know, make the 264. So they, they added that bad software and they reject the price up to 299 and then said, well, this, this sucks. It doesn't sell very good. And, you know, then they left it at that. So meanwhile, they came out with a 232. When I say they, I mean other parts of the company started chipping in like Commodore Japan. But at the end of the day, I'm the one that had to sign off on the final. So I, I, you know, my involvement might only be 10 minutes, but it's the last 10 minutes. But we did the 232. There's this thing called a C16, which is a one-sided PCB in a Vic, in a C64 case. And, you know, they just use solid. Single-sided PCB. Single-sided. Cause it saved a dollar. Yeah. And it's got jumpers. How many jumpers on that? Yeah. Several. But, you know, auto-insertion. And there's a, so in the end, I, I, I was father to seven or eight variants on it. Oh, so here, let me tell you about the other time I was going to get fired because when I mentioned the, being the father of it, so, you know, as I said, I, I had joined and the, the design's done. The design is done by the chip people kind of if you, because it's a single chip computer. And I, I did get to add a reset circuit because they tried to do it with just a non, uh, non-schmitted 7406. And I said, you can fire me if you want, but you need to. And, and so they were, they, they thought, you know, cause Jack Tramiel said only nine chips. And I added the 10th chip and I was still working there on Monday. So they said, Oh, Oh, okay. That works. Um, the, uh, let me get back on track here. So, um, oh, so, so at that point I'm kind of more like the, the caretaker of this, you know, cause sorry. So as we were going through all the steps and what I'm really doing is learning all the steps of how to get a computer out at, at, at Commodore. So it's kind of like wax on wax off time for me, right? Cause I'm learning on and release the chips and release to this release. So that, and, um, but, but I'm still not really the designer, right? So then one day, uh, we plugged a joystick in the guy from Commodore Japan had shown up with the joystick and the, the, there's two stories involved with that. The first story is he, we looked at it and said, that's too flimsy. He said, no, we said, yes. He turned his head and you hear snap. And it's me going, and what I did is I had snapped a $15,000 soft tool joystick to make the point. Right. So he got back. I mean, he taught me some bad Japanese that got me in trouble, uh, in Tokyo one time, but that was, you know, that was kind of part of my whole reputation. You know, the long hair guy that actually, you know, kind of did it as the, and, and he understood he did, he did make it stronger. But then the other thing was we plugged it in to the one 16, again, a beautiful little computer. And we got these sparkles on the screen, bad ones. And so I grabbed the, you know, joystick and I hold it up next to the monitor saying, well, if it's that bad, it should crash the processor. Oh, just crashed the processor. What had been on the schematic all along that I didn't really take ownership of was they had used the data lines directly into the keyboard, the, the, the membrane keyboard. Oh, yeah. Right. Right. Yep.

**Dave Jones:** So if you did that on the original Tandy, I think.

**Chris Gammell:** Yeah. So if you look though, D zero and D one sneak off the keyboard to go out the joystick for the fire button.

**Dave Jones:** Oh, that's nasty. So now you're extending the bus right out there.

**Bill Hurd:** You're yanking down the bus basically. That's like how the joystick works.

**Chris Gammell:** More, more like, yeah, yeah. You, you would, uh, with the right pull up and stuff, you would do a read cycle and either it'd be ground or high or whatever RF it had picked up on the one. Yeah. Oh, that's horrible. And so, you know, I, I sit there and as I'm looking at the schematic, cause I pull schematic open and I see the little D zero and D one. And, and the truth is I've been carrying the schematic around enough that I should have seen it. So by, you know, ownership was really mine at that. So, and I laughed, I said, ah, I see it. I said, my boss was not as amused as I was. He said, fix it or you're fired. All right. This is the first time he said, I said, whatever. Yeah. You don't stop talking to me. So, um, he comes back in, uh, an hour later and I'm sitting there playing a video game and he thinks I'm taking my lunch. Cause you walk around common or half the people anytime we're playing video games and you don't know if they're working or playing, you know, or testing something. So I'm sitting there playing and he says, so I thought, you know, something to the fact that, you know, he told me to fix it. And I just point and I go on playing. He gets a little more pissed and I point again. And finally I point to the fact I had had one, the techs put a six foot long, um, cord on it. I had taken the case off of the monitor and I had wrapped the cable around the yoke. Oh, you know how scary looking the yoke is to the civilians, right? So I've wrapped this cable around there to prove that it's no longer sensitive to the thing. Nice. So, but that was, he didn't say, okay, you're, you know, you can stay working here. He just grunted and puffed on a cigar. Right. Yeah.

**Dave Jones:** He grunted and mumbled off. Yeah.

**Chris Gammell:** Yeah. So I had that wrapped around the, I mean, cause you know, if you're going to prove it once and for all, that's the way to do it.

**Dave Jones:** So, so how long did you last at Commodore? You joined in 93 ish, sorry, 83 ish.

**Chris Gammell:** 83 ish. Yeah. Um, I lasted through how many computer cycles? Um, it was about three years. You know, I, I, I, I left because I thought Commodore was really about to go down the tubes quicker than, than, and, you know, I didn't know that having a $10 billion company means it'd hang around even if it was jerked off life support, you know? And, and later I felt bad that I had left, you know? And, and honestly, at that point they're like, well, we don't really need Bill back, do we? Remember when he broke the joystick? Yeah. So, um, so yeah, it was, uh, um, it was kind of like dog years, you know, engineer years. It's, it's, uh, um, it, it was very fast moving, very high stress, um, you know, for that three years. Um, whereas later I, you know, they did get to slow down and actually kind of, um, as, as Dave Haney said, cause I said, well, I, I told him one day, I said, I wasn't trying to change the world. I was just trying to meet the schedules. Right. And he said, but we were trying to change the world, you know, with the Amiga stuff that came out. And, and that's what was sad because they had something there they could have if they had a company that backed them properly. Yeah.

**Dave Jones:** So to wrap the story up, what killed Commodore in the end? Uh, Jack Tramiel leaving to me was.

**Chris Gammell:** Oh, okay. Right. So, so, you know, again, there was.

**Dave Jones:** Because there was no, no direction that sort of took over. Right. There was no one who sort of. Right.

**Chris Gammell:** And, you know, there had also been a philosophy of, of fear and resource, uh, battling. And so I likened it that, um, see, we used to have things that, they're urban legend called Jack attacks, but what they mean is, um, Jack Tramiel would not suffer fools. Let's let's, that's how I interpret it. Right. You're good or you're gone in the higher up you are, the more, more you in good means that you listen to Tramiel also. Right. And, um, so with, with him gone, with the wolf gone, the sheep are just multiplying left and right. Oh my God. You know, we, the QA manager should have been fired the first time he did a drop test without the box, you know, this guy shattered a $40,000 printer. We know because we saw the pieces slide out from under the door, but the cool thing was he said, and the second and the third one didn't do any better. And we're like, wait, you shattered our $40,000 printer and then proceeded to shatter two more. And you still work here. And he did. Oh, goodness. He was that guy that was QA that, you know, got to stand up on the desk. Right. So what's amazing though, if to, to kind of wrap up, as you said, is this is what 35 years ago, 30 years ago. Yeah. Yeah. It's a long time. And, and the fact that anybody's even heard of it amazes, I'm speaking on behalf of a bunch of my friends amazes all of us. Yep. Some of us just think the world's insane. So that's how they describe it. And, you know, it's, if it wasn't for the internet and the globalization of the knowledge, nobody would know.

**Dave Jones:** It would have been all, yeah, it'd be all forgotten.

**Chris Gammell:** Yeah. Totally. Yeah. Oh, I'd be, see, my wife already thinks that I worked at a company with a dozen people and we sold a hundred computers. She has no idea. Right. Right. Yeah. Go on. We're at a computer store, right, Bill? Yeah. Right. Right. Right. Right. At three in the morning, I'm like, no, no.

**Dave Jones:** My husband sells computers. Right.

**Chris Gammell:** And, you know, at three in the morning, I'm having a nightmare. Must pass FCC. No. All right. Yeah, yeah, yeah. CES. It's next week. No. Oh, God. The suicide rate after. You should have seen it. See, after a CES show, people really would.

**Speaker ?:** Oh, jeez.

**Chris Gammell:** They'd walk around in dazes and stuff and you'd like lead them and be like, go home, take a shower. Yeah. Even if you do nothing else, take a shower. Please. Right. And, you know, we got used to eating dinner like Christmas, you know, because CES was first week of January. Yeah, that's a killer. Right. So, you know, we got used to eating out of aluminum foil in the lab, you know, just one of us, if he went home, would bring back food for all. And I just remember one time, you know, how I used to use a radio to listen to my computer. Greg Berlin. Yeah. Who did the, Greg's six foot eight, this hulking big guy, shattered my shoulder for me in a brawl. He did the floppy drives for these. And so what he would do is he would lay his head down on the floppy to listen to the heads because when they get stuck, he'd hear it in the back. And you'd walk in, here's this six foot eight guy just fast asleep with his head on a floppy drive, you know, and he would just have like a microwave hot dog near his nose, you know, and he'd wake up five minutes late. But that's how we were. We wouldn't have known what to do with Christmas. But then January, you walk around and you go, you know, I gave a, you know, a finger in life for this. What? So we used to say life after CES.

**Dave Jones:** Right. Right. So you weren't around for the death throes of. No.

**Chris Gammell:** No.

**Dave Jones:** Commodore, that final hour.

**Chris Gammell:** And when I tried to watch Dave Haney's deathbed vigil.

**Dave Jones:** Yep. Video, which he filmed, for those who don't know, he shot, he carried a video camera around on the last day they shut down. Was that the. I think it was.

**Chris Gammell:** Yeah. That the thing. Yeah. I think like the very first thing is that he hits like Greg Berlin prying chips out of a computer. You know, it's like the, the sacking of Iraq.

**Dave Jones:** Right. Yeah. Right. Yeah. Yeah. Yeah. Everyone's ransacking. Yeah. And PCs, they're ripping out the 6502s. Yeah. Yeah.

**Chris Gammell:** The DRAMs he was taking.

**Dave Jones:** Oh, the DRAMs. Oh, yeah. Bloody expensive DRAMs. Yeah. Yeah.

**Chris Gammell:** And see, and I had wondered where all these weird, you know, because we would still get together once a year. And, and you can tell that we were a tight group that we still get together after 35 years, you know. Yeah. And these are still people that if they really called me and asked me to mow the lawn, I probably would once. You know, I mean, we're still good for it. But the, but then there would be these people that I had never seen and I didn't realize what they were. They were the people from that last act. So what I, I call Commodore a Greek tragedy in three acts, you know. And the first act was the days of the pet and the Vic chip. And it was like, it was Camelot, right? The sun's shining. The king is there. Money, money, money. Right. You know, the part of the wizard played by the, the ship designers, you know. And then the second part is, you know, when we get into the LCD and the C128 and that, and the third act is the Amiga and, and then the things going downhill. And so it wasn't until I read Brian Bagnall's book that I, I actually knew what had happened, you know, during that time. Right. Because I had lost contact with him. Yeah. And it's just sad, you know. And so, yeah, if, if I seem bitter, chances are I am.

**Dave Jones:** They, they just flat went out of business. Like they just went bankrupt overnight or something.

**Chris Gammell:** I think they sold the name off repeatedly.

**Dave Jones:** Yeah, they sold the name off.

**Chris Gammell:** And there was like some chips not being kept in storage correctly that went with it. So they were actually no good. You know, they weren't in nitrogen and stuff. And I know that Commodore USA, Commodore Gaming got the right to use the logo as part of Commodore Gaming. And it was black and white, I think, several years ago, but that was only for game machines. And then Commodore USA got it. And then that, the gentleman passed away, I believe that was head of Commodore USA. And so I, I personally don't know where it's at, but you know, the Commodore logo is still, I'd love for it to become part of. Someone owns it. Right. It'd be great if it was public sourced or something. So you could actually put it on a website or something. Yep. That'd be nice. So if people want to see more about this though, speaking of the logo that's not on my c128.com website, that's mostly just old stories and stuff. And a form there, if you're trying to fix one of your old computers, there's a lot of guys there that can help with it. Also, I think lemon.64 or something like that. And then, um, got it. Oh, there's, there's a name we haven't talked about. One, one last QA story for you. Do it. There was a, um, our, our QA man, you know, QA department never actually pressed all of the keys on the computer. So it turns out the shift Q didn't work. Right. So that was our first thing. But what the, what the programmers found when they did a, um, a V, a, a, a, a, a, a, I think they did a reversed V. There was a line over it. And so they kind of quietly, you know, uh, patched the font ROM. Well, the reason they found it was they were making the Easter egg and Von Ertwein, the guy that did CPM, which someday I got to tell you a story how he rewrote a CPM sector on a disc the night of CES up in the suite using a hand disc editor. I mean, the guy was just phenomenal. Oh, nice. So, but they, they, you know, we founded ourselves for, for that when they were making the Easter egg. Now, when I got the ROMs, uh, to release, I said, yeah, it turns out there was a problem. So I'm releasing them to, uh, MOS on such and such a date. I'll get my lot back. And the head of software said, I think I should be the one to release it. I said, okay, you need to release it Thursday. Like I just said to the production, and then it'll go through and I'll have it on time. He said, yes, no problem. So, Hey manager, how's that coming? I will, uh, you know, I will assess the situation and do a release upon validation of the, and so the Monday comes and goes that says, meanwhile, a memo had come out that said, stop breaking into the offices because you could climb over the walls and get in the offices. And it all but said, this means you bill hurt. Cause I had had to break into my own office once by punching through the wall so I could reach in and unlock it. So I was always the guy that, you know, was, and, um, so I broke into his office and I took this thing and I released it to MOS without telling him it was right in his pencil tray. Right. And so we let him get to the meeting where I said, how's that coming by the way? Well, it's under evaluation. I just shut him down. It's a long haired kid.

**Bill Hurd:** I go, you lie.

**Chris Gammell:** I released it. I broke into your office. Listen, so he's trying to get me fired for the breaking into the office thing. Um, but the, but, uh, but the, the Easter egg then that those guys were working, meanwhile, the font ROM got me nicely, but the, the Easter egg was, um, make arms, link arms. Don't make them. I believe. Right. And, uh, then under it said software and the three guys that worked on it. And then it said herdware and I had nothing to do with that. The guys did that as a present to me because my last name's herd and I'm doing the hardware. So, uh, I, I managed to get my hands on the herdware, uh, um, domain name and, and trying to do, I'd shown Chris and stuff. I was going to say herdware.com. Yeah. So trying to, you know, it's, it's a work in progress, but my whole thing is if, if I can in any way, um, help somebody find that enthusiasm that you heard me talk about tonight, you know, and it's tough when I talk with kids, like, you know, back when I was an entrepreneur and we'd have kids come in and I tell them about how drive and, and, and ingenuity would be, but then I had to stop and go, Oh, and stay in school kids. You know, so I'm a dichotomy. I can't say, Oh, you can get anything you want. I mean, stay in school. Uh, but, but if I can give that to somebody these days, you know, how an op amp works or, you know, you, so you broke your transistor. How do you know, you know, that kind of thing, then that, that'd be cool. So that's kind of what I'm working on, on the, and FPGAs. I love FPGAs.

**Bill Hurd:** And so, yeah, we should mention that, uh, so Bill does some awesome videos both for Hackaday and for his own stuff. And, uh, and there's the, uh, there's that modular hardware stuff that those boards that you're making.

**Chris Gammell:** Those are, oh, and Hackaday's been, that's been a great ride. Um, did I tell you how, how I ended up with the Hackaday last story for the evening here? No, sure. Um, how did I end up with Hackaday? I was watching the Adafruit, the thing they used to do on Saturday nights. Oh, yeah. Yeah. As an engineer. Yep. Yep. And they would give away, um, something, you know, they'd have a little quiz and, you know, I never participated when it was something you could just buy out of stock. Right. Didn't need $3 saved on a midget or whatever they were called. Um, but then they had been to the Open Hardware Consortium in MIT and they had a bag full of swag and here's something you couldn't buy. Right. Actually, that had an amp hour, uh, I'm staring at it right now.

**Dave Jones:** I have it. And I had one of my micro rules.

**Chris Gammell:** That's right. Yeah. And now I'm staring at it because that's, that's the first time. Yep. Yes. And it's got the little detachable. That makes sense, huh, Bill? Yeah. Yep. Yeah. So, so, um, uh, so yeah, so that's where I saw you guys, but there was also a, uh, a beta test for datasheets.net. And I ended up talking with Ben Dallaire from there about, well, you know, as engineers, what I do is I make piles and I use them like this, you know, and he teases me because I still say data book, which I guess that's. Yeah. Yeah. Yeah. Right. That's a data sheet. Um, and so that's what led to, you know, they're, uh, they're owned by Switchrack. What's the name of it? Power Switch? Uh, Supply Frame. Yeah. Thank you. Supply Frame. Supply Frame. I don't need a long, it's been a long night here. Switchrack. No, I like that. Yeah. So they're owned by Supply Frame, which owns Hackaday. And that's how I ended up writing a story for Hackaday, literally about, you know, the five month hacking of the, uh, of, of, you know, getting ready for the CS show. And that's how I ended up with those guys. You know what they noticed? They say, well, you, you seem to like to talk. Why don't you make us a video?

**Bill Hurd:** Yeah. So that's good. Yeah. So, uh, and that's, and those videos are under your, uh, is it just the Bill Hurd YouTube account? Is that right?

**Chris Gammell:** They're under the Hackaday ones or the good ones. And. Oh, right, right, right. Right. And, and so, you know, I'm, I'm, I'm, and I've made every mistake under the sun. I, I think one day I showed a, uh, I was my forked take and I showed the, uh, the carriers pushing the, the, uh, PN junction off the end of a diode instead of over the, the, uh, the, the center, you know, over the tunnel. And I'm like, Oh, great. Everybody thinks I don't know how to make a diode, you know, work. So as I'm sure you guys know, you just have to be so careful when you make those things that, you know, those words live forever when you do it.

**Dave Jones:** Oh yeah. No, I, yeah. You've, you've got to learn to accept mistakes because every video, every one of my 700 videos I've produced has a mistake in it. I'm sure.

**Chris Gammell:** I just refuse to do math on, on camera anymore, you know, cause. Oh yeah.

**Dave Jones:** Oh, totally. Yeah.

**Chris Gammell:** If I don't have the number written down, I'm not saying it, you know, it's a, but the one feedback that I did get though, somebody said, well, this guy's approach is less than perfect. And if you've listened to anything I've said tonight, that's a compliment. I haven't done a perfect thing. Exactly. Cause. Absolutely. Me too. Cause you're always, it's always a compromise, whether it's time and cost materials, FCC, you know, it's totally. So guys, it was great talking with you. It's, uh, it was awesome, mate.

**Dave Jones:** Where can people find you? Are you on Twitter? Cause we love when people are on Twitter.

**Chris Gammell:** I'm on Twitter, but I didn't know people would listen. So I, you know, only do it when Verizon stops talking, you know, stops working and stuff. Um, the, the, the C one 28, a lot of people there.com and the herdware. And then also my presence to Hackaday. So it's, I'm going to be doing more for them and it's bill heard at Hackaday.com. Oh, it's one L and bill. Remember the whole computer incident. Is that your legal? Well, my legal name is William.

**Dave Jones:** Is it legally one L? Oh, right. So Bill's just there. Right. So yeah. Right. Right.

**Chris Gammell:** So yeah, that worked, that worked out well. I, you know, I didn't know that I was making a, a handle that 30 years later would allow you to search the internet and find only one person instead of every single William in the world. Yeah. Which there's at least 40. Yep. So. Right.

**Dave Jones:** Excellent. It's been awesome, Bill. Yeah. Thank you. Thank you for sharing your stories.

**Chris Gammell:** I'm going to have to go curl into a fetal position now after all this therapy. It's like. We had the world by the horns. We lost.

**Bill Hurd:** We had a good session today, Bill. You just go and you card your teeth on that.

**Dave Jones:** Do I send the chat to the same place? That's right. Right. And here's the important part. Which photos should we put up for you on, on our Ampower site? Should it be. The shorts. A classic one on your wiki. The shorts with the bear, with the bear chest and the long hair and the bandana. Maybe we can mash a couple together.

**Chris Gammell:** You know, I was trying to get my, my cat to help pose for one, but she had nothing, nothing to do with it. So Chris, did you get the one I sent?

**Bill Hurd:** I did. I did get that one. We might have to, we'll definitely include the other, the wiki pictures. Oh yeah. We'll get that on there somehow. It's whatever you think.

**Chris Gammell:** I didn't want to scare the audience. You know, it's like. Hey!

**Dave Jones:** The things they did in the summer. It's okay. It's the 1980s. Yeah.

**Chris Gammell:** Well, yeah. There's a picture of us like chugging tequila in the Vegas airport because that was legal back then. I put beers through the metal detector and they're laughing. We're seeing how many it takes to trip it. And the only thing was we couldn't get on the plane with an open bottle of tequila. So three of us stood there at the ramp chugging it. And the stewardess, everybody's laughing their asses off while we're doing it. And that thing, you know, that's how we came back from CES 85, you know, posted. Wow. Nice. Excellent. All right. Guys, it's been real.

**Dave Jones:** Thanks, Bill. It's been awesome, mate. All right.

**Chris Gammell:** Until next time or when I run into you somewhere else, we'll carry on then. Yeah, definitely. All right. Talk to you then. Catch you next time. Bye, guys. Bye, guys.
