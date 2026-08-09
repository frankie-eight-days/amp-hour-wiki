---
episode: 412
title: 3 Cent Micros And 1000s of LEDs
url: https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/
---

**Chris Gammell:** This is The Amp Hour Podcast, released October 21st, 2018. Episode 412, 3 Cent Micros and Thousands of LEDs.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Mike Harrison:** And I'm Mike Harrison from Mike's Electric Stuff.

**Dave Jones:** And what's that echo sound I can hear? That's the lack of Chris. He's not here this week, it's just us.

**Mike Harrison:** Yeah, he's skiving off.

**Dave Jones:** Awesome. Welcome back. How long's it been?

**Mike Harrison:** Oh, ages. It's about once a year or something on average.

**Dave Jones:** Yeah, I know you've been on a couple of times with Chris.

**Mike Harrison:** Yeah, I think it's about once a year. Because you were like overseas.

**Dave Jones:** Oh, right. Yeah, okay. Yep. Galloping, because you guys often find yourself in the same country, don't you, or something?

**Mike Harrison:** I have done it on occasions. Belgrade or Pasadena or wherever. Well, I went to Make Affair this year in New York, but he wasn't there. Oh, right. Yeah, so how was that? Yeah, it was good. It was, you know, the New York I've not done before. So it's like a different crowd of cool people. And, again, most of the interesting stuff was like the evening events, sort of talking to people, comparing gadgets, and, you know, this little bar.

**Dave Jones:** Oh, okay. These are just, right, these are private, you know, hack things. Or private-ish, yeah.

**Mike Harrison:** Or private-ish, yeah.

**Dave Jones:** Exactly. So did you go over there just for that?

**Mike Harrison:** Yeah, it was like Make Affair plus like a couple of days' tourism, a day or two tourism either side sort of thing, just wandering around various bits of New York.

**Dave Jones:** Yep. Cool.

**Mike Harrison:** I've been there for like about 20-odd years.

**Speaker ?:** Yeah.

**Dave Jones:** How do you find New York?

**Mike Harrison:** Yeah, it's very, and it's pretty much as expected, you know, just ridiculously busy, crowded, noisy. Yep.

**Dave Jones:** Smelly, dirty. Yeah.

**Mike Harrison:** Yeah. Yeah. So the transport system is pretty decrepit. Where I was staying out near the, where the Make Affair was in the area called Flushing in Queens and it's where the subway runs on like overhead tracks over the road, which obviously makes the road really dark and dingy, but just it looks so like rusty and I'm sure it's safe, but anything that's, anything isn't direct safety related does seem in need of a great deal of care and the TLC. It's just, and just the noise when the train went past was just unbelievable. You know, it was clattering over the rail joints directly overhead. It was just, you know, ridiculous. So is the... We were a bit spoiled in London. Our system isn't great, but it is generally pretty good.

**Dave Jones:** Yeah, I thought it was pretty good when I was there, but granted it was quite a while back, but, you know, I was pretty impressed with the underground, you know, system and stuff. I know you locals would probably disagree, but, you know, I was kind of impressed. I was coming from Sydney whose public transport infrastructure sucks, you know.

**Mike Harrison:** Yeah.

**Dave Jones:** So, yeah. So what have you been up to? This last couple of years, just still doing contract?

**Mike Harrison:** Yeah, same sort of business area, lead stuff. I've actually just stuck a load of new projects on my website, whitewing.co.uk.

**Dave Jones:** I see that.

**Mike Harrison:** Some sort of fairly recent stuff. Annoyingly, a lot of the stuff recently has been basically making our own lead strips because we can't, you know, there aren't really sources of really good quality lead tape. Right. And, you know, what I would really love is someone like Osram and TI to get together and do their own, like, chip, you know, driver plus lead in one package.

**Dave Jones:** Got it. And they're guaranteed high quality leads. Is that the problem? Exactly.

**Mike Harrison:** And also just the, I mean, the other problem with, like, the 2812, for example, the one wire is fine, but the problem is you've only got eight bits per color, which means you don't really have any global dimming. Right. And the APA 102, which is the two wire one, is better in it. You know, you've got SPI, it's much easier to drive. You've got, I think, five bits of global control, but the PWM starts getting quite slow once you do that. And the 102 isn't actually even constant current. You know, if your supply voltage drops from, like, four and a half to four volts, your intensity drops. Oh. So it's all a bit.

**Dave Jones:** Wow. Yeah, that's not terrific for the kind of stuff you're doing. Consistencies, yeah. Yeah. So the global control would be important for, I would assume, for your art installations because you're always, like, dimming the whole lot if you've got 10,000 legs.

**Mike Harrison:** Yeah. But so if you've got just some pattern going on that's using all 256, you know, intensity levels, that's it. If you want to then dim that down, you then start eating into those intensity levels. And 256 isn't enough anyway because you generally need to do gamma. If you want to do a nice smooth fade from, like, off to on, you need to do gamma correction. So you need really a minimum of 12 bits control to do that.

**Dave Jones:** Eight bits isn't enough. I'm quite surprised by that.

**Mike Harrison:** Well, basically, it's a roughly square law. Basically, if you take an eight-bit linear thing and do a linear fade from zero to 256, the bottom, you'll see, like, about 16 steps at the bottom, and then it all just looks like on. Oh, right.

**Dave Jones:** So is this the eye response doing this? Yeah, because the lead is actually linear light output pretty roughly.

**Mike Harrison:** Yeah, it is our response. And a very good first approximation is if you've got, say, 12-bit hardware, if you take it, eight-bit values are fine if you then post-correct them. So if you take your eight-bit value, square it, and then use the top however many bits you've got in your hardware. Right. That works really well. And ideally, you want 10 you can just about get away with, 12 is fine. So you can do a really nice smooth fade from, like, all the way off to all the way on, and it looks fairly linear and even.

**Dave Jones:** Ah, so there's more magic going on there than you would think. Can you explain the gamut correction for us?

**Mike Harrison:** Yeah, and that term originates back from CRT days because the phosphor on a CRT, again, is non-linear. So cameras pre-correct that because, obviously, it's easier to do that in the camera than all the TVs. But, yeah, gamma correction in general is basically just meaning putting some sort of translation curve between your input values and your output values. And so in the case of LEDs, or I think light sources in general, yeah, I've never looked into the detailed science of it, but empirically is what it actually looks like. It's a roughly square law. So, for example, if you want double the brightness, you have to give it four times as much power. Right. So you're just applying an inverse to the eye response.

**Dave Jones:** And that's different for R, G, E, and B, right?

**Mike Harrison:** No, I don't think there's enough difference to it. If you're going for a really precise color, then maybe. But the vast majority of the stuff I do is like white anyway because it's so much more power efficient. It's like maybe five to ten times more power efficient in terms of the amount you get out for a white LED versus RGB. Right. And, in fact, a lot of the stuff that I do now is RGBW so that you use the white to give you the punch and the power, and then the RGB just tints it.

**Dave Jones:** Oh, I didn't know you could get RGBWs.

**Mike Harrison:** Well, what I tend to do for the smaller stuff, most of the stuff I do use is a lot of quite small LED. So I tend to use an RGB LED and a white LED next to it. Right. Okay. The higher power ones, you can get them all in one device.

**Mike Harrison:** And you can get RGBW LED tape now because they've realized that for decorative applications, RGB is horrible. I mean, if you've ever seen RGB trying to do white, it just looks horrible.

**Dave Jones:** You're right. Right. Okay.

**Mike Harrison:** Because you've got three dies, each of which has an intensity and a peak wavelength variation. So trying to match those is just not going to happen.

**Dave Jones:** Even if you put a white phosphor lens over the front of it? Well, that becomes a separate thing. But then, of course, it ruins it, right? Because then you can't get out the RGB. You might as well have a white LED. Yeah. Yeah.

**Mike Harrison:** So you just take a white LED next to it. And that gives a... It means that you can do subtle pastel colors rather than horrible disco garish stuff. And it means you get fairly decent efficiency.

**Dave Jones:** Right. Because a white LED is just a blue LED with a phosphor, right? So effectively... Is that still the case?

**Mike Harrison:** Yes.

**Dave Jones:** Or have they got some new whiz-bang thing?

**Mike Harrison:** No, that's it.

**Dave Jones:** Still covers it, right? Yeah.

**Mike Harrison:** I mean, you occasionally get things like these, the high CRI stuff. They add like an amber or a red along with the white just to tint it. Oh, okay.

**Dave Jones:** Just to give the broader spectrum kind of...

**Speaker ?:** Exactly, the spectrum.

**Dave Jones:** Kind of.

**Mike Harrison:** Yep. Got it. Okay. I don't think they've yet got phosphors that can actually do that. So they tend to... All the ones I've ever seen just have some additional LEDs. Either red or orange or whatever.

**Dave Jones:** I didn't know that they corrected that. That's how they improve the CRI. I thought it was just, you know, more carefully controlled phosphors and LEDs or whatnot.

**Mike Harrison:** Maybe there are some cleverer phosphors out there. I've not looked in that in that much detail. It's possible. I don't know.

**Dave Jones:** Fascinating. There's just so much science behind LEDs. It's really... And how the eye perceives them and stuff like that. I find it really remarkable.

**Mike Harrison:** Yeah.

**Dave Jones:** You know, you could do a PhD thesis on it. Many people have.

**Mike Harrison:** And there's also things like... Which, again, I've never looked into the science, but purely empirically, is what I call the point saturation effect. Is that if you look at an array of LEDs and you're just looking at the LEDs, the eye tends to saturate on the point. So you don't tend to see grace goes. Your eye just sees, oh, this thing is on. You don't really get much gradation. Whereas if you then stick a diffuser in front of that, you then see the... For example, you start seeing the differences from LED to LED. Interesting. If you imagine you've got this really bright thing in your field of view, the eye is basically adjusting itself. And all it sees is this bright blob. And it doesn't really give you any indication of how bright it is. So the difference between diffuser and non-diffuser is huge. Certainly a close eye. As you move to the distance, obviously the distance acts as a diffuser. But there's lots of things like that that you just only notice once you start playing with this stuff. I'm sure there's science behind it, but... Right.

**Dave Jones:** So do you find yourself putting diffusers on, have to put diffusers on these various projects, like custom ones?

**Mike Harrison:** Depends on the application. Anything that's viewed vaguely close up, yes, pretty much needs a diffuser. Stuff that's further away, then the distance does that. But generally, you know, if you want something that looks nice and subtle and not dotty... Some people like dotty. I mean, some people like that effect. But if you just create a blob of light or like a strip of light, then you generally do need to put stuff in diffusion of some sort.

**Dave Jones:** And that's pretty much up to the artist, isn't it, though? Yeah, yeah. Do they, like, have a clue about these LED stuff? Some. Oh, do you?

**Mike Harrison:** Through experience, yes. Different customers have different backgrounds. Some of them have actually got lighting designers on board who know some of it. But, I mean, I've had some hilarious... Probably the best one was this was a large conference table, which was made of Corian, which is like an acrylic silica type mix. This is homework top. But if you machine it really thin, it works with quite a nice diffuser. They made this beautiful conference table, which had lead strips, like an array of strips inside it. The idea is that when you go to a meeting, you press a button, the bar starts and then it starts reducing. So it's like a timer for your conference.

**Dave Jones:** Oh, okay.

**Mike Harrison:** Right. So they made this thing. They tested it in the factory. The client came down. Yeah, yeah, that's fine. That looks great. They then installed it in a corner office, which had windows both sides. Oh, okay.

**Dave Jones:** It didn't look right enough. They couldn't see it.

**Mike Harrison:** Yeah, they didn't appreciate how good the eye is at compensating between artificial light and sunlight. So at the last minute, I think we added another four sets of lead strips in there just to boost it up. Oh, wow.

**Dave Jones:** And that depends on whether or not you're on one side of the building or the other, you know, whether you get the full sun coming through.

**Mike Harrison:** I think it was basically just daylight versus artificial light. It was as simple as that.

**Dave Jones:** Oh, okay, yeah. Yeah, yeah. Which is a big difference because your average office, I think the, do you know what the legal requirement in the UK is? Because here I think it's like 200 lux on your desk. That's the legal, which isn't much.

**Mike Harrison:** No. 200 lux isn't. But if you're playing with like LDRs or any photo sensor, just the difference between like daytime and artificially is like factors of like 100 or something ridiculous.

**Dave Jones:** Yeah, it's enormous. Yeah, just having a window changes from 200 to, you know, 5,000 lux or something. Yeah, yeah.

**Mike Harrison:** Of course, the eye is so good that you don't really.

**Dave Jones:** The eye is fantastic. Yeah. It's a phenomenal thing. What is it? Like how many orders of magnitude? I have no idea. It's ridiculous. It's like 140 dB dynamic range or something. It's just insane. So I noticed like I'm looking through all your projects here and they're all just, am I wrong that almost every one is a lead project?

**Mike Harrison:** Yeah, pretty much so. There's a few things like the, we've done some stuff with large LCDs. If you go down to the dashboard. Oh, yeah, of course.

**Dave Jones:** Yeah, I remember the LCD ones. Yeah.

**Mike Harrison:** But the one thing that I'd really like to do that nobody seems to have done yet is a large scale e-ink type thing.

**Dave Jones:** Right.

**Mike Harrison:** Yep. Because, of course, that would be super low power, super high contrast. What I'd like is something like a 100 millimeter square single pixel e-ink device. Yes. Please. Right. Just a one pixel. Yeah. Yeah.

**Dave Jones:** Could you get, can you get custom e-ink displays?

**Mike Harrison:** I think you can. You probably can. And certainly when e-ink first came out, you know, all they were interested in was like Kindles and the millions and the million markets. Yeah, that's right. Obviously, you can now get smaller ones. And we may be now getting towards the point where you can get custom ones in moderately sensible sizes. We've not, I don't think anyone's really looked at that recently. Okay. But actually, one of the reasons my voice sounds a bit dodgy is I was talking to people all day at the UK Electronics Exhibition. And there's actually a couple of interesting things I saw there. One was a, like a, because one of the problems with LCDs, of course, is because you've got the polarizers, even when it's totally clear, you're losing 50% of the light because of those polarizers. Yeah. And there was one company that had some sort of shutter glass, which basically went from completely clear to like a 50% mirror type finish, which was interesting. Oh, right. Okay. Very early stages. But I said, look, you know, I've got a potential project coming up late next year, which wants probably something like two or 3,000 somethings in a big array. And it'll be nice if they weren't led. So they're going to sort of go away and talk to their people and see if they can come up with something. Interesting. But the other thing that was interesting was a company that specializes in like scientific, scientific optical stuff. Apparently it was founded by the guy that invented the auto darkening welding masks that then sold it to 3M. Oh, yeah, yeah. And this was an LCD that changes the transmitted light color according to applied voltage.

**Dave Jones:** It changes the color.

**Mike Harrison:** Yeah. It's like a tunable filter. I have no idea. It's magic. Wow. I think they've got a couple of different layers and it does some weird magic diffraction stuff. But they had this demo where literally they were shining a white torch from it and it was going from white to yellow to pink. Wow. So I think a big chandelier or something. It's like digital stained glass almost. Yeah, yeah.

**Dave Jones:** That is brilliant. That would be an interesting art piece, wouldn't it? Absolutely. To do like a church stained glass window that just changed color.

**Mike Harrison:** Wow. I think you have to pick the colors at manufacturing time. It's not like a full spectrum thing.

**Dave Jones:** Got it. Yeah.

**Mike Harrison:** But it'll show you two different colors. You can do a lot with that. I think a few of my customers got excited. Oh, let's take a color monitor and take the backlight off. But the problem is first you lose 50% of the polarizers. Oh, I was going to say. Then you lose two thirds through the RGB stripe filters. So you end up with at best about 15% of the light coming through. I mean, if you've ever taken apart a monitor and looked at how bright the actual backlight is, it's like you can barely look at it. It's crazy. I know.

**Dave Jones:** And I would assume that this new Whizbang Blackmagic technology would have quite a loss too. I can't imagine it's just going to be magically not much.

**Mike Harrison:** It does. But the fact you've got the color, that's what gives you the – Yeah, exactly. The thing that I did, that digital ornithology, that's the only one I've done with clear LCDs. I've done some stuff with LCDs that have like a reflector on the back, which works reasonably well. The only other one I've seen, there's a really good one that was done in the USA. It's like a bird museum where they've got this ribbon of LCDs. And they make really good use of the backlight from the skylights. And it's like a flock of birds flying overhead. But that's actually one of the nicer ones. But say if you're using clear LCDs, it's really dependent on having the lighting to actually make it work. Because the 50% at best means the things – they always look great. So these clear ones actually look quite interesting. But obviously you have no idea what the costs are, whether they're going to be – A, the costs are going to be viable, and B, whether the manufacturer is actually going to be interested in talking to us.

**Speaker ?:** Got it.

**Mike Harrison:** Yeah, they're interested in making like one-inch square scientific windows with dead flat spectral response and all this sort of stuff. And I say, look, I just want to tell you, it looks pretty.

**Dave Jones:** But I think if you went and said, oh, look, we need 3,000 of these for some installator, I think they'd go, ooh, we didn't figure on this market.

**Mike Harrison:** Yeah, possibly. I say I've asked them to quote just as a song. Like, okay, look, you know, if I wanted 100 mil square and I wanted 1,000 of them, just give me some idea. But both of these are products that aren't – they don't even have sampled units that you can buy yet. Right. Yeah. What I'd like to do is just literally bought a little like inch square sample and I'll just take it to my clients and show them. Because quite often things will come from, you know, oh, that's an inch thing. You can get a tech. I'll buy something, do a little demo unit, and then like a project will come from that. There's nothing like having it in your hand to inspire ideas.

**Dave Jones:** So it's basically just really talking at the product, like the product concept stage almost. It's like what if I had one of these, you know.

**Mike Harrison:** I think some of it may be a case of, you know, they've developed this thing and they don't really necessarily know exactly what they want to use it for. So they've done some demo pieces, but we'll see if they buy it.

**Dave Jones:** Right. Nice. Nice. So what happens to these? Because like art installations typically just go up for a certain amount of time and then they rip them down.

**Mike Harrison:** What happens to all these? Most of these are permanent. Oh, they are. The bigger ones. Right. So yeah, there's some temporary stuff. I've done a few temporary things. Obviously, some of the design, the design side of things is somewhat different, whether you're doing a temporary or a permanent thing. But most of the big ones are permanent. Yeah.

**Dave Jones:** Oh, okay. Yeah. Like the airport one and stuff, you know, that's hanging in the airport. It's going to be there for, you know, 10, 15 years until they, you know, change their mind and want a different one.

**Mike Harrison:** And if you're lucky, they've even got a maintenance budget to keep it going. Oh, okay.

**Dave Jones:** So do they hire you to maintain it? No, no.

**Mike Harrison:** It's because it's such a random thing. It's very hard to find third parties. It's my clients generally handle that side of things. Okay. Because actually one of the, when I was in New York, one of the things I went, I actually went to one of the big installations that was done a few years ago that I've never seen in person, which was the iPod Nano thing. Which again, that's been maintained and that still looks really good.

**Dave Jones:** Okay. And any failures on that? Or do they, like if one fails, they swap them out?

**Mike Harrison:** We certainly had quite a few initially. I don't know whether there's been any. I don't, I asked them the other day. I don't think they've had much in the way of failures over time. But I think, you know, once it was burnt in, I think it was pretty good.

**Dave Jones:** Because a lot of these installations you would notice, like if something's out, right? Some of them you wouldn't, but some it's like, oh, God, one's failed. Do you have that?

**Mike Harrison:** The other stations I like are the ones which are like a random cluster of things. So if the other thing isn't working, you don't really notice. But this was like a big array. So even one out is very noticeable.

**Dave Jones:** So do you have any sort of like rough gut feel stats for like the failure rate of leads? Like, because you're usually like driving them full, like, you know, high power type stuff.

**Mike Harrison:** I'm extremely conservative. Oh, okay. I very rarely drive a lead at more than 50% of its rating and sometimes a lot less than that. Right, interesting. You know, I'll sooner like throw more leads at it and run them. Got it. I take the paranoid engineer thinking of everything that could go wrong and often scare the crap out of my customers when I explain all the things that could go wrong.

**Dave Jones:** Yeah, you don't want to tell the muggles all the gory details.

**Mike Harrison:** The worst thing you can say is, oh, yes, it's all fine. It's all going to work because, you know, if you tell them everything could go wrong and then it doesn't, then they're happy.

**Dave Jones:** Yeah, okay. But they wouldn't. Do you find that they often don't understand all the technical stuff you're telling them?

**Mike Harrison:** I think most of the customers I've been working with for quite a while, so they do now, and I generally know how to pitch things. I know what their level is. Right, okay. I know how to pitch. I mean, I don't like working with people that have no in-house technical because it means I've got to then handhold them. Exactly. I've got an in-house guy that I can throw him aboard. He can wire it up without reverse plouting and smoking it. You know, he can get data going too. There's nothing I hate more than just, you know, writing noddy instructions for, you know, people that don't know what they're doing. I absolutely hate that, and I've, you know, quite often just not even take on jobs if I get a sniff that they don't really know what they're doing. It's just not worth my time.

**Dave Jones:** You just turn them down, yeah. Yeah, yeah. What percentage of jobs would you turn down, roughly?

