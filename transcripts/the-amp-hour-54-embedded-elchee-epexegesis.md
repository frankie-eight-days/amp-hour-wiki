---
episode: 54
title: An Interview with Jack Ganssle - Embedded Elchee Epexegesis
url: https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/
---

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog. And I'm Chris Gammell from Chris Gammell's Analog Life.

**Jack Gansel:** And I'm Jack Gansel with myself. All right.

**Dave Jones:** Hey, Jack. Jack Gansel's in the house, everyone.

**Jack Gansel:** Welcome, Jack. Well, thank you. I appreciate it. I really am looking forward to this. I've been following the Amp Hour for quite a while. Oh, awesome.

**Chris Gammell:** That's right. You were like one of our first benefactors in the media. You wrote about us early. I believe you called me a young whippersnapper or something like that.

**Jack Gansel:** A young whippersnapper, yes. I think so. I did, you know. And since I'm a certified old fart, sometimes the audio and video stuff I stay more away from. I tend to go more towards the written word because I find I can consume something written much faster than I can by watching a video or whatever. But, hey, this sounds like fun.

**Dave Jones:** Yep.

**Jack Gansel:** Well, there goes Dave's model.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** My business model is right out the window.

**Dave Jones:** All this talk about old fart and young whippersnapper, geez, it sounds like you're Australian.

**Chris Gammell:** I don't think those are Australian sayings, Dave, I've got to say.

**Dave Jones:** All right. Okay. Interesting. Hang on. I think I've got this stupid because we're using Skype. Oh, no. We're using Skype. And my audio meter is peaking here. Sorry about that. But I may have clipped.

**Chris Gammell:** I'm sure you sound fine. Yeah, you sound fine to us.

**Dave Jones:** All right. We're doing well.

**Chris Gammell:** We're having audio problems. We're back to our normal level of Chris mess-upper-y here.

**Dave Jones:** Yeah, normal level of incompetence, yeah. Yeah. Jack has been very kind.

**Chris Gammell:** I'm still warming up the vacuum tubes here, guys. That nice, that warm, crunchy sound that all those audiophiles love. Yeah, right, right. Right.

**Dave Jones:** With their $10,000 speaker cables. Yeah, exactly. For a digital signal.

**Chris Gammell:** That's right. Yeah. Gold plated. It's important. Right.

**Dave Jones:** So, Jack, tell us about your background.

**Jack Gansel:** Yeah. Oh, well, I mean, I've been in the embedded field forever. Go ahead. Forever, huh? Well, just about. I guess, gee, you know, the 4004, the first micro, came out in 1971. And the 8008 was the first 8-bitder, which came out a year later. And roughly at that time is when I got into embedded systems. So it's been a long time. That's pretty early, yep. Yeah, it's really a great field. And I was very fortunate in that I was able to get a job as an electronics tech when I was 16. And it turns out that the company where I was working decided to get into microprocessors with the 8008. But it turns out no one knew anything about digital design or software. Wow. So I got sort of bumped into engineering while I was in college, which was not good for my college career, but was great for everything else. Right.

**Chris Gammell:** Yeah. Well, you know, that seems to be a common theme. You know, we read about, like, Jim Williams, who sadly just passed away. Very sad. And, you know, he never finished MIT. Our friend Jerry, you know Jerry. Yep. She never finished high school, I think. And she's rocking the electronics world. I mean, there's tons of stories like that. And it's just because it's hands-on and you get to know it, you know? Like, I don't know if you finished a degree or not, but it doesn't really seem to matter.

**Jack Gansel:** Well, actually, I went through four years of double E. And when I was three courses short of finishing, I stopped. I was so busy working and having so much time building these systems, so much fun building these systems that I just couldn't get around to finishing school. And, you know, I have a lot of regrets. It was really a dumb move. But I think partly it's been good for my career because I've stayed away from having real jobs because I figured no one would hire me. Oh, yeah.

**Chris Gammell:** Well, how do you define real jobs then? That's interesting.

**Jack Gansel:** Well, I did have a real job at that company where I was working as an engineer building these systems. But in, I think it was 1980, I quit there and started a consulting outfit with a friend. And we did that for a while. Then I started a company that we manufactured in-circuit emulators, designed and built them and did that for like 15 years. And then, oh, around the mid-90s, sold that company. I tried retiring for a day. I was bored to tears. So I started doing what I'm doing now. Yeah.

**Chris Gammell:** Wow. That's awesome.

**Jack Gansel:** Yeah. It's a lot. You know, this is a fantastic field. It's so big that you can do pretty much anything you want to.

**Dave Jones:** Yeah. I have to agree. It gives you a clean slate every time you start, really. You can do, as you said, pretty much anything. It really is quite amazing. It's amazing how it's actually progressed from those days of like the 8008. Sorry, was it? Yeah. The 8008 you started with?

**Jack Gansel:** Yeah, sure was.

**Dave Jones:** Wow.

**Jack Gansel:** It's a miserable little chip. I mean, it was.

**Dave Jones:** Yeah, I know. I was going to say, they were so massively limiting back then. But, well, that's compared to today, right? With hindsight. But I guess back then, they were the world's most amazing devices, right?

**Jack Gansel:** You know, embedded systems is such a big field. And if you listen to the press, and, of course, I write for magazines, so it's sort of hypocritical. You are the press. But if you read the magazines, if you're not doing 32 bits at 500 megahertz, you're some sort of dinosaur. And the truth is, you know, Microchip sells a billion of those brain-dead little picks, which are wonderful parts. They're really, truly wonderful parts. But they're really pretty minimal parts. And they sell a billion a year. I mean, I see so many applications, which are just literally hundreds of words of memory is the entire app.

**Dave Jones:** Oh, absolutely. I've written them myself. Yeah. And everyone always says that. It's the death of the 8-bit micro. They've been saying it for 20 years. And it's just rubbish. It's horses for horses. You know? No. It's not going to happen.

**Jack Gansel:** I mean, I've been hearing it forever. And, you know, it's kind of interesting. You can get a high-integration ARM part, like from ST, for 65 cents. Oh, yeah. So there you've got a whole computer for 65 cents. You'd think 8-bits would be dead. Well, I think the converse is true. I think what that means is that 8-bits will become even cheaper. And so whole new kinds of applications you never would have dreamed of will surface. You know? They'll be like smart dust. You know? You just... You'll be Johnny Appleseed out there casting sensors into the wind. And there'll be self-assembling mesh networks coming together. I mean, I think it is... Whether you're doing 8-bits or 32, it's just exciting stuff. And in a way...

**Dave Jones:** It doesn't matter. Yeah.

**Jack Gansel:** The low end is, in some cases, even cooler than the high end. The high end can be so big and complicated. You've got these gigantic teams doing all this work and stuff. And you kind of get lost in the crowd. Whereas, on the smaller end, you can be the hardware designer and the software guy and technical support and a whole nine yards, you know? Exactly.

**Chris Gammell:** You don't have a choice about the technical support, right? You don't have a choice. Yeah.

**Dave Jones:** And with those 32-bit micros, therein lies a trap for young players, right? You might be able to buy it for your 60 cents or whatever. But then, often, they will need... Oops. You need a 1.2-volt core voltage or something. Bingo. You've got to add an extra regulator for that. You know, you can't just run it from your 3.3 supply or straight from your battery or something like that. So, it increases your system cost and other complexity issues come into it. And, you know, it's not just all about the price per part. No. But, as always, you pay per square area of silicon. Ultimately, that's what it comes down to. And 8-bit will always be a smaller... For, you know, all things the same, 8-bit will always be cheaper than 32-bit.

