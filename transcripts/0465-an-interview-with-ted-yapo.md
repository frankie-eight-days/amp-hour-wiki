---
episode: 465
title: An Interview with Ted Yapo
url: https://theamphour.com/465-an-interview-with-ted-yapo/
---

**Ted Yapo:** Roden Schwartz is a leading manufacturer of value instruments designed to help you maximize your bench's performance for everyday applications. They just announced an industry-first, complete solutions with all the upgrades up front for one price. Now through December 31st, 2019, save up to $10,000 on Roden Schwartz solution packages that come with fully loaded test and measurement instruments right from the start. When you invest in Roden Schwartz products, you get the highest quality engineering, plus all the bandwidth, channels, inputs, memory interfaces, and signal generation you'll ever need. Learn more about Roden Schwartz value instruments and this limited time promotion at askanengineer.us. That's askanengineer.us. This is The Amp Hour Podcast. Released November 3rd, 2019. Episode 465. An interview with Ted Yapo. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Ted Yapo:** And I'm Ted Yapo. I'm this week's guest on the Amp Hour. You are. That is very self-aware.

**Ted Yapo:** How are you doing, Ted? I'm doing well. How are you? I'm good. I'm good. We are going to be talking about your wide range of projects and the things that you lovingly share online and the fun stuff that you've been working on. But what's your background? How did you get into all of this electronics-y stuff?

**Ted Yapo:** You know, I got into it as a kid. I blame Radio Shack for the whole thing because my parents were – I think they had a credit card there because they would bring home stuff for books and kits and whatnot. And this was, you know, in the early 80s, you know, through mid-80s. And I just loved that stuff. I couldn't get enough. And so, you know, I think I was soldering it at 9 or 10. I remember burning my fingers once and I haven't done it since. Wow.

**Ted Yapo:** Yeah. I have to learn that. I'm yet to learn that trick. So I'm going to ask you about that after the show.

**Ted Yapo:** Yeah. But that's really how it started. And then it was – you know, it's really been a hobby for most of my life. You know, I studied engineering physics in college, which was basically the core electrical engineering curriculum and the core physics curriculum kind of mashed together. And then, you know, when I got out, recruiters said, well, what is that? I couldn't tell them, you know. So I ended up doing work in image processing at first, software stuff. And they didn't tell me. I was working there for six months or so before they told me who the customer was. And it was one of those three-letter agencies that you hear so much about these days.

**Ted Yapo:** Ah, yeah, yeah.

**Ted Yapo:** And so –

**Ted Yapo:** Yeah, I guess if you're not seeing the actual images, you wouldn't know what it is, right?

**Ted Yapo:** Yeah, that's exactly right. And there were, you know, there were a whole bunch of things you needed to do before you could actually see the imagery. And I just didn't like the kind of constraints of that work. You kind of get locked into it at some point. And so I moved around a bit. I did some work in finance, did some consulting work, and then finally got back into the image stuff, which I really liked. And wrote software for color photocopiers and color fax machines, which never caught on in the States, but they were big in Japan at one point. People would fax, you know, people, you know, family snapshots and stuff. And that work was all in assembly because that was back in the day where, you know, it made much more sense to, you know, save a few cents on every part because you were going to sell a million of them and just, you know, spend $50,000 on NRE to have an engineer write everything in assembly. Right. And that was, those were custom processors too. They were custom. Oh, yeah. I was going to ask what processor was on. Yeah, it was a custom parallel processor, you know, because image processing is just, it's embarrassingly parallel. And so, you know, at some point I graduated to writing the tool chains for that stuff. And this was, you know, this was before parallel stuff was on the desktop. And then, you know, the interesting thing was those skills transferred directly into networking. And so I went to a networking startup where they had built their own parallel processor and it had eight cores.

**Ted Yapo:** That's like the, like a threading kind of thing. Like that's what you mean by parallel processing there?

**Ted Yapo:** Yeah, yeah, exactly. I mean, they were, yeah, there were eight, eight cores on the, on the die. And then there were six, eight of those on the board. So there's these 64 cores all going at once to try to get networking packets through. And so they hired me as principal engineer. I knew nothing about networking. I mean, a little bit because I'd hooked up some Linux boxes and stuff. Sure, sure. And it turns out that, you know, there's a whole bunch of it that, that wasn't networking at all. And of course you pick up the rest of it or you pick up the context. But, you know, this, this low level coding transferred over directly, which was, you know, worked out pretty well.

**Ted Yapo:** Yeah, that's great. Is that like, I mean, I guess right now they, they still do that, but just on a broader scale. Now it's not 64. It's what many, many more processors than that or what, or what?

**Ted Yapo:** Yeah, I would imagine that they do. You know, I still have some, some friends that work there and, and they do the same kind of thing. It's, you know, it's a, it's a tough problem. It's, it's the kind of thing where, you know, on the, on the leading edge of performance, it makes sense to, to code things at that low level. You know, it just does, you just can't afford the overhead, even though it's, it's minimal these days of a compiled language. Everything's just kind of hand coded. And, but you do want the velocity that you get with a, you know, with, with software or firmware rather than having everything hard coded. Yeah. You know, in, in an ASIC, because even though that's faster, it's the time to market kills you.

**Ted Yapo:** I remember the first, so like, you know, I've done web stuff now for a while, not, not good, but you know, the amp power has a website and I administer it and other websites and stuff like that. And, and that's kind of how I learned Linux honestly, is doing some of the server side things. But I remember like the first time I learned, I'm like, wait, each, each computer connecting to this box, it's like getting its own like service and thread and like everything is like happening. And then I started thinking about like video streams and like, every time people are streaming video, that's not a broadcast. That means that those are all individual connections. It's like, oh my God, there's, there are a ton of things happening here. You know, there's so much like hidden from the, the casual web user, like I used to be. And then you start digging into it and it just kind of overwhelms you from like a DevOps perspective. And like a, like you're saying the networking perspective of like having individual connections.

**Ted Yapo:** Yeah. It's kind of bananas. Yeah. Yeah, it really is. And then, you know, at the, at the very bottom of the sort of networking stack, you, you get all these packets, you don't know what they're attached to. You know, sometimes you have to keep track of what, what stream they're attached to. Mostly you try not to because you, you just don't have that much time. And so, you know, it's, it's this juggling act of trying to get everything out, you know, in order on time. Um, it's, it can be a real challenge. It's, it's an interesting, it's an interesting field.

**Ted Yapo:** Yeah. There's a lot of technical expertise there for sure.

**Ted Yapo:** Yeah, absolutely. And that doesn't even, you know, touch the routing issues, right? The larger issues of how do you, you know, how do you calculate the routes and how do you deal with failure and all those things? Those are at, you know, another level entirely.

**Ted Yapo:** So then you said you were doing some more image, you're back into imaging stuff. What did, what did that look like? Yes. What did that look like? Yes.

**Ted Yapo:** So, uh, so that was it. So that was the, the office equipment stuff. Um, and so, you know, it was, uh, again, they wanted to spend, you know, a couple of dollars. On a processor. Um, and, you know, there's a lot of, there's a lot of data in an image. You know, you think about, you buy these things now and they sell them at a loss, right? These multifunction, you know, peripherals. You buy the, you know, it's got the scan, print, copy, fax, all in one, the inkjet things. You know, sometimes you can buy the new unit that comes with cartridges for less than a set of replacement cartridges. It's the old razor and blades thing, right? It's ridiculous. Uh, and so they don't want to, I mean, they want to drive the hardware cost to zero. And so they want to put in the cheapest processor they can and still get good performance, right? They want competitive performance. There's a lot of stuff you need to do to get the raw data from a scanner so that it looks like a photocopy. Right. It's, it's one of those, it's, it's, it's, I think it's really the only, um, imaging application where you can directly compare results. Right. If I take your picture with my, with my phone and I hold it up, well, that's, that's you in person versus a 2d thing. If I make a photocopy, I have the original and I have the copy and I can put them right next to each other. Right. Yeah. And not only can I do that, I can look at them here, right. In this fluorescent lighting, I can take them to the window where the colors are different. You know, it's, it's, it's a very demanding application. Um, and, and people are picky, especially with color photocopiers. Like that, that doesn't look right.

**Ted Yapo:** Right. Human eyeballs have their own like log scales and like weirdness like that. Right.

**Ted Yapo:** Absolutely. Absolutely. And, you know, and, and, you know, inks react differently. Some of the inks fluoresce in under fluorescent lights, right. They, they look different than, than in, um, you know, natural lighting for, for a number of reasons. And, and it's, uh, you know, it depends on the paper that people, you know, typically throw the cheapest paper they can find in there. And that doesn't work very well. So, so, you know, it's, it's, uh, adjusting your algorithm to a whole bunch of different parameters that people could throw at it. And, and, and, and you're just constantly tuning and tuning and tuning and trying to do that at speed. Right. Right. Because you, you have to keep up with, you have to keep up with the scanner and you have to keep up with the printer. And, you know, you don't, they don't spend a lot of money on buffering. Now, you know, these days it's easier because memory's cheaper and the processors are, are cheaper. Um, but it, you know, in, in those days it was a real challenge to, to make everything work at speed.

**Ted Yapo:** So then that was the end under the vision type stuff or, or still. Yeah.

**Ted Yapo:** And then, and then later on I did, um, I went kind of, um, you know, after, after the networking startup, we, we, um, we were acquired by Cisco at some point. I stayed there for a little bit. And then after that did some consulting, uh, with a couple, a couple of guys from, that I worked with, uh, previously. We just did some consulting and embedded systems, you know, generally. And, um, then I decided I want to go back to graduate school. Oh, cool. Yeah. So I did some computer vision stuff there. Um, this was midlife, you know, mid thirties or so. And, um, did that for a while. And then, um, so it was, it was like LIDAR based computer vision stuff. Oh, yeah. LIDAR was, LIDAR was just kind of hitting the, um, hitting the scene at that point. And, uh, it was, you know, it's kind of scene analysis from LIDAR and not, not just, you know, the LIDAR, little LIDAR sensors you, you buy today are just distance sensors, really. I mean, and they're just used as, I just want to measure the distance. Uh, you know, I don't want my robot to roll down the stairs or whatever. Um, but, uh, you know, these are scanning LIDAR. So you could, you could get an image, a depth image of a scene, um, and doing analysis in there. One of the, um, papers I did was for finding, uh, and this, it didn't even actually get published, but this was, this was some of the most interesting work that, that I thought was finding, um, telephone wires. And power wires from LIDAR.

