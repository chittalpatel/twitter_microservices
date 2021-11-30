import datetime

from sqlalchemy.orm import Session

import models
import schemas


def get_tweets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tweet).offset(skip).limit(limit).all()


def get_tweet(db: Session, tweet_id: int):
    return db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()


def create_tweet(db: Session, tweet: schemas.TweetCreate):
    db_tweet = models.Tweet(**tweet.dict())
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def update_tweet(db: Session, tweet: schemas.TweetUpdate):
    db_tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet.id).first()
    if db_tweet:
        db_tweet.text = tweet.text
        db_tweet.created_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(db_tweet)
        return db_tweet


def delete_tweet(db: Session, tweet_id: int):
    db_tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if db_tweet:
        db.delete(db_tweet)
        db.commit()
        return db_tweet
