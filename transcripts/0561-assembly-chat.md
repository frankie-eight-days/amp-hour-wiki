---
episode: 561
title: Assembly Chat
url: https://theamphour.com/561-assembly-chat/
---

**Dave Jones:** This is The Amp Hour Podcast. Released October 10th, 2021. Episode 561. Assembly Chat.

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. And I'm assembling a board because I put down solder paste right before we were supposed to record. I was like, oh, I have to assemble during the Amp Hour. So I was like, all right, I can make this work. This is like you're sitting and you're listening to two coworkers BS in the lab while one of them is assembling a board.

**Chris Gammell:** And the other is just annoying the hell out of them while they're trying to do it. But like, we're okay with it. I mean, yeah. Right. Yeah, no, of course. Yeah, yeah. Yep. Yep. Okay. So you think this is a good idea. So I assume. I mean, it might be a bad idea. Right.

**Dave Jones:** Let's be honest.

**Chris Gammell:** We'll find out.

**Dave Jones:** I might get really distracted, but maybe no more distracted than when we, you know, are looking on the internet to try and find a link. Got it. You know, throughout the show.

**Chris Gammell:** All right. So I assume that you have a PCB in front of you. You have a printout of the overlay. Do you have the schematic? Huh?

**Dave Jones:** I have three PCBs.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah, I'm doing. Right. I'm three to one. I don't use a printout anymore. I use Interactive Bomb, which is a great plugin for KeyCad. Oh, right.

**Chris Gammell:** You've got that plugin for KeyCad that does the thingo. Yep. Yep. So can you mark them off as you go?

**Dave Jones:** Yes, you can.

**Chris Gammell:** Oh, okay. Right.

**Dave Jones:** Yep. Yeah. So that's nice. Yeah. The really cool thing about it, what I actually found out for a client a while ago is that it's just like literally it's just I bombed at HTML, right? So whoever the author of this created this with like JavaScript and it's just a single file. And so you just double click on it, opens in a browser, whatever. Really cool though. I was like, I wonder if you can, or maybe I actually saw it on Twitter, but I ended up uploading it to my website. And then I put like a Apache, I think it was Apache or Nginx, like one of the web servers, like passwords in front of it. And so basically I had the client's like bomb available. And it's like, it's really cool because you can even, so that they could then go and see it. And this is an open source project anyways, it just wasn't released yet. So they were ready with it. Okay. And then you can actually like go through and like see the whole bomb, but even the newer version even has like traces. So you could, in theory, you could go and search for a trace and do troubleshooting like that too.

**Chris Gammell:** Right.

**Dave Jones:** Which is pretty cool. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Awesome. Yeah.

**Chris Gammell:** Excellent. Just like Paul Daniels interactive board view thing that. I don't know if I know that one. Lewis Rossman famously uses it in his videos. He, he, that's how he, uh, debugs all the Macintosh computers. He actually repairs. He's got this board view software written by Paul Daniels. He's an Australian guy. And he wrote this software to load in all these pirated schematics from Apple, all these, you know, cause Apple don't actually.

**Dave Jones:** Right. Right. It's not like they're, they're handing them out or anything like that.

**Chris Gammell:** No, it's not like they're handing those out. Yes. They have leaked out. I think they are official Apple schematics, but they're, yeah, they're actually leaked them out.

**Dave Jones:** Yeah. They're verified.

**Chris Gammell:** Yeah. Yeah. They're, yeah. They're actually leaked out. Someone at the factory leaked them out. Right. And anyway, you can get hold of these in various ways. Yeah. So he wrote software that a very cool software that imports the schematic and then overlays it with the board image. And then you troubleshoot, like you actually click on a bit and highlights the trace that goes all over the board and you can actually trace it down exactly. You know? So that's how I was able to do very efficient repairs to Apple max and stuff. And it's very cool software. Yeah. So, yeah. Yeah. So if you're in the board, if you're in the board repair business, like that would be the essential tool, you know? Yeah. It's just, yeah. Trying to do a troubleshooting with no schematic and no board layout is like, yeah, not that great. It's like you would eventually get to realize that, oh, yeah, there's supposed to be 3.3 volts here, but I don't really know what it does because unless you're a reverse engineer, the whole bloody thing, you know?

**Dave Jones:** Right. Yeah. It would really, really slow things down, right? You would just be like kind of, or just removing random components and you just, it would be a bad time. Yeah. No.

**Chris Gammell:** It's having the PCB schematic is, yeah, much better. So that's, yeah, yeah, it's cool. Cool. Does that tool though, does your tool tell you, like, cause really, like if you've got a bunch of 10K resistors, you want to place those all at once. You don't want to go, oh, one 10K. That's right. And then go do another one. Does it tell you where all the one particular part is?

**Dave Jones:** Yeah. I feel like I should just try and upload this while we're talking here. But yeah, it does. It groups them all by component. Right. Okay. Value and MPN. You can basically select it when you generate the bomb. Okay. I think it works for Eagle too. Or it did at one point or I don't know. I remember it not being just for KiCad. So. Right. It is by far like, you know, when I talk about like extensible systems and stuff like that, and I'm excited about like the scripting that's available and the plugin ecosystem. Like this is, this is almost always what I'm talking about. I mean, there are other very good examples as well, but like, this is just, I don't know. This is something that is like a very classy, useful software that just happens to be open source. And like, I don't, I haven't just, I mean, like Altium must have something like this, right? I don't, I don't know what it's like.

**Chris Gammell:** Oh, it does. I don't know. Well, no, I think it does now. It didn't when I was back at Altium.

**Dave Jones:** Oh, got it. Got it. Yeah.

**Chris Gammell:** It kind of, well, no, it had like a cross probing thing so that you could cross probe and stuff like that. But I, I think it might have something like that now, but I don't think it's, it's as good. So don't quote me on that. Cause I'm two versions behind on Altium. So I don't. Sure. Yeah. Yeah. Yeah. I don't use it enough these days. Yep. Yep. I don't keep up to date.

**Dave Jones:** So it's pretty cool though. I can also talk through some of the things that I've been finding on this board as I, so I've already gone through, I had, I assembled the first one, did the troubleshooting. And now I'm assembling based, based on the fixes there. One thing that I, the part I'm on right now is actually, it was a, a common, I don't know if it's common. You can tell me this, I guess. It was a 10, 10 microfarad capacitor that I had on the board. And I just didn't pay close enough attention to the voltage rating. And I've got a boost converter on this thing that goes up to 24 volts and I've got 16 volt capacitors. And I was like, well, that's not going to work. That's going to ruin your day. Yeah. That's right. Yeah. That's going to go pop, pop, pop. Yep. Yeah. Pop goes the weasel.

**Chris Gammell:** Cause most small ceramic capacitors are designed for like low voltage, like, you know, six or 10 volts, something like that. Like, especially the large value ones. Right. Yes.

**Dave Jones:** Well, and this, this is a 1210. So I definitely, you know, I, I knew to go big, but I just didn't order. I didn't order. I think it was when I actually went to the actual order stage. I either didn't market, you know, like in Kaiket, it's not tied to the actual library, which, you know, some people don't like and that's fine. But I make that decision when I go to, you know, put all the bomb together. Right. And, uh, uh, that did not go properly in this case, you know, it's fixable, but it's like, if I didn't catch that, it would have, I didn't, I didn't burn anything up, but I definitely caught it the last time I was assembling.

**Chris Gammell:** Okay. So it actually worked with the 16 volt cap? No, no, no. I'm saying I caught it before. Oh, you caught it before you did it. Okay. Right. Yeah. Yeah. Yeah. And how did you catch it? Cause these capacitors don't have any markings on them.

**Dave Jones:** Uh, I was worried about, it was when I was assembling, I was like thinking about, I was looking at this trace. It was like a big trace for a higher voltage. I guess high voltage doesn't matter, but it's, you know, a power trace. And so I'm like looking at it, I'm like, isn't that going to go to 24 volts? And then I was like looking at tracing it around. I also know another thing on this too. Like it's a, so it's a boost converter, but like, I'm like staring at this thing and I have a huge loop, like a feedback loop to go from the output back through the feedback network to the controller. And I'm like, well, that's wrong. You know, you know, you're supposed to keep that really tight there. And like, uh, yeah, it's just, it was not late. I must've laid it out really fast.

**Chris Gammell:** And I was going to say who actually, I thought you were the one who designed it and actually laid it out. I am. Yeah.

**Dave Jones:** Right. Well, you know, past me though, you know, like, I can blame that guy. Right. Yeah. Of course. Great. No. So yeah. Yeah.

**Chris Gammell:** You know, there you go. Trapped for young players. Are you the type of person who gets anal retentive about which orientation your parts are like all of the resistors, the, all of the values must be in the same orientation.

**Dave Jones:** No, we've talked about. Yeah. Cause I remember you saying that you like to do that. Oh yeah. That's actually really useful when it's assembly time. Usually. And this is such a big board. Like this is a sizable board. So it's right. I definitely have the space for it, but I'm just not in that mode. You know, you're usually in that mode though. Like you're trying to do that. Right.

**Chris Gammell:** Oh yeah. I, it's just something that I feel that. I don't know. I just want to do it. Like it's like, it's going to be important. Like when, when you're staring at a board and then you're checking it afterwards, you know, you don't want to have to flip it over 20 times. Right. So it's like, because when often, when you get the resistors, right, you'll like, you'll actually peel them off the tape and they'll be on the thing and you'll pick them up at oddball angles. Right. So it's like, you know, so it's very tempting to put it like it, it, it's not like I've never done it. So, but it's, you know, if I'm in a real hurry, I will, but you know, if I've got the time, I will make sure it's rotated in the correct orientation. So they're all facing the same way so that I can go and just quickly scan the values and make sure they're okay. So.

**Dave Jones:** Yeah. That's, that's a good idea. I mean, I don't know. I've gotten, I've gotten into some maybe questionable habits. Like I definitely, I don't do silkscreen anymore. I'm just like, yeah, you know, I don't want to.

**Chris Gammell:** And is this a reflow board?

**Dave Jones:** Like this is definitely reflow. This is the oven that I talked about last time. Yes. Yes.

**Chris Gammell:** The oven we talked about last time. Right. Okay. So you've got your paste down and you're right.

