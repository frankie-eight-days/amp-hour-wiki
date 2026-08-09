---
episode: 589
title: Mute Button Discipline
url: https://theamphour.com/589-mute-button-discipline/
---

**LTSpice:** This is The Amp Hour Podcast. Release May 15th, 2022. Episode 589. Mute button discipline.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Camel of Contextual Electronics. We're fighting to see who can maintain their ability not to cough for this entire episode.

**LTSpice:** Yeah, discipline. Mute button discipline.

**Dave Jones:** Mute button discipline. Okay, it's the new terminology. It's the name of the game. All right.

**LTSpice:** Yeah. Yep. Both of us are maybe a little under the weather.

**Dave Jones:** We are both recovering, so yeah. Yeah. Oh boy, this will be good.

**LTSpice:** Yeah. Yeah. Well, all right. I've got a lot more of this ahead of me. Yeah. Little kid in the house. A lot of snot. Yep. A lot of things being transferred to the parents.

**Dave Jones:** Dragging in from the real world. Sorry. Yep. They're a germ factory.

**LTSpice:** Mm-hmm. Yeah.

**Dave Jones:** One of the things we could embarrass ourselves over.

**LTSpice:** Let's start there. Yeah.

**Dave Jones:** Not knowing about beta. Beta. Yeah, that's right. However you want to pronounce it.

**LTSpice:** So before the show, I sent Dave a link and I was like, Dave, make sure I just don't have any clue what I'm talking about here. And we're like going through this thing. And so it's the false death simulator, which you've used before, right?

**Dave Jones:** I've used rarely. Yeah. Yeah. Yeah. Yeah. It's one of those online ones. And I think it was the first one to do the graphical flow where it actually shows you the physical electrons moving back and forth and all that sort of jazz. I think it was the pioneer in that, but please leave me in the comments. Yeah.

**LTSpice:** I mean, I love it for that. Just being able to see like some motion and like you can see when, you know, when a channel is opened up, especially for like dynamic circuits, it's really, really useful, you know? So when you could slow it down, speed it up, whatever, really, really quirky interface. But, you know, as a free resource, I mean, it's basically this and LTSpice and a couple, you know, a couple of other free ones. But I put this, I put this up there with LTSpice, you know, different flavor, right? I think probably a different.

**Dave Jones:** Oh, no, totally different.

**LTSpice:** Different level of probably. This might actually be less quirky than LTSpice. I'm not sure.

**Dave Jones:** Yeah, I know. They're all, they all have their individual.

**LTSpice:** Yeah. Things. But the accessibility can't be beat. I mean, like I sent Dave a link for this versus like a text. Yeah, yeah, exactly. So that. I know. Anyways, if anyone knows the false sad people or person, we'd love to talk to them. I tried reaching out once. I never, never got it through. So anyways, I was helping a student with a MOSFET circuit. There was a drop that neither I nor my student expected across a MOSFET, a P-channel MOSFET. And so tweaking all the different values and playing around with things. And I'm like, you know, this really just, this doesn't seem right. And so you click into the part, you see all these different things and, you know, the different dialogues that are there. And there's a variable in there called beta. So you double click on a P-channel MOSFET and you see beta. And I was like, I don't know what that is, but you just kind of assume it's right. You know, like at first at least. Right. And then I noticed that the beta is a link and it takes you to a calculator. And finally, when you go to the calculator says actually the default value is small, which is for a small signal MOSFET, but for a power MOSFET, which is what the case, you know, I was putting about an amp through this thing. So that's definitely MOSFET power territory. Use a larger value like 80, or you can go and calculate your own. And so before the show, I was like, Dave, is this a value I should know? Because I know beta for a bipolar transistor, but like a MOSFET, I don't know, like what the hell is this? Am I just completely messing this part of the textbook or like what's going on?

**Dave Jones:** No, I was of the same opinion that no, beta is a function of bipolar transistors. In fact, its definition is current gain, right? It is the thing. I mean, that is the difference between MOSFETs, FETs, field effect transistors and bipolar junction transistors, BJTs. One is current. I know there's a lot of fanboys who will rip us a new one for this, right? But BJTs are current driven devices and MOSFETs are voltage driven devices. Now, I know all the physicists are going wild and, you know, it's all fields, Dave. Right. Yeah. Yeah. It's all fields.

**LTSpice:** We'll get to that later. We'll get to that later. Yeah. Yes, we will.

**Dave Jones:** There's a segue there.

**LTSpice:** Yeah.

**Dave Jones:** But yeah, no, beta is not a standard parameter of a MOSFET.

**LTSpice:** I think more to the point, actually, for the bipolar thing, even if, you know, however you want to think about it, you know, if you start from voltage, you start from current. I think that as a mental model, many people start, I know, at least I did. I started thinking about transistors as voltage controlled devices, BJTs as voltage controlled devices. And I think that's way too confusing. And starting to view the world from the current perspective is very, very helpful in that way.

**Dave Jones:** Yep. I totally agree.

**LTSpice:** But in a MOSFET, you know, all that current goes slamming right into that one half of the capacitor, you know, at least in my mental model. And it doesn't flow anywhere. So yeah, beta doesn't make any sense here. So we were like, oh, what the hell is this thing? And so, you know, searching around online, you just type in MOSFET and beta, and the first link that comes up is false dead. So it's like, okay, well, maybe a little circular there. It seems like it's a kind of like coefficient built on top of transconductance, but it's not called transconductance.

**Dave Jones:** But yeah, we like we're little, we've spent like less than five minutes on this. Yeah.

**LTSpice:** So it's like, we have not comprehensively researched this topic.

**Dave Jones:** But yeah, for some reason, they use it in their simulator. It's like, it is the major parameter. There is VGS, isn't it? There's VGS and there's beta. And that's it. They're the two settings you can change for the MOSFET.

**LTSpice:** Yeah. I think you set the threshold as well, right? So you would.

**Dave Jones:** That's what I'm talking about. The VGS. Yeah.

**LTSpice:** But I think, I think the reason they say VGS is they want the threshold to be different than what the gate is actually spec'd at, because usually an RDS on is at some voltage, right? So it might be at 10 volts if it's an N channel FET or minus 10 if it's P channel. And so like, you'd have a different current at that, that what your RDS on is at. So yeah, it seems like kind of like a back calculation of that.

**Dave Jones:** See, it doesn't even give you a value for the RDS on. Whereas, you know, if you open something like LTSpice, right? It gives you your VDS, your RDS on and your gate charge, right? They're the three major parameters you can set for your MOSFET. And I'm just amazed at how different they are.

**LTSpice:** Yeah. I feel like it's tricky for young players, young and old, because sometimes in like LTSpice, one of the things that I like about it, but also I hate about it is that you can go and pick an actual part number, right? Yes. And so if you have your actual part there, it's freaking fantastic. It's like, oh, great. It's already been modeled for me. I'm good to go. It's got like, you know, there's more, you know, if you look at the model, like a model of a FET, there's like a dot model, and then they actually have different parameters they can put in there. You can go as deep as you want.

**Dave Jones:** Yeah.

**LTSpice:** Yeah, exactly. Right. They can, they can basically tweak the curves to look exactly like the curves would look like on a FET, on your specific FET even, which is awesome. Now it's like, all right, now we're zooming back and saying, well, what's the rough curve here, you know, and, and then back calculating. So that's what I assume beta is, is some curve definition that they're using. But at the end of the day, it doesn't really matter for what I'm doing. It's basically like, oh, it's slammed all the way on.

**Dave Jones:** Is there current there? What's your RDS on?

**LTSpice:** It's not. Yeah, exactly.

**Dave Jones:** You aren't simulating the, uh, THD of some high end audio MOSFET amp, you know, with your Falstead simulator, you know?

