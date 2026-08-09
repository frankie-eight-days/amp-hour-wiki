---
title: EEVblog, National Semiconductor, Texas Instruments - The Chinese Clairvoyancy
url: https://theamphour.com/the-chinese-clairvoyancy/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV Blog. And I'm Chris Gammell from Chris Gammell's Analog Life.

**Chris Gammell:** Hey, Chris. What's happening? Hey, Dave. Not much. Some big news on Twitter. We've seen a lot of stuff going on. Big news? We have. Tell us about it. Yeah. Let's get straight to the biggest thing. You and I were talking about this on Twitter. There is a really big piece of information here. There is. It's a big deal. I got a new recording rig. It's in the mail. All right. Fantastic. It is in the mail. So we will have multi-track recording capability soon. I cannot wait. Ah, fantastic.

**Dave Jones:** And, of course, the real news. Can we have a drumroll, please? Oh, yeah. Hold on one second.

**Chris Gammell:** All right. Woo-hoo!

**Dave Jones:** And that was live, folks. Oh, that's right. Yeah. No recording there. Anyway, the real big news is that I am now a full-time video blogger. Yay! Almost two years. Almost two years to the day. Two years. That's all it took. Yeah. And I didn't even realize that. I know. That it was two years. Somebody on the forum just went, it's two years. Happy birthday. And I went, oh, shit. It is. Yeah.

**Chris Gammell:** Now, is that happy anniversary or happy birthday EEV blog? Or how does that work?

**Dave Jones:** I don't know. That's what they put in the forum post. I think it was happy birthday EEV blog. So, yeah. All right. Yeah. 4th of April was my... Yeah.

**Chris Gammell:** That's great. That was the first video, huh?

**Speaker ?:** What's today?

**Dave Jones:** The 6th? Yeah. That was the first video.

**Chris Gammell:** It's 5th here, but yeah.

**Dave Jones:** Yeah. Right. Yeah. Yes. Oh, no. It's the 6th here now. So, there you go. And, yes. Yes. I am now a full-time video blogger.

**Chris Gammell:** So, why are you a full-time video blogger now, Dave?

**Dave Jones:** Why am I a full-time video blogger? Because this is the other big news, which... We will most likely have to talk about at length. Yes. Because as most people would have known or realized... Maybe not, though. Maybe not. There are some people. I used to work for... Used to. Past tense. Past tense. Work for Altium, the EDA. I'm shocked. I know. How would I have ever found that out before, Dave? Nobody. Super top secret. And that was the reason why I haven't been able to talk about CAD software. I haven't been able to talk about Eagle much. I've talked about it a bit on this radio show, but not doing a review of it or doing tutorials or things like that. And I haven't been able to talk about FPGA stuff much. That's right.

**Chris Gammell:** We can start talking about that now.

**Dave Jones:** We can, because I worked in the hardware department designing the FPGA boards, the FPGA development boards. So, yeah, that's why I couldn't really go and do a review of some competitor's FPGA board. Yep. But now I'm certainly free to do that.

**Chris Gammell:** Bring it on. Yes, exactly. It's such a weird situation now. I mean, it's like the whole, you know, there's no restrictions for you now.

**Dave Jones:** No, no, it's right. Yes, I'm a free agent. And I can say anything I like now, which is what I like to do.

**Chris Gammell:** Yeah, you're good at that part.

**Dave Jones:** I am.

**Chris Gammell:** Just trying to stop you, right? Exactly. Not even the lawyers can stop me. Oh, yeah. So, let's hear the story. How did this all go down? What do you know? And where are we going from here?

**Dave Jones:** Okay, well, this wasn't a conscious decision on my part. You know, I've been talking about going eventually, hopefully going full-time one day. But that was just like a, just based on the growth projections and how much I was earning in ad revenue and that sort of stuff. And it just looked like eventually one day, you know, there was just continuous growth. And there still is. And it just looked like eventually one day, maybe a year or two down the track, I might have been able to make a conscious decision to leave full-time work and do it. But no, Altium, I have been retrenched from Altium. A lot of people don't know what that term means, apparently.

**Chris Gammell:** I do not. I do not know what that means. Well, I didn't until before the show.

**Dave Jones:** Right. Okay. Well, retrench means laid off, I guess. In U.S. speak, Altium have retrenched a lot of their staff, especially here in Sydney, which we'll get on and talk about. Yes. Because it's a very interesting topic, actually. Yeah. Just the, yeah, anyway, we'll talk about that. And so, yeah, it wasn't a conscious decision on my part at all. It went down very quick. Yeah. And, yeah, I was made redundant yesterday. Today is my first day of freedom. So, and Chris got me out of the bloody, woke me up at seven, I had to start at 7.30 this morning. Thanks for that. Yep. You bastard.

**Chris Gammell:** Hey, man, freedom ain't free.

**Dave Jones:** Right. Okay. You got to, as they say in the U.S. all the time, right? You got to fight for your, got to work for your freedom.

**Chris Gammell:** Yeah, sure. Right. Oh, goodness. Man, it's our first day of freedom. That's pretty crazy.

**Dave Jones:** Yeah.

**Chris Gammell:** I think the thing is, a lot of people would come up to you and be like, wow, that's great. But it's got to be kind of like a, you know, not an empty feeling, but like it's got to be kind of weird, right?

**Dave Jones:** It's not weird at this stage. I guess it might be weird when I go, oh, I can do anything I like today. I don't have to go to work. So, maybe ask me that next week.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. Because at the moment, it's like, well, you know, I don't know. It doesn't feel any different. Yeah. And it's nothing new for me, though. I mean, I've taken time off work before to work on my own business and do things and just, well, not work at all. Just take some time off. Oh, yeah? So, yeah.

**Chris Gammell:** So, how long were those stretches?

**Dave Jones:** Ah, some of them were like six months. That's pretty nice. Yeah. Yeah. Because as I've explained, I've always had screw you money, you know, up my sleeve. Which is important. Yeah. Which means I can do stuff like that. Mm-hmm. Which means that's why I'm not panicking going out and getting a job straight. Oh, my God. I lost my job. I'm going to cry my eyes out and, you know, and I have to go out and take any shit job that comes along. Well, no. So, yeah. Hopefully.

**Chris Gammell:** You take the shit job that you choose when you choose it, right? Exactly.

**Dave Jones:** So, yeah. Hopefully, I can take several or many months off and hopefully put some more time into the blog and other avenues and see how it goes. So, that's the plan. Not that I really have a plan.

**Chris Gammell:** So, you know, do you have like a list of videos that have been piling up for you? Yeah.

**Dave Jones:** I have a kind of sort of a list, but now I think it's different because that list was based on sort of, well, A, that I couldn't talk about, you know, Eagle and Design Spark and all the other, you know, PCB stuff and FPGA stuff. So, that's changed a bit. And they were based on the fact that I only had X amount of time available outside of my nine-to-five job to work on stuff. Now, I can devote more time to it. So, I can maybe do some more in-depth blogs. I don't know. Yeah.

**Chris Gammell:** Uh-oh. Long pause coming from Dave. Right.

**Dave Jones:** If yet. Why stop at 60 minutes? Exactly. Yes, there is no time limit on YouTube. So, for partners anyway. Yeah, there's no time limit. There's only a file size limit. Oh, okay.

**Chris Gammell:** Yeah. Well, there you go. If you compress the crap out of it, it's just you, blocky Dave, talking for three hours at a time.

**Dave Jones:** Exactly. Oh, three hours is nothing. Apparently, you can do, yeah, HD video for like 10 hours or something that fits within. Oh, wow.

**Chris Gammell:** Yep. As long as it's not copyrighted, right?

**Dave Jones:** Yeah, exactly. Yeah, wow. I can rant on as much as I like.

**Chris Gammell:** Wow. So, what is the file size limit then?

