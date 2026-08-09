---
episode: 388
title: An Interview with Earl Sharpe and Collin Kidder
url: https://theamphour.com/388-an-interview-with-earl-sharpe-and-collin-kidder/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released April 15th, 2018. Episode 388. An interview with Earl Sharp and Colin Kidder. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics. I'm Earl Sharp of Makina.

**Colin Kidder:** I'm Colin Kidder of Makina.

**Chris Gammell:** Welcome, guys. How are you doing? Doing great, Chris. Glad to be here with you.

**Dave Jones:** Yeah, so let's start right at the top. What is Makina? Well, I mean, I guess, you know, Makina, the company, is just a company that develops products mostly for the automotive industry. Now, the hardware that we're probably going to talk about today is an automotive interface for, you know, interfacing with cars and building stuff.

**Chris Gammell:** Okay, so does that mean that both of you are officially car hackers? Colin. Do you identify as car hackers? Do you have it on your business cards?

**Colin Kidder:** Colin more than me, but I suppose so. Okay. Yeah, I do actually have that on my LinkedIn.

**Chris Gammell:** Oh, there we go.

**Colin Kidder:** So technically, yes, it does say car hacker on there.

**Chris Gammell:** Okay, and so how do... Well, we'll get back to Earl and what you would define yourself as, but what is a car hacker, and why would someone do car hacking these days?

**Colin Kidder:** Well, for me, I actually come at it from a somewhat different perspective from the other Makina guys. I started doing electric vehicles, and what I mostly do for hacking is we take OEM components out of wrecked electric cars or electric car companies that went bankrupt, take their excess inventory, and try to reverse engineer how that stuff works so that we can make DIY hobbyist cars with the components out of OEM vehicles.

**Chris Gammell:** Nice. Okay. And so that's... Does that mean that this is kind of a closed... Like, cars are kind of a closed ecosystem? Is that kind of the baseline assumption here?

**Colin Kidder:** Yeah. Cars have historically not been very open, and electric car companies aren't really much more open than the standard car companies. So when we get these components, there's really no information to speak of about how to interface with them properly.

**Chris Gammell:** Great. Yeah. That's... I mean, that... At least the small amount I've heard, and you will probably hear, and the audience will also hear, my lack of knowledge about car stuff, it does seem like it's not... It's not like there's tons and tons of info out there. It's not like Ford is begging you to open up your car computer and start tinkering with that part. So... Earl, how do you define yourself, then, if you're not a car hacker?

**Dave Jones:** Well, I mean, I am to a degree. Colin... Not the master that Colin is, but... Uh-huh. Okay. You know, at this point in time, my role is mostly enabling, you know, people to do that sort of, you know, awesome work. But still, you know, my life revolves around cars in general, so...

**Chris Gammell:** And so, like, day-to-day, I think I've seen pictures, at least of you, Earl, in front of cars. I mean, like, how much are you guys hands-on with vehicles every day? Is it something where you're doing mechanical things, and then you plug in, you know, something that OBD2 and use that as diagnostic, or is it more detached than that?

**Dave Jones:** I mean, I, you know, for at least for me, it changes week to week. And a lot of times, we're just working on a benchtop or, you know, doing the normal hardware development process that you're probably all too familiar with. But, yeah, you know, we definitely do get dirty and play with cars, you know, pretty frequently.

**Chris Gammell:** Yeah, I guess, yeah, what is your car background? I guess, Colin, you kind of talked about turning apart EVs, but, like, you know, growing up in a garage kind of thing, or what's your hands-on background there?

**Dave Jones:** Yeah, no, I literally did grow up in a garage. My father owned a garage for 40 years, and throughout high school, you know, I was working there.

**Chris Gammell:** Nice. So, like, straight up, like, car talk style, huh? Yeah, I guess so. That's about the closest that I've gotten to cars, is listening to car talk on a regular basis. Which I still do, you know, rest in peace to that, buddy. You know, like, yeah. Okay, cool. Well, so, what about the interface then? So, I guess I'm kind of jumping around here, but I at least know the OBD2 is the pathway into the car's computer and all the buses and stuff like that, but, like, why... You said you're enabling people, or, like, well, I guess both of you are, but, like, why do people need to use that on a daily basis for car hacking or otherwise?

**Dave Jones:** You know, I mean, I should also clarify that Machina, you know, we have sort of a dual purpose of, you know, helping hobbyists, but also helping companies. So, a lot of, you know, what the companies are using it for is to, you know, prototype, you know, a product or, you know, really early prototyping. They might be using M2, which is kind of why we built it, right? Because it is so, you know, it's common to a lot of cars, so it definitely can be used for prototyping lots of different ideas. I guess that's the simple answer.

**Chris Gammell:** Okay. All right. So, when you say you're selling it to companies then, so, like, so a manufacturer of other stuff that's hooking into one of the buses would use this as a peripheral just to kind of see what's going on there, or what?

**Dave Jones:** Yeah. I mean, the number of stuff that it can be used for and is used for is pretty incredible. You know, I mean, the OBD2 port is used from simple things like, you know, people monitoring, you know, really simple stuff with diagnostics to really complicated things where companies are, you know, reflashing the ECU over the OBD2 port. So, you know, depending on the company, it really varies what they're trying to accomplish, and it's very similar with the hobbyists as well, you know.

**Chris Gammell:** Well, so let's walk through some of the early stuff then. So, the OBD2, what do people usually expect to see there, right? So, if someone used the M2, which is the Machina product, like, what's actually, what do you get access to when you use that?

**Colin Kidder:** A lot of what you get access to, OBD2 obviously kind of predates these modern cars. OBD2 has been around since 1996, and a lot of what it was meant for is for emissions testing. So, in the past, what people expected to find on the OBD2 port would be diagnostic information about the engine for emissions purposes. You could see the engine temperature, timing advance, the mass airflow sensor readings, and things like that. So, partly it's used as one of the test aids for emissions certification on cars. And even people say, you wouldn't want to probably do emissions testing on your own car, but even that same type of info could be interesting to people. Maybe you want to know how hot your engine's currently running, and your dash only has a needle that has sometimes no temperature readings at all on it. Well, the OBD2 port will say the engine's currently 180 degrees Fahrenheit, and that gives you the info you were looking for. So, a lot of the readings that you find on it are all primarily engine performance related.

**Chris Gammell:** I guess maybe for the beginners, more than beginner, even Chris the beginner, where is this usually located on a car?

**Dave Jones:** So, it's usually, you know, left knee area of the driver. Okay.

**Chris Gammell:** And so, like an access door, or is it just kind of exposed?

**Dave Jones:** It can go either way. I feel like it's, I don't know, what do you think, Colin, but it feels like it's more often just exposed.

**Colin Kidder:** It's usually exposed. I have seen it be under trap doors.

**Chris Gammell:** Mm-hmm.

**Colin Kidder:** Yeah. Normally, it's still going to be in the same basic spot. I think it's, there's a standard for where it has to be. It's something like within a foot of the driver or six inches of the driver or something like that. So, it's always in a pretty common spot.

**Dave Jones:** Yeah. I mean, sometimes it does take a few minutes to find them. It's always kind of funny.

**Chris Gammell:** But it's not going to be in the, it's not going to be like in the roof or behind the driver's seat or anything like that. No. No.

**Colin Kidder:** But it is mandated.

**Chris Gammell:** Good, good. It's good to know. And it's about what, like 15 centimeters across or so, a couple centimeters high. Like, it's not, it's not huge, right? I mean, like, inch or two across. The, the standardized port, it kind of looks like a, kind of reminds me like a Molex port or Molex header.

**Colin Kidder:** Yeah, kind of. It, it is sort of like, like the old, uh, it almost looks like the old printer style port. So, you plug into like the dot matrix printer from the 80s.

**Chris Gammell:** Oh, yeah. That's the, uh, that's the HPad, right?

**Speaker ?:** Maybe I'm kind of showing

**Chris Gammell:** my age there, but. Yeah, no, no, no. That's what, that's what's used on test equipment too. The really old ones is like that, yeah. Yeah.

**Colin Kidder:** But it's kind of about that size.

**Chris Gammell:** Yeah. Okay. Yeah, it is, it's, it's, it's hardened to say is, you know, for car, car stuff always feels like it, it has that kind of extra layer of, of needs to survive in all, all climates and such. So, even, even the test gear. So, um, okay. So, down by your left knee. Um, it's interesting that you say, you know, when you're talking about what's actually coming out on it, uh, what, what are some of the protocols that you might see when you're like plugging into this? Like, is it, is it something where could, could I go and take a scope or a DMM and just, you know, probe on, onto this port or what?

