---
episode: 172
title: CAD courses and cross platform creation - Printing Propaedeutic Patterns
url: https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/
---

**Chris Gammell:** This is the Amp Hour Podcast. Recorded November 19th, 2013. Episode 172. Printing Propideutic Patterns.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Hey Chris. Hey Dave. How's Contextual Electronics going? Have you launched that sucker yet?

**Chris Gammell:** Not yet. It's getting there. It's probably another month or two. I'm thinking like early January.

**Dave Jones:** He's been saying this for six months, folks.

**Chris Gammell:** Of course, yes. Well, you know. But it's a shitload of work, though. Yeah.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Yeah, I posted a picture the other day, actually. I should send you that. I didn't post that on the Reddit links. But I posted a picture of the latest layout. And it's been getting kind of crazy, actually. I like the layout and everything like that. And it's mostly, you know, if this was just me, it wouldn't be a big deal. Right. Of course. But it's because it's, you know, doing it in public eye and recording everything. That's right. And yeah. So that's the real thing.

**Dave Jones:** Makes it different. I haven't seen it. What is the final project? It was like a data acquisition thing, right? Yeah, sort of. Has it expanded? Has it blown out from that?

**Chris Gammell:** Yeah. Well, a little bit from that. It's called Bench Buddy with the...

**Dave Jones:** Bench Buddy. It reminds me of the bathroom buddy from Gremlins. That's right.

**Chris Gammell:** Exactly. Except I had to change the spelling on it because a while back when someone was interviewing me about it, I looked it up finally and I'm like, oh crap, that's trademarked. Oh, really? So now it's spelled with the... It's B-U-D-E-E. Oh. Because it's... Oh. Oh. Oh. Yeah, lame. I know. Oh.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** But yeah, so I sent you the link there. It's basically, it's ATX power supply that then goes to... Right. Watch out, we got lots of wank input here. So it's an Arduino controlled output, right? So you can have like a display and everything like that. And then basically there's a DAC that also drives a current source. There's an ADC that can measure high level or thermocouple inputs. There's a positive negative rail that's adjustable. Right. There's a relay circuit for like high voltage switching type stuff. Yep. And then there's an LED... I see it. LED driver, basically. The idea being that like kind of like everything you need to do, not everything, but you know, just kind of like a multi-tool for your bench. So measuring signals, outputting signals, outputting power, and doing it kind of cheap. I don't know.

**Dave Jones:** The ATX power supply is a bit overkill, although I can see why you did it. I mean, it's not like you...

**Chris Gammell:** Oh, yeah. Oh, yeah.

**Dave Jones:** Those little pissant tracers you got on there, they're not going to carry, you know, 20 amps.

**Chris Gammell:** No, there is. Yeah. But the output, you know, they're just LM317s and 337s. It's nothing fancy. Right, yeah, yeah. Because cost is an issue too. So it's like... Right. It's all current limited. I got PTC thermistors in there and stuff too.

**Dave Jones:** And they're tiny little PCB heat sinks on there too. Yeah, exactly.

**Chris Gammell:** It can't do any significant power, but I don't want it to. It's just that ATX is super cheap and actually really quiet. I was really surprised. Both, you know, actual like auditory noise, the fans on those things, and then the actual supply output as well. I'd expect it to be like super janky, you know, like tons of noise on it. But it...

**Dave Jones:** Yeah, no, they're quite reasonable. Yeah.

**Chris Gammell:** Yeah. I was very pleasantly surprised. And then I put some extra filtering on it too. So, yeah. Sweet. It's kind of, you know, it's going to be open source too. So that's fun. Of course. Multi-tool. And, you know, made with KiCad, of course. This sales announcement brought to you by... By contextual electronics. Yeah. But, yeah, it's been going good. It's just... Just take it forever.

**Dave Jones:** Well, see, that's the thing, isn't it? I mean, this is why... Like, there's a lot of people who don't realize how long it takes to get shit done. You know? It's especially when you... As you said, doing it in the public eye and shooting video while you're doing it. And, you know... Right. Well, I remember your power supply video. Power supply thing. Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Exactly. It's gotten to the point where I refuse to do that anymore. You know? In the public eye.

**Chris Gammell:** Of course. And I think the key there, though, is that I'm doing all this stuff. This... You know, the actual design inputs.

**Dave Jones:** Before it's launched.

**Chris Gammell:** Yeah, exactly. No one...

**Dave Jones:** That's it. You know?

**Chris Gammell:** We'll be going over all the concepts. No one can say, you're doing it wrong. Yeah. And I learned that from you, honestly. Yeah. That's a very difficult thing to do. Yeah. You know, it's like the... You know, what's it? Bike shedding. Bike shedding. Where... And we've talked about that once on the show before. Where if it's a committee talking about a nuclear reactor, you know, they quickly pass through the $10 million reactor plans. But everybody has an input on the color of the bike shed out back.

**Dave Jones:** I got it. Got it. Oh, boy.

**Chris Gammell:** That happens all the time, though, you know?

**Dave Jones:** Yep.

**Chris Gammell:** So, yeah. It's... It's going good, though. Yeah. It's getting there. If people are interested, you know... Oh, that's actually the other thing, though. I meant to mention this a couple weeks back. I did a seven-week video course on building a little blinky board. Yeah.

**Dave Jones:** I've seen that.

**Chris Gammell:** Yeah. That was... It was a little long, to be honest. And people called it out on... It was on Hackaday. Right. Rightfully so. It was a little long. But it's basically getting through KiCad. Maybe you could even, you know, get through KiCad. I know you evaluated KiCad.

**Dave Jones:** Oh, well, no. I did a first impressions video. Right. Of course. I used it for the first hour, and that was my video. And that's it. I haven't touched it since.

**Chris Gammell:** Yeah. I don't know, man. I...

**Dave Jones:** But once again, like, people think that they can do this thing much quicker. Well, you... You know, you can't. Because you were doing it effectively real time there, and you're trying to explain things and waffle, you know?

**Chris Gammell:** Right. And there was a lot of waffle, yes.

**Dave Jones:** There was a little bit of waffle, but, you know, I mean, that's... Like, it's not going to suddenly take one-tenth that time if you aren't doing that. Yeah. Right. Right. You know, it might halve the time or something, but, you know, how many hours total did you have on those videos?

**Chris Gammell:** It was one and three-quarter hours. It was a little bit more than one and a half.

**Dave Jones:** See? One and three-quarter hours getting to Blinky. No, I'm sorry. You know, if you laid out that board yourself... Yeah, oh, that's ten minutes. ...right? It's not going to... It's not... Well, it's not going to be ten minutes, right?

**Chris Gammell:** Well, it depends, though. I mean, like... So I was thinking about comparing it.

**Chris Gammell:** So, like, a good example is, like, Upverter, right? Upverter, you know, you can do it really... Right. ...you can do it quickly, but, you know, that's grabbing components. That's under the assumption that you have all your components. That's right. But as you and I and many of our listeners know, that when you're using a CAD program, you know, such a significant portion of your time is putting parts in for schematic, for footprint, verifying if they're already in there, which is a big step that everybody skips, including myself, and then you curse, and you curse, and you curse.

**Dave Jones:** And then there's looking up parts on DigiKey. You know, sure, if it's just a triple five, right? Yeah. With through-hole resistors, right, you're going to have these parts in your libraries already. So it's not an accurate example of how long a simple board with a couple of chips would take. Yeah. You know, because it really is the bottom of the rung. Yeah. Kind of.

**Chris Gammell:** Yeah, and it's tough, you know, like, when you're trying to compare it. So, like, the whole idea behind getting to Blinky was comparing it to getting an Arduino or a BeagleBone or something like that, and, you know, blinking that first LED. That's a really important first step to make sure you understand the compiler and everything like that. But if you were to go in and, you know, verify all your libraries, all your dependencies, that could really be a pretty deep dive. They're always just set up for that kind of thing. That could take a day or two.

**Dave Jones:** Yeah. Yeah. That's right.

**Chris Gammell:** Oh, I hate that part of projects when you're just trying to get to that point. But...

**Dave Jones:** Well, I've had that with the Arduino in the past. You know, it's had issues. It just didn't work for me first go, and I had to spend half a day, you know, reading the forums to find out what idiot thing I've done, and then I go, and then I find out, oh, no, this version is not compatible with that board and this driver, and, you know, all these drivers, like, they weren't compatible. And if it doesn't work first go, you're screwed.

**Chris Gammell:** Yeah. And it's super frustrating, too, because you're like, everybody else got it, and you're on the forums. You're like... Exactly. I can't describe my issue, because if I try and explain it, it sounds like I'm just crazy.

**Dave Jones:** You know, like, I'm doing everything right here. Yeah, I know. And everyone goes, oh, you just plug it in, and it works. And it's like, no, it doesn't. I swear. Right. And then once you get to the end of it, you find out that, yeah, Murphy got you, because you had some board, and you were running some old version of this or that, and, you know, you were trying to do one thing which didn't have the compatible library, and, oh, I've gone through this before, and it's just, you know...

**Chris Gammell:** Yeah.

**Dave Jones:** Even the simple things can screw up completely.

**Chris Gammell:** Right. And the key, I think, for that is if you're... Yeah. You know, it's like if you have someone who is coming into it, right? Arduino is a great example of something where it's very welcoming because it is, you know, it's a simpler interface, it's friendly code, that kind of thing. And as long as you're following along, there is a higher likelihood of you, you know, finally making that blink and then get started. And that really, it's all about, like, momentum in that case, right? So having someone getting started and, okay, okay, I'm doing this, I can do this. And then you get the blink, and you get that, those rush of endorphins or whatever the hell is in your brain. And, you know, and it's just exciting, and you want to keep going with technology. If you stumble in that path, though, you know, that could just be the end. That could just be like, oh, well, I guess programming electronics or tennis or, you know, water polo isn't for me, you know? That's it. So, yeah, it's important. It's important to try and, I don't know. Yep. It's tough.

