from Entity import Entity
class Camel(Entity):
    def __init__(self, isWhite, y, x):
        super(Camel, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(Camel, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(Camel, self).getX()
            currY = super(Camel, self).getY()
            xQuoteint = max(currX, newX)//min(currX, newX)
            xReminder = max(currX, newX)%min(currX, newX)
            yQuoteint = max(currY, newY)//min(currY, newY)
            yReminder = max(currY, newY)%min(currY, newY)
            if(xQuoteint != yQuoteint or xReminder != 0 or yReminder != 0):
                raise Exception ("Invalid move")
            else:
                if(currX > newX): # means currY > newY
                    counter = currX - newX
                    tempX = currX
                    tempY = currY
                    while(counter):
                        tempEntity = board.grid[tempY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Camel, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Camel, self).isWhite()):
                            # kill found
                            super(Camel, self).setX(tempX)
                            super(Camel, self).setY(tempY)
                            return
                        counter -= 1
                        tempX -= 1
                        tempY -= 1
                else:
                    counter = newX - currX
                    tempX = currX
                    tempY = currY
                    while(counter):
                        tempEntity = board.grid[tempY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Camel, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Camel, self).isWhite()):
                            # kill found
                            super(Camel, self).setX(tempX)
                            super(Camel, self).setY(tempY)
                            return
                        counter -= 1
                        tempX += 1
                        tempY += 1
        super(Camel, self).setX(newX)
        super(Camel, self).setY(newY)