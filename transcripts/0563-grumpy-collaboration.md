---
episode: 563
title: Grumpy Collaboration
url: https://theamphour.com/563-grumpy-collaboration/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release October 24th, 2021. Episode 563. Grumpy Collaboration.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** I've moved on from our past episode about assembly during an episode. Now I'm burning a Raspberry Pi compute module image as we record. It's been giving me some hassle, so we'll see if it goes.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** Bootloaders and such.

**Dave Jones:** Don't you just stick an SD card straight up its clacker?

**Chris Gammell:** You would do that. Yes, for a normal Raspberry Pi you would. This is the compute module, so it actually plugs down onto the board. And there's two versions of it. There is the CM4, the compute module for Lite. And that actually has no solid state on board.

**Dave Jones:** And so then you actually have to have an external SD card. Wow. That's right.

**Chris Gammell:** So you can basically run the lines out from these headers. It's like two parallel high-density headers, basically. 50 mil spacing or 50,000 spacing. I've routed that, but then I also have a... I actually got the version that has Wi-Fi. Basically, I'll just get whatever's available at this point. Yeah. Yeah. And so the one I have has like 32 gigs of flash on board. And so you have to basically plug in USB. There's a switch you have to hold low. And then there's a script on your computer that'll put it into bootloader mode. And then now it's like mass storage.

**Dave Jones:** Yeah. But what's the point of a board like that? I guess it's, what, saving 10 cents for the SD card connector? What's it? Because like...

**Chris Gammell:** No, it's... SD cards are just not reliable enough. You know, there's like the industrial ones. Okay. Those are better. But this is just for... So, you know, just industrial environments.

**Dave Jones:** Yeah. Yeah. But you've got to have the memory external to the board. So, like...

**Chris Gammell:** Oh, no, no, no, no. So, the memory, the flash memory is on the CM4. And so... Oh, okay. The quote unquote light version, they just don't populate it.

**Dave Jones:** Oh, okay. Gotcha. Yeah. All right.

**Chris Gammell:** Yeah. Okay. So, I think we're going to see these in a lot of things, honestly.

**Dave Jones:** Yeah. But what's it for then? If it's external memory, like, so, okay, size, form, factor, cost. But you've got to put the memory external somewhere.

**Chris Gammell:** I'm a little confused. Sorry. So, there's the two versions. One is an SD card that's off the plug-in board. Yep. And the other one is flash memory that's on the plug-in board. Oh, that's on the... Okay. Right. So, it does... Yeah, yeah, yeah.

**Dave Jones:** Okay. Right. Yes. Okay. So, the one with the SD card does not contain the flash memory built into the... That's right. Built into the processor. Got it.

**Chris Gammell:** So, the net effect of that is it's just a little bit more hassle to program it. So, you know, you've got to program it in situ using a USB cable, which is USB 2.0, kind of slow for a 32 gig image. Well, 8 gig image. Yeah, that's fine.

**Dave Jones:** You do it once, you know. I mean, it'd be annoying if you were changing, you know, environments all the time, but...

**Chris Gammell:** Well, no, the tough thing is the... If you think about the... It's about 10 minutes. 10 minutes per board at, like, the speeds I'm working at. Yeah. So, if you think about that per... You know, if you're actually doing production with this sort of thing. You know, that's what they're targeting, you know. Yes, true. You know, whether or not people actually do that, that's fine. You know, for doing production, that's pretty significant. Oh, sure.

**Dave Jones:** Well, people don't think, oh, what would you use Raspberry Pi for production for? Well, the new one, the new compute modules, they come on reels. We've had this on the show before. They actually... You can physically buy the thing, the complete module, on, like, a two-inch wide reel. So, you put it in your pick-and-place machine. It's...

**Chris Gammell:** Yeah, I've seen that for the Pico. I haven't seen that. Does they do that for the CM4 as well?

**Dave Jones:** Oh, I'm not sure. Okay. It's the Pico I'm thinking about. The Pico.

**Chris Gammell:** Pico, for sure, because that's the one that has castellated edges. Yes. CM4, I've only seen in boxes, but, you know... Okay. Yeah, I could see them doing that sort of thing. The only thing is, it's kind of like... It's, like, got a pretty hard press fit into these connectors. And, you know, good luck finding those connectors. Right. Okay. Yeah. Luckily, bought a lot last time I did it.

**Dave Jones:** Are they just Samtech jobbies, or what are they? What's the standard...

**Chris Gammell:** They're not Samtech, but they're, you know, the same kind of, like, high-density.

**Dave Jones:** Yeah, yeah. But, so, they're not, like, a big-name brand standard?

**Chris Gammell:** No, they are. I just don't remember what it is.

**Speaker ?:** Oh, right.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah, I can look it up. I want to say Molex, but it's... Usually, I don't think, like, super high-density for Molex. Yeah, so, I'll look it up. Maybe it's Panasonic, even. Yeah, I don't know. We'll see.

**Dave Jones:** Okay.

**Chris Gammell:** But, yeah, you know, CM4. I mentioned a little bit on the board, on the show here before. So, continuing on and programming them. But, it's... I've been having this issue where I... The flash keeps failing on validation, and that's the...

**Dave Jones:** On validation. So, it programs, and then it does a validation cycle. That's right. A check-in pass, and it fails.

**Chris Gammell:** Yeah, that's another eight minutes, actually. So, 18 minutes per run.

**Dave Jones:** Yeah, 18 minutes per board. Wow.

**Chris Gammell:** Yeah. It could be my setup, honestly. It could be my setup.

**Dave Jones:** Oh, that's really... Is there a faster way to parallel program it, or do you have to do it via, like, the USB 2, or whatever? I don't know.

**Chris Gammell:** I don't know. I'm sure you could probably make a little programmer, maybe. And maybe... Yeah, maybe USB 2, if you... I don't know. Maybe my default on my computer is slow, whatever. So, I'm sure there's some way you could speed it up. Okay. But, I'm not currently there.

**Dave Jones:** Yeah, that's killer. But why it's... Because this uses... For those who don't... Oh, God. I'm not going to be able to remember the name. It uses the cheap... The MMC flash memory, is it?

**Chris Gammell:** Mm-hmm. Yeah. Which is different... EMMC, usually, yeah.

**Dave Jones:** EMMC, yeah. Flash memory. I can't remember what the exact details of it are, but it's like the cheapest version of regular flash memory. It's like... I'm not sure in what way it's different.

**Chris Gammell:** I didn't think so, but...

**Dave Jones:** Right. Okay. I'm going to have to look that up.

**Chris Gammell:** Yeah, I don't know. But, yeah, I'm basically programming it like an SD card, and it just failed. So, yeah. Try again later. More exciting updates from the lab of Chris.

**Dave Jones:** Oh, no. Well, here it is. Straight from HowToGeek is the first Google result. EMMC is the kind of flash storage you'll find in cheap tablets and laptops. It's slower and cheaper than traditional SSD.

**Chris Gammell:** Interesting.

**Dave Jones:** So, yeah, it can't compete with regular solid-state drives. It's NAND and EMMC, all you need to know. Yeah, they are different. What's the difference? Here we go. Windows Central will tell us what the difference is. However, the superior format... No. Okay. It's probably just the surrounding circuitry that makes it better. I'm not sure if it's the actual physical flash structure itself that differs. Anyway, given that this just came up, we have no idea what we're talking about. So, you know, I just knew that there was a difference. That's all. So, maybe your issues... I mean, but that's insane that it could program. And then, like, you know, you're not used to modern flash failing, right? You write your file to your SD card, and you don't bother doing a verification check.

**Chris Gammell:** I think this is my setup, honestly. Yeah, I don't think it's a...

**Dave Jones:** Like, it's not just a dodgy cable, is it? Dodgy UA. But then it'll give you an error. I thought when it's copying, surely it'd be doing some sort of CRC when it's copying.

**Chris Gammell:** Wouldn't it? Yeah, yeah. Or... Well, it checks it, I think, the whole image after the fact.

**Dave Jones:** After the fact. Okay. So, they're... Oh, wow.

**Chris Gammell:** I just sent through the link to the Unobtainium connector that you can check out if you'd like. It's a Hirose, a high-density Hirose, 100 position. Oh, right. So, you need two of those. Basically, it's a 50-pin per side, 50 mil. Yeah. 50 mil pitch. Very... Oh, no, 40... Oh, 0.4 millimeter pitch.