**Colin Kidder:** No, it's, it's all, well, there's a couple of different standards. Modern cars, uh, I believe since about 2009, it's mandated that they use CAN bus for the communications. If you put a, an oscilloscope on that, all you're going to see is, you know, uh, ones and zeros basically, just, uh, digital signal that looks like nonsense. Uh-huh. Uh, in the past they used some other standards but they're all still pretty similar where they're, they're more, you can kind of think of it like a serial port where it's a set type of, uh, communications bus and it has data flowing over it in a specific format but it's not something that you could just look at within a oscilloscope and figure out. It's, it's all kind of encoded a special way.

**Dave Jones:** I mean, there's like what, there's a few physical layers, you know, and, and the one CAN bus uses is very common but there's other ones and, uh, you know, we, we tried to with the M2 hardware to cover a lot of them. So, you know, K-Line, L-Line, Lin, and, um, you know, some of the old J-250 that sort of stuff. I've never heard those before. K-Line, L-Line? I mean, yeah, they're just, uh, there are other protocols, you know, you're frequently finding in cars. Some of them are not really being used anymore. You know, you don't really see J-1850 and stuff like that but you'll still see a lot of Lin in cars. Uh-huh. And, you know, I think Lin gets used in other, in other stuff, right? So maybe you know that one.

**Colin Kidder:** Yeah, I would say Lin is mostly used in cars but, uh, I think that it might get used sometimes in, say, audio applications and such too.

**Chris Gammell:** I still remember the first time, so like, you know, like I said, I never grew up using cars, you know, playing with cars or working on cars or anything like that but I remember the first time, I think it was a Freescale rep, so back when Freescale was still Freescale, um, they come in to where I was working and, you know, it was someone talking about processors and they're like, well, like, tell me what your specs are, what do you need? You need, like, you need, like, can bus and I'm, like, looking at them and I'm like, I have no idea what words you're saying right now. Like, and it, obviously, now I know that there's transceivers that are built into some microcontrollers and, well, it's probably, it's probably the Mac, not even the actual file error, right? So it's, but, uh, but I, I just, I was just like staring at them like, I don't think I need that. Yeah, I mean, Freescale world, that's, there's a ton of them, right? Like, there's tons of Freescale parts in cars, right?

**Colin Kidder:** Yes, there are. Yeah, Freescale is pretty common and, yeah, CAN wasn't common, I wouldn't say, until pretty recently. Like I said, it, it was mandated in cars only starting in 2009, so we're only going on nine years of cars definitely having CAN.

**Chris Gammell:** So you, you're saying CAN at all, like, and using it as a standard bus at all.

**Colin Kidder:** Yeah, well, CAN was, I think it was 06. developed by Bosch in 1985.

**Chris Gammell:** Okay.

**Colin Kidder:** And it was used in engine control units from Bosch starting in about 86.

**Chris Gammell:** Okay.

**Colin Kidder:** So, if you're driving around a 1990 Mercedes, it probably has CAN bus controlled ECUs in it, but it didn't, the, the big three OEM car makers in the US didn't necessarily follow suit quite so quickly. so CAN, it has not been very common until recently in, in American cars.

**Dave Jones:** Interesting. Okay. And there's, there's a couple types of CAN, right? There's like CAN FD and, you know, 2.0 is the most common.

**Colin Kidder:** CAN FD is pretty much a unicorn at this point. It technically exists, but no one has ever actually seen it used anywhere.

**Chris Gammell:** What does the, what does the FD stand for? Flexible data rate or something?

**Colin Kidder:** A normal CAN runs at a single speed. So you'll hear a lot of times say 250 kilobit bus or a 500 kilobit bus for CAN. It's pretty standard. Okay. The CAN FD has flexible data rates. So it can start out sending at say 500 kilobits. And then when it starts transmitting actual data and not just metadata, it can kick up to 8 megabits per second. So it's far faster in the data portion and it supports a lot larger payloads. So it's used, it's going to be used at any rate for ECU flashing in a car where the extra speed might be handy if you have to flash say a 2 megabyte ECU flash file, then you kind of appreciate the much faster speed.

**Chris Gammell:** Right. Yeah. I can imagine trying to dump diagnostic data if you're streaming data back too, that would, seems like it would be a little bit more useful if you had a ton of data coming over it. but, so what about the actual physical, so people that don't know CAN, I remember when I was learning RS-485, they told me that it was pretty similar in the method except it's not differential, it's single-ended, right, for CAN?

**Colin Kidder:** Oh no, CAN is actually differential, there's a couple of different CAN standards, there is single-wire CAN, which is single-ended, and single-wire CAN is basically just one wire from the differential CAN, and you basically don't use the other wire, so it's the same basic thing, just with less wires.

**Chris Gammell:** So, then I remember, I also remember, where did I learn this, this must have been like at a talk I was at, I think it was, I think, or no, maybe it was when Rick was on the show, so Rick was on the show a couple, and I'm forgetting, blanking on Rick's last name, but he was talking about some car timing stuff as well, and it was either him or maybe one of the prior guests to that, but anyways, CAN and Lynn, it seemed like CAN was like the important engine type stuff, Lynn's stuff was like window control, is that a consistent statement in your minds?

**Colin Kidder:** Yeah, that would be accurate. Lynn is much, much slower than CAN. I was mentioning how CAN, the standard data rates in a car would be 250 kilobits per second or 500 kilobits per second. Lynn is, I think, 19.2 kilobits per second, so it's way slower.

**Chris Gammell:** So why do they use it then?

**Colin Kidder:** It's cheaper. CAN requires a transceiver, and the transceiver chip, even for an OEM, might be 50 cents. whereas Lynn might cost basically nothing to add to their items. Got it. So especially for cheap stuff like a window regulator, they don't want to pay the extra, you know, 50 cents or a dollar premium to go to CAN for a window regulator. So they go to Lynn, which is very cheap, and can basically be implemented on a processor with no transceivers, and just use the processor's serial capabilities.

**Chris Gammell:** So it's basically free to use it. So are both of those actually exposed then on the OBD-II? Like, is this something that the M2 would actually start talking to through that interface?

**Dave Jones:** Well, I don't think Lynn has to be on the OBD-II. I mean, Colin, can you confirm that?

**Colin Kidder:** There's only, the OBD-II standard really only requires that you have one primary means of connecting to the diagnostic data. So, in modern cars, that's CAN, and the older cars, that would have been K-Line or the J-1850, but that's the only thing that has to be on there. So, everything else is not really standardized. There could be Lynn, there might not be. It just depends on what the car company wanted to do. Quite often, the OBD-II port is kind of there for the OEM service center too. If you take your car to your local GM dealer and the windows don't work, they might have Lynn on the OBD-II port just so that the technician at the service center can get at the Lynn data easier. That would be the only reason it would be there, but it's not standardized as being there.

**Chris Gammell:** I remember going to the, you know, you always cringed when the mechanic says they have to plug in the computer. It's like, oh, crap. And they charge you for that too. Okay. So, and this is an interesting point to me as well, is that, so it seems like there's tons of processing in cars these days. I don't think that's a surprise to anyone. However, it's not like you plug in the OBD-II and you just get control of the car, right? No. It feels like it's more like it's a mailbox where it's spitting out results from whatever they want to show you.

**Colin Kidder:** There's a variety of ways. Some car manufacturers basically have a dedicated line from the OBD-II port to one ECU in the car, and that ECU answers the diagnostics related questions that you're asking it, and that's the only traffic that you get. So, if you ask, what's the current engine RPMs, it will spit back, oh, the engine RPMs are 2,000 RPMs right now. But there's no traffic to speak of unless you ask it a question. Other cars basically have the whole engine control bus right on the OBD-II port, and you practically could send fake data and make it think that the mass airflow sensor is reading a different value than it is or that the transmission's in a different gear than it really is. So, it really depends on the car. Some car makers are more paranoid, you might say, than others about data security.

**Dave Jones:** Yeah, and that's kind of why we, you know, it's not all about OBD-II, it's also why we make that what we call the under-the-hood version, where, you know, you just kind of tap into the bus wherever you can, you know, gain access, and, you know, other cars are getting, you know, like Colin described, that situation, and, you know, gateways and things like that are making the OBD-II port, you know, increasingly locked down, so people are having to, you know, find other ways in.

