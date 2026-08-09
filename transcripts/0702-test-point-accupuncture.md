---
episode: 702
title: Test Point Accupuncture
url: https://theamphour.com/702-test-point-accupuncture/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released September 14th, 2025. Episode 702. Test Point Acupuncture.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** I hate laptops. And batteries. And weird shit. Guess what happened? Just before the show, I got a new refurb. I thought, oh yeah, I'll be smart. I'll save some money. I'll get a refurbished laptop. It's one of these Microsoft Surface things. And so I get it like it's near perfect. It's like it looks fantastic. It works. It actually turns on and everything. But I've got this weird fault with it though. And it's literally in the box. I'm going to return it now. But see if you've ever heard of any fault like this, right? The battery in it, like it came with like 70% charge or something. So I plugged in the battery last night. Sorry.

**Chris Gammell:** I said pretty standard. Like that's the charging level for that sort of thing.

**Dave Jones:** Yeah, exactly. And it's supposed to have like a 85% battery capacity or whatever. But, you know, even like because it's used, right? So you're going to lose some of the original capacity. And we did the printout, like the diagnostic report for it. You know, ran the command line script. So you can ran the command line script and everything. And did the battery health report. And sure enough, you know, it's lost some of its capacity. But batteries should still charge to 100%, correct? Right? They should still indicate 100%. So I plugged in the charger last night thinking, oh, yeah, he'll use it tomorrow. And so we plugged it into the charger. Came in, woke up this morning, went to it, and went, it's only got 40%. What the heck's going on?

**Chris Gammell:** I've had that happen before, actually. And it was a bad charger, though.

**Dave Jones:** No, it wasn't the charger because we used another charger. And it wasn't the included one because he's got another Microsoft Surface. So we used that. Yeah. So it wasn't that. And Windows indicated that it was charging. And the charging LED on the side of the little magnetic plug-in, you know, charger doodad. It all lit up. Windows lit up and said it's charging. But it didn't charge. It discharged overnight. And then when it hit 40%, it started charging and went up to 50% and then stayed there, flat. I can actually send you the graph of it. But, yeah, it just stayed flat. Like, it stayed at 50% and just sat there.

**Chris Gammell:** You tried multiple chargers, you're saying? Yes. Because I've had that where it said it was charging fine. It was a 20-volt charger or whatever, but it was just underpowered. So it wasn't outputting any actual current. Right. And so it was, like, trickle charging at the right voltage. And it just never made it up there. And then the consumption of the machine would overtake the charger, you know. Yeah.

**Dave Jones:** But this, like, it just got to 40% and then started charging and went to 50%. Here we go. I've sent you the graph. And you can see where it – there's a charge indicator where it shows last night I actually plugged it in. There's that little charge thing above it, right? Yeah. Like it's charging. Yet it goes down. It goes down and down. And it hits 40%. And then it charges back up to 50%. And then it stays flat at 50%. Like, what? How is this even possible?

**Chris Gammell:** Bitcoin mining at any point throughout the night, you know? No. No. No. No. That is weird. Yeah. I'd say, yeah, just from a warranty perspective, too. You know, they'll guarantee the lemon law kind of thing. Yeah, yeah.

**Dave Jones:** I send it back. Yeah. I simply – yeah, I just print out the return label and I'll send it back. And it's like, yeah, I expected the battery to have – like, lose some of its original battery capacity. But it still should charge to 100%. Yeah. And there's a weird thing with the power button as well. Like, it doesn't work. You have to actually hold it down for 10 seconds and cold boot it every time. So, yeah, that's a weird-ass laptop. So, yeah. Back it goes anyway. So, yeah. Speaking of weird-ass.

**Chris Gammell:** Wait, wait. I was going to transition to – I mean, yes, weird-ass is good, too. I was going to transition to charging things. I'm actually finally – you know, just the – you know, now that we talk monthly effectively, my house has been running. Oh, yes. And it's basically just an appliance now, which is awesome. So, I have –

**Dave Jones:** So, the battery is finally working because you did have – tell us a story. That's right. You did have a – Oh, yeah. I didn't even say what it was.

**Chris Gammell:** Yeah, that's right. Yeah. All it was – last time we spoke, the system had been provisioned. It was on and it was, like, not doing anything. It was basically, like, the Powerwall had charged up to 100%. And in this case, all it was, it was just a loose RS-485 wire because there's – so, like, it's on the – The battery is in the back of my garage and the switch, like, the controller box basically is up at the panel right at the front of my house.

**Dave Jones:** This is a Tesla Powerwall, right? I thought they were entirely integrated.

**Chris Gammell:** They are not. They are – What? So, the charger – sorry, the inverter and the batteries are integrated and they're gorgeous. They really are nicely designed. Oh, yeah, yeah, yeah. Yeah. This is actually the controller box that switches – and this might be regional. I don't know if it's different in other parts of the world. But this is the thing that basically tells the, you know, switches at the breaker and says, oh, actually, we're going to back power now into the –

**Dave Jones:** Oh, so it's got smart switches in the breaker, does it? It's got, like – Exactly.

**Chris Gammell:** Well, it's its own control box basically. So, the thing that back feeds into the panel, that is where it shuts down. And so, when the battery and inverter have power, but either I'm, you know, I don't have clearance. So, like, if you don't have the permission to operate, then that will be off, right? So, that basically any power that you try and back feed it, it hits a brick wall. And so, finally, then, when you are ready to export power, that needs to be activated. Let me look up what they actually call it, the power wall, like, switch matrix or something like that. It's something like that. They haven't – Oh, wow.

**Dave Jones:** I had no idea there was a separate box. I thought it was just a one-box solution, which –

**Chris Gammell:** Yeah. It's very good.

**Dave Jones:** Have you ever seen the teardown of the Tesla Powerwall? Yes. It's very impressive. Yeah.

**Chris Gammell:** I think we've – I think we talked about it here. It's very – Yeah, yeah, yeah. It's very nicely designed. Yeah. Yeah. It's got – yeah, it's got Wi-Fi. It's got cellular. It's got all that stuff.

**Dave Jones:** You've got to – hats off to Tesla. They do engineering very, like, very well. Yeah. You know, like, as in the actual implementation of the – you know, like, physical hardware builds and stuff like that. They're very nice. Yeah. Definitely. Definitely. Yeah.

**Chris Gammell:** And so, yeah, it's up and it's running. And, like, literally it's an appliance at this point that I just check the app and it's like, oh, look, I, you know, generated – generate less power than I thought I would. You know, universally, my friends told me that would happen. But that's fine. I think it's, like, you know, it's going to be more valuable over time as power gets more expensive from the provider. And honestly, just, like, how the time of year it is right now, too. Like, my panels are kind of, like, better suited for, like, leaves fall off the trees just because, like, I have one big tree that's in the way. Right. Okay. Yes.

**Dave Jones:** Oh, because it's four now, as you guys call it, right? That's right. Yeah. Awesome. Yes. Yeah.

**Chris Gammell:** It's – we're probably about, like, a month and a half from the leaves falling off the trees here. But already up north. Yeah. They're starting to turn and fall off. Right. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Interestingly, though –

**Dave Jones:** Speaking of trees and sun, though, we've wanted to get these – hang on. We've wanted – just a little side tangent. We've wanted to – Oh, yeah, yeah. Come back. We wanted to get these, like, veggie pods, they're called, which allows us to grow our own veggies and, you know, like, birds and stuff like that. Yeah, sure, sure. And they're in these nice pod things. But we really don't have anywhere with sun. But we just trimmed back with, you know, suitable sun during the day. But we just trimmed back our gigantic rows of trees out the front. So we're actually – so now we've actually got a greater sun angle there. So we've got more hours per day. So we trimmed, like, a meter off.

**Chris Gammell:** Man, you can buy more panels. You don't need veggies. Get more panels. Oh, buy more panels. Turn electricity into veggies.

**Dave Jones:** That really feeds us. Okay. Yeah.

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Yeah. I'll do a startup tech with, you know –

**Chris Gammell:** You know.

**Dave Jones:** Yep.

**Chris Gammell:** How about you could, you know, put solar panels up top, but then you have algae down below it. And then that feeds some – I don't know. Yeah.

**Dave Jones:** Yeah, we can eat microplankton or something. Yeah.

**Chris Gammell:** Actually, I did – I was watching a thing about – what was it? It was, like, oyster farming in the northeast of the U.S. And that's, like, coming back. And, yeah, apparently oysters eat lots of algae. I did not realize that. Oh, right.

**Dave Jones:** I didn't know what they ate at all.

**Chris Gammell:** Yeah. Yeah. They're, you know, they're, like, filter kind of bivalves. So, yeah. Yeah. Plankton and algae. Sorry.

