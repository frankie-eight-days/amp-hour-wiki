---
episode: 297
title: An Interview with Jake Baker
url: https://theamphour.com/297-an-interview-with-jake-baker/
---

**Jake Baker:** This is The Amp Hour Podcast. Recorded May 4th, 2016. Episode 297. An interview with Jake Baker.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Jake Baker:** And I'm Chris Gammell of Contextual Electronics. And I'm Jake Baker. Welcome, Jake. That's a heck of a title you got there, Jake Baker. That's it. We have intrigue and mystery. So, Jake, what is your main profession?

**Chris Gammell:** So, I'm a professor here in the U.S., and I've been a professor at University of Nevada, Las Vegas, where I am right now, University of Idaho, and Boise State University.

**Dave Jones:** Awesome. Awesome. Why Las Vegas? Is that where you grew up? Is that other things brought you to Las Vegas? It just seems like it's in the middle of nowhere.

**Chris Gammell:** I have needs.

**Speaker ?:** Right.

**Chris Gammell:** No. I went to high school here, and when I finished high school, I had one option, and that was to go to UNLV. And then after I'd been working for 27 years, I guess, my kids are grown. I wanted to go back and give back to my alma mater. So, I was going to come back for a sabbatical. They offered me a job instead, and here I am.

**Jake Baker:** Well, that's awesome. And so, we should get to the meaty part. What is it that you teach? This is the part that I'm very—I mean, professors are interesting. I think the stuff you teach is even more interesting, though.

**Chris Gammell:** I teach basically chip design, and I'm a little bit different in my courses in that I also have courses in how to design, like memory circuits, which is a topic, as far as I know, not really taught at the university. So, I've got classes in memory circuits, mixed signal design, advanced analog, analog, and digital IC design, but more from a physical point of view.

**Jake Baker:** So, it sounds like all of this stuff that we pretend to know what we're talking about all the time, Jake actually knows what he's talking about here. Talked about. Excellent. Yeah. That's crazy.

**Dave Jones:** Is there much call for chip design these days? Is it booming? Is it— Busting? You know, busting. What's going on? What's the vibe?

**Jake Baker:** We do see a lot of news stories about, you know, fabs closing down, or, you know, like Intel just closed that thing the way we talked about it last week, and other, you know, chip design going over to Asia as well. Yeah, what is the main feeling there?

**Chris Gammell:** So, it's a little bit complicated question to answer. Of course, that's why I asked it. There's still lots of chip jobs. There's a lot of the jobs have moved overseas to Taiwan and to China. There's still big companies here, Qualcomm, Broadcom, Intel, Micron, that are doing chip design that hire people with semiconductor skills. The big difference between now and, say, 20-plus years ago is that nowadays, it's really hard to do a chip design from scratch. Everything is evolving, and so it's not as glamorous as it used to be.

**Jake Baker:** Right. Well, I'd like to hear about the glamorous old days, if you don't mind taking us back a bit.

**Dave Jones:** Well, you lean over a bench, and you've got these big vellum fumes, and you've got a magnifying glass. Exacto knife, Ben, yeah.

**Chris Gammell:** Yeah, exactly. Well, you know, what used to be that you would attempt new products, you know, if you had an idea, the company might back you, and you would do a brand-new chip design. And, you know, nowadays, the marketers and the companies have gotten so risk-averse that it's really difficult to do anything that's totally new. Everything's just small baby steps or changes from existing products. And so part of the reason is nowadays the reticles, the masks that are used to make the chips are just so expensive that, you know, it could sink a company if the company invests in something and it doesn't end up making a product.

**Jake Baker:** Could you give us a scale reference for that? Like what's a reticle set these days?

**Chris Gammell:** Millions, tens of millions, if not more. Tens of millions. Yeah, for the little ones.

**Dave Jones:** Just for a small, like, analog chip or something?

**Chris Gammell:** Oh, no, no. See, there's companies like On Semiconductor is a great example, and there's others that have a business model of not advancing to the newer technologies, but rather providing technologies for medical and automotive and, you know, parts that don't need to have billions of transistors.

**Jake Baker:** Yep. Right. Yeah, like stay on that old node, use the old equipment, stay on the 8-inch wafer instead of 12-inch, all that kind of stuff.

**Dave Jones:** Well, you could argue that there's greater margin potentially in niche stuff like that.

**Chris Gammell:** Yeah, because, yeah, they need to fab it, and, you know, they can charge a little bit more. Mm-hmm. They can focus on increasing yield, which increases profits, and if they have a piece of equipment that goes down, it's easy to replace, you know, find some surplus equipment from one of the big guys. Right.

**Jake Baker:** Not always, though. I recall stories of them buying, you know, $10,000 desktop computers because they had to match exactly in fabs. I've heard those stories before, too. No. Yeah.

**Chris Gammell:** The copy exact stuff. Yeah, one of my, the guys I know of, my friend that's in a fab, he says there's, the golden rule in fabs is there's no trivial process change, nothing. Even if you get a different cable, you've got to get the same one.

**Jake Baker:** Yep, exactly. Exactly. Right, and people take advantage, sadly.

**Chris Gammell:** Oh, yeah, yeah, yeah.

**Jake Baker:** So you mentioned the golden days 20 years ago. Could you give us an idea also on, you know, Dave was asking about analog versus mixed signal.

**Jake Baker:** Mm-hmm.

**Jake Baker:** But you also mentioned, like, the, you know, the billions of transistor type stuff. Where did that all fall back then? I mean, was it like you were, were you doing entirely new architectures as well, or is it more subsystems within a larger chip?

**Chris Gammell:** So, for example, in DRAM memory design in the 90s, you might have two design engineers that design the entire chip. Oh, wow. And the big cost was in the process development. So it was done at the same time as the designs. And so these chips would sell hundreds of millions, if not billions of dollars worth. And so the engineers were, you know, I say glamour, but, I mean, they were making ridiculous amounts of money. And then as things matured, companies fell out. We went through hard times. You know.

**Jake Baker:** There was the price-fixing scandals. Yeah, yeah, exactly.

**Chris Gammell:** There's all kinds of things. And then, you know, what you could do is, what you could do in designs and your responsibility tended to be a smaller and smaller part of the project.

**Jake Baker:** I see. So it just became more of a business, basically. Like, less of a design, R&D-focused organization, more of an accounting-driven type thing?

**Chris Gammell:** To some extent. And the other extent, you know, frankly, the personnel costs got to be almost negligible compared to the other costs. And so from the point of view of someone running a billion-dollar company, it's easier to throw people at something. So if somebody leaves, there's still people around, you know, to pick up the slack.

**Jake Baker:** Yeah, that makes sense. Well, we could try to go through some of your patents if only we had the time. What? I don't know if we've had someone with this many patents on their show. What is it, like 180 now? No, it's 142. 142, sorry. Sorry. I didn't have the page right up there.

**Dave Jones:** And how many of those actually get granted? Like, what sort of percentage of them?

