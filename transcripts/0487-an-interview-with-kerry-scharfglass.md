---
episode: 487
title: An Interview with Kerry Scharfglass
url: https://theamphour.com/487-an-interview-with-kerry-scharfglass/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released April 5th, 2020. Episode 487. Sponsored by Screaming Circus. An interview with Carrie Sharpglass. Welcome to The Amp Hour. I'm Chris Gammell, Contextual Electronics.

**Carrie Sharpglass:** And I'm Carrie Sharpglass, a human on planet Earth.

**Chris Gammell:** One of the 7 billion plus or so. How are you doing, Carrie?

**Carrie Sharpglass:** Good. I'm doing okay, given the circumstances. The inside of my house looks really nice.

**Chris Gammell:** You know, I was thinking about it today. So we were recording a little bit later than, you know, you were nice to do this kind of last minute. And I was thinking, I could pretty much email anyone right now and be like, hey, are you available for The Amp Hour? And if they say no, I'm like, who are you kidding here? Come on. Yeah, that's true. Yeah, so I'm going to, I'm going to like pack the week with any reviews. You're the first of many, apparently. So it's good to talk to you. You and I know each other from meetups and badge life stuff and lots of things, I guess, right?

**Carrie Sharpglass:** Yeah, I guess so. I think you were originally the guy in the KeyCat hat who I had seen on that cool YouTube thing who had taught me KeyCat 4.

**Chris Gammell:** Yeah, great, great. Yeah. And that was as you were getting into building badges. Is that right?

**Carrie Sharpglass:** Yeah, yeah, yeah. I first tried, what was it? It wasn't Circuit Maker. It was one of the funny online ones, which was really great, except I would work on my commute and the train would go through tunnels and sometimes things would sort of disappear. And so it became clear that I needed a different solution and thus ended up in KeyCat. Right, right.

**Chris Gammell:** That'll do it. Yeah. Well, everybody finds their way to KeyCat in one way or another and trains are one of them, I guess. So that's good. Yeah, maybe it was Upverter or something? I don't know. Like the online ones were, I think it depends on what it was.

**Carrie Sharpglass:** Yeah, it was Upverter. It was generally fairly pleasant to use, except for that one caveat.

**Chris Gammell:** Well, yeah, that is the tough thing with the network connection ones. Yeah. So you've given a couple talks on badges and we'll link all those in, but what is the badge that you worked on? This is for DEF CON, right?

**Carrie Sharpglass:** Yeah. It's been, at this point, it's been a little while since I've done much meaningful badge stuff. The last one and the one that, I guess, introduced me to the most people was the third version of the Dragonfly badge. So lots of LEDs and some infrared communication and things like that.

**Chris Gammell:** Yep. Yeah, and it was pretty tight geometry. So maybe you could explain what the specs were on that thing.

**Carrie Sharpglass:** Right. I guess that description is not enormously useful if you haven't seen one, and this is a radio show. So visual aids are not very helpful.

**Chris Gammell:** Yep.

**Carrie Sharpglass:** It, let's see. So it is an object, sort of an object from a book called The Diamond Age, which now that I'm thinking about it,

**Chris Gammell:** That's on my reread list. Yeah, I got to get back to that.

**Carrie Sharpglass:** Yeah, definitely. So at one point, some of the characters go to a party and they notice at the party that people are wearing these cloisonné dragonfly pins and they're changing colors. And then in the context of the book, there's nanomachines and mind control, kind of, and all sorts of other things that go on, which parts that are harder to source from DigiKey and so we're not included in the DEF CON badge.

**Chris Gammell:** Ah, yeah, yeah.

**Carrie Sharpglass:** There are limits to their amazing selection. So the badge does kind of that. So it is covered in RGB LEDs and they beacon periodically in infrared. And so when they're alone, they just do random color fading. And when they notice that they're near each other, they sort of all, they synchronize a clock, the clock that they derive their animations from. And then the animations switch progressively from totally random to a coordinated pattern. And they all coordinate the same pattern at the same time. So if you, it's basically designed for, you know, if you're standing around in a circle talking to people and you talk for a few minutes, eventually they'll all be totally synchronized. And then when you walk away from each other, they'll kind of spin back out into random fading.

**Chris Gammell:** Yeah, that's really cool. That's really cool. And yeah, and so this was, yeah, this is your, I mean, you were doing firmware for a long time and then this was kind of your entry into hardware. Is that right? Or doing more like personalized hardware?

**Carrie Sharpglass:** I think that's accurate. In college, I had some, my degree was, I guess, about one third EE and two thirds computer science. But unfortunately, the one third EE was the boring part or rather all the fundamental stuff up until the point where it required creativity. And then that was where that segment of coursework ended and I ended up doing more computer science stuff. So I had been exposed to doing PCB design and things, but hadn't really, hadn't actually used it in the real world and the way my brain works. If I don't use it, I lose it. So it was effectively my reintroduction into all those things. There were, I guess, three, that was, the one, the one that they were, are the most of was the third version. The first one was very like, back alley is the wrong word, but. Low budget? Very rough. Yeah. Low, low yield, low volume.

**Chris Gammell:** Yeah,

**Carrie Sharpglass:** yeah, yeah.

**Chris Gammell:** Yeah. And that's what some of the, so like I said, we'll link in some of the talks you've given. You've given a Supercon talk about this. You've given a HDDG talk about it, I believe. And I think that some of that stuff was kind of like, that was kind of like good, small scale manufacturing type of discussion. You know, I think a lot of people, myself included, I got, for a while I was tuning stuff out with like Badge Life. I was like, ah, what is, you know, like, what is this stuff? And I think it was actually your talk and Whitney who was also giving a talk at that same HDDG. It's like, oh, okay, this is working on hardware for fun, right? This is just working on art projects that are, happen to be electronics and it's for fun and there's actual real world challenges and all those kind of things.

**Carrie Sharpglass:** Yeah. And that was what I, I guess I did it the first time because I had gone to DEF CON for a long time and with my group of friends, we talked about, I think since the first year, boy, how cool would it be to build one of these things and eventually kind of decided, well, we could actually, there's like nothing, preventing us from doing that besides actually doing it. It's just like money

**Chris Gammell:** and time and programming, you know?

**Carrie Sharpglass:** Right. Yeah, it's easy. There's infinite amounts of those so that's not a problem. You just turn the crank and there it is.

**Chris Gammell:** Yeah, perfect. Right, right. What are we even talking about here? It's like electronics, just snap your fingers, it's done, you know?

**Carrie Sharpglass:** Right, yeah, done. I'm imagining the Easy EDA logo or the, shoot, not Easy EDA. Oh, that's embarrassing.

**Chris Gammell:** Snap EDA probably.

**Carrie Sharpglass:** Yep, it was Snap EDA. Wow.

**Chris Gammell:** It's in the name. It's in the name. Yep.

**Carrie Sharpglass:** It's in the name. Hello, Natasha. Yeah. Right, right. So the first version was super rough. The second version I built about a hundred of and the first one introduced me to a bunch of people, the second one introduced me to a bunch more people and then I sort of started looking at it as a way to practice small-scale manufacturing, cottage hardware type stuff. At the time, I was working at an engineering consulting company full-time and so I had sort of sequential exposure to a bunch of startups and large companies and all sorts of organizations building hardware. So I had fought in that sort of professional context about the business realities of building hardware and how you deal with factories and things like that, though I'm primarily a firmware engineer. So this was an interesting and relatively lower stakes way for me to kind of play with what it would take to actually build. I certainly don't want to overstate my level of expertise here. So we'll say build a product, build a hardware product lightly, I guess.

**Chris Gammell:** Yeah, yeah, yeah, yeah. That's cool. I mean, like, I think, so I was just part of a conversation that I linked on the subreddit about yesterday and we were talking with former guests, Zach from Bantam Tools and Nadia Peek and another guy, Ben, and Nadia brought up this thing called, it was like a, it's a workshop they do I think was part of MIT when she was there and, but it sounded like it was like war games for manufacturing and it sounds like you're kind of talking about that same thing for like small scale manufacturing. This is the thing we were talking about was kind of like war games for like large scale manufacturing, like how do you actually, it was like you could only talk to, it was such a crazy idea, you could only talk to the different groups that you had, right? So like one, you have a group of 30 people, 10 people are design, 10 people are manufacturing, 10 people are logistics. You could only have one half hour meeting a day or something like that and you had three days to like get everything done and like it just blew my mind of like, oh wow, like that could be something that you would at least empathize with the process or in a best case scenario you actually like optimize, you're like, oh, maybe I shouldn't write an email that's three pages long to try and do this thing. I should do better documentation on, you know, like all of these other things that like anyone who's been doing hardware and manufacturing and all the things that are shitty about the process, you know, like, but like trying to actually practice that up front so that you kind of optimize your real world processes around it, you know? So it sounds like you were doing that same kind of thing. You were, you're basically a wargaming small scale hardware manufacturing.

