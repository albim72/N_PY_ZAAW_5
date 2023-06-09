#Żabia gra
class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()
        msg = f'Żaba {self} spotyka {obstacle} i {act}!'

class Bug:
    def __str__(self):
        return 'robaka'

    def action(self):
        return 'zjada go'

class FrogWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t--------- Frog World ----------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# Gra Czarnoksiężnika
class Warlock:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'Czarnoksiężnik {self} walczy ze {obstacle} i {act}!'


class Ork:
    def __str__(self):
        return 'złym orkiem'

    def action(self):
        return 'masakruje go'


class WarlockWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t--------- Warlock World ----------'

    def make_character(self):
        return Warlock(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self,factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f"Witaj {name}. Ile masz lat?")
        age = int(age)
    except ValueError as err:
        print(f'Wiek {age} jest błędny, spróbuj jeszcze raz...')
        return (False,age)
    return (True,age)

def main():
    name = input(f"Witaj. Podaj swoje imię: ")
    valid_input = False
    while not valid_input:
        valid_input,age = validate_age(name)
    game = FrogWorld if age<15 else WarlockWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()
