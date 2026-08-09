---
episode: 524
title: LEDs and EVs with Mike Harrison
url: https://theamphour.com/524-leds-and-evs-with-mike-harrison/
---

**Mike Harrison:** This is The Amp Hour Podcast. Released January 3rd, 2021. Episode 524. LEDs and EVs with Mike Harrison.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Mike Harrison from Mike's Electric Stuff, again.

**Dave Jones:** Yeah, welcome back, Mike. Hey, Mike. Just in time for 2020.

**Mike Harrison:** That's right. Yeah. 2021. Actually, this will be released in the new year, guys. We really will. This is our final recording of 2020. But yeah, this is a new year episode.

**Chris Gammell:** We're talking in the future.

**Dave Jones:** Oh, well, everything will be normal when this is released.

**Mike Harrison:** Guys, we fixed it. We fixed it.

**Chris Gammell:** Well, I think the Oxford vaccine is, I think, going to be approved any day now here. And they've already made quite a lot of a million doses of it. So it's still going to take a long time. It's going to get worse before it gets better, certainly in the UK after Christmas. Yeah, same here. Same here.

**Dave Jones:** Unfortunately. But even then, I suspect it's not going to be a magic bullet.

**Chris Gammell:** No, no. It's going to take time.

**Dave Jones:** Anyway, how you been, Mike?

**Chris Gammell:** Yeah, what you been up to?

**Dave Jones:** It's been a while.

**Chris Gammell:** It's sort of busy and not busy in equal measure. Sort of a few jobs happening. Everything just died around March. But things have started happening again. More lead boards. But there's a bit of a lack of motivation as well.

**Speaker ?:** Right.

**Dave Jones:** From a self-employed contractor point of view, when everything dried up like that, did you think, oh, crap, I better start actively doing something? I don't know. Designing a product. Doing something to...

**Chris Gammell:** Well, I mean, not financially, but maybe in terms of keeping myself occupied, yes. But the motivation wasn't really there. I still haven't quite finished doing my kitchen. I bought most of the stuff I needed to finish it just before lockdown. And all the wooden floor stuff is still on the shelf. And a few tiles got slapped on the wall, but not a lot of else.

**Mike Harrison:** Yeah. Yeah.

**Speaker ?:** Yeah.

**Mike Harrison:** I mean, are you... Is that the kind of thing, like when you are not doing other people's jobs, do you have kind of like backburner projects in electronics that you're doing?

**Chris Gammell:** Yeah. Obviously, there's YouTube stuff. I'm just in the process of designing a new product. Well, I basically had a few inquiries for a very similar thing from about three different past customers and potential customers within about a week, which is a high channel count dimmer for AC LEDs, AC mains LEDs, like little things like GU10 bulbs and mains LED tape and so on. And there isn't really anything on the market at the moment aimed at low pain. Now, you can get these massive dimmer racks of stage lighting with like one kilowatt per channel. But so I'm working on an eight channel, a 16 channel, sort of about, you know, 250 milliamps per channel sort of mains dimmer.

**Mike Harrison:** Oh, that's good.

**Chris Gammell:** I might do a video on it, actually. It's quite interesting design challenges.

**Mike Harrison:** Yeah. Right. Do you do like a chopper or you like cut off the top of the wave? Or a triac-y control thing? Well, no.

**Chris Gammell:** Lead bulbs like trailing edge dimming rather than the leading edge dimming that you get with triacs. So basically, you use a pair of back-to-back series MOSFETs as a switching element. And that presents a few interesting challenges when you want a lot of them. Because if you imagine you've got two N-channel MOSFETs in inverse series, you've got the two sources connected together. And that is basically your reference point for your drive signal. But of course, that is flying up and down with the mains. And each channel is completely different. So effectively, you need to generate, yeah, for each channel, a completely floating voltage source.

**Mike Harrison:** Oh. Without transformer, probably, right? 12-channel. Ouch.

**Chris Gammell:** Yes. Floating. So I was starting to think through in my head. Oh, yeah, I'll use a 16-channel PWM chip on the main side before I realized this issue about the reference for each channel is completely independent. But I then found this. I mean, I started looking at photovoltaic opto-isolators, but they're a little bit slow if you want to get a reasonable resolution for the turnoff time. It's not so much they're slow. Their turnoff time is not very well specified. So you're going to expect quite a big channels-to-channel variation and variation with temperature, phase of the moon, whatever. But I found this absolutely brilliant chip from Scilabs. This is chip of the week, folks. Chip of the week. It's a SI8751, which basically it's like it's one of these capacitive isolation devices.

**Mike Harrison:** Oh, yeah. Because that's how they do all their isolation, right? Yeah, yeah, yeah. When they're doing like a spy bus isolator, whatever they do, capacitive, right?

**Chris Gammell:** The neat thing is that it also uses some voodoo that I don't quite understand to shove about 20 microamps at 10 volts across the isolation barrier. So it will directly drive these MOSFETs with literally all you need to make a fully isolated switch is two MOSFETs in this chip. And that's it. That's all you need.

**Mike Harrison:** And there's no like coil in there for doing the power?

**Dave Jones:** So you don't need some secondary side power?

**Chris Gammell:** Exactly. And that is the beauty of it. And they're not expensive. They're like a bit over a pound or something each. So and they're in an S08. So, you know, 16 of these with I'm using SOC 23. I found some SOC 23 MOSFETs that are rated at about 12 amps, which I don't entirely believe, but they seem to be fairly robust.

**Dave Jones:** That's the great thing about using MOSFETs is that they don't need much drive. So, well, apart from if you're driving fast with the capacity of gate.

**Chris Gammell:** Yeah, this is 100 hertz. And all I care about is a reasonably consistent turnoff time because that also affects the actual brightness. So, yeah, that, you know, I've bought a couple of other trailing edge dimmers just on AliExpress and another one just to see how everyone else does it. And they've all got like an individual one, those little brick DC-DC converters, like the little like one watt little black jobbies per channel plus auto isolator. So, you know, once you start wanting to get 16 of those into a reasonable space, that gets gets a bit messy.

**Mike Harrison:** Could you explain the trailing edge versus leading edge, too? I've never heard those terms before.

**Chris Gammell:** OK, if you know a traditional triac dimmer, it waits for the zero crossing in the mains, then waits for a while and then turns it on after a delay and then turns the load on for the rest of that cycle. Because the triac, when you trigger it, it latches on and it only turns off when the current through it falls to zero. And that's how light dimmers for the last several decades have worked. Yeah, yeah. But lead, mains lead bulbs, the dimmable ones, and they are fairly specific, much prefer a trailing edge where you turn it on at the start of the zero crossing and you then turn it off at some point through the cycle. And it's to do with the architecture of the way that the lead lamps work in that they have to both generate the drive for the lead, but also sense what the phase angle is so they can actually dim it. Because they're generally like a switch mode power supply with some sensing to measure the phase angle and then dim the lead based on that. So you've got some capacitive load on them. That's one of the issues with the leading edge dimmer. You've got the front end of the switch mode power supply, which is a rectifier and an electric capacitor. So if you turn that on halfway through the cycle, you get quite a high current surge. And generally, if you look inside virtually any sort of conventional light dimmer, you'll see there's a fairly big choke in there just to reduce this rise time when the thing turns on. Whereas with a trailing edge, sometimes it's called a phase cut dimmer instead of trailing edge. But of course, you're turning on at the zero crossing point. So you'll turn it on, it's nice and slow as it goes up the sine wave. And it's only the turn off that's quick, which is generally less of a problem. Although I did find, I did encounter, you learn everything on every job you did. I was running this into a test load, 16 channels into this massive big pile of metal lad resistors. I was using a test load. So I was putting about four amps through this thing. And I was running it through an isolating transform in a VARIAC. And what would happen is, as I turned the mains voltage up, suddenly, I'm using one of these little PCB mounted mains power supplies just to generate all the internal mains stuff. And at some point, this thing would pop. Yeah, literally, it would blow the capacitor out. This is on the incoming. Yeah, this wasn't my output switching devices that were blowing. It was the mains power supply in this thing. I thought, what on earth is going on here? So I eventually put a scope on the incoming mains. Of course, what happens is, I've got this four amp, basically one kilo load being switched off rather quickly. And it's coming from the secondary of a transformer, which, of course, is somewhat inductive. So I was getting this, like, 800 volt spike. It was just annihilating the power supply. So I've learned, if you're doing trailing edge dimmers, either don't use a transformer or just stick a few microfrads of capacitance on the output of that transformer. So, yeah, it wasn't a particularly wide spike, but it was just the amplitude. It was enough to cause quite serious mayhem.

**Mike Harrison:** Well, you know, it's like Christmas season and, you know, British people love Christmas poppers, right? So it's just your power supply doing that, right?

**Dave Jones:** So it's clamping on the solution there is either, well, stop it from doing that or clamp the primary side mains. But you're not clamping it because of incoming lightning strikes. You're clamping it because of...

**Chris Gammell:** I mean, yeah, this isn't something that's going to be an issue in the final product. It's just because I was bench testing on a Variaq or an isolation transformer.

**Dave Jones:** Ah, right. Okay.

**Chris Gammell:** So, yeah, my solution is you just stick a bit of load on that transformer and the problem goes away.

**Dave Jones:** That's great.

**Chris Gammell:** It's because it literally had no load at all, except this four amps that were suddenly switching off within, I don't know, 100 microseconds or something. And it didn't end well.

**Dave Jones:** So, well, I was going to say, this chip has two pillar clamp pins. Can you explain what they do? It's like...

**Chris Gammell:** I don't know. I don't... Yeah, I don't really understand what those did. I just ignored those and it seemed to work.

**Speaker ?:** Right. Okay.

**Dave Jones:** Right. Because it says that it provides clamping to prevent unintended turn-on of the external FET you're driving. So...

**Chris Gammell:** Yeah, I read through it and concluded that it wasn't an issue and I haven't really paid much attention. I was originally looking at this about a couple of months ago. So, I've forgotten what those did now.

**Mike Harrison:** Right. Is this meant for like... Oh, this is meant for like motor driving, huh?

**Chris Gammell:** It's designed for any solid state switching application. Yeah, it's one of those chips that's...

**Dave Jones:** It's just designed for driving MOSFETs, right? It pretty much doesn't do anything else.

**Chris Gammell:** Unless you can think of another application for generating a high-voltage isolated 20 micro-amp supply. Yeah. Right. But it does exactly what it needs. It does exactly the right job. And in fact, they even do a version that's got an input that emulates a lead. So, you can use it as a drop-in opto coupler substitute. But this... Oh, yeah. I see that.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** That's obviously just designed for someone that's trying to update an existing design. How do they do it, though? I don't know.

**Mike Harrison:** It's like... It's magic. So, it has like DC isolation, right? I mean, it's kind of have that if it's doing...

**Dave Jones:** Well, they're using capacitor isolation. They have like tens of picofarads of capacitance in there, like large physical capacitors in there. I don't know if they actually have them on the die.

**Mike Harrison:** I don't know. Yeah. It's like a... It's a polyamide or some kind of filler, right? I mean, that's usually how these things work.

**Chris Gammell:** I must stick one in the X-ray machine and have a look. Yeah. But I think they just blast some RF across the capacitor in such a way that they can, you know, get the DC on the other side.

**Mike Harrison:** Yeah.

**Chris Gammell:** But it works, you know. It works and it's affordable. So, the only annoying thing is it's in a 0.15 inch SO package rather than a wide one. So, the tracking distance isn't quite what you'd like. But because the...

**Dave Jones:** I thought they'd put in a widey, wouldn't you? And then you could get larger capacitors in there as well.

**Chris Gammell:** Yeah. I don't know what that's about. But because of the way I've done it, because I think they say it offers basic rather than reinforced insulation. I'm actually doing a second isolation bar. I'm using an isolated... This is a DMX control dimmer. So, I'm using an isolated DMX receiver. So, I've actually got two completely separate isolation barriers.

**Dave Jones:** Nice.

**Chris Gammell:** Just to, you know... Yeah. You can never have too much isolation. Although, I'm sure there's something somewhere that would... Like a static or something that could kill you if you're not careful. Have everything floating relative to everything else. But... Yeah.

**Mike Harrison:** I mean, so you're saying each channel could be as much as... I mean, they could be as much as five kilovolts apart, right? Or I guess RMS, right?

**Chris Gammell:** No. No. I mean, they're all coming from the same live feed. But because each channel is individually controlled, the reference point for your MOSFET, which is basically halfway between your supply and your load, could be flying all over the place separately per channel. So, you need to have that separate reference for the MOSFET drive for each channel. So, if you're doing like a one or two channel dimmer, it's not a big deal. But when you're trying to do 16, it all gets a bit cumbersome. You don't really want to have 16 DC to DC converters. And so, the couple I've looked at, one uses... I think it was a four channel. It used four separate DCs to DCs. And another one, I think it was a three channel. It actually had a custom switch mode supply with multiple secondary windings on the transformer. But again, that doesn't really scale very well.

**Mike Harrison:** Yeah. Yeah. Cool.

**Dave Jones:** Cool.

**Mike Harrison:** That's great. That's a great project.

**Dave Jones:** Yep. Yeah. That's great. Does anyone make an equivalent one?

**Chris Gammell:** Not that I'm aware of. The only thing that's similar is the photovoltaic opto-isolators. And they tend to be a bit expensive and a bit slow. I didn't look that... I found this before I'd exhausted all the photovoltaic ones I started looking at.

**Dave Jones:** Sweet. Did you find that via the digi-keys and the mouses, the component supplies? Or did you go to trawl in the manufacturer sites?

**Chris Gammell:** I can't actually remember how I came across it. I think I was just Googling, you know, in my desperation when I realized this reference issue and the PV isolators weren't really going to be an answer. I was maybe looking at solid state relay schematics or whatever, and I just somehow found it. I can't remember exactly how. And then there's that moment where you find the absolute ideal chip, and then you nervously say, A, is it available? B, is it affordable? It's sold out in the entire world.

**Dave Jones:** Speaking of which, have you had any... Because you're a manufacturer. You're your own manufacturer.

**Chris Gammell:** I'm very small scale.

**Dave Jones:** Anyway, yeah, but still. Boutique. Boutique manufacturer, mate. Boutique manufacturer. And have you had any supply problems? Because I've been hit with supply problems. Manufacturers of my products, so...

**Chris Gammell:** No, but I've not really done any manufacturing this year to any serious degree. What supply problems have you been seeing?

**Dave Jones:** Oh, I'm not sure of the exact parts, but I've had multimeter delays from several manufacturers. Yeah. And their sight in, yeah, the market is just like sometimes... Sometimes, yeah, we're going back to the 1990s of your 40-week lead times and stuff.

**Mike Harrison:** I've had a little bit of it. Like, one thing that was particularly telling was I was doing some pressure sensing stuff. I think that may be mentioned on the show, but I was doing pressure sensing, and it's just like it's impossible to get anything except anything outside of like just barometric sensors. If you need any kind of like anything that's in the realm of, say, a ventilator.

**Chris Gammell:** I wonder how much of that is people speculatively buying. Yeah, speculatively buying.

**Mike Harrison:** Yeah, I think you're right. And like lead times were out like three months just to get like digi-key single sample type things. And finally, I found stuff on Aero. But like, you know, it's just everybody's racing to catch up. And I think they finally are, honestly. But it's just there's certain things in there. And then others, you know, like crystals will just be completely wiped out or, you know, just like weird stuff.

