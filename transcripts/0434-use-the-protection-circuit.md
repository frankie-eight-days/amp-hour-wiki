---
episode: 434
title: Use The Protection Circuit
url: https://theamphour.com/434-use-the-protection-circuit/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released March 17th, 2019. Episode 434. Use the Protection Circuit.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** I need a new intro after, what, nine years or something? Give it a shot.

**Chris Gammell:** What do you want?

**Dave Jones:** I don't know. Should I invent a title for myself?

**Chris Gammell:** Yeah.

**Dave Jones:** Czar of podcasts?

**Chris Gammell:** There you go. Coming to you live. Live and as hot as solder, the Amp Hour.

**Dave Jones:** Wolfman Jack.

**Chris Gammell:** What did I hear you say? Or no, I saw you write something the other day on Twitter. I thought it was like very Aussie of you. I forget what it was, though. I don't know. It was something that like Aussie Man says sometimes. That's why I was like, oh, I've seen that phrase before. Right. Really? I don't remember what it was, though.

**Dave Jones:** Who's Aussie Man?

**Chris Gammell:** You know Aussie Man. He does like ridiculous review videos, isn't he?

**Dave Jones:** Oh, yeah, right. Yeah, of course.

**Chris Gammell:** Yep. Oh, it was John Saunders who told us about him.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Aussie Man reviews, you know. Yeah, exactly. It's pretty funny.

**Chris Gammell:** It's pure personality. Oh, yeah, totally. It's like you if you didn't know how to do any electronic stuff. Right.

**Dave Jones:** I don't know. I can't put stuff on like that, you know. It's like.

**Chris Gammell:** That's true. I mean, yeah, he just basically like he just adds a flair to just other stuff. Yeah. Yeah.

**Dave Jones:** Although, yeah, I've watched him do like just off the cuff stuff instead of, you know, like live off the cuff stuff instead of scripted stuff. And you can tell it's not far from his, you know, personality. Oh, that's who he is. Yeah. As most Australians are. He's pretty close to there. You know. People say that all. Probably one of the most common things after people meet me, they go, he's exactly like I expected.

**Chris Gammell:** Yeah. Yeah. You know. I agree with that. I agree with that. Right.

**Dave Jones:** Yeah. Okay. Yeah.

**Chris Gammell:** Yeah. Yep. Not a lot of secrets here. So, you know. Exactly.

**Dave Jones:** It's pretty hard to hide a persona after, you know. I think I've had that much time in front of a camera. Yeah. Yeah. Exactly.

**Chris Gammell:** Yeah. Also hard to hide from electronics. How's electronics these days?

**Dave Jones:** It's a pain in the asses ever, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. It is.

**Chris Gammell:** It is like that from day to day. Sometimes I'm like, you know, some days I'm like, I cannot believe I get to do this. Like I get, you know, that like I'm sitting here making things with, you know, silicon and metal and craziness. Right. And other days I'm like, holy crap, what am I thinking? Like.

**Dave Jones:** Like just the other day, like we're still getting a new PCB for the micro supply. Right. And oh yeah, no worries. It's a four layer board. Right. We'll just upload it to JLC PCB. Cause that's who we use at the moment. Right. But they're cheap and they're pretty quick and you know, yeah, yeah, it's 10 million off them out there. Anyway. So we upload the damn thing and like David generated the files out of Altium and, and I upload it and go, this doesn't quite look right. At first of all, it, it detected only two layers and then I'm going, well, it's a full layer board. And then I'm going through and I'm, and it took me a while to work out on David had his out job wrong in Altium and I'm not sure if you're aware, but there's these out job. Well, there's a, yeah, it's a way to automate the production process of your board. So you can like do the same system every time. So you can like script this out job it's called. And then it, it selects all the correct Gerber layers and files and formats and everything and bill of materials. It's like a package kind of thing. It's a package thing and you can have like a company standard out job so that it doesn't matter which project you do. If you use that out job, it generates exactly the same format files every time. Unless it's wrong. Unless it's wrong. In this case, it was wrong. And he screwed up his out job and it took us a while to figure out that he screwed up his out job. So he was only outputting, exporting two layers. So once we fix that, okay, no worries, upload again. And still it's not, it detected four layers this time, but it wouldn't display the inner layers. Like, you know, when you upload the files, it's got like a preview and on-screen preview thing. Yeah, right, right. Fantastic. A lot of the, a lot of the PCB manufacturers have this now. And it was only showing the top and bottom copper layers. And I'm going, hmm, what's going on? And it turns out that JLC PCB doesn't like the inverse inner copper layers that Altium produces. Because like, if you do it as a plane, right? If you do it as a plane in Altium, then it produces an inverse image.

**Chris Gammell:** So it's like drives nothing at that point?

**Dave Jones:** As opposed to a signal layer. Yeah. So it's like, it's blank or whatever, or it just, or it didn't detect it or whatever. It just didn't like it. So anyway.

**Chris Gammell:** I mean, so much of that stuff is just like the old, the old Gerber formats and like, you know, basically piling on different, different standards and ad hoc standards on top of it. It's yeah. Yeah. I do, I do feel for all the manufacturers out there that have to like deal with all it. Because there's, there, there are a few. It's a pain.

**Dave Jones:** So if people don't know what we're talking about, when you produce a Gerber for a regular signal layer, top or bottom or an internal signal layer, it, you know, it actually has a trace where the copper is supposed to be. Sure.

**Chris Gammell:** Right.

**Dave Jones:** But on a plane. A line looks like a line, right? Yeah. A line looks like a, a trace looks like a line on the Gerber file. Right. And so, so that's a positive, that's what's called a positive image of positive photo mask image. And, but planes are produced as a negative photo mask. So it appears inverse. So anywhere you want copper is actually blank. There's no line there. So it's, you know, yeah, it's, um, it's a positive, negative photo imageable thing, which you make PCBs with. So. Yeah.

**Chris Gammell:** Is that, is that a legacy thing too, because of exposures and stuff like that?

**Dave Jones:** It's a legacy thing because most, almost, or I don't know what they do these days. Um, but, uh, historically most of the PCB manufacturers done in the negative image. So if you, back when I was laying out tapes, boards by hand, right? With the, with the, uh, with the tapes and the pads that you stick down, right? So you get a roll of tape and you roll it out and you, so none of this CAD bullshit, right? So, so you're laying everything out and then you didn't have a positive photo resist PCBs. You had negative photo resist PCBs. They're really the only ones you could get at the time. And so you had to first create a negative, uh, image on like some Mylar or whatever. So you have like a, the, so you had to convert your positive image to a negative one. So it was a two-step process. And then you use the negative photo mask to expose your negative photo resist board. And well, it's, you know, yeah. Multi-step process. But nowadays, you know, new manual things. You can buy it.

**Chris Gammell:** You want to use less tape though too? Is that, is that one of the reasons that it was negative?

**Dave Jones:** No, no.

**Chris Gammell:** No. Okay.

**Dave Jones:** No, it's, I believe it. It's, it's because of the, uh, actual, it's something to do with the chemistry. Like it was just better. It worked in the negative image. I don't know. I do. I, if anyone knows specific details. No, no, no.

**Chris Gammell:** Some of that is etching stuff. So it's like, do you think about etching rates? So it's like, if you've got like, um, if you're trying to etch away more stuff, I think it's problematic because then you have more that gets dissolved into the, into the etchant. Right. So then you have to switch it out more often.

**Dave Jones:** That doesn't have, that's got nothing to do with it really. That, that, and that doesn't matter whether you're positive or negative doing that. It's, it's the, uh, what it, it's how the chemistry of the photo mask of the solder mask actually works. So, uh, not solder mask, the photo of the, um, etchant. The lithography mask basically. The lithography mask or whatever. Yeah. I can't remember the name. Anyway, there is a name for it. Anyway. Yeah. It's, it's the chemistry of that about when you expose it to ultraviolet light, then whether or not it hardens or softens, whether it's exposed or not. So it's a different chemistry, whether you're going to have a positive photo resist board or a negative photo resist board, but it's got nothing to do with the amount of copper. That's still your PCB layout doesn't change. Um, no, no, no.

