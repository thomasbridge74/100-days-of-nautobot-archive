# Design Future Sites (Part 1)

- Use Job to populate future site

## Environment Setup

The environment setup will be the same as [Lab Setup Scenario 1](../Lab_Setup/scenario_1_setup/README.md), below is a summary of the steps, please consult the guide for a detailed background if needed.

> [!TIP]
> If you have stopped the Codespace environment and restart again but found the Docker daemon stopped working, please follow the steps in the setup guide to rebuild the environment.

We will follow the same steps to start Nautobot:

```
$ cd nautobot-docker-compose/
$ poetry shell
$ invoke build
$ invoke db-import
$ invoke debug
```

Let's create a file for today's challenge. We can either do this via the shared directory or directly in the Nautobot docker container:

```shell
$ docker exec -u root -it nautobot_docker_compose-nautobot-1 bash
root@c9e0fa2a45a0:/opt/nautobot# cd jobs
root@c9e0fa2a45a0:/opt/nautobot/jobs# pwd
/opt/nautobot/jobs
root@c9e0fa2a45a0:/opt/nautobot/jobs# touch create_site_job.py
root@c9e0fa2a45a0:/opt/nautobot/jobs# chown nautobot:nautobot create_site_job.py
```

The environment is now setup for today's challenge.

This challenge will be spread out over multiple exercises and will be the content for days 34 through 39. Each day we will continue expanding on the code from the previous day.

Today we will begin with creating the necessary prerequisites that will be required to create a new site with all of its racks and devices.

As we have seen in previous lessons some objects in Nautobot have requirements that must be created before you can create the object. For example if you want to add a ROLE to a prefix when you create it, the ROLE must first exist in Nautobot.

We will be creating Roles for prefixes, a new Tenant, Vlans and DeviceTypes. We will be doing the DeviceType portion on day 35. This is the data we will need to for our creation methods.

```python
PREFIX_ROLES = ["p2p", "loopback", "server", "mgmt", "pop"]
TENANT_NAME = "Data Center"
VLAN_INFO = {
    "server": 1000,
    "mgmt": 99,
}
CUSTOM_FIELDS = {
    "role": {"models": [Interface], "label": "Role"},
}
```

Lets break down each section of this data. The first constant is a list of ROLES that will be created in Nautobot. We will need the `p2p`, `loopback`, `server`, `mgmt`, and `pop` roles so they can be added to objects we create, like VLANS, PREFIXES or IP ADDRESSES.

The next constant is TENANT_NAME which will be used to specify the name of the TENANT we will use to put objects of the POP site into.

VLAN_INFO is a key, value dictionary specifying the name and ID of the Vlans we will be creating for use in the Site.

## Create Prefix Roles

The first method we will be working on will be for create the Roles based on the strings contained in PREFIX_ROLES. Take note of the ContentType import and the ContentType sections of code in the create_prefix_roles method. We are making sure that we can apply these roles to PREFIX and VLAN objects later when we are building the site.

```python
"""Job to create a new site of type POP with optional parent site support."""
from django.contrib.contenttypes.models import ContentType

from nautobot.apps.jobs import Job, register_jobs
from nautobot.extras.models.roles import Role
from nautobot.ipam.models import Prefix, VLAN

name = "Data Population Jobs Collection"

PREFIX_ROLES = ["p2p", "loopback", "server", "mgmt", "pop"]

def create_prefix_roles(logger):
    """Create all Prefix Roles defined in PREFIX_ROLES and add content types for IPAM Prefix and VLAN."""

    # Retrieve the content type for Prefix and VLAN models.
    prefix_ct = ContentType.objects.get_for_model(Prefix)
    vlan_ct = ContentType.objects.get_for_model(VLAN)

    for role in PREFIX_ROLES:
        role_obj, created = Role.objects.get_or_create(name=role)
        # Add the Prefix and VLAN content types to the role.
        role_obj.content_types.add(prefix_ct, vlan_ct)
        role_obj.validated_save()
        logger.info(f"Successfully created role {role} with content types for Prefix and VLAN.")

class CreatePop(Job):
    """Job to create a new site of type POP."""

    class Meta:
        """Metadata for CreatePop."""

        name = "Create a Point of Presence"
        description = """
        Create a new Site of Type POP.
        A new /16 will automatically be allocated from the 'POP Global Pool' Prefix.
        """

    def run(self):
        """Main function to create a site."""
        # ----------------------------------------------------------------------------
        # Initialize the database with all required objects.
        # We will build on this in the coming days.
        # ----------------------------------------------------------------------------
        create_prefix_roles(self.logger)

register_jobs(CreatePop)

```

