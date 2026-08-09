---
episode: 601
title: Rebuilding Projects with Dave Young
url: https://theamphour.com/601-rebuilding-projects-with-dave-young/
---

**Dave Young:** This is The Amp Hour Podcast. Released August 28th, 2022. Episode 601. Rebuilding Projects with Dave Young.

**Chris Gammell:** Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Dave Young of Young Circuit Designs and Blue Stamp Engineering. Welcome back, my old friend. My first EE friend? I don't know. Yeah, maybe. Maybe. It was professional, maybe. Maybe it's professional. Longest EE friend, for sure. Yeah, I think. Yeah, okay, longest.

**Dave Young:** Yeah, for sure. Longest. Yeah, like, I've probably met other people before you, but then I've kept in touch with you the best, 100%. Yeah. Yeah. Welcome back. You are a guest of the show in the past. I think, let's see, I got a 305 and 409, which, of course, we will link into the show notes. First time, it was just you and me chatting. I think you said we were in a hotel room. Yeah. Yeah. And then we had you back on for the impedance match, the first consultant's impedance matching. And that's actually the one where I've told people this a couple times before, where I asked you and Eric and Peter, who were on the show, about like, well, where do you guys go when you have questions about consulting? And it was just crickets. And I was like, I guess I'm starting a consulting forum. And like, so that's been, it's been great.

**Chris Gammell:** Yeah. Yeah. That consulting forum has been amazing.

**Dave Young:** Yeah.

**Chris Gammell:** Especially the thread that's going about the component shortage group.

**Dave Young:** Oh my God.

**Chris Gammell:** I have had no end of horror. It's just so many emotions reading that. Yeah.

**Dave Young:** Really.

**Chris Gammell:** Mirthful laughter. Yeah. A lot of laughter, a lot of fear, a lot of relief.

**Dave Young:** Holy crap. Holy crap.

**Chris Gammell:** All these stories.

**Dave Young:** Yeah. Uh, bubble gum tap shoes is the phrase we use around here too, as well. That's the, uh, the code word when we're going to be talking about shortages, which we will be talking about quite a bit on this episode. One of the things that I want to ask Dave about is his experience as a consultant and we'll get to this, but we, his experience as a consultant and like just having to deal with it, you know, boots on the ground every day, getting notices, getting clients being like freaking out, you know, it's just always, there's always something new popping up these days.

**Chris Gammell:** Yeah. Like every third day you get an email.

**Dave Young:** Every third day. Wow. Yeah.

**Chris Gammell:** I, so I, I, I know when all my clients make boards, all the boards I designed for the last 10 years as a consultant, I know when they're making boards because there's something that's short and so I got to go run and find some other alternate or redesign a LDO footprint. Let's get into that right now.

**Dave Young:** Yeah. I mean, so it, okay. So someone goes and turns a hundred part board, right? It's got a hundred parts on it. Let's, let's just make up some numbers here. It's got, uh, 10 active components, maybe another 10, not quite as active as like an op amp, but maybe like, you know, 10 channel FETs and 10 to 15 of those. And then the rest passives, right? So like 80% passives and 20% everything else. How many of those chips are changing on a hundred part board like that?

**Chris Gammell:** Oh Lord. You know, for a while there, it was, it was a lot. It was a lot. So almost all the ICs and almost all of the FETs you couldn't get, but some of them you knew that you'd be able to get, like, it was like, ah, they're not gonna, they're not gonna really push this out very long. And it would take me longer to redesign it anyways than it would for you to do it. Yeah. I see. Or the client just, just pays the ransom and gets them from the gray market. Oh boy. Yeah. I know. That's feel real smarmy doing that. But if it's the choice between shipping your product and not, and you've got to make payroll.

**Dave Young:** I really hope what I'd like to do, here's what I'd like to do. I'd like to do a sting operation where I, you know, right before the shortage ends, I'd like to have like a load of legitimate chips that I sell to someone who's a broker at like a really high price. And they just spend their entire life savings on it. And then they can't unload them. And then the next day, this is like my like ultimate shot in Freud, you know, of like next day they're stuck with that until the next shortage, which is hopefully a very long time for now. And it's just like they, and they're destitute.

**Chris Gammell:** That is. I think that's the only way it's, it happens. And I think they've all made way more than enough money so that that's not a problem for them. And I actually just today, I think the tide may be turning because someone emailed me like spammers. Like, you know, you get, you get spam from PCB houses. And, uh, I got an email of people saying I have FPGAs at the best price. Yeah, no, they, and this is some random person offshore. They've been, no, no, no.

**Dave Young:** They've been doing that the whole time.

**Chris Gammell:** But they just, they finally got it.

**Dave Young:** Well, okay, fine.

**Chris Gammell:** They might've just found email.

**Dave Young:** Your email filters are going bad. Yeah.

**Chris Gammell:** Yeah.

**Dave Young:** Yeah. Yeah.

**Chris Gammell:** Maybe that's it. But when I saw that, I was like, oh, so you got to go out and chase it then.

**Dave Young:** Mm-hmm. So what is, I mean, what is your temperature on the current? I mean, is it slowing down at all for you or no?

**Chris Gammell:** It feels better. It might feel better because I've done all the work of designing all this stuff out. So I'm not, I'm not getting hit every third day like I was. Oh, okay. Yeah. From past clients. So, you know, I'm definitely getting fewer like, oh gosh, we need these parts and we need to turn it and we, you know, we need to get this done in the next six to 12 weeks. Otherwise we're out of stock of our units. Yeah. So I'm not getting those as often. And the other thing is the ones I do get, it is easier to find parts. I remember at one point I couldn't even get an end channel fat with some particular specs of any package. And I was like, well, maybe I'll just go on vacation for a few months.

**Dave Young:** Yeah. Right, right.

**Chris Gammell:** This will work itself out by the time. Yeah. I'm just, I can't do anything if we can't get any parts. I can do stuff if we can get some parts, but if we can't get any parts, it's a silly thing to be working on. So yeah, it's getting better. Every time I go looking for parts, it feels like there's more of them to choose from when I'm looking for alternates.

**Dave Young:** Okay. That's, yeah. I mean, that's the best. I mean, I don't expect like a market report from, from that's, you know, all encompassing here, but you know, I feel like it's just like something we can kind of ask people that are in the industry dealing with this stuff on a daily basis, daily basis. You know, when we have them on, we'll ask about it and hopefully the, you know, it's like kind of like a rotten tomato score over time. Right, right.

**Chris Gammell:** Get the average enough people, you'll get a decent reading.

**Dave Young:** Yeah, exactly. Yeah. Oh my gosh. I mean, what is the scale of the redesign though too? That's the other thing. Like, I mean, I've been hearing a lot about like, like power conversion is kind of like the big one that's, it's biting people.

**Chris Gammell:** Yeah. And the thing with power conversion is it's not well, especially for like switch mode power supplies where they're heavily layout dependent. That's where you really get hurt. So to swap an LDO, which I've had to do a bunch. Yeah. You know, it's no big deal. You move some stuff around, you make sure that your decoupling caps are real close and you're okay. But you, you change a, you change a switch mode power supply. Now your qualification is much bigger and now you've got to pick new passives. So now their passives aren't going to be as, as relevant. And then the layout is a big, you know, it's a big thing. And you might be moving from a QFN package or something bigger like a BGA or a WLCSP package. So the really small ones that trigger having to go to blind and buried vias. Oh. And so now you've got tons of pain just because of a silly switcher that needs to make 3.3 volts.

**Dave Young:** Mm hmm.

**Chris Gammell:** Yeah. So I have experienced all of those things and you have to have candid conversations with the client be like, Hey, this is going to take me some time, not just to design, but then we're going to have to have the prototypes built and then I'm gonna have to qualify them. And then there's a risk that there's going to be something wrong or there's gonna be something that needs adjusted or something is hopefully great, but something might go wrong. And they're talking about having more parts in 20 weeks. Maybe you just wait it out.

**Dave Young:** Yeah. Right. Right.

**Chris Gammell:** I mean, that's how it's always like a risk, risk analysis like that. Right. And there's, there's no Chris, it's just crystal balls. There's no like being an engineer, you always want to quantify it. You want to say like, well, there's a 75% chance of this and a 25% chance of that. There's none of that. It is all speculation. Yeah. And that's usually where they go and they do the smarmy thing in order and pay the people whatever they're asking or not whatever they're asking. There's been some, sometimes they balk and they're like, nope, they're asking a hundred times more. I'm not paying a hundred dollars for a switcher. So, you know, design it out or do it.

**Dave Young:** I've heard, I've heard some bad stories around that. Yeah. Yeah. Some of which were on the consulting forum.

**Chris Gammell:** So like I said, that you, you could easily enter that into the library of Congress as a great capture of the culture at the moment. The zeitgeist of pain in the electronics industry. Yeah. It's a very honest and very real representation of what was going on and what it was like. Yeah. Yeah. Yeah. Yeah. So apart from the work, you know, it's designing circuits, but the other thing that's really obnoxious about it is here I am redoing work that I've already done.

**Dave Young:** Yeah. Right. It's almost like you're being punished for just choosing parts in the past that.

**Chris Gammell:** Yeah. And everybody's getting hits. You don't, you don't feel bad. It's not like, it's not like you made a mistake or anything. It's just, I'm, I'm, I'm doing a bunch of work. I'm billing my clients and I'm not really providing any extra value. Yeah.

