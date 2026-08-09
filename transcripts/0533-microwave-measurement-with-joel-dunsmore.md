---
episode: 533
title: Microwave measurement with Joel Dunsmore
url: https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/
---

**Joel Dunsmore:** Real quick before we start the show, it is that time again. We're going to be doing our 2021 Amp Hour Listener Survey. We love to hear from you, hear what you think, hear what you want to hear more of in the show, and any other feedback you might have. Our giveaway this time is going to be a copy of our guest's book, Joel Dunsmore. He created the front end of the 8753, that's the VNA I've been talking about on the show here, and he has a book called The Handbook of Microwave Component Measurement that he also discusses on the show. It's the second edition. So fill out the survey, be sure to include your email address if you're interested in winning. We will ship anywhere in the world. Thanks for a lot, and we are looking forward to seeing your feedback. This is the Amp Hour Podcast. Release March 7th, 2021. Episode 533. Microwave Measurements with Joel Dunsmore. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Joel Dunsmore:** And I'm Joel Dunsmore from Keysight Technologies.

**Joel Dunsmore:** Hi, Joel. How are you?

**Joel Dunsmore:** Doing really well.

**Joel Dunsmore:** I always have these interesting feelings when people come on the show where I've read their books before, and your book is one of the subcategories where I'm not sure I understood everything. It's such an in-depth topic that I'm not sure I understood everything, but I'm really glad you're here. We can start to clarify some of these things. So thanks for being on the show.

**Joel Dunsmore:** Oh, happy to bring clarity anywhere you're clouded.

**Joel Dunsmore:** Great. Well, actually, one of the things that I'm a little clouded on is actually something you designed as well. So you are one of the main engineers on the HP 8753, which is the VNA that I have. I have the D version, but your hands are all over that machine, huh?

**Joel Dunsmore:** Yeah, I started in 1981 designing the input buffer amp as a college intern project on the receivers. And by the time you got to the 8753D, every one of the RF circuits is my design.

**Joel Dunsmore:** Wow. That's awesome. Well, I have to say, it is a great machine. One thing that we had talked about a little bit is that the APC7 connectors are, that's like one way that you can tell that it's your designs.

**Joel Dunsmore:** Yes, that's exactly right.

**Joel Dunsmore:** What is the reason for the APC7 connector? Because I think I mentioned that on the show, but maybe not the reason why it's a good fit.

**Joel Dunsmore:** Well, it's not a good fit. It's a horrible connector to use for anything practical, but it has the advantage of being the world's best connector for connector repeatability. And you have to remember the 8753 was designed before we had error correction or even computers. It's one of the first pieces of hardware that had a built-in microprocessor.

**Joel Dunsmore:** Oh, really? Oh, okay.

**Joel Dunsmore:** Yeah. The HP8510 shipped about nine months before, but that was like a collection of instruments. This was the first single box network analyzer. And it has basically a washing machine controller. And it was a four megahertz clock rate controller. And a lot of the stuff you see in the firmware is related to that. The APC7 connector was used before we had error correction. So the 8753 was designed originally, and this drove me crazy as a designer, was originally designed to not use error correction at all. To get a really good spec, the repeatability of the connector will make a difference and how stable it is. So that APC7 is a bit more stable than type N, and we can make our directivity spec maybe 3, 4 dB better by using that connector.

**Joel Dunsmore:** Hmm. Okay. So on a different machine that has a type N connector on it, what would the error correction actually be doing in that case?

**Joel Dunsmore:** Well, it would be measuring when you connect a load to the machine. The load can't connect directly if it has a gendered connector because the pin will go into the socket and have a little bit of a gap. And that little bit of a gap, we measure its response, which is going to look like a little inductance, and we essentially subtract that out with the error correction. With the APC7, if you look at the collet, it's got like a tiny little spring in there. So it's a mating connection that has zero offsets. So the shorts are true shorts. The opens are pretty close to opens, and the load has got no little inconsistency in it. So if you didn't use error correction, that would be important. But everybody uses error correction. So we could have changed, but we never did. Got it. Okay.

**Joel Dunsmore:** Yeah, and I mean, they make converters and other ways to do that. So at that point, I feel like it's kind of, you start to get into that ecosystem of just using converters, understanding that they're there and calibrating once they're on there. Maybe we could take a step back. Could you give us a broad definition of what a VNA is? I've always tried to give that definition on the show and why it's necessary and what people are using it for. But I feel like, you know, having an inventor of one, you know, a creator of one on the show is probably the best person to hear it from.

**Joel Dunsmore:** Sure. So network analyzers are not for internets. And maybe a better word for them would be component analyzers now. They're to characterize electrical circuits. And so the things you want to characterize on an electrical circuit is the gain, which is how much signal comes out compared to how much goes in. And if you've worked with antennas before, you also want to know things like the impedance. And the impedance tends to be a complex number. So a vector network analyzer gives you a vector number, which is a magnitude in a phase. And that's a complex number. So it allows you to measure networks that have complex impedances. And anything except a DC network has a complex impedance. So if you have some inductance, you get some phase angle change on your measurements. And instead of using an oscilloscope where you can measure the sine waves on the oscilloscope, but it's hard to pick off the magnitude and phase on an oscilloscope, a vector network analyzer gives you that directly.

**Joel Dunsmore:** Yeah, that's a great explanation. And I do feel like the, you know, like kind of what you were talking about with the connectors as well, everything having an impact on a measurement. Like you were mentioning the physical characteristics. That was a big shift for me is just, so my friend Jeff, who's been on the show a lot, he kind of walked me through and talked me through a lot of this, but it's just like every, everything has an impact on that complex impedance. That's going to be what you're trying to measure normally. And I didn't quite understand like how much that feeds back into systems and really can impact things. But that's really where the VNA starts to have a lot of import and a lot of, you know, you're making an antenna. You want to know everything about that antenna. You probably are measuring with the VNA.

**Joel Dunsmore:** Yes, for sure. You are as far as looking at the input match. And trying to understand how can I match it to get most of the power to go into the antenna. And you need to know not only what impedance you have, am I 50 ohms or 40 ohms, but you need to know the phase angle as well. Because if you get on the wrong side of the phase angle, you can make things much worse instead of better. In fact, in the 8753, I designed the amplifier that's in the source. It has four stages, but the first two are almost identical. And I measured them stage by stage like he did before. And each one had a two to one mismatch. And so that's pretty good. I should be able to put them together. I'll only get a dB of variation. But it turned out they were exactly opposite. I had 60B variation in the gain across the sweep. And that's what learned me up about impedance mismatch.

**Joel Dunsmore:** Right. A couple of late nights in the lab will really hammer that point home, huh?

**Joel Dunsmore:** Yeah. And throwing one design away and starting a new one.

**Joel Dunsmore:** Yeah. And the subsequent conversation with the boss about that, I'm sure.

**Joel Dunsmore:** Yes. Well, those things happened back in the day. You always did the cut and try. That was right at the dawn of doing computer-aided design. And so I was one of the first engineers in HP that actually used computer-aided design. And I evaluated every version of the ADS simulator from the very first prototype that was done by an engineer that sat just down the row from me to the final version, the ADS you have today. Wow.

**Joel Dunsmore:** That's a lot of ADS. And I'm guessing you get the benefit of not having to pay the royalty or the license fee each time as well.

**Joel Dunsmore:** Yes. Although I used to be able to get a permanent version. And now they say, now you can only get the 18-month subscription. So I had to help out with that.

**Joel Dunsmore:** Well, you know, I guess you still get the 18. You're probably good for the re-up after 18 months. Generally, they do re-up. That's great. I mean, back then, I mean, so what was the time frame of that? You said you started in 81. When were you, what was the first version of ADS that you were using for development?

**Joel Dunsmore:** Oh, God. I guess that would be about 84 or 85. It was called the microwave linear simulator, MLS.

**Joel Dunsmore:** Okay.

**Joel Dunsmore:** Then that became the microwave nonlinear simulator. My second boss, the guy's name is Dave Sherritt. Smartest guy I personally know. I mean, we hear about guys like Einstein. But this guy could do Fourier transforms in his head. Oh, my God. In fact, he wrote the time domain transform code that we use in all our analyzers today. But he got tired of working on network analyzers. And so he created the nonlinear simulator and harmonic balance simulations. So since I worked for him, he often had me evaluate this stuff. So I got a part of my job besides being a designer. I got to evaluate some of his work.

**Joel Dunsmore:** That's really cool. Yeah, I'm sure you've seen all colors of the levels of development and all the warts that are underneath the hood, I'm guessing, too.

**Joel Dunsmore:** There are a lot of warts underneath that hood. Yeah.

**Joel Dunsmore:** Yeah. And nonlinear calculations are... Are there magic numbers in there as well? Like, well, it usually does this. And you just put in a 1.7 factor here. I just always assume there's something like that underneath.

**Joel Dunsmore:** There are some things in some of the transformations we did to make them match up with the older equipment.

**Joel Dunsmore:** Ah, yeah.

**Joel Dunsmore:** And sometimes you have to, even in our instruments, sometimes we do some things and you say, ah, that doesn't make sense to do it. But you need to do it in order to have the same answers that you used to get with the analog equipment.

