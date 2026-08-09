---
episode: 286
title: An Interview with Saar Drimer
url: https://theamphour.com/286-an-interview-with-saar-drimer/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded February 10th, 2016. Episode 286. An interview with Sar Drimmer of Boltport.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Sar Drimmer from Boltport.

**Dave Jones:** Hey, Sar, thanks for joining us.

**Saar Drimer:** Thanks for having me.

**Dave Jones:** All the way from sunny London.

**Saar Drimer:** Yeah. Yes, yes, pretty windy.

**Dave Jones:** Thank you for coming on because we don't have many people from the old DART, as it's called here, because of the time zone, you know, three different time zones across the planet. That's just crazy. So what time is it there? 11 p.m. or something?

**Saar Drimer:** Yeah, it's half past 11. Right. These hours are not strange to me. Yes. Fellow nerd, yes. Yes, of course. Nate Owls. It takes me – I'm not a morning person. Let's just say that. Right. And then, you know, I really get into gear later in the day. And so I'm rarely asleep at this time.

**Chris Gammell:** Well, let's hope you don't fall asleep during the show, too. That would be good. Yeah, well. Just keep it. It's paying no one to happen. Same goes to the audience. Same goes to the audience.

**Saar Drimer:** So the duty is on us to make it interesting, yes.

**Chris Gammell:** Every week, man. Every week. So some people might know you from some of your stuff, but why don't you tell us a little bit about Boldport and what you're all about?

**Saar Drimer:** Okay. So I'll start just my background. I'm an electrical engineer, computer engineer. I worked for Xilinx. Yes.

**Dave Jones:** Worked for Xilinx, yep.

**Saar Drimer:** I worked for Xilinx for a few years in California, and then I came to – Do it. Do it. We need to know. I was – yeah. I was part of the Vertex IC design group in a sort of subgroup that was the verification and characterization of new silicon.

**Dave Jones:** Sorry for asking questions along the way to interrupt the story, but if I don't do it now, then I, you know, we'll probably won't get back to it or I'll forget. So what size design group does it take to design – like the Vertex, is it the highest end part? I think it's close to.

**Saar Drimer:** The Vertex? Yeah, it was. I mean, this was 2000 and – I was there from 2002 to 2005. Right. I don't remember the group size. I mean, we were tasked with that. But is it hundreds of people? Is it – I think so, yeah.

**Dave Jones:** Dozens of people? Right? Hundreds?

**Saar Drimer:** Yeah. I mean – Big. Like I said, I was – Big. Yeah. I was part of the – of a small group that were getting the silicon when it came back and made sure that everything works. And how do you do that? So it's very interesting.

**Dave Jones:** How do you – do you whack it in a big BGA ZIF socket and character – yeah? And characterize the thing? Yeah. Yeah. With what sort of tools? We need to know all the gory details. This is exciting stuff.

**Saar Drimer:** It's – well, there are boards that are being made, you know, to prepare and you put it in a ZIF – Test board. In test board. Very expensive sockets, I remember.

**Dave Jones:** Oh, yes. Yes.

**Chris Gammell:** And ZIF is zero insertion force, right? Force for those who don't know, yeah.

**Dave Jones:** And to get one with a thousand pins on it is – Yeah. Or BGA's and all that.

**Chris Gammell:** Yeah. Yeah. That's crazy. Yeah. Machining.

**Saar Drimer:** And a lot of high-end equipment take measurements. So I've done a few interesting experiments and I had a good time there, but at some point I decided to move – I kind of wanted to go back to academia. And so I ended up in Cambridge in the UK to get a PhD in security. I was very interested in security at the time. And part of the interest was hardware and security. I felt at the time that it was a topic that would be interesting to look into. So I joined the security research group in Cambridge.

**Dave Jones:** Hardware security research group, I'm assuming?

**Saar Drimer:** No.

**Dave Jones:** Or are they interchangeable, software and hardware?

**Saar Drimer:** So the group – it was part of the computer lab, which is the computer science department in Cambridge. Interestingly, it came out of the mathematical laboratory, so it was called the computer laboratory. And so it's a computer science department, but – and there is also an engineering department. But there, there's a – the security group does a lot of different things, software, privacy, online. And part of it is hardware security. There's some very good people there. So I started working on FPGA security, security of how do you securely use field programmable gate arrays that are volatile.

**Dave Jones:** And, well, how do you? Because they're external flashes, right, with the program memory.

**Saar Drimer:** Yeah. So one of the things I worked on was a protocol for securely updating firmware over insecure network. Got it. So if you have a – if you have a – if you have a piece of hardware, the user is – could be or should be considered a malicious entity, right? Right. Right. Because they're – it's in malicious hands. Right. Anything outside the lab is malicious hands. That's right. You know, they could do – they could do things intentionally or unintentionally to your thing, to your device. Right. So you –

**Chris Gammell:** Unintentionally malicious. That's like the longest path to saying an idiot I've ever heard of.

**Dave Jones:** There's a T-shirt slogan right there. Yeah. I'm unintentionally malicious. Right. Or I'm with the unintentionally malicious guy with an arrow. So, yeah.

**Saar Drimer:** There's a saying that we say in the insecurities, don't attribute to malice what you could attribute to stupidity. Stupidity. Right. Yeah. That's a good phrase. So, yeah. I worked on that. How do you, in a reasonable, practical manner, able to update the firmware or the bitstream or gateway? It's different names for what goes on to the FPGA to program it. And what are the trade-offs?

**Dave Jones:** And the answer is? It's really like cutting to the chase on research.

**Chris Gammell:** It's not so much the four or five years you spent doing your PhD. It's what was the answer. Come on, man.

**Dave Jones:** I want to know the answer. And I hope it's 42.

**Saar Drimer:** The answer is exactly what it is always in security. And that is a trade-off. It depends. It depends. It's a trade-off. You can spend a lot of effort into protecting it. But sometimes it's not worth it because your product isn't worth that much. Right.

**Chris Gammell:** And your security is only as good as your unintentionally malicious users, right?

**Saar Drimer:** Or the technician or usually the human. Yeah. Usually the human is the – it's a part of the process that is least understood and that is very hard to take account of. But even the technical stuff, there's a lot of trade-offs, right? Do you, for example, pot it? Do you put it in – do you encase it in resin? Right. So in some cases, if you want – say you want to protect from this and that, one, two, three, you might need to pot it, right? But if you don't, say, for example, you say, well, it's actually locked in a room somewhere and we have a physical lock. So maybe we assume that nobody has physical access to it. Our potential attacker doesn't have physical access to it. Right. You know, things like that.

**Chris Gammell:** Mission Impossible, right? That was like that.

**Saar Drimer:** Yeah. Yeah. So that – and I've done quite a few things on banking security. Things like chip and pin has been here in the UK since 2003, I think.

**Dave Jones:** About the same for Australia. Yeah. We were an early adopter.

**Saar Drimer:** Yeah. So the UK has been as well. I think it's just getting into the US and Canada. I just got it. Yeah. That's right. And so they're using hardware. The thing is, it's interesting. You'd appreciate it, I think. You know, you go to security conferences and you write papers and stuff. And a lot of it is about software and online. And being someone who's very comfortable around hardware and can whip things around, you could do quite a lot. And people are really impressed by your skills, right? Because they –

**Dave Jones:** They go, what? You have to use your hands? That's it, right? Soldering. Exactly.

