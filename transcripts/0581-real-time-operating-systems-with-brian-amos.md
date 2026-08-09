---
episode: 581
title: Real Time Operating Systems with Brian Amos
url: https://theamphour.com/581-real-time-operating-systems-with-brian-amos/
---

**Brian Amos:** This is The Amp Hour Podcast. Released March 13th, 2022. Episode 581. Real-time operating systems with Brian Amos.

**Chris Gammell:** Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics. And this is Brian Amos, author of Hands-On RTOS with Microcontrollers.

**Brian Amos:** Hey, Brian. How are you? Doing well. How about you, Chris? I'm good. I first heard about your book, I believe, from Philip from Embedded Artistry. And then I read it, and I was getting into RTOS's, and it's a really good book. So thanks for being on the show today. I'm excited to ask you all the dumb questions that I had as I was reading the book.

**Chris Gammell:** My pleasure. You're definitely in the target audience for the book.

**Brian Amos:** People who are dumb with RTOS's? All right. Yeah, that's right.

**Chris Gammell:** No, hardware engineers with prior programming experience have a familiarity with hardware.

**Brian Amos:** Yeah, yeah, yeah, yeah. I mean, this all kind of started coming up when I was... So I was doing some NRF52 projects, and I was kind of poking around the NRF5 SDK, and there was a bunch of free RTOS stuff on there. And I was thinking I could do some Bluetooth stuff using their binary blob, but there was other examples using free RTOS, and a bunch of people had used free RTOS. And so I started exploring it, and I think that kind of led me down the path towards this stuff. And I remember I talked to Alvaro Prieto, who's one of the co-hosts of the Reverse Engineer podcast, and he's a big free RTOS fan as well. And I think he had also maybe mentioned the book. But just kind of like as a starting point, people... I was like, all right, I need to learn RTOS's. And I was kind of just hunting around for info. Is that a common thing that you see? There's people just saying, today's the day I need to start learning RTOS's?

**Chris Gammell:** I don't really get too much... People aren't coming to me saying, oh, how do I get started?

**Brian Amos:** How do I RTOS?

**Chris Gammell:** Yeah. How do I... How is this whole RTOS thing? Usually I wind up talking to people that have been programming for a while, and inevitably they don't really know what an RTOS is, or why they would want to use one. So it's not even like, oh, how do I get started in this? How do I dive in? It's more like, well, I have my C compiler, and what else do I need? Right? Yeah. There are lots of tools out there that can help you.

**Brian Amos:** Yeah. I think, I mean, for people that are thinking about an RTOS, I feel like the first thing is like, well, would a state machine do what you're really needing? It's like, if so, and it's really small, that might be the best option. You know, it's like, but then I had been asking some people about like, oh, well, should I just start, you know, start from the premise of like, just go straight to it. I'm going to have a real-time operating system instead of a state machine. And some people said, yeah, you know, that's how I prefer to do it.

**Chris Gammell:** Yeah. It's funny because a lot of the projects that I've done, some of them are inherited, right? So you already have a code base and you need to add some features to it. And other times you have an idea of what you're going to be doing. And it's, it's more well-defined. You can kind of bound it a little bit better. And that, if you know ahead of time, minimum requirements and then desirements after, you know, that, that MVP is done, then you can usually get a pretty good idea. But.

**Brian Amos:** Okay. So, okay. So say we got a greenfield project, not like a brown, I say brownfield for inherited, already built greenfield for clean sheet of paper. Yep. What is, give us an example of a project that you've either seen or, or tell me about a time. It's like an interviewer. Tell me about a time. But like, what is a good example of like, yeah, you're probably going to want an RTOS or maybe not. You don't have to care about it. Do you have those in your head?

**Chris Gammell:** Yeah. So anything with, if you have a user interface, almost definitely because, you know, especially like a GUI and onboard GUI or something like that. Anything with extensive communications capability for sure. So network connectivity, USB, tons and tons of spy. You are.

**Brian Amos:** Anything with a stack in the name. Yeah.

**Chris Gammell:** Yeah. Lots of, especially, especially like third party stacks that might be really bloated. You know, if you can wind up, if you can, you can use an RTOS to segment a lot of that, what I'm going to say, lower priority stuff. And then, you know, write really efficient event driven code. That's really, really close to the hardware. You know, we're talking ISRs, all that kind of stuff. Right. And so you push off all of the third party stuff, push it into its own task, give it a nice low priority. And then any of your higher priority things that deal more directly with time sensitive hardware, you kind of do that like under the hood, right? Actually below the RTOS. So you don't even have to interact with RTOS if you don't, unless you have a reason.

**Brian Amos:** That's kind of confusing too, because low priority is, it's like a low priority. It's like golf, right? It's like, if you're bad at golf, you have a high score. If you have low, if you have a low priority in an RTOS system, you have a high priority score. Isn't that right? Or is that, I have that backwards?

**Chris Gammell:** Well, that's like, so the cortex, I'm not talking about a cortex M ISR rankings here. I'm, I'm, I literally mean low priority. So if you've got something, let's say, all right, let's say that I have a, like a, a control system, right? So I have a closed loop control system where I'm reading sensor data and I want to control the position of, let's say a motor, right? So I'm going to read in data from a sensor and I'm going to control some sort of an actuator. Okay. And you have to do that in a tight loop. So we'll say that's high priority, right? Because that's like the main purpose of this system is to control this, this motor, right? It's a servo control system. And then let's say that you also have a front panel for changing the set point or whatever, right? Of this positioning system. So I'm going to argue that the front panel is a much, much lower priority because it's only dealing with user input.

**Brian Amos:** Right.

**Chris Gammell:** Than the actual positioning of the motor, right? So, you know, you, like UX guys are going to be screaming, you know, oh, I can't have glitchy UI.

**Brian Amos:** We need it to be responsive.

**Chris Gammell:** Yeah. Yeah. It's like, okay, well, you know, you can have your responsive UI and that's fine. But the position of this thing is really kind of the important. If we chop someone's finger off, we're going to, we're going to be in trouble. Yeah, exactly. So, so the, the nice part about if you have this, you know, crazy, let's say you've got animations on the UI, a whole bunch of unnecessary crap that's like standard these days, right? And expected, you can kind of, you, you push the priority of all that junk down and then, you know, you operate a higher priority for all the stuff that actually matters. So it's, it's great for prioritization. You know, it's, it's definitely not a magic bullet there by any means, but yeah. Yeah. So that's, that's one case. And, you know, let's say that this thing has also got some crazy IOT stack on it or whatever. And it's talking, talking, talking to the cloud or whatever, right? Some, some horribly, you know, bloated piece of software that has been written by, you know, an entire team and you bring that in, push that to a low priority too, right? And then, you know, it's just focus on the real time stuff.

**Brian Amos:** You can talk to the network when I tell you, you can talk to the network. Exactly. Yeah.

**Chris Gammell:** Yeah. And, you know, you want to do that stuff in the background when you have time, that's, that's perfectly okay. But let me just make sure that I actually do my primary function first. Yeah. Yep. So anytime multitasking is important and you have a bunch of little.

**Brian Amos:** Yeah. So, so the multitasking, a lot of different kind of once in a while things happening. I, I, I kind of, I remember coming at this problem from like thinking, thinking about it from more of a, like an embedded Linux perspective and thinking like, I wouldn't want something trying to get an update on a webpage while I'm waiting on, you know, data coming back from like a spy sensor or something like that. Exactly. And that would be bad. And, and a full, full operating system like Linux does that sort of thing at a different level. So could you differentiate then for people real time operating system from a full operating system?

**Chris Gammell:** Yeah. So, so the book was based off of a free RTOS. I mean, a lot of the microcontroller targeted RTOS is are very, very similar, but you know, with, with free or free RTOS is really just, it's pretty much just a scheduler and like some really basic things like, you know, cues, semaphores, task notifications, that kind of stuff. So there isn't, you don't have any libraries, you know, there's, there isn't a whole lot of stuff now that Amazon acquired them. They're starting to add a bunch of that stuff, but at its core, it's really just a scheduling kernel as opposed to, as opposed to Linux, which is of course, you know, full blown operating system and you can bring in libraries and drivers and all that kind of stuff. You don't really get any of that stuff. Different RTOS is you can, you can purchase them. You can purchase modules sometimes, right? Depending on the vendor and that sort of a thing, but it's, it's really just super pared down. And what it, what it's really, really good at is bounding things based off of time. So if you say, oh, in your example with the, you know, waiting on data coming back from a spy sensor while you're trying to load a webpage, right? The data coming back from that spy sensor, you could actually bound that and say, Hey, I expect data back from the sensor within 10 milliseconds. And if it doesn't come back, if it doesn't complete in this amount of time, you know, or if I can't, if I can't acquire a mutex or a semifor or whatever you're using to access this peripheral in X number of milliseconds, then bail out and, you know, do something right. So all those kinds of timeouts are built into pretty much all the calls, you know, it, and there's always, you're always thinking about, okay, after, after this thing goes wrong and there's no sensor on the other end, what happens? Right. So you don't get into, and you can put in infinite delays if you really want to, it lets you, but you know, you're always thinking about what happens if something goes wrong. So it kind of gets you into that mindset and that's something pretty different as well. I mean, you know, for, for systems programming, I suppose you have exceptions and that kind of stuff, but.