**Dave Jones:** It used to be like 10 gig, 15 gig, something like that. But I think it's been upped. I think it's changed. I think there is no file size limit now, actually. Yeah. They may have changed. Anyway, I've never tried. Yeah. You basically get to the limitations of the system and it'll just crash. I've heard of guys trying to upload these other YouTube partners, trying to upload these massive long videos just to see if they can. Yeah. You know? And the system just falls over. You know? So, yeah. You know, your internet connect or the server just dies and it can't process that video. It's just, I don't know. Yeah. Four hours later. Anyway, no, I have no intention of doing that. It means I can maybe polish them a bit better, perhaps, you know. Actually.

**Chris Gammell:** Next career as a video editor.

**Dave Jones:** Right. Yeah. Pretty much. That's great.

**Chris Gammell:** Man, I think it's, I mean, like, you know, it's kind of crappy that, you know, the job ended, but it's exciting. Yeah, well. You know, there's some excitement to it.

**Dave Jones:** Yeah, exactly. Every step is a step forward, you know? It's never a step backwards. It's never, you know, a loss or whatever. It's always a positive thing. So, change is as good as a holiday.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm. Well, I am on holidays now, which is great.

**Chris Gammell:** Yeah, you should go do a celebratory canyoning and spike some DMMs and...

**Dave Jones:** Yeah, absolutely. Absolutely. I don't know what I'll do with myself now. Honestly, there is no plan. I haven't thought about it. Yeah. You know, it's... I don't know. There's a few kits that I want to get done and there's, you know, blogs I want to do and I want to tidy up the workshop and, yeah, I don't know. I guess I have to be a bit more self-sufficient now because I've often relied on work stuff. You know, work often have better stuff than I have at home in the lab here, so...

**Chris Gammell:** Oh, you mean for, like, gear or you mean for...

**Dave Jones:** Gear, as in, you know, especially, you know, in terms of, you know, soldering, surface mount stuff like that. Oh, yeah. So, yeah.

**Chris Gammell:** Yeah, and the other thing, too, to think about is just the inspiration, too. I mean, like, not that work's always inspiring, but just, like, if you're encountering problems when you're challenged with, you know, a work problem, not necessarily one that you bring to yourself, then, you know, that's something to write about or blog about or make a video about. That's kind of like just kind of tips your brain off and you start thinking about it and then you're like, oh, I should make a video about this.

**Dave Jones:** Yep. Well, that's the other thing. As a non-sequitur here, the blog, like, how I call each blog a blog, right? I call each video a blog. Oh, I've done a blog. Here's my latest blog. And I've heard people on Twitter, you know, say, oh, that's not correct. It's a blog post. Thank you very much. And it's not a blog. A blog is an entity. And it's like, oh, give me a break. Or it's an entry. And, well, I'm going, well, I'm sorry, but I have a video blog. I have a radio show. I have a forum. Or they say it's a post. Just call it a post. I'm going, well, is it a post on a forum? Is it a post on a blog? Is it a post on a comment? Is it a what? I mean, you know.

**Chris Gammell:** I think those kind of things are just best ignored. You're like, all right.

**Dave Jones:** Exactly. Thank you for the input.

**Chris Gammell:** See you later.

**Dave Jones:** I mean, right.

**Chris Gammell:** I mean, I don't know. Yeah.

**Dave Jones:** Yeah. I've always gotten those comments. You know, people who. Semantic. Semantic.

**Dave Jones:** Semantic. Yeah. Semantic experts. It's a blog post. Yeah. Well, you try having a video blog in a forum and then try calling a blog post every time.

**Chris Gammell:** Keep it on straight, buddy. Right? Yeah. Yeah. Yeah.

**Dave Jones:** No. No. It's just easier to say blog. Everyone knows what you're talking about. It's not like you go start up a new blog every day. Oh, go read my latest blog. And you think, oh, it's a new blog. No. It's a blog post. That'd be like me. Right. Yeah. You'll start up a new one. Start up a new one. And then be done. That's right.

**Chris Gammell:** Yeah. Yeah. That's how it seems lately.

**Dave Jones:** How's the engineer's blog going? Engineer blog's going okay. Engineer blog.

**Chris Gammell:** Blogs.

**Dave Jones:** Blogs. Engineer blogs. Dot com. Yes. Dot org.

**Chris Gammell:** Dot org.

**Dave Jones:** Oh, sorry. Dot org. Surely you own the dot com too.

**Chris Gammell:** No. No, I don't. That was not available.

**Dave Jones:** Oh, really? Yeah. Oh, okay. So, is there anything there or is it just a squatter?

**Chris Gammell:** No, it's a squatter. Right. I'm not paying anybody for that shit. Yeah. Yeah. Awesome. And speaking of paying someone, we'll get back to the Altium thing a little bit because I would like to hear more about that. But paying someone. So, we should probably mention this because it is kind of big news too. So, you kind of got overshadowed a little bit even. Right.

**Dave Jones:** Oh, yes. Go for it. Yeah, let's talk about this for half an hour.

**Chris Gammell:** Texas Instruments bought National Semiconductor. That's kind of a big thing.

**Dave Jones:** Yeah. There was no drum roll there. But, yeah, that's kind of big. Right. That is... That's pretty huge. I mean, you know, Toya are this massive... They've been gobbling up companies left, right and center, it seems. And National... Yeah. National... I keep saying National Instruments for some reason. I...

**Chris Gammell:** It's tough because it's Texas Instruments. Then you want to say National Instruments. I know.

**Dave Jones:** And I actually did that on the blog the other day. I was actually playing it back, listening to it. And I said National Instruments when I meant National Semiconductor. It's like, oh. Yeah. But I think everyone knew what I meant. Anyway. Yeah. That's big news. That is huge.

**Chris Gammell:** Yeah. It's a big news just... I think even just from the fab aspect because, I mean, both of them fab their own parts. I'm not sure if they fab all of them. I think National Farms has some of theirs. Probably not. Yeah. Right. But I don't know. I've already been talking to people on Twitter about it, just about cross-part numbers and stuff like that because National and TM, they both make a lot of great op amps, right? I love both of their op amps. And, you know... There's a lot of overlap there. There is a lot of overlap. And that means that that's going to be a focus for cost reduction, right? They're going to probably start trimming off numbers and...

**Dave Jones:** Well, but they haven't said that. I think in the press release, doesn't it say that they're not going to do that? Part numbers won't change. No one would say that up front, though. No, of course I wouldn't, but...

**Chris Gammell:** It's just over time, they'll start fading it out, right? And then... Right. I think just in general, the entire ecosystem kind of... There's more... There's fewer players, and so there's fewer competition. There's less competition, right? Right. Which kind of stinks for the op amp people. It does.

**Dave Jones:** It does. I mean, certain things... There's so many other areas they overlap, too. It's not just the op amps. So I haven't gone through the list. God, it'd take you all day just to go through them and cross-correlate between the different product portfolios. Yeah. Yeah. Wow.

**Chris Gammell:** Well, yeah. And a lot of... I mean, this is... They're now the biggest... The third biggest chip maker and the biggest analog chip maker. Yep. So people know I do analog. This is a big deal for me. You know, like... That... So just from that perspective alone, kind of... I mean, TI has a lot of other stuff, too, right? Like, they bought Luminary Micro.

**Dave Jones:** Luminary Micros for the 32-bit. Yeah. Yeah.

**Chris Gammell:** And that's okay. I mean, they're kind of...

**Dave Jones:** That was a good fit. I said... I think I did a drive-time rant on that. And yeah, they're a decent fit. Yeah. Because TI only had the 32-bit DSPs. Yeah. Really, you know. They didn't have a proper 32-bit micro solution.

**Chris Gammell:** And then they had the MSP430, right? Which is not...

**Dave Jones:** Which is a 16-bit. Yeah.

**Chris Gammell:** Right. And that's not high power. You can't do a lot of... No. No, that's right. Fancy processing with that. No, not at all. That's 16-bit. I thought that was 32. I don't know why I thought that.

