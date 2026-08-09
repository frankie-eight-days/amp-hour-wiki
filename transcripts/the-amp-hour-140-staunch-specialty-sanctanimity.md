---
episode: 140
title: Project Management, Lasers & Robots - Staunch Specialty Sanctanimity
url: https://theamphour.com/the-amp-hour-140-staunch-specialty-sanctanimity/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by ViaDesigner.com, part of Triad Semiconductor. Who needs a chip printer when you can design your own mixed signal chips on your desktop? ViaDesigner is a Windows-based software for the design and simulation of analog and digital circuits. At ViaDesigner.com, you can learn about mixed signal design, share your design IP, and form teams to create your own custom via ASICs. Go to ViaDesigner.com slash the Amp Hour and enter coupon code AMP100 at registration for a free year of ViaDesigner, a $500 value. This is the Amp Hour Podcast, recorded April 8th, 2013. Episode 140, Staunch, Specialty, Sanctonimity.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** And yes, we are brought to you by Triad Semiconductor. Well, we'll get to that. Come on, man. Yeah, we'll talk about that in the middle of the show. I don't have a radio voice. Sorry, I can't do that, you know.

**Chris Gammell:** Oh, no. Well, neither do I. Right. It was in the feedback of get a professional voice actor to do our advertising for us.

**Dave Jones:** Right, to do our intros, right. Well, the reason you do the intros is because you're less nasal than I am.

**Chris Gammell:** Right, and I'm very low cost compared to a voice actor. Right.

**Dave Jones:** Yes, we're a budget operation here on the Amp Hour, folks.

**Chris Gammell:** Maybe when Intel starts advertising with us, we'll get a voice actor. But until then, I think we're good enough. The info is all that matters.

**Dave Jones:** Intel, are they still in business, are they? Didn't R take over the world?

**Chris Gammell:** I saw their CEO, their soon-to-be former CEO, Paul Ottolini, is making $19 million this year.

**Dave Jones:** Is that all? That's not much. He should be milking the system more than that. This guy needs to buy a clue.

**Chris Gammell:** Maybe. I don't know, man. I was discussing the executive compensation and just the general high-level C-suite kind of C-suite when you're a CEO or CTO. It's got to be so crazy to get up there. I mean, obviously, you and I and probably most of our listening audience...

**Dave Jones:** We're never going to know.

**Chris Gammell:** We'll never know, you know? So, my buddy, the buyer, right? The one I've talked about before. Right. He was lamenting at one of the CEOs he's worked under before who was an engineer. And I'm like, because they were so cost-sensitive or something like that. And it's just like, it doesn't matter what your past is. There's such like a magic formula to get like... You know, first off, you're set up for failure. And second off, you know, like in a technology company, it's just so hard to get the balance of like making money and spending money and everything else. I don't know. But C-suite's just never... I don't... I love the money, but I don't think I'd ever love the lifestyle. You're just... Right. You've got to give it all, right? I mean, like you and I have talked about work-life balance before, but...

**Dave Jones:** Yeah, but if you fail, you just take your golden parachute and go to the next one.

**Chris Gammell:** That is true.

**Dave Jones:** It's a great, you know, it's a great deal.

**Chris Gammell:** You can't find that part. It's not bad, but money isn't everything, man. I mean, like, I don't know. Would you rather be... I think I can probably answer this, but would you rather be, you know, in meetings and, you know, shareholder meetings all day making tons of money, or would you rather be working on technology and, you know, hanging out with... Yeah, exactly.

**Dave Jones:** I totally agree.

**Chris Gammell:** Yeah.

**Dave Jones:** So that's... Yeah, no, it's not a job I'd enjoy, I'm sure.

**Chris Gammell:** Exactly. I mean, like the life balance thing, man. That's a big deal for me.

**Dave Jones:** Life balance? Yeah. Same here. And you'd think I have it, you know, doing this gig full-time, but no, I'm working harder than I ever have. Yeah, but you still enjoy it, right? Before I walked out the door this morning, I complained to the wife. I'm always on the... I'm always behind the eight ball. Always behind the eight ball in terms of stuff I've got to get done. I'll never get ahead, ever. It's like, you know, it's that continuous constant pressure to produce, you know?

**Chris Gammell:** Dave does not hire anyone. He will not... He is very... Very much like an engineer, will not relinquish control. I can just do it better myself. I can do it faster myself. Me and Dave have had long conversations.

**Dave Jones:** And I keep saying it comes down to the practicalities. What are the... I'm going to get them to do. What am I going to hire them for?

**Chris Gammell:** Yeah. You know, there's always inefficiencies for that. I mean, like even in layout, right? Like I don't get to do my own layout at work. Right. First off, I have to hand it off. I think if I could, I probably would do it myself. But there are benefits of doing that kind of thing, right? Oh, sure. There's overhead. I have to send emails. I have to correct, you know, stuff that wasn't done the way I'd like it to be done or is just wrong based on my direction or their assumptions, whatever. But I don't know, man. There's at some point...

**Dave Jones:** Well, everything I do is so personal. I agree with that. It's so personal. And that's the, you know, that's the hole I've dug myself into, I guess.

**Chris Gammell:** I guess so. But I think, I still think, you know, like any job in electronics, you know, like at some point you have to really... I read about startups a lot too, right? And that's always a stumbling point for startups. At some point you have to give up some kind of control because you have to sleep or you'll die. Like you'll literally die. I know.

**Dave Jones:** See, if I was doing a startup or running a business, I'd do exactly the same thing. But this is essentially my hobby, which I've turned into a business. It's just something I enjoy doing. Right? I guess so. Yeah, I could, yeah, sure. I could design out the farm of, you know, 10 kits or whatever to somebody else to do all the design and implementation. And then I just slap my name on it and be done with it. But I, you know, that's not the business I'm in. That's true. That's true.

**Chris Gammell:** It's a tough decision to make, you know, like trying to make that jump. I'm sure, you know, a lot of people that have success have to make that decision at some point. Even, I was thinking about, you know, like you and me and how, you know, I know that you've been focused on video and everything else like that. It's just like what you concentrate on, right? I was, because I was thinking the other day, I would be really good at the amp hour and making, you know, making more YouTube videos. Obviously, I don't. But if I just had my head down, I was making circuits all day long. And it's kind of a paradox because if you're doing just that, then you don't have time for the video and the actual publishing part of it, right? There's always like that balance point of, you know, I want to do stuff, but I also have to show it. That's tough.

**Dave Jones:** That happens to me, right? I'm too busy producing the videos because that's what people want me to do that I don't have any time left over to, and they, you know, to finish the kits and designs and, you know, work on, you know, yeah, I'd love to spend two weeks or a month working on some project. And then, but at the same time, I can't film the videos to show how I do it because, you know, they're two full-time jobs, so to speak.

**Chris Gammell:** Well, the same thing goes with like, you know, management versus engineering, right? It's like as an engineer, I feel that draw towards like, oh, man, I just want to make some decisions. I just want to make stuff happen. I want to, you know, get stuff built. I want to change the world. I want to, you know, make more stuff, right? And at the same time, though, I know that if I do that, then I'm in meetings with vendors. I'm in meetings with manufacturing. I'm in meetings with everything else, right? And I'm not actually designing them. Yeah, exactly. You know, my name might still go on the top of the, you know, the patent or whatever, but I don't have that satisfaction of, man, I designed, I was in it, right? I was in the thick of it. I figured that shit out, you know? And it's a tough balance. You know, I've talked to a lot of people about that too because like one of my mentors, right, one of my former technical mentors, he was kind of transitioning into the management side of things. And he talked about that. Apparently, as he got older, he wanted just to have more of the hands in control and actually making that change happen. And I could see it because, you know, at a certain point, you get sick of seeing idiots not do it, right? And you're like, I could do this better myself, right? That's just the engineering way. I want to do it. But you have to give up stuff in order to do so.

**Dave Jones:** That sucks. And that's, interestingly, what part of my Ignite talk is about. Really? Oh, that's coming up, huh? Well, that's what it kind of starts out as. Like, you know, right in the first couple of sentences, I talk about how, you know, I used to have a real engineering job, you know, working for the man. And I'd be working on something for six months and then it'd just get shit canned. It'd never make it to market. So I've just wasted, you know, six months of my life working on that. If your goal is to, if your satisfaction, ultimate satisfaction is seeing something produced and being given to the world and used, right? So, and I don't, I didn't, I never had, I rarely had that satisfaction because most of the projects, as I've talked about before, have been canned or, you know, didn't actually make it out the door. But whereas now I'm getting that satisfaction, you know, weekly of actually producing material that makes it out there and makes people happy, you know? Yeah. So, so I've got my dream, you know, but it comes at a price.

**Chris Gammell:** But just over that fence over there, that grass, it looks, oh, it's such a nice shade of green. Oh, I can smell it too. Yeah. Freshly cut. Freshly cut. Yeah.

**Dave Jones:** So be careful what you wish for, because now, as another thing I talk about in the, in the talk, or will, hopefully, is that, yeah, is that constant pressure? That's one of the downsides. It's relentless. You know, I've just got to keep producing that content. Otherwise, otherwise the dream ends. So, you know, it's like, whew, how do you win? It's tough, man. I don't know.

**Chris Gammell:** It's tough. Yep. And we don't want to sound like ungrateful or whiny.

**Dave Jones:** No, not at all. But we're just talking about the practicalities of what happens when you-

**Chris Gammell:** Right, exactly.

**Dave Jones:** You know, it's just what happens in the real world.

**Chris Gammell:** It's interesting hearing about, you know, I always see the surveys of people as they get older and what age they're at. You know, like, what is the- You know, they ask someone who's 20, 30, 40, 50, 60, whatever. You know, what is the best age of your life? And they always say, right now, right? Now. And it's funny because in technology, or at least in, you know, at least from my experience in talking to other people, it's always, eh, some other time. You know, it's like, it'd be nice to have that same, you know, mindfulness of, it's not bad right now. You know, it's cool. I'm designing circuits. I'm working on cool things. You know, it's not always going to be rosy. Obviously, last week I talked about how crappy manufacturing can be.

