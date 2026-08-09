---
episode: 505
title: Hardware Revision Control with Kyle Dumont
url: https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/
---

**Kyle Dumont:** This is The Amp Hour Podcast. Released August 16th, 2020. Episode 505. Hardware Revision Control with Kyle Dumont.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Kyle Dumont:** And I'm Kyle Dumont of Allspice.

**Chris Gammell:** Welcome, Kyle. You know, when companies have Spice in the name, I usually get excited. You're either going to be about simulating something, doing something with electronics, or you're a Dune enthusiast. And all three are okay in my book. So which ones are you?

**Kyle Dumont:** So we're not Dune enthusiasts, unfortunately. We're also not. Okay, after the show, I'm going to tell you about Dune. So turn us around. I just started reading Seven Eves. So maybe that might be my gateway.

**Chris Gammell:** Okay. Yeah, that's a good one.

**Kyle Dumont:** Yeah, we're also not making food, which is the other one we get a lot. Oh, yeah.

**Chris Gammell:** Right. Oh, yeah. Because Allspice is like a thing. It's like a type of spice, isn't it? Yeah. It goes actually great in mulled wine. So do electronic circuits, if you're so inclined.

**Kyle Dumont:** Yeah. For us, it was really not surprising. It was kind of a play on what we see evolving in spice. Obviously, there's tons of spice tools that have existed since the 70s. You know, NG Spice was kind of like Nutmeg Spice. Obviously, you have LT Spice and others. For us, Allspice was kind of this great unifier of, you know, what we could do by bringing together all the spice tools. So a bit of a fun play on words for us. Yeah, that's great.

**Chris Gammell:** That's great. Well, before we do that, let's hear about your background. I mean, so you are a hardware engineer. You've been doing some interesting program at Harvard. Can you maybe tell us about that and kind of how you got to where you are now?

**Kyle Dumont:** So my background is in electrical engineering product design. I worked at iRobot for a few years doing both industrial products and then also the consumer products. I went from there to help start a 3D printing company called Voxel8. Some of the listeners or you might have seen, we had a pretty popular video that was trending for a while of a quadcopter flying off of our printer bed. Yep. Yeah, I remember that. We're actually 3D printing circuits.

**Chris Gammell:** Yeah, yeah. And yeah, it was like integrated with the actual, so it was like plastic plus circuits, right?

**Kyle Dumont:** Yeah, we had basically a dual extrusion system. So we were printing plastics and we were printing kind of a curable silver ink. Like we had a few different versions, but the most common version we had had a solvent that would dry out of the ink and just leave behind like a silver conductive trace.

**Kyle Dumont:** Yeah.

**Kyle Dumont:** We also had different versions with like epoxy bases and things like that. We did some pretty crazy stuff to try to improve the resolution and the print quality. We even converted our VF2 Haas CNC machine to be a 3D printer.

**Chris Gammell:** Got it. Really got to get that, those sub thousandth accuracy and stuff like that. Or something crazy.

**Kyle Dumont:** Oh yeah, we were down to 100 micron tracing space. Wow. Okay. We were doing like essentially micro machining using Haas VF2 and then we would backfill the traces in with silvers.

**Chris Gammell:** Oh, interesting. So you would make like a small channel and then that would basically be where you'd pour, you'd basically pour in the silver, the ink conductive kind of thing in there?

**Kyle Dumont:** Yeah, we experimented with a lot of different versions. That is definitely one we did. And we could do that actually to do, essentially you're just doing, you know, many, many, many layers of PCBs. But you can do them obviously with, you know, rapid, rapid iteration.

**Chris Gammell:** Yeah. I remember the video. I remember hearing about it. And then I remember, well, I don't remember what happened after that. So what happened with that company?

**Kyle Dumont:** Yeah. Things went quiet in the, on the circuits front. Well, it turns out that 3D printing electronics is very hard and we actually got sucked into 3D printing shoes. So athletic footwear.

**Chris Gammell:** As you do, as you do.

**Kyle Dumont:** Yeah. As one does. You know, nothing to do with, with circuits as it happens. Other than, you know, we use the same hardware. We use the same software to drive all the systems, but we swapped out all the materials for polyurethanes and used very similar processes to help bring in a rapid prototyping for athletic shoes.

**Chris Gammell:** Huh. Well, I think you missed a, a calling to bring back the LA lights. You know, those were really hip back, back in the day. And I think you really missed an opportunity to, to make those shine again. You know, I know.

**Kyle Dumont:** I think they're coming back though. Somebody mentioned that.

**Chris Gammell:** Yeah. Okay.

**Kyle Dumont:** If they ever left.

**Chris Gammell:** So I'm curious about the circuit stuff. So was there, was there interest in the marketplace and that sort of thing? I mean, I, I hope we didn't disparage it here on the show. I feel like that's something we would have been like, ha ha. Yeah. Right. But cause I remember I've said that about some circuit printing and stuff in the past, but it's, it was more like usually the, the phrase that was uttered between me and Dave, whenever we saw that kind of stuff was like, right. Well, Dave especially was like right tool for the job. Right. And it, there are some people, it seems like it does make sense for, but I'm not sure who those were.

**Kyle Dumont:** Yeah. And that was kind of exploratory for us as well. You know, the first printer we launched was called the developer's kit. And the whole idea is we'd put this thing out there and we could, we'd kind of see what sticks. And we did find some areas that had a lot of interest for doing, you know, one-off circuits and like a rapid prototype design, such as, you know, test fixtures were a big one, like, you know, ICT fixtures.

**Chris Gammell:** Yeah. That makes a ton of sense actually just to, yeah, you're all built together. Then you have a way to hold the board and you don't need to laser cut, you know, acrylic and get the pogo pin, the dance of the pogo pins and all that other stuff. Well, maybe you still do, but.

**Kyle Dumont:** Yeah, exactly. And in the other thing we were trying to tie in autorouters to that as well. Um, obviously autorouters are not super popular, but that's one kind of, it's one application where you're like, well, we have infinite layers and we just need to connect a bunch of, you know, connectors on the, a point on the bottom to a point on the top. And it was one scenario where we thought, huh, maybe, maybe an autorouter could work. And it seemed promising. We were also exploring antennas as far as like three-dimensional antennas and what we could do there. Apparently there's a pretty big surge, I guess in people, you know, 3d, 3d antenna companies, for instance, one was just, you know, massive phased array antenna designs.

**Chris Gammell:** Yeah. It's basically lets the, lets the math people go crazy and you're like, Oh, you have a third dimension now. Okay. Well, you know, go all fractal on it, you know? So, okay.

**Kyle Dumont:** Absolutely. It was, uh, yeah, it was over, over my head a little bit, but, uh, but it was, it was,

**Chris Gammell:** I'm sure there's Maxwell's equations, you know, and many, many, you know, teraflops of processing to do that kind of stuff. But yeah. Wow. That's, that's some crazy stuff.

**Kyle Dumont:** Yeah. Yeah. They were, they were, they were, they were pretty neat.

**Chris Gammell:** How would you, uh, so when you said like the multiple layers too, how were you connecting between the layers when doing this?

**Kyle Dumont:** Well, it depended on the iteration of the product, but for the simplest case of like the, the plastic and the multimaterial printing, plastic and silver printing, we would essentially print the, the plastic layer, leave a trough for the silver and then still backfill it with silver. We just wouldn't print over the top of any, any layer. So we would print basically a little via in a, Oh, okay.

**Chris Gammell:** Yeah. So basically like on individual layers, you'd have like a little circular cutout area and then that would look like a VO or similar, like a fillet or. Or, uh, whatever they're called.

**Kyle Dumont:** The other kind of cool thing is we got blind vias for free, you know, inherently because we're not doing a drill process through the entire, entire board. We're drilling as we go. If we were drilling or leaving a trough, if we're printing, you know, we got those blind vias for free.

**Chris Gammell:** And then what was the resolution you could get on that sort of thing?

**Kyle Dumont:** Well, I mean, that was one of the problems with the, the dev kit printer. We were still doing a FFF. So fused, uh, basically fused filament deposition. So it was, uh, you know, we had to basically print a plastic and then be able to fill that trough. So with that process, we were probably down to somewhere around eight, eight mils trace in space. And you, so certainly nothing that would even be industry standard, which is one of the reasons we ended up moving to, uh, to another industry as it happened. Yeah. But with the other process, we were able to get down to like a hundred microns.

**Chris Gammell:** Yeah. That's the milled, milled and like subtractive versus additive, that kind of thing.

**Kyle Dumont:** Yeah. And just using significantly more expensive pieces of machinery.

**Chris Gammell:** Right. Right. Yeah. That's, that's, I mean, that's cool. I mean, what about the silver stuff? So like how, uh, that was another thing that I always wondered about was like the connectivity seemed like a lot lower than copper, but maybe that was just the type that I was looking at. Like the, you know, the, the ones that I always saw were like the ink. There was another one, I think Volterra was one that was like a ink based kind of all in one thing. And that one really didn't seem like it seemed like an interesting idea, but it just, in terms of the capabilities, it didn't seem like it was there.

**Kyle Dumont:** Yeah. You do end up with some interesting properties, especially if you're doing anything high frequency in terms of conductivity, you know, it was something around the order of like one tenth, maybe, maybe one fifth of the connectivity of copper. But at the end of the day, you can just print, you know, because you're, you're printing this stuff, you can print it 10 times thicker and you know, you wouldn't even notice it.