**Dave Jones:** No, that's 16. It's sort of an... I'm not sure if they call it a true 16-bit architecture. It's more of a sort of a quasi 8, you know, 16-bit architecture, I think. Yeah, kind of. Yeah. Something like that, anyway. Yeah. But I think it's closer to a true 16-bit than some of the others that claim to be, you know, 8-slash-16-bit hybrids. Yeah. Yeah. Anyway.

**Chris Gammell:** Yeah, I mean, some certain parts, like, no love lost there, you know, like, a lot of the power converters. I mean, like, National makes some okay power converters. And, you know, they have... I heard a lot of people talking about, like, the app notes, like, the national people write better app notes or something like that. Right. Yeah. That... Yeah. A lot of that stuff's going to transfer over, you know? Like, I doubt TI's going to want to wipe out entire department. Well, maybe they will. Right. Right. You know, some of that talent's going to stick around, I'm sure. Just because fewer chip makers in the market, you know, like, there's fewer places to go. So...

**Dave Jones:** Yeah, of course. So... You wanted to say... Your advice, I saw on... I think it was on Twitter that... To TI... To... Oh, yeah. Yes. No, was it... Anyway, tell us.

**Chris Gammell:** It was to National. It was... National. Don't let TI make your videos.

**Dave Jones:** Videos, that's right.

**Chris Gammell:** Yeah. Yeah, there's some bad ones. Yeah, they mentioned.

**Chris Gammell:** I won't lay into them. I mean, it's just... You know... Now, I heard there's this world-famous video blogger available now who could just make videos, so... There is. Maybe they could, you know, talk to him.

**Dave Jones:** They can. I charge at an hourly rate.

**Chris Gammell:** There you go. Start doing contract videos. Yeah.

**Dave Jones:** That's right.

**Chris Gammell:** Yeah, who knows.

**Dave Jones:** That'd be interesting.

**Chris Gammell:** I don't know if... It would. Yeah.

**Dave Jones:** Well, I've kind of had a... A little baby steps into that kind of area. So... And there's a few things on the boil at the moment. So, yeah, I might be doing contract videos like that, so you may see my head around on various websites.

**Chris Gammell:** Yeah. Yeah. Well, hopefully, just you'll make it a little more exciting than they make some of those videos. Right. Yeah. Because there's the two extremes. There's the smash it, which is... I think we've talked about on here before, and where they just, like, smash up a product and look at what's inside. It's like... Right. Yeah. And then the other one is, like, they just have a guy sit in front of a PowerPoint presentation, and that's not even good in person, you know? Yeah. So, anything's better than that.

**Dave Jones:** I've got to admit that I'm talking to somebody at the moment who shall remain nameless, and they want me to do pretty much that. Oh. But they want my video... You know, they've asked me, make the video fun and entertaining. Make it fun and here's your slides. And also, we want PowerPoint slides to go together, and we'll edit it so that... Wow. You know, so... Yeah.

**Chris Gammell:** If they're listening, that is not what users desire. No. It's like, ooh, you can use fancy clip art, though. Nah. Blah.

**Dave Jones:** It's so 1990s.

**Chris Gammell:** Oh. Oh, dearity. No, thanks.

**Dave Jones:** Yeah. Death by PowerPoint. Yeah. Yeah, right.

**Chris Gammell:** Yeah.

**Dave Jones:** Incidentally, I'm not using Microsoft Office anymore. I'm using the... Open Office? The Open Office, yeah. Yeah. Yeah, I'm using that because, well... Yeah, I got my new computer and it didn't have Office on it, you know? Yeah. So, I didn't have a license, and I hate the new one. The new look and feel of the new Excel and everything else is shit. So, yeah, I've been using Open Office, which is great. Highly recommended.

**Chris Gammell:** Yeah, I mean, it's... I don't know. It's still PowerPoint. I mean, it's still the same concept, though, right? So, if you're... Oh, yeah. If you're sitting in a presentation and someone's just reading from slides, you know? Yeah. That's when it really starts to stink. I know. So, hopefully...

**Dave Jones:** But, unfortunately, that's all these corporate companies know how to do, you know? Right.

**Chris Gammell:** And that's why they need to hire brilliant video bloggers and radio shows, right?

**Dave Jones:** They do. Absolutely. Yeah. People who just don't do it the corporate way because, yeah, that's...

**Chris Gammell:** Because they just got laid off from a corporation. Right.

**Dave Jones:** Oh, dear, Eddie.

**Chris Gammell:** So, what about TI? I mean, that's all I can really think of in terms of, like, the... I mean, obviously, there's a ton of overlap. Yeah. But I think of, like, power and I think of, like, op amps and analog stuff. I mean, TI...

**Dave Jones:** National's got a lot of power stuff. Yeah. But I've always sort of shied away from their power stuff because their simple switch of stuff was always just wasn't that simple, as, you know, ironically.

**Chris Gammell:** Yeah.

**Dave Jones:** And I, you know, it was kind of sort of my... National was sort of my last choice for that, really. Yeah. They were... Well, not last, but they were down.

**Chris Gammell:** You're talking about designing, like, FPGA-type boards for that kind of thing?

**Dave Jones:** No, I'm talking about power. Oh, yeah, power supplies for FPGA boards. Oh, yeah, power supplies for doing, you know, yeah, doing the 1.2-volt rails and everything else and the... Yeah. Yeah. All those, you know, because it's not uncommon to have, you know, five different power rails in a digital product these days. Right, right, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Five, 3.3, 2.5, 1.5, 1.2, you know?

**Chris Gammell:** Yeah. 0.9. Unbelievable. Yeah, 0.9. Yeah. Yeah. Core voltages. Yeah. I think the thing that they were really targeting... And you could see it, too, if you go to, like, the web bench thing. And, you know, I liked web bench. I think we talked about that on here before. Yeah, I'm not a big fan of it. I'm not a huge fan of it. But the thing is, like, I didn't use it as much at work, but I started doing it for, like, side projects and stuff. And if you just need to crank out a design real fast, that's kind of where it was... It kind of popped out. And I think that's what they were really targeting. They were targeting, like... So, like, it's a simple switcher thing and the FPGA-type power rails. What they were really trying to do is get people that were digital designers, right? Yeah. And mostly knew how to code and were doing FPGA. They had to do everything, right? That's right. And maybe didn't have as much power experience. They just want to throw something down. That's the kind of thing that they targeted. Yep. And, you know, people pay a lot for that because it's easy and... Oh, of course, yeah. It makes sense for getting it out to market fast, too. But if you have time, you can start cost-optimizing and doing all the stuff you were probably doing on your designs, right?

**Dave Jones:** Yeah, exactly. Yeah. And I found they weren't that cheap, the national parts, either. Yeah. So, you know, it's... Yeah, because usually I'm going to go for the lowest cost... The simplest and lowest cost part first, as you would. Yeah. Really. Yeah, unless you have some need for, like, a soft start. Unless you have a specific need, yeah, exactly. But there's so many players out there in that market, you know. There's... Yeah. Oh, it's just endless, really.

**Chris Gammell:** I think they started getting into trouble, too. Like, because remember they had that reorg a couple years ago. Right. Was it years ago? Yeah, I guess it was when the downturn happened. You know, they laid everybody off. That's when Bob Peace stopped working for... That's right, yeah. ...stopped working for him, but he wasn't... I think he got laid off. I don't know.

**Dave Jones:** He was laid off, I believe, yep.

**Chris Gammell:** I think he still consults for them or something, but... Possibly. But not necessarily... Not nearly as much. He's not, like, the main apps guy, like people remembered him from, so...

**Dave Jones:** Well, but that's a... Let's talk about that. That was like a PR... That's like PR suicide, right? Oh, yeah, yeah. If you're going to lay people off, why lay off your highest profile engineer? Yeah, I don't get that. Like, public profile engineer. He's massive. He's been massive for 20 years. I know. Everyone knows him, and everyone, when they think of national semiconductor, they think of Bob Peace, right?

**Chris Gammell:** Well, I think they tried to play it off as, like, a retirement or something like that.

**Dave Jones:** Yeah, but, oh, man. And I'm pretty sure it was a retrenchment. Don't quote me on that, but... A what? A retrenchment. That's what we call it here in Australia. Yeah. Oh, dearity.