**Dave Jones:** And I was just thinking about how wonderful it was back in the, well, seemingly wonderful it was. You know, 20 years ago, there was no internet. There was none of this distraction. And I would spend six months just working on a design and do it all on paper and everything else. You know, there wasn't all this CAD and looking up stuff and, you know, thumb through your data book collection and you thumb through catalogs. And you'd just spend your whole life just working on this. And it was fantastic. Yeah. But now, you know, I mean, there's so many distractions. In life. It's true. That you can't focus on. It's hard.

**Chris Gammell:** Right. But on the flip side of that, the access you have, right? Just the. Oh, now the access. Yeah. Right. Distributors and everything else.

**Dave Jones:** You wouldn't trade it. I've said that before. I wouldn't trade the communications revolution in the internet for anything.

**Chris Gammell:** Right. I was actually. So I was by the bookshelf where all the data books were at my office today. I wasn't looking at the data books specifically, but I was, you know, I kind of peered over them.

**Dave Jones:** And you were just going to saw. Look at that. No, they look terrible. They were.

**Chris Gammell:** I was flipping through a price book, actually. And it was terrible. Who would want to do that? And then I actually. No, what was the one I picked up? It was like a wiring guide. It was a guide to wiring. Right. Yeah. And that information is still all out there. Right. It's all on the internet. It's, you know, like. But I don't have to see all the extraneous stuff. I mean, I don't have to see like the, you know, if I'm looking at how to wire up a, you know, 20 gauge wire, I don't have to see 12, 16, 18, 20, 22, 20. You know, like it's, I don't know. It just, it was really overwhelming. I opened this book up and I'm just like, oh, why? What am I looking? I don't know. It was, it was really overwhelming. I don't know.

**Dave Jones:** I grew up. We didn't know any different back then. That's true. Yeah. That's true. We didn't know any different. But I mean, I grew up. That's why I guess we seemingly look at, you know, back on these things with fond memories, you know. I don't though.

**Chris Gammell:** That's the thing. Like I look back on. So what it immediately recalled was the days of, I guess it was like elementary and middle school of doing the research projects, right? And like citing stuff in a book, you know. And now it's just like, I don't know, hyperlinks are like my second language these days. I know that not everyone's like that. I mean, like if you blog, it might be a little bit more your language, but ah, just bibliographies. No, thank you. We're just getting old because we've been doing this show for two and a half years. We have been doing this two and a half years. Yeah. That was another thing that hit me today. Who's the bastard that pointed that out to us? Or was it you? It was me. I'm the bastard. It was, I was, so I've been looking, you know, so I've been working on these t-shirts, right? And the slogan and everything. And I have a whole list of slogans too that I don't know if you saw I tweeted. But.

**Dave Jones:** No, I haven't watched, haven't looked at tweets in the last day. No, that's okay.

**Chris Gammell:** I have to catch up on that. So I was going back through just trying to find. Oh yeah, that's okay. I was just trying to find, you know, just like past data. And, you know, like, because I know, I know for a fact that you and I have said on multiple occasions that would make a great t-shirt, right? Oh yeah, for sure.

**Dave Jones:** Yeah, a dozen times, I'm sure.

**Chris Gammell:** Yeah, at least. And I've been trying to find that stuff and apparently I just never wrote it down. And so none of that stuff is recorded.

**Dave Jones:** Welcome to my world.

**Chris Gammell:** Yeah. So, oh God, that's the worst too, isn't it? Like when you know something happened, you just can't find it. Like searching through like old emails and stuff.

**Dave Jones:** Oh, well, this is what happens with my, I've been trying to write this bloody five minute Ignite talk, right? Yeah. I've been spending days on this, writing this bloody script. Because I don't normally write scripts, right? Right, right. Off the cuff. And I always, you know, and I'm out somewhere and I always think, you know, I'm always thinking about it. So I think of, you know, something great to say. And then I go, oh, I've got to remember that and put it down. And then of course you never do. And then you get there and write, I have to write this script. I can't remember a bloody thing.

**Chris Gammell:** You know? Oh, that's the word. Yeah, that like writer's block, but you know somewhere in your brain that it has been thought of before. There is no worse feelings. Exactly. And it was brilliant.

**Dave Jones:** It was perfect, you know?

**Chris Gammell:** That happened to me the other day with a schematic, actually. So I've been dealing with this problem and I was on a plane and I was reading the data sheet and I didn't have a pen. And no one around me had a pen. And I had this idea for a circuit. This is totally serious. I had this idea for this circuit diagram, right? And so I was like drawing it out with my finger, like on the page with just my finger and like trying to remember, you know, just trying to commit it to memory. And I'm like, God, this is terrible. Like honestly. And then I got off the plane, obviously I forget all about it. And then I got back on the plane to go home. And I'm like, I had remembered to buy a pen because I had to buy one because whatever reason. And I bought one and I was working on the circuit and I'm like, I finally get to it. And I'm like, no, there's nothing there. It's all gone.

**Dave Jones:** This isn't as good as the one I thought of yesterday. Exactly. Yeah. That is a terrible feeling. It's inventive enough. What you need to do is find a sharp object somewhere and cut your finger open and then write in blood. Or just carve it right into my hand. There's always that ink medium, you know, inside you. Yeah. Oh, man. No. I know what it's like. Yeah. Have you ever tried to write a script for something?

**Chris Gammell:** Like a... Yes. Like a talk? My Maker Faire talk last year. It was terrible. Oh, okay. Yeah. It was... There's video of it being terrible.

**Dave Jones:** What, your talk was terrible or the process of writing the script was terrible?

**Chris Gammell:** A little bit of both, yeah. A little bit of both.

**Dave Jones:** Right.

**Chris Gammell:** Not the best public speaker in the first place. Right. Well, me neither, you know. Yeah. You know, in the internet, it's not bad.

**Dave Jones:** No, I'm so used to winging it. Well, I told you about that, you know, when I was at the... A couple of years back when I did the show from the hotel room in... Oh, yeah. Anaheim. That's it. I remember. With Renesis. Yeah. And, yeah, and I tried to write, you know, I had to get up in front of a thousand people and talk about, you know, this contest. And I tried to write everything down and I went, this just isn't working. I spent hours in my hotel trying to write it and I go, screw this, I'm just going to wing it. And I winged it and it was all right, you know. Unfortunately, I can't do that.

**Chris Gammell:** You are what you practice, right? I mean, you are very practiced at winging it.

**Dave Jones:** And, yeah, exactly. Exactly. So, I can, you know, I can probably get up there and waffle on. Yeah, it's not going to be perfect, but at least I'll get through it.

**Chris Gammell:** Yeah. Well, and I think just in general for engineers, I mean, we're not necessarily the best public speakers in the first place. I know that. No, exactly. I don't know. I get that. I get very, I don't know if it's anxious. I get jumpy. That's the thing. Like, I just start talking really, really fast.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** And it always feels weird trying to, like, slow yourself down. Yep. And in figure one. One. There was resistance.

**Dave Jones:** And everyone's sleeping in the audience, so it doesn't matter. Yeah, exactly. So, they're not looking at you anyway, yeah.

**Chris Gammell:** Yeah, bonus.

**Dave Jones:** And that's why I foolishly signed up to this Ignite Talk thing. Yeah. To put, you know, A, it'd be fun, and B, it'd put pressure on me to actually, you know, put a lot of work into it and see if I can actually do something like this. And once again, it's that relentless.

**Chris Gammell:** All those deadlines are a tricky mistress, I have to say. You know, like I've told you before, you need to hire someone to be your boss almost. Right. The jury's still out if I need that kind of thing. I think, I personally do best when I schedule myself for something completely unrelated. Like, if I scheduled myself to, you know, design a circuit board for myself, I would get really good at guitar that day. If I designed, if I scheduled myself to take a guitar lesson, I would have a perfect circuit board. You know, that's mostly how my brain works.

**Speaker ?:** Right.

**Dave Jones:** And we talked about that before, deadline. You know, if you set yourself a deadline, you know, and that's, engineers are great at working to deadlines. Works every time.

**Chris Gammell:** Yeah. Yeah. But, like I said, I'm not always sure about the, for me, the self-imposed deadline is just.

**Dave Jones:** Oh, but, well, the self-imposed, yeah. No, you've got to publicly commit to it or have, or as you said, have someone hire, you know, you have to hire someone to whip your ass. And then, once you've got that, you know, then, yeah. Right. So, like, it's the same thing with this radio show, right? We would never do it unless we had the pressure of, like, 6,000 or 7,000 people demanding this thing every week. And they expect it on a Tuesday, right? So, like, we just go, oh, no, couldn't be bothered. Oh, no, let's just leave it for, no, couldn't be bothered. Right? And it happened. That does help.

**Chris Gammell:** Guaranteed. For fledgling podcasters, that does help a lot. Weekly deadlines.

**Dave Jones:** Yes. You say, we do it on Tuesdays and that's it, you know, and boom.

**Chris Gammell:** Of course, now that I've said that, I'll curse myself into being like, ah, Dave, next week I can't make it. Yeah, can't make it.

**Dave Jones:** Well, we've done it a couple of times, you know. Over Christmas, we just went, eh, what the hell. We're taking a week off, you know. Screw it.

**Chris Gammell:** Yeah. I mean, well, so I've been like that. So, I've been, you know, I get programming books out. I try and do that with, like, programming and stuff, and it never works with that. It just, I don't know why. I don't know what it is about programming. I think what the thing is, though, too, like, so, like, teaching myself KiCad, that was another one where it was like. Right. Yeah, yeah. I just, you know, I wanted to do it.

**Dave Jones:** But you didn't have the discipline to sit down and do it.

**Chris Gammell:** Exactly. It wasn't until I had a project that I really, really needed to get done, and I said, you're not buying a license of anything else, because, you know, I couldn't afford, like, an all-time license. I didn't want to buy an Eagle license, and the board was too big to be a freemium license for Eagle or anything else, which I had experience with, and I was like, all right, this is the time. This is when I'm going to do it.

