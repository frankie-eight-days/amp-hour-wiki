---
episode: 226
title: An Interview with Colin Karpfinger - Blendling Bean Brio
url: https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/
---

**Chris Gammell:** This is The Amp Hour Podcast, recorded December 2nd, 2014. Episode 226, with guest Colin Karpfinger, Blendling Bean Rio.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Contextual Electronics.

**Colin:** And I'm Colin, the founder of Punch Through.

**Dave Jones:** Hey, Colin. Thanks for joining us.

**Colin:** Welcome, Colin. Yeah, happy to be here.

**Dave Jones:** From sunny San Fran.

**Colin:** Rainy San Francisco today. Yeah, out of the ordinary.

**Dave Jones:** Right. But Chris was just cheering that you were from the Midwest.

**Colin:** Yeah, yeah. I grew up in Milwaukee, Wisconsin, actually.

**Dave Jones:** Milwaukee?

**Colin:** Yes.

**Dave Jones:** The only thing I know about that is from Happy Days. Sorry.

**Colin:** We have a lot of beer. A lot of beer. That's pretty much Milwaukee's claim to fame.

**Dave Jones:** Right. And a giant-ass lake up there somewhere.

**Colin:** Yes, yes. A lot of giant-ass lakes.

**Dave Jones:** So you moved to where all the action is?

**Colin:** I did. Yeah. I actually went to school in Minneapolis, which is where our other office is. We have an office in Minneapolis and San Francisco. And then I actually moved to San Francisco about four years ago. So I've been here for a little bit of time now.

**Dave Jones:** But you did start the business where you went to school and grew up?

**Colin:** Yep. Yeah, I started it while I was going to school there. So I just kind of did a little bit of consulting when I had time and it kind of grew. And one summer I kind of spent the whole summer doing consulting and it was just – I really loved it.

**Dave Jones:** All right. So tell us about the Light Blue Bean, which is your main product.

**Colin:** Yeah, yeah, the bean. So I guess at a high level it's a great Bluetooth development board and it's Arduino compatible. So you can kind of write Arduino code to do a lot of Bluetooth low-energy things like be an iBeacon or kind of read and write sensors. And really the most unique part of it is that it has no connectors. So there's no way – you actually can't plug it in. It's entirely wireless. So you can actually program it over BLE.

**Dave Jones:** Cool. Then how do you connect stuff? It's got no connectors.

**Colin:** Oh, it has – so it has eight points that you can solder. It's kind of like a proto-board. You can solder things to. Yeah. So it has, yeah, GPIO and two analog IO and, yeah, so kind of the typical Arduino inputs. But then, you know, to your phone or computer it's all Bluetooth.

**Dave Jones:** And it runs a coin cell battery.

**Colin:** Yes. Yep.

**Dave Jones:** How do you get – what sort of life you get in from an Arduino – I assume you're not running the Arduino at full speed. Are you running it at a slower speed to get the battery life?

**Colin:** Good question. So we run it at eight megahertz, which is kind of typical. But we also have a lot of function calls and we put a lot of thought into putting the system to sleep. Got it.

**Dave Jones:** Yep.

**Colin:** Yeah.

**Dave Jones:** So you don't run the stock standard Arduino, you know, code.

**Colin:** Pretty much. I guess. Yeah.

**Dave Jones:** Because that just runs full pelt, doesn't it?

**Colin:** Yeah. Exactly. Yeah. So you find very quickly that you have to use, you know, bean.sleep instead of wait in your sketches. Ah, got it. Yeah.

**Dave Jones:** Yep.

**Colin:** Yeah. And it is funny, like, you know, now power is so important that, yeah, running your, you know, at mega going a few milliamps is just terrible. So, yeah, we've kind of designed the whole system to be low power so you actually can run on a coin cell.

**Dave Jones:** Any thought about actually ditching the Arduino? Because it's not the lowest power environment. Any thought about coming up with a product that is super ultra low power, you know, using like an MSP 430 or a Gecko or something like that?

**Colin:** Yeah. That's a really good question, too. And we've developed a lot of…

**Dave Jones:** That's what we do here on the Amp Hour. We ask good questions.

**Colin:** Man, you guys are smart.

**Dave Jones:** At least we think we might.

**Colin:** Sure. Yeah. So…

**Dave Jones:** It's the illusion.

**Colin:** So we've done a lot of development with these other platforms that are low power. And the reason we chose to stick with the AppMega and kind of standard Arduino experience is just so that people who've already written code for these Arduino platforms can just use the Bean, you know, without having to change anything. So it gives you this vanilla experience, which is actually pretty cool because if you consider that, you know, you're adding all this Bluetooth flow energy stuff. But really it feels just as if you're using, you know, your typical Arduino.

**Dave Jones:** Right.

**Colin:** Yeah. And we actually, you know, we designed the system so that the… It actually has our other product on the Bean, which is the Bluetooth module. It's the LBM 313 module.

**Dave Jones:** Oh, okay. Yep. I've seen that. Yeah.

**Colin:** Yeah. Yeah. Yeah. And so that both kind of processors, the module and the AppMega can put each other to sleep. And so you can have, you know, the module kind of forcibly tell the Arduino to go to sleep or you can have the user code kind of say, hey, the user requested that we go to sleep. Let's, you know, turn off.

**Dave Jones:** Right. Because you might only have to like, you might have an app where you only have to transmit once every, like a single packet every hour or something like that. Right. But the micro has to run all the time or, you know, vice versa.

**Colin:** Right. So, yeah. So in sketches where people are doing kind of data collection, the AppMega stays asleep, you know, like you said, for an hour or something like that. And then the module kind of handles the connection to the iPhone and keeps that established.

**Dave Jones:** So this module you've got, this Bluetooth module, it's FCC certified. How much grief did you have to go to get an FCC for?

**Colin:** Yeah.

**Dave Jones:** There's that laugh of a, yeah, like I spent all my life doing that. Right.

**Colin:** A lot of gray hair now at the age of 27. No. You know, we actually, I'd say we lucked out in that we had, we worked with a company in the Bay Area and they actually had, some of their techs were really good. They're really not only smart people but also, you know, kind of a pleasure to talk to and be around which is not the typical experience I'd say. Right. So that made it a lot better. It's always kind of a pain, you know, pain in the ass. But we've done it several times. So we kind of understand it.

**Chris Gammell:** Does that mean that you had to, you had to like start over? Is that the several times or is this part of the consulting work? Is that the several times?

**Colin:** Yeah, part of the consulting work. Yeah. Yeah. And actually, so the only thing that appeared that we failed on was when one of the test lab employees started classifying it as a Wi-Fi transmitter in one section of the test. And we just had no idea what he was asking about. What? I'm like, you know, I searched the entire Bluetooth spec for this term that you're asking about and I can't find it. Like I have no idea what you're asking me. And, you know, it's almost like you ask these questions and it feels like either I'm going to be a total idiot and he's going to point out something that I just never knew or it turns out that he's trying to classify it as a Wi-Fi transmitter, transceiver.

**Dave Jones:** Ultimately, how much time and money did it, if you want to talk money, how much time and money did it cost roughly to get a module like this certified?

**Colin:** Yeah. Yeah. So.

**Dave Jones:** Ballpark.

**Colin:** It actually, the module actually has FCC, IC, CE, which is for Europe and Canada. And then we're actually working on KCC and MIC, which is for Korea and Japan. Oh, okay. Yeah. So all of those, what we generally say, you know, if you're comparing the development path of going chip down versus a module, we usually say that it costs about $40,000 and about, you know, two to three months to go through the certification for all that. Excellent ballpark.

**Dave Jones:** For those who want to.

**Colin:** And it'll vary based on your test house.

**Chris Gammell:** Sometimes you should just buy the module, folks.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Just grin and bear it and hope Colin gives you a good price. Right.

**Dave Jones:** Well, was that an option? Was that a design option? When did you think, oh, look, bugger it. Why do I own? There's companies out there that sell Bluetooth LE modules. Yes.

**Colin:** Yeah. We actually.

**Dave Jones:** Is it a price competitive thing?

**Colin:** Yeah. So part of our, you know, initial kind of product plan was actually for two parts. So, you know, we, a lot of our customers build things that are very small and price competitive in the market. And so we needed also a low cost solution for them. Um, so by kind of having these two products, the, the LBM three and three module and the bean, we're able to kind of cover both the, you know, uh, tens of thousands scale and the one scale. Um, so it was kind of a, we kind of planned on it from the beginning.

