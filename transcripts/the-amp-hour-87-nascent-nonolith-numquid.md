---
episode: 87
title: An Interview with Ian Daniher - Nascent Nonolith Numquid
url: https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/
---

**Ian Danaher:** This is the Amp Hour Podcast, recorded on March 18th, 2012. Episode 87, with guest Ian Danaher, nascent nonalith numquid.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Chris Gammell's Analog Life.

**Ian Danaher:** And I'm Ian Danaher of Numble Flubs.

**Dave Jones:** Hey Ian, welcome to our humble podcast.

**Ian Danaher:** Why, thank you. I'm honored to be here.

**Dave Jones:** Excellent. And Chris, give us the background. Ian, you invited him on.

**Ian Danaher:** I was going to let him give his background. I'm kind of lazy here, Dave. I don't know who you've been talking to for the past couple of 86 episodes. But, well, Ian, please, though, take it away.

**Ian Danaher:** So, yeah, I am an electrical engineering student turned entrepreneur. I've been sort of mucking around the open education world since halfway through high school. And now I'm actually, I've co-founded a open source hardware educational startup. Which, I mean, kind of a recipe for disaster there because hardware and education are notoriously difficult to, you know, bootstrap with. But here we are. We're pulling it off.

**Ian Danaher:** That's pretty great. Fantastic. And so you're actually an entrepreneur in the actual term of it, not just someone who calls himself an entrepreneur.

**Dave Jones:** Oh, I was going to say, it's a dodgy term. That's a rough term. A lot of people, it's like the death term, you know, to call yourself an entrepreneur.

**Ian Danaher:** But I think I would actually refer to Ian as an entrepreneur. I mean...

**Ian Danaher:** I've pitched in front of VCs, but I do my own taxes. And so... All right. Yeah. That's about as close as you can get. Right.

**Ian Danaher:** That's good.

**Dave Jones:** So you have pitched this idea to VCs. It's that serious. You're that serious about it. Why the decision to do that instead of just bootstrapping and making and keeping it all yourself and making the money on your own?

**Ian Danaher:** So that's where we wound up. It's been a kind of fantastic learning process. We started out last June. Who's we, by the way? Oh, yeah. That's a good answer. Yeah.

**Ian Danaher:** Good question.

**Ian Danaher:** My co-founder, one of my best friends, Kevin Michal, I met him through Olin College. But we care about the same things and we have complementary skill sets. So we're going it alone. Together. Into space.

**Dave Jones:** Because you failed with the VCs? Yeah. Do tell.

**Ian Danaher:** All right. So this started out with an idea. We had played around with sort of the homebrew source measure unit that one of my professors at Olin had put together. And we liked it, but it was kind of shoddy around the edges. I'm pretty sure he's not a listener of the show. But he had built it. It'll find its way back. Don't worry.

**Ian Danaher:** It always does.

**Ian Danaher:** He had built it because he needed it and hadn't gone through to revise the design because, you know, he's busy managing projects for DARPA. And so Kevin and I were a big fan of it. It's a big fan of source measure units done cost effectively rather than sort of the 10 grand Keithley units.

**Ian Danaher:** Right. Which is the kind I've used before. And I do like them. But they are out of the reach of the normal consumer and definitely the student.

**Ian Danaher:** We're not going to take on Keithley. We're going to provide a different sort of tool for exploring the world.

**Dave Jones:** I was hoping you would say that we're not going to take on Keithley. We're going to bury them.

**Ian Danaher:** Sorry to disappoint there. No, I have ambitions, but they're not quite that long. Not right. So we went at it with a project description. We wanted to build a device that could source current, measure voltage, vice versa, and do it quickly and cheaply. And then we wanted to use it to, you know, charge cell phone batteries, figure out exactly what the capacity of those cheap Chinese LiPos is. Figure out what temperature light bulbs actually run at. And, of course, sort our junk bins.

**Ian Danaher:** Yeah, that's a good use. Actually, that plays near and dear to the hearts of our listeners. Yeah. What the heck do I have in my junk bin?

**Ian Danaher:** Oh, yeah. Well, you know, when you're actually sitting there with a hot plate pulling apart an old radio, half the parts on there don't even have part numbers on them. And so telling your three-pin temperature detector or your three-pin temperature sensor from your TO92 diode is nearly impossible. And so it works for that. You can use a multimeter for a quarter of it. You can use an oscilloscope and power supply for the rest. But I travel a lot and don't want to carry around a bunch of beige boxes with a bunch of knobs.

**Ian Danaher:** Yeah. And the ultimate goal is to eventually even make it curve traceable, right? I mean, that's kind of the ultimate goal.

**Ian Danaher:** Well, the ultimate goal is to make it do everything and do it well. Curve tracing is on the list. And actually, Chris, I don't know whether I sent you, but the screenshots of where I hacked together the Python script to throw together plots for the 2N3904. The just standard NPN diode that we shipped with all the Cs from our Kickstarter campaign. So, yeah, back to the situation at hand. We had an idea. We knew that it had a lot of potential for education because we'd both used sort of its inspiration to teach ourselves a lot more things than our professors were using it for. And so we got flown out to Palo Alto and played the game for a little bit, pitched for Imagine K12, a big education-themed firm. And it turns out they really aren't interested in hardware.

**Dave Jones:** So they actually flew you out, did they?

**Ian Danaher:** They flew us out, but after we presented, we pitched, they mulled it over. Our demo failed the first time around. Awesome. Yeah, no. Well, it turns out that you need to make sure that you have things cached that you thought you had cached. And, well, we pulled it off about, you know, a minute 30 through the five-minute pitch.

**Ian Danaher:** Oh, man.

**Ian Danaher:** So-

**Ian Danaher:** The panic mode button. Not quite the nick of time.

**Ian Danaher:** But, yeah, major props to that goes for Kevin there who pulled us out while I talked away at a mile a minute.

**Dave Jones:** Awesome. So just a quick question. How did you approach? Did you just look for VC companies on the web and then get their email and send them an email and say, hey, we've got this?

**Ian Danaher:** We knew what we wanted to do, which was a tool that would let you explore the world better. And for education, Imagine K-12 took the Y Combinator, the sort of big famous app model, and applied it to education. They each had their own personal fortunes from their days at Yahoo and wherever else they were. And they wanted to try and bring the same sort of team nimble approach to the education field. And so we were like, yeah, we don't really want to go down this path. We'll give it a shot. We wound up being flown out there. They decided they didn't want to give it a shot. And so we finally settled on Kickstarter because the real appeal of Kickstarter is you have an idea. It's a very well-defined idea. There's none of this ambiguous 7% stake in whatever you might do for the rest of your life.

**Ian Danaher:** So real quick on the Imagine K-12 too. So you guys were the only hardware there? I mean, what was the – We were – Yeah, that was app-based or actual –

**Ian Danaher:** Oh, yeah. We were the only hardware there probably by a mile. There were a lot of people with some kind of spectacular-looking iPad apps. There were some people working on better course management systems. But at least in our interview session, we were one of three. We were the only hardware. And they as much as said it in our email that we were the only hardware people who presented. Hmm.

**Dave Jones:** Cool. Well, that's – And sad at the same time. I was going to say this because everything's software because that's what everyone comes out of – That's what everyone has an idea for.

**Ian Danaher:** Software scales. It does. That's what they said to us. And it's cheap-ish. Software is cheap. It's cheap and you can make millions off of a couple of months' effort if it's the right couple of months.

**Dave Jones:** And you don't have to make anything. And making stuff's a pain in the ass.

**Ian Danaher:** Right. Yes. Oh, yeah. Sitting and figuring out why your loop is oscillating when it crosses two volts. Right. That's right. You didn't stabilize things. Yeah. Your phase is – oh, goodness. Yeah. It's hard.

