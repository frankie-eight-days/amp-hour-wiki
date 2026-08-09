---
episode: 374
title: An Interview with Claire (née 'Clifford') Wolf
url: https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/
---

**Clifford Wolf:** This is The Amp Hour Podcast. Released January 7th, 2018. Episode 374. An interview with Clifford Wolfe. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Clifford Wolf:** And I'm Clifford Wolfe of Symbiotic EDA.

**Clifford Wolf:** Welcome, Clifford. We usually don't talk to Europe that often, as I've said in the past, because of the time zone stuff. But I'm super glad to be talking to you right now.

**Clifford Wolf:** Yeah, I'm super glad that I made it. Great to be on the show.

**Clifford Wolf:** Yeah, so people probably know you from Twitter or your FPGA stuff. And I mean, I would probably call you prolific. I'm actually looking at your GitHub contribution stuff, and I'm like, oh, that's a lot of green. Oh, man. So we're going to be talking about FPGAs today. We're going to be talking about RISC-V. I keep saying RISC-V. But EDA and Verilog and Linux and all this stuff. But maybe it'd be best if we started back at the beginning. So how did you get into all this stuff?

**Clifford Wolf:** Yeah, I think my first real proper open source project was Rock Linux. And I started Rock Linux in 1997, maybe 1998, something like that. Okay. And it was not really a Linux distribution, but a system that would allow you to build a custom Linux distribution. So the idea of Rock Linux was that back then it took hours to build stuff like LibC and the C compiler and all that kind of things. So if you would need to go through a lot of trial and error to get a distribution built, then this would be very, very time consuming. And the idea of Rock Linux was that pretty much everything was already pre-set up and you could just make the small modifications like what C library do you want to use? Do you want to use a special compiler change that does some tricks to protect against stack overflows? Things like that. And that was pretty successful, I would say, for a couple of years. And then it became more or less obsolete because the computers became faster and faster. And what took many, many hours to figure out in the mid-90s suddenly was something that you could try a couple of times in a matter of minutes, 10 years later on the faster computers. So there was no really big advantage anymore of having this pre-set up thing.

**Clifford Wolf:** Is it almost like a template? Is that kind of the idea?

**Clifford Wolf:** Yeah. So essentially it was a huge set of shell scripts. Oh, okay.

**Clifford Wolf:** Yeah, yeah.

**Clifford Wolf:** But I think it was really a demonstration what you could do if you really would like to do big software engineering in shell scripts, including things like the Bash shell. And I assume others too have things like plug-enabled modules so you can extend it with C code. And we did stuff like that for a few things. It had big org, so AWK scripts, to solve graph theory problems resulting from dependency graphs. So it was not really your typically shell script where just say, okay, just run these commands in this order. But it was more like a big software project. But it literally started out as well, just run these commands in this order to build package XY. And for that shell was very good. So it expanded from there. So this was my first really big project. And I think in a way, it was very representative of the kind of projects that I do. Because I always do other stuff. And then I end up building tools to do the stuff I started out with. So I built Rock Linux not because I started out with, hey, let's build a system to build custom Linux distributions. But instead, I had one very, very small minor project where I wanted to build a Linux distribution. And there I figured out that it was actually quite hard to build a distribution. But it was hard in a more or less unnecessary way. You have to, like, rediscover things that probably 500 people before you also already discovered when they built a custom distribution. So I thought, well, let's build a tool that makes it much, much easier to build Linux distributions. A project that maybe more of your listeners may know is OpenSCut.

**Clifford Wolf:** That's right, yeah. We've talked about that before. And I think my buddy used it a bunch. And it's very script-focused as well, isn't it?

**Clifford Wolf:** Yeah, yeah. So it's like the programmer's 3D cut tool. Right, yeah. So instead of clicking on things and dragging them around with your mouse, you essentially write a script in a special language. That's very, like, inspired by functional languages. I would say it's kind of a mix between a functional and a declarative language. That essentially describes your 3D object. And then you can make changes to this, like, program. And then click the View button. And it will display a preview of what this object will look like. That's interesting. And people are pretty divided when it comes to OpenSCut. So there are, like, people with a programming background that say, oh, finally, a 3D cut tool that they actually can use and want to use. And there are a lot of people with a background in, like, mechanical engineering. Right. They know the other, the traditional tools. And they say, this is completely unusable. You can't do anything.

**Clifford Wolf:** Mine's more of a, I avoid decoding at all costs, even scripting. And I'm like, nah, I'd rather just see it as it happens. So, yeah.

**Clifford Wolf:** Yeah. And that's fine, too. I mean, I think that's the great thing that we don't need, like, one tool that serves everyone. But instead, we can see what is the actual application? What is the knowledge that the user already has? Mm-hmm. Yeah. And I think there is no catch-all solution for all different versions of tuples with, yeah, like that that we can find. Yeah. So that's OpenSCut.

**Clifford Wolf:** Are you still actively developing that? Like, when did that start? And is that still going?

**Clifford Wolf:** Well, it is still actively developed, but I'm not doing it. Oh, okay. So I did it for, like, two years. I started the project, maintained it for two years, and then gave it to Marius Kintel because he was very active with the project, and I kind of wanted to move on to new stuff. So I said, do you want to take over the project? And he said yes. And I think he's still maintaining it, but now there is, I think, a little bit larger community of people actually doing stuff there.

**Clifford Wolf:** Yeah. I'm looking on the site, too. It looks like Google Summer Code picked up some stuff. Other people are probably contributing. So that's interesting. Does that happen with a lot of your projects where they kind of take on their own life? Is it, like, how long, like, did Rock Linux take on other people as well, or was it mostly just you on that one?

**Clifford Wolf:** Yeah, it was a small group with Rock Linux. And with Rock Linux, I would say I kind of missed that point where I should have, like, given it to somebody else to maintain it. There is a fork of Rock Linux, actually, that is still active. It's called T2 and maintained by René Rebe. And I think that's still active. I'm not 100% sure.

**Clifford Wolf:** Okay.

**Clifford Wolf:** But, yeah. But, yeah. So maybe with Rock Linux, I should have made a similar decision much earlier. And then I would have had a couple of more years to work on other interesting stuff.

**Clifford Wolf:** Yeah. No, it's... I mean, that community piece is really tough, right? I mean, like, even with the Amp Hour community, right? We are pretty scattered. There's a lot of people that are out there that, you know, we kind of have things we all talk about. We all enjoy talking to the same guests, right? Like, you know, people are obviously listening to this, and they're interested in what you're doing. But it's not like, you know, like, actually maintaining it of, like, this ongoing conversation is always tough because of the human dynamics of it as well, right? So there's a human dynamics to the community of, like, power distributions of, you know, what, 1% do most of the talking, right? But then the same thing probably happens with the code contribution where 1% or less contribute, whereas many more people benefit from it. Absolutely. Yeah. That's got to be kind of tough.

**Clifford Wolf:** So I think with OpenScut, the interesting thing about OpenScut and the time that it came to be is the parametric aspect of it. Yeah. So when you do, like, injection molding, it's really, really expensive to produce a mold, right? Right. So if you would like to make a variation of your design, then you will pay a lot of money for the new mold. So it doesn't matter if an engineer is busy, like, in the afternoon modifying your design. But with 3D printing, you can do very cheap one-offs.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** And one thing with, so at MetaLab, that's the local hackerspace, we had a lot of people come by and saying, well, this, I don't know, this knob on my stove broke. Stuff like that. Yeah. Can you print a new knob for it? And pretty soon we realized those knobs are actually all very similar. Yep. They're, like, three different basic geometries, what, like, the metal thing can look like. The knob sits on. Oh, yeah, yeah, yeah.

**Clifford Wolf:** The flat side of the rounded out turning piece, right?

**Clifford Wolf:** And then there is, like, what should the angle be of, like, the little indicator on the knob with regard to that. And then there is, like, a diameter for the knob and there is a diameter for the metal thing. So, you can design each knob individually and spend an hour each time making just the right knob. Or you can make a script once. Right. And then when someone comes and says, my knob broke, you just...

**Clifford Wolf:** Right, put in your dimensions and... Yeah, yeah.

**Clifford Wolf:** You know already the five questions to ask, you put in the dimensions and the model is ready. That's great. And I think OpenScut would not have been able to pick up such a large community if it would have been there, like, five years earlier. Because five years earlier, you wouldn't have the means to produce this small one-off things. So, it would not be that important to have this scriptability and the possibility to set this kind of parameters. So, I think with the community building, it's a big question, as always, at what time do you start doing something?

**Clifford Wolf:** Right.

**Clifford Wolf:** And you can do exactly the same project five years earlier or five years later. And you will have to manage a huge community in one case. Or it will be just you. Right. I heard that one. I heard that one. Yeah. And sometimes you have to grow into it, right? Like, you start out with something and everyone is telling you nobody's interested in it and you stick with it for 10 years. Right. And 10 years later, the surrounding evolved in a way. So, suddenly your project becomes relevant to a larger number of people. Yeah.

**Clifford Wolf:** It took me 20 years to be coming over to the next success, right?

**Clifford Wolf:** Yeah, yeah, right. I always love that phrase. Right. Yeah. Yeah. And I think if you're, like, a little bit too late. So, I think the right point to start is actually before this big need is. You need to be, like, a visionary first. And then...

**Speaker ?:** Uh-huh.

**Clifford Wolf:** Uh-huh. Because otherwise it can be that a lot of people react to, like, the thing that you initially make. And you have a huge community overnight. But then your project will disappear equally fast because you just don't have any means to manage this kind of community. Right.

**Clifford Wolf:** Yeah. Well, and also then you get people that are like, oh, well, you should do this and this and this and this. And it's just a bunch of opinions versus if you have that five years beforehand where you're just working on it, you have this vision, you've developed a thing. Yeah. And then they come in and it's like, oh, well, maybe it's actually useful now to have a little bit of input, but maybe not, you know.

**Clifford Wolf:** And in a way, this is very different from, like, how many startups work, right?

**Clifford Wolf:** Right.

**Clifford Wolf:** Because usually you don't have funding to, like, stick with it for five years until your product becomes relevant. Yeah. So, I think they're quite interesting dynamics there.

**Clifford Wolf:** Yeah. Awesome. So, okay. So, you did, obviously, this is still going, so that was, I'd call that a success. So, let's keep that train rolling. So, how did then this translate into FPGAs? How did you get started with FPGAs in the first place?

**Clifford Wolf:** Oh, I got started with FPGAs much, much earlier, actually. Okay.

**Clifford Wolf:** Okay.

**Clifford Wolf:** So, I think my first FPGA board was maybe 1999, something like that. Okay. Just me playing around, learning a little bit of VHDL back then.

**Clifford Wolf:** Okay. And I think I was doing that stuff in school, and I guess I was early 2000s as well. And so, I remember, like, Cordis II, it was Altera's, like, they had, like, this, it was, like, just the lab board. But it was definitely, you know, drawing lines between logic symbols for a lot of it. It was not pleasant.

**Clifford Wolf:** Yeah. I mean, for me, it was HDLs from, like, the Gapco. And I remember back at the time, I looked, like, at the Xilinx manuals and the Altera manuals.

**Clifford Wolf:** Uh-huh.

**Clifford Wolf:** And at least back then, the Xilinx manuals were all about HDL-based flow. Uh-huh. And then there was, like, an appendix that said, oh, if you really want to, you can also draw schematics using this and that, too. Right. But that's not really how you do it. And then I looked at the...

**Clifford Wolf:** Well, that was, like, a lot of the CPLD stuff, too, right? Yeah. Like, CPLDs was a lot of the logic drawing stuff.

**Clifford Wolf:** But Altera back then had their manuals all about the schematic tools. Oh, okay. And then they had an appendix that says, yeah, you could also use HDL, but that's very complicated. Uh-huh. So I... Well, they ain't wrong. Yeah. So I downloaded the documentation of both vendors. And that pretty much was the deciding factor for me, that I knew I wanted to use HDL. Uh-huh. And not, like, schematic entry. Uh-huh. And ever since, I'm an Xilinx guy, you know? Oh, okay. The Xilinx guys and the Altera guys. Maybe we should say Intel now.

**Clifford Wolf:** Oh, right. Yeah. Yeah.

**Clifford Wolf:** But I spent most of my FPGA career working with Xilinx parts. Okay. So I can't even say in what aspects they are better today or worse, because I don't really have the experience on the Altera side. And I guess most of the people who are religious about that are in a very similar situation.

**Clifford Wolf:** Oh, yeah. No, no. I used to talk to the salespeople, and they'd be like, oh, no, no, that's an Altera house. We don't want to talk to them. Like, it wasn't even... It wasn't like trying... I mean, yes, they would try and get them to switch once in a while, but it'd be like that thing they'd go and try and do once a year, you know, versus like, hey, come on in. Because it's much like CAD tools. It's a religion. And it's even worse because it's tied to your hardware. It's tied to all your past hardware. And it's just the switching cost is very extreme.

**Clifford Wolf:** Yeah. You really need to have some kind of special application that you can only do in the one universe and not in the other universe. And even then, companies might decide just not to do a project because it's not possible with the FPGA they already have because they're afraid of the migration cost or their overhead of just having to learn the other tools and the other devices for this one project.

**Clifford Wolf:** So what kind of... So in the past, I've done like signal processing on FPGAs. I've done video processing on FPGAs. I've seen other people doing video stuff. What were you generally using it for?

**Clifford Wolf:** Well, I always build CPUs.

**Clifford Wolf:** Oh, okay.

**Clifford Wolf:** I don't know. I'm a software guy. We kind of like CPUs. So when we do hardware, we build CPUs. I mean, some of the CPUs I built over the years. So I did FPGA for about 10 years professionally for a living. And a lot of it was DSP work. But it was always like special processors that are tailored towards one specific DSP program that they would execute.

**Clifford Wolf:** Right. So it's like a super filter or something. Super FIR filter.

**Clifford Wolf:** Yeah. More complicated. Yeah, I know. I'm just giving the only real example I know. But I mean, one thing that you have with FRI filters is always the question of how many taps you have and how many samples do you need to process in a second. Sure. And in many applications, your FPGA clock will be much, much faster than your sample clock. Or you will only have to process a small snippet every once in a while. So FRI filters are really, really simple to build if you have a low number of taps and a high number of samples because it ends up just building a pipeline, right? But if you have a huge number of taps but a very, very small number of samples, then you need to figure out a way to reuse the same infrastructure over and over again. Use the same multiplier for all the taps. So essentially, your control logic becomes more complex and the data path becomes simpler in a way. And you could think of the stuff that I did as like the extreme of that, where you have an unimaginably complex control logic that makes sure that it can do everything it can do with a very, very simple data path.

**Clifford Wolf:** I guess, yeah, that's the CPU in general, right? That's like you have an ALU that you keep using over and over again and stuff like that.

**Clifford Wolf:** Yeah, right, right. But in this case, it's usually not a CPU. It's more like a microcode programmed special purpose processor. So I did a lot of building CPUs and also build kind of CPUs because somehow you have to write the microcode. And the microcode programs for those are usually the thousands of instructions. So you don't want to handwrite that anymore. Right. And usually people will come and say, oh, that's great. But now we had this other idea. And can you just change your design so it makes this calculation instead of that calculation? And you could just spend like two weeks handwriting an assembler program with a couple of thousand instructions. And then they come along and say, well, can you just change it so that everything is in the front is in the back and everything that's in the back is in the front. And then you are very happy when the couple of thousand instructions were actually generated by a compiler. And you can easily change the code.

**Clifford Wolf:** Okay. So this is, yeah, I was trying to remember the name of the soft processor that DesignX gives to you. So it was not that. It was always very custom stuff, you're saying?

**Clifford Wolf:** Yeah, yeah. That was always very custom stuff. Right. But that also means that I have some experience writing compilers, right? Uh-huh. Right. And so I did also a couple of like toy open source projects around compilers. I wrote a couple of scripting languages just for me.

**Clifford Wolf:** This is like a computer engineering like, you know, dream. All these things that you did for yourself, right? This is like what they all said that we would be doing. But only certain people like you did actually did all this stuff. So that's great. Yeah.

**Clifford Wolf:** Yeah. So I mean, nobody is using any of the languages I think I built. Despite OpenS. I mean, those are languages I built. But I mean, the smaller things.

**Clifford Wolf:** So what was the motivation behind building that? Was it just to get that experience? Or did you actually use them as well?

**Clifford Wolf:** Yeah. I used them for a couple of things. So SPL, for example, is one of the scripting languages I wrote. After I got very, very frustrated with Perl and decided I didn't want to use Perl anymore. But I still wanted to have a language that has a strong emphasis on regular expressions and processing text and stuff like that.

**Clifford Wolf:** Yep.

