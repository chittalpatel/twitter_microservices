import os

from kafka import KafkaProducer


class Config:
    COMMENT_TOPIC_NAME = os.getenv("COMMENT_TOPIC_NAME", "tweet-comments-topic")
    TWEET_TOPIC_NAME = os.getenv("TWEET_TOPIC_NAME", "tweets-topic")
    KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")


class Producer:
    def __init__(self):
        self._producer = KafkaProducer(
            bootstrap_servers=[f"{Config.KAFKA_HOST}:9092"],
            key_serializer=lambda key: key.to_bytes(length=4, byteorder='big'),
            value_serializer=lambda val: bytes(val, encoding='utf-8'),
            api_version=(0, 10, 2),
        )
        print("Producer connected.")

    def produce(self, topic: str, key: int, value: str):
        try:
            self._producer.send(topic=topic, key=key, value=value)
            self._producer.flush()
            return {
                "message": "Comment sent.",
                "success": True,
            }
        except Exception:
            print("Failed to send comment.")
            return {
                "message": "Failed to send comment",
                "success": False,
            }


if __name__ == "__main__":
    producer = Producer()
    producer.produce(topic=Config.COMMENT_TOPIC_NAME, key=3, value="first comment")