**Dave Jones:** Yep.

**Chris Gammell:** And that one project, man, after that first one, that helps a lot. Exactly. In any CAD program you do. So, but with programming, I haven't been, I still haven't been able to crack that nut. I mean, like, some, you know, I've done some C, I've dabbled a lot of C, but, you know, like, all those, like, massive online open courseware things. Oh, yeah. Nope.

**Dave Jones:** I've signed up for a couple of those, and I just, I last one lesson, you know. Exactly. I don't even make it through the first lesson, you know. Exactly. No.

**Chris Gammell:** Right. Well, there was this, so there's this site on Pando Daily, which was a tech site I like a lot. They had the top 10 websites that teach coding, right? And it's great. I mean, like, this kind of stuff is awesome. You know, they've mentioned Code Academy.

**Dave Jones:** If you've got the discipline to do it. Yeah, it's fantastic.

**Chris Gammell:** Yeah, exactly. You know, Google, Coursera, all the ones that people might have heard of, you know, they're really good for, it's good information. But nothing, for me, replaces A, having classmates who depend on me, or B, having an actual project to work on, you know, like, or something that depends on it. It doesn't hurt to pay thousands of dollars a year to be like, well, you're wasting this, buddy.

**Dave Jones:** You're better off paying thousands of bucks developing a project.

**Chris Gammell:** Right. Right, exactly. Exactly.

**Dave Jones:** And then you, yeah, then you've got some real application of it.

**Chris Gammell:** Yeah. Yeah. Skin of the game is a very, I mean, that's the tough thing with, like, startups, too, right? I mean, like, a lot of people I know who are doing or have done startups, it's, until you make that leap away from your job, it's not really a thing yet. You know, there's no. It's not real, yeah. Yeah, you don't have any skin in the game yet. But once you do, then it's like, all right, it's go time. Let's do this, you know. And it might not be the best time to learn coding. It's not like, all right, I quit my job. What am I doing?

**Dave Jones:** Writing an app sounds good. Yeah. How do I know? Do I know how to program? No, it doesn't matter.

**Chris Gammell:** Yeah. I can figure anything out. And it's like, you know, I feel like with enough time and mentors and everything else that, you know, a lot of things are learnable. But it's kind of balancing that.

**Dave Jones:** Everything's learnable if you've given enough time, but yeah.

**Chris Gammell:** I don't know if I can learn how to dunk on a basketball hoop, but.

**Dave Jones:** That requires some physical ability, which weedy nerds generally don't possess. Right, yeah. Yeah.

**Chris Gammell:** I mean, there's sometimes restrictions like that, right? I mean, like, if you're afraid of really hot things, you might not be great at soldering. Or if you have trouble, like, with, I guess, abstract math, right? Maybe programming would be a problem for you, right? If you're more of a, I guess, what was the, I guess linear algebra is the one that really helps with programming. That's what my programming friend tells me. Yep. Yep.

**Dave Jones:** And as I've said, as I've always said, it doesn't matter how you could practice chess every 20 hours a day for the rest of your life. You're still not going to beat Garry Kasparov at chess, right? Because his brain is just wired that way. And yours isn't. Tough shit. Yeah. You know, I mean, yeah. Some things just require, you know, your brain to be wired a certain way. And you can't rewire it.

**Chris Gammell:** That's, yeah, that's partially true. I think the other thing, too, is like, so like, we've talked before about the 10,000 hour rule, right? Like how if you get to 10,000 hours, you're probably an expert. That's always like what is talked about. And there's a bunch of research on that kind of thing. And then it was talked about by Malcolm Gladwell in, what was it called? Outliers. But the key with that, and I think it's really applicable to like circuit design, too, is you need to, when you're practicing that 10,000 hours, an hour of practice only counts if you're actually getting feedback either from yourself or from peers, right? So I'm going to do a layout on a high-speed design, and then I'm going to have my coworker look at it and tell me what I'm doing wrong in a design review. That hour counts.

**Dave Jones:** Well, the feedback can be from a simulator or it can be from something else, you know? It can be from the compiler. Oh, no, errors, errors, errors, you know? That's all feedback, you know?

**Chris Gammell:** Yeah. That is very important. Because otherwise, you're just kind of banging your head into a brick wall. And that's not really useful. So that doesn't count, right?

**Dave Jones:** Well, it is if you want to knock down the brick wall.

**Chris Gammell:** Maybe. Eventually.

**Dave Jones:** That's not a very efficient way to do it. Andy Dufresne style, right?

**Chris Gammell:** With the, yeah. Rock pick.

**Dave Jones:** Oh, boy. Yeah.

**Chris Gammell:** So practice is important, but only if you have some kind of feedback mechanism. So. Right.

**Dave Jones:** Yeah. Is that negative feedback or positive feedback?

**Chris Gammell:** Depends on your mentor. If it's you, that is negative. There was actually an interesting article from, I think Adafruit posted this today, but it's on GigaOM. And it's one of the former guys that worked at Apple. Yes. Bill Banta. It was really interesting, too, because, so he worked at Apple. But these are just kind of generally applicable hardware notes on, you know, how to make hardware, how to be a better hardware designer. And I think a lot of these things.

**Dave Jones:** It's supply chain stuff, really. True. It's really about the supply chain. I guess so. That's what he's talking about.

**Chris Gammell:** Well, yeah. I mean, yeah, that is his context. But, I mean, these things are also applicable. If you have any control over these things, they're very important. And I think applicable even to smaller projects, you know, even hobby projects. Oh, sure. So, yeah. I mean, like, so he talks about getting inside the factory. That's a big one that I always liked. And not one that a lot of people have experience with. Yeah. And if you don't have, you know, if you don't have a manufacturing facility local and you can't go talk to those people, then you're kind of handcuffed in the first place, right? I've been lucky enough to work with manufacturing people. And you will be surprised at things that they will tell you and the colorful angles that they will tell you it in because they're saying things about you all day long. And when they're, you know, in the lunchroom and complaining about this crappy design that the engineers handed down. Right. I mean, you've worked on test fixtures and stuff, too, right?

**Dave Jones:** They expect in this obsolete part the dickheads, you know. Yeah. Well, yeah. I can't get this part to save my life, you know. Right.

**Chris Gammell:** Yeah. That's from the supply side.

**Dave Jones:** And now it's my fault because I can't get to buy the part, you know.

**Chris Gammell:** Right. Yeah. I mean, you've designed test fixtures before, right? And I'm sure that you've lamented, well, why the hell did they put the test point here, right? I mean, or why didn't they put the test point? That's a big one, too, you know, when you don't put any test points at all.

**Dave Jones:** Yeah, I've now, yeah, someone's just handed me the responsibility to build a production test jig for this board, but the dickhead he laid out the board just has not thought of that. So, God, how do I do it? I don't know. Magic fairies hold test probes against it. Right. You know? Yeah.

**Chris Gammell:** Yeah. Christ. And then, yeah, I mean, in a production environment, oftentimes it's like, well, you're going to try and replicate a user experience, whereas the designer might know, well, okay, you know, if you feed this hex code to the micro, you can actually exercise the whole thing. But no one gives a crap about that, right? And if you were on the floor, you'd know that it's not practical to actually plug in a header each time, you know, or something like that, right? It's just, if you're not on the floor and you don't have context, and context is one of my favorite words in the world, obviously. Right. If you don't have context, though, you know, you just, you're not probably doing good design. And it's funny to think about a lot of industries where that kind of stuff is decoupled, right? I mean, I think about like mobile phones, right? How? Yep. I mean, I'm sure that every mobile phone designer is using a mobile phone, but, you know, in terms of actually develop like an OS and then actually being a full-time user of that future.

**Dave Jones:** Using it has nothing to do with designing it.

**Chris Gammell:** Right, right.

**Dave Jones:** Using, designing a product like a mobile phone is all about the intricacies of getting it manufactured and tested. End of story. Using it has, it gives you no relevance whatsoever to designing. Unless you're the industrial designer of the phone actually, or the user interface guy designing the firmware or whatever, right? Yeah, then that has relevance. But apart from that, if you're actually laying out the boards or doing something else, using a phone has absolutely no relevance to you whatsoever.

**Chris Gammell:** Well, I mean, you might have to put in certain sensors that might be new, right? I mean, that could be a use case kind of thing.

**Dave Jones:** Yeah, but that's just a top-level feature spec, which is handed down, you know, via the stone tablets from bloody Mount Sinai, you know?

**Chris Gammell:** Yes. This phone will have three accelerometers. Exactly. People need to play games. Yeah, I guess you're right. I mean, there's all the DFX stuff, right? There's what? There's design for test. There's design for manufacturability, which is one you were just mentioning.

**Dave Jones:** There's design for reliability in terms of— Design for repair. There's design for environment, and there's— Yeah. Yeah, there's a whole— Yeah, there's design for repair. There's design for—oh, bloody everything.

**Chris Gammell:** Yeah. There's a whole book, I'm sure, somewhere. I used to have a book, so I don't have it anymore.

**Dave Jones:** What are we telling people? It's all too hard. Just get the hell out of the electronics engineering industry now. Leave it to the pros, folks.

**Chris Gammell:** Like me and Dave, who aren't the pros.

**Dave Jones:** Go and become a sales engineer or a marketing guy.

**Chris Gammell:** Well, so that's kind of what we talked about at the beginning of the show, is like, at a certain point, you want to get out of the getting thrown around and, you know, having to design for this little one feature or one, you know, manufacturing optimization, right? And eventually, most people want to say, no, no, I get to define that now. I get to yell at the engineers. I get to talk to the customers and re-dilute it for everybody else, you know? Like, I think that's part of it, you know? I haven't reached that point yet, but I think people want to do that eventually. You think? I don't know. Yeah, I think so. I don't know. So what are some other things on this list?

**Dave Jones:** I'm just out of that game now. I'm just in a different industry now. Yeah, I'm still in the industry, but I'm in a different industry, if you know what I mean.

