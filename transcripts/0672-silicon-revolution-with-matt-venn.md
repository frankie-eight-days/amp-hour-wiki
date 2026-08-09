---
episode: 672
title: Silicon Revolution with Matt Venn
url: https://theamphour.com/672-silicon-revolution-with-matt-venn/
---

**Matt Venn:** This is The Amp Hour Podcast. Released June 30th, 2024. Episode 672. Silicon Revolution with Matt Venn.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Matt Venn:** And I'm Matt Venn of the Zero to Asic course, Tiny Tape Out and Yosis HQ. Welcome back, Matt. How are you doing? Yeah, I'm doing well, thanks, Chris. How's it going with you?

**Chris Gammell:** Good. You know, I've been watching with fascination as you continue to just crank stuff out and your community crank stuff out and the Silicon Revolution is here, I think. Is that a fair assumption?

**Matt Venn:** I'm just waiting for my silicon 3D printer from Sam's Aloof and I'll be set. Yeah, yeah. Oh, yeah. Atomic something? Just Atomic.

**Chris Gammell:** Atomic Semi, yeah. Yeah, yep. Well, we'll see. Yeah. I've been trying to get Sam back on too. So in the meantime, I think you're still using traditional, just the good old, the old ways, the best ways, huh?

**Matt Venn:** Yeah, the well-established, send it off to a factory, wait six to nine months and then hope it works.

**Chris Gammell:** That is pretty wild that it's still six to nine months, but I mean, I get it. I mean, I've seen how it works. I know the economics of it all, but that's a long design cycle.

**Matt Venn:** Yeah. A fab like Global Foundries would do a turn in like three months.

**Chris Gammell:** Right. And if they already have the mass set, like the actual manufacturing could be less, right? If they're moving towards volume, they could get down to like a month, maybe.

**Matt Venn:** But I think, yeah, I think it's still longer than that because it's just a very deep pipeline. Yeah, 300 plus steps. Yeah.

**Chris Gammell:** Yeah, exactly. Yeah. And just like capacity issues and all that stuff.

**Matt Venn:** Yeah.

**Chris Gammell:** I think, yeah, I think Samsung, when I was there, they were down to like 35 day turns, but then that was just to like, just have a wafer. And that's not, that's not where you stop, right? I mean, you actually get, you're getting packaged chips that are tested.

**Matt Venn:** Tested? Yeah. Yeah. The wafers have to be diced and then picked and then packaged and then they send them to me and then we send them on to the contract manufacturer. Then they get warehoused and then sent out to the customers.

**Chris Gammell:** Yeah, that's a long cycle for sure. That's, that's very impressive. So you've, you were back on in January of 23. We're going to talk, that was episode 616. Obviously we'll, we'll link that in. And Matt has once again, I think I mentioned this in the last episode, Matt has sent gobs of links, which is very, very much appreciated. He, this guy, if you're worried that Matt Venn is not organized with your chip stuff, you should, you should put your mind at ease because he's very organized. That's not what other people say. Okay. All right. Well, you know, no, no one's going to be happy every time, but yeah. What has been happening? So where were we, I guess we're, paint a picture for us where we were in 23, January 23. That was 18 months ago.

**Matt Venn:** Yeah. So we just sent off Tiny Tape Out 2. That was the big news. So Tiny Tape Out 1 was basically a minimum viable product with a MailChimp signup page in a Google form. And that was it. But it went, we had maybe 150 people submit designs. It turned out to be a lot of work because it was so kind of hanging together by loose threads.

**Chris Gammell:** Can you remind people what Tiny Tape Out is as well? We've definitely mentioned it on the show outside of the thing.

**Matt Venn:** I think it's fair to say that everybody knows what Tiny Tape Out is by this stage.

**Chris Gammell:** You never know, Matt. We have so many new listeners just, you know, they're just rushing the exit, they're rushing the entrance, you know, like they just want to get here.

**Matt Venn:** Yeah. Okay. So if you're a big firm, then you design a chip and you tile as many of them as you can across a reticle, which is the mask used to project onto the wafers. And then those are stepped across an entire wafer. And then the wafers diced and you get however many chips you get off a wafer. So if it's a small chip, like an RFID chip, you might get 150,000 chips. And if it's a big chip, you might just get 20 or 30. But to do that, you need to buy those masks. And there's like 50 masks. And the ones that pattern the MOSFETs, they have the smallest features, they're the most expensive. And a whole mask set for Sky 130, which is an open source, manufacturable PDK that we have access to. It's 20 years old. The masks are still $200,000 for a whole set. So you pay up your 200 grand, you get your masks, and then you're paying about $2,000 or $3,000 per wafer with however many chips are on it. But if you're wanting to prototype, you'd like to save money. So instead, you hook up with another 39 people on what's called a multi-project wafer. So in our case, eFabless is the company that runs the Skywater multi-project wafer. They take 40 designs, combine them into the one reticle, step that across the wafer, and then you get maybe 20 or 30 of your chips off each wafer. They run just five wafers. So you get about 100 chips in total. But you only have to pay $10,000 for that. So if you want to do that now, you can just go to eFabless, send them your stuff, pay 10 grand, you get 100. 100 QFN package chips six to nine months later. But that's still a lot of money. And the Google-sponsored free lottery hadn't ended at the time of Tiny Taper. But the lottery aspect of it was fairly annoying for me, at least. Other people as well, because you put a lot of effort into the design, and then you don't know whether it's going to get made. And I was always working with like 16 people at once, say. Everybody would be working. We'd all put it together into one design that we would then send to eFabless. So I was already concentrating multiple projects onto the die at that point. And I just thought, what if we just bought an eFabless chip Ignite slot, and then divided it up into 150 or 300 or 400 tiny slots and sold each of them?

**Chris Gammell:** And so this is the $10,000 product that now you're subdividing again to 150.

**Matt Venn:** Yeah. So I think technically it's called a multi-project chip, and we're using a multi-project wafer service to manufacture it. Oh, okay. And the current version of Tiny Taper fits up to 512 projects on one die.

**Chris Gammell:** Why are there only 150 slots? Is it because people get multiple projects?

**Matt Venn:** 150 slots?

**Chris Gammell:** Didn't you say there's 150 slots out of the Tiny Taper?

**Matt Venn:** For Tiny Taper 1, we got 150 people to submit it as R. Oh, I see. Okay. All right. So that was a full... Yeah, we were playing around with kind of what size makes sense. So now the tile size, that's what we call it, for the little area that you get is kind of 150 microns by 100 microns, and it's enough for about 1,000 standard cells. So you can squeeze in a very tiny RISC-V processor or a VGA driver or an FIR filter or PWM generator, these kinds of little projects.

**Chris Gammell:** Yeah. And now this is tied to the stuff that Uri was doing on Wokwe that then enabled all this to happen, right?

**Matt Venn:** Yeah. So we wanted a way of not just handling Verilog and HTLs, especially for working with complete beginners or high schoolers, say. So a schematic-based design entry system. So I'd met Uri through Hackaday, and yeah, we started. He took my Zero to Ace of course and rinsed through it in about a week or two because he's such a gangster. And then we started collaborating on the Tiny Tape Out project. He added a Verilog export, basically, in an eight-cell, standard cell library. And that's actually been really useful because even for people with programming experience, if they have no prior HDL experience, I find that drawing a schematic makes it more obvious that you're designing hardware. Whereas if you come to Verilog and you've been writing C, it's very easy to think that you're writing an executable program for a CPU, not designing hardware and joining wires together and instantiating devices. Whereas if you draw it out like a KiCAD schematic, it's kind of more obvious that it's all going to be running in parallel and it's all made of separate components that are all joined together with a network of wires.

**Chris Gammell:** Great. So now at that time, so basically you had 150 in the first one, you kind of started moving more and more and more, slots being filled, you said up to 512. But it seems like people are also doing more complex things as we kind of move along in the realm as well.

