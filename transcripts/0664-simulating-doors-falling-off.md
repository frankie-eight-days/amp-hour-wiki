---
episode: 664
title: Simulating doors falling off
url: https://theamphour.com/664-simulating-doors-falling-off/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released April 3rd, 2024. Episode 664. Simulating doors falling off.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** With absolutely no idea what we're going to do for today's show, as usual.

**Chris Gammell:** Yeah, yeah. What do you got, buddy?

**Dave Jones:** I got nothing. I thought you had something.

**Chris Gammell:** I mean, I've been getting ready for Embedded World. That's next week. Oh, right.

**Dave Jones:** Okay, yep. That's in Germany.

**Chris Gammell:** 3D printing up a storm. That's right. Yeah, I'll be going to Nuremberg.

**Dave Jones:** 3D printing those one-off jobbies, right? That's right. Exactly. Trade show stand.

**Chris Gammell:** That's right. Yep, yep. A lot of that. And rediscovering the horrors and joys of FreeCAD, of course. Right.

**Dave Jones:** No thanks.

**Chris Gammell:** Yeah.

**Dave Jones:** I've heard the horror stories. I don't want to go there. I actually tried it once. I did try it once. And I went, what the hell is this thing? No. No. Just like you can really get it. Like within 5, 10 minutes, I can tell if I'm going to like a CAD package. It's not, you know, I don't have to spend long with it to realize, oh, yeah, okay, this is working the way, you know, I'm getting a good Spidey sense from this. And it's like FreeCAD just did not do that for me at all.

**Chris Gammell:** So it's a little rough around the edges for sure. But I mean, like, I don't know. KeyCAD doesn't, it doesn't pop at the beginning. It's getting a lot better. It's getting a lot better. Right. Have we talked about 8 since it came out? Since 8 was released?

**Dave Jones:** I think we mentioned it. Yeah.

**Chris Gammell:** Yeah, we probably mentioned it.

**Dave Jones:** But I don't think you had started using it or something. I still haven't. Yeah, no. Right. Okay. Some videos of it. Some people talk about it on the forum. That's about it for me. I've just seen various things. I haven't tried it.

**Chris Gammell:** I am not what they call an early adopter.

**Dave Jones:** You used to be Mr. KeyCAD. I know. Yeah.

**Chris Gammell:** I used to be Mr. Had Free Time in my life.

**Dave Jones:** You were so embedded in that community. It was like.

**Chris Gammell:** I mean, I'm still around. But yeah, I'm not like.

**Dave Jones:** But no, you were like one of the key.

**Chris Gammell:** Not running any conferences these days. No, no, no.

**Dave Jones:** You were running conferences and crap. Yeah.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah. Yeah.

**Dave Jones:** There you go.

**Chris Gammell:** Life changes, Dave. I don't know. Maybe you've noticed this in your own life. That you have a slightly different MO than. You've got kids now. 10 years ago.

**Dave Jones:** Yeah, exactly. Yeah. Things have slightly changed. Just a tad. Slightly changed. Yeah. Slightly changed. Yeah.

**Chris Gammell:** I did a demo on Friday of a thing that I was working on. I've been doing some Bluetooth stuff. Have you ever done Bluetooth? I guess you did with your meters, right?

**Dave Jones:** Yeah. With the meter. Yeah. That was a pain in the ass. Yeah.

**Chris Gammell:** I don't know anything about Bluetooth. I was like, oh, well, I've used Bluetooth. But then you start looking at. I'm like, I didn't. Do you know there's standard messages in Bluetooth?

**Dave Jones:** Oh, I don't. I don't know to that level.

**Chris Gammell:** Okay.

**Dave Jones:** It was my psychic was working on that. Oh, right.

**Chris Gammell:** Yeah. David. David too, right?

**Dave Jones:** David too. Yeah. Yes.

**Chris Gammell:** Yeah. And so I'm sure David too didn't do this. But you can use standard. So there's an HT. I don't even know if it's a protocol. It's probably the wrong name. But one is HT for health temperature, I think. Oh. And so when you have a Bluetooth device that is like a thermometer, like whatever, and it's bleeping out your Bluetooth, it's like a standardized packet. Like it's like some, I'm guessing Bluetooth SIG, like the standards body defines it. And there's other ones too. And like, so if you go, so like my exposure to this is very, very limited, where it's basically me digging through the Zephyr demos, which is, you know, fine. That does it. It's like, you can kind of just see what's in there. And then those are like the well-defined ones. So like peripheral health temperature, HT. And then there's another one for like heart monitor, heart rate monitor. But I don't know what that one is. Right.

**Dave Jones:** So they have sort of like, right, pre-built in for the early apps they thought that it would be used for and stuff like that. Yeah.

**Chris Gammell:** I think just the really common things. Yeah. I think it has evolved over time too, to like make some level of.

**Dave Jones:** Well, they've pushed it a lot further, I think, than what they, don't quote me, but because I don't know.

**Chris Gammell:** What was your first Bluetooth device, Dave?

**Dave Jones:** Oh God.

**Chris Gammell:** What was the first Bluetooth device you encountered?

**Dave Jones:** Oh, well, not me. Well, not that I use personally, because I was probably a late adopter, but I can remember one of my geocation friends used to work at Microchip. He used to work at Microchip, but he was a local guy here. And, you know, when we'd meet up for, you know, we're having dinner and he had this blue flashy thing in his ear. And I'm going, what the hell is it? Oh yeah. What is this blue flashing letting your ear? I'm talking like 2000. Mate, I'm probably 2002, maybe. Really? That is really, yeah. When did Bluetooth first come out? Oh, I need to know the timeline now.

**Chris Gammell:** I have only one. I have my reference point where the first time I encountered it, where I was very confused about what it was.

**Dave Jones:** Right. 1998. 7th of May, 1998. Wow. Yeah. Okay. Yeah. So it would have been probably 2001 maybe is when I first saw somebody use a Bluetooth device. And it was, yeah, he had this little earbud thing. And I think it might've even been a wireless like headset back then or something. And it was hooked into his new phone. I don't know what sort of, you know, he probably had a newfangled flip phone or something, right? Because there were no smartphones back then. But yeah, I can remember that he would, yeah, it would actually beep and it would flash. It was this bright blue flashing lead in his ear. That was the thing that got you, huh? It was like right in your face. It's so distracting. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Oh, and it was so weird at the time. Like, well, I did that. That would be weird now if you had a blue flashing lead in your ear, right? That'd be weird even these days, right?

**Chris Gammell:** I have flashing leads in my ear right now, Dave. My Bluetooth headset is flashing. I mean, it does like-

**Dave Jones:** Yeah, but I've got wireless ear, you know, I've got the Apple fruity wireless earbuds, but they don't flash. There's no leads on them. Those don't flash anymore.

**Chris Gammell:** Oh, my- That just totally pisses away power.

**Dave Jones:** Why would you do that?

**Chris Gammell:** My Soundcore LED, they have LEDs on the side of the day. Oh, okay.

**Dave Jones:** Right. Oh, I guess my big wireless headphones at home do that as well. They've got like- I think it's just to show that they're on, right? Yeah, yeah. It's just to show that they're on. They're on.

**Chris Gammell:** There's no like detection if it's on your head. I think the Apple ones detect if they're like in your ear, so they turn off automatically. But if you don't have that, then you need to like be able to look at it and be like, oh, that's on.

**Dave Jones:** Right. You know? Yep. So anyway, yeah, it was not like an in-ear one that you get these days. It was like one of those outside ear, you know, things that click over the outside. Jabra style. Jabra, yeah. Whatever it's called. Yep.

**Chris Gammell:** Or Jawbone was another one. Yeah. Jabra, Jawbone.

**Dave Jones:** Something like that. Yeah. So he had an early one of those. So that was my first encounter with it. But I don't recall seeing it for donkey's years after that. It was like, it was the only person I knew who actually, you know, started using it. I cannot remember.

**Chris Gammell:** First time I saw anything with Bluetooth, it was when I was working at AudioPack. So it must have been my, I was a co-op. So it was like 2004, 2005. And they had just, they had this new product where they were putting it into like this, AudioPack was like doing like safety equipment for like firefighters. And they usually had it like, like it was basically just like literally audio amplifiers, like on top of like old motor, like tied into Motorola radios. And so they were playing around with, now they're going to be Bluetooth based instead. And they can go to a phone or to a radio, but without like, without a wire connection. And I just remember thinking, this is the worst audio quality I've ever heard of anything in my entire life. And like, and just as context at the time, like I was downloading music, you know, it was college days. It was early, early.

