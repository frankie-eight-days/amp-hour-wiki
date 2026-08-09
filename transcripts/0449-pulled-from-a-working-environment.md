---
episode: 449
title: Pulled From A Working Environment
url: https://theamphour.com/449-pulled-from-a-working-environment/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released June 30th, 2019. Episode 449. Pulled from a working environment.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Hey, nerd. What is up? You know, summertime in the States. Summertime, yeah, winter over here. Spending lots of time in the lab. It feels like every time the weather gets nice, I'm like, yeah, I should probably do some more work. Right.

**Dave Jones:** I thought you just, yeah, because like, yeah, in wintertime, you get all depressed and, you know. Yeah, I think that's what it is.

**Chris Gammell:** Then you've got to shovel snow. Right, exactly. And like, now it's like, oh, the sun's up till 9.30. I could stay in the lab a little longer, that kind of thing. So I try and get out once in a while, but I'm not great either.

**Dave Jones:** Just try and get out once. Beautiful.

**Chris Gammell:** Yeah. How's it going down there? Down under. Down under. What, weather-wise? No, no, no. Life-wise. Life-wise? Busy. Life, you know.

**Dave Jones:** I'm away next week, though. I'm saying bugger it. I'm going to go and walk about next week.

**Chris Gammell:** Yeah, cool, cool. We will have, I will be posting, I did a bunch of recordings at Teardown, which is the conference I was at last weekend. Yeah. And that works out well, because I will post them next week. So I think I have like six, about half-hour interviews, so I'll do them in parts or something. Right. So people seem to like that. Yeah, that's good, though. Cool. And I got to take a really cool training, two trainings while I was there, actually. Do you tell? I usually don't do trainings. Usually I'm just kind of busy jibber-jabbing my head off with people that are there. But this time I was like, no, there's two FPGA trainings I want to take, and I'm very excited about all the open source tools. We've had Cliff on the show. We've had Peter on the show a couple times. You know, so all the open tool chain stuff that's happening right now. I think, you know, people ask, like, what is the most exciting thing you think is happening in electronics these days? And I think open tool chains and RISC-V are the two things that are some of the most exciting things that are happening. And I got to do both. So I was really excited about that. Right. So Peter...

**Dave Jones:** But specifically FPGAs, you said.

**Chris Gammell:** Yes, that's right. So the first one was just...

**Dave Jones:** Do you have a target? Do you have a reason why you're getting into FPGAs? No.

**Chris Gammell:** No. Like I said, I'm just excited about the tool chain stuff. I think that that... I don't know. Like, it feels like something big, you know? I don't know what it is, but I... And you see it more and more places, you know? Especially as more image processing stuff comes online, it feels like it's just a thing that's happening. I don't know. I don't know how to explain it.

**Dave Jones:** So we're talking about FPGA tool chains here.

**Chris Gammell:** That's right. Like the Ice 40 and the ECP5 and then the Xilinx one that's coming online. So this is all IOSIS and NextPNR. So...

**Dave Jones:** What's IOSIS and NextPNR?

**Chris Gammell:** So IOSIS is what Clifford Wolf and team, I think, developed. But IOSIS... Oh, man, I'm going to get this all wrong. I think IOSIS is the... I know NextPNR is the place and route because it's in the name PNR, place and route. So whatever comes before place and route, what is that?

**Dave Jones:** Oh, God, it's been so many years since I've done FPGAs. Sorry. Yeah, some people are cringing right now. Sorry about that. I know.

**Chris Gammell:** But when you go from very long to a netlist, I think, it's like whatever that interpretation layer is. It's not a compilation. I want to say compilation, but it's not that. Anyways, that's what IOSIS is. And I'll add the links to all this stuff so people can go and look this up if they want to.

**Dave Jones:** So are these different... Take the Xilinx part, for example. Is this an entirely different tool chain from the Xilinx or does it work like, say, the Altium one where it simply was a nice sort of, you know, gooey interface layer and then just called up the Xilinx tools at the command line level and just handled it all for you?

**Chris Gammell:** No, no. So this is the one that they reverse-engineered bitstreams on multiple parts. Oh, right. And then they developed tools that basically allowed them to then go and create exactly the same bitstreams.

**Dave Jones:** This concerns me. If I was doing professional development and you're talking about they had to reverse-engineer bitstreams, I mean, FPGAs are insanely complex, the most complex devices on the planet, right? I don't know if I agree with that. The Xilinx... No, come on. It's why the Xilinx and Altera tools are... How big is the download now, right? Oh, 20 gigs, probably. Yeah, 20 gigs, right? It's why they're so massive. They're so... I'm not going to... Well, bloated. It's probably not the right word. They're probably that big for a reason is because there's just so much stuff in them. And when you're using some new tool that has to reverse-engineer the bitstream, that makes me scared that I'm going to run into some obscure bug that's just going to be a project showstopper.

**Chris Gammell:** Totally possible. But I think that the...

**Chris Gammell:** The thing is, the companies aren't going to give up the... I think they're trying to get the companies to buy into this, right? No, that's...

**Dave Jones:** But of course they're not. The Xilinx and Altera's of the world... Sorry, who are they? IBM? Who owns them? Intel now, yeah. Intel, sorry. Intel own them. Yeah. Do they still call them Altera? Or are they Intel?

**Chris Gammell:** You see, anytime I get an ad these days, it says Intel FPJs.

**Dave Jones:** Intel FPJs. I thought so as well, yeah. Yeah. Anyway, I'm still going to call them Altera. Whatever. That's fine. Yeah.

**Chris Gammell:** I think it's still understood.

**Dave Jones:** Yeah. That's their business. I mean, they have thousands of programmers working on this software. Like, it's that complex. And that's their business. Yeah.

**Chris Gammell:** So you were talking about the 20 gig thing. And I think, or like the size of that thing. I think that's because that's across the entire spectrum, right? That's not just...

**Dave Jones:** It's across the entire spectrum. And they have to have legacy support and all the rest. Exactly.

**Chris Gammell:** So it's not just Spartan 6 or even Spartan 4 or 2, whatever.

**Dave Jones:** But that's the problem. There's so many variants of all these.

**Chris Gammell:** Sure, sure, sure.

**Dave Jones:** And it's like, and of course, you know, Murphy being Murphy, you're going to need this particular part that's, you know, not supported or is buggy in some third-party software because nobody else is using it yet, has actually used it yet. You're the first person to use this, you know, slash 2 variant of this part, you know, with this new software.

**Chris Gammell:** Sure, sure. But I mean, like, so if you look at what's actually happening here, right now there's only three parts, I think, that are not even officially. I think though...

**Dave Jones:** It's good to focus on a couple. That's right, yeah.

**Chris Gammell:** And so, and Lattice has been really supportive as far as I can tell. I met some of the Lattice folks who are really nice. This is an older part. It's an older part. The Bitstream, I don't know what the status of it is. Like, it's definitely like a reverse, you know, I think it's like under fair use or... And I, so Clifford's been on the show. Then Peter interviewed FPGA Dave and Clifford at Chaos Communication Congress last December. And that's when he did our traveling correspondent thing. People can go back and listen to those. But I don't know what the status is of like how it all works out in that, in like legality and whatever else. But from my perspective, I'm really excited about it because if something like a Lattice, you know, bought into this thing, basically now you have a bunch of people that are willing to donate their time and their talents to tools like this. I think it's just really, really cool. And the crazy thing, and so this is what was called out in Peter's workshop. So Peter did a workshop there. And he, and basically, you know, you watch these tools happen. Like it's a really nicely done workshop. It was like Joe Fitz also has been on the show and Clifford have done these workshops in the past as well. But basically it was like you click go. And by the way, Yosis is a synthesis suite. Ah, right, yes. So it's Yosis Open Synthesis Suite. That's a recursive acronym because the Y is Yosis and then Open SYN Suite. Anyways, so that's synthesis. But basically all of these tools, you click go and it's like 20 seconds, Dave. It's insane. And like, and like they actually timed it. They said it would have been an eight minute. It would have been an eight minute synthesis and then place and route and everything else.

**Dave Jones:** Yeah, but it's just faster. Is that a big deal?

**Chris Gammell:** I think that's, that can definitely be a big deal. Like think about like iteration cycles when you're like, so I don't know about you. I was, I was telling some of the people at this training. Back in my old, old days when I was doing FPGA stuff, you know, I'd click go on a thing, you know, and I was doing like mathematical modeling and like, like Simulink, which is like the Matlab tour.

**Dave Jones:** Yeah, and you go have lunch and you come back. But they've got to have something more than just speed. I mean, there's got to be like, yeah, like we're still talking about, we're still talking about synthesizing Verilog, right? We're still talking about Verilog and VHDL code. So you write your Verilog or VHDL code and you hit go, right? And, oh, what, it's only Verilog?

**Chris Gammell:** As far as I understand it, yeah.

**Dave Jones:** Right, okay. Well, anyway, do your Verilog code, you hit go. And so if their only thing is that they're faster, I don't see that.

**Chris Gammell:** Okay. So what's the one thing that's always been missing in an FPGA? What's something that you can do in a micro that you can't do in an FPGA? That's a trick question, of course.

**Dave Jones:** Well, you can run sequential code.

**Chris Gammell:** Sure. And that's actually, that's the big difference that I will come back to. But I was actually thinking you can switch vendors, right? If you write C, now, granted, there's going to be some kind of, some level of trouble there. But if you switch from an Atmel part to an XP part, they're, you know, basically GCC handles that without problem. If you do that in an FPGA, you have to start over pretty much. You know, like you basically can't target multiple parts.

**Dave Jones:** Well, no, that's the whole idea of a high level definition language is like VHDL, like Verilog and VHDL. That's the whole point. And like, and when you change vendors, you've still got all the little nitpicky, you know, stuff. The same with micros, you know, you change vendors, you've still got the same picky stuff. But your C code is still got to transport over, right? Yeah, the code itself. I'm not sold on this yet. I'm not buying this. Well, anyways. No, sorry.

**Chris Gammell:** I don't, I mean, I don't mind if you're not excited about this. I think this is very exciting. Okay. All right. And so these tools are now open and fast and I'm sure I'm missing other benefits.

**Dave Jones:** Can I have another little, can I have another little whinge? Another question. It's not a whinge. It's a question. Sure. Aren't most of the FPGA tools still free for like these sort of like low end parts?

**Chris Gammell:** I can't say I've used an FPGA tool in a long time, Dave. This is like, so this is my return to FPGAs.

**Dave Jones:** Well, they were. Okay. So they were last I checked, right? For sort of like the low end FPGA, you know, hobbyist one man band type FPGAs that you're going to want to use. They're, you know, the tools are basically free. So what does open source bring to the table in that case?

**Chris Gammell:** I think other things are like.

**Dave Jones:** What does it be in open source bring?

**Chris Gammell:** ASCII based stuff. I think it's like ASCII outputs. So like, so like right now, if you, if you go and hit compile on a, not compile, if you go and, you know, start using a Xilinx tool, it's all binary stuff. And so it's, it's not, you don't have visibility in the lower level stuff.

**Dave Jones:** Yeah, but. Well, some of us use revision control. Tools like Altium. Right. Right. Okay. Right. Yeah. Fair enough. And not in DaveCad. That was fun.

**Chris Gammell:** That was a fun DaveCad thing where you said. That was, that was. How do you do revision control on DaveCad? It's a tape, tape and, and scissors.

**Dave Jones:** And it's a git paper.

**Chris Gammell:** Git paper. Yeah. Right.

**Dave Jones:** It's git paper. Anyway, people are talking about Twitter. We just, yeah, we're, we're both on Twitter and we banter back and forth. Anyway. See the advantage, like when FPGA, when Altium did FPGAs, for example, right. The, the, the beauty of that is that it was all high level. You could drag these blocks in and it just like, and it just like, sort of like seamlessly worked. And yes, you could go between different vendors and stuff like that. You could just drag it in and it would all sort of like handle that for you. You could drag in a processor core and it would just work. And then you could convert some of your C code to Verilog or VHDL, right. It had a C to HDL synthesis thing, you know, converter. And, and it just, from a high level point of view, it was, it was really magical. So if you wanted to make a real simple application and, and you could even do it like from schematics and things like that, you didn't even have to write any Verilog and things like that. So from a high level point of view, it allowed you to use an FPGA very simply where it, where it actually came a gutter is when you wanted to do like really serious projects. Right. Really, you know, where you had to get to the nitty gritty of stuff. It just, well, you know, all that, all that, you know, flashy high, high level stuff just got in the way and kind of, you know, didn't let you do the job. So. Right. Yep. Yeah. So I like, and, and that was, it was really very nice system. And if this open source one is just, well, it's open source, so it's, it's already competing against a free tool. Okay. It's open source, but nobody really cares about open source as long as it's free. Right.

**Chris Gammell:** I disagree with that.

**Dave Jones:** And no, come on. There's, I put it in PCB land, Dave.

**Chris Gammell:** I, I, I, there, there's tons of free PCB tools. I care about open source. Okay.

**Dave Jones:** But nobody using key CAD cares that key CAD's really open source. They don't really care. All they know is that it's good and it's free.

**Chris Gammell:** I would say that it matters. It is, it has saved my bacon a couple of times that it's open source because people have been able to modify and write plugins for it without any issue. And those plugins have actually saved my bacon. Fair call. Yeah.

**Dave Jones:** Okay. Fair call. But most users, most users. Yes. I think casually. You are so intimately tied in the key CAD community that I, I'd say you, you're not the average key CAD user.

**Chris Gammell:** I would agree with that. Yes.

**Dave Jones:** Yeah. Right. All they want to do is download the latest executable. And if it doesn't do something, it doesn't do it. Right. They'll just find another way to do it. Right. It's like one of those, you know, I think you're just, I think you're just looking for

**Chris Gammell:** things that you like picking fights about open source here. Anyways.

**Dave Jones:** No, no, no, no, no.

**Chris Gammell:** Some of your points, some of your points, some of your points are valid here, but I'm not the best. I'm not the best proponent for this. You know? Yes. Exactly. No, I'm just saying that like, even for the FPGA stuff, I don't think I'm the best one.

**Dave Jones:** See, because I come, once again, I come from the FPGA, you know, intimately involved in the FPGA community. Right. So I've got my own, you know, things about this. But I, okay. So it's, okay. So it compiles faster and it's open source. Cool. All right. But if it's competing against an already free tool from Lattice or from Xilinx, then well, okay. That's going to be tough.

**Chris Gammell:** I don't, I guess so. I mean, you can always switch back to that though too. You know, like it's not like.

**Dave Jones:** Yeah, sure. No, because that's the, that's the advantage of writing in a HDL or high definition language is that you can switch back. There's a little bit of grief there, but generally speaking, you know, shouldn't be too much of a problem. So.

**Chris Gammell:** Right.

**Dave Jones:** Hmm.

**Chris Gammell:** Yeah. So I was getting back to FPG for the first time. And basically, I mean, like it was like pretty much a beginner's workshop, but it was interesting to watch it happen. And, and, you know, honestly, just to switch back into that, I mean, I don't know the last time you wrote HDL stuff, but it's been, it's been a while for me. It's like. Yeah.

**Dave Jones:** I would, I would have to, it's been so long. I would have to start from scratch. You know, I'd have to go back and. Yeah. Yeah. Exactly. So. And also. I'd have to get out the VHDL for dummies, you know.

**Chris Gammell:** Yeah. I, I, I, I started, when I started doing FPGA stuff, it was always VHDL and I had done a little bit of Verilog.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. When I started what? Oh geez. Probably, you know, 15 years ago was the first time I did it probably at least. And yeah, like a VHDL was the thing. And now it's like, it seems like, you know, I don't know. Does anyone let us know? I think. I think some people still do. Like some people still do, but Verilog seems to have taken over.

**Chris Gammell:** I think, yeah. I think the, the chip industry is using Verilog mostly. I think that it's, you know, it's a little. So it won the war, you think? Uh, it's never going to be like all, all or nothing, but it's, uh, I think that, uh, you know, like, like I said, like tools like this too, will also help to, you know, people that are coming in. And if there's accessible stuff, then I think it'll be more likely that it'll be Verilog and VHDL.

**Dave Jones:** But Verilog probably, it reaches that like 80, 20 ratio. Yeah. That's probably. There's a ratio thing. So it's probably, yeah. Yeah. Once it captures like 70, 80% of the market, then it's, you know, it's done. Like, yeah.

**Chris Gammell:** Yeah. Yeah. I, and so like, because I came from the VHDL world where it's like, you can't type a single thing unless it's like, you know, if they like type it in multiple places and it checks everything and everything has to be like perfect. Verilog's just like, yeah, do what you want, man. Just like. It's cool. Yeah. And, uh, yeah, that, uh, that, that did not serve me well. Right. Like I typed one variable wrong. I think instead of time, I typed Tim and, uh, and it was like the, the, uh, the synthesis tool is like, Hey, I noticed you made a new variable here. Uh, I'm going to warn you about it, but, uh, I'll just make a new one. It's cool. It'll just be over here when you need it. It's like, no, don't do that. Tell me I'm an idiot. Come on. I need to. So, uh, yeah, it was, it was, it was a good, uh, it was good.

**Dave Jones:** Oh, I've, I've got a segue.

**Chris Gammell:** Okay.

