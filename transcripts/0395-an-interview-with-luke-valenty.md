---
episode: 395
title: An Interview with Luke Valenty
url: https://theamphour.com/395-an-interview-with-luke-valenty/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released June 3rd, 2018. Episode 395. An interview with Luke Valenti. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Luke Valenti from Tiny FPGA. Welcome, Luke. How are you doing? I'm doing great. How are you doing? Well, you know, this is an early... I'm not used to recording the morning. We're recording the morning this time. And I'm a little more caffeinated than normal. So if I ask crazy questions, I'll blame it on that. Likewise. Okay, good, good, good. So we're going to be talking FPGA. So should people be caffeinated themselves to listen to this? I mean, should people be excited about FPGAs? Oh my gosh, yes. You should be very excited about FPGAs.

**FPGAs:** Why should people be excited about FPGAs? Well, hopefully... Well, okay, so some background. I was just at Maker Faire Bay Area. And this was my first time ever exhibiting at a Maker Faire. Which was awesome. And on the very first day, on Friday, before it started, I saw a tweet from Arduino that made my heart sink at first. And it was that Arduino was releasing their own FPGA board.

**Chris Gammell:** Right.

**FPGAs:** And it has kind of a smallest form factor. You could put it on a breadboard. It's got some pretty cool features. And inside, my first reaction was, Oh God, what am I doing this for now? You know, I'm going to be crushed by Arduino. But then, you know, my more practical and realistic self kicked in and reminded me that, Well, you know, there's lots of different reasons. You know, we want FPGA boards and people have different requirements and things that they want to do. And it's actually fantastic that Arduino is getting into it. Because number one, it's a recognition from a very large, you know, influencer in the maker community that FPGAs are important for makers and hobbyists. And they're really, really useful. So it's kind of a confirmation of what I've been working on and doing here and what other people have been working on with, you know, with FPGAs for makers.

**Chris Gammell:** I think I'm going to challenge you on that one. I don't think actually most people need them. I'm personally very interested in them. But maybe you could explain to me when you think people should start jumping into FPGAs.

**FPGAs:** Okay, I've had a lot of practice because of Maker Faire. Yes, good. And if you look at Arduino Project and you look at some of the libraries, there's a lot of bit-banging libraries. And there's a lot of bit-banging libraries for things even as simple as serial ports for UART. Because for whatever reason, some people want a lot of serial ports. I haven't figured out exactly why they want so many serial ports, but they want a lot. And they want the maximum baud rate available. And if you're using software serial, depending on the board you're running on, you're only going to get 9,600 or a little bit more baud. And it's not always very reliable.

**Chris Gammell:** And they're using it for debug, too, at the same time, right? Yeah, exactly.

**FPGAs:** You could be using it for debug. And the more of these software serial ports that you add up, the less CPU time that you have for your actual task at hand. And so if you use an FPGA board, you can implement a soft microcontroller on it. And you can specify exactly how many serial ports you want. And not only can you do that, you could also set it up so that if you have a sensor on each one of those serial ports, you can have dedicated hardware for each one of those ports that will pull that sensor or that will record the data from the sensor and put it into a register so that your main program can be offloaded and not have to worry about those periodic tasks. So you could not know a single thing about Verilog. And with the right software and tooling... Check, check. Yeah, exactly. Which is, you know, almost everybody that I talk to at Maker Faire. And with the right tooling, though, you could put together a microcontroller that does exactly what you want. And so that's a major use case that I think is useful to anybody that uses microcontroller boards today, is being able to put together exactly the peripherals that you want and use them in your project.

**Chris Gammell:** Yeah, because I think... Well, I think about it at the beginning. It's almost like you have people that... And the reason that I pushed back on it in the first place, normally I wouldn't because I really do like FPGAs. But I think that the thing is people coming in maybe 10 years ago or maybe even more recently, it's like, well, you should really learn the constraints of the system first because if you jump right into... Let's see. Let's see if I can make an analogy. I'll use one of my favorites. Like, if you were going to use piano but your pinky didn't stretch to, you know, one of the keys, right? This is... What you're kind of saying is like, well, you'd move one of the keys to make it a little bit more convenient for that person. And so what I'm saying is that it kind of makes that person not as adept at practicing and stretching to get to that key on the piano. And I think that there's some value in that. But I think pretty quickly the idea is that the key needs to actually be moved. For certain tasks, the key actually does need to be moved and there's valid reasons to move that key. Oh, yeah. So my fear is always just that the people jump right to that and think that that's the solution right away. And I don't think that's the case, but I think that quickly it could be, right?

**FPGAs:** Okay. So I want to make sure I understand your metaphor. Could you make it more concrete? Moving the key corresponds to...

**Chris Gammell:** Oh, so like actually rearranging the piano keys. That's what I meant. Sorry.

**FPGAs:** Yeah. So, and that corresponds to what...

**Chris Gammell:** Not learning how a standard piano layout is, right? So like, so that's in this case, to go back to the normal example, right? So, you know, a lot of people in the Arduino community use like an Atmel 328, Atmega 328 rather, and like learning register sets and learning, you know, that there are constraints on hardware and that kind of thing. But I guess you were kind of saying that they do it with software anyways, right? So that maybe that, maybe that wasn't a good example.

**FPGAs:** Yeah. I mean, in the Arduino environment, there's a lot of abstraction between the hardware and being able to use it. And it's a double-edged sword. So there's positives and negatives to that. On the bright side, a lot of sketches that aren't too complicated can be ported from one board to another without too much fuss. Right. If you are going to using the registers immediately of a particular microcontroller, when you port it, you're going to have to port all of those specific registers over to whatever features are on the target board. Oh, interesting.

**Chris Gammell:** Okay. So you're saying that an FPGA and the flexibility of it allows you to have a standardized register set that people are used to dealing with. But you can...

**FPGAs:** I mean, you could do that if you wanted to. I wouldn't... I'm not necessarily advocating that. I like the idea of having the abstraction at the software level as long as it's not, you know, adding too much overhead. But on an FPGA, you could have... You know, and this is what would happen if you have a good tool for creating SOCs like MyGen. You're going to end up having a few different IPs that most people are using. So standard IPs for something as simple as a UART. Now, no matter what your CPU is that you might choose for that SOC, you know, you might end up using the same UART that everybody else is using because it's really well supported and it has the features that you need. And so, you know, regardless of the other configuration of your microcontroller, you're going to have the same UART. But I wouldn't expect that you would still be programming the registers directly for that UART. you probably would still want to use a higher level driver to talk to it just because it's simpler and you can get things done faster.

**Chris Gammell:** Yeah. Okay. Interesting. Cool. Well, so, you're saying that you think that FPGAs are a good starting place for beginners though too. Is that kind of what you're getting towards?

**FPGAs:** Yeah. Actually, they can be. Interesting. It depends on what you want to do. Yeah. So, if you want to learn FPGAs and you buy a Xilinx dev board or an Eltero dev board,

**Chris Gammell:** Okay.

**FPGAs:** then you end up downloading Vovato, which is 30 gigs. Good luck with that. Right. And it is a very powerful tool, but I tried it for the first time not too long ago porting one of my projects over and it has a very interesting take on user interfaces. Yeah, there's some interesting modes that it has between you know, doing design and implementation and options appear and disappear depending on what mode you're in and it's it's not the easiest thing to learn how to use.

**Chris Gammell:** Yeah.

**FPGAs:** It's not like a software IDE where you know, you can press a couple buttons and do exactly what you need. And that's partly because so many people use software IDs. You know, it could be even on the order of like a hundred thousand or a million times more people use software IDs than they use tools for FPGAs. So if you if you use that that's not going to be so great for a beginner. It's going to be pretty difficult and just the mechanics of getting the software installed getting a license on your computer and generating the bit stream is is actually complicated. On the other hand there's a tool called Ice Studio written by by a group of people that go by FPGA Wars. It's a parody on Star Wars because the kind of the creator is a huge huge Star Wars fan. He's Obi-Wan on Twitter with a J-U-A-N. Got it. It's mostly a Spanish-speaking community and they're all in mostly in Spain. Cool. But it's pretty fantastic. They have an incredible set of tutorials for people that really wouldn't necessarily have any experience even programming. Yet they have people doing projects on FPGAs using Ice Studio which is sort of a schematic entry tool where you can do schematic entry and then if you want you could also insert Verilog modules and then they have tools for sharing the modules and creating collections of modules and components that other people can use and remix. And so I've seen some really interesting projects come out of that like a remake of Pong with no microcontroller. I've seen Space Invaders and I've seen simple things like just somebody learning how to blink an LED for the first time on any dev board. You know even never mind the fact that it's an FPGA dev board.

**Chris Gammell:** Right.

**FPGAs:** Right.

**Chris Gammell:** Yeah I think that's one of the indicators of a dev board tool chain working in the first place is getting that first blink. Right? Yeah. Oh yeah. Okay. So you think though so the the idea though is that you think it is a a good path forward for people that are not that are not more experienced. You think it's okay?

**FPGAs:** I think that the major thing that we need is the tools. We need tools for people that can do things like create your own microcontroller and then take care of everything behind the scenes so that it works. We need tools like iStudio where you can do schematic entry and you can visually create digital circuits and put them together. And we need the open source tools that Tim and Clifford and others are working on because these open source tools are the ones that like the open source tool chain that's sort of the genesis of all of this. If you can release your tool chain open source and people can download it and they can redistribute it without having to get a license file without having to go to a separate website and then they can remix it whichever way they want what you get then is a really nice diversity of solutions on how to use it. So iStudio is one of those. It's great for beginners because all they need to do is download iStudio. That's it. They don't have to go to any vendor website to download other tools. They don't need to go request a license file. So the barrier to entry is really really low.

**Chris Gammell:** And that was Tim Ansell and Clifford Wolf both who have been on the show and we'll link those episodes if people have not heard those. Okay. Cool. Well that's okay. So I know I keep harping back to this point but like the reason I ask is because it's like I think about beginners and how confusing it is at the beginning and I've seen people struggle with Arduino even and it's like so it feels like this is another layer of things that need to be done but I didn't realize that people are still doing the digital logic piece and like mapping that out as well.