**Chris Gammell:** Okay, so maybe, maybe, can you guys walk us through, can you just tell us how every car works? I know that's going to be a terrible, that's not actually what I'm asking, but it seems like there's a ton of computers in there, it seems like the ECU is the main brain of the engine at least, but is there like a, like, what is the usual architecture within, like, who's in charge underneath there, under the hood? Well,

**Colin Kidder:** the engine ECU is in charge under the hood, it's, you know, reading all of those sensors and calculating the correct spark advance and things, basically everything is paying attention to the ECU, quite often the sensors are not connected via a can or anything, the ECU will have dedicated wires for that, so you can't really screw it up too badly, and the ECUs are,

**Chris Gammell:** you said engine ECU, so is ECU not engine control unit?

**Colin Kidder:** Well, it is, yeah, it gets to be where if you just say engine CU, it sounds weird, but yeah, the correct term would be ECU because that's engine control unit.

**Chris Gammell:** Okay.

**Colin Kidder:** There's, in a car, there's usually two main control units, you have the ECU, the engine control unit, that's responsible for making sure that the engine performance is within specifications, and then the BCU, the body control unit, will be in charge of things like making sure that the door locks are working when you push the buttons, making sure the windows go up and down, you can adjust the seats, basically all the other stuff in the car that's not engine related.

**Chris Gammell:** So there's not like, there's not like one main supervisor then, so is that because the ECU needs to be more tightly coupled or like why?

**Colin Kidder:** The ECU is obviously pretty, it's pretty important that that not fault, so they don't want that to be responsible for anything that doesn't, that it doesn't have to be because it's pretty important that your engine, you know, run reliably, you don't want, especially on some newer engines have variable valve timing and some pretty critical parameters. If the ECU goes out to lunch and sticks your valves open, that's not going to make you a happy person. Right. So the ECU is very robust. A lot of times they have multiple processors in there that are all running in lockstep checking each other. It's pretty hard to make the ECU do the wrong thing because the car companies are very paranoid that the ECU keep running. A lot of times they've got, you know, like a hundred thousand mile engine warranty. You don't want the ECU to blow your engine up at sixty thousand miles and they owe you a new one.

**Chris Gammell:** Right.

**Colin Kidder:** Okay. So they kind of keep, it's kind of compartmentalized that way where the body control unit will take care of the non-mission critical things and the ECU might take care of the more mission critical things. And you may even have some other mission critical ECUs or if you want to call them all ECU in a way, you might have some other mission critical computer systems like the ABS is probably its own computer system because it's pretty important that your brakes work properly too. Things like that.

**Chris Gammell:** I guess I'm just surprised that there's not, I don't know what I'm expecting here, but I guess I'm surprised there's not like some, I guess what I'm thinking of is it sounds like the ECU is akin to a microcontroller or an FPGA where it's really, really in the weeds and really fast timing, fast response, just control loop kind of stuff. And then it seems like, like you said, ABS is another one in that vein of tight control, whatever. I guess I'm surprised there's not like the equivalent of like a Linux level supervisor running in the dash or something like that, you know, just saying, here's, I mean, I guess, well, there's probably some stuff up there, but I always assume that the higher level stuff would be in control in that case, but maybe the human is that computer? I don't know.

**Colin Kidder:** They kind of, actually in a Tesla, you'd almost be right. The Tesla Model S, that big 17-inch center display has a computer back inside of it, and that computer is the central brain box of the whole car and really does control everything else. You know, the drivetrain is controlled by the center computer, the ABS is controlled by the center computer. So in a Tesla, that is literally the case, where there is one computer where basically all of the communications networks terminate in that one central place. Not necessarily like that in every other car. I mean, there's usually going to be one system that's kind of responsible, maybe the body control module kind of oversees everything else, but you've got a lot of autonomy too. If you're driving down the road and the body control module blows up, the ABS module is still going to keep working trying to make sure that your brakes work right, and the ECU is still going to keep working trying to make sure your engine works right.

**Chris Gammell:** So it's just about interoperability between all these things.

**Colin Kidder:** It's kind of a redundancy thing. You don't want one thing to be able to brake and destroy the car. They all kind of run in their own separate domains.

**Chris Gammell:** I mean, the feeling I'm getting, at least from this initial conversation, is that there's not much standardization either, at least between manufacturers. I'm sure within manufacturers there are, but...

**Colin Kidder:** Yeah, I wouldn't say there's a whole lot of standardization. I mean, no one wants to completely reinvent the wheel, so the way that one company did it is going to be pretty similar to the way the next company comes through and does it, but you can't necessarily say that any one that, you know, that Ford is going to do things the same way the GM does. They just don't. There's different ways of doing things, different ways of routing the buses between every manufacturer.

**Dave Jones:** Yeah, I mean, I don't think they necessarily want standardization, you know? I mean, that data is worth a lot, and the complexity of getting it and building products for it and that sort of thing is certainly a value to the manufacturer, and they don't really want to give that up.

**Chris Gammell:** I mean, I guess the thing that I think about is smaller companies kind of have to do that, right? They have to be more standardized. Someone was telling me recently that they bought a cheapo router from China and it just had OpenWRT on it, and it was because that company was not even close to big enough to write their own firmware, whereas if you go to Netgear or someone, they're writing their own thing because they can and they feel they have to, right? And that's kind of what I feel like it's part of. It feels like there's a lot of historical stuff here that I'm missing, too. But just big companies doing big things kind of feels like the feeling here.

**Dave Jones:** Yeah, I mean, they're building themselves a little bit of a barrier to entry or a mode or something like that.

**Chris Gammell:** Yeah, right. But the downside sounds like that it's the... So now, as a third-party provider, you have to deal with every flavor that's out there, right?

**Colin Kidder:** Yeah, it is. It's almost mind-boggling sometimes when you try to get into that. As a small-time company, it is difficult to provide support for a wide range of vehicles for that very reason. Every vehicle is going to be different. And in fact, in terms of communications, like the way that the communications on say can work, the car companies feel free to switch that between model years, between models of cars. Oh, really? It makes it really tough. I mean, in the past, there was maybe a more robust DIY hobbyist type of system. You know, people would quite often try to put Ford motors into a Chrysler car, and it could be done because the motor was pretty much its own island, so to speak. But now that's a little harder because even though the ECU on, say, a Ford motor is mostly just controlling the Ford motor, it's still looking for communications with other stuff on the car. Say it might be looking for a message from the ABS or traction control module so that if the traction control module detects that you're slipping, it tells the ECU to not let you have any more torque than a certain limit. So that you quit slipping. So it's always looking for messages. Now that makes it really tough to put, say, a Ford motor into a Chrysler because all the messages are different. It would be like dropping an English speaker into China and expecting that you could get along fine.

**Chris Gammell:** Well, I mean, from what you're saying, though, too, it sounds like even year to year, I mean, like that part or systems aren't compatible even within the family of cars or trucks that you're talking about here because they might not have the same standards.

**Colin Kidder:** Yeah, they may not. I mean, it's not that they do that every single model year or anything, but...

**Chris Gammell:** But like families of model years, right?

**Colin Kidder:** Yeah, when you hear, like, let's say GM came out with this new vehicle and it's the second generation of that vehicle, that's pretty much an indication that probably they changed all the communications in there, too. I know for a fact that Tesla is pretty notorious for that because that's one of the areas where I have done the most work. Between model years or even sometimes for basically no reason at all, Tesla will just up and change things on the CAN bus. A message that used to mean one thing will now be gone and a different message took its place with a different format. So that can be kind of frustrating sometimes.

**Chris Gammell:** Well, I'm sure Tesla and maybe even the bigger companies now, I'm sure when people's stock options start to vest, they move on and then the new person has to prove themselves. So what better way than to mess with all the CAN bus messages, right?

**Colin Kidder:** Yeah, it could be.

**Chris Gammell:** Yes, right. Yeah. A little bit of churn, but definitely some job security. It's funny too, because we can make fun of the Tesla engineers. They're probably not allowed to come on here and talk to us. In fact, I know one and I even asked him on here. He's like, yeah, no way. Well, it sounds like the, so it sounds like people that even within companies then, I can imagine an engineer at Ford who has to, trying to talk to an ABS system from the ECU, you know, for some reason the documentation isn't there. It sounds like they have to, it sounds like within all this stuff, reverse engineering at the very least is baked in because you have to figure out what the hell is this new message that I'm seeing, right? It sounds like that's just a thing you have to deal with.

