---
episode: 693
title: Small Scale Electronics Manufacturing with Colin O'Flynn
url: https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release May 13th, 2025. Episode 693. Small-scale electronics manufacturing with Colin O'Flynn. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Colin O'Flynn of Dalhousie University and also New A technology. Welcome back, Colin, for the third time. It's been... Thank you. Yeah, we're on like a five-year cadence here. You and I chat a little bit more often than that, but it's good to have you back. Yeah, a recorded five-year conversation. That's key.

**Speaker ?:** Yeah.

**Chris Gammell:** Well, you know, if we just keep this up, then it's like a little time capsule for each year we operate, right?

**Colin O'Flynn:** Yeah, time capsule for AI.

**Chris Gammell:** Right, to be able to better recreate our history, our future. Chris and Colin sound progressively older every five years. Both in temperament and in vocal tambulations. Complaining about more basic things. Yeah, right. Don't you hate soup? Ah, soup. I guess we'd like more soup. Anyways, how you been? So you're kind of back in academia a little bit more, huh? I think the past two times... Well, let's see. We have you on episode 239. And we'll obviously link these in. And that was in 2015. And then 552, which is 2021. And I guess you were just starting at Dalhousie in 2021, right? That's like when you just started there?

**Colin O'Flynn:** Yeah. So, and actually, it's kind of a... There's a story in there, too. Because in between, I was not at the university for a couple years. I had started back at the university. And then when Chip Whisperer and New A.E. was sort of taking off, I ended up leaving. Also over the pandemic, you know, things were a lot trickier to teach. So it felt like I needed to dedicate full time. Which at the time, you know, it's often you're deciding at the time of like, okay, that's the end of academia.

**Chris Gammell:** But I came back. Is it like an in or out kind of thing usually, too? I mean, I guess I don't really know. Like, is it... Was it hard to switch in and out like that?

**Colin O'Flynn:** It is. It depends. So I kind of got lucky with the timing that they were growing the computer engineering program. So this program didn't exist the first time. The first time I was actually connected more to like an entrepreneurship program. And they were growing computer engineering with the company or still able to publish. So I still publishing. That's normally the problem, right? As you go to industry, you don't have much time for publishing and you're kind of left behind. So it becomes harder to come back. So... But they promised me this time I can't leave and come back. They said there's a limit to how many times you do that.

**Chris Gammell:** Right. Right. They told me that, too. But it was more in an academic, probationary regard. Yeah. Chris, if you don't get those grades up, you can't come back. Everybody gets one. Yeah. Well, that's cool. So what is it... What are you publishing about these days?

**Colin O'Flynn:** So it's basically continuing on with... Right now, side channel analysis was some of my more recent work. I mean, which was previous work, too. But especially looking at side channel over different ports. So one more interesting thing was like using... Basically using jitter measurements. So as data flows through devices, the time delay varies with voltage, which means you can actually get a really accurate measurement of power on a device, which then gives you information about secrets. And so what I did is I ran that through the JTAG port, which is funny because this is the oldest attack. Like, right? Joe Grant's been doing JTAGulator for years.

**Chris Gammell:** Yeah. Right.

**Colin O'Flynn:** Everyone thinks JTAG is locked down. But yeah, if you run it in like a boundary scan mode, right? And you just do bypass, where it's just shifting bits through. You can basically shift through bits at pretty high, like sometimes a few hundred megahertz. And it basically gives you a pretty good scope. Yeah. Which is...

**Chris Gammell:** And what is the differential? Like, what's the jitter amount? Is it like nanoseconds, picoseconds that you need to be able to detect?

**Colin O'Flynn:** It's pretty small. Although the thing is that I did another version of the attack where what I do is it's called like fault sensitivity. But I basically clock in a bit right at the clock edge, right? And so depending on how that clock edge shifts, it's going to see a one or a zero. Um, and so you actually only get one bit of output data, you know, did a clock in a one or a zero. Um, so it's kind of like one bit GPS receivers type thing. The SNR is worse, but you get enough data and it still works.

**Chris Gammell:** So averages over time sort of thing or...

**Colin O'Flynn:** Yeah, exactly.

**Chris Gammell:** So, um, there's, yeah, there's a lot of pretty interesting stuff you can do with that. Do you need then like a super specialized scope? Is it like a scope on top of something like that chip whisperer? Or like, what is the, what is the measurement methodology for doing that sort of thing then?

**Colin O'Flynn:** Yeah. So for this one, it was actually just a old, you know, old school, but RF mixer. Um, so they, they also give you phase information as well as frequency if you mix the two signals together. So basically that's what was used is just a little, yeah, cheap mixer. So all the designs are available if someone wants to run it. And then I added it in, um, FPGA code to the chip whisperer.

**Chris Gammell:** Yeah, that's great. And then can you maybe run people down again? You know, every five years is good about like kind of how a side channel generally works in a broad scenario.

**Colin O'Flynn:** Yeah. I feel like I, sorry, I kind of dove into it. I don't know if this is the right intro, right? But, um, I should have started with what is side channel. I feel like more people know it now, but basically the idea is that you have information that influences some measurement you could do on the device. Um, which by that, I mean, specifically we're often looking at power analysis, which is, you know, as a device is running different instructions, take different amounts of power. So if your code does like a load or an ad or something, this will look different in a power trace. And it even gets more interesting, which is depending on the data transferred, it can vary a bit as well. So the, um, if you set a bit of a bunch of ones over a data bus, it takes more power out of a positive rail than if you send a bunch of zeros. Um, which seems kind of crazy that it's, you know, that you can actually measure that. I almost didn't believe it at first when someone said that, and then I was like, okay, let's test this. Um, but yeah, it actually works because it's charging right there. The, the, the bus internally is basically capacitance. Um, and so you're charging a capacitor to set it to a high or, you know, just charging, just set it to a low. And that comes from different power rails. So if you guys run one, you do see this.

**Chris Gammell:** And I remember, so I got to go to a training that Colin ran as well. And I remember sitting there and kind of like watching what looked like a scope trace on like a 3.3 volt rail. And then you saw, it was kind of like floating on top of that rail. You saw like action happening, whatever. And then eventually though, you were using that to pull out encryption keys, which was kind of the wacky thing to me. Like you were doing kind of, uh, cross-referencing based on different actions that were happening. I don't remember the exact part of that, but that's what's in my mind at least.

**Colin O'Flynn:** Yeah. No, I mean, that's pretty, that's basically, you know, a high level, what happens? The, the idea is right in that power trace. If I know at what point in time, for example, it's loaded an encryption key and it XORs that encryption key with some input data. Um, I know the input data because it's not secret. Like that would be the, you know, data coming in over the air, for example, I don't know the encryption key, but if I can use the power trace to say, Hey, there's, um, you know, it looks like there's more ones at this time after it did the XOR, um, or less ones. So we have this linear relationship. You could say, well, I know I put in, for example, zero, so there's zero one. So all those ones came from the key. Um, right. So by varying what the input data is, you can kind of, you can imagine that you could sort of slowly puzzle out in a way, right. What the, what the key is, because it's like, well, if I know I put in this and I see a lot of ones or low ones, um, and the only thing that's fixed is that key. Then I can kind of figure out what it is.

**Chris Gammell:** I'm still not sure. I quite remember. I remember XOR, but, uh, so basically though, you're, it's, it's kind of, uh, probing with no, so like known inputs, unknown kind of reference data, and then known outputs cause you're measuring it. So that's kind of the idea is you're back. So you're back calculating that key. That's kind of the idea.

**Colin O'Flynn:** Yeah, exactly. So, so that's the thing you basically have. And this works cause you have like, um, you know, the, the algorithms, they were not secret. Um, so you can build a pretty accurate system model. So the, the part that's kind of crazy is that if you do a test where all you do is you put different data on the data bus internally and measure the power at that point in time, it's a super, it's like a shockingly linear relationship. If I was, um, yeah, I'm always amazed when I do this demo and it's like, oh, that, you know, this sounds like a simple, uh, it's almost to protect against this.

**Chris Gammell:** Huh? I mean, that's the other thing too. That's interesting is like, I remember seeing some marketing material that maybe even referenced the chip whisper, but it was like from chip companies. Now chip companies are like looking at it. They're like, oh, we should fix this. And we have countermeasures to try and make it better. But it, like you said, it's, it's physics at the end of the day, it's like capacitance and charge. Yeah, exactly.

**Colin O'Flynn:** So, but I mean, and there is, there's a lot of ways to fix it so they can, you know, more complicated in the hardware. You can do dual rail and things where you basically have two different lines swinging high and low. So if you had a differential, right, the there's still a tiny bit of a glitch when it switches, but it's much, much, much more difficult to detect. Um, you can also change the algorithms a bit, like still using AES, but you can imagine, right? If I X or it in random data every time, um, and the algorithm is designed such that I can X or that data at the end to remove the effect of it. Like I've, I've complicated the attacker's life because they no longer know what's happening internally. Got it. Yeah. But I mean, the, the bigger thing, cause this, this often comes up and, you know, people say, okay, what should I do? Should I use super advanced crypto to avoid this? But it's like, what doesn't matter? The, the best choice, because, you know, as we might talk about later too, there's a million different attacks. And if you have one key for your 10 million devices out there, right? Like that's right.

**Chris Gammell:** That's, that's the problem for sure.

**Colin O'Flynn:** Yeah.

**Chris Gammell:** Right. Exactly.

**Colin O'Flynn:** Like that's the problem. If someone does a crazy power analysis attack and recovers the key from one device, like you shouldn't care.

**Chris Gammell:** That controls your whole fleet of devices. Yeah. That's, yeah, that's right.

**Colin O'Flynn:** Like you've made a bad decision early on and you're just trying to fix it through something

