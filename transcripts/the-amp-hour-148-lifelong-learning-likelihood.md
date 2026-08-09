---
episode: 148
title: Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood
url: https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Club Jameco, part of Jameco Electronics. Have you ever wanted to sell a kit you dreamed up? Do you have an idea for a new project you're working on and you think others would like working on it as well? Club Jameco allows you to upload your kit ideas and start selling to your peers. You can earn up to 10% on every approved kit that you sell. Additionally, if you submit an approved product brief, you will get a coupon code for 10% off your next order at jameco.com. To learn more and to see the chosen kit of the week, go to clubjameco.com slash theamphour. This is the Amp Hour Podcast, recorded June 3rd, 2013. Episode 148, Lifelong Learning Likelihood.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** You don't do anything on that website anymore.

**Chris Gammell:** No, I don't. But I do stuff while I have plans for a new website that I've posted about. Do you tell? You've posted about it? I have. It's a YouTube video to start with and a website. And it's just to sign up right now. But the plan is to start in July. I'm excited and a little nervous. But, you know, I'm excited. Mostly excited.

**Dave Jones:** That patented nervous gamble delivery on video? Is that the...

**Chris Gammell:** No, no. I did the second video. I look way calm. I'm like a Hindu cow, man.

**Speaker ?:** Right.

**SPEAKER_01:** Because I saw his first video, folks, and it was that trademark gamble nervousness.

**Chris Gammell:** I'm getting a little better. It's a little better. Yeah. But anyways, so this is a new thing that I'm starting. It's going to be a 10-week course. It's going to be basically soup to nuts, start at block diagram, and then go all the way through design, layout, component research, everything like that, all the way through and actually shipping boards to people and having everyone build at once and then troubleshooting all together. Oh. Yeah. Novel. Yeah. It's going to be... I don't know if there's anything out there like it. It's going to be interesting. But I'm going to do a whole KiCad... I've already started a whole KiCad tutorial, too, a video tutorial. So that'll be all included with it, too. And yeah, it'll be project-based. So it'll be like starting with a... I'm probably going to do like an Arduino shield just to make it accessible and then do like some kind of analog component with, you know, some kind of signal input probably. Probably signal input, signal output. And then, yeah. And then, you know, show the whole design and all the design decisions and give context and have everybody work together, do meetups, yada, yada, yada. And hopefully it'll work.

**Dave Jones:** It's kind of like a community... It's almost like a community hackerspace project, but doing it virtual. Yes.

**Chris Gammell:** Yes, that's right.

**Dave Jones:** People still build it up, but they've got to build it up themselves, right?

**Chris Gammell:** Yeah. You've got to build it up in your own lab, but the best part about it is you'll be able to build it at the same time as everyone else. Because that's like the problem with like those... Like I really like those massive online open courseware things. But even the problem with that is like you're not necessarily working on the same stuff at the same time as other people, right? I mean, that's a strength... Right. ...and a weakness. So this will be everybody working on it at the same time, going through the same issues, and then also, you know, designing stuff alongside as well. So, you know, just kind of experiencing it all together. And the stuff that gets sent out, it will be all open source hardware too.

**Dave Jones:** But, aha, the key question here is, have you thought about this? Just dawned on me.

**Chris Gammell:** Okay.

**Dave Jones:** You don't learn much when your project works first go. I've always said it. I hope your project fails. Are you going to deliberately put something in there that doesn't make it work and then have everyone send you flame emails? It doesn't work. You busted.

**Chris Gammell:** That is a good question. I don't know about deliberate failures.

**Dave Jones:** And then, aha, you'll find out why in the next episode, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And you'll... You should learn a lot when something doesn't work and you have to troubleshoot it.

**Chris Gammell:** Yes. That is a good question. No, that was not the plan. But I may have to revise it now. So, I think that's a good plan. I think we just started the videos. But, you know, as we move towards launch, maybe I'll have to work in some... I don't know. I don't like... Like, I agree that, like, you should have to troubleshoot that stuff. But, and, like, that's a good way to learn. But it's...

**Dave Jones:** There is no but there. There is no but there.

**Chris Gammell:** It's shady if you put it in automatically. If you put it in deliberately. That's the only thing I don't like. You know?

**Dave Jones:** Yeah, but, you know, how else are people going to learn? You can't just rely on the fact that, oh, they might get a solder bridge somewhere.

**Chris Gammell:** Yeah. Well.

**Dave Jones:** You know?

**SPEAKER_01:** Hmm.

**Chris Gammell:** Well, that's a good thing to think about, though.

**Dave Jones:** And what's the name of this venture?

**Chris Gammell:** Oh, yeah. It's called Contextual Electronics at ContextualElectronics.com. So, if people are interested, I've just got an email sign up right now. So, if you are interested, you know, if you're looking to learn how to, you know, if you're kind of stuck and you're... Not stuck, but if you're just kind of getting... You've always wanted to build hardware, but you didn't know where to start. And you've done some other stuff, like you've programmed Arduinos or Raspberry Pis or something like that. This is going to be kind of like a good course for that person. Or even if you have built some hardware and you want to build along other side people. Alongside other people, rather.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Sounds good. It's exciting. It's... I hope it doesn't... Good luck with that. Flop. Because that would be an awkward Chris on a video, right? So... You're right.

**SPEAKER_01:** Oh, sorry, guys. I'm not doing any more videos. Yeah. Because, well, it was a flop. I'm going to go hide in a corner. And... My dreams of becoming rich or rich and famous or just gone down the toilet. Yeah. I don't really think that's ever going to happen, so... No.

**Dave Jones:** So, uh... The aisle, we should mention that it's not free.

**Chris Gammell:** Right. It is going to be...

**Dave Jones:** It will be a paid course. It will be a paid course.

**Chris Gammell:** There will be some... I mean, I'll release some of the videos for free as well, but not the whole course. Right.

**Dave Jones:** As a taster.

**Chris Gammell:** Yeah, and also just... You know, some of the resource videos too, you know, like as I'm... Right. Okay. Going through design decisions. You know, if it's like a op-amp selection kind of thing, right? That's always a...

**Chris Gammell:** Nice. Yeah. A good thing to do, right?

**Dave Jones:** They're very popular, yeah. I've done a few of those and they are always very popular.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. I agree. But I'm telling you, you've got to make them fail.

**Chris Gammell:** All right. Well...

**Dave Jones:** Now, throw your...

**Chris Gammell:** Listen to the wise old man. As I stroke my grey beard. Throw the board in your oven for about two hours now and then we're going to troubleshoot and see what happened.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, you could ship them kits with incorrect parts. Oh, God. Yeah, that'd be neat. Or label them differently. Say it's a... You know, say that this cap is actually like a 10-mic cap when it's actually like a... You know, a 10 nanofarret or something.

**Chris Gammell:** You're... That's nasty, man. That's just...

**Dave Jones:** No, it's not. It's great. They're going to learn.

**Chris Gammell:** Yeah.

**Dave Jones:** They're going to learn not to trust you. Not to trust any bastard. Don't trust any bastard. That is a good lesson. One of Dave's tips for life. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm telling you, it's the way to learn.

**Chris Gammell:** All right. Fail. Keep that in mind. Maybe it'll happen naturally. Right. So, what's new with you? What's new? What's shaking, man?

**Dave Jones:** I don't know. Yeah, I'm busy.

**Chris Gammell:** Busy? As I always am. Always behind the eight ball. You're waffling on about your beautiful new microphone. The new Samson.

**Dave Jones:** Yeah, I got one of these little Samson Go mics. I haven't actually powered it up yet, so I don't know what the quality's like. But considering that I'm now talking, doing this radio show on a Samson mic, and all my voiceover work for the video blog is also on a Samson mic, I expect it to be pretty good. And for like $40 or something, it was a bit more here in Australia, but it's a really nice quality, solid little desktop mic. You know, it's designed to carry in your bag, and you can clip it onto your notebook. And, you know, so it's like a portable podcasting mic kind of thing.

**Chris Gammell:** Well, for $40, that's basically a Skype mic at that price. I mean, like...

**Dave Jones:** Yeah, yeah, yeah, exactly. It's a high-quality Skype mic, and it's got selectable cardoid mode.

**Chris Gammell:** Oh, yeah, that's right. Great.

**Dave Jones:** So, you know, neat. And it feels weighty. You know, I love a product that actually, like, you pick it up, and there's some weight in it. Right, it's not that flimsy plastic. You're like, oh, what the hell? Yeah, exactly. You know? Yeah, I've just bought some eBay cheapy piece of shit. You know? No, it feels great quality. So, yeah, the idea is to put that mic onto a laptop that I permanently had set up to a USB microscope. So I can then, you know... Because the problem with the... You know, it's always a logistical problem, right? I've got my... Yeah, I've got a nice Samsung desktop mic here, but if I want to... But it's in the office cubicle part of my lab.

**Chris Gammell:** You want to, like, look and talk at the same time, right? That's difficult.

**Dave Jones:** And then I've got to disconnect all the cable in and take it over to the... No, it's just a pain in the ass. I've got, like, four notebooks here that I've salvaged from the junk room. You know, I'm just going to put one of those and set one up permanently as just a USB microscope thing with a quality mic built in, and then I can just turn it on, press go, and...

**Chris Gammell:** Yeah.

**Dave Jones:** You know?

**Chris Gammell:** See, that's always the thing with, like, test equipment too, right? You want to... You always want to have, like, multiple... Like, the best case scenario would be to have, like, you know, four copies of everything so then for each experiment you're doing you don't have to break something down because as soon as you break down an experimental setup, you're never going to... You know, you can't... Obviously, you can't keep recording the data if you're doing logging or something like that, and then, you know, you can end... You just have a lot of potential for error when you try and set it back up. So it's difficult for that kind of stuff. So it's nice if you can get it.

