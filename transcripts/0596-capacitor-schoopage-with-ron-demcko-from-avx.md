---
episode: 596
title: Capacitor Schoopage with Ron Demcko from AVX
url: https://theamphour.com/596-capacitor-schoopage-with-ron-demcko-from-avx/
---

**Ron Demko:** This is The Amp Hour podcast, released July 17th, 2022, with Ron Demko from AVX. Ron is a 40-year industry veteran in the capacitor manufacturing industry, and this is a discussion about film capacitor failures and capacitor manufacturer and other failure modes in general. This episode of the podcast is best experienced in the video form factor available on The Amp Hour YouTube channel. Because in this podcast, Ron and I discuss various slides that we're showing up on the screen and various images that we're discussing, but hopefully you'll still find the discussion interesting in an audio podcast version. Okay, well, as it turns out, it looks like I'm wrong. So we have an expert here who's joining us, Ron Demko from AVX. Thank you, Ron. You're going to tell us what I've got wrong, because I thought this was a self-healing issue, but you don't think so.

**Dave Jones:** Yeah, I think we could give you some details on the real event.

**Ron Demko:** All right, thank you. So what's your role at AVX? How long have you been there?

**Dave Jones:** Well, I just passed 40 years. Whoa! It's been here for a while. Yeah. Well, you know, it's funny, though, because the company changes. So every three or four years, we buy a new division. So at one point in time, it was just capacitors. Now it's antennas, connectors, modules, a whole bunch of other things. So, yeah. Right. I work in a small group in R&D, and we do engineering support, things like that.

**Ron Demko:** Got it. But you're mostly, but you're the capacitor guy, right? You're in the capacitor. Yep. That's your specialty. 40 years in capacitors?

**Dave Jones:** Well, yeah. Different types. Glass, tantalum, electrolyte, ceramics.

**Ron Demko:** Tell us your opinion. What am I seeing here? What do you think this problem is? Because you don't think that it is being destroyed by impulses on the mains.

**Dave Jones:** That's right. Yeah. Well, I think we should start going back and looking at the parts. So mainly these parts are non-hermetic. They're using a low-cost epoxy. So, you know, they're very cost-effective, easy to use, easy to choose. So it's a probability that moisture got in in the application. And then that moisture was trapped with that non-hermetic case. So what we have – well, there's also another scenario. There could be poor drying in the manufacturing process and possibly materials were – you know, water was put in there. That's very unlikely. So I think what we've got is a couple of easy explanations. Of course, those small holes or maybe the big hole that you have up on the upper right there. Right. That's a result of actually self-healing. Okay. So that's the vaporization, as you expect. Now, when we start getting into the other area, we can explain things kind of easily. As you roll this thing out from the left to right or right to left, you've noticed that there's a variance. Some of that variance is due to the difference and the connectivity from the shoopage on the termination to the actual electrode. So at one point in the video, you showed a very light background with some speckled scenarios. And that was just moisture and a high-resistance scenario. Right. But what we're seeing here is in the crack lines, the lightning bolt-looking thing.

**Ron Demko:** Yeah, that goes right – that almost went through the whole thing.

**Dave Jones:** Yes, that's right. So I think what you're dealing – you have this reaction of the moisture. And what's occurring is that you're getting a moisture effect that's actually causing the electrodes to change. They're getting more resistive. They're getting some migration or movement, oxidations, changing resistances. So those voids are most likely, to some extent, like a micro-healing or an impulse degradation. That's how I'd explain that lighter center section. And the darker blotches are most likely a result – yes. Those are going to be mostly a result of N-termination corona-type effects, something on that order. So it's always difficult to comment maybe, what, 15,000, 20,000 miles away or so. Yep. And not having dealt with the parts. But I think that's pretty much the scenario. It's definitely a moisture event.

**Ron Demko:** So will the moisture, like, eat away at the metal? Will it, like, actually corrode the metal? And what sort of metal are we talking about here for the metalization layers?

**Dave Jones:** Well, in some cases, there's zinc. But this, most likely, is not the case. It's usually alumina. It's probably on the order of 100 angstroms. The dielectric thickness itself – so the film itself – is probably in the order of maybe 1 to 20 microns, something like that. So it's a wonderful part when they work well. And I suppose it worked, in a sense. It worked.

**Ron Demko:** Well, this one is only a year old. See, that's the thing. That's why – because when I think of moisture ingress, all I think of is, like, old-school reefer paper capacitors, which are famous for, you know, getting moisture ingress. They crack. The cases crack. Moisture gets in. It is absorbed by the paper. And then when you go switch it on, you've got this big conductive path that just goes boom, and the magic smoke escapes. I just didn't expect that moisture ingress with film caps after, like, a year. And, you know, the actual product it came from is only a year old. Yeah.

**Dave Jones:** I can make a couple of guesses on where the moisture came in. And that's a big issue. Choosing the right epoxy is tough. And I'm sure these guys build great capacitors. It could happen to anyone. But the right material systems, it's a real secret, right?

**Ron Demko:** Yeah. And is that something you can test, like, after you've constructed them?

**Dave Jones:** Yes. That's a very good point. How do you do that? So what we could do – yeah, we'd put them on a moisture humidity test. Maybe it would be good to have 40 degrees C and, I don't know, 40% RH and maybe another 40 degrees C and an 80% RH brutal humidity cell. And then do an 85-85 cell. And what we would look at, we would look at the degradation of capacitance across time. And that would tell us a lot of things about what's happening within the device. Then we'd probably go in with EDX and we would do some x-ray evaluations of where the material systems have broken down and constituency of water, etc.

**Ron Demko:** And you're not the only one with this opinion as well. Tom Zednik, if I'm pronouncing that correctly, who's a former colleague of yours from AVX and is now over at EU – passive components EU. He's also of the same opinion that this is a moisture ingress problem and not really an impulse. Because, as you said, some of those small little points in there might be self-healing. Is that certain? Is that the size of a hole you'd expect from self-healing as from an impulse thing?

**Dave Jones:** Yes. Yeah, it's pretty neat, too, to throw these on a sample scope and apply, I don't know, a couple of different signals to them. And you'd actually see some noise occurring when we have self-healing events. So that'd be a neat – I don't know.

**Ron Demko:** Noise? What sort of noise are you talking about?

**Dave Jones:** Well, you'd actually apply maybe full voltage at maybe a moderately high temperature. And you might actually see some failures punching through. And you'd actually see some variation in the applied voltage of the part as this thing coronas. So when you get those little micro healing points, you actually vaporize that electrode material. And as it cools, it precipitates around that failure site. So if we could blow this up a little bit more with a SAM or something like that, we actually see a little dark halo around that white point of failures.

**Ron Demko:** I might put this under the microscope and see if I can see that. So this large hole here, I don't think that's a blow – I don't think that's a self-healing blowhole, would it? Would you get one that large?

**Dave Jones:** Well, you could. It depends what hits it. I think that's maybe more unlikely.

**Ron Demko:** Maybe I've torn it there. Is it possible that I've torn this when I've taken it apart?

**Dave Jones:** Yeah. Yeah, I think you did a good job on the DPA, but I think we might have approached it a little bit differently.

**Ron Demko:** Right. Okay. Well, it was my first time. Okay. Oh, you did. We'd still hire you.

**Dave Jones:** All right. All right. Good. One of the things there, though, is there's also a possibility – unlikely possibility, but there's a possibility that the metalization come to come off of the film. Right. So if you had the counterpart of that roll, you could see if that was a deposit.

**Ron Demko:** I think I did see that. As I was unrolling, it looked like some of them peeled apart. So, yeah. I wasn't sure if I had the correct layers or whatever peeled. So, yeah. I wasn't really – It's hard to do. Yeah. Are there, like, qualified parts that would be better qualified for moisture ingress? Like, would you – like, do you sell, for example, higher quality ones that are better – like, you know, look, we guarantee these ones are hermetically sealed and you won't get moisture in?

**Dave Jones:** Well, we don't have hermetically sealed films from what I know. Right. I don't know that there are any. Well, I almost take that back. There's films in cans, so, okay, they're hermetic. Okay. But they're a much different application. But I think, in reality, some of the progress that's been made on the encapsulants could get you such a near hermetic case that you would never experience this.

**Ron Demko:** Right. So, if it's in a metal can, that's by definition hermetic, is it, if it's welded? Yes.

**Dave Jones:** If it's a welded can. Yeah. I mean, many companies will take great care in ensuring the atmosphere within that device, yes.

**Ron Demko:** I don't think I've ever seen a metal can film capacitor. Is there such a thing?

**Dave Jones:** Well, yeah, there is. So, I mean, some of these guys are – Oh, the bigger ones.

**Ron Demko:** Oh, right. The big bad boys. Okay.

**Dave Jones:** Right. And we made them about the size of half of a foster can.

**Ron Demko:** Right.

**Dave Jones:** You know. You're right. Not surface mount, though.

