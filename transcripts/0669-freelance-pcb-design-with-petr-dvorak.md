---
episode: 669
title: Freelance PCB Design with Petr Dvorak
url: https://theamphour.com/669-freelance-pcb-design-with-petr-dvorak/
---

**Petr Dvorak:** This is The Amp Hour Podcast. Released June 6th, 2024. Episode 669. Freelance PCB design with Petr Dvorak.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Kamel of contextual electronics.

**Petr Dvorak:** Hello, this is Petr Dvorak from the Czech Republic. I'm a freelancing hardware design engineer. I'm freelancing for about seven years and I offer my design skills and general hardware design services to customers from around the world. Well, welcome, Petr. How are you doing? Thank you for having me. Thank you for invitation. I'm doing pretty fine. How are you?

**Chris Gammell:** Good, good. I have many things I'd like to talk to you about today. First off, you are a prolific LinkedIn poster, so I always get to see your stuff in my feed and all the things you're working on, which is great. And I thought we could also talk about your QCAD work. I think you're a great promoter of QCAD and all that kind of stuff. You refer to yourself as that QCAD guy. Yeah, yeah. That's great.

**Petr Dvorak:** Thank you. Thank you. I try to promote that software, that EDA tool, because I think it's great. And according to the posts I can see on LinkedIn, the majority of projects can be done in QCAD instead of very expensive tools. No offense, but yeah.

**Chris Gammell:** That's great. That's great. So let's start there, actually. So I'm a long-time user myself. I am always behind the curve. I was telling you right before you started recording, I just switched to QCAD 8, and so I'm kind of lost with some of this stuff. How has that transition been for you?

**Petr Dvorak:** Yeah, the transition from the QCAD 7, version 7 to version 8, wasn't smooth, definitely. I don't think that they should release the version 8 at the day they did. Because I'm not sure if the version was ready to be called a release version. It was buggy, slow, some stupid improvements in the quotes, like you needed to confirm the drawing, like the tracking routing tool with the left mouse click and something like really slowing down the work.

**Speaker ?:** Got it.

**Chris Gammell:** Like workflow type stuff versus some buggy stuff, but then also workflow type stuff. Yeah, I find from workflow perspective, generally I like a lot of the new things there. And most of it feels the same to me. Mostly it's just me kind of getting older and grumpier, and I'm like, oh, I don't know where they move my button. You know, like that's basically the level I'm at right now. And yeah, I'm going to, you know, like I always do, I'll come up around to it. I'm certain all the methods too is like, I think in every version, I'm like, why did they do it this way? And then like three months later, I'm like, oh, I get what they did.

**Petr Dvorak:** Yeah. Luckily, they improved the performance and the bug fixes were done from the 800 to 801 even. So now it's a fully functional again.

**Chris Gammell:** Yeah. And you had mentioned like kind of everything that you think needs to be done for a majority of electronics projects could be done in there. What is the, you know, where are the levels, the limits of what you're kind of doing in KCAD that maybe could give people an idea of like the complexities?

**Petr Dvorak:** The number of layers in KCAD is like unlimited. So this in comparison to, for instance, the free version of Eagle in the past that where I think there was like two sides only. So no limitations in that regard. You can route high speed differential pairs. You can route rounded tracks in any angle. You can do anything. To be honest, I don't feel like to be limited with KCAD. I am limited with my skills, with my brain, not with the tool.

**Chris Gammell:** Same. And I do feel like usually the thing that I come up against is like people being like, oh, well, you know, I'm doing extreme HDI, like, you know, 24 layer FPGAs, DDR5, whatever. I'm like, okay, well, yeah, you probably, I'm like, that's not for me, thanks, you know? But I'm sure there is some limit there. It's just as a, you know, as a normal, I have not reached them personally.

**Petr Dvorak:** Yeah, yeah, definitely. I wouldn't recommend KCAD to designers who need to design special super trooper high HDI designs with, I don't know, super fast 120 gigahertz modulations, something I can't even speak about. So there are missing simulations and online helpers as in Altium or PADS or Mentor Graphics or how it's called today.

**Chris Gammell:** Yep, yep.

**Petr Dvorak:** But for normal things, normal, fast, high-speed design today, you can use it. And even, I think, our industry changed because the high-speed design became go-to-a-guy thing. Yeah. So you don't anymore design 12 or 12-plus layer PCBs. You just buy a module with high-speed design, made by professionals, and then you can place it on your six or four-layer boards, and you are happy.

**Chris Gammell:** Yeah, totally. And yeah, it's tested. It's, in the case of RF, it's maybe pre-certified. It's, yeah, I think that's right. And then basically, that cost of that high-speed design is amortized over the module cost. You know, you have to pay maybe an extra dollar for the part, but from my perspective, it always works. I don't have to worry about, you know, talking to the board vendor and, you know, hearing about, oh, their stack-up is slightly changed. You want to do a change order, all that kind of, like, just the stuff you need to keep on top of if you are doing a chip-down design that's, like, super, super fancy.

**Petr Dvorak:** Yeah, yeah, definitely. But even design a 12-layer board with Kycat, some carrier board for, I don't know, what HPC board or something. But, yeah, I didn't feel comfortable doing it because it's something, I think, more expensive tools are needed. So, yeah, I have to admit that there are some limitations. But for my designs, for my customers, I'm not limited.

