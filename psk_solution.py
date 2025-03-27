"""
Created by Andrew Dunsmoor
Solutions Engineer for Cisco Systems
Intention is to provide a basic walk-through of the Meraki API for the purposes of pushing config changes
"""

from dotenv import load_dotenv
import meraki
import os
from pprint import pprint # pprint makes printing lists and dictionaries prettier to read

# MUST CREATE environment.env FILE WITH THE FOLLOWING VARIABLES #
load_dotenv('environment.env')
API_KEY = os.getenv('API_KEY')

# INITIALIZE DASHBOARD OBJECT
dashboard = meraki.DashboardAPI(API_KEY, print_console=False)
# dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True) # Change to true to stop log outputs

# Uncomment if you need to get your org or network ID.
# Get organizations
# orgs_list = dashboard.organizations.getOrganizations()

# Setting Org ID based on my own network knowledge
organization_id = '1071672'

# Get a list of all networks : Response object is a list of dictionaries
networks_list = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

# Print all network list data
# pprint(networks_list)

# SELECT NETWORK BASED ON CRITERIA

# Define loop variables for clarity
target = 'home stack'   # Define the target we wil be matching on
target_networks = []    # Define the list of networks we care about

### TASK ###
# Loop through all networks in networks_list.
# Print their names.
# If the name matches the target, append it to target_networks
###

# Loop through list of networks: Each network is a dictionary object
for network in networks_list:   # network is a dictionary
    # print(network['name']) # Print Network Name using key/value

    # Check if network name matches target (can match based on any attribute, does not have to be name)
    if target.lower() in network['name'].lower():
        target_networks.append(network)

# Print target network data
pprint(target_networks)

# Define SSID target variable and the desire PSK.
ssid_target = 'Python'
desired_psk = 'sketchers'   # This can be set based on an external settings file if desired.

### TASK ###
# Loop through all networks in desired_networks.
# If the SSID name matches the target, check the PSK
# If the PSK does not match the desired_psk, update it
###
for network in target_networks: # Loop Through All Relevant Networks

    # https://developer.cisco.com/meraki/api-v1/get-network-wireless-ssid/
    ssid_list = dashboard.wireless.getNetworkWirelessSsids(network['id'])   # API call to get list of SSIDs

    # pprint(ssid_list)

    for ssid in ssid_list:  # Loop through all SSID dicts in SSID list

        if ssid_target.lower() in ssid['name'].lower(): # Match based on SSID target name

            print(f"Password for SSID {ssid['name']} is {ssid['psk']}") # Print Current Password

            if ssid['psk'] is not desired_psk: # Check if PSK is set to desired PSK

                # Update SSID with new PSK value
                #https://developer.cisco.com/meraki/api-v1/update-network-wireless-ssid/
                ssid_update_response = dashboard.wireless.updateNetworkWirelessSsid(
                    network['id'], ssid['number'],  # Select correct SSID with Network ID and PSK Number
                    psk=desired_psk # Assign new value
                )
                print(f'PSK updated to {desired_psk}')

                # RESET PSK FOR DEMO PURPOSES
                ssid_update_response = dashboard.wireless.updateNetworkWirelessSsid(
                    network['id'], ssid['number'],
                    psk='not_sketchers'
                )

print('Job complete, all target matching PSKs updated')