**Chris Gammell:** I meant when it actually hits, when it, when it gets into the copper or sorry, when it gets into the, uh, into the bath, that's what I meant. More, more of the copper would be etched away versus less of the copper etched away.

**Dave Jones:** No, but that has to do with your PCB layout. That's not got to do anything to do with whether or not you use a positive or negative photo resist.

**Chris Gammell:** Oh, okay. So this is like the top, because you're just talking about the top layer and then what actually gets, what gets exposed, you're saying?

**Dave Jones:** Yes. I'm talking about how it gets exposed. Yeah. Either it's a negative process or it's a positive process. Either way, your layout is the same. How much copper gets etched away is exactly the same. It's based on how you lay out your PCB. Um, it's just that, yeah, I, if anyone knows the actual history of that, I believe it's because the chemistry started out early, the early chemistry of PCBs. It was just, I don't know, it just worked better in a negative image format, i.e. it, it hardened, sorry, it softened when exposed to UV light or something. No, it hardened when exposed to UV light. So therefore, when you exposed it, the parts that were exposed on the negative image went hard and they wouldn't be removed by the etchant. So that's how it worked. It's a negative process. So if anyone knows, it's like, why, why are solder masks green? Why was solder masks always green? It's because that's how the chemistry came, right? It's only in modern times of, you know, you can get any color under the sun. Well, you still can't, right? You can't just go and order any, you know, 16 bit RGB value solder mask, right? You can't do it. Um, color, you know, you've only got like eight colors to choose from or something.

**Chris Gammell:** Right.

**Dave Jones:** That's a lot. When I was a boy. Right. Geez. I was green or green, sir.

**Chris Gammell:** Right, right. You can choose any color as long as it's green, right? As long as it's green, yep.

**Dave Jones:** And, uh, yes. So, oh, you had a bit more variety in your, uh, silkscreen though. You could either get that in black or white. Take your pick, son. Yep. It's, uh, yeah. So that's, yeah, it's fascinating. So if anyone knows, please let us know. But anyway, what were we talking about? We're talking about bloody Gerbers and, yeah. Yeah, you said you were uploading and having problems with it. Yeah. So we, you know, wasted a couple of hours there. And it's like, because we didn't have that problem when I got my four-layer, uh, my four-layer PCB manufactured through JSE because I used, uh, I used, um.

**Chris Gammell:** Takehead.

**Dave Jones:** KiCad. KiCad. KiCad. What a mental block. I mean, come on, man. I used KiCad and it generates positive, uh, images, right? Even for planes, it generates a positive image. Yeah, that's right. So it just didn't have a problem. It just worked. And, yeah, this is the first time we'd put in a four-layer Altium file through that, that used power planes. If we put a four-layer through that used signal planes, we wouldn't have had a problem. Oh, it's because they're marked internally differently as well? It's because, yeah, it's because of how, Altium works. Altium treats plane layers different to signal layers. And you don't have to use plane layers. If you've got, if you're designing a four-layer board and your inner planes are just big, you know, grounded five volts, right? Right. Just big planes. You don't have to use the plane layers. You can do them as signal layers if you want and then flood fill the thing. Sure. Like, it isn't a problem. It works either way. And it's more than one way to skin a cat when you're laying out using a package like that. Yeah. Yeah.

**Chris Gammell:** So that is the legacy piece you're saying, though, is that when it's marked as a plane, it inverts it.

**Dave Jones:** When it's marked as a plane, it does. It inverts that on the goodness. Yeah. So, yeah. Oh, boy. And then the fab house know that. You know, any decent fab house knows that. And then they just, oh, right. It's inverse. Of course, it's plane. So they just fix it for you and you get your proper board. Right? So it isn't a problem. But yeah, these newfangled automated processes where you upload your file and it instantly previews everything. Yeah. Fantastic. I wouldn't go back. It's great. Like you upload your board and yet, look, this is what, almost in real time, it shows you what your board's going to look like when it's manufactured. Wow.

**Chris Gammell:** I've had a similar issue at one point where it was actually because, you know, even when it does a preview, it was a different manufacturer, but it does a preview. But then it was like, okay. And it wasn't able to delineate between two, four, six, eight, ten layer boards. It just said, yeah, here's your top and bottom regardless. And then like a day later, though, so that was just the time difference thing. It was in China. And a day later, they're like, hey, you didn't upload two of the files. So can we have those? And I'm like, of course. Yeah, you're right. But that's like, that's the mistake. You kind of multiply through that and you almost lose a whole day from that, you know. Oh, yeah.

**Dave Jones:** Totally. You can lose a day or two with time zones. Yeah. And if you don't happen to read your emails for half a day, there's another half a day going. Oh, man. I had it.

**Chris Gammell:** Yeah. I had it. My email for some reason was bouncing certain addresses. Oh, no. Like my work email. Yeah. And so for a while, like they couldn't reach me. And they finally, they figured out, they somehow, they looked me up online. They found another one of my email addresses, thankfully, which is really nice. Oh, really? Wow.

**Dave Jones:** They went the extra mile then.

**Chris Gammell:** Yeah. Wow. That was really great of them.

**Dave Jones:** Right.

**Chris Gammell:** And finally, because I kept like looking at the status too. You know, that's the other problem is that now you have like, you know, it used to be like you send off a board and you're like, okay, it's gonna be two weeks. I'll, you know, check. If I don't hear in four weeks, then I'll be like, okay, what happened? You know? Yeah, right. Yeah. But now it's like, you can like follow the flow tracking process and it's like, hey, I see this is stuck here. It's been there for two days. What's going on? You know, like, and it's.

**Dave Jones:** You can see which part of the 10 step process it's done. I've done a video on that of the multiple. I think there's like 14 steps, 14 process steps to manufacture your board just in like a two layer, just a two layer board. You know, it's nuts. It's just. Yeah. And you can follow it through like they. Yeah. A lot of these good online houses now just have these. Yeah. These automated things. So they must track the boards. They must like add a bar. I assume like they add like a barcode.

**Chris Gammell:** Yeah, they do. To the panel or something. The final package. And they also. Well, they also. The number marking they put on the. You know, the number.

**Dave Jones:** But then you can't automate that because you've got to type it in. So they would have to have a barcode. Otherwise, you don't want people typing in the people on the production line typing in numbers. Oh, sure. So I reckon what they do is they add a barcode on the outside of the panel, which nobody ever gets because they cut out your board and send you your board. Yeah. Yeah. Yeah. So that's very cool. So speaking of which, speaking of China, there's a great article on the China law blog. China law blog dot com about how basically don't go to China. Don't get stuff manufactured in China unless you have like a hundred thousand dollars.

**Chris Gammell:** Yeah, we had mentioned this briefly at the end of two weeks ago. Well, we just mentioned that people should read it. So, yeah. We both read through it now. It's, you know, after reading the article. Yeah. It's, it's, and it's more on the IP side. That's what they're really covering.

**Dave Jones:** But yeah, it's fascinating. But it's also why a lot of the crowdfunding campaigns fail, you know, because they just, they get a lot of money, but it's not enough. Right. You know. Yeah. And it's expensive to manufacture stuff. Yeah. Even in China, you know, it's not cheap. People think, you know, it's peanuts, but nope.

**Chris Gammell:** Yeah. What do you think the lowest, what do you think the lowest you could get like a pro, like what is your budget number for prototyping these days? Like a simple, you know, relatively simple board. What do you expect to spend on it?

**Dave Jones:** The blank board or the assembled board?

**Chris Gammell:** No, like an assembled, like your first, you know, like the first board off a line, even if it's not being made by someone else. Like what do you estimate that to be?

**Dave Jones:** What do you mean? If it's not, if it's made by me.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm obviously not charging my own, you know, I'm not counting my own wages. I assemble the thing. So really it's only the parts cost plus the PCB cost.

**Chris Gammell:** Yeah. But I mean, you do have time that is going into it. I think, I think it's not like, I'm saying you put your hourly rate to it too. That's, that's, that's what I really mean.

