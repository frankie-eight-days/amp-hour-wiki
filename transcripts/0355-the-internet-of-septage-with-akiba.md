---
episode: 355
title: The Internet of Septage (with Akiba)
url: https://theamphour.com/355-the-internet-of-septage-with-akiba/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by, we don't actually have sponsors anymore, but I wanted to pretend that Contextual Electronics was sponsoring this. Really what I wanted to do was tell all of our Amp Hour listeners about a sweet deal that one of our former guests, Clint Cole, his company, Digilent, is offering a deal for Contextual Electronics members. So I wanted to announce it here. Basically, you can get the student pricing if you buy three months of Contextual Electronics on the Analog Discovery 2. It's a really cool piece of test equipment. We do talk about it a little bit in this episode. But check it out. I'll put a link in the show notes. Hope you take advantage of it. This is the Amp Hour Podcast. Released August 13th, 2017. Episode 355. The Internet of Septage. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Akiba:** And I'm Akiva from Freak Labs.

**Chris Gammell:** Welcome back, Akiva. How are you doing, man?

**Akiba:** Oh, good, good, good. Just got back from like five weeks in Europe on vacation. That sounds rough.

**Chris Gammell:** That sounds rough. I got to say. Yeah.

**Akiba:** Yeah. Eating all the sausages and the cheeses. And yeah. It was actually my first time in continental Europe.

**Chris Gammell:** Really? Oh, wow. What countries did you go to?

**Akiba:** It was just Spain. Well, mainly I was in London. So I've been to the UK before. But I spent most of my time in London and then took a trip out to Ibiza in Spain and then also Barcelona.

**Chris Gammell:** Oh, wow. That sounds awesome. Yeah, yeah. Yeah.

**Akiba:** It was really, really nice. So I, you know, and after that, then I've decided that I need to understand Europe much more. Like, because I've been missing out on something amazing.

**Chris Gammell:** Like, what do you mean? Like culturally or?

**Akiba:** I think culturally, like going to Spain was really interesting. Like, because, well, going to Spain was really interesting because I grew up in California. And, you know, and so I grew up with a lot of Mexican influence and Mexican culture. But when you, when I went to Spain, I could see that a lot of the Mexican culture, Mexican, a lot of the Mexican culture was influenced by Spanish culture. And then, you know, and then so I'm curious to learn more about Spanish culture in relation to, like, the Mexican culture, which was part of my American upbringing.

**Chris Gammell:** Yeah, that's interesting. Yeah, I guess you can kind of just keep going east with it, too, right? And seeing how, like, Spanish culture was, Moorish culture was, you know, like all these different things kind of going back as, like, you know, different migrations happen and everything, right?

**Akiba:** Yeah, yeah. And also, like, being in the UK, because I think it was about 10 years, more than 10 years that I've been in the UK. But going back there and actually having more time to look around than I could see, like, a lot of the stuff from the UK helped me understand more about American culture. Because, like, so much of it is imported, but so far back that, you know.

**Chris Gammell:** Right, that it's been morphed and, yeah, it doesn't really, it doesn't make sense anymore or something.

**Akiba:** Yeah, yeah. So that was really interesting. So that was really nice to just kind of take a break from, like, the technology and electronics and just, like, kind of go into place.

**Chris Gammell:** Are you able to shut your brain off or?

**Akiba:** Actually, no. Like, I had to, like, you know, I had to escape and actually kind of work on some designs. And, like, that was really interesting to me because, you know, that, you know, like, because I actually, I really enjoy, you know, electronics and kind of, and designing. And I enjoy what I do. Yeah. So, and then I had, like, a lot of inspirations for, like, kind of designs that could be, you know, that. So, like, new product ideas or something or? Yeah. It could be new product ideas. Some were just, like, kind of, oh, it'd be kind of cool if I tried this out. Like, you know, just maybe some, like, lighting, especially, like, solar-based lighting. Oh, yeah. I don't really into that right now.

**Chris Gammell:** Yeah, that's cool. I definitely want to hear about that. I think it's good, too, because it's like you, when you, when you downshift your brain like that, right? It's like, it's just, like, kind of like the importance of boredom, too, where they talk about, like, well, why do you always come up with, why do people come up with ideas in the shower or, you know, sit in a can or whatever, you know? Like, it's just because you're introspective because there's not much else to do. And so on a vacation, it's kind of like that, right?

**Akiba:** Yeah, yeah. I mean, like, because if, like, if I'm, if I didn't switch, if I don't switch gears and I saw if I'm in work mode, then I'm just looking at kind of maybe efficiency improvements. Yeah. Like, just kind of, you know, other, other things. But then, yeah, if I just have free time and then, like, my mind just wanders and then suddenly I get, like, an idea to try something out.

**Chris Gammell:** That's great. That's great. So what have you been working on? I suppose that's a good catch-up for all of our listeners who've heard shows with you before. We've done, we've done what, like three or four shows now, right?

**Akiba:** Yeah, yeah, yeah. Actually, you know, and thank you, thank you. It's always really nice to be on Amp Hour because I like listening to you and Dave talking, too. Yeah.

**Chris Gammell:** Well, it's good to have you back, man. I think, I think, I point to you often as someone doing interesting things at the edge of the industry, like we were talking about before the show about agriculture type stuff, I think. And you're, well, all the stuff you'll tell us about, I'm sure. So what have you been working on?

**Akiba:** Oh, yeah. Um, yeah, it's, I've been working on a project out in Egypt recently. And so this is a project with the World Bank and it's dealing with sanitation technology, which is very, like, probably the most, you know, it's, it's not really. It's a shitty job, huh?

**Chris Gammell:** You can say it. You can say it.

**Akiba:** It's, you have to deal with a lot of shit. Yeah, right. A lot of shit. Ha, ha, ha, ha, ha. But, um, yeah, it's, it's really fascinating because it's such a basic piece of infrastructure, but it's, like, largely ignored by the technology industry. I think it's, it's probably because it's just an unglamorous thing. It's probably, like, technology and trash. You know, there's not a lot of trash technology also.

**Chris Gammell:** Well, it seems like there's not a lot of opportunity there because it's not really, like, infrastructure is more physical, it feels like. But at the same time, you need to monitor it and control it and all these other things that happen in other industries, right?

**Akiba:** Yeah, yeah. I mean, but I think there are opportunities. Actually, you could kind of say that there are, like, kind of huge opportunities because, um, if you think about, like, how many homes have, like, you know, like, laundry machines or something like that, you know, it'd be, like, millions. And then if you think about how many homes have, like, septic tanks, you know, versus, like, being connected to the standard sewer system, like, homes have septic tanks. And then you need to know, like, when the septic tanks are full in order to call the guy to have it serviced.

**Chris Gammell:** Right.

**Akiba:** You know, and so that would be, that would be a piece of tech, like, a very simple piece of technology that you could implement.

**Chris Gammell:** Right. And the consequences for not doing it are pretty dire. Dire. Yeah. Jesus. Yeah. I was like. All right. All right.

**Akiba:** My girlfriend complains that, like, I'm basically, like, I'm an adult child.

**Chris Gammell:** It's just, you're just creative and free, Akiba. That's what it is, man.

**Akiba:** No, I'm pretty much an adult child.

**Chris Gammell:** Yeah, me too. Okay. So, what kind of, so this was in Egypt, right?

**Akiba:** Yeah, yeah. So, this was, so this was out in Egypt and is actually working with the World Bank and the Egyptian government. It's, like, kind of a collaboration between the two. And the point was to monitor the private operators that service the septic tanks in rural areas. Hmm. Because what they would do is in order to, in order to, so what they should do is when they empty a septic tank, then they need to take it and they need to take it to a government operated treatment facility in order to have the waste treated. Aha. I know where this is going.

**Chris Gammell:** Yeah, right.

**Akiba:** But what they would do is, like, they would, they would service a house and then go to a nearby kind of drain and just empty it all into, yeah, into the drain. And that goes into the Nile River. Right. And then that creates, like, an environmental disaster. Right. Which is one of the major reasons why a lot of the Nile is, like, has unpotable water.

**Chris Gammell:** Oh, really? I didn't realize it was that level. Okay. Yeah.

**Akiba:** Yeah. I mean, well, because so many do it, like, they do it so much that they don't even think that it's illegal. Like, they would just, you know.

**Chris Gammell:** Right, right. It's like, you know, there's, like, everybody else is doing it. Yeah, yeah. The water's gross, man. Yeah.

**Akiba:** Yeah, it was, so it's, it's pretty crazy. And so, so the World Bank had a project where, like, they worked with the government in order to monitor the septic, the operate, the private operators. And then the government would mandate that they have to use this equipment to monitor the liquid levels and geotag the liquid levels and then send that to a server. And then, so anytime the liquid levels decrease where there's, like, some kind of a release of the waste or sanitation, it's called septage. Septage, really? Oh, interesting. I didn't know that term. Yeah, yeah, yeah. Yeah. So I'd be like, so what happens when the poop gets released? And then, like, the septage. Oh, yeah, the septage. Oh, man. But, so, and so it would, like, flag, it would flag, it would flag each event. And so, you know, ideally it should only, it should only be, like, the fluid levels should only decrease at the treatment facilities, the proper treatment facilities.

**Chris Gammell:** Right, right, right, right. Okay.

**Chris Gammell:** Now, that's interesting because I guess thinking about, like, how you would actually track that. So you track it based on the septic tank, not, you don't actually, like, monitor the operator themselves because you might have someone who disables the unit or whatever. Yeah.

**Akiba:** Yeah. Yeah. So, well, one of the considerations was that, like, when the operators understand, like, what we're doing and then they might try and tamper with the equipment. And so, like, there's, like, there's some safeguards that we're, like, we haven't implemented yet because it's still at the pilot stage. But adding in, like, kind of tamper-proof mechanisms. And so those would be, like, kind of authentication. Oh, really? To make sure the hardware, well, to make sure the hardware that's connected to it is authentic hardware. Because, like, there's a couple different ways to tamper, like, such as, like, disabling the sensor or even swapping out to a different sensor. Right.

**Chris Gammell:** Right, hot wiring it or something and, like, just spoofing a level or something.

**Akiba:** Yeah, yeah. So, you know, so I think, but first we're going to do it, do the pilot. So we did the pilot and then we're going to do, like, kind of a controlled rollout and then see how it goes first. And then after that, we'll, then we're going to kind of introduce the authentication based on, like, kind of how. Because, like, there's so many other things to take care of, too. Because we also have to build, like, the server backend and that's, like, working with the government and their IT team to do it.

**Chris Gammell:** Yeah, got it. Right. So what is, what was your, I mean, target bomb cost for this kind of thing was, like, pretty low? Sure.

