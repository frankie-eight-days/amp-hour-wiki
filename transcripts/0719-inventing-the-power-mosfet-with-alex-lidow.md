---
episode: 719
title: Inventing the Power MOSFET with Alex Lidow
url: https://theamphour.com/719-inventing-the-power-mosfet-with-alex-lidow/
---

**Dave Jones:** This is The Amp Hour Podcast, released March 20th, 2026. Episode number 719 with Alex Lido from Efficient Power Conversion. Also, the inventor of the Power MOSFET. Enjoy. Welcome to The Amp Hour. I'm Dave Jones from the EEVlog.

**Alex Lidow:** And I'm Alex Lido from Efficient Power Conversion.

**Dave Jones:** Thank you very much for joining us, Alex. This is going to be really interesting because I'm into history of silicon companies. And a lot of people will not have heard of Efficient EPC, Efficient Power Converters. And we'll get into that. But can you tell us about your background? Because they might know you better as the former CEO of International Rectifier, which was founded by your father and grandfather. Is that correct? That's correct.

**Alex Lidow:** It was founded by my father and grandfather in 1947. And I joined them just after getting my Ph.D. in 1977. So this is my 50th year in the business. And, you know, try to match that for a moment. It's a long time in that. That's impressive. Right. And my first challenge was to build a better transistor. And my friend from graduate school, Tom Herman, and I came up with something that's now called the Power MOSFET. And we developed that in the last couple of years of the 70s. And that was, you know, really replaced the bipolar transistor. And it was the beginning of my journey to constantly, you know, find better ways to do power conversion. So I was an R&D engineer at International Rectifier. Eventually I became head of R&D. Then I became head of R&D in manufacturing. Then I became head of R&D in manufacturing and sales and marketing. Then I became CEO. So it was kind of a progression through the ranks.

**Dave Jones:** When did you become CEO? When did you join the CEO?

**Alex Lidow:** 1995.

**Dave Jones:** 95. Okay. Yeah. And that ended in 2007 when you formed Efficient Power Converters.

**Alex Lidow:** That's correct. I started EPC in November, actually the end of October of 2007. And we launched our first product in June of 2009. And actually went into mass production in March of 2010. So, you know, since then, you know, we've filled out the line with hundreds of parts and many generations of technology iteration. But the main thesis was, number one, make better power devices using GAN on silicon. And then number two is progress from discrete transistors into integrated circuits. And so we've been on that journey for, you know, what is it, about 18 years now? And that's the strategy we started with. It's still our strategy.

**Dave Jones:** Awesome. Well, we'll definitely get into the GAN stuff because that's what you guys are doing now. And that's what everyone's talking about these days, GAN power transistors, how efficient they are, et cetera. Can we go back to the International Rectifier days? You invented the HexFET.

**Alex Lidow:** Yeah. Well, actually, before that, the power MOSFET, we had the basic patents on power MOSFETs in general. There were MOSFETs that conducted power before us. But the power MOSFET, as it became, you know, commercially viable, was really a development that just very few of us were involved in. And our patents over the years brought in almost a billion dollars in royalties. So we were the only ones with basic patents on MOSFETs. Now long expired. But, you know, the HexFET was just a follow-on to that. And it was one of those late-night epiphanies where Tom Herman gave me a call at 2 in the morning and said, hey, I got an idea. And, you know, we went from there. Of course, there are others involved, but Tom and I were kind of the core element of most of that.

**Dave Jones:** Right. So can you explain what makes the HexFET different to a regular power MOSFET at the time? Start with, like, what made a power MOSFET different from just a regular signal MOSFET? And then what makes the HexFET different?

**Alex Lidow:** Well, so the difference was, you know, and maybe I'll give you the background here as well, is, you know, bipolar transistors were the dominant force in those days. And bipolar transistors were used for a whole host of things, you know, from driving motors to making power supplies. And they were very limited in speed. They're also fairly delicate. They had a safe operating area problem. And they also had limited gain. So, you know, it was a little bit more challenging.

**Dave Jones:** They were delicate. Bipolars were delicate.

**Alex Lidow:** Very delicate.

**Dave Jones:** Back then. Yeah. Oh, because they've got the reputation these days of being, you know, robust, solid, as opposed to FETs, which are, you know, not as robust. No?

**Alex Lidow:** Wow. No, maybe a low voltage, but at high voltage, they had a glass passivated trench around them. And that glass cracked. And it was a problem. So when I came to work at International Rectifier, my marketing boss was a guy named Bill Collins. And he was a gray-haired gentleman, very wise and very smart. And, you know, I knew him for the rest of his life. And he became a very dear friend. But he came in. And I remember the very first day I'm starting. I'm just right, you know, like fresh out of graduate school. What do I know? Nothing. And he came in very stern. And he said, what's the definition of an engineer? I kind of looked at him. I'm not quite sure. He said, an engineer is somebody who can do for 50 cents what any damn fool can do for a dollar. Now get to work. That's great. And he's right. Oh, I love it. He was right. Yeah.

**Dave Jones:** It was true.

**Alex Lidow:** And it became almost a little bit of a motivating force. Now, a couple of weeks in, and it was just a couple of weeks in. It was between December 26th and I guess February 8th, 1978 was exactly how long it was in that period. He came to, you know, to me and my desk. I was in a communal area and said, I know what we want to do. I said, well, what's that? 400 volts, one ohm.

**Dave Jones:** Ooh. Which was a big deal. One ohm was hard back then.

**Alex Lidow:** Well, it had never been done. And 400 volts. That was a high voltage device and one ohm. And, of course, I asked why. He said, well, because 400 volts, one ohm means that you can make an ACDC switching power supply using a single-ended flyback topology. He said, if you can do that, you can get that business. So, you know, Tom and I went about doing it and actually were able to fairly quickly achieve that. When I say quickly, we launched our products in November of that year. And those products were not HexFets. They had a racetrack. And I remember drawing it on a drafting table every little line, every little line, every little line, over and over again to make this huge, huge 200x scale design. And we launched that in November. And we launched that in November. But one of the problems was in July of that year, we got our very first run through. And in that time, Tom and I and a couple other people, we would actually run in. We were working in the fab 24 hours a day. And the first ones didn't work. And they weren't 400 volts one ohm. They were 400 volts two ohms. Oh, no. You know, that's Bill Collins. He was very, very strict about these things. He says, well, it's not a product. So, you know, Tom and I, you know, after kind of going through the five-stage degrees, we went back to the drawing board. And Tom pointed out that I'd made a mistake in one of my dimensions. And instead of a 15 micron separation between these two openings, I'd made 10 microns. And just to give you an idea, that was the scale of one little tick on this huge Mylar sheet.