**Chris Gammell:** Well, okay, so this is interesting because when you look at the number of patents, you go, wow, that's a lot of patents. But in reality, it's not as many as it appears. And here's why. When, say, I do a patent on some double data rate DRAM, which I did in the 90s, and there's 20 claims of the patent. And the Patent and Trademark Office will issue 10 of the claims. Right. But what will happen is the attorneys will turn around and take the other 10 claims that weren't issued, and they'll file a continuation, which has the same title as the previous patent. But they'll change the spec or the claims in such a way to get around the objections of the Patent and Trademark Office. And they keep doing that. And if you look at the titles, yeah, it runs up the numbers. So I have 142, but maybe 50 of them are different ideas. Right. Got it. So it looks more impressive than it really is.

**Dave Jones:** Is this a driver? Like, is this a... Is this something that you do for the university? Is this something that they require that you keep churning out patents like this? Is it sort of expected?

**Chris Gammell:** No. Well, they expect it. If they like it, if they're the assignee, they're the ones that own the patents. But almost all of my patents are as a result of consulting work I did in industry. Oh, okay. Right. So the university, I don't think... So they're yours? No, no, no, no. They're the companies. Oh, Dave, Dave. Easy there, buddy. It would be nice. No, they're the companies. They're the companies.

**Dave Jones:** Right. So the companies pay for them. Because you're probably... Like, you couldn't, as an individual, you couldn't afford to just patent everything like this.

**Chris Gammell:** Well, then...

**Jake Baker:** You have to pay for all the development too, right? I mean, that's...

**Chris Gammell:** Yeah, well, yeah. Sometimes people will file patents without doing any development and showing that the concept works. The thing is, with a patent, especially in semiconductors, it's only worth something if someone will license it from you. And a lot of times, then you have to go back and get into litigation or, you know, go after a company and, yeah.

**Dave Jones:** Has that ever happened? Have you ever had patent wars? Have you ever been involved in them?

**Chris Gammell:** Well, I mean, I've done lots of expert witness work. So, yes. I haven't done any with regard to my patents. Some of... A lot of my patents are in double data rate stuff. And so, when those... When DDR was coming on from SD RAMs in the late 90s, I was still working at Micron, so I wouldn't have been involved other than I'd been deposed as a fact witness. The later work is done in resistive memories, which are like the 3D cross-point switch stuff that Intel and Micron are talking about in others. And there's really not a lot of players in that. And I did the work for the people that did the product, so I don't anticipate there being anything there either.

**Jake Baker:** That is interesting, too, that it seems like, I mean, just the overall number of players is going down, too, right? As these companies get bigger and bigger, there's just fewer... I mean, they're obviously... There is the bigger piece. You know, there are bigger companies with more lawyers, but there's a lot fewer of them. They probably trade patents as much as litigate type of stuff.

**Chris Gammell:** Yeah, what happens now is, especially in downturns or when a company goes out of business, they'll go to a venture capital company with their patent portfolio and say, save us. And in order for the VC firm to make money, they take the patents and then they'll go after, sometimes legitimately, sometimes not, they'll go after people that are making stuff.

**Jake Baker:** So, are we going to talk about Rambus now? Is that what we're going to talk about?

**Chris Gammell:** Well, yeah, I haven't kept up on them since the 90s.

**Jake Baker:** The only reason they're still in the foreground of my mind is that I still recall with hatred in my heart that I had this top-of-the-line computer with RD RAM in it, whatever that stood for, I guess Rambus. Rambus, yeah. And I remember all my friends were buying this cheap DDR memory and I was stuck with like $500 memory modules and I'm like, I can never update this computer. It was basically obsolete. It was cheaper for me to just buy a new computer. It was crazy. Oh, yeah.

**Dave Jones:** I do recall it, but I don't recall the technical details. Why was it so much more expensive than Didier?

**Jake Baker:** Because Rambus. Yeah.

**Dave Jones:** Why? Because they charged a premium because they had patents on it or what? What was the... Why was it more expensive?

**Chris Gammell:** I think that's part of it. They put the toll on any of the memory makers that were making the parts.

**Dave Jones:** Right.

**Chris Gammell:** And at the time, the parts were not synchronous and so there was a delay between requesting something and getting it and so it really slowed down the performance and in Rambus everything was very synchronous and quick and so the performance initially was better.

**Jake Baker:** Ah, I see. Okay. And then like the bottom-up type, they started fixing it in other ways basically. That's kind of the idea. Yeah.

**Chris Gammell:** Yeah. Went to a wider bus with the DDR and increased the latency, the number of clock cycles to get something out of the part so that once you got over that, you'd get stuff out really fast and a bunch of other things that weren't common in the time before that.

**Jake Baker:** So how did you get into RAM in the first place? I mean, how did you get into this side of the design field? Oh.

**Chris Gammell:** So I, in the 80s, during Reagan's Star Wars program, the Strategic Defense Initiative. Yes.

**Dave Jones:** Oh, yeah. Chris, can we insert sound of a flush in toilet? Yeah, right, right.

**Jake Baker:** Laser blaster sounds or something? No, no, no. Flush in toilet where all the money? Or do you mean like Reagan clips or something?

**Chris Gammell:** Well, it's good for people working.

**Speaker ?:** Oh, yeah, I know.

**Chris Gammell:** Anyway, I got hired to do design for instrumentation at the Nevada test site. So I'd go out there for the nuclear bomb blasts and all that. And that lasted, I worked there from 85 to the early 90s. And then there was a moratorium on nuclear weapons testing. And I had been teaching part-time at UNLV. And I really liked it. And I decided I'd go back to school. And anyway, long story short, I got a job in Boise, Idaho. And there was the company Micron was there. And part of what they encouraged me to do is build relationships with Micron. And that's what I did. And that's how I got into all the RAM stuff.

**Dave Jones:** Got it. That's great. How does DDR work for those who aren't familiar with the concept? And what's it and the differences between DDR1, 2, 3, all that sort of jazz?

**Chris Gammell:** Yep. So the initial DRAMs, basically you had what's called a RAS, a row address strobe, which you also have in the DDR parts. But it's more of a control signal. It doesn't do the same thing. And you have a CAS, column address strobe. In the older parts, you would multiplex the addressing into the parts. So you'd strobe in a row address. And then you'd strobe in a column address. And then you would wait a while for the part to produce the data on the output. And then you'd read it in.

**Dave Jones:** Why did you have to wait a while?

**Chris Gammell:** Well, because it takes time to open the row that you select. And then it takes time to sense what the value of the data is. And then it takes time, once it's sensed, to feed it from the array. Because these are big chips to the output of the chip. And then there's the time of flight from the chip to the memory controller.

**Dave Jones:** Right. So it's a propagation delay thing. It's not. Yeah. Right. Just because the silicon is so physically large.

**Chris Gammell:** Yeah. And then when they started doing things with synchronous DRAMs, what they said instead was that we're going to send in data with this clock, this CLK clock. We're going to do everything on the rising and the falling. Well, for the commands are on the rising. But the data is going to come out on both the rising and the falling edge. And then because the delays are so long in doing each one of these operations, what we're going to do is we're going to add this latency or delay of a number of clock cycles. So in the earlier DDR parts like DDR1, there might have been one or two clock cycles between issuing a command and then getting a chunk of data out. And then, but after that two clock cycle delay, the pipeline was filled. You just get the data out as fast as possible. Well, all these, and it's interesting to note that in all of the DRAMs, DDR1, synchronous, extended data out, all the older ones, DDR4, the memory, the DRAM memory cell, sense amp, column decoders, all that organization is exactly the same. I mean, the process technology has changed. All they've done is they've changed the wrapper around the memory. And so you would get like 20 clock cycles of latency. And now you can get stuff out at a gigabit because you ensure that any one hop is less than say a nanosecond.

