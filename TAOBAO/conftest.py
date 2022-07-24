import os
from time import sleep
import allure
import pytest
from selenium import webdriver

#用例执行前执行一下这个fixture
@pytest.fixture(scope='function')
def browser():

    # 全局定义浏览器驱动，方便下面的hook函数引用driver
    global driver
    os.popen("d:\work\chrome.bat")
    sleep(4)

    #浏览器驱动加载
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)

    #隐式等待
    driver.implicitly_wait(6)

    '''
    # yield之前：用例前置
    # yield之后：用例后置
    '''
    yield driver
    sleep(5)
    #浏览器退出
    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')



"""
    装饰器@pytest.hookimpl(hookwrapper=True)等价于 @pytest.mark.hookwrapper
    作用：
    a:可以获取测试用例的信息，比如用例函数的描述
    b:可以获取测试用例的执行结果，yield，返回一个result对象
"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    #获取测试用例执行结果，yield返回result对象
    out = yield
    """
    从返回一个result对象（out）获取调用结果的测试报告，返回一个report对象
    report对象的属性
    包括when(setup,call,teardown三个值)、nodeid(测试用例的名字)、
    outcome(用例的执行结果：passed,failed)
    """

    report = out.get_result()

    #仅仅获取用例call阶段的执行结果，不包含setup和teardown
    if report.when == 'call':
        #获取用例call执行结果为失败的情况
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            #添加allure报告截图
            with allure.step('添加失败截图:'):
                allure.attach(driver.get_screenshot_as_png(),'失败截图',
                              allure.attachment_type.PNG)

    pass