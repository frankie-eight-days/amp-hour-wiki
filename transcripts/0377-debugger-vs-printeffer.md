---
episode: 377
title: Debugger vs Printeffer
url: https://theamphour.com/377-debugger-vs-printeffer/
---

**Chris Gammell:** Hey, everyone. Quick announcement before the show starts. This is actually announced also at the end of the episode, but I wanted to make sure I get the word out there. I'm going to be at two different conferences this week, and I'd love to meet up with you. The first one is the Things Conference in Amsterdam that's happening February 1st to the 3rd. You may recall Richard from TWTG was talking about that. I'm also going to go down to Brussels, Belgium and go to FOSDEM, which is where some of the KiCat stuff happens, but lots of other open source stuff happens. That's February 3rd and 4th. So if you're going to be at either of those, I'd love to meet up. Either hit me up on Twitter or send an email to chris at theamphour.com. See you there. This is the Amp Hour Podcast. Released January 28th, 2018. Episode 377. Debugger vs. Prince Epper.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. One month later. What? You're like cut in with the Dick Tracy style. Or like Batman.

**Dave Jones:** Hi Dave. One month later, I actually show up. Yeah. Hey, man. How was your vacation? Not long enough.

**Chris Gammell:** Oh, well, you know, never is. You were seaside? Yeah, yeah. Or oceanside? Yeah, oceanside. Yep. Australia is not on fire? Is it? No, it's not on fire. Why?

**Dave Jones:** It was supposed to be on fire, was it?

**Chris Gammell:** I just remember someone showed me like 42, 43 C temps. Oh, it was 45.

**Dave Jones:** Yeah. Oh, seriously? Yeah, 45 degrees C. Yeah, which is like 105 or something Fahrenheit. I don't know. Something like that. Yeah, that's up there. Yeah. Okay.

**Chris Gammell:** That's like desert temps. Yeah.

**Dave Jones:** And it followed us all the way up the coast as we drove up, you know.

**Chris Gammell:** Oh, so you were going north.

**Dave Jones:** Yeah, we were going north, which is, you know, like hotter. Oh, which is hotter. Yeah, exactly. Okay, yeah. That makes sense. Yep. Anyway.

**Chris Gammell:** Yeah, okay. Well, you know, you can come here anytime you want. It was in the, you know, the minus 40F region. It wouldn't show us. Oh, my God.

**Dave Jones:** Yeah. So what's been happening?

**Chris Gammell:** You know, lots of good guests in the past couple weeks. Cool. So definitely recommend people go and check those out.

**Dave Jones:** I'm sure they've already listened to every episode. Right, right.

**Chris Gammell:** So last week was Laura. Before that was an Aussie Tim from, well, last week was Laura, the protocol and everything with Richard. Yep. And then Tim with the FPGA stuff. Yep. Before that was Clifford with the also FPGA stuff. And, oh, and then Christian Alicia from Embedded FM. We did our joint show.

**Dave Jones:** What is it with FPGAs? Because I did guest videos while I was away, which. Oh, yeah. Yeah, those are great. And, yeah, 12 guest videos. So thanks to all the guests.

**Chris Gammell:** Yeah, those are really. I enjoyed those a lot. So that was great.

**Dave Jones:** But you want to know what the most popular one was?

**Chris Gammell:** Which one?

**Dave Jones:** FPGA.

**Chris Gammell:** Really?

**Dave Jones:** Well, maybe because it was the first one. I think that's, yeah. Maybe. But, you know, yeah.

**Chris Gammell:** Uh-huh.

**Dave Jones:** Hmm.

**Chris Gammell:** Well, yeah, I definitely recommend people go check those out. I mean, it was just really cool to kind of get a look into other videos and stuff like that and other channels. And it seems like it was all the crowd. You know, that was all the, you know, these were all forum members, I'm sure. And, you know, people that were making, like, a lot of test gear stuff. I'm like, oh, okay. Yeah, right. Okay. Yeah. Yeah. Don't worry about that. All right. Right. Right.

**Dave Jones:** You're not really a test gear nerd, which is strange considering you come from a test gear company.

**Chris Gammell:** Yeah. But, yeah, I just never really was into it. You know? All right. We've talked about that here before, right? It's just that I don't, I'm just not as detail driven, I think. I think that's what it really comes down to. So, like, people that want, like, that last bit of precision, I'm like, okay, well.

**Dave Jones:** You're an engineer and you're not detail driven. Something's wrong there. No wonder you moved into science.

**Chris Gammell:** Well, no, yeah. I mean, that's why I'm not a, I mean, I'm not a great engineer. Like, let's be honest here, right? I mean, like, that's something I'm not, but I like breadth more than depth, right? We've talked about that too. Of course. Like, you know, I'm just like shaking things up, learning new stuff. But some people, like, really like keying in, right? On certain things. Of course. Yeah. If the one thing that I have depth on, it's, you know, interviewing nerds.

**Speaker ?:** Right.

**Chris Gammell:** I was thinking about that. It's like the one skill I have these days. Maybe also bringing nerds together. Oh, and by the way, I meant to tell you, you were a ad hoc sponsor of my meetup last night.

**Dave Jones:** Yes. So I heard. Yes. You gave away the meters to a worthy.

**Chris Gammell:** Yes, that's right. Excellent. Door prize. Yep. That's a good one. So if people are on the stateside and need a giveaway for something, they can give me a shout too. I've got some of the Dave's excess meters here. Cool.

**Dave Jones:** Yeah, if people don't know, I'm sure I tweeted this, is that I sell my meter on Amazon, right?

**Chris Gammell:** Yeah.

**Dave Jones:** And of course, Amazon have a great return policy, don't they? Yeah, pretty good.

**Chris Gammell:** I mean, just everywhere in the states, pretty much. Right. There's really no questions asked.

**Dave Jones:** Right. Yeah. So people return it for whatever reason. I don't know what. And then if Amazon deem it to be unresaleable, because I don't know.

**Chris Gammell:** Which is based on their criteria, right?

**Dave Jones:** Their criteria, I have no idea what it is because there's a scratch on the box or something. Then they either, well, they mark it as unresaleable. And then I get an email saying, if you don't remove this within 30 days from our warehouse, we're going to scrap it.

**Chris Gammell:** Yep.

**Dave Jones:** And I can't get them sent back to me. You're only allowed to send it to another person in that country's, in the warehouse, in the country where that warehouse is. So I can only send it to someone in the US.

**Chris Gammell:** Guess who's got a pile of BM235s in his house, yeah. Yep.

**Dave Jones:** And there was a high voltage probe, too, but I don't know what happened with that one. It wouldn't let me get it out.

**Chris Gammell:** Yeah, I don't either. I haven't seen it yet. Get it out.

**Dave Jones:** Yeah, no. No, it wouldn't let me do it. So anyway.

**Chris Gammell:** Well, these are just like retailing things, too. I mean, anyone who's in retail, I'm sure, knows all about the return stuff. Yeah. Well, we've talked as well about this is like the cost that people don't really put in their models when they're doing stuff. The cost of doing business, yeah. Right, right. It totally is. And I mean, I never think about it, right? Like, who would return something? You sold it to them. I don't know. But in retail, it's very common.

**Dave Jones:** And not only just returns, but, you know, if you're a small business and you get the meter back, okay, you can resell it. You can resell your product yourself. You can check it. And, you know, you may not lose a huge amount, but you'll lose out on the postage. But, yeah, you don't realize that a lot of stuff gets lost as well. And you've got to recount the tip of the rule of thumb in the industry is 2% of your sales. Really? You'll decide 2% of your sales as a complete write-off. As in, you will lose the unit. You'll lose every cent, including the cost of the unit and the postage.

**Chris Gammell:** Wow. And if you don't factor that into your business. You just got to send it again, huh? Yeah.

**Dave Jones:** Yeah. If you don't, you know, sometimes I've sent things three times and then given up, you know. So, you lose the item, you know, twice. Like, I've learned now that, no, once it doesn't get there once. I, too, have dealt with the USPS. Yeah. Once it doesn't get there once, that's it. Sorry, dude. I'm not resending you a new one. You just miss out, you know. Right, right. People have a whinge, but what can you do?

**Chris Gammell:** I love the postal service. I won't give them too much crap, but, yeah. If there was an option to pay extra for, like, just skipping that as a delivery mechanism, I'd be like, yeah, just charge me a little extra. That's fine. I just, I love it. I want it to be around. I just don't want to use it.

**Dave Jones:** Right. Anyway, yeah, that's a real hidden cost of doing business. Yeah, definitely. So, it's very, very significant. Yeah. Especially if your items are worth a lot of money.

**Chris Gammell:** Right, right, right.

**Dave Jones:** It's, yeah. And then, if you, you know, people buy things with the courier or whatever, you've got to eat that charge, you know. Like, especially from here in Australia, it can be like 25, 30 bucks each way, right? And it's like. Wow, yeah. Yeah. It's killer. That's crazy. Sometimes it can cost more than the product does in actual manufacturing costs. Yeah. Oh, yeah.

