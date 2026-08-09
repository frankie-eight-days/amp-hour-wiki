---
episode: 531
title: Footprints and Symbols with Natasha Baker
url: https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/
---

**Natasha Baker:** This is The Amp Hour Podcast. Release February 21st, 2021. Episode 531. Footprints and Symbols with Natasha Baker. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Natasha Baker:** And I'm Natasha Baker of Snap EDA.

**Natasha Baker:** Hey, Natasha. How are you?

**Natasha Baker:** I'm doing great, Chris. How are you doing?

**Natasha Baker:** I'm great. I'm great. I'm excited to talk about parts and footprints and just all the nitty-gritty of getting stuff into a design that it seems like Snap EDA is really good at these days.

**Natasha Baker:** Awesome. Me too.

**Natasha Baker:** So let's get a little story about, I mean, so what is your background and how did you find your way to starting Snap EDA?

**Natasha Baker:** So I'm an electrical engineer and I studied at the University of Toronto. And after I graduated, I started working at National Instruments. And they actually create an electronic design tool. So I was actually doing my internship there before I graduated. But then I also joined them in the research and development department. So, you know, the very first thing I did actually while I was an intern was implement IP compliance into their footprint database. So I read through all of the IPC specs and just kind of learned all the nitty-gritties, all that exciting stuff.

**Natasha Baker:** I mean, what you were dreaming of in engineering school, I'm sure, right? Absolutely.

**Natasha Baker:** You know, I thought it was fascinating. I mean, just the level of detail that they put into this whole process. So yeah.

**Natasha Baker:** What is in an IPC spec for people who haven't read it before, who haven't sat down with a, you know, a coffee or, I don't know, amphetamines to stay awake? What is in there? And like, and what do you then draw out of it?

**Natasha Baker:** It's basically a standardization body, the IPC. And they have standards for, you know, all kinds of stuff. The ones that I was going through and then the ones that we're particularly interested in with parts libraries are, you know, the IPC 7351. That's for surface mount components and manufacturing. And basically it lays out kind of all of the best practices for soldering and for making sure that you have good manufacturing when you go to manufacture your boards. So they define the land patterns, all the land pattern standards. And so they have gone into, you know, a lot of depth in terms of the pad sizings and all of the different details that, you know, that you need to follow for good and reliable manufacturing.

**Natasha Baker:** Yeah, that's great. And that's, so you're saying that's actually at the, going into KiCad, I'm just going to use KiCad the whole time. So we'll just assume that here. There's no surprise there, but going into KiCad, making a footprint, it's like best. So like I shouldn't oversize, I shouldn't undersize a pad. And because of X, Y, and Z that might happen as a result of not following it. Is that kind of the thought there?

**Natasha Baker:** Yeah. Well, they actually specify, they actually specify different density levels. So depending on the type of design that you're doing, right? If you're doing a, you know, a mobile device, right? Obviously things need to be very dense and you're probably going to be sizing the pad smaller, right? Than if you're building electronics for some, you know, rugged industrial high power application, right? So they specify most nominal and least, you know, most being obviously on the larger side and then least being obviously on the denser side. And yeah, and they specify basically different calculations and, you know, different sizing depending on the type of application that you're doing.

**Natasha Baker:** So does that change year to year? I mean, obviously devices are getting more dense over time. Does that least specification then change from year to year, like the 2015 spec versus a 2021 spec?

**Natasha Baker:** You know, that's a really good question. I'm actually not sure. I know that they're coming out with the IPC 7351C right now. That's a good question. I actually have to look into that myself or ask our engineers.

**Natasha Baker:** Yeah. Yeah. That's generally curious. I don't expect the latest and greatest on IPC. It's really interesting that, I mean, like this body that does this too. I mean, it's obviously it's like a consortium or something like that, but who's on the other end of that? That just seems like, boy, that's got to be a dry, a dry meeting, meeting group, you know?

**Natasha Baker:** There's actually brilliant engineers that are part of it. I know that one of our engineers, she participates in some of the meetings and what's great about it is that anyone in the industry can participate. So they, so there's definitely members where, you know, you have to have your corporate sponsorship to be a part of the committee. But the great thing about it is that as far as I, as far as I know, like anyone can get involved and participate and the people that are working on it are just so, it's actually incredible the depth of knowledge that they have. Yeah. The depth of knowledge that they have around components and around manufacturing is absolutely like incredible. Like actually one person that comes to mind for me, I don't know if you want me to mention him, but like he works at like mentor graphics, for example, and he has been working a lot on like the standardization of, you know, component naming and things like that. And, you know, just a brilliant engineer who the amount of depth of knowledge he has about components is it's like mind blowing. It's absolutely incredible.

**Natasha Baker:** Yeah. When you think about like the aggregated number of years, just how big the industry is times how many engineers are involved and just, yeah. Then the length of time that the industry has been around, there's many, many millennia of person years, I would imagine that are just aggregated.

**Natasha Baker:** Absolutely. And the people on this, you know, on this committee, like they've been working on this for decades. So they are like the amount of knowledge that they have. It's just, it's amazing. And I've, I've been to some of these meetings. I actually spoke at one of the meetings and I, you know, it's just the comments that you hear afterwards about the best practices around manufacturing. And just like, like, you know, I'm just thinking of one idea off the top of my head where there was this, this woman who came up to me afterwards and she's been, you know, in the industry decades. Right. So of course she has this knowledge, but we were talking about QFP components that have like a thermal pad in the middle.

**Natasha Baker:** Okay. Yep.

**Natasha Baker:** And so the IPC recommends breaking that into chunks, right. So that you don't get a floating component right on top of your board. And so, but what she was telling us was that actually what they do is they actually put like an X of solder mask and solder paste in the middle of the component.

**Natasha Baker:** That's cool.

**Natasha Baker:** Yeah. But it's like, these are like the types of insights that you only get from like having done it, you know, they're not in any guidebook.

**Natasha Baker:** Right. It's almost like formalizing tribal knowledge at that point, right? It's probably someone who tried that cutting out a stencil specifically to solve some problem locally. And then they're like, oh, well, this could be a more broadly available best practice.

**Natasha Baker:** Exactly. Yeah. And there's, there's just such a wealth of knowledge there. I would definitely recommend like to, to check it out and, you know, see how you can get involved because the amount of knowledge that's there is, is really incredible.

**Natasha Baker:** Yeah. That's cool. That's cool. Okay. So, well, you, so you were at NI, you were doing this, but you must have turned around and then said, you must have looked at the industry and been disappointed. I mean, obviously you started Snap EDA. So, so what was, what was a step from NI and reading IPC docs up towards actually starting this, this company?

**Natasha Baker:** Yeah. So, so actually I was working in R and D for a couple of years and, you know, loved it, but I always had this like sense of like, I want to see what, you know, marketing is like, I want to see what like the business side is like. And, and so I moved over to market the marketing side, but while I was there, I was still, it was a technical marketing role. So I was still designing circuit boards and things like that for trade shows. And there was this, you know, one design that I was working on and it was basically a circuit board that we were going to put into a Wii steering wheel to make a cool demo to trade show where you could like, you know, drive, you know, the Wii steering wheel and control this like Nintendo emulator on the computer. Yeah. And so it was a really simple design and it was a simple Texas instruments reference design. And as I started designing this simple accelerometer board from a very simple reference design, what I realized was that all of these super, you know, basic components that I needed weren't in the library of my PCB design tool, you know, so super simple, common voltage regulators, like they just weren't there. And I had to design them from scratch. So this board that should have taken me maybe a few hours, right. To, to, to create ended up taking me like days of time because I had to create all of the symbols and footprints from scratch.

**Natasha Baker:** Right.

**Natasha Baker:** You know, I actually remember I was at my grandparents' house and I just remember like I was there and I wanted to spend time with them, but like, I was so focused on getting this board done. And like, I was making all the symbols and footprints. And it was kind of like in that moment where I was just like, you know, this isn't like, why, why can't electrical engineers have the same, you know, types of libraries and resources accessible that are available to consumers, to software engineers? Like why can't electrical engineers have all of this ready to use content when they're designing? And it's not just about symbols and footprints, right? I mean, symbols and footprints are just the most obvious thing, but a lot of people are simulating. They can't find simulation models. And when they find them, they don't know what are the limitations of that model, right? Because that's the other, that's the other challenge that I was seeing is I would go to simulate and well, you know, at what frequency is the spice model actually valid? And like, you know, as an engineer, you know, as you're using these models, you don't know that. Right. And so what would happen is a lot of the time engineers would simulate something at a frequency that just, it was not modeled at. And then they'd be like, oh, something's wrong with my design or, oh, something's wrong with this tool. But it's like, no, they just don't have insight into the limitations of these macro models when it comes to spice. So the whole idea behind Snappy DA is really not just about access. I mean, access is great. And I think that's step one is, you know, providing a centralized place where engineers can, can get this content. But I think the biggest question is like, well, you know, how do you know you can trust it once you find it?

**Natasha Baker:** And that's, yeah, that's a great one.

**Natasha Baker:** That's the place we really focus.

**Natasha Baker:** I think to take a quick step back, I mean, the inclination you had about that, you know, why aren't there libraries out there? Why, why do I have to keep doing the same thing that everybody else has done? That sounds very familiar. I've said that. I know other people have said that. We've just been grumbling about it for, I mean, grumbled, grumbled about it on the amp hour for many years as well. I don't know as many people that went out and tried to fix it though. So that's the piece that I'm interested in. Like you actually like, you're like, oh yeah, no, I could fix this. So that, that part's pretty cool. So what was then the jump into, into doing that to take that first step?

