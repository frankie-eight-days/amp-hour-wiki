---
episode: 483
title: An Interview with Adrian Tang
url: https://theamphour.com/483-an-interview-with-adrian-tang/
---

**Adrian Tang:** This is the Amphour Podcast, released on March 8th, 2020. Episode 483, sponsored by Roden Schwartz. An interview with Adrian Tang. Welcome to the Amphour. I'm Chris Gammell of Contextual Electronics.

**Adrian Tang:** I'm Adrian from the Jet Propulsion Laboratory, and I build microchips to search for life in space.

**Adrian Tang:** Hey, Adrian, that is a heck of a cool title there. Like, what kind of life are we looking for here?

**Adrian Tang:** Any. Any life? Any life would be interesting. Even signs of life would be interesting.

**Adrian Tang:** Okay, yeah, it's just kind of, it's just like scrolling through and just trying to find something to blips or bleeps or moves or anything, right?

**Adrian Tang:** Exactly.

**Adrian Tang:** Okay, cool. And so you're at JPL? Yep. How did you kind of get there? I mean, first off, I didn't know JPL actually made their own chips. I kind of always assumed it was off-the-shelf stuff, but that's kind of a silly assumption. What is it like where you're making your own chips out there?

**Adrian Tang:** It's a long and interesting story. I like long and interesting stories. So I am the only chip designer at JPL right now.

**Adrian Tang:** Okay, this is why I haven't heard of you.

**Adrian Tang:** Yes, and I only got here a couple years ago.

**Adrian Tang:** Okay.

**Adrian Tang:** How this all started, and it's kind of funny. When I was a PhD student at UCLA, I was working on as my PhD topic, very high frequency circuits. So you can look up some of the old stuff, up to 400, 500 gigahertz type receivers.

**Adrian Tang:** Uh-huh. At that point, I kind of don't even, I can't even conceptualize what that is. You know, like that's crazy fast.

**Adrian Tang:** It's like radio, but shorter. Right. So we built these chips, and one of the interesting things is although we could build the chip quite readily, we couldn't measure the chip, which is a big part of building the chip. And we just happened to be close enough to JPL that has a large submillimeter group here that does a lot of terahertz work for space instruments that we started coming up here to do the measurements. Oh, interesting. And we were doing these. So, you know, JPL instruments at these frequencies cost millions and millions of dollars, right? And here I am doing the CMOS stuff, and it's like nickel and dime circuits. So they got into it, and it's like, well, when you graduate, why don't you come here and keep doing that? Nice. Sure enough, that's what happened.

**Adrian Tang:** So what are your terahertz circuits you use for? I mean, that's starting to get up into the realm of like light, isn't it? It's not IR. No, it's not even close to IR.

**Adrian Tang:** Okay. So what's the relative measure? Well, I'd have to work it out. It's like a factor of 10 to 100, typically, I think. So there's some number of orders of 10 there between IR and where we are. But terahertz, we have a couple of applications here at JPL. But our bread and butter is a terahertz spectroscopy. So let me try to explain this reasonably well. So what happens is, if you're familiar with radio, you know there's a floor, which is the KTB or KT, which is the thermal noise floor, the Boltzmann constant times the temperature of wherever you are. And that's kind of white or flat noise. When you have gases in an environment, especially when the pressure is low, what happens is they tend to emit at certain frequencies. But those frequencies for gases you'd be interested in, in looking for life or figuring out an atmospheric process or something, they're all across the like 50 to 500 gigahertz regime, that kind of place. So like ammonias are in the 490s. If you're looking for water, it's got a line at 180 gigahertz and 557. And that's how we search for life. You can't really use an active measurement because if you're flying by a planet or something, you're not going to carry a transmitter that's going to light up a whole planet. So you have to do these passive techniques. You look for signals in the noise floor.

**Adrian Tang:** Wow.

**Adrian Tang:** Kind of like the shape of the noise floor. But the catch is the molecules only emitted these terahertz bands, which is what forces us to build our instruments at the terahertz band.

**Adrian Tang:** And you say like these are emitting at terahertz bands, like...

**Adrian Tang:** All gases emit at somewhere in the terahertz band.

**Adrian Tang:** That's interesting. So I've never even come close to hearing about this. So what is like the natural phenomenon that's causing that emission to happen?

**Adrian Tang:** Yeah, there's like a good chemistry explanation that I'm going to skip, but I'm going to give you an engineer's approximation. So the molecules of the gas have a resonance. Okay. So what they do is they take in the broadband thermal energy everywhere and they kind of filter or shape it with their resonance. So they cause peaking in your noise spectrum. Now, there's some conditions on that. First of all, when you're in like the room here and everything's warm, you can't really see this because it's all at the same power level. So usually you need a warm gas with a cold background. So you have contrast to see these things popping up, which is why... Like in space. Like in space, exactly. So one of the most popular techniques is called limb sounding. So what you do is you sit on orbit. MLS is an instrument that we worked on here at JPL before I got here, the limb sounds. What you do is you look at the atmosphere at an extreme angle. So you're not looking at the earth. You're in orbit and you're looking through the atmosphere into space in the background. And then you can map all the pollution and what it's doing. And you can map about 30 or 40 different species in a terahertz band of ozone, oxygen, ammonia, nitrous oxide, ozone. I think I said already carbon dioxide. There's lots of stuff.

**Adrian Tang:** Yeah. Okay. So basically when Mr. Spock is doing some kind of scan on a planet, this is the kind of stuff you would be doing.

**Adrian Tang:** Yeah. That's the first condition is that you have to have a cold background. The second tricky one is the pressure has to be low. So if you know filters, like if you have a filter and you DQ the filter to the point where the Q is very, very low, much less than one, it doesn't look like anything anymore. It just looks like straight line. The molecules are the same. If you have lots of pressure, like atmospheric pressure, 100 kPa, suddenly it's DQ'd and then you don't see a line anymore. So you need to do this where the pressure's low, like up at the top of the atmosphere, or if you're on the moon or something where there is no atmospheric pressure and there's just volatiles or something leaking out of the soil, you'll be able to see that.

**Adrian Tang:** Yeah. Wow. Okay. And how do you, how do you differentiate? I mean, like, so I imagine that you have to filter this down because it's, I'll get to that later, I guess. But I assume that there's a simplified output because getting wideband would be really crazy. So you have to do like super narrow output.

**Adrian Tang:** So typically, there's a lot of engineering in that. So the first thing is, you know, from a discovery point of view, if you're sending a mission to another planet or something, that spacecraft is going pretty fast, right? So you don't want to spend hours and hours and hours with a little one megahertz bandwidth searching gigahertz and gigahertz bandwidth, because by the time you've searched, your vehicle has gone somewhere else. Right. So there's a huge drive to try to process as much bandwidth as possible all at once. But obviously you can't build an ADC, which is the key to the whole thing that has a hundred gigahertz bandwidth. That's silly sounding. So you have to do a trade off. Usually we do a heterodyne receiver, you know, 300 gigahertz, 400 gigahertz, 500 gigahertz, whatever band. We'll down convert to an IF and then we'll bring it, we'll digitize that with a single chip and try to bring it in three gigahertz at a time or something, and then try to compute the world's most power efficient FFT.

**Adrian Tang:** And that's just because of the amount of cycles you would need to do on it or because you'd actually be on a spacecraft?

**Adrian Tang:** So you're talking about an FFT processor behind this ADC. So the ADC has got a clock, maybe six giga sample, which is more than commercial ones usually do. And then you have to process an FFT. Typically we're on the order of 4,000 or 8,000 point FFTs. So a lot more intense than Wi-Fi or something uses. And you have to think about the power requirements too. If you do a planetary mission to another planet or something on a CubeSat or a SmallSat or something, which is what we're all talking about now, you know, your instrument power budget might only be 50 watts, which means, you know, forget the FPGAs and stuff. You've got basically a watt to two watts to compute that FFT at six gigahertz clock.

**Adrian Tang:** Right. Yeah. Right. That's a lot of, that's a lot of ups and downs. Yeah, exactly. So I assume this is where the custom silicon piece comes in because you need to actually have like a very specified thing instead of the FPGA, like you mentioned.

**Adrian Tang:** Yeah, well, we find roles. So let me talk. It's interesting to be at JPL. That's a, that's a cool thing. I'm a CMOS guy. I've been doing commercial CMOS before I was here. So I'm, you know, YLAN, Bluetooth, that type of stuff, those designs, those radios. When you get to JPL, you have to understand there's a superconducting group here. So they have quantum level sensitivity detectors and there's a M-Kit or a kinetic inductance detector group here. And there's a, you know, shocking mixture group here that build all these really, really sensitive. They're not, they're not commercial detectors. They're the best science and physics can offer us. So the idea that you're going to come in with some pieces of silicon and displace this technology is joke. What we have to do is we have to pick our spots and say, where does it make sense to save power or whatever? That's not going to destroy the sensitivity of these instruments. So the three places we found a home in are backend processing and digitization, of course, of building ADCs and building processors. The second place we find a home in is synthesis. So a lot of these systems, they don't have the LO directly at whatever crazy frequency. We typically synthesize with a synthesizer somewhere around 100 gigahertz, 200 gigahertz, which is reasonable, and then multiply up. One of the things I probably should have said by now is I've been talking mostly about planetary exploration. But there's a huge side of JPL here that's astronomy based, looking at distant galaxies, distant stellar objects, figuring out how stars form, figuring out what galactic motion looks like. And they are usually looking at much simpler molecules like ionized oxygen, ionized carbon. Those frequencies are much higher. Our group goes up to about four terahertz now.

**Adrian Tang:** Oh, my goodness.

**Speaker ?:** Okay.

**Adrian Tang:** So you can look up Jose or Gatom. They've done work up to 2.7 terahertz, I believe. And my group's working on a telescope right now that has a two terahertz channel. And we have some R&D work to go up to 4.7 terahertz as well. So they get very high. Those detectors are always, you know, they're cryogenically cooled. They have to be in a vacuum. They're in a doer. And they're optically coupled. The LO is not piped in. It's optically coupled. And then my role is to provide the synthesis for that down at 100 gigahertz that they will multiply up to their frequencies. Also provide the back end. So then they have a mixer somewhere. They down convert those very high frequency bands to very low frequencies. Well, 3 gigahertz is low relatively.

**Speaker ?:** Okay.

