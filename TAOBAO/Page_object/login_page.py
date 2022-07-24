from Base.base_page import WebKeys
import allure
from Locate import login_element
from VAR.TAOBAO_VAR import *
import pytest
from selenium import webdriver


class TaobaoLogin(WebKeys):
    #访问登录页
    def login(self):
        with allure.step('流程代码路径：{}'.format(__file__)):
            pass

        with allure.step('打开网页'):
            self.open(TAOBAO_LOGIN_URL)
    #执行登录操作
    def login_input(self, username, password):
        with allure.step('流程代码路径'):
            pass

        with allure.step('输入账号'):
            self.send_keys(*login_element.page_indexlogin_user, txt=username)
            self.time_wait(login_element.page_indexlogin_wait)
            pass

        with allure.step('输入密码'):
            self.send_keys(*login_element.page_indexlogin_pwd, txt=password)
            self.time_wait(login_element.page_indexlogin_wait)
            pass

        with allure.step('点击登录'):
            self.click(*login_element.page_indexlogin_button)
            self.time_wait(login_element.page_indexlogin_wait)
            pass

    #断言
    def login_assert(self, name, value, expect_value):
        with allure.step('流程代码路径：{}'.format(__file__)):
            pass

        with allure.step('断言'):
            self.time_wait(login_element.page_indexlogin_wait)
            self.assert_text(name, value, expect_value)

    pass


if __name__ == '__main__':
    tl = TaobaoLogin(driver=webdriver.Chrome())
    tl.login()
    tl.time_wait(2)
    print(tl.get_text('xpath', "//span[text()='设置']"))

    # tl.login_input('iphone14')
    tl.time_wait(3)
    tl.quit()
