import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload="{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\":\"admin\",\n            \"pwd\":\"Admin_1234!\"\n        }\n    }\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'APIC-cookie=/dIpWUGjQQUYKCddpRimllocJKpCn2UOkUBlUw+sLbtIKCxcsRVy7OyNjpzKMOuBErZ1jNDWTqiZCrCfNSYKKuP97t8ftaYq3k+VnrIzIdqCioPTbr3AB43ATX3bjN8pQ364zn1rUZwwgoTTm3K2wpzUld74z5UHJSetj8dypTw=; nxapi_auth=dzqnf:uTMuw7cKR4Qv+fVy9G5h7t5SxRQ='
}

response = requests.post(url, headers=headers, data=payload, verify = False).json()

#pprint(response)
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token
pprint(token)

url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/33].json"

payload={}
headers = {
    'Content-Type':'application/json'
  }

response = requests.get(url, headers=headers,cookies = cookies, data=payload, verify = False).json()

pprint(response)
