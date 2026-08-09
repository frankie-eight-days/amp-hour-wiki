---
episode: 287
title: Pull The Trigger
url: https://theamphour.com/287-pull-the-trigger/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded February 17th, 2016. Episode 287. Pull the trigger.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Oh, on the road. Traveling, traveling, traveling.

**Dave Jones:** On the road again.

**Chris Gammell:** Yep. I'm in San Francisco. I will be doing a meetup tomorrow, probably by the time this is released. No, it'll be over and done. Yeah, I think. Dusted, won't it? Yeah, probably. Yep. But yeah, just doing my usual thing on the West Coast for a little bit. All right. How about you? What's new with you, man?

**Dave Jones:** Well, you're sucking off the supply frame teat.

**Chris Gammell:** Sure, yes. That makes it sound really appealing, by the way.

**Dave Jones:** Well, it's all paid for by them, is it not?

**Chris Gammell:** Yeah, it's not like I'm not doing work, man. This is my job.

**Dave Jones:** Yeah, your job is just to hang out in hotel rooms. Are you sick of it yet?

**Chris Gammell:** Oh, yeah, no. You're right. You're right. That's what my job is, to hang out in hotel rooms. No, I love it, man. It's been good. We're working on some cool new things, so we'll see. All right. Some tools, hopefully, that I can talk about eventually here.

**Dave Jones:** Excellent.

**Chris Gammell:** Software still continues to be weird. I don't really get it, but...

**Dave Jones:** Software is in, like, the online tools.

**Chris Gammell:** Yeah, web stuff.

**Dave Jones:** Web stuff and the parts.io you're talking about.

**Chris Gammell:** Right. Yes, yes, yes. So, yeah, that's going good. And tomorrow, I'll be... The meetup is actually James, bald engineer. Right. I think maybe you've seen some of his... He's got tutorials online. And then Natasha, who runs Snap EDA. So, that's one of, like, the footprint... It's supposed to be, like, a footprint library for...

**Dave Jones:** Okay.

**Chris Gammell:** ...a lot of different CAD programs. So... And I've been trying to post the talks, so... I just posted a couple of talks from the last time. And, you know, it's a good resource.

**Dave Jones:** Excellent. How many people turn up to these things? I think I've seen photos, because you usually tweet photos. It looks like there's, you know... Yeah. ...50 people there or something sometimes.

**Chris Gammell:** Yeah, it's about that. It depends on how many people are in the office that day, too. Usually 65. We limit it at 65 on the RSVPs, but, yeah, usually 40, 45 show up. Got it. Yeah. It's pretty good. Yeah, it's not bad. It's always a good time. It's a lot of the same people kind of month to month.

**Dave Jones:** I was going to say, is it the same people or...?

**Chris Gammell:** Yeah, but that's actually a nice thing, you know. It's kind of a... Yeah, yeah, no, it's good. ...kind of catch up with people, a good way to keep in touch and stuff like that. Got it. I highly, highly recommend people do meetups, either throwing their own or attending them. So, I think it's... Yeah, yeah, yeah, rub it in. That was not a veiled thing, encouraging Dave to get off his ass.

**Speaker ?:** Yeah.

**Chris Gammell:** But, no, it's good to kind of just trade. You know, I always push for... I sent, actually, an extra reminder this time. You know, bringing... You know, like, you and I talk about this a lot, too, but just bring whatever you have, even if there's, like, a board that didn't work out.

**Speaker ?:** Yeah, yeah, bring something.

**Chris Gammell:** I know. Like, just having that in hand. Have it in your pocket. You can just whip it out. Yeah. When in doubt, whip it out. Different phrase than I would use, but, yes, I agree with the... Sentiment, definitely bring hardware and use it as a conversation piece. I think that that's valid at almost every nerd and even quasi-nerd events, you know? Like, it's just a... Right. It's a good thing to talk about. It shows what you're passionate about. It shows what you're working on. So, I'll have my... That board I mentioned last time, that Ascentions STM32 board I've been working on, finally got that assembled and ready to go.

**Dave Jones:** You have to hang it around your neck on a gold chain. That's the... Ooh, that's a bad idea.

**Chris Gammell:** That's a cool way to do it. Yeah.

**Dave Jones:** A thick gold chain with a PCB hanging off it.

**Chris Gammell:** I am super pissed at myself. Do you do checklists when you do boards?

**Dave Jones:** I used to... At one point, I did a checklist kind of thing, but no, when I was a PCB doing it full-time, you know, I was actually... That's pretty much all I was doing is PCB design. I was a full-time professional. No, you just... Like, it's so routine for you, you don't need a checklist kind of thing. Although, you do go through a checklist. But yeah, you do go through a checklist, but you don't have to... Like, you don't have it pinned up on your wall and you go through each step. But that's the thing.

**Chris Gammell:** I feel like it is a good idea. So, like, last time, I saw this board, I was looking at it and I'm like, what the hell was I thinking? Like, I didn't... So, I remember the big stuff, right? Like, mounting holes, right? That's a big one that I've been trying to remember every other time. But, like, the silly little things, like marking polarities on your input power connectors, right?

**Dave Jones:** It's just like... I know. Yep. Why? There's so many little ones. Yep.

**Chris Gammell:** Yeah. And you know what the really big one is? That I always forget, for some reason, I had two LEDs on board as indicators for, like, a USB to serial type thing. Right. And then I didn't put an LED, just an indicator LED for power. Like, that is such a simple and effective and useful... Or, like, putting a second one just on a digital output, you know, just as an indicator LED. It's stupid simple, but, you know, it can make such a big difference in, oh, hey, this thing's on now. Why is this on? This shouldn't be on. One of the IOPins is powering the entire part. This isn't right. You know, like, it could be, like, tons of different things there. Or, you know, I thought this was on. I thought I put power on it, but there's no LED, so obviously something's wrong. You know, it's like all these little things that you forget about.

**Dave Jones:** But when I have had checklists and I've gone through, I still find they don't pick up everything. Because each board has its own unique sort of stuff, you know, like its own unique things. So when I finish a board, I'll just sit there for a day, like, you know, like a professional board, right, at a job. I'll just sit there all day, just panning around that board, going in different views. This is where the 3D view is brilliant, right? Because you can see, you know, it's a what you see is what you get, you know. So, like, and, like, I don't care about the components most of the time. I just, you know, are my silk screens right, you know. You just wanted another view. Yeah, yeah, yeah. Are there, you know, are the polarity indicators on those connectors, you know. And I'll just spin that board around in 3D view for hours, all day, just picking up little stuff here and there. That probably, you know, like, if I had to do every single checklist for every single issue I've found on every single board, the checklist would be so long, it'd become unusable, right? And you just wouldn't want to do it. It's, you know, sometimes it's...

**Chris Gammell:** Well, I don't know. I've read about the power of checklists before, right? I mean, like, so I was just on an airplane today, like, like, pilots, you know, like, that's a huge thing for the airlines industry is, like, checklists are super big because even when you think you don't need it, like, there is a power to that just because it's part of the routine. Yes. And, you know, it's a very, that's very cultural, but also safety.

**Dave Jones:** Well, there's a lot on the line, too, you know. Yeah, of course. Like, you know. Right.

**Chris Gammell:** Yeah, you and I pay an extra 10 bucks to get another Osh Park board made. They, you know. Yeah, they crash the plane. Right. Yeah, yeah. Yeah. No, but I know what you mean, though. A lot of it is going to be just kind of learned lessons over time. And I think that having that, you're right, having that visual thing of just, the best thing is having it in hand. Obviously, when you have it in hand, you're like, oh, yeah, I forgot, blank, blank, blank, and blank, right? But having some kind of way to visualize it and see it in a different way before sending it out is, that's actually a really good point.

**Dave Jones:** Some people just don't like procedures for what insert reason here, you know? Sure. And that's, you know. And it's fine. I get in moods like that where, you know, I don't want to run through some stupid checklist. I know what I'm doing. Push the go button. Or sometimes you just don't care, you know, too much. Oh, it's near enough. It passed the DRC, right? Good enough, you know. Go. Right. Right. I don't care if I have to re-spin this sucker, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Like, yeah.

**Chris Gammell:** Although for, I don't know about the Altium or anything, but you can generate Gerbers without even checking DRC if you really want to.

**Dave Jones:** Oh, you can. Yeah. I think they might force you into things these days.

**Chris Gammell:** But that's another checklist item is like, did I check DRC? Yeah. Right.

**Dave Jones:** I think Altium's going more that way because to release stuff, you know, into the vault or whatever, you know. Oh, right, right, right. You know, but back then that was their aim was to, you know, like you went through certain steps and this is what you did to check it in. You know, you do your DRC, you generate your Gerbers and you do whatnot. That's good. You know, you bomb. I mean, it's a procedure type thing, right? Yeah, yeah. That makes sense.

**Chris Gammell:** Yeah. Exactly. And it's kind of shades of checklists, right? It's like, yeah. Right. There could be somewhere it's like, oh, no, you have to have like a sign twice kind of, you know, checklist process. That's different than, here's the things you should be doing before you could check it in. It's just a reminder. You're, that's, that's probably a better way to do it. So.

**Dave Jones:** And still, even with checklists, it's better if somebody else does it.

**Chris Gammell:** Oh, that's true. Yeah.