**Dave Jones:** How many things can go wrong with a simple blinky circuit like that? I mean, off the top of my head, I can think of one, you know, easy one that always, Murthy always seems to get you, you know, you do your circuit, you lay out your board, everything's hunky-dory, and you order your parts from DigiKey, and your parts turn up, and you go, oh, it's the wide package chip instead of the narrow package chip. And it's like, oh, it's like, you know. Yeah.

**Chris Gammell:** Actually, I ended up, so the first go-round, I actually put the wrong. I measured, oh, how about this one? I did inner diameter instead of outer diameter for the via, or sorry, for the through-hole component that I used, so it was that battery holder, and it was like, I think it was like 85 mils. It was just showed 85 mils, and I think that was the drill size, and I used that as the outside diameter, so that when I interpolated that for the drill size, it was like, oh. So, you know, I filed it down, and I squeezed it in there, and then I remade the video, but yeah, it's tough. You know, like, that's the hard part of hardware, but it's, I don't know.

**Dave Jones:** No, I, well, anyway, I think that hour and something total for your videos was bang on.

**Chris Gammell:** Yeah, actually, a good comparison, Jeremy Blum just finished his, he did a third video about Eagle as well, and after the fact, someone pointed out, hey, Chris, you made the exact same circuit as Jeremy, and I'm like, oh, well, 555, okay.

**Dave Jones:** Yeah, yeah, right.

**Chris Gammell:** And then I wrote to Jeremy all sheepishly, I'm like, hey, I made the same video as you by accident. But actually, his was three half-hour videos as well, so Eagle, Kaikad, the same kind of thing.

**Dave Jones:** Yep.

**Chris Gammell:** So that was kind of vindication. For sure. Yeah, that's, his has crazy views on YouTube, too. Something like a couple hundred thousand, I think. Man, it's awesome. Yeah, yeah, I don't know, it's insane. Awesome. And that's why he works at Google now. Right. Yeah. So Kaikad has some interesting news. I don't know if you saw this a couple weeks ago. Tell me. So CERN, the particle accelerator out of Switzerland.

**Dave Jones:** Yep.

**Chris Gammell:** They are officially putting people onto the Kaikad project. So Kaikad is an open source software project. Anyone can contribute. However, you know, this CERN, this large lab is basically dedicating people to improving the software even faster. That's effectively what it's going to be. So they're putting money in to have people work on stuff, and it's going to increase feature sets and stuff like that.

**Dave Jones:** Now, how are they doing this? Are they sort of just taking the existing developers and now paying them to work on it full-time, or are they bringing in their own talent?

**Chris Gammell:** No, no. I think they're bringing it. I mean, they already had people that were contributing on the side. Oh, right. Okay. Basically, they're kind of rolling it into duties. And then I think they're also asking for donations as well from the community if people are interested. Basically, there's no way to do that right now either, right? You think about an open source project. It's like you could go and try and pay one of the developers who's doing it in their part-time, but you can't just donate money to something and say, all right, now do it more. So basically, this is another pathway for that as well. So say there's another company that started using KiCat or any other type of program like this. They could go to this entity, CERN in this case, and say, here's $100,000. Let's pick up the pace, boys. And that's kind of the idea. Awesome. That's really exciting. And looking at some of the stuff that's coming out, I mean, you weren't on when Adam was on, but he was talking about this a little bit. But just some of the features that have come out recently with the Python scripting, there's a new 3D engine for KiCat.

**Dave Jones:** There's push and shove routing, I think. Oh, yeah.

**Chris Gammell:** Yeah, yeah. That's another one. Right. So yeah, a lot of exciting stuff coming out.

**Dave Jones:** I'm definitely going to have to get back on this now.

**Chris Gammell:** Yeah. Yeah. Screw Altium. Altium. Well, and Altium just released, I think, 17. Is that right? Did you see that press release?

**Dave Jones:** Oh, I saw something about it. Whoop-dee-doo. Yeah. They got some videos or something.

**Chris Gammell:** Yeah. Yeah. So I don't know. It's just an exciting time. I think it's going to be good times for all. Now, the big caveat here is that Mac users are still kind of in the cold for KiCat, which is kind of unfortunate.

**Dave Jones:** Well, kind of, but like tough tits, you know? I mean, seriously, tough tits. I guess. Right? But it's... You know, these are... You know, I'd rather have a tool that works properly on one platform than some half-assed tool that works across all platforms. Yeah.

**Chris Gammell:** I'd say that's true unless you're a Mac user and then you're like, God damn it. You know? I mean, yeah. You could do virtual machines and stuff like that. And it's not too bad. That's personally... If I was a Mac user, I'd probably do a virtual machine and run on Ubuntu or something like that.

**Dave Jones:** But the fact is, the whole and the brutal fact is the Macintosh has always been a nothing platform as far as engineering tools go. Yeah. Yes. Right?

**Chris Gammell:** Yeah. Much like how Windows is a nothing platform for graphic and video editing tools. We always get left in the cold for that kind of stuff.

**Dave Jones:** I don't think that.

**Chris Gammell:** I think...

**Dave Jones:** I do all my video editing in Windows. Thank you very much.

**Chris Gammell:** Yeah. We've all seen that caliber. But, you know, no.

**Dave Jones:** It's just... I'm sorry. That's just the way the Mac's always been. It has not been a viable platform for most engineering tools. So, you know, why should it suddenly be any different?

**Chris Gammell:** I don't know. That is a good question, I guess. I mean, I think, in general, I think Mac is kind of a... It's been increasingly legitimized as, like, you know, a you-have-to-develop-for-it kind of platform. You don't see that?

**Dave Jones:** No.

**Chris Gammell:** No? Okay. Well, that's been my experience. I mean, just because of the huge increase in Mac users in the past 10 years. Now, maybe 20 years ago, I'd agree. But...

**Dave Jones:** No.

**Chris Gammell:** I do think it's...

**Dave Jones:** Well, is it... But isn't Mac going downhill a bit at the moment? Because Apple's not really pushing their... You know, they're so behind the curve in terms of Mac hardware and stuff like that, aren't they? That was my belief, especially in the Pro range, like in the Mac Pro desktops and stuff like that.

**Chris Gammell:** You know, we are just opening a doorway to hell right here, Dave.

**Dave Jones:** Of course we are. Why not?

**Chris Gammell:** I will just say this. I stopped paying attention. When I sold all my Apple stock, I stopped paying attention. So I have no idea. I literally have no idea.

**Dave Jones:** Well, see, this is what happened to me, right? I had so many people bitch at me. Why aren't you doing your video editing on a Mac? It'll change your life. Swear to God. It's the right tool. So I went, fine. I'll go check it out. Right? So I went to a freaking... Walked into a freaking Mac store against my own better judgment. And I said, show me your hardware. You know, show me your Mac Pro. I want your high-end freaking hardware. Even the people in the store laughed at me, right? You really want to buy a Mac Pro desktop? And I go, yeah. Because I... Why don't you want a notebook? Oh, because I can't put the freaking accelerator card in it.

**Chris Gammell:** Yeah.

**Dave Jones:** You dickheads. And I was practically laughed out of the store, right? And then I came back and I posted on the blog, you know, of my experience with it. And then everyone said, oh, yeah. Mac haven't been upgrading their Pro line for like three years now. And I go, well, why didn't you freaking tell me that?

**Chris Gammell:** I see. You're saying because it was desktop. Okay. Right. It was desktop. And I think that's realistic. I mean, maybe people that are... I use laptops. But, you know, it's not for high processing... So do I. ...high level processing stuff, right?

**Dave Jones:** Well, I do here. No, I've gone back to desktop at home now. But, yeah. Anyway. Yeah, no, it's just interesting.

**Chris Gammell:** It's interesting. Video aside, right? I think video is a different thing. But in terms of engineering tools?

**Dave Jones:** Well, no. Not even video. Because, once again, I used their most powerful Mac at the store. And it was slower than my... Slower for video rendering than my PC. Oh, yeah? Than my out-of-date PC. So, yeah. You know, I'm flipping the bird to the Apple people. I'm sorry.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? No. No. Sorry, I have no sympathy for anyone who says... Write your comments to EEVblog. EEVblog.

**Chris Gammell:** Care of. I don't know your PO box number. Otherwise, I'd tell them to send the bags of dog crap there. You're right.

**Dave Jones:** No, I don't care. Yeah. You know, if it's not available for Mac, it's not available for Mac. Tough tips. You know, if you don't like it, you go out and bloody compile it yourself for the Mac. Well, and I think that's what it comes down to. Don't sit there and complain.

**Chris Gammell:** I think that's going to be a realistic thing for lots of platforms, right? I mean, a lot of engineering tools in general. I think, you know, Windows is going to be around for a while, I'm guessing. But, you know, you think about just the rise of tablets and as people move towards that kind of stuff. I'm never going to run layout on a tablet, at least as far as I know, right? That's right. So what happens then? I mean, does that mean the default tools end up on Linux? Is that the idea? Because that's the only way to really do it anymore?

**Dave Jones:** No, it'll be...

**Chris Gammell:** Or you think Windows is going to stick around? Or, I don't know.

**Dave Jones:** Of course Windows is going to stick around. All these tools, including the high-end Macs and stuff, they must stick around because people need to do professional-level stuff. There's professional-level stuff and there's your consumer shit. And don't confuse the two.