**Ron Demko:** Okay. Got it. So, when you – like, the ones that we tore down here, where's the sealing point? Is it the potting? Is it when they're potted? Is that what they're trying to do? Is that they're trying to seal it as best they can? Yes. Or – right. Okay. So, if the potting's poor –

**Dave Jones:** Yes. It would possibly be at the perimeter of the metallization to the encapsulant.

**Ron Demko:** Right. Okay. And then through the shoopage on the side, really? It would come in through the side. It wouldn't come in through the actual film wrap, would it? Because I would imagine that that's pretty sealed.

**Dave Jones:** It's correct. That's correct.

**Ron Demko:** Right.

**Dave Jones:** It would be at the interface of shoopage or some errors or voids in shoopage.

**Ron Demko:** Got it. Okay. Well, we've got a – we've got a failure modes document. Failure modes. Oh, I can't – I can't zoom that up, but I can put an overlay up here. So, this actually shows the failure modes, doesn't it? Or the most likely failure modes in sequence?

**Dave Jones:** Yeah, there's some good information there. I think possibly the snapshot of the fuse areas or the other one that showed the punch-through is a good way to look at it. Generally speaking, you could say there's two types of films. There's the smaller, low-power films, and they're dealing with that thin metallization on the dielectric. So, we've got maybe 100 microns. And in small scenarios, we'll have a punch-through. We'll have the cooling of that vaporized metal. And it heals, and we drop cap a little bit. So, that's one case. And then, when we get to very high-power films, there's actually microfuses that multiple companies put on their product. So, normally, you'd think that maybe scribing fuses – and here we go – on the bottom part of number four, you could see that there's tiny electrodes and little connections between those electrodes.

**Ron Demko:** Right. So, a little grid, a little square pattern, a little square boxes with little conductive parts between them. Okay. Yes.

**Dave Jones:** And the trick is going to be to make sure that those fuses don't die under certain use scenarios of the film. And now, that's more common with the really big films, the ones that are maybe, I don't know, 20-kilowatt drives or something like that.

**Ron Demko:** So, you wouldn't find those on little surface-mount jobbies or the small ones for mains. And things like that.

**Dave Jones:** Well, they could be, but I'm not – I don't think that anyone has that.

**Ron Demko:** For the application that we're looking at here, which is like a capacitive dropper kind of thing to power a circuit, which you probably – apparently shouldn't use X-Class caps in this situation.

**Dave Jones:** Is that something that you are familiar with? I'm not familiar with that. Yeah. Okay. You might be able to get away with it. Right. I'm kind of surprised about the failure. Usually, films are incredibly reliable. Now, their disadvantage is that they're quite large on a relative basis for the amount of cap you get. But, of course, the self-healing and some of the other low-noise characteristics greatly outweigh that.

**Ron Demko:** Right. So, is moisture the most probable failure mode? Because apparently, if you're in the industry, there's other YouTubers out there who tear apart, you know, these cheap Chinese little, you know, $5 gadgets, and these caps just fail all the time. Is it most likely to be a moisture problem causing this or a capacitance loss due to impulses and self-healing?

**Dave Jones:** Within films, I – well, you know, it's difficult because if you don't get self-healing correctly, it could very well have an early failure. Right. So, that's something to be cautious of. Usually, the industry is getting much better with that. I would say in the old days, it was well over half being caused by that early wear out. I think it's probably switched. Yeah. So, it's probably moisture.

**Ron Demko:** Probably moisture. There you go. I thought it was only the reefer caps that had moisture problems. And a year into it, too, just, you know, a year-old product. I just thought, wow, you know, and it's losing so much capacitance. So, it just eats away the metallization layers and causes a drastic drop in capacitance, which then, of course, if you're using it as a capacity for a dropper, that changes the value and that screws up your circuit.

**Dave Jones:** Yeah, that's right.

**Ron Demko:** Completely. So, yeah. Awesome. All right. Well, thank you very much. Ron, that's, yeah, that's something I was, I went into this video thinking that it was an impulse self-healing issue due to capacitance. But it looks like it's probably a manufacturing moisture ingress type issue.

**Dave Jones:** So, there you go. Hey, and I'll tell you, Dave, if we have a failed cap, one of these big power caps. Yeah. That are about the size of, I don't know, a cabinet, file cabinet. Oh. It's 100 kilograms. Oh. And if they're out on the, you know, Asia and such, I'll be able to ship one to you if you want one.

**Ron Demko:** Oh, yeah. Sometimes they're dented. Right. But it'll have to be shipped by boat. It'll have to be shipped by the slow boat. They physically ship by the slow boat because you can't put them on the plane.

**Dave Jones:** Yeah. Wow. Yeah. Oh, wow. Yeah, we're in CERN and stuff like that. So, like in CERN, when we start getting into CERNs or, you know, other power drives, right? We can't have a compressor go down because of a failed cap. That's where those really big guys are used.

**Ron Demko:** Right. Okay. And these are all, would these be made to order or whatever, like these giant ones?

**Dave Jones:** Yeah. Yeah, they are. I mean, some of them are like 75 kV, massive, massive amounts of energy. Of course, you could do direct with energy and some things like that. But the little guys, they kind of come off of like a bicycle wheel that has the film wound around it. And then they're just cut in a certain arc. Right. Then they're put into a frame. They do the shoopage and, you know, we're done.

**Ron Demko:** So what is the shoopage material that you guys use mostly? Or does it vary? Or is it a secret sauce? It does vary.

**Dave Jones:** I think there's part of that too. And most of it's I've forgotten. So it's difficult. I have to admit, though, I've done that many years ago when we were experiencing some different material systems. We're actually trying to shoop upon glass for a variety of things. But that's made a lot of progress through the years. You know, it's interesting, though. So shoopage might have a, they might go 0.8 millimeters or a millimeter in. Yeah. And other, just to put it in perspective, right? So some of the other accuracies on our processes, not films, but other types of caps are one micron line width. So that's, you know, it's getting down there, right? And then if we look at the thickness for a high CV ceramic capacitor, well, some of those might be 0.4 micron particles and 2 micron dielectric thickness. So a lot's been going on in the world of caps.

**Ron Demko:** Yep. Oh, it's phenomenal. The number, the variety of caps is, it's just dozens and dozens and dozens of them. It's just incredible. So can you take us through some of the technology?

**Dave Jones:** I think this one's kind of neat because it shows, you know, we went from the bigger caps. Remember, in my early career, I remember we couldn't put a 0.1 and a 12.10. Right. You know, that's amazing, right?

**Ron Demko:** Yeah. So that's 0.1 microfarads, folks. Right. 0.1 microfarads. In a 12.10 size capacitor.

**Dave Jones:** That was the old days.

**Ron Demko:** And we're talking imperial here, not the new metric sizes either.

**Dave Jones:** So now we could do that 0.1 in an 0.0804 or an 0.1-0.05, if we want to talk a big part, right?

**Ron Demko:** I don't even know what that size is. I mean, it's so ridiculously small.

**Dave Jones:** Oh, it's teeny. In fact, we could do one mic in an 0.1-0.05. It's under development. Wow. You know, what's happened? One microfarad. Yeah. Yeah. It's hard to believe, isn't it? Yeah. It's crazy. The militarized parts are really a huge impact on everything.

**Ron Demko:** But you pay a penalty for that, don't you? In the dielectric you have to use and the performance is absolutely terrible, isn't it? There's no way you can get a quality performance dielectric that small with that higher capacitance. Right.

**Dave Jones:** Is that right? It's not going to be stable with temperature or with applied voltage. Yep. Or with time. Yeah. Even some AC noise on that, some ripple. Oh, right. Yep. But yeah, it's amazing what's been going on there. There's a low inductance aspect to this as well. When we look at the old days, maybe a 12.06 was a nano Henry of inductance. And now the 0.204 might be 120 picohenries. But there's other termination mechanisms where we're terminating on the side. So we terminate on the long length and the electrodes are perpendicular to the board. So we have a very low loop inductance.

**Ron Demko:** Right.

**Dave Jones:** We can get inductances of a capacitor down to maybe about 25 to 40 picohenries.

**Ron Demko:** Wow. That's insane. That's just crazy. You would get more on your traces going to the component on your PCB than in the cap.

**Dave Jones:** Yeah, you have to be really careful. Yeah. Because you could mess up a very highly performing cap with a bad layout. A bad layout.

**Ron Demko:** Yeah, exactly.

**Dave Jones:** It does so much for you in terms of the resonant point and the ability to supply high DIDTs to so many different types of circuits. We might be doing low side drivers on LiDAR. We might be FPGAs, et cetera. But a lot of work has occurred in the material stability.

**Ron Demko:** And is that what this is showing here, the stability?

**Dave Jones:** Yeah. What we have is there's some DC biases. They vary by dielectric type. They actually vary by lot as well. So engineers should be very cautious. Yes. Okay.

