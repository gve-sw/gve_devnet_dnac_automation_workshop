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
import sys

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

def get_network(dnac_token):    
    """
    API call to get DHCP and DNS center server network details
    Call to DNAC - /dna/intent/api/v1/network
    Documentation: https://developer.cisco.com/docs/dna-center/#!get-network
    :param dnac_token: String with DNAC Authentication token 
    :return: List of JSON objects with network details
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/network'
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
    # # Obtain the DHCP and DNS server details
    # network_details = get_network(token)
    # print(json.dumps(network_details, indent=2))
    
    # # Step 3: Uncomment the following code block
    # dns_server_details = {}
    # # Filter out the DNS server details
    # for network_detail in network_details:
    #     if network_detail['instanceType'] == 'dns':
    #         dns_server_details = network_detail

    # if not dns_server_details:
    #     print("No DNS server details")
    #     sys.exit(1)

    # # Step 4: Uncomment the following code block
    # #####################
    # ##  Golden Config  ##
    # #####################

    # # Verify the IP address of the DNS server
    # # Below is just an example
    # golden_config_ip_dns_server = "10.10.10.10" #Insert correct ip address
    
    # #####################

    # # Step 5: Unocmment the following code block
    # correct_dns_server_details = False
    # if dns_server_details['value'][0]['primaryIpAddress'] == golden_config_ip_dns_server:
    #     correct_dns_server_details = True
    
    # print("Is the IP address equal to the golden configuration? ", correct_dns_server_details)
    # print("Golden config IP address: ", golden_config_ip_dns_server)
    # print("Current DNS server configuration: ", dns_server_details['value'][0]['primaryIpAddress'])