**Jake Baker:** Yeah. That's crazy. Yeah. But yeah, yeah, you're right. Everything else is, I remember sense amp stuff was very basic for, I used to work at Samsung on memory stuff. And we learned about the sense amp first and they're like, yeah, this is pretty much pretty simple. You just go with it, you know?

**Chris Gammell:** Yeah. It's just a two inverters back to back. And then everything is in the process to try to optimize it, reduce the offset and improve the yield. So that improves the signal to noise ratio.

**Jake Baker:** Wow. And the yield increases the money coming in.

**Chris Gammell:** Yeah, exactly.

**Jake Baker:** More jelly beans.

**Dave Jones:** So all the smart stuff is in the process, right? It's not necessarily in the, you know, the schematic implementation of how you implement an architecture.

**Chris Gammell:** Well, going to the other extreme. Now, if you look at like Flash and DRAM to a certain extent nowadays, they do so many things with like trying to wear levels so you don't wear out the cells. So the software part is huge. In DRAM, it's all about speed. And so the difficulty comes in. How do you, I mean, they have all these algorithms for like measuring the distance the DRAM is from a controller so you can optimize the timing window and all these other things they do that maximize the performance.

**Jake Baker:** Yeah.

**Chris Gammell:** Crazy.

**Jake Baker:** That's interesting too, because it kind of, I remember it was such a, maybe it's out of just out of my purview these days, but like it was such a big deal for computers and everything, you know, like buying memory modules and it feels like everybody's kind of moved on to tablets and laptops and stuff like that. So it's almost like it's just built in now. You know what I mean? It's just, you hope for the best stuff and it's built in. Whereas it used to be like people optimizing memory sticks on their desktop type stuff. So, and I'm sure gamers still do that, but.

**Chris Gammell:** Well, now they're trying to go to the hybrid memory cube for the DRAM where they're putting through silicon vias through the chips and then stacking them and then putting the cubes around the memory controller. So.

**Dave Jones:** That's crazy.

**Chris Gammell:** Yeah. Little sugar cubes.

**Jake Baker:** So aside from DRAM, what are some of the other types of circuits you've worked on in the past?

**Chris Gammell:** Uh, well, when I did the star Wars stuff, I did all kinds of high voltage and cameras and all this for recording the, the bombs going off. Um, but consumer electronics, I've worked on, uh, like CMOS imagers, for example. Uh, I, uh, micron acquired a company called photo bit, which was out of Caltech in the, uh, uh, when was that late nineties? And I went down there and I helped transition the products into the micron fabs. And the idea there was to use the old DRAM processes to run the CMOS imagers. Cause they could be larger for obvious reasons, you know, to collect light. Um, and then I've worked on flash. I've done quite a bit of flash memory. And then I've done a quite a bit of, uh, resistive memory development, which is, uh, everybody says it's going to be the new flash replacement and, uh, hard disks and mass storage because they can stack it. And, uh.

**Jake Baker:** Could you explain what that is a little bit more? Yeah, please. That's not like the, uh, what's the fourth element? It's supposed to be the, uh. The Memristor? Yeah, it's not that, right?

**Chris Gammell:** Well, uh, you know, some would argue you could say it is or whatever, but, uh, I worked on it about 10 years before I heard the term Memristor.

**Jake Baker:** So someone with clever branding, uh, know-how got in there.

**Chris Gammell:** Well, I think the, the guy is a professor at Berkeley. He coined that term, uh, uh, what's his name? Uh, Leon Chua, uh, in the early seventies or sometime around there. Anyway, no one realized he'd already discussed this potential element, just didn't have, he hadn't fabricated it. Anyway, the, uh, resistive memory is, uh, in simple terms, it's just a memory that you sense the resistance changing. So a, uh, program state might be a small resistance and a race state would be a large resistance.

**Jake Baker:** Oh, interesting. Yes. So is it like lots of instrumentation amps or how is it actually measured then? Or is it just, uh, current flow changes?

**Chris Gammell:** Uh, so imagine a screen just like in your window, a window screen and that the intersection of every, um, intersection of the horizontal and vertical lines is a Memristor.

**Jake Baker:** Uh-huh.

**Chris Gammell:** And then they put a material in there that, uh, behaves like a diode. So you have a diode in series with a variable resistor. Uh, and then depending on how you apply potentials to the elements of the screen and the rows would be the horizontal wires and the columns would be the vertical wires. Uh-huh. You can then select a row of memory and then apply a, uh, uh, res, you know, a small voltage below the diode turn on to sense how much current flows. And then thus what is in the, uh, what's the state of the memory cell? Huh.

**Jake Baker:** Hmm. I thought you were going to go into like the, uh, the infinite array of one-ohm resistors or something there. I, I started to have flashbacks. Sorry. It's always, it's always a threat with professors, you know.

**Chris Gammell:** I'm not a very theoretical dude. Oh, man, that's funny.

**Jake Baker:** Yeah, no, that's, that's really interesting. And so this is actually coming on, I, I've never heard of this stuff before, but that doesn't mean much. Uh, what, what, where, um, this is kind of starting to come online with, uh, larger memory makers or what?

**Chris Gammell:** Yeah. Intel and Micron, uh, a while back, a month or two just announced a press release that they were going to start releasing samples and, and, uh, uh, you know, it's going to be, I think everybody in the industry feels that this is going to replace flash memory. Um, when it'll actually, you'll start seeing it in your laptops or computers or servers or whatever, I have no idea because they were talking about this, like I said, back in the mid two thousands. And, um, I worked on it for a very long time. Um, what is the advantage of it?

**Dave Jones:** Why is it going to replace flash? What is the, is it faster? Is it cheaper? Is it denser? Is it all of the above?

**Chris Gammell:** All of them. All of them.

**Jake Baker:** It's, uh, all right. That's good.

**Chris Gammell:** So the problem with flash is that, uh, I don't know how well, uh, you know it or the listeners know it, but there's a tunnel oxide and you have to apply a large voltage to the flash cell to get tunneling through this thin oxide and it damages the oxide. And then if there's physical limitations on how, because of the material properties, how thin you can make it. So it limits the size of the, uh, memory cell. And back in 2008 or 2007, 2008, I was working on 35 nanometer flash. I would guess nowadays they're probably in the like 10 nanometer flash range, which is just, yeah, blows my mind.

**Jake Baker:** Because usually they're, they're chasing leading, uh, leading process stuff. And yeah.

**Chris Gammell:** Yeah.

**Jake Baker:** So, yeah. Yeah.

**Dave Jones:** So, uh, how does the damage happen? Does it happen on every right or is it more a bit random? Is it quantumy? Is it what? Quantumy. That's a new word.

**Jake Baker:** Shush. Dude, it's tunneling, Dave. Come on, man. It's like a worm. Like electro worms.

**Chris Gammell:** Yeah. Uh, my understanding is that when you apply the high voltage, it damages the materials because you have the carriers, say electrons tunneling through onto a floating gate. And when it, the carriers tunnel through, they can do damage as they're moving through the materials.

