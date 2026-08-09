---
episode: 250
title: An Interview with Vic Aprea - Federated Firmware Functionalism
url: https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/
---

**Vic Apria:** This is The Amp Hour Podcast, recorded May 20th, 2015. Episode 250, with guest Vic Apria. Federated. Firmware. Functionalism.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Vic Apria:** And I'm Vic Apria of Wicked Device. Hey Vic, thanks for joining us. Hi Dave, thanks for having me. Appreciate it.

**Chris Gammell:** How is the air quality in here right now? Can you tell me how the air quality is?

**Vic Apria:** Well, if you had a certain sensor...

**Chris Gammell:** It's an air of awkwardness with that question that I asked. It is, it is. Let's start with...

**Dave Jones:** Let's start with who are you and where are you from and how was your childhood and...

**Vic Apria:** My life story, huh? Yes. Alright, so I guess I've got a background of growing up in Connecticut. And got my first computer at 10 years old or so. It was a Commodore 64. Got it from a yard sale. Got it from a yard sale.

**Dave Jones:** There you go.

**Vic Apria:** And then, you know, graduated in my adolescent years to like a Hewlett Packard PC. I believe it was a 33 megahertz PC, which was blisteringly fast for its age, right? Screaming.

**Dave Jones:** That would have been a 386 or was it a 386SX?

**Vic Apria:** Yeah, I think it was a 486DX actually.

**Dave Jones:** Oh, screaming. Yeah, I felt...

**Vic Apria:** I was pretty advanced. I upgraded its cache for the frontside burst cache to like 512K or something like that. So, yeah, that's how I got interested in computers. The Commodore got me kind of originally interested in computers. Oh, hang on.

**Dave Jones:** This was back when computers had cache memory. Cache, that's how we call it here in Australia. Cache memory, folks. Who remembers, hand up, anyone who remembers the Cache Ram scandal? The fake Cache... I don't.

**Vic Apria:** I know. I'm not familiar with that.

**Dave Jones:** You youngsters out there. Oh, quick. Let me tell you a quick side story. All right. Yeah, it was probably... Yeah, this would have been like early, mid-90s or something like that. A lot of companies out there, a lot of computer companies started realizing that people didn't really notice the difference if their cache was installed or not, right? So, and of course, I think the Chinese figured this out and they started manufacturing fake cache memory chips. Like these are... They were fake SRAM chips that you would plug into dip sockets on the motherboard, right? Okay. And so they started manufacturing these blank chips or some other, you know, non-functional chip. But you'd plug them in and they'd silk screen them so they would look like real chips. And you'd plug them into the board and, you know, all these companies were selling, all these computer companies, even knowingly or unknowingly, selling computers that had, you know, 256k of cache or so. I don't know what size they were or whatever back in... Air cache.

**Speaker ?:** Yeah.

**Dave Jones:** And it was, yeah, they were air inside. There was nothing. And of course, you know, you really didn't notice the difference unless you did real proper benchmarks and knew exactly what you were doing to figure out the difference. But then, yeah, the scandal broke and this was a huge deal at the time. Because, you know, these SRAM chips weren't cheap.

**Vic Apria:** Oh, yeah.

**Dave Jones:** Right? So, you know. So, yeah, a lot of these computer dealers, because margins were cutthroat back in the day, right? So they were going, oh, you're going to sell us a bunch of cheap SRAM case chips? Fantastic. We'll buy them. And they're, yeah, fake. Oops. Anyway, that was fun. Back to your story. Sorry. That was a little nonsense.

**Vic Apria:** Counterfitting's been around for a long time, I guess. Oh, yeah. Very long time. Yep. It's not just in the news now. Right. Yeah. So, yeah, I kind of got into computers at an early age because of that. And also took, like, an electronics course in high school. It was actually an electricity course, they called it. It was kind of like woodshop, right? Yeah. So they taught you how to wire a house. But by the way, here's about, you know, a dozen ways to blink LEDs with circuits, which I thought was pretty awesome. And so then I went to apply for college and decided I wanted to be an engineer as a result of that class. I didn't know what I wanted to do. I wanted to probably either be a computer scientist or electrical engineer. I kind of knew that from my electronics class and from kind of doing independent study on computer science because it wasn't really a subject they offered in school at the time. And so I went to university. I went to Cornell University. I went to Ithaca, New York, which is where I live now. Kind of I'm one of those guys that went to Cornell and stuck around, never left.

**Chris Gammell:** Right. Now you're the townie.

**Vic Apria:** I'm the townie, yeah.

**Chris Gammell:** Yeah.

**Vic Apria:** Yeah, I went there for, you know, I went there undecided in engineering and kind of split my course load with computer science classes and electrical engineering classes. And around about my second year, I decided staring at the computer screen was less fun than getting in the lab and blowing up capacitors. So I decided to kind of try my hand at electrical engineering. And what really solidified it for me was when I took my first class in microcontrollers. It was the second year that they had offered that class. And so I was in like the second class of it. And it's actually become kind of a pretty well-known class on the Internet. It was taught by Bruce Land. It was called Introduction to Microcontrollers. I was just looking at his stuff.

**Chris Gammell:** Yeah.

**Vic Apria:** He's awesome.

**Chris Gammell:** Yeah, he really is. Yeah, he's on the Hackaday project site. And he's big on there. And I was looking at his YouTube channel. He does like videos of all his student stuff.

**Vic Apria:** Yeah, right after I left, he started actually having the course filmed and put online. I thought that's really great.

**Chris Gammell:** That's cool.

**Vic Apria:** And actually like the project pages on that course are still available, like the historic project pages. And they are an amazing resource. Yeah.

**Chris Gammell:** Especially because it's like right at that level where it's like where you'd want to be. Like if you're kind of getting launched into it, you know, all the pitfalls that other students might be having, that kind of thing.

**Vic Apria:** Exactly. Yeah. And you can see sort of, you can read the projects at a high level. And if you want to dig into it, most of those projects all have their source code and schematics and everything up there as well, which is great.

**Chris Gammell:** I will have to dig in.

**Vic Apria:** Yeah, it's cool. So we like for my final project in that class, me and my lab partner, we made a vertical plotting machine. So you hang that from a whiteboard. It has two separate motors at either corner. And so through stepping the different motors in this kind of triangular space, you can draw rectilinear things, right? All right. All right. So our great accomplishment there was, you know, our culminating thing is we had some kind of a push-button keypad interface with an LCD. And you could type in the coordinates that you wanted it to draw to. And we made it draw square, right? It was no big deal, but it was actually really a lot of complicated math that went into that. And the funny story that goes with that is years later, I would go to a maker fair and I encountered this high school student who had a very similar looking thing. But it was drawing works of art, right? It's called the drawing machine, I think. And it was like mind-blowing. And I was like, wow, that looks a lot like my project. So I went and talked to him. And he actually said that he came across our project page as an inspiration and resource. It was like, wow. And he had done it with an Arduino instead of doing it with, you know, we had done it with like bare AVR GCC code. I mean, it's just amazing how much the barrier tree has gone down so that you can do so much more from the ground level, right? So, yeah. That's great. So that's kind of how I went through college. I guess as a – like I got out of college around 2002 when the job market was pretty soft. So I stuck around for a while to get a master's after that in engineering. So it was really an excuse to take more coursework that I didn't get around to in my undergrad.

**Chris Gammell:** Yeah. Well, and people don't know too. I mean, Ithaca – I mean, sorry, Cornell. It's Cornell, right? Yeah, Cornell. Yeah, it's in Ithaca. It is, yeah. Yeah, I mean, that's a great school overall. And, I mean, there's a lot of good people that came out of there.

**Vic Apria:** Yeah, it's a bit rural. Actually, you know, cool thing. You guys talk about like Shannon Nyquist theorem and things like that, sampling theorem. Shannon was actually a professor here, I think. I'm pretty sure. Anyway, that's my favorite famous reference.

**Chris Gammell:** Don't worry. We do maybe history all the time around here. We're pretty sure that this historic thing happened.

**Vic Apria:** I'll leave the audience to do the fact-checking. Yeah, right, right. Our comment section is our fact-checking. Comment section. There you go. Yeah. So actually, while I was a grad student, I had a kind of a unique experience where I – there was a course that I had taken that a faculty member that would have taught it normally left kind of suddenly to take a position at another university. And they were kind of – the department was in kind of a spot for finding a lecturer for it. And so I got approached by my advisor to say, hey, could you take a semester off of your grad work and teach this class? So I said, yeah, sure. I've got no rush to get out of school. So I did that for – I did that for a semester and a summer. So I taught a course in computer architecture. And I didn't do really well in the course when I was an undergrad and I took it. But I knew it backwards and forwards by the time I finished teaching it. So that's kind of –

**Vic Apria:** That's how it goes. Yeah, I'm sure you – It forces you. Yeah, yeah. I'm sure that that's – you've got a lot of similar experiences probably with contextual extronics, right, Chris?

**Chris Gammell:** Yeah. Oh, yeah. I'm clueless sometimes. But not at the end. By the end, I'm an expert. Yeah, yeah. Exactly.

**Vic Apria:** Well, it's always a lot more pressure to know the right answer so you study harder. Yeah, exactly. When the kids and students are trying to get answers from you. So yeah, I did some teaching and I really enjoyed the teaching to the point where I was actually thinking about trying to stay in school even longer and get a PhD. But ultimately, I decided to go into the workforce and I went to work for Lockheed Martin, which surprisingly is in Owego, New York. They have a big site there. And it actually was like the original IBM facility. That's where IBM started. And I was actually in the southern tier, Endicot. And so I spent the last nine years there till last year and did a lot of work on cockpit controls and displays for helicopters primarily.

**Chris Gammell:** That's pretty cool.

**Vic Apria:** Yeah. I mean, a helicopter is a pretty wild beast. Yeah, a lot of subsystems and crazy stuff, right? There's all sorts of inertial navigation systems and all these things kind of get integrated in glass cockpits now. And so I did a lot of work in sort of designing displays, doing integration and tests on them. And I just kind of had the whole tour of things you could do at Lockheed at the site in Owego anyway.

**Chris Gammell:** Yeah, right. That's interesting. Why New York for that kind of thing? I mean, just proximity to – I mean, that's not that close to New York City though, right? I mean, given geography-wise.

