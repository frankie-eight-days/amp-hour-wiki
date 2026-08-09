---
episode: 187
title: An Interview with Elecia White - Wirewove Worshipping Wookieist?
url: https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/
---

**Chris Gammell:** This is the M.R. Podcast, recorded March 3rd, 2014. Episode 187, with guest Alicia White, werewolf, worshipping, Wookieist.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Alicia White:** And I'm Alicia White, Logical Elegance.

**Chris Gammell:** Hey Alicia, welcome.

**Alicia White:** Hi, thank you for having me.

**Dave Jones:** Or shall we call you L?

**Alicia White:** Yes, please call me L.

**Dave Jones:** L, excellent. Because it's E-L-E-C-I-A with an E.

**Alicia White:** Yes, E-L-E-C-I-A. There you go. Or Echo Lima Echo Charlie Indie Alpha. There we go. Oh, hi-fi.

**Chris Gammell:** And also we should mention, not just of Logical Elegance, but also of our favorite podcast, outside of our own, of course, because we're, you know, ecocentric, but Embedded.fm.

**Alicia White:** Yes, Making Embedded Systems, which is Embedded.fm. Podcast is Making Embedded Systems on iTunes and Stitcher and all of the feeds. And it's titled that because that's also the title of my O'Reilly book.

**Chris Gammell:** That's right. Which we'll get into. Which we'll talk all about that.

**Dave Jones:** No doubt.

**Chris Gammell:** Yeah.

**Dave Jones:** Why have we got the competition on, Chris?

**Chris Gammell:** Okay, so I was so excited. I don't think you realize. I was so excited when I found Alicia's podcast, which was when you had Jerry on, right? I mean, that was, I think, when I heard about it and then I talked about it on here.

**Alicia White:** Yeah.

**Chris Gammell:** I was so damn. And this just goes out to everyone else out there. I would love to see more podcasts. I mean, I don't find this. I don't think there's any competition out there because, I mean, first off, it's Embedded. And I have no idea what Embedded is. And second off. You analog pussy. Exactly. I have no idea what I'm doing there. And then, you know, there's just such a big field. So, thank you. Thanks for doing it.

**Alicia White:** I didn't know about the Amp Hour before you heard of me with Jerry's show. And I was so impressed because, you know, finally I get to know what electrical engineers actually do. And I am glad I didn't know about it ahead of time.

**Dave Jones:** Yeah, we talk out of our ass.

**Alicia White:** I don't know what I would have done my show if I'm like, well, I could just listen to Chris and Dave and they'll tell me what I need to know. But, yeah, it's been really fun. And Jerry's show was probably the biggest one. Although, Lenore from Evil Mad Scientist, people seem to be pretty into that one too.

**Chris Gammell:** I was listening to that on the way home the other day and I really, really enjoyed it. I mean, I love hanging out with Lenore as well. And, you know, you've had lots of great guests on there. I mean, James from, what is it, Test Driven Development stuff. I mean, there's been tons of good ones. And you kind of, you and Christopher, your husband slash producer, also come up with great, they're not quite illiterative enough for my taste, but you do come up with great titles.

**Alicia White:** The titles are supposed to be taken from something embarrassing I say during the show. So, it does allow us to really highlight those things I wish would go away.

**Chris Gammell:** That's good. Yeah. Like the last one was what, the Bwahaha lessons or something like that? Or the…

**Alicia White:** Bwahaha sessions. Sessions. And the next one's going to be Pink Universes Die Really Quickly. Awesome. Because that can't be taken out of context.

**Chris Gammell:** Right, of course. Yeah. Oh, that's great.

**Dave Jones:** Now, even though you do an embedded podcast and you're an embedded software engineer and all sorts of, worked on all sorts of cool projects, as we'll no doubt get into, you're actually a scientist, not an engineer. Is that right?

**Alicia White:** Oh, not really. Really. My degree is half engineering and half CS. Okay. Right. Got it. I'm in the right spot. But I did go to a school where science was like really, I mean, even more than usual in the engineering curriculum, science was really a big deal. So…

**Dave Jones:** Right.

**Chris Gammell:** Okay.

**Alicia White:** That explains it. I tend to think myself as a scientist as much as an engineer.

**Chris Gammell:** That's good. Excellent. I think I kind of, I personally falter without, you know, like I'm kind of a little too hands-on, not enough theoretical sometimes. And I think you and I have talked about the paper side of things. You know, like how you are really into keeping notebooks and drawing everything out in paper. And I was impressed with that. And also, I have no idea how you can do it, especially as an embedded person. I would figure everything would be code.

**Alicia White:** Oh, no. I mean, like today, my mechanical engineer wants me to change how I'm doing some motor control stuff. And I think he's completely out of his mind. It's never going to work that way. And so, I ran, you know, I ran all of the pre-tests for how it works now. And I made some code changes. And then I ran the post-tests. And I showed it to him. And I said, tell me how this is ever going to work. And he looked at it. And he said, oh, I got those two lines crossed. Yeah. I told you.

**Chris Gammell:** It's right there.

**Alicia White:** But, you know, it's like proving stuff. I like proving stuff.

**Chris Gammell:** You like, okay. You like telling people when they're wrong and proving stuff. Okay. I thought it was more of a...

**Alicia White:** No, no. I don't think people when they're wrong.

**Chris Gammell:** No, really? We love that around here.

**Dave Jones:** No, sometimes.

**Chris Gammell:** It's like all Dave does.

**Dave Jones:** Yeah, I know.

**Alicia White:** Because you're always wrong. Thank you, David.

**Chris Gammell:** That's just the way it is. Yeah, thank you.

**Alicia White:** It's not that you're wrong. It's just that I'm right.

**Dave Jones:** Yeah, exactly. Oh, boy. I don't have the discipline to keep documentation. I just go, oh, no, look, it's just, it's so simple. I won't bother. And then it comes back to bite you every time.

**Alicia White:** Yeah. And if you keep doing it, isn't there like a definition of insanity in there?

**Chris Gammell:** Right. Yes, there is. Right. And I think that's how you and I got talking about it. And you've talked about that on your show. And you've talked about that in your book and stuff. But, you know, keeping track of tests and stuff like that. And me too. I'm just, I'm terrible with this kind of stuff. You'd think eventually we'd learn. But, no, I think we're just insane.

**Dave Jones:** No. Yep. Just insane. No, we're just lazy. I think engineers are inherently lazy. Yeah.

**Alicia White:** Yeah. And I don't know if you saw, but I posted where I get my notebooks from. And my notebooks cost a stupid amount of money. But I love them because they lie flat. They have the grids I like. They're numbered. And would I do this if I was using a crap spiral bound notebook? No. I would give up on that pretty quickly.

**Speaker ?:** Not.

**Alicia White:** Yep. But this makes me feel all comfortable. Like I'm making progress even if I'm just writing things down. And so it's not just writing things down because I'm kind of organized and kind of a nerd about that sort of thing. It's also getting to use the pretty paper. I bribe myself.

**Chris Gammell:** So you're an artisan. Is that what I'm hearing? Is you're a...

**Alicia White:** Well... Are you a paper hitster? I'm a paper hitster. Yes. Kind of. How is your penmanship? Do it even get me... Beautiful. Oh, my penmanship is awful. No. All right. Checks out. Checks out. Typical engineer.

**SPEAKER_01:** Yeah, yeah.

**Alicia White:** And you can't spell either, right? No. No. Well... I can't spell.

**Chris Gammell:** Well, the reason I bring this up, though, is because you have a really good... So I was digging into your book today. A little bit later than I probably should have been. But I was digging into the book, and I really actually like... At first, I was like, well, why the hell is she writing about this stuff in, like, the... I think it's chapter two, where you're writing about just, like, you know, drawing out all these different elements and building up systems and stuff. And then I was thinking, I'm like, well, where else do you learn that stuff? I mean, is that what made you put it in there in the first place?

**Alicia White:** Yes. There are... So there's that chapter, and then I think the next one is basically how to read a data sheet, which is like... Oh, you just... It's so obvious. You read a data sheet. Yeah. But there are some skills involved with organizing your thoughts and organizing a system so that you can explain it to someone else. And if you can explain it to someone else, then you can explain it to yourself, which I spend a lot of time talking to myself, I guess, explaining how I think it should work.

**SPEAKER_01:** Yeah.

**Alicia White:** To myself, even. And then that helps me. And yeah, so the book does spend a while on different ways to draw things, because there are different ways to think about things.

**Chris Gammell:** This sounds like the confessions of a longtime consultant who's run headlong into this problem over and over and over again. Is that where a lot of this comes from?

**Alicia White:** Not really. I guess I had been a consultant before I wrote the book, but I had mostly been full-time. And now, for the last few years, I've been entirely a consultant. It's more having been a manager, actually. Having hired people, hired new college grads and trying to teach them. And even people who are four or five years out of school, you know, when you're in college, you either get an electrical degree or you get a CS degree.

**SPEAKER_01:** Right.

**Alicia White:** And whichever way you come, it's horrible. I mean, you have half your job you don't really know how to do.

**Chris Gammell:** Yeah, I'd put it more than half, but okay. Yeah, exactly. Probably. Because there's the business stuff and the mechanical stuff and everything else, but yeah.

**Alicia White:** But even the junior and junior mid-level engineers, how do they learn the other half? How do they learn whatever they didn't learn in school in a way that makes them confident?

**Chris Gammell:** Yeah, that's the tough part, yeah.

**Alicia White:** So the book, I mean, there's the chapter about system architecture, which a lot of the software people are going to be like, oh yeah, I kind of remember doing that in school and oh, this is a good way to look at it. And then the next chapter about how to read data sheets and how to work with a hardware engineer, all the hardware engineers are going to be like, oh yeah, I totally can do that.

**SPEAKER_01:** Yeah.

**Alicia White:** But the two chapters together get you an embedded engineer, which is what I want. I want this book to be used by people who are going to work for me because I'm sick of explaining this stuff.

**Chris Gammell:** Yeah, that's good. Born out of frustration.

**Dave Jones:** Yeah, read my damn book, come back on Monday.

**Alicia White:** What is the hard part about being a consultant is one of my clients asked about how to do IQ math with getting rid of floating point and going to fixed point. And I said, well, I can give you an hour lecture or you could just read the chapter in my book and leave me alone.

**Chris Gammell:** So how did that go over? And then they paid me double.

**Alicia White:** No, he did opt to read the book and then ask me questions, which I feel is a far better use of both his time and mine.

**Chris Gammell:** Yeah, I agree with that too. That's nice. That's really nice. The other thing I like, I mean, you mentioned hiring engineers and I'd like to get into the management side of things, but I really dig that you put in a lot of the questions at the end of the chapter too. I really like that about...

**Alicia White:** The interview questions?

**Chris Gammell:** Yeah, I don't know. I just think that it's good stuff. It's like an odd way to sum up, not an odd way, but it's a non-standard way to sum up the chapter though, right? Like the why the hell does this actually matter?

**Alicia White:** Well, and it's for, if you think about the people who my, my, you know, the, the first five, 10 years of getting out of school, interviewing is an area that you just don't learn. And did you notice the questions are all from the interviewer's perspective?

