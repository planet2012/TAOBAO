'''
淘宝登录页：https://login.taobao.com/member/login.jhtml
page_indexlogin
'''

# 用户名
page_indexlogin_user = ['css selector', '#fm-login-id']
# 密码
page_indexlogin_pwd = ['css selector', '#fm-login-password']
# 登录按钮
page_indexlogin_button = ['css selector', 'button[class$=login]']
#登录前断言
page_indexlogin_agoassert = ['xpath',"//button[text()='登录']"]
#登录后断言
page_indexlogin_assert = ['css selector',"a[class^='site']"]
# 等待时间
page_indexlogin_wait = 2



'''
百度搜索流程 https://www.baidu.com
page_indexbaidu_send_keys
'''
#搜索框输入
page_indexbaidu_send_keys = ['css selector',"input[id='kw']"]

#搜索按钮
page_indexbaidu_button = ['css selector',"input[id='su']"]