**Brian Amos:** Yeah. So, so the, the thing that I always hear about with like OS versus R2S is something about memory management is one thing. Is that kind of the, or is it just more of the build out as well? Yeah. Cause like the, the other thing, my other reference point here is that I've been doing a lot of Zephyr stuff poorly. I'm learning a lot of Zephyr stuff, I suppose I should say. And, and that's kind of like, it's not just the kernel. It's not just, you know, there's like other stuff kind of already there and monologuing and built in. And it's, so it's, it's more like starting from the middle and saying like, okay, you've already got a lot of stuff in this huge package and you can pare it down. But most of it, you're what you're getting. You kind of get it all there first. Whereas like you're saying with FreeR Toss, it's kind of like, when you start from the bottom and you build up, you can bolt stuff on and, and put things together, but you start with a, the assumption that there's not much there. And then I think Linux side is like, yeah.

**Chris Gammell:** And as far as memory management goes, like you can do as much or as little as you want. So there are ways of creating entire projects and it's not just FreeR Toss, but you know, with a lot of R Tosses that are purely statically allocated. So there is no, there is no heap, right?

**Brian Amos:** Yeah.

**Chris Gammell:** So there is no penalty. There is no Malik. There is no new, you know, those kinds of projects exist. And you can get really, really good at predicting how long things are going to take when you're not using a heap because it's just machine cycles at that point. You're not searching for a spot to put this variable in memory, right? Uh, uh, and then, you know, even if you use the FreeR Toss heap, if you prescribe to the notion that you create tasks and then they just run forever, like their own little state machine, each task is basically a state machine, right? So if you, let's say you create five tasks and you want to have the ability to do dynamic allocation, you can use the heap. But the only time that you're, so you would set up a stack for each one of those tasks. And at the beginning, like, you know, right at the beginning of main before you start the scheduler and you don't have to touch those. So as long as you go out and you acquire the memory that you need, you have the memory, there is no more dynamic allocation and you're, you're good to go.

**Brian Amos:** Yeah. So you get what you get then, right? You're just, you're just doing that. You're just using the memory you have at the beginning.

**Chris Gammell:** Yeah. So, right. If, if you're like, okay, well, this is a pretty, you know, this is a very small task. It can probably get away with 512 bytes of stack space or whatever, you know, then the stack for that task is set to 512 bytes. You never have to ask for more and right. That, that, that's it. And that, that task will do whatever it needs to do. And as long as you never go above 512 bytes, you're golden. Right. Right. Just like overrunning a raise, you know, bad things can and do happen. Yeah. Yeah. Yeah. But you know, it, it has some hooks in there to detect that kind of stuff as well. Got it.

**Brian Amos:** So like the, the one, the thing I want to kind of offset there is like my, like I said, my reference point is kind of Zephyr. It's kind of like in the middle somewhere. Free our toss and other kind of, and especially like bespoke our tosses. Cause you talk about that in the book a little bit as well. And that's kind of bottom up, you're kind of building each thing up. And then when Jay Carlson was on the show talking about Linux embedded Linux development, it's one thing he talked about was like, well, you're going to end up reading a lot of code, but not writing a lot of code. So it seems like the free our toss, you are writing a lot of code, but you are crafting it how you want it to be. So it is that bottom up methodology.

**Chris Gammell:** Yeah, very much so. And you know, it, it's API is pretty minimal. So you're not really, I mean, if you're bringing in the exception of course is as soon as you start bringing in third-party libraries, you're reading a ton of code, right. Or maybe documentation or whatever.

**Brian Amos:** Right. Yeah. You want to know how you can interact with their APIs and what are all the gotchas from that sort of thing and what you might want to draw out of them. Right.

**Chris Gammell:** Yes, exactly. Yeah. Yeah.

**Brian Amos:** So one thing I really liked about your book was because it is that bottom up methodology, I feel like most books start a little bit too, most of the free, most of the artos books that I've done, they immediately want to talk about just like only semaphores and only mute. Like I remember John Labros's book about Micrium and Micro-COS too. Very good book, very good reference, but man, it just wants to talk about mutexes. And I'm just like, I don't, I don't know what the hell you're talking about right now.

**Chris Gammell:** Yep. Yeah. That's why all the, all the diagrams were at the beginning with, without any code around them, like little, little flags. Here's a semaphore. That's really useful. Yeah. Yeah. That's because the first time that I used an artos, I, I drew out all that crap. Yeah. That's great. I haven't seen this stuff since school. I've got to, yeah. I've got to go back and get a refresher here.

**Brian Amos:** And I think that's super important, you know, like to be able to do that sort of thing. And I guess one of the things that I didn't realize because I got so kind of stuck on that other stuff is, you know, I'm probably going to say this wrong now, but like the idea of an artos having the segmented memory, like you said, that 512 bytes, it's kind of, it's segmented, but then there it's like, it's doing its own thing. The task, how does it say this? It's like, you have these side-by-side neighbors or like apartments of memory, right? And they're like side-by-side and they're living next to one another, but, but they are the stacks that's, that live next to each other as well. Right. They're like, they act like a stack, but they're all.

**Chris Gammell:** Well, they are, they are a stack. Each, each, each task has its own stack. Right. And that stack is only used by the task. And then you also have.

**Speaker ?:** Yeah.

**Brian Amos:** That was completely new knowledge to me. Like I, I, I did not understand that at all about it prior to your book. So that, that alone was the price of admission for me. That was really worth it. That was awesome. Good.

**Chris Gammell:** Yeah. And then, you know, there's, there's inner task communication between the tasks. Right. And that's, that's where you get things like, you know, okay, well I can have a queue and that queue, you know, let's, let's say that's a, that's a global, right. It doesn't live on either of the two stacks. It's effectively a global variable.

**Brian Amos:** That's, you know, can we, can we make like a Sesame street style analogy here or something that would be very useful for me? Yeah. We're like a queue is like, um, you know, there's like mailboxes and queues would be like, I don't know, like a water slide between them or something.

**Chris Gammell:** Yeah. Yeah. Yeah. And, uh, I think the, I have to go. Let's see. Understanding our test has, if you, if there are actually some really simple diagrams that explain this stuff at the beginning. Great.

**Brian Amos:** Uh, and I have, I have the same PDF that Brian has opened. So we can, we'll, we'll be able to say, we'll try and back back date it to where the chapter and stuff like that, but we'll probably talk about page numbers here from the PDF. So if you're on my Kindle version is very different. So that's why we're looking at the PDF.

**Chris Gammell:** Yeah. So if you look at the, the, the page numbers on the bottom of each page on that PDF are actually like the same page numbers as the book. The book is just like a printed version. Oh, great.

**Brian Amos:** Oh, like the, you mean like the paper book? Yeah. Yeah.

**Chris Gammell:** Dead tree, the dead tree thing.

**Brian Amos:** Yeah. No, I don't. Yeah. And I'm a Kindle guy personally.

**Chris Gammell:** Yeah. There were quite a few complaints about the Kindle version. Oh yeah. Well, the publisher decided it was a good idea not to put chapter numbers. Yeah. There's no, there are no chapter numbers anywhere. It's crazy. Yep. Details. Yeah.

**Brian Amos:** Details.

**Chris Gammell:** Yeah. So, yeah. So, um, let's see. Yeah. So in chapter three, right. You have, you have these cues and there are some super, super simple. They're just, they're just boxes. If you have a, you have a cue of length four, right? You can think of that as four bins and you put something into the bin and then when you take it out the other end, that's, that's it. It's just like a conveyor belt, right? If you want to think of it that way. Yeah. Yeah.

**Brian Amos:** Or how about if we, if we had two, two tiny fiefdoms of memory, then it would be like the security checkpoint between the two, right? Cause you'd get in line to check. Yeah. Yeah. Exactly. Right.

**Chris Gammell:** Yeah. And then those, the two guards that are, you know, staring at each other through the two fiefdoms, they're, they're making sure that one task doesn't step on the data of another task, right?

**Brian Amos:** So they're guarding between, if you want to go with that. We're building, we're building a world here as we speak folks. We moved away from Sesame Street pretty fast. I'm pretty sure Sesame Street doesn't have guards. You know, it's not like, uh, you know, the count being like one, one refugee coming from one place to another.

**Chris Gammell:** I mean, you need Oscar the Grouch in there too.

**Brian Amos:** Yeah.

