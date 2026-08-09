---
episode: 50
title: Callow Cough Coverups
url: https://theamphour.com/the-amp-hour-50-callow-cough-coverups/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV blog. And I'm Chris Gammell from Chris Gammell's Analog Life. Hey Chris, it's one hell of a morning, isn't it?

**Chris Gammell:** Ah, yes it is.

**Dave Jones:** I'm sick as a dog.

**Chris Gammell:** Under the weather a little, yeah.

**Dave Jones:** Yeah, under the weather. We've just spent, I don't know, half an hour looking at kill switches. Cough switches as they're called. Yeah.

**Chris Gammell:** In the industry, right? Very common. I've been told that I've needed one when there may or may not have been toilets flushing in the background. People didn't know that that's what it was.

**Speaker ?:** Right.

**Dave Jones:** And that's what all the pros have, right? They have this big red button sitting next to them. Whereas if you actually, you know, you actually hit the button and it disables your mic cleanly. So there's no like pop sound. Disables it cleanly. And then you can cough. You can do whatever. You can say, oh, F. You know.

**Chris Gammell:** You can fart for four minutes straight. Yeah, exactly. You can just do anything.

**Dave Jones:** And then you remove your hand from the switch and you come back live. And that's what we need here. So we spent, I don't know, the last half an hour trying to figure out how to do it in Windows. Because I'm using the USB mic, right? So, and we found out how to do it in Windows. Here we go. I'll try it now. I'll hit my mute button.

**Chris Gammell:** Oh, where'd he go? He's like gone or something. Silent.

**Dave Jones:** And I'm back.

**Chris Gammell:** He's back now. There you go.

**Dave Jones:** So we do have it in Windows. But, you know, you've got to have the window open. And it's a tiny little button. You've got to scroll with your mouse. And it's just. So I reckon I'm going to build a cough switch.

**Chris Gammell:** I think it's a good idea. I think it's a hell of a challenge for USB. I think.

**Dave Jones:** Well, it's pretty. Well, it's easy. Because you do it in the Windows software. Like you don't put it in series with the USB mic. Right? You wouldn't do that. You would actually have it as a separate plug into a separate USB channel. And all you need is a USB controller. Like a little pick with a built-in USB port. I don't know, man. And a switch.

**Chris Gammell:** Maybe it's worthwhile just to have a man in the middle kind of thing. Where you put an FPGA in the middle. And usually it just passes through data.

**Dave Jones:** Ah, too complicated. Too complicated, dude. No, you've got to kill it at the source, which is Windows. And then it's compatible with every device on the market. Because the whole idea of Windows USB mics is that they convert your USB mic, whatever it is. Any brand, any protocol, any anything, into a Windows audio stream. And then. So you're better off killing it at the audio stream, which goes into your recording program. And then it works with any mic, any recording program. And you're sweet. Anyway, that's how I'd do it. I think you're choosing the complicated option.

**Chris Gammell:** Maybe it's complicated. I don't know. I think Windows is cranky about USB stuff. I mean, I think.

**Dave Jones:** Yeah, but no, it's easy.

**Chris Gammell:** If you pad the whole signal with zeros, you're going to be much better off. Maybe it'll say, oh, wait, I lost all communication with it. Maybe you have to actually inject like a signal that makes sense to Windows, right? So if there's packets and then you have to actually.

**Dave Jones:** No, I don't think so. I reckon it's easier than that. Windows has the capability. It has a mute switch there. And Windows, you can script almost anything in Windows, I think. So it should be pretty easy.

**Chris Gammell:** Oh, then you just want to activate the switch.

**Dave Jones:** And it goes in. And all it does is activate that function that's already in Windows. Just switches off and on. Bang, bang.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, I've. Yeah.

**Chris Gammell:** Well, the easiest thing would be for you to get an XLR mic and then actually just have it in analog, right?

**Dave Jones:** Nah, analog cough switch. But nah, every podcaster on the planet now has moved to USB mics. Everybody but me. Really? Right? Anyway, if you know of a USB, we had a quick look, a quick dumb Google search. And we couldn't find any USB based cough slash kill slash mute switch. Are there other names for them? I don't know.

**Chris Gammell:** I don't know either. That's all I can come up with. But I tell you, I'm going to be disgusting now. I'm just going to fart the entire show. Right, fart and cough and burp all over the place, right? Yeah, I'm going to run upstairs and, you know, like start, get my dogs to start barking.

**Dave Jones:** Awesome. Now that you've discovered the joy of the mute switch in Windows.

**Chris Gammell:** Right.

**Speaker ?:** Right.

**Chris Gammell:** And speaking of, they might start barking this time. It is July 4th here.

**Speaker ?:** Woo-hoo!

**Chris Gammell:** Independence Day from stuff. Yay!

**Dave Jones:** Happy Independence Day, all you yanks.

**Chris Gammell:** Yeah.

**Dave Jones:** It's a big deal, right? Then what the hell are you doing recording? You nerd. What are you doing recording? I got nothing going on, man. Well, you should be out. Isn't this the biggest day of the year in the U.S.? It is not.

**Chris Gammell:** I don't know where you came up with that. I mean, like, it's not like I'm like, it's like everybody is mandated to be in a parade or something. Right.

**Dave Jones:** Oh, well, I got to go, Dave. Sorry. Marching bands and parades and stuff. Come on, it's America, right? Home of the marching band. Oh, there we go.

**Chris Gammell:** Yeah. No, I just didn't have anything going on. I was doing some work today. You know, I was out grilling all day. I posted a picture to Twitter or two. You know, like, I was barbecuing. That's pretty American, right? Grilling. Grilling. Barbecuing. Grilling.

**Dave Jones:** Yeah.

**Chris Gammell:** Sorry. Do you say it differently there? Oh, no. Barbecue. Throwing a something on a something. Is that what I...

**Dave Jones:** Shrimp on a barbie, yeah. Shrimp on a barbie. As Hoag said, and we've never lived down ever since. I know. That's really... Said in that ad campaign back in the 80s. Oh, it's horrible. Crocodile Dundee came out. Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Yes.

**Chris Gammell:** That's actually in the vocabulary of what Americans understand about Aussies.

**Dave Jones:** Right. Shrimp's on the barbie.

**Chris Gammell:** Yeah. And Foster's beer.

**Dave Jones:** Oh. Right.

**Chris Gammell:** Which isn't... It's all right. It's not great. It's not great.

**Dave Jones:** I've heard it's complete shit. Not to say, because I don't drink beer. I'm not a beer connoisseur. So... Right. Right. So it all tastes like shit to me. So... Right. There you go. Or piss. Yeah. Right.

**Chris Gammell:** Which is... Yeah. Jeez, we're throwing in all the... Don't drink and solder, kids. You know?

**Dave Jones:** Bad language today, aren't we?

**Chris Gammell:** What about bad language?

**Dave Jones:** Well, shit and piss and... Oh. All sorts of stuff we're throwing in. Farts and...

**Chris Gammell:** Fart. Yeah. Fart's really the... That's the kicker. It's going to be where those...

**Dave Jones:** That's going to get us thrown off air, is it?

**Chris Gammell:** All those grandmothers really click it off at that point. All our grandmother listeners. Yeah. Yeah. Ah, well.

**Dave Jones:** Just lost half our audience. Just lost the grandmother vote.

**Chris Gammell:** The grandma constituency. Yeah.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Ah, well. So let's... So since we were talking about July 4th, let's talk about... Let's start with This Week in Nerd History.

**Chris Gammell:** Doop-da-doop!

**Chris Gammell:** So, This Week in Nerd History. I got it right here. This Day in Nerd History, rather. On this day, 50 years ago, engineers from the United States were eating hot dogs and watching stuff blow up like all the rest of it. Actually, I looked and there's nothing going on this past week. There's nothing. So, I thought... Right. Throw that in. Yeah. It's tough because I think... You know, I'm sure this shutdown's been going on, at least in the US, for a long time. So, historically, it's been a slow week.

**Dave Jones:** So they were still doing office pranks back then, huh? Yeah. You know, nothing's changed. The more things change, the more they stay the same.

**Chris Gammell:** That's right. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So, that's our... What were office pranks back... Back in the day? In the 50s or something? I don't know.

**Chris Gammell:** I don't know, man. I'm 27, so I wouldn't know that.

**Dave Jones:** Right. They did something with your slide rule? I don't know. Taped it. Oh, maybe. Yeah. Right?

**Chris Gammell:** Yeah. They switched out your pocket protector with a sheet of paper or something? I don't know.

**Dave Jones:** Turned it inside out? I don't know. Yeah, there we go. Yeah. That's it. Right.

**Chris Gammell:** Oh, boy. We're so stereotypical, aren't we? Well, I mean, you think about the engineers back in the day, they definitely looked a lot more stereotypical than these days. I mean...

**Dave Jones:** Yeah, they did, because it was... You know, you couldn't turn up to work in jeans and a t-shirt if you're an engineer, right? I think you had to turn up in the, you know, the white collared shirt and the pants and the... Yeah. You know, and the tie, probably. So... Yeah. Yeah, it was more... You know, these days, shit, if you turn up like that, you get laughed out of the place. Yeah. Or sent to sales. Which is worse. Yeah.

