---
episode: 144
title: An Interview with Bob Davidson - Hoodied HP Hijinks
url: https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded May 7th, 2013, episode 144, with guest Bob Davidson, hooded HP, hijinks.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Bob Davidson:** And this is Bob Davidson with Ambient Sensors.

**Dave Jones:** Hey, Bob. Thanks for joining us. Is it Bob or Robert? It's Bob, right?

**Bob Davidson:** I go by Bob, yeah.

**Dave Jones:** Yeah, everyone does, right? All Roberts do, don't they?

**Bob Davidson:** Especially here in Australia. If I hear Robert, I think I'm in trouble.

**Dave Jones:** Robert J. Davidson, come here immediately. Exactly.

**Bob Davidson:** Yeah, exactly.

**Dave Jones:** Very, yeah, Bob is like, you know, the sort of stereotypical name here. Like, he's my uncle. Yeah, Bob's my uncle here in Australia. Bob literally is my uncle. I do have an uncle, Bob. That's how Australian I am. Yep.

**Bob Davidson:** That's good. Thanks.

**Chris Gammell:** Yeah.

**Dave Jones:** So tell us about yourself, Bob.

**Chris Gammell:** Okay, well. Tell us your life story. Oh, gosh. And go. Put him on the spot.

**Dave Jones:** How long do you have? Well, my parents met. Yeah, exactly.

**Chris Gammell:** That was just a glimmer in my father's eye.

**Bob Davidson:** Well, I...

**Dave Jones:** Well, start... Sorry. Like, you start out where you're working at the moment and what you do, and then sort of go back and how you got started in electronics, because everyone wants to know that.

**Bob Davidson:** Sure. Okay. Well, I have a small consulting and product development company here called Ambient Sensors, and it's in Boise, Idaho, and do custom electronic design for all sorts of people. One of the projects that we've been working on recently is a hit detector for football that measures how hard football players get hit and then alerts them if they should be checked. Checked? Yeah. What do you mean? Like a concussion? It measures the probability of a concussion, and it alerts them if there's a 50% chance of a concussion. Oh, right. I gotcha. A concussion.

**Dave Jones:** I thought you were talking about the ball. No, you're talking about... Oh, no, no, no. Right. The body sensors.

**Bob Davidson:** It measures how hard they get hit in the head. Yeah. Right. I was working with the people at the Injury Biomechanics Lab at Wayne State University and another group up in Ottawa called Biokinetics, and they built this tester for measuring... Banging heads. Yeah. Exactly. And... What a great rig to build. Yeah. Well, and they got it by studying video of guys banging heads, and so the thing has realistic velocities and forces. But to give you a feel for what it's like, it's really violent. If you put a football helmet on and then let... If Dave put a football helmet on and then let Chris take a baseball bat... Wait, can we hook this up?

**Dave Jones:** Which he's been dreaming of doing for years. Yeah.

**Bob Davidson:** As you say, is this a possibility? No, it's really awesome. The pro players are getting peak G-forces of 120 Gs. Holy crap. Over, you know, impulses that are about 15 milliseconds wide, but...

**Dave Jones:** Well, yeah, 150, that's not many Gs. I mean, if you drop something on a hard surface of a bench, you can get thousands of Gs right there. I mean, G is just deceleration in a given distance. Right.

**Bob Davidson:** But when it's connected to a head rigidly, so that's because of MA, then that's why you have to calculate the energy of the impulse, and it gets pretty substantial. Yeah.

**Dave Jones:** Which is just basically the area under the curve is the energy of the impulse.

**Bob Davidson:** Yeah. Yeah. And there's something called the head injury criteria that actually uses that, and it's an experimental curve that was developed actually originally for the automobile crash business, but then it's been extended into this.

**Dave Jones:** So this is like a standard curve, is it? A standard impact curve?

**Bob Davidson:** Yeah, that's recognized by the insurance industry and the auto crash. So this thing has a little three-axis analog devices accelerometer and an NXP microcontroller that does all the management of that.

**Dave Jones:** How do you find those MEMS accelerometers? Because I've never used those for shock and vibration testing. I've always used like a real, in quote marks, you know, accelerometer from ICP or from Brul and Kerr or someone like that.

**Bob Davidson:** Right. So the – you mean in terms of how close they agree?

**Dave Jones:** Like its response, its linearity, its calibration, all that sort of stuff.

**Bob Davidson:** Are those things any good? Oh, they're awesome. Actually, I've been doing testing here with what we call a drop tester, which has a laboratory-grade accelerometer.

**Dave Jones:** They're the ones I've used, yeah, the lab-grade ones. And they come with a cow certificate and a response curve and the whole, you know.

**Bob Davidson:** Oh, yeah, and fancy amplifiers and lab view and all the rest of it. And then we drop it into a – onto a pad that has a certain durometer that gives the kind of impulse that we want. And I get, you know, 90 – you know, I get very good fits to the data like 0.998. Wow. For a goodness of fit and things like that when I've plotted one against the other. So it's actually – it's very good. Awesome. Okay.

**Dave Jones:** I didn't think they were that good. I thought, you know, they're okay for getting a tilt on your mobile phone, but I've always wondered how good they are for actually, you know, their linear calibration.

**Bob Davidson:** These go up to 200 Gs, so they're really not the same as exactly – although they're similar technology, they're not the same as what's in the mobile phone. Right. But the use case before this one for these accelerometers is setting off airbags and cars. Yeah. And so the ones that are used – and that grade of accelerometer is pretty reliable, of course. And so – And it'd have to be, yeah. Expensive. Good one to use.

**Dave Jones:** So all you pussies wearing helmets in your sports over there because we don't have – you know, we don't wear helmets here in our football. Right. Exactly. So that's – is it just in the helmet? Is it – or like you've got them on the body and stuff like that?

**Bob Davidson:** In this case, it goes in the chin cup, the part that holds the helmet onto the – and they – but they wear them very tight and it's very rigid. The overall, you know, combination of chin cup, helmet, and skull is – forms a pretty rigid body. So we do a lot of correlation work. And actually, one of the things we have to take into account is the angle of the hit and so we can compensate for –

**Dave Jones:** I was going to say, can you determine the angle of the hit?

**Bob Davidson:** Yeah. I can through the – because of the initial acceleration, I can work it out.

**Chris Gammell:** Oh, right. Yep. So is this all – do you actually beam it over to like the sidelines or something or is it data logging so that once they are hit, they just kind of pull it off and see?

**Bob Davidson:** Okay. So the other side of this is that we wanted to make one that was affordable at the high school level because that group of players is probably the least observed and most vulnerable. Yeah. And the most career ahead of them. Exactly. Hopefully. And they have – so the system that I've been building only stores the data locally and uses a USB connector to download it. We looked at wireless and that could be an option later. But the wireless is just not reliable enough. So what we do right now is we – at least for the low-cost stuff over an area of a football – the size of a football field with all the other interference. Right. Yeah. So what we do is we have a very bright LED and when the player gets hit where there's a 50% chance of a concussion based on that curve I mentioned earlier, it flashes bright red and they're supposed to go off and get checked to see if they actually did suffer a concussion. At least change the helmet out.

**Dave Jones:** I can see this becoming like a crowd thing. Like, you know, if it goes – I know. You know, if it pulses bright red, the crowd erupts. You know, hit him again.

**Bob Davidson:** That was one of the worries actually is that people start trying to – Yeah. They would hurt each other more, right? Yeah. It's like the – you know, like in the carnival where you hit the hammer down on the thing and try to ring it. Right. Right. Oh, boy. But there – I am actually on a national committee that's setting standards for this because there will be eventually standards for like how many hits. So, one of the issues is not so much the concussions, although it was bad enough, but there's a whole spectrum of impacts below that level and they're starting to find accumulative damage. And so, they want to set – although these standards haven't been established yet. How many concussions you can sustain per game. Exactly.

**Dave Jones:** Which is crazy because if you ask any neurologist, they will say one concussion is too many. Do not even get one. You know, like – yeah, I guess, well, these sports have to exist, right? So –

**Bob Davidson:** And the protocol now, if you do get a concussion is you're supposed to rest for – you're not even supposed to play video games or do anything. What? Even think. Well, because they want to cut down the blood flow. You know, it's micro tears in the brain tissue and so. So, it's – yeah, it's not a – take up cross-country running or something.

**Chris Gammell:** Suddenly, the average mass of a cross-country team goes up by, you know. Yeah. A tenth of a football player, right? Yeah.

**Dave Jones:** So, that's what you're currently working on with your own company, Ambient Senses?

**Bob Davidson:** That's one of them. I'm doing some way scale work and other different things that come along.

**Dave Jones:** Is this just a one-man band company? This is just your own?

**Bob Davidson:** Actually, I have myself and a couple of other people now. I didn't really mean to have a company. Right. Yeah, goddammit. I don't want to run a damn company. But I had done a startup before and then I was working at the local university. But with the cutbacks and things, that job went away. So, I just started this company as a way to pay rent.

**Dave Jones:** Oh, so you're not currently working at the – you're not a professor at the university?