**Ian Danaher:** You know, this kind of leads me to a rant I had this week. Like, so there was the South by Southwest Festival that, you know, they showcased a lot of apps and stuff like that. But they kind of took the software thing to an extreme and they had something called a startup bus.

**Ian Danaher:** Yeah. The startup bus I'm pretty sure was parked outside the concert I was at last night. I'm in Austin right now.

**Ian Danaher:** You're in Austin. That's right.

**Ian Danaher:** Not for South by, but, oh, yeah, I'm pretty sure they were there.

**Ian Danaher:** And, like, I love the idea of it. You know, I love the idea that it's, like, you know, entrepreneurship and, you know, that's a good thing, right? But, like, it's all, like, app development. And I first heard about it from this Ben Brown who wrote about it. And it just sounds really trite. I mean, like, it's, like, startups just to be a startup and, you know, like, all these apps are not useful at all. And it's – so I have to say, I mean, like, that's one thing. You know, I've been talking to Ian for a while now. But that's one thing that I've always – I'm always impressed with hardware startups because, I mean, aside from the fact that I like hardware, right?

**Dave Jones:** Yep.

**Ian Danaher:** Because there is – you know, there's a lot more to it. And you really have to be dedicated to it. You know, you can't put it together on a bus, right?

**Dave Jones:** And why do you have to call yourself a startup? Like, I'm here – like, I've been producing kits for 20 years, right, off and on. I've never called myself a freaking startup. I'm just making some kits, you know? Yeah, that's a long startup, Dave. Yeah, I don't know. It's just – sometimes I get sick of it. Oh, I'm an entrepreneur. I'm a – I'm going to form a startup. Well, just make your product. You don't have to call yourself anything. Right. Yeah. No, that's a good point. You're out there, make it, and sell it. That's it.

**Ian Danaher:** The thing is, it's a full-time endeavor. And when you're doing hardware, the costs for development, for making your product and doing it and selling it, are a lot more than they are for making your app and doing it.

**Dave Jones:** But that's why you can bootstrap. That's what bootstrapping is all about. If you can't afford, like, $1,000 to get a handful of first prototypes up and running, well, you know, I mean –

**Ian Danaher:** Dave, our first assembly run was five times that. I mean, just for people –

**Dave Jones:** Well, I'd say you're paying too much. No, no, seriously. Like, if you're doing – you know, why can't you produce five or ten boards, hand-assemble them, okay? Don't get them production assembled. Hand-assemble them. Then you sell those, and then you get bootstrapped. That's what it's all about. Seriously.

**Ian Danaher:** Dave, I have better things to be doing than sattering together production units. I own a Weller Iron and a $20 Amazon Hot Lids.

**Dave Jones:** Then you pay someone – I pay someone to hand-assemble my prototype boards and my low-production-run boards, and they do it for five or ten bucks a board. So let's talk about cost, then. What is the – It's pretty cheap. No, serious. You know, I'm being serious.

**Ian Danaher:** No, I mean, because maybe the bomb cost is higher for this thing. I mean –

**Dave Jones:** Well, that's the problem, right? Everyone thinks that they have to spend a shitload of money to get initial prototypes done. You don't. That's all I'm saying. No.

**Ian Danaher:** We've built a dozen of these things by hand. I sent – actually, Chris has one of them. Chris has the Revision 2 board complete with its own barge wire.

**Ian Danaher:** Mm-hmm.

**Ian Danaher:** Awesome. It's in his hands.

**Ian Danaher:** Actually, I have to send it back to him. I forgot about that.

**Speaker ?:** Yeah.

**Ian Danaher:** But no, we did this. We put them in the hands of people that would play with them and tell us what we were doing wrong. And it was awesome. But the thing is that doesn't scale at all. There's no way to make that jump except over the course of years from paying somebody $5 or $10 to put four parts on a single-sided board and selling hundreds of these things.

**Dave Jones:** I disagree. Sorry. Okay. I've sold – like I've sold many hundreds of kits where I've still had them hand-assembled by my guy in Melbourne at $8 a board or something. Cool. So, you know, and you can produce hundreds of items and it costs you zero in terms of setup. Like I've been trying to get this latest product actually machine-assembled. It's taken me months and months and I've got nowhere already. It's a pain in the ass actually. Yeah. It's just so slow a process. I could have sent them to my hand-assembler and I would have had them done two months ago.

**Ian Danaher:** Well, we did this great house up in Bellevue, Washington we can hook you up with.

**Dave Jones:** No, I'm trying to keep everything local. Thanks. Ah, there it is. Australian, you know. There's my problem.

**Ian Danaher:** Well, maybe there was something to that then about the hand-assembling, the small run capacity. There is.

**Dave Jones:** It's easy. Quick.

**Ian Danaher:** Yeah, exactly. Exactly. I mean –

**Dave Jones:** There's no setup. You don't have to get a paste stencil. You don't have to wait for the machine to be available.

**Ian Danaher:** But you also can't design in 0402s and 0201 kind of things, right?

**Dave Jones:** No, they pay you a hell of a – they charge you a hell of a lot more to hand-assemble 0402s because they have to do it under the microscope. Yeah.

**Ian Danaher:** I'd believe that in a heartbeat. But I do know that we had less than a two-week turnaround between when we drop-shipped the parts to our assembly house and shipped them the boards after hand-inspecting all of them. And it was two weeks until we had a big box of boards, and that was with a snowstorm.

**Dave Jones:** Oh, yeah. Yeah, that's not surprising at all. Yeah, I've just got a supplier who's just dicking me around. That's all. Oh. An assembler who's dicking me around.

**Ian Danaher:** Oh, Australians, you know. You can't do business with them, right?

**Ian Danaher:** Well, no. It's certainly quick and easy. There are different options. Yeah. I mean, they keep it –

**Dave Jones:** But we've talked about this on the show before, Chris. We've – you know, what is the best option to go for the Kickstarter, get all the money up front, and then do it, or do the bootstrapping, the small-scale bootstrapping thing? Well, let's ask the Kickstarter guy.

**Ian Danaher:** So Ian's done a Kickstarter campaign. And what was the final funding, Ian?

**Ian Danaher:** It was $20,940.

**Ian Danaher:** Wow. Okay.

**Ian Danaher:** That was the – we were shooting for six. So actually, Dave, we did the math, and it would have come out to $6,000 for the first run of however many boards we had originally shooted to produce. But we wound up making the Hackaday, the Adafruit, the Dangerous Prototypes blog circuit, got some traffic from there, and then the educational crowd with which I know, they were super interested, and they have been. And we wound up tripling our goal.

**Ian Danaher:** Yeah. Yeah.

**Ian Danaher:** Awesome. And at that point in time, we just said, oh, well, what now? I wound up taking a leave of absence from Olin College. And then shortly thereafter, my friend Kevin did the same. And we were full-time on development prototyping. And after having started with a mock – or started the Kickstarter with an early proof of concept and a UI mock-up and a render of our pre-beta board and taking it all the way through a couple hundred unit production run and shipping them to customers and dealing with the unhappy people who haven't figured out how to compile the software or download it or the happy people who are just ecstatic that they're now able to figure out more about the way the world works in a way they couldn't before. It's been a spectacular six months. And I – well, six, eight, nine months now.

**Ian Danaher:** See, and he's learning sales too. You heard the end of that. That turned right into a sales pitch. Did you hear that, Dave? That's the thing I heard. That was good. That was good.

**Dave Jones:** There's two advantages to Kickstarter as I see it. One is A, you get the money up front so that you can actually go out and produce a large number off the bat.

