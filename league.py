from yahoo_oauth import OAuth2
import yahoo_fantasy_api 
import json 

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yahoo_fantasy_api.Game(sc, 'nfl')
lg = gm.to_league('399.l.1201487')


with open('teams.json', 'r') as f:
    teams = json.load(f)


team = lg.to_team('399.l.1201487.t.2')
team.add_player(24788)
roster = team.roster()

print(roster)