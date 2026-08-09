---
episode: 220
title: An Interview with Shaun Meehan - Doctiloquent Dove Deployer
url: https://theamphour.com/220-an-interview-with-shaun-meehan-doctiloquent-dove-deployer/
---

**Sean Meehan:** This is the Amp Hour Podcast, recorded October 13th, 2014, Episode 220, with guest Sean Meehan, Doctiloquent Dove Deployer.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Sean Meehan of Planet Labs. Welcome, Sean. It's just me and you today, but I think it's going to be a good conversation. Thanks for having me on. So let's jump right in. So first off, I met you last week, actually, at a hardware meetup in San Francisco. But I had actually seen you once before on video. Why don't you tell us? Because I bet a lot of people have seen this video.

**Dave Jones:** Yeah. So basically, I had Limkin put up this whistle LED, he called it. And at the time, I had just gotten my one-ton robotic arm, Fred, up and running. And I decided that it would be kind of cool to wire in one of these to Fred. And so when I would whistle, he would come over and I'd whistle again and go away. And so I called it the Whistle Bot and I threw it up on YouTube.

**Chris Gammell:** Yeah. And it's awesome because it looks like it. What it reminded me of is like in Iron Man where he's kind of shouting at the robot in his lab. Obviously, it's just whistling in this case, but it's awesome because it makes it like a pet, basically.

**Dave Jones:** Yeah, exactly. You know, I don't like to draw the direct comparison to Tony Stark, but that's okay.

**Chris Gammell:** When I was kind of going for that, yeah.

**Dave Jones:** When I was kind of going for that, yeah. So the goal with it initially was to be able to – I got a bunch of these dog training clickers. Oh. Because they create that really solid point source sound. And so what I wanted to do was wire up Fred with microphones and then actually have him back out a position in 3Space from the click. And I actually took a week off work a little while ago after our last build and wired this thing up. So I have a little FPGA running, four microphones on a plane right now, so I just get a vector. But, yeah, I'm able to do time of flight calculations for that. And so the next step will be to integrate that onto Fred. So the idea was he would be – for that it would be a monitor mount. So I could be working on something and, like, snap for the robot and he would come over and, you know, show me the monitor of whatever I was working on. Yeah, have data sheets just show up in front of you would be kind of fun. A good use of three and a half kilowatts.

**Chris Gammell:** Yeah, right, right, yeah.

**Dave Jones:** Just turn on another coal plant. Just hold the monitor in space. Yeah, exactly. Fire it up.

**Chris Gammell:** So, wait, so you have two robots there, right? Or is it just the one? Yeah, yeah.

**Dave Jones:** No, I have two, Fred and Lefty. So, yeah, Fred was the first one and then Lefty was a gift. So, yeah.

**Chris Gammell:** Sean, what do you want for your birthday this year? Oh, I don't know. A couple-ton robot, whatever, no big deal. You got one laying around.

**Dave Jones:** You got one laying around. No, it was – because basically, like, the story behind the robots is – I must have been, like, 10 years old or something. And I ended up going on a tour of some plant and saw one of these robots move. And I was fascinated by the fact that this monstrous robot, this, you know, one-ton arm – I mean, they're about 700 pounds and another 1,700 pounds for the base.

**Chris Gammell:** Whoa.

**Dave Jones:** And, yeah, they swing. But the fact that this thing can move at 300 degrees per second and the only audible sound from it is this hum that – this is just very, very high-pitched, you know, whine as they move around. But besides that, they're almost silent. And I just thought that was so amazing that this giant thing could be swinging around and, you know, with millimeter accuracy without making, like, this giant rumble. And so then I was hooked and I needed to find one. And, yeah, so –

**Chris Gammell:** Yeah, it's on your blog that you said you had a Perl script going for, like, a couple years. Was this kind of, like, hunting Craigslist or what – so what do you actually pay for this kind of thing? I don't know if I saw the price.

**Dave Jones:** So, yeah, no, actually, I kept the price off the sites because I – it was just –

**Chris Gammell:** Embarrassing?

**Dave Jones:** Yeah, I didn't – well, no, it wasn't quite that. It was – so basically what I had done was I wrote, like, a little bit of a web crawler that would go through, like, industrial surplus sites and stuff like that. And basically it would, like, send me an email whenever it found something and it would be, like, found this. And I'd be, like, okay, well, that's, like, $10,000. I can't afford that. Or, like, that's not what I'm looking for. And so I kept, like, honing this script until one day I got this email from my script and it said, like, orange robot. And I was, like, oh, this is promising. And so I ended up finding Fred totally mislisted. Oh, I love those. Yes, in the industrial – like, some subset of the industrial eBay setup. And it just said orange robot and had a picture of the robot, the cabling, the brain, like the S3 cabinet. And, yeah, and it was $700 was the starting offer.

**Chris Gammell:** Oh, my God.

**Dave Jones:** I put in a single $700 bid, like, six days before the auction ended. And then the horror, like, started to set in, like – Should have waited. Should have waited. No, no, it wasn't that. It was the idea of, like, oh, my God, I'm going to win this. Like, what the hell am I going to do? Like, this is all I've wanted for so long. And now I'm going to get it and I don't know what to do with it. And so then the auction ended and all of a sudden I own 2,700 pounds of equipment in Connecticut. And I live in Colorado at the time. And they sent me an email, like, so what do you want to do about the freight setup? And I was just like, what is freight? Like, how do I do this? And it turns out if you don't know what freight is, it gets very expensive very quickly.

**Chris Gammell:** About $700 or more?

**Dave Jones:** Yeah, a little bit more. So it turns out I needed a forklift operator and a loading dock on each end, which is, like, the tip of the iceberg.

**Chris Gammell:** Yeah. Oh, my God.

**Dave Jones:** And so I end up, like – I talked to the guys who were selling it and they were totally cool. And they actually ended up being the people that named it Fred. Oh, yeah. Because I got this email from them that was just Fred's on his way after all the shipping had been sorted out. And I was like, what? Fred? And it was so strange. But then he arrived and I was like, this is totally your name. You're Fred. But – so anyway, I ended up going to one of my neighbors who owned a plumbing shop that had, like – it was a pretty large-scale operation. And I was like, is there any chance I can get this thing delivered here and, like, your forklift operator can unload it and just, like, put it out in the backyard somewhere. And I'll, like, cover it up with a tarp until I figure out what to do next. And he was like, I'll do you one better. Like, we'll clear out some space inside and let you store it in there. And I was like – Oh, man.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. So then I had it sorted on my side and I, like, you know, was very gentle with the guys on the other side. And I was like, is there any way you can, like, sort this out on your end? Because I have no idea what I'm doing. Which is definitely a theme of the project. And so, yeah, so they ended up getting it, like, weighed and getting it to a shipping facility and getting it onto a yellow freight truck. And then I just got this, like, notification that was on its way. And it was going to be $1,700 to ship it, which was, like, right at the break-even point of what it would cost to, like, fly out, rent a U-Haul one way, like, sort it all out that way. And so I was like, okay, well, like, that's all right.

**Chris Gammell:** But then you're paying professionals too then, right? It's like, that's worth it.

**Dave Jones:** Yeah, yeah, exactly. Yeah, so I can externalize some costs and get them to handle that. And so then it showed up. And, you know, my neighbor calls me. He's like, the thing is here. And I was like, oh, okay. And, like, came down and checked it out. And he's like, yeah, they also billed us an extra, like, $900. Oh. And I was just terrified by this. And it turns out that they had, like, misweighed it at the shipping, like, depot where they had departed from. And they were off by, like, almost 700 pounds. And so Yellow Freight was very clear that I had to pay them that. And actually they made the plumbing company pay. And so I had to, like, scrape together what I had left in my savings and, like, shell that out. But, yeah, so quite a bit of money later, I now owned a robot that was sitting in a plumbing shop in Fort Collins, Colorado.

**Chris Gammell:** That is awesome. It was pretty great. That's the genesis of the story. That's like, you know, like the buddy cap story. This is how it starts. And then eventually you guys start solving crimes together and everything else, right? Exactly. Yeah.

**Dave Jones:** I have to pull them out of hard luck. Yeah.

**Chris Gammell:** Yeah. Oh, man. That's awesome. It was pretty fun. I have to say, like, I don't even know what I would think an industrial robot would cost. I mean, we have a surplus store here. But then I guess I wouldn't even think about the other costs to that. So that makes a lot of sense.

**Dave Jones:** Yeah. So they tend to go on eBay, like, in working condition for anywhere from, like, you know, $10,000 to $50,000 with, like, all the components and all the controller cabinets and cabling and all that. And so Fred, when I got him, it was clear that there was, like, no condition. These guys didn't know what it was. I mean, they knew it was a robotic arm. But beyond that, they were like, it's a thing.

**Chris Gammell:** It's orange. They knew that.

**Dave Jones:** Yeah. And not only that, too, but Fred was actually so old that the name printed on the side of it is Asa and not ABB. Oh, Asia, actually.

**Chris Gammell:** Yeah. Asia Brown-Bavaria, which is what ABB stands for. Yeah, it's the A, ABB. My former employer, as people know. Yeah, maybe. I don't know.

**Dave Jones:** Yeah, yeah. And, yeah, so that may have been another reason it wasn't, like, if people are looking for these arms, after 1987, I believe they're all.

**Chris Gammell:** Oh, yeah, yeah.

**Dave Jones:** They all became ABB arms. You know, ABB stencil on the side. Yeah. So that was, like, another reason he may have slipped through the cracks. So, yeah.

**Chris Gammell:** That's awesome.

**Dave Jones:** Yeah, it was pretty fun. Yeah, and then I, so, yeah.

**Chris Gammell:** And then the gift one, I feel like we have to just go to that real quick, too.

**Dave Jones:** Oh, well, so, yeah, that one came. That was kind of interesting. So I went to, like, when there used to be a big Kodak manufacturing plant in Greeley, Colorado. I'm sure they're still around. Yeah, no, unfortunately. Well, a piece of it is. But, so, what happened was when the plant was shutting down, they went to the, basically went to the high school and they were like, do you guys want this giant arm? And, you know, our robotics team basically at the school was like, absolutely, like, bring it in. And so then we had this arm in the high school, which, like, I was infatuated with and loved because it was the arm from, like, so many years ago. And it was, like, up and running every now and then. And, like, I would program it to move around and kind of, like, dance and do fun things. And our shop teacher was also the robotics team coach. And he used to go and put padlocks on it. The lockouts all had padlocks on it. And so, like, someone wandering through the shop class couldn't power up this, you know, 480 volt three phase thing in the corner of the room. And so I learned how to pick combination locks mathematically. And there's this, like, there's this process you can do to narrow it down from, you know, however many millions of combinations to just, like, 120. And, like, you know, if you really want to play with a giant robot, like, 120 combinations on a master lock isn't that much. And so I would sprawl this.

**Chris Gammell:** And here we already see a pattern appearing here. If you really want a robot, you either need to write pearl, which is painful, or pick locks, which is painful, or ship stuff, which is painful.

**Dave Jones:** Yeah, exactly. Yeah. And so I had these, like, big, you know, I just do all the, not even equations, just the patterns on the board to get these combinations. And then I just write them all out on the chalkboard in the front of the room. And I go and I pick the locks. And he'd just go and put two new locks on there. And I'd be like, oh, well, bummer.

**Chris Gammell:** But skip that writing step.

**Dave Jones:** Yeah, exactly. Just put it in a notebook or something. Yeah, it was all good fun. Like, I wasn't going to, you know, it was a three-phase 480 thing in his room. So I didn't want to exactly, like, send the thing through the wall while he wasn't in there. You know, get some aggression later. Yeah. But so what happened was I ended up going back and I was trying to mentor the team a little bit when I was at the university there. And he found out I had bought this robot and basically hit me upside the head and said, we're trying to throw this one away. Oh. Because, like, the EEPROM on it had, since it was only powered up, like, once a year, had ended up going bad. And so they powered it up. And it's just like, I don't know what I am. And all these fault lights would come on and it would shut down.

**Chris Gammell:** A robot with an identity crisis?

**Dave Jones:** Yeah, exactly. It was so great. And, but it was becoming, like, a risk at the school because people were, like, hanging on it. And it was just this giant hunk of metal in the corner of the room. And so he hit me and he's like, I'm trying to get rid of this thing. And I was like, whoa. You know, I'll take another one, I guess. And so basically, yeah, they were like, all right, take it. And so I came with two of my buddies and actually three of my buddies. It turns out every time you want to move a robot to it, it costs about three relationships. Because it is not, it's about, like, $200 in town plus, like, three good friends that you probably want to talk to a lot after that. Because there's a lot of, like, near-death experiences. Right, right, yeah. There's a lot of swearing, a lot of, yeah.

**Chris Gammell:** It sounds like my, I moved in Oregon once, like a Hammond, Oregon. And it's nowhere near as heavy. But, yeah, going downstairs almost killed some of my friends.

**Dave Jones:** Yeah, just moving this thing up, like, the ramp into the U-Haul. I mean, those things, it doesn't seem like a U-Haul is very high, but it is incredibly high.

**Chris Gammell:** The incline is crazy, right? It's like at least 15 degrees, which is, like, pretty significant when you start doing the physics problems.

**Dave Jones:** Yeah, exactly. So I ended up getting an engine hoist for the later moves. And I was able to just mount that to the side of Fred and then, like, engine hoist him into the back of the truck.

**Chris Gammell:** Oh, that's good. Yeah.

**Dave Jones:** Yeah, and that's, so that's basically when I was moving Fred out of the garage, then I had, I was able to do that. And so Lefty was actually never in the garage in Fort Collins. I had to, as soon as I got Lefty, I had to move into the warehome, which was, which was not, not a bright day. Yeah, I mean, it's like when you own two one-ton robots, they end up dictating your living situation a lot like two golden retriever puppies would.

**Chris Gammell:** That's right. Yeah, that's been my experience with dogs. Yeah, exactly. Which may be barred during this show yet. We'll see. Okay, so I want to move back. But before I do, I feel like I have to ask as well. You're now in San Francisco, probably the most expensive place to have robots in the world.

**Dave Jones:** Yeah, so that's a bit of a pain point. So right now the robots are in storage in Fort Collins in the most absurdly expensive storage unit because for some reason I wanted to make sure that they were like safe.

**Chris Gammell:** Like someone's going to go and take them at night?

**Dave Jones:** Like someone's going to take my robots.

**Chris Gammell:** Well, I just happen to have this engine noise with me. Yeah, exactly. It's so absurd.

**Dave Jones:** It's so absurd. But just the thought of losing them is just, I don't know. Yeah, it's crazy. It's crazy. I can say that definitively. But yeah, so the doors are individually alarmed in the storage unit and everything. And it's just crazy. It's crazy. But I do have two axes of Fred out here. I have the last two axes of, well, actually it's of a different robot. But it's the same, it's not Fred or Lefty, but I have another two axes of the identical model. Because Fred and Lefty are both ABB, IRB 2000 models.

**Chris Gammell:** Okay, that's good to know.

**Dave Jones:** So I got an additional, yeah, for those of you playing the home game.

**Chris Gammell:** Well, we'll link the data sheet or whatever we can find as well.

**Dave Jones:** Oh, yeah, yeah, totally. And so I have two, I have essentially the end effector sitting on my desk here in San Francisco. And so as soon as I can get the control system that I'm designing working on those two axes, then I'll be able to push it to all six or all 12 and be able to bring them out here.

**Chris Gammell:** 12 per robot?

**Dave Jones:** No, six per robot. 12 for Fred and Lefty, yeah. Right, right. And so once I have that control loop stabilized, I guess, then I'll look at getting like a hanger or something over in Oakland that I can.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, that's basically the only way to do it.

**Chris Gammell:** There's a new space over there too. Have you seen, what's it called? Something blue, I forget the name of it now. I met one of the guys at the hardware workshop, but it's a workspace over in Oakland.

**Dave Jones:** Yeah, there's a couple of places like that.

**Chris Gammell:** And it's like a live-in place though too. So like you could move there if you really wanted to.

**Dave Jones:** Yeah, well, I mean, after living in the warehouse, I got to say, so I lived in a warehouse for a year because of these two robots. And like I never want to live in a warehouse again. It was so awful. It was, there was just, there were so many things about that warehouse that were terrible.