**Chris Gammell:** Don't do that. Don't do that.

**Dave Jones:** No, please, don't. Marketing. Jesus.

**Chris Gammell:** Yeah.

**Speaker ?:** Ah.

**Chris Gammell:** Well, let's just... Should we get on with the show? Yeah, let's do some shout-outs, because... Speaking of something I'd like to sell, did you see this footstool from Evil Bad Scientist Laboratories?

**Dave Jones:** Oh, I tweeted it, dude. You're not up to date on my tweets. Oh, you're right. I didn't follow you. It's freaking cool. I'm sorry about that. Yeah, this is awesome.

**Speaker ?:** Yeah.

**Dave Jones:** I want one. And, like, I saw the photo, and I went, oh, that's freaking awesome. And then I went and looked at how much trouble they put into building this thing. Yeah. And it was amazing. You know, CNC routed, cut, 20 different pieces. And anyway, it's a footstool, you know, a full-size footstool. That's a triple five timer. It's, you know, it's painted, and it looks exactly like the chip down to every last detail. And it's, ah, it's fantastic.

**Chris Gammell:** I love it. It's brilliant. I mean, I actually got to visit their lab, so I saw their ShopBot, what they were using to cut this thing out with. And, man, that's cool. I mean, it's, like, simple in theory. You know, like, it's a milling machine for, like, sheets of plywood, right? Yeah, yeah, that's right. That doesn't seem tough, but it seems so much more revolutionary to me than maybe it is. But, man, it's awesome. You know, you get that file in there. And I'm not sure if they have a program that actually did the slicing for them. Because you think about it, if you had a 3D object.

**Dave Jones:** Ah, probably. I think you can do that. You draw the 3D model, and then it can, I believe, the programs can actually slice things up for you. Right. So if that's the case, then... I know people who actually make, we've talked about this before, people who make cases like that. So you draw your case, you know, if you project or whatever, in 3D, you know, in some 3D tool like AutoCAD or something. And then these programs can actually slice it up into individual bits. And then you can assemble. So you can actually... So you don't need a 3D printer. All you need is a 2D, one of these 2D routers. And you can actually get, like, a Mylar sheet or a plastic sheet. And you can actually...

**Chris Gammell:** Yeah. Or like a laser cutter.

**Dave Jones:** And then you can actually cut out all these different layers and then actually stick them one on top of the other with glue, and you can build up your product layer by layer.

**Chris Gammell:** Yeah.

**Dave Jones:** Just like a 3D printer. So yeah, I think the software kind of, you know, takes care of that for you. I would be surprised if they had to individually do each one. Well, either way, it's spectacular. Yeah. It's very cool.

**Chris Gammell:** Yeah. I can't wait to see what they do next. Yeah, well...

**Dave Jones:** Oh, man, they could sell those.

**Chris Gammell:** Oh, you want the actual footstool, not the... You don't want the shot bot?

**Dave Jones:** Oh, well, yeah, both.

**Chris Gammell:** Shot bot. You know, for the size of your lab, I don't think it would fit. I don't think you'd be able to park the car.

**Dave Jones:** I've got room for the footstool. I don't have room for the shot bot. Afraid not. And they're expensive, too. How much do those suckers cost? They're 10 or 20 grand. They're like a decent 3D printer, I think.

**Chris Gammell:** No, I think they're 3 grand, I think. They're kit-based. Yeah, as far as I know.

**Dave Jones:** Oh, are they? Oh, okay. Oh, it's just a kit. Right. It's not a big industrial type one.

**Chris Gammell:** Right, because Wendell, the guy from EMSL, right, he was... Yep. ...talking to me about putting it together, and he actually had to make a bunch of mods for it.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Let's see. Pricing. Pricing. Here we go. Good old... Oh, maybe it is. Ooh. Oh, never mind. I might be wrong, then. How much is it? It says 7,000 for educational.

**Dave Jones:** Right. There you go. And it's a kit, did you say?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Wow. Gee, I thought you could buy commercial ones for almost that.

**Chris Gammell:** Anyway, I don't know. Anyways, I'll look into that more, but yeah. Either way, they're... I mean, you think about the things you can make with it. I mean, man, there's some cool stuff out there. There's a design studio. I'm not sure if I've mentioned them on here before, but it's called Because We Can. It's a design studio. And I know Adafruit has showcased their stuff before, but they actually use their ShopBot. They're really talented woodworkers as well, and they design the Wikimedia office stuff, like all their office desks and everything else. And they did the Wikipedia logo out of slices. So that's some cool stuff, you know?

**Dave Jones:** Yeah. I love that stuff. I wish I had room for... Because you can get these like secondhand as well, like these big industrial type ones. You get them at auctions and stuff like that.

**Chris Gammell:** Yeah.

**Dave Jones:** I give my right arm for... Yeah. For more room. I can put shit like this in. Yeah. Yeah. Exactly. It'd be fantastic.

**Chris Gammell:** Stop parking your car inside.

**Dave Jones:** Yeah, I know. Tell me about it.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Speaking of building up a case for something, we actually had... So I mentioned last week that I think people could do it for under $100. And I'm not sure... We haven't confirmed it yet, but Jeremy Blum, who's been on here before, he... Hey, Jeremy. He said he might be able to do that because he's working at MakerBot this summer. So he's looking into that. He might be trying to do a less than $100 prototype using that Google SketchUp software and...

**Dave Jones:** Oh, okay. And the DesignSpark and all the rest of it. Right. Right. I tried to use DesignSpark the other day. Yeah? Yeah, I downloaded it and I started to use it and, well... Yeah. Eh. Well, it's not perfect. First of all, I hated registering the damn thing. Come on. If you're going to make it available, just make it free. I know you're trying to suck people into your stupid DesignSpark site, but... You know, because you want to show off numbers to your advertisers and stuff like that. Right, right. But, jeez, come on. You know... Anyway, that was kind of annoying. Yeah. But... And then, I don't know. It just... I went straight. I loaded up a piece... The first thing you do is you load up a piece of being a schematic... You know, example piece of being a schematic. I tried to drag some tracks around and, I don't know, it just didn't... Yeah. It didn't do it for you. It didn't work the way I wanted it to. And I couldn't pan. You know, I couldn't just, like, hold down the right mouse button and pan and stuff like that. There's always those learning... I don't know. I think there is a way to do it. I think somebody tweeted me, hold down P or something and move it. I don't know.

**Chris Gammell:** Yeah. It's just... Yeah, it's...

**Dave Jones:** It was okay. You know, it seemed to work, but... Yeah.

**Chris Gammell:** It's always tough learning a new software package, no matter what it is, but...

**Dave Jones:** Yeah, I know. Because it can most likely do the stuff you want. It's just not the way you expect it to work, you know. Yeah. Yeah. I just thought, you know, in a PCB editor, the thing you want to do all the time is pan around. It's a basic functionality of any CAD software, really. And if you've got to go over to the slider window, you know, the slider bars on the side and drag them to move across, you know, you've just killed your productivity.

**Chris Gammell:** Yeah, I agree.

**Dave Jones:** Instantly. So, anyway. I think there is a way to do it, but it's not obvious. So... Yeah.

**Chris Gammell:** While we're talking about DesignSpark real quick, they tweeted back to me about that converter thing. And it's actually... They wanted to point out that I didn't have it quite right. It's actually a generic converter. So, it's that IDF, which is the intermediate design format. And that actually... So, it's just a generic one for that. So, any program that can go to IDF, they can convert to SketchUp. And that's kind of what they worked on. And it's not a full-blown model that's actually in there. It's like a wireframe, so...

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Got it. Yeah. Yep. Still, pretty cool. Good starting point for, you know, getting... If you're a hobbyist and you want to try and crank out a cheap design, that might be the path to do it, so...

**Dave Jones:** And speaking of those PCB programs, I'm trying to figure out a way... Everyone keeps asking this. Can I review all of the PCB packages out there and help people choose which is the best one? And, oh, well, you know... God, yeah, if I've got a whole month to do it. But I'm trying to come up with, like, a basic... I think what I have to do here, to review these programs, I think I've got to come up with a basic list of stuff which, you know, can the program do this or not? And if it can, how hard is it to do it? And, you know, and just go... And systematically go through each program. And then you can get a good comparison rather than just, oh, yeah, I think this program sucks or I think this is really cool. And, you know, very... You need a more subjective kind of... You know, you need to be able to measure the... Quantitative. That's the word I'm looking for?

**Chris Gammell:** Quantitative versus qualitative?

**Dave Jones:** Quantitative. Yep. Exactly. So, yeah, I need to quantify things, you know? So, I think that's the way to do it. If you've got a good idea how I can review PCB packages, please let me know. Yeah. Anyway, I think I have to come up with a list. That's the only way to do it. Yeah. And it's systematic. Otherwise, you know, you just fart around forever and my videos would be five hours long and, yeah.

