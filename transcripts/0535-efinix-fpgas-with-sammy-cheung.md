---
episode: 535
title: Efinix FPGAs with Sammy Cheung
url: https://theamphour.com/535-efinix-fpgas-with-sammy-cheung/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released March 21st, 2021. Episode 535. FNX FPGAs with Sammy Chung. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Sammy Cheung:** Hi, this is Sammy Chung. I'm the CEO and co-founder of Affinates.

**Chris Gammell:** Hey, Sammy, how are you?

**Sammy Cheung:** Pretty good. Thank you. How about yourself?

**Chris Gammell:** Oh, I'm great. I'm excited to talk about FPGAs. I love talking about FPGAs on the show. Some of it because I have a lack of knowledge, and I love learning from experts such as yourself. And some of it just because I feel like FPGAs have been on the cusp of being that thing that's in everything for so long. And it feels like with FNX, it's like, yeah, we might be getting there. We're an FPGA in every device. Is that kind of the goal of FNX? Or how do you see FPGAs in the marketplace?

**Sammy Cheung:** Absolutely. You're right on. FPGA has been around, what, about 30 years plus? And it has been really a great niche market, but it has never been like a mainstream product like the application processes, microcontrollers. And what we are seeing today is what FNX brings on the table with our disruptive FPGA technology, we can become the mainstream product drivers. And we can see that in the next decades and next couple of decades, our device and technology will be everywhere. That's how we see it.

**Chris Gammell:** Yeah. I mean, and FNX is a relative youngster in the market. I mean, you haven't been around that long. So how did everything get started? Where did it, I mean, for a long time, it felt like there was only a couple of FPGA companies in the past couple of years. I feel with fabulous technology, it's possible to get more out there. But companies like yours are doing this interesting new model and new market. So what was the history of getting to where we are?

**Sammy Cheung:** From focusing on building products, we actually start more in 2017. But the company itself was originally started back in late 2012. 2012. So at that time, myself and my co-founder, business partner, Mr. Tony Ai, we came from an area where we both worked in a famous Altera in the past. And we felt like the industry never really grow big. And there's got to be a way to make the technology a lot more efficient, a lot more usable everywhere. So, and we believe at the time of our career, it's a good time to try something new, open up a new company and start to bring some idea and the technology to build something really from scratch. That's how we started. It was very simple-minded, very straightforward. I still remember the original goal Tony and I shared in some way that it's kind of like a curse that we understand the industry and the technology well. And it almost, even before we start, it's already telling us it's impossible to build a full-blown real FPGA business. So our original goal was really try to build a technology technology and work on a few licensed possibilities and expect it we will get acquired within a short period of time. So we work on it with less than 10 people. We really build up the software and early prototype devices. and we were really getting tractions from big companies wanting to license our technologies and go to the point to about 2015, we have multiple possible acquirers. I also know that there were deals on the table. But life never that smooth as what we would like, right? So

**Chris Gammell:** something happened

**Sammy Cheung:** and in that year Intel acquired Altera. At that time it was like pretty big shocking news. It was very clear that FPGA wasn't just a general purpose logic device. It's being used in data center. It's being used in the future for all the data processing. Now we understand for AI as well. So our potential acquirers because of that reason actually paused. So it was disappointed for us but we actually pushed us to go for a different path. So eventually I think we continue to sharpen our technology and there was a breakthrough in 2017. We actually caught investments from pretty big names. Interestingly one of the leading investors is Sainance. Everyone knows our number one leader in the industry.

**Chris Gammell:** Right. So a potential competitor is just like hey we'll help build you up for someday.

**Sammy Cheung:** yes. Yeah. I think that I had questions every week about why they were doing that and in parallel Samsung also invested in us that year together with yeah

**Chris Gammell:** that makes more sense though like Samsung I could see using your parts and you know being that could be a strategic thing like that but Xilinx is like oh okay

**Sammy Cheung:** I wouldn't interpret that there was never an exact reason for that but I really appreciate the opportunity Xilinx gave us I totally looking at it is a big vision thoughts very open mind thoughts about investing in a technology that they view has a strong potential but it's not surprising that I mean no one would thought this technology can evolve to build a full-blown product company within three years

**Chris Gammell:** yeah yeah if we could if we could take a quick step back too so I mean we say start an FPGA company but like how does one actually do that is it is it basically like hire a bunch of chip design I mean it sounds like Tony your co-founder as well he had a lot of architectural experience but is it basically like get a couple people together that know how to build like a chip cell and start to actually just then you just ship it off to a fab house or how does that actually go

**Sammy Cheung:** that's actually a lot more complicated than that and that's why FPGA is a business that very hard to penetrate and make it good I mean the first lowest level is really required the three pieces architecture software and the most crafty IC design so these three has to work concurrently cohesively to make the best products or technology so it doesn't some people come from ASIC world some people come from EDA world and if they try to work things sequentially the device that built in a probably like 2x3x bigger than the most capable FPGA so these are the three fundamentals and the software is not just like GUI or interface it's really the guts of the algorithmic placement and routing and fitting

**Chris Gammell:** right and the user experience too I mean I just think about my younger days working FPGA software and it's just like it comes in a lot of different flavors but a lot of it was just very slow and difficult to use so it's an important it's like the first thing your customer sees

