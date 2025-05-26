# Day 97: Community Highlight - Byrn Baker

## Objective
In today's challenge, we will hear the story from community contributor - Byrn Baker. We will hear how Byrn was introduced to Nautobot, discuss the features he used the most, gather his recommendations for newcomers, and discuss best practices for community interaction. 

## About Byrn Baker
Byrn is a network automation engineer with over a decade of experience in telecommunications, starting as a cable technician and progressing through various roles in NOCs and engineering. 

His initial exposure to Netbox (the predecessor to Nautobot) was driven by the need to manage and track a large number of "settlement-free peering" circuits, which were previously tracked using spreadsheets. This demonstrated the early value of a structured database for network documentation.

Byrn's transition to network automation and deep engagement with Nautobot was driven by a need for a more robust solution than spreadsheets and his natural inclination towards hands-on learning.

## Q & A with Byrn

1. To start, can you tell us a bit about your background and how you initially got involved with Nautobot?

**Byrn**: Yeah, sure. My background is primarily in network engineering. I've been in telecommunications since about 2000, starting out as a cable tech installing cable in homes for about 10 years and transitioned to a NOC in 2010. 

I moved into a NOC role at the same provider and worked through various NOC and engineering titles. Before Nautobot, I was actually using NetBox for documentation. I noticed Nautobot and started using it because I was like, "Well, what's the difference?". What I really enjoyed and appreciated about Nautobot was that the whole point of it was to make it the source of truth and integrate it into automation. That made a ton of sense to me. That started me down the path, and I did that Ansible workshop which kind of incorporated Nautobot into it. So, that was my foray into using Nautobot.

2. You mentioned starting with pretty much zero comfort level with the Nautobot API and automation. How did you approach learning something so new, especially with a limited coding background?

**Byrn**: My comfort level was absolutely zero. I came from a networking background and wasn't a Python programmer. I'm very much a doer. That's how I learn how to do stuff. I'll sit here for hours at my computer typing in different things trying to see like what works, what doesn't work. I'll type it in, hit the enter key, and run it to see what happens and read the traceback. It seems like that's just better for me to learn that way. 

It took me a long time to understand this, but tracebacks aren't lying to you; you just need to understand what it's telling you. That's the difficult part. Doing this over and over is how you kind of pick that stuff up eventually.

3. Building on that, when you hit a wall or encounter a traceback you don't immediately understand, what's your typical debugging process? Do you try to dissect it alone, or go to the community early?

**Byrn**: When I was learning the stuff for the Ansible workshop, it was hours and hours of just kind of banging my head against the wall. My primary way is still by doing – sitting at the computer, typing things, hitting enter, and reading the traceback to see what happens. You look at enough tracebacks, and you probably pick out the most important part and zero in on that. But there are definitely times where I just don't know the answer. Sometimes I could Google it, but sometimes you don't really get the answer you need. That's where I go to the community.

4. Speaking of the community, you mentioned asking a lot of questions in the Nautobot Slack channel. How important has the community been in your learning process, and what value do you find there that you don't get elsewhere?

**Byrn**: The community has been huge. It's a great way to just kind of get a quick answer if you're looking for one or at least get pointed in the right direction. Sometimes Google doesn't give you what you need. Also, you can't be afraid to look dumb. I ask a ton of dumb questions sometimes. When I was first starting, especially with things like nbshell, I had no idea how to navigate that thing because I was brand new to Python and all this stuff. I had tons and tons of questions – how do I navigate it, how do I display fields, etc. I didn't even know where to look sometimes. The community helps with those kinds of fundamental questions.

5. For someone asking questions in the community, particularly when they are stuck, do you have any recommendations on how to ask effectively to get the best help?

**Byrn**: Yes, I think it's important to not be a jerk. When you've got a question, I think what's best is to do your best to explain what you're trying to do and provide examples of what you've done that didn't work. That's pretty helpful most of the time. It helps people understand what you're saying, and it could be that you're just going down the wrong road. If you can't provide examples or help somebody understand how you're thinking about it from your perspective, it's difficult to help. Being verbose about how you came to a conclusion also helps. Don't omit important stuff. Provide a little more information. And if you think you found a bug or have a suggestion, don't just complain in Slack, go submit a GitHub issue. Document it and provide feedback.

6. You mentioned challenges with nbshell as someone new to Python. Are there other specific hurdles or concepts that you found particularly difficult when first getting into Nautobot and automation from a non-coding background?

**Byrn**: Definitely coming from not knowing Python. Tools like nbshell where you need to understand Python to navigate them were confusing. Even things like reading documentation and looking at examples have a learning curve. Understanding what a traceback is telling you took a long time. 