**Akiba:** Well, the initial, for the initial prototype, I normally don't worry about the cost because I feel like you can always optimize the cost. But, but the main thing was to get it up and running fast. So I use kind of as much off the shelf components as possible. Okay. And so, like, I use, like, so the 3G, like, like, we're using 3G. And so, like, so we'd use, like, 3G modules from SimCom. Okay. And so that'd be the Sim 5320E, which is for Europe. And then, like, aside from that, then, like, and that'd be kind of the main thing. And then there'd be, like, kind of the microcontroller subsystem. Sure. Yeah.

**Chris Gammell:** Actually monitoring the analog level or whatever the sensor output is, that kind of thing.

**Akiba:** Yeah. Yeah. Basically just handling all the bookkeeping and stuff, you know, and just control. But then there'd be, there was SD card, there was an SD card interface and, and then, yeah, the interface to the GPS and the level sensor. And so the level sensor was actually the most expensive component because we used an industrial level sensor.

**Chris Gammell:** As you say, corrosive environment kind of thing. Do you have to deal with that?

**Akiba:** Yeah, yeah, yeah. It was, it was, so we used an industrial level sensor. And then, and it was a non-contact sonar sensor. Oh, really? Yeah, yeah.

**Chris Gammell:** Oh, so it doesn't actually, it doesn't actually even go in the soup, huh? No, it doesn't.

**Akiba:** So it's really, it's more just. It's a horrible way to put it. Actually, I had soup for lunch. So now I'm just like, oh. Sorry.

**Chris Gammell:** No, I just mean, so it's basically just bouncing it off the top level. And it's saying like ping time of how far down it is.

**Akiba:** Yeah, yeah. And so like the idea is at least we're going to test out to have a non-contact sensor first and see how it goes. Otherwise, there's like, there's like a lot of different ways to measure like kind of level. So there's like capacitive sensors, there's float sensors, you know, there's all types. And so. Yeah, yeah. But what we need is just like kind of a fairly rough, like it doesn't need to be like millimeter accurate. But it needs to be like, it needs to be able to tell when the levels are decreasing. Right. That's like the main thing.

**Chris Gammell:** Right. You need to know if 10 gallons are being taken out at a time or 100 gallons or whatever, right? However big the. Yeah. Yeah, yeah. So the government originally.

**Akiba:** What's. So like typical feature creep is when they saw that it was actually working and then they're like complaining that like actually we wouldn't be able to take have an accurate estimate of the leaders of septage. I'm like, yeah, we, you know, we don't really care about the actual, the exact leaders of septage. We just want to know when it's decreasing. Right. Yeah. Right.

**Chris Gammell:** So. Yeah. It's like, well, if you guys want to know the actual level, you can always open it up and look. Oh, you know what? We don't need to know that. Yeah. Yeah. It was.

**Akiba:** I mean, it's actually really interesting because it was nice working with the Egyptian government because they're really supportive. And like normally I think of working with government as like a lot of bureaucracy. And there, there is. But I think they actually, at least the sanitation team got really excited about this project. That's awesome. Yeah. It's because there's, it's largely like, this is an ignored problem. And so having like kind of custom designed devices for a specific application and they're like, oh, actually we can use this to monitor septic tanks too. And then all, you know, then they had like all kinds of ideas.

**Chris Gammell:** That's awesome. Yeah. Like boots on the ground type people who actually see problems day in, day out. Like they're, that's like product research right there. Right.

**Akiba:** Yeah. Yeah. I mean, these are the guys that design the sewer networks and, you know, and have like, you know, the logistics for the, uh, the sanitation trucks.

**Chris Gammell:** Wow. So, um, how, what about power? How's it, how's it being powered?

**Akiba:** Yeah. So, uh, that's, that's an interesting thing too. And, um, originally we were discussing whether we take like the power, like the 12 volt power from the trucks. But then, um, my, my thing is like, because if you take the power from the trucks and they can disable that at any time too. Right.

**Chris Gammell:** And so it looks like a dead sensor when in fact it's a sabotage sensor. Yeah.

**Akiba:** Yeah. Yeah. And so like, so what I propose is just to have it as like an autonomous thing that they, it gets stuck onto the truck and then it's like left alone. And so it's solar powered. So there's a, there like, so there's a cable that goes through the, um, through the tank into like, so to the outside where there's a solar panel and basically it'll just recharge a lithium ion battery. And then, um, and for the 3G, like, and with the 3G kind of uploading, like maybe once per hour, then it should have a, uh, a lifetime of maybe two to three weeks of no sun. And then, um, so hopefully that, hopefully it never hits that point, but you know, it should get some of that.

**Chris Gammell:** I mean, Egypt's not quite known for its gloomy weather. Egypt's no Cleveland, you know? Yeah.

**Akiba:** So yeah, yeah. I mean, Egypt, there's like, yeah, there's a lot of sun. I mean, it's freaking hot out there.

**Chris Gammell:** Right. Yeah. Man, that's a, talk about a thankful, thankless job too of the, uh, the sewer workers and that, that heat, man, that's, that's gotta be crazy.

**Akiba:** So yeah. And, uh, yeah, the other thing was like, uh, we did the pilot test in the middle of Ramadan, which is like, you can't, you have to fast during the day. So from 7am to 7pm, there's no food and no water. And so by the end of the day, I'd be getting like dizzy and like, kind of like, oh, geez. Yeah.

**Chris Gammell:** I don't think they're meant for you to work during Ramadan either though. Yeah. They kind of take it easy during that time, you know? Yeah.

**Akiba:** Yeah. Actually, I didn't, I didn't realize that when I scheduled the pilot. So I was like, oh, that was, this was a bad idea. You're like, the hotels are so cheap.

**Chris Gammell:** Nobody's there. Yeah. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Well, that's cool. So, so you're saying that this, this is installed on the truck though. And I thought you were saying this is on the septics.

**Akiba:** Um, oh no, I'm saying that'd be, cause that was like one of the ideas that came up from the sanitation workers is just like monitoring the septic tanks. Like having a very low cost thing that would monitor septic tanks.

**Chris Gammell:** But you, but the, but the actual, uh, thing is the truck you're saying.

**Chris Gammell:** That's the goal.

**Akiba:** For this particular project, then we want to monitor the trucks to make sure they're like behaving properly. Got it. So like, yeah, it's really kind of a check on the drivers to make sure they're not illegally dumping.

**Chris Gammell:** Right. Yeah.

**Akiba:** So, but yeah.

**Chris Gammell:** I mean, this is, I mean, we were talking a little bit before the show too. Like this is like, all right, so internet of things, let's just say that term, get it out of the way.

**Akiba:** But like, this is like, I know, right.

**Chris Gammell:** You never see it coming and then it hits you.

**Akiba:** It's the internet of toilets.

**Chris Gammell:** That's right. Internet, the literal internet of shit. Right. Yeah. Yeah. Um, yeah. But like, this is a really good use case of this, I think. Right. It's like, it's monitoring something that seems a bit banal, but it's actually solving a problem that you can do, you know, with, with monitoring data and, and, and watching. You're over time watching trends doing, uh, what's it called? Uh, SPC, like statistical process control. You can see when something's out of control. It's like, okay. Yeah. Yeah. This all makes sense to me. I mean, this is what you do anyways. You did this for the rice farm as well, right?

**Akiba:** Yeah. Yeah. I mean, I think like, like, cause a lot of people, cause I think the, the problem I see with like, say I, IOT, like internet of things, um, like, uh, we, we called it wireless sensor networks, but you know, that's, but anyways. That's so passe. Yeah. Yeah. I mean, it's being pedantic. So, uh, you know, so I'm just asking permission to use IOT for now, but, um, like, I think the problem is everyone's searching for like the big killer app. That's going to, you know, sell millions of units or, you know, and then.

**Chris Gammell:** Well, they always look in consumer too. Right. Where it's like, yeah, yeah. That's not, that's not where it's really going to matter. I think.

**Akiba:** Yeah. I think, I mean, I think it's going to be really hard because there's so many different domains that you have to cross. Like, so, you know, for this project alone, we had to, we had to deal with just like kind of like just getting the specifications, like under, like working with a domain specialist in sanitation technology. And then after that, creating the electronics, then writing the firmware, uh, getting the communications going and then working on the, the server backend into the database. Yeah. So we had like, so that was like, you know,

**Chris Gammell:** And keeping it secure and all that other stuff too. Right. I mean, like there are legitimate concerns.

**Akiba:** Yeah. And we're still discussing like how to do the security in order to like, you know, like that's, but I mean, yeah. And then, and then, um, there's also, and the big thing, like the government, like, especially the, um, like the, the minister of housing and stuff. And they're really concerned about the front end and like how the front end will look because they need it to look like kind of very intuitive and also like beautiful because that's, you know, that's the, the face of the project. Right. And so we have to work with front end designers in order to do that. So there's like a huge, um, you know, like domain, a huge amount or. Right. The span of it all. Right.

**Chris Gammell:** I mean, yeah, it's, it's crazy. Yeah.

**Akiba:** So, and so I think, and it's complex and I don't think it's ready for consumers at this point, but there's so many kind of niche applications that it'd be really useful and you could actually change a lot of, you could, you could optimize or you can kind of, uh, disrupt a lot of industries with it.

**Chris Gammell:** Boy, we're, we're two for two on the, on the bingo sheet in here, man.

**Akiba:** No, but I mean, you could, you can actually.

**Chris Gammell:** You can make a meaningful impact in the world you're saying.

**Akiba:** Uh, yeah, yeah, yeah. Yeah. So, but I wanted to use the D word cause I think I, I feel, I feel like, I feel like it's important. If I'm going to use IOT, I'm going to use disrupt too.

**Chris Gammell:** You do you, man. You do you. That's good. Yeah. And we were also talking about like the applications. You were saying the applications are what interests you anyways. Right. Because it is this spanning all these domains anyways. Right. Of like, it's different tools you're pulling down off the shelf, but then the interesting stuff is searching out the applications that might make sense.

**Akiba:** Yeah. Yeah. I mean, I think there's, there's so much focus on the technology. Like, so for IOT, then there's so much focus on the technology. So there's like, there's wifi, there's Bluetooth, low energy. There's Laura, there's Sigfox. Sigfox. Yeah.

**Chris Gammell:** There's, you know, like LTE. There's the, uh, what's the WLowPan or something?

**Akiba:** Yeah. Yeah. Six, there's six LOPAN. Six LOPAN. That's it.

**Chris Gammell:** Yep. Yep.

