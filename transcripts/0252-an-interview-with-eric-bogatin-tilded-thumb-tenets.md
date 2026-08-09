---
episode: 252
title: An Interview with Eric Bogatin - Tilded Thumb Tenets
url: https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/
---

**Eric Bogutin:** This is The Amp Hour Podcast, recorded June 2nd, 2015. Episode 252, with guest Eric Bogutin. Tilded, thumb, tenants.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Eric Bogutin:** And I'm Eric Bogutin. I'm the Dean of the Teledyne LeCroix Signal Integrity Academy.

**Dave Jones:** Thank you very much for joining us, Eric. Awesome to have another Signal Integrity guy on here.

**Chris Gammell:** Yes, something I still don't understand, so I expect you to dean us into knowledge here.

**Dave Jones:** He's the Dean of Black Magic, right?

**Eric Bogutin:** That's right. I like that. Well, I don't use that term. Someone else uses that term. And I tend to think it's all engineering. It's not Black Magic. Science and engineering. Come on, now we retired. It's up for grabs now. Well, and you know, I teach Signal Integrity in a lot of different places on campus and to engineers. And I emphasize that it's not magic. It's really engineering. And if you understand the principles, then everything else flows. It's because we don't teach it in schools very much. And so the kids coming out of school, they don't understand Signal Integrity. And they learn it from the street or they learn it from marketing.

**Chris Gammell:** Oh, man. I grew up in a rough area. I learned.

**Dave Jones:** Oh, man. I got pregnant with Signal Integrity. Oh, I learned so much.

**Eric Bogutin:** And you know, sometimes they use that term street smarts as a good thing. And when it comes to engineering principles, if you don't have that foundation in really solid engineering, the street smarts that you pick up may apply to a couple specific situations. But you can't generalize. And okay, it worked in the last design. But just because it worked in the last design doesn't mean it's going to work in the next design. Right. And that's why I'm a big fan of if you want to do engineering in general, you've got to have a strong foundation in the principles of engineering. And everything flows from there.

**Dave Jones:** What do you mean by it? Do you mean like more like the physics level stuff? Or do you mean what, you know, what aspect of engineering do you mean? Yeah.

**Eric Bogutin:** Well, for Signal Integrity, it's mostly electrical engineering. Although I am kind of unusual in the Signal Integrity field because I'm actually a physicist. All of my degrees are in physics. All my training is in physics. And I approach problems a little differently than engineers do, especially electrical engineers. And so from – and I think that's part of where some of my successes come in being able to, you know, kind of explain the effects and provide a coherent kind of set of principles because I look at it from a physics perspective. And that means kind of building your kind of engineering intuition about what's going on. It's about how the fields interact, about how signals propagate. And, you know, it's kind of like the – I have an essential principles class. It's the foundation building class. And one of the first things I talk about is how do signals propagate on a transmission line. First, what's a transmission line? What is a transmission line? Yeah. Right. Right. And then how do signals propagate? And I would say, you know, 50 percent of the misconceptions out there about signal integrity problems are because engineers don't have a really good understanding of what's a signal look like on a transmission line as it propagates. Right. And it is remarkable how many – you know, I always – you do these surveys when I do classes. And I ask, how many of you have taken or studied Maxwell's equations in school? And if you've got an undergraduate double-E degree, you know, you looked at it at least once. You know what they are. You've seen them. You maybe took an E&M class. And then I ask, how many really understand what does it tell you? What do they mean? Other than, you know, they're differential equations and you've got to get the boundary additions and solve them and here's an equation that comes out. And very few people understand what do they tell you? What do they mean? And that's what I mean by an engineering foundation is, yeah, you have the equations but you also look at what are they telling you? What do they mean? How do you use them to help you understand a signal propagating on a transmission line?

**Chris Gammell:** It's an interesting contrast because actually last week we were talking about – you know, I'm very big on like starting with practical and then kind of moving down through the layers of abstraction. But I think about like signal stuff like this and I don't know where you'd really start because there's not really – I mean like there's not really a starting point. So how do you then tie that together with – I mean you can't start with the practical. I mean you could I guess pull out like a, you know, a VNA or something and start looking at signals and look at real measurement stuff. But how do you finally pair that stuff together? Do you have to start at the base physics level or can you start somewhere else?

**Eric Bogutin:** So that's a good question. And that's where I came up with – I call them, you know, my essential principles. They're like, you know, a dozen different essential principles. But the most fundamental one is this idea of all interconnects are transmission lines. They have a signal in return. And a signal is a voltage between the signal and the return. And once you apply that signal, you touch a battery between the signal and return path, those conductors, that voltage is going to propagate. It is dynamic. And that idea of, you know, changing your head from how we're taught in kindergarten about, you know, voltage is everywhere the same on a line to the dynamics of they're propagating really fast. But they're still propagating. And it's the propagation of the signals, that voltage wave traveling down the transmission line between the signal and the return, it's the propagation of that wave that is at the heart of so many signal integrity problems. And so I – you know, depending on the audience, I'll start out with that concept of that voltage that propagates. And then if you have a little bit of fields and you say, well, hey, you've got two conductors, a signal in return, like in a coax cable, for example, signal in return. You put a voltage between the signal and return. And what do you get? Well, between the signal and the return, you get a voltage difference between those two conductors. You get an electric field. And now you came along and you suddenly touched that battery between the two conductors. You created an electric field. Well, that electric field now is – it doesn't just sit there. It propagates down the space in between the signal and the return. And it's that electric field that's propagating down the transmission line that is really the heart or the basis of Maxwell's equations. Maxwell's equation says, you know, if you make a changing field, when you generate that initial voltage on the line that's a changing electric field, that changing electric field generates a changing magnetic field that generates a changing electric field, and that self-propagates.

**Chris Gammell:** So does that mean that your students are coming in as already having – so, I mean, I guess in that case, right, a consistent voltage on a line would be like another layer of abstraction where it's like that's not actually what's happening. It's just a construct that they use because it's way, way more convenient. So do your students already have that or does that toughen the college level where they might not already have the hands-on, I know what a voltage sitting on a line is?

**Eric Bogutin:** Right. So I get students that cross the whole spectrum. My students at CU in Boulder where I teach a graduate signal of Terry Day class, I get some undergraduates, mostly graduate students. They've all had at least one semester of E&M, and they – yeah, they can solve Maxwell's equations, but they don't really know what does it mean, what does it tell them. And so this – the class that I teach really – I see so many of the guys walking away with an aha moment of suddenly they see this is how you use the principles of Maxwell's equations but in a practical situation. And in the industry where I teach engineers, I get from technicians that – or mechanical engineers – and I mean this in the most loving way a lot of my friends are mechanical engineers, but they don't have that intuition of electric fields. And so this is a whole new concept of the electric field. And when we – I first started doing this 20-some years ago, I realized that this idea of the signal propagating down the transmission line once it's launched and it sees as it walks down that line this instantaneous impedance each step along the way, I realized that that was such a novel concept for most folks. I used the expression when I would teach this. I'd say, well, you have to think about it in a kind of a zen way. You have to kind of be the signal. Think about what's the signal signal. And so I was doing these classes in – I was doing these classes in San Jose and my wife was a partner in the company. She and I started it 20-some years ago. And she would do all the project management and organizing and she'd be there. And she was kind of like the – she ended up being kind of like the den mother for a lot of these engineers that were struggling. And she would come to the classes and when I teach about be the signal, I would walk down an imaginary line in front of the class. And I say you walk down the line. You're being the signal. You're looking at each step along the way. This field is propagating. It's charging up the line. You see this instantaneous impedance. And you think about the changes of impedance that signal sees each step along the way and that influences reflections and other things. And she said that during one of the breaks, there were three guys from a large semiconductor company that were off on the side and they were arguing with each other. They were weeping. About a design. They were working. They were being the signal. And one of the guys was walking down the line. He's saying, okay, let's be the signal. You walk down the line and then they veered off where there was a branch point and they realized, oh my gosh, the signal sees 50 ohms. One way 50 ohms sees 25 ohms. That's why they were getting reflections. And she said that it was such an epiphany for these guys to kind of use this model of being the signal. She was the one that said, hey, we have to name our website when we went online. We have to name the website Be the Signal because it was such a fundamental concept for understanding signal integrity. So we became Be the Signal because of her observation of how valuable it was for those engineers. No, I love it. So that was kind of where it came from. But I think if you're not going to be a real hardcore signal integrity engineer doing a lot of simulations, you don't need Maxwell's equations. You just need to understand what do they tell you and what are those kind of like you said, the abstracted principles that you get from Maxwell's equations. What do you need to know to think about, to use your intuition to think about signals propagating the problems that they encounter?

**Chris Gammell:** Yeah, we used to do – at Keithley, there used to be – I was talking about mantras. Like they would be like mantras. Yeah. And it would be like, you know, we're kind of going through a problem and, oh, okay, well, V equals LDIDT. And so because of that, blah, blah, blah, blah, blah, blah, blah, blah, right? There's a spike here. Right. And that's why that's happening. And I'm sure that that's kind of the same thing. You kind of anthropomorphize everything. You say, I am the electron. I am the signal. You know, that kind of thing. And what would really happen if I'm walking through here? So I like that a lot.

**Eric Bogutin:** Yeah, and that ties into – it really kind of grabs hold of your intuition. And so much of designing is, you know, creative and intuition-based. It's not, you know, run a simulator for three days and get an answer. It's really thinking about from a conceptual level, you know, getting a feel for the numbers and getting a feel for the design and having a sense of what would happen if I did this or that. And, okay, if you want to know do you need the spacing 2X or 3X, okay, that's where you use a 2D field solver. But to know that increasing the spacing is going to decrease the crosstalk and why, that's where your physical intuition is really valuable.

**Dave Jones:** Can you run – can you do a lot of SI with just rules of thumb and intuition like that? Or do you – you know, at what point do you have to go to a field solver software to actually fix your issues?

**Eric Bogutin:** Right. So this is a question that I debate in the industry a lot because I find kids that come right out of a graduate program in signal integrity where they spent their graduate career, you know, four, five, six years solving master's equations in different ways and using 3D field solvers. They'll say, oh, you can't do anything with that master's equation. You got to, you know, grab your 3D field. Any problem, grab your 3D field solver because that's the answer to the question. Right. And my approach has always been you want to get to an acceptable answer as quickly as possible. And so you want to have three tools in your toolbox to use. You want to be able to be well-versed in rules of thumb. There's a limit to – you know, there are a balance between accuracy and effort. Tiny little effort, you know, not a huge amount of accuracy. But they help feed your intuition, give you quick answers immediately. And then when you need a little bit more accuracy, that's where approximations come in. And, you know, we call them formulas. But, you know, we tend to think, oh, if you see a formula, even if it's complex, it must be accurate. The more complex it is, the more – there's no connection between complexity and accuracy. But it's a – you can put them in spreadsheets. You can identify what's important, how they're related. They're also really valuable tools to have to help you analyze a problem. And then there are numerical simulation tools. And that's when you want to know, okay, what's going to be the noise margin here? How much is going to reflect here? If I have a branch and I have multiple reflections, I can't keep track of that in my head. The only way is with a SPICE simulator. Or if you want to know how much crosstalk do you have when the cross-section is this much, you have to use a 2D field solver to do it. And so I advocate you need – a good engineer needs to be versed in all three of the tools and use them appropriately when necessary. But that rule of – those rules of thumb, critically important to help feed your intuition. And I actually – I write a lot for the different sources out there. And I write for EDN a series of rules of thumb.

**Dave Jones:** Tell us what other rules of thumb. Can we run through a couple?

**Eric Bogutin:** Oh, yeah. So I've got, I don't know, about 26, 27 so far.

**Dave Jones:** Well, let's run through the top three or something.

**Eric Bogutin:** I'll go through a couple. Okay. So first of all, about signals. So I also advocate it's important to be bilingual in thinking in the frequency and time domain about signals. I like that. And when you're in the – because it's all about what does it take to get to the answer fastest. And if you have a signal in the time domain, like a square wave, then it's got a couple features in it. You've got a whole bunch of voltage versus time data there. But there's only a couple of terms, a couple of figures of merit that describe that sine wave, that square wave. There's the period or the frequency. There's an amplitude. And then there's the rise time. And if you know just that handful of two or three numbers, you can pretty much know all the features of that square wave in the time domain. And depending on the question you're asked, you can maybe look at that signal in the time domain and answer the appropriate question. That information in the time domain, we can also translate it into the frequency domain. And if we take an ideal square wave, really fast, like a zero picosecond rise or one picosecond rise time, we take that square wave in the time domain and translate it into the frequency domain, it's got a pattern to it as well. We're going to see the spectrum, basically. We're going to see the harmonics at multiples of the clock frequency. There's going to be an amplitude to the harmonics. And those amplitudes are going to drop off. And they're going to drop off like one over frequency. And so even if you have an absolutely perfect ideal square wave, the spectrum of it has frequency components, those amplitudes that drop off like one over f. And so the question is, okay, if I know the features in the time domain of my square wave, what's important for the frequency components in the frequency domain? What do I need to know about those frequency components? Well, one figure of merit is if it's a 50% duty cycle signal, then there are no even harmonics, only odd components. So that's one figure of merit, the connection in the time domain with duty cycle and the connection in the frequency domain with odd versus even. That one over f drop off is a feature of a short rise time square wave. So they're always going to drop off like one over f. So that's another figure of merit is dropping off like one over f. But then the last important piece is how high do you have to go? How high a frequency component is important? And if you have a one-picosecond rise time signal and it's – pick a number. So it's at a megahertz. So it's a really fast-edged megahertz. You're going to have frequency components at one megahertz, at two, at three, at four megahertz, the harmonics. If it's 50% duty cycle, okay, the even harmonics are zero. So you have the odds that are left. But how high a frequency do you go? Do you go to the three megahertz, five megahertz, seven, nine? Do you go to 101 hertz, eight megahertz?

**Dave Jones:** How high do you go? And what about if it's a one-hertz square wave? Same rise time.

**Eric Bogutin:** Same rise time. Right, right, right. Then how high is the highest frequency you have to worry about? And we call that highest frequency, that highest sine wave frequency that's important, we call it the bandwidth. And so the question is, what's the bandwidth of that one hertz signal in the time domain? What's the bandwidth of that signal as the highest frequency I have to worry about in the spectrum, in the frequency domain?

**Dave Jones:** Minus 3 dB bandwidth we're talking.

**Eric Bogutin:** Well, that's one of the questions is how do we think about the bandwidth? Because if you use that colloquial expression of, oh, the minus 3 dB point. Well, if you look at the frequency components in the spectrum, the amplitude – so let's do a one-volt square wave amplitude. If you look at the frequency components in the sine wave spectrum, the amplitude of the first harmonic is 0.66 volts. So it's a one-volt in the time domain, square wave, and it's going to be 0.66 volts as the first harmonic. The second harmonic, if it's 50% duty cycle, second harmonic, 0. Do you know what the amplitude of the third harmonic is? Tell us. It's – well, it turns out it's pi over 2. I'm sorry, it's 2 – I have to remember the numbers. But it's 2 over pi – let's see. Well, it's about 0.22 is the amplitude of the third harmonic. Okay. So that's already down by a factor of 3. So that's more than that's – you know, power is 3 dB, amplitude is 60 dB. Right, right.

**Eric Bogutin:** It's way down. So, I mean, naturally they're going to drop. Even if it's a one-picosecond rise time signal at one hertz, the next harmonic is going to be down, and the next one is going to be down by another, 1 over 5, and the next one drops by 1 over 5. So even though they're really tiny, if we care about that one-picosecond rise time, they're all important. And so the question is, how high do you have to go in order to be able to replicate that one-picosecond rise time? And so the bandwidth in the frequency domain you worry about, how high a frequency you go to, so you can still replicate that 1090 rise time in the time domain, that bandwidth is, turns out, when you do the analysis, is about 0.35 over the rise time. So if you've got – let's do a real number. Bingo.

**Dave Jones:** That one's common. That's a common rule of thumb. It's a common rule of thumb. There's our oscilloscope bandwidth rise time rule of thumb formula, which I've done videos on, and you'll find in any textbook.

**Eric Bogutin:** Yeah. Now, that's based on if I have a cliff filter. So I take out absolutely every single component above the bandwidth. So there is zero amplitude above that bandwidth. And I just have the frequency components that are left. So I have a filter, basically, or some amplifier that has a response like a bandwidth up to some frequency, and then everything above that is zero.

**Chris Gammell:** 10,000 tap FIR filter or something like that? Yeah, exactly. I think I tried to make it as an issue.

**Eric Bogutin:** But I've set the amplitudes zero. So it's like a 20th order or 21st order Butterworth filter or something like that. So it's a really well-defined edge. Uber butter. So I know that the frequency components above that cutoff are zero. Nothing there. And I sent a zero picosecond rise time signal in. I'm going to get a rise time signal coming out, that 1090 rise time of 0.35 over the bandwidth, where that cliff filter is. Yeah. And that's the rule of thumb connecting the feature in the time domain, the rise time in the time domain, with the feature in the frequency domain, the bandwidth, the highest frequency component you're going to see. And there are some assumptions in there, but that's a really good starting place. Yeah. So that's the first rule of thumb.

**Dave Jones:** It's only a rule of thumb because it is totally dependent upon the shape of your filter. You know, it's like...

**Eric Bogutin:** Absolutely. Exactly right. It's about the shape. You know, we're assuming that we have kind of a Gaussian edge of the signal going in. We assume that, you know, it's a repetitive signal, a long-time repetitive signal. And we assume that that bandwidth is, we don't care about any frequencies above that. And so we set them to zero. So there are a lot of assumptions there, but, you know, sometimes, you know, one of my favorite expressions, one of my other rules is, sometimes an okay answer now is better than a good answer late. And if you're familiar with the rules of thumb and the assumptions behind them, you can really use them to get to answers quick.

**Dave Jones:** And it's reasonably close because, correct me if I'm wrong, and I may be, because I don't know this stuff in detail like you do, is it's going to vary between somewhere from 0.35 to about 0.5. 0.5. Is that correct? Depending on practical filters. Like if you've got a brick wall filter, it'll be 0.5 instead of 0.35.

**Eric Bogutin:** Well, okay. So here's a little bit of the specsmanship issues. Because, okay, so Tullin and LaCroix, we're the number three largest scope manufacturer in the world. You get tech number one in terms of market size and volume. You get Keysight as number two. And then Tullin and LaCroix is number three.

**Dave Jones:** Who's doing the fastest, the bestest kick-ass scope out there? Is it LaCroix? Who's like really leading the bleeding edge?

**Eric Bogutin:** I'll give you the numbers. The highest real-time bandwidth scope out there right now today that was announced almost a year and a half ago is from Tullin and LaCroix. It's a 100 gigahertz bandwidth real-time scope that samples 240 giga samples a second at 8-bit resolution.

**Chris Gammell:** Is that the one that Shariar did a review on? Yeah, he did a teardown of it or something. Ah, okay. Yeah, yeah. Yeah.

**Eric Bogutin:** So 240 giga samples, that's like 4 giga samples. That's like every 4 giga seconds, you get another 8-bit of a measurement. So that's pretty darn fast.

**Dave Jones:** How is that not black magic? How is that not black magic? I ask you.

**Eric Bogutin:** Oh, gosh. You know, I'll tell you, the engineering team, I report to the CTO and he runs the engineering team and he is so proud of his engineering team because there was so much engineering that went into the design of that high bandwidth scope. I'll give you one example. So the technology, the semiconductor technology to take those samples so quickly, well, it can't be silicon. Exactly. We used to use germanium-doped silicon. That's traditionally what had been used. That's a little faster. You kind of strain the silicon lattice with the germanium and that gives a little higher electron mobility. But to make this scope work, we had to use indium phosphide.