**Joel Dunsmore:** Yeah, yeah.

**Joel Dunsmore:** We get that in the spectrum analyzers, for example.

**Joel Dunsmore:** Oh, yeah. Okay.

**Joel Dunsmore:** There's a thing called Danil displayed average noise level. And it used to be that the logging circuit that changed the voltage to dBs happened before the display. And so if you did it that way, you get a 1 dB lower reading than if you average the power first. And averaging the power first is the right way to do it. But nobody wanted to take a 1 dB hit on their spec. So all the instrumentation manufacturers define Danil as log first, then average.

**Joel Dunsmore:** It's art imitating life, imitating art, kind of one of those things.

**Joel Dunsmore:** Roughly speaking.

**Joel Dunsmore:** Yeah, that's great. Oh, wow. Yeah. I mean, that's amazing because that shows how much, especially in the test equipment industry too, like spec is just like everything. It's that spec sheet that's going to drive how much time you spend on the next feature and like how many times you test something. And it's just, yeah, it's a crazy game to play in.

**Joel Dunsmore:** And what you do in terms of measuring and correcting, one of the things that's happened in modern equipment is we do much more corrections in our instruments now than we ever did before. What do you mean by that? So, well, of course, we measure the frequency response and we correct the frequency response, but now we're doing nonlinear corrections in our instruments. So we're trying to measure the nonlinear characteristics. We build nonlinear models.

**Joel Dunsmore:** Uh-huh.

**Joel Dunsmore:** One of the guys that sits across the way from me, a guy named David Root, invented something called X parameters that are used for nonlinear modeling. So we use that applied to our instrumentation so that we can drive the sources and receivers harder than you normally would and still get a good result.

**Joel Dunsmore:** Okay. Yeah. And that makes sense. And that probably, is it because you're dealing with kind of the perfect nature of a model kind of hitting the real world? Is that kind of the, I call it fudge factor normally, but I don't think people like to call it that.

**Joel Dunsmore:** Well, it's not exactly a fudge factor, but if you're driving an amplifier into compression, so, you know, it's going to clip the top of the waveform. Right, right. If you have the circuits that can drive the peaks of the waveform a little harder, so when the amplifier clips it, they show up to be the right level, then that's how you can restore a linearity.

**Joel Dunsmore:** Got it. Yeah. And, yeah, if it's repeatable, if you can prove it's repeatable, too, it's like, then what's the problem there? I would imagine that that's...

**Joel Dunsmore:** Oh, and, of course, we have to characterize it over temperature. When it's not repeatable, so we can know, okay, at this temperature, we should use this factor.

**Joel Dunsmore:** Yeah. Well, speaking of corrections, let's talk a little bit about calibration, because that's another thing that, as I got started with my VNA, I ran smack into a lot of strife. What is a calibration on a VNA, and, like, what is it necessary for, and how do people get it wrong?

**Joel Dunsmore:** So, calibration is basically you measure something that you know its true value, and then you just correct the readings to get the true value. And for vector analyzers, to do impedance, you need to have three true things. So we usually use an open, a short, and a load. And the biggest mistake that we made as an instrumentation manufacturing is facturers calling them an open, a short, and a load. If we would have only called them an offset open and an offset short back in 1972, or whenever it was first invented, we would save so much grief from people saying, I put my short on and it's not a dot. Why is it not a dot? All of our opens and shorts are offset, so they all have a little arc.

**Joel Dunsmore:** That's like a physical characteristic, you mean, is an arc? Right. Oh, the arc is the thing that shows up on the VNA.

**Joel Dunsmore:** The arc is the thing that shows up on the VNA. They show up as a, if you look at the phase, the phase of a short is not 180 degrees. It starts at 180 degrees, and it goes to, you know, swings around 15 or 20 degrees more. The opens are even more a problem because the open circuit actually is a capacitor. If you think about it, you cut the end off of a piece of coax, it's got something we call fringing capacitance, and that adds an extra amount of phase. So when people look at the phase of an open, they expect it to be zero degrees, but it's 15, 20 degrees as they go up in frequency, and they yell at us, how come it's not the right answer? I had a professor that insisted an open had to be an open, and how could it have any phase? Hmm. Sometimes you just tell them how to fix it. You say, oh, well, you can make this adjustment, and it'll turn it to zero. It won't be the right answer.

**Joel Dunsmore:** Right, right. It'll look as it appears in your head, huh? Exactly. Interesting. And so people are using this. So basically, this is to get rid of stuff that's internally happening in the VNA. Is that right?

**Joel Dunsmore:** Mostly, it's to get rid of stuff that happens between the VNA connection and the thing you're trying to measure. You got your PC board with your little RF amplifier you want to test, and you want to know the input impedance of that RF amplifier. You're going to connect it to the VNA through a test port cable. And cables are horrible. Cables, I say in my book, cables are like dogs. Either they are bad, they've been bad, or they're going to be bad. And if they happen to be good, they only stay good with great care. So you have to be really careful with cables. You put a bend in them, it changes their impedance. And that's usually what we're calibrating out.

**Joel Dunsmore:** Yeah, and I guess one of the things that I learned later on, for some reason, it just never really stuck until I was doing cable stuff too. It's just like the idea of just a coaxial cable, and that there's an insulation between where the cable is, and then the ground around the cable. It's just this consistent amount of stuff between the conductor and the ground all the way through. And for some reason, that never really sunk in. So then when I was bending stuff around, it's like, of course, you're putting stresses on these things. I mean, there's an effect too, like a pyroelectric, but what is from actually flexing a cable as well, that actually impacts how the signal response is throughout these cables?

**Joel Dunsmore:** Well, one of the things that happens when you flex the cable, you squeeze that dielectric. That's what we call that insulator in behind, dielectric. And the dielectric constant is the ratio of the E field to the H field in the cable, roughly speaking. And so as you squeeze it, you can change this dielectric constant a little bit. But also, when you bend the cable, the outer conductor kind of pushes up, the dielectric pushes down. And so you're actually changing the inside dimensions of that cable. And the impedance of a cable is directly related to its dimensions. So that's usually what you're doing when you bend the cable is you're physically changing its impedance. Now, if you look at what's called mainline cable that the cable TV guys use, and I worked with a lot of cable TV guys. I've been to their factories where they have a tunnel that's a mile long, and they send an extruded piece of metal down a mile to another building a mile away. Then they draw the dielectric through by having, they call it a mouse, but they basically tie the dielectric, which is plastic, to a, essentially like a little cannonball. And they shoot it down a mile with compressed air, and it pops out the other end, and they drag the dielectric through. And then they do the same thing with the center conductor. And they pull this whole thing through a kind of a fixture that compresses the outer conductor to the center conductor. And they wind it around big reels. And you've seen those big reels on the back of the cable TV trucks.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** So this is all done in the south in Carolina and Tennessee, where they got lots of cockroaches. So a cockroach lands on that big pulley where they're wheeling it around, and it puts a little ping, a little dent in the outer conductor. And they can tell by looking at the impedance versus frequency, they'll get a little spike at one frequency. And they'll say, oh, yeah, we got a problem with the pulley number 17, because that's the size of the pulley. Right. So those are the kinds of things you have to deal with impedance and mismatch.

**Joel Dunsmore:** Right. And so in those cases, I mean, well, obviously, that's like a high power, high accuracy kind of thing as well. I mean, would someone like... It's super low loss. Yeah, yeah. Would someone like that then go and remake the cable in that case? Or would they be able to correct for that?

**Joel Dunsmore:** Depends on how bad it is. Sometimes they can find out where it is and just cut that bad piece out. But if it's one of these things that happens every one meter for 1,000 meters, they throw that away.

**Joel Dunsmore:** Got it. Yeah. Yeah, I mean, right.

**Joel Dunsmore:** These cables are something like, you know, a dB per 100 meters of loss. So a 1,000 meter cable will only have 10 dB of loss. The cables you buy or that you have at your lab are probably a dB in one meter. So they're 100 times more lossy.

**Joel Dunsmore:** Just because of the cost and the process control, that kind of thing?

**Joel Dunsmore:** Yeah. And it's basically the inside material because these things are sometimes they're even silver coated on the inside to get the best conductivity. Power loss is a big thing in that world. Also in the SATCOM world, you know, they want to have super low power loss. So remember you talking about filters on your show and the cone line filters you saw on your transponder. Those things are all silver coated on the inside.

**Joel Dunsmore:** Yeah, that was Dave talking about the airplane transponder, I think. He had cracked one open.

**Joel Dunsmore:** Yep.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** And they do look like magic. I remember him saying something about having it just the center conductor goes to ground inside. So how does the thing work? Yeah.

**Joel Dunsmore:** How does that thing? Joel, how does that work?

**Joel Dunsmore:** It's all about length. The, what happens is that center conductor goes into the, is just a wire passing to probably have a little piece of Teflon. So it's like a wire that passes through the body and then shorts to the ground inside. But that length of line that it's shorting to is exactly the right length to form essentially a shorted half wave antenna. So it's a probe essentially. It's a little antenna that's going to generate. Because how does an antenna work? I mean, it's just a wire that's open at the end. But if it's the right length, you can stand a wave on it. And so that's generating a little electromagnetic field. And each one of those combs in there is a little resonator that's just coupled to that magnetic field and coupled to each other. So that's how it works. It's all length. That's really the difference between low frequency and RF is the length means everything in RF.