**Dave Jones:** Well, high-rose. I'm not going to say high-rosy. I'm going to say high-rose. Yeah, they're a big manufacturer, so it's not like it's a... You know, they've just chosen some...

**Chris Gammell:** It's Hirose. That's...

**Dave Jones:** Yep. I'm sure that's how it's pronounced.

**Chris Gammell:** You pronounce each syllable.

**Dave Jones:** Yeah, but I'm going to call it high-rose.

**Chris Gammell:** Dave, I took three semesters of Japanese in college that I completely forgot. Yeah, I know.

**Dave Jones:** I don't care. Just like I don't care about, you know, Bodhi plot. It's Bode plot.

**Chris Gammell:** Yeah, that's true. Screw you. I guess I can't say much here. It's Kikad as well. You know. Yeah, right.

**Dave Jones:** Even though it's Kikad, yeah.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, interestingly, on the Raspberry Pi side of things, so they just launched a new site as well. I mean, like, you know, we've been seeing them move more and more into the commercial side of things over time. Yes, they did a .com.

**Dave Jones:** It used to be .org.

**Chris Gammell:** Yeah, they now have a .com. That's right.

**Dave Jones:** I didn't understand the reason for that. They wanted... I know they didn't explain a page, but I just sort of went, what? Yeah.

**Chris Gammell:** Yeah. I think it's just representing the fact that there is more commercial interest, basically. You know, targeting... Right. Yeah. And I think the .org is also sticking around for the education side of things, right? So they actually have it as a charity thing, and then they're probably... Yeah, yeah. Yeah. Maybe tax. I don't know what that side of things are, but...

**Dave Jones:** Right. Okay.

**Chris Gammell:** But, you know, they legitimately... You know, we had those guys on the show talking about Pico and their future plans, and as much as they were able to talk about it, which is a great episode if people haven't heard it. We had Evan on the show many, many years ago, and, you know, they're just moving more in this direction and, you know, bully form. I think it's great. I think this kind of thing is making Linux computing more accessible, and that's a good thing. There is.

**Dave Jones:** I will have to link down below a... It's almost a Raspberry Pi hate thread on the EEV blog forum. Let's just say that there are some people who are not happy with the way Raspberry Pi are doing things, and there's very...

**Chris Gammell:** Well, it is the internet, Dave. Yeah.

**Dave Jones:** I won't go into it. Like, I don't know the substance behind their complaints and stuff like that, but anyway, I'll link it in down below. There is... It's not all roses in the Raspberry Pi fandom, you know? Well, no doubt.

**Chris Gammell:** No doubt.

**Speaker ?:** Right.

**Dave Jones:** They've got... This is on the .com page. They've got an Apple-like Raspberry Pi store. I'm sorry, but this is pure wankery. This is just marketing wankery. No, I don't like it.

**Chris Gammell:** The store is, like, very fancy. I just feel like... It's very fancy. It's very... If you're going to hire a modern web design firm, you're not going to get, like, you know, a Mauser or a DigiKey these days.

**Dave Jones:** No, I'm talking about the... No, a physical store.

**Chris Gammell:** Oh, where's... I don't actually see that.

**Dave Jones:** Go to raspberrypie.com and then scroll down and you'll see a physical store.

**Chris Gammell:** That is always an interesting shift to me for... Oh, I see what you're talking about.

**Dave Jones:** I presume it's in Cambridge because they say Cambridge store and they've got, you know, yeah. Yeah, nah, as we say here in Australia.

**Chris Gammell:** Yeah. I just can't imagine being like, you know what we should do in 2021? Brick and mortar. Brick and mortar store. Yeah. That's the... During COVID. That's the ticket, laddie. Yeah. Yeah, right, right. That's really... We're really going to ramp it up in Cambridge, UK.

**Speaker ?:** Right.

**Chris Gammell:** Like, I'm sure it's very nice. And, you know, like, I just always feel like when it's not an app... You know, like Apple is allotted for their, you know, their store and that's, you know, whatever. Apple's Apple.

**Dave Jones:** Right.

**Chris Gammell:** But, you know, what other people are doing, especially on like single scale...

**Dave Jones:** Yeah, but Apple is the experience, right? Sure, exactly. Apple is the pure fanboy wankery experience. That's why they have the stores. Come on, Raspberry Pi?

**Chris Gammell:** That's the thing. That's what I'm saying is like, when it's this sort of thing, it's like, we want to showcase it. We want to have it as a thing. It's like a tourist destination at that point, you know?

**Dave Jones:** Right. Okay. Yeah.

**Chris Gammell:** I think that's great, but it's like, it's a pet problem. I don't expect to see a Raspberry Pi store in every city.

**Dave Jones:** No, they're not, you know, selling them. They're not making their two bucks profit on each board or something, and they're making a killing at their store. No, it's a total loss leader. Like, it's a total loss.

**Chris Gammell:** Yeah, it's a marketing exercise. It's a marketing. It's great. Yeah. I think it's great. I have no hatred for this.

**Dave Jones:** Yeah, I just groaned when I saw that.

**Chris Gammell:** Dave, you strike me as a shopper. I'm surprised you don't enjoy a good retail, little retail therapy.

**Dave Jones:** I do enjoy the retail experience, but not for my Raspberry Pis. No.

**Chris Gammell:** You're more of a fries, like abandoned fries going under.

**Dave Jones:** I want to get my Raspberry Pis from a dingy warehouse. You know? That's where I want to get them from.

**Chris Gammell:** Got it.

**Dave Jones:** I don't want this glitzy, bright light Apple experience. No.

**Chris Gammell:** It's wrong. Okay. Well, you don't have to go there. You don't have to fly. Okay. I am not flying to Cambridge.

**Dave Jones:** Then next time I'm in Cambridge, I am not.

**Chris Gammell:** I'm going to boycott the Raspberry Pi store. Good. Yeah. Yeah. Instead, you can just go see historical campuses and such. Right.

**Dave Jones:** Okay. Yeah. Like 500-year-old campuses and shit. That's older than all in Australia, you know? Yeah. That's right. You know, modern Australia. Yeah. Sure. Anyway. There you go.

**Chris Gammell:** Yeah. Well, you and Mehdi were talking about kit businesses and buying from kit stores. I was just listening this morning. Oh, yes. Right. I was enjoying that listen. It was always fun to listen to Mehdi. Yep. From Electro Boom, if people haven't listened. Electro Boom.

**Dave Jones:** If you want a timestamp, it's towards the end, probably like an hour into it or something. It's not a timestamp. Just so we're clear. No. It's not how you timestamp. But it's towards the end of the video. Yeah. We talk about the kit business.

**Chris Gammell:** If you want a GPS location, it's up the block, about three, four blocks and take a right.

**Dave Jones:** I should look them up on Google Maps. I'm sure I could find all the, you know, this, you know, Silicon Alley, as we used to call it here in Sydney, and which has all the electronics shops. Yeah. Yeah. Anyway, this is in Iran. Can we actually even get Google's stream view in Iran? I'm doubting it.

**Chris Gammell:** I don't know. I don't know.

**Dave Jones:** I'm doubting it. Okay.

**Chris Gammell:** Another thing you guys were talking about that I was, that was very well timed. It was like my choice this morning when I was walking was either talking, listening to the Amp Hour, which I obviously chose to do, or listen to the book I've been listening to, which you guys also mentioned, which was Surely You're Joking, Mr. Feynman. I actually just started re-listening to that, and if people have never listened to it, it is just like such a, like a bit of mischief, you know, like, it's just like, he's such a goofball and like a mischievous rule breaker, and it's just a lot of fun to read. It's also kind of like an interesting writing style, because it's very plain in a lot of ways, even though it made me, you know, it makes me laugh and whatever. Or it's just like, oh, and this thing happened, and, you know, I went on a date with this girl, and, you know, then we went to a cafeteria. And it's just like very, like, stream of consciousness, kind of like, you can tell it's a nerd writing it, and yet it's like really smart nerd, you know? It's just like, I don't know. It's a very, I'm enjoying it a lot. So, highly recommend that. Click the Audible link. We'll have, no, I'm just kidding. Our sponsor for today's show. Yeah, right, right, right, right. Yeah. Yeah. Cool. Yeah, classic book. Classic book.