**Dave Young:** I was talking to someone about this. Maybe, maybe you, I don't know. Yeah, it could be. I just think about it. Like I, I mean, oh, you know what it was? It was like someone was asking me about like just the consulting field generally. And I was like, you know, the, the part shortage means a lot of stuff sucks right now, but I don't know any consultants that are hurting for work because everybody needs help in this space. Right. It's just like, there is a ton of work to try and just deal. The only way out of this is to, is to go to either wait or to do something about it. And so the, the do something about it crowd making money, you know, like that's, that's part of the, that's part of the thing. You know, you got to go solve problems.

**Chris Gammell:** It also happened at one of the hottest job market times that's ever happened. So even if you wanted to hire a full-time engineer, you couldn't because there's nobody available. Like everybody's, everybody's got a job and everybody's scrambling to get all their work done. And there's, there's a lot of work to be done as a whole and adding the chip shortage just, you know, it just piles on. Yeah, totally. Yeah. What's that term? Cascade failure. Cascade failure. That's a good one. Yeah. It's like one thing goes wrong, which would have been fine, but then that causes another thing to go wrong, which could have been okay. But then the third thing goes wrong and now you're in real trouble.

**Dave Young:** Well, outside of that, you know, so it's been, what year was that? So 305 was half of the show ago. Oh my goodness. Yeah.

**Chris Gammell:** Yeah.

**Dave Young:** Yeah.

**Chris Gammell:** I got to tell you that first time I was on the Ampour, I was like, oh, I'm cool now because I've been on the Ampour. Nah, you weren't. And I definitely was not and still am not, but I was on the Ampour, which is like.

**Dave Young:** I mean, you actually are cool, you know, aside from like, you know, being a dad and like, you know, all the things that make you uncool. Yeah. You've always been like a very cool person to me just because you, you know, like much like other people I think I've described in the show before, like people who just know what they like in life and are just confident about that kind of thing and do it enthusiastically. That's like the people I love hanging out with, you know? So like in that way you are cool. Yeah. But you're not like, you know, Instagram cool.

**Chris Gammell:** I'd refer to it as a confident dork. Like I think it's great to drive a minivan. So I'm going to do it with the best style that I can. And here I go.

**Dave Young:** Yeah.

**Chris Gammell:** Here I go.

**Dave Young:** Look at that cargo space. Yeah.

**Chris Gammell:** Nothing, nothing makes a minivan look good unless you've got, you know, a couple of bikes and a kayak on the top. And then all of a sudden everybody's like, oh, that car is awesome. Yeah.

**Dave Young:** You were living in Denver then now in upstate New York. Yes. But what about like other work you've done in the meantime? Like work you're allowed to talk about, I suppose, in the past.

**Chris Gammell:** So like consulting work? Yeah. Like six years. Six years. Yeah. I bounced around a bunch of stuff, but I've kind of boiled down what I do to take a measurement, make a decision, and then do something with that data. So like every project I do, measure something, make a call, do something. Whether it's telemetry or light up a thing or whatever you want.

**Dave Young:** Is the nature of measuring things changing from your perspective?

**Chris Gammell:** Yeah. It's getting way easier.

**Dave Young:** Way easier.

**Chris Gammell:** They took our germs. I mean, it really is. I just, I designed a, I designed an ADC in that when we were at Keithley, Chris, it would have been awesome to have that ADC. And it was like, it's available now in small quantities for $20.

**Dave Young:** Yeah.

**Chris Gammell:** It's. Yeah.

**Dave Young:** You amortize the engineering over how many products you sell. And yeah. Probably not that many if it's a $20 ADC, right? Yeah. It's like, okay.

**Chris Gammell:** And it's still, it's still great to have. You got to have the nuance because you, you can't plug in crappy cables into a really high hand ADC is, is not going to give you what you want. Sure. Sure. There's still all the nuance and there's still all a lot of engineering, but the things that you can do now are way better with an IC than there were before. At, at, at the price point that can be afforded for a reasonable product.

**Dave Young:** Yeah. I mean, that's the, I think the, that's where the efficiencies have gone. I feel like in our industry, right? Like it's, it used to be IMUs were $500 and now they're, you know, cents. Yeah. It's like, and just the things they enable and, and all of the, so you basically you, you pull all that, that know-how into the silicon design and then maybe the firmware around it. And then it's like, okay. And then schlubs like me can, you know, put it on the internet, you know? Yeah. Yeah.

**Chris Gammell:** So guys like me can look at that design and be like, oh, that's great idea. I'm going to do that.

**Dave Young:** Yeah. Yeah.

**Chris Gammell:** Yeah. That is good.

**Dave Young:** We just, we just, I think we just summarized the electronics industry, Dave.

**Chris Gammell:** It's actually a really great gig. Get to build cool stuff. Talk to other people that are doing similar things. See all their work.

**Dave Young:** It's good. I mean, what about, so let's put it on a five, six year timeline then even like five, six years ago. What about manufacturing tool availability? Like, I mean, let's leave aside the, you know, the shortages, but like the availability of tools and stuff like that too.

**Chris Gammell:** Yeah. So I switched to Altium. Oh yeah. Yeah. You'd been an Eagle, Eagle person. From Eagle. When they went away from the perpetual license, I was like, ah, it's not going to work for me. So while I still have an Eagle license and I still use it cause I have those legacy designs and I want to make sure I can support them. But yeah, I typically work in Altium now and there's been a lot of innovation at the top end. And I know you talk all the time about Kaikad and all the cool stuff that they've been doing. Everything's better. The big thing for Altium that they're doing, which is, which is really great is the Altium three, like the cloud stuff. Oh, you like the cloud stuff. I really do. I've heard mix both ways. Like some people love it. Some people don't, you know? What I, what I like about it is they're really clever. They made it so that you could take it or leave it. If you do not want to participate in the cloud, you do not have to participate in the cloud. You can still. I do not believe that's the case for Eagle anymore or whatever, uh, Autodesk electronics.

**Dave Young:** I think. Yeah, I don't think so.

**Chris Gammell:** And I think a lot of companies really miss the boat on that when it comes to, especially for me as a consultant. Cause like I said, I have legacy designs that I just can't import and move in. Like if somebody wanted to change the footprint and I send it, tell them that I'm going to have to change CAD packages just to change a footprint because part shortage is happening. They're going to freak out because it's a huge cost.

**Dave Young:** You know, it's a big, it's a big, even like the purchasing model of, of the actual software itself too, because you still own an Eagle license, a perpetual license, that sort of thing. Right?

**Chris Gammell:** Yeah. Yeah. And actually I pay for the, I pay for the temporary one too. Oh, you do. Oh, okay. Cause I have a couple of clients that like to use it and that's great. I'm happy to do it. Yeah, sure.

**Dave Young:** Sure. Yeah. That, that is truly a cost of doing business. Right. So as much as my miserly, you know, only like I get it, like, you know, and this is a point that past guest of the show, Jay Carlson makes on Twitter all the time. Like, look, it's the cost of a tool. He says you should use the best tool. I think, you know, KaiCat is best tool for me personally, but I totally get what he's saying generally, you know, like, and, and I think that's kind of the point you're making

**Chris Gammell:** here too. Yeah. The thing that, the thing that would drive me nuts is if they lock me out. If you can't connect to a server, if you can't open your design because you can't connect to a server. I see. Because the company went bankrupt or because they changed their business model or whatever. Yeah. Yeah. And then you've got to do a whole import to a different CAD package. Like that's not going to work. Yeah.

**Dave Young:** I do say the, the opaqueness, like I get IP blah, blah, blah. Like, but like Altium is the IP base or sorry, the binary nature of the files. And I'm still not a fan of like, there are importers now, even in KaiCat and stuff like that. But, you know. Yeah. But you can't trust the importer.

**Chris Gammell:** The importers are worse than the auto router. No. Well. They are terrible. They are terrible. I've done, well, I did the conversion from a couple of boards from Eagle into Altium and it was awful. And then the other problem is the pain stays with you, right? Because your library is imported. And so if you have like 12 extra layers that you don't need on every component, it is so annoying because that means every board that comes out of that component is now going to have extra layers.

**Dave Young:** Yeah. Yeah. Yeah. Yeah. Yeah. And so like either invest in like fix that one thing. Yeah. But even, yeah, that sucks. So now, now you're, you might as well just do it over yourself. That's what it comes down to. Yeah. Right. I mean, one, one trend that I've seen generally, and I think this is kind of like the Altium 365 thing is just like, you know, software moving into the hardware realm, right? Yeah. It's been slowly, slowly creeping into the firmware realm. I was actually just on the, uh, the Memfault and Philip Johnston and Alvaro Prieto did a really good webinar today about like tools and tooling and like, you know, all the stuff that Philip always talks about. And it's really, you know, a lot of it is like software methodologies kind of getting down into firmware. It's awesome. But it's, it is also happening in hardware, I think.

**Chris Gammell:** And I, the revision control that they have is really good. Yeah. And it's all native to the tool, which is nice. Mm-hmm. Yeah. But you know, collaborating with other people is, is way faster. So tell me about that.

**Dave Young:** I mean, are people actually, are you using that with your clients and stuff?