**Akiba:** And then, I mean, there's so many in like, you know, like, and I guess I've been involved in it long enough that I just don't really care about the technology because the technology is come and go. And like the real issue is like, what problems can you solve? You know, like, you know, like it really doesn't matter kind of what technology you use as long as you can solve the problem. And I think that's, that's where I've kind of ended up right now is like, you know,

**Chris Gammell:** so. So is that true in prototyping though, or is that true all the way through to production as well? Because it feels like in prototyping, I agree with you, but I think then the production, it starts to change things around a little bit.

**Akiba:** Um, I guess, well, it would kind of matter. Like right now, I think, I feel like I use a pretty, like I use a fairly simplified stack. So I'm just, you know, I'm, uh, in terms of technology. So I just use like kind of standard 802.15.4, uh, radios, which, which, um, like that's been stable. That's, you know, they're like, like the protocol's about 15 years old now, I think. Yeah. And so like, so, and then the chips are very stable. And then, so that's kind of for the short range wireless. And then, and then that would go to like a gateway that'd be using like, like 3G. And then that's very stable also, because that's the same, you know, cause it's the data network.

**Chris Gammell:** Right. Yep.

**Akiba:** So, um, so I feel like that's a manufacturable, that's, that'd be stable through production also. Whereas, you know, um, I think if you scale something like Laura, then you also have to discuss with the ISPs to see if there's lower service in the areas that you'd want to scale it to. So I, I would consider that like.

**Chris Gammell:** Remind me what Laura is. I mean, these, these names really have crept up on me where I'm like, I don't even know what you're talking about now.

**Akiba:** Oh, okay. So, uh, Laura is a kind of a, I guess, uh, night, like a 900 megahertz, uh, wireless sensor protocol. It's, um, mostly pushed by Semtech, which is a chip manufacturer. Um, and they basically, they're kind of advocating setting up kind of small ISPs and create, you know, basically in my opinion, duplicating the cellular cellular network in order to get to provide coverage for these, um, so that you can throw these sensors down anywhere. And then they'd be able to, uh, connect to the, and they'd be able to connect to the internet. So even in remote locations, you can still connect to, um, uh, the internet.

**Chris Gammell:** So is that like someone else owns the base station though? Or like it's like you, you own and run the base station?

**Akiba:** No, this would be someone else. So this is a service provider model. And so, and then, you know, there's a lot of people like within a lot of skill for that,

**Chris Gammell:** huh?

**Akiba:** Yeah. Yeah. And so like, and they're pushing it, there's like money involved in it. Like Sigfox pulled down, like, you know, I think hun tens or hundreds of millions of dollars. And then they're doing the same thing. But I just feel like, you know, and then the, the data rates that they're talking about is like less than like, you know, and they're saying, oh, if you do this, then you can transmit, you know, once every five seconds or something like that. It's like, right. Right. Right. And like, and you're talking about like, you know, you get like you're, you're available. I don't know. It's just like, my big thing is you don't own the network. And so like, if you don't own the network, then, then, then it works until it doesn't, right? Yeah.

**Chris Gammell:** It works until, until they're like, oh yeah, we're obsoleting this. And you're like, uh, what? All of my devices are in the field.

**Akiba:** Well, yeah, yeah. I mean, like, how is that better than just using available infrastructure? And so like, that's what I, I prefer, I prefer like kind of taking a risk averse way of doing things. They're just using like what's available right now. Right.

**Chris Gammell:** So, I mean, to be fair, like, so you're talking about creating a similar kind of setup where you're saying like 3G backend and then you, you have a 802.15.4, uh, like broadcast point from there. Right. Yeah. Yeah. So like, but, but there is, there is risk at least a little bit in terms of like, well, if 3G gets obsoleted eventually, you know, there is risk for that too, but yeah, it's probably lower risk. Right.

**Akiba:** Yeah. I mean, it's all, it's, it's all a matter of like, yeah, degrees of risk. And so like, I would say that cause like 3G, 3G is working and, um, so it won't be obsoleted for a while because like, you know, like I think GSM is slightly risky in developed countries because that's kind of like, it's being sunsetted in, in the U S and, uh, and some other countries, but it's still like, it's still strong in like India and like Egypt.

**Chris Gammell:** Right. Well, that's another thing that's interesting too, is that like, so you, you obviously already talked about places, you know, having, having devices in multiple places, then you start having to do versioning for your products as well, where it's like, oh, well, you know, that might already exist because of spectrum limitations or whatever, which modems usually take care of, but, but it's like 802.15.4. Is that, is that allowed everywhere?

**Akiba:** I mean, um, the, so 2.4 gigahertz is basically, um, yeah, uh, kind of an international license-free band. And so, uh, so that's why everybody that uses 2.4 gigahertz and then 900 megahertz, you have to be a bit careful because like in Europe it's, it's like Japan 815 or something

**Chris Gammell:** as well. I forget. There was one that like switched shifts down, doesn't it?

**Akiba:** Yeah. Well, it's Japan was originally 950 megahertz, which was like an oddball frequency. And then they switched it down to like 908 megahertz now, which is more within the, the, you know, like the North American, the antenna doesn't change as much. Yeah. Yeah. It's just like, um, basically like chip companies would have to create radio specifically for Japan in order to, um, in order to be compatible with, uh, Japan standards. And then, and then because Japan is a small market, then like basically it would be the price goes up like crazy, right? Yeah. Yeah. Yeah. So basically pretty much nobody did it. And so it was a useless, uh, spec. Oh, interesting. So, um, so that's what that, that's, I think one of the reasons why they changed it down to like 908 and then, uh, but Europe is 868 megahertz. Like us is like nine 15, nine 30. So there's like, there's all these different versions. So most, most 900 megahertz radios will support like maybe 850 to 900, 940 megahertz

**Chris Gammell:** around. Oh, and then they'll just tune in based, like you can set a register or something and

**Akiba:** it tunes into the, to the location. Yeah. Yeah. So there's a PLL that, you know, normally you can, you can, um, set the PLL in the registers to, uh, for like whatever frequency you want to, you want to be the center frequency. Hmm. So that's cool. But yeah. So, I mean, it takes more study based on the country, but you know, but I think I, I like 900 megahertz cause you

**Chris Gammell:** get better range. That's, that's great. Yeah. Um, yeah. You mean also because of like absorption and the 2.4 gig, um, spectrum and stuff like water absorption? Yeah. Well, 2.4 gigahertz,

**Akiba:** you can actually get really good range off of 2.4 gigahertz. You just have to have like a simplified protocol, like a low data rate. And then, um, like say in North America, you can blast out to like one watt. So you can have like a one watt front end. And so that would, you know, they're like people that use like, you know, like, uh, front end app, like Ubiquiti uses like, you know, front end amplifiers and also high gain antennas. And then they can get like, you know, like 10 to 30 kilometers of range. Really? Wow. Yeah. Yeah. And what

**Chris Gammell:** kind of, what is the data rate for those guys? Like kilobit or lower? Uh, I'm not sure. I

**Akiba:** don't have a huge amount of experience with the Ubiquiti stuff, but I think like if you wanted to do like really long range stuff, then you'd have to back off to like, like, um, because you can't like the high data rate, the high data rate, uh, wifi uses a complex, like a complex communications encoding. Right. And, um, it becomes difficult, like, you know, cause if, as you go long distances, you get a lot of noise. So you have to use a very simple encoding. So like a BPSK, like if you, if you go down to like 1.5 megabits per second or something like that, which is like super old school, then, um, you could probably get like really, really long range. Got it. Yeah. Cause, uh, a couple of weeks ago,

**Chris Gammell:** I had, uh, Mike Osman on the show and he was, he was previewing his talk that he was going to give at DEF CON. I had to go see it. And he was talking all about the, uh, uh, direct sequence spread spectrum stuff. Yeah. And that, that blew my mind. I had never really looked at that stuff before, but it kind of blew my mind. So like, but like it was about, it's a, you know, like the keying and all that stuff. I think they'll probably publish that talk eventually, but it was really, um, just like how you, how you can like basically dig a signal out of nothingness. It's, it was really cool.

**Akiba:** Oh, okay. Yeah. Yeah. I don't, yeah, man. I don't like that. That'd be kind of interesting, but like, I don't really dig too deep into like kind of the, the physical layer of the communications, but actually like the spread spectrum is generally just to play nice with other frequencies. And so you can turn it off and then you get like a higher data rate cause you don't have to go through like what's called the scrambler. So you get like a much higher data rate. So if you want to be an asshole and then you just turn off the spread spectrum and then use the higher data rate, but if you're in the middle of the countryside,

**Chris Gammell:** maybe it's not a big deal, right?

**Akiba:** Yeah. Yeah. Yeah. So, yeah. So I've, I've tested that out and it's actually, you know, it's, uh, it's pretty nice, but then, but yeah, if you, but then you'll like,

**Chris Gammell:** it seduces me each time. I love the data. But since you like, you, you have such a sharp

**Akiba:** peak at a center of frequency, you'll corrupt other, other people's data. So those spread spectrum, uh, flattens out that peak and widens the actual spread spectrum. So you spread the spectrum and then that, that will reduce it.

**Chris Gammell:** So like less concentrated in energy kind of thing.

**Akiba:** Yeah. It reduces the noise and interference that would corrupt other, other data that might be sending. Got it. You know, so. Hmm. That's cool. So you're, so you basically,

**Chris Gammell:** I mean, and that's, so that's your kind of your general setup. You're saying 3G to this 802.15.4. And then a lot of your receiving devices are simpler. Like, uh, they, they have that same 802.15.4 and you do some kind of handoff between them then.

**Akiba:** Yeah. Yeah. Like, so I advocate like keeping networks simple. So I, I basically just do, um, like single hop. So, um, like there's all this talk about mesh, like Bluetooth. Oh yeah. Yeah. But I advocate like, you know, just keeping things simple cause that simplifies the software, which simplifies the chance for, uh, bugs and errors a lot, but you just do a single hop to, you know, to the gateway. And then that goes to the, um, the server. And so like, you know, and that would cover, especially if you have like kind of control, if you control the antennas and you have amplified front ends, then you can do like, you know, a couple of kilometers, you could do a couple of kilometers for the, the local sensor network. And then, and then you just have the gateway to the server and that would take you all, all the way to, you know, just like being, I guess all the way to the cloud, the cloud, three for three,

**Chris Gammell:** the cloud, Ooh. Akiva, the cloud is just someone else's computer.

**Akiba:** Pretty much. Yeah. Yeah. For me, that'd be like the $5 digital ocean.

**Chris Gammell:** Yeah. Right. Exactly. Yeah. The droplets. Yep. Yep. Yeah. So, um, but yeah, so, um, Oh, I should, I should announce that, uh, I finally figured out how to do Let's Encrypt. Uh, so the amp hour page is now HTTPS. So I'm, I'm very proud of myself for that on the, speaking of digital ocean tutorial that set me free. Oh, that's awesome. Yeah. I, you know,