**Chris Gammell:** Yep, yep, yep. Well, speaking of manufacturing, what's going on with your manufacturing? Sounds like you're having a little bit of woes in the manufacturing space.

**Dave Jones:** Well, you know, everything that could go wrong has gone wrong, I think, with my Kickstarter. Oh, not, not really. I'm sure.

**Chris Gammell:** I mean, like, you're going to ship it at some point, right? It's not like you were like, well, I was lying. It doesn't exist.

**Dave Jones:** Right, yeah. Unlike half the Kickstarters out there, yeah. Well, we have shipped. I mean, we have actually shipped. Right, right.

**Chris Gammell:** That first batch is out, right?

**Dave Jones:** Right, yes. The first, yeah.

**Chris Gammell:** I've seen pictures of them on Twitter and stuff like that. People say they've gotten them.

**Dave Jones:** Half of the first batch is out. Okay. Yeah, and, well, what happened is that the problem is, yeah, there's a few issues that have cropped up. Some are just dumb because we missed it. Others are showing totally unexpected issues. Oh, let's hear about those first. Well.

**Chris Gammell:** Let's just assume the dumb ones are, you know, whatever, you know.

**Dave Jones:** Well, first of all, there's a story. There's a few stories in here.

**Chris Gammell:** Okay.

**Dave Jones:** First of all, we were supposed to do, there were 40 units that were supposed to be produced and sold before the Kickstarter just for this very reason so that I can get them out to people and they can use it and tell us if there's any, you know, like stuff. Right.

**Chris Gammell:** Slam it against a rock a couple times, send it over a waterfall, whatever you want to do.

**Dave Jones:** Because we have no clue. Like, we've been involved in this for so long that you can't see the forest for the trees, right? You're way too close to it. Yeah. Way, way too close to it. So, yeah, I was kind of counting on that and that was the first thing that went wrong. The units came here to, they made it all the way to Sydney. They made it to the dock here.

**Chris Gammell:** Yep.

**Dave Jones:** And then the manufacturer realized that something was screwed up. I won't get into details. And it's like, oh no, we have to recalibrate them. Oh no. So, yeah, they realized a mistake, you know. Sure. You know, shit happens, right? And we thought, no worries. You know, look, it was a pain in the ass, but we'll ship them back. And no, I think they're still sitting in the dock somewhere.

**Chris Gammell:** Oh no.

**Dave Jones:** I kid you not, this is like a been a month and a half. And I think they're still sitting in a dock somewhere. Because the expediting companies. Not your dock now. No. They're still like, still trying to be returned back to the manufacturer so they can redo them. And it's just the problems with the expediting companies.

**Chris Gammell:** Yeah. It's amazing. So, I was talking to, at this meetup last night, I was talking to a friend about like just the amount of bouncing around. He was doing some crazy assembly, but there was at least four. Four or five countries involved with like a process and then a new thing being applied and then like each step of the way. So, not only is it, you know, like, so you think about small problems that crop up, you know, some kind of inevitability. But now you have like material. Now your assembly line is, you know, thousands of miles long, right? And it's like, holy shit, you know. That really impacts your delivery time and your cost and all the shipping costs and everything. And you can't do it onesie-twosies. You got to bundle them up like you're doing, right? You got to do 40 at a time to make it worthwhile. So, I think what you should do is just, you know, pack up a backpack, throw David on a plane, man, and send him to South Korea, right? You just got to...

**Dave Jones:** Well... You have a courier.

**Chris Gammell:** He works for you. You just got to, you know, repurpose him. He can write code on the plane.

**Dave Jones:** Probably. We shouldn't. That's actually not a bad idea. I know.

**Chris Gammell:** Sometimes that is like the sneaker net is the best way to do it. I know.

**Dave Jones:** But we physically didn't have meters. Like our whole production run of pre-production run of meters of 40 years, like, you know, because they didn't physically have any more, you know. And so, that was it, you know, and they're stuck in a dock somewhere and they're still stuck there. So, you know, so we're left without, you know, high and dry and the people who pre-ordered those didn't get them. So, you know, sorry about that, but it was kind of beyond everyone's control. Well, you know, shit went wrong, you know.

**Chris Gammell:** Yeah. Shit happens. Well, that's logistic stuff, though. So, like, again, that's like the same theme here, right? It's like shipping stuff, logistic stuff, whatever, you know, selling stuff.

**Dave Jones:** It's a combination of that, but, like, I could have easily got them, but they would have been, they would have required a recalibration and I didn't want to send them out to people who ordered them, you know. And I couldn't calibrate them here. It's not like, you know, like, yeah.

**Chris Gammell:** It's not like the calibration goes bad in shipping. I mean, there might be some temperature swings, but probably not enough for it to really matter. No.

**Dave Jones:** Anyway, it was a software thing. Anyway, so we decided to send them back and that's where the problems started, trying to get them reshipped from the dock. It probably, in the end, would have been easier if I just accepted them into the country, paid all the import duty and the local delivery, got them here, and simply then sent them back via DHL Courier. Right. That would have been, like, that would have, like, solved it. But with hindsight...

**Speaker ?:** I see.

**Chris Gammell:** So you turned it around and sent it back through there.

**Dave Jones:** I turned it around at the dock, yeah, because I thought, why would I import them? It's stupid. We know they have to go back, you know, and that's when it just, like, it was a hot...

**Chris Gammell:** I would say, don't plan on ever saving money, right? Just plan on spending money.

**Dave Jones:** Then it was a hot potato, you know, and nobody wanted it. Nobody wanted to touch it. And anyway, like, as in the dock people and stuff. And it was, ah. Anyway, so they're still sitting there. So, and then the pressure was on from all sides to get the Kickstarter done, right? And we went, well, look, we were hoping to get those 40 units so that we could ship them out so, you know, people could have a play with it and give us feedback. So we decided, oh, no, let's, okay. Like, that wasn't happening, you know. And so we thought, okay, let's just take a chance. We'll run the Kickstarter. Get it done before the end of the year. You know, like... Yeah. And we'll take a chance and then the first 450 will be the test lot, you know. All right. Yeah. So let's up the ante by an order of magnitude, right?

**Chris Gammell:** Really selling some pain for yourself here, buddy.

**Dave Jones:** Yeah, exactly. Oh, yeah. And, you know, but everyone was kind of confident, you know. And, yeah. Yeah. So we go ahead with the Kickstarter. Kickstarter's a success, of course. But then, of course, New Year's, Christmas and New Year's, breaking everything. So I was hoping to deliver in January, in December, but I was a week late or something, you know. Anyway, so we shipped out in early January. We got the 400 and... Well, we got 180 units here and, you know, we shipped them to different warehouses.

**Chris Gammell:** Yeah.

**Dave Jones:** And so I got 100 and... Anyway, we shipped out, no problems. We shipped to Australian customers, got them first. Europe got them. And then, yeah, then the report started coming back that, A, it's got slow auto-ranging and it's... And then people started having... Like, there were a few other little niggly software bugs.

**Chris Gammell:** Oh, but software's better. Oh, software can be fixed. I mean, like, this thing's built to be updated with software, so that's good.

**Dave Jones:** It's built to be updated in software. That's why we're confident that, you know, we could fix any issues. Right.

**Chris Gammell:** As long as it's not a hardware bug, you're in good shape. Exactly.

**Dave Jones:** So we were fairly confident that we wouldn't have any hardware issues.

**Chris Gammell:** Well, also, if you can't brick the software with an update.

**Dave Jones:** You can't. No, I've... Okay. Yeah, I've been made... I've checked that and I've pulled out the SD card during the update and it just happily... Oh, nice. That's good, yeah. ...happily takes care of that.

**Chris Gammell:** Have you tried to, like, program in, like, a GoTo10 or anything like that? Right.

**Dave Jones:** I'm sure you could brick it some way if you really tried.

**Chris Gammell:** Right, right.

**Dave Jones:** Yeah. Anyway, so we were pretty confident of that. Cool. So we thought, yeah, no worries, you know, probably the worst case is we'll have some... Like, I knew we'd have some software bugs, so, you know, that was a given. Anyway, and then the odd person started to report that they had a problem with the range switch. And, you know, it was like...

**Chris Gammell:** Range switch, like the actual clicky...

**Dave Jones:** The clicky range switch, yeah. The clicky rotating range switch. And not only was it a little bit loose, a little bit of wobble in it, but... Which we hadn't seen before to this magnitude. And also intermittent contacts as well, which was the killer. Like, you know, it's one thing to have a bit of play in your range switch. It's another thing to have loose contacts. And people started posting videos, like just a couple of people. It wasn't everyone. It was just a few. But, yeah, even one, one is bad, right? And then two sort of confirms it.

**Chris Gammell:** Well, I was thinking about this too, is that like... So, you unfortunately have like a catalog of like complaining about other people's products. Yeah, yeah, yeah. So, like...