**Jack Gansel:** And it's even bigger than that, I think, Dave, because there's things like, you know... I mean, you really put your finger on it. Like, with power management, if I see a lot of 8-bit applications where the processor requires so little power, the problem isn't that it's going to suck the battery dry. The problem is that the battery itself discharges after 20 years. Yeah, that's right. You know, and for a lot of applications, that's huge. I mean, it's huge. I know.

**Dave Jones:** It's massive.

**Jack Gansel:** Yeah. Or energy harvesting. I mean, there's a lot of ways of getting free power where we'll never get more than microamps or even nanoamps. Yeah, nanoamps.

**Dave Jones:** Yeah, microamps is huge in the energy harvesting business. Yeah.

**Jack Gansel:** But that really opens up a lot of opportunities. And, you know, I think the 32-bit world is way cool. But 8 and 16, man, there's some cool stuff going on. I think it's going to continue to be really a great area.

**Dave Jones:** So there you go. You heard it from the expert himself. The death of the 8-bit micro is greatly exaggerated.

**Jack Gansel:** Greatly. I had a conversation 15 years ago over dinner with a well-known industry analyst, shall we say.

**Chris Gammell:** Shall we remain nameless here? Remain nameless.

**Jack Gansel:** Remain nameless. And he told me that what drives the computer field, and this is an embedded guy, but what has always driven the computer field is pornography. Remain nameless. Remain nameless. And that what the porn vendors want is the highest-end processor that they can possibly get to push their content. And sure, okay, that might be true. And so he went from there to say clearly that the low-end processors are going to go away. Well, I mean, I could be wrong, but I don't think any 8-bitters have ever been delivering porn content.

**Chris Gammell:** Maybe back in the days when they were really hard up for material. You're right. Exactly.

**Jack Gansel:** That's funny. There's all different kinds of markets in this business, and a lot of folks tend to just focus on limited ones like datacom and infotainment and stuff like that. Because that's where all the – to go back to make an analogy, that's where the sex appeal is. Right.

**Dave Jones:** Well, the interesting field of the new mobile phones and the apps and things like that, a lot of stuff, you know, everyone talked about, oh, everything's going onto the cloud, everything's going onto the internet. But with phones, everything seems to be going back to apps and doing it locally because we don't have the bandwidth yet. There's lots of talk about that and, you know, and how a lot of people don't want to access the internet because the apps, you know, all they want to do is run these apps and things like that. It's a mobile computer instead of – and there's all sorts of, you know, people, you know, booms and bust things happening in various aspects of the embedded community. One thing I wanted to get your opinion on, Jack, was this – the soft market, the soft processor industry. Now, like five, maybe ten years ago, right, that was all the rage. Everyone said the soft processor market is the future, right? All hard micros will die, right, because everyone will be using FPGAs. And what happened there? Well, we've now switched back where all the FPGAs are starting to get hard processors in them because the concept just didn't really work except in the more niche applications.

**Jack Gansel:** Well, it's very interesting. You know, I think that the soft processor thing and, like you say, they're moving towards a hard like Xilinx now is that new core with the hard part on it.

**Dave Jones:** The ARM cores in them, yeah. Yep.

**Jack Gansel:** You know, I think that it's a fantastic way to build some classes of systems, but FPGAs will always cost a lot of money. It's just the nature of the component.

**Dave Jones:** It's that square area, right? That square area of silicon trap.

**Jack Gansel:** Well, what you're doing is you're making a tradeoff. Everything in engineering is a tradeoff. And with an FPGA, the tradeoff you're making is reconfigurability versus dollars. And for a lot of apps, man, that is a way to go. But you're not going to get down to a 20-cent processor doing that.

**Dave Jones:** No. Well, you can get a $1 FPGA these days, but they're not very big. You've got a processor in there, though.

**Jack Gansel:** And the other processor problem is you drop a processor in it and you start to suck away at most of the resources of the FPGA. And then you don't have anything left to do what you want to do.

**Dave Jones:** And it's not very power efficient either, right?

**Jack Gansel:** No, man. Those things are hot. They run hot. Yeah. I mean, I see FPGAs are high-end stuff. I mean, you've got to basically feed liquid nitrogen into them. I mean, some of them will cost $15,000, $20,000 per chip. Yep. I mean, it's like high-end military apps.

**Dave Jones:** I've used ones that cost a couple of grand. And, well, you're soldering those suckers into your prototype and you're, you know, shit, I better not screw this up.

**Jack Gansel:** Oh, yeah. But, I mean, it does bring a lot of interesting stuff to it. And when I first started doing FPGA design, I thought that this was all going to be the future. But then you start to look at where things, you know, the tradeoffs. Yeah, exactly. And it just, you know, it's perfect for some things and not perfect for others. But it does sort of illustrate, I think, another trend that we're seeing in the FPGA world is that hardware design is moving towards software. Now that everyone's using VHDL and Verilog and System C and all that stuff, the hardware folks are more like software people today, except, you know, they've inherited all the evil of software, but they haven't learned, you know, stuff like configuration management and all the stuff that the software community has learned so painfully over the last 50 years.

**Chris Gammell:** So it's starting to bite them in the rear kind of thing?

**Jack Gansel:** Yeah. It is. But I do think we'll see more of it. You know, we're going to see a lot more of this merging of the two. Because, I mean, there are a lot of obvious reasons. And then there's the cool things. Like, I don't know if you've seen some of the Altera tools. You can, you know, you write your C code for the NIOS processor, and they can highlight some of the code and say, design that into hardware.

**Dave Jones:** See, the hardware compilers are pretty cool. Yeah.

**Chris Gammell:** Well, there's two versions of that, too. Isn't there one that also does it as an instruction if you're using the NIOS as a processor? Right. And so it does an instruction as opposed to just block of logic, right?

**Jack Gansel:** Right. It's a very interesting sort of change in the way that the hardware and software has traditionally been a different size of the fence. And those two things are truly merging in many ways. I think we're going to see a whole lot more of it. You know, if we beat up on FPGAs because they're big and stuff, but the truth is transistors are pretty close to free. And so FPGAs will follow the usual trend. It's just they will always lag, you know, by their nature.

**Dave Jones:** Well, I've got an item. I was actually just yesterday. I was laying out one of the smallest FPGAs you can get. It's a 36-pin chip scale package. It's an Actel Igloo Nano part. I'm not sure how many gates I forget. But the package itself is the same size as the footprint of the two 0603 bypass capacitors that the chip needs. Oh, my God. Oh, my God. Oh, my God. It's like something's seriously wrong with the world when your bypass capacitors are bigger than your chip.

**Jack Gansel:** You know, who would have thought? You know, and a capacitor has got some physical limitations. There's a limit to what you can do to make it smaller. You know, I have a super capture cool.

**Dave Jones:** I could have used, you know, 0201. It didn't warrant that, right? This was a prototype thing.

**Jack Gansel:** So, damn it.

**Dave Jones:** If I'm forced to use this bastard of a package, then at least I'm going to put in some capacitors I can solder, right? Yeah.

**Jack Gansel:** You know, it goes back to our earlier discussion. You get to a little tiny nanoamp circuit. You don't need that bypass cap.

