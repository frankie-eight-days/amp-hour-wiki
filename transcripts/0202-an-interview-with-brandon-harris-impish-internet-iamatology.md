---
episode: 202
title: An Interview With Brandon Harris - Impish Internet Iamatology
url: https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/
---

**Chris Gammell:** This is The Amp Hour Podcast, recorded June 9th, 2014. Episode 202, with guest Brandon Harris. Impish, internet, iomatology.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Brandon Harris:** And I'm Brandon Harris from Electric Amp. Hey, Brandon. Thanks for joining us. Thanks for having me, guys.

**Chris Gammell:** Yeah, we're super excited to talk to you because, basically, we're Wi-Fi idiots, to put it lightly.

**Dave Jones:** Wi-Fi is that thing that was developed in Australia, wasn't it?

**Chris Gammell:** Yeah, right, right, right. That's all I know. If someone walked up to me and they're like, hey, I need you to really get this thing onto the internet and do it quickly, I'd probably run away.

**Dave Jones:** No, you just buy one of the doodles of off-the-shelf modules. Come on, be proactive, Chris.

**Chris Gammell:** Yeah, no. But the thing that's interesting to me is that there's a lot of companies out there doing modules, but the software side as well. So, you know, it seems like Electric Amp is really doing a lot of that and making it easier to get hooked up and started and everything else.

**Dave Jones:** For a dummy like me to get onto the internet, you know, I can do the hardware side of things, but, you know, and I can choose any module. I don't care about the hardware. I care how easy is it on the software side for an idiot like me to have my microcontroller spitting out data to the web or wherever I need it to go.

**Brandon Harris:** Yeah, so that's kind of exactly what we were founded to solve. You know, our founder, Hugo, was doing your standard hobbyist project. He wanted a set of lights in his bathroom to go green when the Apple stock price was up and red when the Apple stock price was down. And he did what, you know, sort of your average hobbyist does and goes, went and bought himself an Arduino and a, you know, a Y-Fly shield and got it all started up. And he, you know, was spending nights and weekends getting it going and figured out, you know, a Yahoo feed where he could pull down XML and he's parsing the XML on his 8-bit microcontroller. Which is something, you know, a lot of people have had to do before. And it's something that's a really awful experience.

**Dave Jones:** Yeah, I know. You could waste weeks on that. That's the thing. That's the demoralizing thing. Like, you know, as a developer, you might go, I don't have time to do that. Jeez, I can't spend a couple of weeks dicking around with, you know, a module and parsing XML and getting data out and all that sort of jazz.

**Brandon Harris:** Right.

**Dave Jones:** It's fine if you've done it before and you're sort of, you know, your mind's in place to do that sort of thing. And you can probably do it quite fast. But, you know, if it's your first shot at it, it's going to be bumbling around.

**Brandon Harris:** And the problem is even then, it's like, you know, you do that for one feed and you get it parsing XML and then, you know, they drop XML support and now you need to do JSON. Right. And you throw the whole lot out the window. Yeah. And you just decide it's not worth it. Yeah. So, you know, while we do make our own hardware as well as partner with other hardware makers, a lot of what Electric Imp is really about is the service. And it's really, it's, you know, I like to think of it more as an internet module than as a Wi-Fi module. Because getting on Wi-Fi isn't that hard. There are lots of modules out there. You can connect to Wi-Fi and you say, okay, great. Now what?

**Dave Jones:** Now what? That's it.

**Brandon Harris:** You know, right? It's like, are you going to be parsing, you know, JSON on your microcontroller? How are you going to update your device? Because it's going to have bugs. What is JSON? It's connected to the internet. JSON?

**Dave Jones:** Yeah.

**Brandon Harris:** So, JSON is a JavaScript serializable object notation. I'm almost certainly completely wrong on that.

**Dave Jones:** And we've learned something new, I think.

**Brandon Harris:** Well, I knew what JSON was, but yeah. JSON is just a structured data format. So, it's a way, you know, like XML, it's a way of passing data between different devices. So, you know, it's nestable and it's phenomenally complex, but extremely powerful. And actually, once you have a good JSON parser, great to use. You know, it aligns with like lots of the program structures that we think of when we think about higher level sort of object-oriented languages of being able to nest things and having keys and values and things like that. So, I should also mention that I am a hardware engineer. Yes. And moonlights of it. One of us. One of us. He just happens to know more than the average bear, it seems like. Yeah. But, you know, you pick up a lot when you surround yourself with smart internet guides. Right. Yes, yes. Blah, blah, blah. Object-oriented. Yada, yada, yada. Yeah. Yeah. Yeah. So, our whole idea is that we basically handle everything from, you know, basically you get a, your device has a URL that only you know. And then you can actually use that URL to interface with it. Right. So, you know, you can have a device that literally serves up its own webpage. You click a button on the webpage and that sends a message down to the device and turns on an LED.

**Dave Jones:** Got it. Is this something you can run on your own server or do you get the URL on your website? I say this because I don't want to jinx you or anything, but hey, what if you guys go out of business or something or your website's flaky or something like that? How does that all work?

**Brandon Harris:** I mean, that's a question we get a lot, right? Right. And one of the things you have to think about in this day and age, right, there, as things become more and more interconnected, it becomes more important for, you know, the services. And as people start using more services, it puts them at greater risk that one of those services goes away. Sure. But so right now we only offer it to run through our servers and, you know, we have good funding and we expect to be around for a long time.

**Dave Jones:** Are you guys running your own servers or do you like shop it out to Amazon or something like that?

**Brandon Harris:** Yeah, we shop everything out, right? Right. Of course. Yep. We don't want to, we're not server maintenance people or things like that. Yeah, that's close. After all the hard work on the software. Right. And actually, I mean, it actually lines up kind of well that, you know, we sort of have positioned ourself as sort of the AWS of IoT connectivity, right? Whoa.

**Dave Jones:** There are more acronyms in there. We're going to have to take a second here, Brandon.

**Brandon Harris:** We need to take a moment of silence for the, yeah. I know. This is what happens when you get prepped by marketing, guys. Yeah.

**Dave Jones:** You know.

**Brandon Harris:** If you say IoT 14 times, you get a bonus. So, so funny story. We actually, one of our, my colleagues, Yenir, literally built an IoT device as in I-O-T-E-A, which is a power sensor that hooks up to the electric kettle in our kitchen. And, and ding, and, and has, we have a sign up in the office that goes red when the, the water is ready and hot because the, the kitchen is far enough away you can't hear the ding. Nice. So, that, that was, that was the first IoT device. Nice.

**SPEAKER_01:** Oh, goodness.

**Brandon Harris:** Yeah, but puns aside, yeah. So, we like to think of ourselves as, as the Amazon web services of the Internet of Things.

**Dave Jones:** That's guaranteed to get investors moist at that.

**Brandon Harris:** Well, so the idea is that like nothing Amazon does is things that you couldn't do, right?

**Dave Jones:** Oh, no, but they do it on such a scale that, you know, you'd be stupid to even try.

**Brandon Harris:** Right. So, that's exactly what we do. We've, we've shipped coming up on half a million connected Internet modules. Nice. Right. So, we know how to maintain links. We know how to navigate firewalls. We know how to get on. You know, I mean, like one of the things is just routers in homes have bugs in them, right? You know, things that are specifically forbidden in the spec for Wi-Fi, some routers just implement, right? Like, oh, zero length password. Sure, I'll accept that. Yeah.

**Brandon Harris:** Yeah. So, you know, things like that, that we get to test and, and it's the sort of thing where it'd be, it's, it's somewhat unfeasible for an individual smaller company to try and collect all that data. And, but because we've been shipping and because we're tested on so many different networks in, I've forgotten how many countries, 30 or 40 countries around the world, it's, we get this tremendous exposure and we're able to aggregate all that information and do it exactly like you said, on a scale that we think anybody else trying to do is, is foolish to, you know, to not leverage that, that learning we've done.

**Chris Gammell:** Can you see, so you said a half a million devices that are out there right now. Can you see like, so those are driving regular traffic back to your servers as well. Like you can see all that analytic information, like when someone turns a light bulb on kind of thing, or how does that all work? And I don't mean like in a creepy way either. I mean like an aggregate, you know, like just like how many devices are active and all that kind of stuff.

**Brandon Harris:** Yeah. So, so, I mean, we, we have a sort of active device counts and things like that. A lot of the devices are not continuously connected because one of our, our core areas of expertise is, is power management. And if you want to do something on batteries with wifi, typically what that means is turning off wifi and going to a sleep state when you're not doing anything. Um, you know, so, uh, there's a, a Budweiser hockey light, uh, that's sold in, in Canada, uh, and basically wakes up for, you know, you set, you set whatever your favorite team. Um, and then, uh, it only turns on during the game, uh, and basically notifies you when your, your favorite team scores a goal. Um, and because they're, they run off of, uh, batteries, they don't want wifi on all the time. So, you know, we, we do see like, you know, when, um, the more popular hockey hockey teams, uh, have a game, we get a little, our server of, of connections, which is pretty funny.

**Chris Gammell:** I'm just impressed that Budweiser can sell anything in Canada, uh, to be honest.

**Brandon Harris:** Well, so, so yeah, they, they, they sold like hotcakes. They, um, they announced it during the, uh, Superbowl last year. Um, I was actually the, the first product to, to ship, uh, the first commercially available product on our platform. Um, and it's Canadian hockey fans, right? And, you know, it sort of points out that like, we have this notion of like, you know, internet connected devices as being a very nerdy thing. Yeah. Right. And that's, that's really because of our imagination is bad. Right. Right. Somebody else imagined a different use for it and made something that's really desirable and isn't nerdy in any way.

**Dave Jones:** And, and your average Joe looking at that thing or buying that probably wouldn't even know or care it connects to the internet or has heard of the internet of things terms or anything like that.

**Brandon Harris:** Absolutely.

**Dave Jones:** Yeah. So would you say that his, his the million dollar question probably should have left it to the end, but we'll throw it in now. Would you say that an internet of things company is, is like, you're probably pushing the brown stuff up the hill with a pointy stick. If you're trying to make a real big business out of just selling hardware is, is the software, everything like the hardware is almost pointless getting into it. It's, it's the software side of things that is ultimately going to make you successful and make you money.

**Brandon Harris:** Yeah. I mean, right now where we are, software is king. You know what I mean? That's, that's something that you don't have to look any further than Arduino, right? It's not like an Arduino processor is better.

**Dave Jones:** Hardware is nothing. The hardware is just the same hardware that's been around for 30 years. It's no big deal. Right.

**Brandon Harris:** Yeah. It's, it's all become so commoditized. Yeah. And so really you're right. It's, it's absolutely, it's about software and about creating compelling user experiences. So one of our.

**Dave Jones:** Another buzzword. Jeez. People's bingo sheets are going to be full after today's episode.

**Brandon Harris:** Yeah. So I.