**Adrian Tang:** We'll digitize them and compute the FFT and extract the spectral features and return them to the computer.

**Adrian Tang:** Wow. And then, so, okay, maybe we could have like an example. So maybe one of these example systems you're talking about here, that would be good to kind of make a visualization in people's mind's eye. What does the actual interface to the physical realm look like? Is it optical? Is it an antenna? Or what is it?

**Adrian Tang:** It's a mix. So it's all quasi-optical. Let's say above 200 gigahertz, it's pretty much all quasi-optical. So you're looking at a horn antenna, which is a feed, coupled to either a lens or a parabolic reflector.

**Adrian Tang:** Because this is like starting to smush together like photons and electrons. And my brain's starting to melt here. You'll have to excuse me. This is way out of my league already. So there's an antenna, but there's optical, you're saying?

**Adrian Tang:** Antenna is a complicated topic. Well, you can use a lens or you can use a reflector antenna. So one of the biggest things to think about, the game is diffraction-driven, right? So if you have an aperture, some antenna, and you're some distance away, your spot size of that distance will be lambda d over r. Where r is the radius of the antenna, d is the distance away, lambda is the wavelength. So the bigger antenna you have, the more you can focus. The more you can focus, the more resolution your measurement has. You're resolving this planet at one kilometer scale or half a kilometer scale or 100 meter scale. The problem is you can't have an infinitely big antenna in space. So you have to get creative with the space you have. Got it. Yeah. And then, you know, beyond that, you say, well, what antenna can we tolerate? What resolution do we need? And then you have other knobs you can turn. You can start to play with trajectories. You can start to do really close flybys with really high apogees or something in order to get you the resolution at some moment. The other thing is generally the closer you get, your relative velocity gets worse and worse and worse. So then you have to accumulate the data faster and faster and faster. But the signal to noise of these things is really low because, like I said, they're at noise levels. So if you don't integrate for a long time, your signal to noise is terrible. So you're always considering those tradeoffs.

**Adrian Tang:** That's a lot to think about. And what are the relative speeds you're talking about on the flyby? So you have like a probe that's going past the planet. You want to know what's on the surface. You're looking down through the clouds. You're trying to say what the soil is, whatever. What is the relative speeds there?

**Adrian Tang:** It really depends on the mission concept. But you could see delta Vs up to 25,000 miles an hour.

**Adrian Tang:** Oh, my. Okay. So pretty speedy.

**Adrian Tang:** Pretty speedy. So acquisitions on the order of milliseconds to microseconds.

**Adrian Tang:** Okay. Yeah. That's the kind of thing I was wondering. Yeah. And you only get one shot at that, too. So you've got to be.

**Adrian Tang:** Depends if you're orbiting or flying by.

**Adrian Tang:** Sure. Sure. I just mean that.

**Adrian Tang:** Yeah. There's other hard things, too. Like the drift is another topic. So people in Wi-Fi and stuff, they deal with packets that are on these millisecond scales, not second scales. So as long as the phase, you know, the phase of the carrier or whatever, and your carrier recovery is locked for 10 milliseconds, you get your packet out. But in a space instrument, what happens is you're trying to pick out. Let me give you a number, for example. Let's say you're studying climate science on Earth, and you're looking at hurricanes or something like the Tempest E mission. So they have a thing called NEDT, which is resolvable delta temperature, the brightness temperature of the noise that they're measuring. Your receiver is probably about 500 Kelvin of noise somewhere in that neighborhood with a mimic. And then you're trying to measure one Kelvin. So you're trying to do a one in 500 measurement. That's easy to do once. But the problem is on the next orbit an hour later, you have to match the scale with the last measurement. So if you drift more than one in 500, that means voltages, that means current, that means bias conditions, that means the overall gain, that means the phase response to the instrument, your measurement becomes no good. So half of our work is trying to keep it stable over long periods of time and calibration strategies that support that.

**Adrian Tang:** And how do you then go and verify something? Because you're talking about relative amounts, it seems like. And then how do you know what the relative pieces are? Do you have to go and point it towards space and use that as a zeroing element?

**Adrian Tang:** Or that's one trick. We know space is two Kelvin-ish, roughly, the cosmic microwave background. So we use that as a cal point. Most systems, we carry an onboard load that's heated. So it's an absorber load that we stare into with a temperature sensor and a controlled temperature. Sometimes we do a multipoint calibration. And usually we have a flip mirror or a switch. Well, at 500 gigahertz, not so much a switch, but we're working on that. The switch is back and forth. So you periodically calibrate to something known so that your measurement is interleaved with this calibration cycle. So when you plot the data a year later and you're analyzing it, you can extract the base drift out of all the calibration cycles between the data cycles.

**Adrian Tang:** Wow. This is really intense stuff. So now we're on a... This is... I'm going to say we. This is a very generous we. So we've designed an instrument here. And we're staring at a planet. We're doing a flyby. We're doing this really quick capture. We have like maybe 100 milliseconds or a second worth of capture. Per spot, yeah. Yeah. Okay, per spot. And then what is the output then? Like what is the output data?

**Adrian Tang:** So what you'll get is... Well, you take in time domain data, right? So what's coming out of your receiver is a time domain trace at the IF port. Three gigahertz of bandwidth. It pretty much just looks like white noise. From the time domain data, you can't see anything. When you take the FFT of it and average it over 100 or 200 milliseconds, you'll start to see that some frequencies, like in the frequency response, some channels will start to come up. The noise will have the structure to it. And you look at those lines and the structure. What we call a line is like a peak, a Gaussian-shaped peak somewhere. And then you can start to determine what chemicals are there and in what abundance. Like I said earlier, it's decued by the pressure. So you can sort of tell something about pressure. And in a vacuum, that tells you how much is there because that's the partial pressure of the gas. If you have a situation like Mars where there's wind, those spectroscopic lines are subject to Doppler shift. So you can start to tell something about the wind or how it's moving and map how the gas is moving over the surface of the planetary body.

**Adrian Tang:** And speaking of movement too, so do you have to account for the fact that the spacecraft is moving as well?

**Adrian Tang:** Yes, you do.

**Adrian Tang:** Yeah. How do you take that out?

**Adrian Tang:** Generally, what we do is we use the LO. So we'll program the LO in steps during a flyby. So the LO will shift from one frequency to another to make up the difference in the Doppler. To give you a typical number, right? You're like, let's say planetary exploration looking for water. You'd be probably looking at the 557 gigahertz line. So you'd be experiencing maybe a megahertz of Doppler shift at the worst case in the flyby. Your resolution in your backend processing is typically about 200 kilohertz. Although, you know, cases can be made for certain astronomy studies where they want down to 10 kilohertz or 5 kilohertz. But that's a lot of FFT channels.

**Adrian Tang:** Yeah, because you're saying just the... So you're saying the megahertz is the bandwidth or not the bits, the bucket that you're using for the FFT?

**Adrian Tang:** Yeah, the frequency resolution. But, you know, like when you fly by a planet, the spectrum doesn't slide away out of your field of view. It just takes a step to the left or right.

**Adrian Tang:** Oh, okay. That's interesting. So, and it's always weird to me that like Doppler has these, you know, I think of Doppler as just like a train going round, you know, like that. And it is, but it's consistent amongst a lot of waveform type of things, right?

**Adrian Tang:** It has some very interesting properties that are useful. Like one of the ones is in astronomy, just to throw this out there. When you look out into the universe, generally speaking, there's going to be more than one object along your line of sight. So you're not going to be able to tell this gas is in this galaxy and that gas is in that galaxy because you're getting a smush of all of it together along your line of sight. But because of Doppler, these lines move a little bit. So I know if this line is, this galaxy is rotating. So if I look at the left side of the galaxy, it's moving away from me. So I see the line to the left on the spectrum and this part of the galaxy is moving towards me. I see it on the right spectrum. So you can start to infer galactic motion from those Doppler shifts in the spectrums.

**Adrian Tang:** That is quite a neat trick. And I mean, that's some intense stuff. I mean, just in general, like you're able to look at this stuff. But again, I'd like to just... You're receiving a signal that's 4 billion years old. Right, exactly. And this is kind of hard for my brain to process all at once. And I'm guessing at this point, you've internalized a lot of this stuff. And I hope I'm playing the part of the...

**Adrian Tang:** I'm just trying to put groceries on the table. Most of it.

**Adrian Tang:** Well, you know, however you got to do it, you know. Exactly. Yeah. So just to go back one more time. So, okay, so now we're looking at a telescope. We're maybe fixed in space or something similar. Yeah. But you're able to look at the data coming from this faraway galaxy. You're looking at the left side of it. You're looking at the right side of it.

**Adrian Tang:** Yeah.

**Adrian Tang:** But it seems like that would all be optical.

**Adrian Tang:** Is that not the case? It's not the case. It's terahertz frequencies. They're like between microwave and optical. You know that 99% of the light in the universe is in the terahertz band, not the optical band. I did not know that. You'll take the noise spectrum of a galaxy. And what you'll do is you'll see over here in the really hot region where stars are forming, there's a certain set of lines. There's a chromium line. There's an HCL line. There's a this line. There's a that line. You look over here where the galaxy is cooled off. There's a different set of lines. So you can start to say how stars start to form because you say these chemical products seem to be where the forming is. These chemical products seem to be not where the forming is. Huh. And there's a lot of work at JPL about mapping the life of the whole the whole star forming life cycle. And if you're familiar with the Herschel telescope, that was one done by my group. And that was at 1.9 terahertz and a few other bands. And they actually mapped out the entire life cycle of star forming through this process of detecting different chemicals at different states of the star formation. Wow. You don't really watch the star for millions of years. Obviously, it's not that old. But what you do is you look at stars at different phases of their formation, and then you can map out the chemistry.

**Adrian Tang:** Hmm. Okay. So that's great. Herschel telescope. Let's maybe use that as a thing to dig into then. Yeah. Can you kind of walk us from the front end to the back end? Like what systems are all in there? I think you've already kind of done this already. And I realize I'm kind of repeating myself here. That's okay.