**Carrie Sharpglass:** Yeah, I guess so. Boy, that sounds really fun actually and very, very shelter in place friendly to organize a remote distributed hardware manufacturing wargames.

**Chris Gammell:** Yeah, yeah, yeah. And it's, yeah. I mean, so what did you learn from it? I guess what is, you know, I say wargames, but at the end of the day you did it anyway. So it was, it was a real thing, you know, it's not like it was for all for naught. It was like you actually were making and selling these things. So what did you learn from that?

**Carrie Sharpglass:** That's, let me see if I can, how much, how many of my bullet points I can reload into my brain. I guess, I feel like the most useful things were meta things because it's not.

**Chris Gammell:** Yeah, that's what's surprising though usually too, right? I mean, it's like, oh, I didn't think that was going to be a problem, you know?

**Carrie Sharpglass:** I guess that's, I guess that's true. So, so maybe foolish things like, I guess, foolish, not foolish, over communicating with your vendors, communicating as clearly as possible in a way that survives, you know, one email exchange a day. So photos and big red arrows and boxes and diagrams describing the orientation of the component because they don't seem to get it and you want to make sure they really get it with this email.

**Chris Gammell:** And did they?

**Carrie Sharpglass:** They did. That was, that ended up being the answer was, was like verbal descriptions that are getting translated both ways don't work super well, but photos of actual units with things in the actual orientation and big colorful illustrations are very helpful and without language barrier.

**Chris Gammell:** Yep. Yeah, exactly. Exactly. There's, yeah, there's a mark on a diode is pretty, when you take a photo of it, it's here and here. It's very clear. Make sure this lines up with that, right? Right.

**Carrie Sharpglass:** Yeah, right. Yeah. I definitely didn't, wasn't dealing with any, anything anywhere near the volumes or complexity where I was worried about optimizing for like acid traps in my PCB design and stuff like that. That, like that, that, that didn't have any kind of real, real reliability stuff that I was thinking about because my volumes were all in the hundreds or lower.

**Chris Gammell:** I think, well, some of that actually points to the, the economics of it though too, right? So you have to make sure you're pricing yourself properly and that's, I think, something that a lot of people who are doing small scale hardware, they don't think about until later, then they're like, oh, maybe 20% margin at the offset was a bad idea after I had 80% yield, you know, or something like that. It's like economics or a thing, you know? Right.

**Carrie Sharpglass:** Yeah, I think that was another lesson is all the different things that you use profit for. So I guess it's probably important to say that it's, everyone does, does things like this for different reasons and it's important to identify, I found that it's important to identify the reasons why you're doing the thing and then optimize for those reasons. So I was doing it as a learning experience about building hardware in a way that I was guessing would be economically sustainable. So I was interested in figuring out how to optimize the cost of the unit so it generated enough profit to cover different sorts of risks in case my yield was really low or I couldn't get a component and I had to, I ended up like risk buying something I couldn't use or let's see, I guess yield, lots of different ways of phrasing yield.

**Chris Gammell:** Right, right. This part broke, this part broke, this part broke. Right, yeah. Scrap this, scrap that. Yeah, yeah, yeah, it's true. And I think at the end of the day, the other thing that I think a lot of people don't actually put into the calculation, like, you know, I was adjacent to the badge life thing I tried making my own and it didn't work out, but like the people that were adjacent to it, they're like, oh, wow, you made 50, $50,000 for this thing. Some people were like, yeah, but I spent 500 hours on that, you know, or I spent a thousand hours on that, or, you know, it's like, there was five people on my team, so we got what, like $10 an hour, you know, it's like, okay, yeah, maybe isn't, you know, the thing that you want to base your livelihood on, but yes, there was money, yes, there was money. That's kind of like, that's the end thing. It's like, yes, there was money, some people make some money, but a lot more spend money, spend their time and don't make much money from it.

**Carrie Sharpglass:** Right, right. And I mean, again, I think it depends a lot on what your goal is. If your goal is to produce really wonderful art pieces that don't, and you're not interested in building it as a sustainable business, you're interested, I mean, everyone is interested in, you know, low financial risk, I guess, so I don't mean to understate that too much, then you're probably not as interested in making sure that you hammer a few more quarters out of your bomb cost because you're trying to increase the profit margin, you're probably more interested in producing maybe something that's more polished or has more features or, you know, who knows, depending on what you want to do.

**Chris Gammell:** Yeah, and it seems like a lot of people are learning from it too, and that's why, I mean, my small experiment with it too is basically, I think it's this great opportunity to, you know, push yourself, it's a reason to learn things, you know, I think that's always, especially, you know, okay, we're in a time of quarantine, you know, if you're sitting inside right now and you're like, I could learn anything, but why should I? It's like, man, if you have a project though, like the people that are working towards ventilators or whatever they're, you know, working on, there's a lot more learning happening when you have that end goal and you had that, so that's great.

**Carrie Sharpglass:** Yeah, definitely. End goals and hard constraints because you can't, you cannot change when DEF CON starts or whatever the event is, you must, whatever you're ready with at that time is what you get, so prepare.

**Chris Gammell:** Yeah. So, other things you learned before we move on from this? I mean, what else did you, like on the hardware side, did you learn anything particular or I guess even pushing back into the firmware side, which is your expertise, did you learn anything surprising there?

**Carrie Sharpglass:** I keep meaning to write this up in some context and I haven't done it yet, but the product, basically the product, the badges feature effectively was RGB LEDs, so that, almost all of the design effort and software effort went into supporting that in one way or another. It turns out the infrared time synchronization stuff, you can make it really complicated, but that is the path towards failure. It turns out the way to do it is actually really dead simple, so kind of the thing that's left is all the LED things. So, I ended up, I'm trying to remember the numbers, 48. 48,

**Chris Gammell:** so, 48, but I guess times three, right, because they're tricolor, right, they're multiple. Right,

**Carrie Sharpglass:** so I ended up deciding I was very wary of the problems that I've had and that other people have had soldering the various controller integrated LEDs, so I ended up choosing to go with the totally dumb, separate, controller-free RGB LEDs. So, 48, three channels each, yeah. So, the whole unit ended up being maybe like a five centimeter square, give or take, and the LEDs were kind of arranged on the top in a particular pattern. So, as I was routing, I started with a four-layer board and I got, I think, maybe 10 something hours into routing it and I eventually kind of just hit a wall and it was not possible for me to go, it was, I rapidly tailed off in my progress per minute of time routing. So, I ended up,

**Chris Gammell:** it's good to figure that out sooner than later though too, right? I mean, like that's better than being like getting into like where you think you're 90% of the way and then you're like, oh, never mind. That's definitely true. Because you're not utilizing the whole, the layer five and six as much.

**Carrie Sharpglass:** Yeah, so I, so I did end up bumping it to six layers because someone suggested that and I thought that was a ridiculous suggestion and it was going to be too much money and then I checked and it turns out it's actually really not that much more money. So, yeah, so yeah, bumped it, bumped to six layers, ended up using, I think I did use some of maybe both of those to write on. So I eventually ended up re, I sort of progressively reconnected the LEDs to the controller again and again until I got to a layout that would solve, which left me with a very strange physical mapping, I guess, instead of a simple physical mapping and a simple logical mapping. So there ended up being a couple layers of mapping in software to map it to the right physical layout to make it so that the LEDs were sane to address, which was, I think, the right choice but in hindsight, if I were to go back and route the board now, I think there are some, I think, I think there is maybe more strategy that could have happened up front that would have let me squeeze it down into four layers or would have let me map it in a more, a more reasonable way requiring less kind of crazy rearranging in software for the six layers. But I mean, it worked out fine.

**Chris Gammell:** What actually was the, so you said it wasn't a driver circuit, but was it just like Charlie plexing or what was the actual method of, you didn't have 144 pins, did you?