**FPGAs:** Yeah so if you go to Twitter and if you look at the FPGA Wars hashtag or if you look at Jesus, Jesus is another fellow that's working on iStudio and he's also working on APIO which is a Python module. I think it's like platform IO, similar concept for managing building for FPGAs. Basically you can initiate a project and then you can build it and upload it in just a few really really easy to use commands. that tool is fantastic. It makes it easy to integrate the Ice Storm and other open source tool chains into other projects. But Jesus and Obi-Wan, if you look at their tweets as well and related tweets, you'll see lots and lots of people making projects with FPGAs for the first time or posting the results of their tutorial that they passed. One has a huge list of tutorials. They're all in Spanish though so it's not very accessible for English speakers but they're working on translating that all to Spanish. You can see some examples, real world examples of people that are using FPGAs for the first time. From that perspective it's more education but some people are making some cool projects with it as well.

**Chris Gammell:** Okay. I was asking about the schematic drawing level in an FPGA. They're actually drawing out logic blocks and doing that kind of thing? Yeah. I didn't realize people were still doing that kind of thing. That's the reason I asked. Sorry.

**FPGAs:** Yeah. And that's a pretty gentle introduction to FPGAs. And then from there they can implement Verilog blocks which I think is kind of a nice next introduction into FPGAs. If you really want to use the full power of an FPGA eventually you got to learn Verilog so that you can implement your own hardware blocks. You're not going to be implementing a very complicated bit of hardware purely using schematic entry. That's just going to help you understand the concepts and learn the basics. But if you are interested in that and you're motivated then you'll want to move to more complicated things including Verilog.

**Chris Gammell:** Yeah. And I think whenever I talk to people at FPGAs I usually talk about the streaming nature of data. Because I think that making a custom micro is one thing and that's something you can do but I think that that ultimately adds more levels of complexity. But I think the thing that really starts to open up imaginations and really even distinguish FPGAs from micros because I think that's another thing that often doesn't happen as much as it needs to is just the concurrent nature of it all. Like understanding that you don't have to have it in a loop. You can have things where it's just streaming data through is kind of just an easier visualization for me at least. It goes through these different stages and at the end you don't have loops happening. You can just have these actions happening and at the end you have some kind of result.

**FPGAs:** Yeah, that's a great point. So when you do a digital design there's kind of two major ways of doing things. One is with a pipeline, a data pipeline where you can keep streaming data through that pipeline whether it's doing data processing on it, DSP operations, or implementing an I.O. protocol, or all of them. You could combine them all together in one big long pipeline. And the other side of that is doing control. State machines, stuff like that? Yeah. Typically you also need to have some control over your design and be able to tell it when to do certain things, when to stop, what to do next in some sort of exceptional scenario. And control is more difficult to implement in digital logic itself. But that's

**Chris Gammell:** also more akin to an if statement in a microcontroller, right?

**FPGAs:** Exactly. Exactly. And so in cases where the control is non-trivial, if the timing required of the control is not too tight, that's why I recommend using a microcontroller in the design or paired with the FPGA. Because it is a lot faster to write imperative code in C or C++ or your favorite language. It's a lot faster to write that kind of control logic in there than it is to implement it on the FPGA.

**Chris Gammell:** Oh, and so that's why you're saying to combine the two and build a soft micro into the FPGA?

**FPGAs:** Exactly. Exactly. So then you can take the complicated control, put that on the microcontroller. It's faster to compile and to reload that than it is to synthesize the design. And then the hardware or the part of your problem that requires either ultra low latency or it requires extremely high processing speed or very low power or some other metric that FPGAs are good at, you implement that in digital logic and you provide an interface to the microcontroller to control it.

**Chris Gammell:** Yeah, could you give us an example of that? Like a tangible example?

**FPGAs:** A serial port. Let's say a serial port that talks to a sensor peripheral, GPS maybe, or some other type of sensor. And then if you have a lot of sensors, you could create autonomous hardware agents that will automatically read from the serial peripheral. It'll perform DMA from the serial peripheral into either system memory of your microcontroller or into a register.

**Chris Gammell:** Okay, so is that like you'd read the GPS data sheet and then it would say, you'd say, read register one, read register two, do this thing, pull the data back, and then put it in this location? Is that the idea? Sure, you could do

**FPGAs:** that. You could, that's one example. I don't think that's a very convincing example. I have a better example.

**Chris Gammell:** Okay, great.

**FPGAs:** If you have a low power FPGA, like the ICE 40 series from Lattice, they can go to very, very low powers with very low power consumption. And let's say you have an internet of things node. And it's connected over Wi-Fi or LTE or some other radio, maybe LoRa. And the purpose of this node is to gather data, like many other IoT nodes. So it's going to wake up periodically, collect data, and transmit it over its wireless interface. If you have a low power FPGA, that FPGA itself can be collecting the data on behalf of your high power micro and radio. radio. And so that FPGA could be collecting 15 minutes or an hour of data in a very low power mode.

**Chris Gammell:** Okay.

**FPGAs:** And then wake up the microcontroller and the high power radio every hour or so to actually upload that data.

**Chris Gammell:** Okay. And so how would the low power micro, or sorry, FPGA actually be collecting that data?

**FPGAs:** So it would have its own digital logic implemented inside that pulls the sensor periodically and saves the data that it reads into an internal memory. And when that buffer gets full, it wakes up the larger micro and the radio, and then the larger micro can pull that data out of the FPGA and transmit it over its radio.

**Chris Gammell:** Hmm. Okay. And so the, I guess the thing I'm trying to get at is the, does in this scenario, does the FPGA have another micro inside of it or no?

**FPGAs:** Not necessarily. In this scenario, you would want the FPGA to have as little logic in it as possible and as slow of a clock as possible.

**Chris Gammell:** Uh-huh. Interesting. Okay.

**FPGAs:** Yeah. If you do that, then you can reduce the dynamic power consumption significantly.

**Chris Gammell:** Okay. And so you're saying that, so like a temperature sensor, let's say like a really dead simple temperature sensor, maybe it's I squared C based. The FPGA knows to wake up whenever it turns down, it's, it even turns down like the I squared C clocking and that kind of thing as well. And then sends some sequence of read commands, pulls the data back, stores it goes to sleep. That's, that's the idea. That's all it has to do.

**FPGAs:** Yeah, exactly.

**Chris Gammell:** Wow. Okay. That's great. Um, how, I mean, what would it take to actually go and write something like that? Is that, that's all Verilog at that point?

**FPGAs:** Yeah, that would be all Verilog and you could implement that with a state machine. And so for, for control logic, if you're not familiar with a state machine, um, it's kind of, you can kind of think of it like a flowchart. Um, and, uh, there's a lot of well-defined patterns for implementing that in Verilog. Um, something that, that I would like to do though, and I don't have the time for it, but it's something that keeps coming back to me. A lot of, a lot of these types of cases where you want to be able to take advantage of FPGAs, but you don't know Verilog or wrapping your mind around it is very difficult because it's a very different way of writing a code because you're not running a program anymore. You're describing how to wire up some hardware, right?

**Chris Gammell:** Yeah. Right.

**FPGAs:** So something that I've always wanted to be able to do or to see is a really simple way to let people write imperative code and just let it synthesize to the FPGA. And I'm not talking about, you know, complicated high-level synthesis where you're going to get the maximum performance and everything. I want something really simple where I can write a function, a control function, and it gets converted into a state machine that can then run on the FPGA. And then I can interact with that state machine from a microcontroller running on the FPGA. If I can have something as simple as that, even though I'm not getting the full performance, you know, that could enable somebody who only knows C and only, you know, works with Arduino. That would help them pick up an FPGA much, much easier and write, you know, a few different parallel processes, you know, on a whim. So let's say you need another thread to do some pretty simple thing. You can just write another thread that does that. And that can get compiled into a state machine and implemented in Verilog on the FPGA.

**Chris Gammell:** Isn't that, I remember, okay, so my FPGA experience is probably from like 2005. So you'll have to excuse me. But I remember there was like a C to H function where it was like you were, you had a micro on board, you had written some code for it, you highlight that code, and you say make it a hardware function. I think this was in Xilinx FPGAs.

**FPGAs:** Yeah. And Xilinx has a lot of high-level synthesis tools for doing exactly that today in Vovato. And it's much better than it ever has been. But I want, and there's been a lot of different high-level synthesis tools throughout the ages. I don't even want something as capable as that. And I don't necessarily think that we need something as capable as that. If you have the really, really capable high-level synthesis, there's a lot of sort of complicated rules on what you can and can't do because you're writing in C code. And getting good results can be kind of difficult because, you know, C and C++ are unconstrained and they kind of let you do everything.

**Chris Gammell:** Yeah, right.

**FPGAs:** So taking that and converting that into logic is hard to do. I want something even simpler and more limited and constrained in scope. Just so that, you know, you could implement something that works. And then later on, you could come back and either re-implement it in Verilog or use Verilog-like concepts to change the implementation to something more performant. Yeah.

**Chris Gammell:** I always liked that idea. That always helped me to understand FPJs a little bit more. Even though it's, I don't think it's actually an easy concept still. But like thinking about like, okay, so you're writing in C, you write some math function, right? Like X divided by Y plus some constant that's stored in memory. And it's like, you're going to be doing that over and over and over again. And like, usually in C, you know, you push that to your ALU and it's doing all the math functions, all that other stuff. But I always thought the C to H function was basically like an escape hatch. It sees that, it sees that function happening yet another time. It has a little escape hatch. It dumps the data down into this, this, this trap door. And then just an answer comes back up. Yeah. That's kind of how I visualized it. Does that, does that sound right or no?

**FPGAs:** Yeah. No, I think that's pretty accurate because for the most part, especially for control logic, which, which is significant, you know, most of your stuff is fine running on a slower microcontroller. Right. So, and every little bit of control logic that you add, if you're implementing that as logic, like actual hardware logic, every bit that you add consumes more resources and the resources on the FPGA are much more expensive than bits in a spy flash or SD card. And so the more that you can put on the spy flash as instructions, the better you can utilize the FPGA for the stuff that really counts, which is the high performance stuff, which could be pipelines or, or state machines that require extremely low latency.

**Chris Gammell:** Yeah. Well, that's an interesting point about resources and costs and stuff like that too, because I saw a presentation at one point, it might've been the hackaday thing, but there was someone talking about like the ping ponging of like parallelization of processes and how FPGAs rose in the 80s and 90s and kind of went back to like, oh no, no, micros are the big thing and now it's back to the, you know, it goes back and forth and back and forth based on technology nodes. Micros are pretty cheap. So what is, what is your response to just like, well, I could just throw another, you know, M0 at this or whatever. Why, why, why is FPGA needed in the, in the world of cheap micros?

