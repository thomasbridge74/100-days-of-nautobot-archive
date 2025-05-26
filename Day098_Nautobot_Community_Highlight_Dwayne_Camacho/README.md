# Day 98: Community Highlight - Dwayne Camacho

## Objective
In today's challenge, we will talk to community contributor and author of multiple days of challenges - Dwayne Camacho. We will discuss his background and contributions in the context of the 100 Days of Nautobot Challenge and the broader network automation community.

## About Dwayne Camacho
Dwayne Camacho has dedicated his entire adult life, since 2000, to the U.S. Army, maintaining his background in communications throughout his service. Nearing the completion of his 26-year military career and aiming to transition back into a technical/engineering role after more than a decade in management, he found the `100 Days of Nautobot` challenge helpful in staying focused on studying network automation.

We discussed his upcoming transition, learning, "light bulb" moment, and his recommendation for newcomers to the project. Let's get into it! 

## Q & A with Dwayne

1. Tell us a little about your background and how you came to be involved with the 100 days of challenge and ultimately authoring many of the days.

**Dwayne**: I've spent my entire adult life in the US Army, enlisting in 2000. 

Before joining, I was interested in electronics and communications engineering in college and have stayed true to that communications background throughout my Army career. I've always been interested in comms but my true passion lies in networking. As I'm nearing the end of my 26-year career, I want to go back into a more technical and engineering-focused path, moving away from management, which I've done for over a decade. To prepare for this transition, I reached out to people who have transitioned out of the Army and that are currently working in technical roles to get some advice. One of those conversations was with DJ Howard, a longtime friend and fellow contributor to the project. I asked him what I should learn to prepare myself and make myself more marketable. That same night, DJ sent me a link to the `100 Days of Nautobot` challenge and suggested using it as my first steps into programming. I started the challenge as a way to keep myself centered on studying and explore network automation, which is something I really want to get into.

2. What were your contributions to the 100 Days in Nautobot challenge?

**Dwayne**: I started by making small grammar edits while working through the challenge myself. That part came more naturally, I guess out of habit, since part of my job is to "red line" awards, recommendations, and evaluations. 

As I progressed, my involvement evolved to shaping the approach and structure to training. Since training is a big part of what we do in the Army, I pulled from that strength and worked to make the content more understandable and digestible, especially from a new user’s perspective like myself.

Later on, DJ asked if I wanted to co-author some of the content. I remember saying yes excitedly, not fully knowing what I was getting myself into! He asked which two topics I was interested in doing. I chose Day 31 as I was already a bit familiar with the subject and then looked at Days 36 to 39. It seemed intimidating at first but saw it as a challenge and a great learning opportunity.

3. How did your extensive background in training and conducting technical information benefit your contributions to the 100 Days challenge, especially for new users?

**Dwayne**: Having deep experience with training and presenting complex, hard-to-digest pieces of information to people new to a field was very helpful. 

We’re constantly training on systems, processes, and concepts that may be completely unfamiliar or where people have varying levels of experience. We don’t expect them to master everything on the first day. That's why the "crawl, walk, run" method felt so familiar and relevant while working through the `100 Days of Nautobot` because of its iterative approach. In my opinion, building on a solid foundation is critical for long-term success, especially when learning new technology. I always say you should master the basics before diving into advanced topics.

I could easily empathize with the learning struggles and the areas that new users might not grasp. This understanding of how to teach is, perhaps, way more important than technical skill when it comes to learning.  It’s not about being the fastest typist in the CLI world; it’s about understanding what’s behind the command: the logic, the flow, and the concepts. These are the elements that truly matters when comes to effective training.

4.  Given your background was primarily in communications and network engineering, how did you approach learning Django and Python for the 100 Days challenge?

**Dwayne**: I started by reading through the code to understand the logic behind, what it was doing, and why. 

When I was writing Day 36, where we actually create a site, I fumbled through it at first, trying to understand it through the Django layer.The abstraction layer between Nautobot and the Django ORM helped, as I didn't have to learn Django in depth, just how to interact with it logically. 

Understanding Day 5, which was an introduction to the ORM, was a huge light bulb moment for me. It made me realize that at the end of the day, it's about objects and how to manipulate them. My approach was to figure out how to write Python code that incorporates Django language to create objects or modify existing ones. A major challenge was creating relationships between objects, for example Device to Vlan. I knew what attributes were required but I couldn't get the syntax quite right to make the connection.

5. You mentioned a "figure it out" culture in your work background. How did that philosophy influence your approach to learning and contributing to the 100 Days challenge?

**Dwayne**: In my work environment, there's a strong emphasis on a "figure it out" mindset. It's often the first response when someone has a question. While it might seem harsh, it really encourages self-reliance and initiative. The idea is that when you're on your own and the mission has to happen, you need to be able to rely on yourself. This culture instills a sense of pride in solving problems independently.

That mindset definitely shaped how I approached the `100 Days of Nautobot` challenge. I spent a lot of time reading documentation, testing, breaking things, and learning from my mistakes. But it's just as important to know to know when to temper down the ego and ask for help. At the end of the day, it's not about personal success but the success of the team and the operation.

