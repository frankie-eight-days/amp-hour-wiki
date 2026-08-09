---
episode: 302
title: An Interview with Clint Cole of Digilent
url: https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/
---

**Clint Cole Of Digilent:** This is The Amp Hour Podcast. Recorded June 8th, 2016. Episode 302. An interview with Clint Cole of Digilent.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Clint Cole from Digilent.

**Dave Jones:** Hey, Clint. Thanks for joining us.

**Chris Gammell:** My pleasure. Glad to be here.

**Dave Jones:** Everyone knows Digilent, I'm sure. That's good to hear. You're everywhere. Like a plague.

**Clint Cole Of Digilent:** If not, they will after this, because we're going to talk all about it, I think. I can't think of a better way to spend time. I didn't quite realize. I mean, so you and I had met previously. I didn't realize you started the company. I'm sure that came up at some point. But I didn't realize that you are also the founder. So you're the president and the founder.

**Chris Gammell:** That's correct. Yep. Started back in April of 2000.

**Clint Cole Of Digilent:** So slightly different time. Could you give us a quick recap of what Digilent is and what you guys do?

**Chris Gammell:** Yeah. And maybe I'll start by just talking a bit about why we started the company as well. Yes, please. That's way better. Yeah.

**Clint Cole Of Digilent:** You're out interviewing me, Clint. Come on. Make me look bad.

**Dave Jones:** It's not hard.

**Chris Gammell:** I was working as an engineer out in Seattle in Portland for a bunch of years. And then in, it must have been 97, I was working for, well, we started a company out in Seattle that made the ultra-portable defibrillators that you see in airports and stuff now. And that company sold in 96. So in 97, I thought, you know, I'll go see what else is out there. And I came back to WSU, Washington State University, to see if I wanted to be a full-time academic. And coming out of industry, I had a pretty good idea of what we needed to teach students, you know, to make them be successful in a more modern economy. And got to WSU, and things really hadn't changed since I was a student. I mean, it was the same topics, the same designs, the same textbooks. The same curriculum, everything.

**Dave Jones:** And all teaching programming on mainframes and that was... Yeah.

**Chris Gammell:** In fact, and I'm not even making this part up, I was handing out photocopies of mimeographs that I had been assigned.

**Dave Jones:** Oh, wow.

**Chris Gammell:** I was expecting punch cards maybe, too. I was hoping for some punch card story, but... They moved up to the VT100s, I guess, since then.

**Dave Jones:** Oh, yeah. Fancy-pancy.

**Chris Gammell:** Yeah, exactly. So I set out to bring some more modern technologies and tools into the curricula. And among other things I was trying to find was a demo board. You know, so students could actually use hardware to implement designs rather than just simulate them. And really couldn't find something that was affordable and had the right features, so started to design a couple of them. And then other universities in the northwest of the U.S., I had kind of friends and associates around, heard what we were doing and wanted to know if they could also take advantage of it and get some of those boards themselves. So all of a sudden, I was shipping parts kits out of the back of the university's loading dock supplying these other schools. And then the problem became that they would, you know, assemble them. And I'm putting assemble in air quotes. They put the chips on backwards and they put the caps in backwards. And I was spending more time troubleshooting their designs than anything else. So I thought, no, that's not effective. Let's go find a better way to get these manufactured. So I started selling manufactured boards. Again, totally at cost, no markup at all. And that worked out for a while. But then all these boxes were showing up on the loading dock at the university. And the dean came along and said, you really can't run your own company out of your office at the school here. Right. Okay.

**Dave Jones:** So you were doing this personally.

**Chris Gammell:** Exactly.

**Dave Jones:** Not under the university's name.

**Chris Gammell:** Well, yeah, exactly. We sort of tried to work with the university. But there's a lot of encumbrances when you try to partner with a public institution like that. That is such a nice way to say it. I have to say it. I've had 17 years to practice that one. Yeah, right, right, right. So we got shown the door and started a company not because we wanted to because that was really the only way to keep the thing going. Right. And really didn't have aspirations of doing anything other than serving our students and maybe the area universities. But just by word of mouth with no advertising and no promotions at all, all of a sudden we're in dozens of schools and there's a recurring demand and people are getting mad when we don't have things in stock.

**Clint Cole Of Digilent:** Right.

**Chris Gammell:** So probably 2001 or 2002 we had to up the game and actually preorder and have inventory and hire a couple of guys to work in a warehouse, which was really just a big closet, to be able to ship things when orders came in. And that went on for a couple of years. And then we had a couple of other OEM opportunities that came up to design and manufacture boards for Xilinx and some other companies. And about 2004 or 2005, we had enough cash flow to get more serious. So we brought in a couple of dedicated engineers, a PCB designer, another hardware guy, a software guy, and then started just building more systems and getting into more schools and expanding the program.

**Dave Jones:** So this is a classic bootstrapped company, no investment or anything like that?

**Chris Gammell:** Yeah, 100%. There was no investment at all. It was just me and my credit card. And I think, if I recall, I could be making this up, but I'm pretty sure that after the very first commercial build, I paid back my credit card bill and then from then on we were profitable. We made more than we spent, in other words. Right. Fantastic.

**Dave Jones:** And it's not hard, is it? Great. It's not hard to bootstrap a hardware company.

**Chris Gammell:** Well, it's not. If you find a product that people actually are willing to purchase, yeah, it works out okay.

**Clint Cole Of Digilent:** Yeah. Well, and if it's priced right and everything like that too, right? I mean, Dave, you just did that video about pricing your hardware and stuff like that.

**Dave Jones:** How to price hardware, yeah. And a lot of people were desperate for that sort of information.

**Chris Gammell:** And for us, I know nothing about running a business. So, what we did is we took whatever we were spending, multiplied in the early days by 1.35, which I'm sure is extremely naive, and that was the price.

**Dave Jones:** I just did a video on that, which is cost of goods sold, and explained why to run sort of a viable hardware business, you need 2.5 times the cost of goods sold.

**Chris Gammell:** Yeah, we're somewhere above 1.35. Now, I don't exactly know where we're at.

**Speaker ?:** Right.

**Chris Gammell:** That's good. We learned over the years that that was a little too thin, but for just a couple of guys shipping things out of a closet, it was enough for a couple of years.

**Clint Cole Of Digilent:** You know, if we go up to 1.36, we can have another packet of ramen this week, guys. That's pretty much right. We can have pizza, yeah.

**Dave Jones:** Although, that lower figure you can just get away with if you ship direct, but if you have resellers, then you're screwed. You can't make profit with that sort of market.

**Chris Gammell:** Absolutely. That 35 points was for us. If there was a distributor in the loop, they'd have to have their own.

**Clint Cole Of Digilent:** Yep. Right.

**Chris Gammell:** But you say the ramen. I do remember, and this is two or three years in. So my partner, Gene Apperson, was one of the early hires at Microsoft, and he was there for a bunch of years. And he and I met at WSU here. So he and I worked together for the first, well, 15 years. But I remember about two years in, I came back from a trip somewhere, and there was a new laser printer. And I said, yeah, what's going on? So I had to buy a new printer. The other one broke. And I'm kind of thinking, geez, that's like 500 bucks. And really, did you need to buy a new printer? And it turned out that the old one was just out of toner. And he went and bought a new printer. But I remember thinking, there was the company. So Earl found your stripe, huh? We just bought the – we just lost the company on this printer. But it turns out it was okay.

**Clint Cole Of Digilent:** That's good. Yeah, that's some thin times, I got to say. So how long was it just the two of you then?

**Chris Gammell:** Yeah, I got to remember back. My wife always was helping as well. She was doing the books and the orders and the order processing. And so it was the three of us for probably the first couple of years at least. And it was probably 2003 before we brought in our first actual employee. And in fact – well, my wife is from South Africa. And we had our first baby about that time. So our first employee had to not only pack the boxes and do all the shipping, he had to watch the baby. So she was on the phone one day talking to a customer about something. And Jamie, our first child, was kind of making some noise. So I was – happened to be in the office and she puts her hand over the phone and says to Mike, our first employee, she says, Mike, go shake the baby. Oh, no. Which – yeah, it's a normal thing to just shugle him a little bit in his pram down there in South Africa, I guess. So he's looking at the baby and looking at Fee and thinking, I really need this job. Is this a test? Is this a test? Exactly.

**Clint Cole Of Digilent:** Oh, that's great. But it sounds like Jamie made it, right? He made it through, okay, yeah. Yeah, good, good.

**Dave Jones:** So what sort of products were your first products that you were doing? You said they were hardware development boards. Were they FPGA boards? What were they?

**Chris Gammell:** They were. My very first product – this is prior to Digilant – was a Xilinx 4000 series board. So that's going back a ways. Oh, yeah, yeah. And it had an analog microphone amplifier speaker on it – microphone amplifier on it, sorry, and a speaker amplifier as well. And the thought was that students could do some digital prototyping, but also there was a signal path for an analog signal in and analog signal out, so I could do some DSP kind of things as well.

**Dave Jones:** DSP audio processing is always a good technical example.

**Chris Gammell:** Yeah, and I think having a dedicated signal source that they could wrap their brain around and manipulate in real time was a good teaching thing. So then from that only – we made like 30 or 40 of those for just my class. The first board that really made it out of our little department was – we call it the XLA board. And it was a – boy, the first Spartan FPGA. Oh, wow.

**Clint Cole Of Digilent:** Okay.

**Chris Gammell:** Yeah, and it had – it was the first board with an onboard programming circuit. So we reverse-engineered Xilinx's programming cable. I don't know if I should say this – oh, well, too late. But we reverse-engineered theirs, stuck it on our board. Nobody said anything. So that was good because you only needed the board and a cable and nothing else.

**Clint Cole Of Digilent:** Nice. See, but that's good though too because that means that ultimately that – what they really want is to sell more parts. So what – I mean, I'm sure that's in spades, right?

**Chris Gammell:** Well, it just made it really convenient to own and to use. Yeah. And then it had a breadboard on it so you could put little like whatever 7400 circuit chips in there or something. And then nuisance things like buttons and switches and LEDs that everybody needs and wants, but you didn't want to make them wire it up in a breadboard. Right.

**Clint Cole Of Digilent:** Right.

**Chris Gammell:** And that sold maybe a couple thousand of those.

**Clint Cole Of Digilent:** And did you have a relationship with Xilinx from the beginning? I mean, like I said, it seems like this is a service. This is something that I would think a lot of companies are doing in-house these days, you know, dev boards and stuff like that. There's a lot of chip vendors doing that kind of thing. So what was the relationship like?

**Chris Gammell:** Well, so we – I knew the guy from previous work that was running the university program at Xilinx. So I called him up for our second board and told him what we were up to and would they be interested in helping out. So they gave us some really good pricing to help us along. I think our total bomb cost on that board was something like $55 or $59. And we retailed it for $79. So we kind of violated our $1.35. We were a bit low then. Wow. Marketing expense. It's getting the word out, right? Exactly. That's what we thought. And again, we moved maybe 2,000 of them mostly to universities up here in the northwest. But I'll tell you, I flew down to meet those guys for the first time to show them what we were up to. This is probably 2002. And when I walked through the cubicle farm there in Xilinx and, you know, they had – I don't know, but they got 5,000 people down there in San Jose back then. And they had a four-building campus. And I was walking through one of the buildings and saw our board framed hug on somebody's wall. Really? Yeah. Wow. That was my thought. Wow. That's what I thought. So I'm thinking, wow, they must like us. You know, we must be on to something here.

**Clint Cole Of Digilent:** And then it was – right next to it was your picture with a target on your forehead or something like that. So it wasn't – it actually was that though that like they were just really proud that it got out there and it was –

**Chris Gammell:** I came to find out after the fact that really they were suffering from the same thing I was, that they really couldn't find the right demo board either to recommend to students and to universities. Yeah. And so when we came along and designed one specifically for teaching and learning, it sort of resonated with those guys. And I think their university program was just getting formed. And so they could kind of rally around this board that was ideally targeting their student audience as well.

