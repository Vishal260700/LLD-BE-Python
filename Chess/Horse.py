from Entity import Entity
class Horse(Entity):
    def __init__(self, isWhite, y, x):
        super(Horse, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(Horse, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(Horse, self).getX()
            currY = super(Horse, self).getY()

            if((abs(newX - currX) == 2 and abs(newY - currY) == 1) or (abs(newX - currX) == 1 and abs(newY - currY) == 2)):
                entity = board.grid[newY][newX]
                if(entity and entity.isWhite() == super(Horse, self).isWhite()):
                    raise Exception ("Invalid move")
                else:
                    # kill or move
                    super(Horse, self).setX(newX)
                    super(Horse, self).setY(newY)
                    return
            else:
                raise Exception ("Invalid move")