Feel free to run this code as we add to it or wait until the end. We are using `get_or_create` method throughout so we will not get any errors if the object has already been created.

Next we will add in the add Tenant portion

```python
"""Job to create a new site of type POP with optional parent site support."""
from django.contrib.contenttypes.models import ContentType

from nautobot.apps.jobs import Job, register_jobs
from nautobot.extras.models.roles import Role
from nautobot.ipam.models import Prefix, VLAN
from nautobot.tenancy.models import Tenant

name = "Data Population Jobs Collection"

PREFIX_ROLES = ["p2p", "loopback", "server", "mgmt", "pop"]
TENANT_NAME = "Data Center"

def create_prefix_roles(logger):
    """Create all Prefix Roles defined in PREFIX_ROLES and add content types for IPAM Prefix and VLAN."""

    # Retrieve the content type for Prefix and VLAN models.
    prefix_ct = ContentType.objects.get_for_model(Prefix)
    vlan_ct = ContentType.objects.get_for_model(VLAN)

    for role in PREFIX_ROLES:
        role_obj, created = Role.objects.get_or_create(name=role)
        # Add the Prefix and VLAN content types to the role.
        role_obj.content_types.add(prefix_ct, vlan_ct)
        role_obj.validated_save()
        logger.info(f"Successfully created role {role} with content types for Prefix and VLAN.")

def create_tenant(logger):
    """Create a tenant with the name defined in TENANT_NAME."""
    tenant_obj, _ = Tenant.objects.get_or_create(name=TENANT_NAME)
    tenant_obj.validated_save()
    logger.info(f"Successfully created Tenant {TENANT_NAME}.")

class CreatePop(Job):
    """Job to create a new site of type POP."""

    class Meta:
        """Metadata for CreatePop."""

        name = "Create a Point of Presence"
        description = """
        Create a new Site of Type POP.
        A new /16 will automatically be allocated from the 'POP Global Pool' Prefix.
        """

    def run(self):
        """Main function to create a site."""
        # ----------------------------------------------------------------------------
        # Initialize the database with all required objects.
        # We will build on this in the coming days.
        # ----------------------------------------------------------------------------
        create_prefix_roles(self.logger)
        create_tenant(self.logger)

register_jobs(CreatePop)
```

The create_tenant method is pretty simple and just takes the constant string of `Data Center` that is defined in TENANT_NAME and creates a tenant object with that name. We will be using the tenant object later in the coming days of the exercise.

Next we will create the VLANs and assign the appropriate roles to each VLAN and finally create the custom fields that will be used to assign the roles to the interfaces.

## Final Code