**Sammy Cheung:** and it all starts with the technology and architecture and there's a term called fitting right so it all depends on how hard you can make your design fit and stuff into FPGA that's the first level and then the complexity arise right when you go up the second level now if you want to build a real chip you have to really understand how to integrate other intellectual property around your chips how to bring it to productions and then we need to build up an ecosystem for all the soft IP inside the core and then on the right hand side you have to build sales channel market it and then this kind of investment will kind of increase exponentially if we try to increase capacity and the most discouraging part for people who start FPGA business was you can build one product or one chip after that if you're a startup you probably spend most of the money you can't even build a second chip or not even think about building a second generation of products that's the killer for most of the startup companies tempted to get into FPGA right so the complexity is a lot higher well I think what F&N has done it's kind of broken a lot of old assumptions rules and as I mentioned that within less than three years we brought up a full-blown FPGA product family called Triont and it's all in production with only one less than one and a half years in full productions we sold over a million units even when we were crossing pandemic that's really impressive yeah so we are still doing something that people start thinking how did you do that what do you guys eat right so yeah

**Chris Gammell:** right yeah and so I mean you mentioned like a lot of startups it's tough to get to that second chip so do you find that the first generation has to be super targeted at a certain application space to try and like really find like a niche that is really well targeted or is it possible to make one that is more general purpose and then just hopefully you get enough traction and enough you build out enough user base so that people are like yeah we want more

**Sammy Cheung:** I think it's actually a trade off of both in our old days we have been building FPJ so long right we usually said all the FPJ are kitchen sink they basically you put all the features take two years to define take three years to build take three years to design so almost like only 10 years you get the revenue right so so that's why it's not growing so and on the other hand if we try to build a one solution market ASSP then you put a lot of pressure on your marketing your crystal ball right is it the real market you want to do right so I would say the answer is you get somewhere in between like for example for us right we are not going to be ASSP company because we didn't build from solution driven but on the other hand we have to pick a couple markets with the right intellectual properties and the right customer targets to start right so so for example we are try on currently is super successful in surrounding computer visions and also intelligent sensing so we are doing very well in industrial cameras all types of visual cameras which usually combine with integrating multiple sensing into the same platform

**Chris Gammell:** and is that because you have peripherals in there that might be more targeted like towards cameras and vision kind of high throughput kind of stuff

**Sammy Cheung:** yes I think the combination of having a MIPI interface and also have strong enough in terms of the memory bandwidth and also one critical thing is our technology because the newer applications in computer visions whether it's industrial or smart home they require a lot more logic elements to processing they are not a bridge device they want to do some low latency computing processing near the sensor and also emergently people would love to put a reconfigurable

**Sammy Cheung:** neural net small things not the big one or some inference function integrated with custom functions so they find it very handy especially they never saw a device like 120k le device in try-on that can fit in such a small package and also low power so and keep in mind it's not just one thing it's a combination of all low power small form factor a lot of logic elements and also we price it right for everyone so the camera guys love it I mean anything that doesn't need necessary camera right it could be a smart home equipment or things that with multiple sensors and they want a path to scale their processing and they like us so that's that's how we really started that way and I think we nailed it but on the other hand it's still an FPGA we sell it to many different things so not necessarily just computer vision right so that's kind of like a hybrid approach and but I could share with you the top customers are all someone playing with computer vision so

**Chris Gammell:** yeah ah interesting okay yeah I mean it sounds like what I heard from what you were saying there is it sounds like when an engineer is doing a trade-off analysis of like oh part size power how many logic cells I can get what is it's tough to do that comparison and if you're in the running there with having a lot of those in the green having the green cells on the Excel spreadsheet that's what I think about because I used to do those comparisons if you're lighting up a lot of those cells green and you're really winning in a lot of these things that alone is kind of like a product speaking for itself I think because sometimes if an engineer convinces themselves that oh I definitely need all these things and the try-on part offers it oh well there's the answer that's great

**Sammy Cheung:** you're right on Chris we never had the most splashy marketing things we did and we run it organically because we still have a much bigger story coming up which we talk about it later

**Chris Gammell:** yeah we

**Sammy Cheung:** never had the top influencers talk about that every day so but I think yes the device actually pulling the whole company and I think I'll co-ecionate this few tracks how our top customers use us they share the same traits they are big size companies but they are still driving very hard very still innovating they have a spec very hard to meet with ASIC nor traditional FPGA when they find us they say oh this is it so what that means is we win truly by the disruptive nature of the technology and the combination of the product definition and the story proliferates once you got the big guy using you the industry start knowing that and everyone say oh yeah I never saw this before now I should find a way to do things differently in the past I thought about FPGA it just for prototyping actually some of my smaller customers had a tough time working with FPGA because they need to innovate with FPGA but the price cost power would never allow them to survive so when they see us say oh yeah we can innovate with you guys so we should better now with the product pulling us together with focusing on more the leading innovating company but as time goes on I believe once everyone recognizes it so our name and how to use us will proliferate pretty fast right so

**Chris Gammell:** yeah well and you mentioned too the fact that a lot of your customers are using computer vision I mean that is that is an area of growth that's just not slowing down in the slightest it's just crazy how much that's going into a variety of products even outside of just an industrial camera type of thing but just putting vision into industrial uses or consumer uses things like that it's a really interesting growth area absolutely I think

**Sammy Cheung:** we arrived nothing like really like a grand planning 3-4 years ago we just arrived at the right time and right

**Chris Gammell:** you put the right IP in there and it's got all the bits and bobs that are needed and people are like yeah I can use that okay cool let's do this