**Matt Venn:** Yeah, so there was a really big set of limitations made by my initial design choices about just trying to get something out there quickly, which was join all the designs together with a scan chain. So that's easy to execute, but you get massive latency if you've got a few hundred designs in there because you have to clock your inputs all the way through to the design that you want to be active and then clock the outputs all the way through to the end. So we ended up with a kind of sampled IO system that ran at about 10 kilohertz or so, pretty slow. And then I burnt nine IOs on the design selection parallel interface. So we had like a little dip switch on the board. You enable design 128. How many do you get? How many IOs total do you get on the MPW waiver? On the eFabulous pad ring, which is kind of the, you fit your design inside that, there's 39 IOs. Oh, okay. Yeah, so then... You're fairly limited. And you need some for, there's like a configuration firmware you need that needs like four pins of flash and then there's reset clock and power and stuff. So after I burnt the nine IOs on a parallel design selection, we only had basically eight ins and eight outs. Yeah. And yeah, Tiny Tape Out 2. So Tiny Tape Out 1 was like a free experimental one that we didn't guarantee. And then Tiny Tape Out 2 was the first one that people could pay for. So I think that was when we last spoke. And then three was the last one on the scan chain. But four, we were like, okay, this is happening. Let's go back and correct my bad initial design decisions. They weren't necessarily bad, but it was just like getting the job done and the time allowed. You know, now we're going to do this a bit more seriously. So let's switch everything out for a fast multiplexer and throw away the parallel design select and change it for a serial one and use those extra eight IOs for an additional eight IOs.

**Chris Gammell:** That's good. And so that was actually, now it was you had to go and design kind of the dinner plate that everybody's dinner sitting on, right? That's kind of the idea.

**Matt Venn:** Yeah. And that's like a classic engineering choice of you want to make it as simple as you can possibly make it without it being too simple.

**Chris Gammell:** Right. Yeah. I guess I still don't have a, I've seen some of the stuff and you've linked some of the, some of the designs. What is a, what would be a typical Tiny Tape Out design that you've seen? Yeah, typical is a bad word probably. What are some interesting ones, I suppose?

**Matt Venn:** Yeah, there's a ton of interesting ones. Well, we also with Tiny Tape Out 4 allowed you to join multiple tiles together. So then you can, the biggest design you can get is two times eight tiles. And then that's about enough for 20,000 standard cells. And we have on Tiny Tape Out 6, we saw a Linux capable RISC-5. Wow. Okay. There's a lot, there's still limitations in that. There's, because there's no room for memory really on these old processes. So the memory's external, so that slows everything down.

**Chris Gammell:** Mm-hmm. But it also benefits from the, the new IO that you were made, you freed up too.

**Matt Venn:** Yeah. Yeah. QSPI, Flash, and SRAM. Yeah. Yeah. Yep.

**Chris Gammell:** Hmm. Well, that's pretty cool. I mean, and Linux capable, I feel like that's like a, you know, that's a flexible term too, right? Yeah. How much Linux?

**Matt Venn:** It's meant to be micro Linux.

**Chris Gammell:** Yeah, I got it. Got it. Cool. But still, very impressive. But does that mean then that, that person that did the micro Linux capable processor design, they did all that in Wokwee? Or did they, do then people split?

**Speaker ?:** No,

**Matt Venn:** they used Verilog. Yeah. Verilog. Okay. So, so what, what we kind of breaks down after maybe 20, 30 standard cells, I think maybe the biggest design I've seen in Wokwee is maybe 50, but it starts getting really like a nightmare. And you're like, ah, now, now I understand why people invented hardware description languages. Yeah. If I want to register of 16 flip-flops, that's really annoying to draw. And I can do it in one line of Verilog. Cause it's a for loop. Is that right? What's a, what is a for loop? No, you just say like reg, my register 15 down to zero. And then it's bam. Okay. Yeah. That's pretty cool. And then if you want to build, if you want to like build a full adder to add two registers together, that's just like reg one, add reg two. And you haven't had to like draw 40. NAND gates. NANDs and NANDs and carries. I mean, that is cool to do that. Once. Yeah. Right.

**Chris Gammell:** Well, and you had mentioned at the beginning, you know, kind of also being able to target high schoolers, right? So like walkway can enable people of all, all walkways of life. Yes. Delirious. So are you actually seeing that come to fruition? Like, is this making its way into college curriculum, high school curriculum, stuff like that? Yeah.

**Matt Venn:** Yeah. We did a project with Oklahoma States last year. And they had a bunch of high school teachers in on a course. And then they all did a tape out with walkway. And now they're using those in their high schools. That was a national science foundation funded project. So we're seeing more of this, you know, we've got that 50 billion EU and us chips act. And a lot of that money is being spent on apps and so forth, but Intel. Yeah. I mean, the big companies have big nets to catch the, catch the dollars and good lobbying probably. That's right. But all the chips act all like say, but we're going to be missing 50,000 people to do the designs or run the fabs. So there's recognized that there needs to be an effort made on the educational front. And probably there's got to be worked on in tantalizing people away from well-paying JavaScript jobs.

**Chris Gammell:** Yeah.

**Matt Venn:** But also recruiting more people from high school into microelectronics and kind of revitalizing microelectronics courses. And one way of doing that is to expose younger people to microelectronics earlier. I mean, I don't know about you, but I had no concept of this kind of stuff when I was in secondary school. That's what high school is called in the UK.

**Chris Gammell:** Yeah. No, I, I mean, maybe I watched like a video and like chip processing at some point, but nothing, nothing like, yeah, I had nothing.

**Matt Venn:** Yeah. So just like showing kind of, you know, how a chip is manufactured. By the way, if people haven't watched my IHP fab tour video, you should definitely check that out. Yep. Definitely. We'll link that into link that in.

**Chris Gammell:** Yeah. It's interesting. I'm not sure I would tell my children to go work in a fab. Would you? No,

**Matt Venn:** I would tell your children. Got it.

**Chris Gammell:** That's fair.

**Matt Venn:** No, it's just spending one day in a clean room was, you know, it's, it's something that you, it's hard work. You have to get adapted to like any job that involves wearing protective clothing.

**Chris Gammell:** Yeah. I mean, I used to, I used to do it. I did it for like two years and I don't think I would ever recommend it to, like I said, family members, at least, you know, I think certain personality types actually do thrive in that. Yeah.

**Matt Venn:** I mean, I interviewed the guy, like some of the guys that I met in IHP and they on the whole love their jobs. And because they had like very, uh, high attention to detail and loved like refining processes and keeping everything very like controlled and in step and measured and precise. Yep. And it's definitely not my type of job.

**Chris Gammell:** Agree. Same, same. But like you said, I mean, like you're really, you're really showcasing. I mean, that's like the process side, right? That's the manufacturing of the chip itself. And there's people that got to design the thing that's going on with the wafer. So, you know,

**Matt Venn:** yeah. It depends. I think the argument that you make though, is that we, we keep running into these barriers. So like we're getting more and more transistors on a chip, but you run out, you kind of hit the top maximum speed you can hit and you hit the top power that you can hit. You hit the top number of cores that you can hit. And now people are more and more looking at the alternatives of general purpose computing and doing more application specific, but designing chips is hard work and takes a lot of effort.

**Chris Gammell:** Yeah. And usually you need an application that can bear the costs and the, you know, upfront costs and the, the ongoing maintenance costs, but yeah,

**Matt Venn:** it totally depends on your predicted volume. Like an interesting thing that I learned the other day was if you're doing volumes of tens or hundreds of millions, your non-recurring engineering costs, your NREs go to zero and you're left just with your recurring costs, which is like the actual manufacturer, the testing, the packaging, like yield issues. And they, they come to dominate the cost of your chip. Ah, I see.

**Chris Gammell:** And I think that you're not saying that they actually cancel them, cancel them out though. You're just saying that as a fraction of the overall,

