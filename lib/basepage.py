'''
此模块主要是对seleium中的常用方法进行二次封装
'''
from selenium import webdriver
from time import  *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.pageelement import Page_Element as p
from utils.handle_ini import Handle_Ini
from utils.handle_path import *
class BasePage(): #定义公共方法类
    _driver=None

    @classmethod
    def get_driver(cls):
        if not cls._driver:
            cls._driver=webdriver.Chrome()
            return cls._driver
        return cls._driver
    @classmethod
    def find_element(cls,locator): #元素属性以及对应值，例如:(id,chat-textarea)
        ele_type=locator[0]
        ele_value=locator[1]
        if ele_type == 'id':
            ele = cls._driver.find_element_by_id(ele_value)
        elif ele_type == 'name':
            ele = cls._driver.find_element_by_name(ele_value)
        elif ele_type == 'class':
            ele = cls._driver.find_element_by_class_name(ele_value)
        elif ele_type == 'xpath':
            ele = cls._driver.find_element_by_xpath(ele_value)
        elif ele_type == 'tag':
            ele = cls._driver.find_element_by_tag_name(ele_value)
        elif ele_type == 'link':
            ele = cls._driver.find_element_by_link_text(ele_value)
        elif ele_type == 'p_link':
            ele = cls._driver.find_element_by_partial_link_text(ele_value)
        else:
            raise TypeError('输入的元素属性类型异常')
        return ele
    @classmethod
    def max_window(cls):
        '''
        最大化窗口
        :return:
        '''
        return cls._driver.maximize_window()

    @classmethod
    def get_url(cls,url):
        '''
        访问指定url地址
        :param url:
        :return:
        '''
        return cls._driver.get(url)

    @classmethod
    def sendkeys(cls,elem,value):
        '''
        对标签对象进行输入
        :param elem: 标签对象
        :param value: 输入内容
        :return:
        '''
        return elem.send_keys(value)
    def click(self,elem):
        return elem.click()
    @classmethod
    def WebDriver_Wait(cls,sec,locator,pull_freq=0.5): #显示等待
        '''
        :param sec:超时时间，单位为秒
        ：param Locator:等待的元素属性，类型为元组
        :param pull_freq:刷新时间
        :return:
        '''
        w=WebDriverWait(cls._driver,sec,poll_frequency=pull_freq)
        m=EC.presence_of_all_elements_located(locator)
        ele=w.until(m)
        return ele
    @classmethod
    def wait(cls,sec): #隐式等待
        return cls._driver.implicatly_wait(sec)

    @classmethod
    def window_scroll(cls,elem): #滚动
        return



if __name__ == '__main__':
    driver = BasePage.get_driver()
    i_file=os.path.join(conf_path,'config.ini')
    h=Handle_Ini(i_file)
    url=h.get_value('test_env','url')
    BasePage.get_url(url)
    ele1 = BasePage.find_element(p.userAccount)
    BasePage.sendkeys(ele1,'admin')
    sleep(1)
    ele2 = BasePage.find_element(p.userPwd)
    BasePage.sendkeys(ele2,"123456")
    ele3=BasePage.find_element(p.loginBtn)
    BasePage.click(ele3)