**Dave Jones:** Yeah. Pasting at home. You know, I, so I've used that paste. What's it called? Like the, the jig, like a M hub where it used to be, they had like a jig with like, so you have a frame stencil and it's basically kind of hinged at the back of the stencil.

**Chris Gammell:** And the whole thing folds down and then you pull the arm forward and there's a big squidgy in there that. That's right. Use the paste over. Yep. Yeah.

**Dave Jones:** Yeah. I find that sometimes it's just easier to do with just a non, non frame. If you're not doing it professionally, like on a machine that the frame stencils are made for. Yeah. I find sometimes the flexible sensors, especially for small stuff, it's just easier to do that. No. Yeah. No. You know, simple.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. It's easy for those who don't know how you do it. You get a blank piece of PCB and then you just stick your stencil on top. And then you, and sometimes you will actually line that, you know, you'll line it up properly and, but sometimes you don't have to. And then that, that's the same thickness as the board. That's important to have it flat. And then you put it over, you line it up and then you just get your credit card or whatever and whack your paste on.

**Dave Jones:** Yep. Yep. You know, exactly right. Yep. Straight over. I took some photos of it. I was like looking at it. I was like, oh, I should probably not put my old credit card numbers in the shot.

**Chris Gammell:** Shouldn't, shouldn't matter, but still, you know. Yeah. Yeah. They can track you. Maybe. I don't know. Yeah. Somehow. Cool. Yeah. All right. Well, don't sneeze. Don't. What, what is the smallest part on there?

**Dave Jones:** These are all, uh, oh, 603. So this is, like I said, this is a huge board. Yep. And I have just, uh, successfully uploaded this. I'm going to try and send it to you. We'll see if I can get this to you in a timely manner so you can see it. Okay. I'm not going to share the, uh, the link with anyone else, but, uh, man, I'm too, my, my keyboard is too far away from my computer. And so as I'm trying to type my password.

**Chris Gammell:** I'm surprised that you can even send the link. Like that other people can view. That's really cool. So that's kind of like. Yeah. Yeah.

**Speaker ?:** Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Dave Jones:** Yeah. I mean, if, if we were like working together on a project, it'd be just as easy to do like a zoom link or something like that. Right.

**Chris Gammell:** But right. Okay. And then share, share screen or share screen. You can mark it up. That sort of thing. So cool. Bananas.

**Dave Jones:** Yeah. It is pretty cool. I mean, like, and it's a little bit more, it depends how wide you want to do it. Right. It could be, I could just, I guess I could have just sent you the file. That probably, actually that probably is the easiest thing to do. I'm just going to do that real quick. Uh, no, just, just send me the browser link.

**Chris Gammell:** That's easy.

**Dave Jones:** Well, I'm trying to do that, but I had to like, I'm trying to, I'd have to, I'd have to send it to, uh, I'm trying to send it up to my server right now. And so instead I just send it to you as a standalone file. Oh, okay.

**Chris Gammell:** Right. Okay. Yeah.

**Dave Jones:** Oh, I didn't know you could just send it as a HTML. Yeah. That's the thing. It's like an all it's, it's all inclusive there, right? It just kind of sits there.

**Chris Gammell:** But I wait, but with that, I won't be able to see you interactively live with it. Uh, I don't think there's actually a way to do that. Oh, okay. So you can't do that with the web link. So it's just. Yeah. I'm not sure you'd need to. Okay.

**Dave Jones:** I mean, I guess, I guess you could, I mean like, otherwise we could do like a screen chair and then, and then it would work. Right. Right. And you could see what I'm doing as I do that.

**Chris Gammell:** Oh, I can't, doesn't automatically open in my browser. That's dumb. What's going on here? Yeah.

**Dave Jones:** You might need to download it first. I'm not sure.

**Chris Gammell:** Yeah. I don't even know how to download it actually.

**Dave Jones:** Oh, maybe it doesn't like it coming through G chat. Yeah. Why are you sending someone an HTML file?

**Chris Gammell:** Yeah. I know. That's yeah. It sounds dodgy. Doesn't it? No, no. I think I got it. I think I got it. Okay. Okay. Yep. I downloaded it. Yep. There we go. Cool. Yep. Yep. There it is. Yes. Now I can interact with it. Okay. I thought I would be able to see you interacting with it live. Okay. That would have been way too cool.

**Dave Jones:** That would have been cool. I mean, I'm not sure. Actually, I'm not even sure what version I did this with. I don't know if this one actually has the traces. Full screen. Yes. This I have used before. Yeah, this does not have the traces.

**Chris Gammell:** Yeah. Yeah. You probably have, right? Yeah. Yeah. I've used it before and it's cool. I don't know why it's not integrated in the standard build. I'm not sure either. Like it's such a killer thing. I don't know why, you know, it's all open source. I'm sure the author wouldn't mind. I'm sure the author would love that it's integrated in the standard build. Wouldn't they?

**Dave Jones:** Surely. I don't claim to know anything about what motivations are around open source projects, you know? Right. That's right. Yep. Yeah. Okay. And sometimes I think it is better to be separate in certain ways, right? I mean, if there's money involved, it might be a little different, right? It was like, oh, you're not paying me enough.

**Chris Gammell:** But then you've got to work out push updates. I don't know how all that works and things like that. I mean, the maintainers of the key CAD build may have a different idea to the author of the plugin. And then they may, I don't know, fork it and go in different directions or something, you know? Yeah.

**Dave Jones:** Yeah. Who knows? Save feelings, save time. Right. Yeah. Yeah. Okay. Do it separately. Yeah. The only downside is that it's, you know, another step for people, but I think we've sufficiently said it's cool enough that people should do it. Right.

**Chris Gammell:** Does your board not have component designators on the silk screen?

**Dave Jones:** Yeah. That's what I was saying. I stopped doing that. Oh, sorry. Yeah. I don't do designators on the board anymore. I just don't, I can't be bothered, you know, for tiny stuff. I'm just like, I don't want to.

**Chris Gammell:** Wow. No, wrong. What? See, so you don't even put like R10.

**Dave Jones:** No. Yeah. You wouldn't even put R10. Oh, you said I was talking about values.

**Chris Gammell:** Oh, no, no. Both. Both.

**Dave Jones:** I think, I mean, I think it looks cleaner. I don't think most people need it. It's, you know, you could say it's for me.

**Chris Gammell:** Nope. Nope. That's a thumbs down for me.

**Dave Jones:** I always have this open though. No, that's fine. I mean, you know.

**Chris Gammell:** Yeah. No, but somebody else.

**Dave Jones:** I am the one who has to use this, you know.

**Chris Gammell:** Yeah. But if it's an open source product, if other people are going to repair it and stuff like that, it's nice to have. That's true. A component designator on it.

**Dave Jones:** Yeah, maybe. Well, you are welcome to submit a pull request. Which, if people don't know, is the open source way of saying, oh, bless your heart. Or also, screw you. Screw you.

**Chris Gammell:** I'm going to fix this crap.

**Dave Jones:** Oh, no, no, no. It's saying, you know, if you want to change it, you can feel free to go change it. But in the meantime, you can pound sand. All right.

**Chris Gammell:** Wow. Not even. Like, I can. Values is a thing. Values is, you know.

**Dave Jones:** I wouldn't do values. Yeah.

**Chris Gammell:** No. Values is nice if you want to actually have independent people repair it actually down the track. That. Sure. That'd be really nice.

**Dave Jones:** Well, I mean, this is like Apple. I'm like Apple, you know. Right. I want someone to make money on my repair. It's not absolutely essential though.

**Chris Gammell:** But yeah. Oh, man.

**Dave Jones:** No zero ohm resistors here, Dave.

**Chris Gammell:** What the hell? Zero ohm resistors. Yep. There are. I'm sure there's a component shortage on zero ohm resistors, is there? Yeah. No, there's not. No, there's not. You can still get zero ohm resistors.

**Dave Jones:** But I was looking at my stack of components, which I'm going to go dig through here in a second. And I was looking at my box of like microcontrollers and sensors and stuff. And I was thinking like, I could make some money right now. Right. Hoard. No. Hoard. Hoard. Hoard. Yeah. Hoard. Hoard. Hoard. Hoard.

**Chris Gammell:** Hoard your components. I'm telling you. Yep. Yep. Hoard.

**Speaker ?:** I don't know.

**Dave Jones:** I do wonder what that would look like. Like, are people just selling them on eBay? Are people actually selling them? Or, you know, are we just such pack rats that we're like, no. Well, I'll never do it. Oh, I'm sure there's people selling. I'm sure there's people selling. My cold dead fingers. Yeah, exactly.

**Chris Gammell:** Yep. Well, yeah. Well, it depends. You need to find a marketplace. If you're making a product, like if you've got a product that you manufacture, you're going to hodl those parts, right? There's no way you're going to sell them to make a quick buck. That's true. You're knowing that, you know, geez, these things, I need these things.

**Dave Jones:** Right.

**Chris Gammell:** Right. So, yeah.

**Dave Jones:** Liquid gold. Black tea. Black tea.

**Chris Gammell:** Texas tea.

**Dave Jones:** Texas tea. That's it. That's it. Texas tea. Yep. I'm not old. I didn't really watch that show. No. No, you didn't. No. Yeah. Even I did. A little before my time. Yeah. That was how you got a picture of Americans. Right. Yeah, exactly. Yeah.

**Chris Gammell:** That was my entire view of America. Yeah. That's okay.

**Dave Jones:** We have very specific views on Aussies because of the media as well. Oh, yeah. Of course. I know. Yep. Yeah.

**Chris Gammell:** Shrimp on the barbie. Yeah.

**Dave Jones:** That's right.

**Chris Gammell:** That's right. Oh, geez. All right. No. No. Sorry. Thumbs down for no component designators on the silkscreen. I mean, that's just lazy ass. I mean, for those who can't see, this is a big board. I like how it looks. Like this board is like 10% populated. Like this is not dense. It is not.

**Dave Jones:** This is not dense at all.

**Chris Gammell:** This is not dense at all. No, this is just. But don't you have to go to the effort to turn those off?

**Dave Jones:** There's a script in Kaika that you can just do everything at once.