**Dave Jones:** It's like, if I, if I put my hourly rate, like I don't have an hourly rate, but if I did, yeah, it's, it's thousands of dollars.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Thousands. It's like trying to get that across to clients. It's, it's, it's hard. It's like, so my job now is to kind of like explain that to someone to be like, look, to get a single resistor onto a board, it's going to cost a couple thousand dollars. Just, you know, like, and it's like, that's not actually practical. Like it's not like that, but it's, it's almost like, you know, having that baseline. I think my friend actually gave me that phrase. I don't want to state that as my own, but it's like, you know, it's not cheap to have that, that first resistor, you know, bought from an online distributor, have the board made, you know, wait the time, you know, have spent my time making all these things. Like the first resistor on a board is a significant cost. And I've been trying to like rectify that too, for like, you know, a lot of the houses now are offering like assembly services and you look at it and you're like, oh my God, it's going to cost $800 to get the first five boards manufactured. But like. But then it's cheap. It's a lot cheaper then, you know, it's almost like, you know, that difference in cost is it's almost always worth it. So yeah, it's, it's kind of like balancing that versus the embarrassment of sending my crap boards to some, you know, if it's like a board that's bummed out and it's like, oh yeah, sorry. I didn't mean to do that, but I would have fixed it on the bench, you know, like.

**Dave Jones:** Well, we're, we're, we're in that position here because the new micro supplier, the latest prototype, we probably want to get like 15 of them made.

**Chris Gammell:** Sure.

**Dave Jones:** And so that we can, you know, give them to various people to, you know, try out and have a play around with. And it's like, well, we're definitely not going to do 15 hand assemble because there's a lot of parts on this sucker and they're small, you know, and it's just fiddly, right. That's it's just a ton of parts. And like, even if we did like a, um, a, um, uh, like a reflow thing, you know, even if we did a, like, if we didn't solder each one by hand, you know, even if we did the, uh, reflow stencil thing and even then it's just not, it's just not worth it. We'll just get somebody to make them for us. We'll, we'll make the first one here to make sure it's okay. We'll do that by hand and then power it up. And yeah, it looks like it kind of works. Yep. You know, and then we'll get the rest a little short run and it'll be reasonably expensive to get that, you know, those 10 or 15 made. So.

**Chris Gammell:** Oh yeah. Right. But, but the cost of having, having 15 evaluation units is worth it. Right.

**Dave Jones:** Oh yeah. No, of course. Of course. Cause yeah. Cause we're at that point now where like, and we're getting a prototype cases made as well. So we, you know, we're serious now we're getting all these, uh, cause everything, there's a lot of custom stuff in this. There's a custom heat sink. There's a custom, uh, case. There's a custom LCD. There's a custom, uh, clear screen, which goes over the top of the LCD. There's custom, uh, keyboards, you know, everything's like, there's a ton of stuff custom. Actually, even, even the connectors are custom. So, you know. Oh no, you didn't. Dave. And I'll transfer. What?

**Chris Gammell:** Why did you do this?

**Dave Jones:** No, it's, it's actually not, it's not as bad as you think. It's not as bad as you think. We just needed a, a banana jack that was slightly different to, you know, there's reasons for it and blame David too, for talking me into it. Anyway, uh, it's yeah, no, we found a company where it's, there really wasn't, they didn't really charge us anything for, for doing this custom thing. Right. So, you know, it's, it's not like a thousand dollars tooling for this, this, uh, custom banana plug. Right. It's just, no, it's not, it's not that bad. And we've got a custom transformer. I mentioned it.

**Chris Gammell:** I mean, what happens when all these sourcing issues come up though? Like if like a banana jack company gets flooded or transformer, you know, like you're not using off the shelf stuff.

**Dave Jones:** So yeah, no, no, we aren't using off the shelf.

**Chris Gammell:** You'd mentioned the transformer last time.

**Dave Jones:** Yeah. Yeah. Yeah. We did mention the planar transformer and well, like we'll just have to deal with that when and when, and if it comes up, it's like there's sometimes like you can't avoid it. Like it's not when we're not designing a, you know, a, um, Arduino hat here, you know, a Arduino shield that sits on top and all it is is a blank board and some PCBs. Right. This is like a, a proper polished professional product that looks and feels like a custom product. Right. And you can't do that with off the shelf stuff. Right. It just isn't possible.

**Chris Gammell:** Well, technically it is going to be a custom product at this point because you're putting a bunch of custom stuff in there.

**Dave Jones:** So yeah, it's just, you know, we can, we can send you the latest, uh, render if you like after the show.

**Chris Gammell:** Well, I mean, it's going to be good to see, uh, what it all comes together as. So I think that, you know, like, like you're saying, it's, I guess custom stuff is necessary sometimes. And that also can, I mean, like, to be fair, that can be the secret sauce of a product. Right. So you're trying to find something that, uh, only you can make then that actually can be kind of good.

**Dave Jones:** It makes it harder for somebody to clone. Whereas my microcurrent, for example, trivial for anyone to clone that it's an off the shelf box with a PCB that sits on top five minutes working. You're done. You can produce one that looks exactly like it.

**Chris Gammell:** Right. It's open source hardware, isn't it?

**Dave Jones:** Well, it is open source hardware. Yes. So you can. So I make it even easier for you, you know, but yeah, but, but you get the point. Yeah. So it's, uh, yeah.

**Chris Gammell:** Speaking of open source hardware, there actually is some news on that front. Uh, the open source hardware summit, uh, is canceled. Not really. Uh, they were going to do the, uh, the summit in China this year, this fall in September, um, in Chennai or something.

**Dave Jones:** Yeah. But there goes most of your market and there goes most of your people who would attend such a thing, wouldn't it?

**Chris Gammell:** I think, yeah, a good chunk would be, I think it would be a much reduced number, but I think it also would provide some interesting travel opportunities for people.

**Dave Jones:** It'd be interesting for those who want to travel to it. Yeah.

**Chris Gammell:** Yeah. Sure. Yeah. I mean, that's the downside. So they canceled it.

**Dave Jones:** Why, why did they cancel it?

**Chris Gammell:** Uh, there's a blog post on the, on the, uh, the amp hour, which we can, we'll link in as well. But basically it was something about like NGOs in China and how they operate.

**Dave Jones:** It doesn't, uh, doesn't work.

**Chris Gammell:** Oh, sorry. Non-governmental organizations. So like a lot of charities and 501c3s, at least in the States, that's how they're classified. Um, uh, they, they have, uh, they have different governance and taxation type stuff. And, um, so yeah. Right.

**Dave Jones:** It just became, there were too many, uh, hurdle, too many paperwork hurdles for them to jump through too many hoops to get this event organized. So they just gave up.

**Chris Gammell:** Oh, no, no. I think it's, I think it's more around like acting as a, acting as an NGO in China, basically the government cracked down on.

**Dave Jones:** Oh, and they mentioned sponsor. They've got to have a sponsor. Right. So you've got to have a Chinese, a Chinese partner unit, a CPU, Chinese partner, there's a new acronym, CPU, Chinese partner unit to act as a sponsor for the summer. Uh, CPUs can only be certain types of organizations such as universities registered in, oh God. Yeah. It's like reams of paperwork. They're mentioning preparing documents to get official status. Oh God. Yeah. No, scrap that. I'd, I'd, I'd pull out too. Yeah. Yeah. I think that's sheer amount of hassle involved.

**Chris Gammell:** Yeah. It's unfortunate too. Cause I think a lot, I was personally, I was thinking about going to that and I'm disappointed, but, uh, you know, it's usually a good conference to go to. That's one, that's one of the ones on the list that I like, I like going to. Right.

**Dave Jones:** So when is it, when is it usually held?

**Chris Gammell:** It's usually September. So it used to, I think it started like the week after Maker Faire New York. So it was like people would travel from that to anyone is on the West coast or East coast rather.

**Dave Jones:** So they do the road trip thing.

**Chris Gammell:** It's bounced around. Yeah. Yep.

**Dave Jones:** I'm traveling a lot less these days.

**Chris Gammell:** I don't, I don't mind that. I don't mind that at all. Right. Okay.

**Dave Jones:** And you wonder why I don't travel with you. Yeah.

**Chris Gammell:** Well, hey man.

**Dave Jones:** I just got another offer the other day to go to the U S someone in the U S who should remain nameless offered me there. They're changing their thing and they like my videos and they want me to have input on their new, uh, stuff. I'll tell you after the show. Here it is. Okay. Yeah. It's not, it's not a big deal, but yeah. Anyway. Um, yeah, yeah. They offered for me to come out and it's like 40 hours travel. Sorry. Amen.