6. How do you use AI tools, if any, like Copilot in your learning and coding process?

**Dwayne**: I think Copilot, and AI tools in general, are awesome but I use it sparingly. My goal is to understand the code myself, not just have it dumped by AI. I prefer to first try writing the code using tools like the `nbshell` and API documentation. I often test code in the `nbshell` first to see the output or errors before putting it into a Python script. 

When I hit a wall, like when i can't figure out why my syntax isn't working, that's when I would turn to Copilot. This approach of having the syntax down and knowing the basics first allows me to use AI to refactor and learn, almost like a senior-level pair coder, rather than just taking the code as is. I believe AI is supposed to make us more efficient but not completely replace or do the work for us.

7. What is your advice for newcomers approaching learning a complex system like Nautobot or network automation, based on your experience?

**Dwayne**: Focus on the macro skill of "learning how to learn". You have to make sense of it in your own head first. Focus on the big pieces or concepts, the "big rocks". The finer details like syntax, specific API methods, or filters can come later. If you understand that everything is an object and how the system abstracts queries, the specifics become easier. It's about having that foundational understanding and building blocks. 

Another approach that helped me is avoiding what I call “buttonology”, which means just teaching someone which buttons to push. Instead of memorizing steps, focus on why those steps matter. That way, when something breaks or behaves unexpectedly, you can actually troubleshoot the issue, and not just follow a how-to guide. 

At the end of the day, programming and automation are about solving problems. If you understand the logic behind what you're doing, the tools become much easier to work with.

8. You discussed the importance of understanding dependencies, like creating a device type before a device. How did grasping this concept help you?

**Dwayne**: Understanding dependencies was definitely eye-opening. For instance, realizing that you need to create a device type before you can create a device helped me understand the difference between creating, assigning, and associating objects and their attributes.

This concept is crucial because when you model things correctly, your work becomes both reusable and scalable. That’s the true essence of a source of truth. It doesn’t help anyone if we’re creating multiple instances of the same object — doing that leads to conflicts and configuration drift. Getting the relationships and hierarchy right from the start makes everything downstream more reliable.

9. What are your thoughts on open source, now that you've gained more exposure to it through Nautobot, Django, and Python?

**Dwayne**: Open source offers a solution to the vendor lock problem and licensing issues. However, just like everything else, a balance is needed. 

The cost isn't just monetary; there's a significant cost in time and personnel – how much time is needed to train people and whether they have the aptitude to learn it. You can't just throw technology at people and expect them to learn it instantly. 

Open source has the power to push boundaries and accelerate innovation, but the cultural and organizational shifts required to adopt it successfully, now that’s the hard part. It's not just a technical transition; it’s a mindset shift.

10. You recently applied what you learned from the 100 Days challenge to solve a real issue at work involving Nautobot prefixes. Can you describe that experience and the lesson you took away from it?

**Dwayne**: After a Nautobot upgrade, we ended up with hundreds of prefixes that were labeled "Cleanup". The goal was to reassign these to the correct, existing namespace based on their assigned tenant, which was a very manually intensive task. A colleague was trying to fix this with a Nautobot Job that used over 100 lines of code, making individual API calls to update each prefix. Using the knowledge I gained from the challenge and how to interact with objects and their attributes, I was able to write a Python script that did the same in less than 30 lines of code. 

From Day 65, I learned about efficiency and program scalability. For large enterprises, performance is crucial, and you can make code more efficient by returning only the related objects/attributes you need, like tenant and namespace, rather than everything. 

Going through the `100 Days of Nautobot`, I realized it's not about just completing the tasks, but taking those lessons and using them to solve real-world problems.

## Contributions by Dwayne Camacho

We sincerely appreciate Dwayne's significant contributions to the 100 Days of Nautobot challenge and the broader network automation community. 

Drawing on his background in the Army since 2000, where he stayed true to his communications roots, Dwayne truly brought a unique and invaluable perspective to the project.

## 100 Days of Nautobot Contribution
- [Day 31 Validate External Routes](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day031_Validate_External_Route)
- [Day 34 Design Future Sites Part 1](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day034_Design_Future_Sites_Part_1)
- [Day 35 Design Future Sites Part 2](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day035_Design_Future_Sites_Part_2)
- [Day 36 Design Future Sites Part 3](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day036_Design_Future_Sites_Part_3)
- [Day 37 Design Future Sites Part 4](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day037_Design_Future_Sites_Part_4)
- [Day 38 Design Future Sites Part 5](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day038_Design_Future_Sites_Part_5)
- [Day 39 Design Future Sites Part 6](https://github.com/nautobot/100-days-of-nautobot/tree/main/Day039_Design_Future_Sites_Part_6)

## LinkedIn
- [Connect with Dwayne on LinkedIn](https://www.linkedin.com/in/dwayne-camacho-7260b39a/)

## Day 98 To Do

Explore the contributions of Dwayne Camacho to the Nautobot community, post what you enjoyed about the days Dwayne authored, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress!

In tomorrow's challenge, we will be highlighting community contributor - Florian Loehden. See you tomorrow!

[Twitter/X](https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+jst+completed+Day+98+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 98 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot)