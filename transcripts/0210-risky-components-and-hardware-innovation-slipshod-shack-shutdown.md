---
episode: 210
title: Risky Components and Hardware Innovation - Slipshod Shack Shutdown
url: https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded August 5th, 2014. Episode 210. Slipshod. Shack. Shutdown.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. Who missed his cue there just by like 500 milliseconds or something, but it's noticeable.

**Chris Gammell:** Oh, yeah. Okay. Well, you know, there's always editing, man. There's always editing.

**Dave Jones:** Right. You can always take out that 100 milliseconds or something.

**Chris Gammell:** People wouldn't believe what I've taken out for Dave. It's just... Right. You could fill books. You could fill books and hours and hours of... One day the gag reel will be released.

**Dave Jones:** Yep. I was... Which is usually before or after the show talk, which is accidentally recorded. Yeah. I was just like reading the other day. Oh, well, maybe it wasn't the other day. I can't remember where, as usual. But it just sprung to mind, as I mentioned, that there's a limit of... Like, if there's a delay in perception, like of X milliseconds, like 300 milliseconds or something, the human mind, you know, like just has seizures or something. Not seizures, but it tunes out or something like that. The mind, if it's not prompted within a certain couple hundred milliseconds, I think it's 300 milliseconds. I can't remember what it actually was. So I'm talking out my ass here, and this is probably useless. But this is what we do here on the air now. We babble. It is.

**Chris Gammell:** Yep.

**Dave Jones:** About random shit that...

**Chris Gammell:** Sorry, I tuned out there for a second. It was about 300 milliseconds. I tuned out.

**Dave Jones:** 300 milliseconds pause. And apparently, yeah, if you don't engage within that amount of time, the mind, boom, it wanders. It goes elsewhere. So maybe it'll come to me by the end of the show, and then I'll just scream it out. Aha! That's where it was. Anyway, that just reminded me of that. Okay. So the human mind's amazing.

**Chris Gammell:** Some days.

**Dave Jones:** And it can be trained. I think it was to do with advertising. I think I got it. I think it was... I probably watched something on TV, and it has to do with subliminal advertising or something. And if there's a 300 millisecond pause or something, it makes all the difference. Or something like that. Yeah. Well, I would... Damp Hour no longer has advertising.

**Chris Gammell:** Or at least does not for right now. No, we don't.

**Dave Jones:** How the hell are we making our money?

**Chris Gammell:** We're not. It's all... We make it up in volume, Dave. We make it up in volume.

**Dave Jones:** We make it up in volume. That's it. Yeah. Oh, hey.

**Chris Gammell:** I think I got a notice on LinkedIn today that our anniversary is this week. So officially... Oh, is it? Congratulations on four years, man.

**Dave Jones:** Four years? You get less for murder. Yeah.

**Chris Gammell:** Less for murder. Well, not in the States. Oh, right. We do like our jails here. But yeah, man. Four years. Four years. Four years.

**Dave Jones:** Wow. Jeez, that's scary, isn't it?

**Chris Gammell:** Yeah. Well, you know. We could probably do another four before we kill each other. Yep. And even that, it's such a long distance to do, you know.

**Dave Jones:** And how many episodes? Two hundred and... This is two... Something, is it?

**Chris Gammell:** Two... Two... Ten, I believe. I think we're at two ten.

**Dave Jones:** Two ten. Wow.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Yep. And we've rarely missed a week.

**Chris Gammell:** Yeah.

**Dave Jones:** Only a couple of times. Handful at most.

**Chris Gammell:** Yeah.

**Dave Jones:** That's pretty impressive.

**Chris Gammell:** That's all right.

**Dave Jones:** If people want to know the key to success and the big bucks like we earn here on the Amp Hour, then it's consistency is the key.

**Chris Gammell:** Right. Annoying everybody week after week after week.

**Dave Jones:** Flogging that dead horse.

**Chris Gammell:** That's right.

**Chris Gammell:** Come on. Yeah. And now on the Kickstarter.

**Chris Gammell:** Yeah. And chip printers. Yes. How about something we do flog relatively often, but it is still a problem. What's up with your sourcing issues here? Seems like you've had some troubles of late.

**Dave Jones:** Yes. Yes. It all... Well, it started because I'm running out of microcurrents. The two thousand I made for the original Kickstarter campaign, even though I only needed like twelve, thirteen hundred or something. You know, I made two thousand because it was a nice round number and I knew I needed it. Well, I'm coming to the end. So if you want one, I've only got like fifty left sitting here or something. I've got orders to fulfill. So yeah, they're going to run out very shortly. So I hit the panic button, you know, that I have to reorder. And then I go to DigiKey. Sorry. Wah. That critical resistor you need is two months lead time. And go to the manufacturer. Yep. Thank you very much. Two months lead time.

**Speaker ?:** So...

**Chris Gammell:** Wow.

**Dave Jones:** Yes. Wonderful, isn't it?

**Chris Gammell:** The joy of having a critical part. This is why... So I've talked to people in sales before. And like, so sales organizations at chip companies, at least. And like, their main job these days, not to say they don't do other things, but like one of the big things that's like really, really important to the sales organizations is always like forecasting sales. Because as much as we complain about like lead times, right? Because really eight weeks, I don't know about a resistor fabrication facility, but like, you know, a chip fab, right? It takes at least 30 days, plus testing, plus packaging, plus shipping, everything else. It's probably eight weeks minimum anyways, you know, if you don't have like a hot lot. They need to know that stuff, right? They need to be able to supply. They don't want to be short and they don't want to have extra inventory either. So like, that's what sales is doing a lot these days is trying to guess at what people will need. And then they're judged on that.

**Dave Jones:** So I know.

**Chris Gammell:** Dave's numbers are not in the queue, apparently.

**Dave Jones:** No. And even when I even have my own special digi-key part number.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** I'm not kidding. Yeah, I think I've mentioned this. I have my own special digi-key part number, which then expedites the process with the supplier, right? And I, you know, I've teed up a deal with the manufacturer of these resistors and like the head marketing person there. And yet they're giving me special preference, right? And I'm still like, you know, a month or two out, right?

**Chris Gammell:** Well, special preference is always a relative term, right? I mean, if Apple comes out and says, we need a resistor first, I mean, they... Right, okay. Usually it's a little more money-driven.

**Dave Jones:** Yeah, but I'm going to get mine in eight weeks instead of the usual 11-week factory time. That's their standard factory time. Right. You know, so I'll get mine in eight weeks, maybe six if I'm lucky, you know, if they've got an idle slot somewhere, you know.

**Chris Gammell:** I like thinking about this with a reference to like software. I mean, like, oh, so yeah, you ordered your new license of, you know, your video software or whatever, and you bought your license. And deliver will be in about three months.

**Dave Jones:** Yeah, somebody has to hand code it.

**Chris Gammell:** Not only do we have to get all of the code, but through the factory, we also then have to assemble it into our product. And then we have to test it. There will be some yield issues, of course, and shipping.

**Dave Jones:** Oh, hardware. Hardware sucks. Hardware's hard. Hardware's hard. I'm doing a talk on that at the Maker Faire, not this weekend, but the next. So people in Sydney.

**Chris Gammell:** Hardware is not hard, but a fickle bitch.

**Dave Jones:** Well, it's something. No, trends, I think the title of the talk is, or the fireside chat. Oh, fireside chat, of course. Trends in hardware innovation. I've yet to come up with those trends, but I'll think of something. So if you've got any good. Yeah, the topic was sort of chosen, and everyone sort of went, oh, yeah, whatever. Okay.

**Chris Gammell:** And now we're going to have a day of BS for two hours, yeah.

**Dave Jones:** Right. The bastards are limiting me to an hour or 45 minutes or something. Oh, geez.

**Chris Gammell:** What can you possibly get done? I can't say hello in 45 minutes. I know, right? Yeah. Dave will do a video camera test in that amount of time. Yeah. Yeah. So, I mean, that's definitely going to be a good topic. But, so you're going to work sourcing in there or something, or what are you thinking?

**Dave Jones:** Oh, I don't know. Well, it's trends in hardware innovation is the topic. What things enable people to- Wank, wank, wank, wank. You know, so, yeah, it'll be, you know, it'll be obviously crowdfunding. There'll be, you know, embedded computing. You know, you can get Linux in a Raspberry Pi now, right? Internet of things and connected devices. You know, internet of things and connected devices and wank. No, but no, but there's other great things like, you know, PCB services, which people take for granted now. And now you can get, you know, prototype boards in, you know, for five, for practically free, you know, five bucks a square inch or something, you know? And it's like, it's just crazy. Even here in Australia, we've now got an equivalent to Osh Park here with exactly the same pricing. Yeah. Except it's in Australia and it's local, you know, dollars and local delivery. And-

**Chris Gammell:** I saw that, and I think there's one, there was another board share over in Europe as well. I think the only real difference is the volume, really. Because I know Lane sends out, like, at least an order a day. I'm not sure about the Aussie stuff. Because, you know, you have to get it to panels and people can go listen to it when Lane is on the show.

**Dave Jones:** Yeah, but they quote, like, five days turnaround and it's five Australian dollars per square inch, you know? And you get free boards. It's priced and worked exactly the same as Lane's. Oh, nice. You can use your funny money to pay for it, huh? Osh Park. Funny money. Australian funny money. They're our polymer notes. Isn't it like a plastic?

