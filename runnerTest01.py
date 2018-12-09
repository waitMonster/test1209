# -*- coding:utf-8 -*-
import unittest
from testCase.userTest import userAddTest
from testCase.userTest02 import userAddTest02
import HTMLTestRunner

if __name__ == '__main__':
    #实例化一个TestSuite测试套件--告诉他运行那个用例
    suite=unittest.TestSuite()
    suite.addTest(userAddTest('testUserAdd1'))
    suite.addTest(userAddTest02("testUserAdd2"))

    print(suite)

    file=open('report1/123.html','wb')
    #HTMLTestRunner
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,title="第一个报告")
    runner.run(suite)