**Ian Danaher:** Yeah.

**Dave Jones:** And B is the advertising and promotion aspect because Kickstarter is, you know, flavor of the month. And there's people on there who just, you know, search Kickstarter every day. Oh, what's the latest project? Oh, I love this. And all, you know, and it's just – Yeah.

**Ian Danaher:** Look at any Apple-themed iPhone peripheral on Kickstarter. They all wind up walking away with $80,000, $100,000, $200,000.

**Ian Danaher:** I think one of them hit the million, didn't it? Didn't one of those? Yeah.

**Dave Jones:** That was the watch band. That was the – The TikTok watch band. The TikTok watch band, which I've got one of those, yeah. Yeah.

**Ian Danaher:** Well. You should have said – I mean, you should have just said this was a way to interact with an iPhone. I mean, you just marketed it all wrong.

**Ian Danaher:** Yeah, you did it wrong. Well, we'll make that mistake again. We'll make that mistake again.

**Ian Danaher:** You should have said something like – Learned our lesson.

**Dave Jones:** Here's an extra board that can control your SMU from your iPhone.

**Ian Danaher:** Oh, yeah. You would have broken through that goal even faster.

**Ian Danaher:** But developing for Apple is not high on our to-do list, let me tell you the truth. Yeah. Developing hardware for Apple.

**Ian Danaher:** Right.

**Ian Danaher:** I think you need to incorporate what the $3 chip that just has the public key on there.

**Dave Jones:** Really?

**Ian Danaher:** Oh, yeah. They have some sort of cryptographic signing of their hardware peripherals.

**Dave Jones:** Oh, really?

**Ian Danaher:** Yes. Okay. I probably horribly bungled that, but you get the idea. Right. Some kind of cost, basically, yeah. Yeah.

**Dave Jones:** I didn't know it was like that. I thought you could just stick a device on there. Oh, no. Oh, okay. This is Apple we're talking about here.

**Ian Danaher:** Right. Well, I was hopeful. Right. I respect them a lot. And in fact, I'm talking to you guys now on my MacBook Air. But no, they make it a pain for their developers.

**Ian Danaher:** So what about the Kickstarter process? I mean, I'm curious about this because I'm sure some of our listeners would be as well. I mean, was there really any hassle to it or was it just kind of a percentage off the top at the end and dump all the money in an account?

**Ian Danaher:** So here's how it went. We put together an application. We sent in the application. We were accepted. A month later, we had finished our render and our cutesy little promo video.

**Ian Danaher:** Which is key, by the way. People should know that.

**Ian Danaher:** Oh, the video was tough. Yeah, the video was huge. I did the audio. Kevin's brother, Brian, did the render and Kevin did the video. It was a team project right there. Yeah. But once with the video, the couple of paragraph write-up, we just sort of hit the go button, ran it for 30 days. And 30 days later, after it hitting Hackaday and whatnot, we collected our $20,000 minus the Kickstarter 5% minus the Amazon 4%.

**Dave Jones:** Oh, what's the Amazon 4%? What's that?

**Ian Danaher:** So Amazon is the payment processor.

**Dave Jones:** Oh.

**Ian Danaher:** Everybody wants a piece. Exactly. Exactly. But Amazon was the crew that collected the credit card numbers. And Kickstarter really couldn't work without that big name behind. Well, I suspect that people would be a lot more nervous giving their credit card information to Joe's Fund It Yourself crew versus Kickstarter backed with Amazon. Right.

**Dave Jones:** Yeah. Right. But that's 9% off the bat.

**Ian Danaher:** Yeah. Oh, no. They have a spectacular business model. You win, they win more. Yeah. Because that's 9% off the top for providing service and PR.

**Ian Danaher:** Yeah.

**Ian Danaher:** This is essentially what it comes down to. And when you have, what, in the past month, we've had three projects break a million dollars.

**Ian Danaher:** Oh, yeah. Some passed two or three million now. But those are software projects, game projects. Yeah.

**Dave Jones:** That's some sweet commission there.

**Ian Danaher:** Yeah, right.

**Ian Danaher:** Oh, absolutely. No, the Kickstarter guys, they must just be, you know, high fives in the hallway.

**Dave Jones:** Sitting on a chair, a throne of cash.

**Ian Danaher:** Yeah. As Chris calls it. Throne of cash, smoking cigars. Yeah, absolutely.

**Ian Danaher:** $100 bill laid-ups, right? Yeah.

**Ian Danaher:** Well, no, their team has managed to do something awesome, which is really empower people like me to do things that they want to do while making money off the top.

**Ian Danaher:** Yeah.

**Dave Jones:** Can I make a clarification to that? They empower Americans only. That is a good point. Yeah. Oh, yeah. And it's freaking annoying. Other than other options, right there. It is ridiculous. In today's global economy, it is absolutely ridiculous to limit it just to Americans.

**Ian Danaher:** I'm pretty sure that's an Amazon payment processing stipulation.

**Dave Jones:** And there's the problem. There's your problem right there. The Amazon, yeah.

**Ian Danaher:** If you look at people like, I guess, Indiegogo is one of the other big competitors. They bluntly aren't, they don't have the same audience. They don't have the same numbers. They don't have the same crowds. You don't get as many high-profile projects.

**Dave Jones:** But the thing is, I find, like, I didn't even know Amazon were connected to Kickstarter. So it doesn't really matter who they use. I'm not going to go, oh, I'm going to use Kickstarter because they're affiliated with Amazon.

**Ian Danaher:** Well, so here's the counterpoint. My grandpa backed me and a couple of his friends who I had met, they're all retired, like, government engineers. Back from 50s and 60s, my grandpa still reads funding grant applications recreationally. Whoa. Yeah, my grandpa's pretty awesome. But his friends would not have backed us if we didn't have a name that they recognized there. They have been raised with the internet as that unknown place full of creeps and rip-offs. Right. And you don't want to just walk around handing out your credit card information. I mean, every six...

**Dave Jones:** See, I know few people who are paranoid like that anymore. It's just not an issue. Yeah, it's not an issue anymore as far as I'm concerned.

**Ian Danaher:** Dave needs to call his grandparents more often.

**Ian Danaher:** But that's the thing is, we're not another hot iPhone peripheral. We wanted to make high-level concepts accessible to people with a computer. You don't need the beige box with 60 buttons anymore. You need a web browser and a USB port. So, if we were... So, actually, yeah, here's an example. RepRap. One of the... I believe it was Dr. Adrian Boyer himself. Bowyer. I probably... Mess his name up there, too. But they ran an Indiegogo campaign to get a bunch of their Huxley kits made. They did fine. I mean, their audience was familiar with Indiegogo. It was indie. And they weren't going for the whole mass appeal. They were going pretty much strictly for people who were okay sitting there for a weekend bolting together stuff.

**Ian Danaher:** Right. Yeah. And they probably had people already coming in from outside sources as opposed to people that were already sitting on Kickstarter looking for new projects to fund and that kind of thing. Yeah. Yeah.

**Ian Danaher:** The sort of engineers who were okay screwing kits together, they weren't our target audience. We didn't offer a solder-your-own-see-together kit. We offered bare PCBs just for sort of a token thanks for your $20. Or we offered assembled PCBs for people who wanted to save some money and save us some hassle. And then we offered the final unit with the laboriously hand-assembled, cut acrylic, aluminum washers. You get the idea. Rubber feet. With a whole getting started kit with a whole $2 of components and nice jumper wires. Scores! Yeah, I know. Scores, yeah. So, you know, we weren't going for the kit makers. And, you know, I guess that's why we call ourselves a startup rather than a couple of guys selling kits because we're not selling kits.

