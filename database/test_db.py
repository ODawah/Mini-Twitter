import unittest
import sql_connector
import os


class TestSqlite3Connector(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(sql_connector.connect())
        os.remove("twitter.db")


if __name__ == '__main__':
    unittest.main()