**Chris Gammell:** I think that's the most important thing, you know? So, like, you're a consultant, I used to be a consultant. Like, I think it is really important to know your own limitations, too. Like, I would often be asked to do something by a potential client and be like, that is not me, man. You know, like, that is not a good idea. You know, I can learn it. I could do it. I'll, you know, only charge you the parts that I know how to do. I won't, you know, if I'm learning something, I'm not going to charge you for the stuff I'm learning about. But, like, it's not going to be the same experience or the same short delivery time that every client always hoped for, right? They want the answer. Sometimes they're like, yeah, learn it. Great.

**Petr Dvorak:** Definitely. You hit the nail. I need to consider every time that, yeah, my approach is that I need, I want that each project will move me forward, like, to give me opportunity to learn something new. But if the bar is too high, I say, oh, I'm sorry, this is outside of my expertise or skills. And I have some freelancers around. I know about them. And small companies in the Czech Republic, I can recommend them because they have team experience, yeah, collaboration. And they will give you a good price. So go for them.

**Chris Gammell:** So you have kind of this ideal in your head of, like, what would be kind of the edge of where you'd feel comfortable, just like the stretching to, like, learn new things. So maybe give us the idea of your normal style of design, like what, you know, any old Tuesday might be for design. And then, like, I'm really feeling, like, excited about learning this new thing.

**Petr Dvorak:** Yeah, I would say that the limits of design I would like to work on is that when I manufacture the prototypes, the limit is that when I don't have tools to verify it fully, it's my limit. So paper or EDA tool can digest anything, anything you want. But when you have the prototypes on the table and you don't know how to verify them, how to measure them, how to verify that the impedance of the tracks or differential pairs is correct, or if the eye diagram is correct at each conditions. So this is something I don't go for because, yeah, it's outside of my expertise. And in that case, I would only deliver the untested prototypes to my customer and say, I hope it will work, but it's not something I would like to do.

**Chris Gammell:** You only operate closed loop. You don't open, that would be open loop if you don't have the verification. Yeah, exactly.

**Petr Dvorak:** That's good. That's a good term about that. Yes. Yeah.

**Chris Gammell:** That's a good marker too. As soon as you said that, I was thinking about one of my consulting jobs that went very poorly because I didn't have the expertise and the knowledge and I ended up just not charging the client for it. I was just like, you're not paying for this because it didn't work. I wasn't able to verify it properly. It just fell apart at that point. And it's like, I'm not going to charge for that.

**Petr Dvorak:** Definitely. I am not a firmware guy. I used to offer some firmware coding services, but I decided a few years ago that this is not something I need to focus on because I think coding as well as hardware design needs 100% of your time. If you do it occasionally only, you don't improve and you go down the hole. So I would like to say that regarding the designs that, yeah, definitely when there is a microcontroller or microprocessor that needs to be programmed and I'm not a programmer, I only am able to verify if the firmware is uploadable, if the LED is blinking, yes, simple routines for verifying the ports, if I can control the ports, if I can control the I2C peripheral or something. And then I say, okay, it works, but definitely, definitely I can't verify everything. But to me, it's usually enough to verify that the microcontroller works well.

**Chris Gammell:** Yeah, no, that's a good point. I think that is, that's another important limit there. You know, and my own thing, I was trying to do more of it because I ran into the problem where I couldn't source enough work that was like consistent on the hardware side. Do you find that as a problematic thing? Or maybe you're also doing more of the manufacturing that I wasn't doing. Like, how do you keep work consistent as a hardware designer when hardware designs are often kind of choppy?

**Petr Dvorak:** I don't know if I understand correctly the question.

**Chris Gammell:** Let me explain choppy real quick. So I always talk about choppy. So I go out and I source new hardware clients and they're like, okay, yeah, you don't have to do the firmware, whatever. We have a team that does that or I'd hand it off to a, you know, another contractor like you mentioned for some of the higher speed stuff. I would do that for firmware. But then for my work, it'd be like, all right, do a new rev, please. You know, go from rev A to rev B. I'd go do that. It would take maybe two weeks. I'd build it. It'd go out for fab. And by the time it gets back, I'm basically validating it and handing it off to a firmware engineer. But then like, they're doing firmware for two months. And so now I have to go source another client. And so in that way, I'd say like, it's kind of choppy because client one has a chunk of time that they need done and client two has a chunk of time they need done. And unless I'm like really overlapping them properly and like managing that, it could be that there's big gaps between clients. Yeah. Because of firmware development.

**Petr Dvorak:** Now I understand. Yeah, I was confused by the choppy word. Definitely. I can handle, I do handle more than, I think, five plus projects at a time. And I pipeline them. It's not like chopping wood. It's like, I work like four hours on a schematics and then I send an update to the customer. I cooperate with the customer frequently because it helps me to avoid rework in the future because in the past I used to work for instance 20 hours on a schematics and then I will send the final version from my point of view and they said, yeah, we didn't want that. We want to change this and that. So there was like 10 hours rework out of 20 works, 20 hours of work. So now I send updates even every day. After two hours of work I sent, okay, this is the new version. Please check this and check that and if it's something you want and when I got the green light from the customer I go ahead, I continue. So this approach helps me to pipeline more projects at a time. I don't call it like multitasking. They say that multitasking lowers your IQ or I don't know what. But I pipeline. I do four hours in the morning and then two hours afternoon on a completely different project, completely different customer and it helps me to refresh my brain to focus on the different things and then the next day I will continue for the project A then afternoon project B. So I'm powerplining. So this helps this work for me and I won't keep myself busy because I don't know why I hate empty calendar. Personally,