**Saar Drimer:** The soldering iron, I think, is a barrier, right? But it's so hot. And so I felt it feels a little bit like cheating because you can do a lot of things with hardware that it opens up a world, you know, to people who come up with theoretical attacks and so on. Okay. So I built a few pieces of hardware to circumvent some of the security mechanisms in chip and pin, the system, with my colleagues. And that worked out very nicely because we were – we published very nice papers that were appreciated and we were on TV a few times. And it was sort of this kind of side interest during my research. But it was a lot of fun. But I always had cash because, you know, those ATMs.

**Chris Gammell:** They spit it out at me.

**Saar Drimer:** So, yeah, there's – for example, we showed an attack where you could steal chip and pin card and actually not need to use the pin when you do a transaction because you fool the bank to thinking that it's a pin – it's a signature transaction which is still possible. Oh, wow. Okay. And you trick the point of sale that the pin that was entered was actually correct. So you sit in the middle. So I developed this kind of relay where there's a fake card going into the machine and then there was a PC in my back, a tiny laptop. It was connected to that and that did sort of a man-in-the-middle attack.

**Chris Gammell:** That's awesome.

**Saar Drimer:** By changing a few bits in between the bank and the terminal. And we showed it live and it worked. And later it was fixed. The banks fixed it. And there's also an attack we've done – this was already 2007. The relay attack where you connect a fake card. I need to remember. It's been a while. You connect a fake card into a terminal where you want to buy something.

**Chris Gammell:** Well, what is a relay attack even like theoretically? I don't even know. I've never heard that before.

**Saar Drimer:** So I'll restart the thing. So in 2007, we demonstrated a relay attack where you can do a transaction in one place, but it actually takes place somewhere across the world. Oh, wow. So you're able to transmit a transaction in one point of sale to another point of sale. So you're as if you're buying the owner. So you present a terminal, a point of sale terminal that is fake. You control it. And then you present it to a user, a shopper.

**Chris Gammell:** So basically you replaced a point of sale terminal. So if someone swipes their card into it and it's not a real thing, like a swiper.

**Saar Drimer:** They wouldn't swipe the card. This is a chip and pin. So they would insert it. They insert their own legitimate card and the terminal will say you're paying $5 for a book. And then that transaction is actually relayed to a real terminal to buy a diamond. And so they enter the pin. The pin is transmitted as well. Oh, I see.

**Chris Gammell:** So they authorize, but they don't authorize that amount at that vendor basically.

**Saar Drimer:** So the attacker at the jewelry shop, they have an earpiece and it tells them the pin. And then they enter the pin and the transaction is actually authorized on the person who buys the book. But they don't know that because they're seeing five pounds because the terminal is under your control.

**Chris Gammell:** Does the fake terminal have to send the info then also, like the chip info basically is transmitted to their laptop in the bag idea?

**Saar Drimer:** Yeah, so exactly. So the fake terminal is connected to a PC that then sends the transaction. That's the relay part, right? You relay that information to a PC on the backpack of the attacker. And that is connected to a fake card that is put into the real terminal. So the nice bit about this attack is that you don't have to do anything other than relay. You don't have to understand the transaction and you don't have to change anything. And what we found is that the latency that is allowed by the protocol, because remember, the card is expected to be inserted. It's a physical connection. But the latency is enough to transmit across the world. And then part of the work was to develop a defense against this, which is called distance bounding.

**Chris Gammell:** Ah, that's cool.

**Saar Drimer:** Yeah, you're trying to make sure that something is very close to you or as close as you can measure.

**Dave Jones:** It would stop it because they could be next door.

**Saar Drimer:** Right, yeah. It would stop if you're measuring the, say, if you assume a contact, right, like a chip and pin.

**Dave Jones:** Right, yeah, because even the fastest internet connection even next door is going to take X milliseconds, right?

**Saar Drimer:** Yeah, so, I mean, yeah, if somebody's next door, it's harder, right? But it won't be in a shop across town because you still have to do the transmission.

**Chris Gammell:** Can I ask a practical question here? Yeah, yeah. When you had the laptop in the bag and then you were using that to plug in the chip and pin fake card, was that a cabled card or was that Wi-Fi?

**Saar Drimer:** Yes.

**Chris Gammell:** So, isn't the actual security just to tell your shopkeepers not to let someone plug in a thing with a cord attached to it?

**Saar Drimer:** Ah, yes. But that's the beautiful part. And you don't realize that because you haven't used chip and pin so much is that they actually tell you. It's kind of against social norms to look while you're putting in the card and pin because you're not supposed to look at what people are entering, right?

**Chris Gammell:** Yeah, but, I mean, if you're attached to the card, I'm just saying.

**Saar Drimer:** No, so there's videos of it online and I basically melted the very thin wires onto the card and then I have long sleeves and it just goes and you can hide it under your thumb, right? So, it goes all the way. It goes in the back. Oh, I see.

**Chris Gammell:** I see because you're holding onto the card as it's authorizing. That's the idea? Exactly.

**Saar Drimer:** And then I put the pin and I even think and then the teller is not supposed to look. Right. Okay. So, practically, it's feasible.

**Chris Gammell:** So, I think the real question here is, you know, what kind of sweet stuff did you get? Don't tell me it was just a PhD because that's boring, man. Come on.

**Saar Drimer:** No, we were, you know, there's what's called responsible disclosure.

**Chris Gammell:** Yeah.

**Saar Drimer:** And, uh... Boo! Well...

**Chris Gammell:** You know what it should be called is free PS3, man. That's what it should be called.

**Saar Drimer:** Well, you know, I mean, we notify the banks ahead of publication and give them time to fix it. No, that's good. That's good. Um... A lot of the stuff that we've done was, um... Um... The live things were done with a film crew, uh... Right. From the BBC. So, it's, um... And everything is published. So, all, you know... Nice. Um...

**Chris Gammell:** So, we'll try and get, uh, links after this. Maybe we can put those in the show notes. Yeah.

**Saar Drimer:** Yeah, yeah, yeah. That'd be cool to see. I think the reward is this work helped people, um, uh, defend themselves against banks who accused them of, um... Yeah, right. Um... Uh... Of kind of first-person fraud, right? So, uh... Because chip and pin was seen... Was billed as, uh, something that can't be broken. Um... If somebody stole from your account, the banks would just tell you, um... You're lying. Yeah. Yeah. You were on the shop now, right? Because that's what they were telling us. You must have given... You must have given the pin to someone or it was your... Right. ...your daughter or your son or your nephew, whatever. And they won't get... They don't get the money back. And usually, it's people that are already not in a very good financial situation. Yeah. Because otherwise, the banks would treat them, uh, nicer. And so, um... And that's unfortunate. So, um... Our work has been... Has been used in... In... In...

**Saar Drimer:** In court cases, um... To show that there are problems with chip and pin. And... And... And even if you've been... You're compliant with... With the rules, um... Which kind of... Usually kind of unclear because you only get to know... You only get to realize a certain thing. I mean, some people have a problem remembering pins and using this thing. It's not... It's not, you know. So, um... And so, when they decided to fight the banks, the research came into, um... Into significance. And that... That's... I guess to answer your question, because it's something that you kind of get, uh, from... From doing... Helping, uh... That... That work had an immediate effect. So, that was... That was good.

**Chris Gammell:** Yeah. That's really nice.

**Saar Drimer:** Um... Yeah.

**Chris Gammell:** So... So, what about since then? I mean, so you've... So you've been... That... So that was... You graduated with PhD. So... What have you been doing since?

**Saar Drimer:** Right. That was end of 2009. Um... Then I was a postdoc doing some computer architecture work, um... At the computer lab. And more and more FPGA work. And... Then... Uh... I started Boldport. And that was... Uh... Around... Kind of mid... Late... 2010. And I don't know if you remember... Uh... The original idea was... Um... A... Um... The... What I started the company for was... Uh... To do an automated build management system for FPGAs. Uh... FPGA project. So... Uh... You... You'd have a web interface. It was called the Boldport Flow. And you'd have... You'd have a web interface.

**Dave Jones:** Oh, I think I remember that.

**Saar Drimer:** And you do...

**Chris Gammell:** I'm sure that we've talked about it on the show or something, too. I think we did talk about it on the show. Maybe way back. That's the thing. Like, we've been talking about Starz stuff across the years, right? So this is... This show's been a long time coming. Let's be honest.

**Saar Drimer:** So... It was... Um... Yeah. So the idea was to... To have a very clean interface and to mask out a lot of the... Uh... A lot... A lot of the things that...

**Dave Jones:** Make FPGAs horrible.

**Saar Drimer:** Yeah. Yeah. A lot of the... In so many words. Let's just call it... Let's just call it a lot of the... The... The user experience nightmare. Lowering the barriers to entry, maybe. You're right. You're right. No, but it wasn't... It wasn't necessarily meant for beginners, but... It meant to do it... To do a lot of things manageable. And I think we'll touch on it when we get to... What I'm doing now. Um... That... Uh... I wanted to create an interface. It's interesting that I think about it now that I talked about it. What I wanted to do. Because I didn't realize it at the time. But... Um... I wanted to create... Um... A very simple interface. That was... Uh... Intuitive to use. But very... And... But... But where the intelligence is on the... In the back. So... The back end. So it would do a lot of... A lot of intelligent things for you. But the interface would be... Uh... Would be clean. And... And easy to use. And it would just kind of be intuitive. So... Somebody mentioned online once... Uh... The... This kind of... This 747 cockpit interface. Uh... Of... Of EDA tools. And... Um... And... And... Because everything is added. And added. And added. And I think a lot of that happens in EDA tools. And FPGA tools. Where you have a lot of things. And backwards compatibility... Um... Uh... Backwards... Um... Compatibility issues. And... Um... And people not liking change. And you have to kind of keep it... Uh... Keep things the same. And...

**Dave Jones:** Well the FPGA companies are contractually obligated. A lot of people don't understand that. To maintain backward compatibility in these tools. It's not like they can go... Oh... We'll just ditch all those 10 year old chips. No. No. They... No.

**Dave Jones:** You know. The big companies have contracts with them.

**Saar Drimer:** So... It happens more often than not though. I mean... Some tools come out. And then... Fairly recent... Uh... FPJs are not included. And I... I... I... I sympathize. And I understand that. And I think part of the problem with the... I... It's... You're right. Dave. I think... There is a distinction between supporting certain tools. Uh... Certain... Sorry. Certain chips. Which is very problematic. And... Certain... Continuing certain features. And keeping interfaces similar. And maintaining some... Um... Uh... If we talk about PCB tools. Maintaining some of the things that are not relevant anymore. Uh... In terms of manufacturing say.

**Saar Drimer:** Um... Or things have just moved on. But the thing... But... But the... The interface and the options are...

**Saar Drimer:** Are...

**Saar Drimer:** Are still there. Um... Instead of... You know... Everything is hidden behind two or three and five and ten layers of... Of... Of menus. Um... So... Anyway... So both were flow. I think it was a good idea. Uh... But... I... I... I kind of failed at implementing it well. And...

**Dave Jones:** I don't see it on your website anymore. So... No, no.

**Saar Drimer:** I... Yeah. It's gone. After a year... I... After a year I quit and I shut it down. Um... It... You know... Those sort of things need to be maintained constantly. And... Of course. I just didn't want to... Yeah.

**Chris Gammell:** Well... I think that... You know... It should be stated as well that like... Operating outside of FPGA companies I think... Also makes it difficult. Because... They are very insular. I mean... It's in their benefit I think to keep software in house. You know... To keep the... The design secrets in house. Well... Obviously that's a lot of companies. But... Um... I don't think there would be a lot of incentive for third party tools. Even the ones like... Like... Simplify. And like stuff like that. Like Simplify Pro I've used. It's okay. You know... Yeah.

**Saar Drimer:** I think one of the issues that I had with my... With... With the software which is... Which is basically what you just said. Is that... Uh... I was... I was wrapping around the existing tools because I didn't... And... And what that meant is that I didn't have a core innovation. And... Uh... I think that... A lot of times with EDA tools... Uh... In order to succeed... Not a lot of times. It's kind of essential for commercial EDA tools. Is that you have... Um... You have some core innovation. Uh... And... Uh... I didn't have that. And that's one of the things that I realized that... Why it can't work. What... The other thing that happened is that... A lot... Not a lot but quite a few... Um... Small EDA owner... EDA company owners. Uh... Things are... People are trying to do things online and... Um... Um... And not online. Simulators and so on. They... They contacted me and we talked. And I understood how... How... Hostile that... That industry is... Uh... To... To newcomers and people trying to do new things. And... Um... And... I don't know if you remember. There was a company called... Gate Rocket, I think. Gate Rocket. Yeah, I don't remember. Um... They were doing co-simulation with... Um... Um... With hardware. So what they've done is they built a... A hardware where... They'd wrap your FPGA design and... Put it on their system so you can do a co-simulation. What is actually happening in the hardware. And... Um... And your... And your simulation. So you can... You can sort of... Um... Compare... The... The inside and the outside. And I thought that... They had a great product and they shut down. And... Uh... After seven years and... And a few million invested. And... I thought, well, if that's... If that can't work... Yeah, it's like an adult. Yeah. I mean... And... And I've learned a lot from... From... From the guys who run that company and several others. And... It was an education on the EDA industry. And... So after a year, I stopped that. Uh... I worked for a contractor. And I built a mobile phone-like thing. And... That really rekindled my love for hardware design. And I... I... I don't know if it's familiar with... I think... During my senior design in college... I did... It was... It was 12 or 16 weeks. And I... And I was... I was totally... Uh... Engaged in that... Uh... Project. And it was... Um... It... It sort of consumed my life. And I loved it. It was... It was... It was... It was just an amazing period.

**Chris Gammell:** I think we have many listeners that are nodding their heads right now. Yes.

**Saar Drimer:** And... And... And... And it was... It was... It was a great thing. Right? It was because you feel like you're doing something that you love. And that... And that you... You... You dream about it. You wake up. But the only thing you think about is that. And it's... And it felt great. And I think that during my career, I was trying to get there again.

**Chris Gammell:** Chasing that first high, huh? Yeah.

**Saar Drimer:** And... And... And it does happen. But not... Not that... That... Kind of because... Um...

**Saar Drimer:** Well, it's... It's different.

**Speaker ?:** And...