**Ted Yapo:** Oh, yeah.

**Ted Yapo:** Because it turns out they're, they're a tremendous hazard to, um, uh, uh, military pilots, helicopter pilots and, and those sort of things. Um, you know, wires, they're tough to see, uh, visually and, uh, and, you know, they're, they could be a real problem. And so, um, you know, how do you recognize these things from, from LIDAR scans? And so that was, that was an interesting problem. Um, and then, and then I also did some, um, kind of transitioned into augmented reality stuff. And so you see AR and VR today, and it's, it's a lot of, um, either image-based where you're putting things into images, right? Or it's, um, augmented reality where you're, you know, you're kind of, um, overlaying images onto, onto a scene. And, and, but the work I was doing was projector-based. So you'd have projectors.

**Ted Yapo:** Oh, kind of like, uh, Jerry, Jerry's, uh, recently completed Kickstarter thingy.

**Ted Yapo:** Yeah, yeah, kind of, except you would, you'd use like, you know, your normal office projector kind of thing to project onto shapes on a table. Or to project onto objects or project onto those sort of things. So there wasn't, you know, you, you didn't have any equipment that you kind of had to carry with you or have on you. Um, and, and a whole bunch of people could sort of share the same thing. Um, and we actually did this at room scale. So we had big projection screens that you can move around in a, in a huge space. And, um, project on those to do like for, um, architectural daylighting simulation. So you want to build a space and you want to sort of be in the space and see how it reacts, you know, during the day. And you, maybe you want to minimize artificial lighting. You want to maximize natural lighting. Um, you want to see how people react to the space that you've created. You know, depending on the time of day, the time of year, you know, you can put a conference table in the middle of the room. Well, is this going to be a problem with glare on, you know, in December when the sun is really low?

**Ted Yapo:** Oh yeah.

**Ted Yapo:** In this, you know, the way the building is oriented. And so these are, these are kind of things that, that architects, um, designers want to explore. And especially when you, you know, you have a client there, they don't necessarily, they can't necessarily visualize it in the same, you know, in, in CAD or in, in models as well as they can be just kind of sitting in the room. So the idea was to build, you know, room scale simulators of, um, of design spaces.

**Ted Yapo:** I mean, it sounds like that's, uh, going to be a high-end architecture firm because that sounds like a high-end, uh, piece of equipment as well.

**Ted Yapo:** Yeah. I, you know, I mean, it was, it was cobbled together, uh, in typical, you know, kind of grad student fashion was cobbled together from whatever we could find, right? Uh-huh. Yeah. Yeah. That we could have. And, uh, and a lot of it was-

**Ted Yapo:** Dumpster finds and stuff like that.

**Ted Yapo:** Yeah. And a lot of it was borrowed. I mean, we just, just couldn't afford to, to have that stuff and, and really didn't have a need, you know, for it full time and long-term.

**Ted Yapo:** Yeah. Grad school. I mean, that, that's interesting too, of like the going back to grad school kind of midway through your career. I mean, was that, was that a tough transition back into the academic life or was it just more like working in a lab kind of?

**Ted Yapo:** You know, it, it was at first. It's, it's kind of weird. Well, the, the mistake I had was, you know, I, I kind of, I got into a position in my career where I thought, you know, this is the opportunity I have to do it just because of the way things worked out with the startup and, and the situation we were in at home. And I thought, you know, if, if I'm going to go back to grad school, this is my shot. And the thing I didn't kind of factor in was I had two young kids at home. And so like, you know, the, the amount of time, and, and they were one and two years old. And I thought, oh, well, they're one and two years old, you know, in another year or two. What could they possibly need? This is going to be easy. Right. This is going to, this is, this is the hard part. It's going to be easy when they're three and four and five and six. And it, it isn't. Um, and so, uh, that, that was a real challenge to balance that. Um, you know, I, I have a lot of respect for people who, who go through that. Um, it was, it was very, it was very difficult. Um, you know, as, as a grad student, I did my master's when I was in my early twenties. Uh, and that was kind of a slog. Right. And then, you know, but somehow I didn't, I didn't factor in the, the other. And then going back, like, you know, if you've been out of school for 10 years, there's a lot of stuff you forgot.

**Ted Yapo:** Like, uh, like day-to-day knowledge kind of stuff.

**Ted Yapo:** Like just fast access memory type stuff. Hardcore, you know, like, you know, I had to take qualifying exams and like linear algebra, for instance. I took a linear algebra class when I was an undergrad and it was just like the most opaque subject I could imagine. And I, I was just like, I don't remember any of it. I mean, and I didn't end up using it in my career, in my work. And so it just, it was all gone. Yeah. And so, you know, when I said, oh, I need to learn this again. Um, you know, I picked up a book and I'm like, yeah, it's just as opaque as, as I thought it was. And then I found these online lectures, you know, MIT has these open courseware lectures. I don't know if you've, you've seen these. Yeah.

**Ted Yapo:** Yeah. Yeah. The MIT X and yeah.

**Ted Yapo:** Right. Yeah. And so, um, you know, I found, uh, a Gilbert Strang's lectures on, in his linear algebra course and went through those. I'm like, oh my gosh, this isn't that hard. This just makes sense. Just the book suck or what? Yeah. Yeah. The, the, the way it's presented is, is just, um, I don't know, just from a theoretical point of view, as opposed to this is how this works and, oh, and here's why you want this. Here's how it, here's how it applies. And for me, that, that's very important. If I can't break it down into how would I use this myself?

**Ted Yapo:** Yeah.

**Ted Yapo:** I, it, I just, the information just evaporates.

**Ted Yapo:** Yeah. Yeah. The give a shit test. Like, why should I give a shit?

**Speaker ?:** Exactly.

**Ted Yapo:** Yeah. It's tough too. I mean, like, and I feel like if, you know, I've, I've harped on this on the amp hour for years now, but like, if they would pull a piece of test equipment into the room when they're showing you the math, it's like, Hey, look at this. This was made with an FFT. Now we're going to learn FFTs. Like, oh, okay. That's cool. I want, I want to know that, you know, that that's very relevant to my interest because it's right in front of me, you know, it's just.

**Ted Yapo:** Yeah. Yeah, absolutely. And I, and I think what happens when you don't do that is, is the folks who don't have that learning style kind of self-select into becoming professors. That's right. Perpetuates itself.

**Ted Yapo:** I agree. Yeah. Yeah. I'm sure they're, they're very talented as well. Like I said, yeah, they are self-selecting of course, but. Absolutely. Yeah. The, the culture, the culture, we're really talking about the cultural side of it, right?

**Ted Yapo:** Absolutely. Yeah.

**Ted Yapo:** Well, that's a, yeah, that's a fun reintroduction then. Yeah. Yeah. Yeah. I, I, I had a very tiny taste of that when I, I was convinced by a former coworker that I should, I should get my professional engineering license. I was like, oh, great. And this is like six, six, seven years out of school. And then I'm like, oh, I have to go take the fundamentals of engineering exam now. And it's like, you know, just a, a, it's a smorgasbord of, of all, all engineering knowledge. And I, uh, I had a real tough time with thermodynamics and the stuff I had tough time with the first time around. It was, it was, I luckily passed, but then I didn't end up using it. So, yeah.

**Ted Yapo:** Oh, well. I've, I've, I've, I've, I've known people who've gone through that. It's a grueling thing and grueling course. And, um, yeah, I guess it's important, right? If you're going to sign off on a big projects, you got to know your stuff.

**Ted Yapo:** Yes, you do. And I have not signed off on a big project yet, uh, nor have been, I offered a, a scenario where that is the case. Right. That's okay. That's okay. I don't want to anymore. Um, so you did some consulting for yourself though, right? I mean, that's, I guess that's one space where a PE might be useful. Consulting, stuff like that. What did, what did, what did that look like?

**Ted Yapo:** You know, um, uh, most recently, well, initially, you know, I had a, I had a few partners and, um, you know, we did, we did some work for, for folks we'd, uh, worked for as employees before. And, and they had plenty of work and were able to hire on consultants and the consulting work I've done since then on my own, again, has mostly been, you know, with people that I've, that I've either worked for or worked with before. It's, it tends to be the kind of easiest way to find, um, clients. And in many cases it's, you know, my phone rings and it's somebody that needs something. I'm not going out there and hustling and trying to find work. Right. Yep. You know, which is great. Um, and I think that's, you know, you hear a lot about, oh, how do you grow your business? How do you, but those connections are key and they, and they lead to, you know, if it's not them, it's somebody they know or somebody that they've worked with in the interim. Um, you, you just, you just can't beat that kind of network if, you know, once you build it. And the, and the problem is it takes time. Yeah. Yeah.

**Ted Yapo:** Which is, I think proximity, even so like I'm from a social network proximity kind of thing of like, you know, how many hops away is it? How well did they know you? That kind of thing. Like a really strong connection of mine might introduce me to a weaker connection of theirs, but because that strong connection is in between, it's, it's relatively close in terms of that, you know, in my own experience. And, uh, and then I think geographic proximity as well, that really helps if you're near somebody, if you can go talk to them in person, even if you don't know them that well, if you can go sit in a room with them, it's like, oh, okay. So that's, that's a much more likely, uh, scenario to get some work, I think.

**Ted Yapo:** Yeah. That's the whiteboard factor, right? If you can get together in front of a whiteboard and, and try to explain yourself, you know, it's, it's, it makes it a lot easier.

**Ted Yapo:** It's not a lock, but it's, it's a lot better. Yeah. Right. Yeah. Does that mean that a lot of your clients were, you're New York based?

**Ted Yapo:** I'm New York based. Yeah. I, when, um, mostly, uh, I worked in Massachusetts. Oh, okay. So, you know, not that, not that far away.