**Vic Apria:** No, it's four hours away from New York City. It's in the middle of – it's like right in the middle of the state. Yeah. Yeah. And so I think it's probably a heritage thing. Like it started as IBM Federal Systems, I think. So they had a government connection. And then over the many years of kind of mergers and acquisitions and yada yada, it ended up as Lockheed Martin in like the late 90s.

**Chris Gammell:** Yeah. Well, if you have talent that kind of – if IBM attracts talent around the area too, it probably makes sense for other companies to come and do the same thing there. Right. Yeah.

**Vic Apria:** It never ceased to amaze me as well just kind of the level of – there's some amazing people in the southern tier. But like you said, because of IBM. I think it's also there's like the culture surrounding that was – people that were working there had been working there forever, right? Like for like 25, 30 years. Yeah. Yeah. It was not uncommon at all to see like 25-year-old – or 25-year-old veterans there.

**Chris Gammell:** Right. Well, and it's like – I mean, the same thing happens at least around here. And I'm sure Dave could say the same thing in Sydney too. It's like when there's only so many jobs in an area, you know, you can bounce between them unless you want to uproot your whole family, which, you know, not a lot of people choose to do. It's like that's a big change.

**Dave Jones:** Here in Australia and Sydney, we – yeah, we just don't have the same culture of moving that you guys do. It's like you live in Sydney, you find a job in Sydney, you don't go, oh, there's a good job going in Western Australia. I'm going to move to Western Australia. It's just, you know, like very few people actually do that. Right. It's, you know – whereas you guys have a different culture of moving, especially for study as well, which we've talked about before, whereas we don't do that. You know, oh, you just study near where your home is. I mean, that's, you know –

**Chris Gammell:** That seems like a starker contrast though because I think a lot of people move for study, but I think less so. I mean, maybe I'm wrong about this, but I mean, I think the people that I know when they start, you know, settling down, having families kind of thing, it's like more sticking the area unless something huge comes along or there's some, you know, some big event kind of thing, you know, so.

**Vic Apria:** Right, right. Yeah, and so in the sort of – in between going to work for Lockheed and finishing up with education, I guess part of why I left education was because I met my wife in college too. And we got married here in the region as well and bought a house, kind of settled down, right? So we really enjoy the environment in Ithaca and, you know, if you can survive the harsh winters, the summers are beautiful. Right. Yeah, so – and so let's see. So that takes us kind of into – again, well –

**Chris Gammell:** Although we should at least mention Southern Tier Brewing as well. Oh, yes. I mean, that's like one of the best breweries in the country.

**Vic Apria:** Yeah, but there's also a good beer company is Ithaca Beer Company. Oh, there's another good one, yeah. Little or known, but they're very good.

**Chris Gammell:** Right, right. I guess. Yeah.

**Vic Apria:** So let's see. So around 2010, while still working at Lockheed, I met a friend through my wife's book club actually. You know, the husband's of the book club, right? Yeah, right. Natural, yeah, yeah. Who hasn't met someone that way? Yeah, exactly. So we got to talking and we had kind of a shared interest in electronics. And he was telling me in 2010 that he had heard of this thing called Arduino. And I was like – you know, he got to describing it to me and I kind of got on my high horse about AVRs and how I could program them without an Arduino. Yeah, right. You know, but eventually he convinced me to kind of have a closer look at it. And yeah, so we kind of got together on the weekends and started doing hobby projects together just to kind of – you know, when you go to work for a big company, a lot of times you don't have – you lose some of the enthusiasm for coming and doing it at home. But I did remember, you know, that I really did enjoy working on electronics sort of in my leisure time, in my sort of younger years before I went to work. And then – so that gave me the opportunity to kind of like get re-inspired a little bit about electronics. And we – I had this project that I had in the back burner that I always wanted to do while I was in college but never got around to it. It was a binary clock, which is like something everyone should make, right? Wrong. And so I – yeah, so I – we made a binary clock as a project. And I had never done much PCB design as a student. And so it gave me kind of a chance to get my feet wet on that area a little more as well. So we designed a PCB in like one of those really garbagey CAD tools that was –

**Chris Gammell:** Like the free ones from –

**Vic Apria:** Yeah, like the proprietary ones from like whatever, PCB Express, right? Yeah. That doesn't even generate Gerbers or whatever. It just generates like order now. Yeah. Which is kind of ironic, right? Like some of these web-based tools are sort of – that's kind of the model they're leaning towards, right? It's like click a button and get your board. What's the Gerber file? But yeah, so I made it originally in that and, you know, had the sort of – had the sort of usual snafu of let's go make some of these. And oh, yeah, I forgot to connect these two ground nets because the tool doesn't tell you that you didn't do that. And so we – so, you know, I had – right out of the gates kind of had my first – made a mistake in the PCB layout kind of a thing. But shortly thereafter, I was like, okay, there's got to be a better solution to this than these garbage tools, right? And that's where I found Eagle, right? Like many of the sort of people around the same era looking on the internet. Eagle was pretty popular at the time. There was no such thing as KiCad. And there was like – Yes, there was. Oh, no, it was called Geeta. It was called Geeta, right?

**Dave Jones:** Yeah, but nobody used it.

**Vic Apria:** No, no, that's different. No, no, it's different.

**Dave Jones:** But nobody used it.

**Vic Apria:** It wasn't as big as it is now. Oh, KiCad's been around that long.

**Chris Gammell:** Yeah, it technically started in 92.

**Vic Apria:** Oh, my gosh.

**Chris Gammell:** Learned something new every day. In 2007 it started, yeah.

**Vic Apria:** Well, it wasn't on the radar, I guess, in terms of popularity.

**Chris Gammell:** Right, and it wouldn't have been very – it wouldn't have been very useful, probably. Yeah, I was – yeah, so.

**Vic Apria:** So I went ahead and I kind of said, okay, well, Eagle seems like a much better tool. I'll pick that up. And I kind of – what's the word? I guess I kind of got my introduction to PCB design by Fire through Eagle, right? Oh, yeah. And so many – so like I've heard you guys say and other guests say many times, it's like the tool that you learn is the tool you stick with. Yeah. Yeah, pretty much. Yeah, I mean like – and I didn't do really any of that kind of thing like layout in my professional life or schematics. And it's kind of interesting, right? Those are like the people that do the schematics are not the people that do the layout in the industry. They're all different people. It's all sectioned off. And so I kind of –

**Dave Jones:** It depends on what company you work at but typically at a military company, yeah, I've been the PCB layout person. Right. You know.

**Chris Gammell:** Yeah, exactly. It's super pigeonholed because it's – the demands are so much higher for super fancy boards. Right.

**Vic Apria:** And you use these big cadence package – you know, cadence and mentor and all these big like packages that you couldn't possibly ever get your hands on outside of work kind of a thing. Yeah. And so I did get the chance to do some kind of test equipment work in my later years at work. And I like that better where I was able to convince some R&D manager to say, hey, get me a license of Eagle. I can do the layout and the schematics and get this done without all this kind of back and forth rigmarole with the different parts of the house doing the job. And so that was kind of fun. But it was just kind of picking and choosing spots where you could actually do that because it wasn't critical and process could be tailored, right? That kind of thing.

**Dave Jones:** Right.

**Vic Apria:** So back in like my hobby work with Dirk who's the friend of mine from the Wives Book Club friend, right? Dirk, we kind of kept doing things on the weekends and evenings and we kind of got to thinking that maybe these projects we were working on could be turned into kits and maybe other people might want to buy them. So we took the binary clock project. We called it Minty Time because it fit into an Altoids 10, as tacky as that is. And we basically put up a website and said, let's see if people would buy these things, right? And so all the work that goes along with that in terms of, okay, now we have to actually make a website and all these other things that are not electronics, right? So was this a surface mount kit or a through-hole kit? No, the Minty Time kit is totally through-hole. Right. And I would individually program the chips with an ISP programmer and stick them into black styrofoam and all that stuff, right? And that's where you learn that kits are not cheaper than dorks. That you don't want to be doing that. Because it takes a ton of work to cut resistors into lengths. I know. Yeah. So we nevertheless continued down that road and made a bunch of other kits. We've done some work on using like ASK radio transmitter receiver pairs.

**Chris Gammell:** Yeah. Is that the Minty Moat as well? Yeah.

**Vic Apria:** So it's Minty Moat. And there's also, that's actually, Minty Moat is just a derivative of the base products that I started with, which were, we called it like a wicked node and a wicked receiver. And that's, they're just like dumb ASK radio and, you know, modulator, demodulator kind of things.

**Chris Gammell:** And are you a ham holder? Are you a ham license holder?

**Vic Apria:** I am actually. That actually harkens back to another story we can go into if you want, which is I got my radio license while doing a amateur ballooning project.

**Chris Gammell:** Ah. Right.

**Vic Apria:** Yeah. We can talk about that if you want. Let's see. So one of the, so while I was at Lockheed, there was a kind of a engineering program that I got into, which had sort of extracurricular project work to do. Right. And so the project was prescribed that we would make an amateur radio frequency controlled high altitude balloon to take pictures of the nape of the earth. Right. Like the high altitude ballooning kind of project. Yep. And so we designed everything to do that from, from bare metal basically. Kind of goes to, it kind of actually is tangent to what we were talking about on email, Chris, about like the multiple MCU function.

**Chris Gammell:** Yeah, we'll talk about that later. I'd like to talk about that in a little bit. Sure, sure.

**Vic Apria:** So we actually put four AVRs into that payload. One of, like every AVR was controlling its own function, right? There was one that was talking to a VHF, UHF radio, and there was one that was talking to a camera, and there was one that was talking to a GPS, and they were all talking to each other over I squared C. And so, yeah, so that's how I got my AVR radio license, and we, that was like a five-year mission that, you know, had team handoffs from year to year. I actually ended up staying on as an advisor for it for the whole time pretty much.

**Chris Gammell:** So this was done through Lockheed or through something like a...

**Vic Apria:** It was like an educational joint venture with Cornell, like through a leadership program basically.

**Chris Gammell:** Oh, okay. Yeah. And so how many of these things actually... And what time frame was this?

**Vic Apria:** So this was... I wonder if it's online still. It was called Project Blue Horizon.

**Chris Gammell:** Okay.

**Vic Apria:** Let's see. It was like 2000... Let me see. It would be like 2006 through 2009, 2010, something like that. Yeah, if you look for Project Blue Horizon, I think... I don't know. It might be polluted with a whole bunch of other stuff now.

**Chris Gammell:** Okay.

**Vic Apria:** But anyway, it was...

