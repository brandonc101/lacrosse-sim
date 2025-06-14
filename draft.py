import random
from player import Player

def generate_position_player(name, position):
    attr = lambda: random.randint(8, 16)
    if position == "Goalie":
        return Player(name, 0, 0, 0, attr(), attr(), goalkeeping=random.randint(12, 18),
                      is_goalie=True, position="Goalie")
    else:
        return Player(name, attr(), attr(), attr(), attr(), attr(), position=position)

def generate_team_roster(team_name):
    roster = []
    for i in range(3):
        roster.append(generate_position_player(f"{team_name} A{i+1}", "Attacker"))
        roster.append(generate_position_player(f"{team_name} M{i+1}", "Midfielder"))
        roster.append(generate_position_player(f"{team_name} D{i+1}", "Defenseman"))
    roster.append(generate_position_player(f"{team_name} G1", "Goalie"))  # 1 goalie
    for i in range(15):  # 15 bench players, mixed
        pos = random.choice(["Attacker", "Midfielder", "Defenseman"])
        roster.append(generate_position_player(f"{team_name} Bench{i+1}", pos))
    return roster
