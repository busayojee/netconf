import requests
import json
from pprint import pprint

#logging into the Apic
url =  'https://sandboxapicdc.cisco.com/api/aaaLogin.json'

payload = {
    "aaaUser":{
        "attributes":{
            "name":"admin",
            "pwd":"ciscopsdt"
        }
    }
}

headers = {
    "clear-cache":"no-cache",
    "Content-Type":"application/json"
}

response = requests.post(url, headers = headers, data=json.dumps(payload), verify = False ).json()

#placing the token in a cookie dictionary
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

#getting all the tenants 
tenant_url = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"
response_tenant  = requests.get(tenant_url, headers = headers, cookies = cookie, verify = False).json()
#pprint(response_tenant)

#getting all the apps
app_url = "https://sandboxapicdc.cisco.com/api/node/class/fvAp.json"

response_app = requests.get(app_url, headers = headers, cookies = cookie, verify = False).json()
#pprint(response_app)

#getting a managed object
app = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"
answer = requests.get(app, headers = headers, cookies = cookie, verify = False).json()
#pprint(answer)

#updating the discripion of the managed object
update_url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"
updated_data = {
    "imdata":[
        {
            "fvAp":{
                "attributes":{
                    "descr":"",
                    "dn":"uni/tn-Heroes/ap-Save_The_Planet"
                }
            }
        }
    ]
}
update_response = requests.post(update_url, headers = headers, cookies = cookie, data = json.dumps(updated_data), verify = False).json()
answer = requests.get(app, headers = headers, cookies = cookie, verify = False).json()
pprint(answer)