**Dave Jones:** Yeah, well, exactly. Save some money. So, I could actually leave it off. And that's what this thing is. This thing's working on, you know, the smell of the proverbial oil, oily rag, you know. So, I probably, ultimately, don't need that bypass cap. But it is working at about 2 megahertz, though. So, you know, that's getting up there. It's not like it's, yeah. I don't know. Anyway, I did put two bypass caps on just as a good measure.

**Jack Gansel:** Well, 2 megahertz, you're really pushing the edge there, Dave.

**Dave Jones:** Yeah, I know. It's bleeding edge stuff. Oh, boy. And here's another annoying thing, right? The Actel Igloos. Here's rant time. Rant of the week. Okay. Do we have any music for that, Chris?

**Chris Gammell:** Dave, we haven't had music for a while. Right. Okay. Sorry, buddy. No, fail.

**Dave Jones:** Anyway, do we even have a segment called Rant of the Week? I think we used to, didn't we?

**Chris Gammell:** No, we don't.

**Dave Jones:** Oh, there we go. Okay. New segment. We're in the professional radio show that we are.

**Chris Gammell:** Just so you know, Dave makes up segments as he goes along.

**Jack Gansel:** Yeah. See, this is sort of like agile development. Yeah.

**Dave Jones:** Oh, wake word of the week, agile development. Oh, boy. Anyway, these Actel Igloo parts, right? They famously claim, one of their big key performance things is that the core voltage can work down to 1.2 volts. Fantastic. So you're designing your 1.2 volt core power supply and you use it at that. And then if you didn't read the fine print, the little asterisk that says, oh, by the way, the core actually needs 1.5 volts for programming. Otherwise, you can't program the damn thing. Right? You've got to be kidding me.

**Jack Gansel:** Oh, that's really good design.

**Dave Jones:** So what they do on the in-circuit programmer, they actually have a special output pin, which is designed to drive a MOSFET, which you are supposed to build into your design so that you can switch the core voltage just for programming. It's like, what a waste.

**Jack Gansel:** Give me a break.

**Dave Jones:** Come on. I know. That is – I reckon somebody screwed up there. I reckon marketing got hold of that because I think these things used to work at 1.5 volts, right? And then they realized, oh, you know, they tweaked the process, manufacturing process. Oh, I think we can now use it at 1.2 volts. Great. Let's market that. And then they –

**Jack Gansel:** I don't know, Dave. I'm not going to give them too much help because, you know, 1.2 volts, the difference between a one and a zero is starting to become, you know, pretty close to noise levels.

**Dave Jones:** It is. It is down in the noise. I've got to admit, it's very impressive. But really, that's just annoying. You know, that is bloody annoying. I've got to tell you. Anyway, I was a bit miffed. I can tell. End rant.

**Chris Gammell:** If Dave knows one thing, it's when he's miffed. You have to be in touch with you.

**Dave Jones:** And I know, please don't write in. It's not Actel. It's bloody, what, Micro Semi now that every company's mine, every other company. And give me a break.

**Jack Gansel:** Yeah. Yeah.

**Chris Gammell:** Jack, how about that? I mean, what's your take on the industry in general? There's a lot of mergers happening, it seems like. And what's your take on that and a lot of the acquisitions?

**Jack Gansel:** Well, you know, we're kind of now victims of our own success. I mean, the cost to build a fab has gotten so high that, you know, there aren't very many people who can afford to do it anymore. So you have a couple of things happening. You know, we see the industry mergers, of course. And we see the growth of, you know, these fab companies, you know, like TSMC and all of that. And I think we're going to see much more of it because, you know, the cost of building a part is getting higher. But there's a part of me that sometimes wonders if we really need, for many applications, all this high-end stuff. I mean, I sometimes wonder if some little company in the Ukraine is going to take one of these old 500 nanometer fabs and realize they could build some way cool parts because the fab is entirely depreciated. And the process variance issues aren't significant. So, you know, I think you can do a really sloppy job and knock out some major cool chips doing that.

**Chris Gammell:** Okay, so I guess you have to weigh in on our continuing debate here at the Amp Hour. Well, first, Chris.

**Dave Jones:** Oh, no, you're not going to raise. Oh, yeah. Oh, that's what I was going to do.

**Chris Gammell:** Oh, come on. Jack, do you know what I'm talking about here? No, I don't. Okay, so the way you're going right now is that if, if I'm right, and I think it was 20 years, Dave, is that right?

**Dave Jones:** Well, no. Well, you added that stipulation later. But basically, back in the first episode, Jack, I think it was one of our first episodes, Chris claimed that you would get a chip-making machine that you could have at home that would just magically spit out chips just like the MakerBots, you know, those 3D printers print out things, right? He reckons that you would have this chip-making machine, and it would be a revolution, quote marks. And, you know, everyone would be making their own chips at home. And I instantly, straight off the cuff, called bullshit. And Chris has been trying to back out of it ever since. I have not been trying to back out of it. Right now, we have...

**Jack Gansel:** No, no, no, no, no, guys. They already did it. It's called an FPGA.

**Dave Jones:** Yeah, exactly. That was my argument. One of my arguments. One of my very well-thought-out arguments.

**Chris Gammell:** Oh, yeah, very well-thought-out.

**Dave Jones:** Oh, come on. How do you test the thing? How do you package the thing? How do you compete against DigiKey with 100,000 parts?

**Jack Gansel:** I don't think there's the issues. I don't think there's any demand for anything like that. I don't think that it brings any advantages to anyone, even if you're just, you know, doing it for a hobbyist standpoint. It's so much easier to either use an FPGA or wire something up yourself or whatever. To get involved in building a chip, I just don't see, brings a lot to the table.

**Dave Jones:** Thank you very much, Jack. Sorry, Chris.

**Chris Gammell:** I just have to say, what does Jack Gansel know about the electronics industry? I'm just going to say it right here. Right. Well, I'll tell you something, Chris. This is my litmus test.

**Dave Jones:** See, Jack just did that straight off the bat. He had no clue what that is, and it just hit him, and instantly he knew that it was bullshit. See?

**Jack Gansel:** I agree with you.

**Dave Jones:** Just like me.

**Jack Gansel:** Yep. Sorry, Chris, but I'm sure you can win on another issue.

**Dave Jones:** Sorry, Chris, you've been thinking about it too hard. Yep.

**Chris Gammell:** Well, I guess I have more people to prove wrong then. Oh, well.

**Dave Jones:** Excellent. And the debate continues.

**Jack Gansel:** You're getting married in the fall, right? That's right. So then you can enter a whole new debate. Now, I have to admit, there are some significant upsides. My lovely wife just brought me a martini. So how bad can things be? Whoa, there you go. Drinking and radioing, that's good.

**Chris Gammell:** That's awesome.

**Dave Jones:** The next 40 minutes could be a good one, folks. That's right. Stay tuned.

**Jack Gansel:** I hope we're not recording.

**Dave Jones:** How do you detune a podcast?

**Jack Gansel:** Detune?

**Dave Jones:** You can't. You can't. You know, everyone, like, stay tuned. Stay tuned, you know, it's not like you can just tweak, you know, I guess you can hit the stop button, right? But you can't just tweak the dial and tune to another podcast.

**Jack Gansel:** I assume you're going to edit all this out, right, Chris?

**Chris Gammell:** We'll see, Jack. We'll see. So speaking of martinis and relaxation, you and I were talking before the show about your priorities, and I was really impressed by that. And so you said that, you know, you make a priority to, you know, get out of the office a little bit of the year. Can you tell us about your philosophy there?

