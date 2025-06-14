class Player:
    def __init__(self, first_name, last_name, college, age, experience,
                 hometown, nationality, position,
                 offense, defense, passing, stamina, speed,
                 goalkeeping=0):  # default to 0 for non-goalies

        self.first_name = first_name
        self.last_name = last_name
        self.college = college
        self.age = age
        self.experience = experience
        self.hometown = hometown
        self.nationality = nationality
        self.position = position

        self.offense = offense
        self.defense = defense
        self.passing = passing
        self.stamina = stamina
        self.speed = speed
        self.goalkeeping = goalkeeping

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