**Chris Gammell:** Oh, okay. Switch them. Because I was going to say, if you went to the effort to individually switch each one or something like that, then yeah, that's just dumb because you might as well spend the time to actually place to drag each one. It's no effort to drag a designator. Goodness sake.

**Dave Jones:** Oh, man. This is a little judgy, Dave. I know. I wasn't sharing. I was sharing this to show you how cool this platform is. Not for you to. I was looking for an app. This is already made, man.

**Chris Gammell:** You didn't think I'd take you to task on that?

**Dave Jones:** My goodness.

**Chris Gammell:** Well, then why would you even.

**Dave Jones:** I will point to the latest board that you made. That's my scoreboard.

**Chris Gammell:** Why would you even bother labeling the damn connectors then? You know, RS-485. Well, that's for users. Power and boot.

**Dave Jones:** Most people who use boards are not the people that are repairing boards. Right. You know, most people are software. Well, okay. Yep. You know, cards on the table. This is for software people. This is. Right. Okay. Building this for. Got it. For other people. Right? Yep. And so.

**Chris Gammell:** Yep.

**Dave Jones:** You know, this is thinking about. They don't really care. And the ones that do care. I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** I think they have a little bit more leeway than I do. But I will also point out that Adafruit does not label their components. They also. They have more leeway. Really? Because obviously they make more boards and they're much tighter. So. They don't know.

**Chris Gammell:** You're saying no Adafruit boards have component designators on them.

**Dave Jones:** None that I've seen. That doesn't mean none of them do. But I think it's because Lamour pushed them on a different layer. And so they decided not to do that. I'm not sure why.

**Chris Gammell:** What a different layer?

**Dave Jones:** Yeah. I think it's. Oh, they're not the kind.

**Chris Gammell:** They're not the ones who put them under. Like physically on top of the component and then put it on a mechanical layer. Are they?

**Dave Jones:** I think it's something like that. I think. I think. I've only ever seen that. I think that might be it.

**Chris Gammell:** Yeah. I've seen a lot of projects like that and it's bloody annoying.

**Dave Jones:** Yeah. It's tough for, you know, like if you're pulling it in. For me, it was confusing because I was like, you know, using their board as a basis. You know, it's all open source and we love that. Yep. And I was using it as a basis for another design. I was like, where? I just couldn't even tell what was what. But also every time I open Eagle, I'm just so confused about how to manipulate anything. Right. You know.

**Chris Gammell:** Well, you're right in that most of their boards are like little. That's right. Yeah. Like micro-y hats. Feather form factor. Feather, you know, things. Like, yeah. No. And you simply can't add those. So, but that's. Yeah.

**Dave Jones:** They're much more of an excuse than I do.

**Chris Gammell:** Yeah. Oh, yeah. Yeah. No, totally. But there's no excuse on your board, dude.

**Dave Jones:** Well, I like how it looks. I have to say when I. The real reason I started doing it is because when I was doing 3D renders. And this is not a good reason, but this is the reason. Is it started when I was doing 3D renders and I needed to send stuff to clients. And like I said, most of my clients don't care. I'm the one who has to deal with this stuff. So. Yeah. You know, the actual building and the actual like troubleshooting. Yeah. Yeah.

**Chris Gammell:** But then you can turn it off in the 3D. Oh, no. But then you. I guess. So I'd have to turn it back on. It's a silkscreen layer. And then you turn off all your labels as well. So.

**Dave Jones:** No, no, no. So it's. In the 3D render, at least in KiCad. In the 3D render, you. When you turn. Even when you turn off the silkscreen layer, it will still show up in the 3D render. Unless you go and turn everything off.

**Chris Gammell:** Oh, really? Okay. That's. Yeah. I'm not sure why that is. Kind of a bit weird. That sounds. It is. Weird off the top of my head. Okay.

**Dave Jones:** Yeah. It's jarring because. Every time you like import a new component, like, wait, where did that silkscreen come from? Or, you know, every time. Every time you think you've. You turn off the layer in the actual layout. And then you go to the 3D model. You're like, oh my God. Where did all that come from? So. Yeah. So that's how it started. And then I was like. Well. Then I was making a couple small tight boards. Like the ABC board is pretty tight. And.

**Chris Gammell:** Yep.

**Dave Jones:** I don't know. I was doing 0402 stuff. And it's just. It's easier.

**Chris Gammell:** Okay.

**Dave Jones:** So.

**Chris Gammell:** Can I take you to task again?

**Dave Jones:** Of course. Amen. We got to talk about something here. Although usually. In the lab. When you're like chatting with a buddy. It's a little friendlier. I got to say. Yeah. Right. Okay. This is more like a boss. You've been to my labs. You haven't been to my labs. Right. Well, I have been to your lab. And it was very friendly when I was there.

**Chris Gammell:** Yeah. But you haven't. You know. Yeah. Been to a. Like where we're actually working on something. Mm-hmm. Yeah. Like. Right. You've got this large. What looks like a connector. In the middle of the board. Like. Is that a module? Or is that a connector?

**Dave Jones:** That's a. That's a. That is a. A feather. Actually. It's a feather landing pads. For basically a feather form factor. Dev board. Right. So it's basically to make.

**Chris Gammell:** So that solders down to the board.

**Dave Jones:** It's a silk. Sorry. It's a surface mount. Set of. Like a 16 pin. Yeah. 0.1 inch headers. Surface mount. And then a 12. 12 pin. Surface mount headers.

**Chris Gammell:** Right. Why do you have components under it?

**Dave Jones:** So there's. It's. It's. It looks like it's a single component. But it's actually two sides. So I did. I did the silk screen. So it's like. Like I said. It's a. 16 pin. And a 12 pin. Individual headers. And then. That. What really plugs in though. Is. A single board.

**Chris Gammell:** Yes. But. But those components are still under the module.

**Dave Jones:** Right. Yeah. But they're like raised up by.

**Chris Gammell:** Yeah. They're raised up. That's fine. But I'm talking about access.

**Dave Jones:** I'm talking about access. For probing. Let's see what's under there. There's a 1k resistor. There's a zero.

**Chris Gammell:** There's four resistors. And two capacitors.

**Dave Jones:** You can actually select. Can you select. Three. You can select them.

**Chris Gammell:** Three capacitors. I think. Oh. I'm not. It's. Yeah. Yeah. Yeah. No. There's. They're. Oh. They're large resistors. You've got large resistors.

**Dave Jones:** 4.7k. Yeah. So those are. Small resistors. Probably pull up resistors for. I squared C. Okay. So like there's a. There's a two pull up. Three pull up resistors for I squared C. That doesn't make sense. Because there would be. Oh. One is a pull up for a button. Okay. So two pull ups for I squared C. S-E-L and S-D-A. There's a. Pull up for the. Yep. Yep. The doot button. Not the. Not the boot button. But the doot button. People following on Twitter will know that. That's. Yeah.

**Chris Gammell:** I saw that. But I have no idea what that means. I'm sure it's a joke. Yep.

**Dave Jones:** Yeah. Alex Glow. Right. And. And. What else is under there? A 1k. Monster resistor. Right. Which I could talk about.

**Chris Gammell:** Why. Why are you mixing. Large format resistors. Large size resistors. With low. Small size resistors.

**Dave Jones:** The. 1k. Is because I ran out of. I was getting lazy. And I wanted to route signals. Through the 1k. Oh.

**Chris Gammell:** You wanted to route. Right. So you wanted a bigger part. Okay. That's right. Yeah.

**Dave Jones:** So that's like a 1210. Right. Okay. Resistor. Yes. And it wasn't going to be like a lot more for that. You know.

**Chris Gammell:** All of your 1k resistors are 1210s. Oh goodness. That's right.

**Dave Jones:** Yeah. Okay. Yeah. Because what I. What happened was I. I routed everything. And then I put LEDs. Don't tell anyone. Of this board I'm working on. But I put secret LEDs. On the front of the board. And so I needed to put 1k resistors. With every LED.

**Chris Gammell:** Yep.

**Dave Jones:** And then route all those traces. After the fact. And I was like. Oh. I have to redo all this layout. And I was like. No. Right. Okay. I can just put the 1k resistor. Over top of some of the big traces. Yeah. Yeah. Yeah. And then that just kind of made it a lot easier.

**Chris Gammell:** Okay. Fair enough. Yep. I can. I've. I've been there. Done that. I'm. Yeah. I mean.

**Dave Jones:** It's just like a sourcing way to get out of it. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm sure 1k resistors are now. You know. 1k. 1210 resistors are probably out of stock. Right. Because why wouldn't they be. But yeah. You know.

**Chris Gammell:** Fair enough. Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** All right.

**Dave Jones:** Other snafus on this board. So the 1210. Sorry. Not the 1210. The 12 and the 16 pin. Surface mount headers I put on here. When you use the surface mount 0.1 inch. You know. They have every other side. And for some reason. I always get it wrong. It's. You can't buy left foot forward. So. If you see at the end. It's always right foot forward. Yeah. And for some reason. Kaiket has both. Even though I've never seen left foot forward. And then I integrated that into this footprint. And so. I was left. Pulling. Pulling the legs. Out of. Innocent components. Yeah. Exactly. In the. Murderer. 180 degrees. I was more like a. Victor Frankenstein kind of thing. Yeah. I was like making a. Franken. Franken connector. For Halloween.

**Chris Gammell:** Torturing. Poor innocent components. Yep.

**Dave Jones:** Exactly. Christopher Gammel. That's right. Yep.

**Chris Gammell:** Exactly. Goodness. Yeah.

**Dave Jones:** Another thing that was going on here. So. I was going to put a. So this is like a. Agriculture board. That I'm building. Which I'm sure I'll be able to share it at some point. But. I wanted to talk about that a little bit too. Because. I was going to put a solar controller on it. Right. Right. Okay. Yeah. Yeah. Pretty. Pretty common these days. And then. To what? Charge a battery. That powers it. Yeah. Like a lithium ion. Or something like that. Right. Okay. But a tip I learned from. I think. Jeff Cavanaugh. I'm trying to remember. I think that's his name. But he's an Arctic scientist. So he does stuff that goes up into like. Yeah. Above the Arctic circle. Stuff like that. He's like look. If anything gets near zero degrees. You're screwed. Your. Your lithium ion just freezes up. Oh yeah. Yeah. Yeah. And it's either. It's either going to be broken. Or it's going to just not charge.

