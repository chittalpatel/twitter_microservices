import os
from collections import Counter

import nltk
from kafka import KafkaConsumer
from nltk.corpus import stopwords

from redis_client import RedisClient


class Config:
    TOPICS_NAME = os.getenv("TOPICS_NAME", "tweet-comments-topic,tweets-topic").split(",")
    CONSUMER_GROUP_NAME = os.getenv("CONSUMER_GROUP_NAME", "top-comment-words")
    KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")


class Consumer:
    def __init__(self):
        self._consumer = KafkaConsumer(
            *Config.TOPICS_NAME,
            auto_offset_reset="earliest",
            bootstrap_servers=[f"{Config.KAFKA_HOST}:9092"],
            group_id=Config.CONSUMER_GROUP_NAME,
            key_deserializer=lambda key: int.from_bytes(bytes=key, byteorder='big'),
            value_deserializer=lambda val: val.decode('utf-8'),
            api_version=(0, 10, 2),
        )
        print("Top words consumer connected.")
        self.redis_client = RedisClient()
        print("Redis connected.")
        self.stop_words = set(stopwords.words('english'))

    def consume(
        self,
    ):
        try:
            for msg in self._consumer:
                try:
                    self.cache_top_words(text=msg.value)
                except Exception:
                    print("Skipping top words caching.")
        finally:
            self._consumer.close()

    def cache_top_words(self, text: str):
        words = filter(lambda w: not w in self.stop_words, text.split())
        for word in list(words):
            self.redis_client.add_word(word=word)


if __name__ == "__main__":
    Consumer().consume()