**Dave Jones:** I've, I've heard that so many, I've heard that term so many times from people who run startups, you know, it's a need, a compelling user experience or something, you know, like, is there some playbook?

**Brandon Harris:** Well, you hear it a lot when you're living in Silicon Valley, you know, eventually people shout things at you long enough. You start repeating them. No, so it's, it's, the point is that, you know, one of the things like you look at some of this early successful, um, internet connected devices, uh, like the nest, right? The nest was, you know, the, the internet connectivity was only part of the story, right? It was about a beautiful design and, you know, um, sort of selling this as a premium product and, and, and a whole package. Um, and that's where people are, you know, I think there's a lot of interest in that these days where it's like, you know, people want to feel good about their devices. They want to have some sort of, you know, positive relationship with them, you know, much in the same way that, you know, that's happened with, with the phones. Like people feel like, you know, if they, they go to work without their phone, they feel, you know, naked often feel lost. Yeah. Um, and I think that's going to start happening with more and more things. Interesting.

**Dave Jones:** I, I came to the office this morning without my watch. Oh my goodness. I cannot go out with there without wearing a watch. It bugs me. I feel naked. I, yep.

**Chris Gammell:** Is it a pocket watch because you're like an old person? Uh, yeah. Yeah. Who has watches anymore? This is, this is my, sorry, a couple of guys. I'm just, I, I, I still don't understand the watch thing.

**Dave Jones:** I don't carry my phone. Well, you know, like if I go out without my phone, oh, whoop-dee-doo, you know? Like, but my watch, no way. No, it's just got something I've got to have on my wrist, you know?

**Chris Gammell:** And I think that, that does point to what a lot of people are trying to do with, you know, like you said with the experience, Brandon, like the people are trying to craft these have to have kind of things. And of course, have to have means you have connect, connection and everything else. So it kind of, uh, how many of your, your, the companies that are using electric imp and stuff like that? I mean, are they outside of the realm of being able to hire people that could do this kind of stuff, or is it just more of a business decision where they say, well, we want to prototype quick and then we want to be able to also push that product to production, or is it something else entirely?

**Brandon Harris:** Um, so some of both, um, you know, for, for some things, you know, smaller, smaller companies, we have, um, companies that are shipping in the few thousands. Um, and for them, they, they just simply couldn't justify the cost of doing all the development themselves. Um, you know, I mean, just, just getting, you know, it, you know, a product FCC certified can cost 10 grand or more, right? If you're only making 5,000 of something, you're, you can't be wasting your time with that. Um, so, but you know, it really, it's about the fact that they also don't have the expertise, right? Um, you know, one of them is a toy maker. They don't, they don't know about wifi. They don't know about networking, right? They, they just knew that they wanted their toys to talk. Um, and, and so that's really what we, we were able to bring to the table for them for some of the larger customers, you know, where it's, um, you know, maybe, maybe more, they can amortize the development cost across, um, more products, you know, there, a lot of it is, it's time to market. Um, you know, you look at, uh, quirky and, and they're able to bring, uh, internet connected devices using our platform to market incredibly quickly. Yeah. Um, and, and for them, that's, that's the real value. Um, so, you know, that, that yes, you know, they, they could develop some of those resources in house, but again, you know, they're able to leverage, you know, we have other large customers and every customer gets the bits, um, as the platform grows. So we have a really positive networking effect right now that, um, you know, really helps, helps all of our customers, um, every time, uh, the platform grows.

**Chris Gammell:** Let's dig into a little bit, like, like, uh, tell us about the, I mean, tell us about the hardware and then, you know, what it would take to get dummies like Dave or I up and running, hooking up our DMMs to wifi or hooking up bench buddies to wifi, that kind of thing. What, what would it really take and how long, how long would it take?

**Dave Jones:** I, hang on. I just want to say how amazing it is when, you know, I've been working in the electronics industry for more than 20 years as a design engineer and here I am being called a dummy.

**Chris Gammell:** I call you a dummy every single week, Dave.

**Dave Jones:** This is, I know, I know. This is how, you know, this is how the landscape has changed. You know, yeah, this is how the landscape has changed. I just find it remarkable. Sorry, go on.

**Brandon Harris:** Yeah. So, so, I mean, fundamentally at its core, you know, just to, to give you a little idea, idea about what, what the imp hardware looks like. Um, it's, uh, a, a Broadcom wifi chip. This is the same wifi chip that's used in iPhones and other kinds of smartphones. Um, plus a STM 32, uh, Cortex M3, uh, arm microcontroller. Um, do you need that 32 bit, um, power? Uh, or is there some other reason you chose it? Um, so to some extent we, there, there certainly are people that have done it with, um, you know, we have, we have a pretty powerful microcontroller. Um, if you're doing TCP IP and holding lots of buffers and, and actually one of the, the other big things is we, we do all of the encrypt, you know, every single packet we send is encrypted. Um, so when you start getting into that, that's, that's pretty serious, uh, CPU.

**Dave Jones:** Yeah. Can't quite run it on an eight bit micro. Can you, you probably could be to be dog slow.

**Brandon Harris:** Yeah. Uh, well, and the other big thing is you, you know, it's, these things always, you know, it's never like, well, you get a really good processor and no memory or lots of memory and a really bad processor. Right. Some of it is, well, we needed the more memory. So you get a faster processor. Uh, and, and one of the big things that's, that's different, um, from a hardware, well, from a hardware perspective, um, that's different between, uh, an imp module. And, uh, most, uh, wifi modules is, uh, many wifi modules are just intended to be basically a wifi modem, uh, where you just talk serial commands to it. And so it doesn't have to have a lot of onboard memory or processing or anything like that. We actually let you write, um, hosted applications that run entirely within the imp, uh, on that arm microcontroller. And because we have a more powerful microcontroller, we're able to let you do that in an interpreted language. Um, okay.

**Dave Jones:** What? You've got your own language?

**Brandon Harris:** So it's, it's a squirrel. Yeah. Squirrel.

**Chris Gammell:** Um, around the office a lot. The, the thing from up that movie.

**Brandon Harris:** Uh, yeah, it was, it was, so we actually started, um, right. You know, back in the very early days, we were using a, a language called Lua, uh, which is used in, uh, gaming engines. And Keithley DMMs. I've heard of that. Keithley, uh, smooths actually. Yeah. So it's got kind of these like strange applications, but, um, what, what's great about, um, both Lua and Squirrel is they both, um, are designed to be relatively efficient because they're designed for, uh, writing plugins for games. And so they have to have relatively high performance. So we're actually able to compile them into something reasonably efficient for a microcontroller. Interesting. Uh, but, uh, the, uh, honestly, the reason we switched from, uh, Lua to, um, Squirrel was, uh, Lua stores every single variable as a double.

**SPEAKER_01:** Oh.

**Brandon Harris:** Uh, and, and has no arrays. Yep. So an array is really just a table with a numerical index, which means you want to put bytes into an array and you're taking eight bytes per entry. Yeah. Ouch. Yeah. It's, it's a, it's a pretty big overhead. Uh, Squirrel doesn't have that. Um, so, you know, we, it, it's an uncommon language. It's actually syntactically very similar to JavaScript, um, which actually fits our platform really well. It's, you know, um, it's odd because, uh, you know, as a hardware engineer, I'm used to coming at these, you know, I think of this as coming at it from a hardware solution. But in fact, a lot of what we're seeing is, is this is really a way of, uh, the, the software and the web guys invading the hardware space. Um, so, you know, we have, we have guys who, who are used to writing web pages who are all of a sudden writing embedded device code. Right. Which is terrifying to me. Yeah.

**Chris Gammell:** So is it cool with like 64 megs of memory to flip this LED on or is it like, should I go higher? Is it like four gigs? Yeah. 20 like four gigs or so? Sorry, software folks.

**Brandon Harris:** Um, yeah, I, you know, it's, it's funny. Like, I feel like every day I, I work here, I, I make, uh, myself less needed. Um, you know, I mean, ultimately that's, that's kind of the, the, the goal of any good hardware engineer, right? Is, right. Is like, you never want the software guys coming to you. Right. It's like, that means you did something wrong.

**Chris Gammell:** Also from a business perspective, uh, teach a man to fish and you lose a wonderful business opportunity.

**Brandon Harris:** Yeah. Um, so yeah, so the hardware is, is, um, pretty straightforward. Um, you know, we have the, a nice beefy processor on there where we, it means that you're, you're writing an interpreted language. One of the great advantages of that is that basically we have a lower OS layer that handles all of the connectivity, the encryption, everything else. And basically it's, um, you know, our goal is to, to build a platform that's so stable that no matter what a user does short of, you know, uh, blowing the thing up physically. Uh, they can't break it with software. Right. So this is again, that's, that's the other goal of the, the hardware engineer is to over engineer things such that no software engineer can ever break it. Sure. Somewhere out there, there's a software engineer saying challenge accepted. Yeah. Uh, yeah. The, the, the, the number of engineering hours I've, I've spent, you know, trying to make sure that the software guys don't break my stuff is, is substantial.

**Dave Jones:** At what point did you, you, I mean, you quit switching languages like this is a huge deal, not only to you, but to the user and the product. At what point did you decide to do that? And does it leave everyone previously who came up to speed using that language now, oh, you've dumped it, go to something else. How does all that happen?

**Brandon Harris:** We, we actually switched from Lua to squirrel, uh, one week before we launched the product.

**Dave Jones:** Um, so thankfully, yeah, no, um, uh,

**Chris Gammell:** That sounds like a great decision overall. Yeah.

**Brandon Harris:** Uh, so, so literally I was, we had, you know, we were ready to launch.

**Dave Jones:** Was that a big gamble though?

**Brandon Harris:** What's that?

**Dave Jones:** I mean, was that a huge gamble? I mean, just a week before launching. Yes.

**Brandon Harris:** Switched to another huge gamble.

**Dave Jones:** Um, was it something that the other one was just so bad? You thought if we don't do it, we're, we're just going to fail.

**Brandon Harris:** Yeah. We're just going to, it really was. Okay. Um, so, so what it came down to, and this is, this is one of those things that like, you know, where it's just like, you just don't learn except by doing. Um, so we, we had, you know, we, we launched, uh, we announced the product one week before, uh, Maker Faire 2012. Um, and so Maker Faire was going to be the first public, uh, exposition of the technology. Um, and so we were building all kinds of demos to sort of show what kinds of devices could be, could be connected. And so one of the devices I built was a, uh, a 16 by 16 RGB LED sort of, you know, display. Um, just made out of, you know, the, the strips of, of, uh, LEDs you can buy off of, uh, Adafruit or, you know, Poly Express, et cetera. Yeah. Yeah. Um, and literally that, that's where we found out this nice, uh, feature of Lua that, that arrays are so inefficient was I was trying to animate the display and make it do things. And I kept running out of memory and, you know, we have 128 K of memory and, you know, how about half of that was at the time was used by the operating system. Um, and, and all of a sudden I'm spinning up 60 K of memory to store, you know, a few kilobytes of data. Um, and, and that was, that was a big, a big aha moment for us where, you know, we, we just, we just said, that's it. You know, that's, that's a deal breaker. We, we can't live with that level of inefficiency. Um, and you know, that was, that was on a Friday and Hugo, our CEO and our embedded team. Um, like just spent the weekend researching stuff and, um, found squirrel, which was, was actually, um, I believe originally written sort of as a alternative to Lua. Um, because of some of the frustrations with Lua and some of the weird syntax with Lua. Yeah. And it, it was a tremendous gamble. Um, I, I'm quite frankly, just absolutely amazed that it worked, but it was, it was one of those things that like, you know, you know, that, that once there are users on the platform, you'll never be able to switch. And you're going to be living with that bad decision from forever. And I think ultimately we would have delayed the product rather than ship it, uh, with, with the wrong choice of language.