**Chris Gammell:** I am. So I, I have, I have a one client that went hard into the cloud space. And so, um, I, I, I dabbled with it before, like for the MCAD co-designer, which basically lets you communicate with a mechanical engineer. So you send the design and. Oh, that's cool. And they have a set, they have a setup so that you can, the mechanical engineer can move stuff and push it back to Altium, which is great. So I dabbled with that and that was fun. And it was, it was good. See now, I always figure that's not that big a deal. I didn't think so either, but. Okay. Yeah. I don't know. Like I have not been able to do that and I've used other systems. I guess Eagle can do that if you're in.

**Dave Young:** I mean, that's the new, that's the fusion thing. Yeah. Right. Well, and that's like the big thing they sell, but here's my point about this. Like someone moving a post in like, or like a plastic support. Yeah. And like, they always kind of, so like the, the fusion thing, it always is like, oh, well like if it moves, it dynamically updates. It's I don't want that to dynamically update. I want it to be like, oh, Hey Chris, there's a big change coming. You need to export your whole model to an STL. And then I'm going to generate an STL and push it back to you. Like I want, and we could do that a couple of times. I'm like, you like, you like to do it manually. I just feel like there needs to be a human in the loop there. But what the big thing to me is like, it's such a, such an important change that like, it shouldn't be a casual thing. Like I know they talk about like, oh, continuous changes should be fine. Whatever. If I'm a mechanical person is moving screw bosses around like that. I'm going to go over and slap the shit out of them. Yeah. Yeah. That is not something that should be happening. Or if it is okay. Maybe if I'm in like such a high speed environment that like, yes, that's the case. But I, I'm not like, yeah, no, you got a good point about that.

**Chris Gammell:** And I guess all team kind of solves that problem because you have to, it's like an ECO situation where you have to.

**Dave Young:** Yeah. Right.

**Chris Gammell:** You have to manually accept the change. And it's like, it's, it's, it's a list where you say like, okay, I want this to come into my board and you can expect inspected at that point, blah, blah, blah. But you're, I mean, your point's well taken. If you sneeze and you mess up the, the PCB outline and nobody realizes it because it's just a few mils here or there.

**Dave Young:** I don't know. I just feel like it's like, I I'm operating in two dimensions and I'm operating on very simple boards. But like if the outline changes, if my, you know, my inner outline changes, cause there's a new screw hole or something like that, there's new keep out areas. Like, yeah, that's a one-time change. It really should be a one-time change. I just, yeah, I don't, I don't know. Again, like I'm working on slow projects. So like, that is not really a problem. Maybe, maybe you're moving faster.

**Chris Gammell:** Well, you know, I, I, this board that I did in particular was a, it was an optical interface board. So, okay. The positioning of all the optical components was critical and constantly like that was, that was the biggest, that was the biggest design point.

**Dave Young:** So you were like, you were like tuning almost on.

**Chris Gammell:** And it was by nature, it's small. So, you know, moving, moving 10 mils this way or 30 mils this way is a, is a discussion. Yeah. I see. Okay. So I, yeah. Okay. So that was good. But then with the, when you go into the cloud and you can have other people working on the designs and every time you save it to the cloud, you type out what you did and what goes on and it's all, I don't know. Okay. So that's the change order stuff you're talking about, huh? Yeah. Yeah. So in general, anything you do, even going between schematic and PCB, you have to do a change order. And you say change order.

**Dave Young:** I think of them as kind of commits what you're talking about though. Like, are they incremental changes or are they actual change orders?

**Chris Gammell:** So they call it an ECO or, you know, engineering change order. So you have a list of things. So like, okay, I have to change some things in the schematic. Here's the, your list of things that we are about to make happen to the PCB.

**Dave Young:** Huh? Okay. Yeah. Yeah.

**Chris Gammell:** And then you say, okay, those all look good. Go ahead. And then there is the commit that you were mentioning. It was when you're all done with your edits and then you put it into the cloud and you can write notes and whatever. Got it. And you put notes on the schematic. That's like a release note. Yeah. And it's, you know, it's not, it's not seamless. It's not like working in Google docs where we could both be working on the same schematic page at the same time. And I can watch you move components over here and there. That's not. I don't think that's necessary either. I think that's, no, no, it's similar to what you were saying before is if somebody's futzing with stuff, I want, I want to, I want to know. Yeah.

**Dave Young:** I mean, like, yeah, it's like, leave me, leave me to do my part and then I'll tell you when I'm done. Yeah.

**Chris Gammell:** And that's what it's good at is like, okay, you work on the digital section. I'll work on the analog section. Yeah. Yep. And we'll, we'll meet in the middle.

**Dave Young:** And that, so that's been helpful. Speaking of ECOs, how have you been managing all of these changes? Cause like, this is almost like, like sustaining engineering type work, like, you know, stuff we used to do a Keeflee man, you know, maintaining products over time, stuff like that. Like, so are you standing up? Are you, we had a Michael Coran from Duro labs and I'll link that one into, but like he, they, they have like a change management system, stuff like that. Are you, are you pushing change management systems into these startups that you're working with or how do they, how do they handle changes?

**Chris Gammell:** So I used to handle change. I used to try and get them set up with systems and it's not great to tell other people what kind of annoying systems to use. Cause there's no like change order. There's, there's no management system that anybody's going to be like, I love working this tool. So. You know what I love? Spreadsheets. Spreadsheets. Yeah. And so that, well, that's what I switched to is I switched to spreadsheets because it's lowest common denominator and everybody can understand it.

**Dave Young:** Yep. Yep. Yep.

**Chris Gammell:** And so even a startup that likes to play around a lot with different ideas or iterate or have like has user interface issues where it's a lot of iterations, you're still talking about, you know, you're, you're probably making at least beta units by rev E. So it's not a ton of changes and it's usually done over a short period of time, somewhere between six and 18 months.

**Dave Young:** So, so basically you are just kind of getting the bootstrapped up enough with like to see the delta between. Yes. The rev a rev B rev C, whatever.

**Chris Gammell:** And that's how I track it is. So I have, I have a change list that I, as I go and actually, so my change list starts when I release the board. So when I release the board, I generate my change list and I generate the next rev of documentation. Uh huh. Uh huh. Cause sometimes, you know, you go to the fab and you wake up in the middle of the night be like, ah, I didn't change that one thing. Yep. So, so then that's what the change is. So the, the idea is to make entering information into the change list as low effort as possible and then checking it out of the change list. It, it takes some effort. So you have to first update it and you have to mark it as reviewed. And so there's some, there's some method there too. And, and it's all captured.

**Dave Young:** Yeah. That's good. Yeah. I mean, this is like the, uh, I think I've talked about this maybe on the forum, maybe I'll, maybe just with you, maybe on the show. I don't remember where, but like the, the concept of like, nobody is checking your work. Like, I think I've learned that from you actually, you know, you, cause you, you've always been very meticulous about checking your own work and you know, it's like, yeah, you gotta

**Chris Gammell:** have protocols. You gotta have, you gotta have things because it's so easy, especially if you're, if you're late on a design or you're rushing or the client's like, Hey, we're really hurt and we need this to be done quickly. Uh, there are always pressures to move faster and you know, it's one of those, you move. Yeah. You got to slow them down, right? I mean, yeah. And you got to say like, Hey, this is a time where we have to go slow to go fast. And I will, I am about to save you $10,000 and three weeks on your schedule.

**Dave Young:** Yeah, that's true.

**Chris Gammell:** Uh, I'm not going to tell you about it cause it means I made a mistake, but I'm going to save you a board right now.

**Dave Young:** Right, right, right.

**Chris Gammell:** And that's, you know, it's helpful when you, when you get them to calm down and it's only a day, the review process takes, even on a complicated board, the review process is like four to eight hours. Yeah.

**Dave Young:** I mean, do you, do you do any? So, well, I guess since the last time you were, I guess you were both times you were on the show, I was not yet doing consulting full time. I had just been thinking about it when you were on the, or maybe I had just started it, but do you like counsel people that are getting into consulting? Is that something you've done aside from me? Apart from you sitting there sharing. I don't count.

**Chris Gammell:** I'm chatting over drinks with Chris to tell him it's great and great and great. It's going to be fine. It's going to be fine. It's going to be great. It's going to be great. Yeah. You know, I, I've talked to some people that, that look at it and everybody always wants to know how to get the first few clients. And that's immediately their first, the first question out of their mouth, which is fair because, you know, the first few years that I did it, it was, it was a, it was a few lean, lean years. You know, you don't, you don't make a ton of money and they always want to talk about that.

**Dave Young:** You know, this is the thing that I've tried to impress on people when I've talked to them about it is actually the stuff that you and I talk about outside of, you know, work stuff is we often talk about personal finance type stuff. And I think the number one thing that I learned from you is just like, you've got to have your personal financial house in order. Like that is the most important thing. Cash cushion, cashflow, like just understanding where you are, making sure you're not like taking on a bunch of debt and like, I don't know, like it's just.

**Chris Gammell:** Yeah. You can't, you can't do well independently if you're sitting there worrying about how you're going to pay your mortgage or pay your car payment or how you're going to, how you're going to, you know, get through the next month. Like it's just not going to work out. You're going to be preoccupied. It's not, it's not going to work out. You got to be right. You got to be making moves six, 12 months in advance if you're going to be out on your own.

**Dave Young:** Okay. So 12 months ahead, you're starting to save, you're saving as much as you can after salary, hopefully type of thing. Sure. Then what, what are you doing after that?

