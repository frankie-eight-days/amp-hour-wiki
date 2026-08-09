---
episode: 682
title: Your Mind Is The Tool
url: https://theamphour.com/682-your-mind-is-the-tool/
---

**Chris Gammell:** This is The Amp Hour Podcast, released November 5th, 2024. Episode 682, Your Mind is the Tool.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Oh, hey, man. I have many problems I've been fixing.

**Dave Jones:** Many problems.

**Chris Gammell:** You know, there's life problems.

**Dave Jones:** Can we go through a list? Are we just going to go through a whole list here? Oh, I had a PCB that had a... We can solve your problems for you, Chris.

**Chris Gammell:** You cannot, actually. I've solved one. We didn't talk about this before the show. I had a board come back to me with a short that I didn't put into it. I'm not going to talk about the manufacturer, not naming and shaming, because it was rectified, but...

**Dave Jones:** As in a short between two traces that are close together, is that the thing? No. So it's an etching... No? No. So it's not an etching thing? Or it's not a defect on the PCB?

**Chris Gammell:** Board files were being modified by the manufacturer to add rails and stuff like that. And a via lost data, and it just got put on the wrong layer.

**Dave Jones:** Oh, wow. Or just a glitch in the matrix. Some sort of cosmic ray thing came through. It must be a cosmic ray came through, and whoop, via moved.

**Chris Gammell:** Yeah, I don't think that's what it was. But here's the thing. Maybe you could tell me. I don't know this. I put it into a bunch of different, like, Gerber analyzer tools. So all I had to work off of was my files, which were, of course, perfect. And pristine, yes. Yeah. I've never made any mistakes. I definitely didn't put a bunch of the wrong components on there, which was a red herring for all the troubleshooting. But then I asked for the Gerbers back, because I knew they'd been modified. That's fine. They were sending out some manufacturing.

**Dave Jones:** You need one of the Don't Touch My Gerber t-shirts.

**Chris Gammell:** Yeah. Yeah. And so I looked at them, and I had to do it manually, because I just, you know, there's like Fab 3000, Fab 5000. There's a bunch of, like, higher-end tools that do Gerber analysis.

**Dave Jones:** Oh, yeah.

**Chris Gammell:** But the thing is, they don't have net name knowledge, right?

**Dave Jones:** So they just test, is this too close to that?

**Chris Gammell:** And it's very, very useful. But it's really for the protection of the board maker and really the edge process. That's the real thing that they're testing. And it's like, okay, fine. But when it's two nets that get shorted together, not of my own making, you know, the nets kind of all tie at the Gerber stage, right? It's like a downsampling of information. And honestly, Dave, I asked myself something I never thought I'd ask, which is, is there an AI tool that would fix this for me? And the answer, of course, is no. Honestly, what it was is, like, you know, I used the AI tool called My Brain, the AAI, the artificial artificial intelligence. And literally, I was just clicking between layers, clicking, clicking, clicking, you know, on, off, on, off. I set them at, like, different, like, opposite colors. So, like, blue on one layer, yellow on another, red on another, so that you had, like, the maximum amount of contrast, like, different parts of the color wheel, because I'm blessed with all the colors in my eyes. And it took about, you know, three hours of just the worst, the worst Where's Waldo session ever.

**Dave Jones:** So, how did you find this? Did the boards come back and two nets were shorted? Is that the...

**Chris Gammell:** Exactly. Right. Okay. So, it started so that my... So, like, my... The thing that is basically, it was, like, a power rail being generated through a, you know, a switching supply, like a buck converter. And it had protection on board. And the protection was firing, but there was no indicator of it. It was, like, a silent failure, where it was just, like... Right. There was no rail there. I was, like, okay, well, something's wrong.

**Dave Jones:** And something's wrong with your switch mode, yep, and you investigate. Right.

**Chris Gammell:** And then I... This board was at the stage where I'm at the neurotic stage, which actually, it was not neurotic enough, where every net, every different net that I was connecting together has a zero ohm in line. And then, yeah. So, then I started removing those. And then I finally got to the point where I had a net that was both on the top copper and on the inner copper, well, on the power plane. And so, like, and then those two groups were, you know, I was doing continuity testing to the ground layer and just, like, 0.0 ohm sort of thing, you know, like, just really, really low impedance. And then... So, did you actually trace...

**Dave Jones:** Did you trace down with the ohms where the actual short was? I couldn't...

**Chris Gammell:** I couldn't even... So, here's the real jam.

**Dave Jones:** Yep.

**Chris Gammell:** Um, I could not get it to do anything. So, I ended up dumping 10 amps into the board. I bought a thermal camera. I bought a thermal camera because I couldn't find my old one. Dumped 10 amps into the board at 3.3 volts.

**Dave Jones:** I'm laughing because I've been there and done that. Oh, totally. Totally.

**Chris Gammell:** And, like, and, like, this thing didn't light up at all. Like, just not a single... And I was like, at this point, there's no other real option at that point. You know, like, even a zero ohm resistor is going to light up like a Christmas light, right? Yep. I mean, it's just going to have some amount of, like, basic resistance there. Unless I had so many zero ohms in parallel that I would just, like... But even then, you'd see some current, you know, just any... Like, this is just, like, flat affect all the way through. So I knew it had to be buried. And that's when I started looking at Gerber's and really just desperation.

**Dave Jones:** Right.

**Chris Gammell:** Wow.

**Dave Jones:** This is where a six and a half digit meter comes in. Five and a half, six and a half digit meter. You can trace down shorts like this.

**Chris Gammell:** The ohms just get lower, lower, lower. Should have called you a week ago. I have a six and a half meter. I have done a video on this. I have a six and a half digit. I have one.

**Dave Jones:** I've done a video on this. So, yeah. Should have done that.

**Chris Gammell:** I didn't think about that. Yes. That's not a bad idea.

**Dave Jones:** That is the use of... Because you don't care about the absolute... Yeah, I used to work on a micro-oh meter, too.

**Chris Gammell:** I mean, they had a micro-oh meter. And, like, that is basically what it is. Like, you would usually hire current, right? Yep. And they do that for, like, rivets and I don't know. Yeah, yeah.

**Dave Jones:** Cool. Yeah, stuff like that. Yes, that is one of the uses of a high count meter is so that you can get fine enough resolution so that you can actually, you know, trace around the board and narrow down the short. It's very helpful.

**Chris Gammell:** Yeah. So, yeah. That's a good one.

**Dave Jones:** But you need really sharp probes that are repeatable each time, et cetera. Yeah, I don't know. You've got to get through the oxide coating, blah, blah, blah. I mean, that's the thing.

**Chris Gammell:** I'm not calibrated either. I guess it wouldn't matter too much, but I guess it's just consistency over time, right?

**Dave Jones:** Exactly. You're just looking, does the value go up or down? So, you know, hot or cold. It's like a heat map or a gradient. Yeah. Yeah. So, yep. And, yeah, it works well. So, that's a bummer.

**Chris Gammell:** Nothing felt like it was going to work well in this case. And it was on the inner layer too, so that's the thing. Oh, right. Yeah. The majority of the current was flowing, I think, on the inner layer. Oh, damn. It was just, there was a net tie from the top layer.

**Dave Jones:** And then the thermal insulation of the PCB wasn't showing it up on a thermal camera.

**Chris Gammell:** That's right. Is that right? Yeah. And, I mean, it's not like, I didn't buy a high, you know, I bought a $200, like, smartphone attach. I used to have the Seek Thermal, which I was surprised.

**Dave Jones:** Oh, yeah, yeah, yeah, Seek one, yep.

**Chris Gammell:** I was surprised they still make those. They still, or they still, we're on Amazon, I guess, is probably a better way to say that.

**Dave Jones:** Fluke have a new one, I think. They've just released like a shoe phone, one that plugs into your shoe phone.

**Chris Gammell:** Yeah. I got one. I don't, I got some Chinese brand one. Yep. For 200 bucks. All right. Not bad. Not bad. I mean, once, here's the thing, once I drilled out the Via, I found a lot of current. Oh, boy. It was, it was a heart, it was a heartbreaker, though. Yeah. Right. That was, that was a stinker.