**Dave Jones:** Days of odd. Yeah. File sharing, whatever. File sharing.

**Chris Gammell:** I was listening to like 64 kilobit per second. Like, yeah. Like just like the, the tiniest crappiest stuff. 64.

**Dave Jones:** That was still reasonably high back then. You know, if you've got 32 or something. Yeah.

**Chris Gammell:** I mean, it was just the worst stuff. It was like the worst files played through them, like a phone speaker. And I'm like, yeah, I'm like listening to it. And so like, this is worse than that. So just as like a reference point.

**Dave Jones:** Yep. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, man. Nah, I've only recently gotten like in my, what the last year and a half gotten like the, uh, Bluetooth, uh, wireless earbud headphones and the ones for home, you know, apart from that, no, I, I, she's wired for all my music stuff before that. Yeah. I, I never used Bluetooth. Well, there you go.

**Chris Gammell:** You play right into that audiophile community, Dave. Right. Yeah. Open, you got your open ear, uh, you know, basically just like driver cones, you know, with a 3.5 millimeter jack in that, you know, like, yeah. Yeah.

**Dave Jones:** Yeah. No, even, even back in the day when I like design my own, um, uh, app for like, uh, workouts that, that used an MP3, uh, player. So you'd, you'd actually take it to the gym and I developed this software that actually, uh, in encoded voice instructions in there. Um, I'm sure I've talked about that before. Mr. Fancy over there. Yeah. And I almost got a patent on that one.

**Chris Gammell:** You should have done that, man. You wouldn't, uh, you wouldn't be doing electronics still. So you'd be off on some beach sipping Mai Tais.

**Dave Jones:** Nope. Nope. Cause this was, uh, six months before the iPhone came out and then apps overtook everything.

**Chris Gammell:** All you had to do, Dave, was just think about the app store before Apple did it. Right. And then did it. Yeah. And you would have been made in the shade. That bastard. Yeah. Yeah, exactly.

**Dave Jones:** Ah, could have been rolling in the cash. Yep.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Oh boy. So anyway. Yeah. So even back then I was using like a, no, even back then I wouldn't use a Bluetooth. Well, I don't even think maybe that, maybe it wasn't available. I don't know when I did it. When did the iPhone come out? Bloody hell.

**Chris Gammell:** 2007. I know that one.

**Dave Jones:** Oh, 2007. Okay. So even in 2007, like a good, almost nine years after Bluetooth came out, I still was not using wireless audio solution. Cause that's pretty much all Bluetooth was back then. It was like wireless audio or a little, or smarter gadgets. It's like, as you said, like a health monitor strap or something, you know, but a lot of the early ones use Ant and stuff like that. They use like the Ant protocol and stuff. Right. Right.

**Chris Gammell:** I think, and then BLE came up and like, you know, I'm talking on my butt here. I have no idea the history of this stuff. Actually, I really like, uh, Mohamed Afana's, uh, podcast, podcast videos. He's got a bunch of videos about like Bluetooth and he has like a horse about Bluetooth. He's, he's the go-to for that sort of thing. I should watch more of his videos. Um, but yeah, um, that, that's, there's like a whole history there of like when Bluetooth 2.0 became 4.0 BLE, all that, all that different stuff.

**Dave Jones:** And like, cause the denominations matter, right. Where it actually went really like it became, yeah, this is super low power. This is longer range. And it's, yeah, this really is going mainstream, you know? Yeah. Um, I don't know what that date was, but yeah, there was like a switch over at one point. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** So, uh, I, let's see, I'm finally looking at the, the Zephyr samples here. So like, there's like peripheral is usually the node device, right? So like there's the peripheral and then central is like the thing that's accepting all these things. Hmm. And so there's like HR, HT, HIDs. There's a UART sample. I know now. Um, yeah. Cause I mean like your mouse is probably running Bluetooth, right? Your keyboard is probably running Bluetooth. That sort of thing.

**Dave Jones:** Uh, they're running the proprietary, whatever the, um, Logitech thing is. The little Logitech. I don't know if that actually uses their own proprietary thing. Yeah.

**Chris Gammell:** Some of them have standard, like their, their own like radio protocol on top of like just a packet radio, like a 2.4 GHz thing. Yeah. That's like the NRF 24 chip that I was playing with on the, that CH32 V003 board that I built. Like that's like, that's like one of like Nordic's earlier chips as well, where it's just basically just like straight 2.4 GHz packets. Got it. Yeah. Anyways, there's all these different messages and you don't have to use them because then you can also make your own thing. And that's what I think a lot of the majority of people do. So like when we talked about toothbrushes a while back, there's no like standard toothbrush method message as far as I know. So they probably have like a standard GAT profile for the toothbrush. And then when I said I connected into home assistant, home assistant knew how to listen for like, I said that there was a toothbrush. It advertised that it was a toothbrush and it had like a database looking up that this is a toothbrush type of message. And here's how you read the data coming out. I wait for the future. Well, you know. Yeah. Hey man, people got to have their stuffs, you know. No. Got to consume the things. No.

**Dave Jones:** Wrong. Wrong. Wrong.

**Chris Gammell:** Anyways, Bluetooth is very useful outside of just toothbrushes. And there you go.

**Dave Jones:** Turns out Bluetooth low energy was 2010 was Bluetooth low energy.

**Speaker ?:** Oh wow.

**Chris Gammell:** Yeah.

**Dave Jones:** Because actually before that, Bluetooth was relatively like, it was quite high power. You know.

**Chris Gammell:** Which I was like, oh, that's only a couple of years ago. I'm like, oh my God, it's 14 years ago.

**Dave Jones:** It's 14 years ago now is Bluetooth low energy.

**Chris Gammell:** Yeah. Yeah. Jeez. Yeah.

**Dave Jones:** Bluetooth low energy was previously known as WeeBri. Did you know that?

**Chris Gammell:** I did not know that.

**Speaker ?:** There you go.

**Chris Gammell:** Factoid of the day. I did not know that person reading off of Wikipedia.

**Dave Jones:** Totally not for reference 93 on the Wikipedia page. Oh my God. The WeeBri forum merges with Bluetooth SIG. It's W-I-B-R-E-E. WeeBri. Oh.

**Chris Gammell:** Well. That's a better. I think Bluetooth low energy is a better name. Yeah. Anyway.

**Dave Jones:** The WeeBri forum. Whatever. I don't know. It was like a.

**Chris Gammell:** Yeah. Probably industry group sort of thing. Industry group or something.

**Dave Jones:** And they, yeah. They merged with. Merged in quote marks.

**Chris Gammell:** Yeah. Yeah. Subsumed by.

**Dave Jones:** They didn't keep their name. The SIG. So yeah. It wasn't really a merger. No. It isn't a merger if you keep your. If you don't keep your name. Yeah. Let's just put it that way. Have there been any mergers in the industry this week? The last two weeks. This. Probably. And we just don't care anymore, do we? So, you know.

**Chris Gammell:** What was the last one we talked about?

**Dave Jones:** Who cares? It doesn't matter. I guess there. Oh, no. It was the Altium. Altium thing. It was the Altium one. It was the last one we probably talked about. Yeah.

**Chris Gammell:** Renaissance actually was going to buy a cellular module maker out of France.

**Dave Jones:** Oh.

**Chris Gammell:** Called Sequans. I don't know if you know them.

**Dave Jones:** No. I don't think so.

**Chris Gammell:** Yeah. They were going to buy Sequans. They're smallish. So. So like a fabulous semiconductor. They. If you remember the Pi Com. Pi Com boards. Oh, yeah. Yes. Yeah. Pi Com is no longer. Right. But that was like. Yeah. They. And they had some cool things. Because they had like. Like one of their claims to fame was like the. The. The Phi Pi. I remember. Was that. Oh, yes. Yeah. Yeah. Yeah. I remember. It had like five radios on it. Yeah. Because it was. ESP 32. So it had Bluetooth and Wi-Fi. And then it had a Sequan cellular module. And then it had. A Semtec SX. 1276. Doing this from memory. So from memory. Whatever. Whatever. And so that was. Laura. And. The other one that's just like Laura. With the butterfly. Got it. What is it called? The French one? No. Flora. No.