**Chris Gammell:** You guys are plastic money?

**Dave Jones:** Yeah, you're plastic money. Plastic polymer. Yeah, that's weird. Let's not mention the WikiLeaks thing, because I could go to jail.

**Chris Gammell:** Okay. I don't know what that is, but... Yeah, seriously. We'll let people look that up on their own.

**Dave Jones:** Yep. Australian gag order. Okay. Yep. Media talk about it. They go to jail.

**Chris Gammell:** Okay. So, we don't want Dave going to jail. Four years. It's been a good run, folks. Dave's in jail now.

**Dave Jones:** Not so. Yeah. But you're allowed to talk about it, because you're American. So, Australian law doesn't... If I knew what the hell you were talking about, sure. Yeah. Yeah. Right. Yeah. Yeah. Anyway, it does involve our... Yeah. Yeah. Something. Go look it up, I guess.

**Chris Gammell:** Yeah. That's cool, though. Yeah. So, I mean, that's a good topic as well, like the PCB stuff. And, you know, I think, how about open source CAD software? That's another innovation that's, you know... Oh, yeah. Multiple options. If not open source, at least low cost or free CAD tools as well.

**Dave Jones:** And then there's hackerspaces where you can go to get, you know, help from, you know, different skill sets and use tools and things like that. And, you know, so there's all these, you know, trends in hardware innovation. And I guess that's all covered under that sort of stuff. And there's more, so if you've got any good ideas, yeah, throw them my way, please.

**Chris Gammell:** Yeah. Definitely. And I'll talk about them. You know what the Aussie boardhouse thing is called? Or no?

**Dave Jones:** Breadboardkiller.com or .au. I'm not sure whether it's .com. Breadboardkiller. Yep. Okay. Type in. This makes for good radio. Yeah. Yep. It's breadboardkiller.com. Yeah. Okay. You get three copies of your board, $5 per square inch. And I think it's fine, you know, and they can go down to six mil trace space, you know, it's pretty good. And you get free shipping with that. Like, wow. You know, like, hence the name, you know, you don't have to breadboard anything anymore. It's, you know, it's cheap enough just to spin a board.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, this stuff didn't exist five, 10 years ago. You know, it was impossible. It cost you, you know, 500 bucks and two weeks and, you know, to get one little tiny board. Right.

**Chris Gammell:** Well, I think, you know, that could be an interesting point for your talk too, is not just what's going on now, but what that could actually enable. That's kind of what.

**Dave Jones:** That's the whole idea of the talk is what enables, you know, startups these days. Well, it's fast. You can do rapid development. There's so many.

**Chris Gammell:** So, well, yeah, I mean, I guess startups is an answer to that, but I'm just saying like, what else is there? Like, I don't know. So I see a lot of this stuff. Like, I always see like Tim O'Reilly talking about like, oh, hardware's, you know, everything's moving faster. Hardware is going to be a big deal. And, you know, and he's always talking about internet of things. And obviously SolidCon is about a lot of that stuff too. I don't know though. I have a bit of a hard time. What's that? Internet of things grown. I know. Well, yeah. And it's just a, I mean, it's a term, whatever, but like, connected devices, however you want to say it. But like, I guess I have a little bit of trouble kind of looking out farther. Like, I don't know what's out there. You know, like, okay.

**Dave Jones:** Well, if you did, you'd be, you know.

**Chris Gammell:** It's true. I wouldn't be talking to you. Leading it.

**Dave Jones:** Right. Exactly.

**Chris Gammell:** Talking to the waiter on the beach in the Maldives or something, you know. Right. Crystal clear waters and my own lab right off the beach. Oh, I got sand in my laser cutter again.

**Dave Jones:** Massage while you're working at your bench while getting a massage. Yeah, there you go. Crystal clear water and your own sharks with freaking lasers. That's right. Yeah.

**Chris Gammell:** It's all good. Yeah. Anyway. I don't know though. Maker Faire. Yeah, so you're going to be at Maker Faire, huh? I'm going to be at Maker Faire, yeah. Last week.

**Dave Jones:** And it's two days this time, which is awesome. Yeah, we mentioned that last week. That's good.

**Chris Gammell:** Next. Cool. I'm going to be given a KiCad seminar out in San Francisco, actually. Sweet. Yeah, so I'll be out there. At what? At what?

**Dave Jones:** You're just going to stand on the street corner and preach KiCad?

**Chris Gammell:** No, we're having a Supply Frame, like a Hangout, like Hackaday Supply Frame Hangout kind of event at our new office.

**Dave Jones:** And who's invited?

**Chris Gammell:** Everyone's invited. Oh, right. There's a... I'll post a link to a... What are those called? The things for you, like Eventbrite or whatever the ticket type of thing is. Oh, yeah.

**Dave Jones:** Right. Oh, right. Okay.

**Chris Gammell:** So, yeah, I'll be doing like a talk and there'll be talks on FPGAs and, you know, we'll just be hanging out, going over ideas and...

**Dave Jones:** I assume there's beer and food.

**Chris Gammell:** Oh, yeah. Definitely. Right. I wouldn't be there otherwise, man. Right. Yeah. So, yeah, this shit should be fun, though. I'm looking forward to it. Cool. And I'm going to be at DEFCON next weekend as well. I don't know... I have no idea what to expect for that. That is in... Oh, that's in Vegas. Yeah, that's in Vegas. Is that in Vegas? Right. Yeah.

**Dave Jones:** Dude, I think you need to move to the West Coast. I don't think I'm allowed to.

**Chris Gammell:** I don't think I'm allowed to.

**Dave Jones:** By she who must be obeyed?

**Chris Gammell:** I think so, yeah. Yeah, yeah. She's pretty adamant that she does not like... I don't know. There's a lot to be said about...

**Dave Jones:** How could you not like California?

**Chris Gammell:** Apart from the price. How could you not like it? I'm a pretty big cheapskate. You know, there's family back this way. Like, definitely... Right, right. Everybody's east of the Mississippi in the fam, so...

**Dave Jones:** All right. Got it.

**Chris Gammell:** Oh, well. Oh, well. Yeah, you're not moving either. Whatever.

**Dave Jones:** Nah, I'm not moving. So, I'll probably be hanging out. What am I going to do? Move to Western Australia?

**Chris Gammell:** Yeah, right. Ooh, jeez. Perth. What, are you going to start mining?

**Dave Jones:** Sorry, Perth listeners.

**Chris Gammell:** If there's any out there.

**Dave Jones:** There's more to Perth than mining. They have some nice canyons over there.

**Chris Gammell:** Oh, yeah? Oh, cool. Yeah. Yeah, so... But I'll be at DEF CON hanging out. There's a hardware hacking village. And I don't know what that means. Oh, right. But I'll be hanging out there and...

**Dave Jones:** People were hacking on their gaming machines. Is that the...

**Chris Gammell:** They sort of...

**Dave Jones:** They're in the casino there with the... Oh. You know, if the screwdriver in the back taking apart the hacker... Yeah, that makes you wonder, right?

**Chris Gammell:** Like, if they get nervous about that kind of stuff, like... Yeah, we're hosting hardware hackers and they're not allowed on the floor.

**Dave Jones:** Here are the world's best hackers inside your casino. That's right. Yeah.

**Chris Gammell:** Don't use any ATM machines. Don't do a walkie with a credit card or a smartphone. Mike Ostman will be out there. And so he'll be, like, doing HRF stuff. And there will be a bunch of stuff like that. So, yeah. I don't know. I don't know what to expect. We'll see. I'll tell you about it next week. Awesome. I think. Yeah. Oh, so speaking of tools, I mentioned that for your talk, like the free tools. We had talked about National Instruments. Remember how they pulled multi-SIM from... Oh, yeah. Yeah. ...analog devices, like the code branding they had before? Yep. So they brought it back out and now it's with Mouser, actually. So now you can download... And apparently it does, like, PCBs as well. I've never tried it and I never will. But, you know, they're like a simulation engine. They're kind of like an... You know, they're a little bit more of a graphical, like, LTSpice and stuff like that. But it's a Spice engine on the back end and then, you know, it can do layout and it's tied into, like, the Mouser catalog.

**Dave Jones:** Right. Every man, his dog's doing simulation stuff and things like that.

**Chris Gammell:** Yeah. Oh, yeah. There's a lot of web-based ones as well.

**Dave Jones:** Yeah, a lot of web. A lot of funky. Some of them are really funky. I mean, you know, you get animation of how the current flows and... Oh, yeah. That's the tablet one. That's it. Is that the tablet one? Yeah, that looks awesome. If you've seen the video for that. I meant to try that. I actually... I can't remember the name of it. Yeah.

**Chris Gammell:** Yeah. I got a tablet finally, so I should definitely try that out. Yeah. But, yeah, so when Mike Englehart was on the show, he mentioned a lot of stuff about the simulators and to be careful because a lot of them pull the open source Berkeley Spice. Right. But he said that there's a lot of inconsistencies. I mean, granted, you know, he runs LTSpice, so obviously he has very strong opinions about that stuff. But also...