**Clifford Wolf:** So I built SPL. And then I used it for some time. But I'm not using it anymore. I'm doing everything in Python nowadays. But that definitely was a very, very interesting experience. And in a way, when someone is learning computer science stuff, I would also always recommend to build your own programming language. Wait.

**Clifford Wolf:** I mean, granted, this is me, right? A hardware guy. I'm a solder jockey, right? But where does one even start for that kind of thing? So you said, oh, I don't like Perl anymore. Now I'm going to write my own. What does that look like? What did you write the base language in?

**Clifford Wolf:** Well, I mean, it's hard if you never had any experience with parsers and stuff like that. So when you do computer science at university, which I did not. But if you do it, and if you're lucky, then you will have courses on things like designing parsers and lexers. And you know what a grammar will look like and stuff like that. And yeah, so you write a grammar usually, and then you run it through a tool that's called a parser generator that will transform your grammar into program code that can parse your language. And I'm oversimplifying now. But that's great, actually. Yeah.

**Clifford Wolf:** And I probably shouldn't have even asked that question because, yeah, of course, like Chris is not going to know how to do this. I guess the real question is, though, what is the expected output of this? So now you have a new language. Then what? I mean, like then you start, you said don't actually write with it. You're saying just kind of structure. It's almost like you're outlining a new language but not using it.

**Clifford Wolf:** No, write it, use it for like half a year for some toy project that you're not going to maintain 20 years from now. But don't use it for that because I can guarantee you 20 years from now, someone will come to you and say, oh, there's a problem with this project you implemented back then. Right. And it's using this obscure program language that nobody knows anymore.

**Clifford Wolf:** And if you don't fix it, I hate you, right?

**Clifford Wolf:** Yeah. So don't make your future self hate your present self.

**Clifford Wolf:** That's usually a good... That's great advice. Yeah. So you said you didn't actually learn that. So how did you actually go about learning this stuff then? Was it mostly just a lot of Googling and trial and error?

**Clifford Wolf:** Yeah. Yeah. I mean, compilers was actually more like reading books because I learned the compiler stuff around 2000. Okay. Yep. So there was not that much information online yet or it was not that well structured. Or maybe I was not that much in the mindset yet that everything is online.

**Clifford Wolf:** Right.

**Clifford Wolf:** I don't know. But I remember spending many, many hours reading books on compiler design and stuff like that. Okay. And actually, I can't recommend any modern books because I read stuff like a dragon book back then. Because that was like the reference, the classic. Which one?

**Clifford Wolf:** What is it called again?

**Clifford Wolf:** The dragon book. Dragon book. It has on its cover, it has like a knight sitting in front of a computer terminal. And on the screen of the computer terminal, you see the pixelated face of a dragon. And then you see the rest of the dragon come out the back of the monitor and it's becoming larger and larger. And it actually goes around the cover and finishes on the other side of the book. And I think that's a great metaphor for what compiler design looks like. That you have like this very easy looking front end, but you have this huge dragon behind it. But the thing, so I just started saying, write a compiler and that will give you an abstract syntax tree in some way and so forth. But the important lesson is essentially you figure out a way to break down the problem of taking your input language and producing the output language into many, many small problems.

**Clifford Wolf:** Okay.

**Clifford Wolf:** And then you solve each of them individually. I mean...

**Clifford Wolf:** Oh, is that all I have to do? Okay. That's all you have to do.

**Clifford Wolf:** And the hard part is not writing all the small program snippets to do the individual problems. The hard part is knowing how you can break down the complex problem into smaller problems. And that's where it really helps to read some of the like classic literature. I'm sure there are a lot of texts online. How do you build your own language? Stuff like that. Sure. Sure.

**Clifford Wolf:** Yeah. You're saying just go deep with the actual reference knowledge. Yeah. That makes sense.

**Clifford Wolf:** Yeah. And you always should have a main focus on the data structures. Because usually you have something, a data structure you put into your algorithm and the data structure that falls out of your algorithm. And in many cases, the problem is not really specifying what your algorithm should actually do like on an instruction level, but figuring out what these data structures look like. Yeah. Yeah. And once you know what you want to convert into what, it's usually not that hard to write the actual code that does it.

**Clifford Wolf:** Got it. I mean, I think the, so like kind of piecing together your experience at the point you're talking about too, it seems like you have a strong Linux background, strong C background, strong scripting background, all that stuff. But at this point, you, I mean, you also understood the underlying memory structures and the registers and everything down in the hardware level as well, right?

**Clifford Wolf:** Yeah. I mean, at that point on a, on a very like abstract level. Oh, really? Okay. Okay.

**Clifford Wolf:** So, so it wasn't like later on when, like now that you do FPGA stuff, you're actually, you know, like doing the register, you know, translating a piece of code into register gets designed and placed here. And while this register inside an FPGA gets flipped to doing or look up tables, getting this value or something, right?

**Clifford Wolf:** Yeah. So, so when I started working with, with FPGAs and started to build like my own processor, I, I clearly was, I was not sufficiently prepared to do that. So when I started to write my first compilers, I pretty much knew what I was doing. Um, but, uh, with, with the FPGA and hardware side of things, um, I, I probably just jumped into a couple of, of projects that in hindsight, a little bit too complex. Um, and then somehow managed to get something at the end anyways. Um, but, um, but I mean, most projects I did back then were like just learning projects for me. Um, and I think that's a very important point that in many companies, the only way how you can learn a new skill is by applying it in a project.

**Clifford Wolf:** Yep. Um, I totally agree with that.

**Clifford Wolf:** And, and, and that's horrible because that, that, that project will, will not go very well if it's the first thing you do. Right.

**Clifford Wolf:** You don't want much like depending on that one project. Yeah. Yeah.

**Clifford Wolf:** So you, you, you need to have some kind of, of, of, of framework, some kind of context that, that allows you to just play around with the technology first before actually deploying it in, in, in something that, uh, that matters. Right.

**Clifford Wolf:** And it's a weird balance too, because you want it to be enough where you're motivated by the end goal, but it's not, the end goal is not like your job doesn't depend on it or your, you know, your future motivation doesn't depend on it. And you're like, okay with that failure in that iteration. Right.

**Clifford Wolf:** Yeah. And you don't want, uh, people to, uh, to take on projects. They're not actually qualified to do just because they say, oh, they want technology XY in the resume. Right. But they have no other means to get, uh, the time and resources to get familiar with project XY. Right. Uh, or technology XY. Um, yeah. So, uh, um, and, and, and for me that was just like playing around, learning new things. Um, and I did not do anything like commercially. I actually live with FPJs until five years later.

**Clifford Wolf:** Oh, wow. Okay. That's great. So, uh, so, uh, so, and what kind of job was this at? I mean, was this like a, uh, a design house or something or what, what were you doing otherwise to make, to pay the bills versus playing around with FPJs?

**Clifford Wolf:** Yeah. Yeah. So, uh, uh, uh, pretty much the last 10 years I was, uh, helping to build, uh, 3D laser scanners. Oh, really?

**Clifford Wolf:** Oh, wow. Okay. Yeah.

**Clifford Wolf:** So, um, so, lighter, uh, time of flight measurements. Mm-hmm. Um, and yeah, as you can imagine, there is a lot of, of very, um, compute intensive DSP stuff, uh, going on. Um, uh, primarily you're fighting two problems. Um, the first one is the light is too fast.

**Clifford Wolf:** Um. I've noticed that they should slow it down.

**Clifford Wolf:** Yeah. So the light is too fast. So, so you can't just say, oh, when, when did it become a little bit brighter? And that was exactly when, when the echo came back, because then, you know, a distance maybe, maybe on a one meter resolution or something like that. Uh, but instead you have to do a lot of, of, of processing and figuring out details. Uh, and the other problem is that light is too slow. I've noticed that they should change that.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Uh, because, uh, because when you would like to do a couple of million measurements per second, um, and your target is sufficiently far away, you are sending new pulses before the previous pulses come back.

**Clifford Wolf:** Oh, yep.

**Clifford Wolf:** Um, so you need to figure out, uh, mechanisms to, uh, to know which pulse you received, uh, uh, belongs to which pulse you sent.

**Clifford Wolf:** That's why you always just send little arrows, right? So if you, the arrow's pointing out, then it's one. Yeah, right, right, right.

**Clifford Wolf:** Um, um, yeah, so, so, so, so I, and you could say that, that a lot of my, uh, the work I did was, uh, was fighting these two problems. That light is too fast and that light is too slow.

**Clifford Wolf:** That's great. Well, that, I mean, obviously that stuff is super in vogue right now with all the driving, self-driving cars and just all the, the mapping technologies that are out there. So it sounds like, it sounds like you were ahead of the game on a bunch of things these days.

**Clifford Wolf:** I don't know. I don't know. I'm, I'm personally not a big, uh, believer in, in lighter for self-driving cars. Interesting. I think, uh, uh, passive technologies like just normal cameras, uh, uh, are probably much better, uh, because, uh, when you have an active technology, everyone is sending out their pulses. Uh, so now you don't only need to distinguish, uh, the pulses you sent from each other, but also from the pulses other people send with, with their devices and things like that.

**Clifford Wolf:** Oh, it's almost like the opposite of a network effect where if you have more people in the system, it gets, it degrades the quality of that system.

**Clifford Wolf:** Yes. Yes. And also, uh, cameras are really, really cheap.

**Clifford Wolf:** Yep. Yep.

**Clifford Wolf:** And, and, and nowadays computer vision is really, really good. Uh, so, uh, and it's only getting better. Um, so, um, so I think, um, uh, lighter is very interesting for, for stuff like mapping where you have a car driving down the street once, and then you have like a very detailed 3d model of everything in that street. Um, but for actual self-driving cars, I'm, I'm not, I'm not convinced yet that lighter will actually be the technology for that. Okay.

**Clifford Wolf:** Well, I mean, you're working on it, so I, yeah, I'll take your word for it. You know?

**Clifford Wolf:** Well, I was not really working on that. Uh, I was, uh, that's the thing because I was, I was, uh, I was working on, on FPGA DSP course, uh, uh, looking at waveforms.

**Clifford Wolf:** Oh, got it. Okay.

**Clifford Wolf:** And, and, uh, I always say if you're really interested in like the application, then the job I did was the last job that you should ever do. Uh, because, uh, I, I do, I did everything except anything to do with the actual application with like trading 3d, uh, models of, of, of anything. And usually I only learned about applications of our devices, um, when there was any problem in the field. Um, and, and when everything was working fine, I was not even aware that, that we were doing this or that.

**Clifford Wolf:** So you're like the, like, like they used to say in like the old mobster movies, it's like the guy behind the guy behind the guy. Yeah. That's like you except, you know, it's for technology.

**Clifford Wolf:** Right. Right. In a way, in a way, yes.

**Clifford Wolf:** Yeah. Okay.

**Clifford Wolf:** Uh, so, uh, so that was all that. Uh, and then I started to go to university, uh, uh, 2008 or something like that. Uh, pretty late for me. Um, I first looked a little bit into computer science, then, then decided, uh, it's not really the thing, uh, for me, uh, because they were like, yeah. Um, I, I, I felt like I know all this stuff already. Right.

**Clifford Wolf:** I mean, it sounds like you kind of were out in the world too. And I'm guessing that would probably, I mean, obviously I, I have very strong feelings on university versus like practical experience. It sounds like you were pretty much in the practical realm to start with. And then it would have been, you would have bumped up against that pretty hard.

**Clifford Wolf:** Yeah. And, and, and maybe it would have gone differently if, um, um, um, if there wouldn't have been so many students per like professor or whatever in, in computer science. Uh, but, but for me to get anything from, from the experience, I would have needed like a very individual thing. Right. Right. Uh, because the thing that were a part of, of the lectures and stuff, the things that they, for the most part already knew. Uh, so, uh, so I did, uh, I looked into that.

**Clifford Wolf:** What made you go back? I mean, I guess that's probably the big question there.

**Clifford Wolf:** Well, I didn't go back.

**Clifford Wolf:** Uh, so this is continuing on. Sorry.

**Clifford Wolf:** So, so I, I quit school when I was, uh, 15, uh, to, uh, to essentially, uh, uh, build the, the technical backend for one of the first internet service providers in Austria. Wow.

**Clifford Wolf:** Okay.

**Clifford Wolf:** Uh, which in, so, so in hindsight saying, oh, I quit school and everything will be fine was a very stupid idea. Uh, but in my particular case and in that particular point in time, uh, uh, it turned out it was actually a very good, uh, decision. Uh, yeah.

**Clifford Wolf:** I mean, that's what I usually think. It's more like the opportunities there and you had the knowledge and there's just, yeah.

**Clifford Wolf:** I mean, like, but I can't recommend it to anyone now because like, uh, the time is

**Clifford Wolf:** gone and I wouldn't, I wouldn't recommend starting an ISP to anyone now. Right. Do you know what I'm saying? Oh, okay. That, that, that, that, that, that time has passed. I mean, that puts you also like, so like you've done that. I think Alan Yates, uh, did an ISP at one point, one of our past guests, uh, Sammy did, uh, Sammy Kamkar did, uh, a VoIP startup doing kind of the same kind of stuff. So that, that doesn't surprise me at all. Like, I mean, that's great.

**Clifford Wolf:** Yeah. So, but that means I never finished school. Uh, I never started university. Yeah. Um, and then, uh, 2008, uh, I made all the tests that you need to do in order to go to university, even though you did not finish school. Um, and then I started, uh, uh, um, yeah, um, trying, trying to study computer science. Um, but then I very quickly switched to electrical engineering, um, because I thought, well, there is like more for me, um, to explore this. Yeah. Yeah.

**Clifford Wolf:** Yeah. Yeah. I mean, if you don't mind me asking, is it, uh, was it the, was the lack of degree limiting at a certain point? Um, like as like a gating mechanism?

**Clifford Wolf:** Um, well, I can think of, of a few situations where it was, uh, but then again, in hindsight, I'm not quite sure if I would have liked to really have this, this kind of, um, opportunities anyway. Uh, because if, uh, uh, if it's really a problem that I don't have a degree and I think they don't really know. Right. Right.

**Clifford Wolf:** They haven't looked at your past work. Right. No, I totally agree. Yeah. No, I mean, it's just, again, this is, this is a theme that has come up like Jack Ansell as well. Jerry Ellsworth. I mean, like a bunch of people in a similar situation, um, you know, like didn't finish degrees, whatever. But, but at a certain point it, it's an interesting like paradox because the, the lack of degree sometimes prevented certain jobs from happening or like from certain opportunities. But at the same time, then, then that was the hack that was needed where they're like, well, I'll just go and do consulting on this interesting thing or that interesting thing. I'll teach myself this. And it's almost like it's cause and effect type stuff. And that's, and that's the only reason I ask. Um, yeah, that's great.

**Clifford Wolf:** Interestingly in Austria degrees are like a very important thing socially.

**Clifford Wolf:** Right. Yes.

**Clifford Wolf:** So I wouldn't, uh, be able to think of any particular like business opportunity. Um, but I don't know if, if you like to, uh, um, to move your dentist appointment on short notice and you, you have a doctor to your name, uh, that will change a lot. And if you're just a normal guy, uh, they will give you a lot of heat for it. Um, and that's, that's a, that's a very, very strange thing. Yeah. Yeah. Yeah.

**Clifford Wolf:** Um, and it's a very Austrian thing. So.

**Clifford Wolf:** Okay. All right. All right. Chalk that one up to Austria. Oh yeah. Clifford's in Austria. If people didn't figure that out. Yeah. Probably should have said that. Yeah. Yeah. Oh, that's cool. Okay. All right. So yeah. University. So you're doing EE stuff then. That's great. Yep.

**Clifford Wolf:** Yes. And, uh, um, I have to say I didn't, um, um, in one way I was a very good student because I got only A's, um, and one B. Um, and at the other hand I was a very bad student because after I got the B I couldn't go to, to exams anymore. Um, so wait, what? It's just like a psychological blockage. Um, and actually the A's were also pretty hard because I, I got the A, but in, in my own, uh, um, opinion, I always felt like, like I failed. Right. Um, because I got something wrong that, that was so obvious and stuff like that. And I think that's a problem when you're working in the industry for, for 20 years and then going to university because in the industry, um, you don't get, uh, easy problems.

**Clifford Wolf:** Right.

**Clifford Wolf:** But then strange artificial restrictions, like you must not use any, any special tools or outside help, uh, and it must all be finished in 30 minutes, uh, and stuff like that. Um, but then in the industry, you can't come back and say the answer is two when in fact the answer is five. Nobody's going to say, yeah, well, but, but actually you demonstrated some basic knowledge of the things. Right. Right. Right. Did you show your work? Yeah. So it's, it's, it's, yeah, but that's, and, and that was a big issue for me, uh, because I got an A, but I got the answer two instead of the answer five. Right. Because time was, uh, uh, was so restricted that I did not really have, uh, enough time to like check all the signs in my calculation or something stupid like that. Um, and, uh, and just imagining, I'm imagining a situation in industry where it's like, well,