**Ted Yapo:** Yeah. Um, New England-ish area. New England-ish, yeah. Yeah. Yeah. That's cool. Yeah. I mean, and I mean, New York itself has a lot of, I mean, a weird, like East Fishkill. That one always gets me. I know some people in that area, but like, wow. That must've been like some sick tax break because it's near Albany and like, that's where the capital of New York is. And like, that must be why that's there. But that, that place never ceases to amaze me. It's like, you're in the middle of, middle of nowhere. You knew the Catskills kind of, right? But like, um, beautiful area, but it's like, okay, now we're going to plop a bunch of fabs there. And say, oh, okay.

**Ted Yapo:** There's, there's a bunch of little pockets, right? Yeah. Um, like that. But yeah, I'm kind of, I'm kind of in the middle of nowhere part of New York. So. Yeah. That's nice too. It's just North Albany. Yeah, it is.

**Ted Yapo:** It only hurts if you're trying to branch out with the network, but I guess the internet helps that. And that's something that you have done quite a bit lately. And that's kind of what we're talking about here is your, your projects that you've posted, uh, to Hackaday and other, and Twitter and other places. So, uh, when did, when did that all start?

**Ted Yapo:** You know, probably, I, I actually, I know exactly when it started. So the 2016 Hackaday prize, uh, I, I don't know how, somehow I didn't, I just, I wasn't aware of the prize before. Obviously I knew Hackaday for years, but somehow I didn't get the, I don't know. I didn't, didn't realize that the prize existed.

**Ted Yapo:** Well, if someone helped run it for the early years, that's on me. So sorry about that.

**Ted Yapo:** That's probably on me because I was, I was busy with other things. Um, but, uh, I, I figured out, well, yeah. Oh yeah. Okay. I'll, I have a project I can submit to this and that, in order to do that, you need to post it on hackaday.io. I'm like, okay, well I'll make a project on hackaday.io. And I did that. And that was the diode clock. That was the first project I really, really published online.

**Ted Yapo:** First of 51 projects that are online. So people, people have a, uh, a relative measure here.

**Ted Yapo:** Right. And, um, that took, uh, that took a prize in the first round. So I won a thousand dollars for that project. And, um, I won another round that, that year too. And sort of that, that got me doing it. I was like, oh, this isn't, you know, obviously it's nice to win a little cash. But, um, the thing I realized right away was documenting something for somebody else to read really makes you, you have to understand it and you have to, um, and you have to kind of go beyond the level that you normally would with, or that I normally would with a project. You know, to document it, you need to push, you need to like, you can't just say, oh, I kind of get what would happen here. Yeah. Right. Yada, yada, yada. Yeah. Right. And when that, and I kind of tricked, I, you know, fool myself a lot when I work on my own, like, oh yeah, I understand how that, how that's supposed to work. I kind of get this. And when you're documenting it for somebody else, you can't really do that.

**Ted Yapo:** Yeah. I always think about that with, uh, with textbooks, you know, when you see the answer to the problem, you're like, oh yeah, I would have gotten that answer. You know? Right. Well, where's your work, Chris? There's no work here. Right.

**Ted Yapo:** Yeah. Yeah. It's different when you have to do that. And the other thing I realized very quickly was I could, I can search stuff that I put online much easier than I can find stuff in my lab or my office or wherever. You know, if I had Google for my house, I would be, you know, it would be great, right? Google for the workshop, Google for storage, and, you know, Google for the crap that's on my desk. You know, that would be awesome. The next best thing is to document it somewhere where I can search for it. And I can't tell you how many times I do that. Like, oh yeah, I did this before. Did I document, did I put this online? And look it up like, oh yeah, that's how it works. All right.

**Ted Yapo:** Yeah. Yeah. And then, yeah, I mean, that's like putting your brain online. I think that's like, uh, I use Evernote for that kind of thing. And that's like what they talk about. It's like, or I guess it's the getting things done method too. It's like using, getting outside of your own head. You can't store that much stuff in your, in your short-term RAM, you know? Right. And, uh, using a notebook for that kind of thing helps. But, you know, I think this is effectively acting as your notebook too.

**Ted Yapo:** Yeah. Yeah, it is. And the other thing that happens obviously is, is you get feedback from people. Yeah. You know, you get people using things.

**Speaker ?:** On the internet.

**Ted Yapo:** People are always so kind on the internet.

**Speaker ?:** Right.

**Ted Yapo:** Well, you know, I, I think, I think this kind of space that we live in is a little bit different, um, in terms of signal to noise ratio. I, I think there, you know, there, there, there been some cranks, um, but, but mostly it's people who are, you know, who are just interested in things, either have, you know, a, a, a, a, a different or better way to do it, or want to apply what you've done to, to their own situation. You know, an hour before we started this morning, somebody, uh, pinged me on Twitter and said, Hey, I just, I saw your presentation from Supercon last year. I'm reading your paper now. I just made a scalar network analyzer. I'm going to try to apply your algorithm. Oh, no way. That's great. Yeah. It was like literally this morning I was, you know, I was setting up here and I'm like, Oh, what is this? Oh, somebody is going to use my stuff. That's great.

**Ted Yapo:** Yeah. It's like upping, upping your serendipity quotient. Right. Yeah. That's great. That's really great. And I definitely want to hear about that before we go on though. What is the diode clock?

**Ted Yapo:** Since you mentioned it. Yeah. So, um, when I was a kid, I was, this was probably 1981, 1982. Again, it was a Radio Shack book that, um, that my parents got me and there were these, the diagrams and it was a, how to, you know, how computers work or the basics of digital logic or something like that. I don't remember the exact book, but they had these diagrams in there of like, and an or gates that were made with, you know, just diodes and resistors. So, you know, how, or you have two, two diodes and, you know, to make an and gate, um, either one of them can pull the output low, right? If you have a pull up and either one of the diodes can pull. And so they, you know, you see these, sometimes you see these things in, you know, where people are, they don't want to spend any money on a real gate or, or whatever. Um, or we used to see them in like diode ROMs in the early days, people would make their, you know, the boot ROM would be, you know, you just need a few bytes and you make it with diodes. And, you know, as a kid, I was what, 11, 10 or 11. I thought, ah, I'm going to make a computer just out of diodes. And, you know, it's a reasonable thing to think, right? Here's an and and there's an or gate. Um, and it turns out you need a couple more things to actually build a computer, right? Because first you need an inverter, which you can't just do with diodes. Uh, and you need some gain because you start changing just and and or gates together that are made with diodes. And, you know, you don't have any, you have gain less than one, obviously. And so, you know, sequential logic is just out. You're never going to make a flip flop. You can't have memory. And, you know, so you can't have a computer. Um, and I thought about this for a long time. Oh my God, there must be a way. There must be a way. And probably around 2002, 2001, 2002, I was doing some work with pin diodes, pin diode switches for, um, I was building a Doppler, uh, radar. Oh, cool. And, uh, and so.

**Ted Yapo:** Oh, this is like the, uh, yeah, I think Greg talks about that in the coffee can radar thing. It wasn't coffee can radar, right?

**Ted Yapo:** Yeah, no, no, it was, uh, it was, uh, just, um, um, uh, a Doppler radar made with, um, you know, four or eight antennas that you switch rapidly in succession. Oh, cool. Okay. You need to emulate a, uh, a rotating, uh, uh, antenna. Yeah. And, um, but you know, you, you use pin diodes to do this RF switching and pin diodes are, you know, they're just one of these kind of esoteric kind of diodes you hear about that you, you pass a DC current through them and then all of a sudden they have a low, uh, impedance to RF. And the, the interesting thing about them, you see them in amateur radio transceivers all the time and, and, and all sorts of radio, um, you can switch more power than you put in. So it's really like a, it's really like a switch. You really can achieve amplification if you want. I thought, Oh, that's it. So I'll use a pin diode to switch RF and then I'll rectify that RF. Like, you know, you think of a crystal radio, right? You're taking RF and you're making DC output and I can use that to drive the next stage. And so I, you know, I was able to prototype this relatively quickly. And then I realized that you can use, um, rectifier diodes, big, slow rectifier diodes. You know, your 1N4007s that you see, the big one, um, they work as really crude pin diodes. So between those, yeah. Uh, at certain, at certain frequencies they're, they're good. So between those and some silicon switching diodes, right? Your 1N914s or 4148s or, or, or whatever, just with those two kinds of diodes, you can make logic gates, any kind of logic gates. So you can make NANDs and NORs and flip flops and everything you need to build a computer. Now there, I mean, without, if you used real pin diodes and Schottky diodes for, um, you know, that, that were real RF components, you probably could make this go pretty fast. Uh, I re I wanted to make it with the kind of junk you find on, you know, that you sweep up after a day in the lab, which are these, you know, these, these commodity, commodity diodes you never think anything of, right? You, I mean, you see them in power supplies and, and wherever else, but otherwise you don't think about them. And so, um, came up with the circuit that would do it. It took a little doing because they're, they're very inefficient as, as pin diodes and you don't get a lot of amplification. So I needed a couple of stages, but I was able to build a logic family out of them. And as an example, I built a digital clock that just uses diodes for all the counters. That's great. And, and of course, you know, the, the display is led, so that's diodes too. Uh, and the only thing that isn't diodes is, uh, you know, I have a time base that's not diode based because I wanted it to be relatively accurate. Uh, and the power supply, because it requires an RF power supply, um, you know, to run it. So that, that was actually the project. Yeah. Go ahead.

**Ted Yapo:** Yeah. But this also seems like it gets a little out of hand. So I'm just looking through the, the, uh, completely out of hand. The instructions, which you people can go and read on the hack. It will link all the pages and stuff. Step one, build 46 DDL01 hex nor boards. This will include starting over 7,000 components. So allow yourself at least a few weeks. Uh, what?

**Ted Yapo:** Yeah, they have an instruction section on the page. So I filled in, you know, what you'd need to do. Yeah. It's had 46 boards and they're like, I'd like three by four inches. They're not, they're not small, you know, and they're all through hole components. So, you know, you bend a couple thousand components and stuff them in the board, flip it over, solder it. It was, it was a fun summer. Yeah.

**Ted Yapo:** Yeah. The entire summer, I'm sure. Um, so, so you need so many cause like each board is what? Like has a couple of nor's on it. Is that the idea? Each board is six. Yeah. It's a hex nor. Yeah.