**Joel Dunsmore:** Yeah. Yeah. Yeah. And I mean, again, it comes back to that physical. I mean, you'd mentioned the cables already. And we talked about the connectors and now the comb line filters and everything. It is just crazy to me that how much the mechanical aspect and the length that you're talking about, how much that impacts things. I mean, it really is just the natural phenomena of resonances that ends up creating all these interactions. I guess I still don't have an intuitive feel for it. How does one gather that intuitive feel?

**Joel Dunsmore:** Well, if you do any radio work, you kind of get a sense by the size of the antenna that you're using. So if you look at a cell phone, you know, or the old, you know, Ericsson cell phones had that little pullout antenna. So that was a wavelength long quarter waves antenna. So anything that's a big fraction of that is going to affect the signal. You can kind of have an idea as you go. 5G is the new thing and it happens at a much higher frequency, 10 times the frequency of cellular. So for a 5G system, you know, something that's only one or two centimeters long will have a huge impact on the signal. Hammer radio. I was a hammer radio operator for years. So if you have an 80 meter system, you know, your wavelength's 80 meters. Ah, what's a meter here or there? It's not going to matter. A few degrees.

**Joel Dunsmore:** That's right. That's right. When you're throwing your antenna up over a tree, you're probably not dealing in centimeters.

**Joel Dunsmore:** Exactly so. The cell bands are what we used to call microwave bands back in the day. But now that's just considered run-of-the-mill RF. Yeah.

**Joel Dunsmore:** Yeah. Where do you put the line for microwave these days?

**Joel Dunsmore:** Well, it's very clear. The line is exactly 6 gigahertz, the maximum frequency of the 8753. That's the definition of RF is what the 8753 can cover.

**Joel Dunsmore:** Got it. Got it. Pass that. And well, it does seem like pass that and the price goes up for sure. So that seems consistent at least.

**Joel Dunsmore:** Also true.

**Joel Dunsmore:** Yeah. I mean, the cables especially, again, back to the physical side of the thing. I remember Sharia from The Signal Path. He shows some things where he's just like, I think he was at a trade show and he was just like fawning over these cables. And then I was like, oh, they must be great cables. I went and looked them up and I'm like, oh, yeah, wow. The price shows that those are great cables. You know, it's crazy how much that stuff matters.

**Joel Dunsmore:** I mean, it's not unusual to pay $1,000 for a microwave cable. Yeah. And they're good until you hang something off of, you know, you connect your cable to your instrument. You connect it to something. It bends over the edge of a cable and puts a little thing in the cable. And now that $1,000 cable is no good.

**Joel Dunsmore:** It's great to tie your shoes with though then. I mean, you can do a lot of, you can give it to your cat if you want to. You know, like there's just really a lot of other things there.

**Joel Dunsmore:** My boss actually took a picture of a couple of guys at one of our customers taking a network analyzer out of the trunk of their car by pulling it out by the cables and holding it by the cables.

**Joel Dunsmore:** Oh, ouch.

**Joel Dunsmore:** Those are easily $1,000 each cables and I don't think they would be good anymore.

**Joel Dunsmore:** Why were the cables even plugged in when they were moving it? That's another crazy thing. It just seems like you're going to start knocking things sideways.

**Joel Dunsmore:** They were movers, you know, they're movers, they're not engineers. So they were told here's a piece of equipment. It has to move and the cables were cooked at the time. So they just said, well, this will be an easy way to pick it up. We'll just pick it up by these. That's horrible.

**Joel Dunsmore:** Wow. Wow. Well, so you mentioned the six gigahertz limit on the 8753. I mean, obviously time marches on, technology marches on and it is not six gigahertz limits anymore. I mean, the 8753 is still, but what is the upper end of VNAs these days? Like what is the high end that people use?

**Joel Dunsmore:** If you're talking about a single box instrument, we make something up to 70 and we can even extend it to 72 gigahertz for a single box instrument. Once you get above the 70 gigahertz range, then we start to make what we call millimeter heads. They're millimeter because that's the millimeter waves. Anything above 30 gigahertz is considered a millimeter wave. But in the bands of 70 to 120 gigahertz, we make these little heads that go on the network analyzer. And you almost have to do that anyhow, because at those frequencies, the loss is so great. If you put a one meter cable on at 100 gigahertz, you wouldn't have any signal left coming out of it.

**Joel Dunsmore:** Yeah. So, yeah, that's... And like what are the... I mean, so you mentioned 5G and it seems like there's some frequencies up there. Who else are using these kind of 100 gigahertz type of VNAs?

**Joel Dunsmore:** Well, of course, there's 6G that's supposed to go up to 300 gigahertz and we're starting to do a lot of work on that.

**Joel Dunsmore:** Oh, wow. Yeah.

**Joel Dunsmore:** SATCOM uses that for satellite to satellite communications. It uses the higher frequencies because the atmospheric absorption protects those signals from being intercepted.

**Joel Dunsmore:** Yeah. Just because of like where water resonates and stuff like that?

**Joel Dunsmore:** Exactly. It's actually water absorption and other oxygen absorption that will absorb those signals. That's why most satellite communications is actually below 50 gigahertz because that's where the absorption function starts to increase. Although they're pushing that up now. I just heard a SATCOM band goes up to 53 gigahertz. So our newest network analyzers, instead of stopping at 50 gigahertz, we push them up to 53 gigahertz for just that reason. So you can get a handheld, you know, we call it a streamline, but it's a handheld USB powered network analyzer to 53 gigahertz now. Sounds affordable. You know, it's probably not that much more expensive than your 8750 3D was when it was brand new.

**Joel Dunsmore:** That's true. That's true. Mine was made in 96. You would ask me this by email and I don't know the serial number offhand, but I know when the screen pops up, it says 96.

**Joel Dunsmore:** Okay. So is that older than you or younger than you?

**Joel Dunsmore:** That's that is about 10 to 15 years older than me. So, yeah, I was definitely a middle schooler when this thing was. I was not thinking about signals when when this thing was came to life.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** I think I maybe got my first walkie talkies around that time. So, yeah. Perfect. Yeah. Yeah. But my interest in RF peaked started, I guess, but not peaked started then. Okay. So so the the 53 gigahertz and that realm of things, I mean. Can you give us a relative measure as well? I mean, like, like what is the expected losses say like a satellite to satellite? It's you know, there's not much. There's no atmosphere up there. But like even even over that distance, how much loss do you expect when you're doing a satellite to satellite communication link using that? Do you expect like 100 dB losses or what do you expect?

**Joel Dunsmore:** Well, it all comes to the beam shape, right? If you have an anisotropic. Well, of course, in space, there's no losses, just, you know, steradians is what they're called. You know, four pi r squared. The signal goes out. There's not much loss in space at all. So it just radiates uniformly. And then you will beam form that. All these satellites have big beam formers. If you've seen the Starlink tear down, it has that big pizza box with a thousand elements. I saw that a few years probably before you did. But those are each one of those elements is kind of aligned to point in one direction. And if you can get it, so it all comes down to how narrow you can make your beam sense how much loss you have.

**Joel Dunsmore:** Got it. So it's like the expanding cone of diffusion of signals or that kind of thing.

**Joel Dunsmore:** Exactly.

**Joel Dunsmore:** You make the cone narrower.

**Joel Dunsmore:** Just like shining your flashlight at night is very bright. When you shine it on the ground close to you, you try and spotlight the tear. Right. It gets pretty diffuse. Right.

**Joel Dunsmore:** But if you can get a laser pointer, you get a lot much better shot at pinpointing something.

**Joel Dunsmore:** Collimated beams. They make a difference.

**Joel Dunsmore:** Got it. Okay. Yeah, that's interesting. So then, okay, so say it is a beam instead, you know, beam formed. What are relative losses then? I mean, again, I just don't really have a good intuitive feel for any of this stuff.

**Joel Dunsmore:** So I'm working on a little phased array antenna test methodology right now. And I have a 64 element phased array antenna that I got from a fellow named Professor Rabiz at University of San Diego. He's one of the leading lights of phased array stuff. I've been working with him to do some testing. I have what's called a horn antenna, which has about 24 dB a gain. I have this phased array antenna, and the loss between them one meter apart at 39 gigahertz is about 25 dB. So that's one meter.

**Joel Dunsmore:** Okay. So a little bit more for satellites that are flying around the Earth.

**Joel Dunsmore:** So if you're going to have 100 kilometers, you've got to have a lot more elements to make that beam a lot more tight so you can get what we call antenna gain. Yeah. That's why 5G, you'll always hear people talk about 5G with MIMO, but also with what they call phased array or beam steering, because there's just too much loss. You can't afford to transmit energy omnidirectionally. You have to focus the energy on the user. So these 5G applications, they actually have to know where you are and point that beam to you and track you out.

