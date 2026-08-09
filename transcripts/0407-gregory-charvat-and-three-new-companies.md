---
episode: 407
title: Gregory Charvat and Three New Companies
url: https://theamphour.com/407-gregory-charvat-and-three-new-companies/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released September 16th, 2018. Episode 407. Gregory Charvat and three new companies. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Gregory Charvat:** And I'm Gregory Charvat, author of Small and Short-Range Radar Systems and the Chief Technology Officer at Humatics Corporation.

**Chris Gammell:** Back once again with a new title, but doing similar things, it sounds like.

**Gregory Charvat:** That's right. Yeah, I wrote the book on what we're doing, so that helps. That helps in the job a little bit.

**Chris Gammell:** It does. You know, that recruiting effort is really easy when it's like, hey, we should just get the guy who wrote the book.

**Gregory Charvat:** Yeah. Well, that's why, Chris, that's why it's always awesome to write a book. I think you should write it.

**Chris Gammell:** Yeah, I think you've told me this before, but I still don't think I'm on board with this one. We'll keep talking about it.

**Gregory Charvat:** Old media, man. Old media. It's still around. It serves a purpose.

**Chris Gammell:** Dead trees can do things.

**Gregory Charvat:** Yes. That's right. Well, dead trees last longer than software. We were talking about software earlier as we were trying to get the audio to work today.

**Chris Gammell:** Another day of, yes, audio woes. Yeah.

**Gregory Charvat:** Yeah, and I'll tell you, things are often a software problem, and I think it'll be a struggle in the future to maintain all of the wonderful media that we have today. The paper will outlive the digital, I believe.

**Chris Gammell:** That's true. And I have referenced this before, but I was at a talk where Bunny Huang was giving a talk about tech, and he was comparing the frameworks of software versus a soldering iron. And it's, you know, soldering iron is a little bit more, a little bit more regular, you know?

**Gregory Charvat:** That's right. That's right. I mean, think of it. When they're digging up the landfills that are full of old televisions and CRT monitors 10,000 years from now, they're not going to find software down there. They're going to find circuit boards and lead and resistors and capacitors. That's what they'll find, Chris. Think of it that way.

**Chris Gammell:** Okay. That's good. For better or worse. So, Greg, for people who have not heard you on the show before, I will obviously link in all of the episodes you've been on before, but can you tell people a little bit about who you are and what you do?

**Gregory Charvat:** Yeah. Let's see. I started in the electronics hobby at an early age, like many of us did. In fact, back in the 80s, I started. I'm taking apart televisions and radios and things like that. In grad school, I taught myself how to make radar imaging devices and systems. And from that work, I was recruited into MIT's Lincoln Laboratory. I actually earned my PhD in applied electromagnetics. And at Lincoln, I built the MIT Thruwell imaging radar, as well as created the project-based learning class, Build a Radar System with coffee cans and wood. Coffee cans, yeah. Yeah. And that thing now is going on seven years, continuously. Wow. And many universities, institutions, and so on and so forth have adopted it and actually improved it dramatically in some instances. So, that's kind of cool. I was a visiting researcher at MIT Media Lab under Ramesh Raskar, where I created the time of flight microwave camera. So, you could actually watch a pulse of microwave energy propagate across a target, let's say, a book or a series of, I don't know, spheres or whatever you'd like. It would be as if you could put on microwave goggles and see the radiation. So, I did that. I wrote a book. When was that?

**Chris Gammell:** I don't know if I've ever seen that. I heard about that one.

**Gregory Charvat:** I think that was sort of between podcasts.

**Chris Gammell:** Oh, okay. Yeah, I was going to say, I just looked it up. The last time you were on here was, geez, 2014. Wow.

**Gregory Charvat:** 2014. We published that stuff, the microwave camera and nature scientific reports in 2015. So, it was on the DL at the time, but that was another garage-based project. And it basically, Ramesh, I was a visiting researcher. I was basically kind of hanging out with all of his grad students and postdocs up at MIT once a month, and I would help them with their projects. And Ramesh says, yeah, I appreciate your help, but I want you to do something really creative and unique. What do you want to do? Think about what you want to do. And so, I thought, oh, I know what I want to do. It's simple. I want to see a pulse of microwave energy propagated across something, and I want to slow down the speed of light so I can watch it propagate.

**Chris Gammell:** Of course. All right. Why not? Right? Yeah. Why not just change the nature of the universe?

**Gregory Charvat:** So, we did that, and I kind of like, I built this prototype and leveraging a bunch of equipment in my lab here, and it worked beautifully, and you could actually, it was the coolest thing. You could take, like, let's say, you know, here's a very canonical version of it. You could take a bunch of thumbtacks, stick them in styrofoam, which is transparent to microwave radiation at our frequency of 10 gigahertz. And you'd actually, you could radiate it from different angles. If you radiate it from the side, you could actually watch the pulse, hit the first group of thumbtacks, then hit the second group, and the third, and the fourth, and the fifth, and play it back.

**Chris Gammell:** As you say, when you say watch, you mean you have a secondary observer, like another microwave receiver or something?

**Gregory Charvat:** Yeah, yeah. You have a camera. You have a lens. So, it was actually an optical system, but it was at the microwave frequency. So, it was optical, and I had a single pixel, and I would scan it into one position, then I would ping the radar. That scan again and ping the radar. So, it was not a real-time system, but it was all the same, and the target was stationary. Like taking a picture in 850, you know, everyone has to stay still. Yeah. In our case, you have to stay still for 45 minutes. Oh, we take the microwave picture. But unlike a still picture in the 1850s, 1840s, this camera would actually take a video of the microwaves traveling at the speed of light and slow it down. So, that was the really super unique and unusual thing that we did. So, you could watch the pulse. You could watch the flash of the camera travel towards the target, bounce off of stuff of the target, and back to the camera. You could see it, which was the coolest thing ever. You could actually see when the pulse, you know, microwave energy scatters and bounces back and forth, just like light does. Sure. But with microwaves, we could slow it down so you can see it, because vis-a-vis coherent processing, which is what I did for this thing.

**Chris Gammell:** I don't quite understand the filter. So, you said there's a microwave filter for a camera? I don't understand the electromagnetic versus... I mean, I know that light is electromagnetic as well. It's all the same. But, in my mind, I keep those separate, because they're both confusing in their own ways. Yes.

**Gregory Charvat:** Well, a lot of people do. What happens... You know, if you look at Maxwell's equations and you start deriving them from scratch, which is a painful thing to do. You know, on Saturday night activity. Yeah, exactly. At some point, the folks with the electromagnetics background, like myself, the EM background, they go the fields and waves route. And the optic people make a few approximations. Now, as fields and waves people, we make different approximations to solve Maxwell's equations. But the optics will make a different series of approximations. And their approximations include the fact that their optical apparatus tend to have many, many wavelengths of... Like, their lenses are many wavelengths in diameter and width and height. Their apertures are many... Like, thousands of wavelengths. The distances between things are zillions of wavelengths apart. So, they have this, like... They can make some approximations that we can't in the microwave world. And so, that's where the two fields part ways. And so... But what you can do is you can say, hey, I understand that fork in the road, that theoretical fork in the road. Let's go back to that fork and see what we can do with microwaves and optics. Let's just put them back together back at the fork in the road. Let's bring that fork. Let's make that... Let's get rid of that fork. And see what we can do.

**Chris Gammell:** You're like, you know what? Fork it.

**Gregory Charvat:** Fork it. Yeah. I think that's pretty funny. Yes. Fork it. Fork it. Yes. Stick a fork in it. Yes. But anyway, that's what you do. Yeah. Okay.

**Chris Gammell:** I still don't quite understand the logistics of that, though. So, like, what is... What does a filter like that look like? Is it just a piece of material?

**Gregory Charvat:** No, it's a measurement. So, it's just a measurement. So, how do you...

**Chris Gammell:** So, when you spoke about a filter, I was... You know, when you say camera and filter, I think of, like, a thing you stick in front of a lens. Right. But you're saying, like, a mathematical filter.

**Gregory Charvat:** I would say... No, I would say method of measurement. I may have misspoke when I said filter. I think what I meant by that is we are a different wavelength. We're at 10 GHz as opposed to, you know, the nanometers of the optical wavelength. So, things look different. And we're only processing electromagnetic radiation at this longer wavelength. But it's all the same. Otherwise, I mean, the ways in which you deal with it. Except it is physically the same. But the way by which you can process the data and acquire it is different. So, it becomes a lot easier to do things like slow it down and watch it propagate across... To back up a little bit, it becomes easier to measure the time of flight. It becomes easier to see the radiation in some senses. You could do things like phase-cohered processing, which are very difficult to do at the optical frequencies. You could do it at the microwave frequencies. And so, using that, I was able to more easily measure the time of flight and actually do some stuff that is normally pretty hard to do. So, anyway, that's kind of why it was cool. It was just sort of combining the two things. And it's fun to combine stuff.

**Chris Gammell:** I think we're going to come back to time of flight here in a little bit. Yes. But before we get to your current stuff, you had another thing in the middle. Like I said, you've been busy. So, you're currently the CTO of Humatics. Yes. What was before that?

**Gregory Charvat:** Before that, I co-founded two companies with Jonathan Rothbard. And one of them is called Butterfly Network, which right now they are fielding a large number of pilot systems, I would call it, to key partners. It's actually an ultrasound on a chip.

**Chris Gammell:** Yeah. This is... My friend, who's an ER doctor, told me about this separately. He's like, man, you've got to see this new thing. It's like an ultrasound you can stick in your pocket for like two grand. And he's like, I've got to get my hands on one. And I'm like, oh, I think I know who helped make that. Yes. So, holy crap, Greg. Like, what is this thing?

**Gregory Charvat:** That was a cool project, man. That was awesome. Yeah.

**Chris Gammell:** So, tell us about it.

**Gregory Charvat:** That's a tough one. That was awesome. So, what we did was, you know, we started the company. There's three of us. Myself, another guy, Tyler Ralston, and Nevada Sanchez with Jonathan Rothbard. Jonathan is a very successful serial entrepreneur. Pretty wealthy guy now. And he just likes taking on really nasty problems that wouldn't normally be funded by venture capital. Like, tough, tough problems. And things that will take sometimes years to figure out. And this was one of them. So, we started the company as an ultrasound tomography company. And then we realized that, you know, the cost of goods for the ultrasound tomography didn't really align well with the market.

**Chris Gammell:** And tomography is like, that's computerized tomography? Yes. Like a CT scan?

**Gregory Charvat:** Yep. You can do it with ultrasound. You can actually transmit ultrasound signals through the body and do the same processing as you would with a CT scan. And actually, the ultrasound system gives you time of flight and phase information, which you can't do very easily. There it is again, folks. Exactly. Time of flight. Yeah.

**Chris Gammell:** We're going to have thematics here.

