---
episode: 141
title: FPGAs, Robots & Thermocouples - Wampum's Wavering Worth
url: https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by ViaDesigner.com, part of Triad Semiconductor. Who needs a chip printer when you can design your own mixed signal chips on your desktop? ViaDesigner is a Windows-based software for the design and simulation of analog and digital circuits. At ViaDesigner.com, you can learn about mixed signal design, share your design IP, and form teams to create your own custom via ASICs. Go to ViaDesigner.com slash the Amp Hour and enter coupon code AMP100 at registration for a free year of ViaDesigner, a $500 value. This is the Amp Hour Podcast, recorded April 15th, 2013. Episode 141, Wampums, Wavering, Worth.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Chris Gammell's Analog Life. You're not going to believe it, Chris.

**Chris Gammell:** What's that, Dave?

**Dave Jones:** I can see the floor of my lab.

**Chris Gammell:** No way. It's clean, huh? Yeah.

**Dave Jones:** Who'd you pay? Who did you hire? It's novel. I hired the wife, and she came over on the weekend. You need to clean up that pigsty. Yes, dear. All right, so she and Sagan. So what, she directed you? Yeah.

**Chris Gammell:** I picked that up.

**Dave Jones:** Yeah, they both came over, and we, well, attempted. It took us several hours, and we could at least see some floor now. Wow. Which is, yeah, which is incredible. Wow. Because if you haven't seen my photos, like, I, this lab is an absolute pigsty. To get from the door to my bench where I film, I've actually got to step over, like, ten things, you know.

**Chris Gammell:** You definitely need shelving or something.

**Dave Jones:** Yeah, it's disgusting. It's like big industrial rack shelving. But there's still shit all along the floor, like, along my bench. But at least the main area is clean. Yeah. And, yeah.

**Chris Gammell:** Oh, yeah. I mean, look, my bench here, I mean, when I moved in, this whole basement was barren, and now it's just completely full of crap. Yeah. So much stuff. Oh, it's okay. I don't need to throw it out yet. You know how that gets, right?

**Dave Jones:** Yeah, yeah. And then we complain about it every time, don't we? Like, oh, I can't. Oh, yeah. Every time I go to do a ten, I can't find my screwdrivers, can't find this, can't find that. And, like, oh, man. But I never actually go, right, I'm going to spend a couple hours cleaning up. No.

**Chris Gammell:** See, I feel like that's, I don't know. I never got into that habit either of just, like, some people are very meticulous. They want to clear their bench at the end of the day or something. Yeah. I don't know if that's, like, just a personality trade kind of thing or. I don't know. I don't trust people with clean benches, though. I'll tell you that. Right. If it's not. The dirtier, the better. Jim Williams style, right? Exactly. Exactly. Yeah. Oh, I don't know. It's just, I think it's just a, like, maybe it's a mentoring thing or something. But something has to get it so that you get into that habit. But I've never gotten it.

**Dave Jones:** Well, usually we're in a rush. Like, you know, we just want to, oh, quick, let's do this. Oh, there's something else on the bench. I'll push it aside. And then you do that 10 times and 10 things have been pushed backwards. And before you know it, the, you know. So, yeah. Like, I've got, you know, six meters of bench space long here. Yet I work in, like, one square foot, as you Yanks would say. You know, because everything else. Like, I just, oh, I need some room to solve the board.

**Chris Gammell:** We don't touch it either, right? Yeah.

**Dave Jones:** That's right. So you just gently sort of sweep.

**Chris Gammell:** You don't disturb the artwork that is your junk pile. That's it. Yeah.

**Dave Jones:** Oh, man. So if anyone is one of those meticulous organizational clean freaks, engineers. They can send their pictures in. Let us know. Send your picture in.

**Chris Gammell:** Happily take workbench of the week photos that are messy as much as. I think last week's was messy and clean. I don't know. I have this kind of thing, too. So, like, whenever I start cleaning my bench, I usually have a trigger in my mind that I stop and I say, I'm avoiding something right now. I know that if I'm cleaning, I'm usually actually avoiding doing work. Oh, yeah, yeah. Exactly. So at that point, I've just trained myself to messiness means activity.

**Dave Jones:** Yes, that's right. I'm doing okay, then. You want to know what else she made me do?

**Chris Gammell:** Put up an air deodorizer? I don't know.

**Dave Jones:** She made me throw out empty cardboard boxes.

**Chris Gammell:** Oh, jeez. Doesn't she know that the trash room is for collecting stuff from, not donating to? That's it. We've all seen the videos.

**Dave Jones:** That's right. I do need those 15 computer monitors and I do need those 10 empty boxes in there.

**Chris Gammell:** Turn it into an episode of Hoarders, right? That's where you're... Right.

**Dave Jones:** Is there a reality TV show called Hoarders?

**Chris Gammell:** Oh, yeah, yeah. That's big in the States. It's like they go into people's houses and I've never seen it. I think that's disgusting. Right. But, you know, there's like newspapers stacked to the ceiling and then they get all like...

**Dave Jones:** Oh, yeah, no. I'm not that bad.

**Chris Gammell:** There's like psychological disorders there too, but...

**Dave Jones:** Yep, yep.

**Chris Gammell:** There are different levels.

**Dave Jones:** Right.

**Chris Gammell:** Well, I'm glad you dug yourself out, man. That's...

**Dave Jones:** Well, I haven't fully done it yet. Oh, yeah. And I still haven't organized anything. So if you asked me, you know, if you came in and said, hey, Dave, can I borrow a 2N 2222 transistor? It's like, oh, yeah, I've probably got one somewhere, but...

**Chris Gammell:** Just dig through the pile, man. That's what we all do. That's why markings are so important on parts. Like we talked about last week and how they're going away. It sucks, you know?

**Dave Jones:** And bags. And like, you know, how do you categorize these things? Because I like to keep my components that I've got in a complete bag that I bought from DigiKey or whatever, mouse or Farnels or whatever, usually. Yeah. I buy them from scratch for each project. So I keep them all in the one bag for that particular project so that when... Oh, yeah, yeah. You know, I'm working on... I'm going back to work on that project. I know all the parts are in that one bag.

**Chris Gammell:** Right. Yeah, you don't want to start pilfering from one.

**Dave Jones:** Yeah. Well, that's right. But if I'm working on another project, then I've got to remember in my head that I've got, you know, that... Oh, yeah, I've got one of those power MOSFETs. Yeah, I use that in that other project. So it must be in that project bag instead of having, you know, a nice, properly laid out, you know, power MOSFET drawers, you know, with all my different... Ten different types of power MOSFETs. Yeah. So...

**Chris Gammell:** Yeah, I think the key in any kind of good workbench setup is to hold off on the junk drawer or the junk cup as I have on my mechanical workbench for as long as possible. Oh, I have a cup. Yep. Yep. Yeah, because as soon as you have one, right, if you want to do it... If you want to have organization, that's good. You know, keep it going. But as soon as you have that junk bin or junk drawer, it's all over, man. It's just... Yeah, yeah. It becomes the... It's just the lower... The path of least resistance. It's just... Yeah, throw it right in there. Now I'm done. Everything's clean, you know. It's like... Yeah, yeah. It's like Calvin and Hobbes when you shove all his belongings into the closet just to... That's how he cleaned, right? Yeah, yeah. That's right. Yeah. Yeah. I have been sorting through stuff as well because it is tax day here in the U.S. I guess not just Cleveland, but it is tax day in the States. And with more than four hours to go, right before the show, I finished filing my taxes. Just... Woo-hoo! You know... In true engineering fashion. I love so much time, you know. It's just... I'm fine, you know. And yeah, I did good this year. On the business front, I almost broke even. That's all I go for. Yay!

**Dave Jones:** Yeah, you'd be surprised the amount of money you spend on just toys and widgets and how it adds up, you know, little parts. Oh, yeah, I'll buy a part. You know, I'll buy 10 bucks worth of parts for this little thing I'm working on. And you do that, you know, a hundred times. Yep. Yeah. Yeah, it adds up.

**Chris Gammell:** Definitely. Definitely. Well, and, you know, at the end of the year, too, it's... If you do... I mean, I don't know. So, I learned about, like, LLCs and stuff like that. Like, I have an LLC. And I learned about that stuff from one of my former mentors, because he had one as well. And he's like, you know, basically, at least in the States, I don't know, everywhere his taxes are different, but, you know, at least in the States, it's like, if you have, like, $1,000 in profit at the end of the year, you have to pay taxes on that, versus, I don't know, buying a CNC machine and, you know, writing that off. It's like...

**Dave Jones:** Yeah, hello. I think that's pretty universal in every country. Then come tax time...

**Chris Gammell:** Yeah. Yeah, yeah.

**Dave Jones:** If you've made a profit, yes, you pay tax on it. That's how the system works.

**Chris Gammell:** Right, right. Well, what I'm saying, though, is making that year-end purchase to, you know, that lessens your taxable, you know, profit, basically. You don't pay taxes on it then, because you have a new...

**Dave Jones:** Oh, see? Yeah, that's a myth, right? You see that, right, at the end of tax time here, which is June 30th, right? Mm-hmm. Right? Right, if you go to the computer markets, right?

**Dave Jones:** Yeah. On, you know, one of those dodgy computer markets. It's on June 30th, or, you know, the last Saturday before tax time. It's packed. People are handing money, you know, wads of money over, because they think that they're, you know, that, oh, the computer's almost free, because I'm going to write it off on tax. But no, folks, go and do the math. You're actually... You don't save anything. Like, you know, people think, oh, I'll buy the $2,000 computer instead of the $1,000 computer, and I can write it off on tax. If you actually do the math, you're not actually saving anything. You're still paying double. Like, you know, give or take. It depends on your tax bracket. Oh, no, no, no. Basically...

**Chris Gammell:** I disagree with that. Well, at least in the States, it's different, but...

