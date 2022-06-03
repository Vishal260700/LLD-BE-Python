from Entity import Entity
class Elephant(Entity):
    def __init__(self, isWhite, y, x):
        super(Elephant, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(Elephant, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(Elephant, self).getX()
            currY = super(Elephant, self).getY()
            if(newX != currX and newY != currY):
                raise Exception ("Invalid move")
            else:
                if(currX > newX):
                    for tempX in range(currX, newX-1, -1):
                        tempEntity = board.grid[newY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Elephant, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Elephant, self).isWhite()):
                            # kill found
                            super(Elephant, self).setX(tempX)
                            return
                else:
                    for tempX in range(currX, newX+1):
                        tempEntity = board.grid[newY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Elephant, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Elephant, self).isWhite()):
                            # kill found
                            super(Elephant, self).setX(tempX)
                            return
                
                if(currY > newY):
                    for tempY in range(currY, newY-1, -1):
                        tempEntity = board.grid[tempY][newX]
                        if(tempEntity and tempEntity.isWhite() == super(Elephant, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Elephant, self).isWhite()):
                            # kill found
                            super(Elephant, self).setY(tempY)
                            return
                else:
                    for tempY in range(currY, newY+1):
                        tempEntity = board.grid[tempY][newX]
                        if(tempEntity and tempEntity.isWhite() == super(Elephant, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Elephant, self).isWhite()):
                            # kill found
                            super(Elephant, self).setY(tempY)
                            return
        super(Elephant, self).setX(newX)
        super(Elephant, self).setY(newY)
        
                
