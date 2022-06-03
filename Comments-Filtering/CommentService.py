from Comment import Comment
class CommentService:
    def __init__(self):
        self.__comments = {}
    
    def addComment(self, message, userId, parent=None):
        if(parent is not None):
            if(parent not in self.__comments):
                raise Exception("Comment parent not found in system invalid request")
            newComment = Comment(message, userId, self.__comments[parent].getLevel() + 1)
            self.__comments[parent].addRelatedComment(newComment.getId())
            self.__comments[newComment.getId()] = newComment
        else:
            newComment = Comment(message, userId, 0)
            self.__comments[newComment.getId()] = newComment
        return newComment.getId()
    
    def deleteComment(self, commentId):
        # delete main comment
        if(commentId not in self.__comments):
            raise Exception("Comment not found in system invalid request")
        relatedComments = self.__comments[commentId].getRelateComments()
        del self.__comments[commentId]

        # remove references to commentId
        for commId in self.__comments.keys():
            self.__comments[commId].removeRelatedComment(commentId)
        
        # remove all relatedComments (child) of commentId
        for relCommentId in relatedComments:
            self.deleteComment(relCommentId)
    
    def updateComment(self, commentId, requestedOwner, newMessage):
        if(commentId not in self.__comments):
            raise Exception("Comment not found in system invalid request")
        self.__comments[commentId].setMessage(newMessage, requestedOwner)
    
    def likeComment(self, commentId):
        if(commentId not in self.__comments):
            raise Exception("Comment not found in system invalid request")
        self.__comments[commentId].addLike()

    def __printComment(self, commentId, level):
        tab = "    "
        pos = ""
        tabs = 1 + level
        while(tabs):
            pos = pos + tab
            tabs -= 1
        comment = self.__comments[commentId]
        print(pos + "{commentId}: {Owner}: {msg}: {like}".format(commentId=commentId, Owner=comment.getOwner(), msg=comment.getMessage(), like=comment.getLikes()))
    
    def readComments(self, printLevel=-1, children=None):
        if(children is None):
            children = self.__comments.keys()
        for commentId in self.__comments.keys():
            comment = self.__comments[commentId]
            if(comment.getLevel() - printLevel == 1 and comment.getId() in children):
                self.__printComment(commentId, comment.getLevel())
                self.readComments(comment.getLevel(), comment.getRelateComments())

    # depends on requirments for now just level based
    def filterComments(self, level):
        for commentId in self.__comments.keys():
            comment = self.__comments[commentId]
            if(comment.getLevel() - level == 0):
                self.__printComment(commentId, level)
    
    # search comment with query
    def searchComments(self, query):
        for commentId in self.__comments.keys():
            comment = self.__comments[commentId]
            if(comment.searchMsg(query)):
                self.__printComment(commentId, comment.getLevel())

