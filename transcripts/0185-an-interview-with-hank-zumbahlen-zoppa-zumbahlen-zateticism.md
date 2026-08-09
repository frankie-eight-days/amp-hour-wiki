---
episode: 185
title: An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism
url: https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/
---

**Dave Jones:** Hey guys, real quick announcement. I'm going to be out in LA next week and we're going to try and do a meetup out there. So if you're in the LA area and you want to come and drink some beers and hang out and talk about electronics, it's also possible some of the Hackaday folks might be there. So keep your eyes and ears open for an announcement on The Amp Hour this week on TheAmp Hour.com. And I'll try and send that out via Twitter and everywhere else. But hopefully we'll be able to get together for a hangout in person and we can all meet one another. All right, on with the show. This is The Amp Hour Podcast. Recorded February 17th, 2014. Episode 185. With guest Hank Zumbelan. Zappa Zumbelan Zeteticism.

**Chris Gammell:** Welcome to The Amp Hour. I'm Chris Gamel of Contextual Electronics. And I'm Michael Lossman of Greyscott Gadgets.

**Hank Zumbelan:** And I'm Hank Zumbelan from Analog Devices.

**Dave Jones:** Welcome, Hank.

**Hank Zumbelan:** Thank you.

**Dave Jones:** We have a non-standard co-host here today. Mike joined us again because Dave couldn't make it. But we're glad to have him. And we are going to throw as many analog questions as we can at Hank because I think he's probably the most analog guru we've had on the show to date.

**Chris Gammell:** And I'm super excited. Thank you, Chris, for having me because I'm excited to get to talk to Hank. Yeah.

**Dave Jones:** The only downside, I think, to doing a show audio-wise is that I feel like Hank could draw us enough PCB layout diagrams to kind of take us through the rest of the day and tomorrow as well. And so we won't have that, but hopefully we can do it by audio.

**Hank Zumbelan:** Oh, by the way, when I said I was going to be here all night, I wasn't really serious about all night. Okay, not all night.

**Dave Jones:** Okay. All right, fine. So, Hank, could you give us a little bit of your background, you know, how you've come up through engineering through the times and then kind of bring it to the current day and your writings that we all benefit from?

**Hank Zumbelan:** Okay. When I graduated from college, I went to the University of Illinois. I graduated in 74. And I got a job immediately out of college at National Semiconductor. Nice. They worked me for about two months, and then I got laid off. Oh, jeez. They spent more on getting me out to California than they did in my paycheck for the time I worked for them. So after that, I got into the system design part of it. I worked at a company that made telecom test equipment, Halcyon, no longer among living.

**Dave Jones:** Rest in peace, Halcyon.

**Hank Zumbelan:** Then I went to a test equipment manufacturer for integrated circuits. They're still in business, but just not the group that I worked for. I had that magic touch with you hire me. You better start looking for other employment. I haven't been able to kill analog yet. Oh, great. You know, I've been there for a while. But after I worked at Sentry Test Systems and I was at Cignetix for a couple of years, and then I went to analog devices, and I've been there almost 25 years now.

**Dave Jones:** Wow. That's awesome. So, I mean, that's a lot of test equipment stuff there. Obviously, you've been on your rampage throughout the industry, taking companies down with you as you go. So when you say system, though, what do you mean by system-level engineering? Do you mean like board-level versus silicon, or how do you define that?

**Hank Zumbelan:** Yeah, I mean, board-level and integrating it into a whole system. Not integrated circuit design, but, you know, taking ICs and stuff and making systems out of them.

**Dave Jones:** That's good, yeah, because, I mean, that's the kind of stuff I think a lot of our audience does. I mean, that's what I do. I think, Mike, that's what you do. Mike writes a lot of software, too. He's an outsider.

**Hank Zumbelan:** I never got too good at diddling bits, so.

**Dave Jones:** And analog devices, then. So that means that you were more on the application side of things and kind of developing the system-level applications?

**Hank Zumbelan:** Yeah, I've been an application engineer the entire time. I started as a field applications engineer and then worked into the central applications group. I spent several years doing seminars and the like, which that job kind of went away because we stopped doing the seminars as often as we were doing them before. And during the whole time, I've been involved in trainings and doing the writings and things like that. And I think that's kind of a sideline to the job.

**Chris Gammell:** Yeah, so your book, Linear Circuit Design Handbook, I was looking around online a little bit. And so there's a – I guess it's an older version of it that is available in PDF form from analog devices. But the newer version is in print. Is that correct?

**Hank Zumbelan:** They're pretty much the same. There's slight differences between it. The one that's available PDF, there was a chapter in there that had a lot to do with tools available from analog. And we basically left that out of the print version. Other than that, they are pretty much the same. And they're both roughly the same genealogy. I think we published the analog devices version about 2005. And then the Elsevier did one. They basically took the book and then relayed it out to their format. And so it was like a year and a half after that that it came out.

**Chris Gammell:** So is that book basically an outgrowth from your training and seminars? Yeah, we like to call it the seminar that never was.

**Hank Zumbelan:** I like that. At the time, we were doing seminars like we did in 2002. We did one on op amps that was basically Walt Young. It was his last version of his op amp cookbook type of thing. The next year, we did one for converters, both of which were then converted into the books as well. And then this one was done as kind of a lump together of those two topics plus other stuff has to do with sensors and the like. And it never really got to the point of actually going on the road as a seminar.

**Dave Jones:** I have to say, so when I first found, I forget, I was Googling around for something and one of the chapters came up. And I think it might have been about the data converter stuff that's in there. And I remember I found the PDF and I started reading through it. I'm like, wow, you know, this is just a great chapter. I can't believe they left it online. And then I kind of like started, you know, playing with the URL there. And I'm like, oh, my God, they left all of these PDFs out here. I'm kind of like looking around like, I wonder if they're going to catch me. And then I realized that then, of course, you know, like a month later, someone sent me the page that lists all the PDFs and that they're all yes, indeed free. And I'm like, oh, man, I thought I like beat the system. That's a really good resource. Oh, man.

**Hank Zumbelan:** Yeah, I still use it. My job today has a lot to do with answering technical inquiries and things like that. So I still use it and I still send out links to it all the time because it is a pretty good general composite of most of the stuff you need to know. Yeah.

**Dave Jones:** Oh, yeah. I mean, I've been pointing it. And so I have this new course, Contextual Electronics. And basically, I've been pointing everybody at it, too. You know, just like, you know, oh, I have a question about grounding. I have a question about linear regulators, that kind of stuff. It's like, no, go check out this handbook. It's definitely. And I think the thing that's interesting about that, too, is that a lot of like a lot of bigger companies might not realize that, you know, having this kind of stuff free and out there online, it builds this goodwill like towards the company as well. It's like, you know, I think, oh, analog devices. Yeah, they got this great book online. I mean, I don't know if I'm allowed to say as much, but I think the same kind of thing about linear tech and LTSpice. You know, just like having free resources endears me to the companies that give me said free resources, including access to people like yourself. I mean, that's just a really valuable thing.

**Hank Zumbelan:** Well, and in point of fact, integrated circuits are kind of stupid by themselves. And if you don't know how to hook them up together, they don't do a whole lot. So, you know, it's part of being able to get things to work. And, you know, applying integrated analogs, specifically integrated circuits, there's some things you need to keep in mind while you're trying to do that to get it to work right.

**Dave Jones:** When you mentioned, so we were talking before the show as well, that a lot of the content in that book and your app notes and your content comes from your own frustrations and wanting to basically help people reduce their banging their own heads into the wall at two in the morning, that kind of thing.

