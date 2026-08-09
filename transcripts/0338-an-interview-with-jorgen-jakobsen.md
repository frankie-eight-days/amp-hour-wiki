---
episode: 338
title: An Interview with Jørgen Jakobsen
url: https://theamphour.com/338-an-interview-with-jorgen-jakobsen/
---

**Chris Gammell:** Hey guys, two quick announcements right before we get started here. First is, obviously, this was released Sunday night. We're going to be doing that for the foreseeable future, a little bit for our timing, but also for you so that you have something to listen to on your Monday morning commute. We're going to just try it out and see how it goes. You'll probably notice we've changed the release date in the past. The other thing is I've moved my trip to New Zealand and Australia. I'll now be going from March 30th until April 19th, and I'll be planning meetups both in New Zealand and in Australia. I'm going to link to my personal website in the show notes, but I'd love to do some meetups with people from around the globe, and definitely will do some meetups also with Dave once we figure that out. On to the show.

**Jørgen Jakobsen:** This is The Amp Hour Podcast. Recorded previously, but released March 5th, 2017. Episode 338. An interview with Juren Jakobsen.

**Chris Gammell:** Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Jørgen Jakobsen:** And I'm Juren Jakobsen from Mios Audio. That's where I work now. But I have a background doing IC design for hearing aids here in Denmark and some other startups I went through.

**Chris Gammell:** Awesome. Yeah. And you were very kind to write to me about when, I think a couple of shows ago, we were talking about just the always-on nature of hearing aids. And then you had heard that. You wrote in. You said, hey, I've been working on these. And we were kind of musing, me and Dave were musing on the implementation of DSP plus audio. And that seems like that's exactly what you've been doing. So welcome. I'm really glad to have you here.

**Jørgen Jakobsen:** Yeah. Thanks. Yeah. Right. I was walking around trying to fix up my two old cars and heard your show. And I've always enjoyed that. So it's very inspiring.

**Chris Gammell:** Were you shouting at the radio? That's what when we usually get emails, it's like people are like, well, I was yelling at my radio. You and Dave were saying something stupid. And then, you know, we came in.

**Jørgen Jakobsen:** Now, I think that the wondering you had around what was put into these hearing aids was pretty right and precise. And yeah, there's a lot of people in Denmark that have been working on that. Right.

**Chris Gammell:** And that was interesting to me, too. You said that there's a large IC industry, but also specifically on hearing aids. So, I mean, why Copenhagen? Why Denmark? I didn't really realize that.

**Jørgen Jakobsen:** Yeah. I think we have three major brands here in the Copenhagen area. That's GN, VDEX, and Oticon. And I think they are around 50% of the total market.

**Chris Gammell:** Wow. Okay.

**Jørgen Jakobsen:** So, that's a very huge concentration there.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** Yeah. And that has grown since the last 25 years where the digital, all digital hearing aids was implemented. Mm-hmm. And yeah, it turned out to be three successful big companies. And they are heavily set on the market today. And a lot of development goes into that.

**Chris Gammell:** Was it based around like a university, though? Or like a past company? Or like what? Was there... Because I know like a lot of... Well, Silicon Valley obviously spun out a lot of the Fairchild stuff. And it kind of like it was this nucleus of people that kind of went out and started their own companies. Was there a similar thing there? Or was it just serendipity?

**Jørgen Jakobsen:** Yeah. We have a university in Copenhagen where they have a strong emphasis in electronics. Mm-hmm. Also, some in the pioneering analog industry. So, and then there's another thing. We have also good skills in doing acoustics and loudspeaker design here in Denmark.

**Chris Gammell:** Ah, okay.

**Jørgen Jakobsen:** So, we have Bang & Olsen. We have their brand called Ice Power. But we also have some really high-end speaker manufacturing, ScanSpeak, just to mention some.

**Chris Gammell:** Yeah. No, that's great, though. And it is that. It's like you get this kind of like this core group of people that are around an industry. And then there's people that go take it even further. Sounds like it's definitely that. How did you get into it? I mean, what got you into the industry?

**Jørgen Jakobsen:** I don't know. I've always been like a hacker from day one. Walking around in the junkyard, picking up electronics, set it apart, see what's inside. Found a lot of magazine at that time. And have to look through all of these and see all the fancy pictures, all the electronics there. And say, oh, well, someday I'll know what's going on there. Maybe I can do it myself.

**Chris Gammell:** Yeah, that's great.

**Jørgen Jakobsen:** So after a trip around the country outside, I went back and started university. Took a short education, what would be a bachelor. And got a job at LM Ericsson because that was another hub that is pretty big in Denmark. LM Ericsson is a Swedish company. They had a big group in Denmark doing intelligent phone systems. So that was the digital exchange that could do caller ID, fancy stuff at that time. But there were computers behind that. And that was coded up in some special coding language that a lot of people in Copenhagen could do.

**Chris Gammell:** Interesting. Okay.

**Jørgen Jakobsen:** And at that time, I got a job as a field support engineer. So I was supposed to go out around the world and set up these new GSM base stations. So they considered they probably just upgrade from electricians to more engineering style people. So they hired in a bunch of young people to do that. So I started out and I had a small year with LM Ericsson, but it was too far from the electronics. So, and at that time I found my wife and started to settle down a family and decided to go back to school. And took a couple of years at DTU, the university there, and learned about doing integrated electronics.

**Chris Gammell:** And DTU is that university you mentioned where there's a lot of expertise. University in Copenhagen.

**Jørgen Jakobsen:** Yeah, cool. And at that time, I've got a final thesis where I helped some guy out at Nokia. Nokia had another big site in Copenhagen at that time. There was the time of smartphones. The 3310 was a big flagship at that time.

**Chris Gammell:** Is that the one that they're talking about bringing back too? Is that the news article about that? Yeah. That was crazy.

**Jørgen Jakobsen:** Actually, some of the colleagues from that time, they produced that. So they produced some of the IC that was inside that one. And there was like, yeah, we now around the 400 million oscillators that went into that one. Oh my God.

**Chris Gammell:** Wow. Yeah.

**Jørgen Jakobsen:** Pretty crazy.

**Chris Gammell:** Yeah. Wow.

**Jørgen Jakobsen:** Yeah. So, but at that time, some guy that I helped there during my final thesis, he actually had some money out of another sellout that was here in Denmark. So he started, found his own company called Silicide and was supposed to do Bluetooth wireless ICs.

**Chris Gammell:** I have to say, Silicide sounds like you're killing silicon. Like.

**Jørgen Jakobsen:** I think it's a process step within the manufacturing IC thing. So it was just a name at that time. So that was a startup at that time. And we were pioneering the first pages of the Bluetooth specification that came up.

**Chris Gammell:** Oh, like what kind of timeframe were we talking about here? Cause.

**Jørgen Jakobsen:** Oh, we are 15, 20 years back now.

**Chris Gammell:** Oh, really? Okay.

**Jørgen Jakobsen:** So, so when we ran around and talked about the Bluetooth to people, nobody knew what it was actually.

**Chris Gammell:** Right. Yeah. The standard was kind of like getting developed by the 802, 15, whatever it was like the.

**Jørgen Jakobsen:** Yeah.

**Chris Gammell:** Or 802.

**Jørgen Jakobsen:** And the spec was out there. We were only doing the first like 15 pages of it. And we had to tell people that that was the hardest part to do. Yeah. Because that was the radio frequency, frequency shifting thing. Uh-huh. Yeah. So, but we, we made our first chips and, but unfortunately we never succeeded. So, but it was three years of very exciting work. Yeah. Yeah. Doing chips on very low budget, doing, using tools from open source, whatever we could find to make it.

**Chris Gammell:** Right. To make it work. And, and so like, and, and, um, I don't want to say that's pre-Foundry cause it wasn't pre, I know there was a Foundry model then, but like, it doesn't seem like it was as big of a thing where it's like, you just go, um, you know, go to any, any Foundry like you can today. Well, I mean, there's a lot of costs today, but.

**Jørgen Jakobsen:** No, I think, uh, the, the, the model at that time was to find a, a fab that had some, a bit of an old process, uh, so that we could afford to, to do tape out in it. Yeah. Um, and, um, yeah, we were able to do that. Um, one thing we might have failed at that time was, uh, that we put a lot of effort in to do a PLL that was a bit ahead of a time. So radio worked fine. PLL didn't. So not a good radio in that way.

**Chris Gammell:** Gotcha. Yeah.

**Jørgen Jakobsen:** Yeah. Yeah.

**Chris Gammell:** Cause you were saying it does frequency hopping in Bluetooth, right? Like it does. And you need to have that kind of like dialed in PLL.

**Jørgen Jakobsen:** You need to have a very fast frequency shift system in doing that. Right. Yeah.

**Chris Gammell:** Yeah. Find the new frequency locked to that, find the new frequency locked to that, that kind of thing. Yeah.

**Jørgen Jakobsen:** Yeah. And that was one of the hot, uh, thing to do at that time and where a lot of people made the effort into that. Uh, but also what happened at that time was that the, so we were only doing the radio frequency thing there and, uh, other companies would then do the, the baseband implementation. And then there's a huge amount of software to put on top of that.

**Chris Gammell:** Right. Right. So it's like a multi-chip solution. Whereas we think of it today where it's like everything is like, you look at like a expressive chip, it's way different than, uh, uh, you know, like then when you were just doing like the front end and, uh, and then you said the baseband processing was separate. Yeah.

**Jørgen Jakobsen:** We, we had to be, we had to partner up with some other company that actually were able to, to do that either in a FPGA or some digital implementation of that. Right. And there were a lot of companies around doing that. LME Ericsson was one of them. We have RTX at Jotland. That's another part of Denmark, a company that was huge in that area. And then there were the big guys today also doing a thing, and people were just posting a lot of millions into that company. We were just like shaking our heads. Yeah, right. But they won. Yeah, right. But not.

**Chris Gammell:** Yep. Sometimes the money does matter a little bit in those things, huh?

**Jørgen Jakobsen:** I think that's a model that is worth following.

**Chris Gammell:** Yeah. I remember the first time I saw Bluetooth stuff, I was working on like these, I was at my co-op, and I was working on radios, and it was like 2004. And I remember the early Bluetooth was just so rough. I mean, it was, you know, it wasn't low power. Like thinking about it today, like how ubiquitous it is, it's definitely what the dream of what the architects of the standard probably thought would happen eventually. But it took 20 plus years, right? I mean, it was not short.

**Jørgen Jakobsen:** Yeah, and it's still under heavily development. So you still see new branches of Bluetooth specification diversity coming out. Actually, this was a big push from the hearing aid industry trying to put some low power audio profiles into there. Yeah. And that's also succeeded now. I think a lot of other like industry will leverage from that.

**Chris Gammell:** That's great. Yeah. That is, I mean, that is, yeah, that is the best case scenario when it is, it hits that critical mass. And enough people are doing it that it's like, well, we can, you almost build on the brand of Bluetooth as much as, you know, like, oh, it's got Bluetooth in the device, but we need to stream files or audio or whatever else where it wasn't really built for that. So that's interesting. So, I mean, what was it like? So that was a startup you were doing.

**Jørgen Jakobsen:** Yeah, so that was a startup small company like max 15 people when things did not go any further. Some financial plan did not go the correct way. We have no products in the market.

**Chris Gammell:** So that's a fun new job. We've had an analog startup on the show before who, unfortunately, also they did not make it out. But, like, it seems like it's, it seems like the, in a resource heavy thing like silicon design, that would be very difficult of, like, getting access to the fab engineers, getting access to the process stuff. I mean, what, what, what, what, what were those challenges, especially since you were kind of getting, getting your footing as a new engineer as well?

**Jørgen Jakobsen:** Yeah, I think the, the challenging was to, it's another concept. You, you, when you have access to analog design, you can put all the transistors you want in there. Okay. So you do that. Yeah. Because the components you have, they are totally rubbish and the spread of them are terrible.

**Chris Gammell:** Oh, really?

**Jørgen Jakobsen:** So you need to put a lot of transistors in there, do a lot of trimming, do a lot of management on top of that. So that's another digital IOs into that.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** And.

**Chris Gammell:** Could you explain the trimming process for people that don't know what that is?

**Jørgen Jakobsen:** Yeah. So, so, so for instance, you put in a resistor, you have, that transistor was spread 20%, but you need a precision around 1%. So you just chop that resistor up in the smaller chunks. And at the production time, you just measure up some, some referred value and trim and fuse. So that's a simple way to do that.

**Jørgen Jakobsen:** Yeah. Okay.

**Jørgen Jakobsen:** There are other techniques where you would like to do automatic trimming so that you don't have to spend time on it on the, on the wafer tester or boot up process, something like that. So you could do trimming on the, on the silicon itself. Things like that. Yeah. Right. That's a lot of possibilities.

**Chris Gammell:** Right. Yeah. Because I think about it, like I, I just go out and I just, I go to Digikey or wherever I'm shopping for parts and I just buy a 0.1% resistor. You are literally putting these structures for resistor into silicon. And then, like you said, there's not enough process control to, to hit the mark each and every time. So that, that is, that is definitely a challenge. Yeah.

**Jørgen Jakobsen:** And you'll still have your, your resistor will spread 20%. Your caps will spread another 20%. Right.

**Chris Gammell:** Your error budget goes, goes out the window pretty fast. Yeah. Yeah. That's crazy. And so, and so same thing with, so you're making inductors as well, all these things in silicon. I mean.

**Jørgen Jakobsen:** Yeah. That's what you do today. If you look at dive photos, for instance, I would recommend to have a look at the expressive ESP32.

**Chris Gammell:** Uh-huh. We actually posted some on our subreddit a couple, I think. Yeah.

**Jørgen Jakobsen:** It's, it recently get out. And what, what you can see there is like 10% of that I see is just analog. Yeah. Crazy structures. And that's inductors. The caps, you can see that, but you also have a lot of caps there. And then the rest is just covered with the, like power supply grids. And that's the digital stuff.

**Jørgen Jakobsen:** Right. The analog stuff is a small part in the corner and the digital is, is big. Right. At least in products like that.

**Chris Gammell:** Right. Exactly. Exactly. And yeah, I was always surprised when I was learning about process stuff at Samsung, I was always the, it's the scale difference stuff that really makes the difference. Right. You can control for small scale and you control for big scale, but it's when it's on the same. Yeah. Piece of, of silicon that was like the processing times, you know, it's like, it's like cooking, it's like cooking spaghetti. Right. Yeah. Yeah. In a small pot of water versus boiling it in a swimming pool. Yeah.

**Jørgen Jakobsen:** But I think one, another important thing here is that the digital structure scales different from the analog structure. Yeah. So you will typically get away with doing analog stuff in the older process compared to your digital stuff.

**Chris Gammell:** Right.

**Jørgen Jakobsen:** So your digital stuff is constantly pushed by putting more memory, higher speeds.

**Jørgen Jakobsen:** Tighter density, stuff like that.

**Jørgen Jakobsen:** Yeah.

**Chris Gammell:** Yep. Yep.

**Chris Gammell:** Yep. Yep.

**Chris Gammell:** So when you're doing these large analog components in silicon, is it mostly utilizing just bulk, like polysilicon and stuff like that and oxides? Or are you also doing doping for capacitors and crazy stuff like that?

**Jørgen Jakobsen:** Typically, it depends on the process. But you can have specialized analog processes where you have high resistance capabilities. So you can do megaohms for low-powering things. Or you could have small transistors for finer grades, things like that. For your caps, you typically... Again, here, it's a matter of putting two metal plates very close to each other. Yeah, right, right. And do it reliable and do it without too much spread in the process. And that's a pretty hard part. But that's kind of the analog options you get in a good analog process. Right, right. But also here, typically what we do right now is doing high-voltage stuff. So we can maybe withstand like 40 volts or something like that in some part of the design. But other part of the design is only 1.5 breakdown. So that's a huge challenge to do that kind of design. But back in the day, it was only low-power stuff. And yeah, that's, in my mind right now, very easy to do.

**Chris Gammell:** Right, yeah. Now that you've been through it, you know... I mean, I'm sure that there are like tips and tricks that you learn over time where you've seen what works. And that is probably a hard-won experience, right? I mean, like you have silicon that you're on the bench testing that didn't go well or did go well or whatever.

**Jørgen Jakobsen:** Yeah. And typically also you will get your experience from when you actually start to measure on the thing. And you have your possibility to trim things. And of course you did a lot of work up front where you actually got a very good idea about how your trim range should be with just normal simulation.

**Chris Gammell:** Yeah, what is the role of simulation? I mean, I know that the best simulators are usually the ones that are in these advanced CAD programs or these, you know, the IC layout programs. But what is the scale of like time spent simulating, time spent designing at silicon to time spent testing on the bench?

**Jørgen Jakobsen:** Yeah, I think up front when we do design, you do maybe like 30% of your time in doing simulation, schematic drawing. Doing layout also. It differs a bit if you do the layout yourself or you have contractors to do that. But I tend to say that the best quality you get is when you have designers doing the layout themselves.

**Chris Gammell:** Right.

**Jørgen Jakobsen:** So that they actually can do this pro and cons. Oh my God, this cap I put in here is way too big. I maybe could make a bigger resistor in that way.

**Chris Gammell:** Right, so there's not like that churn of back and forth, back and forth.

**Jørgen Jakobsen:** Yeah, so you do that kind of regression in your head or during a couple of design cycles.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** And hopefully end up in a block that could be put in the spot where you're supposed to be in the bigger floor plan. Hook it up to the digital part. And that's one of the things that gets harder and harder to do. We are analog driven design house here and I was in the previous setup also. So we need a digital call with all these digital control signals to the analog part. We still have this diversion between analog and digital.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** So for what we are doing now, the analog part is still bigger than the digital part.

**Chris Gammell:** That's where all the optimizations and the magic comes from, you're saying?

**Jørgen Jakobsen:** Yeah, but the digital part, the screen's in size and you can actually put a lot of gates and a lot of control logic into a very small area. Yeah. The only problem it has is you maybe end up with 200, 300 digital wires. You have to put level converters on all of them because your digital call runs on a different voltage. So a lot of things here go into like management of all your digital wires.

**Chris Gammell:** And when you say wires, you don't mean bond wires. You mean traces on...

**Jørgen Jakobsen:** Connections between analog and digital domain.

**Chris Gammell:** So that's in silicon. Okay. And so you'll gate it with some kind of level shifter like you said or something.

**Jørgen Jakobsen:** If you line up a lot of the level shifters, you do a database where you control it. You place the IOs on your digital call. You make automatic layout of things like that. So a lot of inter-steps is needed there to actually do a complex chip like that.