**Chris Gammell:** I mean, so this was just as a basically a way to kind of do technical talent around a shared goal kind of thing.

**Vic Apria:** Yeah. It was like... It was kind of like... Right. It was a way to kind of encourage engineers to develop their skills and talents. And one way to do that is to fly balloons at up to 100,000 feet, I guess.

**Chris Gammell:** Yeah.

**Vic Apria:** Yeah. So that was... And it was... You know, there's also all sorts of other tangential stuff to doing that besides filling a balloon with helium and letting it rip. You have to actually kind of track the balloon. And it was actually really interesting. You guys designed all the systems as well? Yeah. Yeah. We wrote software and used off-the-shelf software. And we designed hardware. We had to design a... So the requirements on ballooning are that... Like the FCC... The FAA requirements, I guess, are that you have to have like a cut-down mechanism, a primary cut-down mechanism, and a secondary cut-down mechanism to be able to abort the mission.

**Chris Gammell:** And so... So that's like the balloon popping itself or what? Yep.

**Vic Apria:** That's one.

**Dave Jones:** It's headed for North Korea, folks. Right. I think we'd better... Scuttle it.

**Vic Apria:** Yeah. Yeah. Yeah. Exactly. And the other way is kind of open to your discretion. And there's a lot of different ways people have used, like using nichrome wire to burn through the load line. We actually came up with a slightly dangerous way of doing it. Dynamite. Kind of. Actually, we filled... We ended up making... Filling...

**Chris Gammell:** We used hydrogen. Or sorry. We used... Yeah. Hydrogen instead of helium. Hydrogen. We made a...

**Vic Apria:** Right. We made a zeppelin. Made a zeppelin.

**Chris Gammell:** Yeah.

**Vic Apria:** No. So what we actually did is we filled a... Like a pencil. Like a... You know... Like a mechanical pencil with black powder.

**Vic Apria:** Yeah. No, really.

**Vic Apria:** Fent an electric match into it. And triggered it through software. Right. We ignited some black powder. Like packed into a pencil to have an explosive link, basically. And so...

**Dave Jones:** I can tell you how we did several things like this in the military stuff for underwater stuff. We... When our sonar boys would hit the water, right? Of course, they had to activate. And then they had to activate the bag, right? So you had to actually fill the bag up instead of burst it. But you did have to burst it later. I'll tell you about that in a sec. But yeah, we had to fill it. So how we did that is we had a cylinder with a... You know, with the gas. I can't remember what it was. Anyway, it was a pressurized cylinder. And then a little spike thing on top that was held back with a spring. And then tied... And held back with a string, which was then tied around a... Tied around a two-watt resistor.

**Chris Gammell:** It sounds like a Rube Goldberg machine here. Yeah.

**Dave Jones:** This was highly engineered and tested, by the way. Uh-huh, yeah. String. String is highly engineered.

**Chris Gammell:** Was there duct tape in there too, Dave?

**Dave Jones:** Oh, no. It was... It was a fishing line. I can't remember. Anyway, we qualified that string to the hilt. We took, you know, months to qualify that string. Anyway, so we'd wrap it around the resistor. And then the batteries, once they... Once the saltwater battery detector was activated, then it would pass current through the resistor. Resistor would heat up. It would burn through the string. And then the spring would go down. Boom. It would burst the cylinder. Crazy. Spike the cylinder. The bag would inflate. And then everything's happy. And then eight hours later, it had to scuttle itself. So we'd burn another resistor, which was in a little pocket on the side of the flotation thing. And that would burn a hole in the flotation bag. And then the thing would sink to the bottom of the ocean. Wow. Totally a rude boat gold-rug device. Yeah. Actually, uh... But there's an amazing amount of engineering, which goes into qualifying and testing. And actually designing that and the thought process that goes through to, okay, this is the best solution. Yeah.

**Vic Apria:** No doubt about it.

**Speaker ?:** Yeah.

**Vic Apria:** A lot of hours are spent coming up with the perfect way to do something or the best way to do something.

**Dave Jones:** Yep. Totally.

**Vic Apria:** Actually, I don't encourage this, but ping pong balls filled with black powder do some amazing stuff when excited. Right. Now we're getting to the good stuff. Yeah. We weren't sure what the best kind of link mechanism would be to tie a string to on one end and tie a string to on the other end and pop it in the middle. And ping pong balls expand to an amazing diameter before they explode.

**Chris Gammell:** Really?

**Vic Apria:** Yeah, it's crazy.

**Chris Gammell:** Did you get a video of this?

**Vic Apria:** Oh, no. We didn't get any video of it because we were kind of sheltering ourselves behind a garbage disposal area. Like, you know, hiding from the blast kind of a thing.

**Chris Gammell:** Right, right.

**Vic Apria:** Getting your hands on black powder is also kind of an interesting experience if you're not a hunter.

**Chris Gammell:** Yeah, I was going to say, I'd figure with muzzle loaders, it would be pretty easy.

**Vic Apria:** Yeah. But we ended up having to dive into the middle of nowhere to, like, a gun shop. I'm not, like, an outdoor enthusiast or anything. It was kind of, you know, going out into the backwoods to get gunpowder was kind of an interesting experience.

**Chris Gammell:** Well, Cleet is selling you some gunpowder.

**Vic Apria:** Yeah.

**Dave Jones:** Well, you want to buy some gunpowder, do you?

**Vic Apria:** Oh, man, I'll never forget it. It was like some guy's house. You know? You should go Googling it.

**Chris Gammell:** No, no, Vic. That's a, it's a registered gun shop. Exactly. That's how you get around the rules. Yes. Exactly. Official. So weird. Yeah. They were having a gun show that day, of course, and that means that you don't need background checks or something ridiculous like that. You're right. Totally. That's fun.

**Vic Apria:** So anyway, we got, we actually did get some really cool pictures that first, that first flight. We got up to 100,000 feet. And over the course of all these, all these flights, there was, you know, I guess there's actual records on all this stuff. And when flights go up, you're supposed to register with the organization. I think that the project itself actually ended up having the record for the big, the highest balloon flight and the longest duration over the course of some amount of time. One of them actually grounded a flight in Nova Scotia. Oops. Yeah, whoops. It almost caused an international incident kind of thing, right?

**Chris Gammell:** Really? Not really. How are you supposed to do that? You're supposed to like notify?

**Vic Apria:** So we had GPS track on all of these flights and one of the, one of them was starting to go right towards an airport in Nova Scotia. I guess the airport, right? There's not many. And, and so, yeah, like when we had to kind of make the call of like calling up this airport and letting them know this thing is on the way and, you know, here's the way you can track it and everything else. And they ended up actually delaying a flight because of it, which was interesting.

**Chris Gammell:** That's got to be an annoying thing if you're on the plane. Yeah, for sure. Folks, we've got a weather balloon. Yep. Bunch of, bunch of nerds are doing experiments here.

**Vic Apria:** You know, you know what's crazy though? There's like a thousand balloons that go up every day. Every day? Oh yeah. It's insane.

**Dave Jones:** There's weather balloons, military and civilian weather balloons alone. There must be hundreds. Yeah. Really? Exactly. Yeah.

**Vic Apria:** Just like, just to get weather data, right? To get, to get like for, for the flight, for the flight traffic and everything else. Yeah. Yeah. I was, I was amazed by that.

**Chris Gammell:** That's how they, they actually pass back that. Are they like reusable or I don't, I think they just go off.

**Vic Apria:** I think they just go out and never come back. Like they end up crashing somewhere and whatever.

**Chris Gammell:** Huh. Yeah. I didn't know. I didn't know that at all. That's it. That actually is really interesting.

**Vic Apria:** Again, I'll probably be fact checked on that, but yeah, it's, it's a, it's a lot. And, and there's the, we actually got community involvement like across there's a whole like subculture of doing this kind of thing, I think. And, uh, this high, high altitude ballooning and, uh.

**Chris Gammell:** Within the hammer within.

**Vic Apria:** There's a lot, there's a lot within ham. I think most of the projects actually have ham connections. Um, yeah. And, and so the, so we actually hooked into the, this, uh, network called the APRS network, which, um, people might've heard of. It's, it's like, uh, I think it stands for amateur radio positioning system or something like that.

**Chris Gammell:** Yeah.

**Vic Apria:** And so.

**Dave Jones:** Hang, hang on. Hang on. I've got, I've, I've got data. Yep. I've got data. NOAA, the National Weather Service, um, they release 70,000 radio songs every year.

**Vic Apria:** Every what?

**Dave Jones:** Every year. Every year. 70,000. How many is that? Divide by 365. How many is that a day? Let's do some quick math here. Don't have my cackle.

**Vic Apria:** I've long since given up doing arithmetic.

**Dave Jones:** 191. A hundred and ninety one a day. Yeah. And that's just one organization. And they only recover about 20% of them.

**Vic Apria:** Right.

**Chris Gammell:** Wow.

**Vic Apria:** Yep. Yeah.

**Chris Gammell:** That's nuts.

**Vic Apria:** I mean, if, if they go out, I mean, a lot of, you know, the, the, the winds are often west, you know, they're easterly winds. I could, they head towards the Atlantic usually. Right. So if you're on the coast, those things are just gone.

**Chris Gammell:** Yeah. I always wonder about like, like, have you guys ever been on hint.fm before?

**Vic Apria:** No.

**Chris Gammell:** There's, there's a wind map you can look at. And I'm sure there's other ways of doing this. It might just be like ground and stuff like that. It's actually really beautiful visualization. It's hint.fm slash wind. And you can actually see live, um, live data. Cool. Of wind stuff. And I'm, so maybe this is just ground, but I always, I always just wonder about how this, how this kind of data is collected. And if it like, or like jet stream stuff, you know, stuff like really high up. Yeah. Maybe that's probably a bit, a bigger one is, is high up stuff.

**Vic Apria:** Well, you just do GPS, right? You put a GPS of some kind on the thing and you track its movement. And actually the, the, it's, it's actually crazy. The winds, the winds do insane stuff on the way up, right? There's like shearing, they change directions like, like radically at, at a layer boundaries. So, yeah.

**Chris Gammell:** Yeah. Yeah. I always wonder about the two, again, another, another outside link, but, um, recently they did the, uh, have you seen, have you guys seen the jet man? You ever seen jet man before?

**Vic Apria:** Uh, no.