**Akiba:** like, um, for, for hacker forum, which is like what, you know, like the project that we're doing out here, um, like Let's Encrypt is amazing because, uh, before in order to set up a web shop, I guess this is kind of an aside from everything else, but to set up a website, web shop, you just had to pay, you know, you had to pay for a, like, of course, like the, the web service provider, but then you had to pay for a, a, a static IP address in order to get the SSL. And then the, and then after that you had to pay for the SSL. And so like, you know, when you total it all up or to get the, the shopping cart. And then when you total it all up, it's like $300 a year or something like

**Chris Gammell:** that. Right. Yeah. Cause you're supposed to get that, like the consumer enabled, uh, uh,

**Akiba:** certificate too. Yeah. Yeah. But I mean, so with, with Let's Encrypt, then, you know, you, and also like, um, you no longer need static IPs in order to, um, like, Oh, I didn't know that actually. Okay. Well, well, Let's Encrypt is, um, your URL based. And so like, and I tested this out. Um, and so you can basically just create web shops for free now with like, you know, if you have like a service provider that handles Let's Encrypt. So for Hacker Farm, we're just setting up web shops for, you know, for all the people out here and then for, you know, local. Oh, really? That's fun.

**Chris Gammell:** So it's like, it's like a distributed Etsy. Yeah. Yeah. Or just all their private web shops,

**Akiba:** but it just, it makes it, it makes it where like to set up a web shop has like zero cost. And then you use, um, uh, like Stripe, which is a free, which is like payment processing. Yep. Yeah. Which is free payment processing. So you don't have the credit card fees either, like the monthly credit

**Chris Gammell:** card fees. Well, it's not free. It's just low cost, right? I mean free. No, no. I mean like,

**Akiba:** because normally for the payment processing, you'd pay a monthly fee for the merchant process.

**Chris Gammell:** Right. Right. Right. Right. Yeah. You're right. Yep. And so like with Stripe, you don't pay those

**Akiba:** monthly fees. So basically you set up a web, you set up a web, a web shop for, for next, next to nothing, I would say. Yep. And then, um, yeah. And then you, and then you only pay, you only pay the process, the transaction fees when you, you go through it. And that's like, I think that's one way that I think we live in the future is that you can just set up a shop for

**Chris Gammell:** almost no cost. Right. He says that as he communicates over thousands of miles under, on fiber optic cables to a guy in Chicago. Yeah. Yeah. We do. We, we do live in the future.

**Akiba:** It's pretty amazing. I, I agree, man. I think it's, unfortunately that future includes a president

**Chris Gammell:** who is Trump. So, well, we won't need to go there too much, but yes. Yeah. Yeah. Okay. I'll, I'll stop right now. I'll stop right now with that. So just had to throw that one in there. Take the good with the bad. Take the good with the bad. Um, late night TV has never been better. Yeah. Yeah. Um, so, um, so you're setting up web shops. Where were you going before that? Uh, we were talking about like, like edge devices, stuff like that. And, and, um, that's really cool though. I mean, so how is the rice project going? Is that, uh, that, that, that is a similar

**Akiba:** kind of setup you're talking about, right? Yeah. Yeah. So actually we're morphing the, the rice, the rice field monitoring project to, um, we set up a, a small, like we have like a plot of land on the farm. Cause one problem with the rice farming project is that we had to set up the monitoring equipment on somebody else's property, which means we had to get permission every time we, uh, go and check and like kind of update it. So we, we, we got our own like kind of plot of land and we're setting up like, um, like experimental, uh, experimental agriculture, uh, areas. It's like a patty for science or, uh, kind of. Yeah. I mean like we're not only experimenting with the technology, but experimenting with different grow methods. So one area is we're doing like, uh, rotation crops, crop rotation. Yeah. One area is like kind of, uh, raised bed gardening, but we're like kind of varying the stack, I guess you call it, which is like what's inside the raised

**Chris Gammell:** beds. And then like, as you, as you go down and then you turn the beds for getting like,

**Akiba:** um, like nutrient, um, cycling stuff. Yeah. Well, you know, like, so like the stack that we currently have is like, there's on the bottom is like cardboard and then some kind of, uh, compost material and then a bunch of cow poop and then, um, some soil.

**Chris Gammell:** Nothing makes better tomatoes. I mean like, let's be honest.

**Akiba:** Really like, actually I have a lot of respect for bullshit now. So it's like, it is, you know, I feel like calling, calling, calling things bullshit is doing a disservice to that wonderful thing that actually comes out of a cow's ass.

**Chris Gammell:** I mean, Akiva, you're, you're quickly, you know, you're quickly moving this show to having a poop pun as the title. We're just, we might have to go there.

**Akiba:** Uh, astronomical. But, um, so, so, and then, um, and at the top of the raised beds, then, um, we have soil and then, um, a layer, an insulating layer of rice husks. Oh, cool. Okay. Yeah. That's really interesting because it keeps the water in. So for our raised beds this year, it just, they went crazy and like the plants were pretty much exploding out of the, out of the ground. Yeah. And we have like a huge harvest of vegetables that there's no, nowhere near one, like one, like, like nowhere near like one person can finish. I mean, you just have to, we had to spread it out because we had to get everybody eating it. But, um, but yeah, and we didn't water it at all because, um, Oh really? So just natural rainfall was sufficient. Yeah. It would rain. And then like, um, the rice husks would prevent the water from evaporating out of the ground. So it would let the water into the ground, but then it, or into the raised beds and then, but no, but no mold problems or anything either. Um, not that we know of. So like, I haven't seen any mold. It's mainly the, the larger problems were, uh, insects because since we're doing it organically, then, um, we don't use pesticides. Right. And so, yeah, we, we had to experiment with all these different peppers and stuff like that. Like, uh, what's it called? Capsaicin. Uh, yeah, yeah. Just like the, the spite, like, like spice mixes with like different, different peppers and like vinegar and things like

**Chris Gammell:** that. Yeah. Right. And isn't, uh, that's what nicotine is, isn't it? Like in tobacco plants, like that's, uh, like a natural, uh, insecticide. I'm not sure about nicotine,

**Akiba:** but I think capsaicin, like the, the spice, capsaicin is what makes spicy things spicy. And I think that it prevents like insects from eating. Yeah. Yeah. Yeah. So, and then tomatoes, tomatoes are actually a evolved from nightshade. So the tomato leaves are actually a good, a good

**Chris Gammell:** pesticide also, which I didn't realize. Right. Cause nightshades are poisonous. It's in high

**Akiba:** doses, right? Yeah. Yeah. Yeah. So if you ever play like Dungeons and Dragons and, or whatever, and you had to mix the reagents or Ultima and you had to mix the reagents to make the, uh, poison cure that is like nightshade and mandrake. So that's how I remember it. Like Ultima 4, blast of the past.

**Chris Gammell:** That's fantastic. Um, well, so, but, so the, the evolution of this, of this project though, so you said it's, uh, it's, it's still going, it's, I mean, you said that you're on your own land now,

**Akiba:** but, but is it, uh, what rev of hardware is it? Um, well, so right now actually, um, we're going to convert to 3g because like, since we're doing a lot of 3g stuff, then we're just moving, moving that,

**Chris Gammell:** uh, what were you on? You were, you were on some other kind of like base station setup.

**Akiba:** Uh, we were just using 900 megahertz and we were using like, um, uh, uh, was it directional antennas to a gateway that'd be an ethernet, ethernet gateway. Okay. So you're like, basically I'd

**Chris Gammell:** like point it back in the farmhouse kind of thing and then collect data from there. Yeah. Yeah. But

**Akiba:** I think, um, so, but it's impractical because there's not a lot of places that are like, you know, like very close to like, say a farmhouse that has, uh, like internet, like an, like an ethernet connection. So it, it makes much more sense. Cause I think once we get it, once we get like the farm, the farm equipment, so like the moisture sensors and we get those ones to send to an aggregator and having that sending out to the 3g, to the backend server, then that becomes a solution that, you know, and that other farmers can take and, you know, and, and use. Yeah. And I think we need to make it much more user-friendly too. Right. I was going to ask about that. So like,

**Chris Gammell:** what is the, I mean, it's not like an unboxing, but it is like an implementation almost. It's like, you have to, so do they have to pair the devices? Do they have to just power them on? How are they

**Akiba:** powered that kind of thing? Well, I think probably, um, based on like how, like based on our experiences here is we'd have to have somebody go and set it up at this moment. Okay. Like, you know, we'd have to have somebody to kind of supervise the setup and have everything, you know, set up because it's based on the farmers that we've worked with. They're all like older people, like, you know, right, right, right. Seven, uh, seventies would be kind of like, would be fairly young, you know? And so you don't, wow. Yeah. Yeah. Like out here, out, out in the Japanese countryside. So, um, like they don't have smartphones, they have the old flip phones. So you can't, you know, like the smartphone interface, like the beautiful iPhone interface. Oh yeah. So like you're not doing

**Chris Gammell:** Bluetooth so you can control your app or control it with an app rather. Right. Yeah. It'd be more

**Akiba:** like, you know, you'd almost have to do like send email alerts or, you know, email summaries or SMS even. Right. Yeah. But I mean, like, I think the internet, like having a nice internet, like, um, a nice page that's accessible from the internet and has like a very, uh, uh, a very well-designed dashboard would be useful. So like, that's kind of what, where we're headed right now is like actually kind of like, um, like basically getting the hardware to the point where you can, um, you can transplant it. Like it doesn't, it doesn't require like, um, an ethernet port. So you can basically anywhere, basically anywhere that there's like a 3G connection, then you can kind of use that setup. And then also we need to improve a lot of the, say the server, the server side stuff.

**Chris Gammell:** Right. Well, and you can always do stuff. Like I've been really into like these, um, I mean, if this than that, I think is a great, a great service. And like Zapier is another one for the business side of things that I've been using. I haven't played with if this than that. Like, Oh no, it's, it's, it's really, I mean, like I know some people kind of scoff at it in terms of like connecting things and it's simple and it's a little bit slow, but like in terms of user friendliness, that's what it's all comes down to. Right. It's like, Oh yeah, it's so, it's such a, and so like if you're creating like even a feed, you can really just pipe, it's really just a data pipe that kind of goes from one thing to another. And so you can really make simple, you know, so like you're saying, right, you're saying you're standardizing on a webpage, but it's probably also being fed with a, you know, an API or something. You could then go and plug it in as a, you know, either convert it to an RSS feed or something like that. And then, you know, have subscriptions to that or do MQTT and subscribe to that kind of stuff or whatever