**Dave Jones:** I know.

**Chris Gammell:** You can't just be like, oh, nobody cares about that when there's video evidence of like... Yeah, exactly. You're like, well, the tilting bale.

**Dave Jones:** And they posted those videos of me complaining. Yeah, yeah, yeah.

**Chris Gammell:** Yeah, got it.

**Dave Jones:** And...

**Chris Gammell:** That's funny.

**Dave Jones:** Yep. And by far the biggest... Well, the biggest complaint was about the slow auto ranging. And it used to be faster. And they made it slow in an update. And we just missed it. I mean, we were just so used to it that we didn't notice. You know, like... Got it. I know it sounds stupid, but, you know, it's just like... No, it's like, again, it's being too close to it, right? It's just like daily type stuff. Yeah.

**Chris Gammell:** You're not going to notice it as much.

**Dave Jones:** No. And we, you know, and we... Yeah. We just didn't notice it. Anyway, so that was a bit embarrassing.

**Chris Gammell:** So tell me about that. Do you guys... Do you and David have, like, a standard battery of tests? Like, did you actually standardize that or anything?

**Dave Jones:** No, we should have. That was a mistake. We should have more formally...

**Chris Gammell:** Right. And so you don't have a calibration rig in your place. You don't have a test jig in your place. No, no.

**Dave Jones:** I like... Like, David went through the pre-production meter and went through design issues and stuff like that. Okay. But...

**Chris Gammell:** Are you not doing, like, bug tracking or anything like that either?

**Dave Jones:** We are now.

**Chris Gammell:** Oh, you are. Oh, I see.

**Dave Jones:** Yeah, once you did the fan.

**Chris Gammell:** How are you doing that?

**Dave Jones:** Oh, David's doing it in some document. Just like a spreadsheet or something? Yeah, some document. I'm not sure how he's doing it. No, it's not. Yeah, because we're not in charge of the firmware, right? We don't...

**Chris Gammell:** Right, right, right. Yeah. Yeah, okay. So it's more just like, is this resolved? Yes, it's resolved. Here's a firmware number. Yeah, yeah. Yeah, exactly. So you can... So when someone asks about it four months down the line, you're like, oh, well, you're on rev 4.02. You need to go to 4.07.

**Dave Jones:** David's keeping track of that in a document somewhere. Okay, cool. Which will make public. It'll be a public sort of bug tracking kind of document.

**Chris Gammell:** Yeah, that's great. Yeah.

**Dave Jones:** And yeah, so like, you know, I was mostly concerned about the rain switch because, you know, that's a physical thing. And, you know, like maybe three, maybe four people reported it out of, so maybe one in a hundred, I think, actually reported in, you know, like a real issue. And we hadn't seen this before. You know, we've had countless prototypes over the last two years and we've never had a contact issue. And it turns out that it was just a tolerance thing in the injection molded parts. You know? So when they went to the production, even though the pre-production was supposed to be the same mold and everything, I think they might make them slightly differently.

**Chris Gammell:** I mean, if you start shooting faster, if you shoot plastic faster or hotter or colder or whatever. Yeah, exactly. I mean, there's just a lot of, there are a lot of knobs to turn there. Yeah. Yeah. And not only that, it's like, even if you think about, you make 50 units, but you start to have problems at like the 500 or 1,000 mark, you're going to see that, you know, 5% of units at a certain point. Exactly.

**Dave Jones:** You may not see, if you make a hundred, you may not catch that one in a hundred.

**Chris Gammell:** Right. Right. Or yeah. And you might even just like right off, be like, oh, well, I just, you know, jiggle it and it's fine. Right. But you had a bunch of customers who get that as their first thing. They don't know how to do that. Oh yeah.

**Dave Jones:** No. No. No. If I, if during any of the production or pre-production, I noticed an intermittent contact, wow, that would have been priority number one. Right.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** But we've never had, and I've, like, flogged the range.

**Chris Gammell:** Well, these are just like volume problems though, right? Oh yeah, of course. That's like, who was it, Jeff talking about that? I think. Jeff Kaiser.

**Dave Jones:** Yep.

**Chris Gammell:** Talking about like just the, you know, when you get into the million unit things, you're going to be playing with this stuff.

**Dave Jones:** You'll get the outliers. Yeah.

**Chris Gammell:** Yeah. And that's when you really start to see the full range.

**Dave Jones:** You'll find out where the tolerances, yeah, where the tolerances lie. You know, you, you won't see it in a few dozen or a 50 or even a hundred units, you know? Yeah.

**Chris Gammell:** Well, speaking of my old test equipment days, I remember like, you know, if you, if you have a vendor that says typical, you know, on a data sheet. Right. Yeah. Typical is just typical. They're, they're giving you that full range for a reason, you know? Yeah. Right. Yeah. That's when, uh, statistical process control, like, you know, knowing your SPC concepts and like being able to doing error budgets and all that stuff. It's like, that's really important stuff.

**Dave Jones:** Please explain SPC for those. So like, uh, yeah. So. I'm using the acronyms.

**Chris Gammell:** Right. So a statistical process control is like, if you have, say you have a test stand where it, uh, you know, you're doing a calibration and it calibrates around, you know, you're trying to calibrate a 10 millivolt range and you got a 0.1% accuracy or 0.001% accuracy, whatever. And that test stand does that. That's fine. But then maybe the next test stand down does the same thing, but it's offset by 0.001%, you know, or, you know, it's, it's just slid to the right a little bit. Yep. And you start to see these things relative to one another and relative to all the components and it's just.

**Dave Jones:** And you've always got hard limits. I mean, at some point you've got to manufacture a pass fail limit. Right. And if it's 0.001 over or, or under, you know, you, you, it'll, it'll, it'll pass, but then that may be different to another test rig. And, you know, yeah, there's. Right.

**Chris Gammell:** And then, and then you start having stuff that doesn't pass and that turns into like seeing stock on the manufacturing floor. That's like literally waste. I mean, you might be able to rework it, but then there's time, you know, like then a tech has to look at it. And if they don't deal with it in a certain timeframe, then it gets scrapped out. So.

**Dave Jones:** Yep.

**Chris Gammell:** Test equipment. Gee, Chris, why don't you like test equipment stuff? I don't know, Dave. I don't know why I don't like test equipment stuff. Maybe I've dealt with it too long.

**Dave Jones:** Oh, man.

**Chris Gammell:** Yeah. Yeah. Yep. You guys are just doing all the, oh, I like this finished goods thing. That's it. Although now you're feeling the pain. So, yeah.

**Dave Jones:** I'm, I'm, I'm just going to keep rebadging shit from now on. Right. Exactly. Yeah. It's just things. Anyway. So yeah. Rain switch. That was like, if you would have asked me what would be the last thing that went wrong in this thing, you know, that would be on the list, you know, that'd be high up the list of things that I wouldn't have expected to go wrong. And it did.

**Chris Gammell:** You never see that. The big ones you never see coming.

**Dave Jones:** Right. Yeah. Yeah. And, and of course that is a showstopper. I mean, you know, we, we, we, we can't have like one in, you know, every hundred or a couple in every hundred units having a dodgy rain switch. That's just unacceptable. Right.

**Chris Gammell:** Well, you know, you know, you know, you know, on the, uh, the Toyota production system, the TPS stuff too. Yeah. Uh, you know, that would be right. That's, that's, that's, that's a big red button incident. I don't think that's what they call it. Yes. Right. You know, when they're like, so in the TPS and I'm sure I'm getting all my terms here wrong. Yep. But in Toyota production system, anyone on the lines allowed to pull the stop and basically, Oh, anyone. Right. Okay. Yeah. So any worker, if there's a true problem, they're supposed to pull the stop and the whole line shuts down and then everybody runs towards that one thing and fixes that problem. Yep. And it's like, holy crap. Yep. Yeah.

**Dave Jones:** I used to have that power as well when I was working in, in, you know, production engineering. If I like, you know, it was like a hundred thousand dollar a day business. Right. So if we, we, if we stopped the line for a day, the company loses a hundred thousand dollars. Right. It's a lot of money. And I, uh, quite a few times went stop like, and shut down the entire production line. And I had the authority to do that.

**Chris Gammell:** Right.

**Dave Jones:** And it was like, you know, and sometimes you had to do it.

**Chris Gammell:** Yep.

**Dave Jones:** Yeah.

**Chris Gammell:** Not, not to hawk one of my old pieces, but like, so thinking about that TPS thing and thinking about all this stuff you're talking about, I wrote an article a while back. It was back, oh God, it was back in May already. Yeah. It was, manufacturing isn't glamorous. And this is the stuff where it's like, you're just on the floor fixing stuff at, you know, 1am. Right. Right. Which isn't. Right. People like to talk about making stuff and everything, but it's, yeah, making, making one of things, making 10 of things, making a thousand of things, very different beasts in your thousand plus. So, and you're not even making them. That's a crazy thing, you know? Like, yeah.