**Dave Jones:** When I was a boy, back in my day, it wasn't Gerber issues like that. It was PCB manufacturing issues. Totally. You know, over etching, you get a bit of contamination on your board or on the film, which they use to expose the boards. And yeah, and you'd get shorts between two traces. Or when you get a roll-soldered board. Have you ever had a roll-soldered board where they put the tin plate, right? The tin plate gets rolled onto the copper and then they put the solder mask over that, right? These days, it's solder mask over bare copper, right? S-M-O-V-C. But no, when I was a boy, it was a solder mask over rolled solder. And that's when, have you ever seen those green solder masks that peel? You know, they like peel off and they go all wrinkly and all sorts of stuff. Or they actually look wrinkly? Well, if you look in any 1970s, 1980s boards or something, you'll probably find that. Because I was sold a mask over solder-coated boards. And then when you roll, so a big roller goes over the board and coats all of the tracks. But it was very common to get a little solder dag between two fine traces that were next to each other. And yeah, tracing those things down was a pain. Or you get, as I said, on a film, you'd get an etching problem. And you get a bit of dust comes in on the film sheet, settles on the film sheet. And that actually gets exposed on the board. And you get a little hairline short between your two tracks, you know?

**Chris Gammell:** I feel like at 10 amps, you'd start to really clear those shorts. Oh, yes, yes, yes.

**Dave Jones:** You can actually blow them out, yeah. Like fuses, you know. Yes, that is a common technique. You can actually blow it. And then you're left with a little carbonized trace, which may come a gutter six months later. Yeah, right, right, right. It will certainly fix the problem then and there.

**Chris Gammell:** So here's the other question. So, you know, you always see like on PCB manufacturer sites that like, oh, we do like 100% e-test, stuff like that. Yep.

**Dave Jones:** But that's – 100% e-test is not 100%. They can't test every possible combination. All they test is the continuity between the traces and maybe some isolation between other traces. But generally, they can't test everything. Right.

**Chris Gammell:** And like, yeah, they wouldn't test like – yeah, they wouldn't have like a branching tree because a complex board would have like – Yeah, million. Effectively infinite – not effectively, you know, but like really, really expensive time-wise. Time-wise, yes. And so – but what I was wondering, like again, they don't have knowledge even of – like they know it's a ground plane.

**Dave Jones:** What they need is AI, Chris. We can start up an AI company that does e-testing.

**Chris Gammell:** We just raised $50 million just in this last 30 seconds.

**Dave Jones:** We can do it. Yes.

**Chris Gammell:** Oh, my God. Yes.

**Dave Jones:** Straight to start engine for us.

**Chris Gammell:** So like they never know. I mean like they know but they don't need to know and they don't really care that like the, you know, layer three – layer two was the ground plane, right? Right. And it's like – would that change anything? Would they then do flying probe between, you know, a top side trace and ground? Like that's what I'm going to do as a user, as the designer.

**Dave Jones:** You would probably have to tell them to do that. I would – I don't think it's part – it might not be part of the automated process. But every manufacturer has different rules for doing that. Yeah. And you can actually program it. Like in theory you could go, right, one flying probe onto the ground plane and then the other flying probe onto every other trace that's not ground. And then see and check for shorts. But then like you've just – and then you've got to do that. Okay. You've got to do that for the positive plane. Okay. You've got to do that for the five different power planes you've got. Yeah, yeah, yeah. You know, it's like – and then you're wasting half your time anyway because the traces may not go over some of those planes if you've got split planes, et cetera. Yeah, exactly. I'm telling you, AI can solve this. Yeah, right. But – yeah, yeah. Yeah. Yeah, nah. Yeah, nah. Yeah, nah. So e-test, yeah, it's like it's something that, you know, they actually –

**Chris Gammell:** E-test, more like e-test.

**Dave Jones:** There's a reason that they chuck it on for free these days. Yeah, right, right, right. It's because it's very minimal. It's basically checking for any breaks between traces. Yeah, it's quality issues, right?

**Chris Gammell:** They're testing the little shorts that you're talking about, right? The hairlines. They aren't testing the hairlines.

**Dave Jones:** I think they're testing for hairline breaks. Sorry, sorry.

**Chris Gammell:** I just meant like, yeah, the crossover traces, like under-etch, over-etch type problems, right?

**Dave Jones:** Yeah. Yeah, I think under-etch won't show up because that'll be two traces shorted together. I don't think that'll show up.

**Chris Gammell:** Well, wouldn't you think an e-test would do – would look at like geographic, like, oh, trace 45 is next to 46.

**Dave Jones:** That's what we've been talking about. How many combinations are there? How does it intelligently know that these two are next?

**Chris Gammell:** Well, proximity actually does have – it does have limited scope, right? So if you imagine –

**Chris Gammell:** Like you're looking through like a lens at just different parts of the board. You could say, oh, well, trace 45 is next to 46. I'll test if they're shorted. Nope, move on. Yeah, but what if they're only – And you can see it all trace.

**Dave Jones:** But what if they only come near each other for one little tiny point over the entire board? Then do you bother? No, then you do it once, that's what I'm saying. Or do I only do it on buses, right? But, you know, yeah. Okay, well. Okay, I'm actually not sure.

**Chris Gammell:** I guess the real thing we should do is we should figure out what e-test is.

**Dave Jones:** Oh, yes, we probably should these days. Yeah. Okay, we'll get there.

**Chris Gammell:** Yeah.

**Dave Jones:** Does e-test on a PCB – See, now he's talking to AI. I'm asking Google, which is dumb. Yeah, there he is. No, I should actually talk to AI. On PCB search for shorts.

**Chris Gammell:** Dave uses Gemini. For sure. Tell everybody. Tell everybody. Dave uses Gemini. Ew.

**Dave Jones:** Has electrical probes used to check for shorts, open, resistance, capacitance, and other stuff. How much they do that and to what extent? I don't think so. Basically, if you're buying your $2 freaking board, right, which costs practically nothing with free e-test, I don't think they're doing much, dude.

**Chris Gammell:** I agree. No, we have not diverged on that point in the slightest. Yep. This is not a cheap board, by the way. Right, okay. Right.

**Dave Jones:** How many actual layers? How many layers?

**Chris Gammell:** It's a four-layer board. Nothing fancy. Right, okay. This is the thing, though. It was not a manufacturing issue. This was a design issue of not my own making as the designer. That's the tricky bit. So, I guess I should get one of those Don't Touch My Gerber shirts. I've never seen that. Is that one of yours?

**Dave Jones:** Yes, yes. I did a Don't Touch My Gerber t-shirt way back. Got it. Got it, got it. But I haven't put on various other stores yet. It's only on my original Teespring store, I think.

**Chris Gammell:** Yeah, I don't know. I mean, I do. I mean, so let's talk about that then, right? So, you know, in this case, the manufacturer was doing Rails, and they were doing some controlled impedance stuff because of just not publishing. You know, they're like, well, we don't really publish some of our specs, so we'll do it ourselves. Okay, fine. And I had very low requirements on controlled impedance, you know, like simple stuff. Okay. And, like, so no big deal, but then, you know, in this case, I could have been more particular about Rails and all that other stuff. And then, like, so then when you're doing Rails on a design like that, are you going back and forth with the manufacturer and saying, like, what do you need for the actual, like, multi-part, or sorry, multi-board design with Rails and stuff like that? Or are you just pushing it through based on standard panel sizes and stuff like that?

**Dave Jones:** Oh, I'm basically, I would always do my own panels. So...

**Chris Gammell:** Do your own panels. But, like, then how are you speccing that in for, so, like, a manufacturer wants to have a certain width of the panels, right? So they're doing a 900 millimeter, you know, Rails on their pick and place machine and stuff like that. So then how are you getting that initial info from them to know that you should be putting certain specs into your Rails? That's what I'm saying.

**Dave Jones:** Oh, okay. Right. Oh, geez, it's been a long time since I've done full, like, high-end production like that. But, yeah, basically, there are industry standards. There were Australian standards for this back in the day. I don't think, well, we don't have many bare-board manufacturers here left here in Australia. I think there's only two. Sure. Sure, yeah.

**Chris Gammell:** But even assemblers, there are more assemblers there, right?

**Dave Jones:** Oh, sorry. Assemblers, yes. Oh, yeah, no, there's heaps of assembly houses. But they'll pretty much do anything you want. They can handle anything. You know, it doesn't matter what kind of... As long as the board wasn't physically too big for the actual machine run that they have, they can handle anything. Because everything's pretty...