**Joel Dunsmore:** Hmm. Yep. Yeah. And that's, it seems, I mean, I know it's possible. Obviously, I've seen a lot of phased array things out there, but it still is crazy to me thinking about like it. I guess it happens even with 4G towers that there's some amount of beam forming, but like, it's still like my brain boggles when I think about that. Like, oh, they're just pointing a beam at me from wherever, you know?

**Joel Dunsmore:** Yeah, I think the 4G, they have maybe six beams per sector, something like that. And these 5G stuff are going to have hundreds of beams per sector. So that's the thing that really boggles my mind is the digital processing behind that to take all these signals and know who needs to be separated and who needs to be pointed which direction and then put it all together. So when the antenna is hit with a signal, it points out 17 different beams in 13 different directions.

**Joel Dunsmore:** Yeah. And all that just so people can, you know, watch a YouTube video.

**Joel Dunsmore:** Watch a YouTube video while they're driving. That's the answer.

**Joel Dunsmore:** That's right. Yeah, exactly. I mean, that is kind of, it bugs me sometimes thinking about that. Usually the one that my brain switches to is just like all this advanced technology and it's just people on Tinder swiping right and left. And it's just like, oh, man. I wouldn't know about that. Well, I mean, just, yeah, just broadly as like, you know, that's what the human race comes down to is just serving commercial needs that are the same commercial needs that we've had for millennia.

**Joel Dunsmore:** All right. So you have your finger on the pulse of the nation. Which uses more bits, cat videos or Tinder?

**Joel Dunsmore:** Oh, cat videos for sure. Yeah. Yeah. Yeah. I mean, just because it's video, you know, multiple frames. So, yeah.

**Joel Dunsmore:** And especially if you're a picture of a lawyer turning into a cat.

**Joel Dunsmore:** Oh, yeah. I mean, yeah. So that just happened here. That was a great video. I'm sure people have seen that. But if they haven't, look up a cat Zoom call or something. Oh, my God. Best video 2021 so far. So these are obviously tools that people are using to measure things like satellites and similar. I mean, let's get back to the actual, the device itself, the VNA. I mean, what happens on the other side of that connector, right? So we've got the APC7 or we've got whatever the new type of connector is on there. What is behind that? What is inside the box?

**Joel Dunsmore:** So it's inside the box. The first thing is the signal source. You have to create a signal. Usually it's a CW signal, but the modern ones can do other things. You create essentially a sine wave signal. CW means continuous wave. But in fact, it's not continuous. We sweep it in frequency. We sweep it in power. And usually on these networks, you want to measure its characteristics as it changes frequency. The biggest thing they're used for is like testing filters and making sure the filter is rejecting where it's supposed to reject and passing signals where it's supposed to pass a signal. And that signal source then goes to what we call a signal separator or reflectometer. And because of the way RF signals work, you can't really have an open or a short. So you can't do the traditional electrical engineering of, you know, what's the short circuit measurements or open circuit measurements. You have to do it in what's called a constant impedance environment. So we use something called a directional coupler that can measure how the signal is coming out of the source. And a second directional coupler that can measure how much signal is reflecting from the device that we're trying to measure. And by taking that ratio of the signal that comes out of the source and the signal that comes back from your device, that ratio tells us the impedance. So the basic network analyzer is a signal generator, dual coupler or reflectometer. And then on either side of those couplers, you have to have a receiver. And the receiver has to be coherent so that when it sees a signal, the two receivers, one for the reference or the signal source and one for the test signal, it can compare the amplitude and phase. So a signal source, directional coupler and vector receiver are the three big pieces.

**Joel Dunsmore:** Yeah, that's a very succinct definition of it. I like that. I mean, it's I compare that again to, you know, Shariar is my video reference for all these things to the signal path. And it's just like, you know, he opens up a box and I'm just like, oh, you know, and he's able to call out the different sections within that. You know, he's obviously seen a lot. I'm sure I know you have seen a lot as well. But again, it's just like it looks like a treasure map to me when you look at like a circuit board on a on a modern VNA. It's just crazy.

**Joel Dunsmore:** Oh, and the things. So that sounds really simple. But the things you have to do in order to get the power to be super flat, you know, people want a tenth of a dB precision across zero to 70 gigahertz. They want the signals to be clean. So in our high performance VNA, we call it the PNA. We have 33 bands of switch filters to clean up the signal.

**Joel Dunsmore:** Oh, wow. OK.

**Joel Dunsmore:** And that's a micro circuit. It's a gold brick. Essentially, let's say six inches wide and a foot long with 82 DC feeds to control all that stuff. That's the most expensive single circuit we've built in Keysight.

**Joel Dunsmore:** Wow. That's. And so the filters then are are basically is because because of how a signal coming back through at like 36 gigahertz or some random random frequency might resonate with other things. Within the circuit. Is that is that the thought or why are there so many filters in there?

**Joel Dunsmore:** So our customers want us to put out a signal that's got no other signals associated. If we put out a 10 gigahertz signal that can't have a 30 gigahertz harmonic or a 20 gigahertz second harmonic, it can't have spurs. And the reason they don't want those is because they want to make sure that what they're measuring is coming from their device only and not coming from the test equipment. Hmm. And so trying to make such a clean signal just coming out of an oscillator is really difficult. And people want like one part in a million in terms of error signals. So we have to go to a lot of effort to get those things cleaned up.

**Joel Dunsmore:** Got it. OK. So so as it's sweeping through different frequencies, a new spurious signal might pop up during the generation of that. Is that part of why the filtering happened? Exactly. OK.

**Joel Dunsmore:** The oscillator might generate it. And also sometimes our oscillators are banded. So maybe it goes from two to four gigahertz. And then we have to go through a times two multiplier to get four to eight gigahertz and through another multiplier. And each of those multipliers generates their sets of harmonics. So we have to clean all that stuff up. The reason they want it clean is because if you have a cell phone receiver, let's say it's got a specification that says, I need to be able to receive a really weak signal in the presence of a strong signal. So they need to provide while they're testing these things exactly precise signals. And if those levels are off at all, their unit won't pass their production tests. And we'll hear about it.

**Joel Dunsmore:** Right. That's right. Yeah. Well, I think that's, again, all the complexity that you've explained so far. I mean, it also just points right back to the fact that it's very difficult to make this stuff in the first place and even more difficult to make it cost effective. I mean, it's just, I mean, it is cost effective as it is. I just imagine from the scale required. And it's just, it sounds like a really tough problem to do, to solve.

**Joel Dunsmore:** It really does come down to scale. And you'd be surprised if you go, you know, to the overseas manufacturers, if we can improve something a little bit, they will pay for that. You'd think nobody's going to pay a lot of money in manufacturing for this equipment. But if they can speed a test up because they don't have to dodge a signal that's a bad signal, that is all real money to them. And they know, they know the cost of tests down to the cost per microsecond.

**Joel Dunsmore:** Got it. So you're saying like handset manufacturers, similar, similar kind of things there.

**Joel Dunsmore:** Yeah. And go one step below that, the component manufacturers. So you talked about, I know on an earlier show, a regulator for a penny and capacitors that cost less than a penny. And those all have to be tested. And so you're doing a million capacitors.

**Joel Dunsmore:** Right. Times however many billions are made a day and on and on and on.

**Joel Dunsmore:** Yeah. I think it is billions a day too.

**Joel Dunsmore:** Yeah. Oh, yeah. Yeah. Hmm. Well, that's great. And I mean, yeah, I mean the process efficiency type stuff too. It's just like the combination of expensive machine that needs to go and test many different things. Yeah. It's quite an equation, like you said, quite an equation to solve.

**Joel Dunsmore:** And that's one of the things that's changed in the world of network analyzers. It used to be you'd build a test system with a switch in a spectrum analyzer. You're switching a signal generator, maybe switching a noise figure meter to do your testing. Nobody wants to do that. They want one piece of equipment that can test everything at the same time.

**Joel Dunsmore:** Got it. Got it. So then do they, is it like the VNA or the network analyzer is plugging into like a test head or something like that so that it can switch to all these things?

**Joel Dunsmore:** It's exactly like a test head. If you've ever seen a wafer prober probing a digital wafer, the RF wafer probers look the same except they have some RF cables that go onto them. And they touch down on their device and they want to measure everything and they want to measure it all in zero time.

**Speaker ?:** Right.

**Joel Dunsmore:** Yeah. Yeah. I mean, so you mentioned spectrum analyzers. So then how is a spectrum analyzer different than from a network analyzer?

**Joel Dunsmore:** So the principal difference, of course, is it doesn't have a source because it's only measuring signals.

**Joel Dunsmore:** Mm-hmm.

**Joel Dunsmore:** Spectrum analyzers traditionally would have some kind of a hardware swept filter that would sweep across the spectrum and remove signals from the detector. So it's essentially a sweeping filter with a detector. But some of the modern measurements you need to do, you need to, the filters can't sweep fast enough or can't be wide enough. So they have removed that filter and use digital techniques. And that's what we do in the P&A, which has our network analyzer, the vector network analyzer with a built-in spectrum analyzer option, essentially uses a digital filter, complicated digital filter, complicated algorithm, to pick out what's the true signals from the signal that we're measuring. So a network analyzer really has the same hardware as a spectrum analyzer plus a source and a reflectometer.