**Dave Jones:** But it meant throwing everything out.

**Alex Lidow:** Starting over. You know, it's not the sort of thing that was even that obvious. Yep. But he figured that out because he went backwards from what was wrong with the device and said, well, it was wrong. So, oh, Jesus. So, you know, kind of going through the five stages of grief. And I remember I was, you know, obsessing on this thing. What do we do? You know, how do we start over? It took six weeks of drawing of that thing. Day and night. Day and night. It was incredibly difficult. And that was without taking any holiday, going 12, 14, 16-hour days. So, you know, I was facing that. And how can I make a November launch date? And I remember fairly clear. I was going underneath a bridge, you know, here in Los Angeles, a freeway, actually. And all of a sudden, an idea came to me. It was July 22nd, to be specific. And that idea was.

**Dave Jones:** You remember the date. Okay.

**Alex Lidow:** I remember the moment. You know, it was one of those flashes. Wow. And, you know, the idea was to inject extra charge in that too narrow region, which would, in fact, make it look wider to the electrons. And that became one of the basic inventions of the MOSFET. It worked not the first, but the second time that we tried it. And immediately, the device went from 2 ohms down to 0.7 ohms.

**Dave Jones:** It was even better than we thought. Nice. You and now you have a product.

**Alex Lidow:** And now you have a product.

**Dave Jones:** You have a viable product. Just in time. How did you inject the charge into there? For those who don't understand that.

**Alex Lidow:** Yeah. But the idea that you put charge there was the innovation because that was new thinking. So, we were very fortunate. We got it out in November. And it became a hit pretty quickly in November 1978. And I remember, you know, lots of people wanted these things. They were lined up all over the place. And one of the early applicants for, you know, samples was Apple. Steve Wozniak. All right. Wanted it for a power supply that would go inside of his Apple II, would turn out to be the Apple IIe. But also, fairly quickly after that, IBM wanted it for their power supplies for their desktop computers. And that became one of those crossing the chasm moments. Because the single-handed flyback, wide-ranging ACDC power supply became a standard. They made millions of those computers all over the place. Initially, they were very standardized on our MOSFETs. Of course, eventually, everybody else came into the business. But by then, we had a whole barrage of patents. And by June, actually, by February. So, we launched it in November. And by February was when Tom came with this idea of, you know, why don't we just make a sell out of this instead of a racetrack. We figured that that was about three times higher density. And so, by 1979. So, that's only eight months later, we launched the HEXFET. And that became, because of the 3x difference in die size, that became commercially obvious against the bipolar transistor.

**Dave Jones:** And that was the IRF-130, wasn't it? The first?

**Alex Lidow:** Well, the very first part was the IRF-100 at 100 volts and the IRF-300 at 400 volts. The very first HEXFETs were the IRF-130 and the IRF-330. Both in those famous TO3 cans, which now you can't.

**Dave Jones:** It's very obsolete. So, what made you choose the hexagonal pattern? Because other manufacturers, so you guys had a pattern on the hexagonal thing, is that right? And other manufacturers couldn't copy the hexagonal. Or they had to use some other pattern? They could. Is that what it was?

**Alex Lidow:** And many of them did. But the reason we use hexagonal was that if you look at a hexagonal pattern like a beehive, you'll notice the hexagons are offset, right? And every angle in a hexagon is 120 degrees. So, if you look at depletion in high voltage, this depletion region spreads out like that. It perfectly meets right in the middle. So, you always have the lowest possible electric field. If you have squares that are aligned like this, then you always have a hole in the middle, which is a high electric field point and cause a premature breakdown. If you have offset squares, you still have 90 degree angles. And that extra curve lowers the breakdown voltage. So, we figured that out way before anybody else. And then people were imitating it with squares and, you know, it wasn't quite as good. They couldn't have to charge thing. And, you know, by, you know, maybe mid to late 80s, well, mid 80, 1986, we started getting people that were imitating our devices. And, but we had, you know, free reign until then.

**Dave Jones:** Right. Yeah. I can remember using the hex vets back in the mid to late 80s. And they were like, wow. You know, nothing else touched it. It was. Yeah. It was fantastic. Yeah. It was game changing. So, IR had the market sewn up fairly much.

**Alex Lidow:** Well, look, our market share, you know, we built a huge factory, all this stuff. But, you know, over time, there were big, big contenders, you know, competitors in there. All the Japanese jumped in. Motorola, which had a huge share of the bipolar market, was finally came into MOSFETs, but late. You know, Siemens was making them. Gosh, we had RCA, General Electric, Hewlett-Packard. It was just a long list.

**Dave Jones:** HP made. Fets?

**Alex Lidow:** Yeah.

**Dave Jones:** Really?

**Alex Lidow:** It was a very short period of time because they could not compete. Yeah. They stopped pretty quickly. But we had, you know, NEC, Matsushita, Toshiba, Hitachi, Oki Electric. They all jumped in on this. At one point, there were about 42 competitors. And we wound up licensing 25 and about 17 fell out.

**Dave Jones:** Wow. Wow. Wow. And they're all merged or gone now, I guess. So.

**Alex Lidow:** Well, you know, they're in different embodiments. I mean, Infineon is a very powerful company. And that's spun out of Siemens. So, but I think that's kind of the only one. Motorola pretty much died. Now there's OnSemi, but it's not really a factor in this business. So really, Infineon is the survivor of that. And eventually, they're the ones that bought International Rectifier.

**Dave Jones:** What have been the major innovations in FETs transistors over the years? Your power MOSFET was one. HexFET was another. What other technologies have there been that were like really major, huge step ups? Because like one, two ohms is like one ohm for a FET is like was low back in the 80s. But now it's like, no, it's nothing.

**Alex Lidow:** Yeah. I mean, now we're talking micro ohms for the same size die. So, yeah, it's very different. So, you know, first step, you know, power MOSFET. Second step, I would say, you know, most people would agree. HexFET was a big step forward. I think the third step was in the later 80s was the IGBT. And that is really a variant of a FET in that it trades the low resistance N plus substrate with a P substrate. And all of a sudden it acts kind of like a bipolar transistor and a MOSFET and at high voltages that results in a lower effective on resistance. So high voltages started to be addressed with IGBTs. But not to be outdone by that, you know, Siemens, now Infineon, developed something called CoolMoss. I'm not CoolMoss. Oh, yes. I remember the CoolMoss. Yeah.

