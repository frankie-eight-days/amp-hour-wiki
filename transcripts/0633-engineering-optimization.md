---
episode: 633
title: Engineering Optimization
url: https://theamphour.com/633-engineering-optimization/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released May 22nd, 2023. Episode 633. Engineering Optimization.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEVBlog.

**Chris Gammell:** And I'm Chris Gammell from Contextual Electronics. And welcome to the Luddite Hour.

**Dave Jones:** It's Dymo, damn it.

**Chris Gammell:** It's Dymo. So I was telling Dave before the show, my buddy was at a car show, and there was this very, quote-unquote, realistic DeLorean that was there. And I was like, actually, the labels don't look correct inside of the flux capacitor and on top of the time meter. So it's not – yeah, so a very big nerd moment there. But then Dave and I were wondering, like, what are those labels called? We didn't know what the name of it was.

**Dave Jones:** Yeah, and I tried to get out, Noel. But it turns out it is actually a Dymo. But I remember them as maybe there was some other brand here in Australia, maybe, and that's why I'm thinking of it. Right.

**Chris Gammell:** And people don't know what we're talking about. It's basically like that plastic strip. It's an adhesive back. And then you basically pressed the letter through the plastic strip. And then because you were deforming the plastic, it made it a different color, usually like a lighter color because the plastic was deforming. And that's the look that we all associate with this thing.

**Dave Jones:** It's that embossed look. So they call them an embossing labeler or – Yeah, tape. Embossing labels, embossing tape or whatever. Yeah. And they were always horrible. Like they were always – you know, they would crack and they would fade. They were brittle. They were – the adhesive sucked on them. But it was a thing, right? It allowed you to make labels on the spot. Yeah. And it was magical. And we just found out you can still buy them. Dymo sell a new – I'm bloody – I'm going out and buying one straight after the show.

**Chris Gammell:** Getting that look. Getting that look, yeah. The vintage look.

**Dave Jones:** That old school embossing because I hate them more – have you got a Dymo label printer, one of the new, you know, plastic tag ones? I have one.

**Chris Gammell:** Yeah.

**Dave Jones:** And they're just –

**Chris Gammell:** I mean, they're great for like – I actually really like the ones where you can like label cables and stuff like that. There's like certain ones where you can like go – Yeah. You can go vertical and then like label a – you know, if you get the wrap, the certain type of wrap, you can label a cable and stuff. Like it is super useful. All the stuff they make is super useful. But it doesn't have that certain something where it's going to fall off at some point, you know?

**Dave Jones:** And I find it's one of these like really low-end – like they practically give them away, right? They're like 20 bucks for this label-making machine. You get them in the local supermarket, right? They give you a label-making machine. You're actually buying the tapes, right? That's what you're really buying. And they give you – they almost give you the label maker for free, right? And they're built down to a price. Like they must manufacture them for like eight bucks or something, right? They're like so cheap. And like when you use the thing, like the LCD fades – like they haven't even got a voltage regulator in there, I don't think. So the LCD fades when you push the print button.

**Chris Gammell:** You're talking about the newer ones, right? You're talking about the newer ones?

**Dave Jones:** Yeah, yeah, yeah.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** Yeah, I'm sure you can buy like the higher-end expensive industrial ones and they're great, right? Sure. But the cheap ones, which is all I'm ever going to buy because I'm not doing – Right. – labels in volume or whatever.

**Chris Gammell:** If I do, then I'm doing my paper labels or whatever.

**Dave Jones:** Or I'm doing my – you know, I'm using my desktop printer, demo printer thing. But, you know, like handheld labels, yeah. You just buy the crummy little machine and they're all just dinky little things and the user interface is horrible, you know, and oh, God. Yeah. But anyway, it do work. But barely.

**Chris Gammell:** Yeah. Well, I guess we'll just continue to be Luddites then, huh? Yeah.

**Dave Jones:** Go back to old school embossing.

**Chris Gammell:** Old school and embossing. Speaking of old school, I was enjoying the episode from last week. You know, Microchip has new school as well. But, you know, hearing about the hundreds of varieties of PIC 16s, I'm like, oh, wow. That is –

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** No, there's over 2,000. 2,000. 2,000. 2,000 varieties of 8-bit PIC micros.

**Dave Jones:** Yeah.

**Dave Jones:** Yeah. I think it is. Yeah. Yeah, it is. 2,000. Yeah.

**Chris Gammell:** So I had some things that I wanted to bring up with you because Steve's time is very valuable and I was not on that show. The first one, though, was mostly around the tooling stuff. So, like, he mentioned, like, he thinks that people should still pay for tooling.

**Dave Jones:** Yeah, yeah, yeah. This is a big argument. This is all in the comments. It's all over the forum. It's everywhere. Yeah.

**Chris Gammell:** The first question is, what do you have to pay for? I didn't realize that there was still a lot. Yeah, no.

**Dave Jones:** It's – right. People think you have to pay for the tools. You don't. All of the microchip tools are free. Okay? They're completely free. There's no limitations. Well, the only limitation, the only thing you have to pay for –

**Chris Gammell:** It's your imagination.

**Dave Jones:** Is fully optimized. When you compile something, there's various optimizations. How much code optimization do you want? And I think it's the first – don't quote me, but, like, the first two levels of optimization are free. But if you want the highest level of code size speed optimization, that's what you pay for. Right? How much? You're paying for – because they do actually use the open source GCC compiler for the 16 and 32-bit micros. Right? Technically, you can go download it. Right? You can go download the compiler and you can – you know, it's kind of, like, hard to do, but you can do it. So, yeah. But anyway, their tools are free. So, they're just – you're paying for the optimized thing. So, the IDE is free.

**Chris Gammell:** So, this is MPLAB?

**Dave Jones:** This is the MPLAB thing. Yeah.

**Chris Gammell:** Yeah. Okay. So, that's free. But then if you want to get to the – so, basically, they're, like, gating a feature with a price thing, what – do you know what it costs?

**Dave Jones:** It's $49 a month. $44 a month, which is not a lot. Right? That's not a lot at all. Which is not a lot. Okay. But the argument people are making on the forum is that, oh, I will refuse to use their tool because it's not an open source tool chain that I use. So, I don't want to pay if I have to support a client for the next 10 years.

**Dave Jones:** I don't want to have to pay.

**Dave Jones:** Yeah. Fair. Right? I don't want to have to pay to, like, monthly or whatever. Or you can actually rent it for one month. You can just rent it for one month. Do the update for the customer using the highly optimized, you know, compiler setting. And then you don't – then you only pay the $44.

**Chris Gammell:** What do you do if you want to, like, buy it, put it in your, like, your CICD tool chain and, like – Yeah.

**Dave Jones:** I don't know if you can do that. I don't know if you can rent it for a month and then take a snapshot copy of it.

**Chris Gammell:** That's kind of a bugger. Yeah. I'm not sure if you can do that.

**Dave Jones:** So, I'm not going to say if you can or you can't because I just don't know. Yeah. Okay. But, yeah, of course.

**Chris Gammell:** So, like, I vacillate back and forth on paying for tools. Obviously, I'm very principled when it comes to ECAD tools, of course. I have no problem paying with tools. I pay for tools that I use. Okay. You know, like, really, like, you know, I look at my hourly rate. I'm like, all right, if it saves me an hour, it's, like – if it's less than the cost of an hour, it's literally a no-brainer. It's like, here's my credit card.

**Dave Jones:** Well, 44 bucks, right, is less than an hour of any engineer's time. That's right. It's 10 minutes of an engineer's time.

**Chris Gammell:** And that's what – I'm sure that's what Microsoft is banking on, too. Yes. But I think there is a valid point in there of, like, not owning the tool and, like, expecting it to be part of your tool chain. Like, that is – Oh, totally. That's more significant, I think. You know, that's a big deal. Yeah. Totally. Because that's messing with you. Like, there might not be anyone to call at Microchip in 10 years, like the person mentioned on the forum as well. Right. So that is a totally legitimate argument. Yeah. But I think that's separate from the should you pay at all. There's some people that are just like, I won't pay for anything. It's like, all right. Yeah, fine.

**Dave Jones:** Go and use something else. Yeah. But the thing is, it's free. Like, how often – I think Mike from Mike's Electric Stuff commented on the forum about this. And he said, well, I don't – in the, what, the 20 years he's been using PIC micros or something, I don't think he's ever – I think I kind of – I have to put up – I'll put up a minute to the exact point. You're paraphrasing. Anyway, he's saying, I've never had to use – I've never – there's never been a case where that paid optimized – where that highest optimization setting, which is the one you pay for, has made or break a project. Because you can always rewrite your code in some way. You know, if you don't want to pay for the massive optimization setting, well, just spend an hour optimizing your code a bit better. Hand-hand optimizing it.