**Dave Jones:** It's got to be customized, programmed in. So it didn't matter if you used circles for your fiducials on the outside of your panel strips. It didn't matter if you used triangles or squares or whether or not you actually used copper or whether you used, you know, like, et cetera. They can just handle everything. It's all manual programmed anyway. So, you know, there is no standard.

**Chris Gammell:** But the thing I'm always, like, getting at is, like, you know, somewhere in my cheapskate brain, I'm just, like, I want to be... I would love to just know, like you said, the standards are good, right? I don't ever see those in my own work, but that's fine. And so it's, like... And so then you kind of... Some of the services that I've used and some of the different manufacturers I've used, none of them are, like, oh, you know, here's an example panel. You know, I could ask for it, but it's not like they're publishing on their site.

**Speaker ?:** Yeah, yeah, yeah.

**Chris Gammell:** No, no, no. That is really what I want. I just want an example that I can copy, and then I can just give me best practice... That's because everyone does everything different. ...so that I'm going to have the cheapest version. I want to have the cheapest version of all these things. Just show me the standard so that I can then say, that's not going to work for me. I'm going to pay more. You know what I mean?

**Dave Jones:** You're basically not going to pay more. It's going to be the same, because as I said, it's a manual process.

**Chris Gammell:** No, if there's people in the loop, there's always dollars. It's going to be more.

**Dave Jones:** Yes, but people are always going to be in the loop. They've got to program the machine initially. And it doesn't matter if you've used a standard. Everyone's going to use a different size panel anyway for various requirements. So really, there is no like, oh, the machine is already programmed for this particular panel size. I am not aware of anyone in the industry who uses, apart from the same manufacturer, the same company who manufactures the same products, perhaps. They might use a standard template between the different product boards. But apart from that, from company to company, no. Everyone uses a different panel size. Everyone uses a different fiducials on their panels. Everyone has different test strips. Everyone has different. Yeah, of course. Everything. Everything is totally.

**Chris Gammell:** I'm just looking for panel width. That's all I care about. Panel width.

**Dave Jones:** Maximum panel height. Give me a length.

**Chris Gammell:** Give me a width. Yep. I'll do metric. Yep. Don't worry about me. I'm a big boy.

**Speaker ?:** Right.

**Dave Jones:** Oh, boy. Yep. Yeah. No, sorry, dude. So. You're not going to save any dosh by asking for some standard panel size. They might give the illusion that you might be paying less. But in practice, it's not going to happen. Because it's the same amount of load for them. Yeah, that sounds right. Yeah, yeah. So, sorry.

**Chris Gammell:** That's all right.

**Dave Jones:** Speaking of sense.

**Chris Gammell:** Sounds like we are experiencing some of the. Wait a second. Wait a second. We are experiencing.

**Dave Jones:** The Twilight Zone. Some of the. No.

**Chris Gammell:** Most knowledgeable and experience in the industry.

**Dave Jones:** Oh, I was going to follow up. I was going to segue into the PCB one that I just posted. But, okay. We can come back to that. Okay. Yeah, we'll come back to that. If you want to go. Okay.

**Chris Gammell:** This is on our subreddit.

**Dave Jones:** We'll take a break from PCB. Okay. Yes, please do. Yeah. All right. Here we go. It comes from Pablo the Ghost Beater.

**Chris Gammell:** Yes.

**Dave Jones:** Okay.

**Chris Gammell:** Great question. Terrible framing. He says, Dave is truly one of the most knowledgeable and experienced in the industry.

**Dave Jones:** I've been around.

**Chris Gammell:** Dave's been around. Here's the thing. People know. I love Dave. He's great. Definitely knows some things. Most knowledgeable and experienced. I would like to point to our slate of past guests across the industry. And Dave is among the throngs of experienced people. Anyways, let's move past that. As I said, that much hot air and you might desolder some parts. Yes. So Pablo is asking, why haven't you designed more products?

**Dave Jones:** Well, I'll read his question verbatim. Okay. Because I don't want to.

**Chris Gammell:** Just skip that one part I already read. Okay. Okay.

**Dave Jones:** I've designed and sold several electronic projects in the past and I'm ready to dive back in. Glutton for punishment, I know. Yes, indeed. Hardware is hard. That was my insertion there. Recently, I've been revisiting some of Dave's classic videos on PCB design for manufacturing, the ergonomics of selling, the economics, the ergonomics. I might have also done a video on the ergonomics. The economics of selling hardware. Top tips for bringing products to market. Do-it-yourself product design and more. All excellent insights. One topic I'd love to explore is Dave. Yeah, yeah. Given his expertise, why hasn't he pursued more product design ventures himself? If someone with Dave's know-how isn't doing it, what chance does the rest of us have? My guess is that it's a conscious decision on his part, but I'm genuinely curious about the reasons behind it. Excellent question.

**Chris Gammell:** Allow me to speak on Dave's behalf.

**Dave Jones:** Go for it.

**Chris Gammell:** He doesn't want to. Yeah, no. Well, we've talked about it many times. Yeah, yeah. It sucks. And also, you know, finding a good marketplace for this sort of thing. The thing I want to get to is Dave's classic videos. Do you think they still hold up after many years, right? I think a lot of those videos were made at the beginning of kind of the maker movement type stuff.

**Dave Jones:** Yes. No, they still hold up. The economics one, I think, still holds up.

**Chris Gammell:** I think some of the expectations have changed around the pricing of goods and the capabilities of the things that are contained within. So, like, to take the microsupply as an example, right? I feel like, not the microsupply, sorry, the microcurrent. Like, that is at a different phase than when it started. It was like a capable – it is still a capable thing, but it's like there are many other products that have entered that marketplace.

**Dave Jones:** Yes, yes, they have. There's like – I've personally got like four others, I think, here that do a similar thing and more. Right. Yeah.

**Chris Gammell:** So, like, that's what I mean. Like, some of it was, you know, serving a certain part of the market and the pricing that was available at the time. But it doesn't discount the usefulness of that product. It's just that if you launch that today, would it have the same impact and marketplace? I'm not sure. What?

**Dave Jones:** No, it's – exactly. All things change.

**Chris Gammell:** Right. So –

**Dave Jones:** But that doesn't change the question was the advice. Your question was do you think the videos have changed? No. No. The relevance of the videos –

**Chris Gammell:** If the pricing was 4X bomb or something akin to that kind of thing – Yeah. And the marketplace doesn't bear the –

**Dave Jones:** But that's always been the case. But that's always been the case. You have to play to the industry. If there's already an existing product in there and they can buy it on AliExpress for $10 and you need to sell it for $50, then, you know, you probably, you know, you might have – and it's popular. Then – and it's popular and well – the existing one's popular and well-known. Well, obviously, you're trying to push brown stuff up a hill with a pointy stick, right? Right, right, right, right. It's, you know, it's hard to break in.

**Chris Gammell:** Yeah, I just think – yeah, I guess you're right. Like product research and like seeing – like finding a niche in the variety of electronic products that might be out there, that is probably a prerequisite for all things before even watching those videos, right?

**Dave Jones:** Things haven't changed. Things like trust, things like brand recognition, name, you know, is your product the name in that particular niche, you know, things like that. Those things haven't changed. Sure, always the –

**Chris Gammell:** And the room for me is just China and the availability of hardware and the like – and just how hardware was manufactured 15 years ago versus now and just the availability of things too. Like just there's a lot more people in China on AliExpress serving needs that are potentially –

**Dave Jones:** There's a lot more like assembly houses. When I did those videos, there weren't those, you know, all-in-one solutions. You can go to your JLCs or your – Sure, exactly. Your whatever PCB ways or whatever. And they will practically do a turnkey for you with minimal risk. You know, you've got practically minimal risk. And they'll do the complete – and they'll do the component sourcing for you. And it's like, well, do you – and then you get tempted into – depends on the complexity of your actual product. But then do you get tempted into using their tools and their parts and their bomb parts, for example? And then they can produce it even cheaper again if you do all that, right? Because they've already got those reels, you know, lined up in their pick-and-place machines. They've already – you know, so if you use their suggested parts, then, you know – But it depends on the flavor of your product. Is it all generic parts and the magic's in the software? Or is it, you know, something like my microcurrent, right? As simple as it is, you can't substitute the parts in that, right? They're all precision. Like, you know, 0.05% resistors. They're all – you know, you can't just substitute the op-amps, right? It just doesn't work, right? There's only single source for these things. A single resistor on there was like $3, right? And it's really the only one. There is no substitute. I mean – Right.