**FPGAs:** I mean, if a micro does the job, then that's what you should use, right? You shouldn't, unless, unless it's for education or because you want to expand in the future or something else. But if you have a very cost constrained project, which many projects are, you don't want to be spending money on things that you don't need and a micro does the job, then that's what you should use. There's lots of fantastic micros out there.

**Chris Gammell:** Yeah. That $1, the amazing $1 microcontroller, one of my favorite articles of this year.

**FPGAs:** So yeah, I'll do a

**Chris Gammell:** call back to that.

**FPGAs:** Yeah. In fact, I have a tiny little programmer board that I developed for the, the A series FPGA boards. The A series don't have a built-in USB. And I kind of wanted to be able to use an FPGA for that because I have my own USB bootloader, but it turned out that, you know, it would be far more complicated and more expensive to do that. So instead I have this PIC microcontroller, which the only external devices that it needs is a 3.3 volt regulator and a couple of decoupling capacitors. And that's it. And it can work on USB and, you know, implement my firmware for, for programming over JTAG. And that was the right choice because, you know, that micro had everything integrated. So that's, that's a big difference between FPGAs and micros. And it's something that I wish the smaller FPGAs had more of. I kind of wish they had more integrated voltage regulators and clocks that are more accurate. So the, the PIC microcontroller, you need a certain amount of accuracy for USB. And so this particular PIC microcontroller can adjust its clock based on the synchronization packets coming over the USB wires. Oh, nice. And so it actually will adjust its clock on the fly as it's operating in order to do that. But in FPGAs, at least all the ones that I've used, you don't have a fine enough adjustment of the clock to be able to do something like that. So you have to have an external clock.

**Chris Gammell:** I mean, I think that that, that's also kind of a, so like in my mind, FPGAs versus micros, like the micros started effectively with FPGAs, you know, it either started in the designers' minds or they started on a board as an FPGA in, you know, but eventually they, they just kept getting optimized for their situation and then people kind of pull them off the shelf and say, oh, well this will probably work for mine too. So what I'm trying to get at though is like, when, when should people think, I mean, obviously, you know, we talked at the beginning too, it's like, yes, it's okay to start at the beginning with an FPGA as well, but in the world of cheap micros, where does an FPGA stand out as a, as a, um, a situation? Like, especially because our listening audience probably already uses micros. When should they think about switching an FPGA with the, with the tiny FPGA?

**FPGAs:** So things that FPGAs are fantastic at, um, one is being able to customize, uh, let's say you are using a micro, you can customize exactly the peripherals that you want to use. That's, that's one thing that's nice. Um, two, you can be sure of all of the hardware that you put into it because you can see the actual, excuse me, because you can see the actual source code for that hardware. Um, if it's open source, it's not open source, you'll have a hard time getting that into your FPGA. Um, yeah, like one of

**Chris Gammell:** the industrial ones, EtherCAT. FPGAs allow you to

**FPGAs:** like all those, yeah, have room for change in the future. So if you think a protocol might change in the future, let's say you're developing a product, um, a commercial product and you need to interface over a protocol like can, or I don't know, just some other kind of industry specific protocol. Yeah. There's, there's so many protocols out there and then there's also vendor specific protocols. And if you want, you could get a micro for many of those, but if you want to have, some future proof in your hardware design and you want to be able to get ahead of the competition and, you know, support those protocols the second they come out or the second that they're specified, you could put down an FPGA and then that FPGA can implement that protocol for you. And it can implement, you know, future protocols provided that they are electrically compatible. Or if you use something like FMC or some other expansion header, you can implement other protocols, even if they're not electrically compatible. Let's say you need to use a PHY layer in between or some passives or, or something else to do the actual interfacing. If you have that interchangeable hardware end, then you can do that as well. So then your main board can stay, you know, fairly similar or the same over time. And you can change the design that's implemented inside to account for either bugs or new features or new capabilities and new protocols. signals. And then if really needed, you can exchange the kind of like the hardware front end for the electricals to change out the PHY or connectors. And so it gives you a lot of flexibility in the future.

**Chris Gammell:** Yeah, it's almost like a business case too. Like you like keep selling the same hardware for a long time as well. Yeah. Like what's the one? So I have a, I got, I got for work, I got a video recorder. It's like a, you know, external recorder for camera outputs. And they would sell, they sold upgrades even for it where it's like you wanted, oh, you want like a, instead of having, you know, just two recorded streams, you could then do four, you could then do faster bit rates when they verified timing and everything. Nothing changed other than, than basically the bit stream that you, I mean, it just looked like a firmware update, but you could tell that there was obviously a, a, a bit stream that went down into, um, uh, into the actual device as well. And so, yeah. Yeah.

**FPGAs:** Um, another, another case where FPGAs are very useful is, um, in test jigs where you need to test your, your own hardware and you need to emulate the devices that your hardware might be connecting to. With an FPGA, you have full control. So you can perform the exact scenarios that you want and you can do it, you know, pretty much as fast as you want to do it. Um, depending on how your, your hardware supports it.

**Chris Gammell:** So this would be like if, if I was making a board that was plugging into the rest, like the rest of my system, you're saying that I could like emulate the cable plugging in, what the cable is plugging into and then like simulate signals that might be coming over that cable. Is that the idea?

**FPGAs:** Uh, from a logical connection perspective, yes. But if you're talking about, you know, sort of the analog characteristics of having a long cable, uh, you know, obviously you would need.

**Chris Gammell:** No, sorry. I just, yeah, I just meant that digital. Like, like, uh, so if I'm plugging, if I, if I have a processing board and then I have a sensor board and the sensor board sending back spy signals, but I can't, but it's, you know, a volcano monitor or something crazy like that. I don't have a volcano to monitor, but I need to still send back some crazy temperatures that I might have a stored file for. You're saying the FPGA could actually send those numbers back.

**FPGAs:** Oh yeah. And, and an FPGA could really control the whole process. Right. Yeah. Okay. Um, and so your, your entire, um, and this would be like manufacturing, um, testing, right? Your entire test suite could live there. Um, I've had people buy, I had somebody buy a, a, a A series board, two A series boards and two programmers. And these are like really cheap parts. One's $9 for the programmer. And I think it was, he got the $18 A series board and, um, he had them overnighted, um, with FedEx first thing in the morning across the country. And it was like, and it was to two different locations. So it was like 150 or $200 of shipping for a few dollars of, of FPGA parts. And the reason why is because this person was using the same FPGA in a product that he was developing and he was having some issues with his board and with the programmers that he was using. So he wanted to isolate the problem and try out the, the Verilog on the tiny FPGA board, which only has the FPGA and the absolute bare minimum of passives for the FPGA to function reliably. Um, and so there's a lot of use cases for these things. I've, you know, it's not just hobbyists and makers that are buying the tiny FPGA boards. Um, it is, um, you know, professionals, uh, that are, that are using them as well.

**Chris Gammell:** Well, let's walk through some of these, uh, some of the hardware. So, so you said A series and I believe I saw B series as well. So, so what is, what is the genesis of like, where did this all start and then what is the hardware today? Okay.

**FPGAs:** So it started a little bit more. Here we go. Here we go. This is, this is a little story. So it started a little bit more than a year ago and I love FPGAs and I've collected multiple FPGA boards and done pretty small projects with them. Just kind of messing around. And I really like this tiny form factor. Like I'm infatuated with it. Um, I, I don't completely understand why, but I just, I love the fact that I can have so much power and capability in such a small module.

**Chris Gammell:** And how, how, how roughly how tall, how big are we talking here?

**FPGAs:** The A series is 1.2 inches by 0.7 inches. Um, and the B series is 1.4 by 0.7. So the B series is about the size of an Andy's mint.

**Chris Gammell:** Andy's mint. Okay.

**FPGAs:** Yeah.

**Chris Gammell:** Those, uh, and you, you had said before the show, before we started recording too, it was similar to the teensy size.

**FPGAs:** Yeah. It's the exact same size. It's the same form factor.

**Chris Gammell:** Same size, but not the same pinout, right?

**FPGAs:** The pinout for power and signals I've kept compatible for power and ground. Sorry. Um, so that you could, if there's a breakout board for a teensy, you should be able to plug in a tiny FPGA board for the most part. There's some signals that, Oh, interesting. Yeah. There's some signals that the teensies have that I don't have.

**Chris Gammell:** Yeah.

**FPGAs:** Like the, and there's like DAX on board, right? Um, and so I haven't replicated those. And then there's other signals with headers that are in inconvenient locations, um, that I didn't break out.

**Chris Gammell:** Yeah. I was wondering, cause you have the, uh, well, I was also wondering cause I just, I just did something stupid last night and I was, I was, uh, playing around with actually soldering these down directly to a board. Uh, and it worked. I'll, I'll share that tweet. Uh, uh, I soldered a teensy directly to a footprint that I created. Um, uh, but I was wondering if it was the exact same thing because it looked like the internal, um, surface mount 0.1 inch headers were also the same on your board.

**FPGAs:** They, they are very, very similar. Um, the difference that I made, number one is, is the, um, analog signals, but number two, I added two extra ground pins. And so at the bottom of the teen C 3.2, there is a row of five through hole through holes for, um, for a header. I don't have that on my board. I didn't have space. Yeah. And so instead I, I'm actually

**Chris Gammell:** okay with that. I think that that's kind of a, I, I, yeah, that's where the DAC is as well. Um, and, uh, I'm not a huge fan of that because then you can't necessarily plug it into a breadboard because then that, that line goes across and they're. Yeah. If you use that, it makes a

**FPGAs:** little bit harder, but I think the use case, and I think one of those pins might even be like a higher power pin, or maybe that's just the teensy low cost. Um, but you can drive LEDs and stuff off of that or the, like those long programmable LED strings.

**Chris Gammell:** Yeah.

**FPGAs:** The, uh, WS2012. Yeah. So, so instead of using that, I added two extra grounds, which are really important for, you know, sort of high speed signaling on FPGAs.

**Chris Gammell:** Uh, do you, do you have people that are using it like that? The FPGA? Uh, with the headers on the bottom? Like, uh, plugging into teensy boards. That's what I mean. Sorry.