**Adrian Tang:** There's a lot. I'm going to try to make it not too bad. So first, you'll have a reflector of some kind that captures the radiation, focus it down into your feed. That's really critical. So you're talking about a surface. On Herschel, it's big. It's about a meter, I think. I'm sure that I'm embarrassing myself in front of my group right now. But yeah, it's about a meter big. And that surface has to be accurate to lambda over 20. And lambda at 2 terahertz is already micron range. If it's more than a micron out, you can't form an image, right? That the mirror will be distorted. So you focus all that down, and you go into a receiver feed. And the first thing you encounter is a mixer. And the mixer will take that noise spectrum and convert it down to a lower frequency. To do that, that mixer needs LO, which is a sine wave at that frequency that causes the mixing action. So to make that, we'll start going from the other end. You'll start at some low-frequency 30 or 50 gigahertz source oscillator. And you'll multiply that up when frequency multipliers all the way to 2 terahertz or 1 terahertz or whatever you're doing. That'll feed the mixer. So those two signals combine. And then coming out the back of the mixer is what we call the IF or intermediate frequency. That's at 3 to 4 gigahertz, 0 to 3 gigahertz flow frequencies. And that spectrum that comes out is a copy of what's going on at 2 terahertz at the input. And then we'll take that through an IF chain. It's noise, so the power levels are very low. So you have to amplify it before you can digitize it. So we have a thing called the IF chain, which is just a bunch of amplifiers and filters that brings that signal up to milliwatt power, volts, volts scale, so that you can go into A to D. Then we go into the A to D, digitize it. We probably apply a window function, Hanning window, Hemming window, Harris-Blackman window, whatever window. Usually polyphase. Polyphase filter is pretty popular at JPL. This has a lot of properties with channel leakage and stuff. Anyways, so you apply the window. Then you compute the FFT, 4,000 channels, 8,000 channels, whatever. Usually one sample is not enough to see anything because the signal to noise is slow. So that processor will take many thousands of samples and average them together and produce a noise spectrum where you can see these little things sticking out that correspond to the spectroscopic emissions in that band. And then you'll save that on a drive and eventually transmit it back to Earth.

**Adrian Tang:** That is an intense system. Okay, so now we have the noise that you're talking about. So you're saying that you can kind of average out the background noise? Is that kind of the idea?

**Adrian Tang:** Well, it's statistics. So you have a signal that's A and you have a noise that's B, let's just say. But every time you measure, A is the same because the line's always there. B is uncorrelated because it's noise and it's different each time. So as you add A and B over and over and over again from each cycle, A grows with N, but the noise B grows with root N. So eventually the A gets bigger than B and you can see it. It's just the statistics, yeah.

**Adrian Tang:** Got it, got it. And then so you had mentioned at the mixer as well, you have these different frequencies. Are you sweeping those across then to get the action across the entire spectrum?

**Adrian Tang:** It depends on mission concepts. So some systems are simple, like a fixed LO. If you remember the Rosetta orbiter, there was a Phoebe lander that landed on a comet and there was some debate if it bounced or not and all that. That was put out by ESA several years ago.

**Adrian Tang:** Yeah, I think I remember that, yeah.

**Adrian Tang:** That orbiter carried an instrument called MRO that was built by my group here at JPL, the microwave instrument for the Rosetta orbiter. That had a 180 gigahertz and 550 gigahertz channel. And they're only focused on one chemical, which was water. So those LOs, those frequencies were not tunable. They took one three gig slice from the 500 gigahertz band and 180 band and brought it down to process. It can't tune left and right. That is much simpler from an implementation point of view than one that tunes. So the advantage is you have, you're using less power. The mass is probably a lot lower, all these good things. The downside is you have less discovery space. So you can't, there's always the emissions that you expect to be there to validate your science hypothesis or whatever. But there's also along the way, you always discover things that you didn't expect to be there. And the more spectrum you can cover, the better your chances of finding something. But you have to think about a few things. If you're changing frequency all the times, it means there's times you're not observing other frequencies. So you have to plan how long you spend at each time. One of the ones we just did is I flew a mission last year that I led called Rectangle. Rectang limb sounder experiment. Our names just worked. Yeah, that was a balloon mission that flew over Texas and measured pollution and it measured water vapor as well. And one of the things is we had a 500 to 600 channel. And then we were interested in measuring nitrous oxide at 570 something gigahertz. And we were interested in measuring water at 550 gigahertz. And we got into a long debate about how long we should spend at each frequency in order to not miss anything important scientifically. And that's kind of how you set up what frequencies you're going to set at, how long you're going to set them, and what order you're going to look at them, and how frequently you're going to revisit them during a mission.

**Adrian Tang:** Hmm. Okay. And so you mentioned this mission in Texas and you were debating it. What was the ultimate deciding factor of how long you spend on different frequencies?

**Adrian Tang:** The ultimate deciding factor was we'll set up on the water line.

**Adrian Tang:** Uh-huh.

**Adrian Tang:** And we'll stay there until we're pretty sure we have water, and then we'll change it halfway through. Because the less commands you send to a space mission, the better your chances of it working out.

**Adrian Tang:** Yeah.

**Adrian Tang:** So Rectangle is a tech demo mission. It's not a full-size mission. It's a balloon craft mission. So everything is made in six months. And the software has been run twice. So who knows if the command is going to crash or not? Do you really want to send these things or do you want to leave it alone? You want to leave it alone.

**Speaker ?:** Yeah.

**Adrian Tang:** I mean, that sounds like it's odd to me to think that there would be uncertainty with big projects and a lot of stuff on the line. But maybe a balloon one has less.

**Adrian Tang:** Well, it's a one-day flight. You're building it for a year. You have a day to fly. And the crash landing is quite the crash landing. So you don't get it back.

**Adrian Tang:** Oh, okay.

**Adrian Tang:** You pretty much get five or six hours up at the edge of space to do your measurements. And then that's it. So it's super precious time. And if you send a stupid command or you put a typo and the C program crashes and it turns the radio off, you're done.

**Adrian Tang:** It sounds like that might be... Is that based on experience or... No, no.

**Adrian Tang:** It's just my mortal terror during the entire development of the project.

**Adrian Tang:** Got it. Got it. Okay. All right. See, folks, Adrian's human here. Okay.

**Adrian Tang:** That's really it. Like, you get into these things. Like, you... It's so tricky. As a designer, you're like, I want to cover every case. But every time you need to cover another case, you need to put more hardware, more software, another conditioner, another if statement. And that comes with risk to the point where it gets so complicated you can't even validate it on the ground anymore. Because what are you going to do? You sit there for a month sending commands to it one by one and checking every bit and every register? That's hopeless.

**Adrian Tang:** Yeah, that'd be rough.

**Adrian Tang:** The rule of thumb is the ideal space mission is the one that you don't have to interact with. You let go of the balloon and it sends you the data you want and you don't have to perturb it in any way.

**Adrian Tang:** Yeah.

**Adrian Tang:** But actually on that mission, we did have a failure. We had a calibration switch we're testing at the front of the 550 receiver and it either lost signal or got stuck. And it was probably the most intense 15 minutes of my life last year. It's desperately sending commands and trying to recover voltage and currents and try to make a 15 minute prediction of what's not right.

**Adrian Tang:** And what was it? Did you end up getting anything to work after that?

**Adrian Tang:** We never got it back after it failed. We don't really know what's wrong and the whole thing is smashed on the landing. So there's a lot. You know, it's smashed. So was it smashed before or is it just smashed now?

**Adrian Tang:** Right.

**Adrian Tang:** It's like forensics except, you know, with a microchip. It's not too hopeful.

**Adrian Tang:** Right.

**Adrian Tang:** So that was rectangle. There's two instruments on that. That's the 550 one I was just talking about. That was measuring pollution and water. We had a really interesting experiment, which was the 180 gigahertz one. That's the Tang part of rectangle. And what that was, was it's the first CMOS chip ever to do an atmospheric measurement. So the first silicon chip. Yeah.

**Adrian Tang:** Very cool.

**Adrian Tang:** And what we did is we actually built the receiver at 180 gigahertz in the CMOS part at 180 gigahertz directly. And the problem with that is the noise temperature, noise figure, whatever metric you want to use. The sensitivity is not great of the CMOS. So what we did is we combined it with an indium phosphide mimic, which is a much more sensitive device. So the very, I don't know if you're familiar with this, but in a radio receiver, the first stage of the receiver is what sets the noise performance. Because all the noise after that first stage is suppressed by the gain of the first stage. If the thing has 30 dB gain, there's no more, there's no more noise because everything's divided by 30 dB or a factor of a thousand after that stage. So you put one really expensive space amplifier in the front and then you use the crappy CMOS part after it, but you can still get a good measurement because that first really good amplifier keeps the sensitivity high. That was the world's smallest spectrometer. It's a little like three centimeter by five centimeter board.

**Adrian Tang:** Holy crap.

**Adrian Tang:** We got lots of, we were able to measure the water vapor profile from where we launched in New Mexico all the way across the Texas panhandle. Wow. And the whole thing's like a half a water or something, a couple of grams.

**Adrian Tang:** That's unbelievable. I mean like that, like that, and that's a true spectrometer and like. Yep. That's the whole thing.

**Adrian Tang:** Wow. The front end, the back end, the L of the mixture, the IF, the calibration, the whole thing.

**Adrian Tang:** I want to hear more about the actual hardware, but I have one last question about like the actual readings and the outputs and understanding how these things coming off of the atmosphere might actually emit signals and stuff like that. Is it such a spike in these frequencies or maybe they're so disparate from one another? Like can things overlap one another? Like is water distinct enough from nitrous oxide that you wouldn't ever get crossover?

**Adrian Tang:** I'm not a spectroscopist. I am surrounded by them though.

**Adrian Tang:** I'm sure. Yeah. I'm sure they like you though a lot if you can make stuff that tiny and make this stuff.

**Adrian Tang:** So first of all, one thing interesting is the different isotopes of the same chemical have different lines. And let me give you an exciting one. Some, some, I like to illustrate these things. Okay. So there's heavy water and regular water. And you must be familiar with the concept of heavy water. It's so it's a water where the hydrogen has an extra neutron.

**Adrian Tang:** Yep. And that's, that's from like a, they use that in nuclear plants and stuff like that. Right. They do. They do. Yes.

**Adrian Tang:** As a moderator, but it's also naturally occurring. Okay. So one of the interesting things in science is that if you go to the Indian ocean or the Pacific ocean or the Gulf of Mexico and you scoop out the water, the ratio of heavy water to regular water is the same in all those places. What that means from a science point of view is they probably have a common origin. Because if you take a sample of water where it has a certain mixture of heavy and regular, that sample you take should also have the same ratio. That's called central limit theorem for mathematics.