**Colin Kidder:** I mean, for us it is.

**Dave Jones:** When companies come to us and they want us to help them, you know, build hardware and whatnot too, we often end up having to help with the reverse engineering stuff or find someone that can help.

**Chris Gammell:** So what does that look like then? So like, so a company comes to you and says, we want to talk to this new module, blah, blah, blah. You're going to go and help them to do that. Where do you start? I mean, reverse engineering to me is like black magic, but where do you start specifically with cars?

**Dave Jones:** You know, it really comes down to the discipline and whether we're trying to do it with the sort of core team we have or find someone that, you know, maybe specializes in it. And there's so many different, you know, specialties within car hacking, I guess, that, you know, depending on what you're doing, you might be looking for, you know, someone specific.

**Chris Gammell:** So when you say specific, you mean someone that's on a certain model year or type of car or like Colin does EVs or is it, what is it?

**Dave Jones:** Yeah, exactly. I mean, I think it goes, you know, multiple ways. You know, Colin might be great at certain types of EVs. You know, other people might specialize in certain types of attacks and certain, you know, tactics for reverse engineering. I don't really think there's, we, you know, we're only a year old, so maybe we will kind of get into a better rhythm on that. But so far, you know, it's just kind of been doing whatever we can to make the job work. So far, the hardest part really has been, you know, acquiring cars that you can work on is pretty challenging too. And I hear that from pretty much everyone.

**Chris Gammell:** You mean like just because of the cost or because you, because you have to get access to

**Dave Jones:** certain parts of the car or what? Yeah, I mean, if, you know, if you're trying to, you know, you can build a product without necessarily having the car, but then as soon as you're trying to integrate it, you know, then you need to actually have, you know, at least a benchtop, you know, sort of kit or, you know, in a lot of cases, the whole car. There's not a whole lot of firms that sort of specialize in renting out, you know, cars to people that are then going to reverse engineer them.

**Chris Gammell:** Interesting. I guess I, I don't know what I expected here. I guess I didn't, I didn't realize that firms were doing this kind of thing in the first place. So, so maybe could you give us an idea of, I don't want any specifics because I'm sure that's sensitive, but like, like the type of a company, like give me an example company that would come to you. Is it like a, like an end product integrator? Is it like someone wants to make a new car seat cover or is it, what, who's coming to you? What kind of companies are coming to you?

**Dave Jones:** You know, I think it's, you know, small to medium. You know, a lot of them, a lot of them are kind of newer startups that are trying to, trying to accomplish something and, and raise money. We've been successful there a couple of times, which is, which is always fun to be involved in sort of a new company. Um, some of them are companies that are, um, they're established companies, but that division is sort of a startup. So they don't necessarily have a, a team built out around, you know, that function or, or maybe it just, you know, it doesn't make sense for them to, you know, build out a team, uh, around that. If it's going to be sort of a, a one-time thing or, you know, very, you know, infrequent. Um, but again, you know.

**Chris Gammell:** Are they making like end parts or are they making, uh, other things that, like, I guess I don't understand what these people are making. Are they making like new car stereos that need to talk to something or new engine timings things? I don't, I'm kind of lacking it, knowledge of what goes in cars.

**Dave Jones:** Um, you know, and it depends on the, uh, like I said at the beginning, you know, there's, there's the, the automotive range of aftermarket products is pretty incredible. So, you know, it might be something, you know, performancey or sort of, you know, creature comfort sort of thing. Um, you know, obviously, you know, uh, there's a big push into IOT these days. So, you know, um, a lot of the, you know, if we're looking at products like our M2 hardware, um, you know, automotive dongles and automotive interfaces, you know, a lot of that's going to be sort of, uh, you know, IOT, you know, make your, make your car smarter for, for whatever purpose it is. And, you know, and even inside of those IOT dongles, uh, you know, there's a ton of markets when you consider, uh, or, you know, a ton of different applications when you start to consider, um, you know, consumer as well as commercial, you know, uses for adding the internet.

**Chris Gammell:** Okay. So, yeah, I, I have seen some of that stuff in the past. Like, so one that I think about is like the, I want to know how many miles I've driven for business expense. Right. And so someone like that, so if I was going to make something like that, I want to know how many miles I drove for my business expense so I could track my work vehicle. I would come to you and I'd say, can you help me to decode the messages coming out of this OBT2 port? Is that kind of the idea?

**Dave Jones:** Yeah. I mean, and some of those, you know, the original ones are very simple. They kind of worked on the standardized data that I think Colin was talking about earlier. Definitely now with sort of second generation ones coming out, uh, you know, they're trying to push a little farther into the, uh, unstandardized stuff. Um, but you know, it's, you know, I don't know if we've necessarily mentioned this, but the, you know, the OBT2 port, you know, can, can read and you can also write to it. So, um, I mean, yeah. So like if someone's flashing an ECU, but you also see, you know, simpler functions where people are, uh, you know, trying to push commands back into the car. Um, you know, for example, I must, you know, talk to someone once a month that wants to start, um, that wants to build, uh, you know, a car sharing program. So they want to be able to, you know, remotely open the doors or remotely, you know, disable the car, you know, whatever is kind of involved in, in, um, what is the big one? Car to go and those sort of, you know, car sharing programs.

**Chris Gammell:** Yeah. Those are, those are actually great. I think. So, okay. So, so to, to use Colin's example from before, if, if it's like dropping someone who speaks English into China, you guys would be like the translators at that point. You'd be like helping people figure out how to navigate the language. Is that kind of the idea?

**Dave Jones:** Yeah. When we do it, I mean, we're wrapped up in a lot of hardware projects these days, but we're definitely getting more involved into that, into that side because, yeah, at first when we started, um, and we, we kind of wanted to stay sort of, you know, the hardware side product development. Um, but you know, we've sort of come to realize that, you know, it's a pretty niche skillset and we're going to have to do some of that sort of stuff.

**Chris Gammell:** Okay. Well, let's talk about the hardware. So, so what is the M2? I think we've, hopefully we've said, we've said it a couple of times. What actually is it?

**Dave Jones:** I mean, it's a, yeah, I think of it as a modular sort of automotive interface, you know, it's kind of a development platform really, you know, that we've got a processor board, an interface board, and then that socket on the top, which follows the XB standard so that people can, you know, you know, add whatever boards they want up there, whether it's a modem or GPS or, you know, all the different flavors of, of those boards that are out there, Bluetooth and Wi-Fi.

**Chris Gammell:** Um, yeah, those, uh, I saw the XB standard, it's pretty much like serial bus, pretty much, right? I mean, yeah.

**Dave Jones:** And it's at that 20 pin, uh, 20 pin socket that was started by Digi. It was another Minnesota company here. Um, yeah. Or popularized at least. Uh, very, you know, very popular in the industrial space for, for many different things. Um, probably because of that pseudo standard. Um, yeah. So, and that's why, that's why we picked it. Um, then on the processor board you're going to have, uh, we've got the SAM 3X from Atmel. And we went with that for that first, uh, processor board just, you know, because it, uh, kind of spans the spectrum, we thought, or at least pretty well. You know, um, beginners can use it because, um, it does work with the Arduino platform since it's, you know, what you find on the Arduino DUE. Um, but it's also, you know, it's one of their, or at the time at least was one of their faster chips. So it, you know, it could, it could keep up when the automotive, uh, um, market pretty well. And Colin already had a little experience with it. Um, then on the interface board, um, you know, we've, we've got all these interfaces we've been talking about so far and a couple of can bus, single wire can and Lynn and K line and J 1850 and probably missing a couple.

**Chris Gammell:** Oh, okay. So, so the modular piece you're saying is you, you actually, so you, you separate out of the processing from the, the, the, the physical layer stuff so that you could swap it in. You find a new card has that, that J line or the, the, uh, what's the one you said, the can, the can FD or some new unicorn thing, like you said. So you can just swap over to that.

**Dave Jones:** Yeah. I mean, certainly, uh, you know, our curtain processor couldn't do can FD, but, uh, uh, you know, as we roll out more processor boards, um, you know, we could, and we plan to, you know, make more interface boards that are compatible with all the new stuff that's out there as well. And, you know, uh, I think people have been talking about flex ray a bit on the forum. Um, certainly can FDs is, um, interesting. And there's a couple others that are, you know, popular. I mean, automotive ether is, is another one as well. Kind of, we all knew that was coming, I suppose.