**Chris Gammell:** I also like money. I don't know about you but I also do like some money. That does help. Yes, yes,

**Petr Dvorak:** exactly. So when the calendar is 80% full I am completely happy and I do in that way.

**Chris Gammell:** Yeah, no, that's really smart. I think that sounds like some good method as well if you are going to do that kind of hardware like the over over communicating until they're like just do they ever come back to you and say better just do it I don't care or are they always appreciative of the communication?

**Petr Dvorak:** I have to say that they are always appreciative about that. Great. Yeah, and it seems that they are somehow surprised by that approach because yeah, sometimes customer told me that yeah, we didn't used to communicate with the designer so much and it didn't work so well as with you and yeah, so I think it's granted almost all the time but frankly I can't remember now an example of customer that didn't want me to communicate as much. they then feel involved in the project they feel informed they feel that they are in charge of the project not like the passengers in the second floor.

**Chris Gammell:** Got it. You know, I have had that I think it also depends on the type of client too because it sounds like if you're working like within a team and maybe there's firmware people involved whatever that sounds like that type of client in my past definitely they want to be involved right? They want to be like well actually that pin shouldn't go there and why isn't this LED here I expected an LED here that sort of thing that's a great client where they are involved other times I've had ones where more hands-off they're like I just need the thing like it's like they were hiring me because I'm doing more of a like a first prototype type of thing and they would they would have much rather been able to buy it off the shelf but they were not able to and they're like just make it so that it's like I'm buying off the shelf and I'm buying it from you you know that sort of thing and so that's that's a little bit different because they're more like high level instead of like how

**Petr Dvorak:** something similar to me my typical customer is even freelancer who hire me for a lower price than they invoice to the end customer or small companies without a hardware development team and they need to design something or yeah yeah

**Chris Gammell:** you're like the you're like the embedded embedded like embedded electronics but you're like embedded in the team right you're like the special agent yeah

**Petr Dvorak:** exactly because yeah we need to understand that big companies don't hire freelancers the big companies want to work with companies at least small companies because of some processes some things around I don't understand even but freelancers want to work with freelancers because we are at the same level like you can imagine the ISO model of communication we are at the same level so recently a customer from here from Europe told me I'm very happy that you communicate with me because in the past I always asked a company hardware development team and they told me we know better than you let us work and don't ask anything but now he's involved and he's happy that he is in charge as I said

**Chris Gammell:** yeah no I think you're right and I think that that is a certain flavor that different types of clients are looking for like you're saying that that person is very appreciative I feel like aside from just the overhead aspect of getting into someone's approved vendor list and all that kind of stuff the thing I don't want to do is talking to a larger product development shop as much as I like them the thing I don't want to do is be like oh now we're going into a planning meeting and this is going to be another four hour process so just give me that thing and I'm sure someone like you could just be like okay let's just sketch it out and do it real quick and communicate it over time

**Petr Dvorak:** yeah definitely yeah

**Chris Gammell:** that's great

**Petr Dvorak:** so yeah those are my customers yeah cool

**Chris Gammell:** what about your so you also have Benny devices is that how you say it yeah

**Petr Dvorak:** Benny devices Benny the cat

**Chris Gammell:** exactly

**Petr Dvorak:** exactly Benny is our cat and I wanted to give her the like Benny is somebody says that Benny is male for a male cat yeah but our cat didn't have anything against the Benny name and I wanted to give her the fame the fame yeah almost the fame so I call it against according to her the project Benny devices and yeah

**Chris Gammell:** I wanted to call out the A to Z of hardware design because first off it's a PDF people can go download it's free you can go sign up we'll have a link to that in the show but it looks like you made this book this ebook in keycat is that is that fair

**Petr Dvorak:** yeah yeah I did I did I said

**Chris Gammell:** yeah

**Petr Dvorak:** yeah I'm happy to hear it from you because it was like kind of a joke yeah why not to write a short ebook about the keycat in keycat because it was written in I think version 7 after the release and it offers a very good work with fonts and formatting and anything and I said to myself oh why not it would be fine

**Chris Gammell:** I think just from a branding perspective I open this up and I'm like I know exactly what this is I guess if you're brand new to keycat you'd be like I don't know what this is but I open it up and I'm like oh I know how this was made you know

**Petr Dvorak:** yeah yeah yeah yeah and it it saves it saved me a lot of time because I didn't need to export some graphics from yeah the keycat to some I don't know graphic software desktop software and back and forth and that so I used some examples directly in the keycat and even without export they work and they are like living I kind of expected that some reader would ask me for the source code for the book and I would deliver I would I would send it to them but

**Chris Gammell:** you say it now you say it now and yeah you know you got a bunch of listeners you might get a couple requests now