**Dave Jones:** So, so it's every right. Yeah. Every right. Does a small bit of damage. I thought that the, that the scale is already so small that if you did damage writing every single time, it wouldn't last millions, it'd last. These are small gates, Dave.

**Chris Gammell:** Yeah, it does. It, it, the older flash, they had the spec of, you could write to it like 10,000 times. I don't know what the exact spec is now, probably hundreds or maybe a thousand if we're lucky. Um, but yeah, it's funny because I mentioned before we started recording that I just installed a solid state drive on my laptop. And one of the things that I, I mentally did after I installed that was turned off my disc defrag, defragmenter. So that would go in and readjust anything, you know? Right.

**Jake Baker:** Yeah. It's like needless, needless reshuffling. It's like, I can't afford that.

**Chris Gammell:** No, it'll wear it out faster. Right.

**Jake Baker:** Right. Right. Yep. It's weird thinking about a solid state drives like tennis shoes now. Yeah, exactly. Yeah. Well, Dave's had that problem recently, right? Right, Dave? You've had, uh, you've had some bad drives.

**Dave Jones:** No, it turned out to be the cable.

**Jake Baker:** Oh, well, there you go too. Yep.

**Speaker ?:** Yep.

**Jake Baker:** Yep.

**Dave Jones:** Cable was dodgy. Everyone, like I put it on Twitter and everyone said, oh, yes, solid state drives suck. It's like, well, it's first time I've heard of it. And, um, they're saying, oh, all these brands suck. And no, you've got to get Intel, blah, blah, blah. And, and no, it turned out of the cable. There was nothing wrong with my drive. Oh. You know?

**Chris Gammell:** So. Yeah. So I was mentioning that about the time, you know, I don't know when the resistive memory is coming into market. And I've been working on 10 years. One of the other products that I worked on back early in the nineties before LCD displays came into is called a field emitting display. And it was going to be a CRT replacement. I don't know if you've ever whacked open a, uh, like a viewfinder in an older camcorder and you see this like three.

**Dave Jones:** Yes, I have.

**Chris Gammell:** Yeah. Three inch little CRT, right?

**Dave Jones:** They're great. They're so sexy.

**Chris Gammell:** Yeah. So anyway, we worked on that and we got, this is like, this is when I learned, I was like really excited. I designed the, the, the field emitting driver. It was on a team. We were working and we demoed the product and all this. And, uh, I was thinking, man, we're going to just, oh, this is going to be great. We're going to replace all these. You know, this was before LCDs were blowing up the market. Right. And it turns out that we could get like 99% yield on the pixels in the array, but that 1% your eye could pick up. And that's what I learned. You need, uh, having ideas and turning them into product is really, really challenging. Yeah.

**Dave Jones:** I can remember back when, you know, LCDs were starting to take off and it was actually normal and expected to have dead pixels on your brand new laptop. You know? I would actually say, you know, 10 dead pixels, normal. You cannot find that under warranty nor, and people like, oh yeah, okay. There's a few dead pixels. And you just, you know, your eye would pick out one dead pixel. It'd be so obvious, you know? Yeah. Yeah. Yeah. And that was normal. People treated that as, you know, eh, okay.

**Jake Baker:** So what happened to the, uh, field. So field emitting displays are different than CRTs or not. Are they like still reversed, uh, like electron shot at a phosphor type thing? Yeah.

**Chris Gammell:** They're, that's exactly what they are. There's a, uh, we did it in like five micron and moss. So it was real old technology. Again, with the idea that we keep the costs low by using older equipment and we would etch a, uh, tip, a field emitting trip, uh, tip down into the silicon wafer. And then you would put a layer of glass and phosphor on top with a metal grid right above the tip and it would extract the electrons off the tip and hit the phosphor. And that's how you'd get the red, green, and blue.

**Jake Baker:** Wow. Sweet. So, but that's, so it was like basically a miniaturization of CRT stuff, huh?

**Chris Gammell:** Yeah. Miniaturization, making it flat and using a silicon.

**Jake Baker:** Wow. That's interesting. Well, how was the, how did the, is it why? So why didn't it take off just because of power and cost or what?

**Chris Gammell:** No, no. It was, uh, we just couldn't get the yield up to a level where it would be manufactured. It'd be like, we would get like 99% of the pixels working and they'd last indefinitely, but there's always be dead pixels in there. I see. And it was, uh, you know, the size of those displays in the camcorders were relatively small. They're like VGA size. And so having a few dead pixels really, uh, yeah, especially when they die in their bright spots, if they died for black, it might be less noticeable.

**Jake Baker:** Oh, interesting. Wow. Wow. That's really, yeah, that's, that's, that's really cool though. That, um, huh. It's just crazy how that, that kind of stuff, it's a viable, mostly viable technology and yet it just got passed by because of, you know, an alternative technology. Yeah. It's crazy. Yeah.

**Dave Jones:** And you couldn't quite perfect it.

**Chris Gammell:** Yeah.

**Dave Jones:** There's probably a ton of tech out there like that, that never made it because it was all my, that last hurdle.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, they just couldn't get over it.

**Chris Gammell:** Yeah. Hmm. Yeah. It's lessons learned about product development. And I think nowadays that's one of the reasons they're so risk averse and trying new things. Right.

**Jake Baker:** Yep. Yep. Yeah. Just more competition and cost to start up and everything too. Yeah. Yeah. So what is the, what is the, so are you still designing chips? Is that, I mean, I know you're teaching and we love, we're going to get into that in a minute here, but, um, are you still designing and consulting for design?

**Chris Gammell:** Um, I'm still designing chips. I'm doing a lot of, uh, work with the military designing like sensing chips. Um, I'm not designing, uh, in the newer technologies just because keeping the CAD tools up and running is painful. Oh yeah. And I have to do a lot of that myself. And so I tend to steer towards the older technologies. Um, I do a lot of, uh, consulting with expert witness work now. Um, I haven't, I, I'm trying to, uh, focus on some, and maybe we'll talk about this later, but I really have a passion for online education and, uh, I'm working on, uh, university courses that will be online that the students can take that are, uh, that they like.

**Dave Jones:** Awesome. On, on what, uh, platform are you going to release those?

**Chris Gammell:** What I'm going to do, uh, so this is still in a state of flux, but, um, I want to have, uh, I want to do like basic circuits one and circuits two, and I want to have it so that it's, uh, you know, web-based where, uh, the students will have like mini lectures right now. I'm thinking like 15 minute lectures over topics that all do recorded examples. Then they'll have like an online quiz that they take and then periodically some, um, online, uh, online tests. And then, uh, I want to have, uh, I want it to be clear and I want it to be no hocus pocus, you know, cause I get students that come in and they just, you know, they don't understand simple things like DBs and why a log log plot is used and all these things that are just not difficult concepts or an op amp. I, I, students come in there like, oh, I took circuits one and circuits two and an op amp's magic. And then I spend 15 minutes and I go, this is the way it works. And they're going, what? Is that easy? Yeah. So.

**Dave Jones:** So is this going to be your own developed web platform or you're going to use like a existing technology web thing to like share it and do all that sort of stuff?

