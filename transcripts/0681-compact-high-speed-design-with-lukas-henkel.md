---
episode: 681
title: Compact High Speed Design with Lukas Henkel
url: https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released October 30th, 2024. Episode 681. Compact, high-speed design with Lukas Henkel.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Lukas Henkel:** And I'm Lukas Henkel, the CEO at OV Tech.

**Chris Gammell:** Hey, Lukas, how are you?

**Lukas Henkel:** I'm doing great, thanks. How are you? Yeah, good.

**Chris Gammell:** You know, usually I'm found on a random Tuesday, like today, marveling at your LinkedIn posts of high-speed designs and simulation and just ridiculous density and, I don't know, just all the things that you seem to post about. Great. Keep doing that, please. Thanks for leaving a follow-up.

**Speaker ?:** Yeah.

**Chris Gammell:** So let's talk about that a little bit. I mean, you are the CEO of a design shop, right? I mean, you are doing designs for hire. Is that right?

**Lukas Henkel:** Yeah, exactly. So OV Tech is like a mixture. We are primarily an engineering company here in the heart of Bavaria. But we are also doing our own open-source projects. We have, I would say, a passion for open-source projects. And now we're also making products out of that. So we are currently working on the Raspberry Pi compatible module. We are also working on an open-source laptop. But, yeah, we are trying to apply what we learn through our engineering projects into our own open-source products. That's great.

**Chris Gammell:** Wow. Well, definitely we're going to come back to the Raspberry Pi replacement module. And let's talk a little bit about the things that you find yourself doing. I mean, it seems like if I had to kind of summarize just from memory, and I do have your feet in front of me too, but this is me without looking. People have to trust me. I think I remember just like high-end Linux-capable systems that often interface to things like vision. Obviously, that's a memory. But just the compactness is one of the big things there. Is that a fair kind of summary of the work you often find yourself doing?

**Lukas Henkel:** Oh, I would say so, yeah. So we're doing quite a bit of embedded devices, especially Linux-capable embedded devices. And we also have a passion for miniaturization. So we're working on a project actually on a little system and package where the goal is to pack as much compute power on a little space as possible.

**Chris Gammell:** Yes. Yeah. And yeah, that's a theme that continues throughout. I mean, I remember also you had one where you were putting just gobs of stuff into like an SD card form factor. Is that right?

**Lukas Henkel:** It's the same project, actually. So this is also the open-source SIP. And one time I was just looking at the form factor and said, wait a minute, this could fit very nicely in a form factor of a small SD card. And so I tinkered with the idea a little bit and designed a small baseboard. And yeah, now we have a Linux-capable and also wireless SD card. I mean, it's not a new idea. These things have been around for quite some time. But they are quite limited in their compute power. And also you can't run custom code on that. So I thought, why not? Yeah. If we already have the SIP, why not just put it in the form factor of an SD card?

**Chris Gammell:** Yeah. And I was going to say the hard thing these days is probably finding a full-size SD card like holder. Yeah. True. Everything switched to mini or micro or whatever it is. Yeah. Micro is the one that has common. Absolutely.

**Lukas Henkel:** Yeah. It's just mostly camera stuff, I think, that uses full-size SD cards now.

**Chris Gammell:** SD card is a good example, actually. So we have these humongous form factors, relative, of course, to just for my fat fingers. Right? Like I have fat fingers. I need to be able to plug this thing to a computer. At some point, they existed because that was the technology node. But like everything is leapt past that. It's just, you know, like thinking about chip scale packaging and just the scale and the scale difference of, I don't know, like even the, what's actually triggering the cellular part of the modem on these packages that I use that are already miniaturized. Like they're always scaled up and up and up and up to make them usable to board level PCB designers like us. But you're starting to kind of just take it down in the other direction. So I guess my question is, where do you start running into the limitations, right? Like of this miniaturization?

**Lukas Henkel:** Well, at the moment, it's really just a price limit, I would say. Price limit? Yeah, yeah. So at the moment, what we're trying to achieve, we have a product in mind. Their space is at a premium. So we really have to cram very, very much compute power in a small volume. And that's why we've looked into this open source SIP. And at the moment, we are using standard PCB technology. So the design that you can see or that I've shared online as well, it's just a standard board, standard in quad marks because it's still high density. So a trace width is 75 micron spacing as well. The vias are also quite small with 200 microns total diameter and 81 or 85 microns drill. So it's a very high tech PCB, but it's not at the substrate or interposer level. So that would be the next step. But this step is quite a leap in terms of price. So we tried for the open source SIP, we tried to use a standard PCB manufacturing process just to manage the price of the whole project, but also since it's open source to make it possible for other enthusiasts or other companies even to adjust and customize the module for their needs. And it would be a huge hurdle if we used some highly exotic process to manufacture this module. So we are still using somewhat standard-ish PCB processes. Got it.

**Chris Gammell:** Yeah, so like off the shelf at the very least, I would say, right? The fact that it is still a PCB and it's not like, there's no chemical, well, I guess there's no direct chemical, I guess that's how they do PCBs as well. They do chemical etching. True, yeah. There's no CVD or dry etching happening.

**Lukas Henkel:** Yeah, exactly. It's just in quad marks. I mean, it's still, as I said, a fairly advanced PCB. So not every PCB will be able to manufacture this board, but there are still quite a large number of boardhouses who can take on this challenge and you don't have to go to an interposer level or a silicon level packaging company to build something like that.