**Ron Demko:** Right. Okay. So one product may not perform the same as the one next month because it's a different lot. That's somewhat true. If you're working in such a critical application where that matters.

**Dave Jones:** Yes. Or you could contact the manufacturer and we take these questions every day. Right. And we give you certain series within high cap dielectrics, which are stable. And on the right, you can see how much it varies by manufacturer. Sure. Now, all, and this comes from EPCI, European Passive Components Institute. That's Dr. Zenechik's site. He's done a great job in showing the overall performance of some of the key players. And you can see the variance is just major. Yeah. But as we said, if you take care, talk to the manufacturer, you could choose the right one that's going to greatly minimize changes on a lot by lot basis.

**Ron Demko:** Especially if you're on the high performance aspect side of things, choosing the absolute. And there's where you can't change brands. You can't change supplies. You know, like even batches might have a problem. You might have to select on test even perhaps.

**Dave Jones:** Well, if you're careful and talk to the manufacturer, you're safe.

**Ron Demko:** Okay.

**Dave Jones:** Got it. Yeah. And you can see here where they can get the various amounts of variance because of ripple on dielectrics. That gets significant. So it's quite possible that if you're not aware of the phenomena of the dielectric instability with biased voltage and temperature and time, you might think you have maybe a one mic part and you're down to 150 or 200 microhertz.

**Ron Demko:** Yeah. That's a real big deal. So what is the latest, greatest dielectric? Is it like that gives you the highest volumetric capacitance per unit size?

**Dave Jones:** Well, you know, great progress has been made in the ceramic world. So particularly now that AVX is part of Kyocera, the Kyocera group has a very big stability effort going on. They've made some tremendous material changes there in ceramics. So that's really important. And that's going to occur across the world. I mean, as manufacturers, we know that we have to have more stable ultra miniature parts. If we start looking at other types of dielectrics, and of course, dielectrics are everything in terms of cap performance.

**Ron Demko:** Yes.

**Dave Jones:** We could talk about the tantalum polymers. They have a lower ESR. It's approximately, you could argue, it's about one eighth of a traditional MnO2 tantalum. So that allows us to get about eight times more current. Right. Wow. The great thing about that is they're incredibly stable. So that's a big deal. And then in the world of super caps, well, we could give you one farad part in something that's maybe six millimeters in diameter, about nine or ten millimeters high.

**Ron Demko:** That's crazy. At what voltage? Like three volts or something? Yeah.

**Dave Jones:** About three. Yeah. Right. Now those you want to derate. Right. You go up by 10 degrees C, you have to life. And every time you go up by like 0.1 volt, you have to life. Sorry.

**Ron Demko:** Did you say every time you go up 0.1 volts, you have to life?

**Dave Jones:** Yeah. Roughly speaking. Yeah. There's a great paper on that. I'd love to see the curve on that. There's a good life to start with though. Yeah. There's a good life to start with though. Oh, wow. Yeah. But, you know, in fact though, there's a, there's a lot of those in vehicles now, whether it be our dashboards or the dying gas on your emergency call circuits and things like that. It's really interesting.

**Ron Demko:** Is, is, is that to keep like emergency power there just in case the electrical systems fail and something? Well, yes.

**Dave Jones:** In the case of the e-call, it's used for, um, backup. So you can get that one call, you know, I've had an accident at whatever mile post. Right. Yeah. Um, and for the case of, um, well, there's, there's an interesting case on, on some of the chunks here in the States, there's an inverter. And that inverter has a buffer with a large super cap that goes essentially to the alternator. So, you know, as you plug in some oversized saw, like everyone does, and I'm guilty of, you don't cause problems down line.

**Ron Demko:** Right. Got it.

**Dave Jones:** But this slide is really neat.

**Ron Demko:** Yeah. Because it talks about. These are tandem, uh, these polymer tantalums. Yep. These aren't, these aren't your old school daddy tantalums that blow up. No. These are, uh, well, is there. Is there still a, is there still a flame issue with these types of, uh. No, no. Polymer tantalums.

**Dave Jones:** They're all benign. Yep.

**Ron Demko:** Okay.

**Dave Jones:** Very good. Um, that incredibly good inductance and great stability. So these are going to be solid as a rock. And what we've seen is many times you're going to want this bulk cap that's stable, low inductance and all of that. So you use this in conjunction with, uh, some of those high CV, less stability ceramics. Uh, so you'll, you'll see this around all of, uh, FPGAs and, and some, uh, cores and things like that.

**Ron Demko:** Um. Yeah. Yeah. There's the low inductance stuff. Tell us about how you minimize inductance by, by case size.

**Dave Jones:** Yes. What we try. Well, of course, as you go with a smaller case size, as you can see, the, the first column shows, you know, 1206, all the round to 0201.

**Dave Jones:** Uh, we drop the inductance, as you'd imagine. That's because we have a lower loop area for the, uh, for the end terminations. So the next slide over is called the LICC. And, uh, that's where we just terminate on the long end. Yep. So we could drop the inductance by a factor two. And then there's a device that looks like a cap array, I believe. I'm not sure if we have a slide on that, but yeah, there we go. Yeah. There we go. Further drop. Yep. And, uh, the last one looks like a, a, uh, an LICC. Yep. Uh, well, this is the LICC.

**Ron Demko:** So this one here is four. Is this four caps in one?

**Dave Jones:** No, that's good. No. It looks like a cap array. Yeah. It does look like a cap array. Right. Okay. Yeah. What we've done there is we've just put alternate terminations on the part. So you have essentially a single part with, you know, four term terminations on it. Hey, now it's interesting too. I could get you a free AVX Cerevic shirt. If you guess the number on a 1206, how many IOs could we put on it in theory? A 1206. How many pins you're talking about? How many pins? Yeah. How many land grid array pads could we put on it?

**Ron Demko:** On a 1206, uh, uh, uh, uh, point. Oh, uh, hang on. Don't guess why you're going to make me feel bad. Uh, um, I don't know. And eight per side. No, no, it's more than that.

**Dave Jones:** No 12, 12 per side. We could do, well, we can do 32 on the bottom side of the package. Yeah. So you never want to use that. But the point is that the metalization accuracy is so good that putting eight or even 10. Yeah. Isn't that big a deal. So I think we've got further reductions coming in low inductance. And I'm not a big fan of land grid array caps. Right. And, and in the world of RF, it's, it has a lot of advantages where we could drop parasitics.

**Ron Demko:** So what is the difference between the, the array one, the pin array like this and just the one big strip like that? I would have thought this would have been better. Yeah.

**Dave Jones:** Uh, well, it's, it's, it depends on the case size. So in the, the, uh, if we look at like an 06-03, the standard 06-03 part would be about, let's say 450, uh, Pico-Henries. So in the LICC, this part, or excuse me, the, this looks like an LICC, but it isn't, uh, that's going to be on the order about a couple hundred. And, uh, maybe, maybe you could say, oh, I don't know, 110 or so on the best, but this land grid array part, the part that has the vertical electrodes, that's about 30 Pico-Henries, maybe 35.

**Dave Jones:** Yeah. So now the trick there is that we have the electrodes vertical to the board and in the RF world, I don't know if you played around with a lot of ham radio stuff, but. I'm not, I'm not an RF guy, no. Well, all that's cheap guys will take, uh, a bad capacitor, at least before I worked here and they gave us free caps to experiment. Yeah. What, uh, what we do is we take the, uh, a cheaper cap and place it vertical on the board and you'll get a better frequency response. So you naturally reduce the inductance that way.

**Ron Demko:** Right. So you'd flip your SMD part up on its end. Right. Yes.

**Dave Jones:** Only certain case sizes.

**Ron Demko:** Right. Oh, yeah. Yeah.

**Dave Jones:** But when the math works out and it doesn't fall over, it's a good, it's a good solution.

**Speaker ?:** Yeah.

**Ron Demko:** Oh, terrific. Or you'd put multiple ones in parallel on the same pad vertically.

**Dave Jones:** Yeah, it could do. In fact, that's a good point. There are larger case sizes. And in fact, there's a new military spec coming out that allows the manufacturers worldwide capacitors to take capacitors and put them vertically or horizontally in between the lead frame. And now you have a very low ESR, low inductance bulk cap. Right. So a lot of those are flight systems. Ooh.

**Ron Demko:** And would you know this? You, you, it'd probably be in the sales department or something, but what is the most popular size these days? Like put in volume. What would you make most of? Like in terms of just a regular SMD ceramic cap?

**Dave Jones:** What would be? I don't think it would be any larger than an 0402. It's probably an 0201.

**Ron Demko:** Right. An 0201. Is that probably driven by the mobile phone market, I guess? I think it would be. Driven.

**Dave Jones:** Right. Now, in fact, I was, you know, I get lucky because I get work on many different programs per day. And we were dealing with a satellite company looking to do an 0201 flight cap. So they're not yet at that point as an industry. But I'd say 0402 would be the realistic spacecraft limit.

