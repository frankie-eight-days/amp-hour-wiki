---
episode: 241
title: An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus
url: https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/
---

**Dave Jones:** Hey guys, this is the last episode of 2019, and we had a great year, lots of great guests, lots of fun recording with Dave and I, and we hope you enjoyed it as much as we did. We also recently asked everyone to fill out a survey, and about 800 of you did. We really appreciate that. We sent out some notices for all the people that won the drawing, and we'll be getting addresses and sending that stuff out soon. If you still want to help us out, you can always send a review on iTunes. That really helps us kind of stay up in the rankings, and you can always let your friends know about episodes, especially episodes like this one. Now this is episode 241. This is a repeat of a past episode, but it is unfortunately because Chuck Petal, the person we're interviewing here, has passed away. Chuck is the inventor of the 6502. It was the chip that started it all, you know, it was in early Apple, early computing stuff, and so this is a great episode to kind of learn about early history and what it took to get that chip made. We love this episode. It was so much fun recording with him. It is a three-hour episode, so I will warn you about that, but we thought it was good enough to actually re-air it here. And hopefully you enjoy it. You share with others. You let people know what a giant Chuck was in the electronics industry and how much he did for us. So rest in peace, Chuck. We really appreciated you being on the show and hope you enjoy this. This is episode 241 of the Amp Hour. Re-aired for you. We'll see you in 2020. This is the Amp Hour Podcast. Recorded March 18th, 2015. Episode 241. With guest Chuck Petal. Charismatic. Chipmaking. Corpheus.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Atari:** And I'm supposed to introduce myself now? That's it. Okay. My name is Chuck Petal. Born Charles, but nobody ever calls me that because I don't like it. And so if you look me up on the internet, my stage name is Chuck Petal. You should see a tap dance. What? And we specifically started this, I'm going to hopefully start this conversation with the beginning of the microprocessor industry. And so we can see how that evolved into the personal computer industry and to kind of where we are today. And I'm going to give a lot of credit to a lot of people as we go along. That's... Most of whom everybody's ignored. But I try to do that. That's what we want to hear about all of us.

**Dave Jones:** Yeah. Exactly.

**Atari:** Well, not just stories that, you know, you'd only... You do things like this with small teams, right? Big teams are not very effective. And so you have small teams. And what happens is, is you get a guy like me that's doing some of the marketing and everything else. So I get all the credit. And yet there's guys who never got any credit, but who in fact created a lot of the pieces of stuff. So I make a point of trying to explain why they should get the credit and how we did certain things. Okay. Gotcha.

**Dave Jones:** Well, we should say as well that what Chuck is kind of dancing around here is that one of the products that he's very intimately involved in was the 6502, which enabled things like the Apple II and the PET, which is the Commodore PET and a wide Nintendo, the original Nintendo and a wide range of other things. And that is why we asked him here.

**Dave Jones:** A bunch of them. We could say, I think it's fair to say, Chuck, you are one of, if not the father of the personal computer. Is that too embarrassing to say?

**Atari:** No, no, not at all. I claim that title, even though Steve Wozniak keeps going around and stealing. Awesome. We can get into that. And I can tell you the stories about Wozniak and why he shouldn't claim it. Oh, yes. All right. But, no, we, I'll give you one minute history and then we'll talk about each piece.

**Dave Jones:** Okay.

**Atari:** We did the 6502 because, and I'll explain why we did that. Okay. While we're in the process of introducing the 6502, we got into the video game business with Atari, right? And that became an enormous business for everybody. Yep. And during that period, there were a bunch of people that were making what were called board game, board computers actually were for technicians to build their own. And there was an Apple II and there was a, but more important was Dr. Sittling, which created that market. And we had a whole bunch of programmers that came to us and said, we don't want to build our own computer, but we really want a computer. And we kept listening. And finally we decided, okay, we'll go build the computer. And we called that product the Commodore PET. And it, I'll show you why it was the predecessor for everything else. And then we got the PET into production and then we built a second product called the VIC-20 and the C64 and we'll explain how those evolved. And during that period of time, we explored how we would do the next generation thing because none of those computers were strong enough to be what ultimately became the personal computer. Right. Right. And so we-

**Dave Jones:** And that gets onto the VIC-20, correct?

**Atari:** Yeah. So we did, we did the first MS-DOS machine outside of IBM. And we'll explain that for a minute as we go by. And we won computer of the year over the PC that year.

**Atari:** And we outsold the PC for two years. So we really started the PC business also. And then we-

**Dave Jones:** I always forget about that, that the PC was actually, that was like an IBM term, but then that got co-opted broadly, right?

**Atari:** Well, what happened was a bunch of guys and Ben Rosen and encouraged some Texans. They kept telling everybody you have to be exactly compatible with the PC. And the reason is because Ben had just gone out and started a funny little company called Compaq.

**Dave Jones:** Oh, yeah.

**Atari:** And the guys at Compaq wanted to build a TI type machine because they were all out of TI. And Rosen said, okay, we'll give you the money and we'll support you, but only if you make it exactly like the PC. And because he did that, then these guys could go out and say, well, you have to have a machine exactly like the PC. And so we went from a product that actually failed, the original PC, to the product that everybody thinks was created by IBM and the whole world did. But in fact, there was so much creativity going on there in the time that were derived from the fact they were trying to make something like the PC or basic MAMOS DOS machines. So ultimately, we got down to calling them PCs. And I'll tell you briefly as we go along with the history, we broke the chain where everything had to look like the old ugly PC, right? Got it. And that actually lasted for about five years, right, until we broke it. Terrific. So let's start in... We believe our team, my team won computer of the year four times. Nobody's ever run more than once with us.

**Dave Jones:** Fantastic.

**Atari:** So we're very proud of the fact that we think we created that business. Okay.

**Dave Jones:** Well, let's start in 1973, shall we? This is after you left General Electric and you moved to Motorola, correct?

**Atari:** Yeah, basically, it was kind of a funny deal because while we were at GE, we came up with the idea of a concept called distributed intelligence. And it was because I had been briefed on what was happening at Fairchild. So I knew the IC industry was about ready to take off, right?

**Dave Jones:** Right.

**Atari:** And communications had started to happen, right? I mean, this is 1970. Communications had started to happen. And there was no internet or anything, but we at least could talk to things over telephone lines, right? Right. And we actually worked on a product that was a very, very centralized server-based sitting in the office kind of cash register. It was written for a design by someone.

**Dave Jones:** I was going to say, you basically invented the cash register.

**Atari:** Yeah, the first one these guys did, right, was a very online system. It was called Tradar. And we took a look at it. We actually were involved in the same group and we have them do some work on it. But we took a look at it and we said, this is wrong. This is not the right way to do it. So a small team of I came down and we said, okay, what happens if we put intelligence into the devices? Now, today you guys only use intelligent devices. You've got a smartphone in your pocket. Okay. A little exposure. Okay. We put snappers. No, but my point is, is that, you know, you don't even think about it not being distributed intelligence, right? Right. But remember, that's at a time where people were still just barely moving away from phones that you didn't need an operator to plug in, right? So they built this computer. I just love to tell the story because it's funny. Please do. These guys built this machine that in order to, when you typed on a key in a retail establishment, you went over the phone line, went to this little central device, and then the central device went back and told it, print on the screen. Oh, my God. That character. Just a single key. So just a single key hit you. Yeah, yeah. Yeah. So anything that went on always went back to the central device and back, and that was distributed. That was centralized intelligence. That's where time sharing was. That's where everybody had, people were moving from punch cards and fooling around with machines to the concept that you could go online and do things, right? And so, but all of the things you did something with, you had a little more than dumb a terminal. Yeah. And you talked to a thing that did something in time sharing. You were on a teletype and you went to a computer and all the computing was done on the timesharing system, right? And that's where the technology was in 1970, right? And we took a look at it and says, it's crazy. It's not going to work, right? And it turns out that we had, you know, I predicted it. We had come up with this alternate design for cash registers, credit verification, everything else, where you put the intelligence in the terminal. Okay? Got it. That's distributed.

**Dave Jones:** But that wasn't a microprocessor at the time because they weren't invented. No, no, no.

**Atari:** It wasn't a microprocessor yet. We just said we're going to put the intelligence there, right? Right. So it was a concept. It was a concept, right? A very important concept. But so anyhow, these guys hooked up. I don't know if you, well, you live in Cleveland, so you know. I don't know what they do in Australia. You practice Boxing Day in Australia, right? Yes. Yes, we do. Yeah. Okay. In America, the day after Thanksgiving is known as Black Friday. Yeah.

**Dave Jones:** Right?

**Atari:** And it's because everybody runs down to the store and buys all the stuff that they didn't want to buy, but they're going to buy for Christmas. That's right. Okay. Because it's hard to say. Okay. So they've got this alliance system hooked up in this store in Anaheim, California, and it's running to a server that's in the same general vicinity. And they're now running cash register, and it did a legitimate job. It would print and other things, and it had a little scanner, and it would scan credit cards. And it was a really well-done system from a conceptual standpoint. And the communication line between the two went down. Mm-hmm. Okay?

**Dave Jones:** A huge retail day. Yeah. Okay. Yeah.

**Atari:** Think of being in a store where you cannot sell anything on that day.

**Dave Jones:** They couldn't even accept cash. No.

**Atari:** It was just – there was a small rebellion against the product at that point. I suspect that if some of those people who were in that store could have gotten their hands on the engineers, they would have been dismembered. Right? I mean, it was just terrible. Right? And it kind of proved what we've been saying all along. You don't want centralized intelligence. It's not useful. Right? It's expensive, and it's not the right thing. So we got an opportunity to talk to Exxon, and they told us how they wanted an automated cash register and why. Right? I love the opening the guy did. He said, we are the most important industry in the world. Right? And as you know, there's been more swatting over the companies. You have to argue that he's not been very wrong. Okay. And he says, we're represented to our client by a pimply-faced teenager that doesn't know which end is up. Right? We want to stop all that. Right? We want to go to self-service gas stations, which, of course, they did. And we want to have it all automated by something that's in the pump. Right? Right. And local. And we talked to the guys at Visa who were starting the Visa credit card. And they said, we need –

**Dave Jones:** It was that early, was it?

**Atari:** Oh, yeah. Just 1970 was all – 70 was a really important time because we were swapping from – the distributed intelligence thing, centralized intelligence thing was strong enough that you could start Visa. Right? Right. And you could go online and get – right? I mean, it didn't work – it wouldn't have worked long-term, but it did. Right? Right. We just slightly progressed from plugging in the phone lines to having some level on missions. Okay? No, and we actually had done things like magnetic checks. Right? And you could scan a credit card and read it. You know, those kinds of things were happening. Right? So – but we got a chance to see this entire market and see that if we did some distributed intelligence machines, we would have an enormous company. So we went out and started a company called Intelligent Terminal Systems. And we built a demo. And just to put it in perspective, the only DRAM I had in that device was 8K shift registers. Okay? Oh. Because there were no RAM devices around. But 8K was a lot. Yeah. It was a special product from Nationals. They'd invented it. And you put one each in. And my technician the other day was one of my investors in my new company was reminding himself that they came in a can. It got hot. Right? Right. Anyhow, the point was – It takes about 4 amps, right? Right? Yeah. Yeah. So the point was is that we did this little terminal and proved that the concepts were going to work. But we couldn't get venture capital funding. It was a time when getting venture capital funding in Phoenix was impossible. Right. So we kind of had to give up on it. And at that point, I had gone off and worked for a guy doing the first online typesetting system we did with distributed intelligence typesetting using the PDP-11. And we were actually setting type for the local newspaper and stuff like that. So we were able to get that level of peripheral working. And it was very helpful for me because I got to really understand the way the PDP-11 worked. And so what happened – I'm going to give you some more history here just so we can put it in perspective.

**Atari:** There was a – during this time, people were starting to go away from teletypes and looking to have something that was on their desk. It looked like a CRT to take a type on. It was really acting like a teletype, but it was a lot more elegant. Right? And they actually were smart enough that they'd type a key and put the key on the screen. But the point was is that these were called CRTs, and they were very important and starting to happen. And a company in Boston announced that they could build this really cheap – I think it was like $300 as opposed to $1,000 – CRT. And the whole world fell in love and said, you know, that's going to be the hottest company in the world. And so they did two things. They went to all the semiconductor guys and said, we can't do this without you doing a high level of integration. You've got to make us a custom chip for this and a custom chip for that. So people like Motorola said, well, that's such a great idea. We'll invest in it. Right? So Motorola created a new process and a new chip to do that. And so did everybody else. And about a year later, it came out that this whole thing was nothing but a big stock scam and they couldn't build it. Oh. So here's these semiconductor companies with these teams pulled together that have just finished these chips that nobody's going to buy. And they got a new process in place. And the guy who was in Phoenix that was in charge of that was named Tom Bettett. And he had come out of the calculator business. Right? So he had a pretty good idea about what a calculator ought to do. And he said to himself, I can do what we wanted to do in the Viotron if I make it into a thing called a microprocessor. And so he was one of the real pioneers in the microprocessor. Intel gets credit. They did a product called the 4040, which was nothing but a calculator. Just a calculator.

**Dave Jones:** Oh, the 400.

**Atari:** Isn't 4004? Yeah, I think it is. Something like that. Whatever it is. Right. The 4004 and then the I008. It was just a – and then the 8008 was actually done for a team of people I knew very well who bought and got it as a custom chip. And what they were doing is they were walking around stores typing in to a small terminal that they built around the 8008. And they were doing stock keeping in grocery stores and everything every night. And they were the predecessors to what they do today. But, you know, now they finally moved it back to the cash register. But at that time, we didn't have them at the cash register. So they would go around. And they actually created the 8008 as a custom for those guys. Right?

**Dave Jones:** But you don't think the 8008 was the first micro, do you? No, not at all.

**Atari:** Because it wasn't. Explain why? It was designed for this one application. Right. No, they started working on the 8080 at the same time Bennett started working on the 6800.

**Dave Jones:** He moved to Motorola, didn't he? So he – Bennett was at Motorola. Or was he already – oh, he was already at Motorola. He was at Motorola.

**Atari:** He was at Motorola leading the Biotron team.

**Dave Jones:** Right.

**Atari:** That's the reason I took it to the rest of the team that was – Yeah, they couldn't sell them. So they went, what can we do with it? All of a sudden, I've got this new process. I've got all this new capability. And Bennett's thought was that I could make a microprocessor. Now, I'm not sure what a microprocessor is. I know it's sort of like a calculator. And here's some of the things you have to do different than you do with a calculator. Because he knew calculators pretty well. And Motorola was in the same general vicinity. It's a company called General Electric, which I worked for up until then, who had gone out of the business. And a bunch of those guys had wound up in Motorola. And they wanted to build a minicomputer. Right? Right. His deck was really hot during that time. And the other day, the general –

**Dave Jones:** So Motorola, who were a chipmaker, wanted to get into the mainframe computer business.

**Atari:** Well, the marketing guys wanted to make the – The huge margins. They wanted to make a microprocessor. They wanted to make a minicomputer. And Bennett wanted to make a better calculator. Right? And so they actually fought most of the time about it. But anyhow. Yeah. So Bennett, somehow or other, I got my resume on his desk. And he called me in. And he said, listen, I know that you want to make your company work. And you can't make it work now because you don't have the equipment. But if you'll come to work with me and make the things that we need to do work, you can then spin back out and use them in your company. Well, given that I didn't have any income, that was a great deal. Right? Yeah. Right. So – Oh, I don't know. You're twisting my arm. I'll take it. Yeah. No, but no, it was a good pitch. He was a great guy. I mean, I really appreciated what he did. So anyhow, and he hired this one young engineer out of the other – Tucson University. And he was doing things like looking at the process to try to make it better. And he assigned him to me. And I looked at some of the instructions in the 6800. We made some changes. Like, for instance, I added non-masculable interrupt, which nobody gives credit for. But it's a very key thing if you're going to do things with pieces of hardware like that. And we changed the addressing some. But we couldn't make any major changes because it was pretty far down the road. It started in terms of being done. And secondly, I had these marketing guys that thought they were building a minicomputer.

**Dave Jones:** But the 6800 was mostly developed before you got there? Is that right?

**Atari:** It was partially developed, and I contributed. But what was important was a microprocessor without an I.O. device is just a current hog, right? Right. Hook it up, plug it in, and it just sits there and eats things and doesn't do anything. Because it can't. And you can't even flash a lead, right? Right. Right. Right. So what we did is we said, look, what we need is a universal I.O. device, right? And we invented it, right? It had programmable I.O. on multiple pins. You could go input, output. You could mix them together. We put edge detection in. And the product was called the PIA. And it was the thing.

**Dave Jones:** You invented the PIA. Thank you very much.

**Atari:** Myself and Bill, Bill Minch did the PIA. Because Bill was the process guy. And I would say, this is what I want. And he would go by and say, well, I'm not sure we have a circuit that can do that. And so he'd go in and create an edge detecting circuit, right? Because you needed all the things we put in there, right?

**Dave Jones:** Real quick, how is this? I'm going to get to play the dumb guy again. What was the option before? Did it have to go over a memory bus otherwise? It didn't anywhere.

**Atari:** Nobody knew what they were going to do with them. They were just building these things. They didn't have any idea. With no I.O. on them, yeah.

**Dave Jones:** No, no.

