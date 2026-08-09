---
episode: 621
title: The Magic of Calipers
url: https://theamphour.com/621-the-magic-of-calipers/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release February 26th, 2023. Episode 621. The Magic of Calipers.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** I am going to defend myself, dammit. Oh, what? You think it's undefendable what I've done?

**Chris Gammell:** No, no, no. No. You have a particular way of doing things. Usually. No. My big problem was watching this whole thing unfold.

**Dave Jones:** Yeah, you watched it live. Okay.

**Chris Gammell:** I watched part of it live. And Dave was trying to get... It was your iOS app, is that right? For the multimeter? Yes. Yes.

**Dave Jones:** And I wanted to upload it to GitHub so that people could have it. Yeah.

**Chris Gammell:** You were basically crowdsourcing from your audience, like your secondary channel stream. And people were very helpful, but there was a lag.

**Dave Jones:** There are, yeah. Live chat is hard. Getting live help is hard. Because there's like... It can be up to like a 30-second lag between people.

**Chris Gammell:** Yeah, exactly. Exactly.

**Dave Jones:** Anyway. Yeah. Yeah, right. Now...

**Chris Gammell:** You want to defend yourself. Go for it. Yes, I will defend myself.

**Dave Jones:** The first thing you said there is plural. I have a particular way of doing things. Now, here is the crux of it, right? What I wanted to do was not things. It was not a process. It was one thing. I wanted to do one task and then never touch it again. Okay? Okay. All I wanted to do was I had existing code, right? An existing project. All I wanted to do at the request of somebody on my forum is put it on my GitHub account so that other people could then use their GitHub and branch it and do whatever and use it, right?

**Chris Gammell:** Yeah, there it is. I wanted to share it with the world. Work it and clone it and all that good stuff.

**Dave Jones:** Which they've already done, right? That's all I wanted to do. Incredibly simple. One-off. One-off. And this is my defense. A one-off task. Okay? I am not versioning controlled. I'm not doing a project using the GUI interface on GitHub. All I'm doing is one task.

**Chris Gammell:** You're using it as file storage, effectively.

**Dave Jones:** File. I'm putting... Yeah, but... Right. I could have just dumped it to a Dropbox somewhere, right? But everyone uses GitHub, right? Everyone uses Git, right?

**Chris Gammell:** But they use it for revision control, so...

**Dave Jones:** Yep.

**Chris Gammell:** Not that important if it... I mean, you don't want to give a Dropbox thing because...

**Dave Jones:** No, it's like... No, it's silly. And I wanted to have it on my... Because I do have a GitHub account, right? So I wanted to put it on my... Yeah, I mean... Well, actually, I started off putting it on the GitLab account, which is a different system to GitHub. But anyway, we'll get into that. So all I wanted to do was one task, right? And you've got to remember, I don't use Git, right?

**Chris Gammell:** Right.

**Dave Jones:** I don't use Git. Yep. And I would love to... I'd love to learn Git, okay? That's a fine thing to do. I'd love to learn it. But for this one task that I simply wanted to spend a couple of minutes doing, I did not want to learn Git for that, okay? Yeah. So GitHub has a drag and drop interface. All you have to do is create the repository, drag the files over, done. It's literally like seconds, tens of seconds of work.

**Chris Gammell:** Yeah.

**Dave Jones:** But the problem was it had a 100 file limit and I had 800 files, right? Right.

**Chris Gammell:** Right.

**Dave Jones:** So I went, aha, I'll upload it to my GitLab account. And GitLab didn't let you do that either. So I was getting frustrated, like how do I do more than 100 files, right? So I tried on Twitter, asked on Twitter, no one could explain it to me properly, right? So I did a live show and then people eventually were trying to help me out on a live show. And we eventually got it, right? After like 45 minutes or something, you would quit by this time. You would quit in frustration, right? By watching this. And as it turns out, I followed everyone's instructions down to the T and it didn't work, right? Because GitLab.

**Chris Gammell:** Right. You were doing it over HTTPS instead of SSH. You didn't have a token on your machine.

**Dave Jones:** Yeah. GitLab. And I do have a GitLab account and that's where my existing multimeter code is for my Android. That's why I wanted to put my Apple code on there as well. And it didn't work because it required a secure connection.

**Chris Gammell:** It required a HTTPS or sorry, it required a token connection.

**Dave Jones:** It required secure keys, right? It requires secure keys. At that point, I just gave up and I just manually uploaded batches of things to batches of files to GitHub. But as it turns out, right? All of these, all these GitHub experts, thank you very much for helping me. It's awesome, by the way. Thank you very much. But not one of them could tell me that you can easily do it on GitLab by simply opening up the GUI IDE interface and dragging your files over. Done. Two seconds. Somebody emailed me after this.

**Chris Gammell:** Nobody really uses it like that. Exactly.

**Dave Jones:** And a lot of people have attacked me or some people have attacked me on Twitter over this saying, oh, you know, only idiots use the GUI interface. Oh, that's not right. No. No, it's not. Right? And this is why I'm defending myself because I wanted to do one task. Sure. If I was going to work on the project from GitHub, I'd learn the Git commands and do it properly. Right? But I didn't want to do that. I'm not working on this project. Sure. I just wanted to upload it. So can you accept my defense that I had one task to do and I wanted it to take a trivially amount of time?

**Chris Gammell:** Sure. Yeah.

**Dave Jones:** And there would be other people like me who have that requirement.

**Chris Gammell:** Let me give you some of my GitHub history because I started in a very similar place to you actually on this stuff. I really, really struggled. And everybody told me not to use the GitHub desktop, which was actually pretty underdeveloped at the time. So it was kind of like-

**Dave Jones:** Quite a few people told me to use that.

**Chris Gammell:** Oh, interesting. Okay.

**Dave Jones:** Yeah. And that is kind of like in between- I didn't want to download another. I didn't want to download a program to do it. Yeah. I'm going, well, the web interface should work. Right.

**Chris Gammell:** Right. And I think they've gotten better actually. Now we know that there is this web interface. That's better for that sort of thing. I think some of it is kind of mindset shift too. And it's like, I was used to kind of, I would think about like uploading like an IDE or like working from an IDE like sample project or something like that. And there would just be this kind of just huge chunk of file, like hundreds of files like you're talking about. And really that doesn't work great. And I think also because like, you know, sometimes you get the build directory involved. And then it's like, so then every time you do another build, all those files look different to the system. Yeah. Yeah. Right. Of course. But you don't really, you don't want to upload those. Yes. Another time. Yeah.

**Dave Jones:** You don't want the build file. Can't you just exclude the build folders? You can't.

**Chris Gammell:** Yeah. I didn't know how to do that though. That's the thing. Right. So I just say in like the growing pains of like learning this sort of system. And then another thing that I, I really struggled with when I started doing Zephyr stuff back when I was doing my ABC board was I was like, I was like, do I, you know, Zephyr is this massive like download, like gigabytes. And so I had that on my computer.

**Dave Jones:** It's like hideously complex stuff, right? Yeah. It's like an FPGA kind of tool.

**Chris Gammell:** Well, like complex. And then it also pulls in a lot of like, you know, vendor libraries.

**Dave Jones:** Includes and vendor stuff. Yeah, exactly.

**Chris Gammell:** Like when you, when you download like the default, when you start from like Zephyr, you're getting all of the S like every, every supported platform pretty much like unless you like go in and you're saying like, Oh, actually I only want this one chip platform, which is a pretty complex task to go and do. You'll basically, you'll get all of the, all of the microchip stuff, all the SDM stuff. Yeah, exactly. Yeah, exactly. And you just don't know it's there. And then, so then I had this huge directory. I was working out of a sample folder. Like you do, like you kind of showed in that, that risk five video, right? You're working on this sample folder. Yeah, right. Cause that's, that's the right way to do it. And then I was like, Oh, okay. Well now I want to like commit these changes, but do I commit the, the whole thing? And then it was like the entire SDK and that's like two gigabytes. And I was like, this can't be right. And I had just remember like being like waiting for like hours for the thing to update. And then like, I don't own, I don't own that code. I shouldn't have that on my GitHub. And so like, just kind of like that, just kind of that understanding of that learning process of like, of how to do it. The biggest thing for me was like having someone like I could watch do it. That was super important for me.

**Dave Jones:** Yeah, totally. Yeah. Yep.

**Chris Gammell:** So what I'm trying to say, Dave is, you know, if you want to look over my shoulder at some point, I'll show you how to write really bad code.

**Dave Jones:** Thank you.

**Chris Gammell:** Really, really bad code.

**Dave Jones:** That's, that's, that's what I strive to do is be a bad coder.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And it's, yeah.

**Chris Gammell:** Just, just good enough to get over the hump. That's, that's what we, that's what we shoot for here at the Amp Hour.

**Dave Jones:** See, people can think, I think I don't appreciate version control. I do. I, I worked it out here. I mean, I used to use version control daily. We use Tortoise SVN though, which, you know, there's quite a lot of people who actually like that Tortoise SVN interface, but yeah. Yeah.

