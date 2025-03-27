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

# Setting Org ID (can be set based on API call or from documentation, if always using the same Org.
organization_id = '<<Org ID Here>>'


### TASK ###
# Get a list of all networks : Response object is a list of dictionaries
# network_list = ?
############

# Print all network list data
# pprint(networks_list)

# SELECT NETWORK BASED ON CRITERIA

# Define loop variables for clarity
target = 'home stack'   # Define the target we will be matching on
target_networks = []    # Define the list of networks we care about

### TASK ###
# Loop through all networks in networks_list.
# Print their names.
# If the name matches the target, append it to target_networks
############

# Loop through list of networks: Each network is a dictionary object
for ? in ?:   # network is a dictionary

    # Check if network name matches target (can match based on any attribute, does not have to be name)
    if ? in ?:
        target_networks.append(?)

# Print target network data
pprint(target_networks)

# Define SSID target variable and the desire PSK.
ssid_target = 'Python'
desired_psk = 'sketchers'   # This can be set based on an external settings file if desired.

### TASK ###
# Loop through all networks in desired_networks.
# If the SSID name matches the target, check the PSK
# If the PSK does not match the desired_psk, update it
############
for ? in ?: # Loop Through All Relevant Networks

    # https://developer.cisco.com/meraki/api-v1/get-network-wireless-ssid/
    ssid_list = ?   # API call to get list of SSIDs

    # pprint(ssid_list)

    for ? in ?:  # Loop through all SSID dicts in SSID list

        if ? in ?: # Match based on SSID target name

            print(f"Password for SSID {?} is {?}") # Print Current Password

            if ? is not ?: # Check if PSK is set to desired PSK

                # Update SSID with new PSK value
                #https://developer.cisco.com/meraki/api-v1/update-network-wireless-ssid/
                ssid_update_response = ?
                print(f'PSK updated to {desired_psk}')



print('Job complete, all target matching PSKs updated')






