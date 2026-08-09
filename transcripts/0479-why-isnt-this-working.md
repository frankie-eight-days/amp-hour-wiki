---
episode: 479
title: Why isn't this working?
url: https://theamphour.com/479-why-isnt-this-working/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released February 13th, 2020. Episode 479. Why isn't this working?

**Christopher White:** Welcome to Ampedded. This is Elysia White with Christopher White and Chris Camel. Hello.

**Chris Gammell:** Sorry, I was going to... No, that's good. We haven't done this very recently, so... Hello. Hi, Embedded listeners. I'm Chris from the Amp Hour. Amp Hour listeners. Yeah.

**Dave Jones:** Well, here we all are. We're doing it. Yeah. Here we all are.

**Christopher White:** Okay. But this time we're going to talk about firmware, right? Yeah. I mean, that's the plan? You have been doing firmware. You're a hardware engineer. You know that, Chris, don't you?

**Chris Gammell:** I do. And you know what's really crazy is like I have... So I've been kind of... The month of January has been me reviewing my yearly goals and just kind of like what... You know, yearly goals or whatever they are. But one of the things that's on there is just like more firmware projects. And I've been consulting for about 18 months now, a little bit more. And the thing about that with hardware is it's really choppy, right? So unless you have like a client that just has lots and lots and lots of boards, it's really choppy. It's... You do a board. You build it. You test it. You know, assuming you build it. And then if you have a firmware person you're working with, it's just like you hand it off and there really aren't any changes unless you mess something up or, you know, you have a revision. And then that's great for the client. That's like a best case scenario is you don't... You haven't messed it up and nothing... Everything works as expected. But from a consulting standpoint, as you both know, it's choppy. And that means that income is also choppy. And I have to have a lot of clients and lining it all up is kind of just logistically really tough. Not to mention that I want to get better and offer better services to clients. And so I was like, well, I should really be taking on more of the firmware aspects. So I've been doing that and it's been great. This firmware stuff, it's got legs, I think.

**Christopher White:** Why'd you go for firmware instead of FPGA?

**Chris Gammell:** That's on the table too. I mean, it's just... You're going to be a full stack product designer? I think it's just more, you know, doing more things and learning more things. Like I had this great revelation recently within the consulting world that like I get to just, you know, like I'm not learning from scratch and I'm not having a client pay me to learn, but there is so much to learn. There is. And I feel like in the consulting world versus my previous corporate gigs, it's really varied. I mean, you really, I mean, both of you know, you know, you're doing machine learning and all of the various things that you're doing. And it's, I mean, there's so much stuff out there.

**Dave Jones:** Yeah. I mean, it's kind of like working at startups. I mean, I remember the difference between working at a startup and working at the big corporate gigs was always, it's big corporate gigs. You got to work on something, but it was a very small little corner. And maybe it was a small little corner of something that had been around for a while. And so there wasn't really that much to learn except, you know, good programming practices and all the high level stuff. But the first real startup I worked at, it was like, oh my God, there's, okay, we need a, we need a motor controller. Oh, okay. We need, we need this, this sensor hooked up with spy. Okay. We need this flash thing to work. Uh, and it was just one thing after another like that. And unless you get into the right startup, that's doing something from scratch that, that has all these pieces, you're not going to get an opportunity to really learn all those pieces unless you kind of have little, little jobs all over, all over the place.

**Chris Gammell:** Yeah. I mean, from a business perspective. Yeah.

**Christopher White:** There's less pigeonholing in startups. You have to do breadth, but you also have to do depth, which is what makes them so hard.

**Dave Jones:** I mean, they always turn into, if they're successful, then they quite often turn into the big corporate things and then you're responsible for eight lines of code for the rest of your career. Optimize that please. Yeah.

**Christopher White:** That's painful though. Going from a startup where you're the third or fourth engineer to supposedly, you know, just being an engineer and you're like, but I designed this system. What do you mean you want me to make another spy driver? I already did that. Um, but you, okay. So you're, you're doing firmware, um, and you made a concentrated effort to learn, not just to modify what somebody else had done.

**Chris Gammell:** Yeah. So I've been hiring tutors and, um, I started with like a personal project, um, just kind of getting back into it. I've obviously bugged both of you, um, bugged other people on the, the embedded Slack and have been just generally trying to put more focus on it because it's, it's, uh, it's not something that just, I could hop back into. And, you know, and so past projects I've been doing, I've done firmware in the past. It's not like I've never done firmware before, but sometimes it's like, well, I'll just throw an Arduino IDE kind of at this problem or that problem. And it just doesn't work at that point. You know, you don't get debugging. You don't get a lot of things.

**Christopher White:** What was your personal project?

**Chris Gammell:** Um, it was a, uh, light up wristband. It's still in, it's still in progress actually. Um, so what I was really doing is I went on LCSC and, um, I found that.

**Christopher White:** What is LCSC?

**Chris Gammell:** Oh, that's the, uh, so, you know, JLC is like a, uh, uh, uh, PCB manufacturer. Have you ever heard of them?

**Christopher White:** Let's go with now.

**Chris Gammell:** Okay. So like they're a very, very low cost, um, PCB manufacturer. And, um, they also have like a DigiKey equivalent, but the interesting thing is that they have a lot of parts that are Chinese only, like they're only available in mainland China, but they'll actually export them. And so a lot of brands you wouldn't know, but a lot of like kind of weird data sheets and maybe not super well-documented functions, but just they're cheap stuff. I mean, like really, really, it's stuff that goes into consumer goods. So for example, one of the chips that I was looking at, it's a 433 megahertz, um, transceiver, not even transceiver. It's a, sorry, it's a transmitter. And so it's a really simple, like I squared C style, uh, interface, but it's called like just data stream or something very, very generic. And, um, that's what goes into those really, really cheap quad copters. You can buy like the toy ones and not super well-documented, but you can use that. And it's like, that's like 10 cents, 15 cents in quantity, like not even local, not even high quantity, like like that's like a hundred quantity. And so, um, I did that. And then I also grabbed like, then like STM 32 stuff is really low cost on there too. And so I grabbed the lowest cost STM 32 I could find, which was a F030. And that's like 30 cents in a hundred quantity. So I think just like really, really low prices for what I'm used to and just wanted to see what I could do with it. And so the idea was making a remote blinky thing, uh, that I could synchronize with lots of people. So that's kind of, that's the thought. Um, that's what I've been working on and, um, we'll see how it goes.

**Christopher White:** Is this for conferences or for raves?

**Chris Gammell:** This is for, uh, an event that I'm throwing. Yeah. The next summer. Ah, so yeah, it's, um, it's still, still in the works, but, uh, that was kind of my platform for like, oh, well now I can dig into, you know, STM 32 and just arm cortex M0. So I'd used them before on, like I said, like using an Arduino ID, everything's kind of abstracted away. It's not like I hadn't used similar kind of micros and stuff, but when you make that shift over, and I think we've talked about it before, it's, it's, it's, it's a drastic shift, you know, and it really is, uh, to, to be deep in the register sets and dealing with data sheets directly and all the things that you talk about in an embedded FM. Yes.

**Dave Jones:** And the tools, I mean, the tools are far more brittle and they've gotten better, but they've gotten better to the point of, well, it should have been this way. Like 15 years ago. So it got a long way to go. Um, how, what, what parts are you finding the most frustrating?

**Chris Gammell:** Well, um, I went a little bit, I swung a little bit too hard. I think I, um, I went to like, oh, I'm going to do everything with GDB and, uh, I'm going to do everything in Vim and, you know, do compilation. And it was really, it was a little overboard to be honest. But the thinking there was I've, you know, I've used, I've used IDs before and I never really knew what all the stuff scrolling by was, you know, like you see. And, and so I always talk about the 2am problem. Like what happens now where I'm on a job working on something? There's a deadline, 8am the next morning. It's two in the morning and I just need to get something working. And there's just some weird compiler flag that I, I just don't understand because I've never used anything on the command line prior to that. And it felt like I really had to have that experience in order to dig myself out of my own holes, you know?

**Christopher White:** Okay. So Vim, which I think when you told me that I laughed initially, um, cause there's only one real thing I know about Vim and it's escape colon Q.

**Chris Gammell:** Colon WQ. Yeah.

**Dave Jones:** You learn that one real fast or else you control Z and you, you know, back out the hard way. The problem is I type so fast that every time I do that, about 70% of the time I do colon W1 instead of Q. So almost every directory on my computer has a file called one in it. And I just come across them occasionally, delete them and realize, oh yeah, that was when I was in VI. It's like a trail of, it's like breadcrumbs, you know? Yeah. I should have a script that periodically goes through and deletes everything called one.

**Chris Gammell:** Right. Yeah. That, that probably wouldn't have disastrous consequences.

**Christopher White:** I like the idea of the 2am problem that you want to be able to solve just about everything yourself, but that's a hard.

**Dave Jones:** Here's my problem with it. Here's my problem with it. And I think it's, I think it's laudable.