**Chris Gammell:** I really like it actually, because it's, uh, you know, it's, it's like taking, taking a consulting business, right? So, I mean, you started as a consultant and taking that consulting business and basically productizing it because it's like, you know, you're going to have people coming to you a lot and be like, I want a Bluetooth device. I want a Bluetooth device. And now you basically say to them, well, you can't afford me, nor can you afford to spend something totally custom, but how about you put in this thing that we designed and we can sell you for, you know, what is it?

**Speaker ?:** What is it?

**Chris Gammell:** What is it?

**Dave Jones:** What is the, what is the, what is the 100,000 units?

**Chris Gammell:** Yeah. Sorry. Sorry. What did, uh, what did you ask? I'm sorry. The, the, what is, what is the bean retail for? Like I, we're actually, I mean, yeah, the module is $30.

**Colin:** The bean is $30, um, you know, getting down to about 26 in higher quantity. And then, um, the module is anywhere between eight, like seven, seven, uh, 80 and $10, depending on your scale.

**Dave Jones:** How are you staying in business selling sub $10 modules? You still doing consulting work?

**Colin:** You got to sell a lot of them. Um, yeah. You're right. Volume.

**Dave Jones:** That's how we make it.

**Colin:** Like you were saying, uh, you know, when we launched the products, we already had a bunch of customers, um, in our consulting customers. Um, and so we kind of knew what they wanted. We knew what they were looking for. So it made it just like you said, you know, we're, um, since we're a mostly self-funded company, we can't, uh, or rather it was not as big of a risk because we knew that there is a demand for this kind of thing.

**Chris Gammell:** I mean, yeah, basically you're designing your toolbox, right? I mean, that's the main thing.

**Dave Jones:** Yeah. So you didn't just have this great idea and go, Oh, look, we'll go out and find a customer.

**Colin:** Right.

**Dave Jones:** Which can fail miserably.

**Colin:** Yeah. Yeah. Got to know there's customer first.

**Dave Jones:** Product names. You've got the light blue bean. Cool name. The development board is the Vegas lounge.

**Colin:** Yep.

**Dave Jones:** Okay. I, I guess there's a story behind that. You wouldn't call your bloody module the LBM 313.

**Colin:** Well, the LBM actually comes from light blue module. So, so light blue is kind of our Bluetooth energy product suite. Um, and we actually have an app on the app store called light blue, which is like a general purpose, uh, test tool for anyone, you know, wanting to test their Bluetooth, um, products. Right. Um, yeah, so that's, that's the idea with that Vegas lounge is a story. Uh, so at some point, uh, we decided that we wanted to name products, uh, and or revisions off of establishments that the punch through team, uh, frequents. And one of those is, uh, this terrible karaoke bar in Minneapolis that I don't think any of us actually go to, but had a great name. So if you're in Minneapolis, I think it's in Northeast Minneapolis. You can, uh, go check out our office and then drive over to the Vegas lounge.

**Chris Gammell:** Go there before the guys do.

**Colin:** Yeah. Yeah. It's actually funny, you know, going through all this FCC testing and everything, you were sending documentation around and, you know, typically these, typically the boards are called. It's called something like, you know, alpha one or something. And ours are like, right. Lounge and the, uh, the techs are laughing at it. And yeah, but it's, it's good. It's memorable. People definitely remember it. It's cool.

**Chris Gammell:** I like it. So what do you use the Vegas lounge for?

**Colin:** Yeah. Good question. The Vegas lounge is, um, the, uh, it's kind of a full feature development board for the module. So it really breaks out everything that you could use on the module. Um, so it's, you know, whereas the bean is like an easy, entry point that gives you like, uh, a feature set that's easy to understand. The Vegas lounge is like, you can, you can test anything on the module with, with this dev board. Okay. Cool. Cool.

**Dave Jones:** So you can actually hack in there, measure supply current and do all that sort of jazz.

**Colin:** Yeah. It actually has a current, uh,

**Dave Jones:** Oh, it does have a current sensor on there.

**Colin:** Yeah. Nice.

**Dave Jones:** Thought of everything.

**Colin:** Yeah. That's another big one. I mean, you know, we used a lot of dev tools from these semiconductor companies. And, uh, as you probably know, they're often terrible. Um, so we, we, you know, took a lot of what we didn't like about others and, uh, made one that we did like. Yep.

**Chris Gammell:** I was actually pretty surprised about the, on the bean. So like I started, so I have one. Uh, I don't think Dave, you don't, you haven't had a chance to play with one yet. Right.

**Dave Jones:** I do not have a bean. No, I'm beanless.

**Chris Gammell:** I'm beanless. Uh, but I was surprised that there's the accelerometer on board. There's, you know, like, and like just stuff that's like, Oh yeah, of course, of course you put that on there. You know, tri-color LED, that kind of thing. And it's just like, but I didn't think about any of this stuff. And then that kind of just leads right into some of these, the starter applications, especially stuff that, you know, might not be on like a lot of the, the beginner Arduino type stuff. So what was the, what was the real thing behind the putting an accelerometer on there as well?

**Colin:** Yeah, we, um, you know, we, we saw a lot of, uh, applications where, um, you could do a lot with a small amount of hardware and the, you know, the cost added for putting something like that on the board is not terribly high. Um, so we wanted to give you something that out of the box you could do a lot of, um, stuff with, you know, and a lot of, um, kind of now you have more software developers getting into hardware and it's really exciting for them to be able to take the bean and, you know, make something right away without having to solder or, um, you know, build any hardware necessarily. Um, so, you know, you can make a motion detector and kind of control something with the gestures and, uh, just right out of the box.

**Chris Gammell:** Cool. Yeah. I saw, and I saw your videos. Some of you guys had that video of you guys like running around your beach house, which was a little campy, uh, the one where you, you tack the, uh, the accelerometer to the toilet seat and then, uh, or sorry, you tack the bean to the toilet seat and hopefully you never reuse it for anything else. Uh, yeah, that one didn't ship out to anyone. Right. Yeah. And what have you got that in your, in your backing of the, of our crowdfunding campaign, right? Lucky winner. Yeah.

**Dave Jones:** So tell us about the crowdfunding campaign. Cause you didn't use Kickstarter or Indiegogo. You rolled your own.

**Colin:** Right. Yeah. Um, yeah, we wanted to try a couple new things and we didn't see anything out there that really let us do that. Um, and so, you know, a lot of people think, uh, we kind of did that to save on, save money, uh, which really wasn't the case. I think, you know, what Kickstarter and Indiegogo take is fair, but, um, we mainly the, the driver was, uh, we had this idea to drive sales where the first day of the campaign, the bean would sell for $18 and then it would kind of go up every day a little bit, uh, and then get, uh, 24, which is like 20% off, I think. Um, yeah. And so it would say, you go to the site and it would show you the price today and the price tomorrow. And, uh, we were, you know, thinking that that gives you a sense of urgency that you should just buy it now.

**Dave Jones:** Right.

**Colin:** Um, and did it work? It, it worked. Um, you know, I wish we could have a sample of, of not doing that, uh, to, to really compare, but our first day was huge, you know, like I think probably 60% of our sales came on the first day. So.

**Dave Jones:** Nice. And how did you get that? Did you get blogged somewhere? Yeah. How did you get the publicity?

**Colin:** Yeah. We, um, you know, we just kind of put it out there as much as we could with any contacts. We had, um, and we actually offered, uh, a lot of blogs, a one hour exclusive window, uh, to kind of launch with it before anyone else could, um, make magazine took us up on that. And so, so they were ready to go, uh, at nine. Bingo.

**Dave Jones:** There's the, there's the huge audience right away.

**Colin:** Yeah. And then I think Gizmodo covered it later that day and that was huge. Um, yeah. Checkmate. Yeah. Yeah.

**Dave Jones:** So how many did you sell and how much money did you raise?

**Colin:** Yeah. We sold, uh, I think we raised almost $200,000, um, and we sold, uh, somewhere around 8,000 units, 9,000 units. Wow. Um, and actually, you know, part of the reason I think that we're able to do that, um, we, we put a lot of thought into, uh, upselling people to four units. Um, so the, you know, the business is cool. You can, since you don't have to plug it in, you can kind of build it into whatever you're making and you don't have to take it out if you want to change something. Um, so there actually is a reason to have more than one. Um, but we, you know, we kind of structured the buy page to, to kind of, you know, uh, Right.

**Dave Jones:** Entice them up the, yep. Yeah. Yeah.