**Dave Jones:** Because you can mentally skip over it. You know, you can mentally skip over a thing because you, you're 100% sure it's there or you see things that aren't there, you know, because they're in your mind. It happens, you know.

**Chris Gammell:** Right. And that's effectively what design reviews are as well. But I think that having it as a, yeah, standardized, here's the things you should be checking or at least think about checking. That's, that's good to have. Right. So. Yeah, man. So I forgot it this time. But yeah, you know, live and learn.

**Dave Jones:** Yeah. So you're using a new CAD package, as in mechanical CAD package, apparently.

**Chris Gammell:** Oh yeah, that's what we were going to talk about that. Yeah. So on the mechanical side, I've been using Fusion 360. Have you ever used that?

**Dave Jones:** No, I have not.

**Chris Gammell:** That's the, so it's by Autodesk. It was like, so they have, they have a couple. They have Inventor is one of the big ones. I actually heard about it from Jesse, who runs Keyboardio. So he, he and I kind of talked about KyCat a bunch. And I was asking what he, you know, he's got this mechanical design. And, and he actually gave a talk last time that I was here in San Francisco, which I can post. But basically, he was telling me about the, you know, like, they were trying to bring up this web-based tool. There's a bunch of these, these, they're all kind of, they want you to pay monthly now instead of buying the big site license type of thing. And, and a lot of them are web-based. So this is actually a web-based tool, kind of like what Altium, the, what's the one you use, Circuit Maker?

**Dave Jones:** The Circuit Maker, yeah.

**Chris Gammell:** Yeah, same kind of thing where it's like you have a, you have a application on your computer, but it's still linked into a library online. But, you know, there's. And it's free, is it? Well, it's, it's, 30 days are free and then, but then they, they support like startups and small businesses and stuff like that. So it's like, I think like one year license is free for startups. So contextual electronics is. A startup. A startup, sure. Yeah. But it's also free for students and stuff like that. So, yeah, I know that. I think it is, it is really accessible and I'm seeing more and more people use it. And, and actually there's a really great YouTube channel called NYC CNC, even though he lives in Ohio now. He started in New York and now he moved back to Zanesville and, and he's got some good Fusion Friday stuff. He does. And then, you know, and then the company makes some good stuff too, good tutorials and. Got it. Yeah. It's.

**Dave Jones:** We were looking at another web-based one called Onshape.

**Chris Gammell:** Onshape. Yeah. And that was, that was another one that was recommended to me. Uh, what, what do you, what do you think about it?

**Dave Jones:** Well, uh, David, not me, but, uh, David, um, likes it and he wants to, uh, use it. So we're looking at getting a license for that. It's not free. Although, yeah, I don't even think there's a trial. Well, there might be a trial version. I'm not sure, but it's all web-based. It's entirely web-based. It's not even sure that, um, a server, you actually run it on a server. So.

**Chris Gammell:** So it's in the browser?

**Dave Jones:** It's in the browser. Yeah. Wow. And, um, but yeah, David seems to think it's quite good. So we're talking with them at the moment about getting some licenses, um.

**Chris Gammell:** Yeah.

**Dave Jones:** To see if we can use it. Yeah, I remember reading about them. We are whores, basically. We will use whoever gives it, whatever package gives us a free license, unless it totally sucks, you know? So.

**Chris Gammell:** Yeah.

**Dave Jones:** Like, because, I mean, that does matter. We have to standardize on something, so, you know.

**Chris Gammell:** Yeah. Right, and you want to be able to, you're not going to necessarily be modeling stuff, but you want to be able to view stuff and manipulate stuff easily, right?

**Dave Jones:** Oh, I want to be able to use it and just maybe make a few mods and do a few videos showing it off or something. Yeah, yeah. So I need a license as well, so.

**Chris Gammell:** Yeah. Right. And ultimately, that's actually what got me into it. It was like, I finished building the 3D printer, and then I realized that I don't know how to design new things. Right, yeah. Like, I know SketchUp, but I don't know how to make complex shapes.

**Dave Jones:** Yeah, no, it's a different ballgame. No. Whereas David says, yeah, Onshape actually has a lot of the stuff that, what's the one he uses? SolidWorks. SolidWorks. That's right, yeah. Right. So, you know, he says, yeah, it's got all the powerful manufacturing stuff, or if it doesn't have it, they're already planning to add it. It's in their list to add.

**Chris Gammell:** Yeah. Or whatever.

**Dave Jones:** And yeah, he seems to like it. So, anyway.

**Chris Gammell:** Yeah, no, I remember hearing about that one was, they raised like a buttload of money, like $60 million for that thing. Oh, okay. I remember. Yeah.

**Dave Jones:** Well, apparently they're former, they're people from, former executives from SolidWorks or something. So.

**Chris Gammell:** Yeah. So, it's, yeah, that's right. Yeah, no, that's, yeah, you're exactly right. Because, yeah, they started SolidWorks and then they sold it to Dassault or Dassault or however you say it, the French company that now owns. Yeah. Yeah. So, San Francisco Sirens. San Francisco. There you go. Yeah.

**Dave Jones:** Another mass shooting in America.

**Chris Gammell:** Maybe. Sorry. I had to. Hopefully not. Yeah. But, yeah, and then they kind of, I think they got to the point where, like, they sold it and then they kind of stuck around long enough and then they started working on this web-based one.

**Dave Jones:** Right. I didn't know it was the founders of SolidWorks. I knew it was some executives or something. Yeah.

**Chris Gammell:** I think it was. But, anyways, yeah, they raised a bunch of money and so it's got a lot of hype and I have not tried it.

**Dave Jones:** Well, actually, I've got a link here. It's like, why we started again, why we started from scratch in the CAD business. Here we go. Oh, nice. John Hershick. I'll send you a link. Okay. To this. Cool. So, yes, he looks like he goes through. Why they restarted the whole thing. Actually, that, yeah, it's not that long so it might be worth a read. There you go.

**Chris Gammell:** We'll look it in. Okay. Cool. Yeah, and, you know, you and I, I'm not a particularly huge fan of Upverter but I do think that, you know, I don't want to use it but I do think that the whole being in the browser kind of thing actually is, in general, the trend that we're going to continue to see on everything, including for CAD and everything else, right? You know, like, it's just an inevitability. I suspect so. Yeah. It'll be interesting to see. And there are a lot of benefits too, you know, like, different views and stuff like that. You can view it on tablets and phones. And your work's always there.

**Dave Jones:** You don't have to worry about backing it up and, you know, you can access it from anywhere. It's, yeah. Yeah. Yeah. Well, you know. That's why, like, I don't know, was it a decade? It must have, might have been a decade ago I moved to Gmail, right? I used to web, I moved to web-based email. I used to have email servers, you know, online. Oh, yeah. Pop 3 versus AMAP. Pop 3, right? And all that, you know, all that old school jazz. But then, you know, I moved to the web-based email and it was because I was using so many machines, you know, like, in different places. And it just made sense. It was a pain in the ass otherwise.

**Chris Gammell:** Right, right.

**Dave Jones:** You know, it's why I'm using Gmail. It's why I'm using Dropbox, you know. Like, everything's just available from anywhere I work, you know.

**Chris Gammell:** Mm-hmm. Yeah. Yeah. Well, actually, I still like the, at least right now, I mean, I like the one where it's still locally caches stuff. I mean, and this is, I think that's actually, again, to use the circuit maker thing where it's, you're still working locally versus being completely tied to the, you know, like, so that every change you do ties into the server. It's like, because then if your connection's slow, then every small change gets, is affected by that. Like, I think about things like Evernote. I use Evernote where it's like, you know, I'm writing, obviously this is just text, but like, you know, writing something locally on my computer, it saves it, but then it syncs against the cloud stuff. Yeah, that's great. That's the kind of thing that I actually, that's the same thing as Dropbox, where it's like, yeah, once you take a quick pause, it's going to start syncing to the server and that kind of stuff, actually. I think it has, you're right, it has a lot of impact. It can really save your bacon quite a bit. But like we talked about last week with, you don't like to get necessarily, you just use Dropbox, right?

**Dave Jones:** It was horrible. Yeah, yeah. No, I just use Dropbox. I don't have the need for version control. You know, I know you crap on about it and I know the benefits of it. I've used it before. So please, nobody try and argue with me. No, we're not.

**Chris Gammell:** I'm not going to at least. Yeah. It's just, you know. I, well, and that was up until you told me that you were using Dropbox. I think at the bare minimum, I think using Dropbox or some kind of syncing service for your stuff, that's the bare minimum. And if you're doing that, then I think for a lot of CAD type stuff, you're in good shape. Because even in a revision control system with CAD or some kind of visual thing like that, it's all or nothing. It's not like you're going to merge changes. And that's really the big difference. If you're at the point where you're going to be merging, you know, two different code, two people working on code separately and you're going to be merging into the same project, then yeah, you need to have a more controlled system.

**Dave Jones:** That's a different game.

**Chris Gammell:** But with CAD, it's going to be like, you're going to be working on something. And then when you're done, you're like, you'd hand it off to David and he's like, okay, no, David's working on it and it's back to you. That kind of thing. Like, that's more of a Dropbox thing.

