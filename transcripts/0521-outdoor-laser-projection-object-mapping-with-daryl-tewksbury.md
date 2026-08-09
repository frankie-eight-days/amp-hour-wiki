---
episode: 521
title: Outdoor Laser Projection & Object Mapping with Daryl Tewksbury
url: https://theamphour.com/521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury/
---

**Daryl Tewksbury:** This is The Amp Hour Podcast. Released December 13th, 2020. Episode 521. Laser Projection with Daryl Suxbury.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Daryl Tewksbury:** And I'm Daryl Suxbury, ex-LaserVision employee, engineer, software, hardware. Who did it all at LaserVision. Thank you very much for joining us, Daryl. No worries. Thanks for having me.

**Dave Jones:** I've always been absolutely fascinated about, and I've wanted to do like a video on like a, you know, a tour of, you know, the company who does this stuff. I may have even contacted LaserVision at one point. For people who don't know, tell us what LaserVision, you don't work there anymore, but you did. And you did practically everything there from hardware to software to lasers, which we'll get into. So can you tell us about your time at LaserVision?

**Daryl Tewksbury:** Yeah, well, I wouldn't say I did everything because obviously there was quite a large group of people, artists and things that, yeah, what I mainly did was come up with the show control design. So that would be software and hardware and firmware and everything in between that basically it's from between the artists and the final output from the lasers. Oh, amongst, you know, audio and video and MIDI and all that other control stuff, which was all part of the system. Everything was integrated in one system.

**Dave Jones:** So LaserVision, for those who don't know, do those huge laser mappings, laser projection mappings on the side of buildings like famously here in Sydney, do it on the side of the Opera House or the Museum of Art building. And it maps and contours to the shape of the building and or the shape of a waterfall. You can project onto waterfalls and other objects and things like that. Can you explain overall what the, you know, what different types of things you actually project on?

**Daryl Tewksbury:** Okay. Yeah. So we would use water screens for creating imagery like above a big body of water like we did in Dubai and in Singapore. So it's a combination of video projection and laser projection because, I mean, obviously you can get a lot of different artwork from a video projector.

**Dave Jones:** Right.

**Daryl Tewksbury:** But with a laser, you can get quite bright. It's horses for courses because the artwork between the two is because we'll have to go into how the lasers actually work because.

**Dave Jones:** Definitely.

**Daryl Tewksbury:** It's an interesting and sort of sometimes hard to get your head around the concept of you have basically X number of photons available. So the more complicated your imagery, the duller your final image will be. And also it can become flickery because of the scan limits and things like that. Got it.

**Dave Jones:** Is it usually just a single laser? What, you know, just one, you know, big couple hundred watt laser doing this? Or is it like multiple ones that do different sections? Or how does that work?

**Daryl Tewksbury:** Yeah. So a large installation will have probably many lasers in different areas all working sort of together. But a single laser nowadays is basically an RGB laser with the red, the green and the blue beams combined. So into a single beam and you modulate the current driving each of those three colors. So it's not unlike, you know, the pixels on a display to generate whatever color you want from the red, green and blue that you have. Some lasers have multiple different colors as well, not just the three, but it's most common to have the three. And then they hit an X and a Y galvanometer controlled mirrors to scan the beam. So if you can imagine you scan a circle and then during the scan time, you change which lasers are on to produce whatever colors you want within that scan. And the persistence of vision of us mere mortals leaves the whole, you can see the whole image where in actual fact, well, it's not unlike a raster scanned CRT.

**Dave Jones:** Yeah. So what sort of scan rates are we looking at? What sort of, and what sort of like modulation rates for the lasers? How, you know, do you have to ramp, how many amps do you have to, you know, amps per second do you have to, you know, ramp this sucker up at?

**Daryl Tewksbury:** For the scanners?

**Dave Jones:** Yeah.

**Daryl Tewksbury:** That's, I like the way you're thinking because they're tiny, tiny, tiny little mirrors, but you've got to have heaps of current available because you're moving them at stupidly high speed sort of angular velocities. And so therefore they have complete feedback. So the position of the mirrors is fed back. And so it's a closed loop. Oh, a closed loop system. Highly tuned servo system. Yep. With like, I think peak currents of like 12 amps or something into, and these motors are only very small, like maybe eight millimeters in diameter. And so. Oh, okay.

**Dave Jones:** So we're talking about tiny little mirrors here.

**Daryl Tewksbury:** Yeah. Because luckily photons don't weigh anything.

**Dave Jones:** Yeah, exactly. So it's, it's, it's just that, you know, I picture like big, maybe when we get into the, the, the projection, the light projection side and not the laser side, that's when you start talking huge powers. Right?

**Daryl Tewksbury:** Yes. Yes. Well, back in the old days, you used to talk huge powers. We should probably cover off because lasers are sort of a pretty interesting thing. And these RGB lasers are relatively new. When I started working for the company, we were using ion lasers, which were like gas discharge, argon, krypton lasers. Now they are a different beast because the single laser, and it had a mixture of argon and krypton as the lasing medium, but they would produce like, I think nine or 10 different lines. When I say lines, spectral output divided into, you know, like 600 nanometers and 500 nanometers.

**Dave Jones:** Oh, so they generate different colors at the same time effectively.

**Daryl Tewksbury:** Yeah. So the one, if you put a diffraction grating in front of the output of one of these lasers, you'd get, you know, maybe 10 or 12 different colored lines coming out of it.

**Dave Jones:** Oh, interesting. I had no idea. I always assumed that they were single color.

**Daryl Tewksbury:** No. So these are designed to have like a lot, a lot of lines. And so you've got different, and they're much prettier, a much prettier light because they have some really, really beautiful orange line, like actual orange light. Right. Not red and green mixed together to make sort of yellow and orange. Yeah. An actual orange, when you looked at it, it was super orange, really, really nice color. And deep reds and violets and like lots of different colors. And the way we extracted those colors is probably pretty interesting to you. So we had a thing called a polychromatic acoustic optic modulator.

**Dave Jones:** Yeah. Okay.

**Daryl Tewksbury:** PCOAM. So it's a crystal and you feed the laser, which has got all the lines in it. You feed the laser through it. It's inside sort of a cavity, which has got an RF coupling to it. And if you feed different frequencies into this crystal, it will bend one of the lines out. Right. So you've got, without any RF energy into the crystal, the line comes in and it comes out the other end. So you've got the laser coming in one end and just coming out the other end. When you energize a particular frequency, it can bend a particular light frequency off axis. So you end up with another beam coming out. Nice. But it's only the particular color that you're wanting to pull out.

**Dave Jones:** Yeah.

**Daryl Tewksbury:** And the amount of energy, RF energy, is basically how bright that line is. It doesn't change the angle of it. It just changes how much of it is pulled out of the main beam.

**Dave Jones:** Wow. So you can modulate it.

**Daryl Tewksbury:** Exactly. So you have the RF generator has like eight channels and each channel is tunable in frequency. So you select which channel pulls out which line. So out of the beam that comes out off axis, that's what you send to your scanners. And so what you do is modulate these colors along with the scanners and then you can produce so many colors. But the beauty of it is that it's coming from the same laser. So the beams, it's a beautiful beam. It's got a fantastic profile. Not like all these solid state lasers these days which have pretty dodgy shapes. And the red's a different shape to the green.

**Dave Jones:** Oh, okay. So the spots are physically a different shape, is it?

**Daryl Tewksbury:** Yeah. So coming out of an ion laser, it's basically the ideal laser. It's round. It's got the TEM, which is the profile of it, is a zero zero in most of these expensive lasers that we used to use. Which means that it's got, if you did a cross section of the beam, then the intensity from the outside to the inside is sort of purely half a sine wave. Oh, lovely.

**Dave Jones:** What causes it? What's the mechanism that makes the ion ones be round and the RGB, presumably like solid state lasers be some oddball shape? What's the physics at play there?