**Chris Gammell:** Yeah.

**Dave Jones:** And, yeah, I thought that was just a bad move, really. I mean, sure, if Bob wanted to... Maybe it was a voluntary thing. Maybe they'll offer involuntary redundancies, as we call them here, where they, you know, just send out, look, if you want to go, you know, as long as you're not the CEO, we'll let you go, you know. Yeah. Kind of. Yeah.

**Chris Gammell:** Yeah, it was actually back... It's funny. I just typed it into Google, the National Semiconductor... What did I say? Layoffs, I think?

**Dave Jones:** Right. Yep.

**Chris Gammell:** And it said... What did you find? It said... It had, like, the autocomplete, where it's, like, National Semiconductor Layoffs, 2008, National Semiconductor Layoffs, 2009, 2010.

**Dave Jones:** It's like, holy crap. I love that. A lot of people have Googled it, obviously. Yeah, right. I love that Google history, because it shows you what people have been typing in, you know?

**Chris Gammell:** Yeah, that's great. It's great. It's terrific. There's some funny ones, too. I love seeing some of the funny ones that, like, autocomplete for you. Yep. But, yeah, so that was back in March of 2009. They laid off 1,725 people.

**Dave Jones:** Wow. And I think... Out of how many? That was...

**Chris Gammell:** Oh, no. Let me see. Maybe here. That's 26% of their workforce.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah. Wow. I remember people complaining then about Brian Halla, the guy who's the CEO. And basically, they're saying that he's flushing the company down the toilet.

**Dave Jones:** Right.

**Chris Gammell:** And, you know, it sucks that it happened, you know? Yeah, absolutely. I don't know what the story is with Brian Halla, but they got rid of peace, so that automatically turned a bunch of people against him just from that... I think so, yeah. Yeah. Yeah. Yeah.

**Dave Jones:** It rubs everyone the wrong way, and yeah.

**Chris Gammell:** I know. And he's such a lovable guy, too, right? Yeah. He's so quirky. Absolutely. You know, writes so often. Yeah.

**Dave Jones:** Yeah, well, he's been doing it for more than 20 years. He's been writing for... Yeah. ...Electronic Design Magazine. Sorry, almost mixed him up again. Yeah. We've done that before.

**Chris Gammell:** Yeah. So, it says... Let's see. March 11th, 2009, they did all his layoffs, and they closed the plant in Suzhou, China. And then he announced his retirement in October 9th of 2009. Okay. And then, since then, Don McLeod has been in charge. Right. So, I don't know. Like, maybe they were trying to shop around after that point, but whatever they were doing... Hmm. Yeah.

**Dave Jones:** Well, yeah, I don't know. It's a shame, because I hate when, you know, these big old names just... I know, right? It's just going to get sucked in, right? It's just going to get sucked into the void, and, you know, it will eventually dissipate. One of my favorite words. Yeah. Dissipate into the ether, you know? Yeah.

**Chris Gammell:** Well, I mean, one of the reassuring things is that TI is kept on the Burr Brown name. So, you know, they still have the OPA parts and the INAs and all those. Yeah. And those are like...

**Dave Jones:** Are they still actually branded Burr Brown?

**Chris Gammell:** Yeah, they still call them that. So, if you go to, like, a seminar or something, they'll still call them Burr Brown.

**Dave Jones:** Oh, awesome. Right. Which is...

**Chris Gammell:** That's good. I mean, so, TI, pat on the back for that. Keep going with that. And, you know, keeping part numbers, too. Like, you know, if you're developing new stuff, you don't have to make it the new stuff. Although TI is... I believe the same group is still developing OPA parts. Right. Yeah, of course. Yeah. So, those are still Burr Brown, technically.

**Dave Jones:** Yeah. But then again, it's a two-way street there. I mean, as a company, you think they should consolidate. You know, when you buy a company, you should... You know, you really shouldn't keep that existing brand. Unless it has, you know, some huge... So, I can understand them wanting to absorb things. I have more problem with actually being acquired in the first place, really, than, you know... Yeah. Well, if they don't...

**Chris Gammell:** I mean, if they don't start consolidating, you kind of question, well, why the hell do they do this? Why? Yeah. Yeah, exactly.

**Dave Jones:** Why did you bother? Yeah.

**Chris Gammell:** I mean... Unless you start changing the name around. Someone on Twitter wrote to us about... And put together a national... A Texas National Semiconductor Instruments logo or something like that.

**Dave Jones:** Yeah, I saw that. Well, that's like Danaher, right? Yeah. You may want to be silent. But they, you know, they're this big conglomerate no one's ever heard of. But they own, you know, Tektronix. They own Fluke. They own, you know, Keithley. You know, a whole bunch of big names. But they don't consolidate. You know, they keep those companies separate and manage them all separately. And, well, mostly. And, you know, it's different. But when a company like TI, which is a player in the same... A major player in the same space, takes over another major player in the same space, you know, that's a different sort of kettle of fish, really. Right.

**Chris Gammell:** Well, no one looks at TI and says, oh, TI, you know, like... There's definitely a lot of brand recognition there that, you know, they make a lot of great stuff. Like, especially from the analog side of things. I mean, a lot of their parts are great. Like, especially those Burr Brown parts I talked about. I love those things, man.

**Dave Jones:** Oh, I love Burr Brown parts. Yeah. One of my favorites. But, and TI, of course, famous for their DSPs and other stuff. So it isn't just analog side of things.

**Chris Gammell:** Yeah. I'm looking at the national webpage, too. So the webbench designer kind of... And just the front page, too. So it seems like a lot of the audio stuff, too. You know, and that's the thing. When that 2009 thing started happening, you could see them start transitioning towards these large, large consumer market kind of things. You know, like, they have a lot... They still have a lot of sensitive parts that I use a lot. But the...

**Chris Gammell:** You know, they started going towards mass market type stuff like audio stuff, LED lighting, power management, that kind of stuff. Yeah. Where you're going to sell... You know, it's great from, like, an executive standpoint because you look at it, you're like, oh, we're going to sell a million units, right? Yeah. But... And it's a lot less... A lot less niche and a lot less... Or niche. Niche. You know, and there's a lot less you have to... Maybe you don't need as much type of process control, that kind of thing, like in the fab. Yeah. So you can crank this stuff out more. And I think they even started pushing stuff to TSMC at that point. I'm not completely sure about that. Right.

**Dave Jones:** Possibly. I think they may have. And National do a lot of niche stuff, you know? Lots of LED solutions, lots of data conversion solutions, you know? And they do VGA, you know, display drivers and, you know? Yeah. Sort of, yeah. But still, it's still a mass market, right? Lots of timing stuff, PLEs. Oh, yeah. Yeah, it is. They're the things that are used in your TVs and stuff like that. Yeah. Yeah. And they... So they do some things really well and other things they just do a lot of.

**Chris Gammell:** Right? Yep. That's right. So it'll be interesting to see as they start transitioning the portfolio over, kind of just to see how much of the power they start getting rid of. I mean, maybe they'll start getting rid of TI stuff. But I think TI... Right. ...owns Unitrode. That's the company they bought. Yes, I think they do. Yeah. So... And that's a really... That's just like a Burr Brown name, right? So... Yep. Unitrode made some great, like, switcher stuff. And... Yep. I have one of their app books, I think. Right. Like, uh... Transformer design kind of books. Yep. So... And, you know, they're starting to go into sensors and a lot of sensor kind of stuff and that kind of thing. Which... Which kind of might be selling to Altium. I mean, who knows? The...

**Dave Jones:** Right. So...

**Chris Gammell:** So let's hear a little bit about the Altium plans.

**Dave Jones:** Well, actually... Well, one more thing with that. Okay. One more comment is, um... That are national too big to absorb?

**Chris Gammell:** Oh, like an antitrust kind of thing?