**Dave Jones:** That was the co-working vision that Altium had. Oh, you can have multiple people working on the PCB at once and they worked on the technology to do it. And it sucked ass. It really did. And it probably always will. You know, to have multiple people laying out a board, it's just, oh.

**Chris Gammell:** It's just a problem that doesn't really exist, right? Because.

**Dave Jones:** Yeah, no, it's a, you know, it's a solution looking for a problem. It's very, very narrow. You know? Yeah. Yeah. Yeah. Like, technically, it's a very neat solution, right? Right. The way they did it, right? You know, technically very good. But it wasn't an issue that needed to be solved. They thought it was the greatest thing since sliced bread. And, well, of course. Yeah. You know. They learned that lesson.

**Chris Gammell:** Yeah. That's right. Hmm. Well, so, you are doing, well, you're having your minion do 3D modeling for you, huh? Yep. So, what are you guys building? Something new? Something new?

**Dave Jones:** We're doing stuff. Yeah, we're doing stuff. I should actually send you a. Yeah.

**Chris Gammell:** All right. Cool. Yeah.

**Dave Jones:** I should send you a little 3D model. Yeah.

**Chris Gammell:** We're working on a couple of projects. Yeah, cool. A couple of projects. Several. So, do you think you'll actually. So, I mean, we're talking about CAD just as a thing. But, like, you know, I don't know if you knew. I was back on my old secondary podcast for a while back, Engineering Commons. And, ah, that's where I was talking about this. I was thinking, like, I've talked about this on a podcast before. But it was there that I was talking about 3D modeling and stuff like that. But I was talking about, you know, just cross-disciplinary stuff, right? Obviously, you've been getting more into the business side of things. I've dabbled in that a little bit as well. But, you know, like, it's just my vision of the future is more and more people as the solos. I could just call them solos. Right. Right. And I think that, you know, you don't have to be great at this kind of thing. You can still hire an industrial design firm if you're really going crazy or if you're a mechanical engineer if you want to just make sure the mold's right for plastic and that kind of stuff. But for a lot of things, like, okay, I'm going to be 3D printing a simple case, I can model that. You know, I can just even just dimension.

**Dave Jones:** Well, so can I. But there's a difference between our skill set, right, yours and mine in 3D CAD and somebody who actually knows what they're doing.

**Chris Gammell:** Right. Oh, no, no, no. I don't deny that at all. But I'm just saying that, like, even just being able to dip that first toe in. Oh, yeah, yeah. That's actually pretty important these days. You know, dimensioning a drawing, that kind of thing.

**Dave Jones:** Here's the difference, though, right? David has a different mindset to me, right? See, to him, everything can be custom, right? Everything. Oh, I'll just model that in 3D and I'll go to China. I've got the contacts. I'll get it made, you know. And that scares the crap out of me. It's like everything.

**Chris Gammell:** It's because you've experienced and you know better.

**Dave Jones:** You know, right. And it's like, yeah, but to him, it's like, you know, that's like everything can be solved that way. And that has its good and its bad points, right? Because, hey, you know, you can lead down that rabbit hole of, okay, you've got 20 custom parts in this design when you only really needed two. You know, like, you know, you could have used off the shelf. Yeah, you could have used an off the shelf case. You know, you just didn't look hard enough, you know, like or something. Or it's good enough, you know. Like the off the shelf case is good enough for the look and feel of the product. You don't have to gild the lily and go completely injection molded and everything else.

**Chris Gammell:** And I feel like that kind of stuff is what ends up. So with someone like David, right, obviously he's very, very, very bright. And, you know, like and very ambitious and stuff like that. Ultimately, I feel like that's also part of how far you take it down the line as well. Like I recall I was really, really interested in making a cable assembly. And I couldn't find what I needed. You know, I searched through. I talked to every vendor I could find. I just could not find what I needed in terms of, you know, a pluggable cable solution that I wanted. First off, cables suck in the first place. We know that. Yeah, of course. It's a given. And it got halfway, you know, and then got the mechanical designer to make this housing for the cable to plug into and blah, blah, blah, blah, blah. And, like, everything seemed great at, like, the prototype stage. And it was like, yeah, we got prototype shot and stuff like that. And that was great, too. But then it just got to the point where it was like, okay, but now we need to make it a product. And, like, that's just another step up where, oh, well, now the case doesn't look. It looked good as a prototype, but this isn't good when you're going to be shooting 50,000, you know, injection molded plastic pieces. Because over time, the moldwares and the plastic sags and the, you know, the executive didn't like this little thing. And then it's like, and then the crazy thing is, like, and then the thing we don't talk about on here a lot either is, and then you have to get it certified. Like, and, like, holy crap. And we've talked to some guests about this, but, like, yeah, you know, getting things, like, certified and moving outside the norm or taking that on when a finished product might already be certified versus you having to go through and certify it. We've talked about this stuff like FCC testing and similar things before. Or, you know, that is a big deal, and that will make you hate your life for a while. You know, like, that certification just can really, and I think what ultimately it does is it just puts you off from going straight to custom the next time. Right. Okay. It's not that it's a bad thing. It's just that everything has a tradeoff. Welcome to the world of engineering.

**Dave Jones:** It's almost by definition what engineering is about, right, is tradeoffs, you know. You know, you can't just gild the lily on everything. That's not, you know, that's not engineering.

**Chris Gammell:** Well, you should be pounding this into David's head, man. Come on. Do you need to get him on the horn rent? Is he there? Can we shout at him? No, he's not here. No, he's on holidays. No, sorry. See, that's the thing. And then these kids go off on holiday, you know.

**Speaker ?:** Yeah.

**Dave Jones:** No, it's, you know. And it's like, you know, even when, you know, NASA, like, went to the Apollo project, they went to the moon, right? Even, like, budget was no.

**Chris Gammell:** Right. Money was no object.

**Dave Jones:** Money was no object. Manpower was no object, right? But there were so many realistic problems that they had to compromise on, you know. And, yeah. And there's just no choice sometimes. And that's why a lot of, especially, like, startups and crowdfunded projects and things like that, all, you know, the wheels would just completely fall off the billy cart. Yeah. Because, you know, they'll think that they can do this and this and they can add this and add that and, oh, and this extra perk, you know. We'll just add this functionality. And then it just, it all falls apart.

**Chris Gammell:** Yeah. I was, so at work today, we did, like, a company hackathon. And actually, software people are pretty good at this normally, but, like, super constraining the problem. Like, we all had these crazy ideas and then we're like, let's just find one example and make that work first. You know, and that's the same kind of thing with the product, too. It's, like, just get, like, the bare minimum of the thing working and then once you do that, and actually, I, so personally, I really dislike hackathons. I feel ineffective at them. I don't feel, like, I want to plan things. But the thing that it's actually really good for is putting you out of your comfort zone and saying, what can I get done today? And what that does is it kind of just strips away all the extraneous crap. And it just gets to the point where it's, like, okay, what can I get done? Just the baybones. Yeah. Right. What can I throw away? And that actually, that is probably one of the more powerful things about hackathons is just don't gild the lily, right? It's, like, you can't get to the point where the main thing is working first. And then once that works, then you could start bolting stuff on. And if the bolt-ons don't work, then, oh, who cares, right? You still have the thing that works in the first place. So, yeah, and the same thing works in hardware, right? It's, like, you know, get the board working by itself before you start trying to shove it into a case. You know, it's, like…

**Dave Jones:** Or sometimes just get a board.

**Chris Gammell:** Yeah. Or get the LED blinking when you jury-rig the wires together, right? I mean, like, anything.

**Dave Jones:** Sometimes we, you know, the circuit will be half finished. We'll order the board because we want a board. We want a board. And we can build up half the circuit on it. We can fit it into a case. We can play with it. We can hold it. You know, it's not finished, but we send it away, you know, because you're halfway there.

**Chris Gammell:** Yeah. Man, my old boss, one of the best things he taught me where he's… I was just, like, stressing over this and that. He's, like, just… Dude, just pull the trigger. Like, really. Yeah, right. Yeah, yeah. Sometimes you really do. You need to, right? Yeah. And it's just, like… Exactly. Except that you're going to have some screw-ups and that's part of the… Especially if you know it's just a prototype, right? If you're going straight to production, first off, you're an idiot. And second off, if that's the case, then… Or if you have… Maybe that's not the realistic thing, but say you have a really expensive board and you only get one turn or two turns total. That's fine. Maybe you spend a little bit more time there. But if you're doing a cheap proto, yeah, just pull the trigger, man. Just accept that some stuff's going to be broken because you can always bodge wire. Bodge wires are the currency of electronics, right?

**Dave Jones:** Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Pull the trigger, folks. And I don't mean that in the American way.

**Chris Gammell:** Oh. Really? Two references, dude? Two references, dude. Okay. Well…

**Dave Jones:** Sorry, I got bombarded with the Jeb Bush thing. I just couldn't…

**Chris Gammell:** I don't… Don't even. Don't even. Next. Yes. Well, so 3D printing… Not 3D printing. 3D modeling. And in general, I think that having those kind of skills, at least in a… Some kind of proficiency in that kind of stuff, really useful. Because at some point, you're going to have to talk to someone about, you know, how tall your capacitors are and interference and that kind of stuff. And it's… Products are not just circuit boards, you know? Like… Yeah, exactly. Yeah. I mean, like, you might see them like that on Kickstarter, but in the real world, people want plastic wrapped around their electronics.