**Jack Gansel:** Well, I feel very strongly about this. I think that especially Americans work way too hard, and I'm guilty of that myself, even today. But I was really struck by a Lee Iacocca quote. He said, no one on their deathbed ever says, geez, I wish I had one more hour to work. And I really believe that. I said, when I started doing what I'm doing now, I set a goal for myself to take four months vacation a year. Four months? Wow. Yeah. And I haven't been able to live up to it recently. But because my family is important to me, you know, especially when my kids were little, I wanted to be able to spend a lot of time with them. And my hobbies are important to me. And life is important to me. And as much as electronics is great, you have to have, you know, have to be more well-rounded. And there's so much to enjoy in life that I basically set a goal for myself that vacation is crucial. And four months has not worked out real well, but we probably average between two to three months a year. And yeah, you got to keep a smile on your face. A very wise guy told me, he said, there's two things you need. You have to make money and you have to have fun. And either one by itself is not enough. Yep. I couldn't agree more.

**Dave Jones:** I've always had, I've never worked on my birthday. I have this one, you know, doesn't matter what was on. I would, I've never worked on my birthday in my entire life. I always take the day off. Yep. It's one of my things. And now I work from home. Well, it's so much better.

**Jack Gansel:** No one knows what you're doing. Right. Right. Working from home is the best. So do I. It's fantastic. We get up in the morning, shuffle across the hall, you know, and here my wife works with me. She takes care of all my travel and all that kind of stuff. It's a very, very civilized. And to go back to philosophy, I guess what I'm saying is I sat down and decided to design everything around my life rather than design everything around work. Sort of re-engineer the whole trade-off. Yeah. And, you know, I took some experimenting and playing and stuff. But I'm pretty pleased with the trade-off.

**Chris Gammell:** Yeah. That's good. So for the balance perspective, I'm guessing you had a little bit less of that because you just got back from India. So you probably had to work a little bit more while you were over there. Can you tell us about that?

**Jack Gansel:** Well, you know, I was over at the Embedded Systems Conference in India. And I guess this is sort of a two-part thing. You know, the Embedded Systems Conference in India is phenomenal. It's just fantastic. There were about, I think they told me, 400 attendees. So it's very small compared to the ESCs in the U.S. But, you know, I've been to a number of the ESCs in India, and it always blows me away. I am seeing the future. When I see these engineers who are all very young, all very eager, they've got these glint in their eyes. They're so engaged with this feeling. Awesome. Yeah. That's great. And I don't see that as much in many of the other places I go. I just, you know, there are a lot of problems in India. There's, you know, education issues still there and everything else. But I see a new generation that is desperate to make this work. And I talk to a lot of engineers here in the U.S. who will say, yeah, but those Indians, you know, they're not as creative or they're not this or not that. Well, maybe. But, you know, these are smart people. Well, some of them are going to be. They're going to figure it out. They're going to figure it out. Ten years, five years, two years. They have so much to gain. Whereas, and not to knock, you know, every time I travel overseas a lot. And I've been doing this almost for 40 years. And every time I come back to the United States, I'm happy to come back. It's a great place. But sometimes we're a little fat, dumb, and happy over here. And for many people, the expectations are that at a minimum, you will own a house, two cars, yadda, yadda, yadda. Whereas a place like India, and it's not the only place I see this, the fact that you can actually move out of your parents' house and all that is something to aspire to. And it's incredible.

**Chris Gammell:** So it seems like my generation is trying to do the opposite. Trying to move back home. Stay at home as long as humanly possible. And maybe it's just shifting back towards that way, you know, where if economics and hard to find jobs for recent grads in the U.S., then, you know, maybe it'll go that way. And then those kids will be hungry and the cycle begins anew.

**Jack Gansel:** There's no such thing as balance. There's no stasis. Things are always shifting to accommodate changes in the environment. You know, it's like natural selection. Nothing stays still. And that's certainly true here. I sometimes worry that we have been through a sort of a Camelot, like a golden age, since sort of the end of World War II, where everything was just wonderful for folks here. And things are getting harder now.

**Chris Gammell:** Well, there were some downturns, I've heard. Yeah, there were.

**Dave Jones:** But generally, though, the quality of life, you know, has skyrocketed. Yeah. Freedom and all that sort of stuff.

**Jack Gansel:** Yeah. I mean, people of the middle class haven't been starving.

**Dave Jones:** Wealth and all that sort of stuff. Yeah.

**Jack Gansel:** I mean, it's been wonderful. It's been, you know, the U.S. has done incredible things as a result of all this. But I worry for the sake of, say, my kids and others, you know, what things will be like. So then the other side of India, because you're asking about India, is India itself. Have you guys ever been there? No. I have not. No. Fascinating place. What cities are we talking about here? Well, Bangalore is one of the big centers of electronics. Okay. Right. It's just, the more I go to India, the less I understand it. The culture is so different. Yeah. And the, you know, religion is woven into the culture in ways that much as I try to understand, I don't. The poverty is grinding. Just grinding. But then you see tons of billboards with signs like, learn English, you know, or improve your English, because these people want jobs in call centers. Or I was really struck by a couple of signs I saw this last trip. Need to gain weight? We can help. What?

**Chris Gammell:** I'm so confused. My American brain is screaming.

**Jack Gansel:** The embedded systems conference starts off with a candle lighting ceremony. Wow. And I don't, I'm trying to figure out what the meaning is. It's a beautiful thing. I don't, I don't understand it at all. But the, the, our cultures are very, not really orthogonal, but they're definitely not aligned. And it's quite fascinating.

**Chris Gammell:** I'm surprised it was only four, you said 400 people total?

**Jack Gansel:** I think, yeah, I'm pretty sure it was 400. I mean, it's tiny.

**Dave Jones:** But it's fairly expensive to go to, right? So I assume that's a limiting factor.

**Jack Gansel:** I think almost everyone who attended was, their companies paid for it. Oh, right.

**Dave Jones:** Yeah. Yeah.

**Jack Gansel:** But it's a fraction of the cost of the U.S. In the U.S., to go to the conference sessions can cost you a couple of grand. And I think in India, it's about a tenth of that. Wow.

**Chris Gammell:** That is crazy. Yeah, it's interesting.

**Jack Gansel:** But all the big guys were there, you know, Wind River had a booth. Green Hills had a booth, you know. Even though the turnout is slow, or is low, what I'm told is that the quality of the attendees is very high. Yeah. And some of the talks were pretty advanced. I mean, there was a whole day session on Android. And Android, I sat in for some of it. And, boy, I'll tell you, that was a fast-paced session. And people were taking notes like crazy. So, you know, there's cutting-edge stuff going on.

**Dave Jones:** Yeah. And so do you think they're keen because they're hungry? No, you know, even in the true sense of the word. Well... Hungry.

**Jack Gansel:** I think the engineers are not hungry that way. The engineers, anyone who's an engineer is rich by Indian standards.

**Dave Jones:** Right. Okay.

**Jack Gansel:** But they are hungry to learn. Man, you can see that. They are hungry to learn. And the truth is, I see that at all the ESCs. The people who are willing to cough up the money for the conference program are, by and large, anxious to learn. And I see, I think I see more of a, desperation is a wrong word, more of an unfailing commitment to it in India than I do, say, at the ESC United States.

**Dave Jones:** One problem with India, though, is their class-based system, I am led to believe. You know, so that it's not as easy for, you know, someone who's less fortunate to rise up and make it. I've been trying to figure that out. It's tough.