**Chris Gammell:** Like what, like mice or weather?

**Dave Jones:** It wasn't bad about that, but it was just, yeah, there was no like, you know, definitely wasn't comfortable to live in like the heating. You know, the living situation was, you know, the kitchen was kind of sketched. The bedrooms, you know, someone was clearly like running a grow operation out of the back or something initially. And so it was like, it was all set up for, to have some people living in there. But it was, it was just, it was rough. It's hard to, it's hard to explain like how, why it was so bad, but it was, it's just always dusty. I had to, I rented out the garage space to a food truck because like they needed a place to park. But then I was terrified to go camping in Colorado because all my camping gear smelled like sausages. And so, you know, I was just going to get mauled by a bear as soon as I left the warehouse or the warehouse. But it was pretty fun. We came up with a game we called Warehouse Ball, which was just like kicking giant kickballs all around this giant empty space at each other. And yeah, it was, it was, there was a lot of things about the warehouse that were great, but there was just so many more that were terrible. So yeah, I definitely want to, I want to separate those two, you know, or when I had Fred in the garage at my, at the first house, that was, that was ideal.

**Chris Gammell:** Yeah.

**Dave Jones:** Even though he was kind of too big for the space. If he had ever gotten moving up in there, he would have gone through the ceiling and like.

**Chris Gammell:** Yeah. He makes his own space eventually then, right?

**Dave Jones:** Yeah, exactly. Yeah. He'll chisel out. Yeah. He'll make do. A little hemisphere around him.

**Chris Gammell:** He ain't going to stop the robot arm if it's not with that much power.

**Dave Jones:** Oh yeah. He, um, yeah, that, the first base was, was crazy getting the power up and running for him. Cause at the, at the warehouse, um, part of the move in was I made a deal with the, uh, the landlord to, um, to run a hundred amps of 220 into the back corner. Um, and that was like my, that's all I wanted from him. I was like, all I want is a hundred amps of 220 in this corner. And he's like, all right, sounds good. You know, and he.

**Chris Gammell:** It's like a dryer done effectively, right? I mean, that, that could be a dryer. A really large scale dryer.

**Dave Jones:** Yeah. And he, he knew it was for giant robots too. And that's why he kind of, he liked it more than I'm sure what the other grow operations were requesting for space.

**Chris Gammell:** But, uh, we need, uh, lamps cause we're cold personally.

**Dave Jones:** Yeah, exactly. All sorts of like air purification systems and all this, but yeah, I just wanted a hundred amps to 220. But, uh, yeah, at the, uh, the house I was living in when I, when I got Fred, uh, there was like a hundred amps service to the house. And so, uh, basically like setting that up to get like, you know, I put a, a 75 amp 220 breaker in there running to, uh, running to the garage. And it was basically like, if anyone else turned on anything in the house while this thing was running at full tilt, it would have just shut down. Yeah. It would have popped the breaker going into the house, which is kind of a cool idea. And the city of Fort Collins wasn't willing to run three phase to, uh, a residential property.

**Speaker ?:** Yeah.

**Dave Jones:** That's always tough. Yeah.

**Chris Gammell:** Cause it's lethal, you know, but I know a lot of, a lot of hackerspaces have to deal with getting that stuff installed. And like, that's, that's always expensive when you need three phase. Um, so, yeah.

**Dave Jones:** So yeah, I ended up, uh, selling my motorcycle to buy a rotary phase converter, which was kind of like showed the, showed the dedication to the project.

**Chris Gammell:** Yeah. Yeah. So, so the rotary phase converter actually takes it from one phase to three phases. Is that right?

**Dave Jones:** Yeah. So I guess, uh, the way these things run is, um, you put in single phase two 20 into it and then it does like, um, like a capacitor lag into the, the second, the second, uh, phase of the, of the motor and drives essentially based off this, like, you know, messed up waveform to get, you know, a three phase motor spinning. And then actually draws current off the, the third phase. And so then you get this like thing that approximates a three phase waveform. But, um, if you try to draw current really during the, during the third cycle, it will, there's no current really to draw out of the system. So it'll just collapse. And so, um, there's some, there's some issue with these trying to run, you know, cause the idea with, with these robots running on three phase powers, like at any minute they can go and spin and that's enough to like draw down the, the input voltage to, to nothing. If you're between cycles on single phase. Right. Right. And, um, so yeah, but, uh, you know, I never really, I mean the, the phase converter took like 10 amps just to spin the thing just to kind of like, yeah. That's true.

**Chris Gammell:** And that's like low speed spinning. We're talking here too, right? It's not like the super high, high jerk, like, uh, stuff that most, most industrial robots can do.

**Dave Jones:** No, no, this is 10 amps just to spin the phase converter. Yeah.

**Chris Gammell:** Oh, geez. Really? Okay. Okay.

**Dave Jones:** Yeah. Yeah. So it was not the most efficient piece. And then, and then I had two 23 phase and I needed three phase four 80.

**Chris Gammell:** Yeah.

**Dave Jones:** And so trying to find a three phase, uh, transformer was just impossible. And then, uh, one day on eBay or not on eBay on Craigslist, uh, there's this post from golden Colorado and it's this guy and he's like, Oh yeah, I got a, you know, a transformer and just wrote all the specs out. And I was like, Oh my God, this is exactly what I need. Like it was designed to step down for, uh, um, you know, some industrial facility and just run it backwards and get my four 80 output. And, uh, so I went to see this guy and it was just the sketchiest transaction I've ever been a part of. Like this thing was clearly like stolen off a construction site, like, or off a, off a demo site, you know, where they were tearing stuff down. He's like, you know, it was just in a dumpster. So I thought maybe I could get a couple bucks for this. And I was like, yeah, just help me get in the back of the civic and like, it'll be good. Yeah. Like I need this thing so bad that I don't, I don't want to know. I just, I really want this transformer.

**Chris Gammell:** You're like Doc Brown trying to, you're like buying the, uh, the plutonium from, uh, the Iranians, right?

**Dave Jones:** Yeah. From very, very reputable sources. Yeah. But yeah, I ended up having this like 300 pound transformer in the trunk of my car. And like, I, it was funny cause I bought it over, uh, like the break at the university. And so I got back home and all my friends were out of town and so I couldn't get it out of the trunk of my car. And so I ended up driving around. Yeah. I was driving around like that for a week with this like 300 volt transformer, just like bottoming out the back of my, my little hoopty. So yeah, it was, it was pretty fun. But I mean like new, those transformers are, um, yeah.

**Chris Gammell:** Oh, they're beefy.

**Dave Jones:** You know, three grand or something like that. And so I just brought a multimeter and owned it out and I was like, cool, it's good. Like I want it a hundred bucks. Yeah. That sounds great. Yeah. A hundred bucks and a six pack of beer. Even better. All right.

**Chris Gammell:** I'm sure he put that a hundred dollars to good use. I'm sure it definitely wasn't gone by the end of the day.

**Dave Jones:** Absolutely. Well, luckily, uh, luckily him and his buddy, you know, his, his toothless buddy there on this, this, uh, like sketchy little piece of property up in golden were able to help me throw it in the back of the car. And that's, that's all I wanted from them. I was like, okay, I'm out. Yeah.

**Chris Gammell:** You know, also, also a parrot head gives you, gives you like super strength. Well, I don't know.

**Dave Jones:** The, the, the most surreal part about all of this was they were parrot heads. So there's like all this Jimmy Buffett or, uh, not Jimmy Buffett. Yeah. Jimmy Buffett. Jimmy Buffett.

**Chris Gammell:** Yeah. That's right. Yeah. Yeah.

**Dave Jones:** Yeah. Yeah. There's this Jimmy Buffett stuff everywhere. Yeah. Yeah. And it was just like, only thing that could have made that more surreal was that these guys were like sitting out back listening to Jimmy Buffett and then like with all this, like, you know, this beach swag everywhere. It was so weird. Yeah.

**Chris Gammell:** Trying to raise money for our trip to the coast, man. Cause we're like in Colorado.

**Dave Jones:** Trying to get back out of golden Colorado. Oh my gosh. Yeah. But yeah. So then I had a three phase four 80. And my garage and Fort Collins, which was, you know, which was terrifying, but like exciting too. So, so wait, so, okay.

**Chris Gammell:** So now you had, okay. So explain the setup once again. So, so you had single phase two 20 coming into your house, right? Then you put it through this phase converter and then through the trans, that put it into three phase two 20 and then you stepped it up to four 80.

**Dave Jones:** Yeah. Yeah. So I had, um, yeah, basically after the, after the rotary phase converter, I had a, um, uh, a box with a 14 KVA relay in it because it was like the only, and at which I had a, I had a hog trade for because like I needed something that was at least, uh, I think, I think it worked out to be like at least four, four and a half KVA with like some margin that I want to make sure that like this trend, this relay would handle. Cause I had to turn on the transformer with the, uh, after the rotary phase converter was started. Otherwise it could, um, depending on the state of the super stuff, right? Yeah. Yeah. I could just blow up my rotary phase converter, which was like at the time, like the most expensive thing besides the robot I had purchased yet. And so I want to protect my investment. And, uh, I ended up trading like three, one KVA relays for this like monster thing. I mean, it's, it was the size of like one of those small tissue boxes and.

**Chris Gammell:** So you have to like hot source this in then? Is that the idea? So you have the. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** So I had that relay going to like a switch box on the wall and then the relay was mounted to the, to this plywood board that was mounted to the wall. And when you would throw the switch, it would just reverberate through the wall. This like contact. And it just made this wonderful like drum beat on the wall as the, uh, as the transformer came on and the transformer would start to hum. And then you, you boot up the, you turn on the robots, uh, uh, power supply, which was, yeah, which was pretty exciting.

**Chris Gammell:** That's right. Folks, mad scientists. And did you have a knife switch too? Is that, did you have a knife switch just for the relay? Just a, you know, five volt knife switch.

**Dave Jones:** I wanted everything like as far away from me as I could because like, I, I mean, I don't know. I, I played with, I played with some things. There's this like blind gap in my, in my electronics. I don't know if it's like this for, for other people too, but like zero to like 48 volts. I'm like totally fine with like, I don't care. I got that. I'll do, I'll do a hundred amps at five volts. Yeah. I was like, whatever, I don't care. Then from like 48 to, to one KV, I am just like uncomfortable. And then above one KV, I'm like, everything's fine. Like I got this, like, I know what to watch for, but like, there's this little area in the middle that just scares the hell out of me. And, you know, Fred was smack dab in the middle of that. So I have like, you know, 600 volt probes and I'm like on the output of, like I put the output of the transformer initially before I wore it into the robot, just into a, you know, a monster contact switch. So I could just measure the output voltage or the phase voltages. Yeah. And I like, I was sweating bullets, like with, you know, these probes that are supposed to be fine, you know, at 600 volts. But yeah, it was, yeah, it was still, it was still nerve wracking, like putting that into a Harbor Freight multimeter. I'm like, oh my God, don't explode. For the love of God, please.

**Chris Gammell:** I'm more curious about the above one K that you're okay with it though. That's, that's what's interesting to me. Like the, like how does it stop being scary at that point? Is it just like, well, I'm definitely dead if this happens, right?

**Dave Jones:** No, no, it's, it's just the opposite. It's like all the tools, all the tools above one KB are like clearly, clearly like listed for these activities. Like you have high voltage scope probes and high voltage, like you're always, when you're measuring something, you're holding onto a stick that's like, you know, four feet long and you have like these giant grounding probes and like, you know, you always have, you know, even with this stuff, you always keep one hand behind the back. And stuff like that. But still it's, you know, there's just something about like the, the stamped 600 volt like probe that you just see on there. It's like 600 V and you're like, really?

**Chris Gammell:** Like, maybe I'll get my ruler out and measure the, uh, the, the creepage and clearance distance again. Yeah, exactly. And you're like, how dirty is this probe?

**Dave Jones:** Yeah, exactly. You're like, well, I was using this in the backyard and like the soil moisture sensor last week. There's a little bit of dirt on it. Like, am I going to die? And like, I don't know. It's yeah. Yeah. So, but above like, above one KV.

**Chris Gammell:** So like, so like the one KV is like, you start looking like photonic induction kind of style. Like you've got like the, you start speaking in that thick, thick British accent and using sticks to touch everything.

**Dave Jones:** Well, um, yeah. Cause like, I don't know, since I was 16, I was in labs that were, um, like using Pockle cell, uh, switches, which are like switch eight KV. And so like, you just knew, like you did a lot of high voltage training before you like started reaching over the optics table. Yeah. And, um, and then, uh, yeah. And actually when I was getting Fred up and running, I was working on, um, like 50,000 volt systems and yeah, 50,000 volts, 20,000 amp pulses. Yeah. So it was.

**Chris Gammell:** Okay. I have to call it here, Sean. We have to go, we have to go back to the beginning and then we're going to move our way forward. Cause I think we've had, we've had a half hour now of, of robots and awesomeness, but we got to start from the beginning and figure out who the hell are you? Because there must be some kind of Genesis story where you got struck as a lightning, struck by lightning as a kid or.

**Dave Jones:** I, you know, I don't know. It may have just been an artifact of, of where I grew up. So.

**Chris Gammell:** So where'd you grow up?

**Dave Jones:** I grew up in Fort Collins, Fort Collins, Colorado in this, in this little part of the city that was up North. And it ended up that like a lot of my neighbors were professors at the university.

**Chris Gammell:** And which university? Sorry. Is that.

**Dave Jones:** This is a Colorado state up in Fort Collins. Okay. Yeah. And, uh, so, you know, I'd be out in my driveway and I'd be like trying to make a, you know, rocket fuel because I got kicked out of the house. I had, uh, I was cooking, I was cooking, like I was melting sugar and salt peter on my kitchen stove. And, uh, and my mom's sitting over at the kitchen table and she's like, is this safe? And I'm like, it's totally safe. Like, there's nothing that can happen. Like once it, yeah, I was like, once it melts, I just pour it into the rocket engine and then it's done and it's awesome.

**Chris Gammell:** And the only time I've ever read salt peter was in the anarchist cookbook junior. That's the only time I've ever read it. So is that where you got it from or is it somewhere else?

**Dave Jones:** No, no. I found it. I found it. I mean, by an equally reputable source, it was by some, some website online that was, uh, talking about 5 cent sugar rockets was the, I remember the name of the article and, uh, it was just sugar and salt peter and you mix it together and you put it in a tube and it will send a rocket up and, you know, rocket engines were very expensive. Yeah. You know, $4 each. Like, yeah, seriously. Yeah. Who could do something like that at, you know, geez, I don't know, it was like 12, 13.

**Chris Gammell:** Well, and when you're 12, you want to iterate, right? And by iterate, I mean blow the crap out of everything you see. So that's, yeah.

**Dave Jones:** Bigger and bigger.

**Chris Gammell:** 5 cents each one is a good, that's a good deal. Yeah. Yeah.

**Dave Jones:** Yeah. It was pretty good. Yeah. So, um, but I ended up, uh, the, the fuel mixture on the stove ended up igniting. And so there was like this six foot purple flame coming out of like this little pot and I'm terrified. And I go running around the corner to get the fire extinguisher and which, you know, it's totally dead, but I, uh, I come back around the corner and you know, my, my mom has like casually gotten up from the kitchen table, like put a lid on the pan, put the pan in the sink and you know, the, and hence it's extinguished the flame. And she looks at me and she's just, she goes, no more in the house. And that was just the most amazing line. And I'll never forget it because it wasn't no more. It was just like, if you do this, do it outside.

**Chris Gammell:** It was implicit approval from your mother, which is like, well, how are you not going to be building rockets and crazy shit for the rest of your life?

**Dave Jones:** Exactly. And so I was out in the driveway, like a, you know, must've been a month or two later and I'm mixing my sugar and salt, Peter. And basically I'm just making these little smoke bombs on the driveway and they're not really doing anything. And it turns out my neighbors have affectionately coined me bomb boy at, you know, at this.

**Chris Gammell:** And they're going to kill people or he's going to be in NASA.

