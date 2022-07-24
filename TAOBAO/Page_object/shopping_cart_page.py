import allure
from Locate import shopping_cart_element
from VAR.TAOBAO_VAR import *
from Page_object.login_page import TaobaoLogin
from conftest import browser


class TaobaoCart(TaobaoLogin):
    #访问购物车页
    def get_cart(self,username,password):
        with allure.step('流程代码路径：{}'.format(__file__)):
            pass

        with allure.step('进入淘宝购物车页'):
            self.open(TAOBAO_CART_URL)

        with allure.step('先执行登录流程'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            TaobaoLogin.login_input(self,username,password)
            pass
    #切换新页面
    def choice_cart(self):
        with allure.step('流程代码路径：{}'.format(__file__)):
            pass

        with allure.step('选择我的购物车'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            self.click(*shopping_cart_element.page_indexcart_choice_cart)

        with allure.step('切换至新句柄页'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            self.switch_to_handles(1)
            pass
    #选择信息
    def cart_check_all(self):
        with allure.step('流程代码路径：{}'.format(__file__)):
            pass

        with allure.step('全选商品'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            self.click(*shopping_cart_element.page_indexcart_check_all)

        with allure.step('选择结算'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            self.click(*shopping_cart_element.page_indexcart_purchase)

    #购物车断言
    def cart_assert(self,name,value,expect_value):
        with allure.step('代码流程路径：{}'.format(__file__)):
            pass

        with allure.step('断言'):
            self.time_wait(shopping_cart_element.page_indexcart_wait)
            self.assert_text(name,value,expect_text=expect_value)

    pass

if __name__ == '__main__':
    tc = TaobaoCart(browser)
    tc.get_cart('13262355765','cc0128CCH')
    tc.cart_check_all()
    tc.cart_assert('xpath',"//div[text()='查看购物车']",'查看购物车')