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

def get_credentials(dnac_token, params):
    """
    API call to get the global credentials. A parameter needs to be specified to get the subtype of credentials. 
    Call to DNAC - /dna/intent/api/v1/global-credential
    Documentation: https://developer.cisco.com/docs/dna-center/#!credentials/credentials-guide
    :param dnac_token: String with DNAC Authentication token 
    :return: List of JSON objects with credential details
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/global-credential'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-auth-token': dnac_token
    }
    response = requests.get(
        url=url, 
        headers=headers, 
        params=params,
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
    # # Specify the credentials subtype as a parameter
    # query_string_params = {
    #     'credentialSubType' : 'CLI'
    # }

    # # Obtain the CLI credentials
    # credentials = get_credentials(token, query_string_params)
    # print(json.dumps(credentials, indent=2))

    # # Step 3: Uncomment the following code block
    # #####################
    # ##  Golden Config  ##
    # #####################

    # # Verify the credentials/vty lines configuration
    # # Insert the golden configuration
    # # Below is just an example
    # golden_config_credential = {
    #     'username': 'example',
    #     'password': 'example'
    # }

    # #####################

    # # Step 4: Uncomment the following code block
    # for credential in credentials:
    #     # We check if the golden_config_credential is a subset of the credential dictionary
    #     is_golden_config_in_credential = all(item in credential.items() for item in golden_config_credential.items())
    #     print("Is the golden config a subset of the credential dictionary? ", is_golden_config_in_credential)


