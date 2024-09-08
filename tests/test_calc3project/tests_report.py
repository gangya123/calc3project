import os
import unittest
import HTMLTestRunner

# 加载ut包中的所有测试用例
case_path = os.path.join(os.getcwd(), "D:\\data\\python\\homework\\calc3project\\tests\\test_calc3project")
all_cases = unittest.TestLoader().discover(case_path, "test*.py")

# 调用open函数，以写入模式，打开一个准备生成测试报告的网页文件（事先不存在）
filepath = "D:\\data\\python\\homework\\calc3project\\tests\\test_calc3project"
f = open("filepath", "wb")

# 创建HTMLTestRunner运行器对象
runner = HTMLTestRunner.HTMLTestRunner(f, title="测试报告标题", description="测试报告描述")

# 执行测试套中的所有用例，并将测试结果，生成到指定的html文件中
runner.run(all_cases)