**Chris Gammell:** Yeah, right. And that is, I actually just caught up with the folks at, oh, shoot, Octavo. And they are kind of down at that level, right? They are basically taking silicon and putting it in interposers. But it's like a polysilicon level. I don't actually know what the, they're stacking stuff up now and they kind of put stuff side by side, but that's different than what you're talking about, right?

**Lukas Henkel:** At least at the moment it is. We are also planning to go down the route, actually. Yeah. Everybody needs new challenges, right? True, exactly. Yeah. Exactly. So one thing we're also looking at for the open source SIP. So I can walk you through the steps of miniaturization. Yeah, yeah, that's great. So at the moment we're using conventional PCBs and also conventional components. In the next step, we will be starting to embed components into the board itself. So instead of using conventional inductors, we will be using silicon-based inductors. There is some very interesting work going on with our cooperation partner. And unfortunately, I can't share too much about that at this point in time. But there will be silicon-based inductors that you can also buy off the shelf. And one thing about those is they are only 200 microns thick, so very, very thin. And you can embed them even in small or very thin boards as well. So the next step of miniaturization for us will be to move those conventional inductors into the board itself. This will give us some room on the top side of the module for, well, either just shrinking the module or put more features on the module. And the next step will be then to source the memory and the storage dice as bear dice, bondable bear dice, put them on top of the SOC. So stack everything on top of each other and just bond them to the board substrate. But at this point, we will also have to move up in the technology class and really think about interposer-level design rules. So 10, 20 microns space width and tracing, standard PCB won't cut it in this case.

**Chris Gammell:** It's interesting, too, because what I'm hearing as you are saying these things, it's like all of these things are possible, but it's just completely irrational to do it in low volume, it feels like. So you also need to be able to find something that's common use case enough. So you're saying it's a SIP. It's a general purpose SIP, but you have to get enough volume to actually make that a reality so that it's worth that NRE, worth the time investment to actually make this all happen.

**Lukas Henkel:** Absolutely, yeah. That's also one reason why we decided to go with a standard PCB in the first step, because the manufacturing cost for these boards is also quite a bit higher than standard PCBs, but it's still manageable. But once we actually move one step up in the miniaturization game, I would just say, then, of course, we're also talking about other volumes that we have to run this module at in order to make it just financially feasible.

**Chris Gammell:** Yeah, totally, totally. Yeah, I don't know how to, how do you even judge that? So when do you decide to take the next step? Is it volume-based or is it just curiosity-based or is it truly, is there actually anything constraining your space in this case? Like you're like, oh, this doesn't fit. Maybe it's a fit in blank.

**Lukas Henkel:** Yeah, there actually is. So the open source SIP is only one part of a project that we are currently planning. So we do have a device in mind where we would like to use the SIP. And at the beginning, we were actually planning to just not do a separate module, but integrate the SOC and the memory on the main board in our target device itself. But we decided that we want to swap out the CPU in the future. We want to swap, we want to support also other CPU platforms. And we also received some requests for a module form factor of the CPU that we are using. Because we are using the iMix8 ULP, which is a very painful package to work with. It's a 0.4 millimeter Chipscape package. And not everybody is looking forward to routing something like that. And so since there was some interest in the community, we decided to design a SIP. We shown the design online and got a lot of requests from the industry to manufacture and use those things. So there is definitely some interest out there. That's why we decided to go with the SIP approach. And just use it as a drop-in module for our own application. But our application is... How much can I share about that? Yeah, for now, I just leave it at... It's very space constrained. Okay, yeah, that's fine. That's fine.

**Chris Gammell:** You know, reasons to follow Lucas on LinkedIn. Yeah, exactly. It will be open...

**Lukas Henkel:** The final project will be open source as well. So at some point, it's definitely worth checking it out.

**Chris Gammell:** Well, and so the SIP is the one where the Chipscale package is kind of like embedded underneath, right? That's the one that we're talking about here. It's like routed out and then a big Kingston on top. Is that the one we're talking about here? Yes, exactly. Exactly. Yeah, okay. So, and this might... Again, people that already follow Lucas and will definitely have links to his LinkedIn so you can follow him. One thing that's interesting about that is showing the Kingston... So I'm going to just try and describe it with words, which I'm sure will fail me. But we'll have links in the show notes, of course. The memory is... So basically, like, top side of this SIP... And this is PCB material, you're saying, as well? Yes. Yeah. Okay. So top side of the SIP, large Kingston RAM, looks like. I don't know how much. Then looks like power switching with some ridiculous density caps and inductors. Is that right? Exactly. The top side? One point. Yep. Bottom right is sensors or oscillators? I'm not sure what that is, actually.

**Lukas Henkel:** Bottom right, that's... Oh, yeah. That's just an oscillator. So a real-time clock and the main oscillator.

**Chris Gammell:** Yeah. And then the bottom side is a footprint. That's the SIP footprint you're talking about. But then routed into that, so basically like a sunken living room, if you've had a house in the 70s in the US, basically that's where the processor lives, so that it's basically when the whole SIP is mounted to the board, the IMX8 is upside down, right?

**Lukas Henkel:** Yes, exactly. Exactly. Got it.

**Chris Gammell:** So now I, as a designer, I could go and take this SIP footprint. You're saying that OpenVisions would potentially swap that out for a non-IMX8 in the future, something different, some different part, or just taking advantage of that. But basically from a drop-in replacement, now I only need to worry about this open-source SIP footprint that goes onto my board. Is that right?