**Carrie Sharpglass:** I did not. So I ended up using, ISSI makes like RAM and LED controllers and their LED controllers are really, really dumb and really inexpensive for the number of pins you get. And I really like them. There are some really incredible TI LED controllers that you can write assembly into them and like they have GPIOs and they are fully functional controllers, but those are, those can be very complicated and quite a pain in the butt to deal with. So I, I much prefer keeping the smarts in the, in the micro controller. So I ended up using a 36 channel driver, which was quite dumb. And then dividing the LEDs into four banks, which ended up sort of being distributed north, south, east, west on the board. So let's see. So there was a PFET on the high side and then, yeah, because it was a low side driver. So there was a PFET on top and then the LED and then the LED controller on the bottom. So the strategy ended up being the sort of predictable, like enable a bank, disable the other banks, write to the controller, wait a moment, disable the bank, enable the next bank, rewrite to the controller, sort of cycling.

**Chris Gammell:** Yeah, like round robin kind of idea. And it's just so fast that you eyeball don't see it kind of thing.

**Carrie Sharpglass:** Yeah, yeah, I was, that took a few iterations to get to the point where it was as smooth as I wanted it. And it did end up, I was worried the controller spoke I squared C and so I was, I was kind of worried that I ended up even needing a full megabit. I think I was running it at maybe 400 kilohertz. I was worried that I wasn't going to be able to get buttery smooth fades, which is my only goal in life. But a couple, a couple rounds of optimization and DMA, I think, eventually got me there.

**Chris Gammell:** Yeah, that's good. That's good. Yeah, and I mean, at that point, you're basically in your wheelhouse and you're doing your firmware stuff. Right, right. It's like bringing work home with you, I guess.

**Carrie Sharpglass:** Yeah, that, I have certainly more recently tended towards projects which don't overlap as much with work things, just to kind of let the brain change shape a little bit.

**Chris Gammell:** Yeah, that's smart. That's smart. Well, let's talk a little bit about work. So, you are doing a lot of firmware stuff, but it's all pretty low-level hardware, it seems like. So, maybe we can go back to bumping out of school and starting into work. What did that look like?

**Carrie Sharpglass:** Yeah, so, I worked at Amazon Lab 126 first out of school, which is the chunk of the company. I guess it's now kind of all amalgamated into one, but at the time it was the chunk of the company that did the Kindle and they, I guess it was just the Kindle and the Kindle fire at that point. I worked on a funny research project and then the thing that eventually became the Echo, which was, in hindsight, very neat. At the time, I did not, at the time it was a weird thing that sat on the desk and didn't work super well, so it was not very engaging. But in hindsight, I guess that turned out to be a pretty easy idea. Yeah, those things

**Chris Gammell:** are frigging everywhere now.

**Speaker ?:** So,

**Chris Gammell:** yeah. I saw recently they made it into a ring, too?

**Carrie Sharpglass:** Yeah. Have you seen starting some more exploratory stuff, it looks like. So, there's a ring, there are glasses, there's, they finally, so part of the original product vision was sort of a wall wart that would be basically disposably inexpensive that you just throw in all the outlets and all the different parts of your house and then you'd have an ambient computer Star Trek style and they do finally have that now after years of iteration. The Echo, shoot, what's it called? The plug one. There's an ugly little wall wart plug one,

**Chris Gammell:** which is like

**Carrie Sharpglass:** 20 bucks. Yeah, it meets that original design goal. I've never seen one in person, but they do exist.

**Chris Gammell:** Well, I think one of the things is they started pushing it down into chips that they could also sell to other companies outside of Amazon, which is an interesting thing. So, it's got the listening engine and whatever, the machine language learning that does the Alexa stuff. Yeah,

**Carrie Sharpglass:** the original Echo was, well, it took quite a while to ship. So, it was an OMAP-3, it was a weird skew of the OMAP-3 with a funny DSP core attached. I don't really have very many memories of the performance thresholds that it was hitting, but at the time, doing all the beamforming and stuff in real time was like a tall order. Nowadays, that is certainly not the case.

**Chris Gammell:** Yeah, well, and it's propagated to lots of different, it's not just Amazon doing it anymore either, it's, damn, it's everything wants to listen to you. Yeah, that maybe has

**Carrie Sharpglass:** other implications which were perhaps not as clearly foreseen at the time.

**Chris Gammell:** Yeah, I mean, right, exactly. It's like a technological thing that you like, I mean, beamforming itself is cool as hell, right? It's in audio, it's in RF, and it's in, you know, it's obviously like constructive, destructive interference, like it's a cool phenomenon, but, you know, maybe people are less interested in having their stuff listened to all the time. How do you feel about it? I mean, I guess you're, you know, you're someone who worked on early versions of it. Do you have lots of listening devices in your house?

**Carrie Sharpglass:** That's a good question. I have pretty mixed feelings. I guess I'm fairly comfortable having Echoes in my house, like at the time, so it, I think they all still have a microphone mute button on them, so at the time, I like looked at the electrical schematics and confirmed that the microphone mute button, like grounded the microphone inputs or disconnected the microphone or something. Actually, I think originally they were planning on having the button be transparent, so you could, like you could see the like mechanical mechanism disengaging, now that obviously wouldn't really have been terribly meaningful and they didn't

**Chris Gammell:** end up doing that. Right, right, grandma doesn't care about that, so. Right,

**Carrie Sharpglass:** yeah, so I guess as a holdover, I still feel comfortable having Echoes in my house and I carry a phone with me like most people do, and the Thorin includes a variety of processors, including processors that run software that can't be inspected, that you don't know anything about, that has DMA access to the rest of the system, so there's kind of a lot of trust implicitly that the sensors on your phone are doing exactly what you think they're doing.

**Chris Gammell:** Right, right, and I think the other thing too is like from a, you know, from an ethics point of view too, it's like even in the best case scenario, like I agree to, I don't know, like Google Maps, right, and then the one that really freaked me out was like, oh, you know, there's like a pop-up that says, oh, check out your history, and I'm like, okay, you know, it was like part of like the data thing, and it like literally showed me getting on the train every day and going to work and then coming back, oh, that day, you know, you like cycle back through and it's like, oh yeah, like this thing, like everything tracks everything, of course it does, right, there's no surprises here, I sound, you know, stupid, but like, but when you see it, it's like, oh, okay, that's a nice little reminder, yeah,

**Carrie Sharpglass:** right, it's very different being intellectually aware that it's happening and then looking at your location history for the last two years and going,

**Chris Gammell:** oh yeah,

**Carrie Sharpglass:** you know, Tuesday in September 2017, I was in fact at that coffee shop.

**Chris Gammell:** That's right, that's right, yeah, and I think, you know, and I guess, again, to bring it back to current events, right, that is how China and South Korea are tracking COVID cases, right, it's like that is something that's in all of our phones anyways, and it can be used for, you know, positive outcomes, but, you know, also negative.

**Carrie Sharpglass:** I think Google actually released a page this week that tracks community mobility, yeah, google.com slash COVID-19 slash mobility, which I think generates that, basically aggregates that data and shows you information about how much people are moving around you. Let's see, I haven't actually looked at okay, there is one for California. I have not looked at this data. Interesting. How familiar are people at transit stations or workplaces or residential? Yeah. By county, very interesting. Yeah, it's, they collect this information, I guess. It kind of makes you wonder, is this, is this like people who have location history turned on and they're anonymizing it? is this information, location information that's collected via some other means? Let's see, a couple weeks ago there was a company that published a similar sort of report about mobility. I think they were rating different regions on how well they'd done sheltering in place. But they, unlike Google, everyone is aware that Google collects this sort of, well, many people are aware that Google collect this sort of information and many people have experienced prompts on their phone asking them, having Google ask them about sharing their location information.

**Chris Gammell:** Right.

**Carrie Sharpglass:** This company is one of the companies that buys that information in bulk from carriers or other sources and then uses it for analyzing like sporting events and marketing performance and stuff like that. So it was a little distressing to see some random company you've never heard of with all this information, but it gets out there, you just don't think about it most of the time.

**Chris Gammell:** Right, right. And it, I mean, it feels in that case most of the time. I mean, it is pretty much like, yeah, okay, I go to CVS, who cares? But then also, okay, you know, so, yeah, it feels fun. So you helped enable this. That's cool.

**Carrie Sharpglass:** Yeah, it feels great. Yeah.

**Chris Gammell:** Surveillance state. Yeah. Well, you know, an opt-in sort of surveillance state. I mean, here's the thing. I love telling a music thing to play jazz. And if I could just tell it to do that and not do anything else, that'd be great, you know? So.

**Carrie Sharpglass:** And there are, you know, open source or offline versions of speech recognition engines and things that do some of that. It just turns out that the way that it works best.

