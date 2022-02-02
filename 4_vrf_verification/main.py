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
import time
from pyats_genie_command_parse import GenieCommandParse
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

def get_device_list(dnac_token, params={}):
    """
    API call to get a list of network devices based on filter criteria such as management IP address, mac address, hostname, etc. 
    Documentation: https://developer.cisco.com/docs/dna-center/#!get-device-list-1
    :param dnac_token: String with DNAC Authentication token 
    :param params: A dictionary where you can specify search parameters
    :return: List of JSON objects with device details
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/network-device'
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

def post_command_runner_request(dnac_token, payload):
    """
    API call to post read only commands on devices to get their real time configuration. A payload neds to be sent in the post request with 
    the commands that the user would like to execute on the CLI of the device. 
    Call to DNAC - /dna/intent/api/v1/network-device-poller/cli/read-request
    Documentation: https://developer.cisco.com/docs/dna-center/#!run-read-only-commands-on-devices-to-get-their-real-time-configuration
    :param dnac_token: String with DNAC Authentication token 
    :param payload: A dictionary with a list of commands, the device UUIDs and a timeout
    :return: A string with the task ID
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/network-device-poller/cli/read-request'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-auth-token': dnac_token
    }
    response = requests.post(
        url=url, 
        data=json.dumps(payload), 
        headers=headers, 
        verify=False
        )
    print(response.text)
    response.raise_for_status()
    task_id = response.json()['response']['taskId']
    return task_id

def get_file_id(dnac_token, task_id):
    """
    API call to return a task by specified id. 
    Call to DNAC - /dna/intent/api/v1/task/{taskId}
    Documentation: https://developer.cisco.com/docs/dna-center/#!get-task-by-id
    :param dnac_token: String with DNAC Authentication token 
    :param task_id: String with the task ID that was returned by the command runner API
    :return: String with the file_id
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/task/{task_id}'
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
    print("get_file_id response:")
    print(json.dumps(response.json(), indent=2))
    progress_json = json.loads(response.json()['response']['progress'])
    file_id = progress_json['fileId']
    return file_id

def get_file(dnac_token, file_id):
    """
    API call to download a file specified by fileId 
    Call to DNAC - /dna/intent/api/v1/file/{fileId}
    Documentation: https://developer.cisco.com/docs/dna-center/#!download-a-file-by-file-id
    :param dnac_token: String with DNAC Authentication token 
    :param file_id: String with the file ID that was returned by the task API
    :return: String with the file
    """
    url = f'{DNAC_BASE_URL}/dna/intent/api/v1/file/{file_id}'
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
    return response.json()

if __name__ == "__main__":
    # # Step 1: Uncomment the following code block
    # # Obtain DNA Center authentication token
    # token = get_auth_token()
    # print("You DNAC token: ", token)

    # # Step 2: Uncomment the following code block
    # # Get a filtered list of devices
    # params_filter_devices = {"family": "Switches and Hubs"}
    # devices = get_device_list(token, params_filter_devices)
    # print(json.dumps(devices, indent=2))

    # # Step 3: Uncomment the following code block
    # # Extract the device IDs of each device
    # device_ids = []
    # for device in devices:
    #     device_ids.append(device["id"])
    # print(device_ids)

    # # Step 4: Uncomment the following code block
    # # Send a number of commands to the command runner API
    # commands = [
    #         "show vrf"
    #     ]
    # payload = {
    #     "commands": commands,
    #     "deviceUuids": device_ids,
    #     "timeout": 0
    # }
    # task_id = post_command_runner_request(token, payload)
    # print(task_id)
    # 
    # # Let's wait 30 seconds after executing the commands
    # time.sleep(30)

    # # Step 5: Uncomment the following code block
    # # We use the task_id to obtain a file_id
    # file_id = get_file_id(token, task_id)

    # # Obtain a file using the file_id
    # file = get_file(token, file_id)
    # print(file)

    # # Step 6: Uncomment the following code block
    # results = []
    # for device in file:
    #     device_uuid = device['deviceUuid']
    #     for command in commands:
    #         if device['commandResponses']['SUCCESS']:
    #             # Print the raw output
    #             command_output = device['commandResponses']['SUCCESS'][command]
    #             print(command_output)
    #             print(' ')

    #             # Parse the raw output
    #             parser = GenieCommandParse(nos='ios')
    #             parsed_output = parser.parse_string(show_command=command, show_output_data=command_output)

    #             # Print the parsed output
    #             print(json.dumps(parsed_output, indent=2))
    #             print(' ')

    #             if command == "show vrf":

    #                 #####################
    #                 ##  Golden Config  ##
    #                 #####################

    #                 # Insert golden config of show vrf
    #                 # Below is just an example
    #                 golden_config_show_vrf = {
    #                     "vrf": {
    #                         "Mgmt-vrf": {
    #                         "protocols": [
    #                             "ipv4",
    #                             "ipv6"
    #                         ],
    #                         "interfaces": [
    #                             "GigabitEthernet0/0"
    #                         ]
    #                         }
    #                     }
    #                 }

    #                 #####################

    #                 # Verify if the vrf config is correct, by default false
    #                 correct_vrf_config = False
    #                 if golden_config_show_vrf == parsed_output:
    #                     correct_vrf_config = True
                    
    #                 # Add the result to the list of results
    #                 results.append([device_uuid, correct_vrf_config])

    # print(' ')
    # print('The results of the VRF verification:')
    # print(' ')
    # # Print a table of the output
    # print(tabulate(results, headers=['Device UUIDs', 'Correct VRF Config']))
                    
                
