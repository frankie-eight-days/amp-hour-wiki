---
episode: 383
title: An Interview with Scott Shawcroft
url: https://theamphour.com/383-an-interview-with-scott-shawcroft/
---

**Scott Shawcroft:** This is The Amp Hour Podcast. Released March 11th, 2018. Episode 383. An interview with Scott Shawcroft. Welcome to the Amp Hour.

**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. And I'm Scott Shawcroft, a freelance software engineer that works with Adafruit. Welcome, Scott. How are you doing? I'm doing great. Busy day, but I was super excited to be on the Amp Hour.

**Scott Shawcroft:** Yeah, I'm glad we could sneak this in here. You and I were talking after last week's my complaining about J-Link, which I obviously got from the wonderful folks at Adafruit. And I have the EDU version. And you're like, hey, did you know I help people with that stuff? And I'm like, yes, I did know that. But how about we talk about on the Amp Hour as well? Yeah. Well, you just said talk. You didn't say on the Amp Hour, but you know. Well, you know, eventually all of my complaints and, you know, cries for help make it onto the show. So, thank you for that.

**Chris Gammell:** Well, now more people can learn, not just you.

**Scott Shawcroft:** You know, I'm starting, you know, I've got like a new theory that like my only real value in this world is being a foil. You know, the foil that people can use as a, you know. Well, at least Chris asked the dumb question. So, I am happy to ask them. And I will be asking them shortly. Before we do that, let's get a little bit about you. So, what's your background?

**Chris Gammell:** I'm a software engineer. I went to the University of Washington and did computer engineering there. And after that, I went to Google and worked on Google Maps for almost six full years.

**Scott Shawcroft:** Who's that? Google? Google? Google.

**Chris Gammell:** They're a small company out of Mountain View. Okay. Actually, in Seattle, the office when I started was not that big. So, it did feel like a small company. And I would visit Mountain View and I'd be like, whoa, there's buildings full of people. You'd be like, wow, the food is better here. Yeah. Yeah. So, it was really, yeah, it felt very intimate when I started and it grew a lot the six years I was there. I did map rendering. So, if you remember, the bike layer came out where you could like toggle the map to see where all the bike lanes were.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** That was one of the things that I did there was the actual like styling of that.

**Scott Shawcroft:** So, how many bike lanes did you have to ride in order to get all that data? It wasn't me. I just finished my coding today and boy, am I legs tired. Right. Right. No. It's not quite that. Okay. Yeah. And I always wondered about that. Where did they, I mean, I probably can't mention where, but I mean, like it's just like a database that gets pulled in. And then you work on how to make it actually play nice with all the.

**Chris Gammell:** Right. So, so there's a, there's a really good article. It's been a while, but one of the efforts that happened at Google while I was there was called Ground Truth. Uh-huh. And they were, their whole goal was to take all of the data that we had satellite, straight view, and, and turn it into structured data that we could use for products like map rendering. Yeah. Or directions or all of that other stuff. Right.

**Scott Shawcroft:** Well, it just paid dividends over, I mean, like the API people use that all, like, I don't think I've seen people using the, you know, the other map APIs that are out there in years now. I mean, like, I know that they still do and there's other stuff that's out there, but I mean, a lot of people are using that API.

**Chris Gammell:** Yeah. And like the data quality is something they invest heavily in and that's really what makes or breaks an API or. Right. Or a mapping product. And that is an annoying job too. It's, it's very hard because the world is constantly changing. Um, but yeah, if people want to know more, Ground Truth is the thing to look up. Okay. About that. We'll put a link. Bike Trails specifically, it was a combination of like, uh, city owned bike data that they acquired plus, uh, just information from rails to trails. Oh, cool. Which is this national effort that turned old railway, railway grids into great, uh, grades into trails.

**Scott Shawcroft:** Yeah. No, I love that stuff. There's one right near me and it's, it's, it's great. Cause it's like out of, out of the, the traffic and yeah, it's really, really good use of, you know, former, former, industrial land pretty much.

**Chris Gammell:** Yeah. So when we, when we launched back in 2010, that was like kind of our national coverage was the rails to trail stuff. Oh, very cool.

**Scott Shawcroft:** Well, so, uh, you know, you eventually got sick of, you know, just solving bike problems and, you know, map problems, whatever. So what happened after that?

**Chris Gammell:** Yeah. So, um, I, I spent six years doing software in the cloud way far away from the hardware. I'd gotten really into quadcopters and drones and, uh, decided to kind of pursue that. I decided to leave Google and then decided to pursue hardware design, uh, for, uh, flight controllers, particular in particular. And, uh, there's open source software called clean flight and beta flight, which are, uh, open source STM 32 based flight controllers for racing quadcopters. Okay. And so I spent about a year developing my own modular, uh, flight control system, which I don't recommend people do. Um, it didn't, I didn't sell very many, um, because they were very expensive.

**Scott Shawcroft:** And yeah, the thing is modular always needs lots of connectors, right?

**Chris Gammell:** Yeah. And I was using Hirose, like 80 pin. Oh, I think it was very well engineered.

**Scott Shawcroft:** It was just way too expensive. You know, when it's an API, it's just, it's just a couple more characters, right? But, uh, you know, that interface, that, that, that'll, that'll, that'll bite your ass, huh?

**Chris Gammell:** Yeah. So I, it did. Yeah. Um, but as I got further and further through that, I started talking about what I was doing. Um, another pro tip is I, I was in this mode of like, I want to be secretive cause it's amazing what I'm doing. When in reality, people would have told you. Right, right.

**Scott Shawcroft:** Wait until the launch, man.

**Chris Gammell:** Everyone's going to care. And nobody cares. Yeah. Um, but I did starting, I did start talking about it, um, on the, I was on the macro fab engineering podcast one time. They were the people that did like my quote unquote production run. And then I had been watching a ton of Adafruit videos because there was really, really useful, like desk of lady Adas talking about like test jigs and things like that. So I was learning a lot about the production side of, of electronics through Adafruit. And I had also started doing, um, show and tell to show off all of the stuff that I was making. And after my, my business, uh, product side chickity of chickity tech, which is my company, uh, kind of was clear that it was not going to pay the bills anytime soon. And then I went on show and tell Adafruit show and tell and was like, Hey, I'm looking for a job. And, uh, Phil, a Mr. Lady Ada was like, what do you do? And I said, Oh, I'm a software engineer. And he's like, Oh, okay. And then the next day he emailed me saying like, Hey, we have a project in mind. Are you interested? And I was like, yes, sweet. And I never looked back.

**Scott Shawcroft:** Nice. That's great. That's yeah. I mean, Lamar and Phil, we love them here. And, uh, yeah, that, that's, uh, that's a, I mean, that's a good rule for people listening to, you know, you got to put yourself out there, right? Talk about what you're working on. It sounds like you're showcasing your product. You know, you have a personal site where you showcase stuff. Tan newt. Is that how that's your handle online all the time? Yeah, pretty much. What does that mean? Tan newt.

**Chris Gammell:** Uh, it's, it's two words. It comes from like the late nineties when they had these like random word generators. Really? Um, I remember a password I got from something like that. It was like pork filled pansy. It was another like completely random. And now we all know his password to everything still. Um, not, not a password I use anymore, but yeah, so tan newt was another thing that was randomly generated and I just thought it was a very funny image and it turns out to be relatively unique. So I was able to get it in a lot of places and I kind of just rode that. Nice. It is a little hard for people to pronounce, uh, which is something I would consider next time I choose a username. Right. You click the button a few more times and then you're good. Right?

**Scott Shawcroft:** Right. Yeah. Okay. But, uh, yeah, that's great. No, I know. That stuck with me a while. I, I, again, again, pointing to, to your stuff. It's like, uh, you know, this is, this is the classic portfolio style site and it's good. You know, you're showing off the stuff you're working on. Not just where you're working.

**Chris Gammell:** My personal website.

**Scott Shawcroft:** Yeah. But I'll see. Yeah. Like what's kind of out of date, but yeah. Well, that's okay. But I just mean like the stuff that you were working on. That's an important thing. So if people were ever looking for a portfolio style site, I think this is a good, good example.

**Chris Gammell:** Yeah. Yeah. I don't update it much, but yeah. Well, you know, that's what it's for. It's just like links to things that I've done and putting my name to all the things that I've done.

**Scott Shawcroft:** Yeah. Yeah. So what was it, what was this project that, that, uh, Phil said you should maybe think

**Chris Gammell:** about working on? Uh, they asked me to port MicroPython to the Sam D21, which is, uh, at the time it was Atmel, but now it's owned, they're owned by Microchip.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Uh, it's a microcontroller from them that, um, kind of came, uh, came to market with the, or I think was popularized with Arduino zero.

**Scott Shawcroft:** Mm-hmm.

**Chris Gammell:** Um, but because of the conflict between Arduino.org and .cc never really got traction. Mm-hmm. Um, but the Sam D21 got on Adafruit's radar there and, and all of the M0 line products, um, run that chip.

**Scott Shawcroft:** Right. Right. Right. And, uh, speaking from the other products that I've used from Adafruit, you know, like they, they, and you by extension have worked hard by, to basically make it a more seamless experience from, you know, going from a, you know, the, the 328, that Mel 328, uh, P, is that right? Whatever the. I don't actually know. I think it's, I think it's the P, uh, but the 328, which is, uh, on the original Arduino Uno and, uh, and now the, uh, yeah, this, the M0, I mean, it's just like such a significant upgrade, you know, in terms of memory and, you know, processing power and everything. It's right. Yeah. It's, it's, it's, it's, it's silly.

**Chris Gammell:** Uh, yeah. And it's not even a, it's not a price upgrade either. It's actually tends to be cheaper than the, the 328s now, I believe.

**Scott Shawcroft:** Right. Yep. Exactly. Because I mean, yeah, I mean all the M0 parts these days are just so scraping the bottom of the barrel kind of cheap. So yeah, really nice. Uh, it's got a lot of the same or even more, I think it depends on which flavor of the part you have, but it has, you know, other peripherals too. So, and again, this is, this is the Atmel slash microchip version, but like really the M0 and the ARM ecosystem in general, like all of the Cortex stuff, it's just, you get so much stuff for so little money these days. Yeah. It's insane. You know? And then, and that's before you even jump into the ESP 32 world where it's like, you know, even cheaper, way more stuff, but obviously not as, not as accessible. Yeah. So, okay. So, I mean, how did you feel about all this? I mean, you'd done, you were doing STM 32 stuff, right? So, so did it cross over pretty well or what?

**Chris Gammell:** Um, I had only dabbled in it a little bit, like most of the beta flight code I was working with, like they did the hard part. It was, is understanding that like pin mapping was a thing and figuring out like how pins mucks together. That's most of the experience I got, uh, with the STM stuff and then bringing MicroPython, which is actually STM 32 by design or with the PI board, which is kind of its flagship board, um, over to the SAM D 21. It was kind of a matter of learning to interact with all the peripherals and, and making that work. Got it. Okay.

**Scott Shawcroft:** Well, and we should, I should mention too, uh, so this is when it was still MicroPython at Adafruit, right? Yeah. And we have had Tony on the show. So, so your coworker is Tony DeCola, uh, who also works on, uh, MicroPython, now Circuit Python. Uh, but Tony's been on the show before. So yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. Really early on, I think as well. Uh, early on for us, early on for him. Early on for MicroPython at Adafruit.

**Scott Shawcroft:** Yeah. I think so too. And yeah, and it, uh, yeah, Tony was showcasing a bunch of this stuff as it was, as it was being used more and more at Adafruit, I think. And, uh, and, but it seems like it's taken on a kind of a bigger role there.

**Chris Gammell:** Yeah. Within Adafruit. Yeah. I mean, I don't actually have much experience with Adafruit prior to that because I was actually hired to work on it. Uh-huh. Um, so my view is very Sandy 21, uh, MicroPython centric. Um, but the impression I get is that, uh, Lamore and Phil have really bet on MicroPython and, and CircuitPython as a platform for the future.