**Dave Jones:** So one of the two, one of the two, they gave me the benefit of the doubt for, for science. But, um, that's good. One of the, uh, one of my neighbors came over who's a professor at the university and he's like, Hey, show up. What'd you make it? I'm like, I'm making rocket fuel. And he's like, do you know what a covalent bond is? And I'm like, you know, I'm 12, 13. I'm just like, no. And he's like, he goes back over across the street to his house and he comes back with this like college level chemistry book. And he gives it to me and he says, when you can tell me what a covalent bond is, I'll tell you what you're missing. Holy crap. Best way to teach someone ever. Yeah. It was, it was amazing.

**Chris Gammell:** And it's like, that's like in like a legend of Zelda where it's like, you have this quest and once you've completed this quest, I will give you the key to the next thing. And it's like, in this case, it's just covalent bonding.

**Dave Jones:** Covalent bonding. Yeah. And you know, I, I flipped to the index and I like, you know, memorize what it says, like word for word. And I go across the street and I'm like, yeah, covalent bond is my two atoms sharing outer valence electron. And he's like, what does that mean? And I was like, I have no idea. He was like, go back. And you know, and so like a week or two later, I go back with like a barely, barely, barely like passing understanding of, of what a covalent bond is. And it was enough to have him say like, you need sulfur. And I was like, oh, okay. And so like, I go to the, the pharmacist that was downtown and I'm like, I need sulfur. And they were like, all right. And they gave me like a little jar of sulfur. And like, so. Sure.

**Chris Gammell:** You're a kid from the suburbs. We'll give this to you.

**Dave Jones:** Yeah. I mean, I got salt Peter at the Walmart pharmacy. Like I always remember this. I'm like, I need salt Peter. And they were like, okay. And they gave me a bottle of it and it was like $3. And I was like, oh, okay. Like that sounds good. I mean, the sulfur was like four, you know, it's like.

**Chris Gammell:** Well, you don't look like a bond builder yet because you don't have a beard. So. Yeah, exactly.

**Dave Jones:** I'm under 18. It'll all be expunged. But yeah. Yeah. So the, um, yeah. So then I was, I was making rocket fuel until like, it started to give me headaches that the fumes. And I was like, all right, enough of this. And I started tinkering with like, and that's how I started getting into electronics because I was like, wow, wouldn't it be cool if like I could launch a rocket on a timer? And so all of this is now like, and that's, that's where I got out of the anarchist cookbook was it was like a time detonator, you know? But I was like, oh, I can use this for like launching rockets. And, you know, it's totally innocent, but like horrific, like things to build. But, um, yeah, so I went to, uh, to, uh, Radio Shack and picked up like all the little parts and I had a little timer that would launch, uh, Estes rockets, which was just the coolest thing ever. You know, I'd have a five, a five second countdown that I could see. And then, you know, a 10 second hysteresis on whether or not the rocket would go. So it was like a five timer or something.

**Chris Gammell:** Is it basically like what it was or something?

**Dave Jones:** It was just a, it was a $2 kitchen timer. And then the beeper wired into a little NFET circuit.

**Chris Gammell:** Oh man, that does look like a bomb.

**Dave Jones:** Yeah, I know. Right. Yeah. So anyway, so that was like, you know, junior high and that started to fade out. And then, uh, you know, I went to Thai school, moved to Australia for a year. Whoa. Yeah, that was, uh, or I guess it was like, it was like half a year. It was super fun. Which city? Just as an exchange student, uh, to Melbourne.

**Chris Gammell:** Melbourne?

**Dave Jones:** Uh, Melbourne, Melbourne, Australia. Yeah.

**Chris Gammell:** Right. Right.

**Dave Jones:** Lived out in the suburbs. Um, Nice. Yeah. And it was, uh, yeah, it was super fun. And, uh, but then I came back.

**Chris Gammell:** If Dave was here, he would, he would approve. I'm sure.

**Dave Jones:** Yeah, absolutely. Yeah. The, the, the, the suburb I was in was a little, little sketchy, but, um, it was super fun. And then, uh, yeah, I, uh, came back and went to school and then in high school and our physics class, we had the option to go and do this, uh, lasers, um, class at the university. Yeah. Yeah. It was like, come play with lasers after school for like a week. And at the end there'll be a pizza party. And I was like, Oh, okay. Sure. And so.

**Chris Gammell:** Still works for big kids too, though, by the way. Yeah. Exactly. Pizza's a pretty strong motivator.

**Dave Jones:** Everybody wants punch and pie. More people will come if there's punch and pie. Punch and pie. Yeah. Tell them there's a free hat. Exactly. So, yeah. So I ended up going to this lasers workshop at the university and, um, I grabbed a, um, basically at the, at the end of the, uh, at the end of this workshop, they, um, did an exit interview. And part of the interview was like, if there was a, you know, a position for research, like a research assistant, would you be interested in coming? And I just like lost my shit. And I was like, to work in a big, like NSF lab, that would be amazing. Like I want that more than anything else. And, and this is still in high school, right?

**Chris Gammell:** I mean, this is like high school.

**Dave Jones:** I was like 16. Yeah. Um, and so this video ended up being shown to the lab director and he saw my like, you know, outrageous excitement about coming and playing in a, in a research lab. And they gave me a, like a stipend to come and hang out over the summer. And I like use solid works to design optics mounts and vacuum chambers with a, uh, you know, an undergraduate student. So I was like a, I was like an undergrad's undergrad.

**Chris Gammell:** So as I was like a low, the lowest of the bottom on the totem pole.

**Dave Jones:** Yeah. I was a helper to an undergrad, you know, I had no authority, you know, and we're working

**Chris Gammell:** for this, uh, we were working on this philosophy from an undergrad, right?

**Dave Jones:** Exactly. Yeah. Yeah. It was a super classy, but, um, yeah, he was, he was brilliant and I was, uh, you know, it was really fun to work with him. Um, and so we, you know, we designed these vacuum chambers and it was super fun. And then, uh, the university got a CNC for that lab at that time too. And so like I would, I would run parts on the CNC, which was great. And, you know, I, some of these parts would take 24 hours to machine like these monster, you know, grading mounts that I had designed. And it was really cool to design this, this optic mount to hold like a, you know, a quarter million dollar piece of glass and then be able to go down and like machine it.

**Chris Gammell:** And so I would have a machining or what?

**Dave Jones:** Yeah, it was all aluminum. Yeah. And, you know, I put this 14 by 10 by five inch block on the, uh, on the mill and like try to figure out how it was like the least number of faces I faces I had to, um, face to be able to get this thing to like the final shape I wanted. And, uh, yeah, I ended up like running the CNC like for 24 hours at a time. Sometimes I just sit down there and like listen to music and hang out and watch this thing cut. And, uh, word ended up getting to the machine shop guys that I had, uh, operated the machine for 24 hours and this was totally unacceptable. And, um, you know, it violated the curfew of the machine shop, which was, you know, 1130 at night or something like that. And so I was banned from the machine shop for one week. And, uh, my, uh, the advisor, the, my advisor, the professor I was working for wrote a little note on the email and posted it up on the wall and it said, he deserves an award.

**Chris Gammell:** Yeah. Badge of honor.

**Dave Jones:** Yeah, exactly. And so that was up on the wall for a while. And so that was like.

**Chris Gammell:** I think most people that have been in machine shops, especially if there's like college ones with overbearing, I, we had a overbearing, you know, for the right reasons, of course they're overbearing because they don't want someone cutting their fingers off, but it's like. Yeah, exactly. You know, if you get kicked out, it's like, it's pretty standard par for the course. Right. I mean, like. Exactly.

**Dave Jones:** It's a badge of honor.

**Chris Gammell:** 24. That's that, that is a badge of honor. So that's cool.

**Dave Jones:** Yeah, exactly. Yeah. And so I was like 17 at the time. And, um, and that was like my, my second summer at the lab. And, um, so, or I guess, yeah, that was my, my second summer at the lab. And I kind of got a, um, my second summer, I was working directly with a group that was working on, um, chirp pulsed amplification lasers building, um, ultra. Uh, the, the lab was the national science foundation center for extreme ultraviolet science and technology. And so we were working on developing laser sources, uh, with incredibly short wavelength. So, um, down to the, the last one that I was there for was a 9.9 nanometer laser.

**Chris Gammell:** Is this for doing like, uh, etching for like the rest? It's for everything. Yeah.

**Dave Jones:** Yeah. It's for, um, lithography and, uh, microscopy and, uh, basically trying to get like within the water window so you can, you know, image cells and things like that. And so we were working on the source development side of it. So trying to make like a hundred Hertz, uh, 46.9. Well, later I was working on the 46.9 nanometer laser, but, um, yeah, basically we would, uh, generate this incredibly high energy pulse and then create a plasma. And then we would use that plasma as our gain medium for the laser. And so depending on the material, um, you'd create this, this line focus on the side of the, um, on the side of the target and then generate a plasma from that. And based on the material, um, you get a population inversion that would be, that would create a, uh, when you sent your seed pulse through, it would send, create a laser of, um, the wavelength depending on the material. So you would get really, really short wavelength lasers, like 9.9, which I forget what the material is, but yeah.

**Chris Gammell:** So I've always been confused about that with lasers too. So it's like you basically stimulate some external material and that basically then outputs this short, short wavelength light.

**Dave Jones:** So, so basically you create, you, you, um, you send a, um, geez, I'm spacing the name of it, but, uh, you essentially like charge up a material.

**Chris Gammell:** Okay. So like a piece of electric almost effect or what?

**Dave Jones:** Uh, it's more, um, you excite the, um, the electrons into higher shells that are unstable.

**Chris Gammell:** Oh, and then when they decay, they decay.

**Dave Jones:** Yeah. When you send a seed pulse through, you actually can, um, so, you know, laser is for spontaneous emission, um, of radiation. And so we can actually, yeah, that's the SE of laser. Yeah. And so if you send in a pulse, um, and if you basically time it right, that you create this population inversion. So all these electrons are hanging out at their, um, high energy states and you send, you send in a seed pulse. Basically all of these start, uh, cascading as this, as this, uh, pulse is going through. And so all the energy from this, this charge pump, that's what it is. The charge pumped, uh, glass or depending on what you're using, um, then you can actually extract that energy that you've put in via, like, if it's a, um, you know, a flash pumped laser, they'll actually use, um, arc lamps to generate this like incredibly bright pulse that will charge this glass. Yeah. You can think about it as like a capacitor analogy that you're storing all of this charge.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. And then discharging it when you, you know, connect it to ground. So it's like a boost converter almost, right?

**Chris Gammell:** It's like, uh, you keep putting these smaller pulses in, it builds up, builds up, builds up, builds up, and then it, it decays and it outputs this crazy.

**Dave Jones:** Mm. Yeah. This crazy amount of energy.

**Chris Gammell:** But that's not really a small, small time scale still, right? Like it's like, yeah, you're putting in super small pulses and then, but then eventually it outputs. Man, that's bonkers. That's bonkers.

**Dave Jones:** So we, um, what we were working on, which was kind of cool was, uh, uh, uh, most of these, uh, you know, titanium sapphire lasers are, are pumped with, uh, arc lamps. And so you send in this like huge amount of energy to charge up this, this glass. And, uh, so what we were doing was, um, using lasers to, uh, uh, set wavelength to actually charge the glass. So it was a solid state version of this, um, or a charge or a flash bulb, uh, less version of this same laser. So, no, it was really fun. Got to play with a lot of like liquid nitrogen and stuff like that. So.

**Chris Gammell:** And this is still at 17, right? I mean, like this is like.

**Dave Jones:** Yeah. Yeah. This is 17.

**Chris Gammell:** That's awesome, man.

**Dave Jones:** It was super fun. And that's, you know, where I started to get experience with the high voltage stuff and, you know, and then also the neighbors too, like, uh, for, I was in the international baccalaureate program in, in, uh, high school. And for the end of that, you have to write, you know, a thesis. And, uh, I ended up doing mine. It was called like the critical temperature, a study of type two superconductors. And, uh, uh, I ended up having a neighbor who had started a superconductor manufacturing company. And I went to his door and I knocked and I was like, can I have a superconductor? And he's like, uh, mow my lawn and I'll give you a superconductor. And it's just like the weirdest thing.

**Chris Gammell:** I think, I think right now about 4,000 nerves want to move to Fort Collins for any potential progeny they have. It's like, uh, yeah, that sounds like a good place to be.

**Dave Jones:** It was a pretty, it was a pretty great place to grow up. Yeah. And so, yeah. So I got a superconductor for mowing, for mowing, uh, my neighbor's lawn. And he was just like super cool about it and told me like that if I just went down to air gas with a coffee thermos, they would fill it up. And I was like, really? I was like, cause I, then I had this, you know, another problem of, I have this toy, but I don't have any of the means to play with it. And it turns out like you just go down to, uh, air gas with a, like a vacuum jacketed coffee cup. Like you get a really nice one where the lid does not seal. And so it was very, very clear on that.

**Chris Gammell:** Uh, and then it doesn't like expand or something. Is that the idea? Yeah.

**Dave Jones:** So it doesn't explode. Yeah. Yeah. Cause, uh, it's definitely, you know, coffee, coffee thermoses aren't designed to.

**Chris Gammell:** Yeah. Be volume tight kind of thing. Right. And hold pressure.

**Dave Jones:** Non-explosively vent and all this. So.

**Chris Gammell:** Yeah. If your superconductor wants to get out, you just let, let it out.

**Dave Jones:** Right. Exactly.

**Chris Gammell:** Just let it out.

**Dave Jones:** It was, it was so much fun. But then I just like, I cut the bottom out of a little styrofoam cup and set it on the table and set my superconductor inside of it and poured in liquid nitrogen until it, you know, froze. And I'd set magnets on top of it and just spin them and then sit there hovering in space. And it was so cool. So the superconductor.

**Chris Gammell:** So what, what's the material type of that?

**Dave Jones:** Oh, geez. It was, it was some like, yeah. Uh, it was some crazy like you tribium. Um, I don't even think I'm saying that right. Uh, you turdium. I don't know. Iturea. Yeah. Something like that. Yeah. It was, it was, there was five or six chemicals in it. I know there was a six involved. Yeah. That's about, it's about all I remember. Okay.

**Chris Gammell:** So the idea is, so when you went to air gas, you were just getting nitrogen. You're saying you're just getting, Oh yeah.

**Dave Jones:** I was just getting liquid nitrogen. Yeah.

**Chris Gammell:** Okay. Oh, okay. Yeah. So anyone, anyone can go down there. Is that the idea?

**Dave Jones:** Yeah. Anyone can go. It's yeah. That's something you like everyone should do at some point is go and get like a coffee cup full of liquid nitrogen. Um, geez, I think they charged me like $4 or something because it takes about a gallon of liquid nitrogen to fill a coffee cup because it has to cool the, cool the vessel. And you know, by the time you get home, you might have like, you know, three quarters of it left. But I mean, if you want to like make liquid or dipping dots or something at home. Yeah.

**Chris Gammell:** That's what a lot of the, a lot of the parties, some, not a lot of, I don't go to many parties, but there is some of the one or two of the parties I've been to in the past. They've done liquid nitrogen ice cream. And that's, I mean, that's tons of fun. I mean like super smooth and delicious.

**Dave Jones:** Yeah. Yeah, absolutely. For my, uh, uh, when I was, uh, leaving to, to, uh, go to Antarctica, um, I ended up having a, uh, my going away party. We made liquid nitrogen martinis and that was super fun. That's nice. Yeah.

**Chris Gammell:** So when do we get to hear about that stuff? Come on. Where you're, we're getting there. I know we are. We're getting there. Yes. We must ask Sean. I knew that.

**Dave Jones:** Yeah. So I, um,

**Chris Gammell:** we should also talk about electronics at some point too, cause that's what you do now,

**Dave Jones:** but probably. Yeah. Yeah. Definitely. Tiny spaceships are exciting. Um, but, uh, yeah, so, uh, I graduated high school and I, you know, didn't really, wasn't really ready to go to college. I was still working in the lab. So I was, uh, that was my, um, third summer in the lab and they said I could stay as long as I wanted. And, um, I started to get involved in more like electronic design and like not really design, more like electronic troubleshooting and like fixing, um, fixing systems that were like, cause a lot of these like weird physics things, they make one of them.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, you call the support line. It's like some dude in his garage and he's like, uh, yeah, I built that like 30 years ago. I have no idea.