**Ted Yapo:** And, uh, and I went with hex because you could make a flip flop. You could make a negative edge trigger. Oh yeah. D flip flop with six nor gates. Uh huh. Um, and so, you know, and depending on how you set jumpers on the board, it's a, it's six nor gates or it's a flip flop or it's, um, three RS latches.

**Ted Yapo:** Oh, nice. Okay.

**Ted Yapo:** And then, you know, you can just use the same board for, for different parts of the clock.

**Ted Yapo:** Did you do a cost comparison of what it would be to buy a hex nor in a chip form versus a, uh, this is a dumb question to ask. I'm sorry. That was a dumb question.

**Ted Yapo:** If, if I ever wrote down how much that project costs and my wife found out about it, I'd be in trouble. So, you know. Yeah.

**Ted Yapo:** I'll just bleep out this entire section.

**Ted Yapo:** That's right. Oh my goodness. A lot of those parts were eBay finds. And in fact, the, the, the design, you know, I had to tweak the design because the inductors I found, I found inductors incredibly cheap. Um, and I think I have the world's last supply of those particular ones cause they were, you know, they stopped making them. And so somebody had this warehouse full they were selling and I, I picked them up dirt cheap and I had to build the circuit around the inductors that I, that I had. So I had to tweak the other components to make that work.

**Ted Yapo:** So I'm not sure I quite understand the, the, how, how it's working here though. So you're saying, okay, so the one, one N four O seven is, is working as the pin diode. What is the frequency that you're passing through it that you then rectify?

**Ted Yapo:** All right. So the power supply is around six megahertz. Okay. So that's, that's the power supply. It's not five volts. It's not three and a half. It's six megahertz, um, and it's plus or minus 12 volts approximately, you know, it, it, it varies a bit, but essentially have this big, you know, the six megahertz square wave and there, you know, there are harmonics obviously. Um, and with the, with the pin diode or the one N four O seven that's standing in as a pin diode, if you send it, uh, apply a DC bias across it, use an inductor, right. To apply a DC bias so that the RF doesn't get back into your DC supply. Um, you apply a DC bias to it, it, it kind of shorts out that RF energy, right? So, so it's a chunk. It's, it's used in a shunt pin switch. Um, and so if you, if you apply a DC bias from one of the inputs that shuts off the output. Got it. So that's an inverter. All right. And, and the output at that point is RF and you just rectify that with a couple more diodes with some faster diodes. Got it. And then it becomes DC again and you can use that to switch the next stage.

**Ted Yapo:** I see. Okay. That's the piece I was missing. So that's because the signal then gets switched back to, so then, so then you'd see the six megahertz power supply going to everything as like the, that's like the rail effectively. And then you're saying that this, yeah. Okay. Then the DC is what, so that first DC signal that gets pushed through is that, uh. That's the logic. That's the logic.

**Ted Yapo:** That's, that's the logic signal. Right.

**Ted Yapo:** Cool. Wow. Yeah. That's weird. And then, so the end of this, so looking at the picture, it's like basically just showing like a binary clock then at the end of the day, like large scale.

**Ted Yapo:** Yeah. Yeah. It's just a big, it's just a big digital clock. Yeah. That's great. That's great.

**Ted Yapo:** Okay. Well, that's, uh, a large, I mean, it was what, what was the approximate, uh, dimensions on that kind of thing?

**Ted Yapo:** It's about two foot tall. Okay. I have, I think I have it somewhere. I don't, um, yeah, it's about two feet. I built this wooden crate for it that for storage, because I took it, I took it to like a maker fair and I took it a couple of places and I, and I still have it in my office, like in the corner and every once in a while it's, you know, it's bolted. It's this big wooden crate bolted together and I have to get the socket set out and unbolted

**Ted Yapo:** and I take it out and look at it for a while and I put it back. The arc of the covenant at the end of the, Indiana Jones. Yeah. So, well, uh, what else, I mean, what are some of the other, uh, projects that you like talking about on your, on your page? I mean, cause you do have a couple here.

**Ted Yapo:** Yeah. Yeah. So there are a couple. Um, so, so one is the, is the Tritiled, Tritiled. I don't even, I made up the name. I don't know how to say it. Um, but, but essentially, essentially it's, um, it's an, uh, a battery based led that, you know, can run for 10 years. And so when I was, um, I used to be into a lot of astrophotography and I was constantly tripping over stuff because you work in the dark, right? Um, and you've got a tripod, you got three legs and you got two of your own and inevitably they get confused and you trip over and you, you know, break some expensive equipment or you hurt yourself or both. Um, and so I was looking for a good solution to, to put on the tripod legs so I could see them in the dark. And, you know, you can, you can buy glow in the dark stuff that needs to be charged up. So, you know, and then it, and then it fades over time. Uh, the perfect thing is these Tritium lights that unfortunately you can't buy in the States just as markers, right? You can buy Tritium, uh, and, and what they have is they, they have radioactive Tritium and a phosphor in there and it closes typically tritiated water in there. And, uh, the Tritium's radioactive, uh, and it makes the, the phosphor glow. Um, you can buy them in compass compasses in the U S you can buy them in watch styles.

**Ted Yapo:** Oh, okay. So it's like the, uh, what they call it? The glow something, uh, I forget what the brand name was. It used to be like the hand, the hand makes watches. Okay. Okay. Yeah.

**Ted Yapo:** Yeah. Yeah. Uh, and so you can, you can buy them in certain, oh, and in gun sites, of course, in the U S you can buy them in gun sites. Um, but you can't buy just markers that, you know, and you can find them on eBay. They're illegal to import, but you can find them if you want. But I thought that's the perfect thing. What if I had an electronic one? And so you can get, you know, you could, I mean, you put a, uh, a battery and an led together and maybe a resistor. So it's not that bright cause you don't want to blind yourself at night. Um, and you know, you have to change the battery often and it just doesn't make a lot of sense. So I said, well, how far can I go? You know, with a, with a small coin cell, lithium coin cell, like a CR 2032, um, and a, and an led. And it turns out you can, you can light it for 10 years. Wow. Um, mostly.

**Ted Yapo:** Fully on or not fully on, but like on. Not fully on.

**Ted Yapo:** Yeah. On, I mean, on, you can certainly see it in, in, uh, at a 10 year rate, I don't think you can see it in daylight, but at a one year rate you can. Um, and certainly at night you want to, you need to turn it down anyway. And so I had these little things that just fit there. It's just a little bit bigger in diameter than the CR 2032. Um, and, uh, I found some plastic cases on eBay that they fit into and you can build these things and, you know, it has a little button on there. You can, you can set the, the, uh, the run rate, you know, from one year to 10 years and just put them anywhere. So I was, you know, I was walking around here today in the, in the, um, in the shop. I was digging through some of the drawers and it's just that there's a little, you know, green glowing light in the back. Oh yeah. There's another one. I just have them everywhere, you know, anywhere I need to mark something. Yeah. Um, and people have, people have written, you know, that they, they make them, they put them on the corner of the sofa so they don't hit their, you know, hit their leg at night when they go to get a glass of water or whatever.

**Ted Yapo:** Yeah.

**Ted Yapo:** Um.

**Ted Yapo:** Yeah. Cause you just need like a location finding more, more than you need an actual lighting. You just need to know relative locations really of, of like hard objects.

**Ted Yapo:** Yeah. And that, and that was, that was the idea. And it turns out there's a commercial application, um, uh, for this, there, um, there are still film processing companies that make, you know, photographic film. Really? And, and yeah. And they make them and they, you know, they get them on these big rolls and need to cut them up and put them in, you know, smaller packages. Uh, and they need to work completely in the dark. Obviously it's not all automated. They have people working in there. And in some of these, um, some of these factories, they actually use the tritium lights that we talked about earlier, that these radioactive lights, and there's this big push to kind of get rid of them because somebody has to make the tritium and trade, you know, the U S doesn't want tritium all around the world because tritium is an, is an important component of certain, certain weapons.

**Ted Yapo:** Yeah.

**Ted Yapo:** Um, and so, you know, there's a, there's a push to kind of not use these things anymore for, you know, I don't know if the reasons are well-founded or not, right? There's some irrational fear of, of radioactive stuff out there for sure. Um, but in any case, if they get legislated away, they need a replacement. And so these could work.

**Ted Yapo:** So, so what is the, what's on board these things then?

**Ted Yapo:** So there's actually a microprocessor on there. Okay. This is a pick, um, a 12, you know, 12 F pick, uh, eight pin, eight pin. Yeah. Yeah. Eight pin. And, and it has like incredibly low, um, sleep current. And in fact, the thing is asleep for most of the time. It just, it, when it, when you turn it on, it configures some things and it uses, um, the built-in, uh, pulse width modulation, um, circuit on there, uh, to drive the LED. And, and the way it works is, um, the PWM triggers a one shot that produces a very small pulse of current. That pulse energizes an inductor and across the inductor and kind of, and kind of flyback with the inductor is the LED. So you've seen, um, diodes on relay, uh, coils for instance. Sure. Right. To absorb the kick when the, yeah. In this case, it's an LED. And so you're using the kickback to drive the LED. Yeah. And it turns out to be a very efficient way to do it. So you control the amount of current and time that you energize the inductor for, and then that's how much, you know, ends up energizing the LED. And the, the, um, the key thing about this is with modern LEDs, they're extremely efficient at, at a specific current. So you can, you can measure the efficiency of the LED versus current. And there's one specific current. It depends on the size of the die, the LED die and the, and the specific physics of the LED at which they're efficient. Above that, you get what's called droop, which is one of the big factors in LED lighting. If you drive them with more and more current, they become less and less efficient. It turns out the same thing happens with very low currents. So if you just take a, um, a normal LED and use a very big resistor and a battery to try and make a dim LED that will last a long time, the LED is very inefficient at converting that electrical energy to light energy. And so what you want to do is you want to drive that LED with very short pulses of the current at which it's most efficient. Yeah. And then overall, it averages out.

**Ted Yapo:** Yeah. Right. Right.

**Ted Yapo:** Yeah. And so you're, you know, if you drive them at 120 Hertz or something, you don't see the, you don't see the blinking.

**Ted Yapo:** Right.