**Dave Jones:** Right. Oh, right. No, here, it's like, no, you pay, you know, you basically, yeah, you're not saving that $1,000. You're basically still paying double. So, you know...

**Chris Gammell:** Well, I mean, assuming you... So, in the States, at least, the estimate I always use is, like, any money that you make as, like, a consultant or something like that. So, say you make $100 as a consultant, at least in the States, between all the different types of taxes and everything, it's about 50% of taxes. Right. Right. And because of, like, self-employment tax and everything else. And so, if you have a year-end purchase like that, like a deductible year-end purchase... Ah, right, yeah. ...then, yeah. I mean, that's, like, effectively getting a 50% discount on it because at the end of the year, you're going to have to either pay taxes on the $100 or spend that $100 and, you know... I don't know. Maybe I'm wrong about all this and I'm sure that there's some consultants and other business people.

**Dave Jones:** Well, that's similar how it is here because if you're earning an absolute buttload and you're in the highest tax bracket, which might be 40-something percent here, then, you know, it's... If you still do the math, it's, you know... Because it comes off your entire... Because that, you know, if you buy the thing for a widget for $1,000, it comes off your entire taxable income. Like, it's not like you get that $1,000 back. It just reduces your taxable income by $1,000. And if you earn $100,000, it goes down to $99,000. Right, right. And then if you do the math, then, you know, the tax... Yeah. You haven't saved much. I see what you're saying. So, it's the same here. Yeah, yeah. I see what you're saying. Okay. Don't be deluded, folks.

**Chris Gammell:** Yeah. Yeah. And at the end of the day, it's still making... You know, it's still spending money. So, it's like, you know... Yeah, no. Exactly. If you don't need to... If you don't need to buy it, then they'll buy it.

**Dave Jones:** That's... That's it.

**Chris Gammell:** Yeah. So, yeah. That's all over. Thank goodness. Right. It's always a stressful time. It shouldn't be, but it is.

**Dave Jones:** And you owed some money. Yeah, a little bit. You poor bastard.

**Chris Gammell:** Yeah. Well, it's okay. Yeah. It's not like... It was just a miscalculation on my part. Not a... Not a big problem. Not like... I'm not like... Rah, rah, rah, rah. You know? Right. All right. Yeah. So, what's new around here? We have t-shirt designs on the way. I don't know if people... We do. And they're very cool. Yeah. They should be released in the next week or so. We're getting some final touches from our graphic artists. We have graphic artists. And they're cool looking. Hey, graphic artists. Yes. Yeah. Yeah. So, we'll be releasing those in a week or two. And then sending out those t-shirts from the survey contest. Survey, I guess, participation. Drawing. So, thank you again to everyone who did that. That was very nice. I'm still reading through a lot of that stuff because there's so much stuff to read.

**Dave Jones:** There's a ton of stuff there.

**Chris Gammell:** Yeah. Gold prices are tumbling. They are. Speaking of financials, which usually wouldn't be... It wouldn't be relevant here, right? It's like, oh, okay. Who cares, right? Well, it does affect us, though, because I've complained about this before. Connectors get damn expensive. Like, all these connector manufacturers are like, oh, well, you know, we were going to save you this for a buck, but gold's so expensive, it's a buck 20 now because we put 10 micro inches of gold per...

**Dave Jones:** Microns instead of two microns, you know? Yeah. Yeah. Because you can pay a lot. You pay the price of your connector. You can get different grades. A lot of people don't know this. You can buy different grades of gold coating. You know, 5 microns, 10 microns, 20 microns thick. And...

**Chris Gammell:** It's actually not microns, though. So microns are micrometers. Yeah. They usually do it in micro inches. At least in the States. What? So like, yeah, it's micro inches. Look it up, man. It's stupid, but it's true. 30 micro inches is the highest you can get, but that 30 micro inches of gold, which is... Right. Yeah. What would that be? It's micro something. 0.03 or 0.3 mil? I don't know. 0.3 mil.

**Dave Jones:** And you can get the same thing on boards as well. When you get your boards gold plated, you know, you can get cheap-ass one-hung-low Chinese plating, or you can get, you know, really ultra-quality thick, you know? Yeah. And it affects yourself, too. Real gold plating from Fort Knox, you know?

**Chris Gammell:** I never realized that. I mean, like, you know, until I, like, really got into it and started seeing, like, failure reports on when you don't have that kind of thing. Yeah, yeah. But it can really start to mess things up. I mean, like... Oh, make a huge difference. Insertions or anything like that?

**Dave Jones:** Hey, I just got a quote for a bulk lot of connectors, right? They're actually those gold binding posts, right? They're gold plated. Yeah, yeah. What I didn't pay extra for is the gold plating, right? But they've got two different types. They've got copper ones, like solid copper. You can get your connectors, and they're much more expensive than your nickel, you know, whatever, alloy kind of... Yeah, your nickel plated steel or whatever they are. Yeah, whatever it is. Yeah. Yeah. And, yeah, you pay, you know, like 30% more for the solid copper. Would you like the solid copper ones, sir?

**Chris Gammell:** What is the benefit of having solid copper? I mean, just the connectivity?

**Speaker ?:** I don't actually know.

**Dave Jones:** I would have thought it'd be... I would have thought it'd be softer or something, perhaps. Yeah. I don't know the benefit of a binding post with copper, if anyone knows. Like, because they're both the same gold plating, right? It's just the middle underneath. Yeah. So, I'm not sure. Maybe it's less thermoelectric, you know?

**Chris Gammell:** Less therm... Like, less thermal resistivity kind of thing? I mean, like, how it actually conducts heat, or what?

**Dave Jones:** No, the... God, what's... I'm having a brain fart today, folks. I do know... It wasn't even tax day there. No, as in... Similar metal junctions, right?

**Chris Gammell:** Oh, like the Seaback effect.

**Dave Jones:** See, thank you. Yes. Yes. But, you know, we're talking about binding posts. That's what... Yeah. Yeah, that's right. Yeah, people probably associate the most. Yeah, don't. And... But there's a binder... The whole video you did on it? There's a speaker binding post. Yeah, the whole video I did, the whole tutorial I did on that. Yeah. You'd think I'd be able to remember it. My brain is just Swiss cheese, folks. Yeah, but we're talking speaker binding posts here, right? So, if anyone knows the advantage of solid copper speaker binding posts, maybe it's heavier current, actually. Oh, maybe. It could be. It could be, because we are talking, you know, really like, you know, like 50 amp kind of, you know, binding posts. So, possibly that's the reason, actually. Low. So, it could be just the copper is better conductivity than the...

**Chris Gammell:** Although... Well, that affects it, though, too, because, I mean, copper is super expensive right now, too. I mean, to the point where... Oh, copper is very expensive. Yeah.

**Dave Jones:** People are stealing it from houses.

**Chris Gammell:** Exactly, yeah. Yeah. I mean, bigger problem in Cleveland, probably, than Sydney, but... Right. I mean, it's just so thoroughly ingrained in every part of electronics, right? I mean, like, I know that a lot of companies moved from... I forget what it used to be. I guess it used to be tungsten that was the metallization layer on microchips. Right. And now, a lot of them moved to a copper layer because that's a lot more contaminating, I guess, that it's... Right. It's a crappier process to work with, but it also has better connectivity properties and everything else like that, so... Yep, yep. Yeah.

**Dave Jones:** They use that on the high-end CPUs and stuff, don't they? You're talking about, like, heat syncing or the actual... No, no, as in, like, part of the fabrication. Yeah, the metallization. Yeah, right, right, right.

**Chris Gammell:** But it's becoming more common in the lower-end stuff as well. Right. So... Okay. And I think they still... I guess they use gold for the bonding wires, right? Those... Yes, yep. When you actually see connecting over from the packaging to the chip, but...

**Dave Jones:** I don't know, all that stuff, though... I've always wondered, are they solid?

**Chris Gammell:** What, the wires?

**Dave Jones:** Yeah, yeah, the bond wires.

**Chris Gammell:** I think so, but they're... I mean, they're tiny.

**Dave Jones:** Yeah, I know. Well, that's the thing, that's the reason that they could be solid gold, right? Yeah. Is because they are... They probably are, you know, how many microns? Microns?

**Chris Gammell:** Think. Microns, yes. I think that actually would be microns, because that's kind of... Right. Yeah. Yep. Didn't we have someone on the show talking about the... Oh, probably. The welding process. Come on, how many shows have we done? I forget. 141 we're on right now.

**Dave Jones:** Yeah, exactly. You know. I've had so many people on. Yeah. We've talked about so much shit. You got it bad.

**Chris Gammell:** I forgot to schedule a guest. If people didn't notice, we do not have a guest this week. Guest, yeah. Yeah. Sorry. We'll try again next week. It's busy right now. It's tough, you know? Like, you get busy at work and... No, you get busy totally. You're busy all the time.

**Dave Jones:** I didn't have enough time to look at the list today, you know? Yeah. So I'm completely winging this. Yeah. I mean, the difference from other weeks is... No, no difference, really. No. No. Usually I jump in 10, 15 minutes beforehand and at least have a look at the links, you know?

**Chris Gammell:** Yeah. Yeah. So it's interesting from the, you know, the... From the actual... All these material science side of things, right? They're still trying to improve it because it's a... Everything is getting pushed lower and lower margin all the time, right? And so I've heard them talking about trying to go to like, you know... I think it was like nanotube type of bond wires and stuff like that. And obviously the packaging is all shrinking so you can start to do, you know, direct bonding and all the other crap. But it's a crazy science. That's insane.

**Dave Jones:** How do you even get the little robot claw in there to hold the bond wire and then, you know, weld it down into place? I mean, that's just stupid.

**Chris Gammell:** It is.

**Dave Jones:** How do they do that?

**Chris Gammell:** I do not know. I mean, I've seen videos of it, but... You used to work in a fab? Yeah, but not there. I mean, I used to work... I used to work in a fab, but the packaging was overseas. That's the crazy thing. Oh, right. You'd get to the end and they'd be like, yep, all right, well, this wafer checks out and we're sending it off to you.

**Dave Jones:** And they just pack the wafers in cardboard boxes and off they go, right?

**Chris Gammell:** Yeah, yeah. Going to get cut up and packaged up.

**Dave Jones:** Hand it to that guy in the brown shirt and... Yeah.

**Chris Gammell:** Yeah. Well, and that's... I mean, a lot of the packaging is almost... I think it's almost all in China and Malaysia, I think. Right. Maybe a couple other places. But yeah, it's very concentrated on the packaging and it's separate from the chip fab. Why is that? Because of labor costs.

**Dave Jones:** Is that because it's a real shitty... Yeah, it's low cost because it's a real... It's probably a real shitty process from a chemical point of view of writing in China. Yeah, they just... Dispose of those chemicals, you know? I don't know. I don't know about that. Oh, H&S? What's that? You know? Yeah. I don't know. I could be... I'm talking out my ass there. I'm probably being... But... You know?

**Chris Gammell:** Being Dave. Yeah.

**Dave Jones:** But no, there's probably... You know, there's elements of truth in that. They take OH&S and stuff like that less seriously over their waste, less seriously than we do in the West sometimes.

**Chris Gammell:** Yeah, but I think normally it's not... I think it's almost always cost-driven. I mean, like, yeah, there are environmental regulations and all that other stuff, but... Yeah, but that costs money, which drives up the cost in the West. Yeah, but not as much as... Man, labor? Labor is killer. Right. Well, yeah. If you look at, like, the overall cost of, like, a PCB or a chip or anything... Well, maybe not in a chip, but anything that, you know, is hands-on, labor costs are just really, really important. So, as we move to robots, right, it'll be less of an issue, but...

**Dave Jones:** No, you can do it anywhere, right? That's the thing. That's the, you know...

**Chris Gammell:** Right. And then with... And then the safety side of that becomes easier, too, right? It's just... It's not like, oh, are you being ergonomic and are you disposing of chemicals properly? I mean, yeah, you still need to worry about the chemicals probably, but the ergonomic and the safety side of things with robots is, did you build a cage around it? Does it turn off when you open the cage, you know? Like, it's... Tick, tick. End of story. Yeah, exactly. It's, I mean, it's not easy. It's not like it's easy by any stretch, but it's less human resource intensive, right? It's just... Right. And you don't have to deal with other stuff, like... This is actually a link from last week, but in... You know, so Foxconn, obviously, is a big manufacturer of PCBs and consumer electronics stuff. That's the... You think? Yeah, yeah. Biggest private employer in China. And... Yeah, 400,000 people working on Apple products alone, I think it was. But we've talked before about them having problems with suicides on campus, actually. So they were the ones who put up the nets, you know, to catch people and everything like that.

**Dave Jones:** I'm sorry. I laugh every time I hear that. I know. Because it's a serious problem, right? It's a very serious problem, right? But it's the wrong solution, you know? It's a comically...

**Chris Gammell:** Yeah, it's a comically ingenious solution, right?

**Dave Jones:** Yeah, stupid solution, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** It cracks me up every time.

**Chris Gammell:** So they've taken it a step further, though. And...

**Dave Jones:** Yeah.

**Chris Gammell:** Well, now... They're taking it a step further. Well, instead of...

**Dave Jones:** They put everyone in big sumo suits so they can't hurt themselves. Yeah.

**Chris Gammell:** They put them in hamster balls, right? They just bounce.

**Speaker ?:** Right.

**Chris Gammell:** No. They fire you. That is the answer. So instead of... So basically, they do some testing of people, and then they say if they're a risk for suicide, they fire them. And then it's kind of like... You know, like in office space, right? How do they do that?

**Dave Jones:** How do they give you a psych test? Right. Office space. Yeah. Yeah.

**Chris Gammell:** It's like, oh, we fixed the glitch. Right. Yeah. Yeah.

**Dave Jones:** But I mean... I can't see how they could afford to do that. Like psychologically screen every worker.

**Chris Gammell:** No. No. I think it was more of a report of, oh, this person is depressed. Right.

**Dave Jones:** This person's agitated, so they bring you in. Right. Yeah. Right. Okay. And then make you even more depressed because they've brought you in and they're giving you psych tests. You know. Yeah. Right.

**Chris Gammell:** Right. It's not the best workplace thing. But I mean, honestly, this is another... This alone is an isolated incident is a sad situation, right? But in terms of like human resources issues and everything else, it's like, man, when there's robots, it's like, that's just another checkbox and the reasons to do it, you know? Aside from the fact that they don't ask for coffee breaks and they don't do other things, it's going to be crazy when robots really kick in. Once they really get that going for like PCB assembly and stuff like that, I don't know, man.

**Dave Jones:** Yeah. But you think they would have done it by now if it was worthwhile? Because like something like PCB, right? Manufacturing PCB, very labor intensive. Very. Very, very labor intensive. Like cabling harnesses, right? Hopefully I'm going to get a video out on this. And yeah, it's like, you think somebody would have gone, well, look, I'm going to invest money in an automated PCB manufacturing plant. But as far as I'm aware, please, if anyone knows of any automated PCB plant, let us know.

**Chris Gammell:** Well, you're talking about the mechanical assembly of it, right? I mean, not necessarily the, I mean, the surface mount stuff is very well documented. Well, yeah, the actual manufacturing of it. Yeah. Okay. But what I'm saying is that like pick and place machines alone are technically a robot.

**Dave Jones:** No, assembly, that's totally done and dusted. Right. Except for the people who have to massage them because they're very finicky machines. They're still just by the very nature of, you know, the complex tasks they're doing. Yeah. Yep.

**Chris Gammell:** Yeah. So this is, this would be the, you know, putting together wire harnesses, actually like soldering, like maybe large surface mount components that can't go through a wave machine or through a reflow machine, that kind of stuff.

**Dave Jones:** Well, they do have selective wave soldering robots, which can selectively. Yeah, that's true. Yeah. Yeah.

**Chris Gammell:** You can do like masking off and everything. Yeah. But I mean, there are certain components that you can't do, like they can't go through water wash or they can't, there's, there's different steps of the process where sometimes it's just you need human labor to do that kind of thing for now. And I mean, like wiring harnesses are getting, I know that those are getting more advanced as well from a mechanical perspective, but I think it always just comes down to a cost balancing really. I mean, if you can find someone to do it cheaply, then they just, they just go with that. Why would you invest when you can just, you know, pay people standard rates and get away with it?

**Dave Jones:** No, there has to be a financial incentive to do it.

**Chris Gammell:** Right.

**Dave Jones:** And there was, in terms of the pick and place machines, it was a find that they realized, well, look, you know, we can, we can sort of automate this. Let's give it a go. And, and it worked. And they've refined that now. Hardly anyone places components anymore. You know, you, in fact, us, us designers design boards to optimize the amount of machine placeable componentry. Yeah. Because it just makes sense. Yeah.

**Chris Gammell:** If you get to 20 reels instead of 21 on your, and you don't have to do a change, then you, you win. Yeah, exactly. You win the overhead contest.

**Dave Jones:** You know what I want to see? What's that? Which is better than your stupid chip printing machine.

**Chris Gammell:** Well, go ahead.

**Dave Jones:** A, a PCB manufacturing machine. You send your file in, out the other end comes, and you're double-sided, plated through, silk screen, solder mask board.

**Chris Gammell:** Hmm.

**Dave Jones:** Out the other end.

**Chris Gammell:** Kind of like a, so that would be more of like a laying down like a silver nitride kind of, is it silver nitride? I don't care how they do it. Whatever the conductive ink type of thing is, right? Yeah.

**Dave Jones:** I don't, I don't care how they do it, but I want, I want it, you know, sure you've got to feed materials in one end. So maybe, you know, you've got to, yeah, you could say, oh, maybe it's kind of sort of there with the LPKF machines, you know, that etch out that, you know, do the boards and stuff like that.

**Chris Gammell:** Yeah, those are subtractive, though. You're talking about additive, right?

**Dave Jones:** I'm talking about additive. Well, once again, I don't care how they do it, right? I just like put raw materials in one end.

**Chris Gammell:** Well, you care about solder mask, though. That's the main thing that you, that's always the ultimate thing is solder mask. If you can get solder mask.

**Dave Jones:** Well, solder mask and plated through holes. I mean, plated through holes.

**Chris Gammell:** Oh, yeah, that's the other one. Right.

**Dave Jones:** You know, essential, of course. But, yeah, that's what I want. Push a button and out comes, yeah, it's got to be, yeah, the holy grail here would be the solder mask and the plated through holes. I don't even care about silkscreen, but generally, if you can, you know, silkscreen's not that hard. You can put it through a silkscreen printer, right? Like a dot matrix silkscreen printer, right? Yeah. Right. So that's probably the easiest part of the whole thing is silkscreen in the board, so.

**Chris Gammell:** Yeah, that's tough with the, it's always the through holes. That's always tough. But if you're doing like rivets, I mean, they have some of that stuff now where you can, you know, you can insert, you know, do a drill and then do a rivet insert and then try and etch around that or something. But it's still pretty time-attemptive.

**Dave Jones:** But I want it to be completely hands-off.

**Chris Gammell:** Yeah.

**Dave Jones:** A la the Chris Gammell fantasy machine.

**Chris Gammell:** Is that what we're calling it now, huh?

**Dave Jones:** Yeah.

**Chris Gammell:** Come with me and you'll see a chip that's completely printed.

**Dave Jones:** I will pay that.

**Chris Gammell:** Yeah. Get me my hat and cane and I'll start to hire some Oompa Loompas. Some Oompa Loompas, that's it. Oh, man.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Well, we had some, speaking of Oompa Loompas, there were some notes from this week about

**Dave Jones:** How can you go speaking of Oompa Loompas? Speaking of Oompa Loompas. How is that a segue? How is this a segue? Amaze us with your Oompa Loompa segue.

**Chris Gammell:** I don't really, I have nothing. I was just going to talk about chip printing. We have a bunch of stuff that's chip printing-esque. I don't know. There is stuff, and you and I both said the same thing where it's like, oh, everyone's like, oh, yeah, this is the next thing. No, sorry, folks. This is not it, but there were some interesting news items this week for some theoretical, you know, like, what do they call them? Well, there always are.

**Dave Jones:** It's a big, heavily researched field, chip printing, and printing circuits on flexible materials and blah, blah. Yeah, that kind of thing. Yeah. Yeah. There's always something new coming out every week. There's nothing new, so folks. So stop sending in the links.

**Chris Gammell:** No, keep sending in the links. I like it. Oh, yeah. It works day-bye. It gives Chris a little. Yeah, it gives me a little boost. You get to start singing and dancing again, like usual. But yeah, this is at a Xerox Park, which is good. You know, that's another good thing, just to see that. I'm glad Park's still doing stuff. I mean, I thought they had slowed down.

**Dave Jones:** Yeah, that's surprising.

**Chris Gammell:** So that's, hey, power to them. I like seeing that stuff come out. But yeah, they say write print in the, and it's in the New York Times too. So I think the wide dissemination of this article and the fact that they say that it could lead to printing, quote unquote, the circuitry for a wide array of electronic devices. Yeah. Yeah. Well, we'll see.

**Dave Jones:** Speaking of printing. Yes. And the lack of printing. No.

**Chris Gammell:** That's not a bad segue.

**Dave Jones:** Thank you very much. I'm a professional.

**Chris Gammell:** Yeah. That's right. He does parties, folks.

**Dave Jones:** UBM, the huge conglomerate who own practically every online electronics magazine or something.

**Chris Gammell:** All remaining industry rags, basically. It's like one or two total companies left.

**Dave Jones:** Pretty much. Yeah. They're all under this UBM banner. Yeah. Yeah. They've got an announcement. They've laid off some people and a whole bunch of people. And there, here it is. UBM Tech announced a strategic shift towards community-focused media and events.

**Chris Gammell:** To synergize core competencies with maximal profitability. Had they put that in there, but it wouldn't surprise me. That was ad-libbed. That was ad-libbed.

**Dave Jones:** Well, here's the end. Here's the tagline under that. Leads evolution of business-to-business media via integration of event and online communities. Oh. You know. Yeah. It's dripping with BS. I am doing the wanking gesture here, jokes. Yeah. Exactly. Folks, you know. Like, yeah. Yeah. Sorry for the mental image, but yeah. That's okay.

**Chris Gammell:** Yeah. It's, you know, it's industry speak. It's fine. It's weird to think, you know, it's weird to think that at some point there's people sitting in conference rooms analyzing how to better influence you and I and all of our listeners. It's like, you know, it's weird to think about. It's almost like, it's not, I wouldn't say stalkerish, but it's a little creepy, you know. It's like, how about you just give us app notes and fun articles? Is that a lot? Yeah. Yeah. But yeah, so they, it's sad. They, you know, they lay some people off and, you know, the thing that I'm kind of angry about, not angry, disappointed. They got rid of Design East. So the Design West is going on, I think this coming week. But.

**Dave Jones:** Are you going to that?

**Chris Gammell:** No, I'm not going. Right. It's next week, I think. Maybe it's next week. I don't know when it is. Yeah. But yeah, so they canceled the Boston one, which I was actually thinking about going to. Oh, did they? Oh, okay. Right. Yeah. Yeah. That's, so that used to be ESC Boston, but.

**Dave Jones:** That's right. So ESC is dead. Boston. ESC Boston. ESC Boston. But they're still going to continue with ESC Silicon Valley.

**Chris Gammell:** I think that's the only one, because there was Chicago too. I started by going to Chicago. So yeah, they're scaling back. And I don't know. I'm sure that there's reasoning for it, but it's just too bad because it's usually a good way to get to know people on the East Coast, you know, meet up with people there. Good excuse to go to Boston.

**Dave Jones:** Hey, I love one of the examples they give here. Yeah. They are, they're, and, and illustration of the success of one of our things is the 2013 Game Developers Conference, world's largest and longest running event serving game development, blah, blah, blah, blah, blah, blah. A community of over 1 million unique visitors each month. Woohoo. My forum gets more than that. Whoop-dee-doo. I'm sorry. Like, eh.

**Chris Gammell:** I don't know. It's a game site. Sorry.

**Dave Jones:** I just wanted, I just found that figure. Like, they're, yeah, they're, they're boasting about this figure as a huge success and shit. My little forum's got more than that.

**Chris Gammell:** Sorry, UBM. Whoop-dee. Yeah. Well, the other, but the interesting thing is that, uh, I didn't realize though that they, they, so they, they killed a test and measurement world too, but, uh.

**Dave Jones:** Yes, that's the other big news, which makes it relevant here, folks. Yeah. So that's, that's too bad, but, uh.

**Chris Gammell:** I'm sure there'll be other ways to get that stuff, but.

**Dave Jones:** And I don't know if we've ever mentioned it on air, but, uh, they tried to recruit both of us for test and measurement world at various times in the past.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. And we, heh, rightfully. Decline. Decline.

**Chris Gammell:** We declined. We genuinely declined. Yes, we declined. Yeah. Um. But, you know. Politely declined. Yep. It's, it's too bad that, I mean, so that's shutting down too, but the thing I didn't realize though is that E.E. Times hasn't been printing paper since January apparently. I didn't, I didn't realize that December, maybe, maybe if you go back and listen to, we've talked about it, but I don't remember, um, ever hearing that or anything. So, it's interesting because you think about, uh, you know, you think about old analog engineers and, you know, the typical. Graybeard. Yeah. Graybeard. Right. It's like, you know, they want paper and I, I, I, I enjoyed paper once in a while. I just. They want paper and messy benches. That's right. Exactly. We know what they want. No, we don't. Uh. But, you know, a lot of people do like still have, you know, it's the same kind of thing with catalogs, right? I mean, like, leafing through can be much more rewarding than going online and clicking articles and all that crap. So, it's, it's too bad. I mean, it's, uh, it's just kind of, it's just a changes kind of thing. Right. Cue David Bowie. Um. Yes.

**Dave Jones:** So, what are they bloody well going to focus on? Yeah.

**Chris Gammell:** Online.

**Dave Jones:** Do they actually tell you in this article? Does it, like.

**Chris Gammell:** Yeah. Online. I mean, that's online.

**Dave Jones:** Right. Online. And by saying, what, so they're basically going to kill every single print.

**Chris Gammell:** Uh, I don't know. I don't know about that.

**Dave Jones:** Is that the. Yeah. Well, surely that's, that's the ultimate game, right? The goal.

**Chris Gammell:** Probably. You know, I think, who was it? Chris Anderson was talking about that on here, maybe. He was saying, you know, like, or maybe it was on a different thing, but at some point I remember hearing Chris talk about, uh, about having boutique printing and having basically high end, you know, the equivalent of having like people listening to records these days, right? You know, like. Yeah.

**Dave Jones:** Yeah. Exactly. You, you print a full color, gorgeous, glorious book and they want to own it because it's a thing worth owning. It's the aesthetics of it. Yeah, exactly. Yeah.

**Chris Gammell:** Yeah. Yeah. And, and I could see that same kind of thing happening here that if there were people that were interested in it, they pay a surcharge or something like that and, you know, companies pay for it or whatever. Yeah.

**Dave Jones:** And they get the printed copy and then you print on demand. You only have to print.

**Chris Gammell:** Right.

**Dave Jones:** You know, I don't know why they wouldn't do a print on demand model.

**Chris Gammell:** Uh, well, technically they're doing that now, I guess, or they were doing that for. Well. I guess. Because demand is.

**Dave Jones:** I don't know why, why you wouldn't take people's money. If they want a print edition, give them a damn well print edition.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And take their money, you know? Yeah.

**Chris Gammell:** If it, if it makes sense financially, that's usually, that's, that's what it comes down to, right?

**Dave Jones:** Well, maybe, maybe, maybe they've done that. Maybe they're sitting around, look, we've only got a thousand people who are paying for the print edition. It's not worth our while even bothering.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, and, and I mean, there's other magazines.

**Chris Gammell:** So you were mentioning there, there's still a bunch of, uh, tech magazines in Australia.

**Dave Jones:** There are two printed electronics, not including Silicon Valley. They can chip. There's, um, electronics news. I've got right in front of me here. And the other ones, uh, what's new in electronics to industry mags. And they're still printed. I get them.

**Chris Gammell:** Are they ad supported or do you pay for those?

**Dave Jones:** No, they're completely ad supported. They're, they're free. They're industry mags. Okay. So they still follow that traditional model of the free industry magazine because all, you know, it's, because it costs a lot of money to advertise in these things. Right. Yeah. Yeah. It does. Yeah. It costs an absolute buttload. I've posted a link to how much it costs, um, to advertise in UBM with UBM, for example, in there at both online and print media. And it's a metric buttload of money, folks. Um, I linked it in the blog article I did about how not to sell out to, you know, in terms of bloggers not selling out. And, uh, yeah, yeah. Very expensive. No, but let's see. Even in a pissant country like Australia here with hardly any electronics industry, right? We've, we've still got two printed magazines. Yeah. Well, sometimes it's scale too.

**Chris Gammell:** Silicon chip. I mean, you think about the amount of money it takes to run a big company versus a smaller one. Sometimes you can kind of skirt by if you're a smaller, you know, smaller tech rag that might be able to have a small staff.

**Dave Jones:** Silicon chip is an example of the small rag, right? It's still privately owned. There's only like less than half a dozen people working there. Whereas the other two are like owned by bigger conglomerates. Oh, okay.

**Chris Gammell:** So then they, they're just like supported by other, other, uh, divisions. Yeah.

**Dave Jones:** Other things, I guess. Yeah. Although ultimately if it wasn't profitable for them, they wouldn't do it. I'm sure.

**Chris Gammell:** Right. A lot of, yeah.

**Dave Jones:** So they're obviously still getting enough old school advertisers to, you know, um, keep the magazine alive. So what we want to know folks, because Chris obviously doesn't know, even though he's a yank, um, how many printed industry engineering magazines are left in the U S or in your country? I don't get that at all. Other countries, please. Other, you know, yeah. Other countries. How many electronics magazines do you have?

**Chris Gammell:** Yeah.

**Dave Jones:** Trade, trade ones we're talking about here.

**Chris Gammell:** Not hobby. Right. Well, and so there, I mean, there are other examples of like the, the higher end stuff. I mean, like you get like a subscription to like make magazine, right? It's like 15 bucks for a quarter, I think. Right. Something like, yeah, I think it's like 60 bucks a year. And that's a nice, it's a nice magazine, you know, but it's definitely not cheap and it's not, it's definitely not free. It's not ad supported.

**Dave Jones:** So no, no, it's right.

**Chris Gammell:** Right. And they are doing a workshop. Did you, uh, did you see the news from that?

**Dave Jones:** Various news on that.

**Chris Gammell:** Yeah. They, uh, so they did this last year. The first one was last year where they have a lot of familiar names. I think, uh, like Chris Anderson and, uh, I think Zach Hoken from, uh, Hexcelerator will be there too. Uh, Lane from, uh, OSH Park will be talking there. So there's a whole list of people that'll be talking there. And it is really, really nice list. Yeah. That's kind of like a good event. Yeah. New industry conference, um, effectively, you know, same kind of price tag as you'd actually expect from like an industry conference, which I was, I was surprised at last year. Um, but the interesting thing from this year is that they're issuing a call for prototypes, which I didn't see coming. Uh, so basically though, they're like, yeah, you can get up for five, five minutes. And if you haven't taken any, uh, any VC funding or you haven't done any Kickstarter or anything like that, then you can get up and give a pitch in front of all these people, many of whom are well-connected and some are, I guess, going to be investors. Right. And, uh, yeah. So maybe, maybe it's a thing. That's pretty cool. Yeah. So, and it's interesting because it is targeted at like, you know, the open, open source hardware and, uh, and just hardware in general, right. That, that alone is a good start. So if people are interested, they should look into it. There's a, uh, deadline is the end of this week, Friday. So we, we made it before the deadline. We announced it before the deadline. That's usually pretty good for us.

**Dave Jones:** So are we, and going back to the, the, uh, industry, the UBM thing, considering that they canceled ESC Boston, are we looking at the end, possibly the end of industry events like that? Uh, maybe consolidation.

**Chris Gammell:** I don't want to spill doom and gloom. No, I don't think, I don't think.

**Dave Jones:** Consolidation perhaps?

**Chris Gammell:** Yeah. I mean, if anything, it would just be like a couple smaller events, but I'm sure that they'll still going to have one big event. And if they don't, that someone else will, or, you know, somebody else will start it

**Dave Jones:** up. Yeah. That's what I'm.

**Chris Gammell:** Right. Yeah. Or it'll just add, ad hoc happen at like Maker Faire or other, you know, like chaos communication camp. Yeah.

**Dave Jones:** That's right.

**Chris Gammell:** It's just as the landscape changes and there's, you know, different places to, to gather or, or it'll, you know, fragment. Right. And, and, uh, it'll go back to just being embedded stuff. Right. Like the, like ESC used to be just embedded, but then it kind of expanded. Um, yep.

**Dave Jones:** Hmm.

**Chris Gammell:** Ebbs and flows, man. Ebbs and flows. Yeah.

**Dave Jones:** Well, the same thing happened here. We used to have an electronics industry, um, event here every year and then it died out due to, well, they tried to build it up to, you know, include everything else, you know, like a big, huge industrial machinery and, you know, and then it became like five in one, you know, so the electronics stuff just got eventually, you know, and they eventually just discarded the electronics thing. And then a couple of years later, um, it sort of came back. They decided, right, we want, you know, or another new company came and decided we want just an electronics exhibition again. And it just started up again from nothing.

**Chris Gammell:** Yeah. Yeah. Well, that's kind of the same thing happened with like, uh, the CES, right? CES got really, really big. And then this year, um, South by Southwest, which we talked about a couple of weeks ago, that got really big. Right. And so it's like, you know, it just, yeah, it all flows around and everybody's looking for the hot new thing to go to or whatever. Variety. I mean, that's the thing too, is variety. Variety does help. So if this shake things, shakes things up, it's fine with me. I just want to go to Boston again.

**Dave Jones:** But you've got to be careful. The variety can also dilute it.

**Chris Gammell:** I suppose. I don't go to many conferences, to be honest. I mean, like, look at when I've been an active engineer, Dave, right? I mean, like I, I effectively started doing electronics, not, not in a fab in 2008 again. Uh, so I don't know, I don't know if you were paying attention since 2008, but, uh, not a whole lot of money floating around these days.

**Speaker ?:** No.

**Chris Gammell:** You know, I talk to people about that. They're like, yeah, you know, I used to go to trade shows and, you know, I'd be like three or four a year, you know.

**Dave Jones:** Yeah. The company had sent me on all these junkets. Exactly. Yeah. Yeah. Yeah.

**Chris Gammell:** You know, like I'm boozing on the company card and stuff like that. And it's like, no.

**Dave Jones:** Now they won't even give you a day off to go to the, on your own dime.

**Chris Gammell:** I've been, yeah, that's how I've almost always done it. I've always done it on my own dime. I've usually taken time off because I do it for networking, right? That's how I got to know a lot of people. Yeah. That's right. You know, that's, so yeah, it's, it's, it, and I do, I do suggest that. I mean, it is, it is worth it from a professional development standpoint. Hopefully you can get in for free by, you know, being a blogger or some other kind of sheisty way like I did. But, uh, um, if you can swing it, yeah. I mean, even if you just go to go to walk around the floor and meet people, that's, that's what that's all about is meeting people.

**Speaker ?:** Yep.

**Dave Jones:** That, that's, if you are one of those social engineers, if you're one of those, uh.

**Chris Gammell:** Even if you're not. Even if you're not. Social retards, though. Yeah, come on. You're not. We know you're not because you've taken video of yourself at this.

**Dave Jones:** Yeah, but, no, trust me, I'm not very, I'm not a very social person.

**Chris Gammell:** Well, I'm not either. I mean, like, I, it's easy for me. Especially way back in the day.

**Dave Jones:** I mean, oh shit, you know, I wouldn't talk to anyone.

**Chris Gammell:** You've become a social butterfly since then. You know? Yeah. Yes.

**Dave Jones:** No, but look, right? No, just, the fact is, right, how long have I had this, I've had this lab for a year and a, I don't know, year and a half or something, right? Yeah. Yeah, right, let's call it a year and a half. Guess how many visitors I've had to my lab?

**Chris Gammell:** Uh, three.

**Dave Jones:** Yeah, about that. Yeah, okay. Right? And that's how social I am.

**Chris Gammell:** I noticed I haven't gotten an invite yet. I don't know, Dave. Right. I'm waiting. I'm sure it's in the mail. Probably just a slow US mail or something, you know? Getting over the ocean.

**Dave Jones:** But I thought you were scared of our spiders.

**Chris Gammell:** Oh, I am. Oh my god. Ugh. Ugh. Pussy. Yeah. Ugh. So what else should we talk about? What else we got on the list? Yeah. We've pissed away the show already. Have we? Oh, we should, oh, we need to talk about our sponsor then. Have we? Oh yeah, we definitely do. We're supposed to do that halfway through. Yeah.

**Dave Jones:** Yeah, we kind of implied the other week. We got it wrong last week. Well, we got it. I'm trying to get us off the hook here. Come on.

**Chris Gammell:** No, we were wrong.

**Dave Jones:** Well, yeah, we assumed that this via ASIC stuff was reprogrammable.

**Chris Gammell:** Right.

**Dave Jones:** Filled reprogrammable. And of course the name alone should have given us a clue. Via what? Via F-E-G-A? Alone McFly. Yeah, yeah. Yeah, ASIC, you know, in the name. Yeah. Usually implies non-reprogrammability.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah, sorry about that. It is a mask process. Right, yeah. A cheap mask process. It's going to be a cheap mask process.

**Chris Gammell:** Right. But still, it's a, you know. We talked about that earlier in the show, rather, about the masking process and doing the metallization layer. It's basically that. So if you look at all the different, like, via one through, or VCA, is it? Via configurable array. VCA 1 through VCA 12. And then there's a couple others for, like, the ARM-based one and everything. All of those are basically, like, that's proven silicon, right? And then you basically do... Join the dots. Yeah. You do the, you join the dots in the Via Designer software, which is what is actually sponsoring the show. And, yeah. That's actually what ends up telling the fab what to crank out. What to actually make.

**Dave Jones:** Right.

**Chris Gammell:** That's right. But yeah, the benefit of that being that it's already tested. So the actual underlying stuff's tested. You're just kind of hooking it all together. So effectively, it's kind of like moving a PCB down into the metallization layer. And that's probably an easier way to think about it. Yeah. Yeah. Hopefully I'm not saying that wrong again.

**Dave Jones:** You're just getting the individual... You're buying the individual chips from DigiKey. You know they're all thoroughly tested. You've got the data on them.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? And then you just... Yeah. You manufacture your PCB. And, yeah, sometimes you might have to re-spin it because you goofed your PCB. Right.