**Lukas Henkel:** Yes, exactly. And the footprint we've tried. I mean, we are all PCB designers here at OpenVision, so our focus is also to make the lives for PCB designers easy. So we try to choose a footprint that's easy to route. The pin pitch is relatively comfortable to work with. It's 0.8 millimeter, so it's pretty standard BGA pin pitch. So we don't have to use highly expensive stack-ups or highly dense basic keys to break out this package.

**Chris Gammell:** So I actually just gave a talk on this. Lucas and I was talking about this before the show, but I just gave a talk to the Zephyr group about the benefits of doing this kind of module abstraction, right? So now this footprint is the same. I created a footprint which is insanely larger than this. Mine is, so this is, I don't know, I don't see the dimensions on this. The one I'm doing is 24 by 34 millimeters. This looks like this is what, like 10 by 12 millimeters? I don't even know. And it's doing way more. Yeah, it's 14 by 16 millimeters at the moment. Oh my gosh, so big. Yeah, and this is a full Linux system and mine is definitely not. But I do, I really agree with this because honestly, for me, it's kind of like PTSD from the 22, 23 of just like not being able to get a part, right? So if you have that IMX8, so if I had said, oh, you know what? I don't need this open vision thing. I'm going to go and put, I can do layout. I'm going to put my own IMX8, whatever. The benefit of module always is if that IMX8 isn't available or really anything on this module isn't available that would have been on my PCB, I can just potentially get a different skew of this SIP and then still be, my line can be up. That's always the benefit.

**Lukas Henkel:** Yeah, absolutely. And that's also another thing to mention. That's one reason why we decided to go open source actually because we want to give the complete ownership of a system to the designer who actually integrates a SIP. So what I mean by this, if I buy a SIP, for example, from Raspberry Pi, I'm always relying on Raspberry Pi to provide the complete SOM with all the parts that I need. And during chip shortage, there also was a shortage of Raspberry Pis. We don't know for which reason. It could be that the Ethernet 5, for example, wasn't available.

**Lukas Henkel:** Yeah.

**Lukas Henkel:** And now if you are- You just need one part to be robusted

**Chris Gammell:** and then you're lying down.

**Lukas Henkel:** Exactly, exactly. And now since we are doing this open source, the designer who is using our SIP or our SOM can just take a look at the bill of materials and say, hey, well, we don't need this particular part that's currently holding up the delivery schedule. Just depopulate it and deliver the board to us without the specific component. Or they can just adjust it themselves, of course. Yeah. So the ownership, I mean, SOM or SIP is really the central building block for many systems. So in my opinion, the designer who is using the central building block should also have complete ownership over the building block as well because it's at the heart of the system. We are completely in sync on this.

**Chris Gammell:** I think the other thing too is that like, you know, just from a, I don't know, life cycle, right? So I'm designing an industrial product. I want to use this SIP. That's great. And that's what it is today. But then, you know, five years from now, maybe I want to just start designing with more horsepower, right? Surely, if the SIP footprint stays the same, if we have a flexible system that Linux provides, then we can just target the same pinouts to this SIP footprint, same functionality. Obviously, I have to test it as the board designer, but I then benefit from better technology, basically. Absolutely.

**Lukas Henkel:** The modular approach is just great. I mean, of course, it also has some insights. You're always paying for interfaces that you wouldn't necessarily need, but the advantages, as you said, is just immense flexibility. That's also something I very much like about, I'm not sure if you know the framework laptop. So this is like the modular laptop concept and I just love that because you can just drop in another motherboard once your CPU is outdated and there is really no other manufacturer who can provide this level of flexibility.

**Chris Gammell:** Yeah, that's also at the truly drop-in level, right? Where it's not soldered down, it's at a connector level, right? Yeah, that's almost like a repairability and true ownership type of thing. That has a different flavor to me. That's less of like, oh crap, I'm lying down than it is like, I don't want to waste and like lap, you know, like there's nothing particularly fancy about my current laptop that I like, I wouldn't benefit from, you know, it's not like I have such a crazy spec on my current laptop that I wouldn't benefit from upgrading it later. Yeah. So the general compute idea definitely, yeah, it benefits at all. Yeah, that's all, you know, like that's, that's a, I think another thing too that you wouldn't think about but I would think about, right? I'm looking at this SIP and again, we'll have links in the show notes. This is just something I can't do. I mean like, or I can't do efficiently or it's not worth it for me to do it, you know, if I'm a consultant, it's not worth it for me to do it for my clients because the time to do that is just not realistic. You know, so that's why, you know, the CM4, the compute module 4 from Raspberry Pi as well, there's nothing special about the connectors on there, the capabilities, the interface out to the world but it's the, it's that kind of like IP, it's like an IP block that I'm basically dropping in.

**Lukas Henkel:** Yeah, exactly. It's a proven design. Yes. There's a large, a big community around that design as well so you have quite a lot of reference designs on how to actually use this kind of module and yeah, you're just saving a ton of work and also potential debugging work in case, you know, memory training between the SOC and the onboard memory fails. These things are very hard to debug and if you don't have the tools or not the time then yeah, probably, probably just get a SIM. Right. Makes life so much easier.

**Chris Gammell:** Yep. Why is the memory so big? What is the limiting factor on the memory here?

**Lukas Henkel:** So, this is actually EMCP module meaning there is both the memory and the storage integrated in one package. So we have Oh, interesting. 4 gigabytes of LPDDR4X and 64 gigabytes of MMC and it's just memory dice are large so it's really just the dice size in this package I would say the molding is like I don't know maybe 10 to 20% of the total volume the rest is just dice stacked on top of dice and so the only way to further miniaturize this design would be to stack the memory on top of the SOC. It's basically modules using modules

