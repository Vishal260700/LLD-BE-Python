from abc import ABC
class Entity(ABC):
    def __init__(self, isWhite, y, x):
        self.__isKilled = False
        self.__isWhite = isWhite
        self.__y = y
        self.__x = x
    
    def kill(self):
        self.__isKilled = True
    
    def getKillStatus(self):
        return self.__isKilled
    
    def isWhite(self):
        return self.__isWhite
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def validate(self, x, y, board):
        if(x >= 0 and x < len(board.grid[0]) and y >= 0 and y < len(board.grid)):
            return True
        return False