**Chris Gammell:** Well, right now I've got a bunch of videos on, uh, on my website, the CMOS EDU website. Uh, the university here, UNLV has indicated they want to work with me. So they're going to give me a, uh, what is it? PHP, uh, programmer to help develop. Oh, okay. Right. So yeah.

**Dave Jones:** So it's going to be a custom thing.

**Chris Gammell:** Right. Yeah. Yeah. Got it. And I'm going to have like different, in order that, you know, two students aren't sitting side by side and working together, I'll just have some randomized problems. So they get different problems and a bunch of other things. But I think it, I have this vision. We'll see how it goes.

**Jake Baker:** Got it. So, uh, yeah. So you said you are still designing though. Uh, so, uh, what, what kind of nodes are you on then? I mean, so I definitely, I think we've talked to someone else about that with like the process kits, like you mentioned the, the super expensive keeping up with cadence and for like the 20 nanometer stuff or whatever's the newest. What, what node, what nodes are you designing on?

**Chris Gammell:** Right now, the smallest we're doing is old 130 nanometer SIGI silicon germanium, uh, because, uh, we can do a multi-project wafer through the MOSIS service, uh, which is, uh, where everybody puts their designs on one wafer and fabs to keep the cost down. So, uh, and it's...

**Jake Baker:** Can you tell us more about that? We've actually mentioned that on here before we were, we've, we've talked about it before, but never really actually going through with it. So, okay.

**Dave Jones:** How much does it cost? Tell us the price, son. Yeah.

**Chris Gammell:** Um, well, okay. So funny you mentioned that. Um, so a little history about, uh, the MOSIS service. It's M-O-S-I-S, which stands for Metal Oxide Semiconductor Implementation Service. And they started in like 1981, I believe. And they're out of USC's, uh, Information Sciences Institute. And they used to be funded by DARPA. Now they're self-sufficient and they're self-sufficient. And what they do to universities that want to fabricate, like me, is if you're teaching how to do chip design in your class, they give you free fabrication support for that class.

**Dave Jones:** Nice. Oh, wow.

**Chris Gammell:** Today, I received, they give you five chips and they package them in a dip 40, uh, for student projects. And they're great for like lab stuff, you know, doing, uh, inverters or some ALU or an op amp or measure resistance and all that. But I just got the, about 10 chips or 10 projects in the mail today for my students from last semester. Now, if you do a, if you have funded research, then they charge you. And it's like for a 2.5 millimeter by 2.5 millimeter and like half micron older technology, it's like $6,000. For a single chip. Well, they give you 40 dice. Oh, that's not bad.

**Dave Jones:** So do they just give you the dice or do they package them for you if they want?

**Chris Gammell:** If you want package, you have to pay extra. Um, and, uh, we actually just over the Christmas break, we, we have two wire bonders and we wanted to develop wire bonding to the printed circuit boards here so that we could, uh, nice. Yeah. Keep things down. Yeah. Flexible.

**Dave Jones:** I was going to say, you're, most people would choose the, uh, dip option or any package option, just, you know, anything but dice. Thank you. Yeah. Yeah.

**Jake Baker:** I don't know though. Cause then you start adding, I mean, dips are not exactly optimal for adding in inductance and capacitance. I mean, I guess you can account for them.

**Dave Jones:** Who cares? I mean, you know, wire bonding, what are, you know? Yeah. Yeah. Sure. Your average person doesn't have wire bonding experience or the machine to do it or.

**Chris Gammell:** Yeah. We, uh, have like test structures. And so one of the big reasons we do the wire bonding to the printed circuit board is so we can just rip off the wire bonds and wire bond over a new test structure to do measurements.

**Jake Baker:** Yeah. Nice.

**Chris Gammell:** So it makes it easy. Yeah.

**Jake Baker:** More swappable versus, yeah. If you, if you put it in the chip, the packaging, then you cannot get it all the tags you're talking about.

**Chris Gammell:** Yeah. I mean, yeah. If you have like a avalanche photo diode in the middle of the die and you have other circuitry around, if you bond out the other circuitry, you'll never have access to the APD in the middle. So this way you can do all kinds of testing.

**Jake Baker:** You see, you see, Dave.

**Jake Baker:** No, that's cool.

**Dave Jones:** Can Joe blogs in their garage, who's willing to fork out six grand or whatever, six or 10 grand or something, can they, how easy is it to actually design your own chip? Are the tools free?

**Jake Baker:** Like to engage you in Dave or you mean the actual, the design process? You mean to engage Moses or to make the design?

**Dave Jones:** Well, both, you know, A, is it possible? And B, you know, how much, like, what are the tools you use to do it?

**Chris Gammell:** So that's a good question. So if you try to do commercial tools, which if you're doing the real smaller designs, you have to use because the process design kits, the PDKs are only set up for the commercial tools. It's really expensive.

**Dave Jones:** As in the commercial tools, Cadence and whatnot.

**Chris Gammell:** Yeah, yeah. Now, having said that, Cadence has a program where they will sell you time on their server, which makes it much, much more reasonable for someone that, say, was interested in doing a startup. So you run the tools on their server. They charge you per hour and, you know, it makes it so you can do something. They set up the PDK for you. And so it's really reasonable. I have another, on my website, I have another set of tools, which are called Electric VLSI. Yeah. Yeah. They're really nice. And they are free. And they run on any platform, Unix or Mac or Windows.

**Jake Baker:** Yeah, the Java base, right?

**Chris Gammell:** Yeah, Java. And I've designed probably, I used to just use these for, use electric only for research and Cadence. I've probably designed, me and my students, I shouldn't say me, have designed more than 20 chips using the electric flow. So the problem with that, with that tool, I mean, it's a great tool. The issue is if you go to the smaller technologies, it doesn't have the PDK. Right. And so you're forced to go to Cadence. The other issue for me is someone that's trying to educate students and make them marketable and attractive to potential employers is they don't use electric in industry. They use Cadence. Of course.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** So I switched over a few years back to teaching Cadence only.

**Jake Baker:** Oh, really? Okay. Interesting. Yeah. That makes sense. Yeah, you can't. We had talked about electric in the past as well as, you know, when we found out about it, what was it, two, three years ago, Dave? I mean, not like it's only two, three years old, but we talked about it on the show two or three years ago. And I was a little confused when I first opened it up, but at least, you know, the fact that it exists is nice.

**Chris Gammell:** Um, yeah, I put some tutorials on the, uh, CMA CDU website, some videos and, uh, uh, some written tutorials. So they're actually used a lot by everybody around the world. I didn't realize, but I went to, uh, I got invited to give a talk in India a few years ago and I went with some colleagues and, um, this was at a time when there were quite a few companies moving into India. They were looking to hire people and I didn't realize how many people were using the videos and the tools to get this experience and had maintained and maintained, got employment, uh, until I visited.

**Jake Baker:** Wow. That's great. That's really good.

**Dave Jones:** And you are the author of two books, are you not? Yep. Tell us. There's two CMOS books.

**Chris Gammell:** One's called CMOS circuit design layout and simulation. The other CMOS mixed signal. I've got a third book with my students called DRAM circuit design. Um, that's in two editions. The mixed signal books done two editions and then the, uh, CMOS circuit design layout and simulation is done, uh, three slash four editions. Three slash four editions because the second edition was revised. So there's a revised second edition. All right. So, yeah.