**Chris Gammell:** I think – yeah. No, I agree. Especially in the test and measurement industry, I think like basically the moats as they are, right? The things that are keeping out competitors are, you know, bespoke supply chains that are – that maybe you only have access to. Right. Or testing methodologies that other people are unwilling or unable to do for, you know, being able to calibrate to a certain standard, that sort of thing.

**Dave Jones:** Right.

**Chris Gammell:** So that's – yeah, that's a good example of kind of – that's like a value add on top of – you know, if it's just a pile of parts, okay. But pile of parts plus Cal plus, you know, sourcing knowledge plus some magic sauce in the firmware and brand and like all those things. Yeah, those all kind of add up. Yes. Right. I agree.

**Dave Jones:** Anyway, I will answer Pablo's actual question, which is why – Yes, please do. Why don't I do it anymore? Yes, it is a conscious decision on my part because I have a blog to run and I have a family and I have other things, you know, going on. And I've got to maintain all these things and I don't have an infinite number of hours to do them all. And as I said, hardware is hard. Like as in number of – not just, you know, hard to actually design the things but the effort, the number of hours and the effort required to put into it is incredibly lengthy. And I don't necessarily have the time to do that sort of thing anymore. And given that, you know, a good part of my product is selling products or a good part of my income is selling products on my store. But when I look at it, I'm going, well, all the time and effort, all the non-recurring engineering is called NRE cost, right? Which is the time and effort you need to not only design it but then build the test systems. Even something simple like my microcurrent. You've seen – I'm sure Pablo has seen all my design videos on designing the panels and the test fixtures and the test products and, you know, all that sort of stuff to go along with it, right? It's not just the product. Although you can leave these things up to other people but it depends how much you want to control of it. Yeah, but then you lose the competitive advantage. You lose competitive advantage. You lose control, et cetera, right? So, yeah. Anyway, but – and again, it depends on your product. If it's just a simple microcontroller on a board and it's all your software is the only thing that is the secret sauce, then, well, you get them to turnkey, make that for $5 and you sell it for $50 or $100 because it requires your smart software, right? Yeah. So that's much easier than doing some other product that requires extensive test jigs and test bed of nails, test systems and programming, you know, like all sorts of stuff, measurements and all that sort of thing. Anyway, so aside from the complexity of the actual product itself and how to get it to market, it is just – yeah, it's just a ridiculous amount of time and effort and I've got to weigh that up against whether or not it's worth it than just to take existing products like, you know, products from other manufacturers and rebrand them under my brand. It's far easier to do that and I can still make a similar or better margin. So it's a business decision as well. It's like, well, yeah, if I didn't have the blog and like if I stopped making YouTube videos and I stopped everything else, yes, I'd probably have the time and the inclination to design products from scratch.

**Chris Gammell:** Yeah, but then you don't have the brand oomph, right? I mean that's the thing. Exactly. That's the trade-off.

**Dave Jones:** You lose the brand oomph.

**Chris Gammell:** I think that's one thing that kind of pops out to me is like the difficulty of doing that as a one-man show is Dave has made a conscious decision to stay as, which is –

**Dave Jones:** Well, I was a two-man show at one point. Totally. And we can actually get into that. I actually had a full-time employee who was designing products full-time, right? And, yeah, so we can get into that. But the other reason is that – so that was run. The other reason is that when I'm designing my own products, it's kind of like my baby. It's my thing. And I often tend to drift in different – you know, I'm sort of halfway through the design and I go, oh, wouldn't this be good if I did it this way? And I went in this direction. And you probably saw that with my micro-supply series. I had three or four different versions of the micro-supply. Like that was just in the series that I was developing because, you know, like it's still a hobby for me, right? It's still – Right, right.

**Chris Gammell:** There was no monetary – like Dave's family wasn't going to not be able to eat if you didn't finish the board that day.

**Dave Jones:** Or there was no boss telling me – you know, when I was working in the industry actually designing products, yes, there was very little leeway. There was some, but there was much more rigid, okay, we've got this and it's not just your idea, Dave. It's like the company wants this. Yeah, there's a product spec. And there's a product spec and there's a whole thing that you have to work to. So you just grind away.

**Chris Gammell:** And your job is based on listening to the person who's writing that product spec.

**Dave Jones:** Exactly. And you've got to grind away and there's other people, you know, checking you, regular meetings and going, where are you at on the Gantt chart of this design, right? And you can't just –

**Chris Gammell:** Yeah, but you probably missed Gantt charts, right? Oh, totally. Yeah, probably. Yeah, yeah.

**Dave Jones:** You just – And, yeah, and so there was little reason to deviate. Whereas if it's your own product, if you're not rigorous enough, if you're not disciplined enough to follow –

**Chris Gammell:** I have some examples in this arena.

**Dave Jones:** Exactly. I'm sure we all do. So that is reason number two.

**Chris Gammell:** But the reason one is that I could chuck in on right now, you know.

**Dave Jones:** So I end up with half a dozen projects, half finished. And I assure everyone in our situation can say a similar story. Half a dozen products, half finished because you lost interest in it or you changed the direction of it. So you started again or you – you know. And by the time you get around to – so you never get around to finishing anything. So, yeah. It's tough. Because, you know, your ass isn't on the line, basically. Yeah. Whereas it is if you're working for the man, right? The man's kicking you up the butt every week at the design review meeting to finish the design and get it to market. Right? That's right. So, yeah. Whereas you don't have that when you're a one-man band. That's right. So, yeah. Anything that does pop out the other end is purely a hobby project for me. So, yeah. Yeah. So that's probably more of the main. But if you combine those two major reasons actually together, then that's why, yeah, I don't design and build my own products. And if you take something for the example of the micro supply, which I did took seriously, right? So I hired David to, right, and one, part of his job was to help finish the micro supply design and actually bring it to market. And you've seen the end, the almost end result, right? It's a really schmick-looking product, right? Everything was custom design. Custom design case, custom LCD, custom keypad.

**Chris Gammell:** You're also hearing some of the problems. Yes, yes.

**Dave Jones:** Custom heatsink. And I've done videos on all these things, right? And the end result is actually a really schmick product. But in the end, it was like, okay, yeah, we got to a certain point. And then David actually left and he went on to greener pastures, which is fine. But then I had to make the decision, right, do I finish this and bring it to market? Or do it, you know, it's almost there. Like I physically got it in my hand. It physically works, right? It looks really sexy. But do I bring that to market? And I just had a look at it and I went, yeah, we have to actually redesign the DC to DC. We have to redesign the custom transformer in it because we weren't meeting the efficiency targets. And well, I think I've got a sniff of other companies coming out with similar competing products soon. In fact, one of them halfway during the process of designing that, I can't remember the company, but they came out with a little, you know, switching micro supply thing. But it wasn't isolated. But it was, you know, it was like, yeah. So all these companies started. Yeah, totally. Right, yeah, right. Yeah. It was 80% there. And it was like, yeah, okay, my one's cute, but it's isolated. But my one was fully isolated. That's a decision I made that would make it unique to others on the market. But then I decided, well, does that really matter to people? And then I was thinking, oh, if I get rid of the isolation, then I can up the power and I can go for, like, you know, there's lots of flow on things that make it better. And then you start doubting the design direction. And then I added up the product. Then I costed it out. You know, I did the big bomb and the Excel spreadsheet and the whole, you know, nine yards. And it came out and I'm going, this is just my bomb cost. Oh, no. No one's going to buy it at this kind of price level. You know, yeah, sure, some people might. Yeah, I might be able to sell a few thousand. But is it, you know, because of just the hype and the brand name, right, EV Blogify did a video with the Kickstarter and everything else. Yeah, I might get a thousand or two people actually buy it. But, you know, looking beyond that, it's like, it's not really worth it. And having been involved in those several large Kickstarters before, yeah, it looks great when the money comes in, when it all rolls in at once. And then you realize that you have to actually build it and ship them and supply them and test them and then back them all for that money. And if you don't judge that right, it's like, yeah, I made, like, what was my multimeter, my 121 GW multimeter Kickstarter? It was like 650,000 US or something. Was it US or was it Australian? I can't remember. I don't know. But, you know, it was quite a lot of money. It had like two and a half, 3,000 backers or something, right? It was a lot of money. But how much profit did I make in the end from that? I don't know. You probably have to ask my account, but it's probably not much, right?