**Dave Jones:** Those pesky customers. Yeah. Ruin everything.

**Chris Gammell:** Yep. Oh, dear.

**Dave Jones:** So, what's this… Speaking of cloud-based rubbish, what's this microchipper now on the cloud? Yay, you can do your picks in the cloud.

**Chris Gammell:** Yes. I don't really…

**Dave Jones:** Yay, I haven't actually… I haven't… Is it released yet, or are they just announced that they're going to do it?

**Chris Gammell:** Uh, I think it's just announced. Yeah. All right. Maybe it's out. I… That's the thing. I never… I never really got into the pick side of things. I know that you've done that in the past.

**Dave Jones:** Yep, I've done many pick projects, yes.

**Chris Gammell:** Yeah.

**Dave Jones:** Various techniques that started out… What do people like about it? Well, see, the thing is, right, people go, oh, why pick? Why pick? Right? Because pick was the first… I… There might be fanboys out there who may correct me, but pick was basically the first, you know, easy to get in… Cheap to get into microcontroller when they released the pick 16 F84. It had flash… Sorry, the pick 16 C84, which had E2Prom programmable memory. You can reprogram the chip. Wow. Without having to get an expensive windowed version that you stick in your E2Prom eraser… That's right. …or go through all these one-time programmables, you know? Yeah. And you could buy these cheap programmers for them. It was, you know, it was one of the first, right? AVR wasn't even around then, right? Right, right. We're talking… Like, I don't even think the company existed, right? Really? Well, I don't know about timelines, but… Okay. Like, it was like… I don't know. Anyway, well, definitely Atmel were around, but I don't think… Yeah, okay. But the…

**Chris Gammell:** Yeah, maybe the…

**Dave Jones:** Yeah, I'm sure I'm going to be corrected. Yeah, whatever. So, yeah. Architecture. Yeah. Architecture, but…

**Chris Gammell:** So, but that was the first one. That was one of the early ones that was accessible. Yeah. You're saying just as accessible thing.

**Dave Jones:** As an accessibility thing to your average Joe. That's why PIX took off in the hobbyist magazine world, right? Before the internet, right? Right. Magazine projects, that'll be using PIX because that was like, that was the one you could get. You know, that's the one you can buy readily. You know, before you had online e-commerce and everything else, right? Right. You could get your hands on these. You could get the hands on development tools relatively cheaply. And you could code it in Assembler, you know, which is what you did back in the day because C compilers were still sort of a bit, you know, like, oh, yeah, you've got to pay $1,000 for a C compiler kind of thing, you know. So, I started off in Assembler on the PIX, you know, and as did everyone else. But it was that reprogrammability. I don't know if they were the first one, but they were the first one readily available. So, that's why, you know, and it's legacy. It's just carried over and over. Yeah.

**Chris Gammell:** Well, they'd probably made a lot of brand loyalty and stuff like that too.

**Dave Jones:** A lot of brand loyalty. And to this day, I think you can still buy almost every original PIX chip, you know. Nice. So, they had a reputation of not discontinuing them and actually abandoning you as a customer, you know. So, that was, you know.

**Chris Gammell:** Well, yeah, that kind of thing. Like, I think invariably too, like, you know, you get people that are doing this as a hobby and then they start working in a company and then they say, well, why not that, right? I mean, like, that's the same kind of thing. You'll see that a lot of places. So, yeah, that's good. Uh, I remember, obviously you weren't there when I interviewed him, but Voya, uh, when I was in Serbia last time, uh, he was huge in the PIX stuff. And some of the stuff I saw that he did on, like, just simple, I think it was PIX-16 as well. It was just, like, graphic outputs and all this crazy stuff. It was, it was really fancy. So, way beyond my purview. Got it. Yeah.

**Dave Jones:** Atmel AVR came out in 1996. There you go. Really? Yep. Yep. 1996 was their first, uh, well, I don't know, I don't know what chip it was, but it was their first, yes, the AVR architecture. First in 96. Whereas PIX goes back to the general instruments, uh, chips. PIX stands for peripheral interface controller. And it used to be, I think it's general instruments used to own them, right, before they became microchip. And, like, back then, they were making, you know, these one-time programmable microcontrollers that were used in everything, you know. And, um, yeah, so they date back to the 80s, you know. They date back, like, you know, a decade or more, you know, way before, um, some of the other newer architectures. So, yep.

**Chris Gammell:** I just, I jumped past all that stuff. I didn't, I didn't do any of that. Yeah, no, you're too young. You don't remember this stuff. No, I mean, but I didn't even do really, I didn't, never did, I mean. You know, I've done some Arduino stuff, of course. Right, yeah, but you've never done, yeah, yeah. I've never done, like, low-level stuff, and now it's just, like, I'm in the STM32 world. It's, like, yeah, straight to Cortex.

**Dave Jones:** All right, whatever. Ah, there you go. The first general instruments PIX were in 1976.

**Chris Gammell:** Whoa, nice.

**Dave Jones:** Okay, right, before you were born, sonny boy. That's right. Yep. Like, yeah. And that's how old school they are. So there's a lot of brand, a lot of legacy there. You know? Yeah. So, yep. Although it wasn't the first PIX, but that's the first general instruments architecture came from there. So, yep.

**Chris Gammell:** And now you can program it from the internet. So.

**Dave Jones:** Right, yay. Progress. That's, yeah.

**Chris Gammell:** Well, no, so we started the show talking about, well, not started the show, but we were talking also about, you know, web-based tools and stuff. Have you evolved your view at all? Obviously, when we were talking about Embed and that started coming out, you know, obviously that's a cloud-based compiler as well. Do you have any revisions on that side of things?

**Dave Jones:** I haven't used them, so I can't really comment.

**Chris Gammell:** I remember, so I've been, obviously, I immediately devoured Jack Ansell's newsletter as soon as it hits the inbox. Right. And if people don't know, you should totally read it, the Embedded Muse. You can sign up on cancel.com. But it seems like, I remember Jack at the beginning didn't seem like he was super jazzed on it. And then, obviously, when Alicia and Chris were on here and they did the call-in show with me, they were recommending it as well. And I think it's kind of one of those, kind of just kind of, I wouldn't say crept in, but it's definitely, I've seen more positive than negative things about it lately just because of the simplicity. And, you know, it's, and if people don't remember, it's basically you can write in an online IDE and then it does the compiling and then it pushes the binary down to you and you just basically drop it as a file into the USB, you know, it looks like a USB flash drive and that you drop it into that and it basically programs the controller. Like, that's pretty cool. Cool. I think that's an interesting model. I don't like that it still doesn't have debugging. But, but otherwise, I mean, like, I think that that actually, I mean, overall, I think that is actually a really interesting low friction model to get people into, to get, especially because it's cross-platform as well. It's, you know, it's more than just one vendor. So that's kind of interesting too. And, you know, it's, it's very low friction. I do imagine someone coming into the, the, coming into the hobby or the field in general and be like, what's debugging again? Yeah, right. Yeah. But yeah, you can learn that later, you know, debugging can actually happen with just a single LED.

**Dave Jones:** So there are debugging fanboys out there. You see it on the, I see it on the forum a lot where, you know, oh, you, my debugging's everything. You must have the ultimate debugging tool that can trace step through, you know, a minefield of, you know, bugs and like, you know, they go, oh, the pick kit three is garbage because it's a garbage debugger. You've got to have the real ice, you know, and there's the ice fanboys who, you know, oh, you have to debug it on the real hardware, you know, none of this in-system serial, you know, debugging protocol rubbish, you know, and it's, it's, it's, it's, it's,

**Chris Gammell:** it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's not necessarily going to be.

**Dave Jones:** Like, I've never been a debugger fanboy. I've never really had the need to, you know, trace step through everything.

**Chris Gammell:** If you or I write something and it's bad, we're going to have to start over no matter what.

**Dave Jones:** My code's never been bad enough where I've had to. Yeah. As you said, like, I will just add a little, a couple of lines of code that like, like, actually blinks a lead or does a serial output or toggles a line and then I can check it with a scope. And that's, you know, like, right.

**Chris Gammell:** That's adequate for me. But then again, we're not doing crazy things, right?

**Dave Jones:** No, we're not debugging 10 million lines of embedded C++. Right.

**Chris Gammell:** Or if you're, if you're like, if you're debugging like a, what's that called? Where you're writing directly to memory from like an ADC or something, you know, like having just high throughput type calculations, stuff like that.

**Dave Jones:** Would it be direct memory access? DMA? Yes. Yes. Thank you.

**Chris Gammell:** I was like thinking, I was like, it's not DRM. DRM is totally different. Don't say DRM. It's a DMA. Thank you. But you know, just like things like that where it's really super high throughput.

**Dave Jones:** Oh, hang on. I, I just got a date. I have to go back. Sorry. Not as early as I thought the 16C84 from the pick from microchip was 1993. 1993, but it was a big deal. But once again, it was still like three years before AVR was even, you know, a wet dream. So yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, that's why it got a lot of brand loyalty. Sorry. Back on target. Stay on target. Stay on target.

**Chris Gammell:** His computer's off.

**Dave Jones:** Is everything okay, Chris?

**Chris Gammell:** Yeah.

**Dave Jones:** Yes. I'm using the force. That's what you're supposed to say.

