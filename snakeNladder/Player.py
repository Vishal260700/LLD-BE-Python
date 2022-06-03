import uuid
class Player:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.position = 0
        self.status = True
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position
    
    def getStatus(self):
        return self.status
    
    def setStatus(self, status=False):
        self.status = status