import allure
import pytest
from Page_object.shopping_cart_page import TaobaoCart
from Test_data import yaml_driver


@allure.feature('淘宝购物车正向结算流程')
class TestCart1():

    @allure.story('购物车结算')
    @allure.title('结算流程')
    @pytest.mark.parametrize('data', yaml_driver.load_yaml('./Test_data/shopping_cart.yaml'))
    def test_login1(self, browser, data):
        global login_count
        lp = TaobaoCart(browser)
        key_name = list(data.keys())[0]
        data1 = data[key_name]
        lp.get_cart(data1['username'], data1['password'])
        lp.time_wait(data1['time_num'])
        lp.cart_check_all()
        lp.time_wait(data1['time_num'])
        lp.time_wait(5)
        lp.cart_assert(*data1['assert_element'], expect_value=data1['assert_value'])
        lp.time_wait(data1['time_num'])