**Petr Dvorak:** probably why not why not I'm 100% open to anything that I yeah why to hide anything we are here in this world for a while and yeah

**Chris Gammell:** share share the other thing I think that's nice about this generally just from a you know when you're doing a book too right I always love like markdown formats for doing documents and stuff like that just because it's like so revision controllable and same same with keycat here you I'm guessing you have this in github or similar and you can just update it as you need to you know something changes something someone puts out a mistake whatever you just go yep now we're in version 3 you know

**Petr Dvorak:** exactly the keycat is great that all the files are textual you can edit them you can version control them you can do anything with them like they are texts

**Chris Gammell:** so it's great how do you do that with clients are you doing just github or gitlab or similar

**Petr Dvorak:** sometimes when they want me I push the work on their github repository but it's very rare very rare I don't know why probably the github and the version control systems github github and other are I think still connected more with the software than with the hardware but I don't know okay

**Chris Gammell:** yeah the thing that I need to hook up for that sort of stuff is the and I think they're working on this in future versions of keycat too is the generative like click a button or like upload a new rather I'm working on a schematic I do a commit I push to github rather and then it does like back-end processing where it spits out or maybe I tag the tag the revision and then it spits out on the manufacturing files like there are a lot of people doing that I've not personally done it but I need to do it just because that standardization is so nice whereas I'm like oh you know I output the Gerbers but I forgot to generate a schematic and it's like that kind of level of automation where if it is automated it starts to become

**Petr Dvorak:** for the PCB part so-called active plugins that they can be connected with your github account and they help you with pushing or committing the work on there but I tried I didn't succeed with successful setup I'm not a plugin and software extensions guy I need my software vanilla because it helps me to keep it up to date without additional work with like looking for reason why the plugin stopped working after the update and anything right like getting

**Chris Gammell:** kind of like dependent upon it sort of thing

**Petr Dvorak:** yeah so I still use the command line for the git I use the lazy git it's called like application for command line which is like graphical command tool I recommend lazy git and it helps me a lot

**Chris Gammell:** that's great too because that's what a Brit would call someone derogatorily right don't be such a lazy git yeah yeah oh that's cool oh wow it's like a terminal windowing kind of thing exactly exactly

**Petr Dvorak:** it's a window like tool but for command line it's bloody fast and yeah it offers anything you need yeah it supports all the git functions so yeah you are not limited to that

**Chris Gammell:** yeah I like that too because like I when I got started with git stuff it was all like github for windows and stuff like that and they try and basically you said you know it's a tool where you're it's graphical but then you're you're more dependent on this third party tool on top of the actual underlying git thing and it's like then I was very confused what was going on and didn't really learn it and I feel like it's also not portable like if I'm on someone else's machine but lazy git you could always just go and install and install have access to it yeah nice

**Petr Dvorak:** yeah the same the same to me I I know that there is official github graphical application but I don't know how to use it properly yeah yeah no I'm probably I'm getting cold I don't know

**Chris Gammell:** yeah me too every day every day I think one of the elastin tool was really helpful for me I forget what the elastin tool is called but it was helpful for me to have like the if you're actually working with a team that has like a bunch of branches and like merges back in like having something like that but there was another command line thing it's actually just a script that you'll run on top of git called git lol like laugh out loud and that's another one where it's just like two lines and then it just formats your git output and that also kind of helps with the trees and visualization and stuff again I'll put stuff in for all of these links we're talking about here but yeah I think it's tough at the beginning when people are you know if they're not coming like I came from the hardware space I was very confused at the beginning but over time I've gotten better with it you know yeah it's surprising to me like you said though like the the fact that they don't that clients don't care about this so then you just kind of maintain the repos for them over time

**Petr Dvorak:** no no I don't if they don't have any repository I don't control I don't maintain that for them and no

**Petr Dvorak:** just

**Chris Gammell:** zip it up send it to them all done I think

**Petr Dvorak:** yeah yeah

**Chris Gammell:** okay sometimes

**Petr Dvorak:** sometimes my customers are not very into having project files they are asking only for gerbers but I deliver always always everything project files you're gonna

**Chris Gammell:** want this later when you call me again I'm gonna be mad if you don't have this so yes yes

**Petr Dvorak:** exactly

**Chris Gammell:** what are the nature of some of your customers I mean so we talked a little bit about the type of work you like to do and whatever but like what industries are they normally in

**Petr Dvorak:** communication devices so home appliance not appliances like smart smart home things I think we can say IOT of course anything these days is IOT it's like buzzword almost but yeah IOT communication and control devices for instance I designed some control boards for electron microscopes I live

**Petr Dvorak:** in the city of Brno in Czech Republic and we are like kind of city of electron microscopes there are really yeah in my in my city is almost I think 30% or maybe 50% of the worldwide production of electron microscopes is being made in my city so there is a lot of companies producing things and tools for them so for one of them I worked on a few projects and then yeah some smart home tools slow control I don't know some 20 amps DC motors I think controlling some some window blinds or something then

**Chris Gammell:** really really big window blinds I'm guessing

**Petr Dvorak:** yeah yeah some huge huge there was huge transistors in bridges and yeah