**Scott Shawcroft:** Yeah. Um, no, I think it's, I think it's, I think it's really smart too. I mean, you know, and it's interesting, like, obviously, you know, I, I know you don't want to speak for them and I'm just speaking as an outsider, but like watching all that Arduino crap, it was like the biggest risk for, for me as a user, not even for someone, people that are selling it and, you know, their livelihood based on products that were using this software. It's like, if that, you know, centralized tool went away with me and Dave talked about this too. It's like the centralized tool of Arduino is the real value there, right? The hardware was varied throughout the ecosystem and ultimately didn't matter as much, right? Obviously it was using a very old processor, but I think that this move too is like, basically it's, it's accessible still. It has all the same things. It's accessible, uh, maybe even more so in turn because it's closer to Python. It's, it's, it loads fast and, uh, it works, you know, pretty seamlessly with the hardware because of the stuff you're doing, the stuff Lamar is doing, the stuff Tony's doing. So, um, yeah, I think it's a really cool move and, uh, and I've been using it and I like it a lot actually. Yeah. I was happy to hear that you like it a lot. Yeah. Maybe, can you give people like, uh, uh, a feel for what it is if they, if they haven't listened to another show with Tony?

**Chris Gammell:** Yeah. So, um, I was thinking about this in the car, uh, how I would answer the question, what is CircuitPython? And I think what we should talk about first is what Python is. Um, yeah, indeed, indeed. What is Python? Right. So, uh, Python is a programming language, uh, which is programming languages are a way that you can tell the computer what to do. And when I talk about what computers are good at, I like to say that they're very fast at being very dumb. Um, okay. So, so they're so fast, you can't tell that they're extremely dumb. Um, but programming languages are human readable forms of telling the computer what to do. They get, gets boiled down to a binary version that the computer can understand. Um, I like that. That's, that's a very high level. Yeah, that's good. Yeah. We were talking about that too, about top down. Right. Yeah. Yeah. Yeah. So, so I wanted to start there and, uh, some people may be familiar with programming languages like C, um, really popular in the embedded world. And that lives kind of from the hardware up in my mind, whereas Python, which is Python is a couple of decades old and it really grew up on the other end of the spectrum of it's really good for beginners and novices. Um, it's very, a lot of schools have moved to using it instead of, um, languages like Scratch or Java in their intro courses. Or C++ in my day. Or C++. Yeah. I learned Java. Not friendly. Yeah. Um, so it's hit that sweet spot with novices. And I would also say that, uh, because its strength is there, it's also grown into a variety of not traditionally computer savvy, uh, spaces. So it's very heavily used in data science. It's heavily used in hard sciences. Yeah. Um, because it is so accessible to people who don't do programming as their day job.

**Scott Shawcroft:** Yeah. It's like a, it's like a language of math. It's like a, it's like a math helper. It's a, it's a, it's a spreadsheet helper. It's a whatever helper. Yeah. Like, like the, what's that one book that automate everything? Yeah. I think it's a no starts press book. Yeah. I know what you're talking about. I can't remember what it is, but it's a book basically where you can automate tasks using Python. And that's what a lot of people use it for. Like, you know, so it depends, it depends on the audience you're talking to. It feels like it's like some people are doing text manipulation. Some people are doing image manipulation. Some people are, it's really data manipulation. Some people are Instagram. Some Instagram. Really?

**Chris Gammell:** Yeah. Oh, really? I think it's Instagram. Oh, wow. Uh, they were one of the keynotes at, uh, PyCon last year. They were talking about switching all over to Python. Three. Um, so it does scale.

**Scott Shawcroft:** The ultimate, uh, we don't need to talk about that. Yeah. Yes. So. Yeah. And server, server front and backend type stuff too, which is fun. Again, not really what we're talking about here, but it's, but now it's taking that similar user friendliness and kind of now what kind of diving down to lower levels.

**Chris Gammell:** Well, it's, it's bringing it to a new platform, I would say. So, um, micro Python and by extension circuit Python bring that ease of use that, um, that Python has to the, uh, the microcontroller world. Yeah. Um, and, and I should say that also Python and circuit Python have this strength where it may not be the fastest to execute, but it's really fast to iterate. Yeah. And for beginners, uh, iteration time as low as possible is a good thing because that means that you change the code and you immediately see how you've impacted what the behavior, uh, and getting that down is super critical. And that's a trade-off that I think Python had made previously in circuit Python makes as well. That has really caused it or is one reason that it's very, very popular with beginners is because of that very fast iteration time.

**Scott Shawcroft:** That sounds right. Yeah. And I think, so another thing that, that really never sunk in, and I'm, and I'm not sure if you and I talking about it now would matter for, it's sinking for people listening rather. Um, but the whole like interpreted versus compiled, I never, I never understood what that was until, until I started using micro Python circuit Python. So can you try to explain that? Maybe I'll try to explain it if I don't understand what you're saying.

**Chris Gammell:** Sure. So the question is, is what is the difference between something that's interpreted and what something that's compiled?

**Scott Shawcroft:** Yes.

**Chris Gammell:** So for example, Arduino is compiled. Arduino is C, C plus plus under the hood. They do some funny tricks to make it proper C before they actually compile it. Um, but the advantage to that is, uh, you have a very strong computer like your desktop or your laptop that can spend time optimizing, uh, the code for you. And then in the end, what you end up getting is some code that runs directly on the CPU. And what I mean by that is that code that you wrote leads to instructions that the CPU can directly execute.

**Scott Shawcroft:** Right. Um, it's basically taking it from, let's say C plus plus, and it's making assembly, right? Which then gets, well, you can view it as assembly, but it's really just have these instructions that are relate to machine code. Yeah.

**Chris Gammell:** Yeah. Yeah. It literally is machine code where shift left or jump or whatever. Yep. So, uh, interpreted languages have an extra step where instead of when you compile something, you get machine code, you get what is called byte code, uh, which is a different intermediate layer that does similar stuff to machine code. But in reality, it has a layer of C code essentially underneath it that executes based on the byte code. Um, I don't know if that, is it good enough explanation?

**Scott Shawcroft:** No, that doesn't really help me actually. Well, I actually didn't even know that was a thing. So that's, that's really what I'm saying. I'm not saying it doesn't help me. I'm just saying I didn't know byte code was a thing. So, right. I always thought the interpreted piece was like now that basically you have written a small application that sits there and is like a, it's like a, uh, what's it called? What's the bug that they stick in your ear in Hitchcock's Guide? Yeah. Uh. Uh. I'm thinking earworm, but I don't think that's what you're thinking. Yeah. It's, it's a Babelfish. It's a Babelfish. Yeah, yeah. Or going, so it, it consumes some kind of code and it craps out machine code, right? And it does that live though, versus doing it once and then always just pushing that, that crapped out machine code to your device. Now, now the Babelfish lives on your device. Does that sound right or no? Is that, is that a weird, I mean, it is weird, but.

**Chris Gammell:** I don't, I, I understand what you're saying, but I, I, when, when you load a file in CircuitPy, Python or MicroPython. Yeah. Um, you don't, and I think Python works this way as well. You don't get out instructions that are equivalent to instructions that the CPU knows about.

**Scott Shawcroft:** Oh, okay.

**Chris Gammell:** Um, instead what you're getting is, what you have is you have a C function somewhere that reads the byte code and then does some stuff.

**Scott Shawcroft:** Interesting.

**Chris Gammell:** Um, so there, there is a layer of indirection there.

**Scott Shawcroft:** Um, but it's not like, there's not some machine that's sitting there and just consuming a lot. You're saying that there is, it's consuming the intermediate step that you're loading into there. It doesn't care. It doesn't need to do it dynamically. It doesn't need to keep going and going and going and retranslating.

**Chris Gammell:** Right. So it does like CircuitPython will translate your source code to byte code up front.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Um, it'll do that once and then it'll execute it just like the machine would do machine code. Uh huh. Um, but that byte code is dynamically loaded. Not it's, it's the byte code is stored in Ram. It's not stored in your flash every time.

**Scott Shawcroft:** Oh, okay. And, and, and does that distinction matter too then? Because so, yeah, cause maybe that's a good, a good, uh, comparison point as well. Right. So, so you compile something, you have an Arduino sketch, you compile it down, you're going to load that into flash. And then when you hit go, it's going to hit reset and it's going to load the flash into Ram and operate out of Ram. Right. Right.

**Chris Gammell:** So in comparison, CircuitPython, what you've loaded into flash is basically your tools. So your compiler you've loaded in there as well. And so there's some code that says like, Hey, I'm going to look for this file code.py. I'm going to load it. I'm going to convert it to byte code, which I'm going to store in memory. And then I'm going to run what is called the virtual machine, which is a big complicated loop that I don't really understand. Uh, that's written in C, um, and it interprets those byte codes to into machine code. But it only does that once you're saying? Uh, so it'll do that the first time it starts up. And then the way CircuitPython works, if you save the file again, it will stop that VM. Um, and then it will go through that process. It will parse the file into byte code and then rerun it again.

**Scott Shawcroft:** See the VM in that case would be the Babelfish in my, in my weird example. So yeah. Okay. Yeah.

**Chris Gammell:** I guess I'm thinking what is stored. It's machine instructions for your code is never stored. It's interpreted from byte code.

**Scott Shawcroft:** Machine instructions for your code is never stored. Never stored in flash. Correct. Okay. Cause that's like what an Arduino does. Yes. Or that's what, yeah. Yeah. Right. Right. Okay.

**Chris Gammell:** Well, we store in flash. We, our express boards have a separate flash chip that stores, uh, the text version of your code. Oh, okay. Interesting. So it's, it's always dynamically compiled to byte code. Right. Right. Okay.

**Scott Shawcroft:** Okay. So that was a lot of discussion. Yeah. That was in the weeds. Let's, let's zoom back out and like, so practically how does this work then? So someone buys a Trinket M zero, which is like my new favorite board. And I think I've said that on the show before, which has a little Sam D 21 on it. And it's what eight pins, 10 pins, something like that. What do they do? Yeah.

**Chris Gammell:** Something like that. So it ships with circuit Python. Yeah. So all you have to do is you plug it into your computer and it will show up as a USB drive and it will have example code on it in a file called code.py, which you can double click and open in a text editor, which you may have installed already. If you don't, Adam is a great text editor. You edit the file, you hit save and it runs on the, on the board.

**Scott Shawcroft:** That's pretty crazy. That is, that's what I've, I've talked about on the show before, but that, that kind of iteration loop is kind of insane.

**Chris Gammell:** Yeah. For, for seasoned programmers, it's kind of like a, I don't want it doing that on behalf of me, but then you use it and you're like, you know, it ran before I had a chance to even go to the other window. Yeah. Right. To see the output. Right. And it's really nice. Yeah, it is.

**Scott Shawcroft:** I'm glad you like it. I mean, especially for like, for like, well, like, like I've said before, right. It's on, I said, maybe not to you, but on the show, uh, you know, like if, if I'm just throwing values at a, at a ADC and I just need to read, read and write to registers, like that kind of thing, that kind of iteration and cycle of like, and it's, it's effectively what I was doing on Arduino anyways. Right.

**Chris Gammell:** Right. Um, but now you're not erasing the entire chip compiling and then uploading it all back.

**Scott Shawcroft:** Right. And actually one other thing that I found out too is, uh, about myself is that, you know, like, you know, like that terrible, like when you get like that, like fever, feverish, uh, troubleshoot, you ever get in that feverish troubleshoot loop where you're like, Oh, I'll just change this one thing. Save. I'll just change this one thing. Save. I'll just change this one thing. Save. And I'm like, Oh, it's broken. And I can't control Z it, you know? And I'm, and I've, for some reason I've, I'm, I'm feverish. So I haven't been like doing revision control or anything like that. And so, you know, the thing that was working the first 30 times and on the 31st time I changed something that I don't remember. Uh, I'm screwed. Whereas, or, or, you know, I save it in a different location or whatever, whatever. And I have to actually keep track of that file. And now it's like, I pick up a board that I was working on. It was working when I put it down and I just load it up and I'm like, Oh, Hey, here's the file.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Yeah. I was just talking with a friend of mine, Sophie Wong, and she was saying she loves that part of it as well. Just her codes on the device.