**FPGAs:** Um, not yet. I haven't seen anybody do that yet, but somebody did create a breakout for the BX board. Um, I think tall dog.com. Um, I have them somewhere. Um, he does, uh, breakout boards for the teensies and then he saw the, the tiny FPGA BX crawl supply campaign and he just emailed me out of the blue with his breakout board design. And I'm like, Oh, awesome. This is, this is one less thing that I have to do.

**Chris Gammell:** You know, thank you. Uh, yeah. Yep. I found it here. Okay. So it's just a way to get kind of a wider form factor. It looks like you can break out all the pins on the bottom. Oh, the stuff in the bottom too. I see. Okay.

**FPGAs:** And the way that he made these boards is really cool because he found these tiny pogo pins for the test points. And so he has this footprint that allows you to manually solder those little pogo pins, um, on the breakout board. And then when you put the FPGA board on top and you solder it in, all the test points make contact with those pogo pins. So you can even break out the test points.

**Chris Gammell:** Wow. That's, that's great. Yeah. And that's usually just used in your programming side of things. Is that right? Yeah.

**FPGAs:** So I have a, I have a test jig that, um, uses those, um, test points for testing out connectivity to everything as well as the voltage levels. And there's a reset signal for the FPGA. So when I program the spy flash, I have to keep the FPGA and reset. So it's not conflicting with the, the spy bus.

**Chris Gammell:** Okay. So, uh, between the A and so what is the difference between the A and the B series?

**FPGAs:** So the A series was the first board that I made and it's very simple. I, I basically went, I I was looking, originally I was looking for another FPGA board, um, the bug blat tiff. So that's bug blat, B U G B L A T Tiff T I F. And that was an even smaller board and it was powered by a mock XO2 FPGA and it had a USB interface chip on it. And it was really bare bones, but it was awesome because it was the smallest FPGA board, you know, that I could practically use that I could find. And so I had bought a few of them and then I wanted to buy more about a year ago. And the guy that made them said, well, you know, the yield on these boards was low because of the BGA package. So, you know, I'm only going to make them if you want to order a whole bunch like for education or something like that. And I wasn't really willing to do that because that would, that was getting very expensive fast. So I thought, well, here's an opening, you know, I would like to make this. And so if this guy can make it and other people can make these boards and I should be able to do the same thing. And so I went looking for FPGA packages that would be easy to use. And, and there's not really there's, there's, there's you noticed that, huh? Yeah. There's very few. There's some that are easy to use, um, in like a TQF F P or the, like the quad flat packages.

**Chris Gammell:** Like the really, really big, like the 200 flat packs. Yeah. Which totally blows out the form factor.

**FPGAs:** So I couldn't use those.

**Chris Gammell:** Yes, it does. Right. I mean, it was crazy too. It was like, you look internally, you're like, oh my God, it's just like, you know, it's a half a millimeter square of silicon, you know? Yeah. Yeah.

**FPGAs:** And so then I, I looked at the QFN packages. I found those, um, from Lattice, um, the mock XO2 packages or the mock XO2 FPGAs have QFN. And I thought, well, I should be able to do that. I saw, I saw a soldering tutorial on how to solder QFN32, you know, I might be

**Chris Gammell:** able to possibly go wrong. Yeah. What could go wrong?

**FPGAs:** So I actually ordered some breakout boards from Adafruit QFN32 breakout boards, um, which are nice. And then I just pursued it to destroy them, trying to solder chips on them because, um, I, I'm not really that, I wasn't really that great at soldering in the first place and QFN is, is not, it is not easy to solder that. It is, it is very difficult. So I, I quickly learned that the way to do that would be with a solder paste stencil and, you know, using a skillet.

**Chris Gammell:** And also we should, I mean, we didn't really talk about it, but you are mostly, you're, you're, most of your days, you're a software person, right? I mean, you have a hardware background, but you are software most days. So not, not hands-on soldering most days. That's what I'm trying to say.

**FPGAs:** Yeah. Especially when I started, I've gotten significantly better. Um, now I'm, I'm pretty happy with my soldering skills, uh, between through hole and, um, you know, hand soldering surface mount. But for surface mount, I almost exclusively use solder paste and stencils and reflow.

**Chris Gammell:** It's, uh, we, we, we, we advise people do the same here at the Amp Hour. So that's, that's good. Yep.

**FPGAs:** So cool. Okay. So I ended up designing a board with just a very simple board to kind of get my, you know, my feet wet and, and try it out. And, um, I send it off to, I look for some manufacturers. So I send it off to PCB way. And then I look at the quote and I'm like, gosh, you know, there's not a big price difference between like 10 and 250. I might, I might as well make 250.

**Chris Gammell:** Yeah. Why not?

**FPGAs:** And then, and then I, I got some prototype boards back and, um, you know, I reflowed them on a skillet and I used, I had some, uh, low temperature, um, solder paste, which was, which was nice and forgiving and easy to use for the prototypes. And I had like a $20 skillet that I used and I just turned it up. And then once it starts getting shiny and smelly, I decided, well, that looks like good. So I turned it off and I was lucky it was good enough. So I had my first, uh, 25 prototypes.

**Chris Gammell:** And this is the tiny FPGA A1, right?

**FPGAs:** Yeah. It's the A1.

**Chris Gammell:** So I thought, well, there's not much on these boards at all. I mean, there's no, there's a, it's, it's a micro or FPGA and a bunch of caps.

**FPGAs:** Yeah. It's a bunch of caps. It's some pull ups or pull downs. Um, I had a, uh, a ferrite bead in there and have some bulk capacitance. And for the, for the next gen, I added some LEDs because people wanted to power light and they wanted a, um, a user LED. Yeah. And I used way too low of a resistance value. And so the power LED is blinding and, um, would have done on all the AX ones, which I've, which I'm no, not the X ones. Yeah. The X ones, I've had a black permanent marker and I just dabbed the power LED with a black permanent marker so that people aren't blinding themselves while they try to look at their user LED, which is blinking. That's a good bodge. I like it. I like it. Yeah. So now I use a 10 K resistors on the LEDs because it's plenty bright and it's, they're just for indicating that, you know, you don't need it to light up the room.

**Chris Gammell:** So that those were both XO2. I actually don't know this family. Sorry. So, so it's a lattice. Yeah.

**FPGAs:** Lattice mock XO2. And those are kind of like a CPLD replacement. So they kind of, they kind of fit where CPLDs would have fit. And they use a FPGA fabric with LUT4s and routing matrix, um, with some distributed RAM. No, no DSP blocks. Um, but besides that, they're, they're pretty nice for doing embedded things and connecting up different IOs.

**Chris Gammell:** Is it, is it large enough to put a micro into those?

**FPGAs:** You might be able to put a really small micro.

**Chris Gammell:** Yeah. Cause that looks, I'm looking at your, your comparison sheet here. It looks like the, the, your board, the A1 has 256 logic cells, 2 K bits of distributed RAM. Yeah. 21 user IO pins. So that feels like, that looks like a CPLD to me. Yeah. And then the A2 has 1200 logic cells, take 10, 10 K of RAM, 60, or sorry, 64 K block RAM, and then some flash as well. So that looks a little bit more like you could fit a micro in there, but yeah.

**FPGAs:** I think a better use case would be to use it in conjunction with a separate micro. Got it. The mock XO2 have, has some nice integrated peripherals like a spy peripheral. And so that would be a great way, um, reuse that spy peripheral. Um, in your FPGA and connect it to whatever hardware you have and then use a micro controller external to control the FPGA over spy.

**Chris Gammell:** Got it. Okay. And so, and you're saying that's a hard spy block. Yeah. Yeah. Got it. Okay. Cool. That's good. That's good. Okay. So then what made you move to the BX? Why didn't you call it the B1? Oh yeah.

**FPGAs:** So, so from the beginning I wanted to have USB. Um, and so I looked up the cost of the FTDI chips, which everybody uses and it's, well, almost everybody. Um, and because it's compatible with the software and I just was shocked that they're like

**Chris Gammell:** five bucks. Yeah.

**FPGAs:** And for the mock XO2 FPGAs, I'm like, that's, you know, twice the cost of the FPGA. That's crazy. Like, why would I, why would I get that? And, and not a more expensive FPGA. And of course the reason why is because you still need a USB interface. Um, and so, so the, you

**Chris Gammell:** pay, you pay now or you

**FPGAs:** pay later, right? So the A series boards, I wanted to learn how this stuff works. And originally I wasn't going to, um, manufacture it and sell it. Um, this was mostly an exercise for myself, but then I like, well, gosh, it's so cheap to have just a few assembled. I might as well have, you know, 250 assembled. So I did that and I put a store up on Tindy and then I, I thought, okay, I really want to make an FPGA board that has integrated USB. And I think I can do it without an external chip.

**Chris Gammell:** Remind me, do, do most micro dev boards have integrated USB or no?

**FPGAs:** Um, the, the good ones do.

**Speaker ?:** Okay.

**Chris Gammell:** Like, well, and what you say good, the good ones, like expensive ones.

**FPGAs:** I think, I think, um, micro boards for, you know, that are easy to use. It's fantastic to have USB on it. Um, yeah.

**Chris Gammell:** Oh, no doubt. No doubt about that. I, I, let's just use Digilant as an example. Like, so like we've had Clint Cole on the show before and I, I like Digilant makes a lot of low-ish costs, you know, FPGAs. They do some big stuff, but like, do they put FPG or USBs in the board? Oh, you mean for FPGAs?

**FPGAs:** Uh, yeah. Almost every Digilant board that I've seen has USB over FTDI.

**Chris Gammell:** Okay. So it's not, I'm just wondering, it's like, is it a, is it a non-standard thing these days? But it seems like most, most boards will have it these days instead of using like a JTAG program.

**FPGAs:** Yeah. Most boards will have it. And I think it's really important to have that if you're trying to appeal to, you know, makers and hobbyists because they're used to having that USB capability and not having to use a separate programmer. And it's, if you can just plug it in over USB, it's, it's so much simpler and it lowers the barrier to entry. If people see that you have to also buy the separate USB programmer or FTDI programmer and they see what it costs, that's just going to put them off to the whole prospect of trying it out. Yeah.

