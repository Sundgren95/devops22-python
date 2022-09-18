# Exercise 5 extra
import random

class Person:
    def __init__(self, name, born):
        self.name = name
        self.born = born


class Player(Person):
    def __init__(self, name, born, speed, agility, strenght):
        super().__init__(name, born)
        self.speed = speed
        self.agility = agility
        self.strenght = strenght

    def __str__(self):
        return f"{self.name}, born: {self.born} - speed: {self.speed} agility: {self.agility} strenght: {self.strenght}"


class Coach(Person):
    def __init__(self, name, born, voice_level):
        super().__init__(name, born)
        self.voice_level = voice_level
        
    def __str__(self):
        return f"{self.name}, born {self.born}, voice level {self.voice_level}"


class Team:
    def __init__(self, players, coach):
        self.players = players
        self.choach = coach

    def summarize_team(self):
        team = "--------------- Coach ---------------\n"
        team += f"Coach {self.choach}\n"
        team += "-------------- Players --------------\n"
        team += "\n".join(map(str, self.players))
        return team


def random_voice_level():
    return random.randint(1, 10)

def random_speed():
    return random.randint(1, 10)

def random_agility():
    return random.randint(1, 10)

def random_strenght():
    return random.randint(1, 10)


def main():
    coach = Coach("Lasse", 1965, random_voice_level())

    players = []
    for name in ["noah", "william", "liam", "hugo", "lucas", "adam", "oliver", "matteo", "frans", "elias"]:
        born = random.randint(1990, 2000)
        players.append(Player(name, born, random_speed(), random_agility(), random_strenght()))

    team = Team(players, coach)
    print(team.summarize_team())


if __name__ == '__main__':
    main()