**Chris Gammell:** If you hit U S soil, I'll be there. How about that? That's my, that's my guarantee. Of course. Yeah.

**Dave Jones:** Hey, look, if I hit U S soil, I'd come find you, you know, it's like, if I'm going to hit, if I'm going to hit U S soil, it's like, I'm going to go for broke. Right. I'm going to go for broke. Right. Right. I wouldn't sleep for two weeks. It'd be like, you know.

**Chris Gammell:** Right. Right. Yeah. Someday. Someday. Maybe with the, with the kiddos in tow with you, I'm sure. And Mrs. Eve. I get the whole, the whole gaggle of, of, of nerds here.

**Dave Jones:** It would, it would literally have to be that because I like, I like, I take the kids to school three days a week. I'm now, I'm now the local soccer coach. Right.

**Chris Gammell:** I heard about that. I saw that. I saw that on Twitter.

**Dave Jones:** I got roped into being the local soccer coach. I've got to take them to all to other activities and stuff like that. There's literally like, I, I, the, probably the most I could disappear for. If I time, if I timed it right, it's probably two days. It's probably like a day and a half, two days. Right. That, that would literally be the longest I could go somewhere without having to reschedule and find like, you know, get parents to help out. Right. Exactly. Taking the kids and looking after the kids. Calling favors. Yeah. Yeah. Yeah. It's, it's, you know, so it's just, yeah, it's silly. So yeah. People ask why I don't go anywhere. Sorry. That's why, you know.

**Chris Gammell:** Yeah. Yeah. No, I'm sure people with, people with kids understand that one. Oh yeah.

**Dave Jones:** And, and, unless you're like, then people make the argument, well, I've got kids and I go for, you know, I'm on the road all the time. It's like, yeah, because that's your job and you're used to that. So you. Yeah. Scheduled around and stuff. You organized your life around that lifestyle, you know. Yeah. Whereas where you used to be in like, I'm five minutes away, drop the kids off, you know. So, yeah. Yeah. It's a very different lifestyle thing. Anyway.

**Chris Gammell:** Yeah, man. Well, speaking of lifestyles, I have a new thing in my life. I don't know if you've been watching my, my Twitter feed, but every morning I, I put up a new, a new video.

**Dave Jones:** Oh, I noticed you were doing a lot of videos at the moment. You're back to a video a day. Is this a thing?

**Chris Gammell:** Uh, it's yeah. So it's like. Why?

**Dave Jones:** You want to build, you want to build up your channel? Is it part of your course thing or is it.

**Chris Gammell:** No, it's not that.

**Dave Jones:** They seem to be just free videos.

**Chris Gammell:** Yeah. It's all KiCat stuff. So it's, it's a 5.0 thing. It's videos I've been meaning to make for a while, but it's kind of like what you're talking about, like finding that time, like you have to like find the time in the day. And, uh, so like in my morning routine now I've just kind of got it so that I go upstairs, turn on, turn on my recording setup and record a video about KiCat that I think about while I'm showering. Maybe TMI there. Sorry about that. But you know, like just kind of like that's where it fits in the day before I leave for work. And, uh, and so that's worked out really great. So there's a lot of.

**Dave Jones:** Well, your format allows for such a thing, whereas my format doesn't, for example, you know.

**Chris Gammell:** This is like the, uh, the five minute videos that you were going to do at one point, you know?

**Dave Jones:** Yeah. Yeah. Yeah. Those five minute rant videos. Exactly. Right. Right. Yeah. Yeah. So there's no reason I couldn't do videos like that. It's just that they wouldn't be the same quality of what people come to expect on my channel. Quality in quote marks, you know, the same, I think, yeah, the same quality is right.

**Chris Gammell:** It's, it's, it's, they have a certain quality to them, you know?

**Speaker ?:** Yes.

**Dave Jones:** Well, then that I, they're edited and, you know, and they're polished. They've got like stuff overlaid on them and they're, you know, they're, they're at least a little bit polished in that. You know, I take out ums and ahs and I take out pause, other pauses and stuff like that, you know? And like with your thing, you can do that because you've got the pause button, right? You just hit the space. Oh, I got rid of that.

**Chris Gammell:** I got rid of that. Oh, really? What? Yeah. So now I do it where, um, basically I, I just record for five minutes. If I get it wrong, I throw it out and just do it again. Ah, that makes sense. Yep. Yeah.

**Dave Jones:** Yep. I can, I can dig that. Yeah.

**Chris Gammell:** But it was all because there's a lot of changes. Like I kept talking to people about the 5.0 version of KiCat and a lot of people were like, yeah, I didn't know about all these features. I keep finding about new features too.

**Dave Jones:** Right.

**Chris Gammell:** And then, uh, 5.1 just, just got tagged as getting released soon. So if people are interested in that stuff, uh, there's a new version there and then they'll start working on six already. So it's not, it's not fast. Don't get me wrong. It's not fast, but it's, you know, it's, it's moving and that's great. So I'm very excited about all that stuff.

**Dave Jones:** Have you thought about a separate channel for that rather than on your contextual electronics channel? Is it better just to have like a KiCat channel? That's a good question, but yeah. All KiCat 24 seven, you know, it's just. Everything KiCat.

**Chris Gammell:** I guess that would be. Yeah, I guess so. I don't know.

**Dave Jones:** Because you've got a lot of material that, that you could seed onto there.

**Chris Gammell:** Really? Sure. Sure.

**Dave Jones:** The problem with that is that it's not evergreen content. Some of it. Right. Exactly. And that's the other reason. And that's just, you know, it's how to use this new feature and this new feature changes in the next version. Oops. Right. Video. You may as well, you may as well remove it. Right.

**Chris Gammell:** Right. Someone, someone made a joke the other day. They're like, what do you, what do you need to, what do you need to, in order to learn how to use the KiCat for layout software? And they're like, YouTube and a good, a good internet connection. You know, like. Right. And that's, and that's unfortunately like, that's just kind of the quirkiness of, you know, CAD programs and specifically KiCat. But yeah, it is, it is a little different, but you know, there's also learning. Like I watch other people's videos about that stuff too. Like I like, I think you can kind of glean other, other methods from, you know, even when there's specifics around, you know, how to do a certain thing in a certain CAD package, I think. So like when I watch like Fusion videos, you know, I might be watching like how to do a spline in, in, that's not the right term. How to do like a rotated shape in, in Fusion 360, right. It's, it is very specific to that release of Fusion 360. And yet.

**Dave Jones:** Oh, and it changes, does it?

**Chris Gammell:** It does. Yeah. Oh yeah. That day move buttons. Well, a lot less than they used to from like, from when they started like four or five years ago to now, it is, is very different. And I like it. Um, but it's, uh, but then.

**Dave Jones:** You like, you like the change, the things changing all the time or you like the, how they do it now compared to how they used to do it.

**Chris Gammell:** I just like the software in general. Like I'm willing to put up with it, you know, like I have pretty high tolerance for that kind of stuff.

**Dave Jones:** Yeah.

**Chris Gammell:** But you know, when I was watching people do it, it was often like, I don't need to know how to make like the spiral on a, you know, a screw, you know, like that's like often the thing I'd be watching. It's like, I don't even know how to do that. And yet that's a new technique that I learned just from watching the feature about the software. And so I, you know, I'll watch that kind of stuff. I'll watch a lot of things on YouTube. Let's be honest. I met someone the other day who said they, they, they watch chainsaw videos on YouTube. Why not? I didn't know that was a thing. Like, like sometimes it's just like, I didn't know this is a thing, you know, there's a,

**Dave Jones:** there's a genre for everything. Like it doesn't matter what you're into.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Yeah. There's a, there's a channel out there, channel out there devoted to it. Oh, I started, I tweeted this the other day because I just did a free energy video, right? Debunking these ridiculous. It's still there by the way. Can we actually talk about that for a minute? It's like, right. So I did this video. People don't know. I did this. We'll link it in. I did this video. It was just like a, actually this was a single take video. I didn't edit this at all. It was a blab. You know, I just press record, boom. And then finished 18 minutes later. It was literally.

**Chris Gammell:** Which is short, which is short for you. Oh yeah. Yeah. Yeah.