**Chris Gammell:** Yeah, you're like an entertainer now.

**Dave Jones:** Yeah, I'm an infotainment specialist. That's funny to think about. Yeah, I know. It's like, Billy Mays here.

**Chris Gammell:** Dave does intromercials.

**Dave Jones:** Oh, Dee.

**Chris Gammell:** Some other things on this list are... I don't do hardcore stuff anymore. It's just, nope. Oh. Well, maybe you'll get back to it. Who knows? Yeah, maybe. Who knows what the future holds? Right. Who knows what she who must be obeyed tells you what to do soon? Soon enough. So yeah, some other things on this list are build prototypes close to home. That's a good one, too. I mean, I think that's kind of common knowledge, that just quick turn is worth a lot, right? I mean, you're either going to find someone who does it close to home and pay the price in terms of management yelling at you, or you're going to pay through the nose for farming it out to someone close to home, or pay through the nose to get it shipped to you really, really quickly. I mean, in prototyping, speed is all about... It's the whole game, you know?

**Dave Jones:** Oh, it's speed.

**Chris Gammell:** Yeah, everything is speed. Fast iteration.

**Dave Jones:** Yeah. We'd get, you know, eight-layer boards spun in 24 hours.

**Chris Gammell:** That's insanity.

**Dave Jones:** Yeah, I know. It's madness.

**Chris Gammell:** I want to see that. Absolutely. I want to see that video tour of that, you know, prototyping place. That seems crazy to me.

**Dave Jones:** Well, I do have a video of my PCBs being actually manufactured each step of the process. Right, but not in 24 hours. It's only a lousy two-layer board, and you look at it, and there's like 15 different step, manufacturing steps, which goes into making a two-layer board, let alone an eight-layer board.

**Chris Gammell:** Right, exactly.

**Chris Gammell:** And not 24 hours either. I mean, like, that's crazy. Yeah.

**Dave Jones:** Well, you know?

**Chris Gammell:** I mean, at eight layers, you need to be, like, super automated.

**Dave Jones:** Yeah.

**Chris Gammell:** I think.

**Dave Jones:** Some poor bastard has worked for 24 hours nonstop, or they've handed over to the next shift. You know, there's three shifts which have manufactured your board. You know, they don't just turn it out in a couple of hours. No. No, no, no. It literally takes the full 24-hour process to, you know? And then your board is tying up the whole line, you know? Right.

**Chris Gammell:** You just bought yourself a spot in line, and you get the jumpsies, right? You know? Yep. That's it. No cutbacks.

**Dave Jones:** And that's why we'd pay, you know, $2,000, $3,000, $4,000 for that board. You know? That one board to get it manufactured in, you know? And then it'd be express shipped, you know? Yep. By FedEx or whatever, and, you know, on their fastest service, and yeah, we'd have it in two days. It's madness. Killer.

**Chris Gammell:** That is killer. Yeah. I always wanted to be one of those people that does courier service, where you actually like hop on a plane. You know, your only job is to deliver something.

**Dave Jones:** Right. To hand deliver it, and then...

**Chris Gammell:** It's crazy.

**Dave Jones:** Yeah. Crisis couriers, they call them.

**Chris Gammell:** Oh, yeah. There you go.

**Dave Jones:** Yeah. Yeah. Well, that's what happened when FedEx first started, right? FedEx, they were like a startup. You know, FedEx were a startup. I can't remember the guy's name or how he, you know, quit his job or whatever to start FedEx, right? And he went into bed, and he tried to get venture capital funded and all that sort of stuff. And people just laughed at him. They said, why would anyone need their package within 24 hours? Yeah. Why? That's just... This was back in, I don't know, when did they start? 60s or something.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, or 70s or something. Yeah. That's... He was turned down by every single person. They said, why the hell would anyone need their package so quick? What's the rush? You know? And, well, that's the world. Welcome to today.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. That's right. Well, welcome to the 1980s, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Let alone today. Yeah. We live in a fast-paced world.

**Chris Gammell:** We do. We do. We do. Especially when transportation hasn't gotten any faster. It becomes even more critical that all the handoffs happen at the right times. Yep. These other three points are more supply-side from this article. Yeah. China isn't the only game. Job doesn't end after launch. Blah, blah. Inventory is evil. Yeah, blah, blah. Those three where it's like, yeah, okay, they're good. You know?

**Dave Jones:** Yep.

**Chris Gammell:** The only thing that I didn't like is that the author says, fire an engineer that says it's not possible.

**Dave Jones:** Yes. That was hilarious.

**Chris Gammell:** Yeah, that's a little bogus. You know?

**Dave Jones:** It is a little bogus because sometimes you need an engineer to tell you, no, that's just not possible. Right. Now, I actually agree within, though, on the surface, fire an engineer who says it's not possible. If that's all they're saying. Exactly. If they're sitting in their chair and they say.

**Speaker ?:** That's not possible.

**Dave Jones:** And they say. But here's how you do it. Right. Or here's the changes you need to make to make it possible. That's your good engineer.

**Chris Gammell:** Exactly. Or here's the data that I've already tested that says this isn't possible. And here's a list of reasons why. Like, if you come with that stuff, you should not be hiring. You should not be firing that person. You should be promoting them. You know? You should be putting them in charge of something.

**Dave Jones:** But it never happens. Because, you know, I don't know about you, but I was always the guy in the meeting who sticks his hand up and says, that's not possible. Right. And then that's why I never got promoted. Right. That's why they stuck me in a corner and just, you know, like, that's it. So, you know, that's, but you need. But I would always put a but on the end of it. I would go, that's not possible. This is what you need to do to, you know, this is a better way to do it. Here's a practical way that'll work.

**Chris Gammell:** Right, right, right.

**Dave Jones:** You know, your idea is bullshit. And I could rattle off 10 reasons why, you know. Right. I could, I wouldn't just say, oh, that's not possible. I wouldn't just be the down.

**Chris Gammell:** You know, the guy who's like, oh, there's your problem. If you're the guy who says that, then, then, yeah.

**Dave Jones:** But unfortunately, in the real world, no, that doesn't get you promoted either. Because, you know, if you always, yeah, it's a tough line to, you know.

**Chris Gammell:** Toe?

**Dave Jones:** Yeah, to toe, yeah. Because, you know, the people who got promoted were the ones who would just say yes all the time and then never deliver anything. But, you know, I mean, but because they said yes all the time, they got promoted, you know. I mean, that's.

**Chris Gammell:** That was another discussion I had this weekend with my buddy. It's interesting because, you know, middle management seems like it's a, it's a sea of saying yes, you know, of follow the leader and saying yes and, you know, passing blame and everything. But it's interesting because at some point, and maybe people would argue this point, at some point when you get to be an executive, if you, true leaders at some point have to make that switch, right? You have to navigate through that field of middle management and yes men and everything else and passing the buck. At some point, you have to, someone has to take charge, right? At some point, the buck stops somewhere. Yeah, yeah, yeah, that's right. And it's interesting because someone has to make that switch at some point. And I've, I have no idea how that happens or who that happens to, but. Yeah, me neither. It's not necessarily because there, there are some, I mean, for as much as you and I complain about it, there are some really good leaders out there, right? I mean, some people would call it Tim Cook or other, other people that are like that, you know, they're, they're decisive. They, they, you know, they treat their people well. They, they make good products and everything else. And, but at some point they had, they had to navigate.

**Dave Jones:** And those people never bother with the details. I find like I am a detail guy, right? I will always have a reason why something won't work or a reason why that's something real work or an alternative. And I can just bang, I'll instantly know it, right? Because I'm, I'm that sort of, you know, detail kind of guy. Whereas that's, and that, I don't, you can't be that kind of person. If you go to that top level, you can't worry about the details. You have to. Oh, I see. You know?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, I don't know what I am yet. You just have to learn to let go. I'll figure it out.

**Dave Jones:** Ah, I don't know.

**Chris Gammell:** Well, speaking of details, we should get to the details of our sponsor for this week. We should? Yes. So our sponsor, this.

**Dave Jones:** Try a semiconductor.

**Chris Gammell:** That's right. And they have a new product. My best radio voice. Oh.

**Dave Jones:** They do. And this is, this is high end folks. This is like, this is some serious shit technology.

**Chris Gammell:** This is, I don't think we've talked about it yet, but it's, it's, it's pretty cool. I mean, so we, we've talked about it in, in strokes before. So we've mentioned FPGAs, right? Obviously that's something Dave's worked on, I've worked on. And we've also mentioned in passing FPAAs, which is field programmable analog arrays. And it seems like. We've talked about ASICs too.

**Dave Jones:** Of course.

**Chris Gammell:** Right.

**Dave Jones:** And how it's so expensive to spin ASICs and blah, blah. Right.

**Chris Gammell:** And Triad is working on a new technology. It's a mixed signal. So it's actually kind of a mashup between an FPGA and an FPAA. And it's kind of cool. I mean, like, so basically you, so they have a software called Via Designer. And that's actually what's sponsoring this week is called Via Designer and viadesigner.com. Designer.com. Yeah. And then there's a slash the amp hour if you want to go to the page dedicated to us. But, so you can go on there. And then basically it's like a block diagram definition of analog blocks, digital blocks, and everything else. And then you can define the different characteristics. And we'll get into this later in the week too, kind of the specifics of it. But you can basically design a signal chain, a mixed signal signal chain through this program. And then download it to something called a Via ASIC. And Via ASIC is basically that mashup of FPGA and FPAA. So, it's pretty cool. I mean, I'm excited about it. I have not tried it yet. Dave has not tried it yet in person.

**Dave Jones:** No, it's a high-end solution for, you know, higher-end problems.

**Chris Gammell:** Right. Exactly. Yeah. Like, they are a partner with NASA. Yeah, right. If that doesn't say it, I don't know what it is. But, yeah. It is going to be higher-end. But, you know, they're working on really interesting technology. I mean, like, this is one of those great deals where they wanted to sponsor the show, but it's also really cool tech. So, it's kind of balancing that line of, you know, well, I really do think this is cool.