**Chris Gammell:** Yeah. He would definitely be. Yeah. He's a trash collector. Totally be in there. He could be like taking care of, uh, counting semaphores and then. Yeah. Yeah. He'd be like the tick, right? I mean, he'd be like, uh, I think that's Oscar the Grouch should be like config assert. So in free, in free RTOS, there's a, whenever you do something wrong, like there's, there's all the, there's this notion of ISR safe functions. Right. And if you call a, if you, if let's say you try to add to a queue with like the normal API from inside of an ISR, then you get a config assert. So it's just, it's an assert that fails. And it's like, Whoa, this is within an interrupt context. So that's like, that could be awesome. Grouchy. Yeah. It's totally grouchy. That's good. Yeah. Okay.

**Brian Amos:** So that's how you get from one task to another. And so the task is kind of like the. That's one of the ways. Is that like the smallest block of memory? Yeah.

**Chris Gammell:** Yeah. Well, I mean, you know, you have semaphores, which are very, very tiny. I imagine in free RTOS, they kind of implement everything under the hood as a, as a queue, which is interesting from a, I think it saves, it saves ROM space, but you know, there are some people complain that there are faster ways of doing that, but yeah. So, I mean, you can have a queue of length one, you can have a binary semaphore, right? But the only, the only time that you're really creating these things that are running in concurrently or when you're creating a task.

**Speaker ?:** Hmm.

**Brian Amos:** Yeah. Okay. So now we have, so say we have a system with, maybe we should make up a fake example here.

**Chris Gammell:** Yeah.

**Brian Amos:** So we have a task that's.

**Chris Gammell:** What's your system doing? What do you, what do you want your system?

**Brian Amos:** Let's say, let's, let's call it a, um, how about a ventilator, right? There's all that open ventilator stuff. So it's like, there's a task that's measuring air pressure. There's a task that's actuating pump. There's a task that's updating a screen about the status of the pump. Yep. And there's a task that's reporting it to the internet or something like that. Even though that would be a huge task, we're just going to, we're going to make it a magic task. How about that? Sure.

**Chris Gammell:** Yeah. Yeah. So, you know, you would have, you're probably going to have, I would say like a task that's taking care of reading the life, life critical kind of stuff. Right. So that gets the highest priority in the system. So if it has any work to do at all, then it will run no matter what. Right. And in the case of a ventilator, you would definitely, that's, that's priority. Number one, you don't really need to, you know, like tweet the number of, of, uh, breaths the ventilator is provided to the, yeah, you don't, you don't care about any of that kind of stuff. And the other important thing for that high priority critical task is that it's, it can't be waiting on any shared resources from any of the other tasks. So you really want that to be pushing information out. Yeah. Right. So you, you know, you don't want to get into a situation where there's this crazy big block of shared memory and you're waiting on a mutex for something to update. You know, you just want that, you want that critical task to be continuously running. And then when it has information to disperse to the other part of the system, you know, it would do that probably through a queue. Yeah. It'd be a reasonable thing to do.

**Brian Amos:** Yeah. So the other thing that, that kind of, that this, your book opened up for me is like, okay, so now you have something that just, it's a task. It's just reading a sensor. And that just looks, basically, it looks like if you just had a, a single function program that was just like spy read, spy read. And then it's just a loop basically. But instead of like a, and correct me if I'm wrong here, but instead of saying like, wait 5,000 milliseconds, it says, I'm going to go to sleep for 5,000 milliseconds or whatever the, you know, the timing is.

**Chris Gammell:** You can have super, super fine grain tasks like that. More often they wind up getting segmented more along the lines of like a group of responsibilities, you know?

**Brian Amos:** Okay.

**Chris Gammell:** All right. So it would be like sensor package. So it'd be like, yeah, so I would, I mean, and again, this is kind of a, this is getting into design decisions. Right. But typically if I'm, if I'm creating tasks, then they're going to have, it'll be a task. Let's say the, you know, the, the ventilator example, right? It's going to be the, the measurement of your, you know, PSI or whatever it is, is going to be happening. You're going to be taking that measurement in, you're going to be controlling your actuator. All of that is going to be in a single task. You wouldn't necessarily need like two tasks, one for the center, one for the actuator. Right. So, so you're, you're kind of grouping stuff in like tasks and, and, or, you know, like, like functionality. Right. So then you, you push all your IOT stuff and that stack out onto a different lower priority task probably in that example.

**Brian Amos:** So when, when you make, I mean, you mentioned design decisions, but like when, when do you construct that? I would imagine that there would be problems if you, like, then you, what if you need to go re reconstruct something later? Is it tough to, to do that sort of thing and be like, oh, actually no, now we need to have the sensor package talk over a cue to the motor instead of having the. Oh, it's just like anything else. It depends on how much spaghetti you've, you've created first.

**Chris Gammell:** Right.

**Brian Amos:** Imagine infinite spaghetti for me.

**Chris Gammell:** Yeah. So, so really, you know, the, the best thing to do is just to, you, you sketch it out on a napkin and say, Hey, I've, I've got, I have, you know, requirements A, B, and C to take care of. How am I going to accomplish these things? What needs to happen concurrently to the other stuff? Each thing that's going to happen, you know, seemingly in parallel, get its own, would get its own task. If you have some long running stuff, that's low priority that gets its own task. If you have some higher priority things that need to happen with tight time constraints, they either need to go into, you know, ISRs and just deal with them below any of the RTOS stuff. So, you know, in the ISR context, that's going to run no matter what. Right.

**Brian Amos:** So ISR is interrupt service routine for people that are hardware focused like me. Yes.

**Chris Gammell:** Yep. Yep. Yep. Yeah. So, so all of your interrupts, you're going to configure those so that you're almost always, so that your scheduler interrupt is a lower priority than any of your critical interrupts. Right. So if you have real time sensor data getting streamed back from something, right? So let's say that you're, that pressure sensor on the ventilators is streaming data, then you would make that a higher priority and you would always go out and read that no matter what. Right. And then you can, you can squirrel that data away and then, you know, post a semaphore whenever you have enough of it and it's time to do something with it. And then, you know, at that point, the scheduler takes over and you start having RTOS tasks kind of, you know, spin on.

**Brian Amos:** I think that was another thing that I didn't quite understand is that you can, so like if you're designing a system now, and I had been, you know, kind of in the bare metal working with interrupts and getting used to that. And then it was like, well, if you're in an RTOS now, you actually don't ever need to use an actual hardware interrupt anymore because basically an interrupt is built in. You have to be careful there.

**Chris Gammell:** You have to be very, very careful there. You, I mean, you. Why is that? You can program like that, but.

**Brian Amos:** Yeah. Not as, not as like a wood, but like a, like, cause yeah, I mean, a lot of the sensors I use, they, you know, they have a pin that goes high when they're done with it, but they never reading ready. So I wouldn't want to use that. But in the event I didn't have that, I just had like really silly, simple, just analog sensors. And I, you know, it was just like this interface into an old analog system or something. In theory, I don't need to have physical hardware interrupts.

**Chris Gammell:** Yeah. I mean, you can, if you're, so we have to be a little bit careful here. Right. So depending on how fast.

**Brian Amos:** Someone, someone in a future design meeting and be like, well, Brian, but on the amp hour, you said, you know.

**Chris Gammell:** So. I mean, you know, how fast are your sensors being read? Right.

**Brian Amos:** Yeah.

**Chris Gammell:** I mean, like that's.

**Brian Amos:** I, I'm not, I'm not, I'm not going to hold you to this here. I'm just saying this was, this was my epiphany about it where I, I had kind of always thought it was like the two choices were, well, you can have an interrupt driven system where, you know, you have these sensors and. Oh, I see. Yes. Yeah. Absolutely. Exactly. Or you're on like just a loop and you're saying, well, I'm going to pull everything. Right. And this is, this is the epiphany here was like, oh, well, it does bet much better options at the middle, which is.

**Chris Gammell:** But the tricky thing, the one thing to keep in mind is yes, you can write pulling routines inside of a task in an RTOS, right? That's not a, that's perfectly okay to do. But at that point you've, you've still written a pulling routine and your, your CPU still needs to go out and check whatever it's pulling at some interval, right? So you're still using CPU cycles, depending on how fast you want to check that thing. If you can manage to design your hardware in such a way that it goes into an interrupt pin or it starts communicating to a UART and your UART peripheral has, or, you know, USART spy, whatever, whatever it is, right? Some sort of serial peripheral has interrupts. Then those interrupts could be activated. They can bring in a meaningful amount of data from the sensor. And then you can, you know, signal a task to wake up and say, Hey, I've got some useful data rather than that task spending time pulling this thing repeatedly. Yep. Yeah. So you can, you can wind up with more scalable systems that have better response times. If you avoid almost all the pulling possible. Now, of course, with pulling really high. Yeah. Yeah. Pretty much. Right. Like, and that also holds true for, for low power designs too. So, you know, the more things that you can have event driven in a low power design, the better, because the one thing that you kind of get for free, depending on which port of free RTOS you're using, some RTOS is, free RTOS is one of them where they have a tickless mode. And so, you know, like normally in RTOS, it, it has to keep track of time. Right.

**Brian Amos:** And, you know, just another, another thing that I learned from your book. Yes. Yeah. People are getting a good feeling for just how little I understood about it prior to this.

**Chris Gammell:** It's, it's a very, you know, time is very important in a real time system as it turns out.