**Christopher White:** Is it 2am? No, no, no. Because you don't, you don't see that time of night.

**Dave Jones:** That's goes without saying, but there's always going to be a 2am problem. You don't remember having come across. Like there's so many things with, like you're saying with C flags or configuration or linker maps or whatever, where there can be just a small error. It's always going to take you hours to figure it out. I'm just, I see where you're going with that. And I just wonder if it's the right application of learning energy.

**Chris Gammell:** Well, I can say in the, I can talk more about it later, but in the interim, I have swung back hard the other direction. Okay. And I think it's like, it's really good for level setting, right? It's like, oh, okay, this is the way it used to be. This is the way it can be. And you can build up your own setup. And I will say that some of it is influenced by my tutors as well. Right. So like they were doing that anyway. Well, one of, one of the two was doing that anyways. And he's really helpful, but he's like, you know, this is a great way to learn this. And, and I agree it was, I mean, and I knew I had, so it's not until the summer of this year, I knew I have time to do that kind of thing. And so I was like, okay, yeah, let's, let's go for it. I think it is good to have that, that baseline of experience, but yeah, you know, it's, it's arguable if it's the best way in general, you know, like there's all these tools are built around it around other, other workflows. And it's kind of, it would be kind of audacious of me to think that, oh, I, I'm going to come up with a better thing. You know, I'm going to customize myself. I really need this because I'm so high performance, you know, it's like, that's not going to be the case.

**Dave Jones:** I mean, there's certainly reasons to stay in the command line world, but I, and it's great to have seen all that stuff. And I think, I think it is valuable to go through that and say, okay, this is how this works. Just so you know what the things are. If you do have to eventually look into it.

**Christopher White:** And there is no one right way.

**Dave Jones:** Of course. Right.

**Christopher White:** And if you can see as many different ways as possible, you can find a path that works best for you. And I don't use VI, but it's not like I don't respect people who do. I just don't know those things. And of all the things in the world to learn that hasn't been high on my priority.

**Chris Gammell:** Right. Right. And I, you know, so I've always been, so I made like a conscious effort to do full Linux, everything these days too. And a lot of the, a lot of the traditional tool makers, they just ignore it. You know, they say, well, sorry. Yes. Switch to windows. I mean, you've talked about it on your show too, of like switch to windows. That's what firmware is. You're in windows. And I kind of reject that a little bit as well. I mean, I think that I know that they're, they're, they're definitely getting better about it. And I try and support tools or support vendors that are, are targeting Mac and all options out there, Linux and everything. But, um, it's, it's very frustrating to be told that like, no, I'm sorry. You, you know, you must conform to this entire worldview as well. And I, I don't like that, but that's also kind of snobby, I guess, of me. I don't, I don't know.

**Christopher White:** So what else have you learned from your tutors who you actually paid?

**Chris Gammell:** Yes. Yeah. I think that's really critical. Um, so I view tutoring kind of like, like, so I play piano and, um, I feel like if you're going to get a tutor, I had many, many people, you know, I said, I put it out in the world. I was like, Hey, I'm a Twitter. I said, I'd like to get some tutors. I want to make this a thing I'm getting better at. And a lot of people were like, Hey, just give me a call. I'll, uh, you know, I'll tell you what's going on. I'll help you out. And that's like super sweet, but it's actually on me. Like I, if I don't have skin in the game, I don't think I'm going to, I don't know, it's just like when you're not, when there's nothing, there's no value transfer. I feel like it's, it's limited in terms of like, it's not like I'm thinking that they're dependent upon my dollars, but I think it's more of a, it's like this, this clear exchange of value, their time for my dollars. And that is a two way street. They're going to show up because they know that I'm, I value their time. And also I'm going to work hard and go through with the, um, with the assignments they give me and follow up with them because I'm paying for it. Like, otherwise it's just a big waste of money. And, um, you know, that's, I just always think that's the, the, the right way to do it. It's not like libertarian, like, Oh, everyone should, you know, whatever. But, uh, it's, uh, I just, I just, I think I view it in the same way as the music world too. You know, you wouldn't ask a piano teacher to just show you a couple of things, uh, because you need some help. It's like, no, it's like, there's a very strong lesson culture there. And I was trying to structure my, my learning in a similar way.

**Christopher White:** You have a podcast, right?

**Chris Gammell:** Uh-huh. Yeah.

**Christopher White:** Where you talk and you give away your information and insights for free to people who don't give you any skin in the game.

**Chris Gammell:** That's true. But when I, when someone asked me, Hey, Chris, can you actually show me how to do a layout specifically? I say, yeah, I can actually. I have tutoring as part of my online course that I do. And I also have an online course people can pay, you know, that's like, it's two way

**Dave Jones:** street, I think, you know, I totally agree with that. I find that to be the same kind of psychological thing with myself. Like I've taken online music courses before and the transition in my mind from just fooling around to, Oh my God, I have an assignment to do. And this person, this nebulous person who runs this course, who I'm never actually going to meet, probably not even going to talk to except over email. You know, they might grade my assignments, but it's not a, it's not a conversational thing. I still feel like, okay, I have to, I have to do what they say and I'm paying for this. There's just something that shifts in your mind when you have a formal relationship with, with instruction.

**Chris Gammell:** Totally. Totally. I mean, yeah. I mean, look at the numbers for MOOCs, right? So like massive online open course, like those are free and they're wonderful resources. But I think even all these years on, there's still 4% completion rates and like, and that's because that's about how many people would follow through all the way when there isn't any monetary, I don't know what it is. There's something psychological. And, um, I think I've mentioned to both of you before, I'm kind of a self-help junkie. So I think there was something I read in books about this too. It's not like this is my only, my personal idea, but like, this is just, I feel like that's the way to move forward. Like, have you, I mean, Chris, you do music, but Alicia, have you ever done, uh, tutoring or similar stuff before?

**Christopher White:** Not very much. I learn out of books.

**Chris Gammell:** Right. Yep.

**Christopher White:** And as far as when people ask me for help or I definitely was one of the people who said, yeah, Chris, call me anytime.

**Chris Gammell:** Yeah. And I did a couple of times. Yep.

**Christopher White:** But I, I mean, I'm very, I'm kind of the first hours free if you want my attention. Although I shouldn't really say that because.

**Chris Gammell:** Uh-oh. But. Bleep that out, Chris.

**Christopher White:** Um, I mean, with the, if there is going to be a client relationship perspective. Um, but yeah, I, I guess I don't take very many classes these days. I used to.

**Dave Jones:** You did the Udacity course that I did this year. That's the car driving one or the car? The ML one.

**Christopher White:** I see. I was, I was paid in services for that because I, I did some, uh, work for one of their other classes. Um, I used to take community classes all the time and I guess I am looking at taking, um, some makerspace stuff here, but.

**Chris Gammell:** Is this after Wendell and Lenore were on and they were talking about their awesome classes they took?

**Christopher White:** Oh man. I still want to go to that.

**Dave Jones:** I know, less of a class and more of a science vacation class. I don't know. That was a fun, that was a really fun episode.

**Christopher White:** Uh, no, it's more from, um, Robert Lang's origami episode where he said he had a laser printer and then, or a laser. Cutter. Cutter. And it made so much difference. And I was like, okay, I need to really like do this. I need to try that. And so I found a makerspace with a laser cutter.

**Chris Gammell:** Didn't you, didn't you both almost get a laser? What's the, uh, desktop one that you, yeah. Didn't you get one or you're going to?

**Christopher White:** We, we were signed up until the CEO said I wouldn't buy it from us. And then I canceled our order after many latenesses.

**Dave Jones:** I think he was, it was by way of apology for the delays. It was very much an apology. It wasn't to don't buy this, but, uh, yeah, the delays were long and it was expensive. And we had other expenses that were coming up.

**Christopher White:** So 3d printers.

**Dave Jones:** Yeah. 3d printer was a fraction of what the globe would cost.

**Christopher White:** Um, yeah, but I read so many books and I read, get them from the library or I guess I do buy some of the books, but that's always how I've learned. So it's not, I totally see the tutoring relationship and I understand why paying for a class makes more sense. But I'm not wired that way. No.

**Dave Jones:** I just need some guilt motivator and it's either, it's either an instructor who I'm paying, or if I have a project that I'm working with, with somebody else, like the album I'm working on with my brother, I'm highly motivated to work on music because we're both trying to finish it. And if it was just me trying to make a record, I think that would be bad. It'd probably take me 10 years. But, um, so, you know, having another person involved in a project or just, uh. Yeah. We're having a goal, right?

**Chris Gammell:** Yeah. I mean, I've got an event coming up in the summer. I need to get something done for that event. Like that's a pretty hard deadline. Yeah. Nothing like a deadline to really motivate, right?

**Christopher White:** Yeah. That I do agree with. And it is really nice to be able to talk to someone when you're learning something, either an expert or a co-learner. Just to unsnarl those things that only takes them 10 minutes, but takes you three hours to work through.

