---
episode: 444
title: An Interview with Ben Eater
url: https://theamphour.com/444-an-interview-with-ben-eater/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release May 27, 2019. Episode 444. An interview with Ben Eder. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Ben Eater:** And I'm Ben Eder. Hey, Ben. How are you doing? Good. How are you?

**Chris Gammell:** I'm good. I'm good. People probably know you from your videos about 8-bit computing and breadboard computers and all that other stuff, right?

**Ben Eater:** Yeah. That's a thing that I'm known for.

**Chris Gammell:** That is a cool thing. And we're definitely going to be talking about that here. What else generally do you do? I mean, I see your software and hardware, mostly software. What are you doing these days?

**Ben Eater:** Yeah, probably mostly software is certainly my background. And actually networking as well. So I spent maybe 15 years in the networking industry. But lately, yeah, it's mostly been software. And then this 8-bit computer YouTube thing has been more of a side project.

**Chris Gammell:** Yeah, I'm sure. I'm sure people... So first off, if people haven't seen it, it's Eder.net is your site. And then tutorials are all YouTube-based. So maybe we start with that. First off, how did you start getting into this? Because it seems like it kind of builds on itself. But how did you start doing it? And what was the basis for starting to do the computing stuff there?

**Ben Eater:** Yeah. So I guess, I mean, as a kid, I was always kind of into electronics. So it had always been a hobby for me. I think like many people, I went to Radio Shack as a little kid and drooled over all the little components. And, you know, got as much as I could, brought it home and tinkered. And then, you know, my career path didn't end up going down the hardware route so much. But it had always been kind of a hobby. And even, you know, in high school, I guess, I started doing more kind of computer systems-y things in terms of building hardware that I could plug into my computer. You know, whether that was parallel port stuff to turn on lights and do different things. Or, you know, even building like an ISA card interfacing with the, you know, the old 8-bit bus in the old, you know, PC architecture. Sure. And so from that, I had kind of this sense of how a computer worked and how the computer architecture worked. And so it had always been this kind of idea in the back of my mind that like, I bet I could build a computer from scratch, you know, where scratch is like logic gates.

**Chris Gammell:** Right, right.

**Ben Eater:** And it's always something that I kind of imagined doing someday. And then, you know, fast forward 30 years or whatever it is. And I had some time and kind of had an idea and decided to try to do it.

**Chris Gammell:** That's great. And so, okay, let's kind of walk our way back through. I mean, so you go over some of the, you know, gate stuff. And obviously, you have a lot of educational content. We'll talk about education a little bit later. But, I mean, where does one start when starting to build an 8-bit computer from scratch?

**Ben Eater:** Yeah, so I guess where I started is I had come across this book a while ago called Digital Computer Electronics. I think it's out of print, but the author is Albert Paul Malvino. And it's an amazing book that describes CPU architecture, you know, from logic gates, essentially, and goes through a lot of the same things that my videos go through. And so that kind of gave me this idea of like, okay, here is a tangible thing I can kind of get my arms around. And in that book, he describes this architecture he calls the SAP one, which is simple as possible, which is what it sounds like.

**Chris Gammell:** I don't know that one. But yeah, okay.

**Ben Eater:** Yeah, it's as simple as possible as you can make a computer architecture, which is roughly what I ended up doing in the videos. You know, it's tweaked a little bit and so forth. Okay. But that's roughly the architecture that I used. And so, yeah, I built something roughly along that architecture in – it was actually for a hackathon. So it was a really long, like I think four-day weekend-ish, but like 12-hour days for four days straight. Oh, boy. Hardcore.

**Chris Gammell:** Red Bull, Red Bull, Red Bull.

**Ben Eater:** Red Bull, lots of Red Bull, lots of caffeine for sure.

**Chris Gammell:** Yeah.

**Ben Eater:** And by the end of it, I, you know, surprised myself. I had something that was kind of working as a computer. And my goal was that at some point this could be a series of videos, or I guess at the time I thought a video describing how it worked.

**Chris Gammell:** Oh, so young. So you're explaining it all in a single video.

**Ben Eater:** Yeah, you know, 15 minutes should do it. Yeah.

**Chris Gammell:** Jeez, yeah. Those professors, what are they even doing out there with all those hours and hours, right?

**Ben Eater:** I mean, it's simple. Simple as possible. How hard could it be, right?

**Chris Gammell:** How long is this book that you used? It's like 300-page books. A couple hundred pages, yeah. Yeah, yeah.

**Ben Eater:** But – yeah, but – and so actually when I was building it during the hackathon, I had a camera pointed at me recording it because I figured I'd get all this – footage and I'd just edit it together and throw together a little narrative and, you know, it would be one nice video. Describe how a computer works. Everyone will love it.

**Chris Gammell:** Awesome.

**Ben Eater:** And that totally – that wasn't going to work at all. So after I built it, I started making some other videos about, you know, how a 4-bit adder works and building that from logic gates and, you know, it's kind of some smaller components. Mm-hmm. And I guess at some point came to the conclusion that maybe that was the way to go is just to talk component by component and almost show building each one. Yeah. And so what I did is said, I'm going to start over. I'm going to build a second one from scratch and make videos showing that process from start to finish. And that's ultimately what I ended up doing. And it took, I don't know, three or four years. Mm-hmm. Yeah. Well, because you're filming.

**Chris Gammell:** Right. Exactly. Yeah. You got all that other stuff, all the overhead there too.

**Ben Eater:** Yeah.

**Chris Gammell:** It's tough too because, I mean, like, what do you – oh, yeah. Well, yeah. Money, blah, blah, blah. Yeah. Yeah.

**Ben Eater:** Details.

**Chris Gammell:** You know, like, when you think about – and I'm sure you got a lot of feedback from people too, but, like, where do you usually start? Like, when you think about starting with a computer like this, you know, do you think about people coming at it from the software world or the hardware world or the, you know, transistors, bottom-up type of thing or software top-down? Where do you think about it personally? And then what do you think is the best method for approaching education like this?

**Ben Eater:** Yeah. I mean, I think personally I just thought about it from, you know, 14-year-old me.

**Chris Gammell:** Okay.

**Ben Eater:** And I just kind of imagined, you know, what would I have wanted to see when I was 14, given what I, you know, remember I thought I knew when I was that age. Right. And that's kind of how I approached it. And so, you know, I made some assumptions. I don't really explain how binary works at any point in the video series. Right. So, I sort of know that. I don't really explain a lot about – I mean, I don't talk about Ohm's Law, for example. I don't really go into any of that sort of more basic stuff. And, you know, arguably you don't even need to understand Ohm's Law to understand how a computer works, which is kind of funny.

**Chris Gammell:** Yeah, that's kind of crazy, huh?

**Ben Eater:** But I – yeah. But I – I guess I just kind of had this mental model in my head of who I thought was watching it. And that was roughly modeled after me when I was like 14. And that's kind of who I felt I was speaking to. And it happens to have resonated with a lot of people.

**Chris Gammell:** That's great. That's great. And so, I mean, and you mentioned kind of breaking it down into the component parts. What were some of the things that you felt like you had to kind of go over as like an understanding kind of thing? Because I – so like I should say 14-year-old me had no concept of computing at all. I didn't do anything like that. I didn't actually get into it until college. And then it was, you know, actual instruction from a professor. And at that point it was very like let's do Carnot maps and let's do transform and DeMorgan's theorem. And it's like – but at a certain point – Right. Like what you're talking about, you're talking about building a real thing. And I'd really like that hands-on – obviously I like that hands-on practical approach. That's what, you know, I always talk about. But, you know, what made you decide then to like, oh, this one actually deserves some more like diving into it? And like what were some of those topics?

**Ben Eater:** Yeah, I guess, again, I thought about it from the standpoint of I want to get to a point where at the end of it I feel like I understand how it all works. But I didn't feel bad about cutting any part out that I didn't think was strictly necessary. And I think a lot of it is a judgment call. You know, Carnot maps, for example, don't talk about that at all. There is one video where I go from a fairly complex combinatorial logic thing and then talk about how you can recreate that in an EEPROM as a lookup table. And there's a perfect place to slide in Carnot maps, however you say that. But I was just like, you know what? It doesn't matter. Like you don't need to know that. Right. And if you then go on and take a class where you get into that stuff, you're going to have a lot of context for why that might be useful or how to use that or what have you. But it's not essential. Right.

**Chris Gammell:** It'll give you the motivation to actually keep learning and digging in instead of being like, oh, this is just a math thing I have to do or a logic thing I have to do.

**Ben Eater:** Yeah, exactly. So I think I just I wanted to cover what I felt you would need to cover so that for any, I guess, any potential sort of why question you might ask as you go along. So you're like, why does that work? Or why did you do that? Or I try to sort of anticipate any of those sorts of questions that you might come up with and try to answer those, but maybe not stray too far beyond that.

**Chris Gammell:** Yeah. Yeah.

**Ben Eater:** Again, kind of thinking about that model, you know, 14 year old me, the person I'm sort of thinking of in my head as the audience of like, what would that person be interested in?

**Chris Gammell:** Sure. Yeah. I mean, and like you go over semiconductors and transistors and all that stuff too.

**Ben Eater:** Um, uh, and I think that starts from that. Why, you know, because yeah, I feel like if you start from a logic gate, you're like, well, why does that work? How does that work? It's like, well, it's made a transistor. Like, well, why what's transistor?

**Chris Gammell:** What is that? Why? Yeah. Right. Right.