**Brian Amos:** Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. So, so if you have a, a fully event driven system and it needs to be low power and you need reasonable, you know, like, let's say you want like millisecond time resolution for whatever reason, right? You really don't want your processor waking up from an interrupt every millisecond. That would be, you know, that's the battery killer. Yeah. That'd be terrible. So they have modes. If you, again, try and avoid the pulling route as much as possible, create everything to be event driven. And you can go into a tickless mode where if you have something to do, let's say once a week, you know, and you're using hardware that has the capability with a real time clock with an alarm, you can set everything up so that the whole chip gets powered down, except for that RTC. It wakes up in a week and then it's time to do whatever you need to do. Then it goes right back to sleep again. And, you know, there's no CPU intervention necessary, you know, between that time, obviously, you know, at that point you start talking about clock drift and that kind of stuff. But, you know, that's where crystals versus RC oscillators start to become kind of important for your RTC stuff.

**Brian Amos:** But yeah, I'm just surprised that I didn't get into this sooner, I guess. I mean, like I should say get into this. I mean, read about it sooner. I don't know. How did you learn all this stuff? I mean, where did this all come from?

**Chris Gammell:** I don't, I don't, I remember. I'm not sure how I, okay. So the first time, my first exposure to, it was, it was actually like an anti-RTOS. So I was working, I was working for a company and we were developing a vibration monitoring sensor that was living on a mesh network. And so it was like, you know, a mesh network, mesh wireless network, right? And this thing was supposed to wake up every once in a while and capture a waveform and then send it back to wherever. And some, you know, some senior engineer had decided that, oh, there's this thing called a Telos module made by a company. This is back in, oh geez, probably like 2007, 2008 or so. And there's this Telos module. It was developed using this operating system called TinyOS using a language called Nessi. And so, you know, a whole bunch of really obscure stuff.

**Brian Amos:** This is sounding good. Yeah, yeah, yeah.

**Chris Gammell:** So anyway, that was my, that was like, well, what, what the heck is this? Oh, it's this little operating system. It's like an, an anti-real-time operating system.

**Brian Amos:** It's like, what the hell does that mean?

**Chris Gammell:** Well, it basically tries not to do anything.

**Brian Amos:** Bullet time. It's bullet time.

**Chris Gammell:** It's like, it, it tries to push off as much as it can to do later so that it doesn't need to wake up because that costs, that costs power. We don't want to do that.

**Brian Amos:** It's like a, it's like a sleepy time, sleepy time.

**Chris Gammell:** That's exactly what it was. So, so they would batch up these processes. So you had all this, all the, the interrupt level stuff, right? And then you would just effectively like post it to a queue. And then at a certain schedule and the schedule could be like at one Hertz or, you know, once every five seconds or whatever, the, the processor would wake up and it would chug through all the stuff that it had to do and, you know, whatever, whatever those kinds of tasks needed to be, needed to have their stuff done. And she was like, okay, here, I'm, I'm good. I have taken care of all of my duties. I'm going back to sleep for another five seconds or whatever that, whatever that was. But that was my first exposure to it. So I was like, okay, there is such a thing as. You know, like an operating system and this is all, this is on MSP four thirties.

**Brian Amos:** Oh, so already pretty, pretty low power to start with. Yeah.

**Chris Gammell:** So there are low power to start with. And these are like little 16, 16 bit microcontrollers that had, I don't know. I want to say that the, the code size of that thing was like 14 kilobytes. So it was like, okay, this doesn't need to be super, you know, have super high end microcontrollers or any of that kind of stuff. But yeah, so that was my first exposure to an operating system running on a microcontroller. And then later, you know, we, we found out, I think it was like the other big one around then. I want to say Contiki, but I'm not real sure. I don't think that lasted very long. And TinyOS kind of went by the wayside because they figured out that Ness C wasn't a great, they were writing the operating system in, and all the modules. Ness C was like a really cool combination of structural VHDL and C. So it was very, very modular. And I wound up, they kind of infected me with, with their design methodology because they would have these hardware presentation layers at the very, very bottom. And the job of an HPL was to expose like all the registers of a, of a given chip, right? So you had access to absolutely everything that thing did. And then above that, you have, you know, like this hardware abstraction layer. And the goal of the hardware abstraction layer was that you provide, let's say you have, you know, like an ADC or something like that. Your hardware abstraction layer just provides like a single function, maybe, or like read ADC and get back. It's like ADC read. Yeah. And that's it. Yeah. But the cool part about that design methodology in combination with this really cool structural VHDL kind of like routing stuff that they had was that it, your, your code was immediately portable and it didn't, it didn't matter what processor it was running on. It didn't matter, you know, the underlying IC that you're using, as long as you had written all that stuff and the top level code existed and it was there and, you know, you guarantee that it was going to work.

**Brian Amos:** So when you pour it to a new chip, you just have to rewrite the VHDL ish piece. Yeah.

**Chris Gammell:** So like if you have the same chip in two different boards and let's say you move some GPIO lines around or something like that, then in that case you would like rewrite your, your, your routes and all that kind of stuff with a VHDL ish thing. And then if you moved processors, then you would need to, you know, like rewrite the routines that access GPIO registers and the stuff that accessed your peripherals, right? Like timer peripherals, serial peripherals, that kind of stuff. But yeah, so, and I, I've fully adopted that approach and it, you know, it's served me quite well over the years. Yeah. Yeah. Yeah. To the point where you can, you know, using that level of abstraction, you can very easily write drivers for an IC and have them map across, you know, chips, boards, architectures doesn't, doesn't matter. So it, it pays dividends in the long run to, to architect things properly with a decent abstraction.

**Brian Amos:** Yeah. And like for testing then too, I'm sure that makes it easier for that as well.

**Chris Gammell:** Yeah. Well, that, that's the funny part. So I didn't, I found out about, you know, things like test driven development and all that much later. And, you know, like I, I remember reading James Grenning's book, TDD with embedded C, or I forget the title of it exactly, but test driven development with embedded C. I think I was like, man, all of my code is like super easy to test because it uses these well-defined interfaces. What do you know?

**Brian Amos:** Yeah. Yeah. Yeah. Right. Versus like, I'm sure the code that I write, which is like, it's all in one file. Yeah.

**Chris Gammell:** All in one file. That's bad. That's bad. Exclusively uses registers directly with, you know. Yep. Yep. Yep. Yeah. Got to do the bitwise math to get access to anything. Yeah. So, so, you know, multiple files is good. Yep. Giving names to the bit, to the bits is also good. You know, long strings, like, especially now with 32 bit processors, you know, long strings of, uh, of binary is not, not favored. Yeah. Yeah.

**Brian Amos:** So at some point, I'm sure you've had the thought I should just write my own real-time operating system. Never. Because it feels like that's. Nope. Really? Nope. Okay. It's, it feels like the other reading that I've done around this was from Jack Gansel. And it's like, it was like, uh, yeah, the, the primary, the number one RTOS out there is, uh, custom. Yeah.

**Chris Gammell:** And, you know, like at some point, if a program becomes sufficiently complicated, you're, you're kind of forced into it, right? Because, you know, you have some routine that's chugging through a complex math calculation or whatever. Right. And in the middle of that, you need to check to see if your, your buffer is overflowing or whatever. So you wind up with all these reads, these unrelated things sprinkled throughout. Uh, this long running process. And yeah, no, I, I have no desire to, to write my own, to roll my own RTOS. I'm very happy and grateful that other people are, are capable of. That's great. Yeah. Okay.

**Brian Amos:** Yeah. I thought I was going to, I thought I was going to trap you on that one, Brian. You, you passed the test. No, no, no. People watch bugger than me. Actually, I would like to announce my new Brian RTOS. No, no. I've announced you're in the Empire. Yeah.

**Chris Gammell:** I, I, I almost accidentally recreated portions of GRPC and for a project and I, I kicked my saw. I just didn't know about it.

**Brian Amos:** Yeah. That's good to, I mean, and that's what it kind of comes down to for a lot of this stuff is like, I don't know. So, I don't know when I, okay, I, I was in the hardware side for a long time and I'm trying to learn more of this stuff, but I just don't know when I would have learned this. I'm sure some people learn this in school, I guess. I don't know.

**Chris Gammell:** I mean, I, I had a, so I, I have a computer engineering degree, right? So it's, it's like a combination of hardware and software. So I, I focused on embedded systems in college and I, there was an operating systems course and I, you know, I took it.

**Brian Amos:** Was it, was it meant for embedded operating systems? No, no, it wasn't. Everything was, you know, it was all Linux. Yeah. It's like for writing Linux or Windows, right? Yeah. Yeah.

**Chris Gammell:** It was like, you know, it was basically a systems programming course more or less. And, you know, it was just, they taught you the basics of things and that was that. But yeah, I didn't really see a whole lot of utility for it until, you know, until you have that first project where it's like, man, this is a little bit more complicated to do. Yeah. And just a super loop. So.