**Dave Jones:** Nice.

**Eric Bogutin:** And that was partly why LaCroix got purchased by Teledyne because it turns out that Teledyne Technologies has the largest fab, non-captive fab for indium phosphide. Ah. Why did they have it? For what purpose? I think it's for space applications. Right. Well, indium phosphide has a really, really high electron mobility. So they use it for cars, the anti-collision radar, 77 gigahertz. That's indium phosphide.

**Dave Jones:** So the ridiculously high bandwidth stuff.

**Eric Bogutin:** Right. It switches really, really fast. Yep. And they were – so Teledyne Technologies, they acquired Rockwell Technologies, Rockwell Science Center, and that became the Teledyne Technologies Science Center. And they developed the indium phosphide technology for – I don't know, might have started for the space shuttle program or some space-related, but it's real high bandwidth stuff. And they were looking for applications for it. And some of the folks from New York, LaCroix, were really intrigued with indium phosphide. So they took a trip down to the old Rockwell Science Center, the Teledyne LaCroix – or Teledyne Technology Center. And they talked to them about indium phosphide. And it was like, hey, you've got – you've got some peanut butter there. We've got some jelly here. Hey, let's make some sandwiches. And so eventually Teledyne Technology says, hey, we've got this outlet for using our indium phosphide, and you've got some other cool measurement instrumentation technology. Hey, why don't you just come over here, and we'll grow more measurement instrumentation stuff. And so that's how that marriage happened. But it was a marriage over indium phosphide, basically, is the selling point.

**Dave Jones:** So do these indium phosphide chips, do they have to be hand-selected for each scope, hand-matched, or anything like that? Or is it –

**Eric Bogutin:** Nope. Nope. No? Really? Really? So here's the key thing about the digital world compared to the RF world. And so I encounter this all the time at CU because CU has a really large electromagnetics group. It's really sharp guys there. But they're all focused on RF and antennas and mimics, and everything is RF-related in one way or another.

**Dave Jones:** Oh, bloody analog guys, yeah. Bloody analog guys.

**Eric Bogutin:** And they kept saying, oh, signal integrity. That's just so easy. Everybody does signal integrity. And then I get my students in the class, and they realize that they've had it really easy in the RF – and relatively speaking – in the RF world, because in the RF world, everything is narrowband. All you care about is what happens at one frequency. And you can use stubs on circuit boards to tune the impedance to get higher, lower impedance.

**Chris Gammell:** Sometimes it hops a little bit, right? It hops from frequency to frequency and stuff.

**Eric Bogutin:** Hey, that's where the design comes in to keep that narrowband there. Right, right. And everything about design is I just care about one frequency. But in the digital world, the bandwidth for the RF world is really narrowband.

**Dave Jones:** That's why you can get away with just free air on copper-clad board, right? You can just homebrew it, right?

**Eric Bogutin:** Yes, exactly. Right, exactly. As long as you engineer the structure, so the impedance and the frequency you care about is the value you want. You can build all sorts of stuff with it. But in the digital world, the bandwidth of signals is wideband. We have to worry about not just the rise time of the signals, the high-bound stuff, but all the way down to DC. And so the bandwidth of signals is from DC to that – Daylight. 100 or 50 – to daylight. Yes, exactly. Exactly. I like that phrase, DC to daylight.

**Chris Gammell:** Yeah, it works until you start asking, well, what's DC really? Come on. What is DC? You've got to give them to cough up.

**Dave Jones:** How long are you willing to wait? Let's be the electron, you know? No, no, not even like that.

**Chris Gammell:** I mean like you talk to an RF guy and he's like, oh, DC, like, you know, 10, 100 megahertz, something like that.

**Eric Bogutin:** You talk to a low level. But even those RF guys, they only care about, you know, at 1 megahertz or at 5 megahertz, just that one frequency range. And it's relatively easy to design an impedance for a target impedance at one frequency. When you need that impedance to be wide band, that's really hard. And so for these indium phosphide chips, it's not just, you know, 100 gigahertz. And what's it look like at 100 gigahertz? It is from DC to 100 gigahertz. And so that means you have to engineer everything. It's all signal integrity. And so these chips, the indium phosphide chips that do the initial A to D, they have an opening in the ceramic package with a little coax connector. So that coax connector goes from the outside of the package where the board connects to right onto the die itself. Oh, nice. And they had to engineer that path from the circuit board through the RF connector, through the ceramic, into the die of the indium phosphide. They had to design that entire path so that it was wide band.

**Dave Jones:** I'm surprised you can even get away with a connector there.

**Eric Bogutin:** Well, that's where that, it's not magic. It's careful engineering. They did a lot of 3D, you know, asking about when you use a 3D field solver, when you want to engineer where little pieces of metals create stray fields and you want to engineer those, sculpt those stray fields to give you a uniform signal path. That's when you use a 3D field solver. You can build the virtual prototypes really quickly in that 3D tool to sculpt those electric fields to make a nice uniform path and make it wide band. And they use a lot of 3D field solvers in order to design that path.

**Dave Jones:** What is the best field solver software out there?

**Dave Jones:** Bar cost. Is there like one everyone uses or is it?

**Eric Bogutin:** Okay, so.

**Dave Jones:** I've opened a can of worms, have I?

**Eric Bogutin:** Well, I have to be a little careful. I mean, I've used a lot of them out there and it's a question of the metric of best. Right. For me, as I've gotten older, I've gotten lazier. And for me, best means easy. Right. Good answer, but easy to use. And so for 2D field solver, I really like the Polar Instruments. They're real popular for circuit board design. Really, really easy to use and pretty accurate. Right.

**Dave Jones:** Is there a trade-off between ease of use and accuracy?

**Eric Bogutin:** There is. And so that's one of the factors you have to add. You have to make sure it's, you know, I hesitate to use the term, but accurate enough. Right. And these field solvers are so good in general that you should be able to get 1% accuracy for any cross-section you can design.

**Dave Jones:** Yeah.

**Eric Bogutin:** Is that good enough for something like these bleeding edge scopes? Well, for the bleeding edge scopes, 2D isn't enough. You need 3D. Right. But if you're designing a circuit board and even, you know, for 28 gigabit per second, kind of the bleeding edge for board sales, 20 gigabits per second, hey, you know, a 2D field solver Polar Instruments is just a fine tool to use for that sort of thing.

**Dave Jones:** That sort of speed, 1% is good enough, right? I mean, it's more than good enough. 5% would probably be borderline good enough, perhaps.

**Eric Bogutin:** Well, so here's the deal with how accurate you need it to be. If you look at, just for this one idea of the characteristic impedance, you know, all high-end boards are spec'd to, you gotta, if you're gonna ship this board, it's gotta meet this characteristic impedance spec. It's gotta be differential impedance within 100 ohms plus or minus, you know, 10%, right? But, you know, the boards, when they come out, because of manufacturing variation, there's a distribution. Is it Gaussian? Kind of, sort of, sometimes. Right. I mean, usually you see it, you know, shifted to one side. It's 5% distribution, but it's shifted over because, well, the pressure in the press changed or, you know, everybody got over-etched a little bit. But it's somewhere, you know, if you look at enough boards, it'll be a Gaussian distribution. But it's got some width to it. And that width is, you know, maybe on the order of 10%. So if you have a center to that distribution that's off by 5%, then you've shifted that distribution and you have a lot more outliers that are beyond the 10% spec. Yeah, yeah. And so that's where the accuracy, even though, yeah, the variation of the board is going to be, you know, at least 5%. Why do I need 1% accuracy? That's so you can center your distribution. Center it, right. And increase yield. Got it. That's why you want 1% accuracy.

**Dave Jones:** Right. Yeah. So you can't use a 5% tool on a 10% manufacturing process. You need to use, there comes that, like, order of magnitude thing again. Like, you know, if maybe for a 10% accuracy thing, you need a 1% accurate, 10% manufacturing process, you need a 1% accurate shot at where you're going to be in the center.

**Eric Bogutin:** And then it's always a question of, well, how much is it going to cost? And that's where the value proposition comes in. Is it worth, you know, spending, you know, five times as much for, you know, twice the accuracy? But for 2D field solvers, gosh, that technology is so well established that accuracy isn't really the issue these days. It's ease of use and doesn't include my exotic structures that I care about. Like gridded planes is a big thing these days for flex especially. And, you know, these really thin boards that are used in cell phones and consumer products, you want really thin for space and size. You know, you think about a watch, I mean, you know, these iWatches and even iPhones, the circuit boards themselves are really thin. And to get, you know, controlled impedance lines and a thin dielectric, you need the gridded planes to help get you that little higher impedance.

**Dave Jones:** As in the, by gridded planes, you mean the old style crosshatch planes.

**Eric Bogutin:** Yeah, crosshatch, exactly.

**Dave Jones:** Tell us the difference between crosshatch planes and solid planes. Impedance.

