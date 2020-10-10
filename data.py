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
    
with open('waivers.json', 'r') as waivers_file:
    waivers = json.load(waivers_file)

with open('free_agent_details.json', 'r') as free_agent_details_file:
    free_agent_details = json.load(free_agent_details_file)

# for position in positions:
#     if position in free_agents:
#         for player in free_agents[position]:
#             if not (player["name"] in free_agent_details):
#                 try:
#                     agent_details = lg.player_details(player["name"])
#                     free_agent_details[player["name"]] = agent_details[0]
#                 except RuntimeError:
#                     print(player["name"], 'was not found.')
#                 with open('free_agent_details.json', 'w') as free_agent_details_file:
#                     json.dump(free_agent_details, free_agent_details_file)
#             else:
#                 print(player["name"], "already on the list.")


for position in positions:
    if position in waivers:
        for player in waivers[position]:
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