**Chris Gammell:** using modules you know exactly on this on that talk I gave I was a little embarrassed because I'm basically like I'm putting an RF module under an RF can right that's like my idea it's you know I'm midway through I'm not like actually doing it yet but like it's embarrassing to be like you know I can't do I'm not gonna do chip down design for a cellular module like it doesn't make sense for me but also I want to like shield the rest of the stuff from any crap that I put on a board but it's like it's always modules all the way down right it's like basically when you get down to the transistor level like it's we're always implementing on top of other people's modules it's just that cost like you mentioned of having interfaces having you know having additional abstraction for each individual level.

**Lukas Henkel:** Yeah absolutely I mean if you look at chip design it's the same story there you get your IO pad library transistor library from your fab or from whichever provider you are using you get those pre-manufactured IP blocks that you can drop in your design and in in this kind of scale there's really no no other way to approach it because so much work has gone into developing these these building blocks and if you would really like to do everything from scratch that would take would take years lifetime yeah

**Chris Gammell:** what about the so again I mentioned CM4 from Raspberry Pi one of the benefits there is that they have builds that are you know standard standard Debian builds for that sort of thing so then do you find that the community has already started targeting this IMX8 with like Yachto or build root style systems or how is that going to work?

**Lukas Henkel:** So yeah we will definitely be relying in part on the community to help us with the BSP but we also provide our own build on on board support package when we actually launch the module so that people have something that works out of the box that's definitely necessary tiny little box yeah tiny little box but yeah I mean one of the one of the unique selling points from Raspberry Pi is just the UHD community so a lot of people are working on implementing drivers for for their specific use case as well maybe not necessary drivers because there you need also some documentation of the SOC which is not available but the ecosystem is just so huge and the community support is so large that there's really a lot of a lot of things going on that would be very difficult to do for a small company yeah right so we're definitely relying somewhat on the on the community for the PyMix 8 as well at the moment there's not a lot of work going on but it's just because we haven't officially released the design files yet so we would we want to launch the crowd supply campaign first and after the campaign is successful we will then provide a GitHub link with the Altium files and also we will provide a keycard project so we convert the Altium design to a keycard so folks who are not using Altium can also work with the design but once that data is public we we hope to see also a lot of engagement from the community because we get a lot of requests at the moment and I'm also for people who are interested sharing those files even even now before we started the crowd supply campaign because a lot of people just want to get started they want to maybe even design a baseboard for the PyMix 8 or look into the firmware side of things and yeah so I expect to see a lot more community interaction once we actually published all the files

**Chris Gammell:** Okay great let's disambiguate a little bit here as well so you have your SIP the SIP has the same IMX 8 on it it has the memory on top we'll have photos of that that is in development the SIP is not going on the PyMix 8

**Lukas Henkel:** is that right? Yes that's right so the SIP being a very very small form factor we have our own product in mind for that that also requires this level of integration the PCB for the PyMix 8 is a little bit a little bit more low tech it's still an HGI design but it's not as expensive as the SIP and it also uses another processor so on the SIP we have the IMX 8 ULP which is the ultra low power variant of the IMX 8 lineup which is targeted specifically for wearable devices or IoT devices with very low energy consumption while the IMX 8 and plus that we are using on the PyMix 8 is catered more towards multimedia and compute hungry use cases tiny security camera versus

**Chris Gammell:** high end camera for example yeah yeah yeah yeah okay cool all right that's a good one and so now PyMix 8 you mentioned is a crowd supply campaign we'll have links to it that is launching in the next the project start launch sorry project launch on crowd supply will start weeks to months away three to four weeks from now yeah okay great probably two to three weeks from when this is posted and you can sign up now and then on crowd supply and then that'll be delivery rough time frame

**Lukas Henkel:** it depends so we have a few requests that we have to fulfill or that we want to fulfill first also as part of the crowd supply campaign but general availability will probably be either late December or early January next year

**Chris Gammell:** that's still pretty fast for a crowd supply campaign that's already like yeah

**Lukas Henkel:** you're already

**Chris Gammell:** well on the way so basically you're just kind of gathering numbers and ready to

**Lukas Henkel:** launch that thing yeah we have done this this project has been going on for quite some time now at some point we actually we started this project not even with the intention in mind of actually selling a Raspberry Pi compatible module so this project actually started as a part of the open source laptop project so we wanted to have a CPU module that we could drop into our open source laptop and in case our CPU module doesn't work we can still use the Raspberry Pi that was kind of behind that but yeah since we since we've gone public with our idea of using a CM4 module for our laptop people really yeah really really thought this was a great idea not only for the laptop but also as a standalone module and yeah we kind of developed this project into into the direction of a standalone of a standalone product

**Chris Gammell:** so then okay let's talk a little bit about the CM4 sorry the PyMX8 so the CM4 replacement module differentiation what are some of the differentiations that people would expect to see between CM4 versus your design

**Lukas Henkel:** yeah well in terms of features we pretty much tried to match what the Raspberry Pi has to offer so we have our own onboard Wi-Fi chipset the on-board Ethernet Phi standard memory standard EMMC we have some extra features on there for example we have SPI flash that will also contain a backup partition that the user can can edit freely which might be for which might be interesting for more mission critical in quote marks applications what we have on there is also a secure element if you're doing some sensitive stuff for example if you're using this kind of module for the designer for cash register you can use the secure element coupled with NFC controller to do a safe transaction which secure element do you use for that

**Chris Gammell:** is that like holding private keys and stuff like that or is that a secure element outside for the actual NFC stuff

**Lukas Henkel:** yeah it's a dedicated part we're using the SE 050 from NXP