**Dave Jones:** Well, they're around still. Yeah. CoolMoss. Yes.

**Alex Lidow:** Right. Explain that to us. What was that? It was a very smart thing. And what it did was, it's now called a superjunction FET, is they actually put multiple levels of grown silicon or epitaxial silicon. And on each level, they would define, you know, openings. So you created these columns of P-type semiconductor that were almost vertical. And so it caused the conduction to go down this way through that, sort of through that tunnel. And when you were blocking, the tunnel basically depleted and closed off. The net effect was you could go to much thinner silicon and you would get 2x, maybe even 3x improvement in the on resistance for a given area. And that was a real big step forward. And, again, now the MOSFETs were competing against IGBTs at higher voltages. And, you know, that tension was going on there. So that was, I would say that then, you know, the next one was probably TrenchMoss, which was pioneered by Vichay in the, like, 1994 timeframe. Yep. Yeah, I think I remember.

**Dave Jones:** Yep.

**Alex Lidow:** Yeah, and that started replacing the HexFET style, which was a planar device, started replacing that slowly, slowly. And today, virtually all MOSFETs are Trench MOSFETs. Right. So, you know, that was the obsolescence of the HexFET concept. Although the HexFET concept and that planar FET concept still is the dominant form of IGBTs and of silicon carbide.

**Dave Jones:** Oh, okay. So it's still kind of a good one. And that was another innovation, wasn't it? Silicon carbide.

**Alex Lidow:** Well, then we get to silicon carbide. And silicon carbide showed up as a diode in the late 90s. And then in the early aughts, started showing up as a transistor. And then, you know, and it starts, it started a process to replace the IGBT. Because it's really in the same wheelhouse. It's higher voltages. It's faster switching. But it's not blazing fast. But at high voltages, you don't care about blazing fast. Because it makes too much noise when you switch, you know. Yes. Oh, of course.

**Dave Jones:** The huge edges. Yeah, yeah. If you switch in 600 volts in, you know, super fast. Right.

**Alex Lidow:** And you have all sorts of issues. In 1999, Japanese researchers figured out how to grow gallium nitride as a thin layer on top of silicon. And that I learned about in the early aughts. And that switched on a light bulb. Because it told me that you can overcome the cost problem of a compound semiconductor. And, you know, just to bring out what that cost problem is, you know, the silicon is very cheap. And it's actually very cheap because, well, it's heavily tooled. Right. There's a lot of capital investment. But fundamentally, it's cheap because the bond between silicon atoms isn't very strong. Okay. So you don't have to put a lot of energy into the system to create the crystal. Now, silicon carbide has a real strong bond. That's what makes it a wide band gap. Because it's a wide band gap because it's hard to peel an electron off that bond. So that's what makes it a wide band gap. It also makes it expensive because the energy of formation is a whole lot more than silicon. So you can't really ever have a silicon carbide crystal that would be as cheap as silicon. It doesn't matter what you do. So what about gallium nitride? It's also a wide band gap. It also has a stronger bond. But if all you do is you lay a micron thin layer on top of a standard silicon, you don't have that cost of growing the crystal. So that was a big light bulb. Gallium nitride also has higher electron mobility. Gallium nitride, because it's a wide band gap, means you can bring high voltage terminals closer together without a spark. And without breaking down the crystal, without pulling that electron off. So you can create smaller dimension devices in high voltage than you can in silicon. And also it has a miraculous thing called a two-dimensional electron gas, which is a quantum mechanical gas that scoots along the surface and allows you to make very efficient lateral devices. But so much more efficient than a vertical silicon device. Much more efficient than, you know, a MOSFET than it could ever dream to be. Theoretically, 6,000 times more efficient. So there's a lot there.

**Dave Jones:** Wow. You said quantum gas. How does that? I've never heard that term before.

**Alex Lidow:** Yeah, it's a beautiful thing. It's called a two-dimensional electron gas or 2DEC. It was first, I'll say, theorized in the 90s and then experimentally verified. Here's how it works. Gallium nitride as a crystal, it's a worksite blend crystal. But what that means is it's a polar crystal. And if you have something that's polar, it means that if you bend it, it generates a charge. Okay? If it's not polar, none of the matter what you do, silicon's not polar. So you bend this thing and it makes a charge. So what you do in gallium nitride is you grow gallium nitride crystals, a thin layer on silicon, and then you put a very thin layer of something that squeezes the surface. In this case, aluminum gallium nitride. So it squeezes that surface with, you know, the intensity of a heterojunction, which is, you know, that is very, very intense. So intense that it generates 6 megavolts per centimeter electric field. And it does that really over an extremely small, just a few angstroms distance. So now you have this huge electric field. What that does is it sucks every electron that it can think of up to the surface and hits this very intense field. And it squeezes the electrons so much that they actually become quantum mechanical. And in that sense, they become a unified electron gas. And because it's no longer individual electrons, but it's an electron gas, it has much higher mobility, right? You're now dealing with a very different transport mechanism than electron hopping from site to site to site. This is just everywhere, all the time, anywhere. And so that allows gallium nitride to be extremely efficient as an N-type transistor. There's no equivalent on the P side. So there is an equivalent, but it's not very good. So you really don't have P-type GAN as a result. So anyway, so 2007, I realized that silicon now MOSFETs was really just a game of cost. And cost is won by the person with the deepest pockets. And that's not so much fun. So I started EPC on the idea that we can make gallium nitride transistors and then integrated circuits that can do power conversion more efficiently. That's how that happened.

**Dave Jones:** Wow. So how do you just decide to start a semiconductor company? Like, did you use your own funding? Did you get external funding? Because I imagine it's not a cheap enterprise to just go, oh, I'm going to start my own semiconductor company. Well, you probably could do it bare bones, but...

**Alex Lidow:** No, I mean, necessity is a mother invention. So, you know, in 2007, I got into a, you know, sideways with my board of directors, and they fired me. So I got fired.

**Dave Jones:** Oh, they did?