**Clifford Wolf:** boss, I showed all my work here. And so I think I should get that raise. And they're like, the bridge fell down. You're fired. Yeah.

**Clifford Wolf:** Yeah. Um, and, and, uh, and I think some people can, can make this transition, uh, to this different system, but, but I, I was not really able to do it. Um, and, um, but nevertheless, uh, I was at university and so I had, uh, made some contacts to people at university. And the great thing in Austria is that we don't really pay, um, a lot in, in terms of tuition or something like that. Um, since a couple of years, we, we have to pay something now, but it's like, uh, 500 euros a semester or something like that. Um, um, so you, you can afford staying, uh, at university for like two more years without actually going to any exams, um, and still staying in touch with people. You couldn't really do that if you're like Stanford or whatever. $80,000 a year.

**Clifford Wolf:** Yeah. Yeah.

**Clifford Wolf:** It would ruin you. Um, so, so even though I did not really, uh, uh, finish, uh, any, any degree, I got in touch with a lot of people at the, uh, institutes and I started to publish papers with them, uh, which, uh, uh, turned out to be quite fun actually. Um, and, and one of the research projects that I was, uh, involved, uh, was in cost cost grain reconfigurable architectures. Um, so think of it like, of like an FPGA, but instead of operating on single bits, it is operating on whole worlds and that can do operations like addition and subtraction and multiplication, um, or even more complex operation in a single, like, like primitive cell. So the architecture that we had, for example, had a cell type that could take the absolute value of the difference of two numbers and then check if that, uh, difference is greater, uh, than, than a certain threshold.

**Clifford Wolf:** Um, and that's a single operation though. Is that the idea?

**Clifford Wolf:** And that's a single operation in that architecture. Yes.

**Clifford Wolf:** Wow. Okay.

**Clifford Wolf:** Which is quite funny because when you write code, uh, usually you write like one operator in your code and it's translated to many, many very, very small fine grain cell types. Right. And in this case, the compiler would need to, uh, uh, recognize a certain constellation of operators and say, oh, this set of operators implement that primitive operation that I, I, I can, uh, do with this hardware primitive. Um, yeah. So, uh, so, uh, a PhD student at university, uh, uh, looked into this kind of architectures, um, and, um, and, uh, essentially he wanted me to, uh, to write a, a tool for a domain specific language that would allow to design things in that architecture. Um, and the, the, the overall goal was when this tool would be available, then we would get a, a, a bachelor student or something like that and let them write, uh, test cases for this architecture, um, as bachelor thesis or whatever. Um, and then we could evaluate how good the architecture is. Um, and I first wrote this tool because I didn't want any discussion about that. And it was very easy to write it. Um, and, and then I said, so here is the tool, but actually we do, we should not use a DSL. We should just pass, uh, a subset of regular variolog, um, and infer the primitives from that. Um, and the guy at university essentially said, uh, uh, uh, I'm not going to stop you, but you will fail. Uh, this is, this is ridiculous.

**Clifford Wolf:** I will challenge you directly. The person who likes challenging being challenged directly.

**Clifford Wolf:** Yes.

**Clifford Wolf:** Right. Yeah. Right.

**Clifford Wolf:** Uh, so, so I sit, sat down and, and, and after two months or something like that, I had something that would actually work better than the DSL that we had before. Um, and yeah, that was the start of Yosis.

**Clifford Wolf:** I'm seeing, I'm seeing a theme here. I have to say. That's great. So that's Yosis. Okay.

**Clifford Wolf:** So I think it's a theme with most of your guests, right?

**Clifford Wolf:** I, I, yeah, you, you, yeah. Having talked to many of them. Yeah. It's, it's, uh, it's, uh, it's, it's that certain something, you know, it's, yeah, it's great. It's amazing.

**Clifford Wolf:** Yeah. I said this program now, Yosis that was capable of doing, um, uh, this cross grain synthesis tasks. Uh, and I realized, yes.

**Clifford Wolf:** Okay. So like, if you had to summarize Yosis in a, in a sentence, what would it, would it just be the course gain grain reconfiguration reconfigurable architecture? Or is it something broader?

**Clifford Wolf:** No. So it's, it's, uh, uh, the name Yosis stands for Yosis open synthesis suite. Um, and I would say it's like a framework for, for HDL synthesis and more. And, and at the moment I would say the end more part is, is maybe even larger, uh, than the explicit part, the, the, the HDL synthesis part. Um, but it started out as this framework for course grain, uh, synthesis. And then I realized to do like regular proper fine grain synthesis, the thing that everyone else is doing, I did not need to add that much to, to Yosis. Um, so I added that just, just, uh, because I could, uh, and then I started downloading, uh, very long examples from the, um, and, uh, very often I found something that almost worked with Yosis, there was only one very long feature missing. So I just implemented that feature. Uh, but after I've implemented that feature, uh, but after I've implemented that feature, now another project was, was really close to that point where I could almost process it with Yosis. Only one very long feature was missing. So I implemented that feature. Um, and, and like that over the years or, or the course of maybe two years, so I pretty much implemented the complete very long 2005, uh, standard, um, or everything that is used by, by code out there in the wind. Um, because I always found another project that I only needed to invest maybe two hours to implement this one feature.

**Clifford Wolf:** It was like almost like machine learning where you kept throwing real world examples. It was like, I mean, I know that this is just regular learning, but like machine learning, I think about like, it just, you keep showing it different examples and it, you'd keep trying things until you get rid of all the errors. Um, you might miss one or two of the small errors, but that's not, I mean, that's always an issue.

**Clifford Wolf:** Yeah. Um, um, um, Um, it's like a different thing, but I'm, I'm, I'm trying to find the, uh, the name for it in my hat. Um, um, um,

**Clifford Wolf:** It's definitely an iterative approach for, I mean, for no, no doubt about that, but yeah.

**Clifford Wolf:** So in machine learning, you have this technique where you, um, start out with very small examples and then make the examples more and more complex. Uh, so you do that for example, when you would like to build a robot that can find its way in a maze. Um, and if you just drop it in a really, really huge maze, it will just randomly go around. And, uh, the best reinforcement learning algorithm will not be actually able to, uh, um, to figure out what was the right behavior that made the robot solve the maze. Um, so you start out with small mazes and then make the mazes larger and larger and larger, and then you can use reinforcement learning for something like that. Uh, but actually wouldn't want, so we could let's talk about machine learning another time because machine learning is also a topic for me.

**Clifford Wolf:** Uh, God, oh geez, of course it is. Yeah. Okay. So I have, I have a different question then. So, um, so could you explain what synthesis is, right? So people might know what that actually means in the first place. So you're starting with Verilog and then what is it doing to it?

**Clifford Wolf:** I mean, um, um, synthesis is used in so many contexts, right? Uh, you create something, uh, essentially, or you have a program create something. Um, and with logic synthesis, you have a pro program generating, um, a logic circuit, um, that might be made out of gates or, uh, lookup tables or other logic primitives. Um, and you have some kind of, uh, of description what the logic should look like, uh, usually as, as HDL code. So you might have an adder in your HDL code, and then the synthesis tool might translate that to a dedicated adder primitive for cross-grain synthesis, for example. It might turn that into a chain of carry cells in an FPGA-based synthesis approach. It might turn it into NAND gates and NOR gates for an ASIC synthesis task. But whatever your architecture is, you have some kind of architecture that allows you to implement logic circuits, and you have some description that tells the tool what kind of logic function you would like to calculate. And the synthesis tool bridges these two worlds. And you could call a compiler, for example, an assembler program synthesizer. But it's pretty much the same thing. It takes a high-level description or higher-level description in one format and performs a sequence of transformations to create the equivalent representation in a format that you can actually work with. So when you have a program, you compile it into machine language, into assembler programs. If you have a circuit, you start out with something like the HDL description, and you end up with NAND and NOR gates if you're building an ASIC.

**Clifford Wolf:** Okay. So what is the actual output of IOSIS then? Is it like a separate language? Because it's not actually targeting any logic at this point, right? Yeah.

**Clifford Wolf:** Yeah. I mean, at this point, we are targeting the coarse-grained stuff. And there is a framework in IOSIS that allows you to express what your coarse-grained architecture can actually do. And then it will know what kind of thing to generate. For the coarse-grained synthesis, I actually wrote an interconnect generator for coarse-grained architectures. And IOSIS that's called Intersynt, has even synted the name, because it generates an interconnect. So it's an interconnect synthesizer. And that has a netlist format that IOSIS can generate. But I think the only person using that or ever used that was this one PhD student who worked on the coarse-grained architecture. There are a couple of different file formats for logic circuits. And IOSIS can generate a whole bunch of them and can also read a few of them. And, yeah.

**Clifford Wolf:** Are there some examples of those that people might recognize?

**Clifford Wolf:** EDIF, for example. So EDIF is a format that's in very widespread use in the industry. EDIF, B-L-I-F, the Berkeley Logic Interchange format, is...

**Clifford Wolf:** One of those Berkeley folks, yeah. Yeah, yeah.

**Clifford Wolf:** That's a format that's very popular with open source tools. Of course, I can generate Verilog again. And amazingly, a lot of industry tools process as... So place and route tools and stuff like that process as inputs very, very simple, strict subsets of structural Verilog. Oh, interesting. So that's also an option. I would need to open the IOSIS help page to go through the entire list. Okay. But there are a couple of formats. There is a JSON format that is very IOSIS specific to make sure that we have something that is, on the one hand, easy to pass. But at the other hand, it's not really losing any information in a way that would be avoidable. Right.

**Clifford Wolf:** Because if you have like a super custom coarse-grained thing, you want to be able to say, well, you might not know what this, you know, ABC adder is, but that's what it is. And keep it around.

**Clifford Wolf:** Yeah. It's more like when you have a file format that IOSIS can, for example, write and read. Uh-huh. Uh-huh. So if you, in a loop, write it, read it, write it, read it, write it, read it, without running any optimizations in between, then your design could become bigger and bigger and bigger and bigger. Um, and maybe it's just because it adds additional wires that are aliases for the wires that are already there and things like that. Um, so, uh, and, and the JSON format does not have this, uh, this issue. Um, and it's used for tools that, uh, are used in flows after IOSIS, but are written specifically to be used with IOSIS. And so in that case, uh, it would be ridiculous to generate an output format, um, that does not exactly represent the internal representation IOSIS is using. Uh, and then read that format in a set, in another tool that now has to pass a more complex format because it passes this other thing instead of the, the JSON output we generate. Um, so there are a couple of tools out there that can process IOSIS JSON files.

**Clifford Wolf:** Very cool. So, okay. So now you're in this new format or, you know, maybe even if you're back into Verilog. So this is something that you would actually then target at a processor or what is the, what is the next step? If you're going to take this, you're trying to go from Verilog and you're trying to target a processor or target an FPGA.

**Clifford Wolf:** Yeah. So if you're targeting FPGA, uh, then, um, um, then you would need to do place and drought next, uh, because the output of IOSIS is only a so-called net list. Um, so it's the list of all the gates that you have in your circuit and, uh, uh, the list of pins on those gates that need to be connected to each other. Um, but it has no, uh, a placement geometry, geometry information. Um, so it doesn't know where, which gate will go on the actual device. Um, and the placer does exactly that. The placer figures out where to place all the individual gates so that the things that are, uh, are tightly connected to each other also end up being close to each other on the actual FPGA device. Uh, right. Otherwise you would need to route signals all the way back and forth, uh, through the chip. Um, and yeah, I mean, it's the same when you, when you build a, uh, uh, uh, a PCB. Uh, yeah. If you just randomly, if you just randomly throw the components on the PCB, you probably won't be able to route it. Um, so the placer figures out a good placement. Um, and then the router tries to actually make those, uh, connections.

**Clifford Wolf:** Right. And there's only so many fixed paths. So like, it's like a crosshatch of, of potential ways to get from one point A to point B, right?

**Clifford Wolf:** I mean, uh, um, interconnect is the thing where different FPGAs, um, make, uh, slightly different design decisions or even vastly different design decisions. But, uh, but as fast approximation, it's something like that. Um, where you have, uh, certain lines and certain points where those lines cross. Um, and if a line is used for one signal, it can't be used for another signal. Um, and, uh, yeah, you have, uh, rip up routers. They essentially try to, to route some nets, but then they figure out, oh, I can't route these other nets now. So they rip up the nets that have routed before to route the new net. And, uh, when you iterate over this, uh, for a certain amount of time, you hopefully end up with something where every signal is routed.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** And, uh, uh, different algorithms you could use for all of that. Um, and the vendors usually write tools for their own devices there. Um, so, uh, you would use a, a tool from Xilinx for the Xilinx part, a tool from Altera or Intel for the, um, Intel FPGAs, a tool from, I don't know, uh, Microsamia for the Microsamia FPGAs from Govin for the Gomi7 FPGAs and all that stuff. Um, but the synthesis part is usually, uh, something they buy from somewhere else. Um, so the two big players are the exception here. So, uh, Xilinx and Altera or Intel. Um, yeah, that, that's like, uh, burned into my head. Yeah, right. By, by, by, by the time I, uh, I get, I'm getting used to saying Intel, they have probably sold the entire FPGA division. Yeah, yeah, yeah, yeah.

**Clifford Wolf:** Yeah, I still call it Actel. I don't call it Microsamia, you know?

**Clifford Wolf:** Yeah, yeah, yeah. And, and, and, uh, do you still say Agilent?

**Clifford Wolf:** Uh, yeah. Well, if I don't say HP, yeah. Yeah, yeah, right.

**Clifford Wolf:** Yeah. Um.

**Clifford Wolf:** So, so you're saying the, the other synthesis tools. So synthesis tools are, are not, so those are usually not written by the companies themselves?

**Clifford Wolf:** Yes, they, they're usually bought from, from other companies, um, and then, uh, multiple FPGA, FPGA, uh, design environments will actually use the same synthesis tool, uh, from the same synthesis tool vendor. Um. Yeah.

**Clifford Wolf:** I have used Simplicity or Simplify Pro Simplicity at some point. Yes, exactly. Yeah.

**Clifford Wolf:** Exactly. That's, that's, that's the kind of tools. Okay. Um, and in, in flows like that, Yozes, uh, can, uh, almost always, uh, replace something like, uh, Simplicity. Uh-huh. Um, um, I'm, I'm not saying that they generate, like, equally good results. Um, but, uh, you can.

**Clifford Wolf:** But because there's, like, an interchange format, you're saying that that's, that's, like. Yes. It's very easy to determine, yeah.

**Clifford Wolf:** And, and, and, and usually the FPGA architectures are similar enough to each other, uh, that it's, uh, uh, easy to, to write all the descriptions for another FPGA, FPGA architecture for Yozes and then, uh, then use it.

**Clifford Wolf:** Right. I always remember people talking about, like, the, like, Xilinx stuff has, like, custom types of logic internally, right? Like, they have ones that, if you target that specific logic, it would work on their parts, but it wouldn't work on another, like, an Altera part.

**Clifford Wolf:** Yes, yes. So, for example, the, the way, um, adder chains are built are slightly different on each FPGA. Uh-huh. Um, but then, uh, um, wherever you go, you have something to build an adder chain. Uh, so all you need to do is tell Yozes how to build an adder chain on this architecture.

**Clifford Wolf:** Uh-huh.

**Clifford Wolf:** Um, and the way Yozes is built, you can actually do that with, uh, with, uh, with small Verilog code snippets. Um, so if you already know how to write Verilog code, you know everything, uh, at least language-wise, that you need to know how to retarget Yozes.

**Clifford Wolf:** Got it. Okay. So what is the, what is the place and route tool then? So Yozes gets to this interchange form, edef, bliff, Verilog, JSON, whatever. Then it's doing place and route. Is that a separate tool?

**Clifford Wolf:** Yes, and that's a separate tool, usually written by the FPGA vendor. Um, oh, okay. And that was more or less the state at maybe, uh, 2013.

**Clifford Wolf:** Uh-huh.

**Clifford Wolf:** Um, and, um, I always thought, uh, wouldn't it be great if we would have, like, open documentation for the bitstream formats and stuff like that?

**Clifford Wolf:** Right.

**Clifford Wolf:** Uh, so that we can build actual open source place and route tools for all these architectures. Um, and, uh, um, when I did talk to people from, from the major vendors, I pretty much always got the same answer.

**Clifford Wolf:** Um, no.

**Clifford Wolf:** Yes, yes. But, uh, I mean, the no is a cultural thing, right? They don't even think about the reasons. Right. But then they have to, like, uh, construct a reason.

**Clifford Wolf:** Right. Because previously they've been like, well, what are you going to do with it? Right. And now it's like, well, we're going to do something with it, but are we allowed to do that?