**Matt Venn:** yeah, that they tend to zero as you get up in the millions of tens or hundreds of millions, which is why I think that the big companies don't really care that the proprietary tools are so expensive or like the cost of maintaining a big engineering team is expensive because it all tends to zero on these massive volumes. Yeah. But I think if you,

**Chris Gammell:** well, if you make one mistake too, right? I mean like, so I feel like what they're really buying when they, you know, they buy a cadence license or whatever, what is cadence? Is that one of the big, the big ones?

**Matt Venn:** Yeah. A cadence synopsis and mentor graphics.

**Chris Gammell:** Yeah. Right. So like one of those, I mean like if there's anything wrong, they could very quickly get damages into the millions of dollars too. Right. I mean, it's just like wacky.

**Matt Venn:** Yeah. Especially these brands, like the, the super mega awesome teeny tiny mini micro nanometro processes. They are like hundreds of millions in mass costs. So you definitely don't want to mess them up.

**Chris Gammell:** I mean, you look at Nvidia is like the most valuable company in the world now. Like, and it's because obviously the output is super important, but they also dominate. Like I was just listening to a report the other day that was just like, nobody can compete with them because, you know, they've got, they, you know, TSMC is basically made to serve applications like that, that are going to be high margin, high, high volume, you know, high needs, leading at bleeding edge, that sort of thing. So.

**Matt Venn:** Well, we are in the middle of an AI bubble.

**Chris Gammell:** It's a bubble. Oh, I didn't know that. Yeah. Didn't you? Yeah.

**Matt Venn:** Oh,

**Chris Gammell:** yeah. Matt, I thought you were, I thought you were going to come onto this show and announce that you were launching a new tool that has AI in it, that makes it easier to make chips. Is that not why you're here?

**Matt Venn:** CPT for chips.

**Chris Gammell:** Yeah. Yeah.

**Matt Venn:** That has been done actually. In fact, tiny tape out was enabled the world's first CPT design chip.

**Chris Gammell:** Yeah.

**Matt Venn:** And are people still using it? Yeah. I think it's pretty helpful for a bunch of things. I mean, I wouldn't trust it for something expensive, but definitely for playing around with things. But the point that I wanted to make was, I think there'll be new niches opening for more application specific stuff, but lower volumes where you do care more about the NREs because you're selling chips for a lot more money, but you have, and you have much lower volume. So then at that end of the market, your NREs dominate. So the cost of the tools, the cost of the team, that's, that's an important thing. So then I think that's where the open source tools can come in as well. Yeah.

**Chris Gammell:** Yeah. I mean, if we were to, to, to, uh, then Venn diagram, sorry, of like the, I think about the things that actually drive people to want to do, you know, like tiny tape of being one thing, like just a MPW wafer from the fabulous or, you know, just shuttle service type stuff in general, the reason people want to do custom silicon, I think about like things like power kind of ad hoc security, maybe even having additional security stuff that wouldn't, you know, be on general compute, uh, size capabilities that maybe aren't, aren't bog standard from like a chip maker, you know, like for some reason you need 16 serial ports or something weird like that. That's what I think about. Are there other ones in there in that diagram?

**Matt Venn:** I, I think in my opinion, anything that is purely digital, you would like, I don't see any realistic reason why you would do those chips, at least with the PDKs that I play with. Cause I'm, I'm also like, you know, the, the PDK that I have access to is 20 years old. Sure. So if I want, if I'm doing a digital project, then I would just use a microcontroller. Oh, okay. So where do you see the, the kind of the overlapping? I think the analog and mixed signal is the, the, the unique selling points of a low volume custom ASICs, because you can do stuff that you can't do in any other process. So if you concentrate extremely high performance analog with some radio, say, or a risk five core on a single die, then you're potentially making something that is really unique, that is hitting a niche in the market that hasn't been exploited yet, because it's too expensive to do with the traditional tools. Got it. Okay. The other thing is like, bear in mind, also for everyone that's listening, that I am really focused on the open source side of things. Like I haven't even used the proprietary tools. I don't have access to them. I don't have access to the NDA PDKs. So my viewpoint is going to be biased towards what you can do with the open source tools and what you can do with these older, cheaper nodes.

**Chris Gammell:** Yeah. But I don't know. I just feel like the industry, you know, you go to something like DAC, like design automation conference, and it's not like, you know, you basically need to be at a big company in order to be there, afford that sort of, you know, like there's a lot of money in the industry because there are big companies doing this sort of thing, but they're expected input into the, you know, like the kind of the hopper of students and, you know, potential people that could do that sort of work. It's just, it doesn't feel like they're aside from, you know, they do have university programs and they, they, they do have like low cost tools for university programs. It doesn't seem like there's as much of a general kind of entrance for other people.

**Matt Venn:** Yeah. I mean, another interesting data point maybe is that we have quite a few designs coming into tiny tape out that are from professional chip designers who are finally able to tape out their own designs when they're allowed to. Because when you're a chip designer working for a company, then you're just doing what your boss tells you because you're part of a big team on a big project. This is very expensive and can't be messed up. You're saying to use them mentor graphics license on the weekends, perhaps. Unlikely that would be allowed. I mean, some people that I talk to wouldn't even be allowed to do a tape out on tiny tape out because of the agreements that they've signed with their companies. Got it. Work for.

**Chris Gammell:** I'm sure they are well compensated for locking down those skills, but yeah.

**Matt Venn:** Yes.

**Chris Gammell:** Generally.

**Matt Venn:** Yeah. We had a great 12 bit SAR A to D put on tiny tape out seven by Texas instruments and analog chip designer. Really? What kind of speed was the SAR? I'm not sure. I'd have to check the repo. It's, I think one of the better repos in that it's got like a bunch of, you can tell it like a good analog design because it has a specification. Whereas my analog designs are just like, it should work. Yeah.

**Chris Gammell:** You just like, you know, you drop a P channel here and an N channel there and yada, yada, yada, you know? Yeah. When the input goes high,

**Matt Venn:** the output should go low. Done.

**Chris Gammell:** Yeah.

**Matt Venn:** Boom. Boom. If you don't specify things like slew or, you know, output voltage, then how can you fail?

**Chris Gammell:** Yeah. Yeah. Right. Guys, don't tell me. Just, I don't want to know. I don't want to know. Well, so you mentioned analog a couple of times. And so where did the analog start coming into the tiny tape outs and, and really just more generally in your use of the, the PDK?

**Matt Venn:** Yeah. So we brought it in, in kind of secret in tiny tape out five. So to be able to do analog, you'd first have to be able to power gate designs because you can't let people basically with open, lane, you'd like write some HTL and it's like a fairly automated flow and you get your standard cells and it's already passed DRC and LVS. And maybe you've simulated it. If you're good. And the design.

**Chris Gammell:** That's sorry. That's a, that's a pure digital design you're saying. Yeah.

**Matt Venn:** Yeah. Like they use, they're usually easy to manufacture and they, um, they work pretty close to how you expected them to work. But analog is really quite a different process. You're kind of drawing things out a lot more by hand. And it's like, it's much easier to say, forget to wire up the power or reverse the power or short out the power. So just like board design. Yeah. Yeah. It's like, um, it's like, imagine designing with KiCad with no DRC, ERC, or like board to schematic, uh, rats nest. Yeah. Very, very manual process.

**Chris Gammell:** Easy to mess up. I don't mean to bring it back to this topic, but I did see a thing that was an AI tool that said, we're 98% accurate on like, you know, helping with your components and like making sure your design's correct. And I'm like, I would never, ever accept a 98% accurate DRC, like engine, you know, like, can you imagine that? Just be like, ah, you'll be fine. You know, no problem. You know,

**Matt Venn:** like it's only $200,000, you know, why not risk it? Yeah. Right. Exactly. Yeah. Swaggy. I spoke to Carsten Wolf the other day's principal IC scientist at Nordic Semi, who's an open source Silicon enthusiast. He submitted a star E2D on tiny tape at six, one of his own designs.