**Chris Gammell:** Find work. You didn't, you didn't, you didn't know I was going to ask you this stuff. I, we didn't. I did not. I did not, but yeah, so the advice is to, to find a client. And actually I would even make that a more broad statement because I've worked with a bunch of startups. I would say starting any business, you have to find somebody who wants to pay you money. And I don't care.

**Dave Young:** That is, that is correct.

**Chris Gammell:** Yes. I don't care how good your patent attorney is and I don't care how great your website is. And I don't care. I don't care about any of that stuff. If you have yet to find somebody who wants to pay you money and like really wants to pay your money, not to just like sit at the bar and tell you, I would totally borrow that. You, you gotta have that. If you don't have that, then you don't even know who you're going to be talking to about what needs to be built or what needs to be done. So like what services are you offering? I don't know. Well, go figure out what people need to need services done.

**Dave Young:** Yeah. I mean, I always think about, uh, so like, I think 12, if you are planning 12 months out as well, like, uh, talking, you know, if you're not networked to actually go and like start talking to people and like, you probably have some people that you could talk to about something relevant to this. So like, I always think about the common contacts we had, like when we were both working together in Cleveland, like you want to talk to people that are hubs. Right. So that's always the. Yeah. People like Chris Gammell of the, I was actually going to say Dave, Dave Young of, of circuit design. Uh, but like, I actually, what I really mean is like FAEs. Those are the ones that I think about, you know, sales, salespeople and that sort of thing.

**Chris Gammell:** And I tell you what, they, they're really awesome people just to start. I've, I've never met an FAE. That's not really happy to talk about electronics. Like they buy their, buy their personality or just the natural person to be drawn to that position loves to talk about cool technology and loves to talk about making cool stuff.

**Dave Young:** Yeah.

**Chris Gammell:** So even worst case scenarios, you talk to an FAE, they don't give you any leads, but you get to talk about really awesome things to build or, you know, neat projects.

**Dave Young:** Yeah, but I think you shouldn't be asking for leads on the first conversation anyways. Right. It's more like, what's that? Uh, there was like a thing about, uh, someone who started a company is like, anytime I asked an investor for money, they gave me advice. Anytime I asked them for advice, they gave me money. I think that, I mean, like that same kind of thing too. Like you don't go and like ask an FAE, like, oh, do you know anyone looking for a consultant right now? It's like, nah, tell me about the business.

**Chris Gammell:** Tell me about the, I don't, I don't think that would work.

**Dave Young:** What are the trends you're seeing? You know, like that sort of thing is like, you got to get to know someone first and like build that relationship.

**Chris Gammell:** Yeah. I mean, really the, the question that I would ask the FAEs is what's annoying all your people right now. Yeah. That's a good one. What job needs doing? That's the question I ask. What job needs doing? What is taking, what's, what's holding everybody up? What kind of crap I take care of for you? Yeah. Yeah. Yeah. What do people hate?

**Dave Young:** What, uh, what is, what is the current answer to that in your region?

**Chris Gammell:** It is very hard to find technical people. It is very hard to find technical people. Yeah. I just spoke to, uh, Cornell's accelerator and I gave him a big talk because they're very early stage at Cornell, their summer accelerator. And so I gave him a talk like, Hey, you really have to know that UL and FCC exist, but not now. So I was trying to give him like the 30,000 view of if you want to be successful, there's all these things that you need to know about and plan for. And this is kind of your path and, and all of their questions at the end were, how can we find people? What level of people should we be hiring or engaging? If we can't find people, should we go on places like Fiverr? Oh my God. I mean, so everybody specifically, I would do Upwork, but you know what I mean? But the question is, how do you find people? And, and unfortunately I don't have a great answer.

**Dave Young:** Leave Ithaca, New York is probably the first step.

**Chris Gammell:** Yeah. Yeah. Well, I don't know. Ithaca is not a bad place if you're just looking for some help over the summer.

**Dave Young:** No, it's a beautiful place. It's a, and there's a lot of smarty pants there, but I'm just saying that like, you know, it's not exactly like buzzing with, uh, humans. No, it is not. It is not a high density area.

**Chris Gammell:** No, no, you're not going to, you're not going to throw a rock and hit people. You might throw a rock and hit a cow, but still, uh, how do you find people? How do you get people to work? How do you, how do you set people up? I think that is the biggest pain point. I talked to multiple of my clients have expressed interest in growing their teams and still struggling to find folks. Huh? So if any of your, any of your listeners are in college or trying to change careers or something, start building stuff and show that you can actually do stuff. And it is a very compelling case to be making like, Oh, look, I know how to build.

**Dave Young:** Yeah.

**Chris Gammell:** Well, IOT point and do all the kinds of stuff that you are trying to do.

**Dave Young:** Well, that's, I think that's definitely one piece of it. We talk about that on the show a lot here, like, you know, build your portfolio, build out the things that you're doing. Yeah, exactly. But then there is that, that matching of those seeking and those looking. Right. Right. Those, those are the same word. Sorry. Those, those looking for a job and those looking to find people for a job. Right. Like that, that matchup is, I think that's still a tough piece though. Right. So that's still networking and I don't know, like, yeah, getting out there. So like, okay. So then your clients, where are they looking? Cause that's another thing. Like, so people might be wanting to change jobs that are listening to the show, but they don't even know where to go. I think the default is always like these job boards that are soul sucking, you know?

**Chris Gammell:** Yeah. So the job boards are soul sucking. The job boards are really great though, because they tell you who's hiring. And so the most successful thing I've seen people do is go on job boards and then go on LinkedIn. So who's hiring? Who do I know that works there? Or who do I know that knows somebody that works there? How can I, how can I connect with somebody who's at this place that's hiring? Cause you're right. The job boards stink. And who knows what process they have for dealing with all the applications and all this stuff. It's a challenge.

**Dave Young:** I had someone who I introduced them to a company and they were, you know, like they said, oh, yeah, we'd love to talk to you. You know, like your credentials sound fine. And then this person that I was introducing them to put in a resume through the place they wanted to do it. I think it was LinkedIn. Yeah. And he's like, yeah, they immediately rejected me. Yeah. And so then he didn't hear back from them. There was like just nothing. It was just black hole. Right. Yeah. And then like two weeks later, I was like thinking about, I was like, they specifically said they wanted to talk to him. Like what the hell happened here? And it was like, because of a filter system on LinkedIn, he didn't click the right button and he just got immediately rejected because that's how these, these things are just like logic engines and they, they have no idea.

**Chris Gammell:** No, no idea. Yeah. And it's not like people are that much better. You could be, you know, if you get a stack of a hundred resumes and you have an hour to get through them, what are you going to do? You're going to try and figure out a way to get through them and you're going to lose good people and you're going to, you're going to put bad people that aren't a great fit in your good fit pile. I'm less worried about that part.

**Dave Young:** I mean, that, that's just tiring in general, right?

**Chris Gammell:** Yeah, sure. Sure. So I guess it's this, this problem that we're talking about is not one that has been solved.

**Dave Young:** Yeah.

**Chris Gammell:** It is still a challenge. Yeah, it is. It is still a challenge. Networking is still the, still the answer, unfortunately. Sorry, folks. Sorry. Sorry about that. Sorry. I do like the, so I have, I run blue stamp engineering where we teach kids how to, how to build stuff. And so I have past staff who are spectacular. You know, we're very picky about who we hire. And so we have past staff who come ask like, Hey, I'm, I'm graduating. I'm getting my, finishing my master's program or I'm finishing my undergraduate program or I'm, I'm leaving school. Can you help me find a job? And I love to help however I can. And the best thing has been me saying, Hey, why don't you look on my LinkedIn profile and see if there's anybody you'd like an introduction to. And you know, some people I have on LinkedIn that I don't really know that well, but some people like if they were asked me if I, if they wanted to work at Goliath, I'd be like, I know the guy, let me connect you with him. You can talk to him over.

**Dave Young:** I'd be like, who introduced you? Oh, Dave, Dave Young.

**Chris Gammell:** I don't know about this kid. Yikes.

**Dave Young:** Well, uh, give people a refresher. What is blue stamp engineering?

**Chris Gammell:** Yeah. So we do, we do engineering programming for high school students. The idea being that if you give the student the ability to pick their project and a bunch of really cool tools and a very experienced staff that you'll be able to give the best education experience possible by them just building it. And there's, there's a bunch of things that we do differently than everybody else. Like we have a, like a three or four to one student to staff ratio. And we need to have that because most of the time our staff haven't built the projects themselves.

**Dave Young:** So, right. They're not like a turn the crank, do the same. Yeah.

**Chris Gammell:** They don't have answers. And we, our favorite conversation to have in training, in a staff training, we talk about this, the best conversation you can have with a kid is they say, Hey, this isn't working and I don't understand it. And then for a staff member to say, I don't understand it either. Let me show you how it approaches problem. Yeah. And so now instead of teaching them how to build that one robot, you're teaching them how to build robots in general, how to face problems that have no clear path forward. And that, that experience is so much more powerful in the motivation that the kids come in because they get to keep their projects. And because they, they define their own goals and they define their own projects. It makes for a really amazing experience for both the students and the staff.

**Dave Young:** Yeah. I feel like there's another piece in there too, which is like the, I'm guessing you already have pretty high performing kids coming in that are doing engineering over the summer that are probably.

**Chris Gammell:** Yeah.