**Dave Jones:** And I'm one of those... I'm one of those engineers who likes to build stuff anywhere, right? Like, I've got multiple... You know, I've got, like, a six-metre-long bench in my lab here, right? Yeah. So it's a pretty generous-sized bench. But, you know, this is why I hate bench multimeters, right? Because they're just fixed in the... Like, you can't just move them from one bench to another. I can't take it home and work on... Or I can't bring it into the office here and work next to my notebook when I'm developing a, you know, a PC-based, you know, USB product or something. You know, it's like... You know, I hate taking the thing I'm working on to the bench. And then it's usually... Bench is filled with crap, right? So I think I move it all. There's three other projects I'm working on. You're, like, probing over top of, like, three other projects. Yeah, three other projects that I'm working on at the same time. And it's just, you know... Yeah, I want to... You know, so I need, you know, six different multimeters because I'm always working on projects in different locations and stuff. And it's just... Yeah, I need an oscilloscope that's not fixed to my bench. I don't want to have to disconnect the power cord and move it over to another bench and then, you know, it's just...

**Chris Gammell:** You used to have, like, a hoverboard with, like, test equipment on it, huh? Ooh.

**Dave Jones:** A hoverboard would be great for the camera, you know, if you get a camera mount with a hoverboard or a light mount, you know?

**Chris Gammell:** What about test equipment mounted to the bottom of a quadcopter? That. It's a little noisy, probably. And the vibration might... I was going to say,

**Dave Jones:** it'll be noisy and breezy, son of a bitch. Yeah. Yeah, it's true. You get the temperature differentials. Oh, boy. Yeah, that's the downside

**Chris Gammell:** with the bench-level test equipment. It's, like, it's got that thing that you like, right? The heft, you know? Like, have a good heat sink on it or something for good thermal stability. But, yeah. All right. It's harder to move then.

**Dave Jones:** Speaking of workbenches and labs and stuff, have you seen the new Iron Man?

**Chris Gammell:** I did, yeah.

**Dave Jones:** Yes. Do you see the... Oh, it's not really a spoiler. It's just something that happens at the end of the movie about the kid's lab. You remember that? Oh, yeah, yeah, yeah. Yeah, yeah. Very sets of the... It tricks it out at the end, yeah. Yeah, it tricks it out at the end. It's not a spoiler, folks. No, I don't think so either. A nice little, you know, part of the ending, you know? And, yeah, so this little, you know, young Tony Stark, you know? Exactly. You know, he sets up this kid's lab and he's got everything, you know? Right. Awesome.

**Chris Gammell:** That would be the ultimate, right? To, like, walk into your lab one day and just, like, Santa Claus has just dropped off... And somebody's kidded out. Yeah, Santa Claus. The ultimate lab, right? Instead of doing it piecemeal and, you know...

**Dave Jones:** Yeah, buying second-hand eBay gear, scrounging it from wherever you can get, you know? Right, yeah. 30-year-old crusty HP gear or something.

**Chris Gammell:** Exactly. Deal hunting is fun, but at a certain point you're like, no, I just want... I want to be able to just, you know, just do everything I want to do immediately, right? Yes. So it's...

**Dave Jones:** You know, exactly. I want everything at my fingertips and everything to be top-notch and brand new and...

**Chris Gammell:** Yeah.

**Dave Jones:** You know, yep.

**Chris Gammell:** Yeah, so you actually asked about this too, about how much it takes... I did. What does it take to equip a killer lab these days? I don't know. Thousands? Well, I don't know either. You're talking about...

**Dave Jones:** Yeah, yeah, yeah. I'm talking money. Because, well, see, I'm probably going to do a tear-down today of this Keithley 2015 meter that I got. Yeah. You know, and it's six and a half digits. It was like 400 bucks on eBay. I know you're not a big fan of it, but, you know, even though... No, well, I'm a...

**Chris Gammell:** I'm a fan of the DMM, just the THD total distortion stuff.

**Dave Jones:** Yeah. If people don't know, it's a six and a half digit multimeter with a THD measurement capability built-in, which means it has a function gen, like an audio bandwidth function gen built-in, fairly low THD, and you can hook it up to your PC and get THD plots of, you know, products and stuff like that. So, yeah, it's a bit wanky.

**Chris Gammell:** Yeah, it's just specific for what they were selling to.

**Dave Jones:** Yeah, yeah, exactly. But, hey, it's a pretty good bit of kit for 400 bucks.

**Chris Gammell:** 400 bucks is a good price, yeah, definitely.

**Dave Jones:** Yeah, yeah. And, you know, because the nearest...

**Speaker ?:** Six and a half digit is tough to get.

**Dave Jones:** Well, that's right. The nearest six and a half digit meter on the market brand new is double that, right? One of those Rigol ones.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Or something, I think, you know, that's probably the nearest one. That sounds about right. It's double that, so... I think that's right.

**Chris Gammell:** Yeah, because I think Rigol just came out with that one, too, the six and a half. It's not very old. Yeah, it's... They started with the five and a half, but...

**Dave Jones:** Yep, yep. But, yeah, so that's about 800 bucks. So, you know, it's half that price. So, you know, and it's not like a 30-year-old HP model, you know. I know that model's about 20 years old, but I think the one I've got's about 10 years old. Oh, okay, yeah. I don't think it's hideously old. I've got to check that again, but... You know, but you can get, but there's lots of great deals out there. I mean, you can set up a pretty kick-ass lab for 10, let's say 10 grand, right? Which is a lot of money.

**Chris Gammell:** I mean, that is a lot of money.

**Dave Jones:** Well, it is a lot.

**Chris Gammell:** It's an investment in your future. But if you do it over a couple of years, that's right. Yeah. Yeah, I mean, I think about, you know, like hobby products. I mean, just other hobbies, right? Like someone that plays golf, right? They might drop, what, 800 bucks a season? I don't know. My dad golfs, but I don't golf. You know, you think about... I don't golf, no. Yeah, like fees and stuff like that and equipment. You know, eventually that stuff all adds up. Yeah, exactly. Yeah. Beers at the...

**Dave Jones:** But, you know, you get these gaming kiddies thinking of, you know, they spend a thousand bucks on a graphics card and, you know, they buy an $800 keyboard.

**Chris Gammell:** That's true. You know? Yeah.

**Dave Jones:** I mean, yeah.

**Chris Gammell:** Yeah, hobbies are expensive. I was talking to someone about that on Twitter. You know, like, it's not that you have to. It's just if you want, you know, if you have specific needs, you know, like a six and a half, right? Like, you know, I've used a lot of six and a half digit meters and it's like most of the time you're using it in a three and a half or four and a half digit context. You don't need the extra digits of resolution. But when you do need it, you're just... You're just... Bang. Yeah. Banging your head against the desk. So. I don't know. Exactly. I don't know how much it would cost, though, to outfit it. I was talking to a friend today, actually, about this cheapy power supply I have. This from Electronics Express. It's a triple output 30 amp. Right. Or 2 amp 30 volts. Yeah, you know what I'm talking about? It's like $130. It's like... That's awesome. Yeah, I know.

**Dave Jones:** Yeah.

**Chris Gammell:** And pretty clean supply, too. I mean, it's not like it's like real noisy either. It's linear.

**Dave Jones:** It's a... No, it isn't a switch mode. It's a linear. Right. You know, like I did a review of that. You know, I got like a $400 one, but it was a precision one, right? It was... Yeah, it was triple output, and it had precision, you know, 0.01%, 0.05%. You know, really. Yeah. You know, the specs are all there, but it was a piece of shit, of course, because the user interface was just garbage. Right. You know, everything else. But, you know, technically, you know, the capability you got for that money is, you know, really remarkable. And as you said, yeah, those power supplies, even a triple output one, yeah, like $150 or less.

**Chris Gammell:** Right.

**Dave Jones:** Crazy.

**Chris Gammell:** Yep. Man, when I was a boy... Yeah, I know, right? Well, you build your own. You know, at a certain point, you balance that out with building your own. It's like, you know... Like I saw... Yeah. What do I see? Oh, I saw an article about Heathkit, actually. And... Oh, Heathkit. I know. Yeah, there's a rumor they're bringing... There's like a survey on their website right now that... And there's a rumor that's saying that, oh, someone might have bought the brand and is bringing it back or something, which I'll believe when I see it.

**Dave Jones:** But didn't they do that, like, five years ago or something? Yes. Right, I thought they did that once. They failed, didn't they?

**Chris Gammell:** Yep, yep.

**Dave Jones:** Right. So someone's going to do it again. Some...

**Chris Gammell:** Well, that's what they're saying.

**Dave Jones:** A nostalgia nut thinks that there's, you know... Mm-hmm. Yeah.

**Chris Gammell:** And I was reading some articles about it, and, you know, they were talking about it, though, and, like, basically with Heathkit, though, it was... You were buying stuff and building it not just because of the interest and, you know, how it works, but also because it was just cheaper. It was... At the time, it was cheaper to do that. And these days, you know, like...

**Speaker ?:** Yes, of course.

**Chris Gammell:** I mean, 135 bucks for this thing, it's like... Between shipping and the amount of aluminum in the heat sink, it's like, okay, well, and the transformer, you know, it's getting down there. It's like, well, what's really in there now, you know? Yeah.

**Dave Jones:** It's like I used to sell PC-based scopes, right? I used to design and sell PC-based oscilloscopes, you know, thousands of them. Yeah. And this was back in the day when, well, you couldn't buy a PC-based oscilloscope for under, well, you know, under, you know, three or four grand or something.

**Chris Gammell:** Yeah, right. You know?

**Dave Jones:** It was crazy. So to buy and build your own one, yeah, it was very limited, but to buy and build your own one for a couple hundred bucks was, you know, an absolute bargain. But now, geez, you know, you can buy a hundred megahertz bandwidth one on eBay for two hundred bucks.

**Chris Gammell:** Right. Exactly. Yeah.

**Dave Jones:** Or you can buy a hundred megahertz, you know, bench scope for three hundred bucks. Crazy.

**Chris Gammell:** Yeah. Different world. Yeah. Well, it's just, you know, that's the, it's the ups and downs of abundance, right? I mean.

**Dave Jones:** Right.