**Alex Lidow:** Yeah. Right. So I was without a job. Wow. Okay. It was, yeah, I mean, it was a terrible story. They did it based on very false pretenses. Somebody wanted to take over. It was a real bad, nasty story. But here I am out there, you know, 50-something years old and without a job. And so I thought, what is the best combination of my skills and knowledge? And, you know, throughout my career, I've never not been a device physicist and an engineer. You know, I may have been a bureaucrat, but I always kept up on this stuff.

**Dave Jones:** Awesome.

**Alex Lidow:** So I went back to hitting up the books and relearned all my device physics, spent nights and days and all this. And I came up with the thought that what we can do is we can, if we can make gallium nitride in a standard silicon foundry side by side with silicon wafers, it would take very little capital to get going.

**Dave Jones:** So no one had done that before?

**Alex Lidow:** No. Not only that, but when I suggested it to the first couple of foundries, they said, you're crazy. We're not going to let gallium into our silicon found. That's a contaminant. Oh, okay. Yeah. So, no, we're not going to do that. So, you know, I got my bag in hand and I keep going around. But then I went to a person who I've done business with for several years who actually owned foundries. His name is Archie Wang. He's a very brilliant, he's a device guy from the beginning as well. And I talked to him and he had kind of an older six-inch fab that was maybe running down on usefulness. And I suggested to him that he let me run my gallium nitride wafers in there. And he said, okay. As a matter of fact, I remember in the meeting, the very first meeting in Taiwan, he said, I'm in. Let's try it. Awesome. And he's been my partner ever since. And he's been a phenomenal partner because we never had venture funding. It was just him and me. Oh, wow.

**Dave Jones:** Okay. So you were just doing, you were designing this yourself and just using his foundry. He was the partner. No, I wasn't designing myself.

**Alex Lidow:** I had colleagues, we hired people. Oh, right. Okay. But I'm saying in terms of writing the checks, it was, you know, Archie and me. And still is. So. Wow. Okay. And, you know, so, and, and so, you know, me and my co-founders, which is Bob Beach and Joe Cow, they've been, they were co-founders. They took a huge risk by leaving international right to fire to go, you know, leave with the, you know, the, the, the fired CEO. So, um, so you're the traitorous three.

**Dave Jones:** In, in, we were traitorous eight. No, you weren't.

**Alex Lidow:** They kicked us out. They kicked us out. It wasn't that we went. So then nothing to, uh, to fall back on there. So, um, so we started, you know, doing this thing in, in Archie's foundry side by side. We were working pretty well. So, so then Archie said, Hey, I want to invest in this. And he did. And he became an investment partner and we grew together and, um, you know, developed more and more product. But it's certainly a lot cheaper than building from scratch a wafer fab. So, uh, we were able to do it, you know, much less expensive than you might have thought otherwise. And, um, over the years we, we, uh, I moved, not moved, but I added to our foundry an eight inch foundry. That's Vanguard international. Uh, they're doing a great job. So we have two foundries now. Uh, and then we started building integrated circuits and higher and higher percentage of our product line is now integrated circuits.

**Dave Jones:** But what do you mean by integrated circuits? What, because as far as I know, you only manufactured GAN power transistors and that was it. What are the, what are the integrated circuits do?

**Alex Lidow:** So, so eight years ago, you know, first of all, power conversion, uh, most power conversion, my estimate is 80% of power conversion, um, has a sub element that is a half bridge. That's a high side and a low side fat. They have drivers and then they have a level shift. And that's how almost everything's done. You have full bridges, you have three phase bridges for motors. You have all that bridge. So the thought was, well, let's integrate a bridge. Um, and in 2014, we integrated a half bridge. Um, and then in 2017, we added all the driver circuitry and the level circuitry, level shift circuitry, uh, and protection circuitry. And that became a hit product, particularly with, uh, motor drives. And today, you know, a large, large number of those humanoid robots use our integrated circuits for all the, the motors and, and, uh, and stuff like that. So that became, um, a thing. Um, and, you know, again, half bridges used for a lot of stuff. So we're making half bridges that work in audio amplifiers, DC to DC converters, humanoid robots, uh, drones, all sorts of things. So that's become a significant business. Now in parallel, um, we also started, uh, making rad hard devices because fairly early on, um, based on, again, experience from the international rectifier. Um, I had been an engineer developing radiation, hard transistors when I was still an R and D engineer. Um, and I recognized that gallium nitrate had some unique properties that would make it virtually impervious to radiation. So we developed a bunch of radiation, hard stuff. And now we have radiation, hard transistors, the radiation, hard ICs, and, you know, all the new satellites are using it. Uh, we have, you know, a large market share up from nothing five years ago. Uh, and, you know, eventually it'd be a hundred percent share.

**Dave Jones:** Can you explain how the radiation hardened works? You said it's basically immune by design or how does it work?

**Alex Lidow:** Partially by design and partially intrinsic. So in, in, uh, uh, power MOSFET, um, and in any MOS device, you put it in space and the weakest element is the O, the oxide. Uh, because silicon dioxide traps electrons. So when you have gamma radiation, um, which is basically electrons or even charged protons, um, they all will trap in that oxide. And the more that trap, the lower and lower the threshold voltage goes until it goes below zero. Oh. And it becomes a non-functioning device.

**Dave Jones:** Oh, so it's a buildup thing. It builds up. Yeah.

**Alex Lidow:** Yeah. Well, that's one, one problem. Second problem. Second problem is that, um, if you have a massive element, like a, like a neutron or proton or gold or some other heavy element, xenon, whatever. Um, and they come crashing into your device. Um, it cracks the crystal. It's like a bowling ball, you know, cracks the crystal. It's called displacement damage. Um, and, uh, the, the good thing is that GAN is a very strong chemical bond. So it withstands that much, much more than silicon does. Much, way beyond the horizon of these satellite lifetime. Um, so that's a second thing, which, you know, is intrinsically better. And the, the third thing is that if you design it right, when one of these charged particles comes screaming on through, it doesn't create a spike in electromagnetic radiation or in, in spike in the electric field, which can destroy the device. That's a lot of design involved in doing that. So by solving those three problems, we created devices that are, you know, they're, they're basically, they're not the thing that's going to fail in your satellite and you don't need shielding to, to, to do it. So they've become very popular.

**Dave Jones:** How much of the satellite market do you have? How much, as far as power semis goes?