**Chris Gammell:** That is true.

**Dave Jones:** Fine. You can run all your whole live, edit all your photos and do your wank-wank Facebook shit on your bloody stupid, you know, iPad. iPad, right? But don't think you're ever going to be able to do freaking layout on it. You're just not, right? You need those dual or triple, you know, 27-inch monitors, right? That's, you know, it's just...

**Chris Gammell:** Yeah, no, I agree with that. Maybe not 27-inch. That might be a little out there.

**Dave Jones:** At Altium, we had 30-inch monitors and it wasn't enough, okay?

**Chris Gammell:** Now, Altium, does that compile for Mac or no? No. No? It's just Windows?

**Dave Jones:** Yep. You can... There are people who use it on Mac, but, you know, they run it under the emulator, whatever it is. Yeah, the virtual machine. Wine or whatever it's called, yeah. Yeah. I don't know.

**Chris Gammell:** Oh.

**Dave Jones:** But no, it's not designed for it. And neither are any of your other industry tools. You know, neither are any of your cadence. Well, LTSpice is on Mac now. All your FPGA stuff isn't. Yeah. All of your cadence and all that sort of stuff. Forget it.

**Chris Gammell:** You know, I think technically FPGA compilers and everything else like that, I don't think those actually work on any platform. I don't know if you... Ka-ching.

**Dave Jones:** Yeah. It's not good. I'll pay that, yeah. Yeah.

**Chris Gammell:** They work one day, but then the next day they do something completely different. So, yeah.

**Dave Jones:** Well, no. Yeah. Here's an interesting thing which I was going to bring up before. It's a segue, right?

**Chris Gammell:** Okay.

**Dave Jones:** This is the thing about... I'm scared about KeyCAD, right? This is... I hate tools that you have to update on a daily basis or you're sort of, you know, because it's bug fix or whatever, right? I want a stable tool. I want a stable tool like here... I hope KeyCAD move in this direction because... Please correct me if I'm wrong, but at the moment... You sort of, you know, you almost have to keep up with the daily or weekly build or something like that.

**Chris Gammell:** That is not correct. You do not have to.

**Dave Jones:** Not correct.

**Chris Gammell:** You don't have to. You do not have to. You can. I've been on a stable... I've been on a stable Windows.

**Dave Jones:** But there's no, like, official release. Like, here... But there's no, like, you know, here's the stable release. We recommend everyone use this unless you're a, you know, absolute masochist. Right. And you want to update down. Yeah, you want to build your own stuff, right. Right. So that's what I hope it moves before. Here's version 14 of KeyCAD, and it's, you know, the one we recommend you use for the next nine months until we get push out the next major version.

**Chris Gammell:** Right. So if you look at the EXE on the KeyCAD mirror, which is out of France... Yep. It's dated 7... No, July 7th, 2013. So that is the latest stable. Mm-hmm. And that's BZR 4022. And I think that might be what I'm running. I don't remember. That's how... No, I'm on 4004. So the 4022, I think, has the better graphical 3D stuff. But honestly, I'm still locked back in the past. Right. And I'm going to stay that way because I've been making all these videos like this.

**Dave Jones:** Well, that's right. That's what I was getting at. Yeah, you want, as, you know, as a design tool, you want stability. That's more important than anything else.

**Chris Gammell:** No, I totally agree with that. Absolutely. I think if, you know, you can build your own stuff, right? But I think you can, you know, you can lock it down. Then you could just tell it to stop reminding you about updates and stuff like that. Now, if something's broken, then you're screwed no matter what, right? Of course. Yeah, yeah, yeah. So, yeah, I don't know. Anyway.

**Dave Jones:** Yeah, so I hope it gets more professional in that regard where... And as far as the downloads, too. Because if I remember correctly, it was like, oh, you want an actual Windows executable in-store file for KeyCAD? Oh, you've got to go to some guy's website who does it over here, you know? And, like, that's just not, you know, that just doesn't instill a lot of confidence in me. No, I understand what you mean. I want, you know, keycad.org and there's one button on there. Here is the latest stable Windows download. And that's, you know, like...

**Chris Gammell:** That exists right now.

**Dave Jones:** Like, I don't give a shit about GitHub and everything, you know, and everything else. I don't want to have to go to someone's, you know, server he's running out of his garage somewhere to download the latest Windows version.

**Chris Gammell:** See, that's how they've done it for years, though. I mean, come on, Dave. Yeah, I know.

**Dave Jones:** But if you want this to be taken seriously as a professional tool, it needs to look professional. And that starts from, you know, not having to, you know, go to some hack website somewhere to find the download, you know? It needs to...

**Chris Gammell:** Right. Well, if people go to keycad-pcb.org and then go to the download link, there is a click for Windows, at least, because that's what I use. And then there is a stable version there. So, that is the way to do it.

**Dave Jones:** Well, I think it was different. Like...

**Chris Gammell:** Yeah, it has changed.

**Dave Jones:** It was different when I did it. Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Because, yeah, I remember it was like, oh, people said just download the Windows, and I couldn't find it.

**Chris Gammell:** It was like... Right.

**Dave Jones:** You know, it just wasn't any good.

**Chris Gammell:** You're listed on their website. Me? Yeah, you are. It says videos from EEVblog. Oh, okay. There we go. This looks new, actually. There you go. I haven't seen this site in a while.

**Dave Jones:** Where's that?

**Chris Gammell:** Now he's interested. It's a tutorials link. And then... Oh, yeah. Videos from EEVblog.

**Dave Jones:** Oh, videos by EEVblog. There you go.

**Chris Gammell:** Yeah. There you go. Yep.

**Dave Jones:** There you go.

**Chris Gammell:** So, we'll make more of them now. Speaking of videos, there's a course for Altium as well that I just found out about. Yep. I've seen that. For... What's it called? Fedivel? I'm not sure if I'm saying that right, but the Fedivel Academy. Yeah, probably not. Yeah. But, yeah, it's for, like, high-density stuff, actually. Like, high-density digital designs that I've never actually done that high-density of a design before.

**Dave Jones:** Has he got examples of... I guess I'd have to watch the videos, right?

**Chris Gammell:** There's an open-source project they worked on, I think, with an IMX6 processor from Freescale. Okay, yeah. And they do all the different breakouts and everything like that, so...

**Dave Jones:** Oh, yeah. I see it here. Yep. Yeah.

**Chris Gammell:** So, yeah, there's another one out there. And... Hmm. Makes me feel good there's more people doing that kind of thing. Excellent.

**Dave Jones:** And people ask me why I don't do Altium videos. Well, I'm not going to do a free video for a tool that costs $6,000, you know? Piss off.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** If I'm going to do any, it'll be for, you know, something like KeyCat or some other at least tool that has a free version.

**Chris Gammell:** Yeah, right. Yeah, or wait until Altium comes out with theirs, right?

**Dave Jones:** Yeah.

**Chris Gammell:** If. If when. Yeah. If. Yeah.

**Dave Jones:** Exactly.

**Chris Gammell:** So, I want to talk about a trend, which I'm not sure we've mentioned in the past. It's going to get into something that I'm not very comfortable with, namely code. But I've seen like three or four Kickstarter, you know, crowdfunded type startups or projects lately. And they're all putting really high level languages on them. And I don't quite. I mean, I get it, but I don't get it. Can you give us an example? Sure. Well, the latest one is Python. It's called MicroPython. It says Python for microcontrollers. And basically, they compile a version. And then you can throw these high level commands at it. And it basically blinks light. It turns on, you know, it's just you're writing very simplified functions, you know. Yep. But I guess, and I should acknowledge that that's similar to, you know, any other Arduino clone or anything like that. But I don't understand the push other than maybe to get people interested in it. I mean, like, there's people that are really interested in, like, putting JavaScript on a microcontroller. I just, I don't understand that. And I want to.

**Dave Jones:** Well, because you just said it yourself. It's, you know, designed for those people who want to, you know, who know Python, right? Who are these software people who know Python, you know, and then they want to do hardware.

**Chris Gammell:** That's their language. Just know it. Because they already know it. They want to just get started quickly.

**Dave Jones:** That's it. And I don't see anything wrong with that, right? There's a market for that.

**Chris Gammell:** So, okay.

**Dave Jones:** Why should you have to force everyone on to using C on your Arduino or force everyone to using Assembler or whatever? Yeah. You know, I mean, why shouldn't people have a platform for the language that they know and like? I don't see an issue. I can understand where you're coming from than, from a, you know, from us hardware purist point of view. It's going, oh, no, you know, there's another, you know, why don't you just stick to C for everything?

**Chris Gammell:** Well, and I, yeah, I mean, I felt that impulse at first, but I think it's more about like, I kind of look at them like, well, is that? I mean, I guess that's just not, they're not really very, they don't need to run fast. They don't need to run small or anything like that. But I kind of look at it and I think, okay, is this, is this a, what's it called? A gateway drug? Is this a gateway drug into hardware? Or is this something where like people are going to be like, well, I want to run Python on everything now. And like, I understand Python's a very friendly scripting yada yada language, but I don't, I don't see the end game. And maybe, maybe I'm missing the point by thinking there is an end game.

**Dave Jones:** But yeah, I don't think there is. It's just, you know, the guy who developed is probably a Python fan and he figures there's other people out there who like Python and they'd like a board to run down. I don't think there's any goal of taking over the world here, you know?

**Chris Gammell:** Okay. What about JavaScript? I think Python is, is makes a little more sense too, as well. But JavaScript is.