**Dave Jones:** I've got to say, speaking about, uh, sort of like, uh, you know, cross-platform code and things like that, the, uh, micro supply that we're working on, right. Or David's working on, you know, um, we're working on the, uh, USB interface, right. Cause we've got like a USB, uh, type C, uh, power delivery controller chip in there. Right. So it's, I'll send you a, uh, send you a link here.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Here we go. So you know what I'm talking about. And, uh, we're actually, okay. So the, you know, it's hard to talk and type at the same time. Now we're, we're, we're using a, uh, Rich Tech RT1716 chip of the week. Um, it's a programmable USB type C power delivery controller chip, right. So it sits on the, um, USB side of the isolation transformer, right. So we've got, you know, power comes in, it's isolated, of course, right. So it's an isolated, uh, power supplier, spoiler alert. And, uh, right. So it handles the negotiation with the, uh, with the type C USB port, because we need to deliver more than your 2.5 Watts. Right. So, so we have to negotiate the higher power levels and stuff like that. So you really need a chip that already, you know, handles all the protocol, the USB power delivery standard PD. And, uh, so we're using this little chip and unfortunately, like it's a, you know, it's a good chip. It's the one we wanted, but unfortunately the development information that came along with it wasn't that great. Right. So David's scratching his head going, Oh, how do I use this damn thing? Right. And, you know, he couldn't really, couldn't really figure it out. But then he, uh, determined that, um, it, it should use the standard protocol. Well, obviously, right. It uses USB type C power delivery as a standard, right. So I can't remember the name of it anyway. So it uses this, um, uh, standard. And so what he did is he went to a Texas instruments part, which was another type of type C, you know, a competing device. And he used their development information and he, and he tried that on the rich tech one and it just worked. Right. So, yeah. So he was, so he's using, he's stealing the Texas instruments development information and, and, and the code and software and stuff, um, to, uh, yeah, to talk to this rich tech, uh, controller and, and it's all just working. He says it's sweet. It just, you know, he can't believe how good it is. And now in theory, he's written his codes so that, uh, we should just be able to, if, if say this rich tech part suddenly went obsolete, right. End of life. And we're five years into the product. Then in theory, we could just switch it out with any other power delivery controller chip and our code should still just work. That's in theory. So anyway, we've got lots of cool functionality now where apparently we can do remote debugging of our main microcontroller over the isolated serial interface through the rich tech tie, a USB power delivery chip. And we can update firmware over that and everything. It's really.

**Chris Gammell:** I'm confused. So like, uh, it looks like there's a I2C interface. Is that not what you're using? It's, it's serial. Yes. Yes.

**Dave Jones:** Yeah. Oh, sorry. Uh, yeah. Well, we're using I2C. Yes. There's an I2C interface and, uh, sorry, no, sorry. We, we have, no, we have another micro on that side. Oh, okay. So yeah. Anyway, so we can update. Yeah. We can update our firmware, our bootloader code. We can do remote debugging over an isolated serial USB type C interface. And it's really, it's really quite advanced. David's like, you know, like just wetting himself. You know, it's so, it's so fantastic. That sounds impressive. That he is. Yeah. That's great. Um, you know, it's, it's granted it's complete overkill for a product like this, but it's kind of, you know, yeah. David's terribly excited over it. So.

**Chris Gammell:** These are not. Yeah. It's just really cool. Tiny parts too. That's chip scale package.

**Dave Jones:** Yeah. Yeah. I think I'm not sure which one we're using, but that looks like it might be the only one anyway. Yeah. Yeah. Pain in the ass. Um, but yeah, it's cool. So yes, all this, um, cross platform kind of, you know, stuff is. So yeah.

**Chris Gammell:** What does that mean by cross platform? It's just that it, it talks to each of the, like it talks to Mac, Windows and Linux. No problem.

**Dave Jones:** It, well, sorry. Yeah. No, I'm using the wrong term there. Um, cross vendor.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Cross vendor. So it's in theory, we can move to any vendor and we don't have to change our code and our development system.

**Chris Gammell:** So is it, yeah. So is it like the, the, the registers are the same internally? Is that kind of the idea? It's like, so.

**Dave Jones:** Yeah. So I believe at the register level, it's identical. Wow. Don't quote me on that though.

**Chris Gammell:** Makes you wonder if like, is it, if the rich tech was supposed to copy the TI thing, or maybe it's like a standard even. I don't know.

**Dave Jones:** No, I believe it's part of the standard. So yeah, he's, he's actually following the standard. And it's, and it's just working. It's yeah, it's great. But granted, right. This has taken months, right? This has taken months of full-time development just to sort out, uh, this USB power delivery stuff. So just be aware folks, if you're developing a, oh, I just whack in a USB chip and I'll get power delivery and I'll get, you know, I can download my firmware to my product and it's not going to be that easy. Right. Um, yeah. It's, there's a lot of effort, but once it works, it's pretty cool. Yeah. But there's a lot of, and David's really good at this stuff and he spent months and months trying to figure it out. Yeah. So yeah.

**Chris Gammell:** Yeah. I'm looking at the, uh, I'm looking at the, the, the register side by side and it does look like they're the same. So that's, that's great.

**Dave Jones:** I think, I think I do believe they are. Yeah. So yeah, it's very cool. Anyway. Yes. He was, he was like stunned that it was, that it actually worked. Yeah. Yeah. So that's great.

**Chris Gammell:** That's great.

**Dave Jones:** Hmm. Very impressive.

**Chris Gammell:** Um, I know you had a segue and I wanted you to do that. So that was a good segue, but I, I did have one other training I want to talk about too. Oh, okay.

**Dave Jones:** Well, segueing back. Yeah. Well, not really. It's okay. It's a, we're looping back.

**Chris Gammell:** Looping back. Yeah. So, um, so the other one I did, uh, go to 10, um, on this loop rubbish.

**Dave Jones:** Yeah.

**Chris Gammell:** So the other one is actually a link in the, um, is a link in the show or not the show notes, but on, on the subreddit and it's the FOMU and we've talked about the Tomu, uh, briefly in here before. So we've had, uh, Tim Ansell is on the show before. Um, and so Tim is the one who did the Tomu, which was a tiny little USB thing. It plugged into your USB port, it like disappeared in there effectively. And I kind of never really got it. I didn't quite understand. You know, it had a USB or I'm sorry, it had a LED on there. It had a couple of like touch interfaces, like cap touch thingies.

**Dave Jones:** Uh, I don't actually remember it, but I can, but I can visualize. Yeah. Yeah. Yeah.

**Chris Gammell:** It looks like a, like a, one of those, you know, like, um, like how you can plug in a wireless receiver for your wireless mouse kind of thing. Like, like that size thing.

**Dave Jones:** So you didn't quite, so you didn't quite get that, but now it's got an FPGA in it. You suddenly get it because you're all excited about FPGAs at the moment. Well, yeah.

**Chris Gammell:** So I, I mean, it wasn't even, I didn't, it's not that I get like a light came on. Like I asked, I was like, so like, what's, what's the point here guys? You know, like, and, and some of it is just, I think the Tomu even the Tomu was the micro based one was basically to get people programming. You know, that's kind of the idea is to get people programming and doing stuff, whatever. Um, this one as well. Like, so I look at it as a hardware person and I asked him, I was like, oh, sorry, it's Tim and, uh, uh, Sean, uh, Zobbs cross. Um, so Zobbs is the one who worked on the Novena with Bunny. Um, so that Bunny and Zobbs worked together a lot on, on hardware software stuff. Um, so Sean did the hardware, uh, and a bunch of the firmware for this. And then Tim's also pushing a bunch of FPGA stuff these days. So that's, uh, so Sean's, Sean's doing a lot of this stuff. And so both, I was talking to both of them. I was like, so like, what is the, what is the point of this thing? You know, like what, what, what is it you say it does here? Um, and because mostly because the hardware person, I look at it and it's just an LED, like a, you know, it's a tricolor LED. Fine. Neat. Cool. Uh, and then like for tiny, tiny, tiny little, you know, cap touch, or I think they're even just resistive touch pads that you can pair them up to get cap touch or something like that. Um, and so I was like, well, what are you, what are you guys doing here with this? Why is this here? And so Sean's like, Hey, you should come to this workshop. I'm going to show everyone what it is. And it's, and so it's called, uh, the, the link that I'll share is the, uh, the, the workshop slides, but it's, I'm looking through them now.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** Yeah. So the, the three levels of FOMU are, uh, Python, then RISC-V and then FPGA. And so all the way through the workshop, what you're doing basically is you, you know, you basically you're just loading bit streams to start with, but you load a bit stream on this FPGA. It, the bit stream has a, um, an FPGA in it, or maybe it's more than just a bit stream, but it has, it has, um, uh, microcontroller in there. It's already got RISC-V microcontroller with a wishbone bus. It's got a built-in USB controller, and then it's got Python already compiled on top of that micro Python rather. So basically what happens is it pops up as a micro, micro Python prompt. And so you just start writing Python. You can access the LED. Then you, you dive down a level, you go to the RISC-V thing, and then you can write, you can compile your own C code for the RISC-V that's underneath there. Right? So now you're not at the Python level, you're at the C level. Right? Then you can basically access the wishbone directly. Right? So wishbone bus. Yes. You know wishbone bus, right?