**Clint Cole Of Digilent:** Right. Right. Right. Because they've got to teach all the software stack and everything too. I mean like that – people have used the Xilinx tools or they know it's – you know, it's not trivial, right? So getting the hardware out of the equation is great, you know?

**Chris Gammell:** So it's just kind of a synergistic thing that they had a need at the time we had a solution.

**Dave Jones:** Do you think that one of the reasons for your early success was the low cost of the boards?

**Chris Gammell:** There's no doubt about it. Right. So my observation – and every bit is true today – when I was a student and when I was inflicting stuff on students, the model – Great verb. Great verb. The model was that they'd come to these sterile, brightly lit labs with these lab benches and stacks of equipment. And they'd sit there for two or three hours a week and they would do, you know, experiments. And again, I'm doing air quotes. Really, they'd follow a recipe. They'd type in some circuits. They'd do a simulation. Then they'd program a board and get some results. And, you know, the last thing that happened in that environment was learning. I mean, their goal is to not look stupid in front of their peers and then to get out of there and go do whatever. That's what I do at home.

**Clint Cole Of Digilent:** There's a lot of beer drinking, I'm sure. Yes, indeed.

**Dave Jones:** So could you say that it is possibly – could not – well, it may not be a bad thing to actually your first product. If you're looking to get into this hardware business, you might have like a razor-thin margin just to get some traction. Or, you know, like I know it can work either way. You know, you either go like, you know, 2.5 or three times cost of goods sold right up front and, you know, bugger this, you know, razor-thin margin rubbish. Or, you know, is it worth doing that to get a foot in the door?

**Chris Gammell:** Yeah, I don't know. I mean, it could be that we left quite a bit of money on the table.

**Dave Jones:** Right.

**Chris Gammell:** And that we stunted our own growth because we sold too cheaply. I guess there's no way to know that.

**Dave Jones:** Right. So with hindsight, you don't know that?

**Chris Gammell:** No, I suspect we could have asked a little bit more for it. But on the other hand, it's pretty clear to me that when we went out to universities and said, you know, you've got to change your model. Instead of you guys spending $20,000 for a design seat for 20 stations in a lab, you've got to instead force your students, each one of them, to buy a board that they own and take home with them. You know, that was a big change already. Right. And if that board came with too high of a price tag, they might have just said, well, no, it's too much, too new, too different. So there's no doubt the low cost helped early adopters be early adopters.

**Clint Cole Of Digilent:** It sounds like the low cost almost acted as your salesman, right? I mean, like that made the sale easier.

**Chris Gammell:** It did. I think if we – yeah, and we never – I mean, now we have a sales force. But up until 2012 or so, we had zero people actively selling.

**Clint Cole Of Digilent:** It was you, I'm sure, you and Gene together, right? Yeah.

**Dave Jones:** Although you've still got now quite reasonable prices on things. They're still not – you know, they're not National Instruments prices, for example. They are DigiLent prices, even though you're now the same company, which we'll get into, I'm sure. But have you found that it's just like the higher volume brings the cost down? What is – like obviously you're making more in margin now. You're at a big company. There's lots of employees. You've got to pay real bills.

**Chris Gammell:** Well, two things. You know, I'm not sure that I have a lot of confidence what a margin or a multiplier needs to be for a technology company supplying gizmos into markets. You want, of course, the highest multiplier you can get.

**Dave Jones:** Oh, it varies so much. Oh, yeah. No, it totally depended upon the market you're in and your competition, all sorts of stuff.

**Chris Gammell:** Absolutely. So somewhere between, you know, on the low side, maybe 2X, maybe 1.8X. On the high side, maybe 3X. Somewhere in there is a sweet spot. So for us, one thing we had to do before we were acquired by NI was we had to always be price competitive for a couple of reasons. One is we knew we were selling directly to students and we were competing with, you know, beer money and pizza money.

**Dave Jones:** Right.

**Chris Gammell:** Tough call. Yeah, exactly. If we're over $100, it's just kind of a non-starter in a lot of cases. And the other thing is we had to be long-term stable. If we were going to convince a professor to move an entire curricular program over to our hardware, they had to know it was going to be there year after year after year.

**Dave Jones:** Of course.

**Chris Gammell:** So that forced us into some longer-term agreements with some manufacturing chains that we put the diligence in ahead of time to make sure that they were going to be low-cost and stable over the years.

**Dave Jones:** So you had to go to the likes of Xilinx and Altera and go, hey, give us a written guarantee. You're going to keep making these chips at this price.

**Chris Gammell:** We never did that. I mean we sort of tried, but it was pretty clear that they weren't interested.

**Dave Jones:** Because you weren't big enough. We weren't big enough, yeah.

**Chris Gammell:** There was no reason to invest in us like that. So instead, we went to the Far East and spent some time over there interviewing and working with various technology manufacturing companies and found one early on that we've partnered with ever since. And in fact, we co-invested with them to help grow the capability. But those guys have consistently let us ride about the optimal, I guess, pricing curve. So we're able to produce hardware substantially at the same price that guys that are doing 100,000 or a million PCB motherboards do. We're sort of in that same area of price performance for manufacturing facilities. So because of that, we were able to have a pretty good idea what our costs were going to be from build to build and from year to year. And we gently nudged up our margins, but we never went to an extreme. And after the acquisition, that production pathway was pretty tried and true. And we knew how many people we could employ based on our income and how many new designs we could start based on our income. And we were able to largely grandfather that in to our current business practices as well. Even though the NI Corporation probably wouldn't want to work at the margins we do, they gave us the latitude to do that.

**Clint Cole Of Digilent:** Got it. So in the early days, too, I have to ask, I mean, did you have – how did you survive that then? I mean, like you said, there's razor-thin margins. Were you paying yourself or were you kind of – I know that you said you sold your past company. Was there – did that affect things as well or how did that all work? Yeah, yeah.

**Chris Gammell:** Very good point. So when I sold the past company – well, I didn't sell it. We hired a guy who just sold it. I'm sure it was the right thing to do. Oh, the selling guy. Yeah, yeah. We know him. Yeah, exactly. Anyway, I had enough – I probably got, I don't know, three, five times manual salary kind of thing in one net payment. But it was enough to lessen the fear of trying something new. It wasn't enough just to stop working by any means. Right. But on the other hand, I thought if I try something and it fails, yeah, I've got a little attitude. I could try something else. So that very much was helpful. So I took no salary from Digilin for, boy, five years or something like that.

**Clint Cole Of Digilent:** Wow.

**Dave Jones:** Okay.

**Clint Cole Of Digilent:** And it was only – So that also enables those lower margins.

**Clint Cole Of Digilent:** But then that also helped you do better – like get that runway going and really build the kind of product you wanted to. You didn't have to take any investment. So then you're in charge. That's great.

**Chris Gammell:** And that's very clear that that was a huge enabling factor.

**Clint Cole Of Digilent:** Yeah.

**Dave Jones:** At any point in the stage, do you think you might need or you should seek out third-party investment in the company, VC funding or anything like that?

**Chris Gammell:** Well, absolutely. So in fact, it was about 2011. And at that point, we designed our 250th product. We'd shipped about 750,000 circuit boards. Wow.

**Dave Jones:** And your company was about nine years old at this stage?

**Chris Gammell:** About nine years old. Yeah. Yeah, essentially. But we were still growing very nicely, but it wasn't explosive. And we did a little analysis, I guess.

**Dave Jones:** How much turnover are we talking about? How many millions per year?

**Chris Gammell:** I think at the time we were flirting with 10 million.

**Dave Jones:** Oh, okay. Right. So yeah. Yeah.

**Chris Gammell:** But our expenses were most of that. Exactly. Yeah, yeah. Exactly.

**Dave Jones:** It's not like you were making $9 million on that. No, no.

**Chris Gammell:** There's very little net, which is part of not knowing how to run a business.

**Dave Jones:** Exactly.

**Chris Gammell:** But we – I lost my train of thought. What was the question?

**Clint Cole Of Digilent:** I was going somewhere. 2011, how you would – oh, venture capital.

**Chris Gammell:** You were seeking our VC. Yeah, there you go. Possibly seeking it out. So we had pretty good volume going. We had pretty good penetration, but there was never this explosive growth. And we were spending about a percent of our income on marketing. And that included advertising in various magazines and going to conferences. So we just weren't spending. And we realized that we were crippling ourselves.

**Clint Cole Of Digilent:** Right. We should say that is low, right? Yeah, it's low. People would be like, oh, why would you spend any money on marketing? It's like, no, that's pretty low.

**Dave Jones:** One percent is low. But you're already getting – you're already $10 million in sales. You're a successful company. Yeah, yeah. It might have been more like $8 million. And it's a niche market. So it's almost as if you don't need to spend much on advertising. Or is that a falsehood?

**Chris Gammell:** Well, we thought at the time we were probably in maybe – I don't know, maybe 1,500, maybe 2,000 schools worldwide out of 10,000 or 15,000. And a lot of those would buy one batch of boards and we wouldn't see them again for years. So we knew students were buying and the labs were. So we thought we were maybe 5% penetrated. Okay. And there was a long way to go. And we just weren't going to get there strictly by organic word of mouth growing. So we thought we've got to bring in enough differential money that we can go hire professional marketing people and salespeople and try to grow the market. And we felt at that point even though our net was thin, the cash flow probably would support diverting some of that. But we really thought we need to bring in some outside money to take that next step. So we were kind of in the mood for bringing in some funding, maybe selling some equity in the company to find a marketing or salesperson to spur that next phase of growth. And during that period of looking for some partners is when we mutually found, and I and Digilent found each other.

**Clint Cole Of Digilent:** Oh, cool. Oh, right. That was around the time. So that basically led to, so it was 2013 that the actual purchase happened, right?

**Chris Gammell:** Yeah. We started, so I was looking, I'd met a couple of financier types, folks I'd known from earlier on in Seattle and San Francisco. So I kind of put in the word out that we're in the market for maybe, I don't know, a million or two of financing. You know, we'd sell some amount of the equity in the company and we'd use the money specifically for bolstering marketing and sales activities within the company to try to grow the market more quickly. And I was probably a year into that and getting closer to striking some deals with some folks when we had a relative chance encounter with a guy from NI and then the discussions kind of took root from there.

**Dave Jones:** Right. So it was just a chance encounter. It's not like you seeked them out or they seeked you out.

**Chris Gammell:** No, in fact, I don't think any of this is off limits to talk about. So we were in the conference room here in our building and one of the sales guys that had assignment for this area of the country from NI was visiting. And at the time we were doing some OEM work for NI. We supplied them a couple of boards. So he's kind of checking on that and just kind of seeing what we were up to. And we were completely open. I mean, we were telling him exactly what our products were, what the specs were, what the costs were, where we were intending to go. We weren't really competitive with them. But on the horizon, you could see if our products got a little higher performant and their products got a little more student focus, that there might be some overlap and some competition. But we were real open about that. So we talked and he's heading out and we're walking down the hallway. And I said something to the effect of, you guys should just buy us.

**Dave Jones:** Right, just as an offhanded comment. So you are a salesman, Clint.

**Chris Gammell:** He kind of laughed a little bit and then he kind of turned around and said, really? And then the conversation started from that point. And really, it turned out to be, I think, a very good match.

**Dave Jones:** Totally, yeah. It was one of the better, when I heard the news that, and I bought Digilet, I thought, that's smart. That's a good move.

**Chris Gammell:** And I went down and visited a couple of times and they've just got a great culture. I mean, I've been to all the high-tech companies. After we worked with Xilinx, we started working with other companies, TI and ADI and Cypress and just Linear and all those guys, Cypress. And so I do a lot of site visits. And, hey, you kind of walk around the cubicle farms and get to know people a little bit. And of all those places, walking down through NI, it was just a different vibe. I mean, everybody there seemed to be totally engaged and excited and having fun. And it was almost like a big dorm party up in the top of the building center.