**Dave Young:** Yeah. Nerds and or future nerds. So like, I'm not too worried about them, but just the, uh, kind of like the self-talk piece. Like, you know, I still, my late thirties, I'm still like, ah, you know, I suck at coding, you know, like I can't do this, but like the getting over that, like, you know, just the spending time on it and doing some research on it and maybe reaching out to people for help. And like that, that self-talk piece and like that ability to just, you know, process that problem. That is, man, that is, I wish I would have learned that a lot younger.

**Chris Gammell:** Yeah. It's a really powerful tool to be able to do that. And the, and you know, the, the confidence and the independence that is gained. Well, there's no other way. In my opinion, there's no better way to grow confidence and independence other than feeling like you've gone in too deep and then figuring out a way out like that. You get to that point where you feel like I can't do this. I'm not good at firmware. Yep. I'm not good at X, Y, Z. I don't know what I'm going to do. I just want to give up. The only way is through. The only way is through. And then once you go through it, you look back and you're like, oh, that wasn't that bad. Well, I, I know that now. Yeah. I know it now. But then the next time you face that feeling, you can remember back. And so every time you face that feeling, you mind it less. And eventually you don't care at all. Like, you know, you and I have been doing this for years.

**Dave Young:** I would say that, but I think, I think the feeling, I think, I think that's the other thing though. Like the fear is still there, you know? Is it? Oh yeah, man. Every time, every time I open an editor, yeah, it's still there.

**Chris Gammell:** Yeah.

**Dave Young:** But I think the thing is, and this kind of reminds me of, this is a bad example because it's, it's not accurate currently. It kind of reminds me of fitness as well. And my old sports coaches being like, look, it still sucks when you have to like sprint across a field, right? But, but your recovery is faster. Like that's what you get better at. You get better at recovering. You don't. That is a good, that is a good analogy. You might get a little bit better at the sprinting part. You might, you know, get a little bit faster, but it's still going to hurt. It's like, there is no getting around like exerting yourself like this still hurts.

**Chris Gammell:** Yeah.

**Dave Young:** But the recovery. Settle on in with a little bit of pain, but. Yeah, exactly. It'll be okay. And like, and then some, like some sickos, they love the pain, you know? Yeah, yeah, yeah. They really do. I have examples of, you know, very accomplished engineers here that have been on the show, yourself included. You're all sickos. I love it.

**Chris Gammell:** Yeah. That's a good ride. It's a good ride.

**Dave Young:** It's a good ride. Right. I mean, but it's like, but I think that that is the most successful, like that tenaciousness is that, you know, if you can learn that somehow, just that like, you know, either you're going to get through it or, you know, you somehow you learn to love it, whatever those that is like, that is a marker of success in my, in my opinion, in the engineering field specifically.

**Chris Gammell:** Yeah. Yeah. And the more, the more you look for that, the better off you'll be like, it's okay. I'm uncomfortable. I'll figure it out. I'll get there.

**Dave Young:** Yeah. Yep.

**Chris Gammell:** I'll get there. And that, that, that is what we try and try and teach.

**Dave Young:** Yeah. I mean, that, how long has that program been going on now?

**Chris Gammell:** We just finished our 11th year, I think. Wow. Congrats. 11th year. Yeah. We've been at it for a while. It's been, it's been quite a ride.

**Dave Young:** So 11 years and they're in high school. So some of them are in almost 30. Is that right?

**Chris Gammell:** Yeah. I suppose. You have like an 18 year old, I suppose. Right? Yeah. That is, that is true. I have not really thought of that that way, Chris, until you brought it up. Oh man, we're old. You old. That's the, yeah.

**Dave Young:** No, that's not, not really the age piece. I just mean like the, you know, like where they are in their careers. Like they're probably out in the world.

**Chris Gammell:** Right. So we have, we have, it's really great because we have some of our past students coming back to do guest talks about what their career was and all that stuff. It's really awesome. And it's fun to have past students come back as, as staff. Actually, they make some of the best staff. And that, you know, having, having that come back full circle is, is pretty neat to see. I'm just imagining what some of those students from 2011 look like now that they're like 30 and that's making me feel quite old.

**Dave Young:** Yeah.

**Chris Gammell:** I mean, you're kind of old too. I am. I'm more than kind of old. That's fine.

**Dave Young:** You know, whatever. Time marches on. Time marches on.

**Chris Gammell:** It's been a good ride. It's been a good ride.

**Dave Young:** I mean, it's, it's interesting. I mean, like as a, if you were able to do a longitudinal study on that sort of thing, you know, like you'd have to really have a control group that just kind of came and sat there and didn't do anything. Like, oh yeah. The, the sit there group, they, they, they did poorly in life. But like I said, they're motivated enough to do a summer camp in engineering. Like that's, that's pretty, that's pretty awesome.

**Chris Gammell:** Yeah. It's, it's, it's pretty great. It's pretty great. And you know, the other thing is since it's self-defined, everybody has this like edge to want to, everybody comes, wants to do really great things and, and make cool stuff. They don't want to just like turn the crank that somebody else has done.

**Dave Young:** So what is the, you mentioned this, I think when you were on the show the first time, six years ago or whatever, but like, what is the, I think I asked this question as well. What is kind of the, what's the hot topic? I suppose. Like, you know, so a high school kid wants to do something in engineering. It wants to do a project for themselves. What is, what is a common denominator of those, of those projects?

**Chris Gammell:** Yeah. I'd say there's, there's two, three things that come up. Robotics is still cool. I think robotics is gonna be cool forever, but robotics was cool 11 years ago. It's cool. Now making stuff, do stuff. I mean, our robotics projects are different because technology has changed over the last 11 years.

**Dave Young:** I mean, steppers are steppers and the drivers and all the circuits there are just incredibly cheap comparatively.

**Chris Gammell:** Yeah. Super cheap. But like now you can hook it up to an Android phone and have it do stuff based on voice control where 11 years ago.

**Speaker ?:** Oh wow.

**Chris Gammell:** Okay. Yeah. That's not something that was available 11 years ago. So that's always cool. The next thing, which is also always cool is user interface stuff. So kids like making things light up or show you information. Actually, that's been different is we have, we have projects that grab stuff from the internet and pull it in and display, like do different things based on what's going on in the world. So that's kind of cool. It's like IOT style. Yeah. So, so yeah, you, you use some of the APIs and you get data that way and you make, you, you make things happen. So non-traditional, non-screen based information from the internet. That's great. Yeah. So, but that, that would be as a bigger thing of user interface. So they like stuff that lights up. They like stuff that makes noise. They like stuff that they like stuff that, that you can see and feel and hear. So that's, that's usually sort of thing. Yeah. And then the third thing that's new is everybody loves machine learning and AI. Uh-huh. Got it. And, and we have some pretty compelling projects for that.

**Dave Young:** And they already know that coming in though, or like, I can imagine like if you're flipping through a catalog of like potential projects, that would be one thing.

**Chris Gammell:** Yeah. A lot of them are plugged into it and they know. Huh. And then some of them aren't like some of them be like, Oh look, a project that can detect when I'm smiling or a project that can detect when we have one project that'll detect when a parking spot opens up in front of your house just by setting a camera out in front of it. So. Depends where you live.

**Dave Young:** That's more important in certain parts of the country than others. Yeah.

**Chris Gammell:** Most of our students come from the Bay Area in New York City. So that's a. Yeah. Yeah. I see.

**Dave Young:** That's a thing. That's critical. Yep.

**Chris Gammell:** That has gotten a lot, a lot, a lot of attention. Hmm. And actually one of the lessons we have to teach the students is like, Hey, I know this is so cool. You don't want to spend your summer at blue stamp cleaning data. Oh, like that. I say, Ooh. Yeah. Cause everybody assumes that you can just like plug in data and it'll figure itself out. And it's like, well, no, it can do that if it has a data set from which to work. But if you want to do something totally custom, which we love to see a blue stamp, you're going to have to provide it the data set.

**Dave Young:** Right. No downloadable data set just outside the window of your house. Yeah.

**Chris Gammell:** Yeah. So they have all these cool ideas and it's like, yeah, that is an awesome idea to automatically detect things. And we would love for you to do that, but it's not so great when you have to spend hours and hours and hours telling the model what is and what is not what you're looking for.

**Dave Young:** What about other things that may have changed? Like, so are more kids popping up with like Python experience or I mean, RP2040 is now like this new, you know, supercomputer, basically that's $4. Yeah. Yeah. Are they, are they coming in with that knowledge already? Cause like I said, I assume these are kind of like high achieving, high interested level students.

**Chris Gammell:** Yeah. A lot of them are not everybody. Some people come in with no experience and they just want to try it. Oh. Which is awesome. And that's a benefit that we have is like, if you're doing your own individual project, you can put a kid right. Who's done nothing right next to a kid who's done 10 projects. And it's, it works great.

**Dave Young:** I can imagine like an amazing outcome would be they don't stop at the summer project. They're like, I like, again, like I like this feeling. I like the achievement or the, you know, kind of the getting through things and like that basically building that muscle and like working it out. Right. That is the most important thing.

**Chris Gammell:** We, we love to see it when, when students keep going and going and going and going. And actually we try and get them, we try and get it. Cause that's a huge dopamine hit when you make something totally new out of a project that already exists. And so we, we ask the students to do that. Like that's the goal is for the students to build their base project, but then design something on it. That's totally new and never been seen before so that they can add something. And it can be something simple. Like if, if you have an obstacle avoiding robot, adding an extra sensor, adding a macro so that it does something unique when it detects a specific type of obstacle or even adding a speaker, you know, there's, there's a hundred things you can do on any project, but once the student makes it up and then implements it, it is so exciting. Like they love it. We love it. Everybody gets really excited. And then once, once you show them that once, it's very likely that they're going to continue doing some other project as they move forward.