**Chris Gammell:** You know, like, okay, fine. Sure. Yeah, so I think – so other things that come to my mind around this is like, all right, so first off, it's a market system. You don't have to use it to parts. That, of course, comes with an extreme caveat of like, well, sometimes actually you do have to use it because your company says so or you have legacy products built on it, yada, yada, yada. So, like, there is always the other thing there. And I think that's why they probably can do this. There is, you know, there is some lock-in with vendors, stuff like that. So, they are – there is just always lock-in with choosing a particular vendor. And if they put a paywall in place, you're just going to pay the tax and move on. And it sucks.

**Dave Jones:** Well, I will actually say I do believe you can actually – because as I said, these tools are free, right? And they actually use the GCC compiler, right? So, if you're doing the PIC-16 or PIC-32, I believe they use the GCC compiler, which, of course, is free and open source, right?

**Chris Gammell:** That's right.

**Dave Jones:** So, you can snapshot that product and you can still use it in 10 years' time even if microchip go bust, right? They don't exist anymore, right? You can still use that tool. No problems whatsoever. But you may have to get a workaround if you want that highest optimization setting. And that's all it is. That's literally all.

**Chris Gammell:** Right, right.

**Dave Jones:** So, I'd certainly be complaining –

**Chris Gammell:** That might be how people work around it with CIC anyways, right? So, yeah.

**Dave Jones:** Well, yeah. And apparently, the workaround is quite easy to get the highest optimization setting.

**Chris Gammell:** Search the EEV blog forum. Dave won't say this, but I will. Search the EEV blog forum. I'm sure you'll find it on there.

**Dave Jones:** I'm sure you'll find it. But anyway, I would be complaining, right, if the code was limited to a certain size, right? If you've got 128K part and the free tool only does 32K or something, okay, right? Yeah, I'd be complaining. Or it only supports half of the peripherals.

**Chris Gammell:** And that is historically how some of these tools did it, too.

**Dave Jones:** That is how some of them have worked. Yeah. Kyle did it, maybe? Kyle did it. They all had free versions of the tool.

**Chris Gammell:** I think Code Composer Studio does that, too.

**Dave Jones:** Yeah, yeah. There's a whole bunch of them.

**Chris Gammell:** Basically, for the bottom of the range of the tools.

**Dave Jones:** I have AVR ones back in the day, I think. Yeah, maybe that was a third-party one. I remember using that. And I had to fit it into the free code limit because I was too tight-ass to, you know. Yeah. I just, yeah. But that's the thing. There is no limit here. There's no size limit. There's no memory limits. There's no part limitations, right? You can use every single part. It's all free. It's just the optimization. So I don't. I'm not buying the complaints or that. I understand where people are coming from. And if it is a really huge problem for you, well, don't use microchip. Okay. But I think it's blown out of proportion.

**Chris Gammell:** So I think the other thing about what Steve was saying is Steve also said, I believe, correct me if I'm wrong. Steve said in the show, we think we should charge because otherwise it gets left behind.

**Dave Jones:** It becomes a cost center. The term he used is it becomes a cost center.

**Chris Gammell:** I don't think that's true, though. Like this is, it's a.

**Dave Jones:** No, I have no reason to doubt it.

**Chris Gammell:** It's a marketing tool for other people as well, right? Like all of these things are marketing tools, right? The reason they do it is because they want you. They want to make the developer experience easier to use their product, whether they achieve it, arguable. But they are trying to make it so that you can. They want you to get to Blinky as fast as possible. And God bless their hearts. They're trying, right? I mean, like, and that is that is a marketing cost. And Steve's right. It is a cost center. But I don't agree with the fact that, like, we have to charge in order to do that. Really, it's a. No, we have to be at a organizational. We have to take a stand in an organization that this is something we prioritize. And he said, like, oh, well, managers are going to, like, trim the fat and that's going to get rid of your tools. But that's a decision internally. And, like, it is saying that we have the charge to do this is I feel like that's a false.

**Dave Jones:** Yeah, but when a new CEO comes in, when a new manager comes in, what are they going to do? They are going to cut things. That is what that is why they were hired. You don't change CEOs. You don't change managers. Yeah, well. Sure, but just charging board is not going to stop it. You know what I mean?

**Chris Gammell:** Like, a hard charging CEO that's just charged with just just there to, like, cut costs. $49 a month or whatever is not going to change your tune either, right? It's not going to pay.

**Dave Jones:** But if that cost center is making a profit. They're not going to cut it, right? They have a harder decision cutting it. It's also a mindset thing. Maybe a harder decision. Right?

**Chris Gammell:** I don't agree with that. Steve Sange has been doing this for 31 years. He's the CEO of Microsoft. I am Chris, the lowly EE. Exactly. I don't agree with it, but it doesn't mean I'm right. You know, like, so that's, I'm just saying, I don't agree with that. I think it is organizational. That's what I said on the forum.

**Dave Jones:** I said, look, I, you know, he's been doing this shit for 31 years, right? He knows a tad more than us about it, right? He knows a tad more than big company politics.

**Chris Gammell:** I don't agree with that generally.

**Dave Jones:** Okay, fine. Well, I think it's also a mindset issue, right? If you have the mindset issue that, oh, we're just going to, like, leave it up to the open source community to do GCC, right? Even though we're doing our own tools, but if you don't keep up that seriousness, you know, that gets into your mindset and then you sort of, like, drift towards the point where, well, you go, well, let's just not bother putting much effort into our own tools anymore. Let's just leave it up to the open source community. And, you know, like, that's where it drifts, right?

**Chris Gammell:** Some of this does touch near and dear to my heart, right? So, like, this is basically, so developer relations is what I do currently and what I've done in the past. And, like, one of the problems is, like, where do you stick someone like me in an organization? It's actually, there's many, many blog articles about it because I cost money to go to conferences and I cost money to do all the stuff that I do, fine, whatever. But me and people that are-

**Dave Jones:** Hey, everyone at home, Chris is talking himself out of a job here. He'll be on it next week.

**Chris Gammell:** Hey, you know what? I am very good at firmware now, Dave. All right. Okay. Right. Yeah. But I think it's legitimate because at my old job when I was in developer relations as part of marketing, like, then it becomes, again, it becomes a cost center and it's, like, it's tougher to justify, right? And it's, like, I think the same thing goes with, like, so, like, what we're talking about here broadly is, like, it's often referred to as developer experience. And it's usually people much smarter than me that can actually write tools. So, like, VS Code plugins and stuff like that. Where do you stick them? Do you stick them in the engineering org? Do you stick them in the sales org because it helps make sales? Do you stick them in the marketing org because it helps promote how easy it is to use your parts? Yeah. I think it's really important to basically wall off that developer experience thing and commit to it, like you were saying, and say, like, look, this is important to our company.

**Dave Jones:** That's right.

**Speaker ?:** It's about seriousness.

**Dave Jones:** That's right. It's about seriousness. Yeah. And I think at least trying to charge some money for it is your way of signaling to everyone that we're bloody serious about this.

**Chris Gammell:** Right? I disagree with that because of the norms only. Okay. Fine. That's a valid point, but I think the norms don't match that. But I see what you're saying about the seriousness. That part I can get behind at least.

**Dave Jones:** That is why I'm not going to be critical of it. It is what it is. And if they want to do that, I don't really have a problem with it.

**Chris Gammell:** Well, Steve saying you can do whatever he wants at this point. Like we said, 31 years.

**Dave Jones:** This is why I don't see what the big problem is. I just don't get all the uproar about it. On the internet, Dave.

**Chris Gammell:** I don't know if you know about this. Yeah, because people want free shit. Okay, man.

**Dave Jones:** Everyone else is doing free shit. So Microsoft should do free shit. They are doing free shit. Microsoft.

**Chris Gammell:** It's all free. Microsoft is not doing free. Well, they do some free stuff.

**Dave Jones:** Dude, it's all free. Go and use the compilers. They're all free. Right? Yeah. It's only if you want some whiz-bang optimized setting on the compiler that that's what you pay for.

**Dave Jones:** Yeah.

**Dave Jones:** All right. Well. All right.

**Dave Jones:** Cool.

**Dave Jones:** Well, I don't care if my code is 7K or 8K. You know?

**Chris Gammell:** Send complaints to HR at eevblog.com and that will go into the appropriate spam inbox.

**Dave Jones:** I don't get it. Anyway, it's funny to see people. Yep. Yep.

**Chris Gammell:** Overall, really great interview. I enjoyed hearing Steve. He was great. Glad he came on.

**Speaker ?:** So.

**Chris Gammell:** Yeah. That was great.

**Dave Jones:** We were very lucky to get the hour because we had to slot into his calendar. So. Yep.