**Dave Jones:** Well, no. But just in terms of their sheer product portfolio, I mean... Oh, yeah. You know, you'd have to dump, you know, half of it or more. It's just... It's just... Will they... I'm curious to see how long they will actually... run national as a separate entity? Right, right. They may not... They may go, oh, shit. Yeah, we bought them. But this is just too darn hard. You know? Yeah. We can't possibly, you know, merge groups. So we'll just run them as a separate company. It's easier and take the profits. Yeah, yeah. Maybe that's... Maybe that's their intention. I don't know. Because they didn't mention in the press... Well, they never do mention in the press release. Right, right. Because that's a forward-looking thing. Oh, yeah. And they don't like doing that. Yeah. So it's a technical term, forward-looking statement. Oh, yeah. You're allowed to have those. Yeah, right. Well, Altium do that. So we'll get on to that. Altium love doing that. But, yeah, these big companies who take over, other companies usually don't say those sort of things.

**Chris Gammell:** Yeah, I don't know about the actual portfolio and, like, managing it. But I know for sure that one thing they want to do is try and, like, squash down the number of fabs they have. Because that is expensive, you know? Oh, yeah. And they both do have their own fab. I mean, Richardson, Texas, TI's and fab out there is huge. And they're actually...

**Dave Jones:** So they may consolidate in that area, but not so much in the product portfolio area. They may just make better use of... I think they mentioned that in the press release, didn't they? They were going to make better use of their, you know, their fabs. Right.

**Chris Gammell:** And another thing they point out is that TI has one of the only... I think the only 300-millimeter, so 12-inch wafer, analog fabrication facility, just because a lot of those were running on older processes. You know, they would run on, like, 180 nanometer. Oh, jeez. Or even 90. Ancient, right?

**Dave Jones:** Jeez, you can print that at home these days, can't you?

**Chris Gammell:** Nice. Yeah. That's what you can do with your spare time, Dave. Just start to make a chip printer. There you go. There's your road to riches and stardom. Fortune and glory, kid. There you go. All right. Yeah, so it'll be interesting to see how much they actually pushed to Texas. And I think that... I'm kind of looking at the national wiki page right now. And... Huh. Interesting. I did not know that they owned Fairchild, too. So national acquired Fairchild. Yeah. Yeah. Back in 87.

**Dave Jones:** Yeah. That was a long time ago. Yep.

**Chris Gammell:** Yeah. So that's two big, you know, juggernauts that are now... Yep. I mean, so TI is big, man.

**Dave Jones:** I know. They are massive. Yeah.

**Chris Gammell:** Yep. And so they have a fab out in Portland. I think that's Maine. I think it's Portland, Maine. Right. I hope I'm not wrong. But, yeah.

**Dave Jones:** Anyway, my guess with that whole thing is that they'll just consolidate behind the scenes in terms of fabs and national will still exist for many, many years as a separate entity. That's my guess. Well, yeah. I haven't really thought about it, but, you know, I just think it's too hard. You know, when a company that size is just... You know, it's easy when you buy Luminary Micro. You know, they just got micros and, you know, bang, we can just slot that in, relabel them as TI. Yeah. You know, that's it. Easy. Yep.

**Chris Gammell:** Well, I think no matter what, we are going to see weeks and weeks of analysis on this because, honestly, this is like the biggest freak out to happen to technical magazines in years.

**Dave Jones:** And no one seemed to have an inkling of it, I don't think. It seemed to come as quite a shock to most people I've spoken to.

**Chris Gammell:** Yeah. I was talking to someone who said they predicted it a while back. Oh, right. Okay. But I was like, yeah, show us the stock transactions and I'll believe it, right? Right. It's like, it's easy to say one thing, but put your money where your mouth is when that happens, right? Yep. Someone's retiring on their earnings from that $12 jump or whatever the stock was. That's right. Yeah. That's a little different.

**Dave Jones:** Speaking of not being able to predict something, let's get on to Altium.

**Chris Gammell:** Yeah. Yeah. Let's talk about it since we're allowed to now.

**Dave Jones:** I am allowed to. And I don't think I can actually say, I don't think it's possible for me to say anything that I'm not supposed to because I don't really know anything more than what's in the press release, really.

**Chris Gammell:** He's basically clueless, folks.

**Dave Jones:** I'm basically clueless. And this is one of the problems. Right. The announcement. We will put a link up because this is big news in its own, right? Because Altium, EDA, Protel, is a much-loved EDA tool by many, many tens of thousands of engineers worldwide. Right.

**Chris Gammell:** Right.

**Dave Jones:** So it certainly deserves to be talked about in its own right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I certainly would have talked about it if I hadn't ever worked there. Yeah. Yeah.

**Chris Gammell:** Let's do it. We should state that. I mean, you still like the software. You still plan on using it?

**Dave Jones:** Well, yeah, I've been using Altium back since the Protel AutoTracks 1.6. I've been using it for 20-plus years. And I love it. It's my favorite tool. It's the only tool I've really used. You know, I've played with a couple of others.

**Chris Gammell:** Basically clueless, folks.

**Dave Jones:** Right. Other than Altium. Yeah, exactly. Because it's the tool I grew up with and I love. And all of my comments will come from a user perspective because I'm going to continue to use it. Yep. And, you know. Unless they find you and shut you down for saying all these things you're about to say. Right. And, you know, and I'm outspoken and I'm going to say my comments from a user perspective because I don't think I'm too dissimilar to the other users. So, you know, this is not coming from an ex-employee. A bit louder. Yeah. I have been known to be a bit loud. That's okay.

**Chris Gammell:** That's what you're known for.

**Dave Jones:** That's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, the big, we'll put up the press release announcement, but basically Altium are relocating their global headquarters to Shanghai in China. As you know, it's an Australian company. You know, it's famously an Australian company. You know, big Australian success story taking on the world and all that sort of stuff. And, well, yeah, they are moving lock, stock and barrel to China. Yeah. And as a result, a whole bunch of people were made redundant or laid off in US speak. And even I don't know the exact numbers of how many, but it's a lot, basically. Yeah. And the idea is to move all their R&D to China and pretty much, you know, start again. Really. They're moving their core R&D over there. Yeah. But, yeah, it's still up in the air of who's going to go and stuff like that. So, I won't talk about that.

**Chris Gammell:** Right, right. I mean, that's not really relevant to the user side of things. No, no, no. It's not. Since we are solidly on the user side right now.

**Dave Jones:** Yep, absolutely. In fact, I – and this came out of the blue, by the way. This, you know – well, if it was in planning for the last year, you know, nobody knew about it. It's as big a shock to me as it is to everyone else.

**Chris Gammell:** Right, and I should state right now that I am on the Altium website and it is not on the website. There is a third-party press release company. So, I don't know how much they actually don't want to – you know, it's a press release, it's out there, but it's not – it's not like it splashed all over like in a national site says, hey, we just got bought by TI. It's not like, hey, we're moving all our stuff to China. Right.

**Dave Jones:** Well, they – I think they – I don't want to speak to them, but I think they know that it's not going to be a popular decision. As many Altium decisions because Altium is a company that likes to push the envelope. They always pride themselves on being, you know, five years ahead of the market. You know, they always – they're a visionary company, not a nuts and bolts, you know, let's –

**Chris Gammell:** A commodity player, right?

**Dave Jones:** Just a – yeah, exactly. They pride themselves as a visionary company and occasionally they've got it right and occasionally they've got it wrong. And so, in my humble opinion – well, in fact, you can look at the – User opinion. You can look at the – well, you can look at the financials yourself and, you know. Right, right. You know, you can – you know, all this is part of knowledge.

**Chris Gammell:** But we talk about electronics here, so we won't talk about financials here.

**Dave Jones:** Exactly. But anyway, they're moving – you know, I don't really have a problem with that because the company is not doing great financially at the moment. So, I can understand if they want to move to China and lower their labor costs. You know, that's great. You know, I certainly wish them all the best. But it's not just the move to China. It's the fact that they're now publicly stated that they're focusing on – oh, there are so many –

**Chris Gammell:** Oh, here we go. It's at the top of the press release. The ecosystem of devices.