**Chris Gammell:** Yeah. That's, well, I mean, it seems like it's been working out since, right? I mean, so, so what is the reception then when you, when you go to, you know, when people start up, then is it like, what is this? Or is it just like, oh, this is what I have to do in order to get, uh, you know, uh, what'd you call it? AWS for IOT. Yeah.

**Brandon Harris:** Um, so, so it's actually, it's, it's, uh, it's some of both, right? Some of the, some people come at it and especially people who were thinking of this more as a webpage, right? And they can do sort of, you know, JavaScripty like things. And so if they have, if they're, they're coming from the website, they absolutely love it. Right. They don't want to have to be writing C, uh, you know, and, and doing while one loops is like, they're used to being event driven and callbacks and things like that, which is very hard to do on your average microcontroller. And that's what squirrel is like all about. Um, it, and so for, for the, the people who have the hardest time with it are the like, you know, really old school, like, you know, I've been programming, you know, microcontrollers since the seventies. The peak and poke guys, huh? Yeah. And, and, and so like, that's, that's kind of one of the hardest things, you know, we're, I don't want to, you know, dump on that crowd at all because, you know, I think they do great work. Um, but, but one of the, one of the great advantages for us is, you know, a lot of the companies that are really on the cutting edge are, uh, you know, more flexible. The, the engineers are, um, you know, from a newer background and, and they, they started learning, you know, they didn't, their first language wasn't C or assembly. It was something higher language and they're writing in, you know, Python or Ruby or JavaScript, uh, as one of their, their main languages. Um, and so for those guys, it, it makes total sense, right? Once they get over, like it's named squirrel, but it's basically JavaScript. Right. Um, yep. Then it's, it's, uh, a really excellent, uh, tool for them.

**Dave Jones:** Well, I found that those people bought up on those sort of languages, they can switch really easy, you know, from JavaScript to Ruby to Python or whatever it happens to be. Uh, they, they, they just seem to pick it up really easy.

**Brandon Harris:** Yeah. I think that's, you know, um, one of the things that, that has happened, um, and especially it's also, it's also just a requirement, right? I mean, you know, if, if you started programming way back when C was the language for so long that you just, and you had so few resources, you had to really understand the, you know, the physical level. And now, you know, your average, you know, uh, programmer doesn't actually understand what's being executed or how it affects the computer, but they know how to get things done. Right. They know how to read API documents. Yeah, that's right. Yeah.

**Chris Gammell:** So what's that memory made out of again? It's like some kind of semi conductor. Yeah.

**Dave Jones:** Uh, and, and, and that's why they often make guys like, you know, hardware guys like us look like fools these days because they're so good at getting the job done. You know, whereas we're dicking around with hardware and in our old mindset, you know, that.

**Chris Gammell:** I think that also means that Brandon is always going to have a job if he wants one too, right? That's what happens. You abstract out these interfaces. And then when there actually is a problem, then that becomes all the harder to actually go and dig down and solve it. You just hope that like Brandon saying, you know, you kind of work yourself out of the system by fixing all the hardware. Right.

**Brandon Harris:** Yeah. I, I mean, I think it's, it's, it's actually great. And even as a hardware engineer, right. I'm also aware that, that I have to be, you know, that in this day and age, it's like, that's, that's just sort of what's required. Um, where you're not going to be sitting down and working on one project for three years. Um, you know, in, in the last, uh, two years here at electric amp, I've worked on, uh, you know, 20 or 30 different designs. That's awesome. Right. It's like, I mean, there was a point in time back in, in the, in the beginning, I was fabbing out a board every two weeks. Nice. Um, and I got into the cycle where I could, you know, I got a pipeline going where it was basically, I could do a design in a week and then I would, I would get back my previous design, validate it in a week and then move on. Um, you know, and, and, and a lot of that is because the, the electric amp hardware is so, uh, powerful and well-tested and the software for it is so easy. You know what I mean? I was writing whole new device drivers in, you know, a few hours, uh, which is just, you know, kind of unheard of. And it, it makes, it makes the hardware so much more fun because rather than saying like, oh, well, what can I find software for? I say, wow, I don't care. What can I buy on SparkFun? Um, you know, what is cheap and digi-key and I just throw it down. And it's like, if the data sheet's reasonable, you know, we can get, uh, simple device drivers up and going in, you know, a few lines of code and, um, you know, a couple afternoons of work.

**Chris Gammell:** Uh, so when you say like device drivers, you mean like, you mean like, uh, having like an ADC or some kind of, some kind of external device where you're actually peeking or you're throwing stuff at the registers, reading back from the registers, just simple stuff like that. But then you get to write, then you have like a webpage where you go and you just access that kind of thing. Is that what you mean?

**Brandon Harris:** Yeah. So, I mean, like, you know, a good example was, uh, you know, we have a, we use accelerometers and a couple of designs and just something as simple as figuring out how to do a free fall detection. Um, so I had a little design, I had a, an accelerometer and some two AA batteries on it and an it module. And it would, uh, wake up when you, when you tossed it in the air, it would wake up, connect to the internet and go back to sleep before you caught it again. Oh, that's fun. Um, which is pretty fun. I mean, you know, and it was, it was silly, but it's like, well, all right, you know, how, how hard is it to, to figure out how to do a free fall detection? And, and because there's, you know, the I2C and everything else is all built into the operating system, you know, you're not faffing about with, you know, read, read this register, then set this register, read this register and set this register. Um, and, you know, power management is, you know, literally going from, uh, offline in deep sleep to online connected to the internet, sending data and back to sleep as, you know, a few lines of code. Um, right.

**Dave Jones:** So how long does it physically take for it to go from sleep to fully connect, to sending something out to the internet to shut him back down? How quickly can it actually do that?

**Brandon Harris:** So, uh, interestingly enough, the slowest thing in the entire path is the local DHCP server.

**Dave Jones:** Right.

**Brandon Harris:** Um, and, and so, you know, like typically.

**Dave Jones:** Well, yeah, it's a freaking server. I don't know. It's got to do server stuff. Right.

**Brandon Harris:** Okay.

**Dave Jones:** I, I, you know, I don't know what it is.

**Brandon Harris:** So there's a, there's a lot of steps that go into actually connecting and things like that. Um, you know, here in our office, we've got real fast internet. We have a nice beefy server or things like that. We can actually connect, send data and get back to sleep, uh, in a little under a second, sometimes, you know, just over, but about a second. Um.

**Dave Jones:** Well, yes. See, to me, that's quite long. That's quite lengthy.

**Brandon Harris:** Yeah.

**Dave Jones:** You know, but hey, if you're running a DHCP server, then that, that is, that is what it has to be. Right.

**Brandon Harris:** Right. Um, you know, and, and it's, there's a lot of things going on there, right? You know, you've got a lot of. Of course. Yeah. There's a lot of steps and getting an IP address and, um, things like that can be, uh, you know, just getting on the network and things. So.

**Dave Jones:** But of course that's all hidden from the user. You can just do it in two lines of code, wake up, send something, go back to sleep. Yeah.

**Brandon Harris:** Absolutely.

**Chris Gammell:** Yeah. So do you guys have any interface hardware, uh, outside of that then to kind of speed up that process and kind of like cue it up? So it's like, wake up, talk to some intermediate device and then, and then, you know, don't have to talk directly to a router type of thing. Or is there, is it always going to be through, through a wifi gateway like that? Is that always going to be the main thing?

**Brandon Harris:** Yeah. So it always, you know, our model is generally, you know, at the point where you're connecting to the internet, you're not that time sensitive. Um, and, and right. So if, if it's, you know, more often than not, it's actually the, the sequence is actually wake up, capture an event and then connect to the internet and send the event up. Um, right. So, so we can wake up and, and, uh, start measuring things and running code. Um, and I think we're somewhere around 50 milliseconds, which is longer than you would have for your average hardware. But considering that's bringing up an entire OS, uh, starting a, uh, VM and then executing your interpreted code inside of a VM. Uh, that's pretty quick. Yeah.

**Chris Gammell:** What, what, uh, do you guys run all that? It's, it's, it's not open, I'm guessing, but what, what, uh, OS do you guys use on there?

**Brandon Harris:** So it's, it's a, um, heavily modified version of ECOS. Oh, okay. Yeah. I've used that before. Yep. So, uh, you know, at this point it's, it's basically imp costs at this point, right? Yeah. Um, and, and to the point where we actually refer to it as the imp OS, because there's so much stuff in it. That's, that's so heavily customized.

**Chris Gammell:** Yeah. Well, that's good. I mean, that's what you do for custom getting, getting good power and stuff like that.

**Dave Jones:** Mm-hmm. From the hardware side of things, as a, as a user of this stuff, what hardware interfaces do you have on this module? Does it have just digital inputs? Does it have ADC inputs? I squared C, SPI? Yeah. So what, how can I hook my stuff, my sensors up to your module?

**Brandon Harris:** Uh, I love this question because, um, yes, all of it. Um, no, so, so we're, um, we're, we're very fortunate. The STM 32 has, uh, really great, uh, peripheral options. Uh, and then on top of it, what we actually did was, um, because we're, we were limited by the number of IO, sort of useful IO pins that we could bring out. Um, because the first generation was actually in an SD card form factor, which limits you to six, uh, six IO pins in total. Um, the second generation soldered down module that went from six to 12 and the third generation M003 module goes from 12 to 23.

**Dave Jones:** Um, so, uh, are you still selling all of, all of those different hardware platforms?

**Brandon Harris:** Yeah.

**Dave Jones:** Or have you, yeah. Right.

