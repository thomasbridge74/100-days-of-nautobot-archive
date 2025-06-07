# Capstone Project Part 4. CVE Management Nautobot App - Day 83

## **Objective**
In **Day 82**, we added CVE information to the **SoftwareVersion** detail view by displaying CVEs on the right-hand side panel. However, to further enhance usability, we will now add a **dedicated CVE details tab** to the **SoftwareVersion** view.

This tab will allow users to see CVE data in a structured format within a separate view, rather than just in the side panel.

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

### **1. Add a CVE Details Tab in `template_content.py`**
We extend the `SoftwareVersionTemplateExtension` class to add a new tab to the **SoftwareVersion** detail view. This is done using the `detail_tabs` method.

- `detail_tabs` adds **new tabs** to the Nautobot UI for the specified model (`dcim.softwareversion`).
- It allows users to access more detailed information about CVEs without cluttering the main view.
- The tab will link to a **dedicated view** that we will define next.

The code below works as follows:
- It adds a “CVEs” tab to the SoftwareVersion detail page.
- This tab links to `/softwareversions/<uuid:pk>/cves/` using the reverse() function.
- In Django, reverse() dynamically generates a URL from a named route by resolving the corresponding view name and optional parameters.

#### Insert the following code in `template_content.py`. **right_page** remains unchanged.
```python
"""Module to change object details view."""

from django.urls import reverse #new
from nautobot.apps.ui import TemplateExtension

class SoftwareVersionTemplateExtension(TemplateExtension):
    """Add CVE information to the Nautobot Software Version detail view."""

    model = "dcim.softwareversion"

    def right_page(self):
        """Add content on the right side of the view."""

    def detail_tabs(self): #new
        """Add a CVE details tab to the SoftwareVersion view."""
        return [
            {
                "title": "CVEs",
                "url": reverse(
                    "plugins:nautobot_software_cves:software_cves",
                    kwargs={"pk": self.context["object"].pk}
                ),
            },
        ]

# Register the template extension so Nautobot applies it
template_extensions = [SoftwareVersionTemplateExtension]
```

### **2. Define the URL in `urls.py`**

We need to create a new URL because the **detail tab** added above requires a destination. This URL will map to a **new view** that displays detailed CVE data for a SoftwareVersion.

The new URL with name **software_cves**:
  - Maps `/softwareversions/<uuid:pk>/cves/` to `SoftwareCvesView`.
  - Ensures the correct SoftwareVersion object is passed to the view.

#### Insert the following code in `urls.py` to define the URL:
```python
from django.urls import path
from nautobot_software_cves import views

urlpatterns = [
    path(
        "softwareversions/<uuid:pk>/cves/",
        views.SoftwareCvesView.as_view(),
        name="software_cves",
    ),
]
```

### **3. Create the View in `views.py`**

The new view will **handle requests** to display the CVE details for a specific SoftwareVersion. It pulls data from the **custom field** and renders it in an organized manner using a template.

- Retrieves the **SoftwareVersion** object using `queryset`.
- Specifies the template to be rendered in the `template_name` attribute.
- Passes the **CVE data** to the template using `get_extra_context`.

#### Inside the **`nautobot_software_cves/`** directory, find `views.py` or create it if you chose "None" on Day 80 Step 9 and insert the following code to define the new view:
```python
from nautobot.apps import views
from nautobot.dcim.models import SoftwareVersion

class SoftwareCvesView(views.ObjectView):
    queryset = SoftwareVersion.objects.all()
    template_name = "nautobot_software_cves/software_cves.html"

    def get_extra_context(self, request, instance):
        return {"cves": instance.custom_field_data.get("cves", {})}
```

### **4. Create the Template for CVE Details**

- The **SoftwareCvesView** needs an associated HTML template to render the CVE details.
- This template structures the data in a user-friendly table format.

The template below works as follows:
- First, it’s an extension of the built-in dcim/softwareversion_retrieve.html template, which is the base template
for every tab in the SoftwareVersion detail view. 
- In this template, we only override the block called content, which defines the HTML content of the tab itself.
- We define a heading for the CVEs, and then a table of CVE entries, which we populate by iterating over the CVEs of the custom field.

#### **Create the `templates/nautobot_software_cves/` Folder**
```
nautobot-app-software-cves/
├── nautobot_software_cves/
│   ├── templates/
│   │   ├── nautobot_software_cves/
│   │   │   ├── software_cves.html
```

#### Insert the following code in `software_cves.html`:
```html
{% extends 'dcim/softwareversion_retrieve.html' %}
{% block content %}
<div class="panel panel-default">
    <table class="table table-hover table-headings">
        <thead>
            <tr>
                <th>CVE Name</th>
                <th>CVSS Base Score</th>
                <th>Severity</th>
            </tr>
        </thead>
        {% for cve_name, cve_data in cves.items %}
        <tr>
            <td><a href="{{ cve_data.link }}">{{ cve_name }}</a></td>
            <td>{{ cve_data.cvss_base_score }}</td>
            <td>{{ cve_data.severity }}</td>
        </tr>
        {% endfor %}
    </table>
</div>
{% endblock content %}
```

### **Verification**

- After restarting invoke debug once again.
- On the **SoftwareVersion** detail view for Cisco IOS-XE version 17.7.2, a new CVEs tab has been added. Clicking on this tab will display a list of CVEs associated with this **SoftwareVersion.**
![cves_tab](images/cves_tab.png)

## **Conclusion**
This enhancement improves the Nautobot UI by:
✅ Adding a **dedicated CVE tab** for each **SoftwareVersion**.
✅ Providing a **structured and detailed view** of CVE data.
✅ Making it easier for users to analyze security vulnerabilities associated with software versions.

In **Day 84**, we can focus on **creating the actual template (`software_cves.html`)** to display the CVEs in a structured table format.

Let me know if you need any modifications! 🚀

## Day 83 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). We highly recommend to just stop the instance, **not** deleting the instance until we completed the whole Capstone project at Day 89, as the days will build on each other.  

Go ahead and post a screenshot of the new detail view for CVEs you built for today's challenge, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will continue on with the Capstone project. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+83+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 83 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 