**Bob Davidson:** No, I teach still for them. I just don't get paid very much. Right. Okay. Like, this semester I'm teaching engineering statistics. Oh, yeah.

**Dave Jones:** Well, you're a funster. Yeah. Yeah.

**Bob Davidson:** They don't want to spoil the reputations of any of the other faculty on campus. Right. The whipping boy of teachers now, right?

**Dave Jones:** So, how does that work? Like, you get paid less. So, you're what, considered a temporary teacher?

**Bob Davidson:** Well, they call it adjunct faculty.

**Dave Jones:** Ah, right. Okay. Adjunct professor. Adjunct professor. Ah, right. Adjunct professor. I've heard that term. I never really knew what it meant.

**Bob Davidson:** It means you don't get paid very much. Yeah. And you don't have tenure. Yeah, right. Okay. But I do it out of a, you know, sort of community sense and also keeps me involved with the university and all that sort of stuff. So, this is University of Idaho? It's called Boise State University. Oh, Boise State. Okay. Yeah.

**Dave Jones:** Why Idaho? Were you born and raised Idaho or did you move there for some reason?

**Bob Davidson:** So, Idaho is totally like so many important things in your life, totally by accident. Detail. Yeah. Yeah. Yeah. Well, so, when I was in my first incarnation as a graduate student, I was at Johns Hopkins working in x-ray astronomy and we had an experiment that we flew on an Air Force satellite out of Vandenberg. And so, I came out west. I had gone to school as an undergraduate up at Washington State University. And so, I came out west for the satellite launch and I went up to visit my friends at Washington State. And actually, Dave will relate to this. I was visiting with my friend and his kid needed to have his diaper changed. Right. So, while he was back changing the diaper, the phone rang. So, he asked me to answer the phone. Well, it was another friend of mine that was working down here at HP had just opened up a division, the disk memory division down here. And they were looking for people to staff it up. But the reason why it's in Boise is because Hewlett and Packard used to like to ski quite a bit up in Sun Valley. That's right. Yeah. They even had a ranch up there. That's right. And the guy who was the CEO at the time, John Young, was from Nampa, which is a small town close by. So, there's no other good explanation except that just pure accident. Serendipity. Yeah. Yeah. And I – but I did get in early days in the disk drive business. Well, the disk drives back then were, you know –

**Dave Jones:** Manly disk drives.

**Bob Davidson:** Yeah. They were the same. One of ours actually used a washing machine motor for the – Yeah, gas powered. But we also could sell them for amazing amounts of money. We had a 400 megabyte drive. I think it was about a $25,000 piece of equipment back then. That's the thing that actually – so, well – so, I graduated from college in 77. That's before you were born, Chris. Yeah, I know. Yeah. And I got – I was first licensed as a ham radio operator in 1967 when I was like 12. Yes, awesome. Yeah, okay.

**Dave Jones:** Okay, that was before I was born. I just want to establish a timeline. Yeah, no, it's good. It's good.

**Bob Davidson:** And just before that was dinosaurs, right? Right, yeah. Well, according to people in some states in the US, yeah. Yeah, exactly. So, anyway – I forgot where I was headed with all that. Music graduated in 77. That was, I think, where I started. Yeah. But, yeah, so disk drives, you know, were still – disk drives and microcontrollers and that kind of stuff were only available in big corporations. Yeah. And computers, basically. And PCs came out in the early 80s. But what amazes me at this point is how much access to technology there is. I just got a – I just bought one of the new LPC Link 2s, their new debugger, and it's like 20 bucks. I know. It's crazy. And it –

**Chris Gammell:** Versus ice prices, right?

**Bob Davidson:** Yeah, and you can run a SEG or JTAG on it or the NXT or Red Probe and all this other stuff.

**Dave Jones:** Well, that's the thing. People don't realize before about 1990, you know, doing your own microcontroller stuff at home was practically unheard of.

**Bob Davidson:** Yeah.

**Dave Jones:** It was impossible, really. You just couldn't afford the tools. Yeah, it was impossible.

**Chris Gammell:** Well, I remember Jack Gansel said he built his whole first business on doing an in-circuit emulator, right? I mean, like that was just an entire industry on its own. So, yeah.

**Bob Davidson:** Now the tools – Oh, sorry. No, no. Now the tools have just gotten so amazing too, the software tools to do the development. And the same thing – okay, so I feel so silly. So when I first did PC boards at HP, we actually used tape. Oh, yeah. On paper. Nice. Oh, yes. And then took a picture of it. Yeah. I mean, they had done that. Priest hasn't. No. No. And so, you know, things like Eagle are just amazing to me as well.

**Chris Gammell:** Yeah. I mean, having had fingertips and everything, right? The cabs.

**Bob Davidson:** Although the other thing that's been, I think, very exciting is the kind of things like Dave's doing with his video and other people. That there's this community around the open source and Jerry's stuff. You can go out on the web now and learn so much if you want to. So being an autodidact is a much easier thing now than it used to be. Yeah. Unless trips to the library, right? Yeah.

**Chris Gammell:** Knocking on doors, begging to sit in the lab for a little while.

**Bob Davidson:** Well, but what's amazing is also how willing people are to help. So we were talking earlier about the Bluetooth low energy. And so, well, I haven't ever done anything with Bluetooth low energy. And I had a project that came up that really needed it. And I started looking around. Well, there's this Jeff Roberg on an open source hardware site. And so I got in touch with him. And he's just turned out to be a ton of help in getting the Blue Giga BLE 112 up and running. And even was able to provide Eagle footprints. And so just, you know, being able to do stuff these days is amazing. And I think it's the synergy of all the people working together that make it so interesting.

**Dave Jones:** Well, that used to happen before the communications revolution, except you used to send letters. Yeah. Or you'd call people up on the phone, you know. I'd get letters in the mail. Can you help me with this? So I'd spend all day writing a reply, you know, writing a reply letter and lick a stamp and send it back. And that's how you communicate and share information.

**Bob Davidson:** I have some really funny ones. My dad came. My dad saved some of mine from when I was a kid writing off to these big companies asking for parts. And I built a phase lock loop based radio teletype demodulator back in about 1970. And it was based on one of these brand new LM 565s. I think it was a 567. Oh, yeah. The thing, it replaced a refrigerator sized piece of hardware at NASA, you know. It was one of the things they claimed at the time. Which it probably did. And I ordered one and the company thought I was some other big company or something anyway. So they, you know, it showed up on Christmas Eve by special delivery and all this stuff. And I just wanted to work on it over the... Awesome. And I built a board and we had a... I forget why we had this. Our school had a... I think it was for exposing printing plates or something. A UV light source. Like a light box? Yeah, a light box. And so I was able to take it to school and spray on the resist and then expose it through a negative that I got made.

**Chris Gammell:** Man.

**Bob Davidson:** That's why we're looking at that on the internet, right? Now I just send off Gerber files. Yeah. And then boards come back in a few days. Exactly. Magical world. It is. It's hard to decide where to divide your time too because you could go, you know, do all these things still. But it doesn't seem worthwhile. Tell us about it. Worthwhile in some ways.

**Dave Jones:** It's a bane of every engineer's existence these days, isn't it? Yeah. There's just too much stuff to work on and just, you know, too much cool stuff to play with and not enough time. I know.

**Chris Gammell:** Right. I know. It's crazy. I've cut down on sleeping. Have you guys tried that? Yeah.

**Dave Jones:** I'm trying that, but, you know. Yeah. Wife doesn't get happy.

**Bob Davidson:** I've been reading a lot recently that you really should get eight hours of sleep to be creative, but...

**Dave Jones:** Yeah, no. You totally should. Well, nah. Some of my best stuff has been done with my eyes practically shut, you know. Oh, really? Yeah.

**Chris Gammell:** That was under the gun probably too, right, Dave? It's not like something. Yeah, no. Of course. Yeah.

**Dave Jones:** Having that timeline. Yeah.

**Chris Gammell:** I bet that was more of the key there.

**Bob Davidson:** Possibly. Yeah. That's one of my biggest motivators.

**Chris Gammell:** I just sit there like in a stupefied, you know, sleepless haze and I'm just like, I just click stuff at that point, but, you know, I still want to be doing it, right? Right. Yeah.

**Dave Jones:** So, tell us about this startup. This startup you did, because we always love hearing startup stories.

**Bob Davidson:** Well, this one, so most of the startup stuff you read, you know, the Facebook stuff is all business porn pretty much. Yeah, yeah. So, this one, it was kind of, it was a fun project, but it nearly ruined me financially. Oh, yeah. Do tell. Yeah. People love to hear these things. You got to be. Take the good. You take the bad.

**Dave Jones:** Be willing to lose all your money. Yeah.

**Bob Davidson:** Yeah. You got to be willing to do that. I don't know. You got to, the problem is, okay, so a startup should really be looked at as a business hypothesis that you're going to test out and you should be dispassionate about it. And at the point where you've proven that it's not true, you should stop at some point. But there's, there was, you know, those, those, those inspirational posters that businesses like to put up. Like with the cat hanging out by a finger?

**Speaker ?:** Yeah, yeah, yeah.