**Ben Eater:** Yeah. And then, you know, then I get down to chemistry and it's like, okay, that's someone else's problem. Right.

**Chris Gammell:** Right.

**Ben Eater:** But I mean, it's just sort of like working backwards. Mm hmm.

**Chris Gammell:** Yeah. So from that perspective, it is kind of like a top down ish because you're saying like, this is a computer. People can kind of grok what a computer is, but now we're digging into each individual component and you need to understand why there is, you know, like you're, you're just like even saying memory units and, and individual like storage elements of a single bit of memory and stuff like that. That's like a flip flop. Right. And, and so I could see that's why you're kind of talking about, you know, different flip flop types and, and, and low level things like that.

**Ben Eater:** Yeah. I mean, I guess I think about it top down in sort of planning how I go through it, but the video series ended up being bottom up.

**Speaker ?:** Sure.

**Chris Gammell:** Oh yeah. No, I think, I think on a broad scale, it's definitely bottom up because it's like, well, this is like the basis of, you know, hell the servers that we're talking about, we're talking through right now. Right. There's at the, at the bottom most level in very, very tiny transistors, there's similar things happening, you know, all around us every day, phones, whatever. So it is bottom up from that perspective, but there's always a, a lower level you can get to, right. You could go and talk about the, like you said, the semiconductor physics and the, you know, even the electrochemistry and all the things that down, down, down, down the rabbit hole. Right. Yeah.

**Ben Eater:** You could keep going down, but.

**Chris Gammell:** Right.

**Ben Eater:** But, but I, but I think, I mean, generally the way that I structured it, I start, I mean, I do start at the, the semiconductor level. Um, but then I work up, you know, okay, how do you, how do you build transistors from a semiconductor? How do you build logic gates from transistors? How do you build a latch from logic gates? And then how do you build a register from latches and just kind of keep going up? And then, and then once you have like, okay, here's a register and here's a counter and, um, here's these different, you know, memory module and all these things. Then it's like, how do these things fit together at a system level to form a CPU?

**Chris Gammell:** Yep. Yeah. Yeah. Yeah. That's good too. I mean, so do you, do you think broadly that this has impact for people these days? I mean, like a software programmer, should they, they know this kind of stuff?

**Ben Eater:** That's a good question. Cause I mean, a lot of software programmers don't know this stuff and seem to be doing.

**Chris Gammell:** I mean, if someone writing JavaScript or Python or whatever, like how often are you really thinking about the hardware that's on the bottom, bottom, bottom level with like all those layers of abstraction there, but. Pretty rarely. Maybe it's useful.

**Ben Eater:** If ever.

**Chris Gammell:** Yeah. Yeah.

**Ben Eater:** Um, but I, I mean, I find that it's interesting cause I, you know, I see comments obviously from, from viewers and a lot of them are software engineers who are in that position of, I've never understood this. And this is fascinating because I work on computers all day. And so they have, they have some notion that, yeah, there's this high level language they're using and yeah, that compiles or it's interpreted by something that's then compiled into this assembly language or machine code. But then that's sort of where it runs out for them. And to see from the hardware up, you know, cause that's kind of where my video stopped is. Okay. Now you've got machine code.

**Chris Gammell:** Um, it's interesting too. Um, there, there was that, um, do you remember that mega computer that was, it was like a British person was doing that a while, while back. And I remember saying like, ah, I don't really think this is useful. You know, like what is the real point of this? And then it was like a couple of weeks or months after that, I was doing some C stuff and I was just, you know, pushing stuff around registers and doing pointers and whatever. And, you know, as you get closer to the hardware though, you know, really having a, uh, if not a direct grasp of the exact architecture you're working on, at least a general one of like, oh, well, how is this data chunking through the system? It, it can definitely have some impact, you know, especially you get closer to the hardware. I don't know if you've seen the same thing.

**Ben Eater:** Oh yeah, for sure. I mean, definitely if you're doing C programming, you are thinking, um, or at least occasionally about registers and register transfers and kind of what's happening at that level. And yeah, to understand what's going on in the hardware and what that actually means, you know, obviously, especially if you're, you know, thinking about any kind of assembly language, understanding, you know, what it means for an instruction to take a certain number of clock cycles.

**Chris Gammell:** Right.

**Ben Eater:** You know, if you've gone through my videos, that's pretty obvious what that means.

**Chris Gammell:** Yep. Yeah. And it's, I think it's, um, you know, it's, it all comes down to like the choice of the user. I think at the end of the day, like how much, how deep do you want to go? How far down the rabbit hole do you want to go? Like if I think about even just playing around with an op amp, you know, like, which is something I've done a lot in my life. Yeah. I don't really think about the internal structures in there. I don't think about the protection diodes until, until they jump up and bite me in the ass because of some, you know, corner case that I'm dealing with or something like that. But I guess having like at least a cursory overview of it does help in, in certain ways, in certain like scenarios. Maybe, again, maybe not for the Python programmers of the world, but, but maybe as they dig down into it, you know?

**Ben Eater:** Yeah, maybe, I mean, that's the thing is like, we, we depend so much on abstractions so that you can be a Python programmer and not have to think about any of this stuff. But, you know, every abstraction, no matter how, how hard we try is leaky in some way. Um, you know, we, we obviously try for that not to be the case, but, you know, even if it just, you know, in terms of performance, you're always going to have some kind of leaky abstractions. And so the better you understand what's on the other side of that abstraction, um, the more intelligent decisions you can make with what you're doing. Yeah. Um, yeah, it's kind of hard to make the case for understanding computer hardware and for a Python programmer, but, uh, cause there's a few levels of abstraction between there, but.

**Chris Gammell:** Right, right, right. When I think about like, I've been doing server stuff lately too, and like virtual virtualization and stuff like that. And now it's like, even at the computing level, I mean, you do a lot of networking. I'm sure you do a ton of that stuff, right? It's like now there's just like layers and layers and layers, even on top of the software. And it's kind of, kind of crazy, but it's also from a, the perspective of getting stuff done. And, and, and having a lot of resources at your disposal, that stuff is kind of necessary to, to move forward, move, move quickly and efficiently.

**Ben Eater:** Yeah, sure. And I mean, I think, yeah, the more, you know, it's just, it's just more data points that you can kind of synthesize as you're solving problems. It doesn't hurt. Yeah. Especially if you find it interesting.

**Chris Gammell:** Yeah, definitely. Um, well, I'm wondering if you want, now this one is obviously people should watch the videos, but, um, I was wondering if you wanted to do a little word picture with me here and, and walk through the data path of a, of a computer real quick. And, uh, I don't know if that would work at all here actually, but, um, maybe if you would walk people through like, okay, so you push data into a computer like this and it chunks through and you're trying to light up LEDs at the end, you know, where does the data go? And if you're trying to, you know, add stuff together, maybe.

**Ben Eater:** Yeah. I don't know how to do this without a visual.

**Chris Gammell:** A word picture. I know exactly. Well, you know, like, and yeah, and this is maybe, maybe it, maybe it's not a good move. I mean, I think broadly, I think about like, I think about like Ram and ALU is like these high level things and you break them down as more as well, like how they actually work. Um, but, but like kind of like putting things into operating memory and then pulling it back out in order to add them together, stuff like that. Um, did you, did you operate from, uh, do you, when you were thinking about writing all these things and doing all these tutorials, were you doing it from like an assembly language perspective almost? Or was it more just single, single operation and single, uh, single instruction type stuff happening?

**Ben Eater:** Yeah, I guess building, building the computer, I'm thinking about it from the micro instruction level. And so a micro instruction is, well, I don't know, maybe, maybe it would help to step back and try to try to do what you were suggesting with this, this word picture of how data flows.

**Chris Gammell:** If it doesn't work, I mean, obviously people have the backup of just sitting there. Okay, go watch the video. Like people should be watching the videos anyways, but it's, it's kind of fun to do this sometimes. Yeah.

**Ben Eater:** Yeah. But I mean, I guess if I were to sit down, let's, let's say we build, we build this computer that I've built in these videos. When I sit down and program it to do something, um, it's pretty basic. It has 16 bytes of memory. It's not, not the most advanced computer in the world, but with those 16 bytes of memory, you can use those each memory location either for, uh, an instruction or for data. And it's entirely up to you. There's no, um, segmentation or anything. Um, but you program it with dip switches. So you'd, you'd set the memory address dip switches to zeros, you know, zero, zero, zero, zero. And then you can set the data dip switches to whatever, uh, bit combination for whatever instruction you want it to execute. And then you hit a button and then that'll manually program that into that memory location. And then you do that for each memory location for your program. And there's different, uh, machine language instructions, which are encoded as different binary values. And those are the things that you're programming in that memory. And then when you, uh, actually switch the computer into run mode, so it's going to run through that program. Uh, it's each instruction essentially has kind of two stages. There's a fetch stage where it's fetching the data from memory, uh, and decoding it. And then there's the actual stage where it does whatever that instruction says to do. Yeah. Um, I don't know if you're following along so far.

**Chris Gammell:** I am. Yeah. Yeah. That's great. This is really great. Yeah. And I think like even, even just from the start, right. Where you're like, there's a, uh, you know, there's an instruction and there's data and like that alone is like, oh, right. Of course there's like, you have to have the thing that you're operating on and then the operating that you want to do to it. Like those are the, but like, those are kind of base level things where if you just assumed you knew all that stuff, maybe, or you assume that people knew that they might not, you know what I mean? Like, like there are these different things and then one interacts with the other.

