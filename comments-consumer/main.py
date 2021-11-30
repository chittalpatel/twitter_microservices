import os

from kafka import KafkaConsumer, BrokerConnection, KafkaClient
from comments_client import CommentClient


class Config:
    TOPIC_NAME = os.getenv("TOPIC_NAME", "tweet-comments-topic")
    CONSUMER_GROUP_NAME = os.getenv("CONSUMER_GROUP_NAME", "save-comments")
    KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")


class Consumer:
    def __init__(self):
        self._consumer = KafkaConsumer(
            Config.TOPIC_NAME,
            auto_offset_reset="earliest",
            bootstrap_servers=[f"{Config.KAFKA_HOST}:9092"],
            group_id=Config.CONSUMER_GROUP_NAME,
            key_deserializer=lambda key: int.from_bytes(bytes=key, byteorder='big'),
            value_deserializer=lambda val: val.decode('utf-8'),
            api_version=(0, 10, 2),
        )
        print("Save comments consumer connected.")
        self.comment_client = CommentClient()

    def consume(
        self,
    ):
        try:
            for msg in self._consumer:
                try:
                    self.comment_client.post_comment(tweet_id=msg.key, comment=msg.value)
                except Exception:
                    print("Skipping save-comments.")
        finally:
            self._consumer.close()


if __name__ == "__main__":
    Consumer().consume()