**Chris Gammell:** So, Subversion is a little different. It's in terms of like, it's kind of just.

**Dave Jones:** Subversion is the name for it. Yeah. Yeah. That's right.

**Chris Gammell:** That's the SVN part. Yeah. It's a little different, but you know, it gets like, it's weird at the beginning, you know? I've, you know, I think. Well, I don't think it's that weird.

**Dave Jones:** I don't, you know, I can, I can totally understand. But when I simply wanted to do a task that should have taken like seconds.

**Chris Gammell:** Have you done get rebase Dave? Cause that I've been doing that for months and I have no idea what it does still.

**Dave Jones:** No, I have no idea what a rebase.

**Chris Gammell:** Yeah. Yeah. That's the thing. Like there's like all these, like, it feels like magic. It's just like these magic incantations, but like, you know, I'm starting to actually get it. But like, you know, at the beginning, it's just like, what does this even mean? You know? And like the idea of like, you know, a local head versus the remote. Yeah.

**Dave Jones:** To be fair, there are quite a few people who actually on Twitter, they actually came in defense and said, look, to be honest, Git is not for noobs or for people who just use it casually or something like that. It's, it's, you know. I think that's, that's what I'm saying here as well.

**Chris Gammell:** I think it is, it is tough. It's a, it's a tough, it's a tough learning curve. And especially because I think the, the common suggestion is like, go straight to the command line and some people aren't comfortable in the command line either.

**Dave Jones:** Well, I can certainly do the command line. I did quite a few command line things. I've got, you know, command line scripts that do my video encoding and do other stuff. You know, it's like, you know, it, it, it isn't foreign to me. It's just that when you want to do a simple task once and, you know, and it bites you in the ass, it's like, you know, anyway, it, it wasn't get that bit me in the ass. It was the GUI. It was the GUI version, which had, we simply had a hundred file limit. So, you know, as like. Yeah.

**Chris Gammell:** I'm guessing they must, they must do that to like prevent like abuse or something. I don't know.

**Dave Jones:** Yeah. Something like that. But like, like a hundred is really low. Like just a, as you said, like, or when you include lots of, you know, when you've got tons of includes and everything, a simple project, like this one app, my, my app has 880 files in it. You know, it's like, and, and that doesn't include any, you know, Mac OS crap subdirectories either. That's, that's just like the code with, with all of its includes and whatnot. So yeah. So I think a hundred is too few. So I don't know what the, what the rationale is there.

**Chris Gammell:** I also remember from the video that, that you were like looking at like, what are all these files here? Or some of it was when you were uploading the dot get folder. That's like a hidden folder.

**Dave Jones:** Yes, that was it. Yeah. Because another issue is that I didn't actually technically start from scratch because there was an existing dot get folder in there or some, something weird like that was messing it up. And you know, all sorts of factors contributed to make it look frustrated and caused you to storm out in disgust. No, not disgust.

**Chris Gammell:** Yeah. So like that, that's, that's where, you know, when you think about it, like there's like a local version and a remote version and it, and it tracks like the changes that you, when you do a commit, it changes, you know, it says like, oh, Dave changed, you know, the copyright date or something like that. Right. And that's a small change.

**Dave Jones:** Yeah.

**Chris Gammell:** But like that then becomes an actual atomic change within your local that in that dot get folder. And then you think about all the changes you might do over time. Those really start to add up in terms of the number of, they're small files, but there's a lot of them. And then it's all that history. You can roll back the entire history. So like if you, if you wrote an entire project, you know, and you kept that history or say you even cloned a project from a remote repository to your computer, you can actually go back and say, oh, you know, Dave's Dave did a commit on January 13th of 2023. And the commit number is, you know, ABC123456, whatever. I can go and say, go to that commit number and create a new branch from that. And I would, I, all of your code is there.

**Dave Jones:** It's really, it's very cool. Yes. I love version control. It's great.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Which is why I wanted to give my code instead of just putting it on a Dropbox somewhere. I wanted to do it properly and put it on GitHub. Sure.

**Speaker ?:** Sure.

**Dave Jones:** You know.

**Chris Gammell:** What is your, what does the app do? I actually don't know. What does the app do? It's just controlling the multimeter.

**Dave Jones:** It just controls the multimeter. Yeah. But it, my, my app apparently has vanished from the Apple store and I have no idea why it's vanished. But apparently there is a third party company that actually wrote an app for my meter, which I didn't know about, which is great. So yeah. That's cool. So at least there is still an app there until I can figure out how to somehow get it back on the Apple store. But I don't know, maybe I'm not paying my dues or something. I can't remember. So I didn't do that. That was David too, who did that. He's, you know, like handled all the Apple app and stuff. He's the one who wrote it, uploaded it and registered it and, you know, did all that sort of stuff. So yeah, I have no idea how it works. I have no idea how any of this Apple app verification or whatnot works. I assume. Yeah. It's, I don't know. Do you have to like continually update them to stay update with the latest Apple version?

**Chris Gammell:** Otherwise it just like drops you off the Apple store.

**Dave Jones:** I've got no idea.

**Chris Gammell:** Anything with app stores, honestly. I don't know. It's interesting because I've started to look into some of that, you know, there's like these different app platforms and stuff like that, where you can kind of have kind of quick start apps there. But even then I've never really done like the Bluetooth, Bluetooth modes either, you know, like, so that's where you see a lot of that stuff. Yeah.

**Dave Jones:** We've talked about this before, but the combination of doing Bluetooth development and Apple and app development is the most horrendous experience possible. You've got like, yeah, it's just awesome.

**Chris Gammell:** I mean, yeah. Pick your poison, right? I mean, like either that or deal with cell companies or deal with wifi or, you know, like if you're going to be connected, it's like you're, yeah, it's, I was actually just talking about someone about that the other day where it is, you know, when you think about like, you know, hardware people, when they think about Bluetooth, it's like the interface, the internet effectively is the phone, right? The phone, the phone is a very powerful device at this point. It's basically a Linux computer. Almost always Apple and Android are Linux computers. And they, you know, then are that they're almost always talking.

**Dave Jones:** Is Apple still a Linux computer? Doesn't Apple run Apple iOS or whatever?

**Chris Gammell:** It's iOS, but that's based on Unix.

**Dave Jones:** Oh, is it? Oh, okay. Right.

**Chris Gammell:** I might be wrong about that. Am I wrong about that? I thought that was based on Unix.

**Dave Jones:** Well, maybe it was way back. Maybe it's not anymore. I have no idea.

**Chris Gammell:** Oh, Unix-like. That's what it says. Unix-like.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** All right.

**Chris Gammell:** Yeah, actually. Oh, that's interesting. Because, yeah, so the stuff that goes on the laptops is definitely Unix-derived. Unix-like based on Darwin, which is BSD.

**Dave Jones:** It's based on Darwin. Yeah, I'm reading it now. Yeah. Based on Darwin, whatever that is, which is a Unix. Way above my head. That's above my pay grade. That's for sure. Darwin BSD. Okay. Which is Berkeley Software Distribution.

**Chris Gammell:** Oh, interesting.

**Dave Jones:** Darwin Operating. Okay. So it's based on the Darwin Operating System. That's interesting.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. There you go.

**Chris Gammell:** But just the idea of then, of like, so now, even if you were doing Bluetooth, right, and you're kind of handing these packets to the phone at that point, and then you're like, eh, the app developer will take care of it at that point, you know? And it's like, that's a very different thing. Like, a lot of the stuff I'm doing these days is, you know, in some cases, like the thread stuff I do, I actually have a IPv6 address. Like, so like these little Bluetooth-y devices, they are going through a border router, it's called. But that actually assigns it an IPv6 address. So in theory, it's addressable from the broader internet. Yeah. You have to go through this router, but it is an addressable thing versus like, as far as I understand it, I think there's some way you can do it in Bluetooth, but the standard way is that, you know, a Bluetooth device, if you have a little fiptid watch talking to your phone, it doesn't have an IP address. No. It has a local address for your phone.

**Dave Jones:** You can maybe somehow map it or something. Yeah, like Bridget or Frost.

**Dave Jones:** Some bridge or something, but I don't know. But yeah, it's not. But like, they're not built for that sort of thing. Yeah. Right. You can't directly address it. And you would have to use IPv6 because IPv4, you can't do because there's not enough IPv4 addresses, right? That's the 192 dot, you know, that's the dot, dot, you know.

**Chris Gammell:** Yeah. Just the non-X type stuff. Yeah. I mean, like, I'm not sure why. I think it is because the preparation for all those addresses, but there's no like subnetting or anything like that either. Right? If you wanted to have like...

**Dave Jones:** Well, you can do ports and stuff like you can do like port mapping and stuff.

**Chris Gammell:** Well, you think about like you have a Wi-Fi address. So you say you had like an ESP32. That thing can have an IP address, but usually it's going to have like a local IP address from your, handed over from your router. So your router has like... Exactly.

**Dave Jones:** Your router maps a local one, which is not a... Well, and then you can port that through to the global network so that you can have other people access it. So that's when they come to your router IP address and then they put in a port number and you can map a port number to the local device. But that's kind of like a roundabout way to do it. So...

