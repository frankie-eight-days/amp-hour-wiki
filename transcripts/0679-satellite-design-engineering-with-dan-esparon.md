---
episode: 679
title: Satellite Design Engineering with Dan Esparon
url: https://theamphour.com/679-satellite-design-engineering-with-dan-esparon/
---

**Dave Jones:** This is the Amp Hour podcast, recorded October 11th, 2024, episode number 679, Satellite Design Engineering with Dan Esparon from Innovore Technologies. Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Dan Esparon:** And I'm Daniel Esparonon, Electrical Engineering Manager at Innovore Technologies.

**Dave Jones:** Hey Dan, thanks for joining us.

**Dan Esparon:** Thanks for having me on.

**Dave Jones:** No worries. I like space stuff. Even though I don't know a huge amount about it, this should be interesting. What's your background and how did you get into space engineering, I guess? Is space engineering the correct term? What would you call yourself?

**Dan Esparon:** Yeah, I call myself an electronics engineer. Yeah, of course. For space systems. Yeah, it's sort of a unique challenge. But at the end of the day, what we're doing is largely similar to what everyone in better systems do, just with different challenges, I guess. So yeah, my background, I studied at the University of Queensland, did an electrical engineering degree and physics degree, graduated in 2018. And was looking for a graduate job. Right. I had an undergraduate job when I finished, so I was kind of still doing that after I went to my graduation ceremony. So I wasn't super rushed and saw that there was all this cool space stuff happening in South Australia.

**Dave Jones:** Ah, interesting.

**Dan Esparon:** I applied to a small company that looked interesting and got an interview and joined as an embedded software engineer, actually, to start with. Great.

**Dave Jones:** And now you're the head of the engineering, the EE team?

**Dan Esparon:** Yeah. So I started as an embedded software engineer, spent half my time doing embedded spacecraft software, and then half my time out at Defense Science Technology Group on contract doing electronic warfare modeling and simulations. So that's kind of something that people don't really, especially being from Queensland and not being exposed to defense that much. It's this whole science technology group down in Adelaide that is massive and doing lots of really cool work. But you kind of don't do it all about.

**Dave Jones:** I used to be involved in that way back in the day. Yep. Yep. I've been to Adelaide before because I used to work at defense companies. So, yep.

**Dan Esparon:** Spent a bit of time doing that, but always had sort of a background in electrical and electronics. So slowly moved across to the electrical team at Inovor and then finished up the contract and was then full time doing electronics designs for them. So then made my way through the team. And now I'm running a team of about 10 electrical engineers. And we do everything from design, manufacture, test, integrate spacecraft electronics.

**Dave Jones:** And you do that all in-house in South Australia?

**Dan Esparon:** Yeah. So all of our designs done in South Australia, all of our, because of it, because it's, because our space systems are listed as defense dual use, all of our manufacturing is done in Australia. So we can't actually send any of our bills, materials or circuit assemblies overseas without export control.

**Dave Jones:** Interesting. What about bare PCB design?

**Dan Esparon:** Bare boards are fine. Yeah. So we get our bare boards from the US and actually from New South Wales as well. There's a company in New South Wales that make PCBs. And that's mostly for the quality side of things. Yes, of course. So they do very high quality circuit boards.

**Dave Jones:** Oh, that's not Lintec, is it?

**Dan Esparon:** Yeah, Lintec. So that's... Yeah, of course.

**Dave Jones:** They do all the high... Very expensive. If you have to ask the price for one of their prototype boards, you probably can't afford it. So...

**Dan Esparon:** In space terms, they're actually quite cheap. They're one of our cheapest suppliers. Oh, okay. Right. There you go. We have solar panels that the price of the boards on our solar panels will blow you away because they've got a custom stack up and a very special coverlay material on them.

**Dave Jones:** Oh, so hang on. Well, let's jump straight into the solar panels, shall we? This is going to be a completely random show. Yeah. So the solar panels have boards in them? How does that work? Yeah.

**Dan Esparon:** So we make all our own solar panels. We buy solar cells from the US, specific space solar cells that come in 27 square centimetre little cells.

**Dave Jones:** Yep.

**Dan Esparon:** And then we have a printer circuit board backing that we assemble those cells onto.

**Dave Jones:** Why is that?

**Dan Esparon:** It's a pretty standard way of designing CubeSat solar panels. The PCB has to be particularly specific because the solar panels will cycle from about minus 70 degrees Celsius all the way up to about plus 70 degrees Celsius in the sun and do that every 90 minutes. So it's quite a thermal load on those panels. And they're also exposed directly to the sun. So you end up getting quite harsh radiation on those.

**Dave Jones:** Got it. So what's the difference between a regular amorphous or silicon solar cell and a space rated one?

**Dan Esparon:** Yeah. So they're triple junction. So they're over 30% efficient, like spectrally efficient, that is, which is quite a bit higher than your standard silicon. So they're, I can't remember off the top of my head the exact stack up of them. But they've essentially got three junctions inside them and each one is responsive in a different band. So you pick up more of the energy out of the spectrum of light.

**Dave Jones:** Nice. Okay. And they're substantially more expensive than regular solar panels, I take it?

**Dan Esparon:** Oh, yes. Yes. Substantially more expensive.

**Dave Jones:** Well, I was just going to say, like, in terms of bomb cost, are the, like, solar panels, like, an expensive part of your build?

**Dan Esparon:** Yeah, they would probably be the most expensive single item, I'd say. Oh, really? Wow. That we manufacture, at least. Right. When we buy components from other suppliers, they're generally more expensive. But in terms of raw cost of materials, they're definitely the most expensive.

**Dave Jones:** Oh, wow. Okay. That's interesting. And I noticed that you've got, we'll talk about your payload and your CubeSat bus and everything like that. But you've got quite a few different satellites here. And I'm having a look at them and we'll provide links down below. But they all look very similar in terms of, you've got, like, two, like, it's like a cube. Well, it's not a cube. It's like a suitcase side, you know, shaped thing with two fold-out solar panels. But you've also got solar panels on the, like, under the solar panel arrays. Is this because of the orientation? It could be in any orientation and you'd still need power? Or is that the reason that it's totally covered in solar panels?

**Dan Esparon:** Yeah. So there's kind of two phases. There's the initial, like, launch and dispense of the spacecraft when we're commissioning it. And it's kind of just randomly tumbling around in space. It hasn't got active pointing control at that point. Right. That's something that we commission and build up that capability to make sure all our sensors and control systems are working. So in that phase, we kind of need solar panels everywhere to just, in case we tumble into a weird attitude, we need to be able to collect power. Got it. Then we have our deployable panels. And what that does, it gives us, you know, a 700 mil by 200 mil surface area on top of the spacecraft that we can point at the sun to pick up our peak power off our, to charge our batteries and to run our payloads. But then also we have solar panels underneath those because in some concepts of operations, we have different faces pointing to ground or the sun or we've got a payload that we're pointing out to the moon or different things like that. So those are generally spaced so that we can collect power when we're doing those operations.

**Dave Jones:** Right. So that provides flexibility based on the mission that you've got inside the satellite, right? Yeah, that's right. Where it needs to point and things like that. What sort of battery tech do you use in there? Andy, I assume you fully charge it before you launch it just in case. So you've got some initial power.

**Dan Esparon:** We do fully charge them before we launch. Yes. They're just standard.

**Dave Jones:** Well, it sounds like a dumb question, but you know, I mean, I don't know.

**Dan Esparon:** We probably need to cut this out, but.

**Dave Jones:** Right. No, no worries. We'll take that out. So what type of batteries does it use?

**Dan Esparon:** So they use lithium ion cells, commercial available cells. That's probably all I can say about that. And we buy the cells from a company in Sydney and then we assemble them onto battery module cards with all the cell management and protection and charge, discharge regulators and everything.

