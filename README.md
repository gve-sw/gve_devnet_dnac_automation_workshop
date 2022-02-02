# GVE DevNet DNAC Automation Workshop
Cisco DNA Center (DNAC) is an intelligent intent-based network controller that allows us to simplify the management of our network and streamline network operations. In addition to the GUI, we can also make use of the DNAC Intent API, which allows us to programmatically interact with the controller and automate our tasks. 

In this workshop, you will learn how to use the DNA Center API. We will be exploring five different use cases: 

* DNS Server Verification
* NTP Server Verification
* Interfaces Verification
* VTY Lines Verification
* VRF Verification


## Contacts
* Simon Fang (sifang@cisco.com)

## Solution Components
* Python 3
* DNA Center

## Installation/Configuration
The following commands are executed in the terminal.

1. Create and activate a virtual environment for the project:
   
        #WINDOWS:
        $ py -3 -m venv gve_devnet_dnac_automation_workshop 
        $ source gve_devnet_dnac_automation_workshop/Scripts/activate
        #MAC:
        $ python3 -m venv gve_devnet_dnac_automation_workshop 
        $ source gve_devnet_dnac_automation_workshop/bin/activate
        

> For more information about virtual environments, please click [here](https://docs.python.org/3/tutorial/venv.html)

2. Access the created virutal environment folder

        $ cd gve_devnet_dnac_automation_workshop

3. Clone this repository

        $ git clone [add_link_to_repository_here]

4. Access the folder `GVE_DevNet_DNAC_Automation`

        $ cd GVE_DevNet_DNAC_Automation

5. Install the dependencies:

        $ pip install -r requirements.txt

6. Open the `.env` file and add the credentials of the [Always On DNA Center Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology):

        DNAC_BASE_URL = "<insert_dnac_base_url>"
        DNAC_USERNAME = "<insert_dnac_username>"
        DNAC_PASSWORD = "<insert_dnac_password>"

7. Click on `next` for the next steps

<div align="right">
   
   [Next](0_dns_server_verification)
</div>


## Further Resources

For more information about DNA Center API Token, please consult the following resources:

> https://developer.cisco.com/site/dnac-101/

> https://developer.cisco.com/docs/dna-center/#!getting-started

For more information on how to get started with the DNA Center API using Postman, then please consult the following resource:

> https://developer.cisco.com/docs/dna-center/#!postman-collections

Alternatively, you can also use the DNA Center SDK. Please go to the following link for the documentation of the SDK:

> https://dnacentersdk.readthedocs.io/en/latest/api/api.html

For more information about the DNA Center REST API Documentation, please consult the following resource:

> https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-2-2-api-overview

You can find Cisco DNA Center sandboxes through the following links:

> [Cisco DNA Center Always On 1.3.1.4](https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology)

> [Cisco DNA Center Always On 2.1.2.5](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology)

Another useful learning resource are the Cisco DevNet Learning Labs. The following are a great resource to learn more about Cisco DNA Center:

> https://developer.cisco.com/learning/modules/dnac-rest-apis

> https://developer.cisco.com/learning/lab/dnac-basic/step/1

> https://developer.cisco.com/learning/lab/dnac-path-trace-archived/step/1

> https://developer.cisco.com/learning/lab/dnac-101-auth/step/1

> https://developer.cisco.com/learning/lab/dnac-101-template-prg/step/1

> https://developer.cisco.com/learning/lab/intro-dnac-cmd-run/step/1

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.