**Bob Davidson:** The one that was the ship and, you know, so, you know, anybody can sail on, you know. The one I always liked was winners never quit and quitters never win. But anyway, never mind. I forget how that went. Sounds like the posters worked. Yeah. Excuse me. Okay. So the idea, you know, I learned a lot from it. I'll have to say that. I learned a lot. But, but the idea was a consumer product and, and getting traction and the resources you need to do a consumer product. That's tough. Really difficult. Yeah. Because the idea was, and this is, okay, so this is back in 2001, 2002. You can also be too early into things.

**Dave Jones:** Like pre-Kickstarter. Yeah, pre-Kickstarter.

**Bob Davidson:** So we had a, essentially a media center PC that was controllable through a wireless pad. But it was one of those early Windows CE. Oh, yeah. Pads. Right. And it had, and it, and it was pretty awesome. And it was, we tried to differentiate it from just a big remote control by some of the things it could do. One of the things it could do is really simplify working with media that was on the internet. One of the other things it could do, though, is display video from security cameras. Because the idea was that maybe you'd be watching the movie, but then the doorbell would ring and you'd want to decide if you needed to answer the door or something like that. Or if it, or if you had a swimming pool and you wanted to monitor it. But the security part of it is what got traction. So we kind of pivoted at one point when we weren't really making many sales in the entertainment side into security. And then sold the company to a small publicly traded company up in Canada. But then the guys that bought it tried to cram down all the early investors, including all the people that invested with me and my own self. And it got, you know, they actually succeeded in pulling a lot of the capital out and having the stock. Because I thought when we sold it to a publicly traded company that that would be providing liquidity for the investors, which is what you're always looking for. And, but they had, as part of the sale, there was a period of time where they couldn't sell. And in that time, they stripped it. Yeah, they did. Bastards. And then we had to get lawyers and it was a mess.

**Dave Jones:** And then, yeah, right. It's not fun anymore.

**Bob Davidson:** No. No. Well, I learned a lot. That's what everyone says, yeah. But it wasn't one of these deals where you, you know, work for 18 months and sell it for a billion dollars to Facebook.

**Chris Gammell:** That's never happened.

**Bob Davidson:** Well, Instagram. Yeah, right. Well, yeah, exactly.

**Dave Jones:** But, yeah, out of how many startups? Millions? Right. Yeah. Like, yeah, there's, you know, a dozen success stories. Nobody ever talks about the failures. That's the problem. No. Not the failures, but the non-success stories.

**Bob Davidson:** Well, I mean, if you look at it as a hypothesis, then either a positive or negative outcome is a good outcome because you've driven it to resolution. But the problem is if you get so enamored with your product that you don't quit when you really should. You're right. Yes. That's the, yep. The, but we almost, it was a close failure. Missed it by that much. Exactly. Exactly. But one of the other things I learned was to do something or to have at least some way to have an income early on. This other product, you know, we worked for a year on it before we started trying to sell any. It's better to do something with it when you're first starting out that doesn't have such a, unless you have somebody with really deep pockets to back it. Yeah. So the current company right now, I have some projects in the background that are sort of longer term. I'd like, so what I'm doing right now is more product development for other people. And the problem with that is it doesn't scale very well because you either got to, you know, charge more. Or so many hours to sell in a day.

**Chris Gammell:** Or work longer.

**Dave Jones:** Well, you're basically selling your hourly rate, right? You're charging your hourly rate and you're a gun for hire. That's, you know.

**Bob Davidson:** Exactly.

**Dave Jones:** So there's no big payoff at the end. You just get continuous employment and you can eat. Congratulations.

**Bob Davidson:** Which is actually, well, so the way we're using it is, you know, do some product development on the side. And to try to be strategic about the projects that we take on, for example, this Bluetooth low energy project gets us involved in learning a technology so that learning becomes kind of an asset of the company. Yeah.

**Dave Jones:** Right.

**Bob Davidson:** Smart. That is smart. Yeah. Yeah. Hopefully, it turns out.

**Dave Jones:** You're interested in this low energy stuff, Chris?

**Chris Gammell:** I am. Yeah. I have the, so you guys are using the 2540 chipset, right? Yeah.

**Bob Davidson:** That's what the, it's Blue Giga is the company in Finland. What they've done is put some nice, well, they sell these modules, first of all, which are FCC approved. So you don't have to put your equipment through the. That's awesome. That's a big saving. There's no reason to do them. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. And then they also have provided a C API that you can compile if you have an external limb microcontroller with your code. Oh.

**Chris Gammell:** What's it talk over? Is it just talk over some serial?

**Bob Davidson:** Over a UR. Yeah. Through the UR on the CC, on the CC2540. And then, but they also have something called Blue Giga Script, which is even, which allows the module to actually, because it has a 8051 controller. Yeah. Yeah. Controller. So the module itself, you can actually hook sensors directly to the module and run Blue Giga Script on it and not really have to hook up an external MCU to it. So it can be a standalone. Very nice. Kind of cool. And the other thing about Bluetooth low energy. So it's really Bluetooth and name only because it's really the very lowest levels, like the physical layer that are Bluetooth. Yeah. Right. Yeah.

**Chris Gammell:** The stack on top is different, right?

**Bob Davidson:** It's very different. And it's designed for sending, you know, bursts of structured data. So, you know, if you have a thermometer or something. And it has a different way of hooking up. So it has, if you have a sensor hooked to your Bluetooth Blue Giga module, and then it advertises that I've got temperature data. So anybody that walks in the room with an application can say, oh, that can attach to it. And, um.

**Dave Jones:** Right. So it's like a Windows, like it's like in Windows, like it's a generic USB microphone or something. It's just that it's. Right.

**Bob Davidson:** Yeah. There's a thing. There's a thing called the general attributes file and, and packet that's part of the advertising that, that tells everybody what it can do. Huh. So, um, you know, whereas with traditional Bluetooth, you have to, you know, send a pen back and forth and do all this.

**Chris Gammell:** Right. Yeah. It's like a handshake at that point, right? It's really, um.

**Bob Davidson:** Yeah. Uh, so it's really designed for, um, for sensors. And the Blue Giga script is a pretty cool way to, um, program it because you can, you just need an XML editor. Oh. And, um, and then they provide an application that works with the TI CC debugger, the same one that TI supplies when you work directly with the CC2540. Yeah. Yeah. And, uh, and you don't have to install IAR and all that expense, um, associated with that to program it then. Yeah. Yeah.

**Chris Gammell:** Yeah. I see a lot of interest in that kind of stuff. I mean, a lot of people, I, you know, I see a lot of projects online switching over to Bluetooth finally. And if you think about it too, I mean, you think about Android devices or even, you know, iPhone devices too. There's just, there aren't that many ways to get into the phone. And that's kind of the, the de facto gateway these days, aside from going through the web.

**Bob Davidson:** And I was reading an interesting article yesterday though, about, uh, what this is doing to Apple's ecosystem, because they used to require that you join this. Oh yeah. Mifi or MFI, M-E-F-I.

**Chris Gammell:** Yeah.

**Bob Davidson:** Having that, uh, that, that Apple chip on, unlike a wired device. Yeah.

**Chris Gammell:** That does the translation.

**Bob Davidson:** And, and if you were designing hardware for Apple, you had to use that 32 pin connector that they've got that's special and nobody else has.

**Bob Davidson:** Terrible. But now with the Bluetooth, you don't, you can bypass all that. So yeah, that's a good thing. Awesome. Um, um, and, and Bluetooth low energy is on some of the Android devices that are on some of the, uh, Samsung Galaxy. Yeah. And the HTC One, I think. Yeah.

**Chris Gammell:** I've been shopping for those. I was, I was telling these guys before the show that I'm trying to, I'm starting to shop for Google Glass stuff because that, that has low energy, Bluetooth low energy stuff, but it's hard to find.

**Dave Jones:** So you have to have a specific phone with low energy support? Is that, is it a different chipset inside the phone? Is it? No. Or is it just one chipset that handles low energy mode?

**Bob Davidson:** Um, I guess they probably have to have a dual mode. Right. Chip. Chipset. Yeah. But that's pretty common. I guess that's the main thing. But then otherwise it's just software.

**Chris Gammell:** Yeah.

**Bob Davidson:** Right.

**Dave Jones:** And that's the key thing. A regular Bluetooth phone can't talk to a Bluetooth low energy device. No. Right. Okay. I need a new phone then.

**Bob Davidson:** Yeah. Yeah. But, uh, but it, but I think it's going to become more common and, you know, and you turn phones over every couple of years anyway. So. Yeah. Right. I'm just a cheap ass. Yeah. Same here. No, no.

**Dave Jones:** I just keep cursing my phone instead of buying a new one. I just curse it every day. You know?

**Bob Davidson:** I've got my, uh, my Ericsson block phone.

**Chris Gammell:** There you go. Yeah. There you go. It's good for, you know, paperweighting and stuff like that. Right? Yeah. So. But. Oh, I love it. Anyway, that's good stuff. What about some of the older stuff? I mean, uh, so you, you'd sent a picture out the other day on Twitter because you're very active on Twitter, which is great. And, uh, that's that.