**Clint Cole Of Digilent:** It helps that it's in Austin. Come on, that does help a lot. Yeah, indeed. Yeah, right.

**Chris Gammell:** And then the people that were just very open and very sincere in our conversations from day one got right to the core of the issue. And there's a lot of passion on the part of the people that we work with at NI for the same things we were passionate about. I mean, they really wanted to go out there and make a difference in younger people's lives to make engineering more relevant and more fun. And that's what we were about. And so the conversations would go on. They would schedule an hour meeting. And three hours later, we'd still be talking about the stuff and feeding on each other's ideas. So it became a very kind of easy decision at the end there. That's great. That's really good.

**Dave Jones:** But ultimately, they're really two different companies from a business and cost point of view. I mean, NI is famous for designing really great hardware and software, but it's ridiculously expensive. And you guys are known for producing real good quality bare bones stuff at bare bones prices.

**Chris Gammell:** Yeah. And I think that marriage is kind of what makes it work because I used to work for big iron companies like that, Hewlett Packard and some others. And I think that, well, the last place I worked was a place called Physio Control in Seattle that also did defibrillators. And we did an analysis there. And it cost about $300 to ship an empty cardboard box.

**Dave Jones:** Oh, awesome. Wow.

**Chris Gammell:** And when you start there, and I'm sure that's pretty much the case at most of those big iron companies. When you start there, because you've got so many built-in expenses, it's really hard to get a consumer-level shrink-wrapped product for sale on a web page and make money at it.

**Clint Cole Of Digilent:** Right. Not to mention power structures and people with, you know, not in a negative way, but just, you know, companies being companies, that there's people that are usually interested in things operating the same way they always have. So if you're making a big shift to consumer type things, that would be a very drastic upset type thing.

**Chris Gammell:** Well, yeah, that and they just had a different kind of machine. I mean, they have lots of salespeople and lots of product line support people and lots of technical support people. And something's got to pay for all that. But then their markets were selling to other bigger companies. And all of that machinery aided in the process. But, you know, we were this little upstart selling off a website shrink-wrapped products that really didn't need, or at least we hadn't cultivated that environment where we needed that kind of support. So I think when we started talking with NI about an acquisition, that was part of the realization that it would be difficult for them to, for any big company like that, to really get down to a consumer-level shrink-wrapped product at whatever margin we can work at because their systems aren't designed to do that.

**Dave Jones:** Yep. It's just almost impossible for the company to do it, isn't it, for those large companies to do it? They can't…

**Chris Gammell:** Well, I think so. And I'll tell you, I've become pretty much impressed, I guess maybe convinced is a better word, that there's a reason that there are startups. And it's because startups are little startups.

**Dave Jones:** They're lean and mean.

**Chris Gammell:** Yeah, and they can take risk. And they can go out and give a new technology a shot. And if it works and it can be commercialized and monetized and it can grow up and can be a part of something, then it gets acquired and the economies maybe change. But it's still, you know, that DNA, that product line is now part of something bigger. Right. And a big company, you know, they've got engineers and they've got priorities, they've got roadmaps, and their resources are committed and they really can't afford to – it's not their business to take these risky steps out into unknown territory. Right. So as these startups are out there doing that, this kind of cloud of gnats, if you will, buzzing around, you know, taking advantage of all these opportunities, occasionally a few of them grow up and those are ripe for being consumed. A lot of them just don't make it and they just die and go away. But there's really no other way to do it.

**Dave Jones:** Were you scared that NI would totally gobble you up into their system and that would be the end of it? Or were you confident that they'd keep you as a separate entity because they're smart enough to know that they can't – their systems can't do what you guys do?

**Chris Gammell:** Yeah, very much the latter. The people that we worked with at NI in the early days were pretty upfront about that. And, you know, when you work with people and you look them in the eye and stuff, you can tell when they're kind of towing the company line. Yeah, you're right. And when they're sincere. And these guys just oozed sincerity. I mean, they really wanted to be impactful in the lives of people trying to learn engineering, you know, to make the world better for all of us kind of thing. And they were sincere and it turns out that they were sincere. So I didn't really have to – it never was intuitive to me to worry about it. It just seemed like they were straight shooters and they were. Got it.

**Clint Cole Of Digilent:** So they also have an educational program, though, too, right? I mean, so is it kind of coming at it from different areas? Like they're kind of more towards the scientific side of things and you guys are more towards the electronic side of things? Is that kind of the split or where's the split?

**Chris Gammell:** That's a good way to put it. So their tool base with LabVIEW and their hardware is very abstract. I mean, their goal is to take a thing in the world that needs to be sensed or controlled and make the act of sensing or controlling it very abstract and kind of fiddling with dials and stuff on an application. And mostly it's because their main market were either engineers or maybe even non-engineers who didn't want to be bothered with the details of interconnect and of setting IOs up and stuff like that. They wanted to get right to the meat of the matter. They wanted to get the data and do their algorithms on the data and do something purposeful with it. So they set up a system where you could design and deploy custom instruments very quickly. That's different than learning how circuits work. And we set up to teach people about circuit nodes, resistors and – sorry, resistances and voltages and currents.

**Dave Jones:** And circuit building blocks and how it all –

**Clint Cole Of Digilent:** Switching behaviors and that comes down. You guys are making engineers that can go and work and build the NI tools, right?

**Chris Gammell:** Well, that's – there you go. That's exactly right.

**Dave Jones:** Yeah. Whereas NI is more focused on producing system-level people perhaps for want of a better word. Who can design systems and solve problems at a higher level. But they can't design electronics, you know.

**Chris Gammell:** Yeah. Yeah. So if you looked at a university environment, you'd tend to find NI products maybe in bioengineering or chemical engineering. Right. Yeah. Mechanical engineering. Places where it's – the point isn't to learn how to design circuits. It's to use circuits as a tool to do whatever your experimental thing is. Yeah. Right. And you'd find us in the EE and computer science departments where the point is to learn how circuits function.

**Clint Cole Of Digilent:** I remember I had a mechanical engineer friend who was asking me about how to do something, you know, just like measure – I think it was a force sensor. And he's asking me, how would you measure it? I'm like, oh, well, you know, I'd get like an instrumentation amp and I'd do this and this and this. And he's like – and he's just like, I'm going to go use national instruments. And that's what it was. And he was done in, you know, an hour versus me designing a board. And okay. Yeah, absolutely. That's what he wanted to do. So that kind of was a good indication. And there's nothing wrong with that.

**Dave Jones:** That is – like you just want to get a job done. They're in two entirely different things.

**Chris Gammell:** I just had this conversation earlier today with somebody. So back in probably 91 and 92, you know, we were consumers of NI products back then. So when we were doing the defibrillator, again, this was the first portable thing. It needed to use lithium batteries for weight and longevity and cost and all that stuff. But nobody out there was saying, oh, here's a lithium battery that has these specs and it's going to last five years. So we had to buy thousands of them and test them for months. And to do that, to cycle them, to load them, to meter them, you know, it was a big – it took up, you know, I don't know, 50 square feet in a lab.

**Clint Cole Of Digilent:** Right.

**Chris Gammell:** Because you were doing big battery stacks because of the high voltage of a defibrillator.

**Clint Cole Of Digilent:** Is that right?

**Chris Gammell:** Battery stacks, not super high voltage. We used flybacks to multiply it up. Gotcha. But still, they were – I don't know what they were. I don't remember, like 9 volts or 12 volts. But it was relatively new and we were doing our own custom battery packs and we just needed a lot of data. And those things blow up too, right? I mean, like that's another thing. Which is pretty cool in the old days to watch them blow up. They were spectacular.

**Dave Jones:** And that's the market NI own because I come from a production test system background. Yeah, exactly. You don't roll your own hardware if you don't have to. You buy – you know, budget usually isn't a problem. You buy your $5,000 National Instruments card. You use LabVIEW or LabWindows CVI and you build these high-level things, you know?

**Chris Gammell:** That's exactly right. So if we had to not only design the test system for the batteries as well as do the test, it would have put us six months behind the curve. Of course. And instead we bought NI stuff and a month later we're up and running. And that's where NI fits. And they were indispensable. And we could not have done what we did do without using that kind of a tool.

**Clint Cole Of Digilent:** Yeah, that's good to have that reference point too when you were talking to them. So that's important to have that.

**Chris Gammell:** Well, indeed. Knowing how they fit in the ecosystem of engineering design, yeah.

**Clint Cole Of Digilent:** For the longtime listeners, they will know that we've said some not great things about the programming language of NI and stuff in the past. You know, because it's a little bit clunky to me at least. And I think there is reason to get down in the lower level stuff. But like Dave said, I mean, it's just –

**Dave Jones:** Horses for courses.

**Clint Cole Of Digilent:** Right.

**Dave Jones:** Right. You choose the right – it means choosing the right tool for the job.

**Chris Gammell:** Yeah.

**Dave Jones:** And NI is the right tool for certain jobs.

**Chris Gammell:** That's exactly right. And if I did this whole thing again and I was – if I needed to have a test and measurement or even an environment that could stimulate parts of a circuit and get me data back quickly and that was on path to building a product, I think they're still the best solution out there for that because they're so customizable. And, yeah, there's some learning curve involved. But when you go through it, you can be pretty productive and create new instruments relatively efficiently and at a relatively good cost.

**Clint Cole Of Digilent:** Yeah. It's very top-down. Like when you need to dig in and customize something, you can. So that's good. Yeah, exactly. So I wanted to get back to the education side because you said you were a professor and obviously you got into this because you were big in the – you saw a need in the educational space. I mean what are your thoughts on education these days? What do you see and what's going right? What could go better?

**Chris Gammell:** Yeah. Well, that's a big question. But starting kind of in the middle, I still think today there's still a bit of a looming crisis. I don't think that we're producing too few engineers for the economy right now today. But if you look at the international production of skilled engineers and if you look at the kinds of jobs that are available now and where all systems that predict future jobs think the market is going, there is a net deficit of skilled engineers coming out of major universities. So I don't have numbers from 2015 but from 2014 and 13, the U.S. was going to graduate about 25,000 engineers with degrees in EE and computer science where those people were doing embedded programming and stuff that would be involved with product design.

**Dave Jones:** That doesn't sound like a lot.

**Chris Gammell:** It's not a lot.

**Dave Jones:** For a country of what, 350 million?

**Chris Gammell:** It's not a lot. And if you look at the USBLS, the Bureau of Labor and Statistics was estimating there's like 900,000 jobs in those same fields. Wow. So we're not even producing enough to cover retirement and attrition. Right.

**Clint Cole Of Digilent:** Wow. That's a massive shortfall. I've always said there's a huge risk if like the stock market does really well because there's a bunch even still from 2008 that like they were just holding on. You know, all these older engineers that were just like, ah, it's not the time yet. It's not the time yet. And when, you know, if there's something big happened and there was a huge spike in the market, they'd all be like, yep, time to retire. Yeah. That's right. That's right. And we're screwed.

**Chris Gammell:** So it's a bit of a fragile situation. So here in the States, we're doing two things. We're importing engineers and exporting jobs. Yeah. Maybe that's OK for, you know, this decade or two in the States because the world will kind of equalize. But no, because the same thing's happening in Australia and in Western Europe. In fact, the same thing's happening worldwide. There's this kind of perpetual shortage. Now, we're doing OK because the tools are getting so much more powerful. I can sit at my desk and use free or cheap tools and low-cost prototyping hardware. And I can do a job today that would have taken 10 people 10 years ago. Yeah, totally. So we're making up for that shortfall. But that's going to stop. And I think there's going to be a deficit of engineers. So part of my mission and passion, I guess, is to make engineering more relevant and more vital and more fun, I guess. So more people at a younger age are thinking, you know, maybe I'll give that a shot. Maybe I should go be an engineer.