**Sammy Cheung:** exactly but everyone knows that building ACET is astronomically difficult so when someone pick up a FPGA device which is very capable and we price it right and they can go to millions of unit production without a sweat so they will be putting their bet easily on us to use us and so we kind of changing the game quietly and but of course it won't be quiet in the next few years when more people start knowing about it so

**Chris Gammell:** right hopefully now the amp hours you can point to that and be like oh well that was the inflection point right there you know a bunch of engineers listening about it so you mentioned the technology like the underlying technology can you tell me about so this is I some of what you said like Tony and the architecture side of things but making it so that it could have many logic cells in such a small package size so what is it under the hood that actually allowed this to happen in

**Sammy Cheung:** the traditional technology basically everyone is using other than us they are more it is simple it's all about logic element and routing

**Speaker ?:** !

**Sammy Cheung:** I'm simplified ! built from a spatial perspective are two different pieces of hardware so in old architecture someone has to have a definitive count in terms of logic element and routing switch and the only way when they scale the technology to be more higher density is to make sure that the routing switch has the routability to cover it and that work very well during the days when I was in Altera is you shrink the technology you use hire software engineers to optimize 5-10% a year or two years to optimize the routing and you hire a great IC designer to make it 5-10% smaller here and there so then whoever execute well which turned to be Altera and Signing they won however you could see Altera and Signing both have been acquired by someone else right so clearly we could see they walk in the path building very expensive devices can only serve very expensive market which is data yeah

**Chris Gammell:** right yeah I think about those yeah servers and data centers and things like that it's just these like monster heat generators you know yeah

**Sammy Cheung:** they the technology force themselves into the market that they couldn't return to build something much smaller much more efficient much more low power and scalable so that's the key and in the industry there were a lot of peers trying to build something small but they more like trading off to make a bridge devices and as I said the main target market we are focusing on is really something high density but very low power very small package size and which actually coincides with this big super hype of edge computing right so that's what we are building so basically our technology the main difference is we have a cell defined called SLR cell basically someone can call it a fine grained architecture so this particular cell is very small relative to what is built in the standard FPGA and it can be reconfigured into either logic elements or routing so what that means is we can use software reconfiguration to determine routing based on customer design and then in the process of building the architecture and the implementation we very much could throw away 20 years of fat that built in the traditional architecture so the net net is get out of the gates we run in about half this area of what's the best in the industry and the best in the industry and then whoever second or third it's somewhat quite bigger than the best right so we are from an area perspective from the core it's very small

**Chris Gammell:** yeah so this is the XLR right the exchangeable logic and routing cell is that right exactly yeah so I'm looking at there's a spectrum article I'll link in for people to view there's a nice graphic in there kind of showing the crossover what actually allows you to do that to actually have the routing matrix and the logic element kind of be combined into one spot is it like a fundamentally different cell than before

**Sammy Cheung:** I think so yeah it's a fundamentally different cell I think the most important is not too much about hardware I think the thought process is really on the architecture and how to make the software work I think the hardware side always built from gates transistors and so on and configurable elements but the way the structure is the way how we organize is very clear very different from traditional so

**Chris Gammell:** there must be like a trade off though right so what is the actual trade off to having now signals being routed through a cell versus being routed elsewhere does it mean that you have fewer logic elements available if you have a more complicated routing

**Sammy Cheung:** not really and the reason is each of the cell it's a lot smaller than the traditional units as I mentioned part of it is ! we don't need to follow the 20 years accumulation of facts or rules that to build the traditional so we actually have we have many maybe given number we have a lot more SLR cells on the chip than what we quoted as logic element count so yes

**Chris Gammell:** oh okay yeah it's always like equivalent logic elements I feel like there's like this push to try and get like apples to apples comparisons between different FPGAs but it's always so tough to do

**Sammy Cheung:** exactly you got it so one of the things that people love to say that is oh yeah this architecture can make small and low cost but performance must be bad because you do this route through here this and that blah blah blah but they really didn't know exactly what we were doing right so for try on it because it's a 40 nanometer low power process it doesn't run like super high performance the performance is pretty decent it's probably the top in that low cost low power level but when someone start looking at titanium this year we already sampling right now the customer astonished so one of the customers told us that when they start trying to run getting the software and getting on the development kit is like are you guys serious I run my RISV processor on try on it's only 100 megahertz it's 400 megahertz now are you sure wow

**Chris Gammell:** yeah I don't believe the simulations anymore so are you guys is it some mistake in your

**Sammy Cheung:** timing model right

**Chris Gammell:** am I actually gonna see some weird bugs later or something like that

**Sammy Cheung:** right so so how so this is titanium yeah yeah this is correct we double check is correct and how big the size is that 60k LE device what three and half by three and half no way it's impossible so that's where we are getting out in the market right now the architecture actually doesn't have a performance problem it's just a choice when we pick a market in net

**Sammy Cheung:** I think we it's really a disruptive architecture it's not a trade off it's just a philosophical difference we believe if we can make things more efficient smaller we can get rid of a lot of fat that would that would hinder the performance in a different way when you make things simple you get rid of a lot of parasitic shorten the routing and making things a lot more efficient

**Chris Gammell:** the titanium that's the new one that's coming out so now you've gone from tryon that was three and a half years ago that was kind of your first offering you got to the second offering that's the titanium that's the one we're excited about that we

**Sammy Cheung:** I don't know how much we disclose yet but I I think I can tell I'm the CEO right yeah you're the boss man so you get to tell so so I I think this titanium we upgrade the architecture in a way that we did a lot of improvements in terms of connectivity and routings the fundamental concept is still the same SLR and also we adding