**Daryl Tewksbury:** Well, because you've got a round cavity, which is quite long, and you've got a flat, perfectly reflective mirror at one end and a very slightly concaved, partially mirrored mirror at the output end, that is basically just the ideal shape to produce the beam. I mean, the beam's basically the shape of the cavity. So...

**Dave Jones:** Right. Okay. But, RG, but solid state, it's not...

**Daryl Tewksbury:** No. So they don't really have a cavity, per se. Yeah. So they're like a...

**Dave Jones:** A die. Aren't they just a bare die, are they? Or...

**Daryl Tewksbury:** Like quantum well diode. Like they're sort of like an LED, I guess, more than...

**Dave Jones:** Right.

**Daryl Tewksbury:** Yep. More than anything else. But they have really weird profiles. Like they'll be wide and narrow. Oh. So you have to put really strange optics in front of them to try and get the beam back into sort of a usable shape. And then we're not talking... This is your standard like red, green, blue diode lasers we're talking about at the moment, which is sort of the most common that you'll see. So, yeah. And the other problem is that to get high powers, because you can't mix... There's no way of mixing two beams together. Because if they're a similar frequency, well, they'll beat with each other and you get all sorts of...

**Dave Jones:** Oh, right.

**Daryl Tewksbury:** So... Could you synchronize them in some way? Well, you can't physically get them on top of each other is the problem.

**Dave Jones:** Oh, okay. Yeah, of course.

**Daryl Tewksbury:** So you have to do them really, really side by side and like in a grid, say, say 10 across by 10 down. And so you end up with a big square blob of energy. I mean, like literally, if you pull these things apart, you will see 40 red laser diodes, all slightly offset and back from each other, hitting mirrors and just passing like knife edges. It's quite amazing to see, but it produces a really crappy beam.

**Dave Jones:** So, has the industry completely changed to solar state lasers from ion or...?

**Daryl Tewksbury:** Well, okay. Here's the other thing. An ion laser with an output power of, say, 4 watts has an input power of probably about 7 kilowatts.

**Dave Jones:** Whoa. Okay.

**Daryl Tewksbury:** Not very efficient. Not only are they heavy, but they require a lot of water. They require three-phase power. Oh, yes. So a 20-watt solid state RGB laser might only draw 300 or 400 watts.

**Dave Jones:** Oh, okay. So that's for mobile installations and stuff like that, that's vastly superior. That's game changing, right? Yeah. Yeah.

**Daryl Tewksbury:** Yeah. It's just, they really, really the, those ion lasers that we were using were scientific lasers, which is why they had such beautiful beam profiles and things. Right. So they weren't really made for what we were using them for. And they were super expensive. How expensive? We're talking. I would have thought 100K or something. Oh, ouch.

**Dave Jones:** Yep.

**Daryl Tewksbury:** I don't know for sure because they're so, I never bought one myself.

**Dave Jones:** Right. Okay.

**Daryl Tewksbury:** But I know just looking at how much hardware there is that goes along with it. I mean, you can imagine that it's got a power supply, which is supplying seven kilowatts of its current regulated. Right. Linear power supply.

**Dave Jones:** Wow. Oh, yes. Oh, wow. Just getting the heat out of that bad boy is just crazy.

**Daryl Tewksbury:** I mean, you'd probably laugh when you pull the cover off the power supply because the power supply is, say, about four foot high and two foot wide. Yeah. And about a foot deep and you pull the cover off and all you see is literally maybe hundreds of TO3 package, like 2N, 3N, or double fives or whatever.

**Dave Jones:** Oh, really? So they're just paralleling them all up?

**Daryl Tewksbury:** Yeah. Like hundreds of them. And often you'd see a wire cut on one of them because it shorted out. So you just cut the wire. Oh, okay.

**Dave Jones:** So you just cut it off and live with a slightly 1,100th you've lost your rating.

**Daryl Tewksbury:** Yeah.

**Dave Jones:** Rather than repair the suck, it's just, ah, cut it off. We've got some excess there.

**Daryl Tewksbury:** Yeah. Yeah. Yeah. So you were talking about scan speeds before. So the scanners are generally sort of 1,000 points per second is their rating. So they might be 60,000 points per second or 100,000 is probably getting up into the higher speed lasers. Right. Some of the big lasers that we use, like the big YAGs, which are the green ones, say 60 watt or 100 watt laser. Because the beam's not particularly wonderful, like it diverges quite a bit. So we put a beam expander. And when you put a beam expander on it, the divergence goes down by the beam expansion.

**Dave Jones:** Right.

**Daryl Tewksbury:** So if it, say it normally is, say, one degree per 100 meters of beam expansion. If you expand it by two, then it's a half a degree per 100 meters. So we take the laser, which was three millimeters in diameter, the output beam, and put it through an expander and get it up to about eight. I think it was eight millimeters or something.

**Dave Jones:** Okay.

**Daryl Tewksbury:** To get its divergence down to more usable for what we're doing so that when you shot a beam out. Because if you're 100 meters away from a laser beam, if it's three millimeters or eight millimeters, it's going to look the same to you. Right. But if it's spreading out a heap so that the spot on the ground is now 10 meters in diameter, if you can get there to one meter in diameter, that makes a big difference to the quality of the beam, how the beam looks.

**Dave Jones:** What's a typical projection distance for an installation like the Sydney Opera House or something like that?

**Daryl Tewksbury:** I don't know, maybe 300 meters or...

**Dave Jones:** Right.

**Daryl Tewksbury:** Something like that.

**Dave Jones:** So at 300 meters, your beam angle wouldn't need to be much, would it?

**Daryl Tewksbury:** No, that's right.

**Dave Jones:** So yeah, just like what, five degrees or something? It wouldn't be... Yeah, it'd be very small. You'd have a calculator out and calculate your signs and your... Yeah. Right. Okay. So that would have advantages. But then I would presume that you need the smaller spot. Whereas if you were closer, you could have a larger spot with a larger beam angle. Is that correct?

**Daryl Tewksbury:** Well, we always aim to get as small a spot as possible. Right. Because the energy density, it makes you lose so much visual brightness when you enlarge a beam because you're spreading the energy out over such a large area. And also it makes artwork look a bit fuzzy. It looks good if it's nice, tight, small beams. But if you're enlarging beams to get bigger distances, the problem is then that you've got to now, you need larger mirrors. So your scan speed has now decreased because of the mass of the mirrors. Because the mirrors are bigger. So you can't, you know, you can only drive them so fast.

**Dave Jones:** Got it. So what would you use, what type of content would you, is it called content? I don't know. What type of art content would you use a laser projection for as opposed to a video projection system?

**Daryl Tewksbury:** Yeah. So the laser projection we would normally do for outlining. Like so often we would do the outline of a water screen with a laser so that it would be nice bright outline and then have video inside that. But also for beam effect, beam effects is where a laser really shines and no projector is ever going to do beam effects like a laser does. So I don't know if you saw any of those videos, but we've got...

**Dave Jones:** Yeah, I saw a few. Yep. And I've been to a few. I've been to all the ones here in Sydney where they project on the Opera House or they project on the art museum there.

**Daryl Tewksbury:** Yeah. So actually, we haven't done a lot of stuff in Sydney. We did the Olympics back. I don't know when it was, 1990s, whatever it was.

**Dave Jones:** 2000. 2000 was the Olympics, wasn't it? Yeah, famously. Yes, the 2000 Olympics.

**Daryl Tewksbury:** Yeah. Was that the one that we did? Must have been. But we didn't get a lot of work locally in Australia, to be honest.

**Dave Jones:** Well, that's interesting because you're a Sydney-based company, right?

**Daryl Tewksbury:** Yes, we are. Yeah.

**Dave Jones:** So that's actually surprising. Who are the other players in this business?

**Daryl Tewksbury:** There are some local ones in Sydney that do all that sort of work. But we did Swan Hill and down in Warrnambool. Well, that was a long time ago. That's not us anymore. But yeah, Swan Hill is still current. But yeah, so beam effects. We shoot a heap of water into the air with like parabolic water jets.

**Daryl Tewksbury:** Yep.

