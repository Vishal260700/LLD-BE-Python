from DiceService import DiceService
class GameService:
    def __init__(self):
        self.snakes = []
        self.ladders = []
        self.players = []
        self.isGameFinished = False
        self.boardSize = 100 # default value
        self.tillLastPlayer = False # default i.e. whenever first win we end the game
        self.diceCount = 1 # default 1 dice allowed
        self.multipleDiceThrows = False # only one dice throw at a time by player
    
    """
    Game setters
    """
    def setSnakes(self, snakes):
        self.snakes = snakes
    
    def setLadders(self, ladders):
        self.ladders = ladders
    
    def setPlayers(self, players):
        self.players = players
    
    """
    Override Default Values
    """
    def allowMultipleDiceThrows(self):
        self.multipleDiceThrows = True
    
    def allowTillLastPlayer(self):
        self.tillLastPlayer = True
    
    def setDices(self, newDiceCount):
        if(newDiceCount < 1):
            raise Exception("invalid number of dices provided")
        self.diceCount = newDiceCount
    
    def setBoardSize(self, newBoardSize):
        if(newBoardSize < 1):
            raise Exception("invalid board size provided")
        self.boardSize = newBoardSize

    """
    Game Driver helper functions
    """
    def finalPositionAfterSnakeNLadder(self, currentPosition):
        previousPosition = None
        while(previousPosition != currentPosition):
            previousPosition = currentPosition
            for snake in self.snakes:
                snakeStart = snake.getStart()
                snakeEnd = snake.getEnd()
                if(snakeStart == currentPosition):
                    currentPosition = snakeEnd
                    break
            
            for ladder in self.ladders:
                ladderStart = ladder.getStart()
                ladderEnd = ladder.getEnd()
                if(ladderStart == currentPosition):
                    currentPosition = ladderEnd
                    break
        
        return currentPosition
    
    def movePlayer(self, player):
        PlayerPosition = player.getPosition()
        PlayerName = player.getName()

        diceService = DiceService()
        diceRoll = diceService.roll()

        # 6 start the game to 1
        if(PlayerPosition == 0 and diceRoll == 6):
            newPosition = 1
        else:
            newPosition = PlayerPosition + diceRoll

        if(newPosition <= self.boardSize):
            newPosition = self.finalPositionAfterSnakeNLadder(newPosition)
            player.setPosition(newPosition)
        
        print("Player: {name} is at {position} on Board".format(name=PlayerName, position=player.getPosition()))
    
    def hasPlayerWon(self, player):
        if(player.getPosition() == self.boardSize):
            player.setStatus()
            return True
        return False
    
    def isGameCompleted(self):
        activePlayers = 0
        for player in self.players:
            # active players
            if(player.getStatus()):
                activePlayers += 1
                if(self.hasPlayerWon(player) and not self.tillLastPlayer):
                    return True
        if(self.tillLastPlayer and len(self.players) - activePlayers == 1):
            return True
        return False
    
    """
    Game Driver main function
    """
    def startGame(self):
        while(not self.isGameCompleted()):
            for player in self.players:
                self.movePlayer(player)
        print("Game Ended")

