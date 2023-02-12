import unittest
import hasher


class TestHasher(unittest.TestCase):
    def test_password_hasher(self):
        self.assertNotEqual(hasher.encrypt("test_pass"), "test_pass")
        self.assertEqual(hasher.encrypt(""), "")


if __name__ == '__main__':
    unittest.main()