**Scott Shawcroft:** Codes on the device. It's just there. I mean, it's probably, it's probably like it's, it's lulling you to sleep, but, uh, you know.

**Chris Gammell:** Yeah. I always back up your stuff.

**Scott Shawcroft:** Yeah. Right. But it is still really nice. Revision control. It's a thing folks. Uh, okay. So, um, so we've talked about how it works. Yeah. A little bit too much probably. Yeah. Um, but we haven't talked about why it works. That's fine. Not the right question either. Why it works. Yeah. I mean like, so I can, I can talk about our goals.

**Chris Gammell:** Yeah.

**Scott Shawcroft:** Okay. That's good. Yeah.

**Chris Gammell:** Like, um, and, and this gets into a little bit of why we aren't still MicroPython. Um, oh yeah, that's good. Um, like our goal is to be an excellent experience for people who have never programmed in their life. Um, those, those are the people that we're, we're going for with CircuitPython. Mm-hmm. And that's not to say we don't, we aren't happy to see people come from Arduino or MicroPython or C, um, to enjoy it. It's just to say that like the decisions we make are not necessarily, not necessarily for those people.

**Scott Shawcroft:** Um, okay.

**Chris Gammell:** The auto reload that you love so much is one example of a decision we've made explicitly to make it easy for those people. Mm-hmm. Another example is that we call it code.py and we actually support calling the file code.text as well, because we're not assuming that the people who have never coded in their life actually understand what Python is or what main is, um, but may have heard this kind of code is a buzzword. Oh, okay. Um, and then we've also made some decisions to, uh, change the way that you work in CircuitPython to better match CPython compared to, uh, MicroPython who has made some trade-offs in how you use it in order to get more performance. Um, so we've, we've explicitly chosen to be less performant than MicroPython in order to be more similar to Python, uh, because Python has tons of resources on its own that we want to take advantage of.

**Scott Shawcroft:** So can you give us an example of that?

**Chris Gammell:** I can't, like, like the API stuff?

**Scott Shawcroft:** No, well, like what, uh, what, what would, what would MicroPython do that CircuitPython doesn't do? Like you said, it's, it's made to be more performant in MicroPython versus CircuitPython. So like, right.

**Chris Gammell:** So one example is, uh, there's a thing called, so there, there's two ways of, of doing things on an object in CircuitPython. So, uh, in C land, you always just have functions in C plus plus you have objects. And then in languages like C sharp, you're, you start to get, um, both attributes and functions. So a function is something you can think of that performs behavior for a thing. So that might be like blink five times as a function. Yeah. It's like a tiny little loop, right? Yeah. Yeah. It's like this little loop.

**Scott Shawcroft:** You say, go do that thing. And then come.

**Chris Gammell:** Yeah. And it takes some time. It does multiple things in a C, a particular sequence. That's what a function is. Um, but in Python, there's also attributes, which is just state, right? It's just, um, is the led on or not is the digital pin high or low? Um, that's just state that exists, whether you read it or write it or, or whatever, it's always there. And, uh, Python has this really cool feature where you can actually internally use functions to, to do that. So we've chosen to use properties, which look like.

**Scott Shawcroft:** There's a lot of words here, Scott. I'm just saying. I know. I'm sorry. Yeah. Um, this is like, this is like your Google or internally. You're like, oh, everything's an object, right? Yeah. Everything's a bike lane. Let me, let me, let me think about it. So. Well, okay.

**Chris Gammell:** So you're saying, okay, well. So, so say we have a temperature sensor, right?

**Scott Shawcroft:** Perfect. I love tangible examples. Yes.

**Chris Gammell:** Yeah. Let me ground it. So the way that we've written our drivers, which we have like 70 now, um, is that for all of our temperature sensors, the object for that sensor will have a dot temperature property.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Um, and under the hood that is running a function because it's actually got to go out over I squared C, you know, set some registers to maybe do the, to do the reading and then read

**Scott Shawcroft:** the value back. Got it. Okay. So I call, I call this object. I say sensor one. I say, you just say this new thing is sensor one, right? Yep.

**Chris Gammell:** And then you say sensor one dot temperature. Right. And that's how I can go. And as if you were reading X. Right.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Yep. Cool. Um, but that has a slight overhead to it, which, uh, micro Python has chosen not to.

**Scott Shawcroft:** Oh, interesting. Okay. All right. So it's kind of just, it's saying it's a style thing. It's like a laundry list of what is capable so that you, it, so it's a little bit friendly you're saying for users because now they would expect that every time you call a new sensor that it would have a dot temperature. Right. Right.

**Chris Gammell:** Right. Not only is it the same, but it's also, we're, we're choosing to be explicit and saying, this is state. This is something you can read. Oh, okay. But it's also something that just is there.

**Scott Shawcroft:** So why doesn't micro Python do that? Because I mean, again, because people were listening last time, hopefully to Tony. Yeah. And I think he talked about some of this stuff.

**Chris Gammell:** I, it's been, um, micro Python's audience is, I understand it is more technical, uh, folks. So one, one feature, Damien George is the creator of micro Python and he did an amazing job, um, because Python is complicated and getting it running on a microcontroller is really hard.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Um, so the Python, you got to know what to cut, right? Yeah. So the Python core is really, really strong. Um, but the APIs around it, um, have made some decisions to be slightly different from the way that you would do it with normal Python, um, in order to be faster. Um, so that's more of their priority is being fast. Got it. So using, not using properties as one example of, of something they choose to do to be, faster. Um, they also allow you to do like inline assembly and interrupts and stuff like that. And, and we haven't even turned it on for circuit Python. Got it. Okay.

**Scott Shawcroft:** Um, well, let's talk about the, the hardware. So I, when, when I heard that Adafruit was doing, uh, circuit Python versus micro Python, I had heard or read or talked to someone about, I, uh, I thought it was because of the hardware focus of it all. But I actually like this mission based of like, I like, I like this. It's, it's more like, I mean, Adafruit obviously has a very large portfolio of, of, of products now as well. Right. And I think that making it a very pleasant experience within that portfolio makes a lot of sense. Right. So, um, whereas micro Python's like, well, you know, come as you are, whatever, whatever devices are out there, we're going to try and make it work for all of them. But there's obviously a lot of hand wringing that goes along with that because you get a new device and you're like, Oh, well got to redo it for this one now. Right.

**Chris Gammell:** Yeah. So, I mean, the fork was originally just created because we were doing Sam D work. Uh, um, and then when we, when I started talking with Damien about, you know, the hardware API, the thing that the, that the drivers are built on, it wasn't clear to me that there was a consistent story across all of the boards that they supported. Like the ESP 8266 was one.

**Scott Shawcroft:** Yeah. All right. That's specifically when I used and I was, I think cause Tony told me about it and it was like, yeah, a bunch of this stuff just didn't work in there.

**Chris Gammell:** Yeah. Yeah. So they have a, an API called machine and it was not uniform across the different ports, which is ports is their term for different microcontroller families.

**Scott Shawcroft:** Right. Right. So using micro Python would feel similar if you're looking at the code, but if you took the code from your 8266 and you tried to put it onto a STM 32 wouldn't necessarily work. In fact, probably wouldn't work.

**Chris Gammell:** Yeah. Well, other way around. There was no guarantee. Yeah. Yeah. There was no guarantee. And so one of the things that, that I did early on, um, with circuit Python was, uh, it's a software engineering thing, but the idea is that the API is shared, like the code that implements the API is shared. Um, so the, the way that circuit Python works under the hood is that it's all C code and there's just structs that represent objects that you can use from Python. And so what I did is I factored that out of all the ports and made, and therefore it's uniform across all of them. And then that code just calls other C code that is port specific.

**Scott Shawcroft:** Um, okay.

**Chris Gammell:** This is, I, I know I'm out of my element, but okay, well let's do a little hand waving

**Scott Shawcroft:** and yeah, that's good. Yeah.

**Chris Gammell:** So the, the goal was that we, one thing Adafruit does really well is drivers and, and guides tutorials.

**Scott Shawcroft:** Yes.

**Chris Gammell:** And we wanted to ensure that we had a foundation that was uniform across all of the places we could bring circuit Python.

**Scott Shawcroft:** Yeah. Uh, right. Especially for longevity of those guides, right? If you want to make a guide tomorrow, you don't want to have to rewrite it. The guide every time a processor changes or whatever, right?

**Chris Gammell:** Yes. Right. So, so we want to be able to bring it like early on, we had Sandy 21 and ESP 8266 support. Yep. Um, we just added Sandy 51 support in our three O, which is in alpha. And we're also adding NRF 52 support at the same time, um, which is going to be super awesome. And adding those, that support for those new architectures is actually easier because the Python side, the Python to C side doesn't need to be redone. We just, you implement some C functions and you get the Python side for free.

**Scott Shawcroft:** So you're basically in C, you're kind of fitting different puzzle pieces together, but you're creating like an in-between layer with C code. Is that right? Right.

**Chris Gammell:** So, so if you say import digital in or digital IO, right, that maps to a table in C that says like all these names go to these other structs. Right. Yeah. Right.

**Scott Shawcroft:** And here's where they're, here's where they're pinned, physical pin locations are.

**Chris Gammell:** Yeah.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Yep. So that's all just like C structs under the head.

**Scott Shawcroft:** Cool.

**Chris Gammell:** So I write more C than I actually write Python. Well, someone's got to do it and I sure as hell learn. Yeah. Yeah. I mean, that's the whole goal is that you don't have to worry about it. But I think something Tony did touch on is that like for people who feel that it's too slow, there is that avenue for you to write C that can hook into the Python.

**Scott Shawcroft:** Yeah. And, and, you know, I think I talked to Tony after the fact about that because I remember thinking like, oh, well, like how would I go and take this, say I did have a new processor and I, what if I wanted to port to that new processor, what would it take? Right. That did, I mean, I looked at it and I'm like, oh, I don't think so. Yeah. I mean, that's, that's what your job, that's what you are doing your job and Tony's job and Lamore's job and like everybody who's doing this stuff. That's what you guys do. Right. I mean, like.

**Chris Gammell:** We don't do new platforms that often. The Sam D21 has taken us pretty, pretty far. But yeah, Dan Halbert and I are, are currently working on the Sam D51 and Kevin Townsend and HotTac are working on the NRF52 stuff. Wow. Yeah. Which.

**Scott Shawcroft:** I'm just saying that's a lot of, that's a lot of, you know, hours it seems like. Oh yeah. So like a new platform is not like a small thing. And, and I, for some reason I thought like, oh, well, it sounds like it's, you know, this is, but the, the implementation layer in each, uh, on each new platform is, is the tough part.

**Chris Gammell:** Yeah. And we're trying to like share as much code as we can between, um, different ports to make that easier. Yeah. No doubt. No doubt. And we're restructuring to make that more feasible in the future as well. Cool.

**Scott Shawcroft:** Um, so what about the, so, okay. Because it's a hardware world, right? Uh, so if there's a Sam D, let's say 51, right? Yep. I don't actually know anything about that processor, but, um. It's awesome. I'm sure it is. Uh, but say it's a 32 bit part and then there's also. It's a Cortex M4. Okay. But say there's a 32, sorry, not, sorry, it's a 32 bit. I meant 32 pin. Say there's a 32 pin part and a 48 pin part. Yep. What is the, what's the swaparoo? Like, is it, is it as hard to go from those, between those families of parts? No, it's super easy. Okay. So that's just a remap.

**Chris Gammell:** Yeah. Okay. Yeah. We, uh, for the ports, we just have a table of all the possible pins. And then when you have a board with a particular, uh, package on it, you just say like, I'm going to say that I have a one on this board and it maps to this, this one internally to the microcontroller. Okay. Uh, makes it really easy. And the code's written in a way that it's just, it's like, Oh, you want to do digital IO on that? Like we can do that or we can't do that.

**Scott Shawcroft:** Yeah. Okay.

**Chris Gammell:** So that stuff is easy. New supporting new boards is really easy. So like the itsy bitsy M zero express came out recently and the hardest part of supporting that was like the new spy flash chip that was on it.

**Scott Shawcroft:** Got it. Got it. Okay. Well, you mentioned there's a bunch of, there's 70 plus drivers. Oh yeah. Does that, does that mean then, okay. So does that driver, uh, so now let's, we're going to just assume that the three parts that you mentioned are out at the 20, the D 21, the D 51, the, the NRF 52. Yep. If you, if you were to drive, if you write a driver now, is it, is it approaching the same place where you have a driver for like the, like a DHT 11 or a 21 or whatever, a temperature sensor? Does it just work on all of them? That's the goal. I mean, like, is it, is that like, I mean, yeah, I know it's a mess right now, I'm sure, but like, uh, or not a mess, but like it's a challenge. Most of the time it's true, I would say. So it's almost like you guys are making like a mini Linux for like, cause again, there's a callback to previous episodes when, uh, Jason Kreidner and, uh, uh, geez, Robert Nelson were on, right? I, I, I was kind of out of my element there. So, um, yeah.

**Chris Gammell:** You could think of it as another platform like that where it's, there's a standard API that you can build drivers on. Okay. Um, Linux has that and cool. We do too. Yeah.

**Scott Shawcroft:** So what about for the people out there that are like, ah, but I need it to be fast or I need it to be low power or whatever. So, right. So I'm sure you get that stuff a lot too.

**Chris Gammell:** Yeah, it does come up. Um, and I would say circuit Python may not be for you. Um, there are other good example or like Arduino is better about power and speed and micro Python is better as well. I would say, um, you could take a look at those, but I would also say don't optimize too early. Like make sure that that's what you actually need and make sure that circuit Python's actually too slow.

**Scott Shawcroft:** Yeah. Okay. Okay.

**Chris Gammell:** Because you're going to save a lot of time in the iteration cycle. Yeah.

**Scott Shawcroft:** Right. And that is kind of like a top down idea as well, right? It's like, you're, you're just trying to get the function to start with. You're just trying to get something working and a sensor talking. You're trying to get whatever. Yeah. Yeah.

**Chris Gammell:** Yeah. Lamore was just telling me yesterday that she was, we just launched a new temperature sensor in the store yesterday. And she was like, I wrote the circuit Python driver first rather than Arduino. Oh, nice. Um, which is a huge milestone given that she's been working in Arduino for over a decade, I believe. Yeah, that's awesome. So, so, so to, to have a system where it's easier for her to get going with circuit Python, despite all that history is just so satisfying.

**Scott Shawcroft:** But I understand, I mean, like, and obviously Lamore is doing that, those new things too, but I imagine that anyone using the, you know, like as more and more people start using it as a primary tool as well, that would be another thing where it's like, if it's just a friendlier, friendlier method. Yeah, totally. Yeah. It's, it's interesting in the software world too. I mean, like I, I've leaned on Adafruit for the, uh, you know, for borrowing drivers and stuff like that. And, you know, a lot of people out there. So, um, I, I do wonder like, you know, writing drivers in, in your mind, is it tough for easier or whatever?

**Chris Gammell:** Um, there's always corner cases that make it hard.

**Scott Shawcroft:** Uh-huh.

**Chris Gammell:** Um, that's another thing. So my background is software engineering. So I like to think about how to make it easier. Um, one thing that I've kind of played around with that we don't do that much in our drivers, but is, uh, making it very easy to just say like the temperature is this register and then it just works. Um, we're not there yet, but we're getting there. Well, I just think about, like in your Python code, you just map like names to registers and that's it.

**Scott Shawcroft:** Interesting. Yeah. Cause I think about like when I've done the, the limited stuff that I've done in C, uh, you know, like the, you know, usually I am setting up like data structures, right? You're have this pretty tight loop. So like in Python, are you setting up like, you know, eight bit variables and stuff like that? Or is it just kind of this loose, are you just saying like everything's afloat, you know, is it like that?

**Chris Gammell:** Um, um, Python actually has a really great library called, or module called struct, uh, which is, comes out of the fact that desktop Python is very well integrated with C. And all this does is it takes a string of bytes and you can tell it like what C type it would be and it'll unpack it in as if it was packed by C. Oh, cool. Okay. Um, so if you have a 16 bit unsigned register, you just pick the character that represents a 16 bit unsigned register and you'll get a Python int back.

**Scott Shawcroft:** Um, okay.

**Chris Gammell:** So it makes that interpretation really easy. Okay.

**Scott Shawcroft:** Neat. All right, cool. Yeah, that's great. Um, so what were we going to talk about otherwise though? Oh, okay. So you're doing, uh, so you're, so now you have to take all this stuff and implement it now on a ARM processor, which is really the reason that I was gnashing, wailing and gnashing my teeth last week as well. Cause I'm doing, I've got this debugger. I want to be, I'm trying to get better at firmware and I want to do some debugging and you have to do that too, obviously. Oh yeah. So, so maybe walk us through like, so you're, you're loading this stuff up on a daily basis onto a CMD 21 and then debugging it directly. Is that the idea?

**Chris Gammell:** Yeah, I tend to. Okay.

**Scott Shawcroft:** Um, can you walk us through some of your, some of your steps if you're firing it up for the, for the morning, in the morning?

**Chris Gammell:** Yep. Sure. So, uh, we use make to compile, so I will make clean and then I will rebuild it. And I'll also start J link GDB server. Uh, so I have on my desk, uh, J link connected to the SWD port that's on a Metro. I'm just straight up looking at it. Um, I also have a nine volt, uh, barrel connector with a switch on it. So I turned that on as well. And then I, I'll fire up GDB with the, with the binary as an argument. And then I will connect to the J link and I will load reset and run the code I'm working on. Um, the code I'm working on right now actually is a spy flash code. So I actually have a salient hooked up to the spy flash that I just used to understand whether my code is working as I expect or not. Okay. Um, okay, cool.

**Scott Shawcroft:** So yeah, the, is that what you're thinking? Yeah. Yeah. That was exactly what I was thinking. That's great. And I think the, so you and I were talking on email as well about like, so how do you, how do you explain what a debugger is in this case? Mm-hmm. And I was trying to say it's like, it's effective like a serial port into the processor, but you didn't like that.

**Chris Gammell:** Yeah. I think, um, serial port, especially from the Arduino land means text back and forth. Oh, okay.

**Scott Shawcroft:** Yeah. Right.

**Chris Gammell:** I was thinking just more like clock and data, you know? Sure. Sure. Sure. Yeah. I mean, in, on the implementation side, it's two wire. Right. I think, um, I mean, you need a ground for return.

**Scott Shawcroft:** Right. But yeah. Right.

**Chris Gammell:** So, um, yeah, the way that I was, I was saying, I think about it is that it's basically controlling what the processor is doing. So is it stopped? Is it going? Um, can I reset it? So it's, it's those basic primitives. And then you also have the ability of reading memory and memory is a very vast thing. It has the Ram that you have, but it also has the registers of the CPU itself. So you can tell where in the code it is. And then it also has all of the peripheral registers, um, which I've started to think of all the peripherals on a, on a system, on a chip, just as if it was an I squared C device. Right. It's not I squared C that it talks to the peripheral, but it's essentially that.

**Scott Shawcroft:** Oh, like it's like hanging out in the middle of space somewhere. And if you want to talk to it, you need to know what its address is. You're saying. Right.

**Chris Gammell:** You need to know its address. You need to know its register layout. Yeah. Um, the only thing that's a little bit different from that analogy is that it's clocked, right? It's clocked in with a similar clock line as the, as the CPU. Um, but it really is like something that you have to go out and talk to. And then something that can run on its own as well.

**Scott Shawcroft:** Um, Oh, like if you wanted to just let it freewheel and wait for an interrupt from it or.

**Chris Gammell:** Right.

**Scott Shawcroft:** Uh, right.

**Chris Gammell:** Okay. Yeah. And, and that I've been doing a lot of work on the same D 51, which is like the newer version of the 21 and the peripherals are very similar. Um, and so the code that you write because you're just talking to the registers of the peripheral doesn't necessarily change that much. Oh, really? Okay. The addresses are similar and stuff too. Um, the memory map is different. So memory map is this idea of like what memory address is it located at, but the actual register layout, once you have the offset, um, may or may not be that different.

**Scott Shawcroft:** Oh, okay. Okay. Okay. Okay. Oh, yeah. So you're saying the address space might be wider, but the, it's pretty similar to you just change the address and you're like, Oh, it's like you moved your house down the road instead of changing the layout. But the house is the same shape. Yeah. Right. Yeah.

**Chris Gammell:** Or maybe you just bolted on a garage, but the rest of it's the same.

**Scott Shawcroft:** Right. Yeah. You can still go walk through. It's still the same. Yeah. That's, that's, that's good analogy. I like that.

**Chris Gammell:** Yeah. Yeah. And it's the same way as if you took a I squared C temperature sensor and hooked it up to your, you know, M zero or your ESP 8266. Like the temperature sensor didn't change at all.

**Scott Shawcroft:** Right. There might be a new version of it, but you didn't want to break the old version. So you didn't change the base functionality. Right. Okay. That's good. Um, I mean, how much, how much of the, so the, the debugger is, is like you're saying, you said there's, you know, there's like play, there's stop, there's, you know, you can go and read stuff back out. Right. How much, how much of that are you utilizing on a, you know, like how much do you need to do break points in this stuff?

**Chris Gammell:** Well, so break points you can think of as something that's a special way of stopping. Right. Um, a lot of the time, well, a lot of the debugging I've been doing recently, I'm not actually hitting a break point. I just have a loop that's looping until a register is a particular value, right? Like I'm doing DMA and I'm waiting for an interrupt to happen and I'm checking for the interrupt by just reading a register and the DMA is not working. So I just control C and I'm stopped. So I haven't, I didn't do a break point to stop there. Um, but yeah, break points are a special way of, of picking where you want to stop when you get there.

**Scott Shawcroft:** Okay. That makes sense. Yeah. I guess, I guess in that case though. So I feel like, I feel, I feel like a little guilty here. Like, cause I'm like, I'm, you know, I'm obviously doing a little bit of my own learning as I ask you these questions and I've talked in the past weeks too. And I, I feel like I should know some of this stuff. And then I also feel like a lot of this stuff should be on the embedded podcast, but I feel like hardware people need to know this stuff sometimes. You know, I, I speak for the hardware person.

**Chris Gammell:** Uh, and I'm, I'm like, I'm a software person definitely by training and I have picked up some of the hardware stuff.

**Scott Shawcroft:** Cool. Um, but in this case, like, okay, so say, say you, so you're waiting for an interrupt and what, and, and what have you, but, uh, it's never going to come cause it's broken. Oh, okay. Say it, say it did show up though. Uh, so you, I mean, yeah. So an interrupt is basically just like a, a, a bit in an internal register of the processor, right? That flips from a zero to one or whatever. And then it goes off and does its routine. Right.

**Chris Gammell:** Right.

**Scott Shawcroft:** But who's actually, it's not polling for that. Right. Or is, is the debugger actually polling for that?

**Chris Gammell:** So the, my code. Um, so there's two places an interrupt can, I'm Sam D 21. There's two places interrupts can live. There's, uh, interrupts that are on the peripheral side. And then those interrupts might get, um, joined together to have one interrupt to the CPU. Um, and then the interrupts to the CPU, uh, the CPU says, Oh, I have an interrupt and I need to run this other piece of code instead. And that's just a table somewhere in, in memory that it looks it up when it, when it happens. Um, and so it'll pause your code and then I'll jump to where that interrupt table points to. And then in there, your code has to say like, let me clear the interrupt so I don't get called immediately again. Um, otherwise you end up in an infinite loop.

