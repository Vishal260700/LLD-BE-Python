import uuid
class User:
    def __init__(self, name):
        self.__name = name
        self.__id = str(uuid.uuid4())
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name