**Chris Gammell:** Exactly. Right. Cause they, I mean, they can't afford it. And it's probably if they built 30 and one of them worked, that's usually what it really is. Right. It's not exactly. It was like, this was a miracle. Yeah.

**Dave Jones:** They're unaware that like they're dependent upon the avalanche transit transistor like that they put in by accident.

**Chris Gammell:** Right. And it's like, we really don't know how this works anymore, but it, it gives us the results we're expecting. So we go with it.

**Dave Jones:** Yeah, exactly. Yeah. And so, um, basically I had met someone the year before who worked in Antarctica and you

**Chris Gammell:** know, this big surly guy and he was, he had a beard, he had a beard, he had a beard,

**Dave Jones:** he had a beard and a temper. Yeah. He was a, he was a character.

**Chris Gammell:** Yeah.

**Dave Jones:** But, um, so he's like, oh yeah, I work at the South pole. And I was like, well, that's cool. And I was like, how do I work at the South pole? And he's like, well, you know, you could apply to be a general assistant, which is like, you know, something that someone with, you know, a high school education could probably pull off. And I was like, okay. And, uh, so he, he gave me some kind of hints on what I, what I needed to do to get like involved in the program. So things like I worked, I worked for a year or not a year, but like probably, probably a few months as an unpaid intern at a tractor supply company.

**Chris Gammell:** Oh, the, uh, the store, right? That's like, uh, the retail store.

**Dave Jones:** Well, it was, uh, basically like a big tractor company. Like they would sell the equipment.

**Chris Gammell:** Yeah. Well, they, they do, but they have like the front end store too, where they, they sell like farming, farming supplies and stuff like that. Yeah.

**Dave Jones:** Yeah, exactly. Yeah. And so I ended up working there just to get experience around heavy equipment. Cause that was like important, uh, you know, if you were going down there and all this other stuff and like basically just like boosted my resume and like any way I could to, to make it seem like I was qualified to shovel snow. So, and I did like deep, I did like, I worked with a, the Larimer County and did like a deep snow survival course. And so I went to that and like all this other stuff just to kind of get my, like, you know, to, to look like I was qualified to go to Antarctica, whatever that means.

**Chris Gammell:** I really, really, really wanted to not see people for the next six months.

**Dave Jones:** So exactly. So I ended up getting the job and I, um, flew down. Yeah, it was, it was pretty exciting. And so I flew, uh, you fly from, you fly, well, I drove to Denver for training. They do like a couple of days of training in Denver, all about your extreme cold weather gear, all this stuff. Um, then I boarded a flight to, uh, LA, LA to Auckland, Auckland to Christchurch, New Zealand. And then in Christchurch, there's a big clothing distribution center. And, uh, we went and basically you get all your, these two big orange duffel bags, uh, of extreme cold weather gear. And it's all your parkas and your, your boots and everything and a bunch of socks and stuff like that. And you know, what you see every time you see a picture of someone from Antarctica, it's like the red jacket and the black pants. Yeah.

**Chris Gammell:** I too have seen, uh, I was going to say, uh, happy feet right at the end where they,

**Dave Jones:** exactly. So we all look like, yeah. Yeah. Um, and so, yeah. And then I flew to McMurdo station, um, which is on the coast. And, uh, basically we hung out there and met some of the other pole leads as we're called, um, that were going to pole. And then we took off, uh, from McMurdo and we're flying for about like three hours or so. And we get like, we get over the South pole. It's three hours from McMurdo to the South pole, three and a half. And we're flying around and the pilot comes on and he's like, uh, it turns out the weather is closed in the pole. We have to go back to McMurdo. And we're like, oh, great. And so we're like literally overhead where we're going, but we can't land because the weather's closed in. And so we turn around and you know, the aircraft has like eight, nine hours of fuel on board. Yeah.

**Chris Gammell:** They're really ready for that stuff. Right.

**Dave Jones:** Yeah. Because there's no, there's no ditch airport to go to, you know, there's nothing between McMurdo and South pole. And so we start flying back to South pole and the pilot comes on and he's like, you know, after about an hour and a half of flying, he's like, turns out weather's closed in at McMurdo. So we're just going to keep flying.

**Chris Gammell:** And hope something opens up. Yep.

**Dave Jones:** Yeah. And I hope something opens up. Yeah. And so we, we end up circling over McMurdo for like an hour and the pilot just keeps diving into like the worst turbulence I've ever been in, in my entire life. And I have my parka on inside out. The people on either side of me are, you know, losing it into the flight bags. The, and we're sitting in cargo netting on the side of the plane too. There's a little LC-130 like Hercules aircraft. The L is because it's equipped with skis. So it's this, this like giant four propeller cargo plane that is just in violent turbulence. The air force load master in the back of the plane is throwing up as like, you know, this is this guy's job and he's losing it. And we just keep diving and diving and diving. And finally we just hit and we, uh, end up like kind of bouncing around for a while and then coming to a stop. And, you know, everyone's like cheering and celebrating and, you know, pilots like we made it. Woo. And, uh, on my second trip, I ended up talking to someone who was on the runway and they said that we came down so hard that we ended up going up on our front ski and then landing back down on level. And yeah, so it was, uh, it was super fun times. Um, and you know, we're in the bus on the way back and we get like a notification from, uh, over the radio that like going back, like, you know, eat some food and then we're going to try again in a little bit. Uh, and everyone just got off this plane and we're like, yeah, it was like, I, you know, I had like, I had come to terms with death at that point. You know, I had my jacket on inside out and I was thinking like, you know, at least I made it to Antarctica. So, you know, it's, uh, it was snow. Yeah. Yeah. It was fun. But, um, yeah. So I ended up going back to McMurdo. Um, luckily we don't take off later. Um, who was it? It was, uh, uh, and, and Curry of the, the today show was on, on our flight too. So that was kind of funny. Um, cause she was doing some, some bit at the, at the South pole. Um, but yeah, we ended up, uh, uh, getting some food and then like, uh, you know, a week later to take off and make it to South pole and ended up, uh, shoveling snow for the ice cube neutrino observatory. I worked as a, as an iron worker for a little bit, which was super fun. Um, you know, basically doing like cargo stuff or wait, no, no, no. Like, uh, like sling and steel. I was, uh, putting together, uh, I was on the iron crew, like helping them for a week, which was really fun. And they were all from Boston, uh, building one of the new, uh, new buildings at a pole. It was a logistics facility. We were putting together the skeletal structure for that.

**Chris Gammell:** And so learn about like a crane operations or how does that work?

**Dave Jones:** Oh yeah. So, um, so I, this is in November I was arriving and, uh, from November to February is like the build season basically where, um, you know, everyone comes in, the population swells to about 250, uh, temperatures, temperatures are warm. You know, it's all, it's pretty much above zero negative 55, uh, negative 55 to average temperature is about negative 20 Fahrenheit. Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. And, uh, and then, uh, towards the end of the winter, temperature starts to drop off and it's actually not that cold. It's a, it's a dry cold. So the South pole has a lower relative humidity than the Sahara.

**Chris Gammell:** Yeah.

**Dave Jones:** And so it's, you know, while it's negative, you know, she's, I don't know, negative 20 outside, if the sun's beating down and you're, you're actually working outside, it's, it's not hard to, to work up a sweat even in a, like a, you know, a sweater, a light sweater. Huh. So it's kind of, yeah, it's kind of interesting like that. And then we all get back to New Zealand and it's like freezing at, you know, 60 C with a hundred percent humidity, you know, it's like, yeah. But, um, yeah, so I ended up working, uh, a whole bunch of random jobs down there. And then, um, the, the most fun was working with the, uh, the bicep team and the ice cube neutrino team working on, uh, like just kind of hanging out with them and seeing what they were working on and, uh, deploying the, the detectors for the ice cube, uh, observatory. And then, um,

**Chris Gammell:** Wait, wait, wait, you gotta explain what that is. I know that. Oh. So like the neutrino detectors down there, cause it's like super deep, is it super deep or it's just super quiet down there? Yeah.

**Dave Jones:** Yeah. It's, um, so the South pole sits on a, a two mile thick glacier or like two and a half mile thick glacier that moves 33 feet a year, which is kind of crazy to think about. But, um, so if you drill down two miles under the station using like a hot water drill, um, there's so much force compressing the snow that the ice, the, the bubbles in the ice, uh, become like essentially non-existent. And so you end up with having this layer that's about two miles down. That's as clear as glass.

**Chris Gammell:** It's like a low pass filter for everything, right?

**Dave Jones:** Exactly. Everything just gets crushed into nothing. Yeah. And so what they do is they drill down two miles and they put these strings of, uh, they're called doms, the digital optical modules. And they're basically like basketball size PMTs or a photo multiplier tubes. And, uh, so then, uh, you know, the whole freezes up and they have this square kilometer grid of these, um, of these doms. And what is dom again? Digital optimizer, uh, digital optical module. Yeah. And so it's all the circuitry and the, and the photo multiplier tube. And, um, basically what happens is, um, if you have a neutrino that, uh, I think this is now, I'm, I should preface this by saying I'm not a particle physicist, but, um, the, I think what happens is that when the neutrino passes through the nucleus of, um, uh, atom of water, right. Or in an atom in water, um, it ends up passing through the nucleus faster than light can travel through that media. And so you end up with this cone of light, which is, uh, the, uh, um, it's not, it's not Kirchhoff radiation. Uh, it's, um, uh, it's the same reason why reactors glow blue.

**Chris Gammell:** Oh, interesting. Interesting. So basically it's, uh, some kind of physics-y effect. Yeah. Yeah. So it puts off light though. So basically, and I know that like, like every time you hear neutrinos, it's always like super deep in, in the, like as, as deep as you can get in the crust of the earth, basically, because you want to basically, because neutrinos will pass right through the earth, right?

**Dave Jones:** Yeah, exactly. They, they, there's trillions of them passing through your pinky at any moment. Yeah. They're just, they're going through everything. Yeah. Uh, Cherenkov radiation. I don't think I'm pronouncing that right, but yeah, the InstaGoogle. Um, but it's the same reason why a nuclear reactor glows blue is it's, but basically so in, you know, so deep down, uh, below the ice, it's filtering out like any other particle is, you know, being slowed down by this two mile thick wall of water. Cause water is a great, um, you know, barrier to this stuff. And, uh, so what you'll get is this, this single event that you can actually then trace back to the cone. So you get a cone of light, um, and that, which is the shock wave, the, you know, this optical shock wave, as I understand it. And then from that, you can actually trace where that neutrino came from. And the idea behind these detectors is that when a supernova goes supernova, like as the star is collapsing, um, and the explosion begins, you get this like explosion of neutrinos before you actually get the explosion of the star. And so it takes like three hours or something for this, this explosion to, to pass through the material for this reaction to occur. And, but the neutrinos aren't slowed down by all the mass of the star. So they just take off. And so my understanding of the purpose of these detectors is they act as a, like a first notification of a supernova. And so you can then take all of your optical telescopes and turn and observe this event that occurred as, you know, that you got the early notification for.

**Chris Gammell:** There's something about Ada Karen A. I've been watching Cosmos lately and they've been talking about Ada Karen A and how that's like a hypernova. And there's, there's something coming big there. They don't know when or how, but I think it's actually part of that basically. Yeah.

**Dave Jones:** Yeah. It's, I don't know, but anyway, so, so there's, there's some particle physics. Um, but, uh, so I ended up hanging out a lot in the, in the radio shop was there at South Pole. Um, just because like there was a bunch of broken band equipment and the Nintendo 64 had, uh, had no connection to the TV. Like the plug was missing. And I was like, well, I was like, that has to be fixed. You know, I was, I was 18. Um, uh, you know, there was another guy there, uh, who was 18 as well. And so we were like, you know, we should play some, we should play some Mario Kart. Like we should get Mario Kart up and running. I think that's a, that's a reasonable goal. And so I ended up like breaking this thing apart, finding out where the connections were and just soldering, um, you know, soldering cables.

**Chris Gammell:** He was the hero of the station.

**Dave Jones:** Yeah. Everyone else, everyone else was, you know, super happy that the band equipment was fixed, but me and me and like a couple other people were thrilled that we could play like golden eye at the South Pole. Um, so yeah. And, uh, but basically I'd spent all this time in the, in the comm shop fixing, uh, fixing the, some equipment that when the, the winner over who was supposed to be the senior communications technician was deemed not physically qualified. Cause you have to go through like a huge battery of physical exams. Um, I had to have my thyroid ultrasounded, which was just a really strange experience and my gallbladder ultrasounded and all this other stuff. Um, and, uh, then you have to go through a two hour psychological interview. Um, and also 600 written questions, which are just absolutely the most ridiculous things you've ever read. Things like I sometimes feel like there's a tight band around my head or, uh, that's another good one. Um, I enjoy fixing doorknobs. It's like, what? Like, what are you asking me? Immediately deemed crazy. Yeah. And this test has been like years ago deemed to be like just, you know, ridiculous, but for some reason the United States Antarctic program holds onto it. Um, but then you, you sit with a psychiatrist and they, and they grill you and they're like, why are you going to go crazy? Like, why would you want to do this? And she's like, I don't know. I like it. And so they ask you that for the winner overs, but not for the summer people. Like you can be as crazy as you want to and go down there for the summer. But, um, if you're going to winter over, you need to go through this interview. And so during this interview, the, the, the guy who was supposed to winter over, uh, as the communications tech was deemed not physically qualified. And so then they were like, holy crap, what are we going to do? Like, we need to have someone here. There wasn't an alternate. They normally, all the positions have like an alternate and a second alternate. So in the event of, uh, you know, uh, PQ not going through, they can bring in someone else.

**Chris Gammell:** Um, and so, uh, clarify here too, this is at the actual South pole station, right? Where you like can't get out for a couple months.

**Dave Jones:** Yeah, exactly. And so the last plane leaves in February and the first one doesn't come back until like end of October, early November. So for those nine months we're isolated from the outside world. Um, and so they looked at me and they were like, Hey, you can fix stuff. And I was like, I guess so. And they were like, you want to stay on? And I had been looking at wintering over as a like carpenter helper just because like I would have done anything to stay on for the winter. Um, and you know, get to experience this like really weird place because during the summer, since you're on the earth's axis, the sun is doing a perfect circle in the sky. It's just like circling around overhead.

**Chris Gammell:** Like, like a couple degrees off the horizon kind of thing.

**Dave Jones:** Uh, well it's up, uh, it's at the, at the earth's, uh, tilt since we're on the, on the axis. So it's like 20 to 26. Yeah. Something like that. It's kind of, it's weird. Cause all these things like, uh, yeah. Uh, but anyway, so, uh, they asked me if I wanted to stay on, I had some like, you know, I'd been crawling through ceiling tiles for my parents, uh, uh, you know, it heavy company for, for a number of years, like running all the networking cables and stuff like that. And, uh, so they were like, you think you could manage the copper infrastructure for this place? And I was like, sure. They're like, do you know what a patch panel is? I'm like, absolutely. They're like, can you, uh, you know, can you terminate a, you know, a RJ 45 connector? I'm like, probably.

**Chris Gammell:** Do you feel a band closing in around your head?

**Dave Jones:** Yeah, exactly. So I ended up doing, I ended up doing this, like this technical interview with three people at the South pole. Um, and then I did a, they flew me out to McMurdo, the coastal station. I interviewed with the person that was in charge of all the, uh, comms infrastructure for the continent. And I was like, you know, I think I can do this stuff. And there was a man wintering over in the, in the sat com position who was, had previously done the, the comms tech job. And so they like hiring me was definitely a risk, but they could hedge their bet because this other guy was there and like, he could be my guru for figuring out this stuff. And he was, he was amazing. And, uh, and that's, that's how I ended up wintering over at the South pole. And so ended up, uh, getting the, getting the contract to be the senior communications technician at the Edmondson Scott South pole station, which was at 18. Yep. Oh, I think it was 19. I just had my birthday. Yeah. Oh, okay. So, um, I was, and they don't let you winter over unless you're 19. So it was, uh, it was exciting. Yeah. Yeah. Bonus. I was like, really?