**Chris Gammell:** Yeah, and especially hourly rate. Oh, yeah, hourly rate.

**Dave Jones:** It's just, yeah. Sure, I'm still selling that product today, but still, yeah, it's like, yeah, it's hard. It's hard.

**Chris Gammell:** Totally. Yeah, totally.

**Dave Jones:** Yeah. But if you want to do it, so my recommendation to Pablo is, yes, definitely do it. It's not that you shouldn't do it, but you need the discipline to go into it. But discipline is so important. I have two things on that front.

**Speaker ?:** I'm just too lazy.

**Dave Jones:** I'm just like, I'm lazy. I change my mind all the time. There's no one kicking me up the ass, you know? Yeah. Well, man.

**Chris Gammell:** I tried to have Dave hire me as a product manager. He said no. Right. So here's the thing. So here's the positive spin on, so like all the things that Dave's saying right now, those are actually also kind of a moat, right? Right. So I'm using moat as in like a competitive advantage kind of term from the silly startup industry, but like that actually, from the trend that I'm seeing, you know, kind of in the IoT industry and similar, it's like kind of the building of the hardware, that piece of it is kind of the hot potato. And it's like everybody's passing around like, oh, no, no, you're going to build the hardware. No, no, you're going to build the hardware. You're going to build it. And so like people that are good at it, that get, that build that, they're not going to make like, they're not going to make like AI fundraising margins. You know what I mean?

**Dave Jones:** Right, right.

**Chris Gammell:** Like taking people's money kind of margins, but you know, like they could build businesses off of it and like they could, they could build decent businesses for sure. Right. Yep. There's, there will be headaches. There will be issues. Like there's, it's not without, but I think increasingly that, that knowledge, especially like for specialized products has been kind of handed off and just someone says, well, you know, we'll just send it, send it to Asia just as kind of a generic thing. It's like, okay, well that's, that is not enough. And you need to, you know, even, even if you're quote unquote sending it to Asia, there's skilled engineers over there that are shepherding the product through production. You know what I mean? Like it's anyway, so having that knowledge is a good thing to learn and to do and to have in your tool belt as a capability. So then I think it comes down to, so assuming you have all those skills, I think that it comes down to having the right product type and, you know, wanting to follow through with it, whatever.

**Dave Jones:** And as always the, one of the hard skills is knowing what the market is, knowing what the market wants, what the market will expect in terms of price and features.

**Chris Gammell:** Getting enough attention to like.

**Dave Jones:** And attention as well. Have people buy it, right? Exactly. Yeah, yeah. Exactly. How do you stand out? How do you, but advice to Pablo is yes, definitely do it. Cause it's actually easier and better these days. You have, it's cheaper and better resources available to you these days. So definitely do it. It's just have, have the discipline to stay with it, like focused on the product and treat it as a business. Treat it as a business. Don't, don't treat it. Although treating it as a hobby makes it fun, but then you've got more technology. Temptation like I do. I mean, don't take my example because I've got unique circumstances that most other people don't. Um, in terms of running a blog and, you know, doing other things, right? I've got unique sort of situations and I sell other products and I already have an existing brand. Um, you know, um, you know, and market and stuff like that. So yeah, don't.

**Chris Gammell:** In terms of, uh, motivation, I can give one piece of advice. Uh, you could live stream your entire design and then, uh, you're compelled to fix it. Oh, this is me, Dave. I'm saying I did this. Uh, and, uh, you could, you could show everyone all the mistakes you did, uh, which is something I did last week.

**Dave Jones:** Just turn comments off.

**Chris Gammell:** Just kind of, yeah.

**Dave Jones:** Well, one of the worst things, sorry.

**Chris Gammell:** You said not to do that. Uh, I wanted to talk about the mistake that I made though. Can you talk about the mistake I made at a PCB?

**Dave Jones:** Yeah.

**Chris Gammell:** Okay. Um, so I, I've been working on this design. I have a plugin board. I think I told you about mentioned on the show before. Uh, got the board back, built it up, nothing, another, another, another LED that refuses to light up. Uh, another, another one, another one added to the pile. Uh, turns out that I rotated the component, the connectors, despite them being perfectly lined up, they were rotated exactly 180 degrees. Uh, so add that to the, the pile of, of issues that I've, I've brought upon myself in the past. And again, another thought that I had there is there is no AI tool that would have fixed this for me because in this case it was garbage and garbage out my own garbage making. Right. Uh, and, uh, so every time, you know, every time someone comes up to me and says, Hey, Chris, try out this new AI tool. All I can think of is like, is it going to, is it going to save me for myself? I don't think there are tools that can save me from myself in this, in this manner.

**Dave Jones:** Okay. Do you know of any tools? No, there are no tools. Yeah. Your mind is the tool.

**Chris Gammell:** Yeah, there it is. Mm-hmm. I am a tool.

**Dave Jones:** I am a tool. Could that be the episode of the name of this episode?

**Chris Gammell:** Yeah, sure.

**Dave Jones:** Yeah. Or your mind, your mind is the tool.

**Chris Gammell:** I'm not sure I'm going to put my photo with that one, but sure. Right. Okay.

**Dave Jones:** Well, like I'm currently being working on a product. Well, at least, you know, it's in the back of my mind. I always sort of like fiddle with it occasionally. And I've, I've actually got the competition sitting on the desk right in front of me. I'm physically holding it now. I won't tell you what it is. Um, I think I might've shown it to Chris a long time ago, but, uh, yeah, that's how long I've been working on it. But anyway, it's a little, it's a little bench, a little thing that sits on your bench. I've got it here. And pretty much this is the only one on the market, but I want to do my own version of it. And I'm thinking, I keep tossing up between this. Well, in order to protect sort of, you know, in quote marks, protect the design at that mode, as you call it, um, between people, uh, you know, copying it or, you know, just making a cheap ripoff version, although this won't stop them, it just sort of makes it a bit easier whether or not I go for a custom LCD, a fully custom LCD in it, or do I use an off the shelf, you know, dot matrix thing and then have custom fonts, you know, like programmed fonts and all that sort of stuff. Well, on one hand, the custom LCD is lower power. It's potentially lower price per unit. Once you've got the NRE out of the way. Um, but it's less flexible. Um, so like in terms of actually the display, you can't change it if you want to, you know, if somebody has a better idea on what's the, you know, cause it would have open source the software or whatever. And, you know, people could change the fonts and they can do whatever, you know, and change this actual, uh, the look and feel and the functionality of the product. Um, if you've got a dot matrix, you can do that. But then that means just, well, anyone can just take it and make it kind of thing. And, and I would open source hardware it. So there's nobody says nothing stopping somebody else just making a cheap clone of it and, and undercutting me, so to speak. So, you know, do I try and protect that design by having custom LCD and making that hurdle higher for somebody to make a competing product or not? I don't know. So yeah. Yeah. Yeah. You know, there's all, there's all those decisions you've got to factor in.

**Chris Gammell:** I don't wait around for, for someone to tell me that a part's out of stock. I single source it by design.

**Dave Jones:** Single source by design. Yes. Yes. Yeah. But you can always go, go to a different LCD manufacturer, you know? So, or the dot matrix thing. Like there's so many like pin compatible ones and stuff like that. So you just choose one of the pin compatible ones, I guess.

**Chris Gammell:** I'm trying to remember what you showed me. I'm sure you, I have no doubt you did show me, but I can't for the life of me remember it. But I don't know. In that specific example, like that's probably not the thing that would sink or float the device, the product.

**Dave Jones:** No, it wouldn't, but it's something that, but it's something that I'm thinking about. Right. So, you know. Sure. Okay. I'll send you a link right now. Okay. If it ever.

**Chris Gammell:** All right. Cool. I'll look at it later. Yeah.

**Dave Jones:** Here it is. Incoming. Boom. There you go. There you go. I think it's really cool. And there's only one product on the market like it and it's quite expensive and I would like to make my own. I thought it'd just be very cool. Add some extra functionality perhaps. And yeah. Yep. So.