**Joel Dunsmore:** Right. Right. You have to be able to switch that source in. And I think Alan Wolke, who we've had on the show before, I think he showed on YouTube. Again, YouTube is my reference for a lot of this stuff. But he showed actually how to do this stuff with, I think, like a cheaper scope and a signal generator, just like the basics of it. And it was great to see, like, to understand how signals have to switch in, how you have to, you know, sweep across frequencies and all that stuff. And it's very non-trivial in order to get a signal injected into a circuit you're also trying to measure at the same time.

**Joel Dunsmore:** Yeah. Part of the problem is you have to, and this is actually where the RF is different than a lot of other things, is in the RF, we define the input and output to be this 50 ohm impedance. Typically, it's 50 ohms. So the test equipment, if it has that same impedance, it doesn't affect the behavior. Whereas if you've ever put an oscilloscope on a circuit and the circuit works when the oscilloscope is connected and you disconnect it and it doesn't work, that's because the impedance loading is maybe stopping that amplifier of yours from oscillating.

**Joel Dunsmore:** Hmm. Yeah. And that, I, uh, test, test equipment impacting circuits is, uh, is a pastime of mine. Yeah. And also, uh, hair tearing. I think that's also usually goes along with that. So, yeah, that's great. So you'd mentioned like how things impact things, but what about like, uh, how noise impacts it then as well? Yeah.

**Joel Dunsmore:** So we have kind of two aspects of noise that we usually deal with. One aspect is, we call it KTB noise or Boltzmann constant noise. It's just everything is warm. So if something is warm, it produces a voltage and a noise voltage. And, uh, our receivers produce their own noise. We try to make them as low as we can, but they do produce noise. The circuits produce noise. And, uh, we measure that with something called noise figure. So it's a way of evaluating things like amplifiers and receivers. And you say the lower the noise, you'd like it to be zero dB, but even a zero dB receiver doesn't have zero noise. It just has the noise of a thermal noise. And that still impacts the, how well you can receive something. So what do they do when they want really low noise?

**Joel Dunsmore:** Make it cold.

**Joel Dunsmore:** Make it really cold. And I've been working with, uh, different groups of different universities that are trying to do a millikelvin temperature network analysis. And that's just a whole, a whole nother challenge where it might take you a day to connect your open. You connect your open, you bring the cryostat down to cold temperature. It takes eight hours. You measure it.

**Joel Dunsmore:** That's to be the nature gender helium vendor to those folks. Just make money hand over fist. It's horrible. It's horrible.

**Joel Dunsmore:** That's, that's not a job I would enjoy. You have to have a different kind of patience to do that.

**Joel Dunsmore:** Yeah. Yeah.

**Joel Dunsmore:** Millikelvin.

**Joel Dunsmore:** Yeah, it's crazy.

**Joel Dunsmore:** And then the other noise we deal with is something called phase noise, or you might call it jitter in a digital circuit. And it's the fact that things happen at times that you don't think they're supposed to happen. So you're generating a clock signal to drive your digital circuit and you think it's 10 megahertz, but sometimes it's 9.99 and sometimes it's 10.01 and it wiggles forth and back. And, uh, that can cause problems. If you have high speed circuitry or you're trying to generate signals for communications, if, uh, those clock signals wiggle back and forth too much, you lose track and then you can't, uh, can't lock on your signal. Hmm.

**Joel Dunsmore:** Yeah. Yeah.

**Joel Dunsmore:** And that's what causes the problem when you're talking on your phone and you're driving too fast away from the, uh, cell station, it can't track you out. So the frequency shift associated with the speed is another issue, but the noise impacts that as well.

**Joel Dunsmore:** Well, interesting. Could you, could you talk a little bit more about that? I mean, obviously I've experienced that and I've, you know, I kind of understand it, but like, what, what do you, what do you, what is the physics happening there?

**Joel Dunsmore:** So there's two kinds of physics happening. One, one is the noise aspect where the, uh, station has to figure out what frequency you're transmitting because you guys don't have a common clock. You got a little crystal in your phone. It's got a crystal in the base station and they both think they know what frequency is, but it's not the same. So part of the protocol of making the connection of the call is it says, what frequency are you at? And figures that out as you drive around and as your cell phone, you know, gets hot or cold or moves in different places, its frequency shifts a little bit. If it shifts too much, that can cause you to drop a call. But the most common thing that causes you to drop a call is what we call multi-path. The signal coming to your handsets bouncing around the room and it's adding and subtracting to itself all the time. And when you move into a spot where two signals of the same size cancel each other, all of a sudden the phone goes dead and you're like, what happened? I have a dead zone here.

**Joel Dunsmore:** That's the, uh, the, I'm, I'm walking into an elevator problem, right?

**Joel Dunsmore:** The elevator problem is slightly different.

**Joel Dunsmore:** Oh, is it? Okay. Okay.

**Joel Dunsmore:** Walking into the elevator is you're going into a Faraday cage. So you're essentially shielding yourself.

**Joel Dunsmore:** Got it.

**Joel Dunsmore:** And you heard of like wifi with MIMO. The whole idea of MIMO is you've got multiple antennas. So each antenna is receiving physically in a different location. So it's physically receiving a slightly different version of the signal. Maybe one antenna has got the signal that's bounced off the refrigerator and another antenna has got the signal that's bounced off the television. And the hope with MIMO is at least one of those antennas is going to pick up a signal strong enough to keep the communications path open.

**Joel Dunsmore:** Right. It's spreading the problem around, huh? Exactly.

**Joel Dunsmore:** Yeah. Or actually avoiding deep holes.

**Joel Dunsmore:** MIMO is multi-in, multi-out. What is the number of transmitter receivers that you expect in a MIMO system in 2021?

**Joel Dunsmore:** Oh, you know, it depends. And some of these backhalls are going to big numbers, 16 up to 64, I've heard. I haven't actually seen that. But we've had people that have asked us to make 64 port network analyzers to test 64 port antennas. And I think those are going into MIMO systems.

**Joel Dunsmore:** Wow. That sounds like a salesperson's dream.

**Joel Dunsmore:** Those do come a bit dear.

**Joel Dunsmore:** Engineer's nightmare, of course.

**Joel Dunsmore:** Not so bad. You make a really good two-port one. And then you... So we switched to a thing called... Or recently started making a lot of instruments in PXI. That's a modular instrumentation. So you make a really nice two-port PXI analyzer. And you slot in 32 of them into a couple of chassis. And you have a 64-port network analyzer just like that.

**Joel Dunsmore:** Hmm. Okay. And in that case, would you have like... So if it's like a 64-port MIMO thing, it would be 64 cables as well going to 64 elements onto like a PCB antenna or something similar? Or what does an antenna look like in that case?

**Joel Dunsmore:** Yeah. So these are ones I've seen are base station styles. So they're maybe, you know, 10 centimeters by 50 centimeters, something like that. And they are... They'll have 64 blind mate connectors on the back of them. The instrument will have... Will sit on a rack next to the test fixture. They'll have 64 cables that go to these blind mate connectors. Then you have to do 64 sets of calibrations on the end of each of those cables. So they'll have a robot that'll hook up the open short loads to the ends of the cables. And then they snap on this antenna onto all 64 blind mate connectors and measure it all at the same time.

**Joel Dunsmore:** I would love to see that. A robot putting on... I mean, putting on the calibration. That's... I mean, that's crazy to me. Like the robot handling... Like actually screwing on SMA or whatever the equivalent would be.

**Joel Dunsmore:** Well, it's better. I was with one customer down in the Southland in Los Angeles. One of the big aerospace defense customers. They were doing a satellite system that had 30 inputs and 30 outputs. And they had a guy in there. Screwing on the open shorts and loads. That would take him something like two weeks to do the full calibration. Because he had something like 900 paths that we were measuring. Just really from every port... Every combination of every port to every port.

**Joel Dunsmore:** Not to mention the carpal tunnel from just screwing things on and off so many times.

**Joel Dunsmore:** It's crazy. Crazy. And so, of course, they asked us to help him out with that problem. And we developed a system that could knock that down by like a factor of 100. So they could do like, you know, 30 connections instead of 900 connections.

**Joel Dunsmore:** Wow.

**Joel Dunsmore:** And those are the kinds of things that don't pay you a lot of money in terms of how much your instrument costs. Oh, totally. Yeah.

**Joel Dunsmore:** Yeah. That's, I mean, process efficiency right there, right? I mean, it's just, I don't ever think about it in terms of calibration. But like, yeah. Especially at the scale that these things are operating at. I mean, because of the hunger for connectivity and moving bits in such crazy amounts, especially in the, you know, the modern era with having so many, just how many cell towers you need out there. It's just like, yeah, you've got to have a piece of test equipment testing everything. You can't just assume it's going to be fine. It's crazy.