**Chris Gammell:** Yeah. And I find another thing that, uh, so a lot of time when you're like nebulously trying to figure out, well, I want to, so I say like, I remember, I think, I think either one of you two said it, or maybe someone on the embedded Slack said it, I was like, I want to get better at embedded. They're like, what does that even mean, Chris? That doesn't mean anything, you know? Like, uh, which is true. Um, but, uh, I think it's more of, you need direction then too, you know, you, okay, well, you want to get better at writing C code. Great. Um, maybe you want to, you know, have a better, people then help you form that and say like, well, maybe you want to get better at memory management and understanding how memory structures work or whatever, but have a project there, you know, have something you're working towards. And that's another thing that the, the, um, that the tutors really help with. Um, so I had like, uh, one tutor was a little bit less experienced, about five, six years of experience, but I actually really appreciated that as well. Cause being closer to the beginning of their journey too, um, if you read about like learning styles and stuff like that, one of the first things that happens is you lose, you lose the feeling of like being confused and being, uh, kind of like lost.

**Christopher White:** You've totally lost that, haven't you, Christopher?

**Dave Jones:** Christopher I am confused and lost all the time. We're going to, we're going to talk a little bit in a little bit. Cause I, I'm actually engaged in a parallel effort to what you're doing, Chris, but, uh, please go on.

**Chris Gammell:** Yeah. And I think that like, so having someone close, you know, you talk about like beginner's mind as well. And so like, that's, uh, that's like a, a nice thing, uh, that you can approach every problem with to, to be like, oh, well, I am a beginner. And so you have this open mind around learning and that's kind of what they're talking about. But then they also say it from the teacher's perspective of you need to have that, that perspective because you don't remember the feeling of like struggle and like cluelessness. And so I'm not saying my tutor was clueless, quite the opposite, but he was closer to the beginning of the process. And so it wasn't like advanced topic. It was more like, well, let's get you blinking an led. And he was super helpful. So, okay.

**Christopher White:** So your project, blinky lights, um, radio, radio.

**Chris Gammell:** Yeah. Yeah. Oh, that's it. Yeah. And that's another problem is that simultaneously I was like, you know, I should really do more RF stuff too. So you're just, yeah, real smart, Chris. Yeah. Well, and so I went and bought a $3,000 VNA and, you know, and, uh, learning, I have like, I have a lot of books as well and I, we can talk about books and, and, and things like that, but, um, it's, uh, there, these are deep. You may, may have noticed that firmware is a, uh, is a kind of a deep field. So is RF. Uh, so. Really?

**Christopher White:** I've heard there's black magic there that makes it deeper.

**Dave Jones:** Right. Oh, and I was, you have to make little squiggles on your PCBs. Yep. Yep. Definitely that.

**Christopher White:** And if you're doing something worn, you have to deal with battery subsystems. Are you just buying that off the shelf?

**Chris Gammell:** Um, that actually I'm fine with, but it is a, it's a battery. Batteries are easy for me. I mean, that's kind of my background.

**Christopher White:** Well, but I mean, there's not just the battery, there's the, how do you charge it? And how do you tell people their batteries going low?

**Chris Gammell:** Oh, I see. Yeah. This is a, um, uh, disposal. It's, you know, it's like a, it's a replaceable, uh, like a coin cell. So that makes it real simple. But then there is voltage conversion and boosting and, you know, all that other stuff as well. But, um, again, that's kind of, that's kind of my bread and butter every day. So I, I'm not that worried about that, you know, but if I was, if someone was coming to me and be like, Hey, I really need help with a battery system, then I'd have to like approach that with beginner's mind and be like, what is the hard part of, of getting started with thinking about current flow? And, you know, that's the kind of stuff I deal with, with contextual electronics. Right.

**Christopher White:** How much are you still working on that?

**Chris Gammell:** Uh, contextual electronics?

**Christopher White:** Yeah.

**Chris Gammell:** That has been a pretty background for me lately. Uh, uh, it's still going, there are still students. I still, you know, do tutoring and helping and, uh, but there has not been any new coursework in, uh, in a long while. I've been really focusing on consulting and, um, and yeah, it's, that's been, you know, it's, it's basically me. I was looking at contextual electronics and I didn't feel like I had a ton more to offer in terms of, uh, in terms of like my knowledge and it's kind of like, uh, cashing in on someone's background knowledge. And I was like, I really need to go build up my skills so I can offer a course that has some firmware in it. Or, you know, um, when I did the first round of contextual electronics or the second, I suppose, um, there was that exact same part, the STM 32 F zero three zero. And because it's a cheap, cheap part. And, but I hired, um, two people to help me with firmware and, um, and I don't want to do that anymore.

**Christopher White:** You also have a, a forum for consultants. Do you talk about that?

**Chris Gammell:** Uh, I mean, it's, it's there, there's an application. Well, uh, we can link it in and, um, but yeah, so that is actually the contextual electronics forum. There's like a hidden semi-private section there and, uh, yeah, it's like invite only. And so you got to apply, but if people are interested in consulting or are consulting and want to, you know, interact on there. Um, I started that because the 20 months ago or whatever, whenever I was deciding to go into consulting, I was just like, so scared and wanted some free help, I guess, to contradict myself from before. Uh, but, uh, I just wanted to talk to people and, you know, discuss things. And everyone I talked to was like, yeah, I really had trouble when I was learning this. And I obviously talked to both of you. You have great experience there, but, um, you know, just kind of like, why, why have people asked these questions over and over again, why not make it kind of searchable, but still private enough that people feel comfortable discussing some detail, some amount of details, maybe not every detail.

**Dave Jones:** Well, community help is a different kind of help than focused individual help. You get a lot of experiences that can contradict each other, but if you get kind of reinforcing opinions, it's like, okay, that's probably meaningful.

**Chris Gammell:** Yeah. Yeah. Yeah. And I mean, right now, I mean, so we have people that are doing firmer stuff and a PGA stuff and RF stuff and, uh, and recently there was a big layoff at analog devices. And so a lot of chip designers are coming in now too. And, um, which is unfortunate. I was very sad about that, but, um, you know, it's interesting just hearing how, you know, hearing a chip designers consulting efforts is going to be so radically different from someone who's like doing firmware, maybe up into the software layer. And, um, it's all still technology. It's all still very, um, complex work, of course, but it's just like, think about like, a chip designer has to have access to like a $50,000 software license when, and a firmware person might be working at completely open source, you know, GCC and VIM and whatever else. Right. And so just the scale differences there are quite stark sometimes.

**Dave Jones:** Well, and the cost for firmware continue to drop. Sure. Right. I'm not sure that's happening on the chip design side of things.

**Chris Gammell:** Right. Yeah. Yeah. Yeah. And I mean, similar things, RF, I mean, you buy equipment, like if you want to do microwave design, my goodness, like I, I found a, I had a talk a couple, uh, back in last August, I suppose. Um, and I, I have a, I had thought I'd found this like great looking VNA and it was like, I was like, Oh wow. It's only like, like $3,000 or something. I don't know how my brain just like completely went sideways. I was looking at this beautiful thing. And then like, I kind of zoomed out and I'm like, Oh, that says $564,000. Like that's more than a, you know, a house in many cities in the United States, you know, like that's insane. But it's a 60 gigahertz VNA that like only very, very small amounts of people in the world need.

**Christopher White:** So back to firmware. Mm-hmm. What was the hardest part that was a surprise? What did you, I mean, you, you went in with, you know, Arduino expectations and some expectations that it was going to be harder than that. Cause you've heard other people talk about it. What, what was a surprise that was hard?

**Chris Gammell:** You know, I feel like it's, it came in stages, right? I think that the, the tool chain stuff and just like figuring out what's going on, uh, is, was hard to me. And I feel like one thing that I think I expressed to both of you at some point on the forum, on the Slack and I've said other places too, is I'm always second guessing myself, you know, so it's confidence pieces, right? It's like, I, I, I, this must be bad code. This must be bad code. This isn't compiling. I don't know what's going on. Oh my God. It, you're so stupid. Why are you doing this, Chris? And then it turns out the cable was broken, you know, or something like that, or, or the driver wasn't installed properly for the, uh, so I think it's just the, the amount of assumptions on the way towards that first blink. They're so, are so large. And, uh, and because I was, you know, arguably this would be also because I was going in a non specified route. I wasn't going like STM 32 using cube software and using everything and like following the instructions on windows. I could have done that. And I could have, I arguably should have done that, but because I wasn't now I'm off, I'm out in the, you know, the wilderness and just trying to like Google around for answers. And that is just, that is a, a tough thing to do. And would I go back and tell myself to do that? I don't know. Uh, I think it was valuable. I think that hiring tutors was a result of, of that frustration. But I think also that kind of learning sucks sometimes. And I think that that is part of the understanding of like, uh, you're going to have some struggle. Uh, but I forget who I talked to about it, but they're like, you know, part of the thing that you start to realize is that if I just stay calm and I keep trying new things and I keep stepping through problems, I'm going to figure this out because there's no other, there's no other, there's no other option. And, and like that, so, so much of it is just mindset at the beginning. Um, and.