**Ted Yapo:** But the LED is coming on for a very short period at its most efficient current and then, and then turning off. Wow. You know, with a very low duty cycle.

**Ted Yapo:** Well, how did you go about testing this? Because I'm guessing you did not test it for 20 years. So how were you?

**Ted Yapo:** I did, I did not. No, I didn't test it for 20 years. I've had several that have, that have been on for, for a number of years now. Yeah. I think the earliest ones I have are, are probably two years old.

**Ted Yapo:** That's great.

**Ted Yapo:** Um, and, uh, the, the first model would had about a year, um, a year life. And I've been through a number of those and I had to change their batteries, but, uh, it's based on, um, it's based on the current draw versus, you know, the, the expected lifetime of the battery. The battery manufacturers will typically give you curves, you know, voltage versus time for different drains. And so you can take those curves and actually found some software that can digitize graphs out of, uh, data sheets. Yeah. Yeah. I've seen that. So you can actually get numbers back and then use those numbers and calculations and, and just measure the characteristics of your device. So at, you know, at 3.1 volts, when the battery's fresh, it draws this many current, this much current at 2.9, it draws this much. And you come up with a curve for your own device and you can mix that with the curves from the battery manufacturers and predict the lifetime. That's great. And of course, you know, it's, it's all a guess, right? Cause you don't know what the temperature is going to be, if these things are inside or outside or, or whatever. Um, you know, it's, it's a best guess, but so far it's, it's been, it's been pretty accurate.

**Ted Yapo:** That's great. I always wonder about the, so I used to do that a lot with like the data sheets, graphs and stuff too. I'd be like, and usually I was just interpolating just myself, you know, like doing a real straight line ruler type thing. Um, but I was like, thought like, well, they didn't test every point here. And what if there was like a hidden spike between two points of data or something? You know, it's like, I'm going to find it if I find it. But like, you know, like graphs are only as good as the graph makers and, uh, you just kind of cross your fingers and hope for the best.

**Ted Yapo:** And then, and you know, this is what they say about data sheets, right? The typical means they saw it once in the lab. That's right. Yeah. Yeah. So, you know. Yeah.

**Ted Yapo:** Got to be careful of those typical figures. Yeah. Right.

**Ted Yapo:** Yeah.

**Ted Yapo:** That's cool. That's really cool. And so, so the idea then is just to have these hanging out for as long as they last, huh?

**Ted Yapo:** Yeah, exactly right. Yeah.

**Ted Yapo:** That's, that's a great idea. That's a great idea. And so what about the astrophotography? Have you, have you avoided kicking any tripod stands since then? I have. Yeah.

**Ted Yapo:** Yeah. Yeah, absolutely. They, they work. Yeah. That's cool. You know, you can do, you can just do, you can glue them to things. You can put a little magnet on the back and stick them on there. Some Velcro.

**Ted Yapo:** Yeah.

**Ted Yapo:** Or whatever. Um, I made one that was waterproof. I dunked it in the lake a little bit. Oh, nice. Seemed, seemed okay.

**Ted Yapo:** So. Just like informal coated or something?

**Ted Yapo:** I, you know, I put an O-ring in the case. The case screws off so that after your 10 years or whatever, you can change the battery. Um, but you know, I think, I think these cases are cheap enough. You could just seal them with silicone. And when you need to change the battery, just crack them. Yep. Yep.

**Ted Yapo:** Uh, well that is a, uh, you know, low and slow and a long lifetime project. Let's go in the exact opposite direction at your latest, uh, latest thing. You've been working on an eight gigahertz sampling oscilloscope and I'm seeing a purple PCB. So I assume this is off the shelf parts and, uh, PCBs from the old Oshpark folks. Is that, is that right?

**Ted Yapo:** It is. Yeah. Yeah. The goal was, um, was to make it with, you know, stuff you could order from us or a digi key.

**Ted Yapo:** Yeah.

**Ted Yapo:** I mean, that's like everything has got to be, you know, commodity parts. Yeah. Um, because. Maybe not cheap though, but. You know, it's surprisingly affordable. I think. Really? Okay. I think the bomb right now is under a hundred dollars. Oh, okay. Wow. PC board. Um, it may go up a little bit, you know, I'm in prototype two now. It needs a couple of things like the power supplies are off the board. Okay. Right. So if you want to run it off USB, you're going to need some switching supplies on there to get the various voltages you need. Um, I need a beefier micro on there, you know, some more memory and those sorts of things. So it might break a hundred bucks, but it's not going to be that much more. Um, yeah, so this, you know, this initially came out of the research I did for the diode clock because I was researching diode switching circuits and, you know, there's a whole bunch of pin diodes were one. And then I, I stumbled across the, you know, shocky diodes for, for sampling. And I'm like, what, what is this? So I looked into it and it turns out that, you know, for many years, the fastest oscilloscopes used, um, used diodes to sample their input, right? Schottky diodes. You can look at, so I have on my desk here, a, um, uh, Tektronix S4 sampling head from 1968. It was introduced in 1968 and it achieves a bandwidth of 14.5 megahertz. Oh, okay. Gigahertz. Not megahertz. Oh, I was going to say, oh, well, you know. Yeah, megahertz is no big deal. Yeah. No, 14.5 gigahertz. Wow. And so you think, well, how did they do that in 1968? Right. And you start to look into it like, oh, it's just six diodes in the front end. That's it. Really? There's some resistors and capacitors and stuff. Yeah. And so it turns out Schottky diodes, and you can buy them today with the same characteristics, can switch in 10, 15 picoseconds. Wow. And the whole idea is you switch them on briefly and get a sample of the input and then turn it back off. And if you do this at the right rate, you can reconstruct the input signal.

**Ted Yapo:** And are you like kind of doing round robin where you like have the different diodes doing like offset from one another or what?

**Ted Yapo:** No, they're all doing the same sample. And so the way it works, and this is the real interesting part is these sampling oscilloscopes use kind of a stroboscopic effect, right? If you think about, you know, you want like an old movie, right? A silent film with wagon wheels. You know, you'd see them move, you see them like, they look like they're rotating backwards. They look like they're stopped or whatever, because, you know, there's interference and aliasing between the frequency of the wheel turning and the 24, you know, hertz of the camera or whatever. But you can do the same thing with waveforms. So, you know, if you and I think of an oscilloscope today, a digital oscilloscope, well, you've got this analog to digital converter on the front end, and you run it at, you know, what, 100 mega samples per second. And they may be interleaved, like you mentioned, but let's say they're not. Let's say you actually can run at full rate with one EDC. You sample, you know, every nanosecond and you, you know, jam it into a fast RAM and then you save all these samples and you apply your sync reconstruction or whatever you want to do and you reconstruct the data. It turns out you don't need to do that if your signal is repetitive, which for a lot of signals, that's a good model, right? Let's say you have a sine wave, well, you know, one gigahertz sine wave repeats every nanosecond, right?

**Ted Yapo:** Yeah.

**Ted Yapo:** And so you can take the first sample right after your trigger point. And then a couple of waves later, you can take the second sample. As long as it's the right place from your trigger point on the waveform, it doesn't matter that you took it then or you took it at the beginning. And so then you can take the next one in a week and you take the third, you know, the fourth sample a month later. And as long as everything's stable, your sine wave doesn't change, frequency doesn't change, amplitude doesn't change. You can do that. You can extend that time as long as you want. They call this equivalent time sampling. So you can actually sample, you know, I have in the lab here, I have a Tektronix 11801 oscilloscope. This is from 1989 or so. And in there, I have a 20 gigahertz sampling head. This 20 gigahertz bandwidth sampling head runs at 100 kilohertz. So it's only sampling every, you know, at 100 kilohertz. And yet you can reconstruct signals that have 20 gigahertz components. And this is extremely powerful.

**Ted Yapo:** Yeah. I think I'm a little confused here still. All right. So I think with a stereostropic thing, stereostro, strobostropic, is that right? Yeah. Strobostropic. Stroboscopic. Scopic. Okay. Scopic, scopic. Stroboscopic. I'm going to write that down so I get that right. What I'm thinking about is like thinking about sine waves like you're talking about. And like, I remember seeing drawings in a textbook where you have, you know, you have a sample and then the next sample might be a little bit higher up and then a little bit higher up, a little bit higher up. And even though the signal is much faster, what you're seeing is basically a reconstruct slower sine wave. Is that kind of what you're talking about here? Um, yes. Okay.

**Ted Yapo:** Yes. Well, in fact, if you think of that same example where, you know, the first sample is like right at the zero crossing, say of the sine wave. And the second sample you're going to put, you know, a third of the way up or a quarter of the way up or whatever. Don't put it on that same wave. Wait a couple cycles and then put it somewhere on that. Put it at that same corresponding place on the fifth reoccurrence of that sine wave. Uh-huh. Right? Okay. So you've skipped, you've skipped the four cycles in between, but now you're going to take the same sample on the same place on a sine wave, but you've just skipped a bunch of the, a bunch of the periods. Right.

**Ted Yapo:** I guess the, the math reconstruction in my head is the hard part then. So, so you're doing the slower actual sampling. How do you then back calculate what the, to know that there wasn't a bunch, like much like my, my thing with the chart. How do you not know that there's like a blip in between the two sample, you know, data points on a chart? How do you not know that there was a huge blip between your sampling points?

**Ted Yapo:** So the, so the Nyquist criteria still applies, still applies. If you sample at, um, if the equivalent time sampling rate, right? Cause now there are two sampling rates. There's a real time sampling rate at which you're actually getting the points. And there's the equivalent time sampling rate at which, you know, that counts how far you're moving along the repetitive waveform each time. As long as the equivalent time sample rate is greater than twice the highest frequency, in the input. It's just the Nyquist criterion. You can reconstruct it exactly with sync interpolation, just, just like you can with, with normal sampling.

**Ted Yapo:** So, so then you're, how are you able to verify this on your bench then? I mean, do you need to use your, your, uh, similar 20 gigahertz head unit that you're talking about?