**Chris Gammell:** The guy, it's like, it's this French guy who basically wears a carbon fiber wing filled with fuel and he can like sky. Oh, right. Yeah, yeah, yeah. And now there's two of them. And basically they're like commercializing this flight method, but like they're just, up there, you know, like in terms of like, like wind and all those controls, like, you know, like that's, I, I know some pilots and, and so they tell me about that stuff, but like, that's still like a, that's a bigger thing and that's a bigger device. And so I can only imagine like, like you said, with those, the shearing forces and stuff like that, it's gotta be just nuts. Oh yeah. I mean, I don't know if it's based on.

**Dave Jones:** Just imagine if you're sitting in a plane and you look down the window and there's a guy going past in his rocket backpack.

**Vic Apria:** That's, that's amazing. I can't believe someone would do that.

**Chris Gammell:** Yeah, no, there's. There's, it's a video that just came out in Dubai. It's, it's unbelievable. They're flying around the Burj, you know, like that, the world's tallest building. Like crisscrossing around it. It's.

**Dave Jones:** I would totally do that. Oh yeah. I would totally do that. If I had one week to live. Right. Oh yeah. Totally. You're right. You're right.

**Chris Gammell:** Yeah. But maybe even if not, I mean, if you're good, I mean, I don't know.

**Vic Apria:** Well, well, a balloon in the jet stream could get up to a hundred miles an hour. Just, just being there. Right. Just based on the winds. Oh yeah. Easily.

**Chris Gammell:** Oh yeah. Wow. Easily. What about like temperature stuff? I mean, how, how. That's also.

**Dave Jones:** You don't want to go above like 10,000 feet. Actually. You're, you'll freeze to death before you.

**Vic Apria:** So there's, that's really, that's really interesting actually. So, so I didn't know this either, but there's like a, there's a temperature inversion thing that happens as you go above a certain altitude and the ozone thins, I guess, you start getting hot. Okay. All right.

**Chris Gammell:** Oh, like cause you lose shielding from the, you get more like radiant energy, I guess,

**Vic Apria:** from the sun. It's not lossy through the atmosphere. Yeah. So there, there's sort of a, I mean, I wish I had all the data from it still, but I, but I'm sure it's actually out there somewhere.

**Dave Jones:** Oh yeah. Well, who we need to get on the show is Felix Baumgardner, if that's how you pronounce his name. We need to get him on the show. Okay. Come on. Tell me, Chris. Oh, is that the guy that jumped? Oh, that's the guy that jumped out of the weather balloon.

**Chris Gammell:** That's the guy that jumped from like 120,000 feet. Yeah. Right. No, that guy's nuts.

**Vic Apria:** Yeah. Red Bull. Fine line between crazy and brave are there.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. Oh, we need to get the original army guy. I think it was an army guy who did it. Um, and Felix broke his record, but he did it back in like the 1960s with just like a leather, you know, aviation helmet and, uh, you know, and calculations were underdone

**Chris Gammell:** for jumping out of a weather balloon.

**Dave Jones:** Right. And he jumped from like a hundred thousand feet or something, you know, and it's like, yeah,

**Vic Apria:** crazy. So another, another kind of weird thing with, uh, that I was worried about with GPS and the balloon was, um, I had read things that I'd read things that said that they would disable themselves above some altitude and we wanted to get up over a hundred thousand feet. And I think, uh, I think, and I think this is true actually, again, I'll be fact checked I'm sure. But I, but I think if, if you're going above a certain speed and above a certain altitude, GPS is have to like shut themselves down. So, so if you're like, if you look like a missile system or something, then I think if they're not allowed to work, so as long as, so I think we were okay because we were slow, a slow moving high, high, high object, but I think that there's, but who's, but who's

**Dave Jones:** going to know?

**Vic Apria:** Well, I guess you could always get like a, uh, a non compliant GPS or something. Right. But I think all like compliant GPS are designed to kind of like self police or something.

**Dave Jones:** Got it.

**Vic Apria:** Got it. Yeah. That was an interesting sort of thing.

**Chris Gammell:** It sounds like we need to test this now. It sounds like we need to launch something very quickly.

**Vic Apria:** I don't know if that's a good idea. Yeah. Fine. I mean, I mean, what's the worst that can happen, right? You just kind of lose whatever it is, but, um, anyway, from, from high altitude ballooning

**Dave Jones:** to eggs. Right. So what, which is what we got you on the show. Right. Right. Right. So.

**Chris Gammell:** Yeah. Eggs, you know, that sounds normal. Just, uh, balloons, eggs. They're both kind of white and roundish, but not white. Yep.

**Vic Apria:** One of them, one of them inflates to a much bigger diameter. Yeah.

**Chris Gammell:** Right. Right.

**Vic Apria:** Yeah. So, okay. So let's see, where were we? So around 2012, um, we, uh, Dirk and I got involved in sort of a community of, um, of of people interested, interested in air quality and, um, and wanting to do, uh, a project that would enable, um, more people to collect more data so that we could have a better picture of what air quality looks like, um, in, in different environments, rural and urban environments across the globe. And so there was a lot of involvement and kind of meetups, uh, in the Netherlands, in London, in New York city. And, um, kind of getting together with a couple of guys we knew through a lot of indirection, but, um, they, so Joseph, Joseph Saavedra and Ed Borden kind of were the, the evangelists, I guess you would call them of, of this, uh, community. And they want, they had this idea, this new, it was kind of a new thing at the time. This Kickstarter was, was out there and they wanted to do a Kickstarter and, uh, to, to reach a broader community audience and get, get these sensors sort of out into the field and see what, see what would happen kind of a thing. And, uh, because they, you know, we knew that we knew these guys through, um, we had, we had worked with, uh, a fellow in London, Ken Boak, who had made a board called the Nanode. Um, and that's how we kind of indirectly got connected to add through Patchy Bay, which is a company that has since become Zivoli through a couple of other name changes. Um, but the point is that, uh, we, we kind of got tapped, tapped as the, um, Dirk and I got tapped as like the sort of the engineering, um, behind that project. And, um, so we, we kind of agreed to go ahead and see what would happen with the Kickstarter. And it ended up being kind of a crazy couple of months where we, um, kind of planned out what this would be, what kind of shape it would take, what it would cost. Joe and a bunch of work on sort of redboarding and, um, proving out the technologies, these metal oxide semiconductor, um, sensors, uh, that were, uh, locally, you know, they were relatively low cost compared to sort of the things that you would find at an EPA government site or something like that. And, um, we wanted to make them be internet connected and be connected to, uh, kind of a global pool of data that people can analyze. And, uh, now what are these sensors actually measuring for? So they actually, they're actually, so what they're actually doing. Okay. So caveat, I'm not a chemist, right? But this is chemistry essentially that's happening.

**Chris Gammell:** Um, it's, they, they actually, you, you know, voltages when it comes off the sensor. Yeah.

**Vic Apria:** Right. Actually resistances, as it turns out.

**Chris Gammell:** Oh, yeah. Yeah.

**Vic Apria:** So what happens is that they, they're, they're kind of glorified variable resistors, um, that have heating elements on them. And the semi-conducting material does, it kind of inspires at a certain temperature, a selective, uh, reduction oxidation reaction, right? Like a redux reaction. And if, and certain gases are reducing, certain gases are oxidizing. And when they reduce and oxidize near the surface of these, um, wafers under the right temperature conditions, they are selective to certain species. They call them. This is all stuff kind of, I've learned in the last couple, you know, few years. Um, yeah. Um, but, but the, the, the gist of it is that, uh, in the presence of a target gas, they will change resistance in fairly dramatic ways. Okay.

**Dave Jones:** And what type of gases are we talking about? What type, what constitutes bad air quality? Got it. Got it. Yes. Is what I'm getting at.

**Vic Apria:** Got it. So, so the common pollutants, the, uh, the EPA has kind of spelled out some guidelines on what the air standards are. They're called the NAAQS, the National Ambient Air Quality Standards, I believe is what that stands for. And the gases that they've, um, identified as kind of important to pay attention to are nitrogen dioxide, carbon monoxide, ozone, particulate matter, which isn't a gas, right? But it's, and it's sort of a nebulous term, but, um, and I think lead is also on the list, which I don't really know that much about yet, but I'm guessing I will in the next couple of years. Um, so yeah, those, those are sort of the species in, in, uh, in question. They're, they're usually like sort of the byproducts of industrial processes and, um, automotive, uh, exhaust. That kind of, which is the main drive. Exactly. The main drive. Right.

**Dave Jones:** So do you need a different sensor for each one or can one do multiple?

**Vic Apria:** Uh, I went. Species. So, yeah. So you can, you, you, you, you typically have to do one per sensor, right? I wish they were that selective though. Right. Cause like inadvertently, I think you end up getting cross sensitivities between gases and, and being able to, um, separate those effects is non-trivial. Uh, so. In the air quality egg, the baseline, um, gas, we, gases we measure with, uh, measured with the unit was NO2, nitrogen dioxide and carbon monoxide. And we ended up coming up with, in the midst of the, you know, the excitement of the Kickstarter, um, there was all this like chatter. They wanted more gases and more add-ons. Basically. We had to come up with a way to, we had to come up with a way to like satisfy this, this new demand.

**Dave Jones:** Species creep. Yeah. Exactly.

**Vic Apria:** I was like, Oh yeah. When I signed up to the product, I was like, Oh yeah, we can, we can put that together. We, we've done work with, um, ethernet connected Arduino stuff. And, uh, we had an idea about it, what it would look like. And then I had to kind of bend my mind and think, how can we do this without designing five products now instead of one? Um, and so I, I kind of dreamed up a, an architecture that would allow for that, um, without growing cost and everything, uh, too much. Right. And so what I did is I ended up making a, a, uh, I guess you'd call it an abstraction layer where, um, the sensors would host their own microcontrollers and be discovered by the main controller. And we were really kind of confined by some of the technology of the time as well, um, between the cost and the technology that exists. Right. Wi-Fi was. Wait, wait, wait.

**Chris Gammell:** Uh, this is four years ago.

**Vic Apria:** Five years ago. Actually it was less. It was like 2012, right? It was like three and a half years ago.

**Chris Gammell:** I guess that's kind of crazy. Yeah. I mean, you think about, uh, what's kind of come on the marketplace.

**Vic Apria:** It's insane. Like the, the prospect of putting Wi-Fi onto a microcontroller, um, back in the end was like, no way, no way. Not for the, not for the price we were talking about. Right. We were talking, we were, we were kickstarting, the Kickstarter was like targeting a hundred dollar, um, rewards. And.

