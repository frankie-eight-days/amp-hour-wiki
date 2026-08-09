---
episode: 686
title: A Benchtop Pick and Place with Stephen Hawes
url: https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released January 21st, 2025. Episode 686. A Benchtop Pick and Place with Stephen Hawes. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Stephen Hawes:** And I'm Stephen Hawes from Opulo.

**Chris Gammell:** Hey, Stephen. How are you doing?

**Stephen Hawes:** I'm good, Chris. How are you, man?

**Chris Gammell:** Good. Yeah. Well, you were my second guest on the now defunct Contextual Electronics podcast.

**Stephen Hawes:** Yeah, like five years ago.

**Chris Gammell:** Yeah, yeah. August of 2020. And we'll probably refer to that show here once in a while. I'll have a link for it. But I don't do that podcast anymore. And obviously, Stephen's going to tell us all of the things he's been doing in the meantime. So maybe give us an idea. Where was that? The August of 2020? What was you, Opulo, your company, Lumen, the Pick and Place machine, everything about that sort of thing?

**Stephen Hawes:** Sure. In like the middle of 2020, it was a really crappy open source project for a desktop Pick and Place that I super wanted because I had just done a Kickstarter in 2019 for a bunch of light up bow ties. Uh-huh.

**Chris Gammell:** Stephen did. But what if I had a Pick and Place? Well, what if I built a Pick and Place? I know how stepper motors work. You know, like, yeah. Yeah. You just, yeah. You kept going, man.

**Stephen Hawes:** Yeah. I mean, I think it's definitely a fair amount of naivete. And then also, I mean, well, mostly that, I think. It's like, you know, I didn't know what I didn't know. You need to stop with that. Yeah. I mean, like, as you continue to go, you uncover more things. You're like, oh, man, I had no idea the scope of this thing. But you're already too deep to stop. So it just keeps going. And it's kind of a good thing.

**Chris Gammell:** We all benefit now from you continuing to go, too. So like, that's what we're going to talk about today. I mean, it's a good thing. The lumen has popped out, right? I mean, that's the thing.

**Stephen Hawes:** Yes. Yeah. So I thought this was going to be super useful. And I was like, I want to make this thing. And I was making YouTube videos about it at the time. And I still had like a full time job. I must have if when we talked was August 2020.

**Chris Gammell:** Yeah. I mean, I'm looking just to show notes. It said you were at Formlabs still. So yeah.

**Stephen Hawes:** Yep. Yeah. Yeah. I must have been. And so like six months after we recorded that and like the end of 2020, I had bought a house in Pittsburgh and I quit my job. And I was like, I'm just going to go out there and see what happens. Pittsburgh is way cheaper to live in than Boston, which is where Formlabs was. And I was making like just my mortgage is was like, oh man, it was like a little over $500. I mean, it was like nothing. Wow. Okay. I could I could get away with going full time. I think I had to. Yeah. Yeah. I mean, 2020. Yeah, exactly. I got super lucky with a lot of things, a lot of luck. And and so my Patreon, I think I had like, like 18,000 subscribers or something. I mean, I'd like nothing, but it was enough. That I could give this a try. And I just wanted to like bootstrap it. I just want to make, you know, iterate on it and like help make kits and stuff like that. And then I got one of my patrons on Patreon reached out to me and was like, hey, do you want a bunch of venture capital money to make this thing like go? Oh, and I told him to pound sand because I was not interested in like making it go close source. I wanted to make it kind of like a common good thing and like keep it open source.

**Chris Gammell:** Open source works great with venture. I don't know.

**Stephen Hawes:** Yeah, yeah. There's no examples of that not working in history.

**Chris Gammell:** Right.

**Stephen Hawes:** So I told him to pound sand and he was like, no, dude, like, come on, hear me out. And that guy is Joel Spolsky, who started Stack Overflow and Trello and a whole bunch of other stuff, Fog Creek software. And so I got on a call with him and he's like, I don't, I don't care about cashing out. Like he, the amount of money that he invested a hundred thousand into a company I had not yet started. And like, that's, he just wanted to see this thing exist. Like he didn't care about having a horse in the race. So he invested with what's called a safe note where I can kind of just have still control over it. If we ever do a big venture capital round, he gets a cut or whatever based on how much he put in and the valuation, blah, blah, blah. There's a lot of rules to it, but effectively I could still choose how to steer the ship. And so then it was like, all right, we got some gas in the tank. And then we iterated on the design a whole bunch because it was crazy rough. It was so bad. It barely did anything when we last talked. And then since then it's been getting an office, hiring a bunch of people, shipping a bunch of machines, making a lot of mistakes, making a lot more versions of it. If for the past five years, four and a half years. That's great. But yeah. That's great.

**Chris Gammell:** It's great that we had the starting point and now we have, so we are currently on V4. So maybe we should now say probably what we should have done in the beginning. What is a Lumen pick and place?

**Stephen Hawes:** Yeah. Yes. Buried the lead. Sorry about that. Yeah. Right. Lumen PNP is a desktop pick and place machine. And it is intended for low to medium volume. It's meant for people that are doing a batch of prototypes in house. You know, you're a large company. You have a small R&D department. You don't want to wait 10 days for CircuitHub to get a whole bunch of boards back to you. You can get boards quick turn, even make them in house if you really feel like being speedy.

**Chris Gammell:** Oh, we'll get to that too. Yeah.

**Stephen Hawes:** Yes. That's been on my mind lately. Yeah. And then you just populate them super quickly. And this is not at all what I thought it was going to be useful for at the start. But that's really kind of where I think it makes a lot of sense. So most of our customers are large businesses. They're doing internal prototype runs of a few hundred. Sometimes as few as like 15 or something. Oh, interesting. Oh, yeah. They'll definitely. That's probably more on average about where it is. But I was super bullish on the idea that it was like for what I called mid-scale manufacturing. We're like, you're not sitting in your jammies on the weekends with a pair of tweezers, putting 10 boards together. And you're also not making iPhones and you hire a huge factory, a contract manufacturer to make them for you. You're in this like weird in between where you don't want to put all this cash down for a contract manufacturer. But you still want to make some boards at some reasonable quantity. And that is a blurry line. It depends on your boards, right? Yeah.

**Chris Gammell:** And also complexity is also in there too, which I'm sure we'll get into it. Like board complexity, speed of, yeah, whatever.

**Stephen Hawes:** Exactly. Yeah. So, yeah, that's what it is. It's an open source desktop pick and place machine for that kind of scale of production is what it's suited for.

**Chris Gammell:** Well, again, I've had this thought. Dave, co-host, has also had this thought. He's like, well, I have access to a pick and place and maybe I should get it and set it up. And man, I just always come back to like, I don't really do that much production generally. So like there is that too. I feel like, you know, someone who's like, well, actually I'm all, you know, I've got a weekly order into a circuit hub, macro hub, fab, whoever, whoever, right? Yeah. That maybe does make sense. And, um, hmm. Hmm. Well, let's, maybe let's, I don't know. Should we talk about specs? Does specs matter?

**Stephen Hawes:** I don't know. Like, well, well, so what's interesting about specs is like we, so, so first off, I totally agree with you. Like there is a very specific person that finds value from a pick and place in house. It's not like a 3d printer where like you can kind of just find a reason for it to be useful in any way. Right. Right. Right. Right. You need to, you need to need to iterate quickly on PCBs. You're in a moderate scale of production. If that's not your thing, it's not for you. You know, that's not the point of it. Um, so yeah, that's just kind of the nature of the game. It's meant for a very specific thing.

**Chris Gammell:** Um, but yeah. And then there's like the philosophical piece of like, does it make you iterate more? Because you're like, well, I have the, I have the thing.

**Stephen Hawes:** I mean, yeah, I, I, I love having one. I have one on my desk and I have a whole other separate one in a back R and D room that I'll use for cranking out boards quickly. I also use it for, you know, just R and D and testing use features and stuff, but, um, it's great. It's really, it's, it's really nice to have it for how, how we use that workflow and how our customers have found that it's useful.

**Chris Gammell:** What is the, what is the board? Like what's a optimal board where you're like, yeah, yeah, this is just like right down, right over the plate for this machine. Like, what is, what does that board look like for you? So you've, you obviously use this thing all the time. Yeah. Is it like a hundred 0603, mostly caps and resistors, a couple of LEDs, microcontroller? Is it more complex, less complex?

**Stephen Hawes:** Uh, uh, both directions, uh, of, in terms of. I know it can.

**Chris Gammell:** I'm saying like, what is the, what's the one you're like, yeah, that like hit it. You know, like that's the perfect balance of, you know, like maximum mix of parts, maximum volume. You know what I mean? Like, right. Yeah. You know, when you see it sort of thing.