**Chris Gammell:** Yeah. That's a good point. Yeah. And I guess if you don't care about most of the time, the Z height, you wouldn't think about, and especially if you, if you have control over each layer, you don't have to worry about like core and prepreg stack. I mean, you probably have to know the dielectric constant of the material in between and blah, blah, blah, if you're doing RF, but like, but you could control that much finer instead of having to go out and order prepreg, you just make your own effectively, you know? Yeah. Hopefully it's going to, you know, consistent enough over the spacing.

**Kyle Dumont:** Yeah. That's actually what we were doing when we were, you know, when we moved to the, uh, CNCs, we were actually printing epoxy glass loaded epoxy. So it was actually fairly similar to. Interesting.

**Chris Gammell:** Okay. And then you would machine glass loaded epoxy.

**Kyle Dumont:** Like I said, it was a dirty process.

**Chris Gammell:** Well, okay. And so is that company still around and still doing shoes and stuff like that?

**Kyle Dumont:** Yeah. Yeah. Voxelate. Um, they're doing shoes, uh, focusing on basically stylizing the uppers of shoes. So, uh, in the time before I did leave the company, I learned more about athletic footwear than I ever thought I would. So I'm sure there's maybe a sneaker head segment that I can join or something like that.

**Chris Gammell:** I have met some people that are like in that crowd. It's like, they're really into it. Like really, really, really, really. There's a lot of passion there. Yeah. I don't understand why though. I mean.

**Kyle Dumont:** Yeah.

**Chris Gammell:** I guess saying they're just shoes is like someone else, some coming up and being like, Chris, it's just electronics, you know? Okay. Yeah.

**Kyle Dumont:** I built my life around this. Yeah. Right. Right. Yeah.

**Speaker ?:** Yeah.

**Kyle Dumont:** Yeah. So they're, they're printing stylizing uppers. They're basically printing, uh, polyurethanes. One of the cool things was that they were able to use very similar bulk materials that the manufacturers are going to use when they actually manufacture the shoes for real. Whereas other processes like, uh, SLA was like, uh, select, uh, laser annealing. I think it stands for, you have to make something that cures with UV light. And then if you have something that cures with UV light, it's inherently not going to have the same properties that you might want to have in a production shoe. Right. So that's kind of their, uh, their current value prop, at least last, last I touched base.

**Chris Gammell:** Yeah. That makes sense. Okay, cool. So, and you were doing the control stuff there or what were you doing on that side of things?

**Kyle Dumont:** Yeah. So startup, it moved around a little bit, but when I joined, I had a team that was basically in charge of designing the desktop 3d printer, um, that dev kit that we launched initially. So it was pretty cool. It was, you know, very, very much what I would consider a robot, a lot of electromechanical parts. We had a pretty cool modular print head. So you could, we had like pogo pins, uh, that would connect to the print engine and you could kind of pop the cartridges in and out.

**Chris Gammell:** Yeah. Which the VCs love so that you can, uh, sell the, sell the cartridges like the, you know, everyone wants to be an HP or, uh, you know, uh, what's the cuff coffee maker? The, uh, Oh yeah.

**Kyle Dumont:** The Keurig.

**Chris Gammell:** Yeah. Keurig pods. Oh yeah. Yep. Yep. Disposable stuff is great for that bottom line.

**Kyle Dumont:** Yeah. Well that bit, uh, Stratasys and Makerbot around that time they had a, yeah, something called the smart extruder, but they got, yeah. Nobody liked it. Grief. Yeah.

**Chris Gammell:** Yeah. Yeah. Oh, well, I mean, 3d printing in general. I mean, like it really did have this rise. I mean, like it's obviously normalized now and it was institutionalized before, but like now like the hobbyist side is almost even institutionalized too. And it's just like, yeah, you know, you just buy a 3d printer. What's the question? Whereas like, you know, back cover many, was it six, seven years ago, whenever that happened, it was pretty hot. I remember.

**Kyle Dumont:** Yeah. There's the 3d printing industry has a lot of boom cycles. Um, it's still an industry that's trying to find that mainstream, uh, hook surprisingly actually like choose an athletic footwear has been one of the, one of the places the industry is going, but it's, uh, yeah, it's, it's struggling to find that mainstream.

**Chris Gammell:** It's limited. I'm sure too. Yeah. So they're going to keep trying other things. And yeah, the downside of, of course, is always the raster versus reverses like molding type of thing. You know, like it's just, it's, you know, they keep saying like, Oh, it's for production is for production. I'm like, Ooh, okay. Well, it's a lot faster to just mold things, you know, especially in plastics.

**Kyle Dumont:** Yeah. The quality can get there, but it turns out that jamming a bunch of molten plastic into, uh, into a mold is, is pretty cheap and pretty quick.

**Chris Gammell:** Yeah. Every time I talk to a mechanical designer to like quoting out like, you know, parts and like, yeah, well, the mold's going to be, you know, $10,000, something like that. I'm like, okay. Like, what's the, what's the part cost? And like two, two cents. Oh, oh, you mean like a big. Cap. Yeah.

**Kyle Dumont:** It's like that fixed. It's all fixed cost.

**Chris Gammell:** Yeah. Yeah. It's, it's pretty crazy and they can really crank them out. So yeah, that's plastics, huh? Okay. Well, that's a, that's a different game. Yeah. Anyway. Uh, what'd you do after that then? That was, that was before I robot or after?

**Kyle Dumont:** Uh, that was after I robot.

**Chris Gammell:** Oh, cool.

**Kyle Dumont:** Um, so from there I did a little actually independent consulting for electrical and firmware engineering, worked on a couple of cool projects and then, um, started at the grad school program.

**Chris Gammell:** Nice. Yeah. And tell us, so when you wrote some, when we started talking about you being on the show, you told me about this and I looked at it and like, this is the first, not that, not that I'm thinking about doing this and I don't think I actually could, but like, it was the first time I was like, Oh, that actually like that MBA program makes sense because it's not just an MBA program. So what is this thing that you just finished?

**Kyle Dumont:** Yeah, it was, uh, it's called the MS MBA program. It's essentially you're combining, uh, an MBA with a master's of science. I think that the master's of science is in a generalized engineering sciences, but you essentially get the custom pick what engineering classes you want to take.

**Chris Gammell:** Oh, cool.

**Kyle Dumont:** It's in two years, like a typical MBA program, they add in some summer classes and winter classes. So you kind of can, can get enough of those elective credits to, to get both degrees. Yeah. Most of our class, maybe not surprisingly focused in either data science or software.

**Chris Gammell:** I guess if you're into that sort of thing, whatever. Yeah. Yeah.

**Kyle Dumont:** But, uh, yeah, it was, it was great. There's a 30 of us in the program, although you're, you're pretty well integrated into the general like MBA, uh, class, which at Harvard was 900 people, give or take. So they kind of throw you in like the first year you're, you're doing kind of the standard core MBA program. And then the second year you get to more or less swap out some of your MBA classes with engineering classes, uh, which was perfect for me because, you know, the engineering classes were enough to, to sink my teeth into something while getting, you know, some good practical value and networking and, and all of the things you typically get from an MBA program. Yeah.

**Chris Gammell:** Yeah. That makes a lot of sense. I mean, the, the thing that always like weirds me out about all this, the, the MBA stuff is like all these people that come out of these programs and they're like, yeah, we're going to go work in startups. And it's like, okay, what's your background? They're like operations. And I'm going to go work at a startup that does software. And it's like, you don't know anything about software. Like, and I realized that there's other, you know, fields that are required, but it's like, there's such a strong pull into tech from MBA programs. And yet there's, there's like no tie to the technology side of things. And so like the fact that that exists, you know, like I, I never understood that aside from the fact of like people that are like, I'm going to go work in tech after, you know, paying 80 to a hundred thousand dollars a year for two years, but whatever, uh, you know, that's, that's its own thing, but yeah. Yeah. Yeah. It's, it's, it's good that they're doing a technical side. I think.

**Kyle Dumont:** Yeah. They're, they're really trying to beef up that side of things. I think the MBA programs realized that you can't have a class full of, full of people from the finance industry because it just, it's so important. And especially in an MBA program, most of the learning is centered around discussion from the students. And so having the voice in the classroom that's saying like, Hey, you know, this is actually how things are built ends up being pretty important. I think they've realized that.

**Chris Gammell:** Yeah. Well, that's great. I mean, it's, yeah, I think I wouldn't expect the people like yourself or, you know, other people that are graduating from a Harvard MBA program that are like, I'm going to go become a coder now. It's like, that's not like likely an output from it. However, having the context of like, Oh, this is what the software people that I'm asking to do all these different things. It's like, Oh, that actually makes a lot more sense then. So from that perspective, it's, it's really good from a being able to communicate with the people that you're building teams around and, you know, understanding their pain and things like that.

**Kyle Dumont:** Yeah. And knowing what really goes behind executing on something so you don't end up. Right.

**Chris Gammell:** Yeah. So we've got to build a Android app and an iPhone app and a desktop app and six weeks. Are we good with that? We had three engineers. Each one does one of them. Yeah. Six weeks. Okay, cool. So yeah, I'll talk to you in six weeks.