**Chris Gammell:** But that's your fault. Yeah. That's a very... Yeah, exactly. Because the chip already works, right? It's your own dumbass fault for not... Yeah. For not thoroughly checking. Yeah. Yeah. And it's interesting because it's... I mean, so it's actually the cost stuff. I mean, so they also do all the talking to fabs and they work with a bunch of different fabs for that kind of thing. So it ends up bringing the cost down. And that's another advantage of them. So people should check it out. Go to viadesigner.com slash the amp hour. And then one thing that we heard about after we published last week was that you get a free year membership. It starts as a month trial, but it actually will go a whole year. There's a code. I think it's AMP100. But we'll have that in the comments or in the show notes from this week.

**Dave Jones:** And you get the software free for a year. It's normally like 500 smackers, isn't it?

**Chris Gammell:** Yeah. Yeah, exactly. Yeah. Nice. Benefits of being an amp hour listener is not just a chance to wear t-shirts anymore. It's also free software.

**Dave Jones:** And that might be a good thing to put on your resume, too, if you've used a tool like that. Even if you just played around with it and you've, you know, yeah, I've played with some ASIC design software. Yeah, true.

**Chris Gammell:** Yeah. I mean, this is still like system level type of design, right? I mean, it's knowing how you need to hook together different, there's transistors on board, caps and everything else, right? And then larger stuff like ABCs and everything else, too. Yeah. Yeah. And it would be good software to use, especially as it grows in popularity. So I think it's always good to have that kind of stuff on a resume. For sure. It's interesting as a comparison point. So I saw this on Planet Analog today. It's actually a chip consultant was writing this article. So this is like the other option, which is much, much more research intensive. But it's also interesting. And I think we've mentioned it before, but there's actually an open source layout program. So if you wanted to not just, you know, do the layout and have a proven chip, but then actually try and dive down into the transistors and everything. Yeah. This allows you to do that. Now, that would scare the crap out of me. That would scare the crap out of me. Yeah. Oh, yeah.

**Dave Jones:** No, exactly. It's a lot of work. This is a lot of work compared to something like VRASIC, right? Yeah. This is like, you know, you're designing your own chip transistor by transistor, folks. Right. There's a lot that can go wrong there. Yeah. And it's very intensive to learn that sort of thing. It is. A tool like that as opposed to a higher system level one. Yeah. But if you need to for some reason, because you really absolutely need, you know, a transistor transistor level custom silicon, then you can do it for about three grand.

**Chris Gammell:** Yeah. Which is cool. And I mean, that stuff is, it's an interesting thing of just like, you know, I took some chip design classes in school, but I didn't know what the hell I was doing. Right. I mean, the fact that there is that software out there too, it's pretty cool to be able to look at all that stuff, you know? Absolutely. It's crazy. You know, it's just, it just always seems like it's, it's way out of my reach, you know, that it's just impossible, but it's no. Yeah. People are out there making that stuff. And in terms of analog, if you get, if you get decent at it, you can make a lot of money. Oh yeah. Yeah.

**Dave Jones:** But, but to get decent at it, you have to actually spend that money and spin the silicon. Yes. Yeah.

**Chris Gammell:** You can't just, you know, simulation is not enough.

**Dave Jones:** But once again, this is something you could put on your resume. Yeah. You know, I've played around with and used these design tools, these ASIC design tools. Mm-hmm. You know, you don't have to have actually made the silicon.

**Chris Gammell:** Yeah. Yeah. And I mean, it's, it's not going to be perfect either, right? Because if you, if you try to go to TI and be like, well, I learned on electric, right? This open source chip design program. They're like, well, we use Cadence, so see you later. Yeah. Or whatever. Yeah. Yeah. Yeah. Yeah. Cadence or what's the other one?

**Dave Jones:** Oh, I don't know. Mentor. Yeah. Do one. Yeah. Yeah. You're right.

**Chris Gammell:** That's it. Yeah. So those are the two. And it's like, you know, usually the tool, knowing the tool is just as important sometimes because of like knowing the design flow and everything else. But it's, it's, it's interesting. I don't know. I thought it was cool.

**Dave Jones:** The catch folks is that it takes four months to spin your chip. That too. Yeah. So you submit it and yeah, you get your chips four months later. Right. Yeah. So it's not exactly a, a fast turnaround.

**Chris Gammell:** Right. And we should clarify, this is for, if you're designing your own thing from scratch, maybe I shouldn't have brought this up after the, the via designer to advertise or sponsorship notice, but yeah, this is if you're spinning your own chip from scratch, then that's. Oh yeah. Yeah. This is.

**Dave Jones:** Yeah. Yeah. Yeah. And then, but before that, it'd probably take you four months to design your bloody chip. Right. Exactly. Whereas it would suck like VRA, so it could take your, you know, a day, you know, because you build at your higher level abstraction, you know. Well, it's the same kind of thing.

**Chris Gammell:** Using preexisting blocks. If you had PCBs back in the day, right. I mean, I'm sure that you spent more time when you were, when you were designing PCBs back in the day, right, with all the tape out and everything, making sure that's right. Oh yeah. Yeah. Because it was so much more expensive, so much more time intensive that you really, really, really wanted to get it right versus these days, it's just like, okay, it's done, you know, get it out the door. Yeah. Hope it's right.

**Dave Jones:** Get it out the door. Oh, I can re-spin in a couple of days if it's wrong, you know, who cares. Exactly. Yeah. Yeah. And that's the benefit, right?

**Chris Gammell:** That's the benefit of moving to faster prototyping type systems and just having more commodity type hardware like, like PCBs are at right now. So. Hmm. And once chip runners, you know. Yeah.

**Dave Jones:** That is interesting, actually. I don't know whether it's just old age or whether I'm looking back with fonder memories and what they were, but I can't recall an incident where I actually goofed a hand-taped layout. Hand-taped PCB layout.

**Chris Gammell:** Yeah.

**Dave Jones:** Because as you say, you put a lot more effort into it. You have a lot more invested in it.

**Chris Gammell:** Yeah.

**Dave Jones:** I can't remember. I don't know.

**Chris Gammell:** I don't know.

**Dave Jones:** Yeah. But of course, I've goofed plenty of PCBs in my life. Me too. Using modern tools, you know. Ah, near enough. Finished. Ah, tick. Send it out to the fab, you know, and you get it back. Oh, do. Yeah. You know. I goofed something up.

**Chris Gammell:** Well, this is a question I had for this week is actually something I've run into with, and maybe you don't ever run into this, but the thing that keeps hitting me over and over again is like, and I think this is still my youth showing and my inexperience showing, but like, I have an idea, right? I'm working on something. I have an idea. I say, okay, idea, ready to go. Let's go. And I work on it, work on it, work on it, work on it. You know, and then like a month later, I run into a brick wall and I'm like, oh, this isn't going to work. Right? And then I, so I back way up. And then I start and I say, let's go. I have idea number two. We're going to work on it. You know, like, and then two months later I say, nope, that's not going to work either. Right? And, and basically my question is, is how do you teach that like early iteration and like the, you know, like, I don't know. I think, I think it's just like a, a natural thing to, for, for young engineers to just say, well, the first thing, of course it'll work, you know, and just go.

**Dave Jones:** Well, there's, there's two different sides to this. I think one is that in, in your case, are you talking about your work projects or your personal projects? Yeah, both actually. Right. Because I find that with my personal projects, that is a lot more likely to happen.

**Chris Gammell:** Okay.

**Dave Jones:** That I'm going to change my mind and change direction and go back to the start again.

**Chris Gammell:** Okay.

**Dave Jones:** And, you know. Yeah, we've heard about that, right?

**Chris Gammell:** Power supply project.

**Dave Jones:** Power supply. All right. I've done five different variations of my power supply project at least, you know, and four different ones of my micro watch and, you know, all sorts of different things.

**Dave Jones:** All sorts of different things.

**Chris Gammell:** I think some of that is because you want to be working on certain parts of that too, right? The design is the fun part. The dreaming is the fun part.

**Dave Jones:** Yeah, it's the fun part. Yeah, exactly. So I go, oh, it'll be fun to start with this new idea, you know? Yeah. So, oh, yeah. I, you know. Yeah. Whereas at work, you can't afford to do that. Well, you can less afford to do that because you've got a deadline and you've got a, you know, and people are relying on you and, well, your job's on the line and, you know, and, well, you just do it, you know? Yeah. I mean, like it's something in your brain that switches into a different mode that allows you to, you know, allows you to battle through and not go back to the start and try again.

**Chris Gammell:** Well, sometimes you're just told you're not allowed to go back to the start too. That's another thing. Well, yeah. No, there's no more money. If you don't do this, then we're all, you know, gone.

**Dave Jones:** The entire 10 million project is riding on you. Yeah.

**Chris Gammell:** Yeah. I mean, it's tough. I mean, I guess at a certain point, like you just have to kind of eliminate some of the things you know won't work and then just kind of start running with the next thing that's available or the thing that's most likely to work. But I don't know. It just seems like, it seems like a youth-induced situation still, you know? Like, of course this will work. Yeah, yeah, yeah, yeah, yeah. This will be fine, you know? And then slam. You know, you hit that wall. You know? Yep. You get smacked by the large stick of reality, you know? I don't know.

**Dave Jones:** Because with the personal projects, yeah, you often get blinded because you're so excited by the idea that you might miss some practicality down the track.

**Chris Gammell:** Yeah.

**Dave Jones:** Whereas with work ones, I'm going, oh, this isn't my idea anyway. Who gives a shit? Okay, I'm only going to focus on, will this work? You know? Yeah. Yeah. Because you don't want to look like a dick. Whereas your own personal projects, you don't care if you look like a dick.

**Chris Gammell:** Right, right. You're trying to maybe dream blue sky a little bit more, dreamscape it, right?

**Dave Jones:** Yeah, yeah. Yeah, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** But at work, because it's usually not your idea. You go, oh, right, I've got a job to do, and I don't want to look like a dick. Yeah. And so therefore, you're going to focus on all the little nitty-gritty details that you know need to be right.