**Jack Gansel:** I don't know. I don't understand that enough. I've been trying to. However, if you read the personal ads in the local paper for a boy once girl, it's never a girl once boy, boy once girl. Yeah. That's a world constant, right? Yes. The required cast is always listed. Yes. So that is true.

**Chris Gammell:** That is for an awkward Craigslist ad, huh? Yeah. I guess so. I guess so.

**Jack Gansel:** Wow.

**Dave Jones:** I wonder if that same class system exists in hiring. Well, I'm sure it does. But in terms of, you know, hiring engineers and things like that, are you even able to go to university if you're, you know, one of the lowest class people, even if you can afford it? I mean, I don't know. Any viewers from India can clue us in on that? Listeners. Sorry.

**Jack Gansel:** I would love to hear that because I'm very interested in understanding the culture more. I have no sense of that at all. Yeah.

**Chris Gammell:** Well, Dave, not Dave, sorry. Whoever you are. I'm used to just talk. Yeah. Yeah. Other guy over there. So, Jack, so where else? I'm interested just from the education standpoint, too. So, I mean, obviously, there's a lot of up-and-coming engineers in India and just kind of what you've seen there and also what you've seen other – because you travel so much. So, other parts of Asia, you know, up-and-coming engineers. What's your general feeling about education overseas and other job markets overseas?

**Jack Gansel:** I think historically the education in the Western countries – well, okay, let me back up. I'll complete my sentence. Historically, the education in the Western countries has been significantly better than in the Asian countries. And I'll give you an example. I often flash up a slide of Faraday's Law, which is an awful, nasty thing from electromagnetics that freaking killed us all, you know? And I purposely change – you know, this basically relates E, the electric field, to B, the magnetic field. And I change the E to B. So, B is on the left-and-right-hand side of the equation. In the United States, not once has anyone ever called me out saying, that's wrong. In Germany, every single time somebody will stand up and say, that is wrong. Jackson, that's a German accent. I think there is a difference even in the Western cultures on the focus on this stuff. What I'm finding in Asia is that there is – I think it's more practical, you know, learn, see in 15 minutes or whatever it might be with less of the theoretical basis that we see over here. And my observation is that in many of the Asian countries – and it's not fair to say all. I'm not even sure if India would be called Asian or not. But certainly this is not true in Asia. But in many of the Asian countries like Malaysia, Singapore, even in China in some ways, if you're an engineer in 10 years, you're a failure. Engineering is a step to management.

**Chris Gammell:** That's right. If you're still an engineer, you're doing it wrong. Got it.

**Jack Gansel:** And so what that means is that engineering is sort of like, you know, secretarial school. You know, you have to go through this in order to get a real job. Yeah.

**Dave Jones:** Boo.

**Chris Gammell:** So how does that affect actual, like, technical expertise then? I mean, does it just kind of fall away after that point? I mean, is that what's limiting not the creativity but maybe the, like, the absolute prowess? You know, because they have PhDs over there and everything, but are those PhDs going into management as well? Or where does that knowledge go?

**Jack Gansel:** They say that after 10,000 hours of deliberate practice, you become an expert. And I'm not sure how you measure that in terms of a 2,000-hour work year. That's five years of experience. Let's assume you're running 50% efficiency. That puts you at 10 years experience. That sort of suggests that when you reach the peak of your competence and you move off to some, you know, into management or something. And that's not a bad thing because you don't have to be, you know, a senior engineer to be a hugely important part of the team and very productive. Right. So, you know, and these places, this is all very new. They're still trying to figure things out there because, you know, outsourcing didn't exist 15 years ago. Yeah. So they're sort of catching up. You know, you look at a place like, I was in Brazil twice in the spring. I seem to be going there a lot more recently. Very different. Very different. The people in Brazil strike me very similar to the people in India. Very, very excited about being an engineer. That's what they want to do with their lives. And they're just... That's awesome. Yeah, it is. Yeah. It is. And a lot of companies are moving down there. Freescale's got a big operation in Sao Paulo, a bunch of other ones, because the Brazilian engineers are really, really good, really engaged. And, yeah, much less expensive than Western engineers. Yeah.

**Dave Jones:** There's an interesting trend, which there's talk about this trend starting to ramp up, is that in particular Chinese companies, are moving their R&D back to the US because they can't get enough talented people, you know, not just, you know, grunts who operate pick-and-place machines or something, but they, you know, talented design people. They can't get enough of them in a place like China.

**Jack Gansel:** Yeah. I think there's some truth to that. What's your take on that, Jack?

**Dave Jones:** Do you have anything? Yeah?

**Jack Gansel:** You know, I'm seeing that, but I refuse to call that a trend. I think that... Well, one data point's not enough. Well, no, no, even if there's 100 data points. Come on. I think the truth, if you take, for example, China, I mean, again, a nation of vast resources, lots of smart people. If they want 100,000 universities, they'll make 100,000 universities. And a university by itself will not create talented people or innovative people. But it's part of the basic infrastructure that's required for an innovative climate to arise. And the Chinese are every bit as smart as we are. And as they build this infrastructure, I think that innovation will become, you know, absolutely global. Absolutely global.

**Chris Gammell:** So we always talk about, like, the maker-hacker kind of movement on here, too. What's been your take on that? Because, I mean, we actually saw some news today that, you know, like, even big companies are taking interest in it. Autodesk actually bought Instructables, which is, you know, a project-based site today. Which we don't particularly like that much. Well, that's just because we don't pay for it.

**Dave Jones:** We've talked about it before because you have to pay to get all the information. You've got to join, pay a membership, and then they will give you the instructions to build something. And we don't. It goes against the regular open source, you know, hacker ethos kind of thing.

**Jack Gansel:** Well, I'm going to challenge you on that, Dave. Right. Number one. Okay. These are great questions before I hit the maker thing. But open source, you know, because something challenges open source, don't throw it out. Open source is just one model. It's just one model.

**Dave Jones:** I'm just saying I don't particularly like it, you know. Yeah.

**Jack Gansel:** But, I mean, I presume.

**Dave Jones:** It doesn't mean it's not good. It doesn't mean there's not going to be a lot of people out there who will, and they'll find it useful. I personally just don't like their approach of doing it. But, hey, they've made a lot of money, and they've made enough money for Autodesk to want to buy them.

**Jack Gansel:** So good luck to them. That's great. And I guess you work for free, huh? Yeah.

**Dave Jones:** Well, no, and the other reason I don't like them is because a lot of the people who have put stuff on there have actually – they put stuff on there in good faith, thinking that they were giving it to people. And then they find that, oh, people can't get my stuff. They've got to pay somebody else to get my stuff that I gave to the world for free. It's like – so, yeah, you know, and those people have actually complained to me about that. And that's crooked. And I see their point of view.

**Jack Gansel:** Yeah, I agree. That's crooked. And there was a thing on Slashdot about that today.

**Dave Jones:** Oh, right.

**Jack Gansel:** Yeah, I mean, as far as the maker thing goes, I think that it's about freaking time. I mean, when I was a kid, I was into electronics from a very early age. Typical nerd. You know, it took me a long time to figure out how to get a girlfriend. But I was into ham radio.

**Dave Jones:** What the hell are they?

**Jack Gansel:** Trust me. You should definitely Google that. Right. But I and all my friends were into ham radio because that was what the nerds did. That's how we learned electronics back then. We built radios and all this kind of stuff. Most of us had no interest in talking on the radio, but we were building radios and doing stuff like that. And that's how generations got sucked into the electronics field. Ham radio is dying. Chris is taking his test soon, just so we can have that clear.