**Dave Jones:** The ecosystem of devices. No, ecosystem.

**Chris Gammell:** Echo.

**Dave Jones:** There's no H in there. I know, right?

**Chris Gammell:** All right, you win this time. You win this time.

**Dave Jones:** Ecosystem of – right. Ecosystem of devices. And other terms they're throwing around is this internet of things. I'm using the quote marks, you know. Right, right. And there's so many other wank words. It's not funny.

**Chris Gammell:** Here's my question about the internet of things. Wasn't that in the early 2000s when my refrigerator was going to order me another carton of eggs? I mean, that's what I think of, right?

**Dave Jones:** From a touchscreen on the front. Yeah, exactly.

**Chris Gammell:** That's what I think of.

**Dave Jones:** The internet was going to be pervasive was the term, you know.

**Chris Gammell:** Well, it has done that, but in a different meaning of the word.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Pervasive or – oh, perverted. Oh, that's what it is.

**Dave Jones:** And, of course, nothing they say in this area is wrong because it's true. But – But. You know, there's always a but. It's only true in certain areas. It's true in terms of, you know, your iPhones and your – you know, and all your other consumer type stuff. Right? Right. But I don't know. Is it relevant to an EDA company? Well, what can I say?

**Chris Gammell:** That's if they stay as an EDA company, right? I mean –

**Dave Jones:** Well, that's – well, exactly. Because they want to get more into the content side of things and they – you know, IP and content and solutions for developing internet-enabled applications, which is great.

**Chris Gammell:** So, we should talk about that some more. So, basically, as far as you understand it, as far as I understand you explaining it to me, the Internet of Things or the ecosystem? Ecosystem, sorry. Ecosystem? Yeah. Of devices. Of devices, right. Yeah. It would be like embedded systems with an Ethernet connection, basically communicating data back. Yep. Smart. So, like smart power meters.

**Dave Jones:** Smart devices. Yep. Smart, yeah. Altium have done a white paper on this. Okay. You can have a read. We might post a link. Yeah. They believe that every electronic device in the future will be internet-enabled, internet-connected, which is great. And it's probably true in the consumer sphere.

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** But – there's always a but.

**Chris Gammell:** And you cannot lie.

**Dave Jones:** How many devices are there out there that simply won't need that? Industrial stuff, just other everyday – you know, there's millions. There's – I wouldn't even want to count the number of boards which won't be internet-enabled. Right. So, you know, and –

**Chris Gammell:** Or even – well, what about like internet versus like intranet, right? Also that. I mean like there's certain things that can't be on the internet, right?

**Dave Jones:** That's right. And in fact, there's a lot of companies who – because Altium is going to this live – the Altium live solution, which means you're always – the tool is always tied into the web and for live updating and content. Cloud-based. Which is great. You know, cloud-based. Oh, yeah. Yeah. Which is a great solution, but it's not for everyone. You know, not everyone is allowed to do that. In fact, there's so many engineering companies out there that can't even – they don't even have an internet connection on their desktop because they're not allowed to due to security concerns and all sorts of other, you know? Yeah, yeah. And I've certainly worked at companies like that where, you know, if you want the internet, there is – well, yeah, certainly in the last five years, yes.

**Chris Gammell:** Yeah.

**Dave Jones:** And where they have a – there's one computer in the whole company and it sits in the corner and it's fenced off and it's the internet connection and it's not tied to the network. And if you want to go surf a website, you have to go physically sit at that computer and – Really? I don't know. Yeah, absolutely. Do you think that still happens? Have you talked to anyone that still happens? Yes, that still happens. Wow. That still happens. I'm impressed. Especially military companies, other companies which have – I could see it. – are bound by their customers, i.e. defense companies and stuff like that. Yeah. You know, our – because you're dealing with our secret data.

**Chris Gammell:** Right, right.

**Dave Jones:** You know, you have to physically have a disconnect between the internet and your internal systems. Yeah. That's end of story. So, you know, yeah. That is real and it happens at more companies than you would think.

**Chris Gammell:** That's crazy. And that's actually that story that we mentioned with the Iranian centrifuges. Remember, that's – they actually had to jump that with like a jump drive or something like that. Yeah, yeah. And it took for so long. Apparently, there's a talk to someone – Harry wrote in on our suggestion page about that. There's a TED talk about that. So, I'll post a link to that. So, just as a side there. But that's crazy. You don't think about a lot of companies that can't have an internet connection to desks. But I guess that is the case, huh?

**Dave Jones:** That's right. And yeah, and it's more – there's more companies out there than you would think.

**Chris Gammell:** So, yep.

**Dave Jones:** Crazy. Yeah. So, Altium have said that they want to focus more on this and less on their core tool. They've stated this publicly on the forums and various other places. And yeah, it's – you know, that's great. Good luck to them.

**Chris Gammell:** Dave respectfully disagrees or –

**Dave Jones:** I respectfully disagree. Yeah. Their core product. I mean, they've got the best PCB design tool on the planet, bar none, in my opinion. You know, and a lot of people think the same way. And to not – to, you know, chase, you know, this Internet of Things stuff, I think, is wrong. But good luck to them. I hope it works. But yeah, I would love to see focus on the core tool. And that's what all the customers – from my perspective, that's what the customers are saying. The customers are saying – Right. And Altium have admitted this, that they know it's not popular, but they're a visionary company and trust us, in 10 years' time, you'll be thanking us.

**Chris Gammell:** Yeah, you almost wish they'd spin it off, you know, like spin off just the layout software, right, or the EDA software.

**Dave Jones:** Yeah, exactly. Yeah.

**Chris Gammell:** Probably not going to do that because that's their cash cow that then allows them to –

**Dave Jones:** I can assure, yeah, that is their cash cow. Most people simply use the core tools. Because as you know, Altium do FPGA tools as well. In fact, they've spent the last 10 years building up the product, which, you know, it's now an embedded solution. You know, it's a complete tool set. And it's pretty – you know, it's pretty funky. The FPGA stuff you can do in it, it's very impressive.

**Chris Gammell:** Yeah.

**Dave Jones:** But it's not –

**Chris Gammell:** I'll tell you, Dave, the first time I ever saw that board you designed, that nano board, I was so – I was so freaking confused about what the heck I was looking at. Why? Why is that? I didn't know what the heck I was looking at. I was like, what am I using this for? I finally figured out it's like a development platform, right?

**Dave Jones:** It's simply a development board. Right. Yeah, it makes sense. It's tightly integrated into Altium Designer. That's the key.

**Chris Gammell:** But I was so confused. Really? I've been meaning to tell you that, but I was just so – Okay. Maybe it's just me. Right. I don't know. But, yeah.

**Dave Jones:** Well, that's sort of – maybe that's reflected in the sales because, yeah, they didn't – Well, you know, you can check it out for yourself. You know, we sold, you know, quite a few of them, but it's certainly not a huge business for the company. Yeah. The FP – so they spent 10 years building that up.

**Chris Gammell:** And they employed Dave Jones in the meantime.

**Dave Jones:** And they employed me, yes, in the meantime. And, well, you know, they spent a lot of money in 10 years of the – in fact, that was the reason – I believe that was the reason they floated the company was so that they could get money so they could acquire all these companies with all embedded technology and FPGA technology. So that, you know – and 10 years down the track, well, you know, their core business still generates most of their revenue. Yeah. And you got – The PCB schematic tool. So –

**Chris Gammell:** You got to imagine that all these embedded devices that are embedded internet, right? It's going to have the devices you're talking about, FPGAs and everything.