**Chris Gammell:** On the upside, we get to benefit from that, but, you know, if you have any sort of nostalgia for the, you know, the good old days of everybody building their own stuff, it's like, eh, you know, it's like, you know, there's a lot of frustration there too, right? I mean, like, in terms of like inclusiveness, right? Like, I think, oh, someone was mentioned on Twitter today about, they long for the days of 6502, and it's like, well, yeah, I mean, like, that's a simple processor core, right? And it's easy.

**Dave Jones:** But there's still a ton of simple processor cores around. Well, yeah.

**Chris Gammell:** Take your pick. But I mean, I think they were longing for the time when everybody was building with those though too, right? Is that, that being the only option? And it's like, well, yes, that might've been the only option, but there was a far smaller community in general too, right? I mean, like, we've talked about before with the inclusive, you know, it's better to have an inclusive hobby that, you know, brings more people in, and then you can segment within that hobby than to, to, you know, keep people out with a, you know, a high entrance cost.

**Dave Jones:** Well, see, that's the thing. Everyone talks about the glory days, but you remember how much it costs to get a 6502 development kit back in the day?

**Chris Gammell:** No, I wasn't alive.

**Dave Jones:** This is right. This is back like in the early microcontroller days, right? Right. Microcontrollers, which now you take for granted, you can do it for practically free, right? You can hook, if you want to, you can hook it up to your parallel port and your programmer and, you know, and it costs you nothing, right? You don't need to spend a cent.

**Chris Gammell:** No, it's USB, man.

**Dave Jones:** USB to serial, JTAG, right? You know, yeah, you can buy it. Well, you can get the, yeah, like the T-I-M-S-P kit for five bucks or whatever, and they give you a USB development programmer. I mean,

**Chris Gammell:** yeah,

**Dave Jones:** five bucks. Yep. It's insane. Yep. Right? Whereas back then, nobody could afford, if you weren't a business, like a fairly reasonably sized business, you couldn't afford a microcontroller development kit.

**Chris Gammell:** Right.

**Dave Jones:** Let alone the hobbyist.

**Chris Gammell:** Right. Nothing with, no emulation either, right? You'd have to pay for that separately.

**Dave Jones:** So don't crap on about giving me the good old days. The good old days weren't that good.

**Chris Gammell:** Right. Yeah, that's, I think that's.

**Dave Jones:** It reminds me of the Billy Joel song, right?

**Chris Gammell:** Was that, which song was that?

**Dave Jones:** Oh, the Billy Joel, you know, um, yeah,

**Chris Gammell:** I used to love Billy Joel. I haven't listened to him in a while. You're talking about like only the good die young. That wasn't in that song.

**Dave Jones:** Only the good die young. I think. Yeah. No, is it? I don't think it was anyway. No,

**Chris Gammell:** next week on the amp hour, we'll have Billy Joel on to explain.

**Speaker ?:** No,

**Chris Gammell:** I'm lying. Yeah. Oh dear. Yeah.

**Dave Jones:** I'm sure we could get him on. This is a. Oh yeah.

**Chris Gammell:** What's he doing? Radio show. We got a lot of pool. Right. Yeah. Oh, actually. Yeah. So we, we were going over this before the show today. We're, we have, we're, we're nearing 500,000 total listens for, uh, the show, which, you know, as I told Dave, it's like compared to YouTube, it's like, well, it's not, it's not quite as many as Dave has on YouTube or a lot of people have on YouTube, but you know, we're a pretty long show too. And so we did some quick math at 500,000 or I think it was for, 480,000 listens. If everybody actually listened to it, that would be 3.6 million minutes. Amp hour minutes, I guess. Amp hour minutes. 6 million amp hour minutes, 600,000 amp hour hours, 25,000 amp hour days, or 68.7 amp hour years.

**Dave Jones:** And we'll get people complaining that where we're just screwing up all the units there. Oh yeah. Yeah. Right. Blow it at your ass. Yep.

**SPEAKER_01:** Send complaints in writing to we don't give a toss.com.

**Chris Gammell:** Take a number. It starts at 36.1 million.

**Dave Jones:** Oh dear. No, but you'll, you'll get those anal people. You didn't do the correct units. I've had people like, I did something on the whiteboard and I didn't do the, like the way I did the equation was incorrect. And they explained why it was incorrect and how it, you know, it's, you know, you can't just put the things on the wrong sides of the equal side. It's like, oh, go away.

**Chris Gammell:** Yeah. No, I was talking, I was talking to someone about that.

**Dave Jones:** Intentive.

**Chris Gammell:** Like the perfection for perfection sake, like kind of like what I view is like the, you know, kind of ivory tower mindset of like, oh, well it's not right unless it's perfect like this. It's like, no, it's perfect.

**Dave Jones:** Academic. Perfect. We're talking about. Yeah. Yeah. Yeah. Yeah. And it's like,

**Chris Gammell:** if you get the job done, you know, like even if there's some mess in the middle, then, you know, like I feel like that's the engineering things, you know, it's like, maybe it's not perfect, you know, from a theoretical standpoint, but sometimes, you know, sometimes you're going to just get out a decade box and try different values. You're going to, you're going to solder in a capacitor to, you know, try and compensate for an op amp, you know, it's like engineering. We get that.

**Dave Jones:** Like, yeah, I get that all the time. You know, things like, oh, my pronunciation of things or the way I do my units or something. Oh, my units are wrong. I don't know how to do units properly. And oh, bloody hell. It's like, I copped this just the other, uh, my last video with the, um, input op amp, input offset voltage, right? People said, oh, that's not strictly the correct definition of offset voltage. The offset voltage is the, what voltage you need to put on the output to make your output input to make your output zero. And it's like, yeah, in fricking academia, in the real world, you care about the, you know, when, when you short the inputs to your op amp, you get 2 million volts on the output. That's your bloody offset voltage. You know, like, oh, it's like, oh, yeah, it's, you know, being, being pedantic and academic, academically correct for the sake of it, you know?

**Chris Gammell:** Yeah. It's tough too. And like, when you get that at like a workplace, I mean, obviously your workplace is, uh, full of, uh, it's got one big asshole there, you know? Right. Yeah, yeah, exactly.

**SPEAKER_01:** One, it's got one big guy in a retentive asshole. Yeah, right. but,

**Chris Gammell:** you know, like you've experienced that at workplaces before, right? And I'm sure a lot of people have where, you know, you had that one guy, oh, well, you know, he's sitting in the back of the conference room. He's just kind of lobbing out stuff. It's like, dude, what have you done lately? Yeah.

**Dave Jones:** I can remember we had the, uh, manager came in once, you know, came into the lab, you know, so we had to put down all our fart novelty toys. Oh yeah. Actually pretend we're doing some work. Right. And, uh, we, we had our boss detection system. Oh yeah. Yeah. You get the trip wire. Yeah. Yeah. Yeah. That's right.

**SPEAKER_01:** Yeah.

**Dave Jones:** And, uh, yeah. Coming down the corridor, you know, you can hear the management footsteps. Yeah. Right. And, um, you know, came in and said, oh, look, we have to talk fellas. And, uh, you know, sorry, it was a lab of all guys. So there were girls. So fellas is actually correct. So don't write in and complain. Sorry, girls. Um, it's just the way it was. No, right. Right.

**Dave Jones:** Right. No, no, this is previous company.

**Chris Gammell:** That's fine. This is big.

**Dave Jones:** This is, oh yeah, this is big. This is big aerospace company. You know, this is big 40, 50 billion dollar aerospace, not aerospace, military. Yeah. company. I know, I know who I've worked for. Anyway, I came in, right. And said, uh, look fellas, we have to talk, you know, we've been getting too many, you know, reading everyone's, uh, uh, reports and documentation and things. And I don't like this, um, funny business where you don't put units, you know, you use words like, uh, you know, Oh, the offset voltage was small. You know, I don't want you to use the word small. I want you to put a quantitative figure in there. Always put a quantitative figure. Do not use a descriptive word. Yeah. All right. You know, it's like, well, you know, fair enough. I know where he's coming from. Right. You know, when you use descriptive words instead of putting actual figures, it's not very engineering like, but you know, it was like, yeah. So that was the new rule, you know?

**Chris Gammell:** Yeah. But there's context there too, right? It's like, it's like, if it, of course, you know, if it matters or not, right. If you were actually exactly, that's right. Yeah. So if he's just coming at it from the idea of, well, it has to be more sciencey, you know, it's like,

**Dave Jones:** exactly. That was the, that was the idea.

**Chris Gammell:** Right.

**Dave Jones:** It's got to be more professional engineering like,

**Chris Gammell:** yeah. Well, and it's interesting in those situations too, of, you know, like looking at that kind of stuff from like taking that at face value. It's like, yeah, you know, screw that guy. Right. But I've had a lot of experiences too, where, you know, that kind of thing will happen. And then, you know, once the anger subsides in me, right. Or whatever, whatever emotion is, is, is initial. If you step back, sometimes you actually can look past that person. Right. It's like, Oh, well, what's really happening here. And it might be that his boss is actually, you know, scanning reports and he got yelled at, or, you know, he's trying to move up the company or something. Right. There's always like these, you know, especially in big companies, there's always like these undercurrents of like politics and all this other crap. And it's just like, I just want to go to my lab and measure stuff and build stuff, you know, like it's, it's tough, but it's, it's, you know, sometimes it's interesting to take that step back and be like, Oh, this is, there's other stuff here, you know, and then, and then mess with them too. If you can not get fired.

**Dave Jones:** So tell us your stories of listeners. That is tell us your stories of stuff like that, where you've come in and you've been spoken to because you're doing it wrong. Yes.

**Chris Gammell:** Yeah. That'll be good. The comment section is always there for you guys to let us know about that stuff. Yep.

**Dave Jones:** Uh, will the best comment win a t-shirt? Oh, um, best story. Shit. I've put it out there, haven't I? You have. I've just, uh, yeah, I've just, all right. Damn it. That costs us money.

**Chris Gammell:** No, that's okay.

**Dave Jones:** We're trying to save money. We're trying to get rich with this amp hour. No, we're not.