**Dave Jones:** And then I upload it. And anyway, there's these four, some viewer pointed me to these four Kickstarters that are basically free energy over unity, you know, BS, right? Yeah.

**Chris Gammell:** And one of the ones you linked on Twitter at least was just like, it literally said like, it was like a computerized voice. It was like free energy all the time.

**Dave Jones:** Free energy, perpetual motion, infinite energy, infinite energy and perpetual motion. Right. They literally say it in the video. Yeah. And it's just like, and sure enough. Right. And somebody said, look, somebody just posted a post on Twitter this morning. I retweeted it that, oh, look, they were going to give Kickstarter the benefit of the doubt because the Kickstarter is so huge now that they don't have the number of people to evaluate every campaign. That's what I was going to say as well. Back in the old game. Yeah. You waited a couple of days and then a human would eventually get around to looking at your thing and approving it. And they thought, look, I'll give them the benefit of the doubt, but I'm going to report this thing anyway. So you reported it and they got the response back. Saying, oh, no, it passes all of our, it doesn't violate any of our guidelines. What? So perpetual motion. No, no, no problems whatsoever. Like the people reviewing these things are either so incredibly stupid they don't understand what perpetual motion is. I mean, you know, anyone with a high school level education knows what that is. Anyway. Yeah. What if they're outsourcing that or something? Or they have to rigidly follow the procedure and the procedure doesn't specifically exclude perpetual motion machines.

**Chris Gammell:** Right. So if you check all the boxes to have like description and video and all these other things. Yeah.

**Dave Jones:** Does it violate any of the... No. And it's from freaking Cameroon. And as you said, it's like it's half in English, half in French from Cameroon. And it's in a robotic voice and they don't have a real prototype. Like it's just...

**Chris Gammell:** Maybe it's one of those things too where like, you know, like sometimes you can only really deal with like exception reports. Like, you know, if you have high enough volume. So like, so if you look through like compiler errors and compiler warnings, all that other stuff, you only really give a crap when something goes wrong. Right. You might not check out the warnings.

**Dave Jones:** You only care about the errors. You don't care about the warnings. Exactly.

**Chris Gammell:** So like if this project started getting funded and then people complained about it, then you pay attention. You know what I mean?

**Dave Jones:** Yeah, pay attention, but it only had like $10 in backers. Yeah. I was like, oh yeah. Yeah.

**Chris Gammell:** Because I think some of that is just, I mean, it's still laughable to have that on there.

**Dave Jones:** But at least it gives... But at least it gives...

**Chris Gammell:** Yeah, exactly. It gives you something to talk about too though.

**Speaker ?:** Exactly.

**Dave Jones:** Like, yeah. Like nobody's going to get sucked into these because they're so bad that they're not going to go viral. Yeah. Like the Solace one did that I did a couple of weeks.

**Chris Gammell:** I think those are more dangerous where they're like, you know, they feel science-y enough. Really slick marketing. Yeah. Yeah. Exactly. Yeah.

**Dave Jones:** And they have really polished slick marketing. Whereas these over-unity machines are done by some nut job in their basement, right? Right. And they've just put, you know, zero effort into the campaign and it's just... Yeah. Yeah. Well, then eventually...

**Chris Gammell:** And it's not polished or professional. You know, you could like put some like background music to it and it could be like a new like chill wave kind of like, you know, new agey music kind of thing, you know? Yeah. Free energy. Mts, mts, mts, mts. It's...

**Dave Jones:** But it's about the principle of these things. That these companies are so inflexible that they allow this.

**Chris Gammell:** And I don't... I mean like...

**Dave Jones:** You know, it's just...

**Chris Gammell:** I don't think that's that big a deal personally. I mean like I get what you're coming from. Like... But I think it's just a numbers game honestly.

**Dave Jones:** Oh yeah. It's a numbers game to them. But if you cared about your reputation as a company, you would –

**Chris Gammell:** Maybe, yeah. I mean you could say the same thing about YouTube though, right? I mean YouTube has so many people on it. Like you can't possibly police everything. And if you did, I think that would be worse.

**Dave Jones:** You work based on reports, and that's what you should do here. But also the fact that there's not – it's not like there's thousands and thousands of these perpetual motion projects and perpetual motion campaigns, right? So it's like –

**Chris Gammell:** Yeah, so you're saying like have like a block on certain topics, that kind of idea?

**Dave Jones:** Well, not necessarily a block, but an engineer or at least somebody with the knowledge to review these sorts of things. And everyone said, oh, they can't afford to hire an engineer because then everyone else – because they'd have to pay them twice the amount of everyone else, and then everyone else would get jealous. And then, you know. But as I said in the video, put them – have an engineer on a retainer, and they do it on a case-by-case. Here's a new project. Oh, it's to do with, you know, they're making some energy device. Send it to Joe Bloggs, and he'll – Joe Bloggs engineer, and he'll evaluate it, you know. And it doesn't cost much. You could pay him $100 or something, and it'd take him 10 minutes to look at that and go, nope. Yeah. You know, like it's not – it's not hard. It's not hard. If they really wanted to do it, they could, and it's just embarrassing that this sort of stuff's allowed. Whatever.

**Chris Gammell:** I mean, like I think it was more of a problem when it gets through, so I don't – I don't know.

**Dave Jones:** Yeah. Anyway.

**Chris Gammell:** What's up with these – so now I'm looking at your Twitter feed. And first off, I found the phrase that I was thinking of Ozzyman for, fair dinkum. I'm sure you've said it on here before. Oh, fair dinkum. Yeah.

**Dave Jones:** I've said it when we were here, I'm sure. Yeah, I've said it on here all the time. Yeah, I'm sure you have. Fair dinkum. Yeah. Yeah.

**Chris Gammell:** I think of Ozzyman, sorry. No offense, Dave. No worries. You had posted about read trailers. But no, it was the chips that you bought on AliExpress. What were those?

**Dave Jones:** Oh, yes. These are little RAM memory, SRAM chips or whatever. Yep. Yep.

**Chris Gammell:** So what were they for though?

**Dave Jones:** Oh, they're for a scope upgrade that I'm doing. This scope has like spare pads for these RAM chips. So you can upgrade them and you can hack the model to be an upgraded model with color screen and stuff. Oh, nice. Okay. Yeah. So I ordered them on AliExpress. Foolish me thought that they'd be new old stock.

**Chris Gammell:** I mean, you can hope, right? It's usually low enough cost and it's like, yeah, I'll take a shot.

**Dave Jones:** It's a low enough cost. I'll take a shot, you know. And sure enough, they come in and they're de-soldered. The pins are bent. There's shorts between, there's solder bridges between pins and they haven't even been nicely removed from the board. So it's like they're being removed on some hot plate, you know, some like fry pan or something. Right, right. So I wouldn't even bother to solder these in. Right. Like I simply would not trust them. I wouldn't, you know. Yeah. So, yeah. Unless I had no other choice and I was absolutely desperate. I'm just not going to waste my time with them. I agree. I agree. Just try and order some more and I'll take pot luck again. And if they turn up looking like they're kind of new, then, you know, at least I'll... Take a shot. So at the moment, somebody in Shenzhen is furiously trying to silkscreen on the top of the chips, the one that I actually ordered. Yeah. That's right. I'll probably get fake chips or something next. Yeah. It's like, oh, God.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Fair dinkum, mate.

**Chris Gammell:** Yeah. Fair dinkum.

**Dave Jones:** Yanks cannot say fair dinkum. They just can't say it.

**Chris Gammell:** Fair dinkum?

**Dave Jones:** Yeah. It's too formal. Fair dinkum, mate.

**Chris Gammell:** Got it. Got it. Okay.

**Speaker ?:** Yeah.

**Chris Gammell:** I wanted to talk about batteries.

**Dave Jones:** I've done like 20 videos on batteries. Knock yourself out.

**Chris Gammell:** So how often are you doing stuff with unprotected 18650s?

**Dave Jones:** I would not build an unprotected 18650 into a product.

**Chris Gammell:** Why is that?

**Dave Jones:** Let's put it that way. Yeah. Because it's, unless you built the protection into your design. Yeah.

