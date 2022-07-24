import allure
import pytest
from Page_object.login_page import TaobaoLogin
from Test_data import yaml_driver


@allure.feature('淘宝正向登录流程')
# @pytest.mark.skip()
class TestLogin1():

    @allure.story('正向登录流程')
    @allure.title('正确账号正确密码')
    @pytest.mark.parametrize('data', yaml_driver.load_yaml('./Test_data/login.yaml'))
    def test_login1(self, browser, data):
        global login_count
        lp = TaobaoLogin(browser)
        key_name = list(data.keys())[0]
        data1 = data[key_name]
        lp.login()
        lp.login_input(data1['username'], data1['password'])
        lp.time_wait(data1['time_num'])
        lp.login_assert(*data1['assert_element'], expect_value=data1['assert_value'])
        lp.time_wait(data1['time_num'])
