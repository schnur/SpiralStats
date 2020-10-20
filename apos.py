from yahoo_oauth import OAuth2
import yahoo_fantasy_api 
import webbrowser
import json 
import urllib.parse

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yahoo_fantasy_api.Game(sc, 'nfl')
print(gm.league_ids())
lg = gm.to_league('399.l.1201487')

agent_details = lg.player_details(26671)
print(agent_details)