**Chris Gammell:** Yes, he is. N3ALO. I was going to ask that. So what is it again?

**Jack Gansel:** N3ALO. ALO. All right.

**Chris Gammell:** The only time I use it is at C. Okay. Well, that's okay, though. I mean, that's very useful, actually.

**Dave Jones:** And it wasn't just the ham radio market that was dying either. If you asked me probably eight to ten years ago, I would have said hobby electronics was almost on its final deathbed. It was. Right?

**Jack Gansel:** I know. It was terrible. But this maker thing is doing the most important thing that he can possibly do, which is getting kids excited about this stuff. Yeah. Whether it's electronics or biology or making cars or whatever they're doing. And, you know, to me, I'm, you know, one of the tests I use to trick people is I'll say things like, well, how does a TV work? And the answer I always get is, well, you press the on button. No, no, no, no, no, no.

**Chris Gammell:** The screen lights up, right? Right. Then it tells me what to buy.

**Jack Gansel:** Well, everything else is magic. And as long as it's magic, that means that people are really enslaved by their technology. And, yeah, I think curiosity and a desire to get some level of understanding of how things work is how we, you know, dominate nature. And that's what got me excited. You know, the reason I'm an engineer is because I like to build stuff. It's not because of, you know, designing circuits or anything. I like to build stuff. And part of building stuff is designing the circuits and writing the code and this kind of stuff. And that's what the maker thing does. You're like pointing at it and saying, I did that. I made that, right? Yeah, and holding the soldering iron and, you know, all that stuff. And I think the maker thing, and there's a lot of aspects to it, Arduino and all that, is fantastic. It's really wonderful. You know, when my son was in high school, he was taking one of these practical classes and the teacher gave him a problem. They were supposed to build a circuit, so if you press various combinations of buttons, different combinations of lights would light up. And it was obvious what the teacher was looking for. It was a circuit with some diodes. And I said to him, you know, Graham, if I were you, I'd throw a computer in there. I mean, this way it's easy to change stuff.

**Dave Jones:** One of those little 8-bit micros that are dead, yeah.

**Jack Gansel:** Yeah, we used a little Z-World board. And he did. And it pissed the teacher off. Awesome.

**Dave Jones:** It wasn't the answer she wanted. Oh, that's great. That is brilliant. I love it.

**Chris Gammell:** So did you have a parent-teacher conference after that one, Jack? Oh, yeah.

**Jack Gansel:** And then I had to talk to the teacher about the classic case that you probably have heard of where there's a test. And the physics professor on the test says, if you have a barometer, how do you measure how tall a building is? And one student gives the answer. Oh, I know the answer to this one. I throw it over the side and time how long before it hits the ground. And time how long it takes. No, no. Yeah. Okay. Do it again. Well, I tie it to a string and lower it over the side and measure the length of the string. Oh. And the guy comes out with like 15 different answers.

**Dave Jones:** See, I would give him an A straight away.

**Jack Gansel:** You know. Yeah. Yeah.

**Dave Jones:** Thinking outside the box. Brilliant.

**Jack Gansel:** Yeah. That's what engineers are.

**Dave Jones:** They're the ones who turn into something, not the people who just learn things by route and, you know.

**Jack Gansel:** I'll give you another anecdote. A friend of mine. Go for it. A friend of mine was just, this was just two months ago. He had a system with 40, I think it was 45 little microcontrollers on it all communicating with I squared C. And there was some kind of a comm problem. And he couldn't figure it out. And I said, you know, Brian, I've got this protocol analyzer on my scope that will watch I squared C. We can figure this out in a heartbeat. So, well, we have a Thursday night group, which we've done for about 20 years. Every Thursday night, a bunch of us get together at a bar and drink beer, argue about politics and stuff. So I brought my fancy scope protocol analyzer there. He brought his embedded system there, power supplies. We set this up all over the various tables in the bar and we're taking data. Nice. He figured out the problem. And this guy in the bar comes up to us and says, you guys, what are you guys doing? We tried to explain. He said, you guys must make a lot of money, huh? I'm thinking engineering was sort of the nerd career. These people are losers and stuff. But, you know, in this country, once you become a senior engineer, you're making a six-figure salary. That's the average family income in this country for the whole family, not just one earner. For the whole family, it's $51,000.

**Dave Jones:** See, it's not that great here in Australia, really. Yeah, you can earn six figures Australian. But if you do earn six figures as just a regular design engineer, you're doing pretty well.

**Jack Gansel:** And that's not even real money, right? That's Australian dollars.

**Dave Jones:** That's Australian dollars, which is worth more than the U.S., yes. It's $1.11 at the moment. It's so embarrassing. Just want to boast there. Oh, boy. So, yeah, I guess it is good money in U.S. terms. It is. It's a great profession. Yeah. Once again, it's better than the average. Like the average wage in Australia might be half that or something. So, yeah.

**Jack Gansel:** Right. And that's the way it is here.

**Dave Jones:** It's definitely good. But it's not spectacular. And there's really a cap on that, really. You know, it's not like you're going to be able to earn $150,000 a year as an engineer here or $200,000. That doesn't happen there. It doesn't matter how experienced you are. It tapers off. It's got that, you know, taper off effect.

**Jack Gansel:** And that's true here. I mean, virtually no one's going to make more than $120,000. But, you know, if you're doing something you love and you're making, by comparison purposes, a ton of money, it's pretty hard to knock it, you know?

**Chris Gammell:** Yeah. So what about the – so we always hear these reports over and over again, you know, can't find enough engineers, can't find enough engineers. I mean, what's your professional take on that? Like, because some sides we hear, well, that's actually corporations saying, you know, we want cheaper engineers. And some say, no, this is actually real. We can't find engineers. So what's your experience with the embedded world, at least?

**Jack Gansel:** I mean – Every time I write about this, I get all kinds of angry email from people saying that it's the corporations that are trying to drive salaries down. And the argument that people will make is if there is such a shortage, shouldn't salaries be going up because of the law of supply and demand? Well, the truth is salaries have gone up. I mean, we've been talking about how well an engineer can do compared to almost any other profession financially. My take on it is – I don't know if you saw last year – the IEEE was perfectly ecstatic that the year-to-year enrollments for EE students were down only 20 percent. The best year in 10 years.

**Dave Jones:** Oh, really? Oh, really? That's horrible.

**Jack Gansel:** And what that says to me, and I've been following this for a while, there's this sort of negative bubble. Fewer and fewer people going into engineering. And that means fewer graduating, which means there are going to be fewer and fewer. We're getting older because there are fewer young people coming in, which means – Yeah, but that's good for us, right? It's great for us. We're here now. But it means that for companies, there will be an ever-increasing shortage, at least until this bubble corrects itself, if it does. Which means for anyone who is an engineer, I think it's a golden career. Sure. But I think that the engineer who thinks, as I used to think, that engineering was this beautiful thing, pure relationship with a soldering iron. No, I mean –

**Dave Jones:** No, we've talked about trade-offs before. Engineering is building something with stuff you can get. That is – It's more than that. That's what engineering is.

**Jack Gansel:** Today, engineering is – this is the communications age. And today's engineer is going to be talking to engineers in India and China. If you can't communicate, if you can't write, at least technical writing, if you can't do – even on like a 10-minute presentation, somewhat coherent. Yeah, yeah. You know, it's not going to be – you're going to be that nerd, the classical nerd that everyone has made fun of. If you can master those things – and this is the advice I always give, especially young engineers – get halfway decent at technical writing. It doesn't mean you have to become a novelist or have character development or anything.