**Chris Gammell:** Use the force. Use the fork, Luke. Yeah. Yeah. So micros and stuff. We should probably move away from that because I think we pretty much run out of things that we have to say about micros. At least I do. I've run out. Right. Yeah. We're done. Yeah. So.

**Dave Jones:** Oh, that's boring.

**Chris Gammell:** What? Not done, done. We're not like done with the show, are we?

**Dave Jones:** Oh, right. No. I've got 20 minutes left. Jeez, that 40 minutes flew by. Sorry. We've just pissed it away. Yeah. Talking about nothing. That was good.

**Chris Gammell:** That was a good conversation. All right.

**Dave Jones:** One of your best episodes ever, you think. Yeah, that's right. Right.

**Chris Gammell:** We should end it now just while we're at a high point.

**Dave Jones:** Ah, boy.

**Chris Gammell:** Yeah. So, how goes the DMM enterprise? You are the DMM.

**Dave Jones:** I'm packing and shipping up to the wazoos at the moment. I'm sold out. Okay. I'm sold out. And here's another thing, which, you know, is an issue. Like, I, you know, I've got my new rebadged Bryman multimeter, right? Yes. That I'm selling. And, like, I haven't really even advertised it yet as such, and it's sold out already. You know, I ordered 200 of these things. Yeah. Yeah. And, you know, it's sold out. Well, I've got a few left that I want to send to various people. But, basically, you know, public as far as, all right. Ah, right. Yeah. All right. Do I get the hint?

**Chris Gammell:** Yeah, I hope so. All right. I'll send you one. Anyways.

**Dave Jones:** Anyway. We've been, like, yeah, basically sold out already, right? And, like, after it leaked online, it accidentally leaked, actually. I think we spoke about this the other week, didn't we? Yeah. We leaked it. Yeah, you're right. Yeah, it started to sell, and I realized, oh, yeah, I'm probably going to sell out of these things. So, I contacted them and said, you know, I'd like to order another batch. You know, what's the lead time? Two months. You know, it'll be April, right, before we can ship you new ones. And then it's going, holy crap, two months every time I place an order? Because they basically build them to spec. That's, you know, it's not like they build 110,000 of these things and keep them in stock for you. They, you know, I guess they might have the just-in-time model. You know, who knows? I don't know.

**Chris Gammell:** Like a PCB, what do they call it, a supermarket? You ever seen that before?

**Dave Jones:** Right. Supermarket. Or isn't the Dell model? You know, didn't Dell used to make computers to spec for you? You know, as soon as you placed an order, they'd, boom, they'd spin it up and they'd manufacture it, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Or something. Or they had all the parts or whatever. Anyway. Yeah, yeah.

**Chris Gammell:** What I mean is the super, I don't think it's a supermarket, something like that though. But it's basically, I've worked in manufacturing places like that where it's like they have a bunch of common pieces. And they would have, they'd build like 500 of the common board and maybe there's 200 of those available, but you're still waiting for, you know, 200 of the displays that aren't yet made, that kind of thing.

**Speaker ?:** So.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, so they obviously don't like to keep stock. So they basically, you know, effectively make them to order. It's hard to get information out, you know. Like I guess a lot of it's trade secret. They don't want everyone to know how they do things and why. But yeah, it's two months lead time to get another batch. And like I expected, you know, maybe a few weeks. I thought, you know, it's a new model. I'd start churning them out, you know. So maybe, you know, it'll be in the pipeline kind of thing. But, you know, no. Two months. Thank you very much. And I'm ordering a big quantity too. Yeah. And so it's, you know.

**Chris Gammell:** Actually, so I've been doing a bunch of stuff with like manufacturing stuff on the software side recently. But, you know, like you don't really, until you get to a certain point, you don't really think about that stuff. Because, you know, it's like, oh, well, I'm going to buy stuff that's in the marketplace. You know, I can buy stuff on DigiKey or whatever. And you don't have to really think about it. But when you do get to a certain level, like you are, right? So you're buying, you know, a couple hundred of something. It's like, no, no, no. Lead time is a huge thing that you don't really have to think about. And what people sometimes don't realize, I'm sure some of our listeners understand this, is like something that is eight to 12 week lead time, which is, you know, some eight weeks is, six to eight weeks is standard.

**Dave Jones:** Oh, you young whippersnappers have got it easy. Forty weeks when I was a boy.

**Chris Gammell:** Yeah, of course. Right.

**Dave Jones:** I'm not kidding. No, no. I know you are.

**Chris Gammell:** Right. But let me say why that is. If people don't know, that's because they're literally taking new silicon and putting it into a fab. So if you want to buy a bunch of new pick 16s and they don't have them in the marketplace already and there's none that are unpromised to customers. They've got to slot you in to their schedule. That's right. Yeah. You have to go. You are basically dun, dun, dun, dun, dun, dun, dun, dun, dun. And they're basically just churning out new silicon and testing it and packaging it or cutting it up and packaging it and testing it again. And, like, yeah, like that is, like Dave said, back in his day, because he's old. And that was more, that was just a capacity thing. Right. Right. And if you don't have lots of excess capacity, then you're basically getting in line and sometimes big customers get to jump the line a little bit.

**Dave Jones:** Apple or somebody comes along and boom, everyone else gets bumped. Right.

**Chris Gammell:** Right. Exactly. And it quickly ripples throughout the ecosystem because, you know, like, so now Dave is getting an eight-week lead time on a multimeter. That means that they're probably getting four to six-week lead time on their stuff, right? Then they can build it in a week or two and get the stuff shipped out. Yeah.

**Dave Jones:** They're probably, maybe that's the reason for the delay is that they're going to order the parts.

**Chris Gammell:** I don't think that's a delay even though. I mean, like, that's just a, like, it's not like there's just bunches of stock in the market. Like, yes, there is stock in the marketplace. Yep. But once you get past a certain quantity, it's all about that purple screw, right? Or like the microcurrent thing, right? You had that one resistor. That one resistor.

**Dave Jones:** That was, yeah, yeah.

**Chris Gammell:** You know, that's just a thing that you have to deal with. And it just ripples through the system really quickly. And I tell you what, you know, like, looking at this, I look at this stuff all the time now. There's no way to fix it. No. Other than building with complete jelly bean components, which means you're not making anything. Exactly. And you can, yeah, turn it. You need to get it in the first place.

**Dave Jones:** Yeah. That's right. But in this case, it completely ruins, I hate to use the word, my business model, right? But I've got a lot of people asking for this thing. It's popular. And I haven't really even advertised it properly yet.

**Chris Gammell:** Dave, lead time makes the heart grow fonder. I think that's how the freeze goes. It's just coming out of Valentine's Day.

**Dave Jones:** And then, like, I did this on the forum. I went, what the hell do I do, right? I asked this on the forum. Do I take pre-orders? Do I crowdfund it so I have, you know, like, money in the bank and get the hype and get people up and get the money up front and blah, blah, blah. Do I do this? Do I do that?

**Chris Gammell:** You hire a hype man, right? Like rappers do.

**Dave Jones:** Like, yo, yo, yo, Dave Jones. Got to have the best DMF ever. And, like, see, that's the thing, right? I had already planned this week to do a video actually reviewing this meter, right? And, you know, like, but what's the point? There's no point if I don't have anything to sell, right? It's just, it's stupid.

**Chris Gammell:** You're thinking like an engineer, man. You're not thinking fourth dimensionally. Dimensionally. Money is, shall we, you know?

**Dave Jones:** Yeah, but no, no, I would get more. No, but I would get more if I wait. I think I would. I think I'm doing the right thing. I'm not going to do a review video until stock's almost there or until I actually have stock to hand. Because, you know, yeah, you'll get X amount of people signing up, right? But then you'll get a lot of people who go, no, I just don't want to wait.

**Chris Gammell:** Yeah.

**Dave Jones:** It's a trade-off. And I think if I did a video now, I just have a lot of pissed off. I've already got a lot of pissed off people. Oh, why can't I buy it? You know?

**Chris Gammell:** Yes, we are a culture that's used to, you know, a lot of stock in the system. Yeah, getting it straight away. Yeah. Yeah, that's true. No, and it's just... And that's another thing. I think from a business perspective, too, is that, like, a lot of people don't realize that, okay, you know, someone might say, well, why don't you just build a bunch and sit on them? And it's like, I'm not sure about where you live, but at least where in the U.S., it's like, if you hold inventory, you start getting taxed on inventory. I mean, like, it's like, you don't get to just... There is a cost for overshooting a...

**Dave Jones:** Hence the stock take at the end of the year, all that sort of crap.

**Chris Gammell:** Sure, exactly. And, you know, that's where all that just-in-time stuff comes from as well. It's like you're trying to not only make sure your cash flow is free so that you can build the next one.

**Dave Jones:** Cash flow is the number one thing to keep a company afloat, is cash flow.

**Chris Gammell:** Yeah, right.

**Dave Jones:** And inventory is the arch enemy of cash flow.

**Chris Gammell:** Right. Stock.

**Dave Jones:** Stock is the arch enemy.

**Chris Gammell:** And so, okay, so we're going to talk about cash flow. It's not that we're turning into a business podcast here. Let's just talk from a practical standpoint, like...

