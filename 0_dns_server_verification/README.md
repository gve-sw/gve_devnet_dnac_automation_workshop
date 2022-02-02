# DNS Server Verification
The Domain Name System (DNS) is a distributed database and crucial for connectivity. It maps the hostnames to IP addresses through the DNS protocol from a DNS server. Therefore, it is important that we verify the DNS Server after configuration. 

In this section, we will explore how to perform a DNS Server verification on the DNA Center through its API. The verification will happen in three steps:

1. Obtain a DNAC authentication token
2. Get the server details and filter out the DNS server details
3. Compare the DNS server details with the golden config DNS server details and create a report


## Usage
Please enter the following commands in the terminal:

0. Change to the current directory (you current directory should be `GVE_DevNet_DNAC_Automation_Workshop`):

        $ cd 0_dns_server_verification

1. Obtain the DNAC authentication token. Uncomment the following code block in `main.py`:

    ```python
    # # Step 1: Uncomment the following code block
    # # Obtain DNA Center authentication token
    # token = get_auth_token()
    # print("You DNAC token: ", token)
    ```
    And execute the following code in your terminal:

        $ python main.py
    
    You should see your DNAC token displayed in the terminal now.

2. Get the network details. Uncomment the following code block in `main.py`:

    ```python
    # # Step 2: Uncomment the following code block
    # # Obtain the DHCP and DNS server details
    # network_details = get_network(token)
    # print(json.dumps(network_details, indent=2))
    ```
    And execute the following code in your terminal:

        $ python main.py
    
    You will see the DHCP and DNS server details displayed in the terminal now.

3. Filter out the DNS server details. Uncomment the following code block in `main.py`:

    ```python
    # # Step 3: Uncomment the following code block
    # dns_server_details = {}
    # # Filter out the DNS server details
    # for network_detail in network_details:
    #     if network_detail['instanceType'] == 'dns':
    #         dns_server_details = network_detail

    # if not dns_server_details:
    #     print("No DNS server details")
    #     sys.exit(1)
    ```
    And execute the following code in your terminal:

        $ python main.py
    
    You will have filtered out the DNS server details and it will be stored in the variable `DNS server details`. If there are no DNS server details, then the script will exit with status code 1. 

4. Add the golden configuration. Customize if needed. Uncomment the following code block in `main.py`:

    ```python
    # # Step 4: Uncomment the following code block
    # #####################
    # ##  Golden Config  ##
    # #####################

    # # Verify the IP address of the DNS server
    # # Below is just an example
    # golden_config_ip_dns_server = "10.10.10.10" #Insert correct ip address
    
    # #####################
    ```

5. Perform the DNS server verification. Compare the current DNS server configuration with the golden configuration. Uncomment the following code block in `main.py`:

    ```python
    # # Step 5: Unocmment the following code block
    # correct_dns_server_details = False
    # if dns_server_details['value'][0]['primaryIpAddress'] == golden_config_ip_dns_server:
    #     correct_dns_server_details = True
    
    # print("Is the IP address equal to the golden configuration? ", correct_dns_server_details)
    # print("Golden config IP address: ", golden_config_ip_dns_server)
    # print("Current DNS server configuration: ", dns_server_details['value'][0]['primaryIpAddress'])
    ```

    And execute the following code in your terminal:

        $ python main.py

    You will see a _report_ in your terminal with the results of the verification. 

6. Great job! You have successfully performed a basic DNS server verification. Customize the code if needed to suit your use case. Click on `next` for the next use case. 

<div align="right">
   
   [Prev](../README.md) - [Next](../1_ntp_server_verification)
</div>