**Dave Jones:** Anyway. So I, I did push the big red button here. Like, cause we, we had, cause we'd only shipped half the units, half the early backer units. We had once again, a more, uh, logistical issues. The people in the U S have been, you know, where's my meter? Where's my meter? And we were using a reshipper in the U S and unfortunately. Not me. We, we, we, we asked the manufacturer to, um, ship via, you know, a door to door courier. So these meters would just get there. There'd be no import hassles. Right. And well, they, they didn't, I don't know. Cause they forgot or it's part of their standard process, not, you know, to do it another way. So they use this expediting company to ship into the U S and wah, nope, they got stopped. Um, not because of, um, you know, like a lot of people instantly speculated, oh, fluke. It's fluke. Because you remember that fluke thing where they stopped the trademark. Oh, that's right. When they turned off the spark fund meters. Yeah. Yeah. The spark fund meters.

**Chris Gammell:** But yours aren't even yellow, you know?

**Dave Jones:** I know. But everyone went into conspiratorial mode, you know, and it's fluke of stop Dave's meter from coming into that.

**Chris Gammell:** I don't think they feel too threatened. I wouldn't worry about that. No, no. Yeah.

**Dave Jones:** It's, it's all good. No. So of course it wasn't a fluke. No, it was just, um, because what, what it turned out to be, which was the first time I've heard of this, but apparently it's a thing. Um, if you're getting stuff into the U S, uh, and it's going to the company, it's going to a company who did not order the goods, who does not own the goods. In this case, a reshipper, they don't own the goods. I own the goods. Right.

**Chris Gammell:** So my, my company name is on the, they didn't get money from you. Right. Yeah. They didn't give money to you for your product. They, they were just handling material.

**Dave Jones:** Yeah. So what, what it was, so the import people looked at the paperwork and went, we're shipping to this company whose name does not match the company who owns the product on the invoice. Um, red flag, stop. And, um, yeah, they've been sitting there for quite some time to sort.

**Chris Gammell:** Like the port of Los Angeles or something.

**Dave Jones:** Somewhere like that. Yeah. There's some, some port in the U S they're just sitting there. Right. And I, I, I didn't know about this, you know, and neither did anyone else.

**Chris Gammell:** It's like, you gotta, you gotta, you gotta do it like the, the Chinese shippers from like AliExpress do and just like put something. Yeah, exactly. Uh, yeah. Very large gift.

**Dave Jones:** Anyway. So, yeah, so we, we, we were trying to sort out that and then the range switch issue happened. So it was kind of for, for shortest timing. Otherwise we would have sent out another couple of hundred units. Yeah. Um, so yeah. So I pushed the big red button and said, look, this range switch thing's a problem. They, the manufacturers investigate and they found a solution that they think is going to work just to treat. And, um, and we said, yeah, look, let's just recall those. Not, not recall. Let's screw all of them back and they'll just, um, do a little mod to the range switch and then we can ship them back out. So.

**Chris Gammell:** See, now I thought you were going to get into the whole, so you haven't had any sourcing issues again though.

**Dave Jones:** Oh, sourcing issues. No, I think they're mostly solved. Component sourcing.

**Chris Gammell:** Have you, have you seen this article though about the, uh, the shortages?

**Dave Jones:** Oh, the, uh, the, the capacitor shortages.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. Who, who is it? Who's the company?

**Chris Gammell:** So, uh, Yegio, Yegio. Yep. I'm not sure. Yeah. So. Yegio, I call. Yeah. Yeah. So that was about resistors, but it's apparently passives all across the board. Oh, really? So like, okay. So this all started, not started. This is, was brought to my attention when a friend was asking about, um, you know, have you seen prices going up? You know, he just sent me a digi-key page and he's like, I paid half as much a reel a couple months ago. Interesting. That was for some diode products. So it was, you know, it was active technically. Uh, but you know, low scale, low complexity parts. Uh, and I'm like, I don't know. So I asked on Twitter and people started saying, yeah, apparently because, because of shortages overall, there's just been general capacitor shortages and some resistor shortages and stuff like that. And because of the weakness of the dollar against the, the RMB or the one, uh, it's like, yeah, it's just getting harder and harder. So I was wondering if that maybe hit you as well.

**Dave Jones:** Uh, no, I haven't heard a thing. No. Okay.

**Chris Gammell:** So, and I mean, yeah, you, you would just might have, I'm sure that like a lot of this is usually, uh, muffled by a good purchasing person, right? They either know about it or they have alternate sources or whatever, but, uh.

**Dave Jones:** Usually it's not too bad for passive parts like this cause you can multi-source, you know. Yeah, exactly. That's the best case. It's, it's not a problem. Right. Yeah. It's bad when like. Unless you got some specialized 0.01%. Right. Right. Two PPM resistor or something. Right.

**Chris Gammell:** Or if it's in your micro that's, your micro's like not available for some reason, then you've also got issues, but. Yeah. Yeah. It's just screwed.

**Dave Jones:** You haven't seen that exact part. No.

**Chris Gammell:** Yeah. Okay. Yeah. So this was, uh, uh, actually former guest Joe Bamberg was, uh, was the one who brought this article to my attention. Uh, so yeah. Uh, but yeah. Yeah. So Yagio is only taking orders out from China now. So, and people might know the name because like they're in DigiKey and usually they're the cheapest option. So there's a lot of people that designed them in.

**Dave Jones:** Right.

**Chris Gammell:** And now you can't really get them. So.

**Dave Jones:** And price has been creeping up. That's, that's interesting. Yeah, it is. So how, how do the stockers like, like DigiKey and Mauser get them then if they're only selling to China?

**Chris Gammell:** Uh, well, some of them might be selling old stock. I, I, I'm not speaking from my place of authority. I don't, I don't know, but you know, I'm sure that they have stock and stuff like that. But if you, you could even just go and look on their sites cause a lot of them lists reorder times. Right. So if they, if they run out of a stock, they, they know their lead times.

**Dave Jones:** Oh, what you can do is you can put in like, I want 10 million of these and he'll tell you, I don't have enough stock. Here's the lead time. Exactly. You know. Right. And that's, and that's effectively the same thing you do.

**Chris Gammell:** If you, if you go to like Arrow, Avnet, whoever, you know, and you get a full bomb quota and you can do that at the other distributors too. Yeah. Uh, you know, they'll give you lead times. Right. Especially if you're doing high volume.

**Dave Jones:** And they're usually pretty accurate.

**Chris Gammell:** Yeah. Oh yeah, yeah, yeah. Yeah. But it's just, it's more about like, uh, you don't, yeah. So like people should be doing this anyways. Right. So, so this is our PSA for, I guess, for this week is like, if you're thinking about high volume, get your stuff quoted fast anyways, because you want to make sure that you can actually get the stuff. And if you can't, then you want to go back and you want to re, you know, find other part numbers and, you know, maybe redesign your circuits if you need to test everything, yada, yada, yada. So. Hmm. But that's not you. So that's good. No, no, it's all good. Although you might want to be, you might want to talk to your manufacturer and just ask them and be like, Hey, have you been seeing this? You know? Because it's the thing. They wouldn't, they wouldn't tell you until it's a problem.

**Dave Jones:** No, no, of course they won't. They won't tell you until it's an issue.

**Chris Gammell:** Yeah.

**Dave Jones:** And even then they, they wouldn't tell me, Oh, we've got to, you know, it'd be, we're going to, it'd simply, sorry, where there's a, a delay. In the, you know, actually delivering. And that's all they tell you. Yeah. They never tell, which has happened a couple of times with my Bryman meter. Bryman, like, you know, for the last couple of years have been Johnny on the spot with their delivery. Right. Like it's, it's always two month lead time, which is ridiculous. Right. No, that's standard. They've got some just in time thing. Yeah. It's standard.

**Chris Gammell:** I mean, like you can't get parts. Like that's, that's, again, that's, if you don't know, that's doing wafer starts, right? You're, you're starting from sand and you're basically getting all the chips you need. So.

**Dave Jones:** Well, I know. Yeah. But I order a meter and they'll say, it'll be two months lead time. They don't keep any stock at all of this meter. You know. I would. I wouldn't. I know. Yeah. No. Okay. Fine. It's just kind of annoying. You know, so I've got to plan two months ahead for when my stock's going to run out and that kind of stuff. Anyway. Anyway. So it's two months. And then for the last couple of times in a row, they've come back sometimes multiple times and said, sorry, there's a delay in shipping these things. So maybe that is related. Oh, totally.

**Chris Gammell:** I guarantee that's like they're getting their lead times pushed out. And so. Yeah. Right.

**Dave Jones:** And so it impacts me. Yeah. That's probably, yeah. That's more than likely the case. Right.

**Chris Gammell:** And they're building in also their assembly times and their calibrating times. And, you know.

**Dave Jones:** And I'm sure they do just in time production, you know. Right. Like. Yeah.