**Stephen Hawes:** Yeah. Yeah. Yeah. Like, like who calls in is like, here's my board. And I'm like, oh, get a lumen. Like, that's exactly what it is. I'd say it is probably less about what the board is and more about why they want boards. Like for what purpose are they? Cause, because honestly, it doesn't matter that much. If the board is, if, if the board is, you know, 200 of 402 resistors and like maybe a couple other, you know, microcontrollers or whatever, but mostly just a lot of little jelly bean parts, or if it's a lot of big ICs or whatever, I don't, it will change how fast it goes. It will change, you know, the, the manualness of it. You know, we have powered feeders for eight and 24 or excuse me, um, uh, eight and 12 millimeter tape, um, and strip and tray for, for the rest of that stuff. And we're working on wider powered feeders as well. So like mostly an eight and 12 is super home run. Cause it's like as fully automated as you can get. Got it. Yeah. Okay. And also, but that also works out really nicely. Cause 16, 24, you know, uh, 32, 44, all those other ones, how many of those are going on your board? A strip isn't nearly as bad. So we've been trying to find like the optimal stuff to work on to improve things the most. So, um, yeah, I'd say probably eight and 12 millimeter tape by standard. And, but aside from that, it's like, it doesn't super matter what it depends too much on why you need the board, which I know is a very unsatisfying answer. No, no, no.

**Chris Gammell:** That's okay. That's okay.

**Stephen Hawes:** Yeah.

**Chris Gammell:** But you mentioned, oh, where are you saying? I I'm also like, you know, I'm playing this in my mind as we talk. I'm like, Oh yeah. Do I need one? I don't know. I do have a garage now. I don't know. I, I'm, I'm, should it go in a garage? Should it just stay in a lab? Like what is the rush? Okay.

**Stephen Hawes:** Ideally it's not hot. There's a lot of 3d printed parts in it. So, you know, you got to keep it moderately temperature controlled, but yeah, it's, it's robust. It's fine for, you know, I I've had them in garages before. In fact, the very first, when we were trying to start the company out of my garage, my house, we ran all the lumens in my garage. I couldn't get too much warmer than like 45 degrees Fahrenheit. Okay. Uh, and it was fine. It's not big deal.

**Chris Gammell:** Um, okay. So then I know a lot of people don't like to talk about competition, but like, you know, I've used like neoden, I've used like a neoden four. It was, I hated it. I really hated it. Yeah. Well, the software was like, you know, it's like, yeah. Like bootleg windows from event. Like this is many years ago. Maybe they're better now. I don't know what it was at the time, but it was like bootleg windows, like all of the interface, like CAD or not. Sorry. Not CAD pick and place software. I've heard from others and I've experienced at least on that neoden. It's horrendous, you know, like, you know, transmissioning from XY data to whatever the XY is locally. And just like, I, I have no doubt that I would have to become somewhat of an expert, but like where, where are then with maybe with the lumen is like, or sorry, with the opulo. Sorry. No, sorry. It's opulo is the company. Lumen is the machine. Yeah.

**Stephen Hawes:** You're good. Sorry.

**Chris Gammell:** Yeah. Yeah. With the lumen, where, where do I have to like start to have some knowledge and expert capabilities in there?

**Stephen Hawes:** Understanding of how it works. Yeah. The whole process. Yeah. It's, you're super right about like that. I think the reason that software for pick and place machines, especially the big industrial ones is rough is because the, the cost of switching is so high. It doesn't matter how bad the software is. You're stuck with like a, you know, $50,000 machine on the lower end of some of these big things. Like you can get used ones cheaper, but you know, you just kind of have to deal with the software.

**Chris Gammell:** Um, so it feels like that's not where the value is for those companies either. Right. Like they, you know, you go to like a PCB show, right. Where they're, you know, they're all, all the booths are next to each other. And they're talking about specs of like transit speeds and like parts per hour and like very mechanical things and not like, Oh, friendliness of software. Like, well, you're going to have to figure that out. Or we have an FAE that helps you figure it out. Yeah. But it's always like the expectation of like white glove, like hands on. Yeah. We'll make it work for you. Not like everything has to be unified. Right. Right.

**Stephen Hawes:** Which is because honestly, the person making the decision about buying the pick and place cares about how many boards they can crank through and not if the poor tech hates their life trying to use the software, you know, like it's, it's an imbalanced priority structure for, for how they make the software good. So, but it's a little different with us because typically the people who buy it are also the operators. Um, and also we don't want to make people go through a hard time. It just stinks to have to deal with. Yeah. Um, there's an awesome piece of open source software called open PNP, uh, which is like, it is like the Swiss army knife of pick and place control software. You can kind of persuade it into controlling mostly anything. Um, it's very unopinionated and that's really cool. Like there's like in their discord, they have a whole thing about like converting Neodens over to open PNP because software isn't good and all that stuff. And there's a whole process you got to go through this whole thing. Um, so the Lumen runs on open PNP and because it has so many options, that's really kind of suited towards people that are building their own, you know, most people are building their own boutique custom pick and place because they want the challenge. They think it's fun and open PNP is like just, they're Steven further, further down, further

**Chris Gammell:** up the chain.

**Stephen Hawes:** And maybe don't have aspirations to sell it. Maybe do, you know, whatever it may be, but they, they want this software is great for them. Um, and, but then now we have this thing that's very stable and, and a lot of the settings in the software are not things that are, we have hardware support for, or that we do, but we're doing it a different way or something. So we, we've, uh, we provide like the configuration to make it as much of like the, the it's encoded into a Lumen as possible when you boot it up. And then we just walk you through the whole process of going through Cal. I've made a bunch of calibration videos. I actually, Chris, I used a bunch of your, um, series on, uh, KiCad, like going through like contextual electronics videos as kind of like a North star and how to do some of those. Before I was like getting into that, I was like, man, cause I remember those. I mean, I, I watched this so much like early, early on learning KiCad stuff when I was a, we taught and I was like, yeah, that's the energy I want. You know, I want a little bit of that, those vibes. So yeah. So I went into, um, just making a whole bunch of tutorials and stuff and just walking people through the process because a pick and blaze is not a simple machine. There's a lot going on. Um, so we, we try and kind of distill it down to like the fewest things possible to kind of get you where you need to go.

**Chris Gammell:** Got it. I mean, it does feel kind of like, uh, yeah, there's not, this is going to sound bad, but like the rep wrap, you know, like you guys are kind of moving into that, like rep wrap of the pick and play space. You know what I mean? Like, I feel like rep has its own stuff in there, but like you're open, you have a community built around it. There is this, you know, kind of interoperability. There's people that are modding and changing whatever. Um, but then I guess the, the stuff in the back of my mind with the rep wrap thing is like rep wrap was not easy to get booted up with. And then like you worked at form labs, form labs built a, you know, kind of competitor type of thing, but also like, it's just, it got easier. Like as the 3d printing industry kept getting more and more easy, the software got more, um, user-friendly, which is great. Right. So like to the point where it's like literally like I open up, I've I'm a Prusa user. Like I have Prusa slicer. I drop it on there. I dropped it to the Octoprint. I'm done. Right. Like, right. Yep. Yeah. Great. So like, how far away are we from that?

**Stephen Hawes:** Is that a thing actually with pick and place? It's, it's close. So there, there's definitely more considerations as opposed to like, if I have PLA and my printer and I just bop it into the slicer, the slicer is going to be crazy intelligent. It's going to set that up. It's going to kick it out. You don't even have to think about it. My, my dad just bought a 3d printer and he's a lawyer and he's been having so much fun with it. And the barrier to entry was so low. It was, it's been really cool watching him dive into it and like see his perspective on the ease of getting going with this thing. He's never had a printer. He's watched me play with them for years, but like he just bought one of his own volition and he just sent me a picture of him with a printer. I was like, it was, it's been very cool to see him go through the process and learning a lot about that.

**Chris Gammell:** I'm just, now I'm just curious about the. What was it? The life stage of a lawyer.

**Stephen Hawes:** I don't exactly remember. I mean, I was home for Christmas. I have a lot of lawyers in my family. I would love, I want to get them into 3d printing. That's what I'm trying to get. It's almost completely not related to 3d printing. All the things that he prints, like he's printing Christmas gifts. Like, you know, the, the, the, uh, stereotypical three stages of getting a 3d printer. First you print a benchy. Then you print like the articulating gold dragon. Exactly. Yeah. Yeah. Yeah. And then you design your own stuff. And so now he's dipping his toe into Tinkercad and he's kind of going into this process and starting to see that. Oh, I can just make a print for this. So that it's definitely not there yet because it's more, cause it's, it's still earlier on in that period of time, but it's also not, if you are making a board and you're familiar with designing circuit boards, it's not a problem, you know, like it's, it's not that hard to get going with. Um, but, but yeah, like I do think a lot about like when I got my solid doodle to pro when I was a sophomore in college, I booted up. I didn't even remember what the heck it's called, but it used slice three R and it was, it took me five hours to get my first print. And I was ecstatic about that. And like, what is that arc looked like for the software pipeline? And like a lot of what I think made it tricky was that it was a lot of community members working on incredibly cool things, but like the UX wasn't considered. And then you have a company like Prusa that comes in and puts a lot of, you know, product manager energy into thinking about the UX and doing studies on those things and putting the money into the open source thing to make the whole experience feel better. That's incredible. And I think that's how blender has been really successful. They have the whole foundation. They have a direction. It's not a group of people. It's like, it's a concerted random group of people. I should say it is a group that has structure and a concerted effort towards a goal. Yeah.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Um, and that's what I want to bring to this space is like being the company energy to try and create this open source effectively Prusa slicer, you know, of, uh, it's an open source thing that's still led by a company that's shepherding it into a, not kind of a UX mess, you know? Right, right, right. Yeah. Right.

