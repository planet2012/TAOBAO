import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import allure


class WebKeys:
    def __init__(self, driver):
        self.driver = driver
        # driver.maximize_window()

    # 打开浏览器
    def open(self, url):
        self.driver.get(url)
        sleep(1)

    # 元素定位
    def locator(self, name, value):
        el = self.driver.find_element(name, value)
        self.locator_station(el)
        return el

    # 显示定位的地方，以便确认定位位置
    def locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid blue"
        )

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 输入
    def send_keys(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # z最大化窗口
    def max_window(self):
        self.driver.maximize_window()

    # 清除
    def clear(self, name, value):
        self.locator(name, value).clear()

    # 句柄切换
    def switch_to_handles(self, status_code):
        handles = self.driver.window_handles
        # 切换到原始页面，status_code = 0
        # 切换句柄到第2个页面，status_code = 1，以此类推
        self.driver.switch_to.window(handles[status_code])

    # 关闭当句柄
    def close_window(self):
        self.driver.close()

    # 切换至原句柄页
    def switch_to_defaultFrame(self):
        self.driver.switch_to.default_content()

    # iframe切换
    def switch_to_frame(self, name=None, value=None, frame=None):
        if frame is None:
            self.driver.switch_to.frame(self.locator(name, value))
        else:
            self.driver.switch_to.frame(frame)

    # 鼠标悬停
    def actionchains(self, name, value):
        action = ActionChains(self.driver)
        action.move_to_element(self.locator(name, value)).perform()
        return action
        # return ActionChains(self.driver).move_to_element(self.locator(name,value)).perform()

    # 获取文本
    def get_text(self, name, value):
        return self.locator(name, value).text

    # 文本断言
    def assert_text(self, name, value, expect_text):
        real_text = self.locator(name, value).text
        with allure.step('结果检查：（预期）{} == (实际){}'.format(expect_text, real_text)):
            assert expect_text == real_text

    # 网页title断言
    def assert_title(self, expect_title):
        result = self.driver.title
        with allure.step('结果检查：（预期）{} in (实际){}'.format(expect_title, result)):
            assert expect_title in result

    # 等待
    def time_wait(self, num):
        time.sleep(int(num))

    # 退出
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    wk = WebKeys(driver=webdriver.Chrome())
    wk.open('https://www.baidu.com/')
    wk.time_wait(3)
    wk.quit()
    # driver = webdriver.Chrome()

    # driver.get('https://www.baidu.com/')
    # driver.maximize_window()
    # sleep(3)
    # driver.quit()
