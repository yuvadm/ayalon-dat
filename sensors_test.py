import unittest

import sensors

class SensorsTest(unittest.TestCase):

    def test_get_sensors(self):
        sen = sensors.get_sensors()
        self.assertTrue(len(sen) >= 1)

if __name__ == '__main__':
    unittest.main()