**Chris Gammell:** You had the N64 there. So, uh, yeah, there was an N64. You basically knew what you were doing, right?

**Dave Jones:** Yeah. Me and this other guy who went it over were the youngest people to have ever done it. And, uh, he beat me by, uh, 29 days and I, I still, I still resent him for it. That he was, uh, 29 days younger than me, but, uh, it was, yeah, it was fun, um, to. Okay.

**Chris Gammell:** So we're going to use this as a transition because, uh, first transition point is, uh, damn you crazy.

**Dave Jones:** Uh, it was fun. Yeah. It was great. I mean, you sit down, you sit down at a table and you're sitting across from like the PI of, you know, an incredible experiment and you could just ask him anything. You know, it's like, uh, John Kovac who was on the bicep team and all that, like, he's just sitting at the table there and like, you know, he's working on his laptop and I'd like show up after like having a beer or two and I'd be like, John, like, what are you working on? Like, I want to work on your project. And he'd be like, all right, hang on. What are you doing? Like, let's, let's talk about this. And you know, that's when, uh, I was a little inebriated and I remember telling him like, I want to be a graduate student working for you. And he said, uh, it'd be improper for him to offer me a graduate position before I have an undergraduate degree. And basically like shooed me away with that line. But yeah, I mean, it's just, it's super fun because yeah, you're just, uh, in the summer it's 250 people there. And then in the winter it's only, uh, it was 60 the first winter and then 47 my second.

**Chris Gammell:** So you stayed for two winters.

**Dave Jones:** Yeah. I've done 24 months on the ice, um, with a year gap in the middle. Yeah. It's pretty cool place though. I mean, the auroras, the sun sets for four months and it's just amazing. Yeah.

**Chris Gammell:** If you're into that sort of thing, I suppose. Right.

**Dave Jones:** Yeah. Yeah. I guess. I mean, I had $600,000 worth of government test equipment that I could do whatever I wanted with.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, you know, my, my manager was in Denver. So I had like, you know, if I wanted to spend, uh, you know, a week working on this thing or a week trying to sort out what that, like some phantom signal is over here, like that would, I was totally fine. Like I was there in the event that things went wrong. Yeah. So I would, I would be there to fix the equipment or I would be there to like talk over the HF radio to, you know, a coastal station, you know, but.

**Chris Gammell:** Well, speaking of HF radio, you sound like, uh, it sounds like we're breaking up right now. Um, it said really, it actually sounded like there was high, high frequency interference. Okay. So 24 months on the ice. That's pretty crazy.

**Dave Jones:** Yeah. It was, uh, um, I think the, the first time was an unbelievable adventure and the second time may have been a bit of a mistake. Oh yeah.

**Chris Gammell:** Started to get sick of it or what?

**Dave Jones:** Uh, well it was, um, it was this feeling of like, uh, so after Antarctica I went and I just like started taking classes and I was so excited because I thought that, um, you know, I was like, Oh my God, I'm finally going to be in a place where like everyone in my physics class wants to take physics. Like that's so exciting. Like I can't wait. I can't wait to be like, you know, surrounded by people who want to learn. This is undergrad, right? This is like undergrad physics. This is undergrad. Yeah. This is undergrad physics. Yeah.

**Chris Gammell:** And I, uh, so did you like turn to the kid next to you and you're like, so where did you spend your past 24 months? Was it like some other exotic location? They're like, uh, I'm, I'm, I'm a, I'm a drama major.

**Dave Jones:** Exactly. Yeah. So this was after this was between the trips and I was just like, Oh my God, I'm going to go back to school. I'm going to get my like undergrad. I'm going to go and work on some graduate project where I get to go to Antarctica. Like, that'll be amazing.

**Chris Gammell:** Everyone does this, right?

**Dave Jones:** Yeah. And I was so disillusioned and just heartbroken by this. And so like, I went for, I went for one semester and then I ended up getting a call from Antarctica. Um, well, basically a buddy of mine was like, I'm going to go winter over at the South pole. And I was like, you know what? I'm having a, like a hell of a time here. I'm not really enjoying this. Like I'll, I'll go with you. And so he's like, awesome. And so he signs up and I sign up and I get a job and he doesn't. Oh no. So, no. And I was like, well, whatever, you know, I wasn't going like just because he was going, I was going cause I want to go back. And, you know, and then I ended up coming down there and this, like the sun was setting, the last plane had left and you know, temperature's dropping to negative 100 Fahrenheit. And I'm kind of looking out, like looking around and I'm like, I don't know what I am doing. Like I've done this before.

**Chris Gammell:** I made a terrible mistake.

**Dave Jones:** Yeah. I've made a terrible mistake. It was, uh, yeah, it was this idea that like thus far, like I had always been like tripping over myself trying to keep going forward and keep doing new things and keep trying new things. And then I was back here, like locked in for another year, uh, which was, you know, not, not the best, not the best decision, but I did have like the whole lab again. And I had, you know, I had brought down the, like the dev kits I wanted to play with and like learn about. And so it was really cool to be able to be, you know, experimenting and learning in this like, you know, unbelievable lab setup.

**Chris Gammell:** Yeah. But, um, do you have, uh, internet access down there as well? Or is that pretty cut off to not, not really?

**Dave Jones:** We have, uh, so actually what's funny is we bounce off of the old command and control signal on a ghost weather satellite. So for like six hours a day, we have like a dial up internet connection. And then there's also the TDRS connection, uh, which before TDRS one deorbited a few, I guess it was in 2000, 2009. It was between my first and second year, the TDRS satellite deorbited. Oh. And, uh, so we ended up losing like one of the major links we had to the outside world. And so whenever there were shuttle launches and stuff like that, like we wouldn't have access to internet cause all the TDRS satellites were supporting the launch.

**Chris Gammell:** These are like geosynchronous type, type of satellites. Yeah. It's just bouncing. It's, uh, yeah.

**Dave Jones:** But the problem is there, there are no signal. There's no, um, there's not really any satellites launched, uh, in like a polar. Right.

**Chris Gammell:** Why would they stay over the polar when you could have a geosynchronous over LA or New York? Right.

**Dave Jones:** Yeah, exactly. And so the, yeah, the polar orbits are up around the equator and what we can hit are like, uh, satellites that have fallen out of orbit. And so like the old ghost weather satellite, like is in this like figure eight, like tumble and essentially it like, it comes over the horizon. Like I think our highest passes are six degrees above the horizon. And so we have like this, this giant dish that's like pointing straight out at the horizon and we get like a little bit of data and that goes away.

**Chris Gammell:** And you get like the intern who has to go and hold the dish up every day.

**Dave Jones:** Yeah, exactly. Yeah. Yeah. Like cranking on the dishes and change things, but we get, um, so we end up with like about six hours a day of internet connection, but it shifts sidereally. So it's like four minutes earlier every day. And so for a large portion of the winter, it's like in the middle of the night.

**Chris Gammell:** And is, is there a concept of night up there? That's the other thing I wonder about. I mean, like I basically put the South pole on par with like the moon, you know, like,

**Dave Jones:** yeah, it's, it's out there. We, um, we, I mean, the, once the sun is either up for 24 hours or it's, you know, down for 24 hours and there's like two months of sunset on each side of the four months of, uh, you know, sun up, sun down. And, uh, what's, uh, what's interesting is we go off of Greenwich meantime. So that's our time on the station is, um, you're at the bottom.

**Chris Gammell:** Everyone's it's every time zone, right?

**Dave Jones:** Yeah, exactly. Or, um, wait, no, we, uh, no, we go off New Zealand time. Yeah.

**Chris Gammell:** Oh, just cause you launch. Yeah.

**Dave Jones:** Uh, yeah. Yeah. Cause that's where all the aircraft go. And it doesn't make sense for us to like change in the middle of the winter. I guess one winter they changed to the same time as the Denver headquarters. And like there were riots with managers, like contacting people just like too much. And so it's nice to have that little buffer when people are going crazy in isolation to not have to deal with your manager for every week. Every waking minute you're there.

**Chris Gammell:** When I'm in full isolation, I don't want to talk to anyone.

**Dave Jones:** Yeah, exactly. Like I can't handle like the fact that you just got out of a meeting at 7am and need to give me action items and need to have a phone call. Like that does not work. That is crappy actually.

**Dave Jones:** Yeah. It's like, what are you doing this weekend? Oh, that sounds fun. Okay. I'm still going to be in Antarctica. So I don't want to hear about it.

**Chris Gammell:** So play against Oddjob again and N64 GoldenEye. Exactly.

**Dave Jones:** Yeah. It's super fun though. It's an amazing place. But it was just, you know, I was burned out on doing it once before. Yeah. So I had to, and you know, I kind of came to terms with that. And so I went back out of Antarctica for the second time and got back into the lab. And basically my, the professor I worked for was like, okay, we're going to have you like start machining again. And I just, I had like just been through some like chaos and I just unloaded on him. And like to this day, it still shocks me, but I just basically told him like, I'm going to be designing circuits. And if you don't want me to do that, then I'll find somewhere else where I can do it. But I am like never machining anything again. And he's just like, cause no one, no one talks back to him. You know, he's the PI of the lab. Like you don't, you don't do that. And I was just like, this is how it's going to be. Or I'm walking. And he just like flustered and told me like, well, I'll give you whatever project you think you can handle. I'll give you a PhD project if you'll just tell me when you'll be here. And cause I had been like sporadically coming in because I just hated machining. And I was so sick of staring at the CNC. Yeah.

**Chris Gammell:** Just going to lose its appeal after a while.

**Dave Jones:** Yeah. I was just like, no, I'm done with this. And so I ended up getting dropped into this lab with this guy, Mark Wilson, who is just an unbelievable engineer. And, uh, so I ended up working with him and he would like kind of give me like iterative projects. So I was working on like, you know, ultra fast timing stuff. And I was working on, you know, uh, this 350 watt RF exciter and things like that. And just like these bigger and bigger projects and all part of this, uh, this laser, this, um, giant, giant laser. It was, it's the size of like a 55 gallon drum on its side. And you send in a 50,000 volt, 20,000 amp pulse. And it steps this up to like 150,000, 150,000 volt pulse. And then discharges that through a capillary. And then the actual, um, fields end up wrapping back around this capillary. And then you get this effective pinch of the, of the plasma. And that spherical pinch of the plasma is called the Z pinch ends up generating a laser. And it's like this just totally crazy thing. But, um, I ended up working with the development of that and the commercialization of that product, which was just really fun.

**Chris Gammell:** Um, so commercialization, like, uh, we're all going to get killed by a death ray soon. Is that what I'm hearing?

**Dave Jones:** Well, it was like, uh, for, for labs that wanted a 46.9 nanometer laser. They could buy this.

**Chris Gammell:** Yeah, I know, I know the story you tell people. It's fun.

**Dave Jones:** Yeah, a giant laser. Giant laser. But it was really fun. Cause I got a, um, I, I built the, uh, so this giant laser is triggered with a thyrotron. Thyrotron. Which is something I had never heard of, but it's like essentially a deuterium filled valve. Okay. Like, you know, to use Dave's terminology, I guess, but the, um.

**Chris Gammell:** Deuterium being heavy, heavy hydrogen. Is that right?

**Dave Jones:** Yeah. Yeah. Or, or depending on the voltage, you could also get hydrogen, uh, hydrogen filled. And I think ours was, may have been hydrogen, but, um, basically this thing will fit, uh, will, uh, switch 50,000 volts, um, and like sub nano. Or in like maybe five nano, something like five nano is the commutation time for this thing. And, but to trigger it, you need to use another thyrotron to get those kinds of edges on it. So I built the thyrotron triggering thyrotron circuit, which was super fun.

**Chris Gammell:** I hear you say your thyrotrons with thyrotrons.

**Dave Jones:** It was, it was so much fun. Like winding giant inductors on the, on the lathe and stuff like that. It was, yeah, it was, it was really cool. Um, and you know, I, I barely knew what I was doing, but I had, um, you know, this amazing mentor who was, who was, uh, guiding me through it. Yeah. It was a crazy Russian thyrotron too. So every time we had an issue with it or anytime we had like a question about it, we're like, oh, well, you know, the data sheet says that, you know, it can only, you know, at 20,000 amps or whatever, it can only operate, you know, at this duty cycle. And what if we wanted to operate it like at a slightly lower voltage, but a higher duty cycle, you know, something like that. And the, you know, we get basically a response from the thyrotron vendor that's like, oh, it shouldn't be a problem.

**Chris Gammell:** And just try it.

**Dave Jones:** Just try it. Then we'd be like, well, the, the data sheet says it's not going, like it shouldn't do this and they'd be like, oh, sorry, sorry. And they'd send us a new data sheet with all the same information, except for that field changed to be whatever we had requested.

**Chris Gammell:** It's like crossbound and red ink.

**Dave Jones:** Yeah, exactly. We're like, what the hell?

**Chris Gammell:** It says just trust us in Russian.

**Dave Jones:** It's like, don't worry about it. It's fine. It's fine. Don't worry about it. You know? And it's, I don't know. It was really fun, but, um, yeah. And so I was, I was working at that. I was, I was trying to take classes, but it just, you know, I'd rather be in the lab building something. And so, uh, then, uh, I guess a year and a half ago, uh, a friend of mine from the South Pole was coming through Fort Collins and, uh, he said that, you know, he is, he was just, he was on his way going, he was on his way to Antarctica and he had just left this startup that he thought I would be, uh, I could fit in. And it was a bunch of like hardware hackers and, you know, uh, cool people building these tiny satellites. And I was like, you know, I don't know. I have a good thing going here at the lab. It's interesting projects. It's fun. But, you know, the more I start to think about it, the more it kind of irked me that I was working on the commercialization of this product, which was technically a startup, but it wasn't really a startup. And I had no equity in the company and I was being paid like pennies for what I was doing. And finally I was just like, you know what? I told my advisor, I was like, I'm out. And he was really, really upset about it. But, um, and I ended up coming out to San Francisco and, uh, I flew out to interview with these guys and they hired me to be the, I think the third, third electrical engineer. Well, I can't, I can't say that. I'm not an electrical engineer. I guess the, uh, I triple E will, will sue me if I say I'm an electrical engineer.

**Chris Gammell:** You know, I feel like, you know, I, I got a bachelor's degree. I feel like they would sue me if I said it though, too.

**Dave Jones:** You know, they're, they're, they're like the only, uh, no, it's the professional engineering.

**Chris Gammell:** They're the ones who do it. The, uh, the PE board.

**Dave Jones:** Oh, they're the ones that do the suing. Oh, okay. All right. Yeah. Either way. I'm a, I'm an electronics designer. That's right. I guess.

**Chris Gammell:** Hardware hacker.

**Dave Jones:** Hardware hacker. Yeah. I don't know.

**Chris Gammell:** Like we have like, we've had like Jerry on the show and like, and like, I mean like Jim Williams, right. He never finished his degree or anything like that. You know, he sounds like the same kind of story, you know, hung out in the lab, just wanted to make stuff. It's like, I don't care about a piece of paper. It's like, no, you're an engineer. Sorry, buddy. It's just, uh, you don't have a choice. Yeah. Yeah.

**Dave Jones:** Exactly. Yeah. So I just can't, I can't sell myself as an engineer, but you can't, you can't say

**Chris Gammell:** it officially in any documentation, but yeah.

**Dave Jones:** So, uh, so yeah, I started, um, came out here. Started building, um, tiny, tiny satellites for this little startup called, uh, Planet Labs. Yeah.

**Chris Gammell:** So Planet Labs and formerly called something silly.

**Dave Jones:** Uh, Cosmogia. Yeah. But that was, that was when they were in stealth mode. So, um, yeah, they actually, they, they, they launched two. Cause even when, uh, when my friend Yuki was telling me about the project, um, he, uh, he was like, oh, well, you know, they're working on space stuff. And this is like a good friend of mine who was trying to get me to go and work at this company. And he still is like, he's not telling me anything about it. And they were just so serious about stealth that, you know, they had no, no outward, uh, announcements of who they were. The, the email address.