**Chris Gammell:** Well, it was also, it would be, you were looking at doing it on the micro, not micro adjacent, like with a lot of the modules that we have today.

**Vic Apria:** Um, doing what on the, on the. Yeah.

**Chris Gammell:** You said put, put, putting Wi-Fi onto the micro. You, but you meant like. Right.

**Vic Apria:** I meant like putting in a Wi-Fi link on, on, on the project. Yeah.

**Chris Gammell:** Okay. In the whole project. Yeah. Yeah. Yeah.

**Vic Apria:** So we ended up still having to solve that problem because, you know, not everyone has an ethernet cable. They can run out to their backyard to plug into the internet.

**Dave Jones:** Right.

**Vic Apria:** Like, like probably no one has that. Right. Um, so what we, so we ended up actually creating a, uh, we used, we used the, uh, RFM 12B radios, right? The, the, their FSK radios and they're in the ISM band. So they're unlicensed. And so we ended up making a two unit solution where the outdoor unit would transmit over radio to the indoor unit and the indoor unit would have a connection to an ethernet and publish it to the internet. Right. It was like four hops to get from sensor to the internet.

**Dave Jones:** And it sounds like you've blown your budget. Oh man. Yeah.

**Vic Apria:** Yes. We, uh, we, uh, yeah, it was a challenge. It was a challenge.

**Dave Jones:** Right. So is it fair to say this Kickstarter didn't make any money?

**Vic Apria:** I think that's a pretty fair statement. I'd say there was a lot of sweat equity that you can't even possibly account for. Oh, no, no, no.

**Dave Jones:** Yeah. Yeah. But, but if, if you ignore lay, like if you ignore like labor and everything else, like just purely on. Yeah.

**Vic Apria:** I mean, it's, I think it's pretty, I mean, there's probably, it's not, it's not hard to deduce that based on the fact that like, once we got through the Kickstarter and shipping them, we made the price go up quite, you know, from a hundred dollars a unit to, I think we went up to like $185 a unit. Cause you know.

**Dave Jones:** Now this is the thing that you shocked us with, uh, when we're talking just before the episode, you like, you, you, you got 927 backers. They had to make like a thousand of these things, which is reasonable enough volume, but not high enough to warrant what you bought. Right. Tell us about that.

**Vic Apria:** Yeah, yeah, exactly. Well, all right. So first, first things first, right. The, uh, the original goal of that Kickstarter was way lower than that. We were trying to just make a handful of them, but there was a lot of excitement around it at the time. And so we ended up kind of getting five times the demand and probably the price point had a lot to do with that. Right. Um, right. Maybe if it caught, maybe if it costs more like what it actually needed to cost, we wouldn't have gotten as much demand. So it's all a trade-off, but, um, so yeah. So can you say the question again, Dave?

**Chris Gammell:** Oh, um, he's asking about the manufacturing. Oh, right. You brought something to help with the manufacturing.

**Speaker ?:** Yeah, yeah, right.

**Vic Apria:** Okay, right. So. A thousand units. Sure. Yeah, right. Same luck is a good idea at the time. So here's the, sort of the background of that. So, so the, the Nanode, um, which is what we were basing the product on. It was, uh, it was, it was basically an 18 Mega 328, you know, the Arduino staple processor, um, coupled to a microchip ENC 28J60. I think I got that right. Uh, ethernet controller. So it's like a spy ethernet controller that integrates the Fi and the Mac and all in a, in a chip. It's kind of a nice, nice abstraction to the, to the microcontroller. And up to the point of air quality, like there had only existed a through hole version of it. Right. So we were like, okay, we, you know, if we get like a hundred backers, we can put together 300, uh, we can put together all of these by hand. It won't be that big a deal. Right. Right. But then we got all this, this demand. It was like suddenly the prospect of soldering by hand, these fairly complex boards, right. Um, that were all through hole became much less appealing at 900 units. Right. So I actually went back to the drawing board and I actually turned it into an SMD design. Um, with the thought of let's get this thing produced by a contract manufacturer. Right. Yeah. Well, again, like you just said, the volume we were talking about is this horrible, horrible kind of twilight region where it's so bad. And so we went shopping around and we didn't want to, well, I mean, it wasn't practical. I was not about to kind of hand over a huge check to somebody in China that I'd never met and I'm not going to fly to China to manage it. So we were shopping around locally and in the States and it was forbidding, right. The prices we were getting were like, uh, okay, we can buy the boards and then we're not going to have an enclosure or we're not going to, you know, we're going to have to like cut so much stuff. So, uh, we made this sort of hard choice to, uh, say, well, if we're going to spend that much money, we may as well do it all, bring it all in house. Right. Well, so we went out and we, we went out and we shopped around for a pick and place machine and we got a second hand pick and place machine from Mancorp actually. I think it was a similar machine to the one that Adafruit originally got. Um, yeah. And so we, we bought a pick and place machine and we were like, okay, I guess we're going to, I guess we're going to figure out how this works now. And, uh, you know, we dealt with all the sort of growing pains of that, which it's not what you, you know, you think it's going to be a piece of cake, right? It's because it's a machine. The machine's going to do what you tell it to. Um, there's not going to, but it turns out, right? These machines take a lot of babysitting. Um, getting them to work the first time takes a long time, getting them to keep working once they are working takes more time. Uh, and, and then when you really kind of sink, start sinking your teeth into it, it's like, Oh, you need more than a pick and place machine to actually make boards. You need a reflow oven. You need, you need a kind of, before you know it, you have like, you'd need a stencil machine.

**Dave Jones:** Yeah.

**Vic Apria:** Yeah. You're right. You, so you get to the point where you're like, Oh, these, these, um, mylar stencils work for about 10 boards and I have to make 900 of them do the math. So yeah, you get into like, okay, now we have to figure out how to make aluminum screens and all the rest. But you know what? It was a really good experience. I, um, wouldn't take that back. Right. Because now we know a whole lot more about manufacturing.

**Chris Gammell:** Um, so how long did it, uh, take you to actually get them all produced?

**Vic Apria:** So, uh, by Kickstarter standards, we were, we, I'd call us Kickstarter on time. We were, we were six months behind the actual deadline, but, uh, but we actually got them out the door by. That's on time. That's on time. Right. Um, and I think it actually considered all things considered, uh, that's, that's remarkable, right? That we, that we, we kind of went into this thinking we would use a lot of things that we already had and, um, ended up having to like spin boards out of thin air, right? To make it actually happen. So.

**Dave Jones:** Can I just do a small boast here? I believe I am the only Kickstarter in history. I'm sure I'll be corrected. That actually shipped the same day the money came into my bank account.

**Vic Apria:** That's awesome.

**Dave Jones:** I know. I thank you. Yes. I think there's probably, I think there's probably, there's probably a few more that

**Vic Apria:** have done it since, right?

**Dave Jones:** Right. Yeah. Maybe. I, I didn't ship them all of course, but I shipped all the, um, ones that I said I like the early backers. Right. Right. Yep.

**Vic Apria:** Yeah. That's the exact. That's, that's, that's a great accomplishment. I commend you for that. Yep.

**Dave Jones:** Hand, hand assembled. Yeah.

**Vic Apria:** Right. Yeah. Yeah. Yeah. So for us to get them out the door in six months took a lot of like friends and family volunteering. Right. Packing boxes, picking up soldering irons and stuff like that. So, uh.

**Dave Jones:** And, and it's only a thousand people have to remember it's only a thousand units. That is not a lot. Yeah.

**Vic Apria:** But you know, but you know what? The other thing you have to keep in mind is making a thousand things doesn't mean making a thousand things that work. Yeah. Yeah. Yeah. There's a little difference there. And when you have, and when you have a system that's made up of multiple boards, it's like a system of systems, you know, failure, all these things that you don't think about. Yeah. Um, kind of.

**Chris Gammell:** So did you have fixturing and testing for all the, cause you said you had a micro per sensor board as well, right?

**Vic Apria:** Right. Uh, so.

**Chris Gammell:** So how are you doing? How are you doing like firmware load there? Yep. This is kind of the conversation I want to have a little bit, but how did you do the initial, the initial firmware load? Did you pre preload firmware before you soldered the parts now?

**Vic Apria:** So I actually put an ISP header on every board. So the, so the AVRs are programmed with a six pin ISP header. Uh, it's like an in circuit system programming header. And, um, we had AVR ISP programmers and we plugged them in and ran AVR dude scripts to load them up. Um, so I did a lot of shell scripting, but it turns out that, um, you can buy preloaded chips from DigiKey for a mere 20, it's like 25 cents a chip or something. I think you could still beat that honestly, but there's a lot of frustration you could avoid too. Yeah.

**Dave Jones:** And it's almost not worth it, especially for like a thousand years, if it's 10,000, you know, like, but if it's a thousand units, yeah. Yeah. It's, you know.

**Chris Gammell:** Well, if you're doing other, other like test fixturing as well, right? So if you have like a jig where you plug in the board, you program it and then you immediately run some tests. Yep. That's different than just plugging in and programming. Right. Yep. Yeah. Yeah. So, yeah.

**Vic Apria:** So I ended up actually, uh, actually ended up writing firmware for every board, every board individually. And, uh, it was all sort of coming from a common baseline. Cause like I said before.

**Chris Gammell:** So CO2 sensor board has a different code base than NO2 sensor board. Right.

**Vic Apria:** Cause a lot of, a lot of the uniqueness to it came from the fact that the naked sensors, um, well, like they give you resistance, right? Right. Right. And they, and they span a huge range. They span like kilo ohms to mega, to like tens of mega ohms during their response. Right. And their responses are all individual. So they're all normalized by some factor that's unique to them. And all the, all this stuff.

**Dave Jones:** Oh, wait, wait. Sorry. Are you saying each one is individual or each different type is individual? Each one. Each one. It's horrible. So you have to characterize each one. Wait, really? Oh.

**Vic Apria:** So we, so the problem is we, so we didn't realize this going in, right? Cause like I said, like I said, going into it, it was, um.

**Chris Gammell:** How is it practical at all in industry though? Like, like who, who uses these sensors then?

**Vic Apria:** Yeah. So no one cares about the accuracy of them per se and what they're actually used for. They're used in automotive industry, right? That's why they're less expensive is because they're event detection detectors really. Right.

**Chris Gammell:** So they have precision, not accuracy.