**Chris Gammell:** Um, I suppose so. Yeah. Eventually they'll put a ethernet jack on everything before it's wireless, right? And it, well, you've already got wireless. Yeah. Yeah. So why, why didn't this exist before, I guess? I mean, it seems like you said it's only 2009 since a lot of stuff had CanBus on it with OBD2. Uh, why, why isn't this already out there?

**Dave Jones:** I mean, I think, you know, there to, to a degree it, it was out there, you know, there's, um, there was definitely some Arduino boards that had, you know, CanBus. Um, I think Colin, didn't you write a CanBus library for the Due? Anyway, um, you know, there's, you know, there, you know, there was to a degree, uh, other things that were doing, you know, lots of the, lots of these pieces, um, you know, and then when you look at industrial tools or, you know, professional type stuff, there's, there's tons of stuff, um, certainly more expensive, but, um, you know, that's, that's what people were using, um, and still are.

**Chris Gammell:** Okay. So it's more about accessibility and getting it in the hands of

**Dave Jones:** making it more people and making it a commodity really. Yeah.

**Chris Gammell:** So, uh, why, I, so I guess, you know, to, to follow my line of why questioning, why not, why not higher level? I mean, is it, is it super timing sensitive that you need to have it embedded? You need to have like tighter loops. Why not do a, a Beagle in Black or Raspberry Pi or something?

**Dave Jones:** Um, you know, I mean, there's certainly lots of car hacks that do, do utilize those, those things. Uh, you know, I mean, making it compact is, is one thing. Um, and you know, we are planning on kind of, uh, we've been working on a little project. We're trying to be, you know, more open with the stuff we're working on these days. Um, we made a breakout board so that you could kind of, you know, replace the processor board with a pocket Beagle, which we're all pretty, pretty excited about. Yeah. Um, yep. So, you know, that'll, that'll definitely kind of, you know, give you a lot of, uh, the functionality that you would get with, you know, the Beagle Bone Black and, and a can,

**Chris Gammell:** can cape. Yeah. So I guess, and maybe this is a question for Colin then. So I don't quite understand. Okay. So now we have this board, we have the M2, it's plugged in. Then what? I mean, like maybe I'm asking higher level or higher power boards, but like maybe it's not necessary. Like, is it just logging the existing data or what, what are you actually,

**Dave Jones:** what are you doing? Yeah. I mean, I, you know, I think we're taking part in the conversation with the car, I guess. Um, you know, so that's, there's a, there's a set standard for, for how you communicate with it. Right. And that's kind of what Colin was describing earlier.

**Chris Gammell:** But yeah, maybe, maybe it would be a good to just get an example of what someone would do with this kind of thing. Oh, I see. is it, yeah. So like, so you plug it in and you're like, I'm going to, I guess you said read the engine temperature. That's like one thing, but yeah. What else, what else, what

**Dave Jones:** else would someone do with this? Well, so there's the, there's what you get automatically, you know, the sort of stuff you can find on, on Wikipedia or all over the web, you know, it'll tell you what different IDs that are standardized will do. Um, that's the, you know, Elm 327 type stuff. Maybe you've run into one of those. Um, it's kind of what the, the China, the cheap, like Chinese, you know, $10, uh, dongles and the apps like Torque. That's kind of what they utilize is that, that known set of information. Um, okay. Colin actually developed, um, a really cool program that would kind of be the next step. It's called Savvy Can. And this helps you sort of pick apart and reverse engineer, you know, basically a data log from the car and, and try to, you know, figure out what those, um, what the unknown IDs are, are up to. Um, so that's, you know, that's generally where we go next.

**Chris Gammell:** Kind of sounds like, like a Wireshark kind of style of things, really classifying, like you said, you're classifying different messages and then you're pulling the payloads out of them. Is that kind of the idea?

**Colin Kidder:** Yeah, more or less. Uh, it is on can messages are sent. Uh, the metadata is mostly an ID. When you see a message on can, it'll have an ID, uh, from zero to 2047. So there's about 2048 different message IDs on standard can. And when they, when you see a message, usually it's keyed to that ID. And in a certain car, that ID means something. Uh, for instance, on a Tesla, ID 15 is the steering angle returned from the steering controller. So if a message with an ID of E comes across the wire, you know that the data is going to be steering angle. And on can, you can have zero to eight bytes of data on each message. So on Tesla, most messages are eight bytes, whether they have to be or not. And the steering angle is returned, uh, with two different scaling factors in that message. So you know that E or 15 or E in hexadecimal means steering angle. But if you have a whole bunch of messages flowing across the wire, you don't know what they mean yet. So, uh, the program that I wrote Savvy Can is kind of meant to try to help you with that. If you see say message 137 comes across lots of times, Savvy Can would let you look at the data bytes that are, that are in subsequent messages as it's being sent and try to see what they do. Do the bytes seem to form a signal that looks like RPMs? Does it form a signal that looks like it could be the engine temperature? You know, you're kind of looking at what, what do the data bytes look like? What could they mean? You're trying to categorize. Do you ever, do you ever just put

**Chris Gammell:** them up on screen, like as like a chart and then go press every button? Is that like something you do sometimes?

**Colin Kidder:** Kind of. Yeah. Sometimes one of the things that we'll do for reverse engineering, let's say that we do want to know engine RPMs and you want to find the message that does it. What we'll do is start recording traffic and then you have somebody mash down on the accelerator, say two or three good times and get it up to 4,500 RPMs. Now you go back to the data and start graphing the different data bytes on different IDs that you saw and see if anything looks like it's got big swoops that seem to match the pattern that you hit the accelerator in. So kind of do it that way, partially visually, trying to determine what message could be the data we're looking for.

**Dave Jones:** The fun thing to do is to start playing things back and see, see what lights up, right? Turn into a Christmas tree. Like play, like actually writing back to the ECU or what?

**Colin Kidder:** Yeah, or let's say that you think that you found the engine RPM message. A fun thing to do might be to start sending your own message and see if the dashboard switches position to match the messages you're sending. You know, if you think that you've determined the correct way to format RPM messages, you might try to set the RPMs to 7,000 RPMs and see if the dash says that, even when the engine's idling at 900. Yeah. So you can kind of check yourself that way. Okay.

**Chris Gammell:** Yeah, that's a great idea. So I guess, how much is this like you're storing and capturing and then you have to play it back or how much is it just streaming? Is it just there's too much data to stream it all out?

**Colin Kidder:** Uh, there's a lot of times Canbus messages will be sent about every 10 milliseconds. Sometimes there's a hundred. So you might have a hundred messages a second flowing for a specific signal. That is a lot if you were just trying to stream it out and look at it as it's streaming by. Uh, but so, but we do that sometimes there is the capability in my software and in other people's software to sometimes just look at data flowing over the wire as it's going and just stream it past and see if you see anything, uh, that looks suspicious, you might say, or that looks like what you're looking for. But we kind of do it both ways. Sometimes you might look at the data in a streaming situation and sometimes you might store it. But the nice thing about Can is 500 kilobits is still only about 50 kilobytes. So there isn't the whole traffic on the bus might be 50 kilobytes a second. It's, you could store hours of data and not take up any hard drive space.

**Chris Gammell:** It seems like there would be a lot of data from coming from a car in general. So why isn't there more, I guess? Is it just a limitation of the Can bus?

**Colin Kidder:** Yeah, the, the Can bus is able to send on 500 kilobit bus, you can send about 4,700 messages per second.

**Chris Gammell:** Okay.

**Colin Kidder:** So that sounds like a lot of traffic, but that's everything on that bus has to share those same, uh, time slices, if you will. You can only send that much traffic. So if you had 10 things on the bus, they could only send 470 messages per second each before they saturate the bus out. Right.

**Chris Gammell:** So again, I guess this comes back to my question of who's actually in charge of saying, you know, sensor one, you can only send 10 messages per second or sensor two, you can only send a hundred messages per second.

**Colin Kidder:** Nobody basically.

**Chris Gammell:** So does it over get overloaded?

**Colin Kidder:** Yeah. The, well, the car, the, the, the people who designed the car know the limitations of the bus. And so, you know, a sensor that's on that bus will only try to send so many messages per second. Usually they're, everything on the bus is usually sending in a time loop. You might say where a sensor might send every 100 milliseconds and it's never going to send its status messages faster than that. It's, it's timed with a timer. And every time the timer ticks off a hundred milliseconds, you send a message. So for the most part, the, the car knows how many messages per second it's liable to see because everything's timed. And usually they use far less than a hundred percent bus load. Normally in a car, you see about 1800 messages per second on a bus that can do 4,700. So you're, they're, they're trying to shoot for under 50% bus utilization for times when say an emergency happens or when you're sending the diagnostic requests, all that stuff can be on top of the 1800. And as long as you don't get crazy, it would take quite a bit of, of extra traffic to go from 1800 to 4,700 and saturate everything.

