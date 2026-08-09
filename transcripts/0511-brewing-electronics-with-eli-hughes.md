---
episode: 511
title: Brewing Electronics with Eli Hughes
url: https://theamphour.com/511-brewing-electronics-with-eli-hughes/
---

**Eli Hughes:** This is the Amp Hour Podcast, released October 4th, 2020. Episode 511, Brewing Electronics with Eli Hughes.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Eli Hughes of T0 Research and Development. Welcome, Eli. How are you? Good, Chris. As I always say, I'm living the dream, whatever that dream may be.

**Eli Hughes:** Great, great. Well, hopefully we don't sleepwalk through this one, though. You and I know each other from the Consulting Forum, also from Twitter, and most recently from me begging for some help on Zephyr, because you've done some cellular stuff recently. So thank you for the help on that. It's very exciting. Why don't you tell people a little bit about how you got to, well, maybe not how you got to where you are, but how you got to where I'm asking you for help. That's a unique question, right?

**Chris Gammell:** No, that's, well, the former question, like I'm actually having a talk next week at Altium Live that I start from growing up on a farm and how I ended up doing electronics and acoustics. But the Zephyr part's interesting. And when I saw you posted that, I kind of felt your pain. Because I experienced the same kind of pain.

**Eli Hughes:** Supporting people together, supporting each other throughout software methodologies.

**Chris Gammell:** Yeah, because when I first saw Zephyr came out in the early days, I'm a really low level, like embedded guy. And I like C, Assembly Language, Verilog, eventually got into RTOS's. Nothing, like I do some embedded Linux, but I always try to push away from that. Yeah. Just for complexity.

**Eli Hughes:** Yeah, you want battery life, you want to get low level, fast stuff, right?

**Chris Gammell:** Sometimes you just want to read an IOPIN and you don't want to do anything other than read this register. And it's that easy.

**Eli Hughes:** Yep, yep.

**Chris Gammell:** So I saw Zephyr long enough ago, I remember when it was first announced. And the first time I saw it, I was like, oh my God, Linux Foundation, are they just bringing all of this baggage to make my life more difficult than it needs to be? Because at the time, I was really into FreeRTOS. And I actually learned about FreeRTOS at a conference in Guatemala where another engineer from Mexico, he did a session. And he said, Eli, this is so easy. Copy these files. Here's how you set it up. It's ported for all these ARM Cortex. And lo and behold, we had a little NXP board. Probably 10 minutes from setting up a project, copying the files, we were doing something. Now, he knew what he was doing, but I was pretty impressed. I did not know what I was doing.

**Eli Hughes:** It's like a personified tutorial. That's amazing.

**Chris Gammell:** And that's where I started with the RTOS. And I always had a lot of arguments against it. Not all of them probably founded in fact.

**Eli Hughes:** I'd love to hear those first. So what are some of those arguments against?

**Chris Gammell:** Well, some of them, yes. Some of them, it's going to slow your processor down. You're using up time. You know, it's overly complex. Like, you need to use dynamic memory allocation, which is not true in a lot of cases. But what I kind of, there's a million reasons why. And especially if you're just used to, like, code with, like, a simple, you know, like, super loop and a handful of functions, it's, you kind of wonder why. And, you know, at the time, a lot of my applications were really, really tight DSP code and things that it was so simple not to have the overhead.

**Eli Hughes:** But yeah, I guess if you're just, if you just crank it through a filter or something like that, right? And it's like, all of the data that comes in is going out the other end. And it's just got to do this one thing. So why bother?

**Chris Gammell:** Yeah. Why bother? And even you can get pretty complicated with, you know, reading files and doing things. It's just where you tend to realize you need it. And I always, and actually, this other engineer, he, when we were talking through this, he had the best analogy. He said, all right, where, what town are you from? I'm saying, well, I'm from a little town called Kane, Pennsylvania. He says, how many people live in that town? I'm like, well, at the time, the population is about a thousand people. He says, do you have any traffic lights in town? And they're like, no, just because there's like one street. I know where this is going. All right. So we're currently in Guatemala City where there's a couple million people. How do you think it would work if there was no traffic lights?

**Eli Hughes:** Yeah.

**Chris Gammell:** You know, sure, you can do it all yourself and you can let people figure it out. But what you end up with is you have to structure a solution to deal with all this. And even if you're doing the craziest while one loop with rolling your own sort of cooperative type operating system, the whole argument about it's slow or it's bloated or extra code, you're writing that code. You're just doing it yourself. You're just choosing a structured way that's documented that other people have worked on and debugged.

**Eli Hughes:** Right. Yep.

**Chris Gammell:** And so and then I thought about it. I thought, yeah, I guess I had some prejudices that were unfounded. And it's really just being afraid of the complexity because I thought, oh, my life.

**Eli Hughes:** That's where I start. Yeah, honestly. And yeah, there was something that popped. So I mentioned on the show last week, but I've been reading a book on FreeR Toss. It's been a great book. I'll link it again. But there was something in there that really made me think about, I think it was something with the sleep code, though, too, like that sleep is just like really easy. And I really didn't understand our tosses fundamentally either. So that was another thing.

**Chris Gammell:** The other thing, and it really clicked for me, and I'm sure there's softer people out there that will like that'll probably face palming right now. But I think I'm pretty correct when I say this. If you're used to interrupt-driven code where you do a lot of things in like interrupts where at any time context can switch and you're in this interrupt doing this thing, and then you leave that thing and you have maybe a different interrupt. I mean, some of those tasks are just kind of like that, right? The process stops. You do some things with the stack. You save state. At any time, this can happen. It's just deterministic with the RToss. And as long as you're in that kind of mode of thinking, free RToss I like as a start because it's not even really an RToss to me. It's just like you set up some tasks and some ways for them to communicate. Yeah. And that's where it kind of ends. Right. It's nice.

**Eli Hughes:** Yeah, I feel like to extend that analogy, too, about the traffic lights thing, it'd be like you could have a cop who's like stopping cars when, you know, an important car has to come through. That would be like an interrupt, right? But eventually, you've got so many cops on the road that, like, basically, it's just the important cars going through. And then sometimes the cop has to talk to another cop and have to figure out which car is more important. And it's like, at that point, yeah, just have traffic lights because you shouldn't have that for everything you're doing, you know? So I definitely like that analogy of the traffic.

**Chris Gammell:** So here is where I think you kind of run into the wall where you can certainly don't need an RToss for this use case, but it makes your life, you know, more enjoyable. So I was working on a product that started about 10 years ago. It started, like all products, it started off with simple requirements. And it was actually for the pyrotechnics industry. Oh, really? Oh, okay. So is the first requirement always don't blow up unless we tell it to? Don't blow up. This was generating, like, time codes and is like a time code translator. Oh, okay. Then it added, well, we needed to decode, you know, MP3 files and WAV files and synchronize them to time code. Then we got to add, like, MIDI time code. Then we have this analog in and out. Oh, yeah, by the way, we need a file system to do all this stuff. Oh, yeah, we need Ethernet, too, because we're going to do stuff like that. And you end up having these background processes that can take a long time, and they don't need a lot of CPU time, but they're always kind of, like, blocked. And you end up, it's easy to, it's not conceptually hard to write without an RTOS, but sometimes you would like the traffic cop. And I kind of say, as soon as you say, I want USB, maybe USB host, like I had in this box, I need to do all this Ethernet where you might be blocking a lot. And you have all this stuff, it can make your life easier. It's a tool like anything else.

**Eli Hughes:** Yeah, yeah, that's great. That's great. So, okay, then let's flip it back to Zephyr, and then we'll move on, because I want to hear about this Altium talk you're doing. So, you've done FreeR Toss, relatively simple, especially because you've gotten into it over the years, and now smack into the wall of Zephyr. And what was that like?

**Chris Gammell:** A little disappointing at first. So, in one of TZero's products, we had already been using a Nordic NRF52, 52840. Love Nordic. That part, it was kind of like a breath of fresh air compared to some of the, I love NXP, but Nordic does some things, like, really, really well. And their environment at the time was really simple. I saw, like, an email saying, hey, here's this new cellular component, the FAE sent it over. I said, oh, this is awesome. I love you guys anyway. I love, you know, your software engineers. I love how you design your, you know, kind of the guts of your peripherals, because they're really simple.

**Eli Hughes:** Yep, yep.

**Chris Gammell:** Then I got the dev kit, and they're like, Zephyr. And I'm like, oh, my God.

**Eli Hughes:** Was there jazz hands involved?

**Chris Gammell:** So, when I started, I thought, okay, they packaged an IDE with it, this Sega Embedded Studio. And I thought, okay, I can at least get started. But the reality of it is Zephyr is based around CMake and Ninja, which is in this other meta tool called West. And all they did with the IDE was try to wrap up, like, the CMake list file. And it added so much complexity to something that already had a lot that I got a little frustrated, because I literally spent a solid day just trying to install the tool chain on Windows. Gave up. I said, let me do this on Linux, and it worked.