**Dave Jones:** Sorry. Come on. Hey. There was an acquisition.

**Chris Gammell:** Who?

**Dave Jones:** It's. It's on our list. Synopsis to acquire Ansys.

**Chris Gammell:** Oh, yeah. That was. That was a while ago. That was actually. I put. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. Yeah. Yeah.

**Chris Gammell:** Hold on. Hold on a second here. Let me get this right. What are these things called? Like Laura. What do I Google? Like Laura, but not Laura. People are screaming into their thing right now. French Laura. Let's see what happens there. Laura fanboys.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Right. Nope. It's not that. It's not Laura. Man. Man. I cannot think of it. This is. It got bought by a Taiwanese. I know everything about it. It got bought. It was. It was. It was put on the block. And it was. They're centrally. Controlled. Network operators. And it was put on the block. And a Taiwanese company bought them. It was on the block. It was put on the block. They were selling. They were. They went bankrupt. And they were selling. Selling assets.

**Dave Jones:** I haven't. I haven't heard that term before. Being. Being put on the block. Is that an American financial term? Yeah.

**Chris Gammell:** I think it's like the butcher block. Maybe. I don't know what the block is.

**Dave Jones:** Right. Yeah. No. I don't. I don't think I've heard that before.

**Chris Gammell:** No.

**Dave Jones:** There you go. There's the Americanism of the day.

**Chris Gammell:** Yeah.

**Dave Jones:** Bring.

**Chris Gammell:** I could. I could be wrong about that too. Yeah. Well, I can't remember. That was the fifth radio though. So. Whatever that was. Sorry. Radio. Thing. It was like a network. It was like low power. Like Laura. And there was a sequence module on there. That's how I remember it. All right. So. Cool story, Hansel.

**Dave Jones:** Moving on. I'm sure you want to talk about hybrids. Because you put this on the list.

**Chris Gammell:** Oh, we should talk about Ansys. We can't just gloss past Ansys. Why not? Although I never used Ansys. I mean, it's like a really high end tool. It's a high end. Yeah. Yeah. Yeah. You never used it? You have used it?

**Dave Jones:** No, not personally. No. I do know others that have used it.

**Chris Gammell:** Yeah. They do like. They have like RF. And then they have like. I think like. Dave, my brain's not working today. What's it called?

**Dave Jones:** They do. Finance element analysis modeling. That's it. Don't they? Yep. That's the one.

**Chris Gammell:** That's the one I was thinking. Yep. Yep. Yep. Yep.

**Dave Jones:** For like. I'm talking like for. Like for like airline engines and shit like that. Like really high end stuff. Right. It's like. Yeah. It isn't just circuit. It's like. Yeah. Really high end stuff. So any finite element analysis.

**Chris Gammell:** This simulation says the door is going to fall off again, Bo. Are you sure you want to ship it? Yeah. Yes, we do. Yes, we do.

**Dave Jones:** Right. And I'm sure I can spit out a checklist of things you need to do to ensure that your door doesn't fall off. You know.

**Chris Gammell:** Right. Right. Taking down all the bolts. Sorry.

**Dave Jones:** We just have to make fun of Boeing and United Airlines because it's such a meme. Yeah.

**Chris Gammell:** It wasn't United, was it? It was Alaskan.

**Dave Jones:** Whoa. Was that Alaskan, was it? Could have been.

**Chris Gammell:** I think so.

**Dave Jones:** Okay. All right. Yeah. Anyway, I've been throwing up memes on Twitter for United Airlines. It's quite funny to keep up.

**Chris Gammell:** Yeah.

**Dave Jones:** Keep on track with.

**Chris Gammell:** Oh, Ansys owns HFSS. Yeah. So that's like a big one for like RF.

**Dave Jones:** Yeah. Right. Yeah.

**Chris Gammell:** Yeah. I remember the RF guys at an old company I worked at, they swore by that program. Yeah. I think it was, I think it was, again, finite element analysis, but for field simulation and stuff like that.

**Dave Jones:** Fields around PCB tracens, transmission line.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** This is way above my. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** I have to be really serious. Yeah. No. Yeah. I have to be designing the latest.

**Chris Gammell:** You have to know how the little bubbles are supposed to go.

**Dave Jones:** Yeah. You have to be designing the latest, you know, satellites and Tesla sky dish or whatever it is. What's it called?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Something like that. Yes. Yeah. Fancy, fancy stuff.

**Chris Gammell:** Welcome to the dummy hour where two dummies can't remember any words.

**Dave Jones:** Because we've never used a hundred thousand dollar package for.

**Chris Gammell:** I just, I literally can't remember any words today, Dave. I think it's like, it's, it's a nine 42. It's, we're recording a little later than usual. Cause you know, like I've had a three year old yelling at me all day, but like, yeah. All right. I do wonder if I'll ever get back into this. You know, I used to simulate things. I used to simulate, you know, used to LT spice from here and there. Not saying this is at the same level, healthy spice, but like. Right. I don't really, I don't really simulate things anymore, Dave.

**Dave Jones:** Oh boy. Anyway, I can't read this bloody hybrid page because Wired, it's from Wired magazine and they can't.

**Chris Gammell:** So now we're switching to cars just so people are following along.

**Dave Jones:** I'm going to sign in. Yeah. Like I've got to, I don't have a bloody Wired account to view the article. No, we need to archive.today. I'm going to archive this bastard for you. Okay. And then we can read it without the ads. So I don't know how you're reading that, but I can't.

**Chris Gammell:** Well, this is from a while ago.

**Dave Jones:** It's last archive five days ago. Yeah.

**Chris Gammell:** Where is, oh, here. So it's, here comes the flood of plugin hybrids, right? That's the one you're talking about.

**Dave Jones:** Yep. That's all.

**Chris Gammell:** You know, it's probably just because I'm an American. Also because I run a pie hole maybe. Oh no.

**Dave Jones:** Yeah. Anyway, I just sent you the archive link so we can put that in the show notes so that people don't have to go through the paywall. They can void the paywall.

**Chris Gammell:** Take that.

**Dave Jones:** Sorry, Wired.

**Chris Gammell:** Conway Nast.

**Dave Jones:** Oh boy. Yep. Yeah. Anyway.

**Chris Gammell:** I think that's interesting. You and I talked about this two weeks ago whenever we talked about cars. But basically just that like hybrids are probably the way to go anyways. Like most car makers are doing that anyways.

**Dave Jones:** Let me guess. Because all these countries, they've all promised we're going net zero. More than half the electric cars will be full. Half the cars will be electric by 2030 or some bullshit like that. And then they realize, oh, people aren't buying them. Oh, this isn't going to work. Oh, they're not really saving the environment. Oh, everything else, right? Oh, lithium prices aren't coming down. Oh, but we can still meet our state of goals by having hybrids. If you put one little 18650 battery in there, you can call it electric. And then we've met our goals, right?

**Chris Gammell:** That's pretty cynical, Dave. That's pretty cynical.

**Dave Jones:** Pretty cynical, you think? I do. Overly cynical, you think? Or you think it's bang on?

**Chris Gammell:** I mean, it's not probably too far off. The idea of I could imagine some car manufacturer. I'm thinking like Volkswagen. Yeah.

**Dave Jones:** They're all backing off at the moment. They're all backing off from their grandiose predictions.

**Chris Gammell:** I feel like they're all retooling, though, too. I feel like they're all reevaluating retooling. I think they got spanked pretty hard during the chip shortage, too. I think that really ended up hitting a lot of planned product lines.

**Dave Jones:** Yeah, but that hit EVs and ICE cars equally, I thought. I don't know.

**Chris Gammell:** Maybe.

**Dave Jones:** No. I think that's a red herring.

**Chris Gammell:** Okay. But, yeah, I do think that there's less consumer appetite than they thought, right? Yes. This is kind of a build-in. They will come in. Now it's... I mean, the charging infrastructure is slow to catch up, too, right? Yeah. I mean, I think at least in the US, the deal...

**Dave Jones:** Your order's a magnitude far ahead than we are.