**Chris Gammell:** They have a very different battery technology. That's right. Sort of environments. Yep.

**Dave Jones:** Yeah. And so what he had recommended. Was to get a low voltage cell. And then a six. So I think it was like a six volt cell. Which actually goes up to like. Eight nine volts. And then you trickle charge. On a six volt gel cell. And then that's the input. So instead. I just made this. So that this just has. So you see external power input. Dave can see this. Everybody else can't. Yep. So I just did like. Off the shelf buck converter. That goes up to like. 18 volts. It's this like. Cool little module. With like the. Integrated. Inductor. In there. Again. Probably out of stock already. But I have some. So I'm good. And. Yeah. I don't know. I just. I had. I had not. I always thought that I was going to put like. Lithium ions. In. You know. In line. And then have chargers. But yeah. The solar stuff. It doesn't matter. In cold. You'd think. You'd think I would have learned about cold weather environments. In the past. But. Yeah. No. Learned it from. Jeff.

**Chris Gammell:** Cool bananas.

**Dave Jones:** You ever designed for the cold or no?

**Chris Gammell:** Oh. Yes. Yes. Oh. The ocean deep. Yeah. Ocean deep. But we knew. It couldn't go below. We knew it couldn't go below. Zero degrees. Well. No. No. Technically we could. Technically seawater. Can go below zero degrees. Because it's freezing point is not zero. Yeah. Yeah. Yeah. It's freezing point isn't zero. So. Yep.

**Dave Jones:** Yep. That's interesting. I guess you'd have internal heat from the. The electronics though too. Right?

**Chris Gammell:** Not necessarily. So. You know. But you can get. Lithium primary batteries that are very good. At lower. Yeah. At lower temps.

**Speaker ?:** So.

**Chris Gammell:** Okay. Yeah.

**Dave Jones:** Yeah. And that's the thing. Like I could probably go out and try and find something like that too. But you know. For this kind of thing. And the last time I was doing this. It just wasn't. Necessary. You know. Right. It wasn't like something that I. Had the resources and or time and or inclination to do. So. Instead I. Switched to this. Yeah. But. I had never experienced that before. So. Maybe if someone out there is listening. Is like. Oh yeah. I live in Minnesota. Yeah. Right. Yeah. Of course. I live in Norway. But I'd love to hear other. Other like. Like. Like weather based stuff like that too. Because. You know. Like solar. There's just. You know. Like. I feel like solar and a battery. Is always kind of the solution I see. And it's sometimes. It's just not. Going to work.

**Chris Gammell:** Right.

**Dave Jones:** So.

**Chris Gammell:** Yep. Now. I was. I was confused when I got a European car. It came with a battery. Warming. A warmer cover. Oh yeah. It came with like a little fur coat around the battery. And I go. What the hell is this? What the. Why? Yeah. I just. Like.

**Dave Jones:** Is there air conditioning inside this coat?

**Chris Gammell:** No. It's just. No. Just a little fur coat around the battery. To keep it warm. Yeah. From freezing in the middle of winter. And it's like. Yeah. Not really needed in Australia. So. You know. Yeah. Yes. Yeah. Anyway. So yes. If you want to know about lithium. Primary batteries. They can go down to minus 55. So. Really? Yeah. Yeah. Yep.

**Dave Jones:** That's pretty cool.

**Chris Gammell:** Yeah. So. You can't just say.

**Dave Jones:** They're not going to charge though. So. Because they're primaries. Right.

**Chris Gammell:** So. They're. They're primary batteries. Yes. Yeah. So. Yep. So. There you go. So. Yes. It's not. Like. You can't just say. Oh. Lithium batteries don't work at zero. You know. That's just not. Oh.

**Dave Jones:** I see what you mean. Yeah. No. I meant the charging. I mean. The charging was the main thing. But. Yeah. This is not a particularly battery optimized thing either. You know. Right. There's a. RS485 on here. 420 controllers. And just. Yeah. It's not. This is more industrial than anything. So. It's not going to be. This is not going to win any low power sippy awards anytime soon.

**Chris Gammell:** Right. Anyway. The one I was talking about was a lithium. Thionyl chloride.

**Speaker ?:** !

**Chris Gammell:** Battery. So. You can get those to. Yeah. Go down to.

**Dave Jones:** That sounds like. Very low batteries. Very toxic.

**Chris Gammell:** Well. It's a lithium inorganic battery. I think they call it. Inorganic. Inorganic. Battery. What does that mean? So. I. It's. Something to do with the thionyl chloride. I don't know. You've got to know your chemistry. I guess.

**Dave Jones:** Anything organic is going to die if it touches thionyl. Whatever.

**Chris Gammell:** Right. Yeah. Yeah. Yeah. Exactly. So. Yeah. But. Yeah. As I looked at in one of my videos for like a. What was it? Like a 30 year. Battery life multimeter or something. I. I. Did a video on. And I was like. Yeah. You can get batteries that last for. You know. Have a shelf life of like. You know. Exceed in a decade. Well exceed in a decade. You know.

**Dave Jones:** Mm hmm.

**Chris Gammell:** So. Yeah.

**Dave Jones:** Yeah. I think about some of the stuff. That's. You know. That's out there these days though. Like. Probably the most likely thing that's going to kill stuff these days is not like. I mean. Even if it's super battery optimized. It's like. All right. Is it getting firmware updates? Yeah. Right. Yeah. Yeah. If it's talking to the network. Is it still going to be able to talk to the network? Is the network still there? Like. I don't know.

**Chris Gammell:** Is the network still there? Speaking of which.

**Dave Jones:** Yeah.

**Chris Gammell:** Yes. Facebook. I completely come a gutter. Right. So some. Some idiot. I don't know. Pushed the wrong button on the network update. And it just nuked the entire presence of Facebook. I didn't notice. Because I don't use bloody Facebook. So. I did.

**Dave Jones:** Just because I was laughing at it all day long. Right.

**Chris Gammell:** Yeah. Yeah. It was great. But anyway. Yeah. The funniest thing that we. We both thought was the funniest aspect was not that it vanished from the internet. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Whatever. You know. It was the fact that they couldn't access their own server rooms because they. Their security. You know. Key. Key swipey card. Security system was controlled on Facebook servers. Yeah. So.

**Dave Jones:** I thought it was building access. But yeah. Well.

**Chris Gammell:** Building access. Yeah. But I heard it was like the server room or something. So. I don't know. Got it. Yeah. Yeah. So. Yeah. I mean.

**Dave Jones:** It's like one of those like systemic things. You know. Like everything's connected. It's all great until it's not. You know. Yeah. It's like.

**Chris Gammell:** You know. It's like if you design your own swipe access thing for your home. And then it's controlled via the controller. Which is inside your house. It's like. Yeah. You know. Yeah. If it goes down then you can't get inside to even fix it. Because like. It's just dumb. Right. Yeah. And you deserve what you get. Well don't worry though.

**Dave Jones:** It's like that. Yeah. That back window just pops right out. I have a really good security system. But then the back window pops out. That's right.

**Chris Gammell:** Everyone. Chris Gammell's house.

**Dave Jones:** Free to. Yeah. Right. Right.

**Chris Gammell:** No. Not this house.

**Dave Jones:** Different house. That was. That happened to your mic. Oh boy.

**Chris Gammell:** You want some. You want some feedback on that sort of stuff. Do a video on. I did a video. So my lab. My new storage unit downstairs. How I put a new lock on it. Right. I changed it to a lock to match my bunker. You've. You've been to my bunker here. It's a similar sort of thing downstairs in this building. And. Yeah. I've got like the world's most secure key. On it. Right. It's a. Abloy. It's an Abloy. Abloy. Protect 2. And it's. It was unpickable at one point. But there's like. There are a few people in the world who can pick it.

**Dave Jones:** There's a thing called the most secure key. That's weird to me. Like that. It's. That seems odd.

**Chris Gammell:** No. But anyway. Like. They. Like. It is one of the most unpickable locks out there. Right. Huh. So it's like. Like. Like Joe Average locksmith cannot pick this thing. Right. Oh. Interesting. Yeah. Like.

**Chris Gammell:** If you call up a locksmith and say. You know. Please. You know. Pick it. They'll have to find some other way in. Because they can't. I was going to say.

**Dave Jones:** Don't most locksmiths just drill. Drill the lock anyways.

**Chris Gammell:** They would have to drill the lock. Or they'd have to get in some other way. Right.

**Dave Jones:** Stick a dynamite.

**Chris Gammell:** You know. Shimmy. Or they'd have to go. Like. Do an attack. Under the door. Or whatever. And. And so I did this video. Challenging the lock picking lawyer. Right. Who's a. Oh yeah. He's. He's like the biggest. You might have seen his videos pop up. Anyway. He's like. I've heard you talk about him. Yeah. He's the biggest lock picking YouTuber out there. And so I did a. A video. Sort of like. Challenging him. Because I actually challenged him. Two or three years ago. To. I bet you can't pick this lock. And he said. I can pick any lock. And I said. It's an Abloy Pro Tech 2. And he said. Oh yeah. That's one I can't pick yet. And three years later. I'm still waiting for him to. But so anyway. So I released the video. You know. So it's just like a tongue in cheek thing. I was just. You know. And then everyone gets in the comments. And goes. That's. It doesn't matter how lock secure your lock is. You can drill it. You can smash it. You can shimmy it. You can do underdoor attacks. Blah blah blah blah. You know. Oh God. Okay. Yeah. Yeah. Welcome to the internet.

**Dave Jones:** Is this like. I was going to say. Is this like a common thing people know? I have no. I mean. Like. My solution is to call a locksmith. I think. Right. Okay. Yeah.

**Chris Gammell:** So. Yeah. Anyway. Brick through the window. No. The whole idea is that. This is an incredibly difficult lock to pick. But yes. You can just smash the door in. You know. Like. Yeah. Yeah. Yeah. Fine. You know. Yeah. Yeah. You got me. I'm owned. You can see. I don't know if you can see my eyes rolling in the back of my head. Oh God. Yeah. Yeah. Yeah.

**Dave Jones:** Right. I mean locks and computer security and everything else. Right. It's just to slow people down. Right.

**Chris Gammell:** Yeah. It's dumb. If you have. If the controller's in the. I think it's dumb. If it's going back to any central server. Internet of things connected anything. And it fails. Well. You know. It's your own fault for using Internet of connected things. You know. It's like. It's dumb. No. If you're going to have a house alarm. Just make it standalone. They're super duper. They're super duper. Reliable. They've been engineered. To be. You know. Incredible. Although. Granted. My one blew up.

**Dave Jones:** What?

**Chris Gammell:** Yeah. I have to link in the video. My local Ness unit. Which is a. Which is company here in. Sydney. Who actually make. Designs and manufactures alarm panels. They're one of the biggest. And I think they are the biggest in Australia.

**Dave Jones:** You're saying Ness or Nest. Ness. With a T. Ness. Okay.

**Chris Gammell:** N-E-S-S. Yes. Yeah. Sorry. Got it. As opposed to that ridiculous. Yankee thing. Startup. Yeah. Yeah.

**Dave Jones:** Yeah. Well. Not startup anymore. Which is now owned by Google. Isn't it? Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Anyway. So. I hope Google headquarters. Google servers. Are all. All protected by. Ness access systems. You know. Nest. Access control. That'd be. And then their own servers. Well. It's mostly like.

**Dave Jones:** It started with thermostats. But yeah. Now it's like. Yeah. Yeah.

**Chris Gammell:** It started with thermostats. And then it. Yeah. It branched down into cameras. And whatnot. You know. All sorts of things. Anyway. Where was I? Yes. My alarm panel blew up. Because the capacitor on there. A little ceramic jobby. Was across the power supply. And it smoked. It just. It just went short. Huh. Yeah. It caught on fire. Big Ernie Bernie marks everywhere. Oh wow. Yeah. So my panel failed. These ultra reliable panels. So. Yep.

**Dave Jones:** Not. Not that reliable. I guess. Not that reliable.

**Chris Gammell:** They should have put two capacitors in series. Would have solved that problem. That's how. If you want to design reliable electronics. That's one of the tricks. Because ceramic capacitors. Done a whole. Probably multiple videos on this. How they can crack. How they can get micro cracks. And. And one of their failure modes is short circuit. Right. It's. It's. It's one thing for a capacitor to fail open circuit. But. It's another thing for it to fail short circuit. When it's across your power rail. And most capacitors are across power rails. Right. So if you want to make an ultra reliable circuit. You put two capacitors in series. Sure. You have your capacitance. But if one of them fails short. The other one's there. And it just acts like a regular cap. In fact. You've still got capacitance on your rail. In that case. So if you design an ultra reliable. Circuitry. Every capacitor. In series. Two of them in series.

**Dave Jones:** Yeah.

**Chris Gammell:** Across every decoupling capacitor. Two in series. Interesting.

**Dave Jones:** Yeah.

**Chris Gammell:** Well there's.

**Dave Jones:** There's another. Yeah. There's another thing for my board. Pro tip for you. Yeah. Yeah. Yeah.

**Chris Gammell:** Because like. Like it's rare that it happens. But it does happen. Right. And. Yeah. Yeah. Yeah. So anyway. Yep. So there you go. Tip of the week. Yeah. Capacitors in series. I like it. It's the best. It's the best of the both worlds. Like if. If one fails. You still got half your capacitance there. So you're still doing half your decoupling. Or filtering. Job. You know. Which is still probably going to work. Right. Because if you engineer your product. Not. Would you do that on every product.

**Dave Jones:** I think I mean that just seems like. Not wasteful. No. No.

**Chris Gammell:** You wouldn't do it on every product. But like you're saying like.

**Dave Jones:** High vibration maybe.

**Chris Gammell:** Oh definitely. Any high. High vibration. Shock.

**Dave Jones:** Just high reliability type stuff. High reliability product.

**Chris Gammell:** Yep.

**Dave Jones:** Because I mean. I would imagine that a. I mean even a secure. I mean maybe a security industry. Type thing. It would be like. Oh well. This needs to. Never ever fail. You could say it like that. But.

**Chris Gammell:** Well. Like you don't need to. Because you can actually buy specific capacitors. That are designed. For this. They designed. They're even designed to fail open. Or they've actually got. This was in my video as well. You can actually get components. That have little flexible end caps on them.

**Dave Jones:** Oh yeah.

**Chris Gammell:** So that. They take out the shock and vibration. It decouples the shock and vibration. That comes through your board. Into the ceramic plates inside. And it decouples them. So then they're not going to crack. Or whatever. And yeah. You'll pay 10 times the price for them. But if you're designing a high. High reliability. Airbag controller. In your car or something. You're going to be using those caps. Because they're automotive. Grade. And they're. You know. Like. But you're paying 10 times the price for them. Right.

**Dave Jones:** That's right folks. Dave says. Design in hard to get components. Yep. It'll. It'll. It'll be fine. What could possibly go wrong in 2021?

**Chris Gammell:** Unfortunately you have to. You know. Yeah. I mean. Yeah. That's. Yeah. Yes. That is correct. Yeah. Yeah. In certain. Industries. To meet certain specs. You have to. Like you can't just. You know. Yeah. I'm going to get this capacitor. From the Shenzhen market. And I'm going to whack it across my power rail. Inside my car airbag. It's like. No you're not. No you're not. I don't know.

**Dave Jones:** I feel like that's one of those things. Where. It isn't really going to get put into place. Until something goes wrong. It's like a. Until it's like. In a lesson learned thing. In a company. Oh yeah. No. Yeah. Totally.

**Chris Gammell:** Yep. So.

**Dave Jones:** Yeah. It's unfortunate. But. So wait. Yep. Did you expect that they would do that in this security panel? No. No no. Okay. No.

**Chris Gammell:** No of course not.

**Dave Jones:** I just wouldn't think that that would be something that would. No.

**Chris Gammell:** Because these aren't in a high. You know. They're like. Placed there once. And they sit there forever. You know. Like they never move. They're never touched.

**Dave Jones:** You're not in like Japan. You're not getting like. Actual like. Vibrational stuff. Right. Yeah. No.

**Chris Gammell:** No. It's. No. They're. And they're permanently powered up. You know. They're just powered up forever. It's. It isn't like they're even power cycled. You know. Right. So it's. Yeah. Yep. So. But. You know. With. With hindsight. Yeah. You know. Having that cap across the main power input. And. Yep. Yep. Caught on fire. But then again. Like. You know. Like. A fire in something like that. Is not. Is not. Critical. Right. Yeah. Sure. Your alarm panel breaks. You don't have your alarm. But it's not. Going to. You know. It doesn't impact anything. Right.

**Dave Jones:** The likelihood of that is breaking. As someone is breaking into your house. As someone is breaking. Yeah. Right.

**Chris Gammell:** Yeah. Yeah. Yeah. And in fact. It probably doesn't matter. The fact that you've visibly. Got an alarm system. Is. Is something that actually deters. Right.

**Dave Jones:** The most important thing. An alarm system. Is the. The little placard. That's out in the garden.

**Chris Gammell:** It's the little sticker out the front. That's why you can just buy the sticker. That goes on your front window. That says this. You know. Things. You know. Yeah. This house. Protected by. This house is alarmed. By shotgun.

**Dave Jones:** Killer drones.

**Chris Gammell:** Drones and shotguns. Especially in America. America. America. Yeah. South. Anyway.

**Dave Jones:** Well on the security side of things.

**Chris Gammell:** Yep.

**Dave Jones:** Past guest. Josh Dadko has been. You know. As people will recall. Josh is a bit of a talker. That's the thing we love about him. He was the one who was telling all the. Submarine stories. If people don't remember. But he's been doing security consulting. And he did a video. A couple. Weeks ago. He's been posting them on LinkedIn mostly. But. And so you can follow him there. But he. He posted about like security risk. And like IOT. Like security audits. And stuff like that. That's kind of something he does now. And he pointed out something I had never heard about. I've actually been asked before. Like. You know. You think about security. For a device. For a product rather. Like. Where do you go to find this stuff out? You can go hire someone like Josh. But he talks about. This thing called the. OWASP. 10. Top 10. And so this is something called the. I'll send you a link here actually. The OWASP top 10 is like. Security vulnerabilities for like. Anyone's hardware. And it could also be. It doesn't have to just be connected.

**Chris Gammell:** Is it like an independent rating thing? Or is it a. What is it?

**Dave Jones:** I think there is like a way that products get rated. But this is really more about like. Just the things that are most likely to break down. Something that's going to break down a system. So like attack vectors. That are common in. Bad IOT devices I guess.

**Chris Gammell:** Okay.

**Dave Jones:** And some of them are like. Completely obvious. Actually me. Can I send you this link? Yeah. Some of them are completely obvious. Like. Bad passwords. Hard coded passwords. Yeah. Right. Yeah. Of course. Yeah. Yeah. No one. No one's surprised by that one. But like. Not being able to update. You know. So if it is a connected device. If it's not able to. Like update firmware. You know. So like you have. A thing. You've deployed. A hundred thousand of them. And even if you wanted to. You couldn't probably go and find all of them. And get them all updated. So now this like. Thing is out in the middle of the world. And it's. This big vulnerability. Like. And. But also.

**Chris Gammell:** The remote updating. Is a vulnerability in itself. The ability to remote update something. That's also a vulnerability.

**Dave Jones:** Yeah. Yeah. Yeah. Is that. I don't think that's listed on here. But.

**Chris Gammell:** Yeah. But bloody well should be. I do agree with that. Yeah. Right.

**Dave Jones:** Yeah. Use of insecure or outdated components. That one's interesting. That's. That's a hardware one. Like if you have like a. I guess there's like a crypto engine. That's.

**Chris Gammell:** Yep. Yep. That's been. That's been. Attacked or hacked or whatever. And then you're still using that chip in your product. Yeah. Yeah. Yeah. Exactly. Right.

**Dave Jones:** Like a. A known. That lock has already been picked many times. Sort of thing. Right. Yeah.

**Chris Gammell:** Insufficient privacy protection. Yeah. Insecure data transfer and storage. Lack of device management. Insecure default settings. Yes. Default settings on routers and stuff like that. You know. Oh yeah. Let's leave them there. Admin password. Or the password is God. You know. Oh yeah. Oh classic. Right. Yeah.

**Dave Jones:** 25 years now that movie has been out. Did you know that? It had a 25th anniversary for hackers.

**Chris Gammell:** Right. There you go. Still as good as the day. Wow.

**Dave Jones:** The first time I watched it Dave.

**Chris Gammell:** Yep. Right. Excellent.

**Dave Jones:** Yeah. Classic.

**Chris Gammell:** Come on. You only watched it for. Angelino. Charlie. Didn't you? That was it. That's the only reason. Yeah.

**Dave Jones:** That's the reason I got into computers in the first place. Right. Okay. No man. It's a classic movie. You know. Yeah. Matt the planet.

**Chris Gammell:** Matt the planet. Planet. Okay. I'm going to have to watch it again. Yep.

**Dave Jones:** Yeah. I mean. You have to know. Yep. Yep. It's so bad. It's so good.

**Chris Gammell:** Yeah. Yeah. I know. Yeah. I think I only saw it a couple of years ago. Again. Oh really? Oh okay. Yeah. Yeah. It's fair. Relatively recent that I watched it again. Popped up on Netflix. I was bored. Yeah. Totally. Yeah. Yep. Hmm. There you go. All right. Something that's really cool.

**Dave Jones:** This amp hour thing is really slowing me down. Just so we're clear. Oh okay. Just so we know. I'm really going slow here.

**Chris Gammell:** Okay. Well you get on with it and I'll yap away in the background. One thing I really like from the list this week is the analog thing.

**Dave Jones:** So. I think we talked about that once before. But I think we mentioned it. But I don't think we dug into it. Really? Oh okay. Yeah. Yeah. Yeah.

**Chris Gammell:** Oh. It's very. I'm looking. It's only coming soon. So presumably you can't buy it yet. But it's an analog computer. It's a modern analog computer with like a big like punch panel. Like a big you know connection panel on the front. It looks like a. For those who want to visualize it. It looks like an analog audio mixer kind of thing. You know. It looks like it. Sliders and stuff like that. It might do something audio. It's got all these knobs on it. It's got a single LCD on it. And then it's just got this big patch panel above it. But I just think it looks really funky. Yeah. And it's analog. Analog computing. Because you can learn stuff about analog computing. Yeah. It's a cutting edge analog computer.

**Dave Jones:** Is the idea you like dig into the hood though? Like is. Are people going to get their hands dirty with like an op amp with this thing? Yeah. Dude.

**Chris Gammell:** It's got five integrators. Four summers. Two comparators.

**Dave Jones:** I don't doubt what it has. I mean it has that stuff. But I mean it's the point to actually open it up.

**Chris Gammell:** Eight coefficient potentiometers. I mean you know. Come on. Two two multipliers. This is great.

**Dave Jones:** It sounds like this is halfway to the. Yep. What's that fake machine? The confabulator. Or whatever it's called.

**Chris Gammell:** No. You're.

**Dave Jones:** No.

**Chris Gammell:** No. I don't.

**Dave Jones:** No. It's like that classic video about like explaining like crazy components that are not real.

**Chris Gammell:** Oh. The turbo encabulator. Turbo encabulator. That was pretty close. Turbo encabulator. Yes. Yes. The retro encabulator that. And there's one. You know. There's all sorts of variants. Daniel from Keysight just remade it. Daniel from Keysight did that. Yeah. Yeah. That's great. Yeah. The turbo encabulator is the. But before that where there was the. Just the encabulator. And then the turbo encabulator was an improvement on that. It started in like the 1940s or something. It's actually old. It's actually. You know. It's an old meme. Like. It's a really old gag. Yeah. It's an old gag from like really early on. So. I think the. I'm sure the. The original people who found it. They're way dead. You know. They're like. Way gone. It's. It's that old. Got it. Anyway. Yeah. It's a great joke. Turbo encabulator. No. It is. It's a.

**Dave Jones:** So. Analog computers. Have you ever used one? I've never used one before. So. I don't even know. No.

**Chris Gammell:** I've never used. No. No. I've never used one. I've got to admit. I've used some of the concepts. But. I've never actually. I have two. Op amps are. That's where op amps come from. Op amps are. Yeah. Yes. But. No. As far as. No. So. You know. It's a very niche market. I mean. They're not going to sell a million of them. But. As with all these things. It's in the. The values in the documentation. Right. The values in the. Like. The actual examples. That you. You know. And the information. I would presume. It comes with some booklet. Or something. That. Explains the concepts. And everything. That's where the value is. The value isn't in the product itself. The values in. How they present the information. And how they teach you. About analog. Yeah.

**Dave Jones:** Well. And if there's community. That develops around it too. That's also nice. If. Oh yeah. If you get other people. To learn alongside. That sort of thing. Yeah. If you'll excuse me for one second. I am picking. A stack of components. Off the floor right now. All right. Well. Stop talking. I can't find my 100k resistors.

**Chris Gammell:** Oh. I shall have to continue. Anyway. That's very cool. We will link that in. It's from Anna Bird. Electronics. The web address is. The analog thing. With hyphens in there. So yeah. That's cool. And I presume you can pre. Order. It's not going to be. I presume it's not going to be cheap. You know. Oh. I thought I saw it. $500 or something. I thought there was a price. Yeah. No. I. Yeah. I would not expect it to be cheap. It's just like. It's a really large thing. It's a really large board. And it's complexly. Complexly. Complexly. That is a word. I'm running with it. Complexly. Put together.

**Dave Jones:** Yeah.

**Chris Gammell:** You know. And. Yeah. And all the documentation. And everything that goes into it. So. That's. That's very cool. I. Another retro thing. Which I want. I. I discovered this. In an old magazine. From the 1980s. And damn it. I want one. Just because. It's such an oddity. It is.

**Chris Gammell:** A digital multimeter. That only has a bar graph.

**Dave Jones:** Ooh.

**Chris Gammell:** That's it. There's no segments. None of that segment rubbish.

**Dave Jones:** No labeling or anything either?

**Chris Gammell:** No labeling. It's just got a hundred and. I think it's 128 point bar graph on it. Huh. And then it's got a zoom mode. So if you want more. More. More detail. You can zoom in. And like. It times it by 10. So it goes in. And you can actually narrow down your reading. And stuff like that. So it was designed as a. Like. The. It was advertised as. The best of both worlds.

**Dave Jones:** So is it like. Meant to be like. A digital version of an analog.

**Chris Gammell:** An analog meter. That's exactly what it's supposed to do. Let me read it out. The. This is the ad. The best of both worlds. Analog digital display. Digital multimeters are great. No misreading. No parallax error. High accuracy. But. But. Many users don't like the loss of dynamics. Hang on. I'll send it. I'll send it.

**Dave Jones:** I'll just see like the in between. That's kind of the idea. Like to see the. As the needles moving. Yep. Hang on. I can't imagine the update rate was that fast on this sort of thing though either.

**Chris Gammell:** Hang on. I'm getting. I'm getting there. I'm getting there. Oh yeah. There we go. You've got it. Yeah. Okay. Yep. There you go. So. It's. Here's. Here's the answer they say. Oh sorry. Yes. They. Many users don't like the loss of dynamics. Because DMM samples at a fixed time interval. Changing values in a circuit are often lost. Here's the answer. A digital multimeter which displays in bar graph form. A hundred and five step bar graph gives one percent resolution. With a fast 10 second sampling. Which is actually pretty quick.

**Dave Jones:** I think you should make like a 1980s style. I mean I know this is much later than the 80s right. Or earlier than the 80s. When actually when was this 80s or.

**Chris Gammell:** 1987. 88. Oh man. Yeah.

**Dave Jones:** You should put on like leg warmers. And like. Right. Yeah. Yeah. Yeah. And like. Like a bunch of neon stuff. And like record an ad for this thing. Right. That's what you should do.

**Chris Gammell:** As I'm doing my. Aerobics. Jazzercise. Yeah. Exactly. Jazzercise aerobics. Yeah. I just wanted to take a break from this. To tell you all about the.

**Dave Jones:** Analog. DMM. That's out there. It's the best of both worlds. And it's got. The best of both worlds.

**Chris Gammell:** Yeah.

**Dave Jones:** I could be working out with friends. Or in the lab.

**Chris Gammell:** Anyway. I think it's like. It is such an obscure thing. Obviously. It wasn't a success. Otherwise. It would go. Everyone would be going. Oh yeah. I had one of those. But. Yeah. Anyway.

**Dave Jones:** What's. I mean. Have you searched on eBay? Do these things still exist? Yeah.

**Chris Gammell:** No. I've searched. Apparently it was manufactured by. Soar. S-O-A-R. Which was a manufacturer of multimeters in the 80s. Which was the first. Digital meter. Which I actually. Owned actually. Oh. Interesting. Digital multimeter. Which I just showed in my recent Fluke 23 repair video. There's part two. That's my latest video.

**Dave Jones:** I watched the part two with the. I like the. You took the back off. And then you put like aluminum foil behind. Oh.

**Chris Gammell:** I put. Aluminum.

**Dave Jones:** Alfoil. Alfoil. Aluminium. Alfoil sounds like it's Al Bundy's cousin or something. Right. Al Bundy's cousin. Yeah. Okay.

**Chris Gammell:** Oh boy. Yep. Hey pig. Sorry. That was a funny show. And. Yeah. Anyway. I think it's very cool. So. Yeah. It was manufactured by Saw. But it was sold in Australia by a tricky Dick Smith. It was their branded meter.

**Dave Jones:** Yeah. This doesn't look like there. I mean. There's like four buttons on it. What are the buttons?

**Speaker ?:** Yeah.

**Dave Jones:** That's the zoom. Is that the idea?

**Chris Gammell:** There was zoom. There's a max button. So it had like a min max mode. Or a max mode. Oh.

**Dave Jones:** There's a resistance mode too. Okay. I see. Yeah. Okay. Yeah. So. I don't think this would have been up to snuff to modern standards. I have to say. Right. Well. You know.

**Chris Gammell:** It's. Come on. It's the best of both worlds dude.

**Dave Jones:** It is the best of both worlds. I feel like you just make. Make a modern one. And you know. Arduino or similar. Right. Yeah.

**Chris Gammell:** I got to say that. That 10 times per second updating was. You know. It's pretty quick. It's not as fast as like typically 30 times per second. That they have on the bar graphs these days. But they had 105 segments.

**Dave Jones:** Yeah. Well. Yeah.

**Chris Gammell:** I mean. You know. With magnification. Thank you very much.

**Dave Jones:** You could also do it like a. Like a QVC commercial. You know. And have like the one person in the corner being like. Oh. 10x. 10x amplification. 10x. I would pay. 10x for that. Oh boy. It's like. Me-me type things you could do here man.

**Chris Gammell:** Yeah. Anyway. I definitely. I want one. If you've got one. I will pay.

**Dave Jones:** He will buy it off. He'll pay 10x. 10x the price you paid. 79.95. Right. That was the list price there.

**Chris Gammell:** I'll pay 799 dollars for it. Oh boy. Yeah. That would be. That would be dedication. Yeah. Yep. And I can get a whole 50 bucks back in Google ad revenue. Yeah. Yeah. Right. Right. Yeah. Right. Anyway. I just think. Yeah. Like nobody remembers this. It's like. It's just this obscure thing. And. And. And then. There's a lot of people. Here you go. I'll send you this. There's a lot of people who thought it was like an. April Fool's joke. Right.

**Dave Jones:** Uh huh. Yep.

**Chris Gammell:** Which was fair. Fair enough. I will. There you go. I will send you. Because the ad. The ad doesn't have a real photo. The ad. Actually has. A. Just a sketch of it. It just actually has a sketch. Right. So. This was the original full page ad that I saw. And it's just a sketch. And a lot of people thought. Ah. You know. Because yeah. Like. They didn't have a real product. That's an April Fool's joke. But it wasn't. It was in the November issue. That's just how they.

**Dave Jones:** They used to do graphics. That's how.

**Chris Gammell:** That's how they used to do ads. Yeah. Yeah. Right.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** They would actually draw them. Somebody would actually redraw them. Because it was cheaper than embedding a photo. I guess. That's right. In the typeset machine. Yeah. Or whatever. I don't know. They. Photos are expensive man. They had an artist inside. You know. They had an in-house artist. That just redrew.

**Dave Jones:** Right. They were probably doing the layout by hand. Right. I mean. They were doing. Yeah. Yeah. Like magazine layout by hand. Yeah.

**Chris Gammell:** It's all typeset. And you know. Cut and pasted. And you know. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Yep. Ah. Update around here.

**Dave Jones:** My 40.2 kiloohm baggie. Apparently I swapped out for 100k. That was a lucky find. Oh. Wow. I did a bad job of that. The last time I did the assembly here. So what.

**Chris Gammell:** You labeled it wrong. Or you put them on wrong. No.

**Dave Jones:** I put the strip of resistors back into the wrong baggie.

**Chris Gammell:** Ah. Into the wrong bag. Okay. Yeah. So did you notice that. Because the markings are on them?

**Dave Jones:** Nope. No. These are still too small. Are these head markings?

**Chris Gammell:** Okay. No. They don't. Yeah. Okay. So the name. Yeah.

**Dave Jones:** They still do. But I. No. It's because. Hang on.

**Chris Gammell:** Are you complaining about your eyes?

**Dave Jones:** I am. Yeah.

**Chris Gammell:** You're getting old. You're married with kids. And you now. You're complaining about the eyesight. Yeah. Yeah.

**Dave Jones:** Kids these days with their fancy eyeballs. Yep. Yeah. No. The 100k bag had caps in it. So I knew something was wrong there. And that's why I was trying to find the baggie off the floor. Obviously the 100k was not capacitors. And then I was testing the 40 point. I was trying to find the 100k. I had found a strip on the floor. This is really exciting radio by the way. The 100k strip was on the floor. That had 40k resistors. I used my 1.21. 1.21 GW DMM to test the resistance on them. So I knew the 40.2k was out of place. And then when I got to that baggie, I was like, I bet these are 100ks. And I was right. So. There you go. Past me was a little sloppy. I got to say. That would have been one of those failures too, where it would have been like, something's wrong here, but I don't know. Like it would have been, it was actually the 40, the 40k was in the feedback network of a different regulator. So that would have just been the wrong value, you know, it just would have been like, nope, I'm outputting half a volt. You're not getting any more than that.

**Chris Gammell:** So how, how, how many components have you placed in an hour? What is your placement rate per hour?

**Dave Jones:** Really slow. I mean, like. Really slow. I've been doing, I find I do best when I can just like turn on a podcast, not be on a podcast. You know, that's a different, that's a different part of the brain. Turn on a podcast and just like turn into a, you know, the, the, the meat, the meat picking place. That's, that's what's necessary. I think, right. I'm probably at, oh, it's pathetically low. 50, 50 components.

**Chris Gammell:** Okay. All right.

**Dave Jones:** I don't know. Oh, six, oh three. So not like the, not the smallest, not the biggest.

**Chris Gammell:** So you're placing with a tweezers. Obviously you don't have a, like a suction.

**Dave Jones:** Yeah. Some people like the vacuum pickup thing. You do that? No, no. I used a tweezers. When's the last time you assembled a board? You need to, you need to make a board, my friend. I need to make another board. You need to join me in my complaining about my old eyes.

**Chris Gammell:** It has been a while. Yep. Yeah. Yep.

**Dave Jones:** We got it. We got to brainstorm. What can you build? What do you want to build?

**Chris Gammell:** I like, cause I love, like, I would love to build something that's just like huge, like a huge board, like a physically huge board.

**Dave Jones:** That's got like, Oh, like the one that Eric Schlepfer did the, uh, the, uh, the Moss 6502.

**Chris Gammell:** The monster 6502 or whatever it's called. Like, I, like I, there's something therapeutic about assembling a board like that. Like, yeah.

**Dave Jones:** It's almost like going and like doing a puzzle, you know, what is like doing a puzzle, but it's like, like a jigsaw puzzle. Yeah.

**Chris Gammell:** No, I like the, the, the thing I hate is like, you know, random boards that have, you know, like, like a hundred different components on that. They're just a pain in the ass. They're just like, no, I just don't enjoy assembling boards like that. But if the board's got like nice symmetrical arrays on it or something, you know, nice symmetrical blocks on it or something like that. And I can just like do the same value over and over. That's just like, there's something satisfying about that.

**Dave Jones:** Can I tell you about that? There's like a craft that I did. It was like last winter. So I may have mentioned it on here, but my, my wife had bought it. Like we were on a vacation and in like the middle of nowhere and it was cold and like, we were like, well, we could just do this. It's like a puzzle. Yep. And it was this craft she had found and it was like these little jewels. And then you get like a straw and a piece. So the straw, you stick into like a piece of putty. And so the putty kind of like sticks in the end of the straw.

**Chris Gammell:** Yeah.

**Dave Jones:** And so then you use that to basically like pick up a gem and then you place it on, you place it by, it's like a match by color. And you place it onto like the color that is associated with it. And then the, the thing you're placing, it's like a sticky mat basically. So it holds the gem. So basically you're picking it up with a little sticky end and you're putting it onto a sticky sheet of paper by, by color. And like halfway through, I'm like, am I doing pick in place on vacation? Yeah. I mean, it actually, it was very therapeutic and like, it's, I think it's like a Japanese thing, maybe Chinese. Okay. I'm not sure. It was pretty fun though. Like it was like a craft for like doing with kids too. I'm not like little kids would have a lot of problem with it.

**Chris Gammell:** Cause it's, it's a very manual, manual dexterity thing. Yeah. Right.

**Dave Jones:** But if you had like, I mean like your oldest is like eight now or he's like 10, 10. Oh yeah. Yeah. So like you could basically like start him on this and then be like, Hey, by the way, I have a board. This is like pretty much the same thing. We're just going to, you know, use resistors now. Cool. You know, just, you know, you got to train the child labor at some point. Right.

**Chris Gammell:** Yeah. So speaking of kids, speaking of 10 year old kids. Okay. Yeah. We will finish off with this. This was my task yesterday. I actually did a live one hour physics demonstration with, yeah. To a year five students who are 10 or 11 years old kids. And yeah. So a whole school worth of year five kids were all watching. They were watching me live demonstrate.

**Dave Jones:** Didn't get pelted with tomatoes or anything like that? No, no. Was it digital? So you were all safe. It was all digital.

**Chris Gammell:** So I was, I would have dodged them easily. Yeah. And so I had to try and hold the interest of 10 year olds for an hour doing experiments in physics. Non-trivial task. Different forces. It was about, this was about forces. That's interesting. So, you know, tension and elastic forces and gravity and, you know. That's awesome. Booyancy forces, you know, floating buoyancy and all these different types of forces. So I hadn't, yeah. So I came up with all these little demos that explained it all to them. And I think it was hit. I think I blew some minds.

**Dave Jones:** That's great. Man. Physics is what got me. Like, I mean, you know that I, I didn't get into electronics until college and, uh, but physics was the gateway drug for me. Right. Okay. Yeah. Well, I mean, obviously not the forces stuff, but you know, like, you know, you get the, if you're into the forces stuff and then you're like, oh, by the way, now we're going to talk about like electrons. Like, yeah, cool.

**Chris Gammell:** No, I, yeah. I, I think I really blew their minds when at the end I showed them how that, uh, their watch can change, it can speed up or slow down if you just turn it over. If you flip it over.

**Dave Jones:** And you're like, kids, you may also have heard this on the amp hour. Uh, we also discussed, we also discussed on the amp hour.

**Chris Gammell:** Yes. That's great.

**Dave Jones:** But yeah. Yeah. I thought, yeah. Anyway. Do they call it physics at that age? Like how do they, how do they organize? Oh, no.

**Chris Gammell:** It's, it's a unit of inquiry. It's like, it's like just basic, like they don't really, they just touch on it. Like they don't learn the physics formulas and stuff. They, they just sort of like touch on the concepts. It's not, it's not really about learning, you know, like, like they don't learn like the buoyancy formula and they don't learn, you know, stuff like that. It's yeah.

**Dave Jones:** It's almost like a, it's like an overview so that they can see the experiment.

**Chris Gammell:** It's an overview concept. So it's in their head. So when they come to learn it in high school, it's sort of, oh yeah, it sort of pops out of their head. That's the, you know, that's, that's the kind of thing.

**Dave Jones:** So I mean, even in high school, when I did it, it was, I, when I did physics in high school, I did AP physics and it was non calculus based. Right. Yep. So like no derivatives, no, no integrals, which is kind of crazy because that's a lot of physics.

**Chris Gammell:** Well, yeah, yeah, exactly. But, but you can do some great concept stuff without any of that. You know, yeah.

**Dave Jones:** Oh, true. I mean, and I think that's what it's really about, especially at that age too. It's just like experiments and getting people excited about it. Yeah. Yeah.

**Chris Gammell:** Exactly.

**Dave Jones:** I mean, hell, that's still the, that's still the thing, man. I still want to see experiments and get excited about physics. Like it's so cool. Yeah. That's great.

**Chris Gammell:** So anyway, the, yeah. One of the things I learned is that, geez, I wouldn't want to be a teacher, you know, like imagine having to come up with this stuff every day, you know, you've got the syllabus. Cause they basically gave me the syllabus, right? The syllabus is like, kind of like the semi-official thing that they're supposed to follow.

**Dave Jones:** I'm just imagining like, like a teacher handing you a syllabus, like being like, you do it. And then pulling a flask out of their pocket. That's pretty much what it was. That's pretty much what it was.

**Chris Gammell:** I was roped into it cause they knew who I am and they knew what I do and they went, yeah. So I think I'm roped into two more. It's great. Yeah.

**Dave Jones:** Anyway, super fun, man.

**Chris Gammell:** Yeah.

**Dave Jones:** I think you should do, you should do a reprise version on EV blog too. I'd watch it.

**Chris Gammell:** There is, there is actually, I haven't released it. I actually did. I did actually shoot the video. Yeah. Yeah. Yes. It is actually patrons only video. One of them is patrons and supporters only is you can see me. Support EV blog. The full, yeah. The full 30 minute video. Dry run test of it. Oh, cool. And sort of, yeah. Yeah. So I actually recorded a dry run test. Obviously I can't, I can't release the, the one that was on the day because it, you know, includes kids. So I can't, you know.

**Dave Jones:** Well, and also all the IP that I'm sure that you generated that, you know, like that belongs to the school now. Right.

**Chris Gammell:** Anyway, no, I did actually.

**Dave Jones:** So much cash, I'm sure.

**Chris Gammell:** Although I did release publicly on my second channel. I did actually release last night, a video, a video segment from that one hour live show. I just chopped out the kids voices and names. Yeah. So, yeah. Yeah. Yeah. That's good. So, yeah. Yeah. That's super fun. Yeah. So that was fun.

**Dave Jones:** That's great. Yep. There you go. Another career, you know, get yourself a real job, Dave. Yeah.

**Chris Gammell:** Get myself a real job. Yeah. I'll become a teacher, you know.

**Dave Jones:** Yeah.

**Chris Gammell:** But there's a lot of people that say that. Why don't I become a teacher? I'm such a good teacher. It's like, well, technically I was. I did actually get, I was accepted for a teaching job once. Oh, really? A long time ago. Yes. Long, long time ago. I was probably 22 or something. And I went for a teaching job to teach PCB design and layout. And I was accepted. Yeah. They actually said, yeah, I was surprised. They gave it to me. Maybe I was the only one who showed up.

**Dave Jones:** I'm surprised they didn't just, they didn't just hire you to critique people's boards.

**Chris Gammell:** I mean, critique people's boards. Anyway. So, yeah. But then just after, like I was, I was about to teach it. But then, yeah, I got another job, I think. And something, yeah, it, it, it conflicted or something and I couldn't do it. So I had to.

**Dave Jones:** I was like, oh, I want to make money someday. So probably not going to be a teacher.

**Chris Gammell:** Turn them down. Yeah. So I, that was my, yeah, but technically, yes, I, I was accepted as a teacher. At a local college. So yeah. That's great. Piece of bid layout and design. Yeah. Anyway. So yeah. No, the answer to that question is no, I wouldn't do it because I see more value in making content for tens of thousands or hundreds of thousands of people for a broader audience. I see more value in that than just, you know, teaching 50 or a hundred people at once.

**Dave Jones:** Also Dave swears a lot. So not really, not a good teacher for kids. Yeah. I'm not great. Yeah.

**Chris Gammell:** And it's like, and like, they asked me, what is your YouTube channel? I'm going, oh yeah. It's the EV vlog. But you know, like, I don't really want you to watch it. Cause it's not really, you know, for 10 year old kids, you know, it's kind of. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Oh boy.

**Dave Jones:** Oh well. They'll figure it out. Yep. I think they could, I think they could probably search and find it. So I'm not.

**Chris Gammell:** I'm sure they can search it. I'm not going to say like, there's the occasional video they'd see that's probably not suitable for kids, you know, but anyway. Right. Right. Yeah.

**Dave Jones:** Probably can't find that anywhere else on the internet either.

**Chris Gammell:** They're right.

**Dave Jones:** One of my, one of my college buddies is, he's doing middle school technology stuff. And we were emailing back and forth about, you know, just some of the tools that are out there. He's going to be doing some, I think he said he was not circuit Python. He's using, I always get these backwards. Yeah. No, he's using circuit Python, which is the Adafruit one, not micro Python. Right. All right. And just some of the tools with that. And like, like the stuff he's doing though, he's like, yeah, we're going to like, you know, do motors and write Python. And I was just like, man, I wish Charlie was my teacher. Like that would be so cool. Yeah.

**Chris Gammell:** We had nothing like that when I was a kid. No.

**Dave Jones:** Man. Like, and like there's, yeah, there's, there's other platforms like that. There's, I mean like the Lego stuff that's out there these days, like the, what's it called? No. Lego league, something like that. No. Do they have stuff like that in Australia? Has it made like, does first down in Australia?

**Chris Gammell:** Oh yes. Yes. I, um, I was a judge. I was, I was a judge in one of those. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. Yeah. I mean, that stuff, I think it, it did exist when I was in high school. Cause one of my buddies did it and now he's a dentist. Come on. Jeez. Yeah. I know. Dan. Yeah.

**Chris Gammell:** Fall you're in life becoming a dentist. Dentist. What a, what a loser.

**Dave Jones:** What a, what a rich, what a rich, handsome loser. Yeah. Yeah. Exactly.

**Chris Gammell:** Oh boy.

**Dave Jones:** Yeah. But Dan had done, had done, uh, first robotics and stuff like that. Yeah. And, but I would just, I don't, it, maybe it was even at my school. I just didn't, I didn't know about it. You know, it's like one of those things that you're not supposed to it.

**Chris Gammell:** My high school was like the opposite of that. Yeah. It was like the, like telling me to go away when I wanted to do something like that. It was like, you know. Well, it's not cheap. I mean, that's the thing.

**Dave Jones:** Like you need to like, really like you need to fundraise, you know, you need to have sponsors and stuff like that. Yeah.

**Chris Gammell:** But I was going to do everything and they still wouldn't, they still wouldn't support me. There was this contest I wanted to enter.

**Dave Jones:** Hey kid, go play football.

**Chris Gammell:** There was this.

**Dave Jones:** Australian rules. Cause we're in Australia. Sorry.

**Chris Gammell:** There was this, uh, design contest that I wanted to enter. It was in, it was in one of the magazines. Right. But, but you had to have your school sponsor you. Like you had to enter it. Like your school had to okay it or something like the school had to support it or something. Right. You know. So yeah, I was, I was going to, enter this contest and I, so I went to them and showed them the article and saying, you know, enter the school. You know, all you've got to do is like, I don't know, sign here and support me or something. I don't know. And like, not, not with money or equipment or anything. I've, I've, I've got all the gear, you know, I'll build my own thing. And they went, no, what is this? Go away kid. You know, it was like.

**Dave Jones:** And you gave up there. Come on, Dave, go around, go around.

**Chris Gammell:** Unfortunately you can't. That was why. That was the one of the firm requirements.

**Dave Jones:** You talked to like the, the principal though. I mean, you know,

**Chris Gammell:** No, no, no. A science teacher. And then my regular teacher and others. Got to go higher. Yeah. Yeah.

**Dave Jones:** Superintendent, you know, super Nintendo Chalmers. You got to talk to the top, man. Take it to the top. I don't know. I don't know what it was like in the eighties. I assume they gave you a wedgie and, you know. Yeah. Yeah. Yeah. That's it. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Popular media is to believe, believe you got it. You got a swirly and, you know. Yeah. Sent, sent on your way.

**Chris Gammell:** But then again, the high school I did go to made, went, went viral like five years ago when another kid like body slammed this other kid. And it was like, yeah, it was, it was, it was a rough school.

**Dave Jones:** Rough, rough and tumble. Huh? Yeah.

**Chris Gammell:** Yeah. Yeah. That's too bad. Yeah. What are you talking about kid? You're still alive, aren't you?

**Dave Jones:** The mean, the mean streets of Sydney.

**Chris Gammell:** Yep. Yep. Oh boy.

**Dave Jones:** Well, Dave, I'm glad, I'm glad you made it. I'm glad you made it. Yeah.

**Chris Gammell:** I, yeah, I made it.

**Dave Jones:** Yeah.

**Chris Gammell:** Yep. I'm alive and I'm not in jail. So, you know. Yep.

**Dave Jones:** Yep. Doing well.

**Chris Gammell:** Yep. Doing well. I'm a success story.

**Dave Jones:** All right. Well, I'm going to be here for another hour or so probably doing placements. I am still in resistors. I still have a ton of resistors. I had. Oh, a ton.

**Chris Gammell:** There's hardly any on the board. Oh,

**Dave Jones:** come on. I had 19 line items and some of them had eight. The zero ohm resist. There was eight zero ohm resistors. Oh, that's. You might add this up here, but.

**Chris Gammell:** I, I, I don't know how you're doing it, Chris. I don't. You know, it's just. The stamina of.

**Dave Jones:** I am a martyr if nothing else.

**Chris Gammell:** All right. Oh, that's it. I'm a crick in my neck.

**Dave Jones:** Yep. Have fun. See you next time. Bye. Catch you next time.

**Speaker ?:** Bye. administered administered administered administered ! administered administered administered