**Chris Gammell:** Yeah. No, I think you're right. And I think at a certain point, the, the benefit of a, a dev platform in the first place is it, it's just like, well, I might as well try it like 30 bucks. Who cares? Right. It's like, it's worth, it's, it's worth just getting one and seeing how it goes. Exactly. Or, or in the case of like, you know, when I shop at Oshpark, I'm like, yeah, teensy 15 bucks in there or 18 bucks, whatever it is. Yeah. Throw one in. You know, it's like, yeah, that's great. I actually really like that. I think that enables weird, you know, having a, having boards on the shelf can actually really enable you in the future. Yeah. So, so, so mindless purchases, folks, that's what we're promoting here at the Amp Hour. Mindless purchasing.

**FPGAs:** Yeah. And that's actually a use case for the small FPGA boards as well is you need something implemented in digital logic or something quick. You don't have the parts on hand. You can use an FPGA board to do that.

**Chris Gammell:** Yeah. I think having, having something like these tiny FPGA boards on your shelf could get you out of a couple of binds. Yeah. Like you were saying with test jigs or just micro or just regular projects, you know, like I think that, yeah, you could, you could spin something up pretty, pretty last minute. Yeah. Hackathons.

**FPGAs:** Oh yeah.

**Chris Gammell:** Yeah.

**FPGAs:** So, so for the B series, I wanted, well, all my boards, I figured I would like to be able to offer multiple sizes at different cost levels at different price points because I really wanted, you know, if somebody can't afford the more expensive one, I wanted them to be able to get the less expensive one, at least to have that option. And so for the B series boards, originally it was going to be B1 and B2 because I had identified this chip I could use with the same package, same footprint, and it would work, you know, with, with different capacities. Well, the, the lower capacity one was hardly any cheaper than the higher capacity one. So it wasn't really worthwhile to have two different products. And so that's why you saw, you know, originally I just had the B2 out and there's no B1. It doesn't make sense. It'd be like $3 cheaper. So nobody would really buy it.

**Chris Gammell:** Oh, you, oh, you did have a B1. Oh, I didn't realize that. I'm sorry. I was just making a joke about that. Well, so there was a B2 board.

**FPGAs:** Yeah. So, so my original B series was the B2 board and it was called the B2 because I actually was planning on having a B1. But the B1 would have cost $35 instead of 38. And so it wasn't really compelling for anybody to buy that one versus the bigger one. And yeah, for the B2 board, that was a different, slightly different design. And it sold all 250 of them. And then they ran out of stock. And so then I was trying to figure out, okay, I need to do another manufacturing run. But there was a few things that bothered me about the B2. There weren't enough pins. I used a two layer board, which means that my ground plane on the bottom was like, you know, Swiss cheese. Swiss cheese. Yeah. There was cuts in it all over the place. And I wasn't.

**Chris Gammell:** I have a complaint about your board, which you actually did not rectify. And I wonder how it goes. Well, okay. I want to hear it. Surface, surface, surface mount USB connectors. Not even once. I don't, I don't, I don't, I don't, I don't mess with those. Why? How many people have been like, Hey, I ripped the FP or the USB connector off. Has there been a lot of

**Speaker ?:** that?

**FPGAs:** So far zero. Um, but there's only 250 of the boards of the B2 boards in people's hands. So that could change over time. Got it.

**Chris Gammell:** Um, but yeah, I would just like to state unequivocally. I always try and put through holes with the USB connector because I've ripped so many off of boards. Yeah. Even super glue doesn't help.

**FPGAs:** Yeah. And I think if I'm using the USB micro connector again and I'm doing another design, I'll probably move to a USB connector that has the, um, the through holes on the sides on the shield.

**Chris Gammell:** Yeah, exactly. Yep. Yep. Yep. Yeah. Just to get that lock from that. Yep. You'd still rip them off. I mean, a dedicated person such as myself has ripped off every type of USB. Yeah. Okay. So you moved to a four layer though. That's, that's good. Yeah. I'm looking at the, I think a picture of it. I think this is different because I don't see as many cutouts on the top side.

**FPGAs:** Yeah. So I moved to a four layer and then I, I committed some different, so I committed some BGA sins on the first one. And for this one, I committed some different BGA footprint sins. Okay. Um, what is, what is the BGA

**Chris Gammell:** footprint? So this is the ice 40.

**FPGAs:** Yeah. So this is ice 40 part. It's a 81 ball BGA with 0.4 millimeter pitch.

**Chris Gammell:** Ooh, boy. Okay. And this is, this is your first, first design.

**FPGAs:** This is my first BGA design.

**Chris Gammell:** Yeah.

**Speaker ?:** Ooh.

**Chris Gammell:** Yeah. We were talking about that on the show the other week. I, I, I have still not done one, uh, surprisingly. And, uh, we were, I was also thinking about doing this and Dave talked me out of it. So, uh, how'd it go?

**FPGAs:** Uh, um, not as bad as I thought it would be. So, so this package is absolutely not meant to be used on a normal PCB process. This package is meant to be used on a HDI, you know, high density interconnect process where you have either via actually you to route out everything. I think the official recommendation is to use via in pad with, you know, 0.2 millimeter vias and like a 0.1 millimeter drill. And then you have to fill and plate the, the via hole. Like plug the vias. Yeah. And that's expensive. Uh huh. That's, that's very expensive. And that was not an option because just to get prototypes for that, it would have cost, you know, thousands of dollars. And so I couldn't do that, but this is the only package in this capacity that would fit the form factor. So I had to use it and this was, and on the B2, I had, I had already done it on the B2, but one of my complaints with the B2 is I didn't have enough IOs. And so on the B2, what I did is I, because it's an FPGA, the IOs are very flexible. And most of the pins on that particular package are, are the IOs. And so for really important things like the spy interface, which is how you program the FPGA, they were kind of a little bit deeper in the footprint. And so what I did is I just routed over other pads. And, um, if you don't use it

**Chris Gammell:** for other, oh, you just, you just didn't, you basically covered up those pads with solder mask.

**FPGAs:** No, I wrote it, I wrote it over those. I wrote it over other IO pads that I wasn't going to be using, that I was kind of sacrificing. Um, they're not, they're not covered by solder mask. The pad is still there. It's just that, you know, on the schematic.

**Chris Gammell:** Oh, so you're just like driving a tri-stated pin at that point.

**FPGAs:** Is that the idea?

**Chris Gammell:** Wow. Okay. That's, that's interesting.

**FPGAs:** And so on an FPGA, if you don't use a pin, one of the IO pins, um, in almost all cases, it'll be tri-stated by default. So the driver's disconnected. It's not going to be doing anything. And so it's safe to do that. Um, yeah, as long as your users don't try and drive that. And, uh, most people don't try to do that because the only way you know that pin

**Chris Gammell:** very explicitly. Yeah.

**FPGAs:** And I provide pin constraints. So I provide a pin constraint file that shows the mapping of the pins to the, uh, you know, pins on the board itself. And then I provide a template that has a top module that has all of those pins listed so you can use them very, very easily.

**Chris Gammell:** Yeah. I'm guessing your users really want to, so like if I'm looking, I'm looking at the, the BX board right now and you have G and then one through 13 on the left side and 14 through 24 on the right side. And like, I'm guessing that your users want to be like pin 24. Exactly. Right.

**FPGAs:** Yeah. Exactly. And that's, that's way more convenient than, than trying to mess with the pin constraints themselves.

**Chris Gammell:** I mean, yeah, if you, if you don't have something like that, then the user has to create it and it just gets created over and over again. So as long as they're, you know, I think once they, if they're using a board like this and then they decide, no, no, I want to put a nice 40, 81 pin crazy BGA on my part, then you have to go and redo it. And it's like, yeah, that's really, that is the time to go do it. I think too. Yeah.

**FPGAs:** So on the B2 board, I was able to route over both power and signals and important control signals by kind of connecting them to the pads and then routing them all out. I had considered using solder paste, not solder paste, the solder mask to block some of the pads, but I rejected that idea because I was too worried about it messing with the BGA reflow process.

**Chris Gammell:** Right. Yeah. It could, and it could, I mean, like you can't really count on solder mask to completely insulate. Exactly. You could have weird intermittent problems too.

**FPGAs:** And then for some ground pins and power pins, I also had to, and even for some signal pins, I did this so I could route out some more signals. I used a via and I would gang together four pads and I would put the via in the middle of those four pads. Right. And it's a pretty big via, but there's solder mask. There's plenty of solder mask between the pad and the hole in the via. And the via annular ring is touching all the pads.

**Chris Gammell:** Oh, really? Oh yeah.

**FPGAs:** Wow. It's not cleanly fitting in there. I had no choice but to take, you know, two by two quads of pads and put a via in the middle of them.

**Chris Gammell:** And so what is, what is the constraint on your PCB process? What's the process you're using?

**FPGAs:** So I'm using PCB way and they can get down to four mil traces and spacing. And then the vias can go down to two millimeter drills with a overall diameter of 0.5 millimeter. And that's kind of their standard.

**Chris Gammell:** Is it 0.2 millimeter drills? Yeah. You said two millimeter. Sorry. That would be way too big. Yes. 0.2 millimeter drills. I was just, yeah, just gotta, I, I, you know, I'm a little metric challenge myself. So, uh, got to double check.

**FPGAs:** Well, PCB layout doesn't even help that much because it's split between metric and Imperial. I didn't, gotta, gotta, gotta get good at that 25.4 conversion. Uh, yeah, I figured that one out now, but I didn't even know what a mil was when I started.

**Chris Gammell:** Oh, wow. I had seen it on, uh, software into hardware, huh? You are, you are, I am impressed. I'm always impressed with people with you, like you who just go for it. You know, it's awesome.

**FPGAs:** Uh, I had a lot of fun doing it. That, that helped. That motivation really helped. That's good. So I was, so I was able to escape a bunch of IO for the board and the power and it worked actually, which kind of blew my mind. I was really, this is the first BGI I had ever done. I was able to assemble some myself. I could hardly believe it. Um, but for the B, for the BX board, I wanted more IOs. Um, that's something that really bothered me. So what I did to get more IOs out is I took the outer pads of the BGA and I squished them down to 0.1 millimeter and then I elongated them. So now there's some, they're like, Oh, okay. 0.35 by 0.1 millimeter. So they have about the same surface area and, um, they're going to be able to grab the, the balls and, and be able to wick them on and, and, and reflow. So, and I was able to get a lot more IOs out. I was really happy with it. Um, and so I ordered some. Are you, are your files online

**Chris Gammell:** anywhere?

**FPGAs:** Yeah. Everything's open source. So, uh, github.com forward slash tiny FPGA and the BX series.

**Chris Gammell:** What is the package type? What do you use to do it?