**Kyle Dumont:** Bye.

**Chris Gammell:** That's right. Right, right. There's snacks in the kitchen and a ping pong table. So I think we're a startup and we're good to go. Yeah. What about, I mean, we've had other people who are MBAs on the program before, but tell me more about the class. I'm always, I have a friend who went to a booth who was in tech and, you know, it was interesting hearing kind of like the people that he interacted with, but tell me more about like the crowd that you kind of interface with, because I also have learned from people that I know who do MBA programs. It's like, no, it's really about like getting to know other people and building connections. Like that's kind of the real value, especially if you're at a place like Harvard.

**Kyle Dumont:** Yeah. I think that's true. Typically wouldn't go to an MBA for like the, the core learning or like the, the classes themselves. Although I think what an MBA is good for is just exposing you to as much material in a short amount of time as, as possible.

**Chris Gammell:** Yeah. Yeah. And especially if you have like high profile access into like a, you know, if you want to do consulting, you can go do an internship at McKinsey easily. If you want to do, you know, if you want to go do a startup, you can talk to a bunch of VCs easily. You just kind of like lean, lean on the name. It feels like.

**Kyle Dumont:** Yeah. Yeah. I don't know if I've gotten quite there, but that's, that's the idea.

**Chris Gammell:** Oh, lean into it, Kyle. I should be like, Oh, hello. I'm Kyle from Harvard.

**Kyle Dumont:** Yes. You got to work on that, that intro. I would say my, my one liner for an MBA is, is basically it helps you sound like less of an idiot in most conversations.

**Chris Gammell:** Oh, okay.

**Kyle Dumont:** Or many anyway.

**Chris Gammell:** Okay.

**Kyle Dumont:** The cases, so you're basically doing all case studies primarily for learning. And so each case study is a different company or maybe it's about a country or something like that. So you just get exposed to like a lot of different scenarios and then you spend an hour talking about that and you'll do two to three of those, uh, you know, a day during the school year. And you're also surrounded by one of the other things they try to do is just bring in the most, you know, diverse group of people that they can find. Yeah. Hence why they wanted some engineer joining the class. Good. So yes, believe it or not, in some pools we are, we are diverse.

**Kyle Dumont:** Oh, good.

**Kyle Dumont:** Yeah. And then, uh, so you, you get those experiences from, from meeting people from different places or backgrounds or industries as well.

**Chris Gammell:** Right. Right. Right. And then you're, uh, you know, you're getting your master's in data science or, you know, computer engineering from Harvard and you're like struggling over adding and subtracting in the accounting classes. Cause none of it makes sense.

**Kyle Dumont:** Oh God. It is so, it was so strange going from like advanced computer micro architecture, then walking into, I think I had sale, like a tech sales class that I took. And it's just the, the whole atmosphere is you walk, you know, from the engineering campus to the MBA campus, it's just like switching from right brain, left brain. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Kyle Dumont:** That's great. It was interesting. Yeah.

**Chris Gammell:** So you mentioned 30 of you, most of you did computer stuff. Do people do other, like, is there like a option even to do hardware? Cause I know Horowitz and Hill are both Harvard folks. So there's definitely some, some, uh, firepower there.

**Kyle Dumont:** Yeah. So the engineering school at Harvard is really focused on PhDs. So the hardware classes are taught maybe slightly less often, which you can get away with if you're doing a PhD, because you're there for four or five years. Right. I will say there weren't as many of those classes. You know, I took computer architecture. There were some, some hardware classes for sure, but there were definitely a lot more, more data science and more of a selection for computer science.

**Chris Gammell:** Yeah, of course. Yeah. I mean, I just, from a numbers game, it makes sense. Okay. Well, that's cool. So, uh, let's get into the, let's get into the data science and stuff you're doing with this. I mean, you're, you're kind of merging it all here. You got the business, you got the, the data science, you got the, the hardware. So tell us about Allspice. What do you, what are you trying to do with Allspice?

**Kyle Dumont:** Yeah. For, for better or worse, I'm not sure what else I would do if, uh, if I wasn't doing Allspice. It's that perfect intersection.

**Chris Gammell:** Right, right.

**Kyle Dumont:** Yeah. So Allspice is really focused on building a Git based automated release workflow for hardware designs. This really comes from my time spent doing product development. It always felt like our, uh, design collaboration and release process really was never suited to do what we were trying to make it do.

**Chris Gammell:** Uh, Kyle, I don't know if you've heard of zip files. Um, you get to email them back and forth. Sometimes if you're really feeling fancy and spunky, you can use a Dropbox link. So I don't know what the problem here is, man. Sounds perfect.

**Kyle Dumont:** And that's, uh, yeah, that's pretty state of the art.

**Chris Gammell:** Plus I label it, uh, if it's rev 34, I rev it to 35 and we're done.

**Kyle Dumont:** So yeah. Rev, rev, uh, 35, no dash, no for real this time. That's right. No for real this time. Yep. Yeah, exactly. So in, you know, it's, it's not surprising reflecting back on it in based on what we've learned doing lots of interviews with our current company, you know, a lot of it's because the, the tools and the processes were built around waterfall design where you could take the time to do all the documentation ahead of time, line things up, get all the pieces in the right order. And then you're only doing maybe a release every six to six months or so, maybe 12 months depending on the industry. Um, but as these, you know, these timescales are being compressed because you have softwares now iterating very quickly, even mechanical engineering is getting better at iterating quickly, especially using 3d printing. Like we talked about. Sure.

**Chris Gammell:** Don't forget, uh, don't forget chip company is deciding to merge every other week. So, you know, you got to change the data sheets that are attached to each design that you do.

**Kyle Dumont:** Oh yeah. Forget it. I, I, uh, I think those, those data sheets, at least that I've ever seen are usually always out of date. Oh yeah. Yeah. So yeah, the ease are kind of stuck in the middle of, of this space and not most are pretty cognizant that the, the tools are, are at least there's a lot of friction around the process of, of iterating. So, you know, when I went to start, uh, the EE team at Voxelate, the 3d printing company, I did what most hardware startups do, which is we use Git and GitHub to actually host our, our CAD designs. Um, at least for electronics. But what we found is that, you know, Git may work to give you that centralized repository. And, and I know you've, you've talked about this some with, uh, contextual electronics, the environment that's built up around Git and GitHub ecosystem for, for software just still doesn't exist in, in hardware primarily because Git isn't set up for those like binary CAD files.

**Chris Gammell:** Well, yeah, but not every CAD file is binary. So this is where I usually, you know, I'm snarky about it, obviously. And, uh, yeah, it, for Altium or other, you know, cadence, whatever, all the binary files, it doesn't work. But to be fair for KiCad and Eagle, which use ASCII based files, it still sucks. I mean, it's still like if you're doing a diff between different things, maybe we could take a step back real quick too. Sure. Could you try and sell people? Okay. So like you just hired someone at Voxelate. It was a hardware engineer. They've never touched Git before and you were going to try and sell them on it. Obviously you're in charge of them anyways. It doesn't matter, but you're trying, you're, you're a good manager and you're trying to sell them on the idea of it. Why should people use Git in the first place? Because this is something I've struggled to explain on the show before, but I'm very much into this workflow as well. So like what, what would you tell that, that new hire?

**Kyle Dumont:** One of the things we find is that a lot of engineers that are entering the workforce right now for EEs, they're doing firmware design as well. And actually a lot of electronics engineers are doing firmware design as well. So one of the clear benefits is if you're doing firmware, you're going to want to understand that process anyways, because it's so industry standard for like that firmware software world. So getting everyone in the same system, you know, is, can be that much more powerful. You know, at Voxelate, I always had somebody that I could go to on the software engineer and he's actually our lead software architect now for Allspice, who was like my guru for, for helping understand Git. Yep. In terms of the core utility, you know, for, for one, it's, this is where, you know, hardware is not there yet. And this is where we're trying to get it into, into this, you know, into a place where you can get some of the, the real benefits that Git provides, like being able to actually segment your design changes based on a branch.

**Chris Gammell:** And we'll dig into that too. I think that's a, that's something we can definitely, I think that's a key piece because that's so tied to like manufacturing ideas as well, right. Of like branching ideas out and trying different things. So yeah. Specifically on Git though. I mean, could you maybe also test even further step back for people that haven't even heard of it before? What, what is Git and how does, how does it fundamentally work?

**Kyle Dumont:** Git is a protocol that enables essentially design revision control. It's particularly designed for those ASCII text files. What's interesting about it is that it actually saves files based off of save new versions based off of the, the change, the Delta in from one version to another. Yeah. And so it helps save space that way. And that's what made it a little bit different from like SVN subversion that came before it. But essentially it's, it's giving you that provision control design history for any files that you put into it.

**Chris Gammell:** Yeah. It always like wigs me out. And it's like, so I, you know, I, I do teach a little bit with this in contextual electronics, but it's like, yeah, you go into the dot Git folder. That's like in a Git repository. And you're like, oh no, it's all there. Like you just have the differences from the first day. And like when you like, so if I go and clone a direct or a repository that you created and I pull down that dot Git repo, that dot Git directory. And that's what defines the, the Git sub, uh, the Git repository itself and all the configuration stuff that's in there. But it's like, I don't just download the latest files. I download all of the history and I get to see every single change that you've made, you know, going from A to B to C to D to E, you know, all the way back to Z. And then Z is the current day. And you can see all these different changes that might've been happening and, and tried and revised and all that, everything else there.