**Saar Drimer:** Uh... I think that when I got back to... Like proper hardware design. And... And... Building... Because I wasn't... I was an academic. And even at Xilinx, it was more kind of a... It wasn't... It wasn't building a product. Right? It was... It was testing... Um... Testing designs and so on. And... Uh... Or doing experiments. And... Uh... And... You know, the PhD was a lot of research and... And things. And... And then I got back to it. And I thought, really, I... This is... This is... This is what... What I love doing. And... Um... Then I finished that project and I... I quit... The... The job. And... I started doing what I do today. And... Um... I... I... I did a few contracting jobs. And then... During that time, this was end of 2013. I... Um... I started writing PCB mode. Um... And the trigger for that was... The frustration with EDA tools. And the fact that they don't allow me to do what I really wanted.

**Chris Gammell:** So, PCB mode is a EDA tool effectively, right?

**Saar Drimer:** It is. It is. I don't consider it an EDA tool. Because... Okay. It helps people make boards. How about that? Yes, yes. No, I'm saying because I don't like to be... I don't like it to be associated with sort of the baggage that EDA comes with. At least from my mind. Um... And we can talk about that. But, um... It is an... It is a... Uh... A tool for designing circuits. Um... Circuit boards. Because, um... Well, in summary, it's a... It's a sort of a command line tool wrapper. Uh... That takes, uh... JSON files, which are very... Uh... Very simple key value. Uh... Text files. Like a very simple XML, if you're familiar with that. Um... Uh... JSON is used a lot on the web. And it takes those JSON files and then it converts, uh... Those into an SVG file, which is, you know, vector graphics. And then I edit that with, uh... With Inkscape, which is a... An open source SVG editor. Uh... Then I extract all my changes. Back to the JSON files. Then I iterate. And then...

**Chris Gammell:** And the JSON contains, like, an atlas? Is that right?

**Saar Drimer:** Uh... Yeah. I'll get... I'll get to that. It's kind of over... Oh, it's a... Uh... Kind of an overall view. And then I'll... I'll... I'll explain a little bit about the structure. And then after I'm happy, uh... PCB mode takes that SVG and, um... Turns it into Gerber's and drill file. Um... And then it's... It's sent out to... To be manufactured. Now, the JSON files contain, um... This... Shapes... Uh... Essentially. And coordinates. And... And... Most... That's the most that... Uh... Most of the stuff that... Uh... Most of the content is just shapes and coordinates. Now, you can put any shape you want. It can be an SVG... Uh... Path. So... Basically any arbitrary shape. And it can be placed on any layer of the board. Uh... By layer... I don't mean like top and bottom or internal layer. But, um... I call them, um... Sheets or... Foils. The... The... Uh... The sort of mass, the silk screen. Uh... Even... Even the sort of paste, uh... Layer if you want to. Uh... Any shape. So... If you can draw it... An, uh... Inkscape or a... Or... Illustrator. Uh... You can put it on the board. And so... But it's structured in a way that you have... Um... A board JSON file where you instantiate modules. Those modules... Module JSON files contain... Um... Uh... Instantiate... Uh... Uh... Components. And those components... Describe the footprint, essentially. So it'll instantiate pins. And each pin can be associated with... Um... Descriptions of... Of what the shape of that pin. And a coordinate... Um... Of where... Where you want to put it. So... Um... That's... That's the structure. And then the routing... Uh... I do by hand... With... Uh... Inkscape. So I draw... I draw it. And it's called... Uh... Bezier... Bezier curves. Um... Oh, yeah.

**Chris Gammell:** And that's like the curvy... The curvy lines, right?

**Saar Drimer:** The curvy stuff. Yeah. And... Um... And then that's... I save the SVG and... Uh... PCB mode extracts those changes. I can also move components and do some other things. Uh... Extracts those changes. Puts them back into the... Uh... Primary JSON files. And then... Then... Then you iterate. Um... It can also generate a BOM and... Do a bunch of other things. Uh... Sort of on the periphery. Um... And... But it doesn't have schematic. It doesn't have... Um... A net list of... You know... Because there's no... Yeah. Without schematic, that isn't... Well, actually... It would be useful to extract a net list out of... That physical... But that's hard. And I haven't done that.

**Dave Jones:** The ultimate end goal here, though... Yeah. Is to produce...

**Saar Drimer:** Boards.

**Dave Jones:** Don't take this the wrong way. Arty-farty looking boards. Really fancy-looking... Yeah. PCBs. Yes. Arty PCBs.

**Chris Gammell:** Yes. Things that you can't do with traditional... How about that?

**Dave Jones:** It would be incredibly difficult or... You know... Excruciatingly painful to do.

**Saar Drimer:** I would say it's like... You know... I have this metaphor where... You can do some of the things that I do with PCB mode... Uh... But it's like... Uh... Screwing in a screw with a knife. Uh... It's not... It's not... It's not the right tool... For... Correct. ...for the job, right? You can... You can because you can have... KiCad or Eagle scripts... That would take... Uh... Something you've drawn on Illustrator... And put it on your... Um... Silk screen layer. But... It's not... It's a pain to... To... Yeah... It's not designed for that. I can verify that. But there's also... There are also practical things. Like... If you think about a drawing tool... Because I started viewing PCB design as a drawing... As a drawing exercise. Um... So if you have a proper drawing tool... Then... Uh... Doing alignment is very easy. And doing... And taking... And doing differential pair... Or a multiple... A whole bus... Is very easy. Because the tools are meant to do that. Uh... Uh... And... And curvy... And any... Any... Any way you want it. So there's a lot of advantages there... Just by using a proper drawing tool. Because... Like I said in my... In my talk... A few weeks ago about... Um... About PCB modes. I didn't... I didn't want to invent a GUI. And I... I... My observation was that... GUI is where good ideas go to die.

**Speaker ?:** Right.

**Saar Drimer:** You... GUI is where a lot of tools fail. Um... And... And... And... And there might have been very lofty goals behind it. Behind wanting to do something innovative. But... Um... The GUI... GUI are hard. And then I figured... Well... I have a perfectly good GUI... Here in the form of... Of... Inkscape. So I'll use that. Um... And... Yeah. But so back to the artsy-fartsy stuff. I... I... I... No. It's... It's fine. It's fair. I... Well...

**Dave Jones:** We... People need to... Why should they be... Why should they use... Why... You know... How can they use... Why should they use PCB mode to... Make their boards look fancy?

**Saar Drimer:** It's a great question. I'll tell you why... What made me start it. Uh... Place. Other than... It was... Uh... Part of it was a vehicle for new ideas. Right? So I can... I thought... Well... I have some ideas about how to do things better. And I want to have a platform to do that. The... But the main reason was I... I started painting. I was doing painting for... For a while. But I... At that point I painted more. And what I ended up painting is circuit board... Circuits. Nerd.

**Dave Jones:** Yeah. Well... Yeah. It's all good. You know... You know what you know, right?

**Saar Drimer:** Yeah. It was close to me and I thought... Well... Of course. Wouldn't... Wouldn't... Wouldn't a big... Big painting of a circuit be so nice? I know. It'd be awesome. Yeah. Yeah. So then... So Dave, now guess what... What was the thought that dawned on me while I was painting?

**Dave Jones:** Why can't I do this on my PC? Why can't I... Why can't I mechanize it? Design a painting.