**Clint Cole Of Digilent:** So you said skilled engineer. How do you define a skilled engineer as well? Because that's another important piece, I think.

**Chris Gammell:** Well, I think when I hire an engineer, and we hire a fair amount here, what I look for is people that have exercised the creative process and kind of owned the design process. So somebody who you can say, you know, go solve this problem. Go make a thing to do to meet this requirement, to meet this need. And they kind of get it. And they go out and they pick up whatever tools are required. And they use the tools. They can monitor their own progress. They can simulate or they can validate and stimulate and validate their own work. And they can correct themselves in flight. And they can get to the point where, OK, here's this thing you requested. And it meets your specs. And not a lot of people can do that. And the way you get there is by a lot of practice. It's like anything. If you're going to play basketball, you don't just pick up a ball one day and start shooting three-pointers. Or sit in a classroom and have someone tell you how to do it, right? Yeah. You just can't – you couldn't take a lecture on riding a bike and jump on a bike and ride it. You've got to practice it quite a bit. And that's kind of the point behind Digilent to make the job of getting that experience and that hands-on practice to make it easier and less expensive for more people.

**Dave Jones:** It almost sounds as if you want a jack-of-all-trades.

**Chris Gammell:** Well, I think I want people who – Or is that the wrong term? No, it's in the right direction. I think you want people who have genuinely pitted themselves against a real problem, who have for themselves found their own limitations, and who have themselves worked through them by finding whatever resources or inputs they need to kind of shatter their own limits and take the next step. And go out and find the person to talk to or find the information or do the simulation or build the circuit and test it. Stay up until three, four, five in the morning every night for two weeks in a row until you demonstrate conclusively to yourself that you know exactly what's happening. And once somebody goes through that process of having that creative desire and then they have the tenacity to see it through and then they get the reward of having felt challenged to the point of maybe they wouldn't make it but then they do make it, it's a very rewarding thing. And they kind of get all turned on and excited and they're ready to do it again and again. And when you encounter those people that have had that experience, when they've found their limits and worked through them and found success kind of in spite of them, that it's a very easy thing, I guess, to find that excitement in somebody and to share that with them.

**Dave Jones:** It's all about the enthusiasm.

**Chris Gammell:** Yeah, it really is.

**Dave Jones:** Because everything's out there today. It's not hard. You don't have to be a genius engineer to do all these things. You just have to have the enthusiasm and the tenacity is the word you use to keep at it. Because all the information's out there. It's at your fingertips. It's not rocket science.

**Clint Cole Of Digilent:** I think of people like Ben, Krasnow, and Jerry too where it's just this unknown problem. And they approach it very scientifically but they just keep trying new things. That's what always hits me about their videos. Well, Ben still makes videos. Jerry's off doing her own thing now. But that continual – like you said, I'm not satisfied yet. I don't quite understand this yet. That is a huge piece of success – an indicator of success.

**Chris Gammell:** Well, it is. And I'll tell you, the best engineers I've worked with, they have this innate ability. And I don't know where it comes from because I don't have it. When they're confronted with a unique problem, they can kind of sense where their knowledge is the weakest and where the design is most at risk. And their natural tendency is to head directly to that point and roll up the sleeves and dive in and figure out why don't I know what's going on and not quit until I do know. And it doesn't – they'll pull out all the stops. They'll spend hours researching and measuring and stimulating and testing and talking with everybody. And come on, move on. It's working. Well, no. There's still this thing going on I don't get. And I admire those people and I don't know where that comes from but it has to be some formative experience when they were younger that they got some positive feedback from really trusting – from knowing something to their own internal sense of satisfaction. So they didn't get an A on a paper. That wasn't good enough. I mean they knew they knew it and they weren't satisfied until they knew they knew it. And that's what I want to cultivate. That's what I'd love to have more people feel the satisfaction of getting there in their lives because I don't know that I've ever gotten there. But the people that have I think are just really happy and successful and full of life and full of energy.

**Clint Cole Of Digilent:** So now the $64,000 question, are colleges teaching that? And some question, is it even possible to be taught? I mean like maybe that's too hard of a question on the colleges but –

**Chris Gammell:** Well, no, I think there's widespread recognition that the current state of formal education for engineers – well, for anybody really is largely nonfunctional. And it really wasn't designed to produce creative, thoughtful, introspective, tenacious engineers. It was designed to produce conformal, interchangeable people. Yeah, that could be plugged into various jobs. So I think this whole – the whole notion of kind of free-range engineering and flip classrooms and MOOCs and all that stuff are all in the right direction. What it all is pointing to is telling every individual student out there that really it's up to you. I mean the institution is there to provide some guidance and a pathway through this complex body of knowledge. But really it's up to you. So here's some tools. Here's some resources. Here's some people you can consult with. Take advantage. Challenge yourself. Go learn. Go pit yourself against these problems. Go create things and let us help guide you. So I think that's where universities need to go and kind of where they are going. I think they could get there more quickly.

**Clint Cole Of Digilent:** By buying more digital projects.

**Chris Gammell:** I agree. Your independent analysis would be marketing. That's right. Are you still teaching? I am, yes. Do you still teach? Yeah.

**Clint Cole Of Digilent:** So what are you teaching?

**Chris Gammell:** I teach – at Washington State University, I teach an entry-level EE class. It's mostly digital but it kind of covers some circuit design stuff and electronics a little bit and some coding styles a little bit. It's kind of a broad survey class with emphasis on digital design. So we do combinational circuits and state machines and that kind of stuff. And then I typically teach a junior-level digital design class as well where we'll do maybe an embedded processor or an audio codec or a video codec or just kind of constituent pieces of larger digital systems to emphasize use of modern CAD tools. So timing analysis and floor planning and all that kind of stuff.

**Clint Cole Of Digilent:** Gotcha. Yep. Yep. That makes sense. So what are the students – I mean like tell us about – I mean you don't have to tell us about individual students but what's your general feel about people entering these classes or just the type of students?

**Chris Gammell:** So the classes – my class size for the entry-level class range from maybe on the low side 50 or 60 students up to maybe 100, 120 students depending on the semester. And it's pretty consistent that maybe 10 or 15 students, not percent but 10 or 15 students, really get it. And they're energized and they're having fun. And they'll come up and ask, you know, I could do these stupid labs you posted but can I do more?

**Dave Jones:** Right.

**Chris Gammell:** Well, sure. Yeah, go nuts and have fun with it.

**Dave Jones:** So is this a compulsory class? It is. Or is it – right. Okay. Yeah. For all – That is why the number is a bit low I think.

**Chris Gammell:** For all double E and computer E students, it's compulsory. Computer science, it's optional. There will be another 30 or 40 that are not sure why they're there and they kind of show up to half the classes and they kind of – Right. They just phone it in. Yeah. And then there's another – the bulk of them, the 50 or 60 in the middle are more motivated but they're not sure it's for them. And those are the ones that I'm most interested in appealing to by showing that it's a vital kind of relevant thing to them. And there is this kind of intrinsic goodness to it. When you solve a problem you didn't know you could solve and you get to the end, that there is a personal emotional reward that comes along with it. And it's worth it if you stick with it. There's dopamine to be had, kids. Yes. Exactly.

**Clint Cole Of Digilent:** Exactly. Engineering is the best drug. Yeah. Exactly. It's a hard sell.

**Dave Jones:** But no matter what you do, I mean, some – you can have the best student but they may not just give a rat's ass about digital. They may be off in some other area of interest.

**Chris Gammell:** And that's great if that's the case. And I'm getting more leniency. I think most programs are getting more leniency to deal with people like that. And again, you can tell. It's really hard to fake that. And if they're sincere and they just really – sure, I'm in your class, but I really want to go make quilts. I just want to quilt. You kind of find a way to help them because they're sincere and they're genuinely human to human asking for your help. I read about FPGA fabric. Like this is not what I signed up for. Yeah. Exactly. Exactly. Exactly. And the other thing I kind of like about this – and I don't know if I can sell this or not, but I'll give it a shot and see if you guys buy it – is that I think people just don't appreciate how to think and the joy of thinking. And it's – I guess – Chris, you're in the States, aren't you? Yeah. Yeah. I'm in Ohio. Yeah. So you're surrounded by Americans. I think there's – it's just too easy to not critically think about a lot of aspects of life. And one thing I think we can do with these kinds of experiences, these kind of maker creative experiences is convince people that if you think and if you create and if you honestly own a problem and a solution, well, you develop a way of looking at the world that's more data-based, that takes inputs, applies a more rigorous function to those inputs, and you reach conclusions based on a process that makes sense, and then you act in that conclusion. And really, engineering is a proxy for that, but you could equally apply it to, say, choosing your next leader or to which bathroom people ought to use or a myriad of other social problems that are maybe off topic. But it still involves thinking and data.

**Dave Jones:** It involves reasoning and – Right. Reason. It's an important school.

**Chris Gammell:** Reason is a very thing.

**Clint Cole Of Digilent:** Yeah.

**Chris Gammell:** Yeah. So I'm hoping if education in the early days gets more rigorous that people will naturally develop better thinking skills as well.

**Dave Jones:** Do you think there's a need for classes like that in either high schools or universities like reasoning skills? Is there anything like that being taught?

**Chris Gammell:** Well, no. And that's my particular passion actually is taking all this and pushing it down into high schools and middle schools and even grade schools. And I approached it like you were saying, Dave, initially, how can you get people to engage in thinking and provide feedback, meaningful feedback, to let them know that they were thinking correctly? Right. And that's hard to do. You know, you can't tell them to go write an essay and say, no, I'm sorry, you didn't think enough. You know, F. You kind of have to say, oh, good for you. You're creative. You're thoughtful. You just – what you have to do is give them a meaningful problem where success and lack of success is evident to them as well as to everybody else. So they have to solve something or they have to do something that has a solution that's a little bit more objective.

**Clint Cole Of Digilent:** So like lock them in a room and they have to kind of MacGyver their way out of it or something.

**Chris Gammell:** Well, yeah, that kind of thing. And to do it, they've got to employ all the thinking skills, but then they know when they're successful and so do you. So do they. And I don't know of any other way to encourage and enhance and mold the ability to think creatively other than those kind of experiences.

**Clint Cole Of Digilent:** Yeah.

**Chris Gammell:** A little bit of stress.

**Clint Cole Of Digilent:** I mean stress is important and it definitely helps to engage the brain and stuff like that. But, yeah, there's different types of stress as well.

**Chris Gammell:** Well, yeah. And, in fact, I tell my students that about every third or fourth lecture, I'll end on a cliffhanger. You know, I'll go halfway through an engineering problem and say, can you solve it? And, of course, they're all just running home to go solve it. But I tell them, yeah, I bet if I locked you in a trunk and gave you two hours or you're going to die, you'd solve it.

**Clint Cole Of Digilent:** Right.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** We've always said here on the podcast, year after year, we say it all the time, engineers thrive. They do the absolute best when they're confronted with a deadline. You know, a trade show. The product must be finished. Buy this trade show. We have to do it. And engineers pull miracles out of their ass.

**Chris Gammell:** Well, they do, yeah.

**Dave Jones:** It's amazing.

**Chris Gammell:** I tell you, and what worked for me when I was going through all this stuff was I could visualize a solution. But I didn't know how to get there and that used to drive me nuts. So my motivation was getting beyond my own limitations. I was motivated not to be as stupid as I was at the time I was conceiving of the problem.

**Clint Cole Of Digilent:** Lowering stupidity. I like this. Yeah. It's good. There you go. Life goal. Lower stupidity. All right. If I just do that, I'll be in good shape.

**Dave Jones:** Wasn't the DigiLent slogan beyond something?

**Chris Gammell:** Beyond theory, yeah.