**Brandon Harris:** So they're, they're all intended for, for sort of different users. You know, the SD card is, is phenomenal for prototyping. One of the great things about it is, you know, basically then sort of the more expensive, you know, from a hobbyist perspective, the more expensive wifi part can be removed from a project. So you just buy a breakout board, you stick it in and, you know, basically you think of it as sort of in the same way you would your Arduino and the shields, right? You can take the Arduino off and leave your shields all hooked up to, uh, whatever it was you had and, and move that, that card around. Um, the, this solder down, the second generation solder down module, um, is great for, uh, customers who don't have a lot of RF experience. It's got an integrated antenna, things like that. Um, it's all on board. You just plunk it down and give it power and it's online. That's it. Um, and then the third generation is, uh, intended for customers who have more RF experience. It's a lot smaller, a little bit lower cost, but with that, with that cost down, um, you know, there's, you have to put down some external RF. You have to provide your own antenna. Sure. There's, you know, so it's, it's kind of a tiered architecture, um, for different customers.

**Dave Jones:** So with the, with the SD card, you've actually, it's physically the size of an SD card and you've got the wifi module built into that. Yep. Now I was, I was gobsmacked when I think the first company to do this was the, uh, was the iFi card, which you put into your camera. It's saved images, just like an SD card, but it, you know, transmit and everyone, like, I just went, wow, you can fit a, a wifi module into an SD card. How the hell are they doing that? Is it that hard these days? I assume it was hard back when they did it. Cause they were the first to do it.

**Brandon Harris:** But, um, I mean, if you, if you're wondering like the size of the chip versus the size of the SD card, it's no, it's not hard.

**Dave Jones:** Right. No, but you've got to have an antenna. You've got to have a wifi antenna in there. You're like, you've got to have the wifi antenna in there and you've got to get the performance.

**Brandon Harris:** Our antenna takes up like a third of the total area, uh, on the card. Um, and you know, so that's significant and you're getting a processor plus, plus a wifi module in there. Um, you know, the i5 is, I actually think the i5 might've been a little bit more challenging because it, it had to have, um, it also had onboard NAND storage, uh, which is physically large.

**Dave Jones:** It had to have a huge die on there. Yeah. It had to have eight gig or something worth of die. Right.

**Brandon Harris:** So, you know, so we're lucky that we just have to put down our tiny little STM 32. Yeah. Um, actually the biggest, the biggest issue with it was, uh, is actually thickness. Um, the, the area is not a package.

**Dave Jones:** Which do you use? Are you doing, uh, just bare die? Uh, are you doing flip chip or what?

**Brandon Harris:** We, we use, uh, just CSPs. It's the, the off the shelf. I mean, you know, one of the things is, is as well as a startup, you don't have access to, um, you know, a lot of the, the, no, no chip manufacturer is going to make a custom package, uh, just for a startup. Right. So we had to buy things that we could get off the shelf that were already being used in high volumes. Um, so we just use the CSPs and, and the relatively thin. And we, we did have to be, uh, very aggressive on our PCB thickness. Uh. I was going to say, what are you using? 0.3 millimeter PCB? Uh, it's even less than that. It's a 0.24. It's a 0.24. It is, it is, uh, not stiff. They're incredibly flexible.

**Dave Jones:** If you've never.

**Brandon Harris:** Yeah.

**Dave Jones:** No. For those who haven't actually played with a, a large, uh, you know, a large size, you know, 0.3 millimeter or something PCB. They are ridiculously flexible. What's your, what's your ruler? They are almost flex boards. What's, what's your. My ruler is, uh, 0.5 millimeters. Okay. Yeah.

**Chris Gammell:** That's a good reference point for a lot of people. I'm sure. The PCB.

**Dave Jones:** Well, it was a point. Yeah. I mean, the, the, the standard one is 0.8. Yeah. And most manufacturers will go down to 0.5, but anything under that gets a bit more special. They're almost down to the point where they're not a regular PCB. They're actually designed as the pre-preg material, which goes in multi-layer boards.

**SPEAKER_01:** Huh.

**Dave Jones:** So they're actually, you know, rather than just like a stock thickness board, they're actually using the, just one internal layer of a multi-layer board for you. Wow. That's pretty much what they end up doing. They are so flexible.

**Brandon Harris:** And the other, the other, um, big challenge on it was actually as well, it was, you know, we wanted, uh, white plastic instead of, you know, your traditional black or blue, or in case of iFi and orange. And it turns out, um, white plastic is a lot more transparent. Uh, and so the very first, uh, generation, you know, the first couple of runs, the white plastic was so thin, you could actually see parts through it. See, that would have been cool to me.

**Dave Jones:** That's awesome. Yeah. I know. Yeah.

**Brandon Harris:** That's awesome. The problem is it also gets really brittle at those thicknesses. So we ended up having to thicken it up and find something that was a little more, uh, flexible, you know, didn't, didn't become a lot of brittle. And, and yeah, I mean, there's, there's, um, uh, challenges like that. Um, you know, and even, even we were looking at, uh, you know, we had to put our logo and FCC ID or information on there and things like that. And we literally didn't have enough room, uh, enough Z stack to fit a sticker. Um, right. The sticker would have put us over, over thinness. So we had to, you know, laser etch everything on. And, you know, that's, that's another advantage of, of having white plastic is you can just laser etch the logo on it and it looks really nice. Yeah.

**Chris Gammell:** Nice. Which it is a fun little logo too.

**Dave Jones:** That's a, so how do you make these SD cards? Are they like, uh, do they come as two case halves and they're, uh, fused together? How do you assemble an SD card? I've never actually looked at the details. Yeah.

**Brandon Harris:** So it's, it's, there's some retaining clips and, um, a little bit of adhesive, uh, pressure sensitive adhesive inside of there to sort of hold things in place until, um, basically until they go into an ultrasonic welding machine. Um, right.

**Dave Jones:** So they do ultrasonic. Yeah.

**Brandon Harris:** And then it's just ultrasonic welding all around the, the edges. Um, and that, that's actually a very important step because it's, it's what gives, uh, the entire thing, the rigidity because the PCB is so thin and the center plastic is so thin that your structure actually comes from that outer ring of ultrasonically welded plastic. That's pretty cool.

**Dave Jones:** Got it. And who, and who has to assemble this for you? A, an SD card manufacturer who specializes in that or can there's some sort of assembly house?

**Brandon Harris:** Uh, so, so we work with, uh, a, a factory in China, um, to build them.

**Dave Jones:** And so we brought a factory in China. That's how it goes. Um, you know, there's not many of them there. So I think we know who you're talking about. Yeah.

**Brandon Harris:** Um, uh, so, so we worked with a factory and, and they have some experience, um, doing, uh, you know, other networking gear and things like that and finished goods and plastics. Um, so, you know, they hadn't, uh, the, the big thing there was they hadn't done laser etching before. So, uh, we had to buy a laser etching machine and store it in their factory. Um, all right.

**Chris Gammell:** So that's cool. So can we go back to the, uh, so to the actual, the, the processor side of things. So we talked about there's six, cause I think like, like you said, I think for the hobbyist, for a lot of the people that are going to get started with this thing, you're going to start with the SD card. But how much do you find that people are actually using this as their main processor in a project, right? For like, for like some kind of external hardware. And how many are using this as a peripheral off of another, another micro that might be on board, like a Arduino talking to this or something else talking to this. Is that, is that even a necessity or do you find most people doing just straight out of the, straight out of the processor here?

**Brandon Harris:** Um, so I'm not sure what the breakdown is, but you know, I would say the majority of our customers don't have a secondary microcontroller. They run the entire thing hosted within the, uh, the imp itself. One of the great advantages of, of doing that is that, um, because we, we do, you can update everything from, uh, a web browser. Um, you write new code, you push go, it downloads it. It's done no matter where it is in the world. Um, you know, so, uh, actually at, um, uh, maker fair right after we launched, uh, you know, I, we had, there were some issues with a couple of the device driver code and I couldn't get, uh, my laptop onto wifi inside of the hall. So I went outside using a 3g connection and was pushing code updates over my cellular network to the other cellular network that all of them were connected, you know, the AT&T hotspot. They were all on and they were updating automagically during the middle of the show. Yeah. Um, you know, we do this stuff. We've done stuff like that all the time. You can leave hardware on your desk and, you know, you forget to take it home while it's all right. You just sit there and you run it from, you know, you bring it up in your web browser and you can debug it from anywhere. Um, which is a really, really spectacular. Once you, once you forget that that's not how most microcontrollers are, it's, it's hard to go back.

**Chris Gammell:** Well, yeah. The only thing that stinks about that is sometimes I found, I've done that with like one or two remote devices before. The only thing that stinks about that is like, it's like, oh crap, now I need a webcam. Cause I put that led on there as a visual. Yeah. So that's your next product is, is the, is the, the troubleshooting webcam. That's what you should do next.

**Dave Jones:** Why can't I find like details on your website about like the SD card and stuff like like a data sheet for these things. I'm, I'm just bumming around on here and I like, it's not even in the product gallery. All you've got is the Budweiser thing and the Lockatron and the Haiku and the.

**Brandon Harris:** Uh, so if you scroll all the way to the bottom, um, yep. You'll find a link to the dev center.

**Dave Jones:** Ah, dev center. Right.

**Brandon Harris:** So, so this is, this is, uh, you know, the, the unfortunate reality of the majority of people who come to electric imp.com are just sort of checking us out and non-technical. Um, and show some of the technical details all hidden there. Yeah. So if you, if you, if you find our electric imp.com, go to the dev center and then you can go into hardware and you can find a data sheets for, for any of the three, uh, products. Got it.

**Dave Jones:** Yep. Found it now. Yeah. Yeah. And you sell the modules through Art of Fruit and DigiKey and Jamesco and SparkFun. Yep. Right. Awesome.

**Chris Gammell:** So, okay. So open the box, get it up, get it, get something, get an LED blinking to it. Two lines of code, one line of code. What are we talking here?

**Brandon Harris:** Uh, yeah, I think, I think you just need one. Wow. Depends how fast you want your LED to blink, but yeah. Uh, so you can, you can just, uh, configure a pin as a PWM is a single command line, uh, single, single line of code. Um, yeah, I think the minimum frequency on PWM is, uh, uh, uh, every 60 seconds. So as long as you're cool with, you know, it blinking for one second at a time. Yeah. One line of code.

**Dave Jones:** Um, well, that's what everyone expects these days. I mean, with the Arduino generation. Yeah. I guess you could call them. They, they expect that sort of simplicity. Yeah.

**Chris Gammell:** So what about the other, the other end of the spectrum then? So have you, have you found yourself limited in terms of complexity? Is that mostly just in pin count or response time or anything like that?

**Brandon Harris:** So pin count is, is one of the biggest challenges with, um, you know, six pins is, is rarely enough. Uh, if it's, if it's any kind of real complex device, um, you know, it's great. We, we do a lot of things, especially with like I2C, right. Where it's like, I can plunk down 12 sensors and only use two pins. Um, yep. And so that's, that's, that's a great solution for, for low pin count devices, but the cost adds up pretty quickly. Um, so, uh, you know, 12 pins most of the time is, is enough. Uh, we also add, um, you know, you can get an I2C based IO expander. Um, they can, they can take a lot of the resources in terms of the code. I mean, we have, uh, customers who are running 4,000 plus lines of code. Um, that's all being written in an interpreted, uh, language. So, you know, your typical code density versus what you'd have in C 4,000 lines of code is, is really probably 50,000 lines. Yeah.