**Dave Jones:** But no, it's an important thing, considering that everyone, everyone, anyone, any Joe blogs in their garage can be a manufacturer now. Yeah, yeah, yeah. You know, a seller, you know.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah, anyway, so it's important.

**Chris Gammell:** So let's use your example here, though. Like, so say, I don't know your actual numbers, but let's say you're going to go and build 500 multimeters at 50 bucks a piece, right? And it's like 50 bucks a piece being like the cost to actually build it, right? Yep. Thinking about the cash flow there, it's like, holy crap, that's what? 25 grand. That's 25 grand, yeah. It was like, well, is that really right? Yeah, it's 25 grand, right? And like that, it doesn't seem like much, but... It's 25 grand. I've got to pony up. Yeah, on a per basis. But like, and then that actually ripples through as well, because I think we've... Who did we talk to? We've talked to someone on the show before, too, where like, you know, some distributors will give you credit for some amount. Right, yep. But not necessarily that whole 25 grand. It's like, that means the rest, you've got to, yeah, you've got to cough it up, man.

**Dave Jones:** Well, in this case, I don't have to cough up the money right now, but I've got to cough it up a week or two before they ship.

**Chris Gammell:** No, no, so it's like...

**Dave Jones:** You know, you can afford to buy all the parts and order the stuff and get them made, you know? Right, or you can just, you know, remortgage your house. But in this case, I decided against that. Right, yeah. You can do that, too. You've got to get... Or get a line of credit. You know, I had PayPal ring me up the other day. They physically rung me on the phone, a human from PayPal.

**Chris Gammell:** Human being, huh?

**Dave Jones:** Yeah, a human being. They actually work there, apparently. Weird. Unbelievable. And they said, you know, have you heard about our credit line, our line of credit? And yes, I've heard about it every time. I log in, you keep plastering it with me, you know? PayPal will give you money, credit now, up front, based on your sales history and, you know, and stuff like that. And then they'll take out a percentage of your sales when you do actually make the sale.

**Chris Gammell:** All it took was David to sign over to Sagan. Right. Yeah. Oh, your firstborn son? 12. Oh, cool. Yeah, right.

**Dave Jones:** It was only 12%, you know, interest rate. Right, right. No, I'd rather pay zero, thank you. Yeah, right.

**Chris Gammell:** You know, I mean, these are very practical things for people that are thinking about making products. And not even if you're not making your own product, too, right? I mean, like, if you're... This is what your accountants at your company and your purchasing agents at your company, if you're big enough, this is what they're thinking about, too. Because there are significant capital outliers to go and build a hardware product. And then the way it gets back to all the designers that are listening is, like, man, don't mess it up. Right. You know, we might be okay with pulling the trigger on a PCB where you're buying three of them or five of them or ten. Don't pull the trigger on the 500 to 1,000 order kind of thing.

**Dave Jones:** I've worked at companies where buying a million dollars worth of parts is, you know, yeah.

**Chris Gammell:** Jesus. Yeah.

**Dave Jones:** Right? But, you know, that's what you commit to. Right?

**Chris Gammell:** Right. Right. Yeah. And hopefully you'll make a 10 million on whatever pops out. But, like... Exactly.

**Dave Jones:** Yeah. You kind of have to. Massive volumes, you know.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** Yeah. It's a big deal. So, there you go. So, in the end, I decided not to take pre-sci... Well, I did start back orders. So, I took a few. But then, oh, my shipping systems are... Yeah. I don't think it's going to work nicely. I'm getting them to change it. Anyway. So, I stopped back orders there. And I've basically just ordered. I've told them, look, yeah, I'll order another X hundred. Thank you very much. And I'll pay for it out of my own pocket. And, you know. Yep. I hope I sell them.

**Chris Gammell:** I hope so.

**Dave Jones:** I'm sure you do. But it's pretty safe because I know the market. I have, you know, I have a decent market to sell into.

**Chris Gammell:** Yeah.

**Dave Jones:** And, you know, if worse... The worst happens, you can always sell at cost, you know. As if people wouldn't, you know, buy a multimeter at cost. They'd sell like hotcakes, you know.

**Chris Gammell:** Right. Yep. So, you know.

**Dave Jones:** So, it's impossible to lose your money. Almost. You know. So...

**Chris Gammell:** Oh, I've been working on ways to lose my money for my whole life, Dave. Come on.

**Dave Jones:** Right. Yeah. No, but serious. If you buy something popular like a multimeter, as if you couldn't sell it at wholesale cost. Oh. Yeah. Of course you could, right? Right. I think you could. People just whack them on eBay at wholesale cost and they'll fly off the shelves. Yeah. Yeah. Like so. So, you can always get your money back. So, the actual downside risk is practically zero. But the upside risk is, yeah, you tie up your cap and you tie up your cash. Yeah. You know. Yeah. And it's, yeah, it's a big outlay. Right. Well, I think another thing with that is... It is not thousands of dollars. You know. It's like, you know, it's more than a year's salary for a lot of people. It's crazy. You know. It's like...

**Chris Gammell:** Yeah. Well, I think so. We talked about lead times as well, right? And that kind of ties into the other, the cash thing too. Because it's like, if you say you didn't think about that one part that has the 20-week lead time.

**Dave Jones:** Yeah.

**Chris Gammell:** And you've already bought all the parts.

**Dave Jones:** Or somebody just... I've been gazumped with that before. You know, you get totally gazumped. They were in stock in DigiKey yesterday, but you went to press the order button today and the stock is zero. Yeah. Sorry, 12-week lead time. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** Like, yep.

**Chris Gammell:** Right. But you've already... The difference would be if you had already bought all the other parts, right? That...

**Dave Jones:** Oh, right. Yes. That kind of thing is... So you bought all the others, you spent all the money, and you're stuck on one bastard part you can't get. And now you're...

**Chris Gammell:** Right. The purple screw. Yep. Yep. Yeah. That's pretty rough.

**Dave Jones:** Jeez. And the red screw just doesn't cut the mustard.

**Chris Gammell:** That's right. Right.

**Dave Jones:** I do like coloured screws. I do like coloured anodised screws.

**Chris Gammell:** Where do you source those from?

**Dave Jones:** Plenty of places. Yeah? Yeah. The aluminium anodised socket head screws. Very popular. You can get them in all different colours. Fantastic.

**Chris Gammell:** I mean, to be completely honest here, Dave, I mean, I've always had people that were doing mechanical stuff for me. Yeah, I know. No, exactly. You know. I mean, I know we've talked about it, and I'm getting into it, and you're getting into it, and it's like... But, like, you know, that is a...

**Dave Jones:** These things matter, you know?

**Chris Gammell:** Yeah. I mean, yeah.

**Dave Jones:** Like, I've worked on projects where the external part of... Or if there is no case, the PCB is the case, and the mounting screws are visible. You know? It's like, yeah, you're going to use nice socket. No, it's Philips bloody garbage. You use nice socket cap heads, right? With, you know, hex cap heads with... You know, and you can get them in multi-vibrant colours. In five fruity flavours. Like, yeah, it's great. You know? Looks are a big thing. So...

**Chris Gammell:** Yeah. Well, yeah. Sure.

**Dave Jones:** You're not a fanboy. No, I mean, I just... Yeah, you've just never been involved in it, right?

**Chris Gammell:** Yeah, I just... I don't... The products I've worked on have always been much bigger than the part that I've worked on. You know what I mean? I've never been a significant enough contributor to a big project like that, so... Got it. But, yeah, that's... Thinking about that stuff's good. I think that helps to differentiate products and stuff like that, so... That's good. What other links do you want to talk about? Because I have one on here that I want to talk about, just because...

**Dave Jones:** Well, go for it, because our hour's up.

**Chris Gammell:** It's not quite up, but... Three minutes. I think this was Greg Charvat on Facebook shared this. There's a video of a guy that has a jumper cable on a 500 kilowatt... Or 50 kilowatt AM tower. Did you watch that one?

**Dave Jones:** No, but I want to.

**Chris Gammell:** Oh, my God. It's so good. Basically, he pulls... He's pumping... He's shunting current around something using a cable. He pulls the cable off, and then it sparks across the gap. But because it's like... It basically becomes a plasma speaker, because that much power is going through it. Ah, yes. I've done plasma speakers. They're very cool. You can hear the radio... The radio... The audio, rather, that's being pumped out on the radio. And it's just... It's so freaking cool. And it looks so dangerous. This guy's so nonchalant about it. He's just some workman dude. He's like, yeah, whatever. All right. Yeah, that's crazy. That much power. I'm watching it now. Yeah.

**Dave Jones:** Yep. He looks like he doesn't really care. Yep. Like, nothing but phasing.

**Chris Gammell:** Any kind of thing you're... Any job most people are in, they get normalized to that stuff, right? Yeah. Oh, no. Totally. And that actually is very dangerous, I think, too. You know, getting too comfortable with something like that. That's where habits really are quite important. So, having good training up front, that kind of thing. Right. But, yeah, it's... It was crazy.

**Dave Jones:** Anyway. Yep.

**Chris Gammell:** What else?

**Dave Jones:** It's like the workers who worked on, you know, back on the Empire State Building. You know, you see the photos of them. Yeah. Just, you know, out there walking on the... You know, having lunch, just sitting on the beam, hanging over. But, you know, like... Pass. Maybe that can be the photo for today's... Yeah. You know. But, yeah, you become normalized to it, you know? Yep. So... Yep. Yep. Ah, boy.

