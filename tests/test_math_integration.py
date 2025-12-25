from lib.math_utils import add, substract, multiply, divide
import unittest
import time

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        time.sleep(2)# Simulating a long-running test
        assert add(3,4) == 7

if __name__ == '__main__':
    unittest.main()