**SPEAKER_01:** Yeah.

**Alicia White:** It's not, how do you answer this? It's how do you ask this? Because nobody ever taught me to interview and it was really hard. Oh yeah. And once you've made somebody cry in an interview, you're like, I suck at this. No, that means you're winning.

**Chris Gammell:** You ever made someone cry from a voltage divider? You've waited them out. Yeah. It's fun.

**Alicia White:** But I've seen a lot of people, when I, when I was a manager and people, when we were hiring and I would get these notes about how different people weren't adequate for the job and what questions you ask and people would answer weird things. And I kind of wanted to know, why do you ask this question? What do you expect from it? What do you look for? Is this just a way to weed out people who aren't like you? I want.

**Chris Gammell:** Oh, you mean like the desert island question? Like that stupid one?

**Alicia White:** Oh, yes.

**Chris Gammell:** Yeah.

**Alicia White:** Well, the, in the, in the, the, the goat and the cabbage and you and a boat. And the wolf. Yeah. Yeah. That's actually in the book. And, and then I make fun of it because it is, it's a question that you have to know the twist. And if you don't, it's, it's a dumb question for, for finding out if this person can program or, or if this person understands dealing with resource constrained systems. Sometimes it's, it's a dumb question. I hate that question. I agree.

**Dave Jones:** Sometimes the correct answer can be, that's a dumb question. I, you know. I like that. I've, I've said that in an interview. People have asked me a question. I go, that's a dumb question.

**Chris Gammell:** Have you ever thought about hitting yourself, Mr. Interviewer?

**Alicia White:** I had a guy who would interview my people who would ask them, who would interview new candidates. I would ask them, uh, what does this evaluate to? And it would be I equal five and then I plus, plus, plus, plus, plus, plus, plus. And he would want to know what, what does that evaluate to it? And my response to that is that evaluates to me firing you for your crappy ass code.

**Chris Gammell:** Exactly. That is the right answer. Yeah.

**Alicia White:** I care what it evaluates to.

**SPEAKER_01:** Yeah. Oh, goodness.

**Chris Gammell:** So, uh, okay. So, so obviously you have, you have a good deal of experience in firing people. Why, why did you make the jump back? What, what, uh, what made you come back to the, yeah. What made the jump back to engineering versus, versus management?

**Alicia White:** Ah, engineering is more fun.

**Chris Gammell:** Well, duh.

**Alicia White:** I mean, I like getting my hands dirty.

**Speaker ?:** Yeah.

**Alicia White:** I, I, so every job I've had, they've tried to make me manager. Um, and then finally.

**Chris Gammell:** She writes stuff down. Quick.

**Dave Jones:** Give her people to, to talk to. This isn't a sexist thing, is it?

**Alicia White:** No, I don't think so. I, but I am very naturally organized and I.

**Dave Jones:** Oh, right. Yep. And that gravitates you towards. Yep.

**Alicia White:** And program management.

**Dave Jones:** And it makes the appearance you should go towards that.

**Alicia White:** Yeah. And I, I mean, schedules, people look at schedules and they're like mystified and I'm like, oh no, you just do this and this and this. And if you make this bottle point go here, then I'll work out fine. Nobody will, will feel too pressured. And once they do that, people are like, oh, well, clearly you're a manager. Yeah. But that's just playing Tetris with time. That's fun. Yeah. And then finally I did become a manager at ShotSpotter and, uh, it was kind of cool. It was way cooler than I expected. I quit fighting it and, um, and suddenly my new role in one project.

**Chris Gammell:** Give in to your dark side.

**Dave Jones:** Yeah. I could feel the power. If only you could feel the power of the dark side. Yes. So you said it's relevant today.

**Alicia White:** So my role there.

**Dave Jones:** Be a manager or be not. Was to ask questions.

**Alicia White:** Like, are you done yet? And how can I throw money at this problem to make it go faster? And at the end of six months, they'd finished the project and it was under budget and early and everybody thought I was a genius manager. And I'm like, you know, I could have been replaced by a little button that just said that in meetings that wasn't.

**Chris Gammell:** Yes. But it's not, it's not the, it's not the, uh, the amount of force. It's the correct placement of force. Right.

**Alicia White:** Um, so that was, it was actually more fun being a manager than I expected there, but that's not what I want to do. I like the technical track.

**Chris Gammell:** Yeah. Well, I mean, as a consultant, you know, going back into consulting then, I mean, you gotta, you gotta do both, right? I mean, you're, you're just as much, uh, in charge of, of your time and client's time and everybody else's time in order and, you know, in order to get stuff actually delivered. Yes.

**Chris Gammell:** So.

**Alicia White:** And I do manage my clients some, you know, when are, when are we going to have a hardware and, and how is that going to lead us to a product? And just asking the right question, it provides more value than just typing on my computer, like, uh, the coding. Yeah.

**Dave Jones:** There are clients who expect the consultant to actually manage the project for them.

**Alicia White:** Yes.

**Dave Jones:** Which, you know, they, they, they just assume, oh, you'll take care of it. You know, you'll handle everything. And it's like, well, you know, it's not, that's not what you sign on for a lot of the time.

**Alicia White:** And so many consultants don't, and they don't have those skills. They have the good technical skills, but they don't, all they do is what they're told. And I feel like those clients are like toddlers in traffic. And if you get the wrong consultant, you are so host.

**Chris Gammell:** So does that mean you're like Frogger then? If you're good at that then?

**Alicia White:** It's the same skill. Yeah.

**Chris Gammell:** Yeah. Okay.

**Alicia White:** All right. And it's the same result when you screw up. Yeah. Splat. Splat. Oh, man.

**Chris Gammell:** So what, what about like the range of your client, your normal clients? I mean, so you, you said ShotSpotter was your full-time job, but, uh, are you working with more like early stage companies, later stage companies, startups, experienced companies? What, what about those?

**Alicia White:** Um, my broad range of skills, it starts to become less interesting, at least to me, if I'm working in a company, it's more than 50 people. So I'd prefer to be in a very small environment. Um, because it does let me exercise some of the product and program management to say, well, what about, and then be able to push a company this way or that way. Um, and so I like that. Uh, I occasionally will do work for a larger company, but it's usually a search and destroy or come in as a fixer for a couple of weeks to help get back on track. Yeah. Right.

**Dave Jones:** For those out there who want to get into the field, do not take those jobs. Come in, fix it up. It's a rig game. It really is.

**Chris Gammell:** It'll just be a week, Alicia. It's just, don't worry. Just come on in. All those noobs out there. We'll give you a cube and you can just, you know, come in and fix it and it's fine.

**Dave Jones:** Oh yeah. And this whole, our whole team of 10 people couldn't fix it. Now we expect you to fix it.

**Alicia White:** And fixed bid for that. Yeah. Oh yeah. Contractors don't do a fixed bid right away.

**Chris Gammell:** No, no, no, no. That can go great when you're, when you know exactly what the problem is before you already get in there. Yeah. Yeah.

**Dave Jones:** And, and you can milk it and you can be the hero at the last minute. Oh, it's all going to, it's all going to hell. But no, you come back in, I fixed it. Look at the 11th hour. I fixed it. I'm a genius. And you knew all along what the problem was. You were just holding off, you know, just to appear to be the hero. That's another tip for the newbies out there. Don't fix it straight away. You know, keep them on the line a bit, you know, reel them in.

**Alicia White:** You got to make it look hard. Otherwise, why are they paying you?

**Dave Jones:** Totally. Exactly.

**Chris Gammell:** So how much of the, so like for the smaller companies then, because, you know, you write in your book as well about a lot of the system architecture and the design and stuff like that. And I think that's also interesting from, you know, because you mentioned like young people don't necessarily, younger engineers don't get to necessarily do that as well.

**Alicia White:** You sound so old when you say that. Now say, get off my lawn.

**Chris Gammell:** Get off my lawn. I am in my third decade. I'm just saying, you know. Not for long, but. Wait. Fourth decade. I'm in my fourth decade. I get to say that. I've started my fourth decade, right? Yeah. Yeah. Okay. Yeah. You figured it out. Well done. Right. Yeah. I'm an engineer. Anyways. So how often, how often with these smaller companies do you get to actually do that? Like that. Do you like tear it all down and tell them like, no, you have to go back to basics and re-architect this kind of thing? Or what is it? What happens there?

**Alicia White:** I don't like telling people to throw away their whole system. I don't like telling people to throw away their code. But somebody wrote this for a reason and they had some insight that I didn't and that I won't until I start to rewrite it.

**Dave Jones:** Yeah. But even if it really, really sucks and it's obvious that it really, really sucks. Yeah. I know.

**Alicia White:** I know. And I try never to say it. And then I eventually, three months later, say, oh crap, I should have thrown it all away. Okay. But different clients want different things. A lot of people want me from the start or from, to do the system architecture and then do a prototype and then get out. Which is, I mean, it's totally fun because they want me to design their system. Yeah.

**Chris Gammell:** You get to do all the cool part. Oh, you get to manufacture this. Don't worry. I'll be on to the next thing. I'll be two down the line.

**Alicia White:** Turn the crank and optimize. It'll be fine.

**Chris Gammell:** It's easy. What could possibly go wrong?

**Alicia White:** But I also do like to see things ship. So sometimes I get to see the whole cycle. And right now, one of my clients, they have a whole ton of code and I have been trying to use their code and occasionally throwing bits out. Who uses floating point divide and interrupts? It's just wrong. Wait for it. Wait for it. Wait for it. So I get to see lots of things and I do a fair amount of system architecture because of the book and because I have a decent reputation. I mean, last summer I worked on an IMU with a whole bunch of people that I'd worked with at a different company on an IMU. And what they wanted was how fast can we get the basics working so that we can go back to working on algorithms. And I know it's a Lego project. You can go to SparkFun. You buy an accelerometer. You look at the specs for all the gyros that are out.

**SPEAKER_01:** Yeah.

**Alicia White:** So that was, I mean, it was great fun. And now they're going to productize it, but they don't. And what they want from me now is to hire their team. So, sure. I can interview people. I'm good at that.

**Chris Gammell:** Have you read the last part of the chapter, guys? I mean.

**Alicia White:** I interviewed at a company and, you know, that day they had done a Google search and realized that I wrote a book. And then magically somebody had the book on their desk and they, the whole, it was a team interview. They were supposed to all five of them interview me. And, and then they seemed really afraid. They were totally embarrassed to ask me questions. They were just, it was hilarious.

**Chris Gammell:** That would have been better if they would have just asked you one of your questions by accident.

**Alicia White:** They did say that one of their standard questions was in my book. So they were going to try something else.

**Chris Gammell:** Darn. If you'll just turn to page 37.

**Dave Jones:** I love it when you get to an interview and your reputation precedes you. That's always a good thing. I know. That is never a bad thing.

**Alicia White:** No, no. I'm sorry. That's not true. I disagree.

**Chris Gammell:** Don't agree? Give us the situation where it was bad.