**Eric Bogutin:** So if you just have like a microstrip, signal and return. Yep. And one of the important figures of merit you care about in design is what's the characteristic impedance? And so here's my 30 seconds. What's characteristic impedance? So remember that transmission on that cable we were talking about. We're going to be the signal. We're going to walk on that signal or walk on that transmission and be in the signal. Each step along the way, as that voltage propagates down to charge up that next little footprint of capacitance between the signal and return, we have to dump some charge and dump some charge in time as a current. So as that signal propagates down, that voltage wave, to support that voltage wave, we have to send some current into that line to successfully charge up regions of the transmission line. And each step along the way, we, the signal, are always asking the question, what is our instantaneous impedance? What's the impedance for that next step? What's the ratio of the voltage we're applying to the current going into that next step to charge up that region of the line? And that ratio of voltage to current is the instantaneous impedance. If I have a uniform transmission, like a coax cable, every step as I walk down that transmission line, every step, I'm taking the same length of stride in each time period. It's the same cross section, same capacitance. It's the same charge to charge up each footstep. It's the same current. It's a constant current going into that line. And that means each step I take, I see a constant instantaneous impedance. And if I have this uniform transmission line, as I walk down that transmission line, there is one value of instantaneous impedance I see in order for me – when I propagate down that line. That's right. And if I have a uniform transmission line, that one value of instantaneous impedance the signal sees as it propagates down the line, that one value is an impedance that characterizes that transmission line. And we call that impedance, that characterizes the transmission line, the characteristic impedance. That's right. And so it tells you immediately what is that one value of instantaneous impedance I'm going to see if I'm the signal walking down that line. And so from a signal integrity perspective, knowing that instantaneous impedance and engineering it to be the value you want it to be so everybody sees that same value, engineering that is really important. And so you design for a specific characteristic impedance. And so it depends on the space in between the signal and the return, the capacitance per inch in that interconnect. And if you have a solid plane, you get one value of capacitance per length and one value of characteristic impedance. If you now take out some of the metal in that plane – Yes, you have a hatch pattern. You don't have as many – That's right. A hatch pattern. You don't have as many electric field lines between the signal and the return anymore. You don't have as much capacitance. The capacitance has gone down. The characteristic impedance has gone up. And that allows you to build a thinner board with the same characteristic impedance.

**Dave Jones:** Got it.

**Eric Bogutin:** And that's used for flex, a lot of flex where it's really thin dielectric anyway and for a lot of consumer portable circuit boards where you really are constrained in thickness. So hatch planes are really popular these days. And you want to – so one of the innovations in 2D field solver tools is you want to be able to analyze what's the characteristic impedance not when you have a solid plane but when you have a hatched plane. Right. And so some of the new end tools are like polar tools. They're able to handle the hatch plane.

**Dave Jones:** Because as you be the signal and you're going down that microstrip on a hatched plane, at each step you might have copper under you and the next step you won't have copper under you.

**Eric Bogutin:** Right.

**Dave Jones:** And it's going to actually change. So the instantaneous characteristic – instantaneous impedance is going to change when you've got copper or no copper.

**Eric Bogutin:** You're absolutely right. And so the way to think about that is, okay, now think about a reasonable rise time. You know, if you've got a – easy to do in our head, a nanosecond rise time. So we talked about earlier about some of the rules of thumb and I mentioned the rise time and bandwidth. Well, another rule of thumb that's really important is how fast does a signal travel down a transmission line? And, well, in air, it travels down at the speed of light because light is changing electric field. Correct. And that's what the signal is. It's the change of electric field, right? Well, in FR4, in laminates, you know, the dielectric constant is like four. That slows the speed of light down and it slows it down with the square root of the dielectric constant. So it's not the speed of light in air. It's the speed of light in the laminate material. And so do you guys remember Grace Hooper? Oh, yes, yes, yes. Grace Hooper.

**Dave Jones:** Yes, Hooper. Sorry, can you? She invented – yeah.

**Eric Bogutin:** Yeah, she was the – I think the admiral in the Navy or – She was admiral.

**Dave Jones:** She was the first programmer, right? She designed – yeah. She was one of the first – technically the first computer programmer, was she?

**Eric Bogutin:** Yeah. Yeah. She was a big fan of computers. Well, no, no.

**Dave Jones:** That was Lady Arta, but anyway.

**Eric Bogutin:** Well, but she was a real strong proponent of digital computers.

**Dave Jones:** Yep.

**Eric Bogutin:** And she was one of the first users of the ENIAC for the tube-based computer. And she was a big fan in the Navy. She was pushing the Navy to get into electronics and move into high tech. And she used to talk about how slow the high-speed tube electronics was and how we had to innovate in the electronics because she said that the limitation with a lot of these huge – you know, ENIAC took up a couple of rooms. And the limitation was the speed of the signal getting around. And she would carry around a string in her pocket that was a foot long. And she said, this is a nanosecond. That's how far light goes in air in a nanosecond is a foot. And she was a big fan of kind of giving you a visceral sense of how slow electronic – relatively speaking, electronics is. So speed of light in air is a foot per nanosecond. You take that into FR4 and it slows it down by a factor of two. So it's six inches per nanosecond.

**Dave Jones:** That's a rule of thumb I always use. One nanosecond for every 15 centimeters. That's half a foot. Exactly.

**Eric Bogutin:** Yep. It drops quite high. You're right. Yep. Yeah, metric. Sorry. And I've learned – because I teach all around the world – I have learned to have to be bilingual. So I say, yep, in the States it's six inches a nanosecond. Everywhere else it's – you're right, 15 centimeters per nanosecond. You're absolutely right.

**Chris Gammell:** It should be centimeters here too. Let's be honest. Okay.

**Eric Bogutin:** Well, you know, the circuit board design industry is still mils and inches. I know. Yep. So I have to be bilingual. Yep. But yeah, so it's six or 15 centimeters per nanosecond. So now you've got this edge that's a nanosecond long. As it's propagating down the transmission line, that edge is 15 centimeters long. You've got 100 picoseconds, 0.1 nanoseconds. That edge is one and a half centimeters long. And so now you ask, okay, from that edge's perspective, that's where it's sensing that instantaneous impedance. If it's 100 picoseconds as a rise time, that edge is a spatial size of only one and a half centimeters. And so as long as that hatch spacing or the size of the hatch holes in the board, as long as they're really small compared to one and a half centimeters, then they're all blurred out. They're smeared out over that rising edge.

**Speaker ?:** How small?

**Dave Jones:** Order of magnitude? 10? Yes. 10?

**Eric Bogutin:** One tenth? Good estimate is a tenth of that rise time. So that means, okay, if a hundred picosecond edge, you've got one and a half centimeters. So as long as the size of those holes are one and a half millimeters, then that edge is going to blur out and it's going to look like the average.

**Dave Jones:** Right.

**Eric Bogutin:** So it's these kinds of rules of thumb that I think are really important for every engineer to have because you can instantly make this connection. And when I was teaching live class in consulting, I would go to companies and work with teams in design reviews. And it's in a design review where you've got five guys or ten guys in the room. You're looking at a design on the wall and you're trying to decide, is this going to work or not? That's where you don't want to take the time to run over and run your 3D field solver to see what the result is. You want to get a quick estimate. Is it going to work? Are we in the danger zone? And that's where using rules of thumb. And I found that just so incredibly effective in having whiteboard discussions with folks to be able to pull up these rules of thumb to be able to explore design space very quickly. And that's why I'm a big fan of them as one of three important tools every engineer needs in their toolbox. Not to be little of the other ones, but to emphasize, hey, everybody needs to use these rules of thumb.

**Dave Jones:** I think we only covered one rule of thumb. Well, more than one. Oh, I threw into the second one. Yeah, we're going to go to the second. We're going to have the top three rules of thumb. Is there another one?

**Chris Gammell:** And if we're also doing reminders, we still need to hear your favorite 3D solver too. I'm keeping track.

**Dave Jones:** Okay, we're going on tangency.

**Eric Bogutin:** Like I said, my wife says, hey, you push my play button, I don't shut up. So you have to rein me in a little bit. So, okay, here's the third rule of thumb. So we got bandwidth is 0.35 over the rise time. We got a speed of a signal in FR4 is 6 inches per nanosecond. Now here's a really simple design rule for 50-ohm microstrip in FR4. You want a line width to dielectric thickness 2 to 1. So you got a 10-mil wide line, 5-mil thick dielectric to the adjacent return plane, 50-ohm transmission line.

**Dave Jones:** How does that come about?

**Chris Gammell:** Sorry, can you repeat that one more time too? Sorry.

**Eric Bogutin:** Right. So you got a microstrip. So it's signal over plane with air above. Surface traces, basically. So if you want a 50-ohm characteristic impedance transmission line, so the signal would see an instantaneous impedance of 50-ohms each step along the way, you want a line width to dielectric thickness of 2 to 1. So the line width of 10 mils, dielectric thickness of 5 mils in FR4.

**Chris Gammell:** And that's what your standard FR4 is.

**Dave Jones:** So on a standard 1.6 millimeter, single-sided copper on bottom, one on top, how wide does the trace need to be? I could do the math now.

**Eric Bogutin:** Yeah, so if it's 1.6, then it's going to be 3.2 millimeters as the width of the line.

**Dave Jones:** 3.2, of course. It's double.

**Eric Bogutin:** Right. And that's for double-sided.

**Dave Jones:** Hang on. Right. That's double-sided.

**Eric Bogutin:** Right. Yeah. But typically, you're going to have four or six layers in there. And so it's depending on the thickness to the adjacent plane. And on the high-end boards, you're talking 24, 32 layers. I know. And there, you've got a 5 mil wide line, 2.5 mil thin dielectrics. Yeah. And it doesn't matter whether it's 10 mil wide and 5 mil thick or 100 mils wide and 50 mils thick. It's the aspect ratio that's important.

**Chris Gammell:** Ah, that's interesting.

**Eric Bogutin:** It's only about the ratio of line width to dielectric thickness that influences the characteristic impedance.

**Dave Jones:** Because the dielectric constant doesn't change a huge amount between different material boards, does it? It changes by 20% or something.

**Eric Bogutin:** Yeah. Yeah. And if you care about getting an accurate number better than 20%, don't use the rule of thumb. Grab your 2D field solver. Right. Right. Right.

**Chris Gammell:** I think this is a missing piece for a lot of stuff, too, with actually doing stack-ups in PCBs. Like, a lot of that stuff isn't usually covered and doing that kind of thing.

**Eric Bogutin:** Yep. And even, you know, so stack-ups is a whole other issue of, well, what's the best stack-up for signal integrity? Can I get that all the time? Right. And unfortunately, I see too many design teams will come up with the layer stack but won't specify any dimensions and just say to their fab guy, okay, you tell me the thickness of each of the layers for 15 lines.

**Dave Jones:** Yeah. Yes. A lot of people leave that up. They leave the instruction on the PCB, please make the correct thickness to give me 50 ohms. And then you leave it up to them to use their signal integrity tool to calculate. Right.

**Eric Bogutin:** And let me tell you, so the fab guys, there are a few exceptions. I mean, there's some really good design groups in some of the larger fab companies. Sanmina, for example, they have some great signal integrity engineers there. But most of the smaller fab shops, they can't spell signal integrity. They're right.

**Dave Jones:** So if you're ordering your board from a fab house and chai, you know, from PCB car. Yeah.

**Chris Gammell:** We try breathing those chemicals all day and see if you can do any problems.

**Eric Bogutin:** Right. So let me give you – I'll give you one example of how the fab house was going to screw you up. So, you know, typical board, you know, first the wrong – the worst place to put power and ground planes is in the center of the board. But a lot of guys do. So you put power and ground planes in the center.

**Dave Jones:** Why is it the worst thing?

**Eric Bogutin:** Well, for two reasons. One is if – you know, why do you have power and ground planes? Well, you're delivering low impedance, basically DC voltage.

**Dave Jones:** Low inductance, yes. Low impedance, low inductance.

**Eric Bogutin:** Low inductance and impedance in general to the chips that you're powering. And when you're – when you put the power and ground planes in the center of the board, that means that even if you have great, you know, power and ground planes, which your fab house is going to screw up and I'll tell you why in a second, you have to go up through the center of the board all the way up to the package. You do. Through the Vs. You always drop the Vs. And those Vs are long. And if you have decoupling capacitors, they have to go from the top surface all the way through half the board to the center of the planes.

**Dave Jones:** On the flip side of that, the advantage is putting them closer together in the middle is that you get greater distributed capacitance, greater distributed decoupling. Well, forget the word capacitance.

**Eric Bogutin:** That's one of those – that word capacitance is one of those misconceptions out there because people don't know how to think about impedance. But forget that. But now what you said is really important. You want the thin dielectric between the power and ground planes. Right. Not for the capacitance but for the low impedance. Yes. The low spreading inductance and impedance.

**Dave Jones:** That's what I meant, yeah.

**Eric Bogutin:** So now you build your board and you put the power and ground planes in the middle of the board. And you need a specification of an 064 board in order to fit into some edge card connector, let's say. And when you do the stack up, based on the line widths and the dielectric thicknesses for 50 ohms, you come out with a 32 mil thick board. And so what's your fab house going to do? They're going to say, oh, I need to add a dielectric fill layer here to make the total board thickness 064. And where do you think the fab house is going to put the dielectric fill layer? Right in the middle. That's right. Because, hey, that's better. That's easy. Because I'm going to get better yield. Yeah, that's right. It's going to get better yield. And it's just power and ground planes. Who cares? I'll pull them apart. I'll put the dielectric fill there. And now I'm going to have the total thickness. And it's symmetric. It's not going to warp. And so it's the perfect place. And that is the absolute worst place from a power distribution notion of putting the dielectric fill. So that's a case where if you leave it up at the fab house, they're not going to come up with the best solution for you. It may still work, but it's all about risk and insurance. And if you're not going to simulate, which a lot of folks don't do enough of, if you're not going to simulate, you're kind of using hope and keeping your fingers crossed to hope it works. And, you know, sometimes it does, but sometimes it doesn't. If you want to increase your luck, you want to do all the things that push you to a more robust design.

**Chris Gammell:** So this brings up a good question for me then. When, I know what your answer is going to be, but when do people need to start caring about this stuff? At what frequency? Like if you're just doing a linear regulator on a board, yeah. Right. Go ahead and tell me that it always matters.

**Eric Bogutin:** Okay. So what's the most common answer to all signal integrity questions?

**Chris Gammell:** It depends.

**Eric Bogutin:** It depends. You got it. Exactly right. So, you know, unfortunately, it depends. And you can use design guidelines that is kind of telling you the directions to head. You can use design guidelines to help you in the layout and the stack up of the board. And you can ask, you know, okay, suppose that, you know, for example, you know, one of the design guidelines is, okay, to not have to worry about crosstalk, line-to-line crosstalk, you want to keep the space in between the signal. If you have 50-ohm lines, you can space between the signal lines roughly twice the line width. Okay. There's another rule of thumb. Yeah. And that's based on using a field solver and putting in the numbers. And you find, okay, yeah, for 5% worst-case crosstalk, spacing twice the line width gives you that worst-case crosstalk. And so you say, okay, let me always use that design guideline. And I'm going to build my board that way. The downside of doing that is you're spacing the lines farther apart. You're making a bigger board or more layers. And that means more cost. And so if it doesn't cost extra, I always say, if it's free, you always want to do it. And I call those habits. If it's not going to cost extra, follow the design guideline. If it's going to cost you more because now if I use that design rule, I'm going to need four signal layers. If I don't use that and if I bring the lines closer together, I can route everything in three signal layers. I'm going to cut down a layer. That's going to be a cheaper board. And the question is, do you do that or not? And it's a question of how much risk do you tolerate? And if you're not going to simulate to evaluate, will it still work given the length of the lines and the rise time and the drivers and the noise margins? If you're not going to simulate to see, will they work if you bring them closer enough together? I know I'm going to have more crosstalk. Will it still work? If you're not going to simulate, then you have two options. One is you can just do it that way and try it in C. And you keep your fingers crossed and you hope that it's going to work. And maybe it will. That's how I operate this. And you know what? And if your rise times aren't very long or if you've got a little lower impedance of 50 ohms, it'll work. Or if the lines are relatively short, it may be fine. The problem is, of course, you have to be sure that you have good enough test factors to test whether it works, whether that term works or not. And you're just booting up isn't always an indication that it works. But so you can do it that way and kind of keep your fingers crossed, try it and see, test it, build it and test it. Or you can say, well, if I did a simulation – so just because you don't do a simulation doesn't mean it's going to work or not work. It just means you don't know until you build it. And if I don't simulate, if I say, well, you know, if I did a simulation and it told me, oh, gosh, the lines were too close, then what would I do to fix it? I'd pull the lines farther apart. I'd go to the four-layer board. And so you can say, if schedule is really important and I really want to get this board out, I want it to work the first time, then one of the design strategies is let me pay extra for the first set of boards. So I'll do everything I can to make it as robust. Buy – we call that we're going to pay extra for insurance. We're going to pay extra insurance. We build the board. We get it. We have it back now. High confidence is going to work. We're going to use it to debug the software and get the whole system working. We'll ship early prototypes with that more expensive board. And once we have the product out, now we have a cost reduction program to look in detail and try some of the things that will cut the cost down. You know, bring the lines closer. Now I can see. And if that board doesn't work because I brought the lines closer and I have fewer layers at slower cost, I still have my other product that I'm shipping out the door. And it's not in the line of the critical path if you're not going to simulate. And that's what simulation does for you. It allows you to build virtual prototypes. You can test those. It's like you're building and testing, only you're building it in this virtual environment. And if you have confidence in your simulation tool, you're almost as good. And if you know how to use it well, it's almost as good as building and testing it. So it's a shortcut path.

**Chris Gammell:** Yeah, I was kind of talking more from the – so, I mean, you and I had talked when we met at DesignCount a little bit as well. And I think we'd emailed about it too. Like there's a lot of people that are coming in from like the Arduino side of things. And, you know, you think about how you might have a spy bus and if it doesn't work at 16 megahertz, okay, well, you just turn it down to 2 megahertz and it starts working. You know, like that's kind of the level of that. And so that's what I really mean is like when should people – because I think a lot of our listeners as well are kind of in that, you know, learning or interested. And when do they go start playing with 2D solvers or, you know, taking your course or, you know, reading the books. Using the rule of thumbs even. Oh, yeah.

**Eric Bogutin:** Yeah. Well, I personally think that when you're in the 10 megahertz and above range, you should have some good intuition about capacitance and inductance and the IDTs. Because, you know, 10 megahertz, it's no longer, you know, that simple DC world. Inductance starts playing a role. Right. And so above 10 megahertz, you should have some idea of it. And, you know, I do – I love Arduinos. I do a lot of work with Arduinos. And I just started writing for Nuts and Volts magazine, in fact. Right. And I'm writing a number of articles on data acquisition with Arduinos and things you can do with it. And I think that if you're building, you know, the 16 megahertz, even 32 megahertz kind of systems, you know, as long as you use a half a dozen simple design rules, you can get away really well. About design, you know, controlled impedance lines, have return path adjacent signal lines. You know, one of the things – so I'm a big fan of the SparkFun guys. You know, they're down the street from me. They're a lot of really fun – I call them kids there. You know, I feel like when I'm around, I'm the responsible adult there. Right.

**Chris Gammell:** We've had them on the show. They're not very responsible.

**Eric Bogutin:** They're a fun crowd. They're a fun crowd. And so they have – I use the red board, which is, you know, $20 for an Arduino board. Yeah. And for an 8 megahertz processor, it works fine. But it is a terrible signal integrity board. It's two layers. Right. The power distribution from the regulator is this wandering line that goes all over the place. Yeah. But they did because it's only $20. Exactly. And that's why they did it. Yeah. But it's not a set of design rules that's scalable to, you know, maybe the 32 megahertz and above. Right. I think it'll be okay in the 10, 20 megahertz kind of range. So a handful of design rules will get you into the 100 megahertz range. Okay. The bigger problem is, you know, so many of these designs, especially the Internet of Things thing, boards, have RF on the board. Yep. And when you have RF on the board, you've got in one region a receiver that's looking at, you know, minus 100 dB kind of signals. And right next to it, you've got this clock pulsing away that may be, you know, 32 megahertz. And we said before, hey, but it's only 32 megahertz. But if it's got a short rise time, then you're going to have, if it's got 100 picoseconds, you've got, you know, 3 gigahertz bandwidth signals there. And they're right next to this receiver at 2.5 gigahertz. Yeah, exactly. Exactly. And so that's when you have to worry about the crosstalk and noise and shield and mix signal design. And so I think there will be – so you always want to use those low clock frequencies you can get away with. Like you said before, you, you know, cut the clock frequency out. You want to use as long rise time as you can get away with. And then, you know, when you're talking about 30-some megahertz clocks and above and mix signal, that's when you want to start worrying about signal integrity.