**Chris Gammell:** Like literally it was like, I think it was like X, Y there was like two columns in like a bootleg spreadsheet, like tool in a windows, windows, windows XP box. That's like my reference point. And it was like, well, zero, zero is not where you think zero, zero is. And then you got to translate and flip and like, oh, you're on the backside. You have to do math yourself, you know, like that kind of level of things. And I'm like, I don't, so I don't want to do any of that stuff. So then, okay. So now if I, so I get a lumen as I'm sure many of our listeners are going to want to do, uh, and we'll have links for all that stuff. Um, excuse me. Um, if I get a lumen, I follow tutorials, do open PNP. Yeah. What does that process look like? So I'm in key cat. I have a board. I export X, Y, I put it in to open PNP. Like what is the setup steps then? Like what's that process look like?

**Stephen Hawes:** So there's kind of, there's kind of three chunks to it. The first one is calibrating your machine. So open PNP knows one of the most key measurements in the machine is your top camera to nozzle tip offset. It is on the vision plane. What is your X, Y offset from the center of the camera's field of view to the center of the place where the nozzle touches? This is key. Cause when you do your fiducial cal, you find out where your board is, where everything should be camera in camera space, but in real world space, you have an offset to your nozzle. So when you're going to place your part, you need to keenly be aware of that number. That's one of, I think there's like six or seven really key numbers that you have to have in there. So the first step is like getting your machine caled. So that's what the videos and the docs walk you through. You do all these things. It's just a, you just follow the instructions. Do you get it? And it's every lumens, you know, 200 microns off a little bit in some other little metrics. So, you know, you gotta, you gotta go through that process. We can't do that whole thing. Uh, here, here at the, um, the office. And then you go and you set up your board and then you set up your feeders. So if you're using, we have a powered feeders, eight mil, uh, eight millimeter tape and 12 millimeter tape. If you set those up, it's easy. We added a, uh, a feature to open PMP where it will automatically scan for all the feeders that are loaded. It remembers what part you have loaded in them. You can swap them around.

**Chris Gammell:** I do remember you have, you have videos about when you started doing the EEPROM on all the feeders and all the powered stuff like that. It was a lot of fun to watch that happen.

**Stephen Hawes:** Dude, what an arc that whole thing was. That's the most fun. People are saying you should do addressing of the slots in this way is such a fun conversation and everyone has a different take on it. And like, well, okay, it gets a little long in the tooth, but you know, I have a, uh, in the GitHub repo, I have a folder or a file called design decisions where it explains why we did what we did. That's smart. And I asked that people read that and if they still disagree, great. Then I want to engage with that.

**Chris Gammell:** But, um, man, you have a lot of patience. This is the thing about like community projects too. Like you, I mean, you benefit from the community, but like also you have to kind of corral, you know, people on the internet have feelings.

**Stephen Hawes:** Yes, they do. Yep. But you know, it's really hard. It is a constant challenge to the ego. You know, it's like people, people tell me, Steven, you're stupid. Like this is super stupid. And sometimes they're right. And then I know, I know, like it would be nice if they were kinder about it. But when they do that, it is like such a, it is a gift because it's, it's making me go, am I like, should I consider this approach? And I find a lot of value.

**Chris Gammell:** So method is, method is rough, but you're saying you appreciate the, the donated knowledge at the end of the day. Tremendously.

**Stephen Hawes:** Tremendously. I, I, I, it doesn't bother me if people call me names, making YouTube videos and open source community stuff. I've gotten so much of that. I just, yeah. Like it just doesn't affect me. That doesn't bother me that much. But, but when they give actual feedback, it's like, oh great. Thank you for this little nugget of knowledge I can use. I it's, it's great. So yeah, it can be rough, but it's also like I signed up for it. You know, it's far for the course.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Stephen Hawes:** Okay. Yeah. But yeah. So then you set up your feeders and you can get strip feeders too. If you don't want to spend the money on powered feeders.

**Chris Gammell:** Also, could you, it's all define strip feeders in that context.

**Stephen Hawes:** I'm sorry. Yeah. Strip feeders are literally just a little 3d printed bracket that holds the tape. It's very not nothing fancy. So what you do is you load the tape in, you effectively peel the film back and then open PMP knows to just kind of do a dead reckoning offset or even find the tape with the camera and pick the parts from there. Oh wow. And, and yeah, so you can do that too. If you don't want to pull the trigger on feeders, there's also a ton of open source community feeders. And there's also we sell the parts for our feeders, the hard to harder to get parts. So you can build your own. We have a ton of people that buy feeder kits. They buy all the motors and like the motherboard and stuff. Or I think it's, I think it's a motor in the wheel is what we do because everything else is pretty easy to get. And people build their own feeders and like, so there's a million ways to like set up your feeders, but you do that and we walk you through the whole thing and then getting your board imported, which is pretty easy to do. You import your, KICAD puts out a .pos, a position file. You import that.

**Chris Gammell:** All my boards are POS.

**Stephen Hawes:** Dude, every time I see that, I have a laugh. I'm like, I know it says position, but that's a POS file.

**Chris Gammell:** Yeah. Yeah.

**Stephen Hawes:** And, and you drop it in and, uh, you know, set your position and all that stuff and, you know, tell it where the board is. And, um, and then you should, should really workflow in, in open P and P is kind of like

**Chris Gammell:** helping, helping in that way. Kind of.

**Stephen Hawes:** Yes. I think if you're just kind of diving into it with a machine that you don't have a lot of instruction on, there's a lot of reading to do. There's a lot of figuring it out, but people that buy a pick and place to make some boards in house, they, they want a tool and not a project. They don't want to have to learn all the ins and outs of open P and P. They just want it to run. So we do as much as we can to like, just give you what you need to like run the job. You know, that's what most people want.

**Chris Gammell:** That is exactly what I was. Yeah. Hoping for. Yes.

**Stephen Hawes:** And I also, to be super fair to open P and P is a very cool piece of software. My buddy Tanner runs an S and T line in Ohio, just across the state line from us. And he runs a bunch of big, crazy, wacky machines. And he thinks open P and P is an absolute dream. And he's coming from the really other weird, complicated stuff. So, you know, if you're coming, if you're used to like a slicer, a 3d printer slicer, it's going to feel different. You know, there's a lot more options that it may not explain it to you. And that's why we kind of put the guard rows on. But if you're coming from the other stuff, open P and P is a revelation. You know, it just depends on your context. Right.

**Chris Gammell:** So it's almost like the standardization. I'm sure for someone like Tanner is like, yeah, it's all the same. Now I get to, you know, the machines are different. The capabilities are different. But once you tune that, it's kind of like a abstraction layer across pick and place machines as well.

**Stephen Hawes:** Yeah. That's a cool way to say it. Yeah. The configuration is just a, it's a shim layer to still have the same API with how do you control the thing? It's just different interface to actually control the machine underneath. Yeah.

**Chris Gammell:** Well, that's, that's good then. That's real good.

**Stephen Hawes:** Yeah. Yeah. It's a super cool project. It's, it's an awesome piece of software for sure.

**Chris Gammell:** Okay. So if I go in, if I go and buy now on a Lumen P and P V4, I get a five pack of eight millimeter feeders. No. No.

**Stephen Hawes:** You don't get, you don't get five pack of eight. Oh, sorry.

**Chris Gammell:** Add to cart. I didn't see that. Sorry. Sorry. I don't want to misstate. I'm going to, I'm going to spec this thing out. So what is in the, what is in the, when I didn't buy, so the pick and place itself is the camera head, the moving, the pick, the, it's like. Is the base machine. The chassis. Yeah, exactly.

**Stephen Hawes:** It's the base machine. And it's also enough that you can get going. You don't need the power to feeders. They're highly recommended. Yeah, of course. Of course. Because feeders are like, if you have a bunch of little jelly bean parts, it's just not the move. It's, that's why we made feeders. Like people are like, please give us feeders. And we, yeah.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Stephen Hawes:** But yeah. So that's the, the base machine. We get you a little getting started, get a little test population board, a strip feeder to get started with. Um, and you can print a lot of strip feeders, uh, yourself to all the, the files are online. So you don't have to pay us for them. We have them for sale on there for, for a bit of money, but they're, you know, most people just print them, you know?

**Chris Gammell:** Yeah, I see. Okay. All right. Yeah. And then like, uh, so if, so I buy the machine, it arrives, I get it configured. Um, I maybe print a couple of strip feeders. I set up for, I don't know. Again, I was like trying to like have a, a board in mind that I've done recently. That would be a good fit here, but I, I think, well, I guess, okay. So now let's talk specs, I guess. Okay. What is, what is the minimum I can do? Like, so I have, I have a board with like a bunch of, I have some BJ modules. I have, you know, some old four or two is like, okay, no problem.

**Stephen Hawes:** Yeah. Yep. Uh, we, we go down to a four or two passives. Um, we do 0.4 millimeter pitch. I sees like a cuff and TKP stuff. Um, yeah, no problem. We have had people say they've had great luck with 0.5 millimeter pitch BGA. Um, which is really cool because BGA was like not originally on what I was even thinking about. Um, but yeah, people use it for BGA all day. Um, so yeah. Oh, two Oh one is very much not something that we're most people don't want it. I don't want that.

**Chris Gammell:** I can't rework a board at that point without, you know, like I'm not, I'm not good. That's just, I'm not too much at electronics.

