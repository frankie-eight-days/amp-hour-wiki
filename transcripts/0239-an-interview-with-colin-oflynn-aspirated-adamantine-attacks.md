---
episode: 239
title: An Interview with Colin O'Flynn - Aspirated Adamantine Attacks
url: https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded March 3rd, 2015. Episode 239, with guest Colin O'Flynn, aspirated adamantine attacks.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Colin O'Flynn. Welcome, Colin.

**Dave Jones:** Is that a Canadian accent I hear?

**Chris Gammell:** Yeah. You got that from that? Last name O'Flynn, and you say, are you Canadian? Yeah. The middle name's Patrick, too, so it's excessively. Right. Favourite day of the year, March 17th. Yeah. Well, welcome. And Colin is part of the, well, no, not part of, the, he is, welcome, the chip whisperer. Oh, thank you. Shhh. Whisper, whisper, whisper, whisper.

**Colin O'Flynn:** As long as Cesar Millan doesn't sue me, it's fine. Or Robert Redford, right?

**Dave Jones:** And very, very timely. Yes. Very timely, because I just released a mailbag video yesterday with your chip whisperer project in it, which, as everyone should know, because everyone follows, anyone who listens to the show, I'm sure, followed the Hacker Day contest and knew that you came second in that. And they may not know that you've got a new Kickstarter for a chip whisperer lite.

**Colin O'Flynn:** They do now.

**Dave Jones:** So they can go buy one. Well, they do now.

**Colin O'Flynn:** Yeah. Yeah. Make sure you put in Dave's name as the sold buy, and then he gets 10%.

**Dave Jones:** Oh, do I? Hey. All right. There you go.

**Colin O'Flynn:** Now we're talking.

**Chris Gammell:** Kickstarter upgrading. Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** I think that should be a featuring Kickstarter. A commission system. An affiliate program. A commission-based thing.

**Chris Gammell:** Yeah, they already have that, Dave. It's called The Money Goes to Kickstarter. Right.

**Dave Jones:** The Money Goes to Right. They're the ones who get it right. Yeah.

**Chris Gammell:** Got it. So, Colin, let's talk about security, because I think this is an interesting topic. I don't know if we've talked about it much on the show before. Maybe when Mike Osterman's been on.

**Dave Jones:** We've touched on it, but we've never talked about the level of detail you're capable of doing with this project, though.

**Chris Gammell:** So, security. Why security? Why embedded security? What's the deal? All right.

**Colin O'Flynn:** So, the basic deal here is that we get a lot of people doing stuff. You know, they want to protect maybe their IP of the product, and they say, ah, I'm going to throw AES, you know, AES-256 on my bootloader. And it's unbreakable because, according to the government, you know, you can use AES for, like, top, top secret protection of documents. And the problem is that when you implement it on real embedded hardware, there's these fundamental issues. Like, it takes a certain amount of power to set more lines high than it does to set them low. And you can measure, you can basically measure these tiny, tiny power differences and break the encryption algorithm that's running on these embedded systems. So, it's, you know, it's not just a checkbox. You can't say, oh, yeah, I got AES. We're done. You know, go home. Type thing.

**Dave Jones:** Because it was designed – is it because they didn't think about the embedded platform when they designed that standard? They thought, oh, it's running on computers, which nobody has physical access to. Therefore, it's unbreakable. Yeah.

**Colin O'Flynn:** Is that – I think they – well, at the time, I don't think they really knew about these attacks. But, I mean, even now, fundamentally, they're almost unprotectable. So, there's some things you can do in hardware. Like, you can have balanced registers. So, it sets one line high at the same time it sets one line low. So, you can't see any switch, right?

**Speaker ?:** Ah, got it.

**Dave Jones:** So, it masks out those current pulses. Yeah, exactly.

**Colin O'Flynn:** So, but this costs more area. So, if you're just doing, you know, like a XMega or some sort of standard hardware peripheral. Chip, yep. You know, you're not going to waste the silicon on doing that fancy stuff.

**Dave Jones:** Because there's dedicated encryption chips, isn't there?

**Colin O'Flynn:** Yeah, exactly. So, things like smart cards, they –

**Dave Jones:** Right. And they would probably have something like this, I'm assuming. Yeah, exactly.

**Colin O'Flynn:** With those dedicated chips, right. Because they have good money behind it, right?

**Dave Jones:** Right.

**Colin O'Flynn:** So, that's what really differentiates them. But a lot of people don't realize that. You know, they'll use a regular chip and just say, yeah, we're doing software. It's fine. Right. So –

**Dave Jones:** But it stops the majority of people, though. But it's not going to stop the –

**Chris Gammell:** It's like a lock on your house, right? That kind of idea. Right. Stops people just from directly – Stops the honest people. Yeah.

**Dave Jones:** Right, exactly. But before the chip whistler came along, how hard was it to – is there a word for this? For decrypting security based on power line checking? Yeah.

**Colin O'Flynn:** So, the whole field is really – officially would be called side channel analysis using power analysis. And it's more frequently referred to as DPA or differential power analysis, which is the first real algorithm published in this area. And so, people have been doing it for a while. Like, this was published in 1998. And – Okay. There was commercial hardware. Like, you could buy setups for doing the attacks. And I've never got an official quote, but it's on the order of $30,000 to $100,000 for these setups, right? Right, yep, yep. For serious people, yeah. Yeah. So, before this – and a lot of academics do it. Like, you can use a regular scope, but, you know, you've got to script everything in MATLAB and stuff. And no one really shares that because it's – you know, some PhD has spent a while making it and he doesn't want to just publish it freely.

**Dave Jones:** No, he wants to go make a startup so he can make a $50,000 machine to sell it. Yeah, exactly, right? That's right. So, finally pay off those student loans.

**Chris Gammell:** Yeah.

**Dave Jones:** That's it. So, wait.

**Chris Gammell:** I want to take a step back then. How did you get into all this? Because, again, the whole security field, like, you know, I went to DEF CON, got to meet you. Yeah, you were there, right? Yeah. Mike was there.

**Colin O'Flynn:** I think we ran into each other once.

**Chris Gammell:** Yeah. Well, we saw each other at Solid as well. Yeah. But I never really understand this. Like, is it – did you come in from the IT side? Or, like, it feels like that's a lot of the – a lot of people are coming in from the IT side but not necessarily – and then kind of getting into the hardware real deep. So, how did you get into all this?

**Dave Jones:** Starting with your background, like, your actual career.

**Chris Gammell:** Yeah, okay.

**Colin O'Flynn:** Way at the beginning. Yeah, yeah.

**Dave Jones:** The way back machine.

**Colin O'Flynn:** I was born in – Yeah, yeah. Not quite. When I was a wee lad.

**Chris Gammell:** I liked fans. Start with your first job. It was about 19. Sorry. Yeah. Am I allowed to make a boot jokes? Can I say a boot? Is that cool? A boot?

**Colin O'Flynn:** Yeah. Don't worry about it.

**Dave Jones:** Sorry? What's this boot joke? No. Sorry. That just flew straight over my head. No, no.

**Chris Gammell:** Canadians say a boot instead of about. It's endearing.

**Dave Jones:** Oh, right. Okay. Right.

**Chris Gammell:** Yeah. Got it. Now you get it. A boot.

**Dave Jones:** I can speak fluent Canadian now.

**Colin O'Flynn:** You'll just be able to trick everyone where you're from. Yeah.

**Dave Jones:** Right. Just like I can do fluent Yankee speak if I just speak in a southern accent, you know. Yeah. Like a southern hick. What you think is a southern accent, of course. Small town accent. Yeah, right. That's right.

**Chris Gammell:** Anyway.

**Colin O'Flynn:** Sorry. No, go ahead. Sorry. Go. Yeah. So I started all sort of as a hobbyist really is almost my background. And I did electrical engineering in school. And during that time, I worked at a place doing gimbaled cameras. So the, you know, cameras in the bottom of helicopters and stuff like that. So that was a lot of fun. So I did that for a few summers, you know, as an intern or whatever you call it type thing. And after that, I worked with Atmel and sort of the low power wireless division for three years. And that's a lot of that was Internet of Things and all that stuff. So obviously you get sick of Internet of Things once you spend more than a year in it basically is the.

