"""
    作者:北辰
    日期:17/05/2019
    功能:使用unittest.TestCase来创建测试
"""

import unittest

class MyUnitTests(unittest.TestCase):
    def setUp(self):
        """setUp方法仅在执行测试用例之前被调用"""
        print("In setUp..")

    def tearDown(self):
        """tearDown方法会在测试执行之后被立即调用"""
        print("Tearing Down the test.")
        print("~"*10)

    # 以前缀test的方法会被测试运行器识别为测试用例
    def test_2(self):
        print("in test_2")
        self.assertEqual(1+1,2)

    def test_1(self):
        print("in test_1")
        self.assertTrue(1+1 == 2)

    def test_3(self):
        print("in test_3")
        self.assertEqual(1+1,3)

    # 忽略该测试要使用python修饰符
    @unittest.skip("Skipping test_4")
    def test_4(self):
        print("in test_4")
        self.assertEqual(1+1,3)

    # 期望一些测试用例执行失败
    @unittest.expectedFailure
    def test_5(self):
        print("in test_5")
        self.assertEqual(1+1,3)

    def will_not_be_called(self):
        """默认情况下，这个方法不会被认定为一个测试方法"""
        print("this method will not be called automatically")

if __name__ == '__main__':
    unittest.main() # 加载并运行该测试