**Chris Gammell:** wow that's cool so on the electron microscopes I think real quick do you get a feel then for like I know people use old electron microscopes and I watched videos of people using like Ben Krasnow and Adam McCombs who's on the show like they're they're always using old ones do you have an idea of like what is what is the new hotness in electron microscopes I don't I don't actually know anything about them other than the videos I watched

**Petr Dvorak:** yeah the fact is that I had worked in a company producing electron microscopes between 2008 and 2014 so I put my hands on almost all kinds of microscopes that company produced so even high-end models with price tag more than one million dollars a piece so very high end with resolution below one nanometer or even one-tenth of nanometer those microscopes were able to see the atoms of some materials so yeah

**Chris Gammell:** so what is changing though so is it like the acceleration like the electron volts is going up higher is the detector is getting better on the

**Petr Dvorak:** exactly the acceleration voltage quality goes higher because there must be no noise definitely no noise even in the voltage and there is not only the high voltage for rough acceleration there are some auxiliary power supplies to deflecting the beam or shaping the beam yeah and you need to control the beam you need to focus the beam with some special like lenses in quotes they are not lenses like electromagnetic lenses or electrostatic lenses even big

**Chris Gammell:** magnetic magnets or what what actually does that

**Petr Dvorak:** yeah big coils with special core or the most precise microscopes use electrostatic deflection so not not electromagnets but electrostatic like desks electrodes yeah yeah yeah you can imagine the old analog oscilloscopes the CRT tube in those oscilloscopes where the beam was deflected electrostatically no electromagnetically I didn't know that yeah okay it's much much faster much much more precise and yeah

**Chris Gammell:** and I guess from a physics perspective too it's like it's like a big bucket of electrons sitting there opposites attract same repel so basically because you have a plate of electrons sitting there the beam of electrons wants to kind of bend away from that is that the idea

**Petr Dvorak:** yeah yeah it's the idea and you mentioned correctly the detectors yeah it's a big part of the modern electron microscopes are the detectors because there are numerous types of signals you can detect like I don't know the terminology anymore but like so-called I think the primary electrons the back scattered electrons the secondary electrons yeah so you can detect even the multiplex scattered electrons in the chamber and you can then accelerate the back scattered electrons so the detector can suck the back scattered electrons to their sensing area where they count it and or even there are some very special detectors I think developed in Geneva Switzerland in CERN they can count particles wow yeah

**Chris Gammell:** the particles not like uncharged but yeah yeah or like just individual electrons

**Petr Dvorak:** individual electrons and even they are able to mark the timestamp of each particle yeah so you can imagine that there is a big science behind it

**Chris Gammell:** yeah I feel like I could you know like how there's like this I have like these mental models of how this stuff kind of works and then I think about it I'm like I have no idea how this works yeah I'm like I looked at an electron in physics class you know

**Petr Dvorak:** yes I was in the I wasn't in the development team to be honest I was in the product engineering called group like between the development and the production so but it was a great experience because I know what the manufacturing group needs and what are the outputs of the hardware design group and how to manage the transition yeah because not every project coming from the hardware design group was completely finished so we need sometimes we needed sometimes to finish it for the serial series manufacturing and to support guys in the production because we needed to write some procedures some guides for the manuals and everything so I put my hand on a lot of things it

**Chris Gammell:** sounds like you and I have a very similar path honestly because I also I mean basically I think I'm like hearing this I'm like oh Petter is at a test equipment company in 2008 until 2014 basically I was doing the same how

**Petr Dvorak:** old are you I'm

**Chris Gammell:** 40 now

**Petr Dvorak:** I'm 43 this year so I'm very similar nice to hear

**Chris Gammell:** you've got your LinkedIn that's like a podcast for you we're just like electrons that are in the same path

**Petr Dvorak:** exactly that's

**Chris Gammell:** great so how do you like the more unstructured consulting world versus that more structured at the job how did you switch over

**Petr Dvorak:** like from the company world to freelancing world you mean

**Chris Gammell:** that's right yeah exactly how did you build up from you know like one of the things I liked about the company world was just like someone walks in like hey here's the new project go dig into this and it's like technical requirements go learn it go do it whatever and it's handed to you versus more the freelance world is like I'll go and see what's out there you know and I have to build my name and that sort of thing because I think a lot of people listening as well might be in that first stage that working for a company and want to get into the freelancing stage and talking about that transition is yeah

**Petr Dvorak:** the transition was not easy definitely I started with looking for potential customers even when I still working on as an employee so I find two customers because in my country there is some law that you have to work on more than one company as a freelancer otherwise it's a bit yeah

**Chris Gammell:** being abused as an employee kind of thing yeah exactly yeah that's the same it's less enforced here but it is same kind of idea like in the US it's called a 1099 some companies want to pay everyone like they're a freelancer yeah then there's the ABC test of like yeah well you're only working for this one customer 40 hours a week you are an employee and there's a bunch of other regulations

**Petr Dvorak:** exactly exactly this is the same reason here in the Czech Republic so I looked for those customers I found and at the end of the year I quit my latest job and up in the morning and started working and procrastination you and I

**Chris Gammell:** now diverge the electrons have diverged

**Petr Dvorak:** it was it was expectable that we are not the same so to me it's not very issue to work since the I don't know 7 a.m to 16 to 4 p.m so I started working for those two customers and as I started working as a freelancer I started building my so called personal brand on LinkedIn I didn't know why I didn't know it will be beneficial but I started

