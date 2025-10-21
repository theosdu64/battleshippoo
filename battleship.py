import pandas as pd  # type: ignore

class Grid:
    def __init__(self):
        self.grid = pd.DataFrame(
            data=[['~' for _ in range(10)] for _ in range(10)],
            columns=['A','B','C','D','E','F','G','H','I','J'],
            index=list(range(1, 11))
        )
    def print_grid(self):
        print(self.grid)

class Ship:
    def __init__(self, positions, name):
        self.positions = positions
        self.name = name

class Game:
    def __init__(self):
        self.grid = Grid()
        self.ships = []

    def print_grid(self):
        self.grid.print_grid()

    def add_ship(self, ship):
        self.ships.append(ship)

def main():
    game = Game()
    game.print_grid()
    aircraft = Ship([(1, 'C'), (2, 'C'), (3, 'C')], 'aircraft')
    cruiser = Ship([(1, 'A'), (2, 'A')], 'cruiser')
    destroyer = Ship([(9, 'E'), (9, 'F')], 'destroyer')
    torpedo = Ship([(1, 'J'), (2, 'J')], 'torpedo')

    war_boat = [aircraft, cruiser, destroyer, torpedo]

    for boats in war_boat:
        game.add_ship(boats)

if __name__ ==  '__main__':
    main()