**Saar Drimer:** Exactly. Why can't I design a painting? Yeah. And I knew the tools and I knew that they would never let me do that. They wouldn't let me do the... All the things that I wanted to do. And so coupled with... With the vehicle for new ideas... I just sat down and spent six months writing the software. And by the beginning of 2013, I fabricated my first board. It only supported one single layer and no drills. But I did it. And then things got evolved. And I recently released version four of PCB mode. And it supports any number of layers that can be practically supported by your machine. You know, Inkscape needs to load up all of them. And the usability is better.

**Chris Gammell:** Like from memory, you mean and everything?

**Saar Drimer:** Yeah. Yeah. Because there's... I mean, if it's too heavy, it starts getting clunky. But... And so I've been... For three years, I've been designing. Now, your question, Dave, why would anybody use that? And that's, I think, a great way to... It's... It lets me say that this is a personal project, right? Of course. Yes. So I've done it... I've... When I started, because of everything that I learned from doing Boldport Flow, what we discussed before, I said, I'm going to develop it for myself. It's going to be open source. So it's an open source. It's on GitHub. And it's MIT license. Very permissive. Written in Python. I said, if nobody uses it, that's going to be fine. I'm writing it for myself. If anybody wants to look at it and use it, that's okay. And that's been my attitude when I was developing it. But I wasn't... I didn't mean to make it a thing, right? I just wanted to be it. But then I enjoyed it so much. I enjoyed doing it. I thought, well, this is really letting me express myself. And doing something that combines what I was passionate about. And it's that circuit design and hardware design. And programming, which I enjoy. And art and design. And so I said, why don't I try to do that? And then that's when I started thinking, well, how can I make it? Into something that I do. And that I can make a living from. And that's what I've been working on for about two and a half years. And it's been hard.

**Dave Jones:** Are you making a living? Is this your full-time job?

**Saar Drimer:** This is my full-time job. Yeah.

**Dave Jones:** I see you're mostly into services. Because I'm looking at your website. And I can't actually see anywhere to download PCB mode. Like I found the GitHub. Yeah. So it's more like you're into services and that sort of stuff.

**Saar Drimer:** Yes. So, no. Okay. So I'll explain. You can go to pcbmode.com. Oh, okay. Right.

**Dave Jones:** It's not linked in. Okay.

**Saar Drimer:** No, but I think your question is right in the sense that I need to make clear. I treat PCB mode as an internal tool that is open source.

**Dave Jones:** Right. Oh, interesting. Yeah.

**Saar Drimer:** So I use it for my work. But it's not something that I am making money off of directly. So that was one of the lessons. And that one is one of the nice things about what I do. I develop an EDA tool. Let's call it that. But I don't rely on people using it for me to make some money.

**Dave Jones:** Got it. Right.

**Saar Drimer:** Nice. And it's gaining a little bit of interest. People are starting to get interested. I mean, I think a lot of it is motivated by things that I do. And I always try to make things interesting.

**Dave Jones:** Well, because people see. I mean, your PCBs have been, these arty looking PCBs have been published everywhere. Like, you know, and people are seeing these and go, wow, you know, how did you do that? Yeah, exactly.

**Saar Drimer:** So, you know, people can do it. The tools, unfortunately, as a practical matter.

**Dave Jones:** Circuit PCB design tool, right.

**Saar Drimer:** Well, there is. It's not, you know, it's not a replacement. It's not a drop-in replacement for Eagle or whatever. But what I was going to say is that for practical reasons, I can't invest in making it more usable or more documented. Because I just don't have the resources. I can understand that. Yep. So, I do some. And I support people who are using it. But I'm not. You know, I could probably spend a whole month documenting the thing and making it very usable for people. But I just don't. I can't. I can't put that time in. And part of the hope always with open source projects is that, you know, it'll pick up a community that would contribute to that. And that really hasn't happened. But, like I said, I'm okay with that. But it would be nice if it did.

**Dave Jones:** Well, because it's a very niche thing, right? I mean, you know, how many people want to produce art or feel the desire to produce arty PCBs? I mean, it's, you know, it's relatively limited.

**Chris Gammell:** Well, I think that's another question, too, is do you think that there is a case for just an everyday design? As an everyday design type tool as well? I mean, are you using it in that way for your work?

**Saar Drimer:** Well, I mean, I do design, you know, audio, some products for, not products, but these are kind of for, one design I did for Eurorack. I don't know if you're familiar with that. I designed a Bluetooth Low Energy product for a company with it that wanted to have a window that you can see the circuits.

**Dave Jones:** Ah, you can see the board, yep.

**Saar Drimer:** Yeah, and some of the user interface was there. So, for example, the label for the button was on the board. Right. So, they didn't need to have that on the external case. But a lot of what my work is for people who want – for projects that require that visual – that benefit from that visual element. So, if somebody comes to me and wants a project in a box where I feel that I'm not giving them that benefit, then I tell them that they're probably better off going with someone else. Of course, a regular design house. Yeah. Because, you know, I have a certain specialty and where I can contribute and, you know, if they're not going to benefit from it, then, you know, it might not be in their best interest. So, yeah, I don't know. You start something new and you're exploring and you're experimenting. And I think one of the things that is very important to me is for people to experience electronics in a slightly different way. So, the experience is important to me. So, it's not – and it's just not only the board. It's the way it's packaged and the way it's presented. And so, I'm less interested in people using Arduino or Raspberry Pi or things like that. I want them to have a sort of feeling of discovery. And you could do that with very simple things. So, you could do that with LED and a battery and a resistor. You can learn a lot from that. You don't necessarily need a Raspberry Pi or Linux running on the machine. So, I try to concentrate on those things. And, look, if you're going to do controlled impedance, eight-layer boards, you won't use PCB mode, right?

**Chris Gammell:** No, it's got to be incredibly painful.

**Saar Drimer:** Yes. You could. Yeah. It's just going to be like other stuff, right? You'd have to do all the math in your head or on paper or something. But you can do quite nice sports. And it really depends on what you're trying to achieve. If you want to have that little while factor when somebody opens the product and go like, whoa, this is nice, I'll take a picture and put it on Twitter, then you gain something. Or some of the things that I'm promoting to chip and IC manufacturers is to move away from the square green giveaways and demo and evaluation kits and do something more interesting where the user is more excited about using those kits. And that's the purpose of them, right? Because the purpose is for them to use it and not look at it as a chore. Oh, now I need to take it and install the tools and stuff. But if I give you something that you say, hey, that would be so cool on my desk, you're actually getting familiar with the chip or whatever is on it. And you have it on your desk and then you have the logo there. And when the engineer is designing in a component, you have that logo there near their desk and that's where you want to be. So I think there's some mileage there. I'm trying to get a bit more work there. Designing kits as giveaways and things that have a novelty factor to them.

**Chris Gammell:** Yeah, there's a surplus of, almost like PCBs as an art form now, right? So there is a surplus. They're dropping in price, obviously. We love Oshpark as well. Just in terms of the cost coming down. So now thinking of this as a new medium and being able to deliver a better experience like you're talking about, I mean, it does seem like it's actually the right time for that kind of stuff.

**Saar Drimer:** Yeah, I mean, you'd know this, right? The circuit, the PCB manufacturer medium is actually very versatile.

**Chris Gammell:** Yeah.

**Saar Drimer:** You can do a lot. You see, I mean, I'm not paying any extra for these designs, by the way. There's not the...

**Dave Jones:** No, it's just artwork. The manufacturer doesn't care. Exactly. They'll print any. They'll print pictures of fluffy bunnies on the board. Gerbers are Gerbers.