**Ron Demko:** Okay. Is that because the smaller you get, the less qualified you can, you can make them, I guess, the less, like the more vulnerability you have in terms of physical variation and physical failure modes?

**Dave Jones:** That's pretty true. Yeah, it's good intuition. So what happens is when you think of this part, if we were to do a cross section, think of vertical electrodes or chunks of metal that have to be isolated from the outside world and moisture. Right. Yeah. Because of, you know, the effects it would have on it.

**Ron Demko:** So even in ceramic caps, you have moisture issues that you can have moisture issues as well in ceramic parts?

**Dave Jones:** Yes, if you had a crack in here. Right. Moisture, but again, we drop our insulation resistance and then we have a problem. Hey, but by the way, there's parts that have terminations that have a sub-metalization of a conductive epoxy. And that conductive epoxy, it will actually allow you to bend the printed circuit board and not have a crack propagate in the cap. Multiple manufacturers have it. Yep. It's a really big deal.

**Ron Demko:** And yeah, well, I've done, this is I think the next slide. I've done a video on this and ceramic capacitor cracking and board flexing and how this can cause shorts and fires. I've had my own products catch on fire because of, you know, the board is flexed. And, you know, people mount them. It's also a PCB construction, a PCB layout thing. If you put it too near to a screw point, for example, like a mounting point, for example, just screwing in your board into your chassis can cause a crack in your capacitor and boom, up it goes. It could be a disaster.

**Dave Jones:** Yep. And especially on a car, imagine like terminal 30 power at all time. Boy, you got real trouble.

**Ron Demko:** Shock and vibration is crazy business. Is it mostly shock or can you get cracks through vibration as well? I'd assume that's less common than shock impacts.

**Dave Jones:** That is true. But there's actually a paper that I believe was done by NASA that talked about a vibration induced crack. It's very uncommon, in fact. Hey, but, you know, it's interesting. Most of the failures on a capacitor, ceramic capacitor specifically, are application errors. And so if we talk, let's say, a million failures, right, or something like that, I bet maybe less than 10. Oh, goodness, less than that. It would be less than, well, we had to look at maybe 100 million caps. So maybe one is the manufacturing error and the rest of them usually are mechanical issues. Right. It's amazing the percentage. It really is.

**Ron Demko:** Wow. Yeah, well, I'm stunned that you can even make them this small. Or, you know, I'm stunned that anyone would want to use ones this small. But I guess you have to, right? That's the progress. But as you said, certain applications, military and space and or, you know, airlines or something like that want to, they're very on the safe side. So they're going, oh, yeah, we'll use these O201s. But I don't know. Seems a bit like, yeah. Right. I guess it takes years for them to qualify.

**Dave Jones:** Oh, it does. Yes, it does. And if we look at a comparison between a military, well, a flight part and the highest capacitance, high CV part, you could probably say the dielectric is four times thicker on the high rail part.

**Ron Demko:** Wow.

**Dave Jones:** Now, that's changing. And it'll continue to change. Particle sizes of the ceramic are going to get smaller. So we'll have less E-field per grain, things like that. But for the most part, there's going to be some practical limit where we're not going to really go underneath it. I thought it might have been O201. Certainly it isn't. And maybe I'll bet that there's one more iteration after O105.

**Ron Demko:** Right. Ken, can you explain, you mentioned E-field per grain there. Can you explain what that is?

**Dave Jones:** Yeah. If we look at, I should have given you a better diagram. Do we have anything else? If we looked in between the electrodes, we would actually see the grains almost stacked up between them. And what you'd like is maybe X number of grains. So you could divide the electric field across each grain. And if one fails, you don't.

**Ron Demko:** What actual material grain are we talking about, though?

**Dave Jones:** Barum Titanate. So it's a ceramic grain.

**Ron Demko:** Right. Okay. Right. So they're actually granular? Yes. At the physical level, they're actually a granular structure?

**Dave Jones:** Yes. Yeah. Oh, interesting. I assume. Grains that are fired into a monolithic block. Oh. And the grain sizes are usually on the order of about, well, it varies there again, but manufacturer, composition. But we could say maybe a half micron or so.

**Ron Demko:** Mm-hmm.

**Speaker ?:** Yeah.

**Ron Demko:** Interesting. Yeah. I always just assumed it would be a solid ceramic material. But you're saying it's grains compressed.

**Speaker ?:** Yes.

**Ron Demko:** Okay. Right.

**Dave Jones:** Wow. That's something I didn't know. It's really neat. So we build this by taking a ceramic, milling that ceramic to a certain particle size, and then suspending it in a binder. So it almost looks like paint. And then we'll pour that paint out on a stacking mechanism. And then we will dry it. We'll put a liquid metal, a liquid electrode on it, and then do the next layer of liquid paint, that dielectric. Mm-hmm. And then do the opposing electrode, build up to the right cap value and XYZ thickness. Yeah. Wow. It's really interesting. It's basically a liquid cap.

**Ron Demko:** How do you produce, like, billions of capacitors? I don't know what volume just AVX would make every year, but it's got to be in the billions and tens of billions of capacitors. It's got to be. Right. It's just crazy. And you can buy them for next to nothing. Well, not the real high-value ones are quite expensive these days. Right. But, you know, like, just a jelly bean low-end one is just so cheap.

**Dave Jones:** That's true. So much has occurred in terms of the mechanization on this. Wow. And it makes sense. We got exceptionally good, built our own equipment, came up with special processes. So the selects are exceptionally high. And you could kind of see why, given that volume. If we make an error, it's repeated very quickly.

**Speaker ?:** Right.

**Ron Demko:** Yeah. If somebody tweaks something on the production line that they weren't supposed to.

**Speaker ?:** Right.

**Ron Demko:** Okay.

**Dave Jones:** It's very cautious, very stable.

**Ron Demko:** Right. Is it like, are there many people on the production line? Is it like a, or is it like as completely automated as you can get it?

**Dave Jones:** Well, it's not like a resistor factory. I've had a chance to see one. And I believe they were building a billion plus with, I want to say, eight or ten people. So we're nowhere near that. Okay. Right. But it's not an army of people.

**Ron Demko:** Wow. That's incredible. So, so what are the different technologies for the, you know, you've got FlexiSafe trademark, but I'm sure you do different techniques for flexible end caps. This is what I've talked about in my video. It'll take the, so as the board, as the board flexes, as the board flexes like that, then the capacitor, then the end terminations can take, can decouple that stress from the ceramic. That's right. Yeah. You've got different techniques for that?

**Dave Jones:** We do. Now, it's stabilized to one material system. And it's a great trade secret, but it basically has a conductive epoxy. And that could be very problematic because if it's not the right conductivity, we increase the ESR.

**Ron Demko:** I was going to say, yeah, you screw up your ESR. Yeah. Right. And does that mean your ESR can change slightly when it flexes?

**Dave Jones:** Well, no. We're very cautious. Okay. It could. Right. That's a question for an end user. Right. And the other one is ESR could change and suddenly you can get a short if the, if that conductive epoxy is, is, I want to say it without giving out trade secret, if it's the wrong conductive

**Ron Demko:** epoxy. Right. Okay. No, it's all good.

**Dave Jones:** Very cautious. And I'll have to say that the flexible terminations have gotten very good because there is a military spec, 32, 535, and they actually call out the use of flexi term or flexible termination material sets. Got it. And there's multiple suppliers to that. So it's, but truly as end users, they should be careful to make sure that that termination is stable with ESR and under environmental conditions.

**Ron Demko:** Yes. Yep. And there's on, then on the design side of things, as a designer, you can, you know, if that's an ultra critical spot and you can't afford a short in a capacitor, then you would put two in series. You have your capacitance, but it improves your reliability.

**Dave Jones:** And that's what we're looking at here. This flexi safe has the two caps in series. So this is the traditional. Oh yeah. I think we saw that.

**Ron Demko:** Yeah. Yeah. Two, two, two caps in series there. Yep. Okay. Right. So that's, that's, that's built in. So you don't have to do that on the, you don't have to use two parts on the board level.

**Dave Jones:** Right. And here we're showing the ESL of two parts in series versus a single. Of course, the value on the flexi safe is half, as you said. Yes. And then we did a frequency plot looking at ESR and it's, it's very appealing.

**Ron Demko:** Yep. Terrific. They'd also use those in the automotive market too, wouldn't they? Yeah. I would assume.

**Dave Jones:** Self-driving technology.

**Ron Demko:** Yep. Yep. There's, there's rumors going around that because of the component shortage in the automotive industry, they're putting in dodgy caps instead of like they're putting in non-flex ones instead of flex. Anyway, that's, that's, that's just a rumor. So.

**Dave Jones:** Maybe I don't, you know, I'm kind of far out of that.