**Clifford Wolf:** So, so the reason, uh, I always got was even if the vendor would release the documentation, we wouldn't have the, uh, the resources and the knowledge to actually build place and route tools. Um, because you need like a hundred PhDs, uh, and, and a billion dollars to, to build a place and route tool.

**Clifford Wolf:** That sounds like a challenge to me. I'm just saying, you know. Yeah, yeah.

**Clifford Wolf:** Right. Um, so, uh, so it became pretty clear that, uh, uh, in order to have a good argument for releasing bitstream formats, uh, we first have to demonstrate that we actually can write good place and route tools. Um, and in order to do that, we had to reverse engineer bitstream format. Um, so, uh, that's, that's pretty much what I did. Um, um, so that's project ice storm. Um, we took the ice 40 FPGA from lettuce. Uh, and that's a relatively small FPGA and it has a, a very, very regular structure. Um, uh, so you don't have like, uh, a thousand different, uh, um, special function units that have their own kind of configuration. Uh, all you have in an ice 40 FPGA. So the, the ones we targeted initially, the LP and HX series, uh, are lookup tables, uh, flip flops. Uh, carry, uh, sells some block run primitives and IO blocks and also a PLL. Um, so I, uh, spend, um, yeah, uh, a large portion of 2015. Um, uh, um, working on that, uh, reverse engineering, the bitstream. Oh, sorry. Documenting the bitstream. Um, um, um, I've recently learned that, uh, that for lawyers reverse engineering actually means like disassembling something. Uh, but that's not what I did. I just threw things at the, at the vendor tools and then looked at the output files they generated. Right. Right. And I mean, for, for most engineers, this is reverse engineering, but apparently for lawyers, it's not. Um, um, so I, I, we documented the bitstream format, uh, and, uh, the, we created the Yozo's backend for that. Um, and, uh, Cotton Seed wrote, uh, a place and route tool for it called Arachni PNR. Uh, and, uh, so by, um, mid 2015, we had a complete open source, uh, tool chain for this, uh, lattice Ice40 FPGAs.

**Clifford Wolf:** That's pretty killer. Yeah. That's, that's, that's the first I gotta say.

**Clifford Wolf:** Yeah, that was great. Uh, so, uh, later we added support for the larger 8K devices. Um, just recently, um, we, uh, we added, added support for. Uh, uh, I'll pass, uh, uh, devices. Uh, David did that. Uh, and, uh, yeah, so, so we have.

**Clifford Wolf:** Are the methods the same when each, each next thing you have to document of the bitstreams? Is it, is it the same kind of like iterative, like try file one, see what the bitstream is, try a file to see what the bitstream is, change this, change that, see what the output is?

**Clifford Wolf:** Pretty much. I mean, the method is the same for all, um, Ice40, uh, devices. Um, it's a little bit different for the Xilinx devices. Um, but, uh, but we're not there yet in the history, right? We are just in 2015. Right.

**Clifford Wolf:** Oh, true, true. I see, I see. And, and, and, and just real quick, the, uh, can you explain what the bitstream actually is? Because I know what it is, but, well, I think I know what it is, but yeah.

**Clifford Wolf:** Um, I mean, it's a, it's a binary configuration file that tells the device what to do. Um, and as, as far as most users are concerned, it's just a huge binary blob that the vendor tool will generate, um, and that you can only use as is. So usually there is, there is no meaningful way to make a modification to bitstreams, for example. Right. Um, but, uh, uh, yeah, there are also some, some, uh, scientific publications underway, uh, regarding making meaningful, uh, changes to bitstreams to activate trojans and stuff like that. Oh, really? Interesting. Yeah, yeah, yeah. So that's, that, that, that's one of the topics that I, uh, I publish on with the people from, from TU Vienna is, uh, hardware trojans and, um, uh, trigger for hardware trojans and stuff like that. Um, and then you, when you think about the security of FPGA devices, it really helps a lot if you can tell what the individual bits in the bitstream do. Um, um, also because that then allows you to actually demonstrate the possible attacks and not just, um, speculate about what could theoretically be possible.

**Clifford Wolf:** Right. I mean, what do they do now? It's just like, they have the bitstream itself and then they have like a hash on the bitstream to see if it's actually all adds up. Is that kind of the only real security device right now?

**Clifford Wolf:** Yeah. I mean, most bitstreams don't have any security at all. I mean, there's just a CSE on it to make sure that there are no transmission errors, but that's not really, that's not even a hash or anything. Um, um, and the, um, the idea pretty much is that it would be so complicated to document it. Document the bitstream, uh, that nobody would be able to do it anyway. So it's essentially obscurity. Yeah. Right. Uh, and that, of course, historically never worked. Um, right. When I originally released project ice storm, uh, the first thing that I released was just a tool that could look at a bitstream and produce an equivalent Veralog source code. Oh my God. Um, because that's, that's great for a verification loop. Um, so what I try with all projects like that is to automate as much as possible, uh, other that makes it much more reproducible when other people can like run the same scripts and stuff like that. Um, and, and, and the most important thing is that you have, uh, uh, uh, continuous, uh, checking and rechecking. If the things that you think you found out are correct, uh, because if you go down, uh, an incorrect path and work on, on, on, with, with incorrect assumptions, uh, then it will become super hard to, to document an FPGA bitstream. Um, so whenever you have a theory, you should write some kind of small program that, uh, um, that in one way or another tries to check if your theory is correct. Um, and what I did with the ice 40 was I generated thousands and thousands of, of random programs, random Veralog designs. Uh, and then I synthesized them all with the vendor tools. And then I extracted the circuit from the bitstream with this other tool. And then I checked if the extracted, uh, uh, circuit from the bitstream is equivalent to the original auto-generated circuit.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, and if this is true for thousands and thousands of auto-generated designs, then you have a high confidence that actually your model of what the individual bits and the bitstream do is correct.

**Clifford Wolf:** Right. Um, I kind of think of it like, uh, doing, if you did like Google translate, so if you went from German to English to German to English to German to English, if it's the same phrase each and every time, well, for a range of phrases, then the translation is perfect. Obviously there's a little bit more nuance in language. Yeah. Yeah. Yeah. Yeah.

**Clifford Wolf:** So, so, uh, so in language, I think this is like the, the ultimate goal that is unreachable. Uh, but with, with, uh, with logic, uh, uh, gate circuits and FPGA bitstreams, um, this is essentially the only acceptable thing.

**Clifford Wolf:** Yeah. You're right. It's in the name, logic. Yeah.

**Clifford Wolf:** If there is, if there is only, if there's only one very, very small, uh, deviation between what you got out and what you started with, uh, behaviorally, uh, then, uh, then there was a bug somewhere in, in, in your documentation or in your tools. Um, yeah. Yeah. And, and so, because that was an, an inherent part of the process that I used to, uh, to do the actual documenting, um, uh, because of that, it was like the first thing that I could release. Um, and immediately I, I got very, very angry email from, from people.

**Clifford Wolf:** Um, um, Lattice. Is this when you started talking to lawyers?

**Clifford Wolf:** Not, not from Lattice. Okay. From, from, from random people, uh, who said, uh, very unfriendly things. Um, and, and seemed to like work under the assumption, uh, that I like to steal their IP in particular.

**Clifford Wolf:** Uh, because. So that's some ego coming through in the email. Yeah.

**Clifford Wolf:** Yeah. Um, and, uh, my only theory about that is, uh, and so I've been in a couple of, of companies that, uh, had discussion about how can we protect our IP and stuff like that. And there is always one person who said, well, I don't need to think that we need to do anything because it would be too complicated for anyone to actually make sense of the bits in the bit stream. Um, and I would assume that, uh, that one guy was, did this guy in a meeting like two days before my, my, uh, initial release was published on Hackaday. And like he said, oh, nobody can do that. And like the next day.

**Clifford Wolf:** Uh, yeah.

**Clifford Wolf:** Um, so yeah, so I, I have not replied to the emails. Uh, I don't know what the actual story is. Uh, but, but to me that sounds like a very reasonable, uh, explanation. Yeah. Right.

**Clifford Wolf:** Um, or, or some variation on it. Right. Cause it's probably multiple times, right. Where if you got more than one email, it's a bunch of people are like, oh, you've just ruined my worldview.

**Clifford Wolf:** Yeah. Um, so by the beginning of 2016, I, I was pretty much finished with, with the original ice 40 stuff. The last thing I had to do was a timing analysis. Um, and that was done in January, 2016.

**Clifford Wolf:** Um, yeah, that's, and that's good. I mean, you've kind of walked us through all of the tools that, uh, FPGA flow does anyways. Right. So you have going from, you know, a, a language like Verilog to the logic blocks. You do the place and route or so you, uh, what was the next step? So the next step is actually, yeah, place and route is next, right. Then you need to do timing to make sure everything gets from point A to point B. If you want to make a mega, a hundred megahertz clock or something like that. Yes. Yeah. Yeah. You need to make sure you can get all the way across the chip and everything hits, hits the, hits the mark. And, uh, and then what, then you actually have to just generate the final bit stream and shove it into the, to the, uh, to the, to the FPGA, right?

**Clifford Wolf:** Right. That's it. And we have open source tools for each and every of those steps. Um, that's a complete thing. Um, and, and we can do a couple of things that the vendor tools can't do. Uh, for example, um, I can take a bit stream file, um, convert it into our own ASCII representation, uh, and then run timing analysis on that. Uh, the vendor tools don't allow you that you can't run timing analysis on a bit stream with, with the vendor tools. Um, so if, if you have some outside entity and they make it designed for you, uh, and you say, yeah, it must run with a hundred megahertz. But for like, I don't know, copyright reasons, they only give you the bit stream and they don't give you anything else. You can't actually check if the timing goal is reached, right? Yeah. Yeah, you can now.

**Clifford Wolf:** Wow. So is that because you were perfectly recreated and that's because of the perfect recreation of the Verilog or logic elements from the bit stream? Is that the idea?

**Clifford Wolf:** Yeah. I mean, it's, it's using a different, different flow. Uh, but the main reason is I need a way to actually verify that my timing analysis is correct. Uh huh. So what do I do? I run timing analysis with the vendor tools for a design, again, a randomly generated design. Um, and then I store the bit stream and then I run my timing analysis on that bit stream. So now I have run the vendor timing analysis and my timing analysis on the same design.

**Clifford Wolf:** Oh, I see.

**Clifford Wolf:** And I can compare if they produce the same results within a few picoseconds.

**Clifford Wolf:** Got it.

**Clifford Wolf:** Yeah. And they do. So I know my timing analysis is sound.

**Clifford Wolf:** Right. So if they would have just given you, they would have just given document in their own bit stream. You never would have had to make all these tools that made everybody so upset. You know, it's their, it's their fault. And that's why people should be more open.

**Clifford Wolf:** I think the main point here is that, uh, um, most of this stuff was, was like me more or less in my spare time, uh, plus a handful of other people, uh, helping with various, uh, things. Some of them are large things like, like cotton wrote the entire, uh, which was very impressive. Um, and, uh, and they've shot at the entire, uh, ultra plus recently. I had, I didn't need to do anything for that. Um, but, but it's a very, very small group of people, um, with, uh, very limited resources. Um, and it was not that hard actually. Um, so if, for example, a large, uh, Chinese corporation doing industrial sparence or whatever, uh, they, they would have no problem doing something similar.

**Clifford Wolf:** Right. Um, right. So mad because you've made it available to them. It's like, well, they might've already done it and just not published about it. Right.

**Clifford Wolf:** They have no reason to publish any of that, but, but I don't think that I would actually be surprised if we really be the very first group to do that, uh, for this FPGA. Um, I know that other people did similar things for Xilinx FPGAs in the past.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Um, so, um, um, So we actually not the first one. So as, as some of, uh, your listeners might know, we are right now working on, on doing the same thing for exciting seven series FPGAs. Oh, nice. Um, and a couple of weeks ago, we, uh, we released the first bitstream documentation. Um, so if you always wanted to know what, what this or that bit in your bitstream does, then now you can go to a webpage and look it up. Uh, but, uh, so far we don't have the tools finished. So right now we are working a lot of, uh, on, on, on, on, on the tools, but it's all on the way. And I guess, uh, uh, many people would say that, um, actually documenting the bitstream is, is the hardest bit.

**Clifford Wolf:** Yeah. Okay.

**Clifford Wolf:** Um, so we've done that, um, at least for the, uh, the basic logic cells and, uh, the CLBLM, uh, tiles. And that's most of the, the FPGA and the interconnect tiles. Uh, we know them, but we don't have a detailed bitstream documentation yet for DSP slices, for block ramps, and then for all like IO related stuff, uh, uh, and things like that. Uh, but the nice thing about Xilinx seven series is the Xilinx seven series, uh, allows partial reconfiguration. So you can, you can define, uh, a certain area on your chip and say, Oh, this is now my FPGA within the FPGA. And you generate bitstreams that only update this, this particular area. Um, and you can still interact with the rest of the, the FPGA. Um, so this is our first target for Xilinx seven series. We don't need to actually generate a complete bitstream for the entire device. Um, we could have a kind of harness and synthesize the harness in the vendor tools. Um, and that harness contains a reconfigurable section. And then we use our open source tools to reconfigure that reconfigurable section. And I actually think that for this, there are much more like industrial use cases than for actually replacing the vendor tools with the open source tool chains. Um, I would imagine that, uh, especially in the near future, um, most people would not see any advantage to, to replacing the vendor tools completely. Um, but the interesting thing is our tools are open source tools. Uh, when you have something like a Zync FPGA that has a embedded ARM processor that runs Linux, you can run all our tools on that ARM processor and build a bitstream on demand in the device to do exactly what you want to do.

**Clifford Wolf:** I mean, that's the dream. That is the dream. And so one, and then you have like, so basically it's like a prototyping area, but in an FPGA, right? That's the idea is like the, that little playground area is what you can make the, you can use the ARM to make the tools to, to play around in that little sandbox. Yes.

**Clifford Wolf:** And so I'm a strong believer that, uh, when you, uh, when you create the tools, you don't know all the applications yet. And I think it's the same thing here that, that most of the, of the most astonishing killer applications that will come from that are things that I can't even dream.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Um, but I can give you one, uh, one example, uh, that this could be useful and it's in a logic analyzer. So, uh, when you have a logic analyzer, you usually have a, uh, means to define very, very complex trigger conditions. Um, and those trigger conditions are of course implemented using a trigger unit that you built in the FPGA, uh, that, uh, is very configurable. Um, so in a way you just build a reconfigurable architecture in a reconfigurable architecture. It's a, uh, genormous waste of resources. Um, um, and it's not going to be as fast, uh, or as flexible as if you could, uh, just expose all the flexibility from the underlining, uh, uh, reconfigurable architecture, the FPGA itself. Uh, so what we could do instead is if when the, when the user clicks on acquire, we take the trigger condition, uh, translate it into a logic circuit, synthesize the logic circuit, place and route it for this reconfigurable architecture, generate the bitstream and then program the bitstream. Um, and, uh, but you could, you couldn't do that with the vendor tools. Even if Xilinx would, would open source all their tools tomorrow, you still could not do it because their tools are so optimized to a different scenario. The, when, when you start up Vivado, it, it, it's not uncommon for it to, to think for a couple of minutes before you can interact with the tool at all. Um, and I mean, that's, that's fine. If you start Vivado in the morning and then two times more over the course of the day after it crashed. Uh, um, but, uh, and it's okay if you have synthesis jobs that, that take hours and hours because they're huge designs. Um, but with this partial reconfiguration area, we are looking at a, a very, very small FPGA in the end because this area is very, very small.

**Clifford Wolf:** Um, like how many logic blocks would you imagine would be in there?

**Clifford Wolf:** Uh, I mean, you can, you can, you can choose whatever you want. Uh, but just to give you a data point, um, the, um, ice 41 K has, has 1000 logic cells. Uh, so 1000 look at tables, 1000 flip-flops and stuff like that. Uh, 1200 something, but, uh, who counts? Um, and, uh, um, for a small designs, we can go from Verilog to Bitstream in less than a second. Whoa. Um, for large designs, we're actually a little bit slower than the vendor tools, but for slow design for, for, for, for small designs, we are super optimized. And this is also great for stuff like workshops. Uh, when we do workshops, people can like make small changes to the design, click one button and immediately see the result in hardware. Uh, and don't need to like wait for three minutes for the design chain to change, to go through. Um, and when you, uh, for an experienced FPGA engineer, this is not an issue because the experienced FPGA engineer isn't, isn't synthesizing most of the time. Uh, most of the time you're just simulating, you're working on, on individual cores. Uh, and then when you synthesize your whole design, it will take a day or something like that anyways. Um, so, so if you would like to do like iterating on small changes by testing it in hardware, you don't think something completely wrong. Uh, right. Um, but, but, but it's how most people start playing with this kind of technology. Um, and, uh, and, and we can do something like that. And, uh, so for, for the logic analyze example, that would be a possible, uh, application, um, for, for this that you can't really implement with, with, with the vendor tools, uh, also for, for like licensing issues, uh, but also for other issues because they.