**Natasha Baker:** Yes, Chris, you bring up a very good point. You have to have a little, a little bit of craziness in you to go after this.

**Natasha Baker:** I'm going to say gumption, Natasha. I think that's gumption.

**Natasha Baker:** You know, have you read Zen and the Art of Motorcycle Maintenance?

**Natasha Baker:** That's right. Yeah. I love that book. Yeah.

**Natasha Baker:** I love that book too. So yeah, they talk about gumption. You know, I read that actually in university, actually at the same time or not in, yeah, in university at the same time I was doing my internship. And at the same time that I was actually, I was doing some contract work for analog devices as well, helping them with libraries. Right. And so, and I was reading Zen and the Art of Motorcycle Maintenance. I loved that concept of gumption.

**Natasha Baker:** Yeah.

**Natasha Baker:** And I think that comes back to the trust point, right? Which is if you can have, if you look at anything with a sense of craftsmanship, right? Then like everything becomes so rewarding. And I'm so glad you brought that up because I think sometimes people think of libraries as an afterthought. They think of them as like, oh, they're just the libraries.

**Natasha Baker:** Right. Right. Well, and it should be right, but it's, you know, and it should be something I can trust and it should be this thing that a CAD tool has or whatever, but it's just, there's a ton of work there. I mean, that's, that's what I've learned. And, and I, I obviously you have as well. I mean, that, that sounds like that's your exact experience.

**Natasha Baker:** Yeah. Each library, like, I think that people think, oh, it's just a library, but what the, and oh, an intern can do that, you know? But what they don't realize is that for some of the, like for a lot of these models, especially the electromechanical models, first of all, you need to be really skilled to read those data sheets sometimes. Like for, like these are complex mechanical models and even understanding all the nuances of your tool and to create proper slotted holes, understanding like the plating, you know, being able to interpret a plated or non-plated hole. Like there's just so many details that are so not only easy to overlook, but that take time to understand and to take time and take a lot of expertise. And, you know, at Snappy Day, we, we don't think of it as just, this is a library. We think of like each library we create as like something that we do put, you know, that gumption into and that craftsmanship. But anyway, I digress a little bit here.

**Natasha Baker:** That's great. That's great.

**Natasha Baker:** Great question, which is about the.

**Natasha Baker:** Just like the genesis of it. Yeah. The genesis. I mean, so actually taking that leap then is, is a big one. I mean, and I'm going to, I'm going to be completely honest. I was a bit skeptical. I first learned about Snappy Day, not right at the beginning, but relatively early I saw it and I was just like, oh, well, would I use something like that? I don't know if I would. But over time, I guess one thing that inspired me to reach out to you is like, I was going back to Snap, Snappy Day and requesting models multiple times. And I was like, oh, I know Natasha. I should have her on the show. Like I, you and I have talked when I was out in San Francisco a bunch. And like, I think it's a great product. I honestly hadn't found myself using it until recently. And now that I have, I mean, obviously anyone has that light bulb moment. It's just like part of my workflow now. And that's really cool. I think that's really a great thing.

**Natasha Baker:** Wow. That's awesome to hear, Chris. Cause I mean, that, that comes like, that means a lot coming from you just being that I know you, I know, like, I know how discerning you are with the tools that you use.

**Natasha Baker:** Oh, I don't know about that.

**Natasha Baker:** I've listened to your show and how, you know, so that, that does mean a lot. And, you know, I think that, so first of all, you're absolutely right. When I was getting started, getting started was so hard because everyone I would talk to would say, you know, this sounds really cool, but I wouldn't use it because my company has a librarian or making libraries is part of my job, or I would never trust a third party for that. Like, those are the things I heard over and over again. And I can't tell you like how demoralizing it was like in the early days, because I felt like the world needs this, the world needs this product, but it like just kind of facing that every day, day in and day out. And then on top of that, you know, going out into the local startup community was very challenging as well because no one knew what I was talking about. They would be like, well, what are footprints?

**Natasha Baker:** Right, right. What are symbols? Well, let's, let's start with PCBs. And you just like plop the IPC spec down in the desk. We're like, read this and get back to me.

**Natasha Baker:** Yeah, totally, totally. It was, so it was definitely really challenging, but I believed in it. So what I did is I just said to myself, you know what, like, I'm just going to build this. Like maybe the world's not ready for it yet, but I'm going to build it. And so what I did is I quit my job, even though I loved my job and I thought it was great, but I was like, if I don't do this now, I'm never going to do it. So I quit my job. I didn't have a ton of savings, but I had enough to just kind of start coding. And I didn't, I actually didn't know how to do any web coding. Like obviously I studied engineering. So, you know, you do the basic programming classes.

**Natasha Baker:** Yeah. And you know how to go figure things out that that parts, you know, you can, you can figure it out over enough time, but do you want to spend that time and you have the runway to do that sort of thing?

**Natasha Baker:** Exactly. But like, I just, I just spent that time. I just spent that time. I mean, I had the luxury of time then I didn't have funding. I didn't have a team. I didn't have like a job anymore.

**Natasha Baker:** Yeah.

**Natasha Baker:** So I had kind of the luxury of time to just learn how to code. And I figured it was a good investment. Right. I was very young, young at the time relative relative to now, obviously. And so I just started coding and actually funny enough, the, the same code base that was like the code base that I started learning on, which was this Django like tutorial for a, like a bookstore, a bookstore app, like book management. Sure. That's actually like that same Django application is like what our current code base is built on today.

**Natasha Baker:** Oh, cool. Yeah.

**Natasha Baker:** So it's like still the same, our database.

**Natasha Baker:** It's got stand power. Yeah. That's great. And that's great. Yeah. And it's interesting too, like the, the book, I mean, classification and that sort of thing. It does actually make sense as a, as a starter template too, because you're, you're, I think there are very hard categories that you're going to things that different parts are going to slot into. So it does seem to kind of fit that model pretty well. Is there, have you formulated a, a, a snap EDA Dewey decimal system or similar? The Django based system is like, is like a bookstore that actually seems to make sense. Like having really hard categories for parts as well. It seems to fit, fit that same model pretty well.

**Natasha Baker:** Totally. Yeah. And like the tutorial, it really does. It's kind of funny because like there's certain database fields even today that are based on that original, you know, that original tutorial. So for example, for component images, we use cover art, book cover art. Oh, nice. Yeah. Yeah. That's great. And we just haven't changed it, but I mean, it's, it's changed so much over the years and, and thank, thankfully much better and, uh, software engineers than, than myself have kind of continued evolving it. But anyway, yeah, that was kind of the, the Genesis. I just, you know, I just sat down and started coding and started talking to people kind of, you know, different engineers who were willing to talk to me, give me their feedback. And, and again, a lot of them were saying, yeah, I would love to use it. It sounds cool, but I wouldn't use it. You know, they were very honest with me.

**Natasha Baker:** Right. Yeah. Yeah. I would think one thing that's really tough about it too, is just the network effect type of thing where you, I mean, so now on the front page of Snap EDA, you talk about having, you know, over a million parts or sorry, a million engineers rather, and many, many parts that are available are right out of the gate. Like I'd imagine at the beginning, it's tough because you just, you're starting from zero and you have to actually go and build these models that are used over and over again. Each time you get a new one, you benefit from it because it grows the, the centralized database, but it's, it starts at zero.

**Natasha Baker:** Yeah, absolutely. It, you know, yeah. Building a library with millions of components was definitely like, you know, looking back on it, knowing what I know now, I think I had the enthusiasm on my side, but you know, it took us a long time and for a long time, we, you know, we just didn't have a lot of components. So what we did is we started, well, I can go into that after, but we started offering things like free requests right from the beginning. And, and that was kind of like a way to bootstrap our database. We allowed engineers to upload components. We had user generated content, which we didn't want to have, but it was just kind of the easiest way to get started. That was like the only way to get started is we allowed people to upload their models to, to our community.

**Natasha Baker:** Were they actually doing it? Was it IPC compliant?

**Natasha Baker:** Definitely not IPC compliant. And, and, you know, we had to come up with an algorithm to, you know, in terms of how to handle that, right. To make sure that we always de-ranked user generated content. So today you don't find a lot of that just because we always prioritize supplier or snappy DA generated content. And we give kind of a big warning if something's user generated, but you know, the reality is, is, you know, with there being millions and millions of parts out there, you know, actually I think IHS says there's a billion parts, you know, that have a million, a billion.

**Natasha Baker:** IHS, those, those folks, I don't know. That's, so this is a clearing house of data for components. I used to do a little bit with IHS stuff, but like, yeah, they, a billion. I mean, I, I just feel like there's, that's, that's such a big number. I don't know.

**Speaker ?:** Yeah. Yeah.

**Natasha Baker:** I mean, it is, but a lot, you know, a lot of these, uh, connector companies, especially they build so many of their components on the fly, right. They're all made to order and there's so many different permutations of, you know, different combinations and things like that. So, I mean, it may not be like, I don't think it's, I don't think it's an impossible number, like knowing what I know about some of these connector companies.

**Natasha Baker:** Uh-huh. Specifically connectors you're saying, huh? Yeah.