**Dave Jones:** Beyond theory. Right. Yes. That's it. Is that still the slogan?

**Chris Gammell:** I think we moved away from that. Right. But the thought was there that, again, the market we were trying to convince to be our customer was the traditional university market, which was dominated by doing paper homework and simulations. Theory, yeah. Yeah. And no real application of it.

**Dave Jones:** Have you ever caught any – copped any backlash from lecturers going – From the Ivy Tower? Yeah, from the Ivy Tower. No. It's all about the theory. None of this practical rubbish.

**Chris Gammell:** Yeah, absolutely. In fact, a lot of it came from my own institution here but also from other places. And the objection was typically we're not training technicians. We're not training people to go out there and be slaves for actual engineers. We want – yeah, in so many words, that's just a pile of horseshit. I mean –

**Dave Jones:** Did you try and convince them otherwise or did you just throw your hands up and go, no, I'll move on to somebody who gets it?

**Chris Gammell:** I try to convince but pretty soon you realize that what you're dealing with is their own weakness and their own limitation. Right. And you just can't ask people to – in a particular conversation to realize that and get beyond it. It takes months or years of gentle nudging and cajoling to get them to change their views.

**Dave Jones:** Can you necessarily blame them because that's always the world they've operated in? That's always the world they've grown up in.

**Clint Cole Of Digilent:** They were the best at doing the theory, right? So, of course, they're going to –

**Clint Cole Of Digilent:** Yeah, they found success there. Right.

**Chris Gammell:** Yes and no. I mean on the one hand, I agree that they're a product of their environment and you really can't – you can't blame them or judge them for that. But on the other hand, they're entrusted with leading – carrying the torch forward to educate tomorrow's shapers of the future. Bingo. And they really should take a moment and pause and think about that and make sure that the things that they're imparting are on path and meaningful and useful and pithy and not sort of esoteric and fluffy and not of direct application.

**Clint Cole Of Digilent:** Yeah. I just gave away my old Fields book. What's that? Yeah. There was no electromagnetic Fields book. Oh, right. Okay. I was clearing out the old bookshelf.

**Dave Jones:** Field theory. Yeah.

**Clint Cole Of Digilent:** And this was all theory. But it doesn't mention Transformers like anywhere in there. Like, how about the Transformer? How about Chapter 1?

**Chris Gammell:** Well, one thing that drives me nuts is that every product out there, every electronic product has a circuit board in it and a power supply. Yep. The answer to the question is name two things no university teaches you about and you get circuit boards and power supplies. Right.

**Clint Cole Of Digilent:** It's becoming more and more apparent that, Clint, you could pretty much become a regular. We could never become a regular on our show because that's like all we talk about.

**Chris Gammell:** But yeah, it is frustrating. And the frustrating part is that it's just fun to do this stuff. And if more people knew that it was fun and believed they could do it, I mean, we probably would be floating around on hoverboards, you know, and teleporting ourselves all over the place.

**Dave Jones:** But what is the solution? Does university need – university EE courses I'm talking about here in particular. Do they need to be split like, you know, yeah, you still need the theory. Everyone agrees you still need the theory background. Right. At some point, yes, for sure. You can't just be a practical course as much as I would love that. But you still need that. Should it be like half that and then half mandatory, practical, there's no pass, fail as long as you go out and you build, spend a year building your widget, come back. Even if you failed, you still passed because you showed the process and everything else.

**Chris Gammell:** Absolutely. I mean the whole notion of teaching theory before practical knowledge is nonsensical. I mean I went through all that.

**Dave Jones:** It is. It's backwards because nobody, hardly anyone, a young person will get excited about the theory. They just – I can't see how they would. You'd have to be the ultimate nerd. You don't have to be the ultimate math and theory nerd to get excited about it. You know, first class at university is let's learn, you know, all this – let's start with here's the atom and here's the – First principles, yeah. And two years later, you get into how a transistor works, you know, like at a practical level.

**Chris Gammell:** Well, even that, I mean imagine if in computer science land, if in high school when you get your first Arduino or better yet chipboard, and you're setting down to – I don't know, to make a little motorized arm work on your piece of art. And day one, it was, okay, class, let's learn compiler theory.

**Dave Jones:** Yes.

**Chris Gammell:** And then we'll learn parsing languages and stuff. We don't do that. We haven't done that for 20 years or for 40 years. In computer science, we tell people just go use these marvelously complex tools that you don't have a prayer of understanding, compilers, assemblers, linkers, loaders, and just write applications. And make colored things appear on the display and interact with them and have fun. And then when you're a senior, you know, we'll tell you compiler theory. We'll tell you language theory.

**Dave Jones:** We'll tell you how it works. We'll wish. We'll tell you the secret. We'll tell you the secret in the fourth year. Yeah. Exactly.

**Chris Gammell:** Yeah, yeah. A level nine compiler theory. But in EE, we don't do that. In EE, just like you said, Dave, we drag them through all this math and physics. Yeah. And then when they're a senior, we let them do the fun stuff. And by that time, we've lost – Yeah, right.

**Clint Cole Of Digilent:** You turn around and you say, where'd everybody go? Yeah. Exactly. Right. Right. Yeah, that's –

**Clint Cole Of Digilent:** I remember – I think I was sitting with you at the – so I went to that conference, the ECE DHA thing. And I was sitting with you and with Kip Bradford too. Right. And I remember Kip told us about his grading model, which I thought was brilliant, which was you do one prototype, you get a D. You do two prototypes, you get a C. You do three prototypes, you get a B. Nice. Four prototypes, you get an A. I love that. I think that is just like – I mean, you need to show progress. It can't be like, oh, I changed the resistor from D to A. But yeah, like that is great.

**Chris Gammell:** I mean, that is showing progress. What I've done in my junior class here at WSU is I tell them – and they're on the web. You can go read them. There's like six or five projects that they have to do. And if they do those to the minimal extent that I require, they're eligible for like a B, C to B. And then I tell them, do something else. Well, what? Well, I don't care. Something else. And the more of you you put into whatever it is, the more credit you're going to get. And so it's totally open. And they've got to conceive of a way to enhance the design. And then they've got to do it. And there's no guidance because nobody else has done it before. So they've got to kind of go out on their own and challenge themselves. And it's hard to grade. It takes a long time to assess and give credit for it. But for the people that do it, it's well worth it.

**Clint Cole Of Digilent:** Yeah. Right. That's basically instilling that thing you were talking about before the... Motivation, drive, tenacity, all that stuff. Tenacity. That was the word. Yep. Yeah. That's really important.

**Dave Jones:** I want to... You mentioned the chip kit in there. Can we talk about that for a bit? Because everyone... Like the chip kit... Was it the first one that used a pick instead of an Atmel AVR?

**Chris Gammell:** Yeah. So what happened is when Arduino rose to prominence...

**Dave Jones:** Yeah.

**Chris Gammell:** We had a line of boards we called the Cerebot boards. And we were...

**Dave Jones:** Oh, so you did have an AVR version? Like an Arduino AVR version?

**Chris Gammell:** Yeah, kind of. Kind of? But gosh, what was on that? I think it was... It wasn't... We did it a couple of AVR boards to start with. But then we moved over to microchip in the PIC32 line pretty early on. Nothing to do with Arduino. We just thought it was a better-costed, more performant processor.

**Dave Jones:** Right.

**Chris Gammell:** Okay. That was more illustrative of the concepts that computer engineers would need to know. The MIPS architecture is very teachable. A lot of textbooks out there.

**Dave Jones:** Okay. Right. That was the choice behind it.

**Chris Gammell:** Yeah. Yeah. So we did that and we started making these Cerebot boards for a while. And then microchip decided that Arduino was just getting out of control. They were huge, you know. And they thought, well, we should be relevant in that market as well. And they were looking for people to produce kind of an Arduino-like board that would appeal to the same customers and have the same sort of IDE and be a maker kind of entry-level board.

**Dave Jones:** So they actually approached you?

**Chris Gammell:** They did.

**Dave Jones:** Right.

**Chris Gammell:** So we agreed to make those for them. And, you know, that's gone pretty well, but never got to the level of Arduino, of course. They were just way too saturated by that time.

**Dave Jones:** Yeah.

**Chris Gammell:** So we're still doing that. And we're coming out with new products all the time that are teaching and learning products based on the PIC32. Like one you guys might be interested in we're doing right now, we're calling the OpenScope. Oh, okay. Arduino-compatible board based on Microchip's MZ PIC32 processor. But it's going to have oscilloscope-like front ends. I think they're six mega-sample. And we have up to three megahertz analog bandwidth on two channels, plus and minus 25 volts. So it'll be two scope channels. And then it's got a waveform generator. Also, I think, five mega-sample. And then a 50 mega-sample logic analyzer. And the whole thing's on a little tiny board. It'll have Wi-Fi back to a browser app. And we're trying to get it out for like, you know, less than 100 bucks retail. Oh, wow.

**Clint Cole Of Digilent:** That's great.

**Chris Gammell:** And totally open. So the hardware will be open. All the software, all the firmware is open. The browser app's open. And the hope is we can use that as a teaching and learning platform to not only do computer science kind of algorithmic things, but also talk about the analog front ends, you know, and be relevant in circuits classes and talk about the digital stuff and be relevant in the digital classes as well. Yeah, there's definitely a lot of teaching there.

**Dave Jones:** Have you always had all your products as like open source hardware, essentially?

**Chris Gammell:** Yeah. So we've always, from day one, posted all the schematics and the bombs. We send out Gerbers when people ask for them. So the whole DNA of the company was to educate and empower and enlighten and make enthusiastic engineers and all that's on path with that. So yeah, we've been open source since before there was an open source.

**Dave Jones:** Right. Okay. Did you jump on board with the actual open source hardware movement and the logo and the whole show like that? Or were you just more liberal and just said, no, it's open. Here you go. Like I don't, we don't care about the logo and everything else.

**Chris Gammell:** Yeah. The latter. It just always has been open.

**Dave Jones:** Right. Okay. Do you think that's a good thing? Because now they're trying to, the open source hardware, we haven't talked about this for a while now, but they're trying to, the open source hardware group are trying to have like you can pay to, you know, use their approved logo and all that. Do you think that's like a good move or should things just be more informal? That's what he's trying to ask. Yeah. Do you care? Should it just be kept informal? It's like open's open, you know, like you can make it as open as you want. And, you know. Yeah.

**Chris Gammell:** So I think I'm a little bit in the, I don't care so much. I mean, I think if, if companies like, like digital and other companies, just if they put their stuff out there and it's free and easy to get ahold of, and there's no binding license agreement, you know, I think that's enough and people will find it. The problem we've found with some open source communities is they get kind of real snooty about it. They do.

**Dave Jones:** Yes. Yeah.

**Chris Gammell:** And you can't, you know, so for us, if somebody took one of our designs, we'll put hundreds or thousands of hours into a design and anybody out there can use it and put it in an amateur product or a professional product. That's fine. We don't care. But the open source guys would say, well, no. I mean, if somebody takes something that we've branded as open source and use it in a commercial product, well, that's verboten, you know, and they need to be punished. We want to take the stance, well, yeah, we made it open. We don't care. If they want to do that, then that's fine. That's up to them. We're here to enable and empower and keep the ball rolling, not to be purists about it and insist that a company or an individual can't benefit from what we did and they can't take the next step in their professional development because we feel we're purist about this open source thing.

**Dave Jones:** So you're more in the public domain camp than a license-based camp?

**Chris Gammell:** Yeah, and it's by choice. I mean, it's not for everybody, but for us, we've economized what we do through the sale of hardware.

**Dave Jones:** Right. So you don't attach a hardware license to any of your hardware? It's not like CCBYNA or anything like that?

**Chris Gammell:** Yeah, the stuff that we create and have control over, no. The stuff that's encumbered in some way because of some partnership or approval of the creation for somebody else, then sometimes we have to do that.