**Colin:** And you got a free, you got a free kit of sensors and stuff. If you bought four. I got it.

**Dave Jones:** If you bought four. Yeah.

**Colin:** Right.

**Dave Jones:** Yep.

**Chris Gammell:** I actually really liked that too, because in the, in the software dialogue, obviously that becomes a very big issue really quickly too, right? If you have, you turn on, you know, these things are always on, right? I mean, they're, they're turned on by software. Um, but if you had 10 of them in a room, well now you're, you don't get to see which cable you're plugged into. So there's just a function on there that says identify. And then that one actually lights up. And I, I, I know, I know it's been years for me, right? I mean, I know it's been years with electronics, but like, even I think, I think because it's wireless and because it was, you know, I put it across the room and just clicking the identify, like that was even a little bit more magical than the, you know, the, the Arduino blink contest, right? Because it's like, Oh crap, this is magic. Yeah. Obviously. Yes. I understand RF, blah, blah, blah. I get it. Right. I know, I know, I know software stacks and stuff like that, but like, yeah, something about it still does it for me. I'm glad you appreciate that. Yeah. Yeah. That's cool.

**Colin:** The other, the other one kind of like that, um, that we built in is, um, if you downloaded our app before you received your, your bean, um, when it actually got within range since the battery, you know, we ship with a battery already in the unit. Um, when the FedEx or UPS guy or whatever got to your front door and it was within range, your phone would actually pop up a notification. Uh, so yeah. So that was cool. And you know, we were trying to say like, it's, you know, so easy. You can use it without even opening the box. And, um, so that, that was cool. A lot of people liked that. A lot of people tweeted that right away and that was really rewarding to see.

**Dave Jones:** Pretty sweet.

**Colin:** Yeah.

**Dave Jones:** So how was the, um, how was the ID done in these things? How was each unit, um, ID'd and given a serial number?

**Colin:** Yeah.

**Dave Jones:** How does that work?

**Colin:** Yeah. Um, for the user, it's generally done by name. Um, so like in the loader, you can, the loader app is, you know, the app that runs on the Mac or, uh, the iPhone or iPad or whatever. Um, and you can rename them to whatever you want. And then that's, you know, you can sort them based on signal strength and see the name. Um, and then as far as.

**Dave Jones:** But how do you do that when you've ordered 10 boards and you've got 10 boards sitting there?

**Colin:** Yeah. Um, so you can.

**Dave Jones:** All running and with their battery.

**Colin:** Yeah. Right. You can write, um, so in one situation where the beans are acting as like an eye beacon or a beacon, you can actually assign them specific IDs. Um, and so that's one way. And then, uh, you know, there's a, there's a profile, um, on the bean that allows you to kind of only see devices that are beans, but then to go kind of to find an individual one, um, you can either change the name or add a little bit of data to the advertising packet. Um, but generally, you know, generally we just wanted to, uh, we didn't want users to like get into the state where they couldn't see them anymore. And so it's generally done based on name.

**Chris Gammell:** So what about do, do these kinds of devices? Uh, I know that like a lot of the, um, often you need to have like a unique ID chips on like, like ethernet devices. Do these have built in unique IDs on, on the Bluetooth chip or how does that work?

**Colin:** It's a, yeah. Um, so they, it's a tough, it's a tough question. And part of the reason that stuff is that, uh, Apple actually salt, uh, I guess the, the ID and so salt, like, yeah, so they ruin it. They like change. Yeah. They make it, yeah, it tastes better. Um, they change the ID so that you can't really track, you couldn't track anyone based on their Fitbit or something like that. Oh. So it's like a security choice that they made, uh, you know, and maybe I'll talk about later each, each like, you know, mobile OS vendor has their own kind of style of, of stack where they change some things around. And this is the one that Apple, um, changed that, uh, you know, it's good, it's good for the users, but it's sometimes it's frustrating for the developers.

**Chris Gammell:** So they were doing this while they, uh, forgot to update the security on iCloud basically. They were salting IDs. Yeah. Yeah. Sorry. I couldn't resist. Preoccupied with that. Yeah. That's, uh, uh, that's, that's weird. And that probably would get really frustrating for like, cause then, so how do you guys actually go and you just kind of just pick them randomly then? And you just say, whatever this idea is, you just hope it stays unique or what?

**Colin:** Um, no, so the, you know, what the, um, the thing that won't change is kind of the, um, the profile of the bean. So like our apps can tell which Bluetooth, uh, smart devices are beans. Um, and that's always going to, you know, be the same, but, uh, generally, you know, it's harder to know exactly which, which specific bean is yours. And, uh, the solution to that is kind of adding something, you know, in the pro and the application layer. So you can, um, you can, you know, set an ID and, uh, we actually have on, on the module, there's a serial number that's burned into it. Um, and that's, that's pretty much unique.

**Chris Gammell:** Okay. Yeah. All right. That's good. Oh yeah. I see it here now. I guess that's the second line there. Yeah. I won't read mine on air. Yep. When you guys are handling that kind of stuff then, so does that mean like on the, on the Apple side of things you, because you're using their, their Bluetooth stack that basically you kind of just have to take whatever they're spitting out there? Is it kind of the idea?

**Colin:** Yes. Yes. Um, but you know, I'll say that actually, um, there is a, a vast change in kind of Apple's policy towards external hardware for the better, um, with Bluetooth flow energy. So that's when, when punch through started, uh, I was developing a lot of products, um, for the iPhone, but they'd have to plug in. So they had to go through this separate program called, uh, made for iPod or made for iPhone MFI. Uh, and anyone who had to go through that kind of shares the same badge of honor of how terrible it was. Um, and we really, we actually sold our services based on, Hey, we've done this, you know, for a 10 or so products. We know how to do it. Don't worry. We'll, we'll help you get through it. Uh, and I remember thinking like, you know, maybe someday Apple will change this. And, uh, I didn't have more faith in that, but with Bluetooth, Bluetooth for Bluetooth energy, whatever you want to call it, um, you don't have to go through that same hardware approval process. And so, you know, you set up to get approved and in the most extreme situation, they'll ask you for a video of your hardware working with the app, um, which is worlds different than to be.

**Dave Jones:** Why are they such a pain in the ass?

**Colin:** I mean, there are a lot of people wondering that same thing.

**Dave Jones:** Actually, but is it like, can you, at the end of it, did you kind of go, Oh yeah, I can kind of see why they're being such a pain in the ass now, or do you still not get it?

**Colin:** I, I still don't get it. Um, get it right. I, you know, I think part of it was if you have things plugging into the iPhone, you're really, you really have a chance to change the user experience of the phone. You know, like if something is drawing too much current from the phone, it's going to kill the battery and users will complain about that. Or maybe, you know, it'll change the, uh, antenna characteristics of the cell antenna and people will complain about that. So there's definitely reasons for it. Um, but you know, I, I think, you know, promoting this of, of accessories to work with mobile phones is pretty important. So they finally kind of changed their tune on that.

**Dave Jones:** And how did you go shipping your 8,000 odd products? Any dramas?

**Colin:** Um, as far as the good stories, uh, we had one, we had one catch that we, we, you know, right before a manufacturer, uh, in Korea started fabbing 8,000 boards. Uh, we figured out that, um, basically the way we expected to wake up the module in hardware wasn't going to work. And so we had to, you know, do this really scary thing of getting them on Skype saying, stop, stop, stop. And then figuring out exactly how far they had gotten. Um, and there's these weird situations where like they may have etched, you know, the bottom and not the top. And you may be able to get some really crazy, uh, solution in there by moving just one layer. But thank God, you know, they hadn't started, uh, the boards yet. And so we were able to change it. Um, so they all, they all went out there, you know, no, no problems there. Uh, and we, we used a fulfillment center here in the Bay area, um, to do that. So we, you know, yeah, we shipped all the units over there and then we actually went and toured, toured the place mostly just to see what 8,000, uh, beans would look like. And, uh, you know, it's, it's funny with stuff. I was expecting, it's almost like you're expecting this giant, you know, pallet stacked to the ceiling of boxes and they're pretty small. Yeah. So it was so cool.

**Dave Jones:** So was that a worthwhile experience using a, uh, using such a, uh, company or did it, you know, eat hugely into your profit? No margin.

**Colin:** No, I'm very happy that we did it. Um, you know, for, for a small company, I think it's, we're not good at shipping, you know, I think.

