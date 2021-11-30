import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    text = Column(String)