**Speaker ?:** They're just not

**Carrie Sharpglass:** $20.

**Chris Gammell:** You know, they're not built into things.

**Carrie Sharpglass:** Right. They're not $20. They're not built into your stove or your microwave there. Yeah. Yeah. For better or for worse.

**Chris Gammell:** Yeah. Well, what is the, so did you work on the OMAP when you were there? Is that the, some of the kind of things you worked on?

**Carrie Sharpglass:** Yeah, I did, I guess like Linux system software-y things. I don't, I, amazingly, so I still have the device that I got at the time when they were first launched and it still has feature parity. So there's some, some unfortunate team of people stuck in a corner working on our weird open embedded OS build supporting that strange old processor.

**Chris Gammell:** They're pushing updates to your stuff still?

**Carrie Sharpglass:** I,

**Chris Gammell:** that's amazing. If so, I mean like that's, that's wow.

**Carrie Sharpglass:** It had, it definitely has the same features as more as far as, well, accepting, accepting hardware things like sensors that don't exist. I believe it still has the same set of software features that a more recent Echo does. I'm not 100% sure, but it definitely did get things like Spotify playback and stuff like that.

**Chris Gammell:** Right, right. I always kind of figured that like on the hardware, it's basically just a processing engine to push to the network. Like when I, like I have a Google Home as well and it just like sometimes, you know, both of them just kind of sit there and spin if the network's slow, right? I have like kind of crappy Wi-Fi. And so I always just figured that there's not like a ton of localized, there are some localized things of course, right? It's driving speakers, it's handling inputs, outputs, whatever, but like, like you're, it's not pushing like firmware updates to talk to Spotify, is it? Actually,

**Carrie Sharpglass:** Spotify specifically, so I think it, I think it ends up being a mixture. I can, so I guess I can speak to things that were true at the time. I have no idea if they're true now and if sure, you left five or so

**Chris Gammell:** years ago or whatever.

**Carrie Sharpglass:** Yeah, more than that. Yeah, six or seven, I think. So at the time, some, some link or some, let's see, there's natural language processing and then the actual voice recognition stuff. So some of that happened on board. So like for any of these devices, I assume you want them to respond as quickly as possible when you wake them up. So the wake word stuff presumably runs on device and probably one or two other things like the ability to tell it to stop presumably happen on device because you want that to be very low latency. Some things are sort of a mishmash. So again, I have no idea how it works now, but the original integration with things like Hue was a very strange, it didn't happen on, actually, was this the case for Hue? I think it was the case for Hue and maybe some of the Wemo smart outlet stuff.

**Chris Gammell:** Yeah, Hue is a light bulb for people that didn't know, it's a Philips light bulb.

**Carrie Sharpglass:** Sorry, yes, yeah, so there's like the Philips Hue light bulb things which were very early on the scene in terms of home IoT hardware and there were, was it Belkin makes under the Wemo brand, switches and maybe light bulbs and outlets and energy monitors and stuff. So some of those early integrations happened via, I think it was via UPnP on the local network. Oh,

**Chris Gammell:** really? You would

**Carrie Sharpglass:** ask her to discover devices and then she would basically proxy like UPnP from your local network to the back end and then back down. So you'd like tell her to turn off a light and so the wake word would run locally and then voice would stream to the back end where they would do all the recognition stuff and figure out you wanted to turn off a light and they would craft the appropriate message that needed to go out on your LAN and then send that message down to the device and the device would relay that message out to your light switch on LAN and then you'd also get like streams back the voice response to your query. It's like a funny mixture of stuff.

**Chris Gammell:** I always just figured that the light bulbs were like listening on the general network as well and like talking back to the servers. Is that not the case?

**Carrie Sharpglass:** I think it depends. I think there are in a perfect world you'd want these things to all be over your local network because you don't want control of your light bulbs to be dependent on an internet connection. Or at all. In reality things are probably not quite so clean. But more recently they've started adding Zigbee to some models and Bluetooth for some home IoT stuff. In those cases there's a local interaction between your device and sensors and actuators that are physically near it. Some things I think there was originally some funny Spotify might have happened on device just because of the way their libraries were put together or something. But for the most part I think I would make the same default assumption that you do about most things happen on the back end and get streamed down because why would you? It's preferable for speed of development and debugging and everything it's preferable to do as little edge compute as possible probably.

**Chris Gammell:** Like you were saying with libraries and stuff too. It may be less of a problem at the beginning but as the things open up you get more and more and more people in the ecosystem it's like you don't want to have to be doing hardware specific calls. You want to have these genericized inputs or these interfaces rather and yeah the web is pretty good at that kind of thing actually. Right.

**Carrie Sharpglass:** I would also assume that most of these certainly when we were doing it and processing power was a little more limited it was a custom Linux OS built on built with open embedded or eventually Yocto. I would guess though that nowadays compute is so inexpensive these things are probably all running something that looks Android-ish. I would actually Google has a weird mishmash of different operating systems. I would assume that all of Amazon stuff is running Android of some flavor though I have no particular inside knowledge to believe that that's the case. Sure.

**Chris Gammell:** I've been interested in this kind of like when you think about it from a human resources perspective that's one of the things that actually really start to get interesting. You're trying to grow an ecosystem and it's like we're going to build this thing let's say we're going to make something like building out an ecosystem of lights and all these different things and you're like no but everything has to be written in C. Everything is bare metal whatever. It's like okay that works great but how many engineers are available for that sort of thing and how smart is that? It's like you're going to just run out of engineers before even if you have these great performance improvements you don't have the same amount of engineers available as you might if you take it up a level and you start to make it available on a software level with a bunch of people that know software level things. I just feel like the numbers are way different.

**Carrie Sharpglass:** Yeah I experienced that so that I guess the next company I worked at the little engineering consulting company the last big thing I worked on was one of these dockless shareable scooters that you see around.

**Chris Gammell:** I haven't heard about those.

**Carrie Sharpglass:** Well actually if you wait another six months you might not have heard about those

**Chris Gammell:** depending on

**Carrie Sharpglass:** what the market continues doing.

**Chris Gammell:** Yeah I'm okay with that though. Scooters are the first thing to go I'm okay with it. Very sensitive to the San Francisco ecosystem which apparently is built entirely on scooters.

**Carrie Sharpglass:** It is built entirely on scooters. It's like Seattle's built on top of a city underneath. It's in San Francisco it's the city and then scooters and then I think ping pong tables from failed startups and then mud at the bottom of the bay.

**Chris Gammell:** Right right yep. Today we're again hearing from Screaming Circuits this time about how our listeners can optimize their designs for assembly. But we first wanted to give an update on their services. Screaming Circuits are remaining open during the COVID-19 shutdown to help in the fight against coronavirus. Dwayne Benson who we'll hear from here in a bit told me over email quote We've changed a lot in the factory so that we can keep our employees safe especially those that work on the production floor putting parts on your board every day. Any electronics used in diagnostics or treatment of COVID-19 are given priority. It's not an easy thing to do but people still need their electronics built. End quote. We're glad they're helping people get electronics they need especially in this time of crisis. We had previously talked to Dwayne about how our listeners can optimize designs for getting board assembly done. Here's what he said.

**Dave Jones:** Yes, keeping all the surface mount components on one side is going to be less expensive in most cases. If you have a really small board however you may be able to get the board even smaller by using the double-sided. So check with check pricing on the board with the board house as well as with us to see what combination of smaller board with parts on two sides versus larger board with parts on one side is going to be less expensive. Another thing you can do is BGAs, while they're awesome, they do cost a little bit more money to process. So if you don't have to, don't use BGAs. And with us, it's a any BGAs is the same as one BGA. Any number of BGAs is the same as one BGA. So it's kind of a yes or no decision because we used to charge per BGA because it cost us per BGA. We x-ray all of them. So there's extra inspection, but we kind of average it off and say, okay, for x-raying one or two, it costs us about the same. Some people have more, but we'll just eat that cost. The other thing is that most people or a lot of people don't realize today is if you can go 100% surface mount, that can save you a lot of money as well. Thru-hole parts are usually either, well, for most boards, they're hand inserted. So that takes extra time. A surface mount component will cost a lot less, usually to buy the component and to place the component. So surface mount all the way is a good way to save cost. Something else you can do if you've got a lot of components that are similar, you know, for example, an I2C pull-up resistor, you might have a 4K and, you know, you might have a pull-down resistor for a MOSFET switch that's 5K. If they can both use the same component, use the same component. Surface mount assembly, one of the major charges is each different component costs extra because that's an additional setup stage. So if you can combine parts, do it. Make sure, of course, it's not an engineered component where you need the exact value. That's something different. But if you need a bunch of 180-ohm resistors for LEDs and the other LED has two 20-ohm resistors, check and see if you can use the same part for both.

