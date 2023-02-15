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
    tweet.created_at = datetime.utcnow()
    command_handler.execute("""INSERT INTO TWEETS (uuid,tweet,is_reply,is_deleted,created_at,user_uuid)
                                VALUES (?, ?, ?, ?, ?, ?)""",
                            (tweet.uuid, tweet.text, tweet.is_reply, tweet.is_deleted, tweet.created_at,
                             tweet.user_uuid))
    db.commit()
    if command_handler.rowcount != 1:
        return None
    return tweet


def find_tweet_by_uuid(tweet_uuid):
    db = connect()
    if db is None:
        return None
    if not is_valid_uuid(tweet_uuid):
        return None
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM TWEETS WHERE uuid = :uuid""", {'uuid': tweet_uuid})
    got_tweet = command_handler.fetchone()
    if got_tweet is None:
        return None
    result = Tweet(uuid=got_tweet[0], text=got_tweet[1], is_reply=got_tweet[2],
                   is_deleted=got_tweet[3], created_at=got_tweet[4],
                   user_uuid=got_tweet[5])
    return result


def delete_tweet(tweet_uuid):
    db = connect()
    if db is None:
        return False
    if not is_valid_uuid(tweet_uuid):
        return False
    command_handler = db.cursor()
    command_handler.execute("""UPDATE TWEETS SET is_deleted = TRUE
                            WHERE uuid = :uuid""",
                            {'uuid': tweet_uuid})
    db.commit()
    if command_handler.rowcount != 1:
        return False
    return True


def get_user_tweets(user_uuid):
    db = connect()
    if db is None:
        return []
    if not is_valid_uuid(user_uuid):
        return []
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM TWEETS WHERE
                            user_uuid = :uuid""", {'uuid': user_uuid})
    records = command_handler.fetchall()
    if not records:
        return []
    res = []
    for record in records:
        t = Tweet(uuid=record[0], text=record[1], is_reply=records[2],
                  is_deleted=record[3], created_at=record[4],
                  user_uuid=record[5])
        res.append(t)
    return res