**Chris Gammell:** Further ahead. Oh, sure, sure, sure. I just meant the charging infrastructure of Tesla opening up to other manufacturers. That's going to be... There has to be a standardization.

**Dave Jones:** Otherwise, it's just going to all fall flat. It's all going to fall flat. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah, and I think some of it's just lifestyle, too. There's a lot of street parking in the US, so I think there's...

**Dave Jones:** No, it's a total lifestyle thing. And unfortunately, all these governments have promised all this shit that this was the future, and I'm a huge EV car advocate, right? And yet, I know the bullshit when I hear it, right? It's like, no. It was never... It's always going to be a lifestyle-based thing, right? It's like, no. You can't make everyone drive an EV by 2030. That's complete bullshit, you know? You can't force people to use these things. It's just ridiculous.

**Chris Gammell:** Yeah, I think you incentivize them, right? I mean, you incentivize them with tax breaks and all that other stuff.

**Chris Gammell:** Well, you can.

**Dave Jones:** Yeah, there's arguments against that, but yeah, okay.

**Chris Gammell:** Sure. Yeah, that is a policy choice, but I think that's one way to drive.

**Dave Jones:** Because subsidies is people who don't or who don't have the lifestyle to pay for these expensive EV toys are the ones funding it through their tax dollars, you know? Sure. So that's like... Yeah, yeah, yeah. I can't talk. I took government money. I got a free EV. I got a free EV. The government, in quote marks, paid for it. My children's future actually paid for it, but you know. Yeah, free. It was part of the COVID. Stimulus payouts. They gave me like 60 grand. The government gave me like 60 grand. They went, here, spend it to boost the economy. I went, okay, I'll buy an EV. Thanks.

**Chris Gammell:** Oh, I see. So it wasn't just the tax break. I see. No, it was like... Yeah, okay.

**Dave Jones:** No, it was no. We have no tax breaks here. It wasn't earmarked for EVs only. You're saying you chose to use that.

**Speaker ?:** No, no.

**Dave Jones:** It was COVID funny money, right?

**Chris Gammell:** Got it.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, that's fine.

**Dave Jones:** And now if you're in Victoria, the government's now taxing your... is introducing a new land tax to pay for all the free money they gave you. Great. Yeah. How do all the listeners in Victoria? Australia. Yeah, right.

**Chris Gammell:** Right.

**Dave Jones:** Hope you're enjoying that. Oh, boy. Anyway.

**Chris Gammell:** Yeah, I think... I do think, yeah, there's a lot of policy difference and things like that here. But I think at the end of the day, what they're pointing at is Toyota kind of holding back and looking like geniuses now, right? That's one of the big things they point to. Yeah, because... I do think one of the big switches, like Toyota, like with the Prius specifically, they held off on the plug-in version for a very long time.

**Dave Jones:** Oh, for... Yeah, half a decade. It was a long time.

**Chris Gammell:** Right, exactly. But now, I think they have a good platform there. And I think that that's going to be copied a lot over and over again. Right. And I think that that's the other thing too, is like now there's going to be this new... It's just going to ease people into it a little bit better.

**Dave Jones:** Oh, yeah. No, people need it. Like if hybrids didn't exist, EVs would be a niche little hobby toy thing. You know? Hybrids, yeah. Yeah. It allows people to just use their normal car, yet they get some of the advantages of EV. Yeah. If you're only traveling 30Ks a day, yeah, it's got a small enough battery. Full enough battery that it does 30Ks a day for you. So, you can actually... Yeah, right. And you can slow charge it overnight at home. And you know, like, yeah. Yeah. It does ease people into it. And that's huge.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So, you're buying one? No, because you've already got a full EV.

**Chris Gammell:** No, I already got one, man. I'm not buying another car for a long time. Yeah, right. I do think the next car, probably the next, you know, we talked about it here, like the next car that we buy will be probably a large, you know, very large for Australian standards, but just a large car by US standards and, you know, something that's probably hybrid, plug-in hybrid.

**Dave Jones:** Ours will be a large hybrid. In fact, we may have to make this decision in the next couple of weeks. Oh, yeah. Your car's sick. Yeah. Did we talk about it? Did we talk about my sick car?

**Chris Gammell:** You and I talked about it, I think.

**Dave Jones:** Which is electronics related. I can bring this back to electronics. In fact, we can talk component level here, if you like.

**Chris Gammell:** All right.

**Dave Jones:** All right. Great. Yeah. So, I've got a 2010 Hissendualis Plus 2. It's like a seven seat, you know. It isn't a large, it's not considered large, but it's, you know, it's large enough for us to go on holidays with. So, that's our car we go to drive on large-ish holidays where we have to pack all the kids' stuff and all the wife's stuff and me. I just take one little duffel bag and I'm right, you know. But anyway, kids and wives take a lot more stuff. So, it's a space thing. And it's a fairly efficient car. It hasn't given us a lick of trouble in 14 years and it finally failed. The ABS system failed it, the anti-lock braking system. And a weird fault. Which the manufacturer had not, they said that they hadn't seen that before. So, what it was is even if you turn the car off and took the key out, the compressor in the ABS modulator was still running. You could actually hear it. Like the ABS was like on permanently. So, even when you remove the key, this sucker just kept going.

**Chris Gammell:** You're always safe. You're always, you're never going to, you're never going to get into a, your wheels aren't going to lock up. Right. You're parked on the side of the road, right?

**Dave Jones:** No. But it still drove. Fine. Right. It still drove. Because people don't realize that the ABS doesn't apply brakes. It actually releases the brake. So, it actually releases it. It actually releases the pressure so that you stop skidding a bit and then it turns it. Then it turns the release off, which then applies the brake again. But the actual ABS modulator does not actually apply the brake. It actually, it has all the hydraulic feed lines going into it to your brakes and it just turns them off for a brief, you know, half a second or something. So that you get that pulsing sensation in your brakes. Yeah, yeah. As you say, that's what it really feels like. Yeah, yeah. So, that's what the analog braking system does. And that's what the modulator does. So, anyway, it was continuously on. So, I had to actually finally, so that we could still drive the thing with, and it wouldn't drain the battery because this thing's just continuously running even when you take the key off. I had to rip out the 30 amp fuse for the ABS system. So, for the last couple of weeks, we were driving around for three weeks or something.

**Chris Gammell:** And shoved the penny in there, huh?

**Dave Jones:** Yeah, right. So, we were driving around with no anti-lock or anti-skid braking system. But, of course, the car works fine. The brakes still work fine. But it just, yeah. You only lost one kid. Right. That's all right. Yeah. Nah, it's all good. So, anyway. So, I put this on the, I did a video on the second channel. And basically, everyone, most people thought that it was either a shorted out motor in it, or it was a shorted out drive transistor pair in it. Or it was a shorted out relay, depending on which one it used. Like, the older style used a relay to actually drive the pump motor thing. Whereas, I believe mine uses a pair of MOSFETs, like a totem pole pair of MOSFETs. And apparently, yeah, one of them was shorted on. And, yeah. That is the best guess. I haven't had that confirmed yet. But that is the best guess. That it was, yeah. One of them was shorted on. And, of course, and the ABS system, I don't know how it's wired into the car. But it must bypass the switch, the key switch thing. So, it must be permanently on. And so, anyway. Yeah. It's a failed MOSFET is the best theory. And it keeps the pump on. And the pain in the ass thing is that it's serialized. It's a serialized part. So, it talks to the, it's programmed. Yeah. It's programmed. And it talks to the car's computer. And, yeah. So, you can't just get one from the freaking wreckers and put it in. You have to have the special programmer that serializes it and reprograms it in the car computer. So, it reads out the serial number of a bloody pump drive thing. A motor drive thing. How evil is that?

**Chris Gammell:** Yeah. Evil bastards. Lewis on the case. I feel like we maybe have talked about this now. Like, I'm having, like, flashbacks.

**Dave Jones:** Yeah. I think we might have. Sorry for those. You've got to listen to it twice.

**Chris Gammell:** People still listening. They're like, what the hell? Anyway, I still haven't heard back. I told you we're tired.