**Kyle Dumont:** Yeah. When you do that Git checkout, it copies everything to your local repository and you can very quickly hop back and forth between it, which is what makes Git kind of nice. Um, between different versions and then to do, to re-sync, you know, you do run the Git pull process and that'll essentially pull from the centralized, uh, you know, cloud version to your local repository.

**Chris Gammell:** Yeah. I feel like that's another important like element too, that it is that there's, everybody has a copy of this history and then there's the, what's the centralized one. So like if I'm on github.com or Git lab, that's called a remote, right?

**Kyle Dumont:** Like your remote. Yeah.

**Chris Gammell:** Yeah. And so the remote is like the kind of the reference that everybody has, but then I'm making changes on my local copy and then I can go and say, Hey, my changes are getting pushed to the remote. And this is probably the most boring podcast that anyone has ever listened to. Every, every hardware engineer is tuned out, but it actually really matters because now it's like, you're not just changing, you're not just sending the end files. Right. And this is actually probably coming back to the binary ideas is I'm not just sending version 34, moving to version 35. It's I'm actually changing. Our one has moved from position, from X position, X 34, X 72 for to position X, you know, 34, Y 95, you know? And it's like basically just change. You can actually have these discrete changes that are tracked. And we've seen this in some other tools as well. Right. So like, uh, the web-based tools try and do all this stuff on an individual move basis. Right. So they actually track history of like, Oh, user one moved our one from those two coordinates to the second set of coordinates that I, you know, I said, and it's like, they actually just track all of those things as historical elements. But now it's like, basically the user decides when those changes get pushed. You know, I make all the changes on my local copy. I now say I've decided now's the hour, Chris time to make that change. I push a commit. And then that basically bundles up all of the changes that I've made and I can then send that to the server.

**Kyle Dumont:** Yeah. Yeah. One of the interesting things for, for Git, as you mentioned, is there's that separation between the local and the remote. So what happens is to push a new version is actually generally two steps. First is you do that commit and that commits it to your local dot Git folder, your Git history on your local computer. And then when you run the push, that's when it actually pushes it now to the remote server. Everyone else can access it.

**Chris Gammell:** Yeah. There's an XKCD about Git that we're talking about. Like, you know, like it's like this highfalutin like, Oh, Git is the most like magical thing ever. And they're like, well, what is it really? They're like, yeah, it's a better set of commands that you remember. And you try and you try and use them possibly to, you know, make your thing work. Finally, you know, it is really, it really does start like that. And it sucks when you're getting started, but once you start to get into it, it can really open up your workflow and try different things.

**Kyle Dumont:** Yeah. What's beautiful about, you know, and it's hard to say whether it was more Git or more GitHub, but was the kind of the workflow that started evolving around that and the ecosystem that evolved around that. And the hooks were there in the Git protocol. For instance, literally the function called like a Git hook where you can have it run every time you push a new version, you can have it run a series of scripts on your design. So if it's software, you could have it essentially, you know, check your formatting or something like that and all your indentations and things like that.

**Kyle Dumont:** Yep.

**Kyle Dumont:** But for us, we look at using that essentially to start to build this continuous test, continuous integration process that has also evolved in the software, software discipline.

**Chris Gammell:** Yeah. Yeah. That's a great, and I love the digging. Before we do that, I would, I would call out. So Jesse Vincent, who's been on the show before, he actually gave a talk at KiCon last year and he used Git hooks. So like for his example, and I'm sure this is stuff you guys do too, but his example was for KiCad, when you push a new revision or you tag it or whatever, whatever the finalized version is saying, Hey, this is ready for production. There's some way he can send that as a input to his Git repository. And then it just starts spitting out everything. It auto generates Gerbers. It regenerates a schematic file. It regenerates the bomb. It does all this stuff that you'd have to do anyways. But like, why, why shouldn't that be automated? It's like, Hey, I'm ready for production. Spit out every file I need to send to a manufacturer right now. And that's like a great example of like, that's a hook that drives all these other changes that, you know, then the files just show up somewhere and you're ready to go for manufacturing.

**Kyle Dumont:** Yeah, absolutely. I mean, that's, that's a perfect example. You know, you can really go from there. Of course, this is whole environment and industry of, you know, CI that didn't even exist 10 years ago, I think in software to this, at least not to this degree where you can run, you know, kind of an endless level of test and release on your design files. And I think there's actually, I mean, we believe there's even more power to do that for hardware because there's so much information that you need to go gather. I mean, we talked about data sheets, but if you can actually pull that information together to start automatically validating some of the manual processes that we're doing now, you know, one could be building that documentation like the bill of materials. We also look a lot about at what other documentation you could automatically be generating and updating for each version, such as building a power table, you know, going through, we know all the power, power ports on your design, and we can basically go through and maybe with a little help from you to fill in the blanks, we can build out a power table and then check, you know, let you know, this is the amount of current that each power supply is drawing. Yeah. You know, on average or peak and whatever else you might have. And not only that, but you can do that with the same diff process as you can on the original design. So you can take, you can look at how your current, maybe on a particular power supply has changed from one version to the next.

**Chris Gammell:** That's right. Yeah. Right. You could set limits on two, but can you explain what CI is? Because I think you said that, or maybe you said what it means, but can you explain it? Yeah.

**Kyle Dumont:** Yeah. CI is continuous integration and it means, actually it has a pretty broad usage, but essentially you can set up a series of tasks that run in your cloud on that remote repository where every time you push a new change, it can kick off a series of scripts or processes to either produce some documentation information, produce those releases, maybe deploy onto a website. If you are talking about a software web application.

**Chris Gammell:** Yeah. Yeah. I, I forget where I heard about it. Maybe it was a guest done here. And if it's, if so, I'm sorry, but there was someone who was talking about CI at some point and they were like, well, I think a best case scenario would be if you sent a, so say you were doing firmware and you go and check in a change and it's just a small change, right? You're like changing a variable, but what should happen then is like the firmware should get compiled. It should get built. It should get sent to a test board that might be hooked into a test stand. And then the test board basically runs through a suite of tests. You know, maybe there's a hundred tests and it doesn't need to run them all, but why wouldn't you just run them all every time? And then the, the one change that you've done does every test still pass based on the small change that you made. And if it does, then it's like, okay, the change that I just made that's, you know, the small, maybe I was just literally changing a, the name of a variable, but like it propagates all the way through the system. And at the end there's a test report that says, yeah, Chris, you didn't break anything, at least nothing that we care about. And then that basically, you know, gives you this, this confidence that you could continually well integrate, but I mean, you could continually try all these things and test that it's been working. I think the hard thing is the testing is it feels like it's a lot less, it's a lot less well-defined than it might be in a software world because it might, it might involve some real world characteristics that are tough to measure. You know, test stands and, you know, test equipment and all that other stuff.

**Kyle Dumont:** Yeah. We, we actually did that, which you mentioned at Voxlate. We had a, you know, we had a build server and it would push a new version of the code. And we had a, it run through a whole series of unit tests on the printer would go like jog it to all the coordinates and make sure it didn't crash. So I think that's a great idea.

**Chris Gammell:** Yeah. Those are like high level things that like, it absolutely must never do these things, right? It should never crash into the edge of the printer. Right. But who knows if one small thing causes that to happen and it is good to just try it to make sure. Yeah. So is that what you're kind of building with at all spice then as well? I mean, or is it more still on the software side and working with spice and testing these inputs? Yeah.

**Kyle Dumont:** Yeah. So we'll say we're, we're focused on the design files initially, though. That's definitely something we, we want to talk about and have more conversations around because that is so, it's so specific to people's hardware. We certainly will help people build that type of process, but we also want to take those tests and just run, emulate them as well. A lot of people get, you know, in really simulation itself is, I believe one of the biggest flaws with simulation is that it's so focused on getting like the perfect fidelity, you know, third, fourth, fifth order, you know, fidelity for simulation models. And for many cases, that's exactly what you need. But there's many cases where you're almost better to get a breadth of design information, such as like, did I hook up TX to RX? You know, we, you don't need a fourth order equation. That's never happened, Kyle. I don't know what you're talking about. If you have, yeah, if you haven't switched TX and RX as a, as an engineer. You haven't lived, you haven't felt the power of soldering wires. There are two types of electrical engineers. Those who have swapped TX and RX and liars. That's right. So one of the things we look at for this is, is just getting you a breadth of design knowledge. And then we can drill down like both using, you know, custom, basically custom information from the user. So start putting more information into, you know, into your design or into your documentation and also improving our own database of component and model information.

**Chris Gammell:** Of screw ups. Yes. You know, it almost sounds, I was really like into like the idea of like checklists and Atul Gawande's book about checklist manifesto and stuff like that. And it almost sounds like you're, you're automating a lot of that stuff, right? You're basically pre-flight check, checking everything just for like idiot proofing it to make sure that you didn't, you know, I mean, you could do DRC stuff and you can do all these. Like there are some built in, but it's not unified anymore.