**Chris Gammell:** else. Right, right, right, right. Okay. So, and you had mentioned the power rails, you mentioned JTAG. Are there other like interesting, like, I guess you, I, you kind of have power in a couple of places. You might have the battery, you might have the USB port, the five volts and USB. Are there other like ports and other ways to do this sort of thing? Yeah.

**Colin O'Flynn:** Yeah. I mean, and that's kind of the, the interesting thing is that there's, so with this, this one doing this phase modulation stuff, it was kind of showing, you know, digital ports in general. So JTAG is one of the more accessible, but the other one, I, I didn't implement it, but sort of looked at was, you know, like an SD card or SDIO interface because that often is user. Right. Like some front panel interface has something in there.

**Chris Gammell:** Right.

**Colin O'Flynn:** Yeah. Yeah, exactly. And like, and they're pretty, it's high speed, which is good for being able to sample a lot of data. Um, so any of those interfaces usually encrypted through there or would that not even matter? Uh, it wouldn't because like really what you're doing is you're, you're basically using for the attack to work. What you want is a clock ideally that comes out from the target device. Cause that clock has small phase shifts encoded in it. Um, right. So if you get a clock and like the SDIO is good because it has a clock rate that runs quite a bit. Um, and you can kind of trick the system because you can send busy command busy states back. So if it does a read, you know, you send, you say, oh, actually I'm busy. Please continue to read for me. Um, and it'll just keep basically giving you a nice clock and every clock edge has some data encoded that, um, may do that. And then, you know, there's a similar thing. And one of the interesting things about, I don't know, one of the points of this paper actually that I had tried to make was not that, you know, this is a cool attack, but it was actually referenced in some of the earliest work. Um, you know, some people explored it and then sort of put it away. So like a lot of things in life, right. It's sort of been sitting there. Um, you know, from like 2003, I think the, the first paper I saw referencing this sort of angle modulation, they called it.

**Chris Gammell:** Yeah. So does it mean that there's also like other clocked things that you could target like displays and even like RF front ends and stuff like that? Or.

**Colin O'Flynn:** Well, yeah, exactly. And that's, that's kind of the, the idea is, and after I had worked on this paper, um, someone else totally independently published, you know, basically using the phase modulation, they were measuring over RF, um, the phase modulation, they were showing that has the advantage. Of course, you can, you know, you get longer distances, um, which was a bit of a spinoff of someone else had previously shown that you could do this over just RF. Um, what they actually did is they used a, I think it was a 802 15 four chip. Um, but the idea is right. As you, that chip is transmitting, you have it, it's running crypto at the same time. And like this ends up modulating onto the RF carrier. Oh, that was pretty wild. You know, it's, it's like kind of one, I think most of them are one die. Right. And so it's, you're going to vary. And even if not.

**Chris Gammell:** It depends on the chip. Like, I think the TI one is, has a dual radio, like two, two, like, like chiplets or something like that. Okay. But I think the Nordic one is, is yeah. Like single die. Like the chiplets.

**Colin O'Flynn:** I think there's enough coupling was the thing because like, you know, most of the radios are designed to say, you know, all they care about is do I meet, am I going to meet EM requirements?

**Chris Gammell:** Right. Right. Right.

**Colin O'Flynn:** Right. So like if they see a little bit of spread because of CPU noise, they're going to say, yeah, it's fine. Yeah. I don't care about that. But yeah, someone comes along to attack it and they say, oh, well that, you know, that phase spread is actually related to data being processed on the CPU at the same time. And yeah, which someone showed that quite a while ago. And there's been, as I said, some follow on on that. And then this kind of phase modulation over RF was proving that as well.

**Chris Gammell:** Yeah. It sounds like you get to buy some fun toys then that also, I guess it's, you mentioned some of it's simple toys, but I mean, when it starts getting into the RF space, I imagine that starts moving, moving you up the, the purchase list of all the fancy RF measurement equipment. Yeah.

**Colin O'Flynn:** I'm lucky there though. I, you know, actually I sort of co-located with a professor at Dalhousie that does Hans RF, right? So he has like a 40 gigahertz spectrum analyzer. He's got the good stuff. Yeah. Yeah, exactly. Right. Like anechoic chamber. So, so I like half of the, half of what I'm doing is trying to think, okay, well we have access to this, like, let's make sure we use it for, for doing this stuff. So this works wasn't, but yeah, exactly. I really want to, that's like the next stuff I want to look at is a little more on EM, like, you know, long, medium, long range, which I think is super interesting.

**Chris Gammell:** Yeah. I mean, it's really, it's interesting, you know, looking at your, the stuff you've been doing. I feel like I keep coming across it in my work where I'm like, oh, this is what Colin was talking about. Like, as I get more into the space and just, you know, think more things that need to be encrypted, more, you know, putting secure elements onto things, all the trust zone stuff, like things that I know that you've, you've played with, you've, you've tested and stuff in the past. And it's like, oh, this is, this is why it's here. So it's good to have, just to also contextualize for people that are like listening to like, well, why do I care about security? It's like, well, maybe you don't right now, but at some point you might, you know, like yeah, it's going to come. That's the thing. I mean, broad strokes across the industry, are things steady state? Are they improving? Are they, you know, like, are we seeing more focus on this? Less focus doesn't really matter. I don't know. I don't know like where, where the state of the hardware security industry is.

**Colin O'Flynn:** Yeah. I mean, there's definitely more focus on, especially, you know, the, the thing I find interesting is when I sort of started this, I don't know, like public chips that talked about side channel fault injection resistance were super low. So, um, you know, there is one or two vaguely mentioning a bit now, like the, the, the Raspberry Pi, that new device, the 2350. Oh, 2350.

**Chris Gammell:** Yeah. Yeah.

**Colin O'Flynn:** Like that. A, they went really far out of their way to add a bunch of more fault injection, but countermeasures and, and even just tools that, you know, you can use as a developer. Um, they do.

**Chris Gammell:** When they were on the show too, they were also promoting how they ran the contests and they were promoting, you know, trying to get people to test it and push the limits of it. Like that, that security focus was definitely a thing they wanted to talk about. Right.

**Colin O'Flynn:** Yeah. And that would be like, um, was unheard of. I mean, they, and they really pushed it harder than anyone did. Um, but you know, there's a few others. So like we've been involved a bit with the open Titan project, which was an open source route of trust, um, that Google was heavily involved with, um, and is basically going to be using that as part of their, um, some shipping hardware. So there's some, you know, blog posts or PR where they talk about where they're going to end up shipping it. Um, but yeah, so like there's, there's been a big push, right. For not just security, but like actually having more transparent security, I think is the, the thing that is more helpful for everyone. Yeah.

**Chris Gammell:** Yeah. So you like, traditionally it was like, well, no one's going to find out about this. Cause like, how would they possibly get information? And now it's like, I ask a GPT to give me all the information. It's like, here you go, sir. Yeah. Yeah. Yeah. No, very true. Right. And like, yeah. Can you remind me or can remind me and the audience about like root of trust? I remember Laura from, uh, Laura Abbott was on the show. She's at that server company that I always forget the name of. They were also working. Yeah. Yeah. Okay. Yep.

**Colin O'Flynn:** I was like, that seems like the only cool server company.

**Chris Gammell:** I don't know who else you have pretty much, uh, them and impair impair. Okay. Yeah. Okay. I take it back. I'm sorry. I'm fair. Yeah. Yeah. Those, those two together though. Yeah. Those, those, and then like what Dell. So cool. Dude, you're getting a Dell.

**Colin O'Flynn:** I'm sure they're doing cool stuff right there.

**Chris Gammell:** I'm sure they are, but it's just like, you know, they're stalwart in the industry. It doesn't have the, uh, it doesn't have the same right.

**Colin O'Flynn:** Cool.

**Chris Gammell:** I mean, Dell might have a podcast, but is it, is it as good? I don't know.

**Colin O'Flynn:** You know, you just wait. Mm-hmm.

**Chris Gammell:** Um, yeah. So could you remind people what, so like how the root of trust stuff fits in as well? Cause that's like a, that's like a security element that's on the server board. Is that right?

**Colin O'Flynn:** Yeah. So it can be on anything. I mean, the idea of the root of trust is this is what's booting your system. Right. So, um, the normal use case for it, and I'm, I'm going to kind of generalize cause someone's going to definitely be like, that's not actually true. Um, I don't actually know all the industry definitions. Don't worry. Colin's just explaining it for me.

**Chris Gammell:** I'm a dummy. Just we'll, you know, Henry. I have to have that.

**Colin O'Flynn:** See, this is, this is one of the downsides. You know, I don't know if it's feels like you're complaining as a hipster now, but now that there's more people involved before you could totally get away with like, it was totally

**Chris Gammell:** cool before. Yeah. Yeah.

**Colin O'Flynn:** Being like more vague or being, you know, being a bit wrong cause no one knew, but now lots of people know. Anyway, but yeah. So the root of trust, the idea is this is booting your system. So you have an untrusted system. How do you boot it up? And so the idea is you have this one super secure device. That's like checking every stage of the firmware. Um, so devices will have this internally, right? So some devices will say, you know, they have the first stage bootloader is in ROM and normally can never be changed. Right. And then that boots some external bootloader that boots the next one. So it's like bootstrapping your whole system securely. Um, it normally also can then handle stuff in the future. Like if you need to sign something or you're getting a firmware update, right? The root of trust is going to manage that and make sure you don't, you know, get a bad firmware update or malicious really, not just bad.

**Chris Gammell:** Right. So is it like the idea is me as a user, I log into a server built by Google, whatever, multiple layers of software on top of it, whatever. And I'm trying to say, how do I know this is actually the server it is? And I could dive, keep diving down, down, down, down, down. And then at some point this is the chip that says it. Is that kind of the idea?

**Colin O'Flynn:** Exactly. Yes. This is your like total, right. This is your root of trust. This is how you trust everything. And like the idea of open Titan was they had kind of said, you know, well, look, how do you trust the root of trust? Right. Right.

