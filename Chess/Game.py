from Board import Board
from King import King
from Queen import Queen
from Elephant import Elephant
from Horse import Horse
from Camel import Camel
from Soldier import Soldier
# contains info specific to game
class Game:
    def __init__(self):
        self.__player1 = None
        self.__player2 = None
        self.__board = Board()
    
    def setPlayer(self, player):
        if(self.__player1):
            self.__player2 = player
        else:
            self.__player1 = player
    
    def getPlayer1(self):
        return self.__player1
    
    def getPlayer2(self):
        return self.__player2
    
    def getBoard(self):
        return self.__board
    
    def move(self, currX, currY, newX, newY):
        entity = self.__board.grid[currY][currX]
        if(not entity):
            raise Exception ("Invalid move no entity present at given position to move from")
        else:
            entity.move(newY, newX, self.__board)
            if(currY != entity.getY() or currX != entity.getX()):
                # move confirmed
                self.__board.grid[entity.getY()][entity.getX()] = self.__board.grid[currY][currX]
                self.__board.grid[currY][currX] = None
    
    # TODO - check status of game
    def over(self):
        # check if both kings are present
        grid = self.__board.grid
        count = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if(grid[y][x] and type(grid[y][x]) is King):
                    count += 1
        # Game over
        if(count < 2):
            return True
        
        # Game continues
        return False
        # TODO - Checkmate - another situation of game over
        