**Chris Gammell:** Yeah. And so like in the process side of things too, because I mean, when I hear you talking about the high voltage, low voltage stuff, I assume that's like moving towards like a BCD type process or something. Yeah. Exactly. But is it actually masked off when they're processing one level versus another? So like I'm kind of thinking through, like I said, I did process just for digital, for memory stuff. But there were those kind of big, large scale differences, you know, multiple steps. So... Yeah.

**Jørgen Jakobsen:** I think it's basically the same structure you're working on. And it's just a matter of your wells and your buried isolations and the structures that you put in there. And then it's just a matter of how close you do to each other, how good you are to do substrate pickups and weld ties and things like that. Yeah. So that you control the different area of the chip. And from what I've seen now, what we did on this first generation of chips, then you can get away with real, a lot of things there. Yeah. Because we have real high current running around in the chip, but we have real sensitive circuits also.

**Chris Gammell:** Uh-huh.

**Jørgen Jakobsen:** And it works. Good.

**Chris Gammell:** Yeah. Excellent. Yeah. Excellent. Yeah. Yeah. Yeah. That's crazy. I mean, so give us a... Just to hop back to the psilocyte stuff real quick. So that was mixed mode as well, analog digital stuff, right?

**Jørgen Jakobsen:** Yeah. That was mainly analog. We did not have access to digital tool. Oh, okay. Digital tools are always very expensive. And we did definitely not have money for that at that time.

**Chris Gammell:** Oh, okay. So you wouldn't even like make your own like foot plops and stuff like that, like manually?

**Jørgen Jakobsen:** Yeah. On the other hand, we did that because we thought... Ah, we could do that. If we look at what people did before, CF gates, that kind of technology. Yeah. Yeah. Okay. Then we have a synth tool and we could get a cheap one from Aldic at that time. They had some tool that they sold into the market, but it was not taking off. So we got a good deal on that.

**Chris Gammell:** Oh, that's good.

**Jørgen Jakobsen:** So actually, I did that and I wrote a standard cell library of CF gates things. Oh, cool. And we were actually able to synthesize things and place a route, small things. So we had a serial bus. We could configure different parts of the ICs. Right.

**Chris Gammell:** So you're just saying that you weren't buying the digital tool that would allow like a core to be dropped in there and then synthesize and all that stuff, right?

**Jørgen Jakobsen:** We did some local digital blocks within the analog stuff so that we have all the configuration bits out there, but we have a serial bus to set it up.

**Chris Gammell:** That's nice. Yeah. No, that's great. That's great. So what I was getting towards though is like, so like, could you give us a scale difference of like an analog transistor versus like in that case, even, you know, CF gates type of thing where you're making smaller digital transistors? What is the scale difference on the gate sizes?

**Jørgen Jakobsen:** So, so at that time at the city side, we did 35. So that's 0.35 nanometer. So 35 micron. Yeah. Yeah. And today what we have is 0.18. Oh, 180 nanometer.

**Chris Gammell:** Yeah. Yeah. Right.

**Jørgen Jakobsen:** Yeah. So we in that ball game and that's not state of the art, but that's more than enough to do a lot of digital stuff. Right. It's more of enough to do good analog circuits. Right. So that's a sweet spot. And the good thing about it is that the process is cheap compared to the. Right.

**Chris Gammell:** Seven nanometer that the Intel loves talking about. It's like, yeah, we don't need that guys. Right.

**Jørgen Jakobsen:** The problem is that the tape out you have there is so extremely expensive.

**Chris Gammell:** Yeah. Yeah.

**Jørgen Jakobsen:** Yeah.

**Chris Gammell:** $10 million masks and stuff like that. Yeah. Yeah.

**Jørgen Jakobsen:** And the tool cost you have at that point is also crazy in the run times you have for doing LVS DSC. So that's the schematic versus layout and check for your mask set. That is, it has a long run time and is also expensive.

**Chris Gammell:** Yeah. Wow. That is, that is a whole other world. That is crazy. Yeah.

**Jørgen Jakobsen:** Yeah, it is. So, so we are still in, in this area where the vendors, they know that we, there's a lot of startup that can do analog stuff. They require a bit of digital and there's some option for us and that's what we do.

**Chris Gammell:** That's good. So, okay. So after your cellicide, then you, so you did that for a couple of years and then. Yeah.

**Jørgen Jakobsen:** I've run into this other company called Oticon and that was just to join the forces of, of engineering in these companies. There's a lot of them. Um, I think at Oticon at that time, there was a core group of around 10 analog IC designers. That's a lot.

**Chris Gammell:** Wow. Yeah.

**Jørgen Jakobsen:** And, uh, we were supposed to do, uh, wireless technology at that time. So that is also collided with the, the fall of, uh, of Nokia. So there was a bunch of people doing it. Yeah. So, so actually there was a lot of know-how in, in doing wireless technology and these people were taking into the hearing aid companies. Interesting. And introducing wireless technologies for the hearing aids. So at that time, we, uh, the first, uh, envision that you, for instance, could have audio streamed from some external thing into your hearing aid using, uh, digital technology to, uh, until today you only were doing telecoil. So analog magnetic, magnetic, uh, connections into your hearing aids.

**Chris Gammell:** Yeah. Wow.

**Jørgen Jakobsen:** But that's, uh, at that time, that was a complete new, uh, role to go into. It's a, it was a big organization. So we had to sneak in and use the digital tool by night if we wanted to do something like that.

**Chris Gammell:** Yeah. Yeah.

**Jørgen Jakobsen:** There was like a silo organization and, uh, we were only supposed to do analog stuff, but, you know, to test the, the things we done, we probably needed some FPGA stuff, but,

**Jørgen Jakobsen:** uh, yeah.

**Jørgen Jakobsen:** So, so that was something we had to do by night to, to do.

**Chris Gammell:** So you, so you were, you were working on integrating an RF component to there. So that, and that, and like you said, that was to get connection to other devices, stuff like that. Could you just kind of walk us through some of the blocks that exist in a modern day hearing aid as well?

**Jørgen Jakobsen:** Just kind of, yeah. So what do you have today is typically one or two microphones, typically two microphones there on each hearing aid. So these will do a noise cancellation. They will do a directional. So you can actually beam form your, your vision or your audio vision that way. Uh, and then that comes into, uh, yeah. Uh, uh, A to D converter, take it into the digital domain, do a lot of, uh, filtering there. And the, in the digital domain, the main focus there is of course to do EQ. So people have lost their ability in some of the audio bands and you could adjust that.

**Chris Gammell:** Uh-huh. Right. Right. Because usually the high frequency stuff goes first, right? If I remember.

**Jørgen Jakobsen:** Yeah. So that would be what you will crank up or you could even do some compression or you could move some of the frequency information.

**Chris Gammell:** Oh, that's great.

**Jørgen Jakobsen:** So you could compress the frequency band down to a lower bandwidth and you will, and that helps a lot on, on, on, on recognition of, of your speech. Yeah. And Oticon at that time was, was, has a good reputation because there was, uh, some, some R and D going on in, in that concept on how you understand the speech. Right.

**Chris Gammell:** Intelligibility, all that kind of stuff. Right.

**Jørgen Jakobsen:** Yeah. So a lot of that came into the audiology way of, uh, making up the programs in the DSP.

**Chris Gammell:** Hmm. That is. Uh, so, and so what, and what kind of, I have to ask this one, what kind of, uh, power budget do you have here? I mean, we were talking a little bit about that, but what is, what is the norm? There's like a benchmark.

**Jørgen Jakobsen:** So you're, yeah. So you're around, uh, uh, sub one milliamp for hearing aid. Wow. And that you need to have your, uh, two microphones going on. DSP processing real time and your, uh, and your speaker. Wow. Your speaker at the previous version, actually a speaker in the physical device yourself. And then you have a tube into your ear. Right. Transferring that in there. But, uh, reasonably, maybe that's 10 years ago. Now they remove that speaker and put it into your ear channel. Uh, so you just connect by wires. That helped a lot. So now you have actually displaced the distance between microphone and your speaker. And that helps a lot on, on the feedback you have, because there's a lot of, uh, amplification going on in the hearing aid. Yeah. So, so, so one of the main purpose when you're starting to, to lose your ability to hear is to crank it up.

**Chris Gammell:** Right. Right. And that's what happens. And that's like the, the, the meme, not the meme, but like the, you always see people in like movies, they turn it up too much and then you hear the feedback and they turn it back down. Like, yeah.

**Jørgen Jakobsen:** And there's, there's, there's, there's some clever algorithm within the hearing aids. Uh, is somebody whistling or is it feedback? Oh. So some audit detection that can adapt to that and, and crank down that feedback path if needed.

**Chris Gammell:** Wow. That is, yeah, that's some dynamic stuff then, huh?

**Jørgen Jakobsen:** Yeah. So, but I think that's, uh, not much to be done there at that time when, when I entered the, the area. So more of it were like, how do the, the people control the device? Could we put, uh, rechargeable batteries in there?

**Chris Gammell:** Right. Yeah.

**Jørgen Jakobsen:** Uh, so when you start to use rechargeable battery, the density of, of that material went down a lot. So it was a fight to have a system that actually could survive one day of, uh, of continuous working without having to charge it by the end of the day. Right. Almost like your smartphone.

**Chris Gammell:** Right. Right. Exactly. And so, uh, so, okay. So you were probably also then integrating DC to DC type, uh, conversion stuff and high efficiency switchers.