**FPGAs:** I use key cad or a key cad.

**Chris Gammell:** Hey, hey, all right. This is the long, this is the long con. I, I, I knew this in the beginning. That's the only reason Luke's a lot on the show. No, I'm kidding. I could actually tell from the beginning because, uh, you used, you use the built-in, um, text generator to say BX and B2. And I know that font by sight. Nice. Which is, makes me sad. Uh, okay. So that's good though. So, and I mean, people can view the Gerbers either way, right? So. Yes.

**FPGAs:** Uh, I should have the Gerbers up there. If I don't, I can add them. Yeah.

**Chris Gammell:** Okay. But they can also generate, generate them with.

**FPGAs:** Yeah. So people ask me to upload the Gerbers and they want to see the PDFs. Um, and I originally had thought, well, anybody can look at it because it's, you know, KiCad or, how do you pronounce it? KiCad or KiCad?

**Chris Gammell:** Uh, this is a contentious, uh, contentious thing. Gosh. I say, I say KiCad. I always say KiCad. There's actually a Wikipedia article that, that was recently amended to say KiCad because Wayne, the product, project leader says that. But, uh, the, the debate continues. Uh.

**FPGAs:** Okay. So I'll be careful then.

**Chris Gammell:** So I thought. There's a t-shirt if people are interested. They can pick a different side. Yeah.

**FPGAs:** I thought that using an open source FPGA or a PCB layout and schematic entry program, I would be safe from having to upload the Gerbers because everybody could download it and everybody could use it. But still people, they don't want to have to do that. So.

**Chris Gammell:** Yeah.

**FPGAs:** Then I relented and uploaded PDFs. And now I need to relent some more and upload Gerbers as well.

**Chris Gammell:** Yeah. I mean, there's, there's online viewers you can do too. I'm, I'm really waiting for, uh, I think GitHub will eventually do it as hardware hopefully keeps getting more interesting to them. Um, but there are online viewers you could do. So you might want to just upload the Gerbers to that too. And you could just link people to view the Gerbers. Oh yeah.

**FPGAs:** Not a bad idea. Actually, that gives me a good idea. I could, um, there should be like a JavaScript plugin somewhere.

**Chris Gammell:** Yeah, exactly.

**FPGAs:** And I could put that on my website.

**Chris Gammell:** Yep. That will save you some, I don't want to download this. Problems. Yeah. Yeah. So. Okay. So, so the, so you broke out more pins on the BX though. Yeah. So what, what is, what is the total count on the BX then?

**FPGAs:** A total of 41 IOs where 31 of them are dedicated to whatever function you want. And 10 of them are shared between the, the boot LED or the user LED, um, and USB and the spy flash.

**Chris Gammell:** So how would that work? Is it like once it's done and programmed, it can like switch modes or what?

**FPGAs:** On the spy flash, the easiest way to reuse those pins is if you have another spy device. Ah. And so you can reuse most of the pins and then have a separate, uh, chip select.

**Chris Gammell:** Okay.

**FPGAs:** Um, alternatively, if you're really careful about how you use them, you could share them with a different bus, um, or just LEDs. I mean, after boot up, if you don't use the, the spy flash, you can reuse most of those pins for, for other things, as long as, um, they're not conflicting, um, during boot up. And then for USB, you can reuse them as long as you don't need the USB interface. It just makes it complicated to use those.

**Chris Gammell:** That was another thing. Right. So it's a best case scenario to not use them, but you're saying that you can, if you're in a pinch. Exactly. So how would it work? So, so if you were using, so say you put a, uh, like an ADC onto the spy bus as well, right? So that's what the spy flash is normally pulling from whatever. Um, is that just because when the micro, sorry, when the FPGA wakes up, it hits the chip select for the spy flash, goes and reads what it, it's bit stream programs itself. And then it says, okay, now I'm an FPGA. I know how to talk to the other chips that are on this bus.

**FPGAs:** Yeah, exactly. So once the configuration process is complete, all of the spy IOs on this particular chip are handed over to the user design. And so the user design can do whatever it wants with them.

**Chris Gammell:** How do you expect, do you expect people to be using this mostly in dev projects and like, like wired together type stuff? Or do you think that people will eventually start kind of doing what you're doing and pulling, uh, FPJs into their PCB designs as well?

**FPGAs:** That's a good question. I think most of the people that are using it today with a few exceptions are using it for their own development projects, right? Not necessarily for a new PCB, but I have, I've seen a few people develop their own PCBs using the boards. And I've had a few people ask me, you know, if, if they use this, would, would I recommend using the same FPGA? Ah, okay. And I would not, I would not recommend using the same FPGA package. Ah, okay. Yep. Uh, because it's not really meant to be used in this way. And I would recommend a much larger package, uh, because it's so much easier to use. Even a larger BGA package. If you go to 0.8 millimeter pitch, it's so much easier. Yeah. Like it's, you don't have to do weird things.

**Chris Gammell:** I, I, you can, you're saying you can escape in the normal method, like on a four layer

**FPGAs:** board, no problem. Yeah, exactly. You can use regular size vias that don't cost, you know, crazy amount of money for prototypes.

**Chris Gammell:** What about, uh, I was going to ask again, because I've been playing around with this. Um, have you thought about doing a castellated design for your board? I have thought about it.

**FPGAs:** Um, but that makes manufacturing a little bit more complicated. So I'm not, I'm not familiar with castellated. So I, I might not know the ways that people work around this, but if all the edges, if the two edges are castellated, um, on the front, I also have the USB connector. And so right now on my panel, I route out the top and the bottom of the boards so that the USB connector has space to, um, to sit because the, the lip of the connector goes over the board a little bit. Got it. And then, so I can't connect anything there. Um, like in the, in the panel, I can't have any tabs there. And then on the sides, if it's castellated edges, I couldn't have any tabs there either. Yeah. Yeah. That's true.

**Chris Gammell:** So then, well, you might have to move your, move your USB in, right. Or something.

**FPGAs:** I would have to have a different USB connector, I think.

**Chris Gammell:** And then the other. But you're thinking about doing that anyways. So, you know.

**FPGAs:** Yeah. And then the other reason why I haven't done it when I started out is because I felt that the normal use case will be people wanting to solder pins on or wires. Uh-huh. And, um, I thought that if it's a castellated edge, um, it would be harder for more people to be able to solder the pins on.

**Chris Gammell:** Yeah. Right. I think, I think this is, so, I mean, I guess that kind of does point back to the thing we talked about at the beginning was this is meant as a beginner platform trying to get people, more people into FPJs as well.

**FPGAs:** Yeah. Okay.

**Speaker ?:** Okay.

**Chris Gammell:** Um, okay. So, someone listening right now says, I'm going to go buy a BX board. What, they get it in the mail. They're like, this thing's beautiful. I really enjoy it. What is the next step?

**FPGAs:** So, on my webpage, I have a B-series guide, which is kind of like a getting started guide. So, this is what you can do to get your development environment up and running and it leads you through a simple example to get the LED blinking. And then beyond that, there are some resources for learning more Verilog and doing other projects.

**Chris Gammell:** Okay. I need to rewrite that page. And we should, yeah, I was going to say, we should clarify the B2 board is the BX board, right?

**FPGAs:** So, the, yeah, the BX is the next gen of the B2 board. Yeah. They're functioning equivalent though or no? They are not, they use almost all the same components.

**Chris Gammell:** I guess, I guess maybe the, the edge connector pins are the, are all the same?

**FPGAs:** The footprint, the footprint is different. You'd want to use a different pin constraint file. Okay. Okay. Yeah. But I, I, I take care of that for you basically. So, there's, there's templates that you can use, um, that kind of abstracts that away. Cool.

**Chris Gammell:** Uh, and then, so people using this, they would be doing this from the command line using the Ice Storm project. Is that right?

**FPGAs:** You could do that. I, unless you're already really comfortable using Ice Storm. I don't recommend that. I recommend instead using either API.com. on the command line. Which allows you to do things like API.com. Um, and it, which will initialize a project and then API.com build and then API.com upload. And that's it. It'll automatically know how to build the whole project, um, based on the top file. And then it knows how to, how to upload it to your FPGA board. Um, so if you want to use the command line, that's what I would recommend. Okay. But if you want to IDE, I recommend using Adam with the API.com, um, IDE plugin.

**Chris Gammell:** Okay.

**FPGAs:** And, um, I'm actually going to be rewriting my B-series guide to use that instead because that's all open source and, um, it's super easy to install and use.

**Chris Gammell:** So you're, yeah, I was going to say, I'm looking at this right now. It's using the actual Lattice tool chain in your existing B2 guide, right?

**FPGAs:** Yeah. Yeah. And Ice Cube 2 is, is like what Lattice had out for the Ice 40 FPG. It's not really that great to develop in.

**Chris Gammell:** Um, it looks like, I mean, to me, it looks like traditional. Yeah. It looks like traditional FPGA tool chains type stuff. It's a little bit simpler, but, um, yeah.

**FPGAs:** It's, it's way simpler. It's, it's, it's uncomfortable to use. Um, Adam IDE is, is way better. And with the, with the plugin, it's much simpler.

**Chris Gammell:** So, I mean, okay. So I'm looking at the Ice Cube UI here too. And it does talk about place and route and all that stuff. Uh, synthesis, place and route, uh, actual programming. How much is visible? If people are using an APIO thing, how much is visible to the user then? Like how much do they need to know about timing constraints and pin files and all that other stuff?

**FPGAs:** Um, if you're using APIO, you still need the pin constraint file. Sure.

**Chris Gammell:** Um, I meant more like the knowledge of it though. Right.

**FPGAs:** So like the knowledge, uh, you don't really, you wouldn't really need it unless you're really trying to push the, the design into, you know, high performance.

**Chris Gammell:** No, no. Um, I'm, I'm really talking about the blinky side of things, right? Cause like, honestly, that's the hardest thing is that I think you, so if you go download, uh, what is, I don't remember what Altera calls it anymore, but the Altera tools or the FP or the Xynex tools, they're like, this is, this is your control panel for doing everything. You can tweak every knob, you can make it completely custom. It's like, that's great for a 20 year FPGA designer. For a beginner, it's like, it's like your jaw drops and your stomach drops. And then, and then your motivation drops most importantly, it's like, yeah, uh, it's,