**Chris Gammell:** Because most of the time when you hear stealth, you're like, okay, people aren't really doing anything. Right. Like people like, oh, my company's in stealth mode. It's like, oh, you're trying to figure out what to do. Yeah. I'm in stealth too. Wink, wink, nod, nod, you know? Exactly.

**Dave Jones:** Yeah. And these guys, uh, they, you know, they were, they were serious. They, um, I mean, they raised, uh, the Siri, they raised their, um, angel funding and a round and B round or no B round was right at the announcement of, uh, of their existence, but they actually launched.

**Chris Gammell:** No longer being Cosmogia.

**Dave Jones:** Yeah. They actually launched two satellites, uh, before being out of stealth mode. Wow. So they were, and, uh, company was, was two, two years old. I think when I came on board and they had just launched, uh, dove one and dove two, which are, our, um, which were the, our tech demo satellites we call doves. Hmm. So, uh, we were, um, so I came on board during the buildup of, uh, dove three and four, which were, um, kind of technology, uh, proof of concepts that we could actually, um, well, I guess I should say what, what planet labs is doing. Yeah. That'd be great. We're no longer in self load. Yeah. Uh, so our, our mission one, our, our goal of the company is to, uh, image the whole land area of the earth every day at three to five meter resolution. So we want to essentially create a global mosaic that is updated on, um, on a daily timeline. And the idea for that is that, uh, we kind of, we're looking at this, uh, the earth as like spaceship earth. And the idea that, um, if we're trying to do any kind of meaningful control loop on this, this spaceship we're on, we need to be, um, you know, our, our inputs need to be updated at a rate that's greater than what we're changing things at.

**Chris Gammell:** Yeah. And so, um, and so, and so you said three to five meter, uh, could you possibly speak in terms of, uh, Google maps for dumb, dumbs like me?

**Dave Jones:** Oh, sure. Yeah. Um, so three to five meter resolution is, uh, we can, we can see, basically we can count every tree on the planet, but we can't see cars on the road.

**Chris Gammell:** Okay.

**Dave Jones:** It's kind of a, an idea like for that. So, um, it lets us kind of get our away from the security and the, or not security, but the, um, the privacy concerns that people have with things like Google earth and all that. And, um, lets us still be able to do useful things like count every tree on the planet, which was one of our initial goals for, uh, dove one was to be able to like resolve trees,

**Chris Gammell:** which was, uh, okay. Yeah. That's kind of cool. Which is pretty tough when you think about it. Like people don't, I don't know. I'm sure a lot of our listeners understand, but like that kind of level of zoom is, especially when you need stability over time and everything, it's like, it's pretty intense.

**Dave Jones:** Yeah. There. And especially, uh, since we're operating in a, uh, cube set form factor. So we're, uh, we're a three U cube set. Um, so we're, uh, 10 centimeters by 10 centimeters by 30 centimeters or about, uh, four inches by, uh, four by a foot long. So yeah, we, um, sorry. Uh, yeah. So we, um, we operate these cube sets in, in constellations. And so the idea is that, um, each satellite, uh, will be launched into, into a ring and sun singular orbit. And so we'll have, uh, depending on the, the orbit, uh, a number of satellites. And what will happen was as these satellites are orbiting, the earth is rotating underneath them and we end up getting a line scanner for the planet. And so we'll be able to, um, to capture this. And so instead of targeted imagery, which is how, um, basically all, um, imaging satellites operate right now, we'll actually just be constantly capturing and then downloading that data.

**Chris Gammell:** So how much can a, a single, I mean, I guess I would think this would start to quickly run into a, a memory issue and a bandwidth issue. Um, like the specs on a single satellite, how much can it capture? And, and like, so, so it's like a video stream almost like a video stream where it's like frames per second type of thing.

**Dave Jones:** Yeah. Yeah. And so, um, basically the satellites are operating in about, uh, right now they're operating about one frame per second based on the, their position in the orbit. So they're constantly capturing as they go along. And then, um, one of the major things that we were able to develop here at Planet was, um, this really robust radio system. And so we actually have an X-band, uh, satellite, uh, downlink on this, you know, this little tiny satellite and we have ground stations all over the world. And so the idea is that you capture, um, you capture during the, during the, during the sunlight part of the orbit. And then you can downlink on the, on the dark side.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Cause you don't need to be, um, imaging. And, uh, we're able to get like incredibly high throughput on our, our little satellites, um, compared to anything that's ever been done on a QEMSAT form factor. But, um, you know, we're not, we're not hitting the TDRS, uh, the LADIS laser comm 600, uh, megabit per second. But, uh, we're, you know, we, we do have a fairly respectable link to the ground. Um, that being said, uh, we are still downlink limited in our satellite, but we're definitely making, uh, modifications to the bus to see if we can, uh, up our throughput. So one of the cool things about these dubs is that we've actually iterated over them, uh, 12 times since the company was founded, uh, uh, three, four years ago now. And so about every three months we go through a major design cycle and we look at almost everything on the bus and say, okay, what can we improve? What can we change? What can we make faster? And, uh, so I was brought on board to do image compression and hardware. And so I was working on, um, uh, FPGA algorithms to essentially go in between our camera and our, our CPU and allow us to just do compression on the fly. So we don't have to worry about wasting CPU resources or downloading, um, these, you know, incredibly high resolution photos.

**Chris Gammell:** Yeah. So can you give us an idea? So like the raw capture off the, off the image sensor, like what kind of, uh, megapixel that is?

**Dave Jones:** Uh, I don't know if I can speak to, to that exactly.

**Chris Gammell:** Ah, secretive stuff. Okay. Yeah.

**Dave Jones:** Well, it's, it's kind of, it's kind of that weird, that weird metal section between, um, uh, we're technically governed by, um, the ITAR, the glorious ITAR international trafficking of arms regulations because satellites are like any, any satellite just falls into the same bin as like missiles and guidance systems and all this other stuff.

**Chris Gammell:** And if you can count a tree, you can probably count them a silo. So that's, that's another good reason.

**Dave Jones:** Well, so one of the cool things though, is that, um, the regulation is actually trying to like catch up where, you know, uh, we're saying that this is, this is absurd, you know, like we understand that this needs to be in place for, for things like, you know, global eye and all the other satellites that have, you know, quarter meter resolution and things like that, or like 25 centimeter resolution, you know, be able to read your ID from space. You know, that's, that it's understandable that like these need certain restrictions, but, um, for our satellites, we're, you know, we don't really fall into that, that bin of like international, uh, you know, espionage or anything like that. So we, uh, we're, we're actually changing in a few months here. Um, they're changing the ITAR restrictions for satellites of our resolution to actually fall under department of commerce, kind of NOAA area instead of department of state and DOD. So yeah, it's nice to see that, that kind of, you know, that there is some kind of feedback loop in Washington.

**Chris Gammell:** Yeah. Uh, yeah. Well, we'll leave those comments till later. All I'm, all I'm imagining is like, like James Bond calling and being like, I, I need a spy satellite image and then calling back and be like, uh, it's the blobby thing near the blobby thing. We can't get any more resolution.

**Dave Jones:** Exactly. Yeah. So like, since we're not targeted imagery either, we're not like, you know, we don't have that, um, we, we don't, I mean, we, we could do targeted imagery, but it's not, you know, it doesn't follow with our, our goals as a company and we still have to fall under things like shutter control. So technically the, um, the U S government could come and say like, turn off your cameras and we'd be like, okay, like, yeah, that sounds, that sounds fine. But, um, you know, this is, this is on every single imaging satellite and it has, uh, in the history of, um, you know, the existence of imaging satellites, this has been, um, you know, exercised by the government. Oh yeah. Turn off your satellite. Yeah. So, especially at our resolution then.

**Chris Gammell:** This is interesting. Cause I mean, you mentioned other satellites and it's like, then you start to think about it and it's like, well, how many are actually up there? And you mentioned there's like 90 some of just your satellites now, like that are up there. Yeah.

**Dave Jones:** So we've launched, uh, we're actually currently operating, um, the largest constellation of earth observing satellites.

**Chris Gammell:** Wow.

**Dave Jones:** Um, yeah. Which is kind of a funny thing. Uh, when, when we got that title, we also had as many satellites in orbit as employees at the company. So that was right around like 30, 32, something like that. We had as many satellites in orbit as employees, which was kind of cool. Um, and we've kind of, we've trended along that line. Um, we have about 70 people here and we've shipped, uh, 90, 90, uh, seven satellites.

**Chris Gammell:** So like every time you hire a new person, you're like, all right, we get to send up another one.

**Dave Jones:** Send up another bird. Yeah. That's right. Uh, well, we send them up, uh, they, they go up, uh, we call our, our constellations flocks. Um, so we have doves and flocks. Yeah. Yes. Yes. That's cute. Yes. So, um, well, you know, it's, it's this idea that, um, like all these imaging satellites always have like these horrible names, like, you know, Hawkeye or like, you know, you know, all these birds of prey, you know, Eagle Talon. And you're like, okay, well, we're just, yeah, exactly. We're like, well, we're just launching doves. You know, we're, we're having fun. We paint our ground stations. We're like the, you know, I think we were the only people that have ever painted a radome. Like if you look around, like all these radomes, they're just like these giant white golf balls on the horizon. And so we've covered ours with our artists and residents has gone out and like spray painted all over them. And so it's kind of awesome. It's super cool. Like it's something so simple, but, um, we also have artwork all over our satellites too. That's great. Um, yeah, our artists and residents, uh, did these, uh, these three pieces. He actually ended up becoming our art director and, uh, he, then we, um, basically took those images into Photoshop, sliced them into five pieces and then, uh, laser etched those into non-outcasting panels and put those on the side of the satellite. And so every one of our satellites is like covered with all sorts of cool art in space.

**Chris Gammell:** So that's awesome. Are there pictures that people can see online?

**Dave Jones:** Are there, uh, yeah, on a planet.com there's a, it has a little bit about our, our, um, our spacecraft.

**Chris Gammell:** Cool.

**Dave Jones:** Yeah. I think that's a slightly, slightly older. Um, yeah, I think that's the flock flock one. Satellite. So we've been, uh, we have to update that, but we also have, um, some of our first light imagery in the, um, in the gallery page there. So there's all the, the images coming down from our satellite, which gives kind of a sense of the resolution in our, uh, our ground area. Okay.

**Chris Gammell:** And so who does this stuff go to then? Is it like going to like think tanks and stuff like that or?

**Dave Jones:** Uh, yeah, there's, uh, there's lots of, um, and applications for this. There's everything from, uh, the precision agriculture market is actually kind of big. Um, also the, the, the mapping sector and, uh, places like that, uh, just imaging over China alone. Like the change detection is insane. Like every time you take a picture over China, even if we took the previous picture, like everything is different. Like they are just like, everything is under construction in that country. Yeah. Yeah. It's amazing. Like rivers are changing path.

**Chris Gammell:** Like it's, that's the garbage.

**Dave Jones:** It's nuts. Yeah, exactly. Yeah. And, uh, it's, it's really amazing. And so, uh, if you do like image in the Northwest, you'll see like, uh, areas where logging is occurring and stuff like that. And so what we're trying to do is just basically have this, um, the major value in our data is actually in the temporal domain. And so you can actually look back through and see like how are things changing time lapse

**Chris Gammell:** almost basically.

**Dave Jones:** Yeah, exactly. So you get a time lapse of like a certain area because, uh, once we actually, um, hit our target cadence of daily imagery, then we'll be able to actually have this like unbelievable data set. And so that's of applications, everything from research to, uh, you know, planning and urban development and looking at things.

**Chris Gammell:** Agriculture makes a lot of sense to me. I, I mostly, I was wondering like, it's like, Oh, how are these guys making money? Especially cause I'm sure satellites aren't cheap, even small satellites. And I would think agriculture stuff up there. Yeah, exactly. And I'm just, uh, agriculture is, is huge, right? I mean, that's just like everything like factory farm, like there's just so much data going into that these days that that makes, that could make a really strong case for that. So that's really interesting.

**Dave Jones:** And also we have, um, we have a position at planet of, uh, providing universal access to this data. So absolutely anyone who, who wants the data can get the data. And the idea of, um, of like selling base maps and things like that to countries that, uh, you know, couldn't afford targeted imagery because they can't afford the, you know, it's not realistic to yearly send over like a, you know, this a hundred billion dollar satellite to actually point it at their, their area and like get a base map, you know? Yeah. So what we'll have is the ability to where in, you know, disaster response and things like that, where it would take a week or two to get this imagery or to get the satellite to be overhead, to image this area. Like we have the ability to just capture it because we will already have satellites there that are already recording this data anyway. So you can see that the day to day changed instead of saying like, oh my gosh, all of these buildings fell down, which ones are they? And then if you have the base map of the day before, you can know, well, these ones were actually torn down a month ago. These ones, you know, haven't been there in 10 years. And right.

**Chris Gammell:** Right. So like earthquakes, mudslides, like stuff like that, that's really valuable then. Yeah.

**Dave Jones:** Yeah. To have that, that up to date imagery. And so with, um, yeah, so that's, that's kind of what we're working on is.

**Chris Gammell:** So how, how do you, I've always wondered about this too. Like, so how do satellites, I always think of like, like retro rockets and all the other, like the little, the little spritzer thingies they have on them that like position themselves. Is that like part of a satellite these days or is it something else or is it just like throw it up there, you get what you get?

**Dave Jones:** Yeah. So we have, we have three methods of attitude determination, um, control, sorry, attitude. It's the ADCS system, but the, the control side of it. Um, so we launch all of our satellites and they end up in this little blob, this like hunk of, you know, 11 or 28, depending on what, uh, orbit we're in and what launch we're in. And so we have these 11 satellites that are just kind of whipping around the planet at, you know, seven kilometers a second in this little ball. And we want to spread them out because it's not useful for us to get like all this, you know, data of one spot. Um, you know, having a single point line scanner isn't, isn't the point of these. So, uh, we deploy our solar panels and then we actually rotate the spacecraft into, uh, the velocity vector. And so we can turn our, turn our satellite. And instead of having this, this three, you, or this, uh, four centimeter by 10 or four centimeter, ah, four inch by one foot, uh, you know, right to the atmosphere. Cause even in the orbits we're in, there's still a bit of atmosphere. Um, we can, uh, actually change the amount of drag on the spacecraft. So if we rotate our satellite, we have, um, you know, a 19 unit cross-sectional area versus when we're flying normally, we'll have a three unit cross-sectional area. If we rotate, so the telescope is in the velocity vector, then we have a one U cross-sectional area. And so by varying the, uh, the position of the satellite, uh, we can actually separate them in space by changing.

**Chris Gammell:** So how, wait, how do you rotate them though? Like that's still, is that just from inertial, like from changing the motors?

**Dave Jones:** Yeah. Yeah. So there's, there's two methods we use. Um, uh, one is we have, uh, a stack of four reaction wheels, which are nominally spinning at 4,000 RPM. And by accelerating them, we can put a moment on the spacecraft in one direction or by decelerating them slightly. We can put a moment in the other direction. Um, and then, uh, if our reaction wheels become saturated, then we have three, uh, orthogonal coils and we can energize those coils at different levels to actually push off of the earth's magnetic field. Oh, that's awesome. Yeah. So we have a model on the satellite that knows what the earth's field is at that point in space. And then we can energize the spacecraft in such a way that we can kind of push against it.

**Chris Gammell:** Okay. And then for the big movements, that's where you start getting into the drag stuff with the, uh, yeah.

**Dave Jones:** For separate, for phasing the satellites in orbit. Yeah. We use the drag technique, differential drag and for, um, for just movement. So if we were like pointing at a ground station or if we're, you know, making sure we're pointing down over where we're imaging, we use, uh, uh, the reaction wheels and the magnetometers or I'm sorry, magnetorkers.

**Chris Gammell:** That is so cool. So how do you tell absolute position then too? Is it just from imaging or is it from, uh, so we have a base?

**Dave Jones:** Yeah, we have a couple of different systems. Um, you know, the, the number one thing we use is, uh, is a common filter, which basically, yeah.

**Chris Gammell:** I know those, those are crazy.