**Brian Amos:** Yes. Right, right, right. Yeah. And, and again, you would, you would cross that threshold. You would, you would, so say you had a super loop project and then you were like, oh, this is not going to be good. When do you, when do you pull the trigger? When should people listening, I suppose it's the real thing, you know, and I guess including me, when should people make that, like just bear down and make the switch?

**Chris Gammell:** Well, you know, the first time you converting stuff is, can be surprisingly difficult, especially when you're new, you know, converting like a super loop program into, if you're the original author of it, then, you know, you at least know about most of the stuff that you haven't, you know, like, okay, I know that this system requirement runs and it's like, I've got requirements ABC and I know that all of those things exist. So then you say, okay, well, can I make requirement A into a task requirement B into a task requirement C? So the, it's really, if you find yourself sprinkling in calls that check on unrelated processes in the middle of a long running process, right? Like let's say, oh geez, let's say you have a block of data that you need to do some math on. And, you know, so there's a loop and you find yourself adding like, oh, every hundred iterations of this loop, I should, I need to go check on the UART to make sure that I don't get, you know, a buffer overflow and I don't drop characters. Like at that point, you know, that long running, that long running algorithm should probably be in its own task. And, you know, there should be a different way of accessing the data and making sure that the UART, because the UART ISR isn't really, you know, it's not really like a big deal necessarily, or maybe it is, and you actually need to break out of that long running task and, you know, go service that, that thing, that frame that just came across your, your serial line or whatever, right? It could be an abort, right? I've got this, I've got this calculation that takes 30 seconds to do. And, you know, you could just imagine someone like, you know, hitting a push button, like, you know, stop it, stop, stop. So, you know, attach, attach the interrupt of the push button to a, to a semaphore and, you know, yank. Yep.

**Brian Amos:** But, okay. So let's go back to the, so the, uh, the ventilator example. The one thing I wanted to ask you about that is, so you have this super high priority task, like keeping someone alive. Why isn't that always just running?

**Chris Gammell:** I mean, what's it doing, right? So does it ever have any.

**Brian Amos:** I guess when I hear something like high priority, I just think like, well, that's always going to be, you know, that's the highest priority. It's always running. So is that not the case? Well, if. I'm setting you up for a dunk here. If you couldn't, if you couldn't tell, this is a very obviously not the case. Yeah.

**Chris Gammell:** So it is, if you're, it's always running, if it has something to do. Got it. But the minute that your high priority task needs to wait on something, like let's say it's, it's set up to, I mean, I don't, sorry, I don't know anything about ventilators, but let's say it's set up. Yeah. I don't need to operate. Say it's set up to operate at like, I don't know, 20 Hertz, a hundred Hertz, whatever it is. And it's going to evaluate human scale stuff. Right. Right. You know, it's not super fast and you, you want to run this control algorithm for the ventilator at a rate of a hundred Hertz. Well, you're either, you know, you're probably going to set it up so that you have like streaming data coming back from your sensor. Right. So you already have data available. You don't need to wait on anything. And then you take the necessary steps for actuating, you know, the thing that you're the pump or whatever. Well, your processor is running probably at least several, if not tens or hundreds of megahertz, which is a lot faster than a hundred Hertz. Right.

**Brian Amos:** Right. Right. Yeah. So you have what? 10, 10 milliseconds. When, if, if you split it all into a hundred, second into a hundred, right, you'd have 10 total milliseconds for each window. So it probably doesn't take 10 milliseconds to read a sensor.

**Chris Gammell:** Probably not. Right. And, you know, especially if you've, if you've taken care of all of that in, inside of an ISR. So, you know, let's say it takes, it takes a millisecond for this thing to run. What are you, what's that task doing for the other nine milliseconds? Right. Well, that's, it's not running. Right. Because it's either calling a sleep function or it's waiting on some sort of a, you know, like a semaphore that's being generated by a hardware timer. If you want some nice, accurate, you know, every 10 milliseconds on, on the dot. Yep. It's, it's just, it's not doing anything. So then your other tasks are going to run. And if you don't have other tasks that run, then in the case of a non tickless mode, your idle task is going to just sit there and check to see if it's time to bring in another task or run the scheduler.

**Brian Amos:** Yeah.

**Chris Gammell:** And if you're in, you know, if you're fortunate enough to be running a, well, not fortunate enough to be, if you're running a tickless version of an OS, the whole chip just goes to sleep. Well, not the whole chip, but the CPU, right. And you can go into the power, whatever parts, right. Whatever, you know, power down, whatever you need to and go to sleep for a little while. So, so yeah, it's, it's not running because it doesn't have anything to do. It's, it's got nothing, it's got nothing to do, but wait. So that's, that's the reason it doesn't run. But the second that it does, it will be running as long as you haven't kind of, you know, screwed things up. And now all of a sudden it's got to wait for a different lower priority task. Right. That's holding a shared resource. That's called priority inversion. And that's, you know, that's, that's not a good thing. Ah, right.

**Brian Amos:** I feel like that always gets like pushed pretty early into the conversation as well. And I'm like, well, I still don't know what priority means. And you know what I mean? Like, it's like, I need to just understand these simple things first. Yes. Uh, so, okay. So now the vent sensor, it takes that millisecond. It's gotten nine milliseconds. And the, so the scheduler is like, okay, well we can go start updating the screen.

**Chris Gammell:** Yep.

**Brian Amos:** But the screen task is going to take 30 milliseconds. Yep. So like what happens not after that first nine milliseconds where it's like, okay, actually I had to go back and check the, the vent sensor again. Yeah.

**Chris Gammell:** So, uh, the scheduler is going to, so either the scheduler is going to run, like if you call a delay function or whatever, right. Or it will update some software timers or something like that. Or if you, you know, it kind of depends on how you have it set up and how accurate you want that periodicity to be. Right. Basically there's going to be some mechanism, either a software timer that goes off or the scheduler, while the scheduler is controlling software. Timers in free RTOS, but you're going to have something wake up that high priority task again and say, Hey, go.

**Brian Amos:** Yeah.

**Chris Gammell:** You know, it could be, it could be giving a semaphore from, you know, like if you want a really high resolution, high fidelity timing to, to hit that, you know, that 10 minutes, like seconds on the dot every single time, then you probably set up a hardware timer peripheral. And that would, you know, just give a semaphore that your high priority task is waiting for. And then, so inside of the, your, your ISR for this, you know, this 10 millisecond repeated timer in hardware, the only job of that ISR is to just give a semaphore to this task or, you know, there's, there's also task notifications. And then the, you know, the moment that that task receives that notification or semaphore, it's going to, the scheduler is going to swap it in, uh, into context and then it'll, it'll do its thing.

**Brian Amos:** Yeah. Okay. That's great. Yeah. So like if, if I had like a slow-mo camera of a screen that's updating, it's like just rastering across for the first nine milliseconds. Yep. I might see a quick pause as it's going to check the sensor again, but then it would just continue. It would effectively just continue on.

**Speaker ?:** Yep.

**Chris Gammell:** Yeah. Yeah, exactly. And, and the beauty of, you know, task priorities is that that's happening all the time, you know, no matter what. And it just, if, if everything is working properly, it, it, it looks like magic because things are just happening. Yeah. You know, it's perceived to be in parallel.

**Brian Amos:** Right. I think what's crazy to me is that this is actually what's happening on the computers we're running right now. I mean, obviously there's more threads and, you know, they actually, but it's not but like, yeah, we actually have computers do this stuff too.

**Chris Gammell:** Yeah. They, they absolutely do. Right. Yeah. And you have multiple, multiple processors so that it actually is happening in parallel. You don't have just one CPU.

**Brian Amos:** Right. But it used to, it used to be more like the embedded ones, right? I mean, like it used to be more single thread. Yeah.

**Chris Gammell:** Yeah. Yeah. But you know, the, the thing that a lot of people forget is that modern microcontrollers, they can do a lot in parallel too, believe it or not, because. You have a lot of power buried in these hardware peripherals, right? So you've got hardware peripherals, you've got direct memory access controllers, DMA controllers. It's not that difficult to set up all of your communication to be DMA driven. And at the end, let's say you have like a block of 12 bytes coming back from some sensor, right? And it just, you know, that you're always going to get those same 12 bytes and you know, it's got sensor data in it. Well, you, you set up DMA with a, a transfer block size of 12. And whenever the DMA controller says, Hey, I've collected 12 bytes, it signals some tasks to go look at those 12 bytes. And that entire time, the CPU wasn't worried about collecting any of the individual bytes. It was off updating your pretty screen or whatever. So, you know, there, there are actual ways to get true parallel computing on a microcontroller, but you know, it's mainly for like communication. That kind of stuff. So it's not entirely, you know, they're, they're not as bad as single core microcontrollers or as bad as they seem, I guess.

**Brian Amos:** Yeah. But I've mentioned on the past episodes recently, I've been reading, I've been reading about a lot of like computer history at park, Xerox park and stuff like that. And they are talking about like early computing days. And it's like, no, no, no, they're doing it. They're doing that time slicing directly. You know, they're doing memory. They're moving memory the hard way. And it's just like, Oh boy. Yeah. Yeah. So yeah, we don't have to deal with me.