**Dave Jones:** Right.

**Ian Danaher:** So, Dave, when you make that transition, you'll finally be a startup there, Dave, right? As soon as you sell the final USB power supply or whatever it is, the battery power supply.

**Dave Jones:** I just don't like the term. I know. It's just too overused, I think. Yeah.

**Ian Danaher:** Oh, it's absolutely. So, yeah, it's absolutely overused. Having run a little bit in that circle, I mean, being flown out of Palo Alto, going to a hot tech college right next to a hot business college. I mean, everybody wants to start a startup and write an app. And everybody wants to get rich quick.

**Dave Jones:** Right.

**Ian Danaher:** Yep.

**Dave Jones:** Yep.

**Ian Danaher:** And startup has been romanticized as a way to get rich quick.

**Dave Jones:** Yep.

**Ian Danaher:** I mean, we had a web bubble in the late 90s, early noughts. We kind of have another one now, an app bubble, if you will.

**Ian Danaher:** Yeah. Possibly. So, a couple more years until the hardware bubble or is that 30 years past us?

**Dave Jones:** No, because it'll never be a bubble because you've got something tangible.

**Ian Danaher:** Exactly. It doesn't, you know. I don't know. I would like to think that with companies, well, we now have Hackcelerator, a startup accelerator, build as such, where they want to fund hardware companies. They want to give hardware companies $15,000 to $20,000 to come spend some time in China and work from their idea to a mass production run in a couple of months.

**Ian Danaher:** Yep. We've mentioned them on here a couple times. Yep.

**Ian Danaher:** We were actually, we applied, we were accepted. We wound up turning them down because, you know, we have customers and we need to be in the same time zone as them.

**Dave Jones:** Yep.

**Ian Danaher:** But I would like to think that there's now going to be a backlash to the trivial get-rich-quick startup feel. And we're going to see more people doing hardware, more people doing things that matter, taking on hard problems with technically non-trivial solutions. That would make me happy.

**Dave Jones:** One of the big differences between a hardware and software startups in this case is that software, you write your app, right? It takes you a month to write your little app and you get rich instantly. But anyone else can come along in that same month who's smarter than you and write a better app and instantly wipe out your market overnight. That's the problem. Yeah, sure. Whereas hardware is different. You know, you spent six months, 12 months developing this product. It's, you know, someone's not going to come along easily and knock you off your perch.

**Ian Danaher:** Except for the fact that all our designs are on GitHub. Oh, well, that's the open source hardware side of things.

**Dave Jones:** Well, that's the open source hardware thing, isn't it? Yes, that's the point. Anyone can take your files and go and compete directly against you. They shouldn't because that's one of the unwritten rules of open source hardware is you don't do that. We got that all the time. You're a douche if you do that. You're legally allowed to do it.

**Ian Danaher:** Talking to VCs, everybody wants to know how we're protecting ourselves, where's our IP. Well, that's why we're not playing the game at nearly as much as we, you know, we did it. We were curious and we found out that we don't like it.

**Ian Danaher:** Yeah, that's...

**Ian Danaher:** I mean, personally, we have a lot of... The way that it's done right now is it's all about owning something. It's all about monetizing something. It's all about screwing over your users to make a dollar. I'm just going to be blunt and wrong there. There are a lot of exceptions to that.

**Ian Danaher:** Of course.

**Ian Danaher:** But when it comes to pitching anything open to anyone who wants to give you money to take it further, there's the risk of people ripping you off and walking away with your freshly acquired $2 million of VC funding is too big for a lot of the old hats and the old crew, old guard to play.

**Dave Jones:** Yep.

**Ian Danaher:** So, you know, that's all right. To be honest, our designs are under a Creative Commons non-commercial license. So you actually have to talk...

**Speaker ?:** Oh, non-com...

**Dave Jones:** Ah, so you're not allowed to call it open source hardware then? No, you're not is the answer.

**Ian Danaher:** That's okay. He's right because he went on about this for hours.

**Dave Jones:** Yeah, you are not allowed... If it uses the non-commercial license, you are not allowed to call it open source hardware. I'm serious. That is one of the rules.

**Ian Danaher:** Interesting. Yep. Well, we changed it when we were talking to people who wanted to give us money to put our devices in schools. We can probably change it back. All right. You know, but we're... I've had people look at our schematics and build versions of the C just because we had a nice reference design for the ATX mega chip. Yeah. I am happy with the extent to which we're playing by the rules and I feel that by playing by the rules to the extent we have, we've made the world a better place. So...

**Dave Jones:** Yeah.

**Ian Danaher:** And we should...

**Dave Jones:** But if you're calling it open source hardware, if you're using the logo or something like that, then you're not playing with the rules. Okay. Interesting. Because no, seriously, it must be non-commercial license. It must... You must not be able to use the non-commercial license. Must not be... So please stop. If you are doing that, if you're using the open source hardware logo, you will get frowned upon in the industry and your name will be mud. Well, thank you for the warning.

**Ian Danaher:** One thing we should mention, too, about that specific device is the... I mean, there are a couple other layers there, too. I mean, it's not just straight hardware, right? So it's not...

**Dave Jones:** Oh, yeah.

**Ian Danaher:** There are no...

**Dave Jones:** Hardware and software, yeah.

**Ian Danaher:** Right. So what I'm saying is from an IP perspective, I mean, there are... And that's really how you do it in open source hardware, I think, is that you have more layers in terms of firmware, in terms of software in this case, you know, and that actually... Yeah. That becomes another part of your competitive advantage, right? You can... You don't necessarily need to, like, lock it all down, right? But...

**Ian Danaher:** Yeah. Well, our software is all GPL. We're all under GPL v3. It is what it is, and we will take that under advisement.

**Ian Danaher:** Another startup term.

**Dave Jones:** Right. Take it under advisement. Yeah. Well, I don't see anywhere on your website that you're actually using the open source hardware logo.

**Ian Danaher:** We have the gear on our circuit board.

**Dave Jones:** Oh, you do? We do. We do. No, yeah. Seriously, you're not playing by the rules at all. Go to the open source hardware group, and they specifically mention you must not choose the non-commercial license. Oh, all right. Otherwise, you are to remove the symbol from your board. So, bit of friendly advice there. Yes. Yes. If people find out, they will... Yes. You will not be popular.

**Ian Danaher:** Interesting. Yeah. Well, we've had a lot of people, you know, hack our software. We actually have a patch in our publicly distributed code that slightly modifies the user interface. So, which...

**Dave Jones:** Yeah. I mean, your design is open. You're just not allowed to call it open source hardware. Yeah. Well, that's just... And use the logo. You can call it open. It's an open design, all that sort of stuff. But, yeah. Yeah. All right. Well, in the next batch of boards... The industry has decided that those are the rules, you know.

**Ian Danaher:** Well, in the next batch of boards I ship out, I'll make sure to sit there with a piece of sandpaper. Yeah, some acetone. And rub them off. Excellent.

**Dave Jones:** Thank you. Because, see, a lot of people don't notice this sort of thing. They don't notice these small details, but it's a very important thing. So, it's a very important part of the ethos of open source hardware is that it must... There's no exceptions. You must be completely free and open, which means people are allowed to compete with you.

**Ian Danaher:** Which is what Dave is really saying is he got yelled at for this after fighting the point for a while. And now he's finally come around. That's what he's really trying to say.

**Dave Jones:** I finally... Well, yeah. I mean, no. See, I'm in agreement with Ian here that, you know, you can release a product that's open and everything else. And you can use the non-commercial license. And I'm fine with that. I see advantages to some people who, you know, if they want to get venture capital or something like that, they might have to do that. But using the open source hardware logo, I now agree that you shouldn't do that unless you are non-commercial.

