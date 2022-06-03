from Elephant import Elephant
from Horse import Horse
from Camel import Camel
from King import King
from Queen import Queen
from Soldier import Soldier

class Board:
    def __init__(self):
        self.grid = [[None for x in range(0, 8)] for y in range(0, 8)]
        self.setWhites()
        self.setBlacks()
    
    def setWhites(self):
        # soldiers
        for x in range(0, 8):
            self.grid[1][x] = Soldier(True, 1, x)
        
        # Elephant
        self.grid[0][0] = Elephant(True, 0, 0)
        self.grid[0][7] = Elephant(True, 0, 7)

        # Horse
        self.grid[0][1] = Horse(True, 0, 1)
        self.grid[0][6] = Horse(True, 0, 6)

        # Camel
        self.grid[0][2] = Camel(True, 0, 2)
        self.grid[0][5] = Camel(True, 0, 5)

        # King
        self.grid[0][3] = King(True, 0, 3)

        # Queen
        self.grid[0][4] = Queen(True, 0, 4)
        
    def setBlacks(self):
        # soldiers
        for x in range(0, 8):
            self.grid[6][x] = Soldier(True, 6, x)
        
        # Elephant
        self.grid[7][0] = Elephant(True, 7, 0)
        self.grid[7][7] = Elephant(True, 7, 7)

        # Horse
        self.grid[7][1] = Horse(True, 7, 1)
        self.grid[7][6] = Horse(True, 7, 6)

        # Camel
        self.grid[7][2] = Camel(True, 7, 2)
        self.grid[7][5] = Camel(True, 7, 5)

        # King
        self.grid[7][4] = King(True, 7, 4)

        # Queen
        self.grid[7][3] = Queen(True, 7, 3)
    