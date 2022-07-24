'''
淘宝登购物车页：https://cart.taobao.com/cart.htm
page_indexcart
'''

#选择我的购物车
page_indexcart_choice_cart = ['xpath',"//a[text()='我的购物车']"]


#全选按钮
page_indexcart_check_all = ['css selector',"label[for=J_SelectAllCbx1]"]

#结算按钮
page_indexcart_purchase = ['css selector',"#J_SmallSubmit"]

#断言
# page_indexcart_assert = ['xpath',"//div[text()='查看购物车']"]

# 等待时间
page_indexcart_wait = 2