**Stephen Hawes:** It's like the, uh, the soldering challenge that, uh, super con, you know, I think that goes down to a one, right? It does.

**Chris Gammell:** Oh yeah. Maybe smaller. I think there's a, I think it does go like insane mode that maybe goes smaller than that, but like they're doing it in the dark with like a soldering iron that's been used by 20 other people.

**Stephen Hawes:** It's like a big, you know, yeah, exactly.

**Chris Gammell:** It's amazing that they're doing that, but I just, it's so that is not me. That is not me. Same. They're doing with unleaded solder. Like what are they doing? Yeah. Yeah. Yeah. That's okay. So that's, it sounds like, I mean like a lot of things and even still, I mean, I guess I could always stencil, you know, you could always stencil on something smaller and then, you know, try and hand place like a small BGA or something like that. Or, or, yeah, absolutely.

**Stephen Hawes:** And you know, some people will, if we support like 50 powered feeders on the machine, um, and you can put more strips on. I think the, if you max it out, you, and your board is really tiny. Like it's, it's really max scenario. I think you can get up to like 75 unique parts or something like that. It's, it's packed, but up to 50 is like the real comfy spot with power feeders. It's some people that have a few more than that. They put a couple of parts on with tweezers afterwards. If they're like, I mean, this has taken the edge off of making a bunch of boards. Most people, it's just full population. It does everything. But you know, if you get 95% of them done, it's not the end of the world.

**Chris Gammell:** I mean, if you just got zero ohms, 10 Ks, one K, you know, like just like get the high runners. And then, yeah, like you said, you know, do the other placements. Yeah. Probably would be helpful. Yeah. Yeah.

**Stephen Hawes:** Yeah. So that can be super nice with it is, um, you know, yeah, there's, there's, um, my buddy Seth has been, he has a lumen and he's trying to like scope out. Can I only design boards with this set of parts? Like when you, exactly. Like when you design a 3d print file, you're thinking about print orientation as you design it. So there can be design constraints for this too. They're going to be a little more strict than, you know, what you get at a fab, right? When you're actually going to a CM for sure. But if you design around that, oh man, I mean, you can just iterate. So he's like trying to keep his part count. He's like, I, this is my microcontroller. This is what I use for my microcontroller. The one microcontroller. Yeah, exactly. So it kind of an interesting thing. He's, he's kind of experimenting with that idea right now. It's kind of cool to see him play with it.

**Chris Gammell:** I mean, you guys are like the mid to low end on price as well. So like, have you started seeing people where they, I mean, you have a photo on your, I think on the product page for the lumen where you have a couple of, um, uh, lumens next to each other. Or have you seen people who are like buying multiples and then just keeping set up so they can, instead of switching out feeders, you just move it to the next machine sort of thing. Is that, yeah. You seen that?

**Stephen Hawes:** Realistically, that's what most people do. Like sometimes people will be like, Hey, I have a board with like 90 parts and we're like a second lumen is going to be way better than trying to squeeze it in this one. And like, it's going to be, it's, you're going to have a better time with it. And so they get two lumens and then you put them next to each other. That photo that you're looking at is one of our customers that he bought a V2 when we first launched in early 2022. And then he bought a V3.0 and he bought a 301, a 305, a V4. Like he just keeps, yeah, it's, it's really cool. And they'll send us pictures of his line and he just has like a whole production line set up with like every gen of lumen we've ever made.

**Chris Gammell:** It's very cool. That's, that's really nice too. Cause then that, that person is also going to be doing like regression testing for old hardware. Like, Oh, V2 doesn't run the newest stuff, right?

**Stephen Hawes:** So yeah, exactly. Well, so what we do, we actually kind of do that ourselves. We have a, what I call our Mars rovers at the office. So when JPL makes a Mars rover to go to Mars, they don't just make one, they make two, one to actually send to Mars and one to keep a JPL that they test all their software on. Cause if they're going to send something that bricks it, they don't want to do it to the one on Mars. So every major release of the machine, we keep at least one version of it. So if I, for example, V2 came out, we didn't have a feeder support when we started selling V2 of the limit, we didn't have feeders, but I kept a couple of V2 so that when we had feeders come out, I could test all of it on original hardware. Make sure it was all going to work the way we expected to. But yeah, he helps us with that too, I guess.

**Chris Gammell:** You should do it like, you know, like the whiskey makers, they also do that where they're like, they keep a couple of casks aside and then they, you know, they could sell it later as the really, you know, the 50 year, right? The 30 year. So you could sell a V2 in like 20 years and, you know, sell it for like 20 grand, man. I don't know. That's a stupid idea. That doesn't work like, like whiskey, but it'd be great if it did.

**Stephen Hawes:** I would be honored if someone for some reason thought they would want an old version of the Lumen like for that much.

**Chris Gammell:** I guess there is actually that in, uh, in fabs, actually there is that sort of thing where, uh, Intel does copy exact. And so you have to buy the same machine, including the same like desktop computer that's inside of there.

**Stephen Hawes:** Right.

**Chris Gammell:** So if you like stockpiled a bunch of like 386s for like some popular machine, like you could in theory sell that in 10 grand for 10 grand someday because Intel needs it and they have to copy exact.

**Stephen Hawes:** Sure. Yeah. It's like the, it's the beanie babies of electronics.

**Chris Gammell:** The beanie babies of electronics. Yeah. That's great. So, okay. So now back to the, the out of the box sort of thing. Right. Uh, so what I, I remember you did a video as well about kind of what's under the hood, what's controlling this thing. So this has its own microcontroller that's driving all the motors. Is that right? That's the interface piece.

**Stephen Hawes:** Yep. Yeah. Yeah. Yeah. There's a main motherboard in V4, the one we just put out in September. There's a control box on the side of the machine that has all the, everything to make the woman do what it does. So it has a microcontroller on board. It's running Marlin that we've modified to support our feeders and a whole bunch of other pickup place operations, our vacuum sensors, all that stuff. Um, there's also a pumps and valves inside this control box. So that's actually what does the, the vacuum for picking, um, and the solenoids for immediately allowing atmosphere to rush back in, uh, to the line to immediately drop the part, all that kind of stuff. So all that's kind of like nicely, literally black boxed into a black box, abstracted away. Uh, so that, you know, that, that's kind of all the brains there. Yeah.

**Chris Gammell:** Okay. Okay. And so that's, so that, and then there's in the head of the, there's two picker, what are those called? Tubes?

**Stephen Hawes:** Yeah. Uh, tube nozzles. Yep.

**Chris Gammell:** Nozzles. That's it. Yeah.

**Stephen Hawes:** Yeah.

**Chris Gammell:** So two nozzles, that's got all the kind of smarts in those as well. There's a camera. There's, there's a camera on the head and another one.

**Stephen Hawes:** Yeah. There's, there's a stepper on the head for moving the two nozzles up and down. Um, to select. Yeah. One goes up while the other one goes down so we can get away with just one motor, keep it a little lighter. Uh, and then they cut, they kind of rack back and forth. Um, on the nozzles themselves, we got hollow shaft stepper motors. So these are stepper motors that literally have a drilled hole through the shaft. So that's actually what we pull our, our vacuum through and the nozzle will rotate in line while also pulling a vacuum through the, the actual shaft of the stepper. So when we bring it over the part, of course you pick the part, it may not be at the orientation. You want to place it on the board.

**Chris Gammell:** So you got to do the, exactly.

**Stephen Hawes:** So you bring it over the camera. There's a bottom camera. It takes a peek at it. You do some machine vision on it and then it figures out how to place it from there. Um, and then also a camera on the head to find the board and homing fiduciary and all other kinds of stuff.

**Chris Gammell:** Got it. So, okay. So we got black box on the side. We got camera on top, camera on bottom. How much like of that is visible to me? To me as a user now of open PNP, I think about it or is it like a home button sort of thing? Like I'm kind of thinking in the context of like a Octoprint or maybe, yeah, like that sort of thing.

**Stephen Hawes:** Like, right.

**Chris Gammell:** How much, how much manual is in there?

**Stephen Hawes:** You don't really have to, once you get it and it comes in like seven parts, uh, and you bolt it together in like an hour. Um, and then once you have it together, you'd, you hit home. I mean, it enumerates like a comp port on your computer. Um, so you know, it shows up, drop, select an open PNP and we walk you through that whole thing. And yeah, I mean, it thinks I really don't want to think about it. It's great. It, you, you really shouldn't have to, unless you're hacking it weird, unless you're doing some cool stuff with it. Like, yeah, then, then it shouldn't be. Um, okay. But it thinks it's a 3d printer. It, it, it really does. It's running Marlin. I mean, it, it, it's a 3d printer with no nozzles, no beds and a way more axes than a normal 3d printer.

**Chris Gammell:** Yeah. Why, why is that just because of the, how it was built up over time? Like why, why is it a, to think why Marlin versus, is it like what a Marlin or custom sort of thing or.

