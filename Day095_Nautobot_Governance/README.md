# Day 95: Nautobot Governance Best Practices

## Objective

Understand the best practices for governance in Nautobot.

- version control
- release management
- dependency management
- Licensing

## Governance in Nautobot

Nautobot is a community-based Free Open Source Software (FOSS) project sponsored by [Network to Code](https://www.networktocode.com). The Nautobot Core Team is responsible for the direction and execution of the code that gets committed to the project. Here are some key guidelines and best practices for governance in Nautobot:

### Governance Structure

1. **Core Team Responsibilities**:
   - The Core Team is responsible for the overall direction and execution of the Nautobot project.
   - They review and merge pull requests (merges), manage releases, and ensure the project's health and progress.

2. **Community Involvement**:
   - Nautobot encourages community contributions and involvement.
   - Users can submit GitHub issues for feature requests and bug reports.
   - Discussions and feedback are welcomed through GitHub Discussions and Slack channels.

### Project Structure

Nautobot components are arranged into functional subsections called _apps_. Each app holds the models, views, and templates relevant to a particular function:

- `core` - Nautobot core application functionality, base classes, and utilities.
- `circuits`: Communications circuits and providers
- `dcim`: Datacenter infrastructure management (locations, racks, and devices)
- `extras`: Extensibility features and augmentations of the core data models.
- `ipam`: IP address management (VRFs, prefixes, IP addresses, and VLANs)
- `tenancy`: Tenants (such as customers) to which Nautobot objects may be assigned
- `users`: Authentication and user preferences
- `virtualization`: Virtual machines and clusters
- `cloud`: Cloud models adaptation 
- `wireless`: Wireless models and adaptation

### Release Management

1. **Versioning**:
   - Nautobot adheres to Semantic Versioning (SemVer) strategy, which gives versions of the format `X.Y.Z`.
   - Major (`X`), minor (`Y`), and patch (`Z`) versions indicate the nature of changes.

2. **Release Schedule**:
   - One major release per year
   - Three minor releases per year
   - At minimum one patch release every two weeks or more frequently as needed

3. **Maintenance Release (LTM)**:
   - The last minor version of the previous major release train is considered a Maintenance or Long Term Maintenance (LTM) release.
   - Actively maintained until the next maintenance release is available.

4. **Deprecation Policy**:
   - Deprecation warnings and notices are provided to assist in transitions.

### Communication

Please reference to the `Community Involvement` section as well. 

1. **Slack**:
   - [`#nautobot` on Network to Code Slack](http://slack.networktocode.com/) for quick chats and discussions.

2. **GitHub**:
   - [GitHub issues](https://github.com/nautobot/nautobot/issues) for feature requests, bug reports, and substantial changes.
   - [GitHub discussions](https://github.com/nautobot/nautobot/discussions) for general discussion and support issues.

### Licensing

Nautobot is released under the Apache 2.0 License, which is a permissive open-source license. This means:

- Freedom to Use: You can freely use, modify, and distribute the software.
- Commercial Use: The license allows you to use Nautobot in commercial products without restrictions.
- Attribution: Any distribution of modified code must include the original copyright notice and a copy of the license.
- Patent Grant: The license provides an express grant of patent rights from contributors to users.

- Community Contribution: Being open-source, Nautobot thrives on community contributions. Users can participate in development, reporting issues, and discussing new features.

- Compliance Requirements: Users must adhere to the terms set forth by the Apache 2.0 License, such as including notices of any changes made to the source code.


## Day 95 To Do

How's your project going? Please feel free to post about the progress of the project. 

Alternatively, you can also post your thoughts about Nautobot's governance on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will discuss Nautobot Testing and Continuous Integration. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+jst+completed+Day+95+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 95 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 