**Speaker ?:** Yep.

**Chris Gammell:** Busy guy.

**Dave Jones:** Yep. And we saved the audio just.

**Chris Gammell:** Yes.

**Dave Jones:** I'm recording a backup this time.

**Chris Gammell:** Yeah. We started. This week.

**Dave Jones:** Yep. I'm recording. Yeah.

**Dave Jones:** I'm backing up recordings.

**Dave Jones:** Yeah.

**Dave Jones:** Zencaster. I don't know. Yep. Yep.

**Dave Jones:** Works 99.9% of the time. And then the one big show that you do, the critical one that you really want. And they. Yeah. Screws up. Yeah. Yep.

**Dave Jones:** Yeah. Well.

**Dave Jones:** Anyway.

**Chris Gammell:** Let's do.

**Dave Jones:** Are we all calmed down now? About. I think so. I think so. All right.

**Chris Gammell:** Breathe in. Let's switch into announcements real quick. Uh. KaiCon or Kikon. Whatever your. Whatever your chosen flavor is. Is happening. Dude.

**Dave Jones:** It's Kik. It's Kikad. We've been through this. You've even admitted it.

**Chris Gammell:** September. September 9th and 10th.

**Dave Jones:** Are you still saying. KaiKad.

**Chris Gammell:** A Carunia. A Carunia Spain. I'm just going to ignore Dave here. Uh. Luckily I'm the editor this week. So I could just. I could just blank him out. Right. Um. A Carunia Spain. Which is in the northern. Northwest corner of Spain. Uh. So. Yeah. There will be a conference. It's actually being run. By the services corporation. That's. Seth and Wayne. The. Two of the.

**Dave Jones:** Oh right. As in the. Kikad services.

**Chris Gammell:** That's right.

**Dave Jones:** Division. I guess. Is that a. Yeah. Yeah. That's right. Yeah. I mean corporation.

**Chris Gammell:** Yeah. They're a company. So.

**Speaker ?:** Yep. Yep.

**Chris Gammell:** Um. So yeah. Uh. There is a talk proposal now. And uh. That'll be September 9th and 10th. I will not be there. Personally. Um. But I will be. At embedded open source summit. June. 26th. I think about a month from now. Let me look at my calendar. June 26th to the 30th. In Prague. Checha.

**Dave Jones:** Oh.

**Chris Gammell:** Yeah. Nice. I've never been to Prague before.

**Dave Jones:** Oh yeah. I've heard it's nice. Yeah.

**Chris Gammell:** Yeah. It's supposed to be very great. So. Um. Yeah. So that'll be. That's like a combo of like the Zephyr developer summit. And like automotive Linux. And a bunch of other stuff. So. Right. Yep. Cool. Nice. Yeah. That's it on the. Uh. Conference front. But in the automotive front. Since we're talking about automotive there. Um. I had a bit of a. A fun. A fun interaction. Um. Tell us. So I post. I posted our. Uh. Noisy can bus. Yes. Uh. Uh. Episode from. I think two episodes ago. And uh. Someone wrote back to me on. On Mastodon. And said. Never in my 30 years. Of working on can bus. Have I ever heard so many wrong things. And I'm like. Who. I'm like. Who is this joker. And then like. There was an article. That I was ready to talk about. Like. That following. The following week. When we were supposed to record. About this awesome thing. We're about to mention. With the can bus. And I was going to mention it. I was like. Oh my god. He wrote that article. I was like. Ah. Crap. Ah. Anyways. Uh.

**Dave Jones:** I don't even remember. What we said about can. I don't even remember. We said.

**Chris Gammell:** Because we were talking about. Like. I mentioned that. Like. I was starting to work on some can stuff. And just. Can's really noisy. And Ken told me I'm wrong. And then he. Came on the show. And told me. How wrong I am. And in a very. Very nice way. He's. Uh. And so. Ken will be the episode next week. So. People can hear it next week. Little teaser there. Uh. And. This is the article. That I was talking about. This was going on the internet. But it's basically someone who. Uh. One of his friends. Ian. Basically had seen that his headlight had fallen off. Or like. That someone had like. Peeled away the stuff. From his. His headlight.

**Dave Jones:** Oh. Okay. Like a. Like a rubber seal or something.

**Chris Gammell:** Yeah. The paneling. The plastic panel. Like just. Right. The left headlight. And he's like. What is going on here? And like. Did somebody hit me? But it was like. On the. The side of the street. So. It wasn't. Right. It was like. Something about it was like. It wouldn't have been someone hitting him. And then. He kept noticing. Kept noticing it. And then he got a notice. From his car. That it had been stolen. Uh. Because there was some.

**Dave Jones:** Right. Because everything's monitored. And everything's.

**Chris Gammell:** Right. So apparently. Car thieves can now. Uh. Buy these devices. On the black market. And. Uh. They look like bluetooth speakers. But they're actually. Can hacking devices. That basically send a signal. To your engine. That say. Hey. You've just been unlocked. And that's how they steal cars now.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah. It's. First off. Fantastic article. Yeah. I was going to mention anyways. Hang on.

**Dave Jones:** How do they physically connect to it though?

**Chris Gammell:** So. They. They peel back the. The paneling.

**Dave Jones:** Oh. Okay. All right. So they go outside. Oh. Okay. Right. So they go through a headlight. Or they go through a. So the headlights are all.

**Chris Gammell:** Can devices now. Right. They used to just be. Can devices. Yeah. They used to just be like. A light bulb. But now it's got all these crazy. Microcontrollers in there. Whatever. Yeah. To have different modes.

**Speaker ?:** And.

**Dave Jones:** They've got a micro in every single headlight. Everything.

**Chris Gammell:** Yeah. Yeah. So we talk about all this stuff next week. Right. But. First off. So people should be prepared. Go and read this article. I'm trying to find it now. In our. Our thing. Here. Is it so long ago? I didn't. I didn't post it. Oh. I feel stupid. Yeah.

**Dave Jones:** I was just thinking that the other day. Like. How does someone steal my. Ionic EV? How do they steal it? Like. You know. You would have to have some serious hacking tools.

**Dave Jones:** You know. To sort of. Yeah.

**Chris Gammell:** So I mean. So basically. There's a message. Like a canned message. So I think they. They. Again. This is a. A question for the next episode. That I. Well. I'm not. I've already recorded it. When we're recording this one. So. I can't ask any of the questions. You're about to ask me. But. I think. There's like. A blocking signal. Based on can bus. That. That Ken talks about. He wouldn't tell me. Exactly what it was. Because he doesn't want to make it easier. For people to make these devices. And sell them. For like $5,000. Yeah. Or more. Oh. Okay. So they're really expensive. They're really expensive. Yeah. Okay. Wow. Bluetooth. No. Man. I don't know where this is. Anyways. I'll find it.

**Dave Jones:** That's some serious investment. On the part of the. Criminal. It's almost. Hats off to them. They've invested in the tools. Required. That's right. That's right. You know. I've got to tip my hat actually.

**Chris Gammell:** I'm improving my career.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** Yeah. Here's the video. Here's the link in the chat, Dave. But. I certainly can't fault that. Yeah. So they. They're made for specific cars. They inject these. So basically they block other devices from transmitting. And then they just. Yeah. Blast this unlock message.

**Dave Jones:** Okay. So you can block the. But so you can take over the bus.

**Chris Gammell:** Yeah. So to speak.

**Dave Jones:** So there's some sort of command that goes. No. Hi. Yeah. I'm so mega important. Everyone else shut up and listen to me. I guess. You know. Guess what.

**Chris Gammell:** Guess what's. Guess what's inside this Bluetooth device.

**Dave Jones:** Yeah. One of those.

**Chris Gammell:** Pick 18.

**Dave Jones:** Oh. Pick. Pick 18. There you go.

**Chris Gammell:** Thanks, Steve Sangy.

**Dave Jones:** Nice.

**Chris Gammell:** Yeah. Anyways. Fantastic article. Really, really good stuff. So. Okay. Yes.

**Dave Jones:** This looks comprehensive. Yeah. Yeah. Yeah. I was going to say like there. I assume that every car would be different. So any like universal hacking tool would have to be programmed with. You know, a hundred different models or something.

**Chris Gammell:** Yes. Would that be right? And we do talk about that too. Because. So that's another thing that. So when in the art. In the. I bring this up again next week. But this is weird. This is like back to the future for me. But. You know. I brought up as well that like the. The reason it looks so noisy is most of the time you don't. You don't have the decoding keys for different manufacturers. So like you're saying. It's different car to car. Like it's different. Not just for. What would unlock each car. But also what. What like the. What the engines. Different readouts are. You know. Like how they actually. Bit pack. Yeah. Yeah.