**Dave Jones:** Anyway. I did get a quote for $1,800 to actually repair it. Apparently, there's one shop in Sydney. The manufacturer, right? So, I sent it back to the manufacturer, right? And, like, I took the car back there and they confirmed that the problem was. And they said they know of one company in Sydney that will actually try and repair this. Try to repair it. So, whether or not they can repair it, because then you won't have to reprogram it, physically reprogram the thing, which is apparently something the manufacturer has never done or something, presumably. So, yeah, they can't even get one from the wreckers. So, it's either buy a brand new one for about $5,000 or $6,000. They told me this is the manufacturer. New one for $5,000 or $6,000. Or we can send it to a company that tries to repair it. Yeah.

**Chris Gammell:** It doesn't feel very often, huh?

**Dave Jones:** No. No, no. Yeah, they're fairly reliable things. So, yeah, this is the first time they've seen one that fails when you turn the key off. So, apparently, it's the first one. Yeah. Yeah. So, anyway, trust my luck for that. And so, anyway, if they can repair it, it's going to cost me $1,800. And it's a 14-year-old car. But we figure the car is worthless. If we try to trade it in, now it's worthless without an anti-lock braking system. So, we would easily get the $1,800 back in value, in resale value. Well, we should be able to get $1,800 back in resale value if they can fix it. So, and I think once it's fixed, I think we might, yeah, it's pretty old. We might start thinking about a hybrid. There you go. Whether like a second-hand hybrid or whether a brand new one. I don't know. Leave it in the comments down below. Should we consider a second? Because yours is second-hand, right? Yours is a... Just barely. Barely.

**Chris Gammell:** Yeah. 10,000 miles on it, yeah.

**Dave Jones:** 10,000 miles is still a decent amount.

**Chris Gammell:** That's like one year of... Yeah. One year of average. Least of miles. Yeah. Yeah.

**Dave Jones:** And was that like a corporate car or was it like a privately owned car? I don't know. They don't tell you. I don't want to know. Right. They don't want to know. Okay. Right. Mind, when I... You remember when we went on the road trip in my little Toyota Corolla?

**Chris Gammell:** I do. Yes.

**Dave Jones:** That was a second-hand one. I bought it with 18,000 Ks on the clock. Got a huge discount. It was owned by the CEO of Toyota, actually, in Australia. The CEO of Toyota Australia used it as a person. And he just commuted. And he did like 18,000 Ks in like five months or something because he actually lives somewhere up the coast or something and he just drives down every day, you know? Yeah. It was his next gun.

**Chris Gammell:** I'm just thinking about the CEO of Toyota. It's like, this car used to belong to the President of the United States.

**Dave Jones:** States, right.

**Chris Gammell:** The President... Sorry, no. The President of America and Express. Owners Anonymous. Yes. Oh, boy. His name was Bill.

**Dave Jones:** Anyway, yeah. Hybrid. Yeah, we're thinking a hybrid. Because we have the solar system to give us free. And really, and that second, like that one's our second car because we have the full EV to do all our daily driving with. So the second car doesn't get, you know, and it gets used in short little tiny trips, you know? So, yeah. So a hybrid with even the smallest battery would do just fine. Although it's got to be a plug-in hybrid. I don't understand why they ever made hybrids that weren't plug-in. I mean, it's just like...

**Chris Gammell:** I think because of just logistics. There was... If there was no charge... You know, like at the beginning, there was no charging stations available.

**Dave Jones:** Yeah, but you could have plugged in a bloody into your outlet at home. You know? The batteries in those were tiny. They were like five, ten kilowatt hours. The five, five... No. Only a few kilowatt hours or something. It weren't much.

**Chris Gammell:** Yeah. Like the early Prius and stuff like that.

**Dave Jones:** Yeah, yeah, yeah. That were naff all.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Yeah. So...

**Chris Gammell:** I don't know.

**Dave Jones:** Anyway. Yep.

**Chris Gammell:** All right. Enough cars. Okay. How about... Parts? How about parts? Parts? You see the new Espressif part? It's actually... Nope. I realized I linked it in.

**Dave Jones:** Because there's a new one every month. You just keep talking about a new part every month.

**Chris Gammell:** I know, but this one's badass. The rigorous clock one. Yeah, yeah. This one's a dual core 400 megahertz plus a secondary RISC-V at 40 megahertz. All right. Yeah. Yeah, it's a beast. It's... I don't know how much it's going to cost, though. That's the thing. Ah. But it's like... Okay. Wi-Fi, thread, Bluetooth. What else is on the docket? I guess this is not a very good video. So is this on the list? There's a...

**Dave Jones:** Or is this something you pulled out of here? It is on the list.

**Chris Gammell:** I added it right at the end. But there is a YouTube video where they go over the block diagram. And that's the... That's the real jam. Okay. I really hate their labeling system. I think it's horrendous. Right. But...

**Dave Jones:** So what's the target market with the secondary processor in there? Is that like a low-power secondary processor?

**Chris Gammell:** I think it's here. Let me send you a link, too. I think... This is bad. You just need to make a background. I think what they're going for here is this is like a targeting vision application. So like a smart doorbell or something like that. That's probably a pretty good example here.

**Dave Jones:** All right. Let me have a look.

**Chris Gammell:** So I think... I think that that is probably one of the things. AI.

**Dave Jones:** Of course it's got AI. Oh. They have all got AI. Oh. Wank, wank, wank. AI. Of course.

**Chris Gammell:** Of course. And I think... But then the camera input and also display. So that's like... You know... It's not quite tablet level, right? Because it's still embedded. But I can imagine, you know, stoves and...

**Dave Jones:** Well, they're showing examples of one of those...

**Chris Gammell:** Smart wanks.

**Dave Jones:** One of those, you know, Alexa microphone bloody things, you know?

**Chris Gammell:** Yeah, exactly. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** All right. And it really is. It's interesting because it's like this stuff is... This is starting to touch... This is kind of like the mid-tier kind of stuff. The NXP calls them crossover type of things where it's like basically... It's enough juice that it could be running Linux, but it's not Linux. Right. Usually it's more specific. It might be, you know, whatever.

**Dave Jones:** It's got a sane amount of stuff in it. You know, it's got H.264. It's got, you know, HMI. It's got multi-camera, you know, MIPI interfaces. It's got like... This is ridiculous. It's got touch sensors. It's got...

**Chris Gammell:** I3C. You're starting to see that stuff pop out. Never thought I'd see that stuff. How do we say that, Dave? I cubed? I squared C? I cubed C?

**Dave Jones:** No, I don't like cubed. That gives me the heebie-jeebies. Sorry for any of you I squared C fanboys. Yeah. Yeah, I would say I3C. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Sorry.

**Chris Gammell:** That one's going to take a while to get used to. Yeah. Yeah. Yeah. So, I don't know. It strikes me that this stuff is... You know, it's expressive too, so it's going to be cheap, right? And so, I really like to see that all this stuff is, you know, these RISC-V, like, secondary processors just, like, thrown in. Because that's, like, the low power. It's going to just be handling probably... I can imagine, like, a workflow where you have, like, a firmware team. Like, the low power firmware team just handling, like, talking to sensors and things like that. Right. And they were kind of independent of the...

**Dave Jones:** You could actually have two totally independent teams because there's two different processes on here, right? Right. There's that low power one. You could have a team just...

**Chris Gammell:** Some bust between them probably, right? Yeah, of course. Maybe shared memory. I'm not sure how they would do it.

**Dave Jones:** You could share stuff, but...

**Chris Gammell:** Yeah.

**Dave Jones:** But that's it. But you could actually spin off a separate team just to work on that aspect. And then you wouldn't really have to cross over much as long as you shared how you transferred information between them. Then, you know, yeah, yeah.

**Chris Gammell:** Right. I'm going to dump the sensor memory into this region. Right. And then, you know, you use your AI blah, blah, blah. Blah, blah, blah.

**Dave Jones:** You could have an AI wankery team to do that.

**Speaker ?:** Exactly.

**Chris Gammell:** Right, right, right. Yeah. Yeah, and so it's just interesting how this stuff is developing more. And, you know, I'm sure there's going to be other manufacturers that are, you know, they're all pushing it down into the silicon now. These, like, these engines, they want to have, like, you know, they already have, like, models that you can put onto, like, floating point units and stuff like that where it's just generic computing. But now they're starting to put more specialized computing down into these modules as well. Right. Yeah.