**Eli Hughes:** Yep. And by the way, this is exactly the advice that Eli gave me as well. So, it worked great.

**Chris Gammell:** Well, so, yeah. I have another colleague at T0 who's a real Linux guy, and he teases me anytime I use an IDE, and really smart. And he makes good arguments of when you should and when you shouldn't. But he was already trying to get me into the CMake Ninja flow for some of our stuff we have to maintain. And once I kind of abandoned their other tool and just said, okay, I'm going to install in Linux according to their command line build, and just read through the Zephyr documentation, Nordic did a really good job of putting a tutorial together of, like, not only how to build their stuff, but they inserted little things about how Zephyr worked. Because Zephyr, I mean, it is an RTOS. At the end of the day, you can use it in a mode where all it does is it's like free RTOS. All it does, you can have threads, you can switch, you have some queues. But what Zephyr also adds, it standardizes the build process for all these different boards. In most of your hardware interface, you don't have to use it, but they kind of standardize how you talk to UARTs and SPY. And they brought in kconfig and the device tree concept from Linux, and that's where I got really scared.

**Eli Hughes:** Yeah. So when we had Robert on the show, Robert Nelson from DigiKey and BeagleBoard, and Jason Kreidner was on the show then too, I remember them talking about some of the device tree stuff and just like, it literally, like, I literally, like, I was losing my breath because I was just like, oh, I have no idea what they're talking about right now. And they did a great job explaining it, you know, eventually, but I was just, it's a very scary concept at first. And same thing, I mean, just generally, like, building Linux, building these, you know, high level, higher level systems, it just, it feels like there's a, it feels like you're underwater because there's so much stuff above you.

**Chris Gammell:** Yeah, because at the end of the day, I'm like, okay, this has to turn into C files that bang a register. That's all it has to do. And it's all this stuff in front of it. And so the Nordic tutorial actually really helped because it explained some of the backstory of, like, why they chose Zephyr. And I'll get to why I think it's really important. But, you know, the device tree, how they use it kind of in a special way where it kind of static, you take all this stuff. At the end of the day, it makes, like, a header file that says, here's where all my registers. Here's my memory map. Here's where the UARTs are at. And it at least gets you to a point that it's pretty easy once you have Zephyr code that you can kind of move it between boards. And if you use things and they're some of their standard models for drivers, which are very thin, they're not nowhere near as complex as Linux. It was nice. And once I really got through the NRF 9.060, the value I see in it is that every time I do a free RTOS project, I'm writing the same. I'm coming up with a build system. I'm bringing in a file system. I'm bringing in all this stuff. That's what Zephyr does is you can optionally bring in all the boilerplate, like, some way to have, like, any parameters. There's always – you need to be able to, like, save parameters. You always have a couple things you need to do in code. And at least standardizes it with some decent documentation. So when you come back a couple years later, if you still remember Zephyr, you at least have – you remember what you did. And someone else is working on it as well.

**Eli Hughes:** Yeah. Yeah, that's kind of nice. I mean, yeah. It is making it, like, an extensible ecosystem insofar as that goes, right? I mean, like, yeah, there's always going to be some porting, some customization. But if you can reduce that – I mean, as a – you know, so I'm a standalone engineer. You know, I'm hiring someone to help me with getting up and running on Zephyr and stuff like that. But, like, once that's done, I'm hoping that it's just like, oh, I could pull in a new thing, pull in this other thing. That's kind of the goal and the hope.

**Chris Gammell:** So here was the thing, and my colleague, Brandon, really advocates for this, especially with – like, so we're doing, like, you know, Internet IoT-type products. And, you know, anytime you're talking on the Internet, there's this myriad of protocols and whatnot. And it's really nice to have, like, a test harness that you can test your code and abuse it, like, on a PC. And so Zephyr allows you to do that. The network stack, they have a way you can run Zephyr code with all the network and all this stuff and just run it on a PC, do all of your, you know, testing. And if you have a Zephyr port for the, you know, the network stack, you have a reasonable chance that it's going to work the same in the embedded. And Nordic really bought into this. They – their whole network library for the cellular, it just uses the same network calls as all the other stuff. So if you're trying to play with some protocol and make your stuff work, you can kind of do it in the PC and simulate it all.

**Eli Hughes:** Yeah.

**Chris Gammell:** And it's really fast and then kind of move it over. And that's – I think that's a good thing.

**Speaker ?:** Yeah.

**Eli Hughes:** Yeah. That's great. That's great. So, okay, let's switch to the – so now you're talking about this stuff at an upcoming talk at Altium Live. That's like a remote conference. What's going on there?

**Chris Gammell:** Yeah, so Altium Live, this year is virtual. It's free. They do a pretty good job of having more than just PCB type – I mean, it started out, it's a PCB conference. Some of it is Altium Kool-Aid. I'll say it's like, hey, we're great.

**Eli Hughes:** Yeah, you know, they never have any KaiKat talks there. That's all I'm saying. Yeah.

**Chris Gammell:** Well, they bring in like Lee Ritchie, Rick Hartley, who if you ever can listen to Rick Hartley – oh, my God. I don't know that name.

**Eli Hughes:** Sorry.

**Chris Gammell:** So, Rick Hartley, he's always at PCB Design West. He's kind of like a signals fields guru. Okay. If you want to learn about EMI, board level stack up, he's just a phenomenal teacher. Is he a British guy?

**Eli Hughes:** There's a couple of people that do training, and I think Lee does as well. I think we had another guest on that was talking about Lee Ritchie's training.

**Chris Gammell:** Yeah, Lee Ritchie, Eric Boguton goes to talk about like Be the Signal, that kind of stuff. Yeah. Rick Hartley is like – he really ties into that maybe in a little bit different way, but just goes into – he worked for like L3 Avionics for his career. Oh, cool. And did –

**Eli Hughes:** So, intentional radiators, big microwave dish, intentional radiators.

**Chris Gammell:** Well, he always quotes another colleague of stuff and how he hates how people use the word ground. He says, ground is where the potatoes live. It's not useful for RF. Nice. You know, it's like I've designed things that fly in the air that are low noise. Ground has nothing to do with low noise. Right.

**Eli Hughes:** Where's ground on a satellite? I remember hearing that before. Yeah.

**Chris Gammell:** Yeah. Yeah. So, but phenomenal speakers that are just good teachers. And so, my talk, I was asked by Ben Jordan, who now works for Autodesk, but he was at Altium Forever. I'm friends with Ben. Yeah. We met about 10 years ago. He got me, you know, hooked up with them before he left and said, hey, you'd be a nice addition. And I got with Judy. She says, hey, we want something a little different. And I said, you know what, I want to – I'll talk a little bit about, you know, the beer, the fermentation sensor. But also just, I think it's important to talk about engineering kind of from the human side because we've all faced some fear of approaching a new thing, asking questions. You know, I kind of want to talk about the imposter syndrome and some of the challenges I see in myself as being an engineer, having to work with other engineers.

**Eli Hughes:** As someone who's interviewed, you know, some of the top minds in the field, yourself included, I've never felt that. I never felt the inferior to every single person I talked to.

**Chris Gammell:** Yeah. And I just wanted to tell a story of kind of where I came from, starting with, like, the Nintendo Entertainment System. We were poor. We didn't have a computer. I did get a Nintendo. And it kind of started from there, and it kind of crosses over into guitars, signal processing, Sega Genesis, my college education, going through the acoustics program, getting the science of sound, and kind of leading up to this fermentation sensor and kind of putting all these hardware pieces that go from, you know, physics, which really is just, you know, the acoustics and physics, up to the sensing element, the embedded stuff, the talking to the cloud on all the cloud, you know, the, you know, the back end and kind of seeing that as a whole picture. And, you know, and I use the term, like, full stack hardware engineering and kind of being a student for the rest of your life in this concept of appreciating what other people do, respecting what they do, being willing to learn, and never trivializing what someone else does because it's perceived as easy, because it rarely is.

**Eli Hughes:** Right. Yeah. Usually it's just perception. So you dig in, you're like, oh, my God.

**Chris Gammell:** You know, and I'm guilty of that. I actually used to think, oh, those JavaScript programmers, what an easy job they had until we had to put together this back end with all these web technology. And I realized, holy crap, there's actually a lot here. And it's really easy to trivialize all this stuff we put together in the web and how you make it all, like, put something on a web, you know, this dynamic information on a web page and make it reliable.

**Eli Hughes:** I feel like, too, when I found myself doing that, usually, like, I'm, like, trivializing something or, you know, like, not giving it its due. But, like, somewhere in that chain, I'm also, like, paying, like, a monthly fee to, like, some company that's just, like, taking care of it for me. You know, it's like, oh, oh, yeah, they're doing the hard part. That's right. You know, like, just same thing with, like, you know, even, like, an AWS, right? It's like, oh, I'm paying a lot of money to AWS and I don't have to maintain a single server. Okay. Okay, yeah, that's not trivial. Yeah, yeah, totally.

