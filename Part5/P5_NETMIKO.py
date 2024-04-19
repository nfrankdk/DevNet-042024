from netmiko import ConnectHandler

# Define router details
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
}

# Establish SSH connection
net_connect = ConnectHandler(**router)
net_connect.enable()

# Task 1: Gather information with "show ip interface brief" and "show ip route"
print("Task 1: Gathering information with 'show ip interface brief' and 'show ip route'")
output_interface_brief = net_connect.send_command("show ip interface brief")
output_ip_route = net_connect.send_command("show ip route")
print("Output of 'show ip interface brief':")
print(output_interface_brief)
print("\nOutput of 'show ip route':")
print(output_ip_route)

# Task 2: Create Loopback interface lo15
print("\nTask 2: Creating Loopback interface lo15")
config_commands = [
    "interface Loopback15",
    "ip address 15.16.17.18 255.255.255.0",
    "no shutdown"
]
output = net_connect.send_config_set(config_commands)
print(output)

# Task 3: Create Loopback interface lo18
print("\nTask 3: Creating Loopback interface lo18")
config_commands = [
    "interface Loopback18",
    "ip address 16.17.18.1 255.255.255.0",
    "no shutdown"
]
output = net_connect.send_config_set(config_commands)
print(output)

# Task 4: Create a default static route
print("\nTask 4: Creating a default static route")
config_commands = [
    "ip route 0.0.0.0 0.0.0.0 Loopback15"
]
output = net_connect.send_config_set(config_commands)
print(output)

# Task 5: Gather information after configuration
print("\nTask 5: Gathering information with 'show ip interface brief' and 'show ip route'")
output_interface_brief = net_connect.send_command("show ip interface brief")
output_ip_route = net_connect.send_command("show ip route")
print("Output of 'show ip interface brief' after configuration:")
print(output_interface_brief)
print("\nOutput of 'show ip route' after configuration:")
print(output_ip_route)

# Disconnect SSH session
net_connect.disconnect()