**Dave Jones:** Right. Because you use something else that had a license attached, therefore that has to carry forward. Yeah.

**Chris Gammell:** Sometimes it's formal like that. Sometimes it's informal. Like the company said, we just assume this not get out sort of thing. And there's very few examples of that, but there are a couple.

**Dave Jones:** Right. Who were your competitors back in the day and who are your competitors these days?

**Chris Gammell:** So in the day, I think when I first started, I found a board that I believe Avnet produced with and or for Xilinx. But at the time, Avnet was one of many distributors. I think there was also a board from, gosh, maybe it was Future. Somebody else that's kind of come and gone. But there were a couple of distributors.

**Dave Jones:** But they didn't have the same focus, right? Those distributors just make these one-off boards and they don't really have the same

**Chris Gammell:** goal of focus, right?

**Dave Jones:** Yeah.

**Chris Gammell:** And their goal was to illustrate all the functions and features of a given piece of silicon. It wasn't to make teaching and learning easier. Right. Yeah. Totally different.

**Clint Cole Of Digilent:** Yours is more like a dev board that they basically just took on themselves, right? Like a chip company would make a dev board. Exactly. The distributor made one too.

**Chris Gammell:** And their goal is to demonstrate to desktop engineers all the features and benefits of a new piece of silicon.

**Clint Cole Of Digilent:** Yeah. Sell more parts. That's the main thing. Exactly. Right. You guys want to show how parts interact and can teach and stuff like that.

**Chris Gammell:** We wanted to make, for instance, our demo boards needed to have more buttons and switches and LEDs and displays than a distribution demo board would because we knew students needed those inputs to adequately stimulate and visualize their circuit. Yep. So I think the main competitor, there was a company that's still around called XS, XESS. Oh, yeah. Dave. We've had him on the show. Yep. Yeah, Dave. Yeah. And he was around. He still is and does great products. And we've never really done anything with him. But I think he was just kind of getting going about the same time.

**Clint Cole Of Digilent:** Oh, yeah. That's true. He has been around for a while. And he was a – you should definitely go back and listen to his shows. He was in a very similar situation. He was a professor as well. And you guys would definitely hit it off, I think.

**Chris Gammell:** Yeah, yeah. We've talked on the phone a couple of times, but I don't think we've ever met at a conference or anything.

**Clint Cole Of Digilent:** Yeah.

**Chris Gammell:** But I can't think that there was anybody else. And I'm thinking internationally as well. I think it was a pretty open palate back then.

**Dave Jones:** Interesting. And these days?

**Chris Gammell:** So nobody's really – there's been some knockoffs from some other countries that have attempted to reproduce what we've done in the FPGA world. Namely?

**Dave Jones:** Can we name names?

**Chris Gammell:** I don't even know the names. They're Chinese companies. Oh, right. Okay. And there's been one company from Australia and one from Germany that were flirting with educationally themed demo boards. But most of them had come and gone. And I think that they just weren't willing to work over the long term at the margins we were willing to work at.

**Clint Cole Of Digilent:** Yeah. Right. Well, there's a lot of back-end content you need to make too. I mean, that's the other thing. It's like you can say it's educational, but unless you back it up with like, hey, there's stuff here. Yeah. And getting into education systems. And all that stuff. Right. That stuff matters.

**Chris Gammell:** And it takes time to build that stuff up. And we were able to keep at it long enough to get enough of an arsenal to have that kind of at our disposal.

**Dave Jones:** So once again, it comes down to the fact that they thought maybe they couldn't compete. You guys were on such low margins that, well, you know, that's going to be a tough space to enter.

**Chris Gammell:** Yeah, absolutely. One of my favorite examples was a publishing company in China contacted us to buy some of our mid-level boards. We sent them a bunch, sent them the schematics, sent them all that stuff. And then about six months later, out came a clone of our board. Oh, where did this come from? Well, I went and met the guy. He's a nice enough guy. He didn't speak any English. So I think he was nice. It might have just been the interpreter was nice. So he was kind of proud of it, but maybe a little bit embarrassed by it. But it turned out at the end of the day that they were selling the board they designed and manufactured in China for about 20% more than ours was for sale for. Wow.

**Clint Cole Of Digilent:** Nice.

**Chris Gammell:** So it just, you know, we had a long enough. We got the economies of scale going to where we could remain competitive. It's a little different on the analog front. You know, we got the analog discovery that's been out there for a while. And I think, Dave, I think you did a review on that a while ago.

**Dave Jones:** Yes. Yes. The first one and the second one, I think. Yep. Yeah. Or just the second one. Yep. Yeah, it's nice.

**Chris Gammell:** And that's still doing nicely. There's more players in that market now. Yes, there are now. Yep. But we're trying to keep our features and performance at a high level and our costs at a low level. And so far, I think we're doing okay. And this new open scope will be the little brother in that family. You know, a little less performant, a little less cost, but far more open. And, you know, hopefully it'll find its niche. And then down the road a little bit, we'll come out with maybe a slightly higher performant one for a little bit more cost. But try to, again, keep that student-faced. Everybody can buy one. Academic materials, backing it up. Curricular adoption, strong. And just make it a very good educational play.

**Clint Cole Of Digilent:** Well, the thing I like about it is the, I mean, like, so me and Dave talk about this a lot now because I've been traveling so much, is like, we've been talking about how do you have test gear on the road? And really, it's just how do you move away from test gear that's very heavy and bench-based? And this is a pretty good move in that direction, I think. You know, so I think this is the right kind of direction, especially because, you know, we talk about Rigol-type scopes a lot. And it's like hitting 50 megahertz bandwidth is not easy with off-the-shelf parts, especially at a low cost point. But it's starting to get there. And for a lot of stuff I do, at least, I don't need to be above 50 megahertz. So it's great. Indeed.

**Chris Gammell:** The product we're working with on paper now will offer 250 megahertz analog bandwidth and try to be in the same ballpark from a pricing perspective as well. Okay. Yeah, that's good.

**Dave Jones:** Now, please correct me if I'm wrong, but the analog discovery is not open.

**Chris Gammell:** No, yeah. The circuitry on, that's the one product. I mentioned a couple of exceptions. That's the one product that's, we've got that technical reference manual. I don't know if you've seen that online. Yes, yeah, I've seen it. Yep. Yeah. So all the circuits are there individually. And they're pretty good explanation about what it is. But the Gerbers, I don't think we've released publicly.

**Dave Jones:** Or even the full schematic, like as such. Right? Yeah, I don't think the full schematic's posted either. No, that's right. And I think people have complained about that. And, you know, so why is that?

**Chris Gammell:** Yeah, I think it's because for us, that was by far the biggest investment we'd ever made. And that was pre-acquisition.

**Dave Jones:** Is that because the software was so much of the development cost?

**Chris Gammell:** Yeah, the software took a year and a half. The hardware took a good year with several iterations. And, you know, we pretty much put every disposable penny we had into that thing.

**Clint Cole Of Digilent:** Oh, okay.

**Chris Gammell:** Yep. And it was speculative. And we didn't know who was going to buy it and how many. So that one product we felt we would keep a little more private until we hopefully paid back some of our lab bills so we didn't have to shut the doors.

**Dave Jones:** Because there's a huge price difference on those between the student version and the, you know, just the regular Joe Bloggs version. Are you still making money on the student versions or do you sell those at a loss just for, I don't know, loss later purposes?

**Chris Gammell:** I think I could probably find an accountant here that would tell you we're selling them at a loss.

**Dave Jones:** Right. When you include labor and all sorts of company stuff. Exactly. It's very hard to calculate. Amortization, Dave. Yeah. Amortization. Exactly. Exactly.

**Chris Gammell:** If you look at just dollars, you know, that it costs us to put one on the shelf and dollars we get to sell it, it's more or less a wash. Yeah. And then the commercial version is an attempt to have enough margin to keep the machine running. I got it. Yeah.

**Clint Cole Of Digilent:** That's good.

**Chris Gammell:** But the new one, the OpenScope, that will be totally open. You know, from the get-go, the Gerbers will be out there, the Bomb, everything will be out there.

**Dave Jones:** And you don't care if people copy it?

**Chris Gammell:** In general, we don't care if people remanufacture our boards because we've learned over the years that they'll quit doing it because they won't work at the margins we work at.

**Dave Jones:** Right. Okay. It's like, good luck. Take us on. You know.

**Chris Gammell:** Exactly. And we've had that experience two or three times where they just gave up. Yeah. Enjoy the ramen, guys. Enjoy the ramen. Exactly. Exactly.

**Dave Jones:** There's another. It just sprung to mind. The Ter... Is it TerASIC? They make FPGA boards. Correct. Quite popular FPGA boards. Are they an up-and-coming competitor?

**Chris Gammell:** Yeah. I kind of forgot. I should have mentioned those guys. I kind of forgot about them. They're on the Altera side.

**Dave Jones:** Yep.

**Chris Gammell:** We're on the Xilinx side. And they got started...

**Dave Jones:** You guys only do Xilinx?

**Chris Gammell:** Right now, the only programmable logic we do is Xilinx. We do other... Right. You know, analog and digital. We do other processors and other analog parts. But for FPGAs, it's only Xilinx. Why is that? I don't know. You know, I was a Xilinx customer from years ago. And I knew the tool set. And I knew some people there. And it was just an easy place to get started. And we just never really ventured. And because you have to choose, right?

**Dave Jones:** I mean, you can't.

**Chris Gammell:** You have to pick a side, Dave.

**Clint Cole Of Digilent:** Come on.

**Speaker ?:** Well, no.

**Dave Jones:** You don't. But then you've got to... If you choose both, then you've got to put development of resources into both. With entirely different tool sets and learning and everything else.

**Chris Gammell:** And that was a disincentive. And so Teresic got started a few years after we did. And their early boards looked very much like our early boards on the Altera side. And then gradually, the costs... You know, their initial boards were several hundred dollars. But then they came down in price. And so now we're kind of equitable in terms of features and our pace of new boards and our costs and all that stuff. And now both of us are kind of somewhat beholden to our parent companies in terms of their promotion of their devices into broader markets.

**Dave Jones:** Oh, I didn't know they had a parent company.

**Chris Gammell:** Well, Altera, we don't either. But if Xilinx, for instance, was no longer interested in attracting university students and change their tone, or if Altera didn't... What were interested in university business, then both of us would suffer a little bit.

**Dave Jones:** Well, that could happen because Altera is now being bought out by Intel.

**Chris Gammell:** Here's hoping.

**Dave Jones:** Right. Is that... How do you see that move?

**Chris Gammell:** Yeah, I don't know. You know, it's interesting. You know, Altera and Xilinx had been working... Or sorry, and Intel had been working together for a while. And they'd been putting some programmable stuff on dyes and kind of experimenting with reconfigurable computing. So it's intriguing to me as an engineer and as a consumer what that might unveil because I probably read more FPGA studies than you guys do. And there's some... Yes, yes. There's some really cool stuff out there. I mean, with relatively cheap FPGAs, you can get just almost unbelievable performance increases for certain applications like video processing and, you know, multi-broad sensor inputs.

**Clint Cole Of Digilent:** Like parallelization of signal chains and stuff like that.

**Chris Gammell:** Yeah, massive parallelization.

**Clint Cole Of Digilent:** Yeah.

**Chris Gammell:** Like thousands of data paths all being managed autonomously, contributing to one data set that the processor can then do something with.

**Dave Jones:** So they could be thousands of times faster, several orders, you know, three, four orders of magnitude better than...

**Clint Cole Of Digilent:** Take that, GPUs. Yeah, absolutely.

**Dave Jones:** Well, GPUs are parallel, Chris.

**Clint Cole Of Digilent:** I know, but I'm just saying that, like, it's the same. It's even better than those are, right? I mean, that's usually the comparison is even better than GPUs, right? Yeah, absolutely.