**Joel Dunsmore:** And, well, the thing that you run into is these folks, they actually want stuff to work. You say, I got a gig speed connection. They actually want to see that it's a gig speed connection. And how many times have you read, well, I have this gig speed connection. I'm getting 100 megabits per second. But, you know, that's just what happens. I think a lot of times what occurs is just little discontinuities, little badnesses stack up so fast at these super high speeds that you can give up performance so fast. You spend a lot of money to get to high performance and you have to spend a little bit of extra money to make sure you maintain it.

**Joel Dunsmore:** Yeah. And it is very interesting too. Like, I mean, especially because I think, you know, when I think about Keysight, I think about test equipment broadly. I think about like on my bench, right? That's where I expect things to be. But, yeah, it's the factories where the stuff, that's where the money is. That's where the rubber hits the road, it seems like.

**Joel Dunsmore:** That's where all the problems are. Well, that too, yeah. Usually, you know, I like to, so at my level right now, I only get involved with customers if they have a million dollar problem. You got a million dollar problem, I'll come in and talk to you about it. Got it. Oh, cool. You're the fixer, is that right? I've been to so many places and sometimes the fixing is surprisingly simple. I was in the Far East where they said, ah, your systems are just not working. They're drifting terrible. And, you know, I asked the inevitable question, have you connected the reference, the 10 megahertz reference? Yeah, absolutely we have. So, we came around to software, well, here's a software way you can track out the drift. And they said, great, that works. Next time I went to visit them, I said, let me see that system is drifting. And they connected the reference end to the reference end because the person who was doing the work wasn't a native English speaker. So, reference, it's like A to A, B to B. That's right. And so, that was a problem that you couldn't solve except by being there.

**Joel Dunsmore:** Well, yeah, I mean, I have to say, so as someone who has to like troubleshoot people's hardware remotely, I will say the first thing I ask people to do is take a picture of it. Because, yeah, that's a very human problem, right? Man, that's an expensive fix for a simple thing.

**Joel Dunsmore:** FaceTime helps out a lot in that case.

**Joel Dunsmore:** Yeah, right, right, yeah. That's great.

**Joel Dunsmore:** But then just the old stupid 60, you know, or in other countries, 50 hertz signals floating around.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** I went to give a presentation to one of our large customers. And they said, yeah, we're not doing a presentation today. We have a problem in the lab. So, they put me in a bunny suit and I had to go up to their lab. And they're showing me, see this, one of our network analyzers has the ability to also measure DC at the same time as RF. So, you want to do that for power added efficiency. And they're saying, your DC trace, it's terrible. It's wiggling up and down. It's all noisy. So, I'm adjusting the speed. And when I get the speed to where it can do about 200 millisecond sweeps, let's see, 10 cycles, 200 milliseconds. That's 50 hertz there. Yep. They had a giant ground loop on their test station. Oh, my God. So, they're running amps through the ground of our system. And I told them, you have a ground loop. No, there's no ground loop. So, we just start disconnecting other pieces of equipment. And all of a sudden, the ripple went away. And it's like, okay. Falls right into place. I'm sure you've ran into those kinds of things.

**Joel Dunsmore:** I have specifically at my days at Keithley, it was one day a firmware change had flipped a bit. That was the 50, 60 hertz internal calculation thing on the ADD. You know, it was a DC thing. So, it was low and slow. But like that offset, just, you know, the 60 hertz line cycle thing, it was like five sixths of what it should have been. You know, it was like, oh, okay. So, yeah.

**Joel Dunsmore:** And how long does it take you to find that the first time?

**Joel Dunsmore:** The first time, a week. The second time, I thought to look.

**Joel Dunsmore:** Yeah. It's not that I'm so smart. It's just I've been around long enough to see all these things.

**Joel Dunsmore:** I mean, that's the thing. You are the physical incarnation of that engineering cone of, you know, the guy that walks in with a piece of chalk. And, you know, it's $49,999 of knowing where to put the piece of chalk or the mark with the piece of chalk, whatever. Exactly. Same old engineering story, right?

**Joel Dunsmore:** Except that everything's new again. So, all of the problems that you never thought you'd see.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** Eventually, they show up. And then you're taking a week or two to figure out something that seems like it should have been simple to know.

**Joel Dunsmore:** Well, Joel, I have to say it's reassuring that someone with your level of expertise is also frustrated with that because some days I get frustrated with like a UART, you know. It's just like I can't get it to work. I've done this before. I know it should work. Yeah. Yeah. Well, speaking of your extensive experience, we have not even brought up the fact that you have a book that's on my bench and is my favorite of the books that I got as I was frantically trying to learn VNAs. Let's talk a little bit about that. So, this is – I had the first edition, I think, microwave component measurements. Yep. And there is a new edition.

**Joel Dunsmore:** Yeah. So, the new edition – first edition was in 2012. And it was all network analyzers and CW signals, swept sign signals. And since then, we've added a lot of capabilities, not just us all, other competitors as well. So, added the capabilities to do spectrum analysis, to do modulated measurements, to do complicated noise figure measurements. So, I had to come up with the second edition to add all that new capability in to explain what we do and how we do it. And I go down to essentially the mathematics of what's going on inside the analyzer. So, if you want to recreate the error correction we're doing or understand why we get a power number that we get, all that math is in there, as well as a lot of very just practical examples. If you're measuring an amplifier and it's got to be 50 watts output power, how can you avoid blowing up your equipment? Here's the block diagram you need.

**Joel Dunsmore:** I appreciate that, yeah, because I'm pretty good at blowing things up. And this helped me do less of that.

**Joel Dunsmore:** Yeah, there's a whole chapter on fixturing and all the tricks of dealing with PC board fixtures and, you know, how can you remove those effects?

**Joel Dunsmore:** Yeah. You mentioned all the things that are changing since the 2009 book came out. Why is all this stuff changing so much?

**Joel Dunsmore:** So, a lot of it is just this push for both high-speed tests, but also they want to have better accuracy in the tests. So, a standalone noise figure analyzer is pretty accurate, but its largest error is caused by the impedance mismatch between its system and the thing you're measuring. So, as network analyzers measure impedance mismatch, if you put a noise figure analyzer inside a network analyzer, you can remove that error. And the noise figure analyzer, 90% of it's the same hardware as a network analyzer. So, you can get the noise figure analyzer capability. It's only a marginal increase in the material cost to the instrument. So, it makes things less expensive, but more importantly, it makes them work better. Yeah. So, I like to say our new P&A is the world's most accurate spectrum analyzer, not because it's so accurate as a spectrum analyzer, but because we can apply the vector error correction to it that if you don't have a network analyzer inside your spectrum analyzer, you can't do that. Yeah.

**Joel Dunsmore:** So, it's kind of like the kitchen sink type of approach to things, but because you have all these other adjustment tools that are in there in order to make a network analyzer, that's what really makes the magic happen, it seems like.

**Joel Dunsmore:** Yeah. So, if you have a chip you're trying to test and it's on wafer and you have to go through all these probes and all those discontinuities, the standalone equipment like a signal source or a spectrum analyzer is really difficult to compensate for all those losses and you have to pre-measure everything. With the network analyzer, you put an open short load chip in the fixture and it characterizes that. So, then we can apply that fixture characterization to all the other measurements. If you're doing demodulation and you've got to remove the effects of frequency response, we can remove all those effects without having to pre-measure stuff because it's all done as part of the normal calibration.

**Joel Dunsmore:** So, when you say pre-measure stuff, what does that actually mean?

**Joel Dunsmore:** Basically, they would take the cable that goes from the spectrum analyzer to the wafer prober and they'd have to measure that on a network analyzer and they'd have to take the probe and measure the loss from the probe to the probe tip. Then they have to combine those in an Excel file and download that offset into the spectrum analyzer to know the right power at the right place.

**Joel Dunsmore:** Oh, interesting.

**Joel Dunsmore:** So, it could take you a couple of days to do that.

**Joel Dunsmore:** Yeah, yeah, yeah. Yeah, so like if you had a signal generator that was just sweeping from like zero to 10 gigahertz, you're saying, some cable might put in some unknown impact at like five to six gigahertz and you'd have to characterize that. And you're saying you'd have to then adjust for that somewhere else. Right.

**Joel Dunsmore:** Right. And with older systems, they would literally have to program a single frequency and then adjust the power level up or down according to that loss of the cable. Maybe your cable goes through a switch matrix and then the switch matrix goes to an on-wafer probe and someplace in there it's not great. So, it has a little narrow band dip of 3 dB. So, half the power is gone. And so, you have to point by point kick up and down the power as you're moving across and that might slow you down a thousand times slower than if you had that integrated into your system.

**Joel Dunsmore:** Yeah. I would imagine that at some point, too, you'd start to be able to reduce the cabling needs. Not that you would go with bad cables or bad test heads or, you know, test probes or whatever, but I'd imagine that you'd be able to not be as rigorous as otherwise needed because you're, if you're adjusting for everything and it's like provable that you can adjust for it, then no big deal or less of a deal.

**Joel Dunsmore:** That's pretty insightful. That's one of the things that we can do. So, we're getting into making modulated measurements and it's really hard to do a clean job of making a source pristine if you want to make some kind of, it's called QAM modulation.

**Joel Dunsmore:** That's the one, is that the one where like it's in the little tiny circles? I've seen that on the, the signal to a spectrum analyzer had that. I had no idea what I was looking at, but it looks so cool.