**Chris Gammell:** And he did a video. I think we shared, shared on here as well.

**Matt Venn:** Yeah. I asked him what he thought about like AI for analog. Cause that's something people go on about. Like cause layout for analog is very manual. And he said, well, where would you get the training data from? Cause no one shit, like no one publishes that stuff.

**Matt Venn:** Yeah.

**Matt Venn:** That's a good point. Yeah.

**Chris Gammell:** Yeah. I just feel like they're going to be like auto rudder style, just like shuffling stuff around and just be like, Oh, this will probably work. We're going to just simulate it over and over and over again. Sort of thing.

**Matt Venn:** Yeah. I mean, there was like, I think an interesting application for tiny tape out is if you did build one of these tools, you could do like a hundred variants of your, analog layout and put them on each of a hundred slots on tiny tape out. Buy now. Now you're, now you're just trying to sell, man. I was,

**Chris Gammell:** yeah. We will give you a 2% discount. 2% discount for the 2% error.

**Matt Venn:** If you come with codes, Chris Gammell says, I'll give you a 2%. Yeah.

**Chris Gammell:** Chris Gammell hates AI as a code. Right.

**Matt Venn:** One more data point from Carsten's interview was he's told me that Nordic only moved away from 130 nanometer process like a few years ago. So, you know, they built their brand and all their IOT integrated radio stuff on 130. So you can do like a ton of great stuff on these older nodes.

**Chris Gammell:** Yeah. Do you know what family it cut off at? Was it like the 52, the 53? No, I don't know. No, sorry. I would have figured the 52. Yeah. Yeah. Didn't make it a 52 for a while, but yeah, I mean like the actual feature size of like, when you have like a Bluetooth chip or a wifi chip, you know, you look at like a die shot of like a ESP 32, they've got massive structures on there. You know, you need a processor still. There is a processor, but like,

**Matt Venn:** yeah, the analogs get big caps and inductors. Yeah. Right. And 130 nanometers is quite a sweet spot for analog designers. It's got good, good performance. So yeah, we had to make this power gate so that designs could be turned off if they're not enabled. And I got help from Harold Prettle, who's a professor at JKU in Austria. He's helped a lot on the, on advising on the analog side of things. And he submitted us super simple design. The only analog design we put on, I know we put two analog designs on tiny table, five, a ring oscillator and a, a deck. And a transmission gate power gated. And we just got those chips back. And they work. So that was a relief because six and seven are both based on that.

**Chris Gammell:** Yeah. We made some assumptions and we may have made a bunch of garbage sand. Yeah. Yeah.

**Speaker ?:** Yeah. Yeah.

**Chris Gammell:** The pipeline is long. What is the, when you do a, I still get anxious when I'm like releasing a PCB just to like, you know, JLC or something like that. How, how nervous do you get when you're like ready to cut a release?

**Matt Venn:** I used to be very nervous, but now we have one of the awesome things that URI has brought to the team is all the continuous integration stuff. So we started with that fairly early, but now it's basically everything is in GitHub. This is another nice thing about the open source tools is you can install them on a GitHub virtual machine and everything is public. So when you submit it, you get free to compute that too, right? Yeah, exactly. Yeah. Yeah. That's great. It basically opens a pull request. So on your repository, it builds the GDS and checks it and runs any simulations verification. And then once the green lights are all lit, you can basically open a pull request on the chips repo and then it gets integrated. And then we then run our own verification, simulation, formal verification, equivalence checking, like all the CI stuff. generate the final GDS files,

**Matt Venn:** submit them to eFabulous, run the pre-check there. And we, so we're kind of running this continuous integration, like the, all the time that the shuttle is open. And then when we do the, we close our shuttles like one week before the eFabulous deadline. And then it's, yeah, no, no longer stressful.

**Chris Gammell:** That's good. Okay. That's great. And in terms of like, when someone does a pull request into the, to the shared way for them, is it like, like, so if I uploaded a design, that's like a ring oscillator, is it just like, I get assigned a number and then there's like a folder that corresponds to my design. Like who does that integration piece?

**Matt Venn:** Well, we integrate it all into the die that is tiny tape out. And then we submit to eFabulous and then they integrate those 40 projects into the one reticle.

**Chris Gammell:** Oh,

**Matt Venn:** so they,

**Chris Gammell:** they actually do the glue. Who does the gluing? I guess when I think about like, um, Osh Park of yesteryear, right. You know, like it'd be like lane, like, you know, basically dropping these designs and like fitting them. Right. And now there's standards. There's like, you have a standard size. You just said 512, like standard blocks that you have.

**Matt Venn:** Yeah. So maybe consider, yes, it's a good question. I guess, I mean, I kind of feel like tiny tape out is the Osh Park of basics, but in this particular case, eFabulous is the company that is doing that final gluing all the designs together and submitting them to the fab. We don't, we don't talk to Skywater.

**Chris Gammell:** Oh, sure. But that's more like, like Osh Park used Royal, right? Like at one point, and, and so the eFabulous would be taking on the role of the board house. Right.

**Matt Venn:** Well, they still don't have the fab. Yeah. Yeah. So it's more like eFabulous is Osh Park and we're a customer that takes a small PCB. Switches up together. Divide that small PCB up into another 500 tiny PCBs.

**Chris Gammell:** Subdivisions on subdivisions on subdivisions. What does the PCBs? There's like a,

**Matt Venn:** because the PCBs are so expensive in this case. Yeah. Right. Even though eFabulous are bringing the price down to $10,000 for 10 square millimeters and a hundred chips, which is actually great value when you compare it against the things you can get from Euro practice and so on. 10 grand is still too much the average hobbyist.

**Chris Gammell:** Is that price dropping? Like, I don't actually know the economics of like, maybe eFabulous is like making more efficient and they get to, you know, kind of basically grow their margin over time. But I would, I would imagine that a mature process can have more efficiencies and that they could drop their costs eventually, or they'd be forced to by supply and demand sort of thing. Yeah. Maybe. Is that $10,000 ever any cheaper or not that it's like with tiny tape on two, it's not like, it's not expensive. Like this is amazing that it's so available, but I'm just curious about general costs. I mean, maybe it's a Mohammed question instead of a Matt question. Yeah. And that's your answer. Maybe. I mean, I know that. Mohammed, can you tell me all of Mohammed Kassim as well, who has been on the show? Like, can you tell me all of your business secrets, please?

**Matt Venn:** That's more of a fab question, isn't it? Cause you, you get your massive loan for billions of dollars and then you build your fab and buy all your machinery. And then you're basically selling wafers until you've paid off all the machines. Yeah. Yeah. It's an annuity. Reverse annuity. Every wafier you make is money in the bank. So it's kind of, you're going to try to get as much as you can. So I imagine that as more processes are considered trailing edge, the price will continue to lower.

**Chris Gammell:** Yeah. That's what I figured. And like I said, maybe e-fabless is, is, has it put into their model where they, they have a flat price over time. They basically get more margin. That would make sense. You know, they're basically taking a risk upfront sort of thing. But yeah, I just, I am generally curious about like, I don't know what fab costs do. Like it's, there's a lot of actual material costs and just operational costs for a fab, like just weird gases. And like, you got to have crazy ass, like a glycerin machine, like those things that like the implant machines, you ever see those? Did you see those on your tour?

**Matt Venn:** Yeah. They're like, they're like, they're like, they're like, they're like, they're like,

**Chris Gammell:** they're like, exactly. Yeah. Except, except with like boron gas and like phosphorus gas. And it's just like, it's like, it's basically like a, yeah, it's like a particle accelerator with like poison, you know, like in, in there, you know, it's, it's wacky, you know? Yeah. Yeah. It is magical bits of sand, of course. Yeah. So huge bits of engineering to build these individual machines as well. I know. And I take them for granted so often. I'm just like, well, why doesn't this chip work? Why is it so expensive?

**Matt Venn:** Yeah. Yeah. And it, yeah, it's crazy that they even work at all.