**Dave Jones:** Exactly. LTSpice is awesome. This is designed for beginners. You know, all these web-based, they're all designed for beginners. They're not a professional tool. Right, right, right. Look, flasher LED. Here it is. Use your transistor. You know, it's not like...

**Dave Jones:** You know, it's not like it doesn't... You know, it's not designed for professional, you know, switch mode power supply type stuff that converges and does everything properly. And, you know, yeah. I mean, so it wouldn't surprise me if there's issues with it. But it shouldn't really matter.

**Chris Gammell:** I don't know. How do you feel about that for people like, you know, kind of like you kind of co-learning with Spice? Do you have strong feelings about that or like...

**Dave Jones:** Oh, you know, the Bob Pease feelings of, you know, Spice is shit. You know, like it's good. No, it has its place. Right. I mean, you know, because I use it. Right. So I've got nothing against it. Right. Because it's quicker than breadboarding sometimes. You don't want to try something out or you don't have the parts or whatever. You know, so you just want to test a circuit concept or something. Yeah. Right. Yeah. You know, it's good. But, you know, you can't just like simulate the whole thing and go, right, I'm going to go straight into production and... Or I'm going to start my Kickstarter campaign. Right. And, you know, I'm going to take this money and, oh, yeah, but it'll work because I've simulated it. You know, no. Okay. It's a useful tool, but yeah, it's just that, you know, you've got to know how to use it.

**Chris Gammell:** Right. And, yeah, I totally agree. You know, so I use that for the course as well. Like, and basically, though, I try and hold people off from it. And it really, you know, you should try and learn about, you know, low-level components on their own first, at least how they work. Mm-hmm. So it's not just a guess game, right? Yeah. Because you could try and do like a trial and error thing. Oh, what if I do this? What if I do this? Yeah. Yeah. Yeah. Unless you kind of co-learn it with, you know, your art of electronics in one hand and, you know, some basic transistor theory in another, right? Like, oh, well, oh, I put more current through the base and now the collector, no more currents going from the collector to the emitter. I, there might be something there, you know? Yeah, right. Yeah, yeah. There's something to this, folks.

**Dave Jones:** This newfangled transistor thing.

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Oh, dear.

**Chris Gammell:** Yeah, I've been actually, I've been going back. I have this piano, actually, this old, it's called a Wurlitzer 200.

**Dave Jones:** Yeah, I think you mentioned this way back, like four years ago.

**Chris Gammell:** Yeah, yeah. Actually, when I was kind of transitioning, moving back to Cleveland and getting back into electronics and stuff like that, I was fixing it up and I blew it up and stuff like that. And now that things are starting to sort of calm down, I doubt they'll actually stay calmed down, but I was, you know, I was just like looking at it and I've always wanted to redo that board because it's, you know, it's all through a whole, you know, it's like a hand-drawn, like hand-etched board. Type. Single side. Yeah, it's taped, exactly. Right. And it's a mess because people, you know, previous owners have hacked on it. So, you know, basically I put it back into Spice just to see, you know, just what I need to do and make sure I understand everything, click around. And it's great for that kind of thing. I mean, it's just a, it's a class A, B amplifier, basically. And, you know, but that's kind of a great thing because, you know, my amplifier theory is a little rusty. Really? And, you know, like.

**Dave Jones:** Come on, you're the analog man. Yeah.

**Chris Gammell:** Hey, man, it's been a while, you know, and, but it's a good tool for that kind of thing, you know, to have that crush to lean on and, like, be able to click around and, oh, yeah, that makes sense. Yeah, that makes sense. And then, of course, when I, you know, when I breadboard it again, it's, you have something to check against, right? That's the nice thing. Right. So.

**Dave Jones:** Got it. Yep.

**Chris Gammell:** Yeah. We'll see if that.

**Dave Jones:** I got nothing against it.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, we didn't finish the, my resistor story.

**Chris Gammell:** Oh, yeah. Let's loop back to that.

**Dave Jones:** Yeah. So what happened? Because, yeah, I found someone who has stock, right? Is it a. One person on the planet.

**Chris Gammell:** Is it a broker?

**Dave Jones:** It's a, one of the, no, it's one of the bigger distributors. Have you already bought it? One of their international affiliates. Well, I thought, look, I'll contact the local rep, right? I emailed the local rep, no, two days have gone by, no, screw you, okay? And I'm not going to call up a human. No, I'm just going to go and order it directly from the international website, right? But, you know, it's 6,000, it's over $6,000, right? Whoa. That's a lot. For some resistors, right? This is half the price of a new car here in this country, right?

**Chris Gammell:** Yeah.

**Dave Jones:** For a bunch of resistors. Well. They're resistors, right? How much did you pay last?

**Chris Gammell:** Maybe that's a good reference point, too. Wasn't it like 2K you paid last time?

**Dave Jones:** No, it's not a huge amount more than what I paid last time. Plus, there's, I have to order a minimum amount more than what I actually wanted.

**Chris Gammell:** But still, you know, it's like, you know. That's a lot of, yeah, that's a lot, man.

**Dave Jones:** You know, it's, but, you know, it cost me X amount to make each unit, and I'm going to make another 1,000, right? Yeah. So, you know, it's going to cost me X amount. But when you're just, you know, when you're doing that buy it now button. That's a bitter pill. Which I haven't done yet. I'm going to do this after the show. And it's like, yeah, like, like six grand. Like, and I can't even buy any smaller quantities to avoid customs. And so, yeah, so I'm going to get slugged with, you know, customs, GST, and the whole bloody works as they come. And the associated delays with that as they hold them there in customs in Australia. And it's just, you know, it's just bloody annoying.

**Chris Gammell:** On the bright side, it's not super heavy. You're not paying tons of freight charges, right? Oh, no, no, no.

**Dave Jones:** It's like, it fits in a tiny little cardboard box.

**Chris Gammell:** Yeah, you're not buying heat sinks in 1,000 quantities, right?

**Dave Jones:** But it's just amazing when you compare it, you know, like a complex thing, like a car. You know, it's half the price of a good, of a, you know, of a brand new car.

**Chris Gammell:** Yeah, but at the same time, they're buying, you know, they're buying a quarter million worth of brake pedals from some manufacturer.

**Dave Jones:** I know, but it's a car, dude. It's a freaking car.

**Chris Gammell:** But that costs as much as, you know, 10 cruise liners. I don't know how much it costs to make brakes.

**Dave Jones:** I know, but it's one resistor. It's one freaking resistor, you know?

**Chris Gammell:** Yeah, but it's also the main resistor. Like, that's the thing. Like, that's the main thing in your design, right? I know. It's the main thing on my own design. The main thing on my design. Yeah. Exactly. Exactly. And you're paying for not calibrating.

**Dave Jones:** Exactly. I'm paying for the extremely low temp car. Yeah. I'm paying for not calibrating the thing. Yeah. In theory, it probably might be cheaper for me to put in a, you know, a, you know, a 30-cent resistor and then trim it. Right.

**Chris Gammell:** So, wrong. It could be. Disagree. I mean, because that's... It depends. That's what... It depends on what your labor's worth. Well, yeah, but I just think from a... So, basically, you're also... What you're also paying for here is you're paying to offload the risk, right? I mean, that's really what it comes down to. Oh, yeah. Yeah, yeah. So, as well. Yeah. If it... You know, and you've had this before. You've talked about this on the show where parts came in and they weren't just back and you get to go back to the manufacturer and you yell at them and whatever else. But the other one is now what if you buy that 30-cent resistor and you have a test program in place, but what if, you know, it's known to happen...

**Dave Jones:** The operator was pissed off or they didn't follow the rules.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** The operator is doing it. Yeah, yeah.

**Chris Gammell:** Yeah, or like even worse, like test stands just don't do their job sometimes. Sometimes they just have random failures and they don't, you know, you don't have the right error checking in there. These things happen and, you know, you get all the way to the customer and then you're out whatever you charge them plus all the replacement fees, everything else.

**Dave Jones:** Absolutely. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah, you've got to weigh... It still might come in cheaper or it might come in more expensive. Hard to do those calcs, you know. Yeah. But, so, yeah, I'm buying peace of mind. You know, if somebody comes back to me and says, oh, I measured... You know, I've had this, right? And people do sound like this, you know. Oh, I bought a microcurrent and it measures wrong and it's out. And I used this $50 cheapy multimeter from Dick Smith to measure the output and it says it's 2% out. And like, no, you know, and it's like...

**Chris Gammell:** Right, right, exactly.

**Dave Jones:** You know, I can be pretty confident that it's not the microcurrent.

**Chris Gammell:** Right. Well, you're removing a troubleshooting variable, right? I mean, that's effective what you're doing. Yeah, exactly.

**Dave Jones:** Yeah, because I've got a two-step process. Not only do I buy the precision resistors from one of the world... Probably the best, world's best manufacturer of these things, right? There's a reason that they cost so many dollars each, you know, that they're thoroughly tested. And then I test... Then each unit is individually tested to spec anyway, after, you know, as part of the manufacturing at the assembler testing for me to spec using a jig that I designed and built, you know? And, you know, so I'm pretty confident when I send those things out that it's going to be damn close to spec, you know? It could be a... In theory, it could be a smidgen out, right? Yeah. But that's unlikely too. But, you know, for it to be like a couple of percent out, you know, it's like, no. You know, so I can confidently tell these people that, no, you're measuring it wrong, you know?