**Chris Gammell:** Yeah. If your FETs aren't burning some serious powers or going through the transition, they're just – you're just not doing it right, right? Yeah. Nice sloping curves. Right. I like that.

**Eric Bogutin:** Yeah. I have to be careful mentioning, you know, 32 megahertz because I rarely use the word megahertz. It's always gigahertz. Right. 20 gigahertz or gigabits per second is, you know, what the bleeding edge is these days. So we've got, you know, three orders of magnitude to go before the hobbyist level gets to the high-end stuff.

**Chris Gammell:** Yeah. Yeah, that would be interesting seeing that crossover.

**Dave Jones:** What are some of the major misconceptions that you keep seeing? Are there any really common ones?

**Eric Bogutin:** So one of them is capacitance in the planes, that that's what's important. It's not capacitance. It's actually inductance, spreading inductance and impedance. Another is this whole idea of characteristic impedance. And, you know, I always start out my classes, my introductory classes, I take a little coax cable and I say, here's this RG58 cable. Coax cable. Open at one end, three feet long or one meter long. If I take an ohmmeter and attach my ohmmeter to the front of the cable between the signal and the return, what impedance, what resistance will my ohmmeter read? And I would say 90% of the guys say 50 ohms. It's a 50 ohm cable. It's going to read 50 ohms.

**Dave Jones:** Oh, wow, really? It's open, right?

**Eric Bogutin:** And it's this idea of, you're right, it's going to be open, right? Because it's open at the far end. And so what does it mean to have a 50 ohm cable if my ohmmeter reads open? And so that's the idea of that instantaneous impedance that is, and as soon as, I have literally had guys come up to me after one of my lectures on this, and they'll come up and they'll say, oh my gosh, I had an aha moment. Suddenly I got this epiphany. I've been hearing 50 ohms for the last 20 years, and I didn't know what does that mean because my ohmmeter just reads an open on the sound. And now you suddenly get it. It's the dynamic nature of the signals propagating. So I'd say that's a huge misconception out there. Right. And then, so one of my tests, when I interview engineers, so I'll tell you guys, one of my interview questions is always, what's inductance? And it is amazing.

**Chris Gammell:** It sounds like another philosophical slash zen kind of like, show me the way of inductance.

**Eric Bogutin:** Well, it's one of those, I hate to say mysteries, but it's one of those poorly explained properties of conductors that I fault our textbooks. All except my textbook, of course, because I think I can explain it really well. But I fault the textbooks that are used in EE classes when they describe inductance. I fault them at instilling, I don't even, I would call it poor intuitive models of inductance, but just no intuitive models of inductance, all based on, you know, the integral of B.DA, normal to a surface, normalized to the current through this. I mean, you get these concepts of either flux linkages through coils or in terms of, you know, integrals of B.DA over surfaces.

**Chris Gammell:** Can we have me and Dave do a little guess-a-tron here? I mean, can we get the interview? I hesitate to ask as much, but.

**Dave Jones:** Well, how about he just tell us, what is your definition? How would you explain what an inductor is?

**Eric Bogutin:** So, I'm going to give you two answers. The quick one is, okay, so I have a whole chapter in my book, this signal and power integrity simplified, a whole chapter in there on the physical basis of inductance, where I go through in great detail. So, that's the short answer. The 30-second answer is, so inductance is fundamentally about how good a conductor is in generating rings of magnetic field lines. And so, you first have to have an idea of, you send current through a wire and you get rings of magnetic field lines. The more current, the more rings of field lines. But you want to look at the efficiency of generating those. You can count all those field lines that are around the conductor. And we count the units for magnetic field lines are webers of field lines. So, you take a wire, you know, five inches long, let's say. You put one amp of current and you can literally go in and count how many rings, how many webers of field lines, rings of field lines are around that wire. And now, the inductance of that wire isn't about, well, how many rings of field lines do I have? It's about how efficient is it at generating those rings? It is the ratio of the number of webers of field lines per amp of current. If I double the current, I double the number of rings of field lines, but the ratio stays the same. And now, when I change the shape of that wire, I bring the two ends closer together so it's now a loop or a ring or a loop. Or I go a signal and return path, for example, on a microstrip. I change the shape. Now, it's how those currents generate those rings of field lines around that conductor as I send current through it. And depending on the shape, the proximity, three things, three physical things that influence the inductance of an interconnect. There's the width. The more I can spread out the current, the fewer rings of field lines that I get. So I spoil the inductance. There is the length, of course. The shorter it is, the fewer rings of field lines I have over that shorter length to count. And then it's the proximity to the return path. The closer I bring the return path, I get current going down one direction. It generates rings of field lines circulating in one direction around the conductor. The return current is going in the opposite direction. It generates rings of field lines around that first conductor in the opposite direction. It helps to cancel them out. I have fewer rings of field lines, lower efficiency of generating rings. I have less inductance. Right. And that's why we want, like you said before, Dave, why we want the power and ground planes close together. Because the counter-propagating currents, the signal and return currents, power and ground currents in those planes going in the opposite direction. The rings of field lines of the power currents help to cancel out the rings of field lines of the ground currents. And we have less total number of rings of field lines, less inductance, and less voltage generated when the current changes. Right.

**Dave Jones:** And this is why you can get non-inductive wound resistors, because they're wound a certain way where they cancel out. Very good.

**Eric Bogutin:** Yes. Yes. Very good. Yes. Exactly right. So it's a really important concept. Yeah. It's really valuable when it comes to figuring out, you know, kind of the ground bounce noise that you're going to get when you have changing currents through inductance. Yeah. But it's because it's taught so poorly, people don't walk away with a good understanding of what is inductance. Yeah, I know it's L. I know it's, you know, omega L is the impedance, but what's the inductance?

**Chris Gammell:** Right. And I think that the, I mean, that physical model really helps too, because, I mean, humans are such good pattern matchers. Yeah. When you start to look at a layout, you're like, oh, that's a loop, right? And you see that, and you're like, oh, okay, well, now that's going to cause some kind of inductive effect to actually at least go review it. You know, just kind of getting those, I mean, combining rule of thumb and also, you know, just having these mental models is really, really important. So that's good.

**Eric Bogutin:** Right, right. And that's because so much of engineering is that intuitive, creative process, and you really leverage your intuition and those mental models when you design product. And that's where you create it. You don't create things with a 3D field solver. You can verify performance with a 3D field solver to know is it going to work or not. But where it comes from initially, that's where engineering, intuition, and creativity come in.

**Dave Jones:** Oh, I was going to say, in a lot of my videos, when I'm talking about, like, you know, I'm doing a teardown of PCB, I'm always talking about loop area. And that's, to me, that's one of the fundamental rules of thumb that I try to get across for signal integrity is, like, minimize your loop area. Have your return path as small as physically possible. Well, the bigger it is, the bigger your loop area, the more problems you're going to have with signal integrity. Am I – is that a decent rule of thumb to – or is it opening a big can of worms?

**Eric Bogutin:** No, no. No, it's a very important rule of thumb. You just have to keep it in context of when is that important. Right. When you care about the lumped inductance, then you're absolutely right. Smaller loop area means the signal and return are closer together, lower loop inductance.

**Dave Jones:** I'm generally talking in terms of, like, you know, EMC, like, you know, radio, you know, things like that.

**Eric Bogutin:** Right, right.

**Dave Jones:** Yeah.

**Eric Bogutin:** And now the difficulty of using that rule of thumb is identifying where are the return paths. Of course, yeah. And when you have surface traces, it's not the return current between two signal lines. It's the return between the signal and its return in the plane underneath. That's right, yes. And that's what you care about. And that's where the controlled impedance comes from.

**Dave Jones:** And that's why you don't have split ground planes.

**Eric Bogutin:** Yes, very good.

**Dave Jones:** Yes.

**Eric Bogutin:** You're exactly, because then the return current has to make a bigger loop. Go around, yeah, make a bigger loop. And you get more voltage generated in that path. And it doesn't always want to go around.

**Chris Gammell:** Sometimes it goes through the air. Yeah, yeah. So you're teaching all this stuff. I mean, so you're teaching this in classrooms. You've taught this in the past in person. Let's hear a little bit about the online stuff, because obviously that's close to my heart. Dave teaches online too. Yeah, yeah.

**Eric Bogutin:** Well, so we realized a long time ago there was going to be this revolution in online training. And there's no substitute for being there in your face and participating and playing along. It's kind of like I say, it's the difference between listening to a CD and going to a live concert. Right. And yeah, you listen to the CD, that's great. But you bought that CD and you listen all the time, but you still want to pay the extra to go to that live concert. Yeah. And I look at the live classes that I've done. You know, our corporate attorney before I got acquired was an attorney who represented some of the Cirque du Soleil performers. And he was the one that told me that what I do is I'm a performer at heart. And people come to my classes, yeah, they want to get the knowledge, but I'm a performer.

**Dave Jones:** Yeah.

**Eric Bogutin:** And it's the show that they get with the classes. But I realized 10, 15 years ago that travel is going to be limited and I don't want to travel all that much. And I realized, you know, we've got to start leveraging the internet to distribute the information. And so we've experimented lots of ways. And in the last couple of years, we decided to take all the live classes that I've done. We recorded them. We parsed them up into little chunks of 15, 20 minutes and put them online. And that's what we call the Signal Integrity Academy is all of the recorded live classes in units of lessons, small lessons that are all individually accessible. And we charge a subscription fee. So a whole company can get access for a single subscription fee. Everybody in the company can view all the lessons for a year or an individual can buy an individual subscription and view all the lessons. And as we add more stuff to more content, I'm always recording new lessons and posting and everybody gets access to those as well. And so that's the new business that we've got. This is the Telen and LaCroix Signal Integrity Academy. And we've had it up and working for one year now. We're at the almost exact one-year anniversary. And it's been growing very, very successfully. So we're really pleased with it. But it's a tough business model because we compete with free. There's so much stuff online that –