**Vic Apria:** Right. They're meant to say, oh, uh, this thing is behave, this, this engine muffler or whatever is behaving out of spec, right? Like you're, you're getting a huge spike of, of, um, of pollutants coming out of it. It's not meant to say gradually. Right. So what we were thinking is that, um, originally what we were thinking in this project really early on was we can neglect all of that in the aggregate, all of this will wash away. Right. But in reality, that didn't actually happen. I mean, you could still tell quite a bit by watching the time series data. You could sort of get a lot of good relative information, but the problem is the expectations in a project like this are really varied too, right? Like the people backing the project, um, come from such a wide, wide swath of life, right? There's people that are research scientists that are interested. There's people that are, you know, like my mother, my mom in her backyard, she wants to put it out there and not care about it. She just wants to contribute. Um, and there, and there's like people that are real hobbyists, enthusiasts, do it yourself people, right? They want to get into the code and, and like mess with it. So we were trying to suit all of these very demeaning needs at once. And, um, and so that's, that's, that's a tough, uh, tough pill to kind of, to, to get the message across to that whole community that like these sensors are all unique. And, um, we ended up kind of after that, right, coming up with ways to normalize their responses. Cause if you look at the data sheet, if you look, if you look at the data sheets for the sensors, they don't really talk about this, right? They just show you a characteristic response. It's representative. Um, and they give you sort of a span of response, uh, of the normalization factor for sensors. And the circuitry, right? I actually, I actually kind of, while I was designing it, I was looking at these things. I was like, wow, this circuitry has to hopefully account for this large span of resistance, right? Just making a divider, a single value divider probably doesn't cut it because of the non-linearity across the spectrum of resistances is too much.

**Chris Gammell:** Well, even just if you're up in the mega ohms, you don't want to use a divider.

**Vic Apria:** So yeah, right. Again, things I would, things I would have, uh, would have done differently last. Yeah. I would have probably put in a buffer somewhere in there, um, but I actually made some, I made, uh, the circuit actually have sort of, uh, selectable. It was like a selectable divider. I had three resistors in series on the bait, on the bottom side of the divider. And the top side of the divider was the sensor. And what I would do is I would infirm where turn on and off subsets of the base resistor by grounding nodes on the, on the low side to give me sort of a variable span. So even though I only had a 10 bit ADC, I had like three bins in which I could do 10 bit resolution. You know what I mean?

**Chris Gammell:** Yeah. What about the, uh, input impedance on the, the micro though too? Right. I mean, if you're at the mega ohm level. No, you're right. You start to set up another divider there too.

**Vic Apria:** Yep. Yep. It's true. Um, so I think the input impedance on the AVR's ADC is like a hundred mega ohms. So it's, it's not that, it's not that big of a deal. Yeah. That's not too bad. But, um, but like, again, if I was to do it from scratch, right. I would have, I would have probably now put in some kind of a, at least a buffered amplifier. Yeah.

**Chris Gammell:** You had said, you had said when we talked before the show too, that you were, you were kind of, uh, these, some of these constraints are placed upon you, right? So you said cost constraints and then it seems like also expectations of PPMs on the sensor. So like, did you, did you not get a, uh, uh, say in that at all or what?

**Vic Apria:** Well, I had to say, but I don't think I, so, so what I, what I wanted to say is, um, what I wanted to say is like, let's just put, let's just publish the resistance, right? I understand that the world really wants to know about concentration cause that's what matters. Um, and I, and that's what, that's what kind of made me kind of concede on that point, which was like telling people resistance doesn't really answer the mail on what people want, right? People want to know.

**Dave Jones:** No, totally.

**Vic Apria:** So, but, but, uh, I also had this vision that like doing this translation at the end points on the, on the controllers also wasn't necessarily the best place to do it either. Right. Trans transforming since the data was going to go up to the internet anyway, transforming it in the cloud, so to speak, um, would have been also kind of an interesting idea, right? Like sort of treating the individuality at a higher level because the amount, the amount of processing that we had available to us at the, at the low end was limited, right? Yeah.

**Chris Gammell:** Yeah. Yeah. Linear realization is not, not trivial. It's like, you know, you need like second, third polynomial type stuff that could, that could get real messy real quick. Yeah. Yeah.

**Vic Apria:** Yeah. And I was actually doing, I was actually doing, um, you know, fixed point math all over the place. Oh, really? Yeah. Yeah. Yeah. Right. Yeah. Yeah. Yeah. It was, it was a real, it was a real, there was a lot of weeds involved, right? Right. Way down in the weeds. I'm getting all this stuff to actually, um, I actually encoded tabular transform curves.

**Vic Apria:** Oh, man.

**Vic Apria:** So I didn't do these polynomials you're talking about, Chris. I just made a table that was like, interpolate between these values kind of a thing. Yeah. Yeah.

**Chris Gammell:** Yeah. No, it's, that's how it's, that's how it's done a lot of times. It's a perfectly acceptable way to, yeah. Yeah.

**Vic Apria:** So it's perfectly acceptable, except remember the whole thing I talked about where I wanted to, um, have add-ons and have the sort of interaction be abstracted over our bus and all that kind of a thing. Well, that meant that, uh, in order to calculate a value, right, a parts per million value from the resistance, the, the, the master controller that was like sort of running the show would go out, first of all, discover that there was a sensor out there, right? So it would scan the bus and say, oh, there's a sensor at address 10 on iSquirtZ. Then it would say, oh, what kind of sensor are you? Then it would say, why don't you please tell me your entire lookup table so I can store it in my, my memory. Now why don't you tell me your resistance? And now on the base controller where I have sufficient resources to actually do the fixed point math, I could actually do the like lookup interpolation problem.

**Dave Jones:** So I, I, I would have done that right at the sensor microcontroller.

**Vic Apria:** I would have done that too, except that we put a microcontroller that had 512 bytes of RAM and eight kilobytes of flash on it. And it had to do the job of, you know, handling the bus interface, handling the, um,

**Dave Jones:** Yeah, but it's just a matter of paying an extra 30 cents for a bigger micro. Agreed.

**Vic Apria:** Right.

**Dave Jones:** With more, more resources.

**Vic Apria:** Yeah. Yeah. So like I said, like I said, right. I mean, like, I think we made some optimizations, uh, at the wrong levels in some cases, right. Kind of lessons learned there. Uh, I, I agree with you now in retrospect, putting a, a more powerful microcontroller, uh, at the node makes always a good idea, right? Yeah. I mean, if you can, yeah, if you can, like I, like I said, so in, in, so fast forward to today, right. So we, we, um, we've, we've continued shipping air quality since then. And in the meantime, we've been, we've been looking for different kind of technologies for the sensors and re-architecting the whole kind of system. Because like I said, all those hops to get to the internet are kind of, uh, there's so many chances for things to get messed up. Right. So, um, in the meantime, since all of that, I designed the board that has wifi on it called wildfire. And so all, I guess I should mention like all the stuff I've been talking about here is like open source, right? You can get all the CAD files, all the, all the source files, everything. It's all out there. Um, and so I, I designed the, uh, a, a wifi board called wildfire that. Has an 18 mega 12 84 P microcontroller on it, which is, uh, way beefier, right. Then the mega three 28, it's got like 128 K of flash and 16 K of Ram. And so like, um, it's got much more kind of resources and capabilities and it has a built in CC 3000 microcontroller or CC 3000 wifi card and an SD card and an external watchdog timer.

**Chris Gammell:** Hey, Hey.

**Vic Apria:** Cause you know, now, now that, uh, suicide mission. Yeah. Like once you, you know, once you fielded these things and you see, Oh, some of the, sometimes they lock up because you're using open source software and sometimes the libraries aren't perfect. Right. Yeah. Um, so actually I made a, for, for the wildfire actually made a custom firmware load for an 80 tiny 85 so that it can be kind of a programmable watchdog, external watchdog. So you can sort of, um, at startup tell it, uh, I'm going to pet, you know, more often than once every second and no less often than every 30 seconds. And it'll, you know, hold you to those, that contract. Yeah.

**Chris Gammell:** Right. And it'll just yank on the, yank on the power. If it, if it needs, if people don't know what a watchdog timer is that it can yank on the power, just reset itself if it doesn't get the, the pet within the 30 seconds.

**Vic Apria:** Yeah, exactly. So, or, or just the reset line. Yeah.

**Chris Gammell:** Oh, that too. Yeah. Right.

**Vic Apria:** So, so there's that. So I designed this wifi board. We put that out there as a dev board that people can use. Um, and we started looking at different sensors. We, we found a company, uh, called spec sensors that makes electrochemical sensors, which are different than metal oxide, semi-kinder, dark, their sensors. They're a totally different measurement problem, right? They, um, they're, they're like potentiostat controlled circuits. And, um, so they're like microvolt, microvolt kind of resolution changes. Yeah. Yeah. So I, so I put, I put together some, some software and boards and everything else to kind of drive those. And that's what we're basing the, uh, the new version of the air quality of gout on. And we just kind of released, um, it's kind of a soft release. We're, we're kind of a beta community of testers.

**Chris Gammell:** So it's the idea that eventually, because you have, you have this, what you called egg, egg bus, is that right? Egg bus or something? Yep.

**Vic Apria:** So the egg bus, the egg bus was something that I think was per, was, was, uh, it suited a purpose for the first version of the egg. But what I've done architecturally, I've made some pretty, I don't know, I guess I made some pretty, uh, big changes there. Right. So what I'm, what I'm doing instead of like having this add on architecture, cause that's another thing I think was, um, making add ons is really kind of nice. Making an add on architecture is really nice. Um, right. In theory. Right. It feels nice. It feels nice. Everyone's going to do it, right? Like everyone's going to. Yeah. It feels like you're doing the right thing. Right. So, so you don't have to buy it all at once and someone can pick up a new thing and the concerns are separate and everything else. Yeah. But then what happens in reality is no one ever buys an add on. They just get them together. Right.

**Dave Jones:** It's the, it's the Holy grail dream of modular electronics. Right. Right. Modular electronics development. So it's, you know, it's the Altium model.

**Vic Apria:** Yeah, exactly. So instead, so instead for the new version, what I'm doing is I'm making them complete, completely self-contained. Right. So the unit that is an NO2 and CO sensor, which is the first one we're releasing here is a single egg that has wifi and that gives you that data. So it is isolated and reports data on its own.

**Chris Gammell:** Yeah.