**Dave Jones:** That was a tangent you were saying?

**Chris Gammell:** Yeah, yeah. No worries. So, I started looking into this just because, like, you know, the app gives you, like, costs and, like, how much you're saving per day and stuff like that. And it's not a ton. It's fine. All right. Yeah. But I started looking into just, like, power rates. And I think we talked about it on the show before, but it's, like, super cheap here. It's, like, some of the cheapest power in the U.S. Not the cheapest. I think the cheapest is, like –

**Dave Jones:** Where does your state – because, you know, they're very state-based over there. Where does the majority of your state energy come from? Have you got a local nuclear plant? We do.

**Chris Gammell:** Well, we have four nuclear plants in North Carolina. And it's, like –

**Chris Gammell:** The mix is, like, 70% nuclear. And that's why it's cheap. Yeah. That's why it's cheap. Yeah. I was very curious about that. Yeah. Yeah. Yeah. So, that's why it's, like – I think it's, like, we're at, like, 13 – like, 12.5 or 13 cents per kilowatt hour, which is nuts because it's, like – Right. I think the – I was looking at the highest per statewide in the U.S. It goes, like, Hawaii is 41. Yeah. California is, like, 38. And then, like, you know, down from there. But it's – Yeah. It's, like, orders of magnitude. Orders of magnitude. But, like, multiples, right? I mean – Right. Yeah.

**Dave Jones:** We're probably 24 U.S. cents per kilowatt hour here. Oh, okay. That's less than I would have guessed. I thought you said it was more. Right, okay. Well, we're about 35 cents, which is probably about 25 Yankee – 23 Yankee cents or something like that. Yeah.

**Chris Gammell:** Yeah, yeah, yeah. Okay.

**Dave Jones:** So, it's high for here, yes. Because we – Yeah. Because we ban nuclear. We're stupid, you know. I think anywhere that does it is –

**Chris Gammell:** I can't believe that, you know, Germany's going back on – like, just, like –

**Dave Jones:** They – yeah, they had them, didn't they? Didn't they have, like, a dozen plants or something? And they decommissioned them all. Why would you do that? You went to all the effort to –

**Chris Gammell:** I think it's – yeah.

**Dave Jones:** Oh, stupid politics. Oh, my God.

**Chris Gammell:** Yeah, I think that's a big part of it. I think it's – and that's one of those things, too, where it's like when it goes away, it's – Oh, yeah. The time to start it back up is – It's hard to get it back. Yeah. Yeah.

**Dave Jones:** Yeah. Well, it's literally still banned here. We have both federal and state bans on nuclear energy.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** So, like, even if you wanted to do – yeah, look, even if you're some rich billionaire, I'll build a nuclear plant for you. No. It's banned.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** It's like, you know.

**Chris Gammell:** Yeah. It's so dumb. I'm curious about it. So, like, you know, I was just kind of, like, using the dummy box and asking questions and stuff like that. So, you know, take it all with grains of salt. But, like, rates, those are very easily lookup-able, right? That's fine. Yep. But the thing I was curious about was, like, the amount of waste generated just because I was like, oh, well, you know, like, it's higher than I would have guessed per plant. And it was something like 77 kilograms – not kilograms. Was it tons? Oh, you're talking about the – It was more than I thought per year. Yeah.

**Dave Jones:** You're talking about the nuclear waste.

**Chris Gammell:** Yeah, waste product. Oh, okay. Right.

**Dave Jones:** Yeah. Okay.

**Chris Gammell:** Oh, yeah. Duke Energy Generation Mix. Here we go.

**Dave Jones:** It's actually, yeah. What, it's more than you thought? Yeah.

**Chris Gammell:** It's more than I thought. Right. It's kind of closer to, like, the kind of my initial idea on it. Like, you know, I think a lot of the modern stuff around it is just, like, if you look at, like, true waste of it, it's, like, you know, like, the offshoots from, like, a coal plant and stuff like that. It's, like, that's very, very high, right? But it's, like – Oh, yeah. Yeah, yeah, yeah. In my head, I was, like, oh, it's, like, making, like, buckets of nuclear waste, right? You know, sort of thing. Yeah. So, like, the – let me see if I can find that in here. Waste. Megawatts. That's not it. How much waste is generated? It says – How many barrels? It's about 50,000 to 77,000 kilograms of nuclear spent per year.

**Dave Jones:** Per year. Per year? Is that one plant?

**Chris Gammell:** Per plant.

**Dave Jones:** Yeah, exactly. Per plant. Okay. Yeah.

**Chris Gammell:** Okinaea is the – is my – is the – one of the local plants here, like, one of the bigger ones. And that's a 2.5 gigawatt plant. Right. Which is, you know, big, really big. Yeah, yeah.

**Dave Jones:** Offhand, I don't know what the biggest ones are. But it's around about that, I thought. Yeah. It's around – you know.

**Chris Gammell:** So, 20 to 30 metric tons of used fuel per one gigawatt per year. Per one gigawatt energy a year. Okay. So, like, multiply that if you have a two – this is a two and a half terawatt plant. So, yeah.

**Dave Jones:** You can't reprocess it. It's just more than I thought. It's a lot. Right. Yeah. Okay. Yeah. Yeah, but in the scheme of things, it's not – well, it's still not a lot.

**Chris Gammell:** But also, that's kilograms, and that's not – you know, like, uranium is a heavy material, and it's like – Yes. Maybe volumetrically, that's not a lot either.

**Dave Jones:** It's 10 barrels or something, maybe. Right.

**Chris Gammell:** Exactly. I don't have an idea for that.

**Dave Jones:** I don't know exactly how many barrels that is. But, again, it's more than I thought. I was looking into the waste side of things because I always wonder, oh, yeah, we need these, you know, hollowed-out mountain solutions to store it and everything. Yeah, right.

**Chris Gammell:** Exactly.

**Dave Jones:** Apparently, you can just leave them there on site, just sitting in a concrete thing, and there's no excess radiation from them. You can stand right next to it, and it's not a problem. It's like, you know –

**Chris Gammell:** I would prefer not to.

**Dave Jones:** I don't know if it gets into, I don't know, the groundwater or something like that, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah, yeah. But apparently, yeah, it's not a problem. Apparently, the storage solution is not hard. You can just literally just leave it there. Sitting in a concrete thing. You know, the Simpsons would have me thinking otherwise, Dave. Yeah, exactly. Exactly. Right, right. Anyway, anyway, it's very interesting. Don't let the fish get to it. So, yeah, I'm kind of jealous that you guys have cheap nuclear power, and we don't. But, yeah. In several other countries, France is huge. Like, France, I think, is one of the biggest in the world.

**Chris Gammell:** They're an exporter. Yeah, they export.

**Dave Jones:** Yeah. Oh, yeah. Yeah, yeah. They're an exporter, aren't they? Yeah. Crazy.

**Chris Gammell:** I got the numbers wrong, too. So, this is the nuclear is 53%, natural gas, 33%. Coal is 9%. Hydro is 1.3%, and solar is 2%. Natural gas?

**Dave Jones:** That's high for natural gas.

**Chris Gammell:** No, natural gas is a huge mix in the U.S. right now.

**Dave Jones:** Wow. Wow. Okay. That's surprising.

**Chris Gammell:** Yeah. Just build a couple more nuclear plants and you're done. No, I mean, like, the cost and just a lot of them are older. So, like, a lot of the natural gas in the U.S. is very, very cheap because coal sands, sorry, what's it called? The stuff up north from Alberta and stuff like that. And then just fracking in the U.S. in general. Yep.

**Dave Jones:** Got it. Yep. Still, there you go. Interesting.

**Chris Gammell:** Yeah, yeah. Knowing the mixes is very interesting. Oh, yes. Hey, I am an exporter now, too, so I'm part of that mix.

**Dave Jones:** Excellent. Yeah, but somebody else controls that, right? It's like they can pull it when they need it, right? It's one of those. That was part of the deal. Yeah, that hasn't.

**Chris Gammell:** That's right. Yeah, that hasn't happened yet. But that is there. Yeah. Yeah, it has been interesting watching, like, the, you know, like, the, so we had one of my friends on who works for the DOE. And he was kind of telling us about the duck curve and stuff like that, like, the, you know, the usage throughout the day and peaker plants. And, like, you know, you and I talked about the, you know, the, how Australia is paying for batteries. And I was really surprised just how much, you know, a relatively small battery carried me through. So, like, I usually stop using power around noon, given where my panels are. And I don't start using power again from the grid till, like, 8 or 9 p.m. And so, like, that carries me all the way through that, that, the dip in the duck curve. And, like, I think the only downside to my system that I could see being problematic from the grid perspective is, like, I don't have any, like, on a sunny day when it's not super hot out, like, right now. So, like, it's cooling off here. It's still super sunny. So, like, 3 p.m. right now, my battery's full. You know, if I'm not, like, the dryer's not on or I'm not, like, using the washing machine or something like that.