**Speaker ?:** Yeah.

**Bob Davidson:** I like to tease Akiba.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. And you had sent a picture of, uh, you in a hoodie and you said, uh, I was wearing, I was wearing hoodies before Zuckerberg was even born. That's true. Right? That's true.

**Bob Davidson:** Um, so what that. What is in this picture? Okay. What that is, is a, um, a system for measuring how the recording heads fly over the disc. And it's a, it's a heterodyne interferometer system. So I take the single frequency laser at 632 nanometers and split it and then frequency shift it with these things called acoustic optic modulators. So the, so the, uh, those, uh, signal generators up in the corner of the rack, um, those are just to drive the acoustic optic modulators at certain frequencies. But what happens is when you recombine the light, you create an optical beat note and, uh, and the phase shift of the beat note, which you can, you can bring that beat note down into the few megahertz range if you want, or even down into Hertz. Um, in fact, you can actually slow it down just like you listen to a beat note between two tones and you bring the tones closer in frequency and you get that wah, wah, wah thing. You can see this all in the optics, but what it does is it lets me then measure the phase by just measuring the phase of the, of this like two megahertz optical beat note. And, um, so I could get, um, you know, with the phase detector that I had, which had a 10th of a degree resolution, I could measure, you know, the lambda over 3600. In other words, 632 nanometers divided by 3600. So I was getting me like a 10th of a nanometer resolution and position, but with a 500 kilohertz, um, bandwidth. And I, and I, and I, what I would do is form an image of the whole, so I would illuminate the whole head and the disc around it. And so this is the actual, the, the head of the, uh, the recording head. Yeah. Yeah. Out over the, cause what, well, so in magnetic recording, the head's actually flying over the disc, but if the disc, if the head separation changes, it modulates the amplitude and affects the, you know, air rate and other things. Yeah. It starts to bleed over channels and stuff then? Or you, well, you can have that if things get really bad, but just, um, back then we were trying to have raw bit air rates in the neighborhood of, it seems like 10 to the minus eight or something like that. And then we had boosted with ECC up into the 10 to the 10th.

**Dave Jones:** And you didn't, and you're, you're just doing this in the lab, right? I don't see like any, you know, I mean, usually these hard drives are, uh, you know, vacuum sealed, right? They're sealed to keep out dust and crap.

**Bob Davidson:** Yeah. Well, I did under, it was kind of, it was fairly clean conditions.

**Speaker ?:** Right.

**Dave Jones:** Fairly clean. That's a clean body other thing. As in, you would smoke outside instead of inside, right? Yeah. Right.

**Bob Davidson:** Actually, it's funny that back then they did allow people to smoke inside. Yeah. But, um, no, uh, you notice the disc diameter there is about 14 inches. Yeah. Yeah. It's huge. So, and the flying height was quite a, was at the time seemed really small, but we were flying at like 19 millionths of an inch above the disc surface.

**Dave Jones:** Ah, that's a, you drive a truck under that. Yeah, exactly.

**Bob Davidson:** And, uh. You'd have an earthquake on one touch, right? Yeah. So we had, you know, what we were trying to do was, uh, design the mechanical structure that held the head out there so that it wouldn't flap in the wind. And, you know, um, disc drives, they get pretty warm if you run them, especially if you can get some of those 15,000 RPM drives, they get pretty hot. Yeah. And most of that, most of that heat is just the air friction. And there's very little of it. Very little, very little of it's actually the electronic heat or the usual, you know, electronic heat that we think about.

**Dave Jones:** Yeah. Yeah.

**Bob Davidson:** And, uh, so, you know, designing the mechanical structure inside to deal with all that was a pretty good challenge. It was, the disc drives were a lot of fun to work on because they had all these servo systems and mechanical challenges and magnetic challenges and electronic and, you know.

**Dave Jones:** This is a great photo. You've got to see it, folks. We'll definitely post this as your feature photo for the product thing. Or would you prefer your Twitter photo? No, no, no. This one's awesome.

**Bob Davidson:** That one's fine. Excellent beard, by the way. Oh, thanks. Yeah.

**Dave Jones:** And so this is like a, um, is this an anti-vibration laser table?

**Bob Davidson:** It's, it looks, it's just a giant piece of granite. It was like, it was four by six feet by a foot thick. Wow. That works as well. Yeah. And, uh, and then the disc is actually on an air bearing spindle. So the spindle's very low vibration, very low run out.

**Chris Gammell:** And what, what year, what time frame was this?

**Bob Davidson:** This was the 80s? It was about 19, no, it was about 1981. 81. Okay.

**Dave Jones:** All right.

**Bob Davidson:** Yeah.

**Dave Jones:** What, uh, model HP scope are you using there?

**Bob Davidson:** Oh, those were like 1740s.

**Dave Jones:** All right. No, no, no evil tektronic scopes in the building? Oh, no.

**Bob Davidson:** It was pretty funny when people would want to get something like that. I mean, sometimes they had to because that was, you know, they had the capability we didn't have.

**Dave Jones:** What's this purchase order for this tektronic scope?

**Bob Davidson:** Well, actually, um, it wasn't, there was, it wasn't so much that there was a, so HP was an awesome place to work, um, when I was started there. Um, very different than the company it is now. Um, but it was 82 different divisions and each one had a product and the, and each division was run as a small company. So, uh, disc memory division was one of the largest ones. It had 300 people in it. Um, but most divisions were, you know, 50 to a hundred people and they had all the functions of a small company. And, and the advantage of that was they were really close to their customers. The disadvantages that HP looked at from 30,000 feet, the way the CEOs and MBAs look at it, looked like a real fragmented place, but it really wasn't. Um, but the, um, so anyway, it was, um, yeah, 1981 and, um, And who is the role of age? Oh, what I was going to, yeah, now, yeah. And, and what I was going to say is that, so Agilent now was part of HP then. And so the reason that they broke up the company was again, an MBA thing. They broke up the company because they, they, they, the, the stock on computers had higher multipliers than the stock on the instruments. And so people thought if they broke it up, then the half that was computers could run at a higher multiplier in the stock market than the instruments.

**Dave Jones:** That old short term gain chestnut. It was, exactly.

**Bob Davidson:** It worked for a little while, right? I don't know. I'm sure it worked a treat. It never worked very well at all. I, every time they did a merger, you know, you, two plus two equaled one and a half. Right. Never, never, never made it to four, much less five or six. Um, but they always convinced people that it was a good idea. Um, the, um, what, what I, it's a long way around to what I was going to say is that the, um, so we got these instruments for transfer costs, they called it. So basically we got, we got the instruments for paying the, the bill of materials on it. We didn't even labor. No. Oh wow. That's pretty good. And so, and so we'd trade disc drives for oscilloscopes. High alley deals. Disc drivers were worth a lot. So, yeah. So we had a lot of nice instruments. Um, and Hewitt and Packard actually would come around. Um, you know, so like I've got this old HP signal generator that was Bill Hewitt. It was based on Bill Hewitt's master's work at Stanford, but. Oh, 200, right? Yeah. Uh, and, um, and I got them to autograph it. They were just around one time looking at, so I got them, but they would do, I mean, they were the sort of people that you could just walk up to and talk to. And I had a little bit of a, one of the nice things that HP did for me was I, uh, they sent me back to graduate school. So I got my, uh, PhD back at Carnegie Mellon, um, while, while working for Hewitt Packard. Wow. That's awesome. So I was like one of the better paid graduate students. You mean paid? Yeah, because the deal was they paid all my tuition books. Plus I had 75% of my salary while I was going to school. Oh my God. That's awesome. I know. They would never do that these days. Yeah, these days, right? And you can find any company that does that, right? Yeah, so I wrote, he'll had a nice thank you note after it all was all over and he wrote back and it was just the kind of people they were. And that's really cool. Whereas, um, I was in a meeting with, I don't think, I think this is fair to tell, um, they can't fire me anymore. Yeah. Oh, please do tell. Come on. So, um, so I was in a meeting where they had all the, um, sort of, uh, senior engineers. It was a technical meeting, technical, HP internal technical conference. Right. So there were the hoodies as far as the idea. Yeah, exactly. And actually the HP guys were more like the old ham radio operators. Suit and tie. Skinny tie. Well, you know, no, it was always a jeans and t-shirt kind of place. It was, it was always the only, yeah, they never, you never saw a tie around there. And if you did, people would make fun of you. But, um, no, so we were there, we were there. This is when Carly first came in. And, and so if it was Hewlett and Packard, cause I'd been to these kinds of meetings before, they would come and have dinner or have breakfast. You know, they'd always have a breakfast buffet beforehand in the morning and, and they'd come sit at the table and talk and find out what was going on. Well, the way HP changed when Carly came in was we were sitting there having breakfast and then over the PA system, it says now introducing the CEO of Hewlett Packard, Carly and she walks out on stage with spotlights and her syncophanced in the audience, you know, and then as soon as she was done, uh, she took a few questions from some of the shills in the audience. And then, and then, uh, and then, uh, then, uh, then she said, well, I got to go and walked off and never, never, never, never talked to an engineer. So HP in the days when I was working there and sort of the, the apex of it, I also worked on a HP labs and Palo Alto was, was sort of a great engineering company to work for. Um, and, um, and there's still parts of it that are good, but it's just not the same as it was because it used to be really, really of buying for the engineers.