**Chris Gammell:** Cash flow, man. Cash flow is important. Yeah. Exactly. Yeah. Yeah. You know that. You've put in POs for big orders. I've put in big POs for the year. You've seen the zeros at the end of the order, right? Yep. It's crazy. Yeah. I had another friend who was doing that. They were doing some macro fab stuff and they just. Yeah. Big ass order, you know. They were just. Yeah. Sticker shock, you know.

**Dave Jones:** I'm a pissant little, you know, almost one man band. Right. Almost. Almost. You know. And I'm putting in, you know, six digit purchase orders.

**Chris Gammell:** Yeah. Exactly. You know.

**Dave Jones:** I mean, holy shit.

**Chris Gammell:** Right. You'll get six digits back. Right. Yeah. Hopefully. Hopefully. That's the plan. You better. Yeah. If not, you know, Dave might be looking for a job, but yeah. Right. But yeah. Yeah. I think that that stuff is. Yeah. It filters down to you at the. You know, you're like a reseller at this point for a lot of this stuff. Yeah. But, you know, you're still getting hit by it.

**Dave Jones:** Hmm. Yeah. Which is interesting. So there you go. Anyway. So yeah. The, yeah. The problems with the, with the meter. That was. Yep. Oops. Yeah.

**Chris Gammell:** That's stressful, man. Yeah. I know.

**Dave Jones:** And it's, you know. People might think.

**Chris Gammell:** On the whole, you're doing well for a Kickstarter. Right. Yeah.

**Dave Jones:** Yeah. For a Kickstarter. Yeah. And people, you know, people complain. Oh, you know. How can there be so many problems? Oh, you've been working on this for two years. It's like, well, even the Bryman meter, they worked on that for two and a half years. And that's much simpler. Right. That's like a really simple meter. And it still had problems when it came out. Yeah. People started finding, you know, all sorts of issues when it came out. Yeah. Yeah. So, and yeah, we've, we've had to upgrade the mask ROM micro in there. This is none of this flash rubbish. Yeah. It's a mask micro ROM.

**Chris Gammell:** Low cost, man. You got to do it. Yeah. Yeah.

**Dave Jones:** Yeah. They, they actually make their own chips.

**Chris Gammell:** Oh, I believe it.

**Dave Jones:** Yeah. Yeah. Yeah. Bryman actually make their own multimeter.

**Chris Gammell:** And so when you say mask ROM, that's like the, so what they're doing is like the, the metallization layer, right? Yes. That's what they're changing. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. So that's like the stuff that Jerry Ellsworth used to do for like C64. Or, and like just lower costs.

**Dave Jones:** No, no, no. They're, they're, they're, sorry. They are one time programmable. So. They're one time. So you can burn them once. Oh, so it's not metallization layer. No, no, no, no. So you make the chip and you can burn them once, but you can't reprogram them. Okay.

**Chris Gammell:** So you're not changing the mask there. It's, it's a mask ROM. Okay. Yes.

**Dave Jones:** So they can't just keep stock, you know, it's a big risk for them to keep stock, stock of mask ROM programmed parts. Because if you have to change the firmware, well, you have to scrap all your old stock.

**Chris Gammell:** Right.

**Dave Jones:** And there's just no other way to do it. And, and yeah, and we, we've had to revise that firmware probably four times now.

**Chris Gammell:** Wow.

**Dave Jones:** You know, and, and this was after two and a half years of development, you know? So yeah, people just kept finding issues. So yeah, it happens.

**Chris Gammell:** Hmm. Well, better to find them than to be like over your bench and, you know, I'd rather have other people find them personally. So yeah. Yeah. True.

**Dave Jones:** I would hate to produce a product that's, you know, a mask ROM like that.

**Chris Gammell:** Yeah.

**Dave Jones:** But that's what you had to do back in the days. There was none of this flash rubbish. Right. Exactly. There was none of this E-squared problem rubbish.

**Chris Gammell:** How about the OTA stuff? That's what we're moving towards, right? Everything being OTA. So over the air. OTA. Oh, over the air. Over the air updatable, right? Right. I mean, like that's just the future of stuff, right? I'd already have, I was, I think about that when I look at my phone in the morning, it's like, you know, 18 apps have updated. Yeah.

**Dave Jones:** 18 apps have updated. Yeah. And it's like every night.

**Chris Gammell:** It's crazy. Right. Yeah. I know.

**Dave Jones:** It's nuts.

**Chris Gammell:** They're just moving pixels around, but yeah, it's got to update that stuff. Got to make sure the new features are there and bug fixes. Bug fixes are there.

**Dave Jones:** It's just, ah, it's nuts. Anyway, but that's, you know, before it was the pick 16C84 that started the revolution. Oh, yeah. You know, the microcontroller revolution. We've probably discussed that before, but that was the first, you know, that was the industry's first pretty much, you know, popular reprogramable chip. It's like, you can reprogram this, you know? Holy crap. I can reprogram it. I can make mistakes and then not have to throw my chip in the bin. Right. Wow.

**Chris Gammell:** How novel, you know? Right. I'm going to get sloppier.

**Dave Jones:** And that was a big deal. Back then, flash wasn't invented, so they used eSquared Prom.

**Chris Gammell:** Yep. Yep. Then that's the UV erasable or electronically. No, no, no, no. Electronically.

**Dave Jones:** No, this was the electronically erasable.

**Chris Gammell:** Yes. Oh, so EEPROM and EEPROM. Okay. Yes. Okay. Yes. Cool.

**Dave Jones:** So, yeah. And that was a, you know, you could do it 50 times. It had like 50 cycle right limit or something, but hey, that was a revolution. You know?

**Chris Gammell:** Whatever. I mean, yeah, you get more than one, you're in good shape, right?

**Dave Jones:** Yeah. It's fantastic.

**Chris Gammell:** Yeah.

**Dave Jones:** So that changed everything. Yeah. So there you go. I was like, I did a teardown. It's currently up, it's just uploaded. It's not live yet, but I did a teardown of the IBM PC Junior.

**Chris Gammell:** PC Junior. Okay. Well, that'll probably be up by the time this show comes out.

**Dave Jones:** It should be. Yeah. Yeah. No. Anything fun in there? Anyway. Yeah. Well, the interesting, like I did like a walkthrough of the motherboard. So I did, I took like a photo and then just panned around and zoomed in and did voiceover of the motherboard. It's a bit different to my usual style. So watch it and let me know what you think. And it, the, the, the ROMs, I kid you not, the ROMs, the bias ROMs are soldered into the board. They are mask ROM chips soldered into the board, into the full layer board.

**Chris Gammell:** Oh yeah. Wow. So if you want to upgrade your bias. No updating, yeah.

**Dave Jones:** No, no, no, no updating your bias. It was like, and, and it was date coded before the release of the product. So they were, they must've been so supremely confident in that code that, you know.

**Chris Gammell:** They just didn't have a choice. I mean, I don't know.

**Speaker ?:** Like.

**Dave Jones:** Well, they could have put it in a socket for goodness sake.

**Chris Gammell:** Yeah. That's true. You know, like that's what everyone else does. This is like a low cost thing.

**Dave Jones:** Yeah. Maybe. But geez. Oh, you know, maybe IBM, IBM don't use sockets. We're IBM. You know, like, you know, that's, that's adding unreliability into the engineering chain, you know. Right. Screw that. Yep. So, yeah. And it's so bloody soldered in mask ROM chips. Holy crap.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Into a full layer board. So you've got to, you know, you've got to desolder. It's not easy to desolder those puppies, you know, the big ground plane and everything.

**Chris Gammell:** Yep.

**Dave Jones:** Yeah. So, but, but this was back in the days when they actually published the bias, bias assembly code in the manual. Yeah. You know, it's got the full bias listing in there. Yeah. Anyway, they were supremely confident. So that's the old days. Yeah, man. Sometimes I love it. Like, I like, you know, products like that, that are so well engineered that you're so confident in the code that, you know.

**Chris Gammell:** I'm sure there was a lot of stress in there though. You know what I mean? Like, yeah, it looks like, like with the, you know, the sheen of time, right? The patina of time. You know, like it's.

**Dave Jones:** What was, yeah. What was the, there was for, you remember the, who did the original zip program? The, you know, the, the zip compression thing.

**Chris Gammell:** Oh.

**Dave Jones:** Anyway, it, it was PK where, I think it was PK where did PK zip was the first, you know, everyone's familiar with zip these days, right? Sure, of course. Yeah. Back in the DOS days when, you know, zip was, came out, it was like, it, they didn't change that program. They didn't update that program for like a decade and everyone went, well, is there like a new version? Why isn't there a new version? It's because it's perfect, dude. It's because it, there are no bugs in this thing and it's, we're not going to, why? Why, why touch it? It's perfect. It's right. And for like more than a decade or something, they never released it.

**Chris Gammell:** I can't tell if that's like sarcasm or, or what it was. Is that hubris? Is that what that is?