**Dave Jones:** Right.

**Chris Gammell:** Like, there's nowhere for the power to go. So, it's going back to the grid. So, like, me and all of my cohort here are dumping power on the grid. Yes. And that's probably right when you, you know, like, the equivalent when you are getting paid to take power, I'm guessing they're looking for the same thing. So, like, from a battery perspective, it makes a lot of sense. I think my prediction on this is that they're going to start trying to get consumers without solar to start doing it, too. Because, like, where else are they going to put that power, right?

**Dave Jones:** Well, exactly. That is the problem that we've got here, which is why the government, the new government, just announced the $2 billion battery scheme where everyone gets a battery. You get a battery. You get a battery. Oh, so there's no solar. Because there's so much excess solar. Oh, sorry.

**Chris Gammell:** Interesting. There's no, like, need to get a solar setup.

**Dave Jones:** No, there's no need to get solar. Because we already have the world's largest uptake of home solar in the world. Got it.

**Chris Gammell:** Yep.

**Dave Jones:** Right? Like, almost 50% of the houses in Australia have solar.

**Chris Gammell:** Yeah.

**Dave Jones:** It's huge, right? So we've got so much excess that we've got nowhere to store it. We've got nowhere to use it. So, yeah. Yeah. So I can... We've kind of backed ourselves into a corner there. Yeah, whoops.

**Chris Gammell:** I think we're right behind you. But also, like, the fact that... So then a user... So now somebody around you, you know, gets subsidized, the battery, whatever. Then you take them out of that duck curve equation, right? Yes. Because the same problem happens. Like, if you are electrifying everything, like, where do you... You know, they all come home at 5 or 6 p.m. as well. They all, you know... Exactly. Plug in their cars, turn on their stove, whatever. Like, do the wash. You still need to take it from somewhere. So, like, you either got to store it at grid level or store it in someone's house. And I'm surprised at how much the battery carries me through to, like, you know, like 8, 9 p.m. So.

**Dave Jones:** Interesting. Okay. Yeah. Yeah. Ours barely last, which is why we're going to expand ours. But I've got an update on this. One of my batteries... Oh, yeah. Cool. Well, died in quote marks. You know how I've got five? I've got a big rack of six, but I've only got five in there. Yeah. One of them is playing silly buggers, so I had to shut it off. And we've tried to, like, originally, you know, I'm talking with Peter. He's been on the show before he actually designed the battery. And he seems to think, oh, yeah, I've got very early, like, almost beta firmware in it or something. We need to upgrade your firmware. Right? So he sent me the doodad, the remote doodad box, you know, to try and... So that he can update the firmware remotely. Somehow I killed that. And it's the second one I've killed. I don't know how. So he's going to have to send me a, like, a 3G, like a 4G modemy interface or something.

**Chris Gammell:** Dave, if only you knew someone who works on IoT things that does over-the-air updates. Right.

**Dave Jones:** Well, you know, it's... Yeah. It's... But, no, I somehow... I don't know. I killed this gateway thing which hooks up to the Ethernet. And it's just... I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** But, yeah. Anyway, I killed two of them, actually. Two of them? Yeah, yeah, yeah, two. Because he originally gave me one when I got the battery. Oh, that's a total skill. Yeah. Yeah.

**Chris Gammell:** I mean, you and me run the cut from the same cloth. I've killed many things like that, too, yeah.

**Dave Jones:** So he's got no idea how it happened. So, anyway, we're going to have to sort that out. So, yeah, it could be, like, a weird firmware, you know, thing. And it's just automatically switching off. And, yeah. So, yeah. It's not the actual battery part of it, I think. Got it. Yeah.

**Chris Gammell:** Batteries, the cells are still healthy, whatever.

**Dave Jones:** It's just the... Cells are healthy. The computer. The computer's got problems. Yeah, the old firmware. Because I was kind of, like, not quite a beta tester, but I was a very early adopter of this new battery. So, yeah. Yep. Yep. So we need to update that. Anyway, so I'm expanding with, hopefully, a lot more of those soon. We're getting our new pavers laid today outside the house because we had to get that done before. We could add the... Before we could install the battery. So that's being done today. Cool. So, yeah. Hopefully. We can get some follow-up on that.

**Chris Gammell:** Yeah. That'd be great.

**Dave Jones:** Yeah. But I'm still at 20 kilowatt hour battery. So, yeah.

**Chris Gammell:** Do you guys ever do the thing where you, like, just cut off your own access and you're just like, yeah, we're just... I have an option for it. No. To go off-grid. No, I don't want to cut off.

**Dave Jones:** No, I don't want to go off-grid. That's dumb. That's just the dumbest thing ever.

**Chris Gammell:** I can see it for, like, people that were remote that, you know, it'd be more... Oh, yeah. Oh, totally. If I was remote, yeah. More of, like, a test mode for when things are flaky or whatever.

**Dave Jones:** But, yeah. Yeah, totally. But when I install the new battery, I might install one of those reversing switches so that I can power the entire house from the battery if the power fails. Oh, yeah. That's what I meant. Sorry.

**Chris Gammell:** That's... I didn't know that was... That's what I was wondering. Oh, okay. If you could do that and stuff. Okay, so that is, like, not a...

**Dave Jones:** Well, Peter actually recommended that I do that. He recommended that I power the entire house from the inverter and then only if, like, you know, something happens, do we switch back to the grid. But then it's like, nah, the inverter's only 8 kilowatts maximum. I'm going to have to get a new inverter, so I'm going to ditch that DI thing I've had so many problems with. Don't know which inverter. But, you know, 8 kilowatts. If we turn on all of our stuff because our entire house is fully electric. Everything. Right? Yeah.

**Chris Gammell:** It goes up faster than you'd think, too. Oh, yeah.

**Dave Jones:** Yeah. Like, you know, 8 kilowatts sounds like a lot until you turn everything on at once. And then he said, oh, yeah, you'll have to do your EV from the grid and then I'd have separate lines going everywhere. Like, it's like, no, no, no, I'll just keep going from the grid. So do you have everything fully electric? Hot is your hot water from?

**Chris Gammell:** It is. It's resistive. No, that's on the list of things to replace. That's resistive. Oh, okay. Right. It is electric.

**Dave Jones:** With the battery, you want to change to a heat pump for that.

**Chris Gammell:** Yeah, totally. Yeah. Yeah, right. You know, we've been here a year. I got the panels first. So, yeah, no, that's on the list.

**Dave Jones:** And does that charge overnight? Like, does that, like, do it overnight or is it just a thermostat anytime it needs it kind of? Yeah, anytime it needs. Right. Okay. Yes.

**Chris Gammell:** Yes, certain members of my household are very particular about hot showers. They will go nameless. Yes. Nameless here. Oh, yes.

**Dave Jones:** Nameless. Yes. I also have nameless people. You may also know that. Yeah, yeah. Yes. Yes. It's fine. It's fine. The hot shower dictates everything we do. Yes. Right. Everything we do. Yeah.

**Chris Gammell:** And so we also have a weird thing. So, like, we have a garage apartment for when people stay. And so that's on a different, it's, like, subpanel. So that's actually not metered at all. Oh, okay. So, like, there's a big.

**Dave Jones:** Oh, it's not metered? Sorry, it's not metered by the.

**Chris Gammell:** No, no, no. Sorry. It's not metered by the. It's separately metered. It's not backed up by the Tesla power wall. How about that? Oh, okay. Gotcha. So it comes, the power comes in from the, from the grid to, to the electricity meter. It's then split into two, 200 amp subpanels. Ah, okay. 200 amps in the U.S. because it's lower voltage.

**Dave Jones:** Ah, so your Tesla's only connected to one subpanel.

**Chris Gammell:** That's right. The one for my main house. Gotcha. Right. Exactly. So, and then, but then the garage, like the, even though the power wall's on the garage, it's not on the grid there. And so the, the second subpanel that powers the garage apartment, that's the one that would charge my car and stuff. So I, I don't, like, back that up or anything like that from, yeah. So, and it's fine. It's fine. It's, you know, we don't use that much.

**Dave Jones:** Yeah. Yeah. Interesting. So are you aware of anywhere in the U.S.? Maybe, maybe you haven't looked, but are you aware of anyone, any state in the U.S. that has a similar plan to mine where I get free power during a certain time window every day?

