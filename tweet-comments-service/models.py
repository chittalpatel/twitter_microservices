import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    text = Column(String)
    tweet_id = Column(Integer)