**Dave Jones:** See, I don't know the difference between the two. I've got no idea that that's just lost on me.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Sorry. I don't write scripts for anything.

**Chris Gammell:** Well, JavaScript is what you use in like browsers and stuff like that. And like, that's just. Yeah.

**Dave Jones:** Yeah. I've done a bit of JavaScript 10 years ago, you know? Oh, yeah. But.

**Chris Gammell:** Yeah. I think I'm, I'm way too far out of my wheelhouse to understand, to know. But I, it just, it just seems really odd to me. I guess. I know they're not like trying to like create process. I remember hearing about like people trying to make like native Java processors in the past. Right. And it's not that. Yeah. Yeah. You know, basically these are like mini, you know, small arm chips. And basically it's the exploding availability of memory space and stuff like that. But, yeah. Okay. Well, I have no opinions then, I guess. Honestly, I'm just, I'm just confused by it. I guess that's what it really is. I'm confused other than, okay, it's simple. That's good. Now what?

**Dave Jones:** Yeah. But how much simpler is it than C? You know? I mean, is it any simpler?

**Chris Gammell:** Right. I guess there's just.

**Dave Jones:** With the easy pre-compiled libraries with the Arduino, is it that simpler? I mean, I don't know enough about Python to know, but presumably they've got to have a library to toggle the IO lines just like they do on the Arduino. So you're calling up a, you know, you've got to call up a library to toggle some IO or do something. You know? Do a PWM or.

**Chris Gammell:** I guess that's what it ultimately gets to me is like, like, I wonder is, are people doing this because of the language? Which is okay. You know, like, that's cool that, you know, they want to bring more people in. And if that is the purpose of it, then that's fine. But I guess part of me is kind of like, are they doing this because they just want to sell little widgets of hardware and then, you know, make people dependent on them? And, you know, I'm always kind of just questioning that kind of side of things. And maybe that's.

**Dave Jones:** Oh, I don't. Yeah. No. That's probably way too. I don't think of that.

**Chris Gammell:** Yep. I don't even know the word.

**Dave Jones:** Never do I, but I know what you're getting at. No, I don't think they're doing that. I don't think they're doing it for that purpose. They're just a Python fanboy and they want to run Python hardware. They think that'd be cool, you know?

**Chris Gammell:** Yeah. Well, and I guess, you know, things like Kickstarter definitely allow this kind of thing as well.

**Dave Jones:** And it has allowed it because it's met its funding goal. So, sorry, Chris. It's going to be made. Oh, yeah.

**Chris Gammell:** Yeah. I have no say in that. I have no say in anything, really. Right. Now, I think we are expected and we should say something about a different crowdfunding project that is of particular interest around here, which would be the EX1 rapid 3D printing of circuit boards. I know you saw this and I know you rolled your eyes at it, but I still fear we should take a quick mention of it. Do you know what I'm talking about?

**Dave Jones:** Let me call it. Yeah, I think I saw it last in the comments last. Let me call it up again. Let me call it up. It's a PCB rapid prototype. It's a million machine, right? No, actually, it's a printer. Oh, this is a, right. Yes, sorry. Yes, this is the silver ink. Is it silver ink? Yeah, right. Or something or some sort of conductive ink. They can print on anything.

**Chris Gammell:** Yeah, it's a silver ink. Yep. Yeah. Yep.

**Dave Jones:** I know. I don't. I know. Like, I originally thought, ooh, ooh, okay, maybe I'll get one of these. And then I thought about it for a couple of minutes and I went, no, it's pointless. It's not pointless.

**Chris Gammell:** No, it's interesting. It's a toy. It's interesting as a stepping stone.

**Dave Jones:** It's interesting if you want to do the more unique things it can do, like print onto some sort of flexible substrate or something like that. Yes, exactly. That's what it's interesting for, right? You can even, I think they did an example where you can print onto paper.

**Chris Gammell:** And fabrics as well, yeah.

**Dave Jones:** And fabrics and other things, right? Yeah. That is where it's going to be useful. As far as making your rigid printed circuit boards, no. You're just wasting your time. Forget it.

**Chris Gammell:** Right. And honestly, even some of these onto fabrics and other type of materials like that, I mean, these are, people shouldn't understand that these are higher impedance traces, right? So these are not going to be like, you know, two ounce copper. This is like, I think it was like, I'm going to talk on my ass here. I think it was a couple ohms per inch or something like that. I mean, it was pretty significant. Fairly substantial. Yeah, yeah, yeah. I mean, like, you're not going to be running any currents through here. But again, you wouldn't want to be doing that in a flexible circuit anyways or anything like that. Exactly. Yeah, this would be battery, you know, sensor type stuff.

**Dave Jones:** How do you solder onto some of these things? Like paper, right? You print your traces down onto paper. How do you solder paper?

**Chris Gammell:** Yeah. Did you watch that video from Ben Krasnow a while back?

**Dave Jones:** Oh, I haven't seen that yet. He's vacuum deposited some conductive layer onto something, hasn't he?

**Chris Gammell:** Yeah, yeah, exactly. He did the same kind of, I think that was the conductive. Well, it was definitely like a similar type of thing. It was like a printed type of, you know, he did a transfer with an SVG outline. And then I forget how he actually did, if it was like a CVD type process or what it was. But yeah, that's what he talked about is once you have to actually solder, you know, I think you had to do like a weld instead of an actual solder because the amount of heat, or maybe you had to use low temp solder or something like that. That becomes a really big issue because, you know, doing, I use Fahrenheit, but you know, like 650, 700 degrees Fahrenheit, that's a significant temperature. And it's like, if you have any kind of significant like pad size, you're going to need to add a significant amount of heat and, you know, your material, your substrate has to take it, your actual traces have to take it.

**Dave Jones:** For a few seconds, yeah. I, you know.

**Chris Gammell:** Did you do a thermal camera teardown or something like that? I saw Mike did a thermal camera.

**Dave Jones:** No, Mike, Mike did thermal camera teardown.

**Chris Gammell:** Yeah. Did you do, do you do thermal cameras at all? Do you have thermal cameras?

**Dave Jones:** I've got a thermal camera, which is currently sitting in the FedEx depot here in Sydney. Oh yeah. And it's been sitting there for the last week.

**Chris Gammell:** Oh no. So it's on the way though?

**Dave Jones:** No, it's not because it's going back. Oh. It's going back to the manufacturer because they wanted me to pay a thousand bucks import duty on it.

**Chris Gammell:** Oh my God. That's insane.

**Dave Jones:** Yeah. I always forget about that stuff. Yeah.

**Chris Gammell:** That was a big screw up. It's just interesting when you see like the thermal profile of when, you know, like, you know, like when you're actually heating up a trace, especially if, you know, it's a, you know, copper pour or something like that, you know, like it is a significant amount of heat. You will, like, I think about like doing big, big thermal or big copper pours for like around inductors on like switching circuits and stuff like that. You know, I'm heating, I'm heating up that, that big pad to try and get the inductor off. But at the same time, that heat is conducting all the way up where, everywhere the trace is connected to. And it's like, that could be a significant, uh, you know, that's, it's a, a large amount of copper outside of where I definitely want the heat to go. So it's just.

**Dave Jones:** Everything's a heating.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Yeah. You know, and for those, you need a large thermal capacity iron. Right.

**Chris Gammell:** Right. Yeah. Or a heat gun.

**Dave Jones:** And or a pre, a preheater and, and a heat gun and, or a thermal oven and stuff like that. Yeah, exactly. And it's, and they retain heat. Yeah. As well. You know, when boards with a lot of copper come out of those reflow machines, right there, they're smoking hot for 10 minutes. You know, these things are bloody, they retain a lot of heat.

**Chris Gammell:** Yeah.

**Dave Jones:** And which is what causes tombstone in and stuff like that. You know, if you've got a massive internal copper layers in your board that retain a lot of heat. And then if you've got, and if you don't design your thermal release enough to components, then when you're all, all of your bypass capacitors, for example, might tombstone on your board. Cause one end is joined to ground, which has a large thermal mass, right? Usually to a ground plane. And the other end is connected to a thinner trace, which goes off to your power, localized power for your chip. So it's not unusual to have, you know, on a very thick boards, especially, um, that actually retain the heat, you know, or your bypass capsule tombstone, because one end cooled down quicker than the other end. And whoop.

**Chris Gammell:** There it goes.

**Dave Jones:** There it goes, folks.

**Chris Gammell:** Yeah. And if people don't know what tombstoning is, when it's like a 0805 comes up on one end. It flips up. Yeah. It's on one end.

**Dave Jones:** It flips up on one end because yeah, the, yeah. It's pretty, pretty. Surface tension is. Yeah.

**Chris Gammell:** Pretty descriptive there, right? With tombstoning, but.

**Dave Jones:** Yep. Tombstone. But that, that, that is a legitimate issue.

**Chris Gammell:** Yeah.

**Dave Jones:** In the industry. And you know, if you don't know what you're doing, it can really ruin your day.

**Chris Gammell:** Definitely.

**Dave Jones:** Yeah. Thermal's a bitch.

**Chris Gammell:** Uh, so what about this? Uh, so these guys are in, how far is Brisbane from you guys? Is it pretty far? Brisbane's an hour north of here.

**Dave Jones:** Yeah. My plane.

**Chris Gammell:** You should give them a call. They're, they're, they're, they're out of Brisbane.

**Dave Jones:** Oh, right. Okay. Right. Oh yeah. I think I noticed that. That's right. It's an Australian thing.

**Chris Gammell:** I figured you were going to jump on that immediately. I thought you were going to be like.