**Gregory Charvat:** This is a theme. And so, you can do all that stuff with ultrasound. So, we believe that the fact that you can do it with ultrasound allows you to make imagery that you couldn't with the CT. And also, it's safer and you're not blasting your x-rays and stuff.

**Chris Gammell:** Yeah, there's less radiation, right?

**Gregory Charvat:** Yep. And as long as you're – there's some FDA levels and it's pretty easy to stay below those. And so, it's a cool sensor. But we found out that the cost of goods for something like that is pretty high. And then, at the time, we were talking to this professor at Stanford University, Peter Karyakob, who's essentially like the big proponent of what's called CMOS, which is a CMOS ultrasound transducer, which is – here's another buzzword for you, MEMS. You know, like the MEMS, IMU. MEMS is a buzzword.

**Chris Gammell:** Microelectrical mechanical systems. That's right. Now, MEMS is a buzzword. That was bigger like in the 90s, wasn't it?

**Gregory Charvat:** Yeah, yeah, kind of like, you know, right around the time Smashing Pumpkins was really hitting it big, this MEMS sort of popped up around the same time. Got it, yeah, yeah. But it was –

**Chris Gammell:** Yeah, they figured out they could make structures in silicon, basically.

**Gregory Charvat:** It was pre-Britney Spears, this buzzword.

**Chris Gammell:** Okay, that's good. You know, all of our time-based measurements, our time of flight through time will be based on pop culture.

**Gregory Charvat:** That's right. Now, I kind of tuned out of pop culture right around the Britney Spears time. I sort of tuned out, but I don't know.

**Chris Gammell:** You missed some things.

**Gregory Charvat:** What did I miss? What did we miss there?

**Chris Gammell:** Boy bands. Really? You know, I missed a lot of it too, Greg, I got to say. Okay, good. I don't think you missed it necessarily. Yeah, that's right.

**Gregory Charvat:** It's kind of like work. Like I missed work the other day, you know. I don't know if I – So, yeah, yeah, yeah, yeah. So, getting back to that, so we built this prototype. The cost of goods was too high. The market didn't support it. Got it.

**Chris Gammell:** And this was like a huge, like an actual installed machine. That's the idea. Yeah, we built it.

**Gregory Charvat:** We built this thing. It worked, this tomography machine. It was actually the world's fastest ultrasound tomography imager. It could image two frames per second real time, which was fast because there are other large tomography systems like ours. It was a prototype. It was racks and racks of stuff. But it wouldn't scale.

**Chris Gammell:** I remember your picture was for LinkedIn or something for a while. It was in front of racks of equipment.

**Gregory Charvat:** That was the machine we built. Yeah, yeah. It was big.

**Chris Gammell:** This is why it was confusing for me when, you know, I haven't caught up in a while, but my friend told me about this handheld thing. I'm like, I don't think Greg's working on a handheld thing.

**Gregory Charvat:** It wasn't. But what happens in these startups, as you know, they start out and they pivot. They do some pivoting, right? And that's pretty typical for all of them. And, you know, every startup I've been in has done their share of pivots. Sure. And some greater than others. But in this case, we started with that. We realized that we couldn't. It wasn't a good product market fit because the COGS was so high. So then, but at the time, we were also talking to Pierre Jakob and his thing is MEMS-based ultrasound transducer. So if you look at an ultrasound system, there are the probe that you see in the ultrasound cart. It's full of these piezoelectric transducers that are literally built with a high, like some guy or gal takes a tile, cuts these things up, and then solders, hand solders, electrodes to the end of them.

**Chris Gammell:** And it's like quartz, like high frequency.

**Gregory Charvat:** Yeah, it's high frequency quartz. To get bandwidth, they put dampening on it so they reduce the efficiency. And it's just, it's a beast, right? It's really great for 1960s technology, but it is expensive.

**Chris Gammell:** Right, but an ultrasound is just like, what, like 100 kilohertz sound wave? No, no.

**Gregory Charvat:** The medical imaging systems tend to be at like at the low end, two and a half megahertz, the high end, 10 to 15. Oh, okay.

**Speaker ?:** Oh, okay.

**Gregory Charvat:** They're higher.

**Chris Gammell:** I was going to ask about, okay, two to 15 megahertz. It's good to keep talking about frequencies with you because sometimes you jump into gigahertz, and I swear one day you're going to be talking about terahertz.

**Gregory Charvat:** Yeah, and I also like to talk about kilo megacycles. Let's not leave that out.

**Chris Gammell:** Oh, okay. That's from your ham stuff.

**Gregory Charvat:** Well, actually, no, that's from my test equipment collection because the test equipment in my lab is all like pre-1960s stuff. So it's in kilo megacycles, so it can be confusing.

**Chris Gammell:** Got it. I might switch to that. That's your boat anchor collection.

**Gregory Charvat:** Look it. Inches, mils, kilometers, millimeters, whatever. It's all the same, right? It's all the same. That's right. It's all the same.

**Chris Gammell:** Right.

**Gregory Charvat:** So, you know, we're actually, my book has mixed units of inches and meters and all that stuff. Oh, man. So don't look too carefully, but it is a mixed unit publication. So there are, anyway, this thing was a beast, but Pierre-Curie Jacob's Seamutz sounded interesting, but they were still very much in the academic world. And so Jonathan made this decision, which was a good one, which was, you know what? We're not doing this tomography stuff anymore. We're going to make an ultrasound on a chip. And everyone's like, whoa, wait a minute. And we kind of hired a team that was really well poised to make things with FPGAs and ADDs and circuit boards. Big stuff. Big stuff. Lots of power. Lots of power. We hired a bunch of people out of Chicago, actually, who were previously at Motorola. And we were going to do this thing, right? And all of a sudden, we're doing this thing on a chip. And Jonathan goes, I remember this. And I thought I was crazy at the time, but he says, Greg, don't worry about it. You'll figure it out. You'll figure it out. And I was like, really? But I was like, okay, I'm going with it. And he was right. We started to figure this thing out. And so we got Pierre on board.

**Chris Gammell:** This thing being ultrasound and also chip processing.

**Gregory Charvat:** It was MEMS and chips. Two things none of us had done before. Cool.

**Chris Gammell:** Smart people doing smart things.

**Gregory Charvat:** So we figured out, like, so I took on the MEMS stuff. We had a smaller team at the time. I took on the MEMS stuff. And the other guy, Nevada Sanchez, took on the chip stuff. And then Tyler took on the imaging stuff. And then we needed circuit board to swallow the data and compute. So our colleagues from Motorola took on that stuff. So we kind of divided it up. And, you know, my focus being on the MEMS side, because I had a background in electromagnetics, I immediately jumped on a plane to visit Pierre-Kurik Jakob because we just signed him on as a scientific advisory board member. And, you know, I took our hardware team at the time and I said, all right, we're going to read every single paper on MEMS, every single paper on CMUTs, the CMUT, the MEMS-based transducer. We're going to build a spreadsheet of dimensions and frequencies and bandwidths, right? Because we have to understand how we're going to make this chip, how we're going to dimension the physical device. And then we did all that in two weeks or so. Then I flew out to visit Pierre. And at the time I started to write this MATLAB script to compute the dimensions and then make it line up against the literature dimension. Because you want to know how much pressure you're getting, membrane thicknesses, heights, widths, all these dimensions of how you make this mechanical thing. It's really like a little electrostatic speaker is what it is. Yeah.

**Chris Gammell:** Okay.

**Gregory Charvat:** Imagine, you know, a very, you know, tens of microns diameter electrostatic speaker. That's all these things are. But it's hard to actually make that in CMOS. So, Floatup here, Kariakob's lab, we ended up just working together with them on a few things. And, you know, that was that. And we started making these things.

**Chris Gammell:** And then at the end there was a chip.

**Gregory Charvat:** Right, right. And so we ended up making some chips that started to work. And then we had some initial success with extremely low yield. But we got one or two to work. And we ended up getting, then we ended up getting like small subsets of them to work. And then we ended up starting to get images out of them. And then we ended up raising some money against that.

**Chris Gammell:** So it was pretty. But did you skip a step in here, though, where you actually talked about like what the hell's on? And how do you, so like you as the guy who's figuring out some of the MMM stuff and like, but like, does it look like, is it a circuit diagram? Like what does it look like to go from, you know, this idea? Or is it kind of building on your peers' work of like, oh, we already have some structures?

**Gregory Charvat:** Like, not to get into too much detail, but I would say, you know, it started with reading his literature, getting, you know, getting a little bit of help here and there and some advice. Then we made our own and started to gain confidence in it. And that was enough to get things started. And then what we did was we hired people who had done this before other, you know, who had experience doing this at other institutions or universities. And then we ended up, you know, then it just all the, then it became our own version of it, which was different.

**Chris Gammell:** Right, right. I guess the question for me is like, okay, so obviously this researcher had not taken it to production, right? And you, you and your team were interested in taking it to production. So like, what was the, what was the different thing there?

**Gregory Charvat:** You know, I think the different thing there, there, you know, I think part of it is, that's a great question. I think part of it is that people have tried taking this to production earlier and a lot of their approaches for making the ultrasound tend to be rather old. So they ended up putting a lot of analog parts onto a chip that, you know, have a lot of phase variants, you know, over, you know, fabric. You know, you make a dozen of them and they're all different, right? So there's a lot, you know, they're doing like late nineties ultrasound imaging approaches as opposed to modern day, like digitize everything and use digital signals. Okay. So that was one aspect of it. The other aspect was, I don't think it was as, you know, the, the, the fabrication processes available to us today are far more mature than they were 18 years ago with, with these things.

**Chris Gammell:** And I would imagine that too, is like, if you, if you're at a lab, so like Case Western where I went, we had a, we had a semiconductor processing lab. It was, you know, what, like half a, half a micron or something like that. Right. Right. And, and they had grad students that they had at their disposal and, you know, they were trying out a lot of things and that's cheaper than going to a, you know, a TSMC or a modern process. So I assume that having a little bit of money behind you allows you to tap into that, that network of, of expert advice.

**Gregory Charvat:** I think it's all of those things, quite honestly, it's, it's, it's all that, but also there's a lot of special sauce that we came up with to make these things manufacturable because it's, you know, you start with the academic paper and not just peers' papers, but other people's papers, although he's the main person in this field right now. But you, you start there, but the academics make one thing and then they do their thing with that one thing and call it a success. And that's really their role is to make that one thing and show that it's possible. Right. The output is the paper, right? Right. The output's the paper. But when you need to make something with yield, then that's a whole different story. And so the way, you know, we were looking at it as a yield, from a yield perspective, and we immediately, one of the people, we hired immediately an analog devices fellow who helped set up the MEMS fab in analog devices. Because, and that's the person who she, quite honestly, like a lot of credit belongs to her for early successes, because as electrical engineers, we can dimension the thing and say, we don't want this size and so on and so forth. But we don't know how to actually make it come up fab at work. And she did. And, and so there's, there's a lot of, you know, when you have the finances and you also have the experience, I think that Jonathan brought to the table, which is he had experience making, you know, things on a chip that were kind of similar in a lot of ways to this with like, you know, arrays of, you know, FETs and things sensors for electrochemistry.

