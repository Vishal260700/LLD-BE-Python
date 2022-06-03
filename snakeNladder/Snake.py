import uuid
class Snake:
    def __init__(self, start, end):
        self.id = str(uuid.uuid4())
        self.start = start
        self.end = end
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getId(self):
        return self.id