**Ron Demko:** Yeah. No, no, I'm sure. No, I, I, I don't expect to comment from ABX on that. That's not your, you just sell them. You don't actually implement.

**Dave Jones:** I know our guys would love to take the orders.

**Ron Demko:** Yeah.

**Speaker ?:** Right.

**Ron Demko:** You know, it's a classic though.

**Dave Jones:** Well, I was just saying about lead times. I don't get involved in lead times, but I just wasn't aware there was any problems, but you know, so much is going on. There's usages off the chart.

**Ron Demko:** Oh yeah. Well, there was, I can't, was it five years ago now was the great capacitor shortage. That was nuts. It was, is that because there was like one or two major, one factory caught on fire? I can't remember the details of that. I don't know. What was, oh, it was, yeah, it was bad. You, you could not get a reel of SMD, you know, one mic caps to, you know, it didn't matter how much you paid. You just couldn't get them at one point. Yeah. And it was.

**Dave Jones:** I know we've expanded beyond belief. Right. And that's great. Okay. So, you know, I think I'm badge number four or 500, right? And I think now the company's at 28 or 30,000, at least our division of KS.

**Ron Demko:** Wow. Yeah. Yeah.

**Dave Jones:** It's grown.

**Ron Demko:** That's, that's nuts. So, right. So what's this pulse withstanding stuff? Can you explain what makes it a pulse withstanding? I mean, we, I mean, we're talking 24 kilovolts, 26 kilovolts, 28, 30.

**Dave Jones:** Yeah. Pretty significant stuff, right? Yeah. So when people want to, we realized two things, right? Number one, we build a varistor, which looks like a ceramic capacitor, but in the presence of an electric field, it will become conductive. And it's just like the big old MOVs that you used to use on one. Yeah. Right. Right. But now we can build them down to an old tool, one size. They don't wear out and all of that. But the pulse withstanding caps, when you want to integrate versus clamp, these are ceramics that are used on less sensitive IOs that if you integrate down to a few hundred volts, the, the IC will survive. So this is a big deal. A lot of times we used to pray, right? In the old days. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Exactly. 500 volt part.

**Ron Demko:** Yeah. Yeah. Yeah. Okay. But these are specifically engineered to do this job. What else? Low inductance, high, high, high current jobbies.

**Dave Jones:** Yeah. Well, you know what we did here? These are three terminal caps. Yeah. And now there's a 10 microfarad, I think a 15 microfarad 0402. And what happens is we've, we've made this into like a T filter. The next slide kind of shows.

**Ron Demko:** Okay. Oh, yep.

**Dave Jones:** What's occurred. Yep. There we go. Basically what we've done is we take out the parallel inductance looking at that equivalent model. So we have a low cap C1 to ground, low inductance. And that's thing that could be 10 or 15 microfarads. And then we'll inject or transform that parallel cap into series cap, inductance. Right. So we transform the parallel inductance to series. And we end up with a very low Q filter. So that means it's broadband. You could be 30 dB down across maybe a gigahertz. Right. And you could start that response at maybe, well, 20 megs. And you could have, depending on which part you choose, you could have parts that have their endpoint, 30 dB points that may be 10 gigs. So it's a neat, cheap, dirty broadband filter.

**Ron Demko:** Got it. And it saves board space too, which is, you know. Oh, it does.

**Dave Jones:** Right. And it takes a lot of the questions out of like hysteresis on the inductor or temperature fix on the inductor, et cetera.

**Ron Demko:** Got it. That's all taken care of in the part. You don't have to worry about component selection there for your capacitor and your inductor and everything else. It just makes the design process vastly easier. So, yeah. But, well, there's some of the benefits there. Yeah. Yeah.

**Dave Jones:** Nice. It's just real easy to use. Actually, that's out of date now that we can do up to 10 or 15 mics. Yeah. It's kind of interesting. But it's easy. You could see the response and they're kind of interesting. All of this has spice and simulations that are exportable. And, of course, all the manufacturers are putting out much more spice models, of course.

**Ron Demko:** Now, you're a capacitor manufacturing guy rather than an electronics design engineer. Actually, what is your background?

**Dave Jones:** Oh, doubly. Yeah. Yep. Yep. Yep. Doubly. Okay. So, I come here rather than doing design. Right. But I might be able to do a couple of things.

**Ron Demko:** Okay. What's your standpoint on multiple caps in parallel for bypassing? Well, I mean, I think that's fine. Because, you know, there's a ton of people say just one big 10 mic jobby is fine. Because that's what these impedance curves here. You overlay two impedance curves and you're supposed to get a broader, lower inducted, lower impedance path over a wider frequency range if you use two caps as opposed to one.

**Dave Jones:** Certainly, that's true. And we've seen that as a trend and seen people that want minimum ESRs and controlled ESRs for ringing and all that. What's interesting is that the low inductance parts, the LICC, the LGAs, the ones that we saw before, those kind of change things a little bit where you might be able to use a big bulk cap and one of those. Now, the three terminal caps, this feed-through concept, it changed things a little bit further because you might have a 10 microfarad cap, but it has a very low inductance. So it has a broad frequency of operation. So although it's very valid to have the multiple caps in parallel, and, of course, there's negatives to that, right? Yes, it can.

**Ron Demko:** Yeah, poles and zeros with your PCB inductance, and it resonates to buggery and, yeah.

**Dave Jones:** Yeah. You know, simulation kind of helps you out, but, you know, the effort was put in on the low inductance parts, LICC, LGA, and then now this three terminal cap. I think we're starting to change things. And there's something that we can't really talk about, but imagine a true bulk capacitor that has a feed-through characteristic. So that'll be something that will be coming out soon.

**Ron Demko:** Ooh, ooh, new capacitor type. Okay. Ooh, exciting. Specifically for bypass applications?

**Dave Jones:** A lot of applications.

**Ron Demko:** Right, okay, right. I'm sure there's many. Yeah, right.

**Dave Jones:** Yeah, it's kind of interesting. But, you know, it comes back to the metallization control and the material advances that are occurring. There's a lot of those trends which are reinforcing one another. Yep. And it's really going to provide some significant new types of components out there.

**Ron Demko:** No, that's the, yeah, the shock vibration, anti-shock vibration stuff. Yep.

**Dave Jones:** Yep, yep. So the determinations on the tantalums tend to take quite a bit of stress. And in fact, you know, one of the best applications for tantalums now, well, there's great applications. One is on SSDs to hold up, you know, the dying gasp there.

**Ron Demko:** Right, okay.

**Dave Jones:** But then, with everything we learned there, we took a relatively standard tantalum, the MNL2 technology commonly, and they could be a great part for wake-up caps or even low-level scavenging energy harvesting caps. So ILT is seeing a big use or potential use of ultra-low leakage tantalums, small package, quite good.

**Ron Demko:** That's interesting because I never associate low leakage with tantalums. That's something, like as an older guy, I just don't associate, you know. Yeah.

**Dave Jones:** Well, me neither until I saw the curve. In fact, after this, I'll send you the curve. Yes, please. And it's amazing. If you derate, it's exponentially dropping.

**Ron Demko:** So that is the trick, is it, to derate them? And then the leakage. Ah, there you go.

**Dave Jones:** Yeah, you know, the other neat one is, on tantalums, the tantalums, the bathtub curve, okay, it's true, but the end curve is maybe a thousand years out or so. Right, okay. So, you know, they're incredibly reliable parts.

**Ron Demko:** Wow, okay. Yeah, yeah, because they got a bad rep, especially the tag tantalums, you know, the old school tag parts with the, you know, through hole pins and just the blob types, which are famous for catching on fire and whatnot. Yeah.

**Dave Jones:** Well, you know, they actually could self-heal to some extent. Oh, okay. Yeah, and that's why we tend to derate them. So, in fact, I have a neat spacecraft story. There is a device that's flying with a tantalum that was installed incorrectly.

**Ron Demko:** Oh, no, about what, backwards? Yes, sir, yeah.

**Dave Jones:** It's like a one-point rail, you know, and I think it's a 50-volt part. So, it's not recommended, of course. But there's some, I guess, horror stories in production that kind of turned out well, you know. Right.

**Ron Demko:** So, we can't name this probe, can we? No. No, no, okay, right. Okay. Is it a probe or is it a satellite? Can we narrow it down?

**Dave Jones:** I can't hear you, Dave.

**Ron Demko:** No, okay. Okay, all right, all right.

**Speaker ?:** Yeah.

**Dave Jones:** I can't actually say for sure it's our part. I don't know, but I was involved on the meetings.

**Speaker ?:** Right.

**Dave Jones:** It was amazing. It was a great thing to attend.

**Ron Demko:** Oh, that's great. So, what, did it die? Did it? No, it's fine. No? It's still fine, even though they installed it backwards? Yeah, but the derating is so massive.

**Dave Jones:** Oh, okay. It's so massive, right. 50-volt part in space that's already saying it's a, you know, it's a much higher voltage that we derated to 50 and they derated it to like one point, you know, whatever.