**Adrian Tang:** Okay.

**Adrian Tang:** So they did these D to H measurements all over the solar system on comets, on planets, and everywhere you go, pretty much the ratio is comparable. So that, that tells us that the water in the solar system is probably from a common origin. That was done with micro-espetroscopy. And interestingly enough, that's how our model of the origin of the solar system was formed is that we have those common water sources and comets and this and it went everywhere. So then Moreau, the one I mentioned earlier, it actually did a measurement on comet 67P, which is a Jovian family comet out of Jupiter. And that had a different ratio. So that has kind of unsettled the discussion now. We were pretty settled and the Nobel Prize was getting ready to go out. And now, now we're not, not so, not so sure anymore.

**Adrian Tang:** Right. Right. Don't, don't put a stamp on it, you know?

**Adrian Tang:** What, what it means is that we need to do more measurements to understand this.

**Adrian Tang:** Does that mean that maybe the heavy water develops when it's like in system or something like that, instead of like crashing down from?

**Adrian Tang:** Not likely. There's not a lot of natural processes that are not origin time skills that are going to make a huge abundance of heavy water.

**Adrian Tang:** Okay.

**Adrian Tang:** It does mean we need better measurements or more measurements in more places, but you're not going to send a flagship Cassini mission to every object in the solar system. So we need cheap, compact and dirty instruments that can do the measurement. And that's a lot of why we're using CMOS.

**Adrian Tang:** Okay. That's a great lead in. So maybe you can explain now, you, you kind of, you'd started to talk about it with, I think you said Indian phosphide or whatever the front, that super crazy front end is. But like traditionally, what do, what do these measurement circuits look like? Are they all made out of that or how, how has it changed as moving into CMOS?

**Adrian Tang:** It's really, there's so many things. So let's just go through it. There's okay. At the highest level, there's what we call active receivers and passive receivers. And an active receiver is something with an amplifier in the front. The only people that have amplifiers at these frequencies are our friends down in Redondo Beach. And they develop these really, really nice 300, 400, 500, 600 gigahertz amplifiers. The problem is it's not a commercial process. They, they, they almost do it as a favor for us. I mean, we pay them, but it's a favor for us.

**Adrian Tang:** You said friends, but is this some secret agency? I don't actually know.

**Adrian Tang:** No, no, it's a, it's a Northrop Grumman. Oh, okay. Okay.

**Adrian Tang:** Northrop Grumman Aerospace Systems.

**Adrian Tang:** Okay. Yeah. Yeah.

**Adrian Tang:** So Tony, Tony Long used to, I think he still works there.

**Adrian Tang:** The guys that do this stuff are, well, Vesna is one of their best designers. Shout out to her. Bill Deals down there and Rich Lai and those guys, they make these beautiful amplifiers. They actually had a DARPA program and it all started for defense purposes, but we're the only ones that could actually use them. Because we are the only ones that build systems at these silly frequencies. Not by choice. Again, the chemicals are there. So we have to go up there. So sure enough, that's one way to do it is put an amplifier in front. And what the amplifier does is it's fairly low noise and it suppresses the noise of things behind it. The exciting part about amplifiers is they work pretty well at room temperature. They work even better cooled, but they work well at room temperature. Then the other technique is to use a passive receiver, which is just a mixer first. Mixers don't suppress the noise behind them. They add to it. So generally speaking, a mixer is less sensitive than an amplifier at the same temperature. Generally speaking, there's some exceptions. So on the mixer side, there's a shocky mixer. Shocky mixtures are gallium arsenide shocky. They're just two diodes in a metal box, basically.

**Adrian Tang:** Are you saying shocky or shockly? Shocky.

**Adrian Tang:** A C-H-O-T-T-K-Y.

**Adrian Tang:** Okay.

**Adrian Tang:** Yeah. And they're a metal semiconductor junction. So they're typically very fast because they don't have a recovery time. Okay. And what that lets you do is it lets you do a conversion, but they're not super... Let me put numbers on this. A typical mimic is... Mimic amplifier is 500 Kelvin, 700 Kelvin, 1,000 Kelvin, somewhere in that neighborhood. A shocky mixer can be 700 to 1,500 Kelvin at room temperature. If you cryogenically cool it, you can maybe get 200, 300 Kelvin. So you're saying Kelvin, and I don't quite understand how that... Kelvin is at noise temperatures. So you know that noise is KT, right? The thermal noise of the universe is KT. And we express sensitivity in the level of KT difference that we can detect.

**Adrian Tang:** Got it. Okay. Okay. So that's why it's in Kelvin, because like you said, the background is 2K and...

**Adrian Tang:** It's not a physical temperature, right? It's just the noise caused by something at that temperature will be the same. So if you heat something to 500 Kelvin, it'll make noise as a mimic that has a 500 Kelvin noise temperature. Then you get into the fancy detectors. So my group has a guy named Boris. He's amazing. He does HBT mixers, HEB, so hot electron volumetric mixers. Those are much lower. They're 100 Kelvin, 50 Kelvin crazy, but they're cryogenic. They need liquid helium. They need a laser to pump them. That's a long story. So that is very good for astronomy. So astronomy is like, it has to be as sensitive as possible, because the thing is 4 billion light years away, right? Right. Planetary is like, we need to keep the power and mass and everything low because we don't have a lot of solar power at Saturn. The rocket's not so big. Stories like that. Earth science is like anything goes.

**Adrian Tang:** We're the bad boys of science. You know, we get as much weight as we want to.

**Adrian Tang:** Well, no. You look at something like the space station, right? It's got gigawatts of power with those giant solar panels. There's always access to Earth ore, but it's not expensive. So you can keep putting stuff and putting stuff. You're not constrained the same way you are on the mission to Saturn, where you have, it's nighttime all the time, and your payload's five pounds, right?

**Adrian Tang:** Yeah.

**Adrian Tang:** Yeah.

**Adrian Tang:** Okay. You mentioned hot electron volumetric? Is that what you said? Volumeters, yeah. Hot electron volumeters. Oh, okay. Okay. And so what are the materials that are in these, though? Are these really rare materials?

**Adrian Tang:** Yeah, they're exotic semiconductor junctions. I'm not the guy to ask that. But basically, they're a nonlinear device, and you pump them at these frequencies, and you pump them with another tone that's nearby, and then they intermodulate, and the intermodulation is a low frequency, and you collect that low frequency off them, which is basically how all mixers work.

**Adrian Tang:** Yeah, I feel like the relative measures here are so far scant from what I'm used to, because you're like, oh, it's nearby, and you're like, oh, it's only like 100 gigahertz. But what is the nearby in this case? So you have this exotic semiconductor junction. You're pumping it with blank to get blank.

**Adrian Tang:** So you're chasing a 2 terahertz line, and you would pump it with 1.997 terahertz on the laser or on the LO to get 3 gigahertz difference, which is what you're collecting at the output.

**Adrian Tang:** And how would you generate the 1.99 terahertz?

**Adrian Tang:** So you have a few choices. There's quantum cascade lasers, which are one technique, which is a solid state laser technique. Those tend to work better at the higher frequencies, because they're more like an optical technique. Or what we'll do is we'll use a synthesizer, like the ones I provide in CMOS to the group, and then we'll multiply those up. So we'll have a frequency doubler and frequency tripler and frequency doubler. And that's a long topic, too, because those doublers and triplers, they're good. They're the best in the world, but they're still only 20% efficient. So the more multiplying you do, the more destroyed you are. After you get past 600 gigahertz, even Northrop Grumman can't help you. There's no amplifiers above there. So if you need a lot of power to pump a mixer, you're in trouble.

**Adrian Tang:** Huh. Yeah, yeah. So you just have to brute force it by just giving it more and more.

**Adrian Tang:** Well, you can't. The devices saturate pretty quickly. So there's like two angles, right? One is we have huge efforts here to try and get more and more power at these frequencies so we can drive things. And one is we try to make the mixture need less and less power so the requirements are more reasonable. And together, you hopefully get something good.

**Adrian Tang:** Here at the Amp Hour, we focus on learning. We also choose advertisers that have a similar mindset, like Roger Schwartz. They have a new product meant for education. The 2000 Series Oscilloscope is a new entry into the market that bundles features together that normally would be charged per add-on. This means that engineers, or people that are working towards becoming an engineer, get a much higher value for the money they spend. And Roden Schwartz doesn't skimp on features. Friend of the show and YouTuber, Shariar from The Signal Path, said this about the RTB 2004.

**Chris Gammell:** So here I have the output of the generator from the Roden Schwartz directly connected to the input of my EXA signal analyzer. And this would allow us to measure the THD performance of the instrument. Now I have set also the Roden Schwartz to 25 MHz, which is the highest sinusoid signal it supports. And the amplitude is 500 mV peak-to-peak into 50 ohms. Now we can go ahead and increase the amplitude one step at a time and see how the THD behavior changes. So right now with half a volt peak-to-peak, the THD is 0.5%, which is minus 46 dBc, which is very, very good. For smaller signals, the THD is absolutely excellent. So I have no doubt that this would be a useful generator, particularly because we do have the ability of creating arbitrary functions. And for little experiments, projects here and there, this would be very useful.

**Adrian Tang:** Shariar is well known for his interesting experiments, and we always recommend people subscribe to his channel. In this particular video, he demonstrates how the protocol analyzer works on the scope and showcases the problematic serial bus on an Arduino, which he troubleshoots live on screen. Of interest to me on this scope is the web interface that completely replicates the front panel for remote troubleshooting. Check out Shariar's video for a more in-depth review of the device. And if you want to see other reviews and opinions from fellow engineers, check out askanengineer.us. You can see all the devices that are good value for your bench, which includes other oscilloscopes, signal generators, RF equipment, and more. That's askanengineer.us to find out more about your next piece of test gear. And now, back to the show. Okay, so now we're in the CMOS realm, sort of. I'm still, I'm still, I mean, Adrian, I'm going to be honest. I'm so confused about all this stuff, but it is so fascinating to me that, like, this is out there. I mean, this is, like, so much further in the realm of, like, bleeding edge than we're usually talking about in the Amp Hour. I'm going to be honest.

**Adrian Tang:** Well, I mean, most of the terahertz work here was done in the 70s and 80s. And the technology has improved a lot, but the block diagram on the wall is pretty much the same.