**FPGAs:** that's really tough. Yeah. It's super intimidating and it puts a lot of people off when I was talking to people at Maker Faire. That was the number one thing that people had worked in FPGAs before. Yep. It was several years ago and they were totally put off by the tools.

**Chris Gammell:** Yep.

**FPGAs:** So there's a lot of, there's a lot of work. It really matters.

**Chris Gammell:** I mean, and, and as a call back to the Arduino folks, like, I mean like the, you know, whatever people think about the hardware, I think the, the, it is the program, it's the simplicity of the programming interface that really matters. And that's also what I like about the new micro slash circuit Python stuff too. Right. I mean, it's just, it really matters to get people into it and having tools that are enabling that's really important. So if you think if API O is that, I think that's, that's a great, that's, you know, that's almost like, you know, I, in the past I have pushed back and been like, oh, that's, that's, that's kid stuff. Right. But I have revised that stance many times over because I've run into, you know, every time there's a new platform, you got to learn the new thing. So. Yeah. And that's better to have something simple. Yeah, exactly. And it's better to learn something simple and get some of that dopamine, that sweet, sweet dopamine and, uh, and then move on from there. Oh yeah. I agree. What is, so how, how far can people go with an API O I mean, type of situation?

**FPGAs:** So with API O you can, if you want, you can add constraints, but I'm not sure right now the ice storm tools don't support most constraints. I think they only support pin constraints. I'm sure somebody will yell at me later and say, I'm forgetting about something. Um, but there's not a lot of like stuff that you'll be able to do there, but you can do, I mean, API, API O itself, isn't going to be restricting you from doing much of anything. Um, well, I guess it's more about how much visibility it has to like, yeah. Right. And, and on ice studio, there's not a whole lot of, I'm sorry, an ice storm. There's not a whole lot of knobs to tune at this point, but going forward, that could be

**Chris Gammell:** a blessing too. Right. I mean like that's nice for, for new users.

**FPGAs:** It's fantastic.

**Chris Gammell:** And so when they, when they move forward, then they'd have to move into using like an ice cube or the more traditional tool chain type stuff.

**FPGAs:** So the SimbiFlow guys are making a lot of progress. And so SimbiFlow is like the next generation of the, the open source FPGA tools. And, um, Tim is very close to having a bit stream and maybe he might've done this already, but he is very close to having a bit stream being output from SimbiFlow for ice 40.

**Chris Gammell:** Nice.

**FPGAs:** And so SimbiFlow has a much better, um, place on route backend, which is like one of the really complicated parts of, of doing the bit stream generation. And that supports.

**Chris Gammell:** I actually did not even know that, uh, SimbiFlow is one of Tim's many, many projects as he talks about. He, yeah, he does a lot. He does a lot. He does a lot. Yes. Anyway, sorry. So it's, it's on the, it's on the cusp though, you're saying.

**FPGAs:** Yeah, it's on the cusp. And SimbiFlow will support, uh, the seven series FPGAs from Xilinx. There's, there's work being done on that. Um, Dave Shaw is, uh, is FPGA Dave on Twitter. I'm getting, you know, tweets and, and commit messages, you know, all hours of the day, um, you know, with his progress of documenting the ECP5 FPGA. Um, ECP5 is a larger FPGA from Lattice. Um, that I'm using in my next tiny FPGA board, the EX.

**Chris Gammell:** Cool.

**FPGAs:** So that's really exciting.

**Chris Gammell:** When's that coming out?

**FPGAs:** So I had some prototypes built of the EX a while back and it took a really long time to get them because the, the ECP5 package, the specific package I'm using is kind of hard to get. Um, but I want to redesign it because I actually want to use the high speed certes on the ECP5. Oh, okay. And I want to route them over to a USB-C connector.

**Chris Gammell:** I was going to say, what, what are those and why should people care about them?

**FPGAs:** So if you use the high speed certes, then you can connect your FPGA board to hopefully USB-3, um, and, or PCI express. And so if you want to get data in and out of your design very fast, um, that's the way to do it. And that can connect you up to standard, you know, interfaces on computers or embedded, um, SOCs, you know, project boards, computer boards.

**Chris Gammell:** So you're saying doing that instead of having a chip that does USB to serial, like a, like a, um.

**FPGAs:** So the, the benefit of, of that is these, these external USB chips are very expensive. And one that can do USB-3 is, is at least $10. Wow. And it has a very specific interface. So there's an open source USB-3 device that I'm, um, working on porting over to ECP-5. And then I want to port the PHY layer to work on the transceivers that are in the ECP-5 itself.

**Chris Gammell:** Nice.

**FPGAs:** Yeah. That'd be great, yeah. I'm super excited. I'm looking at a 3D model of the redesign right now. Um, and I have a USB-C connector and you'll be happy because it has, uh, holes in it for the, tabs. Yeah. For the shield to be soldered in. It's very solid and it's, it's going to be an awesome design. It's, it's going to be the smallest. It's about, it's smaller than a stick of gum and it will have USB-3 on it and PCI Express, SD card, DDR, spy flash, and the FPGA on it. If I do the power delivery network well enough, you could get some, you could get the 85,000 LUT4 part on it. Um, ECP-5 is a relatively low power part for the size.

**Chris Gammell:** And that would be a 10X, 12X improvement, right? On your current size.

**FPGAs:** Yeah. It, that would be huge. So I'm not, I'm not a hundred percent convinced I'll be able to support that full size, um, with like a full power hungry design. Um, but I am pretty convinced that 25K and 45K should be, should be very happy on that board.

**Chris Gammell:** And what are you targeting that time timeframe for?

**FPGAs:** I would like to have a crowdfunding campaign for it in the fall.

**Chris Gammell:** Okay.

**FPGAs:** So early fall, late summer. Um, and then I want to, I want to put that on crowd supply as well.

**Chris Gammell:** Yeah. Oh yeah. We should talk about that. So you had, you had the BX on crowd supply in the first place. So how did that all go?

**FPGAs:** Uh, it actually was awesome.

**Chris Gammell:** Um, I learned, uh, 200, 2 million, 332,300% funded.

**FPGAs:** Yeah. Yeah.

**Chris Gammell:** So because you cheated. Yeah.

**FPGAs:** I, I did, I was trying to figure out what's my minimum funding. And then I thought, you know, I didn't have any crowdfunding for the B2 boards and I made them and I sold them. So I, I'm going to end up making these boards. I decided regardless. Yeah. And, um, so I put my minimum funding as $1 and the crowdfunding went much better than I expected. And I think most of that is due to, um, actual marketing.

**Chris Gammell:** No, don't say it.

**FPGAs:** Yeah. So I've, I've learned a lot about engineering and PCB development and FPGAs and Verilog and even USB digital design throughout this whole project. But I think I've learned even more about, you know, doing shipping and fulfillment and the business side of things and strategy and marketing and, you know, networking with people. I've learned so much more of these, you know, soft skills and business skills that, um, I had always kind of discounted before. And now I really understand their value so much more than I did before.

**Chris Gammell:** And it's, it's actually a great perspective. Evolution for a engineer, huh? Yeah. Yeah. Kind of that. People don't have to have it, but I think the idea is like, if you're kind of doing a side project or out on your own, yeah, that, that is kind of the currency that other, other people work in. Yeah.

**FPGAs:** And I was scared of doing a crowdfunding campaign starting out because I knew I had no experience in doing this. And so I was afraid that, you know, I would get this project funded and then I would ship a thousand boards out and then I would get a thousand complaints coming back, you know, for different things not working. Right. The, the, the B series boards, I implemented a USB device in the FPGA fabric. That's how you program it.

**Chris Gammell:** Oh, really? I didn't know that. Okay.

**FPGAs:** Yeah. And so the, the ice 40 FPGA has this really nice multi-boot feature and it's really easy to use in your spy flash. You can have multiple configuration images. And then there's this multi-boot primitive that you can instantiate in your design and you can tell it, you know, which one you want to boot into next. And so once you tell it to boot into that next design, it'll go ahead and do that. Because the FPGA has that capability, I was able to forego having an external USB chip. So when you plug in the, the B2 or the BX board, that USB connection, that USB device is implemented on the FPGA fabric itself. So that's the default boot. So it boots up, implements the USB device, gets enumerated as a serial port on the computer, just a standard serial port. Sure.

**Chris Gammell:** Yep. Yep.

**FPGAs:** And then you can use the, the programmer tool to, to download the bit stream. After the bit stream is downloaded, the, the USB device internally tells the FPGA to, to reboot. And so it completely wipes out the current design, the boot loader, and it loads in the user design. And so this was for like zero cost. I could implement a USB interface. And this means that the boards are probably $20 cheaper for the user to buy than they would have been otherwise.

**Chris Gammell:** The, the boot loader still stored in the spy flash though, right? So if you needed to do a hard reset, you could still bring it up.

**FPGAs:** Yeah. So every time you, if you boot up and you're plugged into a computer, into a USB host, it'll load the boot loader and it'll stay in the boot loader. So it's ready for you to either tell it to boot to the user config or to download a new configuration. If you plug in the board into a dumb power supply, it will, the boot loader will detect that it's not connected to a computer and it'll automatically reboot into the, the previously loaded user configuration.

**Chris Gammell:** Oh, nice. Okay. And then, and then it's just doing what it, what it would normally do.

**FPGAs:** Yeah, exactly. That's great.

**Chris Gammell:** So that kind of shows the power of having that flexible fabric in the first place. Does, is it possible to pull that F or that USB, that USB integration into future designs as well? Like can, can people have a USB interface to a computer for their designs?

**FPGAs:** Yeah. So it's all open source. They can reuse it and distribute it. I think it's under GPL three right now.

**Chris Gammell:** Okay.

**FPGAs:** Um, and, uh, I'm using it, I've, I've ported it over to a Xilinx board and then I'm also using it on my, my EX boards. So the EX prototypes that I have back have the, the boot loader running and something cool that I was able to do. So I had going to the BX, I also rewrote, um, a lot of the boot loader and I fixed a bunch of bugs and I cleaned up the programmer and I added a new capability. So every FPGA board that uses this boot loader can store information about the board, um, in the spy flash. And it's called metadata. So that the programmer application knows where the boot loader goes. If you're updating the boot loader, it knows where the user configuration goes and it knows exactly what data and what addresses in spy flash are usable for the user for their own data. Like, um, storing, you know, instructions for their CPU to execute.

**Chris Gammell:** So it's kind of like a map file, but for the spy flash, it's like, yeah, it's like a map