**Akiba:** you need to do. So actually that sounds really interesting. So I have to check it out. Like now that, so the world bank project is like on a bit of hiatus. So everyone's on holiday and, you know, and they've just closed out their fiscal year. So, um, so I have more time.

**Chris Gammell:** Money's gone. I'm gone.

**Akiba:** No, no. Um, but I think, um, so I'm going to have more time to like kind of play around with stuff. So I'd like to, I'd like to look more at, um, like, yeah, I'd like to check out if this and that right now we're using Python. So Python flask is really, is so useful. Yeah. Like, or the flask framework for Python is so useful for like just quickly implementing, like say a server, uh, sorry, uh, a backend, a backend thing. Cause you just, you know, you just use the library for the database implementation and use the library for the, um, the, uh, uh,

**Chris Gammell:** Front end UI.

**Akiba:** Uh, well not the front right now it just spits out like ugly text. So, so that's, that's the problem is like, you know, when you go to a specific thing, then, um, it'll just spit out like kind of Jason, like Jason, Jason, Jason, I guess. It's a Jason. Yeah. But I mean, yeah, so sorry. I meant you need a library for the, uh, the, like, uh, it's a simple library for a database and then it's a simple library for kind of the rest API. And then that's pretty much what we're looking for. And then beyond that, we probably have to work with like a front end developer. Right. Cause like, cause otherwise, yeah, I, I just, I don't even know which, what, which JavaScript library people are on right now.

**Chris Gammell:** But that's probably not worth your time to do either. Right. I mean like, that's the thing. I don't know. I think about like, like APIs and like these, you know, the, the rest, restful APIs and stuff like that too. It's kind of like, they're like connectors, right? Yeah. You know, it's like you, you have a defined interface, you expect certain things to come over each pin or, you know, whatever that interface is. And it's like, then you can talk either way on it, you know, like that's kind of maybe connectors to the API of the hardware world. I don't know.

**Akiba:** Yeah. I'm, I'm hoping that like, you know, so then like ideally we'd only have to work on kind of the API and then like, there'd be like different front end people that would work on various pieces of the front end. Because, um, I think, yeah, that's definitely, I'm not like, I don't, I don't make beautiful front ends. So my, my front ends are ugly and just like functional.

**Chris Gammell:** Right. Yep. But that's, that's fine. Right. I think that kind of separation is as long as you're publishing about what the API is spitting out, then it's not a big deal.

**Akiba:** Yeah. Yeah. No, it's all, it's all open. So this is, you know, and I think that's, that's why I want to do like kind of the, um, just the standard, like say, say 802.15.4 is an open standard to like the 3G, which is like kind of a well-known thing. And then with that, then you can just basically have just everything standardized, everything open and you own the network. And I think that's a very, that to me is very important is because then you control like how often you set, you transmit, you control like how the data is handled, you know, whereas like if you have to go through a service provider, you really don't know, like, are they, are they archiving all that information? Like, do you really own that information? There's like all

**Chris Gammell:** these questions. Right. What happens? Well, like what happens when you stop paying? Right. I mean, that's like, that's a huge thing. Yeah. Yeah. Yeah. The SAS model, but. Sassy. Super sassy.

**Akiba:** So you were talking about, uh, actually, actually, hold on, hold on. I think we're at number four on the bingo. Cause we used, uh, we did say SAS. You're right. Disrupt. Yep. I, I use cloud and then use SAS. So I think, um, are there any more that we should, I'm sure there's more. I think somehow we need to

**Chris Gammell:** work in machine learning and TensorFlow. Oh yeah. Oh yeah. So I mean, venture capital has to come up at some point. Right. Um, AI, AI, AI, of course. Right. And that's kind of tied to machine learning, right? Blockchain. Oh yeah. Bitcoin. Yep. Yep. Yep. We got them all folks. Yeah. Yeah. Yeah. Oh,

**Akiba:** I have, I have one more, which would be, um, uh, what is it? Like bio, what is it? Uh,

**Chris Gammell:** something biohacking, biohacking, biohacking. Okay. Yeah. Yeah. So, cause that's like a big one. What about like autonomous vehicles too? We could just like say that's, I mean, we could really,

**Akiba:** I think, yeah, I mean, oh yeah, I guess that's, that's a bit hypey. Like, no, that's, that's a bit hypey. Yeah. Yeah. So I think, I think blockchain is more hypey than autonomous vehicles. Yeah, that's true. So, and then, and then I really, I really like, um, but I really like kind of drones. So one thing that I'm thinking of doing is I'll probably set aside some money and set aside some money and time and invest in learning how to build like, uh, drones, but more like kind of, um, more like from the point of view of using them in agricultural, uh, applications. And I know like, cause everybody says, Oh, DJI, DJI already does that. But I think, yeah, I mean, I'd, I'd like to know just for my own self, because if I, you know, if I bought or actually my friends have DJI drones and they're terrified of crashing them and I hate, I hate that feeling. So I'd rather like, if I build it and I crash it, then I know that, Oh, it just takes like $20 in parts to repair it. And then that would make me feel much better.

**Chris Gammell:** I think, well, so like, especially with agriculture stuff that I think that you got to do it with a, a fixed wing instead of quads, honestly, cause it's just, you don't get it. You don't get enough

**Akiba:** distance otherwise. Oh, with the quads, like, cause you get like maybe what? 15, 20 minutes?

**Chris Gammell:** 20 minutes is the usual figure. Yeah. And so like, unless you have like a bunch of recharge stations, then, then what, you know? And it's like, fields are not small. So if you're trying to like do a raster of his field, uh, you know, like how do you, how do you do that? You have to,

**Akiba:** Oh, I feel like fixed wing takes more, takes more effort to like. No way. No, they're super cheap too.

**Chris Gammell:** You can do like foam ones that are like super cheap. Oh really? Yeah. Okay. Yeah. Yeah.

**Akiba:** Actually. Um, like also that would kind of like, I'm trying to, I'm trying to set aside like more time to like kind of, uh, uh, to, to get like to, uh, I guess use skills that are outside of what I normally do because I find that I just, you know, cause that keeps me motivated. And so like, if I did the quadcopters that would force me to learn more about quadcopters and also, or fixed wing. And then also then I could actually use my FPGA skills again so I can, um, for the imaging. Yeah. Yeah. Yeah. Cause a lot of the cameras, you need kind of an FPGA interface now. So like, um, yeah, at least, at least it's glue logic to the, uh, to the controllers. Yeah. Sometimes there's a bunch of

**Chris Gammell:** solutions for that stuff. There's that open MV is a Python based one. Um, open, I mean, but I think you

**Akiba:** would, you'd still need, well, I guess if you use a Raspberry Pi, but I'm talking about using like a Cortex M3 as a, you know, keeping the cost down and everything. Yeah. Yeah. So like something that doesn't use like a MIPI interface, like the, the serial, the, the high speed serial interface. So if you use the parallel interface, then you pretty much need like some programmable logic as, as the

**Chris Gammell:** glue to a controller. Yeah. You know, last time we had Bunny on a couple months ago and he was talking about his, his, his 10 year PhD thing. And I was, I was, I was telling someone about that the other day of like, yeah, every 10 years, you know, you just learn a new thing, you know, obviously more than that,

**Akiba:** but like specialization he was talking about. Oh, I feel like, like, I mean, if that's true, then I feel like my, my 10 year thing is business. Cause like I've business, you know, it's like business ethics, business ethics. There are no ethics in business. I'm just kidding. Actually, I've, I feel like much the opposite, but, um, I, because you know, for my business, I think I've made every mistake possible. I've just done everything wrong that you could do. And like, you know, and I've suffered, I've suffered, I paid, I paid my dues. And now I feel like finally, I kind of understand what the concepts are and like, Oh, okay. So when people come to me and, you know, talk to me about like, kind of like, yo, I'm going to do this and this and this. I'm like, you know, normally I don't really, I don't really say much because like, you kind of have to go through it. Otherwise I don't want to like pop their balloon, but you're just like, Oh, okay. I know how this is going to end. Yeah. Your balloon's going to pop though.

**Chris Gammell:** You are going to fall hard. Well, you said, and you said that you're, uh, you're looking at reworking some of your products to, because of that, right. Because of the lessons you've learned and the, the way you want to like improve manufacturing, stuff like that. Right.

**Akiba:** Yeah. Yeah. So like, um, I think one of the big things and like, so if you look at my websites, they're all in flux right now. Cause I'm revamping my main website and also, um, I'm up upgrading my, uh, web shop. But, um, what I'm doing is first of all, I'm organizing my products into product lines. So one of my, one of the mistakes that I made before was just designing stuff because I could like, um, so that's like kind of, you know, like you would start from scratch each time or would

**Chris Gammell:** you actually make like a derivative, like the design A becomes design A1 and then branches to B,

**Akiba:** B1 or something like that. It's like designing, designing something just because like, Oh, you know, like you see something like, Oh, I could design something like that. And then you, so you do it, but that doesn't become a product that you design something and then you put it out there and then, you know, and there's no interest because.

**Chris Gammell:** So the difference between a prototype and a product you're saying, or not even a prototype, like a pilot build almost.

**Akiba:** Well, I think right now, like when I approach a design, it's like, you know, like by the time I'm designing, I already kind of know who my target audience is, like how I want to reach them, like what, you know, the features are kind of features that I think they'd need, you know, like I, I take it, I, I think about the marketing first before I even started design. And I think that's kind of the big shift that happened rather than just like, Oh, you know, like I see something and like, Oh, I'm going to design something for like, I designed something for TV white spaces so that you could geotag, you could measure the white spaces and geotag it and, you know, and see like where there's, like what locations have a new spectrum. And I think that was really interesting, but you know, but there's like, there's like three people in the world that need that. Yeah. You know what else works? GPS. Yeah. So, you know, and then, so like, and, you know, and like, I think my, like, uh, my projects with Wrecking Crew were, you know, where we do like the wireless control of the lighting. I think that was kind of the thing where somebody said, Hey, can you do this? And I said, sure. Let's, you know, give that a try. And then later on trying to turn that into a business. But then, um, you know, it's like, actually it's really cool, but I think I have to figure out like, kind of like how much effort I want to put into that versus like my real thing is like kind of environmental monitoring. So like, I'm really like that, that I feel is kind of my, my calling and my, like, is fascinating to me. He's like trying to figure out like, kind of what might be invisible to, you know, to, to everyone else. Yeah. That's good.

**Chris Gammell:** How to, how to measure what's invisible. So, uh, did you, do you still sell the, you still sell the, uh, the Wrecking Crew like kits to other people?

**Akiba:** Um, I, yeah, I, I sell them. I'm very selective about, because they're not advertised. There's no way to buy them. You kind of have to, you have to.