**Ben Eater:** Yeah. And, and, and in this computer, for example, there's 16 bytes of memory. So there's, there's only 16 eight bit things you can put in memory. And each of those eight bit things could be an instruction or it could be data. It depends. Um, typically the thing in address zero is going to be instruction because when you reset the computer, that's what it starts executing. Um, but it might, you know, execute something in address zero, then it'll move on to address one, address two, address three, maybe it'll loop back to address zero. And so then address four or five, six, and so on, those could be data or they could be unused or, you know, who knows? So what, what a particular memory location is used for is, you know, not necessarily known. Now, some computers have, um, segments that are for executing code versus data. And that's maybe a good security thing to do, um, so that you don't accidentally execute user, uh, data.

**Chris Gammell:** Right. Right. Injecting, injecting bad stuff in there or something.

**Ben Eater:** Yeah. Yeah. Yeah. But, uh, that's not, not a thing that I'm doing on a breadboard. Right.

**Chris Gammell:** Right. So we're gonna do a security audit now.

**Ben Eater:** Yeah. Yeah. Yeah. Well, there's no speculative execution attacks. Newn from those.

**Chris Gammell:** Yeah.

**Ben Eater:** No, no specter bug.

**Chris Gammell:** Right.

**Ben Eater:** But, um, but yeah, so, so, I mean, the, the computer itself, I mean, most of what's going on is you're just sort of moving data from one register to another. That's really a lot of what it is. Right. And so you have, you have some number of registers in this computer. There's, that depends how you count two or three or four, but the registers are hooked into a bus and then at any point in time, a register can either be spitting its content onto the bus or it could take whatever's on the bus and read it into that register. And those are just control signals. So each register has a read and a write control signal. It's either high or low. And so if it's, if the, if the right, uh, control signal is high, then whatever's in that register gets put on the bus and then everything else that's connected to the bus can see that value. And obviously you want to make sure there's only one thing at a time doing that because you don't want multiple things writing to the bus at the same time.

**Chris Gammell:** Yeah.

**Ben Eater:** Um, and then any, and then you have the, the read, which says, you know, if, if that read signal is high, then that particular register will just take whatever's on the bus and read it into that register on the next clock pulse. Yep.

**Chris Gammell:** Yeah. And so then using the, the registers actually, you know, that's like the kind of like the working, the working memory area effectively. Right. I mean, that's like the, how you interact between different, uh, pieces of data that you're pushing around.

**Ben Eater:** Yeah. So if you want to add two numbers, you'd load one of the numbers into one register and you load the other number into another register. And then, uh, depending on how the computer is set up, you probably have those two registers connected via hardware into some arithmetic logic unit that can do the addition. And then you can tell the ALU like do addition and put the contents on the bus. That's how you get the result out of that. And then you can take that result and read it into another register.

**Chris Gammell:** Yeah. What is the, um, I, and I think we should, you know, that I, is that the, the end of the, the process you think, or, I mean, I guess you're, you're adding, subtracting, kind of manipulating data and moving it around. Is there, are there final outputs to that kind of thing or what?

**Ben Eater:** Yeah. So, uh, in, in my computer, there's an output, uh, register, which is a little bit different than a, you know, a real computer, I guess. Uh, but there's, there's a register that if you put a, if you put any data into that register, it'll show up on a little, uh, LED display, a little seven segment display. Mm-hmm. Um, in a, in a, you know, sort of quote unquote real computer, you might have, um, you know, a video card. And so in that case, you know, I guess a simple example might be the video card might be memory mapped. So what you do is you'd write data to particular memory addresses, and then the video card is kind of reading that same memory. And whatever contents is in that memory is what it's painting on the screen. Um, but again, it's still just kind of register transfers.

**Chris Gammell:** Right. Yeah. When you really break it down like that, it's kind of crazy. You know, you think about how, all that stuff shifts together and that's what makes video games and that's what makes, you know, audio transfer over networks and, you know, like all the things that does. Yeah, exactly. Yeah. So that kind of brought me to, um, how, how fast are we talking about here? Like, what is the speed of, of this thing?

**Ben Eater:** Well, I mean, I, you can go a couple hundred, uh, Hertz, which is, you know, not, not too impressive in, in reality though, just because you want to be able to see what the output's doing. Like you probably only run it at a couple Hertz because it's, it's an educational thing, but it's, it's also on a bunch of single step as well. Yeah. You can single step. Yeah. You definitely often want to do that. Yeah. Um, you know, to, to sort of trace through what a program's doing. Um, and so I, you know, I have a video where I do that. I, I stepped through a program.

**Chris Gammell:** That's great. Yeah. Yeah. I mean that, and that kind of stuff too, it's like, um, I think that this is a really good way to think of, you know, like as people are thinking, kind of moving up that stack of, of hardware up to machine code, like you're talking about, these are effectively machine codes, you know, with the different instructions and things like that. Then there's assembler that would kind of put those together. And then, you know, maybe you have C on top of that. That's actually, you know, writing the assembly and stuff like that. Um, that sounds right. Right. And then, you know, maybe C can also be Python up above that or whatever.

**Ben Eater:** Um, yeah, pretty much. And then, yeah, you know, the C compiles to assembly or, well, yeah, or machine code. I guess you can write assembly and assemble that into machine code or the C compiler will compile to machine code. And then the machine code instructions are, are made up of micro instructions. And that's, that's actually kind of the hardware that you're, you're doing is, um, each, each instruction has some number of micro instructions that make it up. So for example, if you wanted to, uh, add a number, the first micro instruction might say, uh, uh, turn on the, the output from memory. And, and turn on the input from the A register. And so what that'll do is move data from memory to the A register. And then the next micro instruction might say, you know, turn on output from somewhere else and turn on input to the B register. And that'll move data from somewhere else into the B register. So now you've got the two operands in the A and B register. And then the third micro instruction might say, take the output of the ALU, which is now your sum and, and, and, uh, turn on the output of the ALU, turn on the input of the A register. So that'll move that sum back into the A register. And so those are the micro instructions that make up an add instruction. And so the machine code would just be one instruction says add. And then that machine code is defined to, you know, take data from these different places and add them and put the result in some other place.

**Chris Gammell:** Right. Yeah. And I think that's the other thing I remember, like one of my first classes and like in writing, you know, the thing was writing C plus plus two and, you know, decently high level language, I suppose, but it was just like, I had no concept of what was going all the way down to the bottom. Right. And I don't think it was even, I think it was running on like an, you know, 486 processor or something like that anyways, probably an Intel something. And so like, there was no concept of what was actually happening. And it was just so far away from what you're talking about. But I like, I like that, you know, like what you're talking about there is you're talking about actually, you know, writing one plus one equals result, you know, and then it actually is implementing each of these different instructions and micro instructions and stuff like that. Yep. What does it look like when instruction actually hits the computer, right? Is it just like a pathway that is pre-programmed based on logic? So like if the instructions zero one, then there's a, like a effective logic pathway that kind of is activated by that zero one. What is, what is the actual implementation of an instruction or micro instruction that then makes it do the thing?

**Ben Eater:** Yeah. So you have essentially kind of a couple, you can think of it as like a combinational logic circuit that has some inputs and some outputs. And the outputs are the control or what's called the control word. And the control word is really just a whole bunch of control bits that are things like, you know, put the contents of the A register on the bus or read what's on the bus and put it into the B register. Each of those would be a bit. So a register would have two control bits, one that says read, one that says write to or from the bus. And so you have a whole bunch of control bits, you know, in my computer, it's, what is it? 16 control bits in other computers, it might be a hundred or more, uh, just controlling all of these different things. And so at each point in time, that set of control bits tells all of the different parts of the computer, what they're doing. So that's the output of the decode logic. The input of the decode logic is the instruction that you're executing, which you fetched from memory, um, and the, the step that you're on. So there's essentially a little counter that goes through, you know, zero, one, two, three, four, and so forth. And so for each instruction, you could be on step zero. You can be on step one. You can be on step two, and you get a different control word for each step. And those are the micro instructions. So the decoding is really just combinatorial logic where your, or combinational logic, whatever the right term is, where you, where you have the instruction and the step coming in on one side, and you have this whole control word going on on the other side that's controlling everything.

**Chris Gammell:** Right. And I think about like, like the control word, you think about it, like, and you look at these things and it might be like zero X B E or something like that, you know, usually reading in hex or whatever. Yeah. But like you're saying, yeah, you break it down into binary and then you're like, oh yeah, bit four controls that thing. And then it's flipping on or off and it's doing that thing or opening that pathway or whatever it is, putting stuff under the bus, like you're talking about. And, and that is ultimately the, um, the, the output of this, of this thing. I like that. I like that a lot. Um, and, and when I think about like writing, writing drivers for like NC for like a, you know, a spy chip that you might be working with, oftentimes it's that same thing. You know, you're, you're going through, you're reading the data sheet. You're like, oh, pin six does, you know, does enable heater or enable, you know, the X, the time 16 gain or whatever it might be. And you have to know that that's going to be part of your entire thing. You shift it in there and you, you work with it. So it's good to, it's good to have that as a, as a visibility for, for people that are kind of far away from it. It's not a magic word. It's just a, it's just a number that controls a bit.

**Ben Eater:** Yeah. It looks like this number, but it's, you know, it's just a bunch of little bits and each bit does a different thing. And so each combination of those bits moves data from one place to another.