**Dave Jones:** Well, especially that sort of volume, like if it was a couple of hundred, you could do it yourself. Right. You know, it's not a, it's not a drama, you know, you can slap on labels. Right. You know, wander down to the post office, but yeah.

**Colin:** Yeah.

**Dave Jones:** 8,000 is a bit much.

**Colin:** No, I remember, um, you know, doing some, some previous things and always thinking like, oh, it'll be, it'll be fine to kind of, you know, build or ship or whatever the first, first thousand or so. But no, I'm, I think it's great to use fulfillment center and kind of be ready for the next, uh, you know, tier.

**Dave Jones:** Right. But apart from that, you pretty much handled it all yourself in terms of like, like, did you, uh, buy, like it wasn't a turnkey solution. Like one company just handled purchasing, manufacturing, testing, shipping. This is what they do for a living, Dave. Come on, man.

**Chris Gammell:** Yeah. They're consultants. They consulted for themselves.

**Colin:** Exactly right.

**Dave Jones:** So what, what aspects did you guys do yourself? Did you, you know, did you buy your own parts and then ship them to the assemblers? Yeah.

**Colin:** Did you, we, um, we basically did everything, um, besides the component purchasing and the assembly and test. Um, but we, you know, we designed the, uh, kind of test procedure, which I'd say is like a big task that a lot of people, uh, leave out or, you know, don't expect to be. Oh yeah. It's no task. Um, so we, you know, we did all that. We worked with our, our manufacturer to create this cool test jig. I think it tests, um, I think there's like nine beans on one panel that come out from the assembly line and then it, it actually tests all of them in one, uh, one jig. So we, um, we have some cool videos of that and stuff, but.

**Dave Jones:** Are those up on public?

**Colin:** Can we have a look at those? Yeah, they are. Um, I believe we sent those out to one of our backer updates, uh, but they're probably on our Vimeo channel. Um, if you just go to vimeo.com front slash punch through, it should all be there.

**Dave Jones:** Right. Because I'm sure there's a lot of people who want to know the, you know, love seeing that sort of thing. Want to know the ins and outs of how do your production test something?

**Colin:** Yeah.

**Dave Jones:** You know, cause it's, um, because if you haven't done it before, like you'll have no clue. Right. You know, of, of the best way to do it or even the different methods to do it. Right.

**Colin:** And I would even say, um, you know, understanding how the manufacturer wants to do is important because like these guys don't have iPhones a lot of the time, you know, and, um, one of the previous products I worked on, uh, was this air guitar controller for the iPhone that had an accelerometer in it. You could kind of play air guitar on your, with your phone. And, uh, we made this great test app that was on an iPod touch and we had to supply iPod touches to everyone in the factory.

**Dave Jones:** Uh, but we did some cool things.

**Colin:** Like, you know, you, you would, um, it would actually time you testing each unit and then you could get like a high score and put your name in and stuff. So we tried to gamify our testing.

**Chris Gammell:** I don't think anyone, we didn't fool anyone, but. I'm just imagining this button down like test lab where then like you walk, you turn a corner and there's like, you know, this gray haired dude just like wailing on an air guitar type of thing, you know? Yeah, pretty much. No, I'm testing. I'm testing. Go away. Yeah.

**Colin:** Well, we had to test each axis of the accelerometer because, uh, we had this bug where they were joining the plastic pieces with ultrasonic welding. And I learned that that's terrible for MEMS accelerometer. It's like, it'll sometimes stick on one axis. And so, yeah, the test, you would just have to rotate it to the positive and negative, you know, uh, ends of each axis. And then when you got to the end and it had passed, uh, an image on the screen switched to Homer Simpson and it had his voice going like, woohoo. So we had all these people on the assembly line, uh, going through this thing and then Homer Simpson popping up. And I don't know. I don't know. Who knows how much that translated.

**Chris Gammell:** That's cute the first time, man.

**Colin:** Yeah, exactly.

**Dave Jones:** No, there's, if you've ever worked in a production facility and it like, and it goes beep, just going beep every time it passes a test, it just, it just gets on your nerves, you know, after the 10,000th year.

**Colin:** So we were actually torturing these, these poor assemblers with Homer Simpson.

**Chris Gammell:** Yeah. We used to have these, these etch machines at Samsung that would play like tunes when you're done, but like, you know, you hear for release on a chip tune, like, you know, eight to 10 hours a day. You just want to shoot yourself, you know, or shoot Beethoven, you know, couldn't have been a little shorter. Yeah. Right. Exactly. So, um, so on the manufacturing side of things, I'm curious. So the, the actual module that's, that's separately manufactured from the bean, correct? Correct. So what, what are some of the challenges with, I mean, cause this is like a super thin board. I've seen these kind of, these type of modules before, you know, with the metal can. Sorry. So people that hasn't, haven't seen it will have pictures obviously, but you know, there's a metal can. It's, it looks like a, you know, uh, what maybe the 20 mil board or something like that. And then a balance on there. I mean, so what's, what's the hard part about that stuff?

**Colin:** Um, I'd say the hard part, uh, kind of, I would say generally the RF. You know, the RF characteristics, that's, that's the harder part. Um, just because it requires some really expensive tools. And, uh, you know, as everyone always says, it's kind of like a black magic thing. Like you don't, you don't really, there's so many parameters to the equations going into the, how it performs that you're really just, you're tweaking, you know, tweaking things and trying to get, uh, you know, the impedance to match. And so that, that's interesting. Um, but it wasn't, it wasn't too, too bad. I'd say, uh, yeah. Yeah. Generally the RF stuff.

**Chris Gammell:** I guess. Yeah. I, I look at this, I mean, mostly cause I'm looking at it and the only real components that are showing outside the metal can, I'm not going to pop the can off this obviously, but are like 0201 and for maybe smaller, I can't tell. Yeah. But you know, just like, I'm not used to that small either. Yeah, totally.

**Colin:** And actually it's funny, the first, um, the first few revs of the board, or maybe it's just the first rev we assembled ourselves here in our office. And, uh, you know, if, if you've ever complained about 0603, just try 0201 for a couple of boards and you won't complain anymore. We're going to need a bigger microscope. Yeah. Yeah. So, and it's funny, our first, our first iteration of the module, um, we, uh, we finished right before this company trip. So every, every year, all of us, uh, we rented a house somewhere in California and everyone comes out from Minneapolis or San Francisco and we just kind of hack on some stuff for a week. And, uh, we had just finished like the first rev of our module and the first dev board right before this trip. So we're, you know, we think we're all ready. And, uh, we get down there and within the first day found a bug that, uh, killed three out of the four boards. Um, so, and those, and we actually, you know, we hand soldered all the modules. We had hand started the modules to the board and, oh, it was, it was terrible. But, uh, now, now that they're, you know, assembled by professionals and, uh, you have this nice thing like the bean to use. It's a lot nicer.

**Dave Jones:** So how do you connect up to these things? You've got a bunch of square pads on the bottom, which I originally thought were, oh, okay, there for production testing or something, but that looks like the only IO on the thing.

**Colin:** Yep. That's how you, um, that's how you attach it to your board. So it's really optimized for size, you know? So, um, by putting the pads underneath.

**Dave Jones:** So you just reflow square pads. So they're not like a ball array. Right. It's not like a ball based system. It's just square pads. Then you just put the solder paste down and it reflows. Yep. Yeah. This is on the module you're talking about, Dave? Sorry. The module. Yeah. Yeah. Yeah. Yeah. Yeah. Sorry. Yes. Yes. This is the module.

**Colin:** So we're able to actually do it. Um, you know, hobbies can do it with a hot plate or a, a toaster oven or what have you, but, um, yeah, it's a little harder to inspect, you know, cause you obviously you can't see underneath it.

**Dave Jones:** Well, it's practically impossible to inspect. Yes.

**Colin:** Yes.

**Dave Jones:** Unless you've got an x-ray machine.

**Colin:** Right. So we've, we've done that in a few cases, but generally, you know, when you get the profile right and, uh, in production, it's not a problem.

**Dave Jones:** And of course.

**Colin:** Yeah.

**Dave Jones:** So any thought given at the time to doing the, uh, half moon, uh, pads around the edge.

**Colin:** That's what we did initially. Um, our first, yeah. Our first prototypes used that, um, basically we just wanted to get it smaller, uh, and be able to break out more, more pads.

**Chris Gammell:** Got it. When you, when you were designing the pad layout for that kind of thing too, is what kind of, what kind of considerations go into that? Cause I've, I mean, I've never done anything like that where it's a module with the pads underneath. I mean, are there, is it basically just to get the pads as spread as possible or, or does not even matter because there's so few IO kind of thing?