**Chris Gammell:** Yeah. I'm going to be honest. That's outside of my realm. But I do know that I have... I do cellular stuff very often. Those are private IP addresses. Those are on the network, but you can't really access them from the broader internet, which unthread stuff. I don't do Wi-Fi too often. But then you think about like in those cases, you know, like the internet is the internet at that point. So if I wanted to go and, you know, ping Google, I can do this. I can do that from a cellular device. I can actually like send out a ping over the network and it should get to the Google side of things. Whereas like a Bluetooth device, it would still have to go through the phone. The phone is serving up any kind of traffic that way. So yeah. Networks, Dave.

**Dave Jones:** Yeah. I don't know. That's not...

**Chris Gammell:** Let me tell you. Speaking of cellular, I am about 16 days away from leaving for Embedded World and I'm freaking out a little bit. I am in demo mode. Yeah. I just hand assembled eight boards tonight. Oh, nice.

**Dave Jones:** Yep.

**Chris Gammell:** And I got another eight to do tomorrow and I got a lot of testing to do.

**Dave Jones:** These are like stand demos, are they? So that people can play with them? Yeah.

**Chris Gammell:** Yeah. Some of them are going to be like walking around demos. Some of them are going to be stand demos.

**Dave Jones:** Oh, okay. All right.

**Chris Gammell:** A lot of 3D printing happening here. Some laser cutting. I'm just like a maker. I'm like a maker space in here, Dave.

**Dave Jones:** Cool bananas.

**Chris Gammell:** I have to do some vinyl cutting. I have a vinyl cutter now. Did I tell you that?

**Dave Jones:** No. No. There you go. Sticker cutter. Wow.

**Chris Gammell:** Those things are super fun.

**Dave Jones:** So it's got one of those blades, right? That sort of like goes around and... Right.

**Chris Gammell:** Yeah. So it's like basically the blade goes kind of across the X axis and then it like pushes the vinyl paper or the vinyl sticker in the wider axis then. And so then when you map that, it basically can do a 2D shape like a circle or, you know, just a text or whatever.

**Dave Jones:** How does it like stretch the paper material sticker thing?

**Chris Gammell:** Maybe by stretch it.

**Dave Jones:** Because otherwise, like if you don't stretch it, if it just like, like how do you hold it in place? Otherwise it'd just tear it or whatever, wouldn't it?

**Chris Gammell:** Right. Yeah. There are some limits, some lower limits. The thing that moves the vinyl in and out is like a tensioner rod basically. So it has a really strong...

**Dave Jones:** It's a platen. It's a roller platen. Oh yeah.

**Chris Gammell:** Yeah. That's a good way to think about it. Yeah. That's right. Yeah. Yeah.

**Dave Jones:** Got it.

**Chris Gammell:** And so that has like downward force and it's got a really strong grip on the vinyl and that's what actually makes it, that's what gives it tension.

**Dave Jones:** Yes.

**Chris Gammell:** And it's like a known distance across as well.

**Dave Jones:** Right.

**Chris Gammell:** But like then it's like super easy, super easy to like just drop in an SVG or something like that. And then the limit is just your, your imagination.

**Dave Jones:** Nice.

**Speaker ?:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Vinyl cut sticker front panels.

**Chris Gammell:** That's exactly what I'm doing. Yeah. Yeah. Yeah. So I have a, I showed you last time I made a PCB front panel.

**Dave Jones:** Yep. Saw that.

**Chris Gammell:** And it's kind of E-ink display, some backlight LEDs. I'm doing some vinyl cutter stickers on it. I should mention.

**Dave Jones:** Why an E-ink display over a traditional LCD or OLED?

**Chris Gammell:** Yeah. That's a good question. The thought is that it showcases, you know, like, so these are cellular devices. And so the whole thing is on. Low power.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Low power. But really, you know, when you think about a lot of like cellular devices, if they're, if they're going to survive out in the wild at all, they're going to be mostly shut down all the time.

**Dave Jones:** Yeah.

**Chris Gammell:** And with E-ink, when you update the screen and then you shut the whole thing off.

**Dave Jones:** It stays.

**Chris Gammell:** The display still is there. So that's kind of cool. Yeah. Yeah. And plus it's like super crisp. It looks great in like, like lighting conditions. So yeah, it definitely is a hassle, but like in terms of the updates, but yeah.

**Dave Jones:** I think E-ink technology is one of the radical game changers in, in tech. I think, you know, cause like just the ability to have a display, just stay there with no power is just, wow. Mine. Yeah. It's, it's a, it's a freaking mind blow yet. We sort of take it for granted now.

**Chris Gammell:** Yeah. It's just like, Oh, a Kindle. No big deal. Yeah. Yeah. Right. It just stays there at this point. Like, yeah. Yeah. Yeah. I mean, low power, less for like my Kindle last.

**Dave Jones:** Zero power. It's literally zero power. It only draws power when, when you, well, yeah, there's a residual power. Cause it's, it's checking for the capacitive touchscreen. Right. Right. Right. But apart from that, right. Technically, if you turn it off, it's off and the image is still, the, the book cover

**Chris Gammell:** is still there. Sure. Yep.

**Dave Jones:** Like, you know, wow.

**Chris Gammell:** Yeah. You do Kindle. Yeah. Yeah. For you.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. I'm on mine pretty much every night and, you know, probably like 20 minutes or so. And I think it goes 30 days. Pretty standard. Oh yeah.

**Dave Jones:** You easily get a much use out of Kindle. Yeah. Yeah. Yeah. It's great. Yep. Fantastic.

**Chris Gammell:** Yeah. I don't see it on a lot of products. It's still pretty expensive. So like this is a 200 by 200 screen, probably 12 centimeters by 12 centimeters. Not like a big screen. Yep. And it's five bucks. Yep. Like not cheap.

**Dave Jones:** But when you say expensive, right, you got to remember they use these for disposable things.

**Chris Gammell:** Yeah.

**Dave Jones:** Now it's just like.

**Chris Gammell:** Oh, like those tags in the grocery store.

**Dave Jones:** About e-ink shipping labels for goodness sake.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** That just a one-off thing goes on a package and then you toss it out. Like, hold. No.

**Chris Gammell:** I've never seen that. Have you seen that? I've never actually seen that.

**Dave Jones:** Well, I've heard talk about it because they're so, you know, apparently cheap in volume if you want like a real simplistic one or something like that. Yeah. And they're using them for supermarket like labels, shelf labels now. You know, they've got those. Yeah.

**Chris Gammell:** I've seen that. Yeah. That's cool. I think that's a, that's a great use of them. And there's, I forget his name, but there's a hacker out there who basically like buys us in bulk and reprograms them. Yeah. Yeah. It's great. People that sell them for grocery stores are like super cheap.

**Dave Jones:** Yep.

**Chris Gammell:** I forget. I forget who that is. Yeah.

**Dave Jones:** When you buy them in that sort of volume, you know, cause like one, one, one store would need what? 10,000. Oh yeah. Yeah.

**Chris Gammell:** How many skews is in a, you know, just a large grocery store. Yeah.

**Dave Jones:** Single store. Oh yeah. Yeah. It's a great use, you know, but at least they're not disposable.

**Chris Gammell:** Yeah, exactly. Yeah. The reprogrammable at that point. Yeah. And they have like, there's some, I forget how they update them. Maybe RFID or something too. Well, that's the other thing. It's cool.

**Dave Jones:** Yes. Yes. They do update them via a RFID resonant coil in there, I think. So you come along with the programmer. So there's no battery in there. They come along with the programmer and it energizes the coil and then it updates the display. And then once you remove the little handheld programmer thing, it's done, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** So, and there's the, I can remember I was working way back when.

**Chris Gammell:** Are you saying there's wireless power, Dave? Is that what you're saying? Yeah, there is wireless power. Couldn't help myself. It was all the rage.

**Dave Jones:** Back when RFID tags were big, I'm talking probably late 90s, something like that, you know, all the rage and all the talk at the time was, oh, RFID tags will be embedded. And, you know, these disposable RFID tags will be embedded in everything. Everything. Every single box that you ship will have an RFID tag on it because these things will be so cheap. You know, these little glass, back when they were like glass sphere kind of, you know, things and they'd be taped to you and they were so cheap. And they still are, I think, because there's not much in them. There's like a silicon die. There's a, you know, a little patch antenna and there's a.

**Chris Gammell:** Yeah, it's like chip down kind of thing, like chip on glass sort of thing.

**Dave Jones:** Yeah, yeah. You can get chip on glass or you can get the patent etched on glass as well. But, you know, but making glass isn't cheap. And then, you know, making silicon dies isn't cheap either. You know, well, it's cheap, you know, but should you use them in disposable applications where you can use a piece of paper? Yeah, you know, it's like, right, right, right, right.