**Chris Gammell:** Yeah. Yeah. I mean, so maybe give a view of fuel here as well. Like, um, how protected is this stuff in a modern processor? Like, like would people ever see any of this stuff? Like how much, how much of this would you predict that, that people listening would actually interact with if they're maybe just even using an 8051 processor? Obviously it's an old processor, but.

**Ben Eater:** If you're doing assembly programming, then you are very much thinking about all of this. Maybe not the, maybe not the individual micro instructions, but you're certainly thinking about the register model. And so oftentimes if you're doing assembly programming, you'll, you know, that you'll look at the data sheet or whatever you're looking at documentation. And there'll be like, here's the register model of this thing. And it says, these are the registers. These are what they're used for. These are the instructions. Each instruction will act on certain registers. And so you'll very much be thinking of, of that. You might not think the next level down in terms of, okay, what are the actual micro instructions to move something from one register to another? But you will see in the data sheet, it'll say, oh, this takes X number of clock, or clock cycles. And so that kind of tells you how many micro instructions or, you know, it might be some optimization, some pipelining or something going on, but, but you're, you're certainly thinking of something very close to this. So if you don't, if you don't understand some of the details, you know, you might be able to get by because you understand the mental model of, of, you know, what it is you're programming. But I think it would probably help you to understand physically what's happening as well.

**Chris Gammell:** So the optimizations and the pipeline you're talking about, like, again, how, how much do you, do people see that when they're writing code as well? Like, so that's something that, that people might think about or people might hear about, but they might not be thinking about as they're writing C code and stuff like that. How do you, how do you see that happening?

**Ben Eater:** Yeah, probably not. It's probably not something you're thinking too much about when you're writing code. You know, it, even if you, even if you're writing assembly code, excuse me, even if you're writing assembly code, you know, you, you might just see the result of that as being, oh, this, this instruction takes fewer clock cycles than it might, if you didn't have some optimization in there. I don't know. Yeah. I don't know as a programmer that you'd really bump into that too much, but maybe there's something I'm missing. I don't know.

**Chris Gammell:** Okay. Well then how, how did you, um, I guess the other thing about optimization I was thinking about, like, how did you determine, you know, you know, that there's a discrete number of clock cycles that an operation takes. Did you, did you go back and then optimize any of your own processes in terms of like, um, doing that pipelining and doing that in the hardware then?

**Ben Eater:** No, not at all. Um, actually. So every instruction takes six clock cycles on my computer, whether it needs it or not, which means that there are a number of instructions where the last few clock cycles are no ops. And, uh, the, the cool thing though, is a lot of people have, have realized this and there's all sorts of comments in, in, you know, the relevant videos where people are saying like, Hey, you could add an optimization where if you get to the end of the instruction, you could have a control word signal that resets the, the counter for the instruction cycle. And they're absolutely right. You can do that. And, and people have done that. And it's, it's kind of cool to see people who, uh, you know, take this project, build it themselves and then do optimizations like that.

**Chris Gammell:** Yeah. So what does the community look like? I mean, like it, it sounds like there's community built up around this. What, you know, are people, so people are building their own, are they sharing them as well? Is there anywhere like centrally that people are discussing all this stuff?

**Ben Eater:** Yeah, it's, um, well, to, to take a step back, I'm kind of shocked. Um, I guess that there is a community around this. Um, it wasn't, this is cool. Yeah, I know in hindsight, it's like, well, obviously, I mean, I find it interesting, so why not? But I don't know. I feel like I'm kind of weird, but, uh, no, I, I guess when I, when I started this, I didn't really have in my mind that there was going to be a community of people who were going to be building this. Um, which in hindsight, I would have done some things differently, frankly. Um, but yeah, a lot of people have, have seen these videos and said, I want to do that. And they've gone out and they've built their own and done different optimizations.

**Chris Gammell:** What would you have done different, um, based on knowing, knowing that the community was bigger or going to be interested in this kind of thing?

**Ben Eater:** Yeah. Well, one, one thing for sure. Well, actually, I guess that one question is it's kind of weird that it's on a bunch of breadboards. You know, you probably haven't seen anything else that's, you know, takes up 14 breadboards. That is, that is true.

**Chris Gammell:** Yes. Yeah. I haven't, I was, I have not seen that.

**Ben Eater:** Full disclosure. That's a little weird. Um, and, and honestly, the reason was I, I just thought that it was easier to sort of see what's going on. Um, right. With it laid out like that versus, I don't know, it felt a little bit to me anyway, kind of sort of removed. If you, you know, draw a schematic in a CAD package and then you spit out a PCB and you send it off and it gets manufactured and you just solder it up and it works. Right. To me, that, that felt like it's a little bit harder to kind of really viscerally see what it's doing and explain what it's doing versus being able to like that. Yeah.

**Chris Gammell:** There's an accessibility standpoint, I think as well, right? Someone sees a breadboard and they say, oh, I know what a breadboard is.

**Ben Eater:** I could, I know what a wire is.

**Chris Gammell:** I could, I could put that together. Yeah.

**Ben Eater:** Exactly. Exactly. Yeah. Yeah. Um, but that does present some challenges because the reliability is not quite what you get with a PCB. Yeah. Okay. Yeah. So, so that's, that's number one. Number two, uh, there, there's some other shortcuts that I took, um, just in the interest of, you know, I'm interested in computer architecture and just demonstrating, uh, how a computer works and, you know, how, how all this stuff works. Um, one thing that I did like that was really kind of evil is I'm using TTL logic chips. That was partly because I just had, you know, a box of TTL LS, you know, old, old school logic chips. And it turns out that the outputs of those, um, have a, you know, there's like a pull up, pull down resistor kind of thing on the output. So you can't pull too much current out of the outputs. Mm-hmm. And it also happens that the, uh, what is it? The high level for TTL LS is I think two volts is the threshold. Mm-hmm. So it turns out you can stick an LED directly on the output of an LS chip with no current limiting resistor. Uh-huh. And the LS output stage will limit the current well enough. And the voltage drop of an LED is like 2.2 volts. So that's still above that two volt high. Uh-huh. And it, it kind of works. Um, and so that's, that's what I did. And I just, I don't, I just, you know, I've got, I don't know, 50 LEDs or something on this thing. And I just skipped the current limiting resistors because it works.

**Chris Gammell:** And then some of your, your viewers did not, I'm guessing, huh?

**Ben Eater:** Or they, you know, they used, uh, uh, CMOS chips or something that don't have that current limiting or, you know, or, or, I mean, you know, the 2.2 volts versus two, I mean, you're so close on the tolerances there or your power supply isn't quite five volt. I mean, it's, you're just so close to the thresholds there. It's, uh, no, no guarantees. And so, yeah, it's, I think it's led to some frustration from, from people trying to get this to work. So that's definitely something I would have done differently.

**Chris Gammell:** You're, you're, um, you're helping replicate the early, the days of computer clubs and how people had to struggle, struggle their way through.

**Ben Eater:** Yeah, that's it. It's a little built-in challenge.

**Chris Gammell:** Exactly. It's like that Easter egg that they didn't know about and you didn't know about either. Right, right.

**Ben Eater:** Well, I knew I was doing it, but I figured, well, no one else is going to try to do this. Yeah, yeah. No, it was just, I was just my short-sightedness. I figured, well, who's going to want to do all this? And you can just watch the video, but it's obviously the, the opposite. People watch the video and they're inspired to want to do it. So that's great. Here we are. People are muddling through, I guess. Um, but yeah, there, there is a pretty good community on, on Reddit slash R slash Ben Eater. You know, a lot of people building it there and talking about it. Um, and, uh, because of the, the interest, I started selling kits. So you can actually buy all the components.

**Chris Gammell:** Tell us though, do you, do you sell the LS chips or which kind of chips do you sell now?

**Ben Eater:** Oh yeah, it comes with the LS chips. Okay. It comes with a very high quality breadboards. So I try to include everything that optimize your, your likelihood for success. It also comes with enough current limiting resistors that you can put resistors on all the LEDs. That's good.

**Speaker ?:** Yeah.

**Ben Eater:** I would recommend.

**Chris Gammell:** Yeah. And that's, you know, that's an interesting point too, because people that are getting into this, I'm sure are people that are returning to hardware in general. Like that's a big thing. And then, you know, you or I think about like, oh, well, yeah, you go to your drawer, you grab a resistor and then they're like, wait, what's a resistor? And then I don't have a drawer with anything in it or, and then where do I buy it even? Like, where do I even start? And holy crap, I'm looking at DigiQ and Mauser and Aero and like all these sites that are just like, like overloads. Yeah. Where do I start? Yeah. Right. So that's, I think from that perspective, it's really good that there's a kit. Um, of course, from your perspective, you know, if you, if you short a resistor or two, you get a call at, you know, 2am your time or whatever it is and the usual kit business problems, but yeah. Yeah. Not insurmountable.

**Ben Eater:** Yeah. So far it's been, it's been pretty good. Yeah. And because I, I put together, uh, I mean, there were a lot of people wondering like, what, what are all the parts? And I had some parts list and descriptions of some of the videos. At some point I put them all on my website, um, just a whole parts list. And I, um, I added like Amazon affiliate links cause I figured why not? Or like other affiliate links. And, and yeah, I just started noticing like a lot of people are clicking on these things. Maybe I should try a kit. That's great. Yeah. The kits have been surprisingly popular. And, you know, I send out surveys like two months after each kit ships and, uh, you know, ask a few questions and things. And, um, you know, also ask people how far they got in. And it's a surprising number of people who have built the whole computer and it works.