**Chris Gammell:** So if you need electronics made for a medical project that can help with coronavirus, be sure to mention that when you order. And check out screamingcircuits.com slash theamphour to get your next board quoted for everyday electronics. And now back to the show.

**Carrie Sharpglass:** The company we were working with...

**Chris Gammell:** This is Mindtrib, the company you were at Yes. Sorry.

**Carrie Sharpglass:** The engineering consulting company I was at is called Mindtrib, was called Mindtrib, I guess. They've been since acquired by Accenture.

**Chris Gammell:** That's right. And actually, some of the people that worked at Mindtrib now work like 100 feet away from me because Accenture is working at mHub and there are some other people are like, yeah, they bought the Mindtrib group. So unfortunately, Carrie didn't come to visit or Fred, who was also, we used to work there that I met through you. And I was expecting to like know all these people that were going to come to my office and not anymore.

**Carrie Sharpglass:** I think we were hoping that that would have been fun. The MHub space is really incredible. Much more impressive shop space than our office was. Though our office did okay given the amount of room available to it. Sure, sure. I mean, yeah. That would have been very, very fun to come in.

**Chris Gammell:** Chicago versus San Francisco real estate prices are different.

**Carrie Sharpglass:** That's a good point. Yeah.

**Chris Gammell:** Anyway, so you were saying Mindtrib and you were working for some small, you were saying they were doing a dockless scooter.

**Carrie Sharpglass:** Yeah. So one of, one of these companies that they had existed for a while, they had a large engineering organization. They had a variety of products already on the market, but they didn't have any experience doing hardware because that didn't like very orthogonal to the rest of their business. So we did end up at least for the version of it that I worked on. It's, it has since been revised at least once. We did end up using, using like a, a real microcontroller, micro controller, not, not a Linux system, but there was a lot of discussion about it. It just feels, I don't know, it feels kind of wrong. It feels wrong to put an entire, to coop up an entire Linux computer in, in the head of a little scooter where it's only ever going to need to like actuate three GPIOs and turn on a light. But there was a lot of discussion about whether or not that was appropriate because they certainly, they employed people who could write C, but they employed a very large number of extremely skilled engineers who worked on, you know, the things you find on a server backend. So languages like Python and JavaScript.

**Chris Gammell:** Yep. Yeah. And I think a big argument against it normally is batteries. But like when you look at like the comparative processing of like a, you know, micro or even like a small phone on there versus what the battery draw, there's huge batteries on scooters. So like it's actually not a bad design decision either. You know, there's no be a small percentage of the total power used. So that's not a big deal.

**Carrie Sharpglass:** Right. And you, cause it's going to have like a cell modem and stuff that's going to be on all the time. Yeah. Yeah. It's going to be on all the time and like all these other things that are going to be hogs. And the, the economics are very, very, at least at the time were very strange because they weren't, it isn't a product they were selling. They weren't trying to make a margin on each one. They basically actually at the time I certainly they wanted it to be reliable. They were, they were most, and actually to be clear and to their credit, the highest priority through everything was making sure that it was always going to be safe for the user.

**Chris Gammell:** Yeah. Right. That's good.

**Carrie Sharpglass:** Besides that, like it was, you know, hopefully we'll turn a profit, but, but there, they needed this product because it was an existential threat to them if they didn't have it. That's right. Right. almost nothing else mattered. It needed to exist and you needed it like you needed to have a battery and you need to be able to write it. But besides that, the individual branding

**Chris Gammell:** exercise, it's crazy, but yeah.

**Carrie Sharpglass:** Right. Right. Certainly spending less money is preferable, but if the answer was, well, we need to add another $50 to each unit because we're going to put a Linux computer in there, then the answer was like, okay, that's, that's fine. If you need it, that's fine. Especially if it, if it would let you get to market faster. That was like the, the name of the game was how quickly can you ship, how quickly can these things be on the streets? Yeah. And so if, if the answer was spending more money on a part, then that was fine. And they would turn the screws on the suppliers because the volume was going to be super high and see where it ended up.

**Chris Gammell:** Yep. Yep. And that's an interesting constraint. I think that you deal with more being in the Bay area than I ever see in the Midwest. You know, you're, you're, I mean, functional

**Carrie Sharpglass:** companies versus dysfunctional companies. No, actually.

**Chris Gammell:** Well, I mean, no. Uh, I wouldn't say it. I wouldn't say it. You can say that, but I wouldn't say it. Uh, I actually just meant like time to market. I mean, like that is, that was a really good point though. Right. I mean, like, yeah, you might be doing a subpar system from like a long term perspective, whatever, but like we got to get a thing out there. And I don't think I've ever worked on something that was so quick turn that it was like, you know, we have to hit market within three months or six months or whatever. Like, you know, it was just throwing, throwing money at a problem, of course, but throwing it a money at a problem that has a, a deadline that is very, very driven by market forces. So that's kind of interesting.

**Carrie Sharpglass:** Yeah. Mindtripe, the consulting company, I think per hour was fairly expensive. And so almost everything we worked on, it made the most sense to, to like turn PCBs as quick as possible and turn mechanical prototypes as quickly as possible, because that was going to be fewer of our hours and fewer, fewer hours overall. And that was more money efficient, especially because many of, many of our clients were efficient, were very interested in minimizing time to market or they needed an answer to a question quickly or something. And it aligned best with their goals to not, to not sit and spin your wheels waiting for PCBs to come back in three weeks when you could turn them in five days. Six week turn, what's

**Chris Gammell:** the problem? You're going to get a great price on these guys. Come on.

**Carrie Sharpglass:** Yeah. Yeah. Right. So I think that project ended up being four months from start to units rolling off the production line that went onto a real street that people actually rode.

**Chris Gammell:** Yeah. Yeah. That's, that's impressive. I mean, we're our mind tribe clients, mostly they were kind of like localized to the Bay area as well. So it was kind of similar kind of MOs towards design constraints and stuff like that of real fast market.

**Carrie Sharpglass:** Yeah. For the most part there, they definitely were slightly farther afield, but a large, a large fraction was, was very local to the Bay area or really to San Francisco. And I don't remember what the breakdown was, but a good chunk ended up being startups where the thing that we were working on for them was like, that was the company. It wasn't, you know.

**Chris Gammell:** Yeah. Right. We are a hardware company. We're making a big, yeah, it's, it's the all around that hardware thing though. Right. Yeah. What does that mean for you as a, as a firmware person then? So like, uh, so, you know, you were working on Linux systems on low level hardware, low level code and stuff like that. Like, does that impact you more or less than normal? Like, uh, that, that fast timeline, or I guess, were there lots of revs on the hardware side that you had to kind of keep up with?

**Carrie Sharpglass:** It was definitely really good in terms of exposing me to a large number of different technologies and ways of solving problems. At some point as a consultant dealing with the client, dealing with the client is maybe a, a strong, a strong arm way of phrasing it. Being able to interact with people. This is actually a lesson that I learned at some point. I think, I think mostly at MindTribe. It turns out if you can't communicate about the thing that you're doing, it almost doesn't matter what you're doing at all. So, uh, communication with the client and the stakeholder was extremely important. And so I, as a random engineer, all the engineers needed to be able to do things like this, but it was a useful skill to be able to walk into a room and just whiteboard off the top of your head, how you might get put together a system to do X. And so working on a variety of small or small and kind of medium products over a bunch of industries meant that I was forced to bump into a bunch of different kinds of microcontrollers and sensors and vendors and all sorts of stuff. And so I got good at doing that and good at trying to wade into something as quickly as possible. That's great. On tight timelines, it was important to communicate well about what was likely to be done and what was not likely to be done and to try to mercilessly hack away at requirements and things to get to, again, it's important to identify the problem you want to solve and then solve that problem and not the other ones. So it became very important to clearly identify the thing the client was most interested in doing or learning about and then optimizing as much as you could for solving that problem. And then, you know, as much as much flowery, nice gravy on the side as possible. But like you needed to hit whatever the MVP feature set was and anything else was nice to have.

**Chris Gammell:** And that was your job as a consultant, not as like a manager's job. You had to be like, well, if you do this, it's going to add three months or how did that actually interaction go down?

**Carrie Sharpglass:** It came from a variety of places, but MindTribe was very small and very picky about who they hired. And so the expectation was certainly that individual engineers would would have those conversations with clients as well. I mean, you know, you if there's someone who's really hard to deal with or there's a lot of sensitivity or something, then maybe that's not what happened. But generally, the engineers were in those meetings and helped make those decisions.

**Chris Gammell:** So it's interesting to me because I had a past job. I worked with some consultants and they were. A bit rude, to be honest, they were very, very talented, but they were they were they I think they felt very comfortable with the scenario they were in and they very much spoke their mind. They're very strong, you know, strong willed and like that stuff I'm fine with. But the way that they did it was very rude, especially at least from my, you know, somewhat naive standpoint of it. But now on the other side of the equation, as a consultant, I find myself wondering is like, oh, you know, some of the things they were saying were, you know, smart things. I disagree with how they said it, but like I'm always curious about how the interaction goes down. And I guess I'm wondering if you were empowered to do that as well. That it sounds like you were.

**Carrie Sharpglass:** I think so. Yeah. Yes. Like I would I would say that I was there's definitely I guess as as you have probably experienced, there's sort of sometimes some not really cross purposes, but if you're paying someone to be a consultant, you want to feel like you're like you're paying them because they're you feel they convinced you that they were an expert at this thing and they could help you solve this problem. And so part of that is like showing your expertise because you like you needed every new every new client. You have to convince that you are in fact not like a talking doorknob and you do you do actually know what you're doing and you're worth paying. So there's I have definitely had this maybe doesn't directly answer your question, but I've certainly had lunches and stuff with clients where I was very intentional about telling like strategic war stories in order to encourage them that I did in fact know what I was doing.

**Chris Gammell:** Right, right, right. No, I think that's and I think that's the right. I don't know what I'm actually getting at here other than to say that the consultants I worked with in my past were kind of a holes and I'm I don't I know I know you and you're not an a hole and so I was just kind of curious about what your experience was like. So it sounds like that's that is the way to do it though, right? It's like talking about past experience is good. I think proving your point showing your work that kind of thing is sounds like stuff you're doing. So that's great. Yeah.

**Carrie Sharpglass:** Yeah, it's so I work at a tiny startup now and yeah, I in some ways being working as like a consultant for this sort of small hardware stuff was great preparation and in other ways it was not.

**Chris Gammell:** Okay. So let's hear what are the differences?

**Carrie Sharpglass:** I think I because you are the lead

**Chris Gammell:** firmware engineer of span.io. We should say that here.

**Carrie Sharpglass:** That is I guess that's true.

**Chris Gammell:** But at the smallest if it depending on the smallest company if it's like four people it's like yeah well carries the firmware guy. It's like okay. Well, right.

**Carrie Sharpglass:** Yeah. So I was number six. I was the first person hired to do software on the device. So yes, I was the lead because I was the primary person and so there was no one else to do that work.

**Chris Gammell:** He's the guy. You know, he's the guy. Yeah. Right. Yeah.

**Carrie Sharpglass:** That that nice title inflation startup benefit.

**Chris Gammell:** Yeah. Yeah. You should change it to VP of firmware.

**Carrie Sharpglass:** I think I when I started I did actually push a little bit on that title envelope and this is where things end up. I guess I thought that I was good at at hacking away at all the things that weren't absolutely critical to the product but I think working at a tiny company where I have all of the skin in the game instead of some of the skin has definitely made it clear that I in some cases as a consultant there's some amount of process that you you like really need sort of as a almost a defensive shield like you you really do need to do very I'm gonna say careful planning but you can you can get shafted if people aren't all on the same page about what you're building and why you're building it and what it's gonna do and so you spend a lot of time or I found myself spending there's like a process for producing not exactly spec documents but sort of like requirements documents and feature lists and stuff like that and you know depending on the client you do more or less of that but in I when I started at this company I definitely felt uncomfortable with the level of planning and eventually I kind of or the level of I don't know too

**Chris Gammell:** too little or too much to I guess I

**Carrie Sharpglass:** was worried that that like I was not building the right thing or I wasn't sure if I was building the right thing and eventually I kind of figured out that like the company is very small we sit at one table like we're building the right thing because we constantly talk to each other about what we're building we don't like that doesn't require documents to be produced and JIRA tickets to be filed you can just you should just talk to a person and then figure it out and it'll be fine

**Chris Gammell:** mm-hmm yeah yeah okay so you're saying this is I guess true yeah if you're coming out of school to lab 126 which has grown I don't know how big it was when you joined it but like that and then Mindtribe it sounds like you've kind of been going to smaller and smaller companies over time yeah

**Carrie Sharpglass:** yeah lab was I think around the thousand to fifteen hundred yeah I don't remember so there's a process

**Chris Gammell:** there because you have to have it you don't you're not sitting here that would be a friggin big table to sit around and it would be very loud to talk right specs right right yeah yeah

**Carrie Sharpglass:** and that was I think that was one of the things that eventually caused me to to decide to leave lab was was I I felt like I was too far removed from the people making kind of product user related decisions which I don't think was unreasonable at all given that I was a fresh out of school engineer working on the software of some random component of the system but certainly being the person writing the software for the device at a startup remove that there is no insulation yeah yeah when

**Chris Gammell:** it's interesting too it's like I've talked to some friends and you know colleagues and people on the consulting forum and similar things and I'm always interested people it seems like a common theme of like I want to have more agency I want to I want to be they don't always say in charge but they I want to have impact on decision-making right it sucks to be removed from everything like you're talking about and just being told what to do like that you know you want to you want to have skin in the game like you're saying but the interesting twist is that some people then say I want to be a manager and I have never felt that but I think is because I didn't I moved away from moving away from the technical stuff usually makes me feel worse and it's like I think going smaller is actually the right you know you don't get necessarily get to work on as as big of projects right so if you want to stay and work on a engine at GE it's like yeah you're gonna be a manager at some point because you just you want to make an impact and do some new thing with an engine it's like yeah that's tens of thousands of people work on that but if you want to work on a thing that's you go to something smaller like you're

**Carrie Sharpglass:** doing mm-hmm yeah I think that's that's probably a good way of I guess it's really like a multi-dimensional curve or gradient yeah between like company size and product complexity and and org size and where you have to sit in the org to feel like you're holding holding onto the reins efficiently and and to be clear I do now have co-workers who are who are also working on device software stuff so I I certainly cannot take credit for for everything that that exists now and they might yeah you're this podcast so I don't want to

**Chris Gammell:** you're the lead man you have to have other people there if you're the lead that's a software yeah right um no you're

**Carrie Sharpglass:** the you're the principle of um of

**Chris Gammell:** analog life right yeah you should see all of my the hordes of people that I command you know many many people

**Carrie Sharpglass:** that's right um yeah I think that's depending on the amount of control you want and the complexity of the product and the size of the company it's possible that if you I can I I also had trouble empathizing with that position but now I can sort of see that at some point the trade-off you make is if you want to have a larger impact on the business the way that you do that is by moving up the chain away from the technical work because those probably aren't the people who need to be in the room when some decisions are being made so like if you want control over non-technical decisions you have to do that by going up not um deeper I guess

**Chris Gammell:** yeah yeah I think that's right yeah yeah you were you were kind of talking about like the you were kind of like talking about mvp and stuff like that I still don't quite understand what you were saying about the you said you're saying the skin in the game thing and that makes sense but what has changed now for you like you're saying that you you were worrying too much and you've tried to scale it back and just write code now or you're saying you've you were worrying too little and you were yeah I've started you dove into more

**Carrie Sharpglass:** planning I think it's more like me and this is this is certainly still something that I'm I'm working on striking the right balance of but I think it's there's a skill perhaps a skill that comes with experience in knowing when you should push back and really you know make sure you get the architecture right and when it matters considerably more that you just implement the thing and then ship it and you're gonna learn so much more by actually shipping the thing and having someone try using it than you are by sitting and polishing the design for two weeks and it's it's difficult as a consultant often there were relatively clear deliverables and so it was like spend as much like you're gonna work on this thing so we're gonna design the thing and then we're gonna build the thing and then we're gonna deliver the thing but right in this context there's a product that we're trying to ship and the only thing that matters to the company is like generate revenue ship product improve product so whatever you do needs to and needs to go towards that end so if if you need to spend some more time polishing to make sure something is safe or reliable or is gonna work great for the next 10 years then that's absolutely worth doing and you should do it but if you're if you're working on like making sure you're dividing your software module appropriately then like maybe you don't need to think about that for more than five minutes that's right

**Chris Gammell:** yeah yeah and that actually I think what it sounds like to me is like it's how you're getting paid right so like as a consultant you're getting paid by the deliverable which is the thing it's like you point to it's like hey there's the thing I delivered it you know and like what you're saying is now you're talking about like experience and yeah you need to deliver a thing that works of course but it's also there's a lot of other inputs it sounds like

**Carrie Sharpglass:** I think that's that's a good way of phrasing it

**Chris Gammell:** yeah what is span I guess we should probably talk about what that is real quick you know we talk about like all these things nice and you know soft skill of talking about things but what are you actually building

**Carrie Sharpglass:** yeah so I mean try to do this in a way that doesn't sound like a pitch loop so span is building a home electrical panel a home breaker panel a load center depending on what name you know it by the thing that your circuit breaker sit in it is specifically designed for people who are using storage with solar which is to say batteries probably with solar so right now if you you like go to the Tesla website and you see that you see the power wall and you think that looks nice and you put your credit card in the machine and you spend thirty thousand dollars or something what you get isn't just the one box that you see on the website what you get is a whole bunch of boxes so that the power wall is actually sort of an outlier in some ways but if you get if you get like battery plus solar you often end up with maybe six of these gray sheet metal boxes on the wall that all get conduited together and then attached to your your home electrical system and it turns out that even though the batteries and the hardware are expensive you often end up spending more money on electrician time installing it and wiring it up together and commissioning it and you do on the hardware itself which is pretty wild yeah so span integrates a bunch of those things together into one bigger box and then also adds a bunch of layers of monitoring and control on top of it which make it much more pleasant to live with battery storage that's great

**Chris Gammell:** that's great I remember when learning about solar panels themselves I was like flabbergasted it's like yeah the cost of the you know the actual pn junction wafer that you're sticking a solar panel are important but like damn that glass and the mounting and the you know the micro inverter the inverter like all that other stuff it's like really add it's not just silicon you know there's a lot of other costs in there to get right to get

**Carrie Sharpglass:** the juice probably so probably an important lesson about the realities of business

**Chris Gammell:** yeah right right that's yeah yeah that's that's the everything else that sounds really cool and so yeah kind of similar hardware-y kind of stuff and then we would we can't talk too much about it I think because of the you know it's a current employer but it sounds like it's got some computing in there and some smarts so sensors you said right

**Carrie Sharpglass:** yeah this is all this industry is is totally new to me I my background is mostly in consumer electronics so I have had to do a lot of learning very quickly about what the industry looks like and even the right words to use and things like high voltage safety because now the prototype that's sitting on my desk at home has like a 240 volt AC power supply and some other stuff attached to it

**Chris Gammell:** well and like you're talking about the deliverables to like that I mean safety like you said reliability that stuff is all really important you know yep it

**Carrie Sharpglass:** mattered a lot for the scooters though the expected lifespan of the scooters was relatively short it matters a lot

**Chris Gammell:** more for this yeah yeah yeah I guess if you're what house house installation timespans now or I guess at least solar solar plus battery installations are what 20 years kind of thing right yeah I don't

**Carrie Sharpglass:** know what we are officially warranting but it's definitely in that kind of order of magnitude whatever the real number is right

**Chris Gammell:** right right right does that change your sourcing stuff like so are you so one one thing I felt in the industrial space has been like yeah 10 years no you know of course why wouldn't you design for 10 years and yet putting in a Linux computer for 10 years it's like oh maybe we should make this swappable because right yeah we

**Carrie Sharpglass:** were just talking about the echo right yeah

**Chris Gammell:** right right right well and yeah so then you're basically creating technical debt for yourself and something that has to you know you're going to update for however many years or whatever and so you're kind of grows exponentially in terms of builds you need but then I think just from a sourcing perspective just pure hardware sourcing you know either you buy them all up front you got a stock room of 10 years worth or you get an agreement that says they'll make it for 10 years or you know you're switching it out at some point you have to like maintain multiple versions so like how are you dealing with that I guess I'm

**Carrie Sharpglass:** not the right person to answer that question I think my the shorthand answer is choosing components that are sufficiently overrated so that as they you know things like capacitors and stuff so as they degrade over time after thermal cycles and years oh sure they they still perform sufficiently I I don't think I have a useful comment on the supplier side

**Chris Gammell:** stuff yeah no I actually I just meant like the the the just thinking purely in the horsepower of like okay so like I'm going to use an example so you don't have to tell me what's actually going on in there but say say you're building like we talked about earlier right you're building something with Android for whatever reason right I don't think you are but let's just use it and you're on Android 9 and you know 10 years from now it's going to be on Android 90 or whatever it is right and it's just like so supporting that and then also having the hardware that's underneath and and that kind of thing like does that mean that you have to do all like you just jump ahead and you're like okay we're gonna do all custom at that point or does it change your design constraints significantly including on the

**Carrie Sharpglass:** firmware side it definitely changes them some it would be it would be really nice to consider it to be a dumb piece of hardware and then right you ship it with whatever set of features it has and as long as those features never change you're never gonna need more horsepower but that's not that's not reality that's not the product I don't I don't think that's I doubt anyone thinks about a sort of programmable network connected thing in that in that way right so there definitely has been some work that's gone into making sure that it will be all the stuff that's difficult to change which is to say the things that are like literally screwed into the side of someone's house will last for as long as they need to last and the stuff that doesn't need to last that long can be swapped so it can stay a little more current so there are certainly are components of our product that have been strategically chosen so that they can be and the product has been physically designed in such a way that some of it is easy to field service and swap out so we don't have to worry about that you know that Android 18 to 19 update really really breaking this right yeah and then you

**Chris Gammell:** have a technician that goes out pops out the old thing but this is exactly what I was discussing and dealing with is like do you basically designing for swappability that's I it's not a real term but like just that kind of idea I guess service designing for service that kind of thing in the industrial space it kind of feels like that's a important

**Carrie Sharpglass:** thing that's yeah certainly keeping that in mind is important here we also we're in sort of an interesting position where we have two customers one customer is the homeowner who's going to live in the house for a long time and needs to be able to use the product and we want to enjoy it the other customer though is installers so typically something like this and really most of a home solar system isn't you don't like go to Home Depot and buy the pieces and drive it home in your minivan you call someone who comes to your site and like inspects it and then quotes you a system which includes a bunch of integrated components those people are solar installers so the product needs to be it needs to be I guess delightful is probably a good word a cheesy but good word to use part of part of the point though is that it makes it easier for solar installers to do their job it's it is a more pleasant experience to install it's a more pleasant experience to set up it saves them from from some things that are big headaches so for instance one of the things you can do with our product is and and this is a totally this is this is totally dumb but you can change the wi-fi network over sell so like the homeowner can open their app and plug in wi-fi credentials which is a totally that to me that seems like a not quite a nothing feature but it seems obvious and unremarkable but the

**Chris Gammell:** alternative they don't have to connect to a access point and then and then figure out which access point they're on and all that other stuff right you're just saying

**Carrie Sharpglass:** it's kind of automagical right it's automagical but it's it's actually even worse than that there are products on the market today where the answer is you know you your solar stuff is on the outside of your house you probably don't think about it unless you have an outage in the case of like storage you're probably not really thinking about it unless you're either a super geek which is definitely a thing that people people who are really interested in in clean

**Chris Gammell:** tech absolutely jones has multiple videos about his solar system yes that's right

**Carrie Sharpglass:** yes um and i can certainly empathize with that um after having spent a lot of time iot-ing everything i could in my house most homeowners and and certainly as this becomes mainstream technology which i think is my expectation you don't think about it it's like on the side of your house and once you're you have a power outage and you remember you have it and that's great so when you change your router because your internet is slow you don't think about the fact that your wi-fi doesn't work anymore and then six months later you open your app and you're like boy i can't see how much house how much power my house is drawing and you don't know what's wrong and so you call your solar installer and then your solar installer has to do a truck roll and then they have to use like the special professional installer commissioning app which the homeowner doesn't have to put the the solar inverter or something's gateway into the special setup provisioning mode and then like ask the homeowner for their wi-fi credentials and then stand there outside and plug in the wi-fi credentials so that like torpedoes half a day of time that that that person could be using to install a new solar system which generates profit instead right they have to do a truck roll to update wi-fi credentials which is just like totally totally doesn't make

**Chris Gammell:** any sense yeah that's a really good point yeah so the so the you're saying that's that's the old way of it happening and now the new way is they just do it themselves and that is a time saver money saver

**Carrie Sharpglass:** whatever right yeah sorry let me try to pop pop a few layers off the stack and remember how we ended up in this diversion well i know we were talking about the uh

**Chris Gammell:** the installers so you said there's two there are two uh two customers one installer yeah and that's an interesting point too about the the installer because actually i have a childhood friend who does this stuff which is interesting and i get to hear some of the business side of things too and like he they they don't have just one product that they sell you know they they sell whatever there's you know a range of services they're quoting multiple different options whatever and yeah they so not only are you they're one of your customers because you want to delight the the installer as a customer you want to be a better solution because they're they'll just sell something else and instead you know like you need to be the thing that like they're like oh yeah no you should definitely use the span io box instead of the the gray box that has all this other stuff

**Carrie Sharpglass:** so right yeah right we want them to think it's cool so they recommend it anyway but we also want them to to prefer it because it's much faster and easier for them and so they're more inclined to quote it into a system and there's i mean that there's a lot of business strategic stuff around that i think which is sort of out of my out of my immediate wheelhouse but that rolls back

**Chris Gammell:** into features that you end up having to put into the device so that's kind of interesting

**Carrie Sharpglass:** right so speaking of serviceability there are a bunch of layers one layer of serviceability is the homeowner being able to debug a unit the next layer of serviceability is our service techs or our engineers being able to remotely help debug a unit when a customer calls or to be able to preemptively detect that there's a problem and either help the homeowner fix it or sort of be be ready to reach out and help them fix a problem and then there's how do we how do our service techs boots on the ground physically solve a problem or debug something and then there's like what is the electrician going to do when it's the end of the day and it's raining and they're outside and they just want this job to be done and they need to throw it on the wall as fast as they can how do we make it as easy as possible for them and then how do we make it very hard for them to

**Chris Gammell:** do it raw yeah that's a good point too yeah like uh for lack of a better word dummy proofing i mean like usually that's me the dummy but um yeah dummy proofing is so it like it pays dividends you know like it's like people think like oh well it's an expert system you want to make it expert but it's like the more you can simplify it that pays off in terms of you know service hours

**Carrie Sharpglass:** multiple multiple times so yep there are lots of people who are users of your product and you should

**Chris Gammell:** consider as many of them as possible yeah definitely uh well speaking of things that have lots of users you are also a uh former maybe current uh writer for hackaday you have many readers current though

**Carrie Sharpglass:** if you if you ask mike um he he he would probably shake his fist angrily at me but oh yeah yes he does

**Chris Gammell:** that and you were the uh the kai cad consultant or the uh the writer for about kai cad a lot too i guess that's true it did end up well i i have a i have a story for you carrie there's a kai cad just has its first uh ultium importer so oh really yeah that's a big one yeah so it's very very rough but it's uh thomas i think who did it but it's um yeah it's i saw it on twitter and um wow it's in the

**Carrie Sharpglass:** it's in the developer branch now so that's kind of exciting oh wow it's baked into kai cad it's not it's not a uh a plug-in or something it's someone else's shipping that i mean it was a plug-in but then

**Chris Gammell:** yeah it got it rolled into the into the source so yeah that i mean that could be a big one you know

**Carrie Sharpglass:** i mean that that without question will be a big one i assume it doesn't require something cheesy like an ultium installation or something right it's totally standalone what you do is you

**Chris Gammell:** pay ten thousand dollars and then you uh yeah you can basically you know spit out this thing no i think it somehow they reverse the file format or something i don't know interesting yeah i wonder how

**Carrie Sharpglass:** stable the format is i wonder if that's that's something that you can sort of like reliably do

**Chris Gammell:** into the future yeah i don't know you should write an article about it though man so well yeah now that you've now that you've told me about it i certainly will yeah you can even like roll in the we talked about this episode you can like put it in there and you know it's great just writes itself yeah guerrilla marketing yeah i mean so uh what would you like writing about when you do write mr author let's see oh this is kind of cool the inner workings of a pcb that was neat

**Carrie Sharpglass:** that was a really cool a very impressive youtube video i don't i don't know pcbs definitely seem like well like like many things like a laser cutter things that seem like magic until you understand how they work pcbs are very magical until you realize that they're actually just wires that are flat and then they're not as magical anymore right well we'll link in all your uh all of your articles

**Chris Gammell:** if you don't have any that are like on the top of mind it's okay man i'm trying to think of stuff that i

**Carrie Sharpglass:** that i was been excited to to write up recently i i've been looking at embedded device file systems i think i did maybe one or two and i think i had a couple more in the pipe that i was that i was thinking about because in the vein of compute becoming inexpensive it's really easy to get a little blob of of norflash or something and stick it on a board and then the kind of old school way of dealing with it is to manually and bitbang is the wrong word but manually sort of bitbang your files onto the disk but it's really it's really preferable to use an actual file system with actual directories and stuff and so yeah yeah and you you can certainly try to use something like fat but it's there are a bunch of file systems which are purpose-built for embedded devices which support you know not using a dynamic allocator which support the right sort of wear leveling and and power loss tolerance and stuff uh and those are it's like a neat a neat thing to have in the tool belt so that you know you can

**Chris Gammell:** reach for it instead of rolling your own thing yeah yeah that's great that's great there's multiples

**Carrie Sharpglass:** of them though you're saying there's multiple like ways to do that yeah i think the the the one that was most interesting that i'm using at work is called little fs which i think i did i did actually write up for hackaday which was or was originally is is still part of the arm embed project so it is actually developed by arm and has really really wonderful detailed documentation about how it works including great ascii diagrams of blocks in the file system and all sorts of things as well as ports to a bunch of different languages including like javascript so if you go to there you go to the like github page somewhere in there there's a link to a javascript demo that lets you play with the different wear leveling and block size parameters and stuff and and sort of visualize how long your file system will last which is very cool yeah that's really cool it also i think there's a there's a fuse module so you can if you've formatted like a flash drive or something in it you could mount it on a desktop

**Chris Gammell:** system there's a lot of good stuff that's great that's great yeah i found the article too it's called cool tool it's a little file system that keeps your bits on lock so yeah we'll put that in yep cool well any uh any last things we should know about you carrie because we've covered a

**Carrie Sharpglass:** wide span of your career so far i don't know that i have anything in particular i'm i'm looking into getting a laser cutter for i so i just moved i went through the process of well trying to iot everything in the house and now i'm kind of figuring out what things should go in the lab space that i now have so i'm i'm finally i think going to pull the trigger on the laser but i haven't figured out i haven't i haven't figured out whether i'm going to go uh chinese budget laser plus mods or glowforge or um one of the other various options but i don't yeah like i don't have a good answer for that full

**Chris Gammell:** spectrum or something like that or something on ebay yeah chinese stuff is just so attractively

**Carrie Sharpglass:** priced but i i think the question is sort of do i want to use the laser or do i want the laser to be a

**Chris Gammell:** project that's right is it a project yeah i think um i think the other question is uh if one of the things that i've moved towards is like if the thing will hold its value so like say you bought like a a decent you know low-end thing that's not like the the cheap you need to mod it if it'll hold its value there's there's lower i for a long time i never thought about the resale of the thing but i've kind of started moving towards that because it's like okay well first off it goes in my my company books is like something that i have to depreciate anyways and like there's actual value there but also like there's just less risk i can just i can just sell it on ebay and you know yeah i take a loss of some amount but not all of it's not like all or nothing so that's a really good point

**Carrie Sharpglass:** uh and i would expect i would expect that especially in the case of a laser a higher end laser from a manufacturer i certainly having browsed uh used epilogues and stuff they hold their value remarkably well

**Chris Gammell:** right right exactly it's like i'm gonna buy one of those uh yeah right so you know you could rent it out to people too or some you know just make a business out of it if you want that's a a dangerous a dangerous and good idea yeah yeah well good luck with that uh hopefully i hope the new lab works out well thanks yeah me too i know we all have time to be in our home labs for now that's for sure

**Carrie Sharpglass:** it is really really i think i've been to the hardware store every weekend uh with an increasing pile of different projects and things around to work on great time for housework that's right

**Chris Gammell:** that's right all right well thanks for joining us carrie yeah thanks chris it's uh it's been a

**Carrie Sharpglass:** pleasure talk to you soon yeah sounds good you

**Speaker ?:** you