**Ron Demko:** So, that was part of the design process. It wasn't just luck that somebody specced in a higher voltage part. They deliberately derated it and that came in handy.

**Dave Jones:** Yes, it came in handy. That's right. It's really handy. It's kind of an extreme number of derating, wasn't it?

**Ron Demko:** Yeah, right. Oh, wow. That's terrific. And this shows the internal construction of those. Wow. Is that like a little pin in there? Yeah. Is that like a, it's got a little wire? Channel wire.

**Dave Jones:** Right. Yeah. So, the tantalum wire is, we kind of start with some length of that, then we press a pill around that. And then it's, we basically process the thing after that. So, you've got essentially a tantalum plug with, which is porous, right? And then the wire is going to be your other end of that. We'll basically form a very thin dielectric through an electrochemical reaction. And then we'll put on a counter electrode. And the counter electrode is kind of where you get the ESR. And that's where the conductive epoxy makes a big difference. It's, I don't think tantalums are going away at all. And I think tantalum polymers are going to do, have a lot of growth. They're going to do really well.

**Ron Demko:** Right. So, what's the biggest usage case for tantalum polymers as opposed to MLs? When would you want to use a tantalum instead of a whiz bang 100 mic multi-layer ceramic cap?

**Dave Jones:** Well, stability. You're always going to get stability. And I think ultimately a…

**Ron Demko:** You're talking voltage stability, temperature stability.

**Dave Jones:** Yes. Yeah, right. All of that. Time.

**Ron Demko:** Right. All of it.

**Dave Jones:** Yeah. Yeah. And now, incidentally, the tantalum polymer has just had a military spec come out, 32700. So, that kind of reinforces the known and proven history and reliability of the 55365 military tantalums and flight tantalums. So, you know, these can now be even quite high reliability devices. But the amount of cap you can get in there is quite startling. So, in the commercial world, the tantalum polymers are great for the things like, oh, I don't know, it might be the SSD drives.

**Ron Demko:** Yep.

**Dave Jones:** Tantalums or even tantalum polymers are ideal on the negative gate bias on hemp's and VDD lines where you don't want to have a bigger electrolytic.

**Ron Demko:** Yep.

**Dave Jones:** Electrolytics are fine. They could work there, but, you know, the tantalums are a much smaller package and also much more reliable. So, you'll see a lot of these in flames.

**Ron Demko:** Is that because of the sealing you can get in them? Right. In the packaging instead of like a metal can sort of like plugged, you know, because they're plugged from the bottom or whatever.

**Dave Jones:** Yeah, that's partly true. So, we make, we got Electrolytics too. And the real trick, as you say, is in the wet electrolytic is to seal that can around the bottom of it. There's a seal and, of course, the possibility for that thing to go bad. Yep. So, that's, you know, a negative on aluminum electrolytics. Of course, there's hybrid electrolytics and polymer aluminum electrolytics that get rid of those issues. But, you know, the tantalum is also inherently more reliable than the electric, the aluminum electrolytic system. Right. You know, it's funny too. Everybody calls them tantalums, but really they're also an electrolytic.

**Ron Demko:** Right. Yes. Okay. Yep. Gotcha. This, this looks difficult to manufacture. This looks tedious, I guess, to manufacture.

**Dave Jones:** Well.

**Ron Demko:** More, more tedious than any other type.

**Dave Jones:** Yeah. You've got that electro, electrochemical reaction and, and it's also well controlled and easy to put these out in the billions, I think. Oh, okay. In fact, I think there's a YouTube video on our process.

**Ron Demko:** Oh, really? Oh, okay. I'll have to try and find that and link it in.

**Dave Jones:** Yep. I'll try to find it for you too.

**Ron Demko:** Yeah. That'd be great. Okay. So, so tantalums are, you know, tantalums are the in thing, huh? Yeah.

**Dave Jones:** Well, you know, it is. And a lot of the FPGA and the real high-end processors, they're going to be using this technology because it's low inductance. It's inherently lower than the aluminum electrolytic. You could also, with the multiple case sizes, you have a lot more ease of being close to the processor, easier layout, things like that. The stability and the ESR is a great advantage. So, yeah, there's a lot of growth. It's funny because I could almost say that in the world of semiconductors, passives can tend to limit the semiconductors and performance. In fact, I can give you true examples of that. So, it's becoming quite important that you're using the right passive.

**Ron Demko:** Right. So, would anyone use a wet electrolytic for bypassing these days? I can't see why you would. I'd... For bypassing.

**Dave Jones:** Yeah, actually, I think because of cost.

**Ron Demko:** Oh, okay. Oh, well, yeah, it's going to be less than a tant, I guess, if you need like 100 mic in, you know, 10 volts or something, maybe. But...

**Dave Jones:** Yeah. Yeah, I think I repaired a hot tub board recently. So, replacing it with a tantalum, too.

**Speaker ?:** Right.

**Dave Jones:** So, no, I think it's true. The electrolytics have a lot of great uses. But I think... And although I'm not into pricing, right, I think they tend to be fairly low cost. Having said that, though, you know, the polymer electrolytes are quite good. And the hybrid ones, likewise, are quite good.

**Ron Demko:** They use those on PC motherboards. They have a big advertising thing. Polymer capacitors, you know. Our ones don't fail, you know. Our ones don't dry out and go bad, you know. Right. That's a big deal.

**Speaker ?:** So, yeah.

**Ron Demko:** That's a big deal. It's a huge sales thing on every computer motherboard advertises that they use polymer caps, you know. Yeah. Yeah. It's crazy. I guess they've been burned too many times in the past.

**Speaker ?:** Yeah.

**Ron Demko:** Yeah, you've just got so many different types.

**Dave Jones:** Yeah, sir. Yeah, it's neat because we also have a hermetic tantalum or tantalum polymer. Oh, okay. And we just achieved some flight qualifications. That's really interesting.

**Ron Demko:** How do you hermetically seal that?

**Dave Jones:** Well, we'll use a Keosura case and then process the thing like a standard hybrid. But we'll, instead of microcircuits, we'll have the tantalum pellets, tantalum polymer pellets. We've welded them into the material system, you know, into that ceramic package. And then we'll do the proper environment. There's a little bit of magic and special processes. But, of course, we'll fill it with a non-moisture type of environment. And there's an incredible performance on that part.

**Ron Demko:** Wow. Yep. Do you guys, like, where do you experiment? Because you're always, you know, you're always experimenting with dozens of different, probably dozens of different things at once. You don't do this on the production line, do you? Do you have, like, a smaller, like, R&D line? Because I assume, like, you can't just hand make these on the bench and then, oh, yeah, here we go. You've got to sort of put a bit more sort of – when you're designing a new cap like that, do you put it through, like, a mini production process?

**Dave Jones:** In the old days, we actually could kind of do it on the line. The old days being, like, 40 years ago. Okay. But I remember we came up with some types of single air caps by getting MLCC scrap from the sides of the wafer starts, grinding it down by hand, and then metallizing it. Nice. But, yeah, nowadays it's a lot different. So we've got central R&D for AVX at any rate is in Greenville, South Carolina. Then there's applied R&D and process R&D around the world.

**Ron Demko:** So you've got three different types of R&D.

**Dave Jones:** Yeah.

**Ron Demko:** So can you explain the different – what the different types of R&D do?

**Dave Jones:** Boy, I'll get in trouble because, you know – Oh, okay. All right.

**Ron Demko:** No, no, that's an internal thing. Okay, right. There's just different R&D groups. Okay. Yeah, I mean – Different specialists.

**Dave Jones:** They tend to – right. They tend to specialize with some things. But, yeah, the interesting thing is that we have multiple test labs around the world. And for a while I ran a teeny EMC lab, but that got to be so big. I think there's three of them now around the world. And then we've got far-field chambers in France and San Diego. And, you know, it's amazing. Right. It's been a ride, you know, to see from maybe two factories to, I don't know, maybe there's 40 now or so.

**Ron Demko:** So you've got EMC chambers, even far-field ones for testing your – testing caps.

**Dave Jones:** Well, that's for the antenna group. So they actually have – Oh, okay. Oh, okay. There's some really neat things we can talk about antennas. And I know we're running out of time, but maybe another one.

**Ron Demko:** No, no, no, no. We can keep going. We can go as long as you want.

**Dave Jones:** Well, there's active antennas that we have, and I don't do any work with those. But there's some really neat things that are occurring there to make miniature steerable types and tutable antennas. Okay. So that's potentially very impactful. But incidentally, we also sell the chambers. Oh, wow. Wow. Oh, gee. Yeah. Really? It's amazing how big the place is getting, right?

**Ron Demko:** But – AVX cell EMC test chambers.

**Dave Jones:** Yes, that's right. Okay. They're really neat. Hey, and the software is so easy. It's amazing when we start looking at radiation patterns of antennas. It's so complicated. And their HMI is so wonderful. It really allows even somebody like me to figure it out.