**Chris Gammell:** It's a question of how much R and how much D you're doing, right? I mean, I guess that would be the ultimate thing. If you're doing a lot of research, then you do have to do a lot of iteration and kind of stepping through different ideas. But even in that case, right? Yeah. So like I saw an article today about how they prototyped Google Glass in like a day or something like that. Like just a basic concept. But even with that, it's like, how do you go from saying, okay, well, this works in this limited case, and then trying to expand it to, this will work in every case, right? I mean, like, I don't know. It just seems like-

**Dave Jones:** Oh, well, that's 20 different iterations. I mean, that's, you know.

**Chris Gammell:** I guess so. Yeah. I guess you just need to throw a lot of stuff at the wall, right? I don't know. Yeah, yeah, of course. I was just thinking about it today and thinking, man, I still got a lot to learn. I mean, that's a very good thing, right? I like that, that it's not like easy yet. But on the other hand, it's not easy yet, Dave. Yeah. Stressful.

**Dave Jones:** But stress is how you learn, right?

**Chris Gammell:** That's how you learn. Yeah, yeah.

**Dave Jones:** Yes, I think so. And you learn by failing. Yes. That's what I've always said. Yes.

**Chris Gammell:** So we had questions from, once I had said that we weren't going to have a guest this week, I asked for some questions. And on Facebook and by email and a couple other ways, people had sent in questions. So we should get to some of those. Shoot. I think we might have covered this before. But two different people asked about it. Yeah.

**Dave Jones:** We've always, we always say that and we always have covered, just assume that we've covered everything on the show. Okay.

**Chris Gammell:** We've definitely covered this before. I can't believe you guys haven't listened to episode. I don't know. But yeah, FPGAs are always a big stumbling block for people and how to get started with them and stuff like that. And so that was one of the questions of not just where to start, but also what to start with and projects and how to actually dig into it.

**Dave Jones:** And I've got the answer for that. Oh, good. The universal answer to starting with FPGAs, and it's very similar for micros and everything else, is start with a working example. Buy your demo board that has a working example and then work backwards. Just get it going and then figure out how FPGAs and everything and all the configuration fuses and everything else works later.

**Chris Gammell:** Yeah.

**Dave Jones:** And if you want to copy their example circuit, right? And then figure it out how. Don't try and figure out how their example circuit works and then implement it in yours. Just copy theirs and then work backwards.

**Chris Gammell:** Yeah. Yeah, I think they're getting a little cheaper, but I had started on... I had done some work with some of the embedded micros before, or the soft core micro stuff from Xilinx and Altera before. And that was fun because it was just like a... I mean, like I said, those are a little more expensive. But if you have... Especially if you have micro background, it's tough to make that switch. You know, it's... Yeah, yeah, yeah. So... But we've also mentioned before the Papilio, I think it is, or Papilo. Yep. I've got one of those, yeah. And then also Zess, Dave Van and Bout's company.

**Dave Jones:** Yeah, there's many of them. There's DigiLent and all sorts of ones out there. Right. And the thing is, they're so hideously complex. They can be. That if you try and start from scratch, right? Yeah. You know, it's just not going to work. And when it doesn't work, you don't know what the hell is wrong. Right. It could be a combination of 10 different things wrong. And you think you solved it. No, it still doesn't work. Still doesn't work. Still doesn't work. Oh, I'll solve another problem. Still doesn't work. Oh. Right? Yeah. Start with a working example, then work backwards.

**Chris Gammell:** Right.

**Dave Jones:** I like that. That's the only way to do it. Otherwise, you'll just get frustrated and you'll go, these FPGAs are shit and I'm never touching them again. Nothing works.

**Chris Gammell:** Yeah. From a contextual standpoint, I mean, like, actually knowing why to use them, that's a whole other thing. I mean, and there's a lot of stuff out there. But, I mean, DSP is a big one. So, if you need to, like, do filtering. Anytime you need to do, like, lots of iterations on something. So, if you think about, like, math operations, that can be really good in an FPGA. Because even, like, DSPs, like, the DSPs, the chip, those are often just micros that are running really, really fast that have dedicated hardware to that kind of thing. Versus an FPGA, you can actually start to, you know, level out the logic and run things in parallel. And that kind of thing, that was always my favorite side of it, was actually getting to do parallel processing and stuff. Parallel is the key.

**Dave Jones:** You know, if you're doing, you know, high-speed serial to parallel conversion or something like that and you've got 10 channels or something like that, yeah, I mean, it is the best solution.

**Chris Gammell:** FPGAs are really, really good estate machines, too. I mean, you can do estate machines, obviously, and micros. But FPGAs are great at that kind of thing.

**Dave Jones:** But if you're just running a soft core and that's it in your FPGA, you're basically wasting your time, money, you know, package, space, power, everything. Right? You just, no. No. Right? You've got to have something else, VHDLE in there. Yeah. Or Veriloggy in there.

**Chris Gammell:** Right. Or if you're planning on messing up a lot, that's another thing. But in those soft core flows, right, you know, where you do have a processor in there, you don't want to, like, change it around a lot because then you have to recompile all your microcode for that. Yeah, yeah. That's right. Mess. That is just a mess. So there's a lot of cool things you can do. But, yeah, it's, like Dave said, starting from a project can really help. So, yeah. Good luck, guys. You can do it. You can probably, I'm sure, EEV blog forum people would happily offer some projects.

**Dave Jones:** Yes, I have a dedicated FPGA micro section there. You can ask. There you go.

**Chris Gammell:** Yeah. All right. We'll link that in, too. Yeah. More questions? There was a question from Kenny about choosing op amps. Oh.

**Dave Jones:** Choosing op amps. Oh, God. How long is a piece of string?

**Chris Gammell:** How long is, what does that mean?

**Dave Jones:** Well, like, how can I choose? He's basically asking, how can I choose, you know, have you got any suggestions for choosing op amps? And it's like, well, that's one of the how long is a piece of string question.

**Chris Gammell:** I don't still get that, but I'm guessing you just mean there's a lot of options. I don't get it.

**Dave Jones:** This doesn't translate to American? I don't think so. No, I don't think so. How long is a piece of string? You don't know the phrase, how long is a piece of string?

**Chris Gammell:** No, I don't think so. Seriously. I think we've reached an impasse, Dave. Join us next week as Dave and I fight about different Aussie-isms.

**Dave Jones:** Well, it's like, I thought this was pretty much universal around the world. I didn't think it was an Australian expression at all. Maybe it is.

**Chris Gammell:** Maybe I'm just, maybe I'm just. You're not cultured enough. Yeah. Yeah. Yeah. I'm not cultured enough, says Dave. Yeah.

**Dave Jones:** I'm the epitome of culture. Right, right, exactly. Well, the clue to it is in the nature of the statement itself. How long, if I ask you how long is a piece of string, you're going to go, huh? Yeah. Yeah. A piece of string is however long you make it, right? Similar thing here. Like, you know, it's, how do you give general advice? Yeah. There's so many answers that you don't, you know, I mean, it's hard to answer.

**Chris Gammell:** So, here's the thing. So, Kenny was asking about, he has an ultrasound and transducer, and then the frequency of operation is upwards of 40 kilohertz, right? Yeah. And then he says audio op-amps won't work, which is good, because that's, I mean, he recognized that to start with, right? Because- But why don't they work? Because of the gain bandwidth product. That's what he's saying. Although some of them do have higher gain bandwidth products, because in op-amps, you need more gain bandwidth product if you're going to be doing feedback and everything else, right? So, uh-

**Dave Jones:** The gain bandwidth product, for those who don't know, the gain of the op-amp changes depending upon the gain- the bandwidth changes depending upon the gain of the op-amp you have. So, if you're operating at times one, yes, that one megahertz op-amp is going to work to a megahertz. Right. But if you ever gain a 10, wah, or a hundred, wah.

**Chris Gammell:** Yeah, it starts to roll off.

**Dave Jones:** The bandwidth is going to drop proportionally.

**Chris Gammell:** Yeah. And that's just from the internals of the op-amp and everything else, the compensation cap in there, or whatever that cap is called.

**Dave Jones:** That's if you have a compensated op-amp. That's true. There's another difference between op-amps. You can have compensated and uncompensated op-amps. General rule of thumb, compensated op-amps, generally you want to try and use them because they've been optimized to be stable. Whereas if you get an uncompensated op-amp, all bets are off. Good luck. Do it yourself. Do it yourself. Make sure that thing's stable yourself. Right.

**Chris Gammell:** I know this would be a very unpopular piece of advice if Bob Peace were sitting here still, but he's not. So LTSpice is always at your disposal, right? I mean, there's tons of Spice programs out there, and so that's a good way, especially because those kind of things have it built in. Now, it seems like he has cost in mind, so that's a good place to start too. I mean, you can always go to a distributor and sort by price.

**Dave Jones:** You can go to DigiKey and sort by price. That's how you start. Exactly.

**Chris Gammell:** Or, in this case, since it is a defined application, right? I mean, he's talking about ultrasonic transducer. You can go out, you can find an app note for the same kind of thing, right? So you find, you know, LM whatever it would be, you know, not 324, but whatever the part might be, right? And then you type that in, you say similar parts, and you get a whole list of parts that are in the same spec range, and then you can start to optimize for price more. And if you start with an app note, and they give you a certain part, and it's $20, and then you go and search for other ones, and they're all $20, well, you need to look at your application more and see if you actually need the specs that you think you're asking for, right? I mean, or you're just priced into an expensive market, and you just have to swallow it. You know, like, that sometimes happens. You know, if you need super precise or super fast, or, you know, then you go to eBay.

**Dave Jones:** And one thing I would say is that, are you driving a line at all?

**Chris Gammell:** Yeah.

**Dave Jones:** You know, because once again, driving a capacitive load can be a killer for an op amp. There's another design criteria.

**Chris Gammell:** Right.