**Ted Yapo:** Yeah. Yeah. It's a challenge. So, um, you can compare against a known good oscilloscope. It turns out there, there really aren't any known perfect oscilloscope. There was a paper that was published by picosecond pulse labs many years ago where they rounded up nine of these sampling oscilloscopes, you know, the fastest ones in the world. And they applied the same input to them. Uh, and they all look different. Huh. You know, slightly different, right? But different enough that you'd be like, well, which one's right? Yeah. Um, and you're not quite sure. And to some extent it doesn't matter, right? At those speeds, you need to, you need to get what you're getting out of the, out of the data. And you need to understand the response of the scope itself. And really, you know, it forces you back into, you know, if you, if you deal with, um, even your, your multimeter, right? You try to measure current, very low current with your multimeter. And then you have to kind of think about meter burden, right? How much current is the meter itself taking, right? Are you trying to measure a voltage for low current? And how much, you know, how much does the meter itself change the measurement in this case? You know, it's not necessarily changing the waveform, but it's affecting what you see. And so, um, you have to take that out of the quote, but yeah, I'm comparing it against, uh, the, the 20 gigahertz sampling head I have. Um, you know, you can test the bandwidth of an oscilloscope with a really fast edge, right? So you've, maybe you've seen this in one of the Jim Williams, um, app notes. Yeah.

**Ted Yapo:** He loved doing that, that, uh, one shot kind of fast rising edge type of thing, right?

**Ted Yapo:** Right. And, um, you know, he used an avalanche transistor back in the day, they would use a step recovery diode, another special diode that just had this, um, characteristic where it would turn off very quickly. Uh, you can buy that. I found one of them at Mauser. Um, the G key doesn't stock any. And so I played with that a little bit, but really want to use, um, I wanted to use commodity components, right? Things that, that, that may be around for a little while today. And so it turns out there are a number of things. So there's ECL gates can switch pretty quickly. Oh, cool. Um, CML gates, even faster, CML comparators can switch pretty quickly. And a lot of things, a lot of parts designed for optical networking. Um, obviously if you can run, you know, 10 gigabits through a, through a, through a circuit, it needs to switch pretty quickly. Yeah. And so there are, you know, some limiting amplifiers or laser diode drivers that can switch in, you know, tens of picoseconds. Um, that's plenty fast. If you want to test your, you know, a hundred gigahertz Regal or Ciglant scope, that's, that's more than you need. Um, you know, when you get down to testing, uh, you know, an eight, an eight gigahertz scope that, you know, that's on the order of the rise time of the scope itself. So you kind of have to correct for the fact that the edge isn't as fast as you'd like. And so you kind of get into this gray area where, you know, what have I actually measured? You know, how, how accurate is, is this? And to some extent it doesn't matter, right? You just want to make sure that you're sampling fast enough so that you don't alias. Um, you'd like to understand the bandwidth of the scope, but it's, um, it becomes difficult to measure that way. The best estimate I have right now is that has about a 48 picosecond rise time. Um, and just to put that in perspective, if you're not used to dealing with picoseconds, which I wasn't until recently, it may not, may not make a lot of sense. So light travels, you know, three times 10 to the eight meters per second. That's pretty fast. In 48 picoseconds, light travels 14.4 millimeters, which is about the width of your little finger. That's so that's pretty, that's pretty fast.

**Ted Yapo:** Yeah, it's pretty fast.

**Ted Yapo:** Yeah. That's, that's the rise time of the, you know, of the, of the, of this oscilloscope. Um, and it turns out that, that the key to, to making that with commodity components these days is to kind of forget the special diodes that they used in the sixties. Um, you can still make them like that and you can still get diodes that are fast enough, but it's difficult to produce the sampling pulse that you need without the step recovery diodes that, you know, you just can't get anymore. They've, they've kind of become unobtainium. Right. Yeah.

**Ted Yapo:** Cause they're probably not doing like custom, uh, recipes for that kind of thing. They're all switching to cheaper, cheaper processes and stuff like that.

**Ted Yapo:** But that's exactly right. Yeah. Uh, and so, um, it turns out there's another architecture that came about, um, there was a master's thesis at UCLA in 1975 where, um, the idea was, it was, um, S.P. McCabe. I'm just remembering his name now. S.P. McCabe. The idea was that you could use a comparator, a fast comparator to sample the waveform. And you think, well, you know, how does that work? Right. Comparators just, there's no time component really to it. It turns out if you, if you build a comparator with a latch input, which is, is very common. They're off the shelf components these days. You can use that latch input as this, the stroboscopic input to sample your input waveform at a particular point. Um, and the, the complication is that it's just a comparator. It just tells you whether the input was higher or lower than some reference. Right. And so you can do the same thing that they do with successive approximation, um, ADCs, right? Where you, um, you take, um, a voltage, use that as a reference and see whether the input is higher or lower than the voltage.

**Ted Yapo:** Yeah.

**Ted Yapo:** And then based on the, based on the results of that, you adjust the voltage and try it again. And so you can do this kind of binary search. Yeah.

**Ted Yapo:** It's like a binning, a binning kind of thing, but with just two bins that move around, right?

**Ted Yapo:** Yeah, that's exactly right. And, um, and you just do this. And so it takes you, you know, if you've, you want 12 bits of, of converted 12 bits of ADC, it takes you 12 samples to do this. But now you've come up with an estimate of what the input is. Um, and you can do that at speed. So you can do that and, and get eight gigahertz bandwidth out of it with a commodity comparator. This is an analog devices, ADCM to ADC MP 582. It's tough to say, uh, comparator that, um, has an eight gigahertz input bandwidth in single quantities. It's less than $20.

**Ted Yapo:** Wow.

**Ted Yapo:** Not much less, but 19 something. Right. Um, I think in, I think in hundreds it's $8, something like that.

**Ted Yapo:** What's the, uh, what's the application for that usually? Is it usually doing like higher, like RF type stuff or?

**Ted Yapo:** They, they use it in, um, uh, in networking, you know, to square things up. Sure. Right. Receivers. Um, you know, they list, you know, uh, test equipment and the, the usual kind of things, but you'd find this any place you need a really fast comparison. I think the, you know, when you think, when, when you think of normal comparators, you think, oh, maybe it's a microsecond or really fast comparators. Like from the Jim William days, the LT, uh, 10, 16, right. From what that was, uh, four nanosecond, maybe five nanosecond comparator. This is 180 picoseconds. So much, much faster. Um, they're built on silicon germanium process, which is just amazingly fast. Um, and so, you know, they're, I mean, they're, they're, you know, parts from the, from 20, 2019, right. I mean, this is, this is what we have available. These are, these are leading edge things. And, um,

**Ted Yapo:** That's great. So what is the, uh, what is the status of this, uh, project then? Cause I see, I was looking at a tweet from October 2nd and it looked like you had a, uh, uh, you said an RMS error of 700 femtoseconds. Uh, but it is also showing a scatter plot that approximates the waveform, I believe. Right.

**Ted Yapo:** Yeah. Um, that probably, uh, I have to bring that up, but, uh, I think that was the, um, that's the, that's the time-based calibration. So I think, I think the error there was, um, 700 femtose seconds. It is better than that now. Oh, great. You know that I have the, yeah. Yeah. So that was, that was just some, some measurement error. So it turns out there's an, there's, part of this is, is generating the delay so that you can sample the signal at the points you want to. That's really, you know, the, the first part was getting the comparator to, to do its job. And the second part is, is, is this time base where you have need to move this sample over slightly with every reputation of the waveform. Um, and there's a part you can buy that's used for, um, uh, timing, you know, adjusting the edges on clocks. It's an ECL, um, time delay part that's adjustable. It has 10, 24 steps, and you can move the steps in roughly increments of 10 picoseconds, you know, and it might be nine, it might be 11. Um, and you can use that to, to do your sampling. And then, and then there's, there's an analog fine tuning voltage in there that you can tune. And I've run that with a 12 bit DAC. And so theoretically you've got a resolution of about 20 femtoseconds that you can tune this thing. Obviously jitters a lot bigger than that. And there's noise. And so you, you don't actually, you know, you don't get anywhere near that precision, but that's a resolution that you can tune it with. And so now you've got this thing that you can tune and you've got to figure out how you can, how you can measure it. How do we measure it and then adjust this tuning voltage to get the samples exactly where we want them. And it turns out it's, it's a delay line. And so one of the ways you can calibrate this is turn it into an oscillator. So you take the output of the delay line and feed it through an inverter and feed it back into the input. And depending on what the delay is, it oscillates at a different frequency. And so you can run this for, you know, a hundred milliseconds or so, um, and count how many times it oscillates in a hundred milliseconds. And then from that determine how long the delay is. And you can use this to calibrate and you can, you know, get into the easily into the hundreds of femtoseconds, um, of accuracy of calibrating the delay through this line.

**Ted Yapo:** And that's just a standard. So because it's a known, a known transmission line kind of thing, is that the idea?

**Ted Yapo:** Yeah, because the, the, the line cell is, I mean, it's just a trace on the, on the printed circuit board and because, um, you can, you can measure, uh, the frequency with the delay set to minimum. And then with the delay set to values above the minimum, you can just subtract off the delay from when it was at zero. Because you don't really care about the absolute delay. Yeah. You care about the relative delay. The absolute delay just moves the waveform on the screen of an oscilloscope left or right. Yeah. Right. That's just kind of, you know, that's just moving.

**Ted Yapo:** What's that called? Not an offset. That's, uh.

**Ted Yapo:** It's just an off.

**Ted Yapo:** Yeah. Um. That's like from the intercept type of thing when you're, when you're moving it back and forth on the screen, you know?

**Ted Yapo:** Right. Like if you change the trigger point, you get that. Right. You change the trigger. You just move the trigger point, I guess, is what you, what you do. Um, so you don't care about the absolute time necessarily. You care about the relative time from, from the trigger point.

**Ted Yapo:** So what are you going to use this for? I mean, just for other, other diode clock type things?

**Ted Yapo:** This is the kind of thing that you need to open up a space for other people to, to work on, you know, to work on fast things. Right. Yeah. So when I started this project, I had a 300 megahertz oscilloscope. It's actually one I bought with the winnings from, when I rounded the Hackaday prize.

**Ted Yapo:** Oh, nice.