**Natasha Baker:** Specifically connectors. I, there's just so many like, you know, potential permutations of, of connectors. Yeah.

**Natasha Baker:** Yeah. Yeah. Yeah. The part, the part numbers are horrendous sometimes. I feel like connectors and crystal companies, I feel like crystal companies have the worst part numbering scheme I've ever, I've ever had to deal with. I don't know. Like it's again, maybe because it's made to order type of stuff, but it's just like, and they always put spaces in there, which are just like, what are you guys doing? It just seems like such a, so, so out of the norm from the other, the other types of components that I'm normally using.

**Natasha Baker:** Yeah. Well, you know, with some of these companies that are doing all the acquisitions, right. You know, well, all of these semiconductor companies, all these component manufacturers acquiring so many different departments. I mean, there's no standardization for, for so many of these companies, right. Once they've acquired all these different groups, they all use these different naming conventions. Don't even get me started on naming conventions, you know, I've gone forever.

**Natasha Baker:** Well, let's get to something that's not, uh, not controversial at all. Let's talk about being a startup. Uh, it's not like there's a, there's a, you know, HBO documentary about it. So you joined, uh, Y Combinator and that's where Snap EDA kind of got, got its official start. What, what was that like? I think we've had a couple other companies from, from Y Combinator on here, but what was that like for you and Snap EDA?

**Natasha Baker:** You know, Y Combinator was honestly the best thing that could have happened to Snap EDA. I think that, you know, cause between the time that I started the company and the time that we got into Y Combinator, I started with, you know, just kind of building this thing, you know, from first principles, we didn't have any funding. And, uh, and because we didn't have any funding, I was working on other projects, right? I, well, I had to, I had to have an income. So I was writing for Reuters. I was writing for Forbes. I was, you know, writing for, you know, all kinds of clients and even doing coding for different companies. Yep. Yep. And what Y Combinator did is, you know, I always knew I wanted to do Snap EDA full time, right? It wasn't a question in my mind. It was just a matter of resources. Yeah. And what was so great about Y Combinator is, you know, obviously first and foremost, it's, you know, having a little bit of funding, but I think the, you know, and that was what was most important at the time was that I could actually focus on this full time. But, you know, ultimately the biggest benefit is just the people that you are able to surround yourself with that, you know, go through Y Combinator. They're, they're all people that are like-minded. They're all very driven to seeing their company succeed. They have, you know, ideas that they want to build. They're determined. I think that that is ultimately the best thing. And I think for, I think for me as like a founder, it was kind of like the inflection point between, you know, just being an engineer, coding this on my own and just trying to get it off the ground to, you know, thinking more about, okay, like, how do I make this bigger than just building the product and, you know, thinking about how do we, how do we grow it faster? Yeah, I would absolutely, I would highly recommend Y Combinator to anyone who is considering it and, you know, any, any companies that are doing, you know, yeah, I would definitely recommend it. I don't know, Chris, I'm curious, like, what have you heard from other people who've been on your, on your show?

**Natasha Baker:** Well, so we, we had Luke Eisman, who was the hardware person at Y Combinator, I believe, right about the time you were, you were joining. Is that right?

**Natasha Baker:** Yes. Yes. He was there right. Yeah. He was there when I was there.

**Natasha Baker:** So Luke's been on the show. It's interesting hearing, you know, their take on hardware. I think Upverter was also in through, went through Y Combinator. So I think those are the two that we have had on the show. My take on it is I'm curious specifically around the hardware aspect of just like how, how they handled it because it, it does, you know, like seeing the companies that came out of Y Combinator, it's very software-y in terms of like the, even the end product type of stuff. Like they're very traditional consumer type things. Whereas it seems like you're more, you know, B2B and serving engineers. So I think that's, that's, that's curious to me. And I would be curious to hear about how they, how they treat a thing. Obviously the, the website of things, obviously it is. Snap EDA is a great website and there's web technologies in the backend. So that all makes sense.

**Natasha Baker:** And Octopart, Octopart went through Y Combinator as well.

**Natasha Baker:** Oh, Octopart as well. That's right. Yeah. Right. And so that's probably one of the closest ones because of the, the component tie-in and stuff like that. Well, I mean, what, what was the take there? I mean, was it, was it, has, has there been similar hardware stuff since or hardware adjacent type stuff since?

**Natasha Baker:** First of all, what I would say is that, you know, Y Combinator definitely has that reputation being where they started from of being more focused on consumer and webby kind of stuff. But the reality is, is that the types of companies that they've been funding in the last few years, like they funded like some really, really interesting hardware companies. I'm talking about rocket startups, satellite companies, like airplane, like there's the company that's building the supersonic airplanes. Like I think that people don't realize, you know, and I'd say, especially like the past three to five years, there's actually been, if anything, from what, what I can see is that I do see, I mean, and I guess I, I'm also looking for those types of companies, right? I tend to notice those companies.

**Natasha Baker:** Sure. Yeah. Right. You want to, you want to talk to them. You want to talk to their engineers. I'm sure. Right. Yeah.

**Natasha Baker:** Yeah. I would definitely say like, there's a lot of really interesting companies in that area. So if anything, I think that now there's kind of the, the criticism, not criticism necessarily, but criticism of like people in VC in general, kind of mentioning that, oh, like there are people aren't funding enough consumer stuff, right? Like with the whole clubhouse thing, they're talking about how that's like reviving investment in like the consumer space and a consumer app. So if anything, I think there's like been a shift away from investing in a lot of like consumer and just kind of like, yes, general SaaS for sure has always been popular, but yeah, I think more, more and more hard tech. Like I think that people are definitely interested in more hard tech for sure.

**Natasha Baker:** Cool. Okay. Yeah. And I mean, I can imagine from a trying to find funding and having the community, like you mentioned, you know, just dealing with a lot of the same issues, dealing with people in, you know, trying to put modern startup methodologies into more traditional industries, that has to be a really helpful thing in terms of how to like break through to different, different groups. You know, I assume that you're pretty regularly talking to grumpy old engineers or grumpy young engineers, to be honest. I mean, I'm, I'm probably the younger persuasion and pretty grumpy. So, uh, yeah.

**Natasha Baker:** Yeah. Yeah. And actually that's a great point. Cause that's what I was also going to mention is that, you know, you don't go to Y Combinator for them to teach you about hardware. Right. Like if you're going to Y Combinator for them to teach you about hardware, you're doing it wrong. Like, I mean, that's not, that should not be the expectation at all. And, and of course there's obviously some aspects of like scaling a hardware startup that they can definitely help you with. Like the person that's in charge of the hardware side now, I believe is Eric from Pebble.

**Natasha Baker:** Oh, uh, Nikofsky or however you say his last name. Yeah.

**Natasha Baker:** Yeah. I wasn't going to try to mispronounce his, uh, his last name, but yes, he's in charge of hardware now. And like, you know, he has so much experience with scaling up hard, a hardware company. Right. And so I think, you know, if you're looking for that, I think that, you know, Y Combinator is a great fit. And also for all of the other benefits around scaling your company and business models and things like that. But I think if you're going to Y Combinator with the expectation of helping you with the actual hardware, like I think they can connect you with people. I think you can meet other people, but like, you know, I think, you know, you have to recognize like, what is the value there? And I think the value there is really around, they're going to help you with the best practices of like startup stuff. Right. Like understanding the startup ecosystem, how to, you know, build a company in a way that maximizes the, you know, the understanding of the customer pain points.

**Natasha Baker:** Yeah.

**Natasha Baker:** So it's just kind of a different, you know, you just have to go into, you know, go into it with the understanding that you're not going for necessarily hardware expertise.

**Natasha Baker:** Yeah. Yeah. And it doesn't sound like you were looking for that. You were looking more for that methodology and that, the website. I mean, it is a web service company that's serving a particular set of grumpy engineers and that's, it's just hard. It's hardware adjacent, but it's not hardware itself. So that helps a lot.

**Natasha Baker:** Yeah, totally.

**Natasha Baker:** Well, I am a hardware grumpy engineer. What would you, what would you normally ask when you were, you know, so you're starting to do this. I assume you're doing interviews and, you know, just talking to engineers. What were the kind of things that you got into and what were some of the insights you learned when you were talking to engineers about their, their heart habits?

**Natasha Baker:** Yeah. We, you know, we talk to engineers all the time these days still, but, you know, I think the biggest thing was just, I think the biggest thing was trust, right? Like, I think it was that engineers recognized that when they use third-party libraries, they might spend just as much time verifying the component as they spend creating it.

**Natasha Baker:** Yep.

**Natasha Baker:** I think that was definitely like a, you know, obviously a, an interesting point, right? Which is that it's not just enough to provide components.

**Natasha Baker:** Right. Yeah. Yeah. You know, it's just, you could just have a, like a GitHub repo that has like, you know, a bunch of, you know, just like, oh, here's some zip files. Good luck.

**Natasha Baker:** Exactly. Yeah. No, or just exactly. But like, that's the thing is that that's something that I think, unless you're from our industry, unless you're an engineer, it's a very like nuanced point because they don't recognize how important that is, how important that sense of trust is.

**Natasha Baker:** Yeah. I always said like, it's, it's hard for me to, you know, when I was working at a big company, it was hard. It would have been hard for me to say, Hey, I downloaded this thing from the internet. And by the way, our prototype is late because I found this footprint somewhere and I didn't check it versus even, even if it's still wrong, it's like, I can at least take the responsibility and say, Hey, I, Chris mess this up. Yes. I'm responsible. Yes. I will fix it. And it wasn't like a, it wasn't a laziness on my part or not checking it or whatever. It was, I just made a mistake and, you know, mistakes happen. And so I think the, in my mind, the, the mental switch has to be like, it has to be so reliable and so, uh, such a, an obvious choice that like, I would, you know, I'm still going to check it, but, but I start from there. Right. That part becomes part of my workflow.

**Natasha Baker:** Mm-hmm. Yeah, absolutely. So that was, that was definitely one of the points and we spent a lot of time on that, you know, cause we're not going to like, you know, you can go to GitHub, you can upload everything on GitHub, right? All your libraries and things like that. And you can find them on GitHub and there's lots of places on the web where you can find content and crowdsource it. Right. But I think what's unique about the electronics industry is that there are all these nuanced aspects that engineers need to understand about the component. We talked about IPC have different, having different density levels. So which density level does this component follow? Does it follow the data sheet recommendations? Does it follow, you know, IPC recommendations? Uh, so I think that is the first point that we learned. I think another point is that there are so many preferences with libraries. It is absolutely nuts. There's also not full, like, yes, we talked about how the IPC has standards around manufacturability, but they don't define standards for everything. They don't define standards for things like the pin one indicator or the line widths of your silk screen and things like that. Right. So, you know, we have like, you know, some engineers who have specific desires for how big the pin one indicator size is, whereas other people don't care. So that's the other thing we learned is that what we're doing is very preference based. Another example is in our annual survey this year, we asked engineers, how do you like your symbols built? Do you like them, you know, in a logical flow with kind of like, you know, the inputs on the left, the outputs on the right, power on the top and bottom? Um, or do you kind of like it, you know, kind of like the data sheet application application circuit? You know, they usually have a, an example, you know, schematic symbol there.

**Natasha Baker:** Yeah. Like a best fit to, so that the inductor has a short lead between, you know, switch, switching pin and feedback pin or something like that.

**Natasha Baker:** Exactly. Yeah. And so we asked them that, right. And that's another example where like, it was like completely split down the middle and which actually really surprised me. Yeah. It's like, oh, great. What do we do?

**Natasha Baker:** So surveys are frustrating that way where it's like, yeah, it's like, yeah, it's like, like, oh yeah, people, people like things. That's what we've learned.

**Natasha Baker:** And which is great. And so what we've realized is that like, what we need to do is we need to be flexible, right? So we've architected our system to enable that flexibility in preferences. And we've started allowing people to customize their symbols more. So one example is in KeyCAD, correct me if I'm wrong, because you're the KeyCAD expert here. Just say you have like, I don't know, a no connect pin, right? And just say they're like, there's like four of them. Or maybe like a better example is probably like multiple ground pins.

**Natasha Baker:** Sure. Yeah.

**Natasha Baker:** So in KeyCAD, you can't have a pin named the same thing.

**Natasha Baker:** You can have the same name, but it has to have a unique number. So like if it's pins like 2, 8, 7, or 2, 8, 15, and 16, you have to have, you can, you have to have individual pins for each, but you can actually stack them on top of one another and it'll connect as though it's one. I find that very, very confusing personally though, if that's, if that's where we're going.

**Natasha Baker:** Yeah. So that's, and that's the difference. So there's some people that like them stacked and overlapped when there are multiple ground pins, right?

**Natasha Baker:** They say, yeah, ground's connected. I'm good. And they don't want to draw all the individual lines.

**Natasha Baker:** Yes, exactly. But then there's some people that want them expanded because they want all the individual lines. They want to like customize each, or they want to like, they want to like control each net individually.

**Natasha Baker:** Yep. Yep.

**Natasha Baker:** So because of that, we now have a feature that allows engineers to expand that ground pin, right? And to show all the pins. So that way they can kind of customize it to their needs.

**Natasha Baker:** Yeah. That's great.

**Natasha Baker:** So that's the other, that was like the other main learning, right? And so, yeah, we're working on some other ways of kind of further customizing the symbols and based on that.

**Natasha Baker:** That's great. Actually, that's a good lead into the fact that this is a centralized database. So obviously Snap EDA owns the IP, owns the knowledge of what's hooked to what. It is in some meta in between format. But then if someone, if I go to, if I go to the, you know, the, let's see, I'm on the page right now. If I go to the TSC 101 BILT, Current Sense Amplifier page, I can go and download that part for KiCAD. Someone else can go and click the different button on the same page and get the Altium part, the Eagle part or the whatever part. So it actually re-exports it from some meta format. So what does that look like on the inside?

**Natasha Baker:** Yeah. So we create everything in basically a neutral format that we then can convert to all the different file formats. So we've created export exporters for every single PCB design format that we support, which, you know, has its own challenges. Because there's different ways of defining different elements in every tool. Slotted holes in particular are quite challenging just because there's different ways of doing that. And in some cases there's, there's actually no way to create slotted holes in some PCB design tools. So we have to, you know, figure out the best practices in every tool. Yeah. I believe in Eagle, for example, we need to use the milling, you know, the milling layer because there isn't like an actual slotted hole element that there is in other formats. And I think even in KiCAD, I think it was relatively recent that they introduced the slotted hole shapes. Yeah, exactly.

**Natasha Baker:** I think that's right. Yep. Yep. Yeah. So you just have to deal with all the messiness of all these different CAD programs and all their own quirks on each individual level.

**Natasha Baker:** Yeah. But you know, our, our goal with each exporter is to make it native-like, right? So to get it as native as possible, that is what we've been spending a lot of time on is making sure that when you download the KiCAD symbol or when you download the Altine symbol, it looks as native-like as possible.

**Natasha Baker:** Yeah.

**Natasha Baker:** And yeah, like we want to make sure that it looks, it totally conforms to your, you know, to your circuit board design.

**Natasha Baker:** Yeah.

**Natasha Baker:** When you download it.

**Natasha Baker:** One thing I'm really excited about, so like the V6 KiCAD stuff is all of the symbol, right now all the footprints, even in V5, all the footprints are atomic. So you could basically get, get a SAT 23-5 and a SAT 23 and basically download that footprint and it just kind of sits there. But that was a mess for the symbols. And now in V6, it's going to do that. And I think that's actually going to play really well into the Snap EDA like workflow. Now it's like, I go and download TSC 101 or whatever the part is, and it's, there's a downloaded symbol, there's a downloaded footprint, and it's not like I'm downloading a symbol library like I have to now. So that's actually going to be a great change, I think.

**Natasha Baker:** Hmm. Interesting. So how is it, how is it like now then? Like what, sorry, what's the change it's going to be?

**Natasha Baker:** Yeah. Yeah. So right now when I download, so if I go to the TSC 101 page and I download the KiCAD version of the footprint and I download the KiCAD version of the symbol, the symbol is actually importing a, what it, what KiCAD interprets as a entire library. So you could actually stack 50 different components into that symbol library instead of that one file being just specific to that one symbol.

**Natasha Baker:** Right. Right.

**Natasha Baker:** So now that's changing in a good way. I think it's going to be a messy change, I think, to V6, but I think it's going to fit really well here because like I said, I want to go and download all these individual things. The export already works like that. But what it ends up as is right now with V5, I go download 20 different parts on Snap BDA. It's effective like I'm importing 20 libraries instead of 20 individual symbols, but it's just reusing. It's the only way to do it really. So it works, but it's going to get better.

**Natasha Baker:** Well, actually, and that's interesting. But also, I don't know if you're aware, but you can also batch export a library, a KiCAD library from our site.

**Natasha Baker:** Yeah.

**Natasha Baker:** So just FYI. Okay. And then it consolidates it all into one library. Yeah. So that's great. Yeah.

**Natasha Baker:** That's great. Okay. That's good to know.

**Natasha Baker:** One more thing is if you use our plugin, you can save it to the same library. So just another pro tip, if you want to add like five different parts, you know, you want to download five different parts. If you use our KiCAD plugin, you can save them all to the same library as far as I know. I don't know if you've tried that or not, but just another pro tip.

**Natasha Baker:** I mean, I'm usually doing onesie twosie type things too. I mean, like, I'll be honest, you know, I use Snap BDA for like the fancy parts. Mm-hmm. So recently I requested a part build that was like a weird 3D model. And I don't think the vendor one was available and the footprint wasn't available. And I'm like, oh, 50 bucks. That's like totally worth the hour I would spend on this and just getting it looking good. And like, you know, so then it looks good for my client. I can check the footprint, which was kind of weird too, against the data sheet. And it's just like, check it. Good. Go. Fine. You know, like that to me is actually like very valuable. So that's a recent use case.

**Natasha Baker:** Mm-hmm.

**Natasha Baker:** Awesome. Yeah. Where do you see all this going? I mean, like, so obviously it's growing by the day. It's 25 million parts. I was reading engineer number before. So it says in the little search bar, 25 million parts. How much bigger are we getting here?

**Natasha Baker:** So I think in terms of what's next for us, I mean, definitely we still have to grow our coverage. I mean, there's just, I feel like we haven't even scratched the surface of our vision, right? I mean, yes, we have symbols, footprints, 3D models, and we want to continue growing our coverage. We want to continue supporting more tools and supporting more preferences, right? So that's definitely in the short term. We've only just gotten started with where we want to go in terms of helping engineers with content, right? So we started adding simulation models, so Spice and IBIS models. And, you know, I definitely see us continuing to build out our coverage there. I have a lot of really, like, I'm just really excited about that space, honestly. I feel like there's lots of really interesting things that can be done there. We are also starting to introduce other, you know, larger building blocks, you could say, like reference designs.