**LTSpice:** Yeah. I probably wouldn't, I wouldn't recommend that. That's probably not, uh, not the program for you. Yeah. There's so many other weird quirks about it too. Like, so it's JavaScript based. So like, you know, that's, that's the best part. It's in the browser and stuff like that. And there's other JavaScript based ones out there that are built on top of, you know, there's probably some spice engine underneath ng spice or whatever, uh, p spice. But the quirks are just like, man, I, I look for like an half hour, be like, how do I rotate apart?

**Dave Jones:** Hmm.

**LTSpice:** Yeah. The way you rotate apart is you redraw. So if you want to, so if you hit, if you're in the, if you're in the simulator right now and you hit uppercase N, which should draw an N channel MOSFET and you click and drag, you can drag it in 90 degree directions. That's the only way I found that you can rotate this thing. So it'll like pivot around a center point, but that's the only way you could do it. And then it's like, okay, well, what if, what if the drain and source aren't in the right orientation while you place it in the direction you want, you double click on the part, you say swap drain and source. So it flips 180 degrees. And so it's just like, all right, well, I'm, I'm playing in Mr. Falstead's world, Dr. Falstead, I should assume, uh, Dr. Falstead, I presume.

**Dave Jones:** Uh, I did find a reference to beta in spice in LT spice models to do with N channel J Fets and also MESFETs. MESFETs. So I, I, yeah, I, I just, I don't know.

**LTSpice:** Which is quite a MESFET, isn't it?

**Dave Jones:** There you go. Send a little link. It's like, yeah, I, I just don't know. I don't, you know, spice. Yeah. Uh, Nomenclature. Nomenclature. I can never say that word.

**LTSpice:** Yeah.

**Dave Jones:** Yes. Spice parameters. Yeah.

**LTSpice:** You know, so then like I click on a page. So actually I just analog.io is like a newsletter that's out there and they posted a link to like this 1990s, like reference of like, it was like a professor's notes and, and a textbook basically. And it was like available online. And it was like this unsecured HTTP site with just like a bunch of like word documents. I'm like, this is a pile of viruses waiting to happen. And yet I want the knowledge in here. And, uh, you know, like, I don't know, like you, you see all this stuff online too. And it's just like, Oh, I hope this is right. I hope there's no malicious people that like making, uh, like making nonsense, uh, uh, equations in whatever the hell that, uh, equation language is. LaTeX.

**Dave Jones:** Oh, right. Yes. The, uh, yes. It's like, that's the online, uh, that they use on forums and all sorts of stuff. Yeah. It's like the markdown language to make, uh, make big square roots and stuff like that.

**LTSpice:** Yeah. Yeah.

**Dave Jones:** Fancy, fancy. Yeah.

**LTSpice:** Yeah. I think the only thing that saves us is like, who, who would do that? That's, that's insane.

**Dave Jones:** It's going to be a great troll if somebody does, you know, if you're like, you know, you can, you can pretty much like own the Google search terms for a certain weird thing, you know, it, it wouldn't be that hard.

**LTSpice:** That's some, some deep troll. That's some deep troll right there. Yeah. Oh man. What? Why? Why? Just imagine you're like, you're closing the book at 6am ready before your, your, your, uh, your final exam for an electronics class. And you're like, you get to the bottom and it's like, none of this was real. Devious. Devious. Devious.

**Dave Jones:** Well, you want to know what else that may or may not be real.

**LTSpice:** What's that? Is it feel, is it fields? Fields. Current flowing. Sorry. But energy, energy flow inside or outside of a wire. Dave, you got a huge shout out. I have to say. I got a little one. I mean, you were on screen on a Veritasium video.

**Dave Jones:** Actually, there is an hour's worth of footage of, of us two talking about this.

**LTSpice:** You and Derek. Yes. Me and Derek.

**Dave Jones:** Yes. Yeah. Cool. For those who don't know, he was actually planning this video before Christmas time. That's when I met with him. I think I was the last one that he contacted just before he was going to release the video at Christmas time. And for those who don't know what we're talking about, we're talking about the follow, he's finally done a follow-up video to the infamous, you know, transmission line to the moon switch light bulb thing.

**LTSpice:** How fast does the, does the light bulb turn on? Yeah.

**Dave Jones:** We've talked about this previously, I'm sure.

**LTSpice:** That's right. Yep.

**Dave Jones:** So yeah, he finally done a follow-up video, but yeah, he actually was going to release this before Christmas time. And he frantically called me up just before Christmas. I think it was Christmas Eve or something. I'm not sure. Oh, wow. And, and he going like, I'm, I'm going to release this video. I'm not sure if I'm going to release this video. I'm not sure. You know, like he, he genuinely was, sorry.

**LTSpice:** Is that, that's when it came out as the original?

**Dave Jones:** No, no, no, no, no. The original came out. I don't know. Early December. Maybe. I can't actually remember.

**LTSpice:** Huh?

**Dave Jones:** It's been a while now.

**LTSpice:** Okay. Oh, so you're saying, so the original came out in December, then he called you towards the end of December after he talked to a bunch of people, then he was going to post this most recent video, which is Derek talking about or doing an experiment where they actually do a transmission line. They measure the responses. They do some simulations. Great. I thought it was a great follow-up.

**Dave Jones:** Oh, it was excellent. It was very, it was very well done.

**LTSpice:** It helped me understand it actually a lot better that I don't remember the YouTuber who did a simulation, but that was really, it was like a field simulation. That was really cool.

**Dave Jones:** Yes. It's great. Yeah. That was Alpha Phoenix, which is another, another YouTuber. Anyway, it was released on November 20, November 20. So geez, you know, that's a while ago now. And he only just got around.

**LTSpice:** Uh-huh. Dave missed his cough button.

**Dave Jones:** I did. I did. Sorry. I lose. Hang on.

**LTSpice:** Yep. Yep. Wah, wah, wah. All right. I'm good to go again. Good to go. To be fair. He was, you know, he was talking a lot there. To be fair. Dave talks a lot.

**Dave Jones:** Anyway, where was I? Yes. Yes. He practically called me up because he was so worried that he wouldn't like, you know, make everyone happy because he, he generally wanted to explain it the way he originally, you know, he wanted to, like he was, you know, he discovered point. We didn't just discover, but you know, he, he wanted to share pointing's theorem if the world and everything.

**LTSpice:** Right. Right. That was the, that was the basis of it. It was like, look at this cool thing.

**Dave Jones:** And that was the basis of it. Energy flows in fields. Right. And, and it's like, yeah, of course it does. Yes. Right. Everyone learns this. And people thought, including myself, I thought maybe he's trolling with the moon question. Right. Because yeah, maybe he's trolling us engineers, but I'm absolutely confident now after talking to him about it, that no, it was, it was just like, he just wanted some example that would look good and, you know, to Joe average on screen. Right. And, and he didn't give any thought to how it would rile up all the engineers and cause this great controversy, you know, because a point in theorem is not controversial. Right. Energy flows in the fields. Right. And it's, it's just like bread and butter kind of stuff, even though us engineers tend to ignore it most of the time. Right. In fact.

**LTSpice:** Up until, up until you get a board back from the board house and you're like. Yeah. And it's.

**Speaker ?:** Yeah.

**LTSpice:** This, this, this controlled impedance line is not doing great. This just failed emissions testing. All right.