**Christopher White:** The stay calm. They don't get frustrated. The, it's okay to assume it's your code, but it's also okay to give a 50% probability to it not be in your code or 25% or whatever percent you want. But that has to increase as you continue to check your code.

**Chris Gammell:** Right. And actually, so I, I'm just, now it's just about back in my head. What one of the problems that I had that Alicia was very kind and helped me with. The NRI 52. Yeah. Yeah. So I was, I was working on NRI 52 and I was using a dev board and I, you know, try and like the Dickens to just get this thing running. And finally I'm expressing so much frustration. Alicia's like, why don't you just give me a call on Skype? We'll talk through it. And the end result was I was following an example for the wrong goddamn part. It just wouldn't have worked no matter how much I tried. I was reading the, I actually had gotten this board from someone who was very kind who sent it to me and it said NRI 52 and nope, it was an NRI 51. Let me tell you. Or it was, I don't remember me. Oh no, sorry. It was the NRI. I thought it was the NRI 52, 840. And this was the NRI 52, 832. And every example I tried would not have worked on that.

**Christopher White:** And the thing was, I knew those examples. I had used them. So I knew how they should work and what you were telling me were the right steps. So then you start thinking, okay, something else is wrong. But as a beginner, if the steps don't work, it could be the way you did it. It could be the steps. It could be cosmic rays. It's just hard.

**Dave Jones:** There's a thousand things like that. That's right. Because they're complete systems, right? They're not, it's not like a little circuit. It's not like a little program running on your desktop, you know, that you can fully understand. It's a complete system with all these parts and memories and huge. I mean, we talk about firmware and it's not like 1982 where firmware was, you know, 500 bytes of code that somebody wrote. Right. It's huge amounts of code that are running on various pieces. So it's this complete system and lots of parts can break in a complete system through no fault of your own, even through things as ridiculous as mislabeling, right? It's so, yeah. And there's always something, I guess that was my point back with learning C-flag. There's always something that can go wrong. So don't bother learning anything. It's not really a lesson I want to give.

**Chris Gammell:** It's a system on the edge of entropy, right? Yeah. I mean, that's kind of what it gets towards. And this is the reason, right? So again, to go back to the, like, should you just follow the vendor's path? And it's like, yeah, maybe. You know, like that is the least entropic way towards getting some dopamine in your brain, you know? And like for some people, that is the right solution. I would probably say that as well. When I was said I wanted to learn GDB and all these other things, people kept telling me, yeah, use NIDD. Use this and this. And it's like, there are very, very strong arguments for that. I ignore them and I paid the price for it. But then again, you know, like I think about that too. You know, someone says, do this the easier way. And it's like, okay, but all those skills that you have, person telling me that it do the easier way. All those skills you have came from similar frustrations. So do you skip those frustrations in order to get something done? And it's like, well, sometimes you have to get something done, but sometimes you want the learning. So I don't really know. I don't know what to.

**Dave Jones:** I wouldn't say it's do it the easier way anymore. I think it was. Now I would say it's do it the modern way.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. There's very few cases. I mean, there's a few instances where I've been places where we've gone to raw GDB and GCC and command line with people using IDs on top of that, of their choice.

**Chris Gammell:** Yeah. You're doing it for like a revision control or continuous integration or something like that. You're building like these stacks of tools for your whole company, right? Right.

**Dave Jones:** But even there, it's usually to get away from a licensing fee. It's not a technology decision. You know, it's like, oh, we're paying 5,000 bucks a month per seat for whatever for IAR. That's a big cost center. Let's take the pain and shift to something else. And we'll support it.

**Chris Gammell:** Let's spend it in hours. Yeah. We had people supporting that.

**Dave Jones:** You know, we had a team of two or three people who were like the GCC folks. Right. So it wasn't that every developer was a genius at running command line tools. It was that it was a supported product within the company.

**Chris Gammell:** Yeah. And that's interrelational property that actually adds value to the company and all these other things. But as a solo starting person, you're not going to get that. You know, you're really going to lean on some company that may have done that for you.

**Dave Jones:** And did you use how for your stuff at all or just completely?

**Chris Gammell:** No, I did. Yeah. So the SEM32 stuff, I was I ended up going into using the cube configure tool and and then doing some house stuff, too. OK. And that's what Nicholas, my tutor, the less experienced but very helpful tutor, was kind of walking me through that. And it was just like super calm to like watch and like follow along as well. You know, there's also that. And there's actually some really great YouTubers who do that stuff. And I think there should be more of that. You know, I'm very strong on the I talk about apprenticeship and that kind of thing. But just walk walk watching over someone's shoulder sometimes just gives you that. Oh, it's not like, oh, I can immediately do it. But it's, oh, I think I can do it. Oh, I I think I can struggle through it. And I can always go back to that example. And that is I wish there was more of that.

**Christopher White:** I've heard more people are programming on Twitch, which sounds awful to me. I mean, I hate it when people watch me type. And yet I can see how that would be valuable just to see how somebody else works. Drive me insane. Well, but Chris and I worked recently together and I use push and pop D to store my directories when I'm in Linux so that I can change directories. This is very not important. I use a certain command.

**Chris Gammell:** Yeah.

**Christopher White:** And he saw me doing it. I was like, what's that? And then a few minutes later, he used a command. I'm like, what's that?

**Chris Gammell:** Yeah, exactly. It's like, you know, workflow voyeurism, you know, like you don't know how other people work. And you might find something. How do you figure out, how would you go and Google for that functionality that you, the push and pop D thing that you do? I don't know. Like, I don't even know what it's, I don't know what you use it for. Like, but once you learn it, it's really valuable and it could save you a lot of time. Not to mention the confidence piece. Like, I feel like so much of learning is a confidence game. So again, going back to piano, right? Like, if I want to go and like learn how to play a D minor seven on the piano, I can follow and look it up online and find a chart. But like having a teacher sit there with you and be like, oh, sometimes the seventh goes down below the root, you know, and then you play the root on your left hand. You know, just all these things that like, yeah, now I feel great about it, but I don't know. Like the way I used to play was very clunky and self-taught and having that guiding hand is like a fast forward. It's like a cheat code. And I think that's worth paying for, honestly.

**Christopher White:** You've said you've gone from Arduino and then you went to GDB and Vim and the hard way. And then you've gone a little back. Are you back to Arduino or do you mean the cube and sort of the center point?

**Chris Gammell:** No, I will. A little call back here to the Jay Carlson shows on Embedded. Also, dibs on having Jay on the show next. You guys don't get him back. I've talked to him about it. I said, if they call you, do not, do not go back on Embedded before you go on the app power. So Jay's, if people haven't listened to Jay's shows, I think they were both great. I enjoyed his first show, which was about the $1 microcontroller in depth. But the real second one was about learning. And man, everything he said was just like, just the contextual electronics parts of my brain just lit up. They were just like a Christmas tree. You know, everything just really fell into place. But he has the $1 microcontroller page, which is a great resource still. And let me tell you, his favorite part is the EFM8 LB1264E, whatever it is. And wouldn't you know it, I am using that part now. And it is a great little part. A lot of people give me sideways glances like, 8051, huh? In 2020, okay. But I was looking around for some parts that, for a part that had a lot of DACs. And this thing has four DACs and a whole bunch of analog inputs and other peripherals. And it's just a peripheral machine with an 8051 core. So it's great.

**Dave Jones:** I think the thing about STM versus things like that is the STM has all this infrastructure behind it. And the clock tree that's, you know, if you look at the configuration thing in Cube, it's a poster. Oh, yeah. There's a lot of complicated stuff. So if you were to try to bring up an STM without Cube and without help by yourself, that's like a year-long project for somebody. Yeah, right. Sometimes. And it's just you're in front of a data sheet the whole time, right? Yeah, yeah. I think the 8-bit stuff usually is a lot more friendly. Am I wrong? Or do you find it more friendly?

**Chris Gammell:** Parts of it. As you may both recall, I've sought some help on the embedded Slack. And there's been some quirky stuff. The interrupt stuff is always a challenge. Not just interrupt stuff. So like there's paging. So there's a special function register paging. And so like I think that I'm writing to a register. And it's like, no, Chris, you're on the wrong page. Change the page before you write to a value. But some stuff's really simple, actually. So like the way that you're just reading and writing from registers sometimes is just super intuitive. You know, there's basically there's a macro that assigns a value or a register name to it. And it's just equals one, equals zero kind of stuff. And you're turning things on and off like that. And I know that there are similar things in HALS and stuff. But it seems like there's less overhead to do some of that.

**Christopher White:** That's true. I mean, the HALS purpose is so that you can switch chips.

**Dave Jones:** Right.

**Christopher White:** It's not real. I mean.

**Dave Jones:** It's an abstraction. And abstractions come with costs.

**Christopher White:** Yes. And you were saying earlier about, well, people didn't. Are you supposed to go the path that the person who's teaching you went? Or are you supposed to go the path that they say is easier?