**Chris Gammell:** Yeah. This, this RISC-5 chip is 12 cents instead of 10 cents. I'm upset.

**Matt Venn:** Yeah. The customer's always right, Matt. You've got to find a customer that's willing to pay high margin chip costs. I have to find them or you, you, I think you have to find them. Well, I've, I've already found them. Are you talking to them right now? Yeah. Well, I mean, tiny tape out is an example of a high margin chip or like a high value chip. You know, the chips are a hundred dollars.

**Chris Gammell:** Yeah. Right. Right. Exactly. Yeah. So a hundred, a hundred dollars, you get how many chips? One chip, two, two, three. How many do you get?

**Matt Venn:** One chip. Yeah.

**Chris Gammell:** One chip.

**Matt Venn:** Yeah. By the way, we increased our prices. So for tiny tape out one, two, and three, that was all a hundred dollars. Now it's $300.

**Chris Gammell:** Wow. And people are still okay with it. Yeah. Didn't get any pushback at all. That's great. I mean, yeah. I mean, at a certain point you're, you're really offering the experience of building a thing, holding that thing in your hands. Like that is, excuse me, super magical. Right. I mean,

**Matt Venn:** like to the point where I feel like I did my classic thing of just like chronically underpricing the product and not taking into account, like all the work that goes into sure making something. Yeah. Yeah. A hundred dollars was, I mean, when I originally came up with the idea in my head, it was like a hundred dollar tape out, but I have like enough business sense to know not to embed the price into the name of the company. So I changed a tiny tape out, but kept the a hundred dollar price mark. But yeah, too low. But the, due to the e-fabulous sponsorship, the first hundred customers get it for $150. So we only actually, for individuals, the price only went up by $50. But for universities or like companies that need an invoice or after the first hundred chips are sold, then it goes up to $300. Yeah.

**Chris Gammell:** Buy now. Buy now. Buy now. Okay. So let's talk a little bit about, so obviously you have a course too. We've talked about that when you've been on the show in the past. It's well, well regarded.

**Matt Venn:** Before I forget, let me just say tiny tape out is open now and closes September the 6th. So if anyone's listening and they want to do a basic tape out, go to tiny tape out.com and have a look at what's going on there.

**Chris Gammell:** So that's like six weeks away. So like that's, that's a good lead in here too. Can I learn chip design in six weeks?

**Matt Venn:** You could like draw a few standard cells in walkway, run it through the automated flow and then get a custom ASIC made and ordered in a few hours. Okay. Let's move up from there. What's the next step up? The next step would be like learning how, like a, like kind of going back to what we were talking about with walkway, like what's a full adder? How does a register work? What, how about like a linear feedback shift register or like pseudo random number generator? Okay. Draw like a bunch of these kind of fundamental digital building blocks on in walkway, test them all, take them out. Next step up, learn a hardware description language like Verilog or one of the new, newer ones like Spade or. I was going to say Rust. Everybody says Rust. Yeah. I think probably Rust is coming soon to chip design. I don't know. Yeah.

**Chris Gammell:** If, if, here's the thing. If Rust is coming anywhere, you're going to hear about it from the Rust station. So don't worry, don't worry. You'll hear. Yeah. I see, I see all you Rusties. Rust. Yeah. Rustations. Yep.

**Matt Venn:** And they do great work. I just, you know, as, I mean, as long as you eventually end up generating Verilog, that will work. That plays nicely with all the open source tools. So there's one that is not a high level synthesis. It's more, more of a hardware description language called Amaranth. It's a new one. Newish. Uh, by WhiteQuark. Oh. It's got, it's under a lot of development at the moment. Lots of, um, community driven RFCs and so forth. Good one. Worth checking out. And that compiles down. That's the wrong thing to say, but you, you end up with Verilog and then that's, you can put that into your replay.

**Chris Gammell:** Yeah. WhiteQuark is kind of like Uri in like, in terms of like the echelon of just producers, just like wacky, wacky amounts of output. Yeah. They're very, very impressive.

**Matt Venn:** Catherine WhiteQuark. Yeah. And did you see, uh, she recently showed, um, full in the browser, HDL to FPGA bit stream and program the board. Like I think she did it all on a mobile phone.

**Chris Gammell:** Oh my gosh. Yeah.

**Matt Venn:** Yeah. That's what we're talking about here.

**Chris Gammell:** Like that level of that's, that's very impressive. Yeah.

**Matt Venn:** We've got a, um, a GitHub action now that also generates the bit streams for ice 40 FPGAs. And we have this, um, Oh, cool. Little replacement board that fits on top of the dev kit instead of the ASIC. So for development, you can develop on an FPGA and then when the ASIC comes back, you swap them over. Oh, that's a great idea.

**Chris Gammell:** Okay. So basically because you're starting from Verilog that can compile to just FPGA land, bit stream. What about the, um, size? I guess probably the, the ice 40 is probably much bigger, right? It has a lot more headroom in there.

**Matt Venn:** The up five K is the same one on the, um, one bit squared ice breaker, which by the way is my recommended FPGA of open source choice. If people are after an FPGA.

**Chris Gammell:** Okay.

**Matt Venn:** Shout out to Esden. And I think it's 5,000 logic elements. Uh, so that would be maybe like two or three tiles. worth of tiny tape outs, but it does come with programs and DSPs, which are.

**Chris Gammell:** Got it. Okay. Yeah. So like the Linux capable one that you described earlier in the show that would not fit on there, but maybe other ice 40s that are large. Yeah.

**Matt Venn:** Got it. Yeah. I mean, it's a good, it's a good for people that are, uh, like beginners. It definitely covers you. Yeah. Okay. Yeah. That's great.

**Chris Gammell:** What about, so, okay. So walk us through again, the, so I had said six weeks. What is the, what is the most you think someone could do in six weeks? Not saying they should do it, but like maybe, or maybe what have you seen that has been the most someone's done in six weeks?

**Matt Venn:** I saw someone do a, a GPU. Really? Yeah. Which, and that took a lot of work because they had to read a lot of papers about the kind of fundamental architecture of GPUs and how to, I think like not everyone, but a lot of people know that like a massive array of multiply accumulates, but how are they actually fitted together? And how would you then be able to load something onto that and make it work? Like the devil is in the details. So sure. They spent, you know, names, Adam, they did like a tweet thread on Twitter about it. Yeah. And we've seen FPGAs as well. Again, I wouldn't recommend that for beginners.

**Speaker ?:** Okay.

**Matt Venn:** There's a really cool, um, risk five course by Bruno Levi, who walks you all the way through nothing to building your own risk five processor.

**Chris Gammell:** Oh, cool.

**Matt Venn:** And that would fit on like one or two tiles worth of tiny tape out.

**Chris Gammell:** Right. Cause risk five stuff can be basically as big as you want. Like you could put lots of memory. You can make like super crazy large processors, right?

**Matt Venn:** Yeah. And you can do things like, yeah, you could have like out of order or like multi-stage pipelines. So it gets bigger or you do like bit serial stuff. So it gets smaller, but like personally, what the kinds of things that I like to do are the kinds of things that surround the, the CPU core. There's already so many risk five CPU cores. So, but they're not, they're not really much good on their own. They need GPIO drivers or like the RP2040s PIOs or PWMs or A to Ds or D to A's or timers or interrupts or like all of this, you know, the, when you'd like buy an Atmel chip and it's got like 40 really cool rock solid peripherals.

**Chris Gammell:** Yeah.

**Matt Venn:** All of those things have to be made. And they're like, they're an interesting thing to try making. And it, I think also as you know, most people that use tiny tape out aren't going to become chip designers. It will just fill in an area of their knowledge they didn't have before. So if you make a, a serial you what, um, for a risk five processor or something, something like that. So that when it runs on an ASIC, it's just printing out like a, a pre-programmed. Hi, Chris, welcome to your first ASIC. And that's all it does. And then counts up to a hundred or you have a little bit in there that is like a, I don't know, Prince of Fibonacci sequence or something.

**Chris Gammell:** Yeah.

**Matt Venn:** But then next time you're writing code for a serial port, you're more thinking about, okay, yeah, the data gets loaded into this thing. And the serial port is going to go off and use a clock divider to clock this stuff out at the right board and then raise an interrupt. And then that's when the CPU will get interrupted and load the next byte of data in. And you kind of get a bit of a better understanding of what's going on under the hood with all these libraries and levels of indirect that we all take for granted these days.

**Chris Gammell:** Yeah. And that's, that is good. I mean, like I think younger, earlier, let's just say earlier, Chris would have been more like grumpy about that. Like, why do I need to learn it? But I think as I've done more programming, I do, I do think there's value, value to understanding it. Right. So it's not a true black box where it's just like, well, I wrote it in there. Why didn't it do what I wanted it to, you know, like it's actually understanding some of the underlying does, does have benefits outside of.

**Matt Venn:** Yeah. I think I, yeah, I'm a big believer in like a broad level of knowledge that gives you jumping off points, or at least, you know, that there is a field that is focused on this. And then you could be like, who do I know that is an expert on DMA? And then you find that person and then they like accelerate your program by a thousand times by like correctly writing a DMA driver. Whereas if you have no idea about how that stuff is working under the hood, you like, well, my processor just is too slow for my application. So I need to write one that's a thousand times faster.

**Chris Gammell:** I got to, I got to pay more.

**Matt Venn:** Right.

**Chris Gammell:** Exactly.

**Matt Venn:** Yeah. Yeah. No, like you need to enable this bit in the DMA register and then you're going to take advantage of this, like incredibly accelerated pipeline to take memory and pump it out of the D2A. I'm a fan of VGA projects, stuff that puts stuff on these panels. We have a community developed little VGA PMOD by Leo Moser. And we're going to run a competition for Tiny Tape Out 8. It's kind of in the works, but it's like ASIC demo scene.

**Matt Venn:** Oh, so like one cell? Has to fit in one tile, uses the standard PMOD and PWM audio. And then we'll like give prizes to the, the coolest, most impressive designs and have like categories like best sound, best graphics, best racing the beam, best newcomer.

**Chris Gammell:** That's great. I like that. I like that a lot. Yeah.

**Matt Venn:** I think, I think we like one thing that we've heard a lot about why people like Tiny Tape Out is kind of working within the limitations. How much can you really do in 1000 standard cells?

**Chris Gammell:** What would you, if you had to guess the maximum, I guess you, you've seen a lot of these now too, right? You kind of get to sample all these in terms of like single tile. What's the most, I guess you said you've seen a very tiny risk five or not.

**Matt Venn:** Yeah. I've seen a risk five or like just very many CPUs. They're a very common thing.

**Chris Gammell:** Oh really? Okay.

**Matt Venn:** Yeah. And I think, because you get to start from,

**Chris Gammell:** because you get to start from other people's IP, or you think people are just kind of like re-implementing in Verilog? Yeah.

**Matt Venn:** I think like after you've built a full adder and a state machine, you're like, you're halfway there to a very simple CPU.

**Chris Gammell:** Sure. Yeah.

**Matt Venn:** So it's like a common, I mean, it's still on my bucket list to be honest. Really? Okay. Make my own CPU. Just to, especially after playing with that cool Supercom exploded view, four bit CPU badge. Oh, the, the Voyeur. Yeah. I think I, I have that one. Voyeur's. Awesome. Yeah.

**Chris Gammell:** Yeah.

**Matt Venn:** It's like, you really kind of see, okay, you need, you need like a clock. You need an ALU. You need some registers. You need like a couple, you need a data path. You could see it coming together in a few hundred lines of Verilog.

**Chris Gammell:** Yeah.

**Matt Venn:** But yeah, I would start off with simplest. I mean, after you've got the CPU, then you, then you need like an assembler and, a compiler and all the, all the governance, if you want to make it nice to develop for.

**Chris Gammell:** You had said in that your list of tools that you're seeing, so you're seeing new tools come up as well, like new tools for people that are building stuff. Is that like compilers or is that other, other tools that are,

**Matt Venn:** like new hardware description languages. There's a one called Surfer that is a browser based waveform viewer. There's the one that everybody uses is called GTK wave. Again, in the open source world, the one that everyone uses. That's quite interesting for us because we would like to plug that into our GitHub action flow. So that after it runs the tests, you can then load the waveform in the browser. Yeah. Then, um, uh,

**Matt Venn:** Yosis HQ's got a formal equivalence testing tool. So you can take your incoming harder description language and then formally prove that the output of the GDS compiler essentially is correct.

**Chris Gammell:** Can you remind me? So I remember Claire, when Claire was on the show, talked about formal verification. I'm not sure I understood it then. So like, how do you prove that it's correct?

**Matt Venn:** You use a SAT solver, satisfiability solver, which is, I think a nice, we actually, there's a cool blog post about this on the Yosis HQ blog. If you've not checked that out, then it's worth a read. And there's, um, one by a guest, a guest post on using SAT solvers to solve Sudokus. And it's, I think that's quite a nice way of thinking about it. Everyone, everyone's like knows what a Sudoku is. So you basically say, all these rows have to add up to this. All these columns have to add up to that. Is there a solution that satisfies all these constraints? And then a SAT solver is a type of software that can basically say yes or no. And if it says yes, then it's not just a, a yes. It's that there's a mathematical formal proof that can be made to show that that is true. Got it.

**Chris Gammell:** And it's not just doing brute force. No. Like just try all the things because that would take forever. Right. Yeah. It works a different way.

**Matt Venn:** I mean, it, it has its own strengths and weaknesses like every other verification technique, but yeah, there's some, you can do a lot in, in this, in a simple thing. Like we have formal verification on the tiny tape out multiplexer. And there's like just one or two assertions that basically say, so we instantiate the chip, we connect all the outputs to all the inputs. And then in a, in a design, we say assert that my inputs equal my outputs and allow the solver to set the outputs to be anything that they want. And then the solver can pick any designs in any of the multiplexer and set any of the outputs. But if the multiplexer is working, then the inputs are always going to be what the outputs are. If we've made a loop back on the outside of the chip. Huh. Whereas if, if one wire was missing in one MUX location, then that formal assertion would fail. But I didn't have to write a program that checked it in every position because the sat solver would find, if there was a place where it would fail, it would fail there.

**Chris Gammell:** Yeah. I think that just highlights to me, like the amount of helper software that's in, like you mentioned, that's in the CI loop. And now just enabling all this stuff. Are you also, are you seeing new tools? I mean, so open lane, open road, I think, oh, did we have someone on that was doing that stuff?

**Matt Venn:** No. I think we've done a different podcast. Andreas Uluson of, um, Oh yeah. Zero Ace. Not to be confused. He was on the show. His company have a tool called Silicon Compiler, which is another. That's right. Verilog to GDS flow.

**Chris Gammell:** Got it. Okay. Yeah. And, and he had been doing some of that stuff, I think for the government too, right? The U S government, some of the open lane, open road stuff.

**Matt Venn:** It's been a lot of shows. Yeah. He was an e-figure in actually getting the open source tools developed. So yeah, he was working for DARPA and funded the development of open road and open road is like the core set of tools that are now used by pretty much all the open source ASIC flows.

**Chris Gammell:** Got it. So are there new tools that are coming down that pipeline in terms of like open source capabilities? And like, are you, maybe you don't have visibility into that. I really don't, I don't watch that scene. I mean, you just, yeah, there's another,

**Matt Venn:** there's a new version of open lane called open lane two, which is like an upgrade of opening. Okay. And yeah, like the fundamental tools like replace and Triton router and these kind of, um, place and route tools and legalizing tools. And there's one called open STA for static timing analysis. They're all like in active development.

**Chris Gammell:** What are you, sorry,

**Matt Venn:** legalizing tools. What does that mean? Yeah. Getting a bit into the details there. So,