**Stephen Hawes:** Um, Marlin for a number of reasons, it's super stable. Um, and I'm friends with Scott, who's the lead maintainer of it. Um, and he was just tremendously helpful in getting it set up. Um, way easier barrier to entry, uh, than getting all the other, these, these other components of it connected. Um, clipper is obviously the other, the other option and very cool. Um, and something that we, Oh really? I'm sorry. It's like the other.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Okay. Okay. Sorry. I, I, I should provide context. It is Marlin is like one of the most popular 3d printer firmwares that exists. Um, most printers are running on that clipper is kind of like the new thing in the market that people are using. Um, and it, it's good for like distributed processing. So, uh, instead of like a microcontroller doing all your time steps all together, there's actually like something that runs on Linux that does real time, like packet sending over USB to the microcontrollers and it makes sure that over USB, all of those are synchronized. Well, so you can like, you can have a microcontroller on the head that is still synchronized with the microcontroller on the base. Even though there's several microcontrollers, you're still making sure those steps are in sync. So that's kind of the, the new hot. Okay.

**Chris Gammell:** This is sounding more familiar. Now, this is what Piotr, as in Tempski was telling me on blue sky the other day. He's like, Oh yeah, you know, you should switch. I'm like, yeah, that's great. Sounds great. Cool. I, I am, I am a user of tools, not a builder of tools. Sure. Yeah. I'm very grateful for the people that are builder of tools. Uh, okay, cool. All right. So, but I guess my question was why Marlin versus, I don't know what the other options are. Like why build a pick and place that looks like a 3d printer in the first place is just cause it's stepper motors and kind of look alike and a good starting point. Yeah.

**Stephen Hawes:** I mean, yeah, it truly is pragmatism. Like I am not interesting, interested in reinventing the wheel because it feels like an interesting engineering challenge. Like I don't want to write my own host firmware because I'm not going to do it as well as Scott and the thousands of other people that have contributed to Marlin are going to do it. That's not where I want to provide value. It's kind of like the Nintendo principle, you know, like they will take incredibly old, stable, cheap, old tech and do something interesting and creative with it. So it doesn't end up being expensive for them. It's a well understood development space. I've configured tons of printers on Marlin. I know Marlin. So it was easier for me to dive into there. And I was just truly about how do I get the same placing apart? And that was lowest barrier to entry, easiest access, easiest configurability, at least, especially at the time. Clippers come a long way.

**Chris Gammell:** Does it play nice with Open PMP as well?

**Stephen Hawes:** Yeah. Yep. It just enumerates a serial port. And yeah, that's a good point. It also is fine with Open PMP as well.

**Chris Gammell:** Got it. Okay. All right. Cool. You have solved all my puzzles. Thank you. That's great.

**Stephen Hawes:** There's on that motherboard, we have a couple of vacuum sensors. So we can actually tell what the pressure is in the line. And I've been playing around recently where you can tell when the nozzle has hit something because you can detect a drop in pressure.

**Chris Gammell:** Yeah. Right.

**Stephen Hawes:** Exactly. So what I've been playing around with doing is you can actually take the nozzle and probe a whole bunch of XY positions and capture the Z position it's at. And you can 3D scan with it, with the vacuum pressure.

**Chris Gammell:** It's like the anteater model, you know, it's like ant, ant, space, ant, space. Yeah.

**Stephen Hawes:** It is miserably slow and horribly, like, it's just not the correct way to 3D scan something. But I have been able to, I printed out like a little shape and I scanned it and then I reprinted that back out. And it's like, it does do it. It's very cool. It does. It's nice. That's great. Yeah. But yeah. So yeah, that's kind of the whole spread. We also, a lot of folks are really interested in using it for like weird hacky stuff. Like people will message us and be like, hi, I want to use it to feed my crabs. Can you tell me how to make it do XYZ? And I'm like, what do you, what do you mean feed your, do you want to pick up food and drop it in the tank? And they never responded to us. So some dude is somehow found a way to use aluminum to feed his crabs. I somehow, I don't even know how he's doing it, but.

**Chris Gammell:** Yeah. That's great.

**Stephen Hawes:** Like, yeah, it's weird. It's great.

**Chris Gammell:** And how much would you say, I mean, like, so now percentages of audience, right? So you have a hundred percent of your audience that are purchasers, not like viewers like me. I'm a, you know, a YouTube viewer, but like actual, like, I guess a hundred percent of customers, how many are actually tinkering, modifying machines? Is it 5%, 1%, 0.1%, 0.001%?

**Stephen Hawes:** I'd probably put it at five to 10%. Oh, really? Maybe five. Yeah. The vast majority of them are businesses using it for prototyping or small production runs. But there's a lot of, especially our discord server, a lot of people. I mean, if you're, if you're an electrical engineer and you're going to be interested in doing mods and trying different things. And like, so I, you know, there's also a, there's also like, you know, our customer base is like also more inclined to tinker, which is so cool. Yeah. Yeah.

**Chris Gammell:** That's nice.

**Stephen Hawes:** But yeah, most folks don't, uh, because they want it for a tool, you know, they're not

**Chris Gammell:** looking for the other reasons. Don't mess it up for on a Friday night while you're tinkering with it so that it doesn't work on Monday morning. Right?

**Stephen Hawes:** Exactly. However, there are hundreds of builders that hack the heck out of it and they, they do all kinds of wacky stuff. Um, if you're buying it from us, typically they're hacking at less. That's not patently true. Uh, but if you're building it, oh yeah, there's all these months, there's a wide body mod. When we were still on rollers, we had a linear rail mod. There's all kinds of feeder mods. I mean that we have a whole mods page that just goes through stuff that the community does. So most people that buy it don't most community members that build it definitely do.

**Chris Gammell:** Got it. Okay. Yeah. All right. So now's the part of the show where you should give. All right. So I'm going to pretend that I'm going to try and convince my boss that it would be financially irresponsible not to buy one. So how do I do that? Because like, I was thinking, I was looking at your page, uh, on the product page, it's got like a thing about like, oh, time, blah, blah, blah. But like, yeah. Legitimate, there is a crossover point. I'm not saying it's short term and I'm sure it's not, it's not going to be whatever I would tell a boss that like actually makes sense, but there is an actual crossover point. So where, how do I convince a boss that I should buy one of these instead of sending like maybe let's say, let's be very generous. The next 10 things out to like a, you know, moderate turn PCB house.

**Stephen Hawes:** Right there. Okay. I have a, I have a big thing about, I don't want to sell a lumen to someone that doesn't need it. So I'm, I'm definitely not going to come swinging hard to someone who doesn't need it. I don't want someone to buy it. That isn't going to find it useful. So I'm not going to try and convince you. I'm what I've done is I've made, um, uh, a tool, a web tool that helps you figure out if it is useful. I think it's compare.opula.io and it's a little crappy little website that I coded up that you drop in some numbers and it kind of gives you the gut check of like, okay, with how much time and money you're going to invest, when do you, you know, break even on your ROI of buying the machine? How, what, what's your time worth? I put in like some standard estimates from surveys and stuff like that, but you can always, you can change the numbers. Um, and it's pretty conservative with like speed of lumen and all those kinds of calculations. And it will tell you, you know, like I, I legitimately do not want someone to buy that is not going to find it super useful. So I would, if you were a theoretical person emailing sales at opula.io, I would point you here. I'd ask about your boards. I'd ask how important time turnaround time is for you is waiting 10 days to get boards back a huge pain in the butt. Do you mind getting your 24 hour, you know, 48 hour board turn. And then you immediately put them on the lumen. You have boards, you know, a few hours later, fully populated. If that's super valuable to you. Yeah. I think the lumen's awesome and totally checks your use case.

**Chris Gammell:** Um, yeah, I think one of my concerns is that I'm, uh, I've had a lot of bad luck actually with like paste and reflow. Oh, really? Like. Really? Yeah. I don't know. I think it was bad. It was, it was back when I was at M hub. I had, um, I had like just, I don't know. It was like a bad pace. Like, uh, it was like one of those, you know, like the squeegee beds. Yeah. Yeah. And I just did, I did it poorly. And even when I was hand placing on top, it was, it was problematic. So like, obviously it's isolated from the pick and place machine, but there is that concern too, of like kind of the someone to yell at. There is nice to have someone to yell at, but also like, then you have to do the yelling. So.

**Stephen Hawes:** Yeah. There's, there is another, that's, that's what a great way to say it. Yeah. It's like, if you, if you're, you're still bringing it in house, it's your operation, but you also own the whole stack of it.

**Chris Gammell:** Yeah. Right. Right. But, and if you get to do it again and you just.

**Stephen Hawes:** Yeah. You fix it yourself, which can be nice. Well, that's another problem.

**Chris Gammell:** You asked about the paste I was using. Yeah. Which paste were you? I was using expired paste for a long time. Oh, dude. Oh no. That was, that was a rookie move. That was a rookie move. Um, yeah. Figuring that out was a, a big, a big deal. Um, but yeah. Regularly throwing it out and starting like get new paste. That should be your mantra.

**Stephen Hawes:** Yeah. That is. There are a lot of places where being frugal and skimping is fantastic. And I fully believe solder paste is not one of those. Like it's, it's just so not worth it. We use Loctite GC 10 for everything. And it is just the GC and GC 10 literally stands for game changer. Yeah. It's like, it's just great.

**Chris Gammell:** Uh, this temp stable at, at room temp.

**Stephen Hawes:** Oh yeah.

**Chris Gammell:** Yeah. Yeah. It is. That's, that's the tube I had for a long time, but I had it for so long. Ah, it was. Yeah. Yeah. Yeah. Don't do, don't do that kids. Don't be like me.

**Stephen Hawes:** Yeah. Be bullish on throwing out solder paste. If it's getting rough, it's just not worth the time. It's yeah. Yeah.