**Chris Gammell:** And this is your, this is the co-founder, Jonathan.

**Gregory Charvat:** Yeah, yeah. He's, he's really the, the, the, he's the investor founder and sort of brainchild behind this stuff. And he's, you know, he brought a lot of experience to the table too. And, and he knew what resources to tap to make this a reality. You know, he's like, let's do this. This looks a lot like some of the other stuff I've done before. I think we can figure out the rest. And, you know, he put us in touch with consultants and, and, you know, chip designer contractors that we used for the initial prototypes and things like that, that allowed us to really accelerate the program and allow it to be at a point where you can raise money against it and say, all right, this is doable. This does work. And we have a path forward here. And that's, that's what happened. And when, and then I actually moved on to another one of those companies once we raised the money. Oh, got it. Got it.

**Chris Gammell:** Got it.

**Gregory Charvat:** And that's where Hyperfine came in. So, you know, we got the point, we got to this point where the, the, the MEMS could image things. And then we, we got to the point where we had some serious progress on the chip itself and everything was clicking. Now it's a tough problem. They spent years and years getting to the power there today. But that's where we're, we're at a happy point. And then John said, you know, I want to do, he came to me, he said, I want to do the same thing we did together with Butterfly. I want to start a new company, new lab from scratch. And we're going to do this other thing. And I want to do just that. So we had this, like, this party on his, his boat and, uh, Oh, well, okay. Yeah. Yeah.

**Chris Gammell:** Dr. Charvat here, you know, the esteemed Dr. Charvat is, uh, you know, giving tips on how to start chip companies out at sea. Right. Right.

**Gregory Charvat:** Which is what we did. But it was interesting because it was like, it was actually a work accession. So we had like IP meetings, we had tech meetings, it was a lot of work. And then finally he said at six, all right, guys, just stop working everybody. Cocktail hour. Right. Let's, uh, you know, relax. And I think we're okay. And then we kicked off the company and that's hyper fine. Although it's, I can't really speak at all about their, what they're doing. Um, I have, it's in stealth mode. I respect that. And the way he likes to roll out the companies is he likes to keep in stealth mode as well as possible. But that's another, that thing's going to be awesome when, when we, when it does go public, it's going to have a similar impact, I think. Uh, to butterfly for sure. But it's another really, and the theme that job, this company's habits, it's all medical. It's all hugely impactful. But then, you know, I was, I was happy where we started that company and, um, built the first machine in a hundred days, uh, that built the next one. And I think four or five months and then started hiring people that similar to butterfly, you know, you get people who are kind of generally good. Like I've gotten pretty broad. And then we get a couple other people who are pretty broad, can get something together working. And then as to make it better, you hire the, the, the key experts, right. Yeah. Who are really, really good at it.

**Chris Gammell:** Yeah. Well, you have funding secured at that point, right? You, so you have a prototype, which allows you to shop it around and then you get funding and then you can afford the super experts as well. And you can afford to have a team that's a hundred people because four or five of them might be supporting the expert as a tech or a, you know, an admin or whatever.

**Gregory Charvat:** Yeah, that's precisely you kind of, what you want to do with all these startups. I think what you do with these startups is you, you, you, you get, it's good to have people are generally good at first. And then like yourself, Chris, and then who can kind of do a lot of different things. And then you get it to a point where you have funding or it's clear you're going to get it. Or, um, or so some night point wherein it's worth, then you get the experts. You, you have to pay for them. They're not cheap, but you get the experts in and they make it better. You got to convince them too.

**Chris Gammell:** I think that's the other thing. It's not just convincing them with money, but you got to convince them on vision too. And it's like, you know, someone who talks a big game is a lot different when they're holding a device in their hand. They're like, let me show you. Right. Right. Especially when it's, and so I think the thing to call out here is that these are pretty high tech startups. I mean, this is not just like slapping something on a web server. This is, you know, this is some serious science. Yeah. This is great.

**Gregory Charvat:** This is not, you know, that's, I think, I, I think that quite honestly, as a good expert with Jonathan, I learned a lot. He was, um, he was a mentor in a lot of ways. And I, I, I, I feel like that's a good bootcamp. So like, you know, if you, that's one advantage of working with a very, you know, people are really aggressive like that is you're going to learn a lot fast and apply to your next company, your next venture. But yeah, it's, these are all hard, hard problems.

**Chris Gammell:** You're going to, you're going to be feeling it at one in the morning when you're stressed out, but you're also going to learn a lot, right?

**Gregory Charvat:** Yeah, you will. And I think my recommendation for that is, you know, you need to get into sort of exercise routine, whether it's a half hour walk a day or something to burn it off because. You know, there's no point in stressing yourself out. There's always going to be some challenge. You just, you get used to it. It's like you get acclimated.

**Chris Gammell:** You know, that's the thing that I've been talking about recently with some friends. It's just like the, you know, sticking, like understanding when to stick with it is kind of like the hard thing. But like people who are really good almost always stick with it and they, they know when to bail. Sure. Right. But like you need to kind of wait through the pain.

**Gregory Charvat:** I think the bailing thing is tough. I don't, you know, every one of these, every company startup you get involved with is going to have some down, some bad things go down. You know what I mean? Sure. There's always some tough times. And right.

**Chris Gammell:** And that's the waiting through it. I think, you know, you got to understand that there's some stuff there.

**Gregory Charvat:** Yeah, exactly. There's always some crap that you have to work through because it's a pressure cooker. Everyone's under the gun. And the worst behavior, it will come out. And, and you have to acknowledge that you have some bad behavior yourself you're bringing to the table.

**Chris Gammell:** And I don't, I don't, Greg. Sorry.

**Gregory Charvat:** Oh, that's right. No, no, no, no. Yeah. Perfect. Yeah. I'm definitely not human. I'm sure people who work with me will, yeah, say the same thing.

**Chris Gammell:** Oh, we're getting to that. We're getting to that. I met some of your coworkers yesterday.

**Gregory Charvat:** Awesome. Oh, boy. Oh, boy. Yeah. Oh, boy. It's, it's interesting. It's, I don't know. It's an interesting experience. I do think that some of it can be smoother than others. I, I think some teams work better than others, naturally. I think that there's like, I do, I do believe that there's a hiring strategy that I've learned over the years with these. I've been doing startup stuff now for seven years. And I think I've actually learned, you know, there's sort of an optimum way to hire to be careful. You got to watch out. You don't want to hire people with the big egos. That always causes chaos. You got to get.

**Chris Gammell:** Yep. Yeah.

**Gregory Charvat:** You just see people, team players who are willing to be aggressive. You want people who are not so analytical. You want people who just can take one data point, decide and go. Because it actually costs more money in a startup to, to think about things and analyze them than it does to go. So it typically costs more to think about it and wait another week or whatever than it does to just go. Because you got to think about your burn rate, you know, your, your, your salaries, your burn rate, your fixed costs are just, it's costing you X number of dollars per month per week. And, you know.

**Chris Gammell:** So you're just saying like, because the iterate, because you're assuming the iterative approach and you're going to rework things. Is that kind of it? I mean, you're not saying like throw caution to the wind and just try anything. You're saying that once you have figured out that first path, try something, then bounce back and bounce, bounce, bounce. It's like a serpentine between ideas.

**Gregory Charvat:** I think what you want to do is you pick the easiest one. That's the highest probability of success. And, and you go and you rely on your experience to make the call and whatever data you happen to have at the moment and just call the shot and just go. Because.

**Chris Gammell:** Yeah.

**Gregory Charvat:** You're not going to get better. I mean, sure. You make a 10% better information, but you may, you'll spend a week doing that. And if you're burning a million dollars a month, which is a pretty typical burn rate of a startup, uh, $250,000 for a week of consideration is the money.

**Chris Gammell:** Right. Right. And if the prototype costs even $20,000, you've, you know, and you're doing some active work on that. Yeah, exactly. It's cheaper. Like it really, like it's crazy.

**Gregory Charvat:** It's what you want to see when you're running these teams and programs, which I've been doing like that's, I ran teams and the programs with Jonathan. I ran the team, the hardware team at butterfly. I ran, um, the hardware team at, you know, hyperfine as well. And I, I do the same at, um, at, uh, humatics. I kind of, I run hardware.

**Chris Gammell:** Are you forgetting the names at this point that you talk a pause there? I'm just saying, you know, you've done enough startups.

**Gregory Charvat:** Starting to forget the names. Exactly.

**Chris Gammell:** At least, at least on these startups, these are actually like regular names. I mean, like, you know, at least it's not like Cluesy.

**Gregory Charvat:** Oh yeah. Well, phone, we're not making phone apps here, man. That's, uh.

**Chris Gammell:** Yeah, right. Right.

**Gregory Charvat:** Wait a minute. Now let's talk about this for a sec.

**Chris Gammell:** Oh yeah. We, we kind of got into this right before the show started. Huh?

**Gregory Charvat:** There's a, listen, I think we have a problem in society right here, right now. Okay.

**Chris Gammell:** And I'm speaking to. A quick break from the actual tech talk to talk about tech.

**Gregory Charvat:** Let's talk about technology. Okay. So what amp hour listeners, right? Hardware people, right? Are most of them hardware? Most of us are hardware people.

**Chris Gammell:** I think hardware interested at least if they're, you know, if you're, if you're listening to this and you're not at least interested in hardware, you're going to, you're going to have, you're going to have a bad time probably. Yeah. Yeah, exactly.

**Gregory Charvat:** Everyone here can pick up a solder or a guy here and we know what a transistor is and all that stuff. Okay.

**Chris Gammell:** So, or, well, no, we don't want to be exclusive there, but at least they're interested in doing so. Right. You know, like, so.

**Gregory Charvat:** So, okay. Let's think about what technology is. I think the word technology, Chris, we need to take it back. Okay. Okay. It has been hijacked by the software and IT and phone app community. They've hijacked it. Oh, I know. They've hijacked it. It's a travesty. The easy way to see this is to. They don't make anything. There's no circuit boards over there. There's no LEDs. There's, it's, listen. When, when the archeologists 10,000 years from now dig up the landfills and they look, you know what they're.

**Chris Gammell:** Back to the landfills. Real landfills. They're going to find my trash. They're not going to find. They're not going to find my shitty PCBs.

**Gregory Charvat:** They're not going to find software down there.

**Chris Gammell:** They're going to find my leaded, whatever.

**Gregory Charvat:** They're not going to find Facebook down there. They're going to find CRTs and circuit boards and things full of lead and stuff. That's a good thing, right?

**Chris Gammell:** I'm not sure that's a great point. I got to say.

**Gregory Charvat:** Well, I guess it's not a good. Well, look, it's not a good thing for drinking water. That's for sure. We can, we can get that off the table. It's no question about it.

**Chris Gammell:** You're just talking about substance and world changing type things.