**Chris Gammell:** We're trying to give it away. Yeah, we are giving shit away. Actually, we should mention too, we're, we're getting, we're getting more, um, transcripts of old shows, especially where we're trying to find ones. Yes, we are. Get the ones done with the guests first. So if, you know, if, uh, if, if anyone out there has heard of people, you know, stopping listening because it's just, you know, too much time or whatever, they read faster. or if you, if anyone out there is listening wants to go off and read stuff, we, we have a category now just called category slash category slash transcripts. Um, and it should, there's a button on the website, but, you know, if you are interested in going back through and making it more searchable too, because, you know, every time we do a survey for the show, everyone's like, your titles are ridiculous and I can't find shows. So, yep. Hopefully that'll help. So, uh,

**Dave Jones:** that's the idea because it does cost a fair bit of money to get each show transcribed. Cause some poor bastard has to sit there for an hour and listen to us idiots. Yeah. Yap on. And then actually go, right. Who's talking? And they have to, I'm amazed that they can, I am too. They have the patience to sit there. They've actually,

**Chris Gammell:** uh, the, we've, we've got two, two nice ladies doing it for us. And, uh, the one actually said she really, she likes it. Cause you know, you compare it to like, usually it's like doctors, you know, like talking into their tape recorder. right. Yeah. Transcribe that stuff. So apparently we're a bit less formal than doctors. Go figure.

**Dave Jones:** You think?

**Chris Gammell:** Yeah.

**Dave Jones:** So hi to our transcriptions. Yes. Sorry. What do they call themselves? What would be a term? Transcriptionist? Transcriber? Transcriptionist. Yeah. Transcriptionist. Yeah. There you go. Hmm. Yeah. Yeah. And they get to put in shit words, words like shit and dickhead. Nice. I can do that. Cause I'm Australian. Right. Of course. Of course. That never happens in America. FCC.

**Chris Gammell:** Yeah. I'm actually, the FCC came and told me it's okay if Dave says it, but if you say it, Chris, you, uh, when nothing happens, it's a podcast. Right. Speaking of, uh, former shows, uh, former shows, uh, we had, we had talked previously on here about the, uh, the low cost pick and place machine. I think, uh, when Zach Hoken was on, he, he mentioned it. That's right. Uh, Ian from dangerous prototypes has actually gotten one. He's been doing some videos with it. Um, I got an email from them just like out of the blue, the people that make those. Yeah. I've read that. Yeah. Yeah. And like, they, they,

**Dave Jones:** they sent it to the Ampere.

**Chris Gammell:** Oh, they did. Okay. Yeah. So they, um, yeah, yeah,

**Dave Jones:** yeah.

**Chris Gammell:** The, it is now like the, before you had to actually buy it over there. Um, I, I actually wasn't able to find how you buy it, but apparently they are exporting them to the States now. So if people are interested, um, I'll put a link in.

**Dave Jones:** Even to Australia. I think, I think they mentioned Australia as well. Oh, cool. Except, except they spelled Australia wrong. If I remember correctly. Yeah. Well, these things happen. No, it wasn't Austria. Yeah.

**Chris Gammell:** Yeah. Well, that's cool though. I mean, like in, and he's got some cool videos for that stuff too. I mean, it's, it seems pretty slow, but every time I kind of look at that, I think about, you know, if you could, if you could do a pick in place, you know, if you had enough boards to do maybe like a 20 run kind of small board thing, it starts to make sense eventually, you know, if, if, if it, if it won't mess up and you can walk away,

**Dave Jones:** maybe, but yeah, I've, you know, but, but then it can't do tubes, right? It can only do feeders. Like, so if you've got tubes that can't do, I don't even know if it can do trays. So, you know, like, well then, you know, that, oh, there goes half of my parts on my current board, you know, my, my current design. It's like, well, if it can't do all of them, then what's the point? You know, I might as well send it over and send it to a real shop, you know, that has a machine that can do all types of packages. Yeah. There's always going to be a balance. Yeah. But he's pick and place. Yeah. I'd love to have one as a toy, but I, you know, I just always can't help feeling that. It's just in that narrow band of, you know, very niche area where it makes it worthwhile. Yeah. I think there's a very narrow band in there and you've got to weigh up whether or not your time is to run this thing is worth it. I think, you know, I think you've got a suitable project.

**Chris Gammell:** I think you have to balance the fact that you just want to learn it too. Like that, I think that that has to be the number one thing to start with.

**Dave Jones:** That's another aspect.

**Chris Gammell:** Right. I mean,

**Dave Jones:** if you want to use it as a real tool, right, you, you have to go, well, you know, I have to look into all the, all the details matter, right? There can be showstoppers. Like I said, no, no trays, no tube vibrators. Right. So there's another word, add vibrator to the transcription list.

**Chris Gammell:** Different, different context than sometimes.

**Dave Jones:** We're talking about tubes. Yeah. Right.

**Chris Gammell:** Right. Of course.

**Dave Jones:** But it'll, it'll help with the search terms. Yes, of course. We'll get all the great search traffic at that point. We should say vibrator a couple of times. And yeah.

**Chris Gammell:** I'm not getting this show transcribed now. It's just.

**Dave Jones:** Oh, damn it. All right. So where was it? Yes. You know, there can be one showstopper. Oh, it doesn't support tubes or trays. Right. I'm out. Cause my next project has tubes and tray parts. So what am I going to do? Hand soldering by hand. Screw that. Yeah. And I have to, I might as well send the whole lot over to a house that can do it.

**Chris Gammell:** Right. Yeah. And I think that point is like, because if you wanted to go off and learn it too, you probably also would be willing to try and, you know, integrate your own tube loader or, you know, tray loader at that point, because, you know, you're learning it for like, like Ian, he's learning for the sake of learning it, but then you also get boards on the other end. It's, it was, it was kind of the same advice that was given to me when I was looking at a milling machines was like, do you want a machine or do you want a project? And I think. Right. This is closer to a machine, but I think it's still a project right now.

**Dave Jones:** It's still a pro. Yeah. It's yeah. Yeah. So yeah, I don't know. You know, yeah, I'd love to have one to play with too, you know, but well, would I produce my new microcurrent boards with it? Well, you know, no, no, no. Right. And, and that's a simple board.

**Chris Gammell:** Yeah. Well,

**Dave Jones:** it's also the working area is quite small.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh no, it's not. No, no, no. Somebody was talking about a developing a pick and place machine. Was it another bloody Kickstarter thing or something?

**Chris Gammell:** And it was like,

**Dave Jones:** you know, a thousand dollar pick and place machine. And it was like, and the, and the build area was only like Euro card size. Yeah. What's the point? If you have to do one board, the whole point of a pick and place machine is that you can do a panel at a time.

**Chris Gammell:** Yeah. Big. You know,

**Dave Jones:** you can do 10 boards. Right. Otherwise you're just pushing shit up here with a pointy stick.

**Chris Gammell:** Yeah. I saw there was a, someone took a picture of maker fair. It looked like at first I thought it was an old maker bot. It was like the wood chassis style, like the maker bot. What's the one you have? The thingamatic or whatever. Yeah.

**Dave Jones:** The thingamatic. And yeah, even, even the new ones would. Well, the newer one I've got, I've got two of them. They're both wood.

**Chris Gammell:** Oh, okay. Yeah. But it's, it was that same kind of laser cut wood chassis and stuff. And I was looking at it and I'm like, that's a, Oh, it's not a 3d printer. It was actually like a little pick and place in there. And it's like the same kind of thing of like, well, you know, at a certain point it's, well, I'm just going to, I'll get, you know, tweezers and, you know, a little syringe, like one of those, I've used those little air, air operated, uh, solder paste syringes. Those are nice. I mean, you can do a lot of work with those.

**Dave Jones:** Those are okay. Yeah. You can have your tape. You can peel back the, you know, the, uh, the, the tape and peel back the, what's the thing called? The cover, you know, the tape on the tape. It doesn't make sense.

**Chris Gammell:** Like off the reel. You're talking about like the little, the clear.

**Dave Jones:** I'm talking about the plastic. Cellophane. So you, so you peel the film off the tape, right? And you stick your tape down to your bench and you can have multiple ones and you label them and then you can get your little vacuum pick and place machine. So you're, you become a human pick and place. Yeah,

**Chris Gammell:** exactly. Exactly.

**Dave Jones:** Basically. And you can get pretty efficient at that. Yeah. Yeah. Actually. You know, um, yeah, I've had some boards. And it's great. If you only want to do five boards. Yeah. If you want to do five boards or something.

**Chris Gammell:** Exactly. Or if you think you're, or if you think you're going to mess something up, uh, you know, you know, or if you want to selectively populate too, you know, it's like at a certain point you have to, you have to program a pick and place, right? It's like, but if it's, you know, human programming, you just say, Hey, don't put that one there. Leave that part off for now. Oh, okay. I don't have to change the program. So humans win for now. Take that robots.

**Dave Jones:** Right. So how much is this pick and place machine? It's like three grand or something. Yeah. Three or four. Four grand.

**Chris Gammell:** I remember. I think.

**Dave Jones:** Right. See, that's probably, you know, that's too expensive for me to get wife approval on that and just play around with it for some video action. You know, if it was a thousand bucks, yeah, I might, I might actually buy one to play around with and do some videos on it. Yeah. Um, but yeah, that's probably a bit, that's a bit much. I'm afraid.

**Chris Gammell:** Oh, well, then some breaks. We should mention our sponsor who's back this week. They are back. Yeah. Club Jane Co. Back from the future. Back from the future. Really? No, back. Uh, yeah. Club Jane Co. is back. And, um, so people can go to clubjameco.com slash the amp hour. That's where they list all of the kits we've talked about, uh, this show and the past shows. And also you can submit to your own kits. So if you submit a kit idea, you can get a coupon. Once it's approved as a, you know, it's a legit idea. You can get a coupon for 10% off your next Jane Co. order. And then if they start manufacturing your kits, which they have a growing library of kits that are, you know, you submitted, um, then you get upwards of 10% of the kit sales, which is, uh, dependent on how many they sell. So, you know, of course. Oh yeah. Yeah. If they sell,

**Dave Jones:** that was just bleeding, obviously. No, I'm sorry.

**Chris Gammell:** Then I meant there's like tears that like, if it's like, if you get past a certain tier, it's like starts at 5%, it gets eight and then 10%. Yeah. Yeah.