**Speaker ?:** okay cool

**Lukas Henkel:** so it's interface over I2C with the SOC and the same I2C interface is also broken out on the CM4 connectors but other than that the features are pretty much the same in terms of which kind of interfaces you have available it's just the different CPU architecture and the open approach that really is the USP for our customers so that they have complete ownership over the design and can also use the for example advanced features for image processing that come with the iMix 8 processor

**Chris Gammell:** but you were also you're no longer targeting the Coral TPU I thought I saw that on there

**Lukas Henkel:** yeah so we have a footprint for the Coral TPU on there and we're also supporting this module still but we are currently integrating the Halo 8L deep learning accelerator but at this point we are not sure if this will be an open source design as well because well there are also some policies around the Halo chipsets it could be that this is just another version but either way both versions will have will have an HCI accelerator on board in addition of course to the internal HCI accelerator yeah sure sure yeah

**Chris Gammell:** yeah the Coral thing I wasn't sure about like I'd seen I had followed some of the Coral stuff over time and like I know that the I only know it because the tensor processing unit that's the T in the TPU but like I thought they were end of life in that as well I thought the Coral project was kind of maybe not long term

**Lukas Henkel:** yeah this is the thing when we started this project which was about three years ago things looked a little bit different at the moment of course the TPU was around for some time as well but there were still some new developments going on and a bit more active community engagement for this module as well and if I were to design the PyMix 8 now I probably wouldn't have chosen the Coral module so this is a little bit of a yeah just historic artifact but there

**Chris Gammell:** is still interest in the benefits of modularity right you can have multiple skews and you target different ones and then it's up to the firmware people to just make it work come on folks what's the hard stuff here it's just software yeah make people angry right okay yeah it's interesting and just in general for this kind of like offloaded edge processing like this this is for image streaming type stuff or just generally like machine learning type stuff on the edge what is in the general use case what is the problem you're trying to solve with something like that

**Lukas Henkel:** well honestly it started a bit with industrial and embedded vision use cases especially since the iMix 8 has been used for these kind of applications quite widely in the industry but since we've published our plans for the iMix 8 model we have gotten so many requests from places where we didn't think we would ever see an interest in this kind of module so we have people who would like to use this which is still somewhat expected for advertising monitors so how would you call it advertising panels that you hang in front of your smart science exactly yeah so we've got a lot of requests for those and then we have a lot of requests for niche products so these would be IoT projects that will be used for either smart city systems we also have IoT projects for monitoring for monitoring how would you say it so this is a camera system that will be used on mountain tops on snowy mountain tops in ski resorts and this could monitor for example how prone to avalanches the region is so this would be another vision use cases but it's got to be

**Chris Gammell:** battery power solar power it's got to be super sleepy and only detect just that one event and then go back to sleep sort of thing right

**Lukas Henkel:** exactly yeah so another request also we've received was to put this thing on a rocket also maybe another interesting project coming up but what I'm saying is at the moment we are not targeting a specific industry we are really just providing the tools and our customer choose what they want to use it for

**Chris Gammell:** just to go back to your business too as well so you're designing these things that are open source obviously you can reuse them in your own business but how much of your business is these kind of bespoke designed for hire type of applications versus making a product that is going to be purchasable and funded sort of thing

**Lukas Henkel:** so I would say the open source projects or our products are about 30 to 40% maybe of the company revenue or let's say company resources is a better term at the moment and the rest is really consulting and engineering services that we provide and this is another benefit I would say a side effect of these open source projects it's a great tool for marketing and advertising our services obviously I talk to a lot of

**Chris Gammell:** consultants on my consultant forum which I don't think you're on you should definitely join and you know it's always the same problem of like how am I going to promote my work I can't talk about my customer stuff it's tough right and then often full utilization especially for smaller consulting shops or individuals it's just like you want to be at full utilization you know 80-90% so then in that last 10% usually people are billing for their time or doing learning whatever it is a really good doing 30-40% of stuff that you can talk about and also utilize in your own work is a great you know I think that is a good target you know if you can do it so that's awesome

**Lukas Henkel:** yeah that was our idea but if you're already doing marketing we also want to be able to make some money out of that outside of just the marketing advantages and that's why we decided to go with the open source approach there we can generate some revenue by selling the modules but also have a nice side effect of just going out and showing what we're capable of

**Chris Gammell:** and you can make all those LinkedIn advertising bucks right I'm sure that no yeah they're not paying you for all those posts you do they should I look at them

**Lukas Henkel:** enough nice yeah well we do have also some marketing corporations going on oh good there's also an article series on the Altium resource pages for the PyMix 8 where you can take a look at how we approach the design of this module so yeah doing just doing a bit of public work or just work in the public domain really helps a small company to grow

**Chris Gammell:** Altium is smart and it seems like they are in this way I would be promoting the hell out of your work because the stuff that you're doing with these tools is really really impressive historically I found out before we started recording I knew that you were part of PCB Arts but you used to be in charge of the Twitter profile when I think I first started learning of PCB Arts so yeah I think I was first drawn to your work when you were in charge of the Twitter for PCB Arts as well that's okay so the marketing approach does work out that's great it does it does it worked it grabbed my eyeballs that's how I met Saber who we've had on the show as well that's your co-founder there and yeah I think it's I pretty much I think that seeing layout high density layout is pretty much always going to work for me so if I'm your target market it is working it is working Lucas