**Chris Gammell:** Right, yeah, exactly. And that's what makes it worth it. Yeah, that's a, you know, that's a big part. Like, I think about this a lot. Like, risk. Risk is kind of like one of the big things in procurement. Risk sucks. It does. But it's like...

**Dave Jones:** I hate risk in my life. It's just risk equals stress, you know? It does.

**Chris Gammell:** And you'll get it every time. But when you really look at it, like, that's what engineers get paid for, right? They get paid to reduce risk, right? You design tests... Mitigate risk, yes. ...in order to mitigate risk, right? And, you know, it's just all about, you know, making those decisions. And the tough part, you know, like, so, like, this is not necessarily early in your design cycle. But if this was early in your design cycle, you have to try and predict, you know, six months out, a year out, two years out, how a part you design in early ends up... Could end up biting you in the ass later, right? Because if you design in something now and you don't have any idea about the risk, you won't actually know... You know, if you design in something now because it looks good, it's available on DigiKey, it's low price... Well, that's great, but what if it's low price because they're trying to unload stock right now, you know? And it's like, oh, crap, that part's going out of... You know, you don't know. It could just be going out of production. And that's why it was low cost.

**Dave Jones:** Nobody else is using it. Nobody's buying it. Because the manufacturer, the chip manufacturers keep, you know, huge stats on these things. And they build to, you know, they know a part's going to be, you know, on average, yes, another order for $50,000 is going to come through next month, so we'll make some more. Right. You know, but if they're seeing the trend down on that part, it's not going to sit into their schedule. And that's when you're going to get hit with your 12-week lead time.

**Chris Gammell:** Right. You know, thank you very much.

**Dave Jones:** Or worse, yeah. Or it's discontinued or it's 40 weeks. You know, I can remember back in the 90s when, you know, chips were in here in Australia together. They were 40 weeks. I'm not kidding. 40.

**Chris Gammell:** Right. I believe it. That was a year or two ago as well. There was all those lead time issues as well. I don't remember what the reasoning was, but I remember there was an inductor I got quoted that was like a year plus. It was crazy. Yeah.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** And it's just capacity stuff and it's them looking at their risk as well. I mean, that's everybody's playing that game. You know, that's why, like I said with the salespeople, that's why they're looking at, you know, trying to forecast and all that other stuff. It's everybody just like on their tippy toes. Oh, crap. Oh, crap. Oh, crap. You know? And then it's like the really big problem I see is like, you know, for a lot of analog parts that I look at these days, you know, they're all, there's no footprint cross at all. Right. There's no compatibility. Right. Right. And so it's like your risk now is baked in. You know, you pick a part, you pick a footprint. Unless you do a footprint, you know, and have like a second one on board where you can switch over to it. You're screwed, you know? Well, you're not screwed. It's just you're going to take a huge hit to your schedule.

**Speaker ?:** No, no.

**Dave Jones:** Exactly. Because you've got to re-spin the board and then you might introduce another failure and, you know, you've got to re-qualify it and everything else. You've got to change your, you know, your mask and your paste and stencil and everything else, you know? It all changes. It's going to reprogram the pick and place machine so they can goof that up, you know, again. And like, you know, it all just flows and flows.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. And it goes all the way back to the, you know, all the way back to the fabs. Right. And the reason that they're all on tippy toes is because it's so frigging expensive to operate the fabs as well, right? I mean, that's the reason that we have this problem. You know, that's why.

**Dave Jones:** And they've got every bastard like us screaming at them.

**Chris Gammell:** Well, yeah.

**Dave Jones:** Where's my part? Where's my part?

**Chris Gammell:** Well, I think there's much more important bastards than us that are screaming about their parts. Well, like, so like IBM, right? There was this news, I don't know when it was from. But basically they were, they wanted to pay global foundries to take the chip business off their hands. Right. So IBM has this, you know, I think they're down to mostly server chips and they have some advanced RF chemistries and stuff like that. But, you know, they run a high end. Basically, there's tons of costs there, right? And unless you really, really need chips, you know, IBM is most of us.

**Dave Jones:** So they're willing to pay someone to take their chip business.

**Chris Gammell:** Exactly. Exactly.

**Dave Jones:** Rather than, we're looking to sell our chip business, we're looking to pay you. Here's a billion dollars, you know. Yeah, they're trying to get it off the books, right? Maybe we should rock up. Yeah. Yeah, exactly. Yeah.

**Chris Gammell:** Because it's going to be, I mean, because they've been taking losses for so long.

**Dave Jones:** Oh, IBM's in deep shit. IBM is in deep shit. I've been reading a bit on that. Oh, yeah? They're going down the Googler fast. I don't know.

**Chris Gammell:** Nobody ever got fired for buying IBM. You ever hear that phrase?

**Dave Jones:** Right. Yes, it was common back in the 80s, 70s.

**Chris Gammell:** I don't know. It'll subsist in some form.

**Dave Jones:** No, IBM have been doing, if you're reading, it's in all the financial blurbs and stuff like that IBM are the poster child in the US now for, I'm not into this finance stuff, but they're doing the finances all wrong. They're doing it for short-term gain only. And like, yeah, yeah, the government are paying them, you know, they're like giving them grants or whatever or the tax cuts or whatever. And they're using it not to reinvest in the business and build the business and grow. They're using it to pay themselves back and buy back their own shares. Oh, wow. And apparently that's great for short-term gain. Right. But in five years, everyone in the financial industry is saying, yeah, IBM will be ruined. Right. They will be, you know, because, yeah, it must come to an end.

**Chris Gammell:** Well, any company that's, you know, chasing those short-term things, that's always the NBA playbook, the, you know. Exactly. Exactly. Trying to align some pockets and stuff.

**Dave Jones:** Yep. You heard it here first. You heard it here first, folks.

**Chris Gammell:** IBM will fail in five years' time. Financial analyst David Dell Jones.

**Dave Jones:** That's right.

**Chris Gammell:** Who heard it from other financial analysts, but he wasn't really paying attention. That's right. Yeah. I mean, it's tough, too, when you see, like, I always think about it when you see these hardware, you see hardware companies moving towards, like, software, and they always make these, you know, HP as well, right? I mean, HP still makes laptops for brands' laptops, I guess.

**Dave Jones:** And printers.

**Chris Gammell:** Yeah. But it's all consumer level. It's super low-end. And they all want to move to, like, this, you know, software as a service model. Everybody loves that kind of stuff. Oh, yeah, we'll write software for you. And it's just, it's the same story all the time. It's like, I don't know. It's not like hardware's easy, right? I mean, it's a tough game, but I think that software stuff is, it's, meh. Yeah. Speaking of hardware companies in trouble, how about Radio Shack? Do you see that stuff? The, uh...

**Dave Jones:** Yeah. Rat Shack.

**Chris Gammell:** Rat Shack. Is that what you call them?

**Dave Jones:** Rat Shack. You're, see, you're too young, right? Of course. Everyone back in the U.S. Even I know this. Everyone in the U.S. used to call it Rat Shack. Well, here it was never called Radio Shack. It was Tandy.

**Chris Gammell:** Right, right, right.

**Dave Jones:** Yeah, yeah, which was, um... I, I did, technically, that was my first job, so to speak. Oh, yeah? Was working in the Radio Shack Repair Centre. Um, in high school, I was doing it as my work experience thing. Huh, yeah. That's cool. I worked in the local Radio Shack, yeah.

**Chris Gammell:** Right, when people actually still took stuff in to get fixed and that kind of thing. Exactly.

**Dave Jones:** Yep. They took in their Radio Shack Model 4 computer, you know, and they got it fixed, you know.

**Chris Gammell:** What does one need to get, like, would they, like, blow out power supplies, or what are those usually...

**Dave Jones:** Oh, power supplies fail, drives need to be aligned again, you know, so I was, you know, aligning the disk drives and, you know, stuff like that. They had to be cleaned and re-aligned. Aligning them? The heads cleaned, and you had to re-align the heads on the drives.

**Chris Gammell:** They weren't, like, sealed or anything? I mean, like...

**Dave Jones:** No, dude, these had, you know, adjustment pots on them. Wait, are we saying, like, floppy drives?

**Chris Gammell:** Is that what it means?

**Dave Jones:** Floppy drives, yeah. Oh, okay. You would put in a specialized floppy testis that had all the alignment stuff on it, and you would, you know, read out on a scope, and you'd get the, you know, and you'd tweak them, and yeah, yeah.

**Chris Gammell:** Interesting.

**Dave Jones:** Yeah? Yeah, yeah, yeah.

**Chris Gammell:** I know what you're talking about now. Because then, yeah, because, like, the head moved up, didn't it? Like, the read head, and so the mechanical...

**Dave Jones:** Yeah, it moves in and out. The head moves in and out, and the speed, you know, and the, you know, it's... The speed is different on the inner ring than the outer ring, and, you know, all that sort of jazz.

**Speaker ?:** Right, right, right.

**Dave Jones:** Anyway.

**Chris Gammell:** I was thinking hard drive, but then I remembered that... Right. They didn't quite do that. They used to just run right off the floppy disk.

