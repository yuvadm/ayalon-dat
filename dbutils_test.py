import unittest

import dbutils

class DBUtilsTest(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_get_tables(self):
        tables = dbutils.get_tables()
        self.assertTrue(len(tables) >= 1)

if __name__ == '__main__':
    unittest.main()