**Chris Gammell:** Oh, I do remember this. Cause we talked about this with the case. The case specifically was the thing that you. Yeah. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. I was going to do was like a bare board thing. So you could like, or like you could sell it as like a kit or you could just like manufacture yourself as like a bare board kind of thing. And it could sit on your desktop as a bare board thing and it would still work. And it's still, you know, it just looks like a bare board solution or you could.

**Chris Gammell:** Dave's not going to say what this is, but I think when you, when, when, and if you ever released something like this, they'd be like, well, what, this is not what I expected it to be. A release. Yeah.

**Dave Jones:** Right. Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** It's, it's a very niche product. It's very niche. It's very niche. Yeah. But I, I like it. It's just a really cool thing that I think every lab should have one.

**Chris Gammell:** Got it. Kind of thing. You know? Yeah.

**Dave Jones:** So, yeah. Yep. Because, uh, you, you, you might see it. Um, you don't, I don't know if you've checked Chris, but there are things on there. There are connections on the back that you can actually hook up external trigger inputs to it. So, yeah. Yeah. Yeah. I just, I just think it's handy. Well, we shouldn't keep dancing around what it is. I mean. No, no, no. Yeah. Anyway. Yeah. Anyway. Yeah. Do you go custom LCD? Do you go, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Generic kind of thing. What's the look and feel? Do you design it into a fully custom case? Do you use an off the shelf case? I've, I've done videos probably saying this in the past that often a lot of good projects start around a case. You, you see a case and you go, Ooh, I could make that into a product. That's the perfect form factor. That case is brilliant. So you sort of work around the case and you've got an idea for a product and you go, this is the perfect case for it. You know?

**Chris Gammell:** No. What you do these days, Dave, is you 3d print something. And then when you're finally going to production, the production house says, we can't build this, you dummy.

**Dave Jones:** We can't build this, you idiot.

**Chris Gammell:** This is a single, single thickness sidewall. What are you doing? This is going to cost you thousands, thousands of dollars.

**Dave Jones:** The mold is going to be hundreds, hundreds of thousands of dollars for this mold. Yeah.

**Chris Gammell:** So that's how I do it. Thank you very much.

**Dave Jones:** Oh God.

**Chris Gammell:** All right. Did we answer Pablo's question though? I think we did. I think so. I think so.

**Dave Jones:** There were two reasons why I don't have a slew of my own products and why. Didn't ask me this.

**Chris Gammell:** I must not be the most knowledgeable experience in the industry, I guess. Yeah. Despite having said that I designed more boards in the last week than Dave has in the last year. Years. Yeah, exactly. Yeah. Yeah.

**Dave Jones:** I know. I know.

**Chris Gammell:** What's your keycat doing these days, Dave? We should get back on a keycat for you. Nothing. No. Oh, rip it. I've been touching it. Rip it and rip it, man. Come on.

**Dave Jones:** There's been two major releases, I think, since I last touched it. And I haven't even laid out. I've never even laid out a board in anger on it.

**Chris Gammell:** Eight is great. Eight is great.

**Dave Jones:** Aida?

**Chris Gammell:** Yeah. Eight. I said eight. Oh, eight. Keycat eight. Keycat eight. It's great. Right. Yeah.

**Dave Jones:** Yeah. Yeah. Meh. Meh. Yeah. Whatever. But yeah, the other thing was just to finish that off is that, yeah, even when I decided to take it seriously and I hired someone, even though I didn't hire them specifically for that, but I got them to specifically work on it full time and they worked a long time on it. And I was like driving the project. It still didn't work out. So just for various reasons, you know.

**Chris Gammell:** I have thoughts about that too.

**Dave Jones:** Yeah.

**Chris Gammell:** What? You hired yourself, Dave. That's the real problem there. You know that.

**Dave Jones:** Oh, yes. Yes. I know. Yeah. Yes. Yes. Yeah. I hired him because I thought he was cool and I liked him.

**Speaker ?:** Yeah.

**Chris Gammell:** That's the thing. He's another Dave. Which is true.

**Dave Jones:** No, he did an excellent job. If you go take a look at my, if you look at my micro supply.

**Chris Gammell:** But you just said, I yield the lily on everything and I do this and I do this and I do this and that's what David did too. And that's, that's the problem. That was one of the problems.

**Dave Jones:** Well, that's because I let him. Right? Yeah. Yeah. Yeah. Exactly. I suck at management.

**Chris Gammell:** I guess the buck does stop with you. Yeah.

**Dave Jones:** No, the buck totally stops at me. I should have managed the thing better and I just suck at management. So, yeah.

**Chris Gammell:** That's okay. You're.

**Dave Jones:** That's why I've never been a manager.

**Chris Gammell:** I'm very knowledgeable and experienced as an engineer in the industry.

**Dave Jones:** That's why I've been stuck in the basement.

**Chris Gammell:** In the industry.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Can we, can we have, maybe the image for this show can be me sitting on a couch in the basement at my former job.

**Chris Gammell:** Like, like Milton? Like when he gets put in the basement? Yes.

**Dave Jones:** Milton gets literally put in the basement. I was literally put in the basement.

**Chris Gammell:** Oh, I've seen that photo. Yeah. Unfortunately, I think we've actually used that as an image on the show before.

**Dave Jones:** Oh, we have? Okay. Right. 682 episodes of Dave. I'm pretty sure we have actually.

**Chris Gammell:** Yeah. Probably.

**Dave Jones:** All right. No worries.

**Chris Gammell:** All right. So you wanted to talk about PCBs. Get back to PCBs.

**Dave Jones:** Oh, yeah. PCBs. Yeah. I put this on just before the show. Have you seen it? It's a Twittery post. I'm looking at it now. Yeah. Yeah. Even though you think Twitter's an evil place.

**Chris Gammell:** Yeah. Yes. I don't understand the post though. It says two layers is all you ever need. Two layers is all you ever need.

**Dave Jones:** Right. Anyway. Okay. Okay. Roo Mo. M-O-H-R is his name? More. More. More. Yeah. More. Okay. Roo Moore on Twitter, which I think I might've done a video on one of his questions before actually. Kind of rings a bell. Anyway. Yeah. So he just made this post with a screenshot of a PCB he's working on. It's a typical rat's nest thing. You know, it's got various parts on it. It's got a big dip connector.

**Chris Gammell:** GK8 has curved rat's nest now. I just found that out the other day.

**Dave Jones:** Oh, really? Curved rat's nest? That's very interesting.

**Chris Gammell:** Yeah. It's very interesting. It's like, oh, this is not what I expected. Sorry. Go ahead. Keep going. Keep going. Anyway.

**Dave Jones:** And then, and as you said, all his text was is two layers is all you need. Two layers is all you need. Two layers. He's trying to remind himself that basically I think he's employing. Got it. He's trying to.

**Chris Gammell:** It's a mantra. It's a mantra.

**Dave Jones:** He has kind of like a quarter routed the board and he's gone. I think he's just throwing up his arms in frustration going, well, I can't do this on two layers. This is, you know, like it's going to be a pain and it's going to be really hard. I don't think so.

**Chris Gammell:** It does. It does look pretty hard, to be honest. Yeah. But it always looks hard at the beginning of the rat's nest phase. It always looks. Yeah.

**Dave Jones:** Like he's laid out maybe one, maybe one fifth of the traces or something. Um, but the, the old adage is that layout is 90% placement.

**Chris Gammell:** Agree.

**Dave Jones:** Yes, absolutely. So I can immediately see based on, although it'd be handy if I can physically manipulate the parts and move them around so I can see the rat's nest changing. So it's hard to do on a single image. Yeah. Yeah. Yeah.

**Chris Gammell:** That AI, you know, like get, you know, have your eyes be like, oh, that looks like the best orientation. Right.

**Dave Jones:** No, I just physically move it.

**Chris Gammell:** As you rotate it, you rotate, you rotate. It's like the fewest number of lines that are crossed over. Yes, exactly.

**Dave Jones:** The fewest number of lines that are crossed over and blah, blah, blah, blah. You know, group, group things together into functional modules, et cetera. I can already see, I would rotate the big dip part there. I would rotate that 90 degrees perhaps, or I'd at least try it. Yeah. I'd at least try it. So, so he's got like some rats go in the full length of the board, which might be unavoidable, but you do those last. And then you might auto route those, those, those last few, or, you know, or who cares if you use, who cares if you use 20 Vs to get that one, that last signal right across the board. Right. As long as it's, yeah, I, there's no control in penis traces.