**Dave Jones:** I'm putting my hand up here, yes. I've written articles for 20-plus years and I can't write for shit. I'm hopeless at it, but at least I can actually string something together.

**Jack Gansel:** You can convey an idea, and that's what it's all about. Active voice, this does this. Do presentations. You know, when I had my emulator company, I was terrified of standing before a crowd. And it became apparent to me that this is something I would have to master. And I worked really hard at learning how to not be terrified in front of a crowd. Now I enjoy it. It's something we need to be good at. And the engineer who is technically good and can communicate well is going to be golden for the future.

**Chris Gammell:** And I can vouch for Jack. I sat through eight hours of listening to him talk about management, no less.

**Jack Gansel:** Oh, my.

**Chris Gammell:** All told, I loved it. It was one of the best presentations I've ever been to, Jack. Oh, thank you. It wasn't the same sentence over and over? It was not. It was not. Okay.

**Dave Jones:** I think it's like an eight-hour presentation on eight hours is the length of stuff I do. That sounds like one of my rants.

**Jack Gansel:** Hey, Dave, you do a whole project in eight hours. Yeah.

**Chris Gammell:** Man, that's a good point, though. So, Jack, I mean, speaking of writing communication, I mean, you are – obviously you've been writing for, what, 20 years for various magazines now? I mean, how did you get into that?

**Jack Gansel:** A bit over 20 years. I went through 12 years of Catholic education in my youth. And one of the things that – My condolences. Thank you. My knuckles still hurt. One of the things the nuns and jesuits do is drive into you the whole English thing. You do an awful lot of writing, composition and all. And I hated every minute of it. But what I found as I got older, I found myself enjoying the written communication more and more. Email, even. You know, it was fun to structure a nice email. And I started – I've kept a journal, I don't know, for 40 years. And I wound up digitizing that at some point and then had ideas. I turned them into some articles and they went over well. And Tyler Sperry, the first editor of Embedded Systems Programming, called me one day after I had a couple of articles run there and asked me to do a column. And that was like 20 – that was 1990. So that's been 21 years. I've been doing a monthly column in the printed edition and for about the last 10 years a weekly in the online edition. And, you know, the coolest thing about it – I mean, I enjoy the writing. I hate the deadline. But the coolest thing is the responses from the readers. I get so much email from people who are so smart and have such really interesting ideas. It makes me question everything I know. Yeah. Yeah. There was – when I was a young hippie freak, way, way back during the Vietnam era, there was a group called Firesign Theater, which was a comedy group that would riff on all the issues of the times. And one of their albums was called Everything You Know is Wrong. And that's sort of the theme I've adopted in my life, that kids have taught me that everything I know is wrong, and the readers have taught me that everything I know is wrong. And one of the nice things is learning new things. It's a – correct a little bit of that wrongness, you know.

**Chris Gammell:** Yep, yep. Well, we should point out, too, that you have – you have a weekly newsletter, or not – more of a at-will newsletter, I guess.

**Jack Gansel:** Yeah, I do a newsletter, email newsletter that goes usually every two weeks, but like me, it goes on vacation during the summer.

**Chris Gammell:** That's a good thing. Yeah, that's one of my favorites, too. I mean, that's a must-read in my column.

**Jack Gansel:** Well, you know, lately a lot of it's been stuff that people have sent in because they're doing so many interesting things, and they send in their ideas. And I reprint them, and I know it resonates with a lot of people. So it goes to about – I think about 25,000 people right now.

**Chris Gammell:** Whew, dang.

**Jack Gansel:** Thanks a lot. Isn't email wonderful, you know? Yeah. It is. Isn't that cool?

**Dave Jones:** Do you remember the days when you used to get letters? Oh, yeah. I can remember when I used to publish an article in the magazine. Then I would get – my address would be in there, and I'd actually get letters, hundreds of them. And I'd type up a reply and print it out. You know, I actually started out on a real typewriter, you know, like an actual ribbon typewriter typing people's replies. So occasionally I'd do a handwritten one. And, geez, yes.

**Jack Gansel:** My daughter came to me a couple of weeks ago. She had to mail something to someone for some reason. She said, do I need a stamp or something to do this? Oh, no. Oh, fail. Modern generation fail. Oh, that's fun, though. You know, when I was a student at the University of Maryland 1,000 years ago, we had a big mainframe, a big UNIVAC mainframe. And we had email. This was 1971. Wow. The way email worked was you'd type your email in or use a punch card deck to put it into the computer. And then at night, these mainframes would call each other up on 300-bond modems and exchange the stuff all over the country. It was awful. But it seemed great at the time.

**Chris Gammell:** I was going to say, I bet at the time you guys are so excited.

**Jack Gansel:** Yeah, it was wonderful.

**Chris Gammell:** It's like magic. It really was.

**Dave Jones:** But I wouldn't give up email and the information evolution for anything. Oh, no. It's fantastic.

**Jack Gansel:** It's just awesome.

**Dave Jones:** It's fantastic.

**Jack Gansel:** It really is.

**Dave Jones:** It's opened up a whole new world, especially on the design side. I've talked about it before. You know, the amount back before the internet, that was before you were around, Chris. You had to actually do engineering without the internet. Young whippersnapper, you. Yeah. I'm unnumbered. You could only design stuff based on what you had in your data book library, in your personal library. Yeah. You know, that's the only, you know, some ad in a magazine for a new chip. That's all you had.

**Jack Gansel:** Nowadays, you can. I don't know if it was like this in Australia, but they would hold at the distributors, distributors who are long gone now, once or twice a year, there'd be this come and get data books things. And we'd drive to them and we'd fill the car with data books. Remember? Yeah.

**Dave Jones:** You'd fill your boot. Yeah.

**Jack Gansel:** The TTL, the TI's TTL handbook. The yellow. Yep. Oh my God.

**Dave Jones:** Yes, I've still got one. Yeah. Right next to me, it's half a meter away from me. Yep.

**Jack Gansel:** Is that a foot and a half? I don't know. Yes. It was. Jack's back on my side. Ah, bloody feet. Yanks. Yanks. But yeah, it was all about the data books. And every year they change. Yeah. I can't imagine with the printing costs. This is before PDFs and stuff like that.

**Dave Jones:** And they're all 1,000, 2,000 pages, these data books. Oh, massive.

**Jack Gansel:** But last year I was involved with a part. One chip. The data book was 5,000 pages and was woefully incomplete. For what I saw.

**Chris Gammell:** Oh, that's. Yeah. The data sheet?

**Jack Gansel:** The data sheet. The data sheet was 5,000 pages and woefully incomplete. Wow. You had to talk to the vendor.

**Chris Gammell:** 5,000, you can't blame them. There's probably a 1% failure. Come on.

**Jack Gansel:** Name and shame.

**Dave Jones:** Name and shame the chip.

**Jack Gansel:** Texas Instruments OMAP.

**Chris Gammell:** Oh, no.

**Dave Jones:** Oh, yes. Yes.

**Chris Gammell:** They crank out a lot of those, too.

**Jack Gansel:** They're very popular, though. They're in the mobile phones. They're massively popular. They're fantastic parts. They're just very complex. Oh, yeah. Yeah.