**Chris Gammell:** That's great. Which is, and do you have an idea of like, you said like a lot of software people, but are like these students, young people, old people, like what are, what are your demographics?

**Ben Eater:** Like, yeah, I mean, it's hard, it's hard to know. I guess maybe I should ask some demographic questions, but, uh, the just anecdotally it's been a lot of, you know, sort of career software people who just are interested in a side project and interested in learning more about the thing that they work with all day. Um, and then there's also a big contingent of sort of high school, uh, even college students, um, you know, doing it for school projects and, or, or just doing it at, you know, cause they're interested. Um, and I've even, uh, talked with some teachers who are doing it in classrooms.

**Chris Gammell:** Oh, that is great. Yeah, that's really great. I was thinking about it. Like, you know, I think about the kind of courses that I took in college, like I said, I didn't really get started till college. And, um, you know, at that point they're, they're trying to cover things that are relevant to industry. And like, you know, so we're doing things that were, and things that are like accessible and then clean to grade as well. And like, there's so many things that this kind of kit probably wouldn't fit into, but from a practical perspective of like learning, actually learning, you know, not, not what schools are in the business of always actual learning, uh, you know, and you know, they do their thing too. It's fine. Um, uh, this is like a really, a really hands-on practical approachable result, I think. And, uh, from that perspective, it seems like a really, really good thing.

**Ben Eater:** Yeah, for sure. And I mean, in hindsight, it, I mean, it would be nice to say that I planned all of this ahead of time, but, but, but in hindsight, it, you know, it turns out to be this pretty powerful project in terms of if you actually get the thing built, I, as far as I can tell, it's impossible to do it without understanding something about computer architecture by the time you're done.

**Chris Gammell:** Yeah. Yeah. Right. Right. Or at least being interested at the end of it too, right? You're like, Oh, von Neumann. Okay. Now what, what is, what is this like stuff instead of like, uh, you know, like me, I'm like, who are these old people? You know, this is just another math problem.

**Ben Eater:** But, but, but even just to get through it, I mean, it's, um, because it's all on breadboards and, you know, you've got to like cut and strip and bend all these wires and it's a lot of wires. It's a lot of cutting and stripping and bending. Yeah. Um, it's, you know, it's, it turns into a labor of love and, uh, it requires a fair amount of persistence to get through. And it's complex enough that you're basically guaranteed to make a mistake somewhere along the way, which means that you're guaranteed to have to do some amount of troubleshooting, which again, requires a great skill to learn.

**Chris Gammell:** Oh my God.

**Ben Eater:** And try to understand what is this thing actually?

**Chris Gammell:** Yeah.

**Ben Eater:** Um, yeah, that's actually one of the things kind of interesting seeing, um, like I mentioned, there's some classrooms that have been trying this and there's a, um, a high school near, near where I am that that's doing it with some kids. And it's interesting to see, cause some of the kids are, you know, literally they'll pause the video where there's like a clear screenshot and they'll just literally copy what's on the screen on their breadboard. How interesting. You ask them questions and like, you know, there's not a lot of understanding there.

**Chris Gammell:** Um, but then, you know, wait, wait, wait, are they getting graded?

**Ben Eater:** Yeah. Yeah. Yeah.

**Chris Gammell:** Aha. Yeah. Okay. Sorry. Keep going.

**Ben Eater:** So anyway, no, no, no judgment, but, um, no, I'm not judging.

**Chris Gammell:** I'm just saying that like, that's, but that's like the, uh, the motivational side of things, right? I mean, this is like, this is like a microcosm of, of education and learning and, you know, the school systems in general, I think, you know, like when you, when you just have a output, you know, output driven thing, like, like what I hear you saying is it's, it's almost impossible to just get the, the answer, right? This is an ultimate show your work. And also, by the way, your work is made up of hundreds of wires and probably a couple are going to come undone and you're gonna have to figure out what the hell came undone. That's right. That's right. Yeah. Yeah. And, uh, yeah, there's, there's almost no shortcut from it. So like what, what ends up happening when those, those kids are just copying the output, what what happens to them?

**Ben Eater:** Yeah. So, I mean, it, it works for a little while, right? I mean, you can, you can pause the video, you can look at what's on the screen. You can say, okay, I count how many holes over and okay. The wire goes from this hole to count how many holes it goes to that hole. You put that in, you can do that to a point, but yeah, ultimately, I mean, eventually the thing gets complex enough that it's going to fail in some way. And then you're, you're stuck. You, you have to, you have to behind really. And you, and you get behind and all the rest, but, but yeah, you have to step back and figure out, okay, what is this thing actually doing? And, you know, even if you get your friend to help or you get some help from the teacher or whatever it is, um, it seems like you're, you're going to come away with some understanding at least of, you know, what a register is or what a register transfer is, or, you know, some, some of these basic concepts, especially when you get to the scale of the whole, the whole computer.

**Chris Gammell:** Yeah. That's great. I mean, like, so I should, I should, you know, full disclosure, I was the kid copying off the screen at one point, you know, I was thinking like, like, that's how I started out, you know? And then like, but it's, I think, uh, I think some of it is driven from like, oh, well, I got to get this thing done. It's like a thing I have to do. But like, you know, I think ultimately the, like I said, it is like a microcosm of all education is like, how do you get people to be interested, interested enough at the beginning? Right. That's like the, and I think the building from the bottom kind of helps a lot, but, um, I don't know if you have ideas on how to, how to get people interested at the very beginning, to, to build each element up.

**Ben Eater:** Yeah. I mean, to the extent that I've seen challenges, I mean, in the classroom, it's, it's different. I mean, most people who I interact with who buy the kid, I mean, they're, they're, they're coming in motivated. They want to, you know, they're not, they're not buying a computer and build your own computer on breadboards kid on the internet. They're not interested in it.

**Chris Gammell:** They're not, they're not using it to do their taxes or board processing. You're saying? Exactly.

**Ben Eater:** Yeah. Um, so, but, but yeah, in, in, in a classroom environment where there's, you know, the, the, um, the motivation is a little bit more extrinsic in terms of a grade. Um, one of the challenges certainly is that motivation and that's a, that's a tough nut to crack. I mean, that's what, that's what the job of teachers is to help motivate. And, um, and yeah, I guess my, my hope is that, um, you know, I guess seeing that bottom up, seeing how each thing builds on the next. And, you know, if, if you understand the one thing, you can see how the next thing builds on that. You see how the next thing builds on that. And I guess my hope is that after you've kind of seen that happen a few times where you can start with something simple that you understand and build step at a time into something more complex, you know, you sort of build that confidence that, uh, okay. Yeah. You know, even this complex thing is understandable if I go a step at a time. Yeah.

**Chris Gammell:** The dopamine loop, you know, like dopamine. Yeah.

**Ben Eater:** Yeah. Hmm.

**Chris Gammell:** Uh, well, this kind of leads into the education stuff in general. I want to ask you about, I mean, so you, you worked. You worked at a Khan Academy, which is obviously very well known for doing educational stuff. Um, um, what, what did, what did you do there? Was it mostly the networking stuff you're talking about?

**Ben Eater:** No, not at all. So it's sort of an interesting story how I wound up there. I was in, like I said, I was doing networking, you know, sort of systems engineering level stuff. And then I, um, had started my own company for a while where I was building, um, I guess, I don't know. I say networking hardware, but it was really just a, um, a server running some custom software doing, doing some fancy stuff. But, uh, but you sell it as a hardware thing. And anyway, um, uh, so, but anyways, this network measurement stuff that I was selling. And, uh, when I was doing that, I stumbled on Khan Academy. I thought, man, this is really great. And I'm someone who I was never a good student. Uh, and.

**Chris Gammell:** Same. Yeah.

**Ben Eater:** Didn't do well in, in high school. Um, got into college, didn't do well there, failed out of college a couple of times, never finished college. So, uh, yeah, education was, was not something where I, I felt like I succeeded. And so I guess I've always kind of had this thought that like, yeah, man, the education system really, really failed me. Let me down. Um, seems like we could do better. Never really had a sense of how to do that. I mean, I. You know, got lucky. I, this was all kind of at the peak of the.com boom. So I was able to easily get a job in, in the tech industry and, you know, had kind of an established network and stuff and, you know, had, had no problems myself. Um, and so, you know, I've, I've been fine, but that it always bothered me that the education system just sort of didn't, didn't work for me. And so when I stumbled on Khan Academy, I was just like, man, this is exactly what I would have needed. Like if I had this when I was in high school, I would have been like amazing at math. Cause I enjoy math. I just didn't. There were just, you know, these gaps in my knowledge that, you know, you get one or two gaps in your knowledge and then it just compounds year after year. And by the time you get to calculus, you just sort of fall down. You can't, can't do it. And it's just because you have these gaps in pre-algebra or whatever.

**Chris Gammell:** And then I think that, like you mentioned to the confidence piece too, right? Like there's so much of that where once you're like, oh, this is, it's all me, you know, it's all me. You kind of start kicking yourself. And then the next thing you might've been able to do, but then you, you start from that, that darker place almost. And, uh, that, that, that has a bad feedback loop, you know? Yeah.

**Ben Eater:** Yeah. That's yeah. That's not, yeah. And for me, I just never understood it because I, I guess I was reasonably confident in, in, in my skills in other places. Cause you know, I was tinkering with electronics. I was doing programming. Like I could do things that seemed to me were valuable, but, uh, you know, the academic stuff, it just never, I don't know. I, I guess I, I think I just told myself I wasn't interested in it and like, yeah, I could do it if I wanted to, but you know, I just tell myself like, I don't want to, to make myself feel better.

