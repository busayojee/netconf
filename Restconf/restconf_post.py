import requests
import json
from pprint import pprint
from router import router
from headers import headers



module = "ietf-interfaces:interfaces"
url = f"https://{router['ip']}:{router['port']}/restconf/data/{module}"

payload = {
    "ietf-interfaces:interface":[
            {
            "name":"Loopback1000",
            "description":"Added by Oluwabusayo",
            "type":"iana-if-type:softwareLoopback",
            "enabled":"true",
            "ietf-ip:ipv4":{
                "address":[
                    {
                        "ip":"172.16.100.1",
                        "netmask":"255.255.255.0"
                    }
                ]
            }
        }
    ]

}

response = requests.post(url, headers = headers, data = json.dumps(payload), auth = (router['username'], router['password']), verify = False)
if (response.status_code == 201):
    print("Successfully added interface")
else:
    print("Issue with adding interface")

    