**Chris Gammell:** you didn't follow a lifestyle blogger who told you you should be doing it I read

**Petr Dvorak:** a book by Austin Clion Clion called Show Your Work and he advised to blog about your job every single day or regularly at least to show people what you are doing and to let him know what you are doing and what your output so I started posting blog posts on LinkedIn every single work workday I

**Petr Dvorak:** I I

**Petr Dvorak:** I I didn't stop for for a day really yeah that is yeah yeah some guys as active as I on LinkedIn said we deleted more posts than some people even ever written so it's a it's true sometimes but it's I don't want to sound rude to them but yeah I am pretty active on LinkedIn it took me I think almost three years before I got the first job on LinkedIn like using yeah

**Chris Gammell:** but

**Petr Dvorak:** since then since then it started working and yeah

**Chris Gammell:** see now this is always the thing I talk to people I'm like look you want to become a freelancer consultant whatever right like you need to if you want to do the content path right I would call that content path that's great like Petter said like three years to actually then I'm saying like three months six months to even get people to start noticing and it's just the consistency that does matter and so yeah first off super impressive that you were just able to keep that going because that is it's tough it's like shouting into a void right I mean it's like basically shouting into the void people like see it later and they're like oh well Petter has been doing this forever so he must be so good at but it's like you have to start at the beginning I think the big thing that's important for for my sanity and I've tried to keep this going for a long time is that nobody cares at the beginning you know like you know like so like having that in your head and it's reminding myself that because it's easy to get locked up and be like oh well what if what if everyone sees this well nobody's going to see it exactly so just post anything you know like that's

**Petr Dvorak:** exactly exactly that you hit the nail again it's a big helper if you if people realize soon that they can they can write anything they can they can making making videos about anything they can stand in front of the camera and publish anything because nobody would see it would watch it and would comment it and they have unique opportunity to learn before being popular or famous not famous in a way well known perhaps

**Chris Gammell:** prolific for sure you're very prolific and by the time people do start paying attention and you're well practiced ! People want

**Petr Dvorak:** the perfect result very quickly very soon but sometimes it takes 100 posts before you get your first viral post but you need to write the 99 posts before you can't start with the viral post well

**Chris Gammell:** with all these algorithms so I could imagine someone getting started trying out going on TikTok making a short video about something electronics related that they want to have to talk about and hopefully promote future work and maybe the algorithm does reward it for some unknown reason that could be more detrimental than anything because then you're like oh my god 500,000 people saw this and I need to make it perfect for the next time and the algorithm doesn't care in the future it's like this genie in a bottle that you just don't know about

**Chris Gammell:** that is almost

**Petr Dvorak:** it took me three years it's true probably I could be faster but yeah I didn't know how to be faster so I was consistent and it pays off it paid off how

**Chris Gammell:** do you keep it going now I mean as you do get more work now I imagine it's tough to keep that up

**Petr Dvorak:** I keep having a window in my calendar each week there are like two or three hour window in my calendar usually Friday morning in the past it used to be on Sunday morning but my wife was against that so yeah so I want to write five at least five posts a week because yeah to be sustainable to to keep the process sustainable I need to to write five posts a week to be able to publish five posts a week so sometimes I write four sometimes I write seven so it works and usually I have about one month buffer I use some oh my god

**Chris Gammell:** yeah okay another time we diverge that is so impressive one month buffer one month

**Petr Dvorak:** with my post yes

**Chris Gammell:** wow

**Petr Dvorak:** today today I prepared posts that will that will be released in a month yeah at the end of June

**Chris Gammell:** I am so impressed right now like that is so impressive to me wow

**Petr Dvorak:** I'm organized freak but yeah it helps me it helps me to focus on other things when I design not to distract myself with some blogging some yeah

**Chris Gammell:** yeah yeah yeah well when you are thinking about making a new ebook in the future if you could instead just teach me how to do that instead of key cad I would be really appreciative how Chris could organize his life I don't know if there's any help there for me yeah

**Petr Dvorak:** it's a 1 million question 1 million question yeah I don't know if anyone can learn this habit I think it's some kind ! of nature but there are some famous authors of books about procrastination and how to manage your time and how to manage your work I've read

**Chris Gammell:** many of them and ignored them all I'm prolific in ignoring the advice

**Petr Dvorak:** so do I so am I

**Chris Gammell:** yeah

**Petr Dvorak:** that's great

**Chris Gammell:** what about the I mean so like one of the other things I think about is like the fact that you're getting tons of repetitions and all this stuff too right you're building the work obviously you're doing I always kind of think about building up skills like layout and just building electronics it's like going to a gym it's like working out consistency matters same with content consistency matters that sort of thing if you were talking to someone who was at a company looking to then start building like you did how do you recommend that they kind of build reps like repetitions I guess to get their PCB stuff up as well