**Clifford Wolf:** Right. Cause if I, you don't want to give me all the source code for an arm probably, but you might want to be able to enable me to play, you know, give that custom logic next to the arm.

**Clifford Wolf:** Yeah. And, uh, yeah.

**Clifford Wolf:** Is that, is that one of the concerns I would suppose? Like, so if you can, if you could, uh, reverse engineer a bit stream of something that has an arm internally, could you then go and pull out the Verilog that determine what that arm processor does?

**Clifford Wolf:** No, because that arm processor is a hard IP block. Oh, okay. So it's, it's, it's not really configured by the bit stream.

**Clifford Wolf:** So they don't even get, they don't even give, uh, the, the bit streams that would have an arm processor.

**Clifford Wolf:** Yeah, because there is no bit stream. So, um, um, with, with other devices, I think Altera once had a, uh, soft IP arm.

**Clifford Wolf:** Yeah. They, I remember they had like early, they used, they had like really early stuff. They had like an M, not an M zero, but it was something before an M zero. Yeah.

**Clifford Wolf:** But, uh, uh, the processor blocks in, in Xilinx FPGAs, um, so. Microblaze? Uh, microblaze is of course a soft IP. Um, yeah. So yeah, you, you, you could, you could generate a microblaze netlist by, um, by looking at the bit stream, but you don't actually need to, you can just generate a timing netlist, for example, and then the tools will already give you a netlist for the microblaze. Um, so the only thing they're really hiding there is like the, the more readable actual very low code they put in. Right. Um, but for stuff like when you look at the older, uh, uh, vertex two pros, they had power PCs in there. They have, they have a hard IP blocks. Uh, and now in, in, in, in syncs, the, uh, the arm is in hard IP block. Um, so only thing that the, uh, the bit stream does is configuring how these hard IP block connects to your logic. Uh, but it, but the IP, IP block itself is a complete black box. Um, and you could swap out the, the, the theoretically, the, the arm block with the risk five block, for example, I mean, as, as vendor Xilinx could do that, uh, without having to change the bit stream format.

**Clifford Wolf:** Right. Right.

**Clifford Wolf:** As long as the interfaces are still compatible.

**Clifford Wolf:** That is a, that's a great segue. So let's, let's talk about risk five because that's, that's, uh, so you, you had mentioned to me before the show that the, the risk five is entering the chip scene. So obviously we've heard some of the stuff we've talked about, me and David talked about a little bit, but like you told me that like, it's actually pretty, pretty high interest levels in, uh, in the chip community. Yeah.

**Clifford Wolf:** So, um, so if you're like in the AC community, then, then you definitely have heard of risk five. Uh, and probably your company has some kind of project that is using risk five or is related to risk five. Um, uh, and, and just as one data points at the last risk five workshop, this was, um, two months ago, something like that. Um, okay. Uh, uh, Western digital, uh, actually. So Western digital is, is shipping a billion processor costs a year. Oh my God.

**Clifford Wolf:** Um, just in their hard drives or in other stuff too?

**Clifford Wolf:** In the hard drives and whatever else. But, um, but if you, if you look at the modern hard drive, it had a couple of small processors in it, uh, so that, or adds up to about a billion processors a year. And they have now announced that, uh, by, uh, 2019, they would like to have them all replaced by risk five.

**Clifford Wolf:** Whoa. Wow. Okay. So why? I mean, is it just cause it's free or because they want to customize it?

**Clifford Wolf:** At least they, they claim it's not because it's free. Um, and I also, I don't think that this is the, the, the main reason for them to do it.

**Clifford Wolf:** I mean, imagine the IP costs would be a small portion of the overall costs of making a thing. So yeah. Yeah.

**Clifford Wolf:** So the, uh, the, the main thing I guess is that, uh, you have, you have a wide range of costs to choose from, from different vendors that have different application domains in mind. Um, and you can always use the same tools. You don't need to retrain engineers to the arm tools in this case. And then some special instruction set in the other case, um, you can easily switch vendors. Um, you can easily extend processors to implement additional features that you just happen to, to need for the application you, you work on. Uh, so maybe we should start out by explaining what risk five actually is. Sure. That'd be great.

**Clifford Wolf:** Just, uh, cause Lord knows me and Dave didn't do a good job with it.

**Clifford Wolf:** So, uh, so risk five is, uh, not an open source processor. It's an open instruction set architecture.

**Clifford Wolf:** Okay.

**Clifford Wolf:** So like x86, which is an architecture that has two companies for the most part implemented, a couple of others too. Um, but if, if I would like to implement x86 for, um, for my hobby project, uh, and just release an x86 capable core on GitHub, uh, then Intel would sue me into the ground. Uh, right away.

**Clifford Wolf:** They're good at that too. Yeah.

**Clifford Wolf:** Yeah. Yeah. And, and the same, if I would build, for example, an ARM processor, um, and, uh, so it's not like those big vendors, uh, have forgotten to open source their instructions and architectures. Uh, no, it's, it's like a huge asset for them that, that they have a monopoly, um, on, uh, uh, on these instructions and architectures. At the same time, they're benefiting a lot from a huge open source community of like compiler developers and, and debugger developers and, and whatnot, uh, building software that targets their instructions and architectures. Um, and, um, I always say, uh, in comparison, building a processor is actually very, very simple. The hard part usually is not building the processor. The hard part is building all the software tools around that processor. Um, and I could build my own ARM processor, uh, to reuse that, that universe of tools that is available, um, from a, from a technical point of view, but, but legally I can't do that.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, and that's where risk five comes in. That risk five is an open architecture that everyone can implement.

**Clifford Wolf:** Um, what is the hard part of the software though? Is it just the scale of the getting everyone and like buy-in from everyone? Is that kind of the hard part?

**Clifford Wolf:** Uh, well, yeah, a couple of things. It's the, the, the scale of the project to start with. Uh, but also for example, you build compilers. Uh, it's not only that you need people building compilers. You need also a lot of people using that compiler and looking at the compiler output very, very closely and saying, oh, I'm convinced in this case, the compiler could actually do a better job and, and wanting that enough to create good test cases and then contribute those test cases to the compiler developers. So if I build a, a, a processor just for my own use, and then I retarget a GCC, for example, for this processor, I still don't have this, this huge user base that will provide me with very valuable test cases that helped me optimize my compiler. Uh, so you really need this, this whole ecosystem, um, around stuff. Okay. Um, and, and with risk five, the idea is we only need to do that once. And, and then, then because everyone is using risk five, uh, we can, we can benefit from this work that has been done once and we don't need to redo it whenever we build a new processor because we can't reuse any like large, um, ISA and risk five is supposed to be like this large ISA that everyone is allowed and supposed to actually use.

**Clifford Wolf:** So do you actually, do you actually believe that or no? Like, do you think that if it's only has to be done once or is this going to be like that XKCD comic where it's, we have 14 standards, then it becomes 15 standards.

**Clifford Wolf:** Um, so, um, I, I believe that to a certain degree, um, because, uh, it's not like the 14 other open ISAs out there with the same goal. Um, okay. Okay. There are a couple of open ISAs out there that predate risk five, but they were never meant to be this like universal standard. Um, and they usually, uh, evolved from, from one specific processor implementation. Uh, so usually the life cycle of an ISA is that someone builds a very popular processor and that processor happens to implement a certain ISA. Okay. And now this ISA becomes popular. And then a couple of years later, they build a new processor and they support the old ISA because people are using that ISA already and the compiler is there and so forth. Right. Um, and the ISA used to be really, really optimized in the way they encode stuff, uh, to the original processor. But by the time you have the second processor in the family, um, it's not that optimized anymore, actually. Okay. Because you can't change the ISA to fit the microarchitectural choices that you have made in the, in your next process of generation.

**Clifford Wolf:** Everything else is just bolted on. Right. It's just a, right. And I should also just clarify, you keep saying ISA, that, that is instruction set architecture, right?

**Clifford Wolf:** Yes. That's instruction set architecture. Okay.

**Clifford Wolf:** Okay.

**Clifford Wolf:** Um, and, uh, and with risk five, the idea is we just skipped this initial part that we first optimize the ISA for the microarchitectural choices of one particular microprocessor. Um, and then, uh, maybe it will be hard to write a processor that is as good as a match to the ISA, like this initial one. But the, the successor processors in those other ISAs are usually, uh, a larger mismatch to the ISA than what everything is to risk five because risk five from the very beginning was meant to be a, a universal thing. It did not start as the ISA used in this particular processor. And then it became popular and other people like emulated something that's compatible.

**Clifford Wolf:** Is this, does this have the risk of being the Esperanto of the processor world though? Like Esperanto was meant to, you know, be the ultimate standard of language, but nobody uses it then, you know?

**Clifford Wolf:** Yeah. Uh, um, I, I don't think that nobody's using it because I mean, Western digital is committed to ship a billion, uh, risk five processors two years from now. So.

**Clifford Wolf:** I guess so, but maybe they'll just speak in Esperanto, you know?

**Clifford Wolf:** Yeah. So, um, so I, I, I, in my opinion, risk five will be very successful. I mean, it already is very successful. Okay. Um, the other question is, will we need a different risk five like project 20 years from now? Um, because risk five, in my opinion is also a very good ISA. So it tried to, to learn from all the mistakes that have been made in the last 30 years. Um, but maybe over the course of the next 30 years, we will realize that some other things would be better decisions. Um, and then in 30 years there will be something new. Maybe a risk six, maybe something else.

**Clifford Wolf:** Um, hopefully they, they get a little bit more creative at that point, but yeah.

**Clifford Wolf:** Yeah. Um, but, uh, there is one thing that I'm certain about, uh, and that's whatever will come after risk five will still be an open ISA.

**Clifford Wolf:** Okay.

**Clifford Wolf:** So I think that's the important point. Uh, it's not that is risk five better than everything else or, uh, or not. Um, it's, uh, we are right now at the point where we move from proprietary ISAs where one company owns the exclusive rights to decide who is allowed to implement it and who is not allowed to implement it to open ISAs.

**Clifford Wolf:** Um, and saying I should sell all of my ARM stock.

**Clifford Wolf:** Uh, well, I, I, I can't comment on that. Um, uh, that's okay.

**Clifford Wolf:** I didn't have any anyways.

**Clifford Wolf:** Okay. But, but one, one data point is that the ARM usually was, uh, um, very secretive with their actual code.

**Clifford Wolf:** Uh-huh.

**Clifford Wolf:** So if you wanted to use something like an ARM M0 in your ASIC, you would need to go through long negotiations and probably only at the end of those negotiations, you would be allowed to, to actually see the HDL code and play with it and try to integrate it with your system. Um, and recently ARM has put, uh, the code for the M0 and the M3 on their webpage. You can just. Wait, really? Yes. Yes. Wow. You just click on, I accept the conditions and then you can download, uh, a zip file or whatever it is. Um, and of course it has a license that says you're not allowed to actually use it in an ASIC, but you can start playing around with it, integrating it right away. Um, and, um, um, some ARM people say, yeah, but we have actually been working on that for a long time now to make this a little bit more open and it has nothing to do with RISC-V, but I think it has everything to do with RISC-V.

**Clifford Wolf:** So it's like, uh, writing's on the wall. You better get up, get open or get out kind of thing.

**Clifford Wolf:** Yeah, I think, um, um, if, if you're an ASIC company and, uh, you don't have an existing relationship with, uh, with ARM or any other vendor of processor IP. So this is not specifically about ARM actually. Um, you have to go through, uh, uh, certain negotiations that take up, uh, uh, months at least, um, before you can actually start integrating the core. And usually your ASIC will have a little bit of your own magic sauce plus some kind of, of microcontroller, uh, that, that runs everything.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, and if you have to, uh, to wait another six months before you can go to market, uh, then this is a huge issue.

**Clifford Wolf:** Right. You're dead in the water sometimes, right? I mean, like, yeah, you miss your opportunity.

**Clifford Wolf:** And with, uh, the open source ISAs, there are open source processor cores that you can't just use right away. You just download them from, from GitHub and start experimenting. And maybe you don't end up using exactly that core. Maybe at the same time you start negotiating with some commercial vendors of RISC-V processor cores.

**Clifford Wolf:** Right. Right. Someone who's tested it and does, does a little bit more verification.

**Clifford Wolf:** If, if, if, if you feel more comfortable with that, but you're not dead in the water. You can do all the other development integration work. Right.

**Clifford Wolf:** And you're using the software tools that you mentioned too, right? Yes. That's the idea is that your workflow is out there.

**Clifford Wolf:** So, um, so, and I think that's the, the, the reason for, for, um, for example, to be suddenly so open with their M0 and M3 designs that they want to be in a situation where people can say, oh, I can just download the, uh, the cores. I can start integrating them. I can start testing the system right away while the negotiations are going. Um, right.

**Clifford Wolf:** And I'm sure that arm has, you know, very capable lab techs that can open up any chip, see what looks like an arm, an arm core, and then sick their lawyers on someone who didn't actually pay the licensing fee. Right.

**Clifford Wolf:** Well, um, I don't know if they're actually doing that.

**Clifford Wolf:** Um, I don't either. I'm just guessing, you know, like, but like that, I just mean that like the licensing is a separate issue than, uh, than the code. That's the idea.

**Clifford Wolf:** So, uh, I think if I'm building a chip, um, I'm more concerned about, uh, uh, having someone that I can yell at if something goes wrong, then they're not paying the, the, the, the cent, uh, for, for the arm core.

**Clifford Wolf:** Right. Yep.

**Clifford Wolf:** Um, or whatever it is. I mean, it really depends on what kind of core you have and what kind of volume you have and, uh, and all that kind of stuff.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Yeah. So that's risk five. Okay. And I learned about risk five, um, maybe three years ago. Um, and I was, uh, uh, immediately sold. I mean, uh, this is, I, I, I've, I've built my share, share of processors and then custom compilers to targeted processors and all that kind of stuff. Um, so, uh, yeah, uh, I immediately knew I, I, I want to do something with that. I don't know what yet, but I want to do something with that.

**Clifford Wolf:** Well, you've done, you did something. You just gave a talk about it. What were you talking about it?

**Clifford Wolf:** Uh, I, I, I, I built a processor. Okay. So it's called Pico RV32. Um, it's in an odd design corner a little bit, uh, because it's, um, um, it's, it's a small processor. It's not really the smallest processor you could ever build, but it's, it's a relatively small processor. So in Xilinx seven series FPGA architectures, it's about 750 lookup tables large. Um, and, uh, it's optimized for very, very high clock speeds, but not for performance. Um, so it has actually pretty poor performance. It takes a couple of cycles for each instruction. Um, but because it runs in a very, very high speed clock domain, you can run it in the same clock domain like your, as your actual processing course.

**Clifford Wolf:** Oh, so no translation of clock domains.

**Clifford Wolf:** You don't need to cross clock domains to go from your, uh, work core to your control processor. And that simplifies the fact designs a lot.

**Clifford Wolf:** Right. And you don't have to wait on stuff either, right? You're just, you just pass it through and it's fine.

**Clifford Wolf:** But I mean, clock, clock domain crossing is always a, a, a, a very complicated thing where I can, uh, get a lot of stuff wrong and you would like to avoid it at any cost if possible. Yeah. Um, then usually when, when you cross clock domains, you have to figure out how to convert something in like a, a stream of data. Um, so, so some things need to have like, uh, additional abstractions and translation layers. Uh, so that you can actually get your data from one clock domain to the other. Right. Um, and, and the idea was that I would like, wanted to build a risk five processor that is well suited to be a control processor that avoids all this kind of, of issues. Um, and if you have to cross clock domains, for example, and you have a more complex, um, application, uh, that you actually have like an address data bus, uh, with arbitration and all kinds of things. Um, uh, it's not uncommon that actually this integration to this bus system with crossing clock domains and everything is larger than my processor would be.

**Clifford Wolf:** Um, so, uh, the, the crossing logic you're saying is, is it? Yes. Yes. Okay. So it's, it's, uh, so with integration. This thing is so small, you just sprinkle it in anywhere. That's kind of the idea. Yes. Yes. Yes.

**Clifford Wolf:** That, that, that's the whole idea. Um, and, uh, yeah. Uh, interestingly, a lot of people are using it, uh, for, for different applications. A couple of people have actually taped it out on ASICs, uh, as well. Um, one, one very big, uh, company that, that builds like TV sets and stuff like that, uh, uh, told me that they are using it in one of their ASICs. Cool. Um, um, so I don't know for what exactly, but, uh, um, yeah, but, but apparently.

**Clifford Wolf:** Maybe you'll get a sticker on the outside at some point built with a Pico RV 32.

**Clifford Wolf:** Yeah, probably not. But, uh, uh, you don't get like the Intel inside.