**Dave Jones:** We've got sick of it after talking about it for a year. Yeah. Yeah. Right.

**Colin O'Flynn:** That's as much as you can deal with. So, yeah. And then after that, I went back to school. And originally I was doing magnetic field communications and switched. I'd seen a presentation on this whole area of, you know, side channel analysis and sort of said, oh, wow, that's super cool. And yeah, basically switched my whole topic. And that more or less brought me here.

**Dave Jones:** Is this your like a master's thesis or something? Did you go back and do?

**Colin O'Flynn:** Yeah. So after doing the bachelor's, I went back. The plan was to do a PhD. So start with master's, then switch in to the PhD, which.

**Dave Jones:** And then sell a device for $50,000. Yeah.

**Colin O'Flynn:** Somewhere along the line, right? So, yeah. All my background's embedded. That's really where I came from. And I'm in the security field. And it's always a bit scary because at DEF CON and stuff like that, like I just have a Windows computer and, you know, I don't really care. It's not encrypted. It's not any of this thing. I think when I was at DEF CON, I bought some stuff from DigiKey while I was there because I really needed something. So I was like, oh, you should not be doing this. You're on the grid. Yeah, yeah. You're putting your credit card in this. DEF CON network. But nothing happened. Didn't end up on the wall of sheep though, huh? No, yeah, yeah. I had VPN. I was careful. There you go. I don't know. I only vaguely know what I'm doing, right?

**Dave Jones:** So this topic is your master's thesis, is it?

**Colin O'Flynn:** Yeah, well, it will be my PhD thesis. That's where it stands. Oh, right.

**Dave Jones:** It will be your PhD thesis. Okay.

**Colin O'Flynn:** And where are you studying? Dalhousie University here in Halifax, Nova Scotia.

**Chris Gammell:** Nova Scotia, which is – I don't – so I grew up next to Canada and Buffalo, but I don't know much about Canadian geography. But I looked at pictures and it looks frigging beautiful up there.

**Dave Jones:** I was just going to say it sounds cold.

**Colin O'Flynn:** They only show you photos of it in the summer, right? That's the trick. I did notice that. But yeah, the summer, it looks beautiful. It really does. Yeah, it is. Two months, right?

**Chris Gammell:** Yeah. That's cool though. Yeah. Right.

**Dave Jones:** So this makes sense. This makes sense why it is so in-depth, this actual project. It seems like more than what just some hobbyists would do as a side project. You've just put too much work into it.

**Chris Gammell:** This is your $50,000 thing, but you forgot to charge that much. Yeah, exactly.

**Dave Jones:** You're doing it wrong. You're doing it wrong. You're paying big money to do a PhD and you're giving it away, open source. What's wrong with you, man? Yeah.

**Colin O'Flynn:** Well, it's funny. I talk to, every so often, there's people interested. Oh, we want to invest in what you're doing. But it's like, no, I'm giving it away, by the way. So, you know. You're like, oh, how would you do that? It's foolish.

**Dave Jones:** But you can still invest in open source hardware? Startups? MakerBot? Hey, they were open source and they got bought out for $400 million, $500 million bucks or something?

**Chris Gammell:** $625. Really? $625.

**Dave Jones:** Sorry.

**Chris Gammell:** I'm just calling it like you see it, man. So, yeah.

**Dave Jones:** No, I would actually call them back and say, yeah, look at MakerBot. I'll be the next MakerBot. Yeah, yeah. Right. So, that can be your pitch presentation, you know. I'll be the...

**Colin O'Flynn:** Just that. No questions.

**Dave Jones:** Right. No, that's it.

**Chris Gammell:** Yeah. So, a PhD program. So, what is the PhD? Is it like an actual crypto PhD program or is it just embedded or what does that involve?

**Colin O'Flynn:** Yeah. So, the PhD here at Dow, it's a pretty small school. So, I don't know if there's like 20 profs in the electrical department. So, my PhD is really electrical engineering. My supervisor does communications and radio and antenna design type work. So, there's no real embedded crypto. I sort of was on my own here. And I got funding. There's a Canadian, you know, research council that'll fund you more or less. So, I have funding to do effectively whatever. You know, you get paid for three years. That's great. Should be done. So, yeah. I mean, that's part of the reason it's all open and free like that is there's no one saying, oh, we want...

**Chris Gammell:** Because you're not paying for it.

**Colin O'Flynn:** Yeah, exactly. Right?

**Chris Gammell:** So, from what I hear, I mean, I have some friends who went through PhD programs I didn't myself. But like, you're pretty much on your own no matter what you're doing. I mean, like, you can have an advisor maybe that's kind of guiding you along. But, you know, it's research. You're trying new things. So, yeah. You know, you're out in the wild basically.

**Colin O'Flynn:** I mean, some people, their supervisor really tells them what to do. But, I mean, I prefer to not. I'd rather just show up every week and see what's happening.

**Dave Jones:** So, did you have the idea for the chip whisperer from the start of your PhD? Or did it just eventuate because, oh, this would be cool. There's nothing out there. I'll actually produce something. Did you start out with hardware in mind or just the actual PhD research side of things?

**Colin O'Flynn:** Yeah, it did start out with research in mind. And you can really, because it's all been, you know, in Git, you can look way back and see how it started. It's really clunky, gooey, and stuff like that. And it really started because we, in our lab, we had one really good scope and one pretty good, you know, like one gig a sample per second scope, which wasn't quite enough for what I needed to do. And at the time.

**Dave Jones:** Mine, mine, mine, mine. I can miss it.

**Colin O'Flynn:** Right. And, like, the other one people were using for ultra-wide man. It was, like, a 12 gigahertz analog bandwidth. Yeah. Right. 50 giga samples, I think. Anyway, so, yeah, and I couldn't use that one. They were using it for more important stuff. So, yeah, it really just spun out of that. It's like, oh, I need this hardware to do it. So, the first version of it was just an FPGA dev board with an ADC. I designed, built onto it, and then it slowly morphed into newer and newer revisions.

**Chris Gammell:** I kind of have a checklist of things that, like, in projects that I like, and scratch your own itch is always number one, you know, like that, just because it just means that you, you know, you're not, like, guessing at what people want. It's like, no, no, I am customer number one. And I know exactly what I need here. So, yeah, that's good. That's a good sign.

**Dave Jones:** And as you said before, a scope can do the job, but it's clunky, right? So, if you're doing research on this, yeah, you would want to build a more optimized tool for getting the results you want, right? Although, you don't want to have to, for the next two years, three years of my research, yeah, I'm going to clunk around with a scope and manually capture and export the data and blah, blah, blah.

**Colin O'Flynn:** Yeah.

**Dave Jones:** You know, that'd be painful.

**Colin O'Flynn:** Yeah. Yeah. And that's where, you know, people script it all, but it's still, it's not portable. There's all these issues like that. Yeah.

**Dave Jones:** It's just, you have to have the right tool for the job. There's a lot to be said for designing a tool that does exactly what you need.

**Chris Gammell:** So, at this point, can you explain the physics of it, of it all? So, sorry, I didn't have to go over the entries as close as Dave did. But for the bag of the friends.

**Dave Jones:** He's already explained it. Did I miss it? I mean, so I know that you said- Power, like, transistors, you know, like these chips, they have, like, totem pole outputs, you know, how chips are designed. Yeah, no, I get that. Yeah, I know. And when they switch, they, you know.

**Chris Gammell:** I get it, but like- And you can- But the thing I don't get about it is, okay, so you have, I mean, why doesn't it just look, does each individual pin output look, have a super discreet, different, signature from the next one? So, can you characterize, like, every pin being on or off? Or do you just look at every pin?

**Colin O'Flynn:** So, I mean, how it works fundamentally is, the answer to that question is that you can almost do that. But what I really do as the base is that I'm looking at the data bus inside the chip. So, you know, if you move data from the registers, read it from the registers, put it on the main data bus, it's physically setting, you know, three of these data lines to a high state. Setting those data lines high is basically charging a very small capacitor, which physically takes power. And so, on every clock edge, you could look and say, okay, three of these data lines were high because there was a large, you know, a spike this large. On the next clock edge, seven of the data lines are high. And in between the clock, it's going to an intermediate state that, they call it the pre-charged state that's basically halfway.