**Dave Jones:** Anyway, yes, we're talking about electronic stores, but you don't have this background, because you don't come from a hobby electronics background. You got interested in electronics at university.

**Chris Gammell:** That's right. Yep. Yeah. Although I do live around, well, I lived around some of the few remaining US-based stores, hobby stores, which was Micro Center. They're pretty much the only ones left, as far as I know.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** And the surplus stores like Apex and stuff like that, which I visited, which is absolutely fantastic.

**Chris Gammell:** Apex is still around. I'm not, HSC, a lot of the Silicon Valley ones have closed down. Yeah. I think, yeah, there's very few left. Those are gone now.

**Dave Jones:** Yep.

**Chris Gammell:** Yep. It's too bad.

**Dave Jones:** Yeah. Yeah. But whereas you go into Apex, it's not an electronic store. It's a junk store. No, it's a junk store. Yeah. It's pure junk. It's just unbelievable. Yeah.

**Chris Gammell:** You had a video you did there? Yeah. I've got a video.

**Dave Jones:** That was back in 2010 or something. Yeah.

**Chris Gammell:** I'll link that in.

**Dave Jones:** 2009 even. I don't know. Something like that. Yep.

**Chris Gammell:** Yep. Junk stores across the ages. Yes. Dave also goes to dumpster rooms when he's on vacation.

**Dave Jones:** And you should have. And because we were on holiday, you should have seen the eyes roll in the back of the head of Mrs. E.E.V. as we're. Yep. I can imagine. Let's. This store, it's really good. And then, yeah, you could imagine her eyes rolling in the back of the head as we're going through these aisles of, you know, very, like, very narrow kind of aisles with gigantic steel shelving with, you know, scopes going up to the roof, you know, like. Everything's looking like it's going to topple onto you. Yeah. It's just. Yeah. I don't think she could get out of there quick enough. Yep. Anyway. It was fun.

**Chris Gammell:** Yep. Well, speaking of things that were a bill of sale and interesting buying opportunities, Tempo Automation is going public and you can soon buy their public stock. This has been an interesting, interesting development. Tempo Automation. Yes. So Tempo Automation is a assembler or assembly house. They're like a digitally enhanced assembly house, you know.

**Dave Jones:** What's a digitally enhanced assembly house?

**Chris Gammell:** Well, you know, we've had people on here in the past, like Circuit Hubs, like an example of that. Macrofab's an example of that, you know, like basically kind of. Online. It's not just. Yeah. You don't just email in your Gerber. Right.

**Dave Jones:** You don't email the Gerber. It's all integrated on the website and it's all.

**Chris Gammell:** Yeah. Yeah. Although, so I was, I was going to, I tried using Tempo a couple months ago, I suppose, and it was really slow and it was, it was just a, it was basically like having a zip file upload. You know, I thought, you know, they had developed like this fast process and maybe it's all on the back end. But the, I was very, at the time I was very unimpressed. It took them like three days to get back to me for a, you know, for seemingly a very quick, you know, they're supposed to be super quick turn in the Bay area. They're actually in San Francisco, which is interesting in its own right. And they're supposed to be this like super fast turn thing. And it took them three days to get back to me.

**Dave Jones:** No. So I'm looking at their website and it's just, no, upload your design files to our secure cloud portal. Step two, bomb audit. Step three, quote. Step four, DFM. Step five, tracking. Try it now. It sounds like a, just a regular assembly house with just a, but it shows you like, but most assembly, a lot of assembly houses do this these days. It's been doing it for a decade. They've been doing it for a long time. They show you where your board is in the process. Yeah, exactly. But it's nothing like, no.

**Chris Gammell:** Well, and I'm remembering it from like what it started out as, and I'm sure it's transitioned. So like it started out as like this very utopian sounding like, oh, we're going to have machine vision and lots of robotics and all this other stuff. And I'm sure economics drove it to the point where it's like, oh, no, no, we're just going to do a lot of fast boards at high margin because it's, you know, because Google is up the street

**Dave Jones:** and practicality hits you in the head. Yeah.

**Chris Gammell:** Yeah, exactly. But the news is not that. The news is that they also bought advanced circuits, who is another quick turn board house in the US. Very expensive boards from my experience. Very expensive. So they bought them. Wiz, I don't know who Wiz is.

**Dave Jones:** Yeah, but when you say very expensive, what are you talking about? Because I'm going to give you when I was a boy.

**Chris Gammell:** I'm going to give, okay, so two layer board, two day turn. I think it was black solder mask, black matte solder mask. And it was for like 200 boards, maybe 300, 400 boards. I don't remember how many boards. It was like $8,000. Like the per board cost for two layer board was astronomical. Right. It was like eight bucks a board for, because it was all quick turn.

**Dave Jones:** Oh yes. If you want that sort of volume quick turn, yes, you're going to pay for it because they're going to put through full panels on your behalf.

**Chris Gammell:** That's right. Yeah. And it was quick turn off. Yeah. And they weren't small boards either. And it was quick turn off color as well. Right. So it wasn't just standard solder mask. It was black matte. So it was like custom. And yeah, I mean, but that's expensive. I mean, I expect a two layer, you know, blackboard to be cheap, but it was, I had other, it was just my expectation.

**Dave Jones:** Right.

**Chris Gammell:** But every time I've gotten other stuff, you know, equivalent stuff quoted, it's pretty expensive.

**Dave Jones:** Right. Okay. Anyway, so they bought them, right? And who else do they do?

**Chris Gammell:** Who else do who do?

**Dave Jones:** Oh, sorry. So they bought advanced circuits.

**Chris Gammell:** They bought advanced circuits and whiz systems, which sounds like a urination assistance.

**Dave Jones:** Yeah. I won't tell you what it sounds like.

**Chris Gammell:** And at the end of all this is this thing called a SPAC. And you had never heard of what a SPAC was, but I have heard about it because I enjoy listening to the Prof G show, the Scott Galloway podcast. And he talks about these things all the time. It is a special purpose acquisition company. And so what happens is these companies basically raise money with the idea that, hey, we're going to, we're going to basically get acquired at some point. And literally there is no knowledge of what they're going to actually do because they can't say it beforehand. So like they raise all this money. There's no like knowledge of what they're going to buy. And then they go and basically merge with a company that wants to go public, but doesn't want to deal with going public. And so basically people have already bought into these things. Then they go and merge and the already public company that is the SPAC merges with the company in question, which in this case is Temple Automation. And then usually they take over the branding and all that other stuff. And now Temple Automation is a public company. It's a public company that is basically an assembly house, now two assembly houses and a PCB assembler or PCB manufacturer. Would you like to guess how much they're worth, Dave?

**Dave Jones:** Well, now given that we're talking to no one now, because everyone's just like tuned out.

**Chris Gammell:** Someone's listening because they're like, oh, money. I like money.

**Dave Jones:** I'm going to guess it's close to like, it's half a billion or a billion or something.

**Chris Gammell:** It's a $920 million estimated post-transaction equity based on current assumptions. That is- Based on current assumptions. Bananas.

**Dave Jones:** It's just, yeah. For an assembly house. Someone's got too much money.

**Chris Gammell:** For an assembly house.

**Dave Jones:** Someone's got too much money.

**Chris Gammell:** No, the world's got too much money right now. Yeah.

**Dave Jones:** The world's got too much money. Yeah. No, it's not just one person. There's- Yeah.

**Chris Gammell:** And so what's interesting about this too is that basically the SPAC company bankrolled buying advanced circuits and they also bank, I think they bankrolled buying these other two things. So basically they said, hey, you want to make a deal? Hey, buddy, you want to make a deal? Let's all get together. We'll buy out, we'll buy out advanced circuits. We'll buy out Wiz. And then basically we'll become Tempo. And it's just like, oh my God.

**Dave Jones:** Uh, yeah, nah. It's like, I know, like there's not one person making this decision. Like it's like funds investing in this. So it's like they just invest in multiple things and they probably don't even know what the hell they're investing in.

