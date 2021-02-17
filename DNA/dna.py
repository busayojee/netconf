import requests
import json
from pprint import pprint

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
pwd = "Cisco123!"

headers = {
    'Content-Type':'application/json'
}

response = requests.post(url,auth = (username,pwd), headers = headers, verify = False).json()

token = response['Token']
#print(token)

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

querystring = {
    'timestamps':''
}
headers = {
    'x-auth-token':token
}
response = requests.get(url, headers=headers, params=querystring, verify = False).json()
#pprint(response)

response_client = response['response'][0]['scoreDetail'][0]['clientCount']
print('Clients:',response_client)

scores = response['response'][0]['scoreDetail']
print(' ')
for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f'Wired Clients: {score["scoreList"][0]["clientCount"]}')
        score_values = score['scoreList']
        for score_value in score_values:
            print(f'Value: {score_value["scoreCategory"]["value"]}:{score_value["clientCount"]}')

print(' ')

for score in scores:
    if score['scoreCategory']['value'] == 'WIRELESS':
        print(f'Wireless Clients: {score["scoreList"][0]["clientCount"]}')
        score_values = score['scoreList']
        for score_value in score_values:
            print(f'Value: {score_value["scoreCategory"]["value"]}:{score_value["clientCount"]}')
        