**Petr Dvorak:** yeah the repetition and there book of Max Gladwell I think 10,000 hours the book is called Outliers but yeah we need to build a skill anything is a skill force in the gym is a skill it's not it's not something anything different so we need to work on the skill as a PCB layout is a skill and anything different is a skill so yeah to be consistent sometimes not sometimes quite frequently I got questions on LinkedIn in messages from some beginner engineers or even students how to become the electrical engineer and how to be successful and I always answer pick a project work on it learn something because the issues will come and you need to fight them so and then finish the project and pick another one and this is the best way how to learn something but they think that I am making fun of them but it's not true they sometimes ask me for book recommendations they think that in the books there is knowledge but it's not the case in the books there are informations and you need to extract them and create the information and create the skill and create the knowledge in your brain and then to work on it so be consistent

**Petr Dvorak:** I don't know expected there's no magic bullet

**Chris Gammell:** basically right exactly there is

**Petr Dvorak:** no magic bullet you need to work I have

**Chris Gammell:** thought about that before too of like almost like what people are almost asking there not necessarily I've thought about this from my course too it's like sometimes it's people are just saying just give me the project right like and I feel like that is potentially part of the problem but they nudge right of just like hey go check this out what if you built this what if you built that you know it's like almost like there needs to be a list of like that I think Dave always talks about power supplies or like active loads I makes people want to deliver the end product I feel like that's kind of a key thing too but yeah it is tough because I think when people are messaging on LinkedIn like that they're really saying like just show me show me sensei you know tell me tell me what to do because I think a lot of the traditional school infrastructure too it's like no no student go do this ! you have this assignment and then when you're outside of that infrastructure you know what do I do next you know

**Petr Dvorak:** definitely and I can't add more because almost every time the next question after the question as I said how to become a successful engineer is what project should I work on and I said to them you are I don't know you are a student you are an ! so you need to be their guide their teacher and to be their guidance but I am not a good teacher in that way I think everyone needs to know what they want to work on because otherwise I don't know

**Chris Gammell:** one thing that I tried to tell students in the past and stuff like that too is it like it it sometimes really helpful to have constraints so like even so like doing work for someone else might be helpful because then they're going to tell you well the end product has to cost less than $30 and you know basically they're going to be kind of like a customer or something like that so just anything that puts constraints in your project is useful because one of the problems I found as well is like if you have limitless constraints then someone's like well I could just throw this Vertex 7 FPGA out here that's a $400 part you don't want to do that it's not a realistic thing and then it's also not challenging for one reason but it's not challenging in the way that's actually going to teach you a lot of the skills that they really are asking about learning I

**Speaker ?:** feel like

**Petr Dvorak:** 100% the constraints are extremely helpful to support your creativity because not the creativity in a way that you can use any microcontroller any FPGA but for instance I worked on a project in the first company I started working as a freelancer and we needed to display something on a matrix display with very low resolution like 8 pixels times 32 pixels very small and we needed to find a way how to deliver the information to the user what happens on that very small display and it ignites a lot of creativity because you need to find a way how to use the small playground to deliver the information if we wouldn't limit it we use for instance some big LCD panels and I don't know what

**Chris Gammell:** but right exactly like a Linux machine where you're like putting OpenGL on there and create stuff and it's like okay yeah then you can do anything and then you get locked up in a different direction and it's not realistic in the end anyways

**Petr Dvorak:** yeah so constraints are really helpful and probably I can't remember being a beginner but I want to be a beginner for my entire life but I would like to be in their skin when they don't know what to work on but I still believe that they should have some hobbies some interests some things that excites them so

**Chris Gammell:** would you actually want to be back in that position I hated that position you hated

**Petr Dvorak:** the position to be a beginner

**Chris Gammell:** I mean like I like beginner's mind like that I like the curiosity and the excitement piece but like that you know like that like squirmy like I have no idea what to do like do you like that feeling yeah I

**Chris Gammell:** know I I like I do like it yeah I do like I do like I love to

**Petr Dvorak:** I love to be to to suck at something because it's so it's so refreshing so it's it's a great feeling that you you you don't need to deliver the perfect result you just need to progress on it to be to improve yourself from day to day and in the early phases of learning anything there is a very steep learning curve and you you can feel the progress every single day once you are expert you don't know if you are better than you was one year ago it's not it's very hard to compare but you're

**Chris Gammell:** making sense again I don't like this man that does make sense yeah you're right because it's like you get all of these dopamine hits because you're like oh my god the you art started working versus like oh my god I need to improve the battery 2%

**Petr Dvorak:** yeah exactly for another area for instance I spent two weeks at my customer in Shenzhen China like last month and three weeks ago I started learning Mandarin Chinese

**Chris Gammell:** really yeah

**Petr Dvorak:** because without any Chinese language skill you are completely lost even in the big city of Shenzhen almost nobody speaks English and you need to communicate somehow so I started learning this extremely difficult language and using Duolingo I know already about 50 words so it's nothing but I can feel the progress every single week and it's so exciting to be beginner in that area so and I think it's very similar to our engineering stuff or hardware development stuff

**Chris Gammell:** yeah okay I'm with you on that side of thing I have been doing Spanish for two years and I will agree that it was very exciting in the beginning and very it's very plateaued now right I'm learning like new verb tenses and things like that and it's like okay you know and I need to get better at it of course yeah but like yeah okay I'm with you again I'm with you again I will say on language nothing accelerated me faster than using like a tutor oh man so much like you know slow progress Duolingo other resources whatever with Spanish and then I did I did six months with a tutor in another country it was like a good geo arbitrage type of thing I wasn't paying a whole lot per hour and in six months I accelerated so much oh my gosh definitely