**Atari:** Nobody had any idea why they were building it. They were building it because they wanted to make a mini computer. Now, DAC understood I.O., right? I mean, the PDP-11 had great I.O. Memory managed I.O., right? But these guys didn't have a clue, right? So we took that job on, and we built it, and it worked. It was wonderful. Okay, now I have a PIA, and we've got the 6800 working. And so then the next thing that happened inside Motorola is they said, well, nobody knows what this is or how to sell it. So I did a class on the inside of Motorola explaining this is what it is, and here's how you sell it. Because with these two things, you can do distributed intelligent machines, right? That's all you need because you've got RAM and ROM already, right? And that's enough. You can make a written suit. And they said, so this class got to be a little famous inside the company. And one good thing that came out of that class edition, that was a guy by the name of Roger Camp from the University of Iowa, who fed me all of my great programming and engineers after that from Iowa. But anyhow, so because of that, the guys in the field said, well, we've got to go out and conduct. Our customers are asking us. We've heard we've got a microprocessor. They don't know what they can do with it, and they don't want it. So what they want to do is bring somebody in from the factory, and they'll bring all their engineers together, and you sit down and explain to them what a microprocessor is and how to use it. So I got to visit Hewlett-Packard, Tektronix, Bailey Instruments, NCR, Ford Motor Company. I got to all these places. Every time when I was there, I would have this classroom full of people who desperately wanted to believe this, right? I mean, there were the hot engineers in the company, and they really wanted to do something. They had read about it. They wanted to do something. So I would sit down and explain to them how you use the PIA and how you put the processor together. And then we'd get all done, and they'd say, that's a great idea. And the PIA were selling for $5 or something, right? They were selling the 6800 for $250.

**Dave Jones:** And they went, that's too expensive. The guy said, I can't make it.

**Atari:** We can't build that in your product. I can't do that, right, they said to me. And so I would get all these really smart, this room of really smart people, and I would say, okay, the reason that chips cost more money is because you put too many things in them. So what I want to do is to define the absolute minimum thing you need to make the microprocessor go with this nice little PIA because PIA was small and fast and cheap. And they would almost always agree on a small instruction set. Right.

**Dave Jones:** And the reason it was expensive is when you put more features in is because of the yield, right? The yield was incredibly poor.

**Atari:** It makes the chip much bigger and much more complicated. Yeah, no, it screws up yield totally, right? And so everybody, so I had like 10 of the top engineering groups in the country, all of whom agreed with me, okay? Right. And then it actually helped me do this. And Motorola found out about it, and so they wrote me a letter. And the guys who wanted to make the mini computer said, you're screwing up our mini computer program. So I went to the top management and got a marketing, I mean, a letter from top management that says, you have to abandon your work on that product and never mention it again.

**Dave Jones:** This is the low cost product you're talking about. Yeah.

**Dave Jones:** So you were doing the marketing, basically figuring out what was out there, and you were building this thing, and you were basically defining a product.

**Atari:** What I wanted to have. Yeah, yeah. I was going to build the next generation, right? Because that's what I knew we needed, and they knew what he needed and all that, right? Right. Which is going to be, what, one-tenth the cost? Yes, it was significantly, right? That was about the target? Yeah. And so Motorola wrote me this letter saying you have to stop working on it. So I wrote them back a letter that says, the laws of patents said you just abandoned the product, and all the work I've done on it belongs to me now, and I'm going to go off and do it myself, right? Wow.

**Dave Jones:** And they agreed to that?

**Atari:** No, but they later had to because it was true, right? Oh, okay. It was true. And so I put together a small team, and I went and sold the concept of doing this to the guy who was, I had worked for at Motorola, I mean at GE. He was the guy that did the original magnetic ink card reader system for Bank of America, right? Wow. Very smart guy, right? Yeah. He'd gone off and started a semiconductor company in upstate New York, and he had built the best calculator chips. That's what they were doing, the biggest, best, because he'd invented two or three major new process steps that gave him much higher yield. So here's a guy that knows… We're talking about MOS tech. No, we're talking about MOS. We're talking about MOS technology, right? Yes.

**Dave Jones:** MOS, yes. It's not MOS because that's not what you guys called it, is it?

**Atari:** No, I call it MOS technology because there was a MOS tech in Texas. So I actually talked to LJ7, who later on often was one of the founders of Compaq. He turned it down because he was afraid I was going to get sued by Motorola, which I wasn't. And so he said, no, I don't want to fight those guys. And Pavan didn't care because he had a calculator company, and he didn't have any major reason for them to beat him up. They tried later. But here I was just lucky because here's a guy that absolutely understood what I wanted about a low-cost microprocessor because he was a computer guy, right, and a major tech. And he was a great technologist. So he said, what I'll do is I'll build you the first 5-volt in-channel process, and I'll give you the money, and you put your team together, and we'll build this chip. So you left Motorola like a hot potato? I took his team out of Motorola. We moved into MS Technology. Six months later, we had the chip done and the process done. This is the 6500? 6502, right. Ah, well, 6501 at first, wasn't it? No, no, no. The 6501 was a game, okay? I wish to sign the 6502. Because we had come out of Motorola, we said we'll make a version of it that looks like the 6800 just for fun, just to see if people are interested, and some people actually bought it, but we were never serious about it, right?

**Dave Jones:** And that's what Motorola sued you for because it was pin compatible.

**Atari:** Well, no, they sued us because they wanted to stop us.

**Dave Jones:** Ah, right.

**Atari:** No, no, no. To tell you the story about Motorola's suit is very simple. When we – I'll take you through the rest of the history on the 6502 because it was really kind of fun. No, no, absolutely. Okay, so we got the 6502. We invented another one called the VIA, which was a better version of the PIA, and we built a ROM RAM chip, IO chip, that went with it to make a low-cost device, right? You put ROM RAM and IO on this one device, and then you put the 6502, and you put it in a small package, right? So it was very – all those packages back at that time were costing five bucks a package because they're in ceramic, and you could put the 6502 in a small plastic package with less pins and less addressing space and so forth, but it didn't matter because you didn't need it, right? So we decided that we wanted to get everybody's attention. And so what we said was you can go to this show in San Francisco, and we will sell you one microprocessor for $25. $25. That was unheard of. Compared to the $200 everybody else was getting, right? Yeah. $200? Yeah.

**Dave Jones:** This is what revolutionized the computer. The classical computer industry.

**Atari:** We knew that. Yeah, we knew we could build it a lot cheaper than that, and I'll explain that story in a minute. But anyhow, so what we said is we put it into all the electronics magazines, advertise, see us at this show in San Francisco, and we'll sell you a microprocessor because we wanted to prove to you that you can have one for $25. We're going to give it to you along with the programs and how to use it, right? Developments. And weren't there a lot of people who thought it was a joke? No, no, but it wasn't a joke. So what happened was the day before, about two days before the show, people at the show realized what we had advertised, right? And they said to you, you'll have to close down your booth. And I said, why? They said, because you can't sell anything on the floor. So I said, I'll tell you what. We went up to the St. Francis Hotel. We took over a great big suite, and we had done a development system for it. We had an online system. We had three local cards. We had done a whole bunch of support things. And so we took the suite over, and we showed everything in the suite. And then we sold the computers out of the suite. So people would come to the booth and say, we want to buy this. And they would say, no, you've got to go over to the MacArthur suite and buy it. And people would get on the bus and say, is this the bus that goes to the MacArthur suite? And so we had hundreds of people come through. So my wife was sitting up on the stage with a great big tall glass jar full of microprocessors. And the books beside it, and so she'd sell you the two books and the microprocessor. And if you went around the room, we could order it or some of the development stations and everything. And because we showed this big jar, everybody believed we had lots of them. And we did. But only about half of them worked. The bottom half were the reject.

**Dave Jones:** The bottom half were done.

**Speaker ?:** Right.

**Dave Jones:** I think when Bill was on the show, he mentioned that story as well. That's insane. Yeah.

**Atari:** Let's love it. It's all about image. Yep. Well, no. Exactly. If everybody walks up, gets one, right?

**Dave Jones:** Mm-hmm.

**Atari:** And then they believe that we have enough. And we really did have enough. It's just we didn't have enough yet for the show. We actually had to make it.

**Dave Jones:** Now, apparently the Woz turned up and bought one, didn't he? No. Was it at this show that the Woz bought one or was it a different show?

**Atari:** Actually, Steve.

**Dave Jones:** Oh, it was Steve. I thought it was the Woz that bought one.

**Speaker ?:** Steve came up.

**Atari:** No, no, no, no, no, no, no. Steve came up with the idea. He went to the show and he listened to what was going on. And he looked at some of the guys like Suiting and these other guys had done it. And Steve is the idea that came up with the idea of building their own kid computer. Okay. Woz did it.

**Atari:** But it was Steve's idea originally. And I'll give you a side story because it's really true. Steve, everybody talks about they sold a car or something in order to build the thing. What actually happened is Steve made a contract with Atari because he knew those guys real well. And that they would develop a game for the – and Woz developed a breakout.

**Dave Jones:** That was Breakout, wasn't it? Breakout, that's right.

**Atari:** It's the first – I give Woz credit. Every time I speak to anybody, it was the first nonviolent computer game. Oh, really? Think about it. Nonviolent? Everybody else just pong, knocking to the asteroids, you know, tank, right? It was legitimate. And the money from that, which Woz couldn't officially take and Steve did it for him instead, allowed them to go out and start the company. Right. Anyhow, okay. Just to kind of bury the who started the personal computer industry. Yes, please. I'm waiting for it. We had a development system, which is a big, ugly thing that we carry around. It was an ICE system. Does the word ICE mean anything to you? In circuit emulation?

**Dave Jones:** In circuit emulator. So this is not the Kim 1, right? This is before the Kim 1.

**Atari:** No, the Kim 1 was there. We offered the Kim 1 for people who wanted to do it.

**Dave Jones:** Oh, you were offering the Kim 1 in 75 at the show, were you?

**Atari:** Yeah, yeah, right, the original show. Yeah, yeah.

**Dave Jones:** Oh, right, okay.

**Atari:** And then we had two other development systems done by other people over there, too. And then we had the microphone.

**Dave Jones:** Which, by the way, folks, Chuck also, with the Kim 1, invented the world's first single-bore computer? Yes, sort of.

**Atari:** Maybe. Well, I don't know. It's an argument. Kind of. Yeah. We don't care. Forget it. Forget it. We don't want to take care of that.

**Dave Jones:** Keyboard input monitor. There were a whole lot of guys. That's right.

**Atari:** Well, remember, it had a little calculator keyboard on it. The guys that did it inside of MWS Technology were calculator guys, right? And so they made a little calculator board. It was a nice little product. Right. And so we had this development system, which I was carrying around the Bay Area and plugging into people's stuff and make it work, right? And then I used to have a bet with people. I could go into a company and over a weekend, I could design a new product for them using the 6502. And I did that with calculators and printers and a whole bunch of different products, right? Yeah. And a guy ultimately took it up on a pinball machine and I didn't do it in a weekend, but we did a pinball machine. Okay. Fantastic. A lot of PIAs. A lot of PIAs. Yeah. Anyhow, so my local sales guy had met Jobs and Wozniak because they were listed as somebody that bought the product and he went by and checked on them. And it didn't work. The Apple One didn't work. And so they asked me to bring in the development system, which I did, and we actually helped them work. Now, Woz has a story in some book he's written or somebody wrote a book that says, I showed up with a hat, which I didn't. And I was wearing a suit, which I wasn't. Right. And we were not there to sell them anything. We were there to help them, like we were helping everybody else, make their computer work, right?

**Dave Jones:** And this was in the Jobs' garage?

**Atari:** In Jobs' garage, yes. Yes, yes. Okay. So we did that, right? We got to be working and we went on. And the next time we crossed paths was, I told you, we went around the country introducing the 6502 and telling people what a great idea it was and everything. And kit computers were starting to take off reasonably well, right? I don't think Apple sold more than 100 of theirs, but suiting sold a lot, right? And so the programmer, you know, and I'm going to finish down your story about that because it's a really important story. The suiting kind of machine was designed for the same people that used to buy from Heathkit, right? Yes. Okay. And Heathkit was the guys until Radio Shack kind of buried them, right? And, but Heathkit was the sort of thing, you built your own audio amplifier, right? Absolutely.

**Dave Jones:** They were, yeah, they were the...

**Atari:** The kit business.

**Dave Jones:** They were the kit business, yeah. Yeah, yeah.

**Atari:** And so the concept of the kit computer was the same thing. They shipped you all this stuff in a box and they told you it'll work if you put it together and solder it and all that. And so the guys that built it were the same guys, right? So a programmer who wanted to have his own computer, and I'm going to explain to you why they all wanted their own computer in a few minutes. They came to us at the show and said, because they saw the Kim one, but the Kim one wasn't that. And they said, what we want is a computer that we don't have to build. We want something that we just walk in, take it, and start programming it. And, you know...

**Dave Jones:** Programmers, right? Come on, guys. Yeah.

**Atari:** Well, no. Why not, right? I mean, people who are users, right? I mean, because... Right. Okay. Now, let me explain to you that at the time we started, we knew about a massive user potential. I worked at GE. I did the... I wrote... Gave the first program. The guys that I worked with in GE built the first timesharing system for Dartmouth where the basic was done, right? And I gave the first class inside of GE on basic. And then I worked at the jet engine business where we had guys who were given their own 225 machine with a timesharing version of basic to design jet engines with. So you could do a lot with basic, right? A lot more than everybody thought you could, right? And so a lot of the accounting groups got versions of basic and put them on machines. So every kid that was coming out of school that had any accounting degree, any finance degree, marketing degree, engineering degree, every one of them were coming out of college using timesharing in the college, right? And they all had learned how to get on and write programs in basic. And they had their own individual programs. And then the instructors were given programs and some of the tests when using the program. So they're very computer literate, right? Well, suddenly people started looking at their bill for GE's timesharing service and discovered it was enormous, right? So they said to everybody, you can't have timesharing anymore. We've got a computer downstairs. You take your cards down to it and we'll give you back a run in a couple of days, okay? So here's people who are used to designing their own machines online, right? And you probably don't know it because I'm not sure you're old enough, but during that period of time was a major rebellion in the United States against technology by a whole bunch of people that threw themselves in front of things. Yeah, they killed the SSD, the high-speed, they killed more. They killed a whole bunch of projects because they were so out of... And what they did, a couple of them did, is they broke into university computers and hacked them up, literally, right? Oh. Like what you did. And hatchets. With hatchets. So all of the computer companies put these barriers up. You could not get through a bulletproof barrier to get to the computer. You literally walked up, put your cards in a tray because everybody was afraid that they were going to get their computers trashed. So we'd gone from, here's this wonderful thing of sitting here with my own computer, to this barrier to these big things. That's incredible. Right? And there wasn't a few people, right? It was every graduate and everybody who'd worked in companies like Pete Marwick and all that said, all were sitting there frustrated. So those are the people who were talking to me. They're saying, I want a computer, right? Right. So I knew, absolutely knew, that I had to have a machine that was really good at basic. Okay?

**Dave Jones:** So you added tiny basic to the Kim 1? Never.

**Atari:** No, no, no, no, no. Maybe they did. Maybe they did. It didn't matter. When I was going to do the PET, I got in a car, drove my family across the United States to go to work for Tramiel in Palo Alto. And along the way, I stopped at this, in Albuquerque, New Mexico, went to this two-room place over a bank and met with Bill Gates and his team. And they had written a basic for the 6502. And I said, look, what you have is not good enough. So I'm going to go out there. We're going to get started. And if you'd send your programmer out, we'll define to you what basic ought to be if you're going to put it in a computer that does things. Right? Interesting. Okay. So Gates agreed. Right? And they sent sitting out. And I had this really smart guy that had worked for me about 10 times who would help me start. We did a first board layout program together. And he had an ex-PhD from Czechoslovakia University. And the two of us sat down with this guy. And we blocked out what we wanted to have for I.O. functions and screen functions. And I don't know if you've looked at a way we can prove this. If you look at ASCII, right? At that time, ASCII was only half as big as it is today. They only had the front side stuff defined. So we took over the second.

**Dave Jones:** The first 127.

**Atari:** Right. We took the second. Right.

**Dave Jones:** Yep.

**Atari:** And defined them with pet symbols. Okay? And if you look at them today, they're still diamonds. Right. Right. In that set. They've been slowly taking them out over time. But what we did is we made it. We put character drawing capability in. Right?

**Dave Jones:** With the borders and all the single and double borders and all that stuff.

**Atari:** Everything you needed to build something. You could do visual, complete visual build on the machine using character graphics. Right?

**Dave Jones:** Right. And so we'll put a picture to the keyboard because it's on the keyboard to the pet. Right.

**Atari:** Right. So what happened was we extended BASIC. So it would do that. We put the IEEE 48 bus on because I wanted everybody to believe you could do any IO with it. Right? And HP was in the process of trying to establish that as the proper interface to instrumentation. Right? And HP had actually done some work with putting BASIC on their stuff to be able to manage the IEEE bus. But we put the other commands in. And so all the commands that are in the BASIC you buy today, most of the things that do things rather than run a teletype, were added by us in that week period. Right? And so they took it back, got it working. We made it working. And then we negotiated a contract with Gates for a one-time buy. And he didn't believe in the 6502 because he had been trained at Harvard. And he knew that anything with that small stack was not a real computer. Okay? And he was right. It wasn't. Except he forgot that what he was writing was an interpreter. And the interpreter doesn't need a stack. Okay? Got it. So we could use his interpretive BASIC, right, on a 6502 without ever running into a limitation because of the stack. And we did. Right? So the idea was is we're going to put BASIC in ROM. We're going to put all this beautiful screen stuff that we're doing in ROM. And ROMs just happened right about that time.

**Dave Jones:** Right. We're talking about e-PROMs? Or are we talking about one-time program?

**Dave Jones:** Real ROMs. Real ROMs. Real ROMs. Burn it and you're done.

**Atari:** You're handling one second. You're food and one second. No, no, real ROMs. You put them on the board. Remember, these guys were out of the calculator business at MOS Technology, so they were using ROM-based calculators for a long time, right? Yep. Because you had to do all those mathematical functions. You did them. A little calculator sort of looks like a microproze. You program it, right?

**Dave Jones:** Was the ROM with the lookup table on it or something like that? Yeah, well, I have more than a lookup table.

**Atari:** I actually have algorithms for doing computations, right? All that fancy scientific stuff is programmed in ROM using the calculator functions, right? So they were used to using ROMs, and so they built us a nice big ROM, and we put the big ROM on, and we put the basic in the ROM, and we put the rest of the stuff in ROM. And Radio Shack had been looking at the computer stores. Now, remember, computer stores happened because people were selling these kits, and a lot of people got the kit and said, I don't know what to do with this, right? Exactly. So you go down to your favorite computer store guy, and he'd help you get it working, right? Okay? Yeah. But the problem was is they started stocking things like TTL and ROMs and things like that. Well, Radio Shack had buried, I just told you, Heathcote, right? Heathcote, yes. They'd buried everybody. There was nobody trying to compete with them in the stores for electronics business, except for the new computer stores, right? Right. So John Roach at Radio Shack is, I've got to have a product that kicks their ass, okay? Yeah. And he agreed with us that it had to be a turnkey product. He wasn't going to try to teach the Radio Shack guys how to make a computer. He was going to teach them how to sell a computer, right? So he specced a computer, built-in CRT, built-in keyboard, built-in tape drive, right? And we were working to that spec because it was the same spec I had, and we actually showed it to John Roach the first time ever at the CES show in Chicago when it was 50 degrees below zero outside, right? And – Midwest, yeah. Yeah. The last time the CES show was in Chicago was that weekend, right? And it was – Why? Chill factor. I woke up. I was working all night, and I was having this view over the lake, and I watched this ice fog, which is really beautiful. If you've been in Cleveland, you know what I'm talking about. You can – you know, ice fog is really beautiful when you get the sunshine on it, right? And that's what was going on. It was ice fog on the lake because it was 50, minus 50 degrees. And the management at CES, which was the big consumer show, right? That's why they – the idea around about the January CES is you showed ideas there, and then they had another show in June where you went and wrote purchase orders. Right. And so everybody at that show said, we're not going to come here again. And Vegas came in and made this big pitch, and that's why the CES show is still the biggest show at Vegas, right? Because everybody said, screw it. We're going to go to Vegas, right? But anyhow, Roach came up to the room, and we showed him that we had just gotten the CRT. I had to buy a book from – he was the guy that did the first portable book. Osborne. Adam Osborne had written this book. Osborne, yes. He'd written this book on how to make a CRT work. And so we had built it, and we had the CRT upside down, and we had to call some people. We got the CRT up just about the time Roach walked in. And he looked at it and started sitting down negotiating with Tramiel. Well, Tramiel had put all his money into this thing, hoping to save his calculator business. And so he said to Roach, look, I'll tell you what, you can have exclusive on this product, but you've got to carry all my calculators. And Roach had just signed a deal with TR and some other people. He said, no, no, John. And besides, he didn't like Tramiel very much. And did anybody else?

**Dave Jones:** Oh, at this point, sorry, it should be pointed out that in 75, Commodore, who were king of the calculators, they bought MOS technology. Right, and they bought it.

**Atari:** As a matter of fact, if you want to take a side story, let's do that simple side story. Jack Tramiel had a guy who had actually worked with me way back when we had our own company, a little bit by the name of Andre Cezanne, who was working for a company that was a hot dog company, but it went away. And Andre really did understand semiconductor processing and semiconductor products. And he was really trained in that stuff, as well as applications. He was a very broad guy. And he was Jack's engineering manager. And Tramiel started running into problems with TI, kicking his butt. And so he decided that they would design their own chips and get them built. And they were getting them built in a couple of guys in Palo Alto. And it worked for him, right? But the tie-in calculator chips were the only ones that were really doing well. And MOS technology was way ahead of everybody. Well, the problem with MOS technology was that they had been backed by a company called Alan Bradley, who had put a bunch of money in and then decided they wanted to get in. And particularly when Motorola sued him, they said, screw it, we'll give you the company. Goodbye.

**Dave Jones:** And everyone should know Alan Bradley because they're the famous programmable logic controller. Yeah, well, more importantly, they started MOS tech as an internal semiconductor. Right.

**Atari:** Yeah, but more importantly, they were the leader in making RAMs. I mean, packages of resistors, capacitors. They were the, you know, you bought Alan Bradley resistors and capacitors back in those days, right? Yeah. Yeah, they were the leader. Right, right. And anyhow, so the MOS technology was under financial pressure because we'd had to settle up and, you know, it cost a million dollars to fight a lawsuit like that. And so they were under some financial pressure. And they could see that the calculator business was about to go off a cliff, okay? And the reason that you could see it was going to go off the cliff is the Japanese had introduced the concept of the LCD calculator, right?

**Dave Jones:** Right. Versus the super high-end commercial ones.

**Atari:** Yeah, I mean, they were still selling calculators that were better than HP and everything else. And they sold for a while. But they were a P-channel product, right, versus CMOS product. No LCDs, right? And the market went off a cliff, right? Just like them.

**Dave Jones:** And didn't TI come in as well? They were making chips. TI was a major player.

**Atari:** And then they decided to come in. They were a major player, right, in the calculator.

**Dave Jones:** And then they decided, well, we don't want to make chips anymore. We want to make the calculators as well.

**Atari:** And then everyone, and they just destroyed the industry. Anyhow, so they bought MOS technology so that they would have their own high-end calculator P-channel capability, right? And Suzanne was absolutely pushing Jack to do it because he talked to me, and he and I wanted to do the pet, okay? All right? And so he got me out there, and we kind of lied to Jack and said we'd have it ready to go in January. And we got it far enough along so that he backed us, and we had this show to – so Suzanne was very important at this. And I've got to tell you, one of Suzanne's major contributions to that was this was the year that when you went down to the local store in Los Altos, in Los Gatos, you bought a product called a pet rock, right? Yes, yes, which lasted six months or something. But anyhow, people were all buying pet rocks, right, because they didn't require walking around the block. They didn't require being fed. You didn't have to feed them a little bird, a little snake, you know. So it was a hot product. And so Andre said, we've got to make this computer appear to be warm and frizzy, so we're going to call it pet, all right? And so we decided we'd call it pet, and that's good, okay? And we put a name on it called Personal Electronic Transactor just so that we would have an excuse for it. But the funniest thing is that Andre was from France, right? And he ultimately left Commodore because Commodore and he powered companies. He went over to Apple, and he got the European distribution rights for the Apple, which at the time Apple went public made him one of the richest owners in Apple because they had to buy the distribution rights back from him for an enormous amount of stock. Anyhow, in France, pet has a word like S-H-I-T connotation. Big connotation. So when we sold it in France, we had to call it pet, right? Not pet. Oh, like actually spelled out. Like MLS. Yeah. So it was funny. But anyhow, but Andre named it. Everybody says, why did you name it to pet? We did because we wanted it to be warm and friendly, right? That was we told everybody we're making warm, friendly computers, right? And we packaged it up in the case and got it working. And we took it to Dallas. And Dallas was one of the last of the big computer shows. There used to be a show once a year, maybe twice a year, where all the big computer guys got together and showed off what was going to happen next in the computer industry. And IBM, one year, went out and showed everybody why online really worked, right, in one of these shows. And so you had people like Univac and DEC and everybody were selling these computers during this time. Didn't work so well for them. No, no, no. Overall. By the way, it worked. I mean, come on, man. The PDP-11. Well, yeah. They're huge. Long term. They made Ken Olson a rich man, right? Right. But they had this show down in Dallas. And they had decided that computer stores and everything were taking off a little bit. And Radio Shack said they were going to go into business, but hadn't gone in yet and all and so forth. So there was a big show in Palo Alto in the spring, right? And it was a guy by the name of... Shit. Oh, how can I forget his name? He's one of the lead... Papay. What? Sorry, pardon my language. But anyhow, he... He... He...

**Atari:** Jeez, I'll get his name in a minute. He's really... He decided to put together this show to show that personal computers were real, right? And he set this show up in Palo Alto and he was charging people $25 to go to the show. And we had a prototype of the pet there and Apple had a prototype of the... The stuff they were doing. And it was a whole bunch of people. But Tramiel was totally impressed with the fact that all these people were lining up outside to pay $25 just to go look at computers, right? I mean...

**Dave Jones:** Yeah.

**Atari:** Yeah. They were convinced it was a real product. So, as a result of that show and a couple others, the people in Dallas decided to... And they created a thing in the basement that they called the Computer Boutique. Okay? And we took the first set of pets that worked there, right? That worked. Okay. Well, no. I mean, come on. You're in the middle of prototypes, right? Yeah. I know.

**Dave Jones:** Yeah.

**Atari:** Of course. Of course. So, we had the prototypes. We actually built them on boards and all that stuff. We took them there and we set them up. And we had demos. And then I gave them speeches and demos and so forth. And we were selling the computer there, right? You could buy the computer there. Now, Jack Tumell came to me about three months before. And he said, we're going to be like Hewlett-Packard when we do this computer. And I was thinking he meant like quality and big image and all that stuff. He said, no. When Radio Shack brought... I mean, when HP brought out that fancy programmable calculator, you had to pay them a full price up front and they might ship it to you in three months. Right?

**Speaker ?:** Okay.

**Dave Jones:** Right. Cashless.

**Atari:** And he said, the only way I'm going to have money enough to do this is if we do the same thing with the computer. Take pre-orders. So, at this show, my wife is sitting there. She was a guy who sold Steve Jobs his first 65-02, by the way. So, she's sitting there taking these orders. And people would come up and they were standing in the back of the room saying, take my check next. Right? You know, it was a big fight. There was a stack of people sending checks up. And she would put them down in a book, put them on a list, tell them what their number was. Right? And we took that full money. Right? And what was the money? Just give us a relative amount. It was about... I think it was like $550 is what we're selling. A solid. I think...

**Speaker ?:** Yeah.

**Dave Jones:** It's a solid amount of money, but still affordable for the time.

**Dave Jones:** I mean...

**Atari:** Oh, no. Yeah. I mean... It was... It was cheaper than a stereo system. Right?

**Dave Jones:** And it included the CRT. Right? It had everything. Yeah. It was all built in. It was the whole thing.

**Atari:** It was a real computer that you could use now. Yep. Right? And once I showed people it ran basic and you could do it, we couldn't stop it. Right? I mean, it was going to go. Right? It was absolutely going to go. So, I just want to tell that story about we're sitting down. So, I decided to take a break. And the second... Next to last afternoon of the show. And this room is full of people sending checks up to my wife. And we're totally taken over the downstairs. And I walk upstairs to where the computers were. I used to go to these shows. And there was nobody there. It was just a salesman talking to the salesman. Nobody wanted to talk about big computers. They wanted to be downstairs buying their own computers. Right? And that was the beginning. Right? We had guys signing up to be distributors. I mean, people looked at it and realized that they were at the beginning of a revolution. Right? And so, Radio Shack finished their machine because they couldn't. And they brought it out. And it was a really nice looking product. They brought it out in the fall at another show. The problem is they didn't have enough ROM space. So, they built in Tiny Basic. Okay? Now, Tiny Basic is a nice little basic if you want to just screw around. Right? But, you know, it doesn't do what Real Basic does. Right? The Basic you're used to. Okay? So, they got an instant reject. Right? People bought them and they realized they didn't do what they wanted them to do. Apple, we go back to it and we tell the story about Apple's tie to getting started. But when we went to the West Coast to do the computer, we wanted to be able to make this show. And rather than design our own boards and stuff before we got there, my marketing guy went around and found two or three people, including Apple. It was working on a board. So, we brought Apple over and Jack said, look, you got a little company. I want to get you into my company. He made him an offer for the company, which jobs turned down immediately. But luckily, they had found…

**Dave Jones:** It was $150,000, wasn't it?

**Atari:** I don't know what it was. It didn't matter. It didn't matter because Mike Markler had decided to fund them. Ah, right. Yeah. Okay. So, they weren't going to accept anything. Markler made it happen. Right? Got it. Markler made that company happen. Yep. Markler understood marketing and he had good money. Yeah. He made it happen. He brought a team in from, you know, the guys from National, from Intel that he brought in.

**Dave Jones:** So, Apple weren't going to sell at any price at that point.

**Atari:** Well, I don't think he would have sold at any price. But anyhow, while Jobs is in negotiating, he'd met Waz and everything. But Waz and I are sitting down and I was explaining to Waz what we're doing and asked him if he wanted to sell us his machine. And Waz said, you're wrong. What you're doing is incorrect. What people want, because I spend time with these guys at the computer groups, what they want is a machine that can go in and write their own code in assembly language. Right? Ah, okay. So, he invented a thing called Sweet 16, which is kind of like a super compiler for the 6502. And they built that in at the beginning when they sold the computer. Well, it didn't sell.

**Dave Jones:** The Apple II we're talking about?

**Atari:** The original Apple II started out without a BASIC in it.

**Dave Jones:** Ah, interesting.

**Atari:** And you can find out if you look at shows and everything, they'll tell you about it. But it never shipped without BASIC. Is that correct? No, it did ship without BASIC. Oh, really? Okay. It shipped some, not big numbers. Remember, at this point in time, people were busting their ass to ship 1,000 machines in a week. Right? I mean, this is at the beginning. Right? Okay. Pardon my swearing every so often. I was born in Maine. So, some swear words are part of the vocabulary. We have an Aussie here. Basically, that's us.

**Dave Jones:** He fights to find any pronouns, let alone non-swear words.

**Atari:** Right. Anyhow, we, I think we got deviated. We were talking about. Sweet 16. So, what happened was, Makala quickly figured out that he'd made a mistake. Right? So, he went to Gates and said, I want to buy the same BASIC. It's in the Commodore. Now, Gates and I had a deal. He could sell it to anybody he wanted to. He could, you know, he could clone it. Right? I mean, I didn't care. Right? Because we bought it cheap. And so, he negotiated a much higher price than we paid with Apple. And they paid it. And then, Radio Shack came in and discovered and said, listen, Penny Bakes isn't working. We've got a way to put, to jumper an extra ROM into our machine. Yeah. And we want to buy the BASIC. And John Roach said to Gates, why don't you take a royalty? Right? I want to sell a bunch of these. Why don't you take a royalty? And Gates said, no. 6502 BASIC is not going to. No, it was 88. I'm sorry. It was 88. But he said, no. He said, I want to get paid up front. Because he was financing his company at that point. Right? And so, he got Rouch to pay at least double what Apple paid. And so, all of a sudden, R-BASIC became the standard. Right? And everybody that bought a machine after that, and that's very important when we talk about MS-DOS. Yeah. Okay. So, you bought a personal computer. You had to have BASIC. And that's what sold it. Right? People just bought them, used them. We went to one show one time, and this lady came up to me and said, I want to know where we are on the priority list, because we're still taking money in advance and when we're going to ship. We said, well, we can't take you out of the loop on the priority list, so we'll try to tell you how much time it is. She says, you've got to do something. We decided that all of us in my house wanted to use the computer. So, we drew lots for who had time. And my time is between 2 o'clock in the morning and 6 o'clock in the morning. She's the mother. I'm so tired. I just want to program. She says, you've got to save me, right? Get me a machine, right? But that tells you how much in love people felt with those machines, right? It really and truly created the industry, right? Yeah. And we sold a lot of them. We sold a lot of them in Europe. Ultimately, Apple sold some here. Radio Shack sold a lot of them for the same reason. They were built in and they worked together and everything.

**Dave Jones:** What was the name of the Radio Shack machine? The Trash 80 Model 1. Oh, Trash 80. Trash 80.

**Atari:** Yeah, right, right, right. Trash 80, yeah.

**Dave Jones:** Why did they go with the Z80 in that instead of the 65-8?

**Atari:** Because just because of the fact that he had somebody in Texas that thought it was better. Remember, TI had come up with a machine similar during that time. Yes. With a machine based around their microprocessor. The 99-4A, yeah. Yeah, right, right. So, no, he just got, you know, he delegated it, right? And that's why Tiny Basic was in there. John was a production marketing guy. He didn't know anything about the technology. He just hired people. And he was a good guy. I mean, he's a really good guy. But he didn't have a clue why. And, you know, I told you why they wanted to do it. And they did accomplish that. They basically ultimately killed the computer stories, right? Yep. And fries helped a lot there, too. Mm-hmm. But the big thing about it was is at that point, we went another way. We went into Europe, and the Europeans bought the machines, that's the way we talk. But most of them bought it because they were many computer customers, and they weren't getting that kind of support. And the guys who installed the many computers just became dealers. And so we started getting upgrade machines. We built the machine with the two disk drives. And I designed the first Epson printer and put the printer in. So we had a machine that was a pretty serious machine, right? Okay. And we were selling a lot of them. And the reason I want to tell that story is because what happened was we got the U.S. going one way and the other. And then Clive Sinclair came out with the thing. Yep. What was it called? The Sinclair, whatever it was. ZX80. Yep. And it was selling very well, right, because it was cheap. Exactly.

**Dave Jones:** It was $99, yeah.

**Atari:** Yeah, it was cheap. Okay. And we had designed at – I'd gone to Apple and come back, and Tramiel basically charged me and my group with designing a machine that would kill the Apple, right? Right. So we had come up with a machine that ultimately was the C64.

**Dave Jones:** Was it the VIC-20?

**Atari:** No, no, no. We did the machine, the C64. But the problem was is we were depending on MOS technology having the video interface. Got it. Okay. If you don't mind, I'm going to take a minute and deviate and talk about video interfaces because it's really important. Yeah.

**Dave Jones:** Let's get technical.

**Atari:** Okay. Well, no, no, not that. It's just I'm going to take you – we're going down several paths, and I'm trying to keep you abreast of them.

**Speaker ?:** Yep.

