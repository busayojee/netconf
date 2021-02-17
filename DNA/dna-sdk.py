from dnacentersdk import api
import json
from pprint import pprint
import time
import calendar

dna = api.DNACenterAPI(base_url="https://sandboxdnac2.cisco.com:443",username="devnetuser",password="Cisco123!",version="1.2.10",verify=False)

#get sites
# sites = dna.networks.get_site_topology()
# pprint(sites)

#get vlans
vlans = dna.networks.get_vlan_details()
#pprint(vlans)

#get devices
devices = dna.devices.get_device_list()
#pprint(devices)
# for device in devices.response:
#     print(f'Type: {device.type}')
#     print(f'Man IP: {device.apManagerInterfaceIp}')
#     print(f'Software: {device.softwareType}')
#     print(f'Hostname: {device.hostname}')
#     print(f'ID: {device.id}')
#     print(' ')

#get device by id
device_id = dna.devices.get_device_by_id('98d31cdd-f697-42aa-a934-daa3806ce39f')
#pprint(device_id)

#get client health
timestamps = calendar.timegm(time.gmtime())
client_health = dna.clients.get_overall_client_health(timestamp=str(timestamps))
#pprint(client_health)

#get network health
net_health = dna.networks.get_overall_network_health(timestamp=str(timestamps))
pprint(net_health)
#get site health

site_health = dna.sites.get_site_health(timestamp='')
pprint(site_health)