**Alex Lidow:** Well, so we have about 30% of the MOSFET business. Wow. Uh, which used to be 100% in Finneon. And it was based on designs that I did back in International Rectifier. So those are kind of old designs that were now, uh, now obsoleting. Uh, and, uh, you know, it'll eventually go up to, you know, there'll be legacy satellites. It'll use MOSFET forever. Uh, but you know, anything new is going to use GANs.

**Dave Jones:** Fascinating. So people think GANs are associated with high voltage stuff, but that's not true. They're lower voltage, like, you know, 200, 300 volts maximum. Are they not?

**Alex Lidow:** So if you look at the market for just say power MOSFETs for a moment, 75% of that market is less than 200 volts. And only 21% is greater than 400 volts. So there's a little slice there between 200 and 400, but it's very insignificant. So the high voltage stuff, which you hear about because you're a consumer, is actually, you know, about 21% of the market. And why do you hear about it? It's because everybody talks, everybody knows about fast GAN chargers, which was a, you know, brilliant thing by Gene Sheridan and Navitas, absolutely brilliant, where they found this niche that could then bring GAN to the forefront of people's minds. So now people know about GAN, and that's great. In the meantime...

**Dave Jones:** It's actually branded everywhere. It's like big GAN on the side of, you know, your phone charger or whatever.

**Alex Lidow:** Brilliant. It's brilliant. And, but that market, that 600 volt market, very small fraction of it is a premium market. And now, because so many people jumped into it, it's very, very small. It's a premium market because it's just a commodity. There are a bunch of people selling it, and nobody really cares about the performance. They only care about the price. So that was my experience at International Rectifier with 600 volt MOSFETs and IGBTs, is nobody cared about performance. They just wanted a lower price. So when I started EPC, I said, I'm not going to do that. I'm going to go to where everybody, when I was making MOSFETs, everybody was saying, I want something faster and I want something smaller. So our business started off and stayed in the 200 volt and under range, which is a performance driven market. It's also 75% of the, of the MOSFET market, not 21%. So it's the much bigger market. And a much higher percentage of that is a premium performance market. So that's why our margins are above 50%. And we're growing very rapidly. And I think that we have a defensible position competitively as well.

**Dave Jones:** Have you ever encountered, like, I believe there's lots of fake GAN marketing out there, because like, as you said, like the consumer markets caught on that, oh, if it's got GAN on it, it means, oh, it's super good, super efficient, whatever charges my phone faster, but people will slap. Have you found that people slap like GAN on the side of things and they're not really using GAN? I don't know.

**Alex Lidow:** They haven't done that with our stuff, because our stuff tends to be in AI servers, humanoid robots, drones, and satellites where people, the consumer isn't really exposed. So it doesn't need that fake branding or even real branding to get the emotion, you know, because it's the emotion. I got something cool. I got a GAN charger. Yeah, yeah. Well, what's cool is it's small and compact. The fact that it's GAN is really irrelevant to the user, but if it becomes an emotional connection, they'll buy it.

**Dave Jones:** Yep, exactly. How many competitors are there in the GAN market? How many manufacturers out there of GAN, true GAN transistors that compete with yours, or at least their GAN?

**Alex Lidow:** I don't even know how many there are in the higher voltages, but I'll name a few of them. And then in low voltage, we only have two, and that's Infineon and InnoScience. But in the high voltage, you have Infineon, InnoScience, STMicro, Navitas, Power Integrations, oh gosh, you know, Rome, Ankara. Oh yeah, Rome, yeah. Keep going. You know, they all go on and on and on. And they all go after high voltage because, you know, it's the thing that has the brand on the side of it. So it's a shiny metal object that you can be attracted to. But we've stayed in an area, and there are only two competitors and they really are nowhere near as high performance as our devices. So we can get the premium software.

**Dave Jones:** So there's no Asian competitors? There's no Chinese companies? InnoScience. Making or attempting? Oh, InnoSciences. Okay. Yeah,

**Alex Lidow:** it's Chinese. They were started with government funding. They were started with the purpose of imitating us. And, you know, we've definitely taken them to task with our patents. And we're locked in patent battles in a couple of different countries. So it's, you know, it's a tense thing.

**Dave Jones:** How hard is that in China? How hard is it to enforce your patents in China? Is that, is that a difficult, I've heard it can be difficult?

**Alex Lidow:** So I'll make a statement that will probably be somewhat shocking. The hardest place to enforce your patent is the United States of America. Really? Yeah, China and Germany, they're all much easier. Really? And yeah, and it's, it's really something that I think as a country, we need to come to grips with because that, it didn't used to be that way. It's become that way in the last 15, 20 years. And the reason is because people can challenge patents in multiple forums, multiple times. So they can sue you over and over again. So we won in the ITC and then we, they sued us in the, in the, what's called the patent, PTAB or patent and trademark appeals board. And then they came after us in the, in the customs office and, and federal court. So it's like this multiple jeopardy. And even when you win, there's an appeal. And even when there's an appeal, there's another appeal and then they can sue you again. No. Oh, yeah. Or you can do it over and over and over again for the same thing. There's no double jeopardy thing. Now we're trying to keep the law changed and there's bills in Congress and there's also executive orders are being proposed to make it, you know, single jeopardy, you know, pick one forum and do it once. And do it once. Yep. And in, in China and Germany and Japan, it's that way. So, it, it's just much simpler. Wow.

**Dave Jones:** I didn't know that.

**Alex Lidow:** Yeah.

**Dave Jones:** That is fascinating.

**Alex Lidow:** It's terrible. Wow. And, and it also is biased towards large companies, not foreign companies so much, but if you're a big company, you're not an innovator anymore. So the last thing you want is some little guy with a patent to mess up your business. So just throw a bunch of money at it. Just try over and over again. Yeah. Right. Mess it up. Yep. So, you know, the, the large companies are, are resisting this, um, streamlined process.

**Dave Jones:** Well, you guys are doing like, you mentioned AI data centers and stuff before. Um, obviously they're massive scale now and they need massive efficiency in their power because everyone, like they have to, you know, start up, you know, dedicated power plants just for, uh, these AI things. And you guys are doing stuff in that area and you've got some, um, screenshot stuff to share as well.