**Dave Jones:** Oh, it certainly does, yeah. So that's a good base. But unfortunately, there's – you know, it's the old – the old problem. Many companies have tried to be one – Everything. You know, everything to all people. Yeah. And it's traditionally never worked. And Altium have tried. And I'm not going to say they failed in the FPGA domain, but it certainly wasn't the success they were hoping for. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah. And, you know, that's a bit of a shame because it is a really nice tool. But that's just the – that's just the technique. There's so many technicalities involved in FPGA and embedded solutions. There's so many tools out there. Companies trust certain tools. Yeah. And they – yeah. And they don't want to move to your – they don't – you know, they're as cool as your tool might be. It may not do exactly what they want, so they're not going to move. So it's hard to be, you know, that all things to all people. Yeah. And now Altium are trying to do it with this internet stuff, you know, this internet of things or ecosystem of devices. So they want to be – they want to focus more on, you know, developing or helping guys like us develop internet-enabled applications, which is great. Yeah. But, yeah, is it – I guess you've got to ask, is it a good move for the company? Yeah.

**Chris Gammell:** Yeah. It's kind of weird, too, because – I don't know.

**Dave Jones:** You know.

**Chris Gammell:** You think about other companies that have done that, and some are successful being everything to their users, right? I mean, look at Apple. I mean, look at Apple, right? People that are with Apple wouldn't go anywhere else, right? And they love everything about every Apple product.

**Dave Jones:** Yeah, true. But Apple don't have a solution for everything.

**Chris Gammell:** That's true. Do they? That's true.

**Dave Jones:** So, you know, they're – whereas, yeah, I – no, they're very successful because they make cool stuff, which people love. Cool stuff. And they stick with it, right?

**Chris Gammell:** Right, right.

**Dave Jones:** But, you know, it's – yeah, I don't know if you can make the comparison to sort of – you know, because Altium is an EDA company. Their core tool is an EDA tool.

**Chris Gammell:** Yeah, software, right.

**Dave Jones:** And that's what people use it for. I can tell you that the majority of users – it's no secret – the majority of users use it as a PCB and schematic tool as they always have. So, you know, that's the bottom line. Yeah. Well, hopefully they won't – And they've said they're going to focus less on that. Yeah, that's too bad. I think it's too bad because I want that solid, you know –

**Chris Gammell:** Yeah, and there's always features you can add on, right? But it's just – it's like you said, it's people don't want to – or the company probably doesn't want to necessarily just focus on that. No, that's right. Even though they could take more market share. Yeah. Well, maybe you can go back as a consultant and tell them all the things you want changed about their software when they realize that that's making them money.

**Dave Jones:** From a user – well, yeah, exactly. I mean, yeah. And they've always been a visionary company. I don't think they've ever been content just to be number one in just PCB schematic. You know, that's not – and I think that's a shame because they could have – you know, I think they've got the tool. I think they've got the – I think they've got the world's best tool and they could have owned everything from the hobbyist up to not quite the ultra high end but, you know, the mid to high end range. They could have owned that entire market, I thought. Yeah. But they haven't done so. As everyone knows, they haven't released a low-cost version, you know. Oh, yeah.

**Chris Gammell:** We have talked about that before when we mentioned Eagle and DesignSpark and how they don't want to release that.

**Dave Jones:** No. Well, exactly. They just don't – they're not interested in competing at the low level. I don't know if that will ever change in the future. I have no idea. Yeah. I have no inside knowledge there but, yeah, I think that's a shame because, you know, it's a great tool and I would love to see people ditch Eagle and take up Altium because I think it's a vastly better tool. And, yeah, they've just abandoned that fight, I think.

**Chris Gammell:** Time to start doing some reviews, Dave. I think you're allowed to now.

**Dave Jones:** I'm allowed to, yes.

**Chris Gammell:** Keep 10 minutes. 10 minutes max, huh?

**Dave Jones:** Right. Oh, boy.

**Chris Gammell:** Hey, I wanted to catch some other things before we're done for the week because we got about 10 minutes left, I think.

**Dave Jones:** Oh, we do. Yeah. Eight minutes.

**Chris Gammell:** I wanted to mention your 555 contest video. That was pretty great.

**Dave Jones:** Yes, I caught a few people with that apparently. You did. I wasn't sure.

**Chris Gammell:** So why don't you explain that real quick? Right.

**Dave Jones:** I, if you haven't seen the video, I did a video where I had found a hidden Easter egg in the 555 timer. 40 years later. 40 years later. If you tune it to, if you take the standard S-stable circuit and you tune it to 55.5 kilohertz exactly. Yeah, and you leave off pin 7, is that right? You leave off pin 5, which is the modulation, yeah? Yeah. If you leave off pin 5, then it would modulate the output signal at 55.5 hertz. And a lot of people believed it. Yeah.

**Chris Gammell:** Yeah, and you got the suggestion later that you should have turned off comments for it, but a couple people figured it out and were pissed.

**Dave Jones:** Yeah, exactly. And a lot of people built it up and tried to replicate it. Oh, that's great. It's brilliant. Yeah. I love it. And, yes, I will post a video of, behind the scenes of how I did it, because a lot of people don't know how I did it. Although, I think on the forum last night, somebody finally cracked it. Oh, good. Apparently, there is a screenshot they captured. My video wasn't. I didn't hide it all in the video, and they discovered. Oh, that's too bad. Yeah. Yep, they discovered how I did it. Oh, okay. Yep. Well, that was. I won't tell you how I did it. I'll leave that for the reveal video.

**Chris Gammell:** That's good. That's good. All right.

**Dave Jones:** Sorry, Hans, if he's listening. Yeah, right. Yeah. Right. Well, yeah, because in the, I say sorry to him in the follow-up video. I've already done. I filmed it at the same time. I thought I'd film it. Yeah. Yeah. That's good.

**Chris Gammell:** It's already done. All right. So the other April Fool's joke that got me. I don't know about other people. Right. So Brian Fuller of E.E. Times, he sends out the E.E. Life newsletter. Right. And I think I might have to copy-paste it. I didn't have a link for it, but I have the actual email. I'll try and copy-paste it in. Basically, he broke the news that Obama had dissolved his cabinet and replaced it all with engineers. And I don't know why, but I just got taken. I was like, what?

**Dave Jones:** That's a, oh my God. It's utopia.

**Chris Gammell:** I don't know why I possibly thought that could have happened. Oh, goodness. Brian maintains that it could still happen, too. I was talking to him about it, but I, yeah, I don't really necessarily think that.

**Dave Jones:** Well, I guess maybe it worked because there had been those stories about Obama was, you know, getting more, it was, you know, praising engineering and it's going to be the savior of America and yada, yada. Right. Yeah. So I guess that.

**Chris Gammell:** Jeff Immelt on the board or on that council, the job council or whatever it is. Right. Yeah.

**Dave Jones:** Okay. So that's what sucked you in, I think. Oh, man. That was in your subconscious. That's why I chose the triple five thing because I knew that was on everyone's lifts, you know, the triple five timer contest. Yeah. And that sort of psychology stuff works. Yeah. And there's another April Fool's SparkFun. Did you see the SparkFun one?

**Chris Gammell:** I don't think I saw it.

**Dave Jones:** The soldered iron?

**Chris Gammell:** No, I didn't see that one.

**Dave Jones:** Oh, have to put it up. Anyway, SparkFun put up on their website, you could buy a soldered iron kit. Oh. And it was a HAKO 926, you know, so they would sell it as a kit. So, you know, you solder it together yourself. And they say to put it together, all you need is to buy another kit and then you can... Oh, that's pretty good. Yeah. The old circular argument of how do you solder... Yeah. A soldered iron kit. For beginners, if you don't have a soldered iron, build your own. Yeah. Yeah. How do you do it? I need a soldered iron. What? Ah! And it was well done. And they actually pulled apart a HAKO 926 and they photographed like as all the separate parts. Oh, that's great. So, they showed, here's your kit. Here's what you get when you buy the kit, you know? Yeah. Oh, it's brilliant.

**Chris Gammell:** That's really great.

**Dave Jones:** Yeah, yeah. That was nice. So, and of course, they were out of stock. They were sold out instantly. Oh, yeah. Right. Right. So, yeah. So, people were trying to add it to their shopping cart, you know? Yeah. That's great. Ah, brilliant stuff. Good on your spark fun.

**Chris Gammell:** So, speaking of the 555 contest, we are still not done. So, sorry about that to everybody who's still paying attention to it. I want my damn spreadsheet. I know. Dave wants his damn spreadsheet.