**Hank Zumbelan:** Yeah, I mean, pretty much that's it. If you want to think of it as kind of a – I've been there and I'm going to try to help you not make the mistakes that I made before because, you know, we find that people tend to do the same things as everybody else does because it's the most logical thing. And the kind of mistakes that people make are typically repeated and specifically in the area of grounding and power supply decoupling and the like. That's something a lot of people take for granted until it turns around and kind of nips them in the hind end, you know?

**Dave Jones:** Yes. At two in the morning, of course. Yeah. Day before it's due, yeah.

**Hank Zumbelan:** Well, I've had my share of having things not go exactly the way you expect to and, you know, you're up against a deadline. You have to get something out at a certain time and things just aren't cooperating with you. And it's – the main thing in my life now is to try to reduce stress as much as possible, you know?

**Chris Gammell:** That's good. Very zen. Very zen. So what's it like working for analog devices and what location are you in?

**Hank Zumbelan:** I work out of the San Jose office, although a lot of the time I actually work out of a home office, but I'm associated with San Jose. I did a lot more, you know, when I was actually working as a field applications engineer because then I was interfacing a lot more with our sales guys, going out to customer sites and the like. Now most of the interface that I do with customers is phone support and email support. I do get mailed out pretty regularly to do training for our distributors because most of the distributors have now put in applications people. And, you know, we need to keep them as up to date as we possibly can. That's one of my major job functions of late.

**Dave Jones:** Do you ever do any public seminars where people can kind of hunt you down and find you and ask you questions in person like that?

**Hank Zumbelan:** Yeah. It happens not as much as it used to. I mean, like I said before that, about 10 years ago, that was the main part of my job doing the seminars. Now it happens less frequently. But Analog just went through a series of seminars started last June. We called it Design Conference 13. Actually, I guess it started in May. And we did them in a couple of cities and then we did an online version. And I went out and did the U.S. versions. I got mailed over and did a couple over in Germany. So it does happen. Actually, I enjoy doing that. So I kind of wish it happened a little bit more.

**Dave Jones:** Yeah, it's nice to probably get out and meet people and see the ones who are actually having problems versus – I think that's kind of the problem with a lot of – I mean, I even feel this on the other side. I'm trying to talk to people who want to help me out, like FAEs or factory applications engineers. And it's like the default response is always, well, send me everything you can by email and I'll try and piece it together. Whereas before, I'm sure you were able to be like, okay, can we go back in your lab and you can just point at the thing? I'm sure that that's challenging these days.

**Hank Zumbelan:** Yeah, not doing the field job anymore. So I don't know how quite that's going. But when I was doing that, a lot of time we would go back into the lab and sit there and kind of poke around on a board. And after having spent some years trying to debug circuits, you develop a few little techniques to go in and look at things that other people may not know. And I think that it's kind of a nice feeling from my point of view to be able to go in there and to help people out. It gives you a nice feeling.

**Dave Jones:** Yeah, you're like Superman at that point. You're like swooping in. I don't know if I go that far. Allow me to place the finger of wisdom onto your circuit and impart the capacitance of awesomeness. No, no, seriously.

**Hank Zumbelan:** There was one time where I did something very similar to that to prove to somebody that he had a bit of a problem. I actually stuck my finger in and changed the whole parameter of what was going on. It was because he had a grounding issue. And adding a little bit of stray capacitance and an antenna effect of my body, once he saw that, he started to understand what the kind of things he had to do to kind of improve his circuit. And it's not always stuff that appears on a schematic. Yeah, definitely. How you lay things out can have a pronounced effect on how a circuit works.

**Chris Gammell:** Speaking of grounding, your article, Staying Well Grounded, is a terrific article. It's one that Chris pointed out, and it's one that I had kind of forgotten about, but I had seen that months or years ago. And it demystified a lot of things for me, especially dealing with data converters and the insights in that article about the analog ground versus digital ground on the same chip and what to do with them. I found that very helpful personally.

**Dave Jones:** Yeah, me too. Between that article and then I think Henry, former guest Henry Ott as well, had another analog to digital converter article as well. I think those two basically carried me through my past two jobs completely. Yes, boss, I do know what I'm talking about.

**Hank Zumbelan:** Yeah, it's one of the things we continually run into, and that's why we spend a lot of time talking about it. And we found that when we were doing the seminars, the practical stuff we always would keep in the last quarter of the seminar, because it's usually day-long things, divided up into four sections. The last section usually was the practical stuff, had to do with grounding and power supplies and stuff like that. Again, things that people don't really think about until it causes them all sorts of grief.

**Dave Jones:** What would you say – so you run into this kind of decoupling stuff and grounding issues. What are some of the more common issues that you see aside from those? Are those kind of really the biggest ones, or do you see other stuff that pops up a lot?

**Hank Zumbelan:** I would say that they're two of the major things, but not by any stretch of the imagination the only. There's a lot of other things, but that common theme of decoupling, and especially trying to explain the rationale behind decoupling. Do I really have to put these capacitors right at the chip? Yeah. Yeah, pretty much.

**Dave Jones:** Only as close as possible and no closer. Right. Right.

**Hank Zumbelan:** You know, and, you know, well, you know, when I was back in school, I learned that capacitances in parallel add up. So I've got a 10 microfarad here. What is this 0.01 going to help? You know, and the thing is that they're – the analogy that I like to use a lot is hi-fi speakers. You know, you have woofers and you have tweeters. Woofers handle the low frequencies. The tweeters handle the high. Yep. And neither one does a very good job of doing what the other one's supposed to, and that's the way it is with capacitors. You know, you have the reservoir of charge, which would be the, you know, electrolytics, 10, 100 mic, whatever it is, which is a local reservoir of charge. And then you have the higher frequency, which are basically designed to keep the noise out of the chip to start with. And, you know, they are both optimized for doing what they're supposed to do. Yeah. The capacitors are never strictly capacitors. You know, they're a complex system. It's inductors and resistors and capacitors. And trying to understand that and keep that in your head is one of the true tricks of the trade.

**Dave Jones:** So how do you – I mean, is it for you, is it mostly just experience and kind of seeing these patterns over and over again? Or how – do you have any rules of thumb that you follow or anything like that?

**Hank Zumbelan:** Well, a lot of it has to do with experience. A lot of it has to do with talking with other people and seeing what kind of issues they have. Because like I said before, there's a lot of times that the basic problems, the simple things, tend to be repeated by people all the time. And so you keep seeing the same thing. And so that says, well, you know, obviously this is something people need to be kind of warned about. And none of us live in a vacuum. So me talking to other people and other people talking back at me about different things, you get – even though you haven't had the experience yourself, you can learn from what other people have done as well.

**Dave Jones:** So how about a quick rundown of this? Because this – like Mike said, I mean, this Staying While Grounded article, one of my favorites personally. What about the whole why can't I hook the D ground and the VDD digital to the digital power supply and the digital ground? Could you give us a quick rundown on that? Because I feel like that is – like that was a big turning point.

**Hank Zumbelan:** Yeah, that's a big issue. Let me start out by saying that I wish I could find the guy who had the idea of making your power supply return and your reference node the same thing. Yeah. I wish I could find him and turn him into a speed bump. We can do that. We have a wide network here. I'm just saying. You know, that's – it's one of the worst ideas we've ever had. But, you know, that ship's already sailed. So now what we have to do is figure out how we can make the most out of what we got. The issue has to do with, you know, when we are drawing our schematics, we put whatever your favorite ground symbol is, triangle or little rake-looking thing or whatever. And we assume that they're all at the same potential. And it's not the case. Especially as you get up in higher frequencies because there's not only a small amount of resistance but a small amount of inductance, which obviously changes its impedance with frequencies. So when we draw these things, these triangles on our schematic, we're assuming they're going to be the same. But it's really not going to be. And so the whole idea is that digital, especially if it's CMOS, which is one of the more common structures we use nowadays, the way CMOS works, it actually shorts the power supply for a very short period of time as it's transitioning from low to high. And so that causes a lot of current spikes. Not only that, would the clock speeds get where they are today? I mean, when I did my first microprocessor-based system, we had this screamingly fast one megahertz master clock. You can do a lot with a meg. You can do a lot. Well, we did. But the issue is that that is just the first, the fundamental frequency. Right. If you take a look at the harmonics, you know, they go all the way up from there.

**Dave Jones:** Stupid sharp corners all over the place.

**Hank Zumbelan:** Yeah. Yeah. Fast rise times. And so all those current spikes have to go someplace. And it's a loop. You know, circuits are always loops. Even if we only draw one wire on our schematic, there's always a return. Because wherever things are going, they have to come back. And so kind of keeping that, that's kind of the whole philosophy. And that's why you operate the digital ground separately from the analog ground. Because the digital ground is going to have a lot of these return currents that you don't want flowing through the sensitive analog. One of my favorite examples, I think is in that article that you guys keep mentioning, is that there's a instrumentation amplifier that's really low power. And the quiescent current of that amplifier going through a five-inch trace, I think I'd have to go back and look, but a relatively short trace, will generate an offset higher than the offset of the part itself. You know, so those are the kinds of things that really sneak up on you because, you know, it's like microamps. And even if your ground is milli-ohms, you know, the offset of that part is only like seven microvolts to start with. So, you know, it's something that unless you get hit in the head with it, you may not think about. And that also, things like capacitively coupled noise in IC itself, depending on the size of the package, you're going to have bond wire coupling parasitic capacitances of, you know, something on the order of some fraction of a picofarad, which, again, doesn't seem like much. But when you start putting these high frequencies in through these wires, that they will talk across into the sensitive analog inputs. You know, and that's a big problem as well. So trying to keep – the analogy I use a lot is think like an electron. You know, try to see where you're going to flow and remember that it's always the path of least impedance. That's the way everybody works. You know, so if I get a low impedance path through the analog ground, that's where I'm going to go. And if you don't want me to do that, then you have to kind of shovel me over someplace else. You know, that's really the trick.

**Dave Jones:** Do you ever find yourself worried about quantum effects when you're thinking like an electron? Oh, I know where I am, but I don't know how fast I'm going.

**Hank Zumbelan:** I never get to that kind of detail. I know. But, you know, the idea is just basically you've got to kind of visualize where the currents are going to flow and you keep the heavy flow out of the sensitive areas. That's the first thing you need to do when you're setting up your system, which is why when you're laying on a PC board, almost as important as the total schematic to start with is how you partition that out and keep things so that you don't have these chances of these high current, high noise, high frequency things getting into your high sensitivity analog areas. So how you lay out your board can have a pronounced effect on how things are done as well.

**Chris Gammell:** So I'm intrigued by your idea of separating the reference from the return. Is that a concept that can be used practically today? Or, I mean, have you seen designs that do that, that have like a separate reference plane that's completely different from the return, power supply return? Or is it a case where we would need a fundamental change to the way our ICs are made to really take advantage of that type of approach?

**Hank Zumbelan:** Well, it's not so much in the ICs because once you get inside the IC, you don't really have a lot you can do about how the grounds are separated anyway. It is a concept that has been used. I mean, I still play around in the audio domain. I still play around with design and stuff myself for my own use. And that's always how I do it. I've talked to other people about it and some other people have adopted it. You've got to remember that there's some other things that you've got to worry about. For instance, if you have multiple ground planes, where do they connect? They all have to go together someplace.

**Dave Jones:** Yeah. And how does your CAD program do it too? Because that's always a stinker as well.

**Hank Zumbelan:** Yeah. I mean, that's one of the big problems with CAD. And, well, back in the good old days when we used to lay them out by hand.

**Dave Jones:** Yeah, you just draw the connection, right? It just overlaps and you're like, oh, it's done. It's right there.

**Hank Zumbelan:** Yeah, yeah. Another interesting story. When I worked at Sentry, I was developing a system that was for testing power regulators. You know, like a national at that time had announced a 20-amp linear regulator. And there was nothing on the market that would test it. So we tried to come up with something. And our first design, we were going to use a switch mode power amplifier because the way it was defined, it had to be plus or minus 64 volts and plus or minus 24 amps, four quadrants square quartered. Whoa. Oh, my goodness.

**Dave Jones:** You don't get to take off the corners like you usually do because of extra power, right? Nope.

**Hank Zumbelan:** Nope. Nope. So, yeah, if you take a look at the worst case, it's been a long time since I did this. But if I remember the numbers right, it was like 3,500 watts. Possible dissipation in this thing if you got, you know, going in one of the odd quadrants where you have like minus voltage and minus current, you know. Wow.

**Dave Jones:** What did you use for a heat sink, like a Boeing 747 or something?

**Hank Zumbelan:** That was, well, actually the first, well, it's one of the reasons why we went to a switch mode to start with. Yeah. To try to keep some of that down. As it turned out, we couldn't quite get the switch mode stuff to work. You're forgiven. It's okay. It worked. But what the problem was, it was also defined to be a 16-bit system. And we had a very hard time maintaining the linearity down to a 16-bit level, as you might guess. Yeah. Wow.

**Chris Gammell:** Especially, when was this? Like the early 80s or something? Yeah. Wow. Wow. Yeah.

**Dave Jones:** 16-bit wasn't as common as it is these days anyways.

**Hank Zumbelan:** No. I mean, the ADD converters were hybrids. You know, it was.

**Dave Jones:** Wow. So, this was to test, you said this was to actually test out a new chip. Is that right?

**Hank Zumbelan:** Yeah. It was, National had announced a 20-amp linear regulator, part of their 7800 series types of things. And so, it was kind of aimed at that kind of thing. Also thinking that, well, if one guy does it, then some other people are going to want to do it too. So, you know, there should be a market out there for it. Yeah.

**Dave Jones:** I mean, people need to heat their homes, right? I mean, they. Oh, yeah.

**Hank Zumbelan:** It turns out that we ended up having to scrap the switch mode and go to a standard linear amplifier that had basically the same specs. And so, the power supply on that thing was amazing. I mean, it was just, it was like the coupling capacitors. It had 65-volt rails. And the coupling capacitors was something on the order of about three farads.

**Dave Jones:** So, we took these trash cans, we filled them up with coils of paper and liquid.

**Hank Zumbelan:** It wasn't quite that, but it was pretty close. Yeah. Actually, my technician, I told him, whenever you're going to start messing with this thing, turn it off. Go get some coffee. Yeah. Back in about 20 minutes. Because I put bleed resistors on it, but, you know, I mean, for practical reasons, the time constant was still pretty long. Yeah. Now, he didn't listen to me. Oh, no. And so, he left it set for about five minutes. And he said he was going to short out whatever charge was left with a screwdriver. Does he still have all his fingers? He has his fingers, but he doesn't have a screwdriver.

**Dave Jones:** That thing vaporized, right? It did. It took a tongue out of it. What time of conduction would I like to talk to him?

**Hank Zumbelan:** Wow. So, you know, that was one of the more humorous things. It made a hell of a noise, too, when he popped that.

