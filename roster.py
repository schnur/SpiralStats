from yahoo_oauth import OAuth2
import yahoo_fantasy_api 
import json 

with open('free_agent_details.json', 'r') as free_agent_details_file:
    free_agent_details = json.load(free_agent_details_file)

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yahoo_fantasy_api.Game(sc, 'nfl')
lg = gm.to_league('399.l.1201487')

roster = ['Deshaun Watson', 'Todd Gurley II', 'Josh Jacobs', 'Tyler Lockett', 'DJ Moore']
roster_ids = []

for player_name in roster:
    roster_ids.append(int(free_agent_details[player_name]['player_id']))

player_stats = lg.player_stats(roster_ids, 'season')
print(player_stats)

