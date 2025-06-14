import json
from player import Player
from team import Team

def save_teams(filename, teams):
    data = []
    for team in teams:
        team_data = {
            'name': team.name,
            'players': [{
                'name': p.name,
                'offense': p.offense,
                'defense': p.defense,
                'passing': p.passing,
                'stamina': p.stamina,
                'speed': p.speed,
                'goalkeeping': p.goalkeeping,
                'is_goalie': p.is_goalie
            } for p in team.players]
        }
        data.append(team_data)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_teams(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    teams = []
    for team_data in data:
        players = [
            Player(**p) for p in team_data['players']
        ]
        teams.append(Team(team_data['name'], players))
    return teams
