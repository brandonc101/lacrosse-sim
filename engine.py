import random

def simulate_game(team1, team2):
    """
    Simulate a single game between two teams.
    Player attributes influence outcomes:
    - Average offense and defense of lineups affect scoring chances.
    - Stamina slightly modifies team performance.
    Returns the winning team.
    """

    def team_power(team):
        # Calculate average offense, defense, and stamina of players on field
        on_field = team.lineup  # assume team.lineup is list of 10 Player objects
        avg_offense = sum(p.offense for p in on_field) / len(on_field)
        avg_defense = sum(p.defense for p in on_field) / len(on_field)
        avg_stamina = sum(p.stamina for p in on_field) / len(on_field)

        # Combine stats into a power metric
        power = (avg_offense * 0.5) + (avg_defense * 0.3) + (avg_stamina * 0.2)
        return power

    power1 = team_power(team1)
    power2 = team_power(team2)

    total = power1 + power2
    if total == 0:
        prob_team1_wins = 0.5
    else:
        prob_team1_wins = power1 / total

    # Random outcome weighted by power
    winner = team1 if random.random() < prob_team1_wins else team2
    return winner

def simulate_regular_season(teams, schedule):
    """
    Simulate the entire regular season.
    Returns a dict mapping team names to wins.
    """
    wins = {team.name: 0 for team in teams}
    for team1, team2 in schedule:
        winner = simulate_game(team1, team2)
        wins[winner.name] += 1
    return wins

def get_playoff_teams(wins, teams, playoff_count=8):
    """
    Select top teams by wins for playoffs.
    Returns list of Team objects.
    """
    sorted_teams = sorted(teams, key=lambda t: wins[t.name], reverse=True)
    return sorted_teams[:playoff_count]

def simulate_playoffs(playoff_teams):
    """
    Single elimination playoff simulation.
    Returns the champion team.
    """
    round_teams = playoff_teams[:]
    while len(round_teams) > 1:
        winners = []
        for i in range(0, len(round_teams), 2):
            winner = simulate_game(round_teams[i], round_teams[i+1])
            winners.append(winner)
        round_teams = winners
    return round_teams[0]

def run_season(teams, schedule):
    """
    Run full season: regular + playoffs.
    Returns the champion Team object.
    """
    # Make sure each team has a valid lineup before simulating
    for team in teams:
        if not hasattr(team, "lineup") or len(team.lineup) != 10:
            team.select_lineup()  # fallback to default lineup if none set

    wins = simulate_regular_season(teams, schedule)
    playoff_teams = get_playoff_teams(wins, teams)
    champion = simulate_playoffs(playoff_teams)
    return champion