**Joel Dunsmore:** 16 little dots and you want them to be tiny little dots and it's really hard to make them tiny little dots. And our signal source guys work on that and struggle with that to make that perfect. Then you pass it through a cable and it's no longer tiny little dots anymore.

**Joel Dunsmore:** Right, right. It looks like a pepperoni pizza at that point then, huh?

**Joel Dunsmore:** Right. And what we can do with a network analyzer, we do this today. I'm actually going to be presenting some of this at a webinar a little later in the month. We can capture that response with the network analyzer because we have a way to calibrate it. Then we can go back to the source and feed it a distortion correction signal and make it look perfect. So we can essentially make your source look perfect at the interface of your device a meter away from your signal generator.

**Joel Dunsmore:** Wow. Yeah. That's really cool.

**Joel Dunsmore:** That is what's driving people to these multifunction tests is sometimes the, in the real world manufacturing, they can't connect directly to their signal generator. So they have to go through a switch matrix for all the testing and they got to go through the thermal chucks because they got to test it hot and cold. And all that for the new 5G stuff, without these corrections, they practically can't make the measurements. Yeah.

**Joel Dunsmore:** I'm just imagining like bending, like, so if you had like a test head that had like 100 pogo pins on it and then, you know, Bob is careless one day and he bends one of the pogo pins. It's like, oh, we have to remove this entire test head and recharacterize everything. It's like, Bob, you're fired.

**Joel Dunsmore:** So I was just involved with a situation where almost like that, we said, we've got this data. We can see this got this one bad transmission line. Is there any way it took us weeks to get the data? Is there any way we can figure out what that effect was? There is actually a way that we can look at the data and say, okay, this effect is caused by this bad spot and we can figure out what that bad spot was and then regenerate all the data again as though it wasn't a bad spot. Oh. Huh. We call that automatic fixture removal and we charge people a lot of money for that. We don't give that one away and it's been super popular because with that, you can basically just take your probe or the end of your coax and just leave it open and we'll figure out all the badness of the coax cable and then connect it to your device. You don't even need to calc it anymore. That's also in the second edition explains how we do that.

**Joel Dunsmore:** Okay. That's great. Yeah. I mean, like, do you ever worry that like, I mean, this seems like software kind of just smoothing out the edges and things like that. Do you ever worry that it's not capturing reality? I mean, like, I know that you guys prove it, but like from like just a gut feel kind of thing of like, oh, well, are we actually removing, you know, like, is it like provable? How do you actually tell that it's actually flat and removed and everything's copacetic?

**Joel Dunsmore:** That's a lot of, uh, actually the work I personally do is not proving that something is, can measure a good thing. Good. You got to be able to prove that you can measure a bad thing and show that it's bad. You haven't seen that. You don't have a ripple that's been smoothed out. That's a real ripple.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** Right. Right. So we spend a lot of time and a lot of effort, you know, understanding exactly where all these errors come from, which ones you can correct for, which ones you can't correct for. Then figure out ways. This is what we call a process called verification that says, I'm going to measure a thing. We measure a good thing and make sure it measures good. And we measure a bad thing and make sure that we can see the right amount of badness.

**Joel Dunsmore:** Yeah. Right. Right. Exactly. Yeah. You need to have like, uh, like, like golden, golden samples almost. And, and, but in this case, a bad golden sample as well. It seems like.

**Joel Dunsmore:** Exactly. You have to, uh, noise figures, one of those things that everyone just wants the noise figure to be low. So if you built a system that always measured everything one DB lower than it really was, nobody would complain in manufacturing.

**Joel Dunsmore:** They'd all think that was great. But then the FCC would give you a call, right?

**Joel Dunsmore:** Yeah. Maybe the dish TV subscriber who can't get it when it rains. He's really good. And that's the interesting thing about all these digital modulation schemes is they, you know, degrade slowly. So if you have equipment, that's not really that great. Instead of getting a hundred megabits per second, you'll get 10 megabits per second.

**Joel Dunsmore:** Uh, interesting. Yeah. Yeah. I mean, yeah. And that's, I mean, that, that, yeah. Like you said, the, there's the degradation degrading there. I think about these like correction codes that are in every digital transmission too. And it's just like, they're digging so much out of the noise already. I don't know. It just, it works pretty well. But then, but then it's like your expectations change. And now I can go in an elevator and it's no big deal, but it's, it's a little bit worse for my phone now than it used to be or something.

**Joel Dunsmore:** It's the difference between it goes from good to dead to, it gets a little pixelated for a little bit. If somebody jumps around the screen too fast, it's pixelated. And what's happening there is you're just seeing that's a spot where the data stream had to slow down because a car drew over in front of the antenna or a giant rain cloud came across. And the radios are constantly communicating and saying, okay, got to drop to a lower modulation rate. You got to give me more. The lower the modulation rate, the more signal to noise you have. And at these high scale modulation rates, the signal is hardly out of the noise at all.

**Joel Dunsmore:** Yeah. I mean, it's, it, it's as close to magic as I can imagine.

**Joel Dunsmore:** And there's a reason why these companies like the giant one in Cupertino have tens of thousands of engineers working on this stuff because it is really complicated.

**Joel Dunsmore:** Yeah. Question about, this popped up a little earlier, but I don't think I asked it. So the 8753 on my bench is a two port VNA. Yes. And there are now higher port numbers.

**Joel Dunsmore:** Is that right? Yeah. We go up to, I think the biggest we've commercially shipped is 66 ports. Oh my gosh. So why, why is it higher? What is, what are the added ports in that case? So they're essentially what you, so you have an amplifier, it's got an input and an output. Say, okay, now I'm going to have a differential amplifier. So differential amplifier actually has two inputs and two outputs, right? It's got four ports to it. Yeah. And you say, okay, but now I've got an eight channel MIMO differential amplifier. So an eight channel times four, that takes 32 ports. And we sell lots of 32 port systems for these eight channel MIMO test sets. And the thing is, a normal network analyzer, you could say, well, I'm going to turn on source on port one, and then I'll measure to port two. And then I'll measure from one to three and one to four and one to five. So you got to take a measurement for every one of those paths. And if you have a switching network to switch it around, it's a measurement per path. So I don't remember the number of something like, oh, it's exactly N times N minus one over two. So if you got six ports, it's six times five over two. It's 15 measurements you have to make. If you have 32 ports, it's whatever that is, 32 times 15 measurements that you have to make. So those hundreds of measurements get really slow. But if you have a 60 port analyzer, you turn on port one and you measure it on all other 60 ports at the same time. So you really drop the throughput time. And these manufacturers, they cannot take 10 minutes to test an antenna that they're going to put on a car. They have to test it in a second. So the more ports, it just means making more measurements at the same time. Okay. It's just exactly the same as a multi-core processor.

**Joel Dunsmore:** Got it. Yeah. Yeah. I mean, I think I've seen up to maybe eight for the bench. You know, I browse through these catalogs and my jaw is usually on the floor in terms of I'm like, oh, is my consulting company going to pay for that this month? No, it is not. But maybe I'll rent one sometime. And I have seen up to eight. And it does seem like that would make sense then on the bench with the differential, or I guess four in that case would be a differential amplifier, that sort of thing.

**Joel Dunsmore:** 12 ports is really popular. So in the handheld USB network analyzer, we make a six-port version. So you take two. And the reason 12 ports is popular is if you have differential pairs, you have the signal pair, the adjacent pair, and the alternate pair. And they want to know how much signal is cross-talking from one to the other. So you've got six connections on one end and six connections on the other end. And that's a real popular configuration. And that's also why the PXI analyzers have become so popular because you can, you know, configure up a four-port system. And then your buddy on the aisle away, he has a four-port system. And when he goes on vacation, you can steal two of his modules and make your system an eight-port system.

**Joel Dunsmore:** Right, right. Hey, Bob, you're taking a day off today because, well, I need to do more measurements.

**Joel Dunsmore:** It exactly happens that way.

**Joel Dunsmore:** Yeah. Yeah. Hmm. That's great. That's great. So back to the book real quick. So people get the book. What do you think they should be starting with? Is it just kind of a sit down and read it kind of thing? Is it a sit down and read it before you buy a VNA type of thing? Or is it you already have a VNA, you've already read other books, and you're getting deeper?

**Joel Dunsmore:** If you got a... So it's really written around the modern VNAs. So the first three chapters are all about kind of the older VNAs. It's the kind of underlying theory. And if you always wonder, you know, how does this error correction thing work? It explains that. But the later chapters, it's really written as a handbook. So you say, right, I got a low noise amplifier I have to test. And it's got 60 dB again, and I'm getting terrible results. Let me take a look in the chapter on amplifier test or noise figure test. And, you know, there'll be 20 pages there that you'll have to read through. And then afterwards, you'll understand, oh, this is all the things that I was seeing. It was causing me trouble. So it's really designed to be a handbook where you got a particular problem, you need to test a frequency converter. We'll look up the best way to test a frequency converter.