**Dave Jones:** Oops. And as I said in my video, even Feynman himself, right. Went, well, you don't really have to concern yourself with the detail of whether or not the energy actually flows in the field or not. It's, it's pretty academic. Right. It doesn't, it doesn't really matter that much. Right. That was basically paraphrasing Feynman himself. I mean. It's all, it's all mental models, right? Yeah. Yeah, exactly. It's turtles all the way down. So, yep. And so, so I thought he was not ever going to do the video because I thought, you know, look, it's, it's April now or whatever. And well, that's May now, but it was the end of April. And I thought, ah, no, I think he's abandoned the video. Cause he said, you know, he said to me, I think I might scrap this, you know, I thought like, cause I've done all the measurements. I shot all the footage. I built the thing, went to a lot of time and effort to build the whole, you know, he built it on poles, you know, giant poles. You had to construct these poles and paid a lot of money for the copper pipes and everything.

**LTSpice:** Did he do this? It looks like Stanford. Is he at Stanford? Yes.

**Dave Jones:** Yes. Yes. He's there where he's, he basically isn't there anymore. I'm not sure if that's. Yeah. But anyway, yeah, he's not there anymore. And that's it. So he got all this footage. He measured it all. He got, you know, his a hundred thousand dollar scope up, up the top of the ladder. Oh my God. That was the worst part of that video where I was like, oh God. It was very triggering. I'm here already. Yeah. Nice one. Anyway, I thought he wasn't going to release the video, but sure enough he did. And it's an excellent video, but it does not stop the people arguing. In fact, it's been hilarious to watch the EV blog forum over all this time over the last like five months or so. Right. Back when his first video was released, there's like an 80 page forum thread on this. And if you dared to even hint at maybe suggesting that energy might flow. Within a wire. Right. You were hounded down by the pointing fanboys. Right. You were absolutely pounded into submission by the pointing fanboys. It was hilarious.

**LTSpice:** Pointing fingers. They weren't afraid to point fingers.

**Dave Jones:** What?

**LTSpice:** Pointing fingers.

**Dave Jones:** Ah, point. Oh, God. Pointing. Pointing. Yeah.

**LTSpice:** Okay. Yeah.

**Dave Jones:** Whoosh.

**LTSpice:** Yeah.

**Dave Jones:** Yep. And it was absolutely hilarious. And now it's basically flipped. Now there's a second thread, of course, for his new video. But also the old thread was basically overtaken by a bunch of people. Like, you know, like a handful, less than a handful of people who basically know it's wrong. Pointing is wrong. Energy flows in the wire. And it's been almost complete. It's flipped itself on its head. And it's been overtaken by these people who swear.

**LTSpice:** You know, a hundred years ago, you had to mail papers with evidence and all this stuff back and forth and in journals. And now you can just get on a forum and shout and shout and shout and shout. Yep. Isn't the internet wonderful?

**Dave Jones:** It's great. I think the pointed fanboys have given up. Trying to, you know, go blue in the face to try. Anyway, so it seems like the, yep, the energy in the wire fanboys have won on the EEV blog forum. It's hilarious to watch. Yeah.

**LTSpice:** Well, other things, I mean, so, yeah, I think it's definitely worth watching. Other thing he points out in the video is, which I'm not sure how much we've talked about on this show before, but Rick Hartley's videos. People haven't watched, you know, if you're doing anything like EMI, Rick Hartley is like the go-to. There's a bunch of like his Altium talks. Altium posted those online.

**Dave Jones:** He was on that. Definitely worth watching.

**LTSpice:** Yeah.

**Dave Jones:** Yeah. I don't think, though, I don't think that was, I thought that was one of the lower points of the video. Like, I'm a big Rick Hartley fanboy, right? So don't get me wrong. It was great to have him in there. But I think.

**LTSpice:** He thought he didn't make a good point with it?

**Dave Jones:** I think he didn't make a good point with it. Because if you actually listen to him and watch his slides, he's talking about high frequency transmission line AC stuff, right? Whereas for me, the fundamental question still remains. And I still want it answered. And I'm still not 100% convinced, right? Even though I know the point, the pointing and the Maxwell's equations and the math works out for both DC and AC. But my question is still this. I still have doubt in my mind that at DC. DC is a lie, Dave. Pure steady state DC taking all, no switch bullshit, no nothing. DC is a lie. Right? It's a mental model. DC is a mental model. It's a lie. It's a mental model.

**LTSpice:** There's a T-shirt in there somewhere. I don't know.

**Dave Jones:** Right. There has to be. Yeah. It's like, what happens at DC? Like, if you've got like 100mm diameter bit of copper, right? Cable. 100mm diameter. And you're passing 1mA through it to a load. Steady state. Are you telling me that 0%, absolutely 0% of the energy flows within that copper wire? Yeah. It just does, like, giving that mental model in my head. And I put this on the forum and nobody wanted to deal with it.

**LTSpice:** Yeah. Yeah. That's outside the experiment that he talks about, too. I think that's the important piece.

**Dave Jones:** Oh, yeah. No, no, no. Totally. His experiment is all about transients. Right? And totally. And that's why there's half a dozen different ways to analyze transient circuits like that. And that's why I did my video with, look, here's how a regular electronics engineer who doesn't give a toss about pointing would analyze this. And it's the cable capacitance. And it's basically he admitted in the video that, yes, he actually showed the exact model I did and the lumped element model.

**LTSpice:** Yeah. Yeah.

**Dave Jones:** And how, yeah, this is another way to analyze it. And sure enough, you know, yeah.

**LTSpice:** And it all works and it's all hunky-dory. It does make you wonder, so if we didn't have the lumped element model, how would our jobs be a lot tougher?

**Dave Jones:** Oh, I'm sure we wouldn't have gotten to the moon, you know, if we had to solve, if we had to solve Maxwell's equations every time we wanted to power our lead or something, you know. What's the vector?

**LTSpice:** What's the vector, Victor?

**Dave Jones:** And then, and then on top of that, you've got quantum mechanics. Yeah. Right? You've, you've, you've got quantum field theory, which was what Feynman won his Nobel prize for basically.

**LTSpice:** Yeah.

**Dave Jones:** And he, he wrote the book on it and what, what, what that actually means. And if, if I bring that up on the forum, nobody wants to deal with it. Right. Cause that's, that's outside everybody's wheelhouse. Right. And I, I, I just don't know, but I, I, you know, I mean, it's electronics forum.

**LTSpice:** You go to a physics forum, maybe you'll get some, some takers.

**Dave Jones:** Yeah, probably. But anyway, I'm so, I am actually still on the fence at DC.

**LTSpice:** Okay.

**Dave Jones:** I, I, I have an open mind. I know the math works out. I know the point. I do not debate at all that the maths works out for Maxwell's and pointings at both AC and DC and that you can analyze it using energy flowing in the field at DC. I have no doubt it works out, but I'm just saying there might be something that trumps that in the future. And I can't rule that out.

**LTSpice:** Yeah.

**Dave Jones:** There's a niggling feeling in the back of my mind. And it's just easier. Like a DC who the hell wants to deal with Maxwell's and pointings at DC for goodness sake.

**LTSpice:** Yeah.

**Dave Jones:** Get a grip.

**LTSpice:** Sometimes it trips me out that like a resistor, the resistance is just like a, it's just like a made up ratio, man.

**Dave Jones:** It's all meta, man.

**LTSpice:** We should just, just like all get along with components.

**Dave Jones:** I, I, I have a feeling that we're not sufficiently under the influence of enough drugs to, to truly understand it.

**LTSpice:** Take some cold medicine.

**Dave Jones:** Just like, yeah, I think we need some. Yeah. I think we need some good stuff. Yeah. Pointing. I think they had it right in the sixties, you know. Yeah. You can just picture firemen tripping some acid, you know. Yeah. Seriously.

**LTSpice:** Yeah. Get some bongos out.

**Dave Jones:** Yep. Yeah, yeah, exactly. Yeah.

**LTSpice:** What if we like, what if we pick some locks and we just like chilled out and put some bongos, you know.

**Dave Jones:** Drove a hippie van coast to coast and just, yep. Yep. I'm sure we'd figure it all out. Oh boy. Oh, that's hilarious. Anyway, it was an excellent video by Derek. I thought it was very well done.