**Adrian Tang:** So what has actually improved then? Is it process technologies approved or simulation?

**Adrian Tang:** A lot of things. We've done a lot of work on the way we design the blocks to optimize them. We've learned how to power combine efficiently. We just had a work by one of our guys, Jose, who did this really nice diplex here to do two frequencies at once. But generally speaking, to work at these frequencies, the circuits have to be simple. One diode, two diode, four diode, eight diode, stop.

**Adrian Tang:** Uh-huh. Uh-huh. So, yeah, that does kind of lead us towards, like, what does that actually look like then? So now you're designing the CMOS. And, like, how is it just that front end then? Or then are you integrating it with the more traditional?

**Adrian Tang:** I don't do the front end. They do the front end with all the fancy technology. I provide the LO. So there's a little board in the back that pumps out a lousy 100 gigahertz that they then multiply up to where they are.

**Adrian Tang:** Okay.

**Adrian Tang:** Or I build the back end processor so it has an ADC with an SMA port on it. So there's an SMA port on their two-terahertz mixer, and then there's just an SMA cable going to the little board, and I process what's coming up.

**Adrian Tang:** Wow. Okay. And that still sounds like, I mean, can you give us a relative measure then? Because this is, again, way past anything I've ever even dreamed of using. But, like, the LO that you're creating and the ADCs that you're creating, where do those scale in terms of, like, they have to be custom, I'm guessing, for certain reasons. So why are they custom versus off-the-shelf? Can you give us a relative measure versus what someone might be able to buy off a DigiKey or something similar?

**Adrian Tang:** So DigiKey, you know, I don't know. You can buy synth—there's some nice stuff out there. There's a company called Winfreak that makes nice USB synthesizers up to 4 gig. We use them somewhere. Pasternik has some nice 8 and 12 gigahertz USB synthesizers, but the group needs 100 gig USB synthesizers, so then we have to make our own chip. So it's complicated. We'll build a chip. We'll have a digital core with a fractional sigma-delta generator, you know, MASH-111 or whatever noise-shaping techniques to get the fractional component for the synthesizer. We'll have a charge pump. We'll have a phase detector. We'll have a lock loop. We'll have a VCO on there, probably LC. We'll have some type of driver, and we'll have some kind of transformer-coupled power amplifier to bring the power up before we come outside. We'll have power sensors and temperature sensors and all this stuff. We have a radiation sensor. One of the things I haven't talked about yet is all these things through space need to deal with radiation.

**Adrian Tang:** Yeah, right.

**Adrian Tang:** CMOS is not rad hard. It's not super soft, but it's not rad hard. You need to, especially if you're going around the planet and trying to do a 1 in 500 measurement five times in a row or something, you need to worry about radiation. So we have a lot of sensors that we put inside the SOCs to monitor bias conditions, voltage conditions, current conditions, and say, hey, the radiation has changed something. We need to calibrate. So then there's hundreds and hundreds of knobs that turn, adjust clock phases, adjust bias conditions, change the clock tuning, whatever, adjust VCO tuning or trimming, change tuning on the output stage, whatever, change the output match, whatever. We need to do to bring it back to health. The other thing is we deal with extreme temperatures. Sometimes the chip gets very cold or very hot, and we need to calibrate for that. So that would be a typical synthesizer. It would be a very complex system. There'd be an integrated subprocessor just doing calibration along with the RF circuits with RF sensors everywhere. And the moment something goes out of corridor, we activate that subprocessor. It goes through a calibration routine, brings everything back and lines it all up again for next time.

**Adrian Tang:** That's great. I mean, yeah, I mean, that is, and it sounds like the amount of complexity and the amount of specificity is, of course, you're making a custom circuit, right? You kind of have to because who else would be making this? Yes, exactly.

**Adrian Tang:** Nobody else would be making this. It's too silly. Right. Yeah. The other thing is packaging them is not simple. So when you go to 100 megahertz, you can put a PCB trace or a BNC connector. When you go to 5 gigahertz, you can put an SMA connector. When you go to 100 gigahertz, you need a waveguide. Nothing but a waveguide makes sense. So we spend a lot of time on how to package the chip, how to do these transitions and have very inter... You know, the whole world is waveguided at W-band and higher. W-band being 100 gigahertz. So you have to couple the chips to those. So we do spend a lot of time designing coupling structures, transitions, probes, that type of stuff.

**Adrian Tang:** Yeah. Yeah. Tell us a little bit about the team because you keep saying we. How big is your team and what does it look like starting from a whiteboard with some block diagrams to a thing on a spacecraft?

**Adrian Tang:** I am one of the most privileged people in the world to work in the group I work with. We have some of the greatest talent I've ever seen in my life here. We have a couple of people who are more system people. Gowdem and Ken Cooper. Gowdem, I can't pronounce his last name. He's, they like are instrument system people. They come up with measurement concepts and end-to-end block diagrams. We have guys like Jose Siles who are like some of the best mixer and multiplier designers on the world. These guys design two terrier blocks in an hour. It's incredible.

**Adrian Tang:** Wow.

**Adrian Tang:** We also do a lot of the fab in house. We have a guy, Joseph Lee. He does most of the diode fabrication. We have a packaging person, Cecile. She's amazing. She knows how to do all this really high frequency packaging, fancy silicon work. And as we go around the group, let me see, there's me who builds the chips. I have students in postdocs. They're not cool enough to get named here yet. You got to earn it, kids. When they graduate, I'll be nicer. No, I'm joking. And then we have some help with mechanical support from other groups at JPL. And JPL is very, it's all about projects. So when you have a project, you find the right people for the project. You're not rigidly stuck in your own group.

**Adrian Tang:** Yeah. It's flexible, you know, reconfigurable labor kind of thing.

**Adrian Tang:** We will find a mechanical person if we need that from somewhere else. There's a great antenna group here in Nasser Shereh and Emmanuel Cross are helping me with antennas. They're really good. Everyone's really good here. And I just try to put a chip when a chip is needed. I don't want to build a chip if a chip is not. If you can buy it off to Jiki, go buy it off to Jiki.

**Adrian Tang:** Yeah.

**Adrian Tang:** These things cost millions of dollars. I'm only interested in doing it if there's a demand to do it and if it's interesting.

**Adrian Tang:** Right. Yeah. Because I'm guessing, well, what is the timeline to actually get a chip out the door then too?

**Adrian Tang:** So some of these synthesizers, to be fair, I've done in one day of design work, which is intense.

**Adrian Tang:** Wow. Okay. But that's the design piece, not the...

**Adrian Tang:** Fabrication's quick. About two months, you know, typically.

**Adrian Tang:** Oh, that is fast. Wow.

**Adrian Tang:** Yeah. But, you know, then you got to do a board. That's a couple of weeks. And then you have to assemble it, wire bond it, put the probe, test it, write firmware for it. Like the software is almost as much work as the chip design.

**Adrian Tang:** Totally. Yeah.

**Adrian Tang:** To write all the firmware that runs on it. So end to end, maybe five months for a chip project.

**Adrian Tang:** Okay. Yeah. I mean, that's still very fast in my mind, but like less than the 25 years that I imagine it would take me to even think about it. So.

**Adrian Tang:** But I mean, at the same time, most of these space missions are on an eight year kind of a timeframe.

**Adrian Tang:** Sure. Sure. And how do they approach you about that? So is it, there's like someone in that spectroscopy group that you mentioned or a mission manager?

**Adrian Tang:** I do a lot of system work too. I'm not just a chip designer. Yeah. So like I got approached a couple of years ago about measuring snow here in the Sierras in California. And snow is a tough one because all our California water comes from snow or 60% of it anyways. And one of the biggest problems is how to figure out how much water is in snow. And it's not as simple as taking a stick and sticking the stick in the snow and measuring the height. So the density matters, the size of the snowflakes matters, and the amount of liquid water pulled at the bottom matters. So we have a project we've been working on, on and off, and we just started a big version of it from a UAV. And we're building an instrument to measure snow and extract the water content, what they call SWEs, snow water equivalent. So we have a whole bunch of neat tricks. One of the tricks is we use a wideband radar, but we're not just measuring the depth of the snow with the radar. What we're doing is we're looking at the scattering properties. So when the wavelength is very, very comparable to the particles, the snowflakes, you get what's called B scattering. Because your wave is bouncing around the side. When the wavelength is much, much longer than the particles, you get what's called rayless scattering, where it just kind of bounces off the bulk. And as you sweep frequency, that absorption curve takes an inflection. And from that inflection point, the instrument can tell, well, how big are the snowflakes? Once you know how big the snowflakes are, you know how big the space between them is. You have the depth directly from the radar. And then we do a radiometer trick at two frequencies. We measure the brightness, temperature, and the ground. And we can sort of tell how much water is pulled on it. We put all those things together, and we tell California how much water they're getting this year. And that's, yeah. So we will go from, like, a study of the properties of snow at microwave frequencies. And we will actually do a lot of simulations and scattering and radiative transfer stuff. And then we'll design an instrument concept, a block diagram, what we're going to measure, what the waveforms need to look like. We'll break it out into a block diagram. We'll design the requirements on each block. We'll discuss how we're going to synthesize the waveforms, how we're going to up-convert and down-convert, what type of DSP we need, what type of dynamic range we need to support these. Snow is a tough one. Snow is almost like air. So the dielectric constant is almost the same. So the reflectivity is very low. So your dynamic range requirements are huge. One of the problems we always have is we're transmitting a wad of power or something on the radar. And all of that is going to leak into the receiver that's literally bolted right next to it. So how do we manage that? So then we do the vacuum cancellation schemes, how much dynamic range we have left. Can we see those signals? What kind of ADC we need? What kind of sample rate we need? The waveform and the bandwidth that's going to get us the resolution we need to interrogate the snow. We need to sweep over a wideband to see those regimes. We need to know about our noise sensitivity and if we're transmitting enough power. And we need to worry about distortion. And we'll just go through it end to end.

**Adrian Tang:** Yeah.

**Adrian Tang:** That's a couple of things.

**Speaker ?:** Yeah. Yeah.

**Adrian Tang:** And so in that case, was that like you wanted to measure the snow or someone had come to you and said?

**Adrian Tang:** Yeah. We were approached by two scientists, H.P. Marshall at Boise Usted, who's the PI of this new one, and Tom Painter, who's at UCLA. They're both snow scientists. They're hydrology experts. They came to us asking us how we could do this measurement. And we come back with the concept.