**Dave Jones:** Exactly. Yeah. So, dude... Old. Yeah. Really old. And the head height, you know, the head, it flies above the disk, it flies a certain distance above the disk, the heads, you know, so you had to set the height, and, you know, all this stuff was tweakable. Oh, man. And, you know, it would all wear loose, you know, these drives would just shake themselves out of alignment, you know? It was great. So, there you go. Technically, that was my first job. That's great, man.

**Chris Gammell:** Yeah, that's a shame, too. I mean, actually, so I think about it, too, my first job was repair. Yeah. It was on amplifiers, but... Yep. Like, voice amps, but... It's a good thing.

**Dave Jones:** So, are Radio Shack going under? They're axing, like, 2,500 stores or something. But doesn't the article say that, like, they are in such... They're running out of cash so quickly, they can't actually afford to close the stores.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Because it costs money to shut a store down to, you know, liquidate sales. I don't know. Right, yeah. I don't know. It costs are involved in shutting down a store.

**Chris Gammell:** Hire people to clean it out and stuff like that. Right, okay.

**Dave Jones:** And apparently, they don't have the money to do it. So, is it goodbye Radio Shack? Well, they're at least closing half their stores. They've got 4,000 stores in the US.

**Chris Gammell:** So, here's the thing. I don't really care. Right. So, here's the thing I do like. I mean, like, I like that they jumped into the maker movement probably a little bit too late. I mean, they sponsor Maker Faire stuff. Right. But, I don't. Yeah. I just don't. I mean, like, brick and mortar, I just don't think. I don't think many brick and mortar stores are going to survive the online era. Yeah. Especially for really niche stuff like, you know, electronics and stuff like that. You know, like, I look at. So, like, Micro Center is a store around here and there's other ones around the States. It's a computer store. It's like a full-blown computer store. Still doing well. I think locally owned. Maybe not locally owned. But, like, Fry's and Micro Center, these are all, like, computer stores. And then they have a pretty healthy section. You go in there and they have Adafruit stuff. They have SparkFun maker store or whatever that's called. And, like, that's tenable. But there's not much else at Radio Shack. So, I don't know.

**Dave Jones:** Right. And apparently that's why they're failing. Because everyone thinks the same way. Right. Well, yeah. I think the same way. Because they're a public store. Like, you know, nobody in our. No hobbyists go in there, do they? I. You get something. Maybe if you're desperate. If you're desperate. You might go in and get a.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Buy some 1.914s and, like, a four pack for $2 or something like that. Right. Yeah. I think I did that once. I was pretty desperate. But, yeah. I mean, like. I love it. I. I just don't know. Oh, well. We still haven't heard from. What's it called? What was the kit company, too? Once you had, like, the scope kits and the radios and stuff. Oh, Heathkit. Heathkit, yeah. Well, there was supposed to be a reboot for that, too. I'm sure the same kind of thing will happen.

**Dave Jones:** They've rebooted a couple of times, haven't they? Yeah.

**Chris Gammell:** Yeah. Yeah. Well, and, like. But, like, the same kind of thing. It's, like, past a certain point. I know there's nostalgia for the brand and stuff like that. Yeah.

**Dave Jones:** But the people. But people are getting to the age where the people who have the nostalgia for the brand are dying. Right? Oh, yeah. I mean, yeah. Exactly. Right? So, seriously. Right. Like, in another 10 years, nobody will remember Heathkit, you know?

**Chris Gammell:** Well, they will because of swap meets and people still try and sell people. Right. Okay. But still. Yeah. I mean, like, the ham community as well. There's a lot of Heathkit stuff in the ham community. Maybe not, like, you know, it's not high-end or anything. But, you know, and I weep a little bit for the, you know, the easily-assemblable, you know, kits for that kind of thing. And same for Radio Shack, the available parts. But none of that really exists anymore. So, how can you really weep for it, you know? Right. But it's just a changing world. So, other stuff will work. You know, the Adafruits, the Spark Funds, those guys will kind of fill the void. And they've done a great job so far. So, I don't see too much reason to stress.

**Dave Jones:** Hey, what's this about Tesla are teaming up with Panasonic for their Giga battery factory?

**Chris Gammell:** Yeah.

**Dave Jones:** We love talking about Tesla on here.

**Chris Gammell:** We do love Tesla.

**Dave Jones:** Because they kick ass.

**Chris Gammell:** They do. And I was actually just back in New York. And there was, like, a commercial on the TV about that. I think they're giving some sick tax breaks. That's probably another reason. Because they're going to do it in Niagara Falls. Right. Back by my hometown.

**Dave Jones:** Oh, are they? Is that where they chose? Because I know they had, like, four states up for grabs or something.

**Chris Gammell:** I think there's multiple factories in the works. But I'm pretty sure that... Oh, actually, no. I'm sorry. That was Solar City.

**Dave Jones:** Is the state up there? What's the state up there?

**Chris Gammell:** New York State.

**Dave Jones:** Oh, right. So it's actually New York State. Okay.

**Chris Gammell:** Right, right. So, yeah. If people are not US people, New York is a city and a state.

**Dave Jones:** So they've won the Giga battery factory. What's that? They've won the Giga battery factory contract.

**Chris Gammell:** I think that's actually the solar factories up there. I think that's the one that's up in New York, now that I think about it. It might be New Mexico. That's the Tesla one. Right. But, yeah. That's good. I mean, that's, you know, it's kind of scaling issues, right? It's always tough to get off the ground, especially for big stuff like this. So that's a good thing to team up. Yeah. I heard rumor, too, that they might get into grid storage as well. I'm a little bit more trepidatious about that. I don't think that's really...

**Dave Jones:** Well, they'll probably need it for their own bloody factory because they're going to power the factory by a solar and they're going to have to run their factory 24-7. So no wonder they're getting into grid storage. They'll have to. Just locally, it makes sense to do that.

**Chris Gammell:** I guess so. But I don't know, man. Like, that's just that scale. Like, what are the battery packs on, like, a Tesla, right? I mean, like, they're 20 kilowatt hours, 30 kilowatt hours, something like that. I don't know the exact figure, yeah. Yeah. I mean, they're big, but, like, I don't know. Like, that's a lot of... Like, to really have grid-level storage, you need a lot. Oh, no, no.

**Dave Jones:** Grid... No, you don't do grid-level storage in batteries. You do them in, like, big mechanical flywheels and stuff like that.

**Chris Gammell:** No, but that's what they're talking about. That's what they were saying is, like, yeah, they were talking about getting into that. I mean, like... Like, so when we had Bob Simpson in the show...

**Dave Jones:** You wouldn't do them in 186... You wouldn't do them in 18650 cells.

**Chris Gammell:** That's what they were saying, though. That's what the rumor was. And that's why I'm with you with that drone. I mean, I think it's silly, right? I mean...

**Dave Jones:** It just seems inefficient. It seems inefficient.

**Chris Gammell:** It does. I mean, I always like the idea of, like, the pumping water up the hill, but that one's tough, too, because that's very physical, you know?

**Dave Jones:** Yeah, but it works. It's great. You know, there's lots of, you know, that storage when you pump something up, you know, you pump water up to a dam and then you release it. There's, you know... That has huge efficiencies to it.

**Speaker ?:** But...

**Chris Gammell:** So... Yeah, probably. Yeah, and that's the question. I think it's just more of a scale thing. I mean, like, that's what we always talk about on this show is scale. Scale is the thing a lot of people don't understand. I feel like a lot of people don't understand that. It's just, like, grid level scale is huge. You know, like, to get to the megawatt output of a single coal plant, you know, like... Yeah, that's... It takes so much.

**Dave Jones:** That's why you've got to have huge machines. That's why, you know, when you said, like, 18650 batteries, it's like, huh? Yeah, well... How can that be efficient, right? You've got so many interconnect losses alone, you know? Like, it's okay for a car, but, yeah, I mean, on the bigger scale, no, they have to do, you know, molten salt. They have to do, I don't know... Yeah, I've seen that one, too. You know, water, you know, dam storage, or, you know, big flywheels, or something like that, you know? You've got to, you know, big, big industrial age kind of things.

**Chris Gammell:** Elon on the phone calling Dave to, uh... Do you have any ideas, Dave? Sorry. That's okay. Yeah, so, we'll see how it works out. Interesting article, though. There's another Spectrum article.

**Speaker ?:** Right.

**Chris Gammell:** So, uh... Yeah. Again, you know, we talked about it last week with the battery stuff. I don't really get it. It's, uh, you know, it's gonna be a lot of chemical engineers. Good job, guys. Kick out those batteries, you know? Help Tesla output 100,000 cars instead of 30,000, whatever their plans are.

**Dave Jones:** Yeah, exactly. That's good. I don't know. Anyway, that's cool. So, what a Panasonic bring into the, uh... Bring into the table.

**Chris Gammell:** Uh, probably the manufacturing knowledge. Uh...

**Dave Jones:** Right.

**Chris Gammell:** You know, and like I said, like, it's always... Yeah, yeah. It's always getting started, right? It's always, it's always, you know, knowing how to build a factory. Like, even Tesla, like, their car factory, they retrofitted, but they didn't build... You know, when you think about starting up a new fab, anything like that, it's, uh, it's crazy.