**Ted Yapo:** So I had that 300. Paid it forward. When I bought it. Yeah. When I bought it was a 70 megahertz Regal and you know how they, they upgrade. Yeah. So it became a 300 megahertz. Um, and I realized within like a month of really seriously working on this project that I couldn't do it. Like somebody, whoever made the fastest oscilloscope at any point in time bootstrapped it. Right. Right. Right. They didn't have faster equipment. So I give them a, I mean, you got to give them a lot of credit for doing that, but I, I just wasn't in a position to do it. So in order to build, you know, uh, a really fast oscilloscope, I needed a faster one. So I, you know, I bought a used one gigahertz tech off eBay and that lasted about four months until I needed a faster one. And then I, you know, I, and then I bought the 20 gigahertz one. Right. And.

**Ted Yapo:** Am I going to be bleeping this section out too for your wife? Is that the other one? We probably should. I mean, she could probably just walk in the lab and see all the boxes showing up from eBay. You bought a what? It's a 30 year old scope though.

**Ted Yapo:** So, you know, so I got a cheap on, it's a 30 year old scope. Right, right, right. But, you know, now I'm looking at the 50 gigahertz sampling head for it. Like, oh, can I afford it? You know, just drop it in. Then I get 50 gigahertz. And the thing is, I couldn't have done a whole bunch of steps along the way unless I had something that went this fast. But now I have an eight gigahertz scope. And, you know, once it's in a state that people can reliably and repeatedly make these themselves, then a whole bunch of people can have eight gigahertz scopes, you know, for a hundred dollar bomb cost. And now what can they build with that?

**Ted Yapo:** Right, yep.

**Ted Yapo:** Right. So, you know, you've got to build the infrastructure because, you know, you can find one of those tech scopes maybe for $800 for the mainframe and maybe another 400 for that. So, you know, a thousand dollars, maybe you could have it, you know, have one. That's a lot of money.

**Ted Yapo:** It is, yeah. Right.

**Ted Yapo:** But, you know, if I can buy one like that and use it to come up with an eight gigahertz scope that people can get for a hundred bucks, there's a whole bunch of people who might do some interesting things and want to, you know, and be able to afford a hundred dollars of equipment to do it.

**Ted Yapo:** Yeah. Yeah. You just never know what's going to pop out of that, right?

**Ted Yapo:** Yeah, exactly. I mean, I look at, you know, some applications for it. So, you know, you can, right now I'm using it to measure transmission lines, to measure PC boards. So you can measure the impedance of traces, right? You can see if those calculators you find online are lying to you or not. In many cases they are. Oh yeah? Right. So you can, yeah, you can measure the impedance of traces. Are you close to 50 ohms? Are you not? You know, is the, is the problem with your connector or with the trace or the, the pads on your, on your footprint? Um, and you can measure down to a five millimeter accuracy with this. So if you have a, you know, trace on your PC board, that's five millimeters or longer, you can determine what the impedance is.

**Ted Yapo:** What does that, what does that measurement look like?

**Ted Yapo:** So there's this thing called time domain reflectometry. And so it's a, it's a big word. It's a very simple concept. Think about radar, right? So in the, you know, 19, the world war two radar systems, you sent out this blip of, of electromagnetic magnetic energy. It bounced off something. That's right. You counted how long it takes to return. And then it tells you the distance. Well, this is the same thing, but inside a wire or inside a transmission line. So you send out a signal in this case, just a step, right? Um, down a wire. And when that step encounters impedance discontinuity. So you have a 50 ohm cable and somebody spliced in a piece of 75 ohm because that's what they add around. Um, at that place where those cables are spliced because it's going from 50 to 75 ohms, there's a reflectance there, right? There's a reflectance coefficient of what is 75 minus 50 over 75 plus 50, 20% comes back. Right. And so if you analyze the waveform that comes back on the wire, you can say, oh, okay, there's a 20% reflection at this point in the wire. That means the impedance of that section of wire is 75 ohms. And so you can tell because of the time it came back exactly where that discontinuity is. And because of the amplitude of the discontinuity, whether it's 75 ohms or 60 ohms or 30 ohms or whatever, you can tell what the impedance is of that section of transmission line. Yep. And so you can use this to look at a trace on a PC board. So, you know, you send a pulse down and look at the return and you can see the cable and you can see the connector, whether it's, you know, the impedance are higher than lower, higher or lower than 50 ohms. You can see the trace on the PC board. You can see other components there. And so it's a way to measure these discontinuities on a transmission line. And these are the kind of things that, you know, are going to mess you up, right, when you're designing RF circuits or high speed circuits. You know, if you have reflections at these points, well, that means that, you know, first of all, you're going to have to deal with those reflections might come back. They might bounce around in there and cause problems, you know, later on. Or it may just prevent, you know, signals from getting where they need to go. So that you can, you know, I've got a TDR head for this. It's a little, it's probably another $20 that you kind of screw onto the input here. And that has a splitter in there. It takes care of sending the signal down the wire and returning it back to the sampling head. And, you know, you end up with a display that's calibrated. You know, the Y axis is calibrated in ohms and the X axis is calibrated in time. And you can say, you know, at 20 nanoseconds down the wire, it's, you know, it's 50 ohms and then it goes up to 70. And you go, oh, what's wrong with my PC board at that point? Right.

**Ted Yapo:** And this is all, this is relative as well, right? Because if you, if you assumed it was a 50 ohm to start with, but it was actually 60, wouldn't that change? You would, you wouldn't know the, you just know the magnitude change of the two things, right?

**Ted Yapo:** Yeah. And, and the way you calibrate is you put on a 50 ohm terminator. Right. Yep. Yep. And so it's all, it's all relative, but you can calibrate. Right. So you get a good precise 50 ohm terminator and you put that on and you tune it until that's 50. Yep. And then everything else is relative to that. Right. So, you know, if, if you bought the cheap eBay terminator, you may not reach that after. Yeah. Yeah.

**Ted Yapo:** I, uh, I just, I was lucky enough to have a VNA here and, uh, you know, they sent me a Calcut, which is nice too. And I was just like, wow, why do I need this? And then I was like, oh, I, I know why I need this.

**Ted Yapo:** Right. Yeah.

**Ted Yapo:** Uh, they're not cheap. Yeah. And speaking of VNAs, well, you, you weren't working with VNA, but you have a paper you wrote for Hackaday, the Hackaday journal, which I've never saw, but I, I saw the video that where Mike interviewed about it. And so you were doing stuff with not a VNA, but a spectrum analyzer and a tracking generator. What was, what was that kind of thing?

**Ted Yapo:** Yeah. So, uh, the, I saw the model, you have the, you had the Siglin 3.2 GHz. That's right.

**Ted Yapo:** The V, uh, the SVA 1032 that, uh, Shariar reviewed.

**Ted Yapo:** So, uh, Regal was the first one to come out with the, these really cheap spectrum analyzers. And in, it was late 2011 or early 2012, they came out with the DSA 815. And the first time I saw it online, like within 20 minutes, I ordered one. I saw, I saw the thing announced and it was like 1500 bucks.

**Ted Yapo:** Yeah. Yeah. I remember that came out. Yeah.

**Ted Yapo:** And you, you couldn't get, I mean, this was, you know, cheaper, like by half than the used, you know, HPs that could do the same thing. Yeah. Exactly. And it goes up to 1.5 GHz or whatever. And I said, oh, cause I had, I had struggled with, you know, with this for a long time doing RF. And really, I mean, once you've had one, you understand why you need one. Yeah.

**Ted Yapo:** Oh yeah. I mean, like, and that's the thing. I think that seeing, putting it into, this is like, kind of goes back to the idea of like teaching and like having that, that thing in front of you, like having, having a measurement there and being able to modify it. You might not get, I don't, I still don't get everything about it. However, I'm developing an intuitive sense. I'm doing that mental model based on the, the things that my eyeballs, you know, are passing to my brain. And like that is, it's just, there's very few things that can replace that in my mind.

**Ted Yapo:** Absolutely. And, and I found that, you know, I would write stuff down on paper or maybe do a simulation or whatever. And I might've got the math right, but my assumptions were wrong.

**Ted Yapo:** Yeah, exactly.

**Ted Yapo:** Like if everything were perfect, this is how it would be, but, oh yeah, this isn't, right. But I bought a thing off eBay.

**Ted Yapo:** I bought a, I bought a, you know, 65 ohm load on eBay by accident. That's right. Or not on accident. Yeah.

**Ted Yapo:** And there's nothing like actually seeing it work or not work.

**Ted Yapo:** Yeah.

**Ted Yapo:** So I, so I bought this thing and it turns out I got one of the very early units. They improved it over time, but the, the unit I had, and it came with a tracking generator. Now the unit you had did, did actually did vector measurements. Is that right?

**Ted Yapo:** That's right. Yeah.

**Ted Yapo:** I think that's relatively new in these, in these units.

**Ted Yapo:** Yeah, I think it is. And, and, you know, maybe you could break out what a tracking generator is versus the spectrum analyzer input.

**Ted Yapo:** Yeah. So the spectrum analyzer, um, it will just tell you what the, how much power there is at every frequency. Right. That's all it does. It sweeps over frequency and tells you how much power there is. Now what a tracking generator does is it generates a signal that's in sync with that sweep. So when the spectrum analyzer is analyzing a little band around a hundred megahertz, the tracking generator is outputting a sine wave at a hundred megahertz. So what you can do is you can connect a component in between those two. So let's say you want to test a filter. That's going to, um, you're getting some problem with, uh, FM radio stations are, are interfering with something else you're listening to because they're so strong and it's the antennas right down the road. I actually, I actually do have that. Sorry.

**Ted Yapo:** I need to cut in here. I have, uh, I don't know what, what it is in my H6N recorder, but if people listen to one of my videos on YouTube, you can hear a radio station coming through because I'm, I live right near the Sears tower and that thing just cranks RF. It just cranks that from stations. And so there's like, there's like, like, like salsa music playing in the background of my videos, not on purpose. Sorry. Anyways, go ahead. Sorry.

**Ted Yapo:** Um, yeah. So, so you can, so let's say you're building this, this FM, uh, uh, uh, notch filter, right? This, this, this bandstop filter, that's going to filter out all that stuff. So you don't have that in your videos. Um, so you can build a filter and then you go to test it and you connect the tracking generator to one side of the filter and you connect the spectrum analyzer input to the other. And it, as it sweeps through the 88 to what, 88 to 107 or 88 to 108, whatever.