**Petr Dvorak:** definitely yeah

**Chris Gammell:** well that's very exciting to know that because I mean that'll that'll unlock a lot of stuff for you if you go back for future trips and stuff in Shenzhen

**Petr Dvorak:** yeah I strongly believe I will get back in August or September okay because yeah my customer there wants me to help them and I will be happy to spend some time there because it was a really eye-opening experience to me I didn't expect anything like that in Shenzhen it was

**Chris Gammell:** a scale of manufacturing or what about it

**Petr Dvorak:** the level of technology the level of yeah before I I traveled there I had the silly questions like to my wife even I asked her do you think that I would be able to walk there in the city or yeah I didn't expect that it's like very high-tech oh yeah all all equipped city with all the companies technologies mobile applications oh yeah I would be completely

**Chris Gammell:** out of my league completely out of my league

**Petr Dvorak:** yeah and we in the European Union we are sometimes I think more than 10 years behind them when comparing with Shenzhen Shenzhen is not China I know but yeah

**Chris Gammell:** I mean it is part of China but it's not

**Petr Dvorak:** representative of the entire China this is what I meant yeah yes totally

**Chris Gammell:** yeah

**Petr Dvorak:** so I sucked at Mandarin Chinese and I liked it and each project I worked on I want to learn something new and even completely new because I hate repetitions like like routine yeah once I work on something for five time like repetitively I lose interest in that and I lose focus so I need to keep myself involved in learning because I don't know if it's like more esoteric or something but there is a Gallup five like top strength by Gallup company or I don't know how they say the first strength of me is a learner I feel it I need to learn something all the time because otherwise I don't feel like like like

**Chris Gammell:** you're making progress or enjoying yourself yeah totally does that mean are you at the point now in your career two where you're you're able to turn down like someone comes up to you and is like hey I just need like a couple relays and some LEDs on a PCB are you like turning that down because you're like I'm not going

**Chris Gammell:** learn anything it depends it

**Petr Dvorak:** depends on the on the customer definitely I wouldn't work on some very trivial things I can help them I can support them I can consult with them even for free but not like the entire project but yeah even even the one of the recent customers asked me if it's not too simple project for me and I said look there is no simple project there are only like standard or substandard ideas so I don't yeah and this is this project particularly was at my level completely yeah

**Chris Gammell:** I've talked to some people who are in management at design shops product design firms and stuff like that and one of the tensions I feel like especially when you're supporting multiple engineers who are on staff and being paid salary and stuff like that is that the best case scenario is actually that you do the exact same project every time right because then you know it's very predictable you know it's done you maybe there's some small tweaks back and forth but like it's basically you are a factory for a type of design output and that is in a similar way I feel very similar about that where it's like that is so boring you know it's so boring

**Petr Dvorak:** and I think the major project you work on repetitively and there is a plateau in development so no new things and you just maintain the project you get used to only successes I think

**Chris Gammell:** the other thing we should acknowledge is some people actually like that I really dislike sports that are like that where someone might be a golfer and go play the same golf course a hundred times and they really like trying to beat their last score and being just that much more perfect about it and I'm like I really don't like that same with bowling right they're like I want to bowl 300 every single time and I want to play the same classical piece more perfect than last time and I'm like nah man jazz play some soccer and work as a team and you have different constraints and problems to solve for

**Petr Dvorak:** yeah definitely definitely it depends sometimes we need success to be satisfied with ourselves sometimes we need failing to improve ourselves because the fail is something it can imprint the new knowledge inside of our brains because success don't do that at least not into my brain success is only ego booster but not learning rocket

**Chris Gammell:** yeah yeah well once again the electrons are aligned on this one so well we are past an hour now Petr where can people find you follow you learn more about your work learn more about how to hire you if they want to hire you download an ebook

**Petr Dvorak:** thank you thank you for that question my ebook my ebook is available to anyone for free it means zero cost on my benny devices dot eu website it is like central for so-called hardware design templates you will see just go there benny dash devices dot eu I believe there will be link below the video and in the bio and me personally you can find on linkedin i am there every single day for more time than i should be yeah but yeah i am there all not only long but every day so linkedin petr dvorak it is very common name in czech republic and you can use the profile petr dash dvorak dash hw like hardware and this is me so petr dash dvorak dash hw and yeah it's i think it's enough my linkedin is my top place

**Chris Gammell:** that's your go-to and people can follow you there and yeah see all your posts i was really enjoying those posts from shenzhen too like that

**Petr Dvorak:** sure that it will be interesting because i was not able to speak about the things in the factory of my customer because i wasn't allowed but i decided to deliver some interesting facts about the shenzhen because not many people were there yeah

**Chris Gammell:** yeah

**Petr Dvorak:** so i still haven't

**Chris Gammell:** been myself i need to go at some point i'm a little worried about global tensions and whether i'll get a visa but i would love to go at some point yeah so yeah all right well peder thanks so much for being here i'd love to have you back sometime and chat some more about this stuff and you know future versions of keycat and hearing about what you're doing so keep it up you're doing a great job

**Petr Dvorak:** thank you for having me it was an experience hour and keep designing see you soon

**Speaker ?:** in in
