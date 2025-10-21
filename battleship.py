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

    def place_hit(self, hit_positions, ships):
        for (row, col) in hit_positions:
            list_position = [pos for ship in ships for pos in ship.positions]
            if (row, col) in list_position:
                self.grid.at[row, col] = 'O'
            else:
                self.grid.at[row, col] = 'X'

class Ship:
    def __init__(self, positions, name):
        self.positions = positions
        self.name = name

class Game:
    def __init__(self):
        self.grid = Grid()
        self.ships = []
        self.hits = []

    def print_grid(self):
        self.grid.print_grid()

    def add_ship(self, ship):
        self.ships.append(ship)

    def fire_at_position(self, fire_position):
        self.is_hit(fire_position)

    def is_hit(self, input_fire):
        format_input = self.format_position(input_fire)
        if format_input in self.hit:
            print('déjà tiré, recommencez')
            return
        else:
            self.hit.append(format_input)
            print(self.hit)

def main():
    game = Game()
    aircraft = Ship([(1, 'C'), (2, 'C'), (3, 'C')], 'aircraft')
    cruiser = Ship([(1, 'A'), (2, 'A')], 'cruiser')
    destroyer = Ship([(9, 'E'), (9, 'F')], 'destroyer')
    torpedo = Ship([(1, 'J'), (2, 'J')], 'torpedo')

    war_boat = [aircraft, cruiser, destroyer, torpedo]

    for boats in war_boat:
        game.add_ship(boats)

    continue_game = True
    while continue_game:
        game.grid.place
        game.print_grid()
        where_fire = input('Où voulez vous tirez ?')
        game.fire_at_position(where_fire)
if __name__ ==  '__main__':
    main()