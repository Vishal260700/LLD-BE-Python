from GameService import GameService
from Ladder import Ladder
from Snake import Snake
from Player import Player

class Simulation:
    
    def __init__(self):
        pass
    
    def startGame(self):
        snakeCount = int(input())
        snakes = []
        while(snakeCount):
            startNend = list(map(int, input().strip().split()))
            start = int(startNend[0])
            end = int(startNend[1])
            snake = Snake(start, end)
            snakes.append(snake)
            snakeCount -= 1
        

        ladderCount = int(input())
        ladders = []
        while(ladderCount):
            startNend = list(map(int, input().strip().split()))
            start = int(startNend[0])
            end = int(startNend[1])
            ladder = Ladder(start, end)
            ladders.append(ladder)
            ladderCount -= 1

        playerCount = int(input())
        players = []
        while(playerCount):
            name = input()
            player = Player(name)
            players.append(player)
            playerCount -= 1
        
        gameService = GameService()
        
        # necessary entities
        gameService.setSnakes(snakes)
        gameService.setLadders(ladders)
        gameService.setPlayers(players)

        # overrride default values
        gameService.setBoardSize(120)
        gameService.allowTillLastPlayer()

        # start game
        gameService.startGame()


game = Simulation()
game.startGame()