**LTSpice:** Yes.

**Dave Jones:** Yep. End of story, I guess. No, it's not.

**LTSpice:** Speaking of EMI experts, we have a, another link on our forum about past guests, Eric Boagatins. He did a recent thing about circuit design or circuit design rules and stuff like that. You know, the usual Eric stuff that I keep watching because it's always good.

**Dave Jones:** I'm sure he's another energy in the field fanboy.

**LTSpice:** Oh, interesting. Yeah. Maybe we should do a little round table.

**Dave Jones:** Guaranteed he is. Him and Rick. Yep. Have to be. Duke it out. That's his, like his business is freaking transmission lines. Cash money. Right? Yeah. Yeah. Yep.

**LTSpice:** But DC. Sorry. So, you know, I've been doing this simulation and then other times I've been, I've been in the code realm, Dave, and it's scary. Come back to the hardware, my, my son. Yeah. You know, it's, it's nice. I'm, you know, I've been learning a lot and that's been one of the most exciting things about my, my new gig. But one thing that like I had been coasting on for a long time is that I, I didn't have any like debugging capabilities in like an, in a real-time operating system. It was kind of just like, well, everything's probably going okay because I can, you know, I see a print message and it's probably connecting the internet and oh yeah, there's an, you know, connecting the internet. That's good. But I didn't really like figure that out, but I finally, I finally figured it out and that was, that was very good. That's a good, it's a critical step to any coding journey, which is getting the debugger, step debugging working. Cause yeah.

**Dave Jones:** Cool bananas. I, I still have no idea about anything at all, unless it's C on a microcontroller, C or assemble on a microcontroller.

**LTSpice:** This is C on a microcontroller actually. If you didn't, if you didn't know that.

**Dave Jones:** When, yeah. Yeah. Okay. But when it starts involving anything like web enabled is what I'm talking about. Yeah.

**LTSpice:** Yeah. Yeah.

**Dave Jones:** Yeah.

**LTSpice:** I just, I, I have no idea what I think that's the hard part of all this stuff is like, okay, so now you've got like all of these competing interests, you know? So like, and if you think about like how the computers that we're talking on right now, right there at the end of the day, they have, they have a core multiple cores. Right. But you know, it's still scheduling and operating system is like scheduling tasks and, and, and interrupting based on inputs. If you have hardware interrupts and stuff like that, it's all the same thing when you shrink it down to a microcontroller too. It's just, usually you don't have the same like memory management module. That's like the big definitive difference between like a Linux system and a embedded system. I feel like I should edit myself there because I I'm not defining an embedded system. If you listen to the embedded podcast, they, they always, that, that is a hot, hot button issue. But anyways, so I'm working on tiny, tiny systems, microcontrollers that are talking the internet and most of the stuff running on this thing, I haven't written any of the code and I don't really know what's happening. And so debugging will be helpful only because I'll be able to like figure out where things are breaking and like usually within the stuff that I've written. That's like the important part, but.

**Dave Jones:** That's the only way I learn this stuff. Yeah. Like I can get a microcontroller to talk to wifi and the internet and stuff like that. Right. I can get it to talk to a YouTube API and, you know, get a value back and, you know, stuff like that. But I've got it. Like, I can't write the code from scratch. I've got to take somebody else's code and put it in there and then hack it for my purpose. That's the only way I can learn how to do that sort of stuff.

**LTSpice:** I mean, I think sometimes it would be irresponsible to start from scratch, right? Like if you started from scratch today and you're like, all right, well, I have an Espressif chip. I want to write my own wifi driver. You're right. And like do everything with the ground up. That's kind of irresponsible because one, if you're working for a client, you're going to like charge way more money than they should have to pay. Okay. And two, even if you were given that permission and you get to the finish line, you say, all right, now I've have my very own bespoke wifi driver. And there's no, and assuming there's no other reason, like there's no other requirement, like you needed to do something that the other stuff can't. And you validated that you really, really, really can't do it with the existing off the shelf code. It's like, well, how secure is your new thing? Because now you've just potentially created a very insecure, you know, unless you know what you're doing, you've spent all this time and made this thing that might just be not that useful and you have to maintain it over time. So, you know, it becomes kind of a maintenance neighbor too.

**Dave Jones:** That's what happened with the 121 Holdymeter app. Right. We basically started from scratch. We were all, how hard could it be? And we just both went, oh, it can't be that hard. Right. You know, and no, like 12 months later, like it's just, no, we should have just, you know, yeah, no, no, we should have just given it to somebody who, who knew how to do it from, you know, who's done it, you know, a hundred times already. And it's gone through that pain to like learn it all and stuff. And it was, it was just a horrible process. So yeah, it really sucks.

**LTSpice:** Yeah. It's tough. Bad choice. Yeah. And so the thing that, the thing that I was actually, I was extra excited about is, so we had Brian Amos on the show and he wrote the FreeRTOS book. That was like a couple of months ago. Really great book. Great way to learn about real-time operating systems using FreeRTOS, but like a lot of it's applicable to other, I think, real-time operating systems. If you're kind of doing more complex microcontroller designs and you're getting into the point where you're like, okay, I probably need more than just a state machine and stuff like that. Or if you're connecting the internet really at all, I think you almost certainly need a real-time operating system just to handle some of the timing and stuff. But one thing he talks about in the book that I hadn't gotten working with his book was System View, which is a SEGGER tool. And basically what it does is it listens to the debugger. Like, so as the debugger is like spitting back all of the trace stuff, it basically takes that and it's got some hooks in there that says, oh, I know where you are in your program. And your device just went into idle mode. And now it came out of idle mode and now it's running task A and here's your memory space. And like, you basically like, you almost, it's almost like a power analyzer. Like, and you could probably, you could sync it up to a power analyzer as well because, you know, if you're running like a encryption engine, it's going to have a bunch of, it's going to use a lot more power on that. Right. And so that, that should correlate as well. But even if you're just not sleeping, you're going to be using a lot more power because you're, you're using more cycles on the, on the microcontroller core. Yeah. Yeah. And you can just like kind of map this whole thing out and get an idea of like where your device is spending its time and how it's switching between tasks and stuff like that. And it's, it's really cool. I mean, it's just like, yeah, it's not the only tool out there. Of course there's other ones. Yep. But yeah. Cool stuff. Yeah. Okay. I have to put a plug in because I never understood as I was like, you know, moving into the microcontroller world. I didn't understand why debuggers were important. You know, that sounds stupid.

**Dave Jones:** Yeah. I know. No, I've never been at, I do self debugging with code. I just fill my code. Yeah. I mean like print off debugging is the thing, right? Yeah. Exactly.

**LTSpice:** But I didn't understand like the analysis piece of the, the piece of hardware, the debugger. Right. And like the fact that like the debugger is also, you know, it's also the programmer and like, okay, if you want to, you know, not use a bootloader on this thing, then you need to be able to like access the single wire debug or the J tag pins and stuff like that. Yep. I just really didn't have a good model. Like I kind of stumbled through it in my earlier days and I'm getting a better feel for it, but I will say I always went marveling at how expensive seggers are like segger J links rather. Oh yeah. Very. They're, they're really expensive. I paid, I think $600 for mine and it was like, you're using it. Like commercially your programming stuff, like you have to, you're supposed to pay that, right? Okay, fine. I did it. Yeah, of course. But then like all the other tools that around us, like now I'm like, oh yeah, I'm leaning into this stuff. Like, it's great. You know, go segger, go other debug tool vendors.

**Dave Jones:** Oh yeah. You can pay thousands and thousands of dollars.

**LTSpice:** Oh yeah.

