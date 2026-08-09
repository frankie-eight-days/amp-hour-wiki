---
episode: 544
title: Standardizing Manufacturing with Pete Staples
url: https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/
---

**Pete Staples:** This is The Amp Hour Podcast. Released June 1st, 2021. Episode 544, sponsored by Mauser Electronics. Standardizing manufacturing with Pete Staples. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Pete Staples:** And I'm Pete Staples of Blue Clover Devices.

**Pete Staples:** Hey Pete, how are you? I'm great. How are you? Great. I've heard you before on the Embedded FM podcast, and we wanted to talk a little bit more about manufacturing. Obviously, you do firmware stuff, but you do hardware stuff too, so good fit for both spots. What is Blue Clover?

**Pete Staples:** Blue Clover Devices is an ODM, so we produce electronics for various companies. Tesla, Puma, GM are some examples. We do it across industries. For a long time, the only connective thread we could think of was that they're all connected devices, so we refer to ourselves as the IoT ODM. More recently, we've started making some products under our own brand that are B2B products that are sold to other factories or to clients who want to streamline test automation. Yeah.

**Pete Staples:** And how do you define ODM?

**Pete Staples:** ODM is a flavor of CM, and CMs are by definition making products for other people. ODM refers to its original design manufacturer and generally means you have some design capabilities in-house, so a lot of our clients take us up on doing board layout or firmware development or prototype builds, and so because we have those capabilities on offer, that's why we're an ODM and not a pure EMS company. Yeah.

**Pete Staples:** Yeah, and I think that is important, especially because you're going to have more in-house knowledge of your own manufacturing process. That actually could be really beneficial to a client, but I wonder about how the type of person that comes to you from within a Tesla or a Puma or a Volkswagen or whoever's on your site as your customers, is it like non-EEs are coming to you and saying, hey, we want to just build this thing, or is it like EEs within the company are coming to you and then they're saying, but also it'd be great if you help with blank.

**Pete Staples:** It's normally EEs, but it's busy EEs that we don't have time to do it in-house, so nobody ever comes to us and says, here's our product, we've been making it for five years and we need to do a cost down, have at it. They always are coming to us with new products, and so they're not built yet, they're not designed yet, and they want to know that if the schedule crunch comes that we can help out, and so it's usually folks with a little bit of risk in their project.

**Pete Staples:** Yeah, well, and it sounds like too, I mean, if you're doing IoT stuff and you have this specialized knowledge around not just the hardware manufacturing, but also the testing, like we'll talk about, and the firmware and everything else to get a connected device out in the world, then, you know, I mean, there's a lot of specialized knowledge in there that it might take a lot longer to learn internally at a large company that they just aren't, aren't, not qualified for, but they're not authorized to do, right? Their boss might not be, well, take six months and learn every aspect of Bluetooth or, you know? Right.

**Pete Staples:** Right, and yeah, I think we can go faster because of our experience, and particularly on the connectivity aspect, you're reusing a lot.

**Pete Staples:** Yeah.

**Pete Staples:** You know, if you've made electronic products, but they haven't been connected, and then you're doing a connected one, it would take that firm longer than it would take us, so it should be cheaper to work with someone like us.

**Pete Staples:** Yeah, and what are the timelines you're usually on? I mean, is it like a three-month cycle or six months, 12 months, 18 months because of the current part shortage crisis? Right. What are you guys usually seeing?

**Pete Staples:** Well, as a new father, you can probably empathize with the nine-month cycle, so I think that's really the typical, but it can easily be more. Okay. Yeah, and being less than that normally means it's not a full product. It's more like a board, so if somebody just needs a board that does something specific, so one of our clients is, they're doing a dev board with us, Sci-5, so they make a chip. They need a board that exercises that chip, and so that one was not nine months. Mm-hmm, yeah.

**Pete Staples:** Yeah, and so then how would you, would you define a product being like basically a subassembly that might be going to this company, and they're able to, like a saleable product, and that's the nine-month mark of like fully tested, fully enclosed perhaps, but like it's just a subassembly in their larger process?

**Pete Staples:** Well, if it includes mechanicals, and there are just more suppliers involved and more ingredients, more different materials, that's what extends it. Mm-hmm. Tooling is something that can really be a big wild card, and then if it's a simple enclosure, that's one type of tooling. If it's, you know, a mechanized product with multiple materials that all have to fit together, or, you know, even if it's all plastic but just has a lot of parts, Yeah, yep. I would not know how to do a printer, for example. That would be like, wow, just so many, so many parts.

**Pete Staples:** Yep, yep, totally. Yeah, lots of levels, lots of subassemblies on subassemblies. Yeah. One thing that is interesting about your business, it is international as well, right? So you actually have facilities both stateside and in Asia. So what is your kind of offering look like in that way?

**Pete Staples:** Yeah, we started in LA, but very, very small there. So essentially, I opened up a US entity in LA and then was spending more and more of my time in South China, so specifically Shenzhen. And we built up a design, a hardware design capability there. And design led to manufacturing and initially working with manufacturers and eventually opening our own factory. And we continue to do our production all in Shenzhen. And we do most of the hardware design there. And then we have an office in San Francisco. That's where I am now. And here we do software development and some degree of hardware design. And the teams work together in one cross-functional team to bring the products to market and also develop our own products.

**Pete Staples:** Yeah, that's great. Yeah, I mean, so then what does it look like then? I mean, to just start a, I mean, I guess because you're already over there, you're interacting with people, you're meeting people, you're making connections, and then having your own manufacturing facility. What is that process like to kind of bootstrap that up?

**Pete Staples:** I wouldn't recommend it to everybody. We did it reluctantly. So it was, you know, getting into manufacturing is actually not so difficult. Getting out of it is what's difficult. So it's, you could just buy a machine and offer to make things and you'll be a manufacturer. We were forced to do it because we just couldn't get the efficiency we needed working with partners with our particular quality standards and I would say somewhat modest or dynamic volumes. So, you know, if you've got, if you're Apple, everyone wants to make your stuff, but if you're a hardware startup with like, needing a hundred thousand of something delivered for Christmas and then nothing for nine months, until next Christmas, you're, you're basically there for all the pain, you know, you're providing, providing a lot of pain, but not much of a payoff for a manufacturer because it's so bursty, you know? So, we, we just got one thin training up teams within other factories and then, you know, having to move on after the build and so, it just made sense for us for, and for our clients for us to have our own factory. So, we, we started out doing screwdriver work, just tables and screwdrivers and then we built up PCBA capability and then there was an opportunity that took us into precision cables. So, the two in-house specialties are PCBA and USB-C or lightning cables. So, higher-end cables.

**Pete Staples:** Yeah, yeah. Yeah, I mean, I, I think of, you know, like sending out to Shenzhen just because there's so many cable opportunities out there. There's so many people that are making cables, but I, I usually think about it for kind of the, the simpler stuff only because that's what I'm doing, not because it's not possible to do other stuff. And so, does that mean then that, that kind of business, the PCBA, the continual PCBA and precision cables carries you through the burstiness? So, if you're not developing just for one product just for the Christmas time, it's, it's the rest of the year?

**Pete Staples:** It, it helps. So, if you can only do the, the box build, it tends to be even burstier, whereas board jobs come up more, more, they're sprinkled more diversely throughout the calendar. And so, we also don't have nearly that type of nine-month cycle with a board. Like, if someone has a completed, has the board files and the build materials, we can turn it around in a few weeks and we don't have very high minimums for PCBA, whereas for a complete product, if you're asking us to work through EVT, DVD, VVD, and get a golden sample and all that stuff, we have to have pretty high minimums just to make sure that there's going to be some production to pay off all that energy.