**Dave Jones:** Yeah. Totally. And they'll all use different smart keys. And they'll all use different. You know. Sure. Sure. Yeah. Yep.

**Chris Gammell:** Yeah. So great article. I'd say read it before next week. And then. Ken will be on. And it was really good show. So.

**Dave Jones:** Cool. Excited. All right. About. That's that. Yeah. That sounds good. All right. Yeah.

**Chris Gammell:** So what else should we talk about. Now that I've. Spoiled next week.

**Dave Jones:** All right. Well. What's on the list. Do we have anything on the list.

**Chris Gammell:** I have no idea. Actually. I have something that's not on the list. I was thinking about.

**Dave Jones:** No. No. Hang on.

**Chris Gammell:** Nope.

**Dave Jones:** I can. I can. Put in. I will put a link. To it. Hang on. Let me get the link. But a former guest of the show. Vincent. Himpy. Who's done. The. Oh. The. Three hour. What. Three hour show. Oh yeah.

**Chris Gammell:** Our longest show today.

**Dave Jones:** Our longest show today. Which we don't do anymore. Because we do try to limit to them. Oh my God. Because we know that.

**Chris Gammell:** And it was like two in the morning. My time too. It was like insanely late. Right. Back when I was in Cleveland. That was a long time ago. Yep.

**Dave Jones:** And. He. He has left. Tesla. He was a former. He was the former head. PCB designer at Tesla. Yeah. Spent eight years there. And then he went to a. A space company. Who shall remain. Nameless. And then. He's now looking for. A gig. So if you want to hire. The former head. Of. PCB designer. Tesla. Come on man. Yeah. He put a job ad. On the EV blog forum. He put a. He put a. Don't give him free job ads. You know how much that's worth.

**Chris Gammell:** This is free advertising.

**Dave Jones:** We should be paying for this shit. Yeah. He should be paying. Charging for this shit. Yeah. I mean.

**Chris Gammell:** I guess he did give us three hours of his time. So we'll. Yeah. It's true. We'll put it against his tab.

**Dave Jones:** Yep. All right. I will find a link. Able for the link.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** Okay.

**Chris Gammell:** I was thinking about. What are. What are the first thing. So like. I was thinking about reference designs. And like. I was rebooting up. An old reference design. Like a. Red. Uh. Dev board basically. And like all of the things that you get on a dev board. And then like. Okay. So now I go and. I go and put that chip. I've decided on that chip. That I've tried out the dev board. I've tried all of these different things. I've. Talked to my firmware engineer. I've talked to everybody. Everybody's cool with it. I've started the design. And then. What are some of the things. I was thinking about some of the things that like. My past jobs have been. And probably what other people would be. But like. What are the optimizations that you have to do. Once you have decided. And maybe. It's also part of the deciding process. As well. I suppose. Of like. What chips to do. And like. What. What are you then. Optimizing for. So like. Power. Power. Especially if you're on battery. Cost. If you're still on the chip.

**Dave Jones:** I've done a recent video on this. This would be all part of your selection process. You don't go. You usually don't go. Well. I'm going to. Choose a microchip part. And then. Figure out the lowest power micro. In the microchip. Well. Well you might. Some people might. You might. Because they have the tools. The experience. Or that is the company verified. Microcontroller. Right. And then you have to live within the constraints of. You know. Oh. I've got to use this brain. Right.

**Chris Gammell:** It's part of. It's somewhere between. The dev. Buying the dev board. And you know. Doing the layout. Somewhere in there. Yeah. But even past that too. Right. You might have other optimization through there. But I was just thinking about. Like all of the optimization exercises. That you do have to do there. Like you said. Yeah. Part choice is. Is a huge one. But then. Thinking about. That also. That bleeds into power. And. Battery. Or sorry. Power and cost. Yeah. There's cost. I was also thinking about. There's availability.

**Dave Jones:** There's package.

**Chris Gammell:** I was. I was thinking about. Data. Data. Usage. That's something that might be a little bit later. I suppose. Maybe in the firmware stage. I was thinking about. What do you mean data usage? Like if you're a cellular device. You know. I've been doing a lot of cellular devices. Oh.

**Chris Gammell:** Oh. Right. Okay. So that's like an optimization as well. But other. Other like very common ones you'd say. So you're in space. I guess space is a good one. Right. Because that's often. And.

**Dave Jones:** Well then you would go. Do I have. Radiation. Hardened parts. Do I have. Extreme temperature rated parts. For example.

**Chris Gammell:** That's a good one. You know. Yeah. Yeah. Yeah.

**Dave Jones:** Because not all manufacturers offer extreme in industrial or larger. Yeah. You know. Temp ranges. So.

**Chris Gammell:** Yeah. That's a good one. I would say. I was thinking like Keithley days as well. Like. Like. Spexmanship type stuff. So like. Can I hit my. I guess in that case it was analog specs. As well. Right. That was. Oh yeah. Yeah.

**Dave Jones:** If you need a built in analog to digital converter. Or DAC. Or something like that. Is it one of those little crappy ones. That doesn't meet the. You know. That has crap specs. Or is it you know. Fairly decent.

**Chris Gammell:** Right. Are you building your own. Right. That's. Right. Stuff test equipment does. I don't know. I was just thinking about like. What. As we enter this age of. Computers. Computers. Smart. I don't want to say the words. As we enter this age of. Fake. Smartness. Is that good? We'll call it FS. Instead of AI.

**Dave Jones:** Yeah. Because there's nothing really intelligent about. Artificial intelligence.

**Chris Gammell:** It's. So like. Where are the value props of the. You know. Like. Especially as like. Electronics. Become more accessible. Which is good. We. That's what we want. So then. The optimizations. Are the things that. People are really getting paid for. Right. So like. An analog engineer. Is getting paid to get that extra. You know. Effective bit. Out of the measurement. Yeah. Right. You know. Circuit. All the way through the thing. And the. The engineer. At the toy company. Is getting paid to. Take another cent off the bomb. Because you multiply it by all the devices. And it's like a huge savings. Right. So like. What are the people. Getting paid. Well the optimizations. Are what people are ultimately getting paid for. As engineers. I think. Because the ones that aren't doing that. Specialized knowledge. I think. Are either going to. Maybe there'll be some AI tools. Fine. But probably more likely. You know. Just offshoring is more. Likely. You can just go to a. Any. Generical. Dev. Dev house. And just. Be like. I just need this thing. That is a bluetooth. Speaker. Okay. No big deal. Right. Yeah. We know how to do that. You know. And then it's just a race to the bottom. So the. The engineers. The optimization piece. Is really. That's what you're paying for. I think.

**Dave Jones:** You are. But what's changed. Nothing's changed in the industry. Everything's still the same. This. This has been around. Since day zero. You know.

**Chris Gammell:** I'd say the accessibility of. Offshoring is. Increasing. Increasingly easy.

**Dave Jones:** Also. The accessibility of. This kind of stuff that you work on. Like if you want to do something complex. Like you know. Talk to a cellular network. And you know. Do all that sort of jazz. Right. If you did that 10 years. If you wanted to do that 10 years ago. That's right.

**Chris Gammell:** You were in a world of hurt. Oh you're in a world of hurt. That's right. Yeah. You're. You're basically. You're. You're trying to get a hold of. Qualcomm. And you know. Yeah. Right. I guess there was modems back then too. But like you're. Yeah. You're in AT command sets. You're not. You know. More and more. So like. SC has a new cellular. Integrated cellular part as well. Right. Which is crazy.

**Dave Jones:** Well I can just give you an example. With my. Unfinished. Micro supply. Right. It was. With. With the USB. C. Power delivery. Standard. Right. The. The power delivery standard. Back when we started that project. That was a difficult pain in the ass. Right. Now it's just getting easier and easier and easier to integrate power delivery into your products. You can just buy a little 8 pin Asian micro that just does this power delivery for you. And it's all handled. Right. Whereas we. We had to use. A. 32K. ST. Micro part. Just to handle the. You know. The power delivery thing. And then the. And then the library for that. The power delivery library.

**Speaker ?:** Yeah.

**Dave Jones:** From ST. Was like 30K or something. Right. It was enormous.

**Chris Gammell:** Right.

**Dave Jones:** And it was just. Oh my God.

**Chris Gammell:** So I would say. Bleeding edge. In that case that would be just like general bleeding edge. Now that. You guys were not bleeding edge. But you were ahead of the curve.

**Dave Jones:** We were probably a year or two ahead of the easy stuff. Totally. The easy stuff now. You can buy a chip. You don't even need to program it. It just has pins on it. And you can just strap one of those pins. And it gives you a certain power delivery standard. It just does all the negotiation. It's all pre-programmed.