**Chris Gammell:** You know, this is all starting to sound very similar to my, my distributed control system days. Like it sounds like, like specifically in the same way that I was assumed that temperature sensors would update like a thousand times a second, but it's like, no, well, you only didn't know the temperature every, you know, second or 10 seconds. So you just, you just turn that down manually, manually when you're designing the whole system itself.

**Colin Kidder:** Yeah. It's more of a system design perspective at that point where the bus doesn't get overloaded because when they designed the system, they knew what the bus limitations were and they know certain sensors, you know, ABS probably does send every 10 milliseconds. So it's a hundred times a second you're updating ABS stuff because that's important. But RPMs might only send every 100 milliseconds because 10 RPM updates per second is more than plenty. Right. And they know that ahead of time.

**Chris Gammell:** Yeah. Okay. And I guess this also brings up the question of what is actually being sent? Because I think it came up in the context of the, one of the times I was listening about car hacking and they were talking about what they, what you can control and what is actually coming back from all these computers. Right. So like what, what is the level of access that people have to the data that is actually on the bus and you know, the control they can exert over it?

**Colin Kidder:** Well, it's, it's a kind of complicated topic because in, in one respect, can sends messages with a certain ID and the IDs are associated with certain data. But the interesting part about can is that there's no actual concept at the low level of who is sending that data. Normally everybody has their own compartment and sensors only send messages that they were meant to send and ECUs only send messages they were meant to send, but there's nothing stopping someone from sending messages that somebody else on the bus was responsible for. Right.

**Chris Gammell:** You're like, we're just talking about that even where you said you could play back a message and say, Hey, I'm the, I'm the RPM sensor. Here's what the RPM is, right?

**Colin Kidder:** Yeah. There's nothing to stop you from doing that in can. Anybody can send any message at any time for any reason. The only thing that keeps the wild west under control is that the people who designed the car knew the, the, the design aspects and the domains for every piece of hardware and make sure that their hardware only sends the correct messages. It's, you know, it's their responsibility at that firmware level to make sure that each device is sending what it should, but the bus totally doesn't validate that anybody could send anything.

**Chris Gammell:** So are you saying that if I took an M2 and I plugged into someone's OBD2 port, I could, I could reenact that scene from, uh, uh, the Batman movie where like, uh, Danny DeVito is the penguin is, is driving the Batmobile remotely. Could I, could I do that? Cause that's been a dream of mine.

**Colin Kidder:** Not entirely. I mean, we, we have tried to do some, I've tried before to do some playback on a car where the existing messages are still there. A lot of times it just confuses the computers when they see the re the regular traffic is there. Now you're injecting traffic that says to do something different. So what the receiving end sees is do this, no do that, no do this, no do that, no do this back and forth so rapidly that it gets confused and says, well, which one do you want me to do?

**Chris Gammell:** Well, so like on the Tesla though, could you rip the steering wheel out and the sensor out and then just drive by wire like that? Is that, is that really?

**Colin Kidder:** Well, I don't remember if the Tesla, well, probably some of the newer ones, you actually could do that. Right. Uh, the older ones might, might not allow drive by wire, but the newer ones that are drive by wire, yes, you could pretty much unplug the EC or unplug the control unit for the steering sensor and play back anything you felt like and drive the car.

**Chris Gammell:** Y'all get, y'all get creeped out by that

**Dave Jones:** or? There's a couple of companies, right? Trying to do self-driving cars, you know, uh, yeah, you know, sort of with, with cars that weren't meant to, you know, weren't originally envisioned to be self-driving. Um, but I think like Colin was saying, there's, there's a lot of conflicting messages and they end up having to do a lot of filtering, right? Of, of the messages that they're, um, competing with.

**Colin Kidder:** Yeah. The, the only way to reliably override a control system in a car is to unplug that control system and then fake being the control system yourself.

**Chris Gammell:** Right. And having a good enough knowledge of what it's actually supposed to send. So you don't put in some weird corner case state, right?

**Colin Kidder:** You would have to virtually perfectly emulate a device that you don't have the firmware for. And that's, that's pretty tough to do.

**Chris Gammell:** Right. But at least the very least you could put a, the air gap between them, right? You could take the steering column off, plug it into an M2, transmit it over wifi, account for the delays, pull it back out, put it onto the can bus and then, you know, drive the thing, right? That's kind of the idea.

**Colin Kidder:** Now you could more or less do that. Why haven't you guys done that yet?

**Chris Gammell:** That's a, that's pretty crazy. I mean, like, it sounds like, especially like, especially because, you know, thinking about like the 1970s, like muscle car, like there is nothing electronic in there except for like headlights and like fuses and stuff like that. And like relays maybe, but man, everything is just controlled these days, huh?

**Colin Kidder:** Yeah. Basically everything is computer controlled in a modern car, which has its blessings and its curses. Like you said, it can be scary to think about, uh, cars are starting to come out now where the steering angle detector is literally, you have a steering wheel attached to nothing, just a sensor that, that tells you how far you spun the steering wheel. And it's a piece of electronics that's turning the actual wheels back and forth. Right. So you're kind of trusting your life to, uh, to that kind of electronic hardware.

**Dave Jones:** Yeah. It is kind of weird, you know, cars do, you know, I mean, we're very much so working on, uh, you know, cars that, that are putting this technology in. So I guess it's good for us, but it is a little weird when they kind of start to feel like iPhones and, you know, they get faults and they go into limp mode and stuff. And it's kind of annoying when that stuff starts to, starts to get in the way. Right. It's kind of annoying when you crash into brick walls with that too.

**Chris Gammell:** Yeah. Yeah. So, uh, so that, I mean, I guess you guys probably have clients that are doing this stuff, but whoo, uh, what, what are, is anything changing on the, on the canvas? I guess, I guess my mind always goes dark right away. Like, you know, I read these, these dystopian novels all the time and like, uh, yeah. Like, is there anything happening to encrypt canvas traffic or even just to verify that sensor A is talking to sensor B or sensor A is talking to ECU A kind of thing? Or is there any, is there anything in the

**Colin Kidder:** works for that? Well, I kind of glossed over this quite often on, on anything that's super critical, like steering position sensors. Uh, when they send, they send the data and usually it's not encrypted, but what they'll do is send one or two bytes in that message will be what I would call like a security or a checksum type bite. Okay. But they don't use, you know, like CRC five or CRC eight or anything, uh, that you could easily do yourself. They'll use some, they'll, they'll try to come up with as, as sneaky of a encoding scheme as possible for those security bytes that usually kind of encode the message that they sent. The other bytes will be turned into use, you know, they'll use special operations and then come up with a special security byte and the security byte or two is tacked onto the end of the message. Now, everything that's supposed to receive that message knows how to also calculate the security byte. Right. Exactly. And if it's not the correct one, it will ignore it.

**Chris Gammell:** Yeah. Yeah.

**Colin Kidder:** So there is, but then that's where replay

**Chris Gammell:** attacks come in as well, right? Because you could just, if it's not encoded, you could, you could just do a replay and, and try it again and be like, oh, well, I, you know, see, see what works and what doesn't work. Right.

**Colin Kidder:** Yeah. They try to, uh, stop you from that a little bit by, uh, putting counter bytes in there as well. So every message will have an incrementing counter byte and the counter byte is part of the security byte. So if you can't, you know, you can replay it then because the replay will have the correct counter and correct security byte. But if you don't know how to calculate the security byte, given the message and the counter byte, then it's just all that much harder to calculate the security byte because there's a constantly incrementing counter that's adding entropy, you might say. Sure. Into the data. So they try to mess you up that way, but

**Chris Gammell:** I mean, this sounds like it's like 20 years behind though. To be completely honest. I mean, this sounds like, like in terms of encoding, encryption, all that, it's not like they're encrypting stuff or anything. It's just, they're just adding some other obscurity.

**Dave Jones:** I mean, there definitely are a couple of startups that, you know, are trying to offer the OEMs, you know, encryption for their, even for their existing systems. I think, um, I'm not a hundred percent sure on this, but you know, I heard that the reason the car companies aren't biting is because they, you know, they're, they kind of can't because of legislation. Um, but. Oh, really? Interesting. And I'm not, I'm not a hundred percent sure on, on why they haven't.