**Chris Gammell:** well, yeah,

**Matt Venn:** sure. Uh, place and route. The first part is placement and there's a, I see some really cool animations I've seen because it's the placer uses an electrostatic model. So it like puts a negative charge on all the standard cells in the software model world. And then they like repel each other, puts them all on top of each other. They will blow out into a cloud. And then they're like pulled the other side of the cost function is pulling together where they, where the, which standard cells should be together. So it kind of like jiggles them around and wiggles them and they kind of.

**Chris Gammell:** Like trying to optimize for shortest route, that sort of thing, or like shortest distance.

**Matt Venn:** It's one of these impossible problems to solve that is kind of well handled by these kind of models of nature. Another, the, and then for the routing, a common model is called simulated annealing, which is like annealing metal, kind of crystallizing and melting and recrystallizing. So like ionic re-applied to chip design. Exactly. Yeah. Yeah. It works surprisingly well. Anyway, after the, the best ways,

**Chris Gammell:** man,

**Matt Venn:** after the global place is done, all the cells are in a cloud, but they need to clip into the power distribution network, which is very regular. So the legalizer basically pushes all the cells so that they clip into the right place and maybe flips them. So they get the right power supply. Wow. That's wild.

**Chris Gammell:** And, and I mean like, and then the level that I, as a complete noob would interact with that is none. Right. I would just be like, it's just running. So.

**Matt Venn:** Yeah. Essentially all of that is abstracted in the GitHub action and then inside open lane. But if you want to, you could download the tools, run them on your computer, and then you can like pause any part of the process and inspect where the design is at that moment. So. Cool. You have like full transparency into what's going on if you want it.

**Chris Gammell:** So then when you do, so you've been doing some analog stuff, you've been doing some analog experimentation and learning and things like that. Hmm. All that same tooling applies. I still don't quite understand the analog versus like kind of the more the Verilog flow.

**Matt Venn:** Yeah. The analog is different to start with. You make a real rock tight, rock solid specification because after you do your schematic capture and start your layout, if you have to change your layout or your schematic, you basically have to. Start over. Reset a lot of your work. Yeah. So you really work hard on specification to get like, to know what success is and then you don't want to change it. Hmm. That's not what I do.

**Chris Gammell:** Well, you're learning. I mean, that's okay.

**Matt Venn:** I'm learning. Yeah. So you're learning the,

**Chris Gammell:** uh, in the old head, head on desk mode, right. And you know, like that's the, yes.

**Matt Venn:** So, well, I'm just like, what would be a cool design to make a, like a voltage reference. I'll like download a bunch of IEEE papers and read them and find a circuit that looks like I could do it like with the minimum number of transistors. The biggest circuit I've made so far, I think it was seven transistors. And that was too much to be honest.

**Chris Gammell:** Wait. And does that mean that you can then put a Zener in silicon? Like you can design that in and as a, as a thing.

**Matt Venn:** I'm not sure about a Zener. You can definitely make a diode. Okay.

**Chris Gammell:** Diode. Yeah. I guess you're, so you have access to more of like the building blocks. So you can like basically pull out diodes and things like it, or are those also staying?

**Matt Venn:** The main thing that you're doing is drawing, uh, MOSFETs, resistors, and capacitors. Okay. And one thing that is super interesting that I've found out recently is if you draw a capacitor or a MOSFET and they're close to each other on a, on a die, on a layout, they can be very well matched, but they won't match on the next wafer that is produced. They might be like 10% off in value. Why is that? Because things change in the process. You've got this insanely complicated stack up and just a few microns thicker solder mask on the next wafer is going to give you slightly different performing MOSFETs. So. Wait, how does that work? So you just have to have like lots of like checking and. No, you do it by designing with ratios. So like you do the ratios between components, not precise values of components. Huh. So imagine like a really simple voltage divider made out of resistors. Those resistors might be different from wafer to wafer, but if they're matched well to each other. I see. If you get three that are exactly the same size and you put in five volts or say three volts at the top, you get two volts and one volt out. Yeah. It doesn't matter if those resistors have a different absolute value on the next wafer. Right. You're still going to get two volts and one volt. Got it. Okay.

**Chris Gammell:** That's interesting. Yeah. How, what does this, what does this tooling look like? Cause like, okay, so I had a, I had a very bad experience. I did, took an analog chip design class in college. I got a D I barely passed. I don't, I probably shouldn't have passed to be honest. I think my teacher took pity on me, but it was pencil and paper. It was terrible. It was, it was colored pencils. Yeah.

**Matt Venn:** I mean, that's like, if you want to learn it properly, that's the way to do it. And there's, there's kind of, I don't want to do that. I want to do that. No, no, no.

**Chris Gammell:** The teacher was wrong and he should have, he should have given me more tools, Matt. I wasn't in the wrong. He was. Well, you should start with silly ways. Despite all the people that went on, went on to, you know, design actual chips for my class.

**Matt Venn:** Yeah. Oh, I'm yeah. So just, you should start with silly ways to get a, like just a rough idea of what's going on. And I know Uri and Torsten will be sad if I don't say silly ways. Silly ways. I think,

**Chris Gammell:** I think that was right as, when did we mention silly ways? I remember mentioning silly ways on the show.

**Matt Venn:** It wasn't public last time we spoke and now it's public and so are the lesson plans and they're available in Spanish as well. Okay, great. Um, but that is like, you draw the layout and you simulate the MOSFETs and the capacitors and the resistors. You build simple circuits. The thing that's missing from that is schematic capture. So the reality is you do the schematic capture in a tool called X scheme. And then you simulate that. Once you're sure it satisfies your specification, you do the physical layout of drawing the transistors and the resistors and capacitors and wiring them all together. Okay. And then you extract the circuit, which includes parasitic resistances and capacitances. And you check that when you simulate that, it's still fits your specification.

**Chris Gammell:** Huh.

**Matt Venn:** And then if you're, if you're cool, then you tape that out. I did a video about this recently on the zero to a set course, YouTube channel that like showed, showed how I did it for the simple deck. I think that I did recently. So if you want to see the tools in action on YouTube, check out the channel. And yeah, let me just also mention, I've got a new course under development, the analog version of the zero to a set course. And if people are interested to get on the wait list for that, then it's bit.ly slash analog dash wait list. We'll put, we'll put a link of course. Put a link.

**Chris Gammell:** Yeah. What would people expect to have at the end of that?

**Matt Venn:** Uh, things like op amps are quite common because you only need five transistors for an op amp. DACs like resistive. Like one of my first projects before I even started with transistors was doing things like, um, build a little digital block that does a sawtooth waveform and then plug that into a resistive, an R2R DAC and just like make a sawtooth output. I did a, um, a twin T oscillator. I got inspired by Alan Bulk's, YouTube channel. Okay. Uh, cause you can do that with a notch filter in an op amp. So I stole someone else's op amp. Oh, nice. Build a notch filter. And then that just like the notch filter goes in the feedback path of the op amp. And you get a relatively sinusoidal output, hopefully at two megahertz in my case.

**Chris Gammell:** What are the relative, you mentioned you can put resistors and capacitors in there. What are the relative values you can do? Uh,

**Matt Venn:** yeah. Good question. If you devoted like your entire area of a tiny tape out tile, you would reach maybe one pick a farad. Okay.

**Chris Gammell:** And it would be 10% different the next time you make it. Right.

**Matt Venn:** Yeah. Yeah. I, capacitors match very well on the same die. Yeah. Um, so they're, they're like, you want to use them and transistors more than resistors. If you're going to use one,

**Chris Gammell:** you should use two. Huh?