**Scott Shawcroft:** Right.

**Chris Gammell:** Yeah. There's like an interrupt routine you're talking about there, right? Correct. Yeah. Yeah. Yeah. It's also abbreviated ISR interrupt service routine. Okay.

**Scott Shawcroft:** Um, so, but, but the, the, in the case of the debugger though, is the debugger sitting in the ISR and looking at that or is it? No.

**Chris Gammell:** So the, the ISR or the debugger in, in my mental model is just like, it can pause the CPU or it can tell the CPU like, Hey, when you reach this code, pause or stop. Right. And so when you set a break point, the GDB side of the debugger, the, the code on your, on your computer says, Hey, you wanted this like particular function. What, um, program counter is it at? And then the debugger says, Hey, CPU, when you hit this program counter, stop, please. Okay. Um, so it doesn't have anything to do with the ISR, although you could say when the program counter hits the, the address of the ISR, stop.

**Scott Shawcroft:** Well, I guess the reason I asked about this too, is because I was, I was actually, so as I was troubleshooting my clock pin being plugged into the wrong pin, uh, when none of my debugger working.

**Chris Gammell:** You learn a lot, a lot of other stuff in the meantime.

**Scott Shawcroft:** Right. I was like looking at it and I'm like, Oh, okay. That obviously there was a clock and a data signal going back and forth with the debugger and like, they kind of, some of the stuff felt, you know, fell into place. So I do recommend plugging things into the wrong place sometimes. Excuse me. Um, like you have a choice. Right. Exactly. Uh, so, but in this case though, what I'm, what I'm really asking, I guess, is what is physically streaming back out of the processor and then who is controlling things? So, okay. So we're, let's go to that case where we're now setting a, a break point, right? Mm-hmm. Is it streaming where the code is like in a, in the counter? Is that what's streaming back out? I don't, I don't believe so. Okay. So how does it know when to stop though? That's what, that's what I'm really saying. Like who's the brain, who's the brains of the operation here?

**Chris Gammell:** Well, so the, the debugger, like GDB on your computer is the thing that figures out. You said this function and I will interpret it into this number for the processor. And then you'll see that the, the processor, like the same D 21, the cortex M zero plus supports four hardware break points, which is four 32 bit numbers that represent the code that it's executing at any one point. And every time it executes, it's comparing against those four numbers. And if it hits that four numbers, it stops like the CPU will stop. And then the, the debugger software, like GDB through the J link can then understand that, Hey, I have stopped.

**Scott Shawcroft:** Okay. So it's not streaming back out. We're at line one. We're at line two. We're at line three. We're at line four. And then it gets to line 7,461 or something and says, Oh now, and now the computer says to stop. Right. It's more, it's counting internally and saying, I just said 761 or whatever they said.

**Chris Gammell:** Yep.

**Scott Shawcroft:** Yep. And then it just, it just, it says, okay, I'm pausing here. Yep. Come and take a look at what's going on.

**Chris Gammell:** Yeah. Tell me what you want to do next. Like, do you want me to keep going? Or if you do something like what's known as a step, you're telling like, do the next line of source code. Yep. And your computer is figuring out what program counter that is. It sets another hardware break point and then continues until the CPU says, okay, I hit another break point. Got it. Okay.

**Scott Shawcroft:** Um, now there's a, because, and sometimes that, that breaks, right? It doesn't like doing single steps sometimes.

**Chris Gammell:** Right. Yeah. Single step can be tricky.

**Scott Shawcroft:** Yeah. Yeah. Yeah. Break points are better for that. I know. I knew that one. Cause, uh, yeah, I've, I've definitely had problems with that in the past.

**Chris Gammell:** Yeah. And that, I think that tends to occur if you don't have your entire source code, if your code goes in somewhere that it didn't know it could, like, uh, we have a bootloader on our boards and if you go into the bootloader, but the GDB didn't know about the bootloader that can get tricky. Okay. Okay. Interesting. Yeah. So there are like advanced J links where it does actually stream data back the J trace and all of that high end stuff. But, um, in general, that's not something I use day to day.

**Scott Shawcroft:** Right. Well, and I was thinking even with, uh, I mean like this, like you could set how fast the, the serial can actually talk between like the, over the S the single wire debug SWD. Right. Right. You could say it's default four megahertz, you could say a hundred kilohertz and it won't care. Right. But it's, it's gonna, not gonna be able to stream data back as fast or at all really. Right. So, okay. So that, that makes a lot of sense actually. So then, so basically the GDB server is running on your computer. Yep. It's talking through this hardware chip, the SEGGER hardware chip on the J link. Yep. And that's basically translating it to some kind of serial thing. And then it's going in and saying, all right, I know where to talk to in these, through this quasi serial port. It's saying, go to this location, set this, set this, uh, you know, this rant, this weird number. And that's where the code's going to break. Yep. And, uh, and then, and then we can go and poke around inside. Right. Okay. Right. Any idea how it's actually, so it's like, it's like special access into the, into the processor at that point. Right. Yeah.

**Chris Gammell:** Like the debug hardware, if you've ever looked at a diagram for MCU, it's like right next to the actual processor.

**Scott Shawcroft:** Yeah. So it's like, it's very integrated. Yeah. You get to like see everything. Uh, which is also why all the hackers are always looking for the J tag port. Oh yeah. I was just talking to Joe grand the other day with his J tagulator. Uh, uh, uh, yeah. So they love that stuff because it is your, you get to be right there and you can poke around.

**Chris Gammell:** Yeah. You're, you're controlling the processor and you're able to read all the memory.

**Scott Shawcroft:** That's pretty cool. Yeah. Um, okay. This is helpful. Good. So, uh, you have a great tutorial about this too. So it's kind of showing a lot of what we're talking about here. Yeah. Debugging the Sam D 21 with the GDB. Yep.

**Chris Gammell:** And that, that, uh, tutorial was kind of inspired by my, um, talking about tracing. So like keeping track of every program counter, uh, that tutorial was written because I had figured out how to use, uh, an optional feature on the cortex M zero plus.

**Scott Shawcroft:** Uh huh.

**Chris Gammell:** I think it's optional called the micro trace buffer. Okay. And what it does is every time the program counter. So a code executes by just having a program counter that says I'm executing code at this address. And by default, every cycle of the CPU, that address increments by a fixed amount, right? If it's 32 bit processor, it will go four bytes more. Um, but if you have a branch, which is like an if statement, um, it might not go to that next line, that next address. Instead, what it's going to do is it's going to load a different address. Um, and so what you can do is you can tell where your code has been. If you keep track of all of the branches that you took. So the micro trace buffer says I was here and now I'm jumping to this other part. It's a history of where your processor, what code your processor is executed.

**Scott Shawcroft:** And that's kept on the, on the device instead of like in the computer.

**Chris Gammell:** Right. So the, right. So the micro trace buffer is a little piece. It's a little peripheral that can actually write to Ram. So you just say like, here's my Ram address that I want you to keep this buffer in. And then you can go back and read it. How much can you keep in there? It, you can change it. I think I had like 256 bytes. Okay. Um, so then a couple, a couple branches. Well, well, no, one branch is eight bytes. Cause it's two 32 bit numbers. Oh, okay. Where you were to where you're going. And that's, that's all it has. Got it. So you get about eight steps in eight steps.

**Scott Shawcroft:** Yeah. No 32 steps, whatever. Yeah.

**Chris Gammell:** It's not that many, but it's usually enough to like, it's really handy if you end up in a hard fault handler or something and you want to know why you got there.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Um, you can actually basically see the history of where you are. Um, and that guide includes links to a Python script that you can use in GDB to actually tell you like a line, like source code line numbers for all of those addresses.

**Scott Shawcroft:** Okay, cool. All right. So let's, let's, let's zoom back up a little bit here. Yeah. So, so the good thing. Community at some point too. Oh, definitely that. Um, but on this side of things. So, so one of the things that, okay. So let me step back on my stuff. I came from the world of IDEs, right. And this was like, again, back to that episode with, uh, the BeagleBone guys. Um, like I, I just don't do like make file. I've not done make files and all that stuff. Yeah. And that's something I'd like to work towards for sure. Yeah. Um, but I come from the world of IDEs where you, you know, you basically, you download the whole tool chain from one vendor and you just hope to God it works and, you know, and if it doesn't, you call someone and they help you, right. Or you have coworkers. Yeah. Um, and so my tact has been like, I want to like learn this other stuff about Eclipse. So I have this stuff, but even so it's like Eclipse is like a IDE is basically just a text editor with some hooks into stuff like GDB and everything else. Does that sound right?

**Chris Gammell:** Yeah, I would, I would say so. Um, it's, uh, IDEs are integrated desktop environments, right? So they're trying to integrate all of the, your workflow into one application. Right.

**Scott Shawcroft:** So, so can you tell us how, how you're using this stuff? So, so you said make files. So the make file basically does the compilation and does the linking and does the, all that stuff.

**Chris Gammell:** Yep.

**Scott Shawcroft:** Yeah. So I tend not to use IDs. Right. But, but then what? Right. So then you start the, you start the server, the GDB server. Right. And open OCD as well.

**Chris Gammell:** Well, there's the J link GDB server. And then I use GDB proper to connect to that. Um, which is just like the GDB prompt command line prompt thing. Okay. Which is, I think in the guide, you can see it there. Yeah.

**Scott Shawcroft:** Okay. And we'll definitely link people there. But I guess, I guess the whole thing that I think about is like, so like even the IDE world, right? It, it, it kind of felt like, like FPJs do this a lot as well. You know, like there's all these command line tools underneath and the IDs are basically calling these tools. Yep. And, and, and. Yep. And The Amp Houring thing is like, you can call them yourself, right? Yes, totally. And in different orders. Yep. But that's also a little scary.

**Chris Gammell:** Yeah. I think it takes, I think as a software person, command line is not that scary. Um, I think you see it more there. Um, I've definitely felt coming, coming into the hardware world as a software person, I kind of feel that the hardware world's a little behind in terms of software engineering. I would agree with that. Yeah. Yeah. Um, maybe I should pick on Atmel just a little bit.

**Scott Shawcroft:** Um. Like on their, what, with their, uh, the, the studio thing they have, the.

**Chris Gammell:** Well, yeah, I don't use Atmel studio at all, but, um, just the, the, like maybe CircuitPython is very different than other hardware projects where if you're making a toaster and you need the microcontroller code to do one thing, a wizard that says like, how do you want to set up all the pins and then spits out code for you is really great. Um, but we're not that at all. CircuitPython is very, very dynamic. Like we don't know the code that the user is going to write and we don't know what pin they're going to want to use for something. And so we're, we're much more in this model of like, we just want to download the USB code and use the USB code. We don't want to have to run a wizard every time we want to update our USB code. Yeah. Um, and that's the, Atmel has Atmel start, uh, currently, which is definitely that model. And, and we've run into that because the SAMD 51 is only supported through that. Oh, really? Yeah.

**Scott Shawcroft:** And I mean, that's like what the STM 32 cube is, I think too, right? Like that's like, they're like these, there are these interfaces. They're wizards.

**Chris Gammell:** Yeah. Yeah. I feel like that was something the software world already grew out of. Um, but that's my bias.

**Scott Shawcroft:** Okay. So that, well, no, here's, that's interesting. So, so what do you do instead? I guess that that's probably the best thing. Cause I'm sure that some of our people listening, like they're at least used to wizards. If not, you know, they like them.

**Chris Gammell:** So I, I think the answer is something that Lamore realized long ago. It's good examples and good documentation. Um, the frustrating thing that I have when I'm using at my start to pick it on a little bit more is that I'm working on DMAing QSPI and I can't find an example. What I end up doing is I end up going into at my start and I just get a dropdown of all of the register values essentially. Right. And that doesn't help me. I can read the data sheet and understand the individual registers, but I don't have an example of how I actually want to use it. Um, so I think that.

