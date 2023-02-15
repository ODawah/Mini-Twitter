import uuid
from models.tweets import Tweet
from datetime import datetime
from database.sql_connector import connect
from utilities.validate import is_valid_uuid, is_valid_tweet_text


def create_tweet(tweet):
    db = connect()
    if db is None:
        return None
    if not is_valid_uuid(tweet.user_uuid) or not is_valid_tweet_text(tweet.text):
        return None
    command_handler = db.cursor()
    tweet.uuid = str(uuid.uuid4())
    tweet.created_at = datetime.now()
    command_handler.execute("""INSERT INTO TWEETS (uuid,tweet,is_reply,is_deleted,created_at,user_uuid)
                                VALUES (?, ?, ?, ?, ?, ?)""",
                            (tweet.uuid, tweet.text, tweet.is_reply, tweet.is_deleted, tweet.created_at,
                             tweet.user_uuid))
    db.commit()
    if command_handler.rowcount != 1:
        return None
    return tweet