**Chris Gammell:** I should start making a key CAD sound to things that I've been learning lately. If you hit F, it finishes the trace. That's a new, a new thing that I learned, a new hot key in key CAD eight. Right. Maybe not even eight. I don't even know. I don't know when these things came in here.

**Dave Jones:** Right.

**Chris Gammell:** That's like a thing that's been in all time forever. I'm sure. If you hit F, it finishes the trace for you. It does like an auto route. Oh, right. Yes.

**Dave Jones:** I think that's called a smart, smart routing or smart complete or something in out in. I can't remember the name.

**Chris Gammell:** It's in key CAD now.

**Dave Jones:** Right. Okay. Yes.

**Chris Gammell:** That's right. 25 years later, we got it too.

**Dave Jones:** Right. Right. Right. Right. So, so you start, so, so you start at the pad that has the rats, that has the net on it and you start routing it and then you just press F and it finds a, it finds the finished. Yep. Yeah. So that, that is interactive auto routing. That is interactive auto routing basically. Yeah. Yeah. Yeah. Which is fine if you've got one or two traces left. Like, like you wouldn't do that at the start of your board design. No. That's just dumb.

**Chris Gammell:** I move everything. Right. I'm picky.

**Dave Jones:** Yep. Yep. And, and don't be afraid to rip up half of your board. Totally rip the thing up. If you think, oh, if I move this part over here, um, it's going to make it all better for me, which you should have figured out before you started the routing actually to begin with, which as we said, routing is 90% placement, but you know, yeah, I can already see that. But even if we left it as is, I think if he gave me this board, I could do this on two layers. I don't.

**Chris Gammell:** You should ask for it. Yeah. I bet you can get it for him. Yeah, I should.

**Dave Jones:** Yeah. But no, I can, I can see that there's layout. Yeah. I can see things being easier if maybe like the green, the, the green surface mount part on the top, I think it is, um, there, which is under the dip packaged part. I mean, that, that needs to be moved down for starters. Um, you know, down, down the bottom end of the chip.

**Chris Gammell:** Obviously we're looking at this and everybody else isn't, but. Right. Yeah. No. We will link in the post, of course.

**Dave Jones:** We'll link it in. But, um, yeah, I, I don't think this is a problem on a two layer board, but then again, some of the comments, um, under the Twitter posts were interesting. Some people were saying, uh, uh, what? Like go immediately to six layer. There's no price. There's somebody saying there's no price difference between two layer and four layer these days. That can't be true, has it? I haven't had a board made in a while, but that can't be true.

**Chris Gammell:** It's not, it's not significant. I mean, that's a, that's the real thing. Right. From two to four is not. I mean, okay. I'm just going to say I use JLC for like cheapy. I don't care about them boards.

**Dave Jones:** Yep.

**Chris Gammell:** It's like, it's rock bottom for pretty much everything, but like, yeah, you get to six layers. It's more expensive. It is an extra day or two, which is often, you know, time is the most expensive thing.

**Dave Jones:** And if you go into production, you will pay more for a full layer than you do a two layer.

**Chris Gammell:** Yeah. Yeah, exactly. If you're really, if you're really starting to, you know, crank volume, you will run into it. But I think, I don't know. Does your signal integrity matter? Are you doing RF? I mean, like that's the other thing too. Yeah.

**Dave Jones:** Well, there doesn't seem to be anything signal integrity wise on this board. Um, it just looks pretty generic sort of little, you know, system on module kind of thing.

**Chris Gammell:** I know this is kind of the thing that we're doing here, but like this kind of like quarterback, like, uh, what do they call it? Like armchair quarterbacking sort of thing.

**Dave Jones:** Like armchair quarterback.

**Chris Gammell:** I don't know. I wouldn't want someone to do that for my, like, I'm sure people do and have and will, but like, I don't know. I feel kind of bad, you know? Yeah. It's an interesting conversation piece. Don't get me wrong. Oh yeah. Totally. This is podcast fodder. Like we are doing this, but, but I feel, yeah, I feel bad about it. No.

**Dave Jones:** And, and there's somebody who said, oh, that's a six layer minimum. And it's like, ah, you go on. On what planet? No. On what planet?

**Chris Gammell:** No, I don't think so.

**Dave Jones:** Like, no, no. Hard no.

**Chris Gammell:** I have been noticing there's been like, so like Mouser has a layout show now.

**Dave Jones:** Oh, they got a lot, like a, like a podcasty thing, like a lot, like a YouTube channel.

**Chris Gammell:** No, they got a contest, like a contest. They have, they've been emailing me about this contest. Oh, okay.

**Dave Jones:** Right.

**Chris Gammell:** And then, uh, who else did it? Uh, John Teal from, oh, I forget his program's name. Yeah. I've just been seeing more like, oh, we're going to compare different people, like doing layouts and quicker. And I just like, look at like people doing like fast layout type stuff. And I'm just like, I, I would never, ever be able to compete. Like, I don't, I'm not fast at things. I'm not good at things. Obviously I make 180 degree rotation errors. Like, I don't know.

**Dave Jones:** Like, it's just like, I would have been very good at it back in the day, but I'm so, uh, like, you know, it's a skill that you lose. Um, totally. You know, it's a, you know, it is not like I couldn't get it back. I could get it back, you know, you know, days or weeks or whatever. But you know, when you're late, you know, when I was a full-time PCB design engineer, like doing it all day, every day. Oh yeah. You get really efficient at it. Yeah. You get really quick. It's just like, it's just like, it's a blur, you know? Yeah. Yeah.

**Chris Gammell:** You hit the zone, right? Yeah. Yeah. Yeah.

**Dave Jones:** Just totally hit the zone. Have you ever had a long, uh, drive to work? Have you ever had a long commute to work?

**Chris Gammell:** Define long.

**Dave Jones:** Well, like half hour, you know, 40 minutes or something. Yeah. My old Cleveland. Yeah. Right.

**Chris Gammell:** Sure. Yeah. Yep.

**Dave Jones:** Have you ever gotten home and go, I have no memory of doing that drive?

**Chris Gammell:** Oh, that's yes. Yeah. Way worse than that. I used to have night shift at Samsung at the fab. Right. So I'd be seven in the morning and I'd be like, yeah, get here. Yeah. Yeah.

**Dave Jones:** You were so used to doing that every day. You get used to knowing exactly when to change lanes, exactly when to speed up and slow down. Yeah. Exactly what time. And it's just all become second nature kind of thing. And, and, you know, it's just, oh, nobody could do it better. You know, like if you put somebody in that situation, no, they'd be you because you've done it every day, you'd be like a racing car driver. You know, you just so finely tuned in to that, you know, doing that thing. And that's what it's like to get into the flow of, you know? Yep. Yeah.

**Chris Gammell:** It is nice when you're in it. Yeah. Oh yeah.

**Dave Jones:** Yeah. Totally. And then you finish it and you go, whoa, how did I do that? And it was like, you know, like, whoa, you know, like, yeah, you just have a look at the final product and you have no memory of doing the whole thing. It's just a, you know, it was just a thing that you did by, you know, auto route kind of human auto route.

**Chris Gammell:** 682 episodes later, Dave, I have no idea how we recorded all these.

**Dave Jones:** Yeah, no, exactly. Yeah.

**Chris Gammell:** Nor what we said.

**Dave Jones:** How I've made three and a half thousand videos. Exactly. Something over. Yeah. 15 years. Yeah. Yep. Yep. No, it's just, yeah, getting the flow of it and yep, Bob's your uncle. Yeah. So anyway, our amp hour is almost up. So I'd like to mention this last one, which is good. Former guest of the show, Ian Scott Johnson, who has done a video retrofitting a OLED conversion to an Advantest R6581. I've got an Advantest R6581. I have no idea where this is.

**Chris Gammell:** What is this?

**Dave Jones:** Oh, it's in there.

**Chris Gammell:** The lighting secret? No.

**Dave Jones:** I've linked it in. It's a big purple thumbnail. Keep scrolling down until you see a video with the purple thumbnail.

**Chris Gammell:** Is there a title? What do you know that title was?

**Dave Jones:** Advantest VFD OLED conversion.