**Vic Apria:** Right. And so what we're going to do is we're going to come out with more eggs and they're going to do their job, right? They're going to be individual eggs. They're going to collect their information into the, you know, you'll be able to say, these are my eggs, these are my sensors, right? But they're all doing their own job. Right. And they're all, they're also going to share sort of a pedigree in terms of a lot of the software baseline will be the same, but they're going to have individual sensor management code for them. The other thing that I did on the new one, which again is like, hey, if I had more computing resources and so forth, what would I do? But going back to version one, I made it so that the software can be updated over, over the web. So like users don't have to actually know how to program a device to get a patch. Right. Right. Which, which, which when you, you know, what, when we set the original eggs out, you know, of course there were bugs, right? Cause there's always bugs. No matter what you do, there's always bugs. It's just the ones you don't know about yet. Right. Right.

**Chris Gammell:** So you, so would you say that your, your fault in that first version was just the assumption that all the users were like you?

**Vic Apria:** Yeah. I mean, I, I think I, I think, um, that's, that's a fair way to put it, I guess.

**Chris Gammell:** I think it's, I think, uh, I think that's a very common assumption, right?

**Vic Apria:** I mean, yeah, yeah, yeah. I figured that, Hey, this is all based on Arduino. This is all based on stuff that people, um, you know, in the circles that I run in are like, yeah, beginners can do this, right? But it turns out that when people are, but they will, will they?

**Chris Gammell:** Exactly.

**Vic Apria:** You can make as many video tutorials as you want about how to ISP program an AVR. Yeah. The number of people that are actually going to be able to pull that off are few and far between.

**Chris Gammell:** Right. Especially when you have something where you want it to be a distributed network, you're probably not going to be able to find a distributed network of experts that are willing to work on your project and are interested in programming it. It's much more likely to be able to find a community of enthusiasts who might want the final output.

**Vic Apria:** Yep. So I had this dream of like hacker spaces around the world, supporting their communities and doing this kind of thing. But yeah, that's not reality, right? That's just not how, how things shake out usually.

**Chris Gammell:** Um, it's not all of reality. It could be, it could happen, right?

**Vic Apria:** It definitely happened for sure. Right. There were, there were pockets that like Bristol in the UK. Awesome. Like they were able to help a lot of people out. Cool. Yeah. Chicago, same thing. I mean, like if you get into a sufficiently large population, there are people that are going to come out and, and do the, do the, do the help, you know, support role there.

**Chris Gammell:** Well, and I think the other interesting thing too is that, so, so you mentioned like, you know, the fact that you're talking about architecture, I think kind of talks about the fact that you were doing that, the, the pro engineering stuff for a long time, thinking about that ahead of time. Right. Um, but I mean, even when you're into the next, the second version, you're still architecting it for reuse, but maybe not full modularity, right? There's, there, there is a difference between those things. Well, yeah. Modularity always requires big trade-offs.

**Vic Apria:** Right. So like, for example, having, having like, having it be open source for the, in the first place, right? Having the way to program it be USB, be, you know, that's a, that's a real easy way to like lower the barrier to entry on people that might want to, you know, modify it for their own purposes. Right.

**Chris Gammell:** Right.

**Vic Apria:** Um, yeah. So yeah, your, your point's well taken. Um, modularity and, and, uh, sort of reusability are, are similar, but not, not equal.

**Chris Gammell:** Right. Right. Well, that's, and that's how, that's how you and I got in contact. You had written in actually after the last show about, you know, my discussion about firmware payloads and stuff like that. Right. You said that you had a big problem with that because you had all these discrete nodes on, on a central controller. And then actually delivering that payload is difficult. What, what, what ended up happening there?

**Vic Apria:** Right. So I'm trying to remember this conversation again, but the, the gist of it was that if

**Chris Gammell:** you've got, um, I think the gist was don't, that was your advice to me.

**Vic Apria:** That's kind of, that's kind of what I got. So it's like, it's, it's kind of ties into what Dave said about like the Holy grail and what kind of feels right. But what actually ends up happening is, uh, you end up with this, the interface has to be abstract, right. In order for it to be useful. And so making it abstract kind of inherently grows the complexity of the code that has to interact over it between you're right. You've got two different interacting software loads that have to interface over this bus. Well, first of all, that's got complexity in it to start with. Right. Second of all, every time you add an interface, you add the chance for more bugs. That's, that's sort of a, that's a, I'm sure there's actual hard research, uh, that supports that. Um, even at like, even at the like pure software level, right. They, there's, there's, uh, there's people that have done research into, uh, reducing the number of interfaces reduces the number of code, uh, bugs that you have per whatever, some metric.

**Chris Gammell:** Oh, for Piper, uh, K locks, right. That's good. Kilo lines of code. Oh yeah. Yeah.

**Vic Apria:** That's what I remember. They called it, uh, sort lines of code. Okay.

**Chris Gammell:** Yeah. Yeah.

**Vic Apria:** Kilo slot. That's for like real big projects. And I, I don't remember the last project I worked on that had Kilo lines. Wait, you worked in a military company? Are you sure? I was not a software engineer.

**Dave Jones:** I'll steal my own hobby projects back in the program and back in the eighties and early nineties with 10,000 lines of code. That's true.

**Vic Apria:** I, I, I, I kid, I guess I'm sure that if you add up all the lines of code, it's way more than a thousand.

**Chris Gammell:** Yeah.

**Vic Apria:** But anyway, yeah, I think, I think, um, I think that there is a, there's a sort of a threshold at which the complexity is merited, but you shouldn't cross that threshold properly until you have to, or until you have good reason to, until you've done the sort of tradeoff analysis, um, to justify it in your mind.

**Chris Gammell:** Well, when you say increasing the number of interfaces though, you mean, you mean trying to squeeze everything into a single package, kind of like a single firmware payload kind of thing, or do you mean something else?

**Vic Apria:** Yeah. I also, I, I actually think, um, federating the processing is, uh, I think if you're going to do that, you should do it because you need to specialize and it's code. That's not going to change likely, right? It's going to be like a code that's really stable, very simple and isn't going to change often. If it's got the potential to change, you should try and I think make, make it fit into a single sort of programmable device.

**Chris Gammell:** Um, see now this is the kind of thing where I feel like we're going to have the comment section blow up because this is, this starts to get into a lot of opinion stuff as well, right?

**Dave Jones:** Because there's a lot of, I'll use this project and it worked fine for me.

**Chris Gammell:** Right, right, right. And I use an FPGA. Right, right. But you know what?

**Vic Apria:** The other thing is the number of programmable devices you have equals the number of programming operations you have to do at manufacturing time too. Oh yeah, totally. So, I mean, like it all adds up and like, I think, I think that that's, uh, something that's often neglected is like the actual impact to a project, um, sort of on, um, on a number of fronts is related to sort of the number of programmable devices that are there. Yeah.

**Chris Gammell:** Well, and I, and I really do like the term federated too. I think that's, that's a, that I don't think I'd ever heard that term before. Um, but I'm sure, you know, it's just me not having heard it kind of thing. Oh no, I totally made it up.

**Vic Apria:** No, I'm just kidding. Oh, oh, Vic, the, the federated guy. Yeah, yeah, yeah. Yeah, yeah, yeah. That's it. No.

**Vic Apria:** Yeah. It's, uh, it's, um, right. It's the idea of, it's the idea that, uh, I think where, you know, I think where I think where it makes sense, where it's nice is actually if you've got a small team of people and you want to find ways for them to all to contribute more, it's not the way I think what I'm saying is.

**Dave Jones:** Everyone can have their own module.

**Vic Apria:** Yeah, exactly. And then you can spend time making it so they can talk to each other. But like the point is like, that's not, that's, that's something you do for that reason. You know, it's not necessarily the right design choice. Because then you need more meetings. Yeah, that's right.

**Chris Gammell:** You need more like meetings about the protocol and yada, yada, yada, yada. Right.

**Vic Apria:** And that's why, that's what happens is things get really like bloated, right? The interface gets really bloated ultimately.

**Dave Jones:** Well, I've, one of the reasons I've done this in the past, have multiple processes for multiple things is so that I can, um, so that I can show milestones. This is for, this is big company stuff, right? So I can show that module developed, tested, proven. Here it is documented. Right. Move on to the next one. It's a milestone. I can show at the monthly meeting tick, you know, right? That's another reason. Rather than putting all your eggs in the one basket. See what I did there?

**Vic Apria:** If you will.

**Dave Jones:** Right. And then, right. Trust me. Try, you know, every month I go, how's the progress? Trust me. Trust me. It'll all pop out in the end. Right. You know?

**Vic Apria:** So in those cases, I guess in those cases, do those systems that you do that for stand alone?

**Dave Jones:** They, well, they're, they're like standalone modules, kind of like your eggs. You know, they, they do their one function and then they report.

**Vic Apria:** Do they have to be, do they have to be under the control of some central authority?

**Dave Jones:** No, they can. No. The central authority just basically says start measurement and then it goes off and does its own thing and then it returns data. So, you know, it's like pinned. It's like, do your job. Give me the result back kind of thing. Yeah.

**Vic Apria:** So I'd call that a, I'd call that a federated architecture. Right. For sure. Yeah. So do you use, did you usually use, what kind of buses did you use to do that?

**Dave Jones:** Uh, all right. Serial interfaces. RS, not RS-232 electrical levels, but actual serial. Like RS-485 or something like that? No, no. It was just because it was on the, it was effectively on the same board. So you didn't need the, the voltage level translation of RS-484. Right. Yeah. And 232 or, um. Yeah. The huge swings like the minus 12 or whatever. It was all done at the TTL level, but it used serial UR. So it was all, you know, 9600 board kind of thing. And the reason I did that is so it made testing the module easy. I could test it with a PC and just hook onto the, you know, just bodge in a serial cable in and then go to the, go to a serial terminal and then send it commands and boom, it returns data. And that's how I proved that the module worked.

**Vic Apria:** No, yeah. That's a, that's a good approach. I like it too.

**Dave Jones:** Yep.

**Chris Gammell:** Definitely for the DFM as well. I think the DFM is, that is, that is a big piece there, right? I mean, being able to say, yes, this works. Yes, this is calibrated now. Oh yeah. That kind of thing. Yeah. I think that that's, but the, that's not designed for programming.

**Vic Apria:** But I mean, that comes with complexity too, right?

**Vic Apria:** Oh, it does. There's overhead in there. And you've got to like figure out like what happens when I get out of sync with my master or like if I've got like a byte that's out of phase, all that stuff kind of comes into play, right? And you end up having to write a lot of code that's like resynchronization code that has nothing to do with your problem.