**Alicia White:** Well, in about 2001, 2002, the episode two of Star Wars came out, Attack of the Clones. And, um, I went to the premiere. It was so cool. It was a charity thing. And I got all dressed up and, and took a picture with Chewbacca. And for the next six months, every time I showed up at a new client, they had the picture of Chewbacca and wanted an explanation. So it wasn't a good reputation thing.

**SPEAKER_01:** Darn you, Google image search.

**Dave Jones:** So they were actually using Google image search in your name, were they?

**Alicia White:** They were just using my name and the picture had gotten picked up by Reuters.

**Speaker ?:** Oh.

**Dave Jones:** Right. Okay. Into, yeah, because your name's not that generic, especially with that spelling. I would expect. So. Yeah. Yeah.

**SPEAKER_01:** Hmm.

**Speaker ?:** Right.

**Dave Jones:** But why would they care? Yeah, exactly.

**Alicia White:** Oh, and they mostly found it funny.

**Dave Jones:** And would you want to, well, would you want to work for a company that had a problem with that? It's like, well, screw you. Yeah. You know?

**Alicia White:** I mean. No, no. Nobody was like, you can't work here if you're going to date Chewbacca. What are your wookiest? It was just an odd way to start a technical interview.

**Dave Jones:** Yeah. We don't hire socialists, prepperists, or wookiest.

**Chris Gammell:** Okay, so you're going to hire, you tell people how to hire people. That's good. Obviously, you care about people coming into the field. So aside from reading your book, and maybe if there's an analog engineer that wanted to get into Embedded more, what steps should an engineer take to get into the Embedded field, in your opinion?

**Alicia White:** Buy an Arduino and make a robot.

**Chris Gammell:** Damn, too easy. All right, next question.

**Alicia White:** Well, Arduino is so cheap, and it's so easy to get started with. And underneath the Arduino-ness, there's a beautiful processor. I mean, that Etmega is just a really cute little processor that I would use in products. And so if you realize, oh, wow, this is really fun, the Arduino, but, you know, I don't have enough space. I don't have enough time. I want to get further. I'm going to buy a JTAG. And now you've got a platform to do really cool stuff.

**Dave Jones:** I wouldn't have labeled it as cute.

**Alicia White:** Well, cute's kind of my generic word for good. So, you know, maybe that's a gender thing.

**Chris Gammell:** It could be. It's adorable. So what about processors aside from the Etmega, then? Do you have other go-tos?

**Alicia White:** It seems like everybody wants to use a Cortex-M3 and something. I feel bad for the Cortex-M0s. Everybody said they were going to be like, oh, super low power. And everybody's like, no, I'll just run an M3 at a lower clock rate.

**Chris Gammell:** We do want some MIPS after all.

**Alicia White:** You want, yeah, you want the opportunity.

**Dave Jones:** Are there any significant differences apart from that?

**Alicia White:** From the M3 and the M0s?

**Dave Jones:** Yeah, the M3 to the M0s.

**Alicia White:** Some of the M0s come in a smaller package. And the M0s can't access as much flash and RAM, which is how most people get pushed up into the M3s. They realize, oh, my program is a little bigger than I thought it would be.

**Chris Gammell:** Then they call you and they tell you to make their code smaller. It's either I'll call you or go up to the M3, right?

**Dave Jones:** Yeah. Although, at that sort of level where you've realized, oh, I need hundreds of megabytes of RAM and stuff like that, are you up into the territory of just running embedded Linux on a Raspberry Pi or something?

**Alicia White:** For hundreds of bytes? No.

**Dave Jones:** At what point do you go, well, look, bugger it. I'm just going to run a complete, hugely high-level OS and be done with that.

**Chris Gammell:** That's a big jump, Dave.

**Dave Jones:** Yeah.

**Alicia White:** I mean, that's the difference between spending $4 on your board and spending $40 on your board. So it is a pretty big jump. And it's the difference between making it wearable and making it totally not wearable.

**Dave Jones:** Yeah, but no, I'm not talking – yeah, but you can re-engineer the board, right, because these things are open source. You can re-engineer it. You don't have to pay for the actual board and then put shields or capes or whatever it is on top.

**Alicia White:** Yeah, but those processors are pretty expensive.

**Dave Jones:** Yeah, but I'm saying if you're after hundreds of – you know, if you need all that sort of memory, aren't you up in that sort of high horsepower area anyway? Not always because, you know, you can have like a low-power data logger and you need, you know, gigabytes of login memory or something. No. I'm just talking a bit generically.

**Alicia White:** No, but little processors still do a lot of stuff. I mean, well, this is some bias because I kind of like embedded Linux, but if I have my choice, I will rip out any RTOS. I mean, my book actually doesn't cover an RTOS at all because I prefer to go bare metal or with a little dinky scheduler message passer.

**Dave Jones:** But what if you've got a user interface? What if you've got a touchscreen GUI interface and you're talking to SD, saving to, you know, SD cards and drives and networking and doing all sorts of that? Surely you wouldn't do that from scratch.

**Alicia White:** Oh, no, probably not. But there are Cortex-M3 TCP IP libraries that go on a number of different RTOSes. So SD cards, you can spy to them if you're willing to. Oh, yeah, that's pretty easy. That's trivial. And user interfaces, as long as it's still got pixels, you're fine.

**Chris Gammell:** Yeah. Yeah, if you're not driving like an OLED or something crazy, right? Or even if you are, you can offload it sometimes.

**Alicia White:** Color OLED, yeah, those are a bit much. Yeah. But there is also offloading it. Oh, and my favorite processors, I do have to shout out to the TI C2000 line. Because I have loved that line for as long as I, at least 10 years, maybe 15. And it's still around in the Delphino and Piccolo variants. Yeah. And it's just, I mean...

**Dave Jones:** And why, shall we ask?

**Alicia White:** Well, because anytime I'm using it, I'm doing something neat and mathy. I like math.

**Chris Gammell:** Motor stuff, you're using it for motors as well?

**Alicia White:** I'm using Piccolo's for motors now. And we used the original C2000s on the inertial measurement unit audio processing for some projects. Yeah.

**Dave Jones:** How is it better than something else for the task? Or is it just because you did a cool project and that happened to be the process you used? So, therefore, that process is cool. No, no. Is that...

**Alicia White:** It's a DSP. So, it's got special goodies for doing FFTs fast. And so, Fourier domain stuff.

**Dave Jones:** That's cool. Yeah.

**Alicia White:** You're not going to get that on a Cortex-N3.

**Dave Jones:** No. Typically, you might have a FPGA or a DSP coprocessor or something like that to do that sort of heavy lifting.

**Chris Gammell:** I mean, I guess that kind of gives us an idea of some of the realms of stuff you're doing with the DSP type stuff. I mean, what would you say percentage-wise in terms of, like, size of code base and size of, I guess, not really size, but, like, horsepower of processor? Where are you mostly operating with?

**Alicia White:** Under 60 megahertz or 60 megahertz and below. If I see a half meg of RAM, I have no idea what to do with it. That is so much. Oh, my God.

**Chris Gammell:** Yeah, right. So, I guess I'll put some MP3s in there or something.

**Alicia White:** I'm totally going to make this thing run steady at home. Yeah. Yeah, exactly.

**Chris Gammell:** I'll make this into a space heater by just crunching numbers.

**Dave Jones:** Bitcoin mining. Yeah.

**Alicia White:** And a half meg of flash. That would be a lot for me to fill with code. I could just have jump tables everywhere.

**Dave Jones:** Well, it pretty much is for the embedded systems you're talking about that don't run a really high-level OS, you know? I mean, if you're just sort of, you know, doing your own thing at the bare metal sort of level, then, yeah, you know, a few hundred kilobytes is a ton of flash.

**Alicia White:** Well, and if you need to respond really quickly. I mean, the robotics is a good one. Yeah. We don't have an RTOS because the RTOS's latency just isn't worth it to us. A lot of the audio and visual effects, you have to be at least aware of what your RTOS is doing.

**Chris Gammell:** Well, there's always that weird trade-off, too, with, like, real-time stuff. Like, if you need tons of processing, you're going to probably offload it anyways, right? Like, an FPGA, like Dave said, you know, do some kind of streaming type thing if you really, really need it. And if you need to be small, then, you know, like, the RTOS kind of fits in that middle ground, right? I mean, somewhere between the two.

**Alicia White:** Yeah.

**Chris Gammell:** I always think you have to go RTOS when you start doing stacks. Anytime I hear stack, and I'm like, oh, got to throw RTOS on there.

**Alicia White:** TCPIP stack must need RTOS. Bluetooth stack might need RTOS.

**Chris Gammell:** Unless you offload it, which is so much easier.

**Alicia White:** And then you start offloading your code to the system on a chip, and then suddenly you don't have a processor anymore.

**Chris Gammell:** That's right. Exactly. And then I call you, and I just make you do the whole thing anyways, right? It's just, this is easy. Dave, let's go get funding and make something and call you to make it for us.

**Dave Jones:** Are you a fan of multiprocessor solutions? Other solutions like, oh, throw in a little 30-cent micro over there just to do that one little task. Bugger off. I'm going to, you know, or do you like the one processor to rule them all? That's a good question.

**Alicia White:** So we've, I have been using.

**Dave Jones:** That's why I asked it. See, Chris, this is how it's done.

**Chris Gammell:** Don't be an ask, Dave.

**Alicia White:** So I've been seeing a lot of small coprocessors, small cheap coprocessors that are super low power, that essentially handle the minimum amount you can do with a UI, and then wake up the big processor whenever they actually need stuff. And unlike that, it's not my first go-to solution because of compilers. And this is probably a rant that you don't want me to get into, but...

**Chris Gammell:** No, bring it. Bring it on. Come on. We want it. We want to bring it.

**Alicia White:** Embedded compilers are just not as good as I want them to be. And they're so freaking expensive. Yep.

**Chris Gammell:** You're talking about like third-party tools, right? Not the ones that come shipped with like, oh, you get 64K. Right?

**Dave Jones:** Well, they're not as expensive as they were when I was a boy.

**Alicia White:** But, man, sometimes I use Microsoft Visual Studio. And I hate using it because it makes me feel dirty. But... It's freaking dirty, yeah. But then I use it as like a... I'll debug with it. I'm like, oh, this is so nice. I can see all the variables. I can have as many breakpoints as I want. It does smart things. I can have tracebacks and like go back and... But on embedded compilers, you know, you're lucky to get one, maybe two breakpoints. And I understand the hardware limitations of all that. But still... Mm-hmm. And they're buggy and they crash. And so if you're talking about a two-processor solution, don't forget that means two different compilers probably.

**Dave Jones:** Two different toolshines and everything else. And they don't talk to each other either, right?

**Chris Gammell:** Yep. Unless... Well, even... I guess even if you had two in the same family, right? If you use the same processor twice, you'd still need two separate ones, right? There's no way to do debugging on both at the same time.

**Alicia White:** Oh, I can sometimes bug both at the same time, especially if you use virtual machines to do some of your debugging.

**Chris Gammell:** Mm-hmm. Okay.

**Alicia White:** And my partner and husband, Chris, is like a big... You must use VMs on all client stuff because it's so much better than I just disobey.