**Dave Jones:** Yeah. Wow. What kind of package does that come in? Like something that's that? It was a T-03. T-03. Okay. As I remember. Yeah. Buckets of heat thermal paste.

**Hank Zumbelan:** Well, see, that's why it never really took off. And I don't think it actually stayed on the market very long because the whole practical issue of trying to dissipate any kind of voltage drop between the input and the output, you know, that's got any kind of value to it at all times the 20 amp possibility going through there. Yeah. You start getting into a lot of watts pretty quick. Yeah. And just the practical concern of trying to heat sink that was not trivial.

**Dave Jones:** Right. You always get the edge on that number, right? 125C. That's all you get. You just got to stay away from that number before your silicon starts to go bad. That's right. Yeah. That's crazy.

**Hank Zumbelan:** I forgot where we were going with that. Yeah.

**Dave Jones:** I do too. But who cares? That's such a great story. So, well, so I was going to ask, because Mike's here and he's doing RF stuff, how much of your stuff is touching on RF these days, if not in a direct manner of actually generating or measuring RF, but also just dealing with the increased nature of, you know, so many more RF devices these days?

**Hank Zumbelan:** Well, obviously frequencies are going up across the board. I mean, we're starting to talk about frequencies now that, you know, even five or six years ago would be considered ludicrous. But, you know, they exist now. And, you know, everything, my major experience level is at much lower frequencies. But everything that occurs down there occurs the same at high frequencies with some added things that happen, like current, the forward and return path. The return path tends to congregate directly under the forward path in traces. So at low frequencies, if you have a nice wide ground plane, then everything's fine because the current will kind of go through the whole plane. But at high, as you go up in frequency, it's the path of least inductance in that case. And so it tries to minimize the loop by concentrating the current directly under the forward path, which is an added detail that you don't have to concern yourself so much with at lower frequencies. So the basic concepts stay the same, but some of the details change a little bit as you go up in frequency.

**Chris Gammell:** So when you say at lower frequencies versus higher frequencies, what frequencies are you talking about? Megahertz? Gigahertz?

**Hank Zumbelan:** Basically, when we start talking about low frequency versus high frequency, generally it's someplace between 10 and 100 meg. Okay. It's a dividing line. It's not truly defined. But generally below a megahertz is a little bit more simple than the higher frequency stuff. And once you start getting above 100 megahertz, then you have to start looking at all these things a little bit differently.

**Chris Gammell:** So basically the same frequency threshold, roughly, at which you need to start worrying about your circuit radiating.

**Hank Zumbelan:** Exactly.

**Dave Jones:** Yeah, I always think about that stuff. Whenever I see a trace jumping over a ground plane, I always think about that, like the return path coming back underneath and then it hitting that ground plane like just like a cliff and it just going, no, I'm going wherever I want at this point. And then your EMI testing fails immediately.

**Hank Zumbelan:** Yeah, exactly. And we've covered that in some of our stuff in the books that have to do with, you know, if you are routing a trace and you have a discontinuity for whatever reason where traces are crossing each other or whatever, that all of a sudden the electrons that are running around that return path all of a sudden go, ah! Because the place they wanted to go is no longer available for them.

**Dave Jones:** Yeah. Yeah, they go evil-knievel over the gap and they just jump off into space.

**Hank Zumbelan:** Yeah, and that's what happens when, you know, and when you put things like that on a board, as they do, they radiate out. And that causes all sorts of problems. You know, when I was back doing most of my design work, the radiative field testing still wasn't done all the time and there weren't as many commercial rules about what you could do, but that's one of the other things that's happened. And as the whole commercial and consumer stuff has gone up into these high frequencies, you know, with cell phones and wireless and Bluetooth and all the rest of that stuff, that you've got so much stuff floating around in the air that you are worried now about how much stuff that you're sending out and how much you're actually being able to receive all this anonymous stuff that's floating around and how much that affects you. Both of those have become a lot more rigorous concerns than they were, you know, several years ago.

**Dave Jones:** Yeah, your cube mate's got a HackRF in his cube and he's just spewing out some kind of SDR frequencies. Right, Mike? Am I right? Something like that. Yeah. So, Hank, because I know Analog Devices has a bunch of up-converters, down-converters and mixtures and all that stuff. Did you ever jump into that side of things or was it mostly more on the low-level analog stuff?

**Hank Zumbelan:** I touch it occasionally, but, you know, my comfort zone is definitely down at the slightly lower frequencies. Yeah. But, again, I've heard enough war stories and can relate it that, you know, I can help people out a little bit, but it's really not really where I have my strength. It's really at the lower end of the spectrum, you know, where things are a little sane.

**Chris Gammell:** Yeah. One thing I really like about the RF chapter of your book is your section on mixers, and you have a diagram in there that just shows, like, a sine wave RF and a square wave LO and then the product. And it is amazing how hard it is to find a diagram like that. You know, it explains how mixing works so clearly. And it took me a long time when I was getting into RF to really grasp just exactly what that diagram expresses.

**Hank Zumbelan:** I won't take credit entirely for that. You know, a lot of what's in that book has been gleaned from the – there's a lot of smart people at Analog. And a lot of that stuff has been things that I've seen that other people have done. But that particular diagram, I remember it. It was something that made a lot of sense to me when I first saw it, and that's one of the reasons why I wanted to include it.

**Dave Jones:** What about the – so the chapter on sensors and stuff like that. So I'm always interested to learn how things hold up over time. I mean, have you found that a lot of the sensor stuff has held up, especially as we've kind of moved into more integrated sensors these days?

**Hank Zumbelan:** You know, it's basically the same thing. At Analog, we still do a lot of business in the industrial marketplace. People are still measuring temperature. People are still measuring pressures, and they're using that to control systems. That hasn't changed. I mean, the way we interconnect things has changed. Our ability to measure those things has changed in that we can now do it at much higher accuracies and at much smaller dimensions than what we were able to do before. But the basic need to be able to measure things and control systems based on those measurements, that hasn't changed, and it's not likely to for a long time. So there's still a lot of that kind of stuff around.

**Dave Jones:** We were marveling at that new ADUCM 350 last week, and I've looked at the 360 before as well. And those, I mean, just the amount of integration these days with, like, onboards. I mean, that thing's got a Cortex-M3 in there, and it's like this whole analog front end and power and all this other junk. It's just like, I mean, it's getting to the point where, I mean, these sensor chips are starting to approach, because they have micros in them. You know, they're pushing 1,000-page manuals now, too. It's insane. So it's cool, but it's frightening as well.

**Hank Zumbelan:** Well, the whole integration thing is a two-edged sword. I mean, it makes a lot of sense that if you have a target market that can support development of highly integrated sensors, then the fact that you're putting all that stuff and taking it up off a PC board and putting it on the chip itself makes a lot of sense. The problem is trying to make that fit for target markets that aren't – I said that wrong. Trying to make that fit for markets that aren't the target market, you know, and trying to bend them around to do other things. That's where it becomes a little shaky sometimes. But if we could integrate everything, we save a lot by having all this stuff in close proximity so we don't have the same kind of radiation issues. It's the kind of thing where we only have to solve the problem once. And once we have it solved in the chip, then every time that chip is used in a different application, they don't have to worry about all that kind of stuff again. So, you know, and with the reduction in size of the geometries that they use to build integrated circuits now, you can shove a lot of stuff in even the very small packages.

**Dave Jones:** Oh, yeah. Yeah, I think that one we were talking about is like an 8x8 BGA or something like that.

**Hank Zumbelan:** Yeah, and the problem with that is it could be even smaller if they could get the ins and outs, you know. Yeah, right. The problem is getting in and out of the chip, you know. If you were to take a look at what the active circuit area is compared to the size of the package, it's pretty small. It's, again, the number – just trying to get the things in and out that becomes the big issue.

**Chris Gammell:** That seems to be true for a lot of parts. And as we go into higher and higher frequencies, that becomes a bigger problem, having to have a big package for a small part. Do you see any, I don't know, technological advance on the horizon that might alleviate that problem?

**Hank Zumbelan:** Well, I mean, we've gotten to the point now that some of the packages are basically the size of the die. You know, there's some of those things that – in the smaller packages, I mean the smaller functions where you don't have as many pins. Right. We have what we call the bump die packages, which are, you know, basically the size of the die itself. You know, I don't know how much smaller you can go with that. The larger functionality where we have, you know, the higher integration, the ins and outs, basically, if we could find a way to cut those down, we could make smaller packages. But, you know, that's why the integration at the higher frequencies may not happen quite as fast because of the fact that there's these technological hurdles we have to cross having to do with getting signals in and out.

**Chris Gammell:** So I'm curious about your audio hobby. Can you tell us what some of the projects are you've done?

**Hank Zumbelan:** I'm a musician, so a lot of my stuff has to do with audio. I actually wrote an article, geez, late 90s, mid to late 90s, I guess it was, about making an outboard DAC for a stereo system where you take the AES-EBU input and then convert that into a DAC that was done outside of the chassis. So that, you know, I optimized power supplies and I went to the ludicrous fringe on the filtering on the output. And it came out pretty well. I actually had some good reviews from the stereo Golden Ears crowd. You know, so that's still playing in my system at home.

**Dave Jones:** What is the ludicrous fringe? I don't know that term. I'm sorry.

**Hank Zumbelan:** Excess is not nearly enough. My reconstruction filter on that thing was 7-pole. Oh, my gosh. At the time, most people were operating with maybe 4. 3 was a lot more typical.

**Dave Jones:** So that was a Spaceballs reference then or what?

**Hank Zumbelan:** Why not, you know? The name of my first CD was Unknown Artist, Unknown Album.

**Chris Gammell:** So what kind of music do you do? What instruments do you play?

**Hank Zumbelan:** Keyboards and guitar mainly. I do a little bit of electronic stuff where I use these virtual plug-ins to make my keyboard sound like other things. Yeah. You know, a cello, harmonica, harpsichord, you know, whatever. I said, because of my chronology, my basis is in the folk and folk rock, late 60s type of thing. That's where I started playing. And so there's a little bit of that. It's pretty eclectic. I mean, I go across a lot of different things and just kind of give them my own little treatment.

**Dave Jones:** Yeah. We were talking a little bit before the show about the commonality amongst a lot of engineers. I don't know, Mike, if you've ever played music. I used to play a lot of music. And just how it seems to be a common thread a lot. I'm not sure. We're not sure why. Hank said it's possibly because of the math. I said it's to try and meet girls. I mean, I think we're probably both right. Gotta do something. Yeah. But that's really cool that, yeah, I mean, if you start passing the test with the audio files on the actual DACs, you know, that's...

**Hank Zumbelan:** Yeah, it was one of those strange things where it measured well and it sounded good. So, you know, it's best of both worlds.

**Dave Jones:** That's a rare combination. Yeah. So we had a couple questions from someone over on Reddit where we collected some questions for you. And I thought we should get to some of those. We usually kind of skimp on asking questions from people. But there's good ones here. So first one was ADI app notes. I mean, obviously we talked about yours, the staying well grounded and the book. Are there any others that you find yourself going back to that people should know about and should go out and find and memorize and read and that kind of thing?

**Hank Zumbelan:** There's a ton of stuff out there. And there's good stuff from a lot of different sources as well. So, you know, kind of poke around and see what you can find. And in terms of analog, probably the precursor to my staying well grounded was something that was called... Well, it was written by Paul Brokaw back in the late 60s that talked about grounding and making things go right. That's still highly applicable. You know, one of the things that we've run into lately is at Analog we have MEMS functions, accelerometers and gyroscopes and the like. And not a lot of people are really familiar with the mechanical to electrical conversion process. You know, we all know about, you know, volts and things like that. And we can understand amplifiers where you put a little bit of voltage here and you get maybe a little bit more voltage out here. But when you start talking about measuring gravity and tilt and those types of things and converting that into an electrical number, that's kind of confusing. Yes, it is. You've spent some time doing it and it basically comes from experience. So anything that has to do with the MEMS, I think, is highly useful if you're going to go into that area at all.

**Dave Jones:** So, um... And you think that's still necessary even, I mean, like, because there's such high integration with these things these days, too, especially, it feels like a lot of these MEMS, these three-axis, six-axis things, they just crank out coordinates these days. But you still think it's necessary to understand a lot of that underlying stuff?

**Hank Zumbelan:** Well, I think it helps to have a basic understanding of how the things are working. It basically, I mean, we still field a lot of questions that have to do with, you know, somebody doesn't really fully understand. Um... The relationship, for instance, on the accelerometers, it's a CMOS sensor. It's working with zeptofarads. I mean, it's just way, way down there. And, uh... And that small amount of capacitive change then is converted to a voltage. And so you've always got the problem of Gaussian white noise type things. And how that electrical noise and how that kind of affects your accuracy in your, um, mechanical motion is, you know, something where you've really got to kind of think about a while to get comfortable with the correlation there.

**Dave Jones:** Hmm.

**Hank Zumbelan:** So, you know, there's those ones, um... The other one that we have, not so much anymore because people are getting a lot more used to it, but for a long time, the whole thing about how Sigma Delta worked...

**Dave Jones:** Oh, yeah.

**Hank Zumbelan:** ...confused a lot of people. And so there was a lot of stuff in there about, you know... But, you know, yeah, read it a couple of times because the first time you go through it, you're going to say, nah, I don't think so. That's witchcraft. But it really does work, you know, and it takes a little while for it to... For your mind to really get around it and say, oh, well, maybe that... Maybe it really does do like that.

**Chris Gammell:** I get freaked out sometimes when I'm looking for parts. So I'm looking for converters and I'll, you know, like do a price per sample rate comparison and get totally thrown off because some parts are Sigma Delta and some parts aren't.

**Dave Jones:** Yeah. Oh, yeah, yeah, yeah. You're like, oh, I need 20 bits, right? And find a SAR converter and it's like, what, 35 bucks or more?

**Hank Zumbelan:** Okay, now you've said the magic word. The duck's going to drop down here and you're going to get your reward. Resolution and accuracy. Yeah. These are not the same thing. No, they are not. Resolution is the number of bits that wiggle and accuracy is the number of those bits that actually mean something. Right. So, for instance, our Sigma Delta converters are 24-bit data words. So they're 24-bit converters. But you've got to take a look at the SNR to see what they really are in terms of... Because people are expecting, you know, to look at the 24... They're going to ground the inputs. They're going to look at the 24 bits and they're expecting nothing to move.

**Dave Jones:** Right. Right. No. No, no, no. Sorry. Sorry, folks. Physics and stuff. Do you use the term E-knob or no? Is that not a kosher term around analog?

**Hank Zumbelan:** Well, you know, there's a couple different things that you have to look at from a couple different points of view to sort everything out. So equivalent number of bits is one way to look at it. I tend to more look at it as SNR, signal to noise ratio. But they're really the same thing. Right. Yeah. There's a really strong mathematical correlation between the two. You know, 6.02 times the number of bits minus 1.76. You know, so that... You know, it's really two different ways looking at the same thing. To me, SNR, because I came from a strict analog rather than a converter type background. But if you're mainly working with converters, E-knobs may be more in your backyard than SNR is, you know, in dB. Yeah.