**Chris Gammell:** Who uses crystals these days? Mems oscillators. Yeah, I mean... It's crystal rubbish. Right, right.

**Mike Harrison:** Oh, they're still going to kill them on price, aren't they? I mean, I'm really just following app notes here, guys. So like whatever is in the app note.

**Dave Jones:** And is there any driving need to move towards mems, though? I mean, what's fundamentally wrong with crystals apart from, you know, any vibrational shock issues?

**Chris Gammell:** Yeah, last time I looked, they're smaller and cheaper. Oh, okay. Yeah, if you just want like a bog standard 25 megahertz oscillator, you can get something in like in a... I think they're like little square packages from Microchip for less than a crystal oscillator. More than a crystal, but less than a crystal oscillator.

**Dave Jones:** Yeah. Right. And we're talking about a packaged oscillator, not just an element.

**Chris Gammell:** Yeah, yeah, yeah. The oscillator, yeah. Yeah.

**Dave Jones:** Can you even get MEMS ones that would simulate a crystal?

**Speaker ?:** I doubt it.

**Dave Jones:** Like so you could... Sorry?

**Chris Gammell:** Not as far as I know, because I think the MEMS ones, they do like on factory calibration and they've got like factory programmable divides. I think Microchip actually do ones that you can actually get a programmer. So you buy these things in blank and program that to whatever frequency you want.

**Dave Jones:** Yep. And your burner is just a one-time programmable thing. I think so, yeah. I assume so, because you wouldn't really need it to be in-system programmable.

**Chris Gammell:** I have a feeling it might even be that DigiKey or some distributors actually program them to order some of these MEMS. I don't know whether it's the Microchip one specifically, but there's a few manufacturers that do them. I think certainly some of them, they're basically programmed when you order them, which makes sense for you, because oscillators are so many different frequencies. It doesn't make sense to... You've obviously got issues like packaging and tape and reel and stuff with small quantities. It makes sense for the distributor.

**Dave Jones:** And it's a stock problem too. Like, you know, you don't want to have to carry, you know, 8 megahertz and 10 megahertz and 12 megahertz and et cetera, 12.2.

**Chris Gammell:** Yeah, yeah, exactly.

**Mike Harrison:** See, if they're really smart, though, they would have just the one stock, like generic type. And then what they do is they like survey the market and see what the biggest need is and then just charge more for that. And then they're just putting on a program anyways, you know. It's like, oh, you need 8 megahertz. Oh, well, you know, sorry. That's $30. That's oddball, yeah.

**Chris Gammell:** I think in terms of supply, I think obviously there's been other issues. There's been factories closed. And I think SGS Thompson have had strikes in their factories. And was it AKM? They had their factory burned down. Who's AKM? They make audio A2Ds and D2As. They're fairly niche. Right. But if you use that niche, you're probably pretty much screwed up.

**Mike Harrison:** Right, right.

**Chris Gammell:** When I had that news, I did a search on DigiKey for all the AKM parts and it was like almost zero stock of anything.

**Mike Harrison:** Lead time is whenever we get around to building the new factory.

**Dave Jones:** That's the disadvantage using the boutique part, you know. If the factory burns down, the workers go on strike or that country's embargoed or something. You're up the proverbial brown creek.

**Chris Gammell:** You're screwed.

**Mike Harrison:** Well, you said the LED stuff is – so give us the state of LEDs, Mike. I mean, come on. That's your bread and butter, right? So what's new in that realm these days?

**Chris Gammell:** Nothing really. I've finally actually got a job where I'm using the – my custom wants to use the WS2812 type devices, which I've resisted for a long time based on just quality. But it's their problem. If these things die, then that's not my problem.

**Dave Jones:** Why did they insist on that? Is it because they've heard about it everywhere? Cost?

**Chris Gammell:** Cost. No, it's just cost. I think this particular project is fairly tight on cost because, I mean, quite a lot of the stuff I've been doing over the last year or two has been literally getting TI drivers and, you know, brand name LEDs and sticking on a board. Where, you know, in theory, if someone made some decent quality, you know, dependable loads of built-in drivers, then, you know, we'd have used those. But all there is is the race to the bottom Chinese stuff, which in the past I've had issues with in, you know, various issues. And to the point, I certainly wouldn't trust them.

**Mike Harrison:** Do you ever have to do, like, proving it out to your customer and be like, ah, I did an accelerated life test on this, you know, certain type of part and be like, no, that's crap? Or is this more anecdotal?

**Chris Gammell:** Yeah. Yeah, well, I mean, yeah, the thing is, you know, most of these are one-off projects. We have a finite amount of time to get this project done, one opportunity to build it so we don't have the time to do the life testing and all that sort of stuff. We just need to build something that we know is going to work with a very high degree of confidence.

**Mike Harrison:** So you've got to do the testing and then sell the report, you know, like just be like the Mike Harrison White Wing LED report.

**Dave Jones:** Yes, and charge $10,000.

**Mike Harrison:** Exactly. Yeah, like that report that Dave and I talked about a couple weeks ago or months ago, right? Those things are, that's big money, man. So like, and you're the name. You sell 10 copies, you know.

**Chris Gammell:** Yeah, the problem is you spend two months doing accelerated life testing and your report says these are crap, you don't want to use them. And where are you then?

**Mike Harrison:** Disqualified. Disqualified.

**Dave Jones:** Did your customer actually do the technical stuff to actually vet that's the product that they, that's the lead that they wanted to use? Or did you?

**Chris Gammell:** No, I'm not.

**Dave Jones:** They just said cost, cost, cost. And you went, oh, geez, we have to use these.

**Chris Gammell:** Yeah, I'm not sure about, yeah, I'm not really sure the whole process. All they said is, you know, here we send you a weird of these things that we want to use to test.

**Dave Jones:** Through some process you're not aware of. Yeah. Right. Yeah.

**Chris Gammell:** I don't, I don't know what. Yeah. These are, I think, I think they're RGBW ones. But yeah, again, I say fine, you know. And if leads die, it's not, you know. All I said to them is make sure it's easy to replace them if you need to.

**Mike Harrison:** Right, like some kind of like eject socket or something, you know, you push the little button, they all pop out and you put new ones in, you know, and you turn to just push them in.

**Chris Gammell:** No, not quite. Yeah, we're talking, you know, we're talking like, you know, the tape, the ready-made tape stuff. So assemble it in such a way that you can just pull a whole strip out, plug another one in relatively easily without dismantling the entire installation.

**Dave Jones:** Would a socket exist? Would there be an exotic socket for?

**Chris Gammell:** No, I mean, we're talking lead tape rather than individual devices. I mean, the socket would, if you, you know, with individual sockets, the socket would cost more than the device.

**Dave Jones:** Oh, yeah, no, of course. Of course it would.

**Chris Gammell:** And add even more points of failure as well.

**Dave Jones:** That's right. But there might be some niche requirement out there that, you know, needs a socket or something. Yeah.

**Mike Harrison:** How often is stuff coming to you? Like, so the WS-2012 is a good example, right? I mean, it's like people have, there's lots of great prototyping kind of examples out there. People, you know, same kind of things happen with Arduino or other type of, like, example things that are out there that people can prototype with. And then they come to you and they say, here's the answer. And is it usually cost-based then? Or is it more like, you know?

**Chris Gammell:** Yeah, it depends. It depends on the customer. I mean, I certainly in the past, I've had basically someone that's prototyped something on Arduino and then wants to scale it. You know, it's the classic, you know, one of these days I'll be meaning to sort of do a video of something saying Arduino does not scale. You know, okay, we've baked these things with sort of 200 LEDs. Okay, this installation is just 20,000. And things, you know, things like power, you know, power management is the first thing and bandwidth and so on. But, yeah, the customer I do most of my work for at the moment is, you know, that they are a lot better in getting me involved earlier. They understand a lot of the issues a lot better.

**Mike Harrison:** Right, like knowing where the value lies and someone like you of like making it a hardy system, making it like reliable, making it, yeah, and manufacturable. Those are all important things.

**Dave Jones:** And by saying Arduino doesn't scale is not, you've got to qualify that by saying it doesn't scale in this particular scenario when you want to drive 10,000 LEDs. It's not that you can't take an Arduino design and then repackage it cheaply because you can do that because it's open source. You just strip back the micro and, you know, program. It's when you want to expand the whole system, so to speak.

**Chris Gammell:** So, yeah, yeah, yeah. That's a very sort of overarching statement of, you know, it's, it's, I say, it doesn't happen so much nowadays, but certainly in the past, you know, they say, okay, we've got this thing prototype. We know it's going to work. And, you know, we now want to make like another, well, it might even be something as simple as, you know, they've dashed something up with off the shelf things. And they want to make 200 of them and don't understand that it's going to be much easier to stick everything on one PCB and sort out all the connectors and everything. Then get a hundred Arblinos and put cables everywhere and do all this sort of.

**Mike Harrison:** If you just wire from here to here four times for each board and make sure the wires are really good. Yeah. It's just like, oh, God, no.

**Chris Gammell:** Yeah. Yeah. Yeah. Actually, that, that, that phrase, when you said really good, one thing I told a customer a while ago, I can't remember which project it was, but it was something which it was a fairly large, large, it's like a hang on the wall artwork. And they came up with this potential way of putting it together, which included the words very, very carefully. I think it was to do with gluing something. And I said, any, you know, any instruction that includes the words very carefully. No, just no. No, because, okay, you know, you might care about it, but the intern you've got working over the, you know, over for the college holidays isn't going to care about it as much as you do. And they're not going to take as much care as you do. Yeah, but it works for like a Mars rover and stuff.

**Dave Jones:** Assemble very, very carefully, you know, this one device that you're going to.

**Chris Gammell:** Yeah, but the people assembling it very carefully have probably been trained for several years as to exactly what very careful means.

**Dave Jones:** Oh, boy. Can we put the photo for this one? Can we put like that famous satellite in the clean room that fell over? Oh, it fell over.

**Mike Harrison:** Oh, my God.

**Dave Jones:** I love that one. I've got to trot that one out again in 2020. It's like, yeah. Yeah. It was like a weather satellite or something. And it just, yeah. They did a tilt. They told it and somebody forgot to put the bolts on. If you haven't seen the photo, it's just.

**Chris Gammell:** That reminds me, the photo hasn't come out yet. But you may have seen that tweet from Daniel from Keysight saying apparently a forklift went through an X $100,000 oscilloscope or something. No, I haven't seen it.

**Dave Jones:** Really?

**Chris Gammell:** There isn't a photo yet.

**Dave Jones:** So it was on a pallet or something? It was in the box on a pallet?

**Chris Gammell:** Or the tweet was simply something like, so apparently a forklift went through the side of an X $100,000 UXR oscilloscope. That was it. And everyone tweeted, picture, it doesn't happen. He said, I'm working on it. I'm going to get on that.

**Mike Harrison:** That's got to be like a public safety campaign at that point of like, you know, friends don't let friends drive forklifts.

**Dave Jones:** Oh, that's great. Boy. All right. Should we go through our list? Sure. Oh, yeah. Well, we didn't send it to you. We talked about it before. This is like top of the list, which is I posted a link. I can't remember where I got it from. But anyway, it's from the China Law Blog. And they're talking about how.

**Chris Gammell:** Oh, yeah. Yeah.

**Dave Jones:** It's perfectly. The title is it's perfectly legal for your Chinese manufacturer to copy your products. End of story. Unless you have a really in-depth binding. Don't copy our shit clause in your contract. Oh, that's what we forgot. Oh, man. But unless you're Apple or somebody, you're not going to have, you know, a dedicated contract for a manufacturer or something. Targeting different areas. Please, you know, unless you're like a big player with a legal team.

**Chris Gammell:** Yeah, that's true. But unless you're Apple, what are the chances of the Chinese company is actually going to want to copy your widget? I think it is a bit of a click-baity title. Sure. Basically, it just says most of it really you need to do slightly different things than you might do with other companies. Like using something or something. It was not an NDA. It's something else they called it and register a Chinese trademark and a few other things. But I think that was probably a little bit more. A little bit on the click-baity side. Yeah, it is. I know.

**Dave Jones:** They're not going to want to copy your little Arduino widget or something. But if it's got publicity behind it, like it's a big Kickstarter or something like that, there's been many articles over the years where these Kickstarters, you know, they've got in, you know, $10 million and everything. And they go to the Chinese manufacturer because they need to, like, assemble it cheap. And they all of a sudden find that it's on the market before they can even release it because the manufacturer is just.

**Chris Gammell:** Oh, yeah. The classic Kickstarter. Kickstarter AliExpress syndrome. Although I'm not sure how many times that's actually happened. I know it has happened, but I'm not sure how common it is in practice.

**Dave Jones:** I've seen it a handful of times in the Kickstarter realm. So, you know, but it only tends to happen to the big ones. They're not going to bother to copy some little, you know, tin pot Arduino thing with a thousand backers. You know, it's just. Right.

**Mike Harrison:** Right. And I think at that point, too, the people that are trying to get it cheaper in the first place are like, all right, great. You know, don't have to do manufacturing now. Great. Awesome. I mean, like that's usually wherever the profit motive is. It's like if it's like just trying to get a thing out there, that's different than, you know, trying to make it a business or make it a, you know, a future thing, I think as well.

**Dave Jones:** It is a clickbaity title. I agree. But it's worth keeping in the back of your mind that. Yeah, I think this is a thing. You know.

**Mike Harrison:** Yeah. I was thinking about this the other day with, you know, like, you know, it's very normal for me to now send off gerbers to just whomever. Right. I mean, it doesn't have to be a China board house or whatever. Yeah, you don't even think about it. But it's really just like floating out there. Right. And, you know, these are things that I'm under NDA for. It's not like the I'm not doing anything crazy. I'm not doing anything, you know, it's but it's just IP that I'm doing for a client, whatever. But it's, you know, it's out there. And there's very little likelihood that anyone would ever do it. But it's just it's just a weird thought to think like, oh, I just kind of float this thing onto the Internet. And then a couple weeks later, I get I get fiberglass back. You know, it's just like it's just a weird concept sometimes to think about that. Got to be careful.

**Chris Gammell:** Yeah, but it's just a it's just a board layout. I mean, I'll just strip all the bits off and scan the board and they've got it anyway.

**Mike Harrison:** Yeah. And it comes down to how much you want to focus on it. Right. I mean, like how much you want to. Yeah. If the bombs there, if the layout, the schematics there, whatever. It's like, yeah, I don't know.

**Dave Jones:** But from an IP point of view, Chris, with your clients, you've got to be careful because if you get it made by some of these low cost PCB manufacturers, they will actually default. Your actual design becomes public. I can't remember. There's a couple of the board houses out there that, yeah, if you use your low cost assembly service, you basically sign away rights that they can make this public or something. I can't remember. Is it easy EDA or somebody? It's one of those, you know, it's one of these houses.

**Mike Harrison:** You're saying it's like one of the marketplace solution type of things? Yeah. Yeah. Oh, interesting.

**Dave Jones:** Yeah. It automatically defaults to public or something unless you choose their higher price service. So once again, it's something to be conscious of.

**Chris Gammell:** Yeah. But that's not unique to Chinese. There's a story from a guy in the UK that I spoke to a few years ago. He was doing boards which were like fairly artistic PCBs. You can probably guess who I'm talking about. I won't name him. Like very artistic sort of PCBs. And he had a commission from, it was something like a fashion brand, like a really, the sort of people that really care about keeping things under wraps. And he sent this to a UK PCB manufacturer and who, again, who shall rename nameless, but I think anyone that's used them will know who I'm talking about.