**Dave Jones:** How much work goes into writing that software?

**Chris Gammell:** A lot more software than I've ever written. It's incredibly extensive. Yeah.

**Dave Jones:** I mean, it's just ridiculously, you know, just the feature set of. Yeah. Software like that. It's just incredible, you know, with the simulation and everything else and the whole.

**Chris Gammell:** Yeah. So, there's different parts you can buy. There's VCA. So, VCA is via configurable array. There's one through 12. And me and Dave were trying to find these before the show, but I just found them. So, like, the VCA12, it's got a bunch of, it's got, like, 14 op amps, five single-ended OTAs.

**Dave Jones:** 12, 1,100 resistors, 738 caps. 5,000 ASIC gates. It's got caps on die, you know. It's got high voltage transistors. It's got, yep, 5,000 ASIC gates and 46 IO configurable IO pins.

**Chris Gammell:** Right. And so, it's not necessarily, you know, like, it's, like, always that balance point, right? I used to get really excited about, there was another company that was doing reconfigurable analog. And then I got to it, and I'm like, oh, the specs aren't as great as I am. But the real thing is not necessarily the specs on, I mean, these are good specs, but it's a reconfigurability that really matters more so than anything else. So, if you value reconfigurability, that's really where you're going to find a lot of value in this kind of thing.

**Dave Jones:** Like, if you designed your product, right, and you've released it out in the field, and then you go, damn, look, in this usage case scenario, we really need some extra filtering in that part of the chain there. Right. And, like, in your traditional design, you've got to re-spin the whole thing. Yep. But, you know, here, you can just go, well, I can whack an extra filter in there.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Not a problem.

**Chris Gammell:** So, we will be talking about them more throughout the week, but we want to introduce them from, you know, our new sponsor. So, I think we found a good one. Thank you very much. Yeah. Thank you, Triad.

**Dave Jones:** I like it.

**Chris Gammell:** So.

**Dave Jones:** And they do ones with RF transceivers as well, up to 3GB. Yeah. They've got the RF VCA version of that.

**Chris Gammell:** Which is, of course, way out of our expertise.

**Dave Jones:** And then they've got ones with, hey, Arm Cortex. There's one with an Arm Cortex M0 as well.

**Chris Gammell:** Yep.

**Dave Jones:** So, they've got analog, digital, and Arm Cortex M0 on the one chip.

**Chris Gammell:** Very impressive. Very cool. Very cool. Yep. So, we'll link that in and check out viadesigner.com slash the Amp Hour for more information. Speaking of RF, I'm trying to decide if I'm going to Ham Fest in Dayton this year. I'm sure I'm going to hear a lot of stuff from our listening audience of, yeah, you got to go. So, it's apparently, so, Greg Charvat, the former guest of the Amp Hour, he's been trying to convince me. And I'm thinking about it. I'm really thinking about it. But, I don't know, man. I feel, I felt a gunned, you know. Just said, I.

**Dave Jones:** So, how far is Dayton from Cleveland?

**Chris Gammell:** Dayton's about three and a half hours. Three and a half hours. Oh, okay. Yeah. But, I mean, to hear Greg talk about it, it seems like it's a.

**Dave Jones:** That's a decent drive.

**Chris Gammell:** No, it's not. Really? Do you know how long it takes me to get to, like, Colorado or California?

**Dave Jones:** Well, yeah, it's a different state.

**Speaker ?:** I mean.

**Chris Gammell:** I guess, yeah. Kansas alone is, like, what, seven hours, eight hours for me? I mean, just to get through that. Oh, that was a terrible drive. Driving across the U.S., you know, as much as it's romanticized. I went through Kansas.

**Dave Jones:** You wanted to see the Jeweling Banjo Festival?

**Chris Gammell:** I wanted to see where Crystal Meth was born. No, I, sorry, sorry to all the Kansans out there.

**Dave Jones:** And let me guess, you were running moonshine, too, in the boot.

**Chris Gammell:** Right, yeah, yeah, yeah. No, no, I had, I went out, I went to Colorado for spring break with some buddies and drove out there and, you know, it was, I don't know, I just, the romanticized road trip is just not my, it's not my thing. I don't know.

**Dave Jones:** Right. And it's never as good as the movies, right?

**Chris Gammell:** Never, ever. Come on. I mean.

**Dave Jones:** No. No, it's just boring as bad shit, right? Gas stations and, you know. Yeah, it's gas stations and dodgy food. Trying to stay awake in the car.

**Chris Gammell:** It's, ugh, driving.

**Dave Jones:** Ugh. No, thank you. Yep.

**Chris Gammell:** But if I was on the sea, maybe that would be a little more interesting than driving, especially if the boat I was on had a huge-ass laser. Did you see this video? You're just obsessed with it. I'm not obsessed with it. It's just, I mean, like, the technology is crazy.

**Dave Jones:** And we've had it on here before. You've put it on here before. Every time there's a new video released of some ship blowing up a plane with a laser. No, it wasn't a laser. No, it's Johnny on the spot.

**Chris Gammell:** No, last time it was a rail gun. All right, first off, think about the power requirements for this crap, right? With a rail gun, it's like, you know, it's like thousands of amps at a time. I mean, like, that's magnetics, obviously. But lasers, I mean, that's a whole other game, you know? Like, that's just something.

**Dave Jones:** Yeah.

**Chris Gammell:** I don't know, man. That's, like you said before this show, that's like some Star Wars stuff, you know? Yeah. I mean, not really, but.

**Dave Jones:** But I'm not going to be happy unless it actually, you can see the beam fire out. You know? Yeah.

**Chris Gammell:** Which I don't think is very realistic in general.

**Dave Jones:** I want to see a pulse of beam go boom and then a plane blow up. Otherwise, it's just boring. I don't know.

**Chris Gammell:** I guess so.

**Dave Jones:** So the only thing you see is this green dot on the side of the plane that catches on fire. Whoop-dee.

**Chris Gammell:** Yeah. I don't know. It's scary, though. I'm not a big fan of military technology in the first place, but it's kind of cool.

**Dave Jones:** No, that's some heavy-ass engineering right there. Oh, yeah. I mean, that's, you know. Yeah, the power requirements are, you know. There's two technologies here. There's one, the power supply requirements for this thing. You know, the energy, just the pure energy storage. And two is the physics that goes into producing the laser. Like the cooling and everything else. Yeah, at that amount of power. Yeah. It's probably cryogenically frozen or something. Yeah. Cooled or something. I don't know.

**Chris Gammell:** Yeah, I saw Mike Harrison did a video on lasers. I haven't watched it yet, but I need to watch that one. Oh, is that new? He was talking about low-end lasers. Mike's electric stuff. Mike, former guest, Mike Harrison.

**Dave Jones:** Yeah, I didn't know. He had a new video on lasers.

**Chris Gammell:** Oh, yeah, new video.

**Dave Jones:** YouTube alerts.

**Chris Gammell:** I would add a third one to that list of engineering challenges, too, though, is control systems. I mean, this is a little bit less technically stringent, right? But it's, you know.

**Dave Jones:** Well, that's the third leg of this, is to be able to target and track the plane. Because this laser doesn't just have to hit it once. It's got to stay on it for like five seconds or something, right? Yeah, exactly.

**Chris Gammell:** It's no longer like you're firing something like a smart missile that can then, you know, it has its own control system on it that can go find heat or whatever. This is like you are a fixed point. There is something, you know, a thousand meters away, and you have to stay fixed on that. So as the boat bobs up and down, you have to, you know, compensate and everything else.

**Dave Jones:** But the thing is, the plane never, it's just a drone which is continuously flying. If there was a pilot in there, they'd be going, oh, shit, my ass is hot. And they're just going to get the hell out of there.

**Chris Gammell:** Move away from green dot. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. It's tough because it's, you know, like I said, it's military tax. So it's like, ah, God. You know, they always have so much money behind it, right? Like DARPA. Yeah, yeah. Right? I mean.

**Dave Jones:** Well, they only spent a lousy 40 million bucks on this. That's chump change.

**Chris Gammell:** Well, on that one. But I mean, just the breadth of their programs, it's just, it's unbelievable, right? I mean.

**Dave Jones:** Yeah.

**Chris Gammell:** How about this Petman? Did you see this video of? Petman? Petman from Boston Dynamics, the robot company that does.

**Dave Jones:** No. Petman. What is this? A man who has a thousand pets. What?

**Chris Gammell:** No. It's an upright walking robot. And Petman has been out before. I mean, so it's like a gyro-stabilized robot that actually walks on two legs. It has arms, right? It's super creepy.

**Dave Jones:** What a ridiculous name.

**Chris Gammell:** Yeah. I don't know where that comes from. It's an acronym, obviously.

**Chris Gammell:** But it's a DARPA funded thing. And basically now what they did though is, so they just released a video of it walking on a treadmill, right? Alone, not scary. But because it's wearing a camo suit, it's got this really herky-jerky motions. And it looks quasi, you know, you can't tell necessarily it's a robot, right? You could probably get someone to make these motions with their body. Oh, it is so creepy. I hate it.

**Dave Jones:** But you know just something's not quite right there and that's going, oh, shit. Robots creep me out. And your mind starts thinking Skynet, you know?

**Chris Gammell:** Exactly. Yeah, exactly. I mean, like, I don't know if that's ever going to go away, right? I mean, like, even if you get to the point of sentient, you know, kind robots, you still kind of, you get into the iRobot side of things, right? You know, like the Will Smith movie. It's like, well, obviously it was an Asimov novel first, but. Right. I don't know, man. Oh, it's just so creepy. I mean, I'm sure we've talked about this before, the Uncanny Valley, right? Where, you know what that is? Yeah. It's like the robots look just human enough to really, they're like, they look more and more and more human. To give you nightmares, yeah. Right, well, no, it falls off at a certain point. So they look more and more and more human, but they get to a certain point and they look just close enough that they creep everyone the hell out. You know, like all those robots that, like, they make in Japan of, like, actual faces, but you can still tell the robots.