**Daryl Tewksbury:** And then because that shot's so high, it ends up being sort of just like brain mist stuff. And then when you fire the laser through that, you get really solid beams and sheets and effects in the air that you can't do with a projector. Sorry, you can't do with a video projector.

**Dave Jones:** Right. Do you shoot that? Do you project the laser straight on to that wall of water or does it come from an acute angle or something? How does?

**Daryl Tewksbury:** So, well, many different ways, but generally towards your audience because that's when the beams look brightest. Not into their eyes, but to, you know.

**Dave Jones:** Oh, okay. Oh, so the laser's behind the waterfall relative to the audience. So the audience are in front of the water, the laser's behind.

**Daryl Tewksbury:** The laser's behind, yeah. So when you shoot so much water into the air, it's not a wall, like it's got a lot of depth to it. Right. So you can project geometric shapes and things through.

**Dave Jones:** Oh, okay. So you could do like a cube, a spinning cube kind of thing or something like that. Yeah.

**Daryl Tewksbury:** You could do a square with flat edges and then rotate that. That looks super cool. Or a triangle. So when you're looking through it, it looks like you're looking into the top of a pyramid. And then you can rotate it so that the walls are rotating and then you're making stripes down the edges from the colors modulating. And it's quite a good effect that you can't get any other way. So we use that a lot. Plus animations. Like we projected some fish with the projector in Swan Hill onto the water, swimming through the water.

**Dave Jones:** Oh, yeah. Yeah. I've seen those effects. Yeah. Fantastic.

**Daryl Tewksbury:** Onto the top of the water and then through the fountains. And we don't know about all this stuff until we do an installation and then we're playing around with it during programming and we go, Oh, wow. Right. Look what you can do here. So the show changes depending on what we're able to, what effect we're able. I don't know if you've seen in Singapore, there's a picture of the three big lasers on the top of Marina Bay Sands shining down into the water.

**Dave Jones:** No, that wasn't there when I was in Singapore.

**Daryl Tewksbury:** No, but it's a pretty common photo when you search for Marina Bay Sands. It's like one of the main images that you get. But I remember when that image was taken, we'd set up a Wi-Fi link from Marina Bay over to the other side because we were wanting to see what the show was going to look like.

**Dave Jones:** Yeah.

**Daryl Tewksbury:** So we brought all the programming gear over and I was doing the lasers and we always said we were never going to shoot the lasers down into the water because obviously it reflects off the water and that would probably be bad.

**Dave Jones:** Right.

**Speaker ?:** Okay.

**Daryl Tewksbury:** So we had these three fingered beams coming out of all three towers.

**Dave Jones:** Oh, I'm seeing it now. Yeah. Wow.

**Daryl Tewksbury:** Yeah. So that was poking, those three were poking up into the sky. Yeah. And then I said, you know what, because it was like three o'clock in the morning. I said, I'm going to pull them down and just see what it looks like when you put it into the water. So I grabbed the projection, I dragged it down and they went down in the water. And that was the image that you see there. Oh, right. And it's like, oh, we've got to do this. This just looks so awesome. So out the window went, don't shine the laser into the water. The beam was quite big by the time it hit the water anyway. It was about 10 meters in diameter. So it's not too bad.

**Dave Jones:** Right. So that wouldn't be too bad. Now, let's, yeah, let's talk about the safety side of these, because like I get paranoid over my little, you know, class one, you know, laser pointer here that it might bounce off a wall or reflect off my oscilloscope screen and burn my eyeballs out. And what's the deal with laser safety?

**Daryl Tewksbury:** The deal is that you should be totally paranoid about lasers reflecting off anything. That's the basic deal.

**Dave Jones:** What sort of stuff can they reflect off, firstly?

**Daryl Tewksbury:** That they can reflect off anything. Pretty much anything? Like, yeah. I mean, you can get scatter. If you get a bright laser and you point it, it's very difficult to point it to anything where it won't reflect off.

**Dave Jones:** Really? Even like a work mat, even like an ESD work mat on your bench or something?

**Daryl Tewksbury:** An ESD, it would be pretty scattered because the surface of that is not shiny. Okay. So it would, it would be, it's probably safe. Like if you've, if you're, how many milliwatts is your laser? Do you know?

**Dave Jones:** Oh, only like two milliwatts. You know, the standard, yeah, five or two or something like that.

**Daryl Tewksbury:** See, I think if you brush five or two milliwatts, if it's scanning across your eyes, it's okay.

**Dave Jones:** Right.

**Daryl Tewksbury:** And if you have it reflecting off something, that's probably okay too. But I'm sort of thinking if you've got something that's a hundred milliwatts or something like that, and you're playing with it, you probably should be wearing safety goggles, you know, laser safety glasses for that sort of thing. Absolutely. Absolutely. Because the other thing too, is that the higher power of the laser, it, when it hits surfaces, it melts the surface and then it creates a really nice mirror.

**Dave Jones:** Right. Oh, so it would almost self-reflect back, would it?

**Daryl Tewksbury:** Yes. I've noticed it on a lot of plastics and things when you do that. Oh, that's interesting. When you watch it on the wall, if you have the beam static, the wall, the reflection will start to move because of the shape of the surface it's hitting changes.

**Dave Jones:** Oh, wow. It's just melting and it reshapes itself.

**Daryl Tewksbury:** Yeah.

**Dave Jones:** Oh, fascinating.

**Daryl Tewksbury:** So that can be pretty nasty too. And I've seen. Right. Yeah, I cut a Coke can in half with one of those lasers that's in the top of Marina Bay. Of course you didn't.

**Dave Jones:** Of course. I wouldn't have expected anything less.

**Daryl Tewksbury:** Yeah, we had, like it was in the workshop here in Sydney and I was tuning it to see how much power I could get out of it. And I thought, you know what, I'm going to try this. So I think I've still got the can here somewhere.

**Dave Jones:** Right. Right. Let's, right. Everyone goggles on. I'm going to chop this Coke can in half.

**Daryl Tewksbury:** Yeah. I was by myself. Oh, okay.

**Dave Jones:** All right.

**Daryl Tewksbury:** It was only me in danger.

**Dave Jones:** Excellent. So you wouldn't have any of these safety issues with video projection, although they'd be incredibly bright, though, if somebody stuck their head in front of the video projection box, right?

**Daryl Tewksbury:** Would it blind you? Yeah, so here's the thing. The thing is that if you've got, we were 300 in Dubai, we had 60, 20,000 lumen projectors in this projection, right? Which was-

**Dave Jones:** 16 times 20,000. 60. 60, yeah. Times 20,000 lumens.

**Daryl Tewksbury:** Lumens, yeah. Wow. And they had super long focus lenses because the building that we were video mapping on was a very small field of view from, because it was so far away.

**Dave Jones:** Ah, right.

**Daryl Tewksbury:** So the beam coming out of each one of those, yeah, you would not want to look into that.

**Dave Jones:** Yep. I can imagine. So do you design your system so that that focus distance is configurable? Can you move the lenses or change the lenses? Because each installation would be different, right? Some would be up close. Some would be like, you know, 50 meters away, 10 meters away even.

**Daryl Tewksbury:** Yeah. So when we do the design, we just do a 3D view and work out our field of view and then work out what lenses we need.

**Dave Jones:** Right. So did you write the mapping software for all that sort of stuff?

**Daryl Tewksbury:** So I hired the guy who wrote the mapping software for that.

**Dave Jones:** Right. Okay.

**Daryl Tewksbury:** He worked with me. Like we worked together. I actually wanted someone, I was trying to get another programmer because doing all the work yourself is really taxing. And so we wanted to start getting into video mapping. And I thought, you know what? I want to hire a game programmer because he's probably got a better idea of that sort of thing. So I found this guy, Ken. He's an awesome guy. Like he's so like totally into the math and physics simulation and geometry and all that sort of stuff. So he wrote, I wrote the laser engine. So the engine that does all the geometry correction and stuff for the lasers. I wrote that. And he wrote the video playback engine, which ties straight into this system as well. It's all synchronized together. Right. And so he came up with your, and he did this before everyone else is doing it this way now, but he came up with this idea quite a while ago and was to develop an application where you were looking in a 3D environment, a virtual 3D environment.

