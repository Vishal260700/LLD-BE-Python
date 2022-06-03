from Entity import Entity
class Soldier(Entity):
    def __init__(self, isWhite, y, x):
        super(Soldier, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(Soldier, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(Soldier, self).getX()
            currY = super(Soldier, self).getY()

            if(abs(newX - currX) == 1 and newY - currY == 1):
                # move correct for kill
                entity = board.grid[newY][newX]
                if(entity and entity.isWhite() == super(Soldier, self).isWhite()):
                    raise Exception ("Invalid move")
                else:
                    # kill or move
                    super(Soldier, self).setX(newX)
                    super(Soldier, self).setY(newY)
                    return
            elif(newX - currX == 0 and newY - currY == 1):
                # move forward - check if present anything else ok
                entity = board.grid[newY][newX]
                if(entity):
                    raise Exception ("Invalid move")
                else:
                    super(Soldier, self).setX(newX)
                    super(Soldier, self).setY(newY)
                    return
            else:
                raise Exception ("Invalid move")