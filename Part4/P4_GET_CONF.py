import requests
from requests.auth import HTTPBasicAuth

# Router information
ROUTER_IP = "192.168.56.101"
USERNAME = "cisco"
PASSWORD = "cisco123!"

# RESTCONF endpoint
url = f"https://{ROUTER_IP}/restconf/data/native/interface/GigabitEthernet1"

# Headers
headers = {
    "Accept": "application/yang-data+json",
}

# Sending GET request to read the configuration
response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=headers, verify=False)

# Checking response status
if response.status_code == 200:
    # Printing the configuration
    print("Loopback Interface lo14 Configuration:")
    print(response.json())
else:
    print(f"Failed to read Loopback interface lo14 configuration. Status Code: {response.status_code}")
    print(response.text)