**Dave Jones:** So I picked out a, you don't have to do anything by the way to get that.

**Chris Gammell:** Right. Yeah. Once, once it's,

**Dave Jones:** it's, it's completely hands off. You don't do a thing.

**Chris Gammell:** Right. Once it's approved by the community, like they have voting and stuff. So, um,

**Dave Jones:** money for jam.

**Chris Gammell:** Yep. Pretty good stuff. So, um,

**Dave Jones:** yes, please support our sponsors because they help keep the show alive.

**Chris Gammell:** Yes, they do. Uh,

**Dave Jones:** we're very generous and we need to be generous to them.

**Chris Gammell:** Definitely. Um, the kit we chose this week, actually I chose it. Dave wouldn't care about this, but it's actually a, so it's a kit. It's, it's, it's a double whammy, right? Not whammy. It's a two for one. It's a, uh, it is a kit, right? So it's a, a pickaxe space kit. And then, so you build it up, but then it's also, once it's done, it is a Morse code trainer, basically for all you, uh, CW in, uh, aficionados out there. So people that are ham radio people, you can use it to, uh, learn Morse code. So sweet. Yeah. Exciting. Do you know Morse code? Oh no, that's not part of the, uh, the thing anymore.

**Dave Jones:** No, they dropped it. And that was one of the reasons why you went for it. Yeah. I can easily get my ham license now so I can appear to be cool.

**Chris Gammell:** Appear to be cool.

**Dave Jones:** Huh?

**Chris Gammell:** Yes. Nothing Says Cool Like Ham Radio. That's right. That's right. Grads and dads, get your, uh, get your ham radio license today. Uh, it's the hottest gift of the season. Nothing, nothing says attractive to the opposite sex. Like, I have a call sign. Walking around, walking around Hamvention is nothing more. It's like, it's basically like going to the Cannes Film Festival or a model show or something. You know, it's basically, nothing but beautiful people as far as the eye can see.

**Dave Jones:** Would that be the hallmark of a, uh, of a nerd? If you had somebody come up and ask, ask your number and you actually gave them your cool sign.

**Chris Gammell:** Hit me on the 20 meter, baby.

**Dave Jones:** Oh dear. That's quite sad, really. Yeah. But I can see that happening.

**Chris Gammell:** So speaking of 20 meters, uh, so, so I was, I was at Hamvention a couple of weeks ago.

**Dave Jones:** You've got a segue for that.

**Chris Gammell:** Yeah, I do. I do. Uh, so that's impressive. Yeah. So I posted a video about Hamvention. I don't know if people saw those videos. Did you, did you end up seeing the, uh, Hamvention videos? It was fun, you know, like walking around and stuff. I don't know. I haven't watched it yet. I don't think we talked about it last week, but, um, I also posted a video of the Air Force Museum. That was really cool. Yeah. I saw a bit of that. That, that. So you,

**Dave Jones:** so you kept saying for an hour on the video,

**SPEAKER_01:** this is so.

**Chris Gammell:** Oh, I know. I know. I kept saying it. It was amazing. Everything's so big there. Um, anyways, uh, so.

**Dave Jones:** Of course it is. It's a bloody, you know, the planes, right? And, and the planes are big. They have to hang them from the ceiling. Of course the place is going to be big. Here's the real thing. I didn't expect.

**Chris Gammell:** I didn't expect that much awesomeness in the middle of Ohio. How about that, Dave? Right. That's the real thing. It's not like.

**SPEAKER_01:** You usually just find cornfields, right? Or something.

**Chris Gammell:** Uh, yeah. Mostly, uh, Dayton is mostly slums. I mean, Dayton's pretty rough area. It's not totally terrible. There's, there's a lot of nice people there, but, uh, you know, it's, it's a, it's an older town. Um, but you know, it's just like, it's just so awesome. So awesome. I highly recommend if anyone's in Ohio, get to Dayton. That is like, it's just like the, it made, it made Ohio that much cooler to me. And.

**Dave Jones:** So you were surprised not to find graffiti on the side of the planes and the things jacked up with the wheels missing.

**Chris Gammell:** No, no, it's, it's an air force base, but it's just, it's just the scale, you know, it's just the scale.

**SPEAKER_01:** So there'd be a modicum of security there. Yes, yes,

**Chris Gammell:** definitely. Many people there that could, although it's a private institution. You're not coming in with those shoes, mate. Yeah. Right. Oh, okay. Yeah. Anyways, where was I going with this? Uh, so Greg Charvat, former guest of the Amp Hour, uh, he had bought, part of the video, we, he showed off this, uh, really cool, uh, radio he got. It was like this 1944 radio, but he, he then did a video recently where he actually hacked the whole thing. He basically like pulled the, uh, VFO signal out and, you know, dance it all around and put it back into a transcee, uh, uh, a transmitter and everything. And he goes over the whole thing. And it's this really cool video where he basically takes this formerly, you know, it's a 60 year old radio that was only for receiving and he basically took it and he uses it as a transceiver now to both send and receive. So if people are interested in, uh, nice. Yeah. Like radio stuff. It, and,

**Speaker ?:** and,

**Chris Gammell:** you know, he does a whole whiteboard thing, kind of like how you do, you've been doing with those Friday videos. So he does like a whole explanation of it. So that it's a good way to learn. So, uh, very cool. And I should say, I really have, I've been, I've been enjoying your videos, the, uh, the Friday ones. If people haven't checked those out, they should.

**Dave Jones:** Oh, the fundamental Fridays. Oh, pressure's on to bloody produce the things. Yeah. I've had this stupid idea for, well, you know, since I started the blog, oh yeah, I should probably do some sort of, you know, regular, you know, I was going to call it building block segments, but one, I, I didn't come up with the name. Some, uh, viewer, sorry, I forget your name, actually said, wrote in and, and suggested fundamentals Friday. And I went, oh, that's actually a cool name. Okay. I've got a cool name for it now. Yep. Let's, you know, and I just went and did it. Now I bloody well committed myself. Yep. Ugh. I'm my own worst enemy. Yep. Really? Well, it's good. So is your venture going to have whiteboard stuff?

**Chris Gammell:** Yeah, it'll have whiteboard eventually. Um, but it'll be, you know, as we go along, you know, like whatever we're working on at that point, it'll be not necessarily as, you know, your stuff is like random, but like really cool. Right. I mean, like this'll be more, you know, fundamental and not fundamental because it was just called fundamental Friday, but you know, like basically as we're working on op amps, it'll be like, that's the theory for op amps right at the time. So that's the idea.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Yep. So a little bit more.

**Dave Jones:** Yeah. Mine are very random. You know, I get people, you know, I keep getting people asking, Oh, can you do everything step by step from the beginning? Well, what am I? A bloody university? You know, I mean,

**Chris Gammell:** right. Right. Right. And there, there's a lot of good stuff out there. I mean, like there's a, I found, uh,

**Dave Jones:** there's already a lot of good stuff.

**Chris Gammell:** There's tons. Yeah. Like Alan, uh, Alan Wolke's channel, right. That's great for RF stuff. And he does a lot of op amp. Yeah. He's done.

**Dave Jones:** Yeah.

**Chris Gammell:** Um, and then every college, every college put in, is putting stuff online now too, with all these open courseware things. I mean, it's great. I mean, you can find so much information, but it's just a matter. I think, I think a lot of people like yours because of the, you know, it's you and your jovial style. Right. Versus, you know, like if it's just someone like, like the Khan Academy, you know, like Khan Academy is cool. A lot of people too. Really? Oh, okay. Oh, you just mean you.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. One here too. Yeah. You pissed me off too. People either love me or hate me. I had somebody say that. Why don't I make my fundamental videos like, just like Khan Academy. Khan Academy is so professional and everything.

**Chris Gammell:** Yeah.

**Dave Jones:** Like, geez, well, there's no personal face behind the Khan Academy.

**Chris Gammell:** It's like, yeah, there's, there's a style.

**Dave Jones:** I'll hire a professional voiceover and, you know, like, yeah, no, my, my videos are personal, you know, you get to, you know, know who's delivering. You get to, you know, exactly.

**Chris Gammell:** There's, and there's, there's a, there's a, there's a person. There's something about like the, the, you know, not saying your stuff's grungy, but like, you know, like there's, there's always a real aspect to like the grungy side of things. Right. So like, it's grungy, you know, like a Jim Williams type of, you know, when you see like his, you know, his bodged together circuits and then, you know, as he builds them up or, you know, like the Bob piece stuff and, and seeing that kind of stuff. I mean, like that's just, it's just real. It's just how engineers work. You know, it's like, if you want to dress it up, then go on it like a discovery channel show or something, you know, like with produce segment producers and all that crap. It's like,

**Dave Jones:** can you imagine like if say the Bob peas, you know, peas is porridge column. You, you didn't know who, who he was. You didn't know where he was from. You would never seen his photo. And all you had was this faceless, nameless person writing this stuff. Yeah. The, the, you know, the writing would still be cool, but you'd, you know, you wouldn't get the sense of the personality. Exactly. You know, you wouldn't, you know, you don't get that personal attachment to the person. And doing it. Yeah. It's just not,

**Chris Gammell:** you get more into it. You know, like, yeah, exactly. Well, and that's, and that's just a human characteristic, right? I mean, like humans like being told stories, right? It's just part of our history. It's part of how, you know, communication has been done. And it's the same thing with personas too. I mean, like, like Bob and Jim Williams and everyone and you, you know, it's just personas. People relate to personas as, you know, instead of just faceless entities, right? Like, like I couldn't pick out Sal, Sal Khan on the street, you know, like he's, he's done good stuff for education, but that's right. I don't know who he is. And so that's the difference. That's right. Speaking of,

**Dave Jones:** it's a personality thing. People like to like personalities.

**Chris Gammell:** I agree. Or hate, like, and hate, I think.

**Dave Jones:** Or hate, of course. Like, yeah, I get regular hate mail.

**Chris Gammell:** It's great. Oh yeah. It's hilarious. Exactly.

