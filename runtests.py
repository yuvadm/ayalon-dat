import unittest

from dbutils_test import DBUtilsTest
from sensors_test import SensorsTest

def createSuite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(DBUtilsTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SensorsTest))
    return suite

suite = createSuite()
unittest.TextTestRunner(verbosity=2).run(suite)
