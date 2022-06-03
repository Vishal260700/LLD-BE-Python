from Entity import Entity
class King(Entity):
    def __init__(self, isWhite, y, x):
        super(King, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(King, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(King, self).getX()
            currY = super(King, self).getY()

            if(not (max(currX, newX) - min(currX, newX) <= 1 and max(currY, newY) - min(currY, newY) <= 1)):
                raise Exception ("Invalid move out of range of entity power to move")
            else:
                tempEntity = board.grid[newY][newX]
                if(tempEntity and tempEntity.isWhite() == super(King, self).isWhite()):
                    raise Exception ("Invalid move")
                super(King, self).setX(newX)
                super(King, self).setY(newY)