**Chris Gammell:** Lots of other stuff about... I've seen more and more stuff about security. I mean, obviously, we talked about that, I think, last... Two weeks ago, we talked about that. Boring. You and I don't really know much about that. No, we don't. Got some feedback that people were interested in hearing about that stuff. Obviously, when we talked to SAR last week, SAR was a security researcher. We've had other security researchers on the show, like Michael Osman, stuff like that. We have? I think, you know... Again, I think I've mentioned this on the show before. Usually, the stuff that I'm doing is so low-level that there's not enough intelligence to really have... To require security. But I think that, you know, being part of a larger system, yeah, that stuff is actually quite important.

**Speaker ?:** There's...

**Dave Jones:** Got it? Yeah. Somebody's got a do-it-yourself optical inspector.

**Chris Gammell:** Oh, yeah. That's Bob. Bob Baddeley. Yeah.

**Dave Jones:** I haven't... If people don't know, this is a more obscure bit of kit on a surface mount production assembly line, which I haven't really seen people do before. I haven't heard much, you know, much murmur about it, really. And basically, what it does is when the board comes out of the thermal oven, it goes into an optical inspection camera. It's just a camera. And it looks down on the board, and then it can identify each part to make sure it's there. It can compare against templates. Right. And all sorts of stuff. And it can detect if there's, like, a tombstone. So, like, if you expect to see...

**Chris Gammell:** Or if you detect tombstone in... Yep. Yeah, a resistor with two silver bits on the end, and you only see one silver bit, it means it's probably tombstone, that kind of thing, right?

**Dave Jones:** It's probably tombstone. Yeah, exactly.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And it flags these things, and, you know, or it can read ID, you know, component ID numbers. Yes. Oh, yeah. It's the right part down. Yeah, that is a 221, you know, ohm resistor, right? So, yeah, it can read the part code. You know, it knows if the component's been put in backwards, right? Because the text is upside down, you know? Things like that. And, yeah, these optical inspection things. So, anyway, which it's not hard. It's just a camera and some smart software.

**Chris Gammell:** No, but the software is the important part, right?

**Dave Jones:** Well, which, yeah, Bob's using OpenCV, which is a ridiculously powerful open source optical visual camera, you know, thingamabob. I know what I'm talking about. Yeah, camera thingamabob, that's right, yes. And, yeah, so he's using that to identify parts and things like that. So, that's really jazzy.

**Chris Gammell:** Yeah, no, I think it's actually really good. And Bob was, I remember, part of, he was one of the early classes of Accelerator, and he's been doing some other interesting things with manufacturing and stuff. And this is actually, I think he writes about how it's on-site. He's doing on-site, his own manufacturing as well. And there's some posts about why he did that. So, I thought it was, yeah, it's actually really interesting stuff. So, it's a good use of readily available technology with some software on top. So, that's good.

**Dave Jones:** Yeah, no, that's it. It's basically a webcam stuck on an arm, and it looks down onto your product, and you light it up, and Bob's your uncle.

**Chris Gammell:** Yeah. No, no, Bob's the author of the article.

**Dave Jones:** Oh, dear.

**Chris Gammell:** Yeah.

**Dave Jones:** That's bad.

**Chris Gammell:** What else have you got going on this week? Because we should, let's tease for next week.

**Dave Jones:** What have I got going on? Oh, I'm staring at schematic at the moment for my new product, trying to fix it for them. Nice. Telling them, do this, do this. No, you can't do that. Oh, Dave, the product manager. You've got to use this chip. That's right. No, you've got to watch your grounding on this one. That's important. That's good. Like, I actually want to draw them visual. You know, I'm going to mark up the schematic. Now, it's a big A3 schematic. I'm going to mark it up, and go, you know, this ground needs to connect to this point over here, because, you know, it's going to be a problem, and yep.

**Chris Gammell:** Yeah. Yeah. I was talking to an engineer recently who was telling me, you know, obviously every company is different, but, you know, like, especially as you start working in larger and larger companies, you know, what your focus is around, you know, if you're system design versus, you know, electronics design versus working with a design house or CM or EDS or whatever. And it's really interesting to just hear these different perspectives on it, because I've obviously worked in, you know, small to medium-sized companies. But when that gets really big, it kind of more mirrors what you're doing. Not saying you're doing a big thing, but more like having external design teams where your main role is defining the system and then doing review around that system. Exactly. It sounded very similar. So, that's cool. That's good. I mean, and that's good. It's, I think that probably some of our listeners have a similar kind of work setup, and there's a lot of challenges to that as well, because you can't micromanage, but you sure as hell want to, I bet.

**Dave Jones:** Oh, yes. No, it's, yeah, it makes me want to, yeah, it always makes me, like, if I had access to the actual schematic, I'd be making changes. You know, if I had access to the PCB, I'd be making changes, you know. Exactly. Yeah. It's almost frustrating that you can't, you know. Yeah, right. You know, you have to mark things up. Yeah, you have to kind of trust people, but also you have to. You have to trust things, and then you don't get it back for a week, because it, like, you tell them what to do, you know, in the best way as possible, and then you've got to cross your fingers that the next schematic they send you is, you know, is fixed, you know, and does what you want. And it's, you know, so, yeah, otherwise, you know, so it can take time.

**Chris Gammell:** Yeah, so you've got to be more explicit in your descriptions and more very careful with your wording, stuff like that. Exactly. Yeah, no, that's, that is definitely a challenge.

**Dave Jones:** You know, like, I'm just looking at the schematic here, and right off the bat, I can see that they've added this extra chip in, and, well, the protection circuitry's now in the wrong place. It's got to go on the other side. They didn't, you know, they didn't think about that, but it was bleedingly obvious to me, so I've got to tell them to fix that, and, you know, so, yeah. So people will know, some, a lot of people will know what I'm working on. So, yes, I'm doing real engineering, Christopher J. Gamble.

**Chris Gammell:** I am very proud of you, James. Thank you very much.

**Dave Jones:** I'm reading data sheets, looking at graphs, and going, no, we can't, can't use that.

**Chris Gammell:** How's it feel? Back in the saddle? No, it's good.

**Dave Jones:** Yeah, yeah, yeah. I wish I could do more. It's time, you know. Exactly. Somebody asked this on the forum. What if I could do a video on my dream lab? You know, what I'd want in my dream lab? And I thought about it for a second, and I went, the answer is, yeah, the answer is time to work on stuff. That's my dream lab, where I walk in there, and I have an infinite amount of time to work on stuff. Like, it's got nothing to do with the gear, you know?

**Chris Gammell:** Right. Well, you've already got all that. Yeah, no, exactly.

**Dave Jones:** I've got gear coming out the wazoo, right? It doesn't like you.

**Chris Gammell:** Yeah, you've got more than you figured out. Do you have time to figure out how to work? Yeah. Yeah.

**Dave Jones:** And we should mention the big thing, which is being discussed on the forum at the moment.

**Chris Gammell:** Sure.

**Dave Jones:** Probably close off on this. Is the new Keysight giveaway next month coming up, right? It's going to be huge.

**Chris Gammell:** Is it you giving away, or is it them giving away?

**Dave Jones:** Both.

**Chris Gammell:** Okay. Oh, like joint thing?

**Dave Jones:** Have you heard about this?

**Chris Gammell:** I saw your video about a giveaway. I didn't know. So you said some people are on the forum, but some people are on the mailing list, that kind of thing or something.

**Dave Jones:** If you're not on the fail forum, then you won't be able to win it.

**Chris Gammell:** Active member on the forum.

**Dave Jones:** Yeah, active member. So, yes. Right, right. As in, yes, I don't know the post count yet. Anyway, this is an interesting thing, right? Basically, I'll tell you what's happening. In March, because it's public knowledge now, March, Keysight are giving away a scope per day, right? It's the scopeamonth.com or something. And not just any scope. They're giving away their one gig 3000X series. One gig. Right? 15 grand worth of scope. They're giving one of those away per day, plus giving away a couple of other even bigger things. Right? It's like half a million dollar giveaway. Right? One of those one gig scope per day. Right? It's like, mind blow, right? Yeah. So, yeah. It's just, you know, it's incredible. And what they've, I negotiated that they would give me two scopes so I could give away to my loyal viewers. Right? Which was very nice of them. In return, you know, they want some publicity for the contest, which I'm giving them now. They just got some. Right. We should, The Amp Hour should have. Damn. Damn. The Amp Hour should have got a scope to give away. Yeah, well. It's too late now, I think. Anyway, it's going to have like custom EEV. It's going to be special. It's going to have custom EEV blog branding. So, it's going to have my little face hand on it and stuff. EEV blog special edition. Wank, wank. Okay. Who cares? But the interesting thing is, right, I asked on the forum, okay, how can I do this giveaway? And basically, so many people said, like, you can't. You can't give away a one gig. Nobody is worthy of winning. Seriously, nobody is worthy of winning a one gig scope. Who the hell can actually make real productive use of a $15,000 one gig scope? And I thought about it for a little while. I actually do agree with that. I came to the same conclusion. I, like, yeah.