**Speaker ?:** It does everything for you.

**Dave Jones:** Totally. Does everything for you.

**Chris Gammell:** Right. Right. So how about this pre. Pre. Easily available silicon. Or like a function in silicon. Or something like that. Right. So like. One of the examples I always give in that case. Is like. You know how you can just buy. An off the shelf thermocouple chip these days. And that's like really good. Like really really good. And then I like point at the. The old Jim Williams app note. Where it's like. Like you can just buy the silicon. Right. Equivalent. Of what. Yeah. Of what they did. Yeah. Yeah. Jim Williams did. Right. Exactly. And it's like. Exactly. Maybe it's a little bit better. But even still like. Or you could say like. That extra. You know. Maybe the Jim Williams thing. Was still a little bit better. Than what you could buy today. But the leap from. A piece of silicon. And just plopping it down on a board. And actually doing all the stuff. That Jim does in. App note 18. Or whatever it is.

**Dave Jones:** Yeah.

**Chris Gammell:** It's. It's significant. It's like. It's a step change. In terms of like. In terms of. Needs and capabilities. Whatever. So like. That's definitely an optimization as well.

**Dave Jones:** It is. This is just. The. Continuation. Of something that's been going for 50 years. Which is application specific. ICs. Right. If. If in the early. If in the mid 70s. Or something. Right. You wanted to do a. An analog. VU bar graph. Right. If you want to do an analog. VU bar graph. Right. There was a lot of stuff. A lot of circuitry. You know. You're designing an audio thing. And it's got to have a. A graphic analyzer. You know. Or it's got to have a sound level meter. Lead bar graph. Fancy. Pancy. Right.

**Dave Jones:** Yeah.

**Dave Jones:** And then the LM3914 and 3915 came along. Right. And the 3914 would do linear. The 3915 would do log. I think I have that correctly. If I'm remembering from 30 years. Or 40 years ago. You know.

**Chris Gammell:** His brain is aging folks. He's.

**Dave Jones:** I'm pretty right. I reckon I'm right.

**Chris Gammell:** LM. I bet you're right too. No. I bet. I bet you're right. I bet you're right.

**Dave Jones:** That is memory test live. LM3914 is the analog. And LM3915. Is the log. Is the log version. I think. Anyway.

**Chris Gammell:** Take that chat. GPT.

**Dave Jones:** Bastards. Yeah. Like. You know. And it's just a continuation of all these application specific. I see. This is why DigiKey and Mouser and all the others have. You know. Half a million different devices. Because there's an application specific part for everything. They just keep coming out with it. This is why back in the days of Maxim. Right. Maxim had to release a new data book every. Two months or something. Because. That's right. They came out with 200 new application specific chips.

**Dave Jones:** Yep.

**Dave Jones:** Right. It's just. Yeah.

**Dave Jones:** It's crazy.

**Dave Jones:** Yep. And so it's just a continuation of that. I don't see anything different. Sorry. It's just. It's been around forever.

**Chris Gammell:** No. No. I mean. You're right. It is no different. I'm just saying. What is it today? Right. So. So. Where are the lines today? Right. So. So another example. So I'm staring at my desk. Right. So right now. A lot of like. Machine learning. Tiny models. Tiny ML. Machine learning. Tiny machine learning is like a thing that you can go and like train a model.

**Dave Jones:** Right. Yeah. Yeah. For a very specific. Robot task or something.

**Chris Gammell:** Exactly. Right. Right. Right.

**Dave Jones:** Or.

**Chris Gammell:** What you can do is you can go and buy. So I got to meet Pete. Worden. The guy from useful sensors. And they sell this thing called the person sensor. And it's a camera. And it's a chip on the back. And it's got I squared C output. And it just spits out whether there's a person in the frame or not. Yeah. And I'm like. Yes. You're right. That is what I need.

**Dave Jones:** That's exactly what you want. Yeah.

**Chris Gammell:** Yeah. Yeah. So. That'll be in a future design of mine. I'm excited about that. But like. That's the same thing. Where it's like. Yeah. That 30 years ago. Would. Would have been.

**Dave Jones:** Oh. That was an entire design team. Years of work. It's a PhD. Yeah. Yeah.

**Chris Gammell:** And multiple PhDs. And whatever. Whatever. 10 years ago. It's still difficult. But becoming more accessible. But today. It's buy a person sensor. And stick it on your product. It's got a quick header on it. It's like. It's super simple. Like. That's amazing. Well.

**Dave Jones:** I can remember back in 1994. When I worked at Keycorp. It was at 95. Right. We worked on. We had a box. That would convert. A computer's. VGA output. To an LCD screen. Right. So. People take. And take it for granted. These days. That you get. You buy. Your. LCD monitor. Right. And it has a. VGA input. And everything else. Right. They just take it for granted. Well. Back then. The box.

**Chris Gammell:** These days. It's kind of tough to find VGA input. Well. Yeah.

**Dave Jones:** But you know what I mean. Right. And. And. The box to do it. Was enormous. It was the size of a pizza box. So we actually called it the pizza box. Because it was physically the size of a pizza box. Massive board. Had. You know. Chock full. Of. You know. It had like a hundred chips on the damn thing. Just to convert. 640 by 480 VGA. Into drive an LCD. Yeah. Right. Just to sample that. Low gaff. And re. And re-encode it. And drive a. You know. A parallel LCD. Back then. Right. Totally. It was like. Yeah. Whereas now. It's a single chip. Now it's just a single chip. You just buy it. And there's little converter boards that just do it. And you know. Like. Yeah.

**Dave Jones:** Totally.

**Dave Jones:** Yeah. It's nothing. Yeah. Whereas we were. We were probably like two years too early on that. Right. That was the early. Like. You know. A few years after that. It was like. Well. Everyone's doing this now. To his. You know. Wind bond. Or somebody did a chip to. Yeah. Just. You know. Just do the whole thing. Right.

**Chris Gammell:** Yeah. I just see it. I didn't put it on. Maybe it was on the list. I don't know.

**Dave Jones:** Don't be ahead of the curve people. You guys. Just wait a couple of years.

**Chris Gammell:** That's the thing. If you are ahead of the curve. That's when you get paid. That's what I mean. Right. Okay. Being ahead of the curve. That's when you get paid. But I think what happens then. Is on the other side. There is another side of the curve as well. Where once it falls out of favor. And so this is what's happening now as well. I don't think it was on our list. But I saw that the. The chipsets. That go into car radios. No longer have AM tuning in it. And so. Right. Okay. You can no longer get AM radio. In a lot of cars. And it's like. So now there's going to be a secondary market. For either like devices. AM chips. Or. AM chips. Right. Because there are still AM transmitters.

**Dave Jones:** Was it the AM 510? Am I. No. I've got that wrong. What was the AM chip. I just think about.

**Chris Gammell:** There's a bunch of like cheapo AM FM. You know. Like all in once. You know. That's just basically. Again. You plop it on your board. Antenna input. You know. Audio output. Sort of thing. And I think even it's like PCM. Or like I2S.

**Dave Jones:** The MK484. Is one of them. It's an AM radio receiver. In a TO92 package.

**Chris Gammell:** Oh. I think. I think they're a little past that. But.

**Dave Jones:** Anyway. There it is. 80 cents at Jaycar. Nice. The MK48 AM radio receiver. Literally in a three pin TO220. Right. Sorry. TO92 package. That's just brilliant. That's great. Chip of the week.

**Dave Jones:** It's chip of the week. Yeah. Sure.

**Chris Gammell:** stable operation operates down to 1.1 volts. You can operate from a single bloody cell.

**Chris Gammell:** Who would ever go that low? Who would ever go that low? It doesn't make any sense.

**Chris Gammell:** Man. Right.

**Chris Gammell:** Well we got a little off from where I was figuring we'd go with this.

**Speaker ?:** But.

**Chris Gammell:** You think? Yeah. Yeah. I'm curious. Like. If people think there's other optimizations out there. I'm just generally curious about this. Because. Again. I. I've been building. I've been building cellular stuff. And I think about like. Most people get a cellular thing on the bench. And they're like. Okay. I got to get the data cost down. I got to get the power down. And I've got to get the. What was the third thing? The cost down. And the cost down is pretty tough. But. Because. Cell modems are generally pretty expensive. But you could switch modems. And. But that's going to keep dropping. Right. I mean. That's. That's. That's. That's part of. Part of what it is. So you could try and. Get ahead of the curve. And maybe do chip down yourself. That's. So like. You think about that sort of thing too. Right. If you. Have a cell modem. Most of the time. You're buying a module. That's. It's got a big metal can on it. Somebody else. Has done all the testing. You could. Get ahead of the curve a little bit. By. Doing chip down. Doing all your RF testing. If you. If you had enough volume. It might make a lot of sense. But most people. Aren't willing to do that sort of thing. But that's how you get ahead of the curve. On the cost basis. Sometimes.

