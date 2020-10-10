from flask import Flask, render_template
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


@app.route('/')
def main():
    return render_template('index.html', positions=positions, free_agents = free_agents, free_agent_details = free_agent_details, waivers=waivers) 
    
if __name__ == '__main__':
    app.run()