**Kyle Dumont:** Yeah. Yeah. And most of those things take so much effort to set up for the amount of utility you actually get out. It's, I think it's one of the reasons that they're, they're not as broadly adopted, but certainly you actually, uh, one of the blog posts I've been, been meaning to push out is, uh, the design review checklist. Yeah. Cause I, it's something that we, I don't know, we talk about all the time is, um, and every time I go to a new company or talk to a hardware engineer, it's always, everyone's coming up with their own design review checklist.

**Chris Gammell:** Yeah. Yeah. It would be nice to have some kind of, that would be great to have like a standardized one. I think we've talked about on the show before too. Yeah. And like, so I had asked about it and, uh, Charles, I had submitted some and like I asked on Twitter and a bunch of people did. And it's like, it's really tough because every board is so different. And that's usually what it comes down to is that there is so much difference, but just having a starting point of like, you know, did you check, you know, just having like a published version somewhere, I would point people at that. So if you go and make a blog post and say, here is, you know, go start like a design checklist.com. I'll point people at that just as like, you know, you need some kind of starting place for beginners.

**Kyle Dumont:** And yeah, it's a template. It's a template.

**Chris Gammell:** Yeah, exactly. Exactly. And people are going to customize it. It's more about building the habit more than anything else. I think, because I I've had design checklists before and the number one thing that happens is I just forget to do it. You know, that, that doesn't help. But if it was part of a check-in process or something, you know, and it was like, even if it just sent me a text message, it's like, Hey, Chris, did you, did you check this against your checklist? That would be great. So that's probably one for more of the, the board houses and all the others out there. But yeah, send me a, send me a text message reminding me not to be an idiot. And that would solve a lot of problems.

**Kyle Dumont:** Yeah. I mean, if it gets to the board house at that point, hopefully they catch it. I mean, I've definitely had to send many thank you messages to, uh, yeah. Board manufacturers.

**Chris Gammell:** To cam engineers. Yeah. Yeah. That's true. I mean, and that's true. I guess so. But like, I don't know, I feel like even like a thing, like when you send it off to a, like a really good check that would, a board house would never, well, maybe they would check it, but most people wouldn't need to send it. Right. So if I'm sending my Gerbers to like an Osh park or, you know, whoever the check would be, Hey, Chris, do each of these parts actually correlate to a, uh, a real component? Do you have MPNs for every part here? And it's like, well, that is not necessary for making a board at all. However, that is almost always the source of like me putting the wrong footprint down is because I haven't gone in. Like, I'm like, Oh yeah, I know this one. This is a SOT 23 for sure. And it's like, no, no, no, that's a SOT 523, you idiot. Like there's, there's no way that that's what you actually, you know, like, and it's just, if I would have gone and like really verified the data sheet, that's, that's just an impossible thing to check at a board house.

**Kyle Dumont:** Yeah. I mean, it's on page 37 of the data sheet. I mean, the best is when you get those data sheets that are like, these are all of like the variations of this footprint, like a crystal or, or honestly, uh, I don't know if people

**Chris Gammell:** would be willing to do it, but like, if there was a board house that said, Hey, no, actually you have to send, you have to send it your MPN for this part. If you don't, we can't check it for you. But if you do, we can double check that all of the footprints are the right ones. You know, that would be a great, a great service to have like a check of MPN versus what's actually on the board, you know, because that MPN is always tied to the specific footprint.

**Kyle Dumont:** Yeah. That's actually one of the things we talk about a lot. It's just going through the design metadata and saying, you know, do you have a manufacturer and a part number specified for your parts and how many of the parts are without, um, not to say, you know, give you some big red flag and say like, you know, you have failed, but right.

**Chris Gammell:** Give you that. You might want to check this kind of thing.

**Kyle Dumont:** Yeah. Yeah. Particularly the area we focused on initially. Well, a was connecting with those teams that are using Git to manage their, their hardware designs, because where we do want to do ultimately is make it easier to adopt. But initially we're, we're finding the teams that are already adopting these, the Git technology or Git workflow process. And the first thing we did is we built essentially a diff red line into that. This is kind of, as we spoke about, it's like doing that Delta comparison for, for software Git can go in and tell you, these are the lines, these are variables even that have changed.

**Chris Gammell:** Yeah. Like a diff is like a side by side of like showing like, Hey, someone put a new chunk of code below this function. There's a new function here, or they deleted that function or something. So, yeah.

**Kyle Dumont:** So essentially we go through and we build the red visual red lines. We take the schematic and we highlight, you know, green for added yellow for modified and red for removed components. And then we also take that, that textual metadata side. We show those side by side to tell you what's, what's changed in the design.

**Chris Gammell:** Cool. And how, I mean, how has the feedback been on that sort of thing?

**Kyle Dumont:** So we're just getting it out there, but generally seems to be good so far. I mean, we're, we'd love, you know, it's totally free to use. It's on our website. So we definitely love, love more feedback. We're working with.

**Chris Gammell:** Kyle, what, what, I was going to say, what has to happen here for Chris to use this? There's a, so we are currently supporting. You had to focus on people that actually pay for things. Is that what you're trying to say? Yeah. Yeah. There's a, there's that. Hey man, it's a business. It's a business. It's fine.

**Kyle Dumont:** For, for sure. And yeah, there's, yeah, there's, there's really interesting segmentation. Like who uses what CAD tool.

**Chris Gammell:** Yeah.

**Kyle Dumont:** Which is maybe, I don't know if other industries are like this or if electronics is unique, but pretty much seems like if you know the company, what industry they're in and how long they've been around, you can tell with like 95% certainty what tool. Interesting.

**Chris Gammell:** Well, give us some of this over. I'm curious, just like, it's like broad strokes. Like what is, so like if someone's like an aerospace company with more than 500 people, what are they using?

**Kyle Dumont:** It's probably mentor graphics. It's either mentor graphics or cadence. Actually aerospace is kind of a unique area where if you're talking like Boeing, they literally use like all of them. It just depends on the division. They're that big.

**Chris Gammell:** Like they, they're an amalgamation of different old companies.

**Kyle Dumont:** Yeah. Yeah. So some of those, there's large ones, but so larger, larger and I guess more larger companies that have been around for a while are typically using cadence design. Uh-huh. Altium really has that, that small and medium size company segment.

**Chris Gammell:** Yeah. Yeah. And like, especially consumer, it's like, good luck. If you're not, if you're doing consumer and you're not, yeah. If you're a small company and consumer, it's like, yeah. Okay. Altium is it.

**Kyle Dumont:** Yeah. But it changes all the time. I mean, obviously, you know, you've, you've talked at length about, you know, KiCat is, is really growing and, and really moving up market as well in some, some places.

**Chris Gammell:** Yeah. Hopefully. Yeah. We'll see. Um, yeah, I think that that's the other interesting thing is that like, as it does move up market specifically, like there's companies that are interested in paying for help. It's not just like just hobbyists or just people who are like open source nuts. It's people that are maybe looking to use other programs, but they don't want to deal with licensing, whatever. And there might actually be money there. I think that's really the thing for like companies that are servicing, you know, audiences. It's like, look, you got to pay at some point. I mean, there is, yeah, there's to, in order to, to design specific services for something like that, you gotta like, yeah, you gotta choose your battles. So I, I get it. I think it's interesting to me that Altium didn't have this. I mean, why, or do they have this and it's just not get it's like, um, the other one. Yeah.

**Kyle Dumont:** So, uh, Altium is, is they're building a tool called Altium 365. This is kind of their, their cloud, cloud-based, uh, um, design review system. And so we're, you know, we're really focused on building that, um, analysis and kind of getting early to market with, with the customers that, that really are interested in, in building, being on the early edge of building some of these workflows. Right now building, using GitHub, um, also using, uh, you know, GitLab and Bitbucket would be like the three major, um, hosting services using those as the platform to do the design review on, but potentially we could use Altium 365 as well.

**Chris Gammell:** Oh, you're saying 365 doesn't work. It only works with their internal storage instead of like an external hosting, like a GitHub. Yeah.

**Kyle Dumont:** They actually use Git as their hosting, as I understand. I think most of that is hidden from the users, which most hardware users would, would like.

**Chris Gammell:** Yeah.

**Kyle Dumont:** You know, we're, we're really focused on people who want to really kind of customize and own that, that system a little bit.

**Chris Gammell:** Yeah.

**Kyle Dumont:** At least in the initial days.

**Chris Gammell:** Yeah. What do we, and what do you, you mentioned a little bit that a lot of the younger engineers are firmware plus hardware, which makes a ton of sense. Are the teams like kind of small and integrated enough that they have software, firmware, hardware, kind of all working together? Is that like a kind of a, a, a best case scenario for, for what you're talking about?

**Kyle Dumont:** Yeah. I mean, you typically, you typically at any time a company scales beyond, you know, 10, 10 engineers, you're going to have folks that are just dedicated on, on firmware. Yeah. True. Yeah. You typically will have more and more, I mean, hardware designers are becoming, as far as I've seen generalists doing some firmware, doing some system level design. And then usually you'll have at least a good chunk of your electronics team now, especially at a, a, a newer company will be kind of a general electrical firmware designer.

**Chris Gammell:** Yeah. Yeah. Yeah. It makes sense. Hmm. So your workflow on the website and allspice.io website also calls out PLM. And so are you guys tying into like a, uh, arena or similar, or is it more tied into the Altium, uh, uh, PLM or what, what are you doing with that?