**Natasha Baker:** Yeah, like subcircuits and similar type of things, right?

**Natasha Baker:** Yeah. There's that whole area. So, and I think, and again, I think that, like, that's kind of only the start of kind of our larger vision. I think where we want to go in the long run is really, you know, we want to just, the way I look at it is, like, the EDA tools are so good at creating the tools, right? And I think that they're doing a fantastic job. And I think in some cases we're seeing even, like, greater innovation in other areas as well. But, like, in general, it's like they do a great job creating the tools. But I feel like what's missing is how do we make it easy for engineers? Like, how do we make it easy for them to use those tools? How do we break down barriers in those tools themselves? You know, I think that, like, you know, I think a big part of that is content. But it's also tying the whole kind of design flow together. So when we look at how engineers are designing and, you know, how they're making design decisions and, you know, when they're placing down components, like, do they need to place down decoupling caps? Like, I think there's all these decisions that engineers are making.

**Natasha Baker:** Yeah. Like micro decisions.

**Natasha Baker:** Micro decisions that a company like ours can help to break down barriers for engineers to make those decisions easier using data, right? At this point, we've collected so much data. And by the way, we don't, you know, we don't release any of this data publicly. It's all obviously anonymous, but we've released, we've collected a lot of data about, like, okay, like, what components are engineers using? And, you know, what other types of components are they downloading with those components? And I think that where we're going next is really how do we help engineers to make their designs just, like, flow a lot more smoothly by helping them while they're designing proactively? Yeah. So I think that, like, we're going to move away from just being just a database towards how can we be a proactive, like, almost like an applications engineer.

**Natasha Baker:** Yeah. Right. Yep.

**Natasha Baker:** Like an applications engineer who's helping you, who's, like, there with you and, like, who's just kind of, like, helping you as you're designing. And I think that, like, we're not that far away from that because this is what we're doing right now is really the hard part, right? The hard part is really creating all this content because, again, there's so much of it. It's challenging to automate. There's so many preferences. But I think once we're there, I think that, you know, all of a sudden we can start leveraging that and giving people, like, intelligent recommendations that help them design a lot faster, a lot better. And that's where I think the value is. You know, I think the content's great. It helps people so much. And people love it, right? Like, they need it. They love it. They recognize now that, like, a lot of them don't want to go back, right? Like, we talked at the beginning of this podcast about, like, when I first started how people said they would never use this. But nowadays, especially the last three years, we're seeing this, like, shift, right? Where everyone's starting to use third-party libraries. And it's just something changed. Like, the world changed. The world's different.

**Natasha Baker:** Yeah.

**Natasha Baker:** And I feel like this is just the first step. I think that where we're going next is really the real value in the long run is helping engineers right when they're designing to make these micro decisions. And I love that. I love that term, micro decision. I think that's a perfect way to describe it.

**Natasha Baker:** Well, I'm going to ask you to do something in that I want you to push back on all the vendors. Because that's one of the problems here is that everything comes from a PDF in the first place, right? Everything is this lowest common denominator. Engineering drawing is, like, you can always pass a PDF around. You can always pass this other stuff. Like, why isn't that happening? Why isn't there some standardized digital format between a TI and an analog and an NXP? And, like, why are they all – can you go beat them up and get them in a room and just be like, no, do it like this? I mean, like, how do we do that? That's what I want to know.

**Natasha Baker:** That's an awesome question. Something we definitely hear a lot. And, yeah, I would love to do that. And, you know, the good news is we do work very closely with suppliers. One thing that we believe in at Snappy DA is that we believe that when suppliers win, engineers win and vice versa. So we don't see, like –

**Natasha Baker:** I don't know if I agree with that one. I feel like suppliers are all winning lately and I'm losing every time I go to order parts.

**Natasha Baker:** I think they're changing. I think they're recognizing that they need to – I think they recognize that they need to help engineers if they want to win in the digital age.

**Natasha Baker:** I guess. There's so few of them these days, Natasha. I mean, it's just like, I don't know. This is so big.

**Natasha Baker:** Yeah. They're all consolidating.

**Natasha Baker:** I get the general feeling you're trying to convey, though. I mean, like, yeah. It's not like we're all fighting different battles here, but it's just like – I feel there's so much entrenched – there's so many old ways of doing things and it's just very frustrating.

**Natasha Baker:** Yeah, but it's changing.

**Natasha Baker:** Well, that –

**Natasha Baker:** It's changing, Chris. Like, be positive.

**Natasha Baker:** You're seeing it more than I am, I'm sure. I'm sure you are. Great, great.

**Natasha Baker:** Yeah. Like, I'll say that there's definitely glimmers of hope.

**Natasha Baker:** Okay.

**Natasha Baker:** Okay?

**Natasha Baker:** There's chip companies that know what an API is and they know how to actually implement one and use one. Okay. No. Great.

**Natasha Baker:** Yeah. They are working on it. Great. And, you know, for a lot of these companies, it's multi-year initiatives because the way that things were – or the way that things are today is that a lot of these companies grew from acquisitions, as we were just saying. Right? And so there's some business groups in these large semiconductor companies who are fantastic at collecting all the specs and data and, like, they have it available via spreadsheets or even an API. Right? Some of the best chip companies and the best semiconductor companies and connector companies have APIs. But, like, the challenge that a lot of these companies have is that they don't have that data built up. Right? So they're doing all of these, you know, big undertakings right now that are multi-year projects to make their data available.

**Natasha Baker:** So they've got it all in, like, paper format and a filing cabinet somewhere and they still haven't moved into the digital age either?

**Natasha Baker:** If they even have that. Wow. Like, you ask some of these companies and they say, like, I don't even know where I would find that. I don't think we have it. Wow. Right? So, like, you know, I think that, like, they do recognize it. And I think that there are kind of, like, there is kind of, like, I would say this, like, changing of the guard in terms of, like, this, I would say, like, a new generation of marketing type of people who are coming up who are, like, oh, it just makes sense to support engineers. Like, we got to do this. I've been, like, I've been a big champion for this internally, you know? But they don't, it's like they're fighting their own battle, you know, internally.

**Natasha Baker:** What were you guys doing before?

**Natasha Baker:** Yeah. But, like, I mean, the thing, I think we have to, like, I don't know, I totally get your frustration, Chris, and it's good to hear that from you, too, just hearing the engineer perspective, which we obviously hear a lot. But what I do want to tell engineers is just, like, there are really good people at these component suppliers, right, who want to support engineers. Like, they want to do that, but they're fighting their own kind of battles with the legacy data that's available.

**Natasha Baker:** Yeah, I believe it. But it's changing. Yeah.

**Natasha Baker:** It's changing. And it's going to change. It's going to change. I am 100% sure about that.

**Natasha Baker:** I mean, so do you have any ideas about how to then push on these companies in order to encourage that change more? Because one thing that I think about is some of my favorite vendors are the ones that are putting models on DigiKey. And obviously, Snap EDA is now on DigiKey. And, like, seeing, like, digital access like that, like, that warms my heart. That makes me want to use their parts more. I feel like that in itself is marketing. But I don't know how to get that across. I'm only, you know, one engineer building however few products overall to the general market. And it just feels like it's not going to make a dent. So do you have any ideas on how to then push that back to them aside from doing a podcast about it and hopefully they listen? Yeah.

**Natasha Baker:** I would say, like, definitely contacting any reps that you work with and letting them know. They are listening. Things do move a little bit slower at these bigger companies, but they are listening. If you work with a rep, definitely let them know. Share it with distributors. I think the distributors are really educating the suppliers right now about the need for this content. So, you know, definitely reach out to the disties.

**Natasha Baker:** Okay. That seems very slow to me. That seems, you know, I feel like I'm going to start putting on, like, yeah, like, start a revolution or something like that. I don't know.

**Natasha Baker:** Yeah. I can tell you, like, I've been doing this for a while now. And I can definitely tell you in the last couple years, we're kind of pretty slammed constantly with supplier projects.

**Natasha Baker:** Oh, interesting.

**Natasha Baker:** We have a large demand. So things are absolutely changing.

**Natasha Baker:** Great. Yeah. I mean, it sounds like you're the tip of the spear here. I mean, it's great. I mean, and I hope it doesn't come across like, you know, my vitriol is not pointed at Snap EDA. It's more general frustration at the industry and companies like Snap EDA are actually helping. So that part's great.

**Natasha Baker:** Totally. And, you know, I think it's just education, right? I think that the people that are in marketing sometimes don't understand, maybe they haven't been PCB designers in the past, right?

**Natasha Baker:** Yeah.

**Natasha Baker:** So, and those are the people that are typically pushing forward this content, right? It's either the applications team or the marketing team. And sometimes it's just about educating them. You know, I'm thinking back to our first supplier customer. This was like way back. And I remember, you know, it's a director of marketing at a semiconductor company. And he was just like, can you like remind me? Like, I know we had this call, but can you remind me what the value is of having this content again? Like, can you remind me what this content is for and why we need it? Right. And like, he was like, you know, he's the director of a product line. Yeah. Like.

**Natasha Baker:** Yeah.

**Natasha Baker:** At the semiconductor company. Right. And because I think so, I think that like, there's an education thing.

