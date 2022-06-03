from Game import Game
from Player import Player

game = Game()
player1 = Player("vishal", True)
player2 = Player("vaibhav", False)
game.setPlayer(player1)
game.setPlayer(player2)

Chance = True
while(not game.over()):
    if(Chance):
        print("{player} move".format(player=player1.getName()))
    else:
        print("{player} move".format(player=player2.getName()))

    move = input().split(" ")

    if(move == "exit" or move == "quit"):
        print("Game Forfitted")
        break

    currX = int(move[0])
    currY = int(move[1])
    newX = int(move[2])
    newY = int(move[3])

    entity = game.getBoard().grid[currY][currX]
    if(entity and entity.isWhite() == Chance):
        game.move(currX, currY, newX, newY)
    else:
        raise Exception ("No entity found or entity at pos of current is not the same as player team")
    Chance = not Chance