**Dave Jones:** So we're feeding in basically all the sensor data. So we have, um, you know, uh, MEMS gyroscopes, we have MEMS, uh, we have magnetometers, um, things like that all over the spacecraft separate in space and like, uh, separate in space along the spacecraft. Um, then we also have photodiodes all around the exterior of the spacecraft so we can, based on their intensity, we can see where we are, like kind of course reference to the sun. Um, and then we also have a, uh, star camera on board, which we can then image stars and use that to feed back into our, uh, into our common filter, which will then give us a, um, you know, an estimation of our position. Uh, but the, what we also do is...

**Chris Gammell:** People don't know, uh, common filters are active. They're like, uh, modulating filters, right? Based on inputs and estimation, all that other crap, right? Where you change the, the, uh, coefficients and craziness.

**Dave Jones:** Yeah. And so, and what we get to validate that too, is we get this picture out of the front of the telescope. And so the common filter is like, you're pointing here and we're like, okay, well that was 20 kilometers of where you thought it would be. So we can back that in and be like, where's our error coming from? And so we get this like, you know, this high resolution, uh, sensor. Yeah. It's only, it's, there's a bit of a time delay between, um, rectification and all that. But, um, yeah, one of the, one of the major things that we do is super cool. Um, is that, you know, we're operating this huge fleet of satellites, but we're still a small group of people. Um, yeah. And so what that's, uh, let us, or forced us to do as much as, uh, you know, what we wanted to do is, uh, we have like three or four people in mission control. And, uh, as a frame of, uh, NASA for, um, you know, uh, a large satellite will have 200 people in mission control and, you know, working shifts. And we have, we have three or four people on, on day shift. Like there's, there's no one.

**Chris Gammell:** Three or four people in 20 cases of Red Bull.

**Dave Jones:** Exactly. No, it's, um, it's, uh, it's crazy because we have, uh, the satellites are all scheduled so they know what they should be doing. Um, and that schedule is autonomously determined by this unbelievable, um, optimizer code written by just one of our brilliant, brilliant developers we have here. And he's just like, Oh, that sounds like a fun puzzle. Like I'm going to solve this. And we're like, what? Cause before we were like manually saying like, okay, we need these passes on these satellites. We need these passes on those satellites. Like, okay, this satellite's in a low power state. We should do something about that. Like tune down it's like it's acquisition windows and all this. And he's just like, Oh, that sounds like a puzzle that I could solve. And it's like, you know, writes this unbelievably huge program to like handle all of this. And it's just amazing. Like we watched, uh, like our, our, the number of images coming down from the satellites just like creep up and up and up as this optimizer was just like solving for variables we didn't know existed, you know? And, uh, yeah, it was really cool. But, um, so anyway, the, uh, all the scheduling is, um, autonomous and all the ground stations are autonomous. So they are on there. We don't have people at these ground stations. They're, they're running scripts, you know, and they're pointing at the satellites autonomously. The satellites know when they're taking passes and they'll point at the ground stations. Um, we do our own ranging. So we have, uh, sets or we have ground stations that are just for orbit determination. Um, and, uh, so all of this is done without a human in the loop. And so we end up with, um, you know, our server is just getting images on it that then get pushed into, um, we have some, some barefoot PhDs that work on, uh, how like autonomous geo rectification code. So they take the imagery and then based on, um, known ground control points, they then, um, kind of move and deform and like mess with these, this giant array of pixels until they're, they're ground truth.

**Chris Gammell:** So is this like if there's, if there's like angles or, uh, parallax effect, that kind of thing?

**Dave Jones:** Or if the, um, you know, if there's terrain or if the, the satellite wasn't pointing exactly where we thought it was, it can do this search within the area and then find it and then propagate that through this, uh, through the strip of images, knowing like a known control point, then it can easily find the next ones in the line and move them around until it's, um, satisfied the ground control points. And, and what's, what's amazing about this with the crazy story is like for the first, uh, we sent up 28, uh, satellites for flock one. And when the first satellite deployed, we were all super excited. We're all sitting around. It's being deployed from the international space station. There's a live feed. We're so excited. The satellites pop out of the international space station through this like satellite cannon and we go crazy and we're all super excited. And everyone runs over to the computer to wait for the first pass, which is in like 45 minutes. And I'm going to see if we can make contact and see if the satellites are okay. And by, by the end of this, there was, you know, 26 satellites had been deployed. Maybe like no one was quite sure how many were out there. Like the mission control, like we could open mission control and count them, but like, that sounded like a lot of work. So it, uh, so by the time like the last two were deployed from the space station, um, there were no engineers awake, like every popped out at like 3 AM and we woke up the next morning. Everyone kind of like logs in on the, on their laptop at home. And we see that the satellites have already made first contact, have already started going through their commissioning process or like de-tumbled or like in stable orbits and are like awaiting your command. And it's just like, it's a really, it's a really good feeling that, you know, we designed them to do that, but then they're actually doing that. So yeah. Wow. And, uh, the crazy part was for our last launch, uh, which was also from the space station, uh, for the flock one B satellites, uh, there was a problem with the nano racks deployer. And so they send the deploy signal and nothing happened and they send the deploy signal and nothing happened. And so our satellites are stuck in this, um, satellite deployer. And so, uh, and we're, we're honestly not really thinking about this too much. We're just, we're already working on like three or four builds in the future. So we will like, we'll learn things from the flock one B, but we're already designing the, you know, the flock for like we're, we're way out there on the design. So, um, what happens is, uh, we're all sitting around in the, in the lunchroom, we're kind of hanging out and all of a sudden, uh, have you heard of the yo app? Yeah.

**Chris Gammell:** Yeah. It's just that stupid app where you just say yo to people. Yeah.

**Dave Jones:** It just says yo. Right. Um, so one of our engineers found out that you can actually, uh, you can get a developer account on yo. And there's like a really simple, there's a really simple scripting language, right? To like, yeah. And so what we did was we worked into our mission control, essentially like this, this flag that would send out and on first contact with the satellite, the satellite would say yo. And so you get a yo on your phone every time there was a first contact. And so we're sitting around in the lunchroom and just kind of hanging out and, um, you know, someone's phone buzzes. And then all of a sudden, like everyone's phone's buzzing and we looked down and we're like, we just got first contact from a satellite. And we looked at the mission control guys and we're like, you know, we're deploying a satellite right now. And they're like, we're not. And then it's like another buzz goes around the table and it's like, uh, so we just had another first contact. And so we all kind of, you know, walk over to our computers to see what's going on. And, uh, like the, these two satellites that are supposed to still be on the international space station have made first contact and are like going through their commissioning steps. And we get this frantic email from NASA and nano racks. That's like, heads up. Like your satellites just deployed, like be ready to make contact. And we're like, uh, yeah, we, we know. Cool. It's, it's, it's cool. Like, yeah, we, we're already, we're already commissioning them. Like they're already working away. So it's cool to, to see that stuff work, you know, but that's awesome.

**Chris Gammell:** So they, they all go up with the IS or so they go up on like the dragon capsule now or how do they get there?

**Dave Jones:** Yeah. So we, we've gone up through, um, we go through a lot of service providers. So we just, we want to get so much to space. Um, we've launched through, uh, through us, through Russian rockets. Um, we have gone up on, um, uh, the, what's the name of it? Oh, it's an old, uh, Russian ICBM. Um, the Dnepa rocket. Yeah. Which is just crazy to see. Uh, there's check out the launch video of the Dnepa. Cause it's, it, it's launched out of its silo by an explosive charge. And then it like, once it's out of the silo, which is underground, then the rocket engine lights and it takes off. And, um, so we've gone up on, we've gone up on those into a sun synchronous orbit, which is our ideal orbit, um, which is, uh, an orbit that processes at the same rate as the earth rotates. And so what you ended up getting is, um, uh, every time you're over the same spot on earth. So, you know, however many hundreds and hundreds of orbits later, when you're over the exact same spot, it's the same time on earth that you, it was when you first right. And so all the shadows are constantly the same, which is really handy for, for doing change detection and stuff like that. So, um, so we're in like a 10 30, 10 30 orbit, which is kind of a, um, kind of a funny thing to think about. So at like 10 30, there's a chance of a dove overhead. But, um, then we also launched through the ISS just because there's so much, uh, through the commercial resupply program, there's so many launches going to the international space station that they need to put something on it. And so we, uh, we've bought, um, space on those rockets and then the astronauts essentially take us out of these, these padded bags in our deployers already mount them to, uh, um, basically a big plate inside the space station that slides out through an airlock. And then the robotic arm grabs it, points it away from the station and fires us out two at a time, or that's how it's supposed to work. There were some issues with the last one, not actually going when they asked it to, but

**Chris Gammell:** so they like show up in like lunch, lunch satchels, basically. And like, they're like, you guys delivering your satellites for the day.

**Dave Jones:** Yeah. They're in, uh, they're, they're wrapped in bubble wrap, put in duffel bags and then put inside the capsule. And so we have to go through, uh, launch qualifications for NASA and we're supposed to go through qualifications like in the method that they will be attached to the spacecraft in. And so we take these satellites down to, uh, we take them down to the, the test center, which is like, uh, so we're in downtown San Francisco and the testing center is in San Jose. And so we have to drive the satellites from San Francisco to San Jose. And, you know, this drive is, is pretty rough on the, on the freeway. So the satellites get shaken up a little bit and then they're wrapped in, in bubble wrap and then put in duffel bags and then put on a, on a shaker table. And then they're shaken to the, to the launch loads at, which is so much less, uh, less of a shock than actually riding in the car.

**Chris Gammell:** The one on one is way worse. Oh yeah.

**Dave Jones:** It's awful. Yeah. It's, yeah, it's crazy. It's also a really stressful drive when you think like, okay, I have, you know, however many satellites in the back of my car, like I have to be careful.

**Chris Gammell:** That's like, that's like the same thing where it's like safer to get on the airplane than it is to drive to the airport kind of thing. Right.

**Dave Jones:** Yeah, exactly. It's like, I don't know what you're looking for in this, but I think it's going to be okay.

**Chris Gammell:** That's bonkers. So, uh, so you guys are continually revving boards. Um, what is, what is that? I realized we've now hit the two hour mark roughly. Uh, so I apologize. I have so many more questions though. Are you still okay at time? I don't know.

**Dave Jones:** Oh yeah, I'm fine. I'm, I'm about to go on vacation. Yeah. I'm golden.

**Chris Gammell:** Sweet.

**Dave Jones:** Yeah.

**Chris Gammell:** Uh, yeah. So, uh, what is, what is the, the PCB? Like, I mean, like I always wonder about that stuff too, is do these have to be like rad hard parts or what are you guys designing with?

**Dave Jones:** Yeah. So we take a, what we call a agile aerospace. We take a totally new design, a totally new view of all of the aerospace sector. So, uh, basically, um, our company started out of a project you may have heard about of NASA called a phone set. And basically it was this idea that, um, yeah, one of our, one of our mentors here at the company, he used to sit in NASA meetings and, you know, after this huge design interview of a hundred billion dollar satellite, he'd take out a cell phone and be like, this does everything you want your satellite's computer to do.

**Chris Gammell:** It costs $300.

**Dave Jones:** It sits in my pocket. It is like, why can't this work? Why don't you just plug this in? And they're like, Oh, it'll never work in space. You know, all this other stuff. And, you know, it's understandable when you're looking at it.

**Chris Gammell:** Well, if you send enough of them.

**Dave Jones:** Yeah. That's the idea. I mean, if, if you're spending a hundred billion dollars on a satellite, you're going to have a hundred billion dollar satellite. You're going to have, you know, redundant processors. You're going to have, uh, what they call, uh, you know, multi, multi string between all your devices. So, you know, if you drill a hole through your satellite, like it'll keep working.

**Chris Gammell:** Yeah. Right, right, right. So everything's like a concurrent and, and you did like error checking and all that crap.

**Dave Jones:** Yeah, exactly. And so, uh, what basically happened at Ames was there was this group called phone set that stuck a, you know, a cell phone into a cube set and put a radio on it and threw it into space, like just like that. And, you know, with a little bit of extra battery and they were like, this will work. Like, there's no reason this won't work. And so then they actually, uh, spun out, went to the garage, you know, the whole San Francisco startup thing and, um, you know, decided to start this company building the same thing. And, but just saying like, all right, throw out all the aerospace paradigms. What can we come up with? And they developed a satellite that, um, it was dove one and dove one basically is all commercial off the shelf components. There's no aerospace parts in there at all. Um, there's one thing you have to watch out for is, you know, outgassing. So you kind of look for parts that, um, for our batteries, for example, they have PVC jackets. So we have to cut out the PVC jackets.

**Chris Gammell:** Um, PVC is always the chlorine out gases, right?

**Dave Jones:** Yeah. Every, yeah. Anything that can outgas can either, you know, fog up your detector or can, you know, damage some other component on the spacecraft. So, um, what we, what we've done is just saying like, you know, the commercial technology is at such a position that there's no reason we can't leverage that to, you know, put the most advanced processor ever flown into space just because, you know, we're, we're willing to take a part that is, you know, you know, like a cyclone five or something, for example, that is, you know, still, still the errata is, you know, being discovered. But the idea is, is that we can take that and throw it into space and we'll have the most advanced processor that's ever flown just because we're not on this 10 year lag of, well, it's not proven. And we're like, test it in space. You know, we have redundancy in our network of satellites. So in the event that we lose a satellite or two, that's okay. That's actually part of our design philosophy. If we don't lose a satellite, you know, um, of our flock of our flock one satellites, uh, our CTO took us aside at the end and he said, you know, a hundred percent of the satellites work great. And he's like, I didn't appreciate that.

**Chris Gammell:** It was this idea of, yeah, you're not, you're not cutting edge enough if you're not breaking stuff.

**Dave Jones:** Yeah. If we didn't have any failures in space, we weren't pushing the envelope. And so for flock one D we have this, you know, unbelievable, you know, changes that are, you know, our operations team is going to hate us, but like every satellite has like all these other things that other satellites didn't have. Like we went, um, so one of the projects that I owned recently was a maximum PowerPoint tracker for the solar cells. Cause before we were just trying to keep our system simple and having the panels go straight into the batteries, but then you can't really do charge control. You can't do all any of this other stuff, but you know, the, the reason we had done that was that was a single point of failure. And so I went on to the, the maximum PowerPoint tracker project and we went from concept to PCB to integrate it into a satellite and integrate it into two satellites. You always want to put something into two satellites just in case something goes wrong and you can't contact one of them. So we, we shipped these two boards that were a concept three weeks before were integrated into a satellite and going to space in like three weeks, which is, you know, the amount of time it takes NASA to decide that they should have a meeting to consider whether or not to integrate something into like a satellite 10 years from now. And so we're, we're definitely, we're proud of that, that agile aerospace side of things. So, yeah. And so far we've, we've made first contact with everyone. So.

**Chris Gammell:** And so have you had any spectacular failures yet? I mean, like where are they just go out of orbit or, I mean, do you have that kind of tracking capability?

**Dave Jones:** Yeah, absolutely. So we, we have, you know, it's a, it's a joke around here. How many, how many temperature sensors we have on the satellite? The satellite is, you know, what, 300 cubic centimeters. Um, so inside there we have, uh, or no, 3000 cubic centimeters. Sorry. Um, inside there we have like something like 60 temperature sensors, you know, including the devices that have their own on there. Just because we're like, wonder what the temperature is over here. Like we should know the temperature on all the panels. We should know the temperature here and there. And so we have this like giant piece of test equipment, like taped onto our satellite, essentially for like every voltage rail has a, has a high speed, um, uh, ADC on board. Every, um, like component is behind a, or every subsystem is behind, uh, a, a device that allows us to measure the current flowing to it. And, uh, you know, also protects it in short circuit events like that. But, uh, we have, we have seen things that have surprised us for sure. Um, like certain, uh, degradation of like our, our sensor and things like that, the effects of radiation on certain components. Um, but really we design our satellite for a two year lifetime. So in two years, um, we, we expect to have, uh, different satellites up there in the ring, replacing the, the other satellites.

**Chris Gammell:** Um, do you have, uh, lasers that can shoot other satellites out of the sky? Is that, is that part of the design process?

