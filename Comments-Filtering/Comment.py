
import uuid
class Comment:
    def __init__(self, msg, ownerId, level):
        self.__id = str(uuid.uuid4())
        self.__message = msg
        self.__owner = ownerId
        self.__level = level
        self.__likes = 0
        self.__relatedComments = []
    
    def getId(self):
        return self.__id
    
    def getMessage(self):
        return self.__message
    
    # update a message by owner
    def setMessage(self, msg, owner):
        if(owner != self.__owner):
            raise Exception("User not allowed to update message as not owner")
        self.__message = msg

    def getOwner(self):
        return self.__owner
    
    def getLevel(self):
        return self.__level
    
    def getLikes(self):
        return self.__likes
    
    def addLike(self):
        self.__likes += 1
    
    def addRelatedComment(self, commentId):
        if(commentId in self.__relatedComments):
            raise Exception("Comment already associated")
        self.__relatedComments.append(commentId)
    
    def removeRelatedComment(self, commentId):
        if(commentId in self.__relatedComments):
            self.__relatedComments.remove(commentId)
    
    def getRelateComments(self):
        return self.__relatedComments
    
    def searchMsg(self, query):
        if(query in self.__message):
            return True
        return False