**Chris Gammell:** No, not that I've heard of yet. I, like I said, I could see it happening with like uptake, you know, like. Yeah. Oh yeah. Because they're just so sunny and you had that big. Oh yeah.

**Dave Jones:** And we've got the massive world's biggest uptake. Yeah. You combine those two things and we, yeah, you can actually have too much solar, which is a weird thing. Yeah. Right? Yeah. You know? So.

**Chris Gammell:** I think there's too much solar, but there's too much solar if there's not enough grid storage. Right? If there was like, if you guys had like a lot of hills and like water that you could pump up and down it, then it would be fine. Yeah.

**Dave Jones:** Yeah. We, yeah. We'd be using that, but yeah, we don't. So no pumped hydro. Well, no, we do have a new pumped hydro scheme somewhere, but it's not in Sydney. So. Right. Exactly. Yeah. Yeah. The distance matters too. Yeah. Sydney's actually reasonably, well, no, I, I am in the Hills district. It's in the name, the Hills. Right. But still, it's not, it's not conducive to such things. Right.

**Chris Gammell:** Exactly.

**Dave Jones:** And, but no, you can solve that problem if you have smart solar inverters, which, can be remotely switched off and things like that. Yeah. Right. And they're talking about that. I believe this new battery, um, thing, this new battery thing, you have to have an inverter that is at least capable of in the future of being remotely controlled by the powers that be. So, you know, that's like, yeah. So that's like my wall. Right. So the only reason that excess solar is an actual problem is because they have no ability to turn it off. Right. Whereas if you, if, if they're all smartly integrated and the grid controllers could just go, oh no, we need to turn this suburb off now, then boom, you know, then you'd be able to solve the problems.

**Chris Gammell:** It's almost like the inverse of like, like instead of drawing off the battery through the inverter to back power the grid, you know, at the events they want to. Yes. Yes. You literally turn off the solar. Yeah.

**Dave Jones:** Yeah. You turn off the solar and, oh, the grid's stabilized again. Thank you. You know. Yeah. Right. Exactly. Yeah. Right.

**Chris Gammell:** And that's, and that's just like how they, that would just be them moving up the IV curve. Right. I mean, that's like basically what we're doing. It's like, it's like whatever it's like MPPT, but it's M is minimum. Right. It's the maximum. Minimum PowerPoint tracking. Minimum. Right. Yeah. Yeah. Yeah. Yeah. Cause it's like also when I, I was surprised when these things were off, I was like, well, what are they doing inside that box? And it's like, oh, well, they're just opening up the, the switches. Right. Turning off the relay.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Yeah. And it can handle five, 600 volts that the, the panel strings at and just not drawing any currents. I go, oh yeah. Okay. That makes, that makes a lot of sense then. Yeah.

**Dave Jones:** You know, so it's basically the, the energy from the solar panels doesn't have to go anywhere. Right. Exactly. They sit there and they, and they have their open circuit voltage of, you know, any word ever it is per panel, you know, and they just sit there, but yeah. Yeah. But, um, no, cause we, we, we started solar early. We were one of the early adopters of solar schemes here in Australia. So they're all dumb inverters. They weren't connected, you know, all that sort of stuff. So 95% of the country doesn't have smart connected solar inverters. So yep. Oopsie.

**Chris Gammell:** Um, you'll figure it out. Yeah.

**Dave Jones:** Anyway, I am enjoying my, uh, three hours free per day. So we've, we've got everything on timers now. So it comes on at three o'clock as, as soon as 11 o'clock, um, comes on, we plug in the EV, you know, but we have the lifestyle to do this cause she's usually home during the day. She works from home. So most days. Um, so yeah, we can just plug in the EV once it hits 11 o'clock. It's bloody annoying though.

**Chris Gammell:** That's when you turn on like the pool heater and the water heater. Yes. Yes. Yeah.

**Dave Jones:** The pool pump comes on the heat pump, hot, hot water system comes on. You know, we might turn the dryer on if it's a bad day or something like that, you know? So yeah, it all, boom door comes on. It's fantastic. Um, I can send you some screenshots of that.

**Chris Gammell:** It's really, yeah, that'd be, that'd be interesting. I feel like that's always like the, that's always like painted at the, as like the dystopian, like, oh, well you'll have to like be like, you know, you're, you're at the whims of other, you know, the sun and stuff like that. It's like, yeah, but you just kind of figure it out. Right. It's like the freest power source. You're just going to like work with that.

**Dave Jones:** It's free.

**Chris Gammell:** I mean, hey man, plants do it. It's free real estate.

**Dave Jones:** Oh boy. Yeah. So yeah, I'm just trying to grab the, uh, grab the graph now so I can show you.

**Chris Gammell:** The freeness of it is very interesting. I think, like I said, I think that is in the Southern States. If in the U S where there's just like sunbelt, like there, there's gotta be that much power, but I think just the uptake isn't quite there yet. So once, once it is taken, you know, I sent you the screenshot.

**Dave Jones:** So you can see this is, uh, the last 24 hours or whatever. Um, this is a few days ago, a couple of weeks ago, but you can see that during right at 11 PM, boom, we, we start pulling all the power for three hours and then it switches off. And then we've got, and, and we, and we charge the batteries during that period as well.

**Chris Gammell:** Um, so this is the usage that you have, like, it's just like hollowed out cause it's not paid for. Is that right?

**Dave Jones:** Yes. Yes. Oh, interesting. That's right. So, yep. Yep. So, so anything above the line there. Yeah. Yeah. So, so if there's anything above the line there, that's us consuming and anything actually below the line, the orange there is us, us actually exporting. We've got so much excess that we export. Um, and it's still, well, it's not winter here anymore. It just became non-winter the other day, which is excellent.

**Chris Gammell:** That's great. That's great. I'm jealous. Yeah. We're, we're, we're headed down into the dark, the dark times. Yeah. You're on the downhill. Yeah. Yeah. Yeah.

**Dave Jones:** Sorry, dude. Yeah. That's fine. That's fine. Live on the wrong side of the planet. Yeah.

**Chris Gammell:** Well, yeah, six months out of the year. We all do. Unless you live in the middle. Sorry. Sorry to all you central, central Americans, you know.

**Dave Jones:** Yeah. All right. Well, that's enough of this solar power rubbish. I've been, I did an interesting repair the other day.

**Chris Gammell:** I saw it actually.

**Dave Jones:** Videos on my main channel. Yeah. Yeah. It's like, it turned out to be very simple, but it's something that I didn't expect. It's this tennis remote. For those who haven't seen the video, it's this tennis remote control thing. So it's just a little micro with some buttons on the front, you know, and it sends an RF remote signal. And it's got one of those membrane keypads on it. Right. And it didn't work. And so I opened the thing up and I'm looking at it and I'm going, and like, and all of the keys didn't work except for one row. Right. There was only one row of keys that worked. And I thought, well, you know, like these, these flat membrane keypads, they've, you know, the, you can get breaks where the, where the actual membrane. Right. Right. Right. The flexure breaks. Yeah. Yeah. Yeah. You can get these flex, you know, I see them all the time. Right. It's a very common folia mode in these flex cables, but like usually that would only take out one row or one column. Right. It wouldn't take out all four. It wouldn't take out four of the five rows. Like, how do you have a break in like four of the line, four out of the five lines, you know? But it turns out that yet this cable didn't use like a copper in like a copper trace. It, it actually used a silver conductive ink trace and the silver like migrated away or something on four of the traces. It was like, yeah. So I had to repaint. I had to get silver conductive paint and paint on the four traces and boom, fixed, you know? But yeah, that was, that's something that I hadn't seen to that extent before. I've never seen that. Something I didn't expect. Yeah. Yeah. I just, I didn't expect it. Weird.

**Chris Gammell:** I have, I have a friend who lost a row on his like custom keyboard and troubleshooting that same kind of thing of like, yeah, maybe there's like a broken tray. It's like a column. Yeah.

**Dave Jones:** A broken tray, a bad contact, whatever, but four of them.

**Chris Gammell:** Yeah. That is odd. I think the cabling is interesting too. Cause like that, that I could see it being, I don't know, like maybe water ingress though. Like what do you think the actual migration?

**Dave Jones:** No, no. Cause this thing had been hardly ever used and there was no sign of water ingress at all. So yeah. And, and it wasn't the flexion point. It wasn't like that. It was being like, you know, stressed or anything. Cause this thing was just sealed inside a box and it didn't move at all. And yeah, it looks like some sort of weird chemical silver migration. Um, I, you know, tarnishing, I don't know, you know, combines with oxygen in the air and it just eventually died. I don't know. Yeah. I don't know. Not a chemist.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. Anyway. Yeah. Weird.

**Chris Gammell:** So yeah, that is weird, but good, good fix, man. Yeah.