**Dave Jones:** Right.

**Hank Zumbelan:** Being able to think about them in both terms is probably a plus. The same thing when you're talking about converters. Same thing talking about the frequency domain and the time domain. To really, really understand converters, you have to be able to go back and forth between the two pretty easily. Sure. Because there's some things you understand in the frequency domain and there's some things you understand in the time domain. Could you give us an example of that? What do you mean by that? Okay. Let me think about this a second. Aliasing. Okay. Okay. So aliasing is when different frequencies appear to be the same once they're converted. You know, it has to do with the frequency of interest versus the sampling rate and, you know, read my book.

**Dave Jones:** Not many people get to say that, folks. Yeah.

**Hank Zumbelan:** So, you know, and that's something that you can look at both in the frequency domain because you can start seeing how when you slide the analog frequency up relative to the sampling rate, how the aliases then move in the opposite direction. Ah, right. Yeah. And another way to look at that is just take a look at, which I've put in a couple of the things we've done is you take three different sine waves at three different frequencies and you sample them all at the same. The lower frequency, 10 samples converts to one cycle of the input. In the middle one, 11 cycles will fit in those same 10 slots. And in the top one, 21 cycles fit in the same slot. Just look at the instantaneous conversion of each one of those 10 time things and they're all the same. And so that's another way of looking at in the time domain what you're seeing that can also be expressed in the frequency domain.

**Chris Gammell:** Yeah. Yeah, that's interesting. I'm always a stickler for trying to get people to plot their time domain digital signals as distinct points instead of connecting the dots with lines. Because then, you know, you start connecting the dots and you fool yourself into thinking that there's something there that isn't.

**Hank Zumbelan:** Yeah. And you've got to remember how a converter works. It takes a series of discrete samples and it really doesn't know what came before, what comes after. It doesn't know about the transition from one sample to the next. All it knows is that its clock is coming through and says, take a sample now, take a sample now, take a sample now.

**Dave Jones:** Yeah.

**Hank Zumbelan:** It does that. It spits back the answer, but you don't really know what happened to the signal between those two samples. And it could be one of several different paths it could have taken to get from one point to the next.

**Chris Gammell:** Yeah, that's a really good point.

**Hank Zumbelan:** So, I mean, that's one of the things where, just to give you an idea of how you've got to kind of go back and forth between the two.

**Dave Jones:** Another question we had on Reddit was similar to what we were talking about before. You know, as chip integration increases, where do you see PCB design going in terms of, you know, changes that need to happen and how, like, listeners and, you know, other engineers out there would need to start accounting for that kind of thing?

**Hank Zumbelan:** Going back to as things are getting faster and faster and smaller and smaller, PCB layout is an issue because, again, how you partition the board, how you lay things out, how you have signals connecting from one part to the next part can all affect how the thing works. And if you're not wise about how you partition the board, then things will tend to get kind of spread out in, from an electrical standpoint, more convenient, but from a physical standpoint, less convenient. You know, like you minimize this trace, but to minimize that one trace, you've now made other ones more complicated. So, and as the clock speeds go up, then the possibility of radiated interference goes up. And so you need to start talking about keeping those kinds of things under control. Also, signals, even digital signals are becoming more and more analog. You know, we're starting to talk about characteristic impedances of traces connecting different points, even though we're talking about strictly digital signals. Now we're talking about having to match the impedance in and out of these parts. We start talking about the trace links having to be matched within a certain wavelength of, especially when we, another thing we've done recently has gone to a lot of differential signaling. And so when you talk differential, those, those two paths that are, you know, the two phases of the signal, you've got to be pretty well matched or you're going to start running into problems as well. Also, the reflected. So if you're not, you know, if your traces aren't matched, you're going to have some, some signal trying to reflect on the, on the trace as well. And those are all things that are non-schematic components. You know, you know, you don't, you don't see it as a resistor or, or anything like that on the, on the schematic, but it's, it is a real component that's on there and you have to kind of keep an eye on that.

**Dave Jones:** Do you find yourself, uh, using more of like the, the signal, signal integrity tools, like, uh, for, for doing trace, uh, like matching and stuff like that for, uh, for what that's called that simulation method. Uh, is it IBIS, IBIS models and that kind of thing? IBIS models, yeah. Yeah. Do you do that a lot?

**Hank Zumbelan:** I haven't done, I haven't done so much with that to be perfectly honest. Um, actually, uh, another war story. That's how I met my wife. She's a printed circuit board designer. Oh yeah. Match made in heaven? Um, not all the time.

**Dave Jones:** Well, no, right. Not when board light out's happening, right? I mean, you're going to argue about where, where the signal goes and everything.

**Hank Zumbelan:** Yeah. You know, she, she was not from an engineering background, but more of an art background. And it actually, that actually gave her a leg up on doing a lot of these things because when she was looking at the schematic, if you have a well-drawn schematic, it kind of, it kind of makes it easier to kind of group things into the right. Yeah. Uh, areas. Excuse me. Uh, and, um, you know, so she may not have had all the electrical, uh, background to understand all these things, but, you know, from an art standpoint, if it looked right, you know, it probably was better that way. And in most cases, you know, so, um, I worked with her a lot, uh, in, in trying to optimize how, how things were laid out. And this was right at the beginning of the CAD period when at that time, I would say that the automatic routing programs were a complete waste of time.

**Dave Jones:** Yeah. I think they still are personally.

**Hank Zumbelan:** I think that they probably are better than what they are, what they were, but I think that there's still, still a little bit that, that the human eye can, can kind of do in things. And a lot of it has to do with how they prioritize, you know, a net list will just prioritize whichever is next on the list, you know? Yeah. Right. And that may not be the optimum. You may want to optimize some other trace, you know? And so it's something that in my mind, we really haven't been able to develop an expert system yet in the, in the computers to, to do a really good job of that.

**Dave Jones:** I think if, uh, if you don't have time to do the layout up front and you're not willing to put the time in, that means you have a lot of time later on to be debugging and, and, you know, wanting to pull your hair out. Yeah.

**Hank Zumbelan:** And not only that, even if you know what you're doing, you're not guaranteed success every time on the first time. Yeah. Yeah. Another, another story from analog. We were making a, uh, cross point switch, analog cross point switch for video. Eight by eight matrix. So eight inputs can be routed to any one of eight outputs.

**Chris Gammell:** I think I've looked at that part.

**Hank Zumbelan:** The, uh, evaluation board, even though we, we kind of know what we're doing in terms of, of board layout, we had to go through several revisions on the layout of the evaluation board to get the crosstalk on the board lower than the crosstalk on the part. Obviously an evaluation board that kind of ruins the performance of a chip is probably not the way you want to go.

**Dave Jones:** Look how great our part is folks.

**Hank Zumbelan:** We promise it's better when you do it. So that, that's the kind of thing where I'm talking about that, you know, even, even though you do this and, and I tell the customers this all the time. This is, um, expect to go through at least one revision of your PC board. Just put that into the schedule while you're doing, while you're making the schedule, because I don't care what evaluation tools you use. Um, the chances, the chances of you doing everything right. The first time are slim. Now, as you gain experience and you've made enough mistakes and you, you hopefully learn from those mistakes and decide not to do those, um, non-optimum tasks the same way, you know, your percentages improve. But there's so many things to look out for, you know, in terms of parasitics with, with how traces truck, talk to each other and ground planes and the like. Um, it's really, really hard to, uh, to keep all of that stuff in front of you all the time, especially since the way things are today that we, none of us have the amount of time that we'd like to have to do any kind of project.