**Saar Drimer:** And unless you do V-grooving, the routing is the routing, right? You need to route the board out, right? So it goes on a little curve. Big deal.

**Dave Jones:** And they can even do, if you pay them enough and explain to them, they can do some tricky stuff. Yeah. In terms of they can do controlled depth routing. They can do all sorts of weird and wonderful stuff embedded in your board. You know, there's embedded components in the board. There's colors you can do.

**Saar Drimer:** There's soda mask and silk screen. There's a lot to explore there. And this is what I'm trying to do. Every time I do something new, I try to... I work with fabs and push them to... They get a coffee with it, like, oh, crap.

**Dave Jones:** There's people who don't realize you can do multicolored silk screen. I've got a colleague, friend of mine, who did, like, an old Apple board. Oh, I've seen that. I've seen that one. Yeah. And he's got the eight color, like, the Apple logo, right? All in different colors. It cost a fortune. It cost more, yeah. They did it, right? But, you know, you just have to ask, you know?

**Saar Drimer:** And I go, oh, yeah? You have to ask. You have to have a fab that is willing to... Flexible. Because, you know, mixing a new color for you and taking off a machine, a machine offline to do that and stuff, it costs money. And some fabs just are not interested. But the more you work with them, the more they come to... And what I found, actually, is that they love seeing new things because, you know, in the factory, the job is very monotonous. And they see the same stuff over and over again. But then, all of a sudden, they go, like, whoa, what is that? And they get, you know, they actually want to help you. I know.

**Dave Jones:** Yeah, yeah.

**Saar Drimer:** I've definitely found that. Yep. I'm still figuring things out. You know, I don't have the answers. You know, sometimes I ask myself, what the hell am I doing? You know, is it sad? Oh, we all ask that. We all ask that, right? Yeah, we all do. And I really believe in it, though. I think that there's something here. I can say that I might not have figured it out yet. But I'm hoping that... What I found is that the longer you exist, the more opportunities kind of come because people... I mean, that's kind of obvious. But if somebody heard about you, say, a year ago, and they had nothing for you, then they move jobs or something. And then if you're still around, they call you up and they say, hey, you know, I want to do something or things that I've done like two or three years ago, people all of a sudden are interested and they want 500 of them. And I go, okay. You know, that's good. All right.

**Chris Gammell:** Planted that brain seed, all right. So, yeah. So, I have a practical question about the software real quick because I do want to move on to the other stuff like the Boldport Club and just kind of the EDA, kind of higher level discussion. But how do you do... So, when you do a via, for instance, where you have an overlap and connection and stuff like that, how do you actually do that in Inkscape? Like, how do you actually visualize that? Is it just another... Like, the drill is a layer and then it's just a circle or what?

**Saar Drimer:** So, a via is slightly special, but not as special as it is in other tools. So, a via for PCB mode is just like a component. It's special because you can... Normally, you instantiate a component in the JSON files. You can't just say, I want a resistor here. You have to in-text, add it, and then regenerate. But a via, you can say, I want a via here through some mechanism. And when you extract, you'll know there's a via there. And so, it'll just put, just like a regular component with the drill and pads. Whatever that via file is a thing. And if... One of the nice things that I always think about in general terms... So, you know, in PCB mode, you can even have a three-layer board. Now, that's nonsense, but you could if you wanted to. You could have... It's not nonsense. I mean, it can be done, right? Because they, you know, they sandwich the prepregs however you want them. But nobody, you know... You can pay extra for a whole lot of... Not much, right? But... Or you could have three layers of solder mask if you wanted to. If you wanted three different colors. Or you can have... Or you can have a completely different shape on the internal layers of a drill or a via. Yeah. So, you don't have to have, like, a circle, circle, circle. Or anything. You can have whatever shape you want. And if you want to have sight for... For... You know... Yeah. For waveform. So... Does that answer your question?

**Chris Gammell:** Yeah, I think so. And I think that a lot of that, like... The power and also the handicap for your stuff is probably the arbitrary... The ability to make any arbitrary shape, right? Because you have to check against it. All your ERC, DRC is in your head, right? Exactly. And then...

**Saar Drimer:** That's the point. Yeah. There's no... There's nothing that tells me that two routes are close to each other. Right. Exactly. Exactly.

**Chris Gammell:** And then on the other side of it, like on the KiCad side, at least... I know that Dave will probably say that all teams can do different things. But on KiCad, at least, it's very limited on terms of the number of polygons that you actually... You know, because it's constrained by these mathematical functions that it's using, right? It's not an arbitrary shape anymore. It's a shape that the math understands and it can do checking against and all this other stuff. And so that's where it starts to limit you, basically.

**Saar Drimer:** Yeah. Yeah. One thing about DRC that is interesting is that there are some PCB manufacturers. I know one. There might be more. Eurocircuits that... They have an online sort of DRC. They call it checker, PCB checker or something like that. So you upload your Gerbers and it'll do the DRC for you. So you don't have to order the PCBs. I order from them because, you know, they're close and...

**Chris Gammell:** That is called a marketing tool.

**Saar Drimer:** That's fine. I mean, it's a useful tool.

**Speaker ?:** Yeah, right.

**Saar Drimer:** Of course. Of course. So I do the DRC there, you see. Oh, interesting.

**Chris Gammell:** Okay.

**Saar Drimer:** So I upload the design and it'll show me, it'll flag up some things. It's good because it tells me, you know, that it's conformant to their process, but it also flag up some things. And I also found it very useful to see things in slightly different format. So, and have a tool that is independent of the tool that you're designing with. So all of a sudden, even if you upload to Oshpark, you know, you all of a sudden see it in purple. You're like, oh, that thing... That doesn't look right. Yeah. That doesn't look right, right?

**Chris Gammell:** Yeah, that doesn't go there.

**Saar Drimer:** And so, or use a Gerber viewer that is different than the tool that you're using and just see it slightly differently and that brings up some things that you might want to fix. So, yeah, that's kind of what I do for DRC, but a lot of it, it's just by, you need to know what you're doing basically.

**Chris Gammell:** Yeah, that makes sense.

**Saar Drimer:** And just before we go, that's one thing that people a lot of times react to things that are seeing online is that they assume that I'm coming from the art side and doing... And so they're going, oh, what do these artists want to do with our craft and things? But it really... Well, you can't win.

**Dave Jones:** Because others will claim, oh, he's an artist coming into the PCB world. And then others will claim, oh, he was a hardware guy and now he's going all arty-farty.

**Saar Drimer:** You know? Exactly. Which is perfect for me because the last thing I want to do, B, is in the middle, you know, where people are like, oh, it's boring, you know? So it's fine.

**Chris Gammell:** Free is where it's at, folks. Come on. Let's be honest.

**Saar Drimer:** All right. So...

**Chris Gammell:** Well, let's talk about the EDA industry. I mean, obviously... So you gave a talk at FOSDEM and FOSDEM is free open source... Dem? Something, something, something. I don't remember.

**Chris Gammell:** It's basically an open source conference that happens in Europe every year.

**Saar Drimer:** In Brussels every year. That's the first time I go, I went, but it's been happening for many years.

**Chris Gammell:** And they have an EDA room, right? I mean, so I heard about it from the KiCad mailing list, but they have a room there that's just dedicated to this, right?