**Chris Gammell:** Well, it's all going to come down to probably preference in the end, too. I mean, there's going to be some things, right? But then eventually people have to balance.

**Dave Jones:** Quite a lot of stuff, which is personal preference, of course, yeah.

**Chris Gammell:** Of the balance price and everything else, too, so...

**Dave Jones:** And, you know, but if the program's got that feature, then you can go tick. And, well, you know, you can always say, well, I don't like the way they've implemented that, so, you know, I'm going to mark it down half a point or something. But at least it can do it, which is the main thing. It has that capability or feature or whatever, so... Yeah, makes sense. Anyway, let me know.

**Speaker ?:** Okay.

**Chris Gammell:** So, two more shout-outs real quick. We had Harry from RoboGaia. It's a new company he just started. It's like a boutique electronics company started from his kitchen. So, that's pretty cool. It's always a scary and exciting venture. So, thanks to Harry for... I hope he hasn't quit his day job just yet. I don't think he has, but...

**Dave Jones:** I don't know. I haven't looked at his site. Is it cool? That's not bad. It's getting started.

**Chris Gammell:** I think he only has one project right now. Oh, I think...

**Dave Jones:** Well, I know. You've got to start somewhere. It's awesome. Exactly. Yeah.

**Chris Gammell:** Start small. Build up for him. Good luck, Harry. Yeah, good luck, man. And then also, Richard, who's SJGadgetGuy on Twitter. He linked here from his site as well. So, good stuff. Thanks to... Thank you very much. We always love that. Always love when people link here. We really appreciate it.

**Dave Jones:** Yeah, because we need the extra listeners, don't we?

**Chris Gammell:** I don't know.

**Dave Jones:** If our goal to dominate... Well, if your goal to dominate the world... Me, it's like, eh, whatever. I think you're on some.

**Chris Gammell:** Dave's been a lot more calm about it. That's good.

**Dave Jones:** And Chris is going, oh, no, our graph has dropped by 0.1%. Oh, no. Our listeners have abandoned us.

**Chris Gammell:** No, they wouldn't abandon us. It's tough, man. There's only so many ways we can get feedback, you know? Numbers are one way, and comments are another, and, you know. So, we like it when people listen. It's great.

**Dave Jones:** So, if you're not listening this week, if you haven't downloaded this week's episode, well, you won't be hearing this, and you'll be turning poor old Chris into a big stress bunny. Because, so, please keep listening every week. For my sanity, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** How's my voice holding up? It's not bad, man. I'm afraid it's just going to absolutely die mid-sentence.

**Chris Gammell:** Well, that'll be fun. That'll be fun.

**Dave Jones:** Yeah. It could happen. I haven't had to use my mute switch yet.

**Chris Gammell:** That's good. That's good. I've still got a billboard. I just won't. I've been...

**Dave Jones:** Yeah. I want that big die-cast box on my desk here with a big red missile fire button, you know? Push that sucker down, and it just shuts me up.

**Speaker ?:** Which...

**Chris Gammell:** Can I get one of those, too?

**Dave Jones:** A lot of people would like. Right. Kill co-host switch. Yeah, right. Yeah, one for you, one for the other person. Right. Excellent.

**Chris Gammell:** Yeah.

**Dave Jones:** You can do that any time. You're the editor.

**Chris Gammell:** Oh, yeah. You can just delete your chunk of talking. Right. Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** What else we got in today's show?

**Chris Gammell:** Mm, let's see. Oh, what do we have? I'm going to mute you for a second.

**Dave Jones:** Well, I actually repaired something.

**Chris Gammell:** Oh, oh my.

**Dave Jones:** Yeah, I don't normally do this, but a friend gave me a little Leapster game. It's one of these... I had no idea what it was, right? It's one of these little kids, Game Boy-type games, but it's actually designed for, you know, babies kind of, you know, up to five or something. Yeah. You know, it's got an LCD screen and the plug-in cartridge and it's got sound and, you know... Yeah. It's got games called Doodlebug and, I don't know, something like that.

**Chris Gammell:** Yeah, and it probably cost them, like, you know, $4 to make and they charge parents, like, 50 bucks for it. Yeah.

**Dave Jones:** Anyway, you know, it's quite rugged, designed for kids to, you know, young children just to throw around and all that sort of stuff. Yeah. And, anyway, the speaker had died in it, so I thought, yeah, okay, I'll take a look at it. That's kind of like an easy kind of fix. So, yeah, I opened it up. Sure enough, the speaker had died. It's one of those little 20-millimeter, you know, inch-wide, you know, mylar cone, tiny little speakers, you know, what's the... I don't know, what's the word? You know, one of those little... A tweeter? Flat, miniature speakers, right? Oh. Yeah, it's not a huge thing with a massive, big magnet protruding out the back and a big cone and all... Yeah, it's a tiny little one-inch-wide thing. Anyway, so I couldn't get... And it's mounted in a fancy mounting thing that's custom-molded into the case and all that sort of stuff. And I couldn't... I didn't have a spare one of the same size. And I only had a smaller one, which was 20 millimeters instead of 25 millimeters or something like that. So it wouldn't fit in the custom-molded bracket inside the case. And I'm scratching my head, how can I hold it in there? Oh, hot melt glue, I don't know. You know, super glue, I can sort of wedge it in there. And it was looking real nasty, actually, trying to hold this thing in there. And I knew that if I glued it in, you know, kids throwing it around, it would eventually just, you know, snap off or something like that. And it'll rattle around inside and it'd be crap. So I got the idea just to keep the existing speaker in there, right? And there was actually a big volume of space on the front cone of the speaker. And I just got the other speaker and I put it in front of it. And well, speakers got magnets, right? And these little tiny ones, as it turns out, they're incredibly powerful. And I put it on there and it went, you know, thump. And it actually stuck the two speakers together. So all I did is just mount the speaker on the front of the other one with its magnet.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, that's it. And so I didn't need to mount it there. I didn't need to glue it in. I didn't need to hold it in place. The magnet will automatically keep it in. And if it falls off for some reason, if they're so violent that it overcomes the magnet and it actually falls off, well, it's only got a little volume of space and it will automatically flip back and the magnet will pull it back in place.

**Chris Gammell:** That's a heck of a fix, man.

**Dave Jones:** I call that a win. That's a hack. Yeah. Yeah. Sometimes you just win like that. You know? It's just...

**Chris Gammell:** Yeah.

**Dave Jones:** I love it. I didn't take a photo of it or anything. I should have. But yeah, just imagine...

**Chris Gammell:** You said before you usually try and get away from this, you know? Like you try and usually avoid. Oh, I try and avoid, yeah. Nothing worse. So how'd you get suckered this time? That's what I want to know.

**Dave Jones:** Oh, I don't... Well, they came over and they said, oh, we've got, you know, I didn't have... I didn't have time to, you know, divert it. And it was an easy one, so...

**Chris Gammell:** Yeah. Well, that's good though, man. That's a good fix.

**Dave Jones:** Yeah. I thought that was cool. I didn't have to mount it. Magnet takes care of it.

**Chris Gammell:** I mean, you'll have to do that probably a lot more soon too. I mean, as your kid grows up, he'll probably break stuff all the time, but then you can... Ah, right. And I'll be fixing shit. Left, right, center. You can make him go and fix it. Fix it yourself, son.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Tools are out there. Are you a maker or a breaker? That's what you can say to him.

**Dave Jones:** Right.

**Chris Gammell:** Speaking of, there's...

**Dave Jones:** Hey, that's a t-shirt slogan. Yeah. I'm a maker, not a breaker.

**Chris Gammell:** That's good. I like that.

**Dave Jones:** There you go.

**Chris Gammell:** Yeah. Cool. Speaking of, there was a PBS segment on making, on the maker movement at least. It was Dale Doherty, the guy from Make Magazine, and they were kind of showcasing actually a bunch of the, you know, a bunch of the shops and everything.

**Dave Jones:** Right.

**Chris Gammell:** They were talking about maker fear, obviously, but, you know, just kind of like, I really like what Dale said about it, too. He said he liked it as a subversive educational tool. I thought that was...

**Dave Jones:** Right, yeah, okay.

**Chris Gammell:** You know, way to get kids to...

**Dave Jones:** The wank words come out, yep.

**Chris Gammell:** Well, I don't think that's that bad, you know, like...

**Dave Jones:** No, no, it's not. I don't mind that word, subversive. It's, you know.

**Chris Gammell:** Yeah. I don't know. I think that's good, though.

**Dave Jones:** Yeah, it's trying to teach them stuff, but do it in a way that they think they're not learning. Right. Because when you try and force... You know, when kids know, oh, I've got to learn this, then they switch off, you know?

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** But when they go, oh, I'm just playing fun, you know, that's the holy grail of learning, is to make it fun, really. That's been, you know, the thing from Day Dot with any toy, I guess, any learning tool. You know, back from my 50-in-1 kits that everyone learnt electronics on, right? They were designed to be fun, not just, you know, some boring piece of crap. They made building stuff fun and easy, and then you learn stuff along the way, and you didn't even know it sometimes. Yeah. So, it's great. I love it.

**Chris Gammell:** Yeah. So, it's... I think that's the way to do it. I mean, obviously, we like hackerspaces here on the App Hour, so that's a... You know.

**Dave Jones:** Right. I just used my mute switch, did you realize?

**Chris Gammell:** I did not. I did not hear that. I didn't hear it at all. There you go.

**Dave Jones:** Well, that's why it's called a mute switch.

**Chris Gammell:** I just used it and cussed you out right there. Okay. Brilliant. Dave, you... Beep. And... And... Beep. Beep. Yeah.

**Dave Jones:** Boy. Speaking of... Well, nothing.

**Chris Gammell:** Speaking of nothing. I just want to do. Chicks. Speaking of things to swear about and silly ideas. Yeah, exactly.

**Dave Jones:** Oh, yeah. We always swear about this one. Chicks in engineering marketing, again. Yeah. PCBpool.com. Yes. Go to their web... Well, you know. Go to their website and check it out. You don't want to give them the link.

**Speaker ?:** Right.

**Dave Jones:** They've got a new advertising... It's not really a logo. It's just a... Anyway, it's a picture of a woman there with a really big...

**Speaker ?:** assets.

**Dave Jones:** Assets. And... Bust. ...covered by, well, what? Molten solder, I guess you could call it. Very... Madonna-like. Yeah.

**Chris Gammell:** Yeah, meant to be alluring. Yes.

**Dave Jones:** Yes. And she's holding up, presumably, a circuit board across her stomach. And it's just... And it looks like she's got an outfit of, like, solder on.

**Chris Gammell:** Right.

**Dave Jones:** And it's... Come on. I mean... What does that do?

**Chris Gammell:** Well, it sells boards. Duh. Right.

**Dave Jones:** Obviously, it sells boards, right?

**Chris Gammell:** Yeah. I don't know about that one.

**Dave Jones:** You know we hate that shit here. Yeah.

**Chris Gammell:** Yeah. How'd you... It's crazy. You were just using this service or something already? Saw that?

**Dave Jones:** Me?

**Chris Gammell:** Were you using PCBpool or no?

**Dave Jones:** No. No, I haven't used it. No.

**Chris Gammell:** No. I just wonder how you saw this. You're just, like, cruising the internet looking for...

**Dave Jones:** Hey, it was... Somebody tweeted it. So, I think it might have been Art of Fruit or somebody. Oh. Like that. Oh, gotcha. Yeah. Yeah, they found it and... Yep. I think they were having, like, a logo. Not a... Yeah, like a... Like a... Caption kind of contest, you know? Make up a caption for this stupid image of this woman holding the circuit board with the Maltons... With the solder-like shiny outfit on. Yeah. Ah, please.

**Speaker ?:** Yeah.

**Chris Gammell:** That's... That's too bad.

**Dave Jones:** Yeah. Thumbs down. It's pathetic. We hate that shit. It's not the 1970s and 80s, you know? Right. Where all that stuff was the rage in the magazines. If you open your electronics magazine... Yeah. Yeah. Yeah. Every ad would have a woman in it. So, it was just nuts.

**Chris Gammell:** Yeah. Speaking of other board houses, though, there was a... Maybe one that doesn't advertise with, you know, sexist marketing. There's a... Right. A tour of advanced circuits. I don't know if you ever use those guys.

**Dave Jones:** But there's a... No, I haven't.

**Chris Gammell:** I've used them before. They're all right. And... Yeah. It's not loading, of course, for me. But there's a picture tour. Someone went through and actually... Yep. I can see it. Oh, you can? No. I guess you'll have to describe it.

**Dave Jones:** They've got a picture of every step in the process by the looks of it. Like the bare... You know, from the bare boards and the bare cores that go into the multi-layer ones. And... Yeah. It goes right through the process.

**Chris Gammell:** Yeah. It's a lot bigger than I thought it would be. You know, I don't know why I thought it would be like a small process. But, you know, it's definitely like, you know, large capital equipment kind of stuff. You know, doing lithography and a lot of... Like liquid baths and everything. But that's how they push braces down, you know? No... Yep. Not needing any kind of human interaction or anything like that.

**Dave Jones:** Yeah. So, it's cool. I love the drills. I love the tray of drills. It almost looks like a tray of candy. All these colored... Yeah. These drill bits aren't just a drill bit. They're actually stuck into like a colored holder kind of thing. And it just looks... It looks quite funny. Drills and routing bits and stuff like that. Yeah. Yeah.

**Chris Gammell:** Have you ever been to a large scale place like this that actually does this kind of thing?

**Dave Jones:** I've never been to... I've been to PCB assembly places, but I've never been to a PCB... Yeah. ...a bareboard manufacturing place. Yeah. So, I was... I was possibly going to do one as a tour for the blog. Oh, okay.

**Chris Gammell:** Okay.

**Dave Jones:** Hopefully. There's one in Sydney. It's not large. And in fact, it's a small backyard operation. So, maybe that gives you a different... Yeah. Maybe a different spin on things. I don't know. Maybe I can... Well, you were talking about...

**Chris Gammell:** You did that one video when you were leaving Altium, didn't you? Just a picking place, right? I mean, that wasn't anything...

**Dave Jones:** Oh, that was just a solder paste... Solder paste dispenser.

**Chris Gammell:** Oh, that was just solder paste? Okay.

**Dave Jones:** Yeah. Yeah. Okay.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. No, not actual PCB assembly. But yeah, there's the etchant baths and everything. And it's just... Yeah. It's a big industrial... It's a really complex process. Very... Lots of steps involved in manufacturing a board, especially a multi-layer one, if you've never actually gone into it. That's why they've got six pages of each... Yeah. Yeah. Of a photo for each process here. It's like... You know, because there are a lot of steps. Especially when you've got to not only etch it, but then you've got to assemble boards. You've got to do the plate in. You've got to do the solder mask, the silk screen, and the routing, and the... You know, there's a lot of steps involved.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** We had someone ask, actually, on last week's episode page, and asking about, do pick and place machines actually solder the components as well, or do they just place them? And so that would be the next step, obviously.

**Dave Jones:** Oh, well, you can get sort of combined machines, but usually they sort of go from a conveyor. They're all... The machine's like a joint together. You can see this in one of my videos. Yeah. They're joined together on a conveyor belt. So you put the board in one end, and it literally goes into a solder paste dispenser. Then it moves into the pick and place machine, and it looks like one big, long machine, really. Yeah. Yeah. Because the machines are all, you know, tied together, but they are physically separate. Then the pick and place, and then it goes into the reflow oven, and then to the automated visual inspection, and then pops out the other end.

**Chris Gammell:** Yeah, that's how they kind of do it. Yeah, but they are separate machines. A lot of photolithography, so if you're actually doing wafers, too. I've never worked on the actual machines, but, you know, if you look at it, it looks like this monstrous machine, but it's actually like three or four different machines all stuck together. You know, one where it actually spins it on, then they bake it, and then they actually do the exposure, and then they rinse it, and this is all... And then finally, just all the wafers pop out with all this, you know, pattern resist on them. And that's actually what you want. Take an etch.

**Dave Jones:** Yeah.

**Chris Gammell:** For others, semiconductor units.

**Dave Jones:** I just love these processes, and really, it just goes to show that you really cannot compete making your own boards at home. You know, everyone talks about, oh, making your own boards at home, and it's like, well, yeah, you can make double-sided, non-plate-through. Maybe plate-through if you're... The plating is tough, yeah. You know, it's a tough process, and well, when you can get stuff from these sorts of companies, you know, we've talked about this, PCBs are just dirt cheap these days, so...

**Chris Gammell:** Yeah, they're getting cheaper, too.

**Dave Jones:** You know, really, people persist in making their own at home, and really, the only advantage is if you need it in the next couple of hours. Right. Apart from that, it's just... Nah. Sorry.

**Chris Gammell:** And you're going to keep it on one side, too. That's another thing that usually helps. Yeah. Because that is kind of tough. But I mean, yeah, like, so, you know, like some of Jerry's videos she shows, and she's always doing the, like, over-the-weekend kind of work where she needs it right away. Yep. So if you're...

**Dave Jones:** Oh, I've done the same thing myself. Yeah. I used to make my own boards.

**Chris Gammell:** Yeah.

**Dave Jones:** Used to do it all the time, and it was great, because you had it within an hour or something like that.

**Dave Jones:** I could literally have a board within the hour, but...

**Chris Gammell:** Yeah. And if you mess it up, too. Yeah. That's the real key, right? Is if you mess it up, and then you... You can redo it in another hour, or, well, a couple hours. Exactly. Yeah.

**Dave Jones:** So... I don't know. But they are very basic, and, yeah, it's... I don't know. If I'm going to do that, I may as well build the circuit up on breadboard or something, you know? Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Not only breadboard, but veraboard or stripboard, you know, something like that.

**Chris Gammell:** Well, yeah, but that's a little tougher now with, you know, surface mount components and everything.

**Dave Jones:** With surface mount, it can be. Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Well... Anyway, but then if you've got very fine-pitched surface mount stuff, and you're trying to do your own boards, then you don't have the solder mask. Right. And... That's tough. As you should know, as will probably be in my next... As will be in my next soldering video, little plug there, will be... That solder mask is everything when you're doing these fine-pitched SMD stuff, because it allows you to do drag soldering and all sorts of stuff, and you don't get shorts between your pins. Yeah. Whereas if you've got your own homemade board with no solder mask, well, you know, if you're trying to solder a 0.5-kilometer pin-pitch part, good luck, you know. Yeah. It's a pain in the ass, so...

**Chris Gammell:** You can do it. You'll just be there a while.

**Dave Jones:** No, you'll just... Yeah, it's just messier and... Yeah. ...not nearly as nice.

**Chris Gammell:** Yeah.

**Dave Jones:** So...

**Chris Gammell:** Oh, that tour of the lab, or that tour of the manufacturing facility is really cool, though. So people should definitely check out the pictures. Yeah, I like it. It's definitely worthwhile. And since we're on the... I mean, since we're already here, we might as well... I mean, we've got two items here about at-home printed electronics. We might as well just... Oh, please. We might as well. I mean...

**Dave Jones:** You're not going to talk about this conductive ink pen, are you?

**Chris Gammell:** Yeah. Yeah, I was going to.

**Dave Jones:** I'm sorry. Right? This just came out. It's a news item, right? That somebody has... Two researchers have developed a conductive ink pen where you can write, and it puts down silver, right? It's a silver-loaded thing. It's a silver, yeah. Silver-based ink. I'm sorry. This has been around forever. You can buy them. I can walk into my J-car store and buy a conductive pen. Yeah, but... What's new here? I don't understand. What's new here? It's like a big news item. All these researchers have developed a conductive pen. You've been able to buy them forever. I'm sure I've seen them 20 years ago. Yeah, but... Please correct me if I'm wrong. When was the first conductive ink pen done?

**Chris Gammell:** Well, hell if I know, man.

**Dave Jones:** Hell of a long time ago.

**Speaker ?:** No.

**Dave Jones:** It's not new. I'm sorry. I don't get what's new with this one. Maybe it's... And they're talking about writing on flexible surfaces. Well, J-car advertised their one. It's not new, but if it's a commercial thing, right?

**Chris Gammell:** So if you could do it... Why? You know, you could do it with... You know, if you developed your own ink, but maybe they didn't sell it, right? Were you actually able to buy it back then? The pen.

**Dave Jones:** Yeah, you could buy the pen. That had conductive ink. There's quite a few manufacturers who make them. It's not new, and I'm sure they've been around for a long time. I wouldn't like to put an exact date on when I first saw them, but I know it's a long time ago. It's not a new concept to have a conductive ink pen. All right, next item. They use them in repair of circuit boards. If you've got a... You know, if your track's blowing off, you can actually draw on your conductive ink trace, and you can actually do it like that. That's not the best way to do it. Usually you would use, like, a tape. You'd use a copper tape, an adhesive copper tape to repair your board, but some people do it with these conductive inks and stuff like that. But anyway, sorry, nothing new, unless I'm missing the...

**Chris Gammell:** I'm trying to see what's different than maybe it was before.

**Dave Jones:** And you're going to make the stretch, aren't you, that this is one step away from printable electronics. I didn't make that stretch.

**Chris Gammell:** No, what I'm saying is that you can... It's a good start. It's a good start.

**Dave Jones:** Oh, please. I don't even know where it's... I cannot laugh enough. How about this?

**Chris Gammell:** If you think about it like this. So, we talked about Evil Mad Scientist Laboratories before, right? So, they have another product called Eggbot, right? And that just has a pen input. You could do... I mean, granted, it's on a round device, but you could do... You could at least start with a home-fabbed, you know, conductive baseball. That'd be kind of cool.

**Dave Jones:** To what end?

**Chris Gammell:** Well, it'd be a...

**Dave Jones:** It'd be a large scale still. It'd be a baseball with conductive ink on it.

**Chris Gammell:** Yep. It'd be a large scale.

**Dave Jones:** I'm sorry. I'm just not seeing how this leads to your home-printed chips thing. You've got to be kidding me. That's where you're going to. I'm sure that's where you're going to. Printed. In fact, you've got it under the show notes as printed electronics.

**Chris Gammell:** I do, yeah. Yeah? So, well, I mean, if you could get it into a thermal print cartridge, you could get it into finer resolution, right? You think about it as a pen, that's different because you need the mechanical accuracy. But if you could do some kind of spray-on or, you know, transfer method. I'm kind of reaching right now. I realize that.

**Dave Jones:** That's the sound of Chris reaching extremely far.

**Chris Gammell:** All right. Shut up. Sounded good at first. All right. How about the second one? So, this is another one. Carbon nanotubes. So, this is a Spectrum article. So, carbon nanotubes suspended in a liquid are now in ink. And this seems a little bit more likely as a printable ink kind of thing. So, if you had, you know, you created nanotubes. You chop them all off. You suspend them in a liquid. And now you have this ink that you could then use to print gates, basically, for creating transistors.

**Dave Jones:** Right.

**Chris Gammell:** So, what do you think about that one?

**Dave Jones:** Nanotubes sound very much like something you can't do at home.

**Chris Gammell:** No, but if you, you can, you couldn't make the nanotube liquid, right? So, if you had nanotubes suspended in liquid, you'd buy that as a cartridge or whatever else.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Now, granted, you do need a substrate, a source, a drain, a gate, you know, everything else still. But, your oxide, you would make a sick-ass transistor. Because this would be acting as the oxide, basically.

**Dave Jones:** One whole transistor. That's right. But an awesome one. Yes.

**Chris Gammell:** Like a 10 gigahertz transistor.

**Dave Jones:** Man, you can do so much with one transistor.

**Chris Gammell:** Actually, you can. You can do a lot of stuff with one transistor.

**Dave Jones:** You can do an FM transmitter with one transistor. Exactly.

**Chris Gammell:** Exactly. You could have a 10 gigahertz FM transistor.

**Dave Jones:** I know.

**Chris Gammell:** There you go.

**Dave Jones:** What we need to do is add a tank circuit. It's a shame that the tank circuit is about a million times bigger than the actual transistor driving it. That's too bad. But, you know, that's details.

**Chris Gammell:** Well, maybe at a gigahertz, you don't need it to be that big.

**Dave Jones:** Oh, true.

**Chris Gammell:** Anyway. And so you can pick up a gigahertz on your radio. I'm not saying we're there yet, Dave. I'm just saying these are all the pieces. They're just falling into place. It's falling into place. Right. Oh, boy. We're getting there, buddy. We're getting there. It's a slow, slow transition.

**Dave Jones:** And I never said we wouldn't get there. I just said it's not going to be a revolution when you do.

**Chris Gammell:** Fine. Whatever.

**Dave Jones:** Yeah. Dude, you're on the losing horse. I know. You can just picture Chris there riding his dead horse, just flogging this thing, trying to ride it home.

**Chris Gammell:** Just because I have a dead horse does not mean... It's not a dead horse. He's just hobbled. He can catch his final wind. He can catch a second wind. Right. We have kill switches now. He can pass wind. Fine. Fine. Fine. Fine. I'm done for this week. Don't think I'm stopping now, though. It's going to keep...

**Dave Jones:** That's fine. It adds humor and laughter to every episode, every time you bring it up.

**Chris Gammell:** To you. Yeah.

**Dave Jones:** I love it.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, data sheet of the week. Data sheet of the week. Ta-da.

**Chris Gammell:** Okay. So this is not chip of the week. This is data sheet of the week.

**Dave Jones:** This is not chip of the week. This is data sheet of the week. All right. Ta-da. What do you like about this thing? It's not new. I even remembered that. I think I've possibly seen it before. But anyway, I was searching for a project case the other day, as you do, which can take all day to search for a decent project case. It's got to be the right cost, exactly the right size and form factor and the features you want. Material, yeah. Anyway, there's half a dozen... Well, there's probably three or four major case manufacturers out there. And I went to Hammond, which are a manufacturer. I'm not sure where they're based. I think it might even be England. Or something like that. I don't know. And they make some really cool cases. And I'm downloading their data sheet. And instantly, it popped up. You know, the PDF opened up. And this is not new, but it started to have a 3D... There was a 3D model of the case there, and it started to rotate. It was an animated PDF. You know, which these aren't new. The animated... The capability in PDF has been there for a while. To have interactive, you know, 3D models inside, embedded in a PDF. But it was just awesome. Okay.

**Chris Gammell:** So you have to open it in Adobe or some other kind of reader.

**Dave Jones:** You've got to open it. Well, it opens in my browser, but I've got, you know, Adobe Acrobat. It may not open in others.

**Chris Gammell:** I use Chrome and the native... It has a native reader.

**Dave Jones:** Oh, right. No. It doesn't rotate there. So that makes more sense now. Right. That's... Yeah. So you've got to have Acrobat. And it rotates. And then you can interact with it. You can zoom in. Oh, wow. Zoom out. You can actually select items. I can select the... I'm doing it here. It doesn't work as well on radio. But I can select the bottom part of the case.

**Chris Gammell:** Oh, nice.

**Dave Jones:** And it's just...

**Chris Gammell:** That's fancy.

**Dave Jones:** You know, it's fantastic. You can rotate it around, view it from any direction.

**Chris Gammell:** How do you have to stop rotating?

**Dave Jones:** And it shows the expanded... You know, it shows the screws going in and an example PCB inside the case.

**Chris Gammell:** Yeah.

**Dave Jones:** Ah. Just nice. That is nice. Brilliant.

**Chris Gammell:** It won't stop rotating.

**Dave Jones:** And I love companies that have downloadable 3D models for their cases as well. So...

**Chris Gammell:** Yeah, you're all about that.

**Dave Jones:** That's great as well. But yeah, this was just a nice touch. I thought it was brilliant.

**Chris Gammell:** That's cool, man. I didn't realize that because I clicked on it before, before we started. And I was like, oh, okay. It's a 3D model, but...

**Dave Jones:** Okay. So you can see it now, can you?

**Chris Gammell:** Yeah, I'm actually, you know, scrolling in and out.

**Dave Jones:** And you can zoom in, zoom out. Just use the center mouse wheel and you can... Yep. And then you can rotate, hold down the left button and zoom. And then you can actually select something. Like, I can select the PCB and it turns red and...

**Chris Gammell:** Ah. That's cool. Yeah. Yeah, people should try that out.

**Dave Jones:** Yep. And I'm sure there's other companies with 3D models in their data sheets like this. Yeah. But that's just awesome. So that makes me want to buy Hammond cases. Yeah. It's a shame that case didn't meet my requirements. But anyway, I don't know if they've updated all their data sheets, but that one I happened to see had that really cool feature in it. I love it. I'm sure they will eventually have every single data sheet if they don't already. Yeah. The 3D models.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh.

**Chris Gammell:** That's cool.

**Dave Jones:** Everyone should have that. Granted, you can't have that for a chip or something like that, you know. But you could. It'd just be moot. I mean, you wouldn't. Maxim chip, you know. It's like, eh. No, because it chews up system resources. You know, if you've got 20 data sheets out, and the last thing you want is for 20 3D rotating models going in the background, chewing up all your system resources and stuff like that. And then people start. But you can actually turn it off. You can actually left click. Sorry, right click and then choose disable content. And presumably it doesn't take up any more resources.

**Chris Gammell:** Yeah. That's cool.

**Dave Jones:** And it hasn't interfered with Skype yet, so I don't know. Can't be using too many resources. But I can imagine if you've got 20 data sheets open, you could be screwed.

**Chris Gammell:** So who do you usually buy? I mean, like, do you buy project boxes for most of your stuff or what?

**Dave Jones:** Yes. I try and design all my projects around an off-the-shelf case because there's nothing better than using an off-the-shelf case. You know, if you need a custom case for something, you've failed, I think, as far as I'm concerned.

**Chris Gammell:** Yeah, that makes sense. I mean, well, you don't fail, you're going to pay for it, though.

**Dave Jones:** If a custom case is absolutely required... You're just going to pay for it. You bet you've got to pay for it. Yes. You know, and then you've got to... And then it's a pain in the ass to prototype. It costs you money to prototype and time.

**Chris Gammell:** Yeah.

**Dave Jones:** And there's extra risk there. And, nah, it's just... Right. ...so much easier to actually design your product around an off-the-shelf case. Yeah. So that's why every time I come up with a new project idea, which is practically every week, I'll spend a whole day just looking through, finding a suitable case. And then I'll base my project around that. Yeah. And then my thing... Then the project may even change based on what case I can get. Okay. I can get... I love this size case. It's the right price. It does everything I want. But I can't have, you know, four connectors on the front instead of three. Okay. Well, I'll change my project spec to three to make it fit. That's good enough. And, yeah. So I'm very flexible in my projects to make them fit around the case. The case is almost everything sometimes. Yeah.

**Chris Gammell:** So do these case manufacturers, do they give you the 3D model? Do they also give you, like, the board outline to get started with?

**Dave Jones:** Yes. Yes, they do. Oh, that's nice. Well, not in a PCB package, but they give it to you as a DXF or something like that sometimes, which you can import. Yeah. Yeah. So... Oh, cool. Yeah. It's great.

**Chris Gammell:** I love it. I was surprised when I was out in Silicon Valley at that show, and I went to the... Oh, crap. I forgot the name of it now. It was, like, a surplus electronics store. But I was amazed. They just had, like, two rows just full of these things, you know? And they were great. I mean, just being able to go to... I can't even imagine being able to go to the store and just pick one up, you know? It's like, oh, well...

**Dave Jones:** Yeah.

**Chris Gammell:** Because eventually you could jury rig one into... You know, if you had a project, you're like, yeah, it needs to be big enough to fit this board I made. Well, you could just go... It wouldn't be optimal, but you could go pick one up.

**Dave Jones:** Yeah. You could just... Yeah, I've got a whole bunch of cases sitting in the cupboard, you know? So if I need to make a one-off, then I'll just go choose one of my cases I've got off the shelf kind of thing, so...

**Chris Gammell:** What's your usual price range for these kind of things?

**Dave Jones:** Oh, these are, like, a few dollars. It basically depends on size. These... A small one, like this one, is only, I think, three bucks or something like that.

**Speaker ?:** Oh, nice.

**Dave Jones:** Nice. And that's in, like, one-off, I think.

**Dave Jones:** You know, 100-off quantities. Really? So that really enables your project. Why you would do a custom case? It's... You know, is... You know, that would be a last resort kind of thing. If you want to get into the kit business or selling projects or something like that, there's tons of these really nice-looking, well-engineered cases that, you know, they have battery compartments and battery doors and front panels that you can do as PCBs and stuff like that. And it's just... They're so flexible.

**Chris Gammell:** Yeah. That's great.

**Dave Jones:** Yeah, I love it. So, really, if there's a little top tip for you, if you're trying to design your own... Getting into the kit business, use an off-the-shelf case.

**Chris Gammell:** Yeah. And that's true. I mean, not just for cases either.

**Dave Jones:** Otherwise, you end up like poor old Hitch Altman, who spent $30,000. Uh-huh. We've talked about this before. $30,000 getting his little TV Begone thing on the market, right? Because he did a fully custom case for it and everything.

**Chris Gammell:** Uh-huh.

**Dave Jones:** Yeah, it's crazy. Well, if you have the money and the time to burn, sure.

**Chris Gammell:** Yeah.

**Dave Jones:** Go for it. Do a custom case.

**Chris Gammell:** But, nah. Use an off-the-shelf. It's kind of like what we talked about. I think it was last week we talked about that, too. Just, you know, like...

**Dave Jones:** I think we did.

**Chris Gammell:** We were talking about with chips about, you know, like, trying to design around chips that already are big in the market, so you get that cost reduction. So, that's...

**Dave Jones:** And that... The reason I mention that is because some people on the forum are trying to design an open-source multimeter. Oh, cool. And I just done a video. My latest video is my concept for an open-source multimeter. And, um, as a response to their thing, you know. And that's sort of, you know, something you've got to do a custom case for. Yeah. And, really, I... You know, you can easily underestimate how much effort is involved in doing a case. Not just a case, but the buttons and the battery compartments and everything else that, you know, the range switch if you're going to need it and all that sort of jazz, you know, that goes into a case like that. Yeah.

**Chris Gammell:** Yeah. Yeah, it's tough, too.

**Dave Jones:** I mean, like... It's a tough business.

**Chris Gammell:** Yeah, trying to estimate all those costs up front and everything, too. You're never going to get it right. So, you're always going to have to pad the numbers and...

**Dave Jones:** Yep.

**Chris Gammell:** So, that's too bad.

**Dave Jones:** Actually, somebody asked this on the forum. I saw it last night. It's not on the list here, but I'll bring it up. But with these Kickstarter projects, which is what this open source multimeter is going to be, right, what happens when it reaches its target, raises the money, and then you find, oops, we can't make it for that price? Has that happened? I'm sure it must have.

**Chris Gammell:** Oh, like actual money? Like, they just totally underestimated costs and everything?

**Dave Jones:** They totally underestimated the amount of money it would take to actually fund that particular project.

**Chris Gammell:** Yeah. Is it like a chunk out of their money, out of their wallet, right?

**Dave Jones:** Yeah. Oh, yeah. What happens? Do people get their money back? Do they just fold and everyone's lost their money? Or what happens?

**Chris Gammell:** I don't know.

**Dave Jones:** Does anyone know? Is there any... Is there a history of that actually happening or what? Because a budget, you know, you always... Engineers are notoriously bad for underestimating not only time, but money as well. So, it's a really tough gig.