**Colin:** It's kind of an optimization between, um, you know, having enough room to route out all the traces. Um, so like we are, you know, on our site, we have a couple example escape, you know, patterns, um, that don't require any special PCB technology. Um, so it's just, just between that and, you know, having a decent sized pads that, uh, will be reliably soldered.

**Dave Jones:** But it means you've got to have a four layer board pretty much minimum with this, wouldn't it? I can't, you're like at least, oh no, no, you can route out two traces between pads, I'm guessing.

**Colin:** Yeah. Yep. You can actually do a two layer board.

**Dave Jones:** Okay. Cool.

**Chris Gammell:** Yep. Yeah. Any problems with, uh, like if, if someone stuck this down to, uh, a two layer board and a product they wanted to make, and then, you know, they had to go through the, what's that one that don't, you still have to do some, the non, uh, non-intentional emitter type stuff, right?

**Colin:** Yeah.

**Chris Gammell:** Yeah.

**Colin:** You kind of have to do the end product, uh, approval, which is much faster and cheaper, but yeah. No, I, um, the bean is actually a two layer board. Oh, okay. That's good. Yeah. It's made to be kind of cost optimized.

**Dave Jones:** And are we allowed to say what sort of Bluetooth chipset you're using in there?

**Colin:** Yeah. It uses the TI. Or is that secret sauce? Nope. Nope. It's actually in, uh, it's in the part number of the Bluetooth. Oh, okay. All right. So 2540. Yep. Exactly.

**Dave Jones:** Oh, okay. Yep.

**Chris Gammell:** That was a good chipset. And that's, uh, that's the, so that's got what, like an 8051 on board or something like that? Yeah.

**Colin:** Yep. So it's just a really low power 8051. And, uh, yeah, it's, it's kind of the most production ready part. Um, as far as like BLE, uh, um, um, components with, with also a processor on board.

**Chris Gammell:** Yeah. And there's a, there's a couple out there, right? I mean, cause there's, there's other chipsets that do BLE, but it's just about the, what's, what was available. And I mean, how long ago did you guys start this kind of thing? Cause I remember, I think I got a dev kit a couple of years ago, but I never did anything with it.

**Colin:** Yeah. TI came out with it a couple of years ago. Um, and really a lot of our BLE stuff kind of started when we got the dev kit and there was no, you know, no app on the app store to test it out. The dev kit didn't come with any firmware. And so that was kind of one of the things that kind of, uh, made us think like, Hey, there's, there's an opportunity for some better tools here. Um, yeah. And so there's, there's a couple others on the market. Um, yeah, it's still, it's still kind of in a lot of the, uh, production, uh, a lot of the products out there and, um, it's pretty, pretty power efficient compared to other parts.

**Dave Jones:** Have you had any supply issues with either the TI chip or the Arduino chip? Cause I know there are supply issues with the Atmel's.

**Colin:** Yeah. Um, our, our manufacturer is actually, uh, kind of like a partner with Atmel in Korea. And so they've been able to get them no problem, but I was a little concerned about that.

**Dave Jones:** What about the TI parts? Are they easy to get in large volume?

**Colin:** Those have been fine. Yep.

**Dave Jones:** Right. Because that's pretty much all you've got, right? I mean, well, there's going to be some, my passives and maybe some regulation on there or something, but. Yeah.

**Colin:** And the accelerometer. Yeah. Oh, you mean on the module or the, the bean?

**Dave Jones:** Oh, I guess both. Yeah.

**Colin:** Yeah. So there's the accelerometer and yeah. RGB LED, but. Yeah.

**Dave Jones:** Apart from that, there's not much else.

**Colin:** Really? Yeah. Yep.

**Chris Gammell:** So in terms of the actual, uh, the, the chipset then, do they, so do they give you the, the stack and everything you need for it then? Or how does, how does that kind of work then? Like when you're starting to develop that?

**Colin:** Yeah. So TI has a stack that you get, um, and it comes with some pretty good features. Uh, a lot of the bean stuff, you know, you've kind of added onto it. And so the, the whole system of the bean, uh, kind of all the Bluetooth stuff is abstracted into the, uh, code we've written on the module. And then just the kind of user parts of it, um, are on the bean in the kind of app mail library.

**Dave Jones:** And, and that, and that stack that's running on the 8051, right? Yeah.

**Colin:** Yes. Correct.

**Dave Jones:** Is that, is, do they give that in assembly or do they give it in, uh, C?

**Colin:** It's, it's in C. There's, there are a lot of parts that are pre-compiled, um, but it's kind of part of like a scheduler. And so you're able to kind of fit, you know, user code, uh, uh, into it. So you're not, you know, holding a connection or disconnecting.

**Dave Jones:** Okay. So you didn't write all of this from scratch. You're sort of doing it at a more high level.

**Colin:** Yes. Yeah. Although there's a lot of like quirks that we, uh, kind of our protocol works around. So for example, there's, you know, if you're interacting with the bean from a computer or from an iPhone or something, uh, there's different end points. So you, um, you know, like Chris was mentioning, you may want to just blink the LED and see which, which unit you're connected to. And so that message just goes to the module and the LED is actually connected to the module. So that never has to interrupt anything the user code is doing. Um, got it. It's actually, you know, uh, it prevents against the user code on the Arduino kind of holding the LED. So it always can be overridden by the, uh, by the module. Got it. And so, you know, yeah, the packets kind of know which endpoint they're going to. And, um, you're never able to get it in a state where you can't connect to it and reprogram it. Um, which took some work. Uh, and then you're also able to update the firmware on the module. So, uh, we actually counted the other day. I think we've released 12 new features in firmware since we launched, since we shipped the pre-ordered units. Oh, wow. Excellent. Yeah, that's great.

**Chris Gammell:** So we've been very, very active with that. How does the module actually talk to the, to the, uh, at mega 328? Is it, is it serial or is there a spy?

**Colin:** It's through serial. Okay. And so it, it kind of interacts with the boot, you know, well, there's a lot of commands that we've added, but then also when it reprograms, it just kind of interacts through the boot loader, like you would expect.

**Chris Gammell:** Okay. Yeah. What I'm mostly wondering about is, so say then, say Dave or I were silly enough to think that we could do Bluetooth and, uh, we bought a module and then wanted to interface it to something else, you know, what are, what are like the, the limits on the update rates? And I mean, can you do other protocols or anything like that when you're actually talking to other chips?

**Colin:** Yeah. You mean like if you wanted to interface like a spy or I squared C sensor or something like that?

**Chris Gammell:** Yeah. Yeah. I mean, just basically when, when you're moving away from the bean and just use the module, how do you expect or how have you seen people using this kind of thing? I see.

**Colin:** Um, so actually one thing that we're working with a lot of companies on is, uh, a way to take your code that you wrote on the bean and move that into a, a production ready, um, design. And so what you can actually do is use our module, our, um, Bluetooth module with the same bean protocol and then just add a different coprocessor, which could be a mega, it could be an MSP430, it could be, you know, ST micro part or whatever. Um, and that way, like you can reuse the code generally that you wrote for the bean and also, uh, you know, have this system you can put on a custom board and any shape you want and it's much more, uh, cost efficient. That's great.

**Chris Gammell:** That's like the, uh, promise of C without actually the realities of C, right? Yeah. Oh, I'll just compile my code again for a new processor. Yeah, right.

**Colin:** Yeah, exactly. Good luck with that. Yeah.

**Dave Jones:** Now you don't have any real time clock on here, do you? To do like real time tasks. No. You know, switch this on at 1pm, you know?

**Colin:** You know, that's a, yeah, I've, I've thought about that. You know, there's some nice little modules or little add on boards that could do that. Like, um, one of the projects I actually made, uh, for fun with the bean was, um, this, basically it looks like a painting, uh, it's on canvas. It's, it's not actually, I did it in Photoshop. Don't tell anyone. Um, but it has a bunch of neopixel LEDs behind it. Um, and the, the painting actually shows like the California coast and then it has each surf spot that I surf. So I surf a lot here. And, uh, and so each, you know, for the next seven days for each spot, there's an LED that'll kind of tell me the condition for that day. Um, and so like, yeah. And it's cool except now it's, it's great during the day, but then at night it's way too bright. And, uh, so it's, it's one of those things where you, you know, you finally make it like, oh, this is perfect. And then you're trying to go to sleep and it's like super bright.

