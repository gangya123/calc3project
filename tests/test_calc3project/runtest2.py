import os
import unittest

# 创建了一个测试加载器对象
# 加载了指定包及其后代包中，所有以test开头，.py结尾的文件中测试用例，返回一个测试套件
case_path = os.path.join(os.getcwd(), "D:\\data\\python\\homework\\calc3project\\tests\\test_calc3project")
allcases = unittest.TestLoader().discover(case_path, "test*.py", top_level_dir=None)

# 创建测试运行器
runner = unittest.TextTestRunner(verbosity=2)
runner.run(allcases)