**FPGAs:** file as well as identifying information about what the board is, as well as a unique ID. So if you have multiple of these boards plugged in, you can see all the boards that are plugged in and you can see their IDs. So, which is kind of important if you're doing a different projects because you don't want to accidentally, accidentally flash one board with the wrong bit stream. So you can specifically say flash this board with this ID.

**Chris Gammell:** Hmm.

**FPGAs:** Interesting. Um, and then the, the next step forward that I want to do for that is add either the data within the spy flash itself or a link to a webpage so that tools like ice studio can automatically pull in the configuration for your board and use that in ice studio, even if ice studio itself doesn't know about your board, but because your board provides that data built in ice studio can use that and, um, you can start running with it immediately. And that wouldn't work just for ice studio. I also want to enable that for, you know, APIO and any other tool to be able to just plug in the FPGA board and get all the information that that tool needs to work with that board.

**Chris Gammell:** Man, there's a lot to learn here, huh? Are there other resources that, um, like, how did you get into all this stuff? Uh, boy. I guess you had some background in it, huh? We didn't really talk about that either, but.

**FPGAs:** Like, for FPGAs in general?

**Chris Gammell:** Yeah.

**FPGAs:** Yeah. I never, I never used them professionally. Um. Okay. In college, I had bought a board from Zess, X-E-S-S.

**Chris Gammell:** Dave Vandenbout, who's been on the show before.

**FPGAs:** Yes. And that was my first FPGA board. And it was like, it looks like a gigantic version of my boards today because on, it was dual inline PCB. On one end, it had a parallel port and it was barely wide enough to fit the parallel port.

**Chris Gammell:** Oh, this is an early one. I was going to say, because the ones with the Spartan 6 are not that big. Okay, so you're saying like Dave's early boards.

**FPGAs:** Yeah, this was a Spartan 3. Got it. One thousand something or the other. And on the other end, it had a VGA connector and a PS2, um, port. That was, that was my first board and that was awesome. And I had just played around with that. And then when I got into, um, I did a logic class in college. I, I did more with one of the digital imports. And then I just have been collecting FPGA boards and now developing my own FPGA boards.

**Chris Gammell:** Hmm. Next thing you know, man, you start making your own FPGA chips and then it's all over. Then you'll start, then you'll just start, then we'll just see you on a, on a beach somewhere scooping sand into a bucket. We'll be like, look, what are you doing? Like, oh, I'm going to start a chip fab. Yeah. I'm a, I'm a full, I'm a full stack. It's the last thing to do. I'm a full stack. I'm going to hang out. Yeah. Full stack developer. Yes, that's right. You ain't full stack until you, you're making your own chips. Yeah. Oh boy. Uh, okay. So, but for, you're saying that, uh, learning wise, it was mostly just tutorials and understanding tool chains and stuff over time.

**FPGAs:** Yeah. So I, I had found out about Ice Storm. I actually, after I designed the B B2 board and I had even been selling them, I had kind of heard about it before, but I didn't pay much attention. So then I had took a, another look at it and I just kind of fell in love with it because it, um, the, the, the possibilities that it provides of having the open source tool chain and allowing people to remix and redistribute is, is very powerful. Um, there is a professor in a university in Egypt that is working on a online IDE for working with PGAs. Yeah.

**Chris Gammell:** Okay.

**FPGAs:** And so.

**Chris Gammell:** What's his name or her name?

**FPGAs:** Uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, I would have to go back and look. Um, but with the Ice Storm tools, you could host that on your cloud servers or you could even conceivably, you know, put that and run it within the web browser itself. Um, and, um, you know, get from, you know, plugging in the board to blinking in a matter of minutes and make it very, very easy, um, for people to, to get started and to, to use FPGAs.

**Chris Gammell:** Yeah. It's interesting with all the, uh, man, that would be trippy, huh? I mean, I know that there's like web USB is like how, um, that's how Chrome, like Chromebooks talk to USB and it's all JavaScript based. And I think that's right. But thinking about like that, then programming an FPGA, like going from like cloud level tools down to an FPGA was, is pretty trippy. Uh, yeah.

**FPGAs:** Or even having this, another board design that I want to do at some point is a wifi enabled board.

**Chris Gammell:** Oh, cool.

**FPGAs:** And so you could program the FPGA over wifi.

**Chris Gammell:** You could just, uh, you know, just drive a, a, an antenna directly with an FPGA, a high speed FPGA pin and see what happens, you know?

**FPGAs:** Yeah. So the, the software defined radio guys, I'm kidding.

**Chris Gammell:** I'm kidding.

**FPGAs:** Yeah. This, the software defined radio stuff that is amazing and it's magic to me. Um, and the boards that have come out like Lime SDR and others are just beyond my abilities. I don't think I could, I don't, I don't think I could make a worthy SDR.

**Chris Gammell:** I think that stuff paired together is kind of interesting though, because like, so, so obviously Mike Osman has been on this show a lot and, uh, like HackRF and a lot of the Great Scott, uh, gadgets tools, they are peripherals, right? So thinking about, they are USB peripherals where they're pushing data from a software chain down to the USB and they're streaming data back and forth. So in theory, I mean, if you hook those things together, it could be interesting, but maybe I'll make some intros after the show.

**FPGAs:** Yeah, there are, I mean, there are FPGA boards, um, for software defined radio. So you can do a lot of that processing in the FPGA. I don't, I'm not familiar with it myself, but, um, I've looked at them and they're, they're gorgeous.

**Chris Gammell:** Yeah. Well, I mean, I, and I think that's really where, you know, at the beginning of the show we were talking about like, like, well, I, we always think about it as streaming, right? So streaming data back, uh, you know, high speed data through a thing and then doing some processing on it in line, you called it something else. What did you call it? Uh, like a pipeline, right? Pipeline. Yeah. So it's like you said pipeline versus logic or versus control. So like pipeline data like that, like that is where FPGAs are just killer. Like Derek, uh, Cozell has been on the show too. Right. And you know, he talks about that stuff too. Um, and being able to, Matt Eddis is another one who's been on the show. Uh, you know, it's like all these people that they're, they're often working with FPGAs. I think that, uh, the SDR folks like, like, uh, like Osman, you know, like they got a lower cost by not doing FPGA stuff. But I think that the accessibility and the dropping costs make some very interesting future options. Yeah. Cool. Uh, well, so, uh, Luke, where, where can people find you now that maker fair is over? Are you going to any other conferences?

**FPGAs:** So I would like to do the Hackaday super conference that I think is in November. That's right.

**Chris Gammell:** Yep. I've heard rumor. It'll be the first weekend of November.

**FPGAs:** Okay. So, so I want to do that and I've been toying with the idea of doing a workshop.

**Chris Gammell:** Okay.

**FPGAs:** Um, yeah, which would be pretty cool. Um, we'll see though.

**Chris Gammell:** Okay. Yeah, that'd be great. That'd be really great. Um, uh, where can people find you? And more importantly, where can people buy a, uh, BX board or any other boards really?

**FPGAs:** So if you go, there's, there's two places. Um, I started on Tindy and so Tindy was an awesome way to start selling things with a community of people that are, you know, really enthusiastic about, about hardware. Um, so you can go to Tindy, uh, you could just search tiny FPGA Tindy and you'll find my Tindy store. Um, you, and you can get the A series boards there and the programmer there. Um, once the BX crowdfunding campaign is over, then you can order the BX from Tindy or my own web store. But today, if you want to pre-order the BX, you can go to, uh, crowd supply.com forward slash tiny FPGA. And then you should see the project there.

**Chris Gammell:** Wait, is this not out yet? The BX? Oh yeah. I thought, I'm sorry. I thought it was out already. I'm an idiot. It's, it's almost out. Um, it's almost out. Right, right, right. Yeah. But I didn't even look at the date. So it was funded on April 19th. So it's like in the throes of shipping and programming right now, huh? So right now. She's July 16th. The list says, I don't know what's coming up. Yeah.

**FPGAs:** And that's going to get pushed out a week. I think, um, FPGAs were supposed to be shipped last week, um, to the manufacturer. And the last I heard it's delayed until tomorrow. And so tomorrow I'm going to find out if they're actually getting shipped or if they'll get delayed again. Got it. Okay.

**Chris Gammell:** So the B2 exists and is out in the world, but you're saying that that was a limited run. That's why you can't buy those right now. So the idea is that people could go and buy a BX and have one on the way. Yeah. Okay. Cool. Yeah. Free shipping. $38 for your own BX, huh?

**FPGAs:** Yeah. Yeah. And, and I've offered package on the cross supply. You can get pretty nice discount depending on how many you get. And I put in one for 25 boards and I didn't expect anybody to buy it, but I think I've had two or three.

**Chris Gammell:** The classroom bundle? Yeah.

**FPGAs:** Yeah. I've had two or three people buy that, which, which was pretty cool.

**Chris Gammell:** Well, this is very exciting. I'm excited. I'm going to probably buy one right now. So, uh, so people can, uh, go and buy more. Uh, do you have enough? How, I mean, are you going to build enough that if, there will, there will be stock past the crowdfunding campaign?

**FPGAs:** I don't want to run out of stock again. So I ordered 1250 boards.

**Chris Gammell:** Oh, okay.

**FPGAs:** And, um, I've sold almost half of them now. Whoa.

**Chris Gammell:** Nice.

**FPGAs:** So with the lead times of components and manufacturing, I need to put in another order really soon. Yep. Wow. That's crazy.

**Chris Gammell:** Okay. Where can people find you on GitHub, Twitter, everywhere else?

**FPGAs:** So if you just search for tiny FPGA with no spaces, um, I'm there on Twitter as tiny FPGA. I am at GitHub as tiny FPGA. I'm on Hackaday as Luke Valenti. Um, you know, you can go to tiny FPGA.com and catch me at the forums.

**Chris Gammell:** Okay. That's great. Yeah. Cool. Well, Luke, thank you for being on and telling us about this stuff. I'm excited to try this out. Um, I think that, I think that your enthusiasm around this project is very well founded. And, uh, I think that the FPGA future is, is, is racing towards us. So we'll see.

**FPGAs:** Yeah. Yeah. Well, thank you very much for inviting me. This was a lot of fun.

**Chris Gammell:** Okay. We'll talk to you soon.

**FPGAs:** Great. Thank you. Bye.

**Speaker ?:** Outro Music