**Saar Drimer:** Yes. It's called the EDA dev room. I think that's the second year that is happening. Organized by Javier from CERN. I don't remember his last name.

**Chris Gammell:** Yeah.

**Saar Drimer:** And CERN who's, you know, investing in KiCad, which is great. And yeah, so I gave a talk about PCB mode. I gave sort of the short version here. The, and I talked about the EDA industry and it's, I'm frustrated, but I'm hopeful. I think... So say we all. So the frustration comes from a culture of EDA. So EDA for me is a culture, is a mindset. A mindset that was born in the 80s when EDA started becoming the tool to use or EDA tools became prominent in the 70s, 80s when, you know, that's what you started designing.

**Dave Jones:** Everyone started getting a PC and wanting to automate their, yep.

**Saar Drimer:** So at the time, computing resources were very limited. So you didn't, you couldn't do a lot of things. So it started constraining you. But, and then we were left without those constraints to this day, like 45 degree angles and various other things. But more importantly, EDA was born out of, with, with the view of a single, a single user mentality, a lock, a very strong lock-in mentality and no consideration whatsoever for user experience. But that, that's really not their fault because in the 80s, nobody, user experience wasn't a thing, right?

**Dave Jones:** No, it was, it was design PCB, draw, trace, here, place, component. Right, right, line, line, line, line, square. Yeah, yeah, yeah.

**Saar Drimer:** And if the, and if the option is behind three menus, then tough, you know, just click it and it'll be okay.

**Chris Gammell:** Right, because you're going to training on the computer and you're going to training on everything else because that's just the way it is.

**Saar Drimer:** Yeah, you should, you should be thankful that it's there.

**Chris Gammell:** Right.

**Saar Drimer:** But we don't live like that anymore.

**Chris Gammell:** Speak for yourself, man. I use Kaikad. No, no. I'm kidding.

**Dave Jones:** No, I, I'm. He's 100% spot on, folks.

**Saar Drimer:** I'm looking, I'm looking at, I'm looking at the software development world and I am envious. They are very agile in adopting new things. They develop new methodologies all the time. They have very, I'm saying shiny tools, but, you know, in the good sense, not, not shiny and like shiny throw away kind of thing. They have new things. And, and I think in the hardware world, we are about a decade or two behind. And, and I think that a lot of it has to do with that initial EDA mentality. Um, because the big three, uh, you know, and, and, and company, um, they have, they have that culture ingrained there. They, they're not going to change. They, they're not going to get rid of their entire, um, design teams, uh, or software design teams and, and, and, and bring in, uh, fresh ideas.

**Chris Gammell:** Um, well, would you, I mean, that's the thing, that's what I usually come down to is like, I, I don't think I would. And if you're making money, there's an externally driven thing.

**Dave Jones:** Well, it all comes down to need, you know, I mean, the companies are still, yeah. Okay. I'm getting to that.

**Saar Drimer:** So I'm getting to why I'm hopeful. Okay. So, um, I'm excited about new people from the software, from the software world coming in and gaining interest in hardware development because they are bringing in, I know they are bringing in a new, a mentality that would be good for our industry. So they are, they are looking at the tools that we're using and they say, you know, what is this? This is unacceptable. They're tearing their hair out. And they, and then they go and some of them go and do, uh, build new tools. Now they might not be great and they might not know much about hardware design, but we can learn from that and we can innovate where the big, the, the, the bigger companies can't. And what I said at Foster, I said, look, open source is not enough. You need to innovate. You don't have, you don't necessarily, and, and open source projects are in a good position to innovate where they're not shackled by this, uh, what I call the EDA vortex. This, this, this kind of, um, influence, fear of influence of, of bad culture. And, um, and I encourage people who are, who are, who are doing things in this area to, to try, to try new things. Because look, if you're a company like a Verta, you, uh, your goal is to be sold. Right. And you get sold, you know, you're a startup, you get sold to the big three. So you need to imitate, right? You need to make tools that are the same because otherwise like Zach, uh, the guy runs it, wrote in one of the blog posts, he said, we needed a place in the, uh, in the, on the table, in the table, on the table. And, and I, to me, to myself, I said, look, you know, no, you don't really, you create a new table and then, and then be attractive enough for them to come to, to, to be interested.

**Dave Jones:** And I, I just had a vision of you sitting lonely at your own table, but it's my table, damn it.

**Saar Drimer:** For about 20 years and, uh, drinking, uh, no, crying, uh, whinging.

**Dave Jones:** And then you're sitting there, you finally showed up, it's been 20 years.

**Saar Drimer:** Yeah, so I, uh, I'm saying you, you can, you can, um, the open source tools and people who are doing things in this area, um, uh, can, can innovate and look at what the frustrates the, the new users who are coming in now. But the, the, the reason to get most, uh, most excited about, I think is actually the new, um, new investors in this area. And they're not, they're not investing yet. I mean, there's CERN, which is a very good start, but Google, Amazon, uh, Facebook, I imagine Twitter and many other big companies, they're hardware companies. They all have hardware projects. Yeah. And, and they, uh, particularly, I mean, Google, Apple, uh, Facebook, they are known for solving problems that they're unhappy with, right? So if, if they had inadequate tools or tools that didn't exist for what they wanted to achieve, they created it. They created them. And I'm hoping that their interest in hardware will drive a new era of EDA, or I hope it's not going to be called EDA. It's going to be called something else. I have no idea where it would be, but it would be called something else, um, that, uh, tools that are going to be very productive and match the, the kind of development mentality that software development has. Now I, I'm not, I'm putting aside, um, the difference in software and hardware. I mean, we're, we're kind of all aware of that. Um, uh, the, you know, reliability and, and, uh, the fact that mistakes cost a lot more and things, but I think that we still have a lot to learn from software, uh, development, uh, things like revision control and things like that, that, um, Yeah. You're right.

**Chris Gammell:** How's that? How's revision control going for you, Dave? I know.

**Dave Jones:** I don't want vision. I don't want revision control. I just want to upload. Damn it. Anyway, let's not go there. We got to argue after the show.

**Saar Drimer:** So that's the, that's kind of the, the essence of, uh, I think. So, um, you know, I'm, I'm sort of creating a narrative for a future where things could be very interesting and liberating from, uh, considering the constraints of the big three and having a bit more consumers, both on the user sides and both on the investment side. Um, so encourage to innovate.

**Chris Gammell:** What do you, what do you think it would take for someone to jump over to that? Some, something new though. I mean like that, because honestly, like that's, I was talking to someone about this recently and they're asking, you know, oh, well, how do you get started? You know, how do you, I think they were talking about, uh, ECAD and MCAD playing together, stuff like that. So, you know, how do the electronics output go into the mechanical and back and forth? And, uh, you know, it's like, well, ultimately if you come into a, uh, into a scenario, like if you get a new job, you very rarely, unless you're being hired because of you have like Altium skills, like something like Dave, because you, you already know the program and stuff like that. When you're a new grad, you just come in, you know, you're, you get what you're given because of these high level costs. And I think that some of the things might be, uh, you know, driven by smaller companies and just, you know, wanting to keep costs down maybe, but what do you see is what'll drive it?