**Chris Gammell:** Right. I wonder if that kind of thing is even ever possible these days. I mean, like, Oh, there are companies. I'm sure it is. I think it is.

**Dave Jones:** You think hardware has got to have the right attitude.

**Bob Davidson:** I mean, yeah, I think so. There are companies actually, um, Seagate is a little bit like that, at least the part of it that I've been to. Um, they have.

**Dave Jones:** It's very common in software companies like our team who I used to work for. I mean, that was a dream job. You know, there was no management, no adult supervision, no meetings, no nothing. You know, it was just do whatever you want. Yeah. It was just, you know.

**Bob Davidson:** Actually, what they used to say is work smarter, not harder, but they really, and it was management by objective. They really took that seriously. So, however you could get, if you agreed to do something and however you could get it done, they didn't. Done.

**Dave Jones:** Then that's it.

**Bob Davidson:** Yeah. Exactly. They didn't try to tell you how to do it. That's good.

**Dave Jones:** So, if any of our listeners out there work at a company like that, please, uh, tell us. I think Jerry... We'll even have you on the show to talk about.

**Bob Davidson:** Jerry did, I thought.

**Dave Jones:** Well, yeah, until they gave her the ass, yeah. Which we might hear about shortly.

**Chris Gammell:** I'm really curious to hear about that. Yeah. So, speaking of, uh, management, I mean, so you said management by objective, which is the, that's the, like the Bill and Dave thing, right? I mean, that's what their, their big thing was, but, but you actually had another, uh, management consultant and I'm sure Dave will start groaning now that I bring it up, but, uh, you, you had, you had someone sit in with you that, that's, uh, pretty, pretty famous as well.

**Bob Davidson:** Oh, yeah. You were talking about, uh, Clayton Christensen, um, who's famous in, in, uh, the, in the business management circles for his, uh, book, The Innovator's Dilemma, which actually is a, uh,

**Dave Jones:** sorry. It's serious.

**Bob Davidson:** Well, actually I saw it happen because what he did, his, I had, I hosted him at, uh, here because he did his PhD work on, um, studying the disk drive business. And I saw the things that he described in there, I could really relate to because the things that he describes in that book really did happen in the disk drive world. Um, but yeah, he was out when he was a PhD student and I just hosted him around cause he was collecting information on disk drive companies at the time. Yeah.

**Chris Gammell:** That was one of the big examples. And then I think he talked about like a backhoe companies was another big one.

**Bob Davidson:** Yeah. Well, in disk drives that you have these companies that come in and people kind of ignore them like for disk drives, it was Connor. They, you know, we were building these big, um, high margin, 14 inch disc. And Connor came in with a five inch disc that was kind of a toy, you know, that went into like PCs and it just, the, the performance wasn't any good. Nobody, nobody thought it was. Oh, another thing that used to happen back in those days is that people tried to protect their hardware by having proprietary interfaces. Oh. And HP tried to ride that for as long as they could, but, um, you know, the PC. Scuzzy cables. Totally changed that. Yeah. Yeah. The standards kind of, you know, yep. And, uh, and the companies like Connor got better and became, you know, Seagate. And, uh, I was at what started Seagate. I didn't know that. Um, I don't know the exact pedigree, but it's all in entangled.

**Dave Jones:** Um, it's a very incestuous web, the hard drive. Yeah.

**Bob Davidson:** It is actually, um, well, you got out though. I mean, yeah, well, I did the reason. Well, so HP decided they couldn't make it anymore in disk drives. Um, and, and whether they could or they couldn't, it's debatable, but, um, but they got out of that business.

**Dave Jones:** And so I, uh, by selling it, was there anything to sell off in the end or had they just been totally trapped?

**Bob Davidson:** No, they just, they just walked away from it. Um, there was some technology. They tried to capture some of the technology. Um, but if you don't capture the people with, you know, giving somebody a stack of lab notebooks doesn't really do a lot of good. Here, fix this. The big companies, you know, do a lot of patenting, but the patent business for them is not so much about the IP and the patents as it's just the overall throw weight of who has, you know, how many patents. And, um, so. Anyway, I let, so the disk drive business kind of, it's funny because they sent me to school and, and within a less than a year of coming back from school, um, they shut down the division. And, um, so I got involved in a tape project actually called linear tape open, which was a new standard that got established. And HP is one of the companies that helped to establish that. Type? As in magnetic type? Magnetic tape, which is still used quite a bit in archive. If you think about a hierarchy of archive, you have, you know, fast drives and then slower drives. And it's still eventually when you get back far enough, you get onto tape because the volume density, information storage density of tape is, is hard to beat. That's why I say don't, you don't, don't, you can't, uh, underestimate the transfer rate of a station wagon loaded with tape. Yeah, right.

**Chris Gammell:** The, uh, the next step up from sneaker, sneaker net is, uh, wagon net. Yeah. Yeah.

**Dave Jones:** Because it's sheer surface area, right? Because like you probably assume you can't get the same density on tape as you can on a hard drive, just due to the physical geometries and stuff.

**Bob Davidson:** You can do pretty good, but not quite as good.

**Dave Jones:** Not, not quite as good. But the fact is it's very thin tape and you can roll hundreds of thousand meters on one little spool.

**Bob Davidson:** Yeah. And it's, you know, so. And if you, and you have a, if, so the way the, in these, so the software that manages these, uh, storage systems is pretty amazing because it can kind of work out and figure out which data is not being used very much and move it further down the hierarchy until eventually it winds up on tape where, you know, stuff you never, and it's all handled kind of transparently.

**Chris Gammell:** This is like cloud software you're talking about? Like, like high level storage?

**Bob Davidson:** Data center software, yeah. Huh. Is that like the, uh. They make, well, I just have a friend who makes these big disk arrays now for HP and they can store a petabyte. And I said, oh, you work on pedophiles. Right. They can store a petabyte of data now, though it's not a big deal. Yeah, that's crazy. That's not uncommon. Man, that's a lot of data. Well, there's a lot of things making data these days. That's true, yeah. Yeah. Me? Sorry. Yeah, the FBI's got to store all the phone messages. Yeah. And every video that I produce, yeah. Yeah, exactly.

**Dave Jones:** So that they can declare me a terrorist. Exactly.

**Bob Davidson:** Just throw random words into your video like plutonium or something. Yeah, I know.

**Dave Jones:** Yeah, yeah. White House and, you know, president. Yeah, exactly. Yeah, that's a great idea. Red flag. Awesome. Yes, that's my goal.

**Bob Davidson:** But, you know, NASA, each of those probes generates a lot of data, too. So, I don't know. There's a lot of places to store data. Facebook. Facebook. That's kind of embarrassing. I remember when I started out, when I was at HP Labs and we were on the early ARPANET, and how I just felt insulted that they were starting to let commercial operations onto the ARPANET.

**Chris Gammell:** This is ours. Bob, were you like the first troll? You're like, get these people out of here. I know.

**Bob Davidson:** Back on the old UUSCP groups thing. Well, it just seemed like it was, yeah, it was sort of commercializing something that was pure. There goes the neighborhood. Yeah, we didn't lock our doors back then, you know. And now I've got firewalls and antivirus and everything else. But I totally missed the whole web thing. I just thought that was a fad.

**Speaker ?:** No, really?

**Bob Davidson:** Oops. These things happen, you know. You'll get it next time. How can you make money on that? Yeah, right. Facebook, that's a dumb idea. That's kind of dumb.

**Dave Jones:** But there's a lot of dumb people out there. That's the sheer weight of dumb people.

**Bob Davidson:** I still don't know how they make money on Twitter. I guess they do.

**Chris Gammell:** I don't think they do yet. I don't think they do.

**Dave Jones:** No, I don't think it's a profit. Well, yeah, it's not a profit. I don't think it's a profit-making enterprise.

**Bob Davidson:** But you know what's amazing to me about Twitter is it's kind of like a cocktail party that never stops. So you can, you know, I get on there and, you know, Cuba's in Tokyo and Microbuilder's over in Paris and Chris is on and VK2, ZAY and all those people. And so there's always something interesting. And, in fact, I have to shut it off when I want to get real work done. Yeah, right.

**Dave Jones:** Is your Twitter name, is that your ham?

**Bob Davidson:** Yeah, that's my ham call sign.

**Dave Jones:** W-A-7-I-U-T.

**Bob Davidson:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** I was actually talking to people about, because I just got my radio finally, and I've been trying to find, like, the repeaters around here. And so I was asking about that, you know, because I, like, got it all queued up to the right frequency and everything, and I'm just sitting there waiting, waiting, waiting, waiting. And I go, well, what the hell is going on here, right? And someone says, well, you know, there's Twitter. There's just tons of other ways to communicate, whereas before, repeaters were it, right?