**Chris Gammell:** It's great.

**Brian Amos:** I mean, so you said, uh, when things go right, it seems like magic and I could totally see that. Uh, most of my stuff does not go right the first time. So how does one troubleshoot this? Cause I'd imagine it's a non, uh, straightforward process for troubleshooting in our toss.

**Chris Gammell:** Um, well, it, you know, it kind of depends on the tools that you have at your disposal. One of the reasons that I like ozone a lot is, um, it is free RTOS aware. So, uh, meaning, you know, if you, if you pull up like a standard debugger and now there are a lot of IDs that have gotten this right. But years ago that you're running the mill IDE, it could only look at one stack at a time. That was the, you know, the, the, the processor stack. And that's, and, and you could step through if you have multiple tasks, you could like step through tasks and that kind of stuff. But you couldn't like view multiple stacks at once. Right. So you couldn't view the context of multiple tasks at the same time. You couldn't just hit the pause button. You're like, okay, well, Hey, where's my sensor task? Where's my UI task?

**Brian Amos:** Where's, and this one's asleep. This one's asleep.

**Chris Gammell:** Exactly. And you can do all of that with, you know, things like ozone. And I think that for sure the NXP stuff has, you know, RTOS awareness. I imagine. Ozone is the SEGUR debunkers. Yes. Ozone is the SEGUR debunker. Yep. Yeah. And I think STM 32, their cube stuff, you know, they, they have RTOS awareness too now. So.

**Brian Amos:** Mm-hmm. And do they have to be aware of the specific type? Like they have to kind of understand the paradigm that free RTOS is specifically, or is it just kind of a broad? Yeah.

**Chris Gammell:** Because they're, they're actually looking inside the, the structures, like, you know, you have task control blocks for each task and that kind of thing. So they're, they're actually looking at all of that to obtain stack information from what I, from what I understand. So, you know, it's, it's not just, it's not, you can't use any RTOS and then all of a sudden, you know, everything is magic. Yeah. You know, you have to use something that supports the, the RTOS that you're using specifically. Yeah. Yeah. So there's, so there's that, and you can, you know, be able to hit a pause button and, and get some insight as to what task is currently running, which ones are in the block state. You know, you, you wind up being able to dive into a stack of each task very easily. You know, just, you know, unwind stacks and that kind of stuff and see local variables and all that. So you get all that for free. And then if you wind up running into really interesting problems with, you know, tasks not completing or a task is seemingly never running, you know, it's, it's, it's starved for resources, that kind of stuff. In that case, there's, there are a couple of different products. So Sager makes something called system view, system viewer, and it basically gives you a graphical representation of which tasks are running.

**Brian Amos:** Yeah.

**Chris Gammell:** And their priority. And, you know, it's just all laid out very nicely. There's another product called Persefio Tracelizer, I believe.

**Brian Amos:** God, that's a terrible name. Yeah. Yeah. And I think that's like, has it been around a long time? Cause it sounds like a long time.

**Chris Gammell:** I'm not sure how long, I mean, I, I've, I'm trying to think I first found out about them and.

**Brian Amos:** Sorry. If you work there, I'm sorry. I just, I, I have, uh, you know, dislike for many, many names of things. You know, it's like we're letting engineers name a lot of things. And as an engineer, I'm still offended.

**Chris Gammell:** Yeah. Yeah. Likely named by an engineer.

**Brian Amos:** Um, yeah, it's fine.

**Chris Gammell:** On the upside, you know, they, you know, I guess you could say that they probably didn't put a whole lot of money into the marketing department. That's true. They focused on. That's right.

**Brian Amos:** They're not wasting money.

**Chris Gammell:** They're pouring it back. That's how you wind up with names like that. Or, you know, it was trendy in the nineties or whatever. I don't know how. Yeah. That's what I was really figuring. Yeah. Yeah. I have no idea. But you know, same kind of thing. And that's, that's actually a little bit easier. It's way easier to get set up with Tracelizer than, than system view. Yeah. For free RTOS, because it's just directly. So free RTOS has all these trace hooks built into it and you actually have to go in and like, you have to kind of manually patch in a bunch of stuff. Tell what it is. And yeah. Yeah. For, for system view, but Tracelizer just kind of works out of the box, which is awesome. It's very pretty. You can, you can just see, you know, which tasks are running, which ones are interrupting others. And they give you statistics on, you know, all the tasks, how long they've been in the block state, that kind of stuff.

**Brian Amos:** Mm-hmm.

**Chris Gammell:** Yeah. And at least with system viewer, they also, you can also effectively tie like a really efficient printf debug that gets automatically timestamped and cross correlated with the real time graphing of all this stuff. So that winds up being super helpful too. So, you know, you, if you, if you need to orient yourself, you can give yourself little, little printf breadcrumbs in different tasks and then you can kind of cross correlate things temporarily that way.

**Brian Amos:** Yeah. So you have a really good on page. So people that are following along on page 48, which I think is chapter two. I'm not sure. Page 48 though, you have a realistic task setup and preemptive scheduler. And like, this is what I imagine I would want most things to look like. It basically is a graphical representation. People are looking, if they're looking at this with their mind or their ears right now, they would basically see like how many times the task is run. And then like, as the task gets sliced up and then like the scheduler being part of the task as well, because it does take time. The schedule has to take time to like feel like what's next and figure that stuff out. Yeah.

**Chris Gammell:** Yeah. And when you're using these tools, this is actually like one of the views that you have. Right. So this is, this is what shows up on, you know, on page 48 is, Hey, look, here's, here's everything that ran and, you know, here's why it couldn't run.

**Brian Amos:** Yeah, exactly. Exactly. And like, I think the, so now I'm a little confused again with priority. So if priority is going up. Yeah.

**Chris Gammell:** This is not Cortex M priorities, which are inverted. So, so higher priority is more important in, in, in this world. Okay. All right. So it makes more sense to me. Cortex M priorities lower is more important, but that's not, that's not the case for, for. Yeah.

**Brian Amos:** Cause is Cortex M the one that also goes negative as well when you need to like really do crazy important stuff.

**Chris Gammell:** Yeah. I mean, you have like non-maskable interrupts and that kind of stuff too. So. Ah, yeah.

**Brian Amos:** Okay.

**Chris Gammell:** I'm not sure. I don't know if it starts at zero or if there's a negative number off the top of my head. Yeah.

**Brian Amos:** Yeah. Okay. I feel like generally this graph is, is very useful to see here because it's, and stuff like this where it's showing like some things are, some, some of the bigger tasks are getting split up and anything. And so in, yeah, I guess I certain people should get the book. Maybe we can screen. It looks like you have a CC attribution. Maybe we can drop this into the show notes as well.

**Chris Gammell:** Yeah, absolutely. Yeah. All the images, all the images in the book with the exception of one image that I got permission from ST to use of the, of the dev board used in the book. They're all, you know, it's all creative commons. So you use them as you see fit. All right.

**Brian Amos:** We got some art for the show now too.

**Chris Gammell:** That's great. Oh boy. As long as you have attribution.

**Brian Amos:** Yeah.

**Chris Gammell:** Yeah. CC by so.

**Brian Amos:** Yeah.

**Chris Gammell:** Yeah. Remix them. And there's, I mean, you can even get the source. These were all done with draw.io. So, you know. Oh, cool. You can, yeah, it's awesome. So, you know, it's the, the PNG there's my, I think my personal GitHub repo has like RTOS images or something like that. So they're all in there as PNGs and they have the embedded draw.io source inside of the image.

**Brian Amos:** Okay. Great. Great. So scrolling through this book, like I said, I highly recommend this book. Scrolling through to page 98, you show digi-key, a digi-key window and you show a bunch of STM 32 parts being available. What universe is this in? Well, this book was written in 1995.

**Chris Gammell:** I used bubblegum tap shoes. He knows the code word. So I checked yesterday and Mouser actually had 32, 32 of the dev boards, the, the, the nucleo board that's used. Dev boards. No, no chips. I don't know. Dev boards you can use other chips. I don't have chips, but yeah. Yeah.

**Brian Amos:** We're trying to get people through the content here, not the, not, not to be able to build a thing at the end.

**Chris Gammell:** Well, you know, I mean this, to be fair, this was, this came out in 2020. But it's true. Yeah. You know, but it was written in 2019 and then it was just like finished up. Yeah. Yeah. We didn't have to write in time for people to be locked in.

**Brian Amos:** Yep. Yep. Well, a lot of the, so you have exercises in the book. It's all based on the nucleo F seven. The, I remember it's got the ethernet port on it. That's what is important to me. Yes. Yeah.

**Chris Gammell:** Yeah. So you have a nucleo F seven for all the exercises. And the cool part about that is one of the reasons for choosing that board is that you can actually reef that has an onboard programmer on it. Right. So an ST link V two. Right. And you can actually go through and reflash the firmware that runs on that ST link and make it look like a J link.

