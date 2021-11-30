from typing import List, Tuple

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Body
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates
from google.protobuf import json_format

import crud
import models
import schemas
from database import SessionLocal, engine
from comments_client import CommentClient
from comments_producer import Producer, Config
from redis_client import RedisClient

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates")
comment_client = CommentClient()
producer = Producer()
redis_client = RedisClient()


@app.get("/tweets/", response_model=List[schemas.Tweet])
def get_tweets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tweets = crud.get_tweets(db, skip=skip, limit=limit)
    return tweets


@app.get("/tweets/{tweet_id}", response_model=schemas.Tweet)
def get_tweet(tweet_id: int, db: Session = Depends(get_db)):
    db_tweet = crud.get_tweet(db, tweet_id=tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet


@app.post("/tweets/", response_model=schemas.Tweet)
def create_tweet(
    tweet: schemas.TweetCreate, db: Session = Depends(get_db)
):
    tweet = crud.create_tweet(db=db, tweet=tweet)
    producer.produce(topic=Config.TWEET_TOPIC_NAME, key=tweet.id, value=tweet.text)
    return tweet


@app.patch("/tweets/{tweet_id}", response_model=schemas.Tweet)
def update_tweet(tweet: schemas.TweetUpdate, db: Session = Depends(get_db)):
    db_tweet = crud.update_tweet(db=db, tweet=tweet)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet does not exist")
    return db_tweet


@app.delete("/tweets/", response_model=schemas.Tweet)
def delete_tweet(tweet_id: int, db: Session = Depends(get_db)):
    db_tweet = crud.delete_tweet(db=db, tweet_id=tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet does not exist")
    return db_tweet


@app.get("/tweets/{tweet_id}/comments")
def get_tweet_comments(tweet_id: int) -> dict:
    comments = comment_client.get_comments(tweet_id=tweet_id)
    return json_format.MessageToDict(comments)


@app.post("/tweets/{tweet_id}/comments")
def create_tweet_comment(tweet_id: int, comment: str = Body(...)) -> dict:
    return producer.produce(topic=Config.COMMENT_TOPIC_NAME, key=tweet_id, value=comment)


@app.get("/trending-words/{n}")
def trending_words(n: int):
    return redis_client.get_top_n_words(n=n)


@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", context={
        'request': request,
        'top_words': redis_client.get_top_n_words(n=3),
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