**Dave Jones:** Oh, right. Singing a national anthem. I had forgotten that. Yeah. Yeah. Forgotten that. That's another reason why I thought, oh yeah, I'll back this at first. And then after I thought about it for a couple of minutes, no. Yeah. You know, no, it's a, yeah.

**Chris Gammell:** Well, I think it's, I mean, well, first off, it already did fund. So that's, it doesn't matter what we think. It never, it never matters what we think. Uh, but yeah.

**Dave Jones:** In fact, it's already tripled its funding with, uh, 22 days left.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, I think it'll make some cool projects, especially wearables. I mean, wearables are really, um, you know, exploding these days.

**Dave Jones:** Yeah, wearables are big these days, you know. Yeah.

**Chris Gammell:** Especially for like, uh, sensors and stuff like that. People, people love sensors. They love their blinkies, which is good. You know, both pretty decently low power. Um, so that, you know.

**Dave Jones:** And they're calling it a printer buddy. If it reaches a 700,000 goal, you get a printer buddy.

**Chris Gammell:** I think that, is that what it is?

**Dave Jones:** That, that could be trademarked too.

**Chris Gammell:** I don't know.

**Dave Jones:** Oh, dearity. Yeah.

**Chris Gammell:** Well, and so cool, cool looking project. Um, people should check that out.

**Dave Jones:** No, no, no, it's good. Yeah. But yeah, please people don't think, you know, it's some magic solution to printing your own rigid circuit boards at home. It's not. Okay. So that's what I wanted to get across.

**Chris Gammell:** Right. Yeah. Right.

**Dave Jones:** It's not even close. But for those niche applications, yes. Those, you know, flexible prototype-y things. It'd be no good for, for a production type thing, you know. Um, but for, yeah. Prototypes, one-offs, you know. Great.

**Chris Gammell:** Yeah. Yeah. Well, and you know, any kind of production type thing, you know, I think about, my general rule of when I think about if it's good for production, you have to think about, like, the batch processing type of thing. So I think I actually made this comparison, uh, either on Reddit or Twitter or something like that. But basically, this is going to be, like, a rastered type of, of process where you have to print line by line, you know, like, you're basically moving across the, the surface plane where you're processing things and you have to deposit something at each, at each pass. And that takes a really long time. It's just like 3D printing. That takes a really long time. And the fastest you're going to go is going to be the total area you have to cover times how many times, in the case of 3D printing, is how many times you have to cover that total area, uh, you know. Divided by how fast you can actually do it. Or, I don't know if that math is right. But basically, it comes down to how fast you can physically move the head across and still maintain your, uh, your accuracy of, of your, your process. Well, the thing is, the same for, like, EUV processes. So, so they were talking about doing the same kind of thing for, uh, for processing chips where you basically, because the, the line widths are getting so small, they were talking about doing rasterized layers, right? So, you basically take what is effectively, you know, a UV or extreme UV, EUV, a 13 nanometer, uh, wavelength laser or light source. And you raster it back and forth. And you turn it on when you're, when you're trying to ablate away the, the photoresist. And you turn it off when you don't. And it's this really fancy photoresist that's super hard. And basically, you're, you're blasting away different parts of, of your solder mask, or not your solder mask, your, uh, your photoresist in order to expose the bottom layers and do your processing. Does this make sense still? I'm not, I sound like I'm blabbering, but.

**Dave Jones:** Well, it does, but why are we onto chip printing?

**Chris Gammell:** Well, this isn't chip printing. This is, this is actually regular, uh, semiconductor manufacturing. So, that's, that's the thing. They were, they were proposing this for a long time. And this is why it's taken so long to do this kind of stuff, because doing that rastering back and forth, you would have to do that on a wafer basis. Now, compare that to a, a current photolithography process at a very high level.

**Dave Jones:** Oh, right. Okay. Yeah, yeah, yeah.

**Chris Gammell:** It's shining a big light, effectively, above a, uh, you know, a cutout. And then, you know, with a very fancy cutout. And then the light shines through some places and it doesn't shine through others, right?

**Dave Jones:** And you expose it once.

**Chris Gammell:** It's, it's, it's, it's effectively a batch process compared to this rasterized back and forth process. That is how manufacturing is always going to try and be. It's the same for, like, uh, machining versus stamping, right? So, if you're cutting out, you're cutting out a shape, you want to do it as a stamp because it's ka-chunk. Yeah, stamp, bang, bang, bang, bang. Right? Instead of, you know, like, so, that's always my rule of, if something's going to work for manufacturing, has to be this kind of one-time batch process. That's going to be the best case scenario. It's not always going to be the case because sometimes you have very specified inputs. But, you know, if you have to raster something back and forth and back and forth and back and forth, it's just not going to be as efficient or as low cost.

**Dave Jones:** Without an app.

**Chris Gammell:** Yeah. So, that's how I judge things for manufacturing. Right.

**Dave Jones:** Got it.

**Chris Gammell:** And you see that all the time, right? People talk about 3D printing as a plastic process. It's like, you're never going to go faster than an injection mold. It's just not possible. It's ka-chunk. You heat up plastic. You shoot it through a mold and it's done. And it's super cheap, you know?

**Dave Jones:** Exactly.

**Chris Gammell:** And it's awesome. I love watching injection molding stuff. Have you ever watched any of that stuff?

**Dave Jones:** Yeah, yeah. It's pretty awesome.

**Chris Gammell:** Oh, man. With all the, like, the slides and... Some days I think I should have been a mechanical engineer, but I never make it. All right. Boy. Yeah.

**Dave Jones:** Yeah, you know, you're a mechanical engineer or a... Or, heck, even better, you're a civil engineer. You know, you can build a skyscraper in the same time it takes us to build something, you know, that's an inch square.

**Chris Gammell:** Oh, yeah. Well, let's... Yeah, I guess there are scale differences, but... Yeah.

**Dave Jones:** It's embarrassing, isn't it? You've been working on that for 12 months? Oh, yeah.

**Chris Gammell:** I'm not... No, I don't think it's that embarrassing because... The thing is, if we were building the same structures as we were building in the 50s, right? If we were doing single transistor radios, we could build it in a similar timescale, right? I mean, like, that's effective... Like, bridges, I know that manufactured materials have gotten better for construction and everything else, but come on. Really? They're still just bridges, right? I mean, it's very important that they hold up and yes, yes, yes, but...

**Dave Jones:** Yeah, but they're big and they're impressive.

**Chris Gammell:** They are big and very impressive, yes. And I will never design one because I'm not meticulous enough.

**Dave Jones:** Why? Because it takes you an hour to do a triple five time video.

**Chris Gammell:** Yep. That's why, Dave. That is exactly why. And that, folks, is why I'll never be a civil engineer.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** There was a homebrew computer club reunion.

**Chris Gammell:** There was.

**Dave Jones:** And it was a Kickstarter, apparently, which I didn't know about. Yeah, I didn't know about that either.

**Chris Gammell:** I had heard rumbles about them doing it because I know it was at the Computer History Museum. But, yeah, if you want to see pictures of a lot of gray hairs, gray beards, rather. Yeah. It's quite the group, apparently. Seemed like... And I'm surprised they'd never gotten together before that, but I'm sure...

**Dave Jones:** Yeah, yeah. It's a bit weird. You thought they'd have a 10-year reunion or something every 10 years?

**Chris Gammell:** Yeah.

**Dave Jones:** Well, they've all gone their separate ways, you know. And it didn't last a huge amount of time. Right, right. It's iconic, but it wasn't long-running. Yeah, it's iconic, but, yeah, it's not like, you know, these guys were the best buddies for 20 years, you know.

**Chris Gammell:** I'm sure some of them were, but maybe, yeah, the group as a whole. Yeah. Yeah, so we will actually be able to ask our guest about it next week. We'll be having Jerry on next week. Again. But talking DFM, like we talked about a couple weeks ago when she was supposed to be on, we'll be talking about the design for manufacturing side of things for the Cast AR, which got funded. Congrats to them. Yes, it did. A million bucks. And I was there. I was there. I helped them push it over to a million. Not really, but I was on a Skype call with them when they crossed the finish line. So, basically, I did all the work. That's all I'm saying.

**Dave Jones:** Right. Right. Yeah. Oh, dearie.

**Chris Gammell:** And get your CVs ready because they're going to be hiring, too.

**Dave Jones:** Yep.

**Chris Gammell:** Speaking of CVs.

**Dave Jones:** How many people can you hire with a million bucks? Oh. Not many, probably.

**Chris Gammell:** That is the answer to that question. That's five people if you're not building stuff or if you're not manufacturing. That's five people for a year.

**Dave Jones:** And then there goes all your profit, you know. Yeah, but Kickstarters aren't a profit. Yeah, by the time, yeah. Yeah, because by the time, you know. When you start getting and making a company and all, you know, you get your Kickstarter money and your former company and everything else. I don't, you know, yeah. I don't think you end up with any profit left over. It's like, yeah, you end up with a company at the end of it that hopefully keeps going. But, you know. Well, yeah. We'll ask you about it next week. It's not like you made half a million bucks profit.

**Chris Gammell:** No, definitely not. I'm guessing a significant portion of that's just for tooling. And, you know. Yeah. But we'll ask you about that next week. Yep. Because, yeah, that'll be a lot of interesting stuff. But, yeah. Speaking of CVs, there's been, like, this interesting, I don't know if it's the debate, but it's just a conversation kind of going back and forth on the web about GitHub as, like, the defining CV for, like, software people. Right.

**Dave Jones:** Right. Okay.

**Chris Gammell:** You know, basically employers are now going to software people and they're saying, well, you need to have a public GitHub profile. You need to contribute to X number of projects and stuff like that.