**Chris Gammell:** Well, and that's the other thing too, is that they're, I mean, so Tempo Automation also raised a bunch of money over time. So like they have VCs behind them. And so I'm sure the VCs are the ones that coordinate all this because they want to get their money back. You know, they want to, they want to become a big, big. Expensive thing. So anyways, it's very interesting that there is anyone who thinks an assembly house is worth $920 million. I haven't, I haven't.

**Dave Jones:** Maybe you've got some lucrative government contract. Maybe. Maybe.

**Chris Gammell:** But Dave, apparently once again, we are in the wrong business. Yep.

**Dave Jones:** The highly lucrative podcast business.

**Chris Gammell:** That's right. Yeah. Well, yeah, I think we're in the wrong business.

**Dave Jones:** This just, no, this is just, this is just. It's not so.

**Chris Gammell:** Yeah. Anyway. It's munkers. I would be interested to hear, you know, from people who are listening, I'm sure some of them have used Tempo. I'd be curious to hear how it went, what it was like, if you think they're worth it. Just generally. I don't know. I don't, I haven't heard of Wiz before, so I don't know what that would be like. I've used advanced PCB. I probably didn't say advanced assembly. That's a different company. Advanced Circuits. Sorry. It's 4PCB.com. This is actually the first company I'd ever used for DFM because I used to use Eagle. And then someone had told me, Hey, if you go to 4PCB.com, you can upload your files and they'll send you a DFM report. And so they actually had like an online processor of things. Yep. And I didn't have DFM apparently in Eagle. I'm not sure. But that was actually for young Chris, that was a wonderful service. So I will say that is my favorite thing that has come out of this. So nice job acquiring 4PCB.com. That was a young Chris thinks you've done a great job.

**Dave Jones:** Well, let's come back in five years time and analyze whether or not they've completely come a gutter or whether or not they're. Yeah, I think that's right. Yeah. Or whether or not they've been a raging success and they're worth more than Apple.

**Chris Gammell:** Maybe, maybe. Yeah. Maybe they merge with Apple. Who knows?

**Speaker ?:** Right.

**Dave Jones:** Well, that's probably the play they're after, right? Is to be gobbled up by the next, right? Is the next biggest thing. Yeah, the next biggest fish.

**Chris Gammell:** Yeah.

**Dave Jones:** The trick is getting off the merry-go-round before it breaks down.

**Chris Gammell:** Yeah. Yep. Yep. Yep. Good luck to all involved. I hope you made a lot of money. We have no idea how all that stuff works. Start more electronics companies. Stuff works. Yeah. Yeah.

**Dave Jones:** Oh, boy. Haven't got that much money to piss away, I'm afraid.

**Chris Gammell:** Well, if you did, you could piss away on a $12 million on a hardware design tool in the browser.

**Dave Jones:** Yeah. Here's another, like, what the, why? I mean, how many of them are there? Could you even count them on two hands? I don't know. I don't know. How many online PCB type, you know, tools there are.

**Chris Gammell:** Yeah. I don't, I don't know, but they.

**Dave Jones:** This is not just a, actually, I don't even think it's a PCB tool. I think it's, it's a design collaborative tool. It only seems to have schematic. Although, no, they did show a screenshot of PCB. Okay. Yeah. Right. But, yeah. I mean, it's. I'm sure it's fine. Yet another, it's, it's their own thing. Right? It's not based on a key CAD backend or anything. It's just their own.

**Chris Gammell:** They, they started fresh. It looks like.

**Dave Jones:** Someone's written their own online tool and, uh, I don't know.

**Chris Gammell:** Yeah. I mean, so we've had Upverter on the show many, many years ago. They have since been acquired by Altium. Yep.

**Dave Jones:** I think maybe one or two of them are still there. Is it still, I haven't been there in a couple of years. Does it still work as Upverter? Yes. It, uh, the website's there. It's still online. So, yeah. It's online. Yeah. Okay. Right.

**Chris Gammell:** Uh, there may be people using it. I don't know.

**Dave Jones:** Well, there were when they bought it. I wonder if they're still using them.

**Chris Gammell:** Yeah. I don't, I don't know. I don't know. It looks like it's a little bit more of like a marketplace kind of thing. Yeah. So maybe it's a.

**Dave Jones:** Let's, let's see if there's much happening on the forum. The forum's always a tell. Three replies, 600 views, March 2, you know. There's a few people pottering around on there, but not much.

**Chris Gammell:** Yeah. I think that actually is a, it's a decent measure of, you know, it's like, if you just see the people that are supporting it, then, you know, maybe it's just, there's not much community there that happens. Right. But, uh, yeah.

**Dave Jones:** Anyway, I've watched their wanky promo video and it's. I did as well. It's.

**Chris Gammell:** It was, it was very nicely made.

**Dave Jones:** Oh, it's beautifully produced and shot with their, probably they got in some, you know, company with a $15,000 black magic camera and they, you know, cinemagraphically shot it and, you know, with their prime lenses and their wank, wank, wank. Yeah. And all the fancy animation. And basically all that plugs in, this is why I thought it didn't have a PCB tool is because they didn't show the PCB tool in there. They showed the schematic and how you drop modules in and they magically do this. And then you can probe points and then it can show waveforms. And then it's a collaborative tool. That seemed to be their main thing is that you don't design. You, you're not alone design engineer in the dungeon designing a board. Sorry, but yes, you are. That's how much, that's how it almost always happens.

**Chris Gammell:** What if we want to be?

**Dave Jones:** Exactly. It's like, then flux is not for you. Yeah. Yeah. It's, I don't know. I mean, for some. It's collaborative. It's as if you're going to have 10 people working on your schematic all at once. It's like, oh, come on. Yeah.

**Chris Gammell:** I remember seeing that with the, you know, there was a bunch of like community based projects when people were doing a lot of the ventilator projects, you know, like looking to get involved or whatever. And it's just, it is so tough, you know, like all it takes is one Bose to be like, but what about that? You know, like it's like Dave being like, well, you shouldn't really put reference designators on all your components. And I'm like, Dave, come on, just, you know, stay in your lane, Dave. You know, so maybe, maybe this online tool could like just auto put all the reference designators or something. I mean, here's the thing. I feel, I feel bad for, this is a tough thing to bootstrap. I say this was legit kind of thing. Like it was the most legit thing out there. It is tough to bootstrap from nothing, especially in hardware, because you got, you got grumpy old bastards like us being like, ah, never.

**Dave Jones:** Yeah, I've used Altium for 30 years.

**Chris Gammell:** Right. So maybe give it a try. I don't know, but I will not be using it. Obviously I'm in a very different camp. No, I am.

**Dave Jones:** No, I'm not going to use it. No, it's just, no.

**Chris Gammell:** I was referred to on Hacker News the other day as having drank the KiCad Kool-Aid, to which I respond, that is correct, sir.

**Dave Jones:** No, look, when I was working at Altium, right, they got the brilliant idea for online collaboration, right? This exact thing, right? This was back in 2009, May 2008, probably, something like that. Anyway, they like, and I just said, no, nobody wants this. Like there are so few people want this. Why are we putting priority on this? And it's, oh, just try it out. And they sort of forced us as the hardware design team to like try it out. It's going, no, this is bullshit. No, this is just dumb. This is an absolute waste of time. Yeah. Even, you know, like forcing us to use, you know, to use this thing. It just, no. Yeah. It doesn't work. Even the most advanced designs come down to typically one person, right? One person's doing the schematic. Maybe a different person's doing the PCB, right? Maybe you'll have a couple of hardware designers doing different aspects of the schematic in larger, you know, parts, larger design teams. You know, like if it's like huge boards and stuff like a massive boards. But no, you would typically have just, you know, one person in charge of that. And it's like, yeah, you can have multiple design engineers, but they don't need access to the tool. You can just sit in a meeting, give them the schematic as a PDF and, you know, check it over for them, right? And then it feeds back and there's one central person who makes all the changes and, you know, it's one thing to get design. I can see why they're doing it. And there is some advantage here, right? I'll play, right? There is some advantage in that. Yeah. Then like somebody can get into the tool. Another design engineer can get into the tool and then, you know, use the PCB tool. And then, I don't know, put a circle around something saying, what is this? This is a bad layout. Fix this, please. Right? Or something like that. So they can leave notes and stuff like that. But you don't need a fancy online design. I mean, you could do that in a PDF. You can do that in PDF.

