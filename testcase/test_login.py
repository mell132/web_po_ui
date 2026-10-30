# coding:utf-8

"""
此模块主要是对登录功能测试的用例类
"""

import unittest
from ddt import ddt,data
from time import *
from utils.handle_ini import Handle_Ini
from utils.hand_exl import Handle_Excel
from utils.handle_path import *
from lib.basepage import BasePage
from lib.pageelement import Page_Element as p

i_file = os.path.join(conf_path,'config.ini')
h_ini = Handle_Ini(i_file)
url = h_ini.get_value('test_env','url')   # 获取登录页的url地址

e_file = os.path.join(data_path,'case_data.xlsx')
h_exl = Handle_Excel(e_file,'login')   # 获取登录功能的所有数据
cases = h_exl.read_data()

@ddt
class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BasePage.get_driver()
        BasePage.max_window()
        sleep(2)

    def setUp(self) -> None:
        BasePage.get_url(url)
        BasePage.wait(3)

    def tearDown(self) -> None:
        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        BasePage.quit_driver()

    @data(*cases)
    def test_1_login(self,case):
        """
        登录的用例方法
        :return:
        """
        ele1 = BasePage.find_element(p.userAccount)
        BasePage.sendkeys(ele1,case['username'])
        ele2 = BasePage.find_element(p.userPwd)
        BasePage.sendkeys(ele2,case['password'])
        sleep(1)
        ele3 = BasePage.find_element(p.loginBtn)
        BasePage.click(ele3)
        # 断言
        case_type = case['case_type']
        if case_type == 'success':
            ele4 = BasePage.webdriver_wait(3,p.myDesktop,0.2)
            t = BasePage.get_text(ele4)
            self.assertEqual(t,'我的桌面')
        elif case_type == 'pwd_error':
            ele4 = BasePage.webdriver_wait(3,p.pwdError,0.1)
            t = BasePage.get_text(ele4)
            self.assertEqual(t,'登录密码不正确！')
        elif case_type == 'user_error':
            ele4 = BasePage.webdriver_wait(3,p.userError,0.1)
            t = BasePage.get_text(ele4)
            self.assertEqual(t,'登录帐号不存在！')


if __name__ == '__main__':
    unittest.main()