**Dave Jones:** Right. Is it so that they can see their code? I see what their code's like? Or is it just a wank thing? Oh, you can't be any good if you haven't contributed to GitHub.

**Chris Gammell:** Right. I think it's somewhere in between the two, but I think it's the latter of those, the you can't be any good if you don't, that a lot of people are taking umbrage with.

**Dave Jones:** Like, you can't be any good if you aren't on LinkedIn, right?

**Chris Gammell:** Right. Exactly.

**Dave Jones:** You aren't on LinkedIn? What? You don't know anyone. You're a fraud. I know, right. Bugger off.

**Chris Gammell:** You spend all your time networking at lunch, talking to people? You are a fraud. Yeah. Oh, boy. And yeah, that's basically the argument that's going down is like, well, there's twofold. One is that. It's like, of course you can have other things, you know, going on. You know, you might have secret projects that you can't necessarily talk about unless you're in a private meeting. You can't, you know, you might be working on just private projects for personal reasons. You know, like there's so many options out there that I think the main thing is that people are, they're saying that if you make a requirement, if you make anything like that a requirement, right? Like just saying, just like saying you need to have a PhD in order to get this job. It's like, well, you're excluding some people that are going to be perfect for that job either way. And personally, I say, if people are making that requirement, that's a lazy hiring person and you don't want to work for them anyways. It is. You should be trusting your hiring managers, really.

**Dave Jones:** It's just stupid, right? You're potentially giving up on good employees. I would never make that a requirement to have, you know, yeah, if you've got public stuff out there, cool. Okay. Yeah. But I would not toss somebody's resume in the bin just because they didn't have that stuff on there. Right. But for me, the final answer to that is get them in for an interview. If they sound okay, get them in and then get them to show you stuff in private, right? If they can't make it public or whatever.

**Chris Gammell:** Exactly. Well, that's the thing. That's fine. There's all these hiring groups out there that want to turn money around, right? Where they have these huge hiring bonuses. Oh, yeah. They want to be able to search people online and then go and seek them out programmatically. And that's the thing. That's what it comes down to is that it's a money thing, I think. You're trying to lower your cost for hiring. You're trying to –

**Dave Jones:** Right.

**Chris Gammell:** Hiring companies are trying to increase their turnover so they make more money. And you just can't standardize this stuff from my standpoint. You need to – you can definitely take it as a part of the whole, right? You can say, oh, you did this, this, and this. And then like you said, you bring people in and you actually talk to them. You make sure they're not full of crap, right? They're not like – Yeah, yeah, exactly. They're just contributing in order to contribute. But it's just part of the whole. It's never the whole thing by itself.

**Dave Jones:** Yep.

**Chris Gammell:** But the other argument there is that people that are able to contribute to open source projects on GitHub and stuff like that are often more privileged. And you might be excluding people because of that. Now, I don't know the demographics of that side of things, but it's an interesting point that like you think about who has – if you're trying to bring people up through the ranks, right? It's like it's going to be the top performers who are participating anyways because they're going to have more freedom in their jobs. And it's like you're just going to be cherry picking from the same talent. And so I think that's the most valid argument there. But I think there also are some arguments about women in programming, minorities in programming as well that we've talked about on the show before from a hardware perspective of trying to get people involved and stuff like that. So there is an exclusion side of the whole argument as well. But I don't know it well enough to say anything more than that.

**Dave Jones:** All I can say is that it's that bullshit.

**Chris Gammell:** Yeah. Well, I mean, I would never say like you have to have an open source hardware project to work here. That would be ridiculous, right?

**Dave Jones:** Exactly.

**Chris Gammell:** I would put the same –

**Dave Jones:** It's crazy. It helps. Everything helps. But it's not going to – it shouldn't exclude you from the job. That's just ridiculous. Yeah.

**Chris Gammell:** I think it benefits the hiring people more than the hirees, right? Because it just – they want to be able to exclude people faster. And that's – Exactly. That's where it's stupid. So –

**Dave Jones:** Totally agree. Sorry. I linked in an absolute work of art.

**Chris Gammell:** Oh, yeah. Yeah, you did. This thing was beautiful. I was like, you're on LinkedIn? What? You're looking at art on LinkedIn?

**Dave Jones:** This thing brings a tear to the eye, folks. We will link it in to the show notes. And trust us, you want to download and print this thing.

**Chris Gammell:** How did you – so first off, say what it is, but then how did you find it?

**Dave Jones:** It is a chart. It is a chart of the electromagnetic spectrum, electromagnetic radiations. And it has examples of all, you know, different type of stuff that generates different spectrums and everything. And it's ancient. It comes from like the 1940s or something. And it's a huge poster size thing. You can download it in like 10,000 pixel by 7,000 pixel size. And it's just gorgeous. Awesome. Right? And it's all hand-drawn, colorful, and just got that old school 1940s look to it. So it's certainly not modern. All the examples are old, right? But it's just gorgeous. And Malcolm Fade, who I've had on the blog before, he found it somehow. And he put me onto it. Wow. Yeah. Thank you very much, Mal, if he's listening. I don't take credit for the fight. And it's just – yeah, it's fantastic. Yeah. So somebody scanned this in. Like this is like an original poster. Well, I don't know how they scanned it. It must be public domain, though, right?

**Chris Gammell:** I mean, like –

**Dave Jones:** Well, it'd be – well, it's from the 1940s, right? There's no longer copyright on it, right? I don't know those rules.

**Chris Gammell:** I know – Yeah, I don't know those rules either. 17 meters or something. No, that's patents, right?

**Dave Jones:** All I know is that the guy who drew it is probably dead. That's all I know.

**Chris Gammell:** E. Borzone. That's who drew it. Mm-hmm. We will honor him here.

**Dave Jones:** Absolutely. Yes. Even though he's probably dead. Oh, probably. Well, yeah. Statistically. You know. Yeah. I think so. Yeah. Yep. Yeah, because he would have been at least in his 20s when he drew this, right? Yeah, right. Even if he was 10 when he drew this. Yeah. At best, right? Yeah. Exactly. Yeah. Oh, it's just gorgeous. I'm amazed.

**Chris Gammell:** Like, you know, I think about how hard it was to kind of conceptualize RF type of stuff and really just spectrum type stuff in general from, you know, really – as I've said before, the time when it really, really, really kicks in is when you get a DVB TV, right? One of those little USB dongles. Yeah, right. And that's how you can – you know, when you see like a, you know, a spectrum changing over time, whatever – I figure that's called a histogram or whatever that is where it's passing by the screen. That's when you really – that's when I really, really, really, really got it, even though I had gotten a little bit before. But, you know, it's so hard to grasp. And then I think about doing that back in the 40s when, you know, you didn't have – you know, the best you had was someone drawing something like this or, you know, just drawing it over and over on a chalkboard. Yeah, it's amazing.

**Dave Jones:** And I want to know why he did it, why he drew this, who he drew it for. Was it the company he worked for? Did they, you know, give him the, you know, task him to do this or what?

**Chris Gammell:** I'm sure – yeah, I mean – It's just incredible. I'm sure that that was the case. I mean, this is – this must have taken a really long time. I mean, even typesetting back then was tough, right? I mean, like, thinking about drawing all this stuff and, you know, this is all hand-drawn. So –

**Dave Jones:** I'm surprised it has survived this intact. You know, somebody obviously had the original of it and scanned it in using some sort of professional, you know, flatbed scanner because obviously this was, like, poster size, right? And you wouldn't be able to take just an image of it with your digital camera because the distortion effects of the lens would be too large even if you had a huge –

**Chris Gammell:** You could stitch it together maybe, but –

**Dave Jones:** Oh, maybe, but no, there doesn't look to be any evidence of that. I think it's being professionally scanned by some big raster scanner, you know, roll scanner system or something.

**Chris Gammell:** Just now, it just finished loading for me. That's how big it was. Right.

**Dave Jones:** Yeah, it's 144 meg or something.

**Chris Gammell:** Wow. Are you going to get it printed, do you think?

**Dave Jones:** I was going to get it printed in a big poster, yeah, and laminated and put it up.

**Chris Gammell:** See, now you'll have to share when you get that done. See, that's the thing. Like, I don't know how to get, like, something this big printed. So if you find something good for that –

**Dave Jones:** Google, dude. There's 10 million printing houses that – online printing houses. You just upload your file on their website and bang, it comes to you two days later and it costs you 50 bucks.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** All right. Well.

**Dave Jones:** I think here in Australia, I did some quick pricing of an A0 size poster. Mm-hmm. It's like, you know, 70 bucks or something. Okay, that's not too bad.

**Chris Gammell:** Actually, I just found in the upper right corner, it's the W.M. Welch Scientific Company. Ah, there you go. Right. Edited by Arthur H. Compton. Wow. Right. That is insane. 1944.

**Dave Jones:** Right.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Is there any Google on him?

**Chris Gammell:** Oh, I don't know. W –

**Dave Jones:** Does he have any Google food? Can we type him in?

**Chris Gammell:** W.M. Welch. Oh, are they still around? That would be even better. Right. No, they're not around anymore. Oh, Sergeant Welch. Is that – oh, maybe they are. I see something here. They have a bunch of, like – they have a X-Tech on their site, so – Yeah, I don't know. I'll have to look into that more. But, yeah, that is a sweet, sweet poster. I still want to get – that's the thing. So, I was looking at posters because I actually never got any printed for that Weidlar poster that we have on our site. We never got that done at all, so I don't know about – like, how do I actually get that done? So, I've never found anything that works.

**Dave Jones:** Dude, type in –

**Chris Gammell:** I will. I'm just saying.