**Dave Jones:** Uh, wishbone. Yes. That's what Altium used, Altium used to wishbone. Right.

**Chris Gammell:** So that's like a way to, like a standardized bus in FPGA is to like add peripherals to a microcontroller, a soft, uh, soft CPU that might be in there. And you can like basically write, write your own devices that then hook into the wishbone bus. You can, you know, talk to them with a soft, uh, CPU. So in this case now you can then from your computer through the USB port, you can then directly modify the memory locations on the wishbone bus. And so basically from, from your terminal on your computer, you were then writing values to a wishbone bus. So basically if you think about like you're running a program on a CPU and you wanted to halt it, you can then go and change not a value in the code, but actually a value of something like a device on the bus, which is like pretty crazy. Then we basically ripped out this, the CPU. I might be getting this order wrong, but then we ripped out the CPU and then we could just write just random, not random, but basically just low level Verilog that does the same thing. And all the cases we were just changing the LED, you know, color. It wasn't anything crazy or anything like that. But in each case it was showing like the different levels of software. And I told Sean, I was like, you know, basically like anytime you hear a JavaScript person saying they're full stack, you have to like laugh in their face now because it's like, you're not doing all this stuff, you know?

**Dave Jones:** Yeah, no, you're not doing hardware, soft cores, you know, you're not doing FPGA, bitstream, infrastructure. All the way down to the bottom.

**Chris Gammell:** And of course there's always like, you'd be like, well, you didn't design the FPGA, you know?

**Dave Jones:** See, this is what I was talking, this is what Altium, this is what allowed you to do it so trivially in Altium. That was the magic offer. This is a similar sort of thing. It's allowing you to use a soft core, it's using the Wishbone plugins and you can just, yeah, yeah, yeah. Right.

**Chris Gammell:** Yeah. So I had never done anything like this and it was, I mean, super cool. Like it, you know, it took a while to get all the software installed and stuff like that. But, you know, it's getting to the point where a lot of the software was just like packages that were just like installable from, from Linux even. So. Right. Pretty, pretty cool stuff. Okay. Yeah.

**Dave Jones:** No, this, this totally reminds me of Altium. Yeah. Yeah. It's been there.

**Chris Gammell:** Yeah. And I'm sure that there's people like, like I'm not doing.

**Dave Jones:** Except it has Python because Python wasn't a thing back then. Right.

**Chris Gammell:** Right. Right. But yeah, it was, I mean, super cool to do those two things. Kind of a reintroduction to FPGAs. Like I, like, I think you asked at the beginning, like, why do I even care about FPGAs? Well, like, I don't really know. I don't really have any projects that need them right now. But like when you need them, you need them, you know, that's kind of the thing. And so having the tools now is good. And if, and if the parts are big enough to put like small soft core CPUs on there, like that's kind of cool too. Like it's not necessarily the most power efficient, probably not the most low cost kind of thing. But, you know, if I'm doing a design and I'm feeling like something's going to change in a big way at some point in the future, yeah, maybe this would be a good fit. You know, I can put something on there and, and just reconfigure the whole damn thing at some point in the future. So I found these very energizing workshops. So nice job to both of them and their teams. They did a great job. Well done. Yeah. Yeah. I don't know. I don't know if, I don't know if you ever found a good use for FPGAs.

**Dave Jones:** I didn't, yeah, no, not really. I've never worked on stuff that needed so much parallelism.

**Chris Gammell:** Yeah. I always figured like stuff that was like signal chain based stuff. So you need to like do things fast and you need to like, you know, like I always think like filters and things that have like big data flows going through them. Maybe not, you know, for a little small projects.

**Dave Jones:** No, I haven't worked on projects. Like I've used FPGAs for the sake of using FPGAs because I was at a company that did, you know, was focused on FPGAs. Yeah, yeah, yeah. You've got to showcase stuff, you know. Yeah. So, oh, look, I can get a 10 gig bit per second Ethernet interface decoding. Great. You know, fantastic.

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. But I don't really have a, you know, an actual project application for it.

**Chris Gammell:** Right, right. Yeah. Oh, sorry. There's one more thing too. And I was just kind of flipping through the slides too, is there's another thing called MyGen and LightX. And I don't know which one's which, but basically now it's at the level where now, okay, so now you have these low level tools and maybe this is a reason people like this stuff too. So you have these low level tools that allow it to like synthesize and do all the other stuff. But then you can then, LightX and MyGen, I think are Python based that are written on top of this. Right. So like you were talking about like big, doing big blocks of things. Now it's basically like calling hardware blocks and assembling them all together. And that's another thing that like, because now the tools are open underneath, you can start to stack stuff on top. Like this is the same thing I like about KiCad is that all your Python tools are based, like the ability for someone to change KiCad and do like a tool that I can use and modify files is pretty trivial in Python. Trivial for other people, not for me. Right. And, but it's because the tools underneath are, are open. So, so I think that's, that's the layers we're getting to is that if you're, if you're already all the way down to the bottom and just open all the way from the bottom up, I think that enables some of the high level software tools to, to be scriptable and, and turn things around faster. I think.

**Dave Jones:** We are living in a world where things are getting easier and easier. Yes. Yes. Because all these smart cookies have done all the hard work to, you know, develop all this stuff.

**Chris Gammell:** Right. Yep. I agree with that.

**Speaker ?:** Yeah.

**Dave Jones:** Very cool. Yeah. All right. News, I guess. Raspberry 4. Do we care? No, not really. Yeah. Yeah. No, it's interesting. Raspberry Pi 4. No, come on. It's not interesting. What are new Raspberry Pi?

**Chris Gammell:** It's not interesting to you? I think it's interesting.

**Dave Jones:** Why?

**Chris Gammell:** It's got dual monitor outputs. It's USB-C. Oh, yay. It's 35 bucks still. I don't know.

**Dave Jones:** Okay.

**Chris Gammell:** It's a new core. I don't know. I think, I think these things are interesting. Maybe not as interesting, but.

**Dave Jones:** Sparkfun have another development board. Yay.

**Chris Gammell:** That one's kind of interesting too.

**Dave Jones:** The Artemis. Okay. Yeah. They're all interesting if you're, you know.

**Chris Gammell:** Do you know what it is?

**Dave Jones:** In some niche way. Do you know that one? No, I don't know what it is. No.

**Chris Gammell:** So that one is, so.

**Dave Jones:** It's an ARM Cortex M4, right? Right.

**Chris Gammell:** So what they're doing though is like, you know, what do they call it? It's, it's a machine learning algorithm. Yeah. You can tell I haven't reviewed this in a while. But basically it's a.

**Dave Jones:** Is it one of those? Yeah. It's one of those edge cloudy things. Yeah. Right.

**Chris Gammell:** Is it in here? Sorry. It's so basically like when you're doing like machine learning on something, right? You basically have a model. Like, so you have like servers. So when I, when I did that AI course, that open AI course, basically it was doing like machine vision on a thing, right? So basically you feed in a bunch of images and then the machine kind of iterates on, iterates on it and starts to find edges and dual and basically creates these variables that then allow it to then go in and recognize these things in the future. Right. And that's basically, that's the model that it creates. The idea is that it, it then loads this down onto a smaller device. And in this case, it's a Cortex M4, which is kind of crazy. TensorFlow. God damn it. That's what it was. So TensorFlow is one of these things that allows it to like learn over and over and over again. That's what I think Google came up with. But there's a new TensorFlow for microcontrollers where now you, you do all the, the actual value creation, value creation, where you've figured out all of the variables rather on a big server and then you load it down onto a micro. So the micro is not, right. It's not crunching on it. It just can, can then.

**Dave Jones:** It's not doing the low level crunching. It's, it's, you're working on more abstracted. Yes, that's right. Data, so to speak. Right.

**Chris Gammell:** So, so the thing that, that SparkFun just announced is that Artemis is like this little Cortex M4 module, right? It's actually like a, it looks like a pre-cert, but I don't think it's actually pre-certified. But the idea is it's got a microphone on there, I think. And then you can then drop this onto any kind of simple product, much like how, you know, you or I can go and buy a simplified like cell module where we're not actually putting a cellular baseband chip on a board. We're just putting down a module and then you're interfacing with like a serial bus. This is now the same kind of thing, but doing it for voice interaction. And so that's why all the things say like, say hello to the, to the, I think that's, yeah, that's Alistair's thing.

**Dave Jones:** Yeah, I, I, I thought it would, it implied voice. Yeah, right. Yep. Stuff.

**Chris Gammell:** And, uh, it's pretty cool. I think, I mean, like it's, it's not a trivial thing to like add voice control. Like, like we think it's everywhere because it's, you know, all the Amazon products, but like there's a lot of computing that goes on there and obviously that's talking back to a server too. Right. So it actually, you know, some of the low level stuff like the, so like, oh, sorry, sorry. I'm going to preempt everyone. I'm going to say a word now that your, you know, your echoes are going to not like, but if I say like Alexa, play some jazz, right? The, the, at least the Alexa part, when I say Alexa, that's actually internal on the device. The play some jazz is what's sent up to the server, right? So it actually recognizes that stuff. Uh, the same thing though, if I want to have a trigger word, so we had, uh, Bernard and I forget, uh, I forget the name of the company, but we had people on the show before, um, who were doing the same kind of thing. They did it on like a, a really, really big processor. That was like, uh, that was like a arm a 11. It was something big. Um, uh, but it was the same kind of idea of like having, having like an audio trigger. Now this is basically that and shrinking it down, down, down, down, down, down. So, um, right.

**Dave Jones:** I've done a video on, uh, voice recognition from the 1980s. 1980s.

**Chris Gammell:** Yeah. I remember that one.

**Dave Jones:** Yeah. Tandy Radio Shack VCP 200. That was a great video. Yeah. And it's, um, and I build it up on, on a breadboard and I use the original chip I had from my junk bin from the 1980s. And it's amazing what you could do. This was like, I, was it a, my, I can't remember. Was it a microchip? They weren't called microchip. They were Arizona microchip back then. Although, uh, what was their former company name before that? Mike, Mike.

**Chris Gammell:** No, I thought it was like general something. Wasn't it?

**Dave Jones:** Gen, general semiconductor.

**Chris Gammell:** General instruments.

**Dave Jones:** Was it? No, the gen, general instruments, general instruments. Yeah. Yeah. That's it. Thank you.

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, I think it used one of the early ROM based, like 1k PIC processors and they shoved voice recognition in 1k.

**Chris Gammell:** Right.

**Dave Jones:** Like they did 1k of programming memory. Like insane. Right. I think from memory. Anyway, I'd have to look at the details. We can post the video down below, but yep. Yeah. And you could do like it had instructions, you know, you could do start, stop, turn left, turn, right?

**Chris Gammell:** Right, right, right. That's like the phoneme, uh, detection stuff like that. Yeah. Phoneme based thing. Right, right.

**Dave Jones:** Yep. Yeah. And it worked. Yeah, it was cool.

**Chris Gammell:** I think this is like, uh, you know, I think at the lowest level it might be doing some things like that. But like basically instead of having it hard coded into memory now, you can have it retrained and stuff like that. Yep. All that sort of jazz.

**Dave Jones:** Cool.

**Chris Gammell:** Yeah. And that's the thing. Like, I think that we benefit from, from stuff that is, uh, like modules like this, you know, like it really enables a lot of things. Like I could never, like I said, I use cell modules all the time now. I don't, uh, I don't have the ability to go and do a, you know, a base band chip, put that down and all the.

**Dave Jones:** You wouldn't. No, no. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** You'd be foolish to do it. And then you've got, yeah, you've got compliance issues instantly.

**Chris Gammell:** Right.

**Dave Jones:** You know, because you've got a bloody transmitter. Right. Right. Yeah. You know, it's, it's not just a regular, oh, EMC emission, right. It's not just a regular board that, you know, has transitions and, and, you know, you've got some EMC stuff to deal with. No, you've, you've got an intentional transmitter. Like, you know, that's when the FCC come around with, you know, handcuffs, um, you know, like, yeah. Whereas if you just got your little processor, Arduino hat board and you're selling that on eBay or something, like no one cares. Right. Right. But when you're selling an intentional transmitter, yeah, someone's going to care eventually.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** Yeah. Yeah. Anyway, more, more news. Yeah. We've talked about this and it involves a former guest, Robert, uh, Ferenac, who does the, uh, PCB tutorials, the excellent, uh, Altium and PCB design tutorials. Yep. He's probably the only one in the world. He's actually doing like, that's his full-time job is he does PCB design tutorials. And he, uh, offers these courses through Udemy, which we've talked about here many, many moons ago. It's one of those, you know, online plat publishing platforms where you can publish. Yeah. Anyone can make a course, you know, like, like a video type tutorial course, publish it on there and then you get people join and run your program and they give you a piece of cut of the money. Right. 30%, by the way.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Which is nothing. Right. They keep 70%. Thank you very much. Right. Like, yeah, don't. Anyway, so he's had his content on there for years and, you know, he's got like 10 or 20,000, uh, students, which as he explains in video, he goes through all the finances of it and he goes like, this does not make me rich. It didn't even pay for the development of the course because Udemy screw you on price and everything as well as your cut. So he gets about $4 per course sign up, which is like, anyway, nuts. But he just got an email from them. Udemy are changing their terms and conditions to now say that everyone who publishes content on there, it must be exclusive content with us. We own the rights to it.

**Chris Gammell:** Yeah.

**Dave Jones:** It's like bugger off. So if you've, if you're a, if you're thinking about using Udemy, don't. If you're, if you already have content on Udemy, remove it now before the July 15th deadline or whatever it is. Yeah. Just don't. That's just ridiculous. Sign over your content exclusively to Udemy. That's mad. Yeah. Madness. Yeah. That's anyway, that's a dumb, that's a dumb move. That's a dumb move. So, yeah. And he's, you know, rightly upset about this. So.

**Chris Gammell:** Yeah. Yeah. Yeah. That's, uh, that's rough.

**Dave Jones:** Yep. So, because apparently like one, one of the crux of the things is, okay, right. He's got paid courses on there, but he also offers some free courses on there and he's got a free course on there, which Udemy actually promote to buggery. Right. So like everyone looks at his free PCB tutorial, no, Altium Designer course on there, I think. And a free course. So they promote that. He, he's never earned a cent from that. And now they're demanding that they own the rights to that, that he's never earned a cent from. It's like, gotta be kidding. Yeah. Yeah. Anyway, that's just ridiculous. So I wanted to point that out. So go watch Robert's video. We'll link it in down below.

**Chris Gammell:** Yeah. And if you're thinking about Altium training, I think that's a, you know, it's basically it's him, him and the actual like official Altium training. And I think that he does some good stuff. So we highly recommend it. No, no. His, his isn't official. I'm saying there is official Altium training. Yes, there are. Yeah.

**Dave Jones:** You can pay to go through Altium.

**Chris Gammell:** Yes, exactly.

**Dave Jones:** Altium's approved courses, or you can, yeah, take Robert's. I don't think there's anyone else who's offering that.

**Chris Gammell:** Right. And he does more like in-depth stuff too, like the, taking it actually through development of a board and stuff. So that's cool.

**Dave Jones:** Oh yeah. And not just any board, but a high end DDR3, DDR4 processor, like, you know, really high speed. And yeah, IMX6 processor and the whole works, right? So really complex stuff, really complex project. He takes you from soup to nuts straight, you know, all the way through. So that's why it took him a year. And he says $100,000 to actually develop that course. Yeah, I believe it. So that's, that's there. Totally. Absolutely. It can cost that much easily.

**Chris Gammell:** Speaking of big dollars, I was, I've been thinking about, so after we had Pete on the show a couple of weeks ago, Pete Bevilacqua, who was the antenna designer, I've been like, and I've been doing my RF research and stuff like that. And I was like, you know, I wonder how much it would take to buy. And so Pete developed an open source VNA that didn't actually make funding. And so it didn't actually get made. Oh, okay. And so I started looking around. I was like, well, what actually else is out there? Because, you know, is he the only one that's done this? And it turns out there are others out there. And so you and I were talking a little bit before the show about like, you know, is it better to do like a low end? And I was asking about this on Twitter too, of like, is it better to do a low end type of thing? Or is it better to kind of dive into the used, the used equipment market and hang out on the

**Dave Jones:** Yeah, talking about a VNA here, a vector network analyzer. And you're talking about three gig. You're not talking about like 20 megs. Right.

**Chris Gammell:** I'm not in Shariar territory yet, you know. Right. Because he just did a review actually about some like that custom kit for like an old HP. It was like an add-on.

**Dave Jones:** It was a 30 gig or something.

**Chris Gammell:** It was something. It was something. He does these. Very crazy.

**Dave Jones:** He gets these insanely high frequency.

**Chris Gammell:** No, I think it was more than, I think it was 80 gig. I think it was up in like the. Right, right. Yeah, it was like radar territory and above, I think. Right.

**Dave Jones:** Yeah. Insane.

**Chris Gammell:** Yeah. But we were talking.

**Dave Jones:** And he gets these. I don't know how much he buys those broken bits of kit on eBay for or where he gets them from, what auction house he gets them from, busted. But he actually repairs these like, you know, 30 gig, 80 gig. Yeah. Uh, things. And then he's got this, you know, $200,000 bit of kit sitting in his lap.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, I don't know how much he bought it for broken, but.

**Chris Gammell:** Uh, he said, he said in the video, I think it was like $6,000 or something. Oh, I was going to say. Because he was very.

**Dave Jones:** I was going to guess five grand, you know.

**Chris Gammell:** Yeah. Yeah. He was very thankful for the, the Patreons. He had, he had thanked them for that. So. Right. Oh, okay. Right. I hadn't actually watched it. It was still like a lot. It was still quite a lot.

**Dave Jones:** Yeah. Yeah. That's a huge amount to, you know, buy a broken one and hope that you're going to cross your fingers and hope that it's not the. Right. You know, the, uh, you know, the $50,000 magical component in there that you can't buy, you know, that's broken. So. Yeah. Maybe it's.

**Chris Gammell:** Maybe it's this one. Maybe the, maybe it's 13.5 gig. Maybe I'm wrong about this. Anyway. I don't know. But it's one of his recent ones. Yeah, 80 is pretty specialized. Yeah.

**Dave Jones:** Yeah. Anyway. It's. Very cool.

**Chris Gammell:** Yeah. So you were saying though, um, that I should, you know, we were talking a little bit about like auctions and stuff like that as well, because, and actually, uh, Derek, past guest for the show as well. Um, Derek Cozzell was, he had, he had recommended this really good document to me on Twitter about like, uh, the 8537, I think it is, uh, which is a, uh, classic. I don't know.

**Dave Jones:** Yeah. It's a, it's a high to pay classic. Yeah.

**Chris Gammell:** And, uh, and there's a bunch of different kits and add-ons that you can get for it. Uh, and I started looking at it and it actually does make sense. In a lot of ways, the, um, you know, like I think it was like, I think I saw one for like $1,500. Uh, but you know, a lot of it too. Like, so like I am not the kind of person that is on the EV blog forum nerding out about this stuff. Like, like all the, you know, like. Well, you should be. I know.

**Dave Jones:** Cause that's, that's, that's the place to be. Oh, that's totally the place to be.

**Chris Gammell:** That's the first place I checked too. Um, but.

**Dave Jones:** And the buy sell section on there, I regularly post links to auctions. You almost, usually in the U S. Yeah. Um, you know, where they just like clear, like these whole factories and labs shut down, you know, they shut down the Nokia labs. They shut down some RF. Man, they shut down some chip manufacturer and you just get all these like high end VNAs and stuff. And they've got dozens of them on there. And like you can, that's where you pick up, you know, uh, decent. Be careful though of the, you know, the 15% buyers premium and all that sort of jazz. What does that mean? The secret. Oh, well these, these auction houses, not, you don't just only pay the auction fee, but then there's a buyer's premium on top, which is their fee.

**Chris Gammell:** Oh, really?

**Dave Jones:** It's actually called a buyer's premium.

**Chris Gammell:** Wow.

**Dave Jones:** And yeah. Oh yeah. And it can be 15, 20%. Oh yeah. 15. So you think, yay, I nabbed my, you know, $10,000 instrument for a thousand bucks. And then you realize that it's, you know, a 20%, 30% buyer's premium. And you've got to fork out another, you know, you can fork out 1500 bucks or something. Mm. Yeah. So yeah. Yeah. Just be careful. Okay. Yeah. Or buyers. Yep. Traffing young players.

**Chris Gammell:** See, I think the thing for me is that like, so I'm still new enough in this stuff that I want to buy something like I know works at first. Like I think that for sure. Yeah. Like my first scope shouldn't have been a broken scope. It was, but it was, it shouldn't have been a broken scope. Right. Because then how, how do you, I think your first scope should be a working scope, maybe a low end working scope. And then you use that to, then you buy your second scope is broken and then you've used that to fix the second scope. You need, you need visibility into that thing and some kind of reference. Yeah.

**Dave Jones:** And that's what I'm hearing lies the problem in that if you buy something on eBay, right, you're, you're either buying it as is, or you're buying it from one of the refurbished test equipment sellers and they will test it. You can be pretty confident, right? If they sell it, but you're going to pay a premium, like a real, like a double what you'd pay for just some individual person selling their instrument as is, right? It's like, oh, it powers on, you know, and they show a few waveforms or whatever and it passes some self-test and you go, okay. You know, you've got to at least have like, it's passing itself test. So the good thing about these instruments is that they, they do have comprehensive self-test built in. So if it boots up and passes the self-test, then, you know, you can, you can be reasonably 80, 90% confident. It's going to be at least work, you know, usable. Um, or as I said, you go to these auction houses and when these labs shut down, right? They, they literally have dozens of these high-end instruments in, uh, test racks on, Yeah.

**Chris Gammell:** With cow stickers.

**Dave Jones:** On the production floor with cow stickers and everything. Right. Yeah. And yeah. So you can buy one of those pretty confidently unless it looks like it's beat up or something like that, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Um, then you can, yeah, you can pretty confidently. They're just, uh, as is pulled from working environment, you know, that, that, that, that, that, that, don't, don't trust an individual seller on eBay when they say pulled from working environment. Cause you know, but, but these, uh, test equipment, um, auction houses, when an entire factory shuts down, then yeah, you know, you're almost like 99% confident that suck is going to work. Got it. Okay.

**Chris Gammell:** Yeah. Yeah. And then if it doesn't work.

**Dave Jones:** Especially if they've got 10 identical ones and they all came from these test racks. Yeah. Guaranteed.

**Chris Gammell:** Got it. And then if it doesn't work, you, uh, stick it on eBay and you say, pull it from working environment.

**Dave Jones:** Pull it from working environment. That's it. And you resell it. Yeah.

**Chris Gammell:** Yeah. That's the thing. I mean, I think like I've never really dove into that world. Like, you know, like I was very lucky to have access to stuff. Um, uh, but, uh, now I don't. Yeah.

**Dave Jones:** Now that you're on your own. Yep. Yep. That's the thing. Yep. It's. And your, your, you know, your wanky, uh, uh, pack a space that you're living in now, whatever it's, sorry. What is it? The workspace. Yeah. The workspace. The shared workspace.

**Chris Gammell:** They don't have one. I don't have V&A. I'm trying to convince them to, you know, and that's.

**Dave Jones:** Right. I had to convince them that nobody else would ever need a V&A, but you know, you need one. So. No, no, no.

**Chris Gammell:** I'm trying to convince them. Everyone needs one. Don't kid yourself.

**Dave Jones:** Everyone needs a V&A. Everyone needs a three, three gig V&A. Of course. Yeah. Of course. Of course. You know, to develop their new internet of things like that.

**Chris Gammell:** Well, I think that actually is a decent, uh, uh, that's a decent thing there to, to say like, oh, well people, you know, there's RF all around us.

**Dave Jones:** All these start up. Yeah. That's right. Yeah. You've got to, even though we just talked about everyone just buys a module and plugs in and it works, you know.

**Chris Gammell:** Well, yeah. Yeah. That's true. That's true. Oh, boy. So there is one, I will say there's one that kind of kept coming up, the mini V&A tiny. Uh, it's like three 50, uh, depending where you get it. It's from China. It's, uh, yeah. So that's, that's the one that kind of kept coming up. I had actually wondered about this other one out of Germany. Um, it's called the pocket V&A. I'll, I'll link to both of them. I, I'd love to know if there's people that are actually using these things. I'd love to know just because, you know, three to 400 bucks, it's not a ton of money, but it's also like, I'd love.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yeah. But you can, I don't know, you can have a go, I guess at that sort of price. You could. Yeah.

**Chris Gammell:** Yeah. It's definitely much more, um, much more doable. So.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. And, you know, like it's just for like doing matching, uh, you know, like, uh, uh, transmission line stuff and antenna stuff and things like that. So.

**Dave Jones:** Right. Yeah. So it's not for full characterization and, you know, all that sort of jazz. Right. It's just. Right.

**Chris Gammell:** Yeah. Right. Yeah. And so like the things that people kept asking me to are like, what are the frequency you need to do? And then what is like the dynamic range you need? And, uh, uh, uh, so like the pocket VNA does 40, 40 DB up to gigahertz. It said. And then the other one I think is the same range. I think that's the thing. Like if you're getting like an old HP one, you'll get like maybe like 80 to a hundred DB of dynamic range. Whereas like, you know, in these little handheld things, I don't, I don't think you're going to get it.