**Adrian Tang:** That's a fun challenge. I mean, that sounds like a ton of different measurement techniques that you have to kind of bolt together.

**Adrian Tang:** Applications are zero, just measuring snow. This is not the type of radar you would use in a self-driving car or something. Self-driving car is easy. It's a giant metal block right in front of you. It's very easy to see. Snow is basically transparent.

**Adrian Tang:** Do you mean packed snow as well? I mean, that's the ultimate.

**Adrian Tang:** I'm talking about the snow that's sitting up on the mountains right now.

**Adrian Tang:** On the mountains. Okay, yeah, yeah. Okay. So you're remotely.

**Adrian Tang:** Yeah, the long-term dream is to do it from space, but I see a lot of issues there. Got it.

**Adrian Tang:** Yeah. Yeah, I imagine there's interference from the actual atmosphere and similar types of things.

**Adrian Tang:** Well, no, it's a geometry issue. So let me help you here. Okay, so the snow's on the ground. You want to measure the depth of the snow. But you want to measure it with a footprint that makes sense. So this is like the resolution is the Z direction, how thick the snow is, right? Or the scattering. But you also need to think about XY, which is the footprint that you're measuring at. How much of a footprint are you looking at a time? So like I said, diffraction, right? You have to measure with very low frequencies. This one is only 10 to 15 gigahertz because you need to penetrate snow. If you go to 500 gigahertz, you can't penetrate snow because mostly water will absorb it all. So you're forced to a low frequency to get through the snow. But a low frequency needs a big antenna to have a small footprint. So then what do you do? Do you put a giant 600 meter antenna in space? That makes no sense. So then you have to start making concessions everywhere. We're doing it from a UAV right now, which is, you know, hundreds of meters above the snowpack. So we have a reasonable footprint. If you look at the state of California and you try to assign it a depth to 10 centimeters, does that even make sense? What do you mean the depth? I mean, so if your spot on the ground is the state of California and I have a Z-axis resolution of 10 centimeters, it's going to tell me the average depth of the state, which is not super useful. Right, exactly. And most of the state is not covered in snow. Exactly. So what you need to do is you need to constrain that beam so that it's useful. The problem is it's easy to do that from an airplane that's not flying very high or a UAV. It's very difficult to do that from space because it's hundreds of kilometers. Right.

**Adrian Tang:** Does that mean you'd have to do lots and lots of passes, though, in order to map? Or can you kind of just assume that there's universal coverage over certain areas?

**Adrian Tang:** We can cheat a little bit. It's called forward modeling. You look at the weather forecast and you take certain strategic positions and you can infer what's going on in all the other spots.

**Adrian Tang:** Okay. Yeah.

**Adrian Tang:** And the weather's never wrong, so that helps. But certainly, like, the 3D terrain, there's a lot of techniques to deal with that.

**Adrian Tang:** Yeah. Yeah. Yeah. Yeah, like stretching it out and mapping it back to a flat plane or something.

**Adrian Tang:** The problem is if you're in space, you know, so think of it like an ice cream cone. So your beam looks like an ice cream cone. So if you bite away most of the ice cream cone and only leave the tip that you're holding, you'll have a small circle when you put it on the table.

**Adrian Tang:** Yep.

**Adrian Tang:** Right? But if you use the whole cone, you'll have a big circle when you put it on the table. And unfortunately, from space with a practical antenna, that circle is almost half the state.

**Adrian Tang:** Got it. Yeah. Yeah. Yeah.

**Speaker ?:** Yeah.

**Adrian Tang:** Yeah. Yeah. Let's go back a little bit to the CMOS. Sure. So what does that look like when you're sitting down to do this actual design? Like, what do your tools look like? And then what does the output look like? You said you have fabrication on site.

**Adrian Tang:** Usually it starts with a two liter Coke to keep you awake. So you go through a flow, right? In CMOS, it's a tradition. It's just like what you do in the company when you're building a Wi-Fi chip. So you start with a schematic design. And you use, you know, nice tools like Spectre RF or maybe Keysight stuff if you're less affordable. And you go along. You get the schematics in work debt. You get your distortion and your power level and your gain and everything that you want. Then you start drawing it. You start laying it out. On the ADC side, kind of the same. On the digital side, you're writing Verilog code. And you're going through placelet, synthesis, all that. Optimization, timing flow, power flow, cross-clock stuff, domain, IO, all the usual. And you get a chip. You wrap it together. You spend some time integrating it. You get through verification, caliber, venture graphics stuff, whatever. Check the DRC. Check the LVS. Check the timing, usual stuff. Make sure the power supply is okay. Look for signal integrity. Ansys has nice tools. Pathfinder, check the ESD. Totem and Redhawk, check the thermal. Once you sign it all off, you send it out for fab. The CMOS we don't do at JPL. The CMOS we use TSMC.

**Adrian Tang:** Okay. Yeah. That makes sense. Yeah. So you have like the packages that you can download and use their standard process.

**Adrian Tang:** Yeah. We use their process, but we usually make our own cells for everything. We don't trust anything here.

**Adrian Tang:** Okay. That's interesting. Why is that? Just because of past bad stuff?

**Adrian Tang:** No. When they're making their IP, they're not thinking about radiation. They're minus 100 Kelvin. Eh. Minus 100 Celsius. Sorry. Minus 100 Kelvin is stupid. Yeah. Right.

**Adrian Tang:** There's no minus in the Kelvin range. Yeah.

**Adrian Tang:** So, I mean, you know, one of the jokes is by the time you simulate their stuff, you could design your own. Okay.

**Adrian Tang:** Does each cell need to be like tested and verified? Or how do you know that your stuff's going to work better then?

**Adrian Tang:** Because cadence design systems is awesome. And once you simulate it, you have confidence. Really?

**Adrian Tang:** Okay.

**Adrian Tang:** Like, I don't know how much you know about modern ICs, but like the Foundry provides you models that cover three sigma conditions and temperature, all the different things that can go wrong with the process, all the corner models, Monte Carlo models, whatever. You clean it all up and you get it right. Nothing will go wrong. If it went wrong, Qualcomm would be out of business by now.

**Adrian Tang:** Just because they don't have time to also do that kind of...

**Adrian Tang:** No, they don't have time to re-spin those giant chips. And they're so complicated. If the tools weren't good, they'd be dead. So thank God that, you know, cadence is around and supports the industry and we leverage that ability for our small stuff.

**Adrian Tang:** Yeah, that's great. That's good to be able to do that. Okay. So what is then the turnaround time of like you push it out to a TSMC? I guess I don't really have an idea for budgets either. Like I think of like pushing something to a wafer fab has to be pretty... Time and dollar expensive or intensive rather.

**Adrian Tang:** It's complicated. It depends a lot on the process. If you're using a 90 nanometer, it's not that expensive. I mean, in the context of a JPL project, what's expensive, right?

**Adrian Tang:** Yeah. And that's what I'm really trying to get at. I don't have any idea for... I mean, you talked about the millions of dollars of test gear, but I don't have any idea of what a project would look like.

**Adrian Tang:** Tapeouts that we do here, we call it tapeout when we fabricate something. You know, millions of dollars. They're millions of dollars for some of these parts because they're just so big, so complicated, have so much design time and have so much IP in them. But in the context of the $2 billion Mars 2020 rover, a million dollars is not a lot of money.

**Speaker ?:** Right. Yeah.

**Adrian Tang:** But if you mess up, you can do a lot of damage. So you have to... Right, right. Yeah. So you have to make sure it's right, which is why we probably spend three times longer through verifying things than we do designing them.

**Adrian Tang:** Yeah. That's good engineering.

**Adrian Tang:** Yeah. By verification, I mean SIM, right? SIMs and test benches. Sure, sure. Not... Yeah. Not measurements.

**Adrian Tang:** So because you're not going to have tons of chips to test on the bench, or what do you mean by that?

**Adrian Tang:** It's a chip. It has 50,000 blocks or something inside. You can't get at all the intermediate signals. If it goes south, you're not going to learn much from the physical part.

**Adrian Tang:** Right. Unless you have very, very tiny probes. Yeah, you can't do that. It's just, you know,

**Adrian Tang:** the chip's under glass, right?

**Adrian Tang:** I know. I was just kidding.

**Adrian Tang:** Yeah, yeah. When things go south, the tools that you use to figure it out are the same tools you use to design it. The only thing you can really do, practically speaking, right, is you mess up your design to produce what you're seeing on the bench. Mm-hmm. And then infer that you must have the problem isolated correctly and identified correctly.

**Adrian Tang:** Yep. What does it look like when you are, like you said, you're doing most of your verification and testing in the digital tools, in the simulation domain, stuff like that. But then when it does come in-house and your packaging person kind of puts it on a board and stuff like that, how are you verifying these things?

**Adrian Tang:** A lot of times we're doing BIST. So we build in a BIST, built-in self-test.

**Adrian Tang:** Okay. And what does that look like?

**Adrian Tang:** It's the firmware. You load firmware on it, you click run in, and it checks everything, and it gives you a yes or a no. And that's pretty much it.

**Adrian Tang:** Is that because you said you have measurements on board that are like for temperature and for everything else on there? Exactly. Yes.

**Adrian Tang:** Yeah, there's lots of sensors, and you already know where all the parameters should be. Got it. And if they're not, you've already failed. Right. Yeah. Exactly. Yeah. So, I mean, like that's the thing. You spend months and months designing these things, and it's frustrating at times. You design and design, and then you're waiting for the chip to come back. And then, you know, you need to make the board, and then everybody's sick with coronavirus, so the board doesn't come right away. And then you have to like do assembly, but you're number 500 in the queue, and then the wire bonding guy runs out of wire, so there's another week there, and then someone's on vacation, another week there, and you wait, and you wait, and you wait, and then you finally get it in your hand, and you turn it on, and in 30 seconds, it's yes or no.

**Adrian Tang:** Wow. And the latest one was yes, I hope? How often is it yes versus no? I mean, like...

**Adrian Tang:** We did about 60 chips last year. We had about 55 on the first pass. That's pretty good. Maybe four with a spec problem, and one with an actual functional problem.

**Adrian Tang:** So you guys did 60 chips last year with a team that sounded like it was 30 to 40 people? The chip team? The chip team is three people.

**Adrian Tang:** The chip team is three people? The chip team is three people.