**Dave Jones:** Right, right. You can't, you can't, you can't really stress over it too long and overthink it too much because it has to get out the door and you have to get on to the next thing. Right, I mean, yeah. If the next thing is debugging two designs ago, well, that's just what it is, right?

**Speaker ?:** Yeah.

**Hank Zumbelan:** You know, uh, you, you, there's a fine line there and you have to do a little bit of it or you, you know, to your point earlier, if you don't take the time at the beginning, what was the old, uh, automobile thing, you know, pay me now or pay me later type of thing.

**Dave Jones:** Exactly.

**Hank Zumbelan:** Yeah, that's true in this, in this respect as well.

**Dave Jones:** Do you ever, uh, do you ever get sick of analog? Do you ever like, ah, you know, one of these days I just wish I would have been a, a code jockey or a, I don't know any other derogatory terms for software people.

**Hank Zumbelan:** With the exception of, of trying to find an industry that wasn't as, uh, strongly male dominated. Yeah. I don't think so. I mean, it, it, it's challenging. It's interesting. I, I learn all kinds of new things. I'm, I'm looking at all sorts of, of different, um, different projects, different ideas that people have. I, and I find all of it, well, most of it, uh, pretty interesting. Yeah. Um, so I think that there's, you know, there's a lot, lot worse things I could have done. Um.

**Dave Jones:** I'm, I'm with you, man. I mean, I, I, I, I'm, I'm on the same path.

**Dave Jones:** What about like other, uh, you like people that are kind of like coming out of school now or, or thinking about going into college for like analog, any, any advice for them? Anything like that?

**Hank Zumbelan:** Well, what we've been able to see from analog, analog devices since is that, uh, most of the people that come out of school are very well grounded in, in digital stuff. They can write code. They can, they can program FPGAs and, you know, they, they've got a real good feel for that. But the analog stuff, it's still, you know, the, uh, the black magic and you, and you still have the Merlins running around who understand it while most of us don't. And, uh, you know, I, I think that if somebody was really interested in, uh, in, in kind of adopting that as their, their, uh, major, major area of, of, um, study, I think that it's something that not maybe, uh, offered so much, but it's, it's really kind of an interesting. I mean, I mean, it's, there's so much you can do and so much you can tell me, we're still talking about stuff I was doing 20 years ago. And, uh, you know, how many people, how many digital guys are talking about what they did with a 6502, you know? Yeah.

**Dave Jones:** The C64 guys are, right?

**Chris Gammell:** Yeah. That's about it. So, uh, how do you, how do you recruit good analog people? I mean, you, you obviously need a lot of, uh, analog. I, I see designers that I, analog devices, but you also need system level people like yourself. I mean, where, where do you find them?

**Hank Zumbelan:** Uh, quite often we, we, um, we take people from the industry quite often. So, you know, we, we've had applications, people who have come out of the, uh, the other side of the fence, if you will. Um, the other thing is that, uh, it's, it's kind of a, a groove mentality that, that, you know, you, you have the people who have the basic skills and you sit and let them learn from the people who have more practical experience in these particular areas. Yeah. Because, I mean, I, I know from my, my own personal that, that what I learned in school, uh, just taught me how to, how to learn when I got out in the industry. And, and the, the real practical stuff was all stuff that I learned after I got my degree.

**Dave Jones:** I think it's going to be interesting too, because, um, you know, we've been talking about a lot of the increasing integration, right? And, and so my, my argument against people coming in and showing me these new parts and stuff is always like, you're taking away the fun stuff, right? And that's always my, my argument for, for showing me these new chips. But at the same time, they're also very useful. And I, but what I wonder is moving forwards, like if there'll be like a false sense of security, like, oh, well I can just talk to the registers that are in an analog, analog front end chip, like that 80, 80 UCM 350. And not have to worry about the analog stuff. But then there'll also be this kind of like this latent background. Well, yeah, but you know, you, you stuck it to a piece of bubble gum. You didn't actually put it on a PCB, right? I mean like that, like the, you still need this baseline knowledge in order to actually use a lot of these integrated chips. And I wonder how that's going to affect things going forwards.

**Hank Zumbelan:** I don't think you're going to lose, you know, lose that completely because the chip you were talking about, I mean, you've got all these analog front end things, but they, you got to connect them to something, right? It doesn't do any good. And so there's, there's always, I don't think we're going to get to the point where we're just going to have a piece of silicon that does everything every time for everybody everywhere. You know, the world's varied enough that that's, that's really not where we're going to get. And we're still going to have to have people understand that I've got this really nice chip that does a whole ton of stuff. But I still got to connect it to something to make it work and make it useful, right?

**Dave Jones:** Yeah, I guess on both ends, right? Yeah, yeah, yeah, yeah. Yeah, yeah, yeah.

**Dave Jones:** Yeah. What, what, what is, I mean, you're on the inside. I know you can't tell us about like the super new stuff, but what about, you know, what are some trends or some technologies that you've seen that are really exciting to you on the analog side of things?

**Hank Zumbelan:** Well, the vast majority of that is more evolutionary than revolutionary. You know, it's, it's, it's going faster and, and all the rest of it with, you know, smaller and faster and all, all those things that people want to see nowadays. Anyways, it's, it's rare that something completely new comes out of the woodwork. It does happen. The MEMS stuff is, is a prime example. You know, before that existed, there was really no way to do that kind of stuff. And then all of a sudden we now have a whole line of accelerometers and, and gyroscopes and the, and the like, and people can do some interesting things that they weren't able to do before. Um, you know, we had, um, we have isolators, you know, that, they go across barriers and, you know, that's been done for a while, but, you know, we came up with a new way of doing it. That was a lot more, um, cost effective, lower power. Um, basically what we did is we went to transformers instead of capacitors or optical to do the, uh, to do the conversion. So that was, that was a new technology that, uh, we came up with, but a lot of the stuff is again, just taking what we have and making it better, smaller, cheaper, um, faster. Yeah, more accessible.

**Dave Jones:** Right.

**Hank Zumbelan:** Yeah.

**Dave Jones:** Yeah. Yeah. Because like, I mean, that the, the isolator is a great example. I mean, people used to actually do that with transformers, right? I mean, they would have, you know, drivers on either side, driver, receiver, you know, push a signal across the transformer and yeah. I just sat there doing that all day. Yeah. Now it's a little tiny one.

**Hank Zumbelan:** Yeah. And our value added on that was coming up with transformers that were so small, they could be multiple channels could be put into a normal size IC.

**Dave Jones:** Mm-hmm. Yep.

**Hank Zumbelan:** Um, and you know, there was some practical issues or what about, you know, uh, sensitivity to fields and the like. And it turns out that those guys are actually pretty good because they're so small that the enclosed loop doesn't couple a lot of, a great deal of energy in there. And, and if you take the, uh, outboard transformers, then you've got the traces going to the transformers. You've got the transformer sitting there, not quite as small, so they are more susceptible to fields.

**Dave Jones:** I'm always amazed too. So, so I always wondered about how those things actually worked. I didn't, it took me a long time to realize that it's actually always sending pulses. And then, so like for a low, I think this is how it works at least. It's always sending a single pulse for a low, but then when it does, when a, when a digital signal goes high on, on the isolated side, it's actually sending a double pulse. And that's how it can tell that transition basically or something like that, right?

**Hank Zumbelan:** Yeah. It basically it's, it's, they put a pulse through at every transition. So it doesn't really understand low and highs. What it does is they know that, that the input switched from one to the other. And so it, it, it, it goes across. And the reason that that's required is transformers are notoriously bad at passing DC.