**Scott Shawcroft:** I do like that. No, I, I like that. Like, you know, the, the example, obviously that fits well with my mindset as well. It's like most people can take that and then, and then, you know, make it extensible to whatever they need to do. Right. It's not gonna be a hundred percent of course, but there are almost infinite things you can do. So at least an example gets you one. Right. Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. And the more examples you have, the more starting points people have. Um, and I think that's something that Adafruit's been excellent at from the start and something that we really value. You'll see like all of the products we release have, um, for the circuit Python stuff, we have API reference docs, but we also have guides and tutorials as well. Um, I think that a wizard is an easy answer to that problem of how do you get people started? Um, but I don't feel like it actually helps that much. Right. Cause it kind of hides the, the actual thing that's happening. Right. It just puts a different, it, it's asking you all the same questions in a different way. Hmm. And this is kind of how I feel about an ID as well as like, you still need to understand what a break point is, whether you're clicking a button next to the line of code you want to break point or whether you're just typing it into a command line, uh, doesn't change the concepts that you have to understand.

**Scott Shawcroft:** Yeah. Like, so it's, it's almost like, so what do you think they're like, they're so the hardware, uh, the software that made for hardware people then is like, is basically removing responsibility or what do you think? I mean, like what, what is, what is that method that they're doing?

**Chris Gammell:** Well, I think, I think a wizard is a reaction to understanding that people don't understand it right away. Um, but not understanding how to teach it. Yeah. Um, I think like teaching, teaching people to program is really hard. That's something that like all of our circuit Python docs have, have been iterated on a number of times already. And that's something we continue to work on. Um, so it just, it takes time and effort to make good docs, but good docs are what are going to put you ahead. Yeah. Sorry about that. That's my shade going up. You have motorized shades? Automated motorized shades. Hey, all right. It's getting dark. So it's opening it up.

**Scott Shawcroft:** Verified nerd.

**Chris Gammell:** All right, cool. Yeah.

**Scott Shawcroft:** Nice.

**Chris Gammell:** That's kind of how I got into Adafruit actually was doing home automation sensors. Oh, nice. Okay. Mm-hmm. Cool. Yeah. I hope that's, I don't mean to dump on Atmel too much, but I think.

**Scott Shawcroft:** No, no, no. I think, I really, I think it is an interesting, it's a, it's a software person looking at, the state of the hardware slash firmware industry. Yeah. And it's, it's interesting because, well, first off, I mean, like it or not, more software people are entering the hardware than ever, I think. Yeah. So it's going to happen more and more. And if people don't, if the tool makers don't react, then other people are going to react, obviously. Mm-hmm. Mm-hmm. So it's, it's good to know. From a hardware perspective coming the other direction, I've been confused no matter what. So if there's a better way to do it, like bring it on, man. Like. Yeah.

**Chris Gammell:** Yeah. And it's always good for people to try different, different ways of doing things. Like a lot of our more modern boards, the MZeros also support Microsoft MakeCode, which is a block-based code editor. And that's a great way for other people to get started if they're intimidated by text editing.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Yeah. Yeah.

**Scott Shawcroft:** Well, like, I mean, like Dave always says that, right? So Dave always says, don't, I, he doesn't want a text editor. He doesn't want a command line. That, that is just not what he expects. Right. And I think, especially like, you know, a lot of the, the interesting distinction for me is that like, there's a lot of people that come from like the microchip pick world, right? And pick was one of the first ones that felt like to make it really easy for people, but it's also its own flavor of things. So now anything outside of that, it's like, oh, well, this. What's that? Because it's not arm.

**Chris Gammell:** Uh, what do you mean? Is that why it wasn't hard or? Or why it's a different flavor from other, other MCUs? Oh, um, this is where you're getting me out of my element.

**Scott Shawcroft:** Cause I, I've never used a pick like. Oh yeah. A pick was just like a, you know, it's like a, I think it was a slightly abstracted hardware, where, you know, like, um, yeah, I guess I'm out of my element too.

**Chris Gammell:** Well, I think maybe what you're getting at is that it's just what it was well documented and, and within the pick ecosystem, if you used spy, for example, you knew how it would work.

**Scott Shawcroft:** Yes, exactly. Yeah. I think, yeah, there was the pick way of doing things. And now recently I went over and I tried something. I'm like, oh, I don't even know what I'm looking at either. Right. It's like, it's basically what you get used to. And yep. That's not right or wrong in any case, I think, right? Some people that like the Microsoft stuff you mentioned or, you know, the wizards or whatever, some people are just used to it. And I think it's just about, um, you know, having more options for people.

**Chris Gammell:** So. Yeah. Yeah. The challenge is when you, when you do it as an expensive other things, like, yeah, I would love more example code from. Right.

**Scott Shawcroft:** Well, like you said, like the new, the new parts that are only available in this, you know, in the wizard format. So yeah, that, that does happen. Um, so before we talk about the community stuff, cause I would like about talk about that too. Um, just to take us a little bit further down the road of, of how you're using this. And if you could do it specifically from the realm of, I mean, you reporting some of this stuff. I don't, I don't still quite understand how the virtual machine works. And yeah, I don't either. Oh, okay. We skip that then.

**Chris Gammell:** The point, the point is, is that I don't need to know the intricate details of how the VM works because that's something that works across all of the microcontrollers in the same way.

**Scott Shawcroft:** So how does that, how? I don't, yeah, I guess I don't understand that. Like what is, what, like you said that that stuff gets loaded into flash, right? The virtual machine code that runs it is loaded into flash.

**Chris Gammell:** Yep.

**Scott Shawcroft:** But then what?

**Chris Gammell:** So like it just, it's written in C? Yeah. It's written in C. We call a function that says, Hey, run this file for us. And it does. Is it a binary or is it a? Uh, you could, well, the file itself is, is text. Okay. So it will parse the text and then run it for us from the outside. So why does it work on every processor? That's, um, well, it's C code. So as long as you could compile it across them.

**Scott Shawcroft:** Um, but who's, so when you, when you install it though, that's what I mean. So like is, it's not, it's not machine code. So, so the V the VM is machine code. Oh, it is. Okay. The VM interprets by code. Okay. So the VM is, is machine code that's loaded into flash. Yep. That acts as a little engine that can then. Correct. That does the interpretation. Yep. Okay. So who compiles the VM? Is that, that's done on a computer somewhere? Yep. And it says I'm targeting a Sam D 21. Yep. So use that Sam D 21 compiler. Yep. To take the C code and make machine code.

**Chris Gammell:** Yeah. You go to GitHub slash Adafruit slash circuit Python slash releases and see the latest release. You'll see a number of files for different boards there. Okay. Um, like you can download the, you said you like the trinket. So trinket M zero, and that will be the binary format for, uh, that will be the machine code that has all of the VM and, and all of the data structures to tell you what pin is what and all that.

**Scott Shawcroft:** Okay. So if I wanted to go and configure for a new part or a new board, I'd have to mess with that stuff if I was so bold. Okay. Yeah. So you pile it down, load it onto there. And then, yeah. And I think I actually did this at one point too, cause I, I had taken my circuit, my trinket M zero. I had put the, I had, I had taken the circuit Python stuff off of there and I, or not, I'd taken it off there. I just loaded a new, uh, a new bit of machine code into flash using the, the Arduino. Uh, yeah. Okay.

**Chris Gammell:** Yeah. People ask how to uninstall circuit Python. And the answer is you just write your Arduino sketch over it. Yeah. Right. I figured that out eventually. Okay. Yeah. Yeah. Maybe we should say that explicitly.

**Scott Shawcroft:** Yeah. That's good. That's good. Um, cool. All right. So that's, but, but in, in this case, most people don't need to compile that cause it's already been compiled. So that's why it's in the releases folder. So if you write over it in Arduino, so you're in the Arduino IDE, you load up a new sketch, you mess up your circuit Python thing. You can then go and just load in this new file into flash. Yeah. Yeah. And then boots up, ready to go. Mm-hmm. Boom. Yep. I've got some circuit Python again. Yes. Uh, so what else are you using debugging for then? I guess I was, I was going to ask about that stuff, but it sounds like that's kind of, it's taken care of. So day to day, what are you debugging low level that, so is it like when you're testing out new drivers?

**Chris Gammell:** Right. So if I, so there's a lot of different levels, I guess I would say what, what I was talking about previously is when I'm working on core circuit Python code. But a lot of the contributions that we have to our kind of project and the things that we can do day to day are things that we can just run with circuit Python. Um, we don't need to get the J link out. Yeah. Like if, if we're creating a new device driver, we can just use the I squared C stuff and write Python code and don't have to worry about it. Mm. Like we don't have to worry about the J link at all.

**Scott Shawcroft:** That's great. Yeah. Right. So you make like these, these structural things that you're just done with. Right. And, and then you, you build the tools first and then you use the tools.

**Chris Gammell:** Right. Right. So a lot of the work that happens within like this broader circuit Python project is driver work and, and example and guide work. And that all happens without ever needing to even think about compiling circuit Python yourself on your computer. Right. Or loading it with a J link.

**Scott Shawcroft:** Right. Until you get a new, a new processor type or a new board that has different pinouts and stuff like that. Right.

**Chris Gammell:** Yeah. I, you could, if you had new pinouts, you could probably get away with not using a J link as long as you can load it somehow. Okay. Um, because it's usually not the end of the world if your pinout map is wrong. Um, really? Yeah. Circuit Python has two ways to map pins. One is with the name of that. The board knows that's the board module has like a one, but we also have the, the actual names from the microcontroller itself. So even if you get that board mapping wrong.

**Scott Shawcroft:** Oh, so you could just like make a little map yourself and, and then you just refer to the pin 37 is, is the ADC or whatever.

**Chris Gammell:** Yeah. You can always refer to PA 17 directly if you want.

**Scott Shawcroft:** Are people starting to take, I mean, so are they take, let's just stick with the SamD21. Are people putting a SamD21 on and do a new custom board and then using CircuitPython? Have you, have you been seeing examples about that?

**Chris Gammell:** Yeah. We have a couple people within our community. Um, the ship who, whose name is Radomir. He's, he did the micro game, um, which has been on hackaday. It's kind of Game Boy sized and it's a SamD21. It's basically a trinket, but on a, uh, on a different form factor with a screen. Um, and that's, that's running CircuitPython. He's actually selling those on Tindy. Oh, cool. Um, I don't know if he has them in stock, but, uh, that's one example. Um, I, there's another person on our discord sedacious, um, who is working on their own M4 board. So using the SamD51. So that's been really nice because they're hammering on the SamD51 at the same time we are.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** And they're living on the bleeding edge of what we're doing, which is, which is really

**Scott Shawcroft:** nice. Right. I'm just imagining like a, so like imagining a future where there's more and more parts supported by the, by, you know, MicroPython, CircuitPython, whatever. Yep. Right. I imagine it'd be really nice to have. So I already use like the, the feathers, which is one of the form factors Adafruit cells. Right. So be on a feather, use something like that, refactor, put the exact processor, take that processor, put it on a board that I have, you know, refactor it however I need to drop CircuitPython onto it, make sure the code's working that I've already had on the other board. Yeah. And then eventually as I need to then go in and refactor or then if I need to, uh, you know, save power or, you know, work on my, uh, you know, the speed of my code or whatever. Right. Then I can do it there.

**Chris Gammell:** Yeah. You could make some C code for the stuff that's slow.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Right. Yeah. That's totally possible. I actually, I built a board myself of that's used for a toaster oven controller, um, to replace like the control panel of a toaster oven. Nice. To make it a reflow oven, but it's not done yet.

**Scott Shawcroft:** Yeah. I think it, it sounds like, it sounds like one of the stumbling blocks would be like if someone evaluated or using, you know, using that method that I just explained, the stumbling block would be if you get to the end and you optimize and you optimize and you optimize and it's still not enough. You, that's way too late, right? You've already got this thing on your board. Yeah. So it's like, it's almost like you should, I mean, it's hard to do that at the beginning, but. Yeah.