**Chris Gammell:** I mean, this is, that's the idea. So I basically have a, yeah. I have a thing where I have a cell and I have a, you know, a charging circuit and it takes care of all that stuff outside of it. But.

**Dave Jones:** Oh, well, then, then that's fine. Yeah. But if it's like, if it's anything, especially if it's user replaceable and stuff like that, you're just like, because people are buying these, you know, 18650s from anywhere in Shenzhen, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Like the worst possible places. And you just, yeah. I was amazed.

**Chris Gammell:** So I was shopping for them a couple of weeks ago and it's just like, it's like, it's hard to find them, honestly. Like they're not like listed a lot of places. There's very few retail stores.

**Dave Jones:** It's hard to find an unprotected one.

**Chris Gammell:** It's hard to just find the cells, honestly. Like, I mean, like. What?

**Dave Jones:** 18650 cells. Are you kidding me?

**Chris Gammell:** No. So like, okay. So let me, let me be more clear here. I was looking at Amazon Prime. I wanted them in two days. Right. And yeah, no one has that because like they'll only ship them ground, which makes sense because it's lithium. Right. Of course. Yeah. Lithium.

**Dave Jones:** Yep.

**Chris Gammell:** And then like a lot of the listings. So like you have to, so it's just like non-standard stores. So like even within DigiKey, I was looking on there and like SparkFun sells some that they basically distribute through DigiKey. But that's some of the only cells that are on DigiKey is the SparkFun cells. Really? Yeah. It's surprising. Wow. You'd think that would be on there. I'm stunned. Yeah. And so it was interesting just seeing like what was out there. And, you know, so basically you have to either go to a larger distribution kind of point. I didn't, I didn't go to like larger distributors like Arrow and Avnet. I didn't look at those. I was literally just looking in there. I found it. I'm done. Whatever. But, but like I kind of expected it to be, you know, more prevalent and, and it's just kind of, you have to look in other places, you know, because it's, it's less of a consumer like thing. I think. I think, I think that's really what it comes down to.

**Dave Jones:** Well, what, what type are 18650s? You're talking about the consumer ones with the nib on them or are you talking about the tag ones?

**Chris Gammell:** Can you define the difference?

**Dave Jones:** Well, the solder tabs? The ones that have like, like a normal battery. They have like the little nib on the end that you put into a regular battery holder, or you're talking about the ones that have the welded tabs that come off and they're permanently installed inside your product.

**Chris Gammell:** It's still, but still the same, like a cylindrical cells.

**Dave Jones:** They're still, they're still exactly 18650s. Got it. But they just have a different interface. They just have a different physical.

**Chris Gammell:** This is, this is the nib, but it's not like the kind of nib that I think about for like a AA battery. It's not actually raised that much above the, the, the, the plastic wrapping kind of thing.

**Dave Jones:** Yes. Yes. They're quite indented. Did you know that there's a length difference between the unprotected cells and the protected cells? And that can be a pain in the ass.

**Chris Gammell:** I figured that because where else are you going to put the protection, right? It's just like a circular board that goes on top, right?

**Dave Jones:** Well, no, you can, you can custom design your cell to make it, your actual cell to make it shorter and then put your protection in there on top. But only your more professional manufacturers do that. If you just get some, you know, one hung low brand, then it's going to be a normal 18650 and then they pack the little piece of the on top and that's why it's bigger. So, you know, it depends on who you get them from. But yeah, some things just don't fit. Right. Exactly. Yeah.

**Chris Gammell:** If you don't have like a, like enough give on your, on your, um, your snapping pads, that kind of thing. Yeah. So, I mean, I mean, this is still an early product and I'm, you know, playing around with it too. So it's not like, so, but like I, I've tried it. I've, today I was like playing with it. I got it plugged in and it's all charging. It's doing fine, whatever. And, and I'm just kind of curious about your takes on it too, because I'm thinking about, you know, temperature differences and stuff like that too. Like, is this going to be okay in the field? That kind of thing.

**Dave Jones:** But are you talking about when, when it's charging or when it's discharging?

**Chris Gammell:** Uh, both.

**Dave Jones:** Both. Right. Yeah. So it's a fairly heavy discharge.

**Chris Gammell:** So, so I'm saying, no, not, not, not the internal temperature. I'm saying the, the environmental temperature around it. Yeah. Yeah. Right. That kind of thing. So like, you know, like, does it, does it hold up over temperature? Like, does it, uh, like capacity type stuff change at lower temperatures, those kinds of things.

**Dave Jones:** Have you read the data sheet?

**Chris Gammell:** Some of it. Uh, yeah. I'm saying, I'm asking you about your, you know, like your experience over time though, you know?

**Dave Jones:** Well, I can't remember precisely, but the capacity will, can change slightly with temperature. Um, well, if you're talking about, you know, a 40 degree change, right? We, which is possible. People think that's extreme. It's not. Right. So for a product, like here, here in summertime, 40 degrees. Oh, okay. You're saying, you're saying C. In the U S in wintertime, it's minus 10.

**Chris Gammell:** You're saying C. Yeah. I was thinking, uh, you know, the day we recorded. Oh yes.

**Dave Jones:** Yes. Sorry.

**Chris Gammell:** When we recorded the other day or like a couple of weeks ago, that set fire to the tracks episode, uh, that was minus 30 C and today it's about 10 C. So it's about, no, it's about five C today. So 35 swing.

**Dave Jones:** So in those sorts of temperatures, like everything matters, your LCDs stop working.

**Chris Gammell:** Right.

**Dave Jones:** Right. If it doesn't flow or what the, the liquid crystals do not flow. Go and go and take your multimeter or some other product, whack it in the freezer for half an hour, take it out. And then look at the update rate of the screen. Look at the update rate of the LCD. The, the, uh, the numbers will change very slowly because the liquid crystals are, you know, starting to freeze up in there and they just can't move fluidly. So your update rate goes, you know, crazily slow on your LCD. So, you know, basic stuff like that. You just can't rely on things to work. So it's a, you know, it's kind of a big deal, but you know, which is the big difference between designing a product that's designed to be used like outdoors or whatever. And one that's designed to be used in like a lab environment and things like that. So, yeah. And, and, but sometimes you don't like care about that. You just go, well, it, it is what it is. Right. If it doesn't work down at minus 10 or something, well, you know, sucks to be them. Yeah. So, yeah. Like, yeah. Like you can't cater for like everything. So, well, you can, but there's a lot more engineering effort that goes into it. And a lot of the time, like for example, this micro supply that we're doing, right. It's, it's designed to be portable, obviously. And like, it could be used in minus 20, but are we going to like design it around that? Well, no, you know, in fact, we haven't even tested the LCD down at, down at, you know, zero yet. So.

**Chris Gammell:** Right. Right.

**Dave Jones:** I don't even have the capability to, well, no, I could whack it in a freezer, I guess, but you know, I don't have any controlled capability to do that here.

**Chris Gammell:** Hmm. Yeah.

**Dave Jones:** So, you know, it's, yeah.

**Chris Gammell:** Yeah. You need like, like a, like a cycling, like a cycling oven or something like that you're saying?

**Dave Jones:** Well, what you need an oven that goes below that, what you need a thermal incubator. Right.

**Chris Gammell:** Right. Right. Right.

**Dave Jones:** That goes, that goes below zero, you know, and like I've, I've got my little thermal chamber here, but it only goes down to about five degrees thereabouts, you know, depending on ambient temperature. Yeah.

**Chris Gammell:** Because your heat exchanger, you basically need like a heat exchanger that's pretty beefy to get, keep going down below that.

**Dave Jones:** Yeah. It's just, yeah. It's just, you know, it's not great. So if I want to go below that, basically have to whack it in the fridge, really. And yeah, it's, anyway. Yep.

**Chris Gammell:** Okay. So no other thoughts about unprotected cells in general?

**Dave Jones:** Well, so is this going to be a consumer product?

**Chris Gammell:** No, this is all industrial. This is industrial.

**Dave Jones:** Oh, industrial. Well, no. Nothing I do is consumer, Dave. Okay. Well, like I, in theory, I probably would recommend using a, just, you know, basic engineering, you know, safety principles. You would use a, a protected cell because you can.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Well, there's cost differences. There's really no reason to, right? Because something could go, right, you've got your hardware, you've designed that in, that's fine. But what is something, what if your hardware fails? Right. And then it shorts out. There's nothing to limit the current coming from that cell.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. There's nothing. And that's what the protection circuitry does. But then you can argue, well, the protection circuitry could fail and short out. Right? True. Yeah. Okay. You know, it's like, it's, yes, sir, it's turtles all the way down. Right?