**Dave Jones:** Well, but no, but GPUs are optimized. GPUs are silicon optimized for power.

**Chris Gammell:** And for their solution space, yeah.

**Dave Jones:** Solution space, power per performance, you know, per watt. Whereas FPGAs can do the same thing, but they take more power and they take more area to do it. So...

**Chris Gammell:** And the big thing is you're not locked into one set of features when you produce and put out into the world of circuit board. You know, it can have different personalities over time.

**Dave Jones:** Have you seen those massive ASIC development boards? Like boards. The ones that have, like, you know, 20, you know... FPGAs. High-end, yeah, 10, you know, that cost 10 grand a pop. You know, the chips. And they have, like, 100 of them on there. Oh, yeah, boy.

**Chris Gammell:** I've seen boards that sell for 100 grand. Yeah, 100 grand. Wow. Yeah.

**Dave Jones:** They're insane.

**Chris Gammell:** B-Cube sells some. TED out of Japan sells some of those things. And they're impressive. And apparently they work. I thought you were going to check, right? Yeah, well, exactly.

**Clint Cole Of Digilent:** Only 99 out of the 100 work. We're sending it back.

**Chris Gammell:** Yeah, we did one board that was up there in price. In fact, when we first retailed it, it was $25,000. Because a silicon was cost, and it's like $16,000 just to populate the board. Yep. So that's a bit nerve-wracking when you order 100 of those things.

**Dave Jones:** That's insane.

**Clint Cole Of Digilent:** Just imagine, like, walking down and, like, tripping a tray. Of those chips. Just like, no. Oops. I'll just go home. Yeah, I'll just jump off a cliff.

**Dave Jones:** You probably can't speak for Altera, but do Xilinx care about the educational market? Do they care about the little player? Because I've been screaming for two decades for, you know, low pin counts, low IO chips, you know? But no, they've always told me, no, that is not an important part of our market. We only care about the high pin count, you know, high cost market. We don't care if you only need 10 IO pins. We're not, you don't exist on our roadmap.

**Chris Gammell:** I got two answers for you. One is, if you talk to the mainline sales force at any of those companies, you know, it doesn't matter if it's Xilinx or Altera or TI or anybody else. You know, those guys are largely commissioned and they make their money on supporting the big high volume customers. So, yeah, they're not going to be interested. But I think this is a true statement that I think Xilinx has probably the largest educational slash university program of any semiconductor company. Oh, wow. So, they take it very seriously. Yeah, and they put a lot of time and resource and effort into it. And they do a very good job of helping universities around the world get access to their technologies.

**Dave Jones:** Interesting. So, they have a group that takes care of this?

**Chris Gammell:** They do, yeah. Oh, I would presume. And you can go online and you can read about them. Oh, okay.

**Dave Jones:** There you go.

**Chris Gammell:** I think they might have been the first company to make their tremendously powerful CAD tools free. Oh, interesting. Up until 2002 or 2003, whenever they introduced Webpack. Yeah, a design seat cost you several thousand dollars minimum. Oh, it's insane.

**Dave Jones:** Yeah. Yeah, up to 100,000. The average Joe blogs in their garage doing this startup could not afford to use FPGAs. They just couldn't.

**Chris Gammell:** Absolutely. And when Xilinx made that tool free and Altera followed soon after, all of a sudden you have this tremendously powerful software. I mean, those guys are probably into their current software tool for $50 million or more in development cost. Oh, easy. Yeah. Yeah. And it's free. And it's all tickle scripts.

**Dave Jones:** Well, most of it, except for the real extreme high-end parts, I think, which you have to pay for. But that's fine, because your average Joe is not going to use a $5,000, $10,000 FPGA in their new Internet of Things widget.

**Chris Gammell:** Well, exactly. If you just take one of the FPGAs that are supported and look under the hood, I mean, things like 36-bit multipliers that converge in three nanoseconds. I mean, it's just insane.

**Clint Cole Of Digilent:** Crazy. I remember one of the restrictions when I was using those tools, which was, God, back in 2004, 2005, was that you could use it as long as you wanted to. But if you wanted to unplug the programmer, that's when you basically paid. That was one of the ways that they got you, so that you couldn't really make a downloadable, executable type thing, but you could definitely talk to it.

**Chris Gammell:** Yeah, that's all gone now. You can make your designs non-volatile and sell them if you want to, yeah.

**Dave Jones:** What about the programming side of these? Because you can buy these $5 rip-off JTAG, FPGA, that talk to the Xilinx tools, oh, you can buy them on eBay. But Xilinx sort of never really had a low-cost solution for that, did they? Or am I wrong? No, they never did, in fact. Which you said earlier that you had to actually reverse engineer it, right?

**Clint Cole Of Digilent:** Dave, don't bring it up again. He said not to say that.

**Chris Gammell:** No, I'm going to cop for sure. They never viewed FPGA programming as a low-cost enabler for commodity kind of consumers. And why is that? I think because the people that were kind of in control of those kind of things, they looked at companies like Cisco and Huawei and China and AT&T and thought, you know, those guys just spent $100 million or whatever, $100,000. They don't care about a $300 programming cable. But we were one of the first companies trying to really proliferate those kind of boards into the low end of the marketplace. And so for us, we couldn't sell a $79 circuit board and a $300 programming cable. And that's why we first reversed engineered it and put it on our boards. And then later on, we produced cables that did the same thing as the Xilinx cables did but at a much lower cost. And it took many, many years. But after we demonstrated that we could do that and that they were reliable and people were happy with them, gradually the Xilinx tool set started supporting our programming hardware as well.

**Dave Jones:** Oh, they do. Okay. Right.

**Chris Gammell:** Interesting. So now within their tool set, you can select one of our programming cables as a standard way to program FPGA boards.

**Dave Jones:** But why don't – do they just not get it? I mean, why don't they produce – It sounds institutional, Dave. I know, but why don't they just produce the low-cost program that everyone uses here? It's open. Build it into your development board, into your product. Like why? They can't possibly be making money on the development – on the programmer.

**Chris Gammell:** I think they do make a significant amount on their programmers right now. But I think they suffer from the thing we talked about at the top of the show and that was that it's just hard for big companies to do low-cost shrink-wrapped products.

**Clint Cole Of Digilent:** Well, it also could be that there was a – you know, if there's a group that's in charge of the thing and they have a budget, then they have to prove that they're paying for themselves. I mean, there's that kind of stuff too. Like that's just big company stuff. Yeah, exactly. People wonder why –

**Dave Jones:** People wonder why PIX are popular, especially today if they don't know the history of it, is because they were the first to come out with like low-cost tools that your regular Joe blogs could, you know, do. Whereas the rest of the microcontroller companies were all, you know, real expensive multi-thousand-dollar tools, you know, and that's why a lot of people picked it up and there was a big groundswell of support because, you know, at low-cost or people would make do-it-yourself programmers, you know. It was just like that enabled the popularity of the microchip pick.

**Chris Gammell:** Yeah, very much so. Yeah, and then after that revolution, Arduino came along and said let's not only make it cheap, let's make it intuitive and easy.

**Dave Jones:** Yeah.

**Chris Gammell:** I think that the FPGA side of things, we're heading in that direction.

**Dave Jones:** But it's never gotten there. It's never –

**Chris Gammell:** No, it hasn't.

**Dave Jones:** I never see it reaching that threshold. It's just like big incumbent, you know, machine that sort of can't –

**Chris Gammell:** I think it will get there, but it took – you know, there were probably, I'm going to guess, 5 billion chips sold per year in the microprocessor arena before they got to the point where the tools were very low-cost and very ubiquitous.

**Dave Jones:** Right.

**Chris Gammell:** And that meant there was a whole different economy of scale. For FPGAs, if you wanted to get the tools to that level and the adoption that high, there's just right now a little bit too steep of a learning curve. Yeah. And the tech support would just swamp whatever company tried to do that. So I think those economies kind of follow adoptions. And as more people develop the skills and as the markets get a little more open for FPGAs at lower strata, I think you will see those ancillary tool prices come down and get free. And just an Arduino-like environment for FPGAs is probably out there somewhere, but maybe not until the volumes and the adoptions go up a little bit.

**Dave Jones:** Right. I was going to say, is there still going – like is there – are we still waiting for that killer Arduino-type tool for FPGAs?

**Chris Gammell:** I think what we're waiting for is the killer app sort of. I mean once there's a thing that you could do with FPGAs that you really couldn't do with fixed silicon and once it resonated with a large audience, that's what it's going to take. I'll tell you, those things exist right now, but not enough people have the skills.

**Dave Jones:** Yeah. And they're too niche app requirement because micros are so ridiculously powerful that it sort of pushes FPGA into the niche. And this is why I suspect that they may never – we may never reach that point where they're massively popular. I don't know. I don't know.

**Chris Gammell:** The kind of today's niche is tomorrow's must-have. Here's an example.

**Dave Jones:** But it's been going for a long time and I haven't seen anything on the horizon yet. I thought I would have seen something by now.

**Chris Gammell:** I think it's because the requisite skill set is still a little bit beyond most people. Here's an example I've used in conversations like this that there's no reason, for example, you couldn't put an array of microphones in the ceiling of a given room and then maybe have 64 of them up there. Yep. And then you phase delay from certain microphones a certain amount and that would have the effect of very precisely lensing in to one particular spot in a room where you're receiving audio energy from. And you could filter out the rest very effectively.

**Dave Jones:** So you could do like a shotgun – a beam-forming shotgun microphone you're talking about.

**Chris Gammell:** Exactly. And somebody with a mouse on a computer app could just move around the room listening into private conversations with no moving parts. Right. The NSA has now chosen your board for production. And they could just listen in. And you could easily do that today with – you couldn't do it with a processor because you've got 64 real-time data streams all needing to have their phases delayed a little bit and their waveforms correlated. You could do that right now today in an FPGA. And what a cool thing that would be to have at a stadium or something. And then by the same token, you could put a phased array of speakers up there and you could phase delay output and pinpoint where peak audio energy was in a room and you could have an individual conversation in a crowded room between two people. Like the cone of silence from Get Smart.

**Dave Jones:** The cone of silence, yes. Maybe we'll add that photo of the cone of silence. I think that'd be cool.

**Chris Gammell:** And those kind of apps are real-time feature tracking in live video streams. There's a lot of high bandwidth, high input, high output problems that we just haven't gotten around to trying to solve en masse because they've been just out of reach due to technology. Well, FPGAs bring a lot of that stuff into the sphere, but now we need people with the skills and the knowledge and the exposure to take advantage of those technologies and solve those kind of problems.

**Clint Cole Of Digilent:** It kind of feels like the – I mean the skills that you need for FPGAs though too are like pretty low-level digital knowledge I feel like. I mean I know that with Verilog you can kind of make it more like C, but that's not really a – you know, like we're churning out a lot more JavaScript people I think than we are C programmers. And so it feels like getting back down towards the hardware level, which is what FPGAs kind of require is kind of like understanding how the blocks are put together. It feels like that's not necessarily being trained for.

**Chris Gammell:** Yeah, I'll tell you, and I struggle with this exact topic all the time. Yeah, I'm going to go back and teach in the fall these kind of topics and I don't know what the right thing is to teach even today because, yeah, you've got this whole structural body of knowledge. You know, how AND gates and OR gates are formed and how they connect to each other to form larger circuits and like MUXs and decoders and how those things are connected into larger systems. There's this whole structural kind of blueprint-y way of looking at those kind of things. And then there's the, nah, don't care about that. I just want the function. And you can specify that with one line of high-level code. And what does an engineer have to know about that? I mean, does it matter to them that that one line of code just instantiated several thousand gates and just required 100 milliwatts of power? Doesn't matter until it doesn't fit in the part anymore. Or until it won't run at the speed that it needs to run. Yeah, exactly, exactly. And so if we're going to keep an awareness of the structural ramifications of the behavioral code people produce, if that needs to be a part of the educational and practical landscape, that does kind of put a speed limit on how fast we can educate people and how many we can educate.