**Atari:** We did – we had done the PET. I mean, the 6502. After we finished that thing at the MacArthur Suite, I drove up to Grass Valley. And the reason I was in Grass Valley was when I was doing the marketing for MOS technology. One weekend, the president and my guy who helped me do the PET and all this other stuff threw me out of the building because I wasn't getting the manuals done, right? And so I was forced to stay home and finish the manuals. Yeah, documentation. During this period of time – during this period – well, it's a funny story. It's been well known that I was thrown out of the building until we finished the manuals. But the manuals turned out so well. Everybody really loved them. But during this time, I was accumulating. My people were taking the phone messages, right? So I'd get a copy of the phone messages, and most of them I would just pass off to somebody or just ignore. But I saw this one from Grass Valley, California. Now, if you guys know California, probably you don't. But Grass Valley is up – partway up in the mountains, and it's in the middle of wine country. And it's where, right? It's a nice place, but it's nowhere. Right. And I said, what the hell are we doing with a company in Grass Valley interested in my 6502? So I call the guy up.

**Dave Jones:** Let me guess. It's the Grass Valley Group? Yes. He's the guy.

**Atari:** Yes, called it. John LeCour, right? He was the guy. He said, I'm Steve LeCour. I mean, he said, I'm the advanced arm for Atari. Now, we've been selling products, 6800 products to Atari, and we've been working Atari, but as the guys making the programmable games, right? But he said, my job is to come up with the follow-on to the Pong. You know how Pong happened, right? Pong was a bar machine. Pong was a bar machine. Yep. Right? Pong was a bar machine. Um... As in, used in a bar? Yeah, no. Only because that's why he did it. Yeah. What's the guy's name who started it? Atari.

**Dave Jones:** Oh, uh... Last name Bushnell, is it?

**Atari:** Bushnell. Yes. Bushnell. No one Bushnell. No one Bushnell. He had come out of one of the big companies like Xerox or, I mean, App Bank or one of those places, but he had kind of a bad background. He'd done a lot of things, and he'd been involved with bar machines, right? Mm-hmm. And he said, if I put this machine into bars, I can collect quarters, right? Yeah. So he and this guy, Al Korn, who was also in the same company, they designed the first Pong machine, put it in a bar, took the quarters from there, built another one, kept doing it, and they built an entire company about quarters from a bar machine.

**Dave Jones:** Awesome. Okay.

**Atari:** Okay. So Pong was created in bars, right? Yeah. And this company in Florida called Allied Leisure looked at what he was doing. They were making a lot of game stuff, and they ripped him off and actually outsold him and caused him all kinds of trouble to the point that they did secrecy things after that that were really overwhelming, right? Atari did, because this guy had ripped him off. But they had decided that they could make a portable version of Pong, right? So they designed it, and they had it ready to go, and it was relatively close to Christmas time. I think they missed both CESs, right? So they went to Sears with this thing ready to go and went to the guys who would be in the, where we would sell the TVs and the guys that sold the stereos and everything. And they told him, we don't need it, right? We've got our fall special all planned out and everything. And somehow or other, they met the guy who was in charge of the sporting goods section. And he says, I don't have a hot product to draw people into my store. The sporting goods section. That's my job. That's my job, is to bring people in. So he put the original Atari Pong in the sporting goods section at Sears and created an industry.

**Dave Jones:** I love it.

**Atari:** Because it just took off, right? It became the hot gift for that year. And people were coming by and buying footballs at the same time, and they weren't over in the stereo department. They weren't. It just took off, right?

**Dave Jones:** Do you think that is why mass adoption happened? Is it because there was just that exposure? Or is it just because it was that different and fun for people?

**Atari:** Well, Atari was the original Pong. I don't know if you ever used it. We used it and played it until we got it. Yeah. Considering when it was done, it was really exciting, right? I mean, it did things that you'd never done with your TV before, right? Yeah. It was so. Then what they decided that they wanted to make a really programmable game so they could sell the games, right? You know, the theory behind the program of the game business. You sell the console for nothing and you sell the games, right?

**Speaker ?:** Yeah, yeah.

**Atari:** And so that's what Lecure's job was, is to do that. And so he invited us up. We went up to Grass Valley. We sat down with him, blocked out a program. I drove, went back to Pennsylvania. We sat down and agreed on a budget for him where we lowered the price of the processor plus this Ram Ram IO chip to $12, okay? Now, this is at a time, remember, everybody else is selling microprocessors and IO devices for hundreds of dollars, right? But we knew we could build it and make money, right? We absolutely knew we could do it. So we signed up with them and they said, okay, Lecure got an agreement that they would design a custom chip. And the guys who designed a custom chip were the guys who were our second source called CinderTech, right? So a guy who did the, what's the second machine, Commodore did? It was not the apricot. It was something like that, a word like that. Anyhow, it was a something, right? Anyhow, he, but they hired this guy from CinderTech and he went up there and they showed him how to make the IO device that made the game work, right? Now, the guys at MOS Technology, at the same time as that was going on, had come up with their own version of a thing to make a game, right? Yeah. And I was under this absolute, we'll kill you if you tell anybody, deal with Atari, right? Because remember, they were so, right. So I couldn't tell the guys at MOS Technology you're on the wrong track, right? This whole industry is so incestuous. I literally had to let them finish it. And they actually put this thing out and some guys, some two or three guys built game products and sold them against Atari with this product for a while. Okay. And then we came up with an agreement with them that they would go off and design a machine that ultimately became the driver for the C64. Right. And they were supposed to be off and designing that. And we did the rest of the computer that was going to be, and we said we could build this computer for under $100. So we can sell it for $100. That's the plan. And we were, Sinclair came out after we'd done that, right? And Tremel fell in love with Sinclair. And so one of the guys by the name of Bill Seiler, and don't lose track of that name. He's a really important guy. Bill Seiler had come up with the idea of the VIC-20, right? He'd shown it to Tremel. And Tremel was pissed at us because he said you're supposed to have done the product that will kill the apple, and that product won't kill apple, right? Right. It did kill Sinclair, but it won't kill apple. And we said, well, we have to wait for MOS Technology to finish the chip because we needed what became the C64 interface. And so he actually rejected it. And then he went to Europe and decided he wanted to complete with Sinclair. And so he let a team inside of MOS Technology, I mean inside of Commodore, complete the VIC-20. Guy by the name of Taz Yurikora, right? He's the guy that did that. Not all the people you hear, right? Right. And Sharpintere did the basic product, right? But Yurikora is the guy that made it happen, right? Got it. And so, and I'm not taking anything away from Sharpintere, but Yurikora has understood how to put a product into production and got it packaged and did all the other stuff and made it successful. And, you know, it took off. Well, right about that time, Tremel decided he was going to get rid of me and a couple of the other guys that had built the computer business because he thought we were rebelling because we told him we wanted to do a machine like the Amistos machine. Yeah. We said this industry is about to split in two. And in Europe, we're already selling a higher-end machine. So we can go do the VIC-20. We've got it all done. We can do the 664. It's done. You don't have to worry about it. It'll get done, right? But we need to go off and start a company to go chase this thing, which is going to be the big computer market, right? Yep. I mean, it's very nice. You need these. IBM market, yep. That market that became the PC market, right? But it was obvious it was there, right? And you couldn't do a 664. You needed a new process. You needed everything new, right? But it was okay. We knew how to do it. And because we proposed it, he threw us out of the company. Thank you very much. Well, I don't know. Great. Thank you. We went off and did it for ourselves. And then, of course, he sued us. And we had to fight that battle. But anyhow, the point was is that it was a time to create a new industry, right? Right. Something that was not being sold in Sears, right? But something that was being sold in a more serious way because it would be a more serious computer. And just to, I want to back up one place just so that you understand the evolution. Kit computers had a function. Yeah. And when you built it, it worked. Now, the guy, Bill Seiler, who did the VIC-20 and the C64, was in Florida working with the company, Allied Leisure, that had knocked off Atari. And we were building a pinball game built around microprocessor. And I'm sitting in a place, and Seiler was one of the earliest hobbyists. And he built this machine, and he got it all built up. And he ran it, and it played the Star-Spangled Banner. And I said, okay, now what are you going to do with it? He says, I don't know. I just built this thing right. He did what I asked it to. Yeah. And he was one of the guys in these computer clubs. He was in a computer club that ripped off Bill Gates' basic.

**Dave Jones:** Right. The old paper tape, yeah. Yeah.

**Atari:** Oh, yeah, yeah, yeah. Bill Gates was-

**Dave Jones:** Yeah, they made copies of the paper. Yeah, he wrote the famous open letter to hobbyists. Yep.

**Atari:** So guess one of the few people that ever responded to the open letter to Bill Gates? Bill Seiler. Right. Bill Seiler sent him the money. Send him the money. Gates remembers that. He sent him the money. Send him the money, saying, I'm sorry I stole this, right? And Gates remembered that, because he was one of the few people that did it, right? Right. Yeah. And of course, that didn't happen with us, because they were all in ROM, and it was a totally different place, right? Yeah, yeah, yeah. But the point was, so I stole Seiler, right? And he helped do the original PET, right? He was one of the guys who did the original PET. He did the C64. He did the VIC-20. So he was a major creator of what was the hobby computer business, so whatever you want to call it. What is the C64? C64. Kids bought it for games. They had great games on it. Yeah. But every kid that used that machine became computer literate. I would go into Kmart or something and talk to a bunch of kids that were over there, and we'd sit down, and they'd demo that they could write a program.

**Dave Jones:** Yeah. Oh, yeah. Because you had to if you wanted to major on games, right?

**Atari:** Exactly. It just didn't matter. You just learned, right? I mean, it was so easy to learn. So they sold the concept to parents by this thing called the C64 for your kids to be computer literate. The kids were buying it because of the games, but whether they liked it or not, they became computer literate. Okay? So we had created an entire generation between the basic and the other stuff and the generations. We created an entire generation of people that were what is now today called understood to be computer literate. But because you've already moved on to your smartphones and everything else, you don't even care that you're computer literate, right? Yeah. But you do write text. Anyhow, the point is that Silo was in at the beginning, right? And Glenn Stark, the guy I was talking to when you originally called me, was he did the floppy, and that's going to become an important part of this next story. Okay. So now we've got a new company and multiple new companies.

**Dave Jones:** Which is Sirius.

**Atari:** It was called Sirius Systems Technology. Yep. And because we took computers seriously, right? Is that why you did that? Absolutely. You remember Sirius? No, no, no, no. I did it for another reason, which everybody would laugh about. But I wanted the name Sirius, which I like. But, you know, Sirius is a two-star system. Did you know that? Yes.

**Dave Jones:** Yeah, it's a binary star system. Yep. Right.

**Atari:** So I could make a logo that had a nice bright sun and then a dark hole out of the side of the sun. Now, what does that remind you of?

**Dave Jones:** Is it the Commodore logo?

**Atari:** No, the Apple logo.

**Dave Jones:** The Apple logo. Oh, like the bite of the Apple. Yes, of course. Right.

**Atari:** It looked exactly like the bite of the Apple, right? Nice. So that's one of the reasons we made it Sirius. The other one was because we could play with the word Sirius one and now we got Sirius two. You know what I mean? It was a new band left on it. Right. And we...

**Dave Jones:** This is before the Sirius Cybernet Corporation and Hitchhiker's Guide. No, no, no.

**Atari:** Anyhow, so we went to Intel because we said we need a new computer. And David, who I had worked with in 1960 at the computer lab, was the guy running that. He was a really smart guy. Went on to be a venture capital guy. And he had insisted that the 8086 have an 8-bit version. And the reason he did, which is the reason we all bought it, was because RAM was so goddamn expensive. Yeah.

**Dave Jones:** So you use half of them. That's right. So seriously... You want an 8-bit bus.

**Atari:** You want an 8-bit bus. Right. And so we signed up for the 8080 and he committed to us in writing that it would always be second sourced. Okay. Big lie. Big lie. And so we were two weeks behind IBM when we made that commitment. We then flew up to Washington to sign up for the basic, right? And we had already signed up with CPM because they're right down the street from us. And while we were there, I met with Gates, who I had cheated on the original basic, but because IBM was up to see him because every personal computer had to have basic in it. Right? Yep. So they left a big session at CPM place. They left this big session because CPM would not sign the contract they wanted to sign. And... They wouldn't. Well, he was famously out flying a plane, wasn't he? No.

**Dave Jones:** Total lie. Total lie. Okay. Yeah. Okay. Sorry. What is CPM as well? Control program for microcomputers. It was the dominant operating system.

**Atari:** Dominant operating system.

**Dave Jones:** Dominant operating system before DOS.

**Atari:** It was the only one that... It was the only operating system that let you build something, right? I mean, you had to have an operating system. It was designed for the new 8-bit machines with much of memory and everything. So it was the right solution. And IBM would have signed up. The problem they have, and they kept telling them that, right? The guys that were out there negotiating said, we can't sign that contract. Now, you guys probably don't remember that there was a time when IBM 360 was so dominant. It killed companies like GE and... Oh, yeah. Yeah. Okay. The Europeans and the Americans sued IBM for restrained trade, right?

**Dave Jones:** Right.

**Atari:** And IBM did some very famous things to fight the government. Government subpoenaed a bunch of documents, and IBM sent them truckloads.

**Dave Jones:** Okay.

**Atari:** Buried them with paperwork, yeah. Because IBM could afford the lawyers, and the government didn't have enough, right?

**Dave Jones:** And that's how they worked, yep.

**Atari:** Yeah. They were tough guys.

**Dave Jones:** That's how IBM did business, yeah. They were tough guys, right?

**Atari:** Yeah, yeah. And so they had signed a consent decree that said they would always support open source on their stuff, okay?

**Dave Jones:** Ah, really?

**Atari:** So there was no question about MS-DOS was going to be open source, right? Okay. And the guys at CPM had a clause that said they couldn't distribute it or whatever, and they kept saying, we can't sign that, right? Yeah. And here's this room, Mrs. CPM and Phil, sitting there with the IBM guys, and they were really serious. They want to do this. They absolutely got to do it because they've got everything else coming in. They signed a floppy for the, you know, everything. And Phil would walk out of the room and walk next door, and there's Kildall and his lawyer. And the lawyer kept saying to Kildall, listen, we've signed up. There were a whole bunch of guys making CPM machines. They were paying good royalties, right? They were doing well. They were paying good royalties. And he said, TI came in. They didn't do shit. DEC came in. They didn't do shit. IBM's not going to do shit either. You're right. Make them stay with our contract because otherwise we'll have to go back and redo our contracts with all these other guys, right?

**Dave Jones:** Got it.

**Atari:** Got it. And so they left. And when they sat down with Gates, they said to Gates, after they signed the basic contract, because Gates was happy to sell it. At that time, Gates was getting royalties for everything because the Japanese had taught him that, right? Yes. Yes, they did. And they said to him, would you please call Kildall because we don't have an operating system.

**Dave Jones:** Yeah. I know. He practically told him to, yeah, go back to digital research and talk to him. No. No.

**Atari:** What he said was he had an offer from the guys that sold him the MS-DOS. And he said, Kildall won't do it. You call him up and ask him. If he won't do it, I'll do it. Oh. And they signed the MS-DOS contract right then. Okay.

**Dave Jones:** Even though Microsoft didn't have one, but they knew they might be able to get one. No, no.

**Atari:** They know they had the offer from those guys. They actually seen. Oh, they actually had the offer for the. The MS-DOS clone, right? That was done up in Washington. Yes, that's right. Right. Yeah, they had it. And they paid those guys like $100,000 for it.

**Dave Jones:** Yeah. I think it was like $50,000 or something. Maybe. It wasn't much. That's right. Or the rights to MS-DOS.

**Atari:** I just want to point out to everybody that if I hadn't done the basic with Gates, he wouldn't have had them on his doorstep with that opportunity. Right. Because it had to be in everything anyways, right? That's the idea. And so two weeks later, we walk into Gates. Gates says, I got this deal with Microsoft, with IBM. I'm going to do this thing called MS-DOS. And we said, great. We'll sign a license. We signed in a license with Gates, and we signed a license with CPM. And we first shipped our original machines with both for a short time. Right. But MS-DOS took off, right? And CPM stopped. And so we were the first people with an MS-DOS license, period. Right. Second. Two weeks behind IBM. Right. So now we're going to do our computer. We get our computer ready to launch. We launch it. We take it to the shows. And IBM is out there with a floppy that's got 300 kilobytes on it. And we've got a megabyte. Right. We've got a much better screen. They don't have a screen. Right. We had put in voice recognition or voice results. Right. We put in the audio stuff. Nice. And it's a nicely packaged product. So guess who won computer of the year? We did. Right. Yeah. And we were out selling. We signed Ford Motor County. We signed a whole bunch of people, right, as the customers. And we were getting ready to change the industry that next year. We knew we were going to change the industry that next year. I started working with Juggie Tanden. He was making my floppies for me. And he had a deal with me that I would use his hard disk. Right. Yep. So we got ready to go for the Comdex show. I think it was Comdex. I think it was pretty sure it was Comdex. Anyhow, we got ready to go to the show. And Juggie's ready. He said, I can start supporting you with this five megabyte drive.

**Dave Jones:** Five meg. Woo-hoo.

**Atari:** Wait a minute. Wait a minute. IBM was 340 KB on the floppy. I know. Five meg. It looked like a lot.

**Dave Jones:** You beat them to the hard drive. You were the first ones to use the hard drive. No, we were.

**Atari:** Absolutely. I had designed the product around the hard drive. We knew we were going to put a hard drive on. We came out of the industry. I did my first hard disk patent in 1962. Oh, wow. What aspect of hard drives? Everybody still uses it. As you go out across the disk, you get more space under the head. It's called zoning. So then as soon as you get to a certain place in the zone, you start recording at maximum frequency again.

**Dave Jones:** So you've got a patent on hard drive zoning. Yeah. Or had, because it's expired now, right?

**Atari:** 1962, right? Wow. Guess what?

**Dave Jones:** Oh, nice.

