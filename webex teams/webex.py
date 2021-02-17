import requests
import json
from pprint import pprint
#My token
token = "MDNmYTNkNGQtNDMyZC00NzZlLWJkZWMtZjU5MDkxODAyYmQ5ODkzZTJiOGUtYTdh_PF84_f7a71b70-3805-4c84-8648-f3dfcd33405f"
#creating a team
url = "https://api.ciscospark.com/v1/teams"
headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}
body = {
    "name":"Busayo new team"
}
# response = requests.post(url, headers=headers, data=json.dumps(body), verify=False).json()
# pprint(response)

get_response = requests.get(url, headers=headers).json()
teams = get_response['items']
for team in teams:
    if team['name']=='Busayo new team':
        team_id = team['id']
# print(team_id)

#create a room
url = "https://api.ciscospark.com/v1/rooms"
body_room = {
    "title":"New Room",
    "teamId": team_id
}
# response = requests.post(url,headers=headers, data=json.dumps(body_room),verify = False).json()
# pprint(response)
get_response = requests.get(url,headers=headers,verify = False).json()
rooms = get_response['items']
for room in rooms:
    if room['title'] =='New Room':
        room_id = room['id']
#print(room_id)

# Creating a message
url = "https://api.ciscospark.com/v1/messages"
body_msg = {
    "roomId":room_id,
    "text":"My first message from my python script"
}
response = requests.post(url, headers=headers, data=json.dumps(body_msg), verify=False).json()
pprint(response)