**Dave Jones:** Is, is there a, is there a way to go lower level if you really want to, if you're a real diehard? So, so there isn't.

**Brandon Harris:** Or do you guys go, no way, Hose? Um, the, the main reason being, uh, this is again, it's, it's, you know, Hugo, our, our CEO and myself both have come from Apple. Um, and it's kind of part of the, uh, ensuring the software engineer has the, the right experience. Um, and so as soon as you start exposing lower level, uh, APIs, you know, allowing them, you know, the first thing you're going to want is to allocate memory. Right.

**Dave Jones:** Right. Yeah. Oh yeah. And then you're screwed. Right. Right.

**Brandon Harris:** And, and then it's, then it's game over right now. Now you can break your device. Now you wipe out your operating system. Right. As soon as you do that, all bets are off. So, um, our, our goal is again, that you should never be able to push down an update to the imp that you can't recover just by changing your code and hitting go. Yeah. Got it. So it's, you know, I, again, I'm a, I'm a hardware engineer. I, there are times where it, it drives me nuts. And actually one of the big things is, has actually been a learning experience for us about, you know, what are, what are the shortcomings? What does that actually imply? And, um, so we have, uh, you know, native spy peripherals. So for something, you know, something like, uh, that you typically bit bang, um, like, uh, you know, uh, um, infrared remote to control your TV, um, you know, on your Arduino would typically just be, uh, pin states and delays, and that would be fine. Um, well, we don't want to block the processor for that long. And, and because you're running an interpretive language, timing is a little more challenging. Yeah. Yep. So we use the spy peripheral for it. Um, and so we build the entire packet in spy and then let it do the work of just shifting out bits at the right frequency.

**Chris Gammell:** Nice. So wait, so you're saying if you were going to do an IR remote, you would, would you be writing to another expander type of thing or no?

**Brandon Harris:** No. So, so, I mean, you know, you could, it could be as simple as hooking up a infrared led to, uh, a pin on the imp and then, uh, to a spy data output pin, the Mosey pin. Um, and then just some software to, to basically, um, where the data would be formatted into the, uh, what you want the IR sequence to look like.

**Chris Gammell:** Oh, okay. Okay. So you're, yeah. Okay. So you're writing a bit pattern effectively to like a queue inside of it, like a, like a cute spy module type of thing. Right. And then it just clocks it all out. So I thought, yeah, cause you need that overhead. You need to switch back to your threads or whatever so that you can go talk to the wifi and everything else and do your updates and power checks. Yeah.

**Brandon Harris:** That's, that's, that's actually like the, the far and away, the biggest, uh, challenge for new developers, um, who come from microcontroller land is the first thing they want to do is a while one. Um, yeah. And it just doesn't work in the internet age. Right. Um, let's talk new Texas. Blah, blah. Yeah. Um, so, you know, that's, it's a, it's a big challenge to, to get people transitioned over, over from that to an event driven programming. Um, but there's a lot of like just spectacular things about it that you just, you never want to go back. And, and someone like the other really cool sort of, you know, really bonus side effects is because the entire operating system is event driven. We can actually do at an operating system, uh, dynamic power management where when there's nothing to do, we just idle down the processor and, and peripherals to a lower clock rate to save power. Um, and it's completely transparent to the application because nothing's happening during that time. And then as soon as an event, a scheduled event is ready, all of that stuff comes back up and it starts executing.

**Chris Gammell:** Huh? So really what I'm hearing is that the trade-off, the trade-off for people that are developing with this thing is you give up something on the, the low level, uh, the low level knowledge of what's going on. But what you get is you get like built in optimization for power effectively, because that's really like the thing that is annoying for like, I hear, I hear embedded people talking about that. Oh, well, you know, I got it working in, in two weeks and then I spent three months fixing the power scheme.

**Brandon Harris:** Yeah. So, I mean, power, power is a huge part of it. Um, there's a lot of other, just, you know, um, one of the other, the biggest things is just that networking is fundamentally asynchronous. Right. Yeah. Um, you know, in, in microcontroller land, there's, there's no real notion of it, of an asynchronous event, you know, typically even within an Arduino, rather than setting up ISRs for a button, people just pull the buttons. Um, it's just a lot easier. And the problem is if you need to be doing anything else, it's just a terrible form factor. And it means that now all of a sudden, when you want to do some low power, it's really hard to tell, well, do I actually need to be reading the button or do, am I just sitting here spinning?

**Dave Jones:** You have to change your entire code architecture of how you wrote the thing.

**Brandon Harris:** Yeah. So it also, it also really limits the number of things you can do in that loop, right? If you have multiple devices that you're trying to service, just sitting there and looping through all of them and blocking on any one of them really decreases your, your performance. Um, you know, one of the, the reference designs we have is called Nora and it's got a accelerometer, a temperature, uh, light level, barometric pressure, humidity, you know, all these different sensors on it. Um, and they all take it and it all runs off of two double A's.

**Chris Gammell:** And so you don't really want to just ran a Kickstarter, right? Wasn't there like, like 14 different Kickstarters that did just that?

**Brandon Harris:** Yeah. Um, uh, so, and, and there's actually even a quirky product called spotter. That's, um, quite similar, but you know, sort of the idea is one of the, um, you know, one of the great things is we can actually come up and, you know, I know that the humidity sensor takes the longest to read. Um, and so I can actually start events that says, okay, I have to prime the humidity sensor because it takes like 150 milliseconds to initiate. So I start that. And then as soon as that's done, I start reading all my other sensors, but each one of them has some, some delay. Um, and so I can just schedule basically, I can start all of them. Um, and when I start them, I say, okay, now pick, pick up the data in, you know, 150 milliseconds or pick up the data in 80 milliseconds and everything is scheduled out. And then all of a sudden it just, you get to the end and all your data is collected in the, you know, basically in the guaranteed minimum time, because the humidity sensor will be the last one to be connected. And, you know, rather than blocking for 150 milliseconds, then a hundred milliseconds, then a hundred milliseconds for each sensor, we're able to do them in a, um, in a parallel approach, which would be very hard with a traditional, uh, microcontroller. Definitely.

**Chris Gammell:** Wow. That's cool. That's really cool. What about, uh, let's talk power. I mean, so, so what are we talking here in terms of, uh, sleep power, deep sleep, active power, that stuff?

**Brandon Harris:** Uh, so I, I, I love the power story here. It's actually, um, something we spend a ton of time with, um, uh, because one of the, one of the greatest advantages is we think we bring to the tables is the ability to do battery powered devices, which very few, um, uh, internet connected devices are actually battery powered. Um, and so we can go our deep sleep, which is basically everything off, uh, keeps an RTC, um, and it can, has one wake pin, uh, and that gets you down to, uh, between four and six microamps, depending on which, uh, imp you're on. Yep.

**Dave Jones:** Um, is, is there any other way to wake it up apart from the wake pin? Can it wake on a, uh, real time clock event? Yeah.

**Brandon Harris:** So it wakes either on a timer or on, on a pin interrupt.

**Dave Jones:** Um, and of course that's all built into the STM 32 process. Yes.

**Brandon Harris:** So, so you, um, yeah. So, so when you go to sleep, you can say, wake me up in a day, wake me up in 15 minutes. So if you're doing something like that, nor a reference design where you just want to wake up, read all your sensors, send them to the internet, go back to sleep for 15 minutes. So you're just sort of doing a logging application. It's super simple. Um, got it. Uh, and, and you also have the option. So like on that design, we also have, uh, like the accelerometer. So if you want to wake, if you're disturbed, right, that's really easy to do. It's like you set up the accelerometer for an interrupt and it, it's connected to the wake pin and voila, you wake up and send the results immediately. Um, so, uh, yeah, so, so deep sleep sort of everything down, uh, gets you down to four to six microamps. Um, and the, uh, the interesting thing there, we actually, uh, play a fun game, uh, which is the, um, minimum voltage for wifi is two and a half volts, but the minimum voltage for the processor is only 1.8. Um, which means with wifi off, we can run directly from two AA batteries. Nice. Yep.

**Dave Jones:** Right, right down to what minimum voltage on the battery, because a battery will exhaust its capacity at 0.8 volts and alkaline.

**Brandon Harris:** Right. Um, so, uh, so we typically run them down to about two volts, basically anything, as soon as you really, even then getting to, to about 2.2, uh, they don't have enough, the, the, they don't have enough juice left in them to bring wifi up. Yep. So running a processor, if you can't bring the wifi up, isn't really that meaningful.

**Dave Jones:** That was going to be my next question. What is your minimum battery capacity? Your sort of like, uh, your highest impedance you can use. Can you use AAA batteries? Can you use CR 2050s? I assume they'd have too high an impedance to, uh, to fire up the wifi.

**Brandon Harris:** Yeah. So to, to, um, well, and additionally, we actually have to boost the voltage up once we get down to those ranges. Um, so that actually, you know, and that, that you pay for the current and that you have

**Dave Jones:** to boost the voltage for the wifi. Right.

**Brandon Harris:** So, uh, we basically, we use a, a, a boost converter that has a pass through. So when the imp turns, when the imp wants to turn wifi on, it sets the enable pin high. So it goes from a battery voltage up to, we typically said to 2.7 to give ourselves a little headroom. Um, yep. And, and then we can, we can, uh, operate at 2.7, um, and turn on wifi and be happy. The biggest issue is, uh, the, the wifi chip when it powers on has to do a calibration cycle where it basically sits there and sends, sends packets at maximum power without the antenna connected. Um, oh, poo.

**Dave Jones:** Yeah.

**Brandon Harris:** Uh, and so those, those, those, those, those transients get up to, uh, 250 milliamps. Ooh. Uh, how much of an impulse?

**Dave Jones:** Do you need some local decay? How much local decoupling do you need?

**Brandon Harris:** So, uh, we typically, so on, on the, you know, on, on most things, just one microfarads externally, we also have onboard, um, uh, you know, inside the module there's capacitance. Um, and so with most, uh, power supplies, just sort of the standard decoupling is sufficient running off of two AA batteries. Um, we put a, an electrolytic in parallel with the batteries. Um, and that substantial, what we found was, um, we did like battery life testing with no electrolytic with a 220 and a 470 and a 1000.

**Dave Jones:** Uh, there'd be a big difference. Yeah.

**Brandon Harris:** And, and for the, it, for alkaline batteries makes a tremendous difference. Um, one of the things we're, we're quite fond of, of course, you know, the solution to any engineering problem is to spend more money. Um, that's correct. Yes. Is, uh, the Energizer makes the, um, well in the U S they, they sell the lithium iron sulfide. Oh, okay. And those batteries are awesome.

**Chris Gammell:** Oh, those are the life EO, the life EO threes, right?