**Dave Jones:** Yeah, but they stole all the smart... They stole all the smart people from Toyota and all those sort of companies. Oh, yeah? I didn't know that. That knew how to mass manufacture stuff. Oh, yeah. Yeah. Yeah. But as far as I know, nobody actually, no other company actually helped them build their Tesla factory.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Like, I think they just hired all the smart people from the existing car makers, and then they, you know, knew how to do it. So... Yeah.

**Chris Gammell:** Yeah, so, I was, uh, I helped, when I was down at Samsung, actually, I, I was there when they were building... So, the reason that I got hired in the first place, and the reason my 200 tow workers got hired at the same time, is because we were starting up a fab. It was a chip fab. Right. But, like, even just the scale, like, it, like, just the building alone, right? That, like, that is something you don't think about. You're like, oh, yeah, of course, like, build a building. Like, they know how to do that, but, like, like, all of the, like, you went into, like, the sub, sub basements and all that stuff. Like, all of the logistics of just getting piping in, you know, all of that.

**Dave Jones:** Oh, piping, because they need massive amounts of water and all sorts of jazz, you know. Yeah, oh, yeah.

**Chris Gammell:** Yeah, the facilities people there.

**Dave Jones:** No, you have to design that stuff in.

**Chris Gammell:** Right. They're, I mean, they're superheroes, because you think about, like, especially, like, in a clean room, too, like, getting all that stuff in there was crazy. And I had nothing to do with it, right? I sat around in a trailer, you know, learning how to do this stuff until the fab was done, basically, you know, and I just got to sit there and watch it. It was great. But, you know, like, looking at all of the logistics for that kind of stuff, too, that could just as much be a reason to partner up with people that are, have expertise in building that kind of stuff, right? Yeah.

**Dave Jones:** Fair call.

**Chris Gammell:** Yeah. It's a big deal, especially if it's going to be giga, right? They always do. I remember seeing someone online, they lamented that, why is everything always in football field units, right? Yeah, right.

**Dave Jones:** Units of football fields, yeah. Units of football fields, yeah.

**Chris Gammell:** And the fab that I worked in was nine football fields long, or wide, I guess it would be. So it was, you know, one long and then you stacked them side by side, there was nine of them.

**Dave Jones:** Right. Was it one big open thing?

**Chris Gammell:** Yeah, that's the crazy thing. Right. There was no, you can't have pillars, so it was all trust. Right. So there was these gigantic trusses that came in. It was really cool to see, actually. Wow. Yeah. But yeah, go Samsung. Don't miss it. Yeah. So yeah, that's good. That's good to see. Hope they keep moving that stuff forward.

**Dave Jones:** Absolutely. What else we got?

**Chris Gammell:** Well, we didn't talk about it last week. Is there a reason we didn't talk about it last week? Yeah, kind of. So it's the, you know, I forget what it's called. Oh, shoot. It's like the little printer thing. There's like a little, there's a PCB printer with like silver ink. It's like another one of those things.

**Dave Jones:** Oh, yeah, yeah. It's another Kickstarter, right? Yeah. It's in competition to the one that I looked at at the trade show here. Yeah. The Australian mob who are doing it. It's yet another printable ink thing. And I, yeah, I look at this and go, okay. Yeah, squeak or whatever, squeak or whatever.

**Chris Gammell:** Which is a funny name, but.

**Dave Jones:** You know, it's, I bet it's silver ink. I bet it's.

**Chris Gammell:** It is silver ink. Yes, that's correct.

**Dave Jones:** There you go. Right. There you go. Makes sense now the name. Anyway, the other one is the Cartesian Co. That's right. Yep, yep, yep. Yeah, yeah. Anyway, I look at these things and I go, yeah, okay. They're cute for like learning beginners to, you know, play around with, but it's not a serious tool. It never will be a serious tool for manufacturing prototype PCBs. Not when you can get professional double-sided silk screen solder mask boards for $5 per square inch for three.

**Chris Gammell:** Right. Right?

**Dave Jones:** It's just, so I don't get it. You know, like, yeah, you can make, like you can print onto fabrics and you can print onto flexible things. Okay, that's a novel little, you know, niche thing. But apart from that, you know, no. Like, and that's the problem I have with it is that a lot of people developing these things, a lot of people talking about these things, they always talk about, oh, you'll be able to print your own PCBs at home. No, it's not the same thing. It's not nearly the same thing as having a proper rigid double-sided plated through a solder mask silkscreen PCB. Right. So come back with me when you can do that. Okay? Okay? Otherwise, I don't really want to know about it. It's of no interest to anyone who's designing serious electronics. Well, I don't think it's really sold for that either.

**Chris Gammell:** I mean, it's... But I think that, you know, for three grand, it has to be, right? I mean, like, three grand is pretty significant, right? See?

**Dave Jones:** Three grand. Holy crap. You know? Yeah.

**Chris Gammell:** So the thing that I did like about this, and I wasn't sure about Cartesian Co., the previous one. Yep. I'm pretty sure they used, like, low-temp solder. The thing that was interesting about this one was that they used...

**Dave Jones:** No, they used a silver type ink. You know? No, no, no. I know.

**Chris Gammell:** But I'm saying the actual assembly then. Didn't they say, like, oh, we have low-temp solder? Like, do you use, like, a...

**Dave Jones:** No, I think they could do it on paper with a regular solder and iron. Yeah, it just had to be very quick. There was a technique to it or something. And you could reflow them as well, apparently. Okay. So this is different, though. So it was a bit better than I expected. Yeah.

**Chris Gammell:** So this one's different because it does, instead of doing paste, like, solder paste, it actually does adhesive, conductive adhesive, which is something that I hadn't seen before. Yep. Yes. And that's interesting. You know, and maybe this is all kind of just marching towards something that could make sense later, but that basically, you know, basically because they say they have a built-in pick-in-place, it has, like, a little vacuum nozzle, and then they have a built-in adhesive dispenser. Yep. It is possible that, you know, that makes... I mean, that's basically...

**Dave Jones:** That kind of adds another thing on there, but...

**Chris Gammell:** Yeah, right.

**Dave Jones:** You know, for five bucks, you can get a Mylar stencil for your solder paste, and then, you know, like...

**Chris Gammell:** Yeah, no, I know. Yeah, yeah. Dave, I'm right with you, man, but I'm just saying, like, I do want to credit them with some interesting stuff, right? I mean... Oh, yeah, no, no, totally.

**Dave Jones:** People will think that I'm bashing them. I'm not, okay? I'm just bashing anyone who tries to think that it is comparable with proper PCBs. It's not.

**Chris Gammell:** Right. Right. So, again, you know, maybe niche, you know, for...

**Dave Jones:** Otherwise, it's very cool on its own.

**Chris Gammell:** The flexibles and stuff like that. That's cool, right?

**Dave Jones:** For the flexibles, the fabrics and all... Yeah. ...whatever you want to do, those, you know, more exotic, sort of arty crafty kind of things. It's probably very good. Yeah. It's very expensive for that kind of thing. You know? Well, yeah. Right, right. Hey, you know. No, no, it's good. So, I support them. I just don't think it's a replacement for PCBs. Yeah. In fact, it's not. So, I'm right. Okay. Yeah. Yeah. Anyway. Hmm. Just like you and your stupid chip printer.

**Chris Gammell:** Yeah. Whatever.

**Dave Jones:** Never admit defeat.

**Chris Gammell:** What else should we cover here? Have you seen the flybook thing? I've actually been really interested in this since I've seen it from TI. Do you ever look at that?

**Dave Jones:** No, it's flybuck.

**Chris Gammell:** Flybuck. It's like... It's a new... Not new.

**Dave Jones:** It's a combination of a flyback and buck converter. What?

**Chris Gammell:** Right. Exactly. So, basically... Is it? Oh, okay. I just guessed. Yeah, yeah. That's right. Yeah.

**Dave Jones:** It makes sense by the name. Yeah.

**Chris Gammell:** So, they do... So, like, I was very interested in, like, isolated power stuff. Like, doing flybacks and stuff like that. But, you know, basically, people that don't know if you drive... You know, you drive a transformer and, basically, you know, you can sense... You can either have a feedback element through an opto-isolator or you can... You can... There's a chip I was using. There's a couple now that have primary side sense. So, you actually only have to do it on one side. Yeah. And, basically, the inductance of the coils on the transformer can help you determine how much... You know, how to change your control algorithm on the primary side. This one's interesting.

**Dave Jones:** I can... I can just see the... I just looked at the schematic then and I can instantly see what they're trying to do here without even reading it.

**Chris Gammell:** Okay. Why don't you tell us what you think it is?

**Dave Jones:** Okay. I'll tell... I haven't read the article here. You'll have to trust me. But, they're... Right? They've got your traditional buck. Nothing up his sleeves. Yeah. Exactly. Yeah. They've got your traditional buck converter and, you know, how you have an inductor for the buck converter. That's right. Well, instead of using just an inductor, they're coupling that and using it as a transformer as well, which then gives you the flyback...

**Chris Gammell:** Flyback-like behavior. Right.

