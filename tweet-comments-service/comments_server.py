import grpc
from concurrent import futures

from sqlalchemy.orm import Session

import models
import comments_pb2_grpc as pb2_grpc
import comments_pb2 as pb2
from database import engine, get_db
from models import Comment


class CommentDao:
    def __init__(self):
        self.db: Session = next(get_db())

    def create_comment(self, tweet_id: int, text: str):
        comment = Comment(text=text, tweet_id=tweet_id)
        self.db.add(comment)
        self.db.commit()
        return comment

    def get_comments(self, tweet_id: int):
        return self.db.query(Comment).filter(Comment.tweet_id == tweet_id).all()


class CommentService(pb2_grpc.CommentsServicer):

    def __init__(self, *args, **kwargs):
        models.Base.metadata.create_all(bind=engine)

    def PostComment(self, request, context):
        CommentDao().create_comment(tweet_id=request.tweet_id, text=request.comment)
        result = {'message': "Comment created", 'success': True}
        return pb2.PostCommentResponse(**result)

    def GetComments(self, request, context):
        comments = CommentDao().get_comments(tweet_id=request.tweet_id)
        comments_list = []
        for comment in comments:
            comments_list.append(pb2.Comment(tweet_id=request.tweet_id, comment=comment.text))
        success = False if len(comments_list) == 0 else True
        return pb2.GetCommentResponse(comments=comments_list, success=success)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CommentsServicer_to_server(CommentService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Starting gRPC server.")
    serve()