**Dave Jones:** Oh, right, yeah, right. Yeah, there's a whole robot sex industry, you know.

**Chris Gammell:** Yeah, the heebie-jeebie industry. Yeah. But, you know, it's, I mean, the technical side of me loves it. I mean, like, the control systems and just the power requirements and everything, you know, like, they need tons of awesome stuff. Like, all of, like, Boston, too. Boston is just a great robotics area. And it's a cool industry and everything about it. But, man, if it's not a Roomba, it scares the crap out of me. And you've got to watch the video, man. It's really, really creepy. I don't know.

**Dave Jones:** Anything that you can't just kick over, you know, can't just bugger off, you know. Even if I could kick it over, then it just lies on its back and flicking its legs, you know.

**Chris Gammell:** No, because if it's kicking its legs and it looks like a little bug, then it creeps me out. I'm afraid of bugs, too. Right. I'm a very frightened person in general.

**Dave Jones:** Well, you have to come visit Australia. We got... No. None of that here.

**Chris Gammell:** I know what you're talking about, but no. Oh, the spiders and everything else out there. Oh, thank you.

**Dave Jones:** Dude, we have to talk about this. The world is just gone crazy. They're not printing markings on resistors anymore.

**Chris Gammell:** I saw this. So, this was posted on Dangerous Prototypes. But this has been going on for a while, right?

**Dave Jones:** It's been going on for a long time. They just decided to... Yeah, I guess it's the first time they've seen it, right? I've seen it before. It's not a...

**Chris Gammell:** Well, I mean, I've been seeing the trend, but it's not like... I haven't seen any official announcements, but... You say Yegio or Yagio? I don't know. Yeah, Yago. Yeah. But they officially announced that they're not doing it. Yeah, but they've made an announcement.

**Dave Jones:** Yeah. From July 1st, 2013, they will no longer put markings on all of their resistors. And...

**Chris Gammell:** It sucks.

**Dave Jones:** I guess you can... Well, if you don't like it, you can vote with your wallet. Go to another manufacturer that does. And they're saying... The thing is, they're saying the reason for the change is to reduce, quote, unnecessary chemical usage for environmental protection. Bullshit. It's to lower their bottom line. Yeah, exactly. It's to improve their bottom line.

**Chris Gammell:** Every time you print something, you silkscreen, it takes... It's not actually the cost of the ink. It's an extra step. It's the cost of the time. Yeah.

**Dave Jones:** Exactly. It's an extra step. And when these things cost 0.00001 cents each, especially for Apple, you know, they're...

**Chris Gammell:** No. Right. They figure that it's being placed anyways. And then most of their industry... They probably did a calculation of most of our market is consumer or anything else. Anyone buying these resistors are low enough cost. And at that point, you're not designing for repair like we mentioned earlier in the show. You are designing for manufacturing and high-volume manufacturing. And if it's breaking, you're just throwing it out. You know, it becomes the 0.1% yield that you lose. You know, like that...

**Speaker ?:** Yep.

**Chris Gammell:** I guess it wouldn't be yielding.

**Dave Jones:** And if you've got thorough and extensive testing procedures, it doesn't matter if you have... You know, like it matters to prototypes, right? If you're the designer and you've manufactured your prototype, you get it back, you need to verify that that resistor is, you know...

**Chris Gammell:** Yeah.

**Dave Jones:** ...is the value that you designed in and they haven't programmed the pick-and-place machine wrong, blah, blah, blah, blah, blah, blah. Yeah. Right? Right? And... But once you've got all your manufacturing set up properly, it doesn't matter a rat's ass. Yeah. And that's why a lot of manufacturers will try and save a couple of cents by not silkscreening their boards either. Because that's one less step in the process. You can save, you know... Exactly. ...10 cents per board if you don't get, you know, a top silkscreen on with R1, R2, you know? Yeah. You know what I mean? Yeah.

**Chris Gammell:** And there's a little bit of a security, you know, IP kind of thing there too, but it's probably not the main thing. No, possibly. The main thing is cost. No. Yeah. Almost everything is driven by cost.

**Speaker ?:** Yep.

**Chris Gammell:** Yeah. Yeah. It's tough too because so like when you think about like prototyping and, you know, probing a board, right? I mean, like I can't tell you the number of times where I'm like, oh, I'll just probe this. You know, I'll do a easy, I'll ohm out this resistor and then, you know, there's another one hiding just underneath the surface that's in parallel with it and then I think, oh, this is the wrong resistor value. This is what it... Yeah, yeah, yeah. Oh, wait a second. Wait a second. Desolder it. No, it was right. That's terrible. Have you ever seen like maybe if someone could make like those tweezers, those like heated desoldering tweezers, but then also build in like a grunty ohm meter. That is an invention, my friends. Right, right there. Pull it off and measure it immediately and then place it right back down. That's the... That's the... That I would...

**Dave Jones:** No, I'll tell you what you need, which a lot of meter... Most meters do not have these days.

**Chris Gammell:** What's that?

**Dave Jones:** I'll tell you what, is a low voltage ohm measuring range. When I was a boy...

**Chris Gammell:** Yeah?

**Dave Jones:** They had... Multimeters had a button on them. I had this button on them, you say. And it was a physical button. It gives you a low ohm voltage range so you wouldn't turn on semiconductor junk. Wing jubbies. And, you know, and yeah, I mean some multimeters do. When you go to measure resistors in circuit, they will turn on, they'll have a high enough voltage to turn on PN junctions, you know?

**Chris Gammell:** Oh, interesting. Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** See, usually it's not the PN junctions that trip me up. I mean that has happened before, but... Well, it's other. Yeah. Yeah, mostly it's the... It's other things in parallel. You know, you see another ground or something like that.

**Dave Jones:** Well, and that all comes back to, you know, semiconductor junctions. And then you've got all the shit across your rails and...

**Chris Gammell:** Oh, yeah. Yeah, I guess so. Yeah.

**Dave Jones:** You know. It's a...

**Chris Gammell:** How high voltage does it go? Does it, like, 100 volts?

**Dave Jones:** Well, enough to turn on semiconductor junctions.

**Chris Gammell:** No, it's like 10 volt kind of thing, right? It's not...

**Dave Jones:** 10 volt? No. You only need 0.62 volts to turn on a semiconductor junction.

**Chris Gammell:** Yeah, I know that. But I mean, like... I mean, there could be limits of other things too, right? I mean, break it through oxides or anything else. I don't know. I don't know why the hell you'd do that. Like, you're just talking... You're talking about, on like an ohmmeter, having the current limit, it has a voltage limit as well, so it doesn't...

**Dave Jones:** Well, it has a voltage, yeah. I mean, current limits aren't just magic. They don't just, you know... There's not zero volts in your system, you know? Right. Kirchhoff's law must apply, you know? Yeah. So, yeah. They have a maximum voltage.

**Chris Gammell:** That's been pissing me off recently with... I've been doing some SPICE stuff recently. And current sources... Using what package? LTSpice. I mean, this is just a generic thing, though. Right. Just plan, right? Yeah. Using... You know, I love... I love thinking of circuits and, you know, from a current perspective, right? I mean, I always... Making that switch was a very big deal for me, obviously. And I think everyone... Everyone hits that point of, oh, voltage... No, no, no. Current. Current is where it's at. Right. You know. You know what I'm talking about. And... Yeah, yeah. But programming in current sources into SPICE is dangerous, right? Because, you know, if you turn off a... So, if you have a current flowing through something... Like a switch or a transistor or something... If you turn off the switch or the transistor, then it spikes to, you know, kilovolts and stuff like that, right?

**Dave Jones:** It's going... Well, it spikes to the maximum voltage you've set.

**Chris Gammell:** Exactly. And it's just... Well, LTSpice doesn't have that limit in it. So, maybe that's the problem. There's no voltage limit built into the current source in LTSpice. At least, maybe not that I've found. So, usually I end up putting, like, a diode in peril... Or a zener in peril or something to try and mimic my system, right? Because if you have a current source, eventually it's going to run out of headroom on the voltage side of things, right? So, if you have a current source that you're using, usually, you know, 12 volts, 20 volts, whatever. Eventually it's going to run out of headroom in a voltage standpoint. And it's going to stop producing the current you need. Yep. Because current sources are a load of crap. I'm taking a stand here, folks. Current sources aren't real! There's a t-shirt slogan for you. Yeah, there it is, right? I will put that in. T-shirt slogan to remember. Current sources aren't real.

**Dave Jones:** He's actually typing it, folks. Yeah. Yeah.

**Chris Gammell:** I will remember this run. Now I've lost my train of thought. But anyways, yeah. It's tough and spiced when you use current sources. You know, you need to have realistic boundaries at some point.

**Dave Jones:** Well, because you're not using them for a practical simulation of your circuit. You're using them more as a concept thing.

**Chris Gammell:** Right. Exactly.

**Dave Jones:** To test a concept or something like that. You know, it's not, you know, unless you actually have a real current source in your system. Right. Which don't exist. As the t-shirt says. Yeah, exactly.

**Chris Gammell:** Yeah, because you're right. I mean, if I was trying to simulate a current source as I, you know, use one on my bench, right? If I have a DC current source on my bench, that's not really a current source. That's a voltage source with a current feedback so that it, you know, that it uses that as a control mechanism. Yes.

**Dave Jones:** Because my current source here has a maximum voltage knob on it, you know, from 10 volts right up to 1,000 volts. Right.

**Chris Gammell:** And that might be the current source that I used as well. But, yeah, it's, you know, it's tough to, you really have to simulate what you're actually using, right? The theoretical models, it's not realistic.

**Dave Jones:** Well, yeah, but they're useful for concepts, you know, for testing concepts. Right. And that's generally what I use simulators for. I'm not testing, like, my, you know, to see if my circuit works, you know, at every single, you know, at a real practical level with all my practical parts in there, blah, blah, blah, blah, blah. I'm testing some sort of concept, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Is it stable? Will it oscillate? Or, you know, will it, you know, is it going to give the accuracy I require? Or something like that, you know?