**Chris Gammell:** Not to be that guy, but. I know. It's like. You can do that with a 555, man.

**Dave Jones:** It's just, yeah, nah. Nah. And that's like, and that is almost the sole focus of their software. It feels like when you watch that promo, it's like, this is the solution because you don't design alone. Therefore, you need this. And it's like, no, we don't. No. I'm sorry. Yeah.

**Chris Gammell:** So this was a conversation that came up a bunch on. So I had Zach Friedman. We did the combo show where he was on here. We did this. I recorded with him and I posted him both in the Contextual Electronics podcast in here. And so one thing Zach talked about is like, engineers are fundamentally working alone. And boy, oh boy, did people on the internet not like that. And I have to say, I'm still in Zach's camp. Like, I agree that like people are collaborating. There is no doubt that you need to be able to collaborate. You need to be able to meet with people. You need to be able to make decisions. You need to like push and pull and all that kind of stuff. But Zach's point, as far as I understood it, and I think like he clarified online, is that like at the end of the day, like the hard yards, like the calculations are like, like you're saying it's you're in a dark basement. You're just trying to get stuff done at two in the morning. You know, and it's just like that, that doesn't have to be the only experience. But I, I think personally that that is part of the experience. And yes, and I think that like having resources, I think maybe the unstated piece or the piece that I will add after that, the unstated pieces you had like learning to get comfortable in that discomfort is a very valuable skill, you know, like trying lots of things, the things I've talked about in the past with like, like Ben Krasnow and like just having rigorous methods and stuff like that. Like those are the things that are going to help you as an engineer, I believe. And that's because you are fundamentally alone, but it doesn't stop you from working in a project. I just feel like in the, you know, like this kind of scenario where this is a collaborative tool, there of course is a place for that. But like, are you willing to give up everything else because of that? And that's personally, I'm not.

**Dave Jones:** No, the market for this is so small. They don't, they don't realize how small the market is for this.

**Chris Gammell:** And that's what startups are for, right? I mean, figuring out how big the market is. Hopefully they, you know, if they take a big shot, they might be, I mean, like they might find some untapped market there that we don't know about. Sure. Okay. Fine. I agree with your assessment.

**Dave Jones:** Yeah.

**Chris Gammell:** That is a small market and it's a fragmented market and it's a really tough market. Like we've, you know, how many episodes have we done talking about different CAD tools? And it's just like-

**Dave Jones:** It's crazy.

**Chris Gammell:** Nobody's changed their mind yet. No, I'll say this.

**Dave Jones:** The most productive engineers are the ones that work alone, are the ones that have the mentality, just leave me the F alone. Go away. I'm going to do this. Right? Interesting. Right? I know. I guarantee the most productive ones are the type that have to be left alone. You can't butt in on them.

**Chris Gammell:** Ah, okay. So you mean like unbroken work? Yeah. Yeah. I get what you mean. No, it's not just that. I think people extend that to- It's just that they don't like working with others as well. Yeah. But at some point your stuff is going to be out in the world somewhere or working internal, you know what I mean? Like-

**Dave Jones:** Yeah. But you don't want, you know, sure. You have to go to your design review meeting, right? That's part of the pain of, you know, engineering. I think that's what- And you get your feedback. But once you get your feedback, it's like, leave me the hell alone. I'll do it. Right. Right.

**Chris Gammell:** I think that's where people get tripped up is like the, they think that there's no people involved at all. And it's like, I am an island. It's like, no, no, no, no. There are people involved. Yes, there are. But there's like these, there's like these chunks of feedback. They're like these, it's like a long, you know, whereas maybe software can do like immediate feedback and like have someone sit there coding with you and all the other stuff. Yeah. I just, I, yeah. If Dave was over my shoulder telling me where to route a wire, I would just punch him in the nose, you know, like, and, and, and vice versa. Right. I mean, like, it's not like me versus Dave or anyone else. Right.

**Dave Jones:** I will tell you where, where, where the collaborative design work is done. It's done at the product level. Okay. It's done at how the user interface works, how, what, what, what knobs are the shape of the case, the, the, the physical design of it, how it all works, how it's powered, the battery powered. Okay.

**Chris Gammell:** And firmware interacts with, with the, the pins and stuff. Yeah. And everything.

**Dave Jones:** Right. But once you've done that, you give it to the hardware designer to then design that based on that spec. And then you leave them the hell alone. Give them that here, here, it all is make it work. And then you're, you're, you're not going down. There's not a team of 12 engineers, you know, getting into the design tool going on. Oh no, we, we need an extra bypass capacitor in there and we need to know, let's, let's use this different pin on the micro and stuff like that. It's no.

**Chris Gammell:** And if you do, you can, you can do that at a design review meeting as well.

**Dave Jones:** You can do it at a design review meeting to pick stuff up. Yeah. It's, it's, it's not done at the tool level. It's just, it's, it's just no, no, no, no, no.

**Chris Gammell:** I do wonder if this is a mapping of like, so, you know, there's a lot more people with software backgrounds. I looked at the background of some of the people that are developing this. They're very software focused and like, and there is like this, you know, this modular idea. It's like, I get it, but it does like, not, I think as much as I love a lot of things that that from the software world that have come into the hardware world, I am in the grumpy old man, you know, camp on this one that like, I think the, the smallest atomic unit in terms of workflow is a PCB, maybe a sub circuit, you know, if you've got a really, really complex design.

**Dave Jones:** Right.

**Chris Gammell:** Maybe it's totally different at like a, you know, at an Apple where they, you know, they've got the most complex PCBs ever, but they're not using this tool either. So, so yeah. Yeah.

**Dave Jones:** All right. Can we get off that and get back onto another tool? KeyCAD. Warning, warning, warning, Will Robinson, warning. Avoid all links.

**Chris Gammell:** Dave's pronouncing it wrong.

**Dave Jones:** What?

**Chris Gammell:** What? Yeah.

**Dave Jones:** What am I pronouncing wrong? The warning Will Robinson thing.

**Chris Gammell:** No. KeyCAD.

**Dave Jones:** Oh, did I say KeyCAD?

**Chris Gammell:** No. Nevermind. Nevermind. Keep going. Sorry. Keep going. I was making a joke that is pronounced KeyCAD and you say KeyCAD and I'm making a joke about you still calling it KeyCAD.

**Dave Jones:** Oh, right. So I was warning people. I thought I was legitimately wrong. So great when you have to explain the joke. Yeah, it's great. KeyCAD. Anyway, there's a, there's a, I don't know if it's a spat. What is it? But somebody has bought the original KeyCAD dash PCB. So KeyCAD, K-I-C-A-D dash PCB.org. Apparently that's the original domain name. I don't know the history of it, but apparently now the, the developers are saying, no, this is not the legit site. I, is it virus infected? Should I, should I actually go there and check out what's on it?

**Chris Gammell:** It's very boring. It looks like a GoDaddy parked domain last I looked at it.

**Dave Jones:** Oh, okay. Right. But somebody's bought it and now they're just wanting it. No, somebody sold it.

**Chris Gammell:** Somebody sold it. Oh, okay.

**Dave Jones:** So a former member of the project.

**Chris Gammell:** I don't know, a former member. It is a, someone who was very involved in the project in the old days who registered the original link. Who owned it effectively. He owned it. If they bought it. There was no foundation. There was no, you know, like, so it was very ad hoc. And you know, that individual also, you know, like I, I gave him a little bit of benefit of the doubt. He kept things going. You know, he was one of, one of many people that kept things going throughout the years. You know, KeyCAD is a, I think the nineties, I think it started in the nineties. It's old. Yeah. It's old. Yeah. And yeah. So, you know, I'll give him props for that. And I think that's where I, I will stop enjoying his, his involvement in the project. But basically he sold the domain. He then had the gall to say that he was selling the.com as well, which he also owns the KeyCAD-PCB.com. Okay. I was not happy about that. I did find out today on the list that he was not asked. This is all just open source drama, to be honest. But the main thing is KeyCAD.org is the official new home of it. So, you know, we just all had to go update links and that's tough when you don't have a redirect because you don't own the old domain. Oh, okay.

**Dave Jones:** So this, this, this, this, oh, this domain that got sold used to be the domain, was it?

**Chris Gammell:** That's right. That's right. Yeah. So, okay. So that's where I've downloaded it before.