**Saar Drimer:** You're right. I mean, the dynamics of, uh, inside companies, um, is such that there's no, there's no incentive and nobody's encouraging you to, to, uh, to try new things and new tools out there. Uh, the switching costs are very high. Uh, so it's also, I mean, even if, even if there's a better tool out there, uh, company, companies are not going to adopt it because they're invested so much already. And that's one of the things that I learned about doing stuff with Boltport flow, um, why it can't, right. But, so it's going to take a long time. And I think that that, that's where, that's where the open source tools like Icat could really shine, um, by creating such a, such an awesome tool that it's sort of from the bottom, if you will, um, uh, sort of influenced from the bottom creates such a, it doesn't have to be awesome in all respects, but it can be something that is really, really good. And that will get people's attention.

**Chris Gammell:** Right.

**Saar Drimer:** Yeah. It's not easy. I know. I'm not, I'm not, I'm not saying, I'm not saying it's easy and it's going to take a long time, but hopefully with encouragement and money and, uh, from, from big companies and, and, and you gotta say, I mean, certain certain putting money in KiCat is amazing. It's just, it's just, it's so I'm just, I'm just, I hope there's just going to be more and more of that.

**Chris Gammell:** And maybe money into Boltport too, or PCB mode, sorry. No, to Boltport. Yeah. Yeah. Yeah. Either one's fine. Either one's fine.

**Dave Jones:** Just give me money.

**Chris Gammell:** Right. So speaking of. Speaking of. Yeah. So what, how can people, uh, no, so you have a new thing that you're calling the Boltport Club, right? What is this thing?

**Saar Drimer:** So, um, I do, uh, a lot of, a lot of my businesses, uh, well, the majority of my business currently is, uh, doing contracting work for, uh, doing, designing boards for, for companies, doing the kits and so on. Um, but I'm starting this thing called the Boltport Club, which is a monthly subscription for electronic product, projects that I create. Well, you sign up and you get in the mail, uh, every month. So it must, it'd be a fairly small project. Uh, I call it a project, but it's an overall thing where it might be a kit. It might be a board. It might be a board with some components. It might be something else that is interesting, um, for, that I think would be interesting for the, uh, for the membership, you know?

**Chris Gammell:** Yeah. So like an example would be your, uh, your, like your cordwood puzzle, which I think we've mentioned on the show before. The cordwood stuff.

**Dave Jones:** I had it on my mailbag. Yeah.

**Chris Gammell:** Oh, that's right. Exactly.

**Saar Drimer:** And so, so I'm, I'm, I'm right now I'm developing the second edition of, of the, the puzzle. That's going to be there. Uh, one of the first three. So you sign up for three months for 49 pounds. Um, and that's including shipping and taxes, um, if that's relevant to you. Um, and, uh, and you get three, those three projects. The first one is going to be the peas, peas board, you know, the, the, my, my favorite, uh, programming language.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. That's a fun one. I like that.

**Saar Drimer:** So there's a new edition. It's, it has new things and I'm, uh, it's going to be really nice. That's one, that's the first one. The second or third is going to be the cordwood, the new version of a cordwood puzzle. And another is going to be the, um, the emergency kit. I started with.

**Chris Gammell:** Oh, that's right. And I saw that thing. So that's like, uh, you kind of carry it around just like a little tin. Yeah. Yeah.

**Saar Drimer:** There's a nice story in it. Yeah.

**Chris Gammell:** Yeah.

**Saar Drimer:** Right. Um, and, uh, with, with the components, uh, the through whole components, but, uh, inside of the board rather than through, you know, um, but, um, I started with those three because those three I've done before or done a previous version of them. So I wanted to, to, to get stuff out that, you know, to minimize some of the, uh, of the unknowns, but so those are the first three months. And then I have plans for what would happen next. I I'm running a six months experiment. Um, so, uh, hopefully, hopefully there's going to be, I have about 50 members now, uh, already. And I started about three weeks ago. So that's quite encouraging. Excellent. Yeah. So like I said before, I, I know that there are other monthly subscription, electronic subscription out there. I am, I'm interested in making things, um, unique. And like I said, have people look at electronics slightly differently and, and, and, and entice them and drive them to discovery. So you might, you know, for, for the piece board, the circuit on there is, um, directly from the data sheet and you might be encouraged to go open up the data sheet and look at how do you, how do I change one value to make the LED, um, you know, flicker more or less, you know? So, um, and, uh, my purpose is to create things interesting for, for people, not necessarily beginners or, or teenagers or adults. Um, and I don't think about those sorts of things. I just think about what, what could be interesting.

**Chris Gammell:** It's almost like a electronic conversation pieces that also are fun to build. How about that?

**Saar Drimer:** Yeah. And, and I think they're collectible. Uh, I'm making limited, I'm making limited editions of them. The idea is that I'm going to make a certain amount and members can, can buy old ones, but I'm not, I'm not repeating. So if you, if after three months, somebody starts after the first three months, they're not going to get the previous ones. They'll be able to buy old stock if, if it's left, but, uh, they're going to, people will get new, uh, new projects rather than, than old ones. And, um, I'm really excited about it. I think that, um, it's, it's, it's a matter of, of numbers at the end. Uh, I think the price is, I think about right. Um, and, um, but of course you can achieve a lot more, the more, uh, paying members you have, uh, of course. So, um, it's, it's a little bit like a mini crowdfunding thing because you get paid ahead of time, but it scales, uh, and you're not, you're not getting hammered by, by it. I like things that, that sort of taper, um, and, and you can build up relationships and build up, um, um, you know, production and so on. So, uh, I'm, I'm, I'm going to succeed.

**Dave Jones:** Well, we hope it goes well. Thank you. Thank you. Where can people catch you? Are you a Twitter man?

**Saar Drimer:** Yeah, I'm on Twitter. Uh, there's, uh, at Boltport, uh, mostly active there. Um, pcbmode.com for pcbmode, boltport.com for Boltport and, um, boltport.createjoy.com, which is a service that does the, the sort of subscription thing. Uh, so I have a webpage there. Um, where you can sign up.

**Chris Gammell:** Awesome. Awesome. Well, I highly recommend the people not only go check out that stuff, but, uh, we've mentioned in the past, the Hote circuits thing and the life game. And I think all, I think just, I mean, really, it's just, it's really refreshing to see you doing this kind of stuff for a lot of different, you know, like, like I said, using PCB as a medium. I think that's really, that's really awesome. And I think that more and more people are doing that too. And it's, it's a nice trend. I like that.

**Saar Drimer:** Thank you. I, I, you know, it's some of the, some of the nice things that happen is that I get called by a photographer that, that wants to use me design six pieces to go into a fashion magazine. So, uh, like, you know, it was appeared in Marie Claire in the U S, uh, in December.

**Chris Gammell:** And that's, that's just as soon as I opened my subscription, man, I just, I was very surprised. I was expecting, uh, sensible young ladies fashions.

**Dave Jones:** And I saw her.

**Chris Gammell:** Yeah. I mean, that's great. That's great. And now I will extend my subscription. Yeah.

**Saar Drimer:** It's, uh, yeah, it's, it's, it's, it's, these are, these are, I really enjoy this work. Uh, I really do. I hope to get to continue. Yeah.

**Dave Jones:** All right. Well, thank you very much for joining us.

**Saar Drimer:** Thank you for having me. It was fun.

**Chris Gammell:** It was good talking to you.

**Dave Jones:** Awesome. Talk to you soon. Catch you next time. Bye.

**Speaker ?:** Bye.