**Dave Jones:** I've never used a virtual machine, you know.

**Chris Gammell:** Well, then when you're frantically trying to recover something, he just clicks a button and it's backed up, right? And he laughs, yes. Yeah, it's great. Yeah, yeah. But he works. Right.

**Alicia White:** So you can dual debug, even without VMs, you can dual debug using two JTAG modules. But why use two of the same processor? At that point, just, you know, double the clock speed or whatever it was you needed.

**SPEAKER_01:** Yeah.

**Alicia White:** But if you're doing a $0.30 MSP430 and a $3 Cortex, then those are different chains. You're not even talking to the same thing.

**Dave Jones:** Yeah, totally. But you often don't have to debug them at the same time because the reason that you would, to begin with, to actually make that decision to separate them out, that task out, means that it's a totally independent, verifiable task and you don't have to debug them at the same time.

**Alicia White:** But you still have to buy both compilers.

**Dave Jones:** Yeah, but these cheap micros, you don't have to buy the compilers for them. I mean, if you're talking about the picks, if you're talking about the, you know, the admils and the ones like that, the $0.30 micros, there's free compilers. Free compilers are plenty.

**Alicia White:** But there is some mental cost. I mean, they're fun, so I'm not really going to complain about learning new stuff. But if you are running a team of three or four people and you want them to be able to go back and forth between them, it's just one damn more thing for you. Oh, totally. Yeah.

**Chris Gammell:** Yeah. Well, that's how I always think about these little, these little processors are great for offloading tasks, but I always think about like managing firmware as well. You know, like I've actually rejected like a lot of, a lot of the, like, again, I bring this, this same damn chip that we've been talking about for the last four weeks, but like these, these ADUCM 350, 360 ones from ADI, which are like these awesome all-in-one chips. But then it's like, I don't want to write code for that. I don't want to have, I don't want to have to manage that stuff. I just want, I'd rather have one main guy that's talking spy, even if it's a little bit slower or something like that, and then not have to have a second firmware image. Cause then what happens if it's out in the field and you, and you find a bug, you're screwed, right?

**Alicia White:** I mean, I mean, usually one of the processors has to pass the code to the other processor. Please don't lose power during that time. And you can design good bootloaders for, for passing code around, but it just is one more thing to go wrong.

**Chris Gammell:** You could put in a self-destruct if it doesn't actually update properly, right? The whole board just explodes. It'd probably be, it'd probably be easier.

**Alicia White:** You were joking, but I've worked on military devices, so yeah.

**Dave Jones:** Yeah, me too. I've, I've designed a product that actually scuttles itself to the bottom of the ocean after X amount of hours.

**SPEAKER_01:** That's awesome.

**Alicia White:** Mine just, you know, quietly self-destructed the chip. There wasn't even smoke. Self-destructed in what way?

**Dave Jones:** It just overwrites its own program memory?

**Alicia White:** Yeah, overwrites its own program memory. Loads itself into, loads its little bit into RAM and then flashes the memory a few hundred times.

**Speaker ?:** Right.

**Dave Jones:** Well, if you did it a few, like 10,000 times, bang, it'd just wear itself out, wouldn't it?

**Alicia White:** It did it until its batteries died.

**Dave Jones:** All right.

**Alicia White:** I mean, if you're trying to destroy something, you might as well continue until you're done.

**Dave Jones:** Yeah, right? Yeah, exactly. Guy for a break.

**Chris Gammell:** All those, all those, all that charge is sitting there waiting to break something. So it's just, yeah. So, so what about, what about the dealing with like all the firmware side of things and the updating and like updates? Like, I mean, do you, is that a large part of your, your task as well is kind of thinking about strategies for that?

**Alicia White:** Well, there, there aren't that many different strategies for it, but yeah. Um, and, and being a little bit paranoid helps because there's always the chance you're going to break your unit and totally make it non-functional. Um, so yes, absolutely. That, that is one of the harder firmware tasks. I think, um, making, making the robot go is not as hard as making the robot go after you've changed your mind about what it was supposed to do in the first place.

**Chris Gammell:** I like that. Yeah. What about, uh, making the robot go to sleep and, uh, not waste his batteries?

**Alicia White:** Power optimization. I like power optimization now. Um, I know it's sexy, isn't it? It is. I like it. Because, you know, I did all this optimization fairly early in my career learning how to put, put things small and make them fast and just optimization because the processors weren't big enough to do all the stuff we wanted to do. And now it's all coming back in power optimization because you still have to be small and slow or fast. And sometimes you run the clock speed differently so that you can just eke out a little bit more, a little bit less power. I, I, yes, I love that. What was the question?

**Chris Gammell:** There wasn't one really. I just said, you know, robots need to shut down and sleep sometimes. But it's, you know, it's, it's interesting because it, it, it felt like, I don't know. I haven't been around that long, I guess, but it, it feels like it should, this shouldn't be a problem anymore, right? It's like, oh, well, things keep getting lower power. You know, the, the transistors keep getting smaller and there's less consumption there. And yet, yeah, this stuff is still like a really big deal. I mean, like trying to find ways to save battery life and make it, make, make, uh, devices last longer. Or you'd think, my new batteries haven't gotten any better, so that's not helping. But I don't know.

**Alicia White:** Well, you mentioned last week that I, I worked on something like Fitbit and I will correct you on that. I worked for Fitbit. Ooh. When they were, um, they were about 20 people and three firmware engineers. And, uh, and now they're like 20 firmware engineers and a lot more people. Oh, wow. So I don't work, I don't work as much with them. I work a little bit with them sometimes, but just maintenance stuff.

**Chris Gammell:** Are they all fixing your stuff now? Is that kind of the idea? No, no. Because you get to do the architecture?

**Speaker ?:** Because you get to do the architecture.

**Alicia White:** They're working on fantastic new products. And I wish them all the best. And I'm excited for when those products get announced because I don't have to remember not to say anything. Yeah, right. But that's a power optimization problem. I mean, tiny battery, bright screen, uh, things that are always need to always be on and doing something and yet sucking as little power as possible. That was, that was fun. I mean, robots, robots are a little harder to go to sleep, not because there's any real difference, but because they have to be connected to some large power source anyway. So why bother?

**Chris Gammell:** Right. Yeah. Yeah. If you're cranking amps through a motor, who gives a shit about, uh, milliamps? Yeah. It's like, okay, well, you know, I guess it's a little warmer now. No big deal.

**Dave Jones:** Uh, but you can't just go pissing away a couple of milliamps here and there willy nilly. You've got to, you know.

**Speaker ?:** You can't. No.

**Alicia White:** If you're using wall power, everybody does it.

**Chris Gammell:** Yeah. Yeah. I agree with that.

**Dave Jones:** Well, that's no reason to do it because everybody else does it. Everybody else is jumping off the bridge. I'm going to do it too.

**Chris Gammell:** I don't know. I'm totally with L on this one. I mean, like.

**Dave Jones:** No, no, no.

**Chris Gammell:** If you have, if you have a power cord, if you're dealing with all the crap you have to deal with having a power cord coming out of it, you might as well take advantage and not worry as much about the power stuff.

**Alicia White:** No, I, I kind of agree with Dave actually, because it is, it is a fail. I mean, you, you're destroying the environment with your milliamps all the time, but from an engineering perspective.

**Chris Gammell:** No, no, wait a, wait a second. Wait a second. Dave loves test equipment and having worked on test equipment, I will say that the digital sections help to heat up the analog components and stabilize the temperature. How about that?

**Alicia White:** Says the analog engineer. That's right.

**Chris Gammell:** You need stable temperatures. The faster it gets to ADC, the better.

**Dave Jones:** Analog, when in doubt, throw heat at the problem, you know.

**Chris Gammell:** Oh, God. So, so what, I mean, so what do you do in that case then? So you like shut things down or you do like, like sleep cycles or how are you doing that?

**Alicia White:** Well, processor dependent, but sleep cycles, you know, we PLL the clock so that you only have to put in eight megahertz or sometimes even three megahertz to get up to a 30 megahertz clock. And so you turn your PLL down and now you're drawing much less power. Or many processors have actual sleep instructions and they wake up for a limited number of interrupts. You design your system so the important interrupts are on those interrupts. And, and when you need to wake up and do something, you do it as fast as possible so you can go back to sleep, which is kind of how I do engineering really, kind of lazy.

**Dave Jones:** I love the processors that have little dedicated hardware things in them. Like they'll have a, you won't have to run the process at all. Like it'll have an analog to digital converter that just works on its own, takes a measurement, wakes up, just the ADC part wakes up, takes a, on a timer, takes a measurement and goes back to sleep and stores it without the actual processor waking up. I love those.

**Alicia White:** And then it wakes your processor up when your FIFO's full. That's just brilliant. That's how it should work.

**Dave Jones:** Yeah, I know.

**Alicia White:** I totally agree.

**Dave Jones:** I know. It's great. Yes.

**Alicia White:** Awesomeness. Which processor are you talking about?

**Dave Jones:** Oh, there's lots of them. Almost. Oh, okay. Most families will have, you know, well, you know, the, the, the Atmels do it somewhere. The, uh, microchip PICs definitely do it. And, um, I think the Renesys ones do and, you know, quite a few. And TIs do it too. Yeah.

**Alicia White:** That's what I was thinking of.

**Dave Jones:** Right. Okay. No shortage of them.

**Alicia White:** I just wanted to know if there were other processors I should be playing with.

**Dave Jones:** Oh, there's, well, there's countless ones. I mean, geez, it's almost too hard to make a choice. You know, starting a new project. Oh, what processor am I going to use? That's why most engineers just work with one they've worked with before. Because, well, even if it's not the most optimum solution. Because they're familiar with it. And that's a perfectly valid.

**Alicia White:** It's not a bad solution.

**Dave Jones:** Yeah, exactly.

**Alicia White:** Yeah. Well, and, and then I go back to, I have all the tools and I know how to use them.

**Dave Jones:** Because it's often more important to get the project finished. Well, exactly.

**Alicia White:** Yeah.

**Dave Jones:** You know, at the end of the day, engineering is getting a job done by a certain amount of time at a certain budget. Right? With a certain amount of resources. That's engineering. Otherwise, you're just mucking around. Otherwise, it's just hobby.

**Alicia White:** Oh, getting things done?

**Dave Jones:** Yeah.

**Alicia White:** I think everybody at some point in their career should really think about working for a consumer product. Because seeing my products on Target's shelves was so addictive to getting things out. Right.

**Dave Jones:** Yes.

**Alicia White:** Totally made me want to just ship it. Whatever it was, ship it. Because I want to go to Target and see it.

**Speaker ?:** Right.

**Dave Jones:** See, I worked at the other end of the spectrum where most of the projects I've worked on in my career have been shit canned. They've been cancelled before they actually shipped. And, you know, that could be a bit demoralizing.

**Alicia White:** I was wondering if they left LeapFrog is they cancelled my toy line. And I was like, yeah, why am I here? I'm not going to wait for next year's toy line. Right. Give me some really complicated toy. And I like the little ones.

**Dave Jones:** With fur on them, preferably. A little cuddly furry toy that talks back to you or something. Come on. And that's... Oh, boy.