**Chris Gammell:** You should go your own way. But. Hey, hey. Copyright strike for that.

**Christopher White:** But a lot of us did do 8051s.

**Dave Jones:** I didn't.

**Christopher White:** And there is a path that shows that that's okay if you really want to understand what C is doing.

**Dave Jones:** Well, I guess I did 6502. Okay.

**Christopher White:** And I have brought up a Cortex-M0 when they first came out from scratch from an 800-page data sheet. Really? That hadn't been printed yet. We were pre-production of Cortex-M0s.

**Dave Jones:** Yeah.

**Christopher White:** It was really hard. Really. I mean. But you bring up the clock tree. You do it one step at a time. You map it out with your electrical engineer.

**Dave Jones:** Eight hours a day in an office. Yeah. I mean, there's a little. With a scope. Difference of focus. Push into a pin. Yeah. Difference of focus. Maybe with some other people to bounce things off of. No? Was it all you?

**Christopher White:** That was.

**Dave Jones:** Wow.

**Christopher White:** That was when I was consulting in that place in Union City. So, they didn't have any other firmware people. Although my double E was fantastic.

**Dave Jones:** So, Chris, I'm doing a similar thing to you that you're doing. I have not written a line of C for work since early 2019, I think. Something like that. Oh, okay.

**Chris Gammell:** That's only a year.

**Dave Jones:** A year, right? Yeah. Yeah. Maybe a little longer. I haven't been on my bike in like two years. No, no, no. Late 2018. It was late 2018.

**Christopher White:** It's still only about a year. A year and a half. Yeah.

**Dave Jones:** And now I'm doing, my current client is all machine learning. So, it's all Python. And I haven't, so I haven't done no embedded, no C stuff.

**Christopher White:** We'll go to C eventually. Sorry.

**Dave Jones:** So, I was starting to get worried that I was getting out of practice. Skills were getting rusty. And I said, well, you know, I've got some extra time. I'm not using, I'm not doing a tremendous amount of hours. I'll do a personal project. And I'll do it the way, the hard way. The hard way. Now, listen to what I define as the hard way. The hard way is what I would do for a client. For most clients, if they said, okay, I want to do something in STM32 and here's the project. So, I bought the dev board. I bought some peripherals and things. And I'm making, what I'm making doesn't really matter, but it's a little MIDI thing that does some.

**Christopher White:** We'll probably talk about it last week.

**Dave Jones:** Some synthesis, maybe some note processing, maybe some sort of thing on a TFT display. But it's got a MIDI interface and a display and I2S audio, a bunch of peripherals. But the goal was to just bring that up from scratch and relearn, re-experience bringing up peripherals and writing code. So, I had never used STMs except, you know, far down the road. Oh, yeah. Right now at the beginning of the, you're not architecting decisions. You're just dealing with what was placed in front of you. Yeah, yeah. So, I got their stuff. I'm using their IDE, which is, you know, built on top of GDB and GCC, but it's Eclipse. I've thought repeatedly about leaving it, but every time I do, I'm like, it's working fine.

**Chris Gammell:** Didn't they buy someone too?

**Dave Jones:** Yeah, Etollic. That was on your show. Etollic. Yeah, that's the IDE they've got now. And it's got the cube thing built into it. So, you just hit another tab and you can go look at the whole configuration and it'll regenerate code on the fly.

**Christopher White:** I saw that and it was pretty cute.

**Dave Jones:** It's pretty slick. I mean, there's a lot of problems with it. It's Eclipse, which I generally don't like very much, but it's working fine. But, you know, I'm finding a lot of the same things you are where it's like, what the hell is going on? You know, what have I done? So, I got MIDI working pretty quickly because that was a UART and, you know, the support in the HAL for the UART's okay. But I had a lot of trouble with interrupt handling. Still do. I have notes. Okay, go back and look at this because this is stupid. But the way HAL deals with interrupts is just completely dumb.

**Chris Gammell:** Yeah, and it's like, it's really heavy handed, right? It's usually like, it's like, oh, well, you know, it throws to a function and then there's like 30 lines of code. And you're like, you're literally just turning off the interrupt flag. And why, you know, but they're doing it for a reason.

**Dave Jones:** Yeah, yeah. I mean, it sort of works, but I got into this situation where if I send it enough data, eventually it doesn't reset the interrupt flag. And so, I had to add code to go and, you know, hammer that if that was unclear. We should just sit in the background giggling. This is fun. Yeah. But the next thing I had, I tried to bring up was the display. And that took me two weeks. It was a spy display. And I got one from Adafruit because it was like, okay, this has an Arduino library. I can look at that. Well documented. For reference, well documented. And I got into it and I was like, oh.

**Chris Gammell:** The interface is usually well documented. Yeah. But the parts they buy are usually, you know, some obscure Chinese brand and it's.

**Dave Jones:** It's actually an ST LCD controller. Oh, okay. All right. But it has like a 400 page data sheet. So, if you try to bring that up from scratch, that's another, you know, many month process if you're doing that. So, I said, I kind of backed off on that and went and looked at what Adafruit was doing and copied some of that code. It had like 400 instructions, you know, 400 commands that need to be sent over spy. Anyway, long story short, that took me a huge amount of time to get working. And I had my salier out doing spy. I'm like, God, I hate embedded as I'm doing this. So, it's, yeah, all this stuff is a challenge and it's still a challenge for people who've been doing this a while. The funny thing was the last peripheral brought up was the audio interface. And that was right after getting the display working. I was like, well, this is going to take me forever. Yeah. And so, I wrote like 10 lines of code that I thought might make it work, plugged it all in, went out and soldered a header on, hooked it up. Plugged his headphones in? Plugged my headphones into the thing, put it on my head, and I'd read the note in the Adafruit thing for their little codec thing. It said, well, this audio amplifier is really low level, so it's not going to be able to drive headphones very loudly. And I'm like, oh, this isn't going to work anyway. So, I pressed go and it was the loudest noise, loudest saw wave coming out. Throw my headphones off. But that came up in, you know, half an hour. So, you never know what's going to happen with that stuff. But I'm finding lots of frustrations. And I'm working through it because I'm like, okay, this is always frustrating. I remember it being frustrating four years ago when I was bringing up a display at Fitbit. You know, similarly, why isn't this? And I think a lot of it's because with things like that, nothing works, right, until it does. And you don't know why it doesn't work because you have no visibility. You can't look inside the display controller chip and say, oh, well, I was expecting you to be in this mode with the chip select high and the command bit was set to this. But then you sent me this and I got confused. You don't know. It just doesn't do anything.

**Christopher White:** I would like to note that I'm not allowed to help on this unless asked.

**Chris Gammell:** Oh, wow. Okay. How's that going?

**Christopher White:** It's making me crazy.

**Dave Jones:** Yeah, right. Well, because you'll just tell me to do it.

**Chris Gammell:** It's like listening to someone who they're having a fever dream and they're like, no, no, no, get the bees away from me.

**Dave Jones:** I've asked you for help and I've talked to you about it. You know, you've given me good advice. Yeah. But at other times it's been, yeah, I don't know either, right?

**Christopher White:** Well, there was the, well, yeah, of course it's only sending four bits. You must have only sent the four bits in cube.

**Dave Jones:** That was pretty dumb. I was just, my eyes were just skipping over the part where I had spy set to four bits, but.

**Chris Gammell:** Well, I think that that's, I think that kind of rolls back to like the, okay, so what is the value of IDE and all these other things? I think what some of the vendors are doing more and definitely true for Silicon Labs with EFM8. And I think the STM32 tool is doing better with this now too. And there's a lot of other tools that have similar things. But one of the disservices I find with the Arduino IDE and similar things is like, it's simple, but then you never get outside the simple. Yeah. And when you start to have breakpoints and you start to have register inspection, all these other things, no one's there to tell you how much that will help you. And you're not, when you're not just spitting out double debug to a serial port, you know, like that, that is such a big shift and no one listening. Very few listening are going to be surprised by this, but I feel like people who are at university level, it's like are going to be working in the Arduino IDE and similar kind of reduced interfaces. Like you need the leveling up to the, to the breaks and the debugs and everything like that. That gives you the chance to go and see, Hey, I thought I set that CRC register. And then I figured out that, no, I, I, I wasn't doing it. I, I, I had the wrong page selected, you know, and I can actually go and look at the register after I step past that line of code and it's not there. And, um, again, not surprising for many people listening, but, um, but again, how do you, how do you know that if you, you don't Google for that, you know, it's like, what is the best way to do firmware? No one's going to tell you that basic thing, right? Yeah. It's not a discipline.

**Dave Jones:** Firmware is not a discipline. It's, it's a collection of lore over 30, 40 years. It's just, it's not like computer science. It's this collection of all kinds of different things. And most of it's things that have been developed by these hardware companies, right? Yeah. It's nobody's, nobody's mathematically backed. This is the best way to do serial communication. It's okay. Here's our peripheral and here's the 50 registers that configure it. And, and, oh, and here's the exceptions to the rule. And yeah, that's all.