**Kyle Dumont:** Yeah, that's, um, that's obviously a huge piece of the system for, for hardware engineers. We're, we're still handling that on a case by case basis. Now, um, we're a bit on the, the outside of those systems and just using the APIs for, um, for querying and basically using the design information in the CAD design as kind of like our liaison to the PLM systems, because they tend to pull that information from PLM. But ultimately we need to be able to have an integration to push either the design releases or the component design review information.

**Chris Gammell:** Got it. Yeah. Yeah. PLM is like its own kind of beast. And it seems like it's, it's a lot of like custom integration. It always feels like as well. And it's, it's only when you get to a certain size anyway. So like, you never really hear about it until like you're hitting a face with it. It's like, there's no easing into it. It's like you go to a company and usually they've already got a huge PLM system or yeah, it's, it's tough. It's tough to work with.

**Kyle Dumont:** Yeah, absolutely.

**Chris Gammell:** So let's talk a little bit about the flow. Okay. So you'd mentioned branching before, but like, what's an example scenario that like, walk me through someone making a change. And then what happens? Like, what does that change? How does that change ripple out, especially through Allspice?

**Kyle Dumont:** If you're making a change, the general idea initially, especially using this kind of workflow is to be very focused about the design change you're making. So if you're updating something to solve a particular problem, say, you know, maybe adding ESD protection on some input, you make just that change, or at least some way, make it in such a compartmentalized way that you're solving a particular problem. And then you can commit that. And so instead of making all of your changes and pushing everything all at once, you make a single change that solves a particular problem. You can commit that. And then you can make the other changes that you want.

**Chris Gammell:** Okay. So this would be kind of like, so like in GitHub, there's like issue tracking as well. Yeah. And I actually had to do this recently where I, I had, as luck would have it, I had swapped TX and RX. And my firmware engineer called it out. He's like, Hey, Chris, you did that thing. I'm like, okay. And like, so it had like an issue number five. That was like the number of the issue. And I went and made that change. I saved my schematic. I committed that change. And then I actually referenced the issue in the commit message. And I said, Hey, I swapped the RX and TX back to how they should be. Close is number five. And that was like a GitHub message. Is that kind of what you're talking about?

**Kyle Dumont:** Yeah. Yeah. And that can even go through and close out that, that ticket. Exactly. And so by compartmentalizing it, you can make it just easier to basically go back through that history, see how the issue that you created or that maybe the firmware engineer created links to that particular design change. And then you can easily cross-reference, you know, why was this thing changed? Oh, here's the issue and all the documentation about it.

**Chris Gammell:** What if I don't like making changes like that in an atomic way? What if I'm used to messing up a lot of things at once and fixing a lot of things at once, Kyle? You're just throwing it all, throwing it all in the same change.

**Kyle Dumont:** Yeah. That's hopefully when you're working on your own project, maybe that's, you know, that's digestible. Yeah. But yeah, people, people tend to like to look at when they're reviewing colleagues or reviewing other, other people's designs.

**Chris Gammell:** So what about at the beginning of the process though, when, when you are just creating things? So like fixing, I totally get. What about the initial creation of all the mistakes that I'm going to make?

**Kyle Dumont:** Yeah. So the beautiful thing about issues is you can kind of log them as they come up and then you can have that very clear checkboxes, closing those issues as they're resolved. In terms of just like bulk adding a bunch of designs, some of those earlier diffs or earlier versions, you know, may or may not be the, the ones that you've referenced the most for, for the diff. Okay. Because you're going to get a whole block of like new parts added.

**Kyle Dumont:** Yeah.

**Kyle Dumont:** But you do tend to get a good overview.

**Chris Gammell:** Yeah. So like I, I, I track, I track changes in like contextual electronics as I'm like going through and building each thing. And I'm like, so I'm like doing the layout for the, like recently I was connecting a microcontroller to a logic level translator. And so it had like eight different lines and all the power and whatever. And it was just like one big bulk ad. And it was like, okay, like traces does doing layout, I'm sure is its own beast. But like, that was like one big section all at once. Is that what you, you're just saying you wouldn't really reference it until it's all in there.

**Kyle Dumont:** So you can certainly do it that way. I guess you kind of learn to break it up in the way that you think will be most digestible to somebody or yourself looking back on it. So if there are ways to kind of compartmentalize changes and they're good kind of thresholds to break it up into, when you get into layout, you can kind of see, you know, even from just a very broad high level, you can see the areas that are being changed. You're like, okay, this thing in the top, right. That's my power supply. There's a whole bunch of green going on there. So a whole bunch of things were added there and you can kind of zoom in and do a deep dive. And then it's very quick to be able to look at that commit message, which is the other piece of, uh, of Git says like, Hey, I laid out the, you know, five volt power regulator.

**Kyle Dumont:** Yeah.

**Kyle Dumont:** You can look at that diff for the PCB and you can see, Oh, there's this big green blob. I should go check that out. If I want to go look at how that change was made.

**Chris Gammell:** Yeah. I mean, even though I, you know, I usually disparage online layout tools. The one thing that is really cool about it is because you're tracking like, all right, you're drawing a line from, you know, point A to point B and that's like a single change. And they're tracking that change. You can literally go do a playback of an entire layout, which is like, that is super cool. It's probably, it's not as practical as what you're talking about, but being able to actually track those changes and say like, Oh, here's where it went wrong. You can, you know, like you skipped over a via here, you deleted or whatever. And it's like, you can actually track that change by change. This is much more bulk added at once. And it's like, I started by, I wanted to connect microcontroller to logic level translator. Here's the difference between these two layouts. And it's just like, it's just like a magic fast forward that goes between the two.

**Kyle Dumont:** Mm-hmm.

**Kyle Dumont:** Yeah. That's one of the interesting things. I've talked to some people about the difference between doing like discrete design changes, like how Git does, where you very deliberately say, you know, I'm committing a new version versus real-time design editing. Cause there's some design tools that have really taken up this, like, Oh, it should be real-time on the cloud enabled.

**Chris Gammell:** Yeah. Right. That's like a fusion 360. You have like the history of each thing that happens. And, and then they even do the thing where you can go and like change a certain portion of it. And then it ripples through the design as well. And there's sometimes issues with that, but you can just go change that one dimension and then it all ripples out. And it's like, that's pretty cool, but it's, it's, uh, it's definitely a different way of, these are all like different design methodologies almost.

**Kyle Dumont:** Yeah. Yeah. And, you know, whereas Git would be that more like discretized way of like, um, yeah. So that's where we kind of land is, you know, that seems to be at least what's, what's been adopted most prominently in software, of course.

**Chris Gammell:** Well, I think the other, the other problem with that is like the choice is you either you're using a third party program, right? You, you guys are a layer on top of an established program or you go and build your own layout tool, which is like, well, we've seen that a couple of times that it's just, it's really tough. It's just a huge process. And then you have to like win over all these people and it's just a mess. And it's like, and then you also have to convince them that this new way is the best way. It's like, you know, changing someone's religion. It's like, yeah, you better have a lot of dollars and a lot of patience to, to do that sort of thing.

**Kyle Dumont:** Yeah. Patience, especially, I mean, getting people to change as, as you mentioned, especially, you know, a company, getting them to change to a new, new CAD tool is just, you know, it takes, everybody needs to change and everybody needs to accept it all at the same time. That's right. That's right. Exactly.

**Chris Gammell:** It's like, well, this might work if we burn down the old building and fire all the engineers when they rebuild, they might rebuild with a new tool. Who knows? Yeah.

**Kyle Dumont:** Yeah. I think, so I remember iRobot right when I joined, they had just moved to Altium. They actually did that whole, oh, they did it. Wow. Transition. Yep. And I think it actually coincided with them moving to a new building.

**Chris Gammell:** So do you know what the reason was why they switched over?

**Kyle Dumont:** I don't, I don't recall. I don't know what the real reason was.

**Chris Gammell:** I mean, sometimes it's just like a talent availability, you know, like it's like, Hey, we can't find any engineers that do cadence or whatever. Obviously that's not a good example, but, uh, we can't find any Zook and engineers. Like there's still a program out there, but unless you're like making cameras in Japan, you know, it's just like, it is very targeted segments. And if you're in Boston and you're making robots, it's like, you can't really find people. So where can we go and find the talent? It's like, yeah, we got to make this switch to Altium or whatever. And it's like, yeah, that, that would make sense. But then you think about all the legacy stuff that's dragged along too. It's just, it's insane. So it's nice that you guys are making stuff on top of a popular tool, obviously, but then it could be eventually decoupled from the tool. I think that's kind of the idea, right?

**Kyle Dumont:** It's that's, that's totally the idea. Yeah. And, and especially we can, we can take that input layer and start to create different, not plugins might not be the right word, but basically different parsers for the different design inputs. And then we can kind of in, in the ideal case, create more of a unified, maybe intermediate file format. Yeah. I know folks have, we've talked a bit about that on the discussion boards over at contextual electronics, but that would be the ideal.

**Chris Gammell:** Yeah. And that would be nice. And that's actually how a lot of the, the footprint makers are doing it right now too. They, they have the interchange form. They have their own interchange format and they say, okay, well, pin one's always pin one and it's, you know, power or whatever VCC. And then how does all team want to see it? Okay. Well, I'll put that, you know, pin one's output in this certain format. And how does Kike want to see it? Oh, it's output in this certain format, but then they store it that one way. And then they have ways to ingest and X and excrete footprints basically. And so it's like, sounds like you kind of are looking to maybe do the same thing.

