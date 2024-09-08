import unittest

from calc3project.src.calc3project.calc import Calc


class TestExecuteSort(unittest.TestCase):

    def test_div1(self):
        expect = 6
        actual = Calc(24, 4)
        self.assertEqual(expect, actual.div())  # add assertion here

    def test_div2(self):
        expect = 5
        actual = Calc(25, 5)
        self.assertEqual(expect, actual.div())  # add assertion here


if __name__ == '__main__':
    # 创建一个测试套件对象（测试用例的集合）
    allcases = unittest.TestSuite()
    # 调用测试套件对象，添加“测试用例对象”的方法
    allcases.addTest(TestExecuteSort("test_div1"))
    allcases.addTest(TestExecuteSort("test_div2"))

    # 创建一个文本测试运行器对象
    runner = TestExecuteSort()
    # 调用运行器的run方法，传入一个测试套件对象，就会执行这个测试 套件中的所有测试用例
    runner.run(allcases)

