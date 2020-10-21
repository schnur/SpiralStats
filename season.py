from yahoo_oauth import OAuth2
import yahoo_fantasy_api 
import json 

with open('free_agent_details.json', 'r') as free_agent_details_file:
    free_agent_details = json.load(free_agent_details_file)

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yahoo_fantasy_api.Game(sc, 'nfl')
lg = gm.to_league('399.l.1201487')


player_ids = []

with open('season_stats.json', 'r') as season_stats_file:
    season_stats = json.load(season_stats_file)
        
for player in free_agent_details:  
    if not (player in season_stats):
        player_season_stats = lg.player_stats([free_agent_details[player]['player_id']], 'season')[0]
        player_name = free_agent_details[player]['name']['full']
        season_stats[player_name] = player_season_stats
        with open('season_stats.json', 'w') as season_stats_file:
            json.dump(season_stats, season_stats_file)  
    
