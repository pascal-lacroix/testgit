import requests
import urllib3

# Disable warning for unverified SSL certificates
urllib3.disable_warnings()

host = "10.10.20.48"
port = 443
username = "developer"
password = "C1sco12345"

url = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces"
#url2 = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
}


def get_interfaces():
    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    if response.status_code != 200:
        print(f"Error {response.status_code}")
    return response.json()


def show_interfaces(data):
    interface_lijst = data["ietf-interfaces:interfaces"]["interface"]
    for interface in interface_lijst:
        name = interface['name']
        description = interface['description']
        print(f"{name}: {description}")

def config_interface(interface_number):
    configuratie = {
        "ietf-interfaces:interface": {
            "name": f"GigabitEthernet{interface_number}",
            "description": "Pascal_python_3",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
#            "ietf-ip:ipv4": {
#                "address": [
#                    {
#                        "ip": "10.2.1.1",
#                        "netmask": "255.255.255.0"
#                    }
#                ]
#            }
        }
    }
    response = requests.put(url + f"/interface=GigabitEthernet{interface_number}", headers=headers, auth=(username, password), verify=False, json=configuratie)
#    print(response.status_code)
#    print(response.text)

if __name__ == "__main__":
    data = get_interfaces()
    show_interfaces(data)
#    config_interface(interface_number)

interface_number = int(input('Which interface do you want to configure? '))

if interface_number == 1:
    print("error (we don't want to change interface 1)")
else:
    config_interface(interface_number)
    show_interfaces(data)
    print(show_interfaces(data))