**Chris Gammell:** It's like. Right. Right. Well, Adam's quarks could reverse polarity and, you know, they can implode upon themselves.

**Dave Jones:** Right.

**Chris Gammell:** Right.

**Dave Jones:** So, yeah, it's turtles all the way down. And I, but no, I would do it. Right. Because generally, like, especially if you buy a quality cell, you know, if you buy a quality Panasonic cell or something like that, or some other name brand, and they're going to have name brand, you know, qualified protection circuitry in there. Right. Yeah. It's just one less thing for you to be concerned about. I would certainly do it. There's a lot of energy in lithium batteries. They're freaking dangerous.

**Chris Gammell:** Oh, yeah. Yeah, they are.

**Dave Jones:** Right? They're, they're just, no, I would, I would do it as a matter of course. You know, if you deliberately, from a, just simply from a liability point of view. Right. You've considered this and you've discussed this publicly. Publicly. Hey, man, this isn't out yet. And then you've made, this isn't out yet. And you've made the deliberate decision, engineering decision to not go with a protected cell and it melts down, you're liable for that.

**Chris Gammell:** Yeah.

**Dave Jones:** Whereas if you used, you know, a good engineer, if I was an expert witness in court, if I was called against trial against Christopher J. Gamble. Oh, man. Yeah.

**Chris Gammell:** Dave is, we now call Dave Jones. We now call our expert witness. Who has a fair dinkum testimony against, against Christopher J. Gamble.

**Dave Jones:** That's it.

**Chris Gammell:** Yeah.

**Dave Jones:** And I would say, yes. You know, a good engineering practice would dictate that you would choose, unless there were mitigating reasons that you needed, that you couldn't use it, size, other requirements, you know, efficiency loss or whatever. There was some other engineering reason why you didn't have it, why you couldn't have that protection circuitry. Then good engineering prudence would dictate that you would choose to have it. And if you deliberately decide it just because, meh, sounds like a heap of shit, right? Couldn't be bothered or whatever, right? You're going to be liable.

**Chris Gammell:** Right. Right. That's a good point. That's the thing, right? Yeah. That's a good point.

**Dave Jones:** So, you know, it's a, so yes, use, use your protection circuitry.

**Chris Gammell:** Yeah, well, I was thinking more on the, on the cell side versus on the, you know, the circuit side. So that's, I think it's just.

**Dave Jones:** No, I'm talking about the cell side. I'm talking about the cell side.

**Chris Gammell:** Yeah, double redundancy in that case, right? Oh, yeah, yeah.

**Dave Jones:** You wouldn't, wouldn't design your own. I mean, you can buy qualified little boards that, you know, you put in line with the battery, especially if you've got like the tab wired batteries. Right, right, right. And then you could like wire, and then you wire it in series. You can buy qualified PCBs that actually protect your product. Like, but you wouldn't go, wouldn't necessarily go design that on your PCB, I don't think. You could, but it's just an extra layer of when you can buy a cell that's already protected and qualified.

**Chris Gammell:** Right, right. Yep.

**Dave Jones:** Extra thing you don't have to worry about.

**Chris Gammell:** Yep. Good thinking. Good thinking.

**Dave Jones:** Basic. I don't know why you even asked a question, quite frankly. Got to talk about something here, Dave. Come on, man. Right, yeah, right, yeah. We have to fill the time in. I mean, the other thing too is that. As I said, there are legitimate reasons there why you would choose not to, right? Okay. Not to, deliberately not to have a protection device in there. So it's a, you know, something that should be discussed.

**Chris Gammell:** What would be some of the reasons not to in your mind?

**Dave Jones:** They would be, as I said, a space requirement. If you're designing ultra low, like a volumetric efficient product, like a little watch, for example. You know, well, a watch is not a good example because they've got such low capacity batteries anyway. Right. I don't know. You've got some, you know, you've got like an iPhone or something, you know, which is a real high capacity, dangerous battery in there. But you were so packed for room that you just couldn't add it. You just couldn't add the protection circuitry for some reason. That might be another reason. There might be discharge reasons.

**Chris Gammell:** I guess that's not user serviceable either, right? That's not a...

**Dave Jones:** No, it's not. It's not user serviceable. So, you know, maybe you might choose. No, I mean, you wouldn't in a consumer product selling in the millions like that. You know, you'd be like crazy not to, but of course, because then you end up like being Samsung, right?

**Chris Gammell:** Right.

**Dave Jones:** Where their phones just catch on fire. Right. But they caught on fire internally where the external protection circuitry didn't matter. Right? So that was another turtle there. Yeah, that was a space thing, right? Right? That was a turtle, but two layers below your other turtles that you're dealing with. Right. Right? I'm telling you, it's turtles all the way down. Yep. And so that protection circuitry did squat. Magical firebags, no, no deaths, you know? Yeah. It did squat.

**Chris Gammell:** Yeah.

**Dave Jones:** So then what do you do? Add protection layer, but add protection circuitry on individual layers.

**Chris Gammell:** Right.

**Dave Jones:** You know? It's kind of what they do in the Tesla. Once your solution gets technically big enough, like a car, like a Tesla car, right? They've got individual cell protection. Then they've got group cell protection. Then they've got major group cell protection. Oh, really? And then they've got entire pack protection.

**Chris Gammell:** I didn't know that.

**Dave Jones:** They've got protection up the wazoo.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Because you have to. It's just crazy. Well, I'm not sure if they have... Yeah, they must have individual cell protection. I think they do. But I know that they do have like... And then string protection so that a string can go and it protects the string and so on and so forth. And yeah, it's crazy. And then there might be a leakage issue. I know that, you know, lithium's got... Well, it doesn't have like low leakage. Like, you know, it can last for a year or two, right? On one charge. But like leakage might be a problem, for example. Perhaps. I don't know. If you had an ultra low leakage cell that you were trying to use, then the protection circuitry might take a microample too. Right? And that's constant leakage that you don't want, for example.

**Chris Gammell:** Right.

**Dave Jones:** Yep. You can... Yep.

**Chris Gammell:** Yeah, because it's powering. It's got like a resistor going to ground or something just to watch and have a FET that activates or something like that.

**Dave Jones:** Like the gate of the tranny's got to be pulled up to...

**Speaker ?:** Right.

**Dave Jones:** I don't know. Right? Who knows? I haven't looked at it for years. But yeah, like it is non-zero. It's non-zero. So...

**Chris Gammell:** Yep.

**Dave Jones:** Hmm.

**Chris Gammell:** Cool.

**Dave Jones:** USB 4. What's this shit about? I haven't heard about USB 4.

**Chris Gammell:** Yeah, that's just a new spec. So basically, if you have a Thunderbolt device, so like the laptop I'm actually recording on right now is a Thunderbolt device. And basically, Intel opened that up and then that got adopted as the USB 4 specification. So it looks very similar to USB-C. It is a USB-C connector. Right. But then it has like the little lightning bolt looking thing on it. Okay.

**Dave Jones:** So it's backward compatible with USB-C. Because the last thing we want is you have another bloody connector.

**Chris Gammell:** Yeah, but it is different though. There's like... I don't know. There's a bunch of weird stuff. So like my laptop connects to my external graphics card and all my monitors through that. And then it has like Ethernet. So like that's kind of like the bandwidth it can do. So like my laptop can drive a video card that drives three monitors and then has an Ethernet connection through it at like 10 gig. And it's like, okay. Crazy. That's a lot of... But every time I plug it in, it pretty much crashes the computer. So there is also that. Yeah. It's real finicky. So... Got it. I don't know. We're just kind of reaching speeds and like, you know, like obviously it's amazing what is possible. But it's like the speeds that they're reaching are just insane. Yeah. You know? Crazy. I don't know what this means for us. It's 40 gigabit per second. So like, you know, you need special transceivers for that kind of thing. It is type 3. You know, you have to do a bunch of weird stuff there. I still haven't... I don't know. Have you put any USB-C stuff on boards yet?