**Chris Gammell:** Yeah. Oh, what else should we talk about this week? Or do you want to keep talking current sources?

**Dave Jones:** I didn't give a toss about current sources. You bored up.

**Chris Gammell:** I did, too. Yeah, you're right. Sorry, I got distracted thinking about, uh...

**Dave Jones:** And now you pissed away the rest of the show, because our time was on.

**Chris Gammell:** No, we're still, we're fine. We're, we're fine.

**Dave Jones:** We had people complain the show doesn't go long enough.

**Chris Gammell:** We can keep going. Um, so, okay, so here's, I have stuff from, so I was looking at vintage stuff, right? Vintage amp hour from all of two and a half years ago, right? And I'm like, oh, workbench of the week, how quaint. And then I asked for suggestions on Twitter and Facebook today. Someone sent in the workbench. So, this is going to be workbench of the week. Woohoo! Cue the clip. Did we... We got rid of the clip? Remember I used to do that stuff? That's what I'm talking about. I don't even remember what the clip was. I know, that's what I'm talking about. Workbench of the week, week, week. I remember that! Okay, so I said, Dave, I just sent that to you, because I actually didn't send it to Dave. But this is from... Oh, crap. Who's it from? It is from... Jose Reyes on Facebook. He sent it in, and because he did, we were going to talk about it. So, he sent in a picture of his workbench, and this is actually a log of his build of it. So, this is kind of cool. It's a flicker set. But it looks like he's got... Oh, yeah. This is the classic. This is the same one I have. The cheapo power supply special. I have the HY3002. You see that in the top left there? It's from Electronics Express. That's the one I got it from. I've seen them a couple different places. But that's actually not a bad power supply. I don't know if you've used it.

**Dave Jones:** I've used them, yeah. They go under generic brand names. Like there's one company that manufactures on it. Exactly.

**Chris Gammell:** Yeah, my display broke on it, but it's a pretty solid power supply. It's not bad. All right. Big old orange button. And there's an analog scope. Analog scope. Classic. Classic. Yep. What kind of soldering iron is that? Is that a... It's not a Metcalf, is it?

**Dave Jones:** That's a... No, that's a Heiko.

**Chris Gammell:** Heiko. Okay. Yep. And then he's got some...

**Dave Jones:** I believe, anyway. Yeah. It's a bit fuzzy, but it's blue and yellow.

**Chris Gammell:** Blue and yellow is usually a sign. Either that or a ripoff on it, right? Right. Oh, there we go. Yeah, yeah, yeah. Then he cuts it to the... He cleaned up his bench at one point here. So he looks like an RC hobbyist. But yeah, this is good stuff. All right. Well, I guess that's all we have to say about it this week. But... Workbench of the week. Yeah, exactly. Week. Week. So thanks, Jose. We do appreciate people sending it in. This was a last minute ask, so I thought it's a nice retro throwback. Good old days.

**Dave Jones:** Because we've been doing this shit for two and a half years. Two and a half years.

**Chris Gammell:** Oh, he's got a dope drill press and later pictures. That's an important one, too.

**Dave Jones:** Oh, yeah. All right. Oh, yeah, yeah. Oh, there we go. Now we're talking.

**Chris Gammell:** Yeah. That's nice and messy.

**Dave Jones:** That's good stuff. Now it's filled with stuff. Yeah, exactly. That's what I want to see. Yeah, you can't see the bench anymore. That's what you want. Right, exactly. Because it's just filled with so much crap. Yep. Brilliant.

**Chris Gammell:** Okay, so people may remember I used to do Chip Report TV. Yeah, you used to until that failed. Yeah. It didn't fail. It just faded.

**Dave Jones:** Well, you just... Yeah. It faded.

**Chris Gammell:** Couldn't be bothered anymore. Yeah. But so since I don't do that anymore, so people have asked about that, too. So in the survey and everything else, they said, oh, I'll bring back Chip of the Week and everything else like that. And I found one this week that I really like. It's pretty cool. Yeah. And it's actually kind of relevant to our current source discussion before. Because, you know, in a perfect current source, right, you would have something that doesn't give a crap about what kind of load you have in line or resistance or anything else. And this is a new part from LT that actually it's meant to compensate for drops in cables. Right. So this is the LT6110 cable wire drop compensator.

**Dave Jones:** As in power drop? Or we're talking data comms?

**Chris Gammell:** Well, that's interesting you ask that. Because basically what they're saying is that if you try and put power over a data line, like a power over Ethernet with real tiny wires and stuff like that, you have a really big drop to deal with normally. And so basically that's the market it's meant for. It's meant for like, you know, power over Ethernet, 48 volt kind of stuff. Right. Or, you know, if you're just kind of in a tight spot. So that's the part I kind of like is if you're in a tight spot, you can have this monitoring chip there and it will monitor.

**Dave Jones:** Oh, what it does. I'm looking at the block diagram here. What it does is you can't use it on its own. But what it has is a little current sensor in there. And then you put it in the feedback loop of your regulator.

**Chris Gammell:** Yeah. Oh, yeah, yeah, yeah.

**Dave Jones:** So it tricks it out on your regulator. Exactly.

**Chris Gammell:** It tricks it out so that so like if people think about like a cable drop, right, you need to actually ramp the voltage much higher to overcome the resistance in a cable in order to get the current out at your load. Right. What this does is it kind of it kind of hides that from the feedback until it supplies the correct amount of current and voltage. And then then it feeds back the right signal. And so it's a very sneaky chip. But, you know, LT's done this kind of stuff before where they've had paired chips before. Obviously, they probably want you to use their regulator as well.

**Dave Jones:** Well, let's talk about that, shall we?

**Chris Gammell:** Yeah. Oh, right. Yours. Yeah. Actually, this is...

**Dave Jones:** Yeah. You know how I spent ages designing this LT3080?

**Chris Gammell:** Yeah. This is for your...

**Dave Jones:** This wonderful regulator chip, which we've talked about many times.

**Chris Gammell:** This is for your power supply and everything else?

**Dave Jones:** Power supply. Yeah. Yeah, yeah, yeah. And there's issues with it. It appears that there are issues with it.

**Chris Gammell:** Really? What's going on? They're blowing up. They're blowing up. Well, that's not always a chip issue. Let's just get to that first.

**Dave Jones:** No, but... Well, no. There are discrepancies in their data sheet. And we still haven't got an official response back. But there's a forum link. Go check it out. And somebody found this at pretty much the same time I did. My latest prototype, I've been blowing up LT3080s. And I haven't had time to properly investigate why. Yet I've just been too busy. I'll de-solder and, oh, I don't know. I'll blow it up. I'll have to investigate. Yeah. And putting in a new one, oh, it blew up again. Shit. That is the worst. Yeah. You just keep going through it. Somebody else had the same problem. Yeah. And then it turns out that they've got three versions of this architecture chip. The LT3080, the 3083, and the 3085. And it looks like the 3083 and the 3085 have a fix. Like, there's a slight difference between them and the 3080. And it has to do with back-to-back diodes between the set pin and the output pin, which they don't. Well, they tell you about, but it's, you know, one of those little asterisk notes in fine print that if you don't read. And by the way, there's back-to-back diodes between, you know, the set pin and the out pin. And it has to do with the amount of current which goes into the set pin. If it goes over 10 milliamps or something, forgive me if I'm getting it wrong, but, yeah, it can latch up the chip or whatever, something like that. And that appears to be what's happening. And they don't tell you that in their spec. Their spec is wrong. And, yeah, and the other two versions of the chip have a series resistor in series. They have a resistor in series with the two back-to-back diodes, which the LT3080 does not. So that sort of implies that they've secretly discovered this problem. And in the newer versions, the 3083 and 3085, they've fixed it by putting in a series resistor. But they haven't bothered re-spinning the 3080 to fix the problem. So, yeah. And there's discrepancies in the specs, as I said, and it's all very confusing. And based on their specs, their own application circuit should not work. Their own application circuit will exceed the specs and potentially blow up the chip. And that's what I was following, right? I thought, oh, there's their example application node. It's got a big capacitor on the set pin. Not a problem. But apparently having that capacitor on the set pin can cause the set pin to then, if you short your output, because you've got a capacitor on the set pin, it can hold that charge there. Then you can get a big voltage differential between the set pin and the out pin of your regulator. And bingo, that suddenly exceeds the spec and boom.

**Chris Gammell:** Yeah.

**Dave Jones:** You chip blow. Anyway, that's the theory that several people have got at the moment. And it seems plausible to me. And we're waiting for a response back from LT.

**Chris Gammell:** Well, we will have to wait. Yeah, but saying 3080 triggered my memory. And it triggered memories of one of the most frightening and awesome emails I've ever gotten, which was from Bob Dobkin mentioning.

**Dave Jones:** Bob Dobkin. Yeah, when we mentioned the chip.

**Speaker ?:** That's right.

**Dave Jones:** He's actually done a video on the LT30. Didn't he design it or something? It was his little baby?

**Chris Gammell:** I think it was his, yeah. And so he wrote us an email thanking us for, I think it was back in May of 2011, we covered it on the show. And then he wrote to me. I'm just like, what? I mean, this is the CTO of Linear, right? That's crazy, man. Yeah, yeah, yeah. That's right. Everyone says he's an awesome guy. I've never met him. But yeah, so maybe right back.

**Dave Jones:** Maybe he can come on the show and explain the LT38 and why they're blowing up.

**Chris Gammell:** Well, he said the 3092 is the 200 milliamp version of this too. So maybe that's another good comparison point. Because you said the 3083 and the 3085. So if the 92 has the same thing, I don't know.

**Dave Jones:** Right. But anyway. Anyway.

**Chris Gammell:** You never want to be the one who finds the errata in silicon. No.

**Dave Jones:** Well, and that's the problem, right? I've spent forever and I've done like 15 videos, right? Yeah. Of this power supply design, designing in the LT3080. And I'm just at the point where I'm trying to get this, my final prototype, tested and into production, right? So I can finally finish this heap of shit.

