import unittest
from calc3project.src.calc3project.calc import Calc


class MyTestDiv(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_div1(self):
        expect = 6
        actual = Calc(24, 4)
        self.assertEqual(expect, actual.div())  # add assertion here

    def test_div2(self):
        expect = 5
        actual = Calc(25, 5)
        self.assertEqual(expect, actual.div())  # add assertion here


if __name__ == '__main__':
    unittest.main()
