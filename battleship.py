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

def main():
    grid = Grid()
    grid.print_grid()

if __name__ ==  '__main__':
    main()