**Dave Jones:** Man, 5,000 pages. They're the ones with the RAM piggybacked on top, right? They've got the DRAM, the silicon. It's physically piggybacked on top of the silicon of the processor. Man, it's all packaged up in one. That's how they get the large RAM.

**Jack Gansel:** I bet there's.

**Dave Jones:** The large RAM density in there. Amazing.

**Jack Gansel:** It doesn't count, but I bet you there's on the order of 5,000 control registers inside of it.

**Dave Jones:** Oh, my God. Oh, really? Is that cool? That's the amazing part. Yeah.

**Jack Gansel:** But it does everything. I mean, it's amazing what they do. Oh, yeah.

**Chris Gammell:** Well, I know. We talked to Jason about, like, BeagleBoard stuff, and it's almost like you need that to just start somewhere. Because if you're starting from a 5,000-page data sheet.

**Dave Jones:** Yeah, it's insane.

**Chris Gammell:** Throw your hands up and walk away and go get a law degree, you know?

**Jack Gansel:** Well, what everyone... It's going to be easier. The IC vendors are all telling me that what they're having to do today is provide a lot of the whole solution to their customers, the hardware and the software. software because the customers don't have the time to write the software or even understand these parts. So they have to supply that, but they're having trouble with their own management. They have to supply the apps.

**Dave Jones:** And everyone works from apps. Like, you know, a lot of people... Well, smart engineers will choose... They won't be locked into one device. They'll choose the device which already has the app closest to what they want. Sure. You know, because that will save you a crap load of time and money and effort. And, you know, if they've got an example app that does, you know, tweeting via Ethernet or something like that, which is exactly what you need, you're going to go for that chip.

**Jack Gansel:** Yeah. I mean, it's all...

**Dave Jones:** Even though you're a PIC fanboy or an AVR fanboy or something like that, you know? The smart ones will change devices, bang, like that.

**Jack Gansel:** Well, it's all about the Benjamins, you know? How can you save the most money? Get the thing to market fast.

**Dave Jones:** Right. Benjamins. See, I don't...

**Jack Gansel:** That doesn't translate for Dave.

**Dave Jones:** Oh, no, it does. It's all about the funky-looking plastic paper. I'm Americanized enough to know that you have Benjamin Franklin. Is it on your $100 bill? That's right.

**Jack Gansel:** Oh, you're good. You're good.

**Dave Jones:** I'm good. There you go. I watch too much American TV, obviously.

**Jack Gansel:** Well, one thing that I also try to drive into engineers' heads is it really is all about the Benjamins. We're paid to accomplish a business goal. It's all a business endeavor. And we've got to help the company make a profit. And there are a lot... You know, we do our cool stuff. But ultimately, the only reason we're getting a paycheck is to design a product that helps the company make money. And it's very easy for us to get pure and innocent and, yes, but the correct solution is this and... Yeah. But no, no. That's not really true. Right. There are a lot of other really important issues involved.

**Dave Jones:** There are many correct solutions.

**Jack Gansel:** Yes. There truly are. It's all a trade-off. And a trade-off is far more than just engineering trade-offs. Yeah.

**Dave Jones:** And that's our one hour. That's our amp hour, folks. That flew by. That flew by, Jack.

**Jack Gansel:** That did. That was fun.

**Dave Jones:** How was that? That was painless, right?

**Jack Gansel:** Painless. That's the best you can say?

**Speaker ?:** Yeah.

**Jack Gansel:** Right.

**Chris Gammell:** Well, I'll accept the audio setup at the beginning.

**Jack Gansel:** Yeah.

**Dave Jones:** Yeah. And hopefully, it's recorded. Oh, yeah. Because you're recording with Vista, Jack.

**Jack Gansel:** I'm recording with Vista. And I will make every effort to send this to you, Chris. It may be too big to email. But if so, I'll get you an FTP. We have our ways.

**Dave Jones:** Oh, we've got ways around that. We have ways and means. Okay. Yes. But make sure you don't hit cancel. Make sure you hit save straight away after this. Oh, no. Too late. Otherwise, we might be stuck with the Skype recording. Chris is apparently trying to attempt.

**Chris Gammell:** Yep. Oh, boy.

**Dave Jones:** As a backup. Oh, anyway.

**Chris Gammell:** So, Jack, any final words before we close down the amp hour?

**Jack Gansel:** Well, sure. If I were giving final words, you know, as a certified old fart to engineers today, I would say embrace the field. Never stop learning. Things are changing so fast. And yet, my data suggests that most of us don't read much and don't get many technical magazines. If you're not getting at least 10, 12 magazines, technical magazines a month, you're not connected with this field. And one thing I always say to engineers is save money. Bad things happen to good people.

**Dave Jones:** That's one of my top, Dave's top five tips. Is it? I call it screw you money. Watch, search YouTube for Dave's top five engineering tips or something. I don't know. That's one of them. Awesome. Is have enough screw you money. I call it. Yes. So that you can just tell your employer to, you know. Employ off. Or stick it. Or oftentimes. I've got money. It'll tide me over until I find another job. Thank you very much.

**Jack Gansel:** I'm not taking your Dilbert rubbish. Or for reasons of not your own fault. Your employer may tell you that as well. Yeah. Yeah.

**Dave Jones:** In today's tough climate.

**Jack Gansel:** Money gives you options.

**Dave Jones:** I'm always of the opinion that if you're good enough, there's always a job.

**Jack Gansel:** Yes. I think that's really true. But be prepared. You know. Complicated, difficult things happen. You know. People get sick. Shit happens. Shit happens.

**Dave Jones:** Oh, yeah. Exactly.

**Jack Gansel:** And I think that the one thing that we're missing here, guys, is that at some point we should get together for a beer.

**Chris Gammell:** That might be quite a hike.

**Dave Jones:** That might be a bit tough for me. And the fact that I don't drink. Oh, that's tough. Another stereotypical.

**Chris Gammell:** Root beer for Dave.

**Dave Jones:** A double stereo. A, I'm an engineer. And B, I'm Australian. I don't drink. What?

**Jack Gansel:** I didn't think Australians were like that. They haven't kicked you out yet, huh? I was talking to a buddy who's, he was going into Australia and the customs or immigration said, do you have any criminal record? And he quickly snapped back, oh, do you still need one? Oh.

**Dave Jones:** Well done. Wow.

**Chris Gammell:** I hate that. Oh. Well, I think. How, and how was that received? I don't remember what the response was. Never heard from him again.

**Jack Gansel:** I don't know why. No, you're right. No, my experience in Australia is that people have a great sense of humor, and I'm sure

**Chris Gammell:** that there was a laugh that came out of that. You couldn't help that. That's great.

**Dave Jones:** I love it.

**Chris Gammell:** We might have to play the, Dave snuck in the Australian, some Australian pride songs when I'm not editing. So we might have to sneak one in just to make it feel better at the end of the show here. Good.

**Jack Gansel:** One of my favorite countries. Awesome. You guys are so much fun. Yep.

**Dave Jones:** Well, thank you very much, Jack. It's been a pleasure.

**Jack Gansel:** Yeah. Thank you, guys. I really had a good time.

**Chris Gammell:** Yeah. We hope to have you on again soon. Excellent. Sounds like a plan, man. Absolutely. All right. Been a good show.

**Dave Jones:** Thank you very much, everyone.

**Chris Gammell:** Yeah. We'll talk to you guys next week. See ya. Bye-bye. Bye-bye.

**Chris Gammell:** Bye-bye.

**Speaker ?:** Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye.