**Dave Jones:** I can't remember where I last downloaded it from.

**Chris Gammell:** Yeah. Yeah. So about a year ago, DigiKey very graciously, graciously rather, they bought the KeyCAD.org domain name from a true domain squatter who was hosting malicious software. I remember that. Yeah. Right. Yeah. So that was about a year ago. And so they've been in the process and they donated it to the project. Really sweet. Awesome. Awesome move. Then, so they've been in the process of moving stuff over, but it's just, you know, it's tough. There's links everywhere on the internet. So the internet, Dave, I don't know if you know this. There's a lot of links. It's kind of like a series of tubes with links.

**Chris Gammell:** Right.

**Speaker ?:** A series of tubes.

**Chris Gammell:** That's a political joke for those who don't. That's right. Yeah. Yeah. Those who don't. It's a US political joke.

**Chris Gammell:** Yeah. So it's just chasing down those old links. And, you know, there's just, there's just like, even within the program itself, it's still linked to the old, you know, so if you have, if you open your version of KeyCAD right now on your computer, it probably links, excuse me, to the KeyCAD-PCB. Ah, right. Okay. So.

**Dave Jones:** And now there's just like, it's gone. There isn't anything there. Exactly.

**Chris Gammell:** Right. Okay. And so the concern is that because the, you know, KeyCAD.org owner previously prior to DigiKey buying it was hosting malicious software, that that could happen again.

**Dave Jones:** Oh, okay. That's the fear is that it's been, so they don't know who it's been sold to and they have a fear that it might be.

**Dave Jones:** I don't know. Right. Just, yeah. Okay. So. Interesting. Wow. Drama, drama, drama.

**Chris Gammell:** Little bit of drama, a lot more logistical headaches. Yeah. But if anyone is listening and you've got a link on your site to the old place to download KeyCAD, I still have to update a bunch of my links. But if you have any old links, please go and update to KeyCAD.org. It looks way cleaner anyways. Like that's great. Come on.

**Dave Jones:** One thing I didn't know is that all of the trademarks to KeyCAD have been given to the Linux Foundation.

**Chris Gammell:** Yeah. They're more involved with the Linux Foundation now.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Is that because they're a neutral arbiter or is that?

**Chris Gammell:** I think so. Yeah. I'm not sure how that stuff works. You know, I talked to Wayne and Seth and some of the guys about it. It just seems like a lot of work to do all the open source, you know, like who owns trademarks and just like even setting up, you know, 501c3s and stuff like that. So Linux Foundation helps with a lot of that stuff.

**Dave Jones:** Ah, okay. Yeah.

**Chris Gammell:** Yeah. I mean, it's great. It's a great service and I'm real grateful it's out there.

**Dave Jones:** Right.

**Chris Gammell:** So hopefully all this stuff's cleaned up by version six and hopefully that's on the way. We'll see. There you go.

**Dave Jones:** Wow. The trauma.

**Chris Gammell:** Man, I have that on my computer. So one of my students is using it, you know, and that's fine. We use it fine. But boy, all the shortcuts changed. It's like, they're like normal now. So you want to like copy a command. You want to like the copy command is actually like control C. And I'm like, this is the way to do it. But man, it's tough to switch my brain around. Right. Okay. Remapping my brain.

**Dave Jones:** What was copy in KeyCamp?

**Chris Gammell:** It was a mouse over and hit C. Oh, geez. It was very, yeah. It was very janky.

**Dave Jones:** Yep. Yep. So it's standardized on the old WordPress. Sorry. WordStar. WordStar. I believe it was WordStar. Please correct me if I'm wrong.

**Chris Gammell:** I feel like it's a, that's just kind of like a Windows standard of this. I mean like a, not even a Windows standard.

**Speaker ?:** No, it was.

**Dave Jones:** But no, no, this is pre-Windows, dude. This is pre-Windows.

**Chris Gammell:** You're saying WordStar before OS has started doing it?

**Dave Jones:** Yes. Control-C and Control-V originally. My vintage computer history brain is telling me that it came from WordStar.

**Chris Gammell:** And what was WordStar?

**Dave Jones:** WordStar was a processor. It was the word processor, dude. Okay. It was bundled with the Osborne 1, for goodness sake. You know, it was worth like thousands of dollars.

**Chris Gammell:** You're just saying words to me at this point. Right.

**Dave Jones:** Okay. Does CPM mean anything to you? All right.

**Chris Gammell:** Yeah. Clicks per melee, or that's how we get paid online advertising revenue. CPM?

**Dave Jones:** Control-C. Here we go. No, it comes from Xerox PARC, for goodness sake. Control-C is common computer command. Hang on. Hang on. In graphically in command history. Where's the history? Where's the history? Larry Tesla created the concept of copy, paste, and undo from computer human while working at Xerox PARC. Right? Oh, yeah.

**Chris Gammell:** They had that HCI lab. That's right. The human-computer interaction lab. And that's also where they did the mouse and the pointer and just lots of things.

**Dave Jones:** Well, there's the Macintosh had the Apple key and X and C. Apple key for C and stuff like that. But I'm telling you, WordStar had, WordStar predates that, I'm sure.

**Chris Gammell:** Okay, Dave. Well, I guess you should go write a wiki page.

**Dave Jones:** I mean, it first came out in 1978, WordStar. I actually used to use WordStar. And yeah. Way back.

**Chris Gammell:** So you used a word processor, is that right?

**Dave Jones:** A word processor, yes.

**Chris Gammell:** Man, I do not miss the old days. Yes. Yes.

**Dave Jones:** And then WordPerfect. Yes, I remember. Yes, WordPerfect came along and just swooped up all of WordStar's market share. And then I switched to WordPerfect. And then I switched to MS Word.

**Chris Gammell:** Yeah, yeah. I've heard of that.

**Dave Jones:** Microsoft Word. For DOS. For DOS. None of this Windows rubbish.

**Chris Gammell:** Actually, that's right where Chris started in. Oh, okay. Right. There you go. I remember moving a cursor on a command line screen. Or on a terminal screen, basically. Yeah, it was not pleasant. It was not pleasant at all.

**Dave Jones:** Anyway. Yeah. I got a feeling it came from Control-C. It came from WordStar. Come on. Comments down below.

**Chris Gammell:** Okay. I'm going to find out now. Everyone just links to the same article you read on the air.

**Dave Jones:** Oh, boy. Anyway.

**Chris Gammell:** Oh, boy.

**Dave Jones:** All right. There we go. Drama. Is there any other drama this week? Because this week's all just drama and buyouts and crap like that.

**Chris Gammell:** Any non-drama you said?

**Dave Jones:** Yeah. Oh, no. Is there any more we need to get out of the way?

**Chris Gammell:** Considering that the whole episode is like... I've gotten that. I'm clear. Yeah. I'm clear out of my system.

**Dave Jones:** Okay.

**Chris Gammell:** All right. Mm-hmm. Yep.

**Dave Jones:** Oh, come on. We have to mention Circuit Hub launches a flat rate rapid prototyping service. It's a flat rate. Okay. Right. Okay. That's kind of novel, I guess, considering that we've been talking about assembly for half the bloody show.

**Chris Gammell:** So, yep. It's not cheap. It's about $1,500. Oh, okay.

**Dave Jones:** Five boards, $1,200 plus parts, ships in three days. Oh, $1,200.

**Chris Gammell:** So, okay.

**Dave Jones:** Yep. Yeah.

**Chris Gammell:** I mean, I'm sure it's worth it if you're fit in there. Oh, sure.

**Dave Jones:** If you've got startup money, if you've got all that sweet startup cash. Oh, come on. Yeah. Just burn it. Burn, baby. Burn. That's right. Burn that cash. Oh, boy. You have no idea how much we used to spend on prototype PCBs.

**Chris Gammell:** Oh, I can't even imagine. Yeah.

**Dave Jones:** 24-hour turn, eight-layer jobbies.

**Chris Gammell:** Oh, boy. How much?

**Dave Jones:** Eight and 10-layer. Oh, that was several thousand dollars for one board.

**Chris Gammell:** Oh, yeah. Okay.

**Dave Jones:** Yeah. Like $2,000 for one board. Yep. And then it wasn't the right color. Wasn't the right color black. So, you know. No. We had to get it respun. Yeah. Yeah.

**Chris Gammell:** Yeah. I mean, startup money is cheap these days. I just sent you a link for, you know. I found this link. For free money.

**Dave Jones:** You sent me a link to free money. For free money, basically. Yeah. Right.

**Speaker ?:** Okay.

**Chris Gammell:** Dance church raises $4.7 million. So, you know, like when you're seeing like dance things raising $5 million at a time, it's like, okay, there's a lot of money out there for startups.

**Dave Jones:** Dude, it's a church. That's practically a money cash cow and it's tax free.

**Chris Gammell:** Well, there you go. It's a dance church, though. You know. Dance is my religion.

**Dave Jones:** Don't tell me about churches, dude. I'm currently right next to the mothership.

**Chris Gammell:** Hmm. Yep. Got it. Yeah.

**Dave Jones:** All right. Yep. No, come on. We have to burn up another 10 minutes, don't we? So we just got to drag this sucker out.

**Chris Gammell:** Well, we can drag it out. I'm looking around my bench at what I've been working on. Let's see. We talked, I guess we talked about that last week, the solenoid that got stuck. I cut through and got my solenoid unstuck. I think we talked about that two weeks ago.

**Dave Jones:** Oh, yes. You had to break in to your, yeah. There's quite a few people who pointed out the irony of us talking about on last week's Ampower that Facebook locked themselves out. Oh, yeah. And then you proceeded a couple of days later to lock yourself out of your own security system. Yep. Barely a security system. A golf clap. A locker. Christopher J. Gamble. That's right.

**Chris Gammell:** That's right. Yes. Let's see. What else is on the old benchy bench? Well, so I was surprised. Actually, I bought what I thought was conformal coating, and I thought I was buying silicone conformal coating. I actually bought acrylic conformal coating.

**Dave Jones:** Yep.

**Chris Gammell:** I don't know what the difference is, though. I mean, they're both conformal coatings, but one is just thicker. It kind of felt like it was just clear spray paint at that point.

**Dave Jones:** Well, let me talk about it from my extensive chemical engineering background. Not. I guess not. I don't know. Silicon is nice and soft and fluffy. I figured you've done acrylic versus silicone before. Yeah, I have, but I don't... It's been so long ago. I don't recall details. And then we had mechanical engineers who sort of took care of the aspects of that sort of stuff more.

**Chris Gammell:** No, this is literally a can of spray paint at this point. I mean, like, yeah. Yeah. Buy it off the shelf. Okay. Well, that's a flop. How about I got the Micromod? We talked about Micromod a little bit on the show, I think.

**Dave Jones:** Hang on. No, I can go back. Hang on. I can go back to that.

**Chris Gammell:** Okay.

**Dave Jones:** Acrylic's hard. Silicon is soft. Yeah. Generally, I've used the silicon re-enterable potting compounds, right? I don't think I've ever used silicon conformal coat, like a rubber coat.

**Chris Gammell:** It's not like a rubber. It's like a real thin layer of silicon. Basically, it's like a silicone spray, almost like a...

**Dave Jones:** Yeah, but does it harden or does it...

**Chris Gammell:** It does harden, yeah.

**Dave Jones:** Right. Oh, okay. Right. So it hardened. So it's not... Oh, okay.

**Chris Gammell:** Well, it might have some springiness to it, but it...

**Dave Jones:** I didn't know you could get silicon spray that hardened.

**Chris Gammell:** Let me see if I can find the link. It was just an NG Chemicals, like...

**Dave Jones:** Right.

**Chris Gammell:** Yeah, waterproofing conformal coat spray.

**Dave Jones:** Okay, no, I'm so used to them being re-enterable potting compounds. That's the only way I can think of them.

**Chris Gammell:** That is the... That's like the black goop that you have into a container. Not the black goop.

**Dave Jones:** No, it's actually clear. You can get clear goop. So you can actually see the board.

**Chris Gammell:** Oh, it's like an RTV, almost? Yeah, yeah. Like a... Yeah.

**Dave Jones:** But no, but the good thing is, is that, well, I'm not going to say all of them, but the ones I've used are re-enterable potting compounds. So what that means is that you can stick a probe through or you can stick a screwdriver through to trim a pot. Self-healing. And then once you pull it back out, yes, it's self-healing. It actually, you know, it becomes waterproof again, right?

**Chris Gammell:** Cool, cool. Yeah.

**Dave Jones:** So, yeah, it actually re-sales as you pull your screwdriver or your probe back out. It's great.

**Chris Gammell:** It's good stuff. That's... I've never seen that. That's...

**Dave Jones:** Yeah, it's very cool.

**Chris Gammell:** That was your underwater days? Those are...

**Dave Jones:** Yes. Yeah.

**Chris Gammell:** Yeah. That sounds right. Yeah.

**Dave Jones:** So, yep. Very cool stuff.

**Chris Gammell:** Lots of waterproofing methods. Yeah. Yeah.

**Dave Jones:** Yeah. Yeah. Because, you know, I've designed stuff that had like, you know, five or six trim pots, all that all interact. That all interact. If you want a bad day, design a complicated temperature compensation circuit that has five trim pots that interact. And, yeah, I...

**Chris Gammell:** Like, you mean you turn one to the right and that makes you have to go and turn the next one to the left.

**Dave Jones:** And you've got to do like a successive approximation type thing to get to where you want.

**Chris Gammell:** Would you do that these days with a trim pot still? Or would you do it with like a digital?

**Dave Jones:** No. Everything's bloody digital these days. Yeah. Yeah. Yeah. Yep. But back then, you know, that was the easiest solution. You know, that was the best solution that we come up with. Yep. Even though we had to manufacture them in volume as well, you know, you still had to, yeah. Had these jigs with 10 boards all lined up and you'd have to, you know, trim them all and, you know. But you sort of got, you know, it's actually not as bad as it sounds. Once you get used to a technique of doing it, there's a, you know, like you can do, yeah, yeah. You adjust this one first, then, then this one, you jump over here, then you jump back here and you figure out like the best interactive way to do it. The most efficient way to do it. And then once you figure that out, it goes into the documentation and, and the production operator just follows that. And, you know, it's, it's okay.

**Chris Gammell:** Yeah. I don't, I don't miss those days either. No. Yeah. I mean, like just thinking about like, I'm thinking about the calibration stands that I saw in my days at Keithley and ABB and stuff like that. And like, yeah, there were very occasionally potentially on there, like on the older stuff, but you know, most of the stuff was like a DAC or something like that. If you're not adjusted like that. But yeah. Cause then like, what happens about like a, like a vibrational type, like just jiggling.

**Dave Jones:** Oh, they're usually pretty good. These are like, you know, I think that was, yeah. Expensive pots. Yeah. Oldy term. Yeah. They're expensive pots and no vibration wasn't really a problem on those. So yep. It's all good. Okay. I have sent you dude, a chip of the week.

**Chris Gammell:** No way.

**Dave Jones:** We haven't had chip of the week. When was the last time we had chip of the week?

**Chris Gammell:** I don't know. What do we got? Okay. This does, this does not look new. Pre-trimmed.

**Dave Jones:** This is not, no, well, no, no, it's not. Well, no, I think it's 2018. Is it 20? No, 2015. 2015. 2015. It's from that.

**Chris Gammell:** So this is a, that.

**Dave Jones:** That corporation. This or that. Great, great name. That corporation. Ah, we can't think of a name. Just call it that corporation.

**Chris Gammell:** That's great. What is this? Analog engine dynamic processor, I see.

**Dave Jones:** I thought you, I thought this would be right up your alley, dude. I thought, come on, you're a technically, you were in a band, right? I thought you were a muso. I thought you'd know about compressors and limiters and DSs and all that sort of jazz.

**Chris Gammell:** Yeah, I was not in a good band.

**Speaker ?:** Right. Okay.

**Chris Gammell:** Obviously. Obviously.

**Dave Jones:** Well, anyway, it's a chip. It's a specific audio and it's an analog audio engine. It's a dynamic process. It's an audio dynamic processor. And it basically contains a voltage controlled amplifier, op amps and RMS converter. And basically, yeah, there's four op amps in here and there's RMS converters, voltage controlled amplifiers. And what you can do with this is that you can use them in different ways to do all sorts of analogy audio goodness. You can do a compressor, a limiter, automatic gain control, a DSs circuit, all sorts of stuff.