**Dave Jones:** So, um, uh, 70 DB at 500 megahertz for the mini VNA tiny.

**Chris Gammell:** Right. So.

**Dave Jones:** So they don't give you the spec at three gig. They only give you the spec at 500 meg. Yeah.

**Chris Gammell:** If I could say it goes, yeah, it goes up to three gig.

**Dave Jones:** Do they even have performance plots for that? Right. Do they even, you know, probably not. Right. And it's like, right. Yeah. It'll go up to three gig, but yeah, you've got to practically shout into the thing to, you know, to make it work. Right. Yeah.

**Chris Gammell:** So if there's other suggestions too, I'd love to hear too. I mean, um, I think this is one of the things like where it is quite specialized equipment and you know, not everyone's doing it and that's fine. Uh, but I'm trying to. Yeah.

**Dave Jones:** They're very obscure bits of kit VNAs, Vector Network. Yeah. Yeah.

**Chris Gammell:** I think until, I think I've never needed them until RF stuff. So something new. So we'll see. We'll see. Cool. Excellent. What else is on our list? Anything else? Yeah. A couple of other things here. Oh, there's a talk, actually another teardown talk. Uh, there was a really good talk by Kate Temkin about, uh, a new tool set that, uh, she's working on for like, uh, there's a new set of tools. So we had, uh, Travis good speed on the show a couple of shows ago. And, uh, and so he was talking about the good fat, which is now the great fat made by great Scott gadgets. Um, and Kate works for great Scott gadgets doing the software for this. Basically it's a, it's a debugging thing. So this is something that you and David might want to look at Dave. Um, I, I've never looked at USB packets personally. Um, I don't, I don't know how they work. I don't know what I just kind of plug it in and I just cross my fingers. Uh, but this is actually a new set of tools that without having to buy, um, a USB analyzer.

**Dave Jones:** Yeah. Yeah. Exactly.

**Chris Gammell:** So like, those are like, it's not terrible. It's like 1200 bucks. Like it's, it's a lot, but it's not, you know, it's like if you were, if your entire team was doing it, you need to buy 10 of them. That would be pretty tough. But, um, uh, but this is now, uh, some of the tools are out there and Kate gave a really great talk.

**Dave Jones:** So, um, that, that's something the market is missing is, you know, decent low cost USB debugging tools. Because if you have to debug it, you have to debug it. Exactly.

**Chris Gammell:** Exactly. Right. It's like, yeah. Like what are you looking at in a scope and you're like, oh look, there's, there's a bunch of squiggles.

**Dave Jones:** Yeah. There's no point. Yeah. No, you've got a, you've got a depacketized that, you know, you've got to decode the whole thing, every single, you know, element of the USB protocol. You have to have, you know, hardware, software solution that decodes all that often in real time. Right. Right. Right. Right.

**Chris Gammell:** And if you're like, if you're just like looking at the, you know, like what is your OS doing and is it like, is it enumerating? Is it like figuring out what device it is? Like this is a problem I had when I, one of the dev boards that I had, it's like, you can look in the OS and it's like, yeah, it says, oh, there was an error. It can't enumerate. But like past that, it's just like, oh, I guess I just like swap it out and try again. You know, like you don't actually know, like, is it giving all the things it should be, you know, is it, is it actually announcing itself, it's device ID and all that stuff. So digging in is a lot tougher.

**Dave Jones:** And the problem is, is that they keep bloody upgrading USB. So it's like, oh, okay, like, like 15 years, 20 years ago or whatever, like a USB one protocol analyzer was like, wow, that was like a real expensive high end bit of performance kit. Right. And then USB two came out and go, oh, well, I might as well toss my USB one thing in the bin. Right. It's useless now. So yeah. And then USB two is like, what's the speed of USB two for 400 megbits per second or something. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And that, that actually requires a lot of hardware to decode that in real time. And, you know, so that's difficult.

**Chris Gammell:** Yeah. Like the high speed, there's like full speed and high speed stuff.

**Dave Jones:** I think high speed is the full speed and high speed for a couple of megs. Right. Yeah. I think so. And, and, and yeah, so I've got a USB two protocol analyzer. Oh, you do. Okay. And yep. And it's totally useless. We're using USB three now for the micro supply. And David was complaining the other day that he didn't have a USB three protocol analyzer, you know?

**Chris Gammell:** Oh, you guys are using like the full data rate and everything too?

**Dave Jones:** No, we're not, but you've got to decode the protocol. So if you buy a protocol analyzer, it's going to support the full speed, whether you like it or not. Right. That's the, you know, that's just the way it is.

**Chris Gammell:** I'm so out of my element. I don't even know what these things are. So, yeah.

**Dave Jones:** So I don't know the intricacies of the USB three thing, but anyway, yeah, no, you've got to toss your USB two development tool out and you've got to get a new USB three and that's, you know, some real expensive high end hardware. So I'm not sure what this video covers. Is it like what these tools cover? Is it USB three or is it two?

**Chris Gammell:** It's like how the actual software tools tool chain is like working in then like a new interface for looking at it. So it's, it's super cool. I highly recommend it. It's a, it's a, it was a very good talk. Very engaging. Yep. So. Great. Yeah.

**Dave Jones:** If you need that stuff, you need it. Yeah. You really do. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. But once you're down that rabbit hole, good luck. You're, you know, you're in a world of hurt. If you, if you have to break out your USB protocol analyzer, you're in a world of hurt. Murphy's got to beat the crap out of you.

**Chris Gammell:** So. Yep. Yep. How about this last one? We do the open source multimeter. You want to, you would, you took some interest to this.

**Dave Jones:** Yeah. There's an ulti. So once again, the, the question is why. Sure. You know, yeah. And they actually cover that because it's there because it's there. And, and once again, the first thing that they cover on this, sorry, who's, who's done it? So we can credit the Martin.

**Chris Gammell:** Yeah.

**Dave Jones:** Martin. I don't know her last name. It's just Martin who's done it on the embed blog. Anyway, post link to it. Um, STM 32 open source multimeter. And yeah, one of the things he had, the first question he answers is why. Yeah. And it's like, oh, well, because I wanted to. Yep. And, uh, you know, he's talking about, oh, I can measure power. So voltage and current at the same time, you know, stuff like that. And, and he's got like a 3d printed case and it's got a little dot matrix screen on. It's got, it kind of looks like a multimeter without a range switch. Kind of. Yeah. Yeah. Sort of, you know, and it's, yeah, it's one of these things. And I've been, uh, like discussing open source multimeters for people with like for probably 20 years back on the Oz Electronics and Psy Electronics Design Usenet groups. Right. It, it like, it dates right back to then. Everyone has the dream of, you know, uh, designing their own open source multimeter back before open source was a thing. You know, you, you wouldn't use the word open source. I want to design my own multimeter, you know, and then it's open by default, you know, kind of thing. And, uh, yeah. And it's one of those, they always, it's such a complex thing that, yeah, you have to ask why. And it's like, just because you want to is the only answer. Uh, yeah, I think so.

**Chris Gammell:** I mean, I think the hope is that the longer term it'll build on itself and that kind of thing. But, um.

**Dave Jones:** Yeah. But then nobody wants, and then everyone has a different, the problem is, you know, even if you have like on the EV blog forum, world's biggest test equipment, nerd forum, right? With so many people.

**Chris Gammell:** What? Sunday, Sunday, Sunday. Join the EV blog forum. Go on. Join today. Go on. Don't delay. That's right. As Lewis Rossman would say.

**Dave Jones:** Join today. Don't delay. Okay. And, uh, yeah. Anyway, they're right there. So many people have gotten on there. I want to design my own open source multimeter. Everyone goes, great. Let's design it. Let's design it together. And then all hell breaks loose. You know, it's like, it's fun to watch. You just grab your popcorn. That's right. And just watch, watch them tear each other apart because everyone wants something different. Yeah. You know, it's, it, it, it never works. It just.

**Chris Gammell:** Well, I think there's the, the collaborative hardware thing is tough too, but yeah.

**Dave Jones:** Yeah. Yeah. Yes, it is. As I always say, one person has to drive projects like this. It has to be ruled via a dictator. One person, you know, uh, yeah, it does it. Yeah.

**Chris Gammell:** I think, I think, I think that's the 80% rule at least. Yeah.

**Dave Jones:** These open source hardware things never. Yeah. Well, sorry. Open source collaborative projects, you know, from, yeah. Everyone just wants something different. Yeah. Yeah. So there's, there's just no point. Even if you agreed with all the specs up front, you know, and like you, you, you can't even do that. Yeah. Right. It, it just doesn't work because you go, oh, well, we can't do that because well, that spec, if we lower that spec by, or if we increase that spec or whatever, widen it by 0.1%, we can save an extra 10 bucks in parts. Right. And you know, you always have to be willing to be flexible.