**Sammy Cheung:** the system performance quite a bit we classify as about 4x the performance improvement compared to tryon the fabric itself it's major juice up in terms of performance but the amazing part is we still can keep the area super small

**Chris Gammell:** yeah I mean we should talk about that too I mean there are some really small so we've talked about that on the show before but to just step back to the tryon real 0.4 millimeter pitch 3x3 BGA that's still it's a 49 ball BGA with 33 available IOs so that's still that's crazy tiny right

**Sammy Cheung:** we build those small devices and most of it is get to the market pretty easy and also can illustrate the trend that we see from the demand is the customers are looking for more than a bridge device they want to put some level of processing near the sensors near the data coming in

**Chris Gammell:** got it sorry can we define bridge device as well so how would you define bridge device

**Sammy Cheung:** so bridge device is for example they may be using a few thousand lookup table to just do some simple functions and they're more focusing on the IO the interface connecting device for example and AP is missing this IO

**Sammy Cheung:** was labeled in the past

**Chris Gammell:** right it's almost like a new version of a cpld at that point and using it that way

**Sammy Cheung:** exactly it's it's more like sometime in a mobile space or they build it as a patcher a few hundred million dollar business but it's come and go come and go right so they don't stick except cpld it's different because they're non voluctor so but for they wouldn't be easy to change to ASIC or start with ASIC and once they need to process more but they never had this kind of device before so I think we are still scratching the surface the market understand whoa this is different so as I said the trend and the situation favoring us when the world is still trying to find a perfect good solution for edge computing and everyone say they are doing that actually both Trion and titanium would be the best fit into most of the system I mean just a disclaimer we are not trying to build like some I mean our respected FPGA companies they the culture is tend to build everything themselves but we don't we want to focus on FPGA technology so we actually with that kind of small size we are seeing growing big companies want to partner with us micro controller company microprocessor company sensor company memory company they all seeing that pairing with us there's an advantage and they also see that they can just buy dye from us to build their own module products without really rebuilding a new chip

**Chris Gammell:** so they they're doing like a SIP or similar like a system in package type of thing exactly

**Sammy Cheung:** the simplest thing is just a SIP and I envision that for more high end in the future is what we call the chiplet

**Sammy Cheung:** but they are same thing they're multi chips to build a more complex module and system it it it it it it quite well too I mean it helping us a small company the old school is oh you you need to hire 100 people to build a sales channel and see what happens but now I think we are doing both our own sales channel but some of these companies are very big companies they don't sell FPGA but they package us together say maybe selling I cannot tell exactly but they may sell intelligent sensors with an FPGA behind the sensor that you don't know so yeah

**Chris Gammell:** right exactly right it's like this sensor is reconfigurable ! How do they do that?

**Sammy Cheung:** Exactly so every sensor they sell we have our own FPGA so they are our channel they are our partner so frankly they couldn't package up the old traditional FPGA either is too big too expensive too power hungry or they are too small in larger density that doesn't serve the purpose so now they find something rich especially titanium and going forward right they I think a lot of people jumping on a ship right now so

**Chris Gammell:** does that mean that so the small like chiplet style where you're selling raw silicon to someone else who might be putting it into a ! a sensor package does that mean that the the Trion or more specifically the titanium now does that do you have like a simplified power setup as well because I just one thing I was thinking about with FPGAs is very complex bring up of power rails tracked power rails as they come up that sort of thing and I imagine that if that was pulled into a sensor package that could be very complex so what does the power look like on power bring up

**Sammy Cheung:** I think the power bring up is a lot more straightforward when compared to what you kind of perceive the reason is the device with very complex power rail was more the I would say the last 10 15 years when FPGA company the big leaders try to do everything themselves so they stuff in a lot of different power rail different system onto because they make money out of building chips but for us as I mentioned we are small we don't go that route simply because it's not economical so we make our device simple to interface so even with titanium it would be very straightforward to be integrated with other people's components so essentially we have a lot more friends than enemy ! so we can call ourselves a companion device coprocessor but I think the real name is really in this new era is a reconfigurable ! accelerator we can accelerate the sensor applications and usage being reconfigurable ! Micro processor application processor would love to see us expand their feature sets without keeping out expensive masks that is really time to market and we can sit right next to storage memory to make intelligent memory so I can see there's variety combination applications can evolve and put on top of it and specifically it kind of jumped into a couple areas that is pretty significant what I see is especially titanium it's security and also how we deploy the whole combinations of technology and ecosystem into automotive as well so those are some of the areas we are pretty excited when we can see that our device A is we don't need to carry the burden of our traditional FPGA company we need to build everything ourselves

**Chris Gammell:** yeah

**Sammy Cheung:** B we find a lot of friends and we can build a lot of open a lot of market in parallel with different companies and pretty much they drive the market they find ourselves useful and what we need to do is continue to make our architecture more sophisticated and continue to push our technology nodes and of course improve our software usability and ecosystem so that's how I can see that it's going to be a franchise that it's going to last for decades so yeah

**Chris Gammell:** that's great that's good to have that long term view too I think that sort of thing helps to give some confidence when instead of like I've had vendors talk to me before they're like oh I've got this hot new product and it fits all your needs I'm like yeah it really does and they're like yeah and we're doing all this other stuff and then that company is gone in a year and I'm like oh wow whoops shouldn't have designed that one in you know I didn't design that one in luckily in my past but that's always a risk with the hump you have to get over as the CEO of a smaller company to convince people that this is a thing ! I

