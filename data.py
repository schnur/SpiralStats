from yahoo_oauth import OAuth2
import yahoo_fantasy_api 
import webbrowser
import json 

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yahoo_fantasy_api.Game(sc, 'nfl')
print(gm.league_ids())
lg = gm.to_league('399.l.1201487')

with open('positions.json', 'r') as positions_file:
    positions = json.load(positions_file)
with open('free_agents.json', 'r') as free_agents_file:
    free_agents = json.load(free_agents_file)

with open('free_agent_details.json', 'r') as free_agent_details_file:
    free_agent_details = json.load(free_agent_details_file)

for position in positions:
    if position in free_agents:
        for player in free_agents[position]:
            if not (player["name"] in free_agent_details):
                try:
                    agent_details = lg.player_details(player["name"])
                    free_agent_details[player["name"]] = agent_details[0]
                except RuntimeError:
                    print(player["name"], 'was not found.')
                with open('free_agent_details.json', 'w') as free_agent_details_file:
                    json.dump(free_agent_details, free_agent_details_file)
            else:
                print(player["name"], "already on the list.")

        

# positions = lg.positions()
# for position in player_details:
# players = lg.free_agents('QB')
# parsed_player_data = []
# for player in players:
#     player_details = lg.player_details(player["name"])[0]
#     parsed_player_data.append({
#         "name" : player_details["name"]["full"],
#         "team" : player_details["editorial_team_full_name"],
#         "position" : player_details["primary_position"]
#   })

 
# with open('free_agents.json', 'r') as json_file:
#     data = json.load(json_file)

# positions = lg.positions()
# # for position in positions:
# #     if not(position in data) and position != "W/R/T":
# #         data[position] = []
# #         players = lg.free_agents(position)
# #         for player in players:
# #             data[position].append(player)
# #         with open('free_agents.json', 'w') as json_file:
# #             json.dump(data, json_file)
# #     print("parsed all", position)

# with open('positions.json', 'w') as json_file:
#     json.dump(positions, json_file)

# {
#     'QB' : [
#         {
#             "player_id": 5479, 
#             "name": "Drew Brees", 
#             "position_type": "O", 
#             "eligible_positions": ["QB"], 
#             "percent_owned": 94, 
#             "status": ""
#         }
#     ]
# }

# {
#     "QB" : {
#         "position_type": "O", 
#         "count": 1
#     },
# }

# def get_player_data():
#     return parsed_player_data


# drew_brees_details = lg.player_details('Aaron Rodgers')
# webbrowser.open(drew_brees_details[0]['headshot']['url'])
# print(drew_brees_details)
