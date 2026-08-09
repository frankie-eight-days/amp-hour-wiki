---
episode: 607
title: The Joulescope Upgrade with Matt Liberty
url: https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/
---

**Matt Liberty:** This is The Amp Hour Podcast. Released October 30th, 2022. Episode 607. The Jewelscope Upgrade with Matt Liberty.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Matt Liberty, the creator of Jewelscope and owner of JetPerch LLC. Matt, how are you? Doing well. Great to be back here on the Amp Hour.

**Dave Jones:** Yeah, you have a new product. This is the Amp Hour is the place for product launches. And that's a slogan I just came up with. Product launches for all of your electronic measurement needs. You have a new version of the Jewelscope.

**Chris Gammell:** I do, yeah. We have the next generation. We've taken everything that we've learned from our original product, which is the JS110, and incorporated that great feedback into our new product that's launching on November 3rd, 2022. November 3rd. Wow.

**Dave Jones:** That's awesome. Could you give us a little reminder about, so people who didn't hear the last show, we will link in the last show, which I don't remember the episode number. I should have had that up in front of me, but we'll link that in the last time you were here. What is the Jewelscope and what's it meant for?

**Chris Gammell:** Modern electronics has a huge dynamic range of current. A lot of times they'll go to sleep and consume microamps, sometimes even nanoamps, and then turn on and often do sensing and radios, whatever they need to do at milliamps or even amps. That high dynamic range is very challenging to measure accurately. Also, as you're designing a product, making sure that your overall energy consumption is as low as possible, so you get long battery life, is really challenging. The Jewelscope was designed to help with that. It measures current and voltage and then computes power, energy, charge. From there, you see either a multimeter view or a waveform view of your consumption over time, which allows you to measure and then optimize so you can produce an awesome product.

**Dave Jones:** Yeah, and it is a headless unit as well. I think that's also an important feature to mention. So that there's no screen, but your computer is your screen, and that makes it even easier to script with as well.

**Chris Gammell:** Oh, definitely. Yeah, it's one of the family of USB-connected devices. So I'm a huge fan of Salier Logix stuff as well. So it's in that same family of you connect it up to your computer, you have something running on your PC or Mac or Linux machine that talks to it, and we have a GUI that you get out of the box, or you can script it freely with Python, and we provide all the stuff to do that.

**Dave Jones:** Awesome. And how do you see, how are most people using this? Are they using it in production and tests and new product introduction? Where are people using it most often?

**Chris Gammell:** Actually, all over. So there's a lot of people that are using it during the design phase, either as firmware engineers or hardware engineers. We have some people that use it, actually quite a few people that use it as part of their automated test. So with hardware in the loop, you push up your changes, you run whatever tests you would normally run, and as part of that, you also measure your current or energy consumption. That just goes into your record and metrics over time. We have people that are using it on their factory. Actually, I use my own Joulescope on the factory to manufacture. Bootstrapping, yeah. We have people that use it for scientific as well, which I wasn't really expecting out of the gate when we launched the JS110, but the JS220 is even better for that. It's much more of a stable scientific instrument, and we've taken the time to make sure that it will work well, not just for people developing products that you're measuring the typical LDO or switch mode power supply into your device, but for really any general purpose voltage and current measurement.

**Dave Jones:** Oh, interesting. So they're using it maybe to monitor an experiment?

**Chris Gammell:** Yeah. So there's some people, there's very expensive equipment that measures nanoamps that's out there. For a lot of experiments where you need to measure nanoamps, Joulescope, it's not going to be the same solid metrology of something that goes down to picoamps, right? Yeah.

**Dave Jones:** I used to work on that kind of stuff. Exactly.

**Chris Gammell:** But as far as measuring nanoamps and tens of nanoamps, especially if you remove the slight offset that the JS220 and N110 have, you can actually get a very good signal with much higher bandwidth than a lot of that other equipment.

**Dave Jones:** Yeah. And it's also not going through GPIB or HPIB.

**Speaker ?:** Right.

**Chris Gammell:** It's a nice USB interface with Python, or now with the JS220, it has a C-level driver, so we can eventually hook it up to any language pretty easily.

**Dave Jones:** You know, scientists love Python, so that's it.

**Chris Gammell:** I'm with them. So I do a lot of C, a lot of Python, and my productivity in Python is way more than with C. It's not going to be as optimized or run as reliably necessarily, but if you want to just get something done, Python's awesome.

**Dave Jones:** Yeah. That's great. Well, that's awesome for our listeners. I think a lot of them will probably resonate with a lot of that stuff, tests and experiments and things like that. Do you think, is it an everyday driver, like on the bench sort of thing? Or like what stage, what is the earliest you see people using this in product development?

**Chris Gammell:** So the classic answer of it depends. Of course. So, I mean, if you're building up a lab, is the Julescope going to be the first thing you buy? Great question. Great question. No. I would not recommend it. Before you buy a Julescope, you should have a multimeter. I mean, even if it's a little $30 multimeter, you should have at least an inexpensive oscilloscope. You know, one of the Regal or, you know, Salier Logic is another one. Yeah. We talked about that on the show last week, actually, about like where is that level? Yeah. That makes sense. Yep. And then if you're doing something that involves power, the Julescope might be the next thing there. If you're talking about getting battery life, long battery life out of your product, getting, you know, optimizing your code to be nice and tight so it is not consuming excessive battery or even just selecting the right battery for your product. You know, the Julescope might be that third thing. You know, there's certainly a lot of other demands that you might want ahead of the Julescope because, you know, electricity and designing products is all about making sure you can actually see or measure what you care about. We can't see electrons or, well, I can't. So you really rely on your tools. I keep squinting. I'll get there someday. Yeah.

**Dave Jones:** Okay. That's great. And so you'd say even before a power supply as well. Depends. This could be your power supply.

**Chris Gammell:** Yeah. So, I mean, it depends upon what you're using. So if you're just using batteries to do a lot of your development and a rechargeable, for example, you may not even need that, especially if you're a software developer that is getting hardware from your team or off-the-shelf hardware. But, yeah, I mean, there are certainly other things that are up there. So bench supplies, signal generators, frequency counters, you know, all these type of things are just an analog discovery. You know, one of those, the digital and analog discovery is also a great way to get a lot of that stuff. Yeah.

**Dave Jones:** Yeah. Yeah. That's great. Okay. Yeah. So that sounds great. So it's maybe not your first or second instrument, but it's maybe it's your third or fourth. And it does sound like as well, like the target market as well. It's like if you're doing analog, you know, analog only, this could work for you, but it might not be exactly what you need. But it sounds like it's really that high, like you mentioned at the beginning, the high dynamic range. That's what I think about is like I'm working on a, you know, cellular IoT thing. It's sleeping most of the time. It wakes up. It's drawing amps or hopefully not. But, you know, hundreds of milliamps during transmit. It's like, all right, I want to know that and then go back to sleep. Right.

**Chris Gammell:** Yep. Yeah. If you're just working on the analog design side, typically those are pretty constant quiescent currents when they're on. But a lot of times those are part of sensors. Right. So your analog chain may be measuring a sensor that's transmitting data up to the cloud or over the network. So that whoever's doing the larger part of that may be very interested in something like measuring the dynamic, high dynamic range current. But if you're just the analog designer, maybe not as much.

**Dave Jones:** Hear that, folks? Matt said just the analog designer. Past Chris is so sad. Past Chris is so sad. Luckily, I'm not just the analog designer anymore. I'm also the bad firmware engineer. Well, I'm the bad analog engineer, but I keep trying. I'm also one of those these days, too. No, that's great. That's a really good rundown. So, well, let's talk a little bit about the hardware. So what has changed between the 110 and the 220? It's doubled in number. It's twice as good. Twice as good, yeah. Somebody's working hard at the Jewelscope, the JetPerch marketing department is really thinking through it.

**Chris Gammell:** That's what's a problem with having engineers in charge, right?

**Dave Jones:** Well, eventually, if you have enough revs, then you start running out of digits, right? Just because of the exponential growth.

**Chris Gammell:** Hey, I'll be happy to run out of digits. Yeah, so we've actually made not really one major change to it, but it's really a bunch of changes that together all add up to a totally different level of product. From the beginning, we go from a 14-bit ADC that has 12.1 effective number bits, ENOB, up to something that has 16 bits with 15.1 effective number bits. So that's over an eight-time improvement in just our ADC side. We've improved the analog measurement chain, so the filtering and our amplification. So it behaves awesome now. We had some artifacts that if you hit it really hard, the front-end op amp in the JS110 had this super weird pattern because it was a chopper op amp that wasn't totally well designed for the bandwidths that we were interested in. We've now been able to address that. Overall, we've improved the power supply side, so we have lower noise. We have more processing on board now, so we've upgraded the FPGA to a Lattice ECP5, which I know a lot of your listeners are probably happy to hear. It's an awesome FPGA, and we can do a lot of the processing there rather than shipping it all off to the host now, which helps with a lot of the features that some of our customers have requested. Yeah. Overall, we have a better host-side solution as well. We've gone all in on publish-subscribe. So that just makes software architecture so much cleaner. We still have an adapter layer for our old Python interface that everyone has been using, but if they want, they can move to the lower level. It's still Python or C, PubSub access for the device.

**Dave Jones:** Huh. And so what does the PubSub manifest as? It's like instead of having... Was it polling before, or what was going on?

**Chris Gammell:** Yeah, so before we had essentially data coming in on USB bulk in, and then we had parameters, but a lot of those parameters were being processed on the host side and then sending up these more complicated messages to the device, which made it less flexible for us to add new features. Because every time we had to do something, we had to change those messages, and that just got difficult to manage over time. Now we have actually the device itself processing PubSub in firmware. So we have topics and values that are starting on the host and getting sent down to the device, and then the device just handles each one of those. So adding a new control, a new thing just becomes super easy now.

**Dave Jones:** So now you have to push a change to the firmware to just be like, oh, now you're also listening for Trigger 52 or whatever it is, and then it just starts listening for it?

**Chris Gammell:** Yeah, and it's actually even easier than that, in that the device advertises which topics are available. So it has this metadata that it also provides to the host. So there's really no changes that are necessary on the host to add a new control. Oh, cool.

**Matt Liberty:** Okay.

**Dave Jones:** And then, so then you're, then the device, sorry, the host side publishes or the device publishes?

**Chris Gammell:** Well, they both can. And so if something changes on the device, it can publish that something changed, but normally with these type of controls, the host is changing how the device is behaving. So it publishes and it goes to the device. The device does whatever it needs. It may actually reply with things. It may cause it to start sending out data on that, like current data or voltage data, whatever, depending upon what parameter you just set. So there may be side effects to that publish, but sometimes it may just be, you know, changing the current range. So if you want to set it from auto to 10 amps or 18 micro amps, you can do that from the host using one of these messages.

**Dave Jones:** Cool. That's really cool. And so then are you running, so you have an ECP5 on here. You got a bunch of, I'm sure, custom logic in there. Did you also put a microcontroller inside that or what is, or is it just all in logic and just doing like streaming?

**Chris Gammell:** Yeah, we actually have two parts to this. There's a microcontroller that is a Cortex M7. It's a SAM, so formerly Atmel, now microchip S70 chip that is doing the USB communication, really just shuffling data around. That's its main role in life. And then on the FPGA, we actually have a RISC-V processor, a little teeny Pico RV32. Oh yeah. Claire Wolf's original design, right? Exactly. Yeah. So I actually looked into a few different cores. So Bruno Levy has a great series of learning FPGA cores. There's some higher end cores, but I found that none of them were doing that great as far as cycle, you know, memory accesses and cycle on the ECP5. And the Pico RV32 did well enough. I almost got to a point where I wanted to put more processing on that and started writing my own before I realized I really didn't want to do that.

**Dave Jones:** Well, at least you stopped. Most people realize that like two or three years down the road when they're in like support state, you know, and they're like, oh, wow. Yeah, that was a bad idea.

**Chris Gammell:** Yeah. So instead I wrote my own custom processors. So, you know, win or lose. So we do have actually a couple of custom processors on there where we have, they really are processors, but specialized ALUs. Oh, cool. And running our own assembly language. And we have Python assemblers. So they're super simple. These are nothing that you would write home about. But the thing about when you write your own little processor is you can design your own instructions and things like our calibration, which we're doing at 36 bit.

**Dave Jones:** Yeah.

**Chris Gammell:** And then accumulating statistics, which we do at 100 bit, which don't work really well at RISC-V instructions on a little ECP5. We can do pretty efficiently with these just little custom processors.

**Matt Liberty:** That's cool.

**Chris Gammell:** Yeah. It's not that hard to write them once you kind of get your mind around. You're just writing a state machine.

**Dave Jones:** Yeah.

**Chris Gammell:** If you're coming from the hardware world, all you're doing is writing a state machine. It's just the states are the instructions. And you just have to put the instructions in the right order and you just have it pipelined. And the pipeline comes, you know, free when you start thinking about this as a processor rather than as a state machine.

**Dave Jones:** Matt Liberty explains processors, which is, it's just a state machine. You just got to put it in the right order. There's a pull quote. That's all it is.

**Chris Gammell:** The entire, you know, 60 year or whatever years of computing.

**Dave Jones:** What up now? Noice?

**Matt Liberty:** Oh, that's great.

**Dave Jones:** That's cool. So what is the workflow like for doing ECP5 stuff? Is it all Verilog and then like the open tool chain stuff?

**Chris Gammell:** Yeah. So what we've been using is Verilog for the language, Cocoa TB, and Icarus Verilog for simulation. And I looked into using the open source tool chain and would love to use it. At least when I started on this, there was enough challenges with some of the things like the Mac, which is obviously really important for what I'm doing.

**Dave Jones:** Yeah. Multiply accumulates is kind of your jam, I'm guessing.

**Chris Gammell:** It's pretty important. So there were problems that I think a lot of those have been worked out, but I haven't really reinvestigated yet. So I'm still on the lattice official tool chain. Right.

**Dave Jones:** Because if it, well, and a lot of the, yeah, because that's the kind of thing where they had to reverse engineer a lot of that, right? And I think. They did. It's awesome.

**Chris Gammell:** I mean, it was cool work.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. It's pretty impressive.

**Dave Jones:** Yeah. But I can imagine that, yeah, for a, you know, you just need to make sure it's working as, as it is, as intended. So yeah, that's cool.

**Chris Gammell:** Yeah, no, and it works well. I would definitely like to have the open source tool chain behind it, but we're not there today.

**Dave Jones:** Yeah. Cool. And then on the, on the Atmel, the dual core M7, are you doing like an RTOS on there or what's actually handling all the USB stuff?

**Chris Gammell:** Yeah. About that. We, we do have an RTOS. It's actually a custom RTOS now.

**Matt Liberty:** Oh no.

**Chris Gammell:** Well, I started out with free RTOS because I've done tons of projects in free RTOS.

**Dave Jones:** Yeah.

**Chris Gammell:** And I looked at Zephyr as well. I know that you've been playing with Zephyr quite a bit.

**Dave Jones:** Yeah. Atmel support's not great though. I think it really depends on which, which hardware you're, it's all, it comes down to hardware support, right? I think, I think in the free RTOS space too.

**Chris Gammell:** Yeah. Oh, both of them came up and ran. The problem with both of them is that I'm trying to push data super fast over high speed USB and interrupt latency and, you know, so interrupt latency and interrupt task switching time. So the time to go from the interrupt or from whatever you're doing into the interrupt and then from the interrupt back to your task is super critical for this. Yeah. And I was running into problems just where a huge amount of my time in the microcontroller is being taken up by those task switches. So I ended up just writing this super small, very efficient little RTOS. It's not even an RTOS. It's a tasking library. Yeah. It's a scheduler. Exactly. It's nothing fancy. Yeah. But it is super fast and small. So that's why I ended up going that way. And it's, it's, it's tailored for this particular chip. It's cool. To get the most out of it. And that, that's just enables us to push data super fast over USB.

**Dave Jones:** Yeah. I think that's the kind of thing where like you're at the edge of performance type stuff and you're trying to get that extra efficiency. I think that's, that's usually when custom logic in an FPGA and, you know, custom RTOS, that's, that's the kind of next level stuff that you need. That's when you need to do it. I think the problem is some people start there because they just want the, the control from the beginning. It's like, well, if you're just doing that, you know, like if you're just doing simple tasks, then you probably could pull an off the shelf RTOS or, you know, similar. Well, like you did with like your choice with the, the Pico RV, right? You eventually you scale it back. You said, I could do custom when you scale it back to something that's out there and supported. So I think that's always the trade-offs.

**Chris Gammell:** Yeah, definitely. If you could find something off the shelf that works well enough. And like with the Pico RV, instead of putting more stuff onto that, I made these custom processors, which ends up being a better architectural decision anyway. Oh, interesting. If you can figure out ways of using the existing stuff and just not loading it, that's great. Like in the case of my interrupts, there was, it was really hard to back off on that interrupt requirement because we had to service real, real. It's the USB is not so bad because we're just DMing everything out, but it's the coming in from the FPGA. We're using this kind of dual spy configuration and it just requires a lot of interrupt handling.

**Dave Jones:** Yeah, that makes sense. You know, the thing that always comes up in my mind is the support, the support load on this sort of thing is higher, right? Because I'd imagine you have to make sure that it's manufacturable. If the part changes, we'll get into the manufacturing stuff and that sort of thing in a bit here. But like, like, is it, is it still just you? I mean, on the code, are you bringing other people in or what's, what's the support side?

**Chris Gammell:** So on the engineering side, it's mostly been me. I've gotten a little bit of help along the way, but it's still pretty much been a one person engineering development effort.

**Dave Jones:** Impressive. Very impressive. Very impressive.

**Chris Gammell:** Thanks. It keeps me on my toes for sure. Yeah. Yeah. So doing everything from, you know, the gateway to the microcontroller firmware code and then the host code and then dealing with all the business issues you have to deal with. Yeah. So the engineering side has been mostly me. I've gotten some review and feedback from other, other teams. Obviously, I rely on thousands of people, I think, in order to actually manufacture this, the chips, everything with chips and boards and all the other mechanical parts. My contract manufacturer, actually still working with my wife who does all of the accounting and shipping and a lot of the, all the business side of things that keep our business running every day. She's responsible for that. At one point, I'd hired some marketing help. Paris Kenny was, yeah, yeah. No, he was doing a great job. And then the component shortage really kicked in and I'm like, I don't know if I can build anything. So I scaled all my marketing back to zero.

**Dave Jones:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** So Harrison, Sean, he, Mel were the ones who were doing a hell of a link show and people probably heard us refer to that in the past. So.

**Chris Gammell:** Oh yeah. And if, if you want to reach out to him, I think he's now doing a inbound lead generation and an outbound lead generation. He's been a great guy.

**Dave Jones:** Yep. Definitely. Awesome. Well, that's, that's good. I, you know, the reason I had a, I had an agenda here. I was going to talk about the hit by bus test, you know, like, like that's always, I always think about that as a. A resilience in the business thing. And the only reason I really bring it up is because my software engineer literally got hit by a bus. Like his car got rear ended by a bus and thankfully he was okay. But I was just like, Oh my God, this is like, this is the same thing. And it was just like, wow. Like that, that totally can impact businesses, you know?

**Chris Gammell:** Yeah. So one thing that I have done, so obviously the new product stuff has all been, you know, without me, it would definitely stall. But with both the JS one 10 and with what we're doing now with the JS two 20, I'm fully turning everything over to my manufacturer, my CM. They don't need me to build anything. Well, other than purchasing parts these days, they used to do that. Now, you know, I'm doing all that, which is all fun, but they can actually continue to produce and service customers. That's great. The technical support side with the JS two 20, I'm, I'm doing a better job right now of trying to build up more of a knowledge base that we can hand off to other people and help grow the company. You know, one of the things that we really value is, is customer support. It's a huge amount of, uh, you know, well, high priority for us and a huge level of importance. But, you know, right now I'm doing almost all of that, that is on the technical side. So finding someone else to help out so we can get even better support and more round the clock support for our customers everywhere is a, is a priority.

**Dave Jones:** Is that something you want to amp our listeners to write in about if they're interested?

**Chris Gammell:** Uh, if they're interested? Yeah, certainly. So we're looking for, you know, at least one person that would be interested in, uh, helping to build up a community and answer questions as they come in. We don't have that many, so this is not a huge job. Sure. It'd be like part-time kind of gig. Oh yeah. It's a part-time, but it does require someone who would be interested in, in learning and, and figuring out how customers are asking questions that aren't always, you know, the, what you need to answer. This is a typical FAE thing, right? Figuring out what the customer is really asking, not what they are saying. Oh my God. Yeah. Right, right. Because everyone kind of comes at things from their own perspective. So it's a huge part of the first part. Just the question they asked might not be the question that will help them get to where they need to be. So, you know, working through that part of the communication cycle.

**Dave Jones:** I saw a thing, I saw a thing about that recently. You know, I read, I read in that space as well, as well. And it was like, it was an example. I forget what, I forget where I saw it. So I apologize if someone sent this to me or, but it was like, the person was like on a forum saying, I really need to be able to extract the last three characters of a file name. And they're like, okay, well, what are you, what are you really trying to do? And they're like, I just need to find the last three characters of the file name. Like, all right, well, here's how you do that. But before you do that, like, what are you really, really trying to do? They're like, well, do you need the extension? And they're like, yeah, actually, I do need the extension. They said, well, the extensions aren't always three characters. You do know that, right? That's a bad test. You know, it's like one of those good examples of like, that they think that that's what they need, but it's really about like zooming out and be like, no, what are you actually trying to accomplish here?

**Chris Gammell:** Yeah, that's huge. You know, it's really all of what we're doing as a company. You know, we're trying to solve real problems and the real problem that we're focusing on is helping people develop, you know, low power and energy efficient products. So people come to us with all types of questions of how do I optimize this little part of code? It's like, well, I can help with that, but what is the real thing that you want to get? So it's a very common thing because it's just human nature. We get very focused on the problem that's facing us and ask about that rather than the larger thing that is really the challenge that we're facing.

**Dave Jones:** Yeah, I would think that would be actually additionally challenging too, because they are trying to get lower power on their devices. But that doesn't really, to be a bit blunt about it, that doesn't help you make money, right? I mean, like you are selling devices and you want to support those devices. But like, if it's outside of like the actual device itself, the JS220, the JS110, like that's kind of on them. But I'm guessing they all ask for help in the broader context of saving power.

**Chris Gammell:** Yeah, I mean, we have, I mean, we're very lucky in that we have a great set of customers. For the most part, you know, we have people that realize that they want to do this, right? That this is a self-selecting group of people that are trying to design. That's what I'm coming off the street. Exactly. These are, for the most part, we don't get, you know, people that are just learning how to use a multimeter. Which is fine. We have had people like that, which is awesome. But for the most part, our customer base is pretty well informed. So we don't have to do a lot of that education that a lot of other companies may need to do. So, yeah, we do get questions that are not as, you know, as well formed. But for the most part, people are...

**Dave Jones:** Matt should run for office at some point. That was a very nice, that was a very nice turn of phrase. What Matt's trying to say is some people ask some dumb ass questions. I'll just say it for you, man. It's cool. It's all good. As someone who's probably going to ask some dumb ass questions in the remainder of the show.

**Chris Gammell:** No, it's awesome because we have a forum where people can ask questions publicly. We have our GitHub repos where people make bug reports.

**Dave Jones:** Yeah, that's good.

**Chris Gammell:** And then private, you know, communications as well. So we get all types of great feedback and customer, you know, opinions across the whole range of our customers. And it's really cool.

**Dave Jones:** That's great. That's great. Cool. Well, let's see. So, so far we've talked about... I've alluded to manufacturing. I do want to get into manufacturing. Is there anything else we need to do on the... Before we do that, so we'll... At the end of the show, we'll give some contact info if people are interested in the support side of things. I would imagine... And like helping out with that sort of thing. I would imagine someone who is younger would be able to learn a whole lot. I don't know what age group or, you know, experience level you're looking for. But I imagine a younger person with some background knowledge in this space could learn a whole lot about a whole lot of interesting things at Jewelscope.

**Chris Gammell:** Yeah, definitely. I mean, again, this is not a huge role, you know, a couple hours a day type thing. But yeah, it would be awesome to have someone who's just super eager to jump into different questions. I mean, it could be a role where you actually create examples as well if that's interesting. It doesn't have to be. But we have a whole repo of examples that... A lot of them we built for customers, you know, specific questions that we've gotten asked. So something like that would be part of it possibly. Again, this is super flexible because we're, you know, super small company and really can match things up to what people are interested in.

**Dave Jones:** Well, let's dive into the manufacturing part because you have had a heck of a time with part shortage. But I have to say, I think I saw someone mention just the fact that you're getting anything out right now and that you have ECP5s on this board are their own level of amazing here. So what were some of your challenges, Matt?

**Chris Gammell:** It doesn't feel amazing. It feels more like I have a blunted forehead from bashing against the wall. So for those that don't know, and, you know, as an Ampower listener, I think you already know that there's been a component shortage for the last 18, 20 some months.

**Matt Liberty:** Yeah.

**Chris Gammell:** That has pretty much dampened the entire industry. So I was producing JS110s. You know, we launched it from Kickstarter in 2019 in July. And my normal process was like three to four months before I wanted more JS110s. I'd tell my contact manufacturer, build me more JS110s. And they'd go out, order parts, you know, get them all in, put them on boards, put them in the enclosures, put them in my carry case. And I'd get completed boxes of 10 each that we would then sell to our customers. That's great.

**Dave Jones:** Lot size of 10. That's lower than I would guess.

**Chris Gammell:** Oh, no. That's a box size of 10. Oh, a box is 10. Yeah. Yeah. So our typical lot sizes have been about 500 each. Ah, that makes sense. Yeah.

**Dave Jones:** That sounds more like it.

**Chris Gammell:** Yeah. Get some volume back. Yeah, that's good. 10 would not be cost effective. So yeah, that was an awesome process. That's normal turnkey contract manufacturing. Well, about February of March of 2021, that all changed. So I went to, I was about to start building another lot of JS110s. And I happen to have two parts on that board that are still unobtainable. I ordered them in March or April of 2021, and they still haven't arrived. Holy moly. And the lead time is, oh. Yeah, so one of them is an NXP part, and one is an STM32F0 part that I could probably substitute. But yeah. So both of those have been extremely constrained designs as far as availability. So at that point, I was kind of wondering how much do I push forward with the JS10. We had manufacturing challenges with the JS110. They turn out fine, but it's just more of a pain to manufacture them than I think all of us would like. And the JS220 addresses a lot of that. So at that point, I kind of started making the mental flip to do another JS220, push towards that rather than build too many more rounds of JS110s. So we were able to get more parts in for some of those because I'd already ordered them. But our supply ran out in June of this year of JS110s. Wow. So I started ordering parts for the JS220 in June or July of last year. To put that in perspective, I had just finished the first prototype that wasn't even close to what we have today.

**Dave Jones:** Right. So it was like a true leap of faith. And you're like, hello, I'd like to put all of my cash into this hopefully working venture in the future.

**Chris Gammell:** Yeah. As someone who has a small business, you know, putting out that much money. I mean, so cash flow is hard. Yeah, it's crazy. And I was fortunate enough that with the JS110, you know, I priced it correctly so that we were able to do this. I mean, a lot of people getting into hardware manufacturing don't know the pricing of how you really need to price it. So if it costs you $300 to build or $400 to build and you price it at $500, you're going out of business. Oh, you're hosed. Right. So a lot of people that critique pricing of products, you know, don't realize just what you have to do in order to stay in business. Right. And this is a huge example.

**Dave Jones:** I think also scale too, right? I mean, like, you know, you're talking about buying $500 at a time, but like versus a, you know, a large scale test and measurement company like that is doing thousands or tens of thousands at a time. And just the scale is just completely different, you know?

**Chris Gammell:** It is. But the problems actually only scale up in a lot of ways. When you go to buy parts, I mostly, and well, in the before times, would buy from DigiKey and Mouser, you know, your normal small volume supply chains. When you start getting to the 10,000 unit volume, you really can't do that anymore. You're now scheduling your deliveries using, you know, avnets or direct from the manufacturer. So your challenges about forecasting become bigger too, right?

**Dave Jones:** Oh, totally on the challenge on that side. But I just mean that like at the scale, you get, you know, bigger negotiated discounts and you also have usually better terms on like financing and things like that. Because I think about a lot of these companies, like the CFOs are doing so much on their cash flow. Like I imagine like the Keysight CFO, you know, basically they're running, they're running a finance, a financing organization, right? Where they're like, you know, doing their own. They probably have commercial paper they issue and stuff like that, like short-term bonds and things, which is just like completely out of this world for a small manufacturer. Like how would, how would we do that? You know, like that's, that's the same.

**Chris Gammell:** Well, you can get lines of credit and things like that, that you actually can, you know. But that's different than interesting about bond. I think you would agree. It is, it is.

**Dave Jones:** But I mean, it's not that we're without tools either. So sure. Yes. Right. Yeah. Someone, someone who's like brand new and maybe just like a, you know, a brand new Kickstarter. That's, that's a whole different, yeah, that's a whole different ballgame, right?

**Chris Gammell:** You get nothing. Yeah. Other than the Kickstarter. Credit cards, credit cards.

**Dave Jones:** If you have good credit personally.

**Chris Gammell:** Yeah. And like with all this stuff, I know there, there is a talk recently that you did with, I'm liking the name, about consulting and getting into consulting. And, you know, really in order to do any of this, to get into consulting, to build a product, you do need money up front, right? Oh, yeah. So getting that financing, whether it's by just being super frugal and saving or getting some outside interested investor to help is critical to being able to launch a product. Kickstarter, you know, the crowd supply. Yeah, sure.

**Dave Jones:** Yeah.

**Chris Gammell:** Crowdfunding approach as well. All of those are ways of getting cash into your business. But yeah, you definitely need cash as a business. Otherwise, something like the component shortage comes along and you're instantly out of business. Yeah, totally. Yeah. Yeah.

**Dave Jones:** So the JS110 will never be made again. Is that correct?

**Chris Gammell:** That is the current plan because, well, even if I wanted to right now, I can't. Yeah, right. And so far, no one has come back and said, I need the JS110 over the JS220. So we tried really hard to keep the JS220 compatible at the software layer and compatible enough at the electrical layer. So we did some things a little bit different with the JS220. So the JS220 has a separate voltmeter, essentially, input and a separate ammeter input. The JS110 had this view of power in and power out. You know, so you kind of connected in your power supply to in plus and out plus or in plus and out minus, excuse me. And then you connected your device under test to out plus and out minus. I think I said that wrong. In plus, in minus, out plus, out minus. So it flew through the JS110, whereas now we just kind of have this independent channels of voltage and current measurement. You can do the same things, but...

**Dave Jones:** Yeah, you still need the current to flow through, right? But you don't need to. Yeah.

**Chris Gammell:** Exactly. And actually on the JS110, it was the in minus and the out minus were shorted together. So it just, even though it went through the front panel of the JS110, it didn't do anything. It was just an electrical wire. Got it. So by breaking them out, we have more flexibility, but that's something that people just look at the device and it's different, right? So any of those, it's different things we wanted to help minimize. So we actually have a front panel that is the JS110 equivalent for the JS220. So we've done as much as we can to try to make it so that anyone who really likes the JS110, and we have a lot of people in that group that want to move to the JS220, don't have a huge hurdle to overcome.

**Dave Jones:** That's good.

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. Huh. And then you sent me notes as well. What does cable for GPIO mean?

**Chris Gammell:** Oh, yeah. So the JS110, we had this little header that you could plug into and you get two inputs and two outputs. And people used it for some things, but it was a little bit hard to use for some people, I think, because you just had to figure out you stick wires in it and that's it. With this, we have what most other test equipment manufacturers have, a little cable assembly that you can just plug right in. And we actually found this place through Alibaba that makes them. And actually, all the little ends are labeled nicely. Oh, that's nice. It's kind of cool. Yeah. So they just did a little heat shrink on each wire end that labels each one. And surprisingly, it was not that expensive. So it was awesome to put in. And actually, one of the people on the Contextual Electronics Forum said, you should do that. So that's how that came about.

**Dave Jones:** All right. Well, we will expect our commission check anytime. No, that's really nice, actually, because one of the things I feel like with cables specifically, when you have to like, when they're labeled at the device itself, it's useful, right? You want to know that. But then you like, okay, then I go plug a single cable, like a single jumper into that. And I'm like, all right, purple is V+. I have to remember that. And then I get to the, you know, wherever I'm plugging into, I'm like, what was purple again? I'm getting older, Matt. I can't remember these kind of things.

**Chris Gammell:** Yeah, no, it was super easy, actually, to get this made. So I've never really done a custom assembly, cable assembly like this. Just reached out to a couple suppliers on Alibaba. And the one that I ended up finding is super helpful. I'd like to provide their name. I'll get it here in a moment, and we can put it in the show notes.

**Dave Jones:** Okay, that's great. Yeah. Yeah, I mean, I don't know about your experience, but like, when I've been on Alibaba in the past, it was like, just find someone that was like, kind of close, like photos kind of look like what I was had in mind, and then be like, you make that just a little different. And then I think the big thing for me was like, they wanted some particular format. And I was like, can you just send me a test or a drawing that you like? And I'll just mark it up. And that was like, that was the best. That was like, super fast for me in the past.

**Chris Gammell:** Oh, yeah. No, I've had great luck with Alibaba. You definitely do not want to go with the cheapest person. That's right. Typically, you want to find someone that you believe is actually going to do a good job.

**Dave Jones:** Yeah.

**Chris Gammell:** But for the JS220, we've gotten the carry case, the cable assembly, the USB cable, and the aluminum extrusion, actually, all done by Alibaba suppliers.

**Dave Jones:** Oh, interesting. The extrusion. Okay. What, and you, I mean, you have in the back of this thing, assembled in Maryland. So you're still using your local CM. And I remember last time you said they were kind of up the road, right?

**Chris Gammell:** Yeah. They're about 15 minutes from my house. So I can't complain. So I was just over there yesterday, you know, picking up more dual scopes that we're going to be shipping to distributors. Working through, you know, we have, you know, pretty good yield, but still a few issues, obviously, that we want to work through and talking about that. So, yeah, it's super easy to have a contract manufacturer right near you, especially for a product like this, because we have pretty complicated manufacturing. So obviously surface mount is surface mount, through hole is through hole. But when you build a dual scope. Wait, wait, wait. Wait a second. What is it? All right. So when we build a dual scope, though, a huge part is making sure that it is working correctly and calibrated. So that's expensive equipment that is not part of a normal CM.

**Dave Jones:** Yeah. Yep. Yeah. And so do you have like your own test stand there? I mean, you said you test dual scopes with dual scopes, which is awesome.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Do you, you like maintain your own test stand there as well?

**Chris Gammell:** Yeah. Yeah, we do. So we have really expensive test gear to make sure that we, we meet our, our spec and calibrate each unit. So we have two test, two custom stations, essentially. One is our programming calibration test station. And then we have another one that is our final test station that does just a double check because we don't want anything leaving that doesn't work. Just, you know, in manufacturing things happen. So we, we have a second check of performance. And then that's also the laser. It laser engraves the bottom, each one custom. Like, like you see, so we get the top part engraved from our aluminum extrusion provider. The bottom part is custom engraved in, in Maryland here. And that's a new addition to our manufacturing line, which is kind of a cool purchase.

**Dave Jones:** That is cool. Oh, I didn't realize this was laser. Oh, so it's like black paint over white. Is that kind of how it does the laser engraving?

**Chris Gammell:** No, it's actually kind of cool. So this is black anodized aluminum. And when you laser engrave a black anodized aluminum, you get this like silver white color. And that's what you're seeing.

**Dave Jones:** Yeah, really cool. Yeah, no, it's great. Cause it has the solid, I'm looking at the unit Matt sent me, which is awesome. And I took a part. So that was nice too. I have my serial number on here and it's got a barcode. So it's trackable and all that stuff. So that is really cool.

**Chris Gammell:** Oh yeah.

**Dave Jones:** CD markings, FCC. That's great.

**Chris Gammell:** Yeah. So it's, each one's individually labeled. So if we get a return or someone has an issue, we can kind of trace it back to make sure that everything was right on our side. For the most part, we haven't had any issues with the JS110 as far as parts or bad things being put into it, which, you know, fingers crossed we don't for the JS220. But if we do, we have that traceability, which is good manufacturing. That's great. That's great.

**Dave Jones:** And was it on your site that I saw like a PLM system, a web PLM system that you're using? We use PartsBox. Oh, PartsBox. Okay. No, I was looking at someone else then. Sorry. I had seen someone, someone had sent me a link recently and they had thanked their PLM provider, which is interesting. I think maybe they gave them a discount or something. But how's PartsBox for doing all this stuff? We've had Jan on the show before and we love PartsBox.

**Chris Gammell:** Yeah, no, I really like PartsBox. We have some particular needs given the component shortage. I think Jan's done a great job of actually improving PartsBox to help accommodate some of those needs.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** But the way I met those needs is just entering all my data in PartsBox and then dumping it down into Python and doing my own Python stuff.

**Dave Jones:** Oh, okay.

**Chris Gammell:** So the question of, you know, 2021, 2022, 2023, 20, hopefully not 2024, is when can I build something, right? Yeah. I have all these orders that may come in on dates that may be promised or whatever. So when can I actually, with all these things that are going on and parts flying in, when can I build my next lot? Right. Really, my question now is not when can I build the next lot, but when I could build the third lot from now, which is-

**Dave Jones:** Oh, wow. Like that kind of level of forecasting. Because, yeah, because you also- I think that's the thing. It's like a big chain and you also need to provide. So like if you're shipping stuff to Arrow to have them in stock. No, never mind. Arrow doesn't stock anything anymore. If you're shipping to DigiKey, freaking distributors. Talk about Arrow and Avnet are banks. They're no longer distributors. They don't hold any stock. I will stand my ground on that one. If you're shipping to DigiKey or Mauser, you have to tell them when they can expect your parts too, right? So that's potentially problematic.

**Chris Gammell:** Yeah. And ideally for us, we're always in stock, right? So if I had the ideal world, we'd never have to tell anyone that when we were having more stock, it would just be there.

**Dave Jones:** Yeah.

**Chris Gammell:** And for us to do that, we now have to forecast and be buying parts today really for 18 months out. That's crazy. And I thought I was all smart a year ago buying for a year of production. The world has a way of smacking you back down. So we're now scrambling to think about not this build, not the next build, and really not the one after that, but the one after that.

**Speaker ?:** Wow.

**Dave Jones:** Because- I got to say, that's a lot of cash tied up. If you ever shut down the business, as they sell out that stock, that'll be like a little annuity for you. You'll just be like, oh yeah, I'm still selling Jewelscopes. I'm not making them anymore, but I've been selling them for another two years.

**Chris Gammell:** If we still have the supply chain shortages, I'll be able to sell them all for profit. There you go. Bingo. Yeah. At that one point, it was pretty disheartening. I kind of did the numbers just really quickly, and I think it would have been better for me just to sell the parts that I had bought and not actually launch the JS220.

**Dave Jones:** Oh no, that's terrible. Oh man. Then you're just a part broker, Matt. And nobody wants to be that.

**Chris Gammell:** Right now, it's not a bad business to be in as long as you get out at the right time.

**Dave Jones:** Well, and as long as you don't mind selling your soul. That's the other thing. That too. What is the price of one soul? Who knows? I feel like I haven't done enough justice talking about the actual hardware here. Is the isolated power supply the same as before?

**Chris Gammell:** It's a little bit different. Yeah. So it's the same idea. With the JS110, we use this little transformer. It's a worth transformer. And yes. Yes. I know.

**Dave Jones:** As Americans, we'll never be able to say it properly. We'll be corrected every time by the Germans. Exactly.

**Chris Gammell:** But it's these super little transformers that do a great job. The original one had just plus and minus five volt out. This one actually has both plus and minus five and plus and minus 16. So in the JS110, we were using another word that I'm not going to say correctly. Cook converter?

**Dave Jones:** Oh, the C-U-K. C-U with the- The C's got- The U have it at the C has it. The little hangy dangly on the C. Yeah. Or is it on the U.

**Chris Gammell:** Yes. I thought it was chook. I thought it was chook. Chook. Yeah. I mean, I know I'm not saying it right. So we use that in order to generate the minus 16 volts in order to do the voltage measurement. Oh, cool.

**Dave Jones:** And that's not too noisy, huh?

**Chris Gammell:** No, and the JS110 is super quiet. That actually was really quiet because you have- The nice thing about that topology is you have coupled inductors, and they end up making the power output super smooth compared to a lot of other switch mode topologies.

**Dave Jones:** Uh-huh.

**Chris Gammell:** That's great. Yeah. With this one now, we just have 16 volts plus and minus 16 coming out of the transformer. Just use your normal rectifier diodes to make that 16 volts plus and minus 16 volts, right? Like DC rather than AC coming out of the transformer.

**Dave Jones:** And how do I make sure I don't have 15 volts coming out of this thing when I turn it on? You mean out any of the inputs or outputs? How do I make my plugged-in board not go boom, Matt?

**Chris Gammell:** Oh, you're good. No worries. Okay, cool. So what we end up having is it's an isolated supply, so that gets rid of the boom potential between whatever you plug in on one side in your USB and computer. So your computer's not going to go boom. Oh, yeah.

**Dave Jones:** I wasn't worried about it going boom to ground. I was more worried about it going boom through the rails of my microcontroller that I'm testing.

**Chris Gammell:** And the way that the voltage side works is those go right into op-amp inputs. So you're not getting exposed to any... Great, great. Yep, no plus or minus 16 volts. And then the current sensor part is just going through MOSFETs and our sensor resistors. So it's a shunt ammeter, which is just a fancy way of saying we're measuring voltage across resistors.

**Dave Jones:** Yep.

**Chris Gammell:** And using that known resistance and the voltage, you use almost all to compute current. That's really all that's going on at the front end of Joulescope here. And I say all because there's a lot of nuances to that. Yeah. But...

**Dave Jones:** That's cool, though. So then the plus or minus 15 basically just gives you more dynamic range on the op-amps input, right? Exactly. Yep. Yep. Yeah.

**Chris Gammell:** Cool. Yeah. So we want this to be used for 12-volt systems. So ideally, 12-volt plus or minus 20%. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** And that gives us the 15... The JS220 is really 14.5 guaranteed. Mm-hmm. Some of them go up to 15, some 14.8, but we guarantee 14.5 plus or minus now. So this is a... One difference is this is a fully bipolar in both voltage and current making a four-quadrant measurement device.

**Dave Jones:** Really? Oh, wow.

**Dave Jones:** Yep. That's no small feat there. I'm holding a little source meter here.

**Chris Gammell:** It's... As far as the measurement side, that's exactly kind of what this is. It doesn't produce anything or consume current.

**Dave Jones:** Right, right. It's not doing... It's not sourcing negative current or whatever it is like the... Yeah.

**Chris Gammell:** Yep. Exactly. It doesn't do any of the power supply or current sourcing or sinking. Mm-hmm. But as far as measurement, it is doing that same exact thing.

**Dave Jones:** That's cool. That's great. That's great. Then what is the... You said the ADC went up to 16 bits. I mean, did you just switch out parts or what was the ability to go up market there?

**Chris Gammell:** So one of the things that we want to do is to continue to push this up as far as accuracy. So I think there's a lot of people that are very happy with the JS110 accuracy. They really were doing a great job as far as being comparable to very expensive equipment. I wanted to ideally make it so that we're not just doing very well. We're doing the same as equipment that's more than 10x the cost. So part of that was putting in these ADCs. We also have now four channels of ADCs, and that allows us to have a new technology that we've called N-Waveify that is allowing us to switch, actually measure through current range switches.

**Dave Jones:** Could I get that word one more time? N-Waveify. Oh, man. Engineers making product names. N-Waveify. N-Waveify. TM. Next time you need to name something. Give me a shot first. That's great. Sorry, I missed the actual important part here. I'm a terrible podcast host. I'm sorry. I was laughing too much about the name. All right. So four ADCs, and that allows you to measure?

**Chris Gammell:** Through current range switches. So one of the problems that a lot of equipment has, and this is not just the Julescope stuff, but you look at a multimeter. A multimeter, when it switches ranges, it's blank for milliseconds or even more, depending upon the multimeter. They just aren't measuring that, even though you may think it is. And most test equipment has that problem. During a range switch, it's just taking a while to reset the analog path, do everything, and get to it. With Julescope, we're trying to measure seamlessly for minutes, hours, days, months, right? Without any loss of data. So it's not like an oscilloscope where you have a trigger, you measure for a time, and then you go blank, and then measure again. The JS110 and 220 are always on streaming from the start till however long you want. There's no missed data. So as part of that, we have to switch current ranges. So if you go from microamps to an amp, there's really no conceivable way you can measure that dynamic range with low burden voltage and actually measure accurately. You just run out of headroom. So the Julescope has 20 millivolts of burden voltage. So even if you say, let's measure a million things, great, that takes you down to 20 nanoamps, you know, from 20, you know, or 20 nanovolts. Depending upon how you set your range, that's still not enough to meet what Julescope has as 30, was it 33 or 34 equivalent bits of resolution. So yeah, with the way we've had this now, as you switch current ranges, we're measuring on a separate channel at the highest range always. And with 16 bits, that gives us enough accuracy to actually measure through and have good data. And we've also done things to mitigate some of the other challenges like charge injection from MOSFETs.

**Dave Jones:** Yeah. Oh, interesting. Yeah, no, that's, that is definitely a problem. I think, I think some of it is like the, the old multimeter paradigm. Like you look at like traditional, traditionally how it was done. It was like expecting that you're just sitting in one place and you're just measuring, you're not the dynamic piece is, it was, was something that was introduced more in the microcontroller days. I feel like, you know, like that, it's always been a problem, but it was like, it's such a common problem now that this kind of in waveify is, is necessary. And that's really, that's a, that's a great, great work around there. I mean, that's, so then the, the highest range is always measuring, but you just kind of like, do you, do you annotate that like during the switching time, there's not as much accuracy? How do you actually alert to the user that it's, that a certain data point might be less, less accurate or, or is it just kind of like, well, you would have had nothing there in the past. So better than nothing.

**Chris Gammell:** Right. Yeah. So we're, we've struggled to be honest. I've struggled with how to dynamically state performance metrics for this because it's so much depends upon signals and loads. And for, you know, for the most part, you can take the static specs, which we do provide and convert them into reasonable dynamic specs. And the problem that we've always had, and every test equipment has, if you switch ranges, what do you say about that? Most test equipment doesn't say anything. They'll say, oh, we're out of commission. Good luck. Even equipment that's way more expensive.

**Dave Jones:** Yeah. Yeah. That's a damn shame right there. Yeah.

**Chris Gammell:** Yeah. That measurement stunk. Yeah. Now with, with the JS220, we actually have bounded air. And the thing, it's hard to say how that's bounded. So we have a few nice things. I mean, it's, it's going to be less than a milliamp of air during those times of current air. The voltage range, you typically would keep the same. We do have two voltage ranges, but you normally aren't switching for most of our applications between those. It's the current ranges that you really care about. So with the, the current system, you're switching and within five microseconds, you're full on back to the original channel with some of the, the, the higher ones, the 18 microamps, depending upon your load and system, it can be a little bit longer, but it's typically within five microseconds. So we're not taking a huge amount of time. And that's, that's part of the difference that sets dual scope apart. We're super fast. Right. So current range switches, a lot of people talk about milliseconds. You know, we're, we're, we're done in microseconds for, for switching. Actually, we make the decision in under a microsecond, which is, you know, we have dedicated hardware to do that comparators and a separate analog channel. It's actually making that happen. It goes right into the FPGA. The FPGA sends, Oh, we're doing something and switches things up. We have a super fast, but controlled drive to the MOSFETs to, to mitigate charge injection problems. And then we're switched in over and running through the analog path because it does take time to propagate through in a, you know, five microseconds or so.

**Dave Jones:** Yeah. I think about, you know, like an old multimeter that has like relays basically. And you like hear it clicking through the ranges and it's like, Oh, there's some time when those, you know, like there's, those ranges are switching out. You know, there's also like FETs in the, in the path as well, but like when you hear clicks, it's not that fast.

**Chris Gammell:** Right. Yeah. And you know, there's something to be said about good old fashioned relays. They have zero leakage for all practical purposes. And, uh, they have very few parasitics. They have some extra capacitance, but as far as weirdness, other than, you know, the switching itself, they're pretty nice. MOSFETs have all these.

**Dave Jones:** The dynamic piece stinks, right? Exactly. It's like the switch off. Yeah.

**Chris Gammell:** Yeah. Yeah. So MOSFETs, even when they're in there, they have some issues. Then everyone, you know, that's, that's played with MOSFETs for any amount of time says, this is super weird. You know, you have essentially these capacitances between everything that just cause some undesirable switching behavior and even just static behavior when you have them in a system. So you just have to, when you're doing precision analog like this, you have to think about that.

**Dave Jones:** Yeah. Sorry. I was just on mute, uh, writing down your, uh, this is super weird quote. I'm going to probably quote you on that one too. This is a, no, this is a really good, uh, I wanted to bring up like some of the chip makers have some kits that are like about, you know, measuring battery, like power profiler from Nordic is one that I see a lot recently. Cause I use a lot of Nordic parts and like, and this is just a really good point of comparison here. You know, the, the price is a huge comparison difference. And I was just, I was mentioning to Matt before the show, like on the scale of like power profile, well, maybe on the scale of resistor in line with my power supply. All the way up to, you know, five figure device from Keysight or similar, you know, like there, there is a spectrum of features and kind of like where the, where the dual scope falls on that spectrum.

**Chris Gammell:** Yeah. So, you know, other solutions that you have people use. So starting with a multimeter, you know, just putting a multimeter in line and measuring current is great as long as you don't need dynamic range. And if you try to measure the low, then it browns out your target device, you know, so that's a, if, but if it's a great way to get started, right. If it's better than doing nothing.

**Dave Jones:** Right. Yeah. And I think as long as you like understand where you are on the cycle as well, that's another thing that's important. Right. So being able to. Right.

**Chris Gammell:** Exactly.

**Dave Jones:** To say like, I'm in sleep now, or I'm in transmit now in the case of like a, you know, a Bluetooth or a cellular thing.

**Chris Gammell:** Yep. Definitely. Yeah. And then the next step up that people do is put a resistor in line with a oscilloscope. The problem is how, what are you measuring across? If you touch your ground, is that earth ground to your, your scope ground to your positive side, you know, resistor that can cause problems. So there are a whole bunch of problems with doing an oscilloscope. If you don't have a true differential probe, you start talking about a true differential current probe. You're now talking more than joulescope. So then like things like the Nordic power profiler, they're great. As far as integrating into the Nordic IDE and giving you a relative sense, their specs are, you know, different. Not, not, not as tight as joulescope and what joulescope aims to be. So if you're looking for metrology level, the joulescope is really the, the most inexpensive one that I know of. There's a few other ones that are out there too, but we, we are able to offer isosystems 1725 NIST traceable calibration because we are that level of, of equipment. When we aim to compare with the equipment that you're talking about, that's five figures, starting at five figures and going up from there potentially to, um, you know, not quite to the, the CX 3300 family, which is awesome, but with a hundred megahertz bandwidth on current measurement, which is a totally different level of, of gear than what we're talking about with the JS 220. But, um, the price is also totally different.

**Dave Jones:** Why would you need a hundred megahertz bandwidth on current measurement like that? Like, what is the, what is the true, is that just for like true qualification of like new

**Chris Gammell:** silicon or something? It, you would have to be going directly into the silicon because when you have a board, which most of my customers are using to measure not just a chip, but a board, you have the bypass capacitance. Yeah. And just by, by nature, that bypass capacitance forms an RC filter with whatever else you're applying power in. So whether it's the cable, whether it's the Joule scope itself, that is limiting your measurement bandwidth or your system bandwidth. So you end up having an RC circuit with 10, let's say you have 10 microfarads on your board, Joule scope. And if you're measuring like 1 milliamp is going to be in the 1.8 milliamp range, which I think is the 1.1 ohm resistor. So you have an RC filter. That's the Joule scope plus all of your cabling is forming. So that limits really what you need to measure, which is how we, we pick this bandwidth of 300 kilohertz, because that's usually about where things max out for most real world designs and you don't want to pay for more than you really need. But in the case of measuring directly into a chip, yeah, the CX 3300 can do that. Got it.

**Dave Jones:** Yeah. And I feel like that all of that stuff, like on that, on that, uh, that spectrum from, you know, DMM up to CX 3300, it's like there are different price points as well. And it's, I think it's just about optimizing for the best one there. And it seems like, like you said, you're trying to target, you know, kind of the, the use case that most engineers are going to have on their bench, but then also getting into production and, uh, being able to do production level stuff on boards versus Silicon.

**Chris Gammell:** Yeah. And make it super easy to use. So, you know, all you do is plug it in. Oh, I mean, that's, that's what this is all about. Right. So we have customers that don't want to think about anything. They just want to have an ideal instrument, which doesn't exist. There's no such thing. Right. But they probably asked for it anyways on the forum. Exactly. So the JS one 10 was, was designed for that purpose. The JS 20 to 20, we've improved, but the whole idea is you just drop it in, you pull up a really simple user interface and all of a sudden you are able to see what you can see normally.

**Dave Jones:** Yeah, totally. That's great. What about the, so software hasn't changed pretty, pretty similar between one 10 and

**Chris Gammell:** two 20 right now. It's, it's totally the same. We have a major improvement plan for the UI. Actually, I kind of misspoke there. The, the, the lower level is totally different. So we went to a total C driver. You know, like I said, we're all in on publish subscribe. We did that in C so we could actually bind to multiple languages, but we include a Python binding. So you can access that same API, the publish subscribe through Python. We also have another layer of that, which wraps our previous API, the, the one that we use with the JS one 10. So as far as you know, you're running just like a JS one 10, except you're talking to a JS two 20. So you have the option of using the old API or the new one. And our UI right now is using that adapter layer. Still. We have a plan improvement to go to directly to that other, the new, new layer, which will also enable us to do a lot of cool things like simultaneous device support, which is a huge requested feature. Like you want to measure the efficiency of something like your switch mode power supply or an LDO right now. It's, it's not easy to do that with the UI. It's it, you can do it with the Python code, but not as easy with the UI. So we want to bring that ability to the UI. Also the ability to compare files that you've recorded with what you're measuring now. So there's a whole bunch of features that we're going to be launching over the next, you know, six months or so, not right out of the gate that will support the JS two 20. And a lot of those will still work with the JS one 10 as well.

**Dave Jones:** It's fun that the software is never done, huh? Yeah. And I mean, that's, you just have new projects every time. And you also have software in your FPGA and your microcontrollers and software eats the world, right? I mean, Matt, I am, I am super impressed with this. This is just like so many different layers here. And like, I know that you have supporting people, most notably your wife, your CM team and like, but like just the fact that you are doing all this stuff is, is very, very impressive.

**Chris Gammell:** Well, thanks. Yeah. It's a, it's what is a full stack engineer, right?

**Dave Jones:** Yeah, that's right. All the way down, all the way down to the silicon. Now you're making your own. So what about, what about that? You're going to, you're going to go to Matt Venn and be like, Hey, I need some custom silicon now too. That'd be pretty sweet. That's the next step, man.

**Chris Gammell:** I have, I have, believe me, it, if I wasn't so busy, I would have put something in for his shuttle, but, uh, oh man. Yeah. It'd be so cool to have. I know there's some things that we could do on the silicon layer that right now we have to, you know, piece together from components and there's some downsides to that, but I don't know if I'm up for making a chopper amp in silicon that is high precision analog.

**Dave Jones:** Oh, I wouldn't do, I wouldn't do analog there. I would say maybe one of your little custom, custom processors, you know, if you wanted to break that out for some reason, that would be the, you know, stay digital, stay digital for, for that stuff. Speaking of digital, I wanted to mention the front plate as well. So you have a new test front plate on this thing. So like basically when people buy this thing, unbox it, they can plug in this test front plate. What is, what does the evaluation kit do?

**Chris Gammell:** So the evaluation kit is just a little board that is designed to regulate USB power. So it plugs into USB itself and then wiggle signals. So without any effort, you can just buy this, plug it in and get real world signals of a known pattern into your JS220. So that's, that's the beginning of it. And you don't have to do any programming. You just plug it in and you see some things and that gives you some real world experience.

**Dave Jones:** It's an entropy machine. Is that, is that a fair assessment of it? It generates chaos. That's right. Right. That this thing does. And so does the, so does, so does the semiconductor ecosystem. Oh man.

**Chris Gammell:** Yeah.

**Dave Jones:** Purchasing, purchasing manager.

**Chris Gammell:** Actually, it should connect up over the internet and just track your, your lead times. And that could be the entropy that we drive this way. Yeah.

**Dave Jones:** It just has a little display. It says you're screwed.

**Chris Gammell:** Yeah. But this, this board, the EVK one is actually a MicroPython board. So it has a Raspberry Pi RP2040 running MicroPython. So you can actually connect into it and we have software, you know, little Python, MicroPython scripts that are already on there that you can just configure differently and have it do different wiggles, you know, so it can set different voltages. So we have an LDO and a buck mode power supply. We also have a bunch of resistors that you can toggle. We have a capacitor that you can actually toggle as well with PWM. And that gives you a bipolar, you know, so it can go plus and minus. So you can see that signal through the JS one 10 or JS two 20. And it's just fully programmable with MicroPython. So you can customize it to make it look more like your system and get a off the shelf piece of hardware that you can make measurements on known measurements that you can get confidence and then take it over to your real world equipment and see that it's working similarly.

**Dave Jones:** That's awesome. Yeah. I just, I just plugged mine in and got connected to serial and it's just ready to go.

**Chris Gammell:** Yeah. Yeah. And, you know, so you can use anything you want if you're looking to develop it. Thonny, T-H-O-N-N-Y is a great little getting started. GUI ID. It's not, I wouldn't really call it even an ID, but it's an environment for dealing with MicroPython devices. And you can use that to customize these scripts, even just set things up and play until you are

**Dave Jones:** happy. Python IDE for beginners. That's great.

**Chris Gammell:** So that sounds like me. Yeah, no, it's, it's super easy. I've, I mean, that's what I use for doing MicroPython stuff for anything that's not complicated. So part of the manufacturing setup, I've gone all in on, on Raspberry Pi Picos. So we have. Oh, interesting. Yeah. So if you're trying to control IO, digital IO, it's the simplest environment. So you can just have a REPL, you know, your, your redeval print loop that's coming out of the MicroPython device. You can actually connect to it with Python on your host computer. And without any work, you have a way of toggling GPIOs with a MicroPython, you know, Raspberry Pi Pico.

**Dave Jones:** Yeah.

**Chris Gammell:** So it's, it's super simple for this things like manufacturing stations where you just want to toggle some lines or read some things in makes it super easy.

**Dave Jones:** MicroPython is the new relay logic. Is that, is that what I'm hearing here? I think so.

**Chris Gammell:** Literal logic other.

**Dave Jones:** Yeah.

**Chris Gammell:** So it's, so I used to use Arduino a lot for things like this, but with MicroPython, you get the REPL for free. It's more powerful. And, you know, with the Pico, it's four bucks.

**Dave Jones:** Yeah. The fact that you could just, you could just like immediately have it giving feedback without having to like compile and download and that sort of thing is, is very, very, very nice for, for fast iteration.

**Chris Gammell:** Oh yeah. And for things that you want to run fast, you write your little MicroPython script that runs on the computer, on the processor itself and compiles to somewhat native C code. So it's, it's not as fast as if you hand wrote it, but pretty close. So you can offload things that are fast onto that device. And that's exactly what's happening here. Although we're using the PIO logic. Oh, you are. Yeah. So we can pump out things super fast. So if you want to toggle these, these things are very controlled and you just have the sequence pattern that it just plays out through the PIO.

**Dave Jones:** Huh. How do you, how do you find that? I still haven't dug into that. I should have, we've talked about on the show before, but haven't, uh, haven't found a need for it yet. How do you find that? Like, I guess you're writing your own assembly that you've also created the other side of, so it's probably not, no big deal.

**Chris Gammell:** Yeah. I mean, I'm using just, again, the, it's the, the Raspberry Pi Pico MicroPython code. Mm-hmm. And they have a way of just essentially generating that within the, the Python, MicroPython code. So you don't have to even write like a separate assembly file. It's just part of what you get. So it makes it really nice and easy. You do have to know the PIO peripheral. So there, there are some things that you need to do, but a lot of them, you could just find examples online. They're close enough.

**Dave Jones:** Yeah, that makes sense. And then when you're toggling stuff, is it also, are you going through like an LC in order to get like PWM to go to an analog voltage or how are you, or just have a DAC on board or what are you using to actually get like analog variation?

**Chris Gammell:** Okay. So if we're talking about the regulators, I'm actually just setting resistors to get the different voltages, right? So I have little IO lines that are just connected to one side of the resistor or not, and they're either floating or connected to ground in order to set the LDO regulation voltage or the buck converter regulation voltage. Then on the other side, we have MOSFETs that we're just turning on and off directly from the Raspberry Pi Pico. So that's not analog. It's just digital on or off for those signals, but they're controlling resistors that give you different current values. And then the last part is the PWM on the cap. And that's just, you get what you get as far as voltage, but it's, you can control the frequency. Got it.

**Dave Jones:** Yeah. So you basically can kind of toggle it up and down, but you want to, you want to have some variation there anyways, right? Because you're, you're not using this for measurement. You're not looking for precision. You're just looking for variation and things that you can showcase, right?

**Chris Gammell:** For that case. Yeah. The cap is not as much of a controlled one as the rest of them are. The rest are much more controlled for the resistors, you know, the current loading. Yeah. But, um, the, yeah, the toggle is just to show, uh, something that's harder to get in a controlled environment. Um, but it's very similar to what you'd see with a switch mode power supply.

**Dave Jones:** Yeah. Yeah. And this is a great idea. I mean, like, and I mean, I mean, RP 2040 has actually been available as well. So like just from an availability perspective too, you know, it's crazy.

**Chris Gammell:** Oh yeah. No, I went out and actually bought 500 and, you know, could buy 500. That's, which was a nice statement.

**Dave Jones:** Um, and I have. You did it just, just to get that feeling of, oh my God, that's what I remember this. I remember success when I can think of something to build and actually order it. The cart actually went through. I clicked the button and it showed up my doorstep a couple of days later. Huh?

**Chris Gammell:** Oh my God. I mean, it's an unending source of misery and pain. And, uh, you know, just even last night I was ordering more parts and like, this is like a thing I do every day on, well, maybe not every day, but I kind of give it up.

**Matt Liberty:** Yeah.

**Chris Gammell:** So do you check all the parts that you need and just go click. And sometimes miraculously that one day you win the lottery and TI has them in stock. They have none, none yesterday, yesterday. They have 10,000 now and I'm going to order all of them. So, because they didn't, they didn't, uh, put a limit on that one.

**Dave Jones:** We're like the junkies at the slot machine. Just, just hoping, just hoping for that jackpot. You know what? Most days it's, it's a, it's a bunch of, a bunch of junk. It's, it's nothing there. There's no cherries, no cherries to be had unless you want to pay, you know, 10 or a

**Chris Gammell:** hundred times what a normal price is. Yeah. Right. Right. That's right. That's called a reverse jackpot. I've had, I've had to do that a few times. Oh, really? I'm not happy about it, but you know, the, the, the scalper gray market is, is getting their money now and they'll be in a world of hurt come hopefully next year.

**Dave Jones:** I hope, I hope they, I hope they have to eat it. I hope they, I hope they all crash and burn.

**Chris Gammell:** Oh, they're making enough money now that hopefully they, they're planning for it.

**Dave Jones:** I hope they spend it on stupid stuff and they're, they go broke. Yeah. Where, I guess we should start wrapping up here. Where can people, where can people buy one of these?

**Chris Gammell:** So you can go to Julescope.com. We're accepting pre-orders now and we'll ship by November 3rd. So coming up here in a week from, well, on Thursday, the website is Julescope, J-O-U-L-E-S-C-O-P-E.com. You can find us on Twitter for, well, as long as that lasts at Julescope. You can find me on Twitter. I'm at M Liberty and then the number one or on LinkedIn. I'm Matt, M-A-T-T, Liberty, L-I-B-E-R-T-Y. You can also, if you have any questions about Julescope or just low power design in general, you can hop on our forum. We have a great group of people there, which is the forum.julescope.com. If you go to our support page, you'll get all of this. You can send us a contact email. Really happy to chat. If you have any questions, I'll be checking back with the Amp Hour here so I can answer any questions down below.

**Dave Jones:** Oh yeah, we have a comment section as well. I think the Julescope forum is probably the best way to do it, but we should send people over there. But if they want to commiserate about part shortages, it's probably, that's, the Amp Hour support comment section is the best place to complain about things, as history has told us. And we love you all for it. Anything else we didn't cover about the Julescope, Matt? I mean, like you, I mean, so I should say Matt is super organized and he sent me like an outline of things that like have been going on and like a timeline. It's just amazing stuff here. So anything that I missed on here that we should mention?

**Chris Gammell:** No, I think we're going to, you know, there's a whole part that is super interesting to some people, the business side of running a company. We talked about a lot of that the first time.

**Dave Jones:** Yeah.

**Chris Gammell:** How do you figure out what product you make?

**Dave Jones:** Yeah. Were you on Hello Blink as well? I would imagine that would have been a good place for that kind of discussion as well.

**Chris Gammell:** I was. Yeah. So they, we talked more about finding people for help. So like my experience with Fiverr and Upwork, which have been very mixed. Yeah. So with, I actually have had some great experiences on Fiverr and some really bad experiences as well, mostly on Upwork actually. I've had trouble there. Yeah. But on Fiverr, I just had a great experience. So I wanted to get professional pictures of the JS220 because, you know, my little white box. Oh yeah. White box here doesn't do great with, well, I think it might be the operator more than the white box.

**Dave Jones:** Yeah. Right. It's not the one, it's the magician.

**Chris Gammell:** Exactly. Sent them out and got them back and it was an awesome experience. So there's a whole part there, but maybe another time and yeah, more business.

**Dave Jones:** I'm sure. Oh, do we, do we cover? Oh, we did. We covered the part shortage stuff. Okay. Yeah. We got that in here.

**Chris Gammell:** Well, yeah, there's always more part shortage. Oh yeah. Complaining and 2025.

**Dave Jones:** That's I'm calling it now. That's, that's when it's all, it's all going to be worked out. We're going to be like, oh my gosh, I got the cheapest parts from those part brokers. And I, I got to, I asked them for a vial of their tears as well. And they shipped them to me for $20. Well, best of luck, Matt. And I really recommend, you know, I'm a dual scope user. I highly recommend it and I hope people pick it up and try it out and make better products as a result.

**Chris Gammell:** I hope so too. And feel free to reach out to me if you have any questions and Chris, thank you again for having me on the amp hour. No problem. Let's talk to you soon.

**Speaker ?:** Bye.