**Mike Harrison:** Well, I'm trying and failing to sort of not take on so much so I can do some more work on my own stuff. A lot of the stuff is repeat business. But, I mean, I would say easily once a week I get a random query from someone I've never heard of. Sometimes it's, you know, XYZ recommended you, and I don't know who XYZ is because it's a second or third-hand recommendation. Oh, no, okay. Or they've come across the website or come across my website via one of my clients' things. So, things from just total random as I've never heard of from before. Unless it's something that looks really interesting, I'll generally just turn down because I just want to try and, you know, not be doing stuff. Because, you know, I don't need to take the jobs on for the money and I'd sooner have the time. But that's sort of only partially working.

**Dave Jones:** Do you ever get sick of lead projects? Or do you like working on stuff that you know?

**Mike Harrison:** Yeah, I like stuff that's different. You know, I'd really love to do something for these new LCDs. I'd love to do something with the ink. We've done some stuff with big OLEDs, you know, like big sheet OLEDs before. But, you know, it's really pretty much the only game in town. So, it's a case of interesting arrangements. You know, we've done quite a few, like, ring-type stuff using, like, thin PCBs, like, wrapped around into rings and unusual mechanical arrangements and so on. That's where I'm starting to get a bit more into some of the mechanical sides of things, which adds a bit more of an interest to it. But, I mean, every job's different and every job you learn something.

**Dave Jones:** Yeah. Would you, like, turn down, like, a job, like, oh, I need this protocol converter, that serial converter board, please?

**Speaker ?:** No, I wouldn't be.

**Mike Harrison:** I mean, I basically don't do any stuff for production these days. Right. It's basically design it, build it, next job. Because, you know, the next new job is always more interesting than what I'm working on now. Got it. Yeah, production stuff, you've got all the documentation and loads of other stuff. But also, there's a big, like, you give them a prototype, they go and test it, then it comes back three months later, then something else, then three months later, you've forgotten about it. Whereas, it's generally more, you know, the whole time scale is a lot more compressed. I've got a lot more control. Because it's a small job, I'll just run it on my pick and place. I don't have to deal with subcontractors. Yeah. So, it's just, you know, it's easier. It's a lower proportion of the boring bits, basically. Got it.

**Dave Jones:** How's the pick and place going? It's still churning along? Yeah, it's fine. Yeah, maintenance-wise?

**Mike Harrison:** Sometimes you'll, like, lie idle for a month, then it'll get used to something. But it's absolutely worth it. Absolutely. Right. Yeah. Because just dealing with subcontractors, I've yet to find, I had a really good subcontractor where I could just throw them an order. I didn't even bother getting them to quote, because I knew the price would be good. I knew the quality would be fine. But the guy retired a couple of years ago, and I've yet to find someone that's as good as them. In terms of, they were just the right size. But, yeah, it's a perennial problem dealing with subcontractors. I hate it. So, if I can do something myself. You do it.

**Dave Jones:** But we have to, once again, we probably have to, for the benefit of our audience who see you successfully using a pick and place machine, I've got to say that if you think you have a need for a pick and place machine, there's probably a 90% chance that you don't.

**Mike Harrison:** Yeah, I'd agree. I think that's changing with the decreasing cost, the entry cost. Okay. Right. Yeah, there are certainly a lot more people now who would have a genuine use to have a pick and place machine in their business. Yeah. Right. If you are churning out relatively low numbers of boards, a high mix, you need stuff turned around quickly, then it's becoming a much more attractive option. As long as you understand that it is going to take you some time to get the process sorted out, get all the software flow. I spent quite a long time getting a very slick software process. So, for example, all my PCB library parts are the same way around as the tape in my feeders. So, if I stick a lead on the board that I've used before, I don't need to check it's going to be the right way around. Yeah. Because I know it's going to be because the orientation is right. So, it's little details like that. But, yeah, it's – obviously, the reduced entry cost is, you know, people are starting to see, well, that looks interesting. And in some cases it is. But it is something – certainly, until you have actually used a pick and place machine, you only know a small proportion of the issues. Right. Because it's not one big problem. It's lots and lots and lots and lots of tiny, tiny issues. And little ones that will kill you. Classic example here. I occasionally did jobs on, like, ridiculous timescales. This was one of them. It was to make a – it was something like a 20 by 25 white-lead matrix on a semi-flexible board to go around. It's for a film shoot. They wanted to have text scrolling around a cup. Oh, okay. Right. So, from initial discussions with clients, delivering 10 of these was slightly over a week.

**Dave Jones:** Wow. Nice.

**Mike Harrison:** Which, for me, because, for example, a lot of the software stuff I already had, the driver architecture I already had. So, it's basically a PCB layout job, an assembly job. Got it. Yeah. Which would have been fine, except the LEDs that I – basically, we had to use the LEDs. They were just like 06, 03 or 08. It might be an 08 or 5 white LED. Nothing special. But we could only use the stuff that DigiKey had enough stock of. So, that was our choice of LED. And the tape they came on was really, really thin. So, that when my machine fed it, the tape would advance and the LED would just bounce straight out of the tape.

**Chris Gammell:** Oh, no. Oh, no. Oh, no.

**Mike Harrison:** So, my half-day contingency was more than taken up with modifying my feeder to just make it only lose – I think I got it down to about 10%. Right. Fortunately, I think the whole bill was like about 22,000 LEDs. So, fortunately, DigiKey did have one more reel in stock that I needed just to cover all the ones that I'd lost. Oh, wow. And there was enough time to get it. But it's just loads of – Hang on. 22,000? Yeah. It's about 2,000 LEDs on each board.

**Dave Jones:** Why did you need that many LEDs to scroll around?

**Mike Harrison:** It was about 2,000 LEDs per board. Oh, wow. And they wanted graphics. I don't remember the exact job parameters off the top of my head. Wow. Actually, I've got it in front of me. It's about – I think the pitch looks about 3 by 3 millimeters. And this whole thing is about, yes, 70 by 100. Oh, okay. And it was actually done on – it's quite – I found a company that will make 0.1 millimeter FR4 boards. Nice. And it's basically the stuff they use for the inside layer of multi-layer. So, it's not an exotic material.

**Dave Jones:** It is the pre-prig. I've done that before. It's stock stuff. They order these pre-prigs, and they have them in stock. They use them for people who don't know to build up the multi-layer boards.

**Mike Harrison:** I've only found this one place that will actually do that as a finished board. So, I don't know if maybe they've just made up jigs or something. So, obviously, it's really floppy so that – Oh, they're super flexible, aren't they? But the nice thing is, unlike my last stuff, is literally you can just tape it down to a bit of standard FR4 with capstone tape, pick and place and reflow it as if it was an ordinary PCB. Yeah. You don't have to use a vacuum bed or anything exotic like that because it wants to stay flat. Exactly. Whereas the capstone stuff wants to curl up as soon as you look at it and you've got attention and so on.

**Dave Jones:** Yep. Yeah, they're great. The thin PCBs are fantastic. But, yeah, as you said, yeah, you've got to find a manufacturer who's willing to just give you that pre-prig as a finished board.

**Mike Harrison:** Just pure chance that I'd seen another job that one of my customers had done on another job using that material. I thought, well, that's interesting. Who makes that? Yep. So, just pure luck. I happen to know that. And they turned around – I think it was 10 of these boards. They turned around in two days. And that was, I think, 60 pounds each for like 100 by 80 boards.

**Dave Jones:** Well, it's not much for that sort of turnaround. Exactly. And that sort of low volume. Yep. Sweet. So, let's get on to the stuff where both of us found interesting recently is the 3-cent microcontroller. Yes. Why do you find – because a lot of people make the argument, and it's a reasonable argument, that, well, look, why bother learning a new platform when you can get a pick one for like – what's the cheapest pick? 30 cents, maybe? The 10 series?

**Mike Harrison:** 35 cents on a SOC 23 something. Sorry, how much? I think it's about 30, 40 odd cents, something of that order. Right. Yep. For like the SOC 23-5 – SOC 23-6, rather. Yep. But this is an order of magnitude cheaper. Yeah. The answer is if you're making crap loads of things. Yep. Yeah. Unless you're up into like well into the 100Ks, it doesn't really matter if your micro is 3 cents or 8 cents.

**Chris Gammell:** Yeah, exactly.

**Mike Harrison:** You know, it's the point at which that cost delta is worth the effort of using a weird chip.

**Dave Jones:** Yes, that's right.

**Mike Harrison:** You know, if you save like, I don't know, 10 cents on your bill of material on like 100,000, that's what? 10,000 odd. So if you can spend less than that amount of money on the engineering, you're into profit. So, no, actually what I found more interesting was the LCSC website was a bit of a sort of revelation to me. I was vaguely – is it LCSC? Yeah, LCSC.com. Yes, that's it. And it's an offshoot of the JLC cheap PCB guys. And I was vaguely aware of that they had a part site. And I think I'd vaguely skimmed through it in the past and assumed it was just like jelly bean stuff. But I've been recently looking at a potential sort of consumer-ish project, which is high volume. So I just started having a look at this just to look at, you know, do they do interesting lab drives? And I just found this huge list of all these weird Chinese chips. I know. They're great. Half of which with only Chinese data sheets. And I literally spent – I've so far spent two complete evenings just going through ordering a few of these, a few of these, a few of these. Partly to test straight away, but partly just so I've got something on the shelf. So like if I have a job that needs like a 10-cent buck regulator, I've got one on the shelf ready that I can test. Exactly.

**Dave Jones:** So I just went and bought a reel of – what is it? Like 10-cent 3.3-volt voltage regulators.

**Mike Harrison:** Yeah, yeah.

**Dave Jones:** Because they're 10 cents. Like they're 10 cents.

**Mike Harrison:** Yeah, exactly. Like, you know, it's just nuts. So as I'm going to get a project where, you know, I actually care about that volume, I've got the thing. If it was just like one of my normal commotion jobs, I would just whack a microchip. I mean, an MTP 1700 in there. But, yeah, if it's something – I mean, because obviously I've been doing all the big stuff for a long time. This commercial – consumer thing that I'm looking at doing, it's the challenge of doing stuff super cheap. I've actually got a good mind to actually just design something with just stuff from LCSC, just like a little letter A badge or something as a little toy. Just let's use the cheapest bits I can, get it assembled, do the cheapest assembly service, just for the hell of it, and see how it comes out. Yeah.

**Dave Jones:** I'm tempted to do similar. It's just – yeah, I've ordered some parts as well that I intend to play around.

**Mike Harrison:** Yeah, I've heard some of the other days they do FSC cables for like five cents. Oh, do they? I mean, unfortunately, the range is a bit weird. But, you know, there's a pretty decent range. It's not particularly well catalogued. Right. But, you know, I've now got just like almost a half shoebox full of all the, you know, all the five and ten way, one mil and a half mil FSC cables they do. Because I do, you know, things like linking up led boards. I use FSC a lot. Yeah. I mean – And they cost you cents each. So you can afford to keep yourself out. You've been paying like, you know, a quid each from DigiKey.