**Chris Gammell:** Yeah. If it makes people feel better, uh, having worked at a test equipment company, it's exactly the same there. It's just, there's more on the line because people's jobs are actually dependent on it too. Exactly. So it's, it's, it's, it's, it's much of a shit show. So if not more.

**Dave Jones:** Right. But somehow you get it done because it's your professional job. Sure. Yeah. Yeah. Yeah. Right. Eventually. As you said, your, your livelihood depends on it. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** So this is a great little project though. I like it. I like it.

**Dave Jones:** Anyway. Yep. Yeah. So, yeah. Sorry. It just, I, I just chuckle inside every time I see open source multimeter because I've been dealing with it for 20 years.

**Chris Gammell:** I mean, I think at the end of the day, like, I think like the things that I think about with multimeters too, it's like you need good, you know, good non-drifting components is very important as that makes it expensive. Even if it is open source, that's what ultimately makes it expensive. Any test equipment has, you know, purple screws like that. And then like good protection, no matter what.

**Dave Jones:** Well, that's the first thing I think about when I think about multimeter. Two things I think about, safety, reliability. Yeah. Right. Confidence. Yeah. Right. Measurement confidence. Yeah. Exactly. Exactly. You don't want to think you're going to want the second thing next to it saying, no, that's wrong. Yeah. Yep. Yeah. It's, it's safety and measurement confidence. And it's like, yeah, a proper multimeter is all, yeah, certified. You can plug it into mains and you know it's not going to explode. Right. Or if it explodes, it's, it's contained inside and it's not going to blow your hand off when you're holding it.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** That kind of thing, you know, it's one of those. Yeah. Anyway. Yep.

**Chris Gammell:** I forget who I was talking to the other day. It was a couple of days ago, weeks ago. Time has no, time is a circle, Dave. I don't remember when I was talking to this person, but they were talking about the cost. Was it on the amp hour? Good Lord. But they were talking about the cost of, of, you know, standalone ADCs. Was that on the show? Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** And like how there's a bunch of micros now where the cost is, you know, the ADCs are good enough that there's a micro in there. They were using it as, um, using it for the micro internally. Like versus the, sorry, for the ADC internally.

**Dave Jones:** For the ADC. So they were using it as they were using a micro just as an ADC.

**Chris Gammell:** Yeah.

**Dave Jones:** Who was that? Right. Like a via the SPI interface or something like that.

**Chris Gammell:** Yeah, exactly. I mean like, well, I think it's just. Yeah. Why?

**Dave Jones:** Because it's cheaper? It was cheaper. The ADCs in, right. The ADCs in micros are usually a bit.

**Chris Gammell:** Yeah, I agree. I agree. I agree. But this, this particular one. Okay. Yeah.

**Dave Jones:** Right. No, you're always going to meet some, there's always going to be some sweet spot where yes, it's going to be cheaper and better. Yeah. Just, just to do that, that, that doesn't surprise me. Yeah.

**Chris Gammell:** I just think about like, like when I start like thinking about like going down the line of like things that start to trip people up in, in test equipment too, like it eventually gets to the ADC. That's why I was thinking about that as well. Yeah.

**Dave Jones:** So, but it's always specific. You can't just go, oh, micros, you know, micros with ADCs are going to be cheaper than an ADC. Yeah, of course. Of course. That's just like rubbish, you know? Right. Yeah.

**Chris Gammell:** No, yeah. Then the really crazy people are like, yeah, I'll just build my own ADC. What could possibly go wrong? Yeah, right. Yeah. The current source is doing that right now. The YouTube channel. Yeah. Oh, is he? Yeah. Okay. Right. Yeah.

**Dave Jones:** Great. Love it. We didn't talk about Maker Faire laying off all this stuff, did we? Yeah, we did last time. Yeah, we did that two weeks ago. Okay. Yeah. Done. Okay. All right. All right. They're still laid off if that's the thing. Yeah. Yeah. Yeah. They're still laid off. Right. Yeah.

**Chris Gammell:** Sorry.

**Dave Jones:** Have you heard what's happened to the IP?

**Chris Gammell:** No.

**Dave Jones:** No? Okay.

**Chris Gammell:** Oh, I thought you knew. You were just asking.

**Dave Jones:** No, no. No, no. Got it. Got it. No, sorry. Yeah. Simone Gertz made the Tesla the truckler. Oh, man. That was cool. That was. We won't go into details, but that's awesome. If people haven't seen that, it's fantastic. When I first heard about that, I thought, oh, she's just going to hack this thing. It's like, no, she got a proper team together. They hired a warehouse and they shot this professional commercial for it. And it's like, holy crap. Like, I actually ribbed her when she said on Twitter that she bought a Tesla. Oh, yeah, yeah. And, you know, and I didn't know. Like, apparently nobody knew she was buying it for this specific purpose to chop it up.

**Chris Gammell:** I remember her tweeting about that.

**Dave Jones:** That's why she bought it. Yeah. That's why she bought it. Anyway, that was very cool.

**Chris Gammell:** What did you say? You said, like, don't turn it on, take it apart, that kind of thing? Or what?

**Dave Jones:** No, I said, because she's the queen of shitty robots, right? She builds shitty robots. That's what she does. And my tweet was, like, tongue in cheek. I couldn't help myself. I thought it was so hilarious saying, oh, I thought you built shitty robots, not bought them.

**Chris Gammell:** Oh.

**Dave Jones:** And it was like, you know. I think the Model 3 is nice. Yeah, it's very nice. You're just jealous.

**Chris Gammell:** You're just jealous you can't get one.

**Dave Jones:** I'm just having a poke at all the Tesla fanboys. And it got a great reaction. It got the, you know, I was trolling. Yeah, of course. And I thought it was brilliant. And everyone, most people got my troll. Everyone went, oh, thumbs up for the troll, Dave. Yes, right. And, you know, most people got it. Classic Dave, yes. Anyway, yeah, I thought it was funny. It was a joke.

**Chris Gammell:** Of course, of course. Yeah. Anyway, yeah. That deal was really good.

**Dave Jones:** Yeah, she was buying it for that specific purpose. So, yeah, it's very cool. Yeah. Yep, that's great. I hope she got her money back. Like, I hope the advertising revenue for the, you know, millions of hits she got paid for the car. Maybe. If it gets, like, five, ten million hits, it'll probably give her 30 grand in ad revenue. So, you know, yeah, it could pay for it, maybe.

**Chris Gammell:** Yeah, hopefully.

**Dave Jones:** Yeah. Yeah, maybe. I haven't checked the numbers on the video. But, yeah. Yeah, definitely. Hmm. Oh, yeah, she's got seven and a half million views just on the build video.

**Chris Gammell:** Yeah.

**Dave Jones:** Just on the build video. So, that's impressive. So, if I search for, hang on, I've got to do the, hang on, one minute, her video, five. Oh, she's got more. That's interesting. Wow, I didn't expect that.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** She's got more views, 7.5 million, compared to 5.3 million that she got for that real polished one and a half minute commercial. Yeah. That she put together. I thought that commercial would have gone gangbusters, right, would have been shared to the hill. Whereas more people watch the 31 minute build video. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** Wow. Okay.

**Chris Gammell:** Good job. That's interesting. Good job, public. Yeah.

**Dave Jones:** Yeah, good job, public, for watching the whole, you know, for wanting to watch the 31 minute and sharing the 31 minute build video. Oh, no, I know why. Of course. Duh. Full-time YouTuber day, of course I know this, is because YouTube do not value a one minute, 46 second video anymore. The watch time isn't there. Mm-hmm. Right, right. Right? Yep. And so therefore, boom, it starts accelerating in the YouTube algorithm and that's what snowballs it. Mm-hmm. So it might have even started off with one-tenth the number of viewers as the commercial, but in the first day, for example, it might have got one-tenth the number of views, but the algorithm accelerated that because it had 10 times the watch time. Mm-hmm. Yeah. So, yeah. And there you go. Interesting. So, hang on, I'm just doing some calculations in the back. Like, 14 times two. Yeah, she probably would have got, maybe if she's lucky, got close to 30 grand for those two videos in ad revenue. Yeah. So, it's close to paying for it. So, cool. That's great. Cool. That's great. I don't want to be out of pocket, but she has a truckler now.

**Chris Gammell:** Yeah.

**Dave Jones:** So, it's its own reward, really. Yeah, yeah, yeah. It's its own reward driving that baby around. Yeah. That's great. Anyway, we're way over time. We are. That's it. All right. Full of quits.

**Chris Gammell:** See you in a couple weeks.

**Dave Jones:** Catch you next time.

**Dave Jones:** Bye.