**Chris Gammell:** I mean, I think, I think you'd run into the same thing that like, so like John Deere has that whole case against, well not case, but like there's a lot of pushback against them because they encrypt all the, all of their parts that have the, you know, they have to get verified and talk back to servers and stuff like that. And that really hurts farmers. I assume with all of the, the car shops that are out there as well, like same thing happens and people don't want to put in, you know, aftermarket parts.

**Dave Jones:** Right.

**Colin Kidder:** And I mean, you know, they, they most certainly the, the same thing. It's funny. You mentioned John Deere like that. Uh, go ahead and try once taking a, a transmission out of a wrecked Mercedes and put it into different Mercedes.

**Chris Gammell:** Oh really? Same thing?

**Colin Kidder:** You, you can't.

**Chris Gammell:** Wow.

**Colin Kidder:** They, they most certainly, uh, they do the same thing John Deere does. Uh, car companies will encode, especially parts that are most likely to be stolen, like motors, transmissions and things like that. They literally do have, it's not really an encryption per se necessarily, but they will have kind of like a, a startup sequence where when the transmission starts up and you go to start the car, the ECU. Right. It sounds like a challenge or something like challenge response. Yeah. Right. The, the ECU will send a challenge and if the transmission can't send the correct response back, the ECU will never ask it to go into gear. So you're stuck. Ooh.

**Dave Jones:** I mean, I was talking to a, a rebuilder the other day who, um, he rebuilds cars and he has to actually find someone to rebuild the original airbag because he hasn't been able to figure out how to, you know, make, um, how to get the car to recognize, you know, the, uh, the one it didn't come with.

**Chris Gammell:** If people don't know that, I think the reason is because the, they're worried about aftermarket components and losing their margin because a lot of these companies make money on the long-term supportive parts, right? That's like part of their, their business. Yeah. I think I heard Caterpillar only makes money on that

**Dave Jones:** basically.

**Chris Gammell:** Oh really? Like the, the, the machine itself is the loss leader on the parts service plan.

**Colin Kidder:** I think it's like that to some extent with cars even as well. They say that dealerships make all their money on, on service calls, which is part, part of the reason, you know, I'm mostly into electric vehicles. That's part of the reason for a slow uptake of electric vehicles because they don't break hardly ever. Right. Yep. The service center won't get any business. So the car, the dealerships are like, well, you know, we sell cars basically at cost. Why would I want to sell an electric car at cost when I'm not going to see this person for five years?

**Chris Gammell:** Yeah. I don't make money selling brake pads. Yeah. Huh. That's, it's, it's a crazy business for sure. And I mean like, and I feel, it feels like the same thing where the, the initial costs, the expectations for users as well, right? People, when they go to buy a car, especially an electric vehicle, like there's a lot more upfront costs, but people don't really think about that for the long-term support of the car. Right.

**Dave Jones:** Yeah. I mean, they're coming down even in price too. So maybe the upfronts are even sort of becoming comparable.

**Colin Kidder:** With electric vehicles, it is, they're more expensive upfront. You have less maintenance and, you know, gas is expensive. So to some extent over the life of the car, it depends on how long you want to keep it. But you know, with an electric car, filling it up is about $2 in electricity. Oh, wow. Whereas, you know, filling up a gas car could be $60.

**Chris Gammell:** Yeah.

**Colin Kidder:** So you, you, you save some money there, but still for quite a while, it still wasn't really much of a value proposition. You, you could spend $15,000 more buying an electric car and you weren't likely to spend $15,000 in gasoline.

**Speaker ?:** Right.

**Colin Kidder:** I mean, the other thing is right.

**Dave Jones:** So you, you, you end up spending a lot of money on batteries occasionally if you, if you keep it for say 20 years or something, at some point there's going to be some giant spike in, in spending.

**Chris Gammell:** So, all right. So let's go back to the M2 because this is, you know, this is like the platform it's all around building or is it, you know, it's a modular platform that you can use to get started. If someone was interested in just even just taking a peek at what's going on in their car, uh, what, and, oh, and I do know from our, our, our, uh, survey recently that like 60% of people are listening in the car right now. So pretty good audience for that stuff. Uh, what, how, how would they get started with the M2?

**Dave Jones:** The best way to start, you know, and I think most people do is kind of, you know, using Arduino and putting Collins Savvy can on there just to kind of see what's going on with your, with the can bus and just kind of get familiar with it. Um, you know, getting familiar with car hacking in general, I always, you know, suggest people pick up, um, you know, the, the car hacker's hand guide and, and check that out. I think that's a pretty good, you know, introduction to a pretty broad topic. Like we've, you know, started to go over here today.

**Chris Gammell:** Yeah, that's good. I think, uh, so, so, so maybe at the beginning they would just be monitoring what's going on, taking a look at messages and would you expect then that they would, you know, I guess they could use this stuff for tuning and what else, what else might they use it for in the end of the day?

**Dave Jones:** Yeah, I think at first you're, you're mostly logging data and just, you know, trying to understand how, you know, how your car works really. Um, certainly once you get a little bit more, uh, once you start to get some understanding there and you can, you know, take on some little projects, um, and try to think of like a really, you know, simple one. Um, you know, like the, the RPM is standard information and a lot of cars today don't come with an R with a, with a tachometer. So, you know, you could theoretically make your own or something like that. Okay. Um, but yeah, you know, I think that just, just logging the data and trying to, trying to figure it out is, is where a lot of people start. Um, and you know, your car being kind of unique, um, you know, there's definitely some, you know, you'll, you'll need to do some work as far as just kind of figuring out what's, what's special and going on in, in there, I guess. Um, but yeah, I mean, you know, there's, there's lots of little communities kind of spread around that are working on all sorts of different projects that you, you know, could get, could get involved in once you, you know, have some, some understanding around, around what you're, what you want to do really.

**Chris Gammell:** So it sounds like with, uh, like one of the M2 breakouts or something, you could maybe wire it to a secondary display that you could stick on your dashboard or something like that. Look at the temperature, look at the, look at the internals of your car without, uh, without retrofitting a huge new display or something. Yeah.

**Colin Kidder:** There's actually a kind of neat thing. I don't think I've actually seen anyone try with the M2 yet, but one of the things that people use on the OBD2 port is a heads up display because most cars don't come with one, but it's, it would be kind of neat.

**Chris Gammell:** Yeah.

**Colin Kidder:** You know, to take data that you wanted to see and display it up on your windshield. So, you know, you could kind of, given our, our example that we keep using of RPMs, let's say you don't have a tachometer, you could, you know, make your own little heads up display thing with an M2 and literally fire out a big graphic of the tachometer right onto your windshield as you're driving.

**Chris Gammell:** Yeah. Yeah. That's a cool idea. I've seen, I saw one like heads up display thing recently. It was like a, it was like a flip up reflective one, but I think it was just showing like directions or something. So it wasn't anything engine related.

**Dave Jones:** I mean, I was driving a Corvette the other day and that had a heads up display that you could kind of, you know, move around where you wanted it on the, on the windshield. Um, so they're, they're becoming more common. Uh, I think Nissan had one early 2000s or even late nineties or something, you know, just for your speed. It just kind of, you know, reflected off the dash basically with a mirror or something.

**Chris Gammell:** Um, I know we're kind of getting up there in time, but I feel like we have to do it after, after the last week too. Like we were talking about the, the self-driving cars and the, you know, the, a lot of the sensors and stuff. How, how does that change now? Like as people are doing more self-driving car stuff, does that impact what either of you were doing or, you know, does it change the nature of what's on the canvas or, or are those completely different systems?

**Dave Jones:** Well, I mean, I think, um, you know, it's going to, you know, there's going to be more, more worry about, you know, car security. Um, and certainly a lot of people that are doing, uh, car hacking are, uh, especially the people that are doing it for a living, you know, um, a lot of them are, you know, security experts that are trying to help OEMs, you know, close loopholes and stuff like that. Um, so I really think that it, you know, probably will make things more important as we, as we move towards, you know, trying to make the, uh, self-driving car and whatnot. And obviously that's got to be very secure to external threats. You know, there's probably going to be, you know, a lot of the, a lot of the same car out there, right. As people start, stop, uh, caring so much about, you know, brand and differentiation of cars and, and really just are kind of looking for the, you know, efficient transportation, you know, there's going to be a lot of, it might be come more standardization than we're experiencing today. So it's going to need to be very secure.

