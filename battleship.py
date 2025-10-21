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
        """Affiche les tirs sur la grille"""
        for (row, col) in hit_positions:
            list_position = [pos for ship in ships for pos in ship.positions]
            if (row, col) in list_position:
                self.grid.at[row, col] = 'O'
                print('TOUCHE')
            else:
                self.grid.at[row, col] = 'X'
                print('MANQUE')

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
        """memorise un tir si la position n'a pas déjà été tirée"""
        format_input = self.format_position(input_fire)
        if format_input in self.hits:
            print('déjà tiré, recommencez')
            return
        else:
            self.hits.append(format_input)
            print(self.hits)

    def verify(self):
        """Vérifie si un navires à coulé. Retourne False si partie fini"""
        for ship in self.ships:
            if all(pos in self.hits for pos in ship.positions):
                print(f'vous avez coulé le bateau {ship.name}')
                self.ships.remove(ship)
        if not self.ships:
                print('partie terminée')
                return False
        return True

    @staticmethod
    def ask_continue():
        response = input("Voulez-vous continuer la partie ? (o/n) : ").lower()
        return response == 'o'

    @staticmethod
    def verify_input(user_input):
        """Vérifie si l'input est au format valide ="""
        if len(user_input) < 2:
            return False

        col = user_input[0].upper()
        if col not in 'ABCDEFGHIJ':
            return False

        row = user_input[1:]
        if not row.isdigit():
            return False

        if int(row) < 1 or int(row) > 10:
            return False

        return True

    def format_position(self, str_pos):
        """Convertit 'A1' en (1, 'A')"""
        col = str_pos[0].upper()
        row = str_pos[1:]
        return (int(row), col)

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
        game.grid.place_hit(game.hits, game.ships)
        game.print_grid()
        where_fire = input('Où voulez vous tirez ? ')
        while not game.verify_input(where_fire):
            where_fire = input('Où voulez vous tirez ? ')
        game.fire_at_position(where_fire)
        continue_game = game.verify()
        if continue_game:
            continue_game = Game.ask_continue()

if __name__ ==  '__main__':
    main()