**Natasha Baker:** Right. Because they're thinking like, how does this help me sell more parts? Right. That's, I imagine at the end of the day, that's what they're getting judged on. So that any call with someone like Snappy Day would be like, how is this going to help me sell more parts? But it's.

**Natasha Baker:** But it helps them sell so many parts.

**Natasha Baker:** I know. Exactly. It seems so obvious to us, but it's just like, to them, it's just like, well, but how many eyeballs will get in front of it? It's like, it doesn't matter how many eyeballs. It's that one eyeball. It's the engineer eyeball. You know, I feel like it's that thing where every single distributor, sales rep, FAE, everybody there, they come to me and they're telling me about a part three months too late. And the ones that are smart would think, hey, Snappy Day is there when I'm actually deciding, you know? And like some of the distributors are doing that too. It's like the important time, the time that matters for getting a, what do they call this? Winning a socket is not when the distributor decides to pop by and see if you can get lunch, if they even do that anymore. Definitely not for me. It's like when I'm doing a web search and like, oh yeah, that part looks good. I'll actually investigate it more. Or it's easy to get data or it's easy to get a sample circuit or something like that. Like that's when this content is gold, I think.

**Natasha Baker:** Absolutely. And like, I think the other thing too, that needs a little bit of just education too. I think it's that, you know, there's a difference between an engineer who knows the component that they want.

**Natasha Baker:** Yep.

**Natasha Baker:** And an engineer who is open to, you know, they're looking for something that suits their needs. Like there's a difference between someone saying, I want this particular sensor versus like, I want a sensor that meets these specs.

**Natasha Baker:** Right. It's like browsing versus buying or whatever it is. Like the person who actually wants the salesperson to come up to them at the store and be like, do you need help with something today? You know, like some people do actually want that.

**Natasha Baker:** Mm-hmm. Well, and even just like, I think in terms of design wins, right? Like if we think of, for these component suppliers, what I think, you know, I think for them, recognizing that this is a design win for them. And it's not always a design win. So if this FAE comes and takes you out for lunch, Chris, and they sell you on a particular part. Sure. Okay. Yep. And then they come to Snappy DA and they download that part. Well, that's not like a design win. Like the FAE won that, right?

**Natasha Baker:** Yeah.

**Natasha Baker:** But if you come straight to Snappy DA and you're like, oh, I want like, you know, a connector that has like 60 pins, 2.54 millimeter pitch. And then we like recommend one, you know, from a supplier and you download that, use it in your design. That's a design win.

**Natasha Baker:** Yeah, totally.

**Natasha Baker:** And so I think there's just like, I think just like education of, you know, educating the market on, on these different things is just, I think once it clicks for them and once they recognize it, they're like, oh man, like we need to, we need to do everything we can to support engineers. We need to do everything we can to, to get them this content.

**Natasha Baker:** Yeah. Well, I think one of the things that's kind of underlying the surface here is it is cutting out some of their traditional sales channels. And those sales channels are incredibly resistant to change because there's a ton of money tied up in there. I mean, like when an FAE comes by and buys me lunch, it's not because they like me so much. It's because there is some, you know, payoff in the end if I do design in a chip there. And that's why they don't buy me lunch anymore because I don't have the buying power anymore. But like, like, yeah, that, that is, that's like the inherent part of the system. So does that mean that Snappy DA is going to start killing things like component registrations? Because I don't know if I've mentioned that on the show, but I'm sure I've mentioned on the show before, but that is an insane system. In my opinion.

**Natasha Baker:** It's insane. And, you know, we're not here to disrupt any industries. Like, that's not what we're here to do. Like what we're here to do is, you know, what we're here to do is basically, you know, looking at that industry and that whole process. It's so inefficient and it's so archaic. That being said, there are certain components that are very complex that need a lot of assistance. Right. And we're not here to say like, we're going to like solve that. Right. What I will say is that we're another channel that's a lot more cost effective, like, you know, magnitudes, orders of magnitude more efficient, like than flying over to another city and like, you know, renting a car and driving to an office and taking Chris out to lunch.

**Natasha Baker:** In the times of COVID, specifically, it's offset very well, I'm sure.

**Natasha Baker:** Oh, in times of COVID, we've had people, you know, reaching out for this exact reason. They're like, we can't sell the traditional way we used to sell. We need to evolve. We need to change. And so I think that this has kind of been a forcing function, the whole pandemic situation where they can't do that anymore. But on top of that, I think they're starting to realize like, yeah, that wasn't very efficient. So I always think there's, you know, I always think there's going to be a place for that. Right. Because these really large deals, like you're not going to land, you know, Apple, you know, you need to have that human touch. Right. Sometimes.

**Natasha Baker:** Yeah, sometimes.

**Natasha Baker:** But I definitely think for the long tail and 80% of like design ends, like I definitely think that a system like ours, obviously it's a lot more efficient. And obviously there's just a lot more insights that we can draw about how they're selecting parts and using data. And we can kind of bring this into, you know, the modern day age. So, yeah, you know, that's definitely what we'd like to do. And I think that's win-win for everybody because what this means for engineers is these companies operate more efficiently, which means that hopefully can also be reflected in the cost or through investment in other types of content. And of course, the only way that an engineer can discover components on our website is if it has content available.

**Natasha Baker:** Yeah. Right.

**Natasha Baker:** If it has the symbol and footprint, it gets boosted. If it has free samples, it gets boosted.

**Natasha Baker:** I didn't know that's a thing. That's a thing.

**Natasha Baker:** Yeah. We have free samples on our site as well. Our whole idea is that like the more we can like make it win-win between suppliers, engineers, and Snappy DA, like the more we're all going to win. We really look at it as like everything we do has to line up. It has to be like ultimately be for the engineer. Like we'll never do anything for suppliers that is going to jeopardize an engineer's ability to get their design done. So we always put the engineer first.

**Natasha Baker:** Yeah. That's good to know. I mean, so you do have analytics on the other side. I'm curious just kind of maybe if you can put your former technology contributor Forbes and Reuters writer hat on. So what are some trends that you see? Obviously, you see a ton of data coming through. You see how engineers are searching for parts, finding parts. Do you have any like broad trends or do you publish any broad trends anywhere?

**Natasha Baker:** That's a good question. We do publish some trends on our Snap Insights blog, which is kind of like a blog for suppliers. In terms of trends, I can't really think of anything. I'm sorry. I could probably send you stuff after.

**Natasha Baker:** That's okay. I mean, yeah, no, that's okay. I should have asked you that beforehand. Yeah, no, that's the kind of like from a... I think, well, you and I talked about this before the episode started as well. Like I'm very interested in like the popular parts, not in like a high school clicky kind of way. But like in a, you know, like I'll go to like an LCSC and I'll go and find what's the most, you know, what's the part on there that is big in the Chinese ecosystem or what's available online in the Chinese ecosystem. Just because I want to see what is going to be high volume and I use that as like an approximation for low risk. And like, so like that kind of thing is interesting to me. Same kind of thing, like to give an example of, you know, a silicon example between NRF52 part family, what is the one that's most popular and most likely to stick around? And that could be the footprint variant or the, even the functional features that are available on a thing. If I have a pretty loose spec for myself, then I'm going to go towards popularity. And that's always something that I try to find, but it's hard to, it's hard to draw that out because that's not something that they want to publish. And I can imagine the same thing. If I go to a DigiKey, they don't want to show that like, oh, everybody buys this one TI part because it's cheap and it's, you know, readily available. But I want to see that. So how do I see that?

**Natasha Baker:** Yeah, that's a really awesome idea. Like we don't, today what we do is we show like the number of downloads. So you could absolutely open like multiple variants of the component and look at how many times it was downloaded, which is a really good proxy for that. But I love the idea of like ranking them. You know, it's not something we do today. We do have like, there's a few categories we show like, oh, these are the top like DC DC converters or these are the top amplifiers. But yeah, I think that's a really, really cool idea.

**Natasha Baker:** Yeah. Yeah. I mean, so when I was working on like, like fine chips and parts IO when I was at supply frame, that's one thing we, we, we did like a risk rank and all this, you know, like a name for it or whatever. And it was kind of popularity based for the data we had. And, but like at the end of the day, that's all I want to know is I just want to know when there is a jelly bean component, I want someone to put a line in the sand and just say, oh yeah, this is the one, you know, like that's, that's really hard to do because obviously the industry is gigantic. Like you said, a billion parts and tons of variation between them. So I don't know. I just, I just want to, I just want an answer, Natasha, you know?

**Natasha Baker:** Well, you're right though. It's like an, it's, it's the 80, 20 rule, right? Like, so like, yeah, I mean, you'll definitely see that 20% of parts dominate 80% of the downloads. So I think what you're asking for is totally solvable. Like I could absolutely go into our backend analytics and like pull that for you in like two minutes. Cool. So I definitely think surfacing that for, yeah, for engineers, I love that idea. It's definitely something that I talked to my team about. I think that's great.

**Natasha Baker:** Coming soon. The amp hour snap EDA report. That was the NFL theme that I didn't sing an NFL theme there. Sorry.

**Natasha Baker:** Well, if I would have known, I would have absolutely brought that. I can send, you know, I can send it to you after the meeting. I know it's, we've supplied it before to EE times and to some other press. So I'd be happy to send that over and it might be interesting for, yeah.