**Chris Gammell:** Well, I was just, I was on YouTube the other day and for some God awful reason, I came across like a top five, uh, uh, America's Got Talent things. I was like watching, singing videos. And then like one of the, the, the things was like this Ukrainian group that was like, that won a prize on there. And I was like, wait a second, that looks like Wrecking Crew. And they did like the dance that looks almost exactly like Wrecking Crew too. I was like,

**Akiba:** Oh, oh, it might, if they're Ukrainian, then yeah, it might've been myself. Really? So like, it depends. There's like one Ukrainian group that I work closely with. And so they, um, you know, and so that's, but yeah, yeah. Yeah. So like I, I sold it, but I think like the thing is when you sell something, you have to also think about the support and the support burden is pretty high on that. Right. And like everybody's kind of waiting for me to upgrade stuff and then I'm trying to do all these other things. So like that's, that became, that became a problem. So like I'm, you know, and so that's where like, that's another mistake is like, you know, once you have all these different products and they aren't related to each other.

**Chris Gammell:** Right. Well like that, that, that dance, the dance troupe stuff, it's like, that's a whole business, right? That could totally be a specialized business that gets spun out by itself, but then it has to be taken and solidified and it can't, it can't depend on Akiba, you know, saving the day at the last minute. Right.

**Akiba:** Yeah. Well, I'm trying, so I'm trying for that. Then I'm working with some guys in Hong Kong and also working with Wrecking Crew and I'm trying to teach them more about how to like, like maintain the software on their own. And if, if, if somehow a, a software developer comes out of it that wants to like kind of work, you know, like work on that stuff that it'd be cool to work, you know, to have them, you know, have them do it or, you know, basically like, you know, I have to figure out, cause like my main thing is going to be working on the Freak Lab stuff and all the environmental stuff. And so like, and then I think I like the lighting, but I don't want to be like the lighting guy my whole life. Right. Exactly. Right. Like, Hey, there's the EO wire guy.

**Chris Gammell:** Yeah. And, but I think that that it's, it's, it's like this, uh, consequence you, you, uh, you've made this child that you put into the world and it's like now it's, it's, you know,

**Akiba:** it's reaching adolescence, right? Yeah. That's an interesting one. Cause I think that's just, I would, I would chalk that up to like kind of the arrogance of being an engineer, like, because, Oh, you know, since I can do it, then it should be done. Whereas from a business point of view, it's like, Oh crap. What about the longterm effects? Right, right, right, right. Yeah. The

**Chris Gammell:** support stuff is, and especially like when it's something that, that, you know, maybe, maybe I'm sure that you have other projects on your shelf that, that didn't hit as well as that. Right. And it's like, but those just as easily could have been a thing that took off and you'd have to support

**Akiba:** as well. Right. Yeah. Yeah. I mean, it's like really, you know, I, yeah, just like, cause now I think about, so if you have customers and then if you, if you release products, then I, you have a responsibility to support, support it and support the customers. And then do you have the time to do that? And so that's like another consideration. And is it priced in too, right? That's another big thing. Yeah. Yeah. Like the documentation, that's like stuff that you don't really consider as an, so much as an engineer, but like as a business owner, then you start thinking about really hard. Right. Like, especially, um, because you're pulled in like 10 different directions, you know, like, especially for, for people that want to do like, say hardware, open hardware, or just, you know, close hardware or whatever, you know, cause you have to think about the manufacturing. You have to think about the sourcing. You have to think about the marketing and the sales, the web shop, you know, all that stuff. Right. You know, so how much time do you want to devote and help, you know, how many different directions can you go

**Chris Gammell:** in? So that's like a big thing. And the thing that messes with my head too, is like, so like thinking about a product like that, you're, so it's a successful, you know, it's a, it's a successful product that could, could grow more, but it's like, okay, if you really wanted to grow it, right. If you want to get the funding to support all the infrastructure around it, like a support staff and marketing and other design staff manufacturing, if you brought that in house, it's like by that point, then you're just the manager of that thing. You don't even get to do the, the fun stuff anymore, you know?

**Akiba:** Yeah. Yeah. I think like, you know, I, I like working with wrecking crews, so I'd, I'd still work with them, but I don't want to, you know, like, like just kind of supporting them on a lot of inane stuff is just like, kind of, you know, like, you know, it's just, I, you know, that's not like, I don't feel like my calling is to do lighting. Right. Is, you know, my, I'd rather do something that I think is meaningful to me. And, you know, I, I've always kind of like nature and natural surroundings. And so like, it'd be great to try and work on things that might preserve the

**Chris Gammell:** environment or improve it. So hanging out by septic tanks and 40 C weather. I mean, that's another thing that's like you were saying before the show is just like your passion. Yeah. Kind of hoping

**Akiba:** that, well, I'm kind of hoping that doesn't become my whole life, but you know, like, but I think, um, it's actually interesting. Uh, my, my girlfriend and I, we, we wrote an article for, uh, I think it's ASME is, or, or the IEEE, IEEE something. ACM? Yeah. Yeah. ACM is for students or something like that, but it's really, um, I'll give you a link afterwards. Uh, I think if it's online, but, um, anyways, it's about like having a business and instead of creating a business plan, it's creating a lifestyle plan. And I think that's kind of where I'm at right now. I don't, I don't really care that much about like, you know, like making a lot of money cause I live in the countryside. So like, you know, like my, my cost of living is really is minimal right now. So, you know, but I do want to have a lifestyle that I feel, I feel like is meaningful to me. And that means that like, I do stuff that has meaning to me. And also like, you know, like I, I go places and I live places that are meaningful to me. And so like,

**Chris Gammell:** yeah, that's good. That's actually, uh, if, you know, if you'll excuse the business book reference, uh, the book, the E-Myth is like a classic, it's the E refers to an entrepreneur, but it's like, it's basically kind of talking about business. It is told in this weird, like, um, uh, storytelling style basically. But one of the things that he talks about is the, uh, what does he call it? It's the same thing where it's like, you know, you have to, you have to basically imagine what you want your life to be like, cause it's going to be different if you want to be like the head of a fortune 500 country company versus living in the Japanese countryside, right? Those things do not cross over. And so, yeah.

**Akiba:** I, um, yeah. I mean, like, I guess, I think I remember the E-Myth. It sounds like, oh God, it sounds like such a, like a technology title now, but, um, right. It's yeah, exactly. Like, like E, like, like electronics or yeah. Like the E-Myth, like, you know, this, uh, deconstructing.

**Chris Gammell:** Like a story of E-Machines in the nineties.

**Akiba:** Yeah. Yeah. Something like that. I don't know. But, um, but I think like the, the main thing is right now I'm trying to like, for my, for my, my company that I'm trying to cultivate, uh, markets in areas that I have family or my girlfriend have family. And so like, you know, so like I would do like, so I'm trying to put together a schedule for next year that would work, that would have like a bunch of workshops say around California. And so that, that would mean that I can like kind of visit my family as well as like kind of handle and do the workshops and

**Chris Gammell:** promote, you know, my business. Oh yeah. We were talking about that same thing. Yeah. Before the show.

**Akiba:** So it's, Oh yeah. Yeah. And then, well, I mean like, and then trying to do that in London so that, you know, so while we're kind of taking care of the business stuff, but also, um, we can visit my girlfriend's family or Australia, you know, just, and so like, I'd like a lifestyle where, you know, like maybe I, I live for a certain amount of time in like places or we live in places that have meaning to us and, you know, and we structure our lives and our businesses or we structure our businesses around the lifestyle that we want. I think that's kind of, that's kind of important.

**Chris Gammell:** People use lifestyle, uh, business as like a disparaging term, but we're like, uh, sign us up please.

**Akiba:** Yeah. Yeah. It's like, it's like a bad word, but I'm just like, I'm like, you know, like I've seen, I've seen people that have gone through like the VC, the VC grinder and like, it's like, I was like, you know, that's, I don't want my life to be like that. So.

**Chris Gammell:** I agree. I agree. It's, it's, I mean like, and it's, and it's neither good nor bad. It's just that, yeah, you choose not to, right. I mean like you can make a lot of money that way and that might allow you to do even more good at some point in the future, but yeah, it's about whether you're willing to trade off for it.

**Akiba:** I mean, yeah, I think, I think, um, yeah, it's, you know, everything is about trade-offs. And so like, I don't, you know, I think I don't care about becoming like, you know, a billionaire or I don't care about creating a unicorn company. Oh, that's number six. Is that number five or number six? That's gotta be 20. We're at 20 now. But you know, like, but I do care about like, kind of, you know, like, like, like just, I do care about like, kind of the intrinsic things like family and like spending quality time with my girlfriend and things like that.

**Chris Gammell:** Yeah. That makes sense. Yeah. That's great. Oh, but, uh, we were talking about, speaking of time, uh, we were talking about the time it takes to, you know, when you're taking a product through production, the time it takes to build out the, uh, the, the test setup. And, uh, and you were mentioning that that, that takes a while.

**Akiba:** Oh, yeah. Yeah. You mean for like,

**Chris Gammell:** Like test stands we were talking about, right? I love like scripting and all that stuff.

**Akiba:** Oh, yeah, yeah, yeah. Well, cause I think I was asking you about like the Digilant, the Digilant, um, uh, was it the analog?

**Chris Gammell:** Analog discovery too. Yeah. So that's, well, actually, that's, that's true. That's, that's my news from this week. Uh, my course now has a bundle option. So if you sign up for three months of contextual electronics, you get, uh, the academic pricing on the analog discovery

**Akiba:** too. And so, uh, so can I, can I sign up? Yeah. Yeah. I'll post a link. What's the analog pricing? Is it okay to see it on air or?

**Chris Gammell:** Yeah. Yeah. Yeah. So usually it's two 79. Uh, and then they're giving the, the academic pricing is one 79. And, but then there's a bundle that they, um, it includes like a breakout board to BNC headers for the, um, for the scope probes and includes two probes. So,

**Akiba:** so that's that whole thing. Yeah. Well, cause it's interesting. I was, um, like, because you've been looking for, I know you've been kind of, cause you've been talking about it for years,

**Chris Gammell:** which is like the portal lab. Yeah. Yeah. Uh, yeah. We've talked about that on the show a bunch and, and this is kind of moving towards that instead of like having a Pelican case that I haul with me and now this is like a small box. And, uh, how many candidates were there?

**Akiba:** So like, cause you've cycled through like a lot of different systems that had potential.

**Chris Gammell:** That's true. And I, yeah. So I used the salier for a while and that was good. Uh, I, I liked the salier, the logic four, um, but it wasn't enough of a scope basically. That was the main