**Chris Gammell:** I don't know if Madison Avenue will ever let us not care about cars. That's what I, that's my response to that one. Cause I think that like, there's a lot of advertising dollars that are behind like, Oh, you are your car, you know?

**Dave Jones:** Yeah, no, I agree. Um, I think there'll always be brands and whatnot. Uh, I think Bob Lutz, you know, was it yesterday or something at, at SAE, he made the argument that, um, the brands will become sort of, you know, the Uber or the, uh, Lyft, you know, as they start to own and buy cars, they won't, you know, they won't want Mercedes branding on it. Um, but I agree. I don't think that Mercedes will ever, um, you know, completely disappear. They'll probably start, you know, competing services and that sort of thing. And, and there'll still be a luxury or whatever that people pay more for.

**Chris Gammell:** So does that mean that the, so like if you had a LiDAR sensor on top of a car, then would that be on a completely different system? And then that whole computer system would talk through the CAN bus to the rest of the car for a retrofit or would it be like a LiDAR system puts data onto the bus as well?

**Dave Jones:** I mean, we, we haven't really worked with a, one of those actual cars yet, but, um, okay. You know, I mean, even in, uh, I think we talked about a little bit, you know, there could definitely, there already are cars that have, you know, six CAN buses or something like that. So I'm sure it'll be something like that.

**Colin Kidder:** Well, also as well, uh, when they, with self-driving cars, they're going to faster buses. I think it was Earl mentioned FlexRay in passing. That's a competing standard to CAN bus, but FlexRay is a lot faster. I think 10 megabits per second. So it's, it's getting up there close to ethernet. So as you see self-driving cars and this autonomous systems, a lot of times the autonomous system is sending so much data so rapidly, you couldn't do that over a standard CAN bus where you have 50 kilobytes per second of transfer speed. So they're going to things like FlexRay and ethernet. And that's where you're seeing the autonomous systems. So there is kind of a transition in that respect to newer, faster buses that can handle the kind of load that say a LIDAR sensor puts out.

**Chris Gammell:** Yeah, I guess, I guess right now, I mean, I, again, like my experience is only in distributed control systems, but it's all like human scale kind of stuff is pretty slow. Like, you know, you upstate something 10 times a second. It seems like it's real time to most humans, right? It's what 30, 30 milliseconds is like the light, the light window or sound window when you start to be able to hear delays. Um, so yeah, that's, it's not that fast. Whereas a computer is like,

**Colin Kidder:** I'll take all the data you can give me. So, yeah, you know, when you're talking about a LIDAR sensor or something, it could be updating the distance to objects a thousand times per second or 10,000 times per second. Right. And when you get up to that kind of data speed, you need something faster than can to send that kind of data to the system. Not to mention that, you know, like Tesla is actually doing autonomous driving by looking at video. So you obviously aren't sending video over a can link. Right, right. So you're, you're getting other bus systems in there that are much faster for that kind of data.

**Chris Gammell:** Okay. Yeah. So that's, and that was, that was my question too. So like, so even at like a, like a reverse camera right now, they, they would be, I guess infotainment's kind of a whole separate system anyways, but, uh, anything with a camera in a car right now, it's pretty, it's going to be

**Colin Kidder:** a separate system almost guaranteed. Yeah. That a lot of times systems like that are connected to, you know, they're connected to CAN bus for command and control kind of, but they have a separate bus too for audiovisual things or in an autonomous system, a separate bus for the actual flow of video data or LIDAR data, but they still have command and control probably over CAN where there's still something, say the ECU is still telling the LIDAR sensor that what it wants to see and things like

**Chris Gammell:** that. Got it. Okay. Yeah. Cause I, yeah, that's the other, I guess the other story that I remember the news past couple of years, there was the, the G packing where they did, they did that, but they did it. They, they, they were able to access the CAN bus, but it was via the, the supposedly firewall

**Colin Kidder:** infotainment system, right? Yeah. It's not uncommon in these cars for there to be a lot of CAN buses. And to some extent they try to segment them away. So the important stuff is not usually user accessible, but there's always going to have to be a gateway system somewhere that can talk on both buses at the same time. So basically what they did in the Jeep was I think hack the radio or something. Yeah, it was. And the radio had access to the other bus. So once they got access to the radio, they could hop over and piggyback onto the bus. That was really important.

**Dave Jones:** It wasn't a lot of that through like the OnStar system or something.

**Chris Gammell:** Yeah. Yeah. I think so. Yeah. It was something that's usually user accessible. I remember that. Yeah. Well, I'm glad that, I mean, that sounds like, honestly, it sounds like all of this stuff is why you guys are doing what you're doing anyways. It's you're enabling, you know, more visibility. It's coming either way, right? It's either people are going to, you know, do it on their own and do it maliciously, or, you know, there's more visibility and then they're like, oh yeah, we should probably secure this stuff. So it sounds like, it sounds like the, uh, Machina and the, and the M2 is, uh, its own, its own, uh, reward there.

**Dave Jones:** Yeah. I mean, I think it's a, it's an interesting, you know, dual goal where we kind of want people to be able to, you know, control their car and, and mess around with it and repair it and, and tinker with it. But, you know, also you, you don't want anyone that doesn't own it, you know, doing anything. So certainly, uh, sort of a dual purpose, I guess.

**Chris Gammell:** I'm, I'm actually amazed that there is so much access onto the CAN bus that there is like, I, I guess from a, you know, I don't know much about security, but I know certain things shouldn't be allowed. Right. And, uh, it seems like a lot of stuff's allowed. So it'll be interesting to see

**Dave Jones:** as that stuff changes over time. Yeah. I mean, we're definitely, I think things have definitely gotten harder even in the last few years. So imagine it'll continue to get complicated.

**Colin Kidder:** It's kind of the dual edge sort of what we do. So we're trying, especially what I do where I'm trying to take OEM components and use them in other cars. Well, security was virtually non-existent at first, even in electric cars, because nobody knew anything about it. It wasn't publicized. And so they were able to be very lax with their security. Nobody, uh, nobody really thought much of it. Now that there's visibility with, you know, the, the G pack and some other things. And even with Makina, I mean, the more visibility we get, the more the OEMs take notice and say, uh, maybe we wanted to secure these things a bit better because now everybody and their uncle is hacking on their cars and who knows what they're going to do. Right. So it's a bit of a, of a double-edged sword in that the more visibility you get, the more they lock it down and the harder it makes your own job.

**Chris Gammell:** But probably, probably for the best, right? Probably. Certainly. Right. Your, your, your day-to-day pain is everyone's, uh, is everyone's benefit. There we go. We've just found the treasure, treasure chest. Uh, we should probably use that as the end of the show here. So, uh, where can people find info about, uh, about Makina and, uh, and M2 and everything else?

**Dave Jones:** Yeah. I mean, you know, we have a website, Makina.cc, um, Twitter. Um, I think that's just Makina.cc. But, uh, you know, a lot of the development stuff kind of goes on on the, on the forum. Colin's, uh, Colin's always on there. Um, we're all on there, I guess, but, um, you know, stop by there if you're, if you're interested in this sort of thing. And, and, um, yeah, I mean, we're, we're at a lot of the conferences too, the ones we've run into you at and, and others as well. So, um, hopefully we'll, you know, run into a lot of your, a lot of your listeners. There's any, any upcoming that people should keep an eye on it? Um, you know, I think Will's at a couple of the B-sides conferences, whether I was, uh, this weekend maybe. And, um, you know, we'll definitely be at DEFCON and, and some of the more popular ones, uh, we're always at at Supercon. Um, yeah, I don't make it to a ton of them, but, uh, I don't think Colin does either, but, you know, Will's at 20 plus conferences a year. So.

**Chris Gammell:** Okay. And that's Will Karuna, right? Yep. Yep. That's the guy. Okay. I'm trying to get better at using last names. I've already, yeah. And, uh, the Rick that it was all Rick Alter was the one that I was trying to remember before I looked it up in the meantime. So, all right, well, great. Thanks guys for being on and, uh, we'll definitely post links to all this stuff. Uh, and this has been a really good, it feels like it's just, this is the beginning. Like I could feel myself like asking more and more questions and like, as I kind of got a feel for what was going on there. So, uh, it sounds like an exciting field to be in. So thanks for telling us about it. Yeah. Thanks for having us. Thanks for having us. All right. Well, we'll see you at conferences and we'll talk to you soon. Bye now. Bye.

**Speaker ?:** We'll be right back.