**Clifford Wolf:** You can't make your, you can't make a sticker like that. Come on.

**Clifford Wolf:** Yeah. I mean, I could make a sticker, but I think they are not going to make it put it on their devices.

**Clifford Wolf:** Right. Um, that's what's crazy too, is that like, yeah, with the licensing days, like you had to know it was there. Now it could just be in anything. Right.

**Clifford Wolf:** Yeah. Yeah. And I mean, that's a big problem with all kinds of open source projects that, uh, that, that usually have very, very poor data on who is using your stuff and what for. Um, usually have a little bit better data. If your documentation is very poor, uh, because then people will, will ask the questions. Um, and usually you can, you have a very, very good idea from the kinds of questions people ask, uh, about how deep they're in and, and if they're actually using it or just thinking about using it.

**Clifford Wolf:** Right. Um, well, you got 71 people watching your, your GitHub repo. So you could probably say there's at least 71 people interested and 368 started. So yeah. Yeah. At least 368 read it. So there's like your, that's like your floor, right? Yeah. Yeah. Right.

**Clifford Wolf:** Um, but actually I'm, I'm more interested in, in like the, the one really auto interesting users than like the, the number of people using it. Um, and, uh, so, so one, one thing that I'm very proud of is that the, uh, Berkeley Lawrence national laboratory, uh, that have a synchrotron, uh, they are using Pico Arbitrity too in their interlocks. Uh, I've learned recently, which makes it the second particle accelerator to use, uh, some kind of code that I've written. Um, well, there you go.

**Clifford Wolf:** Do it a couple more times and I think they name a particle after you eventually.

**Clifford Wolf:** Yeah, I don't think so. Um, but, uh, so, so LHC is the first one. Uh, they were using, yeah, yeah. They are using the library. I wrote lip, lip X SVF. We didn't even talk about that project yet. Uh, uh, it's a library for programs. Okay. And, uh, apparently the FPJs on the accelerator ring for the control logic for all those magnets, um, is programmed with my software.

**Clifford Wolf:** That is crazy. Did you get a tour? Did you get to go there and like tour around and stuff or no?

**Clifford Wolf:** Uh, so, so I've been there once, uh, for a, for a conference. Uh, but, uh, this was, uh, a few years after, uh, they used that. So I'm not even sure if the people who implemented initially are still there. Uh, um, but they, uh, they essentially told me that, that this is going to be there for at least the next 20 years. Um, because it's part of a, uh, of the reference implementation of a field bus that they actually standardized. Oh, cool. Um, yeah. Yeah. So, uh,

**Clifford Wolf:** I love like, like things like, I mean, obviously I love the, the, the, the LHC, right? Those are large, large Hadron Collider. That's the, the, the right thing, right? Um, the, uh, but like, it's like, it's the academics and the scientists actually doing these really huge things. Whereas usually, you know, that's usually smaller lab base, you know, resource constrained, funding constrained. And yet LHC is just like huge stuff. And so, and there's using open source, which is extra cool. Obviously, you know, with, with, uh, CERN using KiCad as well. I'm a big fan of that. Yeah.

**Clifford Wolf:** Yeah. They're also pushing open source a lot.

**Clifford Wolf:** Exactly. That's great. That's great. Yeah.

**Clifford Wolf:** Yeah. Uh, it's, it's funny because, uh, so, uh, that was when, when, when they, uh, used it initially the first, uh, like, like revision of LHC. Uh, uh, was back at the time where, uh, some people had this theories, uh, the large hadron collider will create a black hole. Right, right, right.

**Clifford Wolf:** You're talking about the website has, has the large hadron collider ruined the, or ruined the earth layout.com or something like that.

**Clifford Wolf:** Uh, no, I don't know that.

**Clifford Wolf:** Oh, it's just a website that just says no, you know? Okay. Yeah. Sure.

**Clifford Wolf:** Um, yeah, I mean, it's, it's, uh, uh, yeah, let's, I'm, I'm not a physicist, but, uh, but, but, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, you know, when they always say, yeah, that's not going to happen because the black hole will decay so quickly or evaporate so quickly. Uh, uh, actually they should completely change the language and they should say the black hole will explode so quickly, uh, because the, the, the, the radiation given off by a black hole is getting, uh, uh, larger and larger when the black hole, uh, uh, gets, gets smaller and smaller and has less and less mass. Right. Um, and then you have like a, a, a, yeah, it's, it's, it's, it's better when it's a,

**Clifford Wolf:** when it, when it goes the opposite direction, right?

**Clifford Wolf:** And it's, it's, uh, um, and, and I think that this language of saying, oh, that cannot happen because it decays so slowly or it evaporates so slowly, uh, that language has, has like contributed to this misunderstanding that. Yeah. But what if it's not, uh, yeah, whatever. So back then, uh, I was always making, making fun that, uh, oh, if the, the whole world is swallowed by a black hole, it will be in part my fault or something like that. Uh, so it was like, ha ha, we can all die. Ha ha. Uh, but now that I know that they use, uh, uh, the, uh, my processor at the interlocks at this, uh, um, at the Synchrotron, I'm actually pretty worried. So, uh, because, because, uh,

**Clifford Wolf:** You're like the last line of defense, huh?

**Clifford Wolf:** Well, yeah, man, man, uh, for some crazy reason, it's like, ha ha, we all could die. Uh, but, but one person could die. It's not funny anymore. Right. Exactly. Well, if we're all gone, like who cares, right?

**Clifford Wolf:** Nobody actually, yeah.

**Clifford Wolf:** Yeah. So, um. I'm sure it'll be fine. Yeah. But I asked them, uh, uh, why, why are you using my, my processor? Wouldn't you use something like, uh, industrial strength, uh, thing? Uh, uh, uh, and, and they said, yeah, that's exactly why we don't use something because it's important. And then we talked to the commercial vendors. They just tell us, yeah, our processor is extremely well tested. Um, and, and, and, and, and super quality and whatever, but they don't tell us how they came to that conclusion.

**Clifford Wolf:** That's right. Um, these are scientists you're talking to, right?

**Clifford Wolf:** And, and it's, it's like, it's one salesperson who has no idea about any of the technical aspects.

**Clifford Wolf:** Right.

**Clifford Wolf:** He's just guessing what he should tell us in order to, uh, uh, uh, to get the sale. Yep. Um, but with PicoRV32, all the tests I've done are out there in the open.

**Clifford Wolf:** Yep.

**Clifford Wolf:** Um, and, uh, I'm, I wrote the framework that's used from a formal verification of RISC-V processors, which is RISC-V formal. And I, I mean, PicoRV2 is, is probably the best formally verified processor out there in the RISC-V universe at the moment. Really? Uh, so they said, they looked at all this verification because it's all there. And that was what, what convinced them that they actually would like to use my processor and, and not something from, from a big vendor because the big vendor would not, would not show them how they can be sure that it's correct.

**Clifford Wolf:** Right. Right. Openness is a sales tool. You're saying pretty much. Yeah. Without, without any sales.

**Clifford Wolf:** Yeah. Without any sales. But, but I mean, uh, uh, uh, yeah, the, the, the, the internet geek points I get for that, uh, uh, uh, much more valuable anyway.

**Clifford Wolf:** Right. Well, and it, it seems like, I mean, it is like an academic approach to it, right? I mean, like the showing your work, showing the show, you know, like, uh, replicating papers, that kind of idea. Right. Like, um, yeah.

**Clifford Wolf:** Yeah. Yeah. Yeah. And I mean, um, also, um, I mean, I might be a little bit worried that, that, that my process is used for, for, for critical stuff like that. Uh, but actually I'm not, I'm not really scared or anything because I know what kind of verification procedure I put in there. Um, and, uh, and I think that's also a difference when you, when you, when you have like the, the commercial, uh, vendors, uh, you can't invite the guy who actually, uh, built the IP.

**Clifford Wolf:** Right.

**Clifford Wolf:** And tell them life is depending on your IP and then look at the expression in his face. Right. Right. Right.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, but, but you can do that with open source tools. So yeah.

**Clifford Wolf:** What is our design requirement? Well, we want to scare the crap out of someone. Is that, is that a possible design requirement? Right. So I had a question about the, um, so you'd said the risk. So you said risk five is an open instruction set architecture, but it's not open source. Now the Pico RV is open source is an open source processor.

**Clifford Wolf:** Well, the, uh, the risk five specification actually is, uh, some kind of open source. Okay. Uh, but the thing is, uh, the, that risk five, there is risk five is no software, no, right. There's no varilog involved, right? It's just, yeah. There is nothing that you would make open source. Okay. Uh, actually there is a late tech code that generates the, the document. And that late tech code is under some kind of open source license.

**Clifford Wolf:** Yeah. That doesn't count.

**Clifford Wolf:** Uh, uh, yeah, but there is no, no other thing that like is risk five because risk five is, is this English language document, uh, that defines, uh, how the ISA works and, uh, and soon will be also a formal specification, uh, because with, with, with English documents, there are always like, uh, certain cases where you realize, oh, uh, it's not actually clear if it should be this or that way.

**Clifford Wolf:** Right. Right. Yeah.

**Clifford Wolf:** Um, yeah. But the idea is it's this specification. It's the, it's the instructions and architecture is not the processor and the concrete implementations. Some of them are open source and some of them are not. And it's very, very important that this is okay. So, so nobody in the risk five universe is like everything must be open source. Right.

**Clifford Wolf:** There's no stallman stallmans among the bunch. Yeah.

**Clifford Wolf:** Um, um, but at the same time, I think it's very important that there are some open source risk five implementations.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Uh, because this enables so many, uh, um, applications that, uh, would not be possible otherwise. Yeah. Um, and, and then there is still enough, uh, space for, uh, for commercial entities to say, oh, but we build a risk five processor that, uh, performs particularly well, uh, or is highly optimized for, for seven nanometers, uh, or whatever. Right. Right. Right.

**Clifford Wolf:** Right. Right.

**Clifford Wolf:** Um, right.

**Clifford Wolf:** And that's what, and then, and those, and those commercial applications like you're talking about, that's effectively the someone to yell at. Right. So I'm paying that licensing fee. I need to talk to someone right now because at the seven nanometer node is not working as expected and go fix this.

**Clifford Wolf:** And so a lot of people are talking about risk five and saying things like, yeah, but does it perform, uh, as well as, as, as x86, for example. Um, and that's of course a pretty nonsensical question.

**Clifford Wolf:** Right.

**Clifford Wolf:** Uh, because they implicitly compare different implementations.

**Clifford Wolf:** Right.

**Clifford Wolf:** Uh, they say is an Intel processor as quick as a risk five processor. And the answer, it depends on the risk five processor. Right. There are some risk five processors out there and more that are under development right now that are optimized for, for high performance, uh, single threat, uh, uh, application, um, uh, or a few threats application. So not GPU stuff. Um, the other implementations that are very high optimized for, for exactly that. For like more GPU like, uh, applications. Um, and, and you have to look at the individual processors. Uh, and there is this, this like implicit assumption, um, that, uh, instruction sets can be inherently better or worse for performance. And of course, when you look at extreme examples, then this is the case. Um, but really if a, a, a well-designed instructions and architecture would be necessary for good performance, then Intel could not compete. Their instructions and architecture is, is 30 years old. Uh, and, and, and, uh, came from, from a, a processor that was originally designed to be a, a, a, a control processor and peripherals.

**Clifford Wolf:** Um, so, um, the early, like the early Intel days, is that the idea is like the.

**Clifford Wolf:** Well, the original 8080 was like meant for, for like being a control processor and printer units and stuff like that. Um, and then, uh, uh, IBM came along and they realized they just got too late for the PC revolution. Um, and so they started this project to build a PC within a year. Um, and they wanted to use, uh, the, uh, um, um, 65, uh, a thousand series. Um, but couldn't because Motorola could not, uh, um, guarantee them the, the numbers and Motorola was not, um, did not want to give licenses to other fabs to, uh, to produce replacements. And then they went to Intel because they had something that was easy enough to integrate and said, we want to use your processor, but Intel didn't have the capacities at the time either. So Intel had to give a license to AMD to build x86, uh, 8080 processes at the time. Um, uh, so that IBM would have a guarantee that they could always buy the chips in the numbers they need. Um, yeah, that, that's how, how the instruction set became like the PC instruction set.

**Clifford Wolf:** It's so like the 80s, the x86 architecture is like dependent on like 1989. 1989 Christmas time. Is that kind of the idea?

**Clifford Wolf:** Yeah. Yeah. And then, uh, and then, uh, consumer demand driving. Yeah. Yeah. I think it was a little bit earlier than that. Uh, but, but yeah, some, some, some time in the 80s. Wow. Um, that's crazy. Right.

**Clifford Wolf:** So now we're finally fixing this in 2018. Uh, yeah. Right.

**Clifford Wolf:** But my point is not, oh, Intel is such a, uh, such a horrible instruction set. I mean, it is using a horrible instructions of architecture. Uh, but the point is, despite the fact that they are using this horrible instruction architect set architectures, they can still build high performance processes. Right.

**Clifford Wolf:** Right. Right.

**Clifford Wolf:** Um, so I think the whole discussion about, oh, but can risk five be as performance as as x86 is a red herring. Uh, uh, because x86 is not fast because they have a great instructions of architecture. Yeah. They are fast because they build good processors.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, and if they would build, uh, a risk five processors, uh, arguably they could build even better ones, uh, because, uh, um, a, a lot of the area in an x86 processor is actually dedicated to things like decoding instructions. Um, and, uh, and, uh, and that's one of the reasons why, why you have a, a more risk approach in, in embedded devices. So most stuff there is arm, but even though the R in arm is risk, uh, arm wasn't risk for yeah, quite some time now.

**Clifford Wolf:** Right, right, right, right. Okay.

**Clifford Wolf:** But, but it's still, it's, it's still a cleaner instruction set architecture than, than x86. Um, yeah. So I think, I think all those discussions are pretty much red herrings and at risk five is, uh, certainly a, a good enough well-designed architecture that there is nothing in there that would prevent you from building high performance processors. Um, but, uh, uh, beyond that, the only thing that really makes sense is compare implementations with implementations, uh, when you're interested in, in, in performance. Okay. Yeah.

**Clifford Wolf:** So the last thing that I want to ask about was the, uh, I mean, probably, I mean, it sounds like we could talk all day and we've already been going for two hours.

**Clifford Wolf:** Oh God.

**Clifford Wolf:** That's okay. Um, but you were talking about formal verification. So is that tied to all this stuff or is that tied to, to you building it around the, the risk five or is it, is that stuff we have already talked about?

**Clifford Wolf:** Yeah. So the formal verification is a very, very big topic for me. And, and actually, um, so I started the company, uh, uh, a few months ago. Uh, that's why I'm not working in LIDAR anymore. Um, and, and we are, uh, um, providing, uh, support and services, um, mostly around our own formal verification tools. So all the open source tools, uh, that the marketer in me says, you should probably say

**Clifford Wolf:** your company name now.

**Clifford Wolf:** Yes. Uh, symbiotic EDA. So you said at the beginning, I know that. Symbiotic EDA all one word. Symbiotic EDA.com is, uh, like more or less a placeholder for, for our webpage. Cool. Uh, we are right now focusing on other stuff, uh, than, than, than, than building the, the world's greatest, uh, company webpage. Right.

**Clifford Wolf:** Um, that's when you hire the management people. Come on.

**Clifford Wolf:** Yeah. So, so the thing with formal verification is, um, um, maybe I should, should really quickly describe what formal verification actually is. Yeah.

**Clifford Wolf:** That'd be great actually.

**Clifford Wolf:** Uh, yeah. So when you have, uh, a, a digital design, um, so that's the kind of formal verification that I do, uh, formal verification is used in many, many fields and has many, many meanings. Uh, but I'm doing hardware model checking. So I have a hardware design and I have a list of, of safety, safety properties that essentially say, uh, the design will never be in a state where, where this or this is the case. Um, um, so I don't know, the design will never be in a state where, uh, you have reverse trust enabled and not contact to the ground with your airplane. Uh, that would be, uh, uh, that would be, for example, a desirable thing in your control system. Um, and, uh, then you do mathematical proofs that show that actually your design can never be in that state. Um, so when you do verification via simulation, which is what most people do, um, then you just try a limited set of inputs and maybe your limited set may be hundreds or thousands or millions of inputs. Maybe you, uh, you are using fuzzing or other similar techniques, but still you're using a, a, a relatively small finite set of, of, of inputs. And by relatively small, I mean, compared to the complete set of all possible inputs your design could see. I mean, if your design has a 32 bit input and you run it for a hundred cycles, uh, then we have, uh, two to the, uh, what is it? 3,200, uh, uh, different inputs that, uh, design could have seen and you could try them out individually, but, uh, the universe will die a heat death before you will come nowhere near. Well, the heat death is actually very cold, but, uh, it's right.