**Dave Jones:** Well, see, in my one, it wasn't synchronization. It was just, it just sits there waiting for a command to start to do its thing. And then it goes, then the module does its thing. And then it reports the data back. And that was pretty much it. So it was really.

**Vic Apria:** You wouldn't build in like some kind of packet structure on it or just like some. No, no, no.

**Dave Jones:** It was purely a command. And it returned to all the serial text, you know, serial string text.

**Speaker ?:** So.

**Dave Jones:** It's kind of like the AT command modem structure. Yeah. So there's overhead there, but it meant that you could test and debug an individual module through a serial terminal and you could have, have it print out debug text and, you know, self test text, like, you know, really nice stuff.

**Vic Apria:** That's the, that's the C way of doing things, right? Print. Right. Print F everything. Right. Yeah.

**Dave Jones:** Print F everything. Yep. Exactly. Yep. And, you know, and it worked. But yeah, like if you were designing a, a module that had to put in be, you know, if you're designing a product had to be put into high volume manufacturing, it's a piss poor way to do it. Right. You just wouldn't do it that way. So. Yeah.

**Chris Gammell:** I wonder how this stuff plays into the, like the satellite side of things too. Right. Because I'm sure that, you know, like you've been thinking big NASA satellite style, not necessarily like the planet lab style, but like, you know, it's going away. It's never coming back. It needs to be updated. And there's 25 teams working on 25 modules that all have to do their thing. That would probably be an interesting.

**Dave Jones:** I suspect it's extremely modular and high level in that respect. I think it must be. It must be.

**Vic Apria:** Well, yeah. I mean, if they're, I guess I'm not sure about satellites, but I mean like the, you know, when you need, when you need, when you need a reliability like that, you use like whatever VME buses and things like that, right? Like things that are industry proven established and deal with redundant processors on the same bus and things like that.

**Chris Gammell:** Oh, yeah. I'm not talking about the interface. I just mean like the, how you actually split up who's in charge, how you reprogram, that kind of thing. Like, you know, when you need to do a firmware update for something that's billions of millions or billions of miles away, it's like, you know?

**Vic Apria:** Yeah. Yeah. So actually I, I am. So I made for wildfire, I made a bootloader. Oh yeah. Like, first of all, the AT, the 1284P has like way more space for the bootloader sector. So it can be, so I made a bootloader that is derived from OptiBoot, which I don't know if you guys have heard of OptiBoot. It's like the, it's like the bootloader for Arduino essentially. And so I took that, right? That open source baseline and I derived a new bootloader from it. So I expanded the bootloader section of the chip. But, and the other thing I've got on wildfire is an external spy flash. So what I've, what I did is I made it so that that bootloader can also boot from the spy flash. And what I did is in the application code, I made it so that it can download an Intel hex file into the spy flash and the bootloader parses the Intel hex file directly.

**Chris Gammell:** So it's like a pass through if you need to like, like a hard, hard reset. Yeah.

**Vic Apria:** So my application just goes, my application just goes up to our update server and downloads an Intel hex file into the spy flash, resets itself. And then the bootloader verifies the integrity of the spy flash as a Intel hex file. And then says, okay, I'll burn this to my memory.

**Chris Gammell:** What happens if it has a bad hex file come through?

**Vic Apria:** Well, I also include a, on the server, I include a check file, which has the size and the CRC 16 of the whole thing.

**Chris Gammell:** Okay.

**Vic Apria:** Yeah. So before it decides to burn it, it says, oh, I mean, obviously I could still screw it up by putting a bad hex file on the server with a bad check file to go with it. Yeah. Right. Right. So you have to kind of control. I see what you're saying. Like if you're in a satellite, you're done. No, no, no, no, no, no.

**Chris Gammell:** That's, that's the level. Like I could mess something up spectacularly and that would be something like how I would do it, but you can't protect for everything. So that, that's about as far as I'd expect.

**Vic Apria:** Yeah. If you're going to like a Mars lander though, you'd probably put all sorts of safeguards on it. Like there's probably parts of the code that are, they have to be fixed points or something, right? Like they have to be a, there has to be a dead beef written in this part of the memory. Right.

**Chris Gammell:** Right. Yeah. But they have like lockstep stuff too. Like they're crazy. I didn't mean that level of it. I just meant if it gets a bad hex file off the server, puts it into the spy ROM and then it decides it's not the checksum, you know?

**Vic Apria:** Yeah. So the, the fallback, the fallback then is, uh, you can still program it over USB, right? So if it gets really hosed, the software is available open source and you can down, you can still like burn it again from USB.

**Chris Gammell:** You can always just remove the chip and just program it on a chip programmer, you know? Yeah. Take it out. Come on folks. It's not that hard.

**Dave Jones:** Sock it. Yeah.

**Vic Apria:** Whack it in. There's, there's, there's, there's, there's, Right, right. A video tutorial.

**Vic Apria:** I feel like I've been here before.

**Dave Jones:** Oh goodness.

**Vic Apria:** Yeah. But I don't know. I'm, I'm pretty, I'm pretty excited about the ability to, um, to down, to like be able to push, push software updates to people. That's kind of cool.

**Chris Gammell:** Yeah. No, that's, that's really great. Uh, unless it's like, you know, a robot situation, you program the air quality egg to kill them or something. Um, right. Oh no.

**Vic Apria:** The air quality egg has all three rules intact. It's good. Okay. Cool. Cool.

**Chris Gammell:** Cool.

**Vic Apria:** And it's, it will do no harm to humans.

**Chris Gammell:** It does, it does report. People can go check out, uh, the existing eggs online at, uh, airqualityegg.com and actually see all the nodes that are out there. Um, so that's pretty cool.

**Dave Jones:** And what is your web store? What is your wicked devices?

**Vic Apria:** Our websites. Yep. Our, it's actually singular. I think, I think the plural form works too, but we're wicked device. Oh, wicked device.

**Dave Jones:** Okay. Right.

**Vic Apria:** Yeah. I, you know, that's one of those things I've often wondered if we, if we, uh, chose the right, the right, uh, the right plural singular on that one. But you know, you gotta, you kind of get what you got.

**Chris Gammell:** Yeah. Google helps. That's fine. Google helps. That's true.

**Dave Jones:** Because if it's singular, that implies you're a really small company. You've only got one product. Whereas we could devices. Oh, they must have more than one. Oh, they're huge.

**Vic Apria:** Well, yeah. Cause you, cause you get, you get the question like what, what is the wicked device? Yeah, I know. Oh, no, that's not, that's not it.

**Chris Gammell:** Oh, goodness. Yeah. And so how soon is the, how soon is the egg version two coming out?

**Vic Apria:** So it's available for sale right now. Uh, you can get it. And we actually have a roadmap that, that'll be coming out with, um, I think we're going to come out with silicon dioxide and ozone next and then particulate matter in September, I think. So we've kind of got a plan where we're going to roll these things out, uh, over time and that, yeah, that's, we've got planned basically through the end of the year for, uh, every couple of months coming out with a new one.

**Chris Gammell:** Any idea how people are using this data then, like on the backend? Yeah.

**Vic Apria:** So there's a number of interesting ways, I guess there's individual communities are, are, um, sometimes kind of pooling their eggs and, and using them as a, uh, a way to like look at relative changes in their local environment. Uh, there's a guy out in Colorado who is doing some research on the grand Valley. Uh, there's, they have some, so the part of the problem, right, that the air quality addresses is that there's these, there are, there are like really expensive government run air quality stations out there, but they're few and far between. Right. So the point of the air quality egg in many ways is to fill in those gaps, right. And to kind of see how air quality, um, varies across space at a more granular level than, you know, the three in New York state or something like that. Right. Um, so, so there's a guy in the grand Valley that wants to deploy a bunch of these to sort of demonstrate sort of how the, uh, airflow through the, like these, um, larger regions, right. Because of the geography and because of locations of various, uh, power plants and things like that. Um, he, you know, there, he's hoping to be able to see sort of a structure. A cultural trend from, from, uh, having federated sensors and there's other communities. Uh, there's, there's, uh, uh, there's a London has a big population of eggs. Amsterdam has a big population of eggs. What I'm really still hoping for is like for academics to really get their hands on these things and do sort of more statistical analysis. And, um, you know, citizen science is great and it's like a big part of what air quality serves. It could really benefit, I think, from, um, the cooperate, the cooperation with like, uh, like PhDs and things like that, that are actually in, in the field, um, that want to have an impact on real people, not just published papers. Right.

**Dave Jones:** That's great. That's great. It's a nice interface too. I like it. There's, there's quite a few in Sydney. Oh yeah. It's like a map. Like you go straight to the website and there's the map of all the eggs and yep.

**Vic Apria:** Uh huh. And there's a couple of, um, of the new ones actually that have come out to, that are, that we've shipped out to Australia, which is, which is really cool.

**Dave Jones:** I've got just one little thing. Why doesn't the color of the egg on the map change based on its, based on its value?

**Vic Apria:** Well, that's, that's a good suggestion. It's programming, Dave. It turns out that like, um, it turns out that I do firmware, hardware, web development. So it's a, it's a, it's sort of a limitation of some of our, some of our development capacity

**Chris Gammell:** there. Are you looking for help? Cause that's usually a good thing at the end of the show that, uh, people, if you're looking for people to help you out.

**Vic Apria:** Hey, I mean, always, right. It's always, it's never hurts to, uh, to make contacts with people. Sure. So if you want to email, um, email me, I guess my email address, you put it in the short show notes is my name at wicked device.com. So Victor.apria at wicked device.com. And I'll get it along to, uh, to Dirk who, who handles more of that kind of thing.

**Dave Jones:** All right. Well, thanks for being on the show, Vic. It's been awesome.

**Vic Apria:** Absolutely. It's, it's been a pleasure. And, um, you know, I, I really, it's kind of surreal to, to actually as a listener be a guest. So appreciate you having me.

**Chris Gammell:** Yeah. It was good talking to you and good luck with, uh, good luck with all the air. Yeah.

**Vic Apria:** Hopefully we'll, hopefully we'll have an impact and then, uh, it'll all kind of make our world a better place.

**Dave Jones:** All right. Nice. Thanks, Vic.

**Vic Apria:** All right. Sure. Catch you next time. Take care guys. Bye.

**Speaker ?:** Bye. Bye.