**Chris Gammell:** So, I've been working with, my coworker, Dan, has started, we have a design lab at Supply Frame. And we have, like, we're building up the lab and we're talking about what should we have there. And I'm like, you know what? You don't put a one gig scope in there. You put in 10, 100 megahertz scopes because no one, nobody needs, I mean, like, a couple people that's, like, like, Shariar needs one gig and above scopes, right? Like, people like that totally do.

**Dave Jones:** If they're doing his research on, his bleeding edge research on 10 gig, you know, transmission

**Chris Gammell:** systems. It is a pyramid. It's like, very few people need a one gig scope. Exactly. My, my formerly given to me scope has not been used to its full potential, right? I mean, like, it's for the once in a while times. Every, yeah, exactly. So, I totally agree with that. Doesn't mean people don't want to get it.

**Dave Jones:** Yes, because you, you, you, like most bloggers, got one of the MDI 3000, right? The 500 meg, right?

**Chris Gammell:** Yeah. And the RF card was the more important thing, right? Yeah, of course.

**Dave Jones:** I'm giving it away like candy. But yeah, how often are you going to use that 500 megahertz, you know, like, like practically never? Right.

**Chris Gammell:** Well, I just got mentioned. So, I suppose that comes.

**Dave Jones:** It's, and, and I came to the same conclusion. They're right. Nobody deserves this scope. Damn it. You know, and I've got two to give away. And it's like, I think it's too late. I think they're already on the way or something.

**Chris Gammell:** So, it's like. I don't think it's, it's not a deserved thing. It's just no one actually needs it on a daily basis.

**Dave Jones:** Nobody needs it. So, everyone says, oh, sell them, you know, sell them and buy 10 scopes, you know, and then give away 10 scopes. And like, I don't know. So, it's like, so I'm stuck between the rock and a hard place, you know? Like, I totally agree. Like, it kind of, it almost sucks having two 15 grand scopes to give away. I guess that's a monetary thing. Sounds ridiculous, doesn't it?

**Chris Gammell:** I think, I think that the takeaway is like, like, there is a pretty strong consensus there that, you know, when people like lust after like a high-end scope or something like high-end equipment like that, like, that's a sometimes food, right? Right. That is the, that is the, the moose of the, that is the, that is the, whatever. It's a fancy dessert. You don't need it all the time, right? No, no, no. You want the ice cream sandwich. The ice cream sandwich is the regal scope, right?

**Dave Jones:** And yeah, as, as, as you were saying, like, even a hackerspace doesn't really. You don't.

**Speaker ?:** You don't.

**Chris Gammell:** You benefit by, you benefit by having more of a simple thing because most scopes.

**Dave Jones:** A more usable tool, you know? Right. Maybe a 200 meg scope or something, you know, like, not a $400 scope. If I, if I had the luxury to sell these things, which technically I do, right? Because they're mine legally. Sure. Then, you know, yeah, I'd go, maybe go out and buy five, two grand scopes or something. You know, that's a more, you know.

**Chris Gammell:** I guess. I mean, it's all, it's all, you know, horses for courses. Is that the right phrase? Is that what you said? Is that the right phrase here? I don't actually, I've never known.

**Dave Jones:** Well, horses for courses. Yeah. You have the right tool for the job, basically. Sure. Okay.

**Chris Gammell:** That's what I mean. Horses. Horses. Yes. Horses.

**Dave Jones:** So what do I do? What do I do? I'm stuck in this position of having to give away these two.

**Chris Gammell:** First world problems. First world problems, Dave. First world problems. Yeah.

**Dave Jones:** Giving away two scopes that are worth more than a new car. How about. Right?

**Chris Gammell:** Sell the two scopes and donate the money. I don't know. To an educational program.

**Dave Jones:** So, like, technically I can do that. Legally, Keysight are giving them to me. They're mine. I can do anything I like with it. But that's bad relations. You know, it's bad public relations for me to go sell them and then go and buy RIGOL scopes and give those away. You know, it's like, as much as I want to, you know, as much as I think, you know. Although, like, with hindsight, right, with, I didn't, like, I didn't think. I just went, oh, yeah, give it, like, I didn't know that they were actually going to be one gig scopes, right? I just said, oh, they didn't tell me. I didn't know the details at the time. Yeah, we'll just give you two scopes. And I thought they'd give me, you know, maybe a five grand scope if I'm lucky, you know.

**Chris Gammell:** Right.

**Dave Jones:** Kind of thing. But, yeah, no, they're like the one gig model. Holy shitballs.

**Chris Gammell:** You'll figure it out. Oh, yeah.

**Dave Jones:** So, with hindsight, I wanted just to ask, like, because they actually wanted me to promote this thing. And, like, I don't take money for promotion or anything like that. So, I said, look, I'll do the promotion in return. Just give me a couple of scopes so I can give them away to my viewers, you know, so my viewers win, right? So, they get something out of it. And with hindsight, I probably should have went, well, just pay me, you know. Just give me 10 grand. I'll make a promo video for you and I'll go buy, you know. And then with the 10 grand, I could have, you know, went and bought Xscopes. It's a problem that's pissing me off. It shouldn't be, but it is, unfortunately. So, I don't know. What would you do?

**Chris Gammell:** You're asking me or the crowd?

**Dave Jones:** Audience.

**Chris Gammell:** I'm crowdfunding the solution. I'm crowdsourcing. Yeah.

**Dave Jones:** Yeah, you'll just laugh from the sidelines.

**Chris Gammell:** Yeah. I don't know. You'll be fine. Yep. I think you're, you know, honestly, I think you're doing the right thing. The community matters. It's good that they're, you guys are all talking about it. That's good. Honestly, it really is. So, what I'm trying to say is. Suffering my jocks. Join the EEV blog forum. That's a, that is a good idea. There is actually, I think there actually is a really, I can't do forums. I can't keep up with them, but I think that. Right. Obviously, you have a very good forum there. So.

**Dave Jones:** It's awesome. Yeah. It's one of the best forums I've ever belonged to. Although I'm biased.

**Chris Gammell:** A little bit. But that's okay. I think, I think, I think you get it that one time. Yeah. But. Cool, man. Well, next week we will either have a guest. I have a guest, a robotics guest lined up at some point. I'm excited about that. Or we do need to do another call-in show. I will be back home. So.

**Dave Jones:** Yeah, we. Yep.

**Chris Gammell:** We'll have one of those. If.

**Dave Jones:** I've only ever done one call-in show.

**Chris Gammell:** Really? No. Yeah.

**Dave Jones:** Yeah. Two, right? No, I think I've only done one.

**Chris Gammell:** Who was. No.

**Dave Jones:** Was it two? Okay. Yeah, no, there was two.

**Chris Gammell:** We've done three so far. So it was. We did the first two. And then I was with. At least you and Chris for the second. The third one, rather. So.

**Dave Jones:** Right.

**Chris Gammell:** Yeah, we'll do another one though soon. And we'll definitely announce it on the blog. And post it in places. When we do that. Again, we've been. The last two times we've done that. We were going to call you back. If you'd like. If you. If you have a burning question you'd like to ask. And you want to call in. And leave us a voicemail. So that we'll know that you're interested. You can call. 929 amp hour. At any time.

**Dave Jones:** Oh, that's sweet.

**Chris Gammell:** Yeah.

**Dave Jones:** Why couldn't you get triple five amp hour?

**Chris Gammell:** Oh, sorry. The area code is not. Is not under my. Damn it. Sorry. So. 929 amp hour. There's also an 800 number. I can find it here. Phone.

**Dave Jones:** 929 amp hour. Sorry. I can't do it like a radio announcer's voice. Right.

**Chris Gammell:** Right. Well, the. The. 827. 6255. That's the one I was. Call now.

**Dave Jones:** We'll be giving away free icy cold cans of Coke.

**Chris Gammell:** Sorry. Yeah. So the. The call. The toll free number is 1-855-967-8699. So you can call that. From anywhere. You should be able to call on Skype from anywhere and leave us a voicemail. So you can do that at any time. And we'll just. Yeah. So. We'll set up a time to call you back and stuff like that. So. You can call us at any time. 929 amp hour. Or 1-855-967-8699. And. Yeah. And that will be for our next call on show. Not sure. If it's going to be next week or the week after. But. We love talking to you guys. It's. I. Actually. I really do like the call on shows. I think they're really fun. Yep. I think the timing is always kind of a little weird. But if we really work it out. If we need to. We can. Split up the times and call different time zones. If we really need to. So.

**Dave Jones:** Dude. We sound like a real radio show.

**Chris Gammell:** Sort of. Minus the advertising. Uh. Someday. Someday. Maybe. Maybe not. Who cares.

**Dave Jones:** No. We're.

**Dave Jones:** Patron. Supported. So. That's right. Thank you very much to all. Patrons. If. Patreon supporters. Patrons. Patrons.

**Chris Gammell:** There are Patreon patrons. Patrons. Yeah. Sure. Yep. Yeah.

**Dave Jones:** So. Yes. Which we always link in. Somewhere. Or it's on our website. If you want to help support the show. Keeps it going. Pays the bills. Keeps the lights on. Yep. That sort of jazz.

**Chris Gammell:** Cool man. Cool. Uh. Talk to you next week I suppose. Good show this week.

**Speaker ?:** Yep.

**Dave Jones:** Catch you next time. See ya.

**Speaker ?:** Bye. We'll be right back.