**Daryl Tewksbury:** Yep.

**Daryl Tewksbury:** And then you bring in your projection surfaces as models and you place your projectors within that environment also as objects. And then you adjust the focal length on each one and it projects what its field of view is on the model receiving the image.

**Dave Jones:** Wow. All in a 3D simulated model environment.

**Daryl Tewksbury:** So are you sort of picturing what I'm saying? So you've got. Yeah, yeah, totally. So say you've just got a flat surface and you've got six projectors and you move them around in the environment and you poke them at this surface. And then you get all their fields of view to sort of overlap a little bit on each other. And then you've covered this surface with a video that's made up of different sections from all these projectors. But because you've already explained to the system the perspective and the lens depth and all that of all these projectors, when you feed video into it, it knows how to divide up the video into the different sections that get sent to the different projectors and how to deform them to make them all straight. And also how to edge blend the images because it knows where all the overlaps are.

**Dave Jones:** Yeah. But then would that, but then the perceived image would change with the viewing location of the viewer. And if you've got a large crowd, they would see things differently, would they not? They would have a different perspective. So what is a straight line to one viewer may not be, or, you know, like angles line up for one viewer may not line up for other viewers in the crowd. Is that right? I would imagine that's a problem.

**Daryl Tewksbury:** No, that's, no, it works because if you've, let's just take a simple example. If you've got a cube and you're mapping, say, a whole stack of projectors around the cube, then what the software does is make the surface of each surface of the cube have straight lines on it with respect to the cube. So as a person walks around, it, yes, it changes, but it changes to what they expect it to change to.

**Dave Jones:** Right. Okay.

**Daryl Tewksbury:** Because they're just looking at, say, a billboard, which is on one side and a billboard, which is on the other side. And they expect when they're straight in front of it for all letters to be straight and perfect. And when they move to the side, they expect them to be not straight and perfect because in your mind, you know, you know what a surface is supposed to look like.

**Dave Jones:** Right. Because the ones I've seen, like, say, for example, the New South Wales Museum of Modern Art projection, though I've got a video of that on my YouTube, one of my YouTube channels somewhere, is that I'll link it in. And it, like, it's a real complicated building, you know, it's a big sandstone building with lots of, you know, things poking out and stuff like that. And they projected onto that. Yes. And yet they used the features, like if they've got a big column sticking out from the wall, for example, then they will use that as a feature in the animation. Yeah, totally. Rather than try and make it. Because if you tried to make it as one surface, then it would look, I imagine it would look different to different observers at different angles.

**Daryl Tewksbury:** Yes, it would look wrong. But what you do is you make it so that you're effectively projecting onto each surface from a normal. So from directly straight onto that. Even though they're not, the projectors are not. The viewers aren't straight on. But the image is deformed in such a way that it is. So then from any angle, of course, it looks perfect because it's being corrected for all the surfaces.

**Dave Jones:** Yes. Like it's emitting the light. Well, it is basically emitting the light. It's actually reflecting the light back. Yeah. And wow. What about the reflection, like if different surfaces that you have to project on? I imagine. Yeah, that's. Does the software cater for different reflective properties of like, you know, sandstone building is going to be different to some polished tile thing on the opera house or something?

**Daryl Tewksbury:** So we played with this a fair bit in Dubai because the building was a hotel. And of course, the hotel is full of windows.

**Dave Jones:** Yeah.

**Daryl Tewksbury:** And we had them put a special film on the windows because. Oh, really? The glass is really a very poor projection surface, as you can imagine. Yeah. I can imagine. So we put a perforated film, which had like a 50% or 30% perforation in it. So that gave us a little bit better reflection off the windows, but the windows were still darker. So we played with doing, adding a new luma layer, like an alpha layer into the video with the inverse of the brightness of the windows to the wall.

**Dave Jones:** Got it.

**Daryl Tewksbury:** You know, on the, on the, it would darken where it hit the wall because that reflected better and then would leave the windows at full brightness. So you could get it so that even though it was full of windows, it looked like a, it had no windows in it.

**Dave Jones:** Right.

**Daryl Tewksbury:** But we had to waste like 70% of our power to do it.

**Dave Jones:** Oh, I was going to, yeah. With a projection mapping thing, how do you, video projection, how do you, I guess you could darken an individual pixel, couldn't you? I guess you just drop it. Yeah. Okay. Yeah. Yeah.

**Daryl Tewksbury:** So the, the actual, yeah, the video that we put on there is, you know, all the correction is done by the software. So we have basically a picture of the building and yeah, an artist just makes a black and white version of that. And we're all gray and gray and white version. And we dumped that in on top of the video and it corrects for the difference in reflection. But we ended up not doing it because we just wasted too much power and we wanted it as wide as possible. Okay. Especially in Dubai because there's a lot of sand in the air. So you get a lot of attenuation, even just close. It's terrible.

**Dave Jones:** Really? It's just all blown around, is it? Yeah.

**Daryl Tewksbury:** Like a kilometer or a kilometer away, it looks like it's not even being projected onto, even though the building itself is really bright. Yeah. Wow. Yeah. It's astounding how much energy you lose. Jeez. That's incredible. When there's particulate in the air. It's amazing.

**Dave Jones:** So would you use like different projectors at different angles for more complicated arrangements or is that too hard?

**Daryl Tewksbury:** Yes. So the, the beauty of the software is that you can basically grab as many projectors as you like and just spray them all over the place. Really? And as long as you, as long as you place them correctly. Yeah. Yeah. Yeah. So if you, and it's a balance too, because if you've got them at different angles, if you've got a projector at quite a steep angle, obviously the bright, the light closest to you is a lot brighter. Oh, it's brighter. Yeah. Than further away.

**Dave Jones:** Right up the top of the 50 meter, 100 meter tall building. Yeah. If you're projecting from the ground, of course.

**Daryl Tewksbury:** Yeah. So we were projecting sort of from the fifth floor onto this hotel, which was, I don't know how many floors. I can't remember. But anyway, it was pretty tall.

**Dave Jones:** It looks about 50 or something. Yeah.

**Daryl Tewksbury:** Yeah. But, but we were so far away that it was not too bad. We didn't get that much of a difference between illumination, but you could change, you could change the size of your projector. Yeah. It's field of view. You could change that to increase the, the brightness. So there's a lot of things you can do, but basically because of the way the software worked, you could just put projectors anywhere you like and point them at any surface you like. And then you do an, you do an analysis of the total lumens across the building and you get a, basically sort of like a thermal image of the installation.

**Dave Jones:** Oh, okay.

**Daryl Tewksbury:** To show you the intensity differences.

**Dave Jones:** Oh, so an optical thermal kind of, is there a name for that?

**Daryl Tewksbury:** I'm not sure, but you know what I mean? Like, yeah. Right. Yeah. Sort of the brightness, the amount of energy that the total of all the projectors is projecting and where it is. So you try and get that as flat as possible so that when you do put imagery on, it always looks worse with test patterns and things like that because you're looking for inconsistencies. But when you put real content on there, that sort of all disappears and it becomes fine.

**Dave Jones:** Wow. Wow. Fascinating. So from a point of view of how do you calibrate all of these different, you know, if you've got five different, different projectors, all, you know, like surely it obviously has to be done on site. Right. You can't, you've got to manually, do you hold your tongue at the right angle and go, we think they're aligned. You know, it looks good enough. Yeah. How does that work?

**Daryl Tewksbury:** You can do it that way, but that is really difficult, especially when you have more than like one projector.

**Speaker ?:** Right.

**Daryl Tewksbury:** How's it done then? So what we do is we place physical or we either place physical objects around the projection surfaces or we use existing features. Then we take a photo of it, we stick that, we stick that into the software and then in the software, we select those points on the image and that produces white pixels. And then we basically, we click with a cursor that moves like a live cursor through the software. Yeah. We click on the building, the, the dot that we want to align and then we click on where the dot is coming from. Yep. And then we do that to like three or more points. And then it does a reverse calculation to work out what the geometry is and then it realigns it.

