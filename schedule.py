from collections import defaultdict
from itertools import combinations

def build_lacrosse_schedule(teams):
    """
    Build a full season schedule:
    - Each team plays division opponents twice
    - Each team plays every other team once
    - No team plays more than once against the same non-division opponent
    Returns a list of (team1, team2) tuples
    """
    schedule = []
    scheduled = set()

    # Index by division
    division_map = defaultdict(list)
    for team in teams:
        division_map[(team.conference, team.division)].append(team)

    # Step 1: Division rivals (each team plays other 2 teams in division twice)
    for division_teams in division_map.values():
        for i in range(len(division_teams)):
            for j in range(i + 1, len(division_teams)):
                team1 = division_teams[i]
                team2 = division_teams[j]
                game1 = (team1.name, team2.name)
                game2 = (team2.name, team1.name)

                if game1 not in scheduled and game2 not in scheduled:
                    schedule.append((team1, team2))
                    schedule.append((team2, team1))
                    scheduled.add(game1)
                    scheduled.add(game2)

    # Step 2: All other matchups (outside division) once
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            team1 = teams[i]
            team2 = teams[j]
            if (team1.name, team2.name) in scheduled or (team2.name, team1.name) in scheduled:
                continue

            if team1.division == team2.division and team1.conference == team2.conference:
                continue  # already handled as division rivals

            schedule.append((team1, team2))
            scheduled.add((team1.name, team2.name))
            scheduled.add((team2.name, team1.name))  # prevent duplicate reverse later

    return schedule