**Dave Jones:** Right. Yep.

**Chris Gammell:** All right. That's all for me.

**Dave Jones:** Yeah. No. Sorry. It's.

**Chris Gammell:** I mean. You're right. It's not that different. But I'm just saying. I've been thinking about it. So that's why I brought it up. Okay.

**Dave Jones:** Fair enough.

**Chris Gammell:** What have you been thinking about. Man.

**Dave Jones:** Not much.

**Chris Gammell:** Yeah. Right. Yeah. Sorry. That's what happens folks. These YouTubers. They're just kicking back. Enjoying their. Their profits.

**Chris Gammell:** Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Hanging out in forums.

**Dave Jones:** Yep. Yep. Ah. Boy. Come on. There's got to be something on the list.

**Chris Gammell:** Oh. There's definitely stuff on the list. Let's see. Oh. This one's. Good as well. Powering a Nixie tube. So. From a USB. With a 10 cent. Risk five. This is. Charles Lohr. CN Lohr. On YouTube. Nice. Amazing video. Wait. No. Sorry. This one. Is this. Yeah. This is Charles. Yeah. So basically. He actually references your video. As a.

**Dave Jones:** Oh. Okay. Yeah. Because I did a whole series. On doing the. Designing the. Hixi tube. Counter. Oh. He's actually talking about the.

**Chris Gammell:** CH32 V. 003. Oh.

**Dave Jones:** Okay. Oh. That one. Okay. Well. Yeah. Basically.

**Chris Gammell:** Where Dave went through the dev tools. Yeah. But this is actually another good example. That we're talking about there. So. You and I bought this chip. And you went and did the. The off the shelf tools. And I'm like. I'm going to wait around for someone else to write tools. Right. And Charles now has a tool set that he built around this.

**Chris Gammell:** Nice. If you want. You can go and do. What's it called? CH32 V. 003. Fun. There's now like. This library that helps you to develop for these. Ten cent. RISC-V chips. So that's something people can go check out. Yep. And the. You know. The build's really awesome. And spoiler.

**Dave Jones:** Are they available in volume now? Because there were. When I did my video. They were hard to get. Right. Yeah. That'll be hard.

**Chris Gammell:** I've seen mixed reports. Nothing. Okay. All right. Yeah. Spoiler. Charles will also be on the show soon. Oh. Excellent.

**Dave Jones:** Well. We've had two former guests. We've had Ben Jordan. Oh. You're talking about the list right now.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** And they. And Eric as well.

**Chris Gammell:** Eric's also been on the show. Oh. Yes. Yes.

**Dave Jones:** Yes. So I was. Yeah. They've done a. They didn't streamed interview talk. I was actually invited to a vintage computer conference in San Jose. Which is coming up. Oh. Really? In August. But yeah. I don't think I'm going to be able to make it. So. Yep.

**Chris Gammell:** What's the. Yeah. VCF. There's.

**Speaker ?:** There's.

**Chris Gammell:** There's. There's. There's. There's. There's. There's. There's.

**Chris Gammell:** There's.

**Chris Gammell:** There's. There's. There's. There's. There's. There's. There's. I don't know what the big one is though. I think. Yeah. East is the one that I usually hear about in Virginia or something.

**Dave Jones:** Anyway. There's one in San Jose at the. Computer History Museum. Oh. That's fun. Yep. August 8th or something like that. Yeah. It'd be nice to go to.

**Chris Gammell:** When's the next time Dave is touching down on American soil though? Oh. I heard you're not allowed from the State Department. Is that true?

**Dave Jones:** No. I'm allowed. I can come in.

**Chris Gammell:** Are you sure?

**Dave Jones:** Yep. Are you sure? Yep.

**Chris Gammell:** Moment check with your local embassy. Anyway.

**Dave Jones:** They've already got me fingerprinted. The bastards.

**Chris Gammell:** Yeah. And everybody. It sucks. Everybody who comes in the country now. It's crazy.

**Dave Jones:** It was that way 20 years ago. I was getting. Was it? Yeah. I was getting fingerprinted 20 years ago going to the States.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Come on, man. Yeah. It's been around a long time. Jeez.

**Chris Gammell:** Disreputable Aussies.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Yeah. What's new in the forum?

**Dave Jones:** Oh, well, I can. Look, I can call up the new reply. Oh, no. I can call up the unread replies since last post. And people are still talking about pick and place machines. They're still talking about the neodens. They're still talking about hacking the Rigol scopes. They're still talking about, you know.

**Chris Gammell:** Same old, same old. Yep. Yeah.

**Dave Jones:** Yep. Yep. I think that has been getting a lot of views for me lately. In fact, it's standing out. It's like just cheap ass tools. Oh, you mentioned this.

**Chris Gammell:** Yeah. Yeah, yeah, yeah. Yeah. And you said you were going to do kind of cheap stuff over other stuff, right?

**Dave Jones:** No, I didn't necessarily say that. But that's where the views are. I mean, if I look at my last 20 videos, the largest number of views have been just actually reviewing cheap stuff. You know? It's like...

**Chris Gammell:** What was the last... What's the last cheap thing you did? I... Oh, it was a... Oh, it was the scope meter thing, right?

**Dave Jones:** The Zotek. It was the Zotek ZT702S oscilloscope multi-meter.

**Chris Gammell:** I mean, I think that's kind of interesting, too, because that's like an optimization.

**Dave Jones:** Yeah, it's like, you know, it's only available for 80 bucks, I think, something like that. Yeah. You might even be able to get it cheaper than that.

**Chris Gammell:** But it had a bunch of weird stuff, like weird issues. Oh, yeah, but nothing... Not necessarily showstoppers. I just remember... I was watching that. Oh, that's right. Because I was watching that, and I was thinking about the first round of contextual electronics I did. And I told people to buy this, like, breadboard scope, which was a total bust, built on top of, like, an Atmega.

**Dave Jones:** Oh, yeah, I remember that. Yeah, yeah, yeah.

**Chris Gammell:** Oh, what a... I mean... Right. They tried, but it was, you know, it was like maybe 20 kilohertz bandwidth. It was just like...

**Dave Jones:** I get that all the time. Like, should I buy this little $50 pocket oscilloscope? And I'm going, just no.

**Chris Gammell:** No, just no. But I watched this thing, the review did, and, like, that would have been okay. You know, like, if you can get to a megahertz, and you can have multifunction like that, okay. You know, like, that's not bad. I don't know. It is tough at the bottom of the market, I think. And, you know, and, like... Sorry. There's another edit. All of the boards on my desk falling off. No, that's great. Cave it in. Yeah. You know, like, you and I are, you know, men of means. We are further along in our careers, and, you know, a $400 scope doesn't sound like a lot, right? It actually sounds kind of affordable. But it's... To a student, it's like, $400 scope? Are you serious? And I need other stuff, too? Like, yeah, no, it's like, it's tough to, like, put a whole lab together, especially when you're starting from scratch, you know?

**Speaker ?:** Yeah.

**Dave Jones:** Dude, I couldn't even give away oscilloscopes.

**Chris Gammell:** When?

**Dave Jones:** I did my keysight draw, right? Oh. And I gave away five scopes. Only three people actually replied. Other two people didn't want it. They didn't get back to me. It's like, what?

**Chris Gammell:** What? Seriously? Maybe they'll just don't check. You know what you should do? You should start asking for mobile numbers instead of emails. I bet that would work. All right, yeah. I bet that would have 100% hit rate. Right. Because it's, you know, Dave, kids these days, they just don't check their email, including myself. I stopped checking my email a lot, so.

**Dave Jones:** Anyway. Oh, unbelievable.

**Chris Gammell:** Two months from now, they're going to be like, oh, crap. I could add a free scope.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, God. Yeah. Anyway. That's tough. Yeah, that's tough. Yeah. I did discover a new fandom. I discovered. Because when you start talking about low-cost tools, oh, the fan. The lower-cost tool, the more rabid the fan base. Really? There has to be a name for this law. Dolphin thingy? No. Dolphin thingy? Have you seen the dolphin?

**Chris Gammell:** We'll come back to that. Okay.

**Dave Jones:** Oh, dolphin. No. Okay. No, no, no. I'm talking about.

**Chris Gammell:** The flipper. Flipper zero. Not dolphin.

**Dave Jones:** Oh, the flipper. I've got a flipper now.

**Chris Gammell:** You do. Okay. Yes. I've got a flipper zero. Yep. It's like. The dolphin is the logo. That's what it is. Okay. I'm not a total idiot. Yeah. Right.

**Dave Jones:** Anyway. Yeah. I don't see the attraction to it. It's like. I don't know. Like it couldn't even do any of my garage door keys. Because they're all rolling in code or whatever. Like it just can't do them. Right. Yeah. Okay. I think it's one of those things where it's cheap. Flip the petrol cap on a Tesla.

**Chris Gammell:** It's cheap enough. And then it's like.

**Dave Jones:** It's like 300 bucks. It's not cheap.

**Chris Gammell:** It's cheap enough. That's cheap enough. As a hacking device. That's cheap. Oh, yeah. No.

**Dave Jones:** It's cheap.

**Chris Gammell:** And then some stuff does work. But I think the thing is. Most people are not willing. You know. Like any kind of new vulnerability comes up. Or new things discovered. People then do patches for their equipment. And they're like. Okay. Well then. Basically. This is like the physical incarnation of like script kittying. You know. Yeah. So like. If I can't. You know. If you have to go program it yourself. That's tough. That's a tough thing. Yeah. Yeah. Yeah. Of course. That's an optimization. And like. Of course. But like. Yep. You know. But if you. If you could just download it. Then there are some things you could. That's like what people want to do. They want to buy it. And have this like. This magical hacking tool. Well. Sorry folks. You have to actually do work.

**Dave Jones:** It's not that magical. Yeah. Like. Like it's great. Like it can do some cool stuff. But you know. Like.

**Chris Gammell:** Well the hardware. Yeah. The hardware in it. Yeah. It's flexible. And that's what you really need. Yeah. But if you have to write that. This is like. I bought a hack RF. And I'm like. Oh yeah. I have to. I have to like. Know how to use this thing. You have to actually do stuff. You know. Like. You have to actually know how to use it. Yeah. Right. And then no limits of that. Like. Yeah. Okay. And then I actually have a use case. Where I'm not like. Doing research. Or trying to do. Right. Right. Right.

**Dave Jones:** Yeah. So you got to spend a lot of hours at it. Yeah. You don't. Yes. That's right. Count the time invested. Anyway. All right. So. Rabid fan base. Rabid fan base. Which increases. With. The drop in price.

**Dave Jones:** So it's an inverse relationship. Sure.

**Chris Gammell:** Sure. Rabid fan baseness. You have a specific example. Or do you have. Oh yeah. I got a specific example. Okay.

**Dave Jones:** I actually. I think. I don't know if this is the most recent one. I did. But the cheapest tool. I did. I did do it recently. Which is the. Fursi. HS01 USB portable. Soldering iron. Right. So I actually did a. Oh yeah. A review video of that. Right. It's like 30 bucks. And I thought this is pretty cool. It works. You know. It's 30 bucks. It's reasonable. Build quality. Everything else. Right. And then. Oh no. No. Entire comment section flooded. With. No. The pine 64. You've got to have the pine 64. So all of the TS 100 fanboys. And they were. I thought they were rabid. Right. They've all moved over to this pine 64. Which is like an open source. Version of the TS 100.

**Chris Gammell:** Yeah. And they. So they make. Pine 64 makes risk five chips. And like. And like. Beefy. Risk five chips. Like really. Significantly. Like. Yep. Serious stuff. All right. So. Anyway. Yeah.

**Dave Jones:** Yeah. Yeah. The pine 64. And. And they go. Don't you know. It's only 23 dollars. And it's the duck's guts. And it's like. Yeah. Okay. Dude. Thanks for telling me. You know. Like. And my. Yeah. Comment section was just flooded with it.

**Chris Gammell:** So is this the pine soul? Is that what you're really talking about?

**Dave Jones:** The pine soul. Sorry. Yes. Pine soul. Sorry. Yes. The company is pine 64. I think.

**Chris Gammell:** That's right.

**Dave Jones:** Yes.

**Chris Gammell:** Yes. So basically. They're just buying the exact same hardware. And then changing the chip. Or the board. It looks like the exact same hardware. That you reviewed.

**Dave Jones:** It's slightly different to the TS100. But it's similar. I don't know.

**Chris Gammell:** Oh. I went to. Not to the TS100. With that $30 one you're talking about. Oh. Right. Okay. It looks like the same tips. Like the same resistive tips that you're driving. No.

**Dave Jones:** It has different. Sorry. Does it have the same tips? I don't know.

**Chris Gammell:** I thought so. Yeah. Yeah.

**Dave Jones:** Yeah. Yes. Yes.

**Chris Gammell:** I did watch your video. Right. I can't always say. Yeah. No.

**Dave Jones:** I think they're the HAKO TS12 or whatever tips. Yeah.

**Chris Gammell:** So the Pine stuff is interesting. I mean like. And like I said. The board. I forget the boards I bought. But it was like. It was like the Buffalo. Pine H64. Oh man. They got a lot of.

**Dave Jones:** Yeah. They got wearable stuff. They got internet of things. They've got tablets. They got smartphones. They've got a Pine phone.

**Chris Gammell:** Right. They have a Raspberry Pi. Raspberry Pi.

**Dave Jones:** Pine book. They've got a laptop.

**Chris Gammell:** Tablets. What did I buy? Was this that? Maybe I'm thinking of a different thing. Anyway. I'm looking through there.

**Dave Jones:** Yeah. I'm just looking through their website now. And holy crap. Yeah. Yeah. Geez.

**Dave Jones:** I make a smartphone. Okay. Okay.

**Chris Gammell:** Yeah. Sure. Why not?

**Dave Jones:** Yeah.

**Chris Gammell:** What am I thinking of? Maybe I'm thinking of something completely different. This looks like this is tied to Rock 64 too. I don't know. All these names. I'm not a fan, Dave. Right. But it does look like they're putting a lot of, like, basically they're going into OEM shops and then just making a slightly better version that might be open source. So, like.

**Dave Jones:** Right.

**Chris Gammell:** You know, like the stuff that's in. You know, the molding is very similar to other products that you can get on the market in China. Right. You can just go and, like, line up with that sort of thing. But then customizing it on some level, ostensibly on the circuit boards.

**Dave Jones:** Anyway. Yeah. It's cool. Okay. Yeah. Fine. Pine Sol. Soldry nine of the week.

**Chris Gammell:** Pine Sol. I did. I did order something from the Pine Store. What the hell did I order?

**Dave Jones:** You did? You must have ordered, like, a. I'm searching my email. Single board computer or something? It was a single board computer.

**Chris Gammell:** Yeah. Was it the OX64?

**Dave Jones:** Star 64?

**Chris Gammell:** OX64. That's what it is. Yep. I didn't realize the name. I thought the name of it was the Pine thing.

**Dave Jones:** Oh, okay. Right. They just got a ton of stuff. Anyway.

**Chris Gammell:** Like, look at this thing, though. Like, seriously beefy. Right. So, this is actually, like, a crossover ship, I think.

**Dave Jones:** It's 128 meg thing for. Eight bucks?

**Chris Gammell:** It's got an 802.15.4, because it can do Zigbee. It's got Bluetooth. It's got Wi-Fi. It's got a camera interface. It's got two RISC-32s and a RISC-64 core in there.

**Dave Jones:** Knots. Right.

**Chris Gammell:** 164 megabit. Megabit? Is that right? Yeah. 16 megabyte flash. And so, pretty sure it's a, yeah, it's like a crossover ship. I haven't done anything with it. That's the thing. Like, I buy these cheap-ass boards, and I'm like, oh, what do I do with this thing? Yeah.

**Dave Jones:** I've got a tub full of cheap-ass dev boards.

**Chris Gammell:** But this thing is a beast. I mean, like, and it's all RISC-5 as well, so that's pretty cool.

**Dave Jones:** Crazy.

**Chris Gammell:** Yep.

**Dave Jones:** Oh, boy. Too many options these days. I don't like options. Options make my life hard.

**Chris Gammell:** So, I have a thread, I think I've mentioned a couple times on here, on my consulting forum, about, like, my learning goals. And I think the advice that kept coming back to me, which I think is very, very important, is, like, you've got to have a project. You've got to have a project. Obviously, you talk about that, too. Right? And I've just got to have, I don't know, though. Like, all of the, every time I think of, like, a new project, it seems trite to me. Like, I'm like, oh, I can just go buy that thing. But, like, that's what I need to get over. I need to get over that, like, I could just go buy it. Of course you can go buy it. You can go buy anything, right? But you need to do it just because I want to do it. And that's where I'm struggling. I'm not sure what the, what I need. I don't need anything enough. You know, there's not anything that I need to optimize enough that I'm like, oh, I should go build that, you know?

**Dave Jones:** Yep.

**Chris Gammell:** So, I asked ChatGPT today. And it didn't help me. I'll be honest.

**Dave Jones:** It didn't help you. It didn't help me. Your personal therapist couldn't help you. Okay.