**Chris Gammell:** Sure. Yeah. Right. Right.

**Ben Eater:** But even, even years later, I was, you know, uh, you know, as you know, well-established career and all the rest, I was like, yeah, and I, I should like go back and like actually see if I know calculus or teach myself calculus. I picked up an old textbook and I just couldn't get anywhere with it. So, you know, it just frustrated me, but then yeah, stumble on Khan Academy. I was like, Oh wow, this is exactly how this should be done. And, uh, this was, you know, early days of Khan Academy and, uh, you know, the website, all the stuff was open source at the time. And I, um, in the process of doing that stumbled on a bug as I was, you know, playing with some of their stuff and filed a bug report and then found out that, Oh, this, this is on GitHub. So I started poking around, fixed the bug, spin it, a pull request.

**Chris Gammell:** Nice.

**Ben Eater:** And, uh, you know, just started contributing that way. Um, and ended up, that's great. Ended up basically volunteering my time for a little bit, doing, doing some of that. And, uh, started by, um, most of my early work at Khan Academy was creating interactive math exercises. So little simulations and interactive exploration things. And then, uh, yeah. And then, and so then, you know, they ended up hiring me and I ended up completely switching my career from this whole networking thing into, um, sort of education and software engineering. And then as Khan Academy grew, I ended up, you know, managing teams of software engineers there.

**Chris Gammell:** And so for about seven years, do you, do you know how many people have used like your individual? Like, I, obviously this is just a little bit of ego thing. I'm like feeling your ego for you, but like, uh, like how, like, what are some of like the numbers we're talking about here in terms of like how many times something like that's been viewed? Like a, like a math concept.

**Ben Eater:** Khan Academy? Yeah. Yeah.

**Chris Gammell:** I just mean like, uh, so you did like, if you did like a math module, like you did a sub module of a math thing and then like Khan Academy has had millions, hundreds of millions, tens of millions. I don't know how many students or people have gone through the modules, but just thinking about like one module you submit and help with being like actually educating that many number of people in the world. Yeah.

**Ben Eater:** Yeah. I mean, the numbers certainly add up. I mean, I think at this point they're over 10 billion problems attempted on Khan Academy.

**Chris Gammell:** Oh my God. Okay.

**Ben Eater:** I mean, I don't know how you reason about that. Yeah. And, you know, obviously, I mean, as, as the company grew, we, you know, we hired a content team and the content quality probably got better than some of the stuff I did. But so I don't, I don't know how much of that is me, but, um, yeah, but yeah, the numbers are staggering and it's, it's hard to kind of wrap your head around stuff. Like that. You just, just, you know, even on YouTube, it's like you put a video out and it gets, you know, a hundred thousand views. And it's like, I don't know, that's just a number.

**Chris Gammell:** Right. It doesn't feel like, it's always the minutes watch that the minutes watch is like, holy crap. That's a lot of people spending, you know, consuming time in lives, you know, always hopefully for a good benefit, you know, you're not like, but it's just, it's, it's so hard to like reason about that. And sure. Sure.

**Ben Eater:** I don't know. Just psychologically. I don't know. There's something like if I'm, if I'm giving a talk in front of a group of 10 people. Like kind of where my head is, is just so different than if I'm putting a video out for, you know, what do I have? 200,000 subscribers. Like, like I I'm, I'm thinking so much more about those 10 people that I'm giving a presentation.

**Chris Gammell:** Right. Exactly. Well, you know, having a face in front of you is a, is a big thing. Yeah. You know, like that's how humans are, humans aren't built to, to interact behind screens or microphones or whatever. So it's hard to, it's hard to visualize, but it's good to do it. So what was it like, uh, where, I mean, so what was the eras of, of Khan Academy? So that you were there like, uh, pretty early on, you said.

**Ben Eater:** Yeah. 20, 2011, I guess. That's when I joined late, late 2011. Mm-hmm.

**Chris Gammell:** I don't remember when it started. Sorry.

**Ben Eater:** I, uh, yeah, that was, that was pretty early. So I think there was, you know, maybe 10 people.

**Chris Gammell:** Okay. Oh, wow. That's yeah. That's pretty early. So, so what else did you, so you ended up doing like, like educational planning and stuff like that? Like, did you get into like the theory of education and stuff or, or what, what was that?

**Ben Eater:** A little bit. I mean, so my, I mean, initially, like I said, I was building these like interactive math modules and, and, and just essentially creating math, uh, content. Um, uh, because at, at that sort of early stage, a lot of that stuff was done in software. So we wouldn't, we didn't have a team of content creators writing math questions. We'd have, we'd have software that would write math questions, right? So you'd have a, you'd have a random number generator that would, you know, if you want to, I don't know, if you want to do a addition problems, you pick, pick a random number, pick another random number. And then, you know, what's this number plus that number.

**Chris Gammell:** Right. The computer does it behind the scene and then the human does it in front of the screen, right? Yeah, exactly.

**Ben Eater:** And compare the two. And if it's right, that's right. Yeah. So I was doing a lot of, you know, building those things, um, from software. And so you build these like modules that would generate, and you can generate an arbitrarily arbitrary number of, of problems. And, you know, it gets a little more complex if you're doing like factoring polynomials, because you have to make sure that the answer works out cleanly and all the rest. But, but yeah, building all that logic. Um, and then as the company grew, um, we hired, you know, former teachers and tutors and professors to write math problems. Um, and they, they were frankly a lot better than I was. And, uh, and then, and then my role kind of shifted more towards building the software that the, uh, content creators would use to, to write the problems.

**Chris Gammell:** Right. And so. Right. So it became like a content management system at that point. Almost. Yeah.

**Ben Eater:** We built, you know, we ended up building a whole content management system that handles all of that. And so, so that was sort of my role shifted more towards like pure software engineering. Um, and then as the company grew, ended up managing, uh, teams that did that.

**Chris Gammell:** That's really cool. I mean, like what, and what, I mean, what was it like working there? Like from a, uh, company culture worth worthwhile. I mean, like, uh, did, did people think about the impact it was having? Was that like a big piece of the, of the, the everyday talk around the office? Yeah.

**Ben Eater:** That is, yeah, that is a hundred percent what everyone was thinking about. Um, and so there were always like really fascinating discussions about education theory and, and all the rest going on. Um, and it's, it's kind of interesting being at a nonprofit tech company. Um, and it, it selects for a certain sort of person, I think.

**Chris Gammell:** What kind of person is that?

**Ben Eater:** Well, it's, I mean, it's a tech company and, and, and, and in a lot of ways it felt just like a tech startup, you know, small group of people building software, putting it out on the internet for millions of users. Um, it's, it's all the things you would do at a sort of typical Silicon Valley startup, but it's a nonprofit. So you don't have this lottery ticket of stock options, um, in the back pocket. Right. And so that filters out a lot of people, right? Cause a lot of people go work for a startup cause they want to make a bunch of money. Um, whereas I think people who want to work at Khan Academy want to work there because they want to have some impact in education and they, and they see the potential to do that. And so when you put a bunch of those people together, it, it's a really, really wonderful culture.

**Chris Gammell:** That's great. That's really great. Does that mean that the fridge is not stocked as well though? Is that, is that one of the ultimate, uh, the ultimate, uh, pretty good job. Okay. Good. At least they could, they cover that. That's good.

**Ben Eater:** Yeah. I mean, they are still hiring from the same pool of people. You know, you have to, have to meet some baseline. Got to hit them. Expectations. Got to hit them snacks. Yeah. Yeah. There's their snacks.

**Chris Gammell:** Yeah. That's great, man. That's, that sounds really, that sounds like a really cool culture. I mean, so, and so how did that impact, how did that roll back into your, um, your educational stuff? I mean, did you, did you find that that impacted how you ended up making videos about, about computing?

**Ben Eater:** Um, it's a good question. I think, um, honestly, probably what impacted more was back when I was in, you know, working in the networking space, I would teach classes there, uh, because I, you know, I think that's a big part of my job was, you know, selling equipment to customers that had to, you know, then helping them integrate it. And so I was often teaching classes about how new networking technology worked and, um, how to, how, you know, how routing protocols work and all that sort of stuff. And so when I was doing that, um, I was thinking a lot about education and I was just sort of interested in education. So I was reading stuff about education. Um, and because also part of my job was, was sales. I was, I was like a sales engineer. Um, uh, a lot of, you know, I guess the, the sort of way that I thought about sales was I thought about it as an education problem, which was, I have this great product. It's going to solve your problem. I just need to teach you why. Right. That's good.

**Chris Gammell:** Yeah. Right. You have to define the problem space and like, like actually set everything up and be like, no, no, no. Here's, here's what the actual reality is. And then, and then, oh, by the way, this thing that I, you know, my company charged lots of money for is also the answer.

**Ben Eater:** It's more like, well, let me, let me, here's this thing that my company charged lots of money for. Let me teach you how it works. And as I teach you how it works, you're going to see why the thing that it does and the way that it does it and all the rest, like why that's going to solve your problem.

**Chris Gammell:** Got it.

