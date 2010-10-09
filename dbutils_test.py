import unittest

import dbutils

class DBUtilsTest(unittest.TestCase):

    def test_get_tables(self):
        tables = dbutils.get_tables()
        self.assertTrue(len(tables) >= 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DBUtilsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