**Chris Gammell:** Yeah. I would say like, you'd probably find yourself not using the Python slide at all. You'd just end up with a bunch of C.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** And that's okay. Oh, sure. Sure.

**Scott Shawcroft:** Sure. Sure. I just mean that from a prototyping, like it's really, this is all talking about iteration and design as well. Right. Yeah. You know, I, you know, like again, like thinking like top down, it's best to, it's best to start with off the shelf modules, like a feather or something. Right. Um, and just to get the concept working first, because that's usually the hardest thing. Yeah. And if you're waiting for boards to come back, if you're waiting for all this stuff to work, it's like, eh, it's like, you know, like it's like the longer you wait, the longer, the longer you stretch out your decision time of if it, if it's a viable idea. Right. Right. Right.

**Chris Gammell:** Yeah. Well, it's, um, it's a great way to find the things that you do need to optimize to get going. And there's lots of avenues that you can take to do that optimization because it's open source and it's all C code. Yeah. Um, you need the technical skills to be able to do that, but it's possible.

**Scott Shawcroft:** Right. Right. And yeah. And you know, I've talked to people in the past too. I think, I think that over time, you know, and I've talked to, you know, the embedded folks about this as well, embedded FM. Yeah. Um, and you know, I think more and more people are, you know, the, especially people coming up, like they've worked in Arduino stuff before now they've worked in a micro Python or even just Python. Right. And it's like people that need to get down lower into the, into the stack, like, like the kind of stuff that you're doing. Right. I feel like there's more and more need for that. And if people are listening and no more resources about it, I'd be personally interested. But I think also like, that's just a thing that is needed. Right. There's, there's no shortage of need for embedded engineers. Yeah. And, uh, yeah. So yeah.

**Chris Gammell:** And I think circuit Python is a great way to get started because there are those layers that you can peel back as you find that you need to. Right.

**Scott Shawcroft:** And you're, and I think that it'll get more people comfortable with the actual hands on hardware, which is in my experience, like the embedded stuff's fine. But like usually the embed, even a lot of the embedded folks are like, I don't want to mess with the hardware, but it's, you kind of need that crossover piece, you know? Yeah. Hardware is super fun.

**Chris Gammell:** Um, not always, not always, well, I live in the digital realm. I'm, I'm scared of the analog side, but, uh, that's fine. Uh, in the low speed stuff, but yeah.

**Scott Shawcroft:** Okay.

**Chris Gammell:** Um, it's, we all have different demons, I suppose. Yeah. Yeah.

**Scott Shawcroft:** I'll get there eventually. Yeah. No, I think, well, I think like you said, like writing, writing drivers is a, I mean, you're going to, you're going to be hands on with the hardware because you need to make sure the hardware is actually working. Yeah. Um, and like you said, that's a big, that's a big piece of the work. When I think of embedded work that's out there, it is a lot of that, you know, I got a new sensor, I got a new ADC or I got a new whatever. Right. I got to talk to it somehow. Yep. That's what that work is. Yeah.

**Chris Gammell:** And it's super fast to do that in circuit Python.

**Scott Shawcroft:** That's great.

**Chris Gammell:** Um, and we have people like hinting at our community. Like we've asked people to just like, we had a forum user yesterday who said like this temperature sensor is getting stuck at a particular value. And I just, I asked somebody else in our community, like, Hey, can you rep reproduce this? Right. So they're not even creating a driver from scratch. All they're doing is like trying to validate this bug that we found.

**Scott Shawcroft:** Oh, wow.

**Chris Gammell:** And that's super helpful. Cause now I, now I know it's a real bug that I've got to fix. Yep. And, uh, I haven't done it yet, but I didn't have to take it. It was just yesterday. Come on. Yeah. I didn't, I didn't, uh, have to take the time to be able to tell the difference between whether it was a bug or whether it was just a setup issue. Like somebody else did that for me, which is really valuable.

**Scott Shawcroft:** Right. And I think that especially in the, uh, in, I mean like Adafruit serves a lot of, uh, beginners as well. And yeah, it's, it, it's, it stinks when you just chase ghosts. Right. I mean like it happens, right. Of course. But like, it was like, Oh, well, yeah, you, you turns out you, you didn't plug in the battery after all. Right. So, yeah.

**Chris Gammell:** Yeah. And we're, we're trying to build out and really encourage people to help other people to figure out they haven't plugged in the battery rather than having us, us having to do it directly.

**Scott Shawcroft:** Yep. Right. So yeah. Tell us about the community stuff. I mean, what is, what is, what is this mystical forum slash chat that you talk of?

**Chris Gammell:** Yeah. So, um, it's been really interesting for me personally, because when I first started working with Adafruit, it was simply port this to port microbytes on those AMD 21. And it wasn't so much about thinking of circuit Python as a larger project. At some point we decided to rename it. That was like January of last year. It was like, okay, you know, I think we're going to take, like, take it in our direction and not try to, to merge explicitly back with micro Python. So we'll, we'll call it something else. So people don't get it confused. And, uh, at that point it was like, okay, well, well, how do we define it? And we talked about this before of, of being really easy for beginners and prioritizing that even at the expense of other things. Um, and then we also said like, you know, we want to do the same thing. We want to be just as deliberate with the community that we build around it. Um, I had seen what PyCon last year, there was a lightning talk that said, Hey, the Rust community is really, really strong. And out of that, I found these, uh, really great videos from, uh, E Dunham. I think her name is Emily, uh, talking about how to automate your community. And, and she meant kind of two things by that. One is, um, setting expectations for behavior in your community upfront, uh, using a code of conduct. And that's automating in the sense of you already set expectations. You don't need to manually set them later. You may need to enforce them, but you don't need to set them. Um, and then also things like, uh, automating the, some of the menial tasks when it comes to issues and pull requests and things like that. And, and we've done a little bit of that within circuit Python, which is like we have, when somebody proposes a new file change, we'll automatically make sure it's fits within our style. If it's a circuit Python change, we'll make sure it automatically compiles. Um, just those, those basics that sometimes people miss. Um, so the rest can be.

**Scott Shawcroft:** It would suck a bunch of time if, if, if you accepted it and then you're like, Oh, I got to read it. I'll just do it myself. Right.

**Chris Gammell:** Yeah. Yeah. And, and having that mentality as a maintainer, like I was the first person to maintain Adafruit circuit Python and really having that, that mentality of people coming in to the project are assets. They're not burdens. It may sound simple, but some people see those other people coming in as burdens and, and want to avoid interacting with those people. And, um, while it does take. Right.

**Scott Shawcroft:** You're like, you're like assuming success versus assuming failure. Right. Right. Right. Right. But you set a standard for that success. You're like, well, I'm sure they'll be successful because I said it has to, tabs, not spaces or whatever. Right.

**Chris Gammell:** And it's, yeah, that's a whole nother thing. Tabs versus spaces. Like automating style is really valuable too. Um, because if you.

**Scott Shawcroft:** Did you see, did you see what Bill Gates said? I don't know if you saw. Not recently. He had an AMA recently and he answered. I'll link it. I'll link it in. People can find out. Tabs versus spaces. Bill Gates weighs in.

**Chris Gammell:** I, what I would say is it doesn't matter either way, as long as you have it automatically, uh, found out and, and reported for all code changes.

**Scott Shawcroft:** What I'm really wondering is when's the last time Bill Gates wrote code? That's all. Why are you even asking him that question?

**Chris Gammell:** Yeah. Yeah. Because it's a classic debate that. Of course. Silicon Valley also brought up. Yes. Right. Um, but yeah, I, I think the more important bit as a project maintainer is, is, um, automate the, the answer to that question so that you, when you're doing your review, when you're spending your time, you're not spending your time telling somebody to switch their tabs to spaces or vice versa. Yep. Um, because that is like one of the paper cuts that will kill you when working with a community is death by a thousand paper cuts is right. You want to remove those, those friction things as much as you can. Um, and the people that are coming into your community can also be really helpful, um, to remove those things as well. Uh, the example of testing the device driver to make sure it was actually broken is a great example of that. Like that's one small thing I didn't have to do. Um, so that's great. The way that we organize our community, which is kind of getting in the, into the tools side of community building is, uh, we do all of our GitHub. So we have the Adafruit support forums and that's existed for a long time. And that's the place that people can go to get like official support from Adafruit, official technical support. And then, uh, we have live streams that happen every week. We have ask an engineer and we have show and tell, which is how I got the job. Um, and Wednesday nights, if people don't know. Wednesday nights, four 30 Pacific, seven 30 Eastern. Please. Right. Hey, I'm in Seattle. I got it. I got to do it that way. Um, and what was happening is that we were having people, uh, chat in the chat channel with the live streams recurring week to week. And at some point they said, Hey, we should have a discord server. Um, discord is kind of like Slack, kind of like hip chat, kind of like Gitter, uh, but it grew up out of the live streaming community. And I think that's one of the reasons that it grew. It was the thing that people asked for. Right.

**Scott Shawcroft:** And it also has a voice function like the program you and I are using right now called mumble. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. So, uh, discord's a free application. You can get it on your phone. Um, you can get it on your computer. Uh, there's, uh, there's invite link that you need to join the server. We have one. That's just a, we have a short link for it. It's 80 a F R U dot it slash discord. Um, and that will jump you into our discord server, quote unquote. Um, which is kind of our space where we can have multiple channels. We can set a code of conduct and the moderators can moderate. Um, which I really like. We, I had experimented with a Gitter a little bit, which has really nice GitHub integration, but it's very vague as to what those boundaries are. Um, and so discord's really nice, uh, as a tool for that. So what that brought to our community and particularly the circuit Python community is a way that people can chat all the time, um, and get really quick iterative feedback when debugging. Um, I was on there a couple weeks ago.

**Scott Shawcroft:** Yeah. I was asking questions.

**Chris Gammell:** Yep. And Scott was in there. Yeah. Yeah. It's a balance between paying attention to it and not paying attention to it.

**Scott Shawcroft:** Uh, yeah. Right. You got to lock, lock down sometimes and just do the, do the code. Right.

**Chris Gammell:** Yeah, exactly. Yes. But, um, because I've had this mentality and, and the people that we've started working with have this mentality of like, above all else, helping people and teaching people is, is valuable and it's time well spent. Um, that means that we have a lot of people that sit in discord along with me and can answer questions when I am heads down in code. Um, and that is, is immensely, immensely valuable. And that's also the way that we find people that we want to start paying to do work. Um, which we now have, uh, two new folks since I came on. So Tony was doing some work and then, uh, Dan Halbert is full time as well. Um, and Katni remember is kind of all hands on deck doing stuff as well now for Adafruit with CircuitPython. That's cool. So on the, on the team side, we're growing a lot. And then we have like a dozen people. We have a weekly voice meeting that happens on discord and you can get the recordings of the previous ones through our YouTube channel. Um, we regularly have a dozen people that sit in on those. Uh, and that ranges from people who are, you know, making projects with CircuitPython and just letting us know, like things work, things didn't work, what worked well, what, what didn't work well to discussion that Dan and I will have about the DMA and at Mel start and all of that. Yeah. Um, but it's one place that anybody can go if they're interested. So everybody's welcome to join that. That's great. Yeah. We'll have links to all that stuff too.

**Scott Shawcroft:** That's great.

**Chris Gammell:** Yeah. That's Mondays at 11 Pacific 2 PM Eastern. Yeah. It's nice.

**Scott Shawcroft:** You can just kind of listen in if you want to, you can put on headphones and. Yep. Yeah. Just let us know.

**Chris Gammell:** Um, yeah. And then, sorry, go ahead. No, no, please. I've been talking a lot. I was going to say the last thing is, um, we do all of our, or a lot of our project management all through GitHub. So we have lots of issues and we have issues particularly marked that are good first issues. So if you want to get into the, the core work side or the driver work side, there's, there's good first issues that are marked for that. Um, and people are always welcome to reach out to me or any of the other folks to get help with those as well.