**Dave Jones:** I, I, yeah.

**Chris Gammell:** Yeah. That's a good one.

**Dave Jones:** I was glad to get something that was at least interesting. You know, if it was just a broken trace, it's like, Oh God, I probably wouldn't have even bothered doing the video. I would have been very disappointed. Oh yeah. It's a broken trace due to the flex in the cable. You know, whoop dee doo. Same as that ever was. Yeah. Fascinating. But anyway.

**Chris Gammell:** I, uh, I have been, uh, living, living one of the rules we've had stated. No. Yes. I'm very lucky, but no living one of the rules that we've had stated many times on the show. But when you don't listen to your own rules, um, you, uh, Kamigatsu. Yeah. Yeah, exactly. Like, I'm just, you know, I'm, I'm in it now. And, uh, I put two, for some reason, my dumb brain thought that I could squeeze two test points right next to each other in a, I think they're like one millimeter pads, you know, like just like super tiny, super like, what the hell was I thinking? I didn't put any other test pads on board, you know, something is like a phone's going

**Dave Jones:** off and that's not my phone. What?

**Chris Gammell:** Days been invaded.

**Dave Jones:** That's weird. Something weird just happened. I don't know. Weird sounding in lab.

**Chris Gammell:** Is it the, is it the test pad police, Dave?

**Dave Jones:** I don't know. It almost came from that laptop box that I sealed that laptop in. I swear. Like I'm still, that's where it sounded like it came from. What the heck?

**Chris Gammell:** Yeah. Yeah. I mean, maybe it's Microsoft calling. Hello, this is Bill Gates. I have a, I have a repair for your charger.

**Dave Jones:** This lab's haunted. Yeah. Yeah. I guess so. Anyway, sorry. Time to move. Time to move. No, no worries. No worries.

**Chris Gammell:** I think I'm just living, I'm living the, you know, you could say it a thousand times, you know, like put good test pads on board, you know, keep them well spaced, keep them like sane. And, you know, until you really screw yourself over and have to deal with it, you'll never, you'll never learn that until you really mess it up yourself. You know what I mean?

**Dave Jones:** Good work.

**Chris Gammell:** I'm sure, I'm sure you've never done this, right? You've never learned this. Oh, no, no. Totally not. No, no, no, no. Pogo pins, the tiniest pogo pins you can possibly get.

**Dave Jones:** And there's no more material left in the test jig to put the pogo pin through. Yeah, exactly. So they're practically touching, you know, it's like. Yeah, exactly. That is exactly right. Yeah. Yeah.

**Chris Gammell:** It's like precision drilling.

**Dave Jones:** So you end up doing them at an angle. Sorry, I've never done that. Yeah. Right. Of course. So you end up like.

**Chris Gammell:** Yeah. Right. Yeah.

**Dave Jones:** Oh God.

**Chris Gammell:** Yeah. It's like an acupuncture. You need like acupuncture needles to get this sort of thing going.

**Dave Jones:** Oh God.

**Chris Gammell:** I did manage to, you know, it's probably not as bad as I'm sure you've had to do in terms of the size of the pads or not like the smallest, but I did manage to get a 3D print working with lots of hot glue and lots of.

**Dave Jones:** Right. Nice.

**Chris Gammell:** Lots of poking and prodding. I did get it to go. But yeah, I just feel like it's like one of those things where like, you know, no matter how many times we say it on here, it's not. People won't learn it until they learn it the hard way. Right.

**Dave Jones:** Right. Got it. Yeah. Yeah. Speaking of acupuncture needles, I stabbed myself with my soldering iron tip. It was not on at the time, but I was like, you know, I've got like the, like a holder on top of my soldering iron case that holds all the extra tips. Right. You know? Okay. So I got these new tips. Like I, I, I got an extra smaller, um, uh, like a handle so that could take smaller tips, you know, for like really micro fine stuff because I didn't really have anything that small. So I thought, Oh yeah, I should probably get, you know, an extra, um, you know, handle. And these are tips, not cartridges.

**Chris Gammell:** Is that right?

**Dave Jones:** These are, no, these are the cartridge. These are the JBC. So the smaller JBC. So it actually plugs into my, so it's like the fine. Yeah. Like the fine. Yeah. Yeah. Just a smaller. It's, it's, it's not their smallest one. It's not their like nano one, but it's smaller than the one I had. So it takes these, anyway, it takes these little, you know, much smaller tips so you can get into finer areas, you know? And, um, so anyway, I bought some of these brand new tips and they're really super fine. And of course they're like, they're tiny, sharp, you know, they raised their needle sharp conical tips, right. To get into the finest location. So I was reaching over the soldering iron thing and I accidentally stabbed, accidentally put my hand on top of these tips. And I swear.

**Chris Gammell:** Oh, like not the ones that were off, like just the stored ones. Yeah. Yeah.

**Dave Jones:** Just the ones sitting there. And I think it went like almost through to the bone and I like, I had this soldering iron cartridge hanging off my hand. It was embedded into my finger.

**Chris Gammell:** Oh man.

**Dave Jones:** It was like, oh my God. Damn, they're sharp. Yeah. Bloody. Oh, unbelievable.

**Chris Gammell:** You know, lead's good for you, right? Yeah. Yeah. Lead injection once in a while.

**Speaker ?:** It's fine.

**Dave Jones:** But damn. Yes. Yeah. These might, yeah, they're needle fine. These points. I couldn't believe how they, you know, they could like just totally penetrate and just hang there. Like, oh, I was actually going to take a photo of the cartridge hanging off my finger, but it was hurting too much. Yeah. Right, right, right. So I just pulled it straight out. Your new piercing? Yeah.

**Chris Gammell:** You ever buy the, like the really fancy JBC, like the tweezer ones? I never pulled the trigger on that myself.

**Dave Jones:** Oh, okay. Yeah, I think they were going to send me like, no, that was Pace were going to send me a tweezer one. But JBC make this like nano solder and iron. So it's like even smaller than this smaller one I had. They're insane. They're for doing like, you know, 005, 005 packages or something, you know, like smaller than 0201, like smaller than, you know, 0105. Oh, what is it? 01005 or something? That's right. One of the smallest or something, you know? Yeah. And they might even be smaller than that these days. But yeah. So they're actually designed for that. And they're just, oh my God, they're so insanely small. It's just, it's just nuts. Gorgeous. They're absolutely gorgeous. I want one. But, you know, so I, I didn't go that extreme. I just went.

**Chris Gammell:** Yeah. I didn't know. I know you were there. These are the small ones. I'm just saying like, have you ever done the, the, the JBC style tweezers? Like the.

**Dave Jones:** Oh, no. No, I've just got these cheaping. No, I've got a cheapy wireless battery recharger. Sorry. No, I, I plugs in via external USB. So I've got an external USB powered tweezer thing. And it's like, you know, it's okay. But no, I would like to get one of the JBC ones or one of the. Yeah.

**Chris Gammell:** I mean, the hand, I have, you know, I have the knockoff of JBC, whatever it's called. The.

**Dave Jones:** Oh, I get it.

**Chris Gammell:** Thermaltronics. Knockoff. It's like, you know, people that used to work there, they have lower cost. Yep. Manufacturing. They're very nice. The nice cartridges and stuff too.

**Dave Jones:** That's the Australian company. Is it? You sure? Thermaltronics? No, I didn't think so. Thermaltronics, I think, is a different one.

**Chris Gammell:** Yeah. Okay. Yeah. It's like 250 for like the handle, just for the tweezers. And then like. Yeah. Mine was like. Yeah. 40 per cartridge. And you have to buy two. So. Yep. Yeah. If it was like, you know, if I was like Lewis or something like that, it'd be like, okay, maybe, but. Yeah. I'm not, not anything close.

**Dave Jones:** I didn't buy the genuine tips. I just got, you know, eBay tips. Cause you know, the, basically the, the amount of work I'm going to do with that ultra fine iron is nothing. Right. I just need to have it there on hand if I need to do, you know, something fine. So. Yeah. Didn't really justify, you know, the expense of having all genuine stuff, but I did buy the genuine, uh, JBC handle though, which goes into my existing iron. So it, it isn't like I can have both run at once. I've got to disconnect it. I see. Yeah. Yeah.

**Chris Gammell:** It makes sense. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I think if we, yeah, if we were repair tax, it'd be a little different.

**Dave Jones:** Oh no. If you're doing it every day, it's a different story. Yeah. It's the same with everything.

**Chris Gammell:** Yeah. Of course.