**Dave Jones:** Yes. The new micro supply uses...

**Chris Gammell:** Oh, it does. Okay. But are you using it in USB 2.0 mode or using the newer higher speed?

**Dave Jones:** No. We're not using high speed. It's incredibly low speed. In fact, we could have used USB 1, right? It's like, it's that low speed. It's like 115K bits. It's like serial. Oh, it's just serial. Serial. It's just serial, basically. Yep. Yep. So it's nothing. We're only using it for its physical robustness and for its power capability.

**Chris Gammell:** Yeah, exactly. And I think that is... That's the other people that I've known who've been doing it. Like I know some people who have built with it and it's for the power stuff. And then the higher speed stuff is not really a concern. It's the... You know, you talked about making that one prototype unit soldering yourself. That's going to be fun. Those connectors are not fine pitch. No, they're paying me off.

**Dave Jones:** And we talked about like the original goal was, oh, look, we're going to have multiple connectors on there. We'll have Type-C. We'll have Micro. We'll have Mini-B for, you know, keep everyone happy. And ultimately we decided, no, that's just... It's just stupid. We'll just go for Type-C because you can buy a little adapter that converts Type-C to Micro anyway. So like you just supply that with the product. You can buy that in bulk for like 10 cents or AliExpress or whatever. So, you know, you might as well throw a couple of those into the package. Like it's just... Yeah. So we just went with the Type-C.

**Chris Gammell:** Yep. That's good. I think that's smart. I mean, conversion is... That's on other people. Mini? Mini-Bs? Come on, man. Who's using Mini anymore?

**Dave Jones:** Mini-Bs? Are there a lot of Mini-B fanboys out there?

**Chris Gammell:** I mean...

**Dave Jones:** They swear it's the most robust thing ever.

**Chris Gammell:** It is very robust, but it's, you know, pretty big. I don't know.

**Dave Jones:** Oh, it's not pretty big. Mini-B? It's not that big.

**Chris Gammell:** It's double the height of a Micro-B, you know?

**Dave Jones:** Oh, yeah, but... When the physical plastic around the micro connector is bigger than the Mini-B, then... That's true, yeah. Right, right. Like, you know, come on. You're having a bit of a wake there. Not being fair dinkum, mate.

**Chris Gammell:** Right, right. Not being fair dinkum. Dinkum.

**Dave Jones:** Oh, boy. All right. We're almost out of time. Yep. Almost out of capacity. What else we got?

**Chris Gammell:** I don't know.

**Dave Jones:** Grab your tickets for the KK conference.

**Chris Gammell:** Oh, yeah. Yeah, that's good. That's coming up. Good. Looking back through my tweets here. I guess you... I mean, sorry you weren't here last week, but we did talk about graphene last week. I know that you've also talked about... I did mention you. Right. I haven't heard the episode. So you talked about graphene. Yeah.

**Dave Jones:** What did you talk about? What did you say about graphene?

**Chris Gammell:** Oh, because Sam, the guest, used to be a researcher with graphene. So he was doing like nanotubes. Oh, wait. Was it nanotubes? Maybe it was graphene. I don't know. Yep. Something carbon-based. Right. And, yeah, so we were talking about all that stuff and how it transferred. He's, you know, now doing perovskites and printable solar cells. So it's pretty cool stuff. Cool episode.

**Dave Jones:** Excellent. But it still doesn't magically produce heat from no input. No. So did you actually discuss that on the episode? No, no, we didn't go that deep. Right. But obviously it doesn't.

**Chris Gammell:** Right, right. Yeah. Actually, here's one last thing. This is just a little bit of like engineering porn kind of stuff. I'll send you a link real quick. This is someone who MG on Twitter is doing PCB stuff with a mill, but there's a solder mask involved. And so it's fine enough pitch that they're milling off the solder mask and then it's just exposing the copper beneath it. And it looks really good. And so you can go back through their tweets and like the...

**Dave Jones:** To what end? To what end are they doing this? What's the...

**Chris Gammell:** Making PCBs at home.

**Dave Jones:** So it's one big... No, no, no. They've got like this existing layout board.

**Chris Gammell:** Mm-hmm. So they applied the solder mask on top after doing the actual milled PCB piece. And then they're milling out the solder mask to expose the copper beneath it.

**Dave Jones:** Oh, okay. Right. So they milled out a PCB. They milled out the copper. Then they applied solder mask at home. Do it yourself. And then they're milling out the solder mask.

**Chris Gammell:** Yeah.

**Dave Jones:** How do you mill out the solder mask without...

**Chris Gammell:** Very carefully.

**Dave Jones:** ...damaging the copper is my first question.

**Chris Gammell:** That's the idea. So like think about how much vertical height control you need to have to just get that layer off, you know?

**Dave Jones:** Ooh. Yeah. No, it's very impressive.

**Chris Gammell:** Go back through the tweets. It's very impressive work. Right. So like if nothing more than just as an exercise in making... Oh, yeah. No, of course. ...beautiful PCBs.

**Dave Jones:** It's maybe not a practical solution. No.

**Chris Gammell:** I mean like milling in general is like, you know, but if you're going to use this process, like, yeah, I mean applying solder mask is awesome, right? That's usually one, you know, aside from just the size constraints of, you know, milling. If you get a good mill, usually the solder mask is kind of the next thing that you want to have some kind of insulation between your part and your board. So it's great.

**Dave Jones:** Yeah. And I guess it makes sense. If you're a million person, you've already milled out your PCB. You don't want to get the chemicals out and do your photo imageable solder mask, right? That's just kind of defeating the purpose. So you want to mill that too.

**Chris Gammell:** Yeah, that's right. I guess.

**Dave Jones:** Otherwise, you'd photo etch your boards as well. You wouldn't mill them. You'd photo etch them.

**Chris Gammell:** Right, right. Exactly.

**Dave Jones:** So, cool. You don't... It's got to be taking some of the extra copper off, surely.

**Chris Gammell:** Oh, probably. Yeah. Yeah.

**Dave Jones:** Yeah, but who cares, right? As long as it doesn't eat through at all. Yep, exactly. Yeah, the tolerance, you know, because the one ounce copper is how many microns? It's like five microns or something.

**Chris Gammell:** No, more than five microns?

**Dave Jones:** Sorry, 50 microns.

**Chris Gammell:** Is it that low?

**Dave Jones:** 50 microns or something. Yeah.

**Chris Gammell:** It had 50 mil? You sure?

**Dave Jones:** Yeah. One...

**Chris Gammell:** That doesn't sound right. Micron's pretty small, Dave.

**Dave Jones:** What are we... Hang on. 35 micron. One ounce copper is 35 microns. Really? 1.4 mils. Yes. 35 microns of copper.

**Chris Gammell:** Wow. Okay.

**Dave Jones:** Yeah. It's not much. So if you take off, you know, you have to like not take off more than a few tens of microns.

**Chris Gammell:** Wow. Yeah, that's pretty down there.

**Dave Jones:** That's how precise it's got to be.

**Chris Gammell:** Yeah. Unless you've got a thicker... I mean, maybe there's thicker boards too, so...

**Dave Jones:** Well, you can get two ounce copper. Woo-hoo. You go up to 70 microns. Yeah. You know, you're still down in the sub-100 micron region.

**Chris Gammell:** Yeah. That's crazy.

**Dave Jones:** Imagine like just the flat... You would need your bed to be that flat. Yeah. You'd need your bed to be flat within tens of microns.

**Chris Gammell:** Yeah. Oh, yeah. I mean, like I have no doubt this is very dialed in.

**Dave Jones:** Wow. Oh, no wonder nobody's... Probably nobody's done this before because they just go, well, my bed's got to be flat within 10 microns. Bugger that.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** You know, like... Yeah. That's just... It's just pointless. Even to try it. But, you know, hey, hats off, right? They did it. Okay? Yeah. Wow. Oh, dearie. All right. Groovy. Anything else?

**Chris Gammell:** No, that's all for me, man. I'm back to making sure I don't explode batteries on the bench, so...

**Dave Jones:** Use the protection circuit. Yeah. Unbelievable. All right, man. Talk to you soon. Catch you next time. Bye.

**Speaker ?:** We'll be right back.