**Dave Jones:** Like, yeah, so somebody emailed me like just yesterday and said, yeah, why don't you do a basic op amp fundamentals Friday, you know, completely from the beginning. And I've searched Google. I can't find anything. There's nothing out there. It's like,

**Chris Gammell:** keep searching.

**Dave Jones:** Your Google search skills suck. Keep searching. You know, like, goodness. Yeah. Anyway.

**Chris Gammell:** Speaking of, uh, Bob Peace. Uh, so we had talked about that, uh, artsy PCB program that you, you didn't like previously where, you know, you did like, does like artsy PCBs after you put in. Uh, it's called bold port.

**Dave Jones:** artsy, right. PCBs. Yeah. Right. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** He's taken the, uh, so he, he took his software and then he also ended up developing this, this little test coupon for a Bob Peace circuit. And it's, and it's like hand drawn. And I just thought it was really fun with the, uh, so it's, it, you know, it's got like a piece quote on and everything, but it's got like a hand drawn schematic alongside. It's just a really cool idea for, uh, you know, having, uh,

**Dave Jones:** silk screen in Bob pieces, trademark, convoluted schematic style.

**Chris Gammell:** Yeah, exactly. It's, it's, it's, it's scratchy. And yeah, I think, I think the boards are coming in soon. So people can, uh, people can get those. I'm not sure what the circuit actually, it's a, it looks like it's just a little amplifier circuit. LM311. So,

**Dave Jones:** right.

**Chris Gammell:** Yep. Pretty fun. LM311. No, it's a 331. Sorry. It's a comparator. Yeah. 331. It's a, no, no, sorry. Volt is to frequency. Yeah.

**Dave Jones:** 741. How about that? You remember that one?

**Chris Gammell:** I remember that one, Dave. Yeah.

**Dave Jones:** I never got,

**Chris Gammell:** so like a lot of people, you always see this in the, in the, the, you're an analog guy. Oh, shush. Uh, so the voltage to frequency stuff, I never had to do that though. Like people always did that for, I always see like the Jim Williams app notes for these kinds of things too. They did it for like, you know, going over isolation barriers, right? You know, you, you take a voltage, you translate it from a voltage to a frequency, and then you push it over like a transformer, right? You always see that kind of stuff. And it's like, you don't need it these days, you know, like just optos are so much cheaper. You can get digital isolators, you know, like just, there's tons of other options for that kind of thing. And if you look at it from an analog perspective, everything's hopped over the isolation barrier, right? So whereas before you had, you know, one micro talking to, you know, 15 different analog, analog to digital converters on the other side of, of an isolation barrier. Now you just throw a micro on the other side too. And it's just a local, right? You do local processing. That's just the, the transition of cheap micros these days, right? I mean, it's just, you, you see them everywhere. Everybody's pushing them into products too. And it's pissing me off. They're playing. I, I was pissed. I keep talking to these vendors about it. I'm like, you're going to be out of a job? Okay. That's a, that's a different thing. Cause I do, I do yell at vendors because they, you know, they keep pulling in, you know, I've talked about that before. They keep pulling in, uh, you know, analog functionality, right? And, and that's okay, right? It makes my job easier. And I can do a lot of, a lot more, but no, now they're always throwing in, uh, micros, right? For like local processing stuff. And in like their charge, they want to, I get it. They want to charge more for parts, right? They want to have, you know, two A to Ds and a micro that, you know, then talks over ethernet or something for like, you know, for like local processing. But, you know, if I'm trying to use it just as an analog to digital converter, then I have to go and program that micro. Whereas before I could just talk to it, you know, with a single micro. And it's like, you know, trying to get, trying to shoehorn new electronics and old electronics, uh, into old applications is always a, a difficult thing.

**Dave Jones:** Yeah. I can't picture you screaming, you know, uh, shouting at an, at a, uh, sales guy. I can picture you sitting there with them, sipping a cup of tea going, now, I really don't think that, well, I, I think it may be better if you do it this way. You're not the, I'm that whiny in your head,

**Chris Gammell:** I'm just a, uh,

**Dave Jones:** right. Yeah.

**Chris Gammell:** Okay. Thanks Dave. That's, that's good to know.

**Dave Jones:** I can't picture you there thumping the table. No, I don't thump the table, but I hate this shit. This, these chips are, why don't,

**Chris Gammell:** that doesn't get through to anyone. I, I'd rather be someone that they come back to and ask, it does ask that. No, it doesn't. Believe me, it doesn't. I mean, yes, what they'll do is they'll write you off, right? They'll say, oh, this guy hates us or this guy, you know, doesn't want this part and we should just, just not go. You know, if it's like a specialist again for, you know, analog to digital converters.

**Dave Jones:** they don't annoy me anymore. You know,

**Chris Gammell:** that's true. Yeah. But you know, if it is something that I'm interested in, I want them to come and ask me the next time because I want to tell them exactly what I want in the next generation of parts. I, I always take those meetings because, yeah, I want to, I want to affect that stuff. I want to make my job easier. You know, like that's eventually they all start, you know, calling you and asking what you want in the next generation of parts. It's like, sure. At certain points, I'm like, yeah, do my job for me. That's fine. You know, pull it, pull it more functionality. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Because, you know, then you usually get to cost savings and power savings and everything else too. Right. You got me all worked up, Dave. And then you insulted me. I'm, I'm marginally, upset. Sorry. You're marginally insulted. I'm marginally upset. That's how I respond normally to vendors. I'm like, oh, this is, this is upsetting.

**Dave Jones:** I just think you're a bit of a pussy. That's all.

**Chris Gammell:** I, I think of myself as a,

**Chris Gammell:** I think of myself as a, even tempered, uh, nice person. Well, maybe not nice, but even tempered, uh, amicable customer. How about that? Right.

**Dave Jones:** Right. With tact. Cause that's one thing I lack. Yes, you do. Yeah. I have none. That's okay. No, I tell it like it is. And I expect people to treat me the same way.

**Chris Gammell:** I would be interested to know if, I mean, I'm just guessing about that. You know, if the, if vendors actually, I don't know. I don't think they would say they respond better. Cause who wants to get yelled at? Right. But you know, if you actually like did a study somehow, like,

**Dave Jones:** no, don't yell, but yeah. Like,

**Chris Gammell:** like if, if you and I were trying to get the same point across,

**Dave Jones:** if you tell them something sucks, right?

**Chris Gammell:** Oh, I'll tell someone something sucks.

**Dave Jones:** There's nothing wrong with telling them something sucks.

**Chris Gammell:** Right.

**Dave Jones:** This part sucks ass, you know? Why? Okay. I'll tell you why.

**Chris Gammell:** Oh yeah. I'll say that too. But usually I wouldn't say sucks ass. I mean, you know,

**Dave Jones:** right.

**Chris Gammell:** Actually be a little nicer about it, but again, maybe that's a cultural difference. Maybe Aussies are just a little more brash.

**Dave Jones:** Could be, or it could be just me. Could be. Yeah. Yeah, we are.

**Chris Gammell:** A little more brash. Here in the Midwest, we're a little, we're a little calmer from eating carbs.

**Dave Jones:** I don't take things personally and I don't expect others to. Right. Oh goodness. Can we talk about something technical? We have been,

**Chris Gammell:** but yes, we can.

**Dave Jones:** Yeah, kind of. What do you want to talk about? Let's go to the other extreme from the LM3.

**Chris Gammell:** You mean the amp amp or the amplifier that's a 331? Yeah.

**Dave Jones:** Bob Pease rolling over in his grave.

**Chris Gammell:** I'm sorry, Bob. I didn't mean to. Anyways.

**SPEAKER_01:** Oh goodness. Terrible.

**Dave Jones:** Anyway, I, I linked to a, um, data, uh, an application note. Here we go. I'll, I'll send it to you. Have you, have you, I've seen it. Yeah.

**Chris Gammell:** This is the Altera one.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. So it's through Eweb, but it's, it's an Altera app note.

**Dave Jones:** It's an Altera app note. And, um, it tells you how to lay out your board and design to get a hundred gig bit, uh, serial interface working on this Stratix five GT FPGA, right? One of these, you know, thousand dollar FPGAs.

**Chris Gammell:** Yeah.

**Dave Jones:** One of these huge high end ones. And it's like, you know, and it's like, you look at this sort of stuff and you go, holy shit, you know, and it's telling you, Oh, here's the example layer stack up for the board. It's only 20 layers. You know,

**SPEAKER_01:** it's so easy.

**Dave Jones:** Oh, it's so easy. It's only a 20 layer board, you know? And it's like, and, and yeah, you know, if you follow these app notes, right? Yeah. You know, any schmuck who can afford to make a 20 layer board can probably get one of these hundred. Afford to test one of these boards. I mean, that is working.

**Chris Gammell:** That is the cost.

**Dave Jones:** And you can afford to test it and afford to get the right connectors and everything else. you know,

**Chris Gammell:** right.

**Dave Jones:** And, um, and you go, you know, and you take this shit for granted and you just think about the people who actually developed this, you know, and, and made it, you know, meet all the tolerance margins of, for the standard, for the hundred gig bit standards and all that sort of stuff. And, Oh,

**Chris Gammell:** man,

**Dave Jones:** it's just, it's,

**Chris Gammell:** it's actually, it's four parallel. As you said, test it. Isn't it? I mean, like these are, it's, is it actually a hundred? I thought it was a hundred.

**Dave Jones:** Oh, right. Oh, okay. Yeah.

**Chris Gammell:** It says four by four by 20, 28. I think 28 is the, the,

**Dave Jones:** four by 28 gigabits is the actual data throughput. Yeah. But 20, I mean, it's not like,

**Chris Gammell:** it's not like 28 gigabits is like, Oh, well only 28. Oh, okay. Get out my crappy, you know, eye diagrams and all this.

**SPEAKER_01:** Oh, I'll just get my tech TDS 2. Yeah. Let's go. Exactly. I can measure that. Yeah.

**Chris Gammell:** No problem. No. Yeah.

**Dave Jones:** I see. I, you know, I've done like a 10 gig bit one before, and I've analyzed the bit error rates to, you know, on a 10 gig bit per second serial link to an FPGA. Yeah. You know, that was sort of, you know, black magic enough.