**Dave Young:** I've been really interested to like, I think this is kind of on Hackster, but they've done a very good job of like convincing all these chip companies to like, just keep running contests over and over again. And like, and so like a high school student, like, you know, and you see these, the kids that are winning, not, not always kids, but you know, like they're people of all ages and backgrounds, whatever are submitting projects to these things, but often they are very young as well. And like, you could probably build out a lab or build out, you know, like win some, you know, cash or prizes and stuff like that. If you were just like into that, just designing projects for these Hackster contests and be like, Oh, Nordic's doing a project or a contest. No problem. Yeah. I'm doing a contest. No problem. Like, you know, like just sweepstakes of electronics builders.

**Chris Gammell:** Yeah. And what a great way to contribute to, right? Cause you're, you're, you're feeding everybody who wants to get after that kind of stuff is you're, you're giving them that spark. You're giving them that little bit of motivation to get up and try something. Like on the, on the chip company sides or? Yeah. So for Hackster to keep running all these, all these events or all these contests or whatever they're doing. Well, Hackster's doing, cause they get paid for the contest. So. Oh, they do. Like, oh yeah, yeah, yeah. They, these are marketing activities. That's a good business model.

**Dave Young:** It's not, it's good. I mean, it does well. Yeah. I mean like, and it's not, it's not cheap, but it's, but it is, I think it's a multi-tiered like benefit to, you know, like the people doing the contest win. The people that are promoting a new product or whatever, they win. Hackster wins cause they're selling more stuff.

**Chris Gammell:** Yeah.

**Dave Young:** That's, it's great.

**Chris Gammell:** Does Hackster sell stuff? I don't even know what they sell. I thought they. Hackster is part of Abnet now. So. No kidding. I had no idea. Oh yeah. Yeah. Are there only like three companies left?

**Dave Young:** Yeah, that's right. Yeah.

**Chris Gammell:** It feels like there, I, I was sitting down, I think I talked to you about it. I was sitting down designing an instrumentation amp and I was like, there's really only two or three companies I'm going to be buying this part from.

**Dave Young:** Oh yeah. Yep. Yeah. And I mean, now that linear, linear is gone, maximum gone. Ah. So it's basically analog and TI.

**Chris Gammell:** Analog and TI. That's where I spend most money. And there's, there's a couple other smaller companies that do have some, I think it was like. Yeah. Was it Intersil? No, they got bought too, didn't they? I don't know. But there, there are very few places you can buy instrumentation amps and that's pretty obnoxious.

**Dave Young:** Well, I mean that, but that kind of rolls back to what we talked about before too. Like so many, so many of these chip companies are also like rolling the instrumentation amp into like, oh, it's an in amp plus an ADC plus a micro. And the whole thing is now like a application specific, like measurement doohickey, you know, in a single chip.

**Chris Gammell:** You know, it's funny you mentioned that, that ADC I was talking about at the beginning of the show.

**Dave Young:** Yeah.

**Chris Gammell:** That was an instrumentation amp integrated with a revolted reference with an ADC. Was it the ADUCM 360? No, no, it was a different one. That thing's okay. It was a different one. But the fact remains is I love that. I mean, that's a great thing to do, especially because it helps you really bring down the cost. But I, I just, I don't think any market is helpful when it's an oligarchy. It's like, this isn't a... Yeah, yeah. Right. That part sucks. Yeah.

**Dave Young:** Like a duopoly is not going to be great when... Well, especially when these two companies are making chips at the same place and it's, you know, potentially in a country that might be taken over by China. Like, like... Yeah. We got some systemic risk here. If you want about it, you know, like... Yeah.

**Chris Gammell:** Yeah. I started talking, you know, in 2008 when they had the, everything melted down with the financial crisis. I realized that too big to fail is too big to exist. That's, that's how I've sat there. It's like, if we can't stomach this company failing, then they got to go. Or at least split up. Yeah. Or at least do something else. Split up. Yeah. Split up's fine. Right. Yeah. But the situation can't be where we need you more than you need us. I'm just still salty that Linear got bought. Like, that's... Yeah, me too. That should not have...

**Dave Young:** No, come on.

**Chris Gammell:** That man, when you talk about companies with soul, that company at soul, it sucks. Those guys, those guys, I mean, like I said, I enjoy talking to all of these... Like Maxim, pound sand. I don't care. Maxim, good riddance. You're just mad because they never picked up the phone for you. Yeah, exactly. That's exactly right. Yeah. I understand. They never picked up the phone for me. It's okay.

**Dave Young:** Yeah. The last thing we were going to talk about is investing in oneself, which sounds like we're chapter 11 of the self-help Dave and Chris book. But what we're really talking about is like, because of integration levels of these things, right? Like say that that part you were just describing has a micro in it. Like basically now you as the hardware designer, you'd like, even if you don't have the micro in it, it's just talking to a micro, like hardware engineers need to know more of more of that stack now, right? Like it's, you can't get away with like just being, just being a hardware person. If that was ever a thing, you know?

**Chris Gammell:** Well, and why would you want to? There's so many more opportunities to be more involved with the design, right? Like the reason I only do what I do is because there's only so many hours in the day. I would love to get involved with all the different things and to be able to launch a product all by like, it'd be so cool if I can make an iPhone 11 or whatever they're up to by myself. Yeah. They're only 13 now. Yeah. But that'd be so awesome if I could do that. It's just, you can't, you can't, you can't, but you're right that the tool sets allow you to move and do bigger, broader things because they've abstracted so much of it out. And yeah, it is a challenge to, to figure out, okay, so I've got some time that I have available that I said I wanted to learn XYZ. What should XYZ be? That's where I always get, you know, there's definitely a FOMO situation happening where there's so much cool stuff happening. There's so much cool stuff I can do. And there's so many cool products or projects that I could build or technology I could explore. Oh, how do you pick? It's so fun.

**Dave Young:** What are you learning these days? I guess is the big thing. Like, because you said, like you said, your, your phone's been ringing every three days with a new board to be designed.

**Chris Gammell:** I've been learning tons about supply chain, which is not what I was after, but I guess it's got a purpose. I, I've really enjoyed getting more into digital hardware. And then I've wanted to grow that into doing more firmware. And, you know, I, I can do all of these things, but I would not call myself a bread and butter firmware engineer. You know, I spend most of my time designing hardware and then usually. Somebody else has a firmware. If it's a really big project or if it's a small project, I just do it because it's more efficient for me to do it as opposed to bringing somebody else in. I think it'd be interesting to see if with the gains that you were mentioning in tool sets, if I could take on more firmware, more of a firmware role and have a more full offering in terms of like product development. Yeah.

**Dave Young:** Ah, yeah. Yeah. One of the things that I've always, I think I've mentioned on the show too, is just like kind of the choppy nature. So like assuming, you know, the hardware scene isn't like it is now, but like if everything is smooth and if, you know, and parts are available and all that other stuff, like, you know, you have design takes, you know, even if you're building a board from scratch, right? You say it takes a month or whatever. Or it's like, okay, now I do the full design. I send it out. I'm not paying super crazy shipping times and build times and all the other stuff. There's some amount of time in there. And unless I'm really good at lining up all the work so that the next project starts right as the end, right as I ship off the files for the first project, like there's just no, there's nothing carrying that gap, you know? And that's like that. I feel like firmware kind of smooths out the, not that this is a reason to learn firmware, but I'm just saying that there, there is less of a choppy nature to firmware projects because there's always another thing that needs to be done with firmware. There's always improvements you can do. Same with software, right? It's just like, it's just like the, there's always, it's not as choppy in that way, you

**Chris Gammell:** know? Yeah. You're, you're a hundred percent right. There, there, there could be no waiting in the entire firmware project unless it's waiting on for on hardware. Yeah. Those guys. What do you mean? We didn't buy the fast turn time. I'm ready to go now. That's right. Uh, yeah. Yeah. Yeah. Yeah. I, I think it'd be, I think it'd be cool to see what kind of scope could be scope of project could be done by a single person being fully utilized. So one person, how big of a firmware and hardware task could one person take on and still be as efficient as a two person team? Cause that's what it comes down to, right? Yeah. Yeah. Adding a person adds an efficiency, but it also allows you to go faster and do more things that are more specialized. But there, so there's that point. I think it's moving to bigger and bigger projects and I'd like to do more of those bigger projects. Yeah.

**Dave Young:** Yeah. And I think, well, I think the frameworks are kind of being built, uh, up a lot as well, where, you know, schlubs like me can go and use something like Zephyr and design in a network interface where I'd be like, like, yeah. Sometimes I think about that. Exactly. Like if I had to start from just like, just the chip, right? No supporting firmware at all.

**Chris Gammell:** Like, Oh Lord. I don't even know. Like, would you get there? I don't know if, I don't know if you gave it enough time, if you'd ever get there. Cause I feel like that's one of those things you'd have to go back to school for. You'd have to go back to some, you'd have to get some training cause you can't just sit down and figure it out with YouTube videos. I mean, I assume like, okay.

**Dave Young:** So say like it was the best documented silicon ever. Right. Yeah. Okay. Perfectly documented. But for some reason they decided, you know what, we're going to document it and then it's on you. Yeah.