**Ted Yapo:** Yes. As it sweeps through that, that band, you can see how much energy gets through the filter. So you can get a little plot of the response of the filter. So, you know, does it, does it kill all the signals and how much does it, are they down 50 decibels? Are they down 10 decibels? You know, whatever. Are there, you know, are there problems somewhere else? Does, does the signal that I want still get through? And so you can measure the response of the filter. Um, and this combination of tracking generator and spectrum analyzer is called a scalar network analyzer. Mm-hmm. And network analyzer is just, just a fancy word for something that measures something with, you know, at, with one or more ports, right? And you get one port and you get two port measurements. But, um, what this, the scalar part of a scalar network analyzer means is you're just measuring the amplitude. Right. So you're not measuring the phase of things that go through. So there's some ambiguity when you, when you measure, um, certain things about what the, what the sign say of, of certain things is. Right.

**Ted Yapo:** So like purely reactive components, you could have some problems. You don't get Smith charts, stuff like that, right?

**Ted Yapo:** That's exactly right. The other problem is that they're difficult to calibrate. Oh. So if you have a vector network, network analyzer, where you're measuring the input as vectors, right? You get the amplitude and phase. If there's a phase problem somewhere in, in your, um, in your loop, you can calibrate that out because you know what the amplitude and phase, when you put, you know, you take your expensive cal kit that they sent you. Yeah. Right. And you, and you put the through in there and you can measure the amplitude and phase with the through and you can do the, the short and the open and the load and all those things. And you can build this sophisticated model for what the test jig itself looks like.

**Ted Yapo:** Yeah. Right.

**Ted Yapo:** Without not even your component, just up to the measurement planes at the edge of the thing you want to test. You can build a sophisticated model for all the leakage paths and attenuations and phase shifts and all that stuff. And then when you go to apply, uh, that you put your device in there to test it, you can back all of this stuff out. So you can take what you actually measured and back out that all of the stuff that's just done to the test harness, you know, the wiring and the, and the connectors and all that stuff and understand exactly what the response of just your component is. Yeah. Not the cable that you use and the connectors and whatever.

**Ted Yapo:** As someone who buys a lot of stuff on eBay and Amazon now, uh, yeah, you better, better calibrate those cables out folks. Cause it's, uh, they're not, they're not good.

**Ted Yapo:** No, no, no, I, you know, I have a lot of them and I, I've, I have a large bin right now of crappy cables and a very small bin of good cables and I keep them separate. Yeah. That's good. Um, with a spectra, with a scalar network analyzer like that, it's very difficult to do this calibration. And that's what the paper was about was coming up a way to make two measurements of a device and use these two measurements to compensate for errors inside the device. And, and the, because I bought a very early model of the spectrum analyzer, it had this horrendous leakage path from the tracking generator to the spectrum analyzer. So without anything connected externally, or even, you know, if you put terminators on both ports, when you turn down the tracking generator, the, the trace went up by 20 dB. So you have this, you know, tremendous leakage inside the device somewhere. And I think they just didn't put enough shielding in there. And I think with later models, they beefed up the shielding on the board or, you know, between sections of the board. Um, and so the whole idea of the paper was, you know, I've got this thing, I'm not going to open it up cause it's the most expensive thing on my bench at the time it was. I'm not going to open it up and, you know, tax them, tax them foil in there to try to change the shielding. Cause I don't know what I'm doing. Um, but maybe I can do this mathematically and it turns out you can.

**Ted Yapo:** That's great.

**Ted Yapo:** So then did you, two measurements, slightly different.

**Ted Yapo:** Yeah. Well, the, the, the mathematically, did you have to push that firmware back into the device or is this all just done externally then? Cause you're just exporting data.

**Ted Yapo:** It's all done externally.

**Ted Yapo:** Yeah. Yeah. Export data. So, you know, it has a ethernet port on the back, like all, all of them do today, which is awesome. And you can just grab traces and then you have that data and dragging it to Python and do whatever you want.

**Ted Yapo:** I have a friend here in my workspace who just, uh, he's been pulling a bunch of equipment that has Python APIs for everything. And it's really, that's a really nice change, you know? So Will's doing this thing where it's like, instead of basically instead of doing lab view now, you can start to do Python scripting and, uh, it opens up a lot of avenues.

**Ted Yapo:** Yeah, absolutely. I mean, it used to be all GPIB, I guess. I mean, a lot of the older equipment I have is GPIB and I, I don't even know. It's some kind of weird parallel format, isn't it? I look at the head. It's like, it's like frames basically. It's like frames. So I, uh, yeah, I haven't played with that. It's much easier to just have ethernet.

**Ted Yapo:** Yeah. Yeah. Yeah. It's, it's a, it's a very welcome change, I think. Yeah. Yeah. Especially if you're building test benches and stuff like that.

**Ted Yapo:** Yeah, absolutely.

**Ted Yapo:** Have you, you haven't upgraded then? You've just kind of, you're really getting the, getting all the, all the juice out of it. You can, huh?

**Ted Yapo:** You know, I, uh, I lost an auction last night for a 22 gigahertz spectrum.

**Ted Yapo:** My, my, uh, my condolences, Ted.

**Ted Yapo:** Yeah. It hurts. It hurts. They're selling them cheap on eBay now and people are snapping them up. Yeah. So it was just a little, a little too rich for my blood, but yeah, I'm, I'm looking to upgrade. Yeah.

**Ted Yapo:** I keep looking at the, uh, you know, all the HP 8753s and all those, and those, man, I've mentioned on the show, but they don't, they don't go down. Those are flat. Yeah.

**Ted Yapo:** No. Yeah. But you know, they're built like tanks.

**Ted Yapo:** Yes. Oh yeah.

**Ted Yapo:** So the, the, um, the 1180, 11801, the Tektronix 20 gigahertz scope I have was built in 1989. It has 75,000 hours on it. There's a counter in there. You can look it up. I'm like 75,000 hours. And a lot of these things I think were on manufacturing lines. Yeah. So they would test, you know, they would just, I mean, they just be on constantly testing things. It still works fine. There's no problem. I mean, I haven't found any problem that passes all the diagnostics, passes all the calibration tests. It's, it's fine. I don't know how long it's going to last. One of the, one of the knobs is kind of twitchy. I have to keep tightening it up, but that's it.

**Ted Yapo:** Yeah. Yeah. Yeah. I guess, how do you, how do you know that the equipment's working well enough? I mean, is it, do you have some kind of like local calibration that you're doing? Is it just based on the, um, on the, the Cal kits you have or what?

**Ted Yapo:** Yeah. So, so it does, it does have internal calibration that, that, you know, keeps it, I mean, then you wonder, well, well, what if that's off? Yeah. Right. Right. Right.

**Ted Yapo:** That's why you send it out every year or two to get a Cal sticker, but that's pretty expensive to do.

**Ted Yapo:** Yeah. And I can't, I can't afford that, but you know, it's, it's about making a bunch of different measurements and making sure that they all make sense together. So you make measurements with that, you measure some other things that you have and you make sure that everything's consistent.

**Speaker ?:** Yeah.

**Ted Yapo:** And so, you know, I don't really trust any of it. I don't trust anything.

**Ted Yapo:** That's healthy. Yeah. Right. And, and the reality is I don't trust anything that I'm doing either. So you measure it two or three different ways and see if you get about the right answer. Right. And if not, why? Yeah. And, but you probably need to do that with, even if your stuff's all calibrated. Right. I think that's right. Because was it the test set up? Was it the cheap eBay cable? Right.

**Ted Yapo:** Yeah. Right. Yeah. There's nothing more frustrating than, you know, 20 hours into debugging and you're chasing a ghost that's actually your cable or, you know, it's, you know, it's not something small like, oh, you didn't plug it in, but it's more like you had something in line that you didn't think you did or you put the wrong component on board somehow and you're just like, oh my God. Yeah. Yeah. Well, this is great. I mean, this is a sample, just a sampling we've talked about here. Obviously there's more on your Hackaday IO page, but you're going to be at Supercon as well. So that's coming up in a couple weeks. Is it giving a talk?

**Ted Yapo:** I'm giving a talk about the, about the oscilloscope, about the sampling oscilloscope.

**Ted Yapo:** Oh, great. Okay. So we've got a little, little preview here.

**Ted Yapo:** Yeah. So we've got a little, little preview. There'll be a lot more details and some, and some nice pictures of, of what's going on. Um, you know, it's, it's kind of tough just to do it just with sound, uh, to paint that picture of how the thing works. So I think, I think that, I think the visuals will really, uh, uh, will really make it pop.

**Ted Yapo:** Well, I'm looking forward to hanging out there with you. And I think that that's, you know, it's a lot of fun to, to be there with other, other hardware folks. Hopefully, uh, hopefully we had a lot of, a lot of good talks this year and good, good crowd. Yeah.

**Ted Yapo:** It's an amazing time. I, my first time was last year and I was just, I was blown away by the thing.

**Ted Yapo:** Yeah. I don't, yeah. I don't know if we met last year. I think we met briefly last year. We did meet briefly. Yeah. Because I think you were on my list of people to interview and then finally got around to asking you. So I'm glad you're on the show.

**Ted Yapo:** Yeah. I'm glad to be here.

**Ted Yapo:** Yeah. Cool. Well, uh, we'll talk to you soon and looking forward to hanging out and seeing more about your really, really fast distillate scope.

**Ted Yapo:** All right. I'll see you then.

**Speaker ?:** Thanks. Thank you.

**Ted Yapo:** Once again, we'd like to thank our sponsor for this episode, Roden Schwartz, a leading manufacturer of value instruments designed to help you maximize your bench's performance for everyday applications. They just announced an industry first complete solutions with all the upgrades upfront for one price. Now through December 31st, 2019, save up to $10,000 on Roden Schwartz solution packages. They come with fully loaded test and measurement instruments right from the start. When you invest in Roden Schwartz products, you get the highest quality engineering, plus all the bandwidth, channels, inputs, memory interfaces, and signal generation you'll ever need. Learn more about Roden Schwartz value instruments and this limited time promotion at askanengineer.us. That's askanengineer.us. Roden Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf
