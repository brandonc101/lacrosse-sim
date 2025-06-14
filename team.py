class Team:
    def __init__(self, name, conference, division, players=None):
        self.name = name
        self.conference = conference
        self.division = division
        self.players = players if players is not None else []
        self.lineup = []  # Active 10 players for the game
        self.score = 0    # Used during game simulation

    def add_player(self, player):
        self.players.append(player)

    def select_lineup(self):
        # Pick top players by position based on relevant stats

        attackers = sorted(
            [p for p in self.players if p.position == "Attacker"],
            key=lambda x: x.offense,
            reverse=True
        )[:3]

        midfielders = sorted(
            [p for p in self.players if p.position == "Midfielder"],
            key=lambda x: x.passing + x.offense,
            reverse=True
        )[:3]

        defensemen = sorted(
            [p for p in self.players if p.position == "Defenseman"],
            key=lambda x: x.defense,
            reverse=True
        )[:3]

        goalies = sorted(
            [p for p in self.players if p.position == "Goalie"],
            key=lambda x: x.goalkeeping,
            reverse=True
        )[:1]

        self.lineup = attackers + midfielders + defensemen + goalies

    def __str__(self):
        return f"{self.name} ({self.conference} - {self.division}) with {len(self.players)} players"