**Lukas Henkel:** nice I mean yeah most of the time it's engineers who decide who to hire for external consultancy engineering projects so that's always the thing if I'm looking at sometimes I'm also looking for freelancers if you have too much projects going on we still have to outsource some of our work as well and when I'm looking for freelancers I'm just looking for github projects I'm just looking for some reports on the social media channels to see what they're working on because I would like to really just see a few examples of what they're capable of and I found that two or not enough people are actually promoting their work by just showing what they are capable of and I understand it I mean most of the things are on the NDA but yeah it would be great to see a bit more open source work from those guys as well and I think it would very much benefit them as well in terms of acquiring new customers

**Chris Gammell:** yeah I agree I agree yeah other things that you showcase on your site as well is the same thing that we had that drew me to Katerina's posts with RF stuff was basically like these animated simulations and things like that like that also so Katerina does that with RF stuff you do that with signal integrity stuff and simulations and things like that I mean one thing that I was surprised with Katerina was that she said she doesn't usually use kind of that animation kind of style in an everyday context it's more of a thing that looks good in helping to highlight and educate but like less so on an everyday basis is it the same for you or is it more practical to have signal integrity kind of animations

**Lukas Henkel:** it depends I would say if you already know what you're doing then there's really no benefit in visualizing that because visualizing these kind of simulations is also quite time consuming but what I found especially when I started out with these kind of modeling approaches and yeah just digging deeper into the actual underlying physical processes it really helps you to understand what's going on and to get a feel for some of the problems you're dealing with and you have to do some kind of visualizations in order to develop this feel for the problem but once you have established this feeling then you sometimes don't even need to run the simulation because you can take a look at the layout and say well I know where the problem will be or I know there will be a problem and now you can you can basically jump over the first iteration loop and just start with a better approach from the get-go and maybe put a simulation top of that to further optimize it but you don't have to run those fancy animations every time because for me it's just really a tool of getting a feel for the underlying physical processes building

**Chris Gammell:** that intuition you have one post that will link in with FreeCAD and OpenEMS is that right? That's impressive I've used FreeCAD many times what about OpenEMS that as an open source tooling is sufficient for your regular needs or more of a demonstration in this case

**Lukas Henkel:** OpenEMS is a great tool and it's really sufficient for most of the stuff we're doing but and this is a problem that many open source tools have in common for some time now it really was difficult to use and really a hassle to set up that's also why I'm promoting this free card plug-in because it just streamlines the process very much and makes it much more accessible to people who aren't coders I would say because for example with OpenEMS you have to write either MATLAB code or interface it with a Python command line and for the everyday hardware engineer who just would like to know what the insertion loss for their traces that's not

**Chris Gammell:** really just tell me how to do it better is really what I want the tougher to tell me just be like fix my mistakes just tell me where I need to have a focus and I just need a DRC effectively for signal integrity to just be like you did this wrong Chris this is a bad

**Lukas Henkel:** idea exactly and that's the problem with many open source simulation tools they are written mostly by scientists so the focus isn't really on user experience or usability or just being able to efficiently integrate the tool in your everyday use in your day-to-day workflow but in this case this really is an option with the free cut plug-in and if you just want to simulate your antenna design or want to run some crosstalk simulations this is certainly possible with open EMS it's still a bit difficult in terms of the meshing so you still have to dig a bit into the background of the finite difference time domain simulation topic especially with the meshing that's used by open EMS but once you've done that then it's certainly a very usable and capable tool

**Chris Gammell:** so we had Sean Himel on the show talking he's doing free CAD classes I'll tell him to start doing some classes on that too some scripting on top and boom help the world you have some heat simulations as well with Blender so that's another one where I've seen Sommer I think his name is on LinkedIn he has a bunch of amazing Blender simulations this is a heat based one so is there specialization around doing heat mapping it's not heat mapping it's like heat flow it's like air flow it's like CFD what is that

**Lukas Henkel:** depends on what specific post you're referring to but we've done both static heat transfer simulation for example if you have an LDO on your PCB for example you can run a static heat transfer simulation to see how the heat dissipates in your PCB or just spreads in your PCB and then dissipates to the environment see how the neighboring components heat up and of course just calculate how hot the LDO will get in the end so this is something that you can do with Elmer for example which is also an open source simulation tool but you also can couple this with a CFD server so now you're modeling not only the heat transfer in the solid domain but you're also bridging the gap by transporting the heat in the fluid domain and see how natural convection for example transports away the thermal energy from a heating from a PCB or whatever and all of this kind of stuff you can then visualize in Blender so none of those simulations are done in Blender it's only the post processing got it so you

**Chris Gammell:** basically have like maps of like basically gradients that are calculated through time or something like that and then that's what gets put into Blender

**Lukas Henkel:** yes so there is this is

**Chris Gammell:** BVTK nodes you said in this post I just linked it in our

**Lukas Henkel:** this BVTK nodes plug-in can actually read the server output directly so there is an output format called .vtk which stands for the visual toolkit and this is a file format that many simulation tools use so in the file you have a representation of the geometry or better to say the simulation mesh which represents the geometry and with every node in the simulation mesh you have associated scalar fields vector fields tensor fields and all those fields can be extracted using BVTK nodes and you can map colors on those fields or you can assign graphs to see where the vector field is pointing and stuff like that all this is becoming possible through BVTK nodes by directly reading the output ! So this is a really great tool for these kind of scientific visualizations And

**Chris Gammell:** the VTK files the thing that's actually solving that that was built into Altium in your case or that was another third party like Python script type of thing

**Lukas Henkel:** So you you mean the solver that creates the VTK files That's right yeah exactly Yes so these are tools like OpenEMS for example so OpenEMS can also export these VTK files Elmer which I'm using for static key transfer and elasticity analysis and stuff like that can also export VTK Sorry