**Chris Gammell:** I talked to, uh, I talked to someone from a very, very, very large web scale company who's doing some hardware and, um, boy, are there software people perplexed by hardware. And it's not, not just because it's, you know, it's hard and there's, you know, electrons involved and all these other. But just like the methods, they're like, what are you doing here? Do you know what we can do with code? Yes. You know, it just, it is so far afield. And, uh, and, you know, some people have tried to fix it and I, these are great efforts. The, the chip companies are, I feel like more software people coming into the, or more software, uh, um, background type people coming into the hardware space and getting hired at like an ST or similar things. That is probably one of the best things that will happen for the industry because there will be more methods and, and similar, um, you know, just how they develop these dev kits and similar things. That is just really, really helpful. Yeah.

**Dave Jones:** The tools have been getting better. They need to get better faster. I do worry sometimes about the, the software approach to writing software on small devices because.

**Chris Gammell:** Memory.

**Dave Jones:** Yeah. I mean, there's always a tension between resources and, and cost and things. And if you can afford it and it makes sense, then that's fine. But, uh, I always get worried when people are like, well, you should do it this way. I really can't because then your application doesn't fit, you know? Right. And that's a hard discussion to have sometimes because it's like, well, I can run, you know, I'm running Python over here and it does all this stuff and I can just put that on my micro control. You can, but then you can do, you know, an eighth of what you could do otherwise. And probably in, in eight times the time.

**Chris Gammell:** Yeah. So there's that new, um, there's a new Arduino that just was announced at CES. It's a $99. It's got a Cortex M7 and a Cortex M4 on it. And it's H7. And yeah, it's a Raspberry Pi. Okay. What are you doing? Yeah, exactly. And it's, but I think that it's, it's slightly a disservice because it's like, part of me says, Hey, look, computing is cheaper than ever. You know, you should throw resources at the problem, but at the level they're talking about, I'm not sure if it, where the balance point is. It will find out. Right. Yeah. I don't know who that's for, I guess. I think that's for JavaScript developers who want to do JavaScript near the hardware.

**Dave Jones:** I think that's honestly going to be, um, but it's, you know, it's expensive compared to, I mean, a Raspberry Pi is the same thing, right?

**Chris Gammell:** That's not a problem for software people.

**Dave Jones:** Yeah. I guess so.

**Chris Gammell:** Yeah.

**Dave Jones:** Not for me to get.

**Chris Gammell:** Um, one thing that I wanted to bring up as well about all this too, is that, um, I used to open code, you know, like I, someone would send me some example code or some other things. And my first response was fear. Like it would like, literally I'd be like, open up and be like, what am I looking at right now? You know, like when you look at someone else's code, I'm not sure if there's, uh.

**Christopher White:** Yes, there is. Gerber's. I mean, I do fine with schematics, but if you send me a Gerber and you don't send me these schematics, I am toast. I'm just like, I can't, I can't.

**Chris Gammell:** Right. This is madness. Why, why would you do any of this stuff? Right?

**Christopher White:** Yes.

**Chris Gammell:** And, um, I've, I feel like it's getting better for me. And I think that's a positive, a sign in the right direction. You know, um, Alicia, you have that, uh, resource on GitHub. I forget what it's called now, but it's like reusable code or something like that. Yeah. Reusable code. I owe you some pull requests, by the way.

**Christopher White:** Yeah. And I need to actually do the pull requests.

**Chris Gammell:** I haven't done them. Well, you have the other ones hanging out. But that's like good, that's like good example code. And that scared me. And then Alvaro sent some, some code as well. And that scared me.

**Christopher White:** Well, and the funny thing was that Alvaro's code and my code do the same thing in mostly the same way, but they look different enough that it's, it would be a little like, wow, that's a lot of code to read.

**Chris Gammell:** Yeah. Right. Right. And it's like, it's meant to be reusable. Right. And that makes, that's good code. That's a good library style approach to things. And yet, you know, when you start passing around void pointers and I don't know, like, you know, like string passing, anything with strings is. Function pointers.

**Christopher White:** Function. Function. Once you have function pointers. Yeah. Most people will go cross it.

**Chris Gammell:** Yeah. I'm still, I'm still not quite there yet, but.

**Dave Jones:** You'll know you've made it, Chris. When the, when the reaction to, to code that's not yours, that is given to you or to look at or that you find is not fear, but anger. Then, then you will have ascended.

**Chris Gammell:** I'll be stroking my gray beard. I always, yes. How dare they? Right. Whippersnappers. Yeah. So, I, I don't know. I think that that, again, that, that's a lot of mindset stuff and I'm not sure if that's like immediately helpful for people, but I think that the interesting thing about it, I'm not sure there's a way out of it. Like the only way out is to, to do it. You know, you can't, you can't read your way. I mean, like books are very helpful for me as well, but just reading, it's not going to help you. You know, you have to put in time in front of a, a debugger and, you know, just step through stuff and.

**Dave Jones:** You have to make the mistakes.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Um, enough to, to know what things, to kind of have a sense of every time something's wrong to have a sense of a handful of things that it might be. And then once you eliminate those things, then you start getting worried and.

**Speaker ?:** Yeah.

**Chris Gammell:** Um, so another thing that's been really, really helpful that Alicia talks about, I think Chris, you have too, but, um, I've been journaling a lot and, um, like as I go through, because I would get into these kind of fury states where I would, you know, I'd be trying something, I'd be have a, have a program that's working, change something, nothing, nothing changes. I change something, nothing changes, change something, nothing changes, change something, nothing changes.

**Christopher White:** You didn't plug it in.

**Chris Gammell:** No, it was plugged in. It was, yeah, that has happened too, but I changed something and then it breaks. And then I say, okay, I can go back and undo that thing. And then I go back and undo that thing. And then something else is broken. And it's just like, I've gotten myself so deep into a hole and yes, I am using revision control. But the real thing is that I'm not thinking like experiments. Um, and that's really one of the most valuable things that I've been doing for myself is I'll write myself a journal, you know, just a bullet list on a day by day basis. I call it a build log. Like, what am I doing? What am I stepping through? What am I trying? If I'm running an experiment, I'll indent the bullet list. Hey, I'm going to go try and change the clock. I'm going to go and increase the clock speed and see if I break anything. And this happened, this happened, this happened. Looks like everything's okay. But now I have a record, a chronological record as well of what I've been breaking. Uh, and, uh, and that's been really helpful.

**Dave Jones:** That's fantastic for two reasons. Um, the first is when I've taught people thing, computer related things, one of, one of the chief fears I found with people who don't have a lot less experience than any of us, but, but we're just starting out as kind of, I'm going to break something. Right.

**Chris Gammell:** Like, yeah, I mean, there's like high cost of breaking something. Right.

**Dave Jones:** I'm, I'm really going to break something. Like I don't want to, and, and getting over that and being, being, having permission to just make changes experimentally and see what happens without fear of breaking. That's, that's super important. And the other is it's just a debugging technique, right? When you've got these black boxes, like a spy peripheral that isn't talking to you. Yeah. At a certain point when you've run out of those five or six things that you know it usually is, you, you have no choice, but to start changing the inputs and just see if something changes or if you've got something wrong, uh, in a configuration that, you know, maybe isn't documented correctly because half the time, okay, not half the time, but a fair number of the time the data sheets are wrong. And it may be that a flipped bit in a data sheet is what the problem is. And you're not going to find that without just exhaustively going through and saying, okay, well let's change all the inputs and see if the outputs change at all.

**Chris Gammell:** Yep. Yep.

**Christopher White:** The third reason to do it is rubber duck debugging, which is your notebook actually becomes something you're talking to sort of. I mean, but.

**Chris Gammell:** Yeah. I have like this tone where I talk, like it is, I, I'm like, I'm like, I find myself writing myself notes to like future me, you know? Yeah.

**Speaker ?:** Yeah.

**Christopher White:** Yeah. Yeah. Yeah. Yeah.

**Christopher White:** Yeah. Or, or even just laying out the problem as you would if you were laying it out to a tutor or to a mentor or to a coworker. And that helps me so much because now I've organized my thoughts. It's not just having run all of the experiments. It's that feeling of, I don't know what else to do. And then you write out what you did and what you think, and suddenly you get a bunch more ideas on what you should do because it's just, you put it all together in a different perspective.

**Chris Gammell:** Yep. And listing your assumptions. And I feel like that's usually when I get to the end of the five or six things, like Chris mentioned, that I think it could be, it's because my, the seventh and through 15th thing that I should try is because my assumptions are completely off. You know, it wasn't plugged in or I'm writing to the wrong register or something like that. You know, I don't understand what a register does.

**Dave Jones:** Or you've spent the whole day downloading the old code image and you never actually updated it. Something that's of course never happened to me.

**Chris Gammell:** Too real. Too real.

**Christopher White:** I heard that there was a new KiCat happening.