**Dave Jones:** A3 or A2 poster printing. I don't know what that means.

**Chris Gammell:** Into Google. I don't know what – I don't do the A stuff.

**Dave Jones:** There's – oh, well, what sizes do you bloody yanks at? I mean, these are international standard sizes. I don't know.

**Chris Gammell:** I don't know, yeah.

**Dave Jones:** Well, yeah, printing – but just type in poster printing. Okay. Into Google. And you'll find poster printing Cleveland. And you'll probably find 10 of them.

**Chris Gammell:** What is this Google you speak of?

**Dave Jones:** Oh, goodness sake. Yeah.

**Chris Gammell:** You're a Luddite. I kind of am sometimes. Analog, man. So, I pay someone and they come to my house and they redraw this from site. Is that how it works?

**Dave Jones:** Okay, yeah, yeah. That's how it works, yeah. Yeah.

**Chris Gammell:** So, who did you say put this onto you? Put you onto this, rather? Was it Marcus you said?

**Dave Jones:** Mal.

**Chris Gammell:** Mal.

**Dave Jones:** Mal. Fade. Yeah. Was he the one with – Malcolm Fade.

**Chris Gammell:** Ninja Blocks. Who do you know from Ninja Blocks?

**Dave Jones:** No, no. No, no. Malcolm Fade is the Segway guy. He's made his own Segway. Oh, right, right, right. He's the one who does the electric cars. He builds his own electric cars. That's right. He's the one who had the Sinclair C5s.

**Chris Gammell:** That's right. Those crazy little shitty vehicles. Who was it that did the Ninja Blocks? You knew someone that did that, right? That's an Australian thing.

**Dave Jones:** Yes, that's Marcus.

**Chris Gammell:** Marcus. That's right. Yeah. Yes. So, they're putting on –

**Dave Jones:** He sold that. He sold that to his partner or something.

**Chris Gammell:** They have a new thing out, the group that does it.

**Dave Jones:** Yeah, they've got a new Kickstarter-y thing, don't they? A new fancy-looking –

**Chris Gammell:** It is fancy-looking. Whiz-bang. Yeah, it's like a little – it's like a home networking thing for all Internet of Things devices. Right. Which, you know, wanky, right? But the thing that's interesting about this is like, you know, I expect this to be – you know, this is a Kickstarter project, that kind of thing. They're open-sourcing everything, at least as far as I'm reading it. So, they're open-sourcing all the software, all the hardware. And I haven't seen that on any other type of Internet of Things, you know, because it's kind of a land grab right now. You know, you think about Wemo and all those others. Right, yeah, yeah. They all want to talk to each other. There's all these different RF standards. You know, there's Ant. There's Bluetooth. Oh, it's millions of them. Yeah, there's all these different ways to talk, but there's no standardization. And so, that's kind of exciting from having a home networking type of thing. You still need all the radios in there, but if you have some kind of open interface where people can write plug-ins and all that other kind of stuff, that's actually pretty exciting. Yeah. And it's also a beautiful mechanical design as well. I mean, so it's cool. Ninja Blocks could be very, very interesting. I never tried out the other thing, but I know it's all still built on BeagleBone. No, I've never used it.

**Dave Jones:** Yeah, they did a Kickstarter back then, and it was – and they 3D printed all their cases. That's right, yeah. And they said, yeah, I think he commented once that, yeah, that was a big mistake. They had to have, you know, a room full of 3D printers just running 24-7. Injection molding, folks. In their house. It works. Yeah, exactly. Oh, boy.

**Chris Gammell:** Yeah, so that's a cool-looking project, too. And, you know, just open projects like that are really interesting from seeing how – I feel like there's a lot of fatigue. Not a lot of fatigue because I don't know that closely, but there's just so many projects you can contribute to these days. I can't even imagine how software people –

**Dave Jones:** They're endless, aren't they?

**Chris Gammell:** Yeah. Yeah. It's – well, and, you know, that's another point of that GitHub being a CV article is interesting, too, because they're saying, you know, if you're recruiting people based on how many projects they start, then it basically disincentivizes people from joining other projects.

**Dave Jones:** Right, okay.

**Chris Gammell:** You know, it is tough, though. I can only imagine there's – you know, there's so many projects out there to contribute to that – I mean, and hardware people keep making new hardware, right? I mean, us a-holes, we keep doing it, so.

**Dave Jones:** Has anyone got any stats on how many new hardware crowdfunded projects there are every week? Is anyone – is anyone keeping tabs on this? Has anyone got any data?

**Chris Gammell:** You know, I saw Zach from Upverter posted something about that today. They're really good. Him and Enzo have been posting a lot of, like, infographics. They're really into the infographics, which are – They're right. Whatever. Grown. But there is just some interesting information in there. You know, they are collecting a lot of that information. It's usually in their blog. I don't know if we'll be able to find it by now. But, yeah, they're posting about how many new projects there are and everything like that.

**Dave Jones:** Oh, okay.

**Chris Gammell:** And there are a significant amount, basically. That is the gist of it all. I think they compared it from one year to the next, and I'm never going to be able to find this now. So, I'll try and link it in, though.

**Speaker ?:** Of course not.

**Chris Gammell:** They – big, big poster-size infographic.

**Dave Jones:** Fuck, I hate the infographics.

**Chris Gammell:** Yeah. They're kind of – did you see that XKCD about that? So, five years ago. Yeah. Oh, yeah, yeah. That was funny. Yeah.

**Dave Jones:** Oh, boy. Yeah. No.

**Chris Gammell:** What else we got this week? I think we're – well, we are running out of time, but I think – More Kickstarter projects? Yeah, more Kickstarter.

**Dave Jones:** I don't know if our listeners feel with bloody Kickstarter projects.

**Chris Gammell:** Yeah, I put a lot on this week. There is a new – so, not necessarily Chip of the Week, but, you know, Chip of the whatever. We always end up picking LT because they always end up putting out interesting parts.

**Dave Jones:** Yeah, they do.

**Chris Gammell:** You know, this is an interesting segment because I know TI has parts like this, too, with the wireless power transfer stuff. You know, like for –

**Dave Jones:** Every man and his dog is doing that. Oh, really? How many others?

**Chris Gammell:** I haven't seen many others. It seems like it. But, you know, like, basically, yeah, this is an up-and-coming market. I personally don't understand it, but I guess there's a reason to do this. I don't understand the efficiency. Like, you know, with all the focus on green, I don't understand, like, is it that hard to plug in a cable? But then again, you know, you could say the same thing when people are like, oh, well, is it so hard to plug your laptop into a LAN connection? You know, why are we using Wi-Fi? So, I'm sure that's just me being a fuddy-duddy. But, you know, there are a lot of new parts like this, and especially ones that are integrated like this is. You know, like, this is pretty simplified. The TI part was pretty simplified as well. And, you know, it's basically – What's the part? Oh, sorry. The LTC4120. 4120. And there's a couple different, like, modes, and they're trying to – you know, another – in terms of land grab, they're all trying to, like, say, hey, we're the standard. No, we're the standard. You know, it's like all the same thing, but it's doing handshakes and trying to make chips talk to one another.

**Dave Jones:** Oh, hang on. Wank, wank phrase of the week. What? Here we go. The first feature of this chip is dynamic harmonization control. Oh, who thought that one up?

**Chris Gammell:** Marketer.

**Dave Jones:** Oh, boy. That's just sad. Yeah. Now, the interesting thing about – What the hell does that mean?

**Chris Gammell:** Probably, like, syncing up your harmonization.

**Speaker ?:** I don't know.

**Dave Jones:** It's bullshit.

**Chris Gammell:** It's probably like trying to align your pulses on, like, you know, a resonant type of – I still don't know. It's basically an air core transformer. That's effectively what this is, right? And you lose –

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** You lose some of the efficiency because of that, because it's –

**Dave Jones:** Air cores – yeah, they're just inefficient.

**Chris Gammell:** Yeah.

**Dave Jones:** All wireless power transfers are inefficient because they're not coupled together. As a regular transformer would be nicely, tightly coupled. Exactly. You get that huge efficiency, you know?

**Chris Gammell:** Exactly. Yeah, and so basically what it comes down to is you're not going to be using this for a huge amount of power, but it's – I guess it's for convenience sake. I mean, there might be other interesting uses for it. I mean, you know, you think about coupling, you know, for, like, isolation. You could do – if you didn't mind about the power as much, you could do really, really high voltage isolation because now you can move things apart without actually needing to have a physical transformer where you're doing – you know, where you're transferring power over that. There's actually – there's an analog devices part that does that. But it's like a digital isolator and then the power is built into it and there's more people doing that as well. Well, it's the same thing, though. It's just two coils that are separated by, you know, a substrate. Usually sometimes it's air. Sometimes it's, you know, like a silicon dioxide type of thing. But, yeah, it's the same kind of thing. You're still coupling magnetic energy over some space. It's just a matter of what is the dielectric constant of – no, sorry, not the dielectric constant. What is the coupling between those two coils? What is it? It's the – it's not dielectric constant. There's whatever the core material transfer.

**Dave Jones:** Oh, the permeability of the core material.

**Chris Gammell:** Yeah, there you go. Yeah, basically how well you can transfer magnetic energy. Yeah.

**Dave Jones:** Well, there's a lot of shit that goes into transformer design and getting the ultimate efficiency out of it. It's not just, you know –

**Chris Gammell:** Yes, but –

**Dave Jones:** It's core saturation.