**Chris Gammell:** Like, oh God, time to get up. Yeah. Time to go surfing. The surf is good. Yeah. Oh my God.

**Colin:** That wouldn't be so bad, but, uh. So yeah, I thought about adding like a real time clock for that or maybe a light sensor would do it too.

**Dave Jones:** Got it.

**Chris Gammell:** I mean, I, we don't expect you to tell us about your, your, you know, your specific customers, but I mean, like, could you get us a feel for like, are, are, is it mostly software based companies that are buying and using this kind of stuff? So that's why you're kind of guiding them towards this, this path or is it more just people that need connectivity or that are maybe harder people?

**Colin:** It's really all over the board, which is, makes it really exciting. Like, you know, it's, it's people anywhere from like teachers buying it to teach, you know, students how to code, um, from, you know, literally there's a guy, uh, that works at a middle school program all the way to like Carnegie Mellon. There's a professor there that's, um, the beans part of their like connected device class. And then, uh, companies that ranges from, you know, startups with one person to, uh, fortune 500 companies who have these kind of new, like, uh, proof of concept departments that just, uh, crank out these new kind of prototypes. They're almost like a startup. Um, so it's totally varied. Um, and then, you know, some of those people are going into production with, uh, that model where they use the module and a coprocessor and that's kind of intended for people that are like, you know, Hey, we just want to get this out the door and build a thousand or like 5,000, but we're, you know, we can't quite see the path to like a hundred thousand yet. Um, and then the, the guys a little bit above that, uh, are using just the module. So like one of the companies I can talk about is this company called Misalu. Um, it's an iPad, uh, music keyboard. Um, so it's actually a Bluetooth keyboard that connects your iPad and you can, uh, play music with it and it all works over Bluetooth energy. It uses our module, um, was funded on Kickstarter and, uh, you know, now they're shipping and kind of taking retail orders and stuff like that.

**Chris Gammell:** That's awesome. So, so I guess that's a good example too, because I'm wondering kind of about, like I mentioned the update rate stuff as well. So is it like a MIDI style where it's like 32 kilohertz? Cause the MIDI is slow. That's what I'm always surprised by is like 32 kilohertz clock. That's all you get. And, but it's fine for, for most human based tasks like that. Right.

**Colin:** Yeah. And actually, you know, the latency was their major challenge, which they, they overcame, but, um, yeah, cause the latency, you know, the MIDI, MIDI is definitely slow with the bandwidth, but it's fairly quick in terms of latency. Cause it's wired usually. Yeah, exactly. Exactly. Good old copper. Yeah. And then, uh, so we're actually working with, um, a company here in San Francisco called Retronyms. Uh, they make some really great, uh, music software for the iPad. Like one app is called tabletop. Um, and they're making this thing called wedge, which is, uh, basically like a rubber stand for your iPad where you can plug in USB mini devices and then it makes them, uh, Bluetooth mini devices. Um, cool. So instead of having this like nasty hub of wires and stuff, you can just, uh, make them all Bluetooth and kind of reuse your existing products. Um, so they're using, they're using the module with a coprocessor and actually, um, it's unique in that they're allowing their users to change the code. So it's going to be open sourced. Um, the like sketch that will run basically power the product is, is going to be open source. And so users could download that, change it, and then, uh, reprogram the wedge using the bean software.

**Chris Gammell:** So if you needed to like get rid of a couple of features or something like that to try and speed it up more or what?

**Colin:** Yeah. Well, and actually, so the wedge has like a bunch of, uh, RGB LEDs, so you could write your own effects for like crazy light shows and, um, stuff like that.

**Chris Gammell:** That's cool. So what about the, the latency stuff then? Like, so what is, what is the overhead of, of the bean just kind of out of the box? If I, you know, just hit go on, on whatever, how long does it take to actually go to an LED on the bean?

**Colin:** There are a bunch of factors that, uh, play, come to play here. Um, a lot of them are iOS driven or, you know, whatever mobile OS you're using, um, or desktop OS. So iOS imposes this minimum connection interval of 20 milliseconds. Um, so that's always going to be your kind of driving factor on latency. Uh, so, you know, that's, that's kind of the main one. And there's like a slight amount of latency for the bean as far as, uh, communicating for the module, the app mega, but that's, that's on the order of like millisecond, uh, versus 20. So.

**Chris Gammell:** Right. Okay. Yeah. So that's, I mean, that's, I guess what, what is the human, uh, 30 milliseconds that is noticeable. Is that the one?

**Colin:** I always forget. Yeah. It's, it's funny. This is actually evolved, I think over time because a lot of like touchscreens, specifically iOS, um, there can be, there's always kind of a built in latency that's a little bit longer. So it's kind of funny. I feel like people are, are becoming, uh, less attentive to this, but I think, yeah, 30 to 50 milliseconds is when you really notice it.

**Chris Gammell:** Huh. That's interesting.

**Colin:** Although it's actually more perceptible, I think when you're, uh, touching something and expecting a sound. Yeah. Oh, right.

**Dave Jones:** Right. Okay. Yep. Yep.

**Chris Gammell:** Yeah. I guess, I guess the human, the eye, eye to hand to sound kind of like if you're used to a piano hammer hitting, right. It's like, yeah, that's a very well-defined, uh, interval, but yeah. Huh. So, uh, let's, let's, let's talk about it, man. Let's, let's bring it up finally. Uh, so, so, so Apple, what, what's, uh, so is this based on the, the stack being available or why, why was it Apple first and, and what, what went into that?

**Colin:** Good question. And so, yeah, so basically, uh, it's the stack. Um, it's, you know, Apple, Apple saw this as part of their, uh, core feature set and they really, they really thought through a lot of features in the Bluetooth side. Um, and as much as I'll criticize Apple for other things, they did a good job on this. Um, and you know, they, they actually did a funny thing where they, um, they disregarded the Bluetooth spec and actually added features that weren't in the Bluetooth spec. And now Bluetooth, the Bluetooth SIG is actually adding them. Um, so.

**Dave Jones:** Because they're being forced to. They've had their arm twisted and they went, oh yeah, okay, everyone's using the iPhone.

**Colin:** Right.

**Dave Jones:** Bloody phone, we'll have to put it in.

**Colin:** Yeah. So like, yeah, exactly. On the iPhone, you can be, uh, central and peripheral at the same time. Um. Could you, would you explain that? I don't know what that means. Sorry. Definitely. Yeah. So Bluetooth has two, Bluetooth energy has two roles, uh, central and peripheral. Um, typically the device, the small low power sensor device is the peripheral. Uh, it doesn't, it doesn't manage the connection. It just kind of does a minimum of answering to the central. Um, so typically the phone is the central.

**Dave Jones:** Um, so does that mean the peripheral can't just send out data anytime at once? It's got to wait for a, a ping or something from the main device.

**Colin:** It can, the peripheral can notify the central that it has data and then the data, then the central kind of reads it. Um, so it can go two ways. Uh, but a lot of the more like managing the connection and stuff that happens on the central.

**Dave Jones:** Right.

**Colin:** Um, so the iPhone can be both. You can write an app that, um, scans for peripherals or you can write an app that becomes a peripheral. Um, so like in our light blue app, you can actually simulate hardware. By, uh, advertising like your peripheral. Um, and you can do both of those at the same time. So no one else did that. And now, uh, I think that's going to be in the 4.1 Bluetooth spec.

**Chris Gammell:** Interesting. And that's great too. I mean, that was really smart to make the, so you guys led with this, this app that kind of gave you the, the debugging capabilities, right?

**Colin:** Yeah. Yeah. And that one's done really well for us. I think there's over 80,000, uh, downloads of that. Nice. Um, so, you know, maybe not huge for a mainstream app, but for, you know, developer. Grandma's not downloading the light blue app, huh? No, no. That's funny. Funny story about that actually. Oh, yeah? Okay. That's who she is now. Um, so, uh, somehow Fitbit has recommended light blue as the official, I lost my Fitbit. I need to find it app. Oh, sweet. And, uh, I guess, I mean, it's sweet in that they leave us five-star reviews, but they also call us asking for support, finding their Fitbit. Yeah. So, that's just funny. I don't know if we decided to do that.

**Dave Jones:** All right.

**Colin:** So, you know, I'll use it.

**Dave Jones:** So, your app just sends out a ping, does it, and then tries to find where the Fitbit is?

**Colin:** It just gives you, yeah, it just gives you the signal strength of any Bluetooth device around you. And so, you know, we have reviews that are like, oh, I lost my Fitbit in the sand of the volleyball court, and light blue helped me search for it for an hour, and I finally found it. And it's like, oh, my God.