**Speaker ?:** Yeah.

**Mike Harrison:** Because, I mean, the nice thing about FSCs is that, A, they're off the shelf. You don't have to get the cables made up. The connectors are nice and low profile and fairly cheap. But also, it's the only type of connection where the cable will go through a hole that doesn't need to be made bigger for the connector that's on the end of it.

**Dave Jones:** Exactly. So, yeah, you just need a tiny slot in the PCB. What, like a one millimeter wide slot?

**Mike Harrison:** The smallest slot you can make, basically. Yeah, the stuff's actually – but I've actually used those a lot in the past on various LED installations. And what was really annoying is that before I discovered – literally the day before I discovered this, I'd ordered about, I think, about 50 quids worth of FFCC cable from DigiKey for a project. It's really irritating. One of the things about LCSC is what I slightly do worry or wonder about is how many of these lines are lines they actually regularly keep in stock? And half of them are just literally the leftovers of the job they've ordered. Obviously, there's some stuff they've only got ones and twos in stock, which I'll ignore. But all the out of stock, is this something they ever intend to restock until they get another order for it? Obviously, there's some stuff that they've got like 100K. Oh, ask them, actually.

**Dave Jones:** I'll ask them because I've got a contact there now. They contact me. So I might ask them whether or not – like, do they want to be the Asian mouse or DigiKey?

**Mike Harrison:** Well, I mean, it's probably a mix of what would be good is if there's some indication on the product page to say this is a regularly stocked item or not.

**Dave Jones:** Or a one-off buy. Yeah, exactly. Yeah, which is for you.

**Mike Harrison:** One-off buys can be fine if you've got one project. But obviously, if you're designing something in, okay, they're usually cheap enough you can buy your whole production in one go before you commit the PCB. Yeah. But I think they're actually going to be at Electronica. I'm probably going to be going to Electronica this year. And I think they're going to be there as well. So depending on how good –

**Dave Jones:** That's the Germany one?

**Mike Harrison:** Yeah, that's just the huge indicator. It's like 10 halls of –

**Dave Jones:** And even if you have three full days there, you can't see everything.

**Mike Harrison:** Yeah, yeah. And you have to be selected. But it's fairly well grouped into halls. So you can just omit a complete hall and know that that's something special. I mean, the first time I went, they had a complete hall of Chinese suppliers. And it was the most annoying experience. Literally, you'd walk up and people would be coming up to you offering their business card. PCB, PCB, and all the stands looked like they did exactly the same stuff. And you sort of walk around the stand and you get this little girl with a little clipboard literally following you two paces behind, waiting to take your order. Oh, wow. You had to literally get the right walking pace so you could walk through and look at stuff just fast enough to avoid them coming out to you. It's just hilarious.

**Dave Jones:** It sounds like, yeah. So that's the in real life equivalent to PCB spam on my forum. Yeah, yeah, basically. Because they just keep spamming the forum. You know, like, oh, every single Asian PCB manufacturer, you know.

**Mike Harrison:** Actually, one thing I just found on, again, interesting looking things I found on LCSC. If you look up MUN12A, it's a little DC to DC converter module. And it looks like it's this little PCB with an inductor on the top in an SO8 format. Yeah. And I thought, well, that's interesting. I've got a few to look at. So I thought, well, okay, I'm sure. Well, where's the chip? Oh, it's probably on the inductor. I'm sold on the inductor. And they end up holding just a PCB, what looked like a PCB with three passives on it. Oh, I see it, yeah. The chip is embedded inside the PCB.

**Dave Jones:** Oh, it's inside the PCB.

**Mike Harrison:** Wow, they've actually done a... This is a 1M 12-volt point of low converter for like 20 cents.

**Dave Jones:** Oh, no way.

**Mike Harrison:** Yeah. If you look up, I think MUN12 will give you...

**Dave Jones:** Yeah, I've got it. In quantity, they're actually like under 15 cents.

**Mike Harrison:** And the higher power ones, I think, are probably the same chip with a bigger inductor on it. There's ones up to like 6 amps.

**Dave Jones:** Wow. Oh, what's the copper coming out on the edge of the board? That's in an internal heat sink, is it? Yeah. Yeah.

**Mike Harrison:** So it looks a bit like a PowerPad SO. Yeah. So it's like, yeah, I think you can mount it just like a PowerPad SO, but it's got the inductor built in.

**Dave Jones:** Oh, okay, right.

**Mike Harrison:** Wow. And so I'll have to actually... I bought about a 5-volt. When I've got time, I'll actually peel one down. I'll try x-raying it, and you can't really see much, but I think it will need to be peeled down to see it. But, yeah, it's quite an advanced manufacturing technique for a 20-cent chip from a brand you've never heard of.

**Dave Jones:** That's insane. So 95% efficiency. It's literally the size and not much bigger than the actual inductor itself. Yeah.

**Mike Harrison:** Yeah. And it's... With an SO8 footprint with just basically PCB pads.

**Dave Jones:** Wow. Oh, okay. So you can do... Oh, okay. So it's an SO8 footprint. Yeah. But it looks like it's got all four sides. It looks like a...

**Mike Harrison:** Yeah.

**Dave Jones:** A four-sided thing.

**Mike Harrison:** No, no. It is an SO8 footprint on the bottom. Oh, okay. Oh, right. Okay. I can't see the pads on the bottom. It might not be clear on the website.

**Dave Jones:** Oh, I see the pads on the bottom now. Yep. Okay. Yeah, it's got the power pad on the bottom with the... Yep. Wow. Wow. That is... Yeah. That is insane. It's just... It's cheaper to buy one of these and mount it in your project than it is to buy the individual parts and have them and lay them out on your board. Yeah.

**Mike Harrison:** Obviously, you still need a little bit of capacitors on in and out. Oh, yeah.

**Dave Jones:** So these don't have the caps built in?

**Mike Harrison:** No. No, it's not the caps. Yeah. For a one-amp converter, you know, you can need, like, maybe sort of 50 or 100 micro-carrads on the output like that. Yeah, right. So it's only 10 to micro-carrads. Yeah, for sure. If you can get them.

**Dave Jones:** Yeah, right. If you can get them. Have... Were you hit by the capacitor shortage?

**Mike Harrison:** I'm doing small enough quantities that DigiKey have usually gone in stock. The biggest pain has been I'll send, like, sometimes for the builds, I'll basically set it up with a subcontractor, get my customer to place the order on the subcontractor and send them a DigiKey basket. And I say, look, order this quickly because some of those parts will go out of stock. And, okay, there will be another item, but it's another part number you've got to look up. Got it. So, yeah, apparently it's the high-voltage, high-value ones that are just super, super unobtainium. But stuff like 100 nanofarad 603s, I've never had a problem finding, like, a realtor of those. Okay, they might be, like, 2p each rather than a penny each, but I don't really care about that. Oh, well, you know, no, it doesn't matter.

**Dave Jones:** Nice. Anyway, I'm getting one of those programmers and the in-circuit emulator for that little micro. So I might do a project just for the kicks of it.

**Mike Harrison:** Yeah, it's interesting to see what the whole emulator is. It was interesting to say that there was the English data sheet on it. That was one of the ones, probably the biggest surprise is, A, you can buy them in small quantities, and B, there's an English data sheet. That's it. I had a very quick look at the idea, and that looks, again, it looks in fairly reasonable English. So it'd be quite interesting to see what that's actually like. Yeah.

**Dave Jones:** Although I still am of the opinion, like others on the forum who've discussed this, that, yeah, no, look, you're better off paying $0.30 instead of $0.03 and using the pick with the platform. Well, I think there's maybe a midpoint.

**Mike Harrison:** Again, it all depends on your volume. Exactly.

**Dave Jones:** There is a point where it's worthwhile.

**Mike Harrison:** It probably doesn't matter if it's $0.10 rather than $0.03, but it might matter. There are cases where it might matter $0.10 versus $0.30. Yes, it might. If we're using lots of them. It might be that you've got, you know, some of the stuff that I do, for example, I've had like a board that's got like, you know, several hundred SOT 23 picks on one board for various reasons. Although things like the onboard, you know, self-programming flash tends to disappear at the $0.03 level, which makes it a bit of a risk. And also, the other thing, if you've got any contact, is ask them about getting pre-programmed chips. Oh, yes. Because a $0.03 micro is not a lot of use if you've got to program it yourself. Exactly. If you can pay like another cent and get them pre-programmed, then that'll be a super useful thing.

**Dave Jones:** Oh, that'd be phenomenal.

**Mike Harrison:** Yeah.

**Dave Jones:** That'd be absolutely phenomenal.

**Mike Harrison:** Programming OTPs, I've been told that the board is a slightly risky endeavor. Ah, yeah. You don't want to be doing that. One program, no probe slips and your board's trash, basically.

**Dave Jones:** No, no. You're screwed. Forget it. No, definitely pre-programmed. But the thing with this is that it changes your thinking about how you could potentially do designs. Because if you go, well, you know, oh, I'm used to using the one big micro and I'm going to use a big 100-pin micro and I'm going to drive all these things and the traces have to run right across my board. Yeah. But, you know, if you go, well, I can get a 3-cent micro or a 10-cent micro and I can put them point-to-load kind of thing. Yeah.

**Mike Harrison:** I put a huge butty just managing that many different bits of software can be getting...

**Dave Jones:** Oh, no, no. If they're identical, I wouldn't have like different ones. But if you've got one dedicated function is what I'm talking about. Yeah, yeah. If you can just offload a simple PWM to this 3-cent micro, right, for example, then...

**Mike Harrison:** Or a 10-cent micro, whichever.

**Dave Jones:** Or a 10-cent micro or a 30, you know. Then, you know, it changes your thinking.

**Mike Harrison:** Yeah, definitely.

**Dave Jones:** About how you can potentially design.

**Mike Harrison:** And obviously at high volumes, that's where it starts being interesting. It is, you know, I was quite surprised to see that. I must have a look at some of the other stuff, you know, the other slightly less low-end stuff as well. There's a Cortex-M0 that's about 30 cents. Yes. 30 or 40 cents.

**Dave Jones:** I saw that on there, yeah.

**Mike Harrison:** Which I can't remember if there's any English. I think someone figured it on Haggad. I think someone's actually done some work on it, translating and so on. But that looks quite interesting. They have.

**Dave Jones:** Somebody actually sent me. Somebody, you can buy a programming board which just plugs into USB or something. I don't know. But, yeah, somebody's done some work on that. And then, like, probably at that point, I would go, well, no, I'm going to use a 50-cent ARM chip instead of 30 cents or a 60-cent, you know. Like, it's not the order of magnitude decrease in price that, you know.

**Mike Harrison:** Well, I think the problem, certainly, again, I've not looked, I gather that some of the more popular lowest-end STMs are getting quite hard to get hold of now. Yep. Because everyone's using them, therefore, you know, everyone wants them. Right. So that's it.