**Chris Gammell:** Well, here's the other way of looking at it. Let's say they are doing the most trivial code. Could we argue, are they smarter than us? Like, because if we're working really hard to fight through Zephyr and all this stuff, they're able to... They're just rolling in cash for that easy task they're doing, yeah. Well, or they're saying, you know, we're going to keep using modern tools and reinventing ourselves and trying to make new tools to make our lives easier and not poo-pooing something else because it's not assembly language or we're not, you know...

**Eli Hughes:** Yeah.

**Chris Gammell:** You know, there's something to be said about that, but at the same time, there's an opportunity to learn.

**Eli Hughes:** Yeah, totally, totally. Well, let's talk a little bit. So, we should mention, you were on Macrofab Podcast, which we love here. You were back there over June or so, and you talked about this somewhat, but tell us a little bit about the system that you've been kind of alluding to here. What is this thing that you and your company are building?

**Chris Gammell:** So, we build a... It's called the Sonic Density Sensor. It's this little apparatus that fits in a one and a half inch tri-clamp, which is a kind of thing of a plumbing fitting. And we use sound waves to measure fluid properties. So, that's the generic way of thinking. It's a generic thing, but then tell the people the exciting thing. So, the part that gets everyone's attention is we make a sensor to monitor fermentation for craft breweries.

**Eli Hughes:** So, when you brew beer... So, Eli and his team have a set of customers that are very highly sought after. Exactly. You have friends in high places, you're saying.

**Chris Gammell:** Yeah, it's really neat because there's a lot of challenge along the way. And brewers are interesting people because they're this cross between like a biologist, you know, like a mechanical engineer and a plumber. All in one. So, yeah, they have some challenges, especially like production breweries where you're making a lot of beer in a production setting. It's a lot more challenging to say homebrew because, I mean, there's customers who want to drink. You got to get it canned. You're not wasting time and time is valuable. And the fermentation process, there's a manual way to measure it with a hydrometer, which was kind of... They use it because it's the only thing you got and it's pretty cheap. We came up with a way to do it acoustically that we can use sound waves to get kind of given an estimate of the density of the fluid. And we can also measure interaction with bubbles in the fermenter because basically the way it works is you put in sugar water. That's like the beer tea where it starts.

**Eli Hughes:** That's right.

**Chris Gammell:** You add yeast. The yeast consume the sugars. They generate heat, alcohol, and CO2. Well, we can measure the heat and we can measure the CO2 and understand, you know, how active those little critters are. And basically output apply.

**Eli Hughes:** For a consulting fee, Eli will also test the alcohol.

**Chris Gammell:** We'll test the alcohol. Well, early on when we thought, you know what, we've got to find customers and test the idea. You know, we're engineers. We're not very good at marketing and we've gotten a lot better and we've been students of this. But we said, you know what, we're going door to door. We're just going to all hop in the car, us founders. And, like, we would drive to Pittsburgh and we went to every brewery in Pittsburgh and we soon found on these trips, you can only really go to three. Because when you meet the brewers, they were, like, we met Dan at Church Brew Works in Pittsburgh. Beautiful, interesting brewery. Well, every one of these brewers, I mean, their job is to make beer and, of course, you have to sample it. Well, several of them. And that just, with three guys in a car, we can each drink so much beer and still get home and be safe about it. Right. So, you know, so that's how it kind of started is, you know, all that discovery. And, you know, what we actually, we started with the sensor, but we quickly, the reason we got a little cellular aspect is the, we quickly found out that no one wanted a sensor because they're working 60 hour weeks. These are not always engineers. There's only a few percent of them are. And even the ones that are, they're like, I'm not going to spend my whole weekend hacking something together. Like, I need to, I'm willing to pay for a solution. And that's where the other side of it, they said, you know what, I just want to look at my phone. I want to see a picture of the tank and I want to see a curve. Can I, can I be in, can I be at my couch, look at it and know yet the yeast is doing what it needs to be doing. And that's really the value we're selling.

**Eli Hughes:** Yeah. Yeah. So another thing that was interesting that I heard when you were on the Macrofab podcast was the kind of how you got to this place. It sounded like it was kind of, you know, you guys were engineers. You got paired together with some buddies and, but it wasn't like, you didn't start with the brewery idea, right? Or the fermentation monitoring idea. So like talk, talk about that a little bit. Cause it's interesting to me.

**Chris Gammell:** Well, there's a little bit of midlife crisis combined with serendipity combined with, you know, some risk taking, I guess. Sure. Sure. So, so my business partners, we actually met at the applied research lab, which is a, it's a Navy UARC, which did like undersea vehicles, acoustics, sonar, all that kind of stuff. And Stephen Wells, who is one of my business partners, he was a grad student at the time and we'd get talking. I had an E background. He had Emmy. We would just start talking about business ideas of like, Hey, wouldn't it be cool if, and we were doing this as engineers. We had, we had no idea about what a balance sheet was about how you run a business, any of that. And those ideas were, were some of them were better than others. So at some point Steve finished his degree. He went to Boeing to be a little rocket scientist, to work on Boeing for the SLS. He eventually came back and we decided to really try to make this a real company. He kind of came in my shed and said, Hey, you want to start a company? We're good acoustics, got electronics. We got some ideas. Let's start shopping it around. So we, we had a couple ideas. We tried to put together some slide decks. Really. It was more engineering focused and some ideas.

**Eli Hughes:** So almost like a, like a consultancy versus like a, an actual, like versus like a product business, you mean?

**Chris Gammell:** Yeah. And because I had been a consultant pretty much my whole career on the side. And when you're a consultant, what you do is you sell your time. You have so much of it. And the only way you scale that business is you don't make more time. You've got to either hire people or get really efficient with what you do. But it, like the scaling is really hard. Yeah. Product and services, even if it's combined with some consulting, scales different because you're building products and you bring in different people to help and you get automation. And we, coming from a research background, the consulting type thing was very natural, but it's not necessarily where we wanted to go. So we need to find someone that could help us with that. And we had a couple ideas where we put slide decks together with, okay, here's this cool little thing. Like we had this hydrogen gas sensor that used acoustics. We were pitching that as well as using acoustics to measure road integrity. Steven and his brother worked for PennDOT where they had the drag chain on a highway.

**Eli Hughes:** That's the Department of Transportation, right? Yeah.

**Chris Gammell:** Department of Transportation. And their state-of-the-art technology for determining if there was like a void in the concrete was sending out 18-year-olds on an internship with a chain. You listen to the road and it sounds a little different. And that's still state-of-the-art. That's not even a joke. That's how they do it.

**Eli Hughes:** Yeah, yeah, yeah. Wow.

**Chris Gammell:** So we said, you know, we could make an apparatus. You pull it behind a truck or something. And so we were out pitching this idea. And we were at, you know, kind of like a local event that had basically people with money looking to invest in local businesses. And a lot of it's all businesses, coffee shops, whatever.

**Eli Hughes:** We pitched our ideas. I'm imagining Shark Tank, but yeah, I realize it's not that. Mostly just because of the... Mostly because it's funny to imagine Shark Tank.

**Chris Gammell:** We were nowhere near an investable business. We were just a couple of guys.

**Eli Hughes:** It sounds almost more like a SBIR type of setup where it's like you guys would maybe chase a grant or build a thing that maybe then would turn into a business.

**Chris Gammell:** Yeah. So my first job, I did SBIR type things. And I specifically set out not to do that. And I can kind of explain why. Sure. You can grow a business that way. But I call it welfare for smart people. It's just enough money that you can hang on. But it's really hard to grow.

**Eli Hughes:** Yeah. Okay. Yeah. Yeah. So actually on that point too, because someone had asked me recently about like a... So actually the board that I've been talking about on here and elsewhere, the little board that I'm building, it's like they said, oh, are you going to try and use that as an SBIR or like a thing for that? And I was like, well, that's kind of interesting. But I would have to make a thing that is super bespoke for whatever the idea is. Right. I couldn't just be like, hey, I have this device. Who needs it? It's no, it's like, oh, we have a problem. You need to go monitor soil in sub-Saharan Africa with microamps of current. And you have to solve this very, very specific problem. And then maybe you can turn around and turn it into a business. But there's no guarantee of that.

**Chris Gammell:** And I should say, like the first kind of work for has gotten, you know, been very successful. It's a long road. The challenge of SBIRs is, and I have some personal anecdotes of experiencing this, is that a lot of times when you go to the solicitations, the contractor has already been picked. They're just going through a process to... Right. Wow. This sounds just like us, guys. We're going to get this one. Yeah. Well, the other thing is, which is disheartening. And there are, and I'll use more of a derogatory term, like bottom feeders, that they're companies that are really big, but just fit under SBIR. And their only job is their proposal writing machines. What they do is they get them and they re-contract them out, take a fee off the top to give it to the actual scientists and are adding actually no value other than that their proposal generator is taking a huge fee.