**Atari:** Anyhow, the point was, but we used that technique on all of our machines. That's why we had a couple megabytes when they only had 343, but whatever. So I'm getting ready. I go to the show. I build up some samples. We set them in the back room. We're in the booth. And I've got five machines with five megabytes in them. I've got the operating. Now, I went to Gates before that show. We were at a show in Southern California. And we're arguing outside of Disneyland because Apple's throwing a big party at Disneyland. We're having an argument about the fact that I had, I was going to launch my hard drive at that show. And I had to have the DOS for it, right? And he basically said, I can't do it, right? So I said, okay, I'll do it. And I had the team, and we did it. And we gave it to him. Why did he say that? He did. What? Because he was working on floppies. They were doing the DOS for floppies.

**Dave Jones:** So he didn't believe hard drives were important at that time?

**Atari:** He just felt he didn't have the resources, and it wasn't. Oh, right. Okay.

**Dave Jones:** So you'd have to write new code to talk to that hard drive.

**Atari:** He had to see it. He didn't see it yet. Gates was a perfect. Gates was a smart guy, a very young guy, a very smart guy. But he missed two or three things, right? He missed the internet. He missed the hard drive. He missed the- Internet explorer. It didn't matter. It didn't matter. It didn't matter. He did a great job with all the things he did, right? So he basically, standing outside on a traffic island outside of Disneyland, said, you can do the DOS yourself, and we'll just support it, right? Right. And so we did. I had a team of really smart guys that were ready to do that, and they did it.

**Dave Jones:** So you added hard drive support to MS-DOS? Yes. What version were we talking about here?

**Atari:** Before MS-DOS had any hard drive capability.

**Dave Jones:** All right. That was like DOS. I think DOS 2. No, I don't know. Whatever it was. MS-DOS 2 had hard drive capability. I think, yes, that would have been one. Maybe.

**Atari:** I don't know. Whatever it was, we added it, right? Okay, so now we're going to the show, right? And we get up to everybody and announce that hard drive is the future of the personal computer. And everybody looks at me and says, listen, you've got two megabytes on your double-sided floppies, and you're adding five megabytes. Who cares? And by the way, this is back when everybody thought two megabytes was plenty, right? What else could you do? Yeah, right. Okay.

**Dave Jones:** Because you can buy as many floppies as you want, whereas a hard drive is expensive.

**Atari:** It doesn't matter. People just, you know, we've taught everybody they needed a terabyte, you know? Do you ever sit down and think about how long it would take you to type a terabyte into your computer? Right. Anyhow. And I said to them, very simple, this is editors, because we were famous by that point, right? With CZ4, we had all this stuff in one computer. So, you know, I get the top editors and the top technical guys. And I said, it's the future computer. And they said, well, we're not so sure about that. So I said, listen, it's real easy. And there are five machines set up in the back of the booth. Please go down and use it for 15 minutes. Every one of them came back and said, I'm never going to use a floppy disk machine again in my life.

**Dave Jones:** Because they were just too slow. They were totally different, right?

**Atari:** It was a totally different experience running with a hard drive. Now, all of you have been running with hard drives forever. And they've slowed down and they've become more difficult to use. And you've noticed it, but it just happened to you slowly, right? And that was a major point for us. IBM had to go out and redesign the PC in order to be able to compete with us.

**Dave Jones:** Which was the PC XT, which they came out with. Right, right, right. With supported hard drives, yeah.

**Atari:** Which was done by a guy by the name of Joseph Ruby, who used to work with us at Tannen from us. So I know he did it. I know why he had to do it. But the guys that had done the original PC were not that solid because they were outcasts, right? Well, Sir Ruby was a mainline smart guy.

**Dave Jones:** So you're saying this is even the PC that they showed up with that same show. They even had to redesign that then too, right? Yeah, of course. Yeah, okay.

**Atari:** Yeah, the original PC, the XT was a redesign from the ground up, right? And by the way, I don't know if you remember, they used the wrong disk supplier. And they had to redo almost every XT they sold that year because all the disk drives died. Who was that? Who were they using originally? IBM, I can't remember. Some company that died in Southern California. That's right. Was it Connor or somebody like that? No, no, no, no. It was way before Connor. No, no, no, it was just somebody. What happened was is that IBM, because these guys were under all these constraints, the reason that they couldn't make a better initial machine is because IBM was in this war with Xerox over word processing systems, right? Remember, everybody was buying word processing back in that time, right? And it was a big deal. And Xerox had this big word processing system, and IBM had this big word processing system that was using the 8086. And so they constrained the PC so it didn't hurt that market. Oh, so they were like protecting margins kind of thing? Oh, protecting the market, right? Yeah. They thought these guys had done a Boca Raton and had their head up their ass. I'm sorry. That's totally IBM. Right.

**Dave Jones:** It's just a business thing, right? I mean, just protecting, not cannibalizing, blah, blah, blah. Well, no, the guys at the top end.

**Atari:** Yeah. I mean, that was their knockout. That's the reason that Juggie Tannen got the deal to do the floppy disk for them is because the major supplier at that point was Shoeheart. It was owned by Xerox. So they basically made Juggie famous and rich because they had – so they were going around the industry looking for people that they didn't have to take care of people like Xerox with or Ampex and some of those other guys. So they went with this company that they shouldn't have, but, you know, and they got burned. But it didn't matter. They survived it, right? Partially helped because of Compact, right? That was the year that the you've got to be a PC clone or you die thing happened. Oh, yeah, totally. Yeah. And we lost that company as a result of a bunch of things which I could get into and I won't bother. We made all of the bad mistakes that you can make as a management in terms of bankruptcy lawyers, lawyers, boards of directors, financing. You could get everything wrong and I lost my company. And we came back.

**Dave Jones:** So it wasn't technical vision that killed you? No, no. The problem was I had the technical vision.

**Atari:** We had the technical vision that we needed to go to PC clone. We had started a project inside the company and my engineering manager killed it. And then Juggie and I were going to do – he had it and he had to deal with IBM because of their license. And we could have done it and we just – I couldn't get the – by that time we were behind the curve on the management and the bankruptcy. And we just never did it. We had the vision to do it. And we then two years later did that product for a company called Tandon, right, and built a big computer company in Europe for Tandon, right, which was – which is the first – we did the clone of the AT. We started off doing the clone of the AT, right. Nice. And we were the leading AT supplier for quite a while. And because we were – we had built our own chipset and a couple other things that we'd done before chips and technology. And we had the low cost because we were making our own drives and so forth. So we went into Europe and did very well selling PC clones, right? Yep. And just to finish the PC story – and I'm almost done. I'm sorry. It's dragged on. Oh, that's good. But we had done – when we started the company with Tandon, we would come up with the idea that you needed to be able to move your files and your computer, the operating system, everything. And you shouldn't be able to move that from one computer to another, okay?

**Dave Jones:** As in clone it from –

**Atari:** Just literally, no, take the drive and move it.

**Dave Jones:** Oh, actually, take the drive out. Okay.

**Atari:** So we went to Juggie and said, we want to do this. And we went to Xerox. And Xerox did a case study, a couple of – what are they called? Focus group studies. And we had built this really nice, pretty new package for this thing. And people were in love with the package, right? Because at that point in time, the PC was still this ugly box because everybody was afraid to do a product that wasn't IBM clone, right? So we did this – Bruminated plastic. We did this product. We did this product, this new one with the removal drives and everything. And Xerox helped fund it. And we got started. And we did the thing. And we ultimately built that product, which had drives that Juggie had designed so that we could – we would park the heads off in a special place. And you could take the drive out, put it in another machine at home. And if you dropped the drive on the way, you didn't hurt it, right? And it was called the DataPack machine. And it won our fourth computer of the year. And it was the right idea. But Xerox had to drop out of it because of some internal politics. And right about that time was when the MR heads came along. And disks went from 10 megabytes or 20 megabytes to 100 megabytes to a terabyte in, what, two years, three years, right? Something like that. Because of the technology that IBM brought in and Seagate knocked it off finally and got away with it, right? And the MR head and then TNN had to do MR heads. You know, so the world just totally changed on hard drives. And so we didn't pursue it, right? We got it going. And nowadays, if we put enough hardware on a USB 3, you could match it, right? Right. And yeah, the point is – and we had to do our own disoperating system for that. So we got pretty good at that. So the PC business, the people in Taiwan designed a clone operating – DOS, not DOS, the underlying BIOS – for all the guys in Taiwan. And then they did a couple of things to help the guys in Taiwan. And so all of a sudden, manufacturing went from Europe and the United States to Taiwan for computers. And then, of course, ultimately gone to China, right? And because of that, the industry changed, right? And the other major change in the industry during that time is when we first started off, the guys that we were dealing with were guys who were dropout from DEC or dropout from someplace who were making their own dealer companies. And they really were applications engineers starting their own companies, right? So they were able to support customers. And that was a big deal in Europe. Having the dealer sell your machine and support it became the distribution channel for a long time, right?

**Dave Jones:** And repair and everything else, right? Yeah, yeah. It was all there.

**Atari:** And what happened was with the Taiwanese machines coming in, with the machines becoming more stable and not growing that much, you know, they put more memory in, you put a better screen in, all that kind of stuff. But basically, it turned out that the high-tech stuff had gone away, right? And so, and people started selling, you know, here comes Dell saying, I'll make it for you, right? Buy it from your mail order. And then everybody starts mailing mail order. And these guys who were the applications guys just got eaten up, right? So the computer dealer went away in Europe. And then, so that was a major, major structural change, right? But it happened over time. And the interesting thing now is if you look at Lenovo, who was the big player in China, what Lenovo did was to reestablish that kind of dealer network in China so that they could sell the computers to people that didn't have computers, right? And they literally, they're literally, one of their major strengths is they've got this massive dealer channel. There were people that are selling applications and installing machines and so on. And in China, they have to do that, right? I mean, the people are not here in this country. You're computer literate enough. You've done it and all sorts of things. You just go order another machine, right? Right. Yeah. But, or maybe you're now the best buyer of fries. But in general, a lot of people are buying a mail order, right? And the point is that it totally changed the world. And it was just funny that his Lenovo, in a brand new country with enormous amount of potential, going back to the old dealer network concept, because they need to be able to help people understand what this thing is they just bought, right? Right. And the application. So it's kind of an interesting thing to watch that evolve, right, around the world, right? Okay. So what we've done is we've gotten to machines that are very ubiquitous, right? You know, you buy your machine. Yeah. And we've slowly narrowed it down to either buy it from somebody you know who makes their own and rolls it up for you or you buy it from mail order, right? And that's the PC business in the world. In India, it's mostly guys rolling their own. In the U.S., it's mostly people buying mail order, right? Got it. And so we decided that there wasn't a spot for us in that, right? So it turns out that I had invented a patent on the way to use partial DRAM, right? So when you build a DRAM or you build a flash device, they are 15% to 20% of the parts don't meet spec, right? Right. Sometimes more than in. Dead cells or something like that. Yeah, whatever reason. And so those are sold at substantial discount to people who can find a way to use them. And we had this patent, so we could put two bad ones together and make a good one. And we did pretty well with that for a while. And then we cut a deal with Micron so that we learned how to actually fix bad chips. And so we bought their real junk and $2 million a month and tested them on. How do you fix bad silicon? Actually, every DRAM you buy has been fixed, right? Nobody knows how to make a... Laser. They go in and laser them in, okay? Micron has a patent on being able to go in with a fuse. So they can do it anytime in the system, along. And Micron's not able to do that. Now, flash, they use flash fuses effectively. So they don't have the same issue and there's much less repair done at the wafer level. But... Right. And there's much less repair done. I mean, you can't make a hard... There were... We were doing repair and we would sometimes repair a thousand repairs, each of which took a certain amount of time. Right? And we did that by taking them off the teradines and wafer places people did it and putting them on a little board that did it. Right? And so we could do this repair and then we'd get a chip that we paid 25 cents for and put together when we paid a dollar and sell them both for $4. Right? They're on DIMMs. Nice. Nice business. Nice business. Yeah. Except the problem with the PC business, with the DRAM business was is that there was a period of time when the DRAM business was the golden boys, right? They were the top of the line, right? Absolutely. So guys like the steel company in Japan and a whole bunch of people's built fabs, right? And right about the time they built fabs, people quit buying new PCs. Okay? Ah. What is the time frame here, just for reference? About... See, that would be 2,000 and something, right? If you look at it. Okay, so that... The fastest way to find it out is go do a search on something like Micron and look and find out when they were losing a billion dollars a quarter.

**Speaker ?:** Okay.

**Dave Jones:** This is post the... Because I remember there was a big price fixing thing with the DRAM as well. Yeah, yeah, yeah, yeah.

**Atari:** Yeah, there was. Yeah. But fundamentally what happened was is that they had so much capacity that the price fell below 50 cents and it cost 50 cents to package apart. So those guys were building... You can't shut a production line down. Yeah. So they were building all these parts and selling them at a loss, right? Yeah. Well, you sell a lot of DRAMs at a loss and you lose a lot of money. So what they did is they got together somewhere. I won't admit this, but they got together somewhere and all the major semiconductor players, which by this time was basically Micron, Samson, Toshiba, some guys like that. They agreed to cut over half their capacity over the flash. At the time, they didn't think it was such a great idea, but they decided to do it. And they quit selling partial memories, down memories, which put us out of business. But anyhow, having swapped over the flash was the best thing that ever happened to them. Because by that time, Jobs had come up with the iPad. Is it not the iPad? The iPod, right?

**Dave Jones:** iPod, right, yeah. Right.

**Atari:** Which was flash-based, right?

**Dave Jones:** The first one was a hard drive, but then the Nano and the little ones.

**Atari:** Okay. Then right behind that was the cell phone, right? Which used a bunch of flash. And then, of course, right behind that was the iPad, right? And then finally, the laptop's using SSD, right? And then in between times, everybody came up with the USB, the SSD, and the SD, and the microSD, right? Which was required to make cell phones, you had to have microSD. So what happened was flash suddenly became the thing that you made money on, right? The new dolling of the industry. Right.

**Dave Jones:** That's when I got hired. That was my first job out of school.

**Atari:** Is that right? And people like Sandesk went from nothing to megabillion companies, right? And Toshiba, you know, these guys, the ones that survived became major, major players. And most of them got out of the DRAM business, right? There's only two or three guys making DRAM. Because the flash business worked, and it's going to keep working because it keeps getting bigger, right? There's always a new application for five. So we came up with an invention that lets us buy all of the junk flash and make it all good.

**Dave Jones:** And the companies will still sell you the junk flash? Oh, they love to.

**Atari:** They sell 15%. Oh, okay. Right.

**Dave Jones:** All right. 50% of their wafers, 5% of their chips are bad. 15%. 15% of every chip. 15%. 15%.

**Atari:** 15% of every. Yeah. No, no. They have businesses. A company like Spectac at Micron has made millions for the company. No, no. It's a business. Fall out parts are business. And just that we have an ability to take a chip that other people call a half good or a quarter good, and we can make it all good without doing the repair or anything like that. It's just a patent that was obvious, but I'm the one that got it. Okay. Awesome. So, yeah. But the concept of the USB was essential to help grow the PC business, right? If you think about it.

**Dave Jones:** Right. Right. Just for like the standardization of the bus, you mean?

**Atari:** No, it's just everybody got machines where they could load code and they could send stuff around. They can do everything, right? So, the SD card made the cameras obsolete, right? And the USB eliminated floppies. You can't buy it. Take a look at a new machine from anybody. You don't have a hard drive on it. I mean, you don't have a disc on it. You don't have anything on it except the USB port. Right?

**Dave Jones:** Right. With the extreme example being that new Apple with just the one USB port total. Yeah.

**Atari:** No, but the point was is that it became ubiquitous. It really and truly changed the way. And people don't have any objections that are all just stuffing something in and handing it to somebody else. And, you know, I mean, that kind of stuff. It's the technique, right? Although now with the cloud and everything, it's less important. But it was still a very important part of it. And, you know, they sell lots of them, right? And USB 3 was a legitimate extension and they sell a lot of them. And over time, they'll sell a lot more, right? But the thing that, if you don't mind, I think we say let's make sure we get all the history right so we didn't lose anybody along the way. We talked about hard drives.

**Dave Jones:** We don't want to insult anyone by not referencing them.

**Atari:** No, no, no. I just want to make sure that you understood that guys like Seiler and Stark and those guys created these industries. But they got no credit for it, right? Who's Stark? Yeah, Stark and Stark, Seiler and Scott Patterson did all the disc stuff that needed to be done. Seiler was one of the pioneers in screens, right? In making screens happen. He was one of the pioneers in the audio stuff, right? So, you know, what happened is you got a few people that created this industry that don't get any credit at all, right? Yeah. And, you know, we don't give enough credit to – oh, shit. I mentioned his name earlier. The guy did the first portable hardware, portable computer. Osborne, Adam Osborne. Osborne. Adam Osborne, yep. He was right. He was wrong because he didn't understand the cost of goods, right, and lost his company.

**Dave Jones:** Right. The Osborne effect, the famous Osborne effect.

**Dave Jones:** Oh, is that the – oh, that's Osborne. Is that right? Yeah, yeah. We've talked about that a couple of times on the show.

**Atari:** Anyhow, the point was is that he was right, right? I mean, people wanted a computer that was portable. And when some of the guys in Taiwan started focusing on laptops, we went from a generation that – remember, we move people from the big PC model by our data pack, right? So all of a sudden, you had all these little slim, nice-looking things. But now everybody believes that they can have the same powerful computers sitting on their desk and carry it with them, right? Which is basically the concept we do with the data pack. So a laptop becomes the thing you carry with you. But more importantly, you don't need a high-priced machine other than that, right? Because you can get everything you need out unless you want to set up some kind of lab or service network. So then you buy the machines that go in your server, and then you buy a lot of machines that you can carry with you, right? And we're now in a situation where most new PCs are either going to be server kinds of machines, right, with lots of capability, or they're going to be laptops, right? Of some kind. Got it. They won't be tablets, however, right? They'll have tablet capability, but everybody discovered that the tablet was a wonderful thing. And for people that wanted to show them off and do something with them, they're perfect. My partner watches movies on their iPad and takes it out and gives presentations to customers on it. It's perfect for that, right? But you can't do Excel on it very well, right?