**Ron Demko:** Right. Excellent.

**Dave Jones:** Yeah.

**Ron Demko:** Oh, wow. That would be great.

**Dave Jones:** The neat thing on the antennas, though, on the passives are – although there's multiple types and stamped and all of that, ceramics. But when we could get those metalizations, imagine the 32 different IOs on a 1206. That allows us to have such metal control that we could have an antenna, service mount antenna, effectively with a very efficient counterpoise. So we might have the ability or do have the ability to have an easier keep-out area. However, the keep-out area is minimal with our device, so it's much easier to use with a good radiation pattern and all of that. That's a big problem with antennas, right?

**Ron Demko:** Yep.

**Dave Jones:** You have to have an X amount of keep-out area. It's kind of a waste.

**Ron Demko:** Yeah, it's a waste. Yeah, exactly. Right.

**Dave Jones:** So that's a big deal. Wow. Someday I'd like to show you the metalizations. It's really amazing. Oh, yeah.

**Ron Demko:** That'd be incredible. What other – oh, yeah, there's the SMD. Yeah, the SSD. Sorry, the SSD. Yep. That's one of the big applications for them.

**Dave Jones:** Yeah. So we actually rate that in terms of millijoules. Oh, okay.

**Ron Demko:** Oh, yes. Right. Yeah, because you're talking about joules of energy, right? You're talking about how much energy is required to do this X amount of processing in X amount of time. You know, so, yep.

**Dave Jones:** Wow. That's a big deal. Graceful shutdown. Yep. Yep, exactly. And then all of our sample kits.

**Ron Demko:** Oh, there's the multi-layer varista you were talking about.

**Dave Jones:** Yeah. Yeah, it's kind of neat because it looks like a ceramic cap. Yeah, yeah. But it's a zinc oxide. And remember the old radial MLVs and how those would wear out? Well, those would wear out because the grains were inconsistent. So the electric field stress would cause some to die early, right?

**Ron Demko:** Oh, really? They're just – wow.

**Dave Jones:** How would they die? That's what happened in the old days. How would they die? Oh, they'd become resistive and then flame. Yeah. Oh, my God. So the big old – yeah. Hey, I've got a great story. So I got a – I got a pin – I got an Evel Knievel pinball game for $60. Oh, no. Because they didn't realize the electric – or the MLV blew out. Yeah. And it wouldn't allow any power, of course, to the machine.

**Ron Demko:** Wow.

**Dave Jones:** So we took that out and fixed it.

**Ron Demko:** Oh.

**Dave Jones:** But anyway, these multi-layer roosters are neat because we have exceptionally tight grain-sized control. And believe it or not, they could take tens of thousands of strikes with no – wow. And it's very important because it has an advantage over a TVS diode because you could take more current. With all of those multiple electrodes, you could divide up the current that way. Right. And there's also an off-state cap. So that's something you can use in your favor because most of the time, you know, this isn't doing anything, right? Yeah, exactly. How much capacitance are we talking about? Well, it varies. You can get down to 0.2 picofurids, I believe. Yeah. But I think we are now up to 47 or 100 nanofurids. There's so many advances. That's useful. You used to be able to remember this stuff, right? Yeah. It's really useful. Right. Yeah. So like on a relay or motor drive, stuff like that. And even on can lights, that's simple, right? You can replace it with one part. I think there are arrays. There's also the feed-through filter, you know, the three-terminal part. Right. So then you get a very deep notch of attenuation because these electrodes are exceptionally highly conductive. So that's, you know, where you could increase the effective Q of that filter, right?

**Ron Demko:** And clamping.

**Dave Jones:** And then there's also a neat situation. So not to trash clamp diodes. Right. Because there's some great advantages. Right. What we're showing here is an x-ray. So on the top left picture, you've got a picture. It looks kind of like a teeny ceramic chip cap, right? Mm-hmm. And we're competing maybe against the DFN ceramics, or excuse me, diode. And if we do a top-down, center top picture shows the dye. And that's, you know, kind of shoved in between basically copper electrodes. Mm-hmm. And those heavy copper electrodes, you can see the cross-section on the right, upper right. Yep. And those actually act like heat pipes. So we can have a miniature dye that has essentially a heat pipe taking the heat out of it. And that's where we could be on the HDMI, super low-cap stuff.

**Ron Demko:** Right. So you've got higher power handling in a smaller package.

**Dave Jones:** Ultra-minusor package, right. Ultra-minusor stuff. Yep.

**Ron Demko:** Very cool. That's terrific.

**Dave Jones:** Yeah. I know you did something on heat pipes in the old days.

**Ron Demko:** Oh, yeah. I've done a couple of videos on thermal stuff and things like that.

**Dave Jones:** We're learning a lot about heat pipes and where to put them in.

**Ron Demko:** Yep. I wouldn't have thought about that from a, in that sort of package size, but it matters. Yeah, I can see how that matters.

**Dave Jones:** Yeah, and there's work being done actually on very high-power devices with heat piping as well.

**Ron Demko:** What are these RF coax things?

**Dave Jones:** Well, you know what's neat? It's the insulation displacement connector, that is. Yeah. Where you've got opposing phosphorbron tines and you don't even have to strip the wire. You just pop the wire in between the terminals and you get a gas-tight fitting. So there's no oxidation. Oh, gas-tight. Oh, okay. Wow. So, in fact, I believe they're flying on some of the aircraft that were like Boeing's, et cetera. Wow. Okay. But the RF version of that is really good for the center connector or the center conductor and the shield. So we have a non-soldering, quick, easy-to-use connector for miniature coax. Very cool. It's brutal trying to miniature coax.

**Ron Demko:** Oh, yeah, I know. Yeah, no, it's horrible.

**Dave Jones:** It really is.

**Ron Demko:** So, yeah, so you guys obviously do more than caps. Oh, yeah. No.

**Dave Jones:** And then there's some of the thin film stuff, right? We've got actually two or three thin film fabs around the world. And then there's the big heavy-duty stuff, the one that you could have for your table base, right? Mm-hmm. About this size, a couple hundred pounds. But, of course, all the different types of films. And in the world of now distributed power and green power and all of that, that's becoming quite, you know, important and useful.

**Ron Demko:** So how many different types of poly film capacitors are there?

**Dave Jones:** Oh, wow. This is tough.

**Speaker ?:** Yeah.

**Dave Jones:** I would say we're building like four. Four. And there's probably four majors out there. Yeah. Yeah. TPN, PPS, yeah.

**Ron Demko:** Yeah, yeah. It's crazy. What are the – can you give us a breakdown of when you would use the different types? I don't know if we have a slide here for the different applications for the different types of poly material. There may be.

**Dave Jones:** Basically, yeah, here we go. Sort of – I think it was sort of on the bottom of that slide. But some of it's temperature, some of it's voltage, and some of it's just case – value range.

**Ron Demko:** Right.

**Dave Jones:** Yeah, what – basically, they're not like the K of multiple thousands in ceramics. Of course, they have great other properties, right?

**Ron Demko:** You think that this is moisture? You're confident? How confident? Oh, absolutely. Absolutely. Absolutely. I'll tell you what. Absolutely. All right. I'll put them on the SEM. Oh. What would we see under a scanning microscope like that? What would we see if we did put one under there?

**Dave Jones:** I might be able to see some of the – well, certainly we'd see some of the error or the reformed electrode on the punch through.

**Ron Demko:** Okay.

**Dave Jones:** And we might be able to see some of the patterning, the failure of moisture. Right. We'd probably try to look at the things spectrographically as well and see what types of oxides we've grown. Okay.

**Ron Demko:** That's – yeah. So the moisture attacks the metal and then they form oxides. Right. Is that – Right. That's – Right. Is that how it works?

**Dave Jones:** The resistance changes. Yes.

**Ron Demko:** So with the moisture, like, it just physically eats away the metal and it just vanishes or –

**Dave Jones:** Yeah, that's basically true. It turns into oxides and we start changing resistances. Once we start changing resistances under X amount of current or voltage, now we have a different E-field. We have some heating effects that occur. Heating effects start to accelerate potentially the rate of degradation. And then if there happens to be some transient event, that could even further accelerate this thing kind of exponentially.

**Ron Demko:** But if a year-old part like this fails, is it just going to be, oh, it's just got a bad seal on it? Maybe. Is that the most likely scenario?

**Dave Jones:** I think that's true. Yes. In fact, I can tell you a fact. We've got – I think we've been building films since – maybe it was 25 years. And there's actually been zero failures. Now, dead shorts, that is, right?

**Ron Demko:** Oh, dead shorts. Okay, yes, because these are designed to fail open, right? These are classic capacitors.

**Dave Jones:** So, yeah. And some of these dead shorts would be disastrous. Imagine, you know, wheels and large compressors and things.