**Kyle Dumont:** Yeah. I actually didn't realize that with manufacturers exporting footprints, I have started looking at.

**Chris Gammell:** Well, not manufacturers. So this is more like a snap EDA. I, I think some of the manufacturers do it, but like a some access or a snap EDA or ultra librarian, they all have their own internal format, but then they have exporters and importers and, uh, right. So then when they store like an XML file that has, and I'm guessing here, I haven't seen any of this stuff, but just cause the reason I really know this is I think about this is because some of them, when you download it, you can either choose which program you download and one of them, I forget which one it just sends you all of them. So it's like, I want to download, you know, a TPS 62, 8, 2, 1. And that's a part I used in a recent board. So I want to download that footprint and it sends you 16 different versions of that file in every, you know, like for every popular CAD program is like, well, I guess that's one way to do it. It's like, but it's very unlikely that they have, you know, one person going to make that footprint for every single program. It's instead stored centrally and then generated as a, as a way to export to all these formats.

**Kyle Dumont:** Yeah. It's kind of like that compiled, uh, concept. Like you're, you have all of the information and you're like compiling it and pushing it out.

**Chris Gammell:** Exactly. Yeah.

**Kyle Dumont:** I saw recently, I don't know if you've come across the JDAC 30, I think it's JDAC 30 format. Okay. I think essentially it's a format for component information, which is supposed to contain both the footprint, the symbol, and then also like some parametric component information. So that's something we're looking at a lot too. That's for that component level.

**Chris Gammell:** Yeah. Yeah. That'd be really great. I mean, problem with all that stuff is just that it's the data is just, I mean, there's hundreds of millions of parts out there and much, most of them are really boring and, you know, a resistor that, you know, the one, the 1.13 K resistor is, is a completely different file and, you know, data entry than a 1.18 K resistor, but still got to have the different, you know, you still got to generate each file and it's like, Oh, or it's like a scanned, scanned PDF. PDF. Oh, even worse. Even worse. Oh my God. Yeah. Yeah.

**Kyle Dumont:** It's, it's a challenge.

**Chris Gammell:** It's, it's a, it's a crazy industry. You know, it's, you know, everything's still PDFs. Okay. So, uh, so someone is generating, okay. So they make a small change. Let's, let's go with your example. I like that. So they add an ESD, uh, set of diodes to a design. They, they go and commit that change. They say, Hey, I added ESD diodes. It, you know, now is listed as D one Oh five in the design. And then, then what happens?

**Kyle Dumont:** Yeah. So then you can, you basically commit and push, you know, either in a series of steps or you can commit and push, um, that entire block change and. That's block change, not blockchain folks. Yeah.

**Chris Gammell:** Now enabled by a blockchain technology. Yeah. That's right. Right. It takes 45 minutes, 45 minutes and six gigawatts of energy to do it. Yeah.

**Kyle Dumont:** Yeah.

**Chris Gammell:** But you generate a Bitcoin out.

**Kyle Dumont:** That's right. So we, um, you know, you can, you can push that, that change you're using, uh, all spice. We have essentially a version that can, you know, work as a hook to basically generate that diff to show you the, the differences. So you can actually see this visual representation of how the change was made. Then you can also actually create a, um, you can make a comment that says, close out that issue that, you know, should have been open any other documentation. So say there's like screenshots or documentation, you can actually upload it and attach it to that ticket. You know, some folks use JIRA for this as well. I think some teams.

**Chris Gammell:** Yep. Yep. And JIRA is like a, like a card based tracking system, right?

**Kyle Dumont:** Yeah. Yeah. Very similar to how those issues work. I, it's actually probably fairly similar other than Atlassian, I think makes JIRA. That's right. Um, yeah, JIRA is great.

**Chris Gammell:** I mean, it's, yeah, a lot of people hate it, but I actually kind of like it. It's like Trello or anything else. Yeah. You can basically, it's like sticky notes on a digital desktop.

**Kyle Dumont:** Yeah. Yeah. But you can, you can close out that, that issue. Um, and you can also create a, um, design review or pull requests around that. Could you explain pull requests? I think people probably will understand design review. What's a pull request. It's, it's kind of, it's basically the Git equivalent of a design review. The idea here, at least in the Git landscape is that you've created a branch. So like you've created a fork in your design with your design changes.

**Chris Gammell:** You're saying a lot of new words here.

**Kyle Dumont:** It's like, it's, if you picture a fork, it's like a fork or a spoon. Then you knife it. Yeah. Okay. And then you, uh, and then you create your fork. Yeah. And it essentially should contain all of those, only those changes that you've made and you submit a pull request, which is basically you can tag folks in your organization that maybe need to review it. And then once you make that change, it'll pull it into that, the branch, the main branch that you're using.

**Chris Gammell:** Yep. Yep.

**Kyle Dumont:** And so that's where you can start to put a lot of your, you can start to have your dialogue around the changes that were made. You can actually, again, the idea is with Allspice, you can look at the diff. So we create that diff for you automatically and you can actually comment on some of those things. Yeah. Again, we're looking at using GitHub and, and those, uh, hosts other, so hosting services for that.

**Chris Gammell:** Uh, this is kind of a non sequitur, but have you considered using Git for, for the PLM process because, or is anyone doing that that you know of? Because what, what just popped up in my head was like, I was like, oh yeah, like a, a, a pull request is kind of like when you made a change in a PLM system. So the process that I was thinking about though, is the signature process, right? So you go and make an engineering change request and you, you have to like, I remember like printing when I was a co-op, I like print out paper and then they would sit in someone's literal paper inbox because you know, they didn't have the whole system in place. It would go sit in their paper inbox and you'd have to get their physical signature. It was like four different people. And it would just be like on a Friday, the engineering admin would just be running around just begging them to read their, their change request so they could sign off on it and actually push stuff for production. It was like, but that's basically what a pull request is. It's basically sending around this thing, you know, usually to fewer people, but you send it around and you basically get a sign off and it's decoupled from paper or signatures or anything. And then basically it gets that change. Then that small change gets pulled into the process. And then it's like, that is the new Bible, right? That is the new truth that everybody works off of. So has that happened at the PLM level?

**Kyle Dumont:** I've never seen anyone doing that with, with Git now, but you're right. I mean, it is very analogous to like the ECO process differences being hopefully, you know, it's so much easier to do and you have all the information in one place. It's easier to do that review. And if you break it out into those little bite-sized changes, it's not, you know, a multi hour or multi day process to review a design. It's like minutes or, you know, maybe an hour to go through and say, oh yes, he did that thing that he had intended. You know, I'll give this my stamp of approval.

**Chris Gammell:** Yeah. So then maybe that ties into some of the other stuff that is happening or needs to happen, which is like, okay, so now going back to the ESD example, if you had a test that was like, oh no, these lines need to have low leakage. And then you put a bunch of ESD diodes on them and they start leaking. How do you decouple? Like, so like, it's a small change. It looks fine. It's good. The part, you know, you send it off to these different people within your organization. You send it to the part engineer. He's like, yeah, it's sourceable. You send it off the buyer. He's like, yeah, I can buy it. You know, you send it off to the manufacturing person. They're like, yeah, we can put this on a board. But like, they all sign off on it, but like, who's looking at it to make sure to double check that it's actually supposed to be there? Is there, is that something that you're also planning to get into?

**Kyle Dumont:** So you said that, uh, that what's supposed to be there? Like you have the appropriate, like, yeah, that it's like not a dumb change, I guess that

**Chris Gammell:** it's not like, uh, you know, you put in this ESD diode to solve a problem, but maybe it's going to cause three other problems. And that would be something that at a design review, you know, someone looking at it might be like, well, did you think about this X, Y, and Z? Right. But it's not necessarily a functional change of like, can this be done? But it's more of a, should this be done? Is there any kind of check in there like that? I guess it would be more like simulation and things.

**Kyle Dumont:** Yeah. I mean, this is going to evolve over time. You know, the first step is just provide that same level, at least show you how the design is changing so that you can have people do that manual process that they're in some ways doing now. And then once, you know, we build up more, more robust database of component information, we can check that, you know, you have the appropriate leakage for, um, or like, you know, hold off resistance or whatever it might be.

**Chris Gammell:** Right. Right. Yeah. Like critical, critical element for that, that specific part of your design. Right.

**Kyle Dumont:** And the idea here is that just like you said, you can build that test as you're creating the pull request. So it's like, I made this fix. It fixes the thing here. Look, you know, in that, you know, whatever information you need to add during that test is added and you can see, so you not only add it during that test, but then it will be tested at each future version to make sure that, um, it doesn't fail those conditions.

**Chris Gammell:** Ah, interesting. Okay. Yeah. That's, and that's, is that how it works in this? I've actually never really understood that part. Like I've heard about unit testing and I've heard people talk about it and integration, the continuous integration, but I actually don't know, like, is there a review process for when a new test gets put in or is it just like, no, no, it's always going to be checked now? Yeah.

**Kyle Dumont:** It, uh, it depends how diligent the process is and the reviewers are, but that is the, in principle, the concept of unit testing, which is, you know, if I'm going to make a, add a new function to my software, I'm also going to include the appropriate test that ensures that whenever this function is used in the future, that it's, um, or change in the future, that it's still outputting the, the correct pieces.

