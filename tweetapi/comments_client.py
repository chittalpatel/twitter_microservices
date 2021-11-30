import os

import grpc
import comments_pb2_grpc as pb2_grpc
import comments_pb2 as pb2


class CommentClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = self.host = os.getenv("TWEET_COMMENTS_HOST", 'localhost')
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.CommentsStub(self.channel)

    def post_comment(self, tweet_id: int, comment: str):
        comment = pb2.Comment(tweet_id=tweet_id, comment=comment)
        return self.stub.PostComment(comment)

    def get_comments(self, tweet_id: int) -> pb2.GetCommentResponse:
        get_comment_request = pb2.GetCommentRequest(tweet_id=tweet_id)
        return self.stub.GetComments(get_comment_request)


if __name__ == '__main__':
    client = CommentClient()
    result = client.post_comment(tweet_id=1, comment="An exciting new comment")
    # result = client.get_comments(tweet_id=1)
    print(f'{result}')