Another example is understanding API interactions – like in Nautobot 2.0, if you try to assign an address that doesn't exist, the traceback tells you it's not found. Understanding that the message isn't lying, and realizing you have to create the address before assigning it, requires understanding how the tool works, which is different from the "old way" of just hitting a plus sign to get an address.

7. Beyond just learning for yourself, you've been very willing to share knowledge, creating videos and contributing to 100 Days of Nautobot. What was your motivation for wanting to share what you learned?

**Byrn**: I had picked up so much from other people sharing the stuff that they had learned. Sharing how they learn how to do things. It just felt like it was a decent way to give back to the community. A lot of the stuff I decided to share were things I was looking for. something very specific, and I couldn't find it. So, I made that video series kind of like, "I wish I could have found this". I thought, well, if I'm looking for it, there's gonna be other people looking for something very similar, and maybe that'll help them out. It's really just about that.

8. Based on your experience, what recommendations would you give to someone who is new to Nautobot, maybe also coming from networking with limited or no Python/Django background, on how to approach learning the project?

**Byrn**: For a very beginner, I would suggest you have an idea and see if you can make like a small piece of that functional. For example, wanting to track OSPF information with a device. Maybe you take existing code, like from another app, and add a field to the models.py and see if you can get that to show up in the GUI. That's the kind of approach I took. It's about making small tweaks, making sure it runs, and then tweaking another piece. This is a fantastic approach. Don't give up just because someone says it's stupid. If you think it has value, it probably does.

9. Bringing new tools or automation practices into an organization can sometimes face resistance. Do you have any recommendations on how to get buy-in for adopting tools like Nautobot, especially open source ones, based on your own experience?

**Byrn**: Pick like a small, doable thing. An example could be what was covered in the 100 Days: changing a VLAN, adding a VLAN, shutting or unshutting a port. Those really simple things we do every day. You start with that and show, "Hey, look, look what we can do". Show how you can push perfect configs every time with no mistakes. Or push a button to shut/no shut a port. Then you can show things like setting up RBAC in the GUI, so you know who's logging in and shutting the port down. You can abstract configuration details out to people who maybe don't have deep expertise but know enough to push a button. Find a small project, demonstrate value, and then build on it. Show them they might do one thing fast with a keyboard, but they can't do a hundred at the click of a button.

10. You mentioned using Nautobot at work as your source of truth and managing many devices and VMs. Can you elaborate on some of the practical applications or "cool stuff" you're currently doing with it?

**Byrn**: We're doing some really cool stuff. The `100 Days of Nautobot` kind of gave me a kick in the butt to start doing some validation jobs. We validate things like the operating system matching what's in Nautobot and if required agents are installed. We're managing thousands of VMs and hundreds of physical devices. We use custom fields and other aspects to add quick fields to the GUI. We've just started using the jobs button, which I think was new for Nautobot 2. Going through that day in the 100 Days, I was like, "holy cow, we can make buttons!". Now I've made some buttons to push deployments from. I can build it all in Nautobot and then push a button to deploy it into production. It's really cool. I'm wrapping these jobs into our application.

## Contributions by Byrn

We want to thank Byrn for being such a great contributor and an awesome content creator

### YouTube Videos
- [Learn how to leverage Nautobot's GraphQL capabilities to dynamically query Nautobot from your Ansible playbooks](https://youtu.be/g4aMH_pGo0Q)
- [Nautobot intro/overview from NTC community member Byrn Baker](https://youtu.be/NzwbVsewcV8)
- [Learn how to leverage Nautobot's GraphQL capabilities to dynamically query Nautobot from your Ansible playbooks](https://youtu.be/g4aMH_pGo0Q)
- [Nautobot intro/overview from NTC community member Byrn Baker](https://youtu.be/NzwbVsewcV8)

### Contributions to the 100 Days of Nautobot Challenge
Byrn Baker has authored several days' tasks for the 100 Days of Nautobot Challenge:
- [Day 23 Job Tempaltes](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day023_Jobs_Templates)
- [Day 27 URL Dispatch for Jobs](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day027_URL_Dispatch_for_Jobs)
- [Day 33 Integrate Nautobot with Ansible Workflow](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day033_Integrate_Nautobot_with_Ansible_Workflow)

### Blogs

- [https://blog.byrnbaker.me/](https://blog.byrnbaker.me/)

### LinkedIn 

- [Connect with Byrn on LinkedIn](https://www.linkedin.com/in/byrnbaker/)

## Day 97 To Do

Explore Byrn's YouTube videos, check out his blog, and connect with him on LinkedIn.

Share your experience and insights on social media, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will be highlighting another community member, Dwayne Camacho. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+jst+completed+Day+97+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 97 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 