```python
"""Job to create a new site of type POP with optional parent site support."""
from django.contrib.contenttypes.models import ContentType

from nautobot.apps.jobs import Job, register_jobs
from nautobot.extras.models.roles import Role
from nautobot.ipam.models import Prefix, VLAN
from nautobot.tenancy.models import Tenant

name = "Data Population Jobs Collection"

PREFIX_ROLES = ["p2p", "loopback", "server", "mgmt", "pop"]
TENANT_NAME = "Data Center"
ACTIVE_STATUS = Status.objects.get(name="Active")

# VLAN definitions: key is also used to look up the role.
VLAN_INFO = {
    "server": 1000,
    "mgmt": 99,
}

CUSTOM_FIELDS = {
    "role": {"models": [Interface], "label": "Role"},
}
DEVICE_TY

def create_prefix_roles(logger):
    """Create all Prefix Roles defined in PREFIX_ROLES and add content types for IPAM Prefix and VLAN."""

    # Retrieve the content type for Prefix and VLAN models.
    prefix_ct = ContentType.objects.get_for_model(Prefix)
    vlan_ct = ContentType.objects.get_for_model(VLAN)

    for role in PREFIX_ROLES:
        role_obj, created = Role.objects.get_or_create(name=role)
        # Add the Prefix and VLAN content types to the role.
        role_obj.content_types.add(prefix_ct, vlan_ct)
        role_obj.validated_save()
        logger.info(f"Successfully created role {role} with content types for Prefix and VLAN.")

def create_tenant(logger):
    """Create a tenant with the name defined in TENANT_NAME."""
    tenant_obj, _ = Tenant.objects.get_or_create(name=TENANT_NAME)
    tenant_obj.validated_save()
    logger.info(f"Successfully created Tenant {TENANT_NAME}.")

def create_vlans(logger):
    """Create predefined VLANs defined in VLAN_INFO, and assign the appropriate role."""

    for vlan_name, vlan_id in VLAN_INFO.items():
        # Retrieve the appropriate role based on the VLAN name.
        try:
            role_obj = Role.objects.get(name=vlan_name)
        except Role.DoesNotExist:
            logger.error(f"Role '{vlan_name}' not found. VLAN will be created without a role.")
            role_obj = None

        defaults = {"name": vlan_name, "status": ACTIVE_STATUS}
        if role_obj:
            defaults["role"] = role_obj

        vlan_obj, created = VLAN.objects.get_or_create(
            vid=vlan_id,
            defaults=defaults,
        )
        if created:
            vlan_obj.validated_save()
            logger.info(f"Successfully created VLAN '{vlan_name}' with ID {vlan_id}.")
        else:
            logger.info(f"VLAN '{vlan_name}' with ID {vlan_id} already exists.")

def create_custom_fields(logger):
    """Create all relationships defined in CUSTOM_FIELDS."""
    for cf_name, field in CUSTOM_FIELDS.items():
        try:
            cf = CustomField.objects.get(key=cf_name)
        except CustomField.DoesNotExist:
            cf = CustomField.objects.create(key=cf_name)
            if "label" in field:
                cf.label = field.get("label")
            cf.validated_save()
            logger.info(f"Created custom field '{cf_name}'")
        for model in field["models"]:
            ct = ContentType.objects.get_for_model(model)
            cf.content_types.add(ct)
            cf.validated_save()
            logger.info(f"Added content type {ct} to custom field '{cf_name}'")

class CreatePop(Job):
    """Job to create a new site of type POP."""

    class Meta:
        """Metadata for CreatePop."""

        name = "Create a Point of Presence"
        description = """
        Create a new Site of Type POP.
        A new /16 will automatically be allocated from the 'POP Global Pool' Prefix.
        """

    def run(self):
        """Main function to create a site."""
        # ----------------------------------------------------------------------------
        # Initialize the database with all required objects.
        # We will build on this in the coming days.
        # ----------------------------------------------------------------------------
        create_prefix_roles(self.logger)
        create_tenant(self.logger)
        create_vlans(self.logger)
        create_custom_fields(self.logger)

register_jobs(CreatePop)
```

We are adding a new constant called ACTIVE_STATUS which is just getting the Nautobot Extras Active Status that we can use to assign the status attribute as we build out the site. We will need this status for our vlans in the create_vlans method.

You will also notice that we are getting the appropriate role name for the VLAN using the name of the VLAN in this section.

```python
role_obj = Role.objects.get(name=vlan_name)
```

If we find a role that matches the name of the VLAN we assign that role to the VLAN otherwise we create it without a role assignment.

This ensures that when we create the VLAN we are able to add the role we created earlier.

We will continue with the prerequisites tomorrow by adding DeviceType configuration ot the job.

## Day 34 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/).

Go ahead and post a screenshot of the successful execution of the new job on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode` so we can share your progress!

In tomorrow's challenge, we will enhance our Site creation Job by adding DeviceType creation. See you tomorrow!

[LinkedIn](https://www.linkedin.com/)

[X/Twitter](https://x.com/home)