**Eli Hughes:** I mean, there's some value in not having to write proposals and deal with all that. But also, yeah, it's basically a paperwork company, right?

**Chris Gammell:** It's, yeah. And the fee is large and they get enough, they're good enough where they know what to write to turn it on. But so anyway, to kind of close that, the other story, basically we pitched the idea. We met a guy named Mark Barnhart who owned a local company, did really well. And he said, I love, I love the team. Your products suck, but your team is awesome. Yeah. You know, he said that in the nicest kind of way is that as engineers, how you, how you pitch your company and what, what you have, he believed in the team and the vision of what we were doing, not necessarily what we were pitching at the time. And that's why it's more than an investor. It's a partner that we, you know, it's this combination of like putting ourselves out there, some, some serendipity, luck, you know, all those things trying to communicate the right thing at the right time. Yep. And it all lined up.

**Eli Hughes:** Yeah. I mean, well, it sounds like the products you were doing too. I mean, like the product finding process, it sounds like that was kind of underdeveloped, like the, how you were finding these ideas that might be a good, a good thing. It sounds like you were more starting from, I have these skills. What can we do with them instead of what will someone pay me for directly? And then let me go build that hopefully with my skills. Is that, is that a fair assumption?

**Chris Gammell:** Yeah. And that's, that's pretty close. And the other challenge engineers have is you kind of start at the wrong end. You say, I'll build this thing and then find someone who has the problem. I can apply this thing to. That's right. When the reality is, is, you know, for some consumer based products, that's how, that's how it works. But a lot of times people have problems. They have pain points. It's identifying what those are and finding a solution for them, which may have nothing to do with what you're working on. And they might not even care what the thing is. It's just, you're solving a problem. It's just hard finding those. Do you really, that, that's where a lot of the, the, the work is.

**Eli Hughes:** Yeah. I'm trying to, I'm going back. I'm furiously streaming back through the, uh, the guest episodes and I'm trying to remember who we had on the show, but it was specifically about that topic. I'll, I'll keep looking as we, as we talk here, but it was specifically about the idea of like, how do you go out and find that company? Because it was my apologies. When I do find this, whoever this was, basically he had bought a technology that already existed. And then he was going to apply that to a bunch of potential industries. And basically he ended up doing that. It was like a sensor. It was like a sensor system, but it was specific selling it as an integrator then. And like finding someone who was willing to pay to solve their problem. Oh, it was, uh, it was audio or it was from the, it was for the automotive business. Anyways, I'll keep looking, but.

**Chris Gammell:** Yeah. And so, so our first sensor was, was kind of like that. And then we realized, well, no one gave a crap about the sensor. What they cared about more was the network of them and how we presented the data. Even when we showed our first partner said, Hey, look how we can build all this gobbledygook and have this awesome dashboard. It's like, okay, how does this help someone? Well, I'm like, look how we're plotting this awesome variable. He's like, yeah. So what the guy who's working, like I said, a guy or girl's working 60 hours a week. How does it help them or help their company make money? And it's, it's orienting yourself, you know, to that viewpoint.

**Eli Hughes:** That's always my, uh, my argument against. So like, you know, you hear about this new like platform, even if it's targeted to, to someone like you or me and you know, it's a, Hey, you have an IOT thingy. You're going to hook into the network and then we'll display stuff for you. And like, what is the very first thing that they're going to show you on a screen? It's like a graph. If nobody, but like, they don't, but like you said already, they, they don't care about a graph as much as the actual tank and having some kind of visualization and like making it make sense. Really. People want to know, like, is my thing good or not? Am I, should I be freaking out right now is like the main thing.

**Chris Gammell:** Well, you think about even in our own, in EE world, whether you're soldering a board or not, a lot of times you, you will dig in when you need to, but sometimes, you know, is the board on fire or is it not? Like in the case of the brewers, we made a very specific commitment to say, what we want to show is a bubbly tank. It's going or it's not. And if you care to look at it, you can, but it's like, can you look at your phone? You're in your fishing boat. You're trying to catch some walleye. You just want to know, is it going? And that's all, you know, these got the, while some of them are data scientists, even data scientists, some days they just want to sit and do their thing and know, is the thing okay. Yep. Yep. And there's, and, and we think there's value in that. And that's where we're oriented towards like underneath it's acoustic sensors. It's all this cool embedded stuff. I get a kick out of it. But at the end of the day, the customer wants like the, you know, the, the, the bubbly tank or the thing that says life is good. That's right.

**Eli Hughes:** Yep. All right. So I did find it as Jerry Roston. I will link that in, uh, Jerry. Yeah. Jerry was working for Sivionics at the time and basically he went and shopped all this stuff around. So people can go and listen to that one. So I'm curious though about this, this, this relationship then. So you said he's a partner. The, uh, I forgot Steve. Is that his name? The, no, his name is Mark. Mark, Mark, Mark. Mark. Mark. Mark. Yeah. And so, so then how does that work? So is it like, Mark's like, Hey, I'm going to float you for a couple months to go and solve this stuff or like, how does that relationship work? Because I, I think that's an interesting thing. It sounds like, it's almost sounds like a patron, you know, and like that he's willing, he's believing in the team, but the team doesn't have anything that is making money right now. So like, did you have a deadline? Did you have a, the, you know, a drop dead date or what?

**Chris Gammell:** Well, he, he, he has a saying. And so, so, so Mark's company, NPC, like it's doing a disservice to call them a printing company. But like, for example, they do SAT tests almost every, every SAT test, like say in the country where their value add is not only will we print the test, we'll mail them out, do all the corrections and do all the post-processing. So he's a really data driven guy. And he sees the, the value of data as a, some sort of service in, you know, cloud and sensors is just the same thing, just a different version of it. So being forward looking now, we started out when we look for funding saying, Oh my God. Okay. We quit our jobs. All right. We each quit in not just jobs, but good jobs with, you know, benefits. And I have kids and I'm worried about families and obligations and obligations, healthcare. It's, it's all really scary. And we said, you know what? We, we, we sought out like, for example, in Pennsylvania, there's the Ben Franklin, which offers like low interest loans. We, we went down that path, certainly, you know, direct investment. And at the time there, there was another partner who was interested, who is kind of into this fermentation business. And he said, Hey, you know what? Let's see if we can partner and do something. And it started off with a little bit of money. And Mark had this saying, and I don't know where this came from. It wasn't, it was enough to get going, but there's a saying, it says nothing motivates a person like knowing they're going to hang in the morning. So it's kind of like when you have too much and especially with engineers, well, I can order all these parts. We can do all this stuff. You're not really constrained at the same time. And an undercapitalized company is, is a problem as well. You need gas, right?

**Eli Hughes:** Sure. If you can't buy parts, if you can't buy a pizza at midnight to keep your spirits up. Yeah. I mean, there's, there are some, there are some limits, you know, you can't eat ramen.

**Chris Gammell:** Yeah. And once you realize, unless you're into something very specialized, the actual equipment costs are so much less than just, okay, can we have enough money to have healthcare and like, like

**Eli Hughes:** can keep the lights on? Sure. Yeah. I mean, yeah. Having an office, maybe not a necessity, but you know, if you need a business address, similar kind of thing.

**Chris Gammell:** Getting out of the basement was, was the first good step, you know, that made us, you know, feel like a real company. But yeah. Then from there it's, it's figuring out, and this is where it's the wild west of how do you structure more investment. And it's usually tied to, Hey, we did this thing. We have these customers on the line. Here's what they're willing to pay. Here's what we need to get to this next point. We're not going to solve the world on the next go around, but we think there's this next opportunity. And, you know, a lot of investors look at it in terms of like, okay, we'll dump a whole crap load of money at the beginning. I loved, like, I remember you had Jerry on, we're talking about the, the augmented reality.

**Eli Hughes:** Oh, Jerry Ellsworth. Yep. Yep. Yeah. Talking about the Silicon Valley stuff. Oh my God.

**Chris Gammell:** I just, yeah, we're lucky that our, just because of the local nature of it, the culture is, is, is probably a little bit slower, but it's, it's, but I, but it goes with the saying, things that kind of grow and are built slowly, like just don't fall over one day either. Like, you know, right. Yeah.

**Eli Hughes:** They're not going for a home run, but they're trying to hit a bunch of singles. Right. That's right. Chris did a sports analogy. What?

**Chris Gammell:** Well, and I think you think you, you go up to like Boston, you look at these old cathedrals that took a couple hundred years to build. I mean, they're going to be there for a while versus the McMansions that were put together in the suburbs in like three months. Yeah.

