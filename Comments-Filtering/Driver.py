## we will have comments
## comments DB  - commentId, comment-msg, comment-likes, childComments
## method to show comments in CLI - DONE
## method to upvote a comment - DONE
## method to comment under thread of a comment - DONE
## method to search a comment - DONE
## method to filter comments based on levels of nesting, special charecters in it or not, etc - DONE

## comment class
## comment service

from CommentService import CommentService
from User import User

user1 = User("vishal")
user2 = User("vaibhav")

commentService = CommentService()

msg1 = commentService.addComment("first message", user1.getId())
msg2 = commentService.addComment("second message", user1.getId())
msg3 = commentService.addComment("third message", user2.getId())
msg11 = commentService.addComment("first-first message", user1.getId(), msg1)

commentService.likeComment(msg11)

commentService.addComment("first-second message", user1.getId(), msg1)
commentService.addComment("second-first message", user1.getId(), msg2)
commentService.addComment("first-first-first message", user2.getId(), msg11)

commentService.updateComment(msg1,  user1.getId(), "first-update message") # gives error as different owners

commentService.readComments()
commentService.filterComments(1)
commentService.searchComments("first-second")