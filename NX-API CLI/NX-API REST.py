import requests
from pprint import pprint
import json

#Gotten from postman
url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload="{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\":\"admin\",\n            \"pwd\":\"Admin_1234!\"\n        }\n    }\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'APIC-cookie=d4fwLZTkX6jtgrhLW7X4raUWSvRNpyv7hJ5M/6WZ9X4+x7z+By7NN28SYE5btsuBN04R76GIlFYJLGfPR9MUy0CFG34K+RhNksEn3reaq9bGyf+IhvjWbKmffwzN2gRcAnQpQuTCkCHoBjkh9gzBnPAVz1G/ky8CjzdD1P69huw=; nxapi_auth=dzqnf:uTMuw7cKR4Qv+fVy9G5h7t5SxRQ='
}

#The response converted to a json object by adding .json() to the end
response = requests.post(url, headers=headers, data=payload, verify = False).json()

#pprint(response)

#getting the token from the json output
token = response['imdata'][0]['aaaLogin']['attributes']['token']
print(token)
#creating a cookies dictionary
cookies = {}
#specifying an object in the cookies dictionary called APIC-cookie into a token
cookies['APIC-cookie'] = token


#copy from postman
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/33].json"
#add whatever you wanna change
payload="{\n    \"l1PhysIf\":{\n        \"attributes\":{\n            \"descr\":\"\"\n        }\n    }\n}"
headers = {
  
  'Content-Type': 'text/plain',
}
#make the response data a json pyhon object
response = requests.put(url, headers=headers, data=payload,cookies = cookies, verify = False).json()

pprint(response)