**Eli Hughes:** Yeah. Yeah. That's a good point. Yeah. But still, I think that, I think the interesting thing is the, you know, at some point someone, okay, so there's the assumption it's going to take a while, but they're believing in not much more than brain power, right? I mean, that's. Yeah. There's, that's the risk. That you, you were going to go out and find the market too. I mean, that, that's always interesting.

**Chris Gammell:** Yeah. And it's, it's, it's a balance of getting some perspective from someone who's not an engineer, but is really good at say sales and marketing to, to help coach you into, okay, when do you need to add a salesperson? When should you add marketing? And the answer is you should be selling it before you even have it. You should be talking to people. You don't need to build the whole thing and solve every problem. Like, you know, that's the wrong thing to do.

**Eli Hughes:** Yep.

**Chris Gammell:** You know? And so then it grew from there. So the brewery that obviously you can look at the market and say, well, there's this many breweries that need eight sensors. If we can deploy it this way, so we don't have to be there and we can make this much money, but then, then it evolves to, Hey, this sensor also works for.

**Eli Hughes:** Yep. Yep.

**Chris Gammell:** You know, this other thing. So if right now we're investigating like precision glycol, measuring the cooling systems for the, you know, for the fermentation tanks, as well as for other expensive fluids, where if the cooling system goes down, it could be a hundred K in impact.

**Eli Hughes:** Yeah. Yeah. Yeah. Yeah. Yeah. I feel like I was just talking to a buddy about this and it's like, there, there's no easier sale than like saving someone money, right? That's like a FUD kind of, you can sell based on FUD of fear, uncertainty, doubt, whatever. But like, if you tell someone that you're going to put money in their pocket or keep money in their pocket, that is so much easier to sell than like, Oh, this thing might be kind of cool. You know what I'm saying? It's not a nice visualization. It's like, no, you're going to save a crap ton of money. Then it's easier to sell. I think at a higher price too.

**Chris Gammell:** I believe you actually, you, you were having a discussion with Dave of like the internet of shit, like with, with a lot of the consumer, with the consumer products where it generally falls apart. But you said like IOT does have a space and I think you even said IOT just kind of means money.

**Eli Hughes:** That's right. Yeah. Yeah. Yeah. Because I guess I can't really agree with that since I was saying, well, I agree that I did say that. Yeah. Yeah.

**Chris Gammell:** Yeah. So, and I actually just, I wrote a little thing on Altium. They, they have a little section for new projects. I did something on the NRF cellular, you know, doohickey, but I, you know, I mentioned that, you know, the value proposition of cellular when you couch it, not in like a consumer good, but you're monitoring a machine instead of sending a technician, you can be looking at it all the time in the cost savings of just that.

**Eli Hughes:** Yeah.

**Chris Gammell:** It's incredible. There's actually a local company. That's all they do with vibration sensors. You know, they send out these things, they beam it up over cellular. They have people like watching it on the other end and call, Hey, you know, sawmill number nine, it has a vibration. You might want to check this out.

**Eli Hughes:** Oh, it's literally, literally people like watching. Literally people. Wow.

**Chris Gammell:** Because they actually started out like an engineer where they said, you know what, we're going to make this awesome wifi connected thing. We're going to train the companies how to look at FFTs and power spectrum. We're going to go deploy it and sell them a piece of hardware. And it worked for, it did work for a while, but the minute they said, you know what, there were so many challenges with wifi in those environments. They said, yeah, we're going to do a cellular. We can say there's a cost to that, but there's always a cost to networking. And instead of training them, let's hire people and train people just to look at the data.

**Eli Hughes:** Yeah. Like a scale of scale economics, right?

**Chris Gammell:** And they can write their own scripts to know what things to look for. And the company, I mean, for millions of dollars of revenue to $50 million in revenue in a few years. Oh, wow.

**Eli Hughes:** Wow. Yeah. There's one that started out of M hub called Amper. There's two actually, there's Amper and Amber. And it was just like, oh man, actually they started out of hacks. They ended up at M hub though. And they did the same kind of thing, but they did it based on the power of like industrial machines. So like knowing cycling of when things are on or off. And like, I think they've been moving towards like an AI solution, but at the beginning, yeah, they were just like cranking data of basically just monitoring the power going into a machine and being like, oh, look, your machine's down. It's not, there's no power going into it. It's down. There's something wrong with it. And that alone, you know, that versus like bill, the floor technician who might be, you know, having a bad day, he's nursing a hangover, whatever. He just doesn't notice for two hours. And that literally translates to money. And it's like, you could start to be like, look, you're, we don't, it's not that we don't trust bill, but like, you don't have to anymore. You know, that's the best part about it. So that's when that becomes money.

**Chris Gammell:** And even when it's even as crazy as it sounds in the case of KCF of sending it is having people trained to look at a lot of these problems aren't milliseconds in time, because that means there's like sprockets and gears on the floor. And you know, there's a problem. It's, it's over days or weeks that you notice a trend. And when you can go to a customer and say, Hey, your half million dollar machine that's driving a million dollar a day process, there's a problem. And then you can, you can plan it. And so, so we, we've, that's there, there's a lot of room in that space. So it's everything from us, from the beer sensor to the glycol. We're looking at this new synthetic biology. We have a solution for oils, oil, you know, oil spill detection under the machine. So nice.

**Eli Hughes:** And so, okay. So then are you making a, is it a genericized platform then? Like, can you zoom back and just swap out what sensors in there or how, how are you, how are you making it flexible enough to, to work in all these scenarios?

**Chris Gammell:** So, so one thing we decided and we, we learned this as we went, the, the fermentation side of it actually really helped because a lot of people think in terms of, okay, I'll hook up these sensors and we'll make dashboards of sensors. Well, no one cares about like the sensor. They want to know like information. So what we, what we came up with, with kind of the generic way of plug the sensor in, but don't do the data, a lot of data processing there. And the fermentation case, the algorithm is actually pretty complex. Reduce it just enough to keep your software. Yeah. You know, just enough on the sensor side, get it up to the cloud because computing is nearly free so that all the fermentation algorithms are in the cloud and it makes firmware so much easier.

**Eli Hughes:** That's right. Yeah. And like pushing changes too. It's like you could rerun the same data set a thousand times and it's no big deal instead of like download, test, wait, wait, wait, analyze results.

**Chris Gammell:** Oh, that's exactly how it works too. Yeah. So in the case of when we're looking at a customer that maybe had a complicated fermentation that we'd have a model for, they said, Hey, give us a week. I, you know, I literally have a simulator tool that we can run it through our algorithm, make, you know, understand this data, you know, a lot more. And then when we want to deploy, we can choose, Hey, we can deploy it. If this customer wants it, we don't have to touch firmware anywhere, as long as we're pushing up and it makes the problem so much easier.

**Eli Hughes:** That's really cool. So then what about, does that impact a battery or data costs or other things? Cause that feels like the thing that would have, I would be a little more worried about.

**Chris Gammell:** So on the battery side is I will push everyone in the world, unless you absolutely need a battery, don't use it. And the reason is, is like we started off in looking at all these network technologies, even from a previous life of things like a mesh network, we say, I want to have a thousand battery powered sensors until you realize, let's say you can get three years out of a thousand sensors on average. How often are you changing a battery? Yeah. Like really quick. Yeah. And it's, and these aren't $1 batteries from Walmart. They're more expensive lithium primary. A one, two, threes or something like that. Yeah.

**Eli Hughes:** Yeah.

**Chris Gammell:** Something that you've got to pay a lot of money for.

**Eli Hughes:** And then especially. So, so what was, what was the result of that though? You're saying just don't use them at all. I mean, what if, what if you don't have a choice though?

**Chris Gammell:** Well, certainly if you don't have a choice, there are applications, you have to use it. And for example, you do use it, but if, you know, I'll always push because anyone who's actually had to deploy it and maintain it will understand that value. Then it comes to, you know, the cost of. And I'll tie this into the cellular aspect because. And I'll answer kind of those things in one go is, you know, a comment might be as like, Hey, why aren't you wifi? Wifi is free. And like responses, well, well, you're going to pay for data at some point.

**Eli Hughes:** That's right.

**Chris Gammell:** And. And here's what, here's what happened with wifi is that, or even things like wifi, you would walk into say a brewery or a plant with your, your fancy sensor, ready to send it up. A you're already burning money. Cause there's someone there. You walk in and there is a old links, this router in the closet with like the default SSID and password. That's right. You set it up and you hold your nose and you realize it's down half the time because that same thing is being shared by all the patrons in the brewery or all the office workers it's going down and.

**Eli Hughes:** Or there's a solenoid firing right next to it. It knocks it out. Exactly.

**Chris Gammell:** And they're calling and saying, why is it down? It's your fault. All right. That's one side of it. The other side is there's actual network staff that monitor the network. And they're like, there is no way in heck you're plugging your little IOT device anywhere near our network. Fill out this paperwork, do this audit in maybe a month where, you know, you can install it and just assign a dollar. What does a network engineer cost?

