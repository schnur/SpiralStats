from flask import Flask, render_template, request
import json
app = Flask(__name__)

with open('positions.json', 'r') as positions_file:
    positions = json.load(positions_file)

with open('free_agents.json', 'r') as free_agents_file:
    free_agents = json.load(free_agents_file)

with open('waivers.json', 'r') as waivers_file:
    waivers = json.load(waivers_file)

with open('free_agent_details.json', 'r') as free_agent_details_file:
    free_agent_details = json.load(free_agent_details_file)

with open('season_stats.json', 'r') as season_stats_file:
    season_stats = json.load(season_stats_file)

stats_words = {
    "Pass Yds": 'Passing Yards', 
    "Pass TD": 'Passing Touchdowns', 
    "Int": 'Interception', 
    "Rush Att": 'Rush Attempts', 
    "Rush Yds": 'Rush Yards', 
    "Rush TD": 'Rush Touchdown', 
    "Rec": 'Reception', 
    "Rec Yds": 'Recieving Yards', 
    "Rec TD": 'Recieving Touchdowns', 
    "Ret TD": 'Return Touchdowns', 
    "2-PT": '2 Point Convertion', 
    "Fum Lost": 'Fumble Lost', 
    "Fum Ret TD": 'Fumble Return Touchdowns', 
    "Targets": 'Targets'
}
@app.route('/')
def main():
    return render_template('players.html', positions=positions, free_agents = free_agents, free_agent_details = free_agent_details, waivers=waivers) 

@app.route('/players')
def players():
    player_name = request.args.get('player_name')
    player = free_agent_details[player_name]
    if (player_name in season_stats) and player:
        stats = season_stats[player_name]
        return render_template('player.html', player = player, stats = stats, stats_words = stats_words)
    else:
        return "Player Data Not Found"

@app.route('/compare')
def Compare():
    player_1 = request.args.get('player_1')
    player_2 = request.args.get('player_2')
    return 'Comparing ' + player_1 + ' and ' + player_2
    
if __name__ == '__main__':
    app.run()