**Dave Jones:** No, it's just that the, the program, it was one guy, right? Oh, got it. Okay. Right. It's one guy. It was developed by one guy. And, and he went, no, I am not touching it. It is, it is perfect. There's too many issues if I, you know, I, there's, there's no way I could break so many, I could break a million zips out there, you know? So no, I'm just, no, it's perfect. There are no bugs. I've ironed out all the bugs and that's it. So it's version 2.04 forever. Take it or leave it. Yeah. And yeah, that was fantastic. Well. I kind of miss those days.

**Chris Gammell:** I don't.

**Dave Jones:** So you'd rather come in, you'd rather wake up in the morning and have your, 18 apps have been updated.

**Chris Gammell:** Ah, yeah, well, I don't know. I wish there was a little bit more rigor, but you know, we really do benefit from that too, right? Right. Yeah. Getting, getting updated stuff, updated security, stuff like that. Like, so how about this? So we can talk, I mean, I can't really talk about the, the depths of it, but like, you know, there's the whole Intel bug, right? So.

**Dave Jones:** Oh yes. The Spectre and whatnot. What is it? Spectre and what's the other one called? The other exploit. They're two different mechanisms of the same. Two different. Right. Right.

**Chris Gammell:** Spectre and finding it, finding it, finding it.

**Dave Jones:** If people don't know what we're talking about while you find it. That's it. Meltdown. Spectre and Meltdown. Right. Is somebody found, apparently it's been out for quite some time. It's been known in the security world for quite some time. Somebody did a paper on it like nine months ago or something. Right. And it's an exploit in the prefection, not the pre, the speculative execution in the Intel processes where you can actually read data out of protected sectors of memory. Yeah. Wow. Wow. Wow. Wow. It's like, it's a surprise to take it so long to find this. It's a big one. It's a big one. And it applies to ARM processors, all of these super scalar processors, you know, a whole bunch of them. Right. And, but anyway, Intel.

**Chris Gammell:** I think the reason that it probably takes a long to two, it's not like easy. It's not like this is like some. No, no, no.

**Dave Jones:** It's not true.

**Chris Gammell:** Script Kitty is going to hop in and be like, all right, I got your passwords. You know, it's nothing like that. Yeah. Yeah. But it is still like from a true security standpoint. Yeah. It's bad. Yep. So, and it was something like young kid that.

**Dave Jones:** Was it? Published about it.

**Chris Gammell:** Yeah. 22 year old, something or other. Hmm. I'll post a link to that. But anyways. Yeah.

**Dave Jones:** So that, that's, and apparently, well, there's some, there's some, you know, drama about that.

**Chris Gammell:** Wailing and gnashing of teeth. Yeah.

**Dave Jones:** Well, apparently like the Intel CEO knew, knew about this, of course. Yeah. And has like sold stock and stuff. Right. And like, you know, there's some nasty insider trading stuff happening. Right. And, and yeah, Intel are in serious trouble because like this is, it won't sink Intel, but it's, it's going to. No, exactly.

**Chris Gammell:** I mean, like what are people's options here, right? I mean, like, yes, you need patches.

**Dave Jones:** Well, for people's, people's desktops, it's not really a huge deal, but I've heard for servers, it could be, you know, and there's a lot of servers out there. There are a lot of servers out there. Yeah. Yeah. So, and, and, and those companies take their security seriously, you know?

**Chris Gammell:** Yes, of course.

**Dave Jones:** So, you know, whereas Joe blog with their home, with their Intel home PC, you know, like it, it doesn't really matter. Right.

**Chris Gammell:** Yep.

**Dave Jones:** Probably. So anyway, well.

**Chris Gammell:** You and I are not security people, but I don't remember why I brought that up, but.

**Dave Jones:** But, but like everyone came out, you know, Raspberry Pi came out and said, our one's not, our arm's not vulnerable. And every man and his dog's coming out saying, oh yeah, no, we've, we've, we're certified, you know, it's okay.

**Chris Gammell:** Right. Yep.

**Dave Jones:** So yeah. Because not, not all arms are susceptible, only some, um, the Cortex R8, A8, A9, A17, blah, blah, blah. Yeah. It's only a certain sector of them. So, hmm. But that's huge, you know? Yeah. Because they're, they're all in these internet of things, things, right?

**Chris Gammell:** I mean, not that many, not the low power stuff. Right. I mean, I guess arm stuff, but like even still, yeah. Cortex M0s are okay. You know, like.

**Dave Jones:** Yeah, right. Yeah, yeah, exactly. So.

**Chris Gammell:** Yeah.

**Dave Jones:** Is Cortex M0 the smaller, what's the smallest arm, you know, what's the cheapest, most jelly beanie?

**Chris Gammell:** Yeah, I'd say M0, M0 Plus. Those are. Right. Those are usually like the, the sub dollar ones. Right. Yep. Yeah. I was talking, uh, when Alicia and Chris were on here, we were talking, they had, um, that amazing $1 microcontroller guy on their show. You saw that, that like comparison?

**Dave Jones:** No, the, oh yes, that, oh, that awesome comparison. Yeah. Yeah. That was great.

**Chris Gammell:** Yeah. So Jay was on their show and that was a great show with him too. But a lot of those chips, a lot of the sub $1 chips were all M0s and stuff like that. Right. Yeah. So, yeah.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah. I've been, I've actually been using a M0 lately. I've been, uh, I've been, I've been crushing on a new, on a new microcontroller. Oh, there you go. Specifically with a, uh, with a new software on there. So I've been using, uh, I've been using CircuitPython, which we've had Tony on the show in the past. And, uh, Tim, uh, two weeks ago asked me about if I met Dominic, the guy that started, uh, CircuitPython, but, or my, MicroPython, which became CircuitPython. But I really like it for, uh, the thing I like about it. And I think, I think the thing that you would like about it too is you, it's so you plug this thing in, you know, it's a little USB connected eight, nine pen, 10 pen thing. Right. Plugs into Redboard if you wanted to, whatever. So not a lot of pins, but it plugs in. It shows up as a drive on your computer. Windows, Mac, Linux, whatever. Yeah. You open, you can open up the file directly on your computer. Right. So I open up the main.py. I, I edit it. I hit save. It's soft reboots. And I can see that all happening in the terminal. And then it just runs again. And so like, in terms of, yeah. So like you and I were just complaining about that, like, oh, 18 apps updated because people are, you know, making bad code changes. But that's effectively what I'm doing on like a three minute interval. You know? Yeah. Yeah. Of course. Does this work? No. Does this work? No. Yep. Yep. Yep. But it's great for me. And it's been, it's been really useful. So I do recommend trying it out at least. All right. The Trinket M0, I'll link it. The Trinket M0 from Adafruit ships with CircuitPyGelan. So.

**Dave Jones:** Are you a debug person?

**Chris Gammell:** What does that mean?

**Dave Jones:** As in using debuggers?

**Chris Gammell:** Like, I still don't know what you mean actually.

**Dave Jones:** When you're developing micros and stuff. Like, you know, will you use like an insert debugger? Oh, oh, oh, oh.

**Chris Gammell:** So like the, like the one bits you with the J, the black magic. Like, you're talking about like doing like a halt, halt command type of thing. Yeah, yeah, yeah. Yeah. No, I'm not. Mostly because all the stuff that I've been using lately has just been too small or, you know, doesn't have breakout stuff like that. Are you a debugger?

**Dave Jones:** No, I am not a debugger person.

**Chris Gammell:** You're a print effer?

**Dave Jones:** I'm a print effer. I'm a print effer. Yes. Yeah. That's closer to me. I'm a lead flasher. Yeah. Yeah. Yeah. Yeah. Yeah. Exactly. I'll just flash an eye open. You know? I just compile my code, download it because, hey, you know, we're in a world of reprogrammable flash micros. Right. Right. It's not like you're going to wipe off the stuff. Because it only takes a second. It only takes a couple of seconds. Download it and just run the real code on the real hardware. And then if I need to-

**Chris Gammell:** What we should also mention, though, is we are not good programmers. No, no, no. We're not. No, no, no. Writing complicated things, right?

**Dave Jones:** David takes me to task all the time because he's one of those, you know, by the book. Like, I can mathematically prove that my code's correct. You know? Like, kind of. Which is great.

**Chris Gammell:** You're like, pipe down, junior.

**Dave Jones:** Yeah, yeah. Which is great if you're doing a Mars rover or something. Yeah. You know, a space probe that, you know. Right. But, yeah.

**Chris Gammell:** And that's the thing. Like, the professionals, yeah, that's fine. But, like, you and me.

**Dave Jones:** Yeah. No, we're just hacks, yeah.

**Chris Gammell:** We are not smart.

**Speaker ?:** No, no, no.

**Chris Gammell:** Well, that's the thing. We want to get stuff done. I mean, like, I don't know. Yeah. I think you're totally right. It's like, if you're getting into it more, it's, yes, you should be doing that stuff. You're right. And, you know, Blackmagic Probe's great. There's a lot of the, you know, like, the code analysis tools that are out there. If you like that stuff, go listen to Embedded FM. They talk about that stuff all the time. So, yeah. It's, that's not me. I like that, though. A print-effer, you know.