**Dave Jones:** Right. So you actually design your own BMS and everything in-house?

**Dan Esparon:** Correct. Yeah. Everything's in-house.

**Dave Jones:** Are there advantages to that rather than just like I thought you'd be able to buy like a space battery solution or something?

**Dan Esparon:** You can. Again, you end up spending a lot of time integrating that with your flight computer and the rest of the system. And there's sort of trade-offs that a lot of people make. So, you know, there are companies that make subsystems, but the decision and the background of Intervore is that the CEO and founder really wanted to, you know, design a fully integrated space solution. Got it. Four cubesats and that meant building everything. So we, you know, we build everything from, we take cells, we put them onto PCBs, we build solar panels, solar regulators, maximum PowerPoint trackers, flight computers, UHF radios, the whole ADCS system, which consists of star trackers, reaction wheels, magnetalkers, sensors, everything is all designed in-house.

**Dave Jones:** Wow. That is great.

**Dan Esparon:** Yeah.

**Dave Jones:** So you provide, so your company basically provides a physical satellite solution for cubesats. Is that correct?

**Dan Esparon:** Yeah, correct. So we, we also do the integration as well. So we will take someone's payload and then build a structure for that payload, install our, our bus, which is what we call all the core components. We generally also define design payload interface modules to provide power and comms to the payload. And then we assemble it in our clean room facilities. So we've got clean rooms in Adelaide in our office, integrate it, test it, go through the full spacecraft test campaign, environmental test campaign, and then ship it and to our launch service provider. And then we operate it as well. So we've got a full mission operations team and mission operation tool as well.

**Dave Jones:** Oh, great. How many employees have you guys got? Must be a big operation.

**Dan Esparon:** We've got 51 people.

**Dave Jones:** Oh, is that all? Okay. That's all. I thought it was more than that.

**Dan Esparon:** Yeah, no, it's a pretty, it's a pretty small team and a whole bunch of those, we've kind of got two arms. There's two aspects of the business. There's the space side and then there's also some defense consulting as well. So it's not even 50 people working on the space side.

**Dave Jones:** Are there any, I assume there's competitors out there that have a similar sort of like bus, CubeSat bus system. Are there?

**Dan Esparon:** Yeah. So if you look in, look at Europe and the US, there's a lot of competitors there. There's not really any in Australia. There's a few companies doing space systems in Australia where they're either designing large parts of it for bespoke applications. So there's a company in Canberra who are doing air traffic communications from space and they're building their home bus. There's a company in South Australia who's doing IOT spacecraft. And I'm sure there's some others. Oh, there's another company just up the road who are doing smallsats. So, you know, 200 odd kilo space tugs. But then if you look for, you know, the people selling the buses, it's really people like GOMSpace and Tyvac who are in Europe and the US. And they do essentially the same thing as us. They build all the components. They also sell their components as subsystems to universities to build their platforms. But they also do the integration side as well.

**Dave Jones:** So if a university or the military or some other government organisation wants to put a satellite out there, they don't want to deal with the details of actually designing the satellite, but they want to design just the actual payload, the actual CubeSat payload. They would come to you and go, right, can you integrate this CubeSat with a satellite, please? Is that the...

**Dan Esparon:** Yeah, that's right. So they'll generally have an... Either they'll have a concept of why they need a space system and we can provide the whole payload bus everything, or they'll come and say, we want to launch this payload. And generally it's the, we come with a payload and can you please put it on your bus and launch it for us that we've done so far.

**Dave Jones:** Right. So what is the CubeSat bus? What does it involve? Is it like a physical connector thing with a bunch of protocols and a power budget and et cetera, et cetera? Can you explain how a CubeSat bus works? Because that's one of your company's big things is that you have developed this bus system.

**Dan Esparon:** Yeah. So a bus is a term used in space to define all the... It's generally, it covers everything from CubeSats to, you know, big geos. You know, Lockheed Martin have got, you know, geo buses that they will sell to defence and stuff like that. So the bus normally comprises of all the stuff that makes the spacecraft operate in space, but isn't the payload. So it's things like your command and control systems, all the protocols associated with that, your radios associated with that, your batteries, your solar panels, all the attitude determination control system, which does all your pointing and your attitude determination and location tracking. And then the payload sort of power management side is generally on the bus as well. And then obviously structures and solar panels and the like as well, and antennas.

**Dave Jones:** So in terms of power budget, what are we looking at here? What can you... What can a small... Like how can you give us a physical dimension of your standard satellite arrangement? How big are we talking about?

**Dan Esparon:** So depending on the payload power requirements, we'll generally take up, you know, 100 mil by 100 mil is what our sort of form factor is. And then it expands lengthways to support more battery modules. So, you know, you can take... The way the bus is designed, the way we've designed our bus is that you can plug in extra battery module cards. So each battery module is 30 or 40 watt hours and you plug in more and more and more batteries as you require them to store more power. And then at the same time, you have to put more and more solar regulator cards in to get power off the cells. So that expands up to, I think, Canini, which was the South Australian government spacecraft with a couple of payloads that had... That was about two units worth of bus. So 200 mil by 100 mil by 200 mil long worth of bus components, bus specific components. And then the rest is all payload volume.

**Dave Jones:** How do you keep everything warm up there? Have you got like internal heaters and stuff? How, like, especially for the battery, I would imagine?

**Dan Esparon:** Yep. So yeah, you bang on there. So the battery has got it, have got heaters. There's heaters on the batteries, but that's about it. Everything else is pretty thermally stable. It's actually surprisingly warm and quite stable once it's in orbit because you sort of, you get a little bit of heating as you go through the sun and then a little bit of cooling, but it sort of stabilizes within half a dozen orbits have been on space, in space.

**Dave Jones:** Ah, interesting. Yeah, because I was going to ask, like, how do you actually control the temperature? How do you regulate the temperature in there? And like, how much power does that take out of your power budget, for example?

**Dan Esparon:** Yeah, it's a few watts to keep the batteries warm. The bigger concern really is getting rid of heat off payloads.

**Dave Jones:** I was going to ask about that. Yeah. How do you get rid of heat?

**Dan Esparon:** Yeah. So. Because there's no air. That's right. So a lot of thermal design, thermal straps everywhere to go from payloads to structure to heat sinks on the outside of the spacecraft.

**Dave Jones:** By thermal straps, you mean thermally conductive physical copper straps or something?

**Dan Esparon:** Yeah. So yeah, thick copper. Normally they're copper braid, I think they are, which connects the payload sort of heat sink to the structure somewhere. And there's a whole bunch of thermal design that goes into the critical design phase that informs where they should go and what the thermal properties of the spacecraft will be. And then at the end of the assembly integration phase, we go and spend two weeks doing environmental testing, which involves thermal vacuum testing of the whole system. So we cycle it up and down and check that our thermal balance matches what our thermal models say it should be.

**Dave Jones:** Right. And you've got a thermal vacuum testing chamber in house. Is that right?

**Dan Esparon:** So we have a small one in house. We've got a small one that we use for qualifying our sort of individual board designs. But then for a full spacecraft, we actually go to Canberra. So we fly up to Canberra with the spacecraft. For Canini in December, I had a six unit CubeSat on the seat next to me on the plane as I flew to Canberra with it.

**Dave Jones:** Nice. I assume you had to buy an extra seat. You bought an extra seat for your satellite.

**Dan Esparon:** Yeah. Extra seat and some paperwork to say, please don't open this at airport security. We promise it's just a spacecraft.

**Dave Jones:** Do they actually believe that? Or is it like some sort of official government paperwork they can't actually question? Or, you know, you can't get some dumb ass security person going, no, I don't believe it. And they start ripping it open. You know, how does that?

**Dan Esparon:** It is actually official. So we have to actually apply through whoever handles airport security. And we get an official piece of paper that we can show security. It says, you know, this is what this is. We've got authority to bring it through. Please don't open it. If you do need to open it, you need to provide us with a certified clean room to inspect it in. And that kind of shuts it up.

**Dave Jones:** Yes. So you're physically transporting this satellite thing on the seat next to you in the plane. Is it like in a hermetically sealed container or what?

**Dan Esparon:** It's not hermetically sealed. It's a double bag. So it gets double bagged in our clean room in sealed bags. Oh, okay. In ESD and clean bags. And then put into a Pelican case, carried to Canberra, opened in their clean facilities. So that's just to maintain some level of cleanliness on it.

**Dave Jones:** Right. What sort of class lean room do you need for satellite stuff? I imagine it's not. It just needs to be, you know, reasonably clean, right? It doesn't have to be super duper.

**Dan Esparon:** Yeah.

**Dave Jones:** Silicon wafer clean.

**Dan Esparon:** Not. So the cleanliness is driven by two things. There's a requirement for it to be visibly clean for the launch service provider. So that's the people who put it on. That's SpaceX who put it on their rocket.

**Dave Jones:** Oh, they've got their own requirements, do they?

**Dan Esparon:** Yeah, because they don't want you contaminating other payloads. Oh, of course.

**Dave Jones:** Yes. Interesting.

**Dan Esparon:** So, but that's pretty, that's, you know, just visibly clean. So that's just a, you know, eight, ISO eight or ISO nine clean room, which is like the lowest, that's the lowest end. But normally what's driving the requirement is actually the optics. So when we've got electro optic payloads, they need a lot more cleanliness. So at the moment we have a, we have an ISO eight clean room, a little 16 square meter ISO eight clean room. And we've got currently a flat packed ISO seven clean room. That's about to get installed, which is 80 square meters. Nice. That's about to get installed on a, on the second level of our, of our office that will let us build much cleaner and much bigger spacecraft as well.

**Dave Jones:** By flat pack, do you mean like Ikea type assemble yourself clean room?

**Dan Esparon:** No, so there's a company in Victoria who make clean rooms. Oh, right. And so they, they build up the whole thing in their office, in their factory in Victoria, make sure it all works together. And then they tear it all down, all the walls flat pack down and then ship it across to us. And they're going to install it. They put it all back up and assemble it for us.

**Dave Jones:** What's the, like the highest profile satellite you've done? Is that the Canini one that you just launched?

**Dan Esparon:** Yeah, I'd say Canini is the highest profile so far. I think the Spirit, the Spirit team probably won't be happy with me for saying that. Right. Yeah. Yeah. Yeah. They're the sort of, they're the two that we've launched so far. Spirit went in December last year and Canini went on the 17th of August, 2024.

**Dave Jones:** And these are all fully Australian designed and manufactured from the ground up.

**Dan Esparon:** Is that correct? Yep. So the, yeah, so the Spirit was a project from the Australian Space Agency with the University of Melbourne. So University of Melbourne bought the bus from us and put their payload management system. They've got an Italian, that's got an Italian x-ray and gamma ray detector in it is like the, one of the primary payloads. But it also has a, a electrical ion thruster, which is built by another South Australian company called Neumann Space. Yeah. Neumann Space. Yeah. Yeah. Yeah. So yeah, Neumann Space make electrical ion thrusters. They were actually just up the hall from us in our office. Oh, okay. And they just moved to a bigger facility to make more thrusters.

**Dave Jones:** Yeah. They, they were here in Sydney, weren't they? I've actually met him once and he was based, I think it was based here, it started here in Sydney, didn't it?

**Dan Esparon:** Yeah. I think, I think Patty Neumann studied in, in Sydney and then moved to South Australia. Yep.

**Dave Jones:** Where all the space action is here in Australia.

**Dan Esparon:** Yeah, that's right. That's right.

**Dave Jones:** Right. Is, is that like a, cause is that like a South Australian government push? Is it to get, to be the space hub of Australia? Is that the.

**Dan Esparon:** I think so. So there was the International Astronautical Conference hosted several years ago now when Australia announced the space agency that they were going to have their own dedicated space agency and everything sort of congregated, congregated around, around Adelaide. So the space agencies are here, the, you know, Intervores here, there's a whole, there's probably half a dozen other space companies floating around the city in the Lot 14 innovation hub area. But I guess going way, way back, defense science technology has been based out of Edinburgh for many years. And if you look back at 19, the 1960s, they launched RESAT-1, which was the weapons research satellite. So that was way back in 67. They built that and launched that. So space has sort of been always big in South Australia and defense is obviously big in South Australia. And it's kind of naturally conglomerated around here.

**Dave Jones:** All we need is a launch, a decent launch facility. It's happening. Yeah. But slowly.

**Dan Esparon:** Yeah. We did some work with Southern Launch, who have got a launch facility over at Whalers Way. And we've, yeah, we've done some work with them in the past. And there's obviously Gilmore up in Queensland who are waiting to launch their rocket.

**Dave Jones:** They are. That's been delayed several times, hasn't it? What's the...

**Dan Esparon:** Yeah, I think they're waiting on launch approval from the space agency, so...

**Dave Jones:** Oh, okay. I thought there were... Okay. Right. Is that all paperwork?

**Dan Esparon:** Yes. Paperwork.

**Dave Jones:** Yep. Annoying. Can you tell us more about the propulsion, the Ion Newman's Ion thruster thing? Is that just for maneuvering the satellite? How do you, like, rotate it? How have you got, like, those wheels that do the physical reaction thing? How do you point and shoot?

**Dan Esparon:** Yeah. So I can't talk much about the Neumann thruster. I'm not a thruster expert. Oh, that's okay. I'm sure they would love to have... I'm sure they would love to talk to you about it because they're a super passionate team doing really cool stuff as well. But for the Interval Bus, we make reaction wheels. So we have...

**Dave Jones:** Oh, you make your own ones as well?

**Dan Esparon:** We make our own reaction wheels. Yeah.

**Dave Jones:** Jeez, you guys aren't mucking around, are you?

**Dan Esparon:** No, when I say we make everything, we make everything. We make the... Wow. We buy motors. We buy bearings. We press bearings. We get the wheels machined. We balance the wheels. We make the motor drivers everything in-house.

**Dave Jones:** Wow. I'm impressed.

**Dan Esparon:** Yeah, it's a lot of work, but it's paying off because it gives us a lot of flexibility when we're building platforms. You know, we can build three reaction wheels or we can do four reaction wheels, which gives us a flight spare or a redundant wheel, which is very useful.

**Dave Jones:** Sorry, would you have to pick an orientation for that spare one? How would the... Because you've got three... I assume you have three in three different orientations. If you've got a spare, how does the spare match to any of the others that fail?

**Dan Esparon:** You can put four orthogonally. Mounting them in certain orientations will give you full control with three out of four.

**Dave Jones:** Oh, okay, right. Yeah, yeah, of course. Okay. All right.

**Dan Esparon:** Yeah, so that's how we mount them on our sort of... Oh, got it. Bigger platforms, yep.

**Dave Jones:** Got it. And your software can just automatically take care of that if one fails. It then knows to change the algorithm to keep it pointed in the direction it wants to go, for example.

**Dan Esparon:** Yes. Yeah, we can tweak some parameters on orbit to address that.

**Dave Jones:** Oh, okay. So it won't automatically do that? If one fails, you have to manually take over, do you?

**Dan Esparon:** I believe it's manual. Right. A lot of the system design is around being really stable without, you know, when things can go wrong. The fault detection recovery is a massive part of the system design. So the sort of normal state of the spacecraft is very stable, very safe, and it lets you then, you know, resolve issues on the ground, you know, with plenty of time to spare.

**Dave Jones:** Right.

**Dan Esparon:** So, you know, you can see something's gone wrong, get all the data from it, run some tests to validate that what you're seeing is correct, and then make corrections to the control system, whatever.

**Dave Jones:** What do you do in terms of how do you do the processing in this thing? What sort of core processor do you have that handles everything? And do you prefer to do it like everything modular with its own little processor, like the reaction control thing or have its own little processor that then talks over a bus to a central one? Or do you prefer to have one central processor sort of handle everything? How modular is this thing, I guess?

**Dan Esparon:** So we've gone for a very modular approach. So sort of, yeah, everything is pretty self-contained with a clear comms interface to it. And then, yeah, we've got sort of pretty standard, you know, ARM M4 processors sprinkled around the place, running the majority of stuff. And then some other sort of lower power processors and a bit more reliable processors to run our power system management as well.

**Dave Jones:** When you say a bit more reliable processors compared to the ARM M4, what are you hinting at there?

**Dan Esparon:** They've got more flight heritage.

**Dave Jones:** Okay, right.

**Dan Esparon:** So they've got more on-orbit flight heritage with demonstrated performance in radiation environments.

**Dave Jones:** Okay, so why wouldn't you use those everywhere? Is it just a cost optimization thing?

**Dan Esparon:** No, no, it's because they just don't have the processing power of modern M4 processors or F4 processors.

**Dave Jones:** Which you'd need those for the sensor packages and all that sort of stuff, I guess.

**Dan Esparon:** Yeah, for our flight computer. They don't have any of the encryption that we need for our radios or any of the performance we need for our attitude determination control system to run the filters and the control loops for that.

**Dave Jones:** Got it. I was going to ask about the encryption side of things. So you definitely want it to be encrypted because you don't want some, you know, nerd in his basement to take control of your satellite, right?

**Chris Gammell:** Yep, that's right.

**Dave Jones:** Is that a requirement or you don't have to? It's just the sensible thing to do?

**Dan Esparon:** Yeah, you don't have to. It's a sensible thing to do. Some of our customers require it. So for a Buccaneer May mission, which is for defense science technology, that required, they specified an encryption requirement for that. But yeah, it's pretty standard. It's pretty sensible thing to do.

**Dave Jones:** So in terms of component selection, bill of material stuff, can your design engineers just go, oh yeah, I'll order this from DigiKey and no worries. Or does everything have to be space qualified?

**Dan Esparon:** How does that work? So at this point, so for the CubeSats, it's pretty much you can just go to DigiKey and select what you need. We try and limit what parts we do use to a certain set. We've also done radiation testing on a bunch of parts already. So we've got data, our own data on how they perform under total ionizing dose.

**Dave Jones:** Got it. So the manufacturer doesn't give you any data on that. You just do your own testing and see what happens.

**Dan Esparon:** Not unless you buy qualified parts. Oh, I'm sure you can buy.

**Dave Jones:** Yes, yes, exactly.

**Dan Esparon:** And qualified parts are becoming more and more available nowadays. With the big LEO constellations like Starlink and stuff, a lot of the suppliers are providing sort of, if you look back, traditionally you get a lot of the military screening options or the NASA screening options, which are like your QML standards. And they're hermetically sealed packages.

**Dave Jones:** What's a QML standard?

**Dan Esparon:** They define the testing flow required for a processor or a part, any part that goes into space.

**Dave Jones:** Okay, gotcha.

**Dan Esparon:** So traditionally you go and you can buy those parts and they're the ones you see in the ceramic packages with big lead frames on them. Yeah, they look so sexy.

**Dave Jones:** They do. They look very sexy. They're just great. And they're a thousand bucks a pop. Thank you very much. Or more.

**Dan Esparon:** Yeah, if they were a thousand dollars, it wouldn't be too bad.

**Speaker ?:** All right.

**Dan Esparon:** Yeah. But now you see a lot more providers are doing like, they call them like LEO plus screening options where they're very similar to their commercial automotive options, but with the enhanced wafer level traceability and sort of radiation tolerant by design or radiation at least tested against radiation failures.

**Dave Jones:** Got it. For those who don't know, LEO is low Earth orbit. Yes. Is that correct? Yes. Yeah. Yeah, that's where we operate. Yeah. So the higher, right. So the higher you go, the different radiation requirements you've got, obviously, because you're outside of our ionosphere. Is that the correct?

**Dan Esparon:** Yeah. And the magnetic field lines affected as well.

**Dave Jones:** Is there like a hard cutoff for that? How does that, I've never looked into the details or does it just gradually attenuate as it goes out the magnetic field? I've never really.

**Dan Esparon:** No, it's quite complex. There's a whole bunch of models available for modeling what your radiation environment looks like. It's kind of as you get. So in the 550 kilometer orbit, which is where we sort of have our CubeSats in, it's pretty tame. Like it's, you sort of get a lot, you don't get a lot of the heavy ions or the heavy ion flux. But then as you go higher into sort of your medium Earth orbit square sort of GPS is, that's a really bad belt because of the field lines up there. And then as you get towards geo, it actually reduces a little bit.

**Dave Jones:** So do you have to be aware of like sunspots and all that sort of jazz? Is that like if you get a report that there's a massive flare or something, do you have to take any measures to actually protect your satellite or what?

**Dan Esparon:** We generally don't have to. We all get a little bit anxious when that happens. So when we had the big solar storms come through, I think it was the beginning of this year, we were all, I mean, I was personally checking the spacecraft health reports as they were coming down to see if anything was going wrong or if anything had reset or failed. But we got through that with no issues at all, which was good.

**Dave Jones:** Oh, nice.

**Dan Esparon:** So, yeah.

**Dave Jones:** Yay for our Earth's magnetic field. That's right. Yep. Yeah, it makes. It'd be a bit different if you're around the moon where there's no field at all. Yep. So have you done any moon, like deeper space, like higher orbit missions or anything like that?

**Dan Esparon:** No, not yet. So we've all been limited to LEO orbit so far.

**Dave Jones:** So how does the comms work? I notice I'm looking at the photo of the Canini satellite, if that's how you pronounce it. And it's got like four rod antennas on the top and four on the bottom, just angled out. Are they like a quarter wavelength dipole? How does that work?

**Dan Esparon:** That's a little bit special, Canini, because it's got a Miriota Internet of Things payload is one of the primary payloads on that. So it's actually, there's two antenna sets, which are broken down into two elements each. So there's essentially four independent elements, which is what those rods are. So they're in pairs.

**Dave Jones:** So that's not the satellite comms. That's specific for the Internet of Things payload, is it?

**Dan Esparon:** So six out of those eight elements are for the Internet of Things payload, and two of those elements we get for our transmit in the telemetry and telecommand.

**Dave Jones:** And so how does that Internet of Things, like, is that like a space-based Internet of Things? Someone has a gadget that talks to satellites, do they?

**Dan Esparon:** Yeah. Yeah. So Miriota, who are a company also based in Lot 14 in LA, they spun out of some research done at the universities down here. Their founders created a company. And essentially what they're doing is they've got remote sensors, very low-power remote sensors that you can put out in fields or on cattle or on water tanks. And they will relay their data back via satellites.

**Dave Jones:** How much power do you need to do that? What's the transmit?

**Dan Esparon:** So their whole – all the magic in their system is that the protocols and the waveforms are all designed around very low-power transmit from the ground and then doing a lot of processing on orbit to error-correct the data back out of the noise. So I'm not quite sure what power they need, but the intent is to have them sit for years on single batteries out in fields. Right. Okay. So super low-power IoT modules.

**Dave Jones:** Got it. Because they're just bursting data occasionally. Is that the thing?

**Dan Esparon:** Yeah. So they'll just burst it up when the spacecraft's overhead and they'll pick it up and relay it back through the cloud.

**Dave Jones:** So how do you receive your comms from this? Do you have your own receiver network? How does that work?

**Dan Esparon:** Yeah. So we have a – just another thing we design and manufacture is we've got a modem, a UHF modem. Oh, wow. So we build that and that's on the spacecraft. We also have a corresponding rack mount unit that we've got for Canini is based out of Yass in New South Wales. So there's a – of all the places to have one, there's a ground station provider in Yass.

**Dave Jones:** Oh, there you go.

**Dan Esparon:** I was there back in late July, early August, in late July, doing integration testing at their site. So, yeah, we've got a dedicated antenna there that we use for all of our command and control of the spacecraft. And that's a very low, very low speed. So it's, you know, 9600 board.

**Dave Jones:** I was going to ask.

**Dan Esparon:** Half duplex radio. So it's very slow, but it's very reliable. So we don't need any spacecraft pointing to make communication, to establish comms with the spacecraft, which is very important at the start. And, yeah, it just – it's a very robust link.

**Dave Jones:** Right. So you can only pick it up over – during part of its orbit, I would presume? Yeah.

**Dan Esparon:** So we get about four passes a day or four to six passes a day, depending on, you know, sort of how the phasing works. And sort of two in the morning, two at night, it's on a – Ken Iney's on a – what's called a sun-synchronous orbit. So it passes over the equator at the same time every day, if that makes sense.

**Dave Jones:** Oh, got it. Right. So you know the exact time it's coming over and you can –

**Dan Esparon:** Yeah, and it's very – passes over the ground station almost the same time. And that's important because it's got an electro-optic payload on it. So it needs the backlit sun as it passes over South Australia to take images.

**Dave Jones:** Oh, got it. Okay. Interesting. So, yeah, what's this other payload on that satellite? What's an electro-optical – what was it?

**Dan Esparon:** So it's a hyperspectral electro-optic payload.

**Dave Jones:** What's a hyperspectral?

**Dan Esparon:** Yeah, so it's a payload – it's a European payload that was purchased by SmartSat, which are a cooperative research centre. So government research – so government-funded research organisation in South Australia. Right. And the hyperspectral payload, it has 45 optical bands from 400 to 1,000 nanometres. And it's got filters on – Oh, wow. Yeah, imagine like a normal camera. Oh, wow.

**Dave Jones:** 45 separate filters. Wow. Yeah.

**Dan Esparon:** Yeah. So imagine a normal camera is two-dimensional plane. Yeah. And it's got pixels all. But this has got filters on every line of pixels. So as you fly over, it takes a – it establishes what's called a data cube of optical information of the ground. So it can pick up things like – you can use it to isolate, you know, ground covers and crop performance. And what that lets you do is you can take that data, post-process it, isolate, you know, which part of this field needs more fertiliser, which needs more water. What's this river system's, you know, algal bloom looking like? And that's used a lot by, you know, agriculture and sort of water management authorities to sort of inform their processes.

**Dave Jones:** Right. So the company makes money by selling the data from the satellite. Is that – you buy like a monthly subscription, do you, to your –

**Dan Esparon:** So Canini is hosting the payload and it's a demonstration for the South Australian government on the usefulness of this data. Oh, okay. So it's a tech demonstration. It's a government-funded thing. Correct. And there's a whole bunch of research that this has sort of spawned through the universities and through SmartSat into how we can process this data both on orbit and on the ground to get better information out of it.

**Dave Jones:** So all this transmits on 400.5 megs. Is that right?

**Dan Esparon:** No. So we've also – for the payload data, we've also got an S and X band radio as well. So for our primary command and control, it's 400 megs. But then we also have a payload data radio that's at S band and then X band downlink. So we don't have ground stations for that. We don't build the S band and X band radio. That's one thing we don't build. We buy those because they're a little bit – we're currently developing one, but that's in the pipeline. Yep. So we use a commercial ground station provider for that. We're using a provider that's got sites in Svalbard in the Arctic territories and in Troll off the coast of Antarctica. So with that, because of the orbit we're in, we get passes every 45 minutes.

**Dave Jones:** Oh, wow. That's impressive. Yep.

**Dan Esparon:** Yeah. So we get a lot of passes and very high data rates so we can stream images down very quickly. We get low latency for the IoT payload as well.

**Dave Jones:** How does the launch happen? And what sort of steps do you have to go through to launch on a SpaceX? You were one of like how many payloads on that SpaceX launch a couple of weeks ago? How many weeks ago was it now? Three, four weeks ago?

**Dan Esparon:** Yeah, about a month ago, 17th of August it was. So yeah, so we use a launch service provider out of Europe. So what they do is they take a whole bunch of 6U CubeSats and they have dispensers for them. And then they'll put our CubeSat into their dispenser and then they'll ship that to SpaceX to integrate on the transport or any of the ride share missions that SpaceX have. So there was over 100 different space objects on that one transport mission. So that's everything from like one U CubeSats, three U CubeSats. There were small sats. So small sats was kind of like 100 to 500 kilo spacecraft. All manifested by different companies, different launch service providers, you know, space tugs, all sorts of things.

**Dave Jones:** And ultimately you pay per kilo or is it per like storage, like meterage?

**Dan Esparon:** This is a little bit outside of my knowledge, but I believe you pay per launch and there's a limit on the mass you can launch with that. With our LSP. I think at the end of the day it is per mass, but we're not paying per 100 grams of payload mass we put on there.

**Dave Jones:** So how do they actually, I've never looked into the details, how do they actually launch the CubeSat out of the, you know, the Falcon rockety thing? Is there like a spring in there that just boom and just shoots it out or what? I mean, how does it do it?

**Dan Esparon:** That's exactly it. So there's a spring and a pusher plate.

**Dave Jones:** There's actually a spring, I thought.

**Dan Esparon:** They open the door and the spring pushes it out and that separates it from the space vehicle. Yeah.

**Dave Jones:** Right. So there's a little latch and then they just release the latch and the spring just goes boing.

**Dan Esparon:** Yep. That's pretty much it. Right. As far as I'm aware. At least that's what the test pods look like. Yeah. Very low tech. Very reliable. I mean, our solar panels, you see a lot of the solar panels on CubeSats and antenna elements even. They're all, all the hold down release mechanisms for them are all burn wire. So you wrap a little bit of meltable wire around a resistor. Yes. Get up the resistor. I've done that.

**Dave Jones:** I've been there, done that. Yep.

**Dan Esparon:** And there's a spring and that springs it up and that's how you deploy a solar panel or an antenna element or anything like that.

**Dave Jones:** Okay. So how does your satellite know that it's just been sprung out?

**Dan Esparon:** Yeah. There's a requirement. You have to have separation switches. So they detect when you're, when the doors opened, they'll be released. And that's what is holding the batteries disconnected from the rest of the bus and all the flight computers and radios turned off. Then there's a sequence after dispense where you have to wait a certain amount of time before you can deploy antennas. And then another wait before you can transmit anything as well.

**Dave Jones:** Ah, interesting. Why is that? Because it might interfere with the other, the transmitting might interfere with the other satellites that have just been launched or what?

**Dan Esparon:** Yeah, that's right. They don't want you, you screaming out at, you know, five watts or whatever out of your radio straight after dispense right next to someone else's sensitive receiver.

**Dave Jones:** Okay. Right. Is it, is it randomized or do you have a specific or it's just a separation distance, a fixed timer, like five, 10 minutes later or something?

**Dan Esparon:** Yeah, there's a fixed time. It's about an hour after dispense. Oh, okay.

**Dave Jones:** Oh, an hour. Okay. Right. So there's quite some actual distance separation then.

**Chris Gammell:** Correct.

**Dave Jones:** Yeah. Interesting. It's just a spring, just boing, out it goes. I assume it's not fast. I mean, you know, it's obviously traveling around the globe fast, you know, at how many tens of thousands of kilometers an hour. But in terms of a relative velocity, like how far would you be from the vehicle like an hour after you sprung out of it?

**Dan Esparon:** That's a good question. I actually don't know how far you'd be. It's not very fast. It's meters per second.

**Dave Jones:** Yeah. Yeah. Yeah. You actually see them being deployed and it's like, it just slowly drifts out kind of thing.

**Dan Esparon:** Yeah. And one of the big problems that you can have on transport missions, we were lucky this didn't happen to us. Well, not lucky. We were, because we were on a dedicated band, it wasn't too much of a concern. But one problem that you see a lot on the CubeSat missions is that because there's so many objects being deployed, there's radio interference everywhere. So normally your first few passes are really poor because you just, there's too much noise in your receiver. Right.

**Dave Jones:** Yep.

**Dan Esparon:** We, we didn't have that issue. But the, what that leads to though, is that after you dispensed NORAD, who's the North, the US radar people, they will assign object numbers to every space object that's launched. So we've got a NORAD ID. I don't know what it is, but it took, we only got that last week. So it took, you know, almost a month to get, for them to isolate which object on their radar screen was Canini. Oh, wow. And now that they've, now they've been able to do that, because it's just a big blob of, of metal up there, right? Yeah, yeah, right. On their radar screens. And so they've now assigned us an ID and we can now, they're now updating our orbital parameters every couple of days. We get a new orbital parameter set from them for our ground station tracking. Wow.

**Dave Jones:** So they're tracking every little tin pot cube set up there, which is like thousands now, which is just.

**Dan Esparon:** Yeah, I was just going to look at what the NORAD ID. So we're NORAD ID 60556 is Canini and they're just sequential. So, you know, there's at least 60,000 items in the catalog.

**Dave Jones:** Oh, wow. So is this like public? Can people track your satellite publicly? Is that the.

**Dan Esparon:** Yeah, I can send you some links. There's, yeah, there's a whole bunch of websites, Celeste Track, and there's another one that's run by someone that essentially has a list of every object that's in the NORAD catalog and all the orbital parameters. And then if you go, there's an organization called SatNogs, who are like radio amateur, satellite radio amateur operators. And they will, they've got a list of, you know, all the amateur or all the CubeSats and observations from their ground station antennas of.

**Dave Jones:** I am on their page now for your, yeah, so you can see the waterfall plot and that is cool.

**Dan Esparon:** So, yeah, they have a list of all the spacecraft too and some details on them as well.

**Dave Jones:** What is the audio? I can play audio. What is that? Is that just the audio of the waterfall thing?

**Dan Esparon:** Yeah, that would just be probably be garbage for us because we're all digitally modulated. But a lot of them are, you know, you can get some that are audio band modulated or, yeah, you can at least listen to the spectrum.

**Dave Jones:** I just don't know how they track so many objects up there. It's just, it's just insane. It's just a radar, is it? It's just, they can detect things of, you know, over five centimeters or something.

**Dan Esparon:** So there's, there's so many different ways that they track space objects. So one of the things that Intervo is doing, one of our payloads is a space domain awareness payload. So one thing that sort of defense has realized both in the US and Australia and worldwide is that having systems to detect and monitor space systems is very important. So there's radar systems on the ground that track objects. There's also optical telescopes on the ground that they use to monitor them. There's space-based optical telescopes, which is what our Hyperion payload is. So that's a telescope that we can use to track and detect objects in geo and sislunar space.

**Dave Jones:** Oh, okay. So there's a satellite that detects other satellites.

**Dan Esparon:** Yeah. So we've done an engineering model of that. It doesn't quite, there are, there are many that detect other satellites, but we haven't built one yet. So yeah, they've got optical telescopes and they'll sit there and look out of the area of space and see things come through their, their field of view. And then they can calculate their orbital parameters based on how it traveled through their field of view.

**Dave Jones:** How concerned are you guys and the space industry about the famous Hessler syndrome? About how one, if there's, if there is a space, space collision, then it actually generates debris. And then that just, boom, expands out and then it takes out more satellites, more and more. And all of a sudden the earth is just surrounded by garbage and space has become completely useless.

**Dan Esparon:** Yeah, it's, it's a massive concern for the whole space industry. I mean, that's a lot of the work that the Australian Space Agency are doing is on how to, is on putting in the policy to make sure that there's not a lot of space debris. You know, there's a lot of, in our design phases, there's a lot of, a lot of segments of the review where it's looking at, you know, are you going to generate space debris? Are you going to be on orbit for longer than however many years? Will you naturally decay or are you going to stay up there? And making sure that when you launch something, once it's at the end of life, that it does deorbit is, is quite important. And then especially for bigger spacecraft, having propulsion to maneuver and stuff like that is important as well. So yeah.

**Dave Jones:** Right. Well, I was going to ask, like, how long can you keep a satellite up there in terms of like trade off with fuel?

**Dan Esparon:** Yeah. So our ones go up to 550 kilometers and we expect between three and five years before they'll deorbit.

**Dave Jones:** That's if you don't actually do anything.

**Dan Esparon:** Yeah, correct. And none of ours have got propulsion on them. They're all...

**Dave Jones:** Oh, okay. Right. Right. So the ion bit, but you've got the Newman ion thrusters, right?

**Dan Esparon:** Correct. Correct. On the Spirit, it has got the ion thruster, which is a demonstration of their technology. It's not on there as a actual thruster unit.

**Dave Jones:** Oh, okay. Oh, right. Okay. It's on there as a payload. Right.

**Dan Esparon:** Yep. Then once you get up to higher orbits, it then becomes sort of exponentially longer as you go higher and higher.

**Dave Jones:** So all these CubeSats, I mean, they're launching, what, thousands per year? How many would it be? You know, a thousand CubeSats a year? It seems like every man and his dog's putting up a CubeSat these days. Probably hundreds per year, I'd say. Okay. Hundreds per year. But it's still a lot. And do they all go into the same height orbit or does SpaceX kind of like, oh, we'll go an extra 30 k's higher for this one because we'll just spread it out and then...

**Dan Esparon:** They all go into similar orbits on one launch. Yeah. They do get spaced out. How much that relates to in altitude, I'm not quite sure. Yeah. So they do get sort of spaced out a little bit. But when you look at the relative distances between space objects, it's still a long way between objects. Yeah, it's still a long way. Yeah, yeah.

**Dave Jones:** Yeah, that's right.

**Dan Esparon:** I'm always shocked when I talk to our modelling and sim people about, oh, how far away is that object? Oh, yeah, we're really concerned it's, you know, five kilometres away. It's like, okay, well, yeah, that's probably concerning when you're going seven kilometres a second.

**Dave Jones:** Yes, yes, exactly. Exactly. How is the Starlink? Because how many satellites have they got up now? They have 60% of the orbiting satellites or something? Something like that, yeah. Yeah, it's enormous. How has that changed the game? Has that changed the congestion up there? Are they in, like, their own orbital plane or what's the...

**Chris Gammell:** Not really. We get...

**Dave Jones:** Have you got any insight?

**Dan Esparon:** A little bit. So we get notifications when there's a possible... Not a possible collision, but when two objects are likely to get close together, we get a notification about that. Now, because we can't manoeuvre, there's not much we can do about it. So we just kind of get told. Yeah, right. And the Starlink will move around, use their thrusters to move around a little bit to avoid collisions. But it hasn't really impacted us. I mean, the big impact is that you get more launches, right? So there's, you know, with Starship coming online... Oh, yeah, of course. So the cost comes down. The cost of launch is falling. You know, we're building a... We're currently building our next spacecraft bus, which is, you know, Astralis, which is a, you know, 250-kilo class spacecraft. So going from sort of 25 kilos up to 250 kilos. So they're big spacecraft with big optics. Well, bigger spacecraft with bigger optics, I'd say. They're not the biggest. You know, because the launch cost is coming down, it means that more and more people will be launching these small sat platforms in the future. That's really where the industry is going.

**Dave Jones:** How much has SpaceX changed the industry? Would the industry be... Like, I assume it'd be... Well, it wouldn't be dead, but how would the industry be without SpaceX at the moment, who are doing, like, what, 90% of launches at the moment? It's nuts.

**Dan Esparon:** Yeah, it'd be hard to tell. I haven't been in the space industry long enough to not to know what it was like when SpaceX weren't launching.

**Dave Jones:** Oh, to not under, right? You young whippersnapper. That's right, yeah.

**Dan Esparon:** Yeah, so... But, yeah, I mean, you can just see it in, you know, there's a lot of excitement around the Starship and the master orbit capability of that and what that's going to mean for the industry. You've got fleets of cubesats launching to do things that people haven't ever thought about before. So, like, Miriota's IoT. You couldn't have done that in sort of old space because you could never afford to launch the dozens of spacecraft they need to provide coverage. But now you've got, you know, miniature electronics, you've got, you know, small spacecraft buses that are extremely capable from a power and comms point of view. You know, you can see, you know, nowadays you're looking at modern radios can do, like, over gigabit per second down links. So, you know, you're streaming massive amounts of data down. You know, the ground station providers are all over the world providing high data rate comms to space systems. So, you know, really it's enabled a lot of these industries to grow a lot and a lot of new industry come through. And just, yeah, with more and more capacity to orbit, it's just going to get better and better.

**Dave Jones:** What sort of leap would, assuming that Starship, they can eventually get it, you know, orbiting and actually putting actual payloads out, how much does that change the game in terms of cost to orbit, roughly? Does it come down by an order of magnitude or does it halve?

**Dan Esparon:** I've seen numbers saying that it could be an order of magnitude, at least, for Starship. I can't remember the numbers right off the top of my head, but, yeah, it could be another order of magnitude drop, which would be massive in the industry. Wow.

**Dave Jones:** Yeah, that's absolutely huge. Oh, my goodness. What about laser comms? There's quite a few. There's a few NASA missions at the moment testing out, like, laser comms. Is that a thing? Is that an orbit thing or is that a, like, a deep space mission thing? Do you know anything about that, how that might impact things?

**Dan Esparon:** Yeah, so it's both. So there's a lot of interest in optical inter-satellite links. So Starlink's using optical inter-satellite links, as far as I'm aware.

**Dave Jones:** Oh, that's right. Yeah, I think I heard about that. That's their new gen one, right? Yeah, their new gen ones. So they can talk to each other via laser. Wow.

**Dan Esparon:** Correct. So they've got laser tracking, and that's a big area of sort of research and development is how you get. I was just at a conference last week that had a demo of a laser tracking optical system where it can, you know, it will track the object on the other side to get the link to improve the link performance. So that's really cool.

**Dave Jones:** Wow. So each Starlink satellite would have to know where all the others are, and then it'd have to know its own orientation and position, and then tilt-swivel the laser pointer to point at the other satellite?

**Dan Esparon:** Yeah, and then we've done a whole bunch of projects with the university in the last few years on using piezoactuators to provide very high-frequency stabilisation on both camera images and inter-satellite links as well.

**Dave Jones:** Why would you need a high-frequency? I mean, you're pretty stable out there in space. Why do you need any high-frequency stabilisation compensation?

**Dan Esparon:** It's to get rid of any jitter from your control system. So any high-frequency jitter is the key.

**Dave Jones:** Yeah, but your control system is, once you've pointed it, you only have to occasionally reorient it.

**Dan Esparon:** No, you have to continuously track between the two.

**Dave Jones:** Oh, you have to continuously track.

**Dan Esparon:** So you're continuously tracking between the two objects. Got it.

**Dave Jones:** So you're saying the jitter in the control loop of that thing causes a problem, so you have to go to more high-frequency actuation. Is that correct?

**Dan Esparon:** No, I realise I've goofed that completely. Sorry, that was for optical imaging of the ground.

**Dave Jones:** Oh, okay, right. Okay, so that's the piezoelectric stabilisation. Right. So the optical payloads often need a high-frequency piezoelectric actuator system.

**Dan Esparon:** It's an area of research to improve the performance of them so you can get better. Right. Because, you know, any jitter on orbit will lead to blurring of the pixels on the ground. So you need to...

**Dave Jones:** Blurring photos. Same as our normal handheld camera. Correct. The image stabilisation system. Right. Correct. Okay. Wow. See, I wouldn't have thought of that because when I think of satellite, I think of, like, ultra-stable. You know? It's like, it's something that wouldn't have occurred to me. I think, oh, yeah, they don't need any image stabilisation because they've got a satellite. Sure, it's moving. But other than that, it knows exactly where it's going. There'd be no jitter in it. But the control orientation for the camera... Oh, because the camera's got to be pointed on the ground at the one spot. That's right. Right? Even though the satellite's travelling fast. That's right.

**Dan Esparon:** So you're tracking, you're slewing as you come over a point in the ground. You're slewing. Right, yeah. And any, you know, wobble in your reaction wheels or jitter in your reaction wheel speed controller will cause jitter in your image.

**Dave Jones:** Of course. Right. So the higher frequency orientation, higher frequency stability compensation you got, the more betterer.

**Dan Esparon:** That's correct.

**Dave Jones:** Got it. Okay. So piezoelectric, how does that, I mean, how does that physically work, physically manifest itself?

**Dan Esparon:** You're getting to the edge of my knowledge on this. Okay, right. Okay. You can essentially get, you can get microelectronics, you get micro movement from piezo stages with very, you know, micron or nanometer control. And you can drive a signal into them that will, that will position them very accurately. And very quickly as well, because they're, yeah, they're piezo systems.

**Dave Jones:** Oh, wow. That is very cool. Okay. Is there anything we haven't talked about in terms of the electronics systems that you want to cover? Any, any, any cool, any interesting or really difficult stuff that you've had to solve?

**Dan Esparon:** Lots of difficult problems to solve, but none jump out at me. I mean, the, the testing of these systems is really very quite interesting, is very interesting because you do all sorts of EMI and EMC testing, which you kind of wouldn't, you know, you don't really initially think about, but the payloads can be very sensitive to, to electromagnetic noise. So testing those types of things, testing those in a clean environment is very challenging. And then the, you know, all the environmental testing, the vibe testing, the TVAC testing, that's all very, very cool. But that's probably another half hour worth of discussion.

**Dave Jones:** Yeah. I know. I, yeah, no, totally. We could, yeah, I've been involved in the vibration and environmental testing side of things. And I assume you'd have a small team dedicated to just testing?

**Dan Esparon:** Not really. No. All our engineers test stuff. We've got a dedicated team of systems engineers who act as test directors and test managers and they coordinate the whole thing. But yeah, it's a lot of the, a lot of the engineers end up doing a lot of the testing.

**Dave Jones:** And how do you break your teams up physically? Does somebody work on, right, you're the reaction control module team. You're the RF comms team. How does it, you're the processor team. You're the payload team. How does that work?

**Dan Esparon:** Yeah. So we split by subsystems. So there's sort of the electrical power system, which is your battery, solar panels, solar regulators. There's that attitude determination control system group, which do all your, you know, your reaction wheels, your star trackers, Nadea sensors, all those types of systems. And then all the control algorithms that go along with it. Then there's the CDH team, which are command and data handling. So they do all the radio design, the link design, the command and control of the spacecraft, how protocols work inside and outside the spacecraft. And then there's the mechanical team who do the structures and the thermals analysis and all that stuff. So it's kind of split into those groups. That makes sense. But, you know, within the, you know, we've kind of got discipline splits. So there's a software spacecraft software team. There's a grounds software team who do all of our mission control design and development. Then the electrical team. And within the electrical team, there's, you know, we've got a whole bunch of really good engineers across different disciplines. We've got, you know, RF engineers who are really good RF engineers, really good PCB layer engineers, power system engineers, you know, the lot. So people have sort of got their specific area, but everyone's pretty, got pretty good breadth of knowledge because it's such an integrated system.

**Dave Jones:** How long from go to woe are you talking about for a typical satellite from when you start to when it launches?

**Dan Esparon:** So I can, Canini was announced in 2021.

**Chris Gammell:** Okay. That's not too bad.

**Dan Esparon:** And launched this year. Yeah. There's a sort of, you know, 12 to 18 months is your integration and testing. So, you know, we do on the spacecraft, there's over 400 unique tests that we perform on everything from printed circuit board assemblies. So making sure the regulator works and the process is working all the way through to Vibe and TVAC on the whole integrated system. So lots and lots of testing. And that's the bulk of the time is the test phase.

**Dave Jones:** How far out do you have to book the launch? Because I know engineers do their best work under timeline pressure. If you've got no, you know, if you've got no end date, everyone kind of, you know, just sort of goes into cruise mode. But if you've got a fixed launch date, that kind of puts a fire up your butt.

**Dan Esparon:** Yeah. The fixed launch date isn't actually until very late. You can shift launches. Okay. I can't remember the exact time. It's, you know, months, months out. I think it's about six months out. You can shift the launch. But you have to book in two years ahead. So I think it's about two years ahead. 24 months to get on a launch. And then you can sort of slip launches as you get closer as well.

**Dave Jones:** Got it. So you can't launch any sooner than that.

**Dan Esparon:** Yeah. I mean, that's something that you can, but it's more difficult.

**Dave Jones:** Okay. What if you lose your, what if somebody loses their slot? Can somebody else come in and take their slot earlier? Or how does that work?

**Dan Esparon:** I'm not sure, actually. Yeah. I assume SpaceX managed that internally somehow.

**Dave Jones:** Right. Okay. Right. Because do they have to, well, I guess this is a question for SpaceX. Is every CubeSat treated the same? Or does SpaceX have to do anything specific for individual CubeSats? Or they're all just lumps to them that they shoot out with their spring loaded launcher thing?

**Dan Esparon:** So there's actually, SpaceX don't directly interact with the CubeSat providers. We're too small for them to. So there's actually intermediates, launch service provider intermediates.

**Dave Jones:** I'm sure the larger ones they would.

**Dan Esparon:** Who, you know, we work with a company in the Netherlands. So they essentially, we pay them to launch our spacecraft and they put it on, they assign it to a SpaceX launch or whatever. And then they have, you know, 10 or 20 CubeSats on one transport emission. All from different sub-customers.

**Dave Jones:** Last follow-up question on the thermal side of things. Obviously, you have to get, the battery's important to keep thermally stable. What about all the boards and what about the payloads and stuff like that? Do you just not bother heating those? Or how does that work?

**Dan Esparon:** So because you only have, because we're on a 90-minute orbit, so we come in and out of the sun and the shade pretty regularly, it doesn't get extremely cold inside the spacecraft.

**Dave Jones:** Okay. Okay, right. What's the minimum?

**Dan Esparon:** Around zero degrees Celsius.

**Dave Jones:** Oh, wow. Oh, geez. Oh, that's a piece of cake, right?

**Dan Esparon:** That's pretty normal. Wow. Payloads can get cold. So, you know, one of the payloads we have is very thermally sensitive. Normally, the thermal is dictated by the performance of the payload. So, you know, you've got a hyperspectral, it can't get too hot or too cold because the optic alignment can be affected by that.

**Chris Gammell:** Of course, yeah.

**Dan Esparon:** And they'll sometimes have heaters on them or they'll have heat sinks attached to them, and that's all down in the thermal design phase and then validated in the environmental testing.

**Dave Jones:** Right. Okay. And just some things love the cold of space. It depends on the payload.

**Dan Esparon:** Yeah, correct. That's right. Yeah. So, you get like some of your infrared images, they really want to be quite cold. So, you want to connect them up to heat sinks and try and get as much heat out of them. But then you have the problem of conducted heat through the structure. Through the structure.

**Dave Jones:** So, you might, yeah.

**Dan Esparon:** The rest of the bus will get too cold. So, you kind of, there's a lot of thermal design goes into these systems to, you know, between different heat sink compounds and heat isolation compounds and heat sink materials, putting different material finishes on the outside of the structure to get different radiative performance is a big thing that we do. So, you know, your material coating really affects how well a heat sink will work.

**Dave Jones:** Yes, it does. I mean, yeah, they make heat sinks black for a reason, for example.

**Dan Esparon:** Yeah. And then there's, it's not just the colour, it's like the emissivity and the absorptivity as well as a problem. So, you need to not absorb too much heat from the earth or from the sun if you point that way.

**Dave Jones:** Probably last question because we've run out of time. What in terms of redundancy do you have on board and what if you lose comms? Does the system automatically reboot or how do you hand, does it enter some sort of emergency mode? How do you handle that?

**Dan Esparon:** Yeah, this is, yeah, we've got a, so we'll go into a... John could do a whole episode on that, right? Yeah, the fault detection recovery is a massive part of space systems and the way it's designed, like the modular design is really to support that, right? So, you know, if you have a, if you have one big battery module or battery management system and you lose one critical part there, you lose your whole battery system or you can have five slightly larger battery systems and you've got that redundancy there. So, we handle it everywhere from, you know, the power supply level where we've got protection on all our power supplies, the module level where we've got redundant modules in the spacecraft and then, you know, even like file storage. We've got, you know, a dozen different file storage locations on the spacecraft to store data or command files or things like that or firmware images. And then the software on top of that all is managing the fault detection and recovery process as well and logging incidents and notifying, like, you know, downlinking event logs and things like that. So, it's kind of a very layered approach, right? It comes all the way from the hardware level of the circuits on the board to the modules, to the software, to the whole system design. So, right.

**Dave Jones:** And can you remote update your operating system if you need to?

**Dan Esparon:** Absolutely.

**Dave Jones:** Absolutely. Oh, you can, right. You wouldn't do it otherwise. Is that, so processor versus FPGA?

**Dan Esparon:** We've got a lot of processors on board and not a lot of FPGAs, but the payloads have got a lot of FPGAs because they're interfacing to different, lots of different high-speed sort of interfaces.

**Dave Jones:** All right. Well, I think our amp hour's up, Dan. Thank you very much. That was incredibly interesting. I'm sure we could do an episode on, like, just one hour on each individual thing we've just briefed over here.

**Chris Gammell:** Yeah. Yeah, I think so. It's been very, very good talking to you. It's crazy.

**Dave Jones:** All right. Well, thank you very much. And we'll provide links down below to Innova. And so, do you personally have any, like, websites? Are you on the socials? Do you have a YouTube channel?

**Dan Esparon:** No, only on LinkedIn, unfortunately. So, personally on LinkedIn. And you'll see updates from Innova on LinkedIn and Twitter and all sorts.

**Dave Jones:** Got it. So, no one can follow you personally? No, unfortunately. Not at this point. You're not a social, right. You're not one of those social engineers.

**Dan Esparon:** No, no.

**Dave Jones:** It's probably good for your mental health. Probably. Probably. Awesome. Well, thank you very much, Dan. This has been awesome because I'm very interested in space stuff, but, you know, I know so little about it. So, fascinating.

**Chris Gammell:** Thank you very much for your time. It's been great talking to you. Thanks, Dave. Thanks for your time. All right. Catch you next time. See ya. Bye.

**Speaker ?:** ! We'll see you next time.