**Dave Jones:** Oh yeah. Serious business. Yep. Yep. It's one of those things, if you need it, you really need it. You know, if your back's up against the wall and you know, yep. Yeah. It's the only thing that's going to really show what's going on.

**LTSpice:** Yeah, exactly. Exactly. And it's, and I think, you know, I probably, you know, I'm not going to be that person who's writing the wifi driver or the whatever driver that's out there probably. So I'm kind of on the edge of needing it, but like the people that are writing, writing the wifi driver and like interacting low level hardware, stuff like that, man, they, yeah, they really, they really lean into it. So.

**Dave Jones:** And then you can like integrate them all with logic analyzers. Like if you're at the, you know, if you're working at Intel developing CPUs and stuff, like the tools that they have are just absolutely mind blowing. Right.

**LTSpice:** Yeah. Yeah.

**Dave Jones:** It's just, yeah.

**LTSpice:** Yep. So yeah. So I'm learning a little bit at a time.

**Dave Jones:** Cool bananas. They're right. What else we got on today's list? What's been happening? What has been happening? Uh, got some people buying out some other people. Yawn. Yep. No one cares.

**LTSpice:** I was just going to say there's fewer, fewer vendors, fewer, fewer board makers is probably less good. Ultimately.

**Dave Jones:** Australia's expanded. We actually now have an extra board maker here. Woo. Yeah. I remember you saying that.

**Dave Jones:** Yeah. Yeah. Yeah. Although we did have a stealer from New Zealand, but you know, sucked in New Zealand, but you know.

**LTSpice:** Oceana region. It's fine. Yep.

**Dave Jones:** So technically we didn't actually gain. It's still in the region. It just moved from Auckland to Melbourne. Top the gap. Oh God. Imagine transporting all that crap. Imagine transporting like a wet, bloody acid production line.

**LTSpice:** We really should have taken the, uh, Cooper chloride out of this, uh, this container.

**Dave Jones:** Oh God. Picture a regular lab move. God. You know, this is like, oh, all these hideous bloody, you know, have you seen these machines? Oh God.

**LTSpice:** They're just, I mean, they're just like big tanks, right?

**Dave Jones:** They're just giant tanks and shit splashes everywhere. And everything's got a, you know, rusty, corroded tinge to it. And, you know, it's just awful. You know, copper plated to the legs of the machines. It's just awful stuff. It really is. Oh God.

**LTSpice:** Yep. Well, speaking of, uh, moving shops, you're, you're buying out, uh, you're buying out a, uh, shop recently, right?

**Dave Jones:** Oh, right. Oh, yes. I'm going to pick it up. Well, maybe today we'll see. Yes. I got a whole bunch of, I got a whole bunch of auction. I'm going to become, I'm going into the optometry business. I couldn't resist. There was this auction and obviously it was one of these scientific warehouses, you know, scientific surplus warehouses, you know, specialize in, you know, buying and selling scientific surplus gear. So if you need a, you know, a thermal incubator or you need a, you know, an analyzer, some chemical analyzer or something, they'll have one in stock, probably some used instrument, which they got from, you know, the last company that shut, the last scientific company that shut down, which bought it from them. And it's probably cycled through their hands like five times as these, you know, medical companies, you know, close up shop and sell off all this surplus gear and everything else. So anyway, one of these dealers, so they have occasionally like they have a mass clear out thing on an auction.

**LTSpice:** Yep. Yep.

**Dave Jones:** I just happened to notice. Hang on. I might, I might be able to get the, I might be able to get the names of the instruments. I cannot pronounce them.

**LTSpice:** Yeah. And I mean, so in optometrist, I think about like the little flip, you know. Yeah. No, not the flippy thing.

**Dave Jones:** We're talking about the new 3D eyeball scanning. Yeah.

**LTSpice:** Okay. Camera re made by a Zeiss. Got it. So you're going to be able to use this as like quasi inspection equipment almost.

**Dave Jones:** Yes. And made by Zeiss. Right. Zeiss. Zeiss. I think I'm pronouncing Zeiss correctly. I don't know. Yeah.

**LTSpice:** I think that's right. Yeah. Yeah. Like the, the Swiss lens maker.

**Dave Jones:** Yep. Anyway, so I have an anterior segment imaging system. Okay. It's anterior. I have a natural vision, natural vision auto re ref ker automata. A ref ker automata. R E F K E R A T O M E T E R. Pronounce that one. Yep. A ref ker automata. I have a matrix field, a matrix visual field analyzer. And I have a PECO emulsifier, which actually is not part of the opto. Well, it is part of the optometry thing. It's part of the, it's a laser eye surgery controller, basically.

**LTSpice:** So I can send you like, you know, he's got folks is a lot more crap in the bunker. Got a lot of shit. All right. So, so walk me through this. So like, I, I was thinking about, you know, like the, the optic piece is cool. I mean, like, this is all going to be cool. Teared on stuff. If you end up tearing it down. Yep. But is that it? Is that all you were thinking? Is like, I don't know.

**Dave Jones:** I just wanted it because they were going for a song and I don't, and I feel too good to

**LTSpice:** pass up.

**Dave Jones:** And I just recently had, I tweeted this, tweeted a fair bit about it. And I was actually going, and I did a poll on this and I was actually going to contact. I had a complete 3d eyeball scanning session thing that went for like two hours and you know, I have my eyeballs scanned.

**LTSpice:** Are you sure they're not going to use it like in sneakers or equivalent, like to log in to some facility?

**Dave Jones:** I cannot be sure that Uncle Sam doesn't have it. So yeah. Yeah. That's right.

**LTSpice:** Just immediately updates. Just goes to a. Yep.

**Dave Jones:** Straight into the bunker under the NSA somewhere. Yeah. Now my eyeballs scanned. Great. Yeah. And I just, I just thought these machines were great. You know, I went to, cause the last time I went to the optometrist, yeah, it was just the eye flippy thing. Right. They just had like the lens flippy thing. They put it in front of you. Yeah. You're blind. Here's some glasses go away. You know, kind of thing. Right.

**LTSpice:** Yeah. Yeah.

**Dave Jones:** So no. So I thought, screw that. And my local optometrist shut down. So I had to find a new one. So I found a new one that has all these whiz bang 3d eyeball scanning machines. And I went, well, that's gotta be more better. So I went there and yeah, I was just absolutely amazed. And I thought about actually getting. Shooting a video with him. And he was, he wasn't against the idea that I'd go in there and he'd tell us all about his whiz bang machines and stuff. And then like a couple of months later, here they are popping up on not his machines, but like similar sort of machines from Zeiss optics and other, you know, major companies is popping up on this thing. And I had to have them. Had to have them. They're probably not that complicated. They're just, I'm sure like they're worth probably worth like a hundred thousand dollars. Right. If you had to go buy this Zeiss. Yeah. Like buying it new. Yeah. Yeah. If you had to buy it new. Right. And somebody comes to your thing, you know, a Zeiss man comes around and sets up your machine for you, you know, and for you a couple hundred thousand dollars. And yeah, I'm sure it's got, you know, like just fancy optics and cameras in it to take a photo of your eye, you know, and some sort of flash to light the back of your eyeball. And then, you know, it's all software after that. Right.

**LTSpice:** You know who gets sold some crazy stuff? Yeah. Dentists. Yeah. My good friend is an oral surgeon and he said he gets, he gets absolutely inundated with like salespeople like waiting in his. Yeah. Yeah. And because they're selling like really, really expensive high tech stuff because dentists have some of like the best 3D printers in the market and like oral surgeons. Like basically my buddy like will scan, not only scan your mouth, but he'll like, he'll make jigs for every part that he's like cutting out of your mouth. And so like everything's just like all set up and ready to go. It's wow. Yep. I won't let him show me photos cause I'm too squeamish, but like the stuff he talks about is insane. It's right. Yep. It is.

