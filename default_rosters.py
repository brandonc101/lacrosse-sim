import json
import os
import random
from player import Player

FIRST_NAMES = ["John", "Mike", "Chris", "David", "Alex", "Ryan", "Matt", "Nick", "Jake", "Luke"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Wilson", "Taylor", "Anderson"]
COLLEGES = ["Syracuse", "Johns Hopkins", "Cornell", "Duke", "Maryland"]
HOMETOWNS = ["Boston", "New York", "Toronto", "Philadelphia", "Vancouver"]
NATIONALITIES = ["USA", "Canada"]

positions = ["Attacker"] * 6 + ["Midfielder"] * 8 + ["Defenseman"] * 7 + ["Goalie"] * 4

ROSTER_DIR = "rosters"  # folder to store team roster files

if not os.path.exists(ROSTER_DIR):
    os.makedirs(ROSTER_DIR)

def random_player_data(i, pos):
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    college = random.choice(COLLEGES)
    hometown = random.choice(HOMETOWNS)
    nationality = random.choice(NATIONALITIES)
    age = random.randint(20, 30)
    experience = random.randint(1, 10)

    if pos == "Goalie":
        offense = random.randint(5, 15)
        defense = random.randint(70, 90)
        passing = random.randint(20, 40)
        stamina = random.randint(60, 80)
        speed = random.randint(40, 60)
    elif pos == "Defenseman":
        offense = random.randint(30, 50)
        defense = random.randint(65, 85)
        passing = random.randint(40, 60)
        stamina = random.randint(65, 85)
        speed = random.randint(50, 70)
    elif pos == "Midfielder":
        offense = random.randint(55, 75)
        defense = random.randint(50, 70)
        passing = random.randint(65, 85)
        stamina = random.randint(75, 95)
        speed = random.randint(65, 85)
    else:  # Attacker
        offense = random.randint(70, 90)
        defense = random.randint(30, 50)
        passing = random.randint(50, 70)
        stamina = random.randint(70, 90)
        speed = random.randint(70, 90)

    player_name = f"{first_name} {last_name}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "college": college,
        "age": age,
        "experience": experience,
        "hometown": hometown,
        "nationality": nationality,
        "name": player_name,
        "position": pos,
        "offense": offense,
        "defense": defense,
        "passing": passing,
        "stamina": stamina,
        "speed": speed,
    }


def create_default_roster(team_name):
    # File path for this team's roster JSON
    safe_team_name = team_name.replace(" ", "_").lower()
    roster_file = os.path.join(ROSTER_DIR, f"{safe_team_name}_roster.json")

    if os.path.exists(roster_file):
        # Load roster from file
        with open(roster_file, "r") as f:
            roster_data = json.load(f)
    else:
        # Generate new random roster and save
        roster_data = []
        for i, pos in enumerate(positions, 1):
            pdata = random_player_data(i, pos)
            roster_data.append(pdata)
        with open(roster_file, "w") as f:
            json.dump(roster_data, f, indent=2)

    # Convert JSON dicts back to Player objects
    players = []
    for pdata in roster_data:
        player = Player(
            first_name=pdata["first_name"],
            last_name=pdata["last_name"],
            college=pdata["college"],
            age=pdata["age"],
            experience=pdata["experience"],
            hometown=pdata["hometown"],
            nationality=pdata["nationality"],
            name=pdata["name"],
            position=pdata["position"],
            offense=pdata["offense"],
            defense=pdata["defense"],
            passing=pdata["passing"],
            stamina=pdata["stamina"],
            speed=pdata["speed"],
        )
        players.append(player)

    return players
