from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()

#pprint(orgs)

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        org_id = org['id']
#print(org_id)

params = {}
params['organization_id'] = org_id

networks = meraki.networks.get_organization_networks(params)
pprint(networks)

for net in networks:
    if net['name'] == 'DNSMB1':
        net_id = net['id']
#print(net_id)

vlans = meraki.vlans.get_network_vlans(net_id)
#pprint(vlans)

vlan = vlans[0]
vlan['name'] = 'Busayo vlan'

updated_vlan = {}
updated_vlan['network_id'] = net_id
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan

#result = meraki.vlans.update_network_vlan(updated_vlan)

result_vlan = meraki.vlans.get_network_vlans(net_id)
pprint(result_vlan)
