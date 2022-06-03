from Entity import Entity
class Queen(Entity):
    def __init__(self, isWhite, y, x):
        super(Queen, self).__init__(isWhite, y, x)
    
    def move(self, newY, newX, board):
        if(not super(Queen, self).validate(newY, newX, board)):
            raise Exception ("Invalid move")
        else:
            currX = super(Queen, self).getX()
            currY = super(Queen, self).getY()

            # check elephant
            if(newX != currX and newY != currY):
                # check camel way
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
                            if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                                raise Exception ("Invalid move")
                            elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                                # kill found
                                super(Queen, self).setX(tempX)
                                super(Queen, self).setY(tempY)
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
                            if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                                raise Exception ("Invalid move")
                            elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                                # kill found
                                super(Queen, self).setX(tempX)
                                super(Queen, self).setY(tempY)
                                return
                            counter -= 1
                            tempX += 1
                            tempY += 1
            else:
                if(currX > newX):
                    for tempX in range(currX, newX-1, -1):
                        tempEntity = board.grid[newY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                            # kill found
                            super(Queen, self).setX(tempX)
                            return
                else:
                    for tempX in range(currX, newX+1):
                        tempEntity = board.grid[newY][tempX]
                        if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                            # kill found
                            super(Queen, self).setX(tempX)
                            return
                if(currY > newY):
                    for tempY in range(currY, newY-1, -1):
                        tempEntity = board.grid[tempY][newX]
                        if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                            # kill found
                            super(Queen, self).setY(tempY)
                            return
                else:
                    for tempY in range(currY, newY+1):
                        tempEntity = board.grid[tempY][newX]
                        if(tempEntity and tempEntity.isWhite() == super(Queen, self).isWhite()):
                            raise Exception ("Invalid move")
                        elif(tempEntity and tempEntity.isWhite() != super(Queen, self).isWhite()):
                            # kill found
                            super(Queen, self).setY(tempY)
                            return
            raise Exception ("Invalid move")