**Clifford Wolf:** Heat death meaning that all, everything's spread out enough, right? Yeah.

**Clifford Wolf:** Heat death meaning everything on the same temperature. Yeah. Right.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Um, yeah. So, uh, so that's not an option. Um, but there are tools, uh, that, uh, can do something equivalent without actually going through the, the work of having to try each and every possible input individually. Um, and then that tool says, yes, you are good. Then this would be equivalent to running this, this simulation that you could not really run in, in reality. Right. Um, and this kind of stuff can be used for so many different things. Um, so I use, uh, this a lot to actually verify my own synthesis tools. Uh-huh. So I can use formal methods to, uh, to show for a, uh, particular transformation that the circuit after and before the transformation are still equivalent. Um, because that's hopefully what the transformation does. It makes the design better without actually changing the design's behavior. Um, and, um,

**Clifford Wolf:** And that's like collapsing logic, that kind of thing. Like, like, like what would that be like a DeMorgan's like in a very, very, very simple case, like of translation of logic?

**Clifford Wolf:** Um, um, um, it, it's, it's not, there are different ways how you can do that. Uh-huh.

**Clifford Wolf:** And there are more symbolic ways, but most of it is actually sub-solving. Um, which essentially, um, and, and again, oversimplifying a lot. Um. This is the amp hour.

**Clifford Wolf:** Come on, man.

**Clifford Wolf:** Trying, trying all the different combinations and you say, okay, let's start with all the combinations where the first bit is zero. Uh-huh. Um, and then maybe you can figure out that when the first bit is zero, you can't even get to one of your, uh, bad states anyways. Uh-huh.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Without having to try all the other combinations for all the other bits. Right. And then you're already done with the first bit. Yep. Um, um, and, and the tools do this using techniques like conflict learning. Um, that they, um, try to, to prune the search tree as early as possible. Huh. And yes, this, this is now very, very simplified. Um, um, but that's more or less what it is. Okay. There are different methods how you can do that in the, in the, in the nineties and also in the eighties. Binary decision diagrams are very popular. Uh-huh. But they have the disadvantage that for many real world designs, you need to generate a, a data structure that's exponentially large. Yeah. And you can't do that.

**Clifford Wolf:** Right. Um, and you run out of paper to print it on, right? Yeah. Right. Right. All that stuff.

**Clifford Wolf:** Um, and then there are sub-based techniques, which are more the things that are popular now. Um, and, uh, they, they, they don't need to, to generate exponentially large data structures. Um, but they are not guaranteed to always find like simplifications. Um, so they are potentially running for exponentially long, which is also bad. Uh, so there's the saying that with BDDs, you run out of, uh, memory and with sub, you run out of time. Uh, um, but, but overall sub-based, uh, techniques have proven to be the better choice. Um, and, and most of the tools that I wrote are using sub-based techniques or things based on sub-based techniques. Um, but the whole idea of building formal verification tools, uh, in part is to actually, uh, hide all these details from the user. Um, and, and there is this, this meme that in order to do stuff like formal verification, you need to be like a math PhD. Um, and for some techniques you have to be, uh, but for others, you don't. Uh, and this, this kind of techniques, the automatic techniques, this is the things where, where my tools work, where you essentially just say, this is the thing that I would like to prove. And in most cases, the tool will reply in reasonable time and either say, yes, you are right. This is a property of your circuit, or it will say, no, you're wrong. And here is a simulation trace that demonstrates that you are wrong.

**Clifford Wolf:** Right. Um, so then you could take that and then actually go and dive into the details of it.

**Clifford Wolf:** And that's why it's also very equivalent to like running all the possible traces because it will show you like the one trace, uh, that, uh, uh, that actually violates your properties. Um, but it will using magic, uh, uh, uh, find a way to, to happen to try this trace much, much earlier than almost all the other combinations of inputs.

**Clifford Wolf:** Huh? Interesting. Interesting. So, uh, so what, what, what kind of clients then would be looking for this in general? I mean, like, is this like, these are ASIC vendors that are looking to verify some special design? Is that the idea? Yeah.

**Clifford Wolf:** So, uh, uh, um, historically the, uh, you use formal methods for things where you absolutely need them. They're like, uh, standards that require you to do that. Um, and you can use my tools for, for that as well. Probably, uh, there might be issues with certification or whatever. Um, but, um, what we are actually trying to do is making this kind of techniques, uh, more popular, um, because, um, say for example, you build a processing system, um, and you, you usually go through a phase where you develop it and you find a lot of bugs there. Um, and then the developers are done and then they send it to the verification department and they do a whole range of different tests. And one of the things is that they will implement your processor design in an FPGA and just run it for weeks. Okay. Um, and maybe you realize, oh, if you run this particular problem, uh, this particular program for two weeks, then suddenly the processor will freeze.

**Clifford Wolf:** Okay.

**Clifford Wolf:** And then they will send that to the, back to the developers and say, if I run this program on this FPGA implementation for two weeks, that it will fail. Sometimes it might need three weeks. Sometimes it may crash after one week, but two weeks seems to be the average. Have fun debugging this.

**Clifford Wolf:** Yeah. Right. That's, that's basically saying there's probably a problem that gives no info. Right.

**Clifford Wolf:** Um, uh, but if, uh, if formal verification finds the same bug, it will find the shortest trace that demonstrates the bug.

**Clifford Wolf:** So don't you still need to know what the bug is though, or no?

**Clifford Wolf:** Um, uh, well, it depends. Maybe, maybe you already have properties that, uh, that describe what the behavior of a processor should be. Uh-huh. And, um, and, and then, and freezing usually is, is one of those properties you would have. Usually you would have some kind of bounded lifeness where you say, uh, if I guarantee my memory to reply within that many cycles, uh, then, uh, my processor must retire a new instruction, at least every so-and-so many cycles. Um, so, and, and maybe, maybe it's 20 cycles for your, uh, for your thing. And, and maybe you put that into your formal tool and the formal tool will return with a trace of 50 cycles where the processor is doing nothing in the last 20 cycles.

**Clifford Wolf:** Huh. Okay.

**Clifford Wolf:** And then you know, okay, something is going wrong here. My processor just froze. Okay. And it's, it's a simulation trace. So you see all the internal signals. You know exactly what, what, what is happening. Right. Uh, so this is something that you can actually, uh, uh, uh, troubleshoot very, very quickly. Right. Because it's a very small trace. Moreover, this is something that you can run very, very early in your design process. So it's not like you're sending a design back to an engineer who worked on that one and a half years ago.

**Clifford Wolf:** Right. Right.

**Clifford Wolf:** You, you're telling the engineer the change you did yesterday broke the design.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** And please fix it now. Interesting. And this completely changes the economics. Yeah. Of, of what, what cost actually is produced by, by having had this bug in, in the design in the first place.

**Clifford Wolf:** Right.

**Clifford Wolf:** Um, and.

**Clifford Wolf:** So it's almost like applying unit testing to processor design because you can run these faster test cycles and iterate faster.

**Clifford Wolf:** Yes. The only difference is that with unit tests, you still only test one particular input, but here you test one particular property.

**Clifford Wolf:** Okay.

**Clifford Wolf:** And, and the, the properties can in part be very, very complex. Okay. Um, and yeah, so this is the, the kind of stuff that we would like to do with, with our company to, uh, get more people to use formal methods. Um, um, also FPGA people, uh, right now many people in the FPGA sector say, well, we don't. We don't need formal methods because a bug is not as expensive to us. We can just update the bit stream. Yeah. But even if you have to update the bit stream first, you have to, to troubleshoot the thing that might only happen at the customer, uh, and not in your test lab. Uh, you have to figure out what the problem is. Uh, um, you might have customers who are now unhappy because they lost business. They had downtime of something, uh, because of your bug. Um, so if, uh, so, so maybe for those kinds of, uh, of, of, uh, design, uh, uh, companies, um, it's not really an economic, uh, uh, viable decision to make complete proofs for their designs. Sure. Um, but if there are some aspects of it that they can prove where it's easy to write properties, uh, they would give away a lot of, of, of potential of, of finding bugs early, um, for no good reason. In my opinion, other than, uh, that they don't have the expertise not, uh, yet how to use this kind of tools. Um, because the tools that are, uh, traditionally available, uh, commercially in this sector, they target only at like, uh, military satellites or, uh, what not.

**Clifford Wolf:** Things that can't fail because you can't, you can't reboot them. Yes.

**Clifford Wolf:** Uh, and, and even things that can fail, uh, uh, very often they're not formally verified. Only when there is like a legal requirement to actually do formal verification.

**Clifford Wolf:** Interesting.

**Clifford Wolf:** Um, and then in those settings, this is like seen as a, uh, uh, as a cost for the company.

**Clifford Wolf:** Right.

**Clifford Wolf:** Uh, many companies do formal verification then, but still believe, well, uh, uh, it would be cheaper for us to just take the risk of the thing failing. Right. Then going through the additional, uh, large project of doing the formal verification. Um, but because it's not so feasible for society, if that thing fails, there is a law that requires them to do the verification thing. Right. Um, but, uh, yeah, but, but we, we, we don't even want to, to, to be in that sector. We want to be in, in the other sectors. Right.

**Clifford Wolf:** You're just saying that this is a cost savings. This is a useful tool. Let's make it more accessible.

**Clifford Wolf:** And in, in a way, when it comes to formal verification, I'm a little bit, uh, reminded of like the, the home computer scene in the eighties. Um, and I mean, this is something that I know from, from, from stories. I'm not, uh, I was too young in the eighties.

**Clifford Wolf:** Me too.

**Clifford Wolf:** Um, um, but, uh, um, many, many people back then, uh, they're just programming stuff in assembler and they did not have access to compilers. They did know that compilers exists and that people who work like with mainframes and stuff like that, that they use compilers for their work. Um, but nobody there really felt that they are missing out on something because they were not using compilers on their own. Right. Uh, and in part this is because they never had a chance to actually work with compilers. They, they just use some, some, some stories, uh, about, uh, what compilers do and that they need these huge machines to run on and all that kind of stuff. Um, right.

**Clifford Wolf:** Until you have access to that higher level of abstraction, you don't know what's actually possible because you don't have the workflow. Yes. Optimized yet.

**Clifford Wolf:** And also if there is some kind of technology that might help you, but you cannot really access it right away. Right. Uh, I think it's healthier for you to believe that you don't need it anyways.

**Clifford Wolf:** Right. Well, it's, it's like denial in a nutshell, right?

**Clifford Wolf:** Yeah. And, and I think, uh, uh, and I think that that's a big aspect here as well that people say, oh, those tools, uh, can, can easily cost, uh, hundreds of thousands or even millions of dollars. Right. Uh, so obviously we can't afford them. Uh, so let's just assume we don't need them anyways. It will at least make us feel better and it will not change anything that we can or cannot do. Um, but now we have open source formal verification tools. So the, the Yosis universe, if you like, has a lot of formal tools and I use them in many of my projects.

**Clifford Wolf:** So, and so are those, those are in the Yosis tool or are they external and have a different name?

**Clifford Wolf:** Um, well, some of them are really in the Yosis tool. Uh, there is a separate, uh, package called Symbiosis. Um, that's, uh, essentially that is a front end for Yosis and other open source tools, uh, solvers, uh, mostly, uh, that can work with Yosis. Um, so Yosis is taking your HDL, so Symbiosis is using Yosis to convert your HDL design into a format that those, uh, constraint solvers can understand. Then it's using those constraint solvers to actually solve the, the problem. But the output of that, uh, the thing will say, um, assertion 25 or property 25 failed. Uh, then, uh, uh, signal 28 is high in, in cycle 12. I don't know. Um, but that's not good to you because you don't know what, what, what, what signal 28 is. And, and assertion 15 or whatever that, or whatever I said. Um, so, uh, the more complicated part is actually taking the constraint solver output and converting it back into something that the design engineer will understand and can work with, like a VCD trace and all that kind of stuff.

**Clifford Wolf:** Got it. Okay. Okay. Yeah. I just found a file or a presentation of yours that is, shows a nice diagram. It's got like a, uh, Yosis SMT lib2 code and then showing SMT BMC. Is that like an in-between layer?

**Clifford Wolf:** Um, yeah. So, so, um, Yosis SMT BMC is a driver program that interfaces between, uh, a format Yosis can generate and the format SMT solvers can, uh, can understand. Hmm. And SMT solvers is one large class of constraint solvers. Um, so, so this one thing can actually interface to, to a bunch of different solvers.

**Clifford Wolf:** Okay. This is a lot of stuff. Um, do you sleep? Do you, uh, are you?

**Clifford Wolf:** Um, yeah, actually I, I, I, I think I sleep a lot. Um, great. Usually I wake up with, with, uh, with a lot of ideas that I don't have time to implement. Yeah. Um, yeah. Um, most of this is not actually as much work as you, as you might think.

**Clifford Wolf:** Um, I mean, it's just tough to take in all at once. I think I, I think it's one of the, yeah, I mean, I mean, we've, we've now gone through

**Clifford Wolf:** like 15 years of, of my work. Right. Right. Uh, and we've, I mean, we've, we've, we've, we've skipped over a couple of things, but, um, um, but I think what's, uh, what's a theme that that's kind of reoccurring, uh, with, with my project is that it's so important to, uh, to take your time to think about stuff. Yeah. Um, and, and quite often, especially in a, like commercial setting, uh, you have external requirements that say, well, this must be done by next week.

**Clifford Wolf:** Right. Uh, so you need. If your manager set a, a arbitrary deadline, we must meet it or else.

**Clifford Wolf:** Um, so you have to start working on it and implementing it right now. Um, and it might take you the entire week, but maybe if you would have had time to think about it for a month, not like full time sitting there eight hours a day thinking about it. Yeah.

**Clifford Wolf:** You're talking about like shower thoughts, right? Like you're sitting in the shower and like, oh crap, what if I did this? Right.

**Clifford Wolf:** Yeah. And, and, and a month later you might implement the same thing and just within a day.

**Clifford Wolf:** I see.

**Clifford Wolf:** Because, because now you have detangled everything and you know how the individual components should, should work together. Um, and more when you build frameworks, maybe the thing that you're building one day will be much easier to work with in the future than the thing you would have built in two weeks.

**Clifford Wolf:** Right.

**Clifford Wolf:** Yep. Um, so, so that's all snowballing in, in a way.

**Clifford Wolf:** Right. Um, it's like technical debt, right? That's the idea is like, yeah. Yeah. You make some crap thing. You gotta support it for the rest of your life. Right.

**Clifford Wolf:** Uh, uh, so, um, um, and because of that, there are a lot of things going on. Uh, but, but when you look actually at the like amount of hours going into actually sitting in front of a terminal window and typing the code, uh, that's, that's really easy. The, the, the, the hard part is getting to the point where I say, oh, if I do it that way, then it's really easy. And then I just do the things where I've realized how, how it can be done easily. And you just have to have some, some, some faith that, uh, most of the problems, uh, actually have a, uh, a, a relatively easy solution. If you just take your time thinking about it. Um, not, not saying that this is necessarily true for, for everything. So there are sure. So within the Yosis universe, a couple of things where I just said, okay, I need to build this huge component. Um, and, and for some reason I'm, I'm convinced it actually has to be that big and no amount of, of meditating over it will, will make it any better. Right. Right. Then you just have, have to do it and lock yourself in a dark room for, for two weeks. And, um, um, yeah, but, uh, um, but I think a lot of people sound much, much, uh, a lot of things I do sound much, much larger to a lot of people than they actually are, uh, because they think about the problem and they have a solution in their head immediately, but not the solution that you come up with when you think about it for like, uh, a month or two.

**Clifford Wolf:** Right. Right.

**Clifford Wolf:** Um, and if they would think about it for a month or two, then they would also say, oh, actually you just have to do it that way. And, and, uh, really easy and quick to do. Um, yeah. So formal verification, I'm using that a lot in, in all my projects. So, um, the project ice storm stuff, for example, that I said I generated, um, designs and then generated bit streams and converted bit streams back into Verilog. Um, I was using formal verification there to prove that the generated extracted Verilog is still, uh, formally equivalent to the thing I put in, um, initially. Um,

**Clifford Wolf:** So that probably saves a lot of time as well, right? Yeah. Like over, you have fewer total test cases run, but they hit all of the important points.

**Clifford Wolf:** I have a very similar project called, uh, uh, Flock hammer that generates, uh, uh, Verilog code runs it through, uh, various tools and then uses formal verification to figure out if the thing is still equivalent to the input. And I found a lot of bugs in, in different tools with that. So open source tools and commercial tools alike. Uh, the main difference is the open source tools usually fix it within a couple of days. Uh, and, uh, for, I mean, for Vivado, I have bugs open that I've filed like three years ago. Um, and they're really, they should be really, really easy to fix, but apparently nobody.