**Chris Gammell:** We're talking to free right now. The free has an Australian accent here.

**Speaker ?:** Right.

**Eric Bogutin:** But there are a lot of webinars that are out there with similar topics to what the course I do. The difference is when you listen to those – it's kind of like I used to love buying books. I go to the bookstore and I look at the titles or I look at the pictures on the cover and that's what would sell me. And I'd buy it and I'd come home and I start reading it. And after the first two pages, I go, oh my gosh, this is terrible. And then I toss it and I get sold by the title. And the same way, I see these webinars with these great titles. Wow, I want to watch that. And I go listen to them and after five minutes, I realize, you know, this is a feature list of this product here. I don't really care. It's not telling me anything new that – how I'm going to solve this problem. And that's the distinction of what we do on the academy is it is real high quality principles and how to get you to solving a problem quicker. How to get you to the right answer faster is really what we teach, design methodology, the principles, solid foundation, a lot of examples. How to use tools to help you get to an answer faster. One of the things we do that is unique is we focus on S parameters. And it's this incredibly valuable kind of formalism, a technique that's used to describe interconnects that, again, it's one of those poorly described out there. It's shrouded in a lot of math. We strip the math to really give intuition principles about it. So we focus on S parameters, real high speed design as well as the basic foundations. And so what we differentiate our stuff with is really the quality of the content and the perspective on helping you get up from the ground zero to build really good, strong physical engineering intuition. As well as use the tools so you can solve the big problems quickly. Yeah.

**Chris Gammell:** Got it. I always like the rule online. If you're not paying for the product, you're probably the product. I mean, that's not always negative. It's not like Facebook's reaching into your data set and stealing a wallet. But it's also just advertising stuff like that. So yeah, that's kind of the difference.

**Eric Bogutin:** Can I plug my website? Sure. Yeah, of course. So it's under two names. So SignalIntegrityAcademy.com or BeTheSignal.com.

**Dave Jones:** I like BeTheSignal better. Yeah, me too.

**Eric Bogutin:** Yeah. So that's the easy one to remember. That's the website we've had for 15 years. And we just turned it into the Signal Integrity Academy. So we've got some lessons that are for free. So you look through the classes and you look at the lessons. There's a little I next to it. That's for free. And anybody can view it. You can – we've implemented a lot of simulation tools, some free ones, and all the files and the circuits that you can download for the lessons. So there's just a lot of stuff up there. The class that I do at CU, the graduate class, that whole course is posted on the website as well. And the labs that I've done for that, we use Polar, we use Hyperlinks, we use ADS, HFSS, Symbior. A lot of those tools, the example files for those tools, I've posted on the course as well.

**Dave Jones:** Is there any free content out there or is it all – Yeah.

**Eric Bogutin:** So in each course, there's a little I.

**Dave Jones:** Well, some people might want to sample your work before they – Yeah, exactly.

**Eric Bogutin:** Exactly. And so we have a little – if there's an I next to the lesson, that means it's for free and anybody can click on it and view the lesson, the video, and download the stuff that's associated with it.

**Chris Gammell:** Very cool.

**Eric Bogutin:** Fantastic. So you get a little teaser for it by going to the – look at the free ones.

**Dave Jones:** Now, we were talking before the show about all this sort of online content and online degrees and things like that. What's your take on where all this is going?

**Eric Bogutin:** Yeah. Boy, there are so many MOOCs that are out there that it is an incredible opportunity for all of us users out there because there's so much we can take advantage of. And it's this really perplexing dichotomy in the internet that there are content creators and there are content viewers. And for content viewers, there is so much great stuff out there that's free that you can get a dozen college educations for free just by viewing stuff online. And it begs the question, OK, all these great content creators that are posting their stuff up there, wow, thank you so much for doing that. But how are they making money? And at some point – it's the old story of the internet bubble. So Chris, you're going to have to ask your folks about that because that was before your time. But back in the early days of the internet, there were all these startups that were going to do all these – I was there. You could do all these – I'm not that young. Come on. So there were all these startups that were coming out with, oh, you can post your blog and you can post these pictures and you could do all these things. It was great. But how are you going to make money at it? And so eventually, a lot of VCs put a lot of money in. But eventually, they didn't have a business model to make money and they don't exist anymore. And so it's a question of how are the MOOCs going to make money? And there are a couple of ways. I mean for what we do in the academy, we're basically a MOOC, but we are in a very, very specialized field that there just isn't anything comparable for free out there. But when you look at a college – EDX or Coursera or Udemy or Udacity or some of these other MOOCs that are conglomerates, consolidators for all these university classes, they're not charging for it. And so how are they going to make money? And I think that there are probably two –

**Speaker ?:** Well, some of them are now.

**Chris Gammell:** Some of them are starting to.

**Eric Bogutin:** Some of them are, but a tiny amount. Yes, right. And I think there are going to be two business models that emerge. One is like ASU and Georgia Tech. They're going to charge for an online master's degree with the name of ASU or the name of Georgia Tech. That will be equivalent to if you're there. And they'll charge $10,000, $20,000 for a two- or three-year master's degree. So that will be another way of making money. They'll get more students that way and they'll have some kind of grading and kind of thing.

**Chris Gammell:** More hands-off for them.

**Eric Bogutin:** And I think the other – yeah, exactly. Exactly. Exactly. And I think the other vehicle is going to be when you have 100,000 students that are signing up for an online class and you're tracking all of them. And Stanford has done a lot of the statistics on this and they'll do a computer science class. Literally, 100,000 people sign up for it initially. And by the time they finish, there are 5,000 that have finished it. That's still 5,000. I know. It's incredible. It's incredible. And these people now, okay, they may not be the A students, but they have some of the expertise. And now the course – or EDX that does Stanford and MIT and Harvard, they've got the list of the names of these 5,000 students. And they're going to track what other courses have they taken. And if you're a recruiter or if you're Google or if you're Facebook and you want to find a computer science guy relatively cheap that has experience in these five kinds of classes, you pay EDX to give you the names of their top 100 students that have taken these classes. And EDX is basically – gets a fee for offering the names and Google or Facebook, hey, they get the qualified engineers.

**Dave Jones:** Isn't that the model that the LinkedIn website works? That the LinkedIn website works? Can't big companies pay money to LinkedIn to find people that have got certain talents and things like that?

**Eric Bogutin:** It's self-promoting. You put in your resume. I've taken these classes.

**Chris Gammell:** Although, interestingly, they just bought lynda.com, who is a course provider. So that – LinkedIn did? Yeah. That's their future model. Wow. Wow. Very good. Very good.

**Eric Bogutin:** I didn't know that. Yeah. Wow.

**Chris Gammell:** It just happened like a couple weeks ago. I mean, that's kind of more general because that's like, well, I want to take a photography class or a Photoshop class. Right. But I could very easily see them moving into this skills training kind of thing. Right. Yeah.

**Eric Bogutin:** Yeah. And then they have an idea of who's taking them. Now, for lynda, it's a little different because companies pay a fee to lynda for access to the courses. So I think there would be a conflict of interest if lynda sold names from companies of engineers or folks that have taken a certain number of classes. Yeah. But for EDX or Coursera, I think that's perfectly appropriate. They track the – you have to register. You have an account if you take one of these classes. And if you take one for credit and for a grade, you go through the tests, they know who the Sharp Kids are. And worldwide, Thomas Friedman used to say, hey, if you're looking for that one in a million student in China, there are a thousand of them. Yeah, that's right. Yeah, yeah, yeah. That's right. Worldwide, there are 6,000 of those one in a million students. And that's the huge benefit of all the MOOCs is it is worldwide. And it has given – I mean I think it is such a revolutionary kind of level the playing field tool that you can have someone that has very little access to any good mentors or classes. And they can go – if they have access to the internet, they can take an MIT course just like someone sitting in class. So you can look over their shoulder and take the same courses. So it's fantastic opportunities that – and we're seeing those kids that have that drive, that want to overcome their limitations, their barriers, and haven't had opportunities. Those kids that are willing to put in the work, they can now access it and overcome those barriers. That's it.

**Chris Gammell:** So I'm actually interested in this stuff because – and I might challenge you a little bit on this just because all the – like so like how do you – I don't know how you do it in your course, but how do you do the testing stuff? That's what I always wonder about this. Like you can watch with the students going through the material and stuff like that, but there's still no tangible way to say it's person A, not person B taking the test, and person A is actually watching this, and they actually have retained anything. So like I don't know about your course and also – especially for these MOOCs, this is what I really think about because like how do you know that it's actually stick – it sticks. It's actually done.

**Eric Bogutin:** And so for mine, I don't do testing. The certification is you've listened to these videos, and I don't do a test afterwards. I'm working with some other folks on developing a certification exam kind of thing like IPC does – IPC Designer Council does a certification. So we're looking at something like that down in the future, but I don't do that now. For the MOOCs, there is some testing that's done, but there's always the question of is this person that has signed in with this account, is that the person that took the exam? And I think what ASU does and I think Georgia Tech does, I think they have to require some on-site presence at least at some point to take some of the exams or they do – they could do exams remotely. But I agree. I think that is going to be one of the significant limitations. And it's all about the certification. If you're getting it for free, I don't know how valuable or how much access you have to certification, but if you pay for it, what you're getting isn't the course, but you're getting that certificate at the end. Yes, that's right. And that's the value that you can take your employer. But I'm finding from – I've got a lot of graduate students that are out there looking for jobs, and I talk to many companies that are looking to hire them. And what I am hearing is that when a hiring company, a hiring manager looks at a resume, looking at what courses have they taken, either at school or at a MOOC, they're equally important. And so if you can say you took this electromagnetics course from EDX, from MIT, or from ITT, and you have that on your resume, it is as good as an eye-catcher to kind of get your foot in the door for that interview as I took this electromagnetics class sitting there in the classroom at CU or someplace else. Got it. So I think it's not going to be what gets you hired, but it's what gets your –

**Dave Jones:** Get you in the front door.

**Eric Bogutin:** It gets you in the front door for the interview. Yeah. It is almost as valuable having that on your resume.

**Dave Jones:** Are we going to reach a point where – because we see this a lot of HR departments do this these days. If you're not on LinkedIn, especially in the U.S., I've heard – it's not here in Australia, but in the U.S. – if you're not on LinkedIn and they can't research you, that's most of their job. And they're just going to throw you in the trash bin because you're not on LinkedIn. So who are you? You're a nobody, right? Is that going to be – do we reach a point where, well, you're – you know, I want to look for – you're a HR department. You're given the task of hiring. I need someone who's got PCB design, signal integrity. And if you're not registered as having done these courses online, well, you're just not going to get picked. Oh, you've got that piece of paper? What? How can we prove that you – you know? Yeah.

**Eric Bogutin:** I have to say I'm a bit of a Luddite when it comes to LinkedIn and Facebook. And so I don't know offhand. In fact, I don't really know how to use LinkedIn very well myself. I always get invitations that I always accept and I have, I don't know, a thousand connections there, but I don't really know how to use it.

**Speaker ?:** Yeah, yeah.

**Eric Bogutin:** That's why you did it for me. That's right. Shoot. You know, okay. So are you guys on Twitter? Yes. Oh, definitely. Yeah, we're huge on Twitter. Yep. Okay. Well, okay. So our marketing communications manager, Hillary, when I first started with LaCroix, she was the one that was pushing me to get on Twitter. You have to be on Twitter. You have to be on Twitter. Yeah, yeah. And so I said, okay, okay, I get on Twitter. And I got my Twitter account. My handle is at BeTheSignal. And I started getting a few people subscribing. Is it what it's called? Subscribing? Or following. Following. Yeah. And so I would go around to all the classes, all the lectures that I do. When I go to ZineCon, I do a lecture there for a group. I'll get 200, 300 people in the room. And I'll ask them, how many are you on Twitter? And I'd get out of 200. I get two people maybe at most. Really? Well, look at the audience. Yeah. And so engineers, I find in at least the high-speed, high-end enterprise kind of groups, they're not on Twitter. And so I look at my followers and it's all the press, the media guys, and it's people that I know that are there. And so there's none of my customers, none of my students, none of the engineers that I talk to are on Twitter. Wow. And so I just don't do much with that. And LinkedIn, I have to confess, I don't know how to use that very effectively. So I'm not a good person to ask about the role of LinkedIn for hiring.

**Dave Jones:** I just find this phenomenal because I've got like 20,000 followers on Twitter or something, and they're almost all technical. Well, they're mostly electronics people.

**Eric Bogutin:** But you have a video blog that you're number one in the video blogs, and everybody wants to know, hey, when's your next blog coming out, and what do you have to say?

**Dave Jones:** Right.

**Eric Bogutin:** What bullshit do I have to say today? Yeah, right. Or what cool demo are you going to show off? Pull that back a little bit there. So you have an audience, a live online audience that's following. That's good to know. You have 20,000 followers, huh?

**Dave Jones:** I have 20,000 followers on Twitter.

**Chris Gammell:** Yeah, but look at the ratios, though, too, Dave. I mean, there's a spread online.

**Dave Jones:** I've got a quarter of a million followers on YouTube. I've got a quarter of a million subscribers, yeah.

**Eric Bogutin:** Wow. That is great.

**Dave Jones:** I've only got 20,000 on Twitter and 6,000 on Facebook or something. My Facebook, I don't use Facebook. But yeah, I do have a page where videos get posted. I've got like only, yeah.

**Eric Bogutin:** And you have a very broad audience. I mean, guys that are hobbyists that are playing with resistors in their garage want to watch what you're doing. And guys that are doing high-end RF designs or 10 gigabit per second systems are going to want to watch what you're doing. So you appeal to this huge, wide audience base.

**Dave Jones:** As you said before, you hit the nail on the head about the – or was it your wife? Did or something about you're a performer. Yeah. You're a performer. And that's essentially what I have become. Yeah. Right. I'm no longer an engineer. I'm an educator and performer, you know?

**Eric Bogutin:** Yeah. And entertainer. And it's harder though for you online because you don't have a live audience in front of you.

**Dave Jones:** No, that's right.

**Eric Bogutin:** And there's a big difference between having a live audience in front of you and doing it in front of your computer with a recording. Right. And that's what I – I stopped doing live classes because I didn't want to travel so much and I was doing this class at CU and I put everything online. But especially with the semester ending at CU, I realized that I kind of miss having the audience. Yeah. And so I've started doing a few live classes, you know, partly to introduce some new content and partly because as long as I can keep the travel to a minimum, you know, I kind of enjoy that interaction with the live group. And in fact, next week – the end of this week, I'm flying off to Copenhagen to do a two-day S-parameter workshop over there. Wow. Cool. And, you know, not having to travel much is a good thing. And so many people that, you know, want to hear a lot of this stuff, you know, they're not going to travel around either. They can't get travel budget. And so having an online is a really good balance. Totally. Yeah.

**Chris Gammell:** Yeah, that's good. It's like you're like the stand-up comedians that do – they test in small markets and then they record their special. That's right. That's what you're doing, right?

**Eric Bogutin:** Right. And you go on tour and, you know, even if you've got the CD, you still want to go hear the live performance if your department will pay for the travel.

**Chris Gammell:** Right. Eric, if you could work in some, like, stand-up jokes, like, into your – Right.

**Dave Jones:** What if there's two electrons who walked into a bar? Yeah, right, right.

**Eric Bogutin:** Well, you know, the one about the electron and the neutron going to the bar and the bartender, you know, the electron says, I'll have a beer. And the bartender says, OK, that's $1.50. And the neutron says, I'll have a beer. And the bartender says, hey, it's free. And the electron says, hey, I had to pay. How come you're not paying him? And he says, no charge for the neutron. That's a physics joke. Anyway, I do try to have – you know, so when I go to Asia in particular, sometimes I'll do a sequential translator, like in Japan or in China, and I'll always try to do a couple of jokes just to see who in the audience understands English.

**Dave Jones:** All right. That's good.

**Eric Bogutin:** Yeah, yeah.

**Dave Jones:** Oh, love it. So where can people find – well, we've already covered that. Where can people find your stuff? BeTheSignal.com is the best place.

**Eric Bogutin:** Yep, it's the best place.

**Dave Jones:** And what's your book? How many books? Have you only got the one book?

**Eric Bogutin:** Well, I've got about six books out. Some of them are hard to find, and some are about packaging technologies. All right. Yeah.

**Dave Jones:** Packaging technology there is an interesting field.

**Eric Bogutin:** Yeah, and I have a lot – and they're online as well. I mean, I did a book with my buddy, Mike Reso, who's at Keysight. It was Signal Integrity Characterization Techniques, and that's as PDF, and you can download that from our website. Oh, awesome. So it's free. It's a pretty big book. Fantastic. Completely free.

**Dave Jones:** Why did you originally intend to release it as free?

**Eric Bogutin:** So we did it – so Mike and I have done a gazillion different DesignCon talks, and for a while I wrote a bunch of app notes for Agilent folks years ago, and so we combined all my app notes and all the talks into one book, and we did it with the IEC. And the IEC was the organization that used to run DesignCon before UBM, and they published the book. And about three years ago, IEC said, hey, we're going to be out of the book publishing business. You can have the copyright back. Oh, sweet. So Mike, through Keysight, gives it away for free, and me, through the Signal Integrity Academy, I give it away for free. So it's a pretty good deal. Yeah. Awesome. And so the other textbook – so the popular one that I wrote is from Prentice Hall. It's called Signal and Power Integrity Simplified. And it's – I would say just based on the comments that I get and looking at the reviews on Amazon, it's probably the number one Signal Integrity book these days.

**Chris Gammell:** Fantastic.

**Eric Bogutin:** And it really helps bring you up from the ground zero to understand these physical principles. It minimizes the math, but really gives you a feel for – there's some math in there, some examples of rules of thumb, approximation, simulation tools. So it goes from soup to nuts on getting you up to speed understanding Signal Integrity. Got it. And then I've got another one that I'm just finishing.

**Dave Jones:** Oh, and there's a free sample chapter on that available. Oh, there you go. I've just – yeah.

**Eric Bogutin:** Yeah.

**Dave Jones:** Some website. We'll post in the link anyway.

**Eric Bogutin:** Oh, great. Yeah. And you can look at some of the reviews. I mean, I've got some great reviews. It always warms my heart that someone else read it other than my relatives, and they liked it. So I always get notes from fans out there who've read it and have helped them a lot.

**Chris Gammell:** That's a lot of books. And you said you also wrote for EDN as well. I mean – Yeah.

**Eric Bogutin:** So I –

**Chris Gammell:** We'll link all that stuff.

**Eric Bogutin:** Okay. Yeah. I write – I've written a bunch of articles for them, and I write this rules of thumb column that – I owe them a couple more coming up here. I need to get my act together and get some work done. Yeah. It's a whole series of rules of thumb that are used in Signal Integrity. And they have – I think they have one landing page where you can link all the rules of thumb to. Okay.

**Chris Gammell:** Okay. That's good. Correct. That's good. Cool. Well, I think there's a lot of people that will probably be interested in this after hearing this stuff. I mean, these – Cool. Oh, definitely. Even just the rules you gave on here was really, really useful. So I'm excited about that.

**Dave Jones:** Fantastic. Well, thank you very much for joining us, Eric. It's been awesome.

**Eric Bogutin:** Hey, it's really been my pleasure. I love talking about this kind of stuff, and it's been a pleasure chatting with you guys. And hearing about your stories as well.

**Chris Gammell:** Cool. Well, we'll definitely check out bethesignal.com, and everybody else out there should do that too. So thanks again for being on the show.

**Eric Bogutin:** Hey, thank you.

**Dave Jones:** Thanks, Mike. Catch you next time.

**Eric Bogutin:** Okay. Bye-bye. Bye-bye. Bye-bye.

**Speaker ?:** Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye. Bye-bye.