**Ron Demko:** So do you have any experience with the reefer caps, the paper, which they still make, don't they? I think they still manufacture. Gotcha.

**Dave Jones:** I'm going to have to claim ignorance on that.

**Ron Demko:** Okay. Oh, right. Okay. But do you know anything about the failure mode in the reefer caps? No. Okay. Because you guys have never made paper, old school paper caps like that.

**Dave Jones:** Maybe in the 70s, but that's – well, in fact, AVX was actually Aerovox. And I think there was some history. Of course, that's a long time ago. Yep.

**Ron Demko:** Of course, yeah. Anyone who repairs any vintage test gear from the – yeah, anything vintage from, you know, the 70s or 80s is – if they got those reefer caps in there, you just don't power it on because they'll explode because they've got so much moisture in them.

**Dave Jones:** I carefully cut the case and then put our parts on the inside.

**Ron Demko:** Yeah, exactly. Well, some people do that. There's people who will actually get – reefer, they'll keep the case because they want the vintage look of it. So, you know, vintage radio enthusiasts and stuff, they'll actually keep the case. They'll actually grind it all out, all the material, and they'll put a modern cap inside the actual case and keep the case just to get that vintage look.

**Dave Jones:** I do that on the old Heathcats that we've rebuilt. Oh, right, yes. Take out the old electrolytics.

**Ron Demko:** Right, yep.

**Speaker ?:** It's neat stuff.

**Ron Demko:** So moisture ingress inside a film cap can't really cause a short, can it? Is that something that you shouldn't worry about? It'll just eat away the metallization and cause a drop in capacitance.

**Dave Jones:** That's right. It's just going to go away gracefully.

**Ron Demko:** Right, okay. So many different varieties. And can you use an X-class instead of a Y-class and vice versa and stuff like that?

**Dave Jones:** Devastating. And now then you can throw the complexity of EVs. So inside the electric vehicle, it doesn't have to be ACQ200 plus safety agency rated. So it gets really complicated. I'm afraid we have to have a lawyer and a do-ass. Right. But we got the parts.

**Ron Demko:** Got it. So, yeah, EVs. So you're talking about for use in the control electronics for the actual battery pack itself, for the high-voltage battery pack, which some of them can be 800 volts now, can't they? Some of the newer battery packs in EVs?

**Dave Jones:** Yeah. Yeah. That's, there's some really impressive work going on there. And, you know, many times films are very attractive, especially as the voltage gets higher. Yep. And, yeah, that's amazing how vehicles have changed. They really have.

**Ron Demko:** Is film the only way to go for high-voltage caps? No, you would use glass. You'd have glass ones, wouldn't you, for the, like, the really ultra huge ones you were talking about, you know, the size of a cabinet? Yeah.

**Dave Jones:** Yeah. Well, in fact, there was a recent amount of work done by a university in America with a glass device for power drives. Now, I don't think it was practical or cost-effective at the point, but they have had work ongoing with that.

**Ron Demko:** Right.

**Dave Jones:** Mainly what I see is electrolytics as the, maybe I would say lower cost possibly, but I don't know if they're low cost. But they're having some practical high-voltage limitations. And I think in the future, it's probably going to be film. But it's neat because, as I said before, we're starting to do some heat piping within the, well, the formed leads, but they aren't really leads. They're actually bus bars.

**Speaker ?:** Right.

**Dave Jones:** And you can get some high-frequency response on that. You could reduce inductance. So there's a whole lot to be talked about with high-power films and how to optimize the frequency response.

**Ron Demko:** But with the glass ones, you wouldn't, you'd get very low capacitances, wouldn't you? How thin, like you wouldn't be able to make the glass as thin as you could on film caps and stuff like that, would you?

**Dave Jones:** Well, they actually talked, I believe, precipitating glass onto an electrode. So it was quite...

**Ron Demko:** As in like a sputtering thing?

**Dave Jones:** Yes. Is that what you're talking about? Something along that line.

**Ron Demko:** Wow.

**Dave Jones:** Yeah, and that's why I think it's kind of not really practical. Although, having said that, I probably made it, you know, it's guaranteed to work now. Right. But, yeah, it's funny. My first job within AVX was on glass dielectrics themselves. And we made thicknesses of about one thousandths of an inch. Oh, wow. Maybe one thousandths of an inch. You could bend them quite, you know, effectively across maybe around a six inch radius or so. Wow, really? That's amazing. Yeah, glass had a lot of advantages. It was exceptionally stable. It was probably the most reliable part out there. The K-FAC was only approximately eight. So it's not too much.

**Ron Demko:** Now, on this film here, when I first started to roll it out, it was like clear. And then, like, I started to see like a sputtering of material. And then it got more dense and it eventually reached a point. Is that because they're sputtered? Or are they actually a metal? Do they manufacture them as a film and then cut them? Like, how does that work?

**Dave Jones:** Like, in theory, I believe the consistency of the film color should be the same from the start of your DPA to the end. However, in the start, I believe it's very easy for moisture to attack that. And it's most likely because the shoopage allowed a poor, well, adhesion. And you got the moisture in at that point. Right. So I believe that's what occurred. And then, of course, as the resistance increased between the shoopage and most likely the electrode, basically that metalization just moisturized away, oxidized away.

**Speaker ?:** Right.

**Dave Jones:** It did its job on going away. So it's actually a good point, though, because you would think that the consistency of the color of the film would be the same from the start to the end.

**Ron Demko:** Yeah. Yeah. I expected just a sudden start and then boom, like, and then just hit a metal layer. And that's what you should have. Right. So is it actually a sputtering? Is it a sputtering process? Do you sputter the metal onto the film?

**Dave Jones:** Yes. And it's continuous. So you might go for, well, I'm sure it's all proprietary. So you go for a long ways. Yeah. And then you have these, it looks almost like saran wrap that's metallized. And then you'll cut it into the right width. And then you'll wind that around something that looks like a bike wheel. Mm-hmm. Well, depending upon what you're building. If you're building surface mount, you might wind it around a big diameter and then cut the.

**Ron Demko:** And then chop them. Yeah.

**Dave Jones:** I've got a graphic for that. Yeah. Yeah. And then if you're doing the power films, you might wind them into the size of a donut or a bagel or something like that. Mm-hmm. And then they could be pressed, mechanically pressed to be deformed and fit more efficiently in a square box.

**Ron Demko:** Oh, so squish them down to make a small. Yeah. That's great. That's great. So do you, is it all sputtering or do you do, are there processes and types of caps that would have a metal, you know, you would have like a roll, like you have your roll of your poly put the kettle on film and then you've got your roll of your metal film and you just wind them together. Is there any.

**Dave Jones:** I don't know of anyone building films that way.

**Ron Demko:** Were they. Okay. Not now, but did they used to do it that way or has it always been sputtering?

**Dave Jones:** I think there was some that occurred. Okay. Yeah. Right. And it might not have been a film. It may have been another material system, but yeah, that was done.

**Ron Demko:** Okay. Because a lot of graphics out there will show that they'll show like, oh, you've got a film of metal and you've got a film of. Poly and you roll them together. And I guess that's too simplistic, right? They just do that for.

**Dave Jones:** Well, I think that's not the case anymore.

**Ron Demko:** Okay. Yeah. Right.

**Dave Jones:** Yeah. And the reason would be, you know, you're, you're, you probably want a hundred angstrom on the, the electrode and the, it's going to be hard to roll that out. And you're going to have a, maybe one micron to maybe 20 or so for the film itself. So it's much more efficient to do the demonstration.

**Ron Demko:** Right. So you'd easily lose half or three quarters of your capacitance if you did it as a rolled metal. Yeah. Right.

**Dave Jones:** It'd be difficult. Yes.

**Ron Demko:** So sputtering. All right. Well, thank you very much, Ron. This has been awesome. I was completely wrong. I just went into this video with the mindset that it's all self healing and I didn't think about moisture. Well, who knew? This is going to be a surprise to a lot of people. I think that, um, yeah, it's no, no. Well, it, it, it's something to think about, um, is like, should, as electronics designers, should we avoid, you know, if we're using them in these sorts of applications, um, where like a, a capacitive dropper, should we avoid, um, like a no name brand. Um, brand sourced cap for this reason, or are they all pretty good? I don't know if I could comment on that.

**Dave Jones:** You can't comment? Okay. But I'd have to say films are a good part to use and it's probably a great application for that. Yep.

**Ron Demko:** Well, all right. It's been awesome. Thank you very much, Ron. That's been a very eye opening.

**Dave Jones:** Um, well, next time I'll turn the lights on. Sorry about that. Oh, right. Yeah.

**Ron Demko:** It's getting a bit dark. That's all right. No, we, we have been going for an hour and a half and, uh, yeah, there will be an extended version of this. So thank you very much. It's been very informative and awesome. Great. Thanks, mate. See ya. Goodbye now. Bye.

**Speaker ?:** x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