**Chris Gammell:** what was the name of that again Elmer

**Lukas Henkel:** Elmer Elmer it's called So this is a multi physics platform which can solve things like static key transfer static current conduction what else do we have quite a lot of quite a lot of solver modules in this package linear elasticity non-linear elasticity what else do we have in there It's really a plethora of solvers

**Speaker ?:** It's

**Lukas Henkel:** great It also has the bit of the bit of user experience problem that Open EMS had some time ago It is Elmer GUI but not all features are supported in the GUI so if you really want to dig deep and use all the features of Elmer you still have to use the command line interface I think Elmer

**Chris Gammell:** which is at elmerfem.org I think probably the most telling thing is when you go to their forums and it's the

**Lukas Henkel:** tool is great and very powerful but it's written by researchers primarily for researchers function over form

**Chris Gammell:** which is really how it should go that's super cool how do you know how to do this it seems like some of this is just the constraints over time too the complexity of the designs you've been explaining and you showcased but I've never needed any of this I am another smart person in the AFR I swear to God I keep finding

**Lukas Henkel:** you folks you're just talking to average show but I have I'm just very interested in this kind of topic

**Chris Gammell:** curiosity that's what gets you you know

**Lukas Henkel:** exactly I mean it's if someone really has a passion for their hobby they're always going to be I don't know one of the top performers in their field just because they're spending most of their free time with their specific subject and I mean for me it's a similar story this is really my hobby and I'm spending most of my time with this kind of stuff so I just accumulate knowledge over time and yeah there's not really a secret approach to this at least I don't I'm not aware of one unfortunately it's just yeah so I have some theories here

**Chris Gammell:** I've been I think folks like him and you and other you know CN Lore and other very driven smart people who just stick with it right I mean there's a lot of stick with it going through PHP forums learning how to script all this stuff whatever right that's

**Lukas Henkel:** true

**Chris Gammell:** yeah what is it I think some of it is got to be reward structure in your brain because like when I come up against some problem like ! what is that reward structure for you like when you solve something like this when you figure something out do you get a high from it?

**Lukas Henkel:** Honestly it's quite the opposite for me it's pretty annoying so I'm wired in such a way that once I encounter a problem I can't really let go even if I would like that sounds

**Chris Gammell:** familiar

**Lukas Henkel:** and also if there's more important stuff that I should tend to if there is still an unsolved problem I can't really let it go so it's not really a question of I want to do it well at the start of course it is because it's interesting but once I dig deep and hit some hurdles there's just now going back I to sort it out otherwise I won't be able to sleep quite literally

**Chris Gammell:** got it what's the annoying part is the drive to figure

**Lukas Henkel:** it out no the annoying part is just knowing that there are some other things that I have to take care of or knowing that what I'm doing right now is probably not the most important thing but yeah I just have to do it you can't stop it it's like an addiction to the problem

**Chris Gammell:** I know that feeling a little bit that makes me feel better about myself it's interesting that's good I'm going to keep developing this theory over time yeah yeah ulterior motive here of course as well is like how do I teach my kids to be driven in these interesting ways as well I don't know if you could teach it but there's very interesting output that's what I'm seeing yeah yeah I think you're solving cool problems

**Lukas Henkel:** for me actually how I got into this whole electronics field was I was I don't know how old I was probably nine or ten years and my father brought home a broken laser printer we tore it down and found a little high voltage power supply in there and the first time I've seen high voltage arcs I was really fixed because it just to me as a kid it seemed kind of magical that you could produce lightning in your home and that's how I started with the whole electronics side of things I then started to design my own flyback converters Tesla coils that's how it started but I think it was just the exposure to what's possible and to what's out there I just was fascinated by this specific topic but it could have been anything else as well it's just having the opportunity to find out what really suits you I think at an early age

**Chris Gammell:** is very important if I tell my kids anything it's to be curious that's all I care about honestly be curious about anything that's the important thing yeah okay so man I got a little off track there but there's a lot of other cool stuff here I'm not sure we're kind of running out of time but another question I wanted to ask generally is so like you're doing some you and your team are doing some really really high super high density stuff and so what are things that you've learned in this in working with this high density creation creation of boards are super high density that like are kind of gotchas that you know people could start thinking about as they start to dip more toes into the high density stuff and of course I'm asking from my own perspective so teach me Lucas

**Lukas Henkel:** honestly I would say if you're already into PCB design it's a relief if you can move up a technology class because you have so much more freedom in the PCB design process but you also have to kind of rewire your brain into more 2.5D or 3D thinking because if you're just using standard through vias for example you have to stack up of many layers and just connect to every layer once you place a via that's all fine and good and pretty easy to wrap your head around but when you're doing HDI design and trying to find out how you can optimize space in a specific area of the board you have to start thinking more about a 3D structure within the PCB because you're actually routing of course over separate layers you're not just dropping a via down the whole stack you can move within the stack you can now even start embedding components into the PCB and for me personally it really helped that I also have a little bit of background in CHD 3D design sorry CHD stands for what just like mechanical design with 3CUT for example got it

**Chris Gammell:** got it okay

**Lukas Henkel:** yeah so having this background in 3D design really helped me to get into this kind of HDI design because my brain was already wired in this kind of 3D space or 3D visualization way yeah

**Chris Gammell:** does Altium have when you visualize the 3D output component models and 3D models of those things is it possible to look at the stack up in 3D as well can you zoom in and hyperscale the stack up so you see that visualization as well