**Gregory Charvat:** It's a good thing for history, though, to find those leaded circuit boards that the technologists made, the real technologists, the people who make stuff, right?

**Chris Gammell:** I think you're talking about, yeah, the substance of atoms versus bits, right? And I think, unfortunately, the thing, so like my example for when people talk about like, oh, I'm into tech and I go, well, wait a second. Oh, like, like. Could you please define that? And they're like, well, I like, I like getting new phones and I like apps and it's like, oh, okay. That's just a different thing in my mind. And I think what you're saying too is like, that's just a different word to them versus you.

**Gregory Charvat:** I think that we need to take the word back. I don't think they should own that word anymore. I think it should just be the exclusive club. Well, there's just more people there. Okay.

**Chris Gammell:** Well, maybe we just, maybe we just make our own word.

**Gregory Charvat:** I think we need to make a word up for them. I don't think that's how it works. Because the word technology, it kind of started actually around the civil war.

**Chris Gammell:** I did not know that.

**Gregory Charvat:** It was, it was actually, it revolved around the ship, the monitor. And that's, that was really the first time the word technology was used.

**Chris Gammell:** I mean, what if people like are in, who are into like, you know, war history and guns were like, well, we want to take this word back. All these electro weenies are, you know, they're talking about resistors and soldering irons when we're talking about bullets and barrels.

**Gregory Charvat:** If those people want to take it back, I don't think we can stop them, Chris.

**Chris Gammell:** I don't know, Greg. Circuit boards aren't bolt proof. Like, there's not much we can do about it. Are you, are you working on any like Tony Stark-esque, you know, weapon technology? No, no.

**Gregory Charvat:** I, I used to do that stuff on Lincoln Lab, but not anymore. We worked on sensors back then.

**Chris Gammell:** Yeah. I was going to say that's the seeing through the walls radar. Yeah. Yeah.

**Gregory Charvat:** And that thing, you know, that's, it worked beautifully. But yeah, it's, that's how we work on these days.

**Chris Gammell:** Okay.

**Gregory Charvat:** That's how we work. But it's, it's good stuff. You know, it's made for a reason and you know, there's, there's, there's honorable people doing stuff off that field. And yeah, that stuff's pretty cool. I think, I think, I think it's good to do a tour in defense because they are literally making the, I quite honestly, they're making the cutting edge stuff because they sort of have a limited budget. Nation states have a limited budget. I mean, I'm not sure they're always intentionally unlimited, but I mean, you know, the $1 trillion F35 program is a pretty big budget. That's the largest program ever.

**Chris Gammell:** Oh yeah, that's a big hot mess. Yeah. Yeah.

**Gregory Charvat:** Big program. I mean, it's, geez, that's a lot. That's a lot of money. Yes, it is.

**Chris Gammell:** Well, that's interesting because a lot of that stuff, a lot of the, I was walking on IMTS yesterday. So that's where all this stuff came from. And I was actually, I was there with the Bolt folks and I was there with Mike Stish from Hackaday and, and John Bruner and a couple of the people that we saw. And what we were talking about, like the, how the military and the, the defense industry kind of funds a lot of that, like big tech, like you were talking about. Yes. Yes. And then as we were talking about that, Mike, Mike from Hackaday was saying like, Hey, I just heard from Greg and I think he's here. And I'm like, no way I'll give him a call. And so I called you, Greg. And I was like, Hey, are you here at IMTS? And you went, Nope, Nope. But my coworkers are. And, uh, Humanix was there. And so I got to go see what you're working on. So maybe this is a good way to kind of segue into talking about what are you working on these days? This is public. This is public. Helpful to talk about it.

**Gregory Charvat:** Yeah. We, well, you know, the thing is like, our, this, this one is, this is really cool. So this is another very, very difficult problem that we've taken on to it. It, it, it is tough, but we've, we've nailed it. Now, basically what happened was, uh, while I was working on, um, Hyperfine and having fun with that company, uh, this, you know, people would reach out to me all the time with startup ideas and things like that after my, especially after my book, uh, was published. And, you know, I, I reply to folks and, you know, I replied almost everyone writes me and, but, um, this one professor from MIT wrote me and, and he's an interesting guy because he wrote a book that I'm a big fan, which is a book, this book called digital Apollo, which is about, uh, the, the, the digital real-time flight control system in Apollo. You know, the Apollo flew to the moon, the computer was flying, the computer was, uh, flying the stick and the thrusters the whole time, which is, it was actually the world's first fly-by-wire aircraft was Apollo, which is kind of interesting to think about. Yeah. Yeah. And it was funny because the first fly-by-wire aircraft was the hardest thing we've ever done in aviation. Like the hardest thing humanity has ever done. At least it was low stakes, right? Yeah. Exactly. Uh, uh, funny thing is actually going to, uh, I'm going to meet, um, I might meet Al, uh, Al Warden, uh, this weekend who, who was flying the fan module on Apollo 15. So it's a funny, it's like, at a dinner party, we'll hang out with them at talk shop. It'll be fun.

**Chris Gammell:** Boats, boats and, uh, astronaut dinner parties. It's good. It's good time. So Greg live in the hard life. This is like Greg's commercial for, he's like, you know what? If you write a book, sometimes you get to hang out with astronauts. You do.

**Gregory Charvat:** You do. I think you could write a really cool book. I think you could take, take what you've done with contextual electronics and take the turn into a book. And I think it would be awesome.

**Chris Gammell:** Maybe, maybe not.

**Gregory Charvat:** So, uh, anyway, so, so basically this guy, uh, David Medell, he wrote me, he said, I, Hey, uh, I'm reading your book and I want to like, I wonder if I could do this thing. He goes, I try to, I want to see if I can make a, um, like a, a short range, super high, precise GPS with microwaves. Uh, can you like, what do you think about that? So I wrote him and I said, that should be a piece of cake. And, uh, Oh boy. That's how it, that's how. Okay.

**Chris Gammell:** Yeah.

**Gregory Charvat:** Everything's doable. It's just a matter of time and money. And, and, and, and this, you're not, we're not breaking the laws of physics here. No one's breaking the laws of physics. So, so I said, all right, piece of cake. Um, then he said, Oh, well, can I come down and visit you? Let's talk about it. So, uh, so I had him over on my sailboat and we spent the afternoon on my boat talking about this.

**Chris Gammell:** Yep.

**Gregory Charvat:** And, um, and, and so he told me this story about how he was actually, he worked for Bob Ballard. Um, do you know who that is? He's.

**Chris Gammell:** I don't know.

**Gregory Charvat:** It sounds familiar though. The Bob Ballard is the, is the person who've discovered the Titanic shipwreck.

**Chris Gammell:** Oh, okay.

**Gregory Charvat:** He is on TV all the time and on national geographic and all that sort of thing. He's, he's the most famous oceanographer in the world today.

**Chris Gammell:** Jacques Cousteau.

**Gregory Charvat:** Yes, exactly. He, he literally like Jacques kind of took the reins of Jacques Cousteau and he has his own exploration ship. Nice. Uh, you can actually watch it live on YouTube.

**Chris Gammell:** Don't forget Steve Zissou.

**Gregory Charvat:** That's right. Of course. Bob, though, is an interesting guy. He's, um, his thing, you know, his theme at, well, he's at Woodshall Oceanographic Institute was, he was like, I want to make undersea remote controlled robots to do the nasty work, to do the mapping, to go really deep. Because at that time they had this submersible Alvin, which was a man.

**Chris Gammell:** I remember Alvin. I remember that was in my books growing up.

**Gregory Charvat:** Yeah. Alvin's still around. And actually they recently upgraded Alvin's, um, uh, the, the titanium sphere that you, you, you live in when you go down and you, Alvin. Yep. And our chief roboticist, pneumatics, uh, designed and wrote all navigation software on Alvin when it was updated recently. So, um, his life, your life is in his hands, whoever is diving on Alvin right now.

**Chris Gammell:** And, uh, but it's, it's anyway, so Bob, I should mention too, uh, I forget his name. I, I, I will definitely look at it, but, uh, one of the people who worked on some deep, deep dive electronic stuff, gave a talk at, um, at the supply frame meetup I used to do. And, um, that is a fascinating field. Like stuff I just never thought about, like compressing capacitors. Like what happens when a capacitor goes down super deep and experiences tons of pressure?

**Gregory Charvat:** It's like, Oh, it blows up. It implodes. It just, boom. Yeah.

**Chris Gammell:** I mean, like you have to have tons and tons of different considerations for high pressure situations like that, that I never thought of.

**Gregory Charvat:** Yeah. Yeah. There's a couple of approaches. One is you put it in a pressure vessel and in which case it can be an atmospheric, uh, pressure. Or the other thing is you could fill with oil and let it be the same pressure as the outside as, as the water. And so the hard part is you need to examine and test the parts you use because if there's a bubble in a, let's say a potted chip or something, that chip will implode. Yeah. And take with it, everything around it will get. That's right. Yeah. It's like a, it's like a, like a, like a large, like an M80 going off on that circuit board basically. Right.

**Chris Gammell:** Um, and so Nick Bingham, by the way, that's who it was.

**Gregory Charvat:** It sounds familiar. Cause I've met a lot of the Woods Hole people because of these connections with this company. And right. Yep. Okay. And, uh, there's, there's a really cool, um, there's some really neat, um, symposiums they have on robotics. The center for Marine robotics is a great conference to go to. In fact, if you, that would be a really fricking cool thing for someone to hack a day to cover is to go to the center for Marine robotics conference. Yeah. Yeah. Yeah. Cause the talks are, it's just like, you're like, wow. And it, I, I actually gave a talk there, um, a couple of years ago about short range radar and, and there's interest there too, because, uh, it's hard to find these things when they recover them, especially when the weather's nasty or it's pitch black. Anyway, that's a whole different story, but, uh, it's, it's, um, yeah, it's a whole different. I mean, I honestly got like if, if, if we, if, if there's a break between stars for me, I'd love to just voluntarily go on a cruise at Woods Hall just to, to experience it, you know, and it would be cool. But, um, anyway, that's, that place is amazing if you had a chance to see it, but yeah, Bob was there, found the Titanic and, um, on Navy money, I believe he, he, he like had some extra boat ship time left over and decided to take a look for the Titanic and found it. And, uh, that guy's, he's a wild, he's very aggressive, wild man is super interesting person. And, um, his theme, his career is his theme, his career is to use remote control robot robotics, not unlike how we use the Mars rovers today. We control them remotely in the ocean.

**Chris Gammell:** You could have more real asynchronous too, right? You have to, yeah, because of transmit times and everything, right?