**Sammy Cheung:** couldn't even make a second chip but in trial we actually tip out it's public people can figure we have four different mass sets tip out

**Chris Gammell:** now

**Sammy Cheung:** titanium is 16 nanometer I had an analyst talk to me earlier last year I believe he cannot believe in that no way people couldn't jump into next generations and not even talk about financing hundreds of it and to do that that's what we were told by the FPGA company no I spent very little amount of money that's

**Chris Gammell:** great building on a budget huh

**Sammy Cheung:** exactly but I think it's inevitable that we are at the stage that we need to grow very fast very big and that's probably the challenge for us as I said we know so much back in Altera I sort of crossing space running hundreds of people organization building stuff from scratch so I know what it takes to build it up but right now I think we are kind of put our mentality the whole company is really enjoying enjoying what we see I want to share a little bit about our feeling or my feeling right so someone asked me what do I feel about being a startup CEO I told them I kind of feel like a 15 years old boy so you know why I explain to them that I mean the biggest challenge for me is how to keep ! our patience ! not go and

**Chris Gammell:** chase every new thing not dive into every exciting nook and cranny of the industry I

**Sammy Cheung:** try to use baseball as an analogy I kind of like a 15 years old young man knowing that I can throw in average 100 miles per hour fastball and my power speed is 110 I

**Chris Gammell:** I

**Sammy Cheung:** am 15 years old I am very eager to let the world know I can do that but the problem is if you don't prepare yourself to condition yourself well to hang out with the right people to sign up with the right team your career can be over in one year right

**Chris Gammell:** yeah right you'll burn out

**Sammy Cheung:** your arm

**Chris Gammell:** exactly that's

**Sammy Cheung:** what we are building right now is to make sure short term temptations like for example a lot of companies would say why don't we just go after the low end guy they are easy to bid up and compete with them no that's that's not because they are good at that we may lose to them so I think we really want to target at a market that it was missed by the big guys in the last decade and combining with AI and edge computing we have bright futures

**Chris Gammell:** yeah I think some of the features that you have on the titanium as well I feel like that you know like if you talk about setting yourself apart you mentioned you don't want to chase the low end you don't want to do it on price I as

**Chris Gammell:** you build up this as you build up the family there's like DSP blocks PLLs of course GPIOs high speed IO I assume that's like CERTA style DDR4 controllers ! MIPI stuff inside PCI Express 234 lane and then Gigabit Ethernet all all internal actually to the part too so you start to reduce part costs it feels like you know external that maybe in an old FPGA

**Sammy Cheung:** absolutely in some way that we kind of have the advantage sort of sit behind a market evolution and we have all these features built up essentially in the simplest way is when the density scale up the intercontinent complexity increase and also we would pick based on of course the market direction on some of the important features we harden them in the IO side periphery but at the same time in titanium we want to point out a few things and we still try to make the IO in a manageable flexibility we supply multiple standards in terms of like the service side in titanium and then same thing for the for the DDR itself is can support low power DDR 3 4 and and multiple different choices

**Chris Gammell:** we

**Sammy Cheung:** maintain a good level of flexibility and try to avoid being kitchen sink so that's how we try to draw the line but on the other hand you mentioned about embedded memory and DSP those are not the good old simple multipliers

**Chris Gammell:** not just like a Mac block kind of thing or like a multiplier accumulate

**Sammy Cheung:** it's combination of that as a basis but it is very well in terms of tailored from some of the embedded AI applications I mean we are not building ASIC chip but the main point for using our fabric DSP structure and embedded memory and to build embedded AI or embedded deep neural net

**Sammy Cheung:** accessibility in terms of building the varieties of choices of neural nets DSP is very fracturable in terms of the nature so those are some of the things that we actually I believe we haven't disclosed I need to be careful secret

**Chris Gammell:** stuff I

**Sammy Cheung:** think we probably will talk about more starting in April so the DSP functions and memory is very powerful imagine they are specially designed in a way that it works really well with our proprietary SLR architecture on the side so all these things what we are offering is really a great three in one it's still an FPGA you can do general purpose custom logic on the other hand you can embed a reconfigurable neural net implementation and on the same chip you can do the data path low latency computing processing so we're still doing FPGA but it's just disruptive in the nature that no one see you can make it so small make it so low power can exist in different package and also with good choices of IO in the content so we make it simple how

**Chris Gammell:** does an engineer go and actually so you mentioned we keep talking about vision here and there's some secret sauce in the DSP blocks as well what would an engineer need to do to target that are there actual specific vision packages or is it basically hook up a camera through the MIPI interface and there's some configurator or something in the software that allows you to target those DSP blocks

**Sammy Cheung:** yes I think they are in the FPGA world they're pretty standard way to design into the DSP block it's kind of different that we are going to provide and work with our partners to surface it not need to wait but on the other hand we are actively building up what we call the soft IP offerings for our customers so most of the cases we see two different customers one type is like some of the big companies they have very strong FPGA IP people they mostly they have all the IP themselves so what we need to do

**Speaker ?:** is

**Chris Gammell:** more

**Sammy Cheung:** add the applications therefore to help them to convert their IP onto our device which the good news is we are still fundamentally an FPGA architecture by the look so it doesn't take it's not very hard efforts to porting over to our technology in that case imagine someone invent a new AI chip of totally different things it's much harder to map technology into those kind of technology

**Chris Gammell:** yes switching costs are always high regardless anytime you switch a chip I feel like it's tough but then when there's specialized blocks if someone's targeting a specific function in a specialized block that some vendor might have then you have to go and retranslate it to a new vendor exactly

**Sammy Cheung:** so we're a small company absolutely from a tools IP ecosystem is very far away compared to Sign-Ins and Intel Altura but we are driving very well very focused on making sure soft IP offerings to make it easier to use for customers who don't have a large or high FPGA design team and so that's what we are working very hard on right now because we know that titanium is the complexity a lot higher than try-on so the soft IP offering which when I say soft IP it coverings all the way let's say the MIPI interface coming the MIPI interface coming to different customers may want different standards to work with the MIPI interface same thing for the working around the DSP block and embedded memory we have the plan right now to offer some very standard examples in how to use those blocks together easily and also it's very important to mention that we didn't talk too much about in this talk is we have the soft RISC-V offering on our chip which was extremely successful in try-on and our approach is very straightforward is we absolutely leverage a very credible there's no secret we start with leveraging an open source RISC-V platform working with them and we make it a standard offering as a template and we also make it look like a SOC template in a way that it's much easier for a lot of general customers you just pick it up and use it they can use the template SOC template as they can modify if they like

**Chris Gammell:** I'm curious about that decision from a business perspective too some vendors also have a soft IP block that is a processor RISC-V is hugely growing and I love that but a lot of times they'll still offer an ARM offering I'm curious when customers come to you are some like well we really want to put ARM in there do you have ARM offering

**Chris Gammell:** Is Power I guess Power PC opened up a little bit more recently but what's your view from the top seeing what customers are asking for

**Sammy Cheung:** I think that RISC-V clearly carrying a big hype in the market space and also for affinates in what we call our own offerings is RISC-V because it's easier much easier for us to access and develop the template and the platform but I think the key word is still need to come back to you can see from our website the gut of the template is actually what we call the quantum accelerators so and remember quantum is our marketing name for our technology accelerators means we make our fabric as accelerator to set up next to a RISC-V processor having said that I need to be careful because the reality is our technology is agnostic to processors got it

**Chris Gammell:** okay yeah I mean it's any kind of generic fabric like FPGA fabric you could put any processor you define in Verilog or VHDL you could instantiate right but it's more about buying when you're buying someone else's stuff or you're using open source or open ISA type things then it's a better starting place better tested exactly

**Sammy Cheung:** so what we see at least in the next five years I know for sure that probably we'll have other processor offering not necessarily we have time to build all of them but I can see that some of these processor companies are very willing to port their processor onto our quantum accelerators on top of it I think our philosophy is not trying to build mixing up the same chip with some kind of generic hard wire processor subsystem the main reason is if you look at titanium if someone optimizes well you can run processor at 400-500 megahertz so you don't necessarily build a hard wire system especially when you have so much more logic gates in the same area so but our focus is actually encourage partner or potential customers look into what we call domain specific soc so that's the area it's like if someone really really pushing for much high performance but they need FPGA technology they can work with us by either two chip or single chip to put their subsystem domain specific subsystem design and merge it together into single product offering so those are not that complicated it's only because it's a much bigger investment so from a company perspective we currently focus mostly on a soft core approach especially Titanium when we see it can run 400-500 megahertz it's probably more than enough to serve the market we are targeting that

**Chris Gammell:** I can see it it feels like it's another tool in the toolbox you have firmware engineers you have software engineers you want to be able to instantiate a Linux system or maybe a low-level real-time operating system just something to handle with traditional firmware it makes sense to have a targetable RISC-V processor I am curious the one you chose was by Charles Papon they won a contest in the soft CPU contest in 2018 that's really interesting that it's like oh win a contest become the chosen core that targets an FPGA that's really cool

**Sammy Cheung:** yeah I think so I think it's all about timing we are very grateful that we met up with Charles and we find a time and find that it's interesting to work together I mean we still of course I mean majority of the things we still put in back to GitHub and open source as I said we are not trying to take it too proprietary and quantum accelerator is still very much agnostic I'm kind of not surprised in these next few years some people may take the concept to build their own camp master as you are aware RISC-V have custom instructions and if you blend it with quantum accelerators you can produce up quite a bit in the system performance

**Chris Gammell:** right you just call a feature that's just like process visual frame or something equivalent it's just like oh yeah just go do that thing

**Sammy Cheung:** yes exactly so actually will be serving well with this embedded processor software market and especially they are more and more pushing upstream not just software but all this algorithmic design so this is a very important gateway to allow more and more innovation to be able to use FPGA but once again we are not signings or intel we we don't have plan to build like very fancy EDA tools we believe in making the workflow very simple straightforward and it's inevitable in some part of the workflow to design in will require good engineers to build up certain things but I think we are trying our best to make it very straightforward to allow varieties of innovators from all the way from RTL designers to software designers all the way up I think right now the hardest is how to enable the AI developer when they start their AI projects or if they need an edge device how they can make that decision ! to make them easier

**Chris Gammell:** to

**Sammy Cheung:** neutral in this area if you talk to some hardcore traditional FPGA guy this is not going to work

**Chris Gammell:** I had that feedback before too and I was surprised by it at first because I was so excited about the open toolchain stuff and they just go that's not for me I