**Joel Dunsmore:** That's great. Yeah. Yeah. Between this book and Tom Lee's book on microwave chips, which after the first couple chapters, I was – Tom's also been on the show. And after the first couple chapters, I'm like, ah, it was silicon RF stuff. I'm just – I'm not – that's not me. Yeah. But, yeah, those – the first chapters are very, very, very helpful for those sort of things.

**Joel Dunsmore:** Yeah. And so in the book, I tell – I basically say, here's the six steps you need to do to test anything with a network analyzer. And people always, when I ask the question, I go to a seminar, I say, okay, what's the first thing you do? Everybody says calibrate. And no, that's quite a ways in the process. The first thing you do is you connect – and this has been true for the last 30 years. The analyzers are all pre-calibrated to the factory, so they're pretty good.

**Joel Dunsmore:** Mm-hmm. Yep.

**Joel Dunsmore:** So connect your thing up, make your measurement, take a look. Does it make sense? No, my gain's minus 30 dB on my amplifier. My isolation's plus 30. I hooked it up backwards. So let me turn it around. So the first thing you do is you make all your measurements that you want to make without doing any calibration. Then you adjust your cables, your connectors, your adapters. Wiggle your part to make sure it's stable. So I say first just connect it, measure it. Then optimize your measurement. When you've got everything working pretty good, then take the time to calibrate.

**Joel Dunsmore:** Mm-hmm. Yeah. So I'm almost like fixturizing on your bench. That's another thing that I've learned is just like tape things down.

**Joel Dunsmore:** Oh, yeah. That helps. Especially if you have bad cables.

**Joel Dunsmore:** Yeah. Which I do. Mostly. Yeah.

**Joel Dunsmore:** Taping your cables down is just like keeping your dog in a pending area.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** You know, can't get into trouble if it doesn't move around too much.

**Joel Dunsmore:** That's right. Yeah. I think that one of the big problems for me is that I was at a shared workspace when I got my VNA. And I had to clean up every night. And so every day I had to go and pull this thing out and like redo measurements and redo my fixture. And it's just like, oh, this is just not, you know, it's not as mobile as I wished it would have been, you know?

**Joel Dunsmore:** So network analyzers like to be turned on and then you turn them off when you retire.

**Joel Dunsmore:** Right. They're all, they've got that stable temperature operation and they're all warmed up.

**Joel Dunsmore:** Yep. And they just like to sit there and be warm and stable. And there's a lot of metal in there. So you don't want it to move around.

**Joel Dunsmore:** Right.

**Joel Dunsmore:** It's just, it's, and it's all physics, right? It's the speed of light. The cables inside, as they get hot and cold, they stretch and shrink and that moves your phase around. And that's what causes you trouble.

**Joel Dunsmore:** Yeah. It's almost like the devil, you know, kind of thing. It's like, okay, yeah, maybe your cable's hot and it's, you know, putting something into the measurement. And well, it's not that bad, but it's, you know, it's, it's having some impact on your measurement tool or your measurement path. And it's like, but you know it and it's there and it's the same. And it's like, you don't need to, you just calibrate it. It's gone, you know?

**Joel Dunsmore:** Calibrate it. It's gone and everything will be good.

**Joel Dunsmore:** Yeah. I think that's another thing that's interesting about this kind of area is that it's not, there's, there's not really any absolutes. That's, that's another thing that was different for me coming from the DC side of things. You know, there was like a measurement standard is tracked all the way back to some, some NIST lab, some fancy, fancy resistor or current source or something based on a SI unit. And I just, I, I, it's very different here.

**Joel Dunsmore:** Well, we are based on impedance and that goes back to the diameter of an inner conductor relative to the diameter of an outer conductor on a magic airline. Something that's been measured to the, so impedance.

**Joel Dunsmore:** Oh, okay.

**Joel Dunsmore:** The reference of impedance is distance. And, uh, they have an airline at NIST that they measure and they say, yeah, this airline is this impedance. And then they use that to calibrate a system that then you use to calibrate your loads and resistors and ambassadors.

**Joel Dunsmore:** Okay. So that is tracked all the way back. The, I guess, and I guess there's factory calibration I could do. So I, I just meant like the relative, once it's in hand, I don't even know when mine's been calibrated last. So who, who knows how good mine is, but.

**Joel Dunsmore:** So there's two kinds of calibrations. And, and in my book, I, I'm a little bit more careful than I am in just language. When we talk about calibration from the instrument side, what we're saying is we've measured the instrument and we verified that it meets all the published specifications. And that's what that cal sticker says. It says it meets its specifications. The kind of open short load calibration. That's what I really call error correction. And that's the thing that most people deal with is the error correction. And okay. Dirty little secret here. You can be pretty far out of cal and on an instrument and still have error correction, return it to a reasonable measurement.

**Joel Dunsmore:** Oh, I think, I think mine that's been, uh, you know, the eBay buy and shipped to me and, you know, has a two-year-old certificate. I think, I think mine is pretty far out of calibration probably.

**Joel Dunsmore:** But a good error correction will probably make your measurements look pretty good unless it gets so far out that the, there's only so much you can correct before the numbers start to fall apart.

**Joel Dunsmore:** Got it. Got it. So, so I shouldn't title this episode, Joel Dunsmore does not endorse calibration. Or something like that. That would probably be not correct.

**Joel Dunsmore:** That would be not correct and not good.

**Joel Dunsmore:** Yeah.

**Joel Dunsmore:** Right. Now, calibration is how, is how you know that your instrument works the way it's supposed to work. And the error correction is how you make it perfect.

**Joel Dunsmore:** Yeah. Yeah. And especially the, the test setup thing too. Again, like Jeff, friend of the show and friend of me, uh, uh, Jeff, he, uh, he helped me through a lot of this stuff. And I didn't, again, I didn't quite understand the, the test setup kind of piece. And that really seems like a lot of the error correction stuff. The absolute measurement against NIST standards is, is interesting too, because it's, it's, it comes from somewhere, you know, it's got to start somewhere.

**Joel Dunsmore:** If you have one of our Cal kits, our Cal kits are characterized against a NIST artifact.

**Joel Dunsmore:** Ah, I got it. Yep. And that's why they're, yeah. Cal kits are not cheap. They are not cheap.

**Joel Dunsmore:** Or you could put a 50 ohm resistor on a PC board and call that a Cal kit. I talk about that in my book as well. I'm making your own calibration standards. And if you can do that and it's stable and you characterize it against a good calibration kit, you're going to get good results with it.

**Joel Dunsmore:** Yep. Yep. Yeah. And I think it comes down to like what you need in your own system, in your own reliability of, you know, if you're making something that's going into a cell tower, it's probably a lot different than something that you're making for. Or, you know, a hobby, a hobby project or something similar.

**Joel Dunsmore:** Or if you're making something that's going to fly to Mars and you want to make sure that the signal. Yeah. Lines up. So the aerospace defense guys, you know, people making satellites and making radars, they're like at the top tier of everything has to be in calibrated. You have to run your daily calibrations. You have to record any variation. Oh, wow. Because that stuff has to be perfect. You know, satellite stuff has to be perfect or you're going to end up with dead junk in space. Cell towers have to be pretty good. But if they're not perfect, okay, maybe you can't connect to 100 cars. You can only connect to 20 cars. Handsets are maybe a little less perfect. And ham radio guy tuning up his 80-meter antenna, well, you know, as good as it needs to be.

**Joel Dunsmore:** Right. Right. Yeah. As far as he wants to get on a contest day, I'm guessing, right? I mean, some of them are getting very, very far. It's very impressive sometimes. That's great. Joel, we are doing a giveaway for the book, I believe. Right?

**Joel Dunsmore:** I think we are. Shamri, he was one of our colleagues here, is going to arrange that with you.

**Joel Dunsmore:** Yes. So we will have a form down below if people are interested. They can put into the form their information, which we never sell or use for anything else other than drawing a name for sending out books. But we'll be doing that as a thank you. Well, first off, thank you for being here, Joel. And thank you for sharing some of this knowledge, both here and in the books that we'll be giving away. So it's been great talking to you.

**Joel Dunsmore:** Great. By the way, I've really enjoyed – so I found you and started binging your show and have enjoyed it very much. I always enjoy when Dave talks about RF. It's good for a chuckle.

**Joel Dunsmore:** Got it. Yeah. Yeah. That's – it's fun to have one topic that I know a little bit more than Dave about.

**Joel Dunsmore:** But if you have any more questions on your network analyzer, feel free to give me a buzz.

**Joel Dunsmore:** I have to say that that is a great honor to be able to talk to someone like you. And the person that designed the box that's actually sitting on my shelf is – that's pretty darn cool. That's pretty darn cool.

**Joel Dunsmore:** So thanks again, Joel. Well, hopefully it'll keep working. And thanks for having me on.

**Joel Dunsmore:** Yeah. Thanks so much. We'll talk to you soon.

**Joel Dunsmore:** All right. Bye-bye.

**Joel Dunsmore:** Don't forget to fill out our annual listener survey to be entered for a chance to win one of three copies of Joel's book. We always love the feedback our audience has. If you'd like to give direct feedback and support, join the crowd and the Discord channel at patreon.com slash the amp hour.