**Dave Jones:** No, you can't do anything. Taping sucks. Yeah, real work.

**Atari:** So whereas a good laptop will do anything, right? I mean, literally anything, right? That's right. I mean, so we think, I mean, not we think, it's obvious that that's the future, right? And so we took a look at that and we took our flash capability and decided we'd make USBs for us, which we did just to be able to make sure we had them to make a lot of money. But we took a look at the SSD market. And at that point, SSDs were selling for like about 500 bucks a piece, right? Yeah. For 256. And, you know, the guys with the hard drives went crazy. They got the ability with the MR heads and the high automation at Seagate. They could build a terabyte drive and sell it for 70 bucks, right? Yeah. Insane, yeah. And they do, right? And Western Digital follow them and they do. And if you want a couple of terabytes, like for your videos and things like that, buy it. There's no other choice. No, more importantly, you get it for nothing, right? You can put them on a machine and they're perfect. But they're ugly and slow and they're not the right thing for your nice little portable laptop, right? So what we did is we said, okay, if we can reduce the flash cost, which we know we can, we can lower the price down to the point where we can convince people that they should only have a machine with SSD in it, okay? And we immediately proved the same thing happened when you went from an SSD machine, from a hard drive machine to an SSD machine. People will not go back, right? No, absolutely. They just said it. The president of the company who did 23 years at SanDisk did all this stuff. The first time he'd actually run an SSD machine because he was bought him and wanted to find out what was going on. And two days later he said, that's it. I'm giving the other one away. Don't try to take this one back. Love it. That's going to happen. Now, Windows, let's talk about Windows for a minute because it's such a shame, right? We lost track of what we were doing with Microsoft. Microsoft lost track of what they were doing. What they would do is they'd do a new operating system. It would help Intel's hot new machine or the new video stuff that people would come out with and so forth and take advantage of the terabyte drive. And so people were upgrading, right? If you look at it, from AT on, people bought a new machine almost every year. Certainly no less than two years, right? And so we built this. It's an enormous base. 1.6 billion people owned some kind of personal computer, right? Okay. The last time they updated was Vista, okay? What?

**Dave Jones:** Yes.

**Atari:** Vista? Yep. Nobody upgraded after Vista, right?

**Dave Jones:** Nobody upgraded to Vista because Vista was hot. That's what I said, right?

**Atari:** It was just – Yeah, right. It was like I had an XP. The next machine is a Vista. No way, right? Yeah. And then, of course – Yeah, right. Yeah. Windows 8 was worse, right? You know? That's right.

**Dave Jones:** Everyone jumped to Windows 7.

**Atari:** Yeah. Everything – Windows 7 was okay, but it wasn't perfect. And Windows 8 was such a disaster. They finally did 8.1. Well, Microsoft apparently, maybe by firing their president and everything, has finally gotten the word, and they're making a version, Windows 10, that is friendly enough that I think people who own an XP machine or whatever kind of machine will be able to use the new machines very effectively, and they'll work just like their old machine. Okay?

**Dave Jones:** Yep. And the interesting thing is it's going to be free.

**Dave Jones:** That's right. The upgrade is if you have 7 or 8. Yeah.

**Dave Jones:** Even for people who've pirated it before. It's going to be free.

**Atari:** So now I've got Windows 10, right? And I've got a machine that has in it 256 GB SSD. I know you guys use stuff with your disk and everything else, and that's the reason you've got a USB port and hook up to all these great big storage devices that you don't carry around with you. But 256 GB is a big number, right, with all the respect. Yeah. Yeah. And so you can get a 256 GB machine for probably under $500. Touchscreen. Right? Yeah. And that's next year's future. Now, what we've done is we found a way to make the SSD much faster. How much faster? Sure. Just depending on if you run the test, it's considerably faster. Literally compared. It's like the hard disk, right? You know what I mean? Once you've started using it, it's faster. But, you know.

**Dave Jones:** It's a one-way path. You're not going back after that.

**Atari:** Well, no, and more importantly, it's faster and it's better, but it's not faster and better enough that you would move from one SSD machine to another probably, although we may get there. But right now, remember, there's 1.6 billion people, most of whom do not have SSD machines. Okay? And we think that if we can talk one of the big guys like Lenovo or HP into announcing with Microsoft the new Windows and the new SSD machines with the high performance, that people who have a machine today will look at it and say, Christ, for that kind of money, I can get that something. And you only got to get them to use it once, just like I did the hard drive. Right? They'll buy. Right? I mean, right now. How do I get the money out of my pocket? Yeah. You take checks still, Chuck? No, I'm serious. I mean, I've been in this industry where we got away with that crap, right? And they'll get away with it now because it's that better a machine. And so we have great hopes that we're going to sell the SSDs into that market and build a nice little company. And you just got a patent on that last year? Yeah. Basically, the thing that we've done is, because this is a technology group, we file patents and all that stuff. We put, and we don't have an SSD that runs Flash. We have an SSD that runs DRAM. Okay? Right. So it's so fast because it writes to a DRAM. Flash takes a long time to write and has issues. Flash wears. This doesn't wear out because it's going to DRAM. And then what we do is we write the Flash as an archive. So you have the Flash and you have the hard drive, but you're running basically a DRAM SSD.

**Dave Jones:** How do you handle power loss if there's an instant power loss?

**Atari:** With all due respect, that's an easy thing. Somebody invented the super cap. Yep. You put it, you put... And that's enough? You've got enough energy in the super cap to ride?

**Atari:** It's only... You've got to remember how fast you can dump. If you've got 32 Flash devices, you can dump everything on a 4 GB drive to that in like five to seven seconds. And you can easily make a... That's still a lot for a super cap. No, no, no. It's not. 25? Yeah, no, no. The new super caps with the right power supply, 25 cents.

**Dave Jones:** Okay.

**Atari:** Yeah. It's a system we put in, right? But we can protect the system. And there's some tricks we can do where we actually can recover. We built it so you can recover instantly from any downtime. We actually, every time you shut the machine down, we do a snapshot. So when you pile the machine back on, it's exactly where it was. The files are exactly where they are. There's a bunch of stuff like that that can be done easily. So the machine is a lot better. It feels a lot better. It operates a lot better. And we...

**Dave Jones:** Does this mean that you're now dependent on DRAM pricing though? No. No, no, no, no, no.

**Atari:** I remember I bought DRAM cheap, but it turns out...

**Dave Jones:** Oh, I see. Okay, okay. So it's because you have the technology that can use the bad stuff.

**Atari:** I could, but I'm not even bothering because the DRAMs we're buying, we don't... Because of the way we're doing this stuff, we can use the DRAM and just have holes in it rather than doing the other stuff. But we can do the other. We have patents on how you put DRAMs on boards. We're building all of this stuff directly from dye on the boards. There's a bunch of stuff we're doing to lower the price, right? And the idea is to get the price point again. That's what we did with the hard drives that we did with the Commodore. You know, if you get the price point right and you get the performance right, they will beat a path to your door, right? I mean, we sold a million C64s a month, right? Yeah, crazy. I mean, you know, nobody believed it at the time. But, you know, the point is if you've got a product that people want, you can sell a lot, right? And do people like Atari, Nintendo, you know, ultimately now I guess Microsoft with the Xbox. You know, there's enormous businesses out there, right? And so that's where we're going. That's where we're hoping to go. And we think that if it works out, we will help bring the PC back to its right place and find it because our product works better than an Apple, which has been kicking the butt at the PC.

**Dave Jones:** Awesome. So at 78 years of age, you're still pioneering the computer industry? I hope so. I love it. I hope so.

**Atari:** Yeah. Listen, I'm healthy. You can't see a picture of me, but, you know, I run. I saw a picture. You look healthy as hell, man. I run at least an hour a day and I get my heart rate up beyond maximum and I've stayed in shape. And, you know, what we've proven, I went to a party with my partner and this party is full of 60-year-old women who look 40, right? And act 40, right? You know, age is a little different than it used to be, right? Yeah. Yeah. Yeah.

**Dave Jones:** I'm just, I think not even, I mean, age, yeah, you're right. Age, whatever. I mean, just, man, the fire in your belly though, man. That's what I hear, you know? Oh, yeah.

**Atari:** But people like Gene and all these other guys that I've got that I brought back, I brought some guys back, but I've also got the young guys. I mean, I got this factory in Sri Lanka that's desperate to go back to work, right? Because we built up a great thing and we built a lot of special stuff. We have a lot of patents and stuff like that.

**Dave Jones:** Sri Lanka, who's doing anything there? I mean, that's just, like, that's just something we don't, that's just a country we don't hear about.

**Atari:** What? Places like Sri Lanka? Well, probably because they had this big riot, rebellion going on and everything. But Sri Lankan requires that every child graduate from high school. Okay?

**Dave Jones:** Oh, wow. Nice.

**Atari:** Yeah. Okay? And if they don't go to high school or they don't go to school, the parents go to jail. Okay? Wow. Wow.

**Dave Jones:** That's one way to do it. No, no.

**Atari:** But Singapore did it, right? The guy at Singapore is such an absolute. Oh, right. Of course. Everybody is a high school graduate. So, you know, you go to Singapore now. Are they doing assembly and doing cheap shit? No. They built an entire infrastructure based around being smart.

**Dave Jones:** Weren't they the ones who focused on, like, the innovation curriculum, too, or something like that? Was that Singapore? Oh, I don't know. They, like, the Japanese favorite. I thought I was listening to something. But it doesn't matter.

**Atari:** The point was is that if you've got an educated populace, right? And, you know, like, for instance, I have these, these are really small people, right? The ladies are pretty small and everything. But we do, and we build our products highly automated in the sense that we don't use a lot of robots, but we have the computers are managing everything and keeping track. And, you know, everybody was saying, well, you know, you got this thing where they have to have good manual dexterity. I said, look, every girl in that country learns how to sew from her grandmother from the time she's six. Right?

**Dave Jones:** Ah, interesting.

**Atari:** Right? So they know how to sew, right? They've got dexterity because they had to learn it because their grandmother made them, right? Because for one year before, one generation before that, she had to sew all her clothes for her family and her husband, right? Yeah, of course. So what happens is you go into some of these countries and you get these great skills with great intelligence, right? And you can build factories that do marvelous things, right? I've qualified with multiple companies with that factor. And it's not expensive. Awesome. Right? So we'll build a lot of product in China because our customers are all in China. But it doesn't matter.

**Dave Jones:** What's your view on China and where it's headed in terms of pricing there, labor pricing? Okay. All that sort of everything.

**Atari:** So the labor goes higher in some places, right? But it doesn't go out of sight. I was in India when software guys quadrupled their salaries in a week, right? Because of what happened. Did that mean that they went out of the software business? Hell no. They're the richest people in the world because of software. You know, when you're starting from a base of 20 cents an hour or 40 cents an hour, right? You can go a lot of places without destroying the economy. And it's a question of how you use the people and how you train them. But remember, that country hasn't even begun to touch its rural population, right? They're bringing it in. But, you know, go to Western China, right? And those people are still living out of grass huts and, you know, crapping outdoors, right? I mean, no, no, no. China has enough resources to do what they want to do.

**Dave Jones:** Do you see them sticking with them being the assemblers of the world? No. Or do you see them becoming the technical innovation power?

**Atari:** Read about Lenovo. Lenovo was started by a guy who was head of a company called Legend, which the government started. They gave him money to start. And he's a fundamental investor. His stated goal, and with government supporting him and him doing this with companies like Lenovo, he's saying that we are going to be innovators, not assemblers. And we're putting the money into schools. Now, they've got a tremendous problem getting, catching up. Yeah. And because they killed all their intellectuals for almost 20 years, right? Remember? They did that, right? So you get a company like India where they've had continuous Indian schools are better, right? But they're spending the energy and they're bringing people from India going in. I mean, China will get there, right? I believe they'll get there, right? There's a couple of other places they might be going that the rest of you wouldn't want them to get to, but I think they're going to go there too. So they're not building a whitewater navy and the best military in the world for nothing.

**Dave Jones:** No, that's right.

**Dave Jones:** Oh, right, right. Yeah, yeah. The geopolitics stuff gets a little dicey pretty quick.

**Atari:** Well, I totally believe with the guys that predict that they're going to attack north through Siberia and take Siberia away from the Russians. And I work for the Russians. Why?

**Dave Jones:** Why would they want that?

**Atari:** It's got a funny little thing called oil. China is one of the world's biggest. Oh, yeah, right.

**Dave Jones:** Yeah, yeah, yeah. It always comes down to oil.

**Atari:** Well, it doesn't always come down to oil, but there's also all kinds of minerals and everything else. And so they let the Russians keep the gas and they take the oil.

**Dave Jones:** Yep.

**Atari:** And the Russians are five times those. I love Russians. I enjoy working in Russia. Russia's got tons of smart people and no industry to support it.

**Dave Jones:** I was going to say, is there tech up there at all?

**Atari:** Oh, very high tech, right? Oh, yeah.

**Dave Jones:** I'm pretty sheltered here, Chuck. I don't know if you can tell. No, no, no. I'm serious. I was in Russia. Talking to Aussies is the extreme of my internationalism most days.

**Atari:** Yeah, the problem with the Aussies is they party so much it's hard for them to be the high intellectual capability.

**Dave Jones:** Yeah, that's it.

**Dave Jones:** Just too damn beautiful outside.

**Atari:** They just keep going hanging out at the beach. I don't know. Australia has decent schools and good research. They just don't have enough people, right? I mean, if you look at some place like Perth, they're starting to get somewhere, right? Sydney's problem is you can, you know, it's like here in the States. If you're a pretty good smart guy, you don't go into technology. You go into investment banking or real estate, things like that, right? You know, because the money is there, right? And they, you know, I mean...

**Dave Jones:** Yeah, how's that been seeing that? I mean, because obviously when you were starting, there was, you know, there's just huge margins on tech and everything like that. How has that shift been?

**Atari:** I've never been able to hold big margins because I screw them up, right? We've always been...

**Dave Jones:** You keep innovating.

**Atari:** We're always the price leader, right? We're always trying to build something cheaper than everybody else to build the volume, right? And yeah, so we were not in the high margin business. We were in the fund margin business where you sold a lot and made money by selling a lot, right? And I think both Jaggi and I and a couple of... Some people like that, all those guys were of that philosophy. Tremel used to say, I'm not building for the classes, I'm building for the masses, right? And, you know, so I think the answer is that HP had high margin business and they're having to split the company up, right? I'm not sure that the world supports high margins except on innovation of some kind, right? I mean, you got Xerox with 19 years with the patents, right? I mean, they had a lot of fun with that, right? But, you know, that's okay, right? The economies are good enough that if we keep people working and keep them focused, and that's part of our problem in this country is we took all the jobs and sent them to Asia. No, I'm serious, right? Yeah, I know. You know, these guys, when they got laid off at the auto factories, they were saying, well, that's good. I can go to work. I'm going to go to work doing accounting or something other because it's a lot easier. And they were right, right? But that job went second, right? And those jobs didn't come back. Luckily, Obama saved the automotive industry, but the accounting jobs and that stuff haven't come home, right? And we haven't given anybody the economic incentives to bring them back because everybody wants to talk about cutting this tax. What they need to be doing is giving people credit in some form or another for doing stuff onshore that they moved offshore. And I don't see that happening, but it needs to happen, right? I mean, because, you know, Sri Lanka, 100% college graduate. Counting people, I mean, high school. Tell me about the average people who are really educated that graduate from our high schools now. About 50%?

**Dave Jones:** Oh, right, right. Well, at 100% graduation from Sri Lanka, you can't say if that's the same, if that's actually 100 either.

**Atari:** It's pretty close because they didn't get through, right? They stayed and worked hard and did everything else. No, no. By the way...

**Dave Jones:** Yeah, I mean, that kind of focus on education is huge. I mean, I think that...

**Atari:** My only point was is that we're ruining our future by not educating. We don't have an apprentice system in this country, but we desperately need it. Ask yourself... I totally agree with that. Ask yourself if you've met a master machinist of any age, right? Yeah.

**Dave Jones:** No.

**Dave Jones:** Right?

**Atari:** They died. I don't know. They died.

**Dave Jones:** I know a lot of machinists, but...

**Atari:** No, but they died, right? And because there isn't an apprentice system and a reward system for those guys. I mean, we just... We don't... But the reason I mentioned that, it's a fundamental technology, right? Right. No, definitely. Yeah.

**Dave Jones:** There was an article I saw this week from a local... Because, I mean, Cleveland's built on manufacturing and stuff like that. And just like... You know, one of the biggest threats around here, at least, is if the stock market keeps going and doing okay, all these guys who are 60, 65, you know, they start eyeballing that door and it's like, hey, nobody's here. You know, there's no one behind them. No. So, that's a problem. Yeah.

**Atari:** Yeah. And they also got arthritis in Cleveland because of bad weather. I'm not being smart, but it's true. I live in California where everybody is fit and running and having a good time. That's right. That's it. Yeah. I'm happy. That's the way. Yeah, yeah. But... And I don't even want to talk about Sydney. Sydney is one of the garden spots of the world, right? Yeah. Absolutely.

**Dave Jones:** That's why it's so bloody expensive. Yeah. Well, it should be, right?

**Atari:** Well, I want you guys to have to...

**Speaker ?:** Right.

**Atari:** Yeah. No. It's one of the best. I want you guys to have to earn all that good shit, right? I mean, you know... Yeah, that's it. No, no. But, you know, no. We...