**Dave Jones:** A flyback-like behavior. So, you're getting two for the price of one then. Yeah. Almost. Right. Exactly. So, your inductor for your buck converter now has to be a transformer. So, you're using the primary side of the transformer as an inductor for your buck and then the secondary... And then, you know, because it's a transformer, you can tap off the secondary side and then it's a quasi-flyback kind of...

**Chris Gammell:** Right.

**Dave Jones:** Yeah. Yeah. Yeah. I mean, yeah.

**Chris Gammell:** And you can just use a coupled inductor. You don't have to actually use a proper... I mean, granted, that is, you know, a type of transformer, but...

**Dave Jones:** Well, it is a transformer. Yeah. Right. Right. Right.

**Chris Gammell:** But usually, it's a simpler device as well. You know, it's usually one-to-one, right, and stuff like that. But, you know, you could drive multiple coils as well and stuff like that, and it really simplifies things. And the reason that I liked it is that the waveform's a lot less messy. You know, like, it's a really known waveform when you do a buck and...

**Dave Jones:** Yep.

**Chris Gammell:** And basically, then, on the secondary side, it's all open loop. And that's... Right.

**Dave Jones:** Yes.

**Chris Gammell:** Yes, it is. But, I mean, like, I don't know about you. Like, I don't really care.

**Dave Jones:** Presumably, it's not high current on the flyback secondary.

**Chris Gammell:** I don't think so.

**Dave Jones:** The quasi-flyback secondary. I think so. Unless you... Because if you said, if it's like a loosely coupled sort of...

**Chris Gammell:** Well, basically, the idea is you're going to be driving, you know, you're going to be controlling based on whatever's on your primary side. So, you'll probably put something simple over there. And then, you know, whatever's on the isolated side, you won't have a huge load over there. But you could probably... I don't know the exact figures about how much you could drive on the secondary. But my first...

**Dave Jones:** Probably not much. Because my first thought is that the capability on the second side, the flyback, isolated flyback side, is going to be dependent upon the load you're drawing on your buck.

**Chris Gammell:** Yeah, that's correct. Right. Exactly.

**Dave Jones:** So, it's going to change. So, the characteristics of your secondary flyback are going to change based on your load characteristic curve of your...

**Dave Jones:** ...buck.

**Chris Gammell:** Exactly. Buck. Yeah. If you had a circuit running off the primary, and then immediately that asks for like tons of current, right? And it basically changes the control algorithm within the chip, right? You know, there's... Yeah. Basically, there's always these feedback systems. It goes back in. The waveform changes. The switching time changes. Stuff like that. Yeah. That's definitely going to affect your secondary side because it's just along for the ride.

**Dave Jones:** Yeah, yeah. Exactly. But... So, if you're powering a microcontroller on your buck side that goes to sleep half the time... Yeah, I wouldn't do that. ...then it will, you know...

**Chris Gammell:** Yeah. That's a bad idea. Bad.

**Dave Jones:** And that you can tell just by looking at the schematic, you know? Yeah. Yeah. Like, you don't even have to read this stuff to sort of go, okay, that's how it must work, you know? Yeah.

**Chris Gammell:** Dave, if you've been doing it for 30, 20 years, 20 years or so, you know?

**Dave Jones:** Okay, right. Yeah. And they've got lots of big-ass equations in here and it's like, yeah, wank, wank, wank, well, I can tell from the schematic that you're going to have this issue and this issue. But I can see how it can be novel and lower your cost and you get that often because often you want that flyback secondary like for another, like a low-power split supply or something like that, you know? You might, you know, have to power a negative op-amp or something, you know? Something like that, maybe.

**Chris Gammell:** You mean because it's isolated and you tie it back in or something like that?

**Dave Jones:** Yeah, yeah. That'd be interesting. It's isolated. You can tie it back in. But there's other ways to do that as well. Yeah, you know, I always think about the isolated stuff.

**Chris Gammell:** I mean, like, I'm actually, I was always interested in that for, you know, just for sensitive circuits. You want to take your power off to a different ground, right? You want to be able to, and then you can pass your data back over.

**Dave Jones:** Well, isolated RS-232, isolated USB, that kind of thing. You know, you want to power the secondary side of the USB isolator or something like that. Yeah. You know, here's your ticket.

**Chris Gammell:** Yeah. Yeah, exactly.

**Dave Jones:** So, yeah. And usually they don't need much current. So, you know. Right.

**Chris Gammell:** Well, I don't know. Are you seeing more of that stuff as well? I mean, like, I, you know, I was always in the industrial sector. So, I think that's always an odd ecosystem.

**Dave Jones:** Are you asking if, if isolate is becoming more of a requirement?

**Chris Gammell:** Yeah. Yeah. I mean, are you seeing, are you seeing other people talk about isolated stuff more? I mean.

**Dave Jones:** Not really. No. It's always just been a requirement. If you need it, you need it. If you don't, you don't. I mean, I, I haven't seen any growth offhand. Okay. No. Yeah. I mean, it's, it's tough to say. I haven't seen more talk about it.

**Chris Gammell:** I was doing industrial mostly because that's a big, I mean, it was always big and industrial. Oh, yeah.

**Dave Jones:** Oh, grounding. Yeah. Yeah. Yeah. Exactly. Isolation and grounding and everything else is a huge deal. Yeah. You know, but in the electronics that most people are sort of used to, you know, the main place you're going to use isolated stuff like this is, as I said, like, you know, isolated USB product, you know, you, or something like that. You know, you have to isolate the ground between two systems, but you still need USB or serial connection between them or, you know. Right, right.

**Chris Gammell:** You pass data over an isolated interface as well. So, you need to power it. Yep. And you don't want to just plug in a wall ward for the isolated side. Yeah, yeah. So, yeah, no, definitely. Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** Anyway, it's a cool little part. I like it.

**Dave Jones:** Cool. It's that chip of the week. LM 5017.

**Chris Gammell:** Yeah, there's a couple of flavors of it, I think. But yeah, that's one of them. So, the 5017. It's always a good day.

**Dave Jones:** And they've given it a national part number, the LM.

**Chris Gammell:** I think it started with, I think it started before the demise of the integration. Sorry, TI. Right, okay. Integration into TI, so.

**Speaker ?:** Right.

**Chris Gammell:** Right.

**Dave Jones:** Well, I mean, they keep all that stuff. The assimilation, yeah.

**Chris Gammell:** They make new Burr-Brown part numbers too. I mean, you still can get OPAs. Yeah, yeah.

**Dave Jones:** See, I love Burr-Brown with the duck's guts in the day. I know. You know.

**Chris Gammell:** Oh, man. Yep.

**Dave Jones:** And I still call them Burr-Brown.

**Chris Gammell:** Oh, yeah. You have to. It shows you're in the know, right?

**Dave Jones:** That's right. Yeah, yeah. No, here's a little tip for you youngsters out there. Go to a job interview and throw Burr-Brown into the- Oh, man. Instant hire. You know, just drop names. Yeah, exactly. Totally. Oh, yeah. Heathkit, Burr-Brown. Yeah. You know. Those were the days. Radio Shack. You know, you're sitting there with your pimples on your face. Yeah, right, right. I remember. Skin shitless 20-year-old. Yeah. Yep. That's terrific. Yeah. What about the-

**Chris Gammell:** So, I posted about this a little earlier too. What do you think about schematic standards? Why aren't there schematic standards? In what way?

**Dave Jones:** You're talking file format? Oh, as in layout standards, as in how they actually look and function. Yeah, exactly.

**Chris Gammell:** So, the thing that prompted it was Jack Gansel's newsletter showed up, and he was talking about coding standards. And I started thinking about it. I'm like, well, why aren't there coding standards? Or, sorry, schematic standards. Why aren't we? We don't-

**Dave Jones:** Well, there are de facto standards.

**Chris Gammell:** Yeah, that's true.

**Dave Jones:** If you don't have your inputs on the left and your outputs on the right, you're a dickhead. Right?

**Chris Gammell:** I agree with that. But what about if you're in a culture that reads right to left? Right? I mean, like-

**Dave Jones:** Well, okay. Well, I don't know. Well, my teardown, Tuesday the other day. Okay. Yesterday, is it? Yeah. I released a video. I tore down a 1965 vintage power supply, right? And the schematic in there, we can link it in. Yeah. And it is, like, literally upside down and back to front. Like, it had negative at the top, positive at the bottom. Apparently, that's how they used to do it back in the pre, you know, in the valve days and, you know, and stuff like that. That's how they- Yeah, but modern-wise, it's like a pain in the arse. You can't read it because everything's upside down and back to front. You have to redraw the thing to make heads or tails of it.

**Speaker ?:** Huh.

**Chris Gammell:** Yeah. Yeah. Right, right, right. Actually, so that Wurlitzer schematic I was talking about, the Wurlitzer thing- Right. The standard on there, it had, for, like, large caps, it said 4.7 MFD and then just .001 with no unit. Yeah. And then it also said 100 PF.

**Dave Jones:** Yep.

**Chris Gammell:** And that confused the crap out of me.

**Dave Jones:** Back in those days. Yeah, I know. MFD, yes, is micro Farad. Yeah. It's a big M. Yeah. Yeah, this was in the power supply, too, like I showed. Oh, you did? Okay, I'll have to watch it. I didn't watch that. Yeah, a big 100 MFD on it. And back in the old, when I was a boy, MFD is, capital M is micro, right?

**Chris Gammell:** Yeah. That's odd.

**Dave Jones:** So, whereas a little M was milli, you know? And, of course, there was no such thing as nano back then. Why isn't capital M mega, right?

**Chris Gammell:** I mean, big M, I think mega.

**Dave Jones:** It is for resistors, but when you use it for capacitors, it's micro. Ain't y'all heard of Greek? Get with the program. Mew. Get with the program. When did that change?

**Chris Gammell:** I mean, you've been there. You've seen it. When did that change over? I mean, like, why?

**Dave Jones:** So, that actually was mid, by the 1980s, it was all micro, you know? It was micro everywhere.

**Chris Gammell:** Like micro using a mu, you mean? Like mu or you? A mu.

**Dave Jones:** Yeah, yeah, you or mu. Yeah, I mean, I'm okay with you.

**Chris Gammell:** I mean, I can figure out you is supposed to be mu. That's close enough, but like, yeah, M? Yeah, yeah, yeah, exactly. Well, and the other thing that was confusing to me there was 0.001, right? And it's like, okay, there's no label now.

**Dave Jones:** Oh, you wouldn't know it's even worse. In the specs, right? In the specs for this power supply, they had the drift spec, right? It was like, you know, 0.001% plus 100 capital M-V. 100 megavolts. You know? Exactly. Right? But no, it's not megavolts. It's not millivolts. It's microvolts.

**Chris Gammell:** Oh, no, they didn't.

**Dave Jones:** Yeah, they did. That's in the specs for this power supply. I kid you not.

**Chris Gammell:** Oh, that's terrible. Okay, so that brings me back to my question. Why aren't there schematic standards?

**Dave Jones:** Because everyone likes to do it their own way, and screw you. You know? You know? Well, there are, as I said, de facto standards, inputs on the left, you know, outputs on the right, positive on the top, negative rail on the bottom. And after that, it's a free-for-all. You know, like, some people just like to, you know, some people say, okay, a schematic should have a rail at the top and a rail at the bottom, and everything should connect to the rail. Okay? But some people don't like to do that. They like to use nets. Okay? Because they like to do multi-sheet schematics and things like that.

**Chris Gammell:** Okay, I mean, I get that people like stuff, but that's all well and good. I mean, I have an ego as well. I do it my way as well.

**Dave Jones:** Well, you start it, okay? Go on.

**Chris Gammell:** I think that's what I'm coming to, is like, why can't we have a standard, and then if it applies to it, you just say, this applies to the Chris Gammell standard 1.0. You know? Like, why has that never developed? Why is it?

**Dave Jones:** Well, there's such variability in schematics, and you don't want to waste space. Well, these days, who gives a crap? Well, if you told somebody how to lay out their board, right, you have to align, all the parts must be in alignment like this, right? They will tell you to piss off, right? Because it's not efficient. Layout, I wouldn't touch that with a 10-foot pole. No, it's a similar thing. It's a similar thing. There's so many variabilities in schematics, I don't think it's fair to enforce anything above, you know. You can have guidelines, like inputs on the left, outputs on the right, blah, blah, blah. But apart from that, no. No. But plead your case.

**Chris Gammell:** We're living in a civilized society here, Dave. Come on.

**Dave Jones:** Plead your case. Come on.

**Chris Gammell:** Well, okay, so what I think about is, so coding standards, right? Nobody likes coding standards, but what it all comes down to is that when, the reason you have them is that when you come up to a new piece of code. Sure. You know how to read it. You know what things mean. Okay. You know where to find the proper labels and definitions and stuff like that, and then the expectation is that that will carry along, and then everybody working on the project will eventually get there. That's the idea. I mean, like, everybody who adds anything to that. What?

**Dave Jones:** I'm in total agreement, but how many people follow the coding standards? Only when you're forced to at some big company, right? That's it. Otherwise, it's no. It's a free-for-all.

**Chris Gammell:** Yeah. Yeah. I mean, I guess it's a best practice, right? Yeah. No, and I mean, I made that argument, too, right? I mean, like, I think the best coders, right, probably follow their own coding standard, you know, a coding standard, or if they want to, they make up their own standard, right? But yeah, it definitely makes for, usually it's more people on the project requires that kind of thing, but I don't know.

**Dave Jones:** Oh, I won't name the company, but a company where that shall not be named, used to, if you came in and tried to follow coding standards, you were shot down. They said no. No comments, please. Don't put comments in your code. That's a waste of time.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Well, I don't know.

**Chris Gammell:** I guess I just wonder why you don't. So, right. Some people do it. Some people don't, right? But same thing for coding standards. Some people do it. Some people don't. And yet, the discussion's there for coding. It's not there for schematics. And that's really what it came down to.

**Dave Jones:** So, you think there should be a standard even if people don't follow it?

**Chris Gammell:** That's a good way to say it, right.

**Dave Jones:** Well, there probably is. If you look at, like, you know, anti-standards or mil-spec or Australian standards, even some old Australian standards, I think, might have some guidelines or something, perhaps. There's all these bizarre standards that nobody ever knows about or uses, but they're probably out there.

**Chris Gammell:** Okay. Okay. So, maybe I should look at it. And then I'll make the decision of, like, oh, hell no. I'm not following that. Right. Yeah, yeah. Exactly.

**Dave Jones:** So, if anyone does know, then please tell us. Yeah.

**Chris Gammell:** Some people posted this on the subreddit. And some people, let's see, someone posted links to, I don't know what those are. No, those are wiki pages. So, no one posted anything about that yet.

**Dave Jones:** Right.

**Chris Gammell:** Oh, someone said there's a good one in the art of engineering. And then someone else said that there's internal documents at companies. I mean, I get that, right? If you have a big company, you have multiple people. Yeah, yeah. I get that, but why hasn't that ever translated? Why isn't, you know, maybe it's just because hardware never really ever left the confines of the cinder block walls of engineering companies in the past, whereas code does. Maybe that's the difference. I don't know.

**Dave Jones:** Maybe because it doesn't matter a rat's ass. Maybe it's a pride of, you know, being an engineer that you're supposed to decode any schematic given. You know, it's like, I don't know. Like, there's standards for PCB layout because that's manufacturing, right? That, you know, like, things can go wrong and really ruin your day and waste money. But if a schematic's poorly laid out, who does it affect? Well, no one, really. It doesn't cost anyone anything.

**Chris Gammell:** Well, I'm usually the supporting engineer, which I've done.

**Dave Jones:** Right, yeah. But, you know, you can't go, oh, I can't make heads or tails of this. You can trace it out, right?

**Chris Gammell:** Right, yeah.

**Dave Jones:** You know, I mean.

**Chris Gammell:** Yeah, I don't know.

**Dave Jones:** It's just apathy. No one cares, right? Nobody's cared enough to define a standard for it, I guess. Or, as I say, there's so much variability, it probably doesn't make sense.

**Chris Gammell:** Yeah. Yeah. Well, I will, if people have examples, I would love to hear about them in the comments section. That's always a good place to drop them or, I don't know. We'll see. We'll see if anyone responds. We should probably wrap it up, though. We should. So, you have a couple weeks until Sydney Maker Faire, is that right?

**Dave Jones:** Yeah, not this weekend, but the next, I think it's the 15th or 16th or something like that. And my, yes, it is the 16th and the 17th.

**Chris Gammell:** Okay. And Dave is looking for help topics on his speech. Yes. My speech is one. Trends in hardware innovation.

**Dave Jones:** My fireside chat will be 1pm in the Target Theatre in the Powerhouse Museum on the Saturday, the 16th.

**Chris Gammell:** Yeah. Cool.

**Dave Jones:** There you go.

**Chris Gammell:** And I will be at DEF CON this weekend, and then there's the meetup next Thursday in San Francisco, if anybody's out there. And I will post link to that.

**Dave Jones:** And I have a stand again at the electronics show in September. Oh, yeah.

**Chris Gammell:** Right.

**Dave Jones:** Yep. I guess they didn't sell them all, so they decided to give me one again. Yeah. Excellent. So, yeah, I'm going to be on the stand all day. Yeah. Yep. And even she who must be obeyed agreed to come and man the stand. I won't say booth babe, but I couldn't, you know, I was met with a stern look when I said, can you wear a pair of hot pants? Oops, I'm in trouble. Just a little tip for people who have a significant other. Yeah, don't go suggesting that. It's usually not met with much enthusiasm. But, yeah, she will be there apparently. And, yeah, I might be selling stuff if I can get things together. So.

**Chris Gammell:** Look at that. The amp hour guys getting out in the world only took us four years, man.

**Dave Jones:** And I might have some exclusive merch there.

**Chris Gammell:** Nice. Nice.

**Dave Jones:** Which, yep. Yep. Free merch, like, you know. Like stickers and stuff. Exclusive giveaways and stuff like that. Oh, yeah. Yeah. So, yep.

**Chris Gammell:** Very nice.

**Dave Jones:** Excellent. So, be there or be square.

**Chris Gammell:** Cool, man. Well, let's talk more about it next week.

**Dave Jones:** All right. See ya. See ya.

**Speaker ?:** See ya. See ya. Outro Music