**Matt Venn:** Yeah. Yeah. And connect and use symmetry. You've got all this stuff with symmetry and layout and dummy devices. It's really gets, uh, gets complicated. Boris Merman is a lecturer and he's, I've been chatting to him as well about, he's got like many, many years of industry experience and now lots of experience in lecturing. And he's written a couple of books and they're published on GitHub. If you look up Boris Merman on GitHub, you'll find them. And he made a, I copied this from his book. How does microelectronic design compared to board level? That's quite interesting. So board level stuff, you, you're trying to do like hundreds of components, whereas hundreds or thousands of components is totally fine for basic. Resistors, uh, in the range of one to 10 mega ohm on a board and capacitors, one pick a farad to 10,000 micro farad. Whereas on ASIC, you're like fem to farads to pick a farads range. Resistors and capacitors on board level can be, you can buy like matched like to 1% if you buy the expensive ones, but on a ASIC, although they can be matched to 1% on a die, they'll only be like 30% across wafers. So that's where this, um, where you're wanting to design with ratios, not absolute numbers. So that's where a lot of the, the clever stuff happens in analog design. It's like way beyond me at this moment.

**Chris Gammell:** I feel like the, I'm having the same feeling that I had the last time we were on the show where I'm just, I start to look at this stuff and I'm just like, how does anything work? You know, like I know like at the bottom there's physics and you kind of work your way up and there's all the process stuff and you know, all the tooling that makes it all possible, but like hot damn, like it was just, yeah, it's amazing.

**Matt Venn:** Yeah. I mean, each one of these topics is like years of research and PhD. Graduate,

**Chris Gammell:** graduate degree if you want it.

**Matt Venn:** Yeah. At the free Silicon conference, I was chatting with guys who spent like 15 years only designing PLLs.

**Chris Gammell:** Wow. Right. And I can imagine those, those folks as well that are like PLLs masters. They know chip design generally. I can imagine them being like, yeah, I want to make a processor. I want to make a whatever, you know, like I feel like because of the complexity of, and like the importance of something like a PLL and a chip set, you probably do get kind of pigeonholed. It's kind of, that's, that's a negative connotation there, but like you get specialized because you need to be specialized because you need to make it better than everybody else. Right. Like,

**Matt Venn:** yeah, I think that happens in like every industry, basically you get things get so specialized that you have to, if you want to be useful, you have to, in a big company, let's say in a startup, totally different story. And I think, yeah, we will see more Silicon startups, especially now with like more niches available and kind of the end of the gains of Moore's law and general purpose computing.

**Chris Gammell:** Do you think, I mean, you mentioned the chips act. Do you think any of that will trickle down to the, to the, this crowd or no?

**Matt Venn:** Yeah. I mean, it's trickling down to me and the, the open source crew already. Yeah, definitely. We're getting like, okay. I think I've co-signed 10 letters of support for NSF funded educational projects in the U S. Oh, great. Okay. So like, Oh, that's great. U S chips act funded stuff. And then we've got, I don't know, like five or 10 universities in Europe that are developing their microelectronics courses. courses. And like, typically you wouldn't get to do a tape out until PhD level. And we're basically saying if you're doing electronic engineering or microelectronics or VLSI or computer architecture, you should do a tape out at bachelor.

**Chris Gammell:** Yeah. And then sooner eventually. Yeah. Yeah. That's great. Cool. Well, that's really great, Matt. I mean, every time I watch your stuff, I'm, I'm amazed at how much, how much thing, how many things you're doing. It's really, it looks exhausting.

**Matt Venn:** Delegation is the key.

**Chris Gammell:** Yeah. But still, I mean, like, it's great. It's great. You're doing this stuff. I think we all benefit from it and, you know, you're building a great team too. So yeah, we all, we all benefit. Yeah.

**Matt Venn:** Yeah. I think that that's a very underrated skill is like the communication and the, the team working. And I think a lot of people, myself included, you know, kind of get drawn into maths and science and engineering because we, you know, maybe communicating and working in teams isn't the easiest thing, but I really kind of felt my powers were unlocked when I learned how to,

**Chris Gammell:** with our powers combined,

**Matt Venn:** learn how to communicate because no matter how cool your project is, if you can't get it out there to other people, if you can't communicate it, if you can't work in a team, then it's like can die on the vine essentially. So, and yeah, the, the course and tiny tape out have proved like incredible places to recruit from. So, you know, someone does a tape out on every shuttle. They're ideal people to ask to, are you interested in getting paid to do documentation or get paid to do the next week? That's great.

**Chris Gammell:** Where can people find all your stuff?

**Matt Venn:** Tiny tape out.com, zero to acid course.com. And,

**Matt Venn:** and shoot,

**Chris Gammell:** I forgot the name of it. Fuzzy wigs. No. What is the silly?

**Matt Venn:** Silly whiz. Silly whiz. Silly whiz. That's it. Silly whiz is linked from tiny tape out. Got it. Okay. YouTube channel. There for Silly whiz. Zero to acid course. YouTube channel. Sign up for the mailing list. Like, subscribe, ring the bell.

**Chris Gammell:** Classic. There's the communication stuff. He's talking about folks. He's gotta, he's gotta get people to ring the bell so that we can be dinged when there's new videos and I'm enjoying it. Yeah.

**Matt Venn:** Actually, let me just share one last little anecdote. Um, the 3d viewer, when I show that to people in the biz, they're like, this is pointless because they're so used to seeing everything from the top. Yeah. And they know how everything is interconnected in their mind's eye. They understand. But when you're a beginner, being able to see it from the side or rotate it is so invaluable to understanding how these layers work together, but it's not included in any of the normal tools. So it's like a real, everyone was like so amazed when they saw it. And that came from a community contribution that came from Maximo, who also does all the amazing 3d blender renders of the chip design stuff we do. Awesome. And I can,

**Chris Gammell:** I can tell you another anecdote about that sort of thing. One of my college friends who worked, started at Samsung when I did, he and another person took Google sketchup at the time, Google sketchup now sketchup. Right. And they basically did the exact same thing where they, they, as we were learning chip design, it was so incredibly critical. And, and like you said, the same thing, like the, the teachers were like, why do you need this? And we're like, because it makes sense now, you know, like visualizing, uh, you know, a capacitor cup on a piece of DRAM is like so tough to visualize. And yeah, when you start to see it and zoom in and yeah, that's great.

**Matt Venn:** Yeah. It took me literally days of thinking and drawing to associate masks with 3d structures and MOSFETs. And that was a big reason why we did silly words and having the 3d graphics. And then the, the other part of that story is it turned into an incredible marketing tool because it made the kinds of pictures that people love to share.

**Chris Gammell:** Yep.

**Matt Venn:** So it had this really unexpected community growing influence that was unplanned and unexpected. But I think it's an interesting story because I know a lot of engineers struggle with the marketing stuff. And one thing to maybe think about is like what kind of stuff that people want to share and how can you make that easy for people to share? And that will help you grow a community and that will help your products take off.

**Chris Gammell:** Yeah, no, that's good tip. It is sharing. Yeah. The sharing piece is important because you can't just, you can't just blast different channels, you know?

**Matt Venn:** No. And you need like a sustainable growth if you're going to last without burning out.

**Chris Gammell:** Yep. Yeah, totally. Totally. Well, Matt, thanks for not burning out. Thanks for being back here and, you know, continuing Tiny Tape out. September, what's the close date? September 8th?

**Matt Venn:** September 6th is the next one. And then we've got, then we've got the next one. I think it's in November sometime. Okay. Shortly after the Hackaday Supercon. If people are at Hackaday Supercon in South Pasadena, definitely say hello. Yeah. I'll be there. I hope to be there too. Are you going to go?

**Chris Gammell:** That'd be awesome.

**Matt Venn:** Yeah.

**Chris Gammell:** Yeah, we'll see. Last time I went, I lost my voice. And I don't think, you know, I think we talked about how I lost my voice.

**Matt Venn:** Yeah.

**Chris Gammell:** Yeah. Got to save the moneymaker. All right, man. Thanks for being here, Matt. Thanks so much, Chris. Take care.

**Matt Venn:** Take care.

**Speaker ?:** Take care. Take care. Take care. Bye. Thank you.
