# Capstone Project Part 5. CVE Management Nautobot App - Day 84

## **Objective**
On **Day 84**, we will introduce a **general status view** for CVEs, providing users with an overview of which **Software Versions** have associated CVEs and how many CVEs each version contains. This enhancement will help users quickly identify vulnerable software versions at a glance.

To achieve this, we will:
1. **Create a new data table** to display the CVE status for software versions.
2. **Define the table logic in `tables.py`**.
3. **Ensure this table integrates with Nautobot's UI**, making it accessible through a dedicated view (to be implemented in the next step).

---

## Environment Setup

For the Capstone for Days 80 - 89, we will use [Scenario 2](../Lab_Setup/scenario_2_setup/README.md) lab with Codespace as we have been doing. 

Assume we built on previous day's progress, we need to enable the virtual environment with `poetry shell` and start the environment with `invoke debug`: 

```
@ericchou1 ➜ ~ $ cd nautobot-app-software-cves/
@ericchou1 ➜ ~/nautobot-app-software-cves $ poetry shell
(nautobot-software-cves-py3.10) @ericchou1 ➜ ~/nautobot-app-software-cves $ invoke debug
...
nautobot-1  | Django version 4.2.20, using settings 'nautobot_config'
nautobot-1  | Starting development server at http://0.0.0.0:8080/
nautobot-1  | Quit the server with CONTROL-C.
...
```

## **Implementation Steps**

### **1. Work with the `tables.py` File**
Inside the **`nautobot_software_cves/`** directory, find the **`tables.py`** file file or create it if you chose "None" on Day 80 Step 9.

```
nautobot-app-software-cves/
├── nautobot_software_cves/
│   ├── __init__.py
│   ├── tables.py  # <-- find this file
```

This file will define the structure and behavior of the **CVE status table**.


### **2. Insert the Following Code in `tables.py` if you chose "None" on Day 80 Step 9**
```python
import django_tables2 as tables # pre-created
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn # pre-created
from django.urls import reverse
from django.utils.safestring import mark_safe
from nautobot.dcim.models import SoftwareVersion


class CveStatusTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = SoftwareVersion
        default_columns = ["platform", "version", "cves_count"]

    platform = tables.Column(linkify=True)
    version = tables.Column(linkify=True)
    cves_count = tables.Column(
        verbose_name="CVEs Count",
        empty_values=(),
        orderable=False
    )

    def render_cves_count(self, value, record):
        cves = record.custom_field_data.get('cves', {})
        if cves:
            url = reverse(
                "plugins:nautobot_software_cves:software_cves",
                kwargs={"pk": record.pk}
            )
            return mark_safe(f'<a href="{url}">{len(cves)}</a>')
        return 0

```

Here is the final version of `tables.py` with pre-existing code and new code if you did not chose "None" on Day 80 Step 9: 

```python
"""Tables for nautobot_software_cves."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn
from django.urls import reverse
from nautobot_software_cves import models
from django.utils.safestring import mark_safe
from nautobot.dcim.models import SoftwareVersion


class NautobotSoftwareCvesExampleModelTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.NautobotSoftwareCvesExampleModel,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.NautobotSoftwareCvesExampleModel
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )


class CveStatusTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = SoftwareVersion
        default_columns = ["platform", "version", "cves_count"]

    platform = tables.Column(linkify=True)
    version = tables.Column(linkify=True)
    cves_count = tables.Column(
        verbose_name="CVEs Count",
        empty_values=(),
        orderable=False
    )

    def render_cves_count(self, value, record):
        cves = record.custom_field_data.get('cves', {})
        if cves:
            url = reverse(
                "plugins:nautobot_software_cves:software_cves",
                kwargs={"pk": record.pk}
            )
            return mark_safe(f'<a href="{url}">{len(cves)}</a>')
        return 0

```

---

## **How the `CveStatusTable` Works**

### **1. Defines a Table for Software Versions**
The **`CveStatusTable`** class extends `BaseTable`, defining a table that will display software versions along with their CVE count.

```python
class CveStatusTable(BaseTable):
```
- This table will be used in a **view** that displays an overview of all software versions and their CVE information.


### **2. Specifies the Model and Default Columns**
```python
class Meta(BaseTable.Meta):
    model = SoftwareVersion
    default_columns = ["platform", "version", "cves_count"]
```
- The table is linked to the `SoftwareVersion` model.
- The **default columns** displayed are:
  - `platform`: The software platform (e.g., Cisco IOS, Juniper JunOS, etc.).
  - `version`: The version of the software.
  - `cves_count`: The number of CVEs associated with this version.


### **3. Adds Hyperlinks for Platform and Version**
```python
platform = tables.Column(linkify=True)
version = tables.Column(linkify=True)
```
- Makes **platform** and **version** clickable so that users can navigate directly to their details.


### **4. Custom Render Method for `cves_count`**
```python
def render_cves_count(self, value, record):
    cves = record.custom_field_data.get('cves', {})
    if cves:
        url = reverse(
            "plugins:nautobot_software_cves:software_cves",
            kwargs={"pk": record.pk}
        )
        return mark_safe(f'<a href="{url}">{len(cves)}</a>')
    return 0
```
- Retrieves **CVE data** from the **custom field**.
- If CVEs exist:
  - Displays the **number of CVEs**.
  - Generates a **hyperlink** to the dedicated **CVE details view**.
- If no CVEs exist, displays `0`.


## **Next Steps**
- Now that we have the **CveStatusTable**, we will create a **view** to display this table and make it accessible via the Nautobot navigation bar.
- This will allow users to see all **Software Versions** with their **CVE counts** in one centralized view.

🚀 Stay tuned for **Day 85**, where we'll integrate this table into a Nautobot view!

## Day 84 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). We highly recommend to just stop the instance, **not** deleting the instance until we completed the whole Capstone project at Day 89, as the days will build on each other.  

Go ahead and post a screenshot of this new app instance you have built for today's challenge, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will continue on with the Capstone project. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+84+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 84 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 