**Dave Jones:** With so many bloody things built into it, how can there not be any issues with this? What's the errata list for this thing look like? I mean, you know, it's like.

**Chris Gammell:** Yeah, I've only seen marketing stuff for it because they just released the marketing video for it today. Apparently, it was announced in January of 23. So, like, this has been 15 months.

**Dave Jones:** Oh, okay. Right. Oh, geez.

**Chris Gammell:** Yeah. All right. Probably that must have been CES of last year.

**Dave Jones:** And I'm sure there's still bugs in it, right? Yeah.

**Chris Gammell:** I'm sure that this has been an early, early release. Yes.

**Dave Jones:** If you're an early adopter and you can't figure out why the i3C system's going a bit dodgy on you.

**Chris Gammell:** I don't even know how you would test it. Like, I think we should probably figure out how that works at some point, right?

**Dave Jones:** Yeah, we should. But even the best manufacturers, you know, with the most unlimited budgets to test their silicon still, you know, you'll find bugs. I mean, it's just. Yeah. Because there's so many edge cases. There's an infinite number of edge cases. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. So, I don't know. I'll probably try and drop by Espressive Stand at Embedded World and see if I can.

**Dave Jones:** Right. Well, if we could find somebody who specializes in testing silicon, that's their, like, who's the best industry silicon test guru? You know, maybe we can get on the show.

**Chris Gammell:** Yeah. It's interesting, too, because one of my friends here in town just switched between companies. And it's not always the, like, I always kind of assumed it'd be, like, applications engineering sort of thing. It's, like, somewhere between, like, product engineering and product marketing. And then, like, the terminology is weird. Like, applications engineering. Yeah, sure.

**Dave Jones:** And then, like. That could mean anything. It could mean a whole gamut of stuff.

**Chris Gammell:** Engineers. Yeah, totally.

**Dave Jones:** Hmm.

**Chris Gammell:** So, the best ones? I don't know. I don't know. It's not me. I know that.

**Dave Jones:** Leave it in the comments if you know who's the best of the best out there.

**Chris Gammell:** Or give us a shout. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. All right. Yeah. Part of the week, is it? All right. Well, I will, yeah, I will report back once I, hopefully I'll get to see this in action in a better world. We'll see.

**Dave Jones:** Cool bananas.

**Chris Gammell:** We will see. Yes.

**Dave Jones:** Who's Bitlooney? And do we care that they designed an ASIC? You added this to the list.

**Chris Gammell:** Yeah, Bitlooney is great. You don't watch, you don't follow Bitlooney's channel? Yeah. Yeah, so Bitlooney.

**Dave Jones:** No, I don't think I've heard of Bitlooney. Is this a channel I should be following?

**Chris Gammell:** Yes, yes. He's got great videos. What's on his channel? What's his channel about? A lot of like, you know, small electronics projects.

**Dave Jones:** Oh, okay. There you go. Subscribe. Done. Yeah.

**Chris Gammell:** There you go. All right. You're welcome, Bitlooney. You owe me a beer. Got Dave to subscribe. Now you'll have snarky comments in your comment section.

**Dave Jones:** Well, I only subscribe with my second channel. Sorry. Because that's what I'm logged in at the moment.

**Chris Gammell:** Yeah. All right. So Bitlooney, so there will be some spoilers here, I suppose, if we talk about it. But he did a bunch of the, what's it called? Tiny Tape Out. Remember Tiny Tape Out? The project? Oh, yes.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Yeah, yeah. Basically, Uri had a simulator that then could compile down to Verilog, which then could be pushed into the open toolchain workflow and then put onto a test shuttle wafer, like one of the NPW shuttle runs. And so then that was basically, they split one of the shuttle runs into even more subdivided pieces. And you could do it for like, I think it was like a couple hundred bucks. And so Bitlooney did one of these and he put most of a video file into the memory. So he basically made like a memory array.

**Dave Jones:** All right.

**Chris Gammell:** And then when you play it back out and decode the video, it is, of course, a video of Never gonna give you. Oh, God.

**Dave Jones:** Okay.

**Chris Gammell:** But it's like super, super, super, super, super down, down sampled. Right. Right. Yeah. So it's like little blocks. Yeah, right. It's fantastic. And it shows the process too, right? Yeah. Cool. It shows that it's like, it's very accessible. Yeah. Obviously Matt, Ven and Uri and like everybody working on that stuff. It's like, it's actually accessible. Like that's pretty wild. Right. I mean, the fact that like you can just go and make a chip, you know, like.

**Chris Gammell:** Yeah. It's great.

**Dave Jones:** Yeah. Actually, I think I might've, yes, I have watched his, how I made the custom ASIC. Yeah. The custom ASIC thing. Yeah. I've partially watched that video. Okay. So yeah. Yeah. Great. The end of his lab, he published a video six months ago. The end of his lab, what? Is he being?

**Chris Gammell:** I don't know. I don't know, Dave. Losing his lab? He probably moved labs. Yeah. I don't know.

**Dave Jones:** Right.

**Chris Gammell:** Right. Dave, there goes Dave's day. He's about to go watch. Oh yeah. No.

**Dave Jones:** Any, any lab move video I'm totally into. Yeah. Yeah. Absolutely.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** Um, one other, uh, past guest, Pete Bevilacqua, um, who was, uh, antenna engineer at like Apple and Google and like a bunch of high end places. Uh, he has a new thing where he's basically making it so you can power, you know, like how like, um, outdoor cameras are all like USB powered. Did you know that? Like all the Nest cameras? Nope. They'll expect like five volts to power.

**Dave Jones:** I just don't care about those security cameras.

**Chris Gammell:** Okay. Well, that's, that is how they work.

**Dave Jones:** Right.

**Chris Gammell:** And like, so then you have to like have a professional installer come in and still like, if you want to like have power to these things, you have to have a professional installer basically come and route USB out to them, which is like kind of stupid, right? You should have probably 24 volts out of that security camera. Um, right. And so it's like this kind of this like half measure sort of thing. They are like outdoor weather rated, but like, why would you do that? And then the other method is like, then they have these magnetic mount ones where you can like, you can basically charge it inside and then you could take it outside and like very easily like mounted.

**Dave Jones:** Yeah. But a battery power camera is not going to last long.

**Chris Gammell:** Exactly. And like, it's not, it's actually better. It's better battery life than you'd think, but you still have to like go and take it down. Yeah.

**Dave Jones:** You have to remember to take it down. Oh God.

**Chris Gammell:** You gotta like remember to do it. And then also if you, um, if you want it to be a, like in a convenient location, then if someone wants to come and rob your house, they walk up and they grab the thing off the

**Dave Jones:** side of the house and they spike it.

**Chris Gammell:** And then you don't have camera coverage anymore.

**Dave Jones:** Right. So it's like, that's stupid.

**Chris Gammell:** So anyways, Pete got this new, um, kickstart. He's got a new Kickstarter going. And, um, basically he's passing power through it's the power mole. And it's basically just like a couple transformer through a window. And, uh, and then he's passing USB power outside. It's, it's kind of surprising this doesn't exist already, but yeah, it's a great idea. Right. I mean, like Pete's a great RF engineer, so he knows what he's doing. Uh, and, uh, yeah, he's just basically just passing power through a window up to 30 centimeters. I forgot. It was not 30 centimeters. Yeah. 30 centimeters. Is that right? It was, it was bigger than I thought it would be.

**Dave Jones:** 30 centimeters. That's a heck of a thick window.

**Chris Gammell:** Maybe it's.

**Dave Jones:** Can't you just put like a little coil on, like a wall is like, what, 15 mil thick or something, you know, if you're like.

**Chris Gammell:** Yeah.

**Dave Jones:** You could, that's, you know, that's reasonably far apart. But if you're just talking about a piece, you're just talking about a pane of glass.

**Chris Gammell:** 30 millimeters. Oh, 30 millimeters.

**Dave Jones:** Okay. Jeez. You can get, yeah, you can get 80, 80% efficiency doing that. Yeah. Yeah. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** So.

**Dave Jones:** That's great.

**Chris Gammell:** It is really just a couple of transform. I mean, there's, there's other stuff in there. You got to have like flyback, I'm sure. And drive, you got to drive the coils, whatever. But, but yeah, then you can power something on the other side. So cool idea.

**Dave Jones:** Yeah. Yeah. That's great. Yeah. Especially if you're like rent or something like that and you have to get a cable on the other side or something. Yeah. Yeah. Yeah. That'd be great. Is it just power or does it do data as well?

**Chris Gammell:** Just power.

**Dave Jones:** Oh, okay. Right. Yeah. Oh, because the thing is a wireless. Usually wireless. Okay. Yeah. Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** Yeah. I always point people at the, Pete did was, he gave a talk at the meetup I ran way back in the day about building a VNA where he had never been a PCB before. And then he's like, I'm going to build a VNA. Oh, right. Yeah.

**Dave Jones:** That is, that is bold. That is very, very bold. Yeah. That's. Yeah.

**Chris Gammell:** And he, he got, he got pretty far, but it's not, uh, I don't think, I don't think it ever, uh, went commercial. Okay.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Looks like this is, this is going commercial.

**Speaker ?:** Sounds familiar.

**Dave Jones:** Sounds like every project I've ever done. Never went commercial.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Oh boy. Yeah.

**Chris Gammell:** Anyway. All right. Let's get to, uh, the most upvoted post for the week, which was not from us. How about that?

**Dave Jones:** Oh, really?

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. What is it?

**Chris Gammell:** Here we go. Most popular hobby electronics parts. Oh yeah. I saw this. Former guest, Jan Richter, uh, who does parts box. Oh, okay.

**Dave Jones:** I didn't know who posted it. Okay.

**Chris Gammell:** Yeah. It was Jan. Uh, and so he listed the most popular 10 parts. Do you have a guess before you click on it?

**Dave Jones:** Uh, any sort of part?

**Chris Gammell:** I think hobby part.

**Dave Jones:** So any, well, we have five, five, five, obviously 7805 voltage rig. Uh, 741 op amp. Uh, you know, are they on the list?

**Chris Gammell:** I haven't looked yet, Dave. Well, okay. I did click on the link and five, five, five's at the top. So yes. Yeah. You were right about five, five, five. Yeah. And you know, I would put LN317 on there. Yeah. Yeah. Yeah.

**Dave Jones:** LN317, 7805 voltage rigs. Yeah. Right. Right.

**Chris Gammell:** Stuff like that.

**Dave Jones:** Yeah.

**Chris Gammell:** Probably like a 2N22222. Yep. Something like that. Did I say too many twos?

**Dave Jones:** Yeah. I've done a top five, uh, transistor video recently. Yeah. Yeah. There we go. Here's the list. There you go. Number one, triple five, number two, 7805. I called it. And 317. Yeah. And 595.

**Chris Gammell:** Oh, 595. Shift register. Of course. Yes. Yep. One N1, four, one, four, eight. Okay. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** I've actually, what I'm really looking at now is do I have this in my lab? I'm just like, oh, maybe I should be updating stuff in my lab.

**Dave Jones:** Uh, I, I think I've only got about 5,000 41, 48s. Oh, okay. So yeah, I better stock up again. Yeah. Um, and then 80, mega, 328, 80, tiny, 85. I don't know about that. Um, yeah. Yeah.

**Chris Gammell:** I, I could see it being a popular one. Yep. But, uh. Oh, yeah. Yeah. But I.

**Dave Jones:** Anyway, and the, uh, 2N7000 N channel MOSFET. Yeah. That would have been on my, um, video. If I did a dedicated MOSFET, uh, video. Yeah. That would certainly be LM324. Yeah. Of course. LM358. Yeah. Of course. So yeah, absolutely. No surprises there apart from the 80 megas, which, which I wouldn't have said.

**Chris Gammell:** Yeah. The tinies, the tinies are 80 tiny is, I know some people who are like, like, I remember Joe Fitz, who's been on the show a couple of times before. He's like all about 80 tinies.

**Dave Jones:** Yep.

**Chris Gammell:** And it just, it's, yeah, it's not, not for me.

**Dave Jones:** Well, I was into 80 tinies at one point. He used the 80 tiny 26. Um, and then I think that they like almost semi discontinued it at one point and it was like, Oh, what the hell? You know, it was like, but I think it's back now. Um, the 80 tiny 26, but yeah, yeah. I used to, I can see like the dip package too is like nice for that sort of thing.

**Chris Gammell:** But yeah, if you're doing like a custom.

**Dave Jones:** Yeah.

**Chris Gammell:** It did seem like it was limiting once you went off. Yeah. To try and like make a board then.

**Dave Jones:** I can't remember why I used the 80 tiny 26 at the time. I can't like, it had something that I needed. It had a AD converter that I needed. I don't know. It had something. It's I, I can't remember exactly. Um, but yeah, had one, one specific thing, which I think, ah, right. You know, that's what I'm going to use it for. God, I can't even remember now. That's so late. I was talking 20 years ago, more 25 years ago, maybe. Yeah. Long time. Hmm. There you go. Excellent. Yeah. We have.

**Chris Gammell:** Thanks.

**Dave Jones:** Yep.

**Chris Gammell:** I'll link in Jan's show as well.

**Dave Jones:** Excellent. We shall do that. Is our amp hour up?

**Chris Gammell:** I don't know. No, it's not.

**Dave Jones:** No, I've got eight minutes left. Come on. Let's stuff this turd full of, full of knowledge and wit and wisdom. Come on.

**Chris Gammell:** Oh, man. Oh, it is, uh, it is April 1st today. Did you? No, it's not, dude. Did you pull any stupid shit this year? Oh, sorry. It's April 2nd. It's a second for you. What do you mean? It's still April 1st here.

**Dave Jones:** I never pull any weird shit.

**Chris Gammell:** Oh, no, no. Of course. Not, not you.

**Dave Jones:** I don't know what you're talking about.

**Chris Gammell:** Okay. All right. Well, I'll keep that in mind. Yeah. That is, I guess you usually do post it on the 31st of March for everyone else.

**Dave Jones:** I don't post anything. I just post regular videos.

**Chris Gammell:** Regular videos.

**Dave Jones:** Regular videos.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** I happen to like to certain time zones. Like, hi to all my viewies in Kiribati, by the way.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yeah. But no, no, no idea what you're talking about. Okay.

**Chris Gammell:** How about this one? I was surprised by BeagleBoard.org. They released a new board and it is not, it's not a bone. It's not, it's, it's in the shape of a Raspberry Pi. I was surprised by that.

**Dave Jones:** Is it what? And it's got the pinout of the Pi?

**Chris Gammell:** Yeah. It's got a 40 pin pinout.

**Dave Jones:** So the signless finally relented and they've gone to the Pi form. Yeah.

**Chris Gammell:** I mean, like, I think the most surprising, so like, you know, like CNX software.

**Dave Jones:** That took a decade to happen, right?

**Chris Gammell:** Yeah. Right. I mean, so Jean-Luc is like one of the, you know, so CNX software is like writes about all these things and whatever. I don't think he mentioned it. That was the most surprising thing. It was just like. Yeah.

**Dave Jones:** It just, oh, by the way, it happens to have a Raspberry 5 interface on it. You know, like. No one, no one.

**Chris Gammell:** Do I have to say it?

**Dave Jones:** So is that the first Beagle product that actually has a Raspberry Pi interface? Maybe not. Maybe I'm just not paying attention. Because what is the Beagle one called? The bone. Is it called the bone? The bone, yeah. Right. It's called the bone board.

**Chris Gammell:** It's like the two pin. There's two rows of two pins on either side of the board. It's got the rounded, big rounded corners or whatever. Yep. That's right.

**Dave Jones:** Yeah.

**Chris Gammell:** No one's going to say it? Like, all right, well, I'll say it. So maybe. So I think what's probably happening here is I'm just completely out of the loop and missing the fact that probably Beagle board has been doing other stuff like this and I just don't know. Right. But it's got the TI AM67, you know, beefy ass processors on there. So, you know, it's all Linux-y. Linux-y stuff.

**Dave Jones:** And it's open.

**Chris Gammell:** It's like, that's a good question.

**Dave Jones:** It's got an open source hardware certification. It's got an official tick of approval by the.

**Chris Gammell:** If Jason was involved, then it's almost always, yeah, it makes sense it would be open.

