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

def get_all_interfaces(dnac_token):
    """
    API call to get all available interfaces. This endpoint can return a maximum of 500 interfaces
    Call to DNAC - /dna/intent/api/v1/interface
    Documentation: https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-2-2-2-api-api-devices-get-all-interfaces
    :param dnac_token: String with DNAC Authentication token 
    :return: List of JSON objects with interface details
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/interface'
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
    # # Obtain all the interfaces
    # interfaces = get_all_interfaces(token)
    # print(json.dumps(interfaces, indent=2))

    # # Step 3: Uncomment the following code block
    # # Verify the interfaces
    # # Example: verify that all the interfaces are UP
    # results = []
    # down_interfaces = []
    # for interface in interfaces:
    #     is_status_up = False
    #     device_id = interface['deviceId']
    #     port_name = interface['portName']
    #     admin_status = interface['adminStatus']

    #     # Insert desired config
    #     # Below is just an example
    #     if admin_status == "UP":
    #         is_status_up = True
    #     results.append([device_id, port_name, admin_status, is_status_up])

    #     if not is_status_up:
    #         down_interfaces.append([device_id, port_name, admin_status, is_status_up])

    # print(' ')
    # print('The results of the interfaces verification:')
    # print(' ')
    # # Print a table of the output
    # print(tabulate(results, headers=['Device ID', 'Interface Name', 'Status', 'Is status up?']))
    # print(' ')
    # print('The results of the interfaces verification:')
    # print(' ')
    # # Print a table of the interfaces that are down
    # print(tabulate(down_interfaces, headers=['Device ID', 'Interface Name', 'Status', 'Is status up?']))
    # print(' ')

