import requests
import json
from pprint import pprint
from router import router
from headers import headers

#The url using the variables from router.py and specifying the interface is gigint1
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

#Getting the config data for the url using requets
#specifying the headers from headers.py and using the variables for authentication
response = requests.get(url, headers = headers, auth = (router['username'], router['password']), verify = False)
if response.status_code == 200:
#converting into a python object
    api_data = response.json()

    #Querying the data
    print('/'*50)
    print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
    print('/'*50)
    if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
        print("interface is up")
else:
    print('Interface not found')