**Dave Jones:** It's got an official certification mark. There it is. Serial number 2616. So there you go. So I guess whereas Raspberry Pi is not open source. Right. Like you can't download, you know, Jack for the Raspberry Pi apart from software.

**Chris Gammell:** Other good documentation is getting a lot more open, but yeah. Right.

**Dave Jones:** No, you can't download a schematic. As far as I know, you still can't download a schematic for a Raspberry Pi, let alone board files or anything else. I don't even think you can get a schematic. I don't know anymore, Dave. Yeah. Exactly. We're so out of the loop.

**Chris Gammell:** Oh, my God.

**Dave Jones:** Open source used to be a thing, you know.

**Chris Gammell:** There was a conference. There was an open source hub or something. There was. No, no. I mean, it just happened. Oh, right.

**Dave Jones:** Oh, it just happened. Right. Yeah. Yeah. It's still going. Excellent.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, but we were so into that, you know, space back in the day.

**Chris Gammell:** Just like KiCad, Dave. Right. I used to not even say KiCad.

**Dave Jones:** Yeah. I used to say KiCad. Yeah.

**Chris Gammell:** That's right. You're a KiCad fanboy.

**Dave Jones:** Right. Yeah. You find yourself slipping. Well, I do that with VIA and VIA, you know, because.

**Chris Gammell:** What do you say now?

**Dave Jones:** Oh. I try and standardize on VIA, which is very American.

**Chris Gammell:** Yeah. That's what I say. Yeah.

**Dave Jones:** Because VIA is what we would say here. But, you know, it's like, yeah. So I try and standardize, but I don't know. It just, it slips out occasionally. Yeah. You know what, man?

**Chris Gammell:** Don't worry about it. I know. It's all cool here. Yeah, but it bugs me. Nobody's listening to us. It still bugs me.

**Dave Jones:** Yeah. Anyway. Yeah. Yeah.

**Chris Gammell:** Yeah. Why does it bug you?

**Dave Jones:** Well, because like, it's like, I don't know what I'm saying.

**Chris Gammell:** Because like, you're like standing out and it's like questioning yourself. Yeah.

**Dave Jones:** It's like, and oh, the other thing, alligator clip, crocodile clip, like here in Australia, I'm supposed to, I'm supposed to say crocodile clip, right? But it's an, like, but I find myself trying to standardize on alligator clip. And even in the one video I've used both terms, you know, and that bugs me. What the hell? Crocodile clips. Yep.

**Chris Gammell:** Is it, is it because, is it because of Paul? Is that why you're supposed to say crocodile clip?

**Dave Jones:** As in Paul Hogan. Paul Hogan.

**Speaker ?:** Right.

**Dave Jones:** No, it's just, that's what they were called here. That's what they've always been called here. Crocodile clips. You know? Oh, man. Yeah.

**Chris Gammell:** I didn't know that. Oh, that's, that's great. Yeah. Crocodile clips. So do you feel like you're not Australian enough?

**Dave Jones:** Yeah, I feel like I'm not Australian enough. Yeah. Because I think they're only called that here. Like, you know, crocodile clips. There you go. You buy them at the local hardware store. Crocodile clips.

**Chris Gammell:** Dave, say it loud. Say it proud. Crocodile clips for you.

**Dave Jones:** I don't know. But it's also a hard word to say crocodile. It's like, you know, it's like, it's kind of, alligators kind of like, you know, it rolls off the tongue a bit better.

**Chris Gammell:** I've never, ever given it any thought at all.

**Dave Jones:** Oh, here you go. Alligator clips also referred to as crocodile clips in Europe. There you go. Europe also.

**Chris Gammell:** You know what you got to do? You got to band together with European brethren. Right. And take down.

**Dave Jones:** We can dominate those bloody yanks. Stupid yanks. Seriously.

**Chris Gammell:** Yeah. Take that. Yeah. Yeah. Stupid, stupid Americans.

**Dave Jones:** Apparently, RS Components here in Australia, they've got a, they call them crocodile clips. So, there you go.

**Chris Gammell:** I saw a news story that there was a crocodile in Florida, which is our backwater swamp of a state. Yep. Hello, Florida listeners.

**Dave Jones:** Sure you didn't, they didn't mistake it for an alligator.

**Chris Gammell:** That's what I thought. I thought it was all alligators there. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** But I think they actually did have a crocodile there. I don't know if it was imported or what happened.

**Dave Jones:** What? Yeah. In the wild? It didn't like escape from a zoo or someone's backyard? I think so. Yeah.

**Chris Gammell:** I don't know. I don't know. Maybe it's like a tourist, you know?

**Dave Jones:** Right. It's right. It snuck on a, it's snuck on a quadisplane.

**Chris Gammell:** And apparently, oh no, apparently there is an American species.

**Dave Jones:** Huh.

**Chris Gammell:** I didn't, I don't know.

**Dave Jones:** Oh, I might've heard of that. Yeah. I think you could be right.

**Chris Gammell:** You know what? They can all stay the hell away from me.

**Dave Jones:** Right. Ah, crocs are nothing to worry about.

**Chris Gammell:** Nope. They are something to worry about.

**Dave Jones:** Dude, don't have to worry about a croc if their jaws are open. If their jaws are closed, you don't have to worry about it. Because you can just hold their jaws closed with your hand. They've actually got no opening force. Crocodiles, a crocodile safety tip for yanks.

**Chris Gammell:** I'm not doing any, I'm not doing any of that. No? Okay. None of that for me.

**Dave Jones:** No, just jump on the back and hold their jaws down. And no, no worries. Although if you've got one of the biggies, though, they might take you for a, for the old death roll. But, you know, you've got to be careful of that.

**Chris Gammell:** Right.

**Dave Jones:** Because, yeah, the death roll's a thing where the crocodiles.

**Chris Gammell:** Are we back into you wanting to sound like, be more Australian? Right, obviously you meant be more Australian.

**Dave Jones:** But yeah, you can hold the jaw of a crocodile. Haven't you held the jaw of a croc actually closed before?

**Chris Gammell:** I have not.

**Dave Jones:** Oh, there you go. You're missing out.

**Chris Gammell:** Yeah.

**Dave Jones:** It's an invaluable life experience. Anyway, yes, you only have to worry about crocs if their jaws are open.

**Chris Gammell:** The to-do list for 2014, simulate more things and try out ANSYS products and hold a crocodile's

**Dave Jones:** snout shut. The jaw is closed. Snout shut. Yeah. Because they don't have much opening force. But downward force, about, you know, 2,000 pounds per square inch or something, you know. Yeah. Snappity, snappity. Snappity, yeah. Snappity, yeah. Yeah, but opening, no, they actually, no, they're very weak opening. And it actually takes them time. So they can't just open it in like a split second. They, you know, it takes time for them to open their jaws. So if their snouts are closed, no worries. You go up and pet them.

**Chris Gammell:** I shan't.

**Dave Jones:** No? All right. No. All right. Sure you don't want to come back over here and we'll go on a trip? Yeah, I know. No.

**Chris Gammell:** No.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. No worries.

**Chris Gammell:** All right. Well, we're ending on crocodiles, I guess.

**Dave Jones:** Oh, boy. We can do a great AI-themed thumbnail for some sort of crocodile with clip.

**Chris Gammell:** I'm sure AI gets crocodiles and alligators backwards, I'm sure.

**Dave Jones:** Probably. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. Well.

**Chris Gammell:** I think we can all agree. Florida is terrible.

**Dave Jones:** It's more freer than the other states, isn't it?

**Chris Gammell:** Yeah. It's more something. It's more something. It's more something. Okay. Yeah. It's a lot of more of a lot of things. All right.

**Dave Jones:** Oh, I just heard today that house prices in Florida have gone up like 60% in a year or something.

**Chris Gammell:** Well, they can keep them. I'm not moving. I'm not moving there anytime soon.

**Dave Jones:** Okay. No worries.

**Chris Gammell:** All right. More electronics, probably. I don't know if we're going to show next week. Dave might do a show next week when I'm at the conference. I will not be recording at the conference.

**Dave Jones:** I'll see what I can do. Okay.

**Chris Gammell:** Yeah. If not, we'll see in two weeks.

**Dave Jones:** All right. Catch you next time.

**Speaker ?:** Bye. We'll see you next time.