**Chris Gammell:** You guys are like the new version of the metal detector. Yeah. This hardware thing doesn't work out. That's where you go. Yeah, exactly.

**Dave Jones:** We've just become an app company. That's it. Yeah, that's all you need. No, this hardware business, screw that. Let's just sell an app that finds stuff. That's crazy.

**Chris Gammell:** So, okay, so the stack is good. And I had heard that from other people. Actually, I had heard that when TI was, I think when they were starting to talk about their 2540 and pushing that in the marketplace, because they had asked if I wanted a dev board, and they're like, oh, but you need an iPhone. I'm like, I'm not an iPhone guy, and I'm not spending 600 bucks for one. And then I kind of asked around about it, and they're like, yeah, it's because the stack's good. So that makes a lot of sense.

**Colin:** Yeah. So we have, you know, we have some Android support. Like there's an SDK. It's kind of an unofficial SDK. But there are ways. You can write an Android app that connects to the Bean. And the Bluetooth low energy support on Android has come a long way. Like, you know, as of 4.2, there is really no real way to do it. Like you'd have to use the manufacturer-specific stack for each phone. 4.3 added it. So it's been getting better, and we've actually worked on products with Android. But, you know, as far as being a small team, being mostly self-funded, we just had to focus on the platforms where the user experience would be the best. And then, you know, when Android gets his act together, we can go do that.

**Chris Gammell:** I think it's really interesting, too, because that – so, like, you know, we see this – and we've talked about it on the show as well. But, like, kind of seeing software people moving into the hardware space as well, right? I think that drives a lot of the – a lot of Mac users to start with. So that's interesting because then it kind of self-constrains your audience. And it's not like it's, like, you know, a small group anymore either. But it's interesting because I think it just kind of starts to profile that. But then, you know, seeing that – we also see that on, like, the CAD side. We talk about that kind of stuff. Yeah. And just seeing how it's changing the industry and how it doesn't matter as much as it used to, right? It's just – but I think the other interesting thing is that the fact that nobody said Windows yet, right? So we talked about Mac, we talked about iOS, and we talked about Android. But I think about software development and I think, okay, well, where's the Windows support or – so –

**Colin:** Right. So we're actually working right now on a Windows loader app. And our choice for that was basically just like you said, you know, people are writing software predominantly on Windows. And while we do want to allow people to write sketches on their Android phone at some point, you know, having that as your – if you're a Windows and Android user and your only option is to use your phone, you might be kind of frustrated. So we want to cover the desktop side first and then do that. But, you know, it's interesting. Like we're all pretty much – well, there's a lot of hardware guys here because, you know, we do hardware for more and software. And, you know, like you said, all the CAD tools are in Windows. And so we all have Macs. We all run parallels and, you know, just use our CAD stuff essentially in Windows. Yeah.

**Chris Gammell:** I think it's just really – it's interesting as a – I mean like good, bad, whatever. I don't think it's any of these things. I think it's just – it's really interesting as a changing landscape because if you go back, you know, five, ten years and you just say, well, we're going to, you know, not have a Windows tool. It's, you know, it's just like – they would have been like, what are you doing? But now it's like, yeah, this makes sense, right? This definitely – and it's driven by the stack and the available software stuff. So that's – I just think that's really interesting.

**Colin:** Right. Yeah. And it's actually funny talking about, you know, looking at this ten years ago or something. So our app that we just released allows you to program – actually write sketches and program beans from your iPhone or iPad. And to do that, we couldn't put the compiler inside the app because Apple doesn't allow that. So it actually compiles on the cloud and returns – on our server and returns the compiled hex and then programs over Bluetooth to the bean. And so that – explaining that to someone, you know, that you're going to program this piece of hardware from your phone, it's going to compile on the cloud, and then program on Bluetooth. It just sounds like a, you know, ridiculous thing. But it's really handy.

**Chris Gammell:** Yeah, don't worry, man. The ButterflyNet people are here to help you. Yeah. That's cool. And that's other platforms too, right? Like embeds move into the cloud type stuff, you know, and we've – you know, Dave and I have disparaged it in the past, but then it's kind of come a long way, I think. And it's really interesting because a lot of the stuff that people are doing is, you know, at least starting with I want to blink something. And then eventually it becomes, well, I'm blinking this thing. Now I want to do this other stuff and there's libraries available. And, like, it just kind of all starts to fall together. And that's – it makes a lot of sense.

**Colin:** Yeah, and the nice thing, you know, the cloud compiler, you wouldn't notice that it's – you know, you won't notice that it's in the cloud unless you don't have internet, obviously. But it's pretty – it's pretty quick.

**Chris Gammell:** So what is that like to – do you – I can get it from an iPad because I guess you have keyboards attached to iPads. But, like, are you doing a lot of iPhone stuff?

**Colin:** Yeah, good question. You know, it seems kind of strange when you first think about it, especially for someone who's, like, you know, been in software development for a while. But one thing it's really handy for is imagine you're giving a demo, you know, you're up on stage or in front of some customers or something. And you're like, oh, my God, my, you know, sensor threshold is wrong because this room is a little bit brighter or something. Well, you can pull out your phone and actually change that. Yeah. So that's handy. It integrates with Dropbox so you can still write most of your code, you know, with your computer and then just get it on your phone. That's cool. Yeah. Kind of the hidden value is that if companies – you know, now that companies are making more hackable products, they can actually have different kind of programs that users are able to install or load onto their product over Bluetooth. So, like, you know, I talked about the Wedge product. You could have your friend write a cool, like, light sequencer effect. He could actually put that on your product from his phone. Oh, interesting. So that's kind of cool too.

**Chris Gammell:** So you're saying, like, so it's like go navigate to this link using your iPhone. You tap a link. It pulls it to your Dropbox, loads it up, pushes it to your Bean, and then now you can hook up your toilet sensor that you never knew.

**Chris Gammell:** You never knew you wanted. You never knew you wanted, yeah. But then you can have it actually as part of an app as well then, you're saying. Yes. Yep.

**Colin:** Could be just part of the app.

**Chris Gammell:** That's really interesting because if that becomes, I don't know, actually. I guess, well, I guess like the Bluetooth devices that are out there now, like the Jawbones and the Fitbits and stuff like that, they also push firmware? I mean, do they have to be wired for that kind of stuff? They push firmware, but it's not necessarily like user editable firmware, you know? Yeah. That's, okay. No, that's really cool. I like that. But that could be some interesting stuff.

**Colin:** We like to promote kind of products that you can modify, you know, you can change, you can add features to. A lot more companies are doing that and it's really great to see. Yeah. Nice.

**Chris Gammell:** That's awesome.

**Dave Jones:** So you guys started out as a, well, you started out originally as just a consultant doing this sort of stuff. Yep. And you branched in the harbor and now you've got 13 odd people.

**Colin:** 13, yep. 13? Yep.

**Dave Jones:** Excellent. Are you still doing the consulting stuff? Yes. Or are you looking to get out of that business?

**Colin:** No, because a lot of our, like I said, the products kind of benefit the consulting customers so well that, you know, it makes sense to do both. But I'd say that more and more we're kind of working with companies who are doing stuff in our particular niche. So Bluetooth flow energy or, you know, smartphone connected products is kind of where we're living these days.

**Dave Jones:** Got it.

**Colin:** Yeah.

**Dave Jones:** So have you got people dedicated to doing that sort of thing or is it just, oh, we've got a consulting job, all hands on deck?

**Colin:** It's kind of varied between the teams. So like there's no, you know, everyone's, everyone can work on different consulting projects depending on what we need, what skills we need. So everyone works on a variety of things. But I'd say, you know, the last year we were pretty heavy on bean development, probably like, you know, 60% of our effort. But now that it's pretty stable, we're bringing on more consulting projects and supporting that a little bit more.

**Chris Gammell:** Any plans to do like a standard header or anything like that in future versions? Or, I mean, I guess, you know, users could roll one real simple. But I guess the, you know, if the punch through team has a standardized header then, is that something in the future as well? You mean for like a connector on the board? Yeah. I mean, or just a secondary version of the bean. I mean, is it going to just stay like this form factor for now or are you guys going to keep doing other hardware stuff?