**Pete Staples:** Yeah, yeah. I mean, so does that mean then that you have like high, like variable clothes for workers too? Like, you hire, you know, you hire people seasonally, that sort of thing? Like, does the workforce shift quite a bit?

**Pete Staples:** Yeah, it does. We have workforce attrition and also need to go out and need to bring in new people as things pick up. We have a core of workers who are pretty knowledgeable about our processes and so they kind of mentor the newer folks and typically when we bring in folks, they start out as temporary workers and then become more long-term workers over time.

**Pete Staples:** Yeah, that's cool. I mean, it's, I don't think I've met anyone that actually is like running their own shop over there. I mean, obviously, there's a lot of people I've met that and been on the show that have utilized CMs that are over there, but taking that step to actually set up a facility and maintain it, that's, it's interesting because that really persists the, I'm sure that it's just a whole different set of challenges that you've experienced.

**Pete Staples:** Yeah, I remember taking, classes in operations. So I did a, after engineering, I did an MBA and we had a class on ops and I just was like, yeah, that's somebody else's problem. I'm not going to have to worry about these things and, you know, flows, units per hour and things like that, that are kind of simple calculations. so it's easy to just kind of assume it's, it's super easy, but when it's your livelihood on the line, it really, when you see

**Pete Staples:** your yield, your yield going down and your margins going down, you're like, oh, wow, okay, this really matters. Where was

**Pete Staples:** that book? Yeah.

**Pete Staples:** Right, right, yeah.

**Pete Staples:** I remember having a really painful run, just like one, one production run that was just really going sideways and I was flying back to the States and I picked up the Toyota way at the airport and I've like, was so glued to that book because, and I, if I'd picked it up earlier, I wouldn't have even been able to read like 10 pages of it before falling asleep or something, but because I'd suffered these very issues, you know, just, just days earlier, it was a, it was an impactful book and the Toyota way and Taiichi Ono and what those folks figured out remain like pretty much how I believe manufacturing, like it really guides me today too.

**Pete Staples:** So with the Toyota, I mean the TPS system, Toyota way, all that stuff, like do you actually find yourself implementing that directly? I mean how, how much hands-on day-to-day operational stuff do you, do you have with, with the factory? Because it's just, it's pretty far away. I mean you're in San Francisco, so a lot closer than I am from here, but still not close and probably not traveling that much during COVID either.

**Pete Staples:** Yeah, I haven't installed one of those double robots that like wheels through along the line or anything like that. Oh yeah, yeah, yeah,

**Pete Staples:** the creepy,

**Pete Staples:** this floating head.

**Pete Staples:** no,

**Pete Staples:** frankly right now, I mean this is a pretty unusual situation to not be able to go there. So this was a test of our team and essentially our, our lieutenants have stepped up and they're running it so I'm in touch with them but I, I really don't see what exactly is on that line except through the, through our tools. Through a webcam. Yeah, and the tools we'll talk about here in a little bit, huh? Yeah, so you, you do have to be able to trust your, your partner over there or in our case trusting our, our own team to, to manage things. It's, it's a really demanding, I mean manufacturing is, it just takes so much energy and passion.

**Speaker ?:** It's okay,

**Pete Staples:** you can say it sucks, it sucks a lot of times. It can, it can. It's rewarding too though because, you know, we, when we ship, we take a, we call it a container party. So, in our Slack channel we actually take a photo when we're loading up the container and, we used to even like drink, drink beer at each container but that started to become a productivity problem.

**Pete Staples:** Who packed this thing?

**Pete Staples:** We were joking because we also had those little confetti cannons and we were wondering what our clients would think if they open up the container. It's the strangest packing material. really ineffective but it's nice color. But it's, you know, it's physical so I guess that's one cool thing when you're, when you're manufacturing is it, it's, it's shipped and you get to see it and, you know, pad it and know that a lot of people's hard work came together into some physical goods. So, yeah, I've, I've warmed to it but you gotta know that you're in, getting into something pretty, pretty challenging if you decide to open a factory.

**Pete Staples:** Yeah, no doubt. I mean, what is, what is your, I mean, I've heard this from different people but what is your personal take on like the threshold to taking stuff overseas? I mean, obviously I would think it'd be lower for, for working with Blue Clover. Obviously there's gonna be, there's a lot more capabilities. It's a more seamless transition but what do, what do you usually advise people in terms of when to, when to go to China or Shenzhen specifically and, and really dig in and try and make it a, a broader, like in terms of numbers of units?

**Pete Staples:** Yeah, for, like for us it's not always unit quantity. It's more about like how, how much, what the economics look like. So if it's a high-end expensive product you don't need to make a million of them for it to be worth everyone's while in the supply chain. So, I guess our threshold is a million dollars a year. That's kind of, I think, low in our industry. Not ridiculously low but it's a lot lower than a large Flex or a Jable or Foxconn or someone like that would want to see. Below that, I think it makes sense to do it where, closer to wherever you are and, you know, drive over and, you know, watch the line yourself and really see what kind of, what impact your design is having and give yourself the option to revise the design and make it more manufacturable and then when you take it overseas if you decide to do that you'll be in better shape. So, we have a lot of clients that start out producing in the Bay Area which is not, not a low-cost manufacturing hub necessarily but it works because you're really trying to learn about your product and learn how to make it.

**Pete Staples:** I mean, and any plans to open your own stuff stateside? I

**Pete Staples:** considered it, I remain open to it. I visited a lot of CMs in the Bay Area to try to understand where we might fit. What role could we play? And I was pretty impressed by what I saw. I actually felt like, wow, there are 25 of them right here that pretty much know what they're doing. What would I bring to the table? Oh, I see. I didn't see enough of a hunger for capacity here to take that step here anyway. So, so far we haven't pursued that. I guess if there was such a thing as a tabletop PCBA line or I've heard of things like that, but nothing that really looked like it would do any of the jobs that we see. But if that existed, that would make it a lot easier to bring something to the

**Pete Staples:** space perspective or ease of use?

**Pete Staples:** Just speed and capability and accuracy. I mean, what I would love is you could print boards and you could populate them on a desktop and have a little batch oven or something like that. and I've talked to people who tried to set that up with what is it? LP, LPKF? That's right. Yeah.

**Pete Staples:** Yeah.

**Pete Staples:** Yeah.

**Pete Staples:** Yeah. Like the board routers that are, and they're very advanced and, well, there's different levels they have, right? Yeah.

**Pete Staples:** Yeah. So I, and I've visited Nano Dimension, so they do the printing. They have a PC. The Dragonfly, right? Dragonfly, yeah. Yeah. But we sent boards there to test it and they're like, well, you know, we're kind of busy. We may be able to get you a sample in a month or something. I don't know. It just, I'm cheering them on. I don't, you know, want to throw stones, but it just didn't look like it could do anything that we see in terms of an order in terms of layer count or.

**Pete Staples:** Yeah. Yeah. I mean, it's a pretty, pretty mature process for getting many, many layer PCBs, right?

**Pete Staples:** Well, at the time actually they said, well, this board won't go through a reflow oven and we're like, well, that's the next stop of the line. That's right. Yeah. It's like, yeah.

**Pete Staples:** I don't have my, I don't have a,

**Pete Staples:** so yeah, so far the, the, that real turn type of operate or small scale, we haven't seen anything we could use yet.

**Pete Staples:** Okay. Yeah, that makes sense. And I think that it is, it is a, some of it's just raw economics, right? I mean, that it's like what you're talking about. So it's interesting that it's, you know, you might bounce someone out to a local house until they're ready to, to move over to, you know, to your Shenzhen operation, that sort of thing. So I guess then your threshold must be a lot lower for the stuff you're building or, or just in general, right? You mean like our

**Pete Staples:** own products? Yeah. I suppose we, we, we give, cut ourselves a break on. Yeah. Yeah. I mean, you can give it the margin because it's just like an operational thing,

**Pete Staples:** right? Yeah. Well, let's talk a little bit about the things you're building because that is still related to manufacturing. So you are now, you've, you've started making your own devices. They are related to manufacturing. What, what are the things that you're building? So we have

**Pete Staples:** one flagship product. It's called the production line tool or what we call it internally is the PLT. see what we did there. Yeah. And, uh,

**Pete Staples:** how often do people start like singing like, uh, what is it? Uh, Pete, no, not PLT. What's the, what's the Michael Jackson song? PYT. Like PYT. Pretty young thing. No, uh,

**Pete Staples:** not, hasn't come up. You will know. You will know. Okay. Well, next time you're humming it on the line.

**Pete Staples:** Yeah, exactly.

**Pete Staples:** Yeah, actually McDonald's put out a PLT product in Canada about the same time we launched ours and we thought we were going to get in a trademark issue, but I think they, they killed it off. It was a impossible burger. It was a plant burger.

**Pete Staples:** Yeah. Got it. Personally, I'm very excited about that stuff, but yeah, yeah, that's a

**Pete Staples:** trademark wise, that could be dangerous. Yeah, so far we think we're pretty much in the clear and it works. So we, we call it the PLT. We have a model called the PLT 200 that we, we launched around the time I was on Embedded with Chris and Alicia. And this year we're launching a new version. It's called the 300. And the big change is that it's capable of programming Linux devices over USB. So the last one was really aimed at 32-bit MCU. We use Nordic NRF52 or STM32, that kind of thing. And it did that fine, but we were seeing people putting Linux in all kinds of crazy things and lower and lower cost things than you could imagine. So we felt like we needed to upgrade to handle those kinds of products and then we also addressed other feedback that we got from customers.

**Pete Staples:** Cool. So, well, let's talk about the 200 for people that didn't listen. I mean, we'll link in the embedded episode as well. So what is the PLT broadly? Like, what is the idea for it?

**Pete Staples:** Well, it's a bridge. So for developers working on a product and the factory, there can be a really challenging handoff process, even just for the instructions of programming their hardware. And so this is a box that standardizes the equipment you would need to program devices on a line and also test them. And so I guess the easiest way of thinking of it is what it includes. So it's a programmable power supply. So sometimes you would need a power supply on the line to power up the devices you're testing. We include that. It's also a souped-up J-Link, so it can program the kinds of things that J-Link would do, but also now doing Linux class devices. It's a DMM, and then the fourth thing would be it's a Linux computer itself. And so that is what lets it securely connect to the cloud and push out the test reports.

**Pete Staples:** Yeah. So this basically, so if I was, I've got a new widget, I want to, let's just say the ABC board, the board that I'm building, I have that, I want to be able to program it. I could basically at the end of the manufacturing step. Someone's going to take it, put it onto a jig. This will allow me to not only see that it was programmed, but then also give me feedback on voltages and test pads that might be on the bottom of the board, that sort of thing. Yeah, exactly. Yeah. Okay. And then what else are people looking to do with it? Is it like UART harnesses or how else are people interacting with the boards at the end of their lines?

**Pete Staples:** UART is a great example. So a lot of what you want to do is kind of tinker with your device, you know, sending a command, taking a measurement, send another command, take a measurement, and that's historically been really difficult to do. There have been companies that are more focused on the firmware side of things, and then there are other companies more focused on test automation, but we think that once you've actually got that device right there at that magical moment, it's a great time to pretty much do everything you can to it and have a fully integrated test report for that specific unit. And so UART is a good one. CAN bus is another little feature that we add so that you can write commands that exercise the CAN bus. Voltage, current, resistance measurements, there's a frequency counter. Everything we could think of that we were seeing from our projects is pretty much what we built into the spec sheet.

**Pete Staples:** Here on the Amp Hour, we favor sponsors who help our audience learn. Today we're hearing again from Mauser Electronics, specifically from Paul Galata, who is a senior technology specialist. He'll be talking about predictive maintenance, which is a great real world example combining past discussions around edge computing, artificial intelligence, and IoT.

**Chris Gammell:** You might just have this machine or production line that wretched itself and stopped. Now it becomes where am I supposed to look? And one of the things that predictive maintenance helps us do is keep these uptimes longer, but by also having sensors and IoT and artificial intelligence incorporated, what we can do is even if something does break, we might go, there it is, exactly right in this location, that's where it went awry, that's when I need to go in and address, what do I have to do to go address that? Sometimes it is, you know, turn a screwdriver, flick a switch, you know, whatever and things get rolling again. In other cases, you have to go back and look and go, nope, there's several other factors that have caused this to, you know, break down in this area. And it's hopeful that what you can do through the predictive maintenance is address any and all of these various things that might build into constituating a problem.

**Pete Staples:** Yeah, we had one past guest who was doing remote sensing of the current going into a fan that cooled down a stamping machine in auto plants. And it was because the cost of downtime was so high that the automakers were willing to pay pretty much anything for it. And it was like, so how

**Chris Gammell:** does cost of downtime? You know, there's so much complexity going on when we're producing something with such tight tolerances and high frequencies and those type of things of what we're doing that what we want to do is to be able to operate efficiency. And you can imagine that when a business is shut down, just like when my internet is turned off, just think what that does to me.

**Pete Staples:** I asked Paul to give another example, and he gave one that I think many listeners have experienced and will therefore understand.

**Chris Gammell:** I'm not that handy with my car, but I do know that I'm supposed to go in every few thousand miles or ten thousand kilometers of driving and change the oil. I do that in order to keep the car running longer. I don't know anything per se is going to break, but I do know that if I don't keep regularly changing the oil and going in and making that, that ultimately I'm going to have a very, very expensive break because good lubrication is essential to keep things running. And so in the same way, we go in and we set up, whether it's something like a frequency or certain conditions are met or things exceed a certain boundary condition that design engineers have put together to say, hey, now's the time to step in and do that. So we can use more information than just something like I do with my car where I say every three months or, you know, so many kilometers of travel change.

**Pete Staples:** As in any of these discussions, I was curious about real world examples and where we can expect to see this technology put into action.

**Chris Gammell:** I think the largest three industries that are going to use predictive maintenance are industrial factories, lines, operations in the homes and that type of thing, smart homes and smart buildings, industrial offices, those type of things. And then finally in the automotive section, which is just becoming all about electronics, explosive growth there where the car becomes more intelligent as we give it its ability to drive and sense its surroundings. It's also going to get more and more intelligent about what it needs to keep itself operating.

**Pete Staples:** To learn more about how this might impact industries you're working in and how predictive maintenance will save your users money, check out theamphour.com slash predictive and that'll take you to the Mauser page about the topic. Once again, that's theamphour.com slash predictive to learn more. And now back to the show. And then, I mean, so you mentioned that it was hard because of these kind of disparate tools that are out there. What made it hard about that? Like what wasn't connecting at the end of the day? Like what was an example of like you'd be running an old service, you'd maybe program it, but it couldn't do other things? Is that the idea?

**Pete Staples:** Well, at the larger established CMs, they're very LabVIEW based. So they typically say if you want to do test automation here at our factory, you got to write down everything you want tested and we're going to give it to a specialist who's going to build a GUI on LabVIEW and build all this stuff that does that test. But then there's only that one place that can run it because they've got the license, they've got the hardware configured for it. It's all very specific to that location. And we've talked to a lot of people who ran into that and they just, the only way to really figure out was what was going on in reality on the line was to go there and often it wasn't very close by.

**Pete Staples:** Got it. So then you start talking about maybe being able to mirror a setup on your bench in the States and then also have one at the end of the line and have a very similar setup. Is that kind of the thinking there?

**Pete Staples:** Yes, to standardize the hardware and the OS so that the only thing that the engineer working on the project has to spend a lot of time on is the test plan itself. So he's just writing, he or she is just writing this test plan, which is a script that can be sent to all the PLTs wherever they may be and they're going to get the same result because it's running on the same hardware and the same operating system.

**Pete Staples:** So now the test plan is also like a revision controlled kind of thing and then you could do like a release and say, oh, we're moving from 1.15 to 1.16 and here's the, here's the change notes, that sort of thing.

**Pete Staples:** Exactly. I mean, the release, pattern is we pretty, we really embrace CI, CD and people who are developing in GitHub, which more people seem to be doing firmware in that environment. And so once a new version of firmware can be released, that would be also an opportunity to release a new test plan, maybe a new label configuration file. So these things get packed up into a release and that's the mechanism for deploying out to PLTs. Okay. And you can, you can have different deployment groups. So you could have one for staging and then you could have one that's right on the line. You could have identical lines at different factories, but then you could update them all simultaneously.

**Pete Staples:** Hmm. Okay. Yeah. That's a really interesting point too. So it seems like the LabVIEW methodology, it seems kind of heavy handed, honestly, because it's like you could add so many things to it, right? So much specialized equipment like Pixie and, you know, talking through GPIB to a wide range of tools. It seems like this is kind of like a scaled back version because maybe you don't need as much specialization, but also that allows you to broaden the scope of like what you can talk to and get more volume in terms of the number of testers out there. Is that a fair characterization?

**Pete Staples:** Yeah, I think that's, that's really fair. I mean, and I did an amazing, at the time they launched that it was a huge breakthrough and they have, I'm sure they can beat us on certain technical points on their test equipment, but a lot of people really just need DMM type functionality. They just need to be able to be sure it's really happening on every single unit. And that's what we've tried to make cost effective. Yeah.

**Pete Staples:** Yeah. It's interesting because it's like, I would imagine a lot of the IOT type of devices that are out there too, unless they have some specialized input device. So like if you're using like a pressure sensor or something like that, you might want to have a pressure chamber that's tied to it. And I would imagine that sort of thing would require, you know, if you wanted to do a functional test like that, where you actually take the pressure all the way up and all the way down, or you're doing a calibration, that sort of thing, that might be out of the scope of the PLT. But if you're assuming, if you're getting a sensor from a manufacturer and it's already guaranteed to a spec, and then it's talking over I squared C, you might not be doing that functional test. You might be just sampling on the actual output of, or input to the pressure side of things.

**Pete Staples:** Yeah, that's a good point. And we named it production line tool. We didn't do a focus group or anything on it. We just kind of came up with that. But it does emphasize the point that this is not really built for design validation. So you wouldn't see it at a SGS lab necessarily for thermal vac or shake and bake tests and things like that. You could, but it's not really made for that it's made to be for validating what you want to test on the line and then very quickly, but precisely getting that going on a line and being, having that live feedback so that you know, you know, it really happened. You can get, you can get the updates in Slack even.

**Pete Staples:** Right. Yeah. So that's what I was wondering about. So reporting back to home base, like, what does that look like? Is it just like an MQTT kind of thing, or is there like a database it's tied into? Like, how does it, how does it actually let you know, you know, unit one, two, three, four, five just went through the line. It's out of spec. It didn't talk on, you know, test four, seven and 25 didn't pass that sort of thing. Like, how does that could, how does that get tied all the way back, especially for a PLT that might be in Shenzhen when you're sitting in San Francisco?

**Pete Staples:** All the PLTs are connected to PLT cloud. So it's a cloud native device. And so as, as it's running, it's sending each report back to the, the cloud backend that we built up. We do that because we have to ensure there's a secure connection. People are putting their firmware through this pipe. So it's gotta be, you have to make sure there's not an opportunity for a man in the middle attack to be like, oh, that's the firmware. Well, let's just give it the same name and put our little firmware in every device or something like that. So we have to sign off on the security of that connection. Once it's in PLT cloud, there's a portal. So from a web browser, you can see, you would just click on reports and then you would see the list of reports one by one on each unit. And those can also be exported. So we have a feature called report connector, which allows you to set up to dump those into something like an S3 bucket or some other database. So that if you have your own data lake or your own archiving of all these reports, we're not trying to make it hard to get those or anything. We, we, we actually recommend exporting that if you have some destination destination like that set up. And then the Slack app is just a, an app that we built that you could install on your Slack instance. And then it would show the pass fail on the overall unit. So the, the total test report and result. And if you click on it, then you could see the detailed report that would show you which test failed.

**Pete Staples:** Yeah, that's awesome. What does the actual interface look like? I mean, so is it just like a generic, like what is the physical connection looked like? Does there some kind of like connection header that goes out to a bed of nails wire harness? Is that sort of the standard?

**Pete Staples:** Yeah. The ICT is the kind of easiest to understand arrangement. So we ended up building our own ICT fixtures too, to just kind of convey more clearly what, what you might use this for. It doesn't have to be for PCBA testing, but that's the most popular use case. And so on our shop, we also provide a ICT chassis, which is just a fixed thing to hold these Pogo pin cassettes as we call them. So the cassettes are what engage with the board. And then there's a connector on every cassette that, and a standard cable between all of the, any, any cassette and our PLT.

**Pete Staples:** Do I, do I spy a DB nine or DB 25 rather, or something, something more?

**Pete Staples:** There's a HD 78. That was interesting. Oh, it's even more. Okay.

**Pete Staples:** It looked like a DB 25, but now there's three rows. I see. Yeah.

**Pete Staples:** Yeah. We, we didn't want to design our own connector. That was, that was for sure. And this was the largest, I mean, the most pins we could find in a fairly rugged connector. Actually later found out Garmin uses this connector in their glass cockpit product. So there's at least one other user out there. It's not, these, uh, uh, D sub connectors are not exactly flying off the shelves, but they still make them. And, uh, it was a good fit for us.

**Pete Staples:** You know, in 2021, uh, the, the measure of success is just how few other people are using it. Not, not how many people are using it.

**Pete Staples:** Well, it's us, us in Garmin, as far as I know. And the reason for that connector is you've got a lot of test points on your board potentially. And we wanted to provide as many, cover as many as we could. So we still have to use MUXs, but we can support, I think it's 48 digital test points and 45 analog test points. And that's because we picked a really big connector. And beyond that, if you had, if you came to us and said, well, I've got a hundred test points on my board, any kind of outside of the PLT specs scenarios like that, we, we can address with the cassette. So the cassette is always custom anyway. And if people need to test like a GPS signal or Flora or, you know, something that's just not standard in the PLT, then we can design that into a cassette for some engineering charge. Got it.

**Pete Staples:** Yeah. That makes sense. Yeah. And then that actually brings up another thing that this is reusable as well. So like the PLT would be able to swap between as you update your line or as you change your product or whatever, you, the cassette would probably carry along with the rev that the board being made. Right.

**Pete Staples:** Yeah. You can reuse the cassette. The cassettes themselves have IDs and everything. So we kind of envisioned that being a library. We, we called it cassette cause we're like, yeah, you know, we should bring back cassettes. Nobody has, nobody's making cassettes anymore. It's a cool word.

**Pete Staples:** Right, right.

**Pete Staples:** It's ready, ready, ready to come back. Yeah. We talked about it in the show the other week actually.

**Pete Staples:** Yeah. I heard that. So, and we had a French guy working with us at the time that was like, yes, it is a cassette. That is, that is what it is. And so it shall be.

**Pete Staples:** So, uh, can't, can't fight the,

**Pete Staples:** can't fight reality, you know? So, so we kind of picture that, you know, honestly, nobody's got like shelves and shelves of a full library of cassettes, but you could because they're the same size and they're removable and that's a lot better than what a lot of people do have, which are cemeteries of ICT fixtures wrapped in plastic wrap, taking up like tons and tons of shelves and, you know, getting one of those back up and running is a real crap shoot, you know? And, uh, ours w because it's a more, I would say more engineered. It, it, it, you, you, you kind of know what to expect. You, you put it in the chassis, you connect the standard cables and then you run the test plan that you ran last time and you're going to get the same result.

**Pete Staples:** Yeah. I mean, one thing that I think we talked about, but also does pop out as you look at this sort of the system and setup is I'm sure that there's many engineers listening to me like, Oh, well, and the bristling and they're like, I've, I've done this. I've, I've standardized and I've done this. And it's like, yeah, but I bet you weren't allowed to take it from company to company. And so some of it is just having a third party, like, like blue clover doing this. It's just kind of nice to have, you know? Okay. So yeah, the IP maybe don't own the full IP and it's not completely custom. You don't control everything about it. And yes, there's cost involved, but it's like just having any standard, I feel like in the, in the, out in the world, uh, or any system out in the world, it allows some level of standardization. So if I go to a company a and I design a completely custom ICT, I could not go, I'd have to go and re-engineer that at company B, you know, like I just, I can't bring my design files with me, even if it's, you know, a completely similar kind of design that I'm testing at the end of the day. So having something like this allows you to basically interoperatively switch between companies and use kind of, kind of similar things as well, which is nice.

**Pete Staples:** Yeah. A lot of people have made PLTs for sure. And, uh, but it's $2,000. I mean, it's not, it's not anywhere near the cost of engineering something like that yourself. Right. Right.

**Pete Staples:** $2,000 or 10 main hours. Right. You know, like, yeah. Yeah.

**Pete Staples:** And, and really these test fixtures are typically, I mean, at least our experience in Shenzhen is they get made in Shenzhen, uh, nine times out of 10, it's like a local, it's a small shop that comes over, looks at your board and takes one back and, you know, tinkers with their CNC machine for a while and has like analog dials and, you know, these things come back and they put in the like hot glue, some buttons on it and stuff. And red light, green light. You need that too. Don't forget that. Oh, we have that on the new model. I mean, you gotta have it. And, uh, so it's, it's just not replicable, you know, like that person just has a stock of certain hardware in their, in their shop. And yeah, you're going to get different results if someone else tries to make that. Yeah. Or even that person tries to make it a year later. I get that that could end up being, being very different.

**Pete Staples:** Yeah. I mean, so, uh, looking at the device itself, I mean, I've, I've got the webpage up here. There's basically an access port in the back, but it does say as well that there's like a hardened Linux computer internally. So like what is, what's going on internal to the box as well?

**Pete Staples:** Well, we use Linux to run the, the display. It doesn't have a keyboard that's intentional. We didn't really want it to feel like a computer and have all the, I guess things that could go wrong. We wanted the operators user interface to be highly simplified with a small number of buttons. That's essentially loading a test and executing a test and aborting a test, you know, not, not, oh, here's a command line. What would you like to do today? Or something like that.

**Pete Staples:** Yeah. Yeah. So it's almost more like a, like a 3d printer display where it's like you can pop in, there's an SD card in this case, but it's like you basically, you have the choice of whatever's been loaded on there and then you can run that thing that's on there versus designing the thing that you're putting onto that 3d printer. In this case, a box.

**Pete Staples:** Yeah. It's not meant to like develop a test plan, for example, it's really meant to, uh, to, to run it. And then, you know, we have to connect to the cloud. So you don't really want to be building that on, on nothing. You, you, we, we just use, uh, uh, the Linux kernel and build on top of that so that we can have the, we have a secure element inside of the unit. And there's something that I normally refer to as dual certificate pinning. So essentially the, the cloud is looking for the specific unit and this unit is looking to a particular location in the cloud. And, you know, that's always got to be resolved so that this critical data can be exchanged securely. Got it.

**Pete Staples:** Yeah. Yeah. That's so then does that also enable like provisioning of devices that are out in the field too? So like if I'm making a wifi device and I want to use a PLT to program it, but I want to give that wifi device that like an AWS certificate, does that secure connection enable that sort of thing?

**Pete Staples:** Yeah. It's not automatic. We do have a feature called web hooks so that you could go get serial numbers out of your own cloud backend and put those in. It's starting to come up more and more this need to put tokens in each unit. So anything that's just going to be on some secure network, it may need to have a special identifier. This is a good thing to build on top of to implement those things. But some of those token servers are kind of specific. And so I won't just say, oh yeah, it works out of the box. Like there may be some, there may be something that has to be built, but that secure connection exists. So it's a really good mechanism for doing that sort of thing. Yeah.

**Pete Staples:** So like you'd mentioned that this, there has like a secure element internally. Is it the idea like, so say someone like a disgruntled employee, like walked off the line and they're like, I'm taking this with me. And they take that box and they try and use it somewhere else. Is that kind of the idea that you can basically deactivate different elements remotely, different boxes remotely?

**Pete Staples:** Yeah. A box is enrolled to an org. And so if somebody else got it, they couldn't do anything with it. I guess actually that's not quite the case. So they couldn't do what that org was doing with it because they'd be locked out of it, but you could re-enroll it into a new org. So they, they can be reprovisioned, but they are assigned to an org and, you know, can't see test plans from other orgs and things like that.

**Pete Staples:** Yeah. That's interesting too. Yes. I mean, cause this is going into, I mean, a CM might not, might have four different companies that are using that CM. Usually the lines will be separate, but things, wires could get crossed, whatever. And so I would imagine making sure that only, you know, when board from company A is on text and PLT for company A with using firmware from company A that like, you want to make sure all those things line up and not just for a security basis, but also that you're putting the right firmware on the right device, that sort of thing.

**Pete Staples:** Yeah. The, the model so far has been more that the brand holder buys the PLT and sends it to the CM and then they, they just run it. But it'll be interesting to see over time, whether the CMs just say, okay, we have a PLT is provisioned. It's, it's enrolled in our org. So you need to, you know, send us the test plans and so on through our instance or, you know, or whether they'll get reprovisioned more often, something like that could happen. But we don't, we just make sure that, uh, if you buy it, you control what's on it and you control, uh, what it can do and that, you know, nobody else can use it with their own test plans and things like that. There are different permission levels, but every org has, uh, one specific owner. Okay.

**Pete Staples:** Okay. And then, I mean, so a lot of times this is in China, I've heard about, you know, connecting and, you know, getting data back from factories, whoever the great firewall can be kind of tough. I mean, is it, does it kind of make that more seamless to get data back out? Is that something that this enables?

**Pete Staples:** It definitely seems to it's in a, so it's a lot of the PLTs are used in China. We haven't had any issue of the server it's talking to being blocked. And then, you know, not, not being able to work properly. If the more common problem we've heard of is simply the reliability of the network. So if, if they say like, oh, our connection is, you know, acting up, we just can't, we don't have internet where we're like, well, it's not going to work without internet. So yeah, right.

**Pete Staples:** That is part and parcel of this product line.

**Pete Staples:** Luckily it's not working on wifi. It's a ethernet cable. So you do just plug it in. And then if you, if your entity has internet, then it's going to work so far, it's been proving itself to be the case. If the internet connection itself is flaky, what we recommend are cellular modems. There's not a ton of data. It's not like a live video feed. It's not streaming. Yeah.

**Pete Staples:** Right.

**Pete Staples:** So it's fairly, and we do that at trade shows too. We'll just take our own modem and connect it up and use it that way. And that's, that's been pretty effective too.

**Pete Staples:** Okay. That's cool. So what are the, so you keep mentioning test plans. What do those look like? I mean, is it like a Python script? Is it like some kind of internal scripting language? So if I, if I'm starting, so if I'm writing a test plan for the ABC board, what does that actually look like on my computer, on the PLT, on the PLT cloud everywhere? Like where does, what does that look like?

**Pete Staples:** It's a YAML test script. So it's a YAML file.

**Pete Staples:** YAML rhymes with YAML.

**Pete Staples:** Yeah. Happy coincidence there. So it's, we, we pick that because you can add comments to it. It's just a simple deterministic file, but unlike JSON, you can add what that test is about. So normally you're just listing tests one, two, three, four, five, and then each test may have one or more steps. So you'll have test one and then step 1.1, 1.2, 1.3. And those steps tend to be like connecting up to test points. So you might be establishing which signal you're looking at. Is this an analog test point? Is this a digital test point? And, and you have to configure the routing back to the PLT so that you can take the measurement that you want to. And then you may measure that there's a command called measure. And that may be measuring voltage, maybe measuring current. And you're just identifying which locations on the board you want to take that type of measurement. Programming is just program. And then the file name of the firmware image and what type of target. So you might say program NRF 52, and then the name of your hex file. So it's fairly fast to learn, but every, every line matters. So it's not trivial. Right, right. It doesn't write itself. I mean, you, you do have to know your product in order to write the test plan.

**Pete Staples:** Yeah. Yeah. So I'm looking at the docs.pltcloud.com and the test plan reference. So this does have a bunch of the, the things on there, but you're saying like the connection type stuff that, so that is like internal to the PLT. It's translating that command into basically like a control of the MUX. Is that, is that right? Yeah.

**Pete Staples:** Yeah. So it, it, the, the report then is just a regurgitation of that test plan and except with the result. And, uh, that makes it, you know, fairly predictable. You know what you're looking for. When we make a cassette, there also has to be a little bit of a conversation, which we call the test point matrix. So that matrix identifies what the meaning of those test points are. We don't have a AI way of doing that. You pretty, you pretty much have to tell us. It's like a cloud of test points. Like they have to be identified whether they're analog or digital and ground or VCC or whatever. Okay.

**Pete Staples:** Yeah. Yeah. That makes sense. I mean, that's like, uh, like a pin, like a pin table for a microcontroller as well. Right. It's like, yeah, you might be talking to port, you know, port one pin seven or whatever, but it's actually pin 45 on your BGA or something like that. So yeah, that makes sense. Okay. Yeah. And I mean, looking at the, this is actually really some of these basic examples you have on here too, are, it actually looks super clean. I mean like the actual versioning and just the, the steps that it's doing, it, it doesn't, uh, like the command is like identify NRF 52. That's okay. That's pretty, pretty good. Yeah.

**Pete Staples:** Yeah. Yeah. That, that's, uh, thanks to our dev team. I mean, they're just, they're really good. And, uh, you know, this was born out of their frustrations and their, uh, years and years of experience. And, you know, this thing just came to life. It wasn't, it wasn't like we went out and did a survey. What's the market asking for? Nobody was really asking. It was just, uh, we kept doing projects and we kept building things as needed. And finally there was a project that just had so many tests. There was just no other way other than. Take this anymore. Yeah. Yeah. Yeah. This is great. Yeah. It's a scratch your own itch kind of project. Huh? And we didn't talk about the scanner label printer, but you can also plug in that directly. So, uh, that makes it very manufacturing friendly.

**Pete Staples:** So that, that, a plug that plugs into the, like, that's something that would plug into the actual back of the PLT. Is that the idea?

**Pete Staples:** Yeah. Yeah. Just in the USB ports. And that's something, uh, Jan, um, from parts box. And I talked about, cause he, he was like, we do so many things, but the one thing we can't do is just drive a scanner, drive a label printer. Cause it's a web browser. The web based stuff, huh? Yeah. Yeah. Yeah. So, uh, that's, that's one thing that this offers is you can just plug. Like we have to check it. So, uh, we don't work with every single scanner and every single printer, but the four of each or so that we tested against, that's all you do is plug it in. And those are also things you can put in the test plan, like scan or print. That's nice.

**Pete Staples:** Yeah. And that's, I mean, so that's, is that because this is operating at a lower level, like, like, like basically script code that's running on top of the OS, that sort of thing versus like in a web, web context, like Leon was talking about.

**Pete Staples:** Yeah. I think, I mean, his limitation was that it, it can't, he can only process so much from a browser. And, uh, like the, the printing function is very, I think he said it can only print what's on the screen. You can't say print this file, for example, but we can, um, allow part of the release can be a, a dot ZPL file, a zebra zebra label format. And, you can put that in and it can say print pass and then serial number, and then insert the field for the serial number. And, uh, that can just be part of the test plan. That's nice. Normally, normally that's done if everything passes. And then if it fails some test, you have a different label that says, you know, sorry, try again. And broken. Yeah.

**Pete Staples:** Put this in the scrap pile, uh, have the tech look at it. Please fix.

**Pete Staples:** Yeah. And as a, as an old line manager, that's a huge relief to just have automated labels about what tests fail. Cause, uh, I'm so used to reading, trying to decipher handwritten things on masking tape that's, that say like no lights or, you know, it's just something like really doesn't work.

**Pete Staples:** Doesn't work.

**Pete Staples:** This is buhal.

**Pete Staples:** This is no good. Yeah. Yeah. Oh man. That's yeah. That's really true. I mean, and is that the zebra stuff, is that the, like the acid proof, like the, that, uh, polymer based labeling system as well. I've, I've heard about those. I've never really used that. I I'm used to like, I have an old brother label printer here, you know, paper, paper based adhesives, but I've, I've heard about the ones that are like, like chemically safe as well.

**Pete Staples:** I'm not the expert on it, but the, the paper, you know, the materials themselves have a million flavors. And so you can go, it's a big spectrum and zebra, you know, they've done all these acquisitions. It used to be symbol and then like Motorola. And now like all the scanners and printers are all under one roof. And, uh, so far we're, we're kind of happy just working with zebra. I know they're not the cheapest, but they do have a big range of models. So the scanners typically aren't that expensive. The printers are a little pricey, but they're a lot cheaper than proving this works on another printer. Yeah.

**Pete Staples:** So, I mean, like, I think that's actually a good topic to talk about as well. Like all of these things, I mean, these are industrial level prices, right? I mean, this is like two grand for a thing is not cheap, right? That I'm not going to probably buy this from my bench here. However, you know, if my client, one of my clients is doing a thousand boards, you know, like what is the replacement cost of something breaking down? And like, so if I'm doing a run of a thousand boards and I put the wrong firmware onto a thousand boards, how much does it cost to have someone open the case up, plug in a, you know, plug in a tag connector with whatever is equivalent, reprogram it, close it back up. Like that just like the cost of replacement or the opportunity cost of all these things is really high. And so, yes, you know, the sticker price is high on these things, but it, it saves so much money potentially.

**Pete Staples:** Yeah. I wish I could get a mailing list of all the people who've had to go back into a warehouse and reflash firmware or something. Like a support group. You're like, I have something that you may be interested in. That's right. Yeah. Yeah. Yeah. Yeah. I, I mean, it may not be, I don't really know anything that's a direct competitor and, you know, obviously I'm, I'm quite favorably inclined toward our products, but I would just say, uh, I just say like, uh, you know, ask your CM for a report on every unit and, you know, if there's any other way to do this, I'd love to know about it, but typically they'll give you a pretty, pretty slick deflection or something like, oh, it's all in our, you know, ERP system. That's right.

**Pete Staples:** That's right.

**Pete Staples:** Very secure. That's right. Very, very secure.

**Pete Staples:** We want to make sure we don't put this on the internet. Uh, just to make sure that hackers, you know, hackers don't get to it.

**Pete Staples:** But you know, that doesn't seem like a big ask to just say like, look, I I'm going to give you an order. You're going to make my stuff. This is my business depends on this product and I just want to get a report on every unit. Can you make that happen for me? And I, I think they should be able to do that. And I don't know any other way to do it so far.

**Pete Staples:** Yeah. I mean, one thing that Jan talked about when he was on the show was kind of like tying things all the way back. He was talking about it in a medical context, but you know, just more broadly as well of tracking and troubleshooting from having data. You know, he talked about having data that's attached to each board. What about then? Is there something with the stickers that you might print out or the test reports or something like that where you'd be able to do a post-mortem on something that's like out in the field then and be able to track it back and be like, oh, actually it didn't pass a certain test or like, how does that data end up getting used aside from the business intelligence of we've got 99% yield, that sort of thing.

**Pete Staples:** You can connect the dots with it. So I guess the, the, a classic example would be you have a product with three circuit boards in it. And as each board at the board level, you might scan a QR code on a bare board that identifies which bare board you're using. You populate it, build it, test it with, um, an ICT fixture. It passes all the tests. You put a new label on it that identifies it as a PCBA. And then at the end of the line, you've got three different boards and you scan those three PCBA serial numbers. And that becomes part of the, the test report of that finished good. And that way that's seems like the cleanest way that you could have a test report that then says, all right, this unit is made up of this board and this board and this board. And here's the test report on those boards. And then, you know, see, did that, did that board get tested three times in order to pass or was it a first time pass? When was that, when was it tested? You know, the timestamps are all part of the test reports, the location identity. You can see which PLT was used. If there was ever a variation in PLTs, you could see which pogo pin cassette was used. If a cassette was wearing out and started to show failures, you could trace it back to that, that cassette as well. So it just ties things together. It doesn't necessarily tell you what's wrong, but it makes it a lot faster to get to the root cause or get meaningful data out of it.

**Pete Staples:** Yeah. Yeah. Those test fixture wear out things. Those are fun. I remember my Samsung days, we used to do gauge R and R studies. We'd like compare like, oh, actually no, that, that one, like scanning electron microscope always is low. And you'd like, you'd actually be able to like pull that out of the data, which is insane. But like, then you could start to say like, that's why, you know, obviously you needed fixing or Cal or whatever, but you can actually verify that that's why these things are trending in the wrong direction. And I guess you could do the same kind of thing here if you wanted to kind of back calculate all those, all those things. Yeah.

**Pete Staples:** It just makes it easy to gather that, that data. I think there's still a lot of, a lot of work to do to process some of those things. And we're not really that far along on the analytics aspect of it. And we, we may, we may never even get into that, but we will try to make it as easy as possible to gather good data and, you know, send it to the right place. Yeah. Yeah.

**Pete Staples:** Yeah. One thing I also think about is, so you mentioned this example, I like this example with the three boards, you know, you say you have connectors in between or cabling or whatever it is. I always think about like cables and connectors as like abstraction interfaces, right? So like, yeah, the analog signal going from board one to board two is there or whatever, but there's also an I squared C and you know, you don't, you don't know maybe if the functionality is the same, there's no way to actually test other than like, so if board one is supposed to talk to board two over I squared C or serial, and it's got some command it's supposed to throw down to it. But the firmer version is not right on board two. And it's just like, I don't know. I don't know what you're asking me for. There really wouldn't be any way to check that. It might look like a perfectly fine board, but there's no way to actually validate that until you plug them together. And then you just have this like random error. But it sounds like with the PLT and like these test reports, you actually could say, oh, actually, no, no, no. Board one had firmware version three, board two had version four, and they, those don't talk to each other yet or something like that. Yeah.

**Pete Staples:** Yeah. And it's increasingly common to have a product with multiple, like a PLT itself has three versions of firmware on it or three instances. Like the UX is one piece of Zephyr. The motherboard's got another piece of Zephyr running on it. And then, and then Linux is running on it too. So, and we've had projects where there might be a five or six different firmware images running on a single board and it's just a lot to keep track of.

**Pete Staples:** Yeah. Right. Right. Yeah. And I mean, like, yeah, you could have all the API documentation in the world, but if you don't have the right firmware and the right checking at the beginning of like, oh, actually we don't, we don't talk to each other yet. I don't have that language in my language, that sort of thing.

**Pete Staples:** Yeah. And, and some people might be like, well, it's all over the air updates anyway, but it's like, yeah, but it's gotta get programmed once somewhere. That's right.

**Pete Staples:** That's right. There's no bootloader for OCA yet. I mean, once that shows up, then that'll be interesting. But yeah. Yeah. That's that first time. That first time is pretty critical, huh?

**Pete Staples:** We think so. Yeah. Yeah. Yeah.

**Pete Staples:** Well, what are some of the trends you're seeing? I mean, obviously you, you know, you've, you've mentioned already that you're seeing trends over time and how people are testing things. You'd mentioned at the beginning, like the moving from PLT 200 to 300, that there's more Linux out in the world. Where do you see the IOT industry or just more broadly, like the embedded industry? And where these, this combination of hardware and firmware being put out into the world? What do you see next?

**Pete Staples:** Things are definitely going up market. So just Linux on, on smaller and smaller things. I think there will still be a separation though. There, I, I, I sort of feel like things under a hundred dollars are Zephyr land and, and should be not running Linux. It's just too, you know, if, if it's just a temperature sensor, like, come on, let's not, let's not get carried away here. We don't, we don't need the graphics on that one. Maybe, you know, or an air tag or something like that. Like there's, there's going to be a home for these, for Zephyr essentially. But anything above 250 bucks ought to be running Linux. I mean, why not? It's, it's there. It does a lot. You can run a spaceship with it. That's right. Yeah. You know, like it might as well.

**Pete Staples:** Rovers or, or, you know, Mars helicopter. We've got a lot of choices now, Pete, you know, of all the space vehicles that, that could be extraterrestrial vehicles, I suppose.

**Pete Staples:** So if it's that expensive already, you know, it just seems like it should have that stable foundation and capable foundation. And then I just think it's kind of a no man's land, no man's land in between like a hundred, like things just shouldn't be $180. Like, I just don't understand what that, that shouldn't exist. At least in electronics. Got it.

**Pete Staples:** Interesting. Interesting. So, so like someone shows up to like, Pete, I'd like you to, you know, build this product for me. You're like, how much is it going to cost? Oh, 150. Nah. Nah. See you later. Doesn't, shouldn't exist. Sorry. I don't believe in your product.

**Pete Staples:** I, and I also just really hope we're heading toward a future where just devices are better and that they're like longer warranties, more of a support system behind them. And that there's just more, there, there are fewer devices, but better devices and, you know, they're more capable, but they also last longer.

**Pete Staples:** And you're saying this as a hardware manufacturer folks. So that's, that's something he's like, I hope there's less things to build.

**Pete Staples:** Yeah. Luckily we don't have a lot of shareholders. I would have been booted by now if we were a public company.

**Pete Staples:** So, so he's saying what? No growth, no growth. Actually, well, this does change. This is an interesting thing. So, so recently Blue Clover has been taking more of a new tack on, on like focus and things like that. Could you explain, explain what that is in terms of like the impact and stuff?

**Pete Staples:** Yeah. I get with, with COVID, it was definitely an opportunity for retrospection. And, uh, we, we just decided to double down on the environment. And I guess the easiest way to describe it would be, we, we just aim to be the Patagonia of electronics and really advocate for design decisions that benefit the environment. And, uh, it's, it's hard to do because there's so, there's so much business pressure, but it, there's a big societal payoff. If we think about those end of life situations and conditions, and I try to adopt more beneficial features like recyclability, repairability, durability, and that kind of stuff. And there are a lot of people that care about it and there just hasn't been, there hasn't been that leadership in electronics that we, we could really find Apple somewhat, but you know, it's, it's kind of a different species.

**Pete Staples:** The best they're doing is, is, is make, is making the iPhone look the exact same every single year, even if they're not the exact same.

**Pete Staples:** Yeah. I mean, they, we, we, we've been around a while and definitely the quality of electronics has improved a lot. And I, I give Apple a lot of credit for that. I, I, I think they're so powerful now there's always more they could do, but you know, it's also just hard to compare ourselves to the, I mean, they're just so gigantic that I can't. I mean, I actually get tired of a client coming to me and say, I want to do this because Apple did it. It's like, yeah, but that's right. That's right. I can't do that for you.

**Pete Staples:** That's the largest company in the world. So yeah, I can't build you an iPhone for $600 or, or even $1,200 or whatever, whatever they're selling prices. I can't make that at cost.

**Pete Staples:** Yeah. So, you know, there needs to be somebody else that, that, that can gather electronics companies and say, well, how, what can we do? What can we do actually? And we're at, we're doing that with not even electronics companies, but we're working with folks in the climate neutral community, like Peak Design, they make camera bags and Nomad Goods. They do make electronics. They make other things as well. So, Voy and LineDoc are all companies that we just had a meeting this week to talk about recycled aluminum. So we're all making stuff in China. We're all using some aluminum, not a lot, not as much as Apple, but we want to use, we want to use recycled aluminum. And we talk, we all talk to our suppliers and they're all like, nope, we're not, we're not going to do it. And we're like, well, why not? And we're like, reasons. And we're like, what reasons? And, you know, we're just trying to gather together.

**Pete Staples:** It's just new conversations. It sounds like, like, like, why would you even bother to do that when there's all this perfectly good brand new aluminum that came from the, you know, the smelter or whatever. So, right.

**Pete Staples:** Right. So just bringing people together to have those kinds of conversations and figure out achievable goals toward, uh, you know, more, more eco stuff.

**Pete Staples:** Yeah, no, I think it's, it's tough because, because of the financial focus, right? I mean, because of the end result of the almighty dollar, like, I think any of these things are possible, right? Like to make something that's super repairable or to make something that's super recyclable or, you know, using, using recycled materials. But there's, especially at the beginning, there's always cost involved and there's no, there's no external forces aside from like goodwill right now. And so you're talking about the goodwill, it sounds like, which is awesome. And then if these companies also have client bases that are also for that, it's like, that's a really good first step, I think, because I think that it's totally possible to make things that are of equivalent, equivalent quality. It's just a matter of, you know, finding, finding these new methodologies that do that sort of thing.

**Pete Staples:** Yeah. And other industries have proven they can build a market for it. Like you look at food, you look at apparel. Those are two examples where they talk about how they source their ingredients or their materials. And people seem to resonate with that, the work that they're doing. And they're like, yeah, I'm, I'm eating that. If I'm going to put that in my body, you know, I want to know it's, it's clean. It's grown in a sustainable way. And so electronics doesn't fit that exact, you know, it's not the same thing, hopefully.

**Pete Staples:** Yeah. Well, I was going to say, like, some of the body models, many people are not putting things, electronics in their body, but, but yeah.

**Pete Staples:** But at least you're, you're kind of voting with your wallet a bit when you, when you do that, and so we're luckily in a position where we're selling a higher end, you know, we're not selling a $10 product. So we, and, and, and we don't have, we don't have a direct comp competitor that we got to like, I try to undercut on price yet. So, uh, it just seemed like an opportunity for us to say, well, let's make sure we're making this in a way that. You know, we feel good about and that we, we, we can achieve some environmental goals at the same time that we're doing our business.

**Pete Staples:** Yeah. That's really great.

**Pete Staples:** That's really great.

**Pete Staples:** Well, cool. Pete, anything else people should know about Blue Clover or, you know, getting started, sending business your way, buying PLTs, where should people find out more?

**Pete Staples:** At our website. So bcdevices.com and you can follow me on Twitter. I'm at Pete Staples, but mostly it's just photos of bike lanes. So, uh, don't get your hopes up. I just, sometimes I'm on my bike and I'm like, oh, cool new bike lane and take a picture and I don't know what to do with it. So I just put it on Twitter.

**Pete Staples:** That sounds right. Yeah. It's how the internet formed folks. You know, it was just cats to start with. Pete's just into bike lanes, you know?

**Pete Staples:** And actually as a reward for staying with us this long into the podcast, uh, if you, if you're in the U S and you want a free USB-C cable, you can email me at pete at bcdevices.com to send me your address and we'll send you a cable. Nice.

**Pete Staples:** All right. That's great. Cool. Well, thanks Pete for telling us about all this stuff. I, I, I'm excited about this. You know, I'm getting into more of the firmware and the deployment side of things. And these kinds of software enablements are quite useful and might make me look better to clients. So I really appreciate that sort of thing. And all, all these tools are letting people make better products, which is going to have lots of benefits. Like you explained.

**Pete Staples:** Yeah. Happy to chat more about that and glad to see what you're doing with the ABC board. That's, that's a really cool product. And also thanks for creating contextual electronics. Actually, one of our account managers is in your class. So he's, he's learning a lot of cool new stuff and sending me pull requests on sales material and stuff like that. I'm like, Oh, usually sales teams don't do CICD, but okay, cool. All right. That's great. So thanks for doing that. Yeah. Thanks again, Pete. We'll talk to you soon. All right. Cheers, Chris.