**Alex Lidow:** I've got lots of stuff to share, but, um, let's just set a background. So, you know, we're, we're right now being driven a lot by, um, by NVIDIA. What NVIDIA wants, you know, drives a lot. Uh, and there's a good reason. I mean, they're clearly way out in front. Um, so we started, um, uh, putting our FETs onto NVIDIA boards via module makers in, uh, 2019. Uh, so there's a fairly good chance that if you use AI, the electrons go through our parts. So we've been on those boards for a long time. Our share of that market is expanding. Uh, and, um, that's, that's a really wonderful area. And why is because GAN saves about, you know, 10% of the energy on the board versus a power MOSFET. So now I'll give you a little bit of a, you know, kind of throw some numbers out this year, this year, meaning the, in the last 12 months, uh, we are consuming 500 terawatt hours of electricity for data centers for AI. A terawatt hour.

**Dave Jones:** Just so we can get.

**Alex Lidow:** Yeah. Just so chat GPT.

**Dave Jones:** Just so we can get cat, just so we can get cat videos. And yeah.

**Alex Lidow:** Yeah. There's that too. But, um, and look, it's, it's, it's, it's valuable stuff in the end. We just don't know how to quite optimize the value, but it costs $150 million for a terawatt hour. So 700, uh, 500, um, terawatt hours is $75 billion. You save 10% of that seven and a half billion. So it's a good market. That's just on the server board,

**Dave Jones:** just on the server board. I don't, I don't think you charge enough for your, for your canned power chips.

**Alex Lidow:** Well, yeah. I mean, we can talk about that. People don't pay enough is the problem. Right. But, um, unbelievable. so, so this is, this is going to be a GAN world. I mean, forget the MOSFET. It'll take some time, but as you go from Blackwell to Verorubin to Feynman, the power per GPU goes from 1,400 watts to 4,400 watts in a Feynman. Okay. So, whoa, that's a lot. Now, just to give you, you know, kind of ideas, well, you know, if you're, you know, got a bunch of these Feynmans in, in a server, uh, rack, that server rack might be a megawatt. Okay. It's kind of scary.

**Dave Jones:** That's just mad.

**Alex Lidow:** Yeah. The size of a refrigerator. And that's, of course, the goal because you got to get them very close together to communicate efficiently and, you know, why make a big thing if you can make a small. So now, uh, Nvidia is saying, well, the best way to get a megawatt to a server card is at the highest possible voltage. And they, they picked 800 volts. Maybe it'll go higher in the future. Um, and so the game is, how do you get 800 volts to a, uh, a board efficiently? And there are, there are about four different ways of doing it. And when I say efficiently, you really want to think about the whole thing to the GPU, about four ways to do it. And I don't know which way it's going to work out. And it may, if it works out one way, it'll maybe change to the others. Um, so one of them is go 800 volts and go down to 12 volts on your board and then go from 12 volts down to the point of load. Um, and that's two stages, right? So here is an 800 volt to 12 volt converter. And this is, uh, let's see. Can we see that? I'm not sharing screen. I'm just sharing my picture. So you can see that up front. It's 5,000 square millimeters. It's eight millimeters thick, which is very important because these server boards are so close together. It's six kilowatts. Six kilowatts. Yeah. So, you know, that's a lot of kilowatts, right? It's what that's, that's 500 amperes output. But you know how big it is? How much input goes into these little, uh, 800 volt leads? Seven and a half amps. Seven and a half amps.

**Dave Jones:** Which is fine, which we can go through a pin header, which is why you can just go straight through.

**Speaker ?:** Yeah.

**Alex Lidow:** Right.

**Dave Jones:** Yeah.

**Alex Lidow:** So, so, you know, you go through these, you get 800 volts DC coming out of something called a sidecar, which is this big, um, you know, solid state, uh, uh, rectifier with probably silicon carbide. And this bus comes out with 1200 amps of, of, of 800 volt stuff. And then that goes to a rack and then it breaks up into eight and a half or seven and a half amp, um, little, little, little things that do this. And you have these on the board, no two, three, or four of them on the board. Uh, and it's crazy. It's absolutely crazy. Uh, but it's, it's driving new topologies. And that's, what's fun about it. Um, because if you do 800 volts input, well, what device will do that? So somebody will come out and say, well, you can get silicon carbide 1200 volts. Yeah. But do you really want to switch a 1200 volt device, um, uh, in order to convert it to 12? And the answer is only if you have a transformer that big, which doesn't fit. That big. Yes. Otherwise, no,

**Dave Jones:** no, you can't use a little PCB planar transformer or, or whatever. No.

**Alex Lidow:** So there, there are various options, but all of the options involve going to a multi-level topology. Uh, and the favorite one, which I think most of the successful reference designs, um, use something called ISOF, which is inputs and series and outputs in parallel. So here, what you have is eight stages. You can count them. You know, there's, there's one, two, three, and each stage is just a hundred volt input device and a 12 volt output device. Uh, here's what I was

**Dave Jones:** going to ask because, because your GANs can only do like a hundred, two hundred volts. They can't do the 800 volts.

**Alex Lidow:** yeah. So you do eight stages at a hundred volts and you connect those in series and that's 800 volts. Now you take the outputs, which are all 12 and a half volts and you connect them in parallel, input series, outputs parallel. And what happens is you now have a extremely efficient, um, eight stage converter, like 97 something percent efficient, uh, that can be very thin. Wow. Yeah, because each stage is running at a megahertz. So it's very small, uh, because it's running at a megahertz, not conducting much voltage, only a hundred volts across that. So you can't do that at higher voltages. Um, and, um, the, the other, um, um, the, the other advantage is that these eight stages can be rippled so that they reduce the output ripple. Um, and, you know, one way of looking at it is, you know, in everybody's used to having devices in parallel to share current or multi-phase power supplies to share current. This is just a multi-phase device sharing voltage. Uh, it's very simple control. It's auto-balancing because the transformers force the inputs to be a hundred volts because all the outputs are twelve and a half volts connected through transformers. Um, so I think this will be a very popular topology.

**Dave Jones:** With the, uh, switching frequency there, what is the trade-off? Why one megahertz? Why not two? Why not five? What are the trade-offs as you go up in frequency in your particular design?