**Dave Jones:** Speaking of which, I have finished judging the RX contest. The RX design contest. Oh, that's great.

**Speaker ?:** Yes.

**Dave Jones:** Oh, that's great. And geez, that was hard.

**Chris Gammell:** Yeah. You see? That's what I'm saying. It's not easy.

**Dave Jones:** I know. That's why I didn't. That's why I wasn't going to be roped into the 555 contest because I knew you'd have hundreds of entries. Yeah.

**Chris Gammell:** So, you had 30 entries, you said, and you had to judge all those?

**Dave Jones:** There were 36 entries. Yeah. Wow. And yeah, it took a while.

**Chris Gammell:** That's still a lot, though, because those are more complex projects, too, right?

**Dave Jones:** They're more complex. Yeah. Each one has a video like the 555 timer contest and stuff like that. And I'm here to tell you, people, a little tip. If you're going to enter contest, documentation is important.

**Chris Gammell:** Oh, yeah. That is one of the biggest things I found out, too.

**Dave Jones:** That is one of the hugest things. Even though the 555 timer contest didn't have official rules in that regard. Whereas the RX design contest and your circuit seller contest and all the other more formal contests, they have these rules and they have them for a reason. If it says you must do an abstract, you must do it. And the RX design contest said you should do a video. Yep. You know, it'll help your chances. And people went, well, I didn't do a video because, you know, it's just a couple of things on the screen. Right. You know, that's no reason. You shouldn't have made it. You should have just done a video. All I wanted was a video of the thing. Even if it's just the board sitting there. Yep. I agree. And there's text on the screen. But at least you can talk about it. That's what I wanted. I wanted to hear you talk about the design in the video. Right. And you got bonus points for that. So, a lot of people lost out, you know. And Jerry. Jerry did not do any text documentation at all.

**Chris Gammell:** Uh-huh. She just did the video stuff.

**Dave Jones:** She did some cool videos, which were cool, but no text documentation. So, there were points for. Oh, you had like a rubric or something? There were points for text and videos. Yeah. Yep. She lost points there. Sorry, Jerry.

**Chris Gammell:** Sorry, Jerry. You should say sorry about something else, Dave.

**Dave Jones:** Oh, goodness. Yes. Yes. I formally, hereby.

**Chris Gammell:** Yeah. This is our second apology. The first one was for messing up design news versus electronic design.

**Dave Jones:** Oh, yes. Our second formal apology. David Jones hereby formally apologizes to Jerry Ellsworth for a comment made last week where I said, should I? No, I won't even repeat it. But anyway, I apologize for the comment I made last week. It was not intentional. And it is, to my defense, it is a confusing name.

**Chris Gammell:** It was a mix-up of?

**Dave Jones:** A mix-up of, yes.

**Chris Gammell:** Fat Man and Circuit Girl.

**Dave Jones:** It was a mix of?

**Chris Gammell:** Of that. We'll just say a mix of that.

**Dave Jones:** Fat Man and Circuit Girl. I got it correct.

**Chris Gammell:** Dave wrote it out. He had it. He rehearsed before the show. Right.

**Dave Jones:** Sorry, Jerry. I didn't mean it. Yeah. And she declared war on me. Oh, well. Yeah. Yeah.

**Chris Gammell:** She's got another war going on with Ben Heck right now. So, I think you're safe for now. Plus the whole, you know, ocean thing.

**Dave Jones:** Right. Yes. She's not going to come around and burn down my lab.

**Chris Gammell:** Yeah. Right. And so, one last thing I wanted to mention about design contests, since we're probably wrapping up and talking about those for a little while. You know, I've gotten a couple things about, you know, oh, you should do a 741 design contest. And just recently, Gary wrote in about the 12F629 pick contest. It's an 8-bit, 8-8 pin. Oh, is there?

**Dave Jones:** Is there a contest out there?

**Chris Gammell:** No, no. He's saying that we should do it. You know, like, we should have, like, a user-based contest. Oh, right. And I, like...

**Dave Jones:** Oh, that... Right.

**Chris Gammell:** Yeah. I said, you know, like, we've kind of... We're kind of busy. I mean, like, it's just one contest a year, basically. So, thank you for all the suggestions. But, basically, I think, though, like, that kind of thing is perfect to go back to, like, Microchip and say, why don't you guys have this contest? Because you basically are handing them a big old chunk of social media. Because, like... Oh, of course. Yeah. Especially if they keep it simple. You know, an 8-bit thing. Like he said, it would be restricted because it's a 1K memory. So, it's the same kind of thing as a 555. It's simple to learn. It's simple to implement. But you can do some really cool stuff. And the more elegant the solution, the better the contest is going to be, you know?

**Dave Jones:** I totally agree. Yeah.

**Chris Gammell:** So, if Microchip's listening to, you know, listen to Gary. The 12F629 pick is Gary's candidate for the next design contest. And, of course, users are always welcome to do that, too. You know, like me and Jerry didn't do much to make it special. It was just...

**Dave Jones:** No. Exactly. It just happened.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And they can... Because it's cheap. And the development tool... Yeah. Exactly. They can give away a... You know? They can give away a dev tool. Exactly. You know?

**Chris Gammell:** Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** So, that is...

**Dave Jones:** Maybe we'll have to... Yeah. We'll have to put that to them.

**Chris Gammell:** Yeah. Well, we hereby have. Yeah. I guess so. It's out there.

**Dave Jones:** I'm sure Steve Sangy listens to the Amp Hour every week.

**Chris Gammell:** You know, you were still supposed to send him that clip, Dave.

**Dave Jones:** Oh, I know. I was supposed to send him the audio clip of that. Yeah. Yeah, well. It was just too lazy.

**Chris Gammell:** Maybe you can bundle it all together. With all your free time now, you can... Oh, right. Yeah. Absolutely. You can go bump elbows with all these, you know, chip executives. You can go talk to the TI guy and be like, hey, what are you thinking? And then the Steve Sangy guy be like, hey, check out this design contest.

**Dave Jones:** Right.

**Chris Gammell:** And every time you email him, you'll be like, and by the way, I am available to make videos now. I'm a free agent. I am. That's right. Yeah.

**Dave Jones:** Gun for hire.

**Chris Gammell:** That's right. But the Amp Hour gets you for free.

**Dave Jones:** Right. Oh, goodness. But, yeah, the fear is that, you know, if they do it, they'll just goof it up. You know, they'll go into big corporate mode and, you know. Yeah. And just...

**Chris Gammell:** Restrictive and everything else.

**Dave Jones:** And everything else. And, yeah, not, you know.

**Chris Gammell:** Doesn't stop them from trying, though. I mean, you can always... No. It doesn't hurt to try.

**Dave Jones:** Yeah. Very true. Anyway, I think our Amp Hour's up.

**Chris Gammell:** It is. And I'd like to remind people, we got a bunch of suggestions last week after we reminded people. So, send us tweets, send us suggestions on the suggestion page of the Amp Hour. And if you want to hear about anything or you got some opinions on what we talked about this week, you can always leave it in the comments section, too.

**Dave Jones:** Yes. Especially the Altium thing.

**Dave Jones:** I'm sure there's a lot of... Because it's going to be a hot topic. Yeah. Yeah. I'm sure. And I do wish Altium all the best. I hope it works for you. I don't necessarily agree.

**Chris Gammell:** Respectfully disagree. Yeah.

**Dave Jones:** Not so much with the move, but with the... Direction. Well, which is bad enough. But with the direction of the focus. Like, yeah. Yeah. Focus on the Internet of Things stuff. So, anyway. Maybe more about that next week. Who knows? My comments are endless.

**Chris Gammell:** Oh, yeah. You're a wealth of opinion. I am. Yeah.

**Dave Jones:** I am indeed.

**Chris Gammell:** All right. We'll talk to everybody next week.

**Dave Jones:** All right. That one flew by. See you guys. Bye.

**Speaker ?:** Thank you.
