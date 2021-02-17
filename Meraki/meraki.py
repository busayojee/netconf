import requests
import json
from pprint import pprint

url = "https://dashboard.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.get(url, headers=headers, data=payload).json()

#pprint(response)

for org_name in response:
    if org_name['name'] == 'DevNet Sandbox':
        org_id = org_name['id'] 
#print(org_id)

url_net = "https://dashboard.meraki.com/api/v0/organizations/" + org_id + "/networks"

response_net = requests.get(url_net, headers=headers, data=payload).json()
#pprint(response_net)

for net_name in response_net:
    if net_name['name'] == 'DNSMB4':
        net_id = net_name['id']
#print(net_id)

url_devices = "https://dashboard.meraki.com/api/v0/networks/" + net_id + "/devices"

response_devices = requests.get(url_devices, headers=headers, data=payload).json()

#pprint(response_devices)

url_clients = "https://dashboard.meraki.com/api/v0/networks/" + net_id + "/clients"

response_clients = requests.get(url_clients, headers=headers, data=payload).json()

pprint(response_clients)