**Dave Jones:** You know? Right. Is that transducer? Are you using this amplifier at the transducer, and then driving a line to something else? If you are, well, there's a whole different requirement.

**Chris Gammell:** Yeah.

**Dave Jones:** So, look out.

**Chris Gammell:** And, you know, this kind of advice I give of looking at an app note, that I think me from four years ago, or five years ago, would have looked at me and, you know, put an ugly look on my face and be like, oh, no, I want to design it, right? And it's like, well...

**Dave Jones:** Right. You can.

**Chris Gammell:** I mean, you could start from scratch, right? But it's kind of the same thing that Dave was talking about with FPGA, right? Sometimes starting from a known quantity can help, and then you can start to optimize for what you really need in the case of cost or, you know, more performance and that kind of thing. I don't know. So, actually, Matt Richardson did a video today about artists stealing, you know, like, basically, there are no original ideas. We've said that a lot on this show before, right? Right. Yeah. You know, there's... It's a tough mental switch to make because I think, especially, like, in school, it was always like, oh, I'm going to design stuff when I'm done with school. It's like, well, yeah, design stuff, but more remix stuff and redo stuff. Yeah. You know, like, it's like, there's only so many levels there.

**Dave Jones:** That's the thing. Electronics is one of those fascinating industries where you can achieve a hell of a lot with not a huge amount of detailed knowledge, right? If you've got an idea in mind, you can find and take all these already working example app notes or whatever and piece together block by block and you can get a really incredibly... You can do some incredibly advanced stuff with not much detailed knowledge of how those op-amps work or, you know, all that sort of thing.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** Just carefully take these example circuits. I mean, you can get by a whole career not knowing how an op-amp works inside, right? Sometimes, right?

**Chris Gammell:** Probably, yeah. Yeah.

**Dave Jones:** Yeah. I mean, that's not uncommon. You just never have to worry about it sometimes.

**Chris Gammell:** I don't know if it's not uncommon, but yeah.

**Dave Jones:** Because, right, in this case, right, well, no, right, but it does actually happen. You want an ultrasonic transducer, there's app notes out there that show ultrasonic transducers and which op-amp they've used. Somebody smarter than you has already chosen it. Bang, it works.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, and it's a...

**Chris Gammell:** I think that's a mental switch, too. Like, some people want to dig down into the details, right? But sometimes, even if you do want to dig down into the details, your boss is breathing down your neck. You're like, no, you got to get it done, you know? So, there are different levels, right? I mean, it's always just about optimizing for what your situation is. And making that mental switch was tough, but it's just life. It's just, you know, it's like, okay, well, if I really want to learn the details on something, I come home and I work on it, right? I just learn about that or I read about it, and that's how you get your design jollies, you know, that's... Or you go work for a chip company, you write the damn app note yourself. Right. And talking to people that do that, that doesn't sound like fun a lot of times, too, because it's, uh... And you... Yeah. I'm doing this wrong. A month later, I'm doing this wrong. A month after that, oh, the silicon isn't working right. Oh.

**Dave Jones:** Crap! And if you want to know how long it takes to actually write stuff... Oh, yeah. I just put a post last night. Yeah. Because somebody on the forum asked, somebody had the idea that, oh, I could make money by writing app notes, right? I could make, like, little app, you know, little design brief notes or something. And they said, if you release one of those a week and X thousand of people bought it, you can make X thousand blah, blah, blah a year, right? And they made the offhanded comment, sorry, I forget who it is, that, oh, it'd only take you three hours to write. And I just laughed, right? Yeah. My reply was, it only takes three hours to write an app note laughing in MockyCon, right? Right. You know, like... And then, to prove it, I wrote a blog post last night, a text blog post. And you can read it. It's just been uploaded of how I built my new video machine or specced my new video machine. It took me two hours and 15 minutes to write that blog post.

**Chris Gammell:** Right.

**Dave Jones:** I timed it with a stopwatch.

**Chris Gammell:** Yeah.

**Dave Jones:** And that's just writing out text, right? Oh, yeah. It's a long blog post, but it's like...

**Chris Gammell:** That's without the research and everything else behind it, right? Yeah.

**Dave Jones:** The research, the diagrams, the, you know, everything else. I mean, holy crap.

**Chris Gammell:** Right. So the golden standard...

**Dave Jones:** It could take you a month to write a good app note.

**Chris Gammell:** Yeah, exactly. Jim Williams spent multiple months on app notes, right? The best ones. There was 140-page app notes, you know? Yeah. You don't write that in a couple hours. That's crazy.

**Dave Jones:** That would have taken him six months. He would have worked on that for... Yeah.

**Chris Gammell:** It's crazy. Yeah. And it's a lot of... I like that with a lot of app notes. You know, like, it's interesting that it still exists in the marketplace that these chip companies are willing to do that kind of stuff, but it's because it's... Don't kid yourself. It's because it's a sales tool. It's because that's how they sell chips. No, of course. It's just by offering these example circuits, right? I mean, that's why they do it. That's right. Hey, wouldn't take...

**Dave Jones:** And it works. We're whores for that kind of thing. Even, like, I'm a whore. I don't want to reinvent the wheel. I don't want to spend time dicking around. I'm too busy getting my fantastic widget idea up and running. I don't care about how the op-amp stays stable on that thing. No, I just want to use a bloody circuit that I know is going to work. Yeah.

**Chris Gammell:** The cult of Dunn.

**Dave Jones:** So I don't have to re-spin my freaking board. And, you know, when my design comes back and not working, I don't want to have to breadboard that up and make sure my op-amp's stable.

**Chris Gammell:** Right. For that, I just want to... It's fun at first. I mean, it's fun at first, but... Oh, yeah, of course. Five times? No, after wallet. It might still be fun. Ten times? Eh. Yeah. You just got to optimize for your situation, right? That's what it's all about.

**Dave Jones:** So to answer Kenny's question, that's a pretty basic requirement. An ultrasonic transducer amplifier, really. There's probably, you know, 100 op-amps on the market that could probably do it. So...

**Chris Gammell:** Yeah, we did not look, so we can't say as much, but... No.

**Dave Jones:** No, but there's a lot. It's not a very, you know... Like, you didn't tell us about noise floor or anything else, but, you know, when you're talking about ultrasonic transducers, eh, it's like, you know, what? You want to test it? You're measuring a distance? Is that the, you know, thing? Eh, it's going to be near enough. Yeah. There's not really large spec requirements on your op-amp there, I'm guessing.

**Chris Gammell:** If you are interested in op-amps, there was this really cool video that... I forget who posted it. I think someone on Facebook posted it, but of actually Harold Black, the guy that invented negative feedback, talking about negative feedback. It was crazy. Right. So it's this video from the 80s, and he's like, he's old by this point, but he's talking about actually, like, the moment when the inspiration struck him. It was actually on the ferry staring at the Statue of Liberty. Oh, sweet. Yeah, it's this really cool video. And actually, all of these videos from the old AT&T, like, there's a lot of old Bell Lab stuff. So I'll post a link to the video.

**Dave Jones:** Yeah, I'm looking through the list. I didn't know about this.

**Chris Gammell:** It's a cool channel.

**Dave Jones:** It looks awesome.

**Chris Gammell:** Yeah.

**Dave Jones:** All these retro videos.

**Chris Gammell:** There's a really good one. I was watching on there of the first... They did this press conference for the video phone back in the 70s, right? Right. And it's like, it's exactly what you'd expect, right? It's totally trumped up. It's like, you know, oh, they call it the picture phone, right? And it's like, you know, but it's totally a press event, right? It's like, oh, we're breaking ground today. I'm watching it now. It's hilarious. Yeah. We're breaking ground today. It's like, well, yeah, I mean, they were, but it's like, it was an undefined market. And, you know, obviously, even today, as we have smartphones in our pocket, we're not doing video chats still. So some of what because of AT&T, right? Because of data rates.

**Dave Jones:** This is great. This is a great channel. It really is. AT&T Check and Tech Channel.

**Chris Gammell:** Yeah. We'll post a link to it.

**Dave Jones:** It's just got all these old tech videos, retro tech videos. This is great.

**Chris Gammell:** Yeah. Oh, man. There goes my day. There goes Dave's day.

**Dave Jones:** Yep. That's okay. I don't have a real job. Yeah. Right.

**Chris Gammell:** Yeah. So this is great. Yeah. Oh, anything else for this week? That's a goldmine, folks.

**Dave Jones:** Oh, no. Look, we're almost 20 minutes over.

**Chris Gammell:** Yeah. So we will try and have t-shirts by next week. If not that week, then the week after. And they will eventually make it. And they will be in the store. And they will be awesome. Yep. Should we start saying the catchphrase as we, as we, we have two different taglines that we're using? The amp hour, colon, keep current. And then the amp hour, colon, potentially different opinions. Which are both nerdy and punny. But they look good on t-shirts. Yep.

**Dave Jones:** Well, it's not so much a slogan. It's the logo that we've, that the graphic artist has come up with. Of course. Of course.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So it's not really a slogan t-shirt. It's more of a logo. No. No, no.

**Chris Gammell:** We'll work on those after that. I have a whole list of others. If people like t-shirts, then we'll start cranking them out and having them reasonably priced sales.

**Dave Jones:** All right.

**Chris Gammell:** We'll see you next week, Dave.

**Dave Jones:** All right. Are we going to have a guest?

**Chris Gammell:** Yeah, sure.

**Dave Jones:** Yeah, sure. Yeah, right. Send in your questions for us next week as well.

**Chris Gammell:** All right. See you later, man. All right. Say it. This episode of The Amp Hour was brought to you by Triad Semiconductor. If you need maximum flexibility in both the analog and digital realm, check out the Via ASIC and associated Via Designer software. Visit viadesigner.com slash theamphour and enter AMP100 at registration for a free year subscription, a $500 value. administered administered in administered administered administered administered administered administered

**Speaker ?:** administered administered administered administered administered administered administered x x x Thank you.
