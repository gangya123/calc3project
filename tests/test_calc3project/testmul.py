import unittest
from calc3project.src.calc3project.calc import Calc


class MyTestMul(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mul1(self):
        expect = 25
        actual = Calc(5, 5)
        self.assertEqual(expect, actual.mul())  # add assertion here

    def test_mul2(self):
        expect = 24
        actual = Calc(6, 4)
        self.assertEqual(expect, actual.mul())  # add assertion here


if __name__ == '__main__':
    unittest.main()
