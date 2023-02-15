import os
import unittest
from user_ops import create_user
from tweets_ops import *
from models.users import User
from models.tweets import Tweet
from utilities.validate import is_valid_uuid


class MyTestCase(unittest.TestCase):
    def test_create_tweet(self):
        # insert user for tests
        u = create_user(User(name="john_doe", email="test@gmail.com", password="test"))
        # no uuid inserted
        case1 = create_tweet(Tweet(user_uuid="", text="test text"))
        self.assertIsNone(case1)
        # no text inserted
        case2 = create_tweet(Tweet(user_uuid=u.uuid, text=""))
        self.assertIsNone(case2)
        case3 = create_tweet(Tweet(user_uuid=u.uuid, text="test tweet text"))
        self.assertIsNotNone(case3)
        self.assertTrue(is_valid_uuid(case3.uuid))
        self.assertIsNotNone(case3.created_at)
        self.assertFalse(case3.is_reply)
        self.assertFalse(case3.is_deleted)
        os.remove("twitter.db")

    def test_find_tweet_by_uuid(self):
        # insert user and tweet for tests
        user = create_user(User(name="john_doe", email="test@gmail.com", password="test"))
        tweet = create_tweet(Tweet(user_uuid=user.uuid, text="test tweet text"))
        # empty uuid
        case1 = find_tweet_by_uuid("")
        self.assertIsNone(case1)
        # wrong uuid format
        case2 = find_tweet_by_uuid("35278549-618a-4edc-be2df18804522ab5")
        self.assertIsNone(case2)
        # uuid not in database
        case3 = find_tweet_by_uuid("35278549-618a-4edc-be2d-f18804522ab5")
        self.assertIsNone(case3)
        case4 = find_tweet_by_uuid(tweet.uuid)
        self.assertIsNotNone(case4)
        self.assertTrue(is_valid_uuid(case4.uuid))
        self.assertIsNotNone(case4.created_at)
        self.assertFalse(case4.is_reply)
        self.assertFalse(case4.is_deleted)

        os.remove("twitter.db")

    def test_find_tweet_by_uuid(self):
        # insert user and tweet for tests
        user = create_user(User(name="john_doe", email="test@gmail.com", password="test"))
        tweet = create_tweet(Tweet(user_uuid=user.uuid, text="test tweet text"))

        case1 = delete_tweet(tweet.uuid)
        self.assertTrue(case1)
        res = find_tweet_by_uuid(tweet.uuid)
        self.assertTrue(res.is_deleted)

        os.remove("twitter.db")


if __name__ == '__main__':
    unittest.main()