**Eli Hughes:** Yep.

**Chris Gammell:** At $150 an hour for a good cybersecurity person. I can pay for years of cellular if we're delivering that service. Because we're not talking $80 a month like consumer cellular. When you really boil your problem down, you can get sub dollar per sensor if you really understand what your sensor needs to do. So we like that because the question then becomes, if you can't justify, you can kind of put a number to the movement of that data and say, can we, are we saving this person enough money that it justifies this? And if you can't do that, should you be doing it? That's kind of where it comes out. And same thing with the battery power is that if you're watching a process that's really, really important, does wiring, is wiring it in the end of the world. And in the case of the sensor for the glycol and the fermentation, it was acceptable. No one cared about, okay, we're going to run this cable over the sensor and this little box plugs into the wall. And from there, they didn't have to plum in a, like a drop for ethernet or anything. It wasn't a big deal. It talked from that point.

**Eli Hughes:** Yeah. Okay. Yeah. That makes sense.

**Chris Gammell:** It was just a nice, it's just something we found over and over and over again that it actually saved everyone money. Yeah. You know, in the long run.

**Eli Hughes:** Yeah. I mean, you could still put a battery on there for backup too. Oh, yeah, certainly. Yeah.

**Chris Gammell:** Usually the problems are if power's down and everything else is down, getting that data, there's other things you're worried about a lot more than, hey, I can't read the sensor.

**Eli Hughes:** Like the plants. Is everything down because the tank's leaking and the whole thing's flooded?

**Chris Gammell:** But maybe, maybe you want to know that, Eli. Maybe you want to know. Videos on YouTube of like, you know, brewers playing with a tri-clamp, something fails and you have. Really? Oh, it's pretty awesome because, so in the U.S. they measure in like barrels and it's like 30 some odd gallons per barrel. You'll have these tanks with hundreds of gallons or thousands of gallons of fluid. They're huge. Yeah. And imagine all the pressure on a little one and a half inch opening at the bottom when that bursts. And you're not stopping. Right. Right. So when that happens, our sensor can't help you. That's right.

**Eli Hughes:** It's like the episode of I Love Lucy, except it's not chocolates flying out of a conveyor belt. It's liquid that could cut steel. Yeah.

**Chris Gammell:** And so, and so, yeah, like I said, a lot of these things just come from, you know, some school of hard knocks and taking advice from other people have gone down that road of when you can, you know, translate it into dollars. Because sometimes your initial assumptions aren't, you know, the ones you end up, you know, going with.

**Eli Hughes:** Yeah. I think it's an interesting thing too, because it's, in your case, you're, this is going to be flavored a little bit from, I was just literally just talking to my friend about like system integrators. But in this case, it seems like you're taking this whole system all the way up through being a system integrator because you're actually just offering data, not even data. Like you're, you're offering results, you know, on a web platform to the, to the end customer. And so in that, in that scenario, you're, you are also the system integrator. So you don't have to worry about like, you're going to figure out a way to get it plugged into the wall. You're going to figure out how this clamp is supposed to go on there. I think it would be slightly different if you were like shipping it to someone. You're like, Hey, plug this thing in and hopefully it all works.

**Chris Gammell:** Well, that's actually what we do. And like, Oh, you do. Oh, okay. Oh yeah. So what's nice about the cellular. It's the only thing that, because we kind of designed the sensor to go into these, these tanks that in 10 seconds, you're in the tank. It's all stainless steel. Nothing touches the fluid except stainless steel. You click it together. You get some lights. Like if you have AC power and you can click like the, or screw an M12 connector, threaded connector, probably in about 30 seconds, you have data. And it's really hard to argue that that's not the way. And we've been shipping to Juneau, Alaska, Canada, you know, Mexico, all over the country. And how many, how many breweries are there in the States or in the world? Oh boy. In the United States, this is always changing. There's probably, depending on how they're classified, six or 7,000, you know, in this craft region. Okay. But then there's these, all these other things of like, like I mentioned, we're now into not only doing the breweries and the, you know, you know, that tank. Well, every one of those tanks needs active cooling during fermentation. Well, that's driven by a chiller, which runs glycol through the system. Well, glycol needs to be at the proper mixture to have the right freezing point. And if that's not right, the compressor, the heat exchanger, things that cost 10, 20, 30, 40, $50,000 to go down. And if we can ship out a sensor that, Hey, you kind of, you drop it in, you connect the cell and you get the widget on the other end that says, Hey, the glycol is okay. It's a pretty easy cell.

**Eli Hughes:** Yeah. I think the hard thing for us as people that are interested in technology, we say like, Hey, don't people want to know what's in between? And the answer is almost always no. You know, they don't, they don't care. They want it to just show up and be magic.

**Chris Gammell:** They want to know what's the freezing point of my glycol. What's the percentage. Right. So, so for example, like here is a use case for like the glycol system. So glycol is used everywhere as, you know, a fluid for exchanging heat. You don't use pure glycol because it's too thick. You usually mix it with water and it changes where it's like freezing points at. Well, if there's too much water, it gets slushy. Right. And it's, it'll, it could freeze and cause problems. Well, say at Penn state university, which is local to us, they have an office, a physical plant. Like every building have these giant, like, you know, train or carrier air conditioning units. They literally have to send a guy, you know, to get up a ladder. He takes out a refractometer. It's an eyeball measurement to figure out, okay, what's the glyc, you know, what is it? You know, and replacing that with, okay, we can charge you this amount of money. You just know, you know, you can see it. And if you want to see a trend, we can have a little widget that says, Hey, you know, you know, there's something wrong here.

**Eli Hughes:** Yeah. Yeah. Yeah. I've been saying, I think I've probably said on the show before, but I think my, my paycheck for the next 10 years is replacing that guy. Not in a bad way, but because just, you can, you know, you can work with one guy instead of four. Right. Or you can, you know, if you're a, or, you know, if the guy's on vacation, you, you don't, you know, you're not able to check on this thing. Right. You know, it's basically replacing that person is the value proposition. That's, that's where you're saving the person. That's where you're saving the company money. Or they get to be repurposed for something. Sure. Yeah. That's the best, the best case. I feel like I'm never good at selling that kind of thing. Cause I'm like, I'm going to help you get rid of people. But what it really is, it's like, yeah, it's, it's increasing efficiency with some like remote tech thing, you know? Yeah.

**Chris Gammell:** And I think when you look at it, I don't really have a whole lot of evidence for this, but when you look at any change that people are really scared of, that it's going to eliminate jobs, think about every step along the way. Sure. Cars replaced it. People to, you know, had to get on, do the horse and carriage, but we have more people than ever. And they're, they're still working. The car didn't mean everyone went out of work. Yeah. And actually more people were now employed because we found other ways to use these tools to do things. Like I, I personally want to get to the Star Trek future. Yeah. You know, not be, you know, where, where we can use these tools so we can do it, be doing the really important things for humanity. Beer is a starting point.

**Eli Hughes:** Hey man, you got to have beer, right? It's part of every great civilization, I think. Yeah. It's been on for water. It was for water quality, but you know, it's still, it's still valuable.

**Chris Gammell:** Now we're moving on to like the glycol. People like things cold, whether it be their beer or their ice cream or their building or their process. Right.

**Eli Hughes:** Or their, how about, how about we say vaccines, you know, vaccines have to be kept cold. There's a great Wendover productions video about like the logistics of like shipping out a bunch of COVID vaccines. Oh my God.

**Chris Gammell:** Yeah.

**Eli Hughes:** Very interesting. It's tough. Yeah.

**Chris Gammell:** So, so, which is a great lead in. So, and it just wrapped up. I was, I was at this con online conference, uh, sin bio beta, um, for synthetic biology. And that's, that's where I get, I'm getting really excited because looking at this tool that started with breweries and moving in the HVAC is like, I'm not a biologist. I'm not a synthetic biologist, but after I caught wind about a year ago through a student I had when I taught at Penn state, he was a computer science about what this was. It, it totally blew my mind.

**Eli Hughes:** Yeah. Yeah. Yeah. This is like trying to make fake life, right?

**Chris Gammell:** Well, what, what I found going to the conference there, it's like a fork with multiple tines and there, there's different stuff. And I'm, I'm, I was there to, to learn more about the fermentation aspect. And today I was just in a session where they're talking about fermentation and giant tanks and think about bio farms of as far as you can, I see, instead of fermenting beer that they figured out how to ferment a protein that is very similar to a protein that's in mother's milk. So for mothers who can't produce breast milk or having trouble, they can synthesize it. Yeah. Dairy replacements. And for example, the impossible burger, you read about, you know, Burger King marketed it. Well, if you read about that, one of the proteins that the heme that's actually fermented that they, they discovered instead of scraping this gunk off the, the roots of soy, they can use a fermenter and use yeast as like little machines to do our bidding. Yeah. Yeah.