**Ian Danaher:** So, we've had that logo on there since before it was public. I mean, since before the logo was decided on. We just... We left it on there.

**Dave Jones:** Because nobody noticed, see? Because I don't see anywhere on your site where you're putting the license that you actually... Where it says non-commercial under there.

**Ian Danaher:** It's... I mean...

**Dave Jones:** It's buried away, obviously, somewhere, right?

**Ian Danaher:** I mean, go to GitHub. It's under... Yeah. Okay. I mean, everything is in GitHub. GitHub, where licensing belongs, and where source belongs. All schematics and board layouts for this project are on a create.

**Speaker ?:** Oh, yeah, there it is.

**Dave Jones:** Creative Commons, B-Y-N-C-S-A. Yes. Yep. Yep. That's right. So, wah... Sorry. Please remove the scene. Wah. Wah.

**Speaker ?:** Thank you very much.

**Ian Danaher:** So, I had a question in terms of some recent news. We had been talking about... We had talked on the show before about the JOBS Act, which is a piece of U.S. legislation that opens up the startup, whatever marketplace you want to call it. Basically, now startups can be funded by up to 100 people at $10,000 a pop, and they can get a piece of equity in the company. You can actually, you know, say it's actually like a small share stock ownership. So, this is a government thing. Yeah. Well, this is a change in regulation in the U.S. Right. Yeah. And so, my question is, is it better... Is that kind of thing better, or is the Kickstarter model better, or is none of those better? I mean, maybe it's something else kind of thing. I mean...

**Dave Jones:** Tell me the details about this jobs thing again. What do you... Who can put money in? How much do you have to give up equity in your company?

**Ian Danaher:** So, interestingly, in the U.S. for the past however many... Since like the 30s, I believe, in order to invest in a company, you either had to be a family member, or you had to have... In order to be an angel investor, you have to have $1 million net worth, not including your house. Oh, really? Okay. As far as I know. And that... That's bizarre. Don't quote me on that one. But I'm pretty sure that's what it is. And what they're basically saying now is they're extending the terms in startups. So, before, it was like when you got to 500 investors in startups, even angels, I believe, you had to... Gary Publix. Yeah. At least change your registration with the SEC, which is a regulatory body. Now, that's 1,000. You know, you can get certain amounts of funding now. So, basically, the whole idea behind this is... Well, the whole behind the idea is it's an election year. That's the main thing. But the thing that I'm excited about it is that any small startup can get up to a million dollars in funding in $10,000 increments from small investors. So, you and me, you know, anyone not worth a million dollars, because I'm definitely not worth a million dollars, I could invest $10,000 into Ian's startup if he was taking money. And then I could get some portion of, you know, whatever the terms are in terms of stock ownership. Oh, right.

**Dave Jones:** So, the company can determine what amount you give away for your $10,000. I believe so, yeah. Right. Okay. Cool.

**Ian Danaher:** If that was the case, I could have sold a share to my dad for his parental 2% in exchange for backing the Kickstarter campaign. Right. But I... Without Kevin here, we would not have gone that route. You're saying if Kevin was there, you would have... That gets ugly, right? That gets ugly.

**Dave Jones:** That gets really ugly, because then what, you, they have to get a percentage of your royalties right up front. Oh, yeah. Like, how does... That just gets messy. It sounds messy. You spend half your business time just, you know, playing with the finances and crap. Yes. Oh, man. Well, right now...

**Ian Danaher:** Because we're in... Oh, go ahead. Yeah. Right now, we're in LLC, and I'm almost positive that the JOBS Act won't let you play by LLC rules and take... And sell stock.

**Ian Danaher:** Right. Yeah. Usually, you have to go to an S-Corp or C-Corp to do that kind of stuff.

**Ian Danaher:** Exactly. And that makes... That greatly increases your amount of paperwork. Oh, yeah. Yes, definitely.

**Dave Jones:** That's like here, I guess, and LLC is similar to my sole trader here. I'm a sole trader. I am not a proprietary limited company, which is another step in paperwork and liability and all that sort of stuff. Yeah. Exactly.

**Ian Danaher:** So, an LLC is a limited liability company. My understanding of the term is that...

**Dave Jones:** Oh, okay.

**Ian Danaher:** Is that we're...

**Dave Jones:** Well, no. That's where... That's where I'm a sole trader. I have full liability at the moment. So, yeah, you're a sole proprietorship. Because it's all on my personal income tax. Yeah. I would have to... If I want limited liability, I have to step up to... A proprietary limited company, what it's called here. Gotcha. So, yeah.

**Ian Danaher:** Well, we're... Yeah, the company Nunnall Collapse, the tax pass-through for Ian Danaher and Kevin Michal. Yeah. And, well... Yep.

**Dave Jones:** Well, if there's two people involved, you automatically have to form a company. You can't do it as a sole trader here.

**Ian Danaher:** Okay. Yeah, you can actually do partnerships in the States.

**Dave Jones:** Oh, yeah. You can do partnerships here, too. But I think very few people do that as an option.

**Ian Danaher:** Yes, that is my understanding as well.

**Ian Danaher:** Anyways, the thing that excites me about the Jobs Act is that I think it's a bunch of cash into startups. And I think it's going to be a good thing personally. But I was just wondering if that was available, if you guys would have taken that kind of thing. Or if Kickstarter still would have been the way to go.

**Ian Danaher:** I think Kickstarter would have been the right guy. Kickstarter is great. With Kickstarter, you're responsible for clearly communicating your expectations. And you're responsible for endeavoring to meet those until you deliver products to people's hands.

**Dave Jones:** That's probably the only disadvantage of Kickstarter is that you have to produce. You've taken people's money up front. And you're going to have people emailing you, right? Disadvantage. Where's my kid? You know, that's the disadvantage.

**Ian Danaher:** I love it. We had all our development.

**Ian Danaher:** He wants your emails, people. Just send them an email. Say, where's my kid? Even if you didn't order one.

**Ian Danaher:** Yeah. He loves it. No, I genuinely like talking to our customers. And we only had one person say, hey, what's going on? The people that are kind of alpha geek will follow us on GitHub. The people that are socialites will follow us on Twitter. If they want to know exactly what the status of their product is, they can see how many hundreds of commits we've pushed in the past month. And then they'll be happy. I mean, we took a very straight-up transparent development cycle here, and it made people happy.

**Dave Jones:** There's a lot of horror stories, though. You hear people, oh, I just got hassled every day from hundreds of people.

**Ian Danaher:** There was one recently about a dicey drone project, actually. DIY drones. Yeah.

**Ian Danaher:** Oh, right. Well, not affiliated with the organization, but yes, a DIY drones project.

**Ian Danaher:** Right.

**Ian Danaher:** Where the people responsible had unmet obligations in their personal business and were trying to just skip out and start a Kickstarter campaign. Jeez, I didn't hear that part.

**Ian Danaher:** I knew that they promised all this stuff that wasn't really plausible either. That's what ended up canceling it, right? Yeah. Right. Because Kickstarter is centrally vetted. The people vetted at the Kickstarter headquarters. And that would just slip through and they canceled it later. Yep.

**Dave Jones:** Well, because it would be very technical. So unless they know about the business, that particular drone business or electronics or whatever it is, they can't know if something's truly feasible or not.

**Ian Danaher:** That's true, yeah. Unless they have in-house experts.

**Dave Jones:** But that's what the community is for. There were these glasses, right? There were these, didn't we talk about it on the show? Yeah, I remember those. There were these recording glasses and I just called bullshit straight away. There's no way you can produce something, electronics and HD video and recording and battery and everything that small. Not for the price they wanted. To fit in those glasses for that price. Right. You know, it was just not going to happen. And of course it didn't. So, yeah.

**Ian Danaher:** Well, I'm, yeah, there's a project right now, the Ivy Voltmeter or something.

**Dave Jones:** Yes.

**Ian Danaher:** That I'm personally a little skeptical about. Oh. I would love to see them deliver.

**Ian Danaher:** Yeah.

**Dave Jones:** Okay, what's it called?

**Ian Danaher:** It's a Bluetooth Kickstarter. It's a Kickstarter project. It's a Bluetooth DVM. It's like three and a half digits.

**Dave Jones:** Oh, okay.

**Ian Danaher:** They're trying to get to like $65,000. It looks, I'm not very impressed.

**Ian Danaher:** They're going for $65,000 and they're going to sell them through the Kickstarter campaign for $40 plus shipping.

**Ian Danaher:** Yeah.

**Ian Danaher:** Check it out. If the guy, his previous claim to fame was, he produced a keyboard organizer, a flip up keyboard.

**Ian Danaher:** Yeah. Yep.

**Ian Danaher:** And, you know, actually there's a lot of DFM that went in, designed for manufacturer that went into that. He probably has a lot of the right skills. Okay. The price point just has me a little, well, I'm not going to go on record.

**Dave Jones:** Oh, okay. It's the iVolt meter. Right.

**Ian Danaher:** Yep.

**Dave Jones:** Oh, I see it now. Yeah. And what are those contacts on the end of it? I feel like these weird looking.

**Ian Danaher:** It's a bad render.

**Dave Jones:** No, they're actually banana plugs. Okay.

**Ian Danaher:** I mean, they're showing banana plugs plugging in, but I mean, I think it's just a bad render. Right. Okay. Yeah.

**Dave Jones:** And they reckon they can produce this for 40 bucks, do they? Is that the... Yep. Yep. Okay. Well, we will see. But yeah, that's kind of the thing. Eventually it's a... Well, it's got to retail for 60 bucks. That's what they say.

**Ian Danaher:** 65, I think. Yeah.

**Dave Jones:** With five bucks shipping. Okay.

**Ian Danaher:** Yep. It'll be interesting to watch them because, you know, I would very much like a $65 Bluetooth bolt meter.

**Dave Jones:** Well, there's not much hardware in that.

**Ian Danaher:** No, there's not. You can probably...

**Ian Danaher:** An amp, a Bluetooth chip, and maybe a microphone.

**Dave Jones:** As long as you can get that. Well, there's a custom LCD there.

**Ian Danaher:** There's a custom... So there's a custom plastic...

**Dave Jones:** Plastic enclosure. Yeah.

**Ian Danaher:** Yeah. And that's going to have to be custom injection molded. But on top of that, you have... The way cheap Chinese volt meters work is they are all ASIC based. You have a epoxy blob in there with some supporting passives.

**Dave Jones:** That's how they can sell it for five bucks. Right. Exactly.

**Ian Danaher:** And that's kind of the direction that I think he's using to rationalize his price point.

**Dave Jones:** Oh.

**Ian Danaher:** And I'm going to be really uneasy seeing that ASIC... Or seeing an ASIC integrated with Bluetooth and an external micro at the scale that he's going to be producing is that.

**Dave Jones:** Yeah. That's a huge risk. Yeah. I don't like it.

**Ian Danaher:** Yeah.

**Dave Jones:** Anyway, that's... Speaking of the case, actually, I was going to ask you your C design. Okay. Tell us about the case because you've just got like a base. Like, is it a metal base?

**Ian Danaher:** All right. So what the case is...

**Dave Jones:** Is it a metal base with a clear heart? If people haven't seen it, we'll put up a link or a photo. But it's a clear... It's like a transparent, flat, clear top on it. It looks like acrylic, right? I mean... It's acrylic, right? It is acrylic.

**Ian Danaher:** That's what I was after. What it is, is we actually contracted with a local bio company. By the way, the whole C was made in the United States, made and assembled in the States.

**Dave Jones:** Awesome.

**Ian Danaher:** Outside of chips and board. But everything else was local. There was a company up four and a half hours north of me that did all the laser cutting and screen printing for us. And then there's a picture... I'll have to send it to you guys. There's a picture of Kevin and I sitting down with a thousand rubber feet. We were... We hand inserted a 5-16th inch bolt into a rubber foot. And we did this a thousand times. Oh, yeah. Feel the same, huh? On top of that, we threaded, you know, eight or ten thousand bolts onto screws. Because the actual stack for the C, it's a rubber foot with a bolt in it. A piece of laser cut acrylic. A nut to hold everything together and stand off. The actual C circuit board. And then a 5-16th inch aluminum spacer that elevates the top pretty printed acrylic above our circuit board. So, it's a great design and...

**Dave Jones:** Did you find that was cheaper, though? It was a cheaper solution? Cheaper than what? Than an off-the-shelf case. Oh. Say, for example. Like a baseball. An office. Yeah.

**Ian Danaher:** With a button on it. We could have gone that route, but, you know, part of the difference between doing the whole kit thing and the startup thing is we wanted... We had a look and we had a durability. And I can actually stand on my C. And I've used... I've done chemistry with it. And it survived dilute solutions of hydrochloric acid floating around. And it's a pretty durable design. It's not sealed on every side, but it is mechanically resistant and splash-proof. I like it.

**Speaker ?:** Cool.

**Dave Jones:** My latest project, actually, which nobody's seen yet, it's actually going to use a similar approach, but I'm actually using an off-the-shelf or half of an off-the-shelf case as the bottom. And then I'm putting the clear acrylic on top of that. So it's just a square cut piece of acrylic. And then I use the existing mounting holes in the case to mount the actual clear cover on it. And then the circuit board goes inside that. That's awesome. And then I halve my cost because I'm using an off-the-shelf case and it actually comes in two symmetrical halves. There you go. So you actually get two for the price of one. So you just open it up rather than using the one case because I need to see through to an LCD.

**Ian Danaher:** So that's why I need the clear case, you see.

**Dave Jones:** And then you don't have to cut out any windows or anything like that. So you're saving manufacturing costs there and stuff like that. So yeah, I do like the projects with the clear acrylic top on them. They're really groovy.

**Ian Danaher:** Plus you get the blinky light kind of look to it. And you can get light through.

**Dave Jones:** Yeah. And you don't have to meet up mounting holes. And they're cheap, right? To get a laser cut piece of acrylic is pretty darn cheap and easy.

**Ian Danaher:** So what I did is I actually exported the silkscreen layer from our board into a high-res PNG. I uploaded it to Flickr and then I went ahead and annotated every part on the board. So you can go online right now and look at a line drawing of our circuit board. I've seen that. And get a description of what every part on there does. And that's a level of detail that we think sort of adds to the overall experience. I mean, you want to learn a little bit about op amps, you can learn a little bit about op amps or email us to learn more. Oh, careful with that one, buddy. Oh, yeah, I know. Chris, just go ahead and edit that one out. Yeah, right. Yeah, I'm sure I'll do that.

**Dave Jones:** I noticed that you're using the microchip MCP4922 DAC on there.

**Ian Danaher:** So Kevin was actually in town in my hometown of Cincinnati when we were bolting these together and we were listening to the Amp Hour. And we just kind of looked at each other and laughed when you started railing against that.

**Dave Jones:** Because it's not that great a DAC. It's pretty dodgy. Have you seen that yet? I actually measured it. And, yeah, it wasn't that great.

**Ian Danaher:** Okay.

**Dave Jones:** So.

**Ian Danaher:** We've actually been fairly pleased. The linearity meets spec. I mean, we're only operating at about 1%.