**Chris Gammell:** So, LeapFrog is your... That's the main ones that we would have seen on the shelf. Any other shelf-based things that we would have seen of yours?

**Alicia White:** Well, Fitbits are on the shelves. I worked on the...

**Chris Gammell:** All right, yeah.

**Alicia White:** ...one and a little bit on the Flex and Force. I'm trying to remember their real names, not their codenames. Right. And the ARIA scale. So, those are all currently on the shelves. My Fitbit... Or my LeapFrog toys, none of them were on the shelves at Toys R Us today. But some of them had my code in them, which was fun. Because I had to go play with those.

**Speaker ?:** And...

**Chris Gammell:** Did you... I don't know. Did you... Did you program, like, back doors like Jerry did with, like, fart noises and stuff? Or do you do anything fun like that?

**Alicia White:** Yes. Well, no, there was one toy that everybody hated. And I... Naimus.

**Alicia White:** I did get an Easter egg for that one that ended up being very cute. And cute in a really adorably cute real way. Not in my normal cute. But everybody... It was a toy. Violet is out now for LeapFrog. And they... You can add your own voice to it. So if you're giving it to your kid and you want it to say, Mommy loves you, but in your voice.

**SPEAKER_01:** Right. Creepy.

**Alicia White:** And so we had... We were doing that, like, ten years ago. And... And... It was kind of a beast. Because we were recording and playing back. And there were robotics involved and blah, blah, blah. And the... I totally forgot what I was going to say.

**Dave Jones:** Please tell me that you've embedded a Yoda voice in there somewhere. That'd be awesome. Oh! Oh! Do your homework, you will.

**Alicia White:** The Easter egg.

**Dave Jones:** Yeah. The Easter egg.

**Alicia White:** Right. So if you push the buttons in the right order, it would say everybody's name as though it was Romper Room. And everybody came over to my house and recorded them saying their own name. And so it was this kind of mini tribute to the 15 people who had worked on this toy.

**Chris Gammell:** Oh, nice.

**Alicia White:** And it was really... I mean, people would play it for their friends. And it was clearly you. Clearly you saying your name. And it was a good Easter egg. That is a good Easter egg. It was a happy Easter egg. I think it made people hate the product less. I mean, not the final customers because they never knew about it. But the people who were working on it who were all demoralized. It was better.

**Dave Jones:** Why was it so shitty? Was it a bad idea? Was it bad management at the time?

**Alicia White:** No, it was six good ideas all smacked together.

**Dave Jones:** To create a fail.

**Alicia White:** And, yeah. And there were... Leapfrog was one of the first companies that, you know, that put a whole alphabet on a toy. Before Leapfrog came around, Fisher-Price would have these little buses and it would say A, B, C, D, E, F. And then it would just stop as though that was all you ever needed to know.

**Chris Gammell:** Bunch of kids walking around not knowing their alphabet because of the...

**Alicia White:** Because, you know, it was kind of educational. Right. But Leapfrog would put the whole alphabet on except their infant and preschool line, sometimes they would put the whole alphabet on the chest and it made it hard and uncuddly. And many of us wanted this particular mommy loves you toy to be super cuddly. And with the alphabet on the front, it just... I think that was the deal breaker. Is that we didn't want the whole alphabet. We should have just had a couple of glowy bits or the triangle square thing they do sometimes.

**Chris Gammell:** Yeah. Right. I'm always interested with the whole toy industry side of things. Like, so I've talked to... I've talked to... Obviously, you've been in the toy industry. Jerry's been in the toy industry. Todd Bailey, an analog slash embedded guy. You know, I just... I've never had any personal experience with it. It sounds like it's like this awesome gauntlet of like fast release, like you mentioned. And then... But then the thing that I don't understand is like... It's... I would hate to think about all these things I worked on just like sitting in a toy box somewhere. So is there any of that? Or is it like, no, there's just aren't too many other problems to worry about?

**Alicia White:** Oh, you mean that it's going to go to waste?

**Chris Gammell:** Yeah. I think... I mean, like, it seems like these really elegant, like, fast solutions. Right? I mean, like, these elegant uses of constrained resources. And then it's like, oh, and, you know, well, the company in China didn't really make it right. Or, you know, like, it's just like, you can do everything right and there's still a lot that can go wrong.

**Alicia White:** You're a pessimist. I didn't know that. You always sound like an optimist.

**Chris Gammell:** It's the happy tone of my voice. It's really the Ohio accent.

**Alicia White:** Yes. Yes, of course. And I have been to yard sales and seen my toys being yard sales, which is kind of depressing. But I also worked at... Leapfrog would let me take, like, a half day off to go help in a kindergarten. And I took some of my toys, one of which was the most freaking annoying karaoke. You were supposed to sing along to it and voice change. But it was... Oh, God, it was a karaoke. It was horrible. And this little boy didn't know his alphabet when he got to kindergarten, which I guess now is you're supposed to. Yeah. And he was falling way behind and the teacher was just kind of depressed about it. And I played with lots of the kids and he took the karaoke home with my permission. And a week later, he knew his alphabet and he was catching up to class. Awesome. So it goes... Yeah. I'm sure my toys ended up being used for 10 minutes and then thrown away. And that makes me feel bad. But a couple of the kids learned something. So I'm ahead. I'm fine.

**Chris Gammell:** No, no. That is... And that's true. And, I mean, I guess that's... You weren't making, like, G.I. Joe, like, sound activation type stuff either. So that's good. The educational side, I'm sure, helps a lot there. Yeah. That is really cool.

**Alicia White:** Well, and before that, I'd worked on bombs. So, you know, it was a big win.

**Dave Jones:** It can always be bombs. It can be choker chicken, you know? What? You haven't seen those choker chicken toys that you can buy at your local electronics store? They sell them here. It's a chicken and you choke it and it squawks. You choke it. I mean, that's... And there's a whole spin-off line. There's actually a choker boss. So, like, it's your boss, you know? So you choke it. I hate my boss. And you choke it and it screams out. You know? I mean, it's just ridiculous toys like that. All those farty, novelty toys. All these spank-o-vita we've talked about before.

**Chris Gammell:** Wow. So Australia is weird. I can't believe they ever sell these things in the US. Come on, they have to. That and big spiders, right? Yeah. Oh, boy. So, okay. So how about this question? I already asked about how an analog guy could learn more about embedded. What are some of the big mistakes you're seeing over and over again? Either when you... Not necessarily when you walk into a client, but just, like, overall. What are some big mistakes you see or big misconceptions you see when people are jumping into embedded?

**Alicia White:** People think that because it runs on Java in my browser window, it should easily be able to run on my embedded platform. And people say things like, well, we had the Game Boy in, like, we had Game Boy, you know, a long time ago. This isn't more complicated than a Game Boy. Those poor Game Boy developers, like, simply coded their stuff.

**SPEAKER_01:** Yeah. Oh, my God, really?

**Alicia White:** I mean, they tuned, and it's impressive. Yeah, yeah. Or people who were like, my iPhone can do this. Why can't your $5 device do it? Like, to hell with you. Your iPhone, do you have any idea how much that puppy really costs? Yeah.

**Chris Gammell:** It's $600 on a good day. And that's because Apple probably, you know, holding down people and had a gun to their head to get the pricing, you know?

**Alicia White:** Yeah. And why do you expect your pocket device to do what your iPhone does when you're willing to pay sub-$20? That's silly. But I see a lot of that. Did you mean product things like this, or did you mean more, like, what do I see engineers do?

**Chris Gammell:** Yeah, well, kind of both. I mean, I'm interested in all this stuff, really. I mean, I was really looking at, so I was looking at, you know, chapter four and five and thinking about how crappy I am at, like, interrupts and stuff like that. And seeing how people, like, thinking about how people do that wrong, like, interrupts wrong and state machines and all that. All, like, the more in-depth stuff, like, how you see those being implemented wrong.

**Alicia White:** I mentioned the floating point division in interrupt. Oh, yeah. Yeah, that will always, man. I think dividing in general is usually pretty bad, right? Yes. Yes, and when you type wait millisecond in interrupt, you're doing it wrong. Yeah, yeah. Just a clue. I guess one of the things that if you're at that cusp of, I think I'm doing all the right things, but my stuff isn't getting better, don't be afraid of opening up the assembly with the C code, especially if you can walk through it. And C, which instructions take a long time. In C, every instruction takes a line, right? I mean, you actually can pile in a couple dozen lines on there, a couple of go-to fails, too. But when you open up the assembly, you can see how long a divide takes. When you do a floating point divide, oh, look, there's a whole library out there, and it takes a couple more hundred instructions. So I think that's something people can do to get much better. And it really helps figure out, well, why does my interrupt take so long?

**Chris Gammell:** Did you get started doing assembly, or did you start at C?

**Alicia White:** I started at C. You did? Now, I am fluent in TI assembly most, and I can read ARM assembly happily and write, you know, the boot part, but I won't write a whole lot more in ARM assembly unless I really have to. I've had a couple of clients who wanted something to go much faster and wanted me to rewrite it in assembly. And what I did with that was actually I ended up giving them back a C file because I would read the assembly and then I would tweak the C to tell the compiler what I wanted to do. And that's a really good way to optimize because in the end you end up with code that is readable. And as long as you have lots of notes that say, don't screw with this, don't change it, or if you change it, at least look at, don't do a freaking floating point divide in this interrupt. I'm only a little bitter.

**Chris Gammell:** That gets you going, huh?

**Alicia White:** Yeah, so...

**Chris Gammell:** That's good. So, I mean, I always wonder about that if I should go back and learn assembly and stuff like that. I mean, my C is pretty piss poor to start with, but, you know, so I worked with, like, a really, really good experienced embedded engineer at my last job. And I tell you, like, I will never be at the level he's at, I don't think, because, you know, he's so deep in the compiler and he would run those kind of, those comparisons to see what would be faster and slower. And he would know about, he would talk about everything in clock cycles and that kind of thing. But I just wonder, you know, I was wondering about that with how much you do need to know about under the hood stuff. Because I think for a lot of people, they don't even realize that C still has a lot of under the hood, right? It does. Like instruction sets and all that other crap that...

**Dave Jones:** Well, it's a compiler. I mean, it's not a high-level interpreter. It's a... It compiles to... Yeah. It compiles to machine code. I mean, well, it compiles to assembler and then the assembler converts it into machine code. I mean, it's, you know...

**Alicia White:** But I wouldn't learn assembly directly. I would look at what your C is doing and learn assembly that way.

**SPEAKER_01:** Yeah.

**Alicia White:** Because the assembly languages still are changing, strangely.

**Chris Gammell:** Really?

**Alicia White:** Yeah.

**Chris Gammell:** Just because of instruction set and everything else? I mean, like RISC versus CISC and all that kind of crap?

**Alicia White:** Oh, and then the processor people come up with fancy new things to do and realize they need this or that. And it's easier just to let the compiler do it. And if you need to optimize something, I don't suggest going and optimizing it by hand. Turn up that... I mean, turn up the compiler. The compiler will do a better job than you will. It'll make it hard to debug, but don't torture yourself.

