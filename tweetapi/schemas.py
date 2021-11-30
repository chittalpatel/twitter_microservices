from datetime import datetime

from pydantic import BaseModel


class TweetBase(BaseModel):
    text: str


class TweetCreate(TweetBase):
    pass


class TweetUpdate(TweetBase):
    id: int


class Tweet(TweetUpdate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