**Sammy Cheung:** think the combination of it is I would agree 50% of it is true it is totally not practical when you start as I said if you just want to build something you can build it but if

**Sammy Cheung:** want to build something super competitive you have to harness both hardware software and architecture concurrently to build something good that's where the core is so that is hard

**Chris Gammell:** it it is almost like a vertical integration kind of piece where you need to really focus in on something you want to have that direct control of the whole stack it

**Sammy Cheung:** would be totally inefficient I understand the spirit but it's totally inefficient people may spend 20 years to build something totally inefficient ! But anyway I try to in the middle

**Sammy Cheung:** One of the innovations that we have people may not be aware actually it's patented it's our interface designer set up in our tools I have to be careful I haven't talked to my software guru Jay is this actually

**Chris Gammell:** out yet no no the patent

**Sammy Cheung:** is there it's in our tools our tools look different from standard FPGA because of the interface designer we got a lot of complaints saying how come you didn't make the tools looking like Vivado or quarters it's hard but anyway there was a reason for that because Jay is our software guru without him we couldn't build evidence one

**Sammy Cheung:** of key thing is we are not building traditional FPGA we are building a technology that want more and more things to interact with our core so the concept interface design is to separate the core away from the periphery and potentially anything attached and talking to our core can use this piece of software to talk to the core and not now but clearly that we envision some of our customers and I don't know if you we also have business people license our technology which is public information our investors Samsung we have built something very successful on 10 nanometer it's on our it's a public so I can talk about it so but the role of interface designer is a choice that is a piece of software currently we use to harness the I.O. interface for defining the settings and so on but clearly this piece of software is very expandable in the future not jumping into open source yet but I think this is something that if our customers decide to build a hybrid devices whether two chips one chip and find itself useful we are more than willing to license to code to

**Sammy Cheung:** them so

**Chris Gammell:** I

**Sammy Cheung:** think that is more pragmatic way we think about start democratizing this kind of offerings

**Chris Gammell:** yeah I was wondering about that because you mentioned being integrated to a SIP or something and say okay it's reconfigurable ! you need to have the tool chain so someone can go and reconfigure that and make it useful but

**Sammy Cheung:** we already pre-built this for our usage for our interface this technology clearly can be a great technology when someone tries to bridge another AI chip together with our TI 375 if they find it useful they can choose to license from us or buy the part from us we can open to them so that part of it is a technology in old school everyone to keep it in the closet so when no one can use it but the way in

**Chris Gammell:** the old days they would have charged you a lot of money it would be a hundred thousand dollar seat for it as well

**Sammy Cheung:** now it is more like if more people know how to use as I mentioned that my channel my ecosystem is different and I can see a lot of microprocessor company or people even building ASIC they may want to early to decide to pair with our FPGA together as a product so they may as well to offer a piece of software outside that can work with their system so jump in the talk about this is kind of open source but it's kind of a trend that we allow more people can use the core technology yes I mean but clearly in the industry a lot of folks would envision or imagine that let me I think it more belongs to the group that FPGA architecture never changed why not just open source it but they didn't realize that someone has already changed the core itself it's a lot more sophisticated but open up the interface be able to talk to our core I think it's just a matter of time so yeah

**Chris Gammell:** the way I think about it too is when I think about a graphics card getting integrated into Linux usually the leading edge graphics card you need some kind of special software to work with it just because it is it's got special features that are not just standard yet and then over time it's possible that gets pulled upstream maybe in open source it's not going to be leading edge but yeah it does some of the older stuff gets pulled in so maybe it'll operate in a similar way but I think what I hear you saying is that because it's leading edge it has the specialized tools that are required to get the interesting things happening within the the chipset

**Sammy Cheung:** exactly exactly I can see the trend but I see in stages and adoption and also one thing is we are just too small company to try to make anything open up to be successful so when we this discussion it was three years later I think we'll have a different look but the goal is going back to the first thing we talked about I mean we believe that with this disruptive technology with the timing with arrival of edge computing slash AI we really see a trend that evidence technology can be everywhere so

**Chris Gammell:** yeah that's great that's great are there any interesting applications that people don't see coming that you're like oh they should keep an eye on this one do you see anything on the horizon that might be bleeding edge that we're just not thinking about yet so maybe even vision being used for something that's unexpected

**Sammy Cheung:** actually I have the answer I almost kept coming out from my mouth but I suddenly say I shouldn't tell my competitor about that because competitors are good because they have the marketing they have a channel they can build something not the best but they can still sell right so I think let's take a battle that we are not in everyone in then it's easier I cannot tell the other one because I don't think they're good at that one yet so but I don't want to tell them but let's take automotive

**Chris Gammell:** I

**Sammy Cheung:** mean automotive is going to be truly explosive market the reason is simple I mean everyone knows that I mean yeah it's autonomous car ADAS and all this technology and a lot of sensors I think if you look at from a computing standpoint this is a moving supercomputer right yeah

**Chris Gammell:** yeah

**Sammy Cheung:** and also a can be a live advertising machine I mean your life spending in a car doesn't matter it's a small car big car bus whatever moving I think there would be a new architecture and mostly has to work with very strong software infrastructure and service yeah so when you start looking at that cost efficiency real-time computing is important

**Chris Gammell:** I could see the reconfigurability being very important too thinking about like you know GM putting out a car tomorrow that might have a chip in it but it's being expected to last for 15 years it's like okay well 15 years from now you know like car components might hold up but if the vision is still the same old pokey vision from 15 years ago it's like oh well we want to actually update the vision that might be on board or the algorithms that are actually controlling things and having that reconfigurable nature might give it more lifespan than it would have otherwise