**Dave Jones:** Chris just jumped on the BAM. Chris got to the party. I didn't realize he's the only one left.

**Bob Davidson:** Yeah, yeah. It is pretty quiet, I have to say, compared to what I remember. Hello? Anybody out there? Yeah. Cell phones. Now, out here in Idaho, it serves as real public service, because there's lots of places where cell phones don't get.

**Chris Gammell:** Yeah, right. But, yeah, I mean, just the repeater network before, I mean, it seems like that's what it used to be. And now, you know, you just see, there's a lot of call. I see a lot of call signs on Twitter, which is great, because, you know, people are making these longer contacts. Yeah. And I think it's actually not. Well, no, no, I didn't mean it like that. I didn't mean it like that, although that is pretty funny. I meant that they, you know, they try for the harder stuff with their actual antennas and stuff, you know. Yeah. That's what I really meant, not that.

**Bob Davidson:** Boy, this radio thing's easy. They get on Twitter and set up their radio contacts. Yeah, right.

**Dave Jones:** Well, technically, if you're using a notebook, you're on wireless, right? Exactly.

**Bob Davidson:** Yes, I pinged somebody in Germany. That's raised an interesting issue, though, because when I started out, I had lots of help, and I built a lot of electronics when I was a kid. It was tube. It was made out of tubes. Yeah. But it was still electronics. And nowadays, well, the maker movement and all the stuff that's been going on with the tools and things is a good thing. But there's been a period where people weren't really building a lot of hardware, it seems like. Yeah.

**Dave Jones:** Yeah, the 90s to early 2000s was a dead zone. Yeah, it really was.

**Chris Gammell:** Well, everybody's getting excited about computers, right? I mean, Bob, it's your fault you've made all these disk drives, right? I know.

**Dave Jones:** Well, but that was the problem back in the 90s. That's all people cared about was computers. Electronics as a hobby had almost vanished. You know, it was really quite dicey there for a while. Yeah. I thought the whole thing would actually vanish.

**Chris Gammell:** Yeah.

**Dave Jones:** It seems to be coming back. Well, you know, it wouldn't vanish, but like it would, you know, it would, like all the magazines would die, and then nobody would care about it on the internet. But now, holy crap.

**Bob Davidson:** Yeah, it's a big change. Love it.

**Chris Gammell:** It'll be interesting to see it at Hamvention, too, just to see if it, I mean, like, I don't really have an idea of, you know, if there will be less people than old videos showed and everything.

**Dave Jones:** No, there'll just be lots of old greybeads standing around tweeting each other, you know.

**Bob Davidson:** Yeah, right. Yeah, Chris mentioned it looked like Woodstock, and I said, oh, boy.

**Chris Gammell:** I don't know. You don't want to see naked ham people, right? No. Not the ones I've seen. Right.

**Bob Davidson:** I think there were, I did notice that our local hamvention a few weeks ago, which I went to, so I still stay in touch, that there were a bunch of younger people there. So, that's probably a good sign.

**Chris Gammell:** Yeah, and Tony, who we've had on the show before, who talked about microwave stuff, I mean, he said, I think he sent me a link showing that the ARRL membership is up a lot more than it used to be, too.

**Bob Davidson:** Yeah, and Tony's, I like what Tony's doing with making the microwave stuff available to people. Yeah. I'm real tempted to jump into that.

**Chris Gammell:** Yeah, that's it. I'm just getting started in the quote-unquote low-frequency stuff, you know. Yeah. High-frequency for me used to be like 20 kilohertz, and now it's moving up a little bit.

**Bob Davidson:** That's another interesting thing, I think, because high-frequency digital circuitry used to be like, I don't know, what, 50 megahertz? 10, 20 megahertz? Yeah. That was 50. Whoa, you know.

**Dave Jones:** Hold on to your hat, folks.

**Bob Davidson:** And the radios now that are up in the 5 gigahertz and 10 gigahertz range that are all solid-state digital things.

**Chris Gammell:** Crazy, like silicon, germanium, indium, whatever's in there.

**Dave Jones:** Now we've got kids, you know, building their own PCs with 4 gigahertz processors.

**Bob Davidson:** Oh, I know.

**Dave Jones:** In SoC, it's just ridiculous.

**Bob Davidson:** I was giving Akiba a hard time because I just built one of those recently, and I said I was going to put Linux on it so I could use VI and AARC and GREP and stuff like that. Yeah, well, I don't think you'd be alone in that. But at 3 gigahertz. Oh, right, yeah. Actually, what is amazing about PCs also now is that you can throw these virtual machines on, and then you can't have Linux and all this stuff all in one box running at the same time.

**Chris Gammell:** Yeah. Yeah, that's great for, like, troubleshooting. I mean, like, I know I've worked with some people, too, that they, you know, they'll throw an emulator on a virtual machine. It's not quite as fast, right? And then you have to kind of jiggle with the playthrough, you know, the pass-through of, like, USB or whatever you're debugging with. But, you know, you can actually have entire ecosystems of your, you know, like your compiler and everything else in a virtual machine, and then you boot it back up, and you have that exact same system. So that's a nice little trick you can do, too.

**Bob Davidson:** Yeah, I do that. Sometimes vendors will send you, like, I got an analog devices A to D converter, and they sent along a little, well, it was really something that was based on LabVIEW. Oh, yeah, yeah, yeah. And it really wanted to run an XP, so I just set up an XP virtual machine and put it in there, and it didn't collide with my other LabVIEW. Yeah. Yeah, so it's a great thing. That's pretty cool.

**Dave Jones:** Please, can we not talk about PCs anymore? Okay, yeah, we'll stop. Consumer.

**Chris Gammell:** Yeah. Consumer world. Well, they're all, I mean, there's still tools we use, though, right? I mean, it's like not like electronics to get away from it. Yeah, I know, but that's it.

**Dave Jones:** You know, they're just pens, really. Yeah, right. No, that's a good one.

**Bob Davidson:** Well, I have one on my bench, but it has a bunch of debuggers and... Yeah, LTSPYs. Oh, another thing that's kind of amazing is like these silly logic analyzers that you can hook onto your PC now and do a pretty decent job of analysis with that.

**Chris Gammell:** Yeah, versus the old huge Agilent or HP boxes, right?

**Bob Davidson:** Yeah, or having to buy one of these expensive, although they're not really expensive, you can't really call them expensive anymore, but one of these more expensive scopes. Like I've got a Rigel scope here, the 1052. But I'm tempted to go to the new 2200. The new 2000? Yeah. Yeah, very nice. And you would start to get... Yeah, I watched your YouTube on that.

**Dave Jones:** Yeah, the comparison video of those two. Yeah. Yeah, I know. It's amazing how far we're coming four years.

**Bob Davidson:** The other thing that's just awesome, and I bought it even though I really didn't have a use for it right now, which is the Rigel 815 Spectrum Analyzer. Oh, yeah. Which goes for $1,500 and it comes to the tracking generator and...

**Dave Jones:** Amazing bang per buck, yeah.

**Bob Davidson:** Yeah, well, I don't know, a year ago, you'd probably have to spend $12,000 to get that.

**Dave Jones:** Yeah, I know. Yeah, several years ago, the average person could not afford a Spectrum Analyzer. If you're lucky, you've got a second-hand old boat anchor one off eBay. Yeah. But apart from that, yeah.

**Bob Davidson:** And this is a pretty decent one. Yeah. I mean, it's probably...

**Dave Jones:** Yeah, it's not too bad. It's not going to do leading edge stuff. No. But neither am I. Well, exactly, because it's phase noises, you know, it's phase noises not that great.

**Bob Davidson:** I'm not trying to build a cell tower here.

**Chris Gammell:** Right. No, exactly. That's right. Can it do a 66 gig or what's the... Oh, it's only 1.5. Yeah, 1.5.

**Bob Davidson:** But it's good for your ham radio. Yeah, yeah, there we go. I mean, honestly, like that... I can look at the Spectrum Purity in my HandyTalkie.

**Chris Gammell:** Yeah.

**Bob Davidson:** That's pretty cool.

**Chris Gammell:** So you had mentioned, you know, you're doing more... You do some open source hardware stuff too. I mean, what... Is that some of the energy harvesting stuff you had done or what was that?

**Bob Davidson:** Yeah, that was one project. Just try to give back in a small way because I've learned so much. So it's possible to be a double E and not actually do circuits, by the way. Yeah. Yeah. You know, what I did mostly for HP was model magnetic materials and do computer models of, you know, actuators and disk drives and things. And I worked with some really interesting people and that was a lot of fun, but it wasn't designing circuits or biasing transistors and stuff like that. So I've actually...

**Speaker ?:** Yeah.