**Gregory Charvat:** Yeah. Yeah. But you don't have that problem with, when they're in the ocean, cause you could communicate with them, but bandwidth connections are limited. And so there's, there's pieces of full autonomy, pieces of semi autonomy that you use depending on what your mission is or what phase of the mission you're in. And Bob just gets that. He understood that in 1984 and before anyone did. And there are actually, there's some really, there's a cool, the cover of National Geographic, I believe it's from 84, wherein there's this image of a robot, 6,000 meters below the ocean surface with a cable going up to a control ship. The control ship has a satellite dish beaming signals to a geostationary satellite beaming them back down to Woods Hole. And that was his vision, which he couldn't do in 1984, but he does it today. He actually implemented it today at the University of Rhode Island at his institute there. And it's called Nautilus Live. And you can actually Google that and watch their missions in real time. You actually get the same feed that Bob gets in his control room at URI, including the audio.

**Chris Gammell:** I was going to say, is this just, is this laziness? He's like, I hate boats.

**Gregory Charvat:** No, no, it's more like, it's interesting. What he did was he took like the PhD level oceanographers and historians and all these people, and he got them off the boat. They don't need to be on the boat.

**Chris Gammell:** He's like, they are wimps. Yes, they're wimps.

**Gregory Charvat:** Well, he's using them for their brains to think about what's going on. And then he may have some scientists on the boat, but usually not. But he has a super experienced crew that's laser focused on gig this equipment out in the water and back on and so on and so forth.

**Chris Gammell:** Fewer people puking over the edge, huh?

**Gregory Charvat:** No, yeah, that's exactly it. Fewer people puking, less money, less risk. Plus, you throw a scientist out there for three months or six week crews, they're not getting work done that they need to do. They're kind of hanging out. That's a good point. You know what I mean?

**Chris Gammell:** Yeah, right, right, right. So it's efficiency.

**Gregory Charvat:** You just need them for when now the remote vehicle is getting on station. That's when you need them to tune in, right? And so there's a lot to be gained. But when they're not tuned into that, they could be writing papers about what's going on. They could be doing other work. Like, it is just an efficiency. And it benefits humanity to have that efficiency. And so what he's done there is that he's finally implemented that vision. And it's kind of cool to hang out in his control room at URI and watch what's going on. And actually, if you look at his YouTube feed, you get the exact same feed. Put it on your big screen at home at Truffle Lights.

**Chris Gammell:** That's awesome.

**Gregory Charvat:** It's the same as his control room.

**Chris Gammell:** See, now there's a Saturday night.

**Gregory Charvat:** That is. Quite honestly, I actually leave it on in the background when I work because I find it interesting. And they actually dive on like World War II shipwrecks and all kinds of stuff.

**Chris Gammell:** Oh, man. That is super cool.

**Gregory Charvat:** It is really cool. Like, you are seeing what everyone else is seeing for the first time. So it's...

**Chris Gammell:** And that's called Nautilus Live?

**Gregory Charvat:** Nautilus Live. Yeah, yeah. Your listeners should check it out. It's kind of... It's beyond... It's actually really a cool thing. So Bob's involved in our company. But they... So Bob had one... Here's one of the problems Bob ran into in working on his robots for the first time, his underwater robots, is that he couldn't navigate these things very easily. But when you're above the waves, you have GPS, right? And no problem, navigation.

**Chris Gammell:** But... General triangulation type stuff.

**Gregory Charvat:** But when you're under the ocean, obviously, you know, GPS signals, microwave signals are not going to penetrate the ocean. So especially... They're not going to get more than a few millimeters into the water. Okay. Now, they actually need navigation when they're, you know, surveying a shipwreck, right? Sure. How do you navigate down there? Aside from using active sonar imaging and navigating off of the blobs on your sonar, which is what they would initially do.

**Chris Gammell:** I'd imagine if you could drop like a stationary point on the bottom of the ocean, you know, if you could actually tether it, but there's not actually anything stationary in the ocean. That's the problem, right?

**Gregory Charvat:** No, exactly. So what they did was they... So Bob, working with the other founder of this company, David Mendel, created from scratch, they built from scratch using like Motorola DSP chips and stuff back then. This thing, it's an acoustic-based navigation system where you drop by anchor a series of buoys and the buoys and then you've got a sounder on the host ship and then you've got a special sounder on the ROV, on the vehicle, on the robot. And they all can ping, transmit and receive, so they all ping against each other. And because they can all range to each other, they can solve the matrix of equations that give you absolute position of the ROV, of the robot or the vehicle that's being piloted, like Alvin.

**Chris Gammell:** So is the pinger, the main ship that's sending out the base signal, is that because that's also GPS? That one is GPS. Yeah.

**Gregory Charvat:** And then the ones at the bottom are a local navigation network that are tethered to the bottom via anchors. And then the ones in the bottom make up a local network. They actually know the time of flight between each other. Then they ping the ship. The ship knows its position vis-a-vis GPS.

**Chris Gammell:** Yeah.

**Gregory Charvat:** And so now we know exactly where the network is under sea relative to GPS, which is really good.

**Chris Gammell:** I mean, these absolute positioning problems are, it's just anything in free space really, right? And water really does bring you into free space because you have that third dimension that's a very critical thing.

**Gregory Charvat:** Exactly. And so now you can navigate the vehicle. And so once you can navigate the vehicle, now it opens up a world of possibilities you couldn't do before. So what they did, they did some really crazy things. So first thing they did was they started taking photo mosaics of shipwrecks. So you know those photos, you've seen those photo mosaics.

**Chris Gammell:** Yeah, it's like a photo sphere that people have on their phone. That's from a center point where everybody goes and takes pictures around them. And now you flip that script and you take pictures around the thing.

**Gregory Charvat:** Now imagine it's 1994. You're going back to the Titanic and you have your 35 millimeter camera and a pressure vessel. And you use this high precision nav to trigger the shutter. Okay. And now you can get a perfect photo mosaic where they all overlap just right for the first time ever. And now you get a really good picture of what's going on. So they did stuff like that.

**Chris Gammell:** You could edge match before, but if you had like depth differences, you don't know where you are in free space. You're in trouble. And you don't know how to adjust the photo. Like you, everything's just kind of a guess, right?

**Gregory Charvat:** Exactly. But now you can actually use the control system navigating the vehicle to keep perfect depth to within a centimeter. And then you can make sure that you trigger that shutter so that the overlap is, you know, exactly a meter and a half on every single image. And then the mosaic just is perfect, right? It comes out perfect. And so that's one thing they did. The other thing they did, which was very interesting, it's more abstract, is that, you know, Bob was the one who discovered these high pressure, high temperature fissures. You know, we have these tectonic plates that divide up the surface of our planet. And the theory for a long time that on the boundary layers at the edge where these tectonic plates meet in the ocean, there must be places where it's spewing super hot water and minerals and maybe even lava and other stuff.

**Chris Gammell:** Like volcanoes, basically, or like the San Andreas Fault, right? That's a big...

**Speaker ?:** Yes.

**Gregory Charvat:** There should be a San Andreas Fault. And on that fault, under the ocean, there should be spots where there's these super hot springs. Okay? Okay?

**Chris Gammell:** Yeah.

**Gregory Charvat:** And... But no one ever found these things. But Bob Ballard found them for the first time. And he finds these things.

**Chris Gammell:** That'll get you on the cover of National Geographic. That's for sure. Yes.

**Gregory Charvat:** For the umpteenth time, he finds these things, right? And then what did... Now, what they found was astounding, which was the astounding thing that no one ever expected was that they were teeming with life.

**Chris Gammell:** Yeah. Okay. The sulfur-based crabs that are down there, like those transparent crabs and everything.

**Gregory Charvat:** Crabs, worms, corals, you know, like fish, like all kinds of fauna. You name it. It's there.

**Chris Gammell:** Life finds a way.

**Gregory Charvat:** It found a way. But the funny thing is between... Normally, at the bottom of the ocean, there's not a lot of life, much at all. But at the fissure, there's tons of it, right? A huge amount of shocking amount of...

**Chris Gammell:** It's the reverse oasis, right?

**Gregory Charvat:** It is, yes. It's pitch black. There's no photosynthesis happening. No, nothing. And so that was shocking. And so what else is happening around these fissures? So what they did was they instrumented an ROV with this pinging system, this high-precision nav, and they used to do something very unique. There's this plume of like black... It looks like smoke. It's not smoke. It's like full of rare earth metals and chemicals and all kinds of weird stuff. And what they want to do is find out like what is in that plume? What does a plume look like in 3D space? What is the shape of that plume? Where does the plume fall? How does it interact with ocean currents? So what they did was they took the ROV with the high-precision location, and they made a 3D map by raster scanning it like an old dot matrix printer. Raster scan it, next page, which raster scan... And imagine you raster scan a page, and the next page is the next depth. You go up to like 10 meters higher now, do it again, and 10 meters off higher, do it.

**Chris Gammell:** That is a thankless job right there. Right.

**Gregory Charvat:** And no humans wants to steer that manually in ROV, which is what you'd have to do before this technology was available. Well, the other thing I think about is... So that's what they did.

**Chris Gammell:** Like I said, the ocean currents are just moving you. I mean, that is just... There is a constant thing. You are always moving because of the flow of the water.

**Gregory Charvat:** So you want a map of this thing. So they actually used this technology to make a 3D image and a map. And in that map, each pixel, each voxel in the 3D image was the chemical composition. So each voxel was like, at this voxel, this is what was here chemically, and by how much of a quantity. So you had this multifaceted voxel map of what was coming out of those things, which was staggering to see in the 90s. Right. So that was one of the things they did with this tech. So David's on my boat. He's explaining all this crazy stuff to me. And meanwhile, I'm a really terrible listener. So I start daydreaming about how we could build this thing. Right. I'm like, yeah, I'm convinced.

**Chris Gammell:** Engineers always go straight to the implementation. All right.

**Gregory Charvat:** I'm like, okay, blah, blah, blah. All right. This is cool. Okay. So then we start... I tell them, I think I'm totally confident we could do this. Um, and you know, we talk about... No, we don't get into details.

**Chris Gammell:** I don't know if I've ever said it on the show, but whenever an engineer... And you know, I'm an engineer, right? Right, right. But whenever another engineer says, oh, that's easy, my ears always perk up. Because it's like, that's like a downsampling of total considerations. And I told this to my girlfriend, and she said, you know, you said that to me the other day. And I'm like, oh, yeah. So it's just like an engineer thing. Okay.

**Gregory Charvat:** Well, I think easy to us means... It's feasible.

**Chris Gammell:** Easy to think about. It's feasible. That's the real word. And that we say easy, but it means that I can at least think through the steps.

**Gregory Charvat:** It may mean we need to spend $60 million in four years. Exactly. But it means it's tangible. It's feasible. We should be able to do this.

**Chris Gammell:** And... I can think of a way to possibly do it.

**Gregory Charvat:** Yeah.

**Chris Gammell:** So anyways.