**Chris Gammell:** That is the thing. Where's the crossover point of like the hassle factor of like printing up new labels? And yeah, that's a good point. Before we move on from conference stuff, I wanted to mention again, if people are going to be there. First off, I'd love to meet with you. Let me know. Second off, former guest Saber from PCB Arts will be having an event there. Free tickets. I think there's beer and maybe food. But basically bring a bring a hack style event on Wednesday night, the 15th of March. Cool. So I will have a link to that in the show notes once again.

**Dave Jones:** What swag do you have on your stand? What freebies?

**Chris Gammell:** Oh, nothing good. Oh, come on. Stickers. Stickers.

**Dave Jones:** Come on.

**Chris Gammell:** Yeah, I know. It's not a big stand. I mean, that's the thing. I'm going to be at the Zephyr stand. What's your go-to? What is the best ones?

**Dave Jones:** Well, you've got to have lollies. You've got to either have lollies or you've got to have like a PCB ruler or something useful like that.

**Chris Gammell:** PCB rulers. That feels like e-waste to me. I know that you are famous for your PCB ruler and DigiKey likes their ruler. I personally, I've seen so many of them. I'm like, these are just getting thrown out. I don't take them ever anymore.

**Dave Jones:** Yeah, but you've got to make them practical. You've got to make them like- Sure, sure.

**Chris Gammell:** I don't use rulers though. You know what I mean? You don't use rulers.

**Dave Jones:** Really?

**Chris Gammell:** No, I use calipers if I'm measuring something.

**Dave Jones:** I don't have a PCB ruler right in front of me. I've got a proper engineering ruler.

**Chris Gammell:** Sure, sure.

**Dave Jones:** Like a proper-

**Chris Gammell:** For measuring stuff or for the lookup stuff on it? What do you use it for?

**Dave Jones:** No, it's an actual ruler. It's for measuring stuff. And this is a proper engineering one and it's standard. Yeah, yeah. It's, you know, it's actually rated for a specific temperature. So it's standard at 25 degrees C, it says on here. Yeah, that makes sense. And it's made in the United States of America, USA.

**Chris Gammell:** Oh, nice. It's got metric on it, huh?

**Dave Jones:** Inches on one side, metric on the other. Oh, it's got both. And it's got your different scales. So, you know, your weird ass, you know, one-sixteenth of an inch and all that sort of rubbish, you know?

**Chris Gammell:** Yep, yep.

**Dave Jones:** Yeah, and then it's got, you know, 0.5 mil on the other side. So that's not imperial mil, that's metric mil.

**Chris Gammell:** If I'm measuring anything, I'm measuring it with a set of calipers. Anything past like six inches, I'm probably going to a tape measure.

**Dave Jones:** No. Every time I go to use a bloody pair of calipers, the battery's dead. You know, like every time.

**Chris Gammell:** I have that problem too. Mine also, yeah.

**Dave Jones:** I swear I'm just going to get an old-school dial one because it's just, like, I'm just sick.

**Chris Gammell:** That's a bad idea.

**Dave Jones:** Yeah. I think I'll just read it.

**Chris Gammell:** Another thing to note is that the cheap ones, they don't have enough downward pressure. So another thing that I do, another tip for the caliper people out there, slide a piece of paper in underneath the cover so that it kind of pushes between the catch of the cover. You know, obviously you can't block the battery contact. Or no, actually you can. Sorry. It's only once it gets the rim to the center, right?

**Dave Jones:** It's usually a bottom contact on the PCB and then a rim thing.

**Chris Gammell:** Right. So you can actually put a piece of paper on top. So you basically, like, take a piece of paper, put that in there. If that just worked, fold it over once, try again and fold it over again. And then, like, that, for me, it was almost always the battery was loose.

**Dave Jones:** Yep.

**Chris Gammell:** So try that. See if that helps.

**Dave Jones:** That's another piece of tech that I'm absolutely amazed by. Have you, like, even the cheapest piece of crap, you know, Shenzhen Market $5 digital calipers, they're so super accurate. And you can't trick them, right? Right? Like, like, like you stand there trying to trick it by moving it really fast. Oh, yeah. I'm going to beat this thing, you know? And you can't.

**Chris Gammell:** It's incredible. I can't. It depends on the piece of crap. If you, if it's not the rack and pinion style. So, like, that is basically my minimum is that it has to be rack and pinion. Because there's, like, the really, really cheap ones where it's basically just, like, a roller on, like, a piece of plastic. And, like, that can skip.

**Dave Jones:** But they're, no, they're all like that because they use a capacitive sensor inside. They use a capacitive surface inside to actually detect. So, it doesn't matter if it slips. It's the movement of the capacitor and how fast that they can read it and update it.

**Chris Gammell:** Oh, maybe I don't know how calipers work. Okay. I thought it was, I thought it was number of rotations.

**Dave Jones:** No, I haven't seen a roller one for ever.

**Chris Gammell:** Mine's rolling, rolling right now, Dave. Really?

**Speaker ?:** Yeah.

**Dave Jones:** Okay. They do have an external thumb roller on them. But that's not what does the counting. That is not what does the counting. That is just a convenient thumb roller on it. It's got, like, I'm going to have to get mine out now. Was it in the channel?

**Chris Gammell:** Sorry. I don't actually know how this works, I guess. Yeah.

**Dave Jones:** Mine's actually got a thumb roller on it. Yeah. Mine is a thumb roller as well. But, no. But that is only for your convenience of, you know, because with that, you can do sort of, like, micro adjustments. Fine adjustments. Yeah. That is not how it works. In fact, mine doesn't even make contact. My roller wheel actually pivots off it. So, it's only when I push on it does it actually make contact. No. These are actually capacitively sensed.

**Chris Gammell:** I feel like there's a video in here, Dave. This is good. You should make a video. Yeah.

**Dave Jones:** I was going to, but then other people have already done it.

**Chris Gammell:** Oh, okay. So, I should look it up.

**Dave Jones:** There's quite a few videos out there. If you search for how digital calipers work, there's tons of videos out there.

**Chris Gammell:** Caliper videos. Yeah. Okay.

**Dave Jones:** But, I should maybe, you know.

**Chris Gammell:** No, I don't.

**Dave Jones:** Anyway. So, I do have a brand one here. I actually paid for a good quality brand. Mine's a iGaming one. iGaging. Mine's an iGaging brand, which is apparently like a more upmarket. Mine's the Easy Cow iGager. So, it's premium quality.

**Chris Gammell:** Anyways. Yeah. So, I would use that over. Although, I don't know how they work, apparently. I would use a caliper over a ruler most days.

**Dave Jones:** It depends on what you're doing, you know. If you just want to.

**Chris Gammell:** I don't know.

**Dave Jones:** If I was ever to get a tattoo, I would go the Adam Savage route and get a ruler tattooed on my forearm. Oh, yeah. What about saggy skin, though? No. But, it's just, you know. It's good enough for Australia, right?

**Chris Gammell:** Okay.

**Dave Jones:** It's like, you know.

**Chris Gammell:** Jimmy Rogers, who's in the maker scene, actually got resistor color codes. Like a rainbow of resistor color codes. It was great.

**Dave Jones:** Actual colored tattoo with the color code. Yeah. Yeah. Like all of the different colors. Oh, wow.

**Chris Gammell:** I'll see if I can find a photo. It's great.

**Dave Jones:** Wow. Yeah. Yeah. Yeah, please. We can include that as the thumbnail if we can find the photo.

**Chris Gammell:** Dave, we don't own that image. We don't own it. Remember?

**Dave Jones:** Oh, you come on. But it's easier to see. Did you see the thing about. It is to seek permission.

**Chris Gammell:** The lawsuit up against Mid Journey and Mid Journey and all the others. I heard something about.

**Dave Jones:** I haven't looked into details about. Yeah. Yeah.

**Chris Gammell:** Yeah. I don't know what the. It's going to be interesting what happens. It comes out of it. I don't know. Yeah.

**Dave Jones:** Yeah. But then if you. But then their defense can be. Well, you allow Google to index your images. So. You know.

**Chris Gammell:** I don't know how the legal stuff is going to work out. It's a copyright claim thing. So it's the US. Yeah.

**Dave Jones:** If you're suing us and not suing them. Eh. You know. It might be like. I don't know. Right. I'm not a legal expert. Right. But I. My spidey sense tells me that it could be something along the lines of patent law. Like if you don't defend your patent. Like legally. Then you kind of lose the right to do it. That is ingrained in somehow in patent law. In some aspect. Some aspect.

**Chris Gammell:** Yeah. I know what you mean. But yeah.

**Dave Jones:** I know it's not 100% correct. That's a trademark. Sorry. Trademark. Yeah. Yeah. Sorry. Yeah. Trademark. If you don't defend your trademark. If you let people. You know. Buy. If you let people actually abuse your trademark. And you don't defend it. You can't. That actually makes it harder for you to defend. Against someone else later. Yeah. So I think a similar sort of thing might be at play here. Don't quote me on that. But I.

**Chris Gammell:** I don't know if I agree with that. Yeah. But I think a lawyer could. One thing that. That did happen in the US though. Is that. Generated images then. So like if you generate images from. Mid Journey. Whatever. Mid Journey. Those cannot be copyrighted in the US right now. Yes. Yes.

**Dave Jones:** Yes. That's right.

**Chris Gammell:** If people want to steal our blog art. And spread. Spread Ampower blog images around. Actually. We would. We would appreciate it.

**Dave Jones:** Which I think is fine. Because that's not really the issue. The issue is. Yeah. The artist who owns the original work. It's based on.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** I don't think anyone who generates anything. Using Mid Journey. Is concerned about. Copyright. And it. Like. I think that very.

**Chris Gammell:** Well people are like making books out of it. So. I've actually talked to my wife about this. Like. Like doing a children's book. Would be pretty easy. Right.

**Dave Jones:** Yeah. But what. People are going to steal. Steal your cover. Well. You know. So be it. But.

**Chris Gammell:** Well. No. No. No. So if you can't enforce copyright. You don't own the characters then. Right. So then like. So then nobody's going to publish you. So like. Say. Say I went and made a. Oh. Okay. Right. I talked about with my wife actually. It was like. Oh. It'd be fun to like. Use Mid Journey. Make a. You know. We've got some ideas. Right. Right.

**Dave Jones:** You can make a kid's book or something.

**Chris Gammell:** Read enough of them. Everybody thinks they can do one. Right. And I was like. Oh yeah. We could do that. But then. But then. We could find a publisher. But if. If you. Can't publish. If you can't. Copyright. Generated images. They're not going to invest in the IP. Right. Right. It's not defensible.

**Dave Jones:** Yeah. But is that their problem? Because they're. They're just the publisher of the book. They just sell books. They don't.

**Chris Gammell:** Well. What recourses do they have then? Right. I mean. They're basically. You know. Most publishers are just IP houses. Right. They're.

**Dave Jones:** Yeah. True. Yeah. Then somebody else could come along and sue you to take down the book.

**Chris Gammell:** It's not hard to print a book. It's not hard to download it to a Kindle. Right. I mean. Like. You can download the EPUB. Right. And if it was broadly put on the internet. And you didn't have any recourse against it. You couldn't. You couldn't sue the person that had put it on the. Yeah. On a website. And everybody downloaded it. So. Yeah. I don't think publishers would go for it. Right.

**Dave Jones:** I think you might be right. Yeah.

**Chris Gammell:** Yeah. It's too bad.

**Dave Jones:** Yeah. Well. Wow. Stealth publisher needs a publisher these days.

**Chris Gammell:** That's true. That's true. Yeah. Speaking of IP. Former guest of the show. And. Silicon Wunderkind. Will be generating some IP in the near first future. Because. Sam Zaloof. Has started a chip company with. Someone. Jim Keller. I don't know who Jim Keller was. Jim Keller. Should I know who Jim Keller was?

**Dave Jones:** Well. You should. He designed like. The. Some AMD chips. And the Apple A4 processor. And all sorts of things. I think. So. He's a huge. Like. He's probably one of the big names in the chip industry. If you're. Into the chip industry. Yeah. Jim Keller is like. You know.

**Chris Gammell:** I mean. He was. He was smart to get into business with that. With that legend. Yeah. Yeah. Yeah. Right. You know.

**Dave Jones:** I would love to know how that connection came about. Actually.

**Chris Gammell:** You know. I had breakfast with Sam. Right before I moved out of Chicago. So that's by a year and a half ago now.

**Dave Jones:** Yeah.

**Chris Gammell:** And he was talking about some of the. Or I saw him at a conference. I think too. But. I think he was trying to build a fab for fabs. He talked about. Maybe that's what they're doing. Right. I don't remember. But. Anyways. We. We knew. I mean. We knew this kid was going to do something crazy. Right. Totally.

**Dave Jones:** Yep. I actually. I did. Listen to that episode. Just the other day. So. Yeah. Yeah. Yeah. It's great. Yeah.

**Chris Gammell:** Yeah. We should see if. Maybe. Maybe both of those two would like to come back on. We'll. We'll. Give them a shout. But. Yeah. So. They raised a bunch of money.

**Dave Jones:** They raised 15 million bucks from. And. This is the interesting thing. Who the money's from.

**Chris Gammell:** This is interesting.

**Dave Jones:** It's from open AI.

**Chris Gammell:** I know. Right.

**Dave Jones:** Right. Right. So is there going to be. Like. Why would open AI invest? They're not. Like. You know. Investing something that's not really related. To their industry. So it's not like they're an investment company. Right. So why would they do that?

**Chris Gammell:** They're not making any money yet. So. No. But.

**Dave Jones:** Unless. Some open AI tech. Is going to be used. In the design. Of the chips. Perhaps.

**Chris Gammell:** Maybe. It'll generate memes. And then they'll put that into silicon.

**Dave Jones:** Right.

**Chris Gammell:** What do you think about that?

**Dave Jones:** Sounds good.

**Chris Gammell:** Yeah. Yeah. Sounds good to me.

**Dave Jones:** I'm all for me.

**Chris Gammell:** Yeah. Yeah. Well. Anyway. Go Sam. Go Jim. Yep. So yes.

**Dave Jones:** There's a $15 million investment for $100 million valuation for this startup. And they're hiring people. So you can. That's the only thing on their website at the moment is some jobs going. So they're hiring people. So if you're a hardware. I think they've got a process engineer. A hardware engineer. I don't know. Software or something. So they're. And. And. And they're going to be building their own fab equipment. Where it's not already available.

**Chris Gammell:** I've done all those things. I could. I could go work there.

**Speaker ?:** You could.

**Chris Gammell:** I've been a process engineer. I've been a hardware engineer. There you go. I've written some software. Yeah. Boom. Yeah. I'm the perfect. They can't afford me. They can't afford me.

**Dave Jones:** A hundred to $150,000 for the process engineer. Which doesn't sound like much for Silicon Valley. Someone just mentioned this on Twitter.

**Chris Gammell:** Oh. It's like.

**Dave Jones:** You couldn't even get lunch for $100,000 in San Fran. Can you?

**Chris Gammell:** I don't know about in the Bay Area. But I do know that, you know, process engineers, so like, don't get paid a ton. Because usually they're not. You know, you think about like versus like a. I don't know. Like a DevOps engineer. Right. Like someone who's doing like deploying large servers and stuff like that. Yeah. Like there's just not as much demand. It feels like.

**Dave Jones:** It's a pretty unglamorous industry. Right. Yeah. It's not a high profile, high competition. That works in it. Yeah.

**Chris Gammell:** Honestly. Honestly. I think the other thing too is that the most process engineers come from chemical engineering. Right. And so. Right.

**Dave Jones:** Okay.

**Chris Gammell:** The best ones I knew were chemical engineers. Right.

**Dave Jones:** Makes sense. Yeah.

**Chris Gammell:** And I think there's just a lot more of them. They don't get paid. You know, like if you're working in petroleum in the US, you get paid really well as a process engineer. Yep. But like.

**Dave Jones:** Oh, you would get more in the chemical industry for driving the truck at the mine that mines the chemicals than you would for actually, you know. See, I'm completely serious. You would get paid more for driving the truck at the mine that mines the chemicals.

**Chris Gammell:** I mean, it's hazard pay.

**Dave Jones:** Yeah. Well, you know, it's like, yeah, it's a weird world. It's not a equitable world. Let's put it that way. Yeah. Yeah.

**Chris Gammell:** I think it's, it is detached. You know, like value is detached from pay in a lot of industries. That's just the way the world works. That's just how the quickly crumbles, man. Yep. And sucks.

**Dave Jones:** But anyway, they are after, I think you only need like a year or two experience or something like that. So it's not like they're after like some, you know, industry veteran, veteran process engineer or something. So, yeah. But the interesting thing is, is that they're supposedly talking about, well, if we don't, if we can't buy the stuff we need, we're going to make it, you know, and they want to own the entire process from start from raw silicon, you know, right up. So, yeah.

**Chris Gammell:** You know, Dave, it says Atomic Semi on their job listing. It says Atomic Semi is building a small, fast semiconductor fab. You know, it doesn't get much smaller than on the desktop.

**Dave Jones:** It's not going to happen, dude.

**Chris Gammell:** Still clinging onto that hype, dude. If it was going to happen, I think it's, I think it's Sam's aloof. I think Sam is, I've told Sam, he's, he's my only shot. So if anyone's going to do it, it's him.

**Dave Jones:** Yep. But sorry, dude.

**Chris Gammell:** Probably not.

**Dave Jones:** Still stands. I'm happy to give you another 10 year bet. You lost the last one. Yeah. Okay. You know. Happy to give it to you.

**Chris Gammell:** Yeah. Yeah. That's, that's very, very generous of you. Very generous.

**Dave Jones:** I'm happy to keep extending it every 10 years. It's like, uh, it's, it's like fusion, you know? Yeah. It's just not going to happen, dude. Dream on. Dream on.

**Chris Gammell:** Other things that are dreams and other people who've been on the show in the recent past. So Matt Venn was on the show talking about silly whiz, silly whiz, silly whiz. And that is something he worked on with another guest of the show. Uri. Shockhead out of Israel. And it is now generally available. So app.sillywhiz.com. We will link that in here. You can go and try it out.

**Dave Jones:** And just bam. I'm straight in. Do I have to sign up? It just, there it is. I've got my, I've got my Silicon designer and I've got like a DRC cross section, which shows the vertical. You know, you can see if you've got any DRC errors on your Silicon and it's just, just there. Bam. Yeah.

**Chris Gammell:** Straight in. Yeah. There starts, you start with presets here. So like if you're doing, if you're following along at home, if you click on the preset, you click converter. That's right. So you see the gates here.

**Dave Jones:** What is a skull fet? What is a skull fet? Oh, it's actually got a skull and crossbones. It's actually a fet made with skull and crossbones.

**Chris Gammell:** Uri makes a puzzle with skulls in it. So I think it's got to be said. Okay. All right. Yeah.

**Dave Jones:** That's hilarious.

**Chris Gammell:** Yeah. And so, I mean, like the inverter is like a classic thing. You, like Dave said, you can have a cross sections here. One thing I didn't mention the day before the show as well, in the upper right corner, there's a link to the lessons and that goes to basically kind of a walkthrough. Like, so like how do you think about parasitics? How do you think about how to actually draw capacitors, draw a FETS, draw a logic inverter? So like, so building up from scratch as well, because this is even something that I think, you know, if you, this is a level below when Matt was on the show, he was talking about this. This is a level below how most of the time. You're doing this kind of stuff. Usually you're not individually tweaking like an inverter. It's going to generate that for you from Verilock, right? It's going to actually do that for you.

**Dave Jones:** That'd just be a standard drop-in thing you, you would get from the silicon vendor.

**Chris Gammell:** Right. Yeah. You get cells and it uses the cells there. But then if you wanted to then go and do an analog design. Oh yeah. That's totally different.

**Dave Jones:** You got to tweak it manually. Yep.

**Chris Gammell:** Right. And that's, that's basically what's going on here. So then now you can click on something like the input gate you can, or sorry, on the, you could modify the width of like the gate. You can change the thickness of the gate as well. And then you can actually see how the curves change and how, uh, you know, if you have different pulses coming in or what does it look like? And it's, I don't know. It's just like, it's amazing. I mean, really, it's just amazing. Yeah.

**Dave Jones:** It's, this is begging for AI. This is begging for support. Like, oh, please make my MOSFET a bit faster. And then it just redraws the geometry to make it faster. Oh, please, uh, trade off power consumption for speed, you know? And, and it just knows how to do that. Right.

**Chris Gammell:** Yeah. It's kind of interesting too. So we were just talking about like, you know, what, what is process engineering? And like one thing that you would do as a process engineer there is basically you would say like, you know, you'd design an experiment and you'd say like, okay, I have a, I have a theory that if I change the width of the input, the input, uh, gate, right.

**Dave Jones:** Yeah.

**Chris Gammell:** Then I think I'm going to like map it from, uh, width a to width B and then, you know, you do that. And then you, you also, then you do a cross with maybe another theory, like, oh, I'm going to change the, the, uh, P diffusion depth. And I think that's going to have this other effect. And then what you do is you kind of run these different things in parallel and you see like what has the most impact from that sort of thing. And like, that's also what an AI would do if it was doing that sort of thing, but you can do this.

**Dave Jones:** Well, they do have, uh, simulators for this sort of thing, right? You, you, you, you can simulate like, like you don't have to do the physical experiment like each time you want to do that.

**Chris Gammell:** This is a simulator. This is a simulator. Yes. But yes.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah. Yeah. Yeah. That would be like, figure what that command is, man. It's been a while since I did spice. Oh, I told you about it. Remember I, I told you I downloaded spice. I know I'll do spice on my computer. Right. Yeah. Yeah.

**Dave Jones:** And it had, yeah.

**Chris Gammell:** I had like, uh, it had like, like notes from 1999 in there. Like, yeah, that's great. That, uh, Mike wants to put in there.

**Dave Jones:** Yeah. That is great.

**Chris Gammell:** Apparently Mike, uh, so Mike Englehart, who was on the show way back when he, he was at LTSpice. He left, he left ADI when, so like LTSpice is now part of analog devices. Mike's no longer there. He is now releasing some new simulator soon. That's independent. Yeah. Oh, there you go. Wow. I got another one.

**Dave Jones:** He actually branched his own code. Did he? Is it, cause it's LTSpice is an open source, right?

**Chris Gammell:** It is not open source, but he was the, the big maintainer of it. And we'll, we'll link in that episode as well. That was.

**Dave Jones:** So did he write it again from scratch?

**Chris Gammell:** I think he did. Oh, yeah. Yeah. Crap. Right. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Jeez. I remember that episode. I think it was just me. I don't, do you remember? Yeah.

**Dave Jones:** I think it was just you. Yeah. I don't remember.

**Chris Gammell:** Yeah. He said so many software terms. Like I remember like literally like having to catch my breath that I was so confused about, about like what was going on and what he was saying. Like I'd really. Yeah. Yeah. It was, it was tough. My brain hurt afterwards. But I will link in the name. It had like a weird name. It was like something like Roman, like Latin. It was in Latin or something, but there's a new simulator coming. So.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah.

**Dave Jones:** Cool bananas.

**Chris Gammell:** You can download LT.

**Dave Jones:** I was just asking, I can't remember who or where I was asking it, but like, what is the latest, maybe it was you all casually talking about it. What is the latest go-to simulator these days? Yeah. I think before a show the other week, I think we were.

**Chris Gammell:** Yeah. I think we were talking about it. Talking about it. Yeah. And I said, I don't know. Yeah.

**Dave Jones:** Same here.

**Chris Gammell:** Keycat has it built in now. It's just okay. They're like, that's PSPICE. LT. SPICE is still, you know, good. Honestly, like if I'm doing something fast, I'm probably going to false dead just because I love how it animates and stuff. I think that's.

**Dave Jones:** Oh yeah. If I'm, yeah. If I'm doing a simulator, I'm just going to one of those web things. And usually I don't want to simulate my whole design. I just want to simulate like a couple of transistors or something. You know, I just want to like a little building block. That's right. So yeah. Hmm.

**Chris Gammell:** Yeah. There you go. To Matt and Uri though, this is, I'm very excited about this Silly Wiz thing. And I think that's going to be great. Yeah. Yeah.

**Dave Jones:** Really looks cool. Agreed.

**Chris Gammell:** Speaking of, you know, we might as well hop back on that AI train. I heard, I heard rumor that you tried to get someone to do your homework for you.

**Dave Jones:** Somebody did do my homework. The, uh, the, the bot did my homework.

**Chris Gammell:** Yeah.

**Dave Jones:** You know how I've been working on this, uh, MacGyver project, I call it, which is a BOM, which looks like a B-O-M-E. So we don't get demonetized. Well, this isn't monetized anyway. So BOM, it looks like a BOM. BOM. Yeah. Right. Right. It looks like a BOM. It's a BOM countdown timer. Right. Hello NSA. You know, if you're listening.

**Chris Gammell:** Yeah. Right. Right.

**Dave Jones:** Yeah. We just triggered, you know, all we have to do is mention the, uh, president in the same sentence and where we're going to get flagged at the NSA. Yep. Anyway. All right.

**Chris Gammell:** Deep set it.

**Dave Jones:** So yeah. So I was originally going to do like a, how to design part three was going to be how to design it using discrete TTL logic.

**Chris Gammell:** Mm.

**Speaker ?:** Mm.

**Chris Gammell:** Mm.

**Dave Jones:** And, and then I was going to show how, okay, you need like 30 chips or something. And then I was going to show how you convert that into a single eight pin micro. Right. And, uh, but then I thought, no, why can't I just get, Hey, it'd be more interesting and get AI to actually see if it can drive this display because it's an interesting thing. What I'm trying to do is drive five, seven segment displays connected to five shift, shift registers, right? 7,400 series shift registers, seven, four, one, six, fours. Right. And so it's got a serial clock in, it's got a serial data in. And, you know, so I thought this is like an interesting experiment for chat GPT AI to see if it can, like, I, I know that chat GPT can write code, right? Can you write code for almost anything?

**Dave Jones:** Arduino code. For Arduino, somebody said it can even write code for that PDUK. Oh, really? Three set microcontroller. Yeah. Somebody said it even does that. So it just, I don't know, it just trawls GitHub and finds all this code and just magically, you know, learns it. Right. So it can do practically any language. It can generate assembler for pick. I think somebody said, you know, it can do like.

**Chris Gammell:** So like, I do wonder about the depth of that too. So like, you know, as a prompt engineer. Yes. One thing that's tough is like, how, how many like nested statements could you get? Like, I want it to run a timer, but I also want it to do this. And I also want it to do that. And I also want it to do that. You know, like, that feels like that's where it's going to get gummed up as well, because it's just describing all the things you want it to do.

**Dave Jones:** Right. If it's trying to do like a real time interrupt driven thing, can it handle that? I don't know. But anyway, so I thought this was an interesting, like, so I know I can write code. I know I can write Arduino code, no problem. But can it, can I describe a hardware circuit with seven segment displays and shift registers? Can I understand that? And then how to drive that and translate that in, and how to, and can I translate that into an English? Cause it's a language based processor, right? It only understands English language.

**Chris Gammell:** Right. Right. Cause you wouldn't be, if you were explaining this to me too, you wouldn't want to like, you wouldn't want to send me a schematic, right? You wouldn't want, you wouldn't want to say, oh, well actually pin five of chip one is tied to pin seven of chip two.

**Dave Jones:** So yeah. So what I did is I thought about it for like two seconds. I didn't even put any effort into it. Right. I thought about how can I explain the function of this circuit in a few sentences. Right. So you can see it in the video. I, you know, as a few sentences, I, I type in and bam, it got it practically first go. There are two bugs in the code that it got. It got a complete newbie, newbie mistake where it, uh, it was decrementing a variable in a loop that it should have made a temporary copy of first and then operated on the temporary variable. Right. So it was decrementing the loop value. Right. Which was dumb. Right. It's just a complete newbie mistake. Right. So it made that mistake.

**Chris Gammell:** If people are trusting this thing and like trusting it for increasingly interesting and dangerous things, it really scares me that it might be basing anything off of my old code. Right.

**Dave Jones:** Same here.

**Chris Gammell:** It's available on the internet. So it has consumed my code.

**Dave Jones:** It has. It, it uses it.

**Chris Gammell:** It has taken my knowledge and added it to the repository. Right. Yeah.

**Dave Jones:** More logic trademark. Yeah.

**Chris Gammell:** Yeah. Oh boy.

**Dave Jones:** So anyway, and the, and the other bug was that it didn't realize that the Arduino had a 16 bit integer and not a 32 bit integer. So I was, I was playing with a five digit number that exceeded the integer value of 32,768. Right. So it exceeded that. So that's why it actually failed. It actually compiled fine, but there were two bugs that made it didn't work. And, and it did ultimately require a human, i.e. me to fix those bugs. But geez, it was, I couldn't believe that it actually understood the function of shift registers. It understood the mapping of seven segment displays. It got the mapping all correct. I would like to think that's because of my prompt engineering skills. I actually described it in an adequate detail. I'm sure that played a role, but, but it understood that a seven segment display and understood that it had a decimal point and understood that it had to generate a routine to map all of these segments to the digits. And then it needed to shift them out in the correct order in the correct thing. And it was just, bam, it nailed all that. So it actually understood hardware and then translated it into software to drive the hardware. It's really quite something. This is different to just writing code.

**Chris Gammell:** Here's an interesting question. I mean, that's, that is impressive. Like, yeah, both on the prompt side, like that's, that's non-trivial. And so I'm excited to watch this actually. Here's a question for you. If you hired another helper like David too.

**Dave Jones:** Yep.

**Chris Gammell:** And he came up and he said, I wrote this code and it works. Yep. And then a week later, he's like, you find a bug. And then he, then he blamed it on, I'm not saying David too.

**Dave Jones:** I'm going to say Bobby McGee.

**Chris Gammell:** Bobby McGee here is, is the new, is the new person. And then later he said, actually it was chat GPT. It wasn't me. How would you feel about that?

**Dave Jones:** Oh, to find out my employee used chat GPT.

**Chris Gammell:** Yeah. That's the interesting thing, right? I wouldn't care.

**Dave Jones:** I'm paying them to do a job. Can you get the job done? I don't care which tools you, well, I kind of do care which tools you use. Right. And there is some care there, but ultimately bottom line is, can you get the job done? Whether or not you're a genius who hand, who, you know, codes it in assembler or whether or not you're a, you know, somebody who is really great skilled at, you know, using chat GPT. I like ultimately engineering is about getting a task done.

**Chris Gammell:** Is the solving the problem. I totally agree. I think the real thing is like, I'm not sure I trust the. The thing enough. And now you're basically putting ghosts into a machine as well. Right. Like, so like, what if they're not good enough to find a bug? Right. You know what I mean?

**Dave Jones:** Like that is the thing. The, the chat GPT did find the bug with the integer, but only because I prompted it. Like I knew it was a bug and I prompted it that, Hey, do you think something's wrong here? And then it rechecked it. So it was like, so it required without that human knowing that the bug was there, it, it would not have solved that.

**Chris Gammell:** Right.

**Dave Jones:** And, and then.

**Chris Gammell:** It's just an interesting, like.

**Dave Jones:** And the interesting part about this, right. It really tries to help you. Right. So even if somebody, I asked this on Twitter, is there a word for this? And somebody said, bot splaining. Right. Which I think is a pretty good term. Right. So I think I'm going to use that from now on. Bot splaining. What it does is the, the chat GPT will bend over backwards. Like if you tell it it's all you're wrong here. Can you fix it?

**Chris Gammell:** It'll bend over backwards to try and fix it.

**Dave Jones:** Yeah. It'll, it'll actually modify stuff that is correct and then get more and more confused. It starts hallucinating issues. Right. Seriously. The chat, it starts. That's the best description. It starts hallucinating these issues and solving problems. And you can see it in my video. It gets so completely muddled. It thought the fault. You know, I, I, I, I kept badgering it saying, you know, like there's a problem here. Can you fix it? And then it starts going, imagining that there's hallucinating, that there's a fault in the routine that there's nothing wrong with that routine. Right. And so it starts making changes to that routine. And it goes down that rabbit hole of it's that it really, rather than actually defend itself and go, no, I am right.

**Chris Gammell:** You, you must be, you know, no, it doesn't do that.

**Dave Jones:** It does not do that. It just, it bends over backwards and it'll get completely muddled up its own clacker trying to find, you know, trying, trying to solve your issue for you. It's too helpful. Right. Yeah. To its own detriment and to your detriment too, because you're trying to think, but yeah, ultimately, like I'm amazed at what it did, but ultimately it did require my human skill and knowledge of the code to actually fix it.

**Chris Gammell:** So we get another, we get another week or two before.

**Dave Jones:** Oh yeah. It's yeah. Before it learns that, you know, I, I should have given it like a tick to say, oh, let me, you know, yeah, you solve it.

**Chris Gammell:** I do think, you know, I think about like this kind of stuff and people always are like, oh, but what about the jobs that are like, oh man, bring it on. Like, I just need so much help, you know? You know?

**Dave Jones:** Yeah. So no, like it's, it's not going to take away jobs. It's going to, it's just not, I see it as another valuable tool, you know? And it's incredible. Like, especially for generating tedious stuff, like my example of mapping the seven segments to the displays, it got all that right, right? That's a tedious part of programming that I hate is like mapping stuff. If you've got a huge, you know, bitmap display, you need to map things into and stuff like that. That's kind of like the tedious work that, you know, is, is boring. If you can get the AI to just generate and do the, do the monotonous stuff, then, you know, it's great.

**Chris Gammell:** Yeah.

**Dave Jones:** But I'll tell you something more interesting. And after this, I'll probably shoot a video on it. I didn't shoot my reaction last night, but I, cause I did it late last night. I got in there and I, cause it keeps the chat that you've previously got, right? Cause you can build on your existing chat with it. So it keeps that even when you log out, you log back in. It's all got my existing chat there so I can pick up where I left off. So I asked it, I said something along the lines of, imagine that you're in a digital electronics designer, right? So, so I told it, imagine you're a digital electronics designer. Can you, can you explain how I can make this same code with 7400 series logic? Right. Cause that was going to be my next video is how to, you know, how to do the same function using 7400 series logic.

**Chris Gammell:** Like how to spit out the, so not running Arduino now. And you really are having to do your homework here, huh?

**Dave Jones:** Not running on, on Arduino, but use the existing stuff. If I've told it to, and it started like it, it thought it was the longest pause I've ever had on a chat GPT, right? It sat there for like a good 20 seconds before it, you know, started to spit it out. But then it said, certainly let me explain how to do this. I will have to, oh no, I can't, I can't give you the thing right now, but yeah.

**Chris Gammell:** I'll watch the video when it comes out.

**Dave Jones:** It basically went through step by step. You need, and then it gave me a, a, a bomb. It gave me a bill of materials. You need five, seven, four HC five, nine fives. You need X number of 10 K resistors. You need these. You need two 20 ohm resistors for the dropper. It knew and figured out that the seven segment displays were common cathode.

**Chris Gammell:** Based on current number or no?

**Dave Jones:** I don't know if it, if it figured that out or whether or not it assumed that. Cause I never used the term common cathode in my previous descriptions of it. So I don't know if it assumed it or it figured that out that it needed common cathode displays. And then, you know, so it gave me a bill of materials. Then it explained that I needed a triple five timer to generate the clock. Then it gave me the formula for the triple five timer to generate the one Hertz period signal. Then it told me I needed an inverted clock using NAND gates for one for latching the data and one for shifting the data. Right. And I, I, I haven't, I haven't drawn it up yet, but I think it's kind of wrong. Like I'm actually, I'm, I guarantee it's wrong. Right. But the fact that it did this is just stunning.

**Chris Gammell:** Like index the hackaday comments. And it's like, well, you could have done this with the five, five, five, four.

**Dave Jones:** And it just, and it gave me a bill of materials and then explained in monotonous detail. And then it ran out of path. Right. And then I said, please continue. And then, then, then it continued, you know, it needed like a part two to explain all this stuff. And I was just, even though it's not correct, like, you know, there's lots of gobbledygook in there. Right. That is not technically correct. Right. That, that, that would not solve the actual problem.

**Chris Gammell:** If there's one thing Dave can really, can really appreciate it's things that ramble on.

**Dave Jones:** Yes, exactly. But no, but I was, I was so impressed that it rambled on. And once again, it is the pleasing nature. Like the AI tries, tries to please you. And even though it's wrong, it's, it's the fact that it like, but you know, I don't know what percentage of it is actually right. Like, but there's, so there's a lot of stuff that, that helps you, you know, yes, you need these registers and you need, and then it said, oh, well the, how, how you do the counter is based on how you want to implement. And you can use several 7,400 series logic chips to actually do this. That's up to you to decide. And I can probably continue the chat and say, well, can you recommend a counter chip to do this? You know? And like, so I'm probably going to do that after this.

**Chris Gammell:** Yeah. It's interesting thinking about it too, where it's like, if it's gonna, if it's gonna put in opinion and tell you like, oh, I don't, I don't want to operate like that too. It would be like, you know, you, you really want to be doing this with 74 series logic. Right.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. If it's real old, are you sure you want to do it? Yeah. Yeah. This is very 1980s, you know? Like, yeah.

**Chris Gammell:** I have a lot of data about this, but, but are you sure you want to do it?

**Dave Jones:** You know? Yeah. It'd be much easier to use a, you know, an eight pin micro to do this. Yeah. Right. Actually, I could ask it that would is, which is the most efficient way to do this using a microcontroller or using seven, 400 series logic, you know, to see what it says. But, uh, I know I'm just stunned that it, wow. It went into so much detail, even if the detail is not, you know, only 50% correct. The fact that it could do it, you'll, you'll be amazed when I show you the printout that it gave me. It's just, you know, yeah. Even though it's wrong. I don't care. I'm just like stunned at the technology. Wow. Just wow. Yep. Blown away.

**Chris Gammell:** We are already past an hour. So I feel like we should go into link mode here.

**Dave Jones:** Oh, there you go. Oh, there you go.

**Chris Gammell:** Let's go. Here we go. Link mode. So Andrea Spies, past guest of the show as well. Really cool video actually about, you know, we're talking at the top about connecting your stuff over IOT. This is a thing called open MQTT gateway, where basically, you know, there's like weather stations or like 433 megahertz. Yep. This is basically like a, it's a converter that you can program directly on the ESP32 that actually kind of like snips, snips for packets from, you know, sensors you and your neighbors might have. And then it can just push them up to the net, push them up to the network. Like super cool. Like, yeah. So go in. And then, you know, like there's all this stuff about like home assistant. Have you ever done home assistant stuff?

**Dave Jones:** I do have a system.

**Chris Gammell:** You do?

**Dave Jones:** But it's not very good.

**Chris Gammell:** Yeah. It's the Z-Wave system. It's a Z-Wave. No, no. Home assistant is the, is a software package.

**Dave Jones:** Oh, right. No, no. Yeah. Yeah. Yeah.

**Chris Gammell:** So there's like this open source. I think I'm saying it right. I mean, I always get the, there's like an Apple one and then there's the open source one. And I always get those confused. I think it's right though. I think home assistant is. And basically it's like, you should check it out. It's actually pretty cool. Cause like you just kind of generate these things called YAML files. And basically you say like, oh, actually this thing is going to be hooked up to a sensor. Again, I don't think AI might be interesting.

**Dave Jones:** I don't want to automate my home with YAML files.

**Chris Gammell:** No, no, no, no. It's not that it's basically it's generating, it generates code for the ESP 32. So you say like, oh, I have a, you know, this type of sensor and it's going to be hooked up to these pins of the ESP 32. And then it just writes the code for you. Basically. That's all you have to do. It's just like basically hook those things together and you're not cool. And then home assistant like helps you to kind of create sensor networks in your home. That if you wanted to do that sort of thing. Got it. All right. Very cool. Very cool stuff. What else is on the list? Lots of great links again. Thanks to unmanaged 615. There is. Yeah.

**Dave Jones:** He just puts everything on there. Crazy.

**Chris Gammell:** Yeah. Champ. Champ.

**Dave Jones:** Which gets mirrored to our Amp Hour Twitter account, by the way. So if you want these, you know, it's handy to follow the Amp Hour Twitter account because we don't tweet anything apart from the show episodes. And there's an automated thingo that any, if you post something on the Reddit, then that link automatically goes over to the Twitter account. So you don't even have to use Reddit to follow the links. So it's just handy. These links just pop up. These, you know. Yeah. Yep. Yep.

**Chris Gammell:** KeyCAD 7 is released. That's a big one. So new year. I'm trying to say KeyCAD more instead of KiCAD. I'm trying to do it, Dave. And yeah, it's great. I mean, I did a video at the end of last year with the team where we kind of are going over stuff that's available. Big one that I think is actually really important for companies adopting it is there's actually a database. You can actually build a part database for yourself now instead of like doing it through individual files. And so you think about like revision controlling it, but then also like having multiple inputs into that database and being able to have a librarian that works. You know, you could really start to build out some serious infrastructure. And another one that a lot of people like, but I don't personally, you might like this sort of thing. There's like scalable bitmaps that you can pull into the layout now. So say you wanted to go and recreate an old PCB and without any of the schematic symbols, you basically just pull it into the bitmap layout and then you connect it all up basically by tracing over top of, of these, of, of the, what the board looks like.

**Dave Jones:** Oh, nice. Okay. Oh, so you can use it as a template, a tracing template.

**Chris Gammell:** Like that's right. Exactly.

**Dave Jones:** Nice. Yep. Yep.

**Chris Gammell:** That's like, and again, that's like some people, like depending on what kind of work you're doing, like some people are doing like vintage electronics and that is critical. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** But I don't, I don't use that.

**Dave Jones:** You could also take a photo of a board and then a photo of the traces on the board and then you could reverse and then you could convert that into a new file. Yeah. Yeah. Nice.

**Chris Gammell:** Yeah. So lots of great, I mean, really, really great stuff in the new version. They deliver another promise and they actually released a version on time. And I think by next January, there'll be an 8.0, which is pretty crazy.

**Dave Jones:** Awesome.

**Chris Gammell:** What else? Anything else you see on the list? I mean, there's other, like, like I said, a lot of stuff here.

**Dave Jones:** Oh, there's tons of stuff, but no, we'd have to, we'd have to talk about it.

**Chris Gammell:** There's a remastered version of the mother of all demos. I think we've talked about that on the show before.

**Dave Jones:** Oh, really? Okay. Yes. We have talked about the mother of all demos. Douglas Englehart.

**Chris Gammell:** Yeah. That's right. Legend. Legend. Absolute legend. That was, when I was talking about the Xerox Park book that I loved, that was in there. I think we probably talked about it at least. Yep. It's fantastic. Among other times. Yeah. So cool. Unbelievable. Yeah. I think that's it. People can go check out the subreddit.

**Dave Jones:** Or follow it on Twitter.

**Chris Gammell:** Or follow it on Twitter. That's right. That's right. All right. We done. That's all for me. Yeah.

**Dave Jones:** Have a good week, man. Maybe, you know, we'll AI take our jobs by next week.

**Chris Gammell:** Yeah. We can only hope.

**Dave Jones:** No. Right. Well, the voice, the AI voice thing's getting really good. It's got so much material it can learn from. It's all public. It can learn our voices. It can simulate voices.

**Chris Gammell:** Yeah. But can it bring the witty repartee that we bring to the show every single week, Dave? I just, I don't think a computer can do that yet.

**Dave Jones:** Maybe I can try it because Machia Belly's underbelly, who's a Twitter user. That's his Twitter name. Sure, sure. He's like an AI expert and he generates all these AI videos of well-known people like saying things, you know? Like, and it's absolutely amazing. Maybe we can get him to sort of simulate our voice and make us say something.

**Chris Gammell:** I would love it. Yeah.

**Dave Jones:** Maybe I can find it.

**Chris Gammell:** I want to think so I don't have to record the intro each week. I can just type it in.

**Dave Jones:** Ah, you can just type it in. Yeah, right. Especially when I travel. Yeah, yeah, of course. That'd be great.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. All right. I'll contact him on Twitter and see if he wants to generate, see if he can generate our voices to make us say anything. Yeah. Yeah. Yeah. Because all our stuff's out there. We can't stop it. Like it's, it's going to troll our, troll and troll. It's going to troll and troll our previous episodes and it's going to learn and.

**Chris Gammell:** Yep. Only 620, 21 of them. Plus.

**Dave Jones:** Yeah. All right. Catch you next time.

**Chris Gammell:** See you.