**Chris Gammell:** I think on just a regular basis to like have like a calendar appointment, just like every month, just, or like have it like on Amazon auto order or something. Yeah.

**Stephen Hawes:** Sure.

**Chris Gammell:** Write the date on it, throw it out, you know, that sort of thing. Yeah.

**Stephen Hawes:** Yeah. But yeah, pasting is a whole other part of it and reflow, like, um, uh, see on unexpected makeries on YouTube. He has a master pro. Um, if you don't mind, uh, modifying a toaster oven, it's great. You can also get a, uh, control EO three. You can buy them fully assembled. Yeah. They're like, you know, 1200 bucks.

**Chris Gammell:** I think I had the two and the kit and then I just, yeah. You didn't like it. I used it. It's fine.

**Stephen Hawes:** Oh, okay. Okay. Okay. Yep. I've heard great things about them. Um, I, we have a reflow master pro. The Sian's a buddy and, and I really like, it's great. We, we've bought some of the, the T nine. What's the, you know, T nine 32 a, you know, the one that hackaday has the exactly. Yeah. Yeah.

**Chris Gammell:** And that's what, and that's what the, uh, or no, sorry. The, uh, the, the control Leo modifies a toaster, right? The actual like toaster oven toaster oven.

**Stephen Hawes:** Yeah. Yeah. Just like a black and Decker, you know? Um, and that's great. If you use some, it's better if you insulate them and stuff, but you know, I found that's been really good. You know, those in the control EOs are like awesome approaches for a small, perfect scale for like, you just need to crank out some boards to test some stuff, you know, for an internal prototype run. Um, so yeah, those are great as well, but yeah, there's more lumen is, you know, one third of that chunk. You got to paste. I mean, it's the most significant part, I think, but like, you got to get it hot. You got to put paste on it too. Those two comes things. Yeah.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Yeah.

**Chris Gammell:** Okay. Well, skills to build, I suppose.

**Stephen Hawes:** Yep. But no, I will not pitch you.

**Chris Gammell:** More boards, you know, like I got to build more boards to really make, make the case, you know?

**Stephen Hawes:** Sure. Hey, I mean, if it, if it works out, heck yeah. What, what kind of, how many boards are you making in a run? Like, what's your, your scope of like, are you iterating them on, on them quick that you want to kind of get that feedback?

**Chris Gammell:** No, but I do like the, you know, sometimes I want to yell at someone. Sometimes I want to just be the person that I yell at myself. You know what I mean? Like having that ability to like, be like, oh, I can just change this and I have to like do another email iteration, do another zip pack, you know, like just change the file, make it happen locally. That part's nice. I want that, you know, like that, that is a good thing. You know, there's that, that push pull of like having control versus having somebody yell at is like the, is the control axis, right?

**Stephen Hawes:** So yeah, yeah, absolutely. Yeah. Yeah. That's a definitely, that's a reason a lot of people have one and a lot of people that are in full production too, that like use, I mean, we do this too. We make boards in the lumen on, uh, on lumens. It builds its own board.

**Chris Gammell:** Like the motherboard before it's being built locally. That's smart.

**Stephen Hawes:** So, so like that is, you know, that, that's a, it's great because we get to dog food it and we understand how it works and we, you know, and we're, we're not separated from what it means to use the thing. We're very tightly coupled to that. Um, but yeah, I mean, it, you can push it to that point where it's like production or moving machines and you're, you know, using them to make the boards. Um, but you know, it's really meant for the low to medium scale. Once you it's stable and you're up, that's what CMS exists for. You know, this is really meant to be for that prototyping medium production scope. Um, you know, and that's where it's been most useful.

**Chris Gammell:** So yeah, I don't know. Much like a 3d print. I'm, I'm actually always surprised that like, even though a lot of the 3d printing companies want to still 3d print everything. And I, I get it for like a control and like being able to change stuff over time. But like, sometimes I'm like, you should just get a mold. Like, it just feels like at a certain point you should get a mold. Feels irresponsible to keep going back and forth with the 3d printer.

**Stephen Hawes:** Sure. But like, but that's some of it's ethos I think too. And yeah, there's a, uh, my buddy Lucian and I, Lucian who works here at Opula with me. And, uh, we also both worked at form labs together and we, we, we have kind of an internal, uh, shorthand that we use, uh, about the fuse handle. So the fuse, uh, SLS printer that form labs makes the handle for the fuse is printed on a fuse. And I think they do this for the sake of, yeah, we really, it's dog fooding. You want to have to force yourself to use this thing. Even if you're not in that use case anymore, even if you've outgrown that scope, it's still important to do that. And I think, you know, especially at the rate that things have been going over the past six months or so, you know, it's, you feel, you feel the pole. You're like, yeah, we're, I mean, the lumens meant for medium production and we're starting to grow out of that. Uh, so, but it's, it's been really cool to kind of see like, Oh yeah.

**Chris Gammell:** I think the natural thing to do here, Steven, is to just build a bigger pick and place that can serve the large market.

**Stephen Hawes:** No, Chris, no, no spoilers, man. But I mean, you know, it's maybe that's part of it.

**Chris Gammell:** Sure. Sure. Sure.

**Stephen Hawes:** But, but, you know, I, I, it's cool to really understand the full scope. Cause like we would use it, we use it for making a couple of boards and then we also use it for making like tens of thousands of boards. It's like, okay, you know, what, where is that like, do we want to do the Prusa thing? And we have a crazy print firm for printing all these parts. I mean, Prusa has injection molded parts too. You know, I'm, I don't want to die on the hill if it's the only way to do it. There's a lot of great ways to make stuff, you know, I'm, it has its place. So yeah, it's been interesting starting to kind of a butt up against the higher end of like, we're moving machines. Like we, we, you know, I guess that's another thing where you're empathetic for customers

**Chris Gammell:** that are also maybe at the top of their range. And it's like, you know, when can you tell someone to be like, well, you should really go look at that crazy ass Samsung machine or whatever the hell is.

**Stephen Hawes:** I don't even know what's up above or, or higher contract manufacturer. Really?

**Chris Gammell:** You know, like when you're getting to that point, it's like, if your design is stable

**Stephen Hawes:** and you're not worried about, oh no. Like if, if you get, you know, 2000 boards in the mail and a part is soldered on backwards and you're dead in the water, you have to ship tomorrow or whatever. You can spin up the lumen and crank out some boards and keep up. Right. Like it's almost like an insurance policy at that point. Um, which a lot of customers.

**Chris Gammell:** Everyone should have one. That's what I heard here. Folks. Steven says everyone should have one. We've tricked him into saying it.

**Stephen Hawes:** Chris, you're a better like salesperson than I am about this thing. But I mean, that is a nice use case, right? Like, yeah, I'm sure. Yeah. That's, that's what a lot of people still think about it for. Yeah. But yeah.

**Chris Gammell:** We mentioned Lucien. We should mention the podcast. So you and Lucien have been doing the OM podcast now for 35 episodes.

**Stephen Hawes:** Year and a half maybe ish.

**Chris Gammell:** Yeah. Yeah. That sounds right. Okay. Yeah. Cool. That's great. Yeah. And it is more about open hardware and like manufacturing than just, just electronics. Is that right?

**Stephen Hawes:** Yeah. I would say it's patently not about electronics. Um, like it's out of my turf, man. I wouldn't dare infringe my guy. I wouldn't even think about it.

**Chris Gammell:** There's a lot of room here.

**Stephen Hawes:** Obviously I know nothing about picking places. I think that's very clear. Very, very clear. The OM stands for open hardware manufacturing podcast. So it really is just that it's like, we make an open source thing and we also make it here. Like our line is right next to our manufacturing is right next to our desks. So we're very tightly coupled with making the machine and taking community feedback and starting a company, running a hardware company. So it's really meant for folks that are like trying to start a thing, trying to figure out how process flow works in a company, a hardware company, that kind of stuff, open source stuff. So it's been super fun. It's been so much fun doing it. And so much of what, why Opulo is a thing is because the point is to help people make their products. Like that's the whole point of it. And so the podcast kind of checks that box in a weird, different way that isn't shipping hardware, but like telling people how we screwed up and, um, helping them do that less. Yeah.

**Chris Gammell:** I was at some of the early like open source hardware summits and stuff like that. And it feels like there's less talk about it as like a, it just feels like more of a thing that happens now, which is great. And you guys are doing it and it feels like other people are, are doing it as well, but it's less like, uh, let's talk about the, I guess I'm really, I didn't like how, like it just always devolved into like licensed stuff. And it's like, I like, I like the idea of like, let's just build stuff and then share it. And, and, and like that piece focusing on that is more interesting to me.

**Stephen Hawes:** I agree.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Yeah. It's like, like licenses are like taxes. You have to think about them, but it's not fun to necessarily, you know?

**Chris Gammell:** Yeah.

**Stephen Hawes:** Um, so yeah, I, I totally agree. And I get why that's a very common thread is because it's totally, it's legal East. You have to figure it out. It's what do I feel comfortable with? Blah, blah, blah, blah, all that stuff. Um, but that's not, that's not the hard part. That's like one of the easier parts is like, cool. I'm stoked with this license. This is how I feel about, about how I want to share this thing that I'm making. If I'm choosing to publish it and make it open source and all that stuff. Uh, how do you actually buy stock and stuff and make things and do customer support? And like, that's the hard stuff. That's the tricky thing. So yeah, so that's kind of more of what we're trying to check. And you know, I, I still like having those conversations, but we've had a couple episodes about licensing, um, that are interesting.

**Chris Gammell:** We actually see other people operating in this like more open space as well. Like I see a CN Maslow CNC is like one of your guests.

**Stephen Hawes:** Like in terms of how they manage their open source, uh, just like the realm of, uh, people

**Chris Gammell:** who are doing similar stuff to Topulo. Like what other types of companies, what other realms is it machine builders? Mostly is it, um, manufacturing professionals that are making stuff with tools like yours? Like where, where do you find kind of like lookalikes that, that you would maybe talk to on the podcast?

**Stephen Hawes:** It w it's mostly machine builders. Um, and that might be just like sampling bias of like, that's where we are. Yeah. That's where I'm exposed, you know, to that kind of thing. Um, so it could very well be that, but yeah, like a lot of the guests.

**Chris Gammell:** It's a business model too, right? Like there's a lot of value and still building all the, like being open, but building all the things. Cause it's like serving this, this community as well.

**Stephen Hawes:** Yeah. Yeah. That's true. And I, I think you're totally right. And there's also like, uh, Thea Flowers, um, who we actually recently hired. I saw that. That's very exciting. Yeah. We're so stoked about it. We're so stoked to have her. Um, and she ran winter bloom, uh, synthesizer. That's right.

**Chris Gammell:** Oh yeah. Yeah. Yeah.

**Stephen Hawes:** And beautiful modules. And like her approach is, you know, I don't want to speak for her too much, but like, she's just so giving with source and like encourages people to make and clone and modify and all that kind of thing. Um, and I've seen some synthesizer companies that are open to that's a kind of a whole other vertical of this, this whole thing. But, um, uh, mainly I'm plugged into like, Oh, you know, another cool one, uh, open source, like scientific tools, a lot of interesting, um, open flexure microscope, super cool project. Um, I built one last year, two years ago, last year. Um, and it's an open source 3d printed microscope that uses all these like, um, like lever action gearing. Um, it's a big, crazy, like 14 hour 3d print that has a bunch of flexures baked into it. And that allows a motor to move and it scales down that motion to like, like tens microns at a time or something. It's really, really cool. So that's another interesting thing. You know, people iterating on the design in that way tools typically seems to be where it feels comfortable. Um, where, where it shines the most in my experience. Got it.

**Chris Gammell:** Okay.

**Stephen Hawes:** That makes sense.

**Chris Gammell:** Yeah. I mean, I, uh, I got to release some hardware recently and it was because the hardware was supporting the business. It wasn't because like the business wasn't the hardware itself. And I feel like that's one of the, it feels like with, with y'all as well. Like it's, uh, the business is the ability to kind of pull it all together. Like you said earlier in the show, it's like, if someone prints the, the strip holders, that doesn't kill your business. That makes people do more stuff with it. Right. So it's like. Exactly. Yeah. It's like where the, where the value is.

**Stephen Hawes:** Yeah. Yeah, totally. And I think it also depends on what niche you're in, in the hardware. Cause you know, if you're buying a pick in place, chances are you're using it for work, you know? And if you're using it for work, chances are you don't want to build one. So, you know, the idea of, um, you know, it's effectively free to compile software. It's very expensive and time consuming to quote unquote compile hardware from source. Right. The, it's a beautiful model for making money on sustaining a business on open source hardware is compiling it. You know, people don't want to go through the effort of compilers, man. Oof. Yeah. Yeah. Turtles all the way down. Yeah. Yeah. That's, that's a great way to provide the value for people that, and, and also if you don't have the money to buy one from us, you can build one. We literally all of our internal work instructions for how we assemble it here at our office are also available online. You can follow the same thing. All our texts on the production, as we speak, are working on building lumens. You can follow their instructions and build it yourself. You know, like I, I would so much rather have not have a hundred percent, you know, Oh no, you have to buy one if you want one, but you know, more people are included in it and get to use it and give feedback and contribute to it. And, you know, I find that much more valuable.

**Chris Gammell:** Yeah. That's cool. Yeah. I, uh, I just finally took apart one of my old 3d printers and I have a bunch of bar stock, so I'm not going to build one of these things, but I have the parts for part

**Stephen Hawes:** of one, I think what, what kind of printer is it? Is it, does it use 2020, uh, V slot aluminum extrusion?

**Chris Gammell:** I don't know if it was. Yeah. You're asking questions. I don't know the answer to it is aluminum extrusion. Uh, it is heavy. Uh, it is probably 2020. Yeah. That sounds about right. Actually. It was, um, what was it called? It was called a Wilson two. It was a I three clone. It's great. I've never heard of it before. Yeah. It was very niche. It was big.

**Stephen Hawes:** It's a bed slinger. That's super big from a long time ago.

**Chris Gammell:** So 300 by 300 by 200, I think.

**Stephen Hawes:** Yo. Wow. Yeah. You're not kidding.

**Chris Gammell:** Or no 300 by 200 by 200. Yeah.

**Stephen Hawes:** Okay. Yeah. Wow. Yeah.

**Chris Gammell:** Yeah. And I think it was pretty hard to, my old coworker built them. So that's how I, I did it.

**Stephen Hawes:** So that's cool. Yeah.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Yeah. I mean, it's all kind of the same vitamins as they call them, you know, at the base. And that's why a pick in place now feels more, um, the, the, it was a ripe opportunity to have all of the infrastructure and, you know, the, the parts available, the software available that facilitated 3d printers as a thing led beautifully into supporting a pick in place. The pick in place is effectively a 3d printer. When you boil it down, there's pneumatics, there's a couple other, you know, staff foods, there's cameras, there's other things involved, but like it was a great foundation to start. Got it.

**Chris Gammell:** To go from time had come. You're saying.

**Stephen Hawes:** Yeah, it really was. I think it was an appropriate time. The scale of step promoters are inexpensive. Software was reasonable for controlling them, blah, blah, blah, blah. Yeah. It was, it was a good opportunity for that to happen. Yeah.

**Chris Gammell:** Yeah.

**Stephen Hawes:** Yeah.

**Chris Gammell:** To step into the business thing real quick. I mean, this is not a small amount of just like stuff that you have to kind of like build and store and, and all that sort of thing. So like, what's, what's that been like as you've been building Opulo up? I mean, like you said, you have a bunch of techs that are building this thing, but that means you also have shelves where all this stuff sits. So like, what about that piece of it?

**Stephen Hawes:** That's a huge piece of it. We started in my garage, Lucian and myself, we were living in my house and yep. Yeah. And we were trying to make the first batch of motherboards in my garage and it was, we actually both got carbon monoxide poisoning. Um, because we were running, we were just stupid. We were running, uh, uh, propane heaters in there to try and keep it warm.

**Chris Gammell:** Oh yeah. Yeah.

**Stephen Hawes:** We were just absolute clowns. Yeah. Yeah, dude. It was freezing. And we, we were just trying to stay warm running them and, and we got these headaches and suddenly our carbon monoxide. Oxide alarm goes off and we're like, Oh no, we're really dumb.

**Chris Gammell:** Yeah.

**Stephen Hawes:** So yeah. So we got an office, it's like 3,500 square feet. And in like the first year it was full and like we, Lucian and I probably every four months we go, okay, how do we rearrange this whole thing to squeeze another 15 square feet out of it? Yeah. Right. Um, it has been, it has definitely been challenging to keep up with the space. And like, especially since this new version of the machine came out before, uh, that was a pretty big step for us in terms of scale. And it's been very hard to keep up. Hiring has been a huge thing of just like trying to get more people in to help us build these things. And like, we, it's such a Sisyphean effort. We're always trying to bring our lead time down, but Lucian jokes that like, he is the firefighter trying to put out the, the fire that I'm starting of trying to get people to buy the machine. And he's trying to tamp it down by killing the lead time. And so we're kind of constantly in this flux of doing it. And so we're kind of at a stalemate and we keep growing and then, you know, our, our scale keeps growing as well. And it, yeah. So it's really hard. That's the hard part. You know, the source is also hard. It's hard to get something that works and tested and blah, blah, blah. All those things are tremendously important. And then also the, the compilation of it, the effort of putting the thing together, QC-ing it, what's important to QC, what isn't important to QC, how thorough do we be to make sure we catch these things, blah, blah, blah, blah. All that stuff is incredibly hard to get right. Yeah.

**Chris Gammell:** Well, I was about to wrap up and mention your YouTube channel. And then I remembered that we were supposed to talk about this whole other thing that you, you did.

**Stephen Hawes:** Oh, yeah.

**Chris Gammell:** It actually inspired me to reach out as well. You have been building your own PCBs as well. What? What? Yes. I. So you're a, you're a laser person now too? Not just 3D printers.

**Stephen Hawes:** I mean, yeah, dude, they're so cool. The, I made summer, I went to the form labs hackathon to try and make a PCB on their new printer, the form four. And I tried this when I worked there and it didn't work super well because I was just bad implementation. But it's really interesting to me of like, what's the quickest way you can make a reasonably useful PCB? And you can get boards quick.