**Adrian Tang:** Holy crap. That's a lot of chips in one year.

**Adrian Tang:** That's a lot of... Yeah. People don't believe it, but anybody who's worked with me knows it's true.

**Adrian Tang:** I mean, you had mentioned the one-day turnaround thing. I mean, I know that cells are a thing in chip design, but are you building up larger models that you're able to drop in?

**Adrian Tang:** When I was a wireless guy, 802.11 was 802.11. So a lot of it is like, we're going to use the thing from the last chip for the next product because it's the same thing, and we're just going to push the performance a bit or push the power down a bit. But here, every project is so crazy and so different that the reuse is almost zero.

**Adrian Tang:** Really? Okay. It's almost zero. Wow. So, I mean, you mentioned writing C and stuff like that. I mean, are there standard microcontroller blocks or are those external to the chips that you...

**Adrian Tang:** Well, we always do a partitioning exercise, right? So the discussion is always like, what needs to go on the chip? If you're doing 10 gigahertz ADC, yeah, that needs to go on the chip because there's no way to not do it on the chip. But then it's like all the auxiliary blocks. If we need a filter, okay, we need an RC filter for whatever, for a loop filter, for something. Well, if we put it in the chip and we messed up the calculation, we're dead. Can we put it off the chip? Is it okay to put it off the chip or is there going to be a problem? If we can put it off the chip and we think we might want to change it, we'll put it off the chip. If we think there's like firmware that we're not too sure exactly how this is all going to work, then we'll put the microcontroller on the board next door and run a bus. But if we've done it a thousand times and we know it's going to work and we don't want to add the complexity of another microcontroller or another supply voltage, another headache, then we'll just put it in the chip.

**Adrian Tang:** Is it simpler when you are outside or does that add some... No,

**Adrian Tang:** it makes the board a nightmare, number one. Okay. It makes the assembly more complicated. And, you know, things don't go wrong in a chip. Things go wrong in assembly. The solder doesn't flow right. Something doesn't touch. Something's wrong. So by putting everything in the chip, you're making it absolutely, absolutely the best possibility of it working without assembly problems or mechanical problems or parts problems. But it's also inflexible. There's no... If you're screwed, there's no knob to turn to get out of it. You're just plain old screwed. When you're on the board, I can move this trace. I can cut that wire. I can do something. When you're in the chip, you're just all or nothing.

**Adrian Tang:** Right. And what would be the... What's the percentage of the 60 chips that you said from last year? How many are like the super, super integrated ones that you mentioned? More than half. Yeah. Okay. And in that case then, so you'd mentioned, you know, everything's on the chip, but you still have to get at it to program it or interact with it or whatever. Well,

**Adrian Tang:** it'll have a USART SPI or USB bus that you access everything through. And then some little microcontroller or some other, you know, digital sequencing core inside that can handle instructions and do things. Got it. Okay. Okay.

**Adrian Tang:** That's really interesting. I mean, like we've talked to some chip designers on the show before, but not this kind of variety of things. I mean, there's really a lot that you say that is going in here. The block diagram sounds like it's, some of them are very intense.

**Adrian Tang:** We try to make them as simple as they need to be, but it never ends up that way. It's always like that. It's like, so you, you want an ADC, but it's an ADC for space. So then you need a radiation sensor and then you're worried about the clock jitter. So then you need to have an option to have a bypass PLL. Okay. So that's good. And now you're worried about the, you know, you're worried about clock swing because maybe the radiation is going to kill your driver or push the bias up and you're going to hit common mode. It's going to drive into the rail or something. You're going to be told. So then you need clock tuning and then you need a way to change the bias. So then you need a R2R DAC or something to set the bias. Once you have R2R DAC, then you need a controller for that. Then you got to run a bus for that. Then what's the point of setting and if you can't see it? So then you need to tap to monitor. So then you need another ADC to check that ADC's bias condition. And then you do that. And then you need to worry about like, well, the clock phase might be wrong. And if the radiation comes, the clock phase might change. So then you need a clock tuner, but then you need a way to measure the phase. So then you need a phase detector. So then you need something to look and it gets bigger and bigger and bigger and bigger until it's just gigantic project.

**Adrian Tang:** It's chip turtles all the way down, huh? Yes, exactly. Exactly. Oh, wow. Wow. And then so you're saying, I mean, you're adding all of these elements that you are using to measure and monitor and stuff like that. Yeah. But each of those is also custom each time as well?

**Adrian Tang:** Sometimes we reuse them, but often it's a different frequency, a different voltage, or even worse, a different process.

**Adrian Tang:** Uh-huh. And a different process, like a different silicon process

**Adrian Tang:** that you mean? Yeah, like going from a 65 nanometer to a 28 nanometer. Oh, wow.

**Adrian Tang:** Okay.

**Adrian Tang:** So like here's an example. We had a really good receiver in 65 nanometer. And when we did the receiver for rectangle, sorry, so the 65 nanometer receiver was at 100 gigahertz, which is fast, but not that fast. And we had, and then when we did rectangle, we want to do a 180 gigahertz receiver because the water line is at 180 gigahertz. We don't have a choice. But 65 nanometer doesn't go fast enough to get to 180 gigahertz. So think about this. We had every single block we need to build this receiver in 65 nanometer except the one amplifier at 180 gigahertz. So we had to recreate all of that to support that frequency and move it into the other process and then build one more amplifier. Oh, yeah. That's frustrating. The thing is, the process behavior is different. The supply voltage is different. So it's not just copy and paste and it's not even usually the same schematic. Yeah. You know, like op amps. Op amps are a huge one, right? So if you're in a 90 nanometer process and you have a 3.3 volt IO, you know what a telescopic op amp is? It's where you stack casket stages on top of your input pair to get more gain.

**Adrian Tang:** Okay.

**Adrian Tang:** You can do that. When you go to 28 nanometer, the VDD comes down and bonks you on the head. You have no swing left. So then you can't do that. You have to go to a folded cascode or a low voltage cascode or a two-stage op amp or some other topology completely because the process environment is so different. To get the same gain and bandwidth product, get the same slew rate and get the same drive strength, you have to build something completely different.

**Adrian Tang:** So it's a redo it. Yeah. It's a redo it like you're saying. So like- It's not even just like reuse. It's like rethink. Yeah. Re-architecting. Yeah. Yeah. Rethink. Wow. Do these things live in your brain? I mean, I don't have any personal chip experience, anything like that. So, you know, you're mentioning all these things. Obviously, you've seen them all before. You've built them before. But where did you learn some of this stuff too?

**Adrian Tang:** I've been doing this forever.

**Adrian Tang:** I'm sure, sure. But it had to start sometime, Adrian. So I'm just saying.

**Adrian Tang:** I mean, the first thing is you got to have good circuit fundamentals. And I don't mean IC. I just mean good circuit fundamentals. Sure.

**Adrian Tang:** How electricity works. Yeah. Right.

**Adrian Tang:** You have to look at circuits and you have to know roughly where the poles and zeros are without having to sit down and do SCGS plus GM over CGS. You can't be having to calculate it. You have to have intuition. What's the frequency response going to look like? If you're putting two stages and three stages, you have to have a sense of phase margin and make sure, you know, it's going to be stable. You know, because if you don't have, you know, the thing about simulations is they're stupid. They will simulate whatever you want to simulate. That's right. If you place equal importance on every aspect of every design, you will never finish the design. Your intuition is, tells you which things are going to screw you and which things you can ignore so that you can spend your limited lifetime in the wee hours of the morning focusing on the things that will get the job done.

**Adrian Tang:** As the two liter of Coke is running out. Exactly. Your eyelids are drooping and...

**Adrian Tang:** Well, we're going to put separate plumbing in my home just to run the soda to me.

**Adrian Tang:** You could make like a hat, like those, the hats that you wear with the cans on them but just have like a tap that goes straight to it. Yeah.

**Adrian Tang:** The problem is if it has the container on it, it's too heavy. And I did look at this. Yeah.

**Adrian Tang:** Right, right. Well, speaking of useful commercial products like that hat that might feed you Coke on a regular basis, what about this stuff? I mean, so all this stuff that you're talking about, the hundreds of gigahertz and monitoring water and stuff like that, this is bleeding edge. Is it working its way into industry at all? I mean,

**Adrian Tang:** are you...

**Adrian Tang:** Okay.

**Adrian Tang:** I mean, okay, I'm going to get everybody mad but I might as well do that. There is a huge question about what is this stuff useful for? And, you know, people talk about all kinds of weird stuff. They say, we're going to communicate at high frequency. Let me, let me spend three minutes and just straighten the record as someone who actually, you know, builds the stuff my whole life. High frequency beyond Wband is stupid for wireless.

**Adrian Tang:** Is this like the 5G stuff and things like that?

**Adrian Tang:** 5G and beyond. Like, okay, so yes, you can build a point-to-point link from A to B and focus down with the lens because wavelength is short and do a point-to-point link. You can also run a fiber optic and it's cheaper. So that's not wonderful and when it rains, you'll still have a signal. So then people think that, oh, if we go to 60 gigahertz, we're going to have epic bandwidth. We're going to have bandwidth so then we can send more. The problem is it's not the radio that limits the bandwidth. It's the ADC and the DAC. Yeah, you can have infinite bandwidth but if you can only digitize a 50 megahertz slice, then you can only digitize a 50 megahertz slice. Or you're going to do what? You're going to have a gigabit per second in your phone. Well, guess what, buddy? Your clock's going to be clocking two gigs in your baseband processor and your phone's going to burn your leg. It doesn't make much sense. Those high data rates don't come at low power. They don't come in a mobile compatible type of form factor. You see all these ISSC papers, IMF papers, RFSC papers, 60 gigahertz, da, da, da, da. Really cool. People worked really hard. They did good work. It's impressive. It's also a watt, right?

**Adrian Tang:** Yeah, right. Yeah, a processing. You got away from carrying away, carrying the huge phones with the huge batteries on them. People like the ones that fit in the pocket.

**Adrian Tang:** So the whole world has kind of figured out that there was 802.11a, right, which was five gigahertz. And then there was 802.11bgn, which is like 2.4 gigahertz. And then there was like the 60 gig craze, right? The Y gig and the 802.11ad and the 802.153c and we're all going to go up to 60 gigahertz and life's going to be good. Now everybody's talking about 28 because they figured out 60 is too tough. The packaging's too hard. The power dissipation's too high. The baseband processing's too crazy.