**Dave Jones:** Hey, what's this tiny, ridiculously tiny seven-segment display that you posted? Tell us the – what is this?

**Mike Harrison:** It basically is designed for things like military head-up displays.

**Dave Jones:** Oh, that then get optically enlarged. Yeah. I love it.

**Mike Harrison:** There's quite a nice demo. It's like a pair of binoculars that had a built-in laser rangefinder, so you pointed at something. Oh, of course. Yeah, yeah, yeah. And it'll pop up a little display saying how far away that thing was. Got it. Yep. And they – I had quite an interesting chat with them. And obviously, the first thing I said, well, you know, why don't you use OLEDs? And the answer is that you can't do OLEDs over the military temperature range. Got it. Yeah. Whereas these are – they basically deposit standard LEDs onto a substrate. I don't think they integrate any of the drivers or anything. Obviously, most of the stuff is custom, and, you know, if you have to ask the price, you can't afford it. But they do actually do some standard parts, which just look like little silicon dust. I think I've linked to the data sheet one of them, which is the smallest one, which is a 0.8-millimeter high seven-segment display. Yep. The issue is you need a wire bonder to use it.

**Speaker ?:** Right.

**Mike Harrison:** It looks just like a little chip. So you just literally stick on your board and wire bond to it, and you've got – but that is actually a standard part that you can buy. So if you want to make your own little, you know, clock rants or head-up display type thing, I can't see any real use other than through optical manipulation. But it was just a really interesting thing. So I went to this – Yeah. Sorry. No, sorry. No. Continue. Yeah. I went to this electronic show today, and that was probably the most interesting thing I saw. Because you occasionally see, like, weird things. I was just going to say a bit about some of the electronic shows in the UK. Because obviously I've seen your electronics thing, which is obviously a pretty small affair. Yeah, it's not that. But, I mean, certainly, you know, like 10, 15 years ago, there was, like, a big show called NEPCON up in Birmingham. And that was, like, about half components and half manufacturing equipment. And that was when, like, they had, like, the Panasonic through-hole, like, insertion machines and all that sort of stuff going on, which is good to look at. Yeah. And that sort of gradually died out to being just production equipment and then disappeared. And then there was, like, one or two shows, like, came and went over the years. And then Southern Manufacturing started. And that started off as about 50-50 electronics and mechanics. So it was, like, metal bashing services, CNC machines, plastics, all that sort of stuff. And over those years, basically, the mechanical side has grown a lot. It's, like, the show is maybe three times as big as it was. And the electronic stuff has just started shrinking and shrinking. Because I think the problem is with these shows, you need to get critical mass. Otherwise, you can see, oh, there's not many people there. Therefore, I'm not going to go. Yep. And certainly last year, the electronic side, it was just really, really, really feeble. And it wouldn't surprise me if it disappears completely. And last year, I'm not sure how many years this – basically, it's called the Engineering Design Show. And it's got, like, subtitles, like, Electronics Design Show, Engineering Design Show, and Embedded Design Show. And that was almost the opposite mix. So the first time I went was last year. I think it might have been going a year before that, before I sort of noticed it. That's how I'd be up north in Coventry. And that was mostly electronics. Because the thing about Southern manufacturing is that you never got, like, the big test equipment manufacturers there. You might have got a distributor, a few odd random subcontractors, and so on. So it was never, like, as good as, like, the old NEPCON shows. Whereas the Engineering Design Show, so this year, they had Roden Schwartz, Yokogawa, Tektronix were there. All the big hitters, yeah. Yeah, Keysight weren't there. But it was mainly electronics. But the mechanical side, there was, like – there were about three stands selling springs. And, like, a couple of 3D printing and a few other things. But they – you know, it wouldn't surprise me if that side of the show disappears. Because it was so random and so – such a small part of the overall show. It just didn't really seem worthwhile. They had a few quite cool robots and so on. But so, no, there was quite a few. So I found out about these interesting LCD technologies and had a few interesting chats with various people. And did the various – usually grazing on all the various sort of free suites and sold they've got on the stands. Yeah, right. I didn't say the same technical display was just something that was just so – such a cool little thing.

**Dave Jones:** That is great. One place I think I remember seeing, not this small, but if you tear down, I think, one of the old film cameras, you know how they used to get – you know, when they had – you used to be able to put, like, the time and date on them. Yeah. Or the date, right? Then they would use – I don't know if they were led.

**Mike Harrison:** Which is something like the bubble display type things, but without the bubble, perhaps.

**Dave Jones:** Yeah, something – yeah. Something like – and they would have those embedded in there. And then, of course, they had to be really tiny because then they physically, optically overlaid that onto your film image, which then gets exposed on your film.

**Mike Harrison:** I wonder if they actually did it using just a single row of leads and used the fact the film was winding to actually give, like, a raster scan rather than have the whole array on it.

**Dave Jones:** From what I remember – this is a long time ago that I tore one down. This is before the blog. And, you know, I was just tearing random things down. Yeah, I know. I know. Just because. I hear you. Yeah, I've been doing it since I was, like, five. So, you know. Same here. Yep. And, yeah, from memory, it was – they did have, like, the multiple seven-segment displays in there. So, it wasn't scanned as it went through. It was – they actually projected the whole thing onto there.

**Mike Harrison:** Well, maybe then they didn't have enough processing power to actually do the scanning thing. Probably, yeah.

**Dave Jones:** Exactly. Yeah.

**Mike Harrison:** Yep.

**Dave Jones:** But, yeah, I find those remarkable, those cameras with all their flat flex technology and everything else. I find that how they fit to envelope design is just –

**Mike Harrison:** The one thing that I've never really got my head around is, like, things like cameras and also things like the old Walkman cassette recorders. Oh, yeah, phenomenal. How they design and prototype those things when they didn't have all the 3D CAD modeling stuff. Exactly. You know.

**Dave Jones:** I know. It's – you open any Sony product and it's like, oh, my God, how did they design this? Exactly.

**Mike Harrison:** Like, things like the camcorders, like the later camcorders. Yeah, yeah. Which is just ridiculous. Yeah.

**Dave Jones:** They're remarkable. They're just insane. I know. Like – and the service manuals for them were even more remarkable. Oh, yeah, yeah. Yeah, it works a lot. Oh, with all the 3D exploded. Yeah, yeah, yeah. It's all hand-drawn and everything, like, just remarkable. That was real engineering. I don't know what we're talking about. Oh, unbelievable. I was very impressed with that. Yeah. This world's tiniest LED flasher that you did, I thought that was pretty neat because that was – you know, everyone was puzzled. Like, where was the power source coming from? And I went, ah, it's a super cap, you know.

**Mike Harrison:** Yeah, I think I spotted those super caps on DigiKey maybe a year ago and thought, oh, you know, because I do – yeah. Either it's a case of DigiKey, okay, what can I find to make up the minimum order value for free shipping or just browse through new products. And these things appear, oh, yeah, I've got to get a couple of those. And it was maybe a year ago. Yeah, yeah, that sounds cool. And I thought they were coming from there. I thought it was literally the day before I was due to get out to make affairs. And I've got a collection of random, like, LED toys that I tend to have. Anyone that's ever met me has probably seen me with all these various LED toys. And some people are probably going to start getting a bit bored with them, but I haven't had time to do any new undressing. So I thought, well, let's make at least one new toy. So I just sort of dug these caps out. I was going to make two, but I lost one of the caps on the bench somewhere. Oh, no. And I just thought I found the – I dug around in my pile of LED to see which LED I've got that was the brightest with the lowest voltage. And I just – just a six-pin pick. Annoyingly, I didn't have any of the low-voltage version of that pick. So that one will run for about seven minutes. Yes, it could have gone better, yeah. It may well be the low-voltage one. I might run for a bit longer. But, yeah, that was a –

**Dave Jones:** The thing I found interesting about those caps is that they're in a ceramic package, like, you know, pick-and-place compatible, like, you know, like sort of robust ceramic thing. Yeah, just like a five-by-seven crystal.

**Mike Harrison:** Yeah, and there's a few things about the comments about, oh, using a crystal as a time-based and whatever. Yeah, no, no, no. I don't think anyone actually got the complete – yeah, some of them got the super cap. So I don't think anyone actually got the pick, certainly not until quite a bit later. Yeah.

**Dave Jones:** I posted a link to the – to a super cap, but I don't think I got the right super cap. I think it was, actually. I got a similar one. Yeah, yeah. Oh, was it? Okay. Maybe. Oh.

**Mike Harrison:** Yep. Actually, the hardest bit on that was actually figuring out how to do the charging. I ended up basically soldering, like, a very thin bit of metal onto the – so fortunately the flat face of the super cap is connected to the negative, so I just needed to create a side terminal. Basically, the charger is a 2032 plastic coin cell holder, like, with a square cutout of it and a pogo pin that presses the slider. I'm probably going to do another – when I get time, I'm going to make some with a low-voltage pick and do another video with a bit more detail on those. Yeah, yeah, definitely. But it got exactly the reaction that I wanted. So I'd say to someone, look, hold out your hand. I'll put it in their hand, and they'll just say, what the – you know, it's one of those – you know, you see something and you don't quite understand what's going on, you know, because it's so much smaller than the small battery that anyone's seen. It's really funny just seeing the reaction of people, to techie people. They've seen this thing and think, well, you know, what?

**Dave Jones:** What is the on-timer led? Because, like, you can't just have it, you know, like, is it like a really brief pulse?

**Mike Harrison:** It's two flashes of about a millisecond each, something like 10 minutes. I did a few bit experiments, and I found that a double flash looked a little bit more interesting, but also in terms of visibility, it seems to be better than a single short flash.

**Dave Jones:** Got it.

**Mike Harrison:** And it's like about six lines of code. It's just sleep, turn on, flash, sleep, turn on, whatever. The nice thing about that, Dick, it's got like a one millisecond granularity on its watchdog timer, so you can just use that.

**Dave Jones:** Oh, so you just recycled the watchdog.

**Mike Harrison:** Yeah, you just changed the watchdog timer sleep. Yep, got it. So it's doing almost nothing.

**Dave Jones:** Yep. Yeah, I thought that was sweet. Yeah. That was just great. But it's insane.

**Mike Harrison:** The fact is, I mean, you can show it to someone, take it, and they just don't quite understand what they're looking at. It was just really funny.

**Dave Jones:** Yeah, because people are so used to, well, it's got to have a lithium polymer battery, and I know they're X big, and it's got to have a board in their X big.

**Mike Harrison:** Or anybody, even the smallest coin cell. You can get some really tiny little alkaline coin cells, but it was just so much smaller than even that.

**Dave Jones:** Exactly. No, these are great. So the primary purpose for these surface mount super caps is like RTC backup and stuff like that, right?

**Mike Harrison:** Just short-term. Yeah, short-term, so they charge up in the system. 11 millifarads, I think. Yes, yes. So you'll run your RTC for a while. Yeah, the one I posted was 11 millifarad. It's not like long-term backup, but they're quite nice little suits. I knew I'd figure out something to do with them.

**Dave Jones:** Yeah, exactly. They're so cool. That's the kind of thing you want to throw on your digi-fuel.

**Mike Harrison:** I think the next one's going to have to have inductive charging because the contact charging is a real pain.

**Dave Jones:** Yeah, right. All right, let's – oh, show's almost up. Jeez. I've changed tunes recently.

**Mike Harrison:** Should we go through a few short news items before we go?

**Dave Jones:** We can go through a short news items. We'll do that last. Okay. One thing I wanted to talk about is you've heard that Fran Blanche has been forced out of her lab, right? And the news announcement. I'm moving my lab after seven years, finally. I move out. I get my new lab next Friday. So, yeah, I'll be starting to move things the week after.

**Mike Harrison:** That's going to be fun.

**Dave Jones:** Next. That's going to be fun. But it's like I was going to reorganize the lab anyway because if you've seen a photo of my lab, it's just like shit on – it's just bad. So, yeah, I – and because I own it, I kind of let it degenerate, you know, whereas, you know, maybe if I've got a rented lab, it'll be like, oh, somebody's coming around to inspect it. I've got to keep it clean, you know, kind of thing.

**Mike Harrison:** Are you selling the old one or are you subletting it to someone or –

**Dave Jones:** No, no, I would actually sub – I would – Rent it. Yeah, I have to find – I have to put a new carpet in and lease it out, you know. So, yeah. So, if anyone wants to lease my old lab –

**Mike Harrison:** So, you're combining all your spaces into one –

**Dave Jones:** Into one because I have two spaces at the moment and that was always a stopgap because I had my lab, which is 50 square metres, and it was, you know, I had my desk in there. I worked in there for like four, five, six, five years, you know, and it really – it was, you know, not much space at all. There was no windows. You know, it's a bit depressing, you know, working in a windowless cramped lab for five years. So, I thought, you know, look, I need a bigger space, but I don't want to move the lab and prices have just doubled in this business park in terms of like buying a space. Like, it would cost me, you know, like $800,000 plus to buy a hundred square metre space, you know. It's like, it's not going to happen. So, I thought, oh, look, I'll just rent a nice temporary – like for a couple of years, I'll rent a smaller space that I can move my logistics into and my editing. You know, my work desk and now I've got a window and everything.

**Mike Harrison:** It must have been a real pain having things and stuff in the wrong place.

**Dave Jones:** It's separate location. It kills the productivity because if I'm sitting here editing a video and I go, oh, I'd love to include just another shot. I've got to either walk or cycle or drive to my lab and then, you know, like it's just, yeah. Or if I go, oh, I want to get an idea, oh, I'd love to shoot just a 10-minute video for the second channel. I've got to pack up and go to the lab, you know, like, no, it's not, yeah. Anyway, so, yes, I'm moving into 100 square metres, double the size, which should be enough.

**Mike Harrison:** I think you should probably do some filtering in the move process.

**Dave Jones:** Oh, there will be filtering. There will be filtering. There will be extra benches. And what I've always wanted is like an island bench, like in the middle that I can walk all the way around.

**Mike Harrison:** Instead of taking everything to the second level and literally picking up everything and saying, do I want to keep this eBay and give it away? Exactly, that's what I'm going to do.

**Dave Jones:** That's what I'm going to do, yep. So there may be a lot of eBay.

**Mike Harrison:** Generally, you look at something, have I touched that within the last X years? If no, it's, you know. Probably the biggest problem is the stuff which is too big or too low value to eBay, but you just can't bear to throw away. Exactly. That's the really hard stuff. Obviously, there's a lot of stuff I pull out of teardown gear that is potentially useful to somebody, but it's just a pain in the ass to me. What I tend to do, there's one of the last sort of decent radio rally, ham fest type things in the UK. It's like a car boot sale type format. So last year, I took a transit van full of stuff up there.

**Dave Jones:** I might do that, yep.

**Mike Harrison:** I think I gave away about half of it. I'm quite happy to just give stuff away to someone that can use it.

**Dave Jones:** Yeah, exactly. Rather than see it go to the landfill, you know, at least go to someone else.

**Mike Harrison:** I just basically started off with stuff on the table priced and had things say, anything on this table that's not sold by 11 o'clock is going to be free. And there's a big, huge sheet on the ground. I just kept chucking stuff on this thing, everything on it. This is free. And I think I came back with like two small crates of stuff that I wasn't going to give away. So that was very effective. Yeah, of course. So I would highly recommend that as a tactic.

**Dave Jones:** Yep. I think I will be doing that at the next ham fest. Yeah. So, yeah, for sure. Like, as I've done that, I've done the car boot thing, you know, you like the tarp on the ground. And, yeah, you know, I had like all these scopes and I, you know, like, yep. And as time went on, yep, the price went down and down. I was like, I don't want to take these home. Yep. I remember, though, I came home with like five grand cash in my pocket. You know, I sold a lot of stuff. It was like, you know, it was great.

**Mike Harrison:** I think I just basically, once I'd covered the van rental, you know, I just sold it, you know.

**Dave Jones:** Yeah, yeah, you were happy. Yeah. Yeah, that's it.

**Mike Harrison:** Especially if someone seemed like really enthusiastic about it, like this step motor. And was so, yeah, thinking, well, you know, have I got a pound? I'll just take it, you know, just go and play with it, you know. Yeah, just take it. I don't really need the money. That's it. I need the space more.

**Dave Jones:** Yeah, I'm going to have to do that. So I do have a storage bunker, which I'm keeping, of course. That's where I keep a lot of stuff. But anyway, 100 square meter lab. Fran says she needs like two, she's always had like 2,000 square feet, which is about 190, you know, square meters, which is double my new lab.

**Mike Harrison:** Yeah, but she's got production as well, though, hasn't she?

**Dave Jones:** She's got production for her Frantone pedals and, you know, effects stuff. And she does, you know, and all sorts of stuff.

**Mike Harrison:** And the thing about production is that you're not in the space, but it needs to be fairly well organized as well.

**Dave Jones:** Yes, that's it. So what size is your space? Like you have a house, right? And your lab is in your house, I presume?

**Mike Harrison:** Yeah, I've got it. The reason I bought this house is adding a big double garage out the back. So I converted that into a garage just big enough to put the car in and the rest was workshops. I like the inner wall built in.

**Dave Jones:** Oh, you put your car in there as well?

**Mike Harrison:** Yeah, and I then actually extended a little bit out as well. But it's size-wise looking, it's probably maybe four by 10 meters, something like that. But, oh, yeah. Okay.

**Dave Jones:** So it's about the size of my lab, 40, 50 square meters. Yeah, obviously.

**Mike Harrison:** It's very well packed. But also, you know, I've got secondary storage space in the house. I'm a conservatory in an attic. Oh, okay. The whole back room is just full of shelving. Right, yep. And a lot of that is just like boxes from old projects. Like, say, once I've done a project, it's like the spare PCBs, the testings, whatever. Because there's a reasonable chance that I might. What quite often happens is that a new project will come along that's maybe similar. So I'll just use these boards as a demo to the customer. Of course, yeah. Or the experts and so on.

**Dave Jones:** And you've got to keep those. You can't throw them out.

**Mike Harrison:** Well, I mean, I could throw them out. Yeah, they're obviously absolutely zero use to anybody else and possibly of use to me. So it would be silly to throw those out. Because Soslaw said something would come along. Totally. But sometimes even just silly things like, you know, if I just prototype something, I just need a board that's got, say, a pick and an SD card socket on it. I've probably done something like that in the past. And I can just pull the board out and use that as a prototyping board. Just things like that. It's really useful to do. And so there's the other stuff is just general. Like, you know, just big crate of mains cables, big crate of power supplies, that sort of stuff. And there's various other things. But I do get quite ruthless. You know, stuff goes out of the workshop fairly quickly into intermediate storage. Yep. And, you know, I'm not a particular – I haven't really inherited my – I sort of inherited my father's – it might come in useful gene. But I've learned to, like, temper that with – you know, I just – you know, there comes a point where the bench gets so messy. You need an organized workshop. I've got to just clear everything out. It's well enough organized that, you know, there is a place for everything. Therefore, it's fairly easy to clean up. Got it. I actually did a video about workshop organization a while ago that was actually quite popular.

**Dave Jones:** Yeah, I saw that. But I don't think we saw your wider workshop, did we?

**Mike Harrison:** Well, there was the panorama that I think –

**Dave Jones:** Oh, okay, right, right.

**Mike Harrison:** Yeah. And, like, for example, the PCB tanks went out to make way for the pick-and-place machine. So I still have the PCB tanks in the conservatory, but they get very little use these days.

**Dave Jones:** I was going to say, do you bother making your own? You wouldn't, would you?

**Mike Harrison:** There is things like if I just suddenly need, like, a one-millimeter pitch breakout board for something or, you know, something just really quick.

**Dave Jones:** You can have it in an hour.

**Mike Harrison:** Yeah, exactly. Right? Yeah, yeah.

**Dave Jones:** That's right.

**Mike Harrison:** And just having them – you know, there's a big difference between having tanks set up ready to go than having to, like, pull everything out of the cupboard and dick about. That's actually quite a big difference in terms of usefulness. So the tanks are there. Literally, all these do is, you know, when I start doing the layout, I'll press the button to start it heating up. I'll do the layout. Ah, okay. I'll laser print it, expose it, and then it's done. But it's only, like, really simple stuff, like breakout boards are probably the thing I use it for more than anything else, actually. Yep.

**Dave Jones:** Otherwise, you can wait, you know, three, four days, two, three days or whatever.

**Mike Harrison:** I've got quite a good PCB company up the road with all – if he's not busy, I can get him good by 11, and he'll ship out the same day. Oh, nice. And if it's probably an hour's drive each way, if I want to go and pick him up. And that's, like, 200 quid for a panel. So it's really not that expensive. But that's fine.

**Dave Jones:** Yeah, exactly. No, that's – yeah, definitely. As in what size panel?

**Mike Harrison:** It's the cost of processing the panel. So it doesn't really – like I said, 12-inch square panel or whatever. Yeah, it's almost all just the processing time rather than the physical – Sure. Yeah, the material. Nice. But also, he'll, like – you know, he's quite good in, like – I can have throttable stuff, like, say, for a board that's got two different resist colors on it, and it's on a 0.8 with two-ounce copper. You know, it's one of the old-school shop. You know, he's been around there for, like, 30 years or so, and they'll just do it. Got it.

**Dave Jones:** Yep, I've known a few of those. None of his online ordering thing. They die in this shop, yeah.

**Mike Harrison:** The highest tech they get is that when you send them an order, he will just send an email back to acknowledge that he's received it. That is the limit of that. And that was only after I complained, look, I send you off an order, and yes, they do normally come, but it would be nice to actually know that you have received it. Right. And, like, you know, if it's going to be – like, you know, he'll tell you that, look, I couldn't get this out today, and he'll tell you rather than just not delivering, which obviously is really important if you've got an urgent job on that you can prepare and reschedule things. So, yeah.

**Dave Jones:** Nice. All right. So, shall we finish up with some news items? Yeah, can do.

**Mike Harrison:** What did you want to talk about? Well, there's the – let's go for the quick ones. Something I saw today which I thought was really cool, the world's shortest scheduled flight is potentially going electric. This is in one of the Scottish islands where it's the world's shortest scheduled flight, which is about slightly over one minute, including taxiing. Oh, what? It's like a one-mile hop between islands, and they're now talking – Oh, okay, right.

**Dave Jones:** That's about – that's probably – it's like a cheap pick-and-place machine. There's probably – like, there's very few niches where electric makes sense. If you look at the envelope of usability of the weight of the batteries versus the power you need versus the flight time and all that sort of stuff, there's a very narrow window where electric planes are useful.

**Mike Harrison:** And, of course, there's plenty of wind power, so they could actually have literally a completely environmentally neutral flight service.

**Dave Jones:** Ah, so it comes up, charges it up from the wind power.

**Mike Harrison:** I think they're almost talking about modifying the existing plane rather than doing a custom one. So it was quite an interesting – You got it. I see a nice way of entering into that. I think this in Norway, one of the Scandinavian countries I think is doing some work on it, because I think they've got lots of islands and so on. But it's quite interesting.

**Dave Jones:** Yeah, that'd be –

**Mike Harrison:** Start off on a really easy situation where actually you could actually do it without spending a fortune. Yeah. I mean, you could probably almost do that from stuff you can buy from Hobby King.

**Dave Jones:** Yeah, right. Yeah, probably.

**Mike Harrison:** Obviously, you've got the whole approvals issue. Yeah, yeah, the pesky approval thing. The other one, which I just found totally hilarious – this is on news a while ago – apparently, Apple – it cost Apple something of over $3 billion for warranty fraud when they opened their Apple stores in China. And they'll get people just buying the phone, stripping them for parts and returning them under warranty. Oh, no. Which I mean – And literally, there'd be guys with suitcases full of phones just returning them. And they're wondering why they're getting these 60% return rates. But purely the fact that Apple makes it so difficult for people to repair stuff, I just find it hilarious. I think, you know, good on the Chinese guys, frankly. That is great. If you can't buy the parts, shit will happen, you know.

**Dave Jones:** That's terrific. Anyway, people, don't get excited about you're going to be flying from Sydney to London on a battery power. Yeah, it's just not going to happen.

**Mike Harrison:** It was quite a nice little neat solution. Yeah, it's neat. Yeah, Boston Dynamics, again. Oh, the robots. The parkour and the dancing dogs. But the other thing is there's a UK guy that does some really nice, neat projects called James Bruton. He's got a YouTube channel. And he's actually doing what he's calling Open Dog, which is like an open source robotic dog, which is all 3D printed and machined and so on. And that is like going through all the inverse kinematics and everything. So that looks quite interesting. It's on like about part 11 now, but that's – it's not walking, but it's now standing and bending and tilting and turning. It looks pretty big and impressive, yeah. But, yeah, that's quite good. A couple of just very quick links. One thing which I found really handy, I think it's been discussed on the forum, the online Gerber viewer. Oh, yes. PCBXPRT.com, where literally you just grab, drag a zip of all your Gerber's onto it and it'll give you a preview. And it works actually quite nicely. It's just quite a handy little tool. Excellent.

**Dave Jones:** We'll link it in.

**Mike Harrison:** Yeah, well, the other thing, again, this is a featured hackaday we discussed a little bit before. Oh, yeah, before we came on. The JITX PCB service. I don't quite understand what it is, but it's –

**Dave Jones:** Oh, so they make PCBs, do they? And they're getting into the assembly business.

**Mike Harrison:** They do PCB layout and they say they've got these AI tools that they use. They say they'll design a – for $3,000 in 24 hours, they'll design your PCB as long as – I think they'll try to – a few other than 50 components, 20 unique components, less than 250 things, less than 3 amps, less than 500 megahertz, less than 20 watts total. Yeah, and they're using some – I can see so many problems around that, like how do you specify it? But the thing is – I know, it's ridiculous. Basically, they're pushing this as a prototyping service. And they've got this hilarious video. I'm not sure if it's on the website or – it's certainly linked from the Hackaday article about saying – I think they've got like this student intern that did this project as a case study. And it was this gate control. It's got NFC and web interface and all this sort of stuff. And they say, well, you know, you could prototype this using all these breakout boards and plug-in prototype boards. But, you know, they suffer from bad connections and stuff and whatever. And so let us design a PCB for your prototype. Completely missing that the entire point of a prototype is you can change it easily. Yeah. And then when you order your PCB from that, you can be writing the firmware while you're waiting for the PCB to get back. It just looks – I just don't – maybe I'm totally misunderstanding what they're trying to sell. I suspect they're targeting all the Silicon Valley startups wanting to turn around their prototype. Start-ups and stuff, yeah, yeah.

**Dave Jones:** And they're trying to extract three grand from each one and we'll prototype your board. But people don't realize how much to-ing and throw-in is involved in even doing a prototype board. You know, yeah, they may come back with a design and then in 24 hours and then you go, well, no, I want to, you know, make these changes. And then what do they do? Charge you another $3,000? Yeah, I know, I know.

**Mike Harrison:** I knew if they just come back and it just doesn't work and, yeah, it's – I can see a whole can of worms, frankly.

**Dave Jones:** It's just – yeah. And it's not cheap. It's not like it's $300. It's $3,000.

**Mike Harrison:** Yeah, yeah.

**Dave Jones:** You know, that's – you know, it's like – well, it's not unusual for that sort of cost to get a professional PCB designer to lay out your board.

**Mike Harrison:** Just to do that in 24 hours. All it takes is one query back to the customer and your 24 hours is gone.

**Dave Jones:** Yeah, no, they have blown. It's gone. Yeah, exactly. Single query. No, I'm – no, that's – there's some wankery going on here and artificial intelligence to do your routing.

**Mike Harrison:** Having said that, I mean, I think, you know, auto-routing is – you know, we all agree. It can work in some circumstance. But, I mean, if someone were to, for example, throw GPUs and some AI at an auto – yeah, start an AI. Just show it like thousands of good board layouts and throw some GPU resources at it. I think maybe something useful could come out of it. Maybe.

**Dave Jones:** But, you know, like it's still going to need – like it's 90% placement.

**Mike Harrison:** Yeah, absolutely. You know, PCB layout is 90% placement. I think there's going to be at least some interactive assistance with place. And, like, so you drag stuff around and it, like, colours, you know, colour according to connection density and so on. I think that, yeah, that's maybe potentially useful. But, yeah.

**Dave Jones:** Oh, it's just – oh, yeah, no. It's like – yeah, no, look, I was a former professional, full-time professional PCB designer. And I have used auto-routing, but in niche circumstances, you know. I go, look, oh, look, these are all digital. They're not – you know, length, you know, is not a problem. And, you know, you don't have to match anything. So, you look, I'll just let it go. It'll be good enough, you know. And it's like, yeah, some cases you – you know, there's niche uses. But it takes you – to do a proper auto-routing thing, it takes you just as long to set it up. Yeah, exactly, yeah.

**Mike Harrison:** As it does to – you know, because, for example, if you've got, like, quite a lot of variants of one board, so all the setup is shared, I think that will probably be a really useful – you know, good use case. Oh, possibly, yep, yep. But, yeah, it's limited.

**Dave Jones:** No, just your brand-new one-off whiz-bang widget. And, you know, if it's complicated and you want to go in there and auto-router properly, it takes you – you know, it can take you a week to set up the constraints just to get it right. You know, but if you're doing, like, a PC motherboard or something, then you would go to that effort.

**Mike Harrison:** Although you'd still – yeah, but also you'd probably manually route quite a lot of it to start with and then get into doing – Oh, yes, you would all the critical stuff. Yeah, yeah. All the wiggly stuff that's critical. You know, you wouldn't do all your wiggly length match stuff and all that sort of stuff.

**Dave Jones:** Well, you could use your interactive routers for that kind of stuff, you know, which is a different tool. Yeah, yeah. It's kind of like you're in control. You're telling it where it's going, but it's calculating how many wiggles it needs, you know, kind of thing to match the lengths and stuff like that. So they're incredibly useful time-saving tools. But, yeah, no, my spidey sense tells me this is just wankery.

**Mike Harrison:** Yeah, and, of course, I don't think you mentioned on the last time I've had the whole super micro implants nonsense story.

**Dave Jones:** Oh, yes.

**Mike Harrison:** To which I have one simple statement. Show me a photo.

**Dave Jones:** Photos or it didn't happen.

**Mike Harrison:** You know, it's just I think it's ridiculous. I hope super micro is Sue Bloomberg. That would be hilarious.

**Dave Jones:** Yeah. Well, there's maybe like a kernel of truth in it, but like it's maybe. Who knows? But, you know, it's like and then they showed a stock photo of a little RFI filter and everything. One was analyzing that of how it would work. And, you know, come on. It's just, you know, and like. But that's what engineers like to do. Like, you know, we could sit here and, you know, come up with, you know, 10 different plausible ways. You could potentially do this, you know.

**Mike Harrison:** If you were in play, it probably wouldn't be one of them. Yes, you could do it that way, but there are much easier ways and less detective ways of doing it. Yeah. Actually, one thing I should add on my list here. Cautionary tale of weird things that can go wrong unexpectedly. This is an installation we did a while ago. Tell us. Basically, it's a big installation in the States. So all the stuff was being manufactured in the UK, being shipped over to the US and being like a final assembly and install over there. And basically what this was, it was a large like meter diameter ring custom aluminum extrusion with two, sorry, four, what was it? Four, one and a half meter long lead strips that slot in from like two sides to basically give like a strip on the outside and a strip on the inside. Oh, okay. We actually split it. One and a half meter wall to a real pain to get made. So we split those in half. But so basically on site at the installers, they were getting a few failures of the first driver on the board was dying. Obviously, we didn't have to. I don't think my customer was actually on site there. So the first problem is the communication things. And they sent me a few photos of the setup. I thought, well, is it ESD damage? You've got this great big long strip with a wire hanging off the end. You know, it's quite plausible. If that's sitting on, say, a piece of foam and you pick up the wire, you're going to zap that chip.

**Dave Jones:** And because it's the first one in the chain or whatever.

**Mike Harrison:** I'd seen, I've actually done a video on the Heathrow Airport thing. We had a similar issue with potting in like metal molds and so on. So I assumed it was that. Yeah. They sent me a few strips back to look at and it said the input on the first chip had died. So I assumed it was probably SD. And then later on, I think they got someone in locally that did a report on some of it. And actually, the issue turned out to be far more subtle than that. So these things had a controller board to output. It basically took like 48 volts in and output four. They had four output sockets, which was like five volts and data for the LEDs. And the only socket that would fit in that space was a Molex micro fit, which is a three millimeter pitch, two by two plug in. So you plug it in, it clicks down and the connector is keyed. So you can't plug it in the wrong way around. Which, yeah, no one saw any problem with that. It worked fine, whatever. What actually turned out to happen was that firstly, they subbed out the manufacturer of these. Yeah, they got like a company to make up a plug with a tile and then got soldered onto the strips, which is, yeah, that's something you normally do. And what happened was that the connector housings they used, which weren't Molex, were much easier to plug into the connector the wrong way around. Because the keying was just a little bit smaller. So because the Molex one, if you tried to plug it in the wrong way around, the keying meant you, you know, it felt wrong. It felt very, very, you know, that it wasn't meant to go this way. Apart from the fact that obviously the latch is in the wrong place. And I think the combination of that with the fact that this was being done by people, you know, assembly workers that maybe have, A, maybe not have cared about it as much as we did. And maybe just weren't trained. But the fact that you've got this sort of multiple things, the fact it was being done remotely, the fact that the production connectors were very slightly different. And the fact that they were being assembled by people that may have not taken care to make sure it was plugged in the right way. It meant that, you know, we finally figured out that, you know, I actually took one and said I actually plugged it in the wrong way around. And there was one orientation that would actually kill the first driver. Because, you know, it's just one of those interesting, it's like the old air crash investigation sort of scenario. Yeah, yeah, yeah. Any one thing of those, you know, it had to be the combination of all those factors. And, you know, if we'd have thought about, you know, if we'd have seen that you could actually insert this connector the wrong way, I could have easily just put a protection resistor on that strip. Sure. To fix that. So, you know, it's like saying, you know, every job you learn something. Yeah.

**Dave Jones:** So does that mean you're going to put protection on every new product regardless of, right? Yeah, yeah, yeah. Right.

**Mike Harrison:** But it was just one of those things where, you know, no one person was particularly to blame. It was like, you know, I always tell my customers that, you know, we're doing a one-off thing. You must have a contingency plan for stuff because, you know, shit will happen because we haven't, we can't, you know, run through all this to find out all the problems. And I think that project was sufficiently big that they had the contingency, but it's just the knowing that you've got someone from the States, your product is failing in ways that you don't quite understand, you know, on the other side of the world. And you've got, obviously, your end client is jumping up and down because it's delaying things. And it was just quite an interesting, you know, sort of cautionary tale of just this combination of different things that all, you know, conspired to make this happen. Yeah, that's great. It wasn't until I actually got the production strip back in my hand. And I think there was a comment from some of the guy over there that got into a report on it all, going through the production issues and whatever, who just pointed out the fact that it was possible to plug this connector in, which had not occurred to me because the ones I had were, you know, it felt, it felt good. Exactly, it felt good. But also, I am used to plugging connectors in, whereas if you just go to a factory of assembly workers and say, plug this connector in, they're not necessarily going to know what it's meant to feel like. Yep.

**Dave Jones:** I'll try and shove it in the wrong way.

**Mike Harrison:** Yeah, yeah. So that was quite an interesting cautionary tale.

**Dave Jones:** Oh, that's great. Well, I hope this doesn't happen in China, where you're headed off to shortly.

**Mike Harrison:** The thing we're installing in China is basically the same sort of hardware that we did in Hong Kong, which was like the PCB snapped together to make like a big shape. So at least the firmware is proven, most of the hardware is proven. I'm sure there may be other issues that, you know, China-related issues, I think. So, yeah, that's going to be a bit of an interesting experience.

**Dave Jones:** And it's in the middle of nowhere, right? Yeah, well, it's not quite.

**Mike Harrison:** No, it's Chengdu, which is, it's about the last big city as you head west before you hit the mountains where all the banders live. Right. So it is a central-sized city. I think there are some electronics companies I've seen. I think on LCSC there's been one or two companies there, you know, some of the other Chengdu electronics. Right. So it's a moderately big city. It's not Shenzhen. It's like a tier, I think a tier three, whereas Shenzhen and Beijing are tier one. So it's not like, you know, sort of dirt road type of scenario. Yeah, yeah, of course. It's like a big shopping center. But, yeah, that's going to be an experience.

**Dave Jones:** I can just picture you, Archie, you know, transporting all your boards and critical boards and everything on the back of a push cart or something, you know, down a dirt road.

**Mike Harrison:** Yeah, I don't know.

**Dave Jones:** No, it's not going to be that bad.

**Mike Harrison:** All right.

**Dave Jones:** Awesome. Well, thanks for joining us again, Mike.

**Mike Harrison:** You're welcome.

**Dave Jones:** It's been great. Yeah.

**Mike Harrison:** Good fun. Again.

**Dave Jones:** We'll have to get Chris back on and do the usual thing again. Well, it's what? You're averaging once a year, maybe?

**Mike Harrison:** Something like that, yeah. I've not checked it. Something like that.

**Dave Jones:** Cool. Awesome. So where can people find you if they haven't heard you before?

**Mike Harrison:** Mike's Electric stuff. Google that. You'll find my website, which is some of it is shockingly out of date and old and outdated. YouTube mostly, Twitter. And I'll just give a quick plug for something. Something that might actually be a product. Sure. Which is one of these things. I make it for myself. I have no idea if it will be useful to other people. I've done one quick video on this. It's basically a box to add Ethernet decoding to a MixSignal scope. This started off when a couple of installations I did fairly recently. I tend to use like RS485, but this had enough bandwidth. The RS485 was going to be struggling. So I decided to start looking into Ethernet. I was using the Wisnet W.

**Dave Jones:** I think I saw your video. Did you do a video on that?

**Mike Harrison:** Yep. Yep. Yep. I saw part of that. I'm using the Wisnet chip, which is a nice solution. You don't have to learn like all the other people stack. Which is an easy solution. But I wanted to look at the timing of the incoming packets and how fast I was servicing to make sure I was putting the data out quick enough. With like 100 meg Ethernet, you can't just stick a scope on the line because it looks like noise because of the encoding. You can't even detect when it's going. When it's going. So I started playing around with an Ethernet FI, which gives you like a data is valid thing. Then sort of started. Exactly. I stuck a tiny little FPGA on it to basically take that data and parallelize it. So you then feed it into the parallel bus input with a single scope. So you get Ethernet decoding.

**Dave Jones:** And then you use the logic analyzer in your scope to view them?

**Mike Harrison:** What he's doing is basically taking that serial Ethernet data and paralyzing it. And that's all it does. So that obviously you can do that sort of stuff with Wireshark. But what you can't do is also you relate it to other events and see the relative timings. But also... Could you reformat...

**Dave Jones:** Sorry. Could you reformat the Ethernet packets into, say, SPI so that you can... It's not fast enough.

**Mike Harrison:** You're getting parallel data at 12.5 megahertz. Right. Your SPI will be eight times that. So, no. It's a short time. It's just not fast enough.

**Dave Jones:** So, right. I was just going to... But then you could use the SPI decoding to see text and stuff like that.

**Mike Harrison:** You can use just the cheap... Yeah, the cheap... You can just use the cheapo PC logic analyzer, although it uses up all the channels. But if you've got a 16-channel logic analyzer... But, yeah, my thinking was, okay, you could make... I didn't want to actually build off a Ethernet analyzer. But, you know, the scope does most of what you need. It's got the triggering. It's got the memory. It's got the user interface. So, for just a really simple little board, you know, I don't yet know how useful this is going to be. So, I've sort of done a board. I'll run off a panel, do another YouTube video and say, okay, I'll sell the first few a normal amount just to get people to use it to feedback to whether they think it's actually useful. But I was actually speaking to my contacts with Ronan Schwartz on the show today and he seemed to be... You know, it's quite interesting because, you know, if you actually want Ethernet decoding on a scope, you're talking about very, like, Ronan Schwartz RTOs and, like, you know, well

**Dave Jones:** into five-ticket scope price tags. Oh, yeah, no, you're talking about $20,000 scope.

**Mike Harrison:** So, if you can buy a little board for, like, you know, 50-git or whatever to add it to a mixing scope, there must be some people that might find that useful. One thing I thought was possibly, if you're trying to reverse engineer by looking at the timing of, like, packets coming out of something and the relative timing of, like, if you're trying to do glitching and that sort of thing, it might be interesting.

**Dave Jones:** I'm telling you, just call it the EtherHack and every hacker will buy one.

**Mike Harrison:** Yeah, I've already registered to EtherDecode.com. Right, okay. I didn't look at EtherHack, but maybe.

**Dave Jones:** EtherHack is better, I'm telling you. It'll be, you know, like HackRF and all the other, you know, hacky tools that will, like, become these industry standard tools for hackers everywhere, you know.

**Mike Harrison:** But obviously, you still need to have a lot of canaliser on mixing more scope. Right, well, you know. I think that you can get some moderately, the problem is all the super cheap logic analysers are only about 8-bit, so that's probably not much more useful than Wireshark because you don't get the relative timing. It's when you can do other channels that it gets interesting. But, yeah, I think there are some fairly cheap 16-channel logic analysers.

**Dave Jones:** Ah, yes, yeah, there would be.

**Mike Harrison:** They're just not nearly as cheap as the 8-channel ones. But they're still, like, $100 or something. So, still, you know, if you need to do that, it's certainly a lot cheaper than buying, like, a Roden Shorts RTO or something. Yeah, of course.

**Dave Jones:** Awesome. Well, we look out for that. That's going to be great.

**Mike Harrison:** I'll send you one when I've got a few done. Oh, fantastic. You can send in the mailbag. I've got the boards here. I'm just testing them. I think that board is... First, I thought I got the USB power socket the wrong way around. Then I realised that the one that I'd fixed with the board was, like, the actual connector. It was the inverted type, which has got, like, the wide bit at the top. So, obviously, the authority was wrong. So, fortunately, it was just literally I had made the prototype with the wrong connector rather than the PCB being wrong, which would have been really annoying. Oof. Yep. I think the rest of the time I've got enough of it running that I think it's usable. So, when I get back from China, I'll knock a few out and see if anyone's interested.

**Dave Jones:** Sounds great.

**Mike Harrison:** Okay. All right. Thanks, Mike. We'll have fun in China. I will. Hopefully, I'll get back in one piece and not end up in prison or something. Yeah. Something like that.

**Dave Jones:** All right. Okay. If you do, we'll start a GoFundMe to get you out.

**Mike Harrison:** Yeah.

**Dave Jones:** All right. Thanks, mate. Good to talk to you. Catch you next time. Bye. Bye. Bye.

**Dave Jones:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye.