**Dave Jones:** I'm sure it's in this field as well. You get, if you're, if you're an optometrist, you get, you know, you know, phone calls and people knocking on your door and yeah. I mean, yeah, it's a super high margin equipment. I'm sure. Oh yeah. Oh, huge, huge. So yeah. So I, I don't even know if the teardowns will be that interesting or not.

**LTSpice:** Maybe you could just resell it. Who knows?

**Dave Jones:** I don't know. It actually remains to be seen. Maybe. Yeah. I don't know. Anyway, it'd be very cool if I can get the optometrist to agree to do a, you know, like a, yeah, please explain. Video. I think that'd be great. So anyway, yep. I'm going to go pick up these things and hopefully we'll have some fun. Awesome. That's great. Yep. That's great. I just had to have them. I mean, they just look so funky. They just look so good. Yeah. Yeah. You know, they just like, you know, like big chin rest where you put your chin and then this thing comes in front of your eyeball and it's like, you know, it's like, yeah, it's good stuff.

**LTSpice:** Yeah. It's funny too, because like you think about like the expectations around, you know, different types of equipment and like an optometrist or ophthalmologist is going to be like, well, every piece of equipment has a chin rest on it, you know, or an electrical engineer says, well, every scope has a, you know, probe input on it. You know, it's just like, oh yeah. It's like, we, we just are like completely indoctrinated with like the kind of the user experience of these different machines. Usability of, yeah. Exactly. Yeah. Yeah. So look for a scope input on these things.

**Dave Jones:** I've got something interesting next month that I'll be able to talk about next month in that regard.

**LTSpice:** Okay. Scope. Scope. Maybe.

**Dave Jones:** Can't say. Okay. Can't say. Can't say. All I can say is that there may or may not be a video already on my channel sitting there. Hmm. Hmm.

**LTSpice:** So all we have to do is. Guess. All you have to do is guess. Guess the link.

**Dave Jones:** Guess the link.

**LTSpice:** Guess the eight character hash at the end of. Hash thing or whatever it is. YouTube video. Yeah. Yeah. Yeah. Okay.

**Dave Jones:** Yeah. Anyway. Yes. We might have something interesting to talk about next month.

**LTSpice:** Okay. That's all I'm saying. Cool. Cool. Cool. Cool.

**Dave Jones:** Yep. What else?

**LTSpice:** So let's do a little update on bubble gum tap shoes. Do we have to? I mean, we should. Well, it's milk it.

**Dave Jones:** All right. Why is it milk it, boy?

**LTSpice:** Go. It's still terrible.

**Dave Jones:** Why is it still terrible?

**LTSpice:** I mean, you can't buy any parts. I mean, I don't know. I can. Everything. You can? I've been getting stock.

**Dave Jones:** In fact, I did just beat them off. I just had to beat them off. They were ready to deliver another 500 multimeters to me. And I go, whoa, hold on there. I just got 500. I just got 500 last month. You're trying to shove another 500 on me? What's going on?

**LTSpice:** Yeah.

**Dave Jones:** Well. So I tell them to hold off. So it's a problem for some people. Sorry.

**LTSpice:** Yeah. It is a problem for me. It's not letting up in that way. What can't you get? Top of the list. I'd say the most stressful part for me right now is a microcontroller. I think I mentioned before. Let me guess.

**Dave Jones:** It's an ST.

**LTSpice:** It's not an ST. It's out to March of 23. Which one is it? It's a little too long. What's that? Which one is it? Come on. Name and shame. It's a Silicon Labs part. It's, you know, one of many that are out. I don't see any coming back in, though, either.

**Dave Jones:** Is this a personal project? Work project? What is it?

**LTSpice:** This is a work project, yeah. But I saw, actually, there was an interesting question on Slack that I'm part of where they asked about, well, okay, say you're starting personal or professional right now. Where do you start? Like, so what micro do you go and grab? Assuming, you know, that you don't have, like, super crazy peripheral needs.

**Dave Jones:** Yeah.

**LTSpice:** Where do you go? You know? Like, do you start?

**Dave Jones:** Well, you can rule out ST, right? ST has got such a bad rep now due to the component shortage that there's almost no way you can start with them.

**LTSpice:** You know?

**Dave Jones:** Well, I don't know. I'd go back to, like, microchip. I'd go back to, like, old school microchip, maybe. TI? Like, you know, other, like, you know, TMS 430s? Are they a problem?

**LTSpice:** MSP 430s? Sorry.

**Dave Jones:** Yeah. MSP 430.

**LTSpice:** Yeah, I haven't used those in a while. I don't know. Like, 16-bit microcontroller. Yeah, I think some of it comes down to, like, what you need it for. So it's like, if you're just, like, flipping bits, you know, like, got a UART and you've got some LEDs. Like, yeah, that's probably, that's different than if you're talking over a satellite link or something like that, right? There's always going to be that, you know, it depends.

**Dave Jones:** But, yeah.

**LTSpice:** Even at the low end, I'm just not sure. Honestly, I think these days I would go onto, actually, I think I do have an answer for this. I think I would start with Espressif these days. I have seen they have been extremely available. And I would probably even pick a module over a chip, assuming I didn't have power needs.

**Dave Jones:** Yeah, but see, to me, that's not, that's not like a little jelly bean micro.

**LTSpice:** It's not. Oh, it's definitely not.

**Dave Jones:** No, right? That's what I think of when I think of micro. That's more modular application, webby level thing. Yeah, I mean, you know.

**LTSpice:** I mean, it's going to, yeah, and it does make sense if you're, I mean, so first off, it depends if you're battery powered. If you're battery powered and you're like, I need this to last for longer than a week, it's like, okay, well, probably you're not going to have a good time with Espressif. You know, like it's just, but in terms of sourcing, that's what I've seen has been pretty reliable just because I think they're so, the modules themselves are so spread throughout the, the kind of rest of the ecosystem that it's possible to get them. But, you know, it's still expensive. You know, it's not going to be like a dollar each unless you're going down to a chip, chip down solution. So, I don't know. Yeah, it's, it's a, yeah, it's a good question to have. I mean, like, I think at the end of the day, you know, you go search on a distributor site and buy as many as you think you're going to need and start there. But man, that's, that is risky. It's all risk, Dave.

**Dave Jones:** All risk.

**LTSpice:** Yeah. Oh.

**Dave Jones:** Oh boy, I'll pay that one. Okay. Yeah.

**LTSpice:** Yep. I, that wasn't intentional, but.

**Dave Jones:** All right. Can we have a chip of the weight, chip of the weight?

**LTSpice:** Sure. What do we got?

**Dave Jones:** It happens to be an ST, it has to be, it happens to be an ST micro. But I mentioned this one on Twitter. Well, somebody else mentioned this one on Twitter and there is a segue to this. It's the STM32F334. And I've sent you a link here. And it's actually kind of like a microcontroller specifically targeted at digital switch mode, power supplies, lighting systems, solar inverter systems, you know, like, you know, something that really needs fast, ultra fast analog to digital converter with low latency times. Things like, you know, a mains micro inverter that needs to track the mains, right? You've got to sample the mains and then track it and output and DACs and, you know, things to like, right? You've got to, you know, track and respond to things in real time. And that's what this microcontroller, it's got a high resolution timer in it, 217 puff seconds. None of that nanosecond rubbish. Puff second resolution, right? And which is also temperature and power supply drift compensated, by the way. And, you know, it's got an ultra fast 12 bit ADC in it, five meg samples per second. You know, it's got ultra fast comparators. It's got 10 PWM outputs and all sorts of things, right? So you can get, yeah, so you can get 217 picoseconds resolution in your variable duty cycle, variable frequency drives, right? It's just like, it's designed for, you know, measuring things and controlling things really fast, right? It's just a really cool chip. Anyway, so this comes about because on Twitter, this is from second order EDA. A, no, sorry, 2N order EDO, 2N order EDO. And I think he might be the designer of the open source solar microinverter project. Don't quote me on that, but he seems to be involved. And I think this might be the micro used in it because somebody was asking him on Twitter, why didn't they use like a new Raspberry Pi Pico microcontroller instead of this ARM STM thing? And he said, oh, no, I need the ARM STM thing because the high resolution timer in it to be able to do the tracking and stuff like that. Anyway, so that's another thing we have on the link today, which is the open source hardware grid microinverter thing, which is really cool.