**Bob Davidson:** And I'm really attracted, I guess, because of my personality to the sort of self-learning that goes on. And so, you know, watching Dave's videos on how to do PCBs now, because I had to learn how... I found out that nobody tapes down... I had to go learn... What? You use computers for that? Yeah. I know. And so I had to learn a whole bunch of new skills and so... But I feel like it's... One of the things about openness and about open source hardware that I found is that you get back more than you could ever give out. And so, like, I've been doing this little energy harvesting thing, which is more personal interest. I'm interested in wireless sensor networks and we have one over here in a grape vineyard where you monitor the grapes. And that's a whole other story. But the energy harvesting interests me because you've got to be able to power the sensors out in the field. And so I built this little open source project. And I've gotten email from people all over the world about it that are just interested in it and tried to help out some of them. A lot of college students that are trying to do a senior project on energy harvesting. Yeah, yeah, yeah. But, you know, I try to help them out as much as I can. So, yeah, I like... And I went to the open source summit. And that's a great thing. If for no other reason than I got to hang out with Akiba and Kevin Townsend and John Engineer and all those people back in New York last October...

**Chris Gammell:** Yeah, I'm hoping to go to that one again this year. I went to the first one, but I couldn't...

**Bob Davidson:** Yeah, I was going to the one this fall. Because I think everybody that I was with said they wanted to come back this coming fall because they had such a good time.

**Chris Gammell:** It's actually in Boston this year, too. Oh, is it? Yeah. I didn't know that. Yeah, I was surprised, actually, because it's actually not... So, usually it used to be in New York, the past three have been in New York at different... Like the Hall of Science, which is where Maker Faire is, or at Lightbeam, which is where it was last time, right?

**Bob Davidson:** Eyebeam, yeah.

**Chris Gammell:** Eyebeam, sorry. Yeah. Same thing. Yeah. And now the people who are putting it together, they're up in Boston, so they're moving it up two or three weeks, and then it's going to Boston.

**Bob Davidson:** Oh, okay. Well, that's fine. Boston's a lot of fun, too.

**Chris Gammell:** Yeah, it's a great town.

**Bob Davidson:** So, I went to the... The only thing I don't like about Boston is going to the Museum of Computers because this stuff all looks brand new to me. So, I was like, what's this doing in the museum? It's still perfectly good. So, is this like the gift shop, or... Yeah, really. Exactly. Right.

**Dave Jones:** And where's the museum?

**Bob Davidson:** Actually, a lot of the computers that I worked on, the companies that made them don't even exist, like Data General and DAC. Oh, yeah. All that stuff. That's crazy.

**Dave Jones:** I noticed you've got a HP multimeter on your bench there, with a little handheld. Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Geez, you don't see too many of them around anymore.

**Bob Davidson:** Yeah, I don't think they make those. I just bought a brand new Fluke 289, their true RMS voltmeter.

**Dave Jones:** Oh, yeah.

**Bob Davidson:** That's a good one. It seems like a pretty good...

**Dave Jones:** Shit, battery life, yeah. Well, you know. Yeah, you're good.

**Bob Davidson:** I go to Costco. Go to Costco.

**Chris Gammell:** How about you do some energy harvesting?

**Bob Davidson:** And I have a microcurrent here for the energy harvesting at EEVlog. Excellent. Microcurrent. I got it from Adafruit. Oh. There you go. Excellent. Actually, it's a great thing. Yeah. Yeah. Because one of the big problems with the energy harvesting and wireless sensor nodes is being able to figure out if you're, you know, how your software is affecting the current drain.

**Dave Jones:** Drain, yeah. Exactly.

**Bob Davidson:** And, but as you noted, and I guess that's why you make it, it's really hard to do, measure microamps.

**Dave Jones:** Nanoamps. Well, I originally made, the story behind that is I originally made it because I wanted to overcome the burden voltage in the multimeter. It wasn't necessarily because I wanted to measure nanoamps. Yeah. You know, it was just, I want, you know, I found the burden voltage annoying. So I wanted to, you know, take that out of the equation. And I thought, when I was designing, I thought, oh, I could throw in a nanoamp range. Yeah, that might come in handy one day. And, you know, that's what most people seem to buy it for these days is the fact that I can measure nanoamps.

**Chris Gammell:** Yes.

**Dave Jones:** And, you know, I just didn't, you know, I didn't think that would be a target market. Oh, I think it's. Five, five years ago when I designed it.

**Bob Davidson:** Yeah. No, I think it's perfect for that. Speaking of multimeters, the first multimeter, my dad was a ham radio operator and that's partly how I got into it. Oh, that's awesome. But he had one of those Simpson meters. Oh, yeah, the analog. The 260 probably. And I would always, so my dad and I, you know, would butt heads quite a bit because I would use the tools and not put them back. And then he would come and want to do something and find the tools. And it was always, but he always wanted me to work with him on stuff too. So I guess it wasn't such a bad thing. But I used to burn out that meter every once in a while because I would, you know, it's tube days and it's 300 volts. And you have it on ohms and stick it across 300 volts and burn out. Yeah, yeah, yeah. And then you'd have to go replace the resistors in the thing. Yeah.

**Chris Gammell:** They weren't very forgiving. No. No diodes built in. No, no. No mercury valves or whatever it would be the tube equivalent of diodes. I'm not sure.

**Dave Jones:** Well, no, you usually wouldn't burn out the meter movement because I think the meter movement had diode protection across it.

**Bob Davidson:** Yeah.

**Dave Jones:** I'm not sure about the Simpson 260, but most meters had, yeah, back-to-back diodes across the meter. So you wouldn't blow that out. But as you said, you'd blow out input resistors.

**Bob Davidson:** The dividing resistors. Yeah, yeah. And so you'd wind them with, you know, well, he worked out at Hanford, which was an atomic plant up in Washington State. So he had access to some laboratory gear. So we'd like wind new resistors to put in the front end of the thing that I'd burn out. That's really cool. Yeah, my first radios had mercury vapor rectifiers in them.

**Chris Gammell:** Yeah.

**Bob Davidson:** And the old OA2s had a nice argon glow to them. There's lots of smells and sensation. And my first radio had a 6L6 crystal oscillator driving a 6L6 vinyl. And it was cathode keyed. So when you'd unkey the thing, it would come up to 300 volts. And if your fingers slipped off, you'd get the shock of your life. Oh, my gosh. But stuff that you'd never get away with today. It was amazing. Yeah, yeah, yeah.

**Dave Jones:** Yeah, yeah, right.

**Bob Davidson:** And I remember once this old railroad guy gave me a whole bunch. He gave me boxes of batteries because they would replace the lamps with new batteries. And there were those 6-volt. The wet cells? Yeah, 6. Well, they were not wet. They were just, you know, I can't describe them. But they were, like, bigger than D-cells.

**Dave Jones:** But they were lantern batteries.

**Chris Gammell:** Well, we used to call them lantern batteries. Yeah. Yeah. You mean, like, spring terminal on the top and everything? Yeah. And so I remember...

**Bob Davidson:** 12 volts or this? Yeah. Yeah. Well, they were 6 volts, I think. Yeah, yeah. And so I had, you know, like, 50 of them. So I thought, well, let's just... Yeah, of course. Let's just whack them in series. Yeah. That made a really scary power supply. Protonic induction. Yeah. Yeah. Exactly. Yeah.

**Dave Jones:** Well, you can do the same thing with 9-volt batteries today. You don't even need to wire them up. That's true. Because they just clip back to back. And you can get 1,000 of them and put them in series. And you can arc, you know, you can arc shit over. Yeah. It's really, you know...

**Bob Davidson:** Actually... It's really dangerous. I was replacing all the batteries at a summer camp that we were helping out at and sticking them in my pocket as I went along one day. But I also had my keys in that pocket. Oh, no. And all of a sudden, my pocket started getting real hot. Yeah. I was like, oh, I know better. My neck is melting. Yeah, those 9-volt batteries.

**Dave Jones:** And just before that, you used to ride a dinosaur to school. That's right. Yeah.

**Bob Davidson:** Actually, it's amazing what people used to do, though. Or what I can... It was my first radios were all World War II surplus, but they weren't that old at that point. Because the war was only, like, you know... 20 years of years. 10, 15 years before. Yeah. Yeah. Right. Or a Korean war surplus. Yeah. Oh, there you go. Yeah. Yeah.

**Chris Gammell:** Nice.

**Dave Jones:** Chris, you've heard of the Korean War. I'm surprised.

**Chris Gammell:** Yes. I had some relatives serving it. And also, I've seen MASH. So, you know, there's that. Yeah, exactly. That's not what I know about it.

**Bob Davidson:** Yeah.

**Dave Jones:** Well, they don't call it the Forgotten War for nothing.

**Bob Davidson:** But, you know, that's another thing that's kind of interesting is when I was a ham radio operator in my teen years, I joined this thing called a military affiliate radio service. So, we actually handled traffic and phone patches for soldiers that were over in Vietnam at the time. Really? Wow. And what that, that was how people were able to talk to their families back then. It was very sporadic because you know how hard it is to talk on HF from here to Vietnam anyhow. Yeah. And so, we...

**Chris Gammell:** You get away from the right ionosphere stuff. Yeah.

**Bob Davidson:** And so, we would pass messages and sometimes do phone patches for people, which would be very brief. And just because the conditions wouldn't support it for too long.

**Chris Gammell:** Yeah.

**Bob Davidson:** But now, in Iraq or Afghanistan, they just have cell phones and...