**Dave Jones:** In the lab. If you do it every day, you have dedicated tools, dedicated bench arrangements, dedicated everything, right. Dedicated consumables there. Like, you know, just everything just set up perfectly. If you're doing it every day. Thing is, I don't do it every day. And that's, you know, and that shows in my videos, people go, Oh, why didn't you use a smaller iron to do this repair? It's like, Oh, because I don't do this for a living. Like, you know, it's like, God, I'm, I'm not fixing, you know, phones every day. You know?

**Chris Gammell:** Yeah. Some of the repair channels. There was one that my friend sent me.

**Dave Jones:** Oh yeah.

**Chris Gammell:** It was just like wild. I mean, yeah, there's so much, so many out there now.

**Dave Jones:** Yeah. They're really good. So amazing.

**Chris Gammell:** And they were using these like sponge, like, uh, like foam sponges for like sopping up flux and stuff like that.

**Dave Jones:** I never seen them before. Yeah. Yeah. Yeah. They're using, yeah. They use little wipes to, yeah. Yep. And they have everything on hand. I saw like a subscribe to a, I don't know, fix. I think it's, yeah. Um, YouTube channel and like, he's, he's really good. I'm not sure if he's new, but like he's, and he's like doing, um, entire reviews of, you know, 10 different types of solder flux and 10 different types of solder wick and, you know, really fantastic in depth comparisons of all this, because that's his job, you know, is to fix laptops and phones and things. Yeah, exactly. So, oh yeah.

**Chris Gammell:** Flux battles.

**Dave Jones:** We'll see if I can pull up the chat. Yeah.

**Chris Gammell:** I just found nanofix. It's great. I don't know if this is the same one. No, this is Canadian guy. Yeah.

**Dave Jones:** I'm not sure where he's from, but yeah, he's just like comparing. Oh no, it's the same guy. Yeah. No, this is the exact same guy.

**Chris Gammell:** This is, yeah. I was, cause I was like, ah, this looks familiar. Wife learns reballing. So he taught his wife like reballing BGAs and stuff.

**Dave Jones:** I saw the one where his wife, he taught his wife to do some reballing. Yeah, that's a great channel. Yeah, this guy's great. Yeah, it's great. Give him a sub. Hey, oh no, he's got 111,000. Oh no, that's views. Yeah, no, it's like 17,000. Yeah. Let's get that number up here, folks. Come on. Yeah, get it up there. Oh yes, it's based in Canada. All right. Yeah. Yeah, cool. You know, and there's all these dedicated channels like this. Yeah, exactly. That do it way better than I ever could. You know, it's like, yeah, I don't, I don't do this. They're like, geez, I'm barely sold once a week if I'm lucky, you know? And even then I'm just doing a single joint or something, you know? It's not like I'm, God.

**Chris Gammell:** Yeah, so don't come asking us for our tips, folks. Come on. Go find the experts. They all have YouTube channels now.

**Dave Jones:** Yep.

**Chris Gammell:** Dave and I are obsolete. That's what I'm trying to say. Why are they still here, Dave? Why are they still here?

**Dave Jones:** See, that's the thing. People think I'm an expert and you're only an expert if you do it every day. They're the experts, the ones who fix laptop. You know, people do, well, why don't you fix this laptop, Dave? It's because, well, I've got no schematics. I've got no history in, like, how the hell am I supposed to do this? But somebody fixed laptops every day. They've got the skills. They've got the, they've got all the information because they're tied into the networks of getting these schematics from God knows where. And they're, you know, they've got the board view program that allows them to cross probe from the schematic to the thing. And, you know, like, and they've just got it down and they've done it a hundred times, a thousand times. Yeah. And, you know, it makes them an expert. Yes. I'm, you know, well-known in the industry for doing stuff, but, you know, I don't do it every day. It's not my day job. So, you know.

**Chris Gammell:** That's right. You need a video of me, though. Dave's got it.

**Dave Jones:** Right. Man. Anyway, even though my soldering tutorials are incredibly popular. I think Adam Savage said he learned to solder from one of my videos.

**Chris Gammell:** Really? That's pretty cool.

**Dave Jones:** Yeah. Yeah. I think he did say that once. So, yeah.

**Chris Gammell:** I'm sure he's listening now.

**Dave Jones:** Right. Oh, yeah. Totally.

**Chris Gammell:** Yeah.

**Dave Jones:** He's a great channel. Do you watch it?

**Chris Gammell:** Hi, Adam.

**Speaker ?:** Which one?

**Chris Gammell:** Which channel?

**Speaker ?:** Which channel?

**Chris Gammell:** He's such a great channel.

**Dave Jones:** I love the testing channel. Oh, my God.

**Chris Gammell:** Oh, yeah? Still? I have not been, I'm not watching. Oh, you haven't been following?

**Dave Jones:** Oh, no. He does all the prop things and he goes to the space. Oh, yeah. He goes to the museums and, oh, my God. It's just, it's so addictive. Huh? Oh, God. It's such good content. I'll have to give it a look.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yep. Adam Savage has tested. It's basically just him now. And it's him in his shop and he does builds and, oh, my God. It's just, it's incredible. So, anyway. Yep. Yep. That is one of my favorite channels. I spend time watching.

**Chris Gammell:** Yeah. Nice. Nice, nice.

**Dave Jones:** Oh, can we talk about, yeah, like right at the start of the show, we were talking about, no, no. Anyway, I did this review of this multimeter. Have you seen it? The A&M 626. I did see this, yes.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** Oh, my God. What do you think about, like, the look and the feel of this thing? It's like just the weirdest. It's something.

**Chris Gammell:** Yeah.

**Dave Jones:** It's something. Yeah, right. That's what I thought. Yeah, it's something. Yeah.

**Chris Gammell:** I think this is the one you mentioned on the show last time we spoke, right? Oh, is it? Okay. Right. The wearable?

**Dave Jones:** Yeah, it could have been, but I actually ordered one. I feel dirty now that I actually ordered one. But, you know, everyone was, like, you know, going, this is so interesting. Like, either this is the dumbest thing ever or, oh, I think it's all right. You know? Yeah. And, no, it's just, it's dumb. Even if you love the form factor, it's a poor implementation. Yeah. So, yeah.

**Chris Gammell:** No, this is different. Sorry, we were talking about the wrist-worn one. This is not the wrist-worn.

**Dave Jones:** Oh, the wrist one. Right. Oh, I've ordered a wrist one. It's in the mail. It might even turn up today. I ordered a wrist, like, it's, like, $10 on AliExpress or something, and it's got, like, fixed leads, and it's going to be so bad. Yeah, that's going to get one. But I just, it's morbid fascination. I had to order one. Yeah, yeah, yeah. So, yes, I've got this wrist-mounted multimeter coming. Oh, my God. It's even worse than this thing. And it's, like, I would like to know, because this was talked about on, this was extensively talked about on the forum. I'd love to know what is the minimum viable build number for something like this? Like, someone at A&N comes up, oh, look, I've got this great new design. Look, it looks like some space, yeah, the company, right? You know, right? They come up with this concept of this model. How many of these do we have to sell to make it viable? Because they're churning out so many, infinite number of these multimeter designs. What's the, how many do they have to sell to make the entire project viable? I would love to know that number.

**Chris Gammell:** That is an interesting number. It's got, it's lower than I bet we would, it's lower than it would be in the US for sure.

**Dave Jones:** I would guess a couple of thousand, because I actually have experience in this. My 121 GW multimeter, when we were developing that with that cane, I said, well, how many would you, you know, when we first started talking about it, I think I talked about this in one of my videos once. How do we, you know, like I asked them, well, like they, they originally said, oh, we'd love to design a multimeter for you. You know, we can definitely do this. Great. And I went, well, how many do I need to sell to make this thing viable? And they said, oh, you know, three, 4,000, something like that. And I said, I can probably do that, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And like, yeah, I'm, I'm not sure if they were lying just to get the business or, you know, or what. I don't know. Cause they're like not a fly by night, Chinese, Chinese company. This is an American company who dealt with a Taiwanese company. And there were a lot of people involved and, you know, um, but yeah, yeah.

**Chris Gammell:** I think it's a lot lower than that. I think sub 1,000 for, I think hundreds.

**Dave Jones:** You think sub 1,000 for this thing? Yeah, I think. They're that. I think. They can churn out all the molds and every, you know, you've got to do all the custom molds. Well, I think that's the real thing.

**Chris Gammell:** This thing looks like, whenever you see a weird thing like this, I think this has got to be like, oh, this is actually like a tape measure. And they just closed up part of the mold.

**Dave Jones:** And they're reusing the tooling, you think? Yeah. Oh, I think so.

**Chris Gammell:** I think it would be really interesting to put this in like a Google image search.

**Dave Jones:** I don't think so. It looks similar form factor, but I, it's entirely custom tooling, I'm sure of it.

