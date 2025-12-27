import time

from lib.math_utils import add

class TestMathUtils():
    def test_add(self):
        time.sleep(5)  # Simulating a long-running test
        assert add(3,4) == 7