**Speaker ?:** Yeah.

**Chris Gammell:** So wireless microphones, wireless instrument packs in your monitors. Okay. So basically it's just going to make stuff sound better. It's going to make stuff sound different, better. Yeah.

**Dave Jones:** Why you ask, why you ask, why you ask is digital Dave looking at a analog.

**Chris Gammell:** Yeah. That is a great question.

**Dave Jones:** Yeah.

**Chris Gammell:** Are you making a headphone amp? Is this a new project?

**Dave Jones:** Not, not a headphone amp. I'm thinking about making a microphone, a USB microphone preamp. Cause I, for the life of me, I cannot find one that does what I want.

**Chris Gammell:** I sent you a tweet about this the other day. The F6. Yes, I know.

**Dave Jones:** But it's, no, that's not the solution. No. Sorry.

**Chris Gammell:** 32 bit float, man. 32 bit float.

**Dave Jones:** No, no, no, no, no, no.

**Chris Gammell:** All right. All right. So what do you want? What are you looking for here?

**Dave Jones:** That is not the solution. That is, that is not the peaking thing, right? No. What I'm talking about is that I've been experimenting with different mics. We did this just before the show actually. And I was using a shotgun mic and that didn't have enough bass in it and stuff like that because, you know.

**Chris Gammell:** He's all about that bass. You know. About that bass.

**Dave Jones:** Yeah, because I've got a, like a, you know, if I go back from the microphone like this and talk louder, we're going to lose all the bass. We lose the proximity effect in the mic, right?

**Chris Gammell:** Yeah, but that's true regardless of the microphone.

**Dave Jones:** Yeah, no, no, no.

**Chris Gammell:** You shouldn't be fixing microphones with chips. Yes.

**Dave Jones:** But using this mic, right? I'm using my one inch Rode NT1A, right? The world's quietest mic. It's, you know, it's pretty schmick, right? But if I move my head away from it, you can notice and hear the variations in my voice. Right? And it's annoying. So I think maybe I could help with maybe use a compressor, for example. And then, of course, a limiter for peaks and, you know, stuff like that. If I actually get dynamic like this and accidentally move forward and shout into the mic, you know, and I didn't realize I did it.

**Chris Gammell:** Dave is an excitable creature. I don't know, man. I don't know.

**Dave Jones:** And then, yeah, so I thought I'd do that. But there's nothing. There's nothing. Please, please leave it in the comments down below. I don't want to piss away my time doing it if there's something on the market that does it. But all I want, I'm a simple guy, right? I'm a simple video blogger. All I want is a phantom voltage mic amp, right? USB interface, of course. That has, right? So it's got the 48-volt thing, a headphone jack that turns off the speakers when you plug the bloody headphones in, as my current one does not do, pain in the ass. Right, right.

**Chris Gammell:** Yep.

**Dave Jones:** And I want something that also has a compressor and a limiter function. And I don't need multi-channel bullshit. I'm not plugging in my freaking guitar and my instruments and everything. I've just got a microphone. And I'd love some knobs on the front to be able to make myself sound a bit better because I've got a shitty voice and I'd love to be able to just dick around with some knobs on the front of a bloody preamp until I sound what I think is the best. That'd be great. And it would cut down, you know, peaks because it's got a limiter in there. I know I can do all this with separate stuff. I know. Yeah, I was going to say, are you looking at rack mount inputs and stuff like that? Yeah, no, no. I just want a little box that sits on my desk. One box. One box that's got it all. You can put the rack mount thing. I know I can do all the rack mount shit. Yeah, I know.

**Chris Gammell:** Underneath your monitor. I know. I know. I know.

**Dave Jones:** But typically, yes, you'll get an audio processor, right? One new rack thing. But then you still need the separate preamp. You need everything out like that. No.

**Chris Gammell:** No, no, no. I used to have something like that. Remember I used to, oh God, a long time ago. Back in the basement days. Yeah, there probably is. I had an eight channel. I had bought it for like my drums.

**Dave Jones:** Yeah, I don't want a bloody eight channel. I want one channel.

**Chris Gammell:** I know you don't want eight. I'm just saying that what this had though, it had a, it had mic preamps for every mic. It had phantom power. Yep. It had eight channels, but that doesn't matter. And it had a USB interface. Yep. And then you could add effects internally, digitally.

**Dave Jones:** Yes. I know such a thing exists, but I don't want a big rack thing. I just want a little thing that just sits on my desk.

**Chris Gammell:** I'm sure this exists. Yeah. I'm sure you've looked. Well, I can't find it. I'm not going to go spend my time. I can't find it.

**Dave Jones:** It might be out there. But anyway, I thought, so I'm, you know, if it's not out there.

**Chris Gammell:** I think it's an interesting project regardless. Yeah. Yeah, exactly. That's going to be a lot of work, man. That's a. Yeah. Ooh.

**Dave Jones:** Yep.

**Chris Gammell:** So this would be out of the mic. Is that right? So you would take an, you take a balance signal out of a microphone. Yes. That's right. Put it into this chip. And then that would then act as your preamp.

**Dave Jones:** Well, no, you've got to have a preamp circuit first. This thing isn't a preamp. Right. So this thing's got to, you know, this is just an audio processor. Yeah. Yeah. So you've got to. Yes. Yeah. You've got to have the high impedance preamp input, you know, low noise, jobby, the whole works, right? The whole shit. Okay. And then this goes, then this would be the audio processing part. And then you'd have a, you know, a Cirrus logic USB, you know, standard audio interface chip and stuff like that just works with standards.

**Chris Gammell:** So you're saying you don't want to do, you don't want to buy three different solutions, but you'd rather buy two and make one. No, I don't know. I don't want to buy three boxes.

**Dave Jones:** I know I can get it as one big rack mount box. I know that exists.

**Chris Gammell:** And, you know, maybe I might just like, you know, they make a rack mount things you can put on the back of your desk, like vertically.

**Dave Jones:** Yeah. Vertically and stuff. Yeah. You can get a pretty cool vertical rack. Yeah.

**Chris Gammell:** Maybe you can be mounted on a wall, you know?

**Dave Jones:** Yeah. Yeah. Well, I do have a wall right behind me. So maybe, you know, anyway, this is a cool part.

**Chris Gammell:** This is a cool part.

**Dave Jones:** Yep.

**Speaker ?:** Hmm.

**Chris Gammell:** So what would you need to power this with? So what is it? This is a single supply.

**Dave Jones:** They also do a dual supply jobbies.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Five. Less than five volts per root hertz noise for those playing log at home. Yeah.

**Chris Gammell:** I would love to see, like, even if you don't end up building anything with this, just like getting this and like doing a, like a test on the bench for this sort of thing. Right. Yeah. Yeah. Just to see like what different input. So, you know, if you do like a pulse input, what does that look like in terms of the output? Right. With like log bass beast dynamic processing. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. It's cool.

**Chris Gammell:** Yeah. That's great.

**Dave Jones:** Yep. So you can do all sorts of, so you can configure it in many different ways. Anyway, I think these little dynamic processor ICs are really cool. You can get like really old school, like single in line chip jobbies and you can get, you know, little SO8 package jobbies and stuff like that. But yeah, this one's, this one does come in dip, I believe. Cool. It comes in dip and this newfangled SO stuff. Yeah. Oh, no, sorry. No, no. This particular one doesn't come in dip. QFN and QSOP. The previous version of this, which I think is now obsolete, came in a dip package. Yeah. Yep.

**Chris Gammell:** Cool.

**Dave Jones:** 28 pins. I like it. Yep.

**Chris Gammell:** I like it. Chip of the week. Chip of the week. Chip of the week. Bring it on.

**Dave Jones:** Awesome. There you go. It was, it was first done in 2009 at, at least it goes back to then Rev 5. They're now up to Rev 8 Silicon. They keep on, they keep on refining. Yep. Is that it? Okay. Our amp hour's up.

**Chris Gammell:** Our amp hour is up. Thanks for finding this chip. That was a fun one.

**Dave Jones:** All right.

**Chris Gammell:** Catch you next time. Bye.

**Speaker ?:** Bye.
