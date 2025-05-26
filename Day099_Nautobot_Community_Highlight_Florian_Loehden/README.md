# Day 99: Community Highlight - Florian Loehden

## Objective
Today we will highlight another community contributor - Florian Loehden. Florian has consistently participation and progress in the 100 Days of Nautobot challenge, notably for documenting his learning path through blogging, actively engaging with the community by helping other members, and for making direct contributions to the project code.

## About Florian Loehden
Florian Loehden is currently completing his Master's degree in Computer Science as a dual student in Germany, while also working in DevOps and network automation, where his company uses NetBox and Nautobot as a source of truth. 

He became involved with the Nautobot project and the `100 Days of Nautobot` challenge through his colleagues and his interest in integrating Nautobot in his project of the master thesis on network automation.

### 100 Days of Nautobot Challenge
Florian Loehden has been a key contributor to the [100 Days of Nautobot Challenge](https://github.com/nautobot/100-days-of-nautobot/blob/0ef713bca6111501313a42860919ea9369e1b356/README.md), a self-directed, guided journey for community members to build strong and consistent network automation skills using Nautobot. The challenge focuses on Nautobot Jobs and Apps, leveraging the unique position of Nautobot in performing network automation tasks.

## Q & A with Florian

1. You mentioned you came to the project from your colleague and you guys use both Netbox and Nautobot as a source of truth at work. So is that how you came to know the project? What are the challenges if we take you back to the beginning when you're just brand new with the project and the tools? I find a lot of people don't know where to start and that's part of why the reason we started the project.

Florian: Thank you for the opportunity. I am currently at the end of my studies for my master's in computer science, and I also work at Logicalis Connected here in Germany. We do a lot of things in DevOps and network automation. Because of my colleagues, I learned about the challenge on Nautobot, Nautobot Jobs and how Nautobot can be leveraged for network automation. I came across this challenge, so why not learn about Nautobot through this? I wanted to learn about Nautobot earlier,  because I wasn't familiar with it. </br>
I wrote my master's thesis in the field of network automation, and I thought about how I could integrate Nautobot or how I could make it interact with Nautobot. My colleagues are using Nautobot and told me it's a great tool. We are using it in a lot of projects. With this, I thought, okay, I have to learn about it first, and then I can integrate it. Having a network source of truth is important. We use Netbox and Nautobot in different projects. I got to know Nautobot basically as a documentation tool for documenting networks. And where our services are on which server, and which IP is assigned to which server. It was always a good way also to visualise that in the end.

2. Well, let me maybe I'll rephrase that question a little bit. So, prior to the 100 days of Nautobot challenge, what is the depth of challenge? What is the depth of knowledge that you have for maybe Django or Python or what was your level of comfort?

Florian: Before I started the challenge, I had already worked with Linux and built a website on Django and Python. The part in the challenge about Django was quite a nice reminder and took me a little back to that time. I did the tutorial and also built a system based on Django. I built a system for documentation, like a database front end. I know Netbox and Nautobot can do a lot more. I had a baseline understanding of Django. However, as someone who has more to do with backend and DevOps and not that much with frontend, that is where my knowledge ended.

3. I wanted to take you back in into the project on 100 days in Nautobot because that's why we're here and let me ask you this question of... what was the biggest challenge or at least one of the big hurdles for me is actually to how to fit everything in codespace. What was the biggest challenge for you when it comes to know source of truth?

Florian: Yes, one of the biggest challenges was resource management in a way that I'm used to having more resources available than the Codespace instance provided. This was a great learning. For example, we used Ansible in Nautobot in the first segment and installed Ansible in the containers. </br>
First, I had all the router containers running, even more than stated in the description, and the nautobot containers. However, with this, the installation of Ansible was not possible, and it crashed my codelabs instance. So I had to start only Nautobot first, install Ansible, and then start the router container (only two) and do the task with them. I also used containerlab and Kubernetes in my thesis, but never encountered those issues. I think I had to rebuild the environment 4 or 5 times. But this taught me how to handle the resources and build the environment.

4. Was there any challenge other challenge that you recall from the 100 days of Nautobot project and how did you overcome them?

Florian: Another big challenge was staying consistent. It is not easy. We all have constraints that limit our time, and on some days, I was also not able to do the challenge. The important part is keeping up again and not giving up. The mail reminder helped me. Maybe I also felt a bit guilty because of it, but it was good to keep track of which days I had already done and which I had not.</br>
Another important challenge was running into issues and understanding why I ran into those issues. The troubleshooting process is important with this. Sometimes, it wasn't about the task on that day, but one or two days before, and rebuilding it is part of the process. Failure is part of the process. The important part is not to get discouraged by it, but to look into why the problem came up and learn from it. With this, we can come out stronger in the end.

5. So I wanted to also mention that you know we mentioned a little bit about your contribution. So outside of the fact that you consistently post on LinkedIn having social accountability you also wrote blogs and I also saw you commenting other community member answering other people's question on Slack and encouraging other people to follow through the process. So so I want to summarize. So what are what are some of the you know contributions that you made that you see impacting other members?

Florian: In my opinion, it's great to help each other and go the way together. I learn a lot when I know that other people work on the same, and it's possible to talk with people about what we have just learned. Also, it is possible to reach out on a common platform like the Slack channel, where we can get answers fast. </br>
My first contribution was to fix the GitHub link in the Twitter and LinkedIn posts. It got pretty annoying always having to change it while making the post, and it was easier to change it once for all the days that were realised until that point than to change it every day. This was the first time I was able to contribute to an open-source project, and it is an easy way to get into the world of open-source contributions.

6. Yeah, totally right? So I think that's another good point that you brought up, but I want to elaborate a little bit more. is that you could contribute to project without you know being the technical expert right? I think that's what you did and I wanted to give you kudos what Florian did was he realized that in the Twitter and LinkedIn link that I pre-built it was wrong in you know a few ways but he was able to create like a poll request for a bunch of them and and correct them all at the same time. And as a result, you know, you show up as a contributor and you show up as it's all documented public and that built your own portfolio. So I think that's one of the maybe the unforeseen benefit that I saw from people who may not may or may not have worked with other open source projects that they were able to do pull requests, they go through the merge process, branching and just overall just communicating with other people in the different time zones.

Florian: In this challenge, I learned much more than using Nautobot and Nautobot Jobs and what I can do with them. The ecosystem of Nautobot is huge, and there is much around it. I also came across the Terraform Provider, and getting into that is interesting. 

7. What are some of the you know features or you know things that you saw maybe in your work maybe in your studies for your masters that you you think you'll be very helpful to include in Nautobot that you don't see today? Or even just the learning days right?

Florian: I came from experience in some field, so some of the steps felt too small for me. That depends quite much on the backgrond knowledge people have in the first place, because at otehr tasks I had to read a lot and struggled with it. But that is also the fun about it. We learn something new, but also refresh some of the old knowledge. </br>
In my case, I know some Python, but not for networking, so I also need to build up on that, like with the book you wrote!

8. Yeah. So I think you know, we're we're kind of toward the end of our conversation. I got a lot out of conversation. One of this is one of the kind of the thing that just popped up just during our conversation. was maybe we could do kind of a assessment and we we give you like this kind of sequential quizzes and say if you understand you know docker run if you understand docker compose and then this is like your level at docker if you understand you know a certain level of Django if you're doing that Django admin then this is your level so based on that then we'll give you like this graph and this learning map and to go through like each of the steps but I don't know if that's too ambitious or not but just just from our conversation. I think that's something I got out of.

Florian: I think that's a fantastic idea, but quite an ambitious task. If I can contribute something, I would be happy and honoured.

9. So before before we wrap up, I do want to ask you, do you do you see any additional challenges that Nautobot could address that was learned from the challenge? So I'll give you an example because you mentioned documentation right? So Netbox and Nautobot could always do documentation on your IPAM, on your DSIM, and on your other stuff. But was there anything new that you that trigger, you know, just during the during the the challenges that trigger you think about the new challenges Nabot could address that you did not know before?

Florian: A good addition to the challenge would be to leverage other tools in the nautobot ecosystem, like the Terraform provider for infrastructure provisioning and interacting with this through Nautobot in the Network. There could also be a part on interacting with virtual machines and clients.

10. So I wanted to ask you one last question on what is the the most frequently used tools or libraries when you're working with Nautobot?

Florian: That is also a bit about what I'm currently doing. The thing I have used the most lately is also related because a friend of mine built a [terraform provider for GNS3](https://github.com/NetOpsChic/terraform-provider-gns3). And that's why I also, in the end, thought, okay, why not? Leverage. Also terraform to interact with Nautobot. And with this, I came across the Go library of Nautobot. </br>
It's good to have an abstraction layer, so we can use the library instead of making REST calls to Nautobot, and we don't have to handle this all ourselves.  The same is true for the library for pynautobot.  It saves from looking at the different endpoints, or perhaps more Pythonic, you could more easily guess what this method or function does.

## Contributions by Florian Loehden

We sincerely appreciate Florian's valuable contributions to the Network Automation community and the 100 Days of Nautobot challenge.

He is always consistently post updated on LinkedIn, fostering social accountability, and never shy about sharing his knowledge.

### Blog Posts

- [100 Days of Nautobot](https://medium.com/@florian.loehden/100-days-of-nautobot-175915146de5)
- [100 Days of Nautobot - Advanced Jobs](https://medium.com/@florian.loehden/100-days-of-nautobot-advanced-jobs-c5433ffa1d00)
- [Nautobot Challenge - the basics of applications](https://medium.com/@florian.loehden/nautobot-challenge-the-basics-of-applications-4a4eab7a5d73)
- [100 Days of Nautobot — Advanced Nautobot Apps](https://medium.com/@florian.loehden/100-days-of-nautobot-advanced-nautobot-apps-451a378fa30c)

### LinkedIn
- [Connect with Florian on LinkedIn](https://www.linkedin.com/in/florian-loehden/) 

## Day 99 To Do

Explore the blogs by Florian and post what you have learned on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

For tomorrow, some final thoughts of the challenge. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+jst+completed+Day+99+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 99 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 