**Ben Eater:** That was sort of how I thought about, I thought about it. Um, and so, yeah, when I started reading about educational theory stuff, it all kind of like clicked as like, oh yeah, this, this makes a ton of sense. And so I think, I think that, I think it was more like it came from that to then when I started, uh, you know, volunteering, creating content for Khan Academy. I think a lot of that kind of helped make that content something that caused them to then reach out to me and say like, Hey, do you want a job?

**Chris Gammell:** Yeah. That's right.

**Ben Eater:** And so then I sort of have, I guess, carried that forward.

**Chris Gammell:** What are some of the, do you have any like, uh, references that you can keep going back to on the educational side of things? I mean, this is a personal, I'm personally interested in this stuff. So, um, I don't know if there's any books that you go back to.

**Ben Eater:** There's, yeah, there's a few, I guess.

**Chris Gammell:** Just trying to think of, uh, Ben, Ben is furiously searching his bookshelf.

**Ben Eater:** I am like turning around and looking at my bookshelf.

**Chris Gammell:** Like, yeah, that's fine. Yeah. Yeah. I mean, like, that's great too.

**Ben Eater:** I mean, Mindstorms is, is definitely a, a really good one.

**Chris Gammell:** Uh, like the Lego thing.

**Ben Eater:** So Lego is, uh, Mindstorms is a book written by, uh, uh, Seymour Papert and the Lego thing is named after the book. Oh, okay. That gives you some indication of the, yeah. What, what, that's a, that's a ringing endorsement.

**Chris Gammell:** So, so, and that's just about like what, like the, the thought process behind like how, how like, uh, thinking happens or what is, what does Mindstorms really refer to?

**Ben Eater:** So one of the, one of the things that, uh, Mindstorms introduces is it introduces, um, the logo programming language.

**Chris Gammell:** Okay.

**Ben Eater:** So you've probably come across that little turtle that you programmed.

**Chris Gammell:** I don't think I have actually.

**Ben Eater:** Oh, so logo is this, uh, I guess it was like an old Apple two. I don't know. When I was a kid, it was a, it was a thing, but it's, it's a programming language that you have a little, they called it a turtle and you would tell the turtle what to do. So you could tell the turtle to walk forward. You could tell the turtle to turn left. And then you could tell it to like lift pen or lower pen. And so by telling it to walk forward or turn left, you can draw things. Yeah. And then if you want to turn right, well, that's just turning left three times. So you could write a subroutine called turn right. That is just like turns left three times. And so from that, they build up, they build up this, uh, you know, essentially this whole drawing environment and you can program all sorts of stuff. So that's one of the things that, that was introduced in, in Mindstorms and just kind of talking about, um, you know, using that to learn about geometry and I guess, you know, teaching, teaching children programming.

**Chris Gammell:** That sounds like that's a little more hands-on than I would have guessed actually with the Mindstorms thing. So you were, you were able to basically take that and then kind of back calculate that to how you would use that for teaching methods. Is there like a teaching method kind of written around that as well? Um, yeah, that's what a lot of the work talks about.

**Ben Eater:** So it talks about this language and why this language is, is so powerful.

**Chris Gammell:** Yeah. That kind of like, sounds like you're really building from building blocks up and that, that sounds like a, and each of them is pretty graspable. I like, I like the tangible model of like a turtle as like a visualization as well. It's really good. You could have like a bitey, the eight, the eight bit bite that goes through your, uh, the computer or something. Sure. Now bitey, now bitey, you go into the instruction.

**Ben Eater:** Yeah. I would do graphics display. That's what I'm going to do.

**Chris Gammell:** Yeah. Okay. I, yeah. Or, uh, whenever I think about like, like campy visualization, I always think of like that thing in a drastic park, like Dino DNA. Exactly. Yeah. Any other education books that you, that you liked when you're getting into that kind of thing?

**Ben Eater:** There's some interesting ones that have come out more recently, like, uh, mindset by Carol Dweck. I'm talking about kind of the difference between a growth mindset and a fixed mindset.

**Chris Gammell:** Oh, that's, that is a, can you explain that topic? Cause I think that is like one of the most important things, especially like I read that in the context of teaching adults and, uh, that's, yeah, that's like it's teaching children and teaching adults. I think like those are really important, uh, mindsets.

**Ben Eater:** Yeah. And well, mind storms is, is primarily around teaching children. Um, uh, but, uh, yeah, mindset, this idea of, of a growth mindset versus a fixed mindset. The, the idea there is that a, a fixed mindset is one where you, um, it's, it's kind of about the beliefs that you have. So you might have this belief, for example, that I'm not a math person. I think that's a belief that a lot of people hold, or I, you know, I can't learn math and that's a fixed mindset because it's like, I can't do that. Whereas a growth mindset, you would have this belief that maybe I can't do this math thing now, but I believe that if I, you know, apply myself and, and, you know, focus and, and, and have a plan and kind of work on that plan, I'm going to be able to do that.

**Chris Gammell:** Right.

**Ben Eater:** And the, the difference is that, you know, people, and there's basically the book kind of goes through a lot of research about, um, you know, how people that have that fixed mindset are, you know, don't have as much learning and don't have as many learning gains or don't show as much in terms of learning gain as, uh, as people that kind of have that growth mindset. And then the other interesting conclusion of the book is that a growth mindset is apparently something that can be taught. Yeah. Which is, which is really powerful. Very meta. Yeah.

**Speaker ?:** Yeah.

**Ben Eater:** And so there's this idea that people, even people who have a fixed mindset, if you can teach them about the growth mindset, show them some evidence and, and so forth, you know, that's obviously a really powerful thing. And so there's, there's a lot of work in that. That's actually something that we, um, we're focused a lot on at Khan Academy is ways of integrating kind of meta cognition stuff, sort of teaching about teaching or teaching about learning. Um, for example, teaching about the growth mindset, you know, within the Khan Academy product are the things we can do to, to, uh, to kind of help our, our learners understand that there is this ability, you know, even if you don't think you can do this thing, a shift in mindset can help you kind of get there.

**Chris Gammell:** Yeah. It's, it's almost like a behavioral psychology kind of tied into all of it as well. Like it's, it's interesting. It's an interesting field. Like, um, I think about that when the, like the dopamine squirts, you know, like thinking about that kind of stuff too. It's like, when you think about people and like gamification kind of ties into it's like, as you're building people up, you're building up, not just their, their knowledge, but you're also building up that confidence that they, you know, that they can handle the tougher problem. Um, yeah. And, and kind of keep going forwards. And that kind of ties back into the growth mindset as well. It's like, no, no, I can figure out that I can do this. It's just a matter of time and, and, you know, persistence.

**Ben Eater:** Yeah. I mean, game designers have really figured this out.

**Chris Gammell:** Um, and that's true.

**Ben Eater:** I think that's what we all aspire to do. I mean, you know, I think it's interesting, like, um, you know, one of the classic examples is, uh, is, uh, Mario level one, like the first Mario first level. Um, you know, just the way that's laid out.

**Chris Gammell:** I'm visualizing all of it right now.

**Ben Eater:** Yeah. Just the way that that is laid out is just genius because you start out, there's nothing around you. There's nothing that can hurt you. And you can just walk back and forth and you can just experiment with that. You can play with that and you can walk back and forth and get comfortable with that. But then there's this little thing you have to jump over and then you jump up and, you know, and you can take as much time as you want to, to figure out how to jump because there's nothing that can hurt you. But then when you jump up, you jump over and it's arranged, um, so that as soon as you jump over, you land right on the Goomba. And so you see immediately that, okay, if I jump on top of it, like it almost forces you to jump on top of it.

**Chris Gammell:** Yeah. Right.

**Ben Eater:** And you can see right away that as soon as you jump on top of it, it kills it. And so again, you're safe, but now you've learned that that's how you kill them.

**Chris Gammell:** Right. Right.

**Ben Eater:** And it just, the entire level just unfolds like that. And it's, it's just this amazing thing that you go in, you don't know anything about the game and the game teaches you how to play the game. And that's, I think that's the Holy grail for a lot of education.

**Chris Gammell:** And that's without any like tool tips or like little boxes or like, look over here, you should do this. Right.

**Ben Eater:** If you need a tool tip, you failed.

**Chris Gammell:** Yeah. Right. That's, um, yeah. Obviously things have gotten more complex, but I think in a best case scenario, like you're saying it's, you know, you kind of learn all those things as you're accomplishing tasks and, and moving forward.

**Ben Eater:** Yeah. I think that's the Holy grail is if you can, if you can, if you could do that for algebra, that would be amazing.

**Chris Gammell:** Yeah. I think about some of the problems that, uh, I encountered in like electrical engineering education and that I wish I would have had any kind of reference point for it. Like the story I always talk about is like having a spectrum analyzer in front of me when I was learning four year transforms or, you know, under, you know, having done a kit like yours before I start doing resistors and op amps and, and gates and stuff like, you know, like, you know, building full things before you have to go back and learn the theory, you know, having that push pull of like hands-on theory, hands-on theory, like it's, it's tough to do, but like ultimately that is, I think the most powerful thing because when you get to the theory and you run into that roadblock and you have that mindset, like you're saying the growth versus the fixed mindset, it's not, yeah, I'm not, I'm not bad at math. It's I, I can figure this out because I have to figure this out because I want to make my frigging computer work, you know?

**Ben Eater:** Yeah. That motivation is, is so important.

**Chris Gammell:** Yeah. And, and so often I think the motivation is just, it's so decoupled from what, you know, it's, we have to get through this curriculum. We have to get through this thing. You know, we have to take this test. We have to, you know, get this thing out there and if there's no context behind it, then it's really a tough sell, you know, for people that are already pretty exhausted from all the other classes they have doing these things or whatever.