**Dave Jones:** you know, it's just, eh.

**Chris Gammell:** Well, we should, we should refer people to the, if they are interested in this black magic kind of stuff too, go back and listen to the Howard Johnson interview when he was on the Amp Hour as well. Yes. That was, yes. He's, he's all about this kind of stupidly fast stuff. I mean,

**Dave Jones:** yeah, yeah. They said, well, he was on the, he was on the standards committee for the ethernet 10 gig ethernet standard, and maybe the hundred, gig bit one as well.

**Chris Gammell:** Yeah.

**Dave Jones:** Perhaps. Well, and anyway, he was on the standards committee developing this sort of stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** Was that him? I thought that was someone else. Yeah, yeah. No,

**Chris Gammell:** I think he was, I just, it's been a while. Someone else. I was listening to a show from two weeks ago. I was trying to find something from a show two weeks ago and has listened to us. And I'm like, I said that I, I don't remember anything that we've talked about. Everything I've said so far in the show, I have likely will forget about. So. Yep. Yeah. Absolutely. Absolutely. Yeah. That's the nature of this new project I'm working on. It just, it just blurts out. No. Yes, I did. I told you at the beginning of the show.

**Dave Jones:** Oh, right. Did you? Oh, right. Oh, the new, I thought you meant physical project. Right. Oh, no, no. Yeah. Right.

**SPEAKER_01:** That was just jokes. Yeah. He's got 10 plus years on me. He's getting a little older folks. So, yeah.

**Dave Jones:** Yeah. 10, I think it's more than 10. Yeah, probably. Young whippersnapper.

**Chris Gammell:** This stuff though, if you ever, so did you, when you, when you had to do the layout for this kind of like this 10 gig stuff or like this shows 28 gig stuff, did you have to do like the detection side or were you just, just looking at the eye diagrams, making sure the, the signal integrity made it through, like the signal made it through. Like how, how were you testing it? Oh,

**Speaker ?:** no,

**Dave Jones:** well, it was the two pronged. Well, the two pronged, there were the eye diagram stuff with the high end scopes, but there was, um, to do the bit error rate stuff. That's, um, tools actually provided for the FPGA to, um, that actually taps into,

**Chris Gammell:** uh,

**Dave Jones:** like it's a plugin you get in your VHDL and you, and you can tap into the, um, uh, transceiver. Yeah. The actual, you know, the 10 gig bit transceiver on the FPGA die, and you can extract the raw data out of it. And they've got a, you know, a PC application that then can, you know, decode all that. And, and you just leave it there running for days and days and days, and you can get the bit error, you know, the average and peak and, and whether or not it meets the standard, and all this sort of stuff. So there's, you know, tools built in and, but everything's tweakable, you know, so you have to learn how to tweak the thing for your exact requirements. Oh, and you can ruin the whole thing and get results. You know, you can make anything pass, right? By tweaking, right. You can go, Hey, yeah, here's all my test results. The bit error rate, perfect. And then the temperature changes by one degree. Of course you just, yeah, yeah. Yeah. And, and here I was actually blowing on the chip, you know, to see if it would change the bit error rate or get the freezer spray can out or, you know, the air duster and turn it upside down and, you know, freezing the chip and see what it does to the bit error rate. You should, you should explain that test too. So that, uh,

**Chris Gammell:** in case people have never heard of that, the, uh, the air, the air tester thing. There's likely people that have never done that, right?

**Dave Jones:** Oh, right. If you don't, you, you, you don't need a can of freezer spray in your, what are you talking about physically using the air dust? Yeah. Yeah. Well,

**Chris Gammell:** I just meant in general too. So people, what Dave's talking about is that, you know, dead to temperature test, you don't just heat it up, but you also cool it down. So you can use like a hot air pencil to heat up a chip package and then you can cool it back down with it. There is just a freezer spray, but then if you're out of that, like Dave's saying, you can, uh, you use like a, uh, canned air kind of thing.

**Dave Jones:** It's your air duster and turn it upside down and then all the Freon or whatever the stuff comes out.

**Chris Gammell:** Yeah. Texafluor or whatever the hell it is. Yeah.

**Dave Jones:** It cools your chip down and yeah. So it's, it's that sort of techniques usually for, um, fault finding, you know, to thermally shock a component to just to see if, you know, if something happens, you know, so you can, and you can find dry joints and stuff that way as well. So I've never done that. It's a common, it's a common repair technique. For dry. Oh yeah. That's a very common repair technique. Huh? Yeah. Yeah. What is it? What is the behavior manifest? You thermally stress that joint and it can, Oh, well, if you've got like a, a dry joint, that's just touching. If you thermally stress it, well, you know, metal expands when you stress it and boom, the joint pops open. Oh,

**Chris Gammell:** really? Okay. So it's like, so you can, it's like a turkey.

**Dave Jones:** So you can make your fault come and go.

**Chris Gammell:** Oh yeah.

**Dave Jones:** It's a, yeah. So if you've got a thermally, you know, it's like, it's common. If you've got something, a fault, which fails, you know, like after you've switched it on for an hour, then, well, you know, there's some sort of thermal stress thing happening. So you might go around and selectively freeze stuff with your freezer spray to try and find the culprit, try and crack it down, try and actually track down the culprit. Yeah.

**Chris Gammell:** Yeah. I've done that for the,

**Dave Jones:** speaking about the anal retentives before.

**Chris Gammell:** Yeah. You've, you've done it for what? Oh, I was just going to say, I've only done, I've only done the freezer spray stuff just for like the actual body of the package, not necessarily for the, for the, you know, the pin, the pin separation stuff. So, so anal retentive though. Sorry.

**Dave Jones:** Or you can find dry joints on, you know, you can find bad joints underneath pain in the ass BGA chips and, you know, stuff like that. Oh, that's good too.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. Yeah. Anyway, anyway, speaking of anal retentives way back in the episode, I do actually remember that we were talking about, you know, people complaining about, Oh, that's not theoretically right. You know, and, and then, you know, I mentioned this on a video, you know, using the freezer spray can as a troubleshooting technique. And, Oh, a bunch of people came on. Oh no, that's not right. You don't do that. And it'd be a blah, blah, blah. And here's why, blah, blah, blah. And it's like, dude, it's a standard technique that's been used for 50 freaking years. Yeah. You know, like, you know, tell somebody who cares. It can give you false positives,

**Chris Gammell:** but it's not a reason not to do it. Right. That's, that's the main point. Oh yeah, of course. You know, like, you're spraying something all day and it cools off, you know, it cools down and heats back up and everything. It's like, yeah, you could affect some behavior, but if that's all you're doing anyways, you're not troubleshooting properly in the first place. Right. It's like, you have to go and do other stuff then either reflow the chip or, you know, start actually testing traces, you know,

**Dave Jones:** and you've got to know what you're doing and you've got to know what the results mean. And you've got to, you know, but in experienced hands, you know, there's nothing wrong with doing it.

**Chris Gammell:** Right. I agree. I agree. So, yeah, it's a good starting point. Yep. Getting you. So with this, this transceiver thing.

**Dave Jones:** Maybe that should be a segment in your project.

**Chris Gammell:** That should be a segment in your project. Cooler spray.

**Dave Jones:** Yeah. Like trouble. Yeah. It will be. Thermally stressing. It's fun. It is. Yeah.

**Chris Gammell:** No, that's, it's a, that's all, that's all going to be in there, buddy. See, I'm always coming up with good ideas for your new project. Yeah.

**Dave Jones:** There you go.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, speaking of transceivers, sorry. What, what, what, what the hell are we talking about?

**Chris Gammell:** My only experience with these has been trying to get them. I've used, I think that, I think a six gig one before. And, and because. Right. They actually don't like auto lock onto like, you know, like how, how like the serial signals come in and they, they, the serial deserializer or SIRDES as they're referred to. I didn't realize when I started this project was, was like, you, you know, you basically key on a certain pattern coming in and then basically you lock to that. But there's like, Oh, there's all these like variables you can have for actually locking to the signal. And. Oh yeah. And I didn't have any kind of visibility to the actual signal. So I didn't know, you know, like, you know, like you can, you can, you can get false positives for, you know, like if your signals flopping around all over the place, you can get, you can get one zero one sometimes.

**Dave Jones:** And you'll actually start talking about. You can. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** That's why I said, yeah, you can tweak all these variables, you know, in all these registers, you know, these SIRDESs have, you know, some of them have, well, I can't remember exactly, but they might even have hundreds of registers that you can set up, you know, to, to do and, and, uh, you know, and actually detect and lock onto various things and do all sorts of stuff. It's just,

**Chris Gammell:** it's crazy.

**Dave Jones:** Absolutely phenomenal.

**Chris Gammell:** It's yeah.

**Dave Jones:** And, and, and hundreds of configuration bits, you know, and once,

**Chris Gammell:** once you get it, you're just like, don't touch anything, you know?

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Like that part of a project where if it's like,

**Dave Jones:** so you, so you load up like the, uh, yeah. So you load up like the bit error rate, uh, test program, you know, that comes with the, you know, the Altera or the, uh, Xilinx, uh, chip, you know, and it comes with all these default values for these hundreds of registers and you go, right, I'll start with that. Thank you very much. If you had to read the data sheet and figure out, what each bit in each register did, and then set them all up from scratch, you could spend a week doing that, you know, easily, like seriously, just trying to figure out and understand it all. And just a week, you know, people don't understand eight hours a day for a week, just trying to figure out what your registers should be, you know, and learning all the, all the little intricacies of that SIRDES or whatever. Well, it's like that with lots of stuff.

**Chris Gammell:** I mean, it's not just a SIRDES, right? I mean, it could be, you know, you know, just learning a new processor too. Like that's, that's why people stick with processors. They know when they're doing new projects, they, they don't want to, that you have a, you have a board support package that works, you know, or you have, you have a default project that works. Yeah. Yeah. Hell yeah. I'll pay 10 bucks for a chip just to not have to start at the beginning again. Right.