**Natasha Baker:** Okay. That's great. That's great. I mean, so you do, and you do have an analytics side of things, but that's actually more for the chip companies. Is that right?

**Natasha Baker:** It is. Yeah. So we give them aggregated analytics. These are your top 10 most popular products, or these are the keywords that engineers use to discover your parts, or these are the countries that engineers downloaded in. So yeah, we give them aggregated insights through there.

**Natasha Baker:** Yeah, that's great. I mean, and that's the thing. Like it does, it is very symbiotic, right? One part of me kind of bristles at the idea of like data being shared by that, but then I think the logical brain's like, yeah, but if they get that data, they're going to make more parts you like, Chris. You know, like that's, that's at the end of the day, it's like, it's going to make better parts, better delivery, better supply availability, that sort of thing. So that's actually really great.

**Natasha Baker:** We don't share any personal information with the suppliers.

**Natasha Baker:** Yeah, exactly. That too. Yeah, right. Then, like I said, it's, it's lizard brain versus logical brain there. And once the logical brain takes over, it's like, oh, okay, yeah, that's fine.

**Natasha Baker:** And what I will say is like, I think that in the industry, a lot of, you know, one of the things that we have not done from the beginning is we do not share personal data with suppliers. And I think that's something that's really unique about us. We've gotten a lot of pressure from suppliers because, you know, that's the easy way for them to see the value in us, right? Is, oh, I just want the contact information.

**Natasha Baker:** Yep.

**Natasha Baker:** It might not be the most valuable thing that we provide, right? In the long run, obviously design wins a lot more valuable. But for them, it's like the instant gratification of like, oh, we fulfilled our lead goal for the quarter.

**Natasha Baker:** Yeah, I know. It's, it is, it seems like, it seems like these lopsided like systems of like, especially if you're working with marketing departments, they just need number of leads. And then they're going to span the crap out of that lead. And then it's like, okay, well, look what that did. Yep. It's like, it's like, yeah, it's like ruining goodwill too. I don't know. It's, yeah, it's, I think it's just a lopsided reward. Absolutely.

**Natasha Baker:** Totally. And well, I mean, it comes down to, you know, short-term versus long-term value. And I think that like, it's, it's easy to jump at like, oh, this is the short-term both, both for us. I mean, that would be like an easy thing for us to sell, right? Is just be like, oh, we're going to sell all the contact information and what they downloaded. Right. Like that's not something we do. And we've never done that. And I think that we've, yeah, well, we've had so much pressure from suppliers and we've stayed firm because. That's good. What they say to us is like, you know, all these other library solutions are doing it. Like, why aren't you guys doing this?

**Natasha Baker:** Talk about high school click right there, right?

**Natasha Baker:** Yeah. No, totally. They're just like, let us give you some advice.

**Natasha Baker:** Oh yeah. Right. Right.

**Natasha Baker:** It's definitely been like, we've had to stand our ground, but yeah, you know, the data that we provide is all anonymized and it's literally just, it's like going into Google analytics. That is the best analogy because think of our search engine. It's like organic searches, like Google's organic searches. We have our promoted parts, kind of like Google ads. Yeah. And then we have the analytics dashboard that is just like Google analytics, which gives you the high level insights, but we don't give IP. We don't give any personal information in there.

**Natasha Baker:** Where are people coming from? So I mentioned that Snappy DA is on DigiKey now. That's how I see it a lot. Obviously Google results, people search on the site. What would you say is the, how most people are using it? Do most people you find are using actual SnappyDA.com?

**Natasha Baker:** Most, I would say it's about 40% of people that come direct to us. Yeah, that's great. Or so. It's a big chunk that come through search, maybe 30%. And then, you know, the rest are referrals. I think distributors in total make up about 10% of our traffic.

**Natasha Baker:** Where else would people see you? I mean, it's distributor sites and like within like, is it within any CAD programs or anything like that?

**Natasha Baker:** Yes, it is within CAD programs. Oh, cool. Yeah. So we have Express PCB. We have PCB123.

**Natasha Baker:** That's the JLC one. Is that the Express PCB or no?

**Natasha Baker:** No. So Express PCB is, they're owned by Sunstone. That's their tool. Oh, that's it. So PCB123. Yep. There's Proteus. And we're working on a few mores that are native. We also have like plugins in those tools. So for Altium, for KeyCad that we built. And then, yeah, we have a bunch that are coming soon as well. So that's the other way.

**Natasha Baker:** Awesome.

**Natasha Baker:** Yeah. And we have some new products that are going to provide new ways. But I'd say the biggest ones are people coming straight to our website or through Google. Yeah.

**Natasha Baker:** Yeah. That's awesome. Well, that's great. And I mean, one of the benefits of the site too, is that there's tools on there like the InstaBuild, which is like a new tool. What is that thing?

**Natasha Baker:** So InstaBuild is a computer vision based schematic symbol builder. So the idea is that, well, if you go on there, basically you can highlight the pin table in a data sheet. And what it does is a little, it uses OCR, optical character recognition and computer vision, simple computer vision to detect the table and lines. And what it does is it extracts the information from the table. And then what we do is we can detect, is this an input? Is it an output? Is it a power pin? And we try our best to detect what it is and categorize the pin appropriately.

**Natasha Baker:** Got it.

**Natasha Baker:** And then you as an engineer can go in and make any tweaks you want to the pin designations. From there, we use those pin designations to automate the symbol configuration, knowing that a lot of our engineering community likes a logical flow of symbols, right? So inputs on the left, outputs on the right. We then automate the symbol based on that and attach it to an IPC compliant footprint. So long story short, what this tool does is within like two minutes, you can build a symbol and footprint for your design just by highlighting the pin table, basically.

**Natasha Baker:** Mm-hmm. Yeah, that's great.

**Natasha Baker:** So it's something engineers really like. And yeah, it's fun to use too.

**Natasha Baker:** Yeah. The only thing that was weird about it is like I used it once and then it says like, oh, this is only, so this is only available for me, right? So it's like a custom per time thing. Like if I go and use it for one part, I expected it was going to be more broadly available after that, like building out the database, but that's not the case. No.

**Natasha Baker:** So, well, it's definitely something. So, I mean, it's definitely something that we've considered doing, but what we realized is that a lot of times the data that's generated because it's user generated content, it is a little bit risky. Got it. So what we do is we only make it available to the person that built it. And what we found is that engineers actually are happy about that just because the data is, you know, it's definitely hasn't gone through any vetting. That being said, our long-term plan is, so what we're planning to do is we're planning to, you know, just say five different people build the same symbol. Oh, yeah. Then our plan is to say, okay, is the pin mapping consistent? Are the pin designations consistent? Or, you know, correct in 80% of the cases, right?

**Natasha Baker:** Yeah, right. You start to do like a SBC almost on a particular part, kind of generate.

**Natasha Baker:** Exactly. Yeah. That's our long-term plan. So it's definitely something we're planning to expand really soon. The original goal was absolutely like, okay, let's use this to kind of, you know, build out our library further. But, you know, we also, it's always a trade-off between building our library really quickly and potentially introducing errors.

**Natasha Baker:** Yeah, right. And like you said, you have to build the trust. You've built the trust and people have switched over to thinking about Snap BDA in a positive way now. So you wouldn't want to ruin that. So that's smart.

**Natasha Baker:** Yeah. But, you know, you make a good point. So it's definitely something we want to, we just want to do it right when we release it. So, yeah, we've had some people on like, I know on YouTube, like wondering why their parts weren't showing up. And, but yeah, we've done a lot of surveys. And what we found is that people really appreciate that it's only available to them. Like other people. Other people are happy that that data isn't in our system. Yeah. Yeah. Yeah. Yeah. And you know, another thing too, is sometimes when people use it, they don't know how to use it. They don't recognize that like that's going to show up on the site. And like, I think that, yeah, we just want to make sure we do it right. If we, if we release it to the public.

**Natasha Baker:** That's great. That's great. Last question on the analytics side of things. I'm curious about like the split that you see on the export kind of thing. So you get kind of an ad hoc view of the CAD landscape as well, or at least the CAD landscape of people that are using it, Snap EDA, using web tools in general. Do you have like percentages on what the exports look like?

**Natasha Baker:** Yeah. So Altium is absolutely like the number one.

**Natasha Baker:** Yeah.

**Natasha Baker:** Altium is number one. And then it's next is Eagle. Orcat and Allegro and KiCat are kind of tied. Those are probably like each. So I think like, you know, Altium is probably like 30%. Eagle is probably like 25%. I'm guessing KiCat, Orcat and Allegro are probably like 15% each. And then it kind of goes down to the rest, like, you know, mentor pads and some of the other tools.

**Natasha Baker:** You've got some old ones on there. Like, well, maybe not old. I just don't, I don't recognize them. Like Target 3001. I don't know that one.

**Natasha Baker:** Yeah. Target 3001 we just introduced. So they're in the UK and I believe they're in the UK or, or, or somewhere in Europe.

**Natasha Baker:** Okay.

**Natasha Baker:** And yeah, so they're like, they're a, yeah, they're a totally inactive tool and they have a community and, you know, you'd be surprised how many PCB design tools are out there.

**Natasha Baker:** Oh yeah, exactly. And if you, and if, especially because you're building exporter too, it's like, once you put that, you hook, they put the hooks in place. It's like, you basically open up an entirely new net market segment, especially one that's probably going to be very, very thankful that they're like, oh, someone cares about us instead of being like, we have to go and create all this stuff from scratch now. You know, like that, that sucks. That's, that's the pain of library management.