**Chris Gammell:** That's right. That's right. That guy is kind of useless. I don't want to be mean, but kind of useless. I don't know what to do, though.

**Dave Jones:** Ask another.

**Chris Gammell:** Ask Bing.

**Dave Jones:** Ask Bing AI or something.

**Chris Gammell:** Oh, ask a different AI? I guess I should just ask humans. Yeah, ask a different AI. I don't know. What should I build?

**Dave Jones:** Until you get the response you want. What should I build?

**Chris Gammell:** I don't know. Like, all of the things that I asked, like, I was asking all these things that suggest, too. I'm just like, eh, GPS tracker, digital weather station, smart garage door opener, e-ink display reader, smart mirror, drone, handheld gaming device. Are these the examples it gave you? These are the examples it gave me. And that's the thing. It's just, like, processing, like, probably, like, you went to hackster.io, and it's, like, crawling those, and these are popular products. Like, totally good thing. But I just don't need any of this stuff in my life.

**Dave Jones:** No, exactly.

**Chris Gammell:** You know, like, home security system. Well, no. Digital thermostat, no. Fitness tracker, no. Bluetooth speaker. Like, the thing that I need least in my life is a Bluetooth speaker. Solar tracker, smart light switch, automatic pet feeder, no pets, home automation system, wearable health. I just don't need any of these things, Dave. I don't know what I need. I don't need anything technological. That's the thing.

**Dave Jones:** You need to go push.

**Chris Gammell:** What do I need? Yeah, I mean, what do I need? I don't need anything.

**Dave Jones:** You need to get outside and touch grass. That's what you need.

**Chris Gammell:** I did that today, Dave. And you know what? Oh, excellent.

**Dave Jones:** What?

**Chris Gammell:** It didn't give me a goddamn idea.

**Dave Jones:** All right. I still don't know what to build. Yeah, but it's the act of touching the grass in itself that is the fulfilling part. Don't try and get all zen on me.

**Chris Gammell:** Don't try and get all zen on me. You're not.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah. I do think it's a key part, right? It is a key part to have, like, something that's driving you. There's something you think you need to build instead of buy.

**Dave Jones:** Yeah.

**Chris Gammell:** I can just buy all this stuff, though, you know? I know.

**Dave Jones:** Yeah, I know. We're just getting lazy in our old ages. Our years get shorter and shorter.

**Chris Gammell:** We just have less time and effort to invest. No, here's the thing. I build reference designs for a living. You know, this is what I do. Yeah, but you're getting paid. Some smudges pay you to do that. I get paid. That's right. And so now I'm, like, trying to come up with a thing for myself. And I'm like, hey, who's going to pay me? You know?

**Dave Jones:** I'm going to take some of that money that some schmuck paid me to then go buy it.

**Chris Gammell:** I mean, that's kind of what I think about. I mean, there's that. Yeah, I could go buy it, right? But then it's also like, well, maybe I should just do a consulting project instead, you know? Find someone who needs me to build something. I don't know. I don't know, Dave.

**Dave Jones:** Yeah.

**Chris Gammell:** Anywho, I'm going to keep learning regardless. Right. But the search for a project continues. I think the other thing, too, is I don't have any other hobbies that actually need this stuff. Like, my hobbies are, like, learning Spanish, playing piano. Like, no electronics there. No electronics in those at all.

**Dave Jones:** And some things I just don't need an electronic product for. Like, I just, on my second channel, I just did a mailbag unboxing and test of one of these e-scooter things, right? Yeah. Because they sent it to me. Like, you know, and it turned up in the mailbag. It's like, well, okay. And I'm thinking, well, yeah, okay, it's fun. But no, I'd rather ride my push bike because I actually get exercise. Yeah, exactly. Doing the same task, you know? Yeah. It's like.

**Chris Gammell:** Also, I see a lot of schmucks that wipe out. I just saw someone wipe out tonight on the sidewalk. Nice. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Brilliant. Good luck with that, folks.

**Dave Jones:** Oh, well, they're banned here anyway, so, you know. Are they?

**Chris Gammell:** Oh, that's probably the right move. Yeah. Yeah.

**Dave Jones:** Oh, boy. Yep. Anyway.

**Chris Gammell:** What are you going to do with the scooter now?

**Dave Jones:** No, I didn't.

**Dave Jones:** You've got the scooter.

**Dave Jones:** I can just ride around the underground car park, you know? The kids can play on it or something. I don't know.

**Dave Jones:** I guess. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. I mentioned last week about the beeping buzzer sound. Did I? Two weeks ago? Beeping buzzer sound? That video's up now. I recorded a video, finally, of me. I mentioned I have. I recorded the Mario theme or, like, I put it onto a buzzer. Oh, right. Remember we talked about buzzer versus Pusey Electric? Yep. Yeah. So, that's available now if people want to hear it. Cool. What was the thing you said about Flipper Zero? So, you have one and you've tried it and it does work? Or it's not worth it?

**Dave Jones:** It does. It doesn't work, but it doesn't do things like my garage door remote, my car remote. Because these are, like, encrypted rolling code things. And it's not some magic hacking tool that just bypasses all that.

**Dave Jones:** Right, right, right.

**Dave Jones:** Right? It just, like, I can see it. It's really cool. Like, it's got a spectrum analyzer on it, right? So, you can see what frequency it's transmitting at and everything, right? And you can actually record it, I think. So, you can record the thing, but you can't replay it. Well, you could. You could record it and replay it. But there's no point because it doesn't have the encoding to do the rolling secure code thing. So, it doesn't, you know. Anyway.

**Chris Gammell:** Yeah. It kind of looks like the... Oh, man. There's a lot of YouTube videos about this thing. Yeah.

**Dave Jones:** I basically got caught up in the flipper hype. So, I ordered it months ago. It took months to get here or something. Got it.

**Chris Gammell:** Yeah. Wow. That's a lot of stuff. There's a lot of videos here.

**Dave Jones:** And then I thought, oh, yeah. I can open someone's Tesla door cap, you know, fuel cap with it, right? Charge import cap. Fuel cap. Charge import cap, right? And then, so I went through and I went through all the libraries and stuff. And once again, it's not one of these, like, you've got to try and find someone on some forum somewhere who's actually written the script. And I couldn't find the Australian Teslas because apparently they're different to the US, which is different to the UK, which is different to Europe, which is different to blah, blah, blah. Right?

**Chris Gammell:** Right.

**Dave Jones:** So, I couldn't find the Aussie. So, if somebody knows where I can download the Aussie Tesla thing, I can go around and flip Tesla doors on it. But, you know.

**Dave Jones:** Yay. Woo! Woo!

**Chris Gammell:** So, it kind of looks like the, did you ever see that? I forget what the name of it was. It was, like, basically, like, oh, an I am me. That's what it was. You know, we had, like, all the security people on. We should have more security people on the show. We haven't had them on in a while. But, like, the I am me was, like, this, it was, like, this pink texting toy, basically, where it was, like, over 900 megahertz. Right. Do you remember that thing? I think so, yeah. I think this must be, like, this is, like, the natural inheritor of that thing. So, I remember, like, Travis Goodspeed had one, and I think Mike Osmond might have had one. And I saw them at a couple conferences and stuff like that, but they were, they stuck out because they were, like, this, like, super bright, like, pepto-bismol pink plastic. It was great. And then I think this is, like, the natural, you know, inheritor of that. Evolution of that. Yeah, exactly. But it's the same chipset, I think. I think it's, like, the same analog front end, or, like, RF front end on it as well.

**Dave Jones:** Anyway, I do want to take it to, like, a local shopping center or something and then, like, use it to, like, turn off TVs and stuff like that. You know, like, go into a TV shop and just blast with the infrared remote control. Apparently, it's got the universal TV be gone kind of codes in it, so it'll cycle through 200 different manufacturers' codes off, so you can just turn off every TV or something. Apparently, that'll be cool. Yeah, yeah.

**Chris Gammell:** Mischief managed. Mischief managed. Yeah.

**Dave Jones:** I don't know if I should record that or not, you know, if I should actually take a hidden camera and, like, film me and switch it off, you know.

**Chris Gammell:** Only had Google Glass, Dave. Right. Smart glasses, right? Yeah. Recording glasses. You should get some of those. Get some of those. Yeah.

**Dave Jones:** I'm sure we're developing a new version right now.

**Chris Gammell:** Right now. Yep, exactly. Exactly.

**Dave Jones:** It'll have AI in it. It'll have a chat GPT interface. That'll be the new thing. That's right.

**Chris Gammell:** Right. Except they'll call it A-E-Y-E. A-I. All right. We should probably stop recording now. What do you think? Yeah, we're done. Catch you next time. Bye.