**Dave Jones:** Oh, nice. So does somebody have to go to the top of the building and like hold a calibration chart over the edge or something? No, no, no.

**Daryl Tewksbury:** We, no, we just look at it and go, yeah, that, the top left of that window. We take a photo of the surface. Yes. The actual surface. We take a photo from the projector's point of view.

**Dave Jones:** Right. Gotcha.

**Daryl Tewksbury:** And then.

**Dave Jones:** Not, not from the audience point of view, from the projection point of view.

**Daryl Tewksbury:** Yeah. From the projection point of view.

**Dave Jones:** Right.

**Daryl Tewksbury:** If you take it from the audience point of view, the image won't line up on the building.

**Dave Jones:** Oh yeah. Right. Got it. Right. That makes sense. Okay. Gotcha.

**Daryl Tewksbury:** It's actually super complicated to be honest. Like all of them.

**Dave Jones:** I can imagine. It's like not easy. Yeah. That's why I wanted to do like an onsite video or something. Actually, you know, someone's showing us the hardware, like, you know, how do, like, how do we set up and calibrate this building? How many weeks does it take to actually prepare this?

**Daryl Tewksbury:** Yeah. Set up. I mean, there's.

**Dave Jones:** Is it a long process? How, how long would you guys need onsite to set it all up?

**Daryl Tewksbury:** To do an alignment?

**Dave Jones:** Well, to set up the whole shot, like, you know, to get it all. Once you bring in the hardware, how long does it take you to set it all up and get it ready for the show?

**Daryl Tewksbury:** Oh, I think, I don't know, six months.

**Dave Jones:** Oh, six months.

**Daryl Tewksbury:** Oh, yeah. Because it's all cast. These are permanent installations.

**Dave Jones:** Oh, okay. Got it.

**Daryl Tewksbury:** We did mainly permanent ones.

**Dave Jones:** Oh, you did mainly permanent. Not like the, not like the projection on the Opera House for New Year's Eve or something.

**Daryl Tewksbury:** No, I think the only one we did there was the Olympics, which was a while ago. I got it. Laser on the, on the Opera House. On the pylon. And on the pylons. Yes. Yeah. Yes. Yeah. So it's a little bit different. We, we, we didn't have a specific kit that we had together. So when a, when a new job came in, it'd be long months and months of working out what was going to happen and, and then building, like we manufactured all this infrastructure to, to go in, like where all the pumps for the fountains. And we had, we had three, four, 4.5 megawatts of generator sets on site to run, to run the water pumps. So.

**Dave Jones:** Wow. Just the water pumps.

**Daryl Tewksbury:** Yeah. I think it was two, two point something megawatts of pumps to, to do the, you know, to do the fountains and water screens and things. And they couldn't supply enough power. So we had to get these massive gen sets in. So we ran two generators synchronized together at, at any time.

**Daryl Tewksbury:** Yeah.

**Daryl Tewksbury:** And it would swap every day. A different set of two generators would be synchronized together because we had three. So we just wanted to sort of rotate through there.

**Dave Jones:** That's nuts. It is crazy. But that's, that's what I expected. I mean, you know, I expected all sorts of crazy power levels, but you know, I guess that makes sense. It's like it takes energy to pump a crap ton of energy to pump water, physically shoot it up into the air. And yeah, it does.

**Daryl Tewksbury:** It takes a lot.

**Dave Jones:** Whereas if you're just shooting out photons of light, you know, meh. You know.

**Daryl Tewksbury:** Yeah. It's all right. Well, I suppose that the. Hundreds of watts. The. Each projector drew about two kilowatts.

**Dave Jones:** Mm-hmm.

**Daryl Tewksbury:** And there were 60 of those. So that's still a fair bit of power for the.

**Dave Jones:** 60 projectors at two kilowatts. Yeah. Wow. Jeez. Yeah. That's a lot. How, like, how about servicing these things and the meantime between failures and all that sort of stuff for this high powered gear? Did you have a lot of failures? No, actually. Really? Okay.

**Daryl Tewksbury:** Well.

**Dave Jones:** Is it because you over-engineered the hardware or?

**Daryl Tewksbury:** No. Well, the projectors are commercial grade Panasonic.

**Dave Jones:** Oh, okay. You didn't design the projectors yourself. You used Panasonic.

**Daryl Tewksbury:** No, we didn't design the. Oh, well, yeah. No. That'd be a lot. Another lot of crazy engineering. I mean, that would be great. I did. We did. Because we bought so many of those Panasonic projectors, they actually flew myself and another one of our guys across to the factory. We went through the factory and watched them, how they manufactured these projectors. And that was super interesting. And also at the same time, they were producing, at the time, their brand new laser light engine for their new laser projectors.

**Dave Jones:** Right.

**Daryl Tewksbury:** I got a sneak peek into this room that they had with like kilowatts and kilowatts of laser modules all running full pelt.

**Dave Jones:** Oh, wow. What, they were burning them in, were they?

**Daryl Tewksbury:** Well, I think they were doing, trying to graph their performance over time. You know, how much life you can expect to get out of them, basically. Yep. So that was, it was a super scary room where you weren't allowed in. And it had like a, the window into the room was like welding glass sort of thing. Yeah. And you could just see all this light in there. It's like amazing.

**Dave Jones:** Wow. If you, if you go in there, geez, it'd burn you before it'd blind you and burn you, right?

**Daryl Tewksbury:** Yeah. Yeah. You wouldn't want to, although they weren't collimated. So I don't think.

**Dave Jones:** Oh, okay. Right.

**Daryl Tewksbury:** Yeah. But anyway, you probably don't want to be in there when they're doing that. I mean, the laser, laser projectors are actually quite a fascinating thing in themselves. I don't know if you are aware what they actually, what that means. No. What they do. Please, please, please tell us. Yeah. So a laser projector, it's sort of is, it's probably not what you're imagining, but what it is, is super high power blue laser diodes in a module, a whole stack of them in an array. And then the blue light is sort of collimated and controlled into a, into a source of a particular size, maybe five millimeters in diameter or something. Right. And then that shoots through a wheel, which has different colored phosphors on it. So as, so as the wheel rotates around, it'll get to the green phosphor section. And then the blue light, of course, will be converted with quite decent efficiency into, into green light. And that's your green light source. And then of course.

**Dave Jones:** I had no idea.

**Daryl Tewksbury:** Yeah. Blue would be.

**Dave Jones:** Does it, does it, does it pass through the material or does it reflect off the material?

**Daryl Tewksbury:** It looked like it passed through the material.

**Dave Jones:** Right. Okay.

**Daryl Tewksbury:** From what I can remember.

**Dave Jones:** But wow. They would have a certain life, wouldn't they? Those phosphors. The phosphors. They wouldn't last forever. Yeah. I imagine they wouldn't last.

**Daryl Tewksbury:** Yeah. You can make the, make the wheel bigger so that the density across the, the phosphor is not as high.

**Dave Jones:** Right.

**Daryl Tewksbury:** Like, cause it's obviously the surface is spinning faster because the wheel's bigger. So they obviously work out how long the path needs to be so that that energy is not, you know, obliterating the phosphor.

**Daryl Tewksbury:** Right. So it creates the red and the, and the green. And, and some of them do a lot of other colors as well. Like maybe yellows to get a nicer gamut of, cause they're not really limited to, you know, they can make whatever colors they like.

**Dave Jones:** Okay.

**Daryl Tewksbury:** And then that light goes onto the standard DLP, which is producing, you know, the red image, the green image, the blue image to produce white light, but they're pretty good.

**Dave Jones:** Right. At what power level were we talking about these laser projectors?

**Daryl Tewksbury:** 30,000 lumens.

**Dave Jones:** 30,000. Ooh. Okay. Yeah. Wow.

**Daryl Tewksbury:** This is the biggest one that I, that I know of or that I last saw or 35,000, something like that. Quite big, quite bright. Got it. Actually, I don't know what a domestic projector is, how bright they are, to be honest.

**Dave Jones:** Oh, I, no, I, I think they're like sub, like a thousand lumens is a big one, I think, or it was years ago. Maybe they got better ones these days, but I think it's in that order. I could be wrong. Don't quote me on that. Can we, can we get onto the electronics side of things? Cause you've done electronics and firmware side of all this as well, including FPGA stuff. Can you tell us what, you know, challenges were there in that? What were the FPGAs used for and stuff like that?

**Daryl Tewksbury:** Yeah. So let me, I'll try and do a brief explanation of what was there when I arrived first at Laser Vision. They had a device called, well, they called it a digital data pump, which was what output all the different media types, audio and laser control and, you know, serial format. And all that sort of stuff. A lot of ADAT actually back then, but the IO, so it was a, it was sort of based on a computer and the software that did all the synchronizing of them with the media, like on a timeline. And they had hardware inside the computer, which would convert all these different, it would be basically the codec for all the different communications types, like serial data or DMX or MIDI or, or whatever fiber outputs. So I thought, oh, you sort of limited there because you've got the, the, the speed of the, was, I think it was PC 104 that we're using back then, or was it ISA? One of the others. Oh, okay. Right. Yeah. So you had a limit. I think it was a 4.77 meg or eight meg limit on the data rate of that. And I thought, well, that's not super scalable. And now we're using multiple playback units to get more outputs. So what I wanted to do is to sort of divide that in half and say, well, we can do all the sequencing and everything on the computer with new software. But what we want to do is create a device that can do the media conversion in a separate box on something that's a little bit more expandable than say the PCI or ISA slots in the computer. So I thought, well, networking is pretty popular now. And that seems to just be getting bigger and bigger and bigger and scalable. So let's. What, what year are we talking about here? So we're talking about 12, 13 years ago. So whatever it was. Okay. Yep. And so that's where this whole thing came about. I needed to find a processor that I thought was fast enough to deal with the amount of data that one device would have to look after.

**Dave Jones:** Mm-hmm.

**Daryl Tewksbury:** And so I found one that was, I think, a 174 meg ARM9 based single board computer running a real-time operating system. And then on the, on its bus, I memory mapped a Cyclone 3 Altera FPGA.

**Dave Jones:** Right.

**Daryl Tewksbury:** So that gave me something that I could do processing with, which was the ARM9. And then something that I could build my codex in. So I might want 10 UARTs or I might want, you know, an SPI something or ADAT input output or audio. So I would design up all these, I didn't use any IP cores. I probably should have. And it would have saved me a long time.

**Dave Jones:** Yeah. Right on your own from scratch. Yeah. That's reinventing the wheel.

**Daryl Tewksbury:** But I just did all my, all my UARTs and, you know, SMPTE generators and decoders and stuff all. And I did it in schematic capture, believe it or not.

**Speaker ?:** So.

**Dave Jones:** Oh, okay. Right. Oh, yes. None of that, none of that VHDL rubbish. None of that VHDL rubbish. No, no.

**Daryl Tewksbury:** Schematic capture all the way. I'm putting gates down, man.

**Dave Jones:** You're damn right.

**Daryl Tewksbury:** So, yeah. And I'd never done any FPGA work before then, but I thought, how hard can it be? You know, I've got YouTube. I'll just learn how to do it.

**Dave Jones:** Well, that's the thing with schematic capture, right? It's, it's just your traditional digital design, right? You don't have to learn anything new, right? You don't have to learn a high definition language.

**Daryl Tewksbury:** No.

**Dave Jones:** Or a high definition hardware language.

**Daryl Tewksbury:** No, you have.

**Dave Jones:** So, yeah, just put the gates.

**Daryl Tewksbury:** You have to learn about the intricacies of timing with FPGAs. Oh, of course.

**Dave Jones:** Yep. And, you know, how to map them to the fabric and the limitations and all that sort of jazz. But, no, but that's still just basic digital. You don't have to really relearn anything. Really? No. To do schematic capture.

**Daryl Tewksbury:** No. I mean, it's, you know, it takes you long enough to figure out how to use Quartus in the first place.

**Dave Jones:** Yeah, right.

**Daryl Tewksbury:** That's, you know, that's a whole. Oh, terrific. A whole nother level of pain.

**Dave Jones:** Yes, it is. Oh, boy.

**Daryl Tewksbury:** But actually, there were some frustrating times because I remember having some designs which were not working. Well, not working properly. And it was very difficult to figure out, you know, to debugger an FPGA. So, you'd go into the design and you'd start to pull out test points and throw them at pins so that you could put the oscilloscope on it. And the thing that really annoyed me was the fact that when I put the test pins on, made the circuit work.

**Dave Jones:** Yeah.

**Daryl Tewksbury:** So, you know, you'd go and test it. It's working 100%. I shouldn't laugh at it. And then you go, oh, maybe I just misinterpreted. So, you'd pull the test points off and it stopped working again. So, that was pretty frustrating. Obviously, the rerouting was what was causing the timing differences to make it work.

**Dave Jones:** Right. Got it. Oh, so it was timing. I mean, it wasn't like an internal loading thing. It was a timing issue.

**Daryl Tewksbury:** No, I think when you added the test points, it routed some signals through a longer path or whatever. Yeah. And you ended up with. So, what was on the brink of working became probably only just working, but working nonetheless.

**Dave Jones:** Well, that can be the difference between a synchronous and an asynchronous design, right? If you've got a synchronous design, you're less where everything's, you know, done through registers and clocked all at once. Your timing, well, I'm going to argue, is less critical than it is with an asynchronous design. So, anyway. And then you've got different clock domains. Yes. Let's not get into the clock domains.

**Daryl Tewksbury:** I learned pretty early on that relying on combinatorial logic alone is really not a good idea. Right. Because of all the intermediate states before your final stable result.

**Dave Jones:** Got it. You've got to know the propagation delay. So, yeah. If people don't know, if you're doing some combinatorial logic, if you've got like 10 gates in series all doing something, it takes time to propagate through all those 10. And then if you're latching that output, you've got to know when to latch that output, you know.

**Daryl Tewksbury:** Yeah. Because if you look at the output of that logic fast enough, you will see all the intermediate states. Yeah, states. That occur during that period, the very short period, sure. But, you know, if you feed that as a clock source into a counter.

**Dave Jones:** Oh, you're screwed. There goes your counter.

**Daryl Tewksbury:** You'll find that your counter is counting at bizarre numbers.

**Dave Jones:** Love it.

**Daryl Tewksbury:** So, you want to keep a bucket of D flip-flops at hand.

**Speaker ?:** Right.

**Dave Jones:** Oh, I love it. All classic combinatorial design issues, you know. Yeah. It's just, yeah. Oh, fantastic. So, in the end, this was dedicated hardware that went, that was a box that connected to the PC how? It was just a networked thing? It was an internet?

**Daryl Tewksbury:** Yep. So, I came up with a protocol that used UDP only to communicate to and from the computer to all these boxes. Yep. It's a lot more complicated than it seems because each one of these devices had one FPGA in it. And the FPGA basically ran a 48 meg 64-bit counter as its master timing value. And that was sent back to the main synchronizing computer, which had all the media control in it, so that it would profile all the boxes on the network and have reference points to the computer's clock versus the 64-bit clock in each device.

**Dave Jones:** Right.

**Daryl Tewksbury:** So, all the data that was sent out was scheduled. Say you had 10 of these media boxes out there doing audio or whatever, each one would get a packet of, say, samples for audio and then a timestamp relative to that 64-bit counter as to when that sample had to be output.

**Daryl Tewksbury:** Mm-hmm.

**Daryl Tewksbury:** So, that's how I could synchronize all these things out in the world with no clocks. Right. Like, no master synchronous clock because I just profiled them all. And I knew that when I sent a packet to device number one, these packets had to be synchronous with its counter value at blah time.

**Dave Jones:** Oh, wow. Okay. Gotcha.

