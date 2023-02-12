import unittest
from ops import create_user
import models.users as user
from utilities.validate import is_valid_uuid
import os


class TestOperations(unittest.TestCase):
    def test_create_user(self):
        result = create_user(user.User(name="test", email="test@gmail.com", password="test"))
        self.assertIsNotNone(result)
        self.assertEqual(is_valid_uuid(result.uuid), True)
        self.assertEqual(result.name, "test")
        self.assertEqual(result.email, "test@gmail.com")
        self.assertNotEqual(result.password, "test")
        result = create_user(user.User(name="", email="test@gmail.com", password="test"))
        self.assertIsNone(result)
        result = create_user(user.User(name="", email="", password=""))
        self.assertIsNone(result)
        result = create_user(user.User(name="test", email="test@gmail.com", password=""))
        self.assertIsNone(result)

        os.remove("twitter.db")


if __name__ == '__main__':
    unittest.main()