**Scott Shawcroft:** Hmm. What, what, what, what's an example of one of those? So it's like kind of like small things that could be chased down by someone that's new kind of, that's the idea.

**Chris Gammell:** Yeah. Yeah. Um, drivers are a great way to start. Um, so say like there's a new temperature sensor or there's a, those Nokia phone displays that are kind of prolific. Oh yeah. There's currently an issue out that says like, we need a driver for this. Um, I think one thing that is important in a community like ours is to just ask people to do stuff. Um, and if they say they can do it, believe that they can do it.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** And give them the time and the support to be able to be able to do that. So that's worked out really well. Like I, I had some work that I wanted to do with all of our documentation. We've got 70 drivers. They all have their own docs and I wanted to restructure them a bit to be better. And I was starting to do it myself. And then I had, um, uh, another community member, Mike McWethy come to me and say like, he just emailed me. So I'm like, can I just help with this? And I was like, you know what? Oh no. Yes, you can. I'll like, I wrote up a GitHub issue on it. I had a list of like all of the repos, all of the drivers that needed work and him and some other folks just went in and checked all that stuff off and it was amazing. That's great. Um, so just ask people and, and respect that they're giving you their time and, and give them the time they need to get over humps, uh, any hurdles that they hit and it'll pay off.

**Scott Shawcroft:** Like, right. I think this is good too, because this is a little bit, um, you know, I always, people who are like in school are usually asking like, oh, well I, you know, I hear I'm supposed to like join open source projects or like do this stuff. And it's like, this is a little bit more, this isn't quite as like high, uh, you know, this is, this is obviously it's a commercial venture, right? But it's, it is a, you know, it's a project that helps people, right? And it's probably a project that could help you build your next sensor into a project. So like there are some, some real benefits here. So I think that's good. Yeah.

**Chris Gammell:** And, and on the experience side, we work like I have six years experience with Google and Dan has like two or three decades worth of experience. So, um, yeah.

**Scott Shawcroft:** So like from a mentoring perspective.

**Chris Gammell:** Yeah. From a mentoring perspective and understanding the way that professionals work, it's a very easy way to get in there.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Um, you'll work directly with Lamore and as well as Dean. So like, yeah, it's, it's surprisingly easy.

**Scott Shawcroft:** Hey, yeah. I mean, do you, you do the work you, you get, you, you know, like it gets rewarded, right? So that's good.

**Chris Gammell:** Yeah. And, and, but we also understand that people are better at other things like they have different strengths. And, and one thing that I went into 2018, really wanting to think about, and there's a blog post I can, I can link you to that I did. Sure. Yeah. Is that I, when I first started working on CircuitPython, it was very much, this is a software project, right? I'm, I'm just worried about what I'm going to implement tomorrow and, and what hardware is coming down the pike. I'm not really thinking about everything else, but going into 2018 with our community, Discord started in June and that really grew our community a lot. Um, I really wanted to think about CircuitPython much more broadly than the actual thing you install, right? It includes the guides, it includes the API reference docs, it includes the driver support. Um, it includes the Discord community and the code of conduct and all of these things. These are all things that we need to work on to make CircuitPython as a project really successful. Um, and you'll, that's something that a lot of open source projects do really well.

**Scott Shawcroft:** Yeah. Yeah.

**Chris Gammell:** Um, but it was a re it was like a recognition in my mind of like, oh, I'm doing a lot more than just code coding every day.

**Scott Shawcroft:** Well, yeah. I mean, you're, you're an organizer now as well. Uh, what's, what's, what's, what's, what's, what's, what's, what's, what's, what's, what's coming up tonight?

**Chris Gammell:** Yeah. Uh, we have the second Seattle hardware happy hour tonight.

**Scott Shawcroft:** And Mike, he's been revealed as the creator of the hardware happy hour. Number two. We are the, yes. Oh yeah. Yeah. So I, uh, I don't think I mentioned that, that you were the one doing it. So that's.

**Chris Gammell:** No, I don't think so. But yeah. You're like, yeah, you didn't. Well, Chris, you deserve a lot of credit because you, you connected a bunch of us in Seattle here via email. And so many hardware people out there now. What the heck happened?

**Scott Shawcroft:** I don't know. I think it's the software people coming over, man. You got a lot of software people out there. So. We do.

**Chris Gammell:** We do. We have a lot of tech. Yeah. Um, and hardware is super fun. So I, I understand why people would go that direction.

**Scott Shawcroft:** Right. Exactly. Don't, don't just layer bike stuff onto a map, you know. Oh yeah. Build the bike or, you know, instrument the bike. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** I think the Google AIY kit stuff. Oh yeah. That's cool. Seattle. The Seattle office as well. Yeah. I've been trying that actually. It's, it's a cool little kit. Yeah. So. That's good. Yeah. So you connected us and I picked up time and location last month and one this month. And so we have that tonight. It's very chill. Like you, you do in Chicago. It's just hanging out at a brewery, showing, showing stuff off and chatting. Um, so I'm really looking forward to it.

**Scott Shawcroft:** Is there, is there a Kaiser sighting? Can you, can you tell him we said yes, uh, remotely?

**Chris Gammell:** I'll try to remember that. Okay. He RSVP'd yes on the, on the meetup when I saw it last. So I think, I think Jeff will be there. Okay. Um, I didn't actually get a much of a chance to talk with him last time cause I was too busy talking with other people. So.

**Scott Shawcroft:** Yeah. That's good. That's, that's what these, uh, you know, like these community things like hardware and software nerds like talking to each other. It helps when there's beer too, but you know, there's a, you know, just projects and hanging out and. Yeah. It's, it's super fun.

**Chris Gammell:** I was looking forward to it for sure. And I, I appreciate you connecting us. Yeah. Cause I'm, I'm kind of bad about it.

**Scott Shawcroft:** It's just, you gotta, you just gotta keep it up. You know, like that's, that's the thing over time. It, it gets, it gets tougher over time. I think that's the main thing.

**Chris Gammell:** Yeah. Yeah. And we don't have a particular space we're doing it in right now. So we're, I think it's better to move around.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Yeah.

**Scott Shawcroft:** Uh, if other people are interested in starting a, you know, a, there are franchise opportunities here, folks, uh, you know, the benefits await. Yeah. Uh, one last thing I think you should mention though, is you were going to be at PyCon, right? Yes, for sure. In? In? In Cleveland. Cleveland! I saw that this year. I was like, really?

**Chris Gammell:** Like why? It's next year as well, actually. What? Um, what is going on there? Well, they, the way that PyCon does it is they negotiate hotels and conference centers for two years in a row to lower the overhead of doing that.

**Scott Shawcroft:** That's actually pretty smart. Okay. Yeah.

**Chris Gammell:** So the last two were in Portland, the next two are in Cleveland. And then I don't know where the next one is after that.

**Scott Shawcroft:** Wow. Um. Cleveland.

**Chris Gammell:** Bringing it on. How big is PyCon? It's 3,300 people. Oof. Okay. Um, so we have a goodie bag or we have an item in the goodie bag. Oh yeah? Which we are not revealing what it is, but it's quite exciting. And it does, I guess I could say it runs CircuitPython. I mean, that's okay. That's smart. Right, right.

**Scott Shawcroft:** And this one runs JavaScript.

**Chris Gammell:** There are, there is an equivalent JavaScript equivalent thing. I don't think it's as popular, but. Got it. Um, yeah. So I'll be, I'll be at PyCon. Um, I'll be in New York in April just to visit. So if you're in New York, feel free to hit me up. I'd love to do lunch. Um, I'll be in Cleveland for PyCon and I'm thinking about visiting Boston for the Open Hardware Summit in September.

**Scott Shawcroft:** Oh, actually I didn't even know what that was decided. So.

**Chris Gammell:** Yeah, I think they just posted it. Okay. Um, September 27th at MIT. So I'm going to, I think I'm going to try to make a New York, Boston trip out of it. Uh, because Dan Halbert is based out of Boston as well. Oh, very cool. My other core dev.

**Scott Shawcroft:** Yep. Yeah. Boston's a fun town. I've never actually been in it. They've got some robots up there and stuff.

**Speaker ?:** So.

**Scott Shawcroft:** Yeah.

**Chris Gammell:** Some engineers there too.

**Scott Shawcroft:** Yeah, I guess so.

**Chris Gammell:** Yeah. But then as I'm, I'm based in Seattle and I'm also always willing to get out and have coffee with, or tea with people.

**Scott Shawcroft:** I guess if you're, if you're working from home, you need, you need that, uh, that break, huh? I definitely do. Yeah. Definitely do. Even a discord server doesn't, doesn't, doesn't, uh, cure the, the stir crazies. It helps. It definitely helps, but it, it, yeah.

**Chris Gammell:** Working from home is a whole nother topic.

**Scott Shawcroft:** Did, I don't know if I've ever, I mean, you listen to the show once in a while. Is that right? Yeah. Pretty regularly. Okay. So I don't know if I've ever mentioned why I joined the workspace I'm out of. There was like, uh, so I was, I, and I've told, I tell the story around here once in a while, or usually when I'm at, at M hub, which is where I work out of now. Yeah. People ask like, why'd you join? I'm like, well, uh, I was working remote and I had a really busy day of meetings and, uh, I was on the computer all day long and just talking to people, talking to people, mostly, mostly by text. And, uh, uh, you know, I didn't really think much about it. And then about one, one AM I'm finally done with everything. I'd working on a board, I think, or something. I fall into bed and I say out loud, ah, crap. I forgot to schedule that meeting. And, uh, and then I think to myself, well, no, no, I think to myself, that's the first time I've spoken out loud or left the house in two days. Uh, yeah. And then the next day I joined a shared workspace.

**Speaker ?:** Yep.

**Chris Gammell:** Yeah. So I, yeah, I can totally relate to that. I didn't have quite the same experience, but I did like three days. I was like, I think I've only gone outside to get the mail and like take the garbage out. So I actually, I, I started doing what I call as a commute with air quotes, um, where I try to actually get outside for not that long, but just go walk around my neighborhood, like in the morning before I get going. And then at night as well. That's smart. It really helps. Yeah.

**Scott Shawcroft:** It's been hard because it's bad, but. Yeah. And then doing like 3H and like meeting with humans and like, or having coffees, like you're saying, like these things are all survival mechanisms of the remote workers. It is. Yeah, it is.

**Chris Gammell:** For sure.

**Scott Shawcroft:** Well, and we can always, you know, chat again on, uh, the amp hour. So that also helps. Cool. I'll take you up on that. I think we covered the core stuff, but. I'm sure that there's a lot of people that were shouting about my lack of knowledge about, uh, uh, debuggers, but I don't know what they were expecting. Honestly, folks.

**Chris Gammell:** What I was thinking actually is a challenge. The challenge is if you think you can explain it better, write it up and share it. That's a great idea. Yes. Um, it's, it's hard to explain things well and it takes a lot of practice and I certainly need more of it.

**Scott Shawcroft:** And there's not as much out there as you'd think there would be. You know what I mean? Like, yeah. So that's a great point. So a challenge from Scott. Yeah. Uh, Scott, thank you for being on the show and, uh, uh, Twitter. I will post all your links, I suppose, to everywhere you can be found. So. Yeah. Uh, don't expect to, for me to see Twitter cause I don't use Twitter. Oh, uh, where's the best way then?

**Chris Gammell:** Um, you could just email me. Okay. I'm Scott at adafruit.com. Okay. Um, you can find me on our discord. Yeah. It's probably the best place. Huh? Yeah. But Twitter, I, I try not to be on. That's healthy. Yeah. Okay.

**Scott Shawcroft:** Yeah. All right. Well, enjoy 3H tonight. Tell everyone out there. I said hello. Thank you. I will. We'll talk to you soon. Bye. Bye.

**Scott Shawcroft:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye. Bye. Thank you.
