import requests
import json
from nexus import device
from headers import headers

#specifying the url using my device variables set in nexus.py
url = f"https://{device['ip']}:{device['port']}/ins"

#the command line command in cli show format
show_cmd = {
    "ins_api":{
  "version": "1.0",
  "type": "cli_show",
  "chunk": "0",
  "sid": "1",
  "input": "show ip interface brief",
  "output_format": "json"
    }

}


#Getting the response in a json format and printing it
response = requests.post(url, data = json.dumps(show_cmd), headers = headers, 
auth = (device['username'], device['password']), verify = False).json()
print(json.dumps(response, indent=2, sort_keys=2))