**Chris Gammell:** Yeah. But the thing that I don't understand is, doesn't it matter the order in which those, so you know that three lines are high. I mean, it matters which three, correct?

**Colin O'Flynn:** Yeah, yeah, right. That's the important question.

**Chris Gammell:** So, how does that work then?

**Dave Jones:** This is, yeah. Well, this is the question I had is that, yeah, did you have to do this using signature-based stuff? Do you have to, like, test the chip that you want to decode and then get a signature map of all the different stuff that happens in there? And then you just, once you've got that signature map, then you compare current spikes? Is that how it works?

**Colin O'Flynn:** So, I don't actually have to do that. You can do that. That's sort of one of the more advanced attacks. Because that can tell you, you know, in a single power measurement, it can tell you the exact state of the data bus. What I do is I average a few of them. And you basically use this guess and check system where you say, like, if I had, you know, if the secret key byte was some number, zero times zero, one. And I know how the algorithm works. And I can say, okay, well, if the secret key byte was zero times zero, one, based on the input data I sent to it, the intermediate value, you know, at this point in the algorithm would be something. So, if I was just XORing the input with this secret byte, I could say, well, in this case, the secret byte should be, you know, zero times AB. The next case where I send it a different input. So, I say, you know, send it this input, encrypt. The intermediate state would be something else. So, I'll sort of try every possible secret key. And then one of these sets of intermediate values should match the power I measured. So, you know.

**Chris Gammell:** Okay. So, that's like brute forcing a password as well, where you have the hashed value and then you're just comparing it against a lookup table or you're going and trying every combination as well. Is that similar?

**Colin O'Flynn:** So, and what makes it good? Because, you know, you say, well, guessing that's no better. Is that for something like AES 128, you know, 128 bits, but the algorithm works on eight bits at a time. So, you only have to guess two, you know, the eight bits 16 times. So, now you have this 16 times 256 instead of two to the power of 128.

**Chris Gammell:** So, one of these is a lot easier than the other. So, if computer architecture, if the architecture of that changed in the future where it did somehow simultaneously look at or process all the bits at once, would that make things incredibly difficult for you or would that just change the game?

**Colin O'Flynn:** No, it's a little noisier typically. But, I mean, you can. So, there's an implementation that's doing all 128 bits at once. The thing is the way the algorithm's designed, it's operating on eight bits at a time. So, it takes eight bits of the input, takes eight bits of the key, XORs them together, and puts it through a lookup table. And because of how the algorithm's designed, it's fundamentally breakable. Whether or not it does all 16 of those at once. It can do that, you know, in parallel. That's fine. And it doesn't affect this attack at all. Okay.

**Chris Gammell:** So, it's just how AES is set up, you're saying. Exactly.

**Colin O'Flynn:** And, I mean, they do that because, you know, if you try to operate on 128 bits at once, you would need a 128-bit lookup table. Yeah. Right? So, they split it down to make this really small lookup table at the SBOX. Yeah. So, that's sort of the fundamental problem.

**Chris Gammell:** So, resource constraint is ultimately what allows you to break the code. Yeah. Because if you had a 128-bit lookup table, you'd be able to do that, right?

**Colin O'Flynn:** Yeah, right. So, then this wouldn't work as well.

**Chris Gammell:** Hmm.

**Dave Jones:** Now, the first thing that pops into my head when I hear about this sort of attack on a chip is going, well, what effect does the bypass cap caps?

**Chris Gammell:** Oh.

**Dave Jones:** Have on the chips. Do you have to remove the bypass caps to be able to, you know?

**Colin O'Flynn:** Break it. Actually do this or what? Yeah. So, that's one of the things. I mean, if you're doing it with a physical shunt, then, yeah, you would need that. But the trick is that you can also use an EM probe like the ones you have, Dave, for doing

**Dave Jones:** the H-field probing.

**Colin O'Flynn:** And it's the same thing, right? The current consumption generates a spike. Yeah, of course.

**Dave Jones:** So, yeah, it doesn't really matter. Sorry. So, the shunt has to go after the bypass cap? Is that what you're saying?

**Colin O'Flynn:** If you're using a resistive shunt, it would have to go after. So, you've got to remove them. Right. But you can just use an E-field probe instead.

**Dave Jones:** I thought, yeah, there was no way. Yeah. I was pretty sure there was no way it would work if you put it before the bypass caps.

**Colin O'Flynn:** Just be a line. Right.

**Dave Jones:** Got it. Yeah, yeah, exactly. Well, you would get a very low-pass filtered version of the current spikes. Yeah, exactly. So, yeah. Yeah, it wouldn't work. Okay. Interesting. So, which is better? Your current shunt or the H-field probe?

**Colin O'Flynn:** The H-field probe tends to give better results, I think. And in real systems, it's easier because people have done demos where, you know, they take a cell phone and turn it over and just put the H-field probe on the back. Like, they don't take it apart at all. And they're able to do the attack. Right. The problem is that you need to position it very, very carefully. So, the shunt's easier because, you know, you solder it down and you're done. Yeah, yeah. So, I use that because I'm all about repeatability. If it's research stuff, right, you want.

**Dave Jones:** Oh, yeah, of course. Yeah, you don't want to be dicking around with it. Works one day and doesn't work the next because your tongue's not at the right angle.

**Colin O'Flynn:** 15 microns this way and stuff like that.

**Speaker ?:** Oh, jeez.

**Colin O'Flynn:** Yeah, yeah. Right. It's like, no. We're not doing that.

**Chris Gammell:** Okay. So, I need some more clarification. I'm going to keep playing the dumb guy. This is my role here.

**Dave Jones:** It's always your role on the API, Chris.

**Chris Gammell:** That was, that needn't be said. But anyways, just wait until our guest in two weeks. It'll be a bloodbath. So, okay. So, people are using AES-256 type stuff for, so that'd be for like the bit stream, like for programming the chip. And then you're kind of executing a man-at-the-middle type attack? Or what then are you ultimately attacking?

**Colin O'Flynn:** Yeah. So, it depends what your objective is. But a popular, the example I use a lot in using some of the demos is if you have an AES-256 bootloader. You know, someone's encrypted their upgrade file or binary file with some AES-256 key, and that key is on the micros. The idea being that you can send this binary to anyone, and they can only program it into a microcontroller that you've pre-programmed. You know, the manufacturer's pre-programmed with their key. Yep. And so, you can send it to China or wherever else you want, and you know, you don't have to worry that they're going to steal it.

**Dave Jones:** But isn't that easier? Isn't it easier to just decap the chip and steal the firmware, and you don't-

**Colin O'Flynn:** Yeah, you could do that too, right? But this is another way of doing it. Right. Because the key is in the chip, you're able to instead do a side-channel attack. So, if you just give me a chip, it doesn't have the firmware in it or anything, then I can do a side-channel attack on that chip to figure out what the secret key that's programmed into it. And people show this with, you know, FPGAs for, I think, most of the vendors, like the Bidstream encryption on them.

**Chris Gammell:** Yeah, they all have an encrypted Bidstream, yep.

**Colin O'Flynn:** Yeah, so people show an attack against that, that, you know, if you have a chip, you can get the encryption keys out of it. And the problem is that most of these people are using the same encryption key across a whole bunch of devices, right? So, because otherwise, how do you, you know, you've got to manage, okay, well, I give this one user this firmware encrypted with chip, you know, whatever key, so.

**Chris Gammell:** Right, you don't want to, like, laser etch the key for each individual chip, like a unique ID or something crazy like that. Yeah, so. Well, that, because then everybody would need different firmware. So, okay, so that's one example. So, so it's for people to basically reverse engineer and steal a Bidstream, which actually we talked to Mark and Joe from Salier about, right? Because they had that, that issue, and then it got cracked real quick.

**Dave Jones:** Ah, that's right, yeah.

**Chris Gammell:** So what else do people use this for then? Like, what are some of the, the devious things people could, could use this for? Obviously, you've got, you're testing, right? You're, you're super white hat, right? I'm sure. Yeah. Yeah.

