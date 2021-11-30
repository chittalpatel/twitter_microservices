import os
from collections import Counter

from redis import Redis
import secrets


class RedisClient:
    def __init__(self):
        self.REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
        self.WORD_COUNT_TTL_SECONDS = os.getenv("WORD_COUNT_TTL_SECONDS", 60)
        self.SECRET = os.getenv("REDIS_STORAGE_SECRET", "secret")
        self.redis = Redis(host=self.REDIS_HOST)

    def add_word(self, word: str):
        _word = f"{self.SECRET}_{word}_{secrets.token_urlsafe(4)}"
        self.redis.set(name=_word, value=1, ex=self.WORD_COUNT_TTL_SECONDS)

    def get_top_n_words(self, n: int = 4):
        counter = Counter()
        for word in self.redis.scan_iter(match=f"{self.SECRET}_*"):
            counter[str(word).split("_")[1]] += 1
        return counter.most_common(n)


if __name__ == "__main__":
    print(RedisClient().get_top_n_words(n=5))