**Speaker ?:** Yeah.

**Dave Jones:** Because it's got the tilt-in bail on the back. It's got the probes molded in the side.

**Chris Gammell:** Like you can, you can like, you can modify molds, right?

**Dave Jones:** Oh, you can modify molds, but then you ruin the mold for that. Like just think about it.

**Chris Gammell:** You do putting gates, you know, and especially if they had it as like this kind of generic case, you know, unique looking, but it really does look like a, it looks like a tape measure.

**Dave Jones:** You know, can you machine, can you cheaply machine a mold if you know that you're only going to use it and make a couple of thousand of these? You, you, you, you wouldn't do a proper professional tooling mold that, that is designed for like, you know, a hundred thousand or a million units.

**Chris Gammell:** Or like you go to, you go to a marketplace and you buy, you know, a good, but not great mold. That's, you know, that somebody cast off. Cause they're like, well, we can't do it. It doesn't meet our specs anymore. But maybe you could use this and you could, you know, weld on a new gate for it. Right. And then, and then, you know, add your own stickers and that sort of thing. Like, I feel like that is very reasonable as a reuse kind of thing, you know, like.

**Dave Jones:** Yep. So I think I, but I think you just 3d print the tool. Like you just mill the tool now, wouldn't you? You just get one of those five axes machines and you can churn out a mold and like a steel mold for hundreds of bucks.

**Chris Gammell:** Like you do a soft, you can do a soft metal mold, but you could, you could do that.

**Dave Jones:** That's what I'm talking about. Yeah. Like a alloy mold or something like that. It doesn't have to be like.

**Chris Gammell:** But I just think like, I just think it's more likely that it's, it's going to look like the other thing, you know?

**Dave Jones:** Okay. I think. I could be wrong. If anyone has specific, you know, experience with that in the, in, in Asia, I'm sure it's different in Western countries. I think that's right. The value proposition is different here than it would be in China, I'm sure.

**Chris Gammell:** Yeah. Cause they've got just so much capability. Okay. Here we go. Look at this. I just put this image. I just took a screenshot and I put it into Google image search and I'm finding tape measures. Look at this. I can send you a tape measure from Amazon. Oh really?

**Dave Jones:** Send me a Google image link.

**Speaker ?:** Yeah.

**Chris Gammell:** Let me just send you the actual link to Amazon. Like that's what I'm saying. Like, it just feels like, you know, like it's like a, looks like kind of the same. Yeah. Where's my link? I'll just send you stuff.

**Dave Jones:** It is much bigger than a tape measure though. Okay.

**Chris Gammell:** Well, I don't have a good feel just from here. Yeah.

**Dave Jones:** Right. Yeah. I actually ordered, I was going to do this video. I haven't done it yet. Oh, right. Yeah. Okay. Right. Yeah.

**Dave Jones:** Right.

**Dave Jones:** I see where you're coming. Right. Right.

**Chris Gammell:** Okay. How about this one? Let me just share a screen. Cause I can just share a screen with you. Yeah. I think it's just like, it's just more likely. It's like Occam's razor in this case. It's just like the more likely outcome because it's lower effort to me. Yeah. I don't know.

**Dave Jones:** I don't know. Yeah. Anyway, either way. Yeah. I, I suspect it's like a thousand or two tops. Yeah. I think that's right. They have to sell off this thing and you know, they just, oh yeah. Yeah. I can see a screencast now.

**Chris Gammell:** Yeah. Like look at this thing.

**Dave Jones:** Oh, it could be like an ultrasonic tape measure or something. Yeah. Yeah. Yeah.

**Chris Gammell:** Exactly. Unity. Unity. Unity. This is a laser transmitting slash receiving.

**Dave Jones:** Unity make laser tape measures.

**Chris Gammell:** Yeah. Ruler tape. Apparently. What? I don't know. I don't know any of these things. I'm just, I'm just clicking.

**Dave Jones:** This is the test equipment company. Unity.

**Speaker ?:** Yeah.

**Chris Gammell:** I'll send you other links. That's on Tmoo.

**Dave Jones:** That's just.

**Chris Gammell:** How about this one? That looks just like it. You know, like just got the lasers coming out of every side.

**Dave Jones:** I still, yeah. I still think they just have a cheap way of making molds cheaply.

**Chris Gammell:** I think they just. It could be too. It could be. Yeah. You're right. You're right. I just. Anyway. You're thinking about like white label services and stuff like that. Obviously this is. Yeah. This is the one you, you link to. I'm showing Dave the same thing. Yeah. Yeah. Sorry. Dave Jones on X. And then they go. What new fresh. Oh, me. Me on X. Okay. There you are. Yeah. Yeah. There you go. You've been indexed. Excellent.

**Dave Jones:** Oh, that's great. All right. Yeah. That's. That's interesting indeed. But yeah. I, I said. It could be as low as 500. You know. Sure. Yeah. Who knows? Like, geez. It's just. Yeah. It's crazy. It's crazy.

**Chris Gammell:** It is.

**Dave Jones:** Whereas we, us poor Western designers, wouldn't even dream of doing custom tooling like this for 500 or a thousand units. You know?

**Chris Gammell:** No.

**Dave Jones:** It's like.

**Chris Gammell:** I mean, some of it I just can't get my head around.

**Chris Gammell:** I wouldn't. I think like the, I think I mentioned it on the show last time we spoke, but like this board I've been designing around, the Pro Micro Form Factor board with like a 52 840 end. Like literally I can't, I can't get that chip for less than $3 and this was $3 shipped to my house. So like. Right. Something. Yeah. Wonky in there. Right. Yeah. Something. Something has broken down somewhere in that, in that chain and it's fine. I'm, I'm benefiting from it. Like at a certain point it's like, shut up, Chris, just use it. You know? Like that's fine.

**Dave Jones:** Speaking of which projects, um, update on my, um, a timer project. My little.

**Dave Jones:** I saw your new screen. Yeah. I saw your new screen. It's like a shot. It's like the sharp ones. Those sharp memory LCDs, which are stupidly low power, but they're, but the sharp ones are so expensive. They're just crazy expensive and they don't make them in the right form factor. But I found it. Well, someone on the forum found this company that manufactured this great little LCD.

**Chris Gammell:** I went and looked at, when I watched the video, the goo display, uh, that's also who I bought. Goo display. Yes. You know, I've done e-paper stuff before for a display. Right. Yes. For Goliath. Yeah.

**Dave Jones:** They mostly sell the e-paper. Yeah.

**Chris Gammell:** I bought, I bought from goo display as well. And that's the one where I was saying that I, it was like a, it was a cast off, you know, who knows from where, but it's through goo display.

**Dave Jones:** For those searching, it is not actually goo display. It's actually good display, but their logo puts the D inside the D and you can't see it. So it ends up looking like goo display. Yeah. But the actual website, if you want to go to it, is good. That's right. Dash display or something. Right. Something like that. Yeah. Anyway, um, very cool. But now I'm thinking, right. And cause this is higher resolution. This is like 360 by, and then you get to the point, the interest of like, you think, Oh, that's great. Right. I get all that extra. What am I going to do with all those extra pixels?

**Chris Gammell:** 80 extra pixels. What do I do? Yes.

**Dave Jones:** You get all those extra results. You think you get those for free, but you don't. You pay a penalty in terms of data rate and processing.

**Chris Gammell:** Of course.

**Dave Jones:** So you've got like, it's, it's like requires, I don't know how much memory. I haven't run the numbers off the top of my head, but you know, it requires all the memory to store that. And then you've got to transmit it over the SPI bus. And then if you want to update the screen. So your processor, which I wanted like a slow, low power processor, I can't do a slow, low power processor anymore because the data rates are updating these bloody LCDs so much, you know?

**Chris Gammell:** Right. Right. You got to like chunk all the bits over.

**Dave Jones:** You know, there's tricks you can do to update only a small part of the screen and stuff like that. You know, you send only the data that changes and stuff, you know? Right. Yeah. Yeah.

**Chris Gammell:** I was actually surprised on your video. You said that e-paper can't be updated quickly, but there is, there are some methods for updating e-paper.

**Dave Jones:** There are some. Yes. Yes. A lot of the e-paper displays. But you'll get ghosting and all this stuff. Yes. Yeah. They do actually have internal, a lot of them have internal circuitry that allows them to only update like a small window part of the display at a time. So you can extend the life there, but you know, I was being a bit generic there.

**Chris Gammell:** Sure.

**Dave Jones:** Yeah. So there are ways, but the point was, is that the e-paper e-ink displays have a finite lifetime. You can't. Yeah. So, you know.

**Chris Gammell:** Yeah. And they're expensive as hell. They're so, I mean, like, I think cost is the main thing. No, they're not. Oh. Okay.