**Gregory Charvat:** And so you did that. We did that. And... But I mean, David understands this. And so we did that, came up with an idea for the company and a technology pipeline. And so he took that back. And then he found a business attorney guy. Because you need a business person. Because as engineers and technology people, we have to... We should be honest with ourselves what we're good at and what we're not good at. And you always need a very good business person to help you set the company up, to help you find the market. The legal piece. Do the legal piece. There's a lot there. Yep. So he found that person. Yep. And that's the person that will raise the money as well and do very, very high value stuff. And that's a lot of work. So he found this other guy, Gary Cohen, who's great. Who's been raising all the money for us and keeping all that, the ship on the right course and helping us get to the market, the right market for our stuff as well. So we found that. We got this. And then... So that was really our initial... And then there's another fellow at Woods Hole. It's got James Kinsey, who wrote the software to navigate Alvin and many other things. We got him because... Like, I'm a censors person, but I'm not going to understand how the heck this thing's going to hook up to a robot that is equally as difficult. And so we got him. So there's the four of us and kicked off this company together. And initially, the plan was... There's this time domain corporation, which basically pioneered what's known as ultra-wideband. They've been around for over 20 years. They were for sale. And our initial plan was, let's raise some capital to buy them. We will, with our backgrounds in robotics and our backgrounds in radar, we will find... And our Rolodexes, which, you know, with David Medell and his background, everyone loves him. He's a wonderful man. He has this wonderful golden Rolodex being at MIT all these years. We'll...

**Chris Gammell:** Yeah, that does help. That sure don't hurt with...

**Gregory Charvat:** We will find this application.

**Chris Gammell:** I mean, finding some normals on that list might be kind of weird, but, you know... We're going to take... He's like, can't find a plumber, but, you know, if you need someone to do, you know, high-speed radar type stuff, you know, that kind of guy.

**Gregory Charvat:** Let's talk to... Call Bob. Let's see what he thinks. Bob Ballard and all these people and these astronauts also. So, we're like, all right, we're going to buy these guys. They'll be part of our team. And they've got some awesome technology. And together, we're going to find the markets and we're going to incrementally approve it. It could be approved. And we spent some time. We flew down there. David's playing. He's a private pilot to check to talk to them. And so, we made an offer. Another company was also offering. And we lost the bid to buy them. And we stepped up and lost the bid.

**Chris Gammell:** Oh, man.

**Gregory Charvat:** And so, we're like, uh-oh.

**Chris Gammell:** So, you also showed your hand. Yeah. Okay. Uh-oh.

**Gregory Charvat:** So, it's like those 80s movies where the record stops. It's like... Now, what do we do? So, then everyone looks to me and says, well, Greg, this is December 2015, right? Like a month after joining the company. And I'm saying, Greg, can you make something that's better than their stuff? Can you make something? Let's make... Now, we have to make something from scratch.

**Chris Gammell:** So, I went back out on a boat and thought about it. Right.

**Gregory Charvat:** So, I'm like, all right, fine. I'll make something. So, I go back to my lab. And I spend like four months. And then we build this... We build our first prototype. And we demo it at this thing called Amazon... At Mars. Which was a machine and robotics symposium that Jeff Bezos sponsored out of his own pocket. And he puts on every year at Palm Springs. And this was the very first Mars conference. Jeff asked David if we would demo our product at Mars.

**Chris Gammell:** Jeff Bezos. Jeff Bezos. Yeah. Jeff Bezos asked your co-founder if you could demo your prototype at a brand new conference. Yes.

**Gregory Charvat:** Which we didn't have, by the way.

**Chris Gammell:** Is this after they bought Kiva? Is that why they did the Mars thing? Yeah. Yeah.

**Gregory Charvat:** Because the Kiva people were telling Bezos and his people about us. And our vision. Ah, okay. Which was to locate robots.

**Chris Gammell:** So like Kiva Robotics. If people don't remember, Kiva Robotics was the... It's like the really low squat robots that basically pick up shelves and then move them towards people. So like Amazon bought them because obviously they do tons of warehouse stuff. Yeah.

**Gregory Charvat:** Yeah. Exactly.

**Chris Gammell:** And this will become relevant, I'm guessing, to the conversation.

**Gregory Charvat:** Yeah. So those guys were excited. A lot of people were excited about Humax because our vision is to locate robots just like David and Bob did under the ocean. And so they're like, can we show, can we demo your thing? And this is right when we lost the bid to buy Time Domain. And we're like, yeah, sure. So I go back to my lab and connect it and bake the thing from scratch. Of course. Now we're going to demo. And then we get it working. And we... Let me just pause and say, you have been busy, Greg. Yeah. Yeah. Hey, look, no risk, no reward, no pain, no gain. Yeah. It was crazy. So we built this thing, right? And like, you know, it was really brutal. And we get it done. My second daughter was born during this time while we're building this thing.

**Chris Gammell:** I was also going to say, yeah, you've been having a couple of kids too. And like, you know, yeah.

**Gregory Charvat:** I've got a wonderful wife. And she's very supportive of the entrepreneurship. Her criteria is that she wants to stay in her nice little town of Kielford, Connecticut. And so that's what I do. I stay here as home base. But otherwise, she'll go crazy and do it. So spouse, you mentioned you have a new significant other, Chris. This is something that you have to find that mutual understanding that they have to accept the piles of all the soloscopes and junk for one thing. Oh, yeah. Which comes with all electrical engineers. Obviously, Dave Jones, his wife is very accepting. Yep. Mine is too. I have lots of piles of junk. And I'm sure yours must be or she must be getting acclimated to it at a minimum. This is a key thing. All listeners must go through this, I would think. Those of us who are married or inevitably will be. It is a thing. Anyway.

**Chris Gammell:** It's an important partnership. How about that? It is your most important partnership, maybe followed second by your co-founder type thing, right? Yeah. And often that startups are talked about like marriages. So finding good people to work with.

**Gregory Charvat:** They are. But here's the thing when you have piles of junk, just as a side. When you buy some big piece of junk on eBay, you can always like, you got to line up the shin of that when your wife's not here. That's part of it. You don't want her to see all the junk coming in. Just a small sample of it. Like if she only sees one in five old oscilloscopes or radios or whatever the hell it is come in, that's okay. But don't let her see other ones coming in. Especially if a delivery truck shows up and there's a pallet of crap. That's the one you don't want her to see. Anyway. Just piece of advice. That's the spot we can't. I think all the married folks here, men and women both, will agree that that's probably good advice.

**Chris Gammell:** Right. It is our curse to have more stuff. My curse is I was just moving. But as a quick anecdote, because I really want to hear about what's going on here. One of the guys at the meetup that we just had the other night, he was telling me he used to work at a company that did amplifiers that sold to ham radio. Oh, yeah. That sold for $10,000. Oh, my God. He said the guys would show up with piles of $10,000 in cash because they'd be scrolling away money over the years and they didn't want their significant others to know about it.

**Gregory Charvat:** Of course. $10,000 is a lot of cash. That's a big money right there.

**Chris Gammell:** Yeah, that's quite the stash thing.

**Gregory Charvat:** Some of the ham guys and gals will throw the money down on stuff. I'm a little more frugal as a ham. I like to bake myself from scratch because I just like the experience of making it.

**Chris Gammell:** Yeah, and you get in there, you understand how it works and everything. Okay, so speaking of piles of money, Jeff Bezos. Jeff, yes.

**Gregory Charvat:** So Jeff's like, I want these guys at the conference, blah, blah, blah. So we don't have a prototype. So I go back to my garage at Guilford. I build it over the next four months. I build the hardware. I get to work in MATLAB. And then James Kinsey from Woods Hole was helping us moonlighting. And he comes in and develops the nav software for this thing. And we have it done by mid-March. We ship it out there. And Bezos pulls up the red carpet, paid for all the shipping, for everything. It was unbelievable.

**Chris Gammell:** That's the red carpet, huh? You hang out on boats with astronauts. And the red carpet is Jeff Bezos giving you his UPS number. Yes, exactly. No, no.

**Gregory Charvat:** He's actually sent a courier service to get everything.

**Chris Gammell:** You know, this is still a low bar to jump over for the World Purchase Man. Well, there's more. I'm just saying, Greg, you're letting them off. I am.

**Gregory Charvat:** I'm sure Jeff is a – He had an open bar everywhere, which was really nice too. Got it. Got it. Got it. Got it. Got it. And so then there's a talk we had to give, right? So David Vindell gave the talk. And he's an MIT professor, so he's, like, good at this. He's damn good at these talks. So he gives the talk. And we do a live demo of the machine. And we demo it. And it works. And actually, like, the theme of the conference was Jeff wanted every single demo. He wanted a talk and a demo of something. And our demo was the only one that worked.

**Chris Gammell:** Hey, hey. All right. That's a good sound. Yeah.

**Gregory Charvat:** That was kind of nice. Ways to stand out. We stood out. We worked. And we had the only question that he asked, at least in our session, was how does it work? And, of course, that's the one thing we can't necessarily answer in detail. But –

**Chris Gammell:** Well, I think you do have to say a little bit here, at least what it is, because you don't have to tell us how it works. Of course not. But we'll talk about what it is. I think radar. It's a high-precision – It's not a radar.

**Gregory Charvat:** It's actually –

**Chris Gammell:** I'm just saying, you know, with you, Greg, it's always something. It's always something.

**Gregory Charvat:** It's a short-range, high-precision GPS is what it is. Okay. That's a good way to say it. We have the IMTS on our phone, and it's invaluable now, the 21st century.

**Chris Gammell:** Now, I get to see both of these at IMTS. You guys are – There's two of them. Two flavors, yes. I have to say your wording on it is very confusing, because the one you just released was the centimeter-based system. Yep. And then you also have a millimeter-based system. But that refers to the accuracy, correct? Not the wavelength.

**Gregory Charvat:** Exactly. Yes. That's the precision, actually.

**Chris Gammell:** That naming is very bad. I know. We have to figure out – Yeah, we're doing our best, but like – Because you always talk about millimeter wave stuff, right? I mean, like, that's your thing. Yeah, that's part of what I do. And it probably isn't – Yeah. Well, I mean, just like the waveforms that you – Sorry, the wavelengths that you're using are probably in those ranges.

**Gregory Charvat:** I think our point is that, like, it's – It doesn't matter what wavelength you're at for what we're doing. Got it. But it's all about the precision of the instrument, right? And so, you know, what we've developed is something that it's local. It's short range, out to 500 meters, 0 to 500 meters.

**Chris Gammell:** This is the centimeter accurate system, correct?

**Gregory Charvat:** And it gives you two centimeters or better precision, which – that kind of precision is more than enough – is good enough – actually more than enough – to navigate autonomous robots all over the factory.

**Chris Gammell:** Which is why the Kiva folks would be very interested in it. If I could paint a word picture, there was four units that were kind of, like, lofted and up above at various random positions. And then there was a little robot on the floor that had a predefined path. It was kind of, like, going into figure eight. It also had two things – two of the receivers on it, receivers slash transmitters, because I think it's both. Yes, they are, yeah. And then there was a third transceiver that was just handheld, so you could also see them. So then it was all visualized in 3D space on a laptop, so you could actually show where they are in space. But it was very accurate. Yes. Kudos on that.

**Gregory Charvat:** It is. It is. You know, why is this important? Why do you need short range, high precision GPS? Well, it's – in the factory automation world, it is the thing that's missing, okay? It is the –

**Chris Gammell:** Yeah, I mean, like, you think about getting a GPS signal even inside with your phone is kind of tough sometimes. Right. And then that's from satellite base. You're now basically making the satellites and then also making the receivers.

**Gregory Charvat:** Exactly. And not only that, we are substantially more accurate than GPS. That's true. Right. And that is missing today. It doesn't exist today. Right. And that's what we're –

**Chris Gammell:** Well, we should also talk about the other systems that are there because I think Josh was talking to there, and Josh and Chris are two of the people I talked to there. They mentioned optics or optical isn't – you know, like using machine vision is a very common remedy to this same problem. But then there's shelves in the way or stuff in the way, right?

**Gregory Charvat:** Machine vision works, but what happens is it records the area and uses what's called SLAM, which I forget what acronym stands for. Basically, it remembers what things look like, but if something changes, it gets all screwed up. And in a factory, you know, there's a difference between an academic project or a hobbyist project guiding a robot with a camera and a factory. The requirement of a factory that's making stuff to modern standards is every operation, every time that robot moves from A to B or enables some other process to happen, like put a screw or nut or bolt here or pick up and put it there, it needs – the decision needs to be right 99.99% of the time. That is to say, the robot can't be off by more than two centimeters. It can only be off by more than two centimeters one in 10,000 times it does that operation.

**Chris Gammell:** Yeah. And so – And even then, we prefer that not to happen too.

**Gregory Charvat:** Yes. Exactly. Even then, you should be better than that. And so that's why machine learning is terrible at guiding robots because, you know, if the machine learning stuff can't guide robots to that level of repeatability and accuracy. But you know what, Ken? You know what's really accurate? It's GPS. When I drive to Boston, it's always accurate. It tells you – it's right more than – every time I've driven to Boston, it's right. Okay? It's not right. Like with machine learning – It's not quite too sensitive, though. It's not right to 50% of the time, like machine learning, or even 80% of the time, which is aspirational in the machine learning world. It's right all the time.

**Chris Gammell:** Oh, wow. Okay.

**Gregory Charvat:** Now, machine learning starts to work really well, not for navigation, but when you have a super controlled field of view where you're looking at, let's say, a printed circuit board and you're aligning a part or something like that, where it's trained to look at something that's always the same, that's where it does –

**Chris Gammell:** Oh, and always like the same angle as well. Yes. Like straight on, dead on, not angled at all, not recapting. Yes.

**Gregory Charvat:** But when there's people walking around, when there's inventory moving around and the map doesn't look the same, it gets befuddled. Okay? And that's why you need navigation.

**Chris Gammell:** So – Well, there's other systems out there too though, right? So there's also LiDAR that is on the device, right?

**Gregory Charvat:** LiDAR is not navigation though. That's true. That's just object detection. That's object detection. Now, you could make a SLAM map just as you would with machine learning and vision with LiDAR data, but it has the same problem. Where that shelf of parts moves over here, then it gets all screwed up. So it – now it may be able to – it learns and adapts, but it's not at four nines. Okay? Okay. And so to get to four nines, which is the requirement in the industry, it needs to be very, very repeatable and accurate. Now, what is? Radio navigation, GPS, ORAN, and indoor GPS is – hits four nines. And that's why this is so valuable. Yeah. Everything else is a science project.

**Chris Gammell:** Well, what about other systems though? Like, so like we've had the, you know, the valve folks on a bunch with the lighthouse, that kind of thing. So what about like that as well? Lighthouse.

**Gregory Charvat:** I don't see people using lighthouses to assemble automobiles at the Ford Motor Company assembly. Sure, sure.

**Chris Gammell:** No, I'm just saying that like as a comparison technology though. They are not at four nines. Laser scan. That's fine. So that's the same thing.

**Gregory Charvat:** They're not at four nines. They will – they're not there. They're not going to get there anytime soon. But they're in the consumer space, which we've looked at before. The requirements in those consumer spaces are pretty light. Manufacturing requirements. requirements are very, very stringent. Like what we're showing for pneumatics is –

**Chris Gammell:** Well, I think the price point kind of play that out too, right? I mean like manufacturing is willing to pay higher premiums. Right. Exactly. Yes. And so consumer space –

**Gregory Charvat:** But certain technologies will not – don't scale to that accuracy. They just don't. And I think that is one example of one that doesn't.

**Chris Gammell:** Hearing the two centimeter accuracy with the 500 meter range is – that's what's interesting to me.

**Gregory Charvat:** You're not getting that valve. Lighthouse will not get you that.

**Chris Gammell:** Right. I mean just any kind of light-based technology, you start to have interference. You have beam form problems, right? So what else –

**Gregory Charvat:** Light-based technology tends to have a very narrow field of view. And for accuracy numbers we're looking at, you know, it doesn't go very far either. So it's – you know, you're talking meters as opposed to 100 meters. It's not – it's just not the same. I mean it is a sensor like competing against it necessarily. What you do is a plurality of sensors, but ours is the one that's missing right now. You know, if you want – like we demonstrated at Eckhart two weeks ago. So if you want – if you want a robotic pallet to drive itself out to the loading dock and have material put on it and drop to the assembly line and then have its material being lifted off and stuck onto a car, you're going to need our stuff to do that. Yeah.

**Chris Gammell:** So what are they doing today? What is the state of the art today? That's kind of the important thing.

**Gregory Charvat:** There's humans in the loop. So what happens today is you have assemblies that are on, you know, very – not necessarily a conveyor belt, but a chain. Like if you've seen Auto Factory, they're instrumented. They're precise. The assembly line precise. A robot is bolted onto or near to the assembly line precisely. And the robot is precisely pinned to the assembly line. So it has precision relative to the assembly line. But then to give the robot pieces and parts, humans are involved in getting the material from the trucks to the robots. And then there are other operations that are so complicated because humans have to use their own eyes to locate stuff that humans put the parts on the cars. And that's just an example. But what we would enable –

**Chris Gammell:** Well, what about like Akiva as well? They have lanes, right? So they have like a XY grid that the robots go into. Yes. But then they just kind of tell where they are in free space and make sure the carts don't run into each other. And if there's humans, they also say, no, there's a human in there.

**Gregory Charvat:** Yeah, they have LiDARs and they stop and stuff. And, you know, there's a lot to that. The Kiva stuff uses very, very conventional stuff. And I can't really say too much about it. But I think it's very conventional.

**Chris Gammell:** Yeah, no, I'm going off videos that I've seen, really. And so I don't think that's – nothing's secret there.

**Gregory Charvat:** Yeah, yeah. What you've seen of Kiva on the videos is exactly right. You see how the robots have it. You see them – you know, they have – it works. It could be a lot better. And our stuff – because we're shooting for 4.9s, our stuff could be potentially a big enabler for them as well. And so it's – sure. It's an enabler for anyone who wants to use UGVs on manned ground vehicles or wants to use them better. So it's a key thing. And that is the centimeter scale stuff. And then there's another thread of our technology, which is the next thing in the pipeline. Right now, we sell the centimeter scale stuff as of Monday. We're selling it. And the next level up is the millimeter scale stuff, which is to say when the robot pulls up to your assembly line or your workstation, when the unmanned ground vehicle drives up there with a load of parts. It's only – it only knows where it is within a couple of centimeters now. That's not good enough for an assembly robot to pick up something and stick it on a vehicle yet. It's still not that good. So that's why we developed the millimeter scale, what's called the K1000. So that's a shorter range system that goes out to nominally 10 meters. And what it allows you to do is when you're close, it gives you millimeters to four nines, to 99.99%. So now you know to within a millimeter where your card is. That's enough to pick up something and stick it on a car.

**Chris Gammell:** Right, right.

**Gregory Charvat:** And so that's another – that's like – so that's the other piece that's missing. And that's why we developed both threads is that we want to actually enable – like you remember the movie Star Wars where you see the robot assembly line. It's a fully automated factory and they're building the robots. Well, this –

**Chris Gammell:** Dude, you're not talking about the prequels, are you? Are you seriously talking about the prequels? Yeah, yeah. Well, sometimes you see them. Oh, boy. Oh, boy. This interview is over. Oh, shh. Oh, come on.

**Gregory Charvat:** Have you seen them before? They're great. I mean, that's literally – Jar Jar's my favorite character.

**Chris Gammell:** You just lost the entire audience. Boy.

**Gregory Charvat:** You guys didn't like – you didn't like that guy? Hanging out on boats too much. I thought that that guy brought a chill to the thing and I really liked the fact that they threw romance into the story. You didn't like that? Okay.

**Chris Gammell:** All right. All right. We're done. Oh, come on.

**Gregory Charvat:** That was like the best part.

**Chris Gammell:** Oh, boy.

**Gregory Charvat:** No, no. Just as an example. Okay. That's an example of a fully automated factory. But it's science fiction.

**Chris Gammell:** Yeah. You're talking about robots in general. And I think that's good.

**Gregory Charvat:** Well, it adds like a level of automation that doesn't exist today. Sure. And that's what we enable Tumax. That's what our focus is. And that's why you see both threads. So you've got the centimeter scale can get the material there. Or it can do – it can navigate all of the robots to the centimeters to do whatever they have to. And material handling is one example. And then the millimeter stuff allows you to instrument things, fixture things. We call it virtual fixturing. Now, that cart that's on wheels, it may as well be bolted to the ground and we measured it with a LiDAR because we know where it is to less than a millimeter. Now we could do machine operations to pick up stuff and mount things. So that's the theme of Humatics and that is our focus and that's what we're enabling.

**Chris Gammell:** Nice. Yeah, I like that virtual fixturing thing. And I think – I mean, that played well at IMTS as well. I was walking around with a friend early on in the day who had not done a lot of machining stuff. And he was kind of like asking me, he was like, well, what is the hard part about machining? And not that I'm an expert in this even in the slightest. But I said one of the things that I always struggle with and it seems like a lot of the things that people when they're doing machining deal with is like what is the absolute reference, right? Where is 000 axis coordinates, right?

**Gregory Charvat:** It's a tough problem.

**Chris Gammell:** It is a tough problem. And that's what – so like you think about – okay, so you put something into a vice. Is the vice 000 or is the – you know, is there some arbitrary point? And if there is some arbitrary point that's 000, where is the vice in relation to it? And then where is your piece of material in free space in relation to the vice? And then how do you do all this math backwards? And then how do you do the reverse kinematics for the robot arm that's in there or the milling head or whatever? And like that is a lot of machining and just robotics in general is where is stuff in free space? So if you guys are solving that, then that's a good thing.

**Gregory Charvat:** Here's another way to look at it. I think, you know, consider the cord and frame of a machine tool. You know, we – with the millimeter scale stuff, the K1000 stuff, we project that out onto the factory floor, 10 meters radius. That's what we do. We project it out in 3D, free space, out to 10 meters. That's what that tech does.