**Chris Gammell:** And Krasnow did a bunch of like plating of stuff that he had done with 3D printing as well. And I think Scott did some stuff. Yeah.

**Stephen Hawes:** I think a few, or he had the Micronics printer. Yeah. And he did like copper plating on it or something.

**Chris Gammell:** Yeah. Was Micronics the one that got bought real fast? Like after, like they were about to do a Kickstarter, then they got bought.

**Stephen Hawes:** Didn't they did a Kickstarter, they raised a bunch of money. And then I think they like refunded everyone's money or they didn't collect it yet. Yeah. They got bought by form labs.

**Chris Gammell:** Um, oh, I see. Got it. Yeah.

**Stephen Hawes:** Yeah. It was a whole thing.

**Chris Gammell:** It's a whole thing.

**Stephen Hawes:** It was a whole thing.

**Chris Gammell:** Search the internet if you want to see that story. I suppose. Yeah, exactly.

**Stephen Hawes:** That's exactly it. Um, but, but yeah, so, so I would just like, I want to see different ways to make boards. Like the lumen's great for assembling them quickly. If I really want to like try a design, what's the quickest way? Yeah, exactly. So, you know, making them on an SLA printer, super cool. People have done it before. It works. You still got to deal with ferric chloride and all this stuff. Fiber lasers will actually ablate metal. You can like cut and like vaporize a voxel of metal using this laser. And I tried doing this with a fiber laser and it just works so well. I mean, it's just so cool. If you don't care about a solder mask and of course, huge asterisks here, one-sided boards. You're using FR1 and at FR4, there's definitely concessions you're making here. Um, but 10 minutes of no work.

**Chris Gammell:** Controlled impedance, I'm sure. And like, you like three mil space trace. I'm sure. Right. Yeah.

**Stephen Hawes:** You can get, uh, you can get to six mil trace space.

**Speaker ?:** I know.

**Stephen Hawes:** Yeah. Not three. I mean, yes, of course.

**Chris Gammell:** That's amazing. Right. But I'm just, sorry. I was just.

**Stephen Hawes:** Yeah. It's not going to be. Just lob and bombs. Yeah. You. I, yeah, it's, there's concessions. It's not going to do that stuff. Um, but it's super cool. You can just drop a piece of copper clad in there, send your design over export from, from key cad, key cad. And off it goes, it'll just cut away your board and you have a, a beautiful one-sided board. And solder mask is another five minutes of personal work, 20 minutes of etching time. And now you have a gorgeous solder mask. It's like, it's a really cool process.

**Chris Gammell:** It's really cool. Very cool. I mean, so then the workflow for that, and I'm keep talking about workflow, but like, or like a laser type thing, then that's just now Gerber's go into a, whatever the fiber lasers input is.

**Stephen Hawes:** Uh, it's not even Gerber's it's DXFs. So, because it treats it like a picture you're, it thinks you're, you're etching, you know, something at a craft fair with some, you know what I mean? That's what this laser is for is like, you're supposed to bring it to a craft fair and someone comes up and it's like, I like this necklace. You're like, what's your name? Linda. Okay. And then you like Linda onto, you know what I mean? Like that's the point of the thing. Um, so you export as a DXF. I actually have a whole GitHub repository where I've written up the entire workflow for doing this exact process. So it's all, all encoded if you want to do something similar. Um, but yeah, you export it as a DXF, do a little bit of stuff in their software to kind of, you know, massage it into the format it needs, pick your settings and just let it rip. And you, you have the board at the other side. It's really cool.

**Chris Gammell:** Yeah. That's wild. And I mean, it's like a open, open thing as well. Is that right? Like the fiber laser? No, I don't know anything about lasers.

**Stephen Hawes:** I barely do too. Okay. So yeah, uh, this is a company that has recently been making a lot of lasers and they've just recently started going into fiber lasers. It's still an expensive machine. It's like, I think retails like 4,500 bucks. Like it's not cheap. You really got to have a good use case for this thing to justify this, this path here. It's not, it's not for everybody.

**Chris Gammell:** I'll be selling your own fiber laser, uh, PCB machine anytime soon.

**Stephen Hawes:** I I'm probably not anytime soon. Yeah. I'll give you that. Okay.

**Chris Gammell:** All right. A little ways off.

**Stephen Hawes:** Yeah. I, I, I, I won't discount anything. Um, but yeah, it's, it is a really cool process and they, they sent me the, uh, laser for free. I did not spend that money for it to make the video about it and all that stuff. Um, but yeah, it's, it's a, it's a very interesting way to do it. And I think there's definitely some ways that you could do double-sided pretty easily, but I was talking with Timon and he was saying that like, he has a Carvera that he uses for like milling the boards on a little desktop CNC and he will actually thread like enamel wire. He will like, so between the holes in the board, like to make vias.

**Chris Gammell:** And then you just melt the top and melt the bottom. And yeah, that's a good idea.

**Stephen Hawes:** And then you just snip and you're done. And that's a pretty clean way to do it. And you can drill holes with a fiber laser too. So I want to give that a try. And I think that would be a pretty easy workflow for double-sided boards. Um, I also have this like gnawing thought in my brain, like this intrusive thought of, I really want to try and make the lumen motherboard on the fiber laser. It's a four layer board.

**Chris Gammell:** Oh wow.

**Stephen Hawes:** And I'm like, I think I could do it. I'm pretty sure I could make it happen. It would be a real pain, but I think I could do it. So I like, I haven't been able to get out of my head. I really want to try doing it.

**Chris Gammell:** Yeah. That's interesting. Yeah. Cause I mean, that's always like the thing you think about like the, the four layer process is always the, you know, it's a thin sheet of pre-preg with like copper on both sides. Yeah. I guess you couldn't, I guess maybe you could try and get, what was the reason for FR1 versus FR4? Was it the, it was the blackening, right? Of the, of the FR4.

**Stephen Hawes:** It technically is conductive. Um, so. Oh, that's right. Cause you're carbonizing it. Yeah, exactly. But FR1 is like a phenolic resin in cardboard effectively. Like it gets ablated all day long. It doesn't care. It's just living its best life. So FR1 was way easier to use.

**Chris Gammell:** Um, and I just wonder if you got like a, if there's a special type of like pre-preg you could get where you had like copper over pre-preg and then maybe trying to do an alignment yourself, that sort of thing.

**Stephen Hawes:** And yes, what I was like, like it would be so cool. You could like, uh, drill the holes on one side of the copper and that's like now your alignment feature. If you have through holes or vias or whatever, and then you can flip it over the other side and the laser will actually like trace out the outline of what you're about to etch for the next pattern. That's perfect for aligning it. Once you flip it or I've designed a little bracket that bolts into it that, that does a similar kind of alignment thing. Um, and then you do that on a two layer board and then you just etch another sheet, glue that on top with a bunch of wires you thread through for vias that you've already soldered to the inner two layers. Like, I think you could do it. I think it'd be cool. It doesn't make any sense.

**Chris Gammell:** You say we could do it? I mean, just, I don't want to be in this week personally. I want to watch the video after the fact, but I don't mean to implicate you. I mean, we as a society could figure it out. The royal we. Yeah. Yes, exactly.

**Stephen Hawes:** No, I'm not signing you up for this.

**Chris Gammell:** Okay, good. That's, I mean, I really like watching these experiments. It's, it is a lot of fun that you share all of this stuff. I definitely recommend people follow your YouTube channel. So it's great to kind of follow along and really glad you're doing all this, man. It's like, it's very exciting. And I think we're all benefiting too. Like the fact that the, the lumens out there, that's cool.

**Stephen Hawes:** Yeah, it is cool. I, I really do like the fact that people can just download it and make one, you know, like I, I don't know if me back when I was frustrated with trying to make those light up bow ties, you know, I, it's actually cool. The amount of money I made from the Kickstarter was exactly the price of a lumen. So it's like, okay, cool. This would have paid for the tool to make it, you know, I could have put this in my arsenal from that, but you know, there's a lot of people that don't want to do that. They're definitely more niche in, you know, most people that want one, but those people are there. They still exist. And it's cool that you can, you can just buy a bunch of parts and print stuff and make this thing. And, you know, I, I'm super stoked on that fact. That's a big part of it for me.

**Chris Gammell:** That's great.

**Stephen Hawes:** Yeah.

**Chris Gammell:** Well, um, we already heard you say that everyone should definitely buy a lumen. Where should, where should they go to do that?

**Stephen Hawes:** Uh, you can find out all the lumen PMP stuff. You want to pick one up. It's at opulo.io. Opulo is O-P-U-L-O. Um, there's also links to our GitHub. If you want to find the source, all the stuff kind of stems from there. That's the best place to go. So go check out opulo.io for all that.

**Chris Gammell:** Yeah. There's links to the podcast as well. Links to your YouTube channel, I think. But if not, you're Steven Oz on YouTube. Steven underscore Oz, right?

**Stephen Hawes:** Yeah, I don't think I got that first order, uh, handle.

**Chris Gammell:** It happens. It happens. And, uh, yeah, definitely recommend people check out all your stuff. It's, it's so much fun to watch, follow along. So thanks for being here today.

**Stephen Hawes:** Thanks, Chris. Yeah, absolutely. Thanks for inviting me on, man. It was great to chat with you.

**Chris Gammell:** All right. See you soon. See ya.

**Speaker ?:** See ya. See ya. Thank you.