**Jørgen Jakobsen:** That's what I know has been done right now. Yeah.

**Chris Gammell:** So, so all of these things you mentioned, microphone, well, I guess, uh, amplifiers, beam forming, ADCs, DSP, all the compression, blah, blah, blah, output, uh, drivers for the speaker is, and DC to DC all on the same silicon. Are we talking like single chip solution at this point?

**Jørgen Jakobsen:** Typically you have, uh, three dies stacked on top of each other. So you have your DSP, you have your analog stuff and you have your, uh, memory thing, everything bolted down to a small flex print. Yeah. And that's where you then mount all your, uh, microphones, things like that. Wow. So it was a very, very small system like that. Yeah. Complex and very expensive to develop.

**Chris Gammell:** Yeah, of course. And, and, and, and so if, if, if someone looks at a modern day, the plastic piece that goes behind the ear, is that mostly batteries in there these days then? Is it?

**Jørgen Jakobsen:** It's a battery mostly. Yeah.

**Chris Gammell:** Okay.

**Jørgen Jakobsen:** Uh, it helped a lot when you remove the, um, what's good, the speaker out of the device, then you were able to make it very small. Right. So you, a bunch of chips on top of each other doesn't fill, uh, consume very much area. The microphone is getting maybe the biggest parts in there. Uh, and of course the battery.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** That's crazy. But you also have the telecoil. So, you know, you don't want to lose your backwards compatibility and your backwards compatibility was that when you picked up your, uh, phone, old phone, there's a speaker in there. That signal was picked up by the telecoil. Really? Okay. Yeah. Very low practical things. Or even when you watch TV, you had a big loop with the wire around and that was actually, again, your telecoil, uh, producing the sound from your TV for you. Hmm. And you should imagine that the people wearing these hearing aids are elder people. Right. Watching a lot of TV.

**Chris Gammell:** So that's, uh, it's a, it's a big requirement, right? Yeah.

**Jørgen Jakobsen:** But I think also at that time it was known that, uh, the, the, the people using the hearing aids would be, uh, would like to be cooler or smarter. And that was, uh, why people invented the iPhone white, uh, and, uh, connectivity by iPhone to the hearing aids. Yeah. And that's been a driver. Yeah. The last five, uh, six, seven years now. Hmm.

**Chris Gammell:** So the telecoil though is it's, how long is that? That's been around for tens of years. I mean, like how, is that one of the oldest things?

**Jørgen Jakobsen:** That's very old. Okay. Um, so, and, um, but that was a chunky component and hard to take out of the device. Uh-huh. And the first, uh, generation of wireless technology that, uh, at least Oticon put into the hearing aids was done by magnetic links.

**Jørgen Jakobsen:** Uh-huh.

**Jørgen Jakobsen:** So low frequency, short range thing. So there would be a wireless connection from one ear to the other one. So, uh, one ear would say, is somebody, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, whispering or is, do I hear something or, uh, did the user press the bottom to turn up the volume?

**Chris Gammell:** Right.

**Jørgen Jakobsen:** Then the other hearing it would do that as well. Things like that. So management, uh, from one side to the other. Huh.

**Chris Gammell:** That is nuts.

**Jørgen Jakobsen:** Uh, and then at that time we introduced, uh, audio streaming so that you connect your Bluetooth telephone, uh, to an audio streaming device that then would transfer the speech up to your ears. Uh-huh. So pretty much, uh, James Bond style. Yeah. Right.

**Jørgen Jakobsen:** Right.

**Jørgen Jakobsen:** Pretty cool. Yeah. Very expensive. And, uh, the audience for that very old.

**Chris Gammell:** Right. Well, except for the spies, of course. I'm sure that there's spy people that are repurposing these chips. Yeah. Probably. Probably. That's great. And the other crazy thing too is like the environmental pieces, right? I mean, like, not that like, not that you have the elderly that are mostly using this that are like sweating and stuff like that, but just being on the body, having a water, waterproof, sweat proof, all that stuff is crazy.

**Jørgen Jakobsen:** Yeah. It's a very harsh, uh, environment to be in. Right.

**Chris Gammell:** Yeah. But these things also cost about $2,000 a piece, right? I, I, I have, I have seen them at Costco. The low cost ones were like $1,500, I think.

**Jørgen Jakobsen:** Yeah. They are expensive. Yeah. But it's a, it's a relative, uh, uh, uh, protected area. No, no other company comes in there. It's, there's a lot of, uh,

**Chris Gammell:** Well, that's not that surprising given what you just talked about. It's like, well, if you want to come and innovate here, be our guest, right?

**Jørgen Jakobsen:** There's a, there's a large bunch of, uh, patents, uh, that is, uh, shopped around in a pool that the, the big players are in. So there's, I guess, like, uh, six major players around the world. Uh-huh. And I think that's going to be like that for a long time. And there was some, uh, like discussion on some of the companies buying each other and, uh, that was actually rejected due to, like. Oh, competition. Like, um. Yeah, competition.

**Chris Gammell:** Yeah, that makes sense. What about, I mean, are you seeing, are you seeing competition from China? Is there, are there people that are, uh, is, are there fans out there?

**Jørgen Jakobsen:** And I think also the, the, the thing that is, uh, is the trend right now is that the, the company that runs the hearing aids are also eating up some of the shops that actually are selling the devices that way. So it's a full, uh, development, uh, to end users in that way.

**Chris Gammell:** Uh-huh. Okay. Yeah. That makes sense. Yeah. And I guess they, I mean, it, it does seem like an insular industry. It's like you, you have probably, uh, what are they called? Audiologists that are recommending certain things as well. So it's a controlled industry kind of thing. Yeah. Well, that is very interesting. Um, and so, okay. So, yeah, go ahead.

**Jørgen Jakobsen:** So what you've got today is actually, uh, devices that, uh, connect you with your iPhone. So you managed to put Bluetooth, uh, low power links in there. Um, and that has been the, the, the great fight. Um, yeah.

**Chris Gammell:** Why is that?

**Jørgen Jakobsen:** Yeah. It's a, it's a matter of, uh, instead of having a proprietary, uh, technology that is not comfortable, uh, compatible with the other things, then right now you can just connect your iPhone to your, your air plugs. And that's the way it should be.

**Chris Gammell:** But is it because they, they don't, they don't want to, they don't want it to be like an open standard anymore. They want it to be like controlled or what?

**Jørgen Jakobsen:** No, it's, uh, it's, um, so now it, it is, uh, you can use your open standard, but you probably have some like, uh, proprietary protocols to, to, to run there. But the radio system that you use is, uh, normal Bluetooth, uh, Bluetooth LTE, something like that.

**Chris Gammell:** Okay. Yeah. So the, the hardware is, the hardware is the same, but the, the software and the, the, the control stack is different.

**Jørgen Jakobsen:** Yeah. But, uh, and I think you need to do a lot of tricks to pull down the power consumption on these devices there. You still have the budget sub one, uh, milliamps and some of that, uh, only have a small portion of that is, is left for you for doing your analog, your, your, uh, wireless connection.

**Chris Gammell:** Yeah. Okay. So, and could you give us a, so you've done Bluetooth stuff, you've done all this RF stuff. What, what, what are the relative amounts for, for, um, cause I guess you're streaming audio too over RF. So that's gotta be pretty, pretty power hungry, right?

**Jørgen Jakobsen:** Yeah, it is. Uh, um, actually, but that's, that's more a feature, but, but I think, uh, for, for, at that time we did the audio streaming sub 200, uh, microamps. Oh my goodness. So running a, yeah, running a receiver in that way, doing the digital decoding and audio processing.

**Chris Gammell:** Do you actually, do you actually like down sample the stream as well to, to like get the data rates down as well or what?

**Jørgen Jakobsen:** Uh, you, it has limited bandwidth and it was a, a, a special codec that could do real time because again, it's the TV market you are addressing. Uh huh. So you cannot, uh, have latency in, in that, uh, audio chain. Right. So that's another hard thing to, to handle.

**Chris Gammell:** I guess that's true. You don't need to send, you don't need to send zero to 20 kilohertz when your, your customer is not really capable of hearing all of that. A good chunk of that anyways. So, yeah. Yeah. Yeah. You send like one K to three K and you just chop that up and spread it. Yeah. Yeah. Yeah. That's interesting. Oh, so that's, it seems like a lot of custom, like you said, custom codecs, stuff like that.

**Jørgen Jakobsen:** Yeah. So I guess that all the major brands in Denmark, they have their own, uh, IC development tools and nothing was shared between these companies. So chunks of, uh, engineers in each part. And there was a time where it was not allowed to move, uh, between these. Oh, really? Off the record.

**Chris Gammell:** Interesting. Yeah.

**Jørgen Jakobsen:** Of course that's not allowed. Yeah. Right. But, uh, but then there was some managers that moved from one company to the other one. And then everybody said, okay, no, so we can also do that. Right. Right. And there was a bit of more, uh, mobility between the. Right.

**Chris Gammell:** So that's just, that's just industry politics basically of like, uh, yeah.

**Jørgen Jakobsen:** But I think that the, the companies are running good. It's interesting stuff to be in and it's, uh, there's a lot of tape outs there. So are you analog designer, digital designers? There's a lot of challenge there.

**Chris Gammell:** Oh, believe it. Yeah. I mean, I mean, as an industry too, I imagine that, you know, as the baby boomers continue to age, there's just such a huge market there, especially because they expect this kind of activity, like you're talking about, like every, every baby boomer has an iPhone already. And they, then as their hearing goes, they want to be able to keep hearing it, you know? Yeah. So.

**Jørgen Jakobsen:** And more features would come into the hearing aids. Oh yeah.

**Chris Gammell:** What kind of stuff? Like.

**Jørgen Jakobsen:** I don't know, but, uh, like, uh, we're talking about agents. So I guess that at some time you could speak to your agent, uh, you could speak to Alexa. Uh, so that kind of connectivity would actually be able to be put into your device in that way. So, so if you put it down as a consumer, uh, product, you could probably get a larger audience in there.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** But again, you have to wait if that's what you would like to do.

**Chris Gammell:** That is interesting. Cause there's a lot of, well, I guess there's the, uh, Apple ear pods or whatever they call those things, right? The, uh, and those are low power, but those only get five, five hours of, of, of playtime anyways in a best case scenario. And, and I, so is there, have you seen crossover from that industry into other industries like consumer, like you're talking about? Or is it not really?

**Jørgen Jakobsen:** It's, it's, it's been really, uh, hidden away and the development that goes on there is that far from what's going on.

**Chris Gammell:** So, so listeners here wouldn't be able to go out and buy a, uh, IC that's in one of these things anyways. No, definitely not.

**Jørgen Jakobsen:** Yeah. Yeah. You will not be able to do it. It's a custom chips, uh, for all of the brands there. So, yeah.

**Chris Gammell:** Wow. And so what about the, um, so, okay. So you said, I mean, obviously Copenhagen has this, this talent base where, what about the, uh, the manufacturing piece though? Is there, are there fabs there or are they going to global foundries and all of them?

**Jørgen Jakobsen:** No fabs. Everything is done from outside the country.

**Chris Gammell:** Okay. Interesting. Oh yeah. I mean, that's, it's surprising that it didn't, it didn't come up with that. I mean, any, any idea why that happened?

**Jørgen Jakobsen:** Yeah. I think, uh, the, the fab industry is driven by the large IC, the high runners, uh, million things. So, so I think, uh, at that time where I was around there, we did maybe 1 million devices a year or something like that. Right. Right.

**Chris Gammell:** Which is a lot, but pittance for, too fab, right? Yeah. Yeah. So like a week, a week of the year, uh, in terms of runs. Yeah.

**Jørgen Jakobsen:** Yeah. Small corner. Yeah. Okay. And the same goes for testing. So. Oh yeah. Right.

**Chris Gammell:** Yeah. What about, what about testing? I mean, so you, so you were developing these things, you, you got a tape out, you got a prototype chip. Are you, are you taking this back to your, your bench? I mean, like, how does that work for you?

**Jørgen Jakobsen:** Yeah. So the next thing is that you, uh, when you do the IC design, you also think about test and the, if you did not, you totally. You're screwed. Yeah. Yeah. You can say it. Yeah. It's fine. Yeah. So of course that, uh, at that time, and then, then you typically do test development together with a test engineer, test house.

**Chris Gammell:** Uh huh. Okay.

**Jørgen Jakobsen:** So they have the expertise in running, uh, these high speed testers. And, uh, then it's a challenge to do a full qualification, uh, sort out the bad ICs from the good ones in less than four seconds or something like that. Oh my God. Yeah. So that's another challenge, but it's, uh, it's possible. And, um, yeah, it's doable.

**Chris Gammell:** I guess, I guess if you go from four seconds to five seconds, that's times a million, right? And then you got to pay for all that extra time.

**Jørgen Jakobsen:** That's a narrative there. And that's why you do it like that. Yeah. And the test cost is actually a significant part of, of a budget in that way.

**Chris Gammell:** Right. Right. Well, and you've mentioned too earlier in the show about the, um, like blowing fuses and, and if you, if you're able to dial in your process more, you actually are able to save on your test times and your, your, um, your adjustment times and stuff like that. Right.

**Jørgen Jakobsen:** Yeah. You have to do compromise there. So you need to make sure how fast the, the, what impact a given trim process will do. Could I do it without the test or could I do it? So the decide the device actually run the test on its own, things like that. And that's, uh, that's a challenging part.

**Chris Gammell:** So you have to hit a spec on, uh, on like variation on frequency and stuff like that on the output of your, of the chip that you're designing. Does that end up impacting like FCC testing? Does FCC come back and say at the chip level ever that, um, it's not hitting?

**Jørgen Jakobsen:** It's no, it's, uh, typically what you do is that you'll put in handles so that you could, for instance, move your frequency of disturbance. Oh, interesting. Okay. Move it outside. If you have a product that goes together with an AM radio, for instance, you don't want to hit one of that. Right. Yeah.

**Chris Gammell:** 760 kilohertz or whatever the, yeah. Yeah.

**Jørgen Jakobsen:** So, so you do something where you can actually, it did sort of control your frequency to something other place, but there's a lot of frequency planning. And when you do, uh, especially RF stuff, but also what we do today where we have a high frequency, uh, uh, shifting, uh, switching. Oh yeah.

**Chris Gammell:** Like three bigger switchers for DC to DCs, like stuff like that.

**Jørgen Jakobsen:** And not especially there, but the output stage of, uh, of, uh, is the dirty bastard. That's the one you would like to.

**Chris Gammell:** Let's talk about these dirty bastards. Cause that is what you're doing, uh, as you, at your current place. So you were working on audio stuff now. Let's, let's hear all about it. Cause this is another area where, uh, we've had some audio people on in the past, but this is super interesting to me in terms of. Yeah.

**Jørgen Jakobsen:** So I guess that, uh, actually the, the show is called the amp hour, but we are actually

**Chris Gammell:** doing an amp, um, an amp through, through the, through the output stage.

**Jørgen Jakobsen:** Yeah. So, so, so what we do is actually, uh, class D amplifiers.

**Chris Gammell:** Oh, oh, oh, oh, amplifiers like that. Not like an amp, like the amp, but you're saying like, aha, right, right. Well, yeah.

**Jørgen Jakobsen:** So, so what happened is that, uh, I got stuck at, uh, at, uh, doing hearing aids and, uh, yeah, I just needed to do something new. And, uh, I found, uh, two people out at the DTU again, they had formed a company one year ago and, uh, they have prototyped the novel, uh, output stage and, uh, they had some market insight into the class D market and, uh, they wanted to build a company. So they needed some guy who could actually do a chip implementation of that. And I said, yep, that's me. That's you.

**Chris Gammell:** That's great. Yeah.

**Jørgen Jakobsen:** I can do whatever you want. Programming, database, uh, digital analog stuff.

**Chris Gammell:** We have the Renaissance man of the Silicon industry here.

**Jørgen Jakobsen:** I think you, you do, you, you need to be very multi-talented when you're into, to this.

**Chris Gammell:** Yeah. That's the fun stuff too, right? I mean, this sounds, that sounds like a blast. I mean, honestly, that's crazy. Yeah. Yeah.

**Jørgen Jakobsen:** So, so, uh, we started up there and, um, got a first, round of funding there and were able to prototype, uh, the concept and take the pattern that needed there. And, uh, actually it was a combination of, uh, this guy doing, uh, uh, power electronics, uh, switch mode, uh, supplies, uh, utilizing that technology on, uh, standard class D output stage. Yeah. And combining these two things actually led into the technology that we now have in our chips today.

**Chris Gammell:** Right.

**Jørgen Jakobsen:** And, uh, that is, uh, multi-level. So, I think I need to explain that because when you have a class D amplifier, you either have your, uh, your power, uh, level. So, for instance, you have 12 volts on your, um, on your device, you would have 12 volts or you have zero volts. Right. And switching between that with different modulation type, actually, uh, using that technology, you can actually, uh, like generate analog voltage in your speaker.

**Chris Gammell:** Right. So, and yeah, yeah, exactly. So it's, it's a switching technology. It's a, on, like you're saying, digital on, off, but then it goes through, uh, well, I think we'll have to modulate this a little bit, the, the explanation, but usually it goes through an LC filter and then that changes that, that, uh, you kind of take out some of those higher frequency components.

**Jørgen Jakobsen:** And yeah, exactly. You get, you get rid of the high frequency, uh, shifting frequency and what you're left to is the audio signal there. Yeah.

**Chris Gammell:** And that's higher, much higher efficiency than a class AB or a class A that's like class A is what max 33% efficiency or something. I forget what the number is.

**Jørgen Jakobsen:** Yeah. That's, that's right. So we way past, past the AB technology and we have all moved into the class D thing. But the problem with the class D thing is that when you actually don't send out any signal, you want to be in between your, uh, 12 volts and your zero volts. Oh really? And that actually means that you have a big loss in your switching, uh, sub, sub, uh, suppression filter. Yeah. So constantly there you are losing power. And, uh, that was what we saw there and, uh, doing, uh, uh, output states that can, uh, generic output, uh, uh, exact, uh, between your 12 volts and your zero is this, um, three level output states that we have.

**Chris Gammell:** Huh? Okay.

**Jørgen Jakobsen:** And then combining two of these stages, uh, in what you call a bridge tight, uh, load setup, you're actually able to do five level.

**Chris Gammell:** Really? Okay. Yeah. And so, and when you say that there's, there's losses there, is it because there's like leakage from the rails to that six volt point or what, what is the actual loss?

**Jørgen Jakobsen:** The physical loss is, uh, one thing when you turn up, uh, on a transistor and you shut it off again, there's a, there's a rather large amount of, of charge that goes into that transistor.

**Chris Gammell:** Yeah. So just turning the gate on and off that kind of thing. Yeah. Exactly. Yeah.

**Jørgen Jakobsen:** And we even have, uh, like patents on how to turn on a transistor.

**Chris Gammell:** You people thought people listening now, you think, you know, how you use a transistor. Uh, ha. I think again,

**Jørgen Jakobsen:** yeah, but it's, it, uh, yeah, the problem is that the, and because you are, your transistors are better from your P substrate, no, from your N substrate compared to the P type, uh, uh, MOSFET, you use your, uh, N type transistors also for the high, uh, output switch node.

**Chris Gammell:** Hmm. Interesting.

**Jørgen Jakobsen:** So for doing that, we need a voltage that is higher than your rail. So you need to produce a supply for that. And that supply is going to track your transistor when it flies up and down. Complex stuff, but that's, uh, maybe another story.

**Chris Gammell:** Well, no, that's good though too. So you mentioned this is all, uh, uh, patented, which means that it is public. So people can go and read these, right? I mean like these are, that's, that's the best part about patents. So I'm looking these up. I'll link some of them in, you know?

**Jørgen Jakobsen:** Yeah. And also the thing is that you have like good patents, you have bad patents, bad patents, something that is hidden within the chip. Good patents is something that you can observe from outside. Right. And we definitely can observe people as doing what we claim to have invented.

**Chris Gammell:** Yeah. Well, that's really cool though.

**Jørgen Jakobsen:** So what we do is actually, we, uh, apply that kind of modulation that actually is, uh, needed for the output signal. So if you don't put any, uh, large volume signal into our amplifier, we are just steadily, uh, balancing, uh, zero or a half VDD out of the stage. Hmm. So no idle laws in that way.

**Chris Gammell:** And when you say, uh, when you say not putting anything out, do you even mean those small pauses from like, uh, it's like almost like a, like a, uh, what's it called? A gate, a gating mechanism. So if there's a little bit of sound, you, you, you kind of say where the gate is and you say, oh, well, that's effectively nothing. So we're just going to turn it off at this point.

**Jørgen Jakobsen:** No, we don't turn it off, but we have lower switching activity and, uh, we just need a bit of, uh, output signal. So we could like just turn it, uh, turn it on a bit, turn it off a bit later. So, so, so very small modulation that way. And if we move in and use, uh, five live level, uh, modulation here, we also have the ability or the, the, the, um, the good thing that we don't switch that much energy from, uh, from one state to the other one. So you don't have this long, um, EMC spikes coming up from the device itself. Yeah. So there's a lot of other good things doing here.

**Chris Gammell:** That's great. So, uh, but let's get to the top line spec too, cause this is, this is what you were telling me about before when we talked before the show. So what is, what does this ultimately manifest as in terms of like power savings for these chips?

**Jørgen Jakobsen:** Yeah. Typically, uh, what you see is that, uh, when you have a Bluetooth wireless connected, uh, uh, kind of, uh, uh, radio thing, then you need to turn on the amplifier. And, uh, when it not place any audio out or just the very small audio level. So that's what we call normal listening level. Uh-huh. Then you have a big loss in your inductors, uh, with your filter there. Uh-huh. So I think we, uh, we will be a factor 10 less power consumption in that area. Uh-huh. So the, the, the, the great, uh, efficiency that you have from class D amplifiers, that's what you have when you turn up the volume to party level.

**Chris Gammell:** Uh-huh.

**Jørgen Jakobsen:** But when you move down to normal listening level, you don't get that. You only get losses. Uh, so that's our claim that we have moved that area where you actually use the, the amplifier most of the time.

**Chris Gammell:** Mm-hmm.

**Jørgen Jakobsen:** But we will still be able to do party time with you, uh, because we can turn our stage into a normal class D amplifier.

**Chris Gammell:** I think you guys are missing an opportunity to just say, we make party time all the time. That's what I've, that's what I've, I don't want to help you with your marketing or anything, but I'm just saying, you know.

**Jørgen Jakobsen:** No, no, no, no. That's, uh, that's one possibility. Yeah. But I think, uh, the, the customers that we engage with, they are very eager on what is the, uh, the battery life of a given application. And they see that people are not doing party time all the time. Right. They use the device for, uh, medium, low, uh, listening levels. Right. And it's, it's pretty, uh, uh, compelling when you start looking on how much sound pressure you get from only delivering what, what, a lot of zero, a lot of one, what into an amplifier loudspeakers. Yeah. Um, yeah.

**Chris Gammell:** Yeah. I mean, well, yeah. And you had mentioned as well, like the, I mean, the, the surprising rise of Alexa, you know, like, or the, I guess the Google or the Amazon echo rather, and like Google home to like all of these like voice connected devices that are like all coming online. So there is a focus on this. Those are all, you know, connected to the wall, but there's no reason that they have to be into the future. And, and, and it's definitely not like there's going to be, there's going to be other devices doing the same thing. I'm sure.

**Jørgen Jakobsen:** Yeah. And I think that, uh, the ability that you can have these kinds of devices that both can give very nice sound because you get that from various small devices today. Yeah. Uh, and that is mainly done by doing good acoustics, good loudspeakers and do some filtering there so that you can actually separate your travel and your base and you are able to, uh, yeah, make a good audio product by working with that. Yeah. Uh, so that is one thing. Then the other thing is that you will also want that device to have long battery time or be something that is, uh, good for speech. And that is, uh, again, something where we come in and have a great product there.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** Well, and so one thing on top of the, of, of doing an audio amplifier, we also need to have digital input. So, uh, we still, we, we actually have four, uh, decks built into the amplifier also. Right. So imagine that you can have, uh, uh, in a nine by nine millimeter housing flat pack, uh, four channels of, uh, D to D to a conversion, uh, and two channels of audio amplification up to 70 Watts.

**Chris Gammell:** Wow. That's, uh, yes, that's, that's, that's not, uh, that's not big. I mean, that's a big, that's a big output, but that's not a big, big package for sure. Like that's crazy.

**Jørgen Jakobsen:** Yeah. And the thing is that you don't need then bulky, uh, um, filters at output. You don't need bulky caps to hold your rails. You don't have to have split supplies as you're used to have with other kinds of technologies there. Yeah. Um, so the, the form factor of your amplifier is really decreasing, decreasing a lot. And then with the ability that we have, we, okay, can save customers one battery in, in their design and they, they're, they would like to do that.

**Chris Gammell:** Yeah. Yeah. I'm looking at the block diagram. You did say that the data sheets are public now, so we can, I'll, I'll link those in as well, but I am looking at the block diagram and I'm a little confused though. So like, so you're showing four DACs, four power amps, but then the power amps drive each side of the speaker. Is that right?

**Jørgen Jakobsen:** Yeah. So that's what we call a bridge tight load. Okay. So you can configure the device up, uh, how you want it. So you're going to have four single ended devices. That's actually why we have the, the four DACs in there.

**Chris Gammell:** Okay. Yeah.

**Jørgen Jakobsen:** So you can drive four tweeters, something like that, each of, uh, around 10 Watts, or you could combine into, uh, uh, two channels of bridge tight load. Then you would, uh, utilize all the fancy, uh, features we have in the device. Or you could, for instance, do a combo where you have, uh, two single ended channels, one, uh, BTL for a big base and left, right channel. So, or you could combine them all into a more powerful, uh, driver, low omic, uh, drive or something like that.

**Chris Gammell:** Gotcha. And so could you explain a little bit too, like the one thing I I've, I've done a little bit with, with, uh, class D stuff, but not much. I don't quite understand how that, what is happening that you are able to remove the LC filter on the output? Like, is it just that the, the amplifier has faster feedback that it understands where to turn on and off?

**Jørgen Jakobsen:** Yeah. So, so it, again, it depends on your application. So you can have some application where you totally get rid of the, your output filters. So if you drive the device, uh, in some power modes, uh, not utilizing the very high, uh, outputs, uh, normal operation, then you can remove the filter, uh, completely. But if you want to drive it into very high loads, uh, you need to, to operate with, um, with a filter also.

**Chris Gammell:** But is it because the, is it because the speaker acts as a filter because it's inductance that acts as the filtering as well?

**Jørgen Jakobsen:** Yeah, the speaker act as a inductance, but imagine that you have a long wire from your actually, uh, amplifier out to speaker that is remote. That will act as an antenna and that will actually be the troubles that you run into when you try to go to market and things like that.

**Chris Gammell:** I see. Okay. So it's, it's, it's about like you're sending out these pulses that drive the speaker, but ultimately you send a pulse to a, what effectively looks like a big inductor anyways, and that's going to get the edges off or whatever happens.

**Jørgen Jakobsen:** But what, what you also would see is that you are starting to divide up. So you, instead of having a passive filter in your speaker, you will put one amplifier in front of each of your speakers. So one for the treble and one for the bass, and then you will do your EQ, uh, in a DSP somewhere else in the, in the audio chain. Uh, and that is also a field that is involved pretty heavily at this time. Right.

**Chris Gammell:** Like something like putting a microphone. So it's almost like a sensing application, right? Where it's like you could put a microphone out by the speaker and feed it back and figure out what's going on.

**Jørgen Jakobsen:** Not really, but, uh, but that kind of split is done when you do the acoustic design of the, of your application. So you design that, okay, your woofer would only take a frequency band up to 200 and then I want my tweeter to take over. So you put that kind of, uh, uh, processing, uh, prior to feeding it into our chip in that way. So you have a DSP functionality to do that kind of stuff. Yeah.

**Chris Gammell:** So is there, is there active feedback in the, uh, in the amplifier that like, how does it understand that the pulses that it's sending out are actually delivering?

**Jørgen Jakobsen:** Yeah. There's a lot of feedback there. Okay. So it's a, it is actually a loop, uh, tight control. So what you put in there comes out. Okay. So if you want to drive a DC motor, you can do that.

**Chris Gammell:** Really? Okay. I mean, I guess at a certain point you're just, uh, selectively connecting the rail to the device, but, but that's still a weird thought to me of like, Oh yeah, like a motor speaker, you know, whatever, same thing. Yeah.

**Jørgen Jakobsen:** So it, um, yeah, you can do that. We've done that. Um, so the inventor here, he has daughter. He wanted to get her away from, uh, the iPad and thought some Lego motor. Maybe that could, could we use our trip for that?

**Chris Gammell:** Uh-huh.

**Jørgen Jakobsen:** We could do that. No problem.

**Chris Gammell:** That's cool. Wow.

**Jørgen Jakobsen:** Probably the other better chips for doing that.

**Chris Gammell:** Yeah. Yeah. Probably. Well, that's the thing. It's like optimized for, and I'm sure that the other thing here too, that you were, you were optimizing for standard eight Ohm, 16 Ohm speakers, whatever the standard is, you understand. And even with the feed, the tight feedback loops, you understand the kind of loads you're driving, the kind of characteristics they have. Right.

**Jørgen Jakobsen:** But that's another trend that we see that, uh, you would like to push as much as you can out to the speaker. So, so next generation, uh, would probably have some kind of knowledge about the speaker that you're driving. Right. So that you are not killing the.

**Chris Gammell:** Yeah. So like put, put like a EEPROM on it and then like have it like self-characterized or what?

**Jørgen Jakobsen:** Uh, probably from a design system, uh, system design from startup. But, um, I think people are doing a lot of, uh, of, uh, like, uh, trying to, um, to predict what kind of, uh, power is actually put out to the speaker. And then you have knowledge about what, uh, what that speaker actually will, uh, do before you have to turn down the volume. Right. So, so in our device, we have, uh, like same kind of functionality. If, if people, uh, like shorts or a short circuit, the output, it will protect itself. If it gets too warm, we will crank down the volume and then survive from there. Interesting.

**Chris Gammell:** Like without, without an actual remote temperature monitor, you just able to like kind of see how things change.

**Jørgen Jakobsen:** We have, uh, we have, uh, that internally in the device. Huh?

**Chris Gammell:** That's cool. Yeah. Well, what about the, so I2S, I, uh, that's another thing that I don't quite understand.

**Jørgen Jakobsen:** I think that's another trend that we will see that, uh, more and more like, uh, microprocessors that you see out there, they have like a digital audio output. Take for instance, the SP32. Uh, it has two channels, uh, of I2S output that is able to deliver, uh, um, uh, 24 bits, uh, in, uh, some crazy sample rate, uh, more than what you will, uh, um, see as hi-fi. Um, so from one single there, you could actually drive, uh, four channel individually. Wow.

**Chris Gammell:** Really?

**Jørgen Jakobsen:** So, uh, it is, it is actually very easy to set up there. And that's, I think another trend that we'll see that people typically not from the audio industry will be able to do high quality audio products using, uh, this kind of technology.

**Chris Gammell:** So something like an ESP would have like a library just for like pumping audio out and then ties into a device like yours and just kind of works.

**Jørgen Jakobsen:** I actually did some groundwork there and trying to, uh, somebody released, uh, some, uh, code that actually proved that you could run a full stack of, uh, MP3 decoding on that, uh, uh, the, the forerunner of that chip.

**Chris Gammell:** Oh, on the, uh, 8266 or something?

**Jørgen Jakobsen:** Yeah. So at that time, a lot of people made, uh, Wi-Fi connected Bluetooth, uh, receivers, uh, Wi-Fi connected MP3 decoders. So, uh, so you can just feed out that, uh, signal into an amplifier and like that. And the new version that we have, there's more power on that. So I turned it into stereo and, uh, it works flawless. So I think, uh, when, uh, when people are starting to see that, uh, they might also be able to put in a little bit of DSP processing in that, uh, in that device. And then with a very small setup, you could maybe connect a couple of microphones in front of there and you could maybe have a lecture platform. Really? With only two chips.

**Chris Gammell:** Wow. So that's, yeah. And then not a lot of size, not a lot of power, but I mean, yeah. Battery, battery controller, maybe too. You have to. Yeah.

**Jørgen Jakobsen:** Battery. No problem. So, um, so I think what is the biggest drawback now is that, uh, the, the Wi-Fi connectivity actually take up a great amount of, uh, of audio.

**Chris Gammell:** Right. Yeah.

**Jørgen Jakobsen:** Of, of power consumption right now. Right.

**Chris Gammell:** Right. But as libraries get better too, they'll selectively turn on and off stuff like that.

**Jørgen Jakobsen:** Could be something like that. I doubt that you will be able to do that if you need to manage, uh, audio stream coming down, but I think, uh, that's what, uh, is need to be, uh, found out. I think, uh, the device is out now and, uh, there was, uh, there are a few bugs that we found, um, that is hopefully being fixed here in second generation of, of that, uh, thing. And then.

**Chris Gammell:** Does the 32 have Bluetooth on board? I, I have not seen it yet.

**Jørgen Jakobsen:** They have Bluetooth and they have wires. So, and they proved that it works and they have some products in the pipeline or some example of doing, of, of utilizing that. And, uh, I've seen it myself and it's, the devices, uh, is pretty easy to work with. There's a lot of support from the open source community. Um, yeah. Fun stuff to play with.

**Chris Gammell:** Yeah. Well, what about your device? So how do, so, uh, it looks like there's, you said there's four devices that MA 1204.

**Jørgen Jakobsen:** Yeah, so we have a 40, uh, 40 range, uh, 40 watts, two times 40 watts and a two times, uh, 70 watts. Yeah. And, uh, we have analog input. We have digital input and that's the lineup.

**Chris Gammell:** Oh, that's the P versus the non P. Is that the idea?

**Jørgen Jakobsen:** Yeah. So that's the. Gotcha.

**Chris Gammell:** Well, that's cool. Uh, and able to purchase now or how do, how do people get their hands on one of these things?

**Jørgen Jakobsen:** Uh, we are trying to go to get out there. Uh, we have set up volume production right now and we have samples out at customers. We have that for, uh, for a year or two now.

**Chris Gammell:** Okay. Okay.

**Jørgen Jakobsen:** And the, um, so we have some customers, uh, and, uh, yeah. So, so, uh, people are, uh, being more and more convinced in the technology that we master. And, uh, and again, the audio industry is a bit conservative on what is good, what is not good. Uh, there's a lot of, uh, like subjective, uh, feelings about it. I think you touched that. I think so too. Yeah. So if you can buy a cable for your speaker that is, yeah, uh, $200, you can hear it yourself.

**Chris Gammell:** Right.

**Jørgen Jakobsen:** Right. But you might not be able to measure it.

**Chris Gammell:** Right. And you're never going to be able to convince some people that class D is going to even approach a class A and it's like, whatever, you're just not the customer in that case. You enjoy your, enjoy your heater. Right.

**Jørgen Jakobsen:** Yeah. Sure. And that way. But, uh, I think, uh, when you do, uh, blind testing in that way, I think you will see that we are getting there.

**Chris Gammell:** Oh yeah.

**Jørgen Jakobsen:** And I think that the, the concept of distributed amplifiers also will enable things and, and make people wake up and see that you can do another or other kind of audio products that way.

**Chris Gammell:** Yeah. No, that's great. That's, that is definitely the, the, I'm really surprised at the, you know, we, like, like we said, like the Alexa piece or just even, I mean, hell, even podcasts. Like I'm surprised that audio is still such a, uh, important piece of kind of the conversation these days of like processing and, and user interaction. But I guess it makes sense. I mean, we're used to telephones, we're used to everything else. And yeah.

**Jørgen Jakobsen:** Yeah. And I think a lot of, uh, innovation still have to go in there. If you look, uh, at what kind of, uh, audio processing is actually put in to the aged, uh, so it's over the, uh, standard for doing normal, um, web programming.

**Chris Gammell:** Uh-huh. Yep.

**Jørgen Jakobsen:** You actually, there can do filtering, uh, FFTL analysis, things like that. You can even, even hook up your microphone to your, uh, browser. So in that way, see your waveforms of doing that. Um, pretty amazing stuff you can do there.

**Chris Gammell:** Um, so at some point we're going to have, uh, you'll have a Bluetooth connected chip like yours and while Bluetooth plus your chip, but then just talks directly to like a chromium or something. Is that the idea?

**Jørgen Jakobsen:** Could be.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** Yeah.

**Chris Gammell:** That's crazy. Why not? Awesome. I can get pop-up ads when I'm not even expecting it. I'll be able to walk, walk into the bathroom and Crest toothpaste is like, make your teeth sparkle. Yeah.

**Jørgen Jakobsen:** Yeah. I guess in our, in our, in our space is still with the output stage. So we are still just the amplifier in this ball game. But again, it's a price costs. How cheap can you do it? Yeah. Right. With good quality. Uh, we, uh, also have a measure so we can, uh, tune up the, the audio quality, uh, at an expense of more power consumption.

**Chris Gammell:** So, yeah.

**Jørgen Jakobsen:** And that's the funds, uh, uh, for the application designers that they can actually tune whatever they would like to do without chips.

**Chris Gammell:** Right. Exactly. If you want, if you, if you deem it worthy, you just spend more battery, battery cost or whatever. Yeah. More charge on each, each individual application. Yeah. That's great. Um, well, so what, what else do you see in the, I mean, you see the, the, the browser connected audio. That's very interesting. Other, other things.

**Jørgen Jakobsen:** I think that also the, the, the, the sign features there. So you, uh, will be able to like fine tune, uh, your audio response. So EQing of your personal system, uh, will be more and more normal control from your, what your phone, um, a lot of, uh, so the audio in your laptops, for instance, is getting better and better. Um, but I guess this is more or less, uh, a matter of your speakers that you put in there.

**Chris Gammell:** Mm-hmm.

**Jørgen Jakobsen:** Um.

**Chris Gammell:** Like the physical size and all, and the power that you're delivering.

**Jørgen Jakobsen:** Physical size, uh, the quality of it, uh, uh, reducing the resonance from, from other components in the chassis, things like that.

**Chris Gammell:** I'm really surprised in my, in my own experience that I, I, I'm, I'm surprisingly delighted at being able to kind of throw audio around the room. Like, so I use like Spotify premium stuff where I can just pick which speakers it plays on. It can, eventually I'd like to just have it like follow me, you know, like have audio playing and it's just put my headphones in. It's there, take my headphones off. It's in the living room. Yeah. Yeah. That kind of stuff is really interesting to me.

**Jørgen Jakobsen:** Yeah. I think that's, uh, that kind of innovation has to come from, uh, smart people combining technologies.

**Chris Gammell:** Right. Yeah.

**Jørgen Jakobsen:** On their own. And the, the, the piece of bits and pieces needed for systems like that is out there. Yeah. Right. They should be able to do it.

**Chris Gammell:** Right. It's like an ecosystem thing versus a individual set of devices. Right.

**Jørgen Jakobsen:** Yeah. Hmm. Talking about ecosystems. Uh, I think that's, uh, that's another big gain for, for engineers like me, uh, for instance, that you have Raspberry Pis, that you have all these programming platforms. Uh, so you can actually demonstrate your, uh, technology. Yeah.

**Chris Gammell:** Yeah. Didn't you mention you were doing testing with like, uh, Raspberry Pis and stuff too?

**Jørgen Jakobsen:** Yeah. So we have a lot of burning testing, uh, going on here, burning a lot of kilowatts, uh, having the amplifiers, uh, in some lifetime, uh, accelerated lifetime tests. Uh-huh. So we cranked them up for a long time, uh, month, one month. Really? And, uh, so they play music generated from Raspberry Pis and the Raspberry Pis are constantly, uh, over, uh, monitoring these devices, checking the temperature of the devices and, uh, feeding it back into, uh, to a database. So like 80 of them in one, uh, one very loud room. 42, 20, uh, rack.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** Yeah. That's good. That's good in the wintertime because it generates a lot of heat. Right.

**Chris Gammell:** Copenhagen is not, uh, not very warm.

**Jørgen Jakobsen:** No, it's cold at the time. Yeah. Right.

**Chris Gammell:** Right. What about, uh, is, is there like a standard song that you guys use to test or is it, uh,

**Jørgen Jakobsen:** actually that's a fun story because, uh, when you state that your amplifier is a 70 watt, uh, two times 70 watt, people actually believe that you can, uh, crank out 70 watt continuously from, from, from that's a guy. Yeah. Yeah. Yeah. Okay. That's not how it works. Um, it can do that in peaks and there's no music that actually have, uh, a 70 watt average peak there. Right. That's also why your loudspeaker is rated for some RMS. That's the continuous and your wattage of the amplifier. And that's all your speaker. And that's always a bit higher. So that is what we call the crest factor. So that's actually the amount of energy in that given song. And when you are talking with the, with the far East, uh, and you have some, uh, you demonstrate your amplifier out there, they always come with their own songs there because they have some K pop. Some Korean dynamics. Right.

**Chris Gammell:** So it's like super compressed. It's got tons of bass, tons of tweeting going on. Yeah. Yeah. Yeah. Yeah. Wow.

**Jørgen Jakobsen:** So, so that's actually, if you can, if your amplifier can manage to, uh, survive that and you made a good amplifier.

**Chris Gammell:** Is there a specific song though, or is it just all K pop?

**Jørgen Jakobsen:** No, I think they have some specific songs for that, but it's different from brand to brand.

**Chris Gammell:** K pop is, is, is tough to listen. It's, it's its own thing.

**Jørgen Jakobsen:** You know, it's like, another, another fun thing that we did in the lab, at least is, uh, burning off devices, uh, because we have this current protection system and we need to know where that, uh, stops. And there, we ran through some process step, uh, during the development that actually failed.

**Chris Gammell:** Oh.

**Jørgen Jakobsen:** And, uh, having a combination of, uh, 24 volts on a very small substrate, it actually blew up from time to time.

**Jørgen Jakobsen:** Right.

**Jørgen Jakobsen:** So when you test, you test it with glasses, uh, until you're confident that things work. But at, at that time, it's actually whenever, uh, somebody, uh, burned up a device, it's high five and, uh, okay, cool.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** We have a lot of control. We've done that in the lab and we don't want to, uh, make that happen out at customer sites. That's right. Yep.

**Chris Gammell:** Yep. That is what labs are for, right?

**Jørgen Jakobsen:** That's what labs are for.

**Chris Gammell:** Right.

**Jørgen Jakobsen:** And that's another thing. So being in a company where we do music, uh, then it's, it's okay here to crank up the volume and test some amplifiers from time to time. That's more fun than, uh, than doing hearing aids. Right. In my opinion.

**Chris Gammell:** Well, you know, if you, if you crank it up too, too high, you might have to, uh, you know, utilize a hearing aid eventually. You gotta, you know, watch your, watch your hearing protection. Right. Yeah. Yeah.

**Jørgen Jakobsen:** But then that's where a load boxes comes in. Lots, uh, packs of, uh, resistors that acts as, uh, as loudspeakers.

**Chris Gammell:** Gotcha. Right. You're just dumping power into that.

**Jørgen Jakobsen:** Yeah.

**Chris Gammell:** Yeah. I mean, you must have some really good speakers there though, right? Like being able to crank.

**Jørgen Jakobsen:** I think it's like the shoe, uh, the lazy shoe makers. The, the, the, their shoes are always busted.

**Chris Gammell:** Yeah.

**Jørgen Jakobsen:** Yeah. Sure. Things like that. So, but yeah, we have some, some decent stuff here. Hmm.

**Chris Gammell:** Yeah. I guess it would be tough if you like had a, a Monday morning test and you're, you don't want to be blasted K-pop at 140 dBs or whatever it is. No. So, yeah. Yeah. Well, that's great. So where, where can people find out more about this stuff or maybe find, find you as well online?

**Jørgen Jakobsen:** Yeah. I think, uh, what I do is, uh, sneak around in the, in the hacker spaces at night trying to get the, the ESP, uh, up running with the archip.

**Chris Gammell:** What's your local hacker space?

**Jørgen Jakobsen:** Uh, so Hacker Day. So that's the online space. Oh, okay. Yeah. I think that done a lot for the community. It's always easy to find people within, uh, interest in that way. Uh, um, and then from our website, I think that's, uh, the place to see, uh, our technology at least. And, uh, and hopefully it will be our amplifiers that will, um, be in commercial products and that you will listen through. Yeah. Um, so without knowing it, you will be listening to technology that we produced here.

**Chris Gammell:** Right. That's awesome. That's awesome. Yeah. Especially like, well, you mentioned that the, the chips are still sample stage, but, you know, eventually people will be able to hopefully catch it on a distributor site or something like that.

**Jørgen Jakobsen:** Yeah. Yeah. We are working hard to, to try and find an outlet where we can serve, um, everybody, both, uh, the big, uh, customers that we've been talking with for a long time now. Right. Yeah. And also the, the more hobbyist, uh, but also the guys that actually think that this is, uh, uh, interesting niche to jump into maybe their potential is doing the IOT stuff, but they just need to add some audio in the high quality. Yeah. That's, uh, a good opportunity to try to, to see how, uh, our chips works.

**Chris Gammell:** Yeah. Well, and we'll, we'll spell this site here. How do you say the name of the audio company again? Is it?

**Jørgen Jakobsen:** Meals audio.

**Chris Gammell:** Meals. Yeah. M-E-R-U-S dash audio.com. So if people are just listening, you don't know that we have notes, we have links, all the links will be on our show notes, but, uh, yeah, that's the way to get to it immediately.

**Jørgen Jakobsen:** Yeah. That's cool.

**Chris Gammell:** Yeah. Well, thank you so much for being on the show. This has been a whirlwind tour of analog IC design and audio and everything. So thanks. Thanks so much for being on. I'm really glad you wrote in.

**Jørgen Jakobsen:** Thanks a lot for being here and thanks for doing your podcast. I think it's very good for the community to, to, to listen in and to get inspired from other people.

**Chris Gammell:** Yeah. I'm sure. I'm sure we will have many people that are inspired. So thanks again for being on. We'll talk soon.

**Jørgen Jakobsen:** Okay. Thanks. Thanks.
