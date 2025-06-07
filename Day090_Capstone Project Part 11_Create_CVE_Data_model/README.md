# Capstone Project Part 11. Day 90: Creating a Custom Nautobot Model for CVEs

## Objective

On **Day 90**, we will enhance our Nautobot plugin by creating a custom data model to store CVEs (Common Vulnerabilities and Exposures). This approach offers better data management and integration compared to using JSON custom fields.

## Why Move from a JSON Custom Field to a Nautobot Data Model?

Previously, CVEs were stored in a JSON custom field like this:

```json
{
    "CVE-2023-1234": {
        "cvss_base_score": 9.8,
        "link": "https://example.com/CVE-2023-1234",
        "severity": "Critical"
    }
}
```

While this works for basic use cases, it comes with several limitations:

❌ No relational integrity or built-in querying  
❌ Cannot take advantage of Nautobot's change tracking, filtering, or object permissions  
❌ Hard to scale or link CVEs to other models

By creating a custom model, you gain:

✅ Full query/filter/search support in the UI and API  
✅ Relational connections to other models (e.g., SoftwareVersion)  
✅ Better visibility, permissions, and auditability

## Relationship: CVEs ↔ Software Versions

A CVE can affect multiple software versions, and a software version can have multiple CVEs. This is a classic Many-to-Many relationship.

### Reference Summary of Relationships:

- **One-to-One (1:1)**: Each record in table A has one matching record in table B, and vice versa.  
- **One-to-Many (1:N)**: One record in table A can relate to many in B, but each in B relates to one in A.  
- **Many-to-Many (N:N)**: Records in A can relate to many in B and vice versa.

In our case:

- One CVE → affects multiple Software Versions  
- One Software Version → may be affected by multiple CVEs

## Implementing the CVE Model

We'll define a `CVE` model with a Many-to-Many relationship to `SoftwareVersion`.

### Code Implementation

Inside the **`nautobot_software_cves/`** directory, find the **`models.py`** file or create it if you chose "None" on Day 80 Step 9 and insert the following code:

In `models.py`:

```python
from django.db import models

try:
    from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
except ImportError:
    CHARFIELD_MAX_LENGTH = 255

from nautobot.apps.models import PrimaryModel
from nautobot.apps.choices import ChoiceSet

class CVESeverityChoices(ChoiceSet):
    """Choices for CVE severity levels."""

    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    NONE = "None"

    CHOICES = (
        (CRITICAL, CRITICAL),
        (HIGH, HIGH),
        (MEDIUM, MEDIUM),
        (LOW, LOW),
        (NONE, NONE),
    )

class CVE(PrimaryModel):
    """Model representing a CVE."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH, unique=True)
    link = models.URLField()
    severity = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        choices=CVESeverityChoices,
        default=CVESeverityChoices.NONE
    )
    cvss = models.FloatField(null=True, blank=True, verbose_name="CVSS Base Score")
    affected_softwares = models.ManyToManyField(
        to="dcim.SoftwareVersion",
        related_name="corresponding_cves",
        blank=True
    )

    class Meta:
        verbose_name = "CVE"
        ordering = ("severity", "name")

    def __str__(self):
        return self.name
```

### Explanation

- **PrimaryModel** is the class used in Nautobot for full-featured data models that support most or all of Nautobot’s extensions to base Django functionality. It’s generally the class you’ll want to use for any data model that represents a distinct “thing” in the network.
- Note that we’re using `unique=True` on the **name** field to specify that this must be globally unique within Nautobot’s database.
- **CVESeverityChoices**: Provides consistent values for the severity field, making filtering and validation easier.
- **name**: The CVE ID (e.g., "CVE-2023-1234") is stored here.
- **link**: A URL pointing to an official CVE reference.
- **severity**: The level of severity, selected from the predefined choices.
- **cvss**: A float representing the CVSS base score.
- **affected_softwares**: Establishes a Many-to-Many relationship with `SoftwareVersion`.
  - The `related_name` attribute allows reverse querying from `SoftwareVersion` to associated `CVE` instances using `corresponding_cves`.

- **Meta options**:
  - `verbose_name` Provides a human-readable name for the model, used in the admin interface.
  - `ordering` Specifies the default ordering of query results, first by `severity`, then by `name`.

This structured model supports full ORM integration and relationships, which the JSON field lacked.

## Applying Migrations and Verification

After defining the `CVE` model, you need to apply the changes to your database schema. This involves two steps:

### 1. Create Migration Files

Run the following command to generate migration files based on your model changes:

```
$ invoke makemigrations
Running docker compose command "ps --services --filter status=running"
Running docker compose command "exec nautobot nautobot-server makemigrations nautobot_software_cves"
Migrations for 'nautobot_software_cves':
  nautobot_software_cves/migrations/0002_cve.py
    - Create model CVE
```

This command analyzes your models and creates migration files that describe the changes needed to update the database schema. These files are stored in the `migrations` directory of your app. The generated file `nautobot_software_cves/migrations/0001_initial.py`, basically is a set of instructions to Django telling it how to translate your Python code to SQL.

### 2. Apply Migrations

Once the migration files are created, apply them to update your database schema:

```
$ invoke migrate
Running docker compose command "ps --services --filter status=running"
Running docker compose command "exec nautobot nautobot-server migrate"
Operations to perform:
  Apply all migrations: admin, auth, circuits, cloud, constance, contenttypes, dcim, django_celery_beat, django_celery_results, extras, ipam, nautobot_software_cves, sessions, silk, social_django, taggit, tenancy, users, virtualization
Running migrations:
  Applying nautobot_software_cves.0002_cve... OK
12:53:08.839 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Export Object List" from <ExportObjectList>
12:53:08.843 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Git Repository: Sync" from <GitRepositorySync>
12:53:08.849 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Git Repository: Dry-Run" from <GitRepositoryDryRun>
12:53:08.854 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Import Objects" from <ImportObjects>
12:53:08.859 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Logs Cleanup" from <LogsCleanup>
12:53:08.863 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "System Jobs: Refresh Dynamic Group Caches" from <RefreshDynamicGroupCaches>
12:53:08.867 INFO    nautobot.extras.utils utils.py        refresh_job_model_from_job_class() : Refreshed Job "CVE Tracking: Load Vulnerabilities" from <LoadCVEsJob>
```

This command executes the SQL statements defined in the migration files, creating or altering database tables as necessary to match your models.

By completing these steps, your `CVE` model will be fully integrated into the Nautobot database, allowing you to manage CVE records effectively.

### 3. Verification

You can verify that this model is now defined by using the invoke nbshell command as follows, though of course, there are no specific CVE records actually present in your database yet:

```bash
❯ invoke nbshell
Running docker compose command "ps --services --filter status=running"
Running docker compose command "exec nautobot nautobot-server nbshell  "
# Django version 4.2.19
# Nautobot version 2.3.2
# Nautobot Software Cves version 0.1.0
Python 3.11.9 (main, Sep  4 2024, 07:49:21) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.3 -- An enhanced Interactive Python. Type '?' for help.
In [2]: from nautobot_software_cves.models import CVE
In [3]: CVE.objects.all()
Out[3]: <RestrictedQuerySet []>
```

## Final Thoughts

Transitioning from JSON custom fields to proper Nautobot models allows for scalable, robust, and queryable solutions that grow with your network automation platform.

## Next Steps

In the upcoming days, we'll:

- Enhance the Nautobot UI to display CVEs associated with software versions.
- Refactor the CVE loader job to populate this new model.

Stay tuned for Day 91!