**Brandon Harris:** Yeah. Yeah. Yeah. Um, they, yeah.

**Dave Jones:** Cause they got stupidly low impedance and they, you know, over their full operational.

**Brandon Harris:** They hold their, their voltage across the entire thing. And then, and then when they're done, they're just done. Yeah. They snap off.

**Speaker ?:** Right.

**Brandon Harris:** It just falls off. So, um, actually on our, on our website, if any, if anyone ever wants to take a look, there's a great graph, uh, under, uh, reference designs for the Nora reference design. Cause I, I tested, uh, with three different, uh, uh, battery chemistries with, uh, you know, just Duracell alkaline batteries, the Eneloop nickel metal hydrides and the, uh, Energizer lithium batteries. And it's very, it's, as an engineer, it's a great little graph of, you know, how, how they behave under sort of similar circumstances. And, you know, we have these, these high load transients and that's actually where we end up burning a lot of our power. Um, cause once you're actually online, it's, you know, it's not substantial.

**Dave Jones:** Oh yeah, totally. Yeah. Yep.

**Chris Gammell:** So, so what is the, so the, uh, so you said 250 million amps, but really we should speak in joules almost. Right. I mean, like, cause it's about the impulse as well. Like what is, how long is that impulse?

**Brandon Harris:** Uh, very short. Uh, so, so, and I mean, I don't remember what it is off the top of my head. Um, you know, we measure it in microseconds, uh, tens to hundreds of microseconds.

**Chris Gammell:** Okay.

**Brandon Harris:** Yeah, that's okay. Yep. So, you know, it's, it's, it's in the range that you can pretty easily decouple it.

**Chris Gammell:** Um, so that's like micro joules, right? Is that right?

**Brandon Harris:** Yeah. Somewhere in there. So, so we measure, you know, what's, what's usually more important. Uh, so we recommend, uh, electrolytics for battery powered applications. Um, yeah, uh, it, it, it does sit significantly. Increase battery life. Um, especially in combination with alkaline batteries with the nickel metal hydrides or with, uh, the lithium iron, uh, the energizer lithium batteries, it's not as big of a difference. The output impedance is so much lower on those that you're not. And it's, it's more or less constant across the entire battery life. Um, that, uh, it's, it's not as substantial.

**Dave Jones:** So how long will a typical product last on two double A? Alkalines, for example, I don't know, you know, spitting out, you know, a thing per minute or something like that. So, um, a data packet per minute or even per hour or something like that.

**Brandon Harris:** So, you know, basically we, we measure things for us. The wakes are typically so much higher than the sleep current. Um, you know, we, we optimize the entire, you have to, you have to consider that in the entire product that you basically want your sleep current to get to zero. Um, and if you do that, right, then you, then it's just the power to wake up. Uh, so, uh, alkaline batteries, we can get maybe 60,000 wakes, um, off of a single pair.

**Dave Jones:** Uh, so, you know, 60,000. Okay. Let me do some.

**Brandon Harris:** Um, yeah. So if you're connecting every minute, uh, you get what a thousand, uh, I don't know. Yeah. It's a bunch. I think it's, um, right.

**Dave Jones:** So you can, I think it's 41 days or something. Yeah. 41 days. 41 days. At every minute.

**Brandon Harris:** Typically.

**Dave Jones:** At every minute. Right.

**Brandon Harris:** Um, you know, we'd, we'd be talking more like, uh, every 10 minutes or every 15 minutes for, for that kind of data logging. Um, okay.

**Dave Jones:** So you could run for quite a few months.

**Brandon Harris:** Yeah. So, I mean, like Nora at 15 minutes, um, you know, we, or I think we did 15 minutes every, and then waking up and just collecting data, uh, every minute. So it's uploading 15 minutes of data every 15 minutes. Um, we were getting, you know, one and a half years on, on standard alkalines.

**Dave Jones:** Wow. So that's very impressive. Okay. I'm impressed. Yeah. That's, that's almost game changing. Yeah.

**Chris Gammell:** So Wi-Fi, that's the thing that I think we have to call out here too, right? We have to make that distinction. This is Wi-Fi versus Bluetooth versus.

**Dave Jones:** Yeah. Yeah. It's not Bluetooth LE, you know, this is like Wi-Fi. It connects to your standard router. So you can just shove stuff in your house.

**Chris Gammell:** How do you guys, uh, classify like, like, like distance to router? Stuff like that. I mean, like what router power, or does that not really, is it more of just a blind transmit?

**Brandon Harris:** No. So, so because, um, uh, Wi-Fi is sort of fundamentally TDMA, um, you know, that, that everybody's talking at a different time. There's not, there's actually.

**Chris Gammell:** Time division multiplexing. Is that, that's right. I don't know.

**Brandon Harris:** Time division multiplexing. So, so you're, you know, whereas with a, a cell phone, you actually have an incentive, uh, with, with a, your standard LTE, you have an incentive to lower your output power so that the base stations can sort of just barely hear you. Uh, in Wi-Fi, it's actually sort of the opposite, which is you want everybody to hear you when you're talking. So you actually always want to transmit at your maximum power.

**Chris Gammell:** Uh, yeah. Okay.

**Brandon Harris:** Uh, it's, it's, but are you able to scale it back?

**Dave Jones:** Do you have to, if you know that your widget is only going to be, you know, one meter away from your Wi-Fi?

**Brandon Harris:** Uh, so you, you possibly could, but again, you actually, the network as a whole, if you, if you are only concerned with your network performance, your network is still better off having every device transmit at the same, at a maximum power. Um, because what that, what that prevents, what it means is that, um, if there's somebody, you know, if you're right next to the access point and there's somebody who's far away. And so you say, oh, well, I'll back off my power. Um, and so the, so the access point can just barely hear me. The person that's, that's way out there can't hear you. So you both start talking at the same time and the access points like, whoa, whoa, whoa, guys, you're talking at the same time. I can't hear you. Right. But the guy out there doesn't know that, that anybody's talking. Right. And so he's like, Hey, what, what, what gives? I thought I had the channel. So, um, it's, it's a better system when your network performance goes up, when everybody can hear everyone else. And the best way to do that is to have everyone talk at maximum volume.

**Chris Gammell:** The first person to write a dramatic play based on wifi devices, talking to one another wins the biggest award in the world.

**Dave Jones:** But I couldn't hear you.

**Brandon Harris:** Yeah. Yeah. I mean, it's, it's, it's one of those things that as an engineer just seems wrong and seems like it should be optimized. Um, but again, for, for most of our stuff, um, the actual radiated power, you know, the power going into the antenna isn't, isn't the thing that really, uh, uses the most juice. A lot of it is just keeping the receivers on and, you know, gill all's up and all that, that jazz is a lot of it's just system overhead. So reducing your output power isn't, isn't a way that's going to save you a ton of battery life.

**Dave Jones:** Got it. Do you have issues with like the SD card one, for example, or even though even the module, right? People put a big whacking ground plane. Oh yeah. Under it. Like, how does that limit the performance? And do you have to go, look, guys don't put a bloody ground plane under it. What's the story? Yeah.

**Brandon Harris:** I mean, you know, we've, we've, my team is responsible, you know, sort of our goal is to help customers have a positive first experience. Um, and so we've developed a lot of documents. We've got a document that's, you know, building successful devices. Um, that basically says, Hey, don't put a ground plane under your antenna. Um, right. We're going to talk some RF theory. The, the, actually the, the bigger one is, is actually, it's, that's, that's actually rarely the problem. Usually the problem we have is people putting no ground plane anywhere whatsoever. Right. Which like you can do, or, or like they'll have a switching power supply and the inductors, you know, placed next to the amp and the chip is placed next to the USB jack. Right. Um, and it's like, that's, that's not how that works.

**Chris Gammell:** I looped the trace all over the board to try and make it better. Yeah. Um, but longer, well, I couldn't get a big enough inductor.

**Brandon Harris:** So I added some trace to it. Um, so yeah, that's actually, so the, the, the no ground pour is way, way more common for us that, that you just see sort of auto routed. Uh, yeah. All the grounds are connected. Um, check. T-shirt sales end next week, folks.

**Chris Gammell:** Never trust the auto router. Yeah. It will be wrong. 100% of the time. Oh man. Oh, that's hilarious. Yeah. That's, that's one of my favorites. So we didn't actually cover the other. So you, we mentioned deep sleep. What are the other sleep modes?

**Brandon Harris:** Oh yeah. So, um, so on with wifi off, uh, I guess you, right. And again, all of these things, because we do dynamic power management, a lot of it depends on what you're actually doing. Right. You know, if you're sitting there clocking out spy on a heavily capacitively loaded bus, your power numbers are going to change. Um, yes. So, you know, or you're, you're trying to use an amp to compute Bitcoin. I don't know. Um, uh, so the, the, I'm just going to give ballpark numbers. So basically STM 32 running, not a whole lot going on, gets you into sort of the one to two milliamp range, um, with wifi on, but with wifi power save. Um, puts you up in the five or six milliamp range. Um, and then sort of just stock out of the box. You don't do anything. It comes up at a hundred milliamps that gives you sort of the best wifi performance, the, you know, lowest latency as you go to wifi power save modes, you have a latency for incoming packets. Um, so, uh, you know, we sort of come up with the, in the most performance mode, uh, and then allow your code to bring it down from there and say, no, no, no. I want, I want lower performance. I'm running on batteries.

**Chris Gammell:** Okay. Got it. Okay. So that's the on with wifi off. There's other, other ones. Sorry.

**Brandon Harris:** Uh, so on with wifi off is, uh, one or two on with wifi on in power save is five or six. And then all out, everything on is a, is a hundred milliamps.

**Chris Gammell:** Oh, okay. Okay.

**Brandon Harris:** So, well, uh, you wouldn't do that for long though, right?

**Chris Gammell:** I mean, these are short cycles still. It's wake up, do your thing, go back. Yeah. Yeah.

**Brandon Harris:** So, I mean, typically, um, I've forgotten the, the exact number, you know, so we can do a full wake up, connect, send data and get back to sleep, um, very quickly. And so even though our power level is relatively high in that, um, you know, it means that, uh, the actual, uh, jewels used is, is still relatively low. Um, and there's actually, you know, one of the things with, with power saving is it takes time to get into power saving modes and things like that. So it's actually, you know, even in wifi to, to drop down to the next power saving mode, unless you're online for 300 milliseconds or more, there's no, uh, there's no incentive, um, because it, it takes 300 mills up to 300 milliseconds to take effect.

**Chris Gammell:** Huh. Okay. Well, that's interesting. Uh, and that's probably all the data sheet you said too, right?

