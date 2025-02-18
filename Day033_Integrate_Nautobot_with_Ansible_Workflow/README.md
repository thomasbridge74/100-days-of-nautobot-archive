# Integrate Nautobot with Ansible Workflow 

- Integrate Nautobot as SoT to Ansible Workflow

## Environment Setup

The environment setup will be the same as [Lab Setup Scenario 1](../Lab_Setup/scenario_1_setup/README.md), below is a summary of the steps, please consult the guide for a detailed background if needed. 

We will follow the same steps to start Nautobot, you can skip `invoke build` and `invoke db-import` if you restarted an existing instance and `build` and `db-import` was already completed: 

```
$ cd nautobot-docker-compose/
$ poetry shell
$ invoke build
$ invoke db-import
$ invoke debug
```

Let's upload and prepare cEOS image and start Containerlab: 

```
$ docker import cEOS64-lab-4.32.0F.tar ceos:4.32.0F
```

For this lab we only needed the `bos-acc-01` devices: 

```
$ cd ~/100-days-of-nautobot/clab/
$ sudo containerlab deploy --topo ceos-lab.clab.yml --node-filter bos-acc-01
```

The environment is now setup for today's challenge.  

## Code

TBD

## Day 33 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). 

Go ahead and post a screenshot of the successful execution of the new job on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode` so we can share your progress! 

In tomorrow's challenge, we will enhance our operations job with VLAN changes. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/networktocode/100-days-of-nautobot-challenge&text=I+jst+completed+Day+33+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 33 of 100 Days of Nautobot, https://github.com/networktocode/100-days-of-nautobot-challenge, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot)  