**Chris Gammell:** Well, yeah. It's like a diminishing returns kind of thing, right? If you sit there all day and you have it perfectly, you can debug it really well, but your time is all spent up front. You don't have to spend any time in the back end then.

**Dave Jones:** And if you're optimizing, if you have to hand optimize the assembler to tweak every last cycle out of your processor, then you've probably chosen the wrong processor because you haven't catered for expansion. You've probably made the wrong choice somewhere along the line, I think, in terms of either processor clock speed or resources, something else.

**Alicia White:** Given how fast the processors get cheaper, I agree. I mean, I have optimized if somebody says, we really want this processor right now. But it is a little easier to just wait six months. Yes. Yeah, exactly.

**Dave Jones:** I mean, I can remember having a pick back when picks were fairly expensive. So it was a big choice to choose the next one up that had 2K flash memory instead of 1K. So I would hand code my entire thing in assembler and it had 1K of memory in it. And I used like 1,023 bytes or something. You know, I just fitted my entire application in with a couple of bytes to spare. And it was just stupid, you know, because it didn't allow me to expand. If I want to add, oh, I want to add a couple extra lines. Oops, I can't because I've, you know, I've used every last byte of my memory. If you're making a million, yes, it can matter.

**Alicia White:** Then 15 cents matters a lot. 15 cents is so much more than your salary right now. Go save me some money. How come I don't get any of this money?

**Chris Gammell:** Yeah, right. I think because at that point you'd have people, you know, designing in extra stuff at the beginning. Be like, oh, hey, boss. Just wrote myself a new mini-game. What about that? So from the resource perspective and like where you get in on projects, I mean, do you have a lot of exposure to pricing when you're, are you helping with that kind of stuff?

**Alicia White:** Not really, no. No. I mean, I keep track of the DigiKey 1K cost of some processors and some components that I like. But no, I can make suggestions. But the companies I've been working with lately either didn't care that much about prices or had a whole team to do it. Definitely.

**Dave Jones:** And then you would have forces changed upon you. You would have choices forced upon you in those cases where?

**Alicia White:** Usually A, B choices.

**Dave Jones:** Right. Okay.

**Alicia White:** Sometimes how much would you cry if I change it to this? Right. I've had that conversation many times. More like what features are we going to have to give up if I give you the lower flash processor? Yes.

**Dave Jones:** And sometimes the correct answer to that, somebody coming up and asking you that question is, I won't cry. I will stab you with this hot, soldering iron. Right in the face. That's it.

**SPEAKER_01:** Oh, goodness.

**Chris Gammell:** What about what I think Dan Sachs has made his career on? What's your feeling C versus C++? Because whenever I see Dan Sachs giving a talk, it always seems to involve C and C++ side by side.

**Dave Jones:** C++ is for new age pansies. Okay. I don't know. I'm just throwing it out there.

**Alicia White:** C++ is really useful if you are doing a user interface that involves tiling or moving things around or windows. That's an area that I would just put my foot down and say, we're using C++ because that's the way to do it. No other area has that level of my way or the highway. But I use C, I use C++. They're different. I don't think they're as different for me as they are for some people because I believe in object-oriented all the time. Modules should be encapsulated. They should have limited access points. And they should be testable. And so my modules look like C++ classes whether or not they say class or whether they just have good names. So I'm not as bugged about that.

**Chris Gammell:** So where's the limitation with that on C then? You'll have to excuse my long-term C++ lack of knowledge. But where is the limit then? If you set up all C like that, when do you run into a problem there? Is it like when you're...

**Alicia White:** Inheritance.

**Chris Gammell:** It's just that you can't do classes? Okay.

**Alicia White:** You can make classes look like other classes. But unless you're casting things, they can't just be and inherit other classes. You can do some interesting things with structures and function pointers. So I'm not going to say never. But then it starts getting really complicated and why don't you just go ahead and use C++. Yeah.

**Dave Jones:** I think I'm going to get myself a t-shirt that says global variables all the way.

**Chris Gammell:** Memory's cheap.

**Dave Jones:** Global variables for the win.

**Chris Gammell:** What could possibly go wrong with that plan? Yeah. Just... You just have to be really good at naming stuff, right?

**Dave Jones:** Inheritance and polymorphism and all this sort of new age garbage. Signal 1.

**Chris Gammell:** Signal 2. When I was a boy.

**Alicia White:** If it takes so long to type signal, you should just make them S1 and S2.

**SPEAKER_01:** Right. There you go.

**Chris Gammell:** Right.

**Dave Jones:** Real meaningful labels. Yeah.

**Chris Gammell:** You know, once you hit 64,000 or so, you could probably switch to a different letter or something, you know? Yeah.

**Alicia White:** Yeah. Well, and since comments slow down the code so much, you really shouldn't have any of those.

**Dave Jones:** Right. Yeah. Yeah.

**Chris Gammell:** Are you... Do you participate in the Obstuscated C contest at all or is that...

**Alicia White:** Not intentionally, no.

**Chris Gammell:** Not logical elegance.

**Alicia White:** Not for any reason, just because I have to untangle these things too often. I don't need to make them or not.

**SPEAKER_01:** Yeah.

**Chris Gammell:** Don't take my work home with me.

**Dave Jones:** Have you ever worked at a company where they tell you not to comment stuff? Because I have. I'm just curious.

**Alicia White:** I've had discussions with other developers who believe in self-commenting code, and I don't entirely disagree that your variable names and what you're doing should be readable. And I definitely want that of my code. But the comment is like a... It's like another channel. Like, you know, in meetings sometimes... Well, maybe you don't. But in meetings sometimes, the engineers will type at each other through some sort of IM or chat message system. And so you get both the meeting and the back chat. And so I kind of think of the code and the comments as the meeting and the back chat. And my comments, I try to make them funny or make them story-like or make them engaging. So that you do want to read the code instead of trashing it and writing your own, which a lot of times it's easier to rewrite than to read.

**Dave Jones:** I can just picture it now. Variable X loves variable Y so much that it instantiates over here and then joins up.

**SPEAKER_01:** Oh, goodness.

**Chris Gammell:** Variable X, O variable X, wherefore art thou, O variable X?

**Dave Jones:** Variable X.

**Alicia White:** Variable X code?

**Dave Jones:** No, no. This is actual product code. No, this is reusable. Yep. I wouldn't want to debug that.

**Chris Gammell:** That sounds like a manager thing. Yeah.

**Dave Jones:** It's a total... Yep. Anyway, let's not go there.

**Alicia White:** I've heard people say they don't want comments because they get out of sync and they're not maintainable. But if your comment is delay microsecond 10 slash slash wait 0.1 millisecond, yeah, that's going to get out of sync and why bother with the comment?

**Speaker ?:** Yeah.

**Dave Jones:** Right.

**Alicia White:** So, I...

**Dave Jones:** And there are those useless comments where it's like, you know, like it'll be, you know, X plus Y and the comment will be add X plus Y. You know, it's like, hello. It's like you wasted time telling me that.

**Alicia White:** I think the people who say don't comment anything see only those comments and fail to see the...

**Dave Jones:** Right. Yeah, yeah.

**Alicia White:** We're adding X and Y because...

**Dave Jones:** Because, yes. That's a comment. Because part. Yep. Although there's also those people who are of the opinion that you... Thou shall leave... Commandment. Thou shall leave no dead code. As in or no commented out code. You know, you should totally... If you're going to comment out that code, like as, you know... Delete it. Then you should be... Then delete it. Ah, you're in that camp. Okay.

**Alicia White:** Delete that code and use your version control system to pick it back up if you need it.

**Dave Jones:** Right.

**Alicia White:** Do not leave me code that is just randomly commented out so that when I come up to your code base and need to make a change, I have to grep through all of these lines that don't even exist and then try to figure out why you commented out if that's where my bug is that you accidentally left this... No.

**Dave Jones:** But what if you documented and commented... But what if you documented and commented why you commented it out?

**Chris Gammell:** No one does that. Version control. Ah, this new family stuff. I don't know. So, what if someone comments out the... Comment? The robot code. The robot code that says, do not kill humans. You're right. The Asimov laws, yeah.

**Alicia White:** Or the little comment that says, wanted to murder my wife.

**Chris Gammell:** Oops, did I leave that in there? Don't tell the lawyer. So, what about version control? Because if I... I think you corrected me on this when I was on your show, but I seem to recall you saying you hated GitHub or Git or something.

**Alicia White:** I'm not a fan of Git, but I'm not a fan of Git in a specific environment. I worked with a company who was... They were just... They were expert SVN users. And they wanted to try Git because it was the newfangled cool thing. And...

**Chris Gammell:** Oh, that's stupid.

**Alicia White:** Yeah. And then they all tried it in a different way. And there was no process. Everybody was trying their own thing. Some people were rebasing. Some people were branching here. And some people were branching off there. And it was very disorganized and crazy. And I was... I realize now that I was confused by their stupid processes, not by Git itself. And I think if I went back to use Git, I would use the command line. Somebody told me that was the key. You have to learn the command line before you can use the Torty SVN or Torty Git interface. Torty? Yeah. Tortoise. Tortoise. Yeah. Sorry. Tortoise.

**Dave Jones:** Sorry. That might be a difference.

**Chris Gammell:** That's the big jump I made, too. It was... I did GUI for a while. Then when I actually needed to do anything useful, that's when... Yeah. You got to jump to command line eventually. They also told me... The friend who was helping me is like, there's about a hundred different ways to do everything. Yeah. So... You're all right. You can kind of screw yourself.

**Alicia White:** And I don't like that. I kind of want there to be just one way to do everything. Yeah.

**Dave Jones:** Me, too. Totally. Just like choosing a bloody processor. I want there to be just one choice so I don't have to make it. Yeah. Right.

**Chris Gammell:** You know that Dave would make a video. As soon as someone said you can only use one video. Oh, and then they told me I couldn't use this processor and I have all these thoughts about this.

**Dave Jones:** I long for the days when you had to do everything in 7400 series logic because that's all you had damn well had.

**SPEAKER_01:** Yeah. Yeah. Right.

**Alicia White:** Now it's Dave's turn to say get off my lawn. That's right. Yeah. Exactly.

**SPEAKER_01:** Get off my podcast.

**Chris Gammell:** Oh, dude. So what do you think is coming up? I mean, what excites you about Embedded in the near future? Is it robots? Is it quadcopters? Is it others? I mean, what's most exciting to you?

**Speaker ?:** Hmm.

**Dave Jones:** The latest processor. Because the application almost doesn't... The applications are infinite, aren't they?

**Alicia White:** Oh, I'm way more application-oriented than processor-oriented. Ah. Okay. Processors are a tool to get from here to there.

**Dave Jones:** Oh, naive. They're an end unto themselves. Trust me. It's just a hardware engineer. Nerd.

**Chris Gammell:** Says the guy who doesn't like writing code.

**Dave Jones:** I'm like, hey. I like writing code.

**Chris Gammell:** Every time you write code, you're like, and I know people are going to complain about it.

**Dave Jones:** Yes, because they do. Because they hate my coding style. Shut up about it. I didn't do computer science. I went to the school of hard knocks coding. Thank you very much.