**Brian Amos:** Yeah.

**Chris Gammell:** So Sager has, and there are instructions on how to do that both on Sager's website. And, you know, I think I probably just put a link in the, in the actual text of the book there, but so it winds up looking like a J link rather than an ST link. So you can use all the sacred tooling on like a trial basis for non-commercial kind of stuff, which is, which is a neat feature.

**Brian Amos:** And that then enables things like system view and ozone or is it just. Okay. All right. Yeah. Yeah. That's nice. Yeah. Yeah.

**Chris Gammell:** So, you know, you wind up with like this, you know, effectively a professional grade debug set up, you know, just with a dev board only, which is awesome.

**Brian Amos:** I have, I have a $600 Sager programmer, J link.

**Chris Gammell:** Yes.

**Brian Amos:** Yeah. And I didn't need it. Apparently.

**Chris Gammell:** Yeah. Yep. Yeah. You don't, you don't need it. Not for this. I mean, you know, the, the minute you make your own board.

**Brian Amos:** That's right.

**Chris Gammell:** That's the reason I bought it. Yeah. Yeah. Yeah. Yeah. Don't, don't put, don't put dev boards into products. Don't do it. That's right. As tempting as it may be.

**Brian Amos:** It's bad. It's bad. So if people are going through the book, then what should they expect to learn kind of by the end? Like, I mean, there's different chapters, there's different topics, obviously. Is it like, should someone be able to build an entire system by the end? Or is it more kind of a piece by piece?

**Chris Gammell:** So it depends on your background. Like there is no, so it, it, like, I think chapter 13, that's where everything kind of gets pulled together. And there's a little, like a little project that blinks an led. So it, it has USB connectivity to your computer and it's got like this little Python UI and it's got a couple of buttons. So the, the discovery board has a few LEDs on it and you can control the brightness of each LED with little sliders on the UI. And that, that kind of chugs through building up this message and there's a, you know, there's a message receiver and then there's a couple of different tasks they're running to control these LEDs. So, you know, if you, if you actually follow through up to that point, at least then, you know, yeah, you can, you can get started that as soon. So what, one of the things that, that this doesn't do is, you know, it, it starts out with a code base. So I think, you know, you get like several dozen pre-configured projects and configurations inside of projects for STM cube. So like you, you, you clone the repo and then you just import it into STM 3D cube. And, you know, it's effectively just an eclipse ID. Right. And then all of a sudden you have, you have access to all these examples, you know? So, so if you start from any one of those examples, it's really designed so that you can play with the examples, break stuff and see. It's totally the right way to do it. Like how it broke. So you have this sandbox to start from. So what, what it doesn't do is it, it in, I don't think anywhere in the, in the text, does it take you through like, okay, now open the ID and select the discovery F7 board and select free RTOS. And honestly, like that, a lot of that stuff changes so quickly that you're anything in print isn't going to be able to keep up with it. Most likely.

**Brian Amos:** I mean, even YouTube, like I, I find YouTube videos and I'm like this, this tool, this tool chain is completely different now.

**Chris Gammell:** Yeah. That's the crazy part is that like, you know, with a lot of this stuff, they have all these silicon manufacturers. They're, they're coming out with all these really cool tools for configuration, but it's very difficult to use them long-term. If you have a long running project that needs to be supported, you know, you, you wind up either needing to kind of divorce yourself from the, from the actual like setup portion of it and like, just make a, an archive of the project. Right. And then just deal with the actual source that matters because, you know, in five years, you're, you're not going to be able to like add in another GPIO line that you need to access or reconfigure this extra spy, you know, this extra peripheral for, to do whatever task using the old project with the new IDE, right? Like it's just, it's, it's moving too quickly. So importing source, knock on wood that, that process changes much more slowly, thankfully.

**Brian Amos:** Yeah. Yeah. Yep. So. Right. I think it's just then when you do need to dig through all the registers that set things up and whatever, you either need to start from a project like you were offering here, or you need to be prepared for some time with the reference manual and really making sure things are right.

**Chris Gammell:** Yeah. Well, and that's the, that's the strong point. A lot of these ideas too, right? Is that they're very good. Well, some of them, NXP more so, I think they're, they're very good at creating like a workable starting point.

**Brian Amos:** Mm-hmm.

**Chris Gammell:** But after you get that initial setup, I, you know, my normal workflow is okay, look, I've got, I know what registers to tickle. I know what bits in the registers and all that. Okay, fine. Let's bring all that in and make it, you know, let's make it our own and then put an interface. Right.

**Brian Amos:** And I'm never touching cube again for this project, right? Exactly.

**Chris Gammell:** Yes. Yeah. And, and I've, you know, I've talked with engineers, other engineers are like, oh, how do you get cube to, to play nice with your code? I'm like, you don't. Yeah.

**Brian Amos:** No, I feel, yeah. I've done the same thing. And it's like, if I really then, if I'm like, okay, well, I really need to reconfigure this, whatever. It's like, start a new project with cube.

**Chris Gammell:** Yeah.

**Brian Amos:** Make it output the stuff and then do a diff between the two files. Just be like, oh yeah, that's different there. Yeah. Exactly. Yeah.

**Chris Gammell:** And then, you know, if you do that enough, eventually you start finding similarities and you're like, okay, I need to, I want to change the mode of this GPIO line, for example. I do this a lot. Well, you can actually just create, create your own abstraction for it. Right. And then, you know, at that point it's, you know, now you're, you're starting to think like a software engineer rather than a hardware engineer. And, you know, like, how can I make my own life easier down, down the road? Right. Yeah. But that's right.

**Brian Amos:** I feel like that is probably the best of both worlds too, because it, or the best solution for people in your, and sort of my scenarios where it's just like, you still have the under the hood control versus like, you know, being handed a bunch of hardware abstraction layers and you just don't know what's happening. And you're just like, well, boy, I hope this ADC gives me a reading back when at some point, you know, or, you know, boy, I hope that GPIO eventually goes on.

**Chris Gammell:** Yeah. And some of them are terrifying because they'll, you know, depending on what you wind up with, you know, they're doing stuff inside of interrupt. Like they, there's some, some cases where they're literally delay functions called inside of ISRs and some, in some of this stuff. See, I know that's bad. Yeah. It's, it's, I mean, you can't always avoid it if you're waiting. So if you're in a tight loop, like, you know, waiting for, uh, you know, like the last bit of, of a bite to come in or whatever, right? Like, Hey, you've got something in your received buffer and, or I've got something going out of my transmit buffer. Now I need to pull and wait until it's complete. Like, okay, that's one thing, but finding out that you're delaying 20 milliseconds while you wait for an ADC to warm up between, before you take a reading, like, Oh no, you're in an ISR context. Oh geez. That's not good. Can't do that.

**Brian Amos:** Yeah. It just blocks, blocks at all. Huh? Just hope you're, hope you're, uh, your overall system rate is less than a hundred hertz. Yeah.

**Chris Gammell:** And, and yeah, exactly. And that, you know, that kind of stuff happens. So yeah. Yeah. Be aware.

**Brian Amos:** So like in that scenario, how do you find that then? So then you'd be like, so just to tie that back to the system viewer and the other stuff you talked about. So like you'd then see that task kind of just hanging there or what would you see in terms of a debug?

**Chris Gammell:** Yeah. So like if you're, so if you had all ISRs instrumented, if you added instrumentation code, like, you know, enter ISR, exit ISR, then you would actually see the ISR show up right on the screen. And you'd see that you're spending 30 milliseconds inside of this ISR. So barring that you would just see like a blank spot on the screen, for example. Right. And you're like, oh, well there must be some sort of an ISR being, being serviced. Oh, what the heck is that? And then you can kind of go through and start poking around there.

**Brian Amos:** Yeah. Okay. So if you have a blank spot, right. Can you see like, well, task number one always runs before this blank spot. So then you might go and instrument test number one.

**Chris Gammell:** It might not though. Right. So if you're, if you're asynchronous to that task. Now this is, this is where my, my other, you know, favorite tool comes in. So I typically run with, you know, pretty much always, you know, at minimum, some sort of a debugger, right? If you're doing a lot of this timing kind of stuff, system views or something to visualize tasks is nice for complicated troubleshooting. Certainly, you know, good old print F is kind of nice to have for other, other reasons, but a logic analyzer, right? Just, just instrument the crap out of everything significant coming off of that processor and just leave it there. Right.

**Brian Amos:** Like the entire time you're doing system integration, man with extra pins on his boards, folks.

**Chris Gammell:** Well, no, no, no, no, no, no.

**Brian Amos:** Okay. All right.

**Chris Gammell:** If it's coming off the processor and you're going to an external chip, the it's already there, right? You have a trace somewhere. I mean, assuming, okay. I, so a lot of the stuff I work on is bigger. You know, I can afford to actually put down like a very, very tiny test point.

**Brian Amos:** So you're not saying like, you're not, you don't have like 16 extra GPIOs that are going out to a digit. No, they're not extra.

**Chris Gammell:** You're saying like. Instrument your external buses. That's what I'm saying.