**Dave Jones:** Because it looks so novel and nice. Yeah. Exactly. Yes. Oops. That's not good. Yep. Yeah. Oops.

**Mike Harrison:** Yeah.

**Dave Jones:** Oh, yeah. Yeah. You've got to be careful about, like, I've had lots of companies approach me and say, oh, look, you've reviewed our product. Can we put you as a case study on our marketing website? You know, can we tweet out? You're our case study. And it's like, no. It's like, yeah. Boy. And, well, they asked. At least they asked, you know. So, but my end result is public, of course, with the video, which they can, you know, they're free to post. But, you know, not put, you know, not plaster me all over their, you know, story page or whatever, you know. Right. Yeah.

**Mike Harrison:** Because then it's like an endorsement at that point, too.

**Dave Jones:** Yeah. It's like an endorsement. Like, he chooses to use our service. You know, it's like, holy shit.

**Mike Harrison:** You chose with your wallet. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Yeah. At least I'm sort of very fortunate. None of my stuff is, it's rarely confidential. And certainly once it's out there and been installed, you know, I can talk about it. All my customers care about is, you know, this thing works. And they're not really interested in the IP side of things. It's just quite useful.

**Dave Jones:** Have you had any at all that have said, no, we don't want any, this is our secret source. We don't want anyone to know. And you can't reuse this tech in anything else.

**Chris Gammell:** No. I mean, no. I literally, yeah, the world that I've been working in recently, nothing has ever come remotely close to that. Probably the closest I've had was a customer that just wanted to have enough to be able to rebuild spares if they ever needed to. This was actually from museums. And the museum had a policy of anything like that. They needed to have all the information they needed to do repairs themselves or if necessary, get new hardware built. That's really been it. None of my customers have ever really been interested in owning any of the IP that I've generated in achieving what their vision was.

**Dave Jones:** Right. Because I've got a story of a company who shall remain nameless, who had two employees at the time. And they were working on a product.

**Mike Harrison:** Is it your company, Dave? Is that what we're talking about here? No, no, no.

**Dave Jones:** And they did a Kickstarter. And somebody and one of the employees, former employers, saw the Kickstarter and just so happened to have a very similar product also kickstarting at the same time by pure coincidence. You know, it just happened to enter that same market.

**Mike Harrison:** Like actual coincidence or like they said it was pure coincidence?

**Dave Jones:** Well, this company had been working on it for years, actually longer than this other company. So it was like, anyway, so the former employer of this person started to contact them and say, you've stolen our IP. How dare you? You know, you're reusing like, you know, geez, we want you to tell them to stop releasing this product. And it's like, yeah, nah, not going to happen. It's like, because there was no IP stolen at all. It was simply just a similar product in a similar market on Kickstarter at the same time. You know, it's just one of those coincidences. But yeah, they took it as this employer, employee had stolen, you know, was reusing their knowledge or their IP code possibly from that. So it happens.

**Mike Harrison:** Yeah. I mean, when that stuff gets, I mean, when it gets to lawyers at that point too, it's like, man, that's a tough thing to prove, but it's also, it's expensive for everyone. It's a mess.

**Dave Jones:** Oh, no, it wouldn't have gone to that. It would have been public.

**Mike Harrison:** More than your Kickstarter profits will probably cover.

**Dave Jones:** You know, yeah.

**Mike Harrison:** Yeah, right, right.

**Chris Gammell:** Kickstarter profits?

**Dave Jones:** It would have been a public battle at 10 paces, you know, it would have been. Yeah, right, right. Twitter at 10 paces.

**Mike Harrison:** Right.

**Dave Jones:** Oh, boy. But yeah, those sort of things happen. So, yeah.

**Mike Harrison:** Yeah. Are you, Mike, are you still a PIC32? Is that you're still your part of choice these days?

**Chris Gammell:** Yeah. Yeah. Yeah. Used one in, used another, another different PIC32 in this demo doing sort of 16 PWN channels or bit bashed in software using some like 50% interrupt loading, but it does the job. It's not going to do anything else. So why not?

**Mike Harrison:** Are they updating that line at all though? I mean, like what's, what are they doing with that?

**Chris Gammell:** Yeah, this is a new, I mean, I tend to know, just notice new ones when I've just come across something that I run out of steam. So I don't actually know how new this device is, but I just needed something, add 64 pins and had sort of interrupt shadow registers. So I looked at it and this one was like a slightly newer version of their PIC32 mm range. And yeah, it does the job fine. No error to speak. Yeah, actually, pure chance. A feature that I did really late on. One of the issues obviously with mains dimmers is it's rather difficult to short, protect them against short circuits because you get rather high fault currents. So what I decided to do, well, this thing has got a fuse in it, but obviously the MOSFET would blow to protect the fuse in most cases.

**Dave Jones:** So a lot of people would have missed that joke there. Hall effect.

**Chris Gammell:** But you can get these neat isolated Hall effect current sensing chips. It's basically, it's like an SO8 with like an internal shunt. It's like a 0.5 milli-ohm shunt or something, but it uses a Hall effect sensing. So you can get, the one I'm using has got like a plus minus 10 amp range. So what I wanted to do is have this, so as soon as it detects an overcurrent during the cycle, it would immediately cut the drive so that if you turn the thing on into a dead short, as the current starts rising from the zero crossing up the half cycle, it will actually turn off fast enough to not smoke the MOSFET. So basically the output from this current shunt, it's quite nice. It's fully isolated. You get like 0 to 3.3 volts is your minus 10 to plus 10 amp range. So what I want to do is basically feed this in so that if I detect the current going over a certain amount, it will instantly cut off the outputs. One really neat feature this chip has got, it's got a thresholding ATD converter. So it's got a comparator as well, but obviously because it's an AC signal, you want to sense both the positive and the negative half cycle. So what you want is a signal that will tell you, is this voltage either higher than X or lower than X minus something if it's outside that range? Because the output of the current sensor is centered around half your supply route. It's centered around 1.65 volts. And then it goes higher or lower than that as your AC current increases. And one neat feature this chip has got is it's got an AC converter where you can actually give it two limits and it will set a flag if the voltage goes outside those two limits, which is exactly what I wanted. And I only really discovered that after I designed this chip in and decided to put the current sensing in later, which is another one that's really nice. It's a bonus, yeah. It's a serendipitous thing. Yeah, because I could, you know, I probably could have done it with a comparator, but like every half cycle, I'd have had to switch the parity and it would have got quite messy. But it just happened to have this exact function that was just absolutely perfect. It took a while to figure out how to configure it to actually do it. But once I configured it, it worked fine. But now I'm still a fairly major pick fan.

**Dave Jones:** Have you had any clients demand that you use a certain processor? No, I don't care.

**Chris Gammell:** No, they don't care. My client wants a box that they plug data in and get pretty lights out the other end. You know, it could have a valve in there for all they care.

**Mike Harrison:** Yeah, I mean, I'm just curious in general, too, about like, you know, just from your perspective, what you're hearing, you know, obviously, Microchip owns Atmel now, too. And just like, you know, a lot of their portfolio is legacy based, right? It's not like PIX going away anytime soon. But I'm always just curious about like, you know, are they putting like resources towards new families and stuff like that? It sounds like there is new stuff coming out that you're seeing.

**Chris Gammell:** Yeah. I mean, I only tend to start looking when I have a requirement that needs something. You know, most of my stuff isn't particularly demanding. So I've occasionally glanced and seen some interesting stuff. I don't know how they compare with other things. I'm sort of fairly glad that I didn't go the STM32 route because apparently they're the ones that supply problems at the moment quite badly. But one other nice thing is one of my customers have actually got people in-house that can do sort of low-level software and so on. One of the nice things about PIX is the whole dev tool thing is that I can just give them one project. They just install MPLABX, load my project, and they're away. I write them a little framework. And they just add their code to generate their content and off they go. They don't have to spend ages with different tools.

**Mike Harrison:** You want to install Eclipse, but make sure it's the right version of Eclipse. And then also, here's all the plugins you need to get. Make sure those are perfect and your Ubuntu is up to date.

**Dave Jones:** Oh, I've got that famous video. I've got that famous video of David too installing like an hour video just to install the tools used for the app development of the 121 multimeter. So it was like there's so many different tools to install. It's like, yeah.

**Chris Gammell:** Exactly.

**Dave Jones:** Yeah. It's like the extreme end of what can happen when you do that sort of thing. Otherwise, yeah. No, it could have been done. Sorry. No, it was just the firmware. No, sorry. It was just the firmware. It was the firmware for the power supply. Just, you know, firmware for a ST micro.

**Mike Harrison:** Yeah, but he was doing C++ and weird stuff too, right? He was doing C++, but it could have been done. Stuff that was out of the normal. Yeah.

**Dave Jones:** The point is it could have been done, as Mike's saying, just in the vendor package and that's it. It's not as nice from a software development. You know, if you're a software development aficionado, right? It's not as nice. But as Mike said, there's advantages. You can just go, here's the package file, open MPLAB or open STTools and that's it. It's done. I don't know, guys.

**Mike Harrison:** So here's the thing. Here's what I spent some of my week last week doing was installing onto a VM. Um, uh, so, uh, simplicity studio, which is the S the scilabs, uh, tool for like all their firmware. They migrate, they, they now have a version four and a version five with an upgrade path. And it was like, okay, I'm going to go install all this stuff onto a VM so that it's like locked down forever because I'm just worried. It's just not going to work at some point in the future. And it's like a client project. So that is the downside. I think is like, if, I mean, I think that microchip has been pretty good about, you know, compatibility across time, but I'm just, I'm pretty nervous about that sort of

**Dave Jones:** stuff for myself because I was, well, kind of surprised and not surprised when I did my thousand and 24th video, I took, because it was a thousand 24, it was one K. Right. So I did, I took an old, uh, pick micro assembler code from like 20, 25 years ago. Right. That I wrote and I reassemble it or I installed the latest MP lab. It was for a 16 F 84 or whatever. I pasted the assembler code in and I hit assemble and it just. It, it worked and I programmed my chip and it just worked like 25 years later. It was like fantastic.

**Mike Harrison:** Yeah. Yeah. But that worked because the F 84 is still a popular chip. You know what I mean? Like it's like, it's, it's still, I think the bigger concern is if the chip becomes unpopular. Right. And so if I'm using a part that's unpopular, obviously that's on me, but like that, that's probably the bigger risk. I think, you know, in terms of future compatibility and stuff like that.

**Dave Jones:** So there's often there, I can remember when I, I developed on that 16 F 84, but in production, I actually used the cheaper at the time. Cause you know, those flash parts, newfangled flash parts are expensive. Right. So I use the 16 C 61. Right. So I use the one time programmable, uh, 61 version for my production boards. And it was like, it was changing a couple of like bits in the, uh, you know, fuse bits or whatever. And that was it. Like it, it really was very minimal.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Change. So, yeah. And I just completely changed the chip. It was completely pin compatible, you know, and boom. So I just used a different chip.

**Chris Gammell:** Yeah. Microchip being fairly, and certainly in terms of dev tools, there's only been one really major change when they went over to MP lab X and it's a bit of work taking an old MP lab project, but a lot of that shifts down to which libraries get included by default and stuff like that. And in terms of the devices, you know, they are pretty good. They've done a few pinout changes. The pinouts are pretty much stabilized again. They, when they went from the, like the 84 type devices and then they moved the power. Well, I think it was when they brought out the eight pin devices, they decided to put the power pins at one end and those have pretty much stayed there. So at least you go up to about the 20 pin ones. They're, they're very compatible. And the fact that, you know, the nice thing is that a lot of the, once you start writing in C, you know, you could actually write a C program, which could run on like a, uh, an SOT six and like a hundred pin QFP 32 bit with basic just changing the configs and not much else.

**Mike Harrison:** Yeah. Right, right, right, right. Timer, timer, blinking LED.

**Chris Gammell:** Okay. Okay. Very steady, simple program, but a program nonetheless. Yeah. And, and, and programing with the same programmer.

**Dave Jones:** How much memory can you get in those little, uh, six pin SOT 23s these days? It's still the same?

**Chris Gammell:** Um, I think it's five, 12 words. I think it's five, 12 words. Who needs more?

**Dave Jones:** Oh yeah. You can do a lot. You can do a lot in five, 12 words.

**Chris Gammell:** I, I, I, I've, I've got a thing that I used a lot, which had a serial bootloader and the application code in five, 12 words. Yeah. And that was all in C. That wasn't a sample. That was all in C. That's great.

**Mike Harrison:** I was looking at an app note the other day for this RS 45 thing I'm doing. It was just like, you know, there's a RS 45 transceiver and it's talking to a chip and

**Dave Jones:** I'm like, Oh, are you talking RS 485?

**Mike Harrison:** 485. Yeah. That's right. Like a max 485 or similar. Yeah. Yeah. Like Mike uses that on a lot of his projects too. Right. And, uh, but one of the things is like a maximum, it was like a maximum app note. And I was just like, you know, just searching Google images for app notes, whatever. And it's like, I forget what the, I think it was a pick, but then it was like, and use this external UART chip. And I'm like, Oh, external UARTs. That's the thing. Yeah. Like that used to get me a bit bang to the external UART.

**Mike Harrison:** I never, you guys, I've never had to deal with that ever. Like that's not me. You've never had to use an external UART. No.

**Dave Jones:** Oh, you young whippersnapper.

**Mike Harrison:** I know. I know.

**Mike Harrison:** I think you mean young. I think the other thing too, is that like, I wasn't, you know, like the beginning of my career, I was just doing analog stuff, you know? So it was just like, I wasn't touching any of this. And so, yeah, or I was using more slightly upmarket parts. Yeah. I think Chris is a bit young for that.

**Dave Jones:** That's probably been for the last 20 years, maybe 20 years. You haven't had to worry about it. Yeah. Everything has an internal UART, but if you start talking 20, 25 plus years ago, then yeah. Right. It's common.

**Chris Gammell:** It's the, it's the microprocessor versus microcontroller. That's really when that sort of happened.

**Mike Harrison:** I don't miss it guys. I don't know. I'm not like, I'm not like Jones and the, you know. Yeah. Have an external UART. There's no, there's no rosy colored glasses on that one. You know?

**Dave Jones:** On that, on that 1K one I was talking about, I had to bit bang my own I squared C port. Cause there was no such thing as I squared C built into a micro back then. Yeah. That was unheard of. Hardware I squared C.

**Chris Gammell:** Yeah. That's simple enough. Unless you need to do, be a slave. That gets really tricky doing I squared C slave. But master it's pretty simple. Although it always seems more complicated than it ought to be.

**Dave Jones:** Yeah. The chip I had didn't even have a UART. So the, you know, the 16F84 didn't have a UART. Yeah. Right. Still doesn't. I don't think. Oh, no. I think you can get maybe the A version does or something.

**Mike Harrison:** No. That may have been the part that it was being used there. I think it was like.

**Chris Gammell:** Not the 84, but the microchip, it's only, I mean, probably maybe last, I don't know, I couldn't quantify it. But microchip took quite a while before they started putting UARTs in their lowest end devices. There are some now, but it took quite a while.

**Dave Jones:** They lagged a lot, you know, because that's why, you know, that's another thing, you know, a lot of people used to move to the Atmels or the MSP430s or they moved to other ones because they had, you know, a couple of UARTs in them.

**Chris Gammell:** Yeah. But now they've done, there's an APM one that's got two UARTs, I think. So, you know, they've caught up on that.

**Dave Jones:** And I used one once, it was a 16, no, it was a 24F series pick and it had a couple of UARTs in it and I was using those and it was like, oops, they were swapped. They were actually, it was a silicon bug. They actually swapped it and it didn't get through QA. Like, sorry, it got through QA. I was wondering why my serial port wasn't working. And sure enough, I downloaded the latest data sheet and sure enough, right down the bottom at the E-Rata number 50, it says, oh yeah, by the way, serial port one is actually serial port two of Weisford. You know, it's like, hey, come on, come on. And the pins were swapped. Another E-Rata, I don't know the work experience, you know, kid must have done this chip. And the pins were swapped. So the TX and RX were actually swapped in the register or something. It was like, are you kidding me? And they just casually dropped this in the E-Rata, you know, six months after release.

**Chris Gammell:** That old TXRX confusion problem.

**Dave Jones:** Oh boy. Yeah. But they're coming out with so many variants. I mean, it must be like impossible to thoroughly vet everyone. It's just.

**Chris Gammell:** I'm still staggered by how many different picks there are out there. And I just don't understand, you know, they do like, even some of the low ends, they do like one with 512 words and one with 1024. And it's about a cent difference in DigiKey. Why? Why?

**Dave Jones:** Because it matters in, you know, a million volume. And some customers actually requested that. They've requested, look, we don't. And microchips say, yeah, if you buy a million of them, we'll.

**Mike Harrison:** Yeah. I bet. I bet that could have been though. Like it could have been like the old one was 512. They upgraded because they had the space on the die or whatever. And then, but then the one that, you know, the old company that's using it, like, no, you're still making that old one. You know what I mean? Like they're.

**Dave Jones:** Or maybe it has it on the die. Maybe it actually has the 1K on the die, but they just.

**Mike Harrison:** Cut off one of the bits. Laser it. Yeah, I'm sure it does. You know? Yeah.

**Dave Jones:** So.

**Mike Harrison:** Yeah.

**Dave Jones:** Yeah. In fact, I know, I know for a fact that happens in the ST chips. Cause David too, he actually discovered during development of the micro supply. One of the chips, we had like 128K version, but there was also a 256K version. He discovered how to actually toggle a couple of.

**Mike Harrison:** The unlock.

**Dave Jones:** Bits somewhere. Was there a little USB plug you had to. There was an unlock. There was a software unlock. And he actually discovered how to access the 256K. Cause he started writing, you know, fiddling about, started writing to these memory bits above, like actually directly addressing the memory above and found he could read and write it. And it was like, oh, you know, it's there.

**Chris Gammell:** And it didn't get reflected down somewhere else.

**Dave Jones:** No, no, no. He double checked that. No, it was genuinely. Yep.

**Mike Harrison:** Yep.

**Dave Jones:** Cause, cause we were right on the limit and we had to get there. And it was like double the price or something, you know, for the 256 versus 128. And he went, look, I can actually, and I think he actually compiled into the larger memory space somehow. So like, yeah.

**Chris Gammell:** It's always a bit dodgy. Cause you then suddenly might find they do it differently. And that memory suddenly isn't there anymore. Yeah. Oops. But I think all the, pretty much all the pics have got some factory flash programming, like calibration data. So I'm sure there's bits in there that change some of the device configuration. I'm sure we just decap a couple. You'll find the dies are probably identical.

**Dave Jones:** Have you been using security on these chips? Are any customers worried about people still in the code?

**Chris Gammell:** No, again, you know, no. I mean, the customers just want the box to do the job. They want it done. They're, you know, they're not really interested.

**Mike Harrison:** How about your x-ray machine? I mean, so you still have that x-ray or no?

**Chris Gammell:** Yeah, I've got, I've still got the Faxitron, which is, you know, it's a very small, it's very high resolution. Unfortunately, it's got fairly low. It's only goes up to 35 kV. So it doesn't penetrate through much in the way of metal, but for chips and thin PCBs, it's quite fun.

**Mike Harrison:** I still haven't sent it to Dave, but I got that. I finally got that thing I mentioned on here. The one, the local shop that I work out of, they had the, this CT scan or whatever. And I got to, maybe after this, I can screen share with you guys. It is just so cool to look at, like the high density VGA and like being able to see through the different levels and stuff like that. It's so cool to see. So yeah, it can be really useful. I mean, I don't know how much, are you doing a lot of fine pitch stuff these days or is it just more kind of industrial style? Not really, no. Big pitch things like I do.

**Dave Jones:** He's got to assemble them himself, Chris. Yeah, true. He's not gonna.

**Chris Gammell:** Yeah, right, right, right. Don't make it tough.

**Mike Harrison:** Don't make it hard for himself. Come on. Yeah.

**Chris Gammell:** Yeah. Half mil QFPs is the normal limit. One thing I've been meaning to do with an x-ray is put a stepper motor or something so I can do like a rotation and do a sort of CT-like type thing. But add it to the list of things I'll probably never get around to doing.

**Dave Jones:** Can't you just buy like an off-the-shelf turntable, like an off-the-shelf XY table or something and just whack it in there?

**Chris Gammell:** Yeah, yeah. I've actually got the guts of an old XY plotter that I've earmarked for it, but I just haven't got around to it.

**Mike Harrison:** I think the hard part with that would be like reconstructing the image, right? Once you've made it, then you'd have to like stitch all that stuff together. That would be the hard part, I would think.

**Chris Gammell:** Yeah, I'm thinking literally you just take a number of shots and then play it back as an animation so you just get the rotation and you let the brain join the dots.

**Mike Harrison:** Yeah, you can just slow-mo it or something like that or maybe even do like multiple frames.

**Dave Jones:** Everyone asks me why I don't get an x-ray machine. I believe you need a license here in Australia to own an x-ray machine. Right.

**Chris Gammell:** Yeah, it doesn't surprise me. Yeah. The law in the UK, I actually looked into it and it's a little bit vague. My interpretation, well, basically, again, this may have changed, but my interpretation was the wording sort of implies that this only applies to anything that's done in the course of business.

**Dave Jones:** X-ray for a hobby, yeah.

**Chris Gammell:** They didn't think about people having their own private x-ray machines when they wrote these regulations. No. No.

**Mike Harrison:** Yeah, right. You're not doing it as a service, right? You're not like x-raying people or animals or anything or even other people's boards. It's just your own, you know?

**Chris Gammell:** I think the fact that it's a completely self-contained unit may also be significant. You know, you'd have to defeat a couple of interlocks to actually do anything with this. But yeah, I never looked into it. I looked at this ages ago when I was looking at buying a dental x-ray or something. But yeah, it's one of these don't tell situations.

**Dave Jones:** One of the things here is why I can't, like I couldn't even get one if I wanted, like if I tried, because they don't come up on the second-hand market here. I'd have to buy new and have a license because you're not allowed to sell them on the second-hand license. Well, technically you are allowed to sell them on the second-hand market, but you have to ensure legally that it's sold to somebody with a license. So that's basically why you never see them here on the second-hand market. You'll never find one on eBay or, you know, on Gumtree or something like that. You just won't find it.

**Mike Harrison:** Well, it's also expensive to ship, so they wouldn't be over there unless they're being used probably, right?

**Dave Jones:** No, but you won't even find one local. You know, like the regular Graze Online, like the company's shutting down or something like that. The auction houses know they're not allowed to auction off these x-ray machines. So, you know, they just don't do it. You'll never find one. And that's the thing. It just has to get scrapped or...

**Chris Gammell:** Yeah, I'm just looking at eBay, Australia now. It's all China, USA, various other places. I can't see any local. Dental x-rays are the usual ones that you get.

**Dave Jones:** Yeah, yeah. You get... Yeah, I think you can get portable little dental x-ray machines from import from China. I don't think they'll try and stop those, but maybe, you know, but not like a real one.

**Chris Gammell:** Yeah, actually, I knew there was one that was a bit of a sort of semi-scandal in the UK a few years ago. There was one really popular handheld dental x-ray machine that had horrific leakage to the user. And the... Why is my tummy all warm? I don't get it every time I use this.

**Mike Harrison:** I get a bellyache. Yeah, exactly.

**Chris Gammell:** The UK regulator did get involved in that. I can't remember what the upshot was, but they tested one of these things and said, you know, this thing's horrific. I think they send, like, information out to all the dentists and everyone saying, you know, this thing is lethal. Don't go near it.

**Mike Harrison:** Oh, wow. You could, like, wear, like, you could, like, make a belt or you make, like, it'd be, like, a new artistic thing where you're, like, weaving your own, like, clothing, but out of, like, leaded solder, you know, like, multiple layers. I'm curious about the...

**Dave Jones:** Because my little boy busted his arm, had to have a look, a full arm cast, you know. And he's had, like, half a dozen x-rays on that now because every time he goes back to, like, check the progress of it, they'll x-ray it, they'll x-ray it again, x-ray. Like, half a dozen x-rays. You know, when I was a boy, it was, like, x-rays were, like, oh, a big deal. This is taking x years off your life if you have an x-ray. I guess they're getting better at, like... Yeah, targeted doses or something. They're more efficient. They can lower power or something.

**Chris Gammell:** Well, yeah, so I think because they use, you know, they use electronic sensors rather than film, so I imagine the doses have probably gone down quite a lot. I don't know in detail, but I'd imagine that's one factor.

**Dave Jones:** Yeah, because they wouldn't just, you know, x-ray a little kid half a dozen times, you know, just for a...

**Chris Gammell:** Yeah, well, maybe they figure that since Chernobyl, the average background's gone up enough that it's less of an issue.

**Mike Harrison:** Or Dave's son is going to be in a superhero at some point. At some point, it's just, you know, the mutation happens and you become an X-Man, you know.

**Chris Gammell:** Yeah, you're not that far from Fukushima either, are you?

**Dave Jones:** So, Mike, any new things on the EV front?

**Chris Gammell:** Yeah, I've started trying to take a few bits of my car apart. I tried to get the lid off the onboard charger, but they've got some goopy, gaskety stuff, but I couldn't easily get it off. But I actually... There's a company that basically handles all the insurance write-offs of cars called Copar. They operate worldwide. And I did actually find a Kona that had basically been front and back-ended. And I was seriously thinking about sort of trying to get hold of it. The problem is it's what they call a Category B, which means that it's not allowed to ever go back on the road again. And to buy one of these, you need all sorts of licenses, like waste disposal licenses and all this sort of thing. And I did start making inquiries to a local sort of breaker guy to sort of see if, you know, we could figure out a way of basically him to buy it on his account and sell it to me.

**Dave Jones:** And just sell you the good parts and sell you the interesting parts.

**Chris Gammell:** Well, I mean, it didn't go quite... Because something else got in the way and I didn't follow it up. But basically, what I'd ideally wanted was him to sort of buy it, chop out the VIN number, which I think is mostly what they need for their paperwork, and just dump it at the back of my place so I can then just dismantle it at my leisure.

**Mike Harrison:** So you could just become like a wrecking yard or something like that. You know, like that's what you needed to do.

**Chris Gammell:** Although it was heavily damaged, it did actually still run and drive. So, you know, I was thinking of, well, okay, you know, do some reverse engineering on the CAN bus, keep a few spares for mine, sell a few spares and probably sell the battery to someone wanting to do home storage. And the price it went at, I could almost certainly have easily at least broken even on it.

**Mike Harrison:** And Mike, can you remind people of the model you have as well? You said Kona? Is it Hyundai? Hyundai? Yes, a Kona.

**Chris Gammell:** Which year is it? Hyundai Kona, yeah. I think.

**Dave Jones:** Okay.

**Chris Gammell:** It's 2018. It's a fairly early. I think that was one of their first. Basically when I, basically what happened was, I mean, what spurred it all? I had a VW Sirocco diesel, which is a fabulous car. But the, around London, there's a thing called the ULES, ultra low emission zone, which basically meant you've got to pay a certain amount to drive in London if your cars don't meet a certain amount of emissions. And next year, they're extending this out to like a much wider part of London. So I thought, well, you know, my diesel is going to be worth nothing. When that happened. So I just started looking around. You knew literally nothing at all about EVs. I thought, oh, yeah, EV might be interesting. Had a look. And this, say, this would have been about a year and a half ago, something like that. I started reading reviews and everyone said, oh, the Kona, it's the best car, fabulous range, great car, brilliant, brilliant, brilliant. But, you know, you had to wait a year to get one because, you know, they sold their initial allocation and they're on a ridiculous lead time. And I just found one at a local dealer, which was, I think it was about, it was an X demonstrator, about 5,000 miles or something at this price. So I just sort of phoned them up, took a test drive, said, yeah, fine, I'll have it, you know. Yeah. Time for a new toy. Didn't really make financial sense, but, you know, it was the new toy factor. What do they peg the,

**Mike Harrison:** what do they peg the efficiency at for it? Like the mileage.

**Chris Gammell:** In summer, you can, I mean, four miles per kilowatt hour without even trying. If you're really, really light footed, you can get over five miles per kilowatt hour. And it's got 64 kilowatt hour battery. So you're talking over 300 mile range.

**Mike Harrison:** Right, right. You meant, you said that the, yeah. Ever go that far, but it's nice to just, you know, you just don't worry about range at all.

**Dave Jones:** Yeah. Miles. That's about right.

**Mike Harrison:** I think 200 miles, right?

**Dave Jones:** 217 miles. Yeah. It's a smaller pack. Mine's a 38, 38 kilowatt.

**Mike Harrison:** But Mike, you said that London has like requirements on like efficiency. So like, do they, do they actually tag the efficiency to like a gas or diesel?

**Chris Gammell:** No, no, no. I mean, basically, it's basically emissions. So with the U layers, I think petrol cars over the last, I don't know, six, seven years are compliant. And diesel is the big problem because they were, a while ago, everyone was pushing diesel until they discovered about all the NOx emissions. Oh,

**Dave Jones:** but they were, they were super efficient. The VW ones, nudge, nudge, wink, wink.

**Chris Gammell:** No, this was before diesel. Yeah. Right,

**Dave Jones:** right,

**Mike Harrison:** right.

**Chris Gammell:** Yeah. Right, right. Yeah. Yeah. I mean, my, my,

**Chris Gammell:** my, my diesel Sirocco got amazing mileage. It really did. You know, I hardly ever, it's almost like I hardly ever had to fill it up. And it, it didn't feel like a diesel at all. It was super smooth. So the, the requirements for diesels are quite high. And there's, there's all sorts of things like some London boroughs, they charge you more for parking permits. If you've got a diesel and so on. So that's interesting. But no EVs, basically, if you're anywhere, you know, if you've got need to go through London, an EV is almost a no brainer because there's a congestion charge and an emission zone. And part of this parking, like for example, to park just a day apart, right in the center of London. And you basically, if you've got an EV, you pay for 10 minutes and you get four hours on street parking. And you know, four hours, we're talking probably like, I don't know, something like that. Here in Australia,

**Dave Jones:** it'd be 50 bucks. Yeah.

**Chris Gammell:** Yeah. Yeah. But no, there's, there's sort of major, major concessions, but no, for me, it was fantastic to drive. You know, if you ever drive a pet, a petrol car, it's just so noisy and smelly and whatever.

**Dave Jones:** you'd never go back once you've got an EV. They're great. So, so do you have solar at home?

**Chris Gammell:** No, no,

**Dave Jones:** I do know you live in the UK. It is the UK day.

**Chris Gammell:** Yeah. I don't do a huge amount of mileage, maybe 10,000 miles a year, but I've got a tariff that gives me four hours cheap overnight. About, I think it's four P, four P a kilowatt hour or something for four hours, which is easy. I just set the timer on the car. And that's great. So,

**Mike Harrison:** so, so you're taking this thing apart now and like, I mean, how, how accessible is it under the hood? I mean, like, is it pretty buttoned up and, and like, how much do you have to actually dig into it to, to get at stuff?

**Chris Gammell:** I'm not quite sure why they've used this gunji seal, but the, the motor and inversion, it's all like, like for one big lump. So it's a bit hard to get, there's, there's reason, Mike. But yeah, that's probably more down to efficiency than anything else,

**Mike Harrison:** but there's probably about like 480 reasons or whatever the rail voltage is.

**Chris Gammell:** Oh, no, that's easy. Just don't lick the orange bits. That's fine. You'll be fine. And in practice, all you've got to do is if you, once you disconnected the 12 volt battery, then it can't close the contact that's inside the battery pack. So you'd have to try quite hard. Although I was contemplating the idea of tapping off the orange cable from the battery to the high voltage junction box, stick it into an inverter. Yeah. House backup. House supply.

**Mike Harrison:** Store your own connector on the side, you know?

**Chris Gammell:** Well, well, yeah, one of the things, you know, if I'd have got that scrap one, I'd have taken that cable and done a T off version of it with some fuses and started playing around with that.

**Mike Harrison:** But there was a, there was a commercial going around that holidays for a Christmas vacation, like that Clark W. Griswold thing. And they, they did a remake of the commercial where they went and plugged the, you know, the really lit up house into a EV. So it was a good one.

**Dave Jones:** I don't think the Hyundai's have the capability built in to backfeed into the grid, do they? Cause that's going to be a thing.

**Chris Gammell:** No, I mean, the new high, if you've seen the advert for the new Hyundai platform, their new Ionic branding thing, that does. They actually show the picture and they actually show a picture of a type two plug with a shoe socket in the back of it. What the interesting thing is, is one of the things on my list to talk about is the, the utter horror and crapness. This is the CCS charging standard. The CCS have been talking about, they've got a timeline for basically the, the general buzzword is V2G vehicle to grid or V2H vehicles, a home or V2X vehicle to whatever. And, you know, it makes sense if you've got this 64 kilowatt battery sitting out there.

**Dave Jones:** Oh, of course it's huge. That's a massive pack.

**Chris Gammell:** It would be nice to be able to plug my, plug my house. Okay. We don't get power cuts very often.

**Dave Jones:** For those who want a bit of scale here, like my Hyundai has a 38 kilowatt. Yours is what?

**Chris Gammell:** 64.

**Dave Jones:** 64. Whereas a Tesla is like 10, right? So like, as in, sorry, a Tesla home, a Powerwall. Tesla Powerwall.

**Chris Gammell:** Yeah.

**Mike Harrison:** Right.

**Dave Jones:** So people will typically get 10. Right. But you wouldn't take it all the way down.

**Mike Harrison:** Whereas a Powerwall might go, might go all the way down. You wouldn't take your car all the way down, would you?

**Chris Gammell:** No, unless it was the zombie apocalypse. Yeah.

**Dave Jones:** Okay. Sure. Of course, you know, but you know, like, so these things can be four or five times larger than your typical home battery storage. Right. Yeah. Yeah. Yeah. And actually,

**Mike Harrison:** that's why EVs are so expensive. It does have a big pack too. I mean like some of the, Oh yeah. It's like 45 or something for the big ones.

**Chris Gammell:** Yeah. Oh, is it huge one? I think a hundred, I think a hundred and ten in the top one. It's big, it's big, certainly.

**Dave Jones:** Wow. Yeah. So that, that is 10 times, that's an order of magnitude bigger than their power wall. Right. Yeah. That's how big this thing is. Right.

**Chris Gammell:** But, yeah. One of the issues, I mean, the, the, the fast charge DC charge standard, basically all it is, is two big pins in the socket and a contactor that connects straight across the battery. That's all it is. Um, the problem is the protocol. Now that there's two main protocols out there, the CCS and there's Chadimo. Chadimo was like the old one, things like Nissan Leaf use, which is pretty much dying. Chadimo are trying to claim it's not, but certainly in Europe, it's dying on its ass. I know. Yeah. It'll be around for a while. But the nice thing about Chadimo is a really well-designed standard in, in it's simple. It uses canvas. It's got dedicated pins for dedicated functions and it already supports outputting power from the car. And there are actually some V2G trials, vehicle to grid trials going on in the UK at the moment with the Nissan Leaf. But unfortunately, the one downside of Chadimo uses separate connectors for AC and DC. Um, now unfortunately in, um, the UK and I think elsewhere there's a CCS. And I think the U S uses CCS one, which is basically a, uh, a type one AC connector with two extra pins on the bottom for the DC.

**Dave Jones:** And yeah, the yanks are weird, aren't they? They don't want to, they always want to run their own.

**Chris Gammell:** But it's, it's basically, it's the same standard. It's just because the AC connector was different in the U S it's based on different connectors.

**Mike Harrison:** I think the U S probably got used to like, just determining their own, you know, like GM and all that were just like, well, we always used to make everything. So why don't they follow us?

**Dave Jones:** And even, uh, even Tesla, who are the apple of the car world, right? They have to manufacture the, they use, if you buy a Tesla here in Australia, it's got a different, uh, charge connector. It's got the, uh, CCS charge. Yeah. And in Europe.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** And, and Europe as well, I think. Yeah.

**Chris Gammell:** I was reading something about that about the other day and they're doing some weird, cause I think the U S ones have got their own custom, their own connector.

**Dave Jones:** And Tesla have their own custom connector in the U S. Yeah.

**Chris Gammell:** And I think they are actually doing a CCS adapter for it, which sounds, sounds a bit sketchy.

**Dave Jones:** You can buy an adapter cable. Yeah.

**Chris Gammell:** Yeah. I think I might limit the current a little bit. Cause I don't really like the idea of like 300 amps, 400 volts. No, going through an adapter,

**Dave Jones:** a dodgy adapter cable. Well, you can get off Amazon though. You can get like a secondary market one, you know,

**Mike Harrison:** like just like, uh, not, no, it's low cost because it's, it's lighter, more lightweight. There's less copper in there, you know? And yeah.

**Chris Gammell:** Yeah. But no, the, the problem with CCS is it's a hardware standard that has very clearly been spec'd by a software person. Basically what it, what it uses, it uses a protocol called, uh, green fire, which was originally designed for power line communication, like domestic, you know, putting data over your main power lines. So someone obviously thought, okay, this is a power application. This is a power line protocol. Let's use that. So basically what you've got is a system where all this thing needs to do is the car to tell the charger, give me 200 amps, this much voltage, give me a hundred amps of this mass voltage. And that's pretty much it. It's a very simple, you know, say Chadimo does it using, using can bus. It's really simple, but this green fire protocol has got, you know, ridiculous modulation. It's got encryption. It's got seven.

**Mike Harrison:** It's Qualcomm's green fire. Is that what we're talking about? Yeah. I think we may have just solved the problem right there. It's a Qualcomm green fire.

**Chris Gammell:** yeah, I don't, I don't know why it's a Qualcomm, but it's the fact that it's vastly, vastly more complicated than it needs to be. And this means that it's difficult to implement. There's all sorts of compatibility problems between some, you know, there's always some car you hear that certain cars and certain chargers don't play well together. It takes quite a long time to sort it out. The car, a lot of the car manufacturers are undoubtedly just buying a software stack in. I actually found the, the CCS module in my car. So there's just like a module that's basically a can buster CCS bridge, which I've, I'm going to start investigating some of the can side of things, but because it's a really complicated protocol, there are so many ways that it can fail, but also because it's got this encryption, you can't just, yeah, if it was can bus, you could hang a scope on it. Yeah. If you've got say one charger and one car that doesn't work, you could go down there, stick a scope on it, see, log all the communications, figure out where it's going wrong. But this, you can't really do that. Now, somebody does actually make a CCS monitor, but I don't quite understand how that works because there's, you know, there's all sorts of encryption and key change and completely unnecessary stuff for something, which is a physical hardwired connection between one car and one charger.

**Mike Harrison:** Yeah. I mean, it seems like it's a, so I'm looking at, I dropped a PDF in the, in the chat here for you guys, but like, it looks like it's, yeah, it's just like a, there's, you know, a Qualcomm interface chip effectively. And they made the standard. It looks like that's, yep.

**Chris Gammell:** Oh yeah. Yeah. But the problem is the CCS standard is, is umpteen layers on top of that. Oh, okay. So this is just physical.

**Mike Harrison:** And then you're saying,

**Chris Gammell:** if you look at the CCS standard, the, it's just, you know, plus I've not got the details, but from what I gather, there are certain aspects that aren't very well specified, certainly not as tightly specified as they should have been for a protocol. That's meant to work any car plus any charger. Yeah. And that's where a lot of the problems will come from, but they, I think they have a timeline for doing V2G, but it's like still two or three years off, which is just crazy. And other stuff like, um, plug to charge so that, you know, it can authenticate the car. So you don't have this idiot idiocy with all the different membership cards or apps or whatever. That's another big problem. And that's one of the biggest problems at the moment is that there's a lot of fast chargers out there. Um, yeah, 50 kilowatts. And now we've got some hundred and three 50 kilowatt chargers coming in line, but the newer ones are started. I think there's a, there's a, there's a very strong government recommendation in the UK that they should all accept at least contactless credit card payments. So you just rock up, plug in, wave your card and go.

**Mike Harrison:** Yep.

**Chris Gammell:** But a lot of the legacy ones, you've got apps or member RFID cards, and it's an absolute nightmare. It's ridiculous.

**Dave Jones:** Oh, well, one of them, I can't remember. Is it charge point or something? No, not charge point. One of the other players that have their own network of chargers, they've gone out of business here in Australia. So we're left with like this abandoned network of chargers. I'm not sure if they still work or not, but you know, it's like, yeah. And yeah. And you needed some RFID card to, you know, make it work some account with them and, you know, some card. Yeah.

**Chris Gammell:** There was, I think there was a UK network with just AC, seven kilo AC chargers, which I think they were abandoned. But if you still got one of the old RFID cards, they still work, but you can't get a new card. They still work. Yeah. I've heard that. Some of them still work.

**Dave Jones:** I think some of them still work here too. Yeah. Even though the companies fall apart,

**Mike Harrison:** but no, it seems all night.

**Mike Harrison:** I just can't get a new card. I mean, this is kind of, I mean, I think,

**Mike Harrison:** I think one of the, there's like a page on this, this document I sent you guys to that I'll link on the notes, but like they're doing a comparison. And like one of the other things that they're putting in here is like CCS has controlled DC fast charge. Fine. That's the same as Chattamo, but, but then also simple payment and billing time of day pricing, home network integration. It's like all of these things that are just, it seems like it's this fluff that's on top of it. That's exactly. Yeah. It doesn't seem that necessary.

**Chris Gammell:** Let's think of anything we could might possibly want to throw out of other stuff in. And mandate all of that complexity on the simplest plug in and charge my car. Right. Situation. Right. I don't like that.

**Dave Jones:** They can fix all this Mike by just adding another, like an extra layer that fixes it all.

**Chris Gammell:** Do it in software, man. Cue the XKCD cartoon. Yeah, that's right. Yes. Yes. That's it.

**Dave Jones:** That's the one I'm thinking of.

**Chris Gammell:** Yeah. Oh boy.

**Dave Jones:** The, the thing with EVs though, is that, you know, people don't realize that it actually changes the game for, I, maybe let's just call it half the market, right? Half the market who own EVs, uh, will never have to go to a charging station. Almost never. Yeah. Oh, very rarely. Unless you go on some huge road trip or something. Right. It's so you don't need all the number of petrol stations. Basically, if you've got a home with a place to park your car, you've almost certainly got power there. It'll, you can recharge overnight and it does all of your daily needs. There's no need to go to a charge station.

**Chris Gammell:** I've had, I've needed to fast charge, I think four times since I've had the car. Right. Actually needed to. A year and a half, two years. Yeah. Yeah. Yeah. But I don't do a huge amount of mileage.

**Dave Jones:** I've only done it out of, out of curiosity. Yeah. Oh no. Sorry. Yeah. Yeah. Actually I've only done it out of curiosity. I've never had. Well, see,

**Chris Gammell:** there will be some people that do need to use it regularly and some people that need to use it occasionally.

**Dave Jones:** You know, especially in the European countries where, you know, nobody like people go a garage. What's that? I parked my car on the street, you know? Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Mike Harrison:** Or people who live downtown, such as myself, you know? Yep.

**Chris Gammell:** Yeah. But I think that's one of the problems, one of the barriers for people getting an IV. They've still got this petrol station mindset. Yeah. I think, you know, once they realize the convenience, the fact, you know, just imagine you wake up and your car is full of petrol every morning, you know?

**Dave Jones:** And, and, and, and that's via the slow, that's via the PowerPoint slow charger. Yeah. Right. Because most people want average of 50 kilometers a day or something, you know, 50 miles a day or whatever. You can recharge that overnight. So you come home, you plug it in. Even you don't need a fast charger at home.

**Chris Gammell:** So, I mean, you get into the, I suppose, technically slow, fast and rapid are the, the conventions. Slow, fast and rapid. Yeah. Fast is seven kilowatts or occasionally 11 if you've got three phase, but most people certainly in the UK don't have three phase.

**Dave Jones:** Yours is like mine. It's only single phase charger on the car, right?

**Chris Gammell:** The 20, mine is the, the, the 2019 Kona does have three phase charger. Oh, it does. Does it? Okay. Right.

**Dave Jones:** Mine's the 2020 model and it, it, it, and it has only got single phase. It may,

**Chris Gammell:** that may also vary with region. Cause obviously like some European countries, three phases common, but also the current is lower so that the, the standard single phase would be two 40 volts at 32 amps. But I think in someone said in Germany, you know, the common, they don't have, they've got three phase, but they don't have 32 amps spare. Right. So a three phase 16 amp is a more common scenario, but yeah, that varies country by country. And the way that charge, the actual onboard chargers on the cars, the way they often handle that is that they've actually got three separate chargers and they strap two of them together for single phase and run three separate, three phase, which has had a couple of unfortunate, unfortunate occurrences in there's actually the red eye Zoe, which is quite, quite a well-known situation, but apparently the Hyundai and the cut, the Kona and the Kia Inira had an issue with one or two chargers that support solar in that they didn't do the single versus three phase detection. If the, the way the protocol works, it's a super simple protocol, the AC charging protocol, but the car doesn't know whether it's getting single or three phase until the charger turns the power on. Oh. And what was, what happened with those was that I can't remember if it was actually something that wasn't well specified on the, in the standard, but this particular solar charger, depending on how much power was available could switch between single and three phase. And it would do the, there's a line called control pilot, which the wall charger tells the car what's happening. And it would put it back into the idle state as it, and the car should have interpreted this as the car being unplugged and plugged back in again. But some of the, these two cars, the onboard charger didn't do that. So what would happen was it would switch between single phase and three phase, no, between three phase and single phase, the car would assume it was still in single phase mode and short two of the phases together, which didn't end well. It would generally damage the charger and the onboard charger and the charge point. But I think, I think they've issued a recall to fix that now, but.

**Dave Jones:** Right. Does, does your Kona have, cause my Ionic from the 2019 model to the 2020, the 2020 has changed for the DC fast charge. It's actually a stepped charger. So like at below 50%, you'll get your full 50 kilowatts, but above 50, it'll drop down to 40 kilowatts. And then above 60, it'll drop down, down, down.

**Chris Gammell:** All EVs do that, but the actual curve they use is different between cars. I've heard that the Ionic is particularly bad, cautious, whatever. Yeah. Cautious. Yeah. The Kona has had a couple of recalls cause they've had a few batteries catching fire incidents worldwide. And they've done something where I think it pauses at 80 and 90%. And my reading between the lines, I don't think they actually know what's been causing these fires. And what they've done is they've tightened up the maximum cell deviation. So that if, if it sees more than, I think it's 150 millivolts deviation between the highest and lowest cell, it will just shut the car down and you've got to take it to the dealer. But also it does it pause. Check engine lights, huh? Yeah. Yeah. And the, it all, the, one of the things that has changed in the, in the most recent software update recall was that they pause it, I think at 80 and 90% for a while. And I'm guessing again, that's probably just wait for it to stabilize and then check the cell deviation again. But it's obviously I'm, I'm really saying what's, what's actually happening with this, but the speculation is that. Yeah.

**Dave Jones:** And the thing is, is that the problem is they, in order to compete, they have to offer massive battery warranties. I mean, mine's got an eight year battery worry. I don't know about yours. Right. And they have, yeah, they have no history of how long these things are going to last. Right. So that that's why they're being very, from the 2019 to the 2020 model, they went, well, you know, we're getting the heebie jeebies about this battery warrant. It's got to last eight years and it's got to have X capacity after eight years. And people are fast charging these things at 50 kilowatts. We'd better step it down just to be, you know, once you get over 50%, well.

**Chris Gammell:** Yeah. I mean, I think the, yeah, things like Nissan Leafs have been around long enough that I think they're fairly confident that the fast charging itself, as long as you keep the temperature under control, isn't a problem. You have had Nissan Leafs that have been like, have done like 200,000 miles fast charged every day as taxis and still got like 80% of the battery after, after that.

**Dave Jones:** Yep.

**Chris Gammell:** But,

**Dave Jones:** but that's them. I mean, every manufacturer has to start from scratch. Yeah.

**Chris Gammell:** Yeah. But I don't think the batteries, I don't, there's only a few battery manufacturers at the moment. I think. Yeah.

**Dave Jones:** But how you implement them could be an issue too. Yeah. So.

**Chris Gammell:** But there's really not that many parameters. It's basically temperature and charge rate. I don't think it's really that much, as long as you haven't got any hotspots and your, you know, your heating is well distributed. I don't think that's, that's a major issue. But yeah, apparently in Korea, I saw a report. They'd had a hundred that they replaced the batteries on a hundred conas.

**Dave Jones:** Oh, really?

**Chris Gammell:** But there's, for some reason that this seems to be more prevalent in Korea. I don't know whether it's a usage pattern or something that's different there, but obviously if you've got a battery fire, it's very hard to figure out what actually happened. So my guess is that they are hoping that a cell, they'll see a bigger cell deviation as a precursor to it catching fire. So they can stop it. So it doesn't actually catch fire. But I'm sure that, yeah, the, the, I know there's been one or two reports of people in the UK since having the BMS update that they have said, you know, the car has, has subsequently said, you know, error, take it to the dealer sort of thing for a new battery.

**Dave Jones:** Okay. Yeah. They're being extra cautious. Yeah.

**Chris Gammell:** Yeah. Of course. I mean, yeah. Battery fires are never good publicity.

**Dave Jones:** No, it's never good publicity. And you don't want to find that in eight years time, you're liable for, you know, a million battery packs, right? Cause you know,

**Chris Gammell:** these things,

**Dave Jones:** you know, because everyone would be clamoring, right? If it, you know, cause they, they make a specific claim.

**Mike Harrison:** Yeah. I mean, if you had like a, you know, 5% down, you'd be like, Nope, I'm getting mine replaced. Yeah.

**Chris Gammell:** Yeah. Yeah. You do worry what effect it's going to have on the resale values as it starts getting towards the end of warranty. But I suppose if it's run for eight years without blowing up, then it's probably okay.

**Dave Jones:** Yeah. It's probably okay. Yeah. But yeah, I'm so glad I didn't buy the secondhand leaf. I was arming and are in for years about buying a secondhand leaf and the range is just crap on them. I wouldn't have been, it wouldn't have been usable. You know, it would have been a cute toy for just, you know, but it's not really a.

**Chris Gammell:** For local stuff is probably for, you know, if your usage pattern is such that you can deal with that range, then it's fine. Of course.

**Dave Jones:** Yeah. Yeah. No, but occasionally I've got to drive up the mountains or up the coast. You know, and it's just, no, it's absolutely useless. Yeah. So yeah, Mike,

**Mike Harrison:** you'd mentioned a vehicle to grid. Can, can you explain what that actually requires like internally to get a car that will do that? I mean, is it like a, a secondary, like, like charge flow reverser or like what's in there?

**Chris Gammell:** Well, no, I mean, but if you look at the, the fast charging architecture, as I said, on the car is basically two big fat pins on the plug, a contactor, the battery, and that is it. Obviously there's monitoring and measurement. So the intelligence is in the thing that you have at home that plugs into the car that can tell the car, okay, okay, give me 50 amps now. And it then it's, it'll be very similar to a solar inverter in that it will talk to the grid. The grid will say, okay, I need this capacity at this time. And it can talk to like 20 cars in the neighborhood that can suddenly feed power into the grid. So the, the box on the wall would be a DC to AC converter, very much like a solar inverter. I'm skeptical about vehicle to grid specifically. Um, in places like if like, for example, you've got a bus depot with like 20 buses all plugged in overnight, I think that could easily work. But individual people, I think just because of the cost of the inverter to do it, I'm not really sure how well that's, how viable that, that is. But some,

**Dave Jones:** I've, I've, I've seen prices of $10,000 for one of these grid to, uh, vehicle to grid inverter boxes.

**Chris Gammell:** Yeah. It depends on that. I think the cost would be comparable to a solar inverter. Cause it's doing pretty much the same thing. Yeah. Um, they're not making many of them. Exactly.

**Mike Harrison:** Like micro inverters.

**Dave Jones:** Because they're an exotic thing. Now they're like, yeah, I've heard they're charging like $10,000 for this.

**Chris Gammell:** Oh yeah. That doesn't surprise me, but that's because I don't make many of them.

**Dave Jones:** Yeah. Yeah, exactly. So, okay. So this is,

**Mike Harrison:** so this is a thing that is potentially on the way, but it's not like I, the way you were talking about it, I thought it was like a, something they just hadn't included yet. Like for this specific model, but you're saying this is like a, a trial still.

**Dave Jones:** In theory, the existing cars could all do it. Well,

**Chris Gammell:** it depends what you call theory. Nissan Leafs can do it today and they are actually running trials at the moment in the UK doing it because Luke Chaddemo already has the provision for spitting power out of the car. CCS doesn't support it yet. And it's interesting that that new Hyundai platform claims to be able to do it. And I wonder if they're almost by eat, well, maybe CCS are going to get their, get their act together and put it in the protocol soon. But I suspect that what might happen is actually Hyundai and they're going to do their own thing, their own protocol to just bypass that. And let it spit power out. All their,

**Dave Jones:** all their marketing departments just going to go, Oh, CCS are promising this update. So we'll, we'll market it and then we'll just include it. I mean,

**Chris Gammell:** most cars probably could support it if they had a software update, but who's going to, by the time it's in the standard, are they going to give software updates to five-year-old cars? No.

**Mike Harrison:** So this is just something we're going to see in the future, probably. Yes. As long as the, yeah. Okay. And so then eventually a government might, might try and mandate this in future standards or something like that, but it's not.

**Dave Jones:** Or, or it'll be a marketing thing. Like you won't want to buy a new EV unless the manufacturer promises to give you a software update to.

**Mike Harrison:** Yeah. And yeah, it might be. What was the other option? So there's vehicle to grid and then vehicle to home. Is that right? Yes. Okay. Yeah.

**Chris Gammell:** So you just use your, you know, use your car as a home backup. So if you've got, if you live in a place with, unreliable power, you've got this massive UPS sitting in the garage. So why not use it? Right. And there are one or two cars. The, I think the, the Hond, the Honduri has actually got a main socket inside and there's, I think some of the pickup type. I think, I think the Ford pickup or something has got a, like a three kilowatt AC output or something. I believe that. Like camping and things like that. Yeah. That's,

**Dave Jones:** that's pretty sweet. So all of it, basically all of the issue is have to do with the external box. It's not necessarily to do with the car. That's more of a software. It's software.

**Chris Gammell:** Yeah.

**Dave Jones:** Protocol interface, because the, the, as Mike said, the CCS connector has the two terminals directly across the battery. So, you know, it's basically, that's it. You can get the power out of that car, but it's how you actually integrate with your house, integrate with the grid and everything else. That's the job of the external box. It's nothing to do with the car.

**Chris Gammell:** Yeah. The only possible thing, obviously the, the cars on board current measurement has to be able to deal with current coming out of, as well as into that. Oh yeah. Right. But I'd imagine most, yeah, it's already got to deal with power going in and out of the battery from the motor anyway. So I think it's fairly unlikely you'd have car hardware that couldn't support it. It's just a software thing.

**Dave Jones:** Yep.

**Mike Harrison:** Well guys, I'm really, I have to get one at some point now. I mean, that's, yeah. I feel left out. I gotta say.

**Dave Jones:** Yeah. So, uh, they reckon 2021 is the year of the EV. They reckon there's like, like two dozen EVs coming on the market. Oh yeah. There's loads.

**Chris Gammell:** Yeah. Yeah, definitely. The sales of, yeah, the sales have been increasing even through lockdown. Whereas all the ice, you know, internal combustion has sort of been declining. I think this varies a lot by country. Different countries have got different attitudes. Norway is just off the scale with EVs already. Yep.

**Dave Jones:** Yeah. Yeah. Isn't it like 50% take up new car sales or something?

**Chris Gammell:** Yeah. Crazy. They've got a lot of incentives there. Whereas it's Australia that actually is thinking of taxing EVs.

**Dave Jones:** Yeah. They're thinking of taxing EVs. It's got, I think it might be a bill in parliament at the moment or something. Yeah. Yeah.

**Chris Gammell:** You already generate a lot of your power from coal still.

**Dave Jones:** Yeah. Exactly. But the amount of where our EV take up here, because we've had no tax subsidies at all, unlike the US and other.

**Mike Harrison:** Yeah. We're still 7,500, I think for.

**Dave Jones:** Practically no one here owns an EV. Yeah. There's a lot, you know, quite a few Teslas around and stuff like that, but that's basically a rich person's toy. Yeah.

**Mike Harrison:** Yeah.

**Dave Jones:** Yeah. But the actual percentage take up is like 0.1% of car sales or something. It's like the low, one of the lowest in the world here in Australia, which is surprising because we have practically the world's largest solar uptake here because of the subsidies. We, everyone, like 40% of houses here in Australia have solar on them. Yeah. You know, it's, it's insane.

**Mike Harrison:** You guys actually have sunshine too. Oh yeah.

**Dave Jones:** But it was all because of the tax subsidies. of course. So, you know, it's, you know, so if we didn't have that and the same with EVs, we've had no tax subsidies. Therefore they, you know, nobody bothered to do them. And because we have a import luxury car tax, it's called anything over like 75 or $80,000 gets taxed. And an EV here, like a, a, a Tesla, even the, the model three is barely on the threshold of the luxury car tax. It's like $79,000 or something. Yeah. Same here. I think. Yeah. That's another disincentive to buy a high-end Tesla.

**Mike Harrison:** I think it, I mean, I can imagine like you guys don't have, I mean, do you have any in, in, in country manufacturing for cars? I feel like Australia has nothing left. Yeah. I feel like that drives a lot of it too. Like, because like,

**Dave Jones:** it just stopped like two years ago. Yeah,

**Mike Harrison:** exactly. They're trying to build, you know, like, so at least in the U S or, you know, car manufacturing is just such a huge piece of GDP here too, that like, yeah, I don't think there's a ton of interest in it broadly. I mean, I hope there is, but I don't think, you know, you know, countrywide that there's like people clamoring for it, but I think they're also, they see the future and like, they're like, okay, well, these car companies are going to build out electric vehicles. We got to sell them somehow. And you know, like it's actually, it's an economic move as anything else. So I'm, I'm, I'm damn happy about it personally, but it's like, you know, I don't think it's like, I think that might've changed then Australia's take on it. If, if you guys had in, in country manufacturing for that sort of thing.

**Dave Jones:** Oh, it, it, it may, I can see possibly manufacturing coming back here. Cause you know, this talks about now with our tray balls with China and everything, we're talking about local manufacturing. Start, start the,

**Mike Harrison:** start the automotive,

**Dave Jones:** start the EV or the EV car,

**Mike Harrison:** you know, the angel funding. I'm the EV EV.

**Dave Jones:** There you go. Yeah. Yeah. Oh boy. And, uh, yeah, so that's, I could potentially see that coming back. So, but we'll see, but the other thing is here is Australia is, if you haven't noticed on the opposite side of the planet to where everything else is made. So it's actually kind of expensive to ship stuff. Here's what I'm thinking,

**Mike Harrison:** Dave Sinclair C one with a, with a 20 kilowatt hour battery.

**Dave Jones:** Yep. Yep. I can kickstart that bastard. Yep. 10 million bucks on Kickstarter. Guaranteed. Yep.

**Mike Harrison:** All I need is a few fancy renders and some call it, the call it, the call it the chariot of fire, the chariot of fire.

**Dave Jones:** That's probably not such good marketing. No,

**Mike Harrison:** it's just realistic. It's a flaming EV. Yeah, right. Oh boy. Yep. You know,

**Chris Gammell:** there's a lot of new cars coming out next year. And there's a few like, um, X-Pag in China, one of the big Chinese manufacturers is starting to, um, ship to Europe. So that'll, that'll be interesting.

**Dave Jones:** In my, when, when I went to visit the electric bus depot here in Sydney, I did a video on that.

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, I was surprised to learn that China have like 50% of their buses are electric. Yeah. It's like, wow. Who knew? Right. They have this massive percentage.

**Mike Harrison:** Dave, the people that are taking the bus. Yeah.

**Dave Jones:** I know people in China know, but I go, look, look at an electric bus. I'm getting on the bus.

**Mike Harrison:** So it's electric bus.

**Dave Jones:** It's just because they're, you know, the cities are so polluted that they, even China has to do something about it. You know? It's great. Hey,

**Mike Harrison:** every time, every time I see more stuff like this, it's wonderful. Whatever, whatever it takes. And Mike, did you say it's H I N O? Is that who it is? What was the company you said?

**Chris Gammell:** No, X, X peng. X peng. Yeah. They're the ones that got accused of, um, stealing all of Tesla's self-driving code. Oh, allegedly.

**Dave Jones:** Um, guaranteed.

**Chris Gammell:** Yeah.

**Dave Jones:** With the spies, all those 2 million communist party spies throughout the world, you know, we've all, come on.

**Chris Gammell:** No, I think that was actually ex Tesla employees went, went to work for them. And, uh, yeah. Oh, yeah. I'm looking at that. If they didn't,

**Mike Harrison:** it would have got out. The P7 electric, electric sedan. I mean, like every car kind of looks the same these days, but like, yeah, this pretty much looks like a model S and a model X on their website. So that's fun.

**Chris Gammell:** But apparently that's their self-parking actually works better than Tesla's at the moment. Oh yeah.

**Mike Harrison:** I believe it.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. No, we probably haven't talked about it before, but your take on the self-driving thing, I think, nah, I think. it's not as close to being as certain places. Yes. Yeah. But go ahead.

**Chris Gammell:** I've seen sort of some discussion about it in that, yeah, that's one of, in theory, Tesla's big, big things that all the current motor manufacturers aren't really taking seriously. And things like, you know, self-driving cabs and the fact, okay, people like driving their own cars, but if they're commuting every day, then if they can be sitting, doing something else while the car's taking care of it. Yeah. Right. But also there's other aspects like the safety side of things in that self-driving cars on average will probably be safer than non-self-driving cars. And one of Tesla's sort of hidden things is car insurance in that they've got vast amounts of data. Yeah. And, you know, I think they're already starting to offer it. And the rumor has it that, you know, if you buy a Tesla, you know, you can buy much cheaper to car insurance from them. And that's potentially a massive, massive earner from them going forward with self-driving. And I think there is some, some of the things like collision avoidance is already on the verge of being mandated in some areas. So I think we're going to see that sort of stuff in improving road safety. And at some point, you know, I think there might be a tipping point, but it's hard to know exactly when and where, and it's running very a lot by country.

**Dave Jones:** I've, I've already found that those features in, in mine are very like quite handy. You know, the collision avoidance, like you're going out of the lane or you're trying to pull into another lane, but there's a car there, you know, beep, beep, beep, it warns you and it'll, you know, and it'll keep a safe distance. Mine actually has some self-driving capability. It'll actually stay in the lane. I can take the hands off the wheel and it'll, you know, follow the lane and, and turn and keep a set distance from the front radar as well.

**Chris Gammell:** The front radar. Yes. Yeah. That's a nice thing.

**Dave Jones:** I mean,

**Mike Harrison:** gas-based cars have that too. I mean, like that's a,

**Chris Gammell:** yeah. Oh yeah.

**Dave Jones:** No, no, it isn't anything new to EVs, you know,

**Chris Gammell:** in the past, I've never liked cruise control because it's so easy to suddenly find you in the back of someone. If it's a simple constant speed one,

**Dave Jones:** whereas this will keep a distance. I can actually set, I can program the distance between the car in front and me and it'll automatically slow down and, and, you know, yeah, it's great. And speed up as well.

**Chris Gammell:** Almost found by accident. It's really good in stop, start traffic as well. It works really well in stop, start crawling traffic. And it would just, you know, you just sit there and it just starts and stops. Yeah, exactly. If it stops them all in about two seconds, you have to press a pedal to restart it again. But if it's, other than that, it actually works really well in that situation. And so the steering thing works most of the time reasonably well.

**Dave Jones:** Yep. Although I found that the self-drive, like a lot of these features are easily tricked. I found, you know, at, at nighttime or on a wet road or on a curved road over a hill and it'll, it'll just lose it or some specific cases I found where I'm actually going into a legitimate lane, but it thinks I'm actually turning where, because I've got my blinker, right? Like you need to put your blinker on for a specific, you know, multi-lane turning road, but it thinks you're going turning and it'll beep at you when it shouldn't. Like it just thinks that you're going to crash it and, you know, no, I'm following the road rules and it's just, yeah, it's, it needs a bit of refinement. Yeah.

**Chris Gammell:** And the other one that I've had probably most annoying is that is the collision avoidance thing is where you're, you're basically are actually heading straight to another car, but it's actually a parked car that you're going to steer around, you know, when you get to it, but it doesn't know that yet. It thinks you're going to crash into it.

**Dave Jones:** Yep. Yeah. I've had that. So it's, it's not that smart. I don't know if the Tesla is any smarter, but famously I, while I was at the bus depot, I actually saw the bus that everyone was tweeting that morning. And I even retweeted it myself because there was this Tesla that, that famously was fooled by a big advertisement of somebody's face on the back of the bus. And I thought, and I thought it was a person stepping out, you know, so the camera, and yeah, so he's, he's like, cause the Tesla records everything. So he's got the recorded data from it and yeah. Yeah. Oops. So, yeah, I, I think, yeah, in certain specific circumstances, yes, it's very valuable and it's going to work, but you, you take it in unusual situations, which around Sydney, you know, if you ever drive in cars around Sydney, holy crap, you know, especially at night and in the rain and all sorts of, you know, crap because the, the Tesla only has cameras. It doesn't have, you know, LIDAR and stuff.

**Chris Gammell:** So yeah, I had an interesting take on that in the, I think Tesla's attitude is that LIDAR is very much a stop gap. Right. For systems where they can't do it. Cause you think about it. What are the sensing things on a normal manual driven car? Two eyeballs. You, you don't have like LIDAR. So it clearly can be done with a, with optically. And LIDAR is almost like a stop gap for when you can't make the optics work as well as they could do.

**Dave Jones:** Yes.

**Chris Gammell:** So it'd be interesting to see what happens.

**Dave Jones:** True.

**Chris Gammell:** On that.

**Dave Jones:** But you know, where I, I think we're still a long way from, uh, yeah, their AI being as good as a human.

**Chris Gammell:** Yeah. I don't think it's as long as far away as a lot of people think though. Certainly for quite a lot of situations.

**Dave Jones:** I'm, I'm still calling 20 years.

**Chris Gammell:** Oh no, no, no, no. Five, five, less than, less than five.

**Dave Jones:** No, no.

**Chris Gammell:** I'll bet you on that. I will say 10. I don't have a good take on this. So yeah. No,

**Dave Jones:** I will say 10. It'll be like, people will be using their full self driving in their Tesla. Okay. But it won't be able to do everything.

**Chris Gammell:** No, no. But if you can.

**Dave Jones:** Talking about doing everything. I'm, I'm, I'm talking about being anywhere and then summon your car, come and pick me up, you know, or, or take me to this exact, do this exact thing. Yeah. You mean like, you mean like go up these ramps,

**Mike Harrison:** go on everyday things instead of like practical everyday things,

**Dave Jones:** instead of getting from one city to another, that's, that's fine. You can do that now. Now I'm talking about practical everyday things where, Oh, you know, you have to park up on the curb or something, or because there's roadworks here, or there's some other thing. Like, it's just, it's not going to be able to figure this stuff out.

**Mike Harrison:** I mean, have you, have you seen human drivers, Dave? Most human drivers can't figure things out too.

**Dave Jones:** Yeah, but we are adaptable. Like. We are liabilities. Any situation. Right. That's the thing. I, that, that's what I'm talking about. That, that adaptability. I, that's 20 plus years away.

**Chris Gammell:** Hmm.

**Dave Jones:** I, I do not see that within the next decade.

**Chris Gammell:** Yeah. But if, if you can make it work, you know, safely in, let's say 90% of the situation. Oh, sure. You know, yeah,

**Mike Harrison:** I think it'll take over small things at a time. Of course.

**Chris Gammell:** Yeah. Yeah. And I think once it gets approved in a, in one country and yeah, if they start seeing major benefits in terms of road safety, I think that could then. Oh,

**Dave Jones:** that'll be the trigger. You know,

**Chris Gammell:** you then get like insurance discounts and whatever else I think, you know, that, that could sort of start the ball rolling. And so it will never deal with all situations, but if it can deal with like 90% of the situations, it's still a very valuable thing. Yeah. And if you think about how much data Tesla has probably already got, real world data, you know, certainly a lot more than anybody else has.

**Dave Jones:** There's, there's rumor has that Tesla, because Tesla has got two computers in it, right? Two of these supercomputer, you know, image processing things. And they reckon one of them, there's a theory, nobody's actually sure, but one of the theories is that, is that one of them is actually doing all speculative stuff and actually recording that. And then it's comparing to what the other one did and whether or not it's running new algorithms on the second one. And then it's actually, so they're doing in-car testing and stuff like that. And then they're uploading that to the Tesla server and go, okay, how far different was this new experimental thing from what the driver actually did? So, so they're taking the end, they're recording the inputs from the driver. Okay. The, we, we thought that we had to stop here, but the driver didn't. Therefore, oops, we were wrong and it's correcting the algorithms and that gets uploaded and they learn.

**Chris Gammell:** Yeah. That way.

**Dave Jones:** They reckon experimentation is happening on your car as you drive.

**Chris Gammell:** I'm sure someone will reverse engineer it and show the next chaos communications. Oh yeah, yeah, yeah, definitely.

**Dave Jones:** But yeah, they, that's, that's one of the, that's one of the theories about how they're getting so good. So quick.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Is that there? Yeah. Because they're recording what the humans do and then comparing that to what they expected. And then they're learning each time the human does something different to what they expected. So, yep. Smart. It's very smart.

**Chris Gammell:** Yeah. Interesting. Interesting times. And I think if the self-driving does turn out to be a big thing, then, you know, I think a lot of the other current legacy car companies could start really struggling to catch up because they're, most of them are just so far behind even in just basic car stuff now. Yep. You know, I think, you know,

**Dave Jones:** but I, the thing that bugs me is I, you know, I know a few Tesla owners all talk, Oh, full self-driving. It's, you know, it's, you're mad if you don't get full self-driving. It's like, yeah, it's still not that useful at the moment.

**Chris Gammell:** No.

**Dave Jones:** Like, you know, it's, it's okay, but it's not, you know, some, they, they think it's done and dusted. That's, that's the thing I have a problem with is that they think, Oh, it's done. And Tesla's done full self-driving. You can buy it. You can pay the seven grand package and you've got full self-driving. That's like, yeah, you know,

**Chris Gammell:** but they can update it over the air when they improve it, which a lot of the other companies can't even do that yet.

**Mike Harrison:** No,

**Chris Gammell:** I've got to take my Cona into the dealer just to get some bloody software updates that chug through a half megabit can bus through the OBD thing. It takes my four hours to do four software updates.

**Dave Jones:** In some aspects, I kind of like that. I like my car, not phoning, but I like my car just being a car, you know?

**Chris Gammell:** Yeah, I think there's, yeah, there's pros and cons. I think, you know, but to be able to do updates, even if it's fully controlled by the, even if they, you know, I could just plug an SD card into the head unit to do it, do an update. Right. Yeah. That'd be nice. There's still a very old, old school mentality in a lot of car dealers that, you know, the, the fact that my dealer wouldn't even send me out this bloody boot to stick over the,

**Mike Harrison:** I, I, I, so Mike, when you take your car in, do you go, do you go, when you take your car in and they're like updating this, the firmware, do you like slip in a conversation? You're like, well, you wouldn't download a car. Come on. But we were talking,

**Chris Gammell:** we're talking car dealers here.

**Mike Harrison:** They wouldn't. I know they wouldn't catch it, but it would be funny to like keep saying it until like, they're like, what the hell are you saying? Mine,

**Dave Jones:** mine came with lifetime map updates. Right. But the map updates have to be done at the service. Right. And of course, EVs, you hardly ever get them serviced like once a year. Yeah. You know, it's like, yeah. So I can't just download the map updates and do it myself. You know,

**Chris Gammell:** the stupid thing is Hyundai, I think in Canada and USA, you can. Oh, really? Which is really annoying. Yes, you can.

**Dave Jones:** You can do it. What? You can plug it into the USB port or something.

**Chris Gammell:** Yeah. Well, mine's got an SD card slot under the head unit. And I'm in the US. You can just download the stuff onto an SD card, plug it in and away it goes.

**Dave Jones:** Oh, I haven't seen that. I haven't looked. Really? Is it like hidden under the bottom or is it?

**Chris Gammell:** I don't know if the ionic's the same or not, but all the maps are actually on an SD card.

**Dave Jones:** Oh, okay. Yeah. All right. I'll have a good look.

**Mike Harrison:** They put, they put the SD card slot in the, in the correct place, which is the glove box. And then, you know, that's where you guys put the wheel.

**Dave Jones:** So it doesn't work anymore. Yeah. So I find that it's, is, is your building mapping system actually useful? I find mine. Yeah.

**Chris Gammell:** It's brilliant. It's really, it's really good.

**Dave Jones:** I find mine's mine's and, and the charges. How about when it tells you the charging stations, mine is literally useless.

**Chris Gammell:** Yeah. It's the last software update. At least you can now filter it to, to only show rapid DC chargers. Right. But the information is not very current. You know, it will show the charges that have been there for a long time,

**Dave Jones:** but mine, mine does, does, does not show the biggest car fast charging, free fast charging network in the country. Like it doesn't even show it. It doesn't, you know, your nearest one. I drove up to Newcastle, which is like 150 Ks up the coast. Right. And it's like, I know there's electric. I used one. I did a video using one up there. And it's like, it's, it says your nearest fast charging station is Sydney. It's like bullshit. It's useless.

**Chris Gammell:** I think that varies by country. I think in the UK, it's supplied by Tom Tom, but also sometimes it just doesn't connect. You need with my one. My was the only one that didn't have a telematic. So I've actually got a wifi to like GSM bridge thing. So you can also do it through the phone. You know, the head unit needs a connection to wifi to get live information. But the, the actual sat-nav stuff, you know, works fine. It works fine. It sometimes takes you down slightly of routes, but I actually prefer that to using the phone. Cause it's just there in front of you on a nice big screen with a nice user interface.

**Dave Jones:** Yep.

**Chris Gammell:** But no, it works, works fine. Apart from the charging points.

**Dave Jones:** Apparently the app's terrible. Isn't it? Isn't the Hyundai, everyone complains about the Hyundai app. I don't know.

**Chris Gammell:** I've not used it. I don't have any particular need for it.

**Dave Jones:** But everyone says, yeah, don't, don't even bother downloading it. It's pointless. So yeah, they need a bit of refinement there. I suspect.

**Mike Harrison:** Yeah.

**Dave Jones:** Anyway, yeah. Poor old Chris is probably getting bored of our EV rantings.

**Mike Harrison:** I mean, I'm just, yeah, I'm just sitting here. It's interesting to hear about. I mean, it's just, you know, yeah, a little left out. I drive about once per week guys.

**Dave Jones:** That's the thing with electric cars. There's so much as an owner, there's so much to talk about. Whereas with a petrol car, unless you're a real petrol head. Oh yeah. Yeah. I bought out my cylinders to, you know, like stuff like, but nobody like Joe average is not talking about their car.

**Mike Harrison:** Car talk has 4 million listeners still. And one of them is dead. So I'm just saying there, there is some interest out there. It may not be very concurrent with electronics people.

**Chris Gammell:** I think it's just starting to tip over between the, from the enthusiasts to the more mainstream. Yeah. I think that's right. But I think that's where things like the issues with rapid chargers, you know, for example, the classic one of people sitting on a rapid charger charging to a hundred percent, which is makes no sense because the charge rate goes down so much. If you've got a long trip, it's quicker to charge to 80% and then drive to the next charge.

**Mike Harrison:** And then drive off. Yeah. But a lot of people don't understand that. Yeah. I mean, they have to put in like people control, right? This is, this becomes a capacity problem. And like, yeah, it's just tough.

**Dave Jones:** It's called icing. It's if you've been iced, it means that either a petrol car is taking up a, an internal combustion car. That's where the term comes from. Ice is, is actually taking up an EV car spot, or you can get iced by an EV owner where they're parking. They think they're entitled to park their EV there and not charge it because it's an EV spot.

**Mike Harrison:** Do you guys meet on the weekend and talk about all your cool things?

**Dave Jones:** Oh, there's an app. I don't know if you, there's the there's an app we have with all the local charge and people take photos of other cars and they, this car has been here for half an hour. And I can't, you know, and they like out of, yeah.

**Chris Gammell:** It's great. One thing that's just opened a couple of weeks ago near us is the first electric forecourts, they call it. Yes. I saw that. That's huge. Yeah. It's got like eight 350 kilowatt chargers. It's a grid serve. Yeah. Yeah.

**Dave Jones:** I saw a tour of that. Wow. And it's got a big showroom. They'll, they'll actually loan you out EVs. It's like a big showroom thing, isn't it?

**Chris Gammell:** They've got a few sort of business models. They've got a six megawatt hour on, on site battery. So part of their business model is, is you're selling that, but the use of that battery to the grid for grid balancing and doing the charging. And it's like a, yeah. So like a car service station.

**Dave Jones:** That's not, that's novel.

**Chris Gammell:** So yeah, they, I think they, they say they're planning a hundred locations in the UK, probably not as big as that one. Um, but that's their,

**Dave Jones:** so they could just make money from selling grid storage.

**Chris Gammell:** Yeah. I, I, yeah. I think it'll be a while before rapid charger companies can make money just from charging.

**Dave Jones:** Oh yeah. No, I don't, I don't think that might ever be possible. You've got to make money some other way. I think.

**Mike Harrison:** Difficult one.

**Dave Jones:** Yeah.

**Mike Harrison:** And so this is a, this is like a, it's like a station effectively. It's like a,

**Chris Gammell:** yeah. Yeah. Imagine a gas station, but we're just chargers and no petrol pumps.

**Mike Harrison:** Okay. Yeah. I mean, the gas station, petrol stations, they make all their money on the soda anyways. Right. So you just got to make a nice lounge.

**Dave Jones:** But it's got like, it's a large building. It's got like a luxurious, you know, you can go sit on the lounges in the luxurious rooms and they've even got EV cars that you can try. Oh, so you go there and you can actually load one. Got it. So they're doing like all the upsells. Yeah.

**Chris Gammell:** Yeah. It's like, it's like a leasing thing. They also got like bookable meeting rooms, for example. Oh, right.

**Mike Harrison:** Wow. Yeah. Making money. It's interesting how that might, that might change kind of like social structures and like, you know, if, if there's like a built in charge time you have to do, you know?

**Chris Gammell:** Yeah. Yeah. What do you do when your car's charging? Yeah. Can you get money out of people? Right. Exactly. Yeah.

**Dave Jones:** Yeah. Because the, the problem is it will never be as fast as filling up a petrol tank. Cause I, I actually timed it. People asked me to do the, we were debating this on the EV blog forum. So I went bugger it. Next time I'm going to the petrol station, I'm going to check. This is before I had my EV. I, I actually timed it. And it was three minutes from when I parked up to the pump, filled up my car from zero to full. And I cleaned my window and I cleaned my windscreen and everything. Walked inside. Yeah. Paid. Came back out. It was three minutes before I drove. You pay inside? That's so weird. From when I drove in to drive off. With, with, and, and, and, and that gives me five to 600 kilometers of range in three minutes. And I cleaned my windows and got some snacks from the server. Like, you know, EVs will never be that quick and convenient. I, I just don't see it.

**Chris Gammell:** No, no, that, that's true. And people say, oh, but hydrogen, but hydrogen, no, no,

**Dave Jones:** no, that's what's, what's your take on hydrogen?

**Chris Gammell:** The efficiency is terrible. Yep. The infrastructure will never, but yeah, the, the cost of the infrastructure and you can't charge at home.

**Dave Jones:** Yeah. So, yeah, it's,

**Dave Jones:** oh, but, but, but the, but the hydrogen aficionado saying, oh yeah, we, we have these portable ones you can install in your house. Like these hydrogen tanks you can put on the outside. They're, they're serious. I mean, yeah, they still think it's going to work.

**Mike Harrison:** All you need is to put some, you know, just, you know, drop your, your electrical leads into some water and then get a collection tank above it. You're good. Yeah.

**Chris Gammell:** There might be a few, like the occasional niche, like say someone running a truck, you know, truck depot. A truck depot or something. Yeah, maybe. And whatever, but it's just, yeah, no, no, no, just no. No. The efficiency, the efficiency, I agree. Something like 30%, you know, energy to wheel through hydrogen versus, you know, I know 70% of some of the EVs. It's just, you know, that alone just knocks it out.

**Dave Jones:** Yep. Nah. And the fact that you can't do it at home unless you have these high pressure tanks strapped to the side of your house.

**Chris Gammell:** I think people, people who haven't had an EV just don't appreciate the whole charge at home. That is one of the biggest advantages.

**Dave Jones:** It's just, yeah. It's, it's just something you just don't have to worry about. Although if I'm going on a trip, I've got a plan. Oh, look, I'm going, like I'm going on a long trip up the mountains tomorrow. I need to make sure it's, you know, 80, 90% charged, you know?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** But yeah, apart from that, like it's not hard to put a little bit of thought into it.

**Chris Gammell:** No, no, yeah, it does need a little, slightly more planning, but yeah, the savings, obviously the savings depend a lot on how much electricity costs in your country. You know, if you can't charge at home and have to use public charges and they're not free, then it's still cheaper than petrol, but not that much. Certainly in the UK.

**Dave Jones:** Yeah.

**Chris Gammell:** But the other charge at home, it's literally in the UK with an overnight tariff. You're talking something like one and a half P pennies per mile, which is, you know, it's just so cheap. Yeah. It's the running cost. And if you do a decent, yeah, if you do enough mileage, I think it's, it's probably the sort of thing, the ideal situation is where you're doing, you know, a fair amount of mileage every day, but not so much really, really long trip so that you maximize the use of charging at home.

**Mike Harrison:** Yeah. Yeah. Like a long, long commute or something like that versus like a, you know, you're going back and forth to it.

**Chris Gammell:** And that's before you start looking at the various tax incentives. Like you're in the UK, there's like no road tax. There's no London congestion charge. There's quite a lot of other towns and cities are putting fairly major incentives in which, okay, they might not last forever, but for the moment, you know, they're very valuable. And it's in some cases, it's just a no brainer.

**Dave Jones:** Yeah. Speaking about homes, Mike, have you seen any change this year? What are your experiences with the change in, in, in the community about working, you know, working from home and, you know, big, big businesses downsizing because half their employees are now working from home permanently. Have you seen any? I think,

**Chris Gammell:** yeah, I think the one, the, one of the things this situation has shown is that, you know, working from home can work. And I think a lot of people is accelerated what was probably going to happen anyway.

**Dave Jones:** But it, but it may not have, it probably needed this sort of kick in the guts, didn't it? Yeah.

**Mike Harrison:** Right. To change its actual policy and stuff like that. You mean? Yeah. Yeah.

**Chris Gammell:** Yeah. I wouldn't be wanting to invest in commercial real estate anytime soon. That's for sure.

**Mike Harrison:** Fire or sale, fire or sale prices. Yeah. Yeah.

**Dave Jones:** Not a big ones. I find there's still market for the small ones because, you know, but everyone's down. Yeah. A lot of them are downsizing. So yeah.

**Mike Harrison:** Yeah. I think especially, I think coworking spaces might actually do better in general if people are going to keep doing remote, but.

**Dave Jones:** Weren't they dying the whole WeWork thing?

**Mike Harrison:** Yeah. But I mean, so like, I think WeWork will, you know, like, yeah, WeWork is totally over, oversold or overbought, I guess. Right. But they, I think that when things do come back, if, so if you imagine like you get another year of companies saying like, yeah, you can work from home, but people are like, I haven't seen anyone for a year. I would really love to be near other people. You know, like that's. I've actually been doing this really interesting kind of weird thing. It's called cave day. You guys ever heard of cave day?

**Dave Jones:** No.

**Mike Harrison:** Basically it's a, you, you basically get on a zoom call with a bunch of other people and you talk about what you're going to work on. And then you just like literally have a zoom call with your webcam on and you're just working in front of other people. And like, it sounds super dumb, but I'll tell you what, I bill almost twice as much because like, just like the social, the, like the weird part of your brain, like the social pressure I've been, I've been billing and doing so much more work. And like, like today I did like three hours straight of like firmware, which for me is torture. But like, I just was able to get through it because I, you know, I had committed to doing it and I, I don't know. It was, it's, it's crazy. It's like a weird brain hack and it might not work for everyone, but it's, it's sure working for me. I don't know why.

**Chris Gammell:** So writing firmware with other people watching you.

**Dave Jones:** What's that? Yeah.

**Mike Harrison:** But who's going to be watching you?

**Dave Jones:** They can't be productive and watch you and vice versa.

**Mike Harrison:** No, it's literally,

**Mike Harrison:** it's just like out of the corner of my eye, I see them also in front of their camera and it's not like they're watching me, watching me. Like it's not like they're watching my code. I wouldn't let them do that anyway, but it's like, they're just there on camera and I'm on camera. It's like, it's really,

**Dave Jones:** that doesn't work with engineers. Sorry. That's not going to know. Engineers. Well, at least one engineer Dave, it works. So, and I did this also with, uh, yeah, but you're, you're, you're a weird yank. You know,

**Mike Harrison:** I did this with at least six other engineers as well. So nah,

**Dave Jones:** nah, nah, well, thanks.

**Mike Harrison:** Maybe, maybe, you know, cave dweller such as Dave won't be a thing, but Mike,

**Dave Jones:** Mike, yay or nay?

**Mike Harrison:** No, no, don't like working. Not for everyone.

**Mike Harrison:** For me,

**Mike Harrison:** it worked great. So.

**Dave Jones:** Boy, we're at two hours guys.

**Chris Gammell:** Yeah.

**Dave Jones:** I think an hour, that was EVs. It was. Yeah. Split the EVs out as a second show. Sorry,

**Mike Harrison:** Chris. I feel like maybe I should like cut in with the edit and be like, warning, the next 45 minutes will be about exclusively. But you know, that's great. I think that people are interested in that stuff. I mean, it's, I think, I think a lot of people in our audience are at least thinking about it. Right. And then it comes down to just the trade-offs and whether it makes sense.

**Dave Jones:** You're doing it again, Chris, you're doing it again. You're going back there.

**Mike Harrison:** What? EVs. Oh, yeah. I'm just trying to justify what you've been talking about the whole time, Dave. Come on.

**Dave Jones:** You've been sucked back into the hole.

**Mike Harrison:** All right. Nevermind. We'll talk about it another time. Is there anything else we need to absolutely cover?

**Dave Jones:** Otherwise.

**Chris Gammell:** I've got a very micro rant. Oh, yes. Lattice semiconductor.

**Dave Jones:** Oh, what have they done?

**Chris Gammell:** They have made the software to use their old, their really old CPLDs. You now have to pay for it. And it used to be free. It's, I think, something like $500 a year or something. So if I want to buy, I've used that.

**Mike Harrison:** People who need to pay for supporting engineers.

**Chris Gammell:** My guess is they are having to pay. You know, when you compile a PLD, you get so many copyright notices. They are probably having to pay someone for some of the things they include in that tool chain. So that's my guess. But it means, yeah, I've only used that. You had two, two, two designs for those devices in it. It basically means that if I need to make any changes to those, I have to pay 500 bucks, which I'll just charge to my client, but it's, it's a bit.

**Mike Harrison:** $500 just for the software though. Not for like, not, not per change.

**Chris Gammell:** Yeah. Not for the software for a year, a year's license. Yeah. Yeah. Yeah.

**Dave Jones:** I don't see that catching on.

**Chris Gammell:** I think that, yeah, they're trying to make it go away,

**Dave Jones:** but I don't see, can you see any other manufacturers going, Oh, wow. You know, they let us got away with it. I don't know. There's a bit of kerfuffle on the amp out, but that was about it.

**Chris Gammell:** I can't see they're actually doing it for a profit, but maybe they're just trying to make the old products go away somehow. I don't know.

**Mike Harrison:** I bet they're using it as a, as a lever to get people to, I mean, there is new stuff, right? I mean, like there, there are upgrade paths, but people probably aren't taking them because.

**Chris Gammell:** Not with CPLDs. Yeah. CPLDs are the whole thing is they, they're a simple device. It's good enough for the job and their design probably hasn't changed in the last 10 years. Right.

**Mike Harrison:** Exactly. Yep. Yeah. 20. Right. But they want to sell bigger, better FPGAs.

**Dave Jones:** So can you still buy like a 16 V8 and stuff like that?

**Chris Gammell:** Yeah. Yeah. This is for the, yes, you can. Um, but this is for the slight, the next ones up the, you know, like the 70s in micro cell devices, that sort of scale.

**Chris Gammell:** Yeah. Right. They're not quite big enough for an FPGA or I want a small pin count type devices.

**Dave Jones:** Or you want better timing and stuff like that because the FPGAs, their routing's a bit more loosey goosey than the, uh, let's just say than the CPLDs. So yeah. It's predictable. A bit more predictable. Yes. Well,

**Chris Gammell:** FPGAs are probably way faster, but if you don't need the speed, I think it's more just about you want a simple low complexity device without too many pins.

**Dave Jones:** Yep. Pin counts. Always my bugbear. It's like, geez, I, yeah, I need an FPGA, but I only want 20 pins. Like, holy shit. Why do I have to buy a 500 pin device to get this macro cell count? You know, bastards.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm sure we were ranting about that a decade ago on the first day. I think we were. Yes, definitely. Still. Yeah.

**Mike Harrison:** We will be, uh, having on. So while Dave's going to be on holiday next, starting next week, I think.

**Dave Jones:** Yes. On end of. Yeah.

**Mike Harrison:** So, uh, we are going to be talking with a couple of guests. One of them is Brian, Brian faith from one of the other, one of the newer FPGA companies. So they're the ones who did the, uh, open tool chain. So they basically, as a company, they said, Hey, we're going to use the, you know, Reosis and all the open tool chain stuff. So, uh, I'll try and post a question. Uh, it's quick, quick logic. Sorry. It's a quick logic. Does they, they basically are doing like a fully open tool chain, which is super cool. So, yeah, yeah.

**Mike Harrison:** That's good. Awesome. Yeah. All right. Thank you very much, Mike, for joining us. Yeah, Mike. Thanks for joining. Yeah.

**Chris Gammell:** It's been fun.

**Mike Harrison:** Yeah.

**Chris Gammell:** Have a good new year. Yeah. Thanks man. It can't be, it can't be worse than this year. Yeah. 2021. I'm sure.

**Dave Jones:** 2021 by the time everyone hears this. Yeah. And it'll all be over. Don't worry. It's 20. Well, you know, guys,

**Mike Harrison:** there's still time actually there between when we recorded this and 2021, there may have been an asteroid strike.

**Dave Jones:** So I was about to say asteroid strike. Yeah. That's the only thing left for 2020, right?

**Mike Harrison:** Or a big solar storm. Right. Right.

**Dave Jones:** And then our EVs don't drive anymore because we just got, only the petrol cars work anymore. The, the, like the real old ones.

**Chris Gammell:** Yeah. They did just have a big earthquake in Eastern Europe somewhere. I think.

**Mike Harrison:** There's still time. There's still time. Well, it's, it's been real then guys. It's been real. Yeah. It's next time. Yeah. Okay.

**Chris Gammell:** Cheers.

**Mike Harrison:** You just finished listening to this episode. And that means you made it to 2021. Our past, current and future episodes are only made possible by our patrons. Make this the year, become a part of the club and hang out all throughout the year with other patrons at patreon.com slash the end hour. A special thanks today to our corporate sponsor, Bino.

**Speaker ?:** Bye.
