import requests
from requests.auth import HTTPBasicAuth
import json

# Router information
ROUTER_IP = "192.168.56.101"
USERNAME = "cisco"
PASSWORD = "cisco123!"

# Forbindelse til router
url = f"https://192.168.56.101/restconf/data/native/interface/Loopback"

# Headers
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Konfiguration af interface
data = {
    "Loopback": {
        "name": 14,
        "description": "Loopback Interface 14",
        "ip": {
            "address": {
                "primary": {
                    "address": "17.16.15.14",
                    "mask": "255.255.255.0"
                }
            }
        }
    }
}

##### BRUGERLOGIN på Cisco ROUTEREN
response = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=headers, json=data, verify=False)

if response.status_code == 201:
    print("Loopback interface lo14 created and configured successfully.")
else:
    print(f"Failed to create and configure Loopback interface lo14. Status Code: {response.status_code}")
    print(response.text)