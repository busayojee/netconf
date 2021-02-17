from webexteamssdk import WebexTeamsAPI
import json

auth = WebexTeamsAPI(access_token="MDNmYTNkNGQtNDMyZC00NzZlLWJkZWMtZjU5MDkxODAyYmQ5ODkzZTJiOGUtYTdh_PF84_f7a71b70-3805-4c84-8648-f3dfcd33405f",
                     base_url="https://api.ciscospark.com/v1/teams")



Team_list = auth.teams.list()
for team in Team_list:
    print(team)
    if getattr(team,"name") == "CBT":
        team_id = getattr(team, "id")

    # create new team
    # if getattr(team,"name") != "CBT":
    #     create_team = auth.teams.create("CBT")
    #     team_id = getattr(create_team,"id")
    #     print(team_id)
    # else:
    #     print(team)
# Team_list = auth.teams.list()
# for team in Team_list:
    #print(team)

# deleting team
# auth.teams.delete("Y2lzY29zcGFyazovL3VzL1RFQU0vNGRiOTM4NDAtNmZiNS0xMWViLWJjODgtYTNiZDEyYWVjMWRl")

#create new person
# person1 = auth.team_memberships.create(team_id,personEmail="busayoalabi1234@gmail.com",isModerator=False)
# lists = auth.team_memberships.list(team_id)
# for list in lists:
#     print(list)

# create new room
#create_room = auth.rooms.create("CBTs room", team_id)
#auth.rooms.delete("Y2lzY29zcGFyazovL3VzL1JPT00vNjNmZTBhMjAtNmZiYy0xMWViLTk0Y2EtNWRiNTQwMjM5NmM3")
list_room = auth.rooms.list(team_id)
for room in list_room:
    print(room)
    room_id = getattr(room, "id")
# print(room_id)

#Creating new mwssages
new_message = auth.messages.create(room_id, text="Hello Everyone")