**Alex Lidow:** I, I think in an LLC, that's, uh, you know, inductor-inductor, uh, coupled, um, uh, converter, which is, uh, a non-isolated, uh, converter, uh, that, that connects the input to the output in a, uh, at a variable ratio. So it doesn't regulate. But if you put eight of them in series, you can isolate it. So it becomes an isolated 800 volts, uh, but each of these little things are not isolated between the, the primer and the secondary side. So, um, um, this LLC is, um, uh, optimum at about megahertz or 1.2 megahertz before you get into, uh, losses, both in the transformer and in the FETs. So it's kind of an, an optimum, uh, thing. And a lot of people ask, well, why is, uh, you know, 100 volt per stage the best? And the answer is that there's a lot of, um, theory that shows that, um, lower voltage devices connected in series, particularly somewhere in the 200 volt or 150 volt range are more efficient in terms of silicon area as well as figure, other figures of merit than higher voltage devices. So it's, uh, you just need to be able to compensate, uh, for the cost adder of having more stages. Uh, and, you know, that, that is a, you know, again, that's, that's something that we believe is, is already done. Some people are still questioning it.

**Dave Jones:** Right. So you're, are you using, uh, planar transformers on that board?

**Alex Lidow:** Yeah.

**Dave Jones:** We didn't see it on the backside.

**Alex Lidow:** Here's just, this is a, this is a single planar transformer. Oh, oh, okay. Yep. Yep. So it looks like on the back and we actually put our rectifier FETS right on that transformer board. So you see four of them. Oh yeah.

**Dave Jones:** Yeah. You can see it on the bottom. How many, so how many, uh, turns in that, how many layers? For those who don't know what a planar transformer is, it's basically using the actual PCB as the winding core.

**Alex Lidow:** Yeah. So it's, it's eight to one. It goes a hundred volts down to 12 and a half.

**Dave Jones:** So what is the trade-off with the planar transformer? Have you, did you look at like wound ones, wound transformers? Did you try those or planar just

**Alex Lidow:** kills it? Do not. Is there any downside to it? You know, if you want to squeeze an eight, eight millimeter height, you're going to do a planar transformer. Uh, so. Yep.

**Dave Jones:** Of course. Okay. So it's a height. Right.

**Alex Lidow:** Yeah.

**Dave Jones:** Right. That's for the racks and stuff. Is it, it's got to go into a one rack unit high thing or half a rack unit or how does that work?

**Alex Lidow:** The racks today in Blackwell are 54 millimeter centers. That's called one U. You've probably heard the one U. Uh, but the racks in the Verorubin are HACU or 27 millimeter spacings.

**Dave Jones:** Okay.

**Alex Lidow:** And they're water cool. So you have to have a cooling plane and then your, your server board and that's got to fit in 27 millimeters.

**Dave Jones:** Is there any, is there any cooling plane on the back of your actual converter board or is that?

**Alex Lidow:** Yeah. These, these devices are all, uh, connect to a cooling plane.

**Dave Jones:** Oh, okay. Right. And that's just what one big heat sink that goes over the top or one, one big copper sheet with then water channels in it and whatnot. Yeah. Okay.

**Alex Lidow:** That's the way it's been communicated to us whether or not they change it. I don't know. I also said that's one of several things under consideration. The other ones are going from 800 down to 6 volts, which is even more challenging. Um, and a third one is to go 800 volts down to 50 volts on the rack. Uh, and then a fourth one is to go 800 volts to 50 volts on the board. So there are various different things. Uh, ISOP topology works for all of them. Uh, and, um, so I, I really think that we'll probably see some form of ISOP topology addressing all of those or whatever becomes dominant.

**Dave Jones:** And why, why did they decide at first to go to 12 volts on the board? Because that's kind of like the de facto standard. I mean, I assume there's nothing on those server boards that actually works at 12 volts. It's just then localized DC to DC converters to drop down or?

**Alex Lidow:** Yeah. So it interfaces with their current architectures, which today go 48 down to 12. And for some people it's 48 down to 6. Uh, and so those folks want a 800 down to 6 converter. Um, and the reason is that you want to keep that voltage as high as you can so you don't have load line losses getting to your GPU. There's a lot of current. I mean, GPUs are taking 2000 amps. So, you know, there's a lot of, a lot of current running through there.

**Dave Jones:** That's just nuts. So your board is 6, 6, yeah, let alone what we need in, you know, a couple of years time. Um, so your board is 6, it's going to 5,000 amps. Your board is 6, 6 kilowatts. 6 kilowatts. Look at it. Look at it. That's just crazy. Oh, man. So is, is there any, um, other stuff you wanted to share? Like, um, screen share or?

**Alex Lidow:** Well, I'll share some other things. I mean, you know, our ICs are getting real popular. So we're, we're going on to a lot of robots. Here's a, a shoulder joint, a shoulder motor control. Oh, and you see those three shiny things. Those are ICs. Yep. And that,

**Dave Jones:** those are either half, they're either a half bridge or a full bridge or?

**Alex Lidow:** They're a half bridge each. So three of those makes it three phase. Ross's DC motorway. But in our next generation, we're actually integrating all that into one chip and shrinking it dramatically. So, you know, you don't even need three chips in the next generation, uh, as well as a bunch of the shrubbery will be in there. So this is, uh, you know,

**Dave Jones:** the shrubbery is that the shrubbery, you mean the actual passives around it or?

**Alex Lidow:** Yeah. The passives, the current chunks, that shrubbery.

**Dave Jones:** Shrubbery. That's a great term. I love it. Shrubbery. That's all it is. That's terrific.

**Alex Lidow:** It's easy stuff. Oh, that is. So that's, that humanoid robot is a big part of our, our future, uh, as a humanity. Right. And of course, coupling it with AI makes both, uh, good news and bad news, right?

**Dave Jones:** Exactly. So all of the major humanoid, or not, not, not just humanoid, but there's, you know, the robot dogs and there's all sorts of, you know, we're in a robot future. So they're telling us, um, are all the companies using your GANs because they're the best?

**Alex Lidow:** Well, the good ones are, the not so good ones aren't.

**Dave Jones:** Right. It's just as simple as that. Yeah. Oh boy. So, so have you seen any of this humanoid robot technology firsthand?

**Alex Lidow:** I've seen most of them. Yes. I've seen most of them. Oh, okay. And are they,

**Dave Jones:** do you think they have the future that everyone's claiming?

**Alex Lidow:** Yeah. I'm sure they do eventually. It's just a question of when. Yeah. Because the robots that, that you see in the flesh, if you will, a little creepy to say that, but those robots are nowhere near as good as the videos that you see. Right. And really what you're seeing in those videos are, uh, robots either being teleoperated or using subroutines. They've got subroutines that you trigger a subroutine, but it's not really AI in any, uh, useful way.