**Chris Gammell:** I think maybe, I mean, I don't know. Like it'd be a long time cause you would get stuck at some point you get stuck. Yeah. You get stuck. And then how do you get unstuck?

**Dave Young:** That'd be, I mean, this is always the amazing thing to me when people are designing things in FPGAs and they're like, yeah, well I designed my own custom logic. And it's like, well, nobody wrote the data sheet for that custom lot that you wrote the logic and then you're building on top of that. And it's just like, yeah, it's, I'm always very impressed in that sort of scenario. Yeah. Me too. Me too.

**Chris Gammell:** But I love this whole thing. But it's, but it's hard to charge hours for that sort of thing as a consultant, right? Yes. Yeah. There is, there is a part of consulting where you have to spend some time banging your head against the wall for your own good. Yeah. Yeah. Well, uh, what, anything on your, on your, your to-do list, your to-learn list? No. I, I, the to-do list is to find some time to make a to-do list. Yeah. Okay. It's been, you know, it's, it's been a, it's been a, a very challenging couple, few years in terms of being able to get everything done that should be done.

**Dave Young:** Yeah.

**Chris Gammell:** That's, uh.

**Dave Young:** Yeah. Cause you also, I mean, I remember one thing that I, I remember with you specifically as well, I remember asking you about like, not how you got your first client, but how you got your next client. Right. So like, I knew how your early clients came in, but like, I would remember asking you when I was starting consulting, like, well, how, how do you, how do you find that next job? Like once you're done with the job. And I remember you saying like, well, they just kind of, they come back. And I mean, who comes back? Oh, well the same clients come back because you've had, you've maintained the relationships and you, you know, you have products that are in the field and they need changes, revisions, enhancements, whatever. And like that relationship management is really important as well.

**Chris Gammell:** Yeah. And their, their, their colleagues will come back and also call. So you're like, Oh, Dave did our design. Why don't you call him? He was good. Yeah.

**Dave Young:** Are you sure they're not just looking at your website and just.

**Chris Gammell:** Have you seen my website?

**Dave Young:** Really impressed in your website.

**Chris Gammell:** Oh Lord. Yeah. Yeah. Boy. I had a client. I was laughing with a client about my website and I was like, yeah, I got to get around to changing that. That's one of those things I want to do once I have some time. And he was like, Nope, it's exactly perfect. It tells exactly who you are and what you're doing.

**Dave Young:** It's like, it does, it does show you're not spending all your time learning JavaScript. Nope.

**Chris Gammell:** You want a guy who wants to design electronics and not make webpages. This is him. This is him.

**Dave Young:** I'm pretty sure there's actually the exact same design, you know, more clients and stuff on here. Yeah. I've got a design as six years ago.

**Chris Gammell:** Yeah. Yeah. So that's not even my first website. Do you remember my original website? Oh my goodness. I don't. Oh, I'm so glad. I think you laughed at it then. Yeah, I don't. And that was before you knew about, you know, all the stuff, you know, now. And it's just, oh man, I'm glad people don't grade me on that kind of stuff.

**Dave Young:** Well, I think that's actually an important thing that, because I think that's the other thing when people come to me and they ask like, well, you know, should I, what should I do first? Like, should I go build a website? I'm like, eh. It doesn't really matter. No, I think you got to have a website. I think if you have nothing else. You got to have one. But if you have nothing else.

**Chris Gammell:** Even if it's Squarespace. Because it takes, you know, you stay home on a Saturday night and you make it. Yeah. But you want to have, you want to have a domain and you want to have it.

**Dave Young:** Yeah.

**Chris Gammell:** If you don't have anything else. You need an email for sure.

**Dave Young:** I think it's all about like, the first thing that I'm going to do, if someone comes to me and says, hey, I'd like to do some work for you. I'm going to go look them up. Right. And it's like, what is, it's not just what shows up on the web. Right. But hopefully when I, you know, Google Bob Smith, if for some reason, Bob Smith electronics, I get to Bob Smith LLC or whatever his company's called. And like, and I can like at least see that there's something there. And it's not like the only Bob Smith that I find in the Durham area is like, you know, a brick layer and it's like his photo. And I'm like, okay, well, when did he switch to electronics? Yeah. So you need to at least prove and get over that hump. Right. So like, yeah, I, you need at least that much. And your site does that, Dave.

**Chris Gammell:** It does that. I like to say my site's really great. And if somebody wants to make an introduction, they can send my LinkedIn page and my website. And that is sufficient to get me a phone call. That's right. And that phone call is where it matters. Yeah. That's great. Right. We, we get there, then I can help. And then, then we can decide if I'm a good fit or not or whatever. You know, that's, that's fine. But sometimes I, you know, I haven't been, you know, I've been doing other work lately,

**Dave Young:** but like I was surprised how willing some people were to work with me. That sounds bad.

**Chris Gammell:** That sounds awful. What do you mean? You're great to work with. Tons of fun.

**Dave Young:** I just mean that like there's, there's no proof point. You know what I mean? Like there might be a lot of stuff out. There's a lot of me talking on the internet. There's a lot of me talking on the camera. Oh, right.

**Chris Gammell:** You could be all razzle dazzle and no, uh, no substance. Yeah, exactly. Like there's no. Cause I got to tell you when I think Chris Gammell, I think razzle dazzle.

**Dave Young:** Yeah. Jazz hands. But I just mean like, uh, I was really surprised at like how trusting some people are generally, you know, like there's like, oh yeah, well I'll know pretty quickly whether or not you are really legit or not, you know? And that does make sense, but I am still surprised that that's a thing. So then, then you think about, okay, so now you don't have to like necessarily build the confidence, but it's really, it doesn't matter what you have on the way. I'm not trying to like poke fun at your website or anything like that. I'm just saying it's all about that. It's, it's all about the, the introduction and like the, the confidence in the person that recommended you.

**Chris Gammell:** Yeah. I I'd say so. And you want to show a track record. Like as soon as you can, if you can get that phone call, if you can talk about projects you've done that are similar, you're usually good. Yeah. Right. Like if you can show track record on doing things that have been similar to that, then it's true. That that's where that's really what people want to hear. And so for me, if I were subcontracting out or if I were looking at helping a class, I help clients find other employees and help clients find other staff. If I'm looking at them, the best thing you can show is like, Oh, I've done this before. Cause then a lot of the pain has already been taken off the table for your next person.

**Dave Young:** Yeah. Right. Right. Yeah. And I think even if it's like a looks like sounds like kind of thing, it's like, Oh, well I haven't done, you know, free art toss on a, you know, a Silicon labs part, but I've done it on an NXP part. Okay. Well, that's yeah. Same. That's going to be like drop in. Yeah. Yeah. Yeah. Yeah. And it is like, it's all these like contextual clues too of like, Oh, they know what they're talking about. And it's not a hundred percent like that, but it, it just is interesting. Like, like the things that actually get people over the hump to like say yes. And to like, to sign that contract and pay your first invoice and like all of these things, like it's been surprising to me as like an overall experience. Yeah.

**Chris Gammell:** Well look at it from the other perspective though, is they've got a, anybody can be a charlatan, whether they're a consultant or an employee or anybody. And so if you're going to get help, you've got to open yourself up to that possibility. And it's like, well, I don't think there's charlatan, but we got to make a decision here. So yeah, let's go.

**Dave Young:** One thing I have counseled younger consultants on as well, cause they're always like, Oh, you know, I'm afraid to bill for this sort of thing or like build this hourly rate. I'm not sure I'm worth it or whatever. I always like go back to the same story of like, like I had a lawsuit against the city I used to live in and I had to hire a lawyer. And I remember like, he charged me 350 bucks an hour and I like looked at that and I'm just like, Oh my God. And then after, you know, I raged about it for a little while and it was, you know, a small engagement was like 10 hours, whatever it was. I, you know, got through it. It was fine. My, my, my only thought was like, if not him, then who, right? It's like, okay, so maybe I go find someone cheaper and that may exist, but they're cheaper probably for a reason, maybe not, you know, maybe there's an inefficiency in the market, whatever, but if not him, then who? And that is basically my entire confidence around my billing people for my electronics work. If not me, then who you want to go find someone else who's cheaper. Okay. That's, that's up for you. Right. But like, if, if you've come to me, you've probably come to me for a reason. My billing rate is what it is for a reason. And if not me, then who, you know?

**Chris Gammell:** Yeah. And if they find somebody who's better value, great. Like I would, I would not suggest anybody hire me over anybody else. If there's a better person out there, because that's not how you're going to, you know, that's not how you're going to do good work. You're going to do good work by helping people find the best solution possible for whatever they got to do.

**Dave Young:** Yep. Yep. So I think the summary of this episode is don't hire Dave and Chris. I think that's what you've been saying the past hour.

**Chris Gammell:** Oh goodness. Unless you want web work and then I'm your guy. I'm your guy.

**Dave Young:** Yeah. Oh Lord. What else should we talk about, Dave? I mean, I know we're at like an hour, five minutes, so.

**Chris Gammell:** Oh, there was one other thing. Oh, we were going to talk about remote and in-person education. Yeah. Totally forgot about that with Blue Stamps. So we had, we had this really interesting situation where we had to go remote for COVID.

**Dave Young:** But why? But why?