**Chris Gammell:** Comment stuff out. Applications. Sorry.

**Alicia White:** I think... So, we're seeing lots of LED neat things happening. And we're seeing lots of neat wearables. And I think that power is going to be interesting. You know, MicroGen is making their power generator using vibration. I think that's super cool. And I'm like anxiously awaiting their dev kit. But for applications, I want feedback. I want touch feedback. I want something that can tell when I'm touching it. And I want it to... Whether it's little actuators, little spinning motors, little vibration motors, little needles. Well, not pointy needles. But something that I can... You could send me a board and I could see what it was like, like really physically see what it would look like. But... On a 3D... Not printer, but something temporary that acts. And then if I wanted to have an online, you know, Tamagotchi sort of pet, it would actually give me the petting, purring sensation. And it would be a size, maybe a touchpad initially. But it would get bigger until it was bigger than my iPad. And it would plug into my iPad. And there'd be all sorts of games that involved me tactilely having haptic feedback. So that's what I want next.

**Dave Jones:** What you want is an iPad connected choker chicken. I'm telling you.

**Chris Gammell:** Dave, if you start... No, don't. Don't go there, man.

**Dave Jones:** Dude, I'm telling you. It's the bomb.

**Chris Gammell:** So after the show, we're going to tweet, Dave likes choking a chicken.

**Alicia White:** Just make sure there's no context. That'd be great.

**Chris Gammell:** So wait, do you mean like having a pair of gloves on and putting them into a virtual plane, like a leap motion type plane? Do you mean like that? And then the gloves give you feedback?

**Alicia White:** Well, okay, so...

**Chris Gammell:** I'm not sure I understand that.

**Alicia White:** So say there are... Let's go with gloves. Because that's definitely one way to do it. Okay. Say the gloves have 512 individually accessible, individually addressable coin cell style motors.

**Dave Jones:** Of course, it has to be a vitary multiple like that. It's important. Yeah. Just pointing that out.

**Alicia White:** Now it can vibrate the tip of your finger or just below or the back of your finger or the front. And so if you want to make it feel like you just stuck your hand in 7-Up, you wouldn't get the chilly part, but you would get the fizzy part. And if you wanted to feel like you were touching the Empire State Building, then it would actuate so that your fingers would have a hard part and a soft part and you could touch. You could touch things you can't touch. It's the next... I mean, it's virtual reality.

**Dave Jones:** Why don't you just touch the real thing? I'm sorry. I have called me old-fashioned, you know.

**Chris Gammell:** You're going to get on a plane for 17 hours, Dave?

**Alicia White:** So, coin cell motors are big. If you start thinking about tiny motors, tiny, tiny, the size of, say, 1 millimeter by 1 millimeter, that's still kind of big. But that's much tinier. And now, what if you could put VR glasses on and hold the board that you're about to design and be able to put it into, visually, the system you're about to design and make sure those tolerances are what you think they are? There's something about holding something that's better than visualizing it on the screen. And, I mean, I'm kind of putting it towards technology, but think about games. Being able to play ping pong with somebody who's across the country with your palm.

**Chris Gammell:** That'd be cool. Yeah, that's...

**Alicia White:** I'm waiting for haptics.

**Chris Gammell:** So, is that possible? Yeah, of course it is. So, what's it? Like, a coin cell motor is just a tiny motor running off a coin cell? Is that the idea?

**Alicia White:** No, a coin cell motor is the motors that are the size of coin cells, batteries. They're used in pagers, cell phones.

**Chris Gammell:** Oh, okay, okay. Yeah. I see. The ones that actually buzz when you do, like, a haptic feedback like you're talking about, right? Yeah.

**Dave Jones:** Yeah, they're the vibrators in your mobile phones, you know, those kind of little tiny motors. Yeah.

**Alicia White:** But now I want something much smaller and probably with more memory wire.

**Dave Jones:** You want nano motors and there's work going on on those. Mm-hmm.

**Chris Gammell:** That's cool.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, good. Yeah, I'd like that too. That'd be cool. I'll take one of those.

**Alicia White:** Kickstarter! Kickstarter!

**Dave Jones:** Totally.

**Alicia White:** This is all we need, right? We have a plan. Dave can make a video. It'll be fun.

**Chris Gammell:** Yeah, you're going to make a video. Yep. Nothing. Yeah. We're looking to raise $1.7 billion. Exactly. Exactly. We want to hire DARPA. We want to hire DARPA.

**Alicia White:** So, I'm not working on anything like that. That's just the big next application that I want to see has to do with a lot of the force feedback and haptic sensors, which goes really well with the VR systems that are coming out.

**Chris Gammell:** Yeah. Oh, yeah. Like, well, like Jerry and like the Oculus. Yeah. A bunch of others. Yeah. Yeah. That'd be really cool. I don't really do games. But I think every time I see a game application like that, I always think, how can that be used for CAD? That always seems like the first thing my mind jumps to.

**Alicia White:** I'm playing this game Threes on my iPad, and it involves adding up Threes to make Tetris-like things, and it's algorithmic, and it's, oh, it's so good. But my thought is, this is totally the part of my brain that loves coding, and it's doing this. And so, there should be some application. But I don't know what it is.

**Chris Gammell:** Like add up Threes, and it does like a nuclear launch code or something?

**Alicia White:** No, like add up Threes in order to, like behind it, it should be hiding, like doing layout on a board. And it's like playing Tetris should be actually doing layout on a board, but the interface I see is Tetris, but it's going to do something more useful with my time than playing stupid games.

**Chris Gammell:** You know, doing layout on a board is like playing Tetris. You can just go do layout on a board. Maybe you just need to find the right CAD program. That's all I'm saying.

**Alicia White:** Yeah, I hear CAD is what I should try.

**Chris Gammell:** It's the new hotness.

**Alicia White:** There's even a class about it.

**Chris Gammell:** Yeah, wow. There's even an interview on an embedded podcast. Someone talking all about a class about KaiCAD.

**Alicia White:** Yeah. And he won't shut up. I think so. I think there is. Yeah. We'll have to look for that. That's gracious. Dave's jealous he didn't come on my podcast.

**Chris Gammell:** Oh, I'm sure he would if you asked nice enough. He's so busy. He's busy.

**Dave Jones:** Do we have any listener questions? I lost them. We're so professional here on the Amp Hour.

**Chris Gammell:** Yeah. I have more questions myself. So, I'm going to ask questions anyways. So, what about writing a book? I mean, is that hard? Because this is a...

**Alicia White:** No, no. It's easy. You spend like an hour a day. You drink your coffee. You write your book. It's totally easy. Have fun. It takes, you know, it takes like a month.

**Chris Gammell:** You know, Greg Shervat's been trying to convince me to write a book for like a year and a half now. And this is what I'm saying. It's like, he's like, oh, it's, you know, it's simple. And I'm like, no. No. And so, okay. So, it's not easy. Well, like, what about doing a book like this? Because this is a little bit less... I mean, this is very technical actually still. But it's still like a higher level. It's wrapped nicely in like good writing and everything else like that. It's not just equations or just code snippets. So, does that make it different or... Yes. How did that all work?

**Alicia White:** Well, and the artist that worked on my book took chicken scratchy little things and really nice drawings. So, that was important.

**Chris Gammell:** Ah, yeah.

**Alicia White:** Okay. So, I spent probably three to five hours a day for six, seven months writing a book.

**Chris Gammell:** Oh, holy crap. Wow.

**Alicia White:** And I had a job at the time, a contract job. And they were very understanding and that was cool. And O'Reilly wants you to work with them. They don't want you to come with a fully formed book. They want to help you through the process. So, that...

**Dave Jones:** I think almost all of them do that. Yeah.

**Alicia White:** I think Pragmatic Press wants you to be a little further along. They want to see that you're going to write the book. The way that I did it with trying to insert as many jokes as I could and trying to keep it engaging to read. I mean, there are a lot of books out there that you read the section you need and then you put it down. But my goal was to write something that you take to the beach to feel like you're not entirely slack enough from working, but then actually get engaged. So, I did... There's a fair amount of humor. So, I think that's harder. And I minored in theories of learning, so cognitive psychology stuff. So, I really care about how people think, and I try to do a bit of that. And O'Reilly does the headfirst books. And I think I kind of straddled their ranges. It's not as technical as some of the other ones in the animal line, but it's not quite as fluffy as the headfirst really thick ones that you get a lot of puzzles in.

**Chris Gammell:** Wait, what's headfirst mean?

**Alicia White:** Oh, headfirst is O'Reilly's other line of books. And they tend to be 400 pages. I mean, big, thick books. But each page has a graphical element and like a puzzle element, as well as the technical information they're feeding you. And the goal is to make it easier to pick it up and to learn it and to internalize it. Instead of the technical books, where you really have to make yourself read it. Headfirsts are a lot more fun to read, but they're huge. So, just trade off.

**Chris Gammell:** Well, that's good to know. And I mean, like I said, I haven't gotten through all of it yet, but I mean, I really do. I do like it. It's, you know, for someone like me who complains about code a lot, it makes it a lot more accessible.

**Dave Jones:** So, I like it. And is it the same with most authors that really, if you're doing it for the money, you're doing it for the wrong reason?

**Alicia White:** Oh, yeah. I mean. Totally. At contracting rates, there's. No. Yeah. You lost money. Yeah. I definitely lost money. And they still send me a check every month. But you don't do it for the money. If you, the credibility is very high. The opportunities to do other things. I did, I talked to James Grinney and you mentioned him. He wrote Test Driven Development for Embedded Systems or Embedded C. Yep. And he's a great guy. Embedded C, yep. And he wrote his book and he does a little bit of consulting, but 90% of his, his, uh, income is due to teaching. And so the book is valuable for that. And it's great to get him teaching gigs and it's great to leave with people. And when this book came out, when my book came out, I, I started to look at teaching and realized that I like teaching. I like talking to people, but I like talking to processors more.

**Dave Jones:** Yeah. And he's human.

**Alicia White:** Don't want to deal with it.

**Dave Jones:** Don't want to deal with it.

**Alicia White:** They listen at least. Human race just needs convenience. It does exactly what I tell it to do.

**Chris Gammell:** And when not, you can just, you know, have it overwrite itself 10,000 times in a row.

**Dave Jones:** And we probably can't pass up the opportunity, unless you had more to talk about the book.

**Alicia White:** I just want to encourage Chris that it is very worthwhile, but it is a lot of work. Yeah. And if you're thinking about it and you're thinking about it in like a two years sort of way, consider doing NaNoWriMo. It's November's national novel writing month. And you write 50,000 words in a month. And if you can do that, you can write any book you want. And if you only get to 5,000 words, then really you may not be able to push yourself. They don't have to be good words. They just have to be words.

**Chris Gammell:** Just words. Can they all be participles?

**Alicia White:** But you do a lot of writing already. You do blogs and contextual electronics is going to end up having a ton of material that will be able to translate into a book. So you're not starting from zero. To all of my laughter aside, seriously consider it. And I'll try not to giggle. File.