**Dave Jones:** No, no. The hardware's there, like the robotics hardware is so impressive these days. It's absolutely incredible. All the actuators and, and stuff they're doing, the articulation stuff. But yeah, the, the AI is the, you know, the actual intelligence to drive the thing is going to be the sticking point.

**Alex Lidow:** Yeah. Uh, the mechanics I think will become fairly straightforward. I think GAN is the best way to do those mechanics for a lot of reasons. Uh, and you know, many of these robots have hundreds of our parts on them. Uh, and I think that will, that will continue. Hundreds. Yeah, yeah. Oh, of course. Oh yeah. Cause you've got the fingers

**Dave Jones:** and joints and, yeah, yeah. it's crazy. Wow. So what is your most popular GAN? What is the big seller? Like, do you actually have one in, in particular? Well,

**Alex Lidow:** the big sellers right now are the hundred volt primary side to an LLC and the, uh, uh, 40 volt secondary side. Part numbers are 2361, 2367. Those would be a hundred volt and then 2366 on the secondary side, 40 volt. And then our, our big sellers for, uh, humanoid robots are 23102 and 104, which are those integrated power stages.

**Dave Jones:** What total volume are you guys doing these days?

**Alex Lidow:** Well, we're doing millions per month. Uh, we're private companies. So we don't give a whole lot of public information. Oh, okay. Yeah. Fair enough. Very rapidly. Yes. Very rapidly. And, uh, you know, and our key areas are, you know, humanoid robots, artificial intelligence, um, uh, uh, autonomous machines in general and space electronics. And I think all of those are pretty important in our future.

**Dave Jones:** Yeah. They're, they're going gangbusters. They're huge. So the future is bright. Um, almost too bright because one of the things we lament in the industry is, oh God, somebody has been bought out by somebody and, and it's just, everyone gets like, there's so few left. There used to be, you know, all of our favorites are now being gobbled up. I assume you guys are going to be a target sooner or later. If you haven't had a tap on the shoulder already. Um, maybe you can't talk about that,

**Alex Lidow:** but our advantages, we're a small company, so we can iterate quickly. You know, we're in our seventh generation. We're, you know, getting ready our eighth generation and we're, uh, you know, starting on our ninth generation. When other people are still struggling to meet our fifth generation. So, um, you know, I think that that advantage of fast cycles of learning when a technology is relatively immature, uh, is a fundamental advantage. Now, once it matures, it becomes a cost of capital game. And the minute it becomes a cost of capital game, it basically, you better be a big company or you're dead. Yes. So, that's a lesson learned from my past.

**Speaker ?:** Uh,

**Alex Lidow:** and I, yeah,

**Dave Jones:** I noticed that you guys have in your portfolio have pretty much a demo board, like in a demo board for each part. Is that right? That like an eval board.

**Alex Lidow:** And so we have eval boards for not, not only every part, but we have eval boards for anything you can imagine. Uh, let me, let me give you an example here.

**Dave Jones:** Because your markets, I'm just going through your markets that you've got on the, you've got automotive data center, robotics, industrial, aerospace, defense, consumer, med tech, communications. It's like, wow. Yeah. You've covered,

**Alex Lidow:** you know, we've got, we've got also, you know, all these demo boards for humanoid robots. Uh, so now you probably can see it coming up. There you go.

**Dave Jones:** There we go. Got it.

**Alex Lidow:** There's our Da Vinci guy,

**Dave Jones:** right? Company confidential folks, company confidential. You're going to have to sign an NDA.

**Alex Lidow:** Uh, no, I'll, I'll, I'll waive it for this because, you know, there's arms, uh, there's, there's, you know, arms and, uh, there's fingers. And then there's torsos and each and every one of them not only has a device on our roadmap, but they all have reference designs for every single joint. Uh,

**Dave Jones:** every single one, you can get the demo board, you can get the reference design. Uh, are they available in a CAD format so that you can just pull it straight in?

**Alex Lidow:** Altium files. They're available in DigiKey. Uh, we, we try to make it as easy as possible. Here's an example. I showed you one earlier. This is available on DigiKey. Uh, you can buy this.

**Dave Jones:** it is great. Yeah. How much is that?

**Alex Lidow:** Um, I don't know. That's a good question.

**Dave Jones:** Find out. I'll put a link down below.

**Alex Lidow:** It's a lot of money, but it's worth it.

**Dave Jones:** It's, it's worth, oh, the, the eval boards seriously are worth the money. And they're generally not expensive, you know, 50 or a hundred bucks or something. It's not.

**Alex Lidow:** Ours are more than that, but yeah. Right. Okay. I'd like them to be that cheap for somebody, but they're not. Um, but, uh, you know, and look, uh, you don't meet, you don't need many demo boards, uh, to figure out how to make your robot work. So that's the goal there.

**Dave Jones:** That is, that is fantastic. Well, I think our amp hours up, Alex. Thank you very much. I'm joining this. This has been fascinating. We've had the history. We've had, um, the semiconductor physics we've had, um, and industry stuff. What fun. I mean,

**Alex Lidow:** this is what, this is what I love to do. They say that if you love what you do, you don't work a day in your life. And, and that's the way I look at it.

**Dave Jones:** Exactly. Oh, that's, that is good stuff. Um, where can people, can people follow you personally? Like, are you on X or, LinkedIn? I'm on LinkedIn.

**Alex Lidow:** You can follow me on LinkedIn.

**Dave Jones:** put the link, like, like do you publish articles or stuff like that?

**Alex Lidow:** all sorts of stuff. We do blogs and articles and, uh, podcasts and, uh, uh, you name it. And, uh, you know, we, uh, we do what I call darken the digital sky with information.

**Dave Jones:** Oh, whoa. Well, that's ominous. EPC folks.

**Alex Lidow:** Darkening the digital sky with, EPC.

**Dave Jones:** That should be a slogan down the bottom. Oh boy. That is great. Well, thank you very much, Alex. This has been absolutely fascinating. Thank you for your time. And for inventing the hex fit and the power MOSFET and everything else goes without saying. Um, that's just, it's been a joy.

**Alex Lidow:** It's been a joy the whole time.

**Dave Jones:** Awesome. Thanks, mate. Awesome. Thank you very much, Dave. Catch you next time.

**Alex Lidow:** All right.

**Speaker ?:** Thank you. Thank you.
