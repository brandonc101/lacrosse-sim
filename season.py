import random

class Season:
    def __init__(self, teams):
        self.teams = teams
        self.standings = {team.name: 0 for team in teams}
        self.schedule = self._generate_balanced_schedule()

    def _generate_balanced_schedule(self):
        schedule = []
        divisions = {}
        for team in self.teams:
            divisions.setdefault(team.division, []).append(team)

        for division_teams in divisions.values():
            for i in range(len(division_teams)):
                for j in range(i + 1, len(division_teams)):
                    schedule.append((division_teams[i], division_teams[j], "home"))
                    schedule.append((division_teams[j], division_teams[i], "home"))

        for team in self.teams:
            opponents = [t for t in self.teams if t != team and t.division != team.division]
            chosen = random.sample(opponents, 6)
            for opp in chosen:
                schedule.append((team, opp, "home"))
        return schedule

    def play_season(self, engine):
        for home, away, _ in self.schedule:
            home.score, away.score = 0, 0
            log = engine.simulate_match(home, away)
            if home.score > away.score:
                self.standings[home.name] += 3
            elif away.score > home.score:
                self.standings[away.name] += 3
            else:
                self.standings[home.name] += 1
                self.standings[away.name] += 1
            engine.print_result(home, away, log)

        self.print_standings()
        self.run_playoffs(engine)

    def print_standings(self):
        print("\n--- Final Standings ---")
        for team, pts in sorted(self.standings.items(), key=lambda x: -x[1]):
            print(f"{team}: {pts} pts")

    def run_playoffs(self, engine):
        print("\n--- Playoffs ---")
        # Top 2 teams from each conference (simplified by matching names)
        east = [t for t in self.teams if t.conference == "East"]
        west = [t for t in self.teams if t.conference == "West"]

        top_east = sorted(east, key=lambda t: -self.standings[t.name])[:2]
        top_west = sorted(west, key=lambda t: -self.standings[t.name])[:2]

        semi_1 = (top_east[0], top_east[1])
        semi_2 = (top_west[0], top_west[1])

        finalists = []
        for t1, t2 in [semi_1, semi_2]:
            t1.score = t2.score = 0
            log = engine.simulate_match(t1, t2)
            winner = t1 if t1.score > t2.score else t2
            engine.print_result(t1, t2, log)
            finalists.append(winner)

        # Final match
        t1, t2 = finalists
        t1.score = t2.score = 0
        print("\n--- Final ---")
        log = engine.simulate_match(t1, t2)
        winner = t1 if t1.score > t2.score else t2
        engine.print_result(t1, t2, log)
        print(f"Champion: {winner.name}")