**Dave Jones:** Yeah, print-effer. Yeah. I'm a print-effer. There's a t-shirt in that, isn't there?

**Chris Gammell:** Yeah, exactly. Right. Love it. Yep. Are you programming new things?

**Dave Jones:** Am I programming new things? What do you mean?

**Chris Gammell:** I mean, like, are you just on, are you just in Multimeter World for the next couple months?

**Dave Jones:** I'm probably. Well, no, no. Just straight after this. It is micro-supply. We're back on micro-supply. Oh, right. Because I've been too busy lately, and we've built up the prototype of the controller part, you know, the main controller part. And, yeah, I just haven't had time to sit down for, like, half a day and, you know, actually play around with it and go, okay, yeah. And, you know, play it, test it, analyze it, and go, okay, well, let's move on to the next stage of the development. You know, because we're happy. Because, you know, in a power supply, the main problem is the control loop, right? Yes. Right. Exactly. You know, we've rolled our own control loop.

**Chris Gammell:** Right. So, yeah. Get ready for some ringing. Feedback. Yes.

**Dave Jones:** Oh, just get ready with those little dodgy caps that you just put around your circuit until it works. Hold your tongue at the right angle until it works, you know. Pass it over loads, huh? Yeah.

**Chris Gammell:** Well, you know, there's... Slow it down here a little bit. Slow it down there a little bit. Yeah, we're probably cool.

**Dave Jones:** Well, we've talked about that, haven't we? There's two ways to do control loops. There's the mathematical rigorous way, just like coding. There's the rigorous way, right? And which, if people don't know, involves sweeping your control loop, right? Of course. So, how it works in a DC-DC converter. Yeah, like a network analyzer, right? Yeah, using a network analyzer. So, what you do is you get a big, expensive network analyzer, and you put a little transformer into the feedback resistor network. You know how every DC-DC converter has a... You got your alpha, you got your beta, you got your... I've forgotten everything else. So, you put a little transformer in there, and that allows you to couple a signal into your feedback loop, and then you can sweep it over the whole range via that transformer.

**Chris Gammell:** 0.1 hertz up to, what, megahertz? 10 megahertz? I don't know.

**Dave Jones:** And then you can get the magnitude and phase of the output, and from that you can calculate all your goodness to do with your control loop stability. You know, you've got to have phase margin, you know, with X, and, you know, the data sheets for the op amps will tell you, you know, it's got a phase margin of X and stuff like that, and you've got to be within that, otherwise it oscillates and, you know, all that sort of jazz. Anyway, it's like, you can do that.

**Chris Gammell:** Or... Or you can simply feed... Or you can be a print teffer.

**Dave Jones:** Or you can be a print teffer, and simply feed a square wave into your input, not the feedback, feed a square wave into your input, and look at the output on your scope, and tweak things until it's just...

**Dave Jones:** The waveform, and then there's not any overshoot, really, it's just rounded, just right, you know? Right, exactly. And both methods are entirely valid. You know? I... Well...

**Chris Gammell:** From a support perspective, I'd say the first one is probably a little bit more rigorous. It's more rigorous. But much, much harder to get through, and then even, you know, supporting that then... So, like, now, if you go and change something for a legitimate reason, you know, you add something new, you change your resistor value, whatever, you've got to go retest everything. You've got to read it, yeah, yeah. Yeah.

**Dave Jones:** No, it's much easier to just feed it a square wave and see that it doesn't ring, you know?

**Chris Gammell:** Yeah. And that's... And that is the, you know, the old engineer, and he was allowed to do that, right? You've seen enough of it, you know?

**Dave Jones:** Because if people don't understand how that works, it's because a square wave contains all frequencies, right? Like, a fast rising edge, in theory, contains, you know, all frequencies. Well, not all frequencies, but a lot of frequencies, right? A lot of frequency components, right?

**Chris Gammell:** If you did a FFT of a square wave, you start to see peaks in decreasing amplitude over time, and it goes on for a long time.

**Dave Jones:** So you can simply feed in a fast edge and see if the... And if the output rings, if it, like, overshoots or undershoots, then that's an indication of the stability of the loop, you know, at those frequencies. Right.

**Chris Gammell:** And the sweep is better because you don't just get the harmonics of the base frequency. Yeah, yeah, right. There was actually a really... What did I see it again? So I think...

**Dave Jones:** Oh, yeah, you can feed in multiple frequencies. Like, you don't have to feed in one frequency square wave. You can feed in, you know, multiple. Oh, sure, sure, sure.

**Chris Gammell:** Yeah, that's a good idea, too. Right. But the sweeping gets almost all of them, right? If you get sweeping, you get all of them, and you start to see little peaks and spikes and whatever.

**Dave Jones:** Yeah, but generally, if you look at the phase response of any control loop, it's not random hickledy-pickledy. Right, exactly. It's like nice and smooth, so you can predict that, you know, where it's going.

**Chris Gammell:** Exactly, right. Yeah, you see it on the fifth harmonic. There's probably a couple other frequencies if you change your base frequency a little bit, but that fifth harmonic on all those is going to have a bad time.

**Dave Jones:** Right. So, yeah. Anyway, so that's what we're doing after this. Oh, okay. Yeah, yeah, yeah. We're going to do that. Yeah, it's actually in my calendar because we put it off so many times that earlier in the week we went, let's just stick it in the calendar. Yeah. So, yeah.

**Chris Gammell:** Cool.

**Dave Jones:** So, on that note, we've got five minutes left.

**Chris Gammell:** Uh-oh. Oh, here, I am going to link in a tweet from Seed Studio from a while back, too, that if you don't understand we were talking about the frequency stuff, there's a really good explanation of, like, Fourier transforms and stuff like that. You know, it's been around for a long time, but, yeah, so it's just to see how all the different frequencies are included there.

**Dave Jones:** Cool. Oh, the Goodwatch.

**Chris Gammell:** Oh, yeah. So, Travis Goodspeed. Yeah.

**Dave Jones:** Which, um, this is, um, I was, like, I literally...

**Chris Gammell:** I think I saw that on your Twitter, yeah.

**Dave Jones:** Yeah, I literally have this same watch sitting in a thing with some other Casio calculator watches. I was going to do this exact same thing years ago. Cool. Actually, actually replace the PCB. Well, do you explain what it is first?

**Dave Jones:** It's basically an existing Casio calculator, one of these four bangers, right?

**Chris Gammell:** I mean, everybody knows the Casio watch, the calculator watch. Come on, yeah. Yeah, yeah.

**Dave Jones:** The Casio calculator. Classic. They still sell them, right? Absolute classic. Sadly, they don't sell the scientific calculator version anymore, but hey, you know, which, you know, I don't want a four-banger calculator on my wrist. That's for pussies, you know?

**Chris Gammell:** Right, right. Of course. Yeah. Right. You've got to be hardcore, yeah?

**Dave Jones:** A scientific or bust, you know? Right, right. And, yeah, so anyway, so I wanted to do that so that I could add scientific functionality to a, you know, a...

**Chris Gammell:** Right, obviously, we know you already have a watch fetish, so yeah.

**Dave Jones:** I already have the micro... Well, I already... Yeah, I used to sell the micro watch, you know? Right, exactly. And anyway, so yeah, oh, yeah, you know, I've got examples and I took them apart and I don't know, I got distracted and, you know, it was one of those projects that never got... Well, let's talk about Travis who actually did it, so... Yeah, he actually did it. So he just manufactured a replacement board for inside. Yep. Seemed really easy. He's just put a micro in there. It's one of those TI jobs or something. MS-P430.

**Chris Gammell:** Well, it's not just a new micro, though.

**Dave Jones:** Sorry?

**Chris Gammell:** This is an RF watch. You knew that, right?

**Dave Jones:** Oh, I didn't know. I didn't know that. Oh, yeah. Sorry. No, no, no, no. I didn't look into the details. Yeah, yeah, yeah.

**Chris Gammell:** So this thing is basically transmits and...

**Dave Jones:** No, I hate that. No, no. Okay, no. Okay. No.

**Chris Gammell:** Well, sorry, man. He did it, so... No. Yep. Not wrong. Travis has been mentioned many times here before for doing the IME and stuff like that. I think Austin's probably mentioned him a couple times.

**Dave Jones:** But wrong. No. Oh, has he got a little antenna sticking out? Yeah. A little white. No. Just do a watch. That's so cool. That's just a watch. I'm sick of this smart, bloody wireless watch bullshit. This isn't... No, no, no.

**Chris Gammell:** This isn't... It's not... Dave, Dave, I think you're getting it wrong here. It's not a smart watch.

**Dave Jones:** I don't care.

**Chris Gammell:** It's wireless. This is an SDR in there. It's an SDR. Yeah.

**Dave Jones:** Yeah, but to do... Why? I just want a watch. Because it's awesome.