**Chris Gammell:** Yeah. So everybody goes home and we had a particularly challenging time pivoting because we're like the antithesis of a MOOC or a course that a lot of people can take. You know, you can't. Right, right, right, right. It's really hard to do this. There's a hardware. Hardware is in the title, you know? Yeah, right. Yeah. And with a four to one student to staff ratio, it's like, oh, how are you going to do this remotely? But, you know, we figured it out and we got there. And, you know, at the end of the day, we put together something much better than we thought. Like we thought it was going to be a stopgap for a year. And it turns out it was a really great program and people had a great time and learned a ton. So that was encouraging. So what about made it, what made it successful? Well, so that stuff I was talking about before.

**Dave Young:** In an era of difficult to, you know, educate, remote education is very difficult, right?

**Chris Gammell:** It is. It's super difficult. And that was the other big lesson we learned is it's not as it's it can be as good for some things, but it's never going to be the same as in person. OK. And so you just have to change what your expectations are and you have to change what you're trying to do and how you're doing it. And that won't be the same. And that's just you just got to accept that. And so once you accept that, then we realize what our core was is, OK, so we like to teach students how to be confident and grow independence. And when they're sitting all by themselves, that is a great opportunity to teach confidence. And independence, like you can do this all by yourself. I can't fix this for you.

**Dave Young:** Yeah, literally.

**Chris Gammell:** I can't. Yeah, I cannot do this for you. You have to do this.

**Dave Young:** Did you implement any specific rules, though? Because I think the number one that I would be is like no breadboards, like no breadboards, no jumper wires, because. Yeah, we did. We did breadboards. You did. Yeah, we did.

**Chris Gammell:** And we still do. But we did limit. So that's one of the things you can't do in person or in remote is you can't have more than 20 jumper wires. So if the project takes more than 20, it's not.

**Dave Young:** Yeah, they're like, I'm doing a Ben Ben Eater type of project where they're building a computer or something. Yeah. The chip is like, no, you're that's not that's not right. That's I got to tell you, that's not a great in person project either. Well, yeah, because one of those wires is going to be wrong. And it's you. Oh, man. Terry, I see those things. I am so impressed by people that do those. And like and Ben's course, too. Obviously, Ben's been on the show and, you know, we love him here. But like, damn, like, damn.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. So it was it was it was a wild ride and still is. And it was it was so good that we thought we'd keep it going. And it's a very compelling program, especially for students that don't have access to it, access to education like this in person, because it is it is hard to find engineering programs like this that give that much latitude and that much freedom and that much attention with that much technical horsepower behind the staff. And so doing it remotely really, really worked out. But it is a great stopgap and it is a great tool. But I think the in person one is you just get to do different projects, get to different stuff. Yeah, it's too bad.

**Dave Young:** It can't be like six weeks of like, you know, remote and then it's like one week intensive in person, you know, like final troubleshooting, you know, final presentation type stuff, you know, like that's there's some like, well, there's some college programs that are like that, you know, you all get in person. And then you also get like the the feel good chemicals of just like being around other people and like seeing things work. You know, that's also there.

**Chris Gammell:** Yeah, there's a thousand ways it could work as like a hybrid or as a split or or something else. We talked at length about about all the different options. But in the end, really what you want is that that, oh, my God, I've gotten in too deep. What am I going to do? I'm scared. So like putting them and putting them in tough. Yeah.

**Dave Young:** Tough engineer.

**Chris Gammell:** That's how you grow resilience. And that's how you go resilient. That's how you get experience.

**Dave Young:** The support piece is also really important. Like, you know, that's yeah, we're there to catch.

**Chris Gammell:** So like when you're ready to punch a wall, be like, well, it's not punch walls about it. Let's let's go for a walk. Let's back up and then let's talk. Let's have a conversation about what's holding you back or what's what's been killing you.

**Dave Young:** Yeah, man, that's really tough. That's it's very impressive you got through that. But are you still offer? So so this obviously summer's over. Sorry, folks. Summer's over. And summer's over. Summer's over. The end of August. Summer is over. School is starting. Yeah. Are you going to keep doing this throughout the school year then or no?

**Chris Gammell:** Not through that? Well, so we decided this year we're going to offer private tutoring. Oh, interesting. So the remote program worked well. And then we we had some students ask us how they could continue. And so it's it's hard to do a program like Blue Stamp without the amount of time that you would have in the summer, especially getting a large group of people that would all have the time during the school year because schedules are so jam packed. Yeah. But this year we're piloting. We're doing a small pilot with like selective number of people who can apply a small pilot on private remote instruction. And so that'd be it would look a lot like an independent study in a college course. So you set a goal and you meet for whatever, how many hours a week you want. And then you would be expected to do some of it with the staff member and some of it independently.

**Dave Young:** That's cool. That's great.

**Chris Gammell:** I mean, yeah, yeah, we're pretty we're pretty excited for it. And I think it's it's for the right student. It's going to give them a huge opportunity like the amount of stuff they can learn, the amount of projects they can get through is going to be big. And that, you know, that that's very helpful for them moving on to whatever the next thing in their life is going to be. That's great. It's great opportunity. But of course, we would never be able to. It would be very challenged to scale that to, you know, 100 or 200 or 300 students. Yeah, right, right.

**Dave Young:** Yeah, because then by definition, that is one to one versus four to one. Yeah.

**Chris Gammell:** Or maybe two to one or something. You know, if there's a couple of friends that want to get together and work on a project and collaborate, you know, there's a lot of options we're kicking around. We're really trying to figure out what works. But the remote program gave us enough confidence to say, like, OK, this is a meaningful impact in this. This is a really great thing to be offering. And we should be, you know, figuring out how we can better reach students.

**Dave Young:** Yeah, that's a good point about the summer carve out, too, though, because like so obviously contextual electronics is, you know, a program that does some remote education as well. And like I'd say like the, you know, the the common people that are coming to the program are often like former hardware enthusiasts now doing software, kind of get back into hardware. Yeah. And it's just like the schedule is the hardest thing, you know, like many of them have families and just like, you know, day jobs and whatever. And it's just like, OK, so when are you going to carve time out here? You know, that is I can't make you do the work, you know, and at least in the summer you have this kind of like chunk of time where it's like this is the thing you're doing versus like nights and weekends. Yeah, weekends is really tough.

**Chris Gammell:** This is your day job. You're going to come in. You're going to make something awesome. It's going to take a bunch of time. Yeah. And we're going to do it. Yeah. Yeah. And it's really helpful. If you don't have the time, you don't have much because in the summer that are the blue stamp program is equivalent to a two semester class in high school. Really? Wow. In the summer. Yeah. Hour for hour. Oh, I see. It's like 140, 140 involvement hours. Yep. Which is about what it would be if you took a class like a two semester math class all year, September through June or whatever it is. Wow. Wow. A bit more doing though too.

**Dave Young:** I guess if you include like homework and stuff though too, right? So, right. Right. Yeah. Homework's bogus though. Do stuff. Build projects. It's great.

**Chris Gammell:** Build projects. So much fun.

**Dave Young:** Yeah. So frustrating. That's really great, man. Yeah. All that frustration just to learn new things. Well, I hope you find some time yourself. I guess that kind of also rolls back to what we were talking about. I hope you find some time for your own independent study.

**Chris Gammell:** Yeah, I know. I know. I know. Yeah, you too. Maybe I'll be ringing you to say, Chris, I want some firmware advice. How do I get the Zephyr thing off the ground?

**Dave Young:** Yeah. Well, let's do it. Yeah. Man, I know one thing now. I can teach you one thing.

**Chris Gammell:** Hey, one more than me. One more than me.

**Dave Young:** That's right. That's right. Yeah, you only have to stay one step ahead of your students. That's right. All right, Dave. Well, thanks for being on the show. I really appreciate it. And it's good hearing from you again.

**Chris Gammell:** No, it's my pleasure. Always a good time. I mean, how many goal points do I get from being on Amp Hour again?

**Dave Young:** A lot. A lot.

**Chris Gammell:** Not as many as the first time, but a lot.

**Dave Young:** Yeah. Yeah. I mean, it's a diminishing return. Where can people find more information about you, your business, and your program?

**Chris Gammell:** Yeah. So the delightful website we were discussing is youngcircuitdesigns.com. Highly recommend you go check that out. Oh, yeah. Very recent blog post, maybe as few as three years old. And then bluestampengineering.com is the education program. Actually, I forgot to mention, we've gotten people to apply for the job of instructor from the Amp Hour recordings in the past. All right. Yeah. Nice. Nice. So, I mean, Amp Hour people are exactly the type of people we would love to have apply. They are, in general, pretty great for what we're trying to do. Great.

**Dave Young:** Yeah.

**Chris Gammell:** Yeah. I'm on LinkedIn. I have a defunct Twitter account, Dave Young EE. Oh, yeah. That thing's dead. It's dead. It's gone. It's gone. But sometimes I go on there and look at what other people like you guys talk about. It's fun.

**Dave Young:** Cool. Cool. Yeah.

**Chris Gammell:** Yeah. That's how to get a hold of me.

**Dave Young:** Okay. Great. Thanks, Dave. We'll talk to you in a couple years, I'm sure.

**Chris Gammell:** Oh, I can't wait. I'll talk to you. I'll talk to you soon. Of course. Think of the cool points I'll get for the next one. Yeah.

**Dave Young:** Yeah. Thanks, man.

**Chris Gammell:** You bet. Talk soon. Bye.

**Speaker ?:** We'll be right back.