**Ben Eater:** Yeah. It's interesting. One of the, one classroom that's, um, they just started doing some parts of the, of this eight bit computer project. Um, and you know, we're right at the end of the school year, so they didn't have time to do the whole thing. But, um, one of the incentives that the teacher said was if you build, um, a working ALU, so you've got two registers that you can load and you can add and subtract, um, and you have a clock that can sort of run it. If you get to that point, you'll get a letter grade bump for the course.

**Chris Gammell:** Oh, nice.

**Ben Eater:** It's pretty big motivation, right?

**Chris Gammell:** Sure. Sure.

**Ben Eater:** But it's, it's interesting to see, I mean, there's some kids who are already really, really into the project and cause they're just into it. And for them, it's like, great free letter grade. I was going to want to do this anyway.

**Chris Gammell:** Right, right, right, right.

**Ben Eater:** And then you've got the kids who are motivated by the letter grade and they're just like dragging themselves.

**Chris Gammell:** Yeah. Right, right, right.

**Ben Eater:** You know, they're not really into it. They're just trying to get over the line. They're the ones sort of copying what's on the screen and, you know, just kind of trying to brute force the thing to the point where it works. And it's, I don't know, it's kind of sad.

**Chris Gammell:** You know, it's almost like a, like the, the Dan Pink book I usually refer to on this show that about drive and based on other people's research as well. Yeah. Yeah. Yeah. And, and, and there's that RSA anime talk I'll, I'll put in here because I always refer people back to it, but it's, you know, one of the speeches he gave and he talks about drive and stuff like that, but he talks about like money as a motivator. And I think in a school context, like grades are kind of a motivator as well. Like, you know, it, it's obviously there's not a one-to-one comparison there, but it's like past a certain point, you know, it changes how you operate in your motivations. You know, it doesn't, it, it's not the, it's not the true drive there, right? It's not the curiosity. It's not the wanting to learn. It's just the natural output of like having to get this thing in order to progress to the next level or, you know, to make your parents happy or, you know, some kids get their allowance based on grades, you know, stuff like that. Like it's, there's so many like extrinsic motivators that are tough for, especially for kids, I think.

**Ben Eater:** Yeah. And I think that's what you have to unpack is like grade, the grade isn't what's motivating you. It's, it's whatever someone has attached to the grade.

**Chris Gammell:** Yeah, that's true. Right.

**Ben Eater:** When I was in school, like there wasn't anything attached to my grade. Like my parents weren't really that picky, which I think in hindsight, I'm probably thankful for because I, you know, everything turned out okay. And I had time to kind of play and explore. And I think I learned a lot more just in my free time than I would have if I'd been forced to use that free time to drag myself through this homework or whatever they didn't want to do. So yeah, the only, yeah. So I didn't really have a motivation and so I didn't really have great grades. So I think a lot of it is what is, what other, you know, what is, what is a grade a proxy for? And I think it's different for different kids.

**Chris Gammell:** Yeah. Yeah.

**Ben Eater:** But I think the other thing is you, you mentioned that book drive. Um, he talks about mastery, autonomy, purpose, which I think is kind of an interesting thing. If you think about your typical high school kid probably isn't getting any of those things because there's no autonomy. You're being told what to do.

**Chris Gammell:** There's some schools, some schools are starting to kind of push that a little bit more, but yeah, I think that's more like the charter school kind of like, yeah.

**Ben Eater:** No, it's great to see that. But yeah, it's great to see that. But yeah, there's challenges around that obviously, but, but yeah, I mean, if you don't have that, you don't have the purpose is sort of like, well, I'm doing this thing that's going to get graded and thrown away. It's hard to feel there's a lot of purpose to that. Um, mastery. It's like, well, I'm doing something I don't know how to do yet.

**Chris Gammell:** Right. Right. So if you don't feel like you're making progress, it's very demotivating at the beginning. So it's, again, you have to kind of build up from there.

**Ben Eater:** Yeah. Whereas I think if you, if you, if you're further along in your career and you're, you know, you'll say you're a software engineer and you, you know, you know how to program, you know, particular technology really well, you know that you can, whatever problem you're, you're bringing your skills to bear on, you have those skills. Um, yeah, that's, that's where that mastery thing is, is very satisfying. Um, I think it's maybe harder in school. I don't know.

**Chris Gammell:** I mean, I think that's a struggle throughout life, honestly. I mean, like, I mean, from a personal perspective, I've been trying to kind of refocus on skill building and stuff like that because I was, I was harvesting skills that I had built up in, you know, prior years of my career and I was harvesting them and, you know, using them to make money, of course. But like, you know, there's, there is a true, like, it's a, you know, a gift to be able to like take some time and learn new things, whatever. Like that's from having free time, having, you know, monetary stability, whatever. Um, and I feel really lucky to do that. But like, that's, that's a big piece, I think of, of, um, of happiness and being able to, you know, move forward with a career, you know, like, like you're saying, I think that a lot of, a lot of advanced people are, are, um, understand that, but it's, it's the people that are kind of coming up that it's, it's hard to, to impart that, you know, like, how do you, how do you tell someone that that's going to be a thing that's good for them when they're like, well, I just need to get a promotion or get that next job. You know, it's like, oh, well.

**Ben Eater:** Yeah. I think there's confidence though, that comes from knowing you can fall back on something or knowing that there's some, some skillset that's valuable. I mean, you know, you know how to lay out a circuit board, for example, like you, you know, if you need, if you need to do that, you can do that.

**Chris Gammell:** Yeah.

**Ben Eater:** Knowing that you have it. Whereas if you come in and you're like, I don't really know anything, um, you can, you can kind of get by for a while, but at some point you want to have some confidence that, yeah, okay, I'm there's, there's something that I know I'm bringing to the table here.

**Chris Gammell:** Yeah. It's interesting with the confidence thing too, because I, you know, I remember like, um, in classes, it was always the people, the people that were most enthusiastic or the people that were obviously, they had a good grasp on the beginning. And like I said, I, you know, I, I think you said you struggle in school. I struggle in school. Um, I was always really frustrated seeing how engaged they were. And I was like, yeah, but I just don't get it. You know, like, it's just like, until you get to that point of like that, like little light bulb thing going off, it's like, you, it's a very frustrating experience, especially when you have the social peer peer pressure of other people clicking with it. And so it's like kind of getting over that first hump and clicking and maybe, and hopefully even teaching other people. I'm sure that there's, you know, elements of that as well. Like, let me help you show you what I've learned, that kind of thing.

**Ben Eater:** Yeah. And that's, that's a cool thing to see in, you know, some classrooms now where if there's kids that are going ahead, it's, you know, pairing them with kids who haven't yet mastered the thing that they know and having, having the one teach the other. That's, you know, cause then you learn it at a whole nother level when you're teaching someone else.

**Chris Gammell:** Totally.

**Ben Eater:** No, I don't know. Yeah. I think when I was in school, I mean, my, my defense mechanism was just telling myself I didn't care.

**Chris Gammell:** That's the, that's the Fonz method, I think, right?

**Ben Eater:** That's great. I don't know. I don't know if I recommend that.

**Chris Gammell:** Yeah. Yeah. Cool. Well, where do you see yourself doing education stuff in the future? Are you, you know, obviously you're an online teacher. I mean, are you, you're doing more videos and stuff like that? What else, what else are you planning to do?

**Ben Eater:** That's a really good question. Yeah. I'm making more videos. I'm unclear where I'm going to go with that next.

**Chris Gammell:** Okay.

**Ben Eater:** I've been doing like a little mini series on data reliability and CRCs and how, how the math behind that works and how the hardware behind that works.

**Chris Gammell:** That's cool.

**Ben Eater:** Yeah. So finish that up. And then I'm not, I'm not really sure where, where to go next. I know a lot of people want, want to see me build the, you know, make the eight bit computer, you know, add a monitor to it, add a keyboard to it, make it, make it more complex. Um, I don't know how I feel about that. I think it's, like I said, for, for a bunch of breadboards, it's probably about as complex as you want to get.

**Chris Gammell:** Right.

**Ben Eater:** Not going to be reliable.

**Chris Gammell:** Right. To still make it accessible so that people could make their own and it'll work actually, you

**Ben Eater:** know? Yeah. But I don't know. Yeah. Maybe get like a 6502 or something and build a, build something from that a little more complex computer. Let's start, you know, start with a CPU.

**Chris Gammell:** That's great.

**Ben Eater:** I don't know. Yeah.

**Chris Gammell:** Uh, where can people, you know, I was going to say, where can people suggest ideas? Cause there's one thing people on the internet doing is loving telling others what to do.

**Ben Eater:** Yeah. Over on the, over on the Reddit, it's a good place or video comments. I'll read those often. Okay.

**Chris Gammell:** Are you on social media at all? Otherwise?

**Ben Eater:** Um, yeah, I'm on Twitter and underscore eater. Okay. Awesome.

**Chris Gammell:** And we'll link all that stuff in below. Uh, Ben, thanks for, for, uh, talking about all this stuff. I mean, I think the eight bit computer is a, like I said, a good microcosm of the education system. And you know, like I really liked that you're, you break it down for everybody and make it accessible. That's, that's a super awesome thing.

**Ben Eater:** Yeah. Thanks a lot, Chris. All right. We'll talk to you soon. Yeah. Thanks.

**Speaker ?:** We'll see you next time.