**Dave Jones:** Exactly. And that's how engineering works, you know? Yeah. Often, you know, you're not going to spend that time to choose the most optimal device. You're just going to go with what you know.

**Chris Gammell:** Yeah. Path of least resistance, just like current.

**Dave Jones:** Yep. Yep. Which you were wearing on your t-shirt in the first video you did.

**Chris Gammell:** Yeah. Oh, the, the, the resistance is futile.

**Dave Jones:** Resistance is futile. Yeah. T-shirt.

**Chris Gammell:** Yeah. If less than one of them. Yep. Yeah. Those are fun.

**Dave Jones:** Right. I've, I've now, I'm now keen to see your revised video. How, your first video was eight minutes. How, how long is this?

**Chris Gammell:** It was 10 minutes. It was, it was worse.

**Dave Jones:** 10?

**Chris Gammell:** Yeah. I'm making it.

**Dave Jones:** I advised you to keep it under five. Oh yeah.

**Chris Gammell:** I'm going to,

**Dave Jones:** I'm going to make you listen to the wise old man.

**Chris Gammell:** Yes. I'm, I'm listening to the guy that, that regularly does 30 minute videos after saying they're going to be 10.

**Dave Jones:** Yeah, I know. Yeah. I know. I'm the master. I am the master of waffle.

**Chris Gammell:** Yeah.

**Dave Jones:** I am the waffle master.

**Chris Gammell:** Yes.

**Dave Jones:** But I, but I know the value of a good.

**Chris Gammell:** Right. Do as I say, not as I do. Right.

**Dave Jones:** Introductory video. Right. Yeah, exactly.

**Chris Gammell:** Yeah. Yeah. Yeah. So you get,

**Dave Jones:** if I was doing that, I'd put serious work into putting, getting that video to three minutes long.

**Chris Gammell:** Yeah. I plan to know. Or five tops. Well, I have a whole day until this air. So by the time people see it,

**Dave Jones:** you've already,

**Chris Gammell:** remember it won't air till tomorrow. So we're speaking for the past right now for everyone listening. Oh, so there may be a three minute video by now.

**Dave Jones:** Right. Yes, we are.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Cause this is not live. We actually have quite a few people continuously ask us,

**Dave Jones:** why don't you live stream the show?

**Chris Gammell:** Yeah. That'd be terrible.

**Dave Jones:** The radio show. And it like, it wouldn't be any difference. It's because it's like, it's not like this thing's really edited. You know, there's only, we rarely edit this thing.

**Chris Gammell:** Yeah. Only when there's.

**Dave Jones:** It's pretty much just, you know, I trim the start and the end and only if there's a reason to. Yeah.

**Chris Gammell:** There's lots of noise or something like that or big coughs.

**Dave Jones:** Something like that. But generally, no, we're not going to go in there and, you know, heavily, this thing is not generally, you know, we, we, we shoot for a single take. So we record the whole hour and that's what we dump. Yep. Basically. So, yeah. So there's no advantage to listening to it live. Sorry. It's just boring. Just like our regular show. And on that note, we're an hour and 10 minutes in.

**Chris Gammell:** Oh, that's nothing for us. Well,

**Dave Jones:** we don't want to make it a Jerry length.

**Chris Gammell:** Oh, definitely not Jerry length. That was, that was a long, that was our longest show yet. So it's a,

**Dave Jones:** is that kind of the equivalent to the Smoot?

**Chris Gammell:** The Smoot? Oh, like our, is our measurement unit. Well, everything would be less than one then, right?

**Dave Jones:** The length of measure. Yeah. All right.

**Chris Gammell:** Uh, I don't think we have a standard measure yet. It would be like a, if we had like standard measure of like one rant.

**Dave Jones:** Of course we do. It's in the name of the bloody show. It's the hour.

**Chris Gammell:** Yeah. Yeah. I guess that would be the measure. Yeah. Hello. McFly. Yeah. Oh dear. Uh, so we should do rapid fire lengths because that's always fun.

**Speaker ?:** because,

**Chris Gammell:** because I have so many, I was looking at, so from two weeks ago when, when we had our last just you and me show, we had 40, I, I, we posted 45 links,

**Speaker ?:** 40,

**Chris Gammell:** 45 links. Wow. That's a lot of links. Well, so mostly people can just go to the, uh, the, uh, amp hour subreddit. That is the best way to see all the links. So we won't necessarily, uh, subject everyone to all that stuff. But the one thing I wanted to,

**Dave Jones:** and you can vote on stuff before the show.

**Chris Gammell:** Yeah, that's important too. So sign up for Reddit. You can, you can vote for the,

**Dave Jones:** but we generally ignore it, but you can actually vote, vote for them. Yeah.

**Chris Gammell:** Well, and you can, if you, if you're a Reddit user, you can throw it into your feed too. So, you know, it'll show up as a, as a, uh, a regular story on your front page. But, uh, yeah, what were some of the things that were pretty cool this week? Um, of course I can't find them now. No telling the story. Yeah, there, there was a, uh, there, so there's a, there's a podcast I don't think I've mentioned before, but it's called an innovation hub. Um, it's out of Boston. I may have mentioned in the past, but, they did a cool show about, uh, about robots. It was actually an onstage live show that I wanted to link in. And also, you know, just tell people about the podcast. So it's called innovation hub. There's a robot, uh, podcast that was really good. A lot of Boston's real strong on robotics. So they, they have that as a topic once in a while, but lots of good stuff on that show. Um, and you know, I'm always on the lookout for new engine engineering, uh, podcasts and they're still relatively sparse. So, uh,

**Dave Jones:** we don't mind competition. No,

**Chris Gammell:** I keep hoping people will promote you.

**Dave Jones:** If you've got a, uh, competing podcast, we will promote you. Yeah. How, how nice are we?

**Chris Gammell:** Yeah. I just want something to listen to. So other than us, that's just awkward. Right.

**Dave Jones:** Yeah. I know we're bored as bad.

**Chris Gammell:** Rolling down the street with my windows open. It's like listening to myself. I'm really plugging our own show. Yeah. Yeah. Right. Yeah. Uh, I had a question for the audience too. So, uh, someone, I was talking to someone about Eagle 6.4 and I was looking at the, the recent specs for it. Um, so that was, that was released like at the beginning of this year, beginning of 2013. And there's something that says it can interface with LTSpice, LTSpice rather. Yes. I haven't, I've, I've never, I've never tried that, but I, cool if it works. Yeah. I was wondering if anyone has tried that or if it works. Um, um, so I, I'd just be really interested in that. I mean, Eagle obviously has been continuing their development and, uh, so that's, that's really, that's a really cool feature. So I really liked that. And I, I hope that works. Um, just want to tell people about it too, if it didn't.

**Dave Jones:** I, I can't say it, working out of the box as such though, unless there's a matching model in, you know, let's say you put an LM seven, four, one.

**Chris Gammell:** That's the, uh, that's the one that, uh, shakes. It's a motor, right?

**Dave Jones:** Or an LM.

**SPEAKER_01:** Yeah, that's it.

**Chris Gammell:** Yeah.

**Dave Jones:** Or an LM three, one, one, you know, like, um, you know, they may not have that part in the LTSpice standard library. So how does it match up when you import it? You know, yeah, you know, R's and C's, and your passive parts. Yeah. It's, it can just pull in a generic model for those, but your chips, well, you know, it's got to be in the library. So I'd be very surprised if it works out of the bag, but at least you can actually import most of your schematic, right? And then you can just manually, if you have to, you make the connections, choose the model you want for each chip. And you know, yeah. So you can save a, save a fair bit of time there. So yeah. Yeah. And then you eliminate the error in draw, in drawing the schematic as in, in redrawing the schematic.

**Chris Gammell:** Right. Yeah. And that might be what it mainly is. I mean, if people look at the actual net list, you know, if you drag a net list into a text editor, you can usually see, you know, node names in both, you know, in, in older, some of the newer CAD programs don't necessarily show you the net lists, you know, they're like database based, but, um, you know, if you have an older net list, you actually see, you know, R1 is connected to these two nodes and you know, that, that translates to spice as well. If you know, that's how spice work originally started was just a spice engine. Well,

**Dave Jones:** and that's how it still works under the, under the covers. Of course. You know, yeah. The, the gooey schematic interface just generates a net list, which goes into the spice engine, you know, the 30 year old spice engine. Right. You know, I mean,

**Chris Gammell:** yeah. Yeah. Young, young whippersnappers that have never used the text editor wanted. Been frustrated. Right. Draw your schematics. If you're using just a spice engine, that is the key. Go draw your schematics, label each node. That is the only way you will get it right. I promise you that.

**SPEAKER_01:** Oh dear. Yeah.

**Chris Gammell:** All right. I think, uh, I don't know. There's tons of other stuff, but, uh, yeah,

**Dave Jones:** come on. Let's just, what? You want to keep going? Leave on a losing note. No, let's just quit on a losing note. Oh yeah. No, that's okay. Yeah. Check it,

**Chris Gammell:** check out the subreddit. Uh, Oh, and also if people will, uh, if there, if people are interested and if you like the show, one great way to support us is, uh, give us iTunes reviews. Uh, we, I just dressed up the iTunes page and it did fall, fell behind in the, in the past. But, uh, if, if people like the show, if you can give us a review on iTunes, that really helps us a lot. So we would really appreciate that. Yes.

**Dave Jones:** Thank you very much.

**Chris Gammell:** All right. Well, next week we will have, uh, James Neal, also known as Lane of OS, OSH park or OSH park, uh, the purple PCB service. And he'll be on the show. We'll, we'll post a, uh, uh, something on the subreddit as well to ask questions to him. So looking forward to that.

**Dave Jones:** Awesome. All right.

**Chris Gammell:** See you next week, man.

**Dave Jones:** Bye. Bye.

**Speaker ?:** Bye. Bye.

**SPEAKER_01:** Bye.

**Chris Gammell:** This episode was sponsored by club. Jame co upload your project brief today. And if approved, you'll get a 10% off coupon. If chosen by the community, you'll make 10% off any kit sold without ever needing to buy or bag components. Go to clubjameco.com slash theamphour to find more details and to support the show.