**Chris Gammell:** No. No. That's amazing. No. I just want a watch. Okay. Well, then you finally go and do it, and you'll do that eventually. But I think this is awesome because, yes, it is a watch for radio engineers.

**Dave Jones:** Hey, what's this thing on the back? That's a Yago S432. What's that?

**Chris Gammell:** I think that's probably the antenna.

**Dave Jones:** That looks like the antenna.

**Chris Gammell:** Yeah.

**Dave Jones:** Huh. Okay. Yeah. Uh-huh. Must be. Yep.

**Chris Gammell:** The radio is based on the CC11001 core.

**Dave Jones:** I just didn't know Yago did antennas.

**Chris Gammell:** Oh.

**Dave Jones:** Yeah. Okay. And it looks bigger than your average bear.

**Chris Gammell:** Hmm. Well, anyways.

**Dave Jones:** Right. No, I didn't know that. I hadn't seen this page. I'd just seen another page that didn't, I don't even think, mention...

**Chris Gammell:** So you weren't even interested in the cool part of it. You just wanted the watch.

**Dave Jones:** No. I just went, oh, he's done exactly what I was going to do, which is modify a Casio. Cool.

**Chris Gammell:** Got it. Yeah.

**Dave Jones:** No. Yeah. Yeah. No, that's the level of detail I went into. And yeah, no, it's an MSP430. It's, you know...

**Chris Gammell:** Uh-huh.

**Dave Jones:** No, hang on. No, that was his dream. His dream was to have an MSP430 in there, but he upgraded it to a...

**Chris Gammell:** Yeah.

**Dave Jones:** CC430. Right. It's got one... It's the... It's still a MSP430, but it's the wireless version of it. Yeah. Okay. No, I didn't see that detail. Sorry. The article I looked at before didn't have that detail. So it was just, look, hey, cool. He's made a... He's modified a Casio watch, you know. Sorry. And that wasn't my fault. That was like the article I read somewhere.

**Chris Gammell:** Cool.

**Dave Jones:** Yeah. All right.

**Chris Gammell:** Yeah. Awesome.

**Dave Jones:** Cool bananas. That makes me want to go back and do it now, damn it.

**Chris Gammell:** Yeah, man. Yeah. There's still time. There's still time.

**Dave Jones:** Yeah. Because I'm a glutton for punishment. I want to do another Kickstarter. You do realize that?

**Chris Gammell:** Oh, no. I didn't realize that.

**Dave Jones:** Yeah. Just a scientific calculator watch. No smartwatch bullshit. Cool. You know, just like, yep. Buck of the trend.

**Dave Jones:** Do it. I think... Was it Mike? Mike from Mike's Electric Stuff? Or somebody on Twitter. Like, I mentioned this, and somebody on Twitter mentioned that we should do a Kickstarter campaign that's called It's Just a Bloody Watch. That would be the name of the campaign. You know? Okay. Yeah. Rather than all the smartwatch crap.

**Chris Gammell:** Gotcha, gotcha.

**Dave Jones:** Anyway. Yep. Hmm.

**Chris Gammell:** All right.

**Dave Jones:** Yeah. Are we done?

**Chris Gammell:** Well, I mean, unless there's other stuff on this list. Ah, there's probably a ton of stuff. There's a bunch of stuff on here. After the recording last week, someone posted the... There was a good... So there's a bunch of CCC talks, which is Chaos Computer Congress.

**Dave Jones:** Yes, because that happens in December, right? That happens in late December.

**Dave Jones:** Yeah. So that happened at the end of December.

**Chris Gammell:** So there was a good talk about Laura, and actually the person who was doing GR Laura, which is GNU Radio Laura. And so there was a talk there. There was another talk... Who else is on here? Well, there's a whole list of... I'm sure there's a YouTube channel, right? There is. And so, yeah, just search for 33C3 is kind of the tag for all that stuff. And so that's all...

**Dave Jones:** How do they give presentations? Isn't it like out in the bush?

**Chris Gammell:** No, no, no. So there's... So every four years is Chaos Communications Camp. Oh, right. And then every year is the Congress. So that's... Oh, that's a different thing. Okay. Right, right. So Congress is an actual conference. Right. It's like a couple days after Christmas and... Got it. Yeah, so...

**Dave Jones:** Well, isn't the camp a couple of days after Christmas? Because I was invited to the camp once, but it was like December 27th or something.

**Chris Gammell:** It was crazy. Oh, I thought the camp happened other times, but I'm not sure actually. Yeah. Yeah. Anyway. I'm not sure if I announced, but I'm actually going to a hacker camp this year. Cool. Which one? I'm going to Tor Camp, which is up in Seattle. Oh, yeah.

**Dave Jones:** No, you've mentioned that before.

**Chris Gammell:** I did mention it. Okay, cool. Yeah. So that's like... Apparently that's like the American version of the Chaos Camp. So, cool.

**Dave Jones:** Oh, the Fate of Atari documentary is now on Amazon Prime. Yeah. Producer, Jerry Allsworth. Narrator, Bill Hurd. What?

**Chris Gammell:** Both former guests. Yeah.

**Dave Jones:** What?

**Chris Gammell:** I haven't watched it yet, so...

**Dave Jones:** Easy to Learn, Hard to Master, The Fate of Atari. What? Since when have they been working on a documentary together?

**Chris Gammell:** I don't know. Holy crap. Yeah.

**Dave Jones:** I don't have this Amazon Prime bullshit, so how do I... How do I... I can rent the movie for five bucks.

**Chris Gammell:** So, like, renting, that's what I usually do, so...

**Dave Jones:** Right. Okay. Do you have to have a Prime account, or do you...

**Chris Gammell:** No, I think you can just... Oh, no.

**Dave Jones:** If you have a Prime account, it's free, right? Or some bullshit. Yeah, exactly. Yeah.

**Chris Gammell:** It's like an all-you-can-eat kind of thing, so...

**Dave Jones:** Oh. Yeah. Wow. Cool. Bananas.

**Chris Gammell:** Yeah, that's a good one.

**Dave Jones:** And since when, like, how long have they been working on that?

**Chris Gammell:** You got the wrong... You're asking the wrong nerd, man.

**Dave Jones:** I know, but I'm just...

**Chris Gammell:** They didn't come here on their press tour, right?

**Dave Jones:** No, no, exactly. I haven't heard a peep out of anyone about this.

**Chris Gammell:** Yeah. Wow. Also, in the video space, they're not new at all. There was a cool video from an old... It was an old VHS video of the history of Japan's electronic industry, so that's fun, too.

**Dave Jones:** Right, I saw the link to that.

**Chris Gammell:** Yeah, that's a fun one.

**Dave Jones:** All right.

**Chris Gammell:** Mm-hmm. And finally, given a couple... I guess I should probably put this at the top, but I have franchised my brand, Dave. Oh. Hardware Happy Hour. The thing that just happened here last night in Chicago, there's now one in Seattle. It's not actually franchised. I was just joking about that, but, like... So, if you're in Seattle and you want to join, it's going to happen February 1st, which would be Thursday of next week.

**Dave Jones:** Hardware Happy Hour, that's not an hour. No.

**Chris Gammell:** No. It's usually more than that. It's usually just...

**Dave Jones:** And it's not cheap drinks, right? Right.

**Chris Gammell:** No, it's hanging out at a bar and bringing your hardware to show off and meet nerds. Right. Yep. Cool. So, 3H Seattle. Mr. Kaiser might be there, so...

**Dave Jones:** Right. Yes, sir.

**Chris Gammell:** Yes. And so, on my end of things, after the show last week, I was talking to Richard, the guest who was talking about Laura and Laura Wan, and I am going to Amsterdam. So, if anyone else is out there and wants to hang out, I'll be out there next week. Excellent.

**Dave Jones:** Is this for work? Yeah. Oh, right. Cool.

**Chris Gammell:** Wireless. Wireless stuff. Woo! So, yeah.

**Dave Jones:** Is there a conference there? Oh, sorry.

**Chris Gammell:** There's a conference. Yeah. So, the Things Network is what we were talking about on the show last week, right? So, that's like a network of Laura Phi stuff. Right. That is one of the wide area networks that you can hop onto. Right. And found out there was a conference and got a ticket, and now I'm going. Cool. So, first time in Amsterdam. So, I'm excited about that. Excellent. I'll be around if anyone wants to meet up or...

**Dave Jones:** He'll be in the red light district. Oh, yeah. You'll find him standing under the red flashing light. You know me. Yep. Yeah. Yeah.

**Chris Gammell:** Red light district and pod cafes. Yep. That'll be me. Great stuff. Yeah. So, there's always more links on our subreddit. People can check them out there. But, Dave, it's good to have you back.

**Dave Jones:** It's good to be back. Yeah. It's good to be had.

**Chris Gammell:** All right. Cool, man. Well, let's talk to you next week or something.

**Dave Jones:** Catch you next time. See ya. Bye.

**Speaker ?:** Bye. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