**Chris Gammell:** Why would you project it out though? You're saying that like you know you are giving a new 000 and then everything –

**Gregory Charvat:** What we're saying is take your 000 off your machine tool and now we can navigate relative to that to a millimeter, out 10 meters away.

**Chris Gammell:** So, okay. So I'm guessing – so let me explain the demo as I saw it yesterday. Maybe that will help too. So the demo yesterday was there was a – so you have your four-coordinate system GPS thingy up in the sky. And then there was a small device that had a little antenna-looking thing on it. And then on top of the antenna-looking thing, there was a ping-pong ball. And then the robot – you could move this fixture around. The antenna-looking thing was movable. You could move that within a certain area. And then the robot always went and picked up the ping-pong ball. That was the demo that I saw because it didn't.

**Gregory Charvat:** And it put it in a box for you.

**Chris Gammell:** And it put it in a box, right. The box was fixed. And so you're saying, though, that this is relevant in the machining or the factory context because you might actually want to move that thing around in free space because it might have just come into the frame from another robot, right?

**Gregory Charvat:** Well, imagine that thing that holds a ping-pong ball. This is where you're a little abstract. Imagine – we're slightly abstract here. So imagine that the thing with the ping-pong ball is stuck to a parts rack. And you're from the Midwest. You know what the parts racks look like that go in and auto-auto companies, right? Yeah.

**Chris Gammell:** You know, that's the only way you actually know what a parts rack is.

**Gregory Charvat:** If you're from Ohio or Michigan or Indiana or Illinois, you know what that looks like. So they have these parts racks that are usually made of steel and they'll load them with, like, you know, hoods, windshield wipers, alternators, whatever. And they're all, like, positioned accurately inside the parts rack. So imagine you have the millimeter-scale beacon, we call it, on the parts rack. And the parts rack gets delivered by an employee, a factory worker, or is driven there automatically by an unmanned ground vehicle and dropped off somewhere arbitrarily but within the assembly robot's line of reach, okay? And now the humatic system pings the parts rack to within less than a millimeter and tells the robot, here's exactly where that parts rack is. And we know what kind of parts rack it is. And the robot says, okay, great, now I can start picking up alternators and bringing them over here and sticking them with the car.

**Chris Gammell:** I could pick up hoods and drop them. Right, stuff that our eyeballs do right now, right? I mean, so if the robot is now a human, it says, oh, look, a cart. And then I know how to, you know, move my actuator, which is my hand, to pick up a part, right?

**Gregory Charvat:** And that's why that demo is so powerful because here we have a small ping pong ball and we have our beacon. And you can stick the beacon anywhere and the robot picks it up every single time and puts it in the bin at the same location, too, by the way, every single time. So that is symbolic of all the things we can potentially do with the technology from automatic assembly of things that are now highly manual to we enable that to even packing boxes automatically. That's why it picked up a ping pong ball and dropped it in a box.

**Chris Gammell:** Right. I think that's a good point, too, because, you know, obviously at the show there was tons of robots, including the pick and pack robots that are out there. But the pick and pack robots start within a very significantly constrained frame, right? I mean, they have basically there's a camera and whatever the camera sees, then it knows, OK, there's an object here. I know how to navigate from my zero zero zero to that one, two, three, four or sorry, two, three, four and whatever that location is. And it can pick it up and put it back wherever it needs to. But you're saying now if that camera is moving or if the camera is not as precise, then you can actually start to do other things. Yes. You kind of you're freeing robots from their cage. So, Greg, how do you feel about allowing robots to find and destroy humans?

**Gregory Charvat:** Right. Exactly. Yeah. No, that's not happening. Yeah.

**Chris Gammell:** That's almost worse than talking about the prequels. I know.

**Gregory Charvat:** I think that that's it's so funny because I actually read a headline where they're testing autonomous tanks and M1A2 tanks and stuff like that. So, you know, it's it's it's it's interesting how people use robotics. I think it would be really cool to use robotic. Like, you know, how like automated farming or other mechanized farming, like the use of tractors and combines. Yeah. It freed human society from picking away at the earth. It freed us to do things like electrical engineering. Right. And then build big metal things and stuff like that. We didn't all have to be, you know, picking away at the ground and growing stuff anymore unless you wanted to. And that was a big change in our civilization. That happened in the third century. Yeah, definitely.

**Chris Gammell:** Yeah.

**Gregory Charvat:** And I think similarly, this our technology will enable future factories where there's higher levels of automation. So people don't have to do the drudgery that often happens in these factories. So I think it's I think it is transformational. I think we will change the way we make things in a big way. Yeah. In a similar way that farms were industrialized. I think the new level of automation that we will see in factories of the century will free us from factories to do more interesting and intellectual things as a society, which could be very good.

**Chris Gammell:** Yeah. And I think the I think I really like I think the way that you talked about indoor GPS, I think that's a very important missing piece. Obviously, at the end of the day, it's it's using RF and, you know, time of flight like we were talking about.

**Gregory Charvat:** It's a time of flight measurement. Yes. In all cases, all of our technology measures the time of flight. They measure it in different ways. Like the centimeter scale one, it's an evolution of a technology that's developed 20 years ago. And now it's perfected. And it uses impulses. OK, it uses time of flight. It uses impulses. And then and then we could do really cool things. We can like phase code and we could do all kinds of weird stuff with it. It's actually a very sophisticated technology. Imagine $150 million in 20 years of development. That is what that technology is. And the millimeter scale one is is a lot different. It's just so it measures the time of flight, but it does so in a very, very unconventional way. That's actually the stuff we did. We demoed to Jeff Bezos was the millimeter scale stuff. And that's that's a whole different bird, but it is super unique. And it does. It's kind of incredible. The precision that we get out of it is astounds even us. Those of us who've been working on it past a couple of years. Yeah. So we hope to. Well, our plan is to bring the millimeter stuff to market next year. This year, it's the centimeter stuff, the K100, the K300. And now people can buy that, those products. And next year will be the millimeter stuff. And right now we're piloting the millimeter stuff with some early adopters and getting feedback. And use the system that we showed at IMTS is the one that that the same one that is with our pilot partners. And it's they're loving it so far, so good. So great. Well, they can what they, you know, it's kind of the process. You get pilot units out there and see what the market says. And then you tweak it. And that'll be your first release. And we're piloting that one. And we're selling the other one. And we're just cranking away.

**Chris Gammell:** You know, it's been interesting how our, you know, you being on the Amp Hour has changed. And you've talked about, you know, we started out having you on the show talking about, obviously, your book and the coffee cam radar and all this stuff. And then, you know, obviously a lot of ham radio stuff and just kind of the transition into the startup thing. And it seems like it fits you really well. And so you're doing some crazy things. No, thanks, man.

**Gregory Charvat:** Well, it's, you know, it's one of the same. I think your career evolves. I actually believe that there is a career track in startups. Like, you know, you can set yourself up to go from startup to startup over time. You know, you put in your time. You get, you know, you get to a point where you've achieved something. And then you may move on. You may do your own thing. Or whatever the case, we're all in flux all the time. And I think it is a viable career path these days. I've realized that. When I first started going into startups, I figured I would just do one. And then exit or not, I'm just going to go back to MIT's Lincoln Lab, which I loved it over there. And I'm just going to go back there. I'm going to do this once. And this is, like, super risky and all that. But as it turns out, I don't, I think as an engineering career path, they're not as risky as you might think. Because what ends up happening is once you get that first slug of venture capital and you fill your board with people who have a vested interest in your success, and you deliver, at least maybe you deliver, maybe you under deliver a little bit on some things and over deliver on other things. But as long as you're delivering, you're on path and you're flexible enough, you're pivoting the right way. You can generate that next round of funding if you need it. And you can generate revenue. You know, you can, if you just kind of play the game right, I mean, you do right. They say an old saying from the jazz era, you know, do right, fly right. You know, if you fly right, you can make a career out of this stuff. And it's not an unstable thing. Once these companies are funded and they're moving, there's always ways to get funding. There's ways to pivot them into a useful product. They will make it happen. And that's one thing I've learned over the years, no matter how tough the problem is. And anyway, let's do it.

**Chris Gammell:** Awesome. Anyone can do it. Well, I think I'm excited to hear about what, you know, obviously how this works out. But also, I assume there's something that's next, too. So that's great.

**Gregory Charvat:** Yeah, you know, at Humatics, we have more stuff. We have another thing in the pipeline that hopefully, perhaps, we can talk about next time on Amp Hour. That is very cool. And it's actually meant to be lower cost and perhaps target some of these non-industrial applications. You know, we're looking ahead a little bit.

**Chris Gammell:** Injectable GPS tags so the robots can find you. That's what I'm going to. I'm going to just guess that. You don't have to say yes or no. If you say nothing, I assume I'm right.

**Gregory Charvat:** Rest assured to all your listeners, that would never work because microwaves cannot penetrate saltwater very far. And your body is just made of saltwater.

**Chris Gammell:** So that would never work. Okay. So tattoos then. It's like outside the skin. Right, right. Exactly. All right, cool. Where can people find more about you and the companies that you work with?

**Gregory Charvat:** I think, you know, so we'll list them by latest to the first. So, so, humatics. If you go to humatics, Google humatics corp, you'll find us. For hyperfine, Google hyperfine research. They are still stealth. You're not going to find much. But hyperfine's hiring. Humatics is hiring. So if you want to work with me, we're hiring. Send me an email. We're actually looking for a board designer. Someone who's really good but has experience churning out circuit boards. Like, you know, basically like your usual mixed signal digital stuff with a micro and churning it out fast. We want someone with some of the big three. So if you're that person, send me a note.

**Chris Gammell:** Are you an Altium house, I'm guessing?

**Gregory Charvat:** I believe. We don't care. As long as you can do it. Got it. Got it. And then on the other side, there's hyperfine research. And they are hiring as well. I believe they're looking for an RF engineer. So if you're an RF engineer looking for something interesting, you can email me. I'll put you in touch with the right people there. And then Butterfly Network is the other one. And they're the ones who are building the first ultrasound on a chip, which they are shipping out pilot units now. I believe they have some large number in the field. I don't know. It's got to be on the order of 1,000 because if you look at their feed. Actually, I recommend looking at Butterfly's Twitter feed if you want to see the latest. It's unbelievable.

**Chris Gammell:** You want to see a lot of doctors who are like, what the hell? It's pretty cool, man.

**Gregory Charvat:** They're killing it over there, Butterfly. And I know they're hiring mixed signal ASIC designers. They're looking for one right now. So if you're that person, you can email them or email me and I'll put you in touch with them. And either way, if you want to join the fun, there's always fun to be had in these companies. So thanks again for listening to us yammer on because when Chris and I get together, we just, it's kind of fun. It's good times.

**Chris Gammell:** Yeah.

**Gregory Charvat:** Yeah. Thanks, Chris.

**Chris Gammell:** Thanks, Greg. We'll talk to you soon. Talk to you later. Thank you very much. Thank you.