**Dave Jones:** I see a Chinese edition of this CMOS circuit design. Yeah. Is that, um, is that something that the publisher did? There was a huge call for it in China to be translated into Chinese? Yeah. What?

**Chris Gammell:** Yeah. So the, I think the mixed signal and the, uh, CMOS circuit design book were translated into Chinese, both traditional and simplified. The, uh, what they did, they, the publisher had an agreement with a company in China. And then what the company in China did was they took the book and they split it into three books so that it would, uh, I guess sell. And that made the, the, the Chinese that were purchasing it really upset. They were like, why did you do this? It's why didn't you keep it as one book? And so anyway, yeah.

**Dave Jones:** Is, is, is it, what is, is yours the go-to book in circuit design? What are the go-to books?

**Chris Gammell:** Um, I think in digital, there's several popular books. Uh, one is, uh, Westy and Harris, uh, that's CMOS, VLSI and they're, uh, heavier and also, uh, Rabai has a digital integrated circuit book with, uh, uh, a couple other coauthors. And, uh, at least the Westy book is more geared towards, uh, real digital design. Like he has Verilog and VHDL. And in my book, I'm more geared towards the physical process. I don't want to teach Verilog. We have that taught in other classes. I want them to know what the layouts do and, you know, the difference between diffusion and depletion capacitance or strong inversion, weak inversion. So I'm a lot more physical, uh, other books in analog are like, uh, Gray and Meyer and Hearst Lewis, uh, the analysis and design, Rosavi's design of analog integrated circuits. There's several other good books. So I don't know if I would say, yeah, mine's one everybody goes to, but I'd like to think some people do.

**Dave Jones:** Excellent.

**Chris Gammell:** Yeah.

**Jake Baker:** We'll link to that. So then on, on your, um, on your page for this book too, you have, I mean, you link over to the electric stuff. Does that mean you use electric in the examples when you're talking about this thing? Or do you, do you have to tie in the software piece when you're teaching, when you're teaching the actual circuit design? Is that a really integral piece?

**Chris Gammell:** Um, yeah, I like nowadays, I like the students to be able to build stuff, to simulate things and to really understand what's going on. And so when I was using electric, we did, uh, me and my students did all of the examples from the book using electric. We did them from cadence and then we did them when LT spice where possible and, uh, some other tools.

**Jake Baker:** Cool. Yeah, that's good. So what, what are the usual tripping points then when, when, when a student comes to you and is ready to learn, uh, some of this, the mixed signal stuff? I mean, are you, are you designing all the way down at, I mean, you're designing individual transistors. Is that kind of the idea?

**Chris Gammell:** Yeah. So, yeah, go ahead. I was just going to say the, uh, so with basic circuits, like when they're learning analog, my pet peeve is you got to know RC circuits. And if they know second order circuits like RLC circuits, that's great. You need to know, you know, like step response, phase margin, gain margin, what a Bodie plot is, how to look at it and not cringe.

**Jake Baker:** I'm still working on that one.

**Chris Gammell:** And then for the mixed signal, uh, it's really, uh, and other people would argue with me about this, but I really feel the power of mixed signal design is the fact that it utilizes digital signal processing. And so having a very strong signals, uh, and systems background, uh, you know, and understanding what's happening, you know, in, from a signals and systems point of view and how you do the digital filtering, like in a Delta Sigma modulator, what's really happening there. Those fundamental circuits and signals and systems are really important.

**Jake Baker:** So in those kinds of designs, so say, so using that example, right? So say you're using, you know, like multi-tap filters and stuff like that, would that be like you would design, you would design a front end analog piece and then you would tell them to go code up the rest and generate, like, like, like you generate the multi-tap stuff or do you have to actually design that out and have each individual piece individually designed? So what level, what level is the whole design stack? I guess, because, you know, you talk about VLSI, you talk about these, uh, Verilog versus VHDL stuff, but how much is the tool doing it? How much is the student doing it?

**Chris Gammell:** So I don't, in my classes, I, maybe I briefly talk about Verilog. Uh, but like I said, they get in others when I, you know, like if you look at stocks and stock performance in the stock market and you can apply like a 30 day filter or 60 day filter or whatever, I want them to understand what's going on there because it's not that hard. Once you understand what the filter is, what its frequency response looks like, how to modify it to get a band pass or a high pass response, physically what's happening. Then we build circuits that utilize those things. And I don't do too much when I say digital signal process processing. A lot of times when people say that, or most times I think people think of multiply and accumulate, multiply and accumulate like the top, right? And that's not what I teach. I teach like taking the bilinear transfer function, implementing it digitally, take the bi-quad dratic transfer function, implementing, how do you implement those digitally? What's going on? How do you make a higher order filter using those things? How do you implement those in silicon using transistors, you know, and if you need adders or just delays or whatever. So it's a really low level hands-on kind of approach.

**Jake Baker:** So when you say, yeah, so when you mean digital signal processing, you mean making digital structures that are doing the processing on some kind of signal output versus using, yeah, multiple iterations in a, you know, a processing element.

**Chris Gammell:** Yeah. So when I say to the students, when we go through it and I say, oh, we're going to use decimation and I ask, how many of you have taken a DSP class? And they say, oh, half the class raised their hand. Okay. So what is decimation? And their answer is, you throw out K minus one samples. Yeah. You just throw out some samples. And I'm like, no, you're down sampling. Whenever you sample, what do you have to do? And they're like staring at me and like, you need an anti-aliasing filter. How do we implement that digitally before we decimate, before we, you know, it's kind of, oh, it all makes sense now. Right, right.

**Jake Baker:** Yeah. So it's like, you're, you're basically taking them, you're like a magic school busing them around the actual silicon then. Yeah.

**Chris Gammell:** I guess that's one way of looking at it. Yeah.

**Jake Baker:** That's crazy. Yeah. And so, I mean, so let's get back to kind of how the, you started the whole conversation too. I mean, what's the likelihood that, I mean, it's very important to understand this stuff. What's the likelihood that someone that goes to work at a chip design company will actually be implementing these kinds of structures at the, at the silicon level?

**Chris Gammell:** Well, it could be quite high if you have that arsenal of skill, right? There's places where you can use it. I can give you an example. I worked on flash memory, as I mentioned. And in flash memory, the way it's read is you precharge a bit line, which is the column line. And then if the flash memory cell is erased, it discharges the bit line. And if it's programmed, it doesn't discharge. And so you put a comparator there, Ed, or more than one comparator, and you look at, you know, what happens to the bit line. That's how a flash memory works. Well, I had this idea that, you know what, it would be better if I use this delta sigma process to hold the bit line constant and measure the current that was flowing. And I could actually, and I implemented it, and I implemented it with a counter, a simple digital filter. And I could actually plot the current that flows in the flash memory cell. And I was like, really excited. This is going to be, you know, a huge product. We're going to make lots of money with this. You know, this is going to revolutionize flash and all this. And, you know, it just, because I had that arsenal there that I knew, I was able to do these things. And so when I educate, it's, I'd like to think everybody, every educator thinks like this. You want to educate people because you don't know what the future presents them and what they'll need. You need, you want them to be armed with, uh...

**Jake Baker:** Yeah, given a toolbox.

**Chris Gammell:** Yeah, given a toolbox to solve stuff. You know, I can't tell you how much, how often around, and I'm sure you guys are in the same boat, you have something break around your home and you need to fix it. It's good to know how to fix it, right?

**Jake Baker:** Right, right. Yeah, exactly. Or even, I know, I think, I think a lot of it, so like, that sounds like a very pattern matching type of thing. You, you understand the application. You understand the tools that are in your toolbox. You then applied that, uh, a different tool to it, right? So the Delta Sigma, like you said. And, and then you could implement this, which is quite an innovation then too, right? I mean, that actually does bump you forward in terms of what, what you can do with it. So that's, that's really good.

**Chris Gammell:** Yeah, it was really exciting. I, uh... That's another example of, uh, learning about what actually makes into product.

**Dave Jones:** Yeah. Half of the art there is knowing which tool to use. Yep. Yes, definitely. You know, that's, yeah. That's the finer art.

**Jake Baker:** It's seeing it and recognizing it and then, and then pattern matching. I mean, that's definitely, that's, that's a huge piece. But I think, I think you're right. If you're, if you're super focused on just the tweaking stuff, like you said, a lot of the companies are these days, you know, it's more like, how can we get these incremental benefits versus how can we change the paradigm? How can we change, you know, how we're actually doing things? That's a lot scarier for a lot of companies, I think.

**Chris Gammell:** Well, yeah. And to their, you know, in their, from their point of view, it could break a lot of companies if they, you know, invest hundred million dollars in something and it doesn't work out.

**Jake Baker:** So... Right, right. Yeah, it might be easier to just kick the can down the road, make the process a little smaller. I think it'll be interesting as, as they continue to run out of room, right? I mean, like... Yep, yep. What, what, what happens then? Can you answer that question? What happens?

**Dave Jones:** Is Moore's Law's dead, first of all? Everyone's saying, yep, it's, it's basically gone, as we know it.

**Chris Gammell:** Well, I think from, you know, they, instead of increasing the area or reducing the size, they're doing what they're doing, they're going to start going to stacking the chips. It's just like a densely populated area once you run out of...

**Dave Jones:** So, but once you decide to do that, Moore's Law is dead. It, it doesn't apply anymore.

**Jake Baker:** No, then you go up, Dave.

**Dave Jones:** Yeah, but no, but it doesn't apply, because Moore's Law applies on a two-dimensional plane. It, it, it does not apply to three-dimensional stacking.

**Chris Gammell:** Yeah. Surely. Um, so, you know, I think the same way of what you're saying, but when you talk, say, in a memory, and you look at the size of a memory cell or the size of a transistor, whatever, and you say, okay, the pitch, which is the like distance between points is 2F. And then in the pitch in the other way is 2F. And so the size of the memory cell is 4F squared. And then they start stacking them and they go, look, I put four planes here. I've got a 1F squared memory cell. Look how I'm...

**Chris Gammell:** I'm...

**Dave Jones:** Yeah, yeah. It depends on how you look at it. Do you look at Moore's Law from a, just a, you know, a photographic, you know, process kind of thing of shrinking things down and doubling, or do you look at it as a macro thing? Okay. Memory's getting, you know, half the price every night and twice as much every, you know, nine months or every 18 months.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** And in that case, it can still hold, right? Because you just, just stack them.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. I guess. So, no, I'm, I was talking about Moore's Law in terms of, you know, the actual feature size, the physical feature size.

**Chris Gammell:** Well, they, they did that, the FinFET stuff where they, again, went vertical and then the poly went over and then they can shrink it down a little. I, you know, physically it has to end because... Exactly. I know. Yeah. So, they're just, you know, coming up with different ways to say, no, we're really cheating or we're really getting this enhanced performance. It's all marketing, to be honest with you.

**Dave Jones:** Moore's Law's just turned into marketing. Okay. Yeah, yeah.

**Chris Gammell:** We are in this advanced process and look how small, we're right on Moore, you know.

**Jake Baker:** Moore's Law, sponsored by Intel. Yeah.

**Dave Jones:** The three-dimensional silicon company. Right. Yep.

**Jake Baker:** What about, I mean, so a student getting started on this stuff, I mean, what, what is the path in, you know, just even at UNLV? What, what, at what point in their, in their journey are they, are they getting to your class?

**Chris Gammell:** Well, as I mentioned a moment ago, I'm hoping they get to it in their second year when I teach circuits. But generally, it's been senior. The chip design stuff is senior slash grad.

**Dave Jones:** Is it, is it a compulsory part of the engineering course or is it a optional thing?

**Chris Gammell:** They can select that. Right. Or they could go to power or whatever.

**Dave Jones:** Right. Okay. How many people are doing what these days?

**Chris Gammell:** There's quite a few people that want the power track because there's lots of jobs in power.

**Dave Jones:** I was going to say, yeah. And it's probably easier, right? You know, your stuff is fundamentally, people probably, rightly or wrongly, people see it as difficult.

**Chris Gammell:** Yeah. I think that's what the students would say. Right. I think power's kind of lacking glamour, but.

**Dave Jones:** It is lacking glamour, yes. I can remember when I was doing it, we had a power guy coming in and was practically pleading for people to come into the power industry. It's, I know it's not glamorous, but. But money. But we need people, you know. Yeah. Hands and knees begging.

**Jake Baker:** Sad sight. So where do you see, okay, so you've seen a lot of the industry. You've seen, you've told us that Moore's Law is going to end, if not soon, at some point. It's fine. Where do you see all this stuff going? I mean, are you going to, do you see the education piece still being able to expand to these lower nodes? I mean, how much changes when you go to the lower nodes? Or where do you see even the chip industry going?

**Chris Gammell:** So I think the, it's tough to teach someone about the smaller technology nodes because there's just so many things that, that impede the learning process. Like, you know, you can't turn it this way. You can't do this. And it's not really related. You got to keep them on a Manhattan style. So I think in the older technologies, and it might be sounding like somebody that teaches vacuum tubes. I don't know. But I think you can learn the fundamentals. I actually think you can learn fundamentals with vacuum tubes as well. You just can't do layout, chip layout with vacuum tubes. You can still teach the fundamentals. I think that the future is going to be designing cells or modules for products where their system on a chip, well, I mean, future, it's the way it is now. And, you know, you'll be part of a design team that does something. You'll focus a lot on optimizing the design and looking at the trade-offs and ensuring that it's functions given, you know, this happening or that happening or this yield shift or whatever.

**Jake Baker:** Gotcha. Interesting.

**Dave Jones:** What do you think about the Intel laying off, what was it, how many percent, 10, 12 percent of their workforce or something? Was that, okay, that's obvious, you know, like, do they think they're going in, do you think they're going in the wrong direction or they miss the boat?

**Chris Gammell:** Um, well, first off, as someone that's been through, uh, working at companies, I was at EG&G when they had the nuclear moratorium and they had layoffs and we had three or four rounds before I left and went back to school. And then I've worked in the semiconductor industry and it's cyclic and there are layoffs regularly there. That as far, when I think of that, I just think it's really hard being in that atmosphere because it's depressing to be around people that are worried about, and I mean, you may be worried yourself. I know that it's not fun if you're worried about losing your job. Uh, it's not a fun environment to be in. So that's what I basically think about when, um, I hear about those things about, uh, you know, how unpleasant the atmosphere is to work in, um, unless you don't care.