**Chris Gammell:** Who says that? Who watches the watchman?

**Colin O'Flynn:** Exactly. And like, and you know, this was also around like the Snowden time. I think they were starting this project. So it was a real question. Like, you know, what if the government forces Google to tamper with your server? You know, they, they, Google wants you to believe that they have no tampering. So, so they kind of said like, well, if it's an open source chip, then you can in theory do, you know, attestation that the design is what's running. There's some tricky bits in there, but the general idea, right. It gets you all the way up. But I mean, and people use them like for little, you know, Chromebooks, phones have these like got it. Yeah.

**Chris Gammell:** Kind of everything will use this. And so it's just there to, I mean, it's got all this stuff to prove itself. I'm looking at a data sheet, which Colin also is seeing my screen. So at least we can have a shared context here, but it has a lot of stuff in it that I don't know why it would need it. But I guess, I mean, random number generator. Okay. Key manager. Sure. Like power monitoring. Like it's, it's just able to like look internally and say, everything's cool boss. That's kind of the idea.

**Colin O'Flynn:** Right. So the thing is the, um, and you know, you have to remember too, they're pretty somewhat generic, but, um, they're often booting stuff. So like they might need to read from an external spy and validate it. And then, you know, they can emulate that spy to a system, um, so that someone doesn't do like a attack where they switch, right. What the spy image is there's the classic sort of attack where the, the system looks right. That it validates some firmware image and says, okay, that firmware image looks good. Um, so that's when it does the time of check. And then when it goes to use it, it like reloads the spy flash. Cause it doesn't have everything in memory. It didn't have enough space in memory. Um, and the attacker switches it at that moment in time. I see.

**Chris Gammell:** Right. It's like the side of hand, but with memory.

**Colin O'Flynn:** Exactly. It's like, that's like, that was a common. I mean, it's less, more people are doing validation for the whole thing. Yeah. Avoiding that, but it's still an issue. So, so if you have a root of trust, right, it's actually forcing that. Like, there's just no, there's nowhere to switch it because if you switch it, the root of trust is going to see that or not even possibly not even read it. It might just cash everything.

**Chris Gammell:** I guess, I mean, Laura was on the show and prior to that, I think it maybe heard it one or two times, but I just didn't really understand it. I think the only thing I had heard about it under was the, um, when there was like that scare about there being a chip on one of the servers. And then I remember Joe Fitz made that, that tiny sticker with like the little pencil tip. I want to believe or whatever. I don't remember what it was. It was like, it was like someone had apparently found a malicious chip on a server PCB. Right. Yeah.

**Colin O'Flynn:** Which, and I don't even know. And I think the chip that you use, like unvalidated, right.

**Chris Gammell:** It was like, it was like a lot of fear mongering and that sort of thing. Yeah.

**Colin O'Flynn:** Well, and I remember the big thing was the chip they used in the photo was, uh, the, I think it was just like a ball in or something. Right. It was like an art, it was like totally. And I don't know if that's what they were saying was delicious or they were just like, here's a cool looking chip. Let's put that on the tip. Yeah. Right. Right.

**Chris Gammell:** Right. You never know with us. To a journalist, it's just a black of black blob on a board sort of thing. Yeah. Yeah. Exactly. Yeah. Yeah. Um, but yeah. Okay. How did we get here talking about the, the open Titan and the state of the industry, state

**Colin O'Flynn:** of the industry, industry is looking better, I think is the summary.

**Chris Gammell:** Okay. So there's just more focus on it. It sounds like, and it's like, there's more, uh, people more focused.

**Colin O'Flynn:** And I think personally, right. Like, I think a lot of people don't think the open solution is good. Um, yeah, which I think is nice. Like, as I said, the Reservoir Pi scene, what they did is really cool. Um, you know, seeing stuff like open Titan and, and they're sort of different levels, but it's, it's not just that there's, you know, venture capitalists saying, let's make another proprietary solution or AI does X, Y, Z, right. That's like, here's an actual thing that could actually help people seems reasonably secure.

**Chris Gammell:** You know, one thing that you always kind of bring up is like these attack vectors and like, uh, how people think about it, but how should people listening, think about it for their own products as well of like, Oh, this is what someone is likely to do. And then I guess what some, something I always think about is like, Oh, well they, they need to have physical access sometimes, but not always, you know? So like the likelihood of certain things, is there like a good guideline for that sort of thing? So if I'm designing a product, what do I, what do I have to care about? Because there's no like test other than like maybe hiring a security firm because there's just general guidelines.

**Colin O'Flynn:** Yeah. And there is, and to be honest, and this is where I'm bad again, this is where people listening will know and correct me, uh, because there is some more recent industry guidelines that I've seen released. I haven't even read them yet.

**Chris Gammell:** Oh yeah.

**Colin O'Flynn:** Um, but you know, to, to go back to an older one, like arm had their, um, PSA platform security architecture, right. Um, which was a level and they basically had several levels of, um, if you want to get your device secure, here's like what you can do. So the highest level involved actual side channel and fault injection testing. Um, I liked this one cause the lower levels were just kind of, um, checklist. Like, so you could do it yourself. I don't, you might have to pay money to get an actual PSA. I don't actually know what the system is for commercial, but, um, they did have a bunch of stuff you could download that would say, Hey, and you know, and it would be reasonable things. I liked it because they're big. Okay. Is the J take port locked unlocked, right? Like things that people actually mess up all the time. Right. Totally. So, so you could get like a different, and they had some, a few example threat models, um, where it's like, okay, here's if you're making a smart meter, I think was one.

**Chris Gammell:** And yeah, I'm looking at this page right now. It says smart meter asset tracker network camera. Yeah. TM, TMSAs, right? Yeah.

**Colin O'Flynn:** Threat model security analysis documents, I think. So, so that's kind of showing you, okay, if you have this doc here, you know, and it goes over like, okay, well, would people have physical access to it or not?

**Chris Gammell:** Or, um, stuff like that. So. Not lost on me that I'm downloading a binary, uh, from, uh, a thing about like threat models. Yeah. Excel file on your, on your computer. No big deal. Macro enabled. Of course. Why would it happen? Right. Right. Yeah. And then that's how I got hacked by VBA. Yeah. Yeah. Yeah. I mean, yeah, they definitely give you some, some stuff here and I'm sure they would definitely take your money if you wanted to, uh, pay them to certify it. Right.

**Colin O'Flynn:** Yeah. But, but, but I mean, and there is, as I said, there's, I've seen some other, like there is some, uh, I think the UK government just released a kind of IOT smart device, um, guidelines as well. Um, there's been a few kind of like that and they, they're pretty, again, like I think the, the cool thing we're seeing is that things are, are reasonable. I want to say, right. Yeah. They're, they're looking at real threats.

**Chris Gammell:** I know there's some like, uh, upcoming regulations in the CRA, I think is the one in the EU. Um, that's like a requirement for like being able to OTA stuff. And then there's trust mark or something like that in the U S but which is less of a, there's like some kind of marking as well. But I don't know. Whenever they think about these things too, they're always like, Oh, you're running like a Linux box and you left SSH open. And like, yeah. Yeah.

**Colin O'Flynn:** Which is why the RPSA one I like, because it's, again, this is more like embedded, right? That's their whole thing. So I think that's, it is. If you're doing embedded, like it's a good, you know, as I said, at least at one or level one or two, it's like a checklist you can do. I think you can even just certify without paying from, you know, my information is years old, not checked back check whatsoever, but well, this is the empire.

**Chris Gammell:** So you don't have to worry about fact. Perfect. I like it. Not another thing we do here. Don't worry about us. Uh, I don't know. I did work. I did have a consulting thing back in my day of like, that was, I had somewhat, the third party come in and like do like an audit, but like all the things they were doing, there was just like, Oh, are you not like a, like a raspberry pie? No. Okay. Then we don't know what to do with you. Okay. Then that's, that's less useful. You know, like, I, like, I, I think the thing is like, as like a product designer, it's like, I want to know the best practices. So things like this are good. I feel like. So what about the embedded side of things? I mean, like, are you focusing mostly, mostly in the embedded space and lower? I mean, like, are you doing, doing that kind of stuff these days?

**Colin O'Flynn:** Yeah. That's, um, you know, I mean, my, my own background is less like Linux high level. Um, so most of the stuff is, you know, lower level, bare metal embedded looking at that. Um, yeah, yeah. A little architecture stuff. So, I mean, one newer thing I've worked on is, um, and I haven't worked on it so much. I worked on board designs and have been involved in it. So I feel like when I say worked on, I don't want to have any credit. Is this, um, chariot system? Um, and in particular, so design this board Sonata, which low risk, um, new age parent company, uh, had a project where they made this open source. Um, in fact, the idea is to have like an open source microcontroller kind of soft core device, right? That just feels like a microcontroller, but it's running something called cherry and cherry for IOT, which does all this compartmentalization. Um, so it, you know, rather than just saying, are you in like, if people are familiar with cortex M 33 and these devices, they have like a secure and a non-secure mode and, you know, different peripherals, you can say, okay, the spy device can only be accessed by the secure code. Um, and so cherry, it's kind of cool because you define compartments and you say, okay, the, you know, the spy driver code can access the spy peripheral and that's it.

**Chris Gammell:** Huh? Okay.

**Colin O'Flynn:** You are. And so it's like at a much more fine grain level. So it's kind of cool because you can say like, okay, the web server process can only access these certain things and like this API, stuff like that. Right. So if someone hacks it, it's just like, there's just no, you know, there's no way to read other memory. Yeah. Right. And that was the problem. You know, what I see with cortex M 33 or any of these where it's just secure or non-secure, you know, as a time crunched embedded developer, what do you end up doing? You put too much in secure because you're like, you know, I need access to everything.