**Dave Jones:** They're pretty cheap. Okay. The ones that I used are very expensive. Oh, really? Okay. Yeah. Right.

**Chris Gammell:** Six bucks for like a 200 by 200, you know, like, it's like a 40, 40 millimeter by 40 millimeter screen. It's not big.

**Dave Jones:** Oh, okay. Yeah. But six bucks isn't, it depends on what you're doing, but six bucks isn't, like it isn't 60.

**Chris Gammell:** It's such a, oh, sure, sure, sure, sure. Yeah. Yeah. More than I thought it would be. I guess I don't have a good fit in my head for what it should be for display. Yeah. I can buy it. Anyway, so. I could, that's like, that's like three circuit boards, five circuit boards worth of microcontrollers for me, you know? Right. Oh, yeah. Right.

**Dave Jones:** So now I'm actually thinking, oh God, what process? Like, cause the demo board for this came with an ESP 32 and I'm going, oh, should I?

**Chris Gammell:** With the antenna right in the middle of the board. Yeah.

**Dave Jones:** Should I add the Bluetooth? Should I add, like, you know, should I add the wifi? You know, should I actually design this project so it has wifi, bluetooth capability to make it more flexible? And it's like, you can turn the power off, like you can turn the power off to the wifi and the Bluetooth if you're not using them, I guess, to save power, but it's still way more higher power than like just a dedicated little micro that just doesn't have any of that crap, you know?

**Chris Gammell:** I mean, for you, I would say make it the easiest to program.

**Dave Jones:** Yes. Well, if I've already got the example code for the ESP 32, I might just stick with the ESP 32. Yeah. Like, you know. That's right. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** I think that, and then also, you know, if you are going to sell it, make it extensible for the audience too.

**Dave Jones:** Exactly. I want to make it hackable. I think people will be quite disappointed. It would limit the market if it was just a fixed timer, but if it was a generic wifi, Bluetooth, battery powered display, then that'd be kind of cool, you know? Yeah. So, yeah.

**Chris Gammell:** I think that's, that's probably the right move.

**Speaker ?:** Yeah.

**Chris Gammell:** So I might. But you should move the antenna out to the outside of the board. That design.

**Dave Jones:** Well, I'm going to be.

**Chris Gammell:** Maybe cry a little bit on the inside. I realized they were not actually doing it, but they. Yeah.

**Dave Jones:** So ESP 32 is still the thing?

**Chris Gammell:** Personally. Well, there's a wide range these days. Oh, yes. Yes.

**Chris Gammell:** Yes. Yes.

**Chris Gammell:** product line is nuts like the p4 is like it's like a supercomputer it's insane yeah well i don't want that i i want the lowest power minimal viable got it i like personally i like the c3 i think that's so it's a risk 5 part uh that means they're paying less for licensing and so it's just lower cost overall so it's like a two dollar two dollar module it has wi-fi that's acceptable yeah it's you can get it in the mini form does it have wi-fi it's wi-fi and bluetooth um because some of the ones i think the c6 does not have bluetooth it's wi-fi only it's like they're lower it's a cost down version also all the c's i believe are risk 5 okay i'm not sure i might have a c4 i'm not sure what's

**Dave Jones:** on the demo board i i haven't looked at all the offerings all i've got a i thought your demo board

**Chris Gammell:** was just a plain old esp32 which is the extensa you know 180 dual core uh 180 megahertz like i don't

**Dave Jones:** i haven't looked i haven't looked that far so yeah yeah i mean that's gonna be the standard oh god they've got the esp32 p the s the c the h just the regular esp32 which is probably and then

**Chris Gammell:** they've got the 8266 what the hell don't yeah so the s is going to have like uh usb on it so if you need us if you need like to talk over usb well otherwise you can just usb to serial i've got i'm

**Dave Jones:** probably going to have usb rechargeable battery in it you don't that's fine so whether or not i connect the usb lines over i don't see the point well here's the thing you you would still have it

**Chris Gammell:** programmable this is like uh usb host effectively so if you needed the if you needed the timer to be able to talk to the computer and send data back over that link then that would be right okay gotcha right gotcha yeah most things so like the the esp32 and all the lines almost universally programmable over serial they have a boot bootloader and a serial bootloader and so like okay you just put

**Dave Jones:** a cheapo chip on there and that would be nice if it was if you if people could reprogram it over the usb that would be yeah nicer than having what and how's the regular esp32 which just goes out to header does it or something how does that no no most of them almost all of them also have um you know

**Chris Gammell:** you us cheap usb to serial sort of thing oh okay right and there's like the standard circuit with like if you look at your board q1 and q2 are just like bjts that are like kind of cross-wired that's like a standard circuit you'll see on almost every expressive design and that's like the that's like the boot indicator effectively so it like holds down the boot and then it resets and then it that's puts it into bootloader mode and so right yeah that's you could just copy that part of you know like you could copy any esp32 c3 um yep my my demo board's actually running arduino on this

**Dave Jones:** yeah i believe it yep yep yeah so should i stick with arduino on the esp32 or is that too kitty

**Chris Gammell:** i think it's kitty i think it's like if you you know if you're trying to optimize power eventually i think you're going to want to go into esp idf or other you know ecosystems that are you know tied

**Dave Jones:** into there but arduino means it's super easy for everyone sure sure sure but if you're publishing

**Chris Gammell:** you know so you so like i think here's here's the platforms i think you could probably put on there without too much stripe you could do arduino you could do circuit pipe you can do micropython rather you could do rust if you're nuts and you want to bring in that crowd sorry rust rust stations uh you could do zephyr you could do espaf i mean like and a lot of these are ecosystems a lot of them are artos as well you can do bare metal uh so you know like there's a lot of things targeting these

**Dave Jones:** and and that's just the the the hardware is all the same though right so it makes no difference so if so if i released mine using the arduino code that i've already got then people could just fork that and go oh no i'm gonna do it like a real man and i'm gonna you know do it in rust or something

**Chris Gammell:** you know sure yep yeah so just try and try and stop them basically yeah at a certain point you're gonna be basically building like a you know an esp32 an extensible esp32 display setup yes you want it for a timer but someone might say yeah i just might want it as uh yeah somebody else

**Dave Jones:** might want it as a to display network time on their computer or something or they might want to play games on it or they might want to i don't know right right yeah right yeah all right so yeah i think

**Chris Gammell:** okay i think that's a decent idea i um you know especially if you don't have like strong feelings

**Dave Jones:** otherwise um i don't have strong feelings what whatever works and which is there which is the easiest cost cost is a bit of a factor power is a factor but yeah i mean what is your general target for costs like overall i if it's a couple of bucks if it's more than a cup if it costs more sorry the system cost system oh i don't know i don't know got it got it i don't know but there's not much on it there's basically the display the processor a couple of miscellaneous chips and parts a battery holder and and a case you know and some buttons i mean it's not right yeah the other thing that's

**Chris Gammell:** nice is like if you you know you'll have a case you'll have the one that you design but right at a certain point if it's just like a two millimeter jst ph you know plug right to you know plug into the various lipo pouch packs that are out there it's like well someone wants to get it to you know last

**Dave Jones:** no i'm thinking of an 18650 straight on the board oh so you literally plug an 18650 into a battery holder on the board so you can change it yeah then power via external usb yeah and charge it via external usb yeah so charge it on board okay because the battery meets the form factor requirements so the battery kind of like tucks in behind the angled display kind of thing and it's almost the perfect width you know so it kind of makes sense yeah yeah yeah that's good yeah yeah i've used

**Chris Gammell:** those like those some square lipo those holders stuff like that yeah yeah and then tape it down

**Dave Jones:** and you know all that sort of i don't know anyway so yeah anyway my next video will probably be me playing around with the arduino code and getting got it just talking and compiling and you know stuff

**Chris Gammell:** like that so yeah you could look at um i guess i don't know how much it's going to be like updating the screen and stuff like that like in a true like power down mode you could really you could turn everything off i mean you could oh yeah kevin dara as uh he's another youtuber and he's got

**Dave Jones:** up every second to display the clock it just powers up on a interrupt right you can just do a background interrupt it sleeps and then you interrupt every once per second you dump the data over to the memory and shut down over to the display and shut down again anyway it's fun project i gotta get into that so yeah it gives me something to work on anyway with the very little time i have available at the moment

**Chris Gammell:** crazy anyway we are well over time yeah you should uh you should go do some work i should probably go

**Dave Jones:** to sleep uh it's late here so no yes i'm that opposite side of the planet thing yeah that's right

**Chris Gammell:** that's right all right man well good catching up and uh we'll chat soon catch you next time

**Dave Jones:** you