**Atari:** I guess I'm getting philosophical, but... Education is an important part of... Education is something that we have to spend time on. And in Managiana, we're not doing that, right? And motivation... And I'm not talking about every kid being a philosophy graduate. I'm talking about there's a whole bunch of kids that should be learning machinists, carpentry... Oh, hell yeah. Things like that. And they're not, right? Right. They're just not getting the... And by the way... Okay. So, maybe we'll be able to print all the new prototypes and everything. But remember, you couldn't build a product.

**Dave Jones:** I was so hoping you were going to say chips right there, Chuck. I know you weren't, but me and Dave have a long-standing thing. What about printing? Sorry, go ahead. Oh, no. The printing... Printed chips, I was saying. No, no.

**Atari:** What that printed thing is... By the way, that's a beautiful technology. And I don't know if you know it or not, but that technology has the computer clubs that drove the PC business now. Yes. Right? Yeah, it does. Absolutely. These guys are...

**Speaker ?:** Yep.

**Atari:** Totally. Yeah. Remember I mentioned...

**Dave Jones:** You're talking 3D printing, right? Yeah. Yeah.

**Atari:** Remember I built and mentioned Seiler? During at work, he does 3D printing for an industrial design group. At home, he has 3D printing he's built and he goes to all these clubs because it's the new hot technology and they can do wonderful things with it, right? Yep. And robots, you know, because of the microprocessors, because of the ability that we've done with being able to build materials and things like that. And, you know, in the focus of some of the great stuff they did as a result of trying to make up to people for how badly we damaged them in America. So we've built prostatic arms and we're doing things that are very major breakthroughs in robotics, right? Yeah. And those are the futures, right? I mean, you know, I became a computer guru, right? Which I like to think of myself as at least a little bit of one. Because in high school, in college, my junior year, I learned about computers from a guy that had studied under Claude Shannon and worked with Claude Shannon. Oh, nice. Wow. And the point was, is he built into me a belief that computers were something I wanted to do for a living for the rest of my life and I have, right? Yeah. And what I'm saying is, is we need robots as that now, right? I mean, there are things like that. But you and I are talking about things we know about, right? 3D printing and so forth. If I asked you 10 years ago, would you have said 3D printing? No. Five years ago, I barely would have said that. What kind of printing? What I'm saying is all of these things are happening now and we can grow our businesses and our economies and everything, but we're going to leave half the population behind because we've screwed them up, right? Right. And I hope we're going to fix that, right?

**Dave Jones:** What is your view on the computers, the educational computers these days, like the Raspberry Pi?

**Atari:** I haven't looked at any of that stuff, but I've got one little story which we'll tell, which is fun. When we first did the Commodore, right? And I went to Europe and I was bringing it back. The PET, you mean? Yeah, we just did the Commodore and we announced everybody and we told people. So I gave a lecture in New York or someplace saying that I think the computers are going to change education, which they did, of course, right? Right. I landed at the San Francisco airport and there's a bunch of reporters there, right, to refute me saying that computers are going to change education. And they have a parallel presentation on the news with this little old lady schoolteacher that says you can't change the way people interact. It's with humans. Well, guess what we've learned, right? Okay. Most of the teachers don't interact properly, right? Exactly. And computers at least helped, right? And, you know, so I think computers have, I mean, I think if people find a way, look, people are really starting to project that we won't go to school, won't go to college in 10 years. You'll do everything online.

**Dave Jones:** That's crazy. Yeah. Well, I don't know.

**Atari:** Everything online, right?

**Dave Jones:** ASU will... Dave, I'd like to introduce you to my program. No, no, but think about it.

**Atari:** ASU now will give you a series of pretty good degrees without ever going to school, right? Yep. And there's no reason why they can't do some of that, right? And, you know, and talk to...

**Dave Jones:** There'll be a market for it, definitely. I don't think it'll be the future, though. I don't think it'll be the only future.

**Atari:** I've got grandkids in college now, and I've had kids in college and everything, and they're not satisfied with what they're getting out of the schools, because the schools, I talked to, we have a tenured professor, he's a brother-in-law, pseudo-brother-in-law, and he's saying that we don't get to teach anymore, we just teach to get them through school, because they don't give a damn. Yeah, yeah, that's right. Right. And so what we...

**Dave Jones:** But the world is so complicated these days, though. You can't learn everything at school. It's not possible. And you can't learn everything in one online degree, either. I mean, it's...

**Atari:** No, but let me just tell you something. There's a thing called internship and apprenticeship, which should be the future, right? Totally. So you should be able to get some online education... Good for me. ...and go to some school or some company where you apply some of that stuff and get paid poor wages, but do something useful. Yep. And then go on, right? Just like in general title. Siemens does that. Yeah. But it's just going to happen. That's what I got... When I came out of college, I didn't know anything. When I left my college, there wasn't one computer on campus in 1959. Right. Not one. Right. So why am I going to learn about computers on campus, right? Right. Exactly. There's one guy. Right. So my point is that what's happened is, okay, so now we've got computers on campus. Great. But what I'm saying is that the future isn't about holding hand-holding at the college level. Right? It's not that...

**Dave Jones:** No, no.

**Atari:** Totally. And maybe what you do is you have a whole bunch of people who become therapists for guys who are studying online. Yeah. I like that. And meet with them and hold their hand and tell them they're doing okay. I don't know. Right? I mean...

**Dave Jones:** No, that's like a recitation session with an online program. Totally. I totally agree with that.

**Atari:** Yeah.

**Dave Jones:** I don't know. See, that's the thing. The future is like it's no different whether you go to college to learn something or whether you do an online degree. You're both... You're always going to come out knowing not a huge amount. You have to apply it practically and do...

**Atari:** If GE hadn't had a training program... The reason I went to work with GE is they had a training program. Yeah. They trained me. I worked for my first year troubleshooting nose cone failures.

**Dave Jones:** Right? Nice.

**Atari:** And I got involved with the beginning of the electronics industry in the United States because I had to go out to these companies that didn't know what the hell they were doing and help them try to figure out how to build stuff so we could... Right. And what I'm saying to you is that all of that training was invaluable to me. Right? Absolutely. I went to school. They let me go design a small computer thing while I was going to the training program and that then led to a job there. But what I'm saying is that when I came out of school, I looked at what I said. I don't know anything. Right?

**Dave Jones:** Yep.

**Atari:** I'm going out into industry and they're going to expect me to know something. Yep. Right? Well, luckily, G did. Right? But... And I don't know if they've changed that philosophy now or not. I don't know. Right? I mean, I would hope not.

**Dave Jones:** I... In our... In the engineering industry, it's considered... Like, you know, it's a basic fact that when you come out of college, you know nothing. You know? Like, you know... Like, you have a basic foundation, but you essentially are completely clueless about how to do any practical work. Yeah. And that's got to be the same regardless whether or not it's a real college or whether or not it's an online course. Oh, yeah. No question.

**Atari:** It's... You know... So companies have to have their own training programs. Absolutely. And people... We should be giving them tax credits for that. Right? I mean, we should...

**Atari:** I totally agree. Yeah. I mean, we should do things. I'm sorry. We got off into...

**Dave Jones:** No, I'd actually love to tell a story because it pissed me off so bad. So I was at... Go ahead. I was at... I was at the ECE Department Heads Association conference on Monday and Tuesday this week. And there was a panel and they were talking about the subject. Why can't we hire talented graduates and stuff like that? And there are all these... And it was all these industry people up on stage. It was like a panel of industry, like high level execs. Yeah. And the guy... And so one of the guys... And I won't say where he's from because I don't want him to get mobbed. But he gets up and they're all doing like slides and stuff like that. And he says, I know we keep talking about all this practical stuff, but I just want to keep saying, please... Please only teach theory. And I'm like looking around and I'm like in the back of the room. I'm looking around and all these like ECE Department Heads are like nodding their heads. And I'm just like, where am I? What am I doing right now? Where am I? Is this the Twilight Zone? I'm like, what the hell is going on here? And so at the end, I'm just sitting back there seething, you know, just like with anger. Obviously, you know, I teach a practical electronics program. And so I get up during the Q&A. I'm like, what are you talking about? Why... What did you mean by that? Are you guys willing to train people? That's what I asked them. You know, because I know that none of them are because of the cost and people leave companies early and stuff like that. And he's like, well, no, I didn't. You know, he kind of backtracks. No, I didn't actually mean that. He said, what I really meant was when I interview people, when I interview people, they don't... They aren't able to answer my questions about theory. And I was just going, but that's because you don't ever teach them anything practical to go along with it. And I'm just... I was just like going nuts. Sorry about shouting, but I was going nuts. And it was just like... I was like looking around, I got to get out of here. Because it was just like, that's unfortunately what the state of it is right now. And Chuck, I'm totally on board with you, man. We need apprenticeship. We need practical tie-ins and stuff like that. And it's just like, oh, it was terrible.

**Atari:** And internships work, right? Yeah. And they really do work. If companies support them, they work. So I think your online system has some internships built into it. And that gives you some reality checks and puts you back on track. Yeah.

**Dave Jones:** Yeah.

**Atari:** I mean, my internship was stacking lumber in a lumber yard. Right. Yeah. I was poor. That was the best-fitting job. Right. But I wouldn't have learned anything anyhow. I was coming out of school and the transistor was invented. How would I have learned anything? Right. Exactly.

**Dave Jones:** Where do you get that stuff? For the bluting instincts, you have to get... You have to work together.

**Atari:** Yeah. Particularly now. Some of this stuff is starting to happen. But, you know, we're still going to... I hope we're going to keep seeing breakthroughs. It makes my life more exciting, right? I mean, and your life more exciting.

**Dave Jones:** Yeah.

**Atari:** So anyhow, we got off track. I think I covered everybody. Tell me I got everybody. Oh, I got to give credit to something that you guys should give credit to. Yeah. The Computer History Museum...

**Dave Jones:** Is awesome.

**Atari:** Yeah. ...has started a program over the last two or three years where they've taken everybody who did anything and brought them down, put them on videotape, and recorded them because they were afraid they're going to die. Yeah. Fantastic. It was started as a result of jobs, right? Yeah. I mean, they realized that they missed this enormous opportunity to ask him to tell us about life, right? And so they've done that, and they're still doing it. Yeah. And I don't think they're getting enough credit, and I don't think people know that that's a resource that they should be tapping.

**Dave Jones:** No, I think we mentioned that the other week on the show. Didn't we, Chris?

**Dave Jones:** No, that was a Stanford program going on. Oh, Stanford. Stanford have a similar program. Which is early.

**Atari:** Yeah, I want to know. But these guys have... I mean, I'm an interviewer. I didn't go on tape at Stanford, but me and all my buddies and everybody else, and I just gave them the reference to the guy that may have done Seamon, Sirach, well, and the guys who really did something. Yep, exactly. And by the way, they weren't all right for damn sure, right? A whole bunch of people did bad things. But the fact that we've got them trapped on tape and recorded... Yeah, that's right. ...is enormous. Well, no, because it's a learning experience for what's going to happen next, right? Yep. So I'm totally backing that program. I want you to tell everybody about it. People should be using it for any research they do in the industry because you'll get four different views of the same subject. Yeah. None of them which match popular science, right? Right. Right. You know, because a lot of those stories are wrong, but they weren't wrong when they... But what these people have told is what they remember about the truth, and that's all that matters, right? Right. Because, you know, you get a guy like Gordon Moore, right? I mean, think about how important that is, right? Exactly. Total. I think they missed... I'm sure they missed noise, right? Oh, yeah. Right. Yeah. But it would have been wonderful to talk to him.

**Dave Jones:** Well, I mean, on our show, we've talked about it too because, you know, like we weren't big enough, but like, you know, Jim Williams and Bob Peace and then Hans Commons and like all these guys passed away kind of in a short period. And, you know, they were like...

**Dave Jones:** They were on our list. Yeah. Like they were on our list to be interviewed, you know? Yeah. And like... And they passed away.

**Dave Jones:** Yeah. You know? So, yeah. That's an invaluable... Do you know that... Is there a specific name of that program or is it just the video history?

**Atari:** I think it's video history. Okay. And I may have the person's name. If you don't, I'll send you an email from her.

**Dave Jones:** Yeah, that'd be great.

**Atari:** That runs it because I just don't think it's being promoted enough and it's such a great idea. And they really work hard. They've gotten a whole bunch of people that you might not even thought they might get. Yeah. And it turns out that most everybody who's been in the industry suddenly realizes, yeah, I haven't had a chance to tell anybody my story and it's going to die with me, right? Yeah.

**Dave Jones:** I think it's called the Oral History Collection. That's what I found online. Yeah, I think so. Something like that.

**Atari:** Whatever it is, it's a great idea. That is very good. That's awesome. And so, guys, I've dragged this thing on out. I assume you're going to edit it down to nothing. No, it's not.

**Dave Jones:** You've got like six more hours. We can keep going, man. But I guess we should probably let you get home and eat dinner as well. No, no, no.

**Dave Jones:** I've got a few more questions, Chris. Go ahead. Well, actually, one comes from Bill Hurd, who you obviously know. And he wanted to know, he wanted, I think, to us to ask you about patents on the 6502. Were there any? What was the...

**Atari:** Probably at the beginning there were. And Minch may have done... See, the 6502 went through two evolutions, remember? There was a 6502, which we did, which was designed to do what I said. It was supposed to be the basic building block. And then when we went out and after Commodore threw out Minch from his company, he needed a job. We needed to get something done. And Rockwell, who had taken a second source in the 6502, said, we're making this investment in CMOS, which is the thing I'm sending the guy up to, to the History Museum, who says he's the guy that did CMOS for Rockwell. And they said, we'll fund you, right? And so Bill went in and put fixes into the 6502 that he thought ought to be in there, right? And then he did the 816 with a lot of help from Apple, right? So, you know, he extended that product pretty well, right? So, and I think he patented some of the stuff that he did, right? They would be long since run out. Oh, yeah, of course.

**Dave Jones:** Clone away, folks. Just go ahead for it. Go for it.

**Dave Jones:** And what was your take back when the Altair came out? What did you think of that? Were you surprised by its success?

**Atari:** Altair.

**Dave Jones:** Yeah, the Altair. Like as in the front cover, you know, touted as the world's first personal computer kit.

**Atari:** Oh, no, I think that was, remember, remember that was the first, for the group that they cover it was on, those were the hobbyists, right? They were the hobbyists, exactly. That's right, that's right. You know, they were the guys that were building their own TV sets and everything else. So it was absolutely the first, right?

**Dave Jones:** But that was the same year that the 6502 came out, 75.

**Atari:** Yeah, but they were doing something different. They were making a computer, right?

**Dave Jones:** Right.

**Atari:** And we were doing, the 6502 was not designed to be a computer product. It just happened to be because we were running Interpretive Basic. We were able to use it for that. It was designed to do what it did. It's a great control device. My new chip has 11 6502s in it.

**Dave Jones:** Nice.

**Atari:** Your what device? My new chip. My new SSD chip.

**Dave Jones:** He's the latest patented flesh drive thingy. Oh, really? A really flesh drive thingy.

**Atari:** Yeah, that's awesome. No, the reason it has 11 is because the 6502 was, remember we talked about task processing and distributed processing? The 6502 was designed to do something. Just one thing, right? Do it well, do it cheap. Yeah. And if you want it to do something else, get another one and let that one do something else, right? I mean, and everybody has gotten carried away with seven processors and everything else. And if you look at the operating systems that support those, they're enormous and they've slowed them down and everything else. Distributed process, that's what 6502 was for, was distributed process. It turned out that because of BASIC, we made it into a nice little computer, right? Right. But I guarantee you, when we did the MS-DOS machine, we put 6502s in the controllers, but we didn't put one in the main computer. We were going to go for a machine that was more serious, right? Yeah.

**Dave Jones:** Right.

**Atari:** With all due respect to the word serious.

**Dave Jones:** Serious, yeah. Unintended.

**Atari:** No, but I'm saying that, no, 6502 wasn't a competitor to Altair. It wasn't anything. 6502 was supposed to be enabling the low-cost applications of computers, and it did. Got it.

**Dave Jones:** Yeah.

**Dave Jones:** And were Apple using, because Apple were a competitor of Commodore, obviously, were they using the second-sourced 6502?

**Atari:** Yeah, yeah, from Centitec. Ah, right. Okay. And Rockwell. Yeah, but it didn't matter. Their volume was never that heavy, frankly.

**Dave Jones:** So were Commodore getting a sort of royalty on those second-sourced chips? No?

**Atari:** No, but we wanted the product to be second-sourced, so we took a fee from Rockwell and we didn't take any from Centitec. Okay, so you got a fixed fee and then, yeah. No, Centitec was making it to give us a second source to give us credibility and because we both did Atari, right? I mean, we made serious money off Atari, right?

**Dave Jones:** Oh, yeah. Yeah. So do you think too much credit these days goes to Jobs and Woz because they're the most memorable?

**Atari:** No, I think they had a guy by the name of Regis McKenna who was a great PR guy and they've had a continuous PR campaign from then till now, right? And Woz gets to tell stories that aren't true anymore, right? No, no, I'm saying.

**Dave Jones:** Like, like, like, what are your favourite non-true Woz stories?

**Atari:** Like the thing about going into his place where they have it. Yeah, the suit on, right? Oh, right, you're right. And asking him for help doing the patent, right? And he was right about what should have been done in the patent because he was totally wrong. He missed the basic altogether, right? Right. That's a famous argument, right?

**Dave Jones:** And then you going in there and fixing the Apple I.

**Atari:** Yeah, but we also, the guys that came in from outside had to fix the Apple II because Woz wasn't an engineer at the time and he made two or three basic mistakes on the Apple. But it didn't matter, right? It wasn't that. It was the, remember, people didn't care that the 6502 was at the heart of the Apple. What they, I mean, they cared about the basic, right? And the screen editor we put in. And ultimately, a bunch of people bought the Apple because of some of the stuff he could do with graphics. And ultimately, the reason it saved Apple was the, was VisiCount, right? VisiCount saved Apple. Oh, of course, yeah. It made the Apple. Yeah. Spreadsheet made the Apple. Save it. Yeah, totally. By the way, I'm going to give credit one more time. I keep forgetting some of the people to give credit to. The guys that did VisiCount did the first personal computer program that wasn't like anything else before.

