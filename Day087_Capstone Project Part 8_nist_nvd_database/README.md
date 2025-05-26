# Capstone Project Part 8. Day 87: Retrieving CVE Information from NVD NIST Database via API

## Objective

On **Day 87**, we will explore how to retrieve Common Vulnerabilities and Exposures (CVE) information from the National Vulnerability Database (NVD) maintained by the National Institute of Standards and Technology (NIST). This involves:

1. Understanding the **CVE naming convention**.
2. Understanding the **CPE naming convention**.
3. Learning how the NVD API operates.
4. Demonstrating how to retrieve CVE data for Cisco IOSXE Software version 17.7.2.

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

## 1. Understanding the CVE Naming Convention

The **CVE** system provides a standardized method for identifying and naming cybersecurity vulnerabilities. Each CVE identifier follows this format:

```
CVE-YYYY-NNNNN
```

Where:
- `CVE` denotes the prefix for Common Vulnerabilities and Exposures.
- `YYYY` is the year the CVE ID was assigned or made public.
- `NNNNN` is a unique sequence number.

*Example*: `CVE-2025-12345` refers to the 12,345th vulnerability cataloged in 2025.

## 2. Understanding the CPE Naming Convention

The **Common Platform Enumeration (CPE)** is a standardized method for describing and identifying classes of applications, operating systems, and hardware devices present among an enterprise's computing assets. A CPE name consists of a structured string that includes several components to uniquely identify a product. The naming syntax follows this pattern:

```
cpe:2.3:a:<vendor>:<product>:<version>:<update>:<edition>:<language>:<sw_edition>:<target_sw>:<target_hw>:<other>
```

- `cpe` indicates the CPE prefix.
- `2.3` specifies the CPE version.
- `a` denotes the part, where `a` stands for application, `o` for operating system, and `h` for hardware.
- `<vendor>` is the name of the product's vendor.
- `<product>` is the name of the product.
- `<version>` is the version of the product.
- `<update>` specifies update information.
- `<edition>` provides edition information.
- `<language>` indicates the language.
- `<sw_edition>`, `<target_sw>`, `<target_hw>`, and `<other>` provide additional optional attributes.

*Example*: A CPE name for Cisco IOS XE version 17.7.2 might look like:

```
cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*
```

This CPE name breaks down as:
- `cpe:2.3`: CPE version 2.3.
- `o`: Operating system.
- `cisco`: Vendor.
- `ios_xe`: Product.
- `17.7.2`: Version.
- The remaining fields are wildcards (`*`), indicating any value.

## 3. Overview of the NVD API

The NVD provides a public API that allows users to query CVE data. Key features include:

- **Base URL**: All API endpoints are prefixed with `https://services.nvd.nist.gov/rest/json/`.
- **Rate Limiting**: The API has rate limits; ensure compliance to avoid being blocked.
- **Data Formats**: Responses are typically in JSON format.
- **Endpoints**:
  - `/cves/2.0`: Retrieve CVE details.
  - `/cpe/2.3`: Retrieve CPE details.

## 4. Retrieving CVE Data for Cisco IOS XE Version 17.7.2

To find CVEs associated with Cisco IOS XE version 17.7.2:

1. **Identify the CPE Name**: As determined earlier, the CPE name is:
   ```
   cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*
   ```

1. **Make the API Request with curl**: Use tools like `curl` or Postman to send a GET request to the URL `https://services.nvd.nist.gov/rest/json/cves/2.0`. The cpeName should be included as a query string parameter in your request. Below is a demonstration using `curl`, but feel free to test the same request in Postman as well:

```bash
curl --location --get 'https://services.nvd.nist.gov/rest/json/cves/2.0' \
--data-urlencode 'cpeName=cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
```

1. **Make the API Request with python**: You can also use Python’s requests library to retrieve CVE data from the API, as shown below.

```python
import requests
import json
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
params = {"cpeName":"cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*"}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
response = requests.get(url=url, headers=headers, params=params)
print(response.text)
```

1. **Process the Response**: The API will return a JSON object containing CVE entries related to the specified CPE. Extract relevant information such as CVE IDs, descriptions, and severity ratings.

*Example using `curl`*:

```bash
curl --location --get -s 'https://services.nvd.nist.gov/rest/json/cves/2.0' \
--data-urlencode 'cpeName=cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' | jq .
```

This command fetches the CVE data and formats it using `jq` for readability.

*Fetch CVE data for the CVE with id **CVE-2024-20313** using `curl`*:

```bash
curl --location --get -s 'https://services.nvd.nist.gov/rest/json/cves/2.0' \
--data-urlencode 'cpeName=cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' | jq '.vulnerabilities[] | select(.cve.id == "CVE-2024-20313")'
```

This command fetches the CVE data and extracts the data of CVE with id **CVE-2024-20313** using `jq`.

*Fetch CVE data for the CVE with id **CVE-2024-20313** using `python`*:

```python
import requests
import json
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
params = {"cpeName":"cpe:2.3:o:cisco:ios_xe:17.7.2:*:*:*:*:*:*:*"}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
response = requests.get(url=url, headers=headers, params=params)
vulnerabilities = response.json()['vulnerabilities']
cve_data = next(cve for cve in vulnerabilities if cve['cve']['id']=='CVE-2024-20313')
print(cve_data)
```

## Final Outcome

By following these steps, you can programmatically retrieve and analyze CVE data for specific software versions using the NVD API. This capability is essential for maintaining awareness of vulnerabilities and enhancing cybersecurity measures within your organization.

## Day 87 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). We highly recommend to just stop the instance, **not** deleting the instance until we completed the whole Capstone project at Day 89, as the days will build on each other.  

Go ahead and post a screenshot of this new app instance you have built for today's challenge, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will continue on with the Capstone project. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+87+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 87 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 