**Adrian Tang:** Right. Aren't there like limitations on like the range and how far you have to be away from the receiver?

**Speaker ?:** Of course,

**Adrian Tang:** that's the other problem. Who the hell wants a Wi-Fi that you have to put a router in every room of your house? It doesn't feel like a cell.

**Adrian Tang:** And it's like beam steering can help with that, right? But it's not going to go through a wall. It's not going to... Exactly. You'd have to be an open space.

**Adrian Tang:** You know, the faculty side of the world, they talk about, you know, SDMA, beam forming to 200. Go to the Beijing train station and look at how many people are holding the phone. You're going to form that many independent multiple beams and have the processing for it and have it on board the mobile. Get real. So that was one huge thing is the communication. But that seems to have calmed now. People are still doing point-to-point links. And that's sort of interesting if you can't lay a cable. Then there's a lot of work on short-range 802.11... Not 802.11. Sorry. Short-range 60 gig. And there's a couple of successful things here and there going across the table, docking your laptop, whatever. But you're competing with a $1 cable. So you're going to spend $100 on a packaging solution that competes with a twist of copper. Right, right. So that's kind of the communication side of it. Then the other side is the security side. So that you look at the IEEE, solid-state circuits, or MTT, micro-error theory chainings, there's a billion papers on trying to do imaging at these frequencies and build radar systems. And we're going to see bombs under people's shirts. So Ken Cooper here at JPL is, I would say, the expert on working on that. He's been working on that as long as I've been here. Okay. Which is threat detection under people's clothes. And he built this beautiful radar system using all the space technology that's a 680 gigahertz radar, 30 gigahertz bandwidth. You know, so centimeter resolution. And, you know, he did great work. You can see the target. It's there. You can see the gun. But the problem that he encounters, which is the same I'll encounter, is you need a trained person to look at this thing to say what it is. The part-time guy is not going to be able to process these images and identify the threat 100% of the time. 680 gigahertz, the advantage of imaging with that is that you can be a standoff. You can be several meters away.

**Adrian Tang:** Oh, okay. Yeah. So you could just do it passively or not going through a scanner or maybe walking by kind of thing or something like that? Yeah, yeah, yeah.

**Adrian Tang:** Covertly. So it's a thought exercise. You know the ones you go to the airport, you put your hands up and they scan you?

**Adrian Tang:** That's right. Yeah, like circles around you.

**Adrian Tang:** Yeah, that's 30 gigahertz. There's no reason to go to 600 gigahertz. That's 30 gigahertz. And the key to that is that you know you're being scanned.

**Adrian Tang:** The psychological element, you mean that kind of thing, like the kabuki theater?

**Adrian Tang:** You've walked into the box, right? And you know you're being scanned. You're consenting. You're stepping into the machine understanding that you're being scanned. Okay. So if you have people that understand they're being scanned, you only need 30 gigahertz, which is a lot cheaper than 680 gigahertz. The only time that you want 680 gigahertz is when you don't know you're being scanned because you're doing it remotely.

**Adrian Tang:** You're walking into a stadium and you don't, yeah, they're just randomly, yeah, scanning people.

**Adrian Tang:** Yes. But the issues are, number one, the systems are not that small. So envisioning a way to make them covert is complicated. You only have nine, nine, 10, 20 meters kind of range.

**Adrian Tang:** Why is this garbage can over here so warm? It seems like it doesn't take much trash and it really is putting off a lot of heat.

**Adrian Tang:** And the other, the other thing is constitutionally, there's some legal issues with scanning people. Yes. Of course. So you should definitely look at Ken Cooper's work or even invite him on here to talk. He has done so much work. He's the leading expert on all that stuff. Wow. Okay. So that was the other one that kind of fell away. And then the third one, which was the silliest one, the one that insults me directly is the people who are saying that we're going to find bombs by getting spectroscopic signatures out of bombs and backpacks.

**Adrian Tang:** Okay. So that's like, like what I'm doing. They get like nitrogen, nitrogen type of signature or something like that. And like, oh, this, this has fertilizer in it or something like that.

**Adrian Tang:** Let's see if there's a bomb in your backpack. First, we're going to have to puncture it so gas comes out. Then we're going to have to cool it to 77 Kelvin or minus 200 Celsius. So we have contrast. Then we're going to have to lower the air pressure so that we actually have lines that aren't too cute. Like that's just silly. So hope,

**Adrian Tang:** hope that you, you don't have your pet lizard in your backpack or something like that. Yeah.

**Adrian Tang:** So we can, we can build a million dollar instrument to do that or we can pay somebody $7 an hour with a pair of gloves. Like, right.

**Adrian Tang:** Yeah.

**Adrian Tang:** It's a society question. Do you want to waste money?

**Adrian Tang:** So these are the only applications you're saying outside of looking at stars and Yeah.

**Adrian Tang:** These are the ones that have been talked about at these frequencies. And you can look at my publication record. I've wasted my life looking at all these silly things. And then I decided after doing it and trying it that yes, space science is pretty much the only place for this. And that's why I'm here. Not really. I mean, at least there's space, right? Yeah. I love the science and I am really excited by what we do here.

**Adrian Tang:** I feel like there'd be like some sensor stuff, like, especially as you mentioned, like the shrinking of these sensor systems.

**Adrian Tang:** Sure. Sure. But you know, it's what, it's all about what you're sensing.

**Adrian Tang:** Okay. Okay.

**Adrian Tang:** The way to have a killer application for a technology is that it does something better than every other technology. There's nothing on earth where there's pressure and temperature that terrorists does better than everything else. If you're imaging, there's IR. if you're doing covert imaging, there's, you know, the FLIR and other cameras that can see just fine. Are you doing wireless? Well, there's, you know, Wi-Fi is pretty good. LTE is amazing. Yeah. Where does terahertz dominate? It only dominates up in space where there's not all these terrible environmental issues.

**Adrian Tang:** Got it. Okay. So it's just because it is removing all the other crap that would interfere with your reading.

**Adrian Tang:** Yeah. It's just not performing well down here at room temperature and pressure is not the place for those systems.

**Adrian Tang:** What is coming up in the space realm, I guess? I mean, so we're going to link to all of your papers and all the, your site, which is called sadcircuitdecider.com, which is a great, a great title for a site name. It's good. People remember it. Yeah. Yeah.

**Adrian Tang:** I mean, you don't sound sad, you know? Oh, I'm always sad, but I'm sad because there's a tape out tomorrow and I have 400 blocks to draw tonight.

**Adrian Tang:** Oh my God. Yeah. That's, that sounds like, yeah, that'll do it.

**Adrian Tang:** That'll do it.

**Adrian Tang:** So what is coming down the pipe and then we'll let you get back to your, your many, many blocks.

**Adrian Tang:** So we have another balloon mission flying this year in August, unless something goes wrong first called What's Up. It's the water hunting advanced terahertz spectrometer on an ultra small platform. It's an instrument for looking at water, finding water in places, comets, things like that, outer, outer solar system. And this is a test flight. So we're going to be just checking out the instrument. The sound side about building the instrument for the balloon is you also have to build the balloon craft. So all the transceivers, radio, tracking, telemetry, navigation, landing, launch, and dah, dah, dah, you have to build yourself. So that keeps you busy and power supplies and computers and flight software. Of course, we have that. We have, my group has a telescope called Astros, uh, Imran and Jose are leading that. That's an eight pixel multi terahertz instrument. That's going to look at star forming regions. I also want a balloon craft launched from Antarctica. I have a ground penetrating radar that we're working on and we're going to be testing it in parks in the LA area looking for pipes and all kinds of stuff. Ultimately for the moon or for Mars looking for water. I don't think there's any pipes on the moon. I'm just taking a guess here. You know, there's lava, there may be lava tubes on the moon, which would be useful for astronauts to live in if astronauts want to live on the moon.

**Adrian Tang:** Oh,

**Adrian Tang:** okay. That's, that's kind of cool actually. Sounds like kind of a boring landscape, but yeah.

**Adrian Tang:** Well, you know, the moon is not exactly known for its, uh, surprising, uh, things, you know, a lot of dust and yeah.

**Adrian Tang:** And then we'll be, uh, we're working on this UAV project where we're going to be flying this snow sensor, uh, over the Sierras or somewhere, hopefully, uh, next year. We have about, I think, 40 or 50 chips on the books to deliver this year and it's only February. Wow. So we're busy. So some stuff to do. Yeah. But it's great. It's, it's, you learn, you think every other chip designer, you know, all my friends down at Broadcom, they just get to learn chip. I get to learn about the universe.

**Adrian Tang:** Yeah.

**Adrian Tang:** So I feel like I'm winning. And then, and then, and then the fires come in the San Gabriel's and then I'm not so sure anymore. Sure.

**Adrian Tang:** Sure. The location may be unfortunate, but you know, it's your, just keep your brain safe and that's the important thing. This, I, I think this is the most confused and amused I've been in, in 480 plus episodes of the Amp Hour. So you're doing something right here, man. This has been very, very interesting. It has been a whirlwind and I really appreciate you being on the show. Where can people find more about you and your work? And are you looking for people to work for you or no?

**Adrian Tang:** I'm always looking for people that work for me, but it's a tall bar.

**Adrian Tang:** I, I, I have no doubt about that after hearing all of this stuff.

**Adrian Tang:** You need to relinquish your soul when you apply. And bring, bring cases of Coca-Cola with you, you know, like, uh, if you want to learn about just generally projects, my website, sad circuit designer, if you're interested in the details, the papers, right? I don't write papers because I like papers. I don't write papers because it helps my career. I write papers because it's an opportunity for everybody to understand what I did and therefore not make the same mistake. Most of my papers end with, and we tried it and it sucked. And we're thinking about doing this next. So stay tuned.

**Adrian Tang:** Yep. Yep. Wow. We'll have links to all this stuff in the show notes as well.

**Adrian Tang:** uh, it's been really great. Adrian, thank you so much for being on the show and thanks for making stuff that measures space. I think that's an important social need.

**Adrian Tang:** Yeah, no problem.

**Adrian Tang:** All right. We'll talk soon.

**Adrian Tang:** All right.

**Adrian Tang:** Bye.

**Adrian Tang:** Bye.

**Speaker ?:** Bye. Bye. Bye.