**Colin:** We really like this form factor. You know, we've gotten a lot of feedback and we've seen how people are using it. So we don't really have anything that's public right now as far as different form factor. But, you know, we've seen people do interesting modifications. Like people have just made it smaller by chopping off the perf board essentially. You're right. Yeah. So we may try to make that like a scored feature in the future. That's kind of the only one that will happen relatively soon. And then, yeah, we're just watching, you know, we're watching where the connected devices are going and seeing how people use it. And, yeah, we have a lot of thoughts there.

**Dave Jones:** There is a lot to be said for sticking with one form factor and not flooding the bloody market with 10 different versions of product. That's true.

**Colin:** Yeah. We really, you know, we tried to consolidate everything into kind of, you know, one main product.

**Dave Jones:** Right. Yep.

**Colin:** Yeah. Especially for a small team. You know, you have to focus on one thing.

**Dave Jones:** Of course. You don't want to be supporting 10 different products. That's.

**Colin:** Yeah.

**Dave Jones:** Do you guys find that it's more beneficial working in the same office or do you get the impression that, oh, you could, guys can all work from home and then, you know, come together using online tools?

**Colin:** That's definitely more common now. But I feel I still prefer to be in an office. I think there's like, there's chance encounters. You know, you overhear someone talking about a cool project that relates to something that you're interested in. And, you know, that might happen on Slack or whatever you use for, you know, company chat. But I don't know. I just think it's, it's, it just feels better in an office. You know, you share the enthusiasm and the culture I don't think would be the same.

**Chris Gammell:** No, as a remote worker now, I can tell you it's a, you know, it's a different experience. It's like, you know, when you're actually there with the people. Plus, I mean, I'm guessing if you guys are a San Francisco startup, you must have a beer fridge or something, right? It must like tweet or talk to your blue beans or something, right?

**Colin:** We just got a bigger beer fridge, actually.

**Chris Gammell:** There we go. Yeah. Put your nail on the head with that one. Yep. Yep. I know. I'm learning San Francisco. I'm jealous of beer fridges of everywhere. Yeah.

**Dave Jones:** So are you guys hiring if people want to join the dream?

**Colin:** Yeah, we are. We're always kind of looking for good people. And generally what I say is like, we, you know, we like people who are really excited by building things and, you know, would do or did do engineering like projects outside of school without, you know, being required to do it.

**Dave Jones:** Well, look, if they're listening to the amp hour, they're a shoe in anyway, aren't they? Great.

**Colin:** Great point.

**Dave Jones:** You know what?

**Chris Gammell:** That's good. And that's what I always look for when I'm hiring people too. I mean, that's the thing. And obviously Dave does too.

**Colin:** So, yeah. Yeah. Yeah. Yeah. And it's interesting. I mean, interviewing is a tough, tough thing. And I think, you know, I still have a lot to learn on it. But the thing that I've found is easiest is to have someone in kind of just for a chat with another person that works at Punch Through and me. And, you know, we'll kind of talk around some things. And generally if you talk about a project and someone's really, you know, an enthusiastic engineer, they'll kind of chip in with their thoughts. And, oh, well, I worked on this other project that's similar. And it's really easy to tell just from a casual conversation like that.

**Chris Gammell:** Totally. What you should do is you should lock them in the room, right? And then tell them that they have to access the bean and let themselves out, you know, writing some code.

**Colin:** I hope they have an iPhone right now. Yeah. Oh, Android user, huh? No, we could write their own app. Yeah. No. Yeah.

**Dave Jones:** Don't call us. We'll call you.

**Colin:** We just had an idea for something like that. It's still in the planning stages. But we want to put together a box of mystery components and basically just send it to a potential hire and say, you know, hey, work on this for, you know, max of four hours or something over the next week. And make something cool and show us what you made. Oh, that's great. You know, put some useful stuff in there and put some totally crazy, ridiculous stuff in there and just see what they come out with.

**Chris Gammell:** No, I used to do that for Boy Scouts. They would send us just like a box. I mean, it wasn't obviously technical stuff, but it was just like a box of junk and then just like see what you make. Right. And then we'd see some awesome creations. So, no, that's great, man.

**Colin:** Yeah. I think we're going to try that for students. Just it's a little bit easier, you know, if they haven't been in the, you know, industry for a long time just to get a sense of their creativity and stuff.

**Chris Gammell:** Send them a – make sure there's a slinky in there or something, you know, something – some crazy stuff, you know.

**Colin:** Yeah. Yeah. One of our guys here had a lot of fun putting the list together. There's definitely some ridiculous things there.

**Dave Jones:** For some reason, the first thing that popped in my head there was Egon Spengler from Ghostbusters. He said, I had a slinky once, but I straightened it. Sorry, it just popped in there. Couldn't it?

**Chris Gammell:** That's a great one.

**Colin:** Yeah, that's good.

**Chris Gammell:** So, Colin, how do they do that if they want to get in touch with you for the hiring stuff? Is it like an email address or –

**Colin:** Yeah, yeah. There's just info at punchthrough.com, which comes to a couple of us.

**Chris Gammell:** Okay.

**Colin:** Yeah. Cool.

**Chris Gammell:** Yeah, and portfolios are always probably a good thing to send with them, I'm sure. Yeah.

**Colin:** We always say, you know, we don't want to look at your resume. We just want to see the projects you've made. Bingo. Awesome.

**Dave Jones:** Nice. Yep. These guys know what they're doing, folks.

**Chris Gammell:** They do. That's good. Well, anything else, Dave? What else? I'm kind of – mostly I'm reinvigorated to go turn on the bean again and start programming. I don't even have one. No, you've got to get one.

**Dave Jones:** Oh, I've got to get one.

**Chris Gammell:** Jeez.

**Colin:** You guys have distributors in Australia, right, Colin? Yeah. Yeah. And I'd say right now – actually on Reddit and on our Bean Talk forum, we're giving away 10 beans on each site. If – just tell us a cool holiday project that you want to make and the top 10 will get a free bean.

**Dave Jones:** Well, I can't tell you the project that I want to use this for, but I need it to – basically it ties in with my energy harvesting experiment video that I did.

**Chris Gammell:** So I need to be able to – If you could just send Dave a light blue bean and also a MacBook Pro, that would be very helpful as well.

**Dave Jones:** Yeah, exactly. Right. No chance. All I need to know is how much current draw does it take when it transmits? And the answer's like 5 or 10 milliamps, right? Burst.

**Colin:** I think – Current. Yeah. For that short amount of time, I think it's about 10.

**Dave Jones:** Damn it. Damn you, Bluetooth low energy. I'm going to have to go to something else, I think. It's just too high.

**Colin:** You can get some good capacitors on there to buffer that up.

**Dave Jones:** Yeah, but the issue is the charge time. Yeah. No problems. You know, you can get a cap on there that can supply, you know, your 10 milliamps for your 0.2 seconds it needs to transmit or something. Yeah. You know, charging it up with energy harvesting is – yeah.

**Colin:** You can actually scale – in software, you can scale the output power down. Right. So it's at like 4 dBm now, the highest, and you can scale it to like negative 8. Or something like that.

**Dave Jones:** Okay. Yep. Yep.

**Colin:** Yeah. So it'll be lower.

**Dave Jones:** But still, it's going to take a few milliamps to pump it out, right? Yeah. Yeah. Damn it.

**Colin:** You don't get enough sun there for that?

**Dave Jones:** It's not – no, it's thermal energy. It's thermal energy. Solar is easy. Yeah. So anyway. That's really cool. Too hard. Maybe I'll have to go to Ant or something like that. Yeah. One of those ultra low power, you know, protocols. Because as – Good luck with the coating. Yeah. Exactly. Yeah, exactly. I have to do it from scratch. You won't be able to use a nice module like this. Probably. Hmm. Grumble. Grumble. Anyway, Cole, thanks for joining us. It's been awesome.

**Chris Gammell:** Yeah. Yeah. Thanks for having me. Yeah. Enjoyed it. People should definitely pick one up. They can go to punchthrough.com slash bean and order there. Or then I think there's some distributors around the web as well, right?

**Colin:** Yeah.

**Speaker ?:** Yeah.

**Colin:** Definitely. Yep. Can you know our site? Make Magazine also sells it on the Makershed. Cool. Sweet. Let us know what you make with it. Definitely.

**Chris Gammell:** All right. Thanks, Colin.

**Colin:** Yeah. Thanks, guys. It was great.

**Chris Gammell:** Thanks, mate. See ya.

**Colin:** Okay. Bye.

**Colin:** um oh hold on sorry about that conference phone

**Dave Jones:** oh man boards are finished testing yeah yeah yeah it's homer