**Chris Gammell:** Hmm. Yeah. Yeah. And it does, I mean, this whole thing, I mean, people listening, they're probably like, oh my God, my job just got so much harder, but it does seem like we're talking about like the beginning of the process and it does seem like it builds up over time. So exactly. It would get easier as, especially if you're moving to manufacturing, it would get easier.

**Kyle Dumont:** Yeah. And I mean the same, I mean the same thing exists in software too. It is daunting. You're like, oh, I should be, you know, same with documentation. Like I should be good and create my documentation, but I could just push it out and go to the beach. Uh, right.

**Chris Gammell:** Right. My boss will yell at me at some point, you know, do it when they yell at me.

**Kyle Dumont:** Yeah, exactly. And it's always a balance with all of these things. But the idea is, like you said, you know, you can, you can build it in bite-sized chunks that it is ultimately going to save you time as you're not, you know, calling your manufacturer to figure out why something was built in a certain way at, you know, the midnight hours. Yeah.

**Chris Gammell:** Yeah. Right. Well, and so then that is kind of the, that is where kind of the buck stops is like, okay, I make this change, but at a certain point, it's going to change PCB manufacturing. Then it's going to change assembly as well. And that might have to go through a product lifecycle maintenance tool like PLM. It might have to go through that at some point, but I can imagine that this change literally, if everything was tooled up properly, I can add an ESD diode to, you know, a design and then maybe it gets bundled with other changes. But at some point it ripples all the way through to a main board that's being manufactured differently than it used to be manufactured. So how does that stuff get, when does that keep going through the process?

**Kyle Dumont:** You know, that's, that's kind of like the continuous release side of the, or continuous deploy side of this process.

**Chris Gammell:** Does that actually happen? I mean, like, I just imagine like, you know, rev 478 of my PCB, you know, and just like, and then like, you know, that would just be madness, wouldn't it?

**Kyle Dumont:** Yeah, I, so, I mean, that's, yeah. So who knows where things will go with, you know, turn times for manufacturers getting lower. If the time it takes to actually like release and like send your information over to manufacturer is, is lower. I mean, you could have a lot more rapid design changes, but right now we are focused on the data side of things, not on the release side. But the same analogy I think still applies to the software space. Some, some people might, might push back on this, but it really is like, there's this difference between continuous integration and tests, which is what we talked about. And then continuous deployment. And those are two different steps where the second one says, okay, no, now we're ready to push this thing out the door in software that may be like, we're going to go put this in front of people. And in hardware, it's, we're going to go put this in front of the contract manufacturers. Yeah.

**Chris Gammell:** It's almost like when, if you harken back to like, you know, actually making CDs, it's like, at some point you have to like cut off what's going to get included there. And it's like, you have to hit the button to go print another hundred thousand CDs to send out with your software. And like, that's a big deal versus now it's like, oh, I'm just going to upload, you know, version 4.17.2 and revving from .1 to .2 is not that big a deal because it just updates overnight on someone's phone. You know, not that that's not a big deal that could break a lot of things, of course, but like, but the actual, the physical atoms element of it, bits versus atoms, like it, there is like a, a bigger cost to revving at that point, just like there would have been with printing new CDs. Yeah, totally. Well, it's an interesting, uh, I I'm trying to remember too, Kyle, we've done a lot of shows here and I've forgotten more than I've remembered. I remember someone, it may not have been on the show either, but I remember someone talking about like, we had a design a week going out and like, basically it was on the text to be able to like go and look up, you know, basically they'd have so many revs going that they'd have like, you know, a design goes out to get, you know, PCB manufactured and assembled and whatever. And even if you're going through a quick turn process, it's going to take, you know, three or four days. And so I'm making a change on Monday, the board's coming back on Thursday. I find a change on Tuesday, the board's coming back on Friday. You know what I mean? Like, and it's just like, it's like this ripple effect.

**Kyle Dumont:** So are they leapfrogging or are they actually able to get, you know, the boards spun up and tested?

**Chris Gammell:** I think they were leapfrogging, but they, but they, it was, it was moving so fast that they had to, they had to push these changes. And I just imagine like needing to have that information travel with that actual board coming back, like a technician opens the box on Thursday and it's a completely different set of, you know, maybe not completely different, but it is a different schematic or layout than it is on the box that it's open on Friday. And so like, how would someone go and review that using the Allspice tool?

**Kyle Dumont:** Yeah. I mean, make sure that like the, the physical board lines up with the, you know, the digital version that I'm looking at on the computer. Yeah. Actually, that's, it is, it is interesting because where we are. We are working so much on the design side of it. I don't know. We might, I might have to actually have a follow-up conversation with you about that. Cause that's, you know, there could be, maybe it's, you know, maybe it is, is having your, could be the release code, the release version in Git. Cause you can do this concept called tagging. You can tag a release. Yeah. And those can be with like your custom release tags. So version, depending on whatever company you have, but like, you know, V 0.1, or if you're using letter codes and there's certainly ability for us to like put in hooks that essentially update, you know, in big block letters, what the version is on the PCB when you, when it's done with that pull request. So when the pull request is approved, you bump that revision and then that's what goes on your PCB. So, you know, maybe that's a piece of it.

**Chris Gammell:** Yeah. I used to put a commit numbers on my PCBs. Like I thought that was very clever. But the stupid thing about that is that I would be like, all right, the commit, the commit numbers, like I've hashed basically. And it's like, usually it's shortened down to like six or eight characters. I forget what it is. Six. And so I'd like be like, all right, this is, you know, commit nine, a two F F F F one or something like that. And I'd be like, okay, I'm gonna go put that on my board. And then I'd go and like, save it and be like, oh, I should commit this. And I'm like, oh, it's a new commit now. Cause I'd like go and put it on the board. And so later when I learned about tagging, I was like, okay, this is, this is the real way. This is the real way it's supposed to happen.

**Kyle Dumont:** So yeah, that's interesting. That is funny. Yeah. I'm not sure if there's a way to do that. Like have, yeah.

**Chris Gammell:** Have it like fast forward to be like, what will my commit number be? Yeah.

**Kyle Dumont:** Yeah. Yeah. Don't do that.

**Chris Gammell:** Not easy. Cool. Well, how can people find out more about this and get started if they're interested?

**Kyle Dumont:** Yeah. So you can go to our website, allspice.io or feel free to send me an email at Kyle at allspice.io. Again, the, the diff tool there for Altium is, is free to download and free to use and will continue to be. We're also looking for, for other folks that are interested in the, the analytics and the, the, um, CI component of, you know, what, what you and I talked about a little bit.

**Chris Gammell:** Okay, great. I should probably mention too. So is there a spice component to this yet or is that kind of in, in the works? That's in the works. Okay, cool. So that's down the line. Yeah. So spice at the top, we mentioned spice. It's like, oh yeah, there's, there's spice coming. Uh, and then the final most important question, when's it going to happen, Kyle? Come on.

**Kyle Dumont:** When's the spice going to happen?

**Chris Gammell:** Nope. Not that.

**Kyle Dumont:** Oh, the, we're talking about the wedding.

**Chris Gammell:** No, no. Kyle, the KiCad. When's KiCad going to happen?

**Kyle Dumont:** Oh, when's KiCad going to happen? Um, no, we don't have a set date for that. Um, but I mean, there's so much good information there. I will say if, if any of the listeners are passionate about this piece of things, there's certainly the ability to, to bump that up.

**Chris Gammell:** Maybe we can get a signup form. Maybe like a, do you have like a blog post? Like, do you have any kind of survey information?

**Kyle Dumont:** I thought you were going to say like a petition.

**Chris Gammell:** A petition was kind of what I was thinking of like a, we want the tools.

**Kyle Dumont:** We want them now. Yeah. We, um, we've been talking about that. My co-founder and I. And so we can, we can have that by, uh, okay.

**Chris Gammell:** All right. So we're still going to be waiting. That's okay. There's enough all team users on here that I'm sure that they're going to be fine. Uh, yeah, but, uh, yeah. All right.

**Kyle Dumont:** Sweet. It'll, it'll happen.

**Chris Gammell:** Okay. Well, we'll wait for all the good, the, you know, the other spicy things that are happening anyways. So yeah. Doesn't, does all team have spice in included or no?

**Kyle Dumont:** Uh, all team does have a simulator. It does. Okay. The ability to link together models is it's been tough, but I know they're. Yeah.

**Chris Gammell:** Yeah. Yeah. And, and you'd want to have the actual like information embedded with, you know, you out drop in an op amp. You don't want to go and like look for the spice model for that op. And we want to just be there. So like, that also means that you need part information and all those models. And yeah, it just, it's that same exploding amount of data that happens with millions of parts out there. Cool. Well, Kyle, thanks so much for, uh, for joining us here. And this is a exciting new methodology. Hopefully, hopefully people fall in love with the Git methodology. Like I have, I think it's been really good for my designs and I will save it. It's, it's saved my bacon a couple of times. Yeah.

**Kyle Dumont:** Good. Glad to hear it.

**Chris Gammell:** All right. We'll talk to you soon.

**Kyle Dumont:** Uh, thanks for having me. Bye.

**Speaker ?:** Bye. Bye. Bye. ! ! We'll be right back.