**Speaker ?:** Right.

**Chris Gammell:** But as far as the, uh, um, you know, if it was a strategic thing, um, I don't really know too much about it. If they had a fab, they were closing and they had to lay the people off or they were shifting focus and, uh, it was...

**Dave Jones:** Well, they can their, uh, Adam, uh, CPU.

**Chris Gammell:** Okay. I believe. Yeah. Um, generally, you know, it's funny because I, I'm scratching my head. I read that news and I'm scratching my head a little bit because if you look at the, uh, IEEE spectrum a month or two before they announced announced the layoffs, there were literally pages and pages of jobs at Intel. Oh, really? Yeah.

**Dave Jones:** Interesting.

**Chris Gammell:** It was like hundreds, literally hundreds and hundreds of jobs. And, uh, I told my students, I said, I just got the IEEE spectrum and there were all kinds of jobs. You know?

**Dave Jones:** Quick, take my course. I told you.

**Chris Gammell:** That's great. And then... Well, but you never know. They may be hiring in different locations and the people they laid off didn't want to go or whatever. You don't know.

**Dave Jones:** Right. And what about the consolidation in the industry? It's like every, we could almost do an, in every second episode, we can have news of another semiconductor merger.

**Chris Gammell:** Yeah. Um, I think that's, that's just business. I mean, uh...

**Dave Jones:** But does it have to, I mean, it's got to end at some point, right?

**Chris Gammell:** Yeah. I, I think that it's kind of ending in memory. If you know the players and like DRAM, there's only like a, you know, a... There's two or three, right? Hynex, Samsung, Micron. Hynex, Samsung, and...

**Jake Baker:** Yep, yep. And Micron almost bit the bucket a while back, too. Yeah, exactly.

**Chris Gammell:** Yeah, wow. They, they are working with, or they purchased Elpida, or absorbed Elpida, which is from NEC and Hitachi, and, and there's a few others that, so it's, yeah. I don't know how much more, more, uh, how much smaller the market can get or the players can get before there's issues with monopolies.

**Jake Baker:** Well, actually, the players get bigger, there's just fewer of them. They're right, yeah, yeah. Yeah, yeah, exactly.

**Dave Jones:** That's all too depressing. Can we have something more up?

**Jake Baker:** Yeah, yeah, yeah. So actually, I, I want to call out, so first off, your site is, uh, fantastic. Oh, thank you. Yeah, you've got a lot of great information there.

**Dave Jones:** And it's HTML. Raw HTML. It's HTML. It's, it's Comic Sans. It's great.

**Chris Gammell:** It's funny you mention that. It will tease everyone off. Yeah, Comic Sans.

**Jake Baker:** Everybody hates, everybody hates on Comic Sans, but I think it's fun.

**Chris Gammell:** And that's why I did it, and I'll tell you the other thing. Yes. And the other thing is, there was a book, I don't know, it's been a while now, that says, it was entitled, Web Pages That Suck. And I used to tease my students. I said, you know, my web pages are going to end up in this book, don't you? And they're like, really? You think so? And I'm like, yeah, I put it out there just to get the information out. And I use Comic Sans because everybody hates it.

**Jake Baker:** That's great. Nice. Trolling the students. Oh, yes. I wanted to call out the bad circuit design because not only, there's a lot of good examples here. That was always my favorite part of Art of Electronics, too, except you actually explain it versus the ones in Art of Electronics. I look at it, I'm like, well, what's wrong with that? Yeah, right. So thanks for at least explaining them. These are really good. Oh, cool. Yeah. These are.

**Chris Gammell:** Yeah, I tried to put stuff in there that was useful. The, you know, the examples from the book. So if you're trying to learn on your own and, you know, speaking of layoffs, some of this went back to when there were really good people getting laid off and they were like, well, I know this area really well, but I want to expand my knowledge. Can I take your class or whatever? And right in the mid-2000s, when we started having economic problems, I went from, I taught in Boise on the cable, you know, the cable TV, you know, to broadcast so they could do the videos. Right at that point, they stopped doing the, what's it called, the cable channel for the university. And so I bought this equipment and started recording the lectures and people started using them. And then I started getting emails from people, oh, I studied your class. I did the problems. I was able to get a job. And then, you know, it just, it makes you feel good because, you know, you're helping people and changing their lives. And so I've continued doing it. And the students now love it. And I always joke, well, do you guys really use the videos? Yes, we use the video.

**Jake Baker:** That's awesome. That's great. Yeah. Well, that's good. I think that, you know, we're going to, we're going to definitely look forward to the rest of, or when you get the rest of those courses out, I think that'll be really interesting, especially the, the, the real talk about op amps and everything. That's great.

**Dave Jones:** Are they going to be free? Is it going to be publicly accessible?

**Chris Gammell:** Well, see, that's what I want. I already have on my website, if you hit the courses, if you go to look, I have taught circuits one and it was in the summer. So it was accelerated, but I already have some basic classes, but I really think it's hard for students to stare at a lecture for an hour and 15 minutes on a computer. And so I'm going to try to break up the topics so they're easier to digest. I'm going to try to force the university or not force, ask the university to make them public so that anybody can use them. The issue there is...

**Dave Jones:** Because that's the way a lot of universities are going, you know, the MIT open courseware and all that sort of stuff.

**Chris Gammell:** Yeah.

**Jake Baker:** Yeah. MITx. Yeah.

**Chris Gammell:** Yeah. So we'll see what happens. It's a new thing for me. So...

**Jake Baker:** That's great.

**Dave Jones:** Well, it's a new thing for the universities too. I mean, they go, we're giving away all our lectures. Like, isn't that what people have been paying us hundreds of years? Yeah. You know, like... The answer's no. The answer's no. It's a totally different paradigm.

**Chris Gammell:** You know, the funny thing is you get students that say, they'll send you emails, they want to go to grad school or whatever, and they'll say, I took the online MIT class and I know this subject. And then you talk to them and they don't know the subject because they didn't really enroll and they didn't have the pressure of doing the work and getting a grade and all that, you know? So it's just, it's really a unique person that can be that self-motivated to really push themselves to learn from one of those classes. Got it. All right, Jake. Well, Jake, thank you very much. Thanks so much. All right. Thank you. Nice talking to you both.

**Jake Baker:** Well, wait, where can people find... Other than CMOSEDU.com, how can people find you online? Email, Twitter, anything like that?

**Chris Gammell:** No, no Facebook, no Twitter.

**Dave Jones:** No Twitter. I can understand no Facebook, but come on, Twitter's the bomb. Oh, okay. I don't... No.

**Jake Baker:** We'll get Jake signed up for Twitter just after this. All right. People can bug them on there. Hey, Jake, take a look at this circuit I just designed. What do you think of it? You're asking me to think?

**Chris Gammell:** Don't do that.

**Jake Baker:** Awesome. Well, thanks so much for being on the show. We really appreciate it. All right. Thank you. Talk to you guys later. Thanks, Mike. Bye-bye.

**Dave Jones:** Catch you next time. Bye-bye.
