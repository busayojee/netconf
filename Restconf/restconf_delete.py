import requests
import json
from pprint import pprint
from router import router
from headers import headers

module = "ietf-interfaces:interfaces"
url = f"https://{router['ip']}:{router['port']}/restconf/data/{module}/interface=Loopback1000"

response = requests.delete(url, headers = headers, auth = (router['username'], router['password']), verify = False)
if  response.status_code == 204:
    print("Successfully deleted")
else:
    print("Issues with deleting")