**LTSpice:** And that's, so that's the basis of, of that is, this part is, is kind of integral to it.

**Dave Jones:** Yep. So I think it is tied to it or yes, it is. No, they use the STM 32G 474. I think anyway.

**LTSpice:** So the F3, I always hear about F1, F2, F4. I had not seen the F3 family. I assumed it was there, but, and, but looking for this part online as well. Are you seeing any stock? I see, I see no stock.

**Dave Jones:** Well, you probably can't get it. No, I'm not saying you can get it. No, I'm not, I'm not saying to use it. I'm just saying, I'm just, come on, it's just chip of the week. You don't have to be able to buy the chip of the week.

**LTSpice:** Chip of the 150 weeks ago. Right. Oh boy. Chip, chip of the 52 week lead time.

**Dave Jones:** Yep. Anyway, we will link to the EV blog forum thread through the open source hardware, software, grid, solar, microinverter, 450 watt jobby. Microinverter. Looks like he's put a lot of effort into it. And it looks like a really cool hardware built. Would you put this on your roof?

**LTSpice:** Uh, don't know. Yeah. I don't know. Probably not. I don't know when I would feel comfortable. You know, like you look at like, you know, you're getting an inverter, you're buying an off the shelf inverter. It's like, okay, there's probably some certification there. There's no guarantee that like, this is, you know, this could be just as good or better. Like, I don't know. No, it's a qualification. But like, where does that, where does that mental switch happen?

**Dave Jones:** You pay for the quality. Yeah, exactly. I, I probably would not use it on the roof. I probably would. Yeah.

**LTSpice:** But, but when would you then? Okay. So now this thing goes to market. This is just like the mental thing that I think about. It's like, okay, so I'm, this looks like a very well-designed product.

**Dave Jones:** It'd have to be a mass adoption thing and it'd have to be, look, oh, like everyone's using it. Yeah.

**LTSpice:** It's very chicken and egg in that way. Right. Right. Yeah.

**Dave Jones:** Yeah. Yeah. Yeah. Of course. Totally chicken. Yeah. Yep.

**LTSpice:** It's just tough to break into markets in that, in that way. I think.

**Dave Jones:** Because it has to be highly qualified. Like, you know, it's these sorts of things have to go through all sorts of qualifications to be able to. Yeah.

**LTSpice:** When we had Paul on, what was he saying? Is there like a governing board for this sort of thing? He mentioned inverters, but I don't remember. I don't know. What he said. Like if there's an ISO standard or something like that.

**Dave Jones:** I don't recall.

**LTSpice:** If people haven't listened to the Paul Zawada episode. Yep. It's fantastic. Talked about power. Yep. Dave and I were clueless. We're a little less clueless now.

**Dave Jones:** We'll have to get somebody from Enphase on. Because I've spoken to the Enphase guys. And they were kind of amicable to, you know, getting somebody on the show maybe. To talk about, you know, how these things. Yeah. But they were telling me about the extensive qualification testing. And just the amount of, you know, thermal testing that they do on these things. And life cycle testing. Yeah. And shock and vibration testing. Yeah.

**LTSpice:** But that's totally different than. Like the testing is very different than the market perception. Don't you think?

**Dave Jones:** Uh. But it's only us that cares. Like Joe Averitt. Like if you put this thing in a schmick box and fancy. And, you know. Yeah. That's what I mean. You could be a one man band and market the hell out of this. Right?

**LTSpice:** Maybe. Market is expensive, Dave. I don't know if you know this.

**Speaker ?:** Yeah.

**Dave Jones:** No. Well, no. It's not that expensive. You can do it. You just have to look professional. No. I'm going to stop.

**LTSpice:** I'm going to stop you right there. Marketing is very expensive.

**Dave Jones:** Not for a niche industry like this.

**LTSpice:** Yeah. All right. I guess we're just going to agree to disagree on this one.

**Dave Jones:** But. Well, I kind of liken it to my Zappi. I had not heard of the Inface before. I kind of like it. Like I installed my own Zappi controller. Right? For my car. Right? Right? It's my EV solar controller that actually tracks the solar and everything. Right? Oh, cool. All right. And I can tell. It's basically a bare PCB sitting in a fancy looking box. Right? And if it wasn't for the fancy looking box, I would not get the same vibe.

**LTSpice:** I mean, most products are just electronics sitting in a box. Yeah. Whoa. I know. Mind blown.

**Dave Jones:** Exactly. Right?

**LTSpice:** Zappi. Z-A-P-I.

**Dave Jones:** Z-A-P-P-I.

**LTSpice:** Zappi. Z-A-P-P-I. Is it a P-P-I? P-P-I. There's also a Z-A-P-I. Oh, it's a brushless motor controller. Holy crap. Oh, my God.

**Dave Jones:** It's Zappi, right? And likewise, there is...

**LTSpice:** Zappi. Wait a second. Inverter. Charger. I just want to make sure I have this in front of me. You know?

**Dave Jones:** Zappi, seven kilowatts. So you can see what you're looking at. That's good. Right?

**LTSpice:** Yeah.

**Dave Jones:** Right? It's a kind of funky molded, big molded case. Right? It's got an LCD and the cord wraps around the outside and everything's hunky-dory.

**LTSpice:** Oh, I see. The company is MyEnergy.

**Dave Jones:** MyEnergy. Exactly. Yes. Right? It's a UK company. And, you know, like only a small company. Right? They're not, you know, this is not a big mainstream thing. Right? This is a pretty niche kind of, you know, thing. Yeah, they sold thousands of them, but not millions. Right?

**LTSpice:** Oh, wow. What's... I know this doesn't actually matter for a product. But, like, if you go, like, halfway down the page... Yeah. ...they have a Tesla plugged into one. And it is the worst Photoshop of a cable I've ever seen.

**Dave Jones:** Really?

**LTSpice:** It's like... Oh, it's like... It's not even Photoshop. It's like an Inkscape. Yeah, it's like a render of, like, a cable. It's very fake. And then they put, like, a drop shadow going in the wrong direction.

**Dave Jones:** Oh, right. Yes. Yep. Yep. I see it. Yeah. It's pretty bad.

**LTSpice:** Yeah, yeah. But Dave still bought it. So, you know... Yep.

**Dave Jones:** Yep. I still bought it. Now, what is the difference between this and... There is an open source one. Sorry, I can't remember the name of it. But they're... No. The Open EVSE. Okay. So, if you search for Open EVSE, right?

**Speaker ?:** Okay.

**Dave Jones:** And I think you can even get it... Like, some people sell it as a kit in a box or even fully... No, I think you can buy it fully built, right? Mm-hmm. Okay. You can buy it fully built, right? And it's just, like... It's in, like, a see-through... It's got, like, an industrial see-through kind of case.

**LTSpice:** That's an off-the-shelf case, for sure. Yeah, that's the drilled-out, like, Hammond box or something.

**Dave Jones:** Yep. Exactly. It's one of these off-the-shelf industrial IP cases with the big cable grommets on the bottom, right? And, yeah, it just isn't... Is this better or worse than the Zappi? I don't know. I have no idea. I know. In fact, we'll just say they're absolutely equivalent, right? And they can be programmed to do a similar job, although the Zappi's a bit nicer in its usability, apparently, just from, like, firmware and an app point of view and stuff.