**Akiba:** problem. Okay. And so what was the speed, the scope speed? Uh, it's like six megahertz or

**Chris Gammell:** something like that. It's, it's, but it's not, it's not bad, but it's not a true scope behavior either. And it's only one channel. So, so those things together. So, um, yeah, so I've been playing and the, the link I'll have about the, uh, the, this announcement. I, I did a bunch of streams that aren't really public, but I was just playing around with the, the analog discovery to a bunch when I was streaming videos. And, um, yeah, it's, I mean, it's great. It's a great little tool. It's, it's all, um, it's all uses a computer screen for UI. So it's USB controlled so that some people don't like Dave doesn't like that, but it's, I think from a certain perspective, it's interesting because like, like you said, like we were talking about scripting around doing test stands and stuff. Maybe that's

**Akiba:** kind of interesting. Well, I mean, I think that's like, um, because like, so for some back, some background story, we were discussing, we were talking before the show and then he was talking about the analog discovery too. And I, you know, and, and, um, it's really an interesting thing because it's an open source, uh, uh, instrumentation tool, like it's a oscilloscope function generator and, um, and also...

**Chris Gammell:** And logic spectrum analyzers, like a bunch of stuff. Yeah.

**Akiba:** Oh yeah. I mean, but it also, you can, you can Python script it and that's, that is, um, that probably had the most interest for me because when you manufacture stuff, then you're always looking for different ways to do the test automation and you have, you know, and the Holy grail for instrument instrumentation is like kind of scriptable instrumentation. So that you can just kind of, you can just have it and, you know, like put the probes on, it'll go through whatever the test sequence is and then give you a pass fail, you know? And so you can script it then, then it just makes things so much easier. So I'm really curious about testing out this tool now.

**Chris Gammell:** Yeah. Right. And yeah, especially if you do like with like, if you could tie the scope and the, the function generators into like a, like a Poga pin header or something too, like you could really do, you can do some interesting things there for sure.

**Akiba:** So, well, I'm, I mean like, so because you know, like the test jigs, the test fixtures that, you know, like that you normally see with the toggle, toggle clamps and the Poga pins, like those test fixtures, they're like, they're $50 in China. So all you do really like for those people that don't know how to get those, that instrumentation, what you do is like, so, you know, at least for me, I have luxury of going to Shenzhen, but you just take your PCB to Shenzhen and you go to the stand, like the stand in the electronics market that does the Poga pin fixtures. And then you just, you just take a red marker and you highlight all the holes that you want the Poga pins to hit.

**Chris Gammell:** Oh really? That's awesome. They don't even like, they don't ask for gerbers or anything. They just do it manually. They're like, we'll figure it out.

**Akiba:** Um, yeah, yeah. You just give them, and you have to give them the PCB because they'll measure it themselves. Yeah. Okay. And then use that to test it. But then, um, but yeah, and then you pay 50 bucks, like $50 and you get a test fixture and then that's a full text fixture with a, and just a bunch of wires coming out for each of the Poga pins. And then you connect those to whatever. And so I would probably connect it to either like sub, normally I connect it to a microcontroller and I'd have like a test routine going, but like if the analog discovery, um, like I think it'd be interesting to play around with the analog discovery because it might be interesting to check out like, uh, say, uh, like, uh, voltage levels and

**Chris Gammell:** things like that. Yeah. Yeah. Yeah. Right. If you put like a mux on board or something, so you can actually switch or like an analog, uh, switches and stuff like that, you can make a little matrix board or something.

**Akiba:** Yeah. Yeah. And just, just so people know, I have no affiliation with the analog discovery. I, you know, I, I, you know, I'm not sponsored by it. I'm not trying to pitch for it. I'm not either. It's a partnership. But it does sound interesting and, you know, and it is, it is an open, open source solution. So like,

**Chris Gammell:** that makes me really curious about it. Yeah. Well, and, uh, so like when Nausman was on too, we were talking about like, like he's doing kind of like software scripting to like RF spectrum, right? And so now like, if this is that same kind of thing for like, to like test equipment, that's interesting. And like, but like, that's kind of what we want. Like we're in the age of like, there's a lot more software talent and you can get a lot done when you, you know, have software talent, you can script that kind of stuff versus, you know, like having to do it all traditional way or having someone flip switches or whatever. Right. So all that stuff has a lot of benefit.

**Akiba:** Well, I feel, I feel like, I mean, if you're an engineer, then it's not really a matter of having software talent. I think being able to write software should be a tool in your toolbox. Like you need to have, you know, maybe like, it depends on what language, like I would say C or C++ is kind of a basic for the firmware. Like you need to control your own firmware if you're a hardware engineer. And also I think, I think Python is a really useful tool for, um, just like, it's, it's like, it's a super awesome, yeah. Yeah. It's like, it's the interface. It's the glue tool that, you know, like when you need something quick and dirty, you just like, you know, throw a bunch of Python at it.

**Chris Gammell:** Right. Right. Yeah. You could shove it into like a spreadsheet or something then too. And that's nice.

**Akiba:** Yeah. I mean like, like converting text files or like parsing text files and like, you know, like things like that, then it just, it just makes so much more sense. Like converting text files in C sucks. Yeah. Yeah. It does. Oh yeah. But anyways, yeah. So just, so I was getting a bit preachy there, but you know, just like just saying, just saying for all you young engineers out there. Right. I know.

**Chris Gammell:** But it's, uh, and so are you doing test stands now or now for your stuff?

**Akiba:** Yeah. Yeah. Yeah. So I have like, I just got another one in, um, like for, and like, these are just like the, I mean, these are like the standard test stands that you would use, that you would use in a production factory and then, but they're just so cheap. I mean, they're like really. 50 bucks is really cheap. Yeah. It's just, it's hard to explain. Like people don't really understand that like, like that stuff is just available. And so like, I see a lot of people making their own test, test stands, like laser cut, et cetera, et cetera. And then, but like, um, in Shenzhen, they basically have a template and all they do is they modify the thing that holds the pogo pins. So like, you know, it already has the toggle clamp and all the

**Chris Gammell:** wire. Oh, really? Okay. So what do they do? They just like mill out or drill out the, um,

**Akiba:** the different pogo spots basically. Yeah. Well, they'll, uh, they have like a seat. Normally, I think they have a CNC drill and a CNC machine and they just mill out whatever to hold the circuit board. Like, so there's like the outline. Yeah. Yeah. There's a stabilizer and, um, alignment pins to hold the circuit board. And then there's like the pogo pins, which go up and those are, those are the main things. And that's, that's why it's so cheap is because the templates, like the rest of the framework is already there. So they're not starting from scratch each time. Right. Yeah. Yeah. Yeah. So, so anyways, you know, uh, so when you do it though,

**Chris Gammell:** you're saying that you, you have a micron board that you actually then write, you go and write

**Akiba:** separate firmware for or something. Uh, yeah. Yeah. So then you just have like, you just have feed that into a microcontroller board and then you'd have like a pass fail criteria.

**Chris Gammell:** Got it. Cool. No, that's, that's not bad. Right. I mean, it's just that you got the overhead

**Akiba:** of having to write the firmware for it then. Yeah. I mean, yeah, it's like the test, like, you know, like the writing, the test software is, yeah, it's part of, part of everything too. That's like just another, another tasks to throw onto the pile when you like, right, right, right. Yeah. But, but it's really interesting. I think like, um, and I feel like, I feel like, you know, like I guess running a business is, it's a lot of work, but, uh, you know, I'd recommend it for people like to learn it as soon, as early as possible because it's, it's useful. And then I just, I think, you know, it's like, oh, I don't know. It's, I think it's like, it's, you're saying it's another skill though. You're saying that that's

**Chris Gammell:** another skill to work on and, and that it will pay dividends later. Right. Yeah. I mean,

**Akiba:** like, I think, cause I don't want to worry, like, you know, like when you're an engineer and, um, like right now at like, like I'm, I'm 43 and so I'd be considered an old engineer. So I tried to work at Silicon Valley and then I'd be like, oh, is there like age discrimination

**Chris Gammell:** or whatever? But yeah, but you look like you're 23 Akiba. Come on in. Uh, not really.

**Akiba:** Not really. Like you must be referring to my rippling muscles. Yeah. That's what it was. Yeah. It's all those vacation photos. That's actually not true. I'm like, I'm getting, I'm getting really flabby, especially after the, uh, your vacation. Right. All the, all the Spanish wine. Yeah. But, um, I mean, it's, you know, like I don't, but you know, for me then I just focus on like kind of designing, designing, um, like designs that I think that I want to do or that like, you know, that I think can, can, can do well in the market. And then I don't, I don't need to worry about all that stuff. But the other thing is like, you know, when I, you know, I'm, I'm doing what I enjoy doing. And when I'm, you know, 65, 70, I'm still going to be doing what I enjoy doing. And I think that's really important.

**Chris Gammell:** Sure. Definitely. Cause why, and I think that a lot of like, I mean, that kind of ties into like lifestyle inflation and stuff like that too. But, but like what you said, when, when engineers kind of age out, right. Like they, they usually go into like management or whatever and they move up in, in companies, but man, it breaks my heart too. I see like, I see like formerly really talented engineers taking on like, I have one very specific example of like this formerly very talented engineer who took on a management role. And then he just kept taking like progressively worse roles because he, his lifestyle inflated to, you know, to, to match the salary. And it's like, he goes to somewhere new and it wasn't the best option for his life, but he, you know, he had to chase the money effectively to maintain his lifestyle. And it's like, that's a nightmare, you know?

**Akiba:** I, yeah. I mean, like, I think for that, that's a different, I think that's a different topic, which is like engineers that go into management because like, um, like, cause man, like management might, isn't a very portable skill. Like, you know, so you can be like, you know, like,

**Chris Gammell:** So if you're a manager at like an agricultural tech company, it doesn't necessarily translate to like, uh, automotive or something like that even, or you mean within outside of tech then?

**Akiba:** If you're a manager, like say IBM or something like that, and then like, you know, you, you're, you're managing people, but you're also dealing with all like kind of the politics and stuff that's specific to that company. Oh, sure. Yeah. And then like, when you change to a different company that, you know, you can get placed into like, you know, like maybe another large company, but then you have to relearn everything. Right. You know, I don't know. I just, I'm just like, I I've seen, I've seen the grind and then like, you know, and people kind of job hop all the time, but just like, you know, I, I'm, I'm a designer. So like, I don't think that I'd, I'd want to be like, just, um, I'd want to at least deal with like full-time corporate management. Right. I do, I do understand like having to manage, uh, certain things. Like when you're manufacturing stuff, you have to manage the factories and.