**Dave Jones:** Yeah. Absolutely.

**Atari:** Right? Nothing like it before. Yes, Microsoft's done Excel and everything else and all of us use it, right? And by the way, what the hell?

**Dave Jones:** VisiCount was Dan Bricklin, wasn't it?

**Atari:** No, no, no, no, no. It was, I'm going to kick myself if I forget their names. Look them up because there was two guys, and I know about their names. I just don't remember them right now. But no, no, it was two guys from Harvard. It's a Harvard story all over again. There were two guys from Harvard that came up with the idea while they were going to school, right? Bricklin is the guy that was promoting it, right?

**Dave Jones:** Oh, right. I thought, oh, okay. Right.

**Atari:** Frankston? Frankston? Yeah, Frankston's one of them. No, no, no.

**Dave Jones:** Oh, Bob Frankston. Yeah.

**Atari:** And then there's the other one, right? Anyhow, those two guys absolutely invented it. The Lotus guys came in and made it somewhat better. Excel came in and made it better.

**Dave Jones:** Well, Lotus owned the PC market for it. They took the gamble to write it in assembly language for only the PC, and that's what made Lotus 1, 2, 3 so famous.

**Atari:** But my point was is that Excel is a great product. Totally changed everything. Yeah. Yeah. And by the way, when we went to Bremerton the first time, Gates had moved there not to do operating systems, right? He had the basic, but he was just selling that. He went there to set up Word, things like that. He saw that as the future, and he was right, okay?

**Dave Jones:** Yeah. That's why he brought in Charles Simony. He worked on the early office product.

**Atari:** There's a funny story about the guy from Xerox, right? And it's somewhat public knowledge, so I can tell you. It will be after this. Yeah, exactly. I've told this story before. The Gates knew for lots of reasons that he needed a good word processor. Gates has the same problem with words that I do, right? I mean, you need a word processor to be able to communicate. Okay. And so he wanted the guy from Xerox because Word was a superior product, right? It was built into their start. The star. Yeah, the Xerox star. Right. And he couldn't get the guy to join him. So he went to this guy, Dave Marquardt, who's one of the original investors in Seagate, would have been an investor investor in Sirius, and Gates told Marquardt, I will let you invest if you get this guy for me. And Marquardt went out and got him. And Marquardt's the only venture capital investor, and he's still on the board. Oh, wow. And he changed Microsoft forever, right? I mean, the work he did on Word changed and made them a true application software company, right? Yeah. And then I'm not sure if he carried over into Excel or what, but, you know, Excel turns out to be a great product. But ultimately, Windows Explorer became a great product, right? I mean, presentation manager, all these things became good products after they decided to go do them, right? And so, you know, in terms of their application suite, they've got a really strong application suite, right? And that's where they make all their money, right? Yeah, of course.

**Dave Jones:** That's why they're now looking to not charge for their OS anymore. Right. Yeah. Why not? Yeah.

**Atari:** No, seriously, the applications are really important. They change the industry every time they did them, right? They got them right. And, you know, would you give a presentation today without presentation manager?

**Dave Jones:** I try not to give presentations.

**Dave Jones:** Well, yeah, it's like death by PowerPoint, you know? But, yeah, no, still, you've got to have something like that.

**Atari:** No, that's what I'm saying. It's a nice tool if you want to make a lot of presentations because we're trying to get the company funded and everything, right? And, you know, it's just a great tool, right? I use Excel to do my budgeting and keep my books, right? Yeah.

**Dave Jones:** And it's so part of the business paradigm these days, too. It's just like, it's just assumed, you know? Yeah.

**Atari:** And so what I'm saying is, so he got it right, okay? He did get it right, even though he screwed up the operating system. Not he, but they screwed up the operating system. I mean, Windows. I had a big fight because I had seen, okay, I'm sorry, this one story I didn't tell you yet, but I'll tell you now. This is right. I was at Apple for a short time because they kind of lied to me and I made some mistakes leaving Comet or any help. But anyhow, neither do I.

**Dave Jones:** Did Jobs hire you or what was the? Yeah, yeah.

**Atari:** It's actually the president hired me, but yeah, Jobs. Oh, right. Okay. And I was, Steve and I were working together on what became the Lisa, okay?

**Dave Jones:** Oh, wow. Steve Jobs or was? Steve Jobs was.

**Atari:** He didn't do any architectural work.

**Dave Jones:** Oh, that's right. He didn't work on the Lisa.

**Atari:** He didn't work on any architectural stuff, right? He never. No. I'm not trying to be smart. He just didn't. No, no. It wasn't his skill set. But Steve was an innovator, right? And he was absolutely dedicated to make the Lisa successful. And he went up to Jeff Raskin, who deserves a lot more credit than he got, because he wrote the book that made Apple popular, you know, the user manual. Yes, yes. Everybody loved the Apple user manual. And Jeff wrote that, right? But he took Steve up to meet Park, right? Mm-hmm. And he showed them the operating system that was effectively a shorter version of Star. It became more Star and became better. And Steve came back, and he and I had lunch at Good Earth. And he said, those guys are not going to make this happen. And I'm convinced, and I want to build my next machine around it. Right. And he did, right? Yeah, of course. But he knew he was stealing it from Xerox, right? No question, right?

**Dave Jones:** Oh, well, but that's what you did. I mean, it's just an idea. A good idea is a good idea.

**Atari:** Xerox didn't complain, right, at all, right? Right. Okay. But, you know, the funny story is, is that when Gates finally, after pressure for months and years from me, put Windows into the machine and brought it out, Apple either sued him or threatened to sue him, right? And somebody had to bring it to their attention that if they won anything, the guys who were going to get the reward was Xerox, not Apple, right?

**Dave Jones:** Xerox.

**Atari:** Because Jobs had stolen the thing from Apple and blatantly stole it, right? I mean, but it would give Steve credit. The fact that he, and by the way, Raskin is the one, Steve put it into the Lisa, Raskin forced it into the Macintosh. And then Steve, when the Lisa failed, took the Macintosh away from Raskin and cut their credit. Exactly. Right.

**Dave Jones:** Yeah. Right.

**Atari:** But, but in fact, the point is that that changed the industry in a way it should have been changed, right? It was a superior, superior system. And Gates and I had this fight and internally because IBM didn't want to do Windows. IBM wanted to do something else.

**Dave Jones:** Okay.

**Atari:** And they were pushing Gates.

**Dave Jones:** I mean, you know, they were doing, they were doing, what was the IBM OS back then?

**Atari:** I don't know, whatever it was. But the point was is that they were pressing Gates to do that. And, and the rest of us were screaming at him to do Windows. And he finally did Windows. And of course that made his company totally explode because it was the right solution. Right. Yeah. It was absolutely the right solution. And they did a pretty good job with Windows for a while. And then they screwed it up. They, well, you know, they, they got confused about what Windows is and why you use it and how you use it. And they quit listening to users fundamentally. Right. Yeah. They, they decided that tablets were doing well. So we're going to make it, we're going to make it all a tablet machine. Well, ask the five, 1.6 billion people. And what if they want a machine that acts like a tablet? Right. I think we have three votes here for no.

**Dave Jones:** So we should keep moving.

**Atari:** Yeah. No, no. But I'm just saying, you know, it was, I actually had given them that advice. I was talking to them about trying to focus on doing this next generation product. And, and I wrote that advice to them, but they didn't pay attention to me and nor to anybody else. Right. And, but the point was, is that that was stolen from Xerox. Jobs made it happen. And Microsoft just took forever to make their version happen. And now you wouldn't even think about not having it. Right. I mean, it would be totally against it. I don't know if you ever wrote any MS-DOS instructions, but they had them. Oh, yeah. The most ugly shit in the world.

**Dave Jones:** Oh, I did that back in the day. Yeah.

**Atari:** No, no. It was funny. I'm selling the product. Right. Yeah. And I had lots of programmers and everything else. I said, I'm not going to, it's, I had done this really nice screen editor for the, for the pet. And I said, that is just so ugly. I'm not going to have anything to do it. I'll wait till Windows comes out. Right. And then I kept pushing gates for Windows. Right. Because I didn't want anything. It's so ugly. Right. I mean, it was, it worked and we built a whole industry around it, but that's because we had a lot of dedicated programmers that were willing to do that crap. Right.

**Dave Jones:** I mean, anyhow, I'm sorry. Deal with what's given to them.

**Dave Jones:** So do you know any of the history between Mike, uh, Apple and, um, jobs and, uh, gates in terms of windows?

**Atari:** Only, no, no. Gates, windows, gates didn't, jobs didn't have much to do. I think when windows came out.

**Dave Jones:** No, I mean, he, he was livid that gates had done this window, had gone behind his back and did windows. I don't see why he would be. He was saying that he, no, it's not going to be a desktop OS or something.

**Atari:** And I don't think that, honestly, I'm not sure that it really happened because wasn't, wasn't jobs gone during that time? I think jobs wasn't even at Apple during that time.

**Dave Jones:** I think it was just before he left.

**Atari:** Maybe. I think. Yeah. I mean, it could be, it could be that jobs, jobs before he left was, he had gotten totally full of himself. Right. Right. I think the reason he came back and did such a good job is he got his teeth kicked and at his own company. Right. And, uh, and I think that helped him a lot. Right. But when he came, by the way, just one last comment about flying jobs, didn't come back saying, I'm going to make the world better. He came back and said, flash is going to change the world. I'm going to be the leader. And he did. Right. iPod. I mean, is it iPod? Yeah. iPod.

**Dave Jones:** Yep.

**Atari:** Yeah. The phone, the, couldn't have done the original phone without flash. Right. Yeah. He definitely couldn't do the, the, the iPad. And they basically built the, the, uh, laptops around it. Right. I mean, and he was the leader in each one of those phases. Right. I mean, people were doing other stuff. Right. And you told me that you said the iPod actually was, had a floppy, had a hard drive at its beginning. I didn't realize that. Yeah. The thick ones.

**Dave Jones:** Yeah. The, originally that, that, that, that, that was the breakthrough. Yeah.

**Atari:** I mean, but, but my point was, is Steve recognized that that was a technology that he was going to ride and he wrote it well. Right. Right. And he built the things around it that people wanted to buy. And he does such a great job or did such a great job on aesthetics. Right.

**Dave Jones:** Absolutely. That was, uh, Jonathan Ive. Wasn't it? Yeah.

**Atari:** But let me tell you something else. You know, the, I bought, I was kind of against doing Apple over since I beat them too many times and I just want to, I'm about to, I'm about to buy a smartphone. Right. When smartphones first come out. And so I bought my grandson and my girlfriend, uh, iPhones. Right. And I bought the Samson equivalent. Supposedly Samson equivalent. And I used it for about a week and then I just gave it to my grandson. The screen work that jobs forced them to do before they brought the iPod.

**Dave Jones:** The Gorilla Glass and all the scratch stuff. Right.

**Atari:** Well, but the point was, is the screen really worked with your fingers and it did all the things you wanted it to do. And, and, and the others didn't. Right. He had patents all over that stuff. And that was his contribution. Don't bring me shit. Right. That was basically his view. If it, if you don't, if it doesn't work good, go fix it until you show it to me. Right. Because he would just, he would take them apart if they did. Right. And, you know, I don't know if there's a management style that everybody should go, but he turned out some really nice products. The charms of talk. That's right. Oh, that's my, that's my phone.

**Dave Jones:** I'm wondering now, is that on an iPhone or what? It's on an iPhone. No, no, no.

**Atari:** I wouldn't even think of, I wouldn't even think of, no, seriously. They, they have patents on the screen. Their screen's still better than everybody else. Yeah. Some of the other people have done better, but nah. Yeah. Yeah. No, no, no. No, we have like 10 iPhones in my group. Right. And, you know, that's good. Right. They all work.

**Dave Jones:** Never owned an Apple product.

**Atari:** Is that right?

**Dave Jones:** Yep. Never. That's good.

**Atari:** My girlfriend, my girlfriend is a industrial, I mean, a landscape designer. Yeah. And I used to give her free computers and she insists that she's got only Apple products. She's got the latest Apple Mac. She's got the. Right. She's got the iPad and she's, she would not be, she and her friends would not be anything other than Apple customers.

**Dave Jones:** Oh, yeah.

**Dave Jones:** See, I don't like the closed system. You know, I don't. I think the problem is. That just rubs me the wrong way. You're not.

**Atari:** Your problem is you, you know too much. These people are. Yeah. Yeah. I know. Exactly. These people are people that are impressed by the look. The sheep. They're impressed with the, with the, with what they can do with it. You know. Yeah. I mean, they, they brag about how good their photographs are. How good they're. Oh, no, they're absolutely. The definition of trapping a customer base. They have a trap. Oh, totally.

**Dave Jones:** Yeah.

**Atari:** Right. I mean, they won't go anywhere. Right. I mean. That's right. And, you know, I want to make the new PC superior to anything Apple's doing. So we stopped the migration. Yeah. Yeah. Anyhow. I'm sorry. I'm glad I remembered this story about the windows. No, that's. It's all good. Thank you very much. Oh, listen. It was fun, guys. Yeah. It's been amazing. It's been awesome. They, I hope. What happens to this now? Just two people.

**Dave Jones:** It goes live tomorrow. Yeah.

**Atari:** It goes live as a podcast.

**Dave Jones:** A podcast. A second people can download it as an MP3 onto their iPod, their iPhone, their i-whatever. Or any other thing. Any smartphone. Any other thing.

**Atari:** Yep. Do you have, do you make any money off your audience or is this a. . .

**Dave Jones:** No, this is a, yeah. We haven't figured out how to make money off this show. We've been doing it for five years. Yeah. And, yep.

**Atari:** Labor of love.

**Atari:** You guys are a lot of. . . No, no. You're a lot of fun to talk to. So I. . . Thanks. I'm happy to do it. Thank you very much. Appreciate it. It's been. . . . No, no. You're very gentle to talk to. Gentle.

**Dave Jones:** People don't use that word in my presence generally. Well, no. Have you. . . Well, I'm not the gentle one. Chris is the gentle one. And I'm the. . .

**Atari:** Have either one of you. . . Have either one of you think. . . I mean, Dave, if there's something you want to beat me up on, go ahead and do it. Yeah, Dave. Go ahead.

**Dave Jones:** Right. No, no. Nothing at all. You're a legend. I'm not going to beat you up for anything.

**Atari:** No, no. Listen. The way I learn. It's like having this guy Glenn, right? We get into an absolute war. Right. Because he's got an idea from today. And I've got this other idea. And we come up with something beautiful when we're done. Right. I mean, that's the way you get things done. Oh, I totally do. You don't. . . You have to. . . You have to. . . All good ideas are polished by conflict.

**Dave Jones:** Exactly. I like that. I like that. And that's what I make my living from. I do a video blog where all I do is speak the truth and people love it. Yeah. Your version of the truth.

**Dave Jones:** Come on, Dave.

**Dave Jones:** Well, what my version of the truth. Well, I'm not afraid to say what I think. That's right. Yes. So that's. . . No, listen.

**Atari:** That's good. That's the reason for my success. I just watched Citizen Four last night, right? Oh, I haven't seen that yet. Don't watch it. It's really. . . Snowden deserves a fucking medal at Oslo. Totally. Not people here trying to convict him of something. I know. Yep. And the reporter that did that stuff, it's a great story. They won the Academy Award and they should have. It was. . . It's really well done. Right. And I strongly recommend it. But anyhow, my point was is that here was a guy who said, I have to tell people the truth, not what. . . And he did, right? And they went out and did it. That's. . . And back to, you know, it's changed our way we live because he told the truth. Absolutely. And I thought it was funny about Merkel. And I swear there's a story I heard that they went out and arrested the listening group and the Germans went in and took over their listening group and arrested them right after they found out about that and then, of course, let them go. Yep. Yep. I think it happened, right?

**Dave Jones:** Oh, I'm sure it did, yeah.

**Atari:** And I would have if I'd been a German head, right? You know what I mean? Right. No, no, no. You know, I mean, these are sovereign countries, right? I mean. . . Yeah, totally.

**Dave Jones:** I know.

**Atari:** Yeah. And, you know, but my point was is that he was not out there to be liked, right? He was not out there to be anything other than to tell the truth. And he was really proud. I'm glad he did it. And I'm saying the same to you. Just keep telling the truth. That's what I do. The world is a better place for it, right? I hope so. That's my intent. No, no. Seriously. I totally believe in it, right? And, you know, I may not always agree with you, but that's too bad for me.

**Dave Jones:** I don't expect people to agree with me when I speak my mind, you know? I just expect them to, yeah.

**Atari:** Are we off being broadcast? Not yet. No, no. We're still going. We can definitely say goodbye for now. We'll call it Quincy. No, no.

**Dave Jones:** Then we'll get the juicy stuff off the air. So that's the important.

**Atari:** No, no. Why don't you say goodbye? And I got one little story I want to tell you about China. Yes, we get the good stories, folks.

**Dave Jones:** Sorry, folks. So thank you. So officially, thank you very much.

**Speaker ?:** Yes, Chuck.

**Dave Jones:** Thank you so much.

**Dave Jones:** And thanks to Bill for introducing us as well. That was very nice of him. Yeah. And we really appreciate you coming on the show. It's awesome.

**Atari:** No, no. It was good. Thanks, mate. Okay. See ya.

**Speaker ?:** See ya.

**Atari:** Come back on Don't Hang Up. We won. Okay. All right. We're good now. We're good now. Okay.

**Speaker ?:** We're good now.