**Daryl Tewksbury:** Yeah. So, I could basically, as long as it was done ahead of time, and I had like 100 millisecond of scheduling time. Yep. Yeah, plenty. Yeah. So, you know, effectively, I could schedule an audio sample to be within 25 nanoseconds of another box's audio sample.

**Dave Jones:** Oh, nice. That's pretty impressive.

**Daryl Tewksbury:** Now, obviously, you'd probably have to add network jitter and stuff onto that as well.

**Dave Jones:** Right.

**Daryl Tewksbury:** Because the timing packets coming back from each device obviously has maybe bit variable time. Yeah, of course. That's how you set your QoS on your network.

**Dave Jones:** Right. Would you do it all differently these days? Like, would you just, like, are PCs that good and, you know, embedded PCs that fast and capable that you wouldn't do dedicated hardware anymore? Or is this something you'd still do in dedicated hardware if you had to redesign this?

**Daryl Tewksbury:** Yeah. I've thought about that because I wanted to redesign a system similar to this. Right. And I probably would still go down the dedicated. You can't be turning on it. You know what I hate? I hate boot times. Hate boot times.

**Dave Jones:** Yes.

**Daryl Tewksbury:** So, when I design something, I want it to be running pretty much after you press the power button. Yep. So, I don't like having huge OSs, you know, unnecessarily in devices. So, yeah, I would take, like, my favorite thing at the moment is the DE10 Nano. I don't know if you've heard of that.

**Dave Jones:** Oh, yes. Yeah. Yeah. I've got one. Yep.

**Daryl Tewksbury:** Yeah. So, that I've been playing with, you know, trying to get back into VHDL. And I've been writing some cores for that and playing. And that's an awesome device. I love how the stripped down version of Linux on there is super fast booting. Right. And, you know, like, it's an FPGA. It's hardware. I want some gates. So, I've been doing some stuff with the HDMI output and just playing around with. And that's so capable, that thing. That's actually quite an expensive FPGA on the DE10. I don't know why they're so cheap to buy.

**Dave Jones:** Oh, well, they're probably, yeah. I'm sure they've got a deal with, it's all subsidized, I'm sure. I don't know if they supply them to them. But, yeah, they would get good deals. Trust me.

**Daryl Tewksbury:** Yeah, I'm sure they are. But when I looked up that particular FPGA, I'm like, oh, that's quite expensive.

**Dave Jones:** Yep. Oh, yeah. And that's a, it's not just an FPGA. That's got a dual core arm in it as well. Yeah.

**Daryl Tewksbury:** Yeah. 800 meg, I think it is. Oh, no. Yeah, yes.

**Dave Jones:** Yes, it's 800 meg and it's got one gig of DDR3 gigabit ethernet.

**Daryl Tewksbury:** It's astounding. It's amazing. Yep.

**Dave Jones:** Yeah.

**Daryl Tewksbury:** I mean, I'm using it to play retro games mainly, but still.

**Speaker ?:** Right.

**Dave Jones:** So, you would use something like that these days for the instant boot time?

**Daryl Tewksbury:** Yeah, totally.

**Dave Jones:** Although, if one of these systems went down, like during a show, for example, how long would it take to reboot the whole thing? Would you even be able to reboot and start off where you left off?

**Daryl Tewksbury:** Yeah. So, I designed the system so that, one, you could have a backup computer ready to go if you wanted to. And it would. Oh, does that auto switch in? No, it doesn't.

**Dave Jones:** Is it a redundant?

**Daryl Tewksbury:** We were going to do that, but they didn't want me to spend the time to do the development on that.

**Dave Jones:** Yep.

**Daryl Tewksbury:** It could totally have been done that way. But basically, this system is not... I tried to make it super easy for people to build them. So, like the file that runs the whole show is one executable file. There are no DLLs needed. Oh, wow. I've statically linked in all the libraries. So, it doesn't require any installation. You can put the media directory and the executable file on a thumb drive, plug it into any computer. Oh, nice. Stick it in the network. Just double click on the exit file and it will run the whole show. You don't have to do any configuration. No, that's brilliant. In the actual shows themselves, so if you can imagine a timeline with audio tracks, video tracks, MIDI tracks, whatever. What you do in a show is you deploy each track to a specific hardware output on a specific hardware box. So, that data is stored in the show file. So, when you run that show, that will always play the appropriate media on the appropriate outputs on the appropriate bits of hardware.

**Dave Jones:** So, are you saying the single XE contains all the media material as well? Like the audio and video?

**Daryl Tewksbury:** No. No, there's a media folder that you hang off that directory. Oh, okay. You hang off it. Right. Yep. So, in that media directory, it's got audio, blah, blah, blah, blah, all the different media. But you can copy from where the XE is and the directory off that and move that wherever you like.

**Dave Jones:** Will like and then just run it.

**Daryl Tewksbury:** And just run it. Yeah.

**Dave Jones:** So, if a PC fell over, somebody else could bring in their laptop and just plug it in and get it running again.

**Daryl Tewksbury:** Yeah, basically. Yeah.

**Dave Jones:** Nice. Wow.

**Daryl Tewksbury:** Yes, that's super easy that way. Because a lot of the other systems are so complicated to set up. And all the devices are the whole self-discovery mechanism. So, if you unplug one of the media servers, which might have eight channels of audio on it, obviously the eight channels of audio go away. Those tracks in the show will start flashing orange saying that that output's no longer available. But if you plug that device back in, once it's booted up and re-synchronized, it'll continue to output the audio and everything again. And the show will go green on the timeline. So, it's...

**Dave Jones:** Right.

**Daryl Tewksbury:** You know, I've taken care of what happens when things go away and come back. Because, obviously, if you reboot one of those remote servers, its 64-bit counter is now lower than it should be. And it can never go backwards. Oh, interesting. It's easy to tell when a device is rebooted because that number is now lower than it was last time you profiled it. So, you know that it's restarted.

**Dave Jones:** Aha. Clever.

**Daryl Tewksbury:** Because a 64-bit number running at 48 megahertz is about a 126-year rollover time.

**Dave Jones:** Right.

**Daryl Tewksbury:** And I figured that that was probably long enough.

**Dave Jones:** That's probably enough. Yeah.

**Daryl Tewksbury:** The assumption was that if that number is less than it was last time, something bad's happened.

**Dave Jones:** Right. And that would just stay in non-volatile memory in the box, would it? The counter?

**Daryl Tewksbury:** No. So, the counter starts at zero every time you power it on.

**Dave Jones:** Oh, yeah. Right. Every time you power it up. Okay. Gotcha.

**Daryl Tewksbury:** Yeah. Right. Yeah. So, it always starts from zero. And it's in the FPGA. It's just a counter in the FPGA. Yep.

**Dave Jones:** Nice. Nice. Are there any, like, show failures that you've had, like, in the middle of shows? Has anything, you know, gone wrong? Although, you said you do mainly, like, permanent installations and stuff like that, where I imagine that's not as big a deal as it would be for somebody running a show on, you know, New Year's Eve or something like that. Yeah.

**Daryl Tewksbury:** Yeah. So, New Year's Eve is so stressful because you've got so many people out there and it's a one-time deal. It's a one-time shot.

**Dave Jones:** Yeah. You've got a million people on Sydney Harbour all, you know, they're flowing in from around the world to be there. Yeah.

**Daryl Tewksbury:** It's such a stressful time. Oh, my God. But luckily, the system's been super reliable. I mean, I've put a lot of work into it over the years, finding little memory leaks or whatever, which has been so difficult in some instances. But, yeah, luckily, even if because the actual application that I wrote to do the playback of the shows is so multi-threaded, a part of the application can lock up and it'll only be, like, that one media track that'll go away. The rest of the show will keep playing completely until the end. So... Brilliant. But that hasn't happened for a long time. I think I've pretty much got rid of all the bugs in there. So it's pretty... And we've never had one of those hardware boxes fail.

**Dave Jones:** Oh, fantastic. Is that because you're over-engineered them from, like, a power point of view or something or some other point of view? Yeah, totally.

**Daryl Tewksbury:** Yeah, totally. I mean, it's not a build-to-price product, so...

**Dave Jones:** Right, no, of course. You build one off, right, or five of them or something.

**Daryl Tewksbury:** Yeah, yeah. So they're sort of...

**Dave Jones:** How many of these boxes did you build? Or you build one for each installation, right?

**Daryl Tewksbury:** Well, no, no. Installations, we use many of them.

**Dave Jones:** Oh, okay.

**Daryl Tewksbury:** So I think in Dubai, they use, like, 20 of them or something, so...

**Dave Jones:** Right, okay. So you might make 100 of these.

**Daryl Tewksbury:** In total. I don't think I've broken the 100 serial number yet.

**Dave Jones:** Oh, you haven't broken triple digits.

**Daryl Tewksbury:** No. Nice. So there's been less than 100 of these things made.

**Dave Jones:** But they're... That sounds like the business I came from, yep. Yeah. You know, you make 10 of something. Oh, that's a big production. That's a big order. 10.

**Daryl Tewksbury:** Yeah, if you've got 10 of these things sitting on the shelf, you're like, oh, yeah, look at me. I'm mass producing.

**Speaker ?:** Yep.

**Daryl Tewksbury:** And a lot of them are custom. So the beauty of doing it all in-house like this is if someone needs to control a piece of gear, like did happen, actually, in Abu Dhabi. We did installation and we had a whole stack of VFDs that we needed to control for another fountain thing. And I thought, well, it's a pain in the ass because what we were doing before was using... Have you heard of DMX? Anyway, it's a lighting... Yes. Yeah, I've heard of it. Yeah.

**Dave Jones:** A lighting thing. Yeah.

**Daryl Tewksbury:** So we had DMX to analog converters to do zero to 10 volts, which we fed into the VSD to control the VFD, VSD. I don't know. People call them different things. But to control the speed of the motors. But later on, I'm like, oh, you know what? We should order these with Modbus interfaces and I'll write a Modbus module and we'll control them by Modbus because we've got a lot more control. We can control a lot more parameters and get feedback and stuff. So, yeah. So I wrote a Modbus thing for it and that went out over 485 and that was much easier to do control. But I also wrote an Ethernet Modbus. We haven't used that yet, though. When I say we, I'm not working there anymore.

**Dave Jones:** Right. Yeah. So all of your gear is still working? Yeah. The company is still using all the gear you designed? They haven't changed it?

**Daryl Tewksbury:** In some installations, they have. Right. Because I think that they want to go more down the road of getting off the shelf stuff now.

**Dave Jones:** Oh, okay. Right. And there's companies that offer such solutions.

**Daryl Tewksbury:** Yeah. There are a lot of control systems out there, but you sort of have to hack them together. Right. This was a sort of man of many talents type system where all of your media would come out of this system. This would do, this would synchronize everything together. But what they generally do now is maybe have a master lighting desk or something outputting SMPTE time code. And then they would have, like the laser system would be a pangolin laser system, which would be sort of on its own. And that would be synchronized with whatever was playing back the audio. That was some other system. And then whatever was doing the video would be some other system. We wanted to have the whole lot as one cohesive lump, which was sort of cool. So you could adjust timing between. It was all on just one timeline, but now they're doing it with many different manufacturers, products all sort of connected together somehow. Yeah.

**Dave Jones:** Did you work on any power stuff, power supplies, power drivers, anything like that?

**Daryl Tewksbury:** Not whilst I was there. I did play around a lot back in the day. I was sort of fascinated with inverters and high power switching and switch mode power supplies, like the black magic that happens inside those things. And so I've always been sort of fascinated with that, but it's never been my job. I designed a high pressure sodium ballast a long time ago, a solid state version of that, which was pretty cool, but never did anything with it. Got it. It was supposed to sell them, but it ended up being, you know, the bomb was too expensive. And I sort of probably went through the catalog of MOSFETs and went, oh yeah, I'll put 200 MOSFETs in. That'll be beautiful.

**Dave Jones:** Oh boy. So what are you up to these days since you left Laser Vision?

**Daryl Tewksbury:** So now I'm working for a company now that does a lot of like, I don't know what you would call it, like HVAC systems in buildings, big buildings. So they have a whole stack of controllers and I'm designing a new sensor suite for them. So that will be, it's a touchscreen, a little small touchscreen sensor, which can be temperature, humidity, CO2, CO, refrigerant gas.

**Dave Jones:** Got it. I imagine there's lots of off the shelf solutions for that though.

**Daryl Tewksbury:** Yeah, there are. But I don't know if there's any Australian ones. This company has been going quite a while and got a pretty good name in the business industry.

**Dave Jones:** So you want to design and manufacture here or?

**Daryl Tewksbury:** Yeah. So we've got our own, you know, stencil solder paste machine. And we've got a pick and place machine and a reflow oven.

**Dave Jones:** But once again, it wouldn't be high volume, would it? It'd be, what sort of volume are we talking about?

**Daryl Tewksbury:** Sort of in the thousands.

**Dave Jones:** Okay. That's lowish volume still. It's manageable.

**Daryl Tewksbury:** Manageable. Just trying to work on how I'm going to do calibration and testing in a bit of a better way. But yeah, we're still working. I'm still working on the hardware at the moment. So we've got two processors in there. We've got the STM32 and an ESP32. ESP is driving the display because they're quite a cheap. I like the... Oh, yeah. I like the fact that the ESP32 being a low pin count processor, even though it's a dual core 240 megabit, it's not a slouch. No. And it's got a decent amount of RAM and flash. But I really like the switching fabric around the pins. So you can...

**Dave Jones:** Yeah, you can route them. Yeah.

**Daryl Tewksbury:** You can route any hardware device to pretty much any pin.

**Dave Jones:** Yep.

**Daryl Tewksbury:** That's very nice. Which is great. Like, rather than having a BGA with super fine small balls on it, you've got this one QFN package, which, like, it's great. Because you don't normally need so many pins. You just need to be able to use whatever combination of hardware is available for whatever you're doing sort of thing. So I actually... I wish more products would start doing that so you can just switch the outputs to whatever you want.

**Dave Jones:** Got it. Well, Daryl, thank you very much. I don't believe our amp hour is up. But that's been fascinating. Thanks for sharing your laser vision story. I've always wondered how these things worked.

**Daryl Tewksbury:** Yeah, I don't know how much I rambled and how much information I passed on, but it's actually a pretty exciting time for me back then.

**Dave Jones:** How long did you work there?

**Daryl Tewksbury:** Overall, about 12 years or something.

**Dave Jones:** Okay.

**Daryl Tewksbury:** There was a time in the middle where I went away and came back, but... Got it. Yeah.

**Dave Jones:** Fantastic. All right. Are you on the interwebs, on the socials, on the Twitters? Or anything like that? Can people follow you anywhere? You got any personal work? Stuff like that? Are you a man for hire? Well...

**Daryl Tewksbury:** We should day job keep you too busy. At the moment, my day job is keeping me pretty busy. Occasionally, people contact me and ask me for help on things, which is fine. But I'm not... Yeah. I'm not really doing the social thing. I mean, of course, I'm... Wise man. Yeah. Yeah. Yep.

**Dave Jones:** That's good. Stay away.

**Daryl Tewksbury:** All right. Too busy, I guess.

**Dave Jones:** Yep. Too busy doing real hardware. Yeah.

**Daryl Tewksbury:** Yeah.

**Dave Jones:** Ah, fantastic. All right. Well, thank you very much, mate. Appreciate it. Well, thanks for the opportunity. It's been good.

**Daryl Tewksbury:** No worries, mate. All right. Catch you next time. See ya. Today's episode was projected like lasers out of Dave and Daryl's mouth and into your earballs, courtesy of our patrons. Join the club at patreon.com slash theamphour and join our Discord to talk FPGA's ESP32s and, yes, lasers. A special thanks today to our corporate sponsor, Vino. We'll see you next time.
