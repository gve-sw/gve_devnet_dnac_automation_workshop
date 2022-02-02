""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

__author__ = "Simon Fang <sifang@cisco.com>"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"
"""

# Import Section
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import json
from tabulate import tabulate

# Disable warnings
urllib3.disable_warnings(InsecureRequestWarning)

# load all environment variables
load_dotenv()

DNAC_BASE_URL = os.getenv('DNAC_BASE_URL')
DNAC_USERNAME = os.getenv("DNAC_USERNAME")
DNAC_PASSWORD = os.getenv("DNAC_PASSWORD")

# Helper functions
def get_auth_token():
    """
    Create the authorization token required to access DNAC
    Call to DNAC - /api/system/v1/auth/login
    Documentation: https://developer.cisco.com/docs/dna-center/#!authentication-api
    :return: DNAC Authentication token
    """
    url = f'{DNAC_BASE_URL}/dna/system/api/v1/auth/token'
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url=url, 
        auth=HTTPBasicAuth(DNAC_USERNAME, DNAC_PASSWORD), 
        headers=headers,
        verify=False)
    token = response.json()['Token']
    return token

def get_nodes_config(dnac_token):
    """
    Provides details about the current Cisco DNA Center node configuration, such as API version, node name, 
    NTP server, intracluster link, LACP mode, network static routes, DNS server, subnet mask, host IP, 
    default gateway, and interface information.
    Call to DNAC - /dna/intent/api/v1/nodes-config
    Documentation: https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-2-2-2-api-api-platform-configuration-cisco-dna-center-nodes-configuration-summary
    :param dnac_token: String with DNAC Authentication token 
    :return: List of JSON objects with DNAC nodes configuration details
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/nodes-config'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-auth-token': dnac_token
    }
    response = requests.get(
        url=url, 
        headers=headers, 
        verify=False
    )
    response.raise_for_status()
    return response.json()['response']

# Main function
if __name__ == "__main__":
    # # Step 1: Uncomment the following code block
    # # Obtain DNA Center authentication token
    # token = get_auth_token()
    # print("You DNAC token: ", token)

    # # Step 2: Uncomment the following code block
    # # Obtain the NTP server details
    # nodes_config_details = get_nodes_config(token)
    # print(json.dumps(nodes_config_details, indent=2))

    """
    Example of NTP server configuration:
    "ntp": {
        "servers": [
          "10.10.10.10"
        ]
      },
    """

    # # Step 3: Uncomment the following code block
    # results = []
    # # In case you have a multi node DNA Center deployment
    # for node in nodes_config_details["nodes"]:
    #     node_name = node["name"]
    #     ntp_server_details = node["ntp"]["servers"]

    #     #####################
    #     ##  Golden Config  ##
    #     #####################

    #     ## Insert golden config of ntp server
    #     ## Below is just an example
    #     golden_config_ntp_server = "10.10.10.10"

    #     #####################

    #     correct_ntp_server = False
    #     # Verify the NTP server
    #     if golden_config_ntp_server in ntp_server_details:
    #         correct_ntp_server = True
        
    #     results.append([node_name, ntp_server_details, golden_config_ntp_server, correct_ntp_server])

    # print(' ')
    # print('The results of the NTP server verification:')
    # print(' ')
    # # Print a table of the output
    # print(tabulate(results, headers=['Name of node', 'NTP server config', 'NTP server golden config', 'Correct NTP server Config?']))
    