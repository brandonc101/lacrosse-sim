import os
import json
import random
from player import Player

ROSTERS_DIR = "teams"

POSITIONS = ["Attacker", "Midfielder", "Defenseman", "Goalie"]
COLLEGES = ["Syracuse", "Duke", "Maryland", "Virginia", "Denver", "Cornell", "Yale", "Notre Dame"]
HOMETOWNS = ["Baltimore", "Toronto", "Philadelphia", "Boston", "Rochester", "Calgary", "Denver", "New York"]
NATIONALITIES = ["USA", "Canada"]

FIRST_NAMES = [
    "James", "Liam", "Noah", "Lucas", "Ethan", "Logan", "Mason", "Oliver", "Benjamin", "Elijah",
    "Aiden", "Henry", "Jackson", "Sebastian", "Jack", "Owen", "Gabriel", "Carter", "Jayden", "Luke"
]
LAST_NAMES = [
    "Smith", "Johnson", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee"
]

def random_player(position):
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    college = random.choice(COLLEGES)
    age = random.randint(21, 34)
    experience = random.randint(1, age - 18)
    hometown = random.choice(HOMETOWNS)
    nationality = random.choice(NATIONALITIES)

    offense = random.randint(50, 99)
    defense = random.randint(50, 99)
    passing = random.randint(50, 99)
    stamina = random.randint(50, 99)
    speed = random.randint(50, 99)
    goalkeeping = random.randint(50, 99) if position == "Goalie" else None

    return Player(
        first_name=first_name,
        last_name=last_name,
        college=college,
        age=age,
        experience=experience,
        hometown=hometown,
        nationality=nationality,
        position=position,
        offense=offense,
        defense=defense,
        passing=passing,
        stamina=stamina,
        speed=speed,
        goalkeeping=goalkeeping,
    )

def create_default_roster(team_name):
    file_path = os.path.join(ROSTERS_DIR, f"{team_name.replace(' ', '_')}.json")

    # If file exists, load and return the players
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            players = []
            for pdata in data:
                players.append(Player(
                    first_name=pdata["first_name"],
                    last_name=pdata["last_name"],
                    college=pdata["college"],
                    age=pdata["age"],
                    experience=pdata["experience"],
                    hometown=pdata["hometown"],
                    nationality=pdata["nationality"],
                    position=pdata["position"],
                    offense=pdata["offense"],
                    defense=pdata["defense"],
                    passing=pdata["passing"],
                    stamina=pdata["stamina"],
                    speed=pdata["speed"],
                    goalkeeping=pdata.get("goalkeeping"),
                ))
            return players

    # Otherwise generate new roster
    players = []

    def add_players(position, count):
        for _ in range(count):
            players.append(random_player(position))

    add_players("Attacker", 6)
    add_players("Midfielder", 6)
    add_players("Defenseman", 6)
    add_players("Goalie", 2)
    add_players(random.choice(POSITIONS), 5)  # Flexible extra

    # Save roster to file
    with open(file_path, "w") as f:
        json.dump([p.to_dict() for p in players], f, indent=2)

    return players