**Chris Gammell:** Yeah. That's... I mean, that's kind of tough, too, because it's like with, you know, what the whole site was envisioned for at the beginning was like, you know, like musicians. That's what I always think of as like the main example, right? Right. And you know your costs up front. It's like, okay, we're going to need two weeks in the studio. That's going to cost, you know, $2,000 and whatever. And after that, it's like, well, you just kind of crank it out.

**Dave Jones:** Even that, you could underestimate easily. You can go, oh, yeah, I can do that in two weeks. But really, you just end up, you know... Yeah, but you could... Eating pizza and drinking beer for two weeks and you don't end up doing anything. Okay.

**Chris Gammell:** Yeah, that's true. I mean, I guess in that case, it'd be if you spent that money, unless you like lost the money, right? Like, you could just put out a two-song LP or whatever.

**Dave Jones:** Right.

**Chris Gammell:** You can't put out, like, just a case for an L multimeter, you know? Like, it's like if you're... Yeah. If it has to be a functional multimeter, it's like, well, that's...

**Dave Jones:** Yeah, that's... I know. It's a...

**Chris Gammell:** There is kind of like a minimum thing, a minimum situation you need to meet in order to actually have a product that works, so...

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. There's a link on the Kickstarter blog called, sometimes Kickstarter projects don't make it. Right. Yeah. Wow. That is crazy. I don't know if these are... I haven't read these, so I won't read them online, but... Or on the air, but man. Yeah, that is a good question. I don't know. I'm sure you feel like crap.

**Dave Jones:** Yeah. Yeah. I should want to run away and, yeah. Yeah. I'd change your name and... Yeah. Sorry, dudes. I've pissed away all your money. Yeah. It's gone now. I've got nothing to show for it.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And that's why I'd never do... I don't take people's money. You know, that's my golden rule in business is that, you know, I spend my own money, do it, and then I don't owe anyone anything. Yeah. You know, when you've taken people's money and you owe them something, then, you know, that's really tough.

**Chris Gammell:** Yeah.

**Dave Jones:** So... Yeah. Some people thrive on that. They have no aversion, you know, they have no aversion to that risk, you know, of actually doing that.

**Chris Gammell:** Like buyer beware and everything.

**Dave Jones:** Yeah.

**Chris Gammell:** I just forget the Latin word for that, or the Latin phrase for that.

**Dave Jones:** I just can't do it. I can't take people's money and then promise something. I just hate doing that.

**Chris Gammell:** Mm.

**Dave Jones:** Keeps me awake at night. Don't like that.

**Chris Gammell:** You took my money. You take my money once a month for your donation program.

**Dave Jones:** Oh, right. Wow. Paid all this money and all I get is these EEV blogs. That was a buyer beware, wasn't it? Yeah.

**Chris Gammell:** Yeah. People should donate. Support Dave.

**Dave Jones:** Yes, please. Yeah. I don't have a job now.

**Chris Gammell:** Yep. Poor Dave. Poor Dave.

**Dave Jones:** Yeah. And I've got a screaming wife and child.

**Chris Gammell:** Hopefully the younger one screams more than the older one. Right.

**Dave Jones:** Yeah, I think so. But anyway, it's a good joke. Yeah.

**Chris Gammell:** So I wanted to mention this. There's a Bill Schweber article from EE Times. He actually talked about, he went to this big thing from TI, Texas Instruments. They had like this big conference down in Dallas. And it's interesting, he wrote about all the markets. Well, first off, Texas Instruments, they didn't invite the amp hour. I don't know why. I mean, come on, guys. What are you doing wrong here? Bastards.

**Dave Jones:** We're bigger than EE Times. Come on. Yeah.

**Chris Gammell:** Right?

**Dave Jones:** We are the biggest out there. We're the biggest radio show on the, electronics radio show on the internet.

**Chris Gammell:** We're the biggest something. Yeah. We're the biggest pieces of, biggest bullshit artists on the internet. I just muted myself there. There we go. Right. Anyways, it's an interesting article.

**Dave Jones:** We are a reputable program, are we not?

**Chris Gammell:** I wouldn't call us that. Anyway, he touched on some of the industries they're going for. And this is kind of interesting, kind of hearing it from their mouth of what they're going for. Because, you know, you kind of wonder about where electronics really want to go in the future. And everybody tries to predict that. But you can only predict it as much as the chip fabs and the designers want to actually do something, right? So. Yep. So some of the things, some of the things were, you know, interesting. Some, some just are, some don't make any sense at all. But anyways, here, here's a list real quick. So medical electronics, duh. Touch and haptic feedback kind of stuff.

**Dave Jones:** Yeah, that's big at the moment. Everyone's doing touch.

**Chris Gammell:** Yeah. Although, I would, I would take, well, I'll go back to that one. Uh, microcontroller based digital power control. So basically, instead of having like a little, you know, power switcher chip, you'd have a micro that's actually, you know, having comparators and everything else. And there's already kits out there for that kind of thing.

**Dave Jones:** Nothing's floating my boat yet.

**Chris Gammell:** No. Uh, a lot of renewable energy stuff. A lot of the LT chips do already do that stuff.

**Dave Jones:** Once again, that's a, yep. Yeah. That's a hot topic. Every man with his dog's doing energy harvesting and stuff like that. Yeah.

**Chris Gammell:** Smart energy.

**Dave Jones:** Smart, smart grid. Smart grid. Sorry, yeah. That stuff. Which granted will be quite big, but yeah, I just, a bit sick of hearing it now. It's a bit passe.

**Chris Gammell:** Yeah. Uh, motor control.

**Dave Jones:** It'd be something exciting. Where's robots?

**Chris Gammell:** I think that'd be motor control. Yeah. Advanced motor control. So if you have like multiple, you know, stepper motors driving like an arm, a robot arm or something. Uh, sound bar electronics, data acquisition ICs, and super speed USB transceivers. So all that stuff is pretty boring. Uh, nothing really too shocking.

**Dave Jones:** It is. No. What happened to USB 3? Has it actually trickled into machines now? It probably has, but there's all this big hoopla over it and everyone just went, uh, yawn. Uh, big deal. USB 2.0 is good enough, you know? Well, I think they got, they got overshadowed by Thunderbolt. It's kind of, it's probably just a niche thing, right?

**Chris Gammell:** It's a what?

**Dave Jones:** A niche. Oh, yeah. I, I've. Not niche. Sorry.

**Chris Gammell:** I think right now, there's a couple people that actually make USB 3.0 like transceiver chips, but it's not rolled into actual like, so if you buy a micro, you need, you're not going to really buy that, right?

**Dave Jones:** Oh, no, because it's really advanced stuff. It's really.

**Chris Gammell:** Right.

**Dave Jones:** You know, it's hard enough to put a USB 2.0 transceiver in a micro control, let alone a 3.0.

**Chris Gammell:** Right. And they're throwing those at everything now, right? So every time, now they have the silicon already done.

**Dave Jones:** Now they, yeah, they've got it down pat. 2.0 is now down pat. It's common as mud and it's dirt cheap.

**Chris Gammell:** Right.

**Dave Jones:** But 3.0 is, yeah.

**Chris Gammell:** I think another problem though is the fact that, you know, you need like a leading edge chip manufacturer to actually start doing this so there's demand picks up, right? Like how do you actually push demand versus, you know, what people need? And one of the biggest ones, Intel, they didn't do it because they have their own standard now. They do Thunderbolt.

**Dave Jones:** Oh, really?

**Chris Gammell:** Okay. So that's, it's on. I haven't heard of that. It's in Apple products and it's got a special cable and everything else and it does like 10 gigabit per second. Of course, yeah. But. Wankers. Now it's not open, right? So we'll screw them, right? I mean like so. Right. Yeah, exactly. So now it's, it's a matter of the biggest computer manufacturers in doing this and so now it doesn't push it down into the embedded world, right? And so I think it's kind of stagnated, which sucks, but.

**Dave Jones:** Yep.

**Chris Gammell:** I mean, but I think it's what you said too, like USB 2.0, it's kind of good enough still for, for now. I mean, this is talking about.

**Dave Jones:** It's good enough. I can only picture like niche, maybe high speed video or something. If you need to do that, would you need to go to five gigabits per second or whatever the transfer rate of USB 3 is? Yeah.

**Chris Gammell:** Yeah. And even then, I mean like USB 2.0 has its own different sets of speeds. They can go up to, you know, it has like, I think a couple of different tiers and everything. So.

**Dave Jones:** Yep. Yeah.

**Chris Gammell:** Depending on what you connect to and everything else. So.

**Dave Jones:** I assume that, that the USB 3 has different tiers as well. Oh, I'm sure it does. That it can actually drop back to a slower rate. If, because it's, once you get up to those sort of gigabit speeds, the, the, the cables are crucial. The connectors are crucial, even more so than USB 2.0. And, you know, if you get a kink in the cable, oh, bang, it doesn't, you know, bingo, you've instantly stopped your, you know, your video transmission or something. It's just died because the bit error rates dropped off because you've put a little kink in your cable.