**Chris Gammell:** Skype, right. Skype and talk.

**Bob Davidson:** So, that's another measure of how much things have changed. Because that was, you know, that was the state of the art. Yeah.

**Chris Gammell:** That's pretty cool.

**Bob Davidson:** That led... One of the things that the ham radio did lead to is I got my commercial radio telephone license and then I worked on two-way radios when I was in high school. And that was a really good job for a high school kid.

**Dave Jones:** Actually what? Actually repairing them? Yeah.

**Bob Davidson:** Well, I started out... My first, very first job when I was 15 was working in a TV shop when they used to actually repair TVs. You know, check the tubes and do all that stuff. Yeah. But then I got into... Yeah. It was a two-way radio business. So, I worked for the local Motorola company and they installed radios for the, you know, public utilities and people that, you know. And phone patches, even mobile radio, you used to have to call into an operator and then they'd patch you into a telephone network. It's kind of crazy when you think about it.

**Chris Gammell:** Yeah. I mean, that's just hanging out there then, right? I mean, it's not like it's like a private phone call at that point. It's like, well... Yeah. Well, there's that too. Yeah. You're basing it on the fact that people don't have radios, you know.

**Dave Jones:** I can remember listening into people's mobile phone conversations back when we had the analog network. You know? It was on 700 megahertz or something and I'd tune in with my scanner and you'd... Yeah. You know, it was boring as bad shit. Yeah. Yeah. I'll be home at seven o'clock for... What do you want for dinner, honey? Yeah. Yeah. I got this new phone.

**Bob Davidson:** It's so cool. But yeah, it's way different now. Yeah.

**Chris Gammell:** So what about... So you're teaching now too though. So you said statistics, but you have some other stuff on your research that you've done there and other stuff you've taught there. What was the one I saw in there? It was... Crud. I lost it. Uh-oh. What are some of the courses you taught there? Oh, here we go. Finite element methods. Is that like actual magnetic finite element analysis type stuff?

**Bob Davidson:** Yeah. And the antenna stuff.

**Chris Gammell:** Oh, antenna stuff. Okay. My buddy took a class for like transformers and he did some finite element stuff. Yeah.

**Bob Davidson:** So when I started working in that, I started working with this group at McGill up in Montreal. Oh, yeah. Toronto. Montreal. Oh, Montreal. That's a Montreal. And Pete Sylvester and these guys. And they adapted that method from what civil engineers used to do. But we used to use it to design electric machines like the actuators and disk drives. Huh. And the actuator has a certain force response to the current going through the coil. But that becomes a gain block in the servo loop. And so you want to have, you want to map out how that varies with angle. And we could model that with the finite elements because we could get an accurate model of the magnetic fields. So you would like... Yeah.

**Dave Jones:** It's a very common technique for all sorts of things. Yeah. Very wide ranging. Fea, you mean? Yeah. Well, yeah. Yeah.

**Bob Davidson:** Because you're solving the differential equations. And, you know, as Feynman said, the same equations have the same solutions. So, you know, I initially started out using a thermal model, which is just solving Poisson's equation. But it was for heat flow, but you could change the names of things. And then it became, you know, for magnetic materials. That's awesome. But then we developed... But then there's some special things that Maxwell's equations do that thermal things don't do that you had to take into account. And so we developed our own, you know, programs for doing that. And actually, you talk about the disk drive business being incestuous, but the finite element world is really... They're right. Like the guy that started Ansys and HFSS and all that. Oh, yeah. Those packages. Yeah. Zoltan Sundeis was a graduate student at Pete Sylvester, who was the guy that I was working with at McGill. Huh. Yeah. Yeah. So I taught some courses in that because it's a neat way to... I mean, there's only about three or four problems you can actually solve in electromagnetics by hand. And then you have to go over to, you know, computer methods. Yeah. But that came along with digital computers, too, and the rise of PCs and the power of what you can do with those. And so those tools are... And there's a lot of interest in kind of mixed physics models now. So you have, you know, eddy current heating and that couples into a thermal model so you can model the actual...

**Chris Gammell:** It's like holistic now almost? It's like current creates heat, affects current back and forth kind of thing? Yeah.

**Bob Davidson:** Yeah, they do. Actually, you can... Wow. In the magnetic world, that's sure the case. Huh. Just because the materials change or what? The materials have changed... Most things have magnetic properties that are dependent on temperature.

**Chris Gammell:** Oh.

**Bob Davidson:** And in fact, what they do in disk drives now, they've gone over to real heroics in disk drives because there's something called the super paramagnetic limit, which has to do with if you keep making the bits smaller and smaller, you get to a point where just thermal energy can cause them to flip on their own. Yeah. Yeah. Well, it's nasty business. And the way that you prevent that is increase the corrosivity or the resistance to change of flipping. But the problem with that is then you have to increase the fields that come out of the recording head and you reach a point where you really can't push it any further. So, what they're doing now in the current generation of disk drives is they use a laser to temporarily suppress the corrosivity by heating the material. And then you write on it and then turn off the laser and it cools quickly and sort of freezes in the magnetic pattern.

**Chris Gammell:** Wow. This sounds like... I mean, like, just hearing about this stuff, I mean, I'm very impressed with all this stuff. It's a house of cards. It's amazing that, like, there's so much energy spent on this. Not even energy, but just, like, so much brain power to just keep squeezing more data on there. I know that it's an economic driver thing, but, man, it's so cool.

**Bob Davidson:** Well, you know, you can buy little terabyte drives at Costco now for... Yeah, right. That's the result of it.

**Chris Gammell:** Right, right. And then we, you know, put Jersey Shore. We store, like, digital editions of Jersey Shore. I mean, like, that's the ultimate thing that my brain goes to. Yeah, or Facebook.

**Bob Davidson:** But actually, the story of the increase in aerial density, they call it, the bits per square inch in disk drives, is pretty amazing because it's gone up at a very consistent rate over the years. It's just, like, orders of magnitude every few years.

**Chris Gammell:** Yeah. Is there Davidson Law or what?

**Bob Davidson:** No.

**Chris Gammell:** Who got named after that one? I mean...

**Bob Davidson:** Oh, the super paramagnetic limit? I don't know. It's just called the... We're not as clever. No, Gordon Moore. Let's come up with a... They wouldn't have the marketing guys working with us, so we'll just call it the super paramagnetic limit. That's what I used to say. That's catchy. Yeah, they said if HP sold sushi, they would call it cold dead fish. Right. Somebody else came up with the name sushi to make it sound good. That was the problem with HP. But the neat thing about HP is it was selling to other engineers, so we kind of knew our audience.

**Chris Gammell:** Yeah, exactly. It doesn't matter if the test equipment's all four-digit numbers, right? You just assign your own value in your head of it's something awesome, right? Yeah.

**Bob Davidson:** And the... And the... You know, internally, we used to talk about the next bench phenomenon that you would see what the engineers needed on the next bench and then develop a tool. On the next bench and then... A tool to support that, so... That's crazy.

**Dave Jones:** I think our time's almost up. Yep. Yeah.

**Chris Gammell:** I think so, too. But I think we could probably keep going for another, what, three hours, four hours. As usually. I've got more woodchuck here.

**Bob Davidson:** I think I'm going in all evening.

**Dave Jones:** I had to ask what this woodchuck thing was. I had no idea. Before the show.

**Bob Davidson:** It's hard cider from Vermont. Delicious, delicious cider. And it's got a woodchuck on the front of it. Yep.

**Dave Jones:** I don't even think you could buy cider here. I don't... They have apples. I don't... Well, you probably can, but... You don't hear of anyone drinking cider here. Do you have apples?

**Bob Davidson:** Yeah. They probably have cider. They may make apple juice and they probably get cider eventually. Yeah, exactly.

**Dave Jones:** Well, yeah. Well, you buy apple juice, yeah.

**Chris Gammell:** Some parent leaves it in a sippy cup too long and then they think, well, we should keep doing this.

**Bob Davidson:** Just leave it under the sink there for a while. Yeah, there you go. Right, okay. Don't put it back in the fridge and... Yep.

**Chris Gammell:** Thanks so much for being on the show. I mean... Absolutely. We'd love to have you back on sometime and hear more about what you're doing and...

**Dave Jones:** And where can we find you? Where can we follow you?

**Bob Davidson:** Oh, well, I'm...

**Dave Jones:** People want to see more hoodie HP photos.

**Bob Davidson:** Oh, well, those are kept in the archive, but... Bring it out! I'd love to see this. But I'm...

**Bob Davidson:** W-A-7-I-U-T on Twitter. That's my ham radio call sign. And then... W-W-W-A ambient sensor is all one word dot com. So...

**Chris Gammell:** Lots of good projects and blog posts and stuff on there. And you said you're getting back into...

**Bob Davidson:** I'm getting back into doing that, yeah. I am.

**Dave Jones:** Awesome. Thanks, Bob.

**Chris Gammell:** And we'll see everyone next week.

**Dave Jones:** Catch you later, Bob.

**Bob Davidson:** Okay. Take care.

**Bob Davidson:** We'll see you next time.
