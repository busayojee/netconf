import requests
import json
from pprint import pprint

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
pwd = 'Cisco123!'

headers = {
    'Content-Type':'application/json'
}
response = requests.post(url, auth = (username,pwd)).json()
token = response['Token']
#print(token)

url = 'https://sandboxdnac2.cisco.com//dna/intent/api/v1/client-detail?timestamp=&macAddress=00:00:2A:01:00:2E'

headers = {
    'x-auth-token':token,
    'Accept':'*/*'
}

response = requests.get(url, headers=headers).json()
pprint(response)