**Eli Hughes:** Yeah. Yeah. I'm really excited about the crossover at some point. Like when you think about like replication of like just lots and lots of little things, it's like, okay, you know, you start to like your brain, my brain at least starts to like drift towards like, Hey, there's a lot of little machines in Silicon and things like that. And like, just thinking about like, how would you actually assemble chips using, you know, viral delivery, things like that. Like there's, there's some very interesting, very sci-fi kind of things in there. But in terms of like the, the ability to do tiny things many, many times over, it's like, yeah, I think you've got to go the bio route. Like it's, it's pretty cool.

**Chris Gammell:** Yeah. That's kind of nature's figured that out for us, that that's how a lot of the universe works. It's a little, little process. And I just, it was, it was amazing for me as like electrical engineering and acoustics background coming into this conference, just saying, Hey, I'm here to learn and finding out everything from, you know, you know, the, the mother's milk replacement to all this, there's a lot of talks on COVID and vaccines, all this DNA sequencing stuff, and basically using biology as another path of evolution. Right.

**Eli Hughes:** Yeah. Yeah. That's super cool.

**Chris Gammell:** And if you get far enough into the Elon Musk style thinking of, all right, if we are, and this is where I get into the Star Trek future, but I, I like to think that it's closer than we think is, is imagine a mission to Mars. You can't really take a cow with you, but if you had a way to take some raw ingredients like yeast and whatnot, and you can ferment what you need while along the way, instead of eating your astronaut ice cream and your freeze dry. Come on, man.

**Eli Hughes:** You gotta have that though. You'd have at least a little astronaut ice cream, right?

**Chris Gammell:** Exactly. Um, but, but you think about it, you have these self-replicating creatures that it's more than just consuming the thing and you're done. It keeps going, right? You, you, you, and even in the beer brewing, like the people who make the yeast, they make the yeast almost in the same way. They grow the yeast in a tank and it's the self-replicating thing. That's cool.

**Eli Hughes:** And so are you thinking that, that eventually this, I mean, from a commercial perspective is the interest as well, like that synbiobeta might, or the folks there might have other kinds of target markets for, for sensing and stuff like that. And in the, in the purely practical sense.

**Chris Gammell:** Yeah. So where, where we were going, so there's the, there's a research side of it. They'll buy sensors for research to like do precision in the, in the word they use in there is called precision fermentation to really look at it. We, we feel we have a tool that can allow them to dig in at that level, but also in the production tool, you have all these PhDs getting out of biology school and they kind of put together the lab. They made like a leader of this, like this protoplasmic goo that's going to change the world. Now you got to scale up to making billions of leaders to change. Right. Yeah.

**Eli Hughes:** You got to hire a bunch of process engineers and a foreman on the shop floor.

**Chris Gammell:** Imagine farms. You can now produce food in localized settings. You have these bio farms that live like in some old abandoned building or some even fancy building, but it's not subject to, you know, what's going on outside with the weather. It can be certainly better controlled in terms of what stuff go in the, you know, um, and, and even when you think about the amount of land we need to produce these proteins. Sure.

**Eli Hughes:** Yeah. Yeah. Yeah. You think about the, the climate change aspect as well, like cow burps and things like that. It's, it really could have a huge effect.

**Chris Gammell:** Oh yeah. Ignoring all the, you know, the political side of it. When you just look at the science of like, how can we produce food and stuff for humanity in a way that, you know, we, we don't need billions of acres to, you know, maybe we can, can we reduce that in half? I don't know.

**Eli Hughes:** Yeah. It cuts out on transport too. Like you mentioned, I think that's another big one, right? Just energy costs are lower and probably cheaper food, maybe better food.

**Chris Gammell:** Yeah. And so I grew up in a rural, really rural area of Pennsylvania. And the argument was, everyone's like, well, we don't need these city folk. We got our cows here, our chickens, our eggs. Well, there was something to be said is like, I grew up in a place where we would eat over the campfire. We could literally go to the, you know, the guy up the road who has the cow. We would buy the cow. We would have, it's a locally sourced thing where you're not quite as worried about like what's happening. The fact that they have to ship something from like another country to get here. Like, I think the localized, you know, food system, you know, has some advantages.

**Eli Hughes:** Yeah. And I think that's a supply, like that's just as, you know, there's an analogy in, in, you know, electronics too, of just like, you know, people understand supply chain pain. And yeah, when you have a hiccup in that, you start to start to miss out on things.

**Chris Gammell:** Everyone loves just in time until you realize that kind of blows up. And then even with COVID, you looked at just how disrupting, even for a couple of weeks when everyone's trying to figure out what the heck's going on and China was kind of crazy. Just those couple of weeks, the impacts are still there. I mean, I mean, having a local buffer is not necessarily a bad thing. Yeah. I agree.

**Eli Hughes:** I agree. That's great. That's great. I, I always talk about it too. Like, so I've been vegetarian for about two years now and like, so I've tried all of the fake meats that are out there and, you know, cause I grew up like that too. And I, impossible burgers. Okay. And whatever. I'm just kind of curious about it too. But what I really think about is like, at a certain point, if you get a super tight process, right? Say, say, you know, there's vat grown meat or whatever, whatever ends up being called, but you get like this super dialed in process. It's not like, you know, a Kobe burger is, you know, 50 bucks because it's getting shipped from Japan and it's, you know, a special cow and all these others. It's like literally like, it's just a dialed in process now and everything tastes that good. And I've like, if that alone isn't like a argument for it, I don't, I don't know what it is. You know, like it's just always going to, everything is the best cut of beef then.

**Chris Gammell:** You know, it's just the other thing when I talk about like IOT and like, you know, cellular and all this, I always use the now, like the story of like the Oreo factory, the Oreo factory is a dialed in process. Like stuff goes in, you get Oreos out. Now, is that the most healthy thing for you? No. But when the Oreo machine goes down, holy cow, like there's a reason why I think like my wife loves all the different flavors. I'm like, no, they've dialed in the Oreo. Like it doesn't need to change. Same with like Kobe beef. Like you figure that out.

**Eli Hughes:** Right. And it's replicable. And then you could start to cost optimize it too. And then kind of everybody wins in that case.

**Chris Gammell:** I think, you know, it's kind of like why I can buy this.

**Eli Hughes:** And then you get the hipsters who are like, I only eat original cow, you know?

**Chris Gammell:** Yeah. Well, so I play guitar and it's, it's the same thing. I only play tube amps where the tubes had to be pulled from like this Russian thing from

**Eli Hughes:** the fifties or new old stock. Yeah, exactly.

**Chris Gammell:** Or vintage. The thing is in it. Musicians friends still has vintage batteries. Not sure what that means yet, but it's a thing.

**Eli Hughes:** Pre-leaked. Pre-leaked. Exactly. So, okay. Before we go, we're, we're, wow. We, we raced right through that hour there. Before we go, I am curious about your, so you mentioned NXP a little bit. Yeah. So you, you work on NXP stuff and you've got some, so I think some of the boards that you have shown photos of and stuff inside the, the, the, the brew thing as well have some NXP things, but can you tell us about what's going on with the NXP stuff?

**Chris Gammell:** Yeah. So I actually maintain a relationship with NXP that it, it's kind of, boy, I wish it was a, I could explain a linear path, but it actually started back in like 2010 where I, I, when I was at Penn state applied research lab. So it was a Navy lab, but a lot of people there had ties in university. We taught classes in the department. There's a lot of, you know, cross pollination, but a colleague of mine really knew some guys in the free, at the time, free scale university programs when it was free scale semiconductor. And actually that was motor role at the time. Free scale came in. Yeah. I can't remember what year that was like 2008 or something.

**Eli Hughes:** Yeah. I think, I think that was actually because I, it was when I was at Keithley, I think, because everybody was all up in arms like, Oh, I can't believe they changed the names.

**Chris Gammell:** Yeah. And I, and I learned on Motorola, like HC 11. So I had a long history in like Motorola stuff. And so there was free scale. We used a ton of free scale parts. I got introduced to the university programs. They said, Hey, we're doing this free scale cup. It's this competition, autonomous car competition. You want to get some students involved? I'm like, yeah, this is awesome. I met these guys. They said, Hey, you want to produce some, some videos for the free scale cup. They don't have to be really complicated, but little short 15 minute condom academy. Like what's a servo. How do I set up this, the tool chain for this board? Because no one can figure it out. It's really hard. How do you get code word to compile something? How do you like read the camera?

**Eli Hughes:** That, that is actually still unsolved folks.

**Chris Gammell:** Yeah, it is. Like, and I told them that like, um, in a turn of new clips. And then they, then it, then you've all saying, Hey, we'll throw you a little money. You want to put together some like maker projects, but maybe for kids who, and I say kids, like seniors in college who've learned some stuff, but they haven't learned anything. And they have some skills and maybe had some courses and some things that they're, they're, they're above starting out, but they're certainly not ready for the real world. I said, sure. You know, and, and at the time I was really into a lot of things, free scale simultaneously to that. I'd actually been using Phillips, like, or I'm sorry, NXP stuff. Um, they used to be Phillips because they had some really in the LPC family, um, a little bit of everything.

**Eli Hughes:** Oh yeah. Yeah. LPCs are great. Yeah.

**Chris Gammell:** You know? So, and that's primarily like for, for what I do day to day is where I start. So, so the, the companies merged, which, which was awesome for me because I was using parts on both sides. And then I, I kind of discovered just, uh, talking on internal, the company, the guys in the university programs kind of moved on. And I, I found this division called pro support and pro support model was on the free scale side where it was its own little kind of, um, you know, group of people, some old FAEs, some just people they found that were really good with parts and said, I bet we can build a business around sometimes cost companies need experts kind of in the company. They don't want to go through normal support. They want to pay a little bit of money to be like, not the support person, the generic answering generic form requests, but it's like they're on their team. And by the way, we only want them for like 50, a hundred or 200 hours and we want to be done. Yeah.

**Eli Hughes:** Yeah. And so it's great. It's like paratroopers. It's like, uh, you're mercenaries. You guys are like, uh, internal mercenaries.

**Chris Gammell:** So the pro support group is, uh, pretty cool because everyone has like their, their things. Some are really, some people are experts that say, I don't know, next the, the really high dot, like high end Linux processors. There's like, I'm on the microcontroller side. I do some of the, the item X RT, the crossover, and they just match up. People basically say they, they, they find out about the, the, the program. They may be already using the part. Unfortunately, it's usually like a pants on fire type situation.

**Eli Hughes:** Oh yeah.

**Chris Gammell:** Right. Right. Sometimes we get it early where we can be part of the design reviews, which is great. There's some commercial products. Some I can talk about some. I can't that came out of that. And it was just for them, all their engineers are tied up. They just want to say, Hey, we need someone who knows this fricking part. They know how to put it on a circuit board. They know how to bring it up and you know, we'll pay for a hundred or 200 hours. Right. You know, for that.

**Eli Hughes:** And plus you're, you're paying for like a hundred or 200 of like known hours. It's like, you know, the equivalent I'm sure is, you know, hiring some goofball like me is probably like 500, 600 hours. Just cause it's like, I have to go and learn the platform first. I have to go learn all of the, I have to go read all of Eli's posts on the forum to like figure out all of the nuance that's there, you know?

**Chris Gammell:** Yeah. So, so the great part about that is I'm in a position where I can work with these customers, really help them. I'm an applications guy. So I get to, you know, talk, you know, there's some things that I've done dealt with acoustics or vision or things that I, I kind of had interest in. It's more than just, Hey, this register does this it's application level. At the same time I can use internal resources, like actually go to the people in China. There was one time I had them rerun a Verilog simulation of a peripheral to verify that, Hey, this DMA trigger actually didn't work.

**Eli Hughes:** Oh, wow.

**Chris Gammell:** That's, that's, that's pretty cool. It was really painful, but I boiled it down to, okay, here's the problem. Here's the code. And I finally got the guy. There was one person who had the test vector who could rerun his Verilog. He said, Oh my, yep. You can't do that here. He says, verified it. That'll be fixed in future silicon. So, but we can relay that. And sometimes when you go just through say a support forum, whether it's NXP or ST or TI, you're not getting that level of, you know, back and forth that in, in the pro support people aren't the way we approach it is we're like, you know, we want to be a part of your team. Talk to us like you're part of our team. Not like we're just someone on the other end of a, you know, a chat window.

**Eli Hughes:** Yeah, that's great. That's just, that sounds like really cool. I'm sure I'm going to ask for someone that's listening right now. Are they, are they hiring?

**Chris Gammell:** So, well, what I was going to say is so, so for me, I was really involved. Okay. So with T zero, obviously like there's only so many hours in the day. I maintain the relationship and still do work mostly because it allows me to really interact with cool projects. I get to see kind of what's going on the pipeline. What it's grown into is now is on the, in the LPC kind of marketing department. I've been kind of writing blogs and articles about some of the new stuff that just came out, not in a, like a generic, like really plain app note way, but Hey, here's this cool part. Here's some neat things. Here's some things I've done with it. Maybe here's some things that are not good, say a little bit of everything, but, and I'll build a little board around it or something.

**Eli Hughes:** Oh, that's cool. That's cool. And so we can, yeah, we'll link all that stuff into, uh, cause I mean, that kind of thing is having that expert voice there of like what's actually happening. Like that is so much more valuable as an engineer reading that instead of just like a marketing person saying, and here's the specs again, you could have read the first page of the data sheet, but I will also state them in a blog post.

**Chris Gammell:** Yeah. So for example, this particular chip that I've been writing a lot about this LPC 55 S69 has like, it's, it's really, really low active power has all these neat things in it. It's dual core. It's really inexpensive, but it has this little DSP engine and Mark and will say, well, it does these things. Well, it makes this assumption that, you know, okay, you might've heard of FFT in school, but you might really not know how to use it. And so I wrote some articles of like, all right, here's where it actually comes from. It's just numbers in numbers out. And here's how you set up a little code and here's something useful you can do with it. And, and I found out you don't have to teach to every little nuance and detail, but sometimes just opening the door enough that says, oh, here's some neat things. Then someone who's creative will say, oh, I get it. Okay. Here's what I can do with it.

**Eli Hughes:** Yeah. Yeah. Seeding, seeding, uh, like an idea I feel like is people will take that thing and run with it. Like you said.

**Chris Gammell:** Oh, so, and I do it because I just have a really good time and I do it because I like to learn and I learn a lot just by doing the thing. I don't always do it right. I make mistakes like everyone else and I admit my stakes and I make them and try to seek out those people to help me and, um, um, do the best I can.

**Eli Hughes:** No, that's awesome. That's awesome. Eli, where can people find out more about you, your company, uh, the NXP thing? Uh, where, where are you, where are you at online?

**Chris Gammell:** So, so you can find me. So, so Twitter. So I'm trying to think of like, what's the funnel that, so T zero brew, T Z E R O brew.com is kind of like the commercial product.

**Eli Hughes:** And so that's all the, all the aspiring brewers out there that want to buy this thing. They can go.

**Eli Hughes:** The brewers.

**Chris Gammell:** And it's, we're gonna have links to like the, you know, uh, you know, the biology, synthetic biology and glycol that's out there. You can find me on LinkedIn just under Eli Hughes. I'm this big guy with a beard and you'll probably see all kinds of PCB pictures of, I like to put artwork, especially like, like Nintendo characters on boards or a EMH two or three on Twitter. It'll be pretty recognizable if you, you know, search and find me. And feel free to reach out. And I just like talking to people and hearing what they're working on and go from there. And if, uh, also next week, uh, just to get some more, if you want some more background in some of the actual technology and the brew, we're going to be talking about it like Altium live, as well as kind of the background of where I came from with 6502 and NES. And, um, we'll just have a fun pseudo engineering talk.

**Eli Hughes:** That's great. That's great. We'll have links for all that stuff in the show notes. Well, thanks so much, Eli. I really appreciate it. And, uh, yeah, I hope the, I think you're going to have a lot of, man, you have a lot of, uh, a lot of brewer friends. I'm sure, I'm sure people are very jealous about that.

**Chris Gammell:** So, well, like anything, it's like, uh, I remember the first time I met someone who got a job in the music store selling guitars. They said, I thought I was going to be able to play guitars all day. I actually have to do work. That's right. That's right.

**Eli Hughes:** You know, it's about to hear other people play their guitars.

**Chris Gammell:** Yeah, exactly.

**Eli Hughes:** No stairway.

**Chris Gammell:** But, but, but yeah, so, um, no, it's, it's just a, it's a good time and I, and I like technology and I'm learning a lot about, you know, sales and marketing as well. And, uh, and Zephyr. So I hope you, I hope. Oh, I'm going to, oh, I'm going to be blowing up your DMs. Don't worry about that. So no, I, I do think it like, like anything, it's a tool. And if you try to remove prejudices of, you know, for tools and, and, and, and learn that Linux and windows aren't necessarily enemies anymore, that they can kind of all work together and we can be a happy family.

**Eli Hughes:** Okay. Great.

**Chris Gammell:** Well, thanks again.

**Eli Hughes:** I appreciate it.

**Chris Gammell:** Thank you, Chris.

**Eli Hughes:** This episode was produced by Analog Life LLC and brought to you today by our patrons. Join at patreon.com slash the Amp Hour to get access to a private discord channel and discounts on Amp Hour swag. A special thanks today to our corporate sponsor, Vino. Makers of the Vino Nova.