**Clint Cole Of Digilent:** Yeah.

**Chris Gammell:** And I don't know what the right answer is. I mean, maybe we should just say, you know what, transistors are on the order of a nanopinny per gate now. So maybe we should just ignore all that. And, you know, what's the difference between taking 20,000 transistors and 20 transistors? You know, it's kind of the same. It's a penny more. So forget it. Don't worry about the structural ramifications. Just work at a Verilog or VHDL or even higher IP level and assemble systems regardless of the structural cost and the physical cost.

**Clint Cole Of Digilent:** I think that's the right. No, I think that is kind of to start with the top down and then eventually like, well, now let's try and use it with a battery. And you'll very quickly realize not so much. So I think you have to do it like that because so much these days is the JavaScript. I used a library. It just works kind of thing. You just have to grab people with that and then eventually dive down through those layers. Yeah, maybe with a subset of them that are motivated to learn that stuff. Right, exactly. And unfortunately, I kind of take the test. I don't personally think that FPGAs will ever become like mainstream like that. Not like the way that Arduino is or like just low-level programming because it's just – it does require kind of a more under-the-hood view.

**Chris Gammell:** Yeah, I'm betting that when Spock was eight or nine, he learned FPGAs. Yeah, well. Down the road, who knows? I mean, as this stuff filters down into younger – probably structural design and FPGA architectures and all that stuff probably won't make it down into grade schools, but maybe into middle schools, maybe into high schools.

**Clint Cole Of Digilent:** Yeah. Yeah, well, I think it's definitely an enabling thing. So like you could show it as like a, hey, you can work towards this and you can really supercharge the hell out of your product. So it's worthwhile learning that stuff.

**Chris Gammell:** Yeah, and really, yeah, there needs to be like this problem you can solve with a low-cost FPGA board that really would stymie a non-FPGA solution.

**Clint Cole Of Digilent:** Yep, yeah. And there are some good ones. Like, so I know Ryan from Snickerdoodle, the Snickerdoodle project, and like they're doing interesting stuff. You know, that's a relatively low-cost board. Just basically trying to show that like, yeah, you can put vision, you know, like some high-end vision on a drone for, you know, 50 bucks. And it's like, whoa, that's pretty impressive. And that's an end goal that a lot of people want. They want to be able to have vision in their products and stuff and not have a laptop attached.

**Chris Gammell:** Yeah, yeah. I think that's kind of a holy grail as well. I mean, if you could have a camera with an FPGA backing to it that could do real-time feature extraction and motion detection and that kind of stuff and feed that to a processing engine, that would be huge. And we're working on that same thing as well. We've got an FPGA-based camera in the works that'll be a peripheral device to a processing board as well.

**Clint Cole Of Digilent:** Nice. That's great, yeah. And that's, I mean, like just in terms of robotics, that's super important for lots of things. Oh, yeah.

**Chris Gammell:** Just imagine instead of all these bump sensors and proximity detectors, you just visually detected what was in your way and avoided it.

**Dave Jones:** Yeah. No, totally.

**Chris Gammell:** And there's a lot of processing there. Oh, there's a huge amount, yeah. Yeah. Massive.

**Dave Jones:** That's great. That's where the secret sauce is. It's, you know, yeah, you can stick an FPGA, a camera onto an FPGA, but, you know, so the hardware is easy. Yeah. But the development is not.

**Clint Cole Of Digilent:** I was just listening to Chris Anderson was over. It was actually back from March. I was going back to the old podcast, but he was on the hardware podcast, and he was talking about that with the 3D robotics, how basically they're just moving to like whatever works for sensors and vision and everything else. When you need to have a drone not run into something, you'll just use whatever's necessary. And that's, you know, one of the things you could use is vision, but also all the other sensor fusion and stuff like that. So it was a good one. Yeah.

**Chris Gammell:** But to ask kind of a typical, I don't know, normal engineer to do feature extraction on a video image in real enough time to be useful in a control situation, that's a tall order. Oh, yeah. Yeah, no, definitely.

**Dave Jones:** You practically can't do that in a micro in a low power solution, you know. Oh, no, you can't.

**Chris Gammell:** You know, you'd have to have something like an FPGA to do all the pre-processing and, you know, find the abrupt transitions and somehow parameterize them, you know, and feed that in a meaningful data stream back to a processor that could handle a reduced bandwidth of that stuff. Right.

**Dave Jones:** Now, we are getting well onto the show. We should be well into an hour and 40 minutes in. This is fascinating, so we should probably wrap it up soon. But I want to just briefly revisit the business side of things, if I may, because I did a recent video on this and people seem very interested in it. And have you ever done drop shipping or have you considered that? Have you always, you know, have you always shipped yourself? Are you still shipping yourself? You've got your own warehouse. You ship everything else.

**Clint Cole Of Digilent:** So, Amphar goes from FPGAs and computer vision back to drop shipping. Why not? Dave's, yeah.

**Dave Jones:** It's an important question. A lot of people want to know this stuff.

**Clint Cole Of Digilent:** Sure, sure, sure.

**Chris Gammell:** What is, yeah. No, so we certainly had stocking warehouses in China and in Europe that we shipped from. And it turned out for a while.

**Dave Jones:** Is this back in the early days?

**Chris Gammell:** Well, I'd say mid-2000s, 2005 through 2009 or 10. And I think we maintained, we still have a stocking distributor in Europe, Trends Electronics. And I think we don't have one right now in China. But our manufacturing largely came out of Taiwan. And those guys for a long time would drop ship, certainly if it was more than one or two products. Right. And if it was in that part of the world, they'd drop ship from there. But I think more recently, we've kind of recombined shipping. And most of the product flows through our head offices here in a little town of Pullman, Washington.

**Dave Jones:** Okay. So, you've actually insourced.

**Chris Gammell:** A little bit. I think the European stuff still largely flows through our distributor out there in Germany. But the rest of the world largely comes out of here.

**Dave Jones:** Right. That's because the EU is a different kettle of fish. It's harder, right?

**Chris Gammell:** It is. And once you penetrate them and you're like a virus inside of that organism, you can just stay there and spread.

**Dave Jones:** You're better off penetrating in one big jump rather than trying to get a thousand packages through. That's right. You're better off jumping. That's exactly right.

**Clint Cole Of Digilent:** Customs and everything. Yeah.

**Dave Jones:** Bloody European Union.

**Clint Cole Of Digilent:** Yeah. Indeed. So, Pullman, Washington. That's a good thing to end on. So, you guys are still in Pullman. We are. Is that next to the university? Is that right?

**Chris Gammell:** Yeah. You can't be in Pullman and not be next to the university. It's the town's dominated by the university.

**Clint Cole Of Digilent:** Gotcha. That's got to be good for sourcing new talent for the company and everything, too.

**Chris Gammell:** Yeah. In fact, we had a company lunch today or yesterday. And it's just now summer. And in the summer, we hire more interns. So, you know, you kind of hear the call to meeting going up. Somebody says, you know, come for the meeting. And so, I wander down there and this crowd of, like, locust-type people come out of the intern

**Speaker ?:** area.

**Chris Gammell:** 22-year-olds, yeah. And they just pick that thing clean. There wasn't even a crumb left by the time I got up there. And so, yeah. So, I think we have, like, 20-odd interns from WSU this year. Wow. That's awesome. That's really great. Yeah.

**Dave Jones:** And these guys... Sorry. Yeah.

**Chris Gammell:** And they all do... They're all doing actual designs. So, a lot of what they produce, you can see on the web. And some of them go to conferences around the country and even around the world. And it's a great engineering intern gig, I think. Wow. Reason to go to WSU. Are there any free spaces?

**Dave Jones:** Or is that it? You've already done your intake for the year? No, Dave. For you, we'll make a space. There we go.

**Clint Cole Of Digilent:** Dave's a forever student. Yeah. Student of the world. Student of life, yeah. An Aussie transfer student. Or was it an exchange student? That would be. There you go.

**Dave Jones:** So, you're still essentially a separate company as such? Yeah.

**Chris Gammell:** We've maintained our own web presence, our own manufacturing flows, our own marketing and sales kind of teams. Okay. But we've combined some things like our budgets roll up into NI's budget. Right. I think our headcount comes out of the central headcount. But by and large, we're about as separate as we can be and still be part of a larger company.

**Dave Jones:** And NI want to keep that? They see value in keeping that separation? I think so.

**Chris Gammell:** I mean, we're kind of – we're given the trust and the latitude to innovate, to create new products, to see if they work, to independently develop new markets and new solutions and new strategies. So, yeah. All that's very much in keeping with us being a smaller, independent company, even though we're tethered to them.

**Clint Cole Of Digilent:** So, it sounds like similar to a past guest, Matt Eddis, when he was on, too. His Eddis Research is kind of similarly –

**Chris Gammell:** Oh, yeah, yeah. Matt and I talked a fair amount because we both got acquired about the same time.

**Clint Cole Of Digilent:** Oh, yeah. Cool.

**Chris Gammell:** And actually, his guidance was a lot of what helped me want to do this with NI. And, yeah, I'm glad of it. That's great. Yeah.

**Clint Cole Of Digilent:** Yeah. Yeah. No, he was great to talk to. Yeah. Yeah. He's a good guy. He's the RF people. Yeah, exactly. RF people. Yes. Well, Clint, thanks so much for being on the show. You were exactly the kind of person I want to talk to all the time. Yeah. Totally. Well, vice versa. Yeah.

**Chris Gammell:** Yeah. My pleasure.

**Clint Cole Of Digilent:** I had a great time. Awesome. And I think that you were supposed to announce a coupon code or something as well. Oh, yeah. Sorry, Larissa. You will get in trouble with Larissa. Yeah. What are the odds she would listen for two hours to us?

**Dave Jones:** She's got a – yeah, I was going to say.

**Chris Gammell:** She's coming through, I guarantee you. She's listening right now. Yeah, probably. So what I meant to say is that the coupon code, VAMPHOUR, all in caps, all one word, T-H-E-A-N-P-H-O-U-R, you can enter that at checkout on our website, and you get 15% off anything you put in your cart.

**Clint Cole Of Digilent:** Very nice. Sweet. Well, we appreciate that, and I'm sure our listeners will as well. So hopefully people are picking up some new things. I have the discovery, too. I'm actually enjoying it. I'm playing with it quite a bit. Oh, yeah. It's nice. Definitely check that out.

**Chris Gammell:** I still play with it myself.

**Clint Cole Of Digilent:** Yeah.

**Dave Jones:** And with that discount, you're probably getting it at cost, folks. Exactly. Exactly.

**Clint Cole Of Digilent:** We know all your secrets now. Yes, indeed. Indeed.

**Dave Jones:** That's how you've crushed the competition. Yes. And you didn't have to go to China to do it.

**Chris Gammell:** Yes, exactly.

**Dave Jones:** Fantastic. Thank you very much, Clint.

**Chris Gammell:** Well, thank you, guys.

**Dave Jones:** Where can people follow you? Like Twitter and all that sort of jazz?

**Chris Gammell:** Yeah. I think I'm too old for that stuff. Right. I see these kids doing that, but I don't think I've ever tweeted. Tweeted.

**Clint Cole Of Digilent:** Well, there's a digital on Twitter, though. I'm sure that people could follow. There is. Somebody interacted.

**Chris Gammell:** Yeah, I probably should. You know what? After this, I'm going to go get a presence on Tweetbook and FaceTime and all that other stuff. Yeah, they're good. Good. Awesome. Thanks again, Clint. We appreciate it. Thanks, Clint. Thanks, guys. Okay. Catch you next time. Bye-bye. Bye-bye.

**Speaker ?:** Bye-bye. Bye-bye.