**Colin O'Flynn:** To be honest, I don't know where all of the possible uses are. I'm really on the, you know, training and teaching side of it. But there's a whole lot of stuff. Like, you look at Internet of Things, and a lot of these protocols, like 802.15.4, Zigbee, Bluetooth Low Energy, they use AES, typically AES-128 to protect their networks. And with any of these nodes, you can send them a message and they'll decrypt it. So any device that you can send a message to and it'll, you know, decrypt or encrypt it is basically vulnerable to these type of attacks.

**Chris Gammell:** Okay. So you could, you could send like, so if you're normally sending garbage to like a node because it, it, it only accepts stuff that's, that decrypts as something that makes sense to it, like a packet header that would start talking to it. You're saying that if you went and side attacked it and figured out the key, then you could start sending it legit commands. And that might be the only thing that they, that they were really protecting with. They don't have any kind of handshake or anything.

**Colin O'Flynn:** Yeah, exactly. Like they may, maybe doing something like that.

**Chris Gammell:** And then you can go just start looking at someone's drop cam footage or something creepy like that. Whatever you want to do. Drop cams are super freaky, by the way. I, I was, where was I? I, I was, I forget where I was somewhere in California, but I was like, just like, I kind of like looked up and I'm like, oh, that's a drop cam. That's creepy. You know, like, it's just like, I don't know. Like, I don't know why that more than like a security footage, I think, cause it's just streamed to the internet, but something about it just, I don't know. Not a big fan.

**Dave Jones:** So where is all the heavy lifting in your, on your side of things done? Is it done in the FPGA or is it done in your software?

**Colin O'Flynn:** No, so it's entirely on the software. The FPGA is just shuffling data. So it does the.

**Dave Jones:** Oh, okay. Right. So it's just shuffling data from the 14 bit analog to digital converter, which is measuring the power. Exactly.

**Colin O'Flynn:** So, you know, it has a little RAM in there and stuff too, but that, that's all it's doing. It's none of the analysis is on the. I mean, that was a big thing. The software you can actually use with a regular scope. So you don't need the chip whisper hard drive design.

**Speaker ?:** Oh, okay.

**Colin O'Flynn:** Right. It's, you know, a lot of people are using that.

**Dave Jones:** Nice. So. Oh, excellent.

**Colin O'Flynn:** Yeah. I tell people it's a real.

**Dave Jones:** And, and that's all open source as well, is it?

**Colin O'Flynn:** So I tell people, you know, it's a real open source project. I'm not saying like, oh, it's open, but you know, non-commercial and blah, blah, blah.

**Dave Jones:** Right.

**Colin O'Flynn:** You know, it's like, yeah, you can do whatever you want with it. I don't care. I got a PhD to finish here, folks. Yeah. Yeah.

**Dave Jones:** I would have kept the software to myself. I think this is pretty advanced stuff.

**Colin O'Flynn:** Yeah. Yeah. But so many people have done that, but it's one person needed to release an open source one to really show people how it, how it can be done. Right.

**Dave Jones:** And God, well, it's awesome. My white hat is off to you. Oh, goodness. So can your chip whisperer attack or your software, basically, can it do other types of attacks, not just the power rail? Yeah.

**Colin O'Flynn:** All it's doing is power rail. So the differential paranoia attacks. Got it. Some of the demos do other stuff.

**Dave Jones:** Yeah. But I thought it could, there's, I can't remember the precise details, but you're talking about like, you know, you can actually spike the power rails as well. Is that right? Yeah. So that's a. You can change and you can intercept clocks and things like that, and you can change the jitter on them or something. Yeah.

**Colin O'Flynn:** No, no, no. That's right. So that's on the capture side. So not really the analysis. That's the hardware gain. It can do that. So it can, you can do stuff like if you drop the power, you know, at very specific instance, you can skip over a check and stuff like that. So if it says, like, oh, is the password okay? And right at that moment, it just says, like, oh, yep, it's okay. Yeah. Okay.

**Dave Jones:** So your, your hardware can actually dip the power. Yeah.

**Colin O'Flynn:** All it has is like a MOSFET basically. So it's doing a, you know, a crowbar type thing, just very short, like, you know, nanoseconds possibly.

**Dave Jones:** Right. Yep. But it sucks all the energy from the bypass cap and then boom, it's got to charge back up and that gives you a droop in the rail. So, and what, what can you do? What's the advantage of what can you do with that, that sort of attack as opposed to the power rail?

**Colin O'Flynn:** I mean, that sort of attack, the power rail is very specific, you know, it's breaking encryption. That's more or less all it's doing. Whereas the glitching type stuff, you can do stuff like if there's just a check at boot, you know, it checks, is this signature valid? And people have used this for a while, you know, they loaded firmware that doesn't have a valid signature and they just glitch past that check. So the glitching is probably even more powerful, but it's less precise. You know, there's no real math behind it here. It's just you screw around a bunch and at some point it works at the right time.

**Dave Jones:** I've heard that there was a, many years ago, before Chris was born, there were, there was an attack on one of the pick, one of the early pick micros and it involved pulsing the programming line voltage high or it was the power rail or something. You would actually pulse it high and it would bypass and it would allow you to bypass the encryption on the, on the firmware. Like, no, it allowed you to bypass the bit that the security bit, that's it. So it allowed you to bypass the security bit and actually read out the firmware. So you'd like pulse the chip and then you'd be able to read the firmware just straight back out, even though the security bit was set. And I, at least happened on the pick.

**Colin O'Flynn:** Yeah, there was a guy, I forget his last name, but he, he had a PhD thesis, I believe on the topic of bypassing protection on microcontrollers and he was using a lot of that. So he did some of the AVRs, the earlier AVRs as well. Maybe that's where it came from. Yeah, and the PICS I know and possibly some other ones, but.

**Dave Jones:** Yep. Yeah, I think there were some others as well and it was quite a common technique and I think at the time it was all the rage and everyone was going out trying to pulse these micros seeing to, seeing if they could actually bypass the security bit on them and yep, I think a lot of people had some success. And I think some of the, I think there was one manufacturer even came out and actually said, oh, our chip is, you know, pulse protected or something, you know, it can't, you know, this sort of attack can't happen on our chips. It was like a selling feature or something. So.

**Colin O'Flynn:** Seems like they're just painting a target, right?

**Chris Gammell:** Yeah. Come and get us. Can't break us. Oh, oh, oh really? Yeah. Really? We'll just measure your power rail.

**Dave Jones:** You're gone ski, dude.

**Chris Gammell:** So, so Colin, what, is there any way to actually, I don't know if you're maybe not allowed to give away these secrets, but is there any way to. Of course he is. It's all over. Oh, it's true. Good point. Is there any way to actually protect stuff? I mean, like, so, okay. So we have listeners who are developing embedded projects. Is there a legit way to actually protect it against, you know, this kind of attack or other attacks?

**Colin O'Flynn:** Yeah. That's always the question. So to be honest, I don't do that side as much. I'm more on the attack. But yeah, that's the easy way. Just tell us all the ways it can happen and then we'll avoid using those. I score goals. I'm not a goalkeeper, right?

**Chris Gammell:** Yeah.

**Speaker ?:** Right.

**Colin O'Flynn:** But yeah, there is, I mean, as I mentioned, using the physical devices designed against this is one of the better ways. So most of the main manufacturers make secure devices that are designed not to do this. The downside is most of the time you need to sign NDAs and stuff like that. You can't just buy them a digi-key. Yeah. So if you're stuck in the software side, there is a good book on attacks on smart cards, and it talks about a few of the countermeasures. Most of these countermeasures end up being breakable or broken at some point. So, you know, it's not a sure thing. And a lot of it just becomes, you know, what's your threat level that you really care about that is worth doing? And to some degree, the answer is always going to be, you should think about, you know, what if someone can break it? Yeah. So you should be using separate keys everywhere, stuff like that, and figure out a way to make it work. That's the better answer.

**Dave Jones:** Or just go, ah, couldn't be damned. I'm just going to open, make everything open.

**Chris Gammell:** Yeah, right?

**Dave Jones:** And then, you know.

**Chris Gammell:** Or just write everything in, like, Fortran. And it's like, no, I'm not going to bother. Not even worth it. Yeah.

**Dave Jones:** Still comes down to assembly language.

**Chris Gammell:** Yeah, no, that's true.

**Dave Jones:** Still can't. I mean, not assembly. It still comes down to machine code. Machine code. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. No, I mean, but these secure chips are the way to go, though, because they not only stop, like, you know, power rail attacks and software attacks, but they stop physical attacks, too. Like, they've actually got, you know, metal overlaid, you know, like barriers, physical barriers inside the chip that overlay the flash area and stuff like that. So even if you decap the chip, you can't sort of, like, laser probe it and all that sort of jazz, you know? So, yeah, it's not just the software or power pin side of things.

**Chris Gammell:** I still have some trouble. I mean, if I'm being honest, this is part of the trouble I had at DEF CON, too. I kind of just don't get it sometimes. Like, maybe this is the analog in me coming out. And I'm like, so why would people do this stuff? I mean, so I guess the commercial aspect is, you know, stealing stuff. And you also gave that example of, you know, I think the IoT example is actually really good for intercepting packets that you thought were secure. Are there any others that?

**Colin O'Flynn:** Yeah. A lot of this started with stealing satellite TV, right? That was, like, the number one thing for the longest time. And, like, people were doing, they were attacking chips with fibs, like, focused ion beings, the, you know, electron microscope type stuff. All for HBO, huh? Yeah.

**Chris Gammell:** And this is before Game of Thrones.

**Dave Jones:** Basically, all it comes down to is people just need to be able to steal something. That's it. Either they steal money or they steal content. Take your pick. But either one is going to be justification for doing this sort of stuff.

**Colin O'Flynn:** Yeah, absolutely, right? Like, it's crazy. They're stealing. I don't know how much it was back then.

**Dave Jones:** So they're either stealing content on their HBO channel, on their satellite thing, right, which is all the rage back in the day before it was done over the internet. And all they were stealing, you know, like a SIM card, you know, data, you know, so that they could steal somebody's card and, you know, use it to buy, you know, go to the shop and buy something.

**Colin O'Flynn:** Yeah, true. That's a big one now, right, too. I mean, smart meters with those coming out, stealing electricity, that'll be another thing.

**Dave Jones:** Oh, right, stealing electricity. Yeah, people sort of, yep, hack their smart meter.

**Chris Gammell:** Yes. I feel like so much of this stuff, though, like, so much of this stuff could just be handled by, actually not by the hardware side of things as, you know, as much as that's heresy. It's just like, you know, you could do it with SPC, you know, like statistical process control, where it's like, oh, well, Dave Jones was paying 80 bucks a month for electricity, and last month was $10. Right. Yeah. Maybe something's happening. Yeah. You know?

**Dave Jones:** They do monitor that sort of stuff. That's how they find drug dealers, actually. Yeah, I mean, yeah. Right? If a house suddenly goes from, you know, X amount of power per year, it suddenly goes to like a megawatt, you know, like 10 megawatt hours, they know they're running all these heaters up in their roof to actually grow all their drugs, you know, and stuff like that. So they actually raid them. And, yeah, there's actually, that's actually done. So, believe it or not, there's a lesson.

**Chris Gammell:** I mean, I guess there's always going to be low-level stuff that needs to be protected, though. But I guess I just have, I mean, I've always had trouble with this because I don't understand, I never thought about the attack side of things. So that's why it's been tough for me.

**Colin O'Flynn:** Yeah. I mean, the other thing is like the PlayStation and Xbox, right? People breaking those for, breaking the bootloaders to use.

**Dave Jones:** Once again, it's content again. Exactly. They don't want to run their own stuff. They want to copy the games. That's what they say in court when they dragged them to court. Why are you doing this? Oh, because I want to be able to run my own stuff on there. No. It's because you want to get the pirate of games, dude. It's got to be a financial incentive somewhere.

**Colin O'Flynn:** Yeah, exactly.

**Dave Jones:** Like some people just do it because they can, right? But yeah, there's going to be a lot of magnitude more people if there's a financial incentive to do it.

**Colin O'Flynn:** Yeah. Well, yeah, that's like the internet of things stuff, right? Too. You can, if you put a light network up somewhere that's unsecured, you know, some bored college kid is going to try to hack it, right? Just like play Tetraeus on the side of your building.

**Dave Jones:** Yeah. Yeah. Exactly.

**Colin O'Flynn:** All these threats, right? That people don't think of. It's that.

**Dave Jones:** Right. Never underestimate the tenacity of a nerd. Oh, yeah. Exactly. And yeah. So you're halfway to your goal at the moment. What is your, why was your goal 50,000?

**Colin O'Flynn:** So it was based on, there's a local fab I'm trying to order 1,000 units through. So sort of based on some of the money we have from selling stuff already, how much, you know, how much extra money we'd need more or less to order 1,000 was sort of what it was loosely based on. So that was about. Got it.

**Dave Jones:** And they're all going to be made locally in. Yeah.

**Colin O'Flynn:** Here in Nova Scotia. So there's a fab Sun cell we work with. Nova Scotia. Awesome. I actually experimented quite a bit with getting stuff made in China and stuff here and whatnot. And in the end, A, it's nice to support someone local. You know, everyone likes that. Support local. But yeah, it's cheaper by the time you work everything through. And there's no quality issues that I have. Yeah, exactly.

**Dave Jones:** And even if it's not necessarily cheaper, it's just less hassle. Well, yeah.

**Colin O'Flynn:** That's what, you know, I factor in a lot of hassle money there.

**Speaker ?:** Yeah.

**Dave Jones:** So if you can build that in, and because you've got a niche product, you can build that into your price. It's not like you're doing a Kickstarter for a new shield for the Arduino. It's going to cost $10, right? Where you'd have no choice but to make it in China because people expect a low cost. So for these niche sort of things, you can build that local factor into your price. Yeah.

**Colin O'Flynn:** And the other part of it too is, you know, it's a pretty complicated design in terms of there's a lot of analog portions to it and whatnot. So when you're going to China, they'll often just substitute, you know, whatever part is close enough to what you specified. Yeah. You know, like you specify these nice whatever capacitors. Like, ah, this is close enough. So having that local, it makes sure, you know, it's all legit parts.

**Chris Gammell:** It's what's 10 picofarads amongst friends. Yeah.

**Dave Jones:** That's why I so didn't send my microcurrent to China because it's got like a $4 resistor on there. Oh, that's not no way, right? And I don't want them going out to like, and yeah, they'll totally go out and source a $0.04 resistor, you know? And we go, no. Yeah. But that's the whole key to the performance of the product. Yeah.

**Colin O'Flynn:** Why did that with, I had some ADC boards made a bunch in China and I sent them SMA connectors because they would always just find, you know, some gold plated. Yep. You know. Yeah, yeah. Crap ones. Something like that.

**Chris Gammell:** This one was made out of granite. It was super, super low cost. Yeah, yeah. So, okay. So, you said you sent some over there. And so, like small runs, big runs, what was that experience like? I mean, what ended up happening with some of those? Did you have a bad experience?

**Colin O'Flynn:** No, I had an okay experience. So, like I did, I've done a few really small runs, like five or 10 units in China, which I actually found them cheaper than anyone local because China's NRE fee was like $100 or something like that, right?

**Dave Jones:** Yeah, right.

**Colin O'Flynn:** Because you could just have people placing the parts. Whereas here, that's not cost effective at all. They need to program the machines, right?

**Dave Jones:** Not my assembly here. I can just give them one board or 10 boards and they'll just hand.

**Colin O'Flynn:** Okay, are they reasonable or are they? Yep.

**Dave Jones:** What's that? Okay. Yeah, they're pretty reasonable cost. Yeah. Yep. So, and of course, if they just hand place them, then there's no, you know, there's no machine setup fee or anything like that. So, yeah.

**Colin O'Flynn:** Yeah. So, that's what was killing me is.

**Dave Jones:** So, for those sort of short runs, it works well.

**Colin O'Flynn:** Yeah. So, that was sort of my experience. And then they did substitute tons of parts. That was always the thing, right? It's like everything. Even connectors was the annoying thing. You know, you want nice-ish gold-plated connectors, but not a chance. What's that?

**Chris Gammell:** 30 mils of gold? How about gold flash? Yeah. Oh, not even right.

**Colin O'Flynn:** It's tin.

**Chris Gammell:** You're right. And just crappy.

**Colin O'Flynn:** It just doesn't feel as nice. So, it's like, yeah. Yeah. It's good for prototype and, I don't know, if you send them critical parts or stuff like that, that's been pretty successful, actually, for smaller runs.

**Dave Jones:** We had that at Altium, right? We were having our stuff made in Shanghai. And one of the assemblers substituted a header connector, you know, one of these surface-mount header connectors, right? So, we got these boards back and all these connectors were all melted. And all the pins were all at weird angles because the plastic they used in these headers was just so crap. That was actually chocolate. Yeah. Yeah. And I've got a photo of this, you know, just totally distorted connector after it went through the reflow process, you know. And, oh, it's just, yeah, thank you very much for that. Yeah. Unbelievable. Yep. So, some of the parts aren't just fake. They're, like, just totally crap. You know, they won't even survive a simple reflow, you know, basic stuff like that. Crazy. Oh, yeah. Hand solder, they will survive just fine, you know, because you're only heating up a single pin at a time, you know, the whole thing doesn't have time to come up to temperature and all that sort of jazz. So, it survives just fine, but not whack them through a reflow and it's gonski. Let that be a lesson to you, folks.

**Colin O'Flynn:** Yeah. Well, I had one board, too, come back with all of the, I think it was, like, the 10 nanofarad decoupling capacitors were inductors. Oh, nice. That was tricky to power it up, right? Oh, no.

**Chris Gammell:** Why is it all shorted?

**Colin O'Flynn:** Yeah, yeah, yeah.

**Chris Gammell:** Yeah, I just swapped them all in. There's some capacitance there. Yeah, yeah.

**Dave Jones:** I've had that happen. You go, yes, I found the short, I found the short. You power it up again, now there's another one.

**Colin O'Flynn:** And you just can't keep going. Well, when at first, you know, when you measure it out, then there's that moment where you go, like, oh, crap, did I short the PCB rails or something like that, right? Is this fixable?

**Chris Gammell:** And how did you find the one in Canada? I mean, it was just a local referral type thing?

**Colin O'Flynn:** Yeah, there's only one here, basically. You got one choice. I mean, there's one another, like, two hours away. But around me, that was it. So, I mean, you can, it's, there's a lot more across Canada, but it's nice having someone local. They have pretty good low volume prices and stuff like that. So, yeah, I was happy.

**Dave Jones:** I'm having a look at your board again. You've got a nice looking low noise amplifier on there. What sort of levels are we talking about on these power rail things that you have to analyze? Because you've got a 10-bit analog to digital converter at 105 meg samples per second. So, that's a bit of a beast. But you've also got a low noise amplifier coupled on the front end.

**Colin O'Flynn:** So, you're really measuring, like, you know, if you put a, I'll often use about a 50-ohm resistor across, if it's just a small micro, and you're just measuring the drop across that resistor. So, it's pretty small fluctuations. Like, you know, the constant DC power you don't care about, just the changes. So, something like, you know, 10 millivolts is pretty regular type levels. 10 millivolts at what speed, you said? Right. So, like, a couple megahertz? Yeah, I mean, the speed you measure at is a function, more or less, of the clock frequency of the device. Because, fundamentally, every point you care about is the clock edge, right? Like, that's when the lines are switching. Right. Got it, yeah.

**Chris Gammell:** Obviously, there's some issues with gigahertz resolution right there. Yeah.

**Dave Jones:** So, how much do you have to oversample? Say, with your 105 meg sample per second one, what speeds can you actually do?

**Colin O'Flynn:** Yeah, so I, the way, so this, the whole chip whisper thing, what makes it better than a regular scope for this work, is that you can input the clock, and it uses that as the sample clock.

**Dave Jones:** Oh, God, it's all synchronous. Yeah, it's all synchronous.

**Colin O'Flynn:** And, you know, it doesn't, like, you can put a clock into a scope, but it's got to be 10 megahertz, and stuff like that, right? Normally. Got it. So, this, you can put anything in. Got it. And it'll multiply it by, I often use it multiplied by four. And almost the only reason, you don't need to do that. You can just use one sample. But when you look at the waveform, when it's, you know, multiplied by one, it doesn't look very exciting. It's just like a line.

**Dave Jones:** Right.

**Colin O'Flynn:** Because it's one point. Yeah, yeah, right. Yeah. On each thing.

**Dave Jones:** Right. So, you can go up to maybe 25 meg with a decent amount of.

**Colin O'Flynn:** Yeah, like, 25 meg's no problem. Room in there. I mean, you can do times one. So, if you're, I've attacked. Right. So, you could go up to a happen. Yeah, and you can even do some under-sampling stuff. Like, the actual frequency, the bandwidth that you need is pretty small. Typically, like, 20 or 30 megahertz of bandwidth. Right. So, yeah. So, like, some people will actually use just a down converter, like, standard SDR type down converter to measure, you know, gigahertz devices running encryption. And they just down convert it and sample, you know, 10 megahertz of bandwidth or whatever. They need.

**Dave Jones:** Right. Does the synchronous sampling have any other advantages over using a scope?

**Colin O'Flynn:** No, it's primarily that you're getting, you don't need as high a sample rate because you get on every clock edge. Right. Got it. The issue that people run into is they use these really fast sample rates. And really, the only thing you need is the moment, you know, the device starts the encryption to the start of the sample block. This is sort of this random jitter. Like, if you have an asynchronous scope, you know, it could be whatever.

**Dave Jones:** Does the amplitude matter? Or are you effectively getting the digital output, really? If you know what I mean.

**Colin O'Flynn:** Like the amplitude of the power signal, you mean? Of the pulse.

**Dave Jones:** Yeah. Yeah. The amplitude of the power glitch. Does that matter? Are you, from the amplitude, are you able to differentiate between one, oh, it just moved data to the X register or moved it to the Y register because this is higher amplitude. That's why it has, like, the 10-bit, so higher bits is better. Right. Okay. Right. So, that will keep our esteemed colleague Chris happy here because it's analog domain, dude. There you go. It's all analog. Yeah. It's not just digital. Oh, yeah. Lots of analog. Hacking. It matters.

**Chris Gammell:** Well, yeah. Lots of analog, but you still got to script this thing in Python. Yeah, yeah. So, ugh. Yeah, FPGA is Python. That's software. Oh, I love that. No, no. I love FPGAs, but I don't know. Something about Python.

**Colin O'Flynn:** It's too easy. That's probably it, right? Yeah, yeah. It feels like there should be more.

**Dave Jones:** Except we have no clue how to do it, so we just love it, you know.

**Colin O'Flynn:** You should try. It feels dirty when you use Python. It's just like, you know, there's no, like, it's not an int. You just assign variables. Yeah. It's like, if you think something should happen.

**Colin O'Flynn:** Semicolons. Screw you, semicolons. No, you can put semicolons in, and it doesn't care. That's the best part. Because I always put them in, because I'm writing C, and then switch, right? And so I'll look back, and it doesn't even give you a warning or anything. It's just cool. It says, you know what? I know what you need. Yeah.

**Chris Gammell:** It's like the dude of programming. Yeah, yeah. It's like, just, yeah, man. Yeah, whatever. Chill out, man. No big deal. Chill out. Just make sure you get your white space right. Yeah, yeah. It's OCD.

**Dave Jones:** So what happens with chips with building clock phase lock loops that actually, you know, like it uses an external crystal, then it's bumping up to 400 megahertz inside the chip.

**Colin O'Flynn:** Yeah. So if you want to do the synchronous, there's sort of, there's, you know, a few options. One is you can just use a PLL yourself externally. So the full chip whisperer hardware does have a PLL. And inside the FPGA, there's some configuration that's built in to let you do that. So if, you know, you need to multiply the clock by some arbitrary amount, you can do that. Or the other option is you can do basically clock recovery. So if you're using a totally internal oscillator that, you know, a lot of smart cards will do this. They have their own internal oscillator. To help desynchronize stuff. But you can just, you know, in communications, clock recovery, they use all the time. So you can build a circuit that just pulls the clock out. Typically the strongest harmonic and then uses that to do the sampling.

**Chris Gammell:** Can I ask a dumb question again? Sorry. Can I ask a dumb question? What is a smart card? What is a smart card?

**Colin O'Flynn:** It's like, you know, credit card with a chip and pin. If you do. Do you have a chip and pin?

**Chris Gammell:** Chip and pin is not big in the States. I just got. This is American.

**Dave Jones:** That's a back way. People are still buying their groceries with checks. Yeah. No, seriously.

**Chris Gammell:** The discount grocery by me does that. And it's always a long way. No, I literally just got my first chip and pin card today. Wow. It's stupid, right? So that. Thank you. Thank you. That's the one. I didn't understand that. That's, yeah, smart. Yeah. Okay.

**Dave Jones:** All right.

**Colin O'Flynn:** Yeah, smart to smart, Kevin.

**Dave Jones:** Now, what was I going to ask? Oh, something just occurred to me. How you could possibly avoid having your product attacked in this way. What if you had a spread spectrum clock, random spread spectrum clock powering your product? Yeah. So I mean. Would that cause, would that screw up your thing completely?

**Colin O'Flynn:** So if you do the clock recovery on that, it's still, so there's one example I have where I program an AVR to like, it uses the internal oscillator and then switches it between like four to 12 megahertz. It's spreading over this huge range, way beyond what you legitimately should do. And yeah, no, it's fine. Cause you can do the clock recovery on it and you can do that in software. Yeah.

**Dave Jones:** Yeah. I was going to say, yeah, you could, you're part of your firmware. You could switch always constantly and randomly switch the internal clock to different frequencies. Boom, boom, boom, boom, boom. Yeah.

**Colin O'Flynn:** It complicates things, but it's not. So actually that's not a bad idea though, right? If you want a simple thing to do, but.

**Dave Jones:** There you go. There you go. Folks. Simple technique is to randomly adjust your internal clock. If you're the exact clock rate, it doesn't matter.

**Chris Gammell:** Of course, troubleshooting other problems would be a hell of a time, right? My spy line is just a mess, but yeah, I'm super secure. Right.

**Colin O'Flynn:** No, I mean, I think some smart cards do that too. Like, and they'll have multiple clocks. They'll switch between so that you don't necessarily know which one the crypto hardware is running off, you know? So they have all the clocks running at the same time or different phases on them.

**Dave Jones:** Ah, nice. Yeah, yeah. Jumping between phases. Yeah.

**Colin O'Flynn:** Dealing with timing on that. Like, you know, that gets crazy.

**Chris Gammell:** The digital side. I think someone who's already at the point where they're like, all right, I'm going to sit down and I'm going to be side channel attacking this card. They're not going to be like, oh, they switched one frequency. Guess I'll go get a sandwich. I guess I'll pay for my TV. Yeah, right? It's not like they're just going to be giving up. It's just a matter of time kind of thing, you know? Yeah. So I wanted to go over the hardware as well. So we know there's an FPGA on board. Is there a place where I can see the hardware or a good place to look at this? Like just the board, you mean? Or a schematic? Yeah. Just a schematic.

**Dave Jones:** There's lots of great photos on the Kickstarter.

**Chris Gammell:** There's lots of great photos on the Kickstarter. Sorry, I was on the Hackaday.io page.

**Dave Jones:** I'll go to the Kickstarter. Oh, no, no. That's the old.

**Colin O'Flynn:** Yeah, I think I put one photo of the new one, but I haven't updated. It fully. Actually, yeah, there's a whole breakout of everything that's on it on the Kickstarter. Yeah, okay.

**Chris Gammell:** And so also, can you explain the difference between the old and the new one? So what has changed between the light and the normal?

**Colin O'Flynn:** Yeah, so the normal one, some of the background of the normal one, I wanted people to be able to build it themselves. And to do that, I used an FPGA module that had the BGA FPGA on it so that they didn't have to do that soldering. So one of the objectives of this one was to make it cheaper, which meant making it on one board, and to keep it hand-assembled, switching to a TQFP FPGA. The only TQFP FPGA is small. So the LX9. Yes, I know. The LX25. One of our pet gripes here on the end. Yeah, so anyway, I switched to that. To do that, it drops a few features that a lot of people don't use. Primarily, the old system can trigger on an analog pattern. So it can say, like, here's a pattern of, you know, when the encryption happens, look for that pattern real-time in the data and then trigger the capture. See, this one can't do that. It's missing. It's missing. There's some other stuff. Like, the old one had an external PLL. It had level translators. Those are removed to save costs. And the old one had a whole bunch of jumpers for the target device because, you know, it was designed to work with all sorts of stuff. This one just has one target device on it. You can still interface other stuff to it. There's a whole half that breaks away. But basically, it's taking it and making it, you know, one board, no jumpers. There's no through hole on it, so that saves a lot on the assembly cost. Yeah, so it's really just making it, you know, one board for training. And then you can use it afterwards. But where's the old one sort of developed?

**Dave Jones:** Do you have, like, full tutorials and stuff like that? That, you know, like, it comes out of the box. Does it run a tutorial to, you know, to teach people how to do this sort of attack?

**Colin O'Flynn:** Yeah, that's the objective. So right now, there's all the tutorials from the old one. And almost all of them work, you know, almost as is. There's different jumper settings and stuff like that that I need to document. But that's sort of the objective. You know, I warn people in the Kickstarter. It's not like, oh, if you've never used a compiler ever before, it might be a little tricky for you. Not impossible, but to get the most out of it. Risk and challenge. There will be code. Yeah, exactly. At some point. I mean, if you're doing this stuff, you should know what code is and how to do it. What's the point? I don't know. It just seemed cool.

**Dave Jones:** I've just started with my Arduino. And, well, I want to get into hacking 256-bit AES encryption, you know. Yeah. I just got my first multimeter. Will that help?

**Colin O'Flynn:** Yeah, yeah.

**Dave Jones:** You know. Right.

**Colin O'Flynn:** So, no, so that's sort of what it seemed for. Yeah, I did.

**Dave Jones:** Yep. Sweet. Well, I hope you get there on your target. You're almost, come on, people. Get one. Yeah. This is a very cool product.

**Chris Gammell:** So, who do you, Colin, who do you imagine would buy this that might not already be buying this kind of thing? Is it, you know, like fledgling security people, people who are already making embedded devices that should be worried about this kind of thing? What are you, who are you targeting with all this stuff?

**Colin O'Flynn:** Yeah, so it's a huge, huge market, to be honest. Because with the main Chip Whisperer unit, we've had, you know, everyone from hobbyists have bought it that just want to get into this more. And that's still an interesting area. So, you know, people going to DEF CON that are just interested in, hey, how does this work? Right. You know, obviously the embedded side is what I really want to target. But the whole point of the whole project is really to show people, hey, if you're doing security on embedded things, you should, you know, consider this as a real threat when you design your systems. Right.

**Chris Gammell:** So do you, so you imagine that, okay, so someone is making a new device that they want to sell, and then they should buy a Chip Whisperer, and then actually try a side channel attack to make sure that they can't break it without tons and tons of hassle kind of thing?

**Colin O'Flynn:** Yeah, exactly. Something like that. Or even just to learn. I mean, a lot of it's just learning how the attacks work. And then when you design a product, you'll have a rough idea, you know, how secure it is. You really don't have to do the testing for a lot of stuff you do. You just know, like, oh, this will be totally breakable. But you might not care. Right. It might be like, well.

**Dave Jones:** Of course.

**Chris Gammell:** Yeah. You should go, like, hack a nest or something like that, just so that people sit up and pay attention. Yeah.

**Dave Jones:** It's like, oh, hey, maybe my thermostat should be dumb. That would bring a lot of, that would go straight onto, yep, all these social media sites that would go viral if you had a video that, like, let's hack the nest. I can turn somebody's house into a furnace, you know. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** That would, uh.

**Chris Gammell:** Right. It's got to be done. Send it a thing from the street to turn on the air conditioning in the winter. That'll show you. Yeah, seriously. You and your fancy design.

**Dave Jones:** Let's bring this half a billion dollar company to their knees. Oh, yeah. Awesome. Sounds good.

**Chris Gammell:** So, there is, so there's an FPGA board and then what was the other one, a SAM 3? Is that right? Yeah. So, I'm using a SAM 3, Atmel SAM 3 for the high-speed USB.

**Colin O'Flynn:** And. Is that an older chipset? What is, that sounds familiar. It's old enough that I was going to order a dev board and then I was looking through my stockpile and I had one and I didn't even know. Yeah. Because it was from like four years ago, some project, right? So, all right. But. Yeah. It's a pretty basic high-speed USB chip. You know, there's other people were asking, oh, why don't you use an LPC one, I think. There's a bunch of them that have this. But basically, I use the external memory interface and just memory map the FPGA registers right into the.

**Chris Gammell:** Ah, that's nice.

**Colin O'Flynn:** Yeah. So, it's really easy to do data transfers and stuff. I just point the USB at the FPGA and do that. So.

**Chris Gammell:** Okay. But now the critical question, what happens when someone uses a chip whisperer on a chip whisperer? Because you just have that memory line exposed. Yeah. Well, it's all open, right? Because it's already open. Wasting my time here. That's funny. Yeah. Well, it's cool. I think this is. And so, you teach classes as well, right? I mean, so you will actually teach people how to use this thing or how does that work? Yeah.

**Colin O'Flynn:** So, I've done training. I did a training last year at Black Hat as a two-day embedded security training. And I'm running one again for a company. In a few weeks, I've got to make some more material for that. And yeah, I plan on running training courses, you know, if there's interest more or less.

**Dave Jones:** I was going to say, that's a good place to make your money. Yeah. And that's the thing.

**Colin O'Flynn:** That's why I can do open hardware.

**Dave Jones:** You can do security consulting. People pay big. Companies pay huge dollars for this. Oh, yeah.

**Colin O'Flynn:** And the funny thing I learned is that I can put everything online. I can put all the tutorials online. And people will still, big companies will pay for, you know, a two-day training. Yeah, yeah. I can tell them. I'm going to use this material that's free.

**Dave Jones:** That's available for free. I'm literally going to be reading off my website. But I will happily charge you $1,000 an hour to come talk to you. Yeah, yeah.

**Colin O'Flynn:** But no, you know, people have training budgets and stuff like that.

**Dave Jones:** And they just, no one has time.

**Colin O'Flynn:** If you say, read this, you know, no one's going to do it. If you say, come to a two-day training, they'll learn. There's coffee. I know that. Yeah, yeah. That's right.

**Chris Gammell:** So, that's gone pretty well so far, though. I mean, like, I mean, what is the profile of people that are taking that kind of training?

**Colin O'Flynn:** So, really, the one, Blackhead, it was pretty random. A lot of people doing embedded stuff. But there's been, you know, there's whole fields I didn't really think of. Vehicle stuff is pretty popular right now, in fact. Because, you know, people are, apparently, it's a big threat model, right? Of attacking cars or cloning modules and stuff like that. But, yeah, it really varies. Like, there's no one group.

**Chris Gammell:** You know, that's the one thing I got out of it. So, I mean, DEF CON was weird for me. But the one thing I got out of it was kind of like, you should probably be afraid. You know, it's not because, like, oh, the world's coming to an end. But just because it's not something that people think about. You know, like, it's not, like, stuff that, you know, like I said, I never think about this stuff because I don't do embedded. But also because why would people even bother with this stuff? But then you start thinking about high-value targets, stuff like that. Cars, like you said. I mean, I think about industrial applications especially. There's a lot of vulnerabilities there. And for years, you know, embedded has just kind of gotten away with security by obscurity or by having no interface to it. And then now everybody wants to put the Wi-Fi module or Bluetooth module on something and it's just like, well, good luck with that. Oh, an IP address on everything? Well, guess what that means? It means that, you know, grumpy, grumpy dude in his basement now can access it from 10,000 miles away.

**Colin O'Flynn:** Well, that's what I tell people. It's like if I was buying a house, I would definitely want light switches wired, right? Don't give me any of that Internet of Things, whatever.

**Dave Jones:** None of that Nest rubbish.

**Chris Gammell:** Nope, nope. Are they really not wiring houses these days?

**Colin O'Flynn:** Well, that's what they always, you know, when we were doing our Internet of Things, low-power wireless, they said like, oh, we're just going to run power to every light. And then the control will be wirelessly and you can just stick a light switch anywhere. I don't know if they did it ever, but I've heard that so much. Yeah. I just assumed someone did somewhere.

**Dave Jones:** It's stupid. You can't beat a switch. It's just always there. In 50 years' time, it's still going to work. You know, like people are in houses a long time, you know? It's not, ah, unbelievable.

**Chris Gammell:** Well, I think, I mean, it's okay to have like brokered systems where it's like both, but you always need a fallback, right? It's just like, even if the fallback was, okay, so now you have like a, you know, a system where it is wirelessly controlled. Have the default be on. That's fine with me. You know, you can turn off the circuit record. You know, like, but like, yeah, it seems like some of these, like from a system design perspective, some of that stuff is just like, I don't know. Yeah. You said you've done like IPv6 as well. Does that, does that end up changing things for the whole IoT space or security stuff at all or no?

**Colin O'Flynn:** A little, I mean, with the IPv6 and IP, people are running, you know, some sort of IPsec or something on top of, on top of the lower layer protocols often that will add security onto it. But at the end of the day, you're still are running some sort of encryption algorithm on these small nodes. So there's still attacks you can do against the public key encryption implementations on the end node. So there's still lots of attacks available on it. You know, it might not be the AES at the lower layer. It might be some other layer.

**Dave Jones:** Where can, where can people, Colin, where can people follow you? Do you have a main website? I know you've got the.

**Colin O'Flynn:** Yeah, I have a.

**Dave Jones:** You've got like a GitHub thing. You've got a, you've got the Kickstarter page.

**Colin O'Flynn:** Yeah, I have my own website. Where's all your stuff? Colin O'Flynn.com. Easy to remember. Yeah. Duh. But yeah, it's, I don't know. I'm not very good on the whole, you know, Twitter and social posting project. So I do have a few things there, but yeah. Twitter, maybe.

**Dave Jones:** What's your Twitter handle?

**Colin O'Flynn:** Colin O'Flynn.

**Dave Jones:** Colin O'Flynn?

**Colin O'Flynn:** One word.

**Dave Jones:** Yeah. Too easy. And that was available. Somebody hadn't stolen it.

**Chris Gammell:** No. Luckily, right? That was the. Well, until they do a side channel. Yeah.

**Dave Jones:** That's all you.

**Colin O'Flynn:** Oh, the longest time, like, CO Flynn was widely available at the beginning, but then a lot of Ireland started to get on the internet, it seemed, and that just killed me. I love it.

**Dave Jones:** Well, thank you very much for joining us, Carl.

**Chris Gammell:** Oh, thanks for having me. Yeah, definitely. And people should definitely check out the Chip Whisperer Kickstarter. For sure, we'll link that in. Yeah, absolutely. And if you have, if you're developing an embedded project, you probably want to try this out. You definitely want to get a Chip Whisperer and make sure that your device is secure. So I would definitely recommend going to check that out.

**Dave Jones:** You should just have it in your kit just in case you might need it one day.

**Chris Gammell:** That's a good point, too. You should buy two probably. As a recommendation.

**Colin O'Flynn:** Just as a... Right. Or 10. You know, whatever. There is a 10 pack there, conveniently. I saw that, yeah.

**Dave Jones:** Oh, okay.

**Colin O'Flynn:** I thought you weren't allowed to do that on Kickstarter. They always change the rules, right? Now you can do up to 10. Do they? Okay. Because originally it was nothing. Oh, right. Okay. Yeah.

**Dave Jones:** And then they changed it and then it's right. It's back to 10. Yeah.

**Colin O'Flynn:** So, you know, if you're in a classroom or something, universities sometimes want a bunch for a lab.

**Chris Gammell:** Got it. Yeah. Awesome. Thanks, Cole. Thanks, Colin. All right. Thanks, guys. Talk to you soon. See ya. See ya. See ya.

**Chris Gammell:** See ya.

**Speaker ?:** See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya. See ya.