**Brian Amos:** Okay.

**Chris Gammell:** Right. So, you know, so if you're, if you're accessing some external chip and it's a zero bus instrument and then you get a, it's amazing how much you can learn by just like taking a glance over at your, your logic analyzer screen. And, you know, you, you, you get, you, it's like a, it's like the pulse of the system, right? Like, you know, you just glance over there and, you know, you see these little heartbeats because you know that, you know, this, this ADC is always accessed every 10 milliseconds. And then, you know, you, you can start, if you have a couple of extra GPIO lines in that case, you bring those out and then you start, you know, you just go to old GPIO toggle, right? But if you do it with a logic analyzer, then all of a sudden you have really high resolution. And if you have a problematic ISR, then you just toggle a GPIO register at the beginning and then, you know, neither, you know, do whatever you need to toggles or highs and lows, whatever, you get a really clear idea of what's going on.

**Brian Amos:** So when you say like instrumenting the external stuff, you mean like just putting test points down or literally soldering test points, physical. Yes. Yeah. Yeah.

**Chris Gammell:** I'm, I'm a, you know, I'm, I'm, I'm a really low level guy. So I'm not, you know, I, I, I have a, you know, kind of thing. I have a soldering art at my desk. I'm not just a, just a software guy.

**Brian Amos:** Solid. Solid. Passes, passes the amp power test. That's good.

**Chris Gammell:** I once talked to somebody and.

**Brian Amos:** You have chosen wisely.

**Chris Gammell:** Yeah. We're getting started on this project and, and he was, um, it's like an old school double E and we're talking and he's like, yeah, so what questions do you have? And I think the first thing I asked was, well, do you have a schematic? I was like, yeah. Like, whoa, I thought you were a software guy. No, it's, I mean, yeah, I'm, I'm brought into right software, but I need to know what the hardware is doing. Obviously.

**Brian Amos:** Yeah.

**Chris Gammell:** Apparently not everybody. This is not a buy box.

**Brian Amos:** But yeah. Hmm. So then, okay. So now you mentioned Amazon bought free art toss. They're putting more functionality in there, but then even like you also mentioned, you know, screens are coming in. So now you need to move up the stack and do more complex stuff at third party libraries. What does that then do for you as like this low level person that does understand all that stuff, but then most of the processing time is kind of at that, the higher level functions, like a screen maybe, or a, you know, wifi, wifi connection or something like that.

**Chris Gammell:** And again, that's, that's my, my bias towards prioritization, right? Like, I'm not going to say that stuff is extra, but it's less essential. Right. And in, in some cases, you know, maybe, maybe it's super essential to that particular product,

**Brian Amos:** but yeah, I think it's just the stuff that you've been doing for sure. It sounds like, you know, like high reliability type stuff, real things that actually need the real time piece of it.

**Chris Gammell:** Yeah. Yeah. So yeah, you just, you know, you, I mean, you just kind of, you just kind of accept it. Right. And then, you know, at some point there are always going to be trade-offs to be made. You know, uh, if you, if you have that kind of glitchy feeling UI, then maybe you need to like tone down the animations or something. I don't know. There's, you know, or. You know, there's, there's a trade-off to be made, right? You either, either throw hardware at it or, or simplify it. One of the two, but. Yeah.

**Brian Amos:** Okay. Are you feeling the pull of the embedded Linux space as well? Like, do you, do you feel that like either, I guess from, from, you know, your, your day-to-day

**Chris Gammell:** work or your work in your past? I mean, I've done, I've done a few embedded Linux projects. So it's, it's not something totally foreign. I mean, I, I like, you know, suffered through Yocto for six, six months, getting a system on modules set up and brought up and, uh, in a, in a fully networked environment. So, yeah, I mean, you know, depending on the, on the product, it makes a lot of sense. I'm not, I'm not at all opposed to full operating systems, but they're great. You have, you have a whole bunch of other people's code that you can use most of the time and get a whole bunch of functionality that you don't need to directly create, which is awesome.

**Brian Amos:** Yeah.

**Chris Gammell:** Yeah. And in a lot of cases, you know, what works really well is if you have very strict real time requirements and you have a little bit of wiggle room in your bomb, you know, just add in a microcontroller to do, you know, the simple hard real time stuff. And then, you know, everything else that requires these, you know, crazy stacks and protocols that you'd rather not look at or recreate or you can't or whatever, you know, run that on, on an OS and then, you know, just have some sort of a serial interface between them. So, yeah, yeah. Thankfully, hardware is less expensive every day. So, you know, some, sometimes we can solve problems with, with just more hardware every once in a while. Right. Yeah. As long as we can buy it. Yeah. Yeah. There is that. And then that's another good reason to write code that doesn't directly access your processor registers. Right. Registers. Right. Because it might, it's probably these days, it's probably going to be running on a couple of different processors.

**Brian Amos:** Yeah. Yeah, exactly. So then, okay. This is the last thing I promise. Cause I've kept you long enough here, but so then if you do have that, that co-processor there, right. And it's just doing a couple of small functions that would normally have free R toss as well. Or would that be, I guess, how often do you find yourself going back to super loop then? You personally.

**Chris Gammell:** Me personally.

**Brian Amos:** Yeah.

**Chris Gammell:** Whenever, if I know that something is simple enough that I'm not going to want to do anything concurrently, then, you know, sure. Super, super loop. It is no problem at all. It's great. The minute that like for, for new projects, I wind up, I guess the, the things that I create are often, the projects that I'm involved with wind up being large enough that at some point it's highly desirable to have some level of concurrency.

**Brian Amos:** Yeah.

**Chris Gammell:** So, you know, in that case, you know, it doesn't really make a lot of sense to, to try to shoe transform that into a super loop. If you've already got like a whole bunch of stuff that's operating well and kind of tailored towards an R toss. There, there's one case in the past where we had written a lot of libraries, like some, some middleware kind of stuff. And we actually couldn't afford the overhead of the scheduler that happened one time, you know, this processor was like just totally maxed out super, super tight timing constraints. And, you know, there was just no way to, to, to run an R toss on it. But in that case, all we really did was the middleware was created in such a way that, you know, instead of a free R toss queue, we were just using like an in-house ring buffer, for example. Right. So you can, you can, you can kind of, you can abstract things well enough that a lot of the code doesn't actually care what it's running on. At the end of the day. Right. It's just like, Hey, I have data for somebody else here. I'm going to, you know, get your data here. Yeah. And that's, and that's all it is. And it hands it off and you know, nobody cares. Yeah. Yeah. So in that case, you know, you have something that's super, super fast, you know, in that, in that middleware can run on, on whatever it does. It didn't, it could run on bare metal. It could run on an R toss. It could run on a full operating system. As long as you're, as long as you're not like, you know, tying everything super, you know, like really, really tight coupling between all your modules and everything. And you have consistent interfaces. You can just very fluidly move between things. That's, that's ideal. But I could work on stuff that has super loops. It oftentimes by the end of, well, so, you know, I, I think I, I'm in like the industrial space most of the time. Yep. So a lot of, a lot of our stuff has like some level of network connectivity, some level of, you know, like manufacturing test code and, you know, like all that kind of stuff. So there's usually it's, it's desirable to like add in other features that kind of need to operate with some level of concurrency at some point. So it just more often than not, it makes a lot of sense and it's not, you know, from like a ROM and RAM perspective, free R toss, especially it's pretty cheap. Yeah. There, there isn't a ton of overhead there. Yeah. So it's not like, you know, if you're, you know, you're, you're using like a Python interpreter or something like that where, oh yeah, look, I, I have this, you know, 256 K ROM and it's almost big enough for my, my 20 line script or whatever. I don't, I don't know how big the normal, normal runtime environment for that is, but

**Brian Amos:** you know. It is impressive how they squeeze it down these days, but yeah, it's a, yeah, it's still, it's sizable. Yeah. Brian, where can people find out more about you, about your book and buy your book and hopefully try it out. And also where can they find the, the boards to run? Sorry. That last one was a. Bubble gum tap shoes.

**Chris Gammell:** Bubble gum.

**Brian Amos:** Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Well, Mouser does have, well, as of yesterday, they had 32 of them. All right.

**Brian Amos:** See, he did his homework. He checked before he came on the show. That was really nice.

**Chris Gammell:** I did. I, well, I don't know. Who knows by today? Uh, but yeah, I'm, I'm probably easiest to get a hold of through LinkedIn. If you search for Brian Amos embedded, you'll be able to find me, uh, the books on Amazon. So that's nice and easy. You can email me directly, uh, Brian Amos at holistic embedded.com. And I've, I've got a landing page as well, but that's not really worth mentioning. Find me on LinkedIn. Yeah. Yeah.

**Brian Amos:** Yeah. That's great. All right. Well, thanks for, uh, first off, thanks for writing this book is really useful for me. And thanks for coming to talk about it today. Thanks for having me. This, this helped me understand it even more. So we'll have to chat soon. Thank you very much, Chris. Mutex Semaphore