**Clifford Wolf:** Well, you should just buy more, buy more FPGAs and they'll, they'll fix them.

**Clifford Wolf:** Yeah. I don't know. I did actually talk to, uh, to people by like, um, huge amounts of FPGAs and they pretty much say they have a very similar, um, experience. Um, so, so the, so, so you find some kind of bug, then you reduce it to a very, very simple test case and then you send it to the vendor and then the vendor will come back with a back around and say, well, just, just write this line like that. Right. Right. And then you're like, yeah, but, uh, I spent a lot of time creating a simple test case to demonstrate the bug. Right. Um, it was really hard to preserve the, the, the, the, the incorrect behavior while shrinking it down to this thing. Um, because originally, of course I had this huge thing in Simulink and then I run it through this MATLAB module that allows me to generate very low code from Simulink. Oh yeah. I've done that. And, and I spent like, uh, two months of my life finding this bug. And now you're telling me I should just make small modifications to the generated very low code until it stops misbehaving. Right. Until it stops giving that error actually. Yeah. Yeah. Not even necessarily misbehaving, uh, in, in, in most cases, those, those bugs are really like, uh, the tool says everything is right, but it has, uh, incorrect behavior, which is horrible if you're doing DSP work, because with DSP, it's usually, um, any mistake, no matter how small you just get garbage out.

**Clifford Wolf:** Yep.

**Clifford Wolf:** It's not like you can actually look at the output and say, oh, it's because it like swapped pair of the weights on my steps. Right. Right. Right. And it's nobody looks at those numbers and comes to that conclusion. Uh, um, so yeah, that's, uh, that's a problem. Uh, and I think it will become a, a larger problem because more and more of the HDL code we actually implement is going to be generated by other tools.

**Clifford Wolf:** Yeah. I've done that flow before. That was one of my, it was like the worst time for me too. Cause it was like, it was a co-op. I was in college. I didn't really know what I was doing. I was just kind of like floundering around. And so I try all these things in MATLAB. It would generate the code. Didn't know what that looked like. That would get pushed into FPGA. Didn't know what that was doing. And at the end, it was like an LED was supposed to light up. It was like, it's like a true black box that I, that it took six hours to iterate on. Yeah, it was terrible.

**Clifford Wolf:** Yeah. Um, so formal verification can be used in, in a lot of places. Um, I sometimes use formal methods just because I'm too lazy to write a test bench for something. So I, I, I know I'm interested to see what the design actually does in this or that situation. And if I write the test bench, I have to actually think about what my design does and what input do I need to put into my design to get it into the state I like to observe my design in. With formal methods, I can use a formal cover statement and say, just generate any trace that has this property. And the formal tool will figure out what, what to put into my design to get the design into this kind of state. Um, so, uh, but you need to know how to use these tools, right? If, if, if, if you don't have the time to, to use them, um, um, to just play around them, I guess we are back to this thing. You need to give people like a space to, uh, to learn new stuff. Um, because, uh, I think everyone should learn formal methods, but if you, uh, or at least everyone doing digital design.

**Clifford Wolf:** I'm trying to think what the equivalent would be for like circuit design, like, uh, like, uh, anyways, that, that's probably irrelevant here. But yeah.

**Clifford Wolf:** Yeah. Um, um, well, I did talk to people about like using formal methods with, uh, with spice and stuff like that. Um, but this is a whole different like area. Um, uh, that's also very, very interesting that you use, I don't know, Monte Carlo simulations, for example, in spice. Yeah. And instead of doing Monte Carlo simulation, you actually want to be able to give certain, uh, uh, parameters, ranges and say, make a proof. That no matter what concrete parameters I pick within that ranges, the circuit will always behave in this or that way.

**Clifford Wolf:** Right. You could say it's sort of like, you don't go outside this envelope of signals, right? Yes. That kind of idea. Yes.

**Clifford Wolf:** Um, but it's really, really hard to actually do that because if you look like at the, uh, system of differential equations for a, a modern semiconductor process, like BCMV 4.4. Uh, um, that's just, uh, I mean, it, it, it's 300 parameters or something like that and, and, and many, many pages of equations. Um, so, um, um, so it's very, very hard to, to make like trivial arguments, uh, about interval arithmetic, uh, with, with that kind of stuff. And I, I don't know what the solution to that is because that's not the kind of formal method I'm, I'm, I'm specializing in. Um, but I think that's also very, very interesting. And maybe if the constraints always, uh, improve, uh, maybe stuff like that will, will replace stuff like Monte Carlo simulation and spice.

**Clifford Wolf:** Um, that's, that's so far outside my pay grade. I can't even imagine.

**Clifford Wolf:** But, um, with, uh, so, so about a year ago, I decided I wanted to build a, um, a, a reference system using my formal verification tools that would demonstrate that, uh, you could do, um, large non-trivial things with it. And it's not just this, this toy program essentially. Um, and traditionally the thing that everyone said that's not possible to do with formal verification is to formally verify a processor against the ISA implementation of the ISA that the processor should implement. Okay. So I thought just let's do that. Um, if, if I do the thing that the textbook says don't work, then I have proven my, my tools is, is, is.

**Clifford Wolf:** Again, again, a challenge is placed in front of you and you say. Yeah. I'd like to try that. Okay. Yeah. Right.

**Clifford Wolf:** Right. Um, but I, I would say at the time the textbooks have been written, this was actually true. Okay.

**Clifford Wolf:** Okay. Yeah, that's fair.

**Clifford Wolf:** Right. But the constraint solvers, they improved a lot. Uh, and, uh, as, as a field, we learned a lot of, of, of, of new tricks, um, how to encode certain problems. Um, and of course, uh, a lot of this, uh, work was, was done at arm because arm has this arm ISA formal project, but does something very similar. Um, and luckily they actually publish papers about it. So it's not like you have to piece things together from, from, uh, from information here and there. No, they just published a paper where they have described their process. Uh, um, very well. They, they keep out some, some things, but, uh, for the most part, it's, uh, it's very well documented what they do. Um, so I thought let's just make something similar for risk five, uh, and let's build a framework. Again, I'm building tools. I always end up building tools. I don't build a formally verified processor because that would be like the usual approach. Um, instead I built a tool that you can use to formally verify a processor.

**Clifford Wolf:** Any response processor. Again, if you were going towards the heat death of the universe, you could throw any arbitrary set of bits against this. And then eventually you could say one of those arbitrary generated set of bits made a, or satisfies the risk V formal, or sorry, the risk V ISA. Uh, is that not really the point?

**Clifford Wolf:** Yeah. I mean, theoretically you could use this for reactive synthesis. Okay. Reactive synthesis is when you, when you take the properties and try to infer a design from that. Uh, but that's not what I'm doing. Um, and that would, that would not be really possible with the reactive synthesis tools we have at the moment. Okay. Uh, so that's a very, very interesting field, but it's not that, that far along yet. Um, so, but what we do is we take a processor we already have and we try all possible programs, you could say. Uh, so all possible, uh, machine code programs or bit patterns that you could find in memory. Uh, uh, and see if there is one bit pattern that demonstrates that the processor can behave outside the ISA specification.

**Clifford Wolf:** So what, if, if, if, if you did find one in, in like, what does that represent in the real world? Is that like a segmentation fault or like, what is that ultimately, what would that actual real world error be that you're testing?

**Clifford Wolf:** Uh, it depends. So, um, um, so I would say there are two classes of, of problems that I can find with this approach, um, that are very distinct and different for us human talking about processors, but, uh, indistinguishable for the tools. Um, one is I have a processor that always does the wrong thing when it comes to a certain instruction.

**Clifford Wolf:** Okay.

**Clifford Wolf:** Um, and just some engineer implementing the processor misread a line in the ISA specification and implemented it incorrectly. And he would say, well, that should be very, very easy to find with testing, right? When the processor always does the wrong thing.

**Clifford Wolf:** Right. Unless it's really, really buried and it never gets called, right?

**Clifford Wolf:** Yeah. So there's this one instruction. It's, uh, jump and link register, J A L R. Um, it takes a source register as argument, adds an immediate value to it, then clears the least significant bit of the result and jumps to that, uh, uh, address. Um, and a, uh, surprising number of processors does not clear the least significant bit of the result. You have to read this back very, very carefully to, to, to find that actually. Um, and when you have code that is generated by GCC, then this code will never actually produce an addition result where the least significant bit is not already cleared. So you can have a processor that implements one of the most basic instructions incorrectly. And you can still boot the Linux kernel and the graphical environment and run a web browser in it. Um, until you, uh, find some strange, uh, uh, chit compiler who uses the least significant bit in a function pointer to encode something about that function. And it depends on this instruction actually clearing the least significant bit.

**Clifford Wolf:** Um, and so the real question though is who's at fault here?

**Clifford Wolf:** Well, uh, in, in the meanwhile, now, now when you run RISC-V tests, they actually test this. Um, uh, uh, uh, but they didn't test it all the time. Uh, so, so this is one of the reasons why someone is just reading the spec incorrectly. Um, and then there is this other category of bugs where, um, um, um, there are a function does something different from what it usually does in one very specific situation. Um, so usual errors there would be things like, like in, uh, in the pipelining of your processor and bypassing, um, that you launch an instruction too early when the result it depends on has not been written to the register file yet. Things like that. Um, or bugs like the following, uh, that's one I like. Um, you, uh, uh, run a, you start a division instruction. Um, and, uh, while the division instruction is running. You reset the processor. Um, and then you start, of course, executing your program code from like address zero or wherever you start. And one of the first instructions that you execute is another division instruction. But you must make sure that everything happens just at the right cycle or wrong cycle, depending on how you look at it. And this second division instruction will, will, will return immediately with the result of the division you started before you reset the processor.

**Clifford Wolf:** So like didn't clear out some of the remainders and stuff like that, or?

**Clifford Wolf:** It, it, it didn't properly reset the division engine. Um, and when it tried to queue the new division and it happens just in the right cycle, um, then it will think that the division result that is produced from the, uh, the last division that ran until now is actually the division result of the division. It just tried to do, uh, right now. That's a bug that I happen to have in PicoRV32. It's one of the last bugs I fixed and that you can only find with formal methods because I mean, how would you like, like test this with?

**Clifford Wolf:** Exactly.

**Clifford Wolf:** You wouldn't tell you, tell your test group to be like, well, divide things and then shut down and then divide again.

**Clifford Wolf:** Yeah. Yeah. But, but try all different timing combinations that you could possibly have. Right. Uh, because only when you do everything just in the right cycle, it, it will work. Otherwise it won't. Um, and some people will say, yeah, but at the same time, it's not really a big deal. Right. Because this will never happen in, in production.

**Clifford Wolf:** Right. Um, unless your, your processor's around for 30 years and running something at the large Hadron Collider, right? Yeah.

**Clifford Wolf:** I mean, I mean, uh, um, or it's, it's on a weird space probe that originally only had like a mission time of 10 years, but it's still sending stuff. Uh, and, and 30 or 40 years later, you can still, uh, talk with it and suddenly it freezes because something like that happens.

**Clifford Wolf:** Right.

**Clifford Wolf:** Uh, that, that would be really bad.

**Clifford Wolf:** It almost comes down to like a million monkeys, million typewriters type thing. Right. It's like, yeah, just over time, you know, like at a human scale, we don't really care. Yeah. Right. We're like, oh, well, what's the likelihood. But yeah, eventually something's going to happen. You know, you win a lottery eventually.

**Clifford Wolf:** Yeah. So, so, so, so yeah. I mean, it all comes down to this. In the end, you try all possible traces. Um, and, and if you really try all possible traces, you find all the bugs. If your specification is, is correct and, and covers everything that your processor must do. And, and all the bugs apparently contains a lot of bugs that we wouldn't have thought about.

**Clifford Wolf:** Mm-hmm. Mm-hmm.

**Clifford Wolf:** Um, um, before we had former methods. Uh, because we've never seen bugs like that actually being discovered. Uh, right. Uh, because.

**Clifford Wolf:** Right. But, but they still could, right? There could be something buried in the x86 that is still waiting to, to, you know. I mean, yeah.

**Clifford Wolf:** We, we all the time discover new stuff. I mean, just, just now we had this new, uh, Intel bug. Oh yeah. The, the, the heating up and stuff. Yeah. You need to, uh, uh, flush the TLB now whenever you switch from userland to kernel. So there is a fix for it, but it's a fix that's very decremental to performance. Um, um, yeah. Yep. So, uh, so we wouldn't have things like that if, if everything would be formally verified. And, um, it's not always easy to formally verify anything, but if you have something that happens to be easy, you really should formally verify at least that aspect that you can formally verify. Yeah. Um, yeah. So I, I did this risk five foremost thing, uh, mainly to, to like show that the tools I wrote actually like mature tools and you can do non-trivial stuff with them. And now I've been to the, to the risk five workshop and I had a poster presentation about risk five formal. Um, and, uh, um, it turns out a lot of people have risk five, five processes and a lot of people are kind of aware that formally verifying things would actually be a good idea.

**Clifford Wolf:** Yeah.

**Clifford Wolf:** Um, so.

**Clifford Wolf:** Do you think that the, that this formal verification, if it becomes standardized would also help promote the risk five in the ecosystem because it just makes for a better processor. So now you have a ISA that's in a better shape. It's, it's stuff's verified against it. So that makes it better. It's free. It's up source.

**Clifford Wolf:** But, uh, but I mean the, the big competitor right now would be arm, I guess. And arm is pretty much doing the same thing. Um, so, um, the, I think the main difference is the, the thing we do with risk five formal is a little bit more in the open. Um, so at least for some processors, uh, you, you see the bindings between risk five formal and the processor, and you can try to reproduce the results on your own. Um, and you could not do that at least last time I checked with, with the arm stuff. Uh, you still have a lot of, oh, you have to trust the vendor that they actually did all the things that they did. Uh, I mean, I, I know some of the people at arm who are involved with that and I, uh, I know that they actually do the stuff. Um, but still it's, it's always nicer to actually see the thing. Right. Um, and not having to trust the salesperson.

**Clifford Wolf:** Yep. That's great. Well, I think after two and a half hours, we should probably cut this off, but I, I think the likelihood that I won't ask you to come back on and explain more of this stuff to me, cause I'm, my brain's pretty full right now and I'm sure that some of our listeners.

**Clifford Wolf:** Yeah, great. So, so I'd be, be happy, happy to come, uh, come back, uh, whenever. Okay, great.

**Clifford Wolf:** So are you, uh, are you, I mean, you were at, uh, CCC this year, of course. And, uh, uh, uh, where else are you going to be in the near future that people might find you?

**Clifford Wolf:** Uh, I, I, I don't know yet actually for, so I'm not going to be at foster. I can tell you that, uh, uh, because that's one of the usual suspects in a way. Um, I, I will definitely be at the next or conf, but that will be in fall. So that's quite some time until then. Yeah. I will probably be in, in the Bay area a few times, uh, the, the next year. I don't know when exactly, but if anyone there would like to meet up or give a presentation on any of my work or stuff like that, I'm, I'm always happy, uh, to do that. Uh, and if you're in the Bay area, just contact me and, and, and I will contact you when, whenever I will be there the next time. I think I will also be in the DC area one time or another, the, the next, uh, year. Um, um, yeah.

**Clifford Wolf:** So how do people, how do people get ahold of you? What's the best way?

**Clifford Wolf:** So probably Twitter is the best, uh, best way. So I am at, uh, OA1CXW.

**Clifford Wolf:** Oh, a one CX. Yeah, I get that one. Okay. Cool.

**Clifford Wolf:** Um, and, uh, yeah.

**Clifford Wolf:** Um, and that's your, so you're a ham operator too. So maybe they'll catch you on the airwaves, right?

**Clifford Wolf:** Uh, yeah, I think, I think the, my, my Twitter handle is the only thing I used my, my ham handle, uh, in the last couple of years. So at least it's good for anything, right? Yeah. I mean, if you, if you have something that that's really assigned to you in a guaranteed to be unique way, uh, and it's only a short number of characters, uh, that sounds like a good Twitter handle, right? Yeah.

**Clifford Wolf:** It's not bad. Yeah. Awesome. Right. Uh, Clifford, thanks so much, man. This has been, this has been a wild ride through processors and FPGAs and formal verification and everything. So I appreciate it. Yeah.

**Clifford Wolf:** Uh, so, so maybe, maybe we'll, we'll do another one where we stay a little bit more on focus. And, uh, I think we wanted to talk a lot about the, the exiling seven series documenting and stuff like that. So that might give us a good topic for next time. I guess.

**Clifford Wolf:** I think that's, that's a great idea. Awesome. All right. Well, we'll talk to you soon then.

**Clifford Wolf:** Great. Looking forward to it.

**Clifford Wolf:** Bye.

**Clifford Wolf:** Bye.

**Speaker ?:** Bye. Bye. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