**Sammy Cheung:** exactly and normal wisdom is in the short term just build another chip as long as you have enough money you extremely useful once again not saying that we can build the best AI or application processor or NVIDIA chip no we are not but we could see that within a car there are so many places would require very flexible reconfigurable near data computing accelerator that's where the area is important but hey the area of FPGA doing that I guess the problem is under limited space you think a car is big right but the cost and the space and thermal is crazily critical right a lot of thermal budget may already burn by some critical chips or other things right so I think we have a play in different spaces different places in the car I don't think today's car is already the car for the next 23 years I think there's a lot of innovation within automotive areas still to be seen so the market is actually not a short-term startup it's not a good market because it takes years to qualify to be and so on but I think we already burned a couple years and we have an automotive offering starting this year titanium is perfect for that market so I see that

**Chris Gammell:** pre qualified for the temp ranges and stuff like that

**Sammy Cheung:** exactly yeah as I mentioned there are multiple things that titanium is defined perfectly so I don't worry to mention because I still think there are areas in the auto industry that will have so much innovations that this is the next big market we are growing into on top of our early success in industrial and consumer market

**Chris Gammell:** that's great so you mentioned titanium is on the way to market right now you're in pre sampling and things like that when is the general public going to see these I was going to point people towards your dev kits page people can get hands on with the try on parts what about the titanium that we've been talking about here

**Sammy Cheung:** I start thinking I'm leaking something here as we speak we are receiving POs from customers and try to get development kits the development kit is in the manufacturing right now we already get a number of them to show customers so

**Chris Gammell:** are you held up just like everyone else because of all the supply chain shortage stuff it's like you can't get the crystal you need to build the dev kits

**Sammy Cheung:** we are probably okay we dodged around a few bullets in that problem it's been a mess

**Chris Gammell:** right

**Sammy Cheung:** so I think the Q2 we have multiple events worldwide that doing more disclosing about the titanium product and we took an approach more we have over 50 customers waiting for the device and some of them looking at it but we are still a small company so we are trying very fast to prioritize and it's early sampling so there are things that we need some hand-holding but we're looking at summer as where the production will start then the exciting part is our next device will come up also in early fall or something in Q4

**Chris Gammell:** and like another like a third version that we haven't talked about yet

**Sammy Cheung:** basically today we have the first little brother TI-60 which is a very small one 3.5 3.5 millimeter square which everyone can use it so we just open up a big adoption but then the next one it's I will let the press release in April to talk about it so we basically will get most of the family members to be more ready either production or sample by mid next year these two years our development pipelines are filled up already so

**Chris Gammell:** yeah I guess I didn't really think about that of like yeah you don't just release a whole family once there's actually individual chips in there you have to qualify and make sure each one's working as expected and as

**Sammy Cheung:** I mentioned the challenge and somewhat we are enjoying it is we very much try to build an FPGA business you're doing so many things right so we are trying our best to pipeline each of the steps and so that we can roll our products develop an ecosystem and open up channels that's what we enjoy but nothing close to my old company experience as I said the old company may do these things over the next five years rather than the next two years right so with 10 more people so that's what we are trying to do it's kind of silly but I very grateful our team members is kind of enjoying that right so

**Chris Gammell:** yeah I mean it's like that scrappy startup you know like the you know fight the good fight and getting cool hardware out there that's like the exciting part of it all I think that's really great

**Sammy Cheung:** exactly so but our challenge is not technology our challenge is not financial we get great sub investors our challenge right now is actually how we turn a very organic company that people enjoying that kind of flexibility to a much bigger organization I mean if a company scale you have to start putting in more process system but how to make that change without like suddenly break the key ingredients of the company right so that's where we are working on yeah

**Chris Gammell:** yeah company culture I think what Richard Branson talks about like every time you go from like 3 to 10 like 3 to 10 10 to 30 30 to 100 like each time it's like a whole new company basically or something like that and then it just it keeps scaling like that and you have to just try and maintain

**Chris Gammell:** your culture and keep that scrappy mentality and so you don't change what your customers are thinking about

**Sammy Cheung:** exactly that's I think that's fascinating and we try to work on it I don't think there's a perfect solution but I still going back is let's focus on our own people our own culture and my job is not trying to put a fixed formula on everyone my job is try to see what I can get the best out of each one

**Chris Gammell:** and

**Sammy Cheung:** push forward it's still very much people oriented I mean startup is still very much people oriented !

**Chris Gammell:** I think

**Sammy Cheung:** websites and also we are pretty talkative on LinkedIn I think these are the two venues that we see a lot of followers I believe that we will be a lot more visible this year in terms of in different publications stories and so on but I think the best way to learn more about us is getting a website if you are developers with great ideas or have FPGA experience either and also just click in the website and find out how to get a development kit and start looking into that and you will find something very different from what was in the past we try to build FPGA not just for a couple companies but I think a lot of people can take advantage of this breakthrough in the industry and we count on everyone to bring it alive so yeah

**Chris Gammell:** awesome well thanks for sharing about this Sammy I think you're a great spokesperson and you're very passionate about this and it was really great hearing about where you see FNX and the FPGA industry going so I appreciate you joining us today

**Sammy Cheung:** thank you so much for the opportunity thank you

**Chris Gammell:** by joining the crowd and the discord channel at patreon.com slash the amp hour