**Dave Jones:** Yeah, spec is a bit loose, though. Yeah. That's the issue. So you know what you're getting if you believe the spec, you know. Okay. But it certainly doesn't perform much better than spec. Let's put it that way.

**Ian Danaher:** But it is, it met the need we needed, or it did what we wanted. And it has continued to do what we wanted reliably. So it's a good part for the job. We've been tossing around a couple of ideas for our next version. There's actually an internal DAC in the XMega. One of the questions I've gotten a couple of times is, why didn't you use the internal DAC? And it turns out that if you pay close attention to the Atmel data sheet, there's a 41 millivolt offset in that DAC. And so kiss your ground rail goodbye. Yep.

**Dave Jones:** Trap for young players.

**Ian Danaher:** Indeed. I mean, this chip is a lot better than the last XMega 32A4, where it was like a 410 millivolt offset. Oh, wow. Jeez.

**Dave Jones:** Yeah, you can fly to the moon on 410.

**Ian Danaher:** It's just other stuff on that chip. I mean, it wasn't like, it's not like a DAC micro, right? I mean, it's just a throw it in kind of thing.

**Ian Danaher:** It's just a, yeah. It's so, I have to rant and rave about how much I love the XMega chip on here.

**Ian Danaher:** And before you do, I should mention, I actually had this on the list as the chip of the week at one point. So we can, we can first call this the chip of the week, because this is what I, based on Ian's suggestion, this is what I'm designing into the board I'm working on too. So.

**Ian Danaher:** All right. Chip of the week right here. The ATX Mega 32A4U. It has full speed USB, a bunch of 12-bit ADCs, a pair of 12-bit DACs, and it's actually. Which are crap.

**Ian Danaher:** Which are crap, yeah.

**Ian Danaher:** Which are crap, yep. Crap. But, you know, if you needed to. Anyway. They're crap. So. And it has a bunch of glorious pulse width modulation and functionality. More timers than you know what to do with. I really like it. I have been pleased using it. It has made using it a pleasure. So what more do you want from a chip?

**Ian Danaher:** Well, easy enough for an idiot like me to put it on a board. That helps too. Yeah. So, yeah. I mean, I like the specs as well. It's got 4-bit INL, I think. So it's pretty decent ADCs. So.

**Dave Jones:** Yeah. Yeah, it's not hard to get a good analog-to-digital converter inside a micro, but it is hard to get a good DAC.

**Ian Danaher:** It's hard to get a good analog-to-digital converter at low-cost outset of a micro. That's what we found.

**Dave Jones:** Yep.

**Ian Danaher:** For some reason, the ADC inside the XMega is cheaper than an ADC costing twice as much as the XMega itself.

**Dave Jones:** Yes. I know. It's crazy. It's.

**Ian Danaher:** I guess there's just a lot of inherent cost in the CMOS fab. That's all Kevin and I could come up with was just that once you're actually building or once you're doing photolithography to build your wafer, there's just money tied up there and you've got to alleviate the cost somehow.

**Ian Danaher:** I'd say it's more market-based personally. I think that.

**Dave Jones:** And it's a market-based thing.

**Ian Danaher:** Yeah, they're playing into markets that are already established where they only need an ADC. So those are markets that the higher cost is just built in, right? So industrial markets.

**Dave Jones:** Or they're using an existing micro that they have to use for historical reasons or for other reasons. Yeah, so that's just priced in. And they need a nice and also external precision ADCs are actually going to be superior to the one inside. But they cost a hell of a lot more. Absolutely.

**Ian Danaher:** Overall.

**Dave Jones:** There are limits to what you can get with an ADC on a micro. So, yeah.

**Ian Danaher:** Speaking of good value, Dave, what's this about the, you put a piece of test equipment. I mean, since we're, I mean, Ian, effectively, this is test equipment, right? I mean, it's.

**Dave Jones:** Of course it's testy.

**Ian Danaher:** Low end test equipment.

**Ian Danaher:** I passionately dislike the C being called test equipment. All right. Oh, rubbish. Oh, you can't talk about this now, Dave. Sorry. So, yeah, I know. The term here that I'm personally fond of using. Oh, wait, wait. Start up, start up. It's an educational tool. Kick it in. Here we go. Let me guess. Okay. Cavalier instrumentation. Cavalier instrumentation. Oh, what? What sort of a rank-ass term is that? Cavalier instrumentation.

**Dave Jones:** That's a VC term right there.

**Ian Danaher:** That is. I know. Chris and I are in agreement for once. I'm just getting burned over here. Okay. Yeah. All right, you guys. Well, Cavalier thing. That's a wank word. Right.

**Dave Jones:** Well. Wank word of the week, folks. Oh.

**Ian Danaher:** No, that's like. Run down, Stallman. All right. Well.

**Dave Jones:** How to insult your guest 101. We do it well, don't we, Chris?

**Ian Danaher:** Oh, yeah. We're good at that. Well, it's cool. But, no, it's the sort of thing you throw down to learn more about something. To develop high-level understanding of how stuff works. It's not the sort of thing that you would go to curve trace your transistors coming off the line to make sure they meet spec. I used the earlier prototypes of the C to debug the prototypes that were now shipping, or the versions were now shipping. So, that's about as close as it gets to test equipment.

**Ian Danaher:** Yeah, I was going to say. Equipment that measures other equipment is usually test equipment.

**Dave Jones:** It's test equipment. Yeah. Okay.

**Ian Danaher:** Anyways, Dave, you had a piece of new gear you wanted to mention on here real quick.

**Dave Jones:** Oh, it's, yeah. Rygol are coming out with a new 2000 series. Everyone's been waiting for an update to the 1000 series, which has been out for like four years now or something. It's dominated the market, the low-end market. But, yeah, Rygol have now announced the 2000. You can't buy it yet, which is stupid. I hate this. When they announce these products, they announced it at some European electronics show or something. And you can't buy it, of course. It's not going to be out for at least another three months or six months, and then only in specific regions or something. It's absolutely ridiculous. Anyway, it's a 2000 series scope, and it looks really good. It's going to be under $1,000, and that's a hell of a lot of hardware for under $1,000. Big screen, the whole works. And here's one thing I really like, 500 microvolts per division vertical front end. I haven't seen one of those for donkey's years.

**Ian Danaher:** Oh, yeah. That's like that 22-whatever scope.

**Dave Jones:** Yeah, it's like the tech analog scope that I did a rant on a while back. And, yeah, is this going to start a trend in low noise floor oscilloscope front ends? I certainly hope so.

**Ian Danaher:** No, it's not, actually. We're going to keep going faster. Why not? Because it's not many people asked for it, I think.

**Dave Jones:** But if you get it on a sub-$1,000 scope now, it might push the bigger manufacturers to start including 500 microvolts per division. Because you can't go much lower than that because just the inherent noise floor of the front end, you know, you just can't do it with the high bandwidth. And the one megaohm input impedance and that sort of stuff. But still, I like it. It's got like a big 8-inch WVGA screen. It's got all the USB and triggering stuff and it's going to be really cheap. So they've upped the ante to what you can get in a basic scope these days. Yeah. Looks absolutely incredible. And I'm hoping to get one. Yeah. In fact, I have been promised one.

**Ian Danaher:** So that person better come through.

**Dave Jones:** Yeah, they better come through. Otherwise, they'll be hell to pay. Yeah. You know, I wonder about... Anyway, I think it's amazing what you get these days for the money. Yeah. It's just, you know, this is a serious bit of kit which you couldn't even dreamed of 10 years ago for getting under $10,000. Now it's, you know, now it's under $1,000. It's hobbyist level.

