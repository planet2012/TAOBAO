# # //div[text()='查看购物车
#
# import os
# from selenium import webdriver
# from time import sleep
# from Base.base_page import WebKeys
#
# os.popen("d:\work\chrome.bat")
# sleep(2)
#
# options = webdriver.ChromeOptions()
# options.debugger_address = '127.0.0.1:9222'
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
#
# driver.get("https://www.baidu.com/")
# sleep(3)
# check_cart = driver.find_element('xpath',"//span[text()='设置']").text
# # driver.get("https://cart.taobao.com/cart.htm")
# # driver.find_element('css selector', '#fm-login-id').send_keys('13262355765')
# # sleep(2)
# # driver.find_element('css selector', '#fm-login-password').send_keys('cc0128CCH')
# # sleep(2)
# # driver.find_element('css selector', 'button[class$=login]').click()
# # sleep(2)
# # driver.find_element('css selector',"label[for=J_SelectAllCbx1]").click()
# # sleep(2)
# # driver.find_element('css selector',"#J_SmallSubmit").click()
# # sleep(2)
# # check_cart = driver.find_element('xpath',"a[title='修改地址']").text
#
# print(check_cart)
#
#
# sleep(5)
# driver.quit()