**Chris Gammell:** Even crazier than that is, I've heard about HDMI cables before that had like 20, 20 insertions before they, they die. So that they're only rated at 20 plugging and unplugging. It's unbelievable. So you can't do that with you. You think about that with like a, you know, a cell phone charger, right?

**Dave Jones:** I think the standard one is, but the mini's rated for much more. The mini's rated for like a couple of thousand. Oh, okay. If you go for the mini HDMI. Okay. Okay. It's much more robust, but yeah, I know what you're talking about.

**Chris Gammell:** It's just because there's so much gold that they want, you know, that, you know, like those, the stupid monster cables, those gold monster cables with an HDMI cable, you start to actually get to speeds where you need that, you know, connection there. You actually need that, that conduction between the materials and you actually need gold. So if it starts rubbing off, you're screwed.

**Dave Jones:** Yep. Well, that's the same with any connector really. Yeah. It's always going to have a, it's always going to have an insertion life.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** I've, I've, I've actually done, um, I've done testing on that. Like I've actually designed jigs, which, you know, actually, uh, you know, with little motors that actually, um, insert and, and remove the connector over and over and you do cycle testing on them.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And stuff like that. And it is actually fascinating about how quickly you can wear the gold off.

**Chris Gammell:** Yeah.

**Dave Jones:** The contacts, you know, you can wear the contacts down and then you dig it into the copper and then it gets all, you know.

**Chris Gammell:** Yeah. That's crazy.

**Dave Jones:** This is actually a fascinating subject and you can kill them within, yeah, 10, 20 insertions if you got the wrong angle or something like that. The wrong amount of force at the wrong angle on the connector. Bang.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Dead.

**Chris Gammell:** Yeah. So one last thing about the, uh, this thing. I, I mentioned.

**Dave Jones:** One last thing because our amp hour's up.

**Chris Gammell:** Oh yeah.

**Dave Jones:** We're, we're well over, but who cares?

**Chris Gammell:** Oh, this is the lightning round. I came up with that stupid term last time. No, I don't like that. The lightning round.

**Dave Jones:** No, that is stupid.

**Chris Gammell:** Yeah, that's, come on, man.

**Dave Jones:** What is it? Some American game show or something? No.

**Chris Gammell:** Come on. All right. If we got a better name, you go ahead. The final round sponsored by Printable Electronics. How about that? Anyways, I want to say about this TI thing that, uh, we were just talking about. Don't, um, no, ow, ow. The amp hour is sponsored by Sirius Cybernetics. Sirius Cybernetics. There you go. Yeah. Yeah. This is episode 50, not 42, Dave.

**Dave Jones:** Oh, is this 50?

**Chris Gammell:** It's 50. Oh yeah. We're on 50.

**Dave Jones:** Oh, there you go. Half, half century. Half a century. Wow.

**Chris Gammell:** Yeah.

**Dave Jones:** It's not a binary multiple or anything. It's just a...

**Chris Gammell:** No, I got 14 more episodes for that.

**Dave Jones:** Right. Ah, well. Yeah, we'll get there. Ah. But it's almost a year, which is a pretty big deal.

**Chris Gammell:** Yeah, that is almost a year. We are two episodes away from a year, which is kind of crazy. Yeah. If people have been listening...

**Dave Jones:** And it would have been exactly a year, right? Because we haven't missed an episode, have we?

**Chris Gammell:** No. I mean, usually if we miss one, one of us, we find a sub.

**Dave Jones:** We steps in for the other. Yeah. I don't think we've missed a week.

**Chris Gammell:** No.

**Dave Jones:** And it's pretty much always been close to the same day, so yeah.

**Chris Gammell:** Yeah. And for people that have been listening for a year, we're sorry.

**Dave Jones:** Right. I just object you to this rabble. I'm not sick of us yet. Rabble. This random rabble each week.

**Chris Gammell:** I'm surprised we got through this week's episode. I was worried.

**Dave Jones:** I'm surprised my voice was held up.

**Chris Gammell:** I know. I guess the amp hour is therapeutic. There you go.

**Dave Jones:** It might be. Ranting is therapeutic. There you go.

**Chris Gammell:** Yes, you found a new...

**Dave Jones:** God. All I have to do is bottle that, and I can sell it.

**Chris Gammell:** You open the bottle.

**Dave Jones:** You wickers. Rant. Rant. Rant. Rant.

**Chris Gammell:** Ah, yeah.

**Dave Jones:** Oh, I just peaked there on my mic.

**Chris Gammell:** Should have used the kill switch.

**Dave Jones:** Yep.

**Chris Gammell:** I don't even want to say anything anymore. I... Yeah. Anyways.

**Dave Jones:** Come on. You had something you wanted to talk about before I really interrupted.

**Chris Gammell:** So this touch response thing, all these display technologies and everything else, I think that they're talking about touch responsive and touch feedback haptics. That stuff is moot. It's not going to matter because... I mean, maybe it'll matter for TI because it'll be in the big products, but I think that the way of the displays is going... It's going... The displays are going the way of the Dodo, basically. Because I think with, like, this whole Google Android ADK and everything, the... The... Allowing your... Allowing your hardware to interface to these established devices, I think you're going to stop seeing people put displays on. They're just going to say, all right, use your phone or use your, you know, tablet or whatever. I think that's... I think that's the future. Ah, no. You don't think so? You think they'll still embed screens?

**Dave Jones:** No. Screens. Dead horses for courses, as always.

**Chris Gammell:** I still don't know what that means.

**Dave Jones:** Everyone, you know, yeah, let's buy our next multimeter. It doesn't have a display on it because it hooks up to our phone.

**Chris Gammell:** Yeah, that's what I'm saying. I think it's going to happen more and more because the cost then gets pushed to the phone or the other device. And that's a significant chunk.

**Dave Jones:** Yeah, but it will still remain a pain in the ass novelty.

**Chris Gammell:** Maybe.

**Dave Jones:** And, you know, yeah, it'll be good for some things, right? But for others, no. You've got to keep the display on there.

**Chris Gammell:** I don't think you do. What about, like, industrial equipment? That doesn't need a display, right? You need one display for all of them. So then you can even just sell a display separately.

**Dave Jones:** Of course you need it. Some industrial places, you can't even take your mobile phone in there. Right. They ban them. Of course you need a display.

**Chris Gammell:** You could sell a tablet for $300 to them, right? And then already have it pre-programmed to hook up to it, right? So you could have these...

**Dave Jones:** And then you've got to get your phone out of your pocket, switch it on, and then run the app to actually get the display you want to see?

**Chris Gammell:** So I sell you an industrial controller, right? That controls a robot. So maybe before it had a display. Now, as a manufacturer, as an OEM, I just buy and resell a $300 tablet. It's already there. It's cheap, right? It has all this functionality you'd need. And then I write a program directly for that. It talks to the stuff that I've designed, and I just knocked out a bunch of my costs because I just bought and resold something to you. And because I'm buying a thousand of them in order to sell them with my product.

**Dave Jones:** Oh, okay. I see where you're coming from.

**Chris Gammell:** So you could hook up an iPad or an iPhone.

**Dave Jones:** Not so much using the person's one, but you supply an already developed tablet.

**Chris Gammell:** Right. Or in some cases, you could use the person's tablet or phone. But I think more likely it would be, why not buy a finished goods one even from China? You know, a finished goods tablet that's really low cost and stupid, but it already has everything in there.

**Dave Jones:** Well, that concept's been going on for quite some time. There's nothing terribly groundbreaking. If it makes sense, if it makes economic sense, if you need a portable display, then yes, that's certainly the way to go. But, you know, it's not going to supplant everything. Some things just need a convenient display on there. Yeah, maybe.

**Chris Gammell:** Yeah, if you push the cost down, maybe it'll stay on there. But I think in general, I think it's all going to move towards, you know, having that. No?

**Dave Jones:** Not even close. It'll be niche. It'll remain niche. That is my bet.

**Chris Gammell:** Okay. And you are welcome to it. You're welcome to your opinion. I'll argue with you about it next week. How about that?

**Dave Jones:** Fantastic. That's a pretty big call, you know, that displays will disappear.

**Chris Gammell:** I didn't say displays will disappear. I'm saying they'll get pushed to a discrete device that will contain the display itself.

**Dave Jones:** Well, by disappear, I mean they'll disappear off the actual product.

**Chris Gammell:** Oh, yeah. That is a big prediction. But I think it's going to happen.

**Dave Jones:** Right. Well, I think you're set for a big fall.

**Chris Gammell:** That's okay. I've got another one lined up. Don't worry.

**Dave Jones:** Awesome. Every week there's a new fail from Chris.

**Chris Gammell:** Oh, man. I love it. We really did go over this week, didn't we?

**Dave Jones:** We did. We're eight minutes over.

**Chris Gammell:** All right.

**Dave Jones:** All right. That's enough ranting.

**Chris Gammell:** I'm going to go eat some hot dogs and watch some things blow up like a good American. Awesome. I'll talk to you next week, Dave.

**Dave Jones:** Have fun.

**Chris Gammell:** All right. See you. Bye-bye, guys.