**Speaker ?:** I know.

**LTSpice:** This is just... But I think the key point for me here is just that this is where, you know, you could have the best electronics in the world, but all that other stuff actually does matter. And I don't want to think about it, but it actually does matter. You know what I mean? Of course it does. For, like, perception and sales and marketing and all that other crap. It sucks, Dave.

**Dave Jones:** Would I have been happy to buy this open SVE thing, this open EVSE, right? And even build it myself, right? I got the skill. You know, it's a kit. Sure, sure. And, you know, like... But use this to charge my car at seven kilowatts. Yeah. And be happy to leave it charging overnight.

**LTSpice:** In the house where your children sleep. Yeah, yeah, right. Right?

**Dave Jones:** It's like, eh, maybe. Maybe. Like, you know, probably. But the Zappy is just...

**LTSpice:** And then where do you fall on that spectrum as well? Right. You know? Like, I remember you said when I was... I think when... What's his name? Javier? I forget. One of the YouTube guys who does, like, DIY Powerwalls. And I remember you saying, like...

**Speaker ?:** Oh, yeah.

**LTSpice:** Right. But would you actually build one? You know? Would you be comfortable building one? And as I thought of it, I was like, hell no. Like, no. Same here. Hell no. I don't trust myself that much. Exactly. You know? Like, yeah.

**Dave Jones:** Exactly. Yes. A lot of people ask me, oh, build your own do-it-yourself Powerwall. No. No. The hell no. A, I don't have the time to do it. Right? And it's just...

**LTSpice:** I think some of it is, like, it's perceived bigness as well. And it kind of ties back to the show last week. When Lee was on the show, he related a phrase from his coworker, which is, two people working in a team are worth three. And I think that's kind of what I'm feeling in, you know, like, putting myself in this hypothetical because I don't have this device. But, like, if you have 100 people working on a device like this, you know, there's more people checking it, you know? You feel more confident. To me, it's soldering it together, you know? Like... And you could have, like, self-text and stuff like that to build confidence as well. It's not the only way out. But... Hmm. Yeah.

**Dave Jones:** And as experienced electronics designers, we're used to building our own stuff. That's a no-brainer, right? We feel totally confident designing and building our own stuff. But I think we're both, because we're not power guys, we're... You know, both of us would shy away from anything mains or high power or, you know, like, power wall related or charging my freaking EV. Right? It's like...

**LTSpice:** Right.

**Dave Jones:** You know?

**LTSpice:** Whereas a photonic induction would probably be fine with it. You'd be like... Oh, yeah. That'd be really quick. Yeah.

**Dave Jones:** Mike. Mike from Mike's Electric Staff. He's probably... Yeah. Yeah. He'd probably, you know, do it. No worries. Right? Mm-hmm. You know? But no, we're just wimps. Right? You know? Oh, yeah.

**LTSpice:** I've got a wife and a family and a home and I, you know, I just want the... Now, if I had an outdoor charging station like our mutual friend Martin Lorton...

**Dave Jones:** Oh, yeah. Totally.

**LTSpice:** Maybe I'd risk it then. Right? Yeah. He's got a shed where he's got solar and he...

**Dave Jones:** No, I could probably save myself as well. Yep.

**LTSpice:** Yeah. But that's like a detached structure as well that, like, it burns down. Exactly. It isn't my house. Yeah. But it's not my house.

**Dave Jones:** While I'm sleeping in it. Yeah.

**LTSpice:** I have an attached garage, guys. That's a...

**Dave Jones:** Yeah. Yeah. But that's also one of the things for the DC solar as well. Like, as in the string inverter versus these microinverters. These microinverters, I wouldn't really have that much of a problem because they are only mains. Whereas the high amperage DC string inverter stuff, that scares the living crap out of me. Right? These things arc over and they, you know, just the switches catch on fire for Frigg's sake, let alone the electronics. Right? Right? The switch... If a switch is responsible for thousands of house fires, a bloody switch. Yeah. Right? That's how, you know... They were freaking recalled here in Australia.

**LTSpice:** Oh, jeez.

**Dave Jones:** There were like 10 different brands of DC isolator switches recalled because of fire risk. A bloody switch.

**LTSpice:** Are there rooftop fire detectors for like solar systems? Not that I'm aware of, but for the ultra paranoid... That would be a good product idea.

**Dave Jones:** There's a niche market, yeah.

**LTSpice:** Yeah.

**Dave Jones:** Yeah.

**LTSpice:** That would be like a... You know, especially if you could like tap off a line somehow and like make it powered so it's like always connected and whatever. Yeah. But then like... Because say you have a solar system with this high voltage, high current string, whatever, and it lights on fire. It's probably going to take a while to burn through your roof, but it'd be better to know at the beginning than it did. Yeah.

**Dave Jones:** Right. It'd be better to know so that you can call the fire brigade and actually escape from the house. Yeah. Yeah. Yeah. Before it... Yep. But before it comes through to the smoke sensors, which are actually in your room. That's right. Right. Yeah. Then it's a little... By the way, if your smoke sensor is going off in your room above your head, then you've got to... You're smoking the room. Exactly. You've got a problem. Yeah. You haven't got long to get out. Let's just say that.

**LTSpice:** Yeah.

**Dave Jones:** Yeah. So I would actually feel much more comfortable having my own mains microinverter on my roof than I would my own string solar inverter.

**LTSpice:** Like a DIY version. Yeah. Self-built. If not completely DIY.

**Dave Jones:** Yeah. Okay. Yeah. I would feel safer. I feel safer having... But I've actually got a mix system up there now. Yeah. So I actually have both. So I've been debating whether or not we should actually go completely away from the DC thing. It's just not really worth it because buying a microinverter for each one of my existing old panels is like cost, cost more than the panels are worth. You know, so...

**Dave Jones:** Okay. But then I wouldn't have that worry anymore of that DC, you know, string bloody thing.

**LTSpice:** Maybe you should make a little fire detector thingy. Right. Maybe there's your next project. Maybe.

**Dave Jones:** Okay.

**LTSpice:** Cool. All right.

**Dave Jones:** We figured it out. What we need is an internet connected... Wi-Fi cellular connected internet of things DC isolator switch.

**LTSpice:** Bingo. Who are you going to call? Chris Gammell. There's something on fire in your neighborhood.

**Dave Jones:** It's a switch. And what it does is it detects whether or not it catches on fire and it alerts you on your phone. Holy shit.

**LTSpice:** I mean, it'd sell. It would sell, man. You just got to work up a little FUD. A little FUD and you're good to go. Speaking of IoT things, this is my last thing. I am giving a webinar next week on IoT system development. I don't expect anyone to really want to go. But if you do... You do know engineers generally hate webinars, right? I know. But, you know, you don't have to like sit there. There's always the replay video.

**Dave Jones:** Right.

**LTSpice:** So this is actually for a local group called Riot, Raleigh IoT. I'm near Raleigh, which is Durham. Durham and Raleigh are pretty close. Right. And I'm doing it virtually, but it's actually a cool thing in the area.

**Dave Jones:** So cool.

**LTSpice:** Yeah. I will tell people all the things they don't think about at the beginning when they should be thinking about them, because that's really when you get burned, when you don't know what the hell you don't know yet. So I'm going to try and tell you the things you don't know, and then you can go figure out yourself. Awesome. That sounds pretty good. I'll send it to you, Dave. I'll send you a preview link. All right. You can just watch it whenever you want.

**Dave Jones:** Fantastic.

**LTSpice:** All right.

**Dave Jones:** Now we are powers up. Catch you next time. Talk to you soon. Bye.
