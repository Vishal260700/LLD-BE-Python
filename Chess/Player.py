class Player:

    def __init__(self, name, white):
        self.__name = name
        self.__white = white # true mean white else black
    
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__white