**Chris Gammell:** New KiCon. KiCon. Sorry. Or it is going to be in Europe. So I'm okay calling it KiCon because, you know, the French. Yeah. Yeah. Yeah. That is going to be happening September 11th to the 13th at CERN. Oh, wow.

**Christopher White:** Are you going?

**Chris Gammell:** Oh, yeah.

**Christopher White:** I mean, because this is your conference. This is, you did this one pretty much by yourself last year.

**Chris Gammell:** I did the first one. No, I had a lot of help, but I organized, I was the organizer of the first one. And then I was talking to the development team and Seth, who's on the development team, who started the KiCat Services Corporation, I think it's called, which is like a professional, kind of like a mini red hat for KiCat. And Seth's like, I want to do a conference this year. I want to, you know, get people together. And we started talking about, well, maybe we should have it at CERN. We had talked about that last year, dreamed about it last year. And it all fell into place. There's been like super, like the folks at CERN are so helpful. And they're really well prepared to do conferences too.

**Christopher White:** That's great.

**Chris Gammell:** Yeah. Yeah.

**Christopher White:** That'll be both a lot easier for you and a lot more fun for you and probably really educational.

**Chris Gammell:** Oh, yeah. And I mean, I might get to go. I don't know what the extent of the exploring we get to do at CERN. But like, I mean, that's like a dream to go see the Hadron Collider, Large Hadron Collider, and probably bump a switch and, you know, reverse the universe. Reverse polarity on every electron in the world. Yeah. That's the hope. You know, it's really a dream. It's a dream.

**Christopher White:** That's your dream. That's good.

**Chris Gammell:** Yeah. It's a weird one. Chris, you were doing a little bit of KiCad, I remember. I was. Yeah. Alicia, have you tried it yet? You tried it at one point.

**Christopher White:** Yeah. I did your welcome. I did your blinky. And it was funny. It was really good. And KiCad wasn't that hard. But it turns out, despite my incredible ability to play games that look like layout, apparently I'm really bad at layout.

**Chris Gammell:** Well, at the beginning. Yeah.

**Christopher White:** But, I mean, I play these games and I totally can untangle things, but not with parts. No, no.

**Dave Jones:** Layout is tangling things intentionally. With intention. Making them not smaller.

**Chris Gammell:** That's right.

**Christopher White:** So, I didn't get too far with that. And I kind of realized as much as I like hardware, I prefer to buy it fully formed and then to do software on top of it or to apply it to things. So, for a long time I wanted to learn how to do boards. And it's not that I wouldn't mind that knowledge. It's just I'm not going to invest in it.

**Chris Gammell:** Right. And I think at the point where you can't get a sensor that you really want to attach to a Teensy or whatever the platform of choice might be. That's when, unfortunately, that's the right time to learn. The right time to learn was about three months prior to that. But that's when you're really going to be motivated to do it because no one else is going to do it for you. I think these days there are so many people that are doing hardware, Tindy, similar things.

**Christopher White:** I was thinking, yeah, Tindy and we have had at least one listener offer and actually do a board, which I used recently. So, it may be a skill set I opt not to go towards because I'm more interested in machine learning.

**Chris Gammell:** Yeah. I think that's – it's all choice, right? I mean, we all have so much time on this earth. I can't learn clarinet in addition to piano, in addition to firmware and RF and everything. It's just how deep do you want to get into each thing? And if you want to get deep into machine learning, there's going to be less time to skim the surface out of a hardware kind of thing.

**Christopher White:** Well, and then there's origami, which is a whole –

**Chris Gammell:** Of course.

**Dave Jones:** Well, folded paper has no limits. I'm surprised you weren't doing some now.

**Christopher White:** I'm not allowed to fold paper near microphones. I heard that.

**Chris Gammell:** It is pretty loud, I've got to say. Have you announced on here that we do a book club? No. Maybe we mentioned it. Yeah. I stepped away for this most recent book because I have some other stuff going on. But, yeah. Why didn't anybody tell me? We did a book on learning that both of you hated.

**Dave Jones:** About practice, rather. I liked things about it. I liked the messages. I think it could have been delivered.

**Christopher White:** I liked the messages. I didn't like the author.

**Chris Gammell:** You didn't like the writing. Yeah. I get it. It's – I listened to it. I think – I listened to it. It was very – I listened to it while I walked the dog. And that's much less invested. Yeah. Yeah. Yeah. Yeah.

**Christopher White:** And then we did one about writing that we all kind of mostly liked.

**Chris Gammell:** Yeah. Mostly about writing.

**Christopher White:** Mostly about writing.

**Chris Gammell:** Also about bears. Yeah. It was draft number four. The first one was The Practicing Mind. The second one was draft number four.

**Christopher White:** And then you ditched us for Drift Into Failure, which you would have liked because it's –

**Dave Jones:** Which is wrinkling my brain.

**Christopher White:** It is. Yes. It is wrinkling the brain.

**Dave Jones:** Maybe I'll do a catch up. We'll see if I can sneak in. But it also had a chapter which – very detailed reconstruction of an airline disaster which ruined my Sunday last week. Oh. This is a good advertisement, Chris. Well, I have personal problems with airplanes. Ah, right. Right. Yeah. Okay. But yeah. It's very good. But it's a dense read.

**Chris Gammell:** Yeah. Yeah. Well, speaking of books too. So another thing that happens to me with firmware – so now I'm kind of – I feel like – I'm feeling more confident. And there's been a lot of great people helping me. My tutors were wonderful. I've actually stopped doing tutoring for now because I got so busy with the consulting stuff. But this thing keeps happening now where I'm kind of like moving up in the layers. I'm like, ah, well, I really need to, you know, work on state machines. And I go into the embedded forum – or embedded Slack, rather. And I'm like, you know, here's what I'm working on. Here's what I'm thinking about I should do. And then like about 15 minutes later of people being very helpful in chatting, they're like, did you read that chapter in Alicia's book? I'm like, you know, I did. I should read it again. And then that happened about three or four times. So I'm also rereading Alicia's book. I am too, if it makes you feel any better. So a quick book, Alicia.

**Dave Jones:** And I copyedited it, so.

**Chris Gammell:** Yeah. I have it on my desk right there. People should go reread that. And it's the thing, like – so like you mentioned, like reading books to learn. You know, that first pass, that is an important thing. But it's also like how deep are you going out of things and how much – you know, I always talk about context. How much context do you have for the thing that you're reading? It's so easy for me to nod my head and be like, oh, yeah, yeah, state machines. I get state machines. But when I'm like elbows deep into a state machine and be like, why isn't this working? Why am I doing any of this? It's a lot different, right? And then a guiding hand would be really helpful. And that's kind of like a book chapter acting like a very specified tutor. I could also hire a tutor to do that same kind of thing. But a book is kind of put together to just be all these things at once.

**Dave Jones:** Yeah, and I find with books, like if you have experience with the things that are talked about in books, but maybe you're just a little bit away from it, going back and reading those chapters while you're working with it, it's a lot easier. And it's a different kind of value. It's like, ah, okay, I remember now. That kind of feeling. Oh, and here are the pieces I was forgetting. Which is really, really valuable to go back instead of sitting there going, trying to re-remember or re-derive, you know, a way to do state machines that you kind of remember, but not quite. It's just, it's so nice to go back to a chapter that you may have already read. Maybe you fully understood it at the time, but now you don't. And just think, oh, okay. And refresh your memory.

**Christopher White:** Just look at the pictures. I find that.

**Dave Jones:** Yeah. Yeah. Well, sometimes that's all you need. Yeah.

**Christopher White:** Yeah. And with the machine learning books, a lot of them have Jupiter pythons.

**Chris Gammell:** Oh, those are, yeah.

**Christopher White:** And I love going back and forth between running and reading their code and reading what they wrote about their code in their book and then modifying their code. So, I mean, I guess when I say I read things, I do more than that. And actually, I did email someone this week with a very long, detailed question. And I'm hoping he gets back to me. And since I know it's his job, I did put in the email, if this is too close to your job, feel free to tell me to go away. So, yeah, okay.

**Dave Jones:** I mean, the example I was going to use from your book was I needed a circular buffer, which in my mind I've done a million times.

**Christopher White:** Haven't we all?

**Dave Jones:** And I'm like, okay, I've got to do a circular buffer for this MIDI thing because it's going to interrupt and blah, blah, blah, blah, blah. And I think I flippantly told you to use one on the Slack, Chris, at some point. You did, yeah. Hey, just go use a circular buffer, dude. I mean, it's just no big deal. Right, right. And so I opened her chapter and they're like, well, I'll refresh my memory. I'm like, oh, no. I don't remember this at all.

**Christopher White:** It has a double pointer circular buffer, which is a lot more complicated.

**Dave Jones:** Right. But you did this trick with, you do a little trick with. Powers of two. Powers of two. And there's all these corner cases with circular buffers where you get in real trouble and like, oh, I don't remember any of these things. So it was really great to go back to that because it was both a, wow, I'm full of crap. And also, okay, now I remember, you know, these are ringing bells that, okay, this isn't as easy as I remembered it. And so I apologize to sending you down that road with just a head. I mean, it's a circular buffer. How hard could it be?

**Chris Gammell:** It's good to know. But I feel like that's a great example, too. It's like, okay, I need to do this thing. Talk about a thing for machine learning to really to do is like, if I could just like talk out my problem and then a computer is like, I know what this probably is, you know, because like right now my machine is the slack and, you know, people kindly listening to my being like, oh, I need to do this and this and this. And they suggest things. There's nothing out there like that. You know, how do you know where to go? Stack over for.

**Dave Jones:** Stack overflows where I end up most of the time. Yeah, but that's not always great either. It's always sort of close to what I need, but not quite. Yeah. Yeah. Mm-hmm.

**Chris Gammell:** Yeah. I think that it's, you know, it's imperative on all of us to have a knowledge base and keep building our knowledge base and like truly a base, right? Where we're, we have a little bit of dip a toe into each little puddle and, you know, not figure out how deep it goes, but like know that it's there and you know the name of a thing. That is really helpful. But sometimes that's just, you know, you don't have that. I don't know. Circular buffers is one for me. Yeah.

**Christopher White:** And it's really easy to say. And then if you're in some languages, it's really easy to implement. But then when you go into C and you realize, oh, what about the first one and the last one? Oh, that one. Yeah, off by one.

**Chris Gammell:** The last thing I was going to – I had mentioned this on the Amp Hour, I think, last week when this show airs, or two weeks ago. But we're pre-recording. We got you guys. There's another self-help-y book that I listened to. It was about learning quickly. And they had brought up a thing I'd never heard of before. And again, another thing I never would have heard of if it wasn't for this book. It's called SQ3R. Have you ever heard of that? I think I've heard that acronym somewhere. What is it? It is a reading comprehension thing. And basically, it's a way to teach yourself. And so basically, it's survey question, scrolling down the Wikipedia page, read, retrieve, review. But basically, it's – you go through – the main thing is you go through the tables of contents and you create all these questions based on that at the beginning. So if the tables of contents said chapter heading is PCB layout, the first question you get, what is PCB layout? That should be the answer you should be able to answer by the end of that. And then chapter heading 1A is creating tracks on a PCB. And how do – so the question would be, how do I create tracks on a PCB? And again, you're just creating these questions that are – they sound really pedantic, but like at the same time, that is what the outline of this thing is supposed to be teaching you. And so if you can't do it by the end, what would someone actually be reviewing you on if it was a formalized setting? And so you're basically formalizing a setting for yourself. And then the idea is that you actively go and read based on these questions. And then you maybe make flashcards and then you review them so that you can have recall. How do you really generate recall instead of I know what a circular buffer is. It's like, well, you could go and do it. Or you could go and – if you're reading at least a chapter on circular buffer, you could – there's a subheading on the off-by-one problem. And then you could go and review what is the off-by-one problem. Do you have that kind of in your long-term memory storage personally? And yeah. So that's kind of it. It's a very – it's very tough. I'm trying to do this with the Art of Electronics X chapters right now. And it's very – the headings aren't very good on there. And there's a ton of really in-depth information that I would miss if I just did the headers. So it's not a great book for that. But there are some other books that I've been looking at. And yeah. The RF books are insane. So much to learn, you know?

**Christopher White:** I mean, that's a form of active reading.

**Chris Gammell:** Yes, exactly.

**Christopher White:** And I mean, taking notes alone is a form of active reading that's pretty good for most people.

**Chris Gammell:** Yes, I agree.

**Christopher White:** And the questions give you another perspective. So that makes sense.

**Chris Gammell:** I was not a particularly good student. I think, at least you were a very good student. Such a nerd. Chris, you sounded like you were a – I became a good student. Yeah. That's what I've gotten from the – I did not start that way. Right. And I, you know, many, many years into my non-schooling world, I think that this is – you know, if you're going to learn it on your own, I think that if you're not doing it, you've got to have some kind of active reading like this. And so that's what I'm trying. And we'll see.

**Dave Jones:** Cool. Well, watching you go through all this has definitely inspired me a bit too over the last few months to do some more learning and things. So that's great. Thank you for opening the process.

**Chris Gammell:** Yeah. Thanks for all the help. Such as it is. I'm not going to stop being on the Slack just so you know.

**Speaker ?:** No.

**Chris Gammell:** No, that wasn't.

**Dave Jones:** There's a lot more questions coming. A lot. No, Chris, I think you've got everything. You're fine. Click. Deleted. Deleted. Deleted.

**Christopher White:** It's nice to talk about learning things because we do get frustrated and it's really nice to hear that other people get frustrated too because you can be in that rage hole of it should just work.

**Dave Jones:** Well, and –

**Christopher White:** And then realize, oh, wait, I heard that recently and sometimes it's not what I think it is. It's just nice.

**Dave Jones:** On whatever social media and seeing these, oh, look what I did, this amazing thing. It's like, oh, great. So many amazing things. Let me tell you, that guy.

**Chris Gammell:** People who listen to the Amp Hour will know. He's been on the show recently and he – but him too. Like I love having him on the show. He talks about his learning process. He was on the first episode of the Amp Hour for 2020 and I had him on and he, you know, posts these amazing projects. But you know what? He came on and he was talking about what he struggles with too. And we're all there. We're all struggling with different things. And I think it's okay. I think it's giving yourself permission to learn and struggle and feel dumb sometimes. You know, like it's okay. And speaking of dumb, I think after this –

**Christopher White:** I'm so worried about what's going to happen next.

**Chris Gammell:** After – I'm having Ben Krasnow back on the Amp Hour. Oh, cool. And so, you know, one of my shining beacons of like people who are like driven – whenever I think about like, oh, I need to make my process more of experimental and like formalized. If people watch Ben's video about making – he did like laser cut traces on PCBs and he holds up a thing. He's like, oh, on the 88th try this worked.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Holy crap. That is amazing. So, I'm going to be – I probably will have already by the time this airs asked him about his process and similar things. Because I think that like people that are learning for a living, and I think Ben's a good example among many, that is you need that kind of – that fortitude and that rigor. And Ben struggles too. He talks about it all the time. So, he's a great example of that. So, I'm excited.

**Dave Jones:** If everything was easy, I don't think we'd enjoy it.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Yep.

**Christopher White:** We would have nothing to complain about.

**Dave Jones:** It'd be like The Good Place, you know?

**Chris Gammell:** Exactly. Yeah? Yeah? Yeah?

**Dave Jones:** That last episode destroyed me.

**Chris Gammell:** All right. Well, I think there's only one thing left to do. You forgot to ask me lightning round questions. No?

**Christopher White:** Beach or mountains?

**Chris Gammell:** I'm more of a prairie person myself. What's your favorite fictional robot? Oh, I just finished The Bobiverse. So good. All of the bobs. All of the bobs.

**Christopher White:** Acoustic or electric guitar?

**Chris Gammell:** Electric piano.

**Dave Jones:** What is your least favorite chord progression?

**Chris Gammell:** 7-7-7-2.

**Dave Jones:** I can hear that in my head right now. It's very disturbing.

**Chris Gammell:** It's bad, yeah.

**Christopher White:** What is your favorite flux?

**Chris Gammell:** The one in front of me.

**Dave Jones:** If you could change...

**Chris Gammell:** You actually had these prepared too. I didn't know if they would have...

**Dave Jones:** No, we are making them up.

**Chris Gammell:** Oh, that's actually... You've really narrowed it down, yeah.

**Dave Jones:** If you could change one thing about the C programming language, what would it be?

**Chris Gammell:** Oh, we didn't even bring that up. Okay. Real quick. And now the rest of the episode. No, yeah. So I'm using the EFM8 and I was having this problem. I was trying... I was in a for loop. And I was like, you know, from my Arduino C++, all these other days, I had this error and it kept erroring out. It was, you know, four parentheses, int i equals zero, semicolon, i less than, you know, constant, semicolon, i++, end parentheses, and then the fourth loop, right? And it kept erroring out. And I'm like, what is going on here? And I talked to the Slack. And then we figured out that... What is the year? It's not using C99. It's using C... 90. 90? Yeah. C90. C90. Oh, my goodness. So... Yeah, you can't do that little int in there. Yeah, that's right. You have to declare it outside the loop. If you're using a programming... If you're using a compiler that's literally 30 years old, you're going to have some paradigm changes, I guess. So I guess they changed that. All right. Don't use C90.

**Christopher White:** They did. They did change it.

**Chris Gammell:** A lot of people have changed it. Thanks for having me back on. No, this was fun.

**Dave Jones:** It's great to hear about your experiences with firmware because I think they map well to a lot of people's experiences, too. Yeah.

**Chris Gammell:** Yep.

**Christopher White:** It was good to talk to you, Chris.

**Chris Gammell:** Yeah. We'll talk soon.

**Christopher White:** Bye. Bye.

**Christopher White:** Bye.