**Dave Jones:** No, unfortunately not yet. Um, we were talking about, uh, we were talking about lasers for all sorts of stuff, but we haven't put them on there for, uh, we don't have any defensive capabilities, unfortunately. And even if we did, we'd just get pushed out of orbit by, you know, some other crazy technology on some secret satellite, you know, it'd be like, oh, they've discovered it, push them out. Then we'd be like, oh, we never made contact with that satellite. Yeah. Oh, we did have, um, uh, we did have one, which is kind of sad. Uh, the, uh, the dove forward spacecraft is still awaiting deployment inside of, uh, an Italian spacecraft. So we're, we're what we call secondary payloads. So, um, we, uh, we don't buy the rocket, but we'll buy like the leftover space on the rocket. So if there's an extra, like, you know, a hundred pounds or something like that available on the spacecraft or not a hundred pounds, but like for us, if there's an extra five kilograms available, we'll buy that space. And then, you know, the, the people who buy the primary payload are incentivized to sell this extra space that they're not using. So we don't get to decide where the rocket goes, but that's okay. Cause we can operate from any orbit. Um, and so the, uh, yeah, so, um, we were actually a tertiary payload on one satellite on a Dineper where dove three was ejected straight from the Dineper. And then dove four was on another satellite that it was going to eject us later. And unfortunately they never were able to contact or have not yet been able to contact that satellite. And so we're, we're still waiting for, for our dove four to be released from the Italian prison.

**Chris Gammell:** Are you guys like at this point, you're like, what you operating, you're operating so fast. You're just like, come on. Jeez. NASA. Jeez. Italian space agency.

**Dave Jones:** It was, it was pretty heartbreaking. Yeah. But I mean, the other, the kind of, kind of point to all that too is like by the time like, so dove like launches slip left, right, and center, like that nothing ever goes up on time. And so by the time that, uh, towards the end of the release of one B, which is the, the satellites that are right now being deployed from the space station, like our one C satellites have already been deployed. Our one D satellites have already shipped. And like in that there was already two or three iterations of the spacecraft. So like the, the ones that are still waiting to be deployed from the space station, we're like, yeah, it'd be cool if we get them out there. But like, you know, they're kind of obsolete. Like they're, they're not really, you know, the next satellite is like already, we're just like, wow, that's, that's fun. That's cool that that one's up there. But like, you know, I really want to see what this one's going to do in space. So yeah, it's, it's kind of cool, uh, to, to be working on that, that rapid development timeline. And then also when you're like working on this thing in the back and it's just like a bunch of circuit boards and then you're like putting on a solar panel and you're like, holy crap, this thing's going to space. Like, you know, we build them here at second and Bryant. We build spaceships. Like it's, I don't know, it's kind of absurd. We get our, our boards all turnkey and then we just like plug them together. And it's a, and it's like next stop space.

**Chris Gammell:** So there's no like, yeah, there's no like requirements for like external. Okay. So another question about this, like, how about, how about like temperature rating on parts? Right. Cause it gets pretty cold up there.

**Dave Jones:** So, uh, actually we're so close to the earth that we, we get like pretty, pretty normal temperature ranges. We get, um, you know, below, uh, below industrial rated parts, you know, it's our, in the interior of the spacecraft is nominally like 40 to 70 C. Like, you know, they, uh, and we can actually, yeah, yeah. We're, we're so close to the earth that we're pretty thermally coupled to the, to the atmosphere.

**Chris Gammell:** Wait, 40 to 70 C? Yeah.

**Dave Jones:** Yeah. Yeah. Because we have these big solar panels that are pointing at the sun and we can also, uh, we can do kind of a, like if we, if we were seeing like, uh, you know, temperature gradients across the satellite that we're getting extreme, all we have to do is like turn around like the, the sun will heat us up plenty. Yeah. So, yeah, we don't, uh, and then in the, in the shadow of the earth, the same kind of thing we have, uh, you know, we're orbiting every 90 minutes. And so, uh, about.

**Chris Gammell:** So it's more about the cycling of that is about the actual absolute minus temperatures and anything like that.

**Dave Jones:** Yeah. Yeah, exactly. Yeah. So the, the solar panels see the, the outer solar panels see the most extreme temperatures and they'll see, you know, negative 100 C to positive 100 C. But, um, you know, when they're at negative 100 C, we're not, you know, trying to draw current off of them. So it's not that big of a deal. Um, and then when they're back into the sun, they're fine. So.

**Chris Gammell:** Yeah. And cold is better for solar panels, right?

**Dave Jones:** Yeah, exactly. So, you know, they're more efficient when they pop out of eclipse, but again, we're, you know, we, uh, have designed our power system in such a way that it shouldn't be a problem, whatever the temperature. So. Yeah. I don't know. It's, it's, it's fun. So we, we kind of threw away all these things that were like, Oh, you need this, you need that. Like you need rad, rad hard parts at a hundred thousand dollars in FPGA. And we're like, Whoa, whoa. We're like, we're, we're not sure we want to spend like $500 on this FPGA, let alone like, you know, and it's, it's so funny. Cause you see the, you see the hope in the eyes of the, of the sales guys that come to our office and they're like, you know, we have this new aerospace component and we're just like space. Yeah. We, we don't, we don't care. Like we're not going to spend a hundred thousand dollars on a part. Like that's insane. Like, you know, good luck. I agree. I agree.

**Chris Gammell:** Yeah. NASA's NASA's just, just a couple, a couple of hours South in LA, right?

**Dave Jones:** Yeah, exactly. Yeah. Even them there, you know, uh, the, the one down in, um, in San Jose run by, uh, Pete Warden is the, uh, is the director down there and he's, he's just, you know, he's a character. He'll, uh, he feels the same way about all this stuff. If he sees a project like running away, he'll, he'll put the brakes on it. And it's kind of fun too, because we also have, uh, like for, uh, we were recently having, um, some problems with our, our power system in general. Like we need to step back and take a look. And I kind of drew the short straw because I was the, you know, when I, when I came on board, uh, there was a problem with, uh, we had to get the, the batteries through this like certification testing and there were some issues with the packs. And so I was like, Oh, look at it. You know, I don't know what I'm doing yet. So let me, let me check that out. And so now I've ended up becoming like the, the power system guy and we had, um, you know, a power system expert come in and he's just like, ah, he's like kids, you know, what they're doing there. They're messing around and you know, they don't know what they're doing. And it's like super hostile for the first like 15 minutes. And then he's like, Oh wait, you've looked at this. Like you have on orbit data. Like, you know, this works. And we're like, yeah, that's not what we're here to talk about. Like we know this part works. We're working on this part. Like, what do you think of that? And he's like, Whoa, wait, I want to see this data. And you're like, okay, yeah, that's cool. But we want to work on this. And yeah, it's really, it's really fun. It's, yeah, it's a great.

**Chris Gammell:** So like collision, collision of cultures basically at that point. Is that like the. Yeah, exactly.

**Dave Jones:** Yeah. And so we're, we're not like a great place for people who, you know, we call them the old aerospace guys. You know, we have, you know, there's people who come in from the cloak and dagger sort of meetings and they're just like, Oh, you know, we're, you know, we're interested in this. We're interested in that. And you're just like, you know, I don't know if, if this is like, you know, you guys can't sell us parts. Like we're, if people have like, you know, are, have worked on big billion dollar spacecraft, like this isn't, this is totally different. Like we're looking for people who have like backgrounds in commercial and in, um, you know, those types of products, because what we're really working for is building up like a robust design, quick turn. And yeah, I mean, I've, I was here 40 hours this weekend trying to get like a system up and running just before I headed out. And, uh, you know, fighting with pixels on an FPGA is always, always a, a mind wracking experience, but yeah, I love them.

**Chris Gammell:** And you guys do it. Yeah. And I'll, it feels like, like, uh, the Bay area people always do Verilog for your FPGAs as well.

**Dave Jones:** And it's just like, Oh no, we're all, we're all VHDL shop here.

**Chris Gammell:** Oh, you are. Ooh. Yeah. Man. Which is, I wonder, I have to wonder how many people are listening right now and just waiting. It's like, Sean, Sean, what's, what's, what's the hiring link?

**Dave Jones:** And, uh, we are hiring. Uh, yeah, we're actually looking for, um, we're looking for some, some good RF engineers out there. You know, they're just, yeah, we were looking for some RF people right now, kind of build out our ground station network and our, uh, there's some really cool R and D projects. We're working on that. I think, uh, someone with an RF bend would dig, but we're also, um, we're also looking for, we're looking to hire a gray beard. We want someone who, who knows what they're doing to come and hang out with us because, you know, we're just rolling as fast as we can and it's so much fun. But, you know, every now and then you're just like, man, I need, we're really looking for a senior engineer as well. So, so, but you know, we're, we're, we're a hard stop for our senior engineers cause we're kind of, we're crazy. And, you know, they're, it tends, it seems to be like the, the further along, like in your career, that it's like the less year, it seems like the less risk that people are willing to, to tolerate in their world. But yeah.

**Chris Gammell:** And a lot of the older engineers too, they have, I mean, they have families and stuff like that, you know, young people can, you know, work 40 hours in a weekend. And not blank.

**Dave Jones:** Yeah, yeah, exactly. Like I'm burning myself out.

**Chris Gammell:** Older engineers can't.

**Dave Jones:** Yeah. But we're not, we're not expecting that from our, from our engineers either. That's just my, the danger with me is that my hobbies directly overlap with my work. So I like, you know, I'll look at, at 40 hours of VHDL over the weekend as like, well, you know, I could, you know, how can I kind of move this? And that was, that was something I've always done with my, my designs is I'm like, well, I've been looking at this part, like for Fred. And if I like order it and integrate it into this board, like I'll learn all about it and I can decide whether or not I want to use it on my robot. So yeah. Yeah. That's the.

**Chris Gammell:** Which is actually a great, a great way for, you know, I think especially when you're, people are getting started in engineering too, like that is like the ultimate measure for like, if, if you have a decision between two jobs and one pays, you know, twice the other, but you can learn more at the lower paid job, like that is always the currency you should go for. And, and even into, you know, further in the career, I think that that is just like such a valuable thing, you know, because it'll quench your thirst and, and it'll help your career as well too, in the best way possible.

**Dave Jones:** Yeah. I totally agree. I just, yeah. I always tell my friends, I'm like, don't work outside your field, like find, find anything that like you're passionate about and just run with it because it's so rewarding. And yeah, I don't know. It's exhausting. And the burnout, burnout is definitely high at, you know, places like this, but our planet does a pretty good job to, to fight against that with our, our vacation policy of like, you have to take two weeks of uninterrupted vacation a year, at least like weeks of uninterrupted. Oh, wow. That's, that's your minimum of what you have to do. And so after this last, we do a lot of kind of these, um, aggressive, uh, we call them sprints leading up to the design releases and.

**Chris Gammell:** Ah, yes. Agile.

**Dave Jones:** Agile. Yeah. I know. Right. Well, at the, uh, at the end we're shipping the satellites, so we don't have like, there's a hard stop and.

**Chris Gammell:** Yeah. You know, we can never, we don't know when that'll get up either. Yeah. You just like go up soon. Yeah.

**Dave Jones:** That's the brutal part is like, you have to, you have to build this thing and it is on this incredibly tight timeline, but then like it might sit on a launch pad for six months. So, yeah. And you're just like, so, and we're launch minus 60, you know, and heavy quotes. So we have to deliver the satellite that's going into a burlap bag or a canvas bag or whatever. That's like just going to sit in the corner of our room until it's ready to be put into this capsule. And then it just sits there. And so there's still that, like, you know, we're agile, but like our, our lag time is still brutal because then we get up to the space station. We're just sitting on the space station until like the astronauts have time to then move us over to this pod and then put that pod out the window. And then once that pods out the window, they have like another, you know, it's huge lag until all the, you know, turns out that if this satellite, if this launch goes up, then we have to wait another few days. But if it doesn't go up, then we can launch tomorrow. And it's, yeah, it's still, the launch is still the part of the, the industry that needs to kind of catch up with, with what we want to do. But, and there are people working on that.

**Chris Gammell:** Well, and maybe with, yeah, I was going to say like SpaceX and the, you know, the, all the, all the startups out there, right. The virgins and all that might be able to throw stuff out the window.

**Dave Jones:** There's amazing, there's amazing startups that are working on launch technology too. It's like once you're like, I, I had never thought about working in aerospace. That was one of those things I was always told that I'd never be able to do without a degree. And we're like, no, you can't work on satellites. And I was like, all right, whatever. Like it would be cool, but I guess I can't do that. Um, but the, uh, yeah, the, the number of companies that are actually working on like spacecraft and, uh, rocket launch and sea launch and all these other like, you know, ridiculous technologies. There's a ton of rocket startup companies that are building rockets. And the future is so awesome. It's so amazing. And I was talking to one of them the other day and I was like, yeah, you know, nothing's cooler than, than rockets and robots. And he's like, rockets are robots. And it just hit me that it's like, oh my gosh, it's a, it's a fire breathing robot.

**Chris Gammell:** It just breathed out of the butt, right? Yeah, exactly.

**Dave Jones:** It's like this highly tuned control loop. That's really just like swinging around this actuator to push it up into space. It's crazy. Yeah. It's totally nuts.

**Chris Gammell:** But, and sometimes you can make it with a sugar and salt, Peter, on your driveway.

**Dave Jones:** Yeah, exactly. Right.

**Chris Gammell:** And sulfur and sulfur.

**Dave Jones:** Yeah. Yeah. We were still yet to put an Estes rocket up on one of our satellites, but you know, who knows?

**Chris Gammell:** Yeah.

**Dave Jones:** I think there was a CubeSat that did that, that launched an Estes rocket, just like fired into space. Yeah. Yeah. Yeah. Yeah. Yeah. Why not?

**Chris Gammell:** Nice upper trajectory a little bit and put something further into space.

**Dave Jones:** Or, or, you know, closer to earth, depending on how, how tuned your control loop is. And I guess on the accuracy of your Estes rocket, you know, but. Right. I don't know. No, it's.

**Chris Gammell:** I know you're going on vacation, so I'm going to, I'm going to, I'm going to cut us off at a, at a brief two hours and 20 minutes.

**Dave Jones:** Oh my gosh. Yeah. Sorry. Just babbling.

**Chris Gammell:** I'm going to believe that I'm going to be picking your brain the next time I'm in San Francisco. Because I want to hear more about this stuff. The, the things we didn't talk about were the control, the FPGA control loops, like you mentioned for Fred. Yeah. That's definitely an area ripe with, with interesting, interesting problems to be solved. I'm sure. Oh yeah.

**Dave Jones:** Yeah. Absolutely. So. Well, thank you so much for, for letting me babble at you for a while. I don't know.

**Chris Gammell:** Oh, it was great, man. That's, you got some crazy stories. I got to say. Thanks. It's like, oh, okay. So you were in, you'd make stuff for space and you lived in Antarctica and blah, blah, blah, lasers and robots. Yeah. No. Yeah. I guess it's normal.

**Dave Jones:** Yeah. Yeah. Steady state. Normal, normal trajectory.

**Chris Gammell:** Oh, wait, sorry. One last thing. Where can people find out more about you and Planet Lab?

**Dave Jones:** So Planet Labs is planet.com. You can check that out. There's a, there's a link there for, for hiring. That's something crazy that I was a part of for a little bit until I got yelled at by, by someone we were trying to hire. And then I fell out of that because I'm not, I'm not, I'm not there yet. I don't want to, I don't want to be a part of that world, but if he's listening, apologies. Yeah. So we have, we have someone else handling that now. So the hiring is through, through planet.com. And there's a, there's a join the team side of that. And also you can check out the imagery from our satellites on, on planet.com slash gallery, which is a link on the homepage too. Uh, I, I have, you know, one, one video every, every like four years on, on YouTube under, under logic low and, uh, same at logic low.com.

**Chris Gammell:** Well, I highly recommend people check that stuff out and I'm going to be checking out planet.com and I want to see some pictures.

**Dave Jones:** Definitely. It's worth a shot.

**Chris Gammell:** Cool. Well, thanks again, Sean.

**Dave Jones:** Yeah. Thanks so much for having me. Bye.
