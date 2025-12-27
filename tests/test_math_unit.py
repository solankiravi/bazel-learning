from lib.math_utils import add, substract, multiply, divide

class TestMathUtils():
    def test_add(self):
        assert add(3,4) == 7

    def test_sub(self):
        assert substract(3,4) == -1

    def test_mul(self):
        assert multiply(3,4) == 12

    def test_divide(self):
        assert divide(3,4) == 0.75
