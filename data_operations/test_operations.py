import unittest

import bcrypt

from user_ops import create_user, find_user_by_uuid, find_user_by_email, delete_user
import models.users as user
from utilities.validate import is_valid_uuid
from utilities.hasher import encrypt
import os


class TestOperations(unittest.TestCase):
    def test_create_user(self):
        case1 = create_user(user.User(name="john_doe", email="test@gmail.com", password="test"))
        self.assertIsNotNone(case1)
        self.assertTrue(is_valid_uuid(case1.uuid))
        self.assertEqual(case1.name, "john_doe")
        self.assertEqual(case1.email, "test@gmail.com")
        self.assertNotEqual(case1.password, "test")
        case2 = create_user(user.User(name="", email="test@gmail.com", password="test"))
        self.assertIsNone(case2)
        case3 = create_user(user.User(name="", email="", password=""))
        self.assertIsNone(case3)
        case4 = create_user(user.User(name="test", email="test@gmail.com", password=""))
        self.assertIsNone(case4)
        os.remove("twitter.db")

    def test_find_user_by_email(self):
        case1 = create_user(user.User(name="john_doe", email="test@gmail.com", password="test"))
        case1 = find_user_by_email("")
        self.assertIsNone(case1)
        case2 = find_user_by_email("@wrong email type")
        self.assertIsNone(case2)
        case3 = find_user_by_email("not_registerd@email.com")
        self.assertIsNone(case3)
        case4 = find_user_by_email("test@gmail.com")
        self.assertIsNotNone(case4)
        self.assertTrue(is_valid_uuid(case4.uuid))
        self.assertEqual(case4.email, "test@gmail.com")
        self.assertEqual(case4.name, "john_doe")
        self.assertTrue(bcrypt.checkpw(bytes("test", 'utf-8'), case4.password))
        os.remove("twitter.db")

    def test_find_user_by_uuid(self):
        # insert user for test
        u = create_user(user.User(name="john_doe", email="john@gmail.com", password="test"))
        # empty uuid
        case1 = find_user_by_uuid("")
        self.assertIsNone(case1)
        # wrong uuid format
        case2 = find_user_by_uuid("35278549-618a-4edc-be2df18804522ab5")
        self.assertIsNone(case2)
        # uuid not in database
        case3 = find_user_by_uuid("35278549-618a-4edc-be2d-f18804522ab5")
        self.assertIsNone(case3)
        case4 = find_user_by_uuid(u.uuid)
        self.assertIsNotNone(case4)
        self.assertEqual(case4.email, "john@gmail.com")
        self.assertEqual(case4.name, "john_doe")
        self.assertTrue(bcrypt.checkpw(bytes("test", 'utf-8'), case4.password))

        os.remove("twitter.db")


if __name__ == '__main__':
    unittest.main()
