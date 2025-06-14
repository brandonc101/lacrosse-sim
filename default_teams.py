from team import Team
from default_rosters import create_default_roster

def get_default_teams():
    teams_info = [
        # East Conference - North East Division
        ("Boston Blazers", "East", "North East"),
        ("New York Titans", "East", "North East"),
        ("Toronto Thunder", "East", "North East"),

        # East Conference - South East Division
        ("Philadelphia Phantoms", "East", "South East"),
        ("Washington Warriors", "East", "South East"),
        ("Charlotte Chargers", "East", "South East"),

        # West Conference - North West Division
        ("Vancouver Vipers", "West", "North West"),
        ("Seattle Stingers", "West", "North West"),
        ("Calgary Cyclones", "West", "North West"),

        # West Conference - South West Division
        ("Denver Dragons", "West", "South West"),
        ("San Diego Sharks", "West", "South West"),
        ("Las Vegas Lightning", "West", "South West"),
    ]

    teams = []
    for name, conf, div in teams_info:
        roster = create_default_roster(name)  # loads or creates unique roster per team
        team = Team(name=name, conference=conf, division=div, players=roster)
        teams.append(team)
    return teams