**Brandon Harris:** I mean, like the, yeah, most of that's, most of that's in there. Um, you know, we also, the dev center has a lot more resources, things that are, you know, not strictly, you know, a data sheet, you really want everything in there to be absolutely verifiable and not sort of rule of thumb. Right. So that when somebody says, well, I configured every single peripheral and I'm clocking out at 30 megahertz and, uh, I'm not hitting my power number, the power numbers you quote in your data sheet. Um, you know, there's, there's a little more nuance. So a lot of it's in our, our, our developer center, um, you know, we try and put a lot of, a lot of information in there and it's, it's growing every day.

**Chris Gammell:** So that's good. What about this, uh, blink? The blink link up. Yeah. What's that? Tell us about that. That's interesting.

**Brandon Harris:** Uh, yeah. So, so blink up is our, um, configuration, uh, uh, method. So, you know, sort of the, the fundamental problem, almost every single, uh, wifi device has is how do you get a network name and password into the device? And if you've ever bought a USB, uh, rather a wifi printer, uh, you know that that process can be insanely painful where you're sitting there using an up arrow and an enter button to try and sort of type something in. Right.

**Chris Gammell:** Why did I use an ampersand? Yeah. Why did I use an ampersand? Yeah.

**Brandon Harris:** Scroll, scroll, scroll, scroll, scroll. Um, so, you know, and, and the problem is on a printer putting buttons and a display is totally reasonable. If you're trying to sell an internet connected device for 50 bucks, you don't have room. You don't have room for buttons. You don't have room for a display. You don't certainly don't have the budget for those items. Right. So having, having a way of getting that information into the device is extremely important. Um, so we use, uh, the idea is that most adopters of internet connected devices also have smartphones. Um, and so we use the smartphone to, to set up the device. Um, we thought the, uh, sort of the, the, the traditional process of, uh, well, it, it, it looks like an access point. You join the access point, you load a webpage, you type the information into the webpage. It then reconfigures, you go back into settings, you go back to your normal wifi. It's like, that's just a pain. It's terrible for users. Um, you know, it's like, Hey, set up in less than five minutes. It's like five minutes is way too long to be setting up a device. Um, so, uh, our PhD not included. Yeah. The, the process, the process, um, we like, we use is, uh, our technology called blink up where basically it, it, uh, flashes optically. So every, uh, amp, if you buy the card, it's literally integrated into the card. If you're buying a solder down module, you add a photo transistor, uh, externally.

**Dave Jones:** Oh, okay. So you've got to add it. So you don't have one inside your module that has a little peep hole. Right.

**Brandon Harris:** One of the main, the, the biggest complaints with the, um, the card was that they had to, uh, customers had to expose the, the card so that they could get light in. One of the great things with the solder down version is, well, you can put the module anywhere you want and just expose the photo transistor. Um, right. So you add a photo transistor and basically photo transistor just changes a voltage when it sees light or dark. Um, and so it's, you know, using an iPhone, it's as simple as the, the refresh rate of the screen is extremely reliable, always at 60 Hertz. And so, uh, literally just, if it sees black, it counts as a zero. If it sees white, it counts as a one. Yep. Um, and we have some algorithms on the device. So it, it, it basically samples it, um, uh, as a, uses the, an ADC, um, and samples the incoming signal looks for edges, uh, basically transitioning between black and white. Um, and you can, you can send data that way. So it has a little synchronization and we pack all that data into a, into a format that's, um, that contains the wifi SSID, the password, um, to get it on the wifi network as well as the user's credentials so that, um, uh, we know who that device belongs to. Um, and it gets added to the right, uh, account. So that's actually part of sort of the ownership process as you go and you blink up your device. Um, and it's, it's a really, um, awesome, awesome thing to use once, you know, the first time you see it, you're like, Oh, cool. Yeah.

**Dave Jones:** Um, and well, it's technology straight out of the 1970s.

**Chris Gammell:** It's, you know, um, what if you, what if instead you, you had the, the two, the two, uh, electrodes where you touch those as well. And that does the programming. Do you remember those devices as well? You actually had to physically touch them together. That could be nice. Yeah.

**Dave Jones:** Um, yeah, this was like 1970s, all your, you know, your, your, your light guns and your light pens and everything interface with your CRT screen, which, you know, had a little dot in the corner and you could, and you could send data, you know, it's a, and you guys have got a bloody patent pending on this thing. Obviously something deep, you know, very specific and neat. Uh, yeah.

**Brandon Harris:** So I mean, the patent is really geared more towards using it for wifi setup. Um, right. You know, we're not foolish. Like we know we didn't invent, Hey, I can send data with flashing lights, right? There's the entire fiber optics industry might have something to say about that. That's right. Yeah. Um, late nineties called, but, uh, yeah. So, so no, so it's, it's really about using that as a way of configuring, um, uh, just wifi credentials. Um, so that's great.

**Chris Gammell:** That's really great. Yeah. And, uh, we talked to Adam, Dave wasn't there for this, but Adam, uh, Wolf from, uh, Wayne Lane, they, they talked about doing some similar stuff on, on their device when they were trying to program, uh, I think it was just an AVR or something, but using a, a CRT type screen. So, uh, that's a folder episode. I don't remember which one it was, but people can may remember, or can go listen to that one as well. What about, uh, uh, you know, going forwards, are you guys going to push into other technologies you think? I mean, wifi is cool. Bluetooth. I mean, are you going to actually do that or stick with what you know?

**Brandon Harris:** I sure hope so. Um, no, I mean, uh, yeah, that's, uh, I mean, uh, I mean, uh, I mean, uh, that's sort of the idea, right? Again, um, we're, you know, for, if we're positioning ourselves as, as a connectivity platform, having other kinds of connectivity seems to only make sense. Um, you know, Bluetooth is a little harder because, you know, sort of one of the core tenants of our, our platform is the internet portion of it. Um, right. It's, it's what gets your devices online. And, and right now, you know, we, we see lots of Bluetooth devices and, and a lot of them are being positioned as internet connected devices, but they're really not. They're phone connected devices.

**Dave Jones:** Yeah. You've got to have something in between. They can't just, you can't just connect a Bluetooth something gadget to a, the internet

**Brandon Harris:** doesn't work. So, you know, wifi is, wifi was a great first choice for us. Um, you know, the next, the obvious next step is, is cellular.

**Dave Jones:** Well, there's only two choices, isn't there? There's wifi or cellular. That's how we get our points of, our internet points of presence in your home, your office, you're, you know, ubiquity. Ubiquity, right?

**Brandon Harris:** Yeah. Right.

**Dave Jones:** Yeah. Yeah. They're the only, as far as I know, please correct me if I'm wrong. There is no other option.

**Brandon Harris:** No, that's, that's pretty much it. Um, so, you know, but the idea is that because we have this, we've abstracted the connectivity layer of it. Um, you know, a single customer could have devices that are either cellular or wifi. Um, and they're not, you know, I mean, one of the biggest challenges has been traditionally it's like, well, the connectivity was, was the hard part of the connected product. Um, and so for them, you know, really now it's, it's about creating the, the customer interface and a slick app and things like that. And getting that kind of engagement is, is the challenging portion. And which means, you know, we, if we roll out a cellular solution, that, that means that they can transition from wifi to cellular and have the exact same experience, um, and not be hiring, you know, RF engineers and things like that to go through all the, um, the challenges. The biggest issue with cellular is just, uh, the approval process, you know, wifi is great. It's unlicensed band, you know, you pass FCC, that's it, ship it. Um, cellular is much, much more complicated. The carriers are, you know, I hear ATT is very pleasant. Yeah. Um, so, you know, it's, it's, it's a, it's a hurdle, but again, it's the sort of thing where if, if we can solve that challenge for a lot of our customers, that gives us a really great advantage of, of being able to sort of amortize the, this large fixed development cost, uh, across many customers and make something that wouldn't, you know, you, you just can't sell something at a reasonable price, uh, that cellular these days, um, in, in relatively low volume, because the approvals, I mean, you know, AT&T, um, released a white paper saying they've, they've, they've been really pushing to, to get development costs down and they've, they've pushed it down to $40,000 in six months. Whoa. Right. Right. And you're like, you know, like what kind of products can sit around for six months and, and spend 40 grand before you ship a single one?

**Dave Jones:** No. Um, and, and to do your, and to roll your own sort of unique solution there, you've got to be like an Amazon, like with the Amazon Kindle, you know, they had their own 3G solution or something, or they partnered up with some, you know, but you didn't know any of that. It, it just worked, you know, it just magically worked and yeah, but Hey, they're Amazon.

**Chris Gammell:** Yeah. A little more money there.

**Dave Jones:** How, how big is imp now? How many employees you got?

**Brandon Harris:** Um, I think we're coming up on, we're high thirties, might've hit 40. Nice. Okay.

**Dave Jones:** Right.

**Brandon Harris:** Very cool.

**Dave Jones:** And, and you guys were a startup and you got funded by a couple of companies? Yeah.

**Brandon Harris:** So we, we took the, uh, the traditional Silicon Valley, you know, go get VC funding. Um, right. You know, we've recently closed a, a series B round and, um, which is great to, you know, feel like we have, it's a good validation of the platform and, and gives us a really nice runway to, to focus on bringing in, you know, we're coming up on half a million, but you know, I, I come from Apple, right. You know, half a million is, is pilot bill. It's like not even launch day. Right. Like, yeah, I know. Exactly. So we, we really want to be pushing towards the, you know, the millions of devices and, and, and, and into 10, tens of millions. And, you know, with the, the kind of, um, fundraising we've done and, and one of the other big things is, is partnering with some, um, hardware manufacturers like we did with Murata, um, that, that frees up a lot of capital for us that, um, you know, they're, they're bearing the capital expense of building, you know, product and holding inventory that, um, gives us a lot. Right.

**Dave Jones:** Oh, so, so, so, so they will hold inventory as well. Yeah.

**Brandon Harris:** So just make this. So we, we are actually, uh, it's a, it's a full on partnership where basically they're responsible for the entire hardware solution. Uh, and we are just responsible for the software. Um, that's cool. Right. That's cool.

**Chris Gammell:** That's the chip based one, right? The, uh, the, the 26 pin module you mentioned that.

**Brandon Harris:** Yeah. So it, it, it looks like a chip. It's, it's really is chips and discreet inside of it, but it's all poured into a pretty molded plastic. And so, you know, you get a, a very like chip like feel, but it's got an integrated shield and everything else. They have some really excellent technology. Yeah. We'll definitely link that in that. That sounded really cool. Um, they do some, some really, really great stuff. They're spectacular engineers over there.

**Dave Jones:** I would have thought it would have been easier. Um, you know, the venture makes it sound so easy. Just go out and get the venture capital funding. I think it would have been a tad easier that, uh, Hugo, your CEO and founder was the former head hardware guy at Apple. I mean, head hardware design team or something, right? That carries a lot of weight. I would presume with the venture capital. Yeah.

**Brandon Harris:** Um, he also, uh, spent some, spent some time at Nest and, and did their, did their first, uh, hardware design. So he's got, uh, the Nest serial number one on his wall at the home. That's awesome. Right. Okay. There you go. Uh, so it, it, it does make it easier, but it's still, it's, you know, it's, it's a hard road. Um, and. With hardware. Yeah. Yeah. Well, and the big thing is it's really hard to explain to a venture capitalist why we should be building a platform instead of a product.

**Dave Jones:** Right. Oh, I, but I thought they're all about.

**Brandon Harris:** Yeah.

**Dave Jones:** I would have thought that too. Yeah. Platform as a service.

**Chris Gammell:** They want to capture all of this stuff. Everybody comes to one thing, right? That's the, that's the ultimate.

**Dave Jones:** Who the hell wants to make hardware anymore?

**Brandon Harris:** Uh, so it's, it's really popular, uh, in the software world, but sort of, you know, there aren't a lot of companies doing hardware as a platform. Right. And hardware, really hardware as a service, right? That, that the whole idea of the ElectroCamp platform is that you don't have to worry about the hardware, right? It's just sort of like, whatever somebody designed it, it works, it's online. I can send code to it. Right. In the same way that you don't have to worry about what kind of hardware your Amazon server is running on. It's like, whatever. It runs Linux and does these things. Right. It's just like, um, so, you know, I think that, um, getting, uh, venture capitalists to the point of understanding that it was, was a really big challenge. Um, and you know, they, they, they're sometimes, uh, known for, you know, wanting to make a quick buck and that's, that's, yeah. Yeah. Right. Um, so the, and that's the, that's the other problem with the platform, right? Is it takes a long time to build. Yeah. It's not just sort of get one product on the market, ship it and you're done. What's next. It's supporting the platform, building the platform. Yeah. Right. Um, so switching coding languages the day before you launch. Yeah. Uh, rewriting everything you've ever written, uh, in the one week before Maker Faire. That's fine. So yeah. No.

**Dave Jones:** See what, what your big launch was at Maker Faire.

**Brandon Harris:** Uh, so that was, that was our first, you know, we sort of did a press campaign before that, but that was the first public demonstration of our technology. So.

**Dave Jones:** See, that's interesting. You know, usually it'd be CES or some other, you know, wanky business. Yeah.

**Brandon Harris:** So this, this is actually one of the things I love about electric camp and, and something that, um, is, is, uh, has been like such a blessing as, as it was, as an engineer and in terms of workplace satisfaction is we're still really involved with the maker community and the developer community. Um, you know, we all kind of came up through there. Um, you know, I've been playing with all of the different Arduinos and we have a lot of people on board who've, you know, been through that and, you know, uh, a couple of, you know, a couple of people have done their own Kickstarters and unsuccessful Kickstarters, but, um, you know, that that's kind of, it's been a really great community for us. And so Maker Faire was a great opportunity to get feedback from those users.

**Dave Jones:** Um, because the, they, they're the ones who will give you feedback.

**Brandon Harris:** Well, and, and they get it right. Like the, yeah, they know the hard parts. Yeah, totally. Um, yeah. And they've, they've been there trying to parse XML on an eight bit microcontroller, right? Which your average, you know, most of the, most of our big customers, they haven't been through that or, or they've been through it at a, at a very high level. They've devoted, you know, engineer hours and, and in some cases, engineer years to trying to get a connected product online and, and failing. Um, and so, you know, it's, it's a lot harder to sort of convince them of, and, and get them to give you feedback and things like that. Whereas the Maker communities is really open and receptive. They, they've, we've been through, you know, the hardware stayed the same, but even the platform has pretty radically changed. Um, you know, we started with sort of a, a simpler, uh, software solution where you could only write code for that ran on the device. Um, and then it just sort of had, uh, an input port, an HTTP input port and output port, um, had this, you know, goofy sort of visual programming thing where you could connect one device to another and wire them all up. And, um, you know, that was, that was great for some things, but it just didn't scale to, to larger deployments. And as soon as people started getting to, I mean, even five or 10, they said, this isn't going to work for me. Um, and so we've, we've rewritten a large portions of the platform, um, because of that, that feedback we've gotten from those early customers.

**Chris Gammell:** That's awesome.

**Dave Jones:** Nice.

**Chris Gammell:** Well, uh, I think we're going to see a lot more of these. Uh, I don't know. I sure hope so. Yeah. I, uh, yeah, I, I'm embarrassed to say I haven't tried one yet, but I think I have to now. Um, I was, I was mentioning to Dave before as well that, uh, you know, so we're, we're doing hackaday prize stuff together. I think we'll probably see some stuff in there. Yeah. Some hackaday prize. I'd be surprised if we didn't.

**Brandon Harris:** We're, we might even, um, try and try and help seed some ideas and things like that. We've got a lot of reference designs online that are all free to use. So people can, can start with something that is working and everything else. Um, you know, that's, that's part of our commitment to helping people have a successful first experience. Um, thank you. So, I mean, we've had, we've had, uh, we've had several customers go to mass production with their first spin of the PCB. I'm going to swear at you right now. For something with wifi on it is pretty awesome.

**Chris Gammell:** Yeah. That's good. That's, that's, see, that's engineering cred right there. I think, you know, more than any, you know, money or any, you know, like, yeah, devices. Okay. Yeah. But yeah. One spin of a PCB, that's pretty killer. Yeah.

**Dave Jones:** One last quick question. Who do you see as your main competition in this area?

**Brandon Harris:** Um, that's kind of hard to say, I mean, you know, sort of the, the most obvious one, um, is the Spark core. Um, they have a, a kind of different model from us. Um, you know, they, they're tending, you know, we're, we have, have sort of a, our open source policy is we're willing to open source all the stuff you need to use our platform. So we post everything, you know, literally we tried to, to public domain, all of our reference designs and our lawyer said, you can't do that. Oh, boo. Well, no, like literally you can't, there's no law that allows you to make something public domain. The only thing you can do is apply the most permissive license you can possibly find.

**Dave Jones:** Um, wait, so your lawyer turned you and said, yeah, but that's, that's lawyer talk. You actually can, you can't do it. It's just in their world. It does not exist, but in the real world.

**Brandon Harris:** So, so we found, uh, I think it's the X11 license, which basically says, take this thing, do whatever the heck you want with it. Don't tell us if it breaks. Um, right. Uh, don't come trying to us. I haven't heard of that one. Yeah. It's X11 and something else I've forgotten, but yeah. So, so we, we like to open source all of our stuff that's, that's required to use the platform. We have a big GitHub repo that, you know, has all kinds of device drivers. So if you want to, you know, hook up an accelerometer to an imp, all of that stuff to get a lot of squirrel code out there. Um, but then the, the platform itself is, you know, that's, that's kind of what we consider our proprietary IP, um, you know, in the same way that, that Amazon doesn't tell you exactly how they run their servers. They let you run whatever you want on their servers. Um, yeah. You know, whereas, uh, Spark is a much more open. Uh, system, you know, that in theory, you'll be able to run your own servers and things like that. Um, you know, we think that that's not best for manufacturers, right? We spend a lot of time and a lot of energy getting our servers up and running and maintaining them, diagnosing problems, having the tools to be able to diagnose those problems. And then we can, we, once again, we can, uh, spread that across that cost across all of our customers. Um, so, you know, they're, they're kind of the most obvious. They're also, they also came out of the maker community. They did, you know, a, a crowdfunding campaign and. Yeah.

**Chris Gammell:** They were accelerator, weren't they? I think they were up.

**Brandon Harris:** Yeah. I think that's right. Um, you know, they, they still have a different model than us. They're, you know, I don't think they do low power as well as we do, but, um, you know, they, they have gotten, uh, they have made it. It's, and, and quite frankly, you know, I just like seeing more devices online and connected to the internet. I think our platform is good enough that, that as, uh, the entire number, you know, as the number of devices grows, uh, a big enough percentage of them will be using electric camp that, that really we profit regardless of who is, uh, who is putting the modules into a specific connected devices. It's about building a network and community and this expectation that your devices should be smarter and should talk. To each other. And to you, me and Dave have to figure out how to do that.

**Dave Jones:** Crap. Damn it. Well, no, first of all, we have to figure out a reason to do it. No, there's no, you don't just do it for the sake of it. I'm sorry. Well, I think that's what you play around to start with. That's what bugs me with the internet of things. People do it because they can, you know, regardless of, yeah. Yeah.

**Brandon Harris:** So, I mean, just, just to speak to that, you know, one of the things that, that I like because, you know, and some of this is, uh, when you work at a hammer factory, everything looks like a nail, but, um, you know, one of the, the fun things I did was, uh, I took our, I, I, I recently bought a house and it's the first time I've ever owned a garage door. Uh, so the concept of closing a garage door when you walk out of it is somewhat foreign to me. Um, so I just took our, our Nora reference design that has an accelerometer on it and, uh, foam taped it to my garage, the inside of my garage door and had it hooked it up to Twilio, which is a, a text messaging, you know, an online text messaging service. You can just interface to directly from the platform and had it send me a text message. If my garage door was open for more than five minutes, right? Uh, why? Which was, and I was like, all right, I get five minutes from the house and send me a text. You forgot to shut the door. All right, loop back and go back and close the door. And it was something that, you know, I was able to do in, in a, in a couple hours and it, it saved me leaving the door open all day and actually once all night. Um, so, you know, for me, that was, that was worthwhile and it wasn't something I could do just because it wasn't something I did just because I could, it was something that was a real problem for me. Right, right. You know, and that, that I was able to.

**Dave Jones:** I would have said, yeah, actually just look back and check to see if I shut the door.

**Chris Gammell:** Yeah, I'm, I guess I'm inherently lazy.

**Dave Jones:** I'm so old school, yeah.

**Brandon Harris:** You can't just look at a garage door and tell if it's up or down. It's like a, how dare I? It's like a shredding your cat kind of thing. I need a 16 bit accelerometer to tell me what position it's in.

**SPEAKER_01:** Oh, goodness.

**Dave Jones:** All right, Brandon. Well, thank you very much for joining us. It's been awesome.

**Brandon Harris:** Thanks for coming in, man. Thanks for having me, guys. It was awesome.

**Chris Gammell:** Uh, yeah. Uh, people could find you social media anywhere like that. Can they bug you with that kind of stuff or?

**Brandon Harris:** Um, I, I generally run pretty dark, but, uh, the, the at electric imp, um, uh, Twitter handler, uh, usually makes its way to me if it's. Hard way by. Directed at me or, or I also sort of feed those. You can also find electric imp on, uh, Facebook and, and all the usual places. And of course, uh, you know, our website, electric imp.com.

**Chris Gammell:** So, and you can also find Brandon's garage door online before he is. Yeah. You can, uh, you can figure out the URL. You can, you can know every time I come home. Oh, that's funny. All right. Well, thanks again, Brandon. It was great talking to you. Thanks, Mike. Thanks a lot, guys. See ya.

**SPEAKER_01:** Brandon has just arrived home. Garage door is open. Garage door is still open. administered administered administered administered administered administered administered administered
