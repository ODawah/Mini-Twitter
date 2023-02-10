import unittest
import ops
import models.users as user
from utilities.validate import validate_uuid
import os


class TestUserOperations(unittest.TestCase):
    def test_create_user(self):
        result = ops.create_user(user.User(uuid="", name="test", email="test@gmail.com", password="test"))
        self.assertIsNotNone(result)
        self.assertEqual(validate_uuid(result.uuid), True)
        self.assertEqual(result.name, "test")
        self.assertEqual(result.email, "test@gmail.com")
        self.assertNotEqual(result.password, "test")
        os.remove("twitter.db")


if __name__ == '__main__':
    unittest.main()