**Chris Gammell:** He says for the second year in a row.

**Dave Jones:** Right? Yeah. Well, that's right. But, you know, I was, but this time I mean it, you know? Yeah, that's right, folks. And then all of a sudden this LT3080 problem comes along. Yeah. And now I've got to decide whether or not I should just go, look, screw this. I'm going to abandon this. I'm not going to take the chance. Even if we think we've solved it, right? We think that we may be able to solve it by putting shocky, like low voltage drop, shocky diodes in parallel with the voltage regulator, right? Because by measurement, the internal ones aren't shocky. They're 0.6. So if we use shock keys, we can keep it to 0.3. And that brings it under the spec and it shouldn't blow up. But, well, how do I test that, right? I could test it here. I could build 10 of them and test it. But what happens if one in 100 fail?

**Chris Gammell:** Yeah, the stochastic smoke test. Yeah.

**Dave Jones:** So I go into production and I'm going to build thousands of these, right? I'm sure. Well, hopefully. Probably a thousand. Well, you know, based on my microcurrent and everything, you know, I'd be surprised if I couldn't sell 500 or 1,000 of these things. Yeah. And, you know, I've got to take that chance.

**Chris Gammell:** Well, more so than that, too. I mean, you think about the whole – so your whole forum has been looking at this chip, right? Obviously, other people look to you as, you know, someone who's designing with it. And so obviously, it's a trusted part. Yeah, yeah, that's right. It's just like a waterfall effect, right? Oh, well, Dave used it. I'm okay with using it. Yeah, that's right. And that happens with us, too, right? We use it because of application circuits.

**Dave Jones:** And then I – the reason I used it is because it had the – you know, the example. So I was just following one of the example circuits LT had. So I thought, oh, LT must have tested that, you know? Well, I'm sure it did.

**Chris Gammell:** So I was safe.

**Dave Jones:** And then it snowballs, as you said, yeah. Yeah. Everyone starts trusting everyone else.

**Chris Gammell:** And that's why recalls suck ass.

**Speaker ?:** Yeah.

**Chris Gammell:** If you ever get in a chance – if you ever get in a position where you have to do a recall, you are screwed. I mean, I can bank for businesses, right? I mean, like, it's a real thing. If you have a true recall, there is no – I mean, because it's not just your product getting – you know, you don't just have to replace it, right? Maybe you have to get 10,000 units back and you have to desolder a chip and resolder it and send it back out. There's cost to that. But then there's also – you know, then there's, like, the car manufacturers where they just recall the entire product line. And then there's the things like the Toyotas where they don't only recall the product line. They're hurting people and their brand name is hurt, right? I mean, like, there are so many levels of crap that can hit the fan. It's just unbelievable. So test your stuff. Absolutely, folks. Oh, you know.

**Dave Jones:** Although, I must say, in the defense of LT, I am trying to drive the set pin, which is not the – Ah. You know, which is not the mode of operation of this chip, right? I'm trying to override it. But, you know, it's got a pissy little 10-amp, 10-micro-amp current source on that pin, so I can drive over that, you know.

**Chris Gammell:** Right. And then marketing pops in. They say, well, we specced it that way, right? I mean, that's – and that's why people say they have specs, right? I mean, like, there's always that corner case where, you know, you're going to either get in a lawsuit or – in a worst case or in an argument or something like that. It's tough, man. So you're driving against the current source?

**Dave Jones:** Yeah, I'm driving against the current source. Yes, I'm overriding that current source.

**Chris Gammell:** I guess I didn't quite get that. Oh, man.

**Dave Jones:** So, you know, but, hey, but based on what people are finding in the data sheets for this thing now, several people are investigating, it looks like, yeah, their own application circuit in the data sheet will ensure that the chip exceeds its own specs.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, I mean, it's just crazy. And so now I've got a huge decision to make, right? I've got to either trust – either push on with this chip and try and, A, solve the problem, B, you know, take a risk that it's not going to happen, you know, in when I manufacture a thousand of them. And – or I can just go, look, screw this. I don't trust this thing any further. I can throw it. You know, I've been built once, once bitten, twice shy. I'm just going to abandon it and go with something else. Yeah. And that's – you know, and like – and even if LT come back and say, oh, yeah, yeah, blah, blah, blah. And we assure you that it will meet its spec, blah, blah, blah. And, yeah, we'll fix the data sheet, right? That still leaves a cloud, right? I can't just go back to them later when my things fail out in the field and go, but you said this, so you are going to pay for it. They're just going to go give me the finger and go, well, bugger off.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Yeah.

**Chris Gammell:** It's tough, right? It's a confidence game almost, right? It's like a – you know, it's like that with any – it doesn't matter who the vendor is. At a certain point, you have to decide. You know, you have to make that decision. I'm going to production with this, and there are serious consequences if I – if something goes wrong, right? Like there was an article.

**Dave Jones:** And the bug stops with me. It's my money and my ass on the line.

**Chris Gammell:** Right. But not always. That's not always the case, right? So there was an article today I saw. There was an article. It was a press release because they love this kind of stuff from the company side. But NXP talked about how Moscow selected their part for like a ticketing system in Moscow's transportation center, right? Right. And it's like in that case, you know, like that's even worse because someone at the top at like a purchasing level made this huge deal with them, right? And the bug stops at the bug, right? It's not like they were deciding based on – I mean, hopefully there was some kind of decision-making process based on technical side of things. But in that case, it's like, yeah, you know, sometimes you don't get a choice in these decisions. It's crazy. I don't know. Like, have you ever been – have you ever had to design what other people told you to design with before? Oh, of course. Yeah. I mean like –

**Dave Jones:** Countless times.

**Chris Gammell:** Yeah. Yeah. Hand-strung by vendors, decisions and purchasing agreements.

**Dave Jones:** I think we keep going over the same stuff all the time. We've talked about this, I'm sure. Maybe even a couple of weeks ago. It seems familiar anyway. That – yeah, often that can be a good thing, being told what to do because then you've got less and you've got no choice. You have to – as a designer, you have to – well, you know, hey, my hands are tied. Fine. At least the boundaries are set.

**Chris Gammell:** I don't know if that – yeah, we did talk about that. But we weren't talking about vendors. We were talking about design constraints. I don't think which parts I could use would be part of that. I don't know. I wouldn't list the parts I can use as an input that I want constrained. If you can tell me I have – Well, but no, but sometimes it's good. I have half a lot of power. If I have half a lot of power, that's a design constraint I can work with, right? Like, because then I can go out and I can seek out different solutions and –

**Dave Jones:** Well, but no, like trying to pick a microcontroller, right? There's millions of them. How do you pick, right? It's ridiculous. Whereas if somebody tells you we have to use this microcontroller because we use it in our other product, well, that's fine. Your decision is made for you. I don't have to spend a week agonizing over which bloody microcontroller to use.

**Chris Gammell:** I guess so. I don't know.

**Dave Jones:** I mean, sometimes it's just good to be told, you know?

**Chris Gammell:** I guess I wouldn't have listed –

**Dave Jones:** And you can get on to more fun stuff.

**Chris Gammell:** I wouldn't have listed that as what –

**Dave Jones:** Right.

**Chris Gammell:** As the decision I want made for me, but yeah, I guess so. Top-down decision-making like – no, no. If I have a hand in it, that's fine. But if it's just handed to me like that, I don't know. Right. Yeah.

**Dave Jones:** And then sometimes if I know the project's going to fail, I go, excellent. I didn't make that decision. Somebody else made it and it's not going to be my fault. I know this project's going to fail and it won't be my fault. Yes, I can just sit back and watch the train wreck. You've got middle management written all over you.

**Chris Gammell:** Oh, yes, yes. We'll get someone around you right away, Peter. Oh, man.

**Dave Jones:** That's the only way I survived in companies like that was just watching the fun. It was just hilarious. It was living in Dilbert land and it was just – yeah. If you take things too seriously, you just get going.

**Chris Gammell:** Yeah, I agree with the taking things too seriously, but man, that's – that mental switch is tough, you know.

**Dave Jones:** Anyway, we're way over time, an hour and 20 minutes.

**Chris Gammell:** We have so much more to talk about, Dave. All right, well, fine. If people want to go find other links that we didn't talk about this week, they can check out reddit.com slash r slash theamphour, which is where we put links all week long and – That we never get to. Yeah, we try to get to, but we can't always get to. But, yeah, if you want to comment on things or add your own, please feel free and we try and get to them if we can.

**Dave Jones:** Oh, we didn't talk about the Sputnik schematic. I know. That's what I'm saying. Somebody found the Sputnik schematic. For your sake.

**Chris Gammell:** Let's just list off all the things we didn't talk about. The Sputnik schematic. Let's see what else. I had a follow-up from the Visa program from last week. It was only 65,000, the H-1Bs in the U.S., by the way. The Gene Machine, that IEEE article that you were talking about earlier? Yeah, yeah. Before the show. I guess that's it. Oh, and then that graphene crap where they said they'll charge your phone in five seconds. Yeah, right. I guess things to talk about next week or something. Right. No, next week we'll have a guest probably, but – Yeah, maybe. We'll see. Yeah. All right. All right. In the meantime, if people can give us iTunes ratings, that'd be great. And, you know, we can be found on the Twitters and the Facebooks and everywhere else, too.

**Dave Jones:** Yeah, but I don't read Facebook.

**Chris Gammell:** That's fine.

**Dave Jones:** All right, cool.

**Chris Gammell:** I hate it. Well, until then, I'll be on Facebook making fun of Dave.

**Dave Jones:** Cool. And I'll be behind the eight ball as usual.

**Chris Gammell:** All right. Good luck. See you next week. Sweet. Bye. This episode of The Amp Hour was brought to you by Triad Semiconductor. If you need maximum flexibility in both the analog and digital realm, check out the Via ASIC and associated Via Designer software. Visit viadesigner.com slash theamphour and enter AMP100 at registration for a free year subscription, a $500 value.

**Speaker ?:** administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered Take care.