**Dave Jones:** Right.

**Hank Zumbelan:** So, you know, if you have a signal that's not changing very often, you know, it basically looks like a DC signal. And so by, by just putting the pulses through on the transitions, then you, that allows the signal on the isolated side to transition from one state to the other. You just, and it'll stay there until it gets the next signal coming through saying, okay, flip it back the other way.

**Dave Jones:** Yeah. You know, and, and I, for a long time, for me, at least it was, you know, I didn't quite understand the, the draw of, of the whole, you know, isolator thing. Like, why are people even doing it? And then I, I went into the industrial market and it's like, you better be doing it because, and, you know, even just in a more practical manner too, you know, you have, you have common mode voltages that might be anywhere all over the map. You might have, you know, a thousand feet of wiring where that thing's sitting a hundred volts above where you're sitting. And then, you know, you could, you could have some serious current, current flow and actually hurt yourself at that point or hurt your devices.

**Hank Zumbelan:** Well, to the point we were saying earlier, you know, just because these two points are grounded doesn't mean there's the same potential.

**Dave Jones:** Right.

**Hank Zumbelan:** In a big industrial installation, it's the same thing. The details are considerably different. The distances are better or are longer. The potentials you can have between them can be much larger. It turns out to be mainly a safety issue. I mean, one of the primary uses of isolator technology is in the medical field. You know, if you have a bunch of things connected to a patient, you really don't want to make him your, your star point.

**Dave Jones:** That is an excellent point. He'll become some lawyer's star witness.

**Hank Zumbelan:** So, you know, there's, there's a lot of reasons why those, those kinds of things now. And then there's some reasons that, that may not be too obvious. One thing that I've used the isolators for is I made a A to D converter, again, audio application. And I wanted, this is probably seriously over designed, but, you know, I know where to get the parts cheap. That's the most fun though. Come on. Yeah. I know where to get the parts cheap. So it's, you know. I actually had my converters running and then it went into one of these isolators and then all the stuff that happened on the far side was, there was absolutely no chance of having return currents flow.

**Dave Jones:** Yeah. Yeah. I've thought about that because I have this, this cheapo Behringer, you know, ADC effectively and a DAC on board and it's USB based, but then you can actually, you can hear, you can literally hear, you know, the power supply noise from my computer coupling through to the actual analog output. And it's like, oh, it's terrible.

**Hank Zumbelan:** We have a solution for that too. We have an isolator that's designed specifically for USB. Yeah. We found it advantageous to break that connection and have an isolated side and input a super clean five volt to power the peripheral out there and not have that communications back and forth. And you can, under the right circumstances, hear the power supply. If you, you know, you crank everything up and listen really closely, you can hear that kind of stuff going on.

**Dave Jones:** Yeah. Yeah. It's crazy. That's another cool thing too about some of those parts, the isolator parts starting to have power supplies built in too. I really, I like that too, because then you don't even have to worry about that anymore. It just, I mean, it's not going to be a clean power supply. It's still, you know, some DC to DC isolated switch mode, but that's just cool. Yeah.

**Hank Zumbelan:** When you're talking about, we're talking about small amounts of current, you know, DCs and DCs can be made relatively clean because again, you're not spiking a lot of current. So, you know, the interference levels are reduced.

**Dave Jones:** Yep. So, any other technology coming on the pipeline that we should keep an eye on for?

**Hank Zumbelan:** Again, just going faster. I mean, we're talking about in our phased lock loop group. We're talking about, you know, going up in frequencies, 17 gigahertz and above, and I'm sure that they're looking at things that are even faster than that.

**Chris Gammell:** I like the sound of that.

**Hank Zumbelan:** Yeah, I have a hard time just getting my head around 17 gigahertz to start with. Yeah. You know, that's where everybody's moving up to. That's where the migration is going that direction. So, you know, if that's where people are going, that's where the people who's like analog that are supplying the parts to make the next generation thing have to be looking at that and then the next step beyond that as well.

**Dave Jones:** Yeah.

**Hank Zumbelan:** So, again, it has more to do with evolution than revolution.

**Dave Jones:** Yeah. Well, Mike, what about you? You got any other questions for Hank? I think I'm cleaned out. Yeah. This has been – this is like a short course in analog design. That's exactly what I hope for and more. Absolutely. So, Hank, how are we going to find out when you actually are on the road so we can, you know, bum rush you with Amp Hour listeners that want to, you know, ask you questions and hear your seminars?

**Hank Zumbelan:** Well, I'll tell you what. Next time we have a seminar thing coming up, I'll send you through the Amp Hour thing a notification and you can put it on the notes to people all over the place. And we welcome everybody to show up.

**Dave Jones:** Terrific. That's awesome. First come, first serve, folks. And you know what? I'm hearing about it first from Hank, so I'm number one. Well, Hank, thank you so much.

**Hank Zumbelan:** Yeah, like I said earlier, it's unfortunate I don't get to do that nearly as much as I used to, but, you know, it does still happen.

**Dave Jones:** Yeah. Well, if there's anyone we can talk to to try and get you out on the road more, let us know and we'll be annoying wherever we need to be in order to get you out on the road.

**Hank Zumbelan:** Okay. Well, we'll take that offline because I don't want to put any kind of names out here right now because it may not be appreciated, you know.

**Dave Jones:** And here's the CEO's cell phone number. Okay, great. Well, Hank, thank you so much for being on the show. I really appreciate it. Where can people find your future writings as well? I mean, is it mostly on the analog site?

**Hank Zumbelan:** Mostly on the analog site. I'm actually completing a couple of more articles in a series that I've been doing on phase responsive filters that will be on analog dialogue, whatever the turnaround time is to get into there. I'll probably have the final drafts into them within the next two to three weeks. Right. And then, you know, however long it takes to get everything laid out, drawn up, and scheduled into their system.

**Dave Jones:** Yeah. And that's a great reference as well. If people don't know, that's the newsletter that Analog Devices sends out, and it's very, very valuable. So I highly recommend that.

**Hank Zumbelan:** Anybody who doesn't know about that should look into it, and there's a lot of good information in there. Definitely. They're all archived, so you can actually go back and take a look at stuff that's been there before. It's not completely devoid of marketing, but it tends to be much more technical. And there's a lot of good articles in there. Even I've learned stuff out of there. So, you know, it's like a shark has to keep swimming or he drowns. You know, you've got to keep looking at this stuff all the time, or you just become out of date.

**Dave Jones:** Yep. Got to keep building outboard DACs that have seven pole filters on them. That's how you keep sharp, people. Hey, why not? Yeah, it's awesome.

**Hank Zumbelan:** Nothing succeeds like excess, you know?

**Dave Jones:** Exactly. I like it. Well, Hank, thanks again. And Mike, thanks for jumping in for Dave as well. Yeah, thanks for having me. It was great to talk to you, Hank.

**Hank Zumbelan:** Yeah, this was good. I hope some people found some useful stuff in it. And, you know, if anybody needs to get a hold of me, it's Hank.Zambolin at Analog.com. I welcome people to send me stuff. I may regret having said that, but, you know.

**Dave Jones:** I'm sure they'll be respectful. They always have been in the past.

**Hank Zumbelan:** Yeah, so, you know, if there's something I can do to help people out on individual things, that's what I do nowadays. So, you know, have at it.

**Dave Jones:** Awesome. All right, thanks again, Hank. We'll talk to you soon.

**Hank Zumbelan:** Okay, thanks a lot. Bye.

**Speaker ?:** Bye. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