**Chris Gammell:** Right, right, right. But if – There's a lot. Yeah, if you have a ferrite core, it's better than air, right? It's – Right. Yeah, some way of – And basically, though, from – you know, if you're actually trying to isolate voltages, if you have stuff in between, it's not as good as if you have air in between. So it's kind of balancing those two. And so I guess that's another feature there. But I really think that all these are – the wireless power stuff is because people are lazy. They want to throw their phone onto, like, a pad and they want it to just –

**Dave Jones:** Yeah, a charging pad. Yeah. They haven't really taken off yet. I mean, my phone's got a wireless charger in it, apparently, my Google phone. Oh, yeah. But, you know, people apparently – you know, they've had them for quite some time, but people don't seem to – you know, these things really haven't seemed to have taken off. I don't know why. Well, yeah. So –

**Chris Gammell:** I guess there's reasons to do it for, like, you know, you can plug in more than one thing at once. But it's often like, well, what does it really do for me? Unless it's cheaper. You know, like, you think about how cheap a USB micro cable is. It's like, okay, that's really cheap. Beat that. Yeah. Yeah, it's cheap. Oh, I have to buy an $80 charge pad? Okay, well.

**Dave Jones:** Yeah, exactly. And you can move it around even if you've got a charge pad. Like, you've got to walk to the specific location in your room where the charge pad is. Well, what's the difference between walking across the room, putting on a charge pad, or walking across the room and then plugging in the micro USB that's there?

**Chris Gammell:** Yeah.

**Dave Jones:** You know, you're saving, like, you know, one second of your life. You know, it's not a huge –

**Chris Gammell:** Yeah. Once you get over the wow factor of, okay, it's charging over air, then that is interesting. That is very cool. But, yeah, past that, it's – So maybe there are other applications.

**Dave Jones:** You know, I take my phone, for example, right? Sometimes I want to charge it at my desk here. Other times I want to charge it on my bench. Other times I want to charge it in my car when I'm going somewhere. Mm-hmm. You know?

**Chris Gammell:** So you don't want to buy three $80 chargers, charging pads?

**Dave Jones:** Yeah, charging pads. And it's just –

**Chris Gammell:** Well, and that's the thing. And once it – if it ever does get standardized, right, if one standard does win and, you know, then people can – they sort of start getting commoditized. This is just the usual pathway of how this stuff goes. It'll get commoditized. They'll – you know, a car manufacturer will start just integrating it into the armrest. And then, okay. Right. Now it's fine. Right?

**Dave Jones:** Right. Well, there are standards for this stuff. There are standards for wireless power.

**Chris Gammell:** Yeah, I don't know how to say it. Like the Kai or – it's Qi.

**Dave Jones:** Yeah, Kai or something. It's something like that, yeah. Yeah.

**Chris Gammell:** And there's like – I think there's two big ones. I think so. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** But, yeah, you know, there's all these, you know, big – oh, yeah, working with the standards is Asus, HTC, Huawei, LG. You know, like all of the big companies are trying to work together.

**Chris Gammell:** But then there's always someone else and whatever. Exactly.

**Dave Jones:** Well, does this – linear technology part, I don't see any mention of any standard.

**Chris Gammell:** No, it actually says it doesn't further down. So it doesn't do that standard.

**Dave Jones:** Then what's the point?

**Chris Gammell:** Well, if you have sensors – If you want some custom thing. If you wanted – so say you don't want to use the – wait, it's going to tell me how to say it on the wiki page. Qi. Oh, jeez. I wasn't even close. Qi. Qi is pronounced Qi. I'm guessing that's from like Mandarin or something. Anywho. Right. Yeah. I mean, you could, you know, if you wanted to do like a sensor maybe. But any kind of significant distance away, you're not going to be able to do that. Maybe if you wanted to try and transfer power through like a sealed box, right? To say you had like a – you know, you wanted to have like a really watertight thing without a battery in it or –

**Dave Jones:** Well, Qi would still work, right? But I think there's more to it than the Qi. I did have a quick look at it once. And there's all sorts of, you know, this backscatter like a protocol type thing happening. So it's more complex, right? Whereas this thing is just dumber. So I think it just gets a signal from anywhere, you know, and then just, you know, converts it and charges your battery. I think that's – yeah. That's the goal of this one is just to pick up energy from any sort of source.

**Speaker ?:** Oh, oh, oh.

**Chris Gammell:** Yeah, I guess LT does into that – I think that's the – Well, maybe. But this is – I mean, if you're just trying to grab like ambient power, that's a totally different beast, right? Like you see all these – I see all these news stories about like why people – oh, we're harvesting RF Wi-Fi signals. It's like, okay. My friends post this. I've done a video on that. Let's not go. Yeah, yeah. It's new.

**Dave Jones:** It's a joke. Anyway, eh, it's another wireless power machine.

**Chris Gammell:** Well, I think it's interesting that it's a single chip though. That's usually what interests me when they integrate all this stuff into small packages. That's always interesting to me and –

**Dave Jones:** To me, this is just another energy harvester chip.

**Chris Gammell:** So you're saying it doesn't get chip of the week, Dave?

**Dave Jones:** No. Sorry.

**Chris Gammell:** All right. What was your chip of the week? Was that – you wanted to bring up yours now? Gotcha, bitch. Bastard.

**Dave Jones:** The triple five. That's my chip of the week.

**Chris Gammell:** Yeah, that's your chip of the week, huh? Yeah, that's –

**Dave Jones:** Because my 555th video is coming up soon.

**Chris Gammell:** Oh, it is, yeah? You're going to do anything special?

**Dave Jones:** And people have been – well, I have to. People have been demanding it.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, I was going to – like, I floated it out there, right? And I thought, you know, I'm a lazy ass, right? I didn't want to – No. I suck at coming up with ideas. No. Right here. No. You wouldn't think so, right? And, you know, I suck at coming up with ideas, you know, of something cool to do. Speaking of which, remind me to tell you about the Maker Faire after this. Even though we're way over time. And, yeah, right, so I floated it out there. I thought, oh, just have a party at the lab, right? That'll be my 555th video. I'll just stream it live and, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** People rock up. No one seems interested. No? Oh. All right.

**Chris Gammell:** The social side of things, huh? Yeah. No. Yeah. I forgot to mention last week, we're having another meetup this week in Cleveland. But I think all of the listeners in Cleveland probably are already showing up, too. Right. So there's not many people in Cleveland. Well, yeah.

**Dave Jones:** And so, yeah. So I'm going to have to come up with an idea for the video. So if you have any ideas of what I can do.

**Chris Gammell:** Oh, I'll come up with something.

**Dave Jones:** And, all right. Like, I was, you know, going to do something big ass. Like, you know, I was going to do the world's biggest 555 timer project with 555 555 timers. But, you know, shit, I've only got, like, a week. Yeah, right. You know? Yeah, sorry. So it's not like I can spin custom boards.

**Chris Gammell:** Alan already moved to the States, buddy. His, what was that, 100 and some 555 timers when he did his 555 contest?

**Dave Jones:** Was it that many?

**Chris Gammell:** It was, I think it was over 100, yeah.

**Dave Jones:** Right. It was a significant number.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Hmm.

**Chris Gammell:** So are you going to tell me after the show or are you going to tell me after, like, now?

**Dave Jones:** No. Well, I don't have any idea.

**Chris Gammell:** No, I mean the Maker Faire thing.

**Dave Jones:** Oh, the Maker Faire. Yeah, no, that just fell on its ass. I was going to. Oh, it's coming up, isn't it? I had a project in mind. Yeah, it's coming up this weekend. So, yes, if you want to meet me, and you're in Sydney, of course, I'll be at the Maker Faire this weekend, this Sunday, I think it is.

**Chris Gammell:** Yeah, you totally flopped on that.

**Dave Jones:** Don't quote me on that. Anyway, it's Saturday. Yeah, I totally flopped. I had this project in mind, and I started building it, but then I realized how much work was involved. And then, you know, I thought, oh, yeah, like, you know. And then things just weren't working. You know, it wasn't going as well as I thought. And because it's a complex mechanical build, you know. Yeah. And I wanted it to look good. Like, I just didn't want it to be half-assed, right? If I was going to do it, I was going to do it, you know, properly. Right. And, yeah, and it just, no, it just, there was a shitload of work in it, and it just wasn't working out, and I ran out of time. And, well, yeah, that's the end of that. So, I've got no project to show up Maker Faire.

**Chris Gammell:** Well, I guess you'll have to be the science project, huh?

**Dave Jones:** Yeah. Well, no, I figure, like, I don't want to spend all my time just showing off my project anyway. I'd rather spend my time shooting video of the place. Yeah, talking to people. That's probably, yeah. Yeah, that's probably better of my time, you know.

**Chris Gammell:** Well, it's whatever helps you sleep at night, man. Whatever helps you sleep at night.

**Dave Jones:** Anyway, so I'm pretty disappointed that I didn't get that finished.

**Chris Gammell:** You know, you can just save it for later. Yep, exactly. It's always tomorrow.

**Dave Jones:** Not the end of the world.

**Chris Gammell:** Yeah. Until it is.

**Dave Jones:** Right.

**Chris Gammell:** All right, man. Well, hey, have a good time at Maker Faire. I'll look forward to hearing about that. Cool. And if people haven't asked questions of Jerry on her various podcasts, podcasts and everything else, we will be talking the actual implementation and her trip to China, her upcoming trip to China. So that'll be interesting talking about that kind of stuff. So we'll put up a post for asking for questions.

**Dave Jones:** Awesome.

**Chris Gammell:** All right, man.

**Dave Jones:** All right. See you next week. Bye. Bye.

**Dave Jones:** Bye.

**Speaker ?:** Bye. Bye. Bye.

**Chris Gammell:** Don't forget to subscribe.