**Chris Gammell:** Oh, sure. Yeah. Right, right, right. Well, I think, I think the, the, the main thing that you're talking about, it, it, it sounds like to me at least is like, regardless of what you end up doing, it's like, make sure that you're focusing on skills that are, you know, useful to future roles. And so either as, you know, running your own business or making it portable enough that it could, you know, work within different places, that kind of thing. Right.

**Akiba:** Yeah. I mean, actually, cause my girlfriend reminds me of this too, that not everybody wants to run their own business. And so like, I think that's, yeah, it's, and it's not, it's not easy. You're taking a lot of risk all the time. And so, you know, you just become more comfortable with it and you learn how to manage it. But I think, um, like it is like, I, I have like, I have like this, uh, an aversion to authority. And so like, I'm not, I'm not an ideal, like kind of employee. Like I never felt comfortable at companies. And so I never felt secure. Whereas like having my own business then is the boss. Yeah. Yeah. Yeah. Yeah. I'm like, I'm kind of an asshole boss, but still, I'm like, Oh, I hate my boss, but that's me. I was going to ask, do you, do you have employees or no? Um, I have like, so I have people that like, sometimes I, I, when I need help that I would contract stuff out, but like, um, I don't really have employees. Like I don't have anybody that like kind of relies on me for a salary. Got it. So I do like, I have a very small operation and then, um, and I like, and I take care of everything, almost everything myself. And then, um, like, yeah, I, I like to, like, I think it's possible to actually grow, grow, um, grow a company with, and actually minimize like, or not needing employees up to a certain point. And then like, and then I'd have to start thinking about, you know, about it. Cause like right now, like a lot of logistics and you can, you can, uh, farm out. Yep. And then, um, which is like a big part of like, say running like my operation, which is an online, online shop is just logistics. Right. And then the manufacturing, you could farm out the testing. Um, I would either, the testing, you can have it done at the, uh, manufacturer, but, but I like to do it in house. You don't trust them. Yeah. I mean, that's healthy. Yeah. I mean, yeah. So I, cause they, they'll say something, but then I would have to double check anyways. So, you know, so I'd rather just like test here and then, but I mean like at a certain point, then I think the administration would get to the, you know, we get so that like, you'd have to, you'd have to actually maybe hire somebody, but I think there's already a lot of services that

**Chris Gammell:** are available that, you know, right. I think we are entering an age where there's more, more of that on demand type stuff that really does enable, you know, the, so well, solo engineers, I have an article in the queue that's supposed to be published in about that. So.

**Akiba:** Oh, I'm interested to, I'm interested to read that one. Solo engineers. Yeah. So, I mean, yeah, you'd have to actually, I guess if there were, if there were some place, some gathering hole where people could like kind of swap stories and talk shop, hint, hint, then, uh, you know, maybe, maybe we can form like kind of a support group for solo engineers that there might be an article for or something, hint, hint, but, uh, no, but anyways. Okay. Yeah. But yeah, it's like, it's actually just kind of knowing what resources are available and so, but there are a lot of resources.

**Chris Gammell:** Yeah. Cool. Well, uh, wait, so you're back now, you're back in Japan. Oh yeah. Working on your own stuff again for now. Is that kind of the.

**Akiba:** Yeah. Yeah. So, um, I, cause the world bank stuff tied me up for, for a while. And then there were like other kinds of contract projects that tied me up. And also I think I was trying to, um, let's see, I was trying to do too many things at one time, whereas now. No. So I feel like, I feel like now I've kind of, I have more, you know, I have more focus and I have more like sense of what I want to do. And so I'm going to.

**Chris Gammell:** Time to get back on Twitter, man. We can ruin that quickly.

**Akiba:** I think. Yeah. It's actually, yeah. Twitter, Twitter, Twitter is nice. Cause like, I think all the, all the tech nerds are mainly on Twitter. Cause like if I check Facebook is more like my family and you know, and stuff. And then Instagram is Instagram. I'm still trying to wrap my head around. So I don't really understand how, how it's used.

**Chris Gammell:** I, yeah. You know, Dave started using it too. I finally convinced him to use it, but he actually, he's, he's smart. He tied if this than that so that it tweets out his photos and stuff like that.

**Akiba:** Oh, okay.

**Chris Gammell:** It's like a content hover on pictures. That's the way to think about it. I think.

**Akiba:** Yeah. Yeah. But I mean, people have like these massive hashtags, like hashtag everything. And so like, I don't like, what's the purpose of that? So I'm still trying to figure all

**Chris Gammell:** that out. But, um, I wouldn't work too hard on that one. But I mean, I think like right now I'm,

**Akiba:** I'm also trying to do more, uh, in person, in person stuff like workshops, workshops, um, organizing talks, like creating, like basically organizing a community around like kind of actual applications of internet of things rather than, um, then take the technology. Yeah. So that's great. That's great. Yeah. So that's, that's kind of at least

**Chris Gammell:** where I'm headed right now. Cool. Well, you could, you could set up like a, a, the, the Akiba school of IOT out of the farm or something, you know?

**Akiba:** That'd be, yeah. With no students. But, um, yeah, I don't know. I, so I, I think it's interesting. Like we live, we live in an amazing time. Like, like technology is dirt cheap and like people don't understand like, you know, like the arm arm, was it the 30, 32 bit Cortex M3 is, is like under a dollar. Yep. So, you know, it's nice. Yeah. I'm, it's just like the, the cost of technology is like, is amazingly low and, you know, and really I think the main barrier and the cost of equipment, like when I was a young engineer, I dreamed about having my own lab.

**Chris Gammell:** Like today, everyone in their grandma has their own lab. So. Oh yeah. Oh man. I was, I, uh, I was, you know, trolling YouTube again and I ran across an interview, beers and Akiba's workshop. Oh man. What a throwback. Akiba talking about specula. Oh yeah. Yeah. The specula. Yeah. That was,

**Akiba:** that was trying to, um, that was when I had the weather balloon project and I had to get a circuit board inside a weather balloon. So then I went to the, um, I had to go to the sex shop in Akihavara and ask them, like, I whispered like, do you guys have speculums? And the guy's like, for the front side or the backside? And I was just like, oh, oh, backside please. And then, um, yeah. And then that was, that was 2012, man. That's crazy. Yeah. Yeah. Yeah. So that was, that was great. That was like, Ian, Ian came down and he was like, he was checking out speculum. I was like, oh, this thing, you know, ha ha ha ha ha ha. And then, but, um, but yeah, yeah. Actually, I haven't seen Ian in a while. I need to catch up with him. Yeah. So yeah. Yeah.

**Chris Gammell:** Then I want to hear about that, uh, that service, that cable, I saw the cable service they launched,

**Akiba:** the, uh, dirty, dirty cables. Yeah. I mean, that's, that's another example of like things,

**Chris Gammell:** you know, like solving a problem of things that are super shitty. If you're, if you don't,

**Akiba:** if you don't deal with it every day. Right. Yeah. Yeah. So like for those that don't know, like, so Ian runs dangerous prototypes and then they launched the dirty cables service where you can just get a custom cables made. And that's like a huge problem. Like I have to make my own cables all the time and it sucks. Like it just totally sucks. It's just the worst. Yeah. Yeah. Like I don't have like a pneumatic cable crimper. And so like I do it by hand and your hand, Oh, your forearm just lights on fire. Yeah. Yeah. And so like, so like now I just get all my cables like made in China, but then it's like a pain in the ass. So like, so Ian launched the service where like, he'll just do the custom cables and it's like a really nice drag and drop GUI interface to get to make the cables. Um, and then also he has a service that that's really interesting too. Dirty decapping. So you can actually, uh, get, I haven't seen that one. Oh, if you check on the dirty, dirty PCBs website, they have dirty decapping. So they'll decap a chip and then take high resolution photos of it for like $75. So actually that, that's awesome. That's really useful too. Yeah. That's really fun.

**Chris Gammell:** That's good for like when you're buying those, uh, bags of, of, uh, linear regulators, right? Make sure some of the, you can like sample them and be like, are these actually linear regulators?

**Akiba:** Oh yeah. Yeah. I mean like, I don't think people like they wouldn't, I don't think they'd give you fault. Cause I would buy like the, like for the linear regulators then, you know, cause it's such a jelly bean piece of equipment now that like the, you just buy the Chinese parts and like, I don't, it happens, but Chinese people don't knock off Chinese parts that often because like, you know, you start like a trade war, like a domestic trade war and like, you know, and then everybody gets

**Chris Gammell:** screwed. And how much are you really going to save on a 10 cent regulator? Right. It's like, oh, well this was eight cents. Yeah. I mean like, so it's just, you know, so like, but yeah,

**Akiba:** I buy, like I buy regulators by like the thousand piece bag. It's awesome. So that's like, that's like, that's the world we live in today where like a regulator is like 10 cents. Yep. Yep.

**Chris Gammell:** Awesome, man. Uh, so where should people, where should people ping you these days if they want

**Akiba:** to get ahold of you? Um, I think, well, let's see, my website is like kind of messed up right now. So it's like still in transition. Um, and let's see, the web shop is still there. I'm actually upgrading the web shop right now. And then, but I guess, I guess people just ping me on Twitter,

**Chris Gammell:** like, uh, Freak Labs, like Freak Labs. Freak Labs. All right. We'll get them on there one way or another,

**Akiba:** folks. So yeah, yeah. I need to check, I need to check Twitter more. So right now I'm just posting interesting articles, but I'll try, I'll try and like post like, cause the thing is like a lot of details of my life are pretty inane since I live in the countryside. So I don't know. I think you

**Chris Gammell:** have a very interesting life, man. I think what you should do is you should use if this than that, right? And you can bundle it all. So it like sends you a text, but like only like once a day or something, like use that as like a test case, you know? So it does, you know, like, that's the thing, like getting like that every, every time, um, notifications that ruins my day, but if you

**Akiba:** can like bundle it up, that works better. Oh yeah. I, well, I, you know, so I'll check it out. Maybe I'll, I'll post more poop pictures from the sanitation stuff. We've created a monster.

**Chris Gammell:** Oh man. Awesome. Well, thanks for coming back. I'm sure we're going to talk to you again soon.

**Akiba:** Okay. Yeah. Well take care and, uh, say hi to Dave and everyone for me. And also I love the shows with Mighty Ohm too. So like, yeah, like Mighty Ohm is like, is pretty awesome. So I always like

**Chris Gammell:** hearing his stories. Okay. We'll get, we'll get him back on. Maybe, maybe we can, the three of us can

**Akiba:** talk next time Dave can't make it. Oh, okay. Oh, sounds good. Hope, hope to see you out here soon.

**Chris Gammell:** All right. See ya. Bye.

**Speaker ?:** Bye.