**Natasha Baker:** To your point though, there's, you know, going back to the 80, 20 rule, it's definitely dominated by, you know, by a few major players. So I think there's kind of diminishing returns. Once we start expanding, we obviously want to support everyone that we can. That's part of our mission. We're going to absolutely keep expanding to more, even if they have smaller kind of communities, but you know, 80, 20 rule is absolutely at play here where 80% of engineers are using Altium, Cadence products, KeyCad.

**Natasha Baker:** Got it. Yeah. Yeah. Like the big players and stuff like that. Yeah. That's great.

**Natasha Baker:** Yep.

**Natasha Baker:** Cool. That's really good. That's really good to know. I'm curious too, because like the, it seems like some of the tools, like, so like Altium has some capabilities on internally as well to, to like, obviously there's the, the Snap EDA plugin, but then there's also like some internal libraries that are available, right?

**Natasha Baker:** Yeah. So they have, I think they have like their own search kind of capabilities, I think with Altium 365.

**Natasha Baker:** Ah, right. Yep. Yep. Okay. That's like a new, yeah, it's a new, a newer, newish offering, not new, but like, uh, yeah, that's subscription service they have. Right.

**Natasha Baker:** Mm-hmm. There's just so many components out there. Right. And I think it comes down to like core competency. What is the core competency of the company? And, you know, at Snap EDA, we've kind of taken this bet that like this problem deserves focused attention by, you know, it's enough to be a company. Right. And I think that like anytime, I think that the reason why Altium is such a big part of our user base is because it's just really difficult for any company to solve so many problems at once, you know, and, you know, for them to build up this massive database. And I think they have a lot of great different, you know, companies that they've now acquired and things like that. But I think regardless, it's, it's challenging. It's challenging for one company to tackle that. And, and we've kind of taken this bet that like there's a large challenge here with content in, in design tools that the EDA tools can't solve themselves. I mean, I used to work on the inside of an EDA tool. So I know the challenges that EDA tools have, you know, uh, in terms of R and D and bandwidth and things like that.

**Natasha Baker:** And, uh, yeah, they're all small, small teams to start with. And if you're focused on the actual, like making the core tool better, the data becomes like the secondary concern, maybe as at least, yeah, again, like the, the lopsided reward systems, you know, like the, the tool system or the tool maker is going to make sure the tool is the best thing it can be. It doesn't, they don't care about the data, especially over time, I would imagine.

**Natasha Baker:** Right. Exactly. I mean, I think that Altium is a different kind of company, right? Like I think Altium special in the landscape of companies. I think that they are obviously, you know, pursuing a different strategy where for them data is more important, right? If you look at content in general, that Altium is doing a fantastic job with that. So I have so much respect for them and I think they're incredible, but I also think that like engineers deserve a company that's like really focusing on this, right? Because I think there's just so much opportunity and there's so much that, that these large EDA companies can't do. Even if they want to have a strategy that pursues content and things like that, you know, I think ultimately they'll need to work with other players in the space to help them with that.

**Natasha Baker:** Yeah. That makes sense. That makes sense. Well, what else should people keep an eye on with Snap EDA in the near term? Which, or maybe, and then also how can they, how can people get started with it right now?

**Natasha Baker:** Sure. So we are launching some really cool things in the next month or so. We have, I think, two particular launches that I'm super excited about. So stay tuned and keep an eye on our Twitter channel, I guess you could say. But one is just something that I'm just like, I've just been pumped about for a while. So keep your ears and your eyes and ears open for that. But I think in terms of how to get started, Snap EDA is totally free. Engineers can go to www.snappida.com to get started. And yeah, I mean, it's super easy to use. You just basically create a free account. You can start searching for, you know, a part that you need for your design, download it, and then import it into your design. If you're using our plugins, you don't even need to import. You can place directly from the EDA tools. So, you know, in KeyCAD, you can just search and then place or search and add to library. So yeah, it should be pretty intuitive. And yeah, I hope people give it a try. And yeah. And, you know, I think the one other thing I'd like to say too is that our team is so, so focused on building a great tool for engineers. And they're building it, like we're all building it for the right reasons. We truly believe that the industry needs this and we want to help, you know? And I think that sometimes what people don't realize is we have incredible technical support. We have people that are doing technical support all day and like they are here to help. They're engineers. They're very skilled. They are very experienced. And we want to help engineers. So if a library, you know, if you are, you know, you download a library and you're like, hey, this doesn't look like the rest of my, you know, the symbols of my KeyCAD library, or I'm not sure how this slotted hole is defined. I don't understand, you know, why this is defined on this particular layer.

**Natasha Baker:** You want to like dig in, dig into the, into the nitty gritty with the, with the engineer behind it. It sounds like you can, people, the people listening here can get in touch with them.

**Natasha Baker:** Yeah. Like we're here to support you. If you ever find issues, like we're here for you. Like we want, we want to make sure that Snappy DA is the place that we're always iterating. We're always improving. We're always pushing the boundaries, you know? And, you know, we can't do this in a void. Right. So I think that like, that's something I want to also share is like, please share your feedback. If you guys have feedback for us, whether it's good or bad, like please share it with us because that's the way we keep improving. And what I can tell you is that we go through every single piece of feedback with our annual survey, we had over 2000 responses and we went through every single response. That's great. Every single one. And we use that to define our roadmap as like one of the inputs. So I just want people to know that because sometimes like I noticed that people will ask questions on forums that they could just come to us and probably get the answer, you know, like definitely use the forums. That's totally fine. But you know, we're here for you. So I just wanted to share that with everyone.

**Natasha Baker:** What's the best way to push that feedback to Snap EDA?

**Natasha Baker:** So we have an intercom chat in like the, you know, bottom right-hand corner.

**Natasha Baker:** Oh, the little chat bubble?

**Natasha Baker:** Yep. Chat bubble. We also answer, you know, support at snappy.eda.com. There's also on every single part page, you can report issues.

**Natasha Baker:** Ah, that's great.

**Natasha Baker:** We have people that are constantly going through those. So, you know, we have people who, for example, maybe they are using an older version of the EDA tool and they can't import it or whatever. And like someone will be there to assist you. Great. So, yeah, I just wanted to let people know that we have like multiple channels. And, you know, if we don't know, like if there is something we don't support and that you guys really want, like if we don't know about that, then we only can do so much as we know, you know? And we do have a team that obviously, you know, lots of PCB designers on our team, but no one knows the tools better than the people that are working on them day in and day out, which is all the PCB designers out there. So, you know, if you guys are like, hey, like, you know, I noticed that this silkscreen width is like inconsistent with the silkscreen width in KECAD in the native libraries. Like, please share that with us. We can update our exporter. You know, we can look into that. But again, if like people aren't complaining to us enough, like, or not enough, but if they don't come to us directly.

**Natasha Baker:** No, no, no, you said complain. If people are going to complain, Natasha, you're going to get it.

**Natasha Baker:** No, I mean, and like, you know, and we're good with that, you know?

**Natasha Baker:** It's a valuable feedback is what you're looking for, it sounds like.

**Natasha Baker:** Valuable feedback, you know, like, I mean, you know, complaints are fine too, honestly. Like, I get it. I use a lot of tools on the web and, you know, I'm an electrical engineer who I also like, I want things to work. I want things, I have high, you know, I have high standards of excellence.

**Natasha Baker:** She's saying she's grumpy too. That's what she's, that's what I'm hearing. It's great. I am grumpy, you know? Grumpy engineer builds tools for grumpy engineers. That's what we want. That's what, that's all we've ever wanted.

**Natasha Baker:** You know, I am grumpy because, and I get it, you know, PCB design. There's so many details and I get it. You know, maybe try to be a little bit nice. There are people at the end of, you know, the support channels. Oh yeah.

**Natasha Baker:** Yeah. There are humans there, right? It's not, it's not some AI bot.

**Natasha Baker:** There's humans there that aren't me. Like this is their job and, you know, so be nice, but like, you know, please, please be vocal and, you know, and, and I think that like, I just want everyone to know that because I, you know, I think that on our team, like we truly have a team that is so committed to building something great for engineers. And it's so much more than just making money because if it was just about that, we would be selling leads all over the place and selling contact information. Like, like we would have done that years ago, but we, we truly are doing this because we care about our community. We care about engineers and we care about solving this problem and moving the world closer to our vision, which is how do we break down barriers for engineers? And, you know, we have a long way to go. We're not perfect. There's things that, you know, we know we need to solve, right? And there's things we know we need to do. Every day we wake up and we're focused on the things that we know our community cares about. So please do reach out. And I think that's basically it for me.

**Natasha Baker:** Okay, great. Well, thanks so much, Natasha. We'll, we'll definitely have links for everything. And hopefully that we'll, we'll, you and I will talk after this about the, maybe having that report on the backend that we can pull into, into the show notes and things like that. So please, people can check out the show notes and check out snappida.com. Thanks so much for joining us, Natasha. We're looking forward to seeing more fun things from snappy DA here soon.

**Natasha Baker:** Thank you so much, Chris. Thanks for having me.

**Natasha Baker:** Today's engineering content was made possible by the generous Amp Hour community members at Patreon. Join us at patreon.com slash the Amp Hour. You can share your latest footprints, symbols, and most importantly, opinions on our Discord. We'll see you next time.