**Lukas Henkel:** yeah definitely in at least in Altium there is a feature to do that and I've also used that extensively once I started with the HDI design and it's the same with the simulation once you have developed a kind of intuition for this 3D visualization you had you don't need that functionality as often as in the beginning yeah I'm not sure if Keycut for example also provide these similar feature but it definitely started with HDI design there

**Chris Gammell:** is a stack up you can see the stacks if you zoom in in the 3D viewer in Keycat but I'm not sure about I'm not usually designing with HDI so blind and buried vias and stuff like that are just not usually on my plate and so I'm not sure how that gets visualized that's a good question I think I did that for the board I did a couple years ago but it's been a while since I've needed to do that density because most of the time I'm using modules so yeah yeah

**Lukas Henkel:** yeah yeah but that's definitely very helpful so if you have a way of visualizing the 3D stack up this definitely helps and I'm not sure maybe if there is not a built in feature in Keycat maybe it's possible to export the copper geometry and just take a look at the layout in a third party tool but yeah other than that I would say it's just trial and error just practice basically DRC is our friend it is our

**Chris Gammell:** teacher yeah exactly yeah absolutely what are the normal kind of layer ranges that you find yourself doing as well

**Lukas Henkel:** so we are not doing two layers or doubles sure yeah we're moving to four layers because most of the time it's just the more sensible solution well not in all cases but we are not like designing switch mode power supplies for TVs where you have a single layer board and just jumper wires on the second side so we're usually starting with four layer stack ups and the most layers we have done I think it was 18 layer and 18 layer stack up but most of the time we're hovering around I would say 6 to 10 layer board stack ups okay yeah

**Chris Gammell:** and like you said I mean like the costs have dropped precipitously it's really wild how much cheaper they are than they used to be absolutely yeah

**Lukas Henkel:** also for the SIP for example so this is a 10 layer PCB but it's in any layer design so there is a blind via or a laser wire between each layer so you can freely drop a via from any layer to whatever layer we like that's also where the name is coming from which gives you a lot of routing flexibility of course yeah totally this is quite a complex PCB to manufacture because now you have to now you have a lamination plating and drilling cycle between each layer that you're building up during the PCB manufacturing so the manufacturing cycle becomes really complex and yet still for the SIP if we are ordering 120 boards which is not much considering the size of the SIP so we can comfortably fit that on a A4 size sheet of paper and having 120 of those PCBs each board costs us around $10 and at the beginning I was expecting a much higher price tag but that's $50 to $100 yeah totally yeah but that's definitely doable also for the more advanced hobbyists I would say

**Chris Gammell:** yeah that's great so in that case in the any layer that is a laser for each via or is that

**Lukas Henkel:** and then they

**Chris Gammell:** backplate it so that the ones that aren't going through they cap it so that it doesn't go through for certain layers or they just leave

**Lukas Henkel:** it open so there is a laser via or laser vias only connect at least in most cases there's slight limitation aspect ratio but in most cases laser vias only connect between two layers so a laser via won't connect all the layers in the stack up it will only be between two layers and with the any layer stack up the laser vias are stacked on top of each other in case you want to connect a trace on the top layer to a trace on the bottom layer but there is not a single laser or drilling process that goes through the whole board stack up it's just individual drilling cycles for each layer pair

**Chris Gammell:** so if it's like an 8 layer board so like 1 through is from layer 2 to layer 8 but then the via next to it is going layer 2 to layer 4 2 to 8 would have layers all the way through layers 2 and 8 but they would be plated individually and then connected in the lamination process

**Lukas Henkel:** so there's also different ways in how to approach that you could either stack laser wires or stagger laser wires meaning that you can't this depends on the capabilities of the manufacturer some manufacturers don't like stacking laser vias on top of each other because it can decrease the yield during PCB manufacturing but yeah essentially you have to connect the vias together during the plating cycle in the manufacturing process and now for 8 layer board for example if you're using any layer stack up now you have let me think 5 plating cycles which just makes the board manufacturing expensive because you have to drill and plate the core

**Chris Gammell:** more electroplating all that stuff yeah exactly any board houses that you recommend for this these crazy processes you don't need to promote if you don't want to of course any that you

**Lukas Henkel:** really have had good experiences with we are working with Wirt Electronics for these kind of any layer stack ups and anything that is more high tech and high density I would definitely recommend checking them out got it and

**Chris Gammell:** they also make their own modules so I'm sure they're lending you some of their processes yeah

**Lukas Henkel:** they definitely know what you're doing and they can also help in figuring out what the right layer stack for your application might be as

**Speaker ?:** they

**Lukas Henkel:** have they have experience with this kind of stuff also from their own product so they are a really good resource also if you are not fully decided in which technology to use I

**Lukas Henkel:** to see which

**Speaker ?:** CPU

**Lukas Henkel:** vendor is actually willing to open source some part of their documentation so that we can use their CPU in our open source laptop but once that is sorted out we will also publish articles probably on the Altium resource

**Chris Gammell:** page for that cool all right well keep your eyes glued to the Altium blog and we'll have some links down below of course as well Lucas thank you for being here first off

**Lukas Henkel:** thank you very much for having

**Chris Gammell:** me yeah my pleasure and please continue to push out these great updates you're doing great marketing without even trying for all your capabilities and we all benefit from learning alongside you so I appreciate that a lot

**Lukas Henkel:** thank you very much we'll definitely keep doing that all right we'll see you soon

**Lukas Henkel:** thank you bye bye

**Speaker ?:** you you you ! Thank you. Thank you.