**Chris Gammell:** File. You are speaking at EE Live. Is that right? The former Embedded Systems Conference and Design West now EE Live.

**Alicia White:** Yes. Because, you know, they have to change the name again. I am speaking at EE Live. Well, yeah.

**Chris Gammell:** You know, they got to throw out all those hats and t-shirts and stuff. They want to throw them out each year.

**Alicia White:** I'll be speaking Wednesday at noon with Jen Castillo. We are going to tear apart her BS sports watch and look at the inside. And her slides are incredibly up front with what they're doing inside their product. So I'm excited about the teardown. And anybody can do it. It's on the expo floor. So you get the free expo pass. You can come see me and Jen.

**Chris Gammell:** Oh, yeah. Yeah.

**Alicia White:** And then my session behind the paywall is what marketing won't tell you about the Internet of Things. Sure. In which I rant about how the Internet of Things is not what everybody promised us. And we need to do a better job at making it accessible to consumers. No kidding.

**Speaker ?:** Yeah.

**Chris Gammell:** Yep. So they don't want to configure everything themselves? They don't want to pound define their thermostats? No? Yeah. No.

**Alicia White:** The configuration is the huge, hideous part. And security and ease of use are natural enemies. And just all the stuff that when you're thinking about, should my fishbowl be connected to the Internet? Sure. Absolutely. All fish should get to surf the Internet. But there are some things you need to think about when you are looking at making it low cost and how that's going to affect your fish and his ability to get to YouTube.

**Dave Jones:** Come on. Google can't be wrong. They paid $4 billion for Nest for a reason. Yeah, right? I have a Nest.

**Alicia White:** I have Nest Protects, the smoke alarm. I was so excited about having a smoke alarm that didn't suck. And I have to say the setup sucked. And then...

**Dave Jones:** What is wrong with the smoke alarm? How does a smoke alarm suck? It sits there. It never does anything. It never intrudes in your life. How does it possibly suck? Well, the configuration sucked. Because there's a low battery warning once every... No. How? You stick it up on the roof. You put a battery in it.

**Alicia White:** We had a false positive. And because it is Internet-based, it texted us. And we were 20 minutes away. And it was...

**Chris Gammell:** And you burned the house down or something? You're like, oh, better just...

**Alicia White:** No, it just annoyed the crap out of all our neighbors and gave us a heart attack because, you know, getting home because you think your house is on fire.

**Dave Jones:** A false positive from what? You can mitigate these things.

**Alicia White:** Well, okay. It's not rocket science. You burned the toast, okay? Maybe there was some blame there.

**Dave Jones:** Smoke alarm goes off.

**Alicia White:** They say don't put it in the garage. We have an electric car. So we put it in the garage because we don't have carbon monoxide. So it should be fine. And there may be more than one reason not to put it in the garage. So maybe it was our bad. But still...

**Chris Gammell:** So it was user error.

**Dave Jones:** I've got a smoke alarm in the garage. It's never given me a lick of trouble in 10 years.

**Alicia White:** Are the batteries dead?

**Dave Jones:** What's the problem?

**SPEAKER_01:** I replace it.

**Dave Jones:** No, they don't run dead because I replace them every year.

**Alicia White:** I don't know. I... Since I have an electric car, I actually want a smoke alarm in the garage just in case. Then put one in there. But don't put a nest protect.

**Chris Gammell:** You don't need this newfangled nest rubbish. Don't hook it up to the internet. That's what Dave's saying.

**Dave Jones:** That's what I'm saying. Buy a $10 smoke alarm for your local thing and put it in your garage.

**Chris Gammell:** So is it... But I did it. Is it you actually actively dislike it then? Or is it just that you don't feel like you got what you paid for?

**Alicia White:** Well, I called them and explained the whole situation with the electric car and the garage and asked for help. And the guy read what he was instructed to say over and over again. And I said, can I speak to a manager? And he reread the script. Oh, man. So I went from kind of being annoyed but realizing it's my own damn fault to actively not liking them. In part because of their internet setup was stupid. Actually worse than their Nest thermostats version, which was lame.

**Dave Jones:** And Google paid how much? 3.2 billion dollars.

**Alicia White:** Google, if you'd like to buy logical elegance, it's a reasonable price. A hundred million dollars gets you a lot of experience with embedded systems.

**SPEAKER_01:** Exactly.

**Chris Gammell:** You get a lot.

**Dave Jones:** And that's just lunch money for them. I don't know.

**Alicia White:** A whole stock full of dev kits, tools.

**SPEAKER_01:** Yeah. Yeah.

**Dave Jones:** Heck, you'll even throw in the podcast at that price. Yeah. Right. So that begs the question, how much would you sell out for? I think she just said a hundred million.

**Chris Gammell:** A hundred billion.

**Alicia White:** I think I'm going to stick with a hundred million until, you know, I know the rest of the parameters. Right.

**Chris Gammell:** So we have taken more than enough of your time.

**Alicia White:** I thought these were four hours long.

**Chris Gammell:** Oh. You want to go four hours? No. No. No. No. Okay.

**Alicia White:** I was just about to say I'm getting hungry. I should go have some dinner.

**Chris Gammell:** But people, see the difference here is that people can hear you every week, which is, you know, so they can just go over there. And they should go over there, embedded.fm, my new favorite podcast. And they can hear that lovely voice. I don't miss it. Thank you.

**Dave Jones:** I'm so jealous. I hate anyone who's got a good voice because mine sucks. And somehow I do a radio show. You know, you've got that lovely, mellow voice. And people like to listen to you. So I don't. Yeah. No, I think they put up with me.

**Speaker ?:** I think they.

**Chris Gammell:** Yeah, we do. I mean, for some reason.

**Dave Jones:** They tolerate my voice, you know.

**Chris Gammell:** I really like your, so like your interaction with guests is good, but I actually like when you and Christopher are on together, I like, like you guys just have a really good rapport together too. Like, you know, you're kind of like. Thank you. Yeah. I just think it's, you know, it's like. That's why they're married, dude. Exactly. That's what, that's exactly it. You know, like. So.

**Alicia White:** We are coming up on 20 years together. So there's, we should. Oh, geez. You get less for murder. At this point.

**Dave Jones:** As I always tell my wife. Yeah.

**Chris Gammell:** Yeah. I get in trouble every time. If you waited this long, you guys are doing something right. So that's good. Yeah.

**Alicia White:** But, but we are incredibly fortunate to have not similar careers entirely, but enough that we can definitely talk about what we're doing and how it works. And yeah. That's nice. I like to talk to him.

**SPEAKER_01:** That's good.

**Alicia White:** Sometimes I even like to talk to him with microphones on.

**Dave Jones:** Some people think that's a bad thing to have a partner who likes and does the same sort of stuff you do and works in the same industry and all that sort of, you know, jazz. There's for and against. Some people, you know, think I think you do it. I think you do it. I think you do it. Other people say, no way. Don't do it. You know, marry someone completely different with completely different hobbies.

**Alicia White:** I know that he's going to listen to some of this podcast, but I don't know he'll make it all the way.

**Dave Jones:** All right. We're safe.

**Alicia White:** We have the shared consulting company and we have an office. We actually have a really nice office in our home and our backs face each other. So we don't see each other all day, which I think is important. But I have been with the robotics company. I've been going to client site because the robot's there and I didn't really want to burn down my own house.

**Chris Gammell:** Yeah. Your nest won't help you.

**Speaker ?:** Exactly.

**Chris Gammell:** It's in the garage.

**SPEAKER_01:** Why would you beep? Dammit, just beep. Don't talk to the internet. We don't care.

**Alicia White:** It has been so nice being out of the house and not being with him 24 hours a day.

**SPEAKER_01:** Oh, yeah. Yeah.

**Alicia White:** You do need a little space. Oh, yeah. Right. But yes, now that I'm getting out a little more, it's great. You might make it to 21 years, I know.

**Chris Gammell:** Maybe.

**SPEAKER_01:** We'll see.

**Alicia White:** Oh, goodness. Okay. So I want to say my podcast thing. Do you know that? Oh, yeah. Please do. Welcome to Making Embedded Systems, the show for people who love gadgets. Yes. Okay. That was all.

**Dave Jones:** Thanks. That voice gets me over time. Why did you want to say that?

**Alicia White:** Well, because we didn't, you said embedded.fm, which is where to find the RSS and all of that.

**Alicia White:** Sorry. The show name is Making Embedded Systems, so I just wanted to get that out there. And the tagline, you know, I worked hard on that tagline. It took me all of that 10 minutes.

**Chris Gammell:** Did you buy makingembededsystems.com? That might just make it easier on people. Yeah. You know?

**Alicia White:** Yes. Yes. And it used to be contact this show through show at makingembededsystems.com. But people were telling me they were getting bounces, and so no, it's just show at embedded.fm because it's easy.

**Dave Jones:** It's three words. Goodness. That breaks every rule of domain names, doesn't it? We're three words. Yeah, but we're short words. That's true. The air power. Yeah, we are. Okay. Well, fail. Okay. I'll retract my comment. Yeah, but we're short words. We are short words. Now I have to justify our three-word domain name. That's right. Yeah. Yep. Changing the show name. Wonder off of my tail between my legs.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** What about if people... We will post a link to the book as well, because I highly recommend people buy the book. What if people want to hire you as a consultant?

**Alicia White:** Info at Logical Elegance is our general. Okay. And if you go to Logical Elegance, it is LogicalElegance.com.

**SPEAKER_01:** Okay.

**Alicia White:** If you want to write the book, coupon code is authD, A-U-T-H-D, Alpha Uniform Tango Hotel Delta. Okay. I'm writing it down. Yeah. You've got to give everybody time to write it down.

**Chris Gammell:** Right.

**Alicia White:** That's only useful on O'Reilly.com. Okay.

**Chris Gammell:** That's good. O'Reilly.com. Well, thanks for being on the show.

**Alicia White:** Thanks for having me. It's been fun. We'll have you back.

**Chris Gammell:** For sure.

**Alicia White:** I am so glad you guys exist, too. That's good. I wish I had known more about... I wish I had known about the Ant Hour when you started.

**Dave Jones:** Well, no. Because then you said you wouldn't have started. I kind of sucked when you started. It was, you know... Yeah, we did. It's slightly less sucky now.

**Alicia White:** But it's so useful. You always wonder what the other guy's doing at their desk. And it's nice to hear what the electrical engineers are doing. So, thank you.

**Chris Gammell:** Technological voyeurism. That's my new term. So, I totally agree. That's what contextual electronics is based on.

**SPEAKER_01:** All right. Yeah.

**Chris Gammell:** So, people should go listen to Making Embedded Systems, the podcast. Not embedded.fm, but located at embedded.fm.

**Alicia White:** That is confusing. Thank you for having me. That's all right. It was an honor and privilege. And thank you.

**Chris Gammell:** Uh... Thanks for being on the show.

**Chris Gammell:** Bye.

**Alicia White:** How do we say goodbye?

**Chris Gammell:** We'll probably just keep dragging it out. I'll just put a chop in here somewhere. And then, you know, this will go in the post.

**Dave Jones:** Damn it, I'm hanging up now.