**Chris Gammell:** I see it there now. Okay, great. Right. Yep.

**Dave Jones:** And yeah, yeah, excellent video. Somebody on the EEV blog forum actually designed, figured out and designed a board that took the serial output internally from this eight and a half digit multimeter that went to the original display driver in there, which displays, which goes to a vacuum fluorescent display. And of course, vacuum fluorescent displays famously lose their brightness over time, right? So apparently this is a known thing in these eight and a half, you know, high end, eight and a half digit multimeter. So worth saving, right? You know, this is like a $5,000 multimeter if you can fix it.

**Chris Gammell:** Yeah, the guts, the guts are good.

**Dave Jones:** Yeah, yeah, yeah. The actual guts are good. The display, eh, not so much. So somebody on the EEV blog forum actually designed a conversion thing that, you know, he found like the serial data within the actual design itself. And then he decodes that and drives and converts that into a font on the seven segments. Oh, yeah. I see a little, really nice.

**Chris Gammell:** Arduino Pico. Yeah, a little Arduino or something.

**Dave Jones:** One of those little, yeah, processory boards. Yeah, protocol translator. That's great. Yeah. And it's just, it's a gorgeous look. It's a gorgeous solution. It's just really nice. So very, very comprehensive video by Ian there. So. Yes. I really like that. We will link that one in. Highly recommend it.

**Chris Gammell:** Definitely.

**Dave Jones:** And he's surprised on Twitter. He was surprised why that video was popular. And I went, dude, it's really good. Yeah.

**Chris Gammell:** That's good stuff. Yeah. I feel like that's like end to end kind of like problem solving, but also like kind of like designing retrofit. Got a lot of.

**Dave Jones:** Yeah. Yeah. It has quite a lot of aspects. It's like a complete project kind of thing. Yeah. Even though he didn't do the actual design of it, but he took somebody's design from the EEV blog forum and yeah. And actually implemented it on his unit. And yeah, it's great. So hats off. A lot of work.

**Chris Gammell:** Other things we should mention before we go. Jack Gansel. Congrats to him. Yes. Past guest of the show. He retired.

**Dave Jones:** Oh, did he? Oh, good on you, Jack. He did.

**Chris Gammell:** Yeah. Way to go. He's been kind of, kind of stepping out past year or two.

**Dave Jones:** How old's Jack now?

**Chris Gammell:** He's got to be, I think he was the same age as my dad, which is about 70.

**Dave Jones:** So I think he was very young and sprightly when he visited me in here in the lab, but that was a long time ago. So we can, we can link in that video. I've got a video of him when he visited the lab and when we had a good chat.

**Chris Gammell:** And he's been on the Amp Hour twice. So we'll link that in too. Um, yeah. Congrats to Jack. I mean, we, I've.

**Dave Jones:** Yeah. But is it retire in quote marks? Is he just not, not, not working for the man anymore? Is he doing anything on his own?

**Chris Gammell:** He was the man. So, you know. Oh yeah. Yeah.

**Dave Jones:** He was, but like, is he taking on contract, you know, like, wasn't he like doing contract jobs and stuff and things like that? No, no.

**Chris Gammell:** He's been, he's been doing educational stuff for years and years and years, like courses. And that's why he was in Australia. He was teaching a course there and, you know, he did management training, but he also did. Yeah. Yeah. Yep. Um, yeah. Expert witness, I think stuff like that. Yeah. Obviously his, his newsletter, which is the real. I mean, that's. Yes. Yes. That's the. That's the. That's the old and eight. That hit 500. That's where he stopped.

**Chris Gammell:** All right. Oh, okay. Yeah. Right. Yeah. Nice. Which is very, very impressive. That's like one, once a month for 20 some years. Yeah. Awesome. Hats off. That continuity is just, yeah. So impressive. So, so very impressive. That's incredible. Yep. Yeah.

**Dave Jones:** Well deserved retirement. Yes. Although I don't think he'll retire. He'll still do stuff.

**Chris Gammell:** Well, I'm going to maybe, maybe ask him three or four more times to come back on the show.

**Dave Jones:** Right. Okay. Yeah.

**Chris Gammell:** So roll up all the knowledge of this. Right. Long and storied career.

**Dave Jones:** We'll suck it all out. Yep. Yeah. Yeah. Yep. Totally.

**Chris Gammell:** And then one last not piece of great things. Ward Christensen passed away, unfortunately.

**Dave Jones:** Oh. Wow.

**Chris Gammell:** He was a listener and emailed a couple times with him. Yes.

**Dave Jones:** That's right.

**Chris Gammell:** Yeah. BBS inventor. Yes. And Xmodem.

**Dave Jones:** Yes.

**Chris Gammell:** And yeah. Ward Christensen.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah. One of the ones where, you know, should have gotten him on the show. That's a regret of mine. Yeah. We should have. Yep.

**Dave Jones:** He did Kermit. Didn't he do Kermit as well? The Kermit protocol? Or am I thinking of someone else? I think that's someone else. Okay.

**Chris Gammell:** I used that recently, actually. It was technically.

**Dave Jones:** What?

**Chris Gammell:** Yeah. Yeah. There is a motor manufacturer that has that in their directions. It's like, go to this site at, it's like Brandeis University. There's like some like New York City based like university. It's like some version of Kermit that's like, you have to compile from source. And it's just like, what the hell is going on right now? And that's the only way you could talk to the modem over the serial using Kermit. It's just like. Oh my God. That's great. Guys. Guys.

**Dave Jones:** It's not the 1970s anymore.

**Chris Gammell:** I know.

**Dave Jones:** Or even early 80s. Yeah.

**Chris Gammell:** I mean. Yeah. Whatever. It's anyways, we were. Yeah. So I was sad to see about Ward, but BBS, obviously just for runner of all things forum. PHPBB is what. Do you still run that, Dave?

**Dave Jones:** Yes. Well, no, I don't run PHPBB. I run Simple Machines Forum.

**Chris Gammell:** Simple Machines. Yeah. I mean, every forum software is based. I mean, it's a descendant of the BBS.

**Dave Jones:** It's the BBS style. It's BBS style forum.

**Chris Gammell:** Yeah. The mailing list format, that sort of thing. Yeah. So yeah. Would not be here today without Ward. So. Awesome. Sorry. Sorry to hear about that. Yeah.

**Dave Jones:** The hat's off.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. And speaking of which we should have had on the show, I'm very excited for this Friday. I have booked in Lee Felsensein. Yes. Who is one of the two big names in the early personal computer industry. You would either name Steve Wozniak or you would name Lee Felsenstein, the designer of the Osborne One plus the Soul Computer and others. And famously founded the Homebrew Computer Club. He was one of the founding members and the guy who ran all the Homebrew Computer Club meetings. So I'm very excited. Yeah. That's going to be great. I've got a new book coming out, which I've read part of it, but I have to read it all by the end of this week. And yep. I'm very excited.

**Chris Gammell:** Awesome. Can't wait for that one. That's all I can say. Yep. Yeah.

**Dave Jones:** It may not go for an hour. Like as in it may be over depending on how excited I get.

**Chris Gammell:** Whatever you can get, right?

**Dave Jones:** I mean that's the thing. Yeah, yeah. Exactly.

**Chris Gammell:** On this front as well, right? I mean since we're talking about Ward and Lee and just kind of Jack as well, right? Yeah, yeah. People that are greats in the industry. In the industry. If there's others that we should be talking to, if there's others that you know, if there's others that you've said, ah, if only Dave and Chris or one of them should have talked to so and so, we would love to hear about it. Please let us know in our comment section. Send us an email, feedback at theamphour.com. We just, you know. Yep. Time is a harsh mistress. Yes, it is. Some of them don't.

**Dave Jones:** Yeah, like there are some that I've tried to get on and no.

**Chris Gammell:** I find an email from one particularly grumpy old great.

**Dave Jones:** Oh, really? Oh, you'll have to tell me the name after the show. Okay. I will. I'll remember that one.

**Chris Gammell:** You know who does. Oh, do I? I probably do. Yeah.

**Dave Jones:** Okay. Tell me. After the show. All right. Anyway, we are done.

**Chris Gammell:** Yeah. All right. I'll catch you next time. All right, man. See you soon. Bye. Bye.

**Speaker ?:** Outro Music