**Chris Gammell:** Okay. Secure code. There's no one really enforcing it. Right. It's just like, you're only really size limited based on how it's laid out. I think. No. Yeah.

**Colin O'Flynn:** I don't think there's really like there it's up to you to decide what's secure and what's non-secure. Right. So you're supposed to go through and make sure the secure code is only the finest quality

**Chris Gammell:** code that has no problems ever. There's that's how I get around it by never, ever having fine quality code for my stuff. Yeah, exactly. Perfect. Yeah. Or just do open source. Doesn't matter. Yeah. Right. Yeah. Someone will check it at some point on GitHub. I'm sure. All right. So this board looks like it's had a 40 pin header. It's got a display.

**Colin O'Flynn:** Yeah. So it kind of, it's smushed together. You can fit a Raspberry Pi. I don't know if there's a photo of it with all of them on. A Raspberry Pi hat, an Arduino shield and micro click. Oh, and PMOD. So not simultaneously. Yeah. Quick as well. Yeah. Yeah. Two quick ports. So it was like, okay. Put all the things on there. All the things. All of it. Because what happened is like, we're looking at different sensors, right? People might want to use. And it's like, ah, well, there's a really nice Arduino shield that does whatever it was, you know, can or something.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** That's like, oh, but there's a really nice Raspberry Pi hat that has all the RGB LEDs. Right.

**Colin O'Flynn:** Right.

**Colin O'Flynn:** So yeah, you can make them kind of work. Like it's a little bit funky, the headers, but.

**Chris Gammell:** Yeah. You know, like the really tall headers or something. Yeah, exactly.

**Colin O'Flynn:** Like the, you'll see the hat has like super high headers and the Arduino is really low headers.

**Chris Gammell:** So yeah. Yeah.

**Colin O'Flynn:** It'll fit over mostly, but yeah.

**Chris Gammell:** So then it's got a FPGA. It's got an Arctic seven on there. It looks like, and that's where it's running the actual like Verilog. That is the Sonata, not Sonata, the Cherry, Cherry. Yeah. So while the Sonata core basically. So I guess Cherry is the RTOS and then the.

**Colin O'Flynn:** So Cherry is the. Ah, yeah, it gets worse. So Ibex is the core. Ibex is this risk risk five core that low risk developed. So it's using a few things. It's used in open Titan as well. So Cherry is the extensions that give you the memory. I want to say memory safety, but compartmentalization, all the other features. Um, so yeah, so it runs kind of a, I mean, the idea of the board is that you, you can ignore the fact that it's an FPGA. So there's a, you know, prebuilt microcontroller that has an RTOS. And if you really want, you can go and change it. But, you know, I think what, what I've sort of seen is that, especially with students and then engineers that just want to develop something that's like step one, install 20 gigs of Havato. Nobody likes that.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** Yeah. Right. So it's like step one, download a bit stream and just drag that on and you're done.

**Chris Gammell:** Right. And now, now you presto change. Oh, you are a microcontroller of sorts. Um, exactly. Right.

**Colin O'Flynn:** And you've got an RTOS and it's already got the HAL that has all the things set up for

**Chris Gammell:** the bit stream. I have been really pleasantly surprised when like, I, I personally, like the way I operate with microcontrollers these days, I couldn't tell the difference between a risk five and a, you know, arm core. If I, aside from like, maybe if I'm looking in and seeing what, you know, build systems being called, like those usually have a different, like risk five, risk V or, you know, the, the arm, whatever, but like, otherwise I'm like, okay, tools are there. I don't have to care, you know?

**Colin O'Flynn:** Yeah, no, sure. I mean, I, I recently started using some of the ESP 32 C six, I think. Yeah. Um, yeah. Yeah. It just kind of magically works. Like I would never know. I wouldn't have even known great. What right. The core was.

**Chris Gammell:** So that's great. That's what I want. I want to, I want it to work. Right. I want it to be open for other people to develop on top of it so that I can get other, you know, fun things in the future. But like, yeah, I'm not building anything else. It's a custom like that. So, so like this Ibex score, it's just like one, it's an off the shelf effectively from low risk.

**Colin O'Flynn:** Yeah, exactly. So that was an open source core that, um, I think, where did it spin out of, uh, Zurich research center. See, now I'm forgetting. This is where I should have fact checked anything. Um, it's fine. Do it in post. Do it in post. Um, yeah, yeah.

**Chris Gammell:** They in fact did not do it in post.

**Colin O'Flynn:** But yeah, so the, the, so this core is, um, was run by them for a bunch of stuff. And then there's a version of it that adds the chariot stuff on, um, to it. So, but yeah, I mean, it's basically like a risk five core that's been used. I think it's been used in a number of like tape outs and other things. So it's a pretty, yeah.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** Well tested.

**Chris Gammell:** So then who, who, so like students are using this to, to try out that compartmentalization, like try and kind of break it open or what's the, what's the thought of like, what's the reason for this overall board? Yeah.

**Colin O'Flynn:** I mean, really it was just to, to get people, um, yeah. Get people being able to use the core. So the original idea was students, right. If you had, um, an undergrad class, which is why it sort of had this Arduino, right. All these shield embedded engineers, I think would be like, ah, whatever. I don't care about that.

**Chris Gammell:** Yeah. I use them all the time, man. Yeah. Yeah.

**Colin O'Flynn:** So that's the thing.

**Chris Gammell:** It's what you can buy. So like, that's really the, you know, whatever it's quick.

**Colin O'Flynn:** So yeah. But that was the idea. It's like partially students. So get it academic. Um, you know, the hope was to have lower costs. The FPGAs get expensive, unfortunately. So yeah, especially at lower volumes, like it's, you know, we're not, well, at least you can get them these days aside from the, yeah, that is an amazing thing. Like, uh, you know, we could just get them under a reasonable 14 weekly times or sometimes if they're in stock. Oh, thank you. Stuff like that. One plus a year. Hope you have enough. And I think it's like, I think our last quotes are now cancelable or changeable again. It used to be worth committing like non-cancelable. NCNR. Yeah. Yeah. Like 52 plus weekly times. How many FPS do you need?

**Chris Gammell:** You will, you will pay us up front and you will like it and we may deliver them to you someday.

**Colin O'Flynn:** Right. Yeah. That was the best part. So yeah. So it is a lot easier. That's pretty, pretty nice. Yeah.

**Chris Gammell:** That's great.

**Colin O'Flynn:** Okay. Are you involved in much hardware, like, uh, production these days where you're seeing that side of it or?

**Chris Gammell:** Uh, no, no, not enough volume that to matter. Um, obviously we have other things going on with hardware production down in these. United States that you don't have to deal with, which is nice. Yeah. We kind of have to, but yeah, right. Of course. Like we, uh, you're still coming from DigiKey, huh?

**Colin O'Flynn:** Yeah. And I think, uh, well, we use most as a distributor. So, but they've been, I mean, they're really both. Like everyone's good to deal with or doing what they can with what they've got. So, yeah, totally. Um, and so far, and I'm going to jinx myself by saying it on a podcast. Yes, you totally are. You don't have to finish the sentence. You're already jinxed. Just so you know. Already jinxed. It's already done. Right. Is that, um, the, for some reason this whole time, the like, um, customer right. Made in Canada has been exempt. Oh, because we make everything here or add enough value or whatever it is. Right. We've always ended up, we've never gone the full outsourcing route, which. Oh, yeah. Should have originally, but it's saved us because suddenly we're not. Right.

**Chris Gammell:** We're actually. Yeah. Past Colin being intransigent and just wanted to build with a fun pick and place. Yeah, exactly. They saved your modern day ass, you know?

**Colin O'Flynn:** Yeah. A hundred percent. Cause we were totally like, you know, and the issue was that we were going to have to, they had limited space that was bonded that, you know, they wouldn't have to charge the tarot zone, even if we're shipping to Europe. So everyone was going to have to pay because they had to pay on import. Um, oh, wow.

**Chris Gammell:** So like it's, it flows through a Mauser warehouse, but it doesn't get tacked on because the end destination is Canada. Is that, is that kind of the short, short form of that?

**Colin O'Flynn:** No, no. It's like in our case, because our stuff came from Canada, stuff came from Canada, like because we were source made in Canada, it was exempt under like we're exempt under, you know, the old new NAFTA customer. Oh, okay. Yeah. System because that's always been exempt forever until a little while ago.

**Chris Gammell:** Um, but because of automotive. Sorry. Is that as a seller then? Is that what you're saying? Is that why it's exempt or? Yeah. As a seller. As a seller. I see. As a seller. Okay. Got it. Got it. Got it. Okay. So yeah.

**Colin O'Flynn:** So we kind of lucked out there a little, so we'll see. I'm always worried that's going to change and, uh, we'll see.

**Chris Gammell:** But you don't just because you, but just, just to close the loop on it, because you are building in Canada when parts flow from like a Malaysian packaging facility through Texas at Mauser to you or, you know, but like originally from, you know, a Chinese fab or something like that, for instance, do you get any, is there any tariffs in that, in that loop or no?

**Colin O'Flynn:** There can be. So that's the issue.

**Chris Gammell:** Is that, okay.

**Colin O'Flynn:** They have some space and I don't know if they've, you know, the problem is everything changed. So like no one wants to make drastic changes and then the tariff will change.

**Chris Gammell:** But, well, I'm sure, I'm sure Mauser has been real estate shopping in Canada as well. Right. Of like some, or some offloaded site. So that, yeah.

**Colin O'Flynn:** Well, that's, I mean, so what they had is they did have bonded areas. Right. So it's like, you didn't, you don't pay tariff because it's in the special bonded zone.

**Chris Gammell:** Right. Right. Like where it's only on the final, the final delivery. Exactly. Right.

**Colin O'Flynn:** So, so, but it was a physical, as far as I understood when we were talking to them, it's like a physical zone. It's like this area of the warehouses, you know, chained off because I think, you know, the bonding is a generic like customs thing. It's not specific to any tariff stuff.

**Chris Gammell:** Right. Right. I'm just imagining like there's like a metal detector looking thing and the person walks in, but it has like a little like American flag and their shirt.

**Colin O'Flynn:** And then like alarms are going not allowed.

**Colin O'Flynn:** Serifed. But yeah. So yeah. So we, so anyway, I think like if you had some parts would, some parts wouldn't, it would depend if, you know, they could get them in that zone where they didn't have to apply input tariffs as they came in. But some, and like, the thing is what we're seeing is, you know, like boxes and just random stuff too, as terrorists that. Oh, I see. Yeah. It's like the supplier gets boxes from the U S because our new line, because everyone does. Um, yeah. And like there's counter tariffs and like, even I was talking to a metal supplier and they were saying that, you know, Oh, there was a West, a lot of shipping would go through the U S because the rail lines were better.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** Right. Right. Right. That was their entire distribution chain was it crosses Canada, U S U S Canada.

**Chris Gammell:** Well, in case I've made my feelings not known on this, this is all stupid. This is so, so stupid. Uh, and I will continue to say as much, but, uh, sorry, you're dealing with that. That sucks. Uh, and I'm glad at least on the selling side, it's less bad. Right.

**Colin O'Flynn:** Yeah. I mean, I feel bad. The, and the, the kind of crazy thing. And again, I'm going to like totally jinx myself spilling the beans on this is that because of that customer stuff, I mean, are the tariffs paused or no, are they back on now? What's the like Chinese tariffs?

**Chris Gammell:** I literally can't pay attention. I mean, I I'm very blessed that I don't have to like think about it right now, but I, if I pay attention, I just get angry and like, and starts muttering stupid, stupid, stupid over again. So, yeah.

**Colin O'Flynn:** Yeah. So the amazing thing was that you actually, what people should do if they wanted to avoid tariffs under the current system is that you should build your stuff in Canada or Mexico because you'll import from China, right? No tariffs to either of those places. Yep. You do enough transformation in Canada or Mexico that it becomes Canadian or Mexican

**Chris Gammell:** origin product. Right.

**Colin O'Flynn:** And then it's exempt under the current customer rule.

**Chris Gammell:** So, um, right. Which seems counter of kind of, yeah, I talked about on the show a couple, uh, whenever Dave and I recorded last, like my instinct in all this too, is that like, okay, just assuming there's tariffs, I'm going to go with the cheapest stuff I can get. And guess where I get it from China. It's like, I'm going to get like, you know, the H32 VW three parts or equivalent, and then just like develop on that and do, you know, like put all my brain power into the terrible firmware. I write, but like, but deal with it and just pay the tariff on top of it. And, uh, yeah, it's, it's very counter, like, it's just like unintended consequences abound. That's, that's what it really comes down to. Yeah. Wow. I mean, sure. Stop market bounces were intended, right?

**Colin O'Flynn:** That's another discussion. Right.

**Chris Gammell:** Right. Yeah. Yeah. I, as I said last time too, yeah, I just feel bad for friends at DigiKey and Mauser and people that have to deal with all the paperwork. Yeah. Yeah.

**Colin O'Flynn:** Yeah. That's the thing. I mean, when we were talking to America, they were like amazing credit to them because they were, you know, basically just like do whatever you need to do to get it. We just got to keep things moving.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** I mean, like, you know, we were kind of worried because the agreements you have with, um, you know, we can't say specifically, but you normally have like, okay, if we have price changes, we have to give them notice. Right. Because I changed the price by the way. Um, but they were just like, if you need to change it, change it, we'll deal with it. We'll figure it out. You know, no, everyone's kind of in this together was the feel, which was at least nice.

**Chris Gammell:** Yeah. Well, let's talk, let's switch to talking about actually making stuff on site. So you're, I think the last time you were on, you were kind of started the experiment, but I don't know how much you had scaled it up, but like you've continued to make stuff locally in Canada. Uh, you have some pick and place capabilities at your facility. Right. So how's that all been going? I mean, aside from the, the modern, the modern, uh, uh, luck that has been bestowed upon you because of it.

**Colin O'Flynn:** Yeah. I mean, that, that was not intended luck. Um, uh, pretty good.

**Chris Gammell:** I mean, so this is, that's why they call it luck, Colin. That's why they call it luck.

**Colin O'Flynn:** Um, yeah, so we, I mean, we do a bit, so we use, um, some outsourcing for PCBs, especially because you know, that tends to be more efficient, but for a lot of smaller items. And we still have the thing where we have all these target boards that have different chips mounted. Right. So it can be difficult to know. Um, we did recently upgrade. So we're using some like small desktop pick and places and then got a, um, uh, slightly larger, like floor pick and place still pretty small. Um, what was it? Okay. I need to look up what it was. What are we on the brand?

**Chris Gammell:** Not a, not a Neoden. Are you still running? I remember you had done like some open PNP experiments. Yeah.

**Colin O'Flynn:** Uh, I use that a little bit. I was using the charm high ones. Um, no, it's a Neoden. Yeah. Cause Neoden, we had bought it from the U S. Um, I think it's the Neoden nine was the one.

**Chris Gammell:** Okay. Yeah.

**Colin O'Flynn:** Yeah. Okay. That's it. So, so it's a moderately, it has feeders and stuff like that. So it's a, uh, yeah, it's pretty good. I mean, it's kind of what we need. You know, we're not doing right.

**Chris Gammell:** You're like high mix, high mix, like fast. I remember like you've saying like, Oh, well we need to be able to kind of turn on a dime, especially shortage times. I think you would maybe had talked about that a little bit, but.

**Colin O'Flynn:** Yeah. Yeah. And that, that's exactly it. And this is kind of like when people are talking about the setup, right? It's a bit tricky because I think purely if you were to just look at what's the cost of building it, like, yeah, you shouldn't build yourself, but, um, you know, many times, especially with shortages, but even outside of that, right. Having the capabilities in house has saved us, um, for me, just being able to rework stuff right on the fly, because we have, you know, someone in house that can really do that. Um, yeah.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** Which if you're outsourcing, there's no way you could afford to have someone idle hoping they need to rework a PCB.

**Chris Gammell:** Right. That's the only happens when you like really shout at them, like you got this wrong and I have the documentation to prove it. And I won't send boards to you anymore.

**Colin O'Flynn:** Yeah. Which like those. Yeah. Yeah. And I don't know what your experience is. And I, I, this is like, I don't know if you can do polls in this. This is a very low commitment. I'm sorry. I should have researched more, but you know, we've tried to do fast turn and like it has failed almost every time I've outsourced a fast turn to, and like, I'm multiple different companies.

**Chris Gammell:** Like, yeah. You know, what style of, uh, like what's, what's the fast turn, I guess, in your mind?

**Colin O'Flynn:** Uh, well, I mean like, so twice now and a few different companies, um, I've tried to get this, we were doing this, like it was pretty high spec board, right? It was like four, four mil trace space BGA and paid for like, you know, three or four day turn and I forget, you know, uh, maybe $10,000. Like it was a, yeah, that sounds right.

**Chris Gammell:** Extremely expensive, right?

**Colin O'Flynn:** Like, yeah.

**Chris Gammell:** But I mean, that could get a lot more expensive than that though. Yeah. Yeah. But for me, right.

**Colin O'Flynn:** You want to do some JLPT, um, but, but it took four weeks instead.

**Chris Gammell:** Oh, really? Yeah. And it just kept, what was the failure mode? Was it files? Was it orders? Was it, I don't know.

**Colin O'Flynn:** They never told me it would go to inspection. And then I was like, I don't know. I don't, cause the thing is when I ordered that at the same time, I ordered a JLPT board just cause I'm like, I'm going to, you know, keep a few insurance policy.

**Chris Gammell:** Yeah. Yeah.

**Colin O'Flynn:** Well, and I thought it was like, well, the fast train one's going to come, we're going to test it and then we'll have more JLPT ones to build up. Um, right. Just cause like then, but we, we kind of needed the quick or ideally wanted the quick early test. Um, yeah. So, but the JLPT ones came in and use that and I just kind of, we just didn't pay or disputed

**Chris Gammell:** the one, the four weeks versus four days. That's pretty bad. That's pretty bad. Yeah. Yeah. Yeah.

**Colin O'Flynn:** It was just crazy.

**Chris Gammell:** And like, and it's like, you know, that was one of the worst ones, but pretty extreme have. How far away were they? Could you have gone to like shout at them in person? I mean, like, I feel like they're in the U S right.

**Colin O'Flynn:** This is all, I don't think Canada had the spec we needed. So it was like, ah, uh, I don't know if I should stay because there's not that many. No, that's fine. We don't have to name a shame here this time, but maybe if it happens again, how about five

**Chris Gammell:** years? If you've tried it again?

**Colin O'Flynn:** Yeah. I feel like they, I don't know, you know, at the end it was fine. There was no charges. So things happen. Right. Like, I mean, that's the problem. It's like, was it a, you know, someone they hired that didn't work out? Was it, you know, shipping error? There was a shipping error on top of one of those.

**Chris Gammell:** Yeah. Yeah.

**Colin O'Flynn:** Right.

**Chris Gammell:** So it's like, like we balk at the, the cost of, you know, 10 K whatever, but like, what a terrible business to be in. Like, it's just, it sucks. You know, manufacturing is tough. If you control every aspect that you can and it still sucks. And it's like, then if you're doing it for other people and there's, you know, like things happen, right. Like you said. So.

**Colin O'Flynn:** Yeah. Yeah. And totally. And that's like, you know, another thing recently we did, um, where getting some metal parts fabbed and like first batch was awesome. And the second batch was just shipping or an, and it was a bit of a rush thing too. Right.

**Chris Gammell:** And it's like, yeah, yeah.

**Colin O'Flynn:** It's a shipping thing. Like, you know, that can happen. Packages disappear. Things get smashed.

**Chris Gammell:** Yep. Yep.

**Colin O'Flynn:** I'm like, yeah, I am.

**Chris Gammell:** I'm currently on day six of waiting for a two day delivery from DigiKey. Yeah. It's not DigiKey. It's UPS's fault. It's not DigiKey's fault. Yeah. It's just like, okay, well, what am I going to do? It's like, it's in the ether until it shows up on my doorstep. And I was like, oh, I guess I could pretend I could talk to someone at UPS. Like, no. Yeah. Somewhere in rural North Carolina. Okay. Yeah. Yeah. Yeah. Well, so one of the key things that I remember talking about with the onsite manufacturing too, is that like, you kind of were hands on with it at the time and you were like really into it, but maybe you've handed it off for the everyday operations. Are you still doing?

**Colin O'Flynn:** And I forget one exactly. We talked before who was with us, but we had someone now. So we had kind of a, you know, basically doing everything production. Um, so she's running, you know, combination of running stuff, but doing, you know, things need tweaking, actually doing, um, soldering stuff and anything like that as well. So that's been key. Um, again, having that in house and, and with me stepping away though, someone else is taking on a lot more of the day to day, you know, looking at designs, looking at, oh, cool. You know, overview of what's the, what's like, what are the lead times looking like? What's the current status of all? Right.

**Chris Gammell:** Like sourcing and the boards and stuff like that. Yeah.

**Colin O'Flynn:** Yeah. So that's, that's the, the, the dream. I mean, you know, we're still, to be honest, it took a while, like a shockingly long time after all the COVID things for us to like, it was only this year that we've, or maybe end of last year, I'd say we were caught up and like, really running and yeah, back, which, you know, part of that is just because we're pretty small. So sure. There's so many projects that sort of got just, you know, pushed aside because like, well, we're not going to get chips. So that's not a, let's not worry about that.

**Chris Gammell:** Yeah. Yeah. Yeah. And then when you're selling this stuff too, I mean, like you're selling, uh, to a wide variety of folks as well. Right. I mean, like you're selling stuff to other test houses and students and things like that. Right. I mean, you guys have a pretty broad portfolio.

**Colin O'Flynn:** Yeah, exactly. So we're selling, um, and that's always been the goal is, you know, we want to, uh, people, students doing research, um, on the, the other side, we want engineers using this professionally. You know, we want people doing this as part of evaluation security evaluations. Um, so it does range, you know, the goal has always been to have this range of, and it's gone up over time, right? But like a hundred bucks to 10,000 or something like that for products that people could buy

**Chris Gammell:** chip whispers still being made chip shouters still being made. That's, I guess what you were talking. I think last time you were on here was when ship chip shouter, that's the one that's high voltage, right?

**Colin O'Flynn:** Yeah. Oh yeah. Okay. So that was a little while ago. Um, yeah, I guess that's something good. That's yeah. I guess time, time happens. Um, it sure does. And marches on man. Yeah.

**Chris Gammell:** Let's see. When was it in August of 21? So I had, I had, I had a baby in the house. My first baby. Yeah.

**Colin O'Flynn:** And I saw our GSA was on the list. So we're repeating some stuff. People are.

**Chris Gammell:** We are. All right. Yeah. You asked the same question. It's probably a full recap of what it was, but you know what? I was underslept then. I'm underslept now, you know, whatever. Perfect. I could, I could, you know, I could do is just read off the notes from the last time. Shout out to, to good notes, right? Yeah. Good job. That was not me. So that was all you. Yeah. Yeah. Um, yeah. Yeah. Okay. Okay. Uh, one thing that I did want to bring up on, so, you know, you had mentioned some of the parts you're working on. I, I found your old post about Apple air tag teardowns. I was using this as a reference point for the little board I've been building. And, uh, I was wondering if you'd been doing anything with this in the meantime, the air tag and stuff like that.

**Colin O'Flynn:** No, I haven't looked at the air tag. So, I mean, a quasi unrelated, not a security site, but just for my own, you know, interest, product development had been looking a little more back at the Bluetooth tracker system and how that works. But, um, you know, I haven't looked into all of the, yeah, with the more recent trackers or any of them are using.

**Chris Gammell:** I mean, I think this is the main one in the market, right? It's not, there's like, Oh, the new Samsung one just dropped and I'm, I'm standing in line to get it. It's like, no, no, I got a solved problem, but it is a, it is, this is a very commercially available and accepted solution.

**Colin O'Flynn:** I think that is good. I mean, so I'm, I use Android. I don't have an iPhone and I wanted a tracker for some stuff. And like, I bought tile. It's fine. But like, yeah, there's so few people on the network. I was like testing where it's going to be discovered. I'm basically going to have to drive around if I lose it and like hope I lose enough.

**Chris Gammell:** See, this is like, now you can get into drones, get a new thing, you know, have a scanner yourself, whatever. Yeah. Yeah. Network effects are like really powerful. It's like an important thing to have. So, um.

**Colin O'Flynn:** No, totally. So that's, that's a big part of it.

**Chris Gammell:** It's definitely some cool little hardware too.

**Colin O'Flynn:** Yeah. It is amazing. They packed in.

**Chris Gammell:** Yeah. Cool. So what, you had mentioned more expressive stuff as well. So what are you doing with expressive these days? I guess we were, oh, that's the other thing. We were talking about the, the, um, security wise, like the HCI.

**Colin O'Flynn:** Oh yeah. Right. Okay.

**Chris Gammell:** Quote hack that was happening. It wasn't really a hack that was like undocumented HCI. Right.

**Colin O'Flynn:** Yeah, exactly. So, so, I mean, and that was like, you know, and this was, I, I guess, uh, I forget if I meant to bring it up with the cherry chariot. The interesting thing, right. About this is, um, this is a cool example for compartmentalization, right. Even if there wasn't a hack, but it's like, you know, expressive NRF, you have these sort of binary blobs that you're linking in. Um, and so if there's security threats in them and they're going to be a big target, everyone's going to want to find a attack. Yeah. Right. For one of those, those stacks, because then it applies to everything. So.

**Chris Gammell:** Yeah. And when this came out, I remember like all the things were like, this chip isn't, you know, it was for the originally SP 32. And it was like, this chip is in millions of consumer devices. And now they're vulnerable to Bluetooth, you know, over the air attacks. And it's just like, well, maybe.

**Colin O'Flynn:** Yeah.

**Chris Gammell:** Yeah. Exactly. Right. I'm going to get out of like my, my daughter's Tony box. Like, oh no. Which I think that is not the point for security.

**Colin O'Flynn:** I get it. So like, yeah, yeah. Well, and that was the thing, right. So like you compartmentalize it and that would be really good. But I mean, an interesting thing there, right. Is like one of the things when I've talked to people before and I don't have a good solution for this is for security, how many, you know, people want to have very dramatized headlines. And so it's a bit tricky. Like, you know, I was looking at some access control systems a while ago, a few years ago. And some of the stuff I probably will publish it eventually. I never did because I felt bad because it was like, I was looking at one system and it was no better or worse than any other system. Right. But if I publish it, I was guaranteed just knowing the industry that, you know, the other vendors would use that to be like, oh, look, we're so good because these other people got, you know, had this. But it's like, no, you know, that wasn't the point. The point was, was that so.

**Chris Gammell:** See what you got to do is start a TikTok channel and then publish your work and then get sponsored by the other ones and be like, Colin approves door locks. 44. Click. I don't know. Yeah. This is the one that the best. Yeah. When you say security system, like that's like, like door locks and things like it or, or, or something more.

**Colin O'Flynn:** Yeah. More like access control, you know, like the card we're installing. I was installing one of their building actually. Yeah. Card reader stuff. So, you know, they use lots of it. And, you know, generally I think most people know the, well, the older ones had no security, but a lot of them would have keys in the readers and stuff like that. That are really. Wow. Yeah. Yeah. Right. And it's like kind of for the threat model. It's not amazing. It's better than the old ones. You know, I think newer ones now have secure elements. So also at the time the company was coming out with a newer reader that had a secure element that basically would solve the problem. But it got delayed because this was over COVID time. So again, I kind of felt bad because it was like, you know, they, they were trying to solve it, but I think it came out finally. So I, I kind of, you know, lost interest.

**Chris Gammell:** So I, what I'm hearing here, Colin, is you've lost your killer instinct is the black hacker that we all think you are, you know, now you're just like a teddy bear. Basically. Yeah. Age, you know, like soup is the thing.

**Colin O'Flynn:** I like soup, you know, hang out.

**Chris Gammell:** Yeah.

**Colin O'Flynn:** Yeah. I mean, I am. The one thing I've worked on, so my other COVID project too, was I started writing down a lot of this, like, you know, production, basically trying to write a book on production, small scale production.

**Chris Gammell:** Yeah. We mentioned that before the show. Yeah. We were texting about that and I totally forgot about it. So good. I'm glad you brought that up. Well, it's all promotion, but yeah, I mean, there's nothing to promote because I don't have a, it's not out yet. Well, we're going to have hopefully a landing page in the show notes that people can go and sign up to learn more directly from Colin. So what are you going to write about though? So you're how to do, you said production?

**Colin O'Flynn:** Yeah. Small scale. So, I mean, really, and, and I was a bit careful with how I scoped into game because, you know, there's a lot, a lot of people have done this. Once you start, you think you're really smart and you've done a good job, right? And then you start talking to other people and realize that like, oh man, other people are way smarter and did a better job, but it's too late. Um, I made my choices. Pen has been put to paper. Exactly. So, um, so it's really more, it's a combination of my own experiences, right? It's like a memoir on small scale production. Um, but the idea was to cover everything, right? Because, you know, we've gone to embedded world and book booths and like, okay, how do you, how do you book a booth? Ah, you've got to rent all this super expensive furniture at stupid prices. Okay. How do you do that? Um, so it was kind of like to take people from, I've got a cool idea. And then even if you don't want, even if you're not going to, you know, make a product, what does that process actually look like? Right? Like how much work is in idea to, I can ship a box to a person.

**Chris Gammell:** Yeah. That's actually really, that should be like recorded reading before any Kickstarter or crowd supply came campaign kicks off and be like, well, you have to go through Colin's checklist and add up all your time.

**Colin O'Flynn:** And it was like in doing it. Cause I didn't do that. I would just like started being like, Oh, I can make some PCBs. Let's do it. Let's do a Kickstarter. And this is back when Kickstarter didn't really enforce anything. So you could just do it. Um, yeah, it was, it's a bit of like, you know, lessons learned over that.

**Chris Gammell:** Yeah. Do you think a lot of it will change appreciably in the next 10 years as well? I mean, that's the other thing is like some stuff has changed from 10 years ago, but you know.

**Colin O'Flynn:** Yeah. Well, so the problem is I started this over COVID, right? So it's now five years old. So I've had to go through an update.

**Chris Gammell:** Oh yeah.

**Colin O'Flynn:** You know, it's about 70% plus written. So it's actually pretty, pretty far.

**Chris Gammell:** What I hearing here is that you have a future upgrade path for your, your book as well. Right. You can have like a 26th edition. The needed in 14 just came out and that's a better. Exactly. Right.

**Colin O'Flynn:** Well, yeah. So that's, that'll be one of the things to add, I guess. But I mean, I, I'm trying to, a lot of it's super stuff that hasn't changed in 30 years. Right. This kind of go right. Even simple, what I would call simple, but people don't think about it. Right. Like how do you deal with inventory from an accounting perspective? Oh, right.

**Chris Gammell:** Right.

**Colin O'Flynn:** There's a lot of stuff that you can get some really basic examples, but I've, I just struggled to find good examples specific to electronics hardware.

**Chris Gammell:** And you don't think that would be regionally specific either Canada versus us in terms of like, I guess taxation is you have to consider it at some point. It's all just like, just think about this and go talk to a professional. That's, that's good advice. And that's basically it.

**Colin O'Flynn:** It's like a lot of it is, you know, because a lot of it will change and, you know, I've tried to include details where I can, but a lot of it is just like, here's something again, things people don't, I don't know. I don't think they fully, some people think about sometimes you just don't have time to think about it. Um, so at least if you knew up front, you could say, okay, I need to make sure I talk to, you know, someone about how I'm going to deal with all this inventory that's coming in.

**Chris Gammell:** And, you know, I remember even when to go talk to professional, like, so you're not showing up at like an accountant's office. They're like, there's not, there's nothing here for me to do, right? Like being like having like that kind of like path and guide is very useful actually.

**Colin O'Flynn:** Yeah. Well, no, exactly. Right. And that's like, you know, I, I don't know if there's still stories of this, but I remember from early Kickstarter, there'd be a number of times when people would get the Kickstarter money. Right. But they wouldn't have the expenses yet because they didn't realize that, oh, if you just buy the parts, it doesn't actually count until you ship it. Right. Like you can't realize the cost. Um, and so they screwed themselves because. You know, they, they needed to defer it or stuff like that. Like they didn't do it in time. And they basically on paper had a super profitable business because they had all the input money and they didn't have expenses yet. Yeah. Right. Right. Like they, they hadn't set it up well enough that they could amend their return or stuff like that.

**Chris Gammell:** Yeah. So like Kickstarter money gets delivered December 31st and the new, yeah, all the parts are purchased on January 1st or something like that.

**Colin O'Flynn:** Yeah. Stuff like that. Right. And even in that case, like in, you know, depending on what you're using, you may not even be able to call it an expense until you ship stuff out because it's, oh, it's just an asset. Right. Like now you have an asset.

**Chris Gammell:** Yeah. Right. Right. Right. Like we have a hundred. It's inventory. You have to get taxed on that, at least in the U S I mean. Yeah. Well, yeah, exactly.

**Colin O'Flynn:** That's it. Right. So like you had a hundred K of profit and then you spent a hundred K so you have zero cash, but on the accounting perspective, right. You had all profit and asset like, right. You had no expense. You have zero. Yeah. So that, yeah, that's stuff like that. Right. That like, you know, I've, when I've been talking to people starting this stuff, it's not crazy, but I also think it's, uh, it's easy to miss if you're, you know, just coming out of school, like was sort of a thought process. Yeah. I've got a good idea.

**Chris Gammell:** That is one thing I wanted to ask you about too, since you are a teacher and you're kind of, you're dealing with the youths. Um, and we were talking about like their use of AI and kind of, uh, generally just students, you know, kids these days, uh, as a general, what, what are, what trends are you seeing there?

**Colin O'Flynn:** Yeah. Yeah. I mean, it's interesting. There's tons of chat GBD, like, um, and actually what was terrible. I don't know how many, you know, how much readers are plugged into it, but they, they released, um, a few months ago, a deep, what was called deep research mode research. Yeah. Yeah. Where it would like give you citations and everything, which is terrible timing. Cause in the class, I was just teaching a class, um, in the winter, it's like January to April term. And I had a big research paper is one of the assignments. Cause I was like, oh, that's something that chat GBD doesn't do a great job on. You know, it's like, boom, they released the exact thing that, um, but yeah. So the, the thing is, I mean, it's kind of an existential question of, are we asking students to do things that, you know, will be automated? So is it a stupid thing to ask them to do? Right. Got it. Am I asking them to do manual multiplication when everyone's going to use a calculator? Right. Right. You know, so, and, and it was kind of how I'm trying to approach it and in ways of making new questions. I mean, one of the assignments actually have them do so that in this course they were, um, I was covering for someone. So it's like a, they're using Ross to, to make a robot do various tasks.

**Chris Gammell:** Oh, yeah.

**Colin O'Flynn:** Yeah. So, I mean, I learned a lot doing it. Had to pretend I knew. Um, but yeah, so I have them ask chat TBD to make Ross to code, to drive the robot in a square, which it does an awesome job at, right? Because there's a million tutorials doing that. Um, I then say, okay, you know, use the same prompt and ask it to drive in like a maple leaf. And it just, so Canadian. Come on. I had to tie that in. Sorry. It had to be something, something that the witty tutorials, but it exploit, like it does not work. It doesn't even come close to working. Oh, yeah. Right. And the point is, it's like, it is a good tool. You could ask chat TBD, you know, get me the vector of a maple leaf. Like you could get it there. Sure. Right. You could say, make a function that drives the robot to an X, Y location and it'll make that and that'll work. Cause there's lots of examples, right? Like you'd tie it together. So it's kind of to prove, cause like what I was seeing as students would just like put everything in and it either worked or didn't work. Right.

**Chris Gammell:** And then they try it again, try it again, try it again, try it again. Yeah.

**Colin O'Flynn:** Like there is no, it was teaching them how to be able to make small testable things. Right. Like it is a tool that's useful, but make sure it's testable. You're responsible for what it's doing. Um, yeah. Yeah.

**Chris Gammell:** So, yeah, I saw an article that was about like, basically the, the, the skills of the future are one of the skills of the past, which is just troubleshooting, like being able to troubleshoot, you know, there is going to be there, you know, you have to assume there's some AI slop in the mix somewhere, fine, whatever, but you still need to be able to figure out what's going right, what's going wrong, how to test your assumptions, like just getting better at that. If you, if you were only teaching that like troubleshooting, I feel like that's, that's all every course would have been like every course would have been useful for that sort of thing, you know?

**Colin O'Flynn:** Yeah, absolutely. And that's, I mean, that was an interesting chat GPT usage. I saw actually, you know, we had some sample code that we're giving them that, you know, another prof wrote. So like, it's not, it doesn't exist per se, right? Like he made it really specific for whatever interface and there'd be errors and like the errors would come up and they were putting those errors into chat GPT, which of course was not going to work because like they were just, they were not to know their messages. Like it was just, this is an error message for, right.

**Chris Gammell:** But that was still the first thing was like, oh, do that. Yeah. Does that mean there's more like when there's like a educate or sorry, like a testing kind of paradigm then as well, you know, education always has like some kind of certification, testing, whatever, does it mean that everything has to be kind of in person? Even if there is like an allowed AI agent that's maybe with them in it, like, but it's just like onsite you're, you're watching the, the assessment happen.

**Colin O'Flynn:** Yeah. Yeah. I don't know. I mean, that's, it's a good question. That's stuff like that. I don't know if at least in our university, I haven't seen good answers to it yet. How are they going to deal with that? I mean, I was using a lot. So for this class, they just had a final project. So like, you know, they had to make a functioning robot that did various things. If they used AI to generate code, I didn't really check. I kind of, to some degree allowed it because I said, if you can get it to work, right. Like that's, that's, that's up to you, how you generate the code. But yeah. So for pure, I mean, for pure tests, like the thing I think we're getting at rate is like asking students to rate a research paper on some basic topic is like a non, basically that there's no way you can do that. You're saying, yeah, they just don't do that anymore. Yeah. Like, well, people still do, but I just think you're, you're totally like some students are honest and not using chat GPT that like, they're probably at a disadvantage because like, and it's so hard, you know, they're trying to use tools to detect AI, but I don't, I don't really trust them that much. My reliability is low. So like you're accusing students that haven't right. I'm using it and letting others through.

**Chris Gammell:** So I just feel like the, the problem is always the schools are there to test and certify whatever. Right. And like, that's a huge part of the educational process to like say that you're okay to move on. But like the actual focus on learning, like that is, that's always the tough thing of like, they're often decoupled. They've been decoupled for years and years anyways. Right. Even say for all of education of just like, just because I test on something doesn't mean of actually learned it, if anything, like if it just blew up the testing process and it was just focusing on the learning process, that would ultimately be a good thing. But I don't know if it ever would go that direction, you know?

**Colin O'Flynn:** Yeah. No, you're totally right. Like that's, I mean, there's been some discussions. I know other universities have looked at this about like, you know, what is the value of marks per se? Because yeah. Yeah. You know, as soon as you have marks and testing and then becoming like, did you get 87% or 85%? Right. Right. Is a thing. And then it's, yeah. Which then really is like, okay, what's the, what's the rubric for the assignment? Cause I have to exactly hit that. Right. Right. Because I need to maximize my marks because that's going to in the future impact a scholarship or something.

**Chris Gammell:** And yeah, yeah, yeah. Ties back to money and you know, like how people are there and what they're, like it's a service industry. You're here to like administer a service and, you know, certify based on this so that, you know, all that stuff. Yeah. So it really, it does ripple far out, but someone should. I would still be saying, are the kids actually learning anything? Like, am I learning anything? Like, do I learn anything when I, you know, use an AI engine? Like, yeah, maybe, maybe glancing, but like, do I need depth of knowledge for situations where I'm not going to have access to that stuff? Like, I don't know. It just, the changing nature of like the, the second brain kind of the offloaded to an AI sort of thing. Like, I don't know. Yeah.

**Colin O'Flynn:** Not very much. I mean, my, my, you know, excellent. This is getting very existential now. I'm sorry. Sure. Yeah. But it's like, right. Are we getting to a stage where you'll have like a, you know, knowledge will become, we'll kind of level off in a way because, you know, if everyone's just asking chat GPT, like who's posting blog posts and who's posting, you know, stack overflow questions and stuff like that. Right. So it's like, if AI doesn't know the answer, then.

**Chris Gammell:** Yeah. There's no novel, novel discovery and like publishing about it. Like, what does it ingest?

**Colin O'Flynn:** Yeah, exactly. Right. Like where, where does it, if ever, if no one's, if people aren't publishing as many things, cause they're not, you know, just writing stack overflow questions and stuff like that.

**Chris Gammell:** Yeah. Right.

**Colin O'Flynn:** Like you're just asking chat GPT and that doesn't become public.

**Chris Gammell:** Like, um, maybe it trains on it. That would be the most old man thing for us to do is like soup. And then like, Hey, do you remember the good times?

**Colin O'Flynn:** Stack overflow? Yeah. Back in the day. Oh, good times. Slash people yelling at you. Back in my day, people were grumpy about things and AI's learned from it.

**Colin O'Flynn:** Yeah. Yeah. Yeah. So I don't know. I mean, it is a bit for research, right? That's where like AI, you know, and again, that's what I'm trying to show. Like, Hey, it's good for basic stuff, but, and it could be good for more complex things, but you're also, you know, if you want to push the boundary, then you can't ask it to push the boundary. Cause it doesn't know, like, you know, it's, you know, and I think just removing the magic is almost what they need because for some students, I feel like they do write really big. I can ask this anything. And it gives a good answer.

**Chris Gammell:** Oh yeah. Yeah. Everybody learns that the hard way, like a couple of times before they're like, Oh, maybe I should think about this and be strategic.

**Colin O'Flynn:** Yeah, exactly. Right. And the problem I see is right. That if you're teaching a class, like, you know, how many classes you've, you've seen where it's like, this is the same material from the last 30 years. Right. And like, so of course it's giving a great answer for every class question. Yes. Right. It's not novel.

**Chris Gammell:** I guess some of it is the onus kind of goes back on the professor to put more input in for novel, novel questions for novel solutions, that sort of thing. But yeah.

**Colin O'Flynn:** Yeah. Yeah, exactly. Which is, and I think that's kind of what we're getting at. Right. Is, which I don't think is a bad thing. Like, you know, when I went through university, there was, there wasn't chat GPT, but there was people that had, you know, burned CDRs of a whole bunch of scanned assignments from like 10 years.

**Chris Gammell:** And they would be like, here's all these. There is an old sentence. Burn CDRs of old assignments.

**Colin O'Flynn:** Yeah. Right. But I mean, it's to some degree the same, like cheating's always there.

**Chris Gammell:** Like, yes, it's more effort. And at the end of the day, those people did also did not learn those things. Right. I mean, that's same, same, same, right. It's like, not like the person who, you know, just formulaically, you know, use the old assignments to, you know, fill in the blanks and get the output. It's like, they got the grade, they didn't get the knowledge. And then like, okay, but we need the knowledge. We still need people who know things. Right. Exactly.

**Colin O'Flynn:** And that's kind of what I get at when people, you know, cause some props will really be like, ah, chat GPTs, you know, ruined everything. Um, you know, I think it's always been ruined in a similar way. Like it's, you know, if you, if you're realistic, maybe it's more obvious now.

**Chris Gammell:** Like these, these kids are using abacuses and that, that makes the math easier. Yeah. Yeah. Well, I mean, are you, uh, you know, you interact with students and stuff like that too. Does it make you more hopeful though, that they are, have access to more knowledge? Is it more novel solutions for things as well?

**Colin O'Flynn:** Yeah. I mean, I definitely see, um, you know, especially, I mean, this course was interesting because, because it was sort of a new topic for me because it was this sort of cover. Um, so, you know, there was like a few groups like, oh, you know, like I made this whole simulator for my robot and it's like, oh, wow, that's, I didn't even know. That's why I don't know how to do that because this isn't stuff I do a lot, you know? So there are still, when I, you know, when I went through, I remember being like, you know, there's a few really super engaged students who want to do all the things. Um, so it still seemed that way. Like it definitely, there was some very engaged students and I think, you know, they were doing way, you know, like there were 3d printing tons of stuff and a lot of people were doing that, but, you know, looking at PCB designs, they were doing advanced coding. Um, that's awesome.

**Chris Gammell:** Yeah. That's the thing. Like it's, it is like, it opens up new spaces and things, you know, barriers have come down. That's really great. I feel like. And I guess my, my experience with that is just like, uh, being in the hardware industry, interact with, you know, younger people are coming in that are like more software savvy too. And just like software methodology brought into the hardware space, like that has been very positive as a general development, um, kind of across the board, you know, it's chip vendors can't get away with the same kind of stuff that they might've put out. And then, but then they also hire smart people to build software than that. It's just kind of like rising tide sort of thing lifts all boats, which is good.

**Colin O'Flynn:** Not very much so.

**Chris Gammell:** Yeah. Like if I started out in Ross too, right now, I wouldn't know where to start. So like if there's a bunch of beginner content that like everybody can start with and that helps me too, when I go into a new topic area. So.

**Colin O'Flynn:** Yeah, no, exactly. Right. That's the thing. There was, there was tons of material out there and like, yeah, like this is, and the, you know, the discussion in this course and, you know, we keep having this discussion in various courses is, you know, where do you start? Because I think there's only so much time. There's only so much you're going to cover. Yeah. Right. Right. So it's like, do you start at like, you know, we're still doing resistor networks and stuff, which is important, but also you then don't have time for.

**Chris Gammell:** Yeah. Yeah. I haven't run into many resistor networks myself in. Yeah. Well, exactly.

**Colin O'Flynn:** So like it's, but the argument is, it's like, well, this is used and, you know, heat flow and there's a bunch of stuff where it's used. Yeah.

**Chris Gammell:** Right. Right.

**Colin O'Flynn:** Which isn't wrong, but also. Right.

**Chris Gammell:** I, I, I, sometimes I feel like it comes down to like practical versus academic, like end goal as well. So like, if someone's going to be like going to get a PhD in like some thermodynamic field, then they probably need to know that sort of thing. But like me as like, you know, a dummy, dumb, dumb engineer, who's just going to make things, build things. And like, hopefully they work. Uh, you know, it's just a different outcome that I'm hoping for. Like, I never wanted to know all the base physics about things. Cause it's like, I just wanted to know enough about them to, to move on and like make a thing, you know? So education. Well, you got yourself into quite a space there, Dr. O'Flynn. Yeah.

**Colin O'Flynn:** That's something, but I mean, it is, uh, you know, I think it's interesting to see what people are coming up with. Like it is, as I said, it is amazing. You know, what the capabilities are and lots of people using, you know, little Linux things and stuff like that. Yeah.

**Chris Gammell:** Yes. Yeah. It's, uh, there's, yeah. Starting from cool, cool spots and doing cool things. That's great.

**Colin O'Flynn:** Yeah.

**Chris Gammell:** All right. If people want to see the cool things that you're working on, Colin, where can, uh, where can they find your work?

**Colin O'Flynn:** So right now I have a half updated blog and call them a Flynn.com. That's probably the best spot. Um, yeah, I'm trying to post more. So I've, I, I recently recorded a video. So for this class, actually, uh, kind of, you know, I called an intro to PCB video series, but again, tons of caveats because, um, the, it was designed to be shoved within like one or two classes. So, you know, there's only so much you could do in there, but yeah, I, my, my goal is to get more content posted. Um, a few more teardowns too. So I, one of the things I was looking at with some RF stuff, so like a Marine X-band radar, um, looking at how that works and yeah. Yeah. A few new topics, right? I mean, one of the fun things about academia is you have so much crossover, so I'm trying to embrace that a little more than just pure security, stuff like that.

**Chris Gammell:** More fun things coming from Colin then as well. And we'll, uh, you know, you'll be back at five years. We'll talk about it then and see how it is soup and, you know, see how it goes.

**Colin O'Flynn:** See how life is chat GPT. Maybe it'll just do the interview for us actually.

**Chris Gammell:** Yeah, exactly. Yeah, exactly. No content.

**Colin O'Flynn:** Yeah, exactly.

**Chris Gammell:** Schedule it now. All right. Well, thanks for being here Colin. Good chat. Thanks so much for having me Chris. Outro Music