**Ian Danaher:** Yeah.

**Dave Jones:** Incredible.

**Ian Danaher:** I mean, I bought an Android phone with like a 400 megahertz CPU for $100 without a contract.

**Ian Danaher:** Yeah.

**Ian Danaher:** I mean, tech is getting cheap. It's nice that test equipment tech is getting cheap too.

**Dave Jones:** It is getting cheap as well.

**Ian Danaher:** Yeah.

**Dave Jones:** And it's got 14 meg of sample memory, for goodness sake, at 2 gig samples.

**Ian Danaher:** I bet you it's pulling... Like the screen is probably a cell phone display.

**Ian Danaher:** Yeah.

**Ian Danaher:** It's getting there, right? It has to be reusing cards.

**Ian Danaher:** Maybe a tablet display probably because it's 8 inch. It's a tablet.

**Ian Danaher:** Probably a tablet display or something. Yeah. Okay.

**Ian Danaher:** It makes you wonder because like bringing it back to the C, right? I mean, C is browser based. And I think a lot of like on the scope side of things, you know, there's like Picoscope and a lot of those out there. Anytime I see those though, I'm just, I'm like, eh, whatever. You know, like I've never really thought those were good. They're a diamond dozen. Well, they are, right? But I wonder if these low cost manufacturers continue to put these screens on there just because there is that resistance to it, right? I mean, like personally, I think that like if people, when people see the implementation of the C on the screen, I think it's a really quite a brilliant way to look at data. I mean, I really like that a lot, especially SMU data because, or SMU data. I've seen a lot of that, you know, like, but at the same time, I think there's a lot of people that they probably tested in the markets and they're like, well, no, they want to screen on it still.

**Ian Danaher:** So, well, personally, I would love to get a nice AFE with some SRAM and a high speed USB bus and just have an open Python library or LabVIEW take your pick and be able to throw around the data from a quality, you know, Tektronix made analog front end. I don't think it's ever going to happen. I think that USB scopes are going to stay cheap and dime a dozen.

**Ian Danaher:** Right. Well, that's a pricing it for your market kind of thing again, right?

**Dave Jones:** Yeah, yeah, yeah. Well, they're two different markets. They're two entirely different markets. You have PC-based stuff and you have bench scopes. That's, you know.

**Ian Danaher:** But why are they different markets?

**Dave Jones:** Because, well, because you save a fair bit of cost not having all that because, you know, there's margin as well, which has to go on top of this. You save a lot of money on those knobs and those screens and everything else. And, you know, just having the interface and the fact that they're usually much slower, but you can do absolute, like, continuous sampling. You can do data logging and stuff like that, which you can't traditionally do with a bench scope. So, you know, if you're just using a regular oscilloscope, you don't want to use a PC-based one because they're just annoying, a pain in the ass. You know, it's much more convenient.

**Ian Danaher:** They're annoying in a pain in the ass because nobody with serious design talent has figured out how can we make this nice for our users. I mean, that's not the priority. It's how do we expose the functionality our users expect with a web-based paradigm.

**Dave Jones:** Well, the fact that it's on a PC. You've got a PC and a box and your PC can't sit the PC on your bench. It's just not convenient. That's why people prefer bench scopes for general troubleshooting because it's all in one dedicated box. You don't have to worry about it booting up or anything, you know.

**Ian Danaher:** When was the last time you saw a MacBook Air? Sure.

**Dave Jones:** But who the hell wants to, who the hell has a MacBook Air in their lab, for God's sake? You want a proper bench scope?

**Ian Danaher:** Like a tablet or a laptop or a netbook? No, this is why.

**Dave Jones:** I'm telling you why the two markets exist because USB scopes are cheap and they're a way to get data logging and multi-channel capability. So if you want data logging and multi-channel, it makes sense to go to a PC-based scope. It doesn't make sense to use a bench scope and bench scopes don't try and offer those sort of functionalities. Right? They don't offer your eight channels. They don't offer your continuous sampling and stuff like that. It's better to use a PC and stream data to your hard drive. Okay? All righty. But bench scopes are designed as traditional troubleshooting. There's no way in hell anyone can argue that USB scopes are superior to bench scopes for general purpose troubleshooting. You're not going to win.

**Ian Danaher:** Yeah. I never argued that. I'm just saying that if the scope manufacturers decided to build an analog front end complete with the bare basics of what an oscilloscope is, some way of capturing information and showing it to a user and moving it back and forth, that it would be awesome. Because right now, instead of every university lab ever where a student is sitting there with a laptop, their phone, and then their oscilloscope, their power supply, their function generator, all these beige boxes sitting next to a machine that has 10 times the processing power of the rest of them combined. You would just have a much cleaner user experience where you have one-

**Dave Jones:** That's education, though. That's a different environment.

**Ian Danaher:** Okay. Well, I know education best. I like learning. I like teaching. So I'll stick to what I know.

**Ian Danaher:** I think there's a place in the lab, too. I mean, I think the thing that we're looking at here is that it is an established market, right? I mean, like, this is what- Of course it is. Dave's talking about what people expect. And Ian's talking about what could be in the future, right? And I think if-

**Dave Jones:** I know. It makes sense in the educational thing. I totally agree. But it doesn't mean, you know, bench scopes are suddenly going to vanish.

**Ian Danaher:** And I've talked about the whole tablet thing before as well. But obviously, that's been poo-pooed by Dave. No, there's another thing. There's another thing.

**Dave Jones:** Because everyone will be starting to take tablets into the classrooms. Now, they won't be taking notebooks anymore. They'll have freaking tablets, right? Because they're more convenient. They're smaller and all that jazz.

**Ian Danaher:** I think there's room for it, personally, Ian. So you go and make that, and we'll have you back in the show when it's done. Oh, I totally agree. Get that two giga sample front end done, and we'll talk about it on the show.

**Ian Danaher:** Yeah. USB 3.0, baby. There we are.

**Ian Danaher:** Oh, yeah. You definitely need that.

**Ian Danaher:** All righty.

**Ian Danaher:** Anything else for the week? I think our amp hour is up.

**Dave Jones:** Yeah. All right. As usual, we didn't get through anything on our list, so maybe next week.

**Ian Danaher:** My hour and 15 minutes of BAME is cloning. Closing out. Well, thanks a lot, guys. It's been a blast.

**Dave Jones:** Yeah, it was good talking to you. Thank you very much for coming on. Yeah.

**Ian Danaher:** All righty. Have a great one.

**Dave Jones:** And we hope... Oh, no. I've got one more question. Oh, okay.

**Ian Danaher:** All right. I'll stick around.

**Dave Jones:** How many RCs have you shipped now?

**Ian Danaher:** We've shipped a few hundred.

**Ian Danaher:** All right.

**Dave Jones:** Awesome.

**Ian Danaher:** Yep.

**Ian Danaher:** All right. So, people can find Ian on Twitter at IT Danaher. You can find the company Nonalith Labs on there as well. You can find me on there at Chris underscore Gammel, Dave at EEVblog, and the show at The Amp Hour. Also on Google Plus and Facebook and everywhere else. MySpace? No MySpace. Friendster, though. Damn.

**Dave Jones:** We're missing a social media golden opportunity here, Chris. We should be on MySpace.

**Ian Danaher:** Well, as the t-shirts of the MySpace personnel running the event yesterday said, MySpace is dead. Long live MySpace.

**Ian Danaher:** Nice.

**Ian Danaher:** Well.

**Ian Danaher:** All right. Unbelievable. Well, we'll talk to you guys next week. We will. See you.

**Ian Danaher:** See you.

**Ian Danaher:** See you.

**Speaker ?:** Outro Music
