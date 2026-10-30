'''
此模块为对页面元素属性进行封装
'''
class Page_Element():
    '''

    '''
    # 账号输入框
    userAccount=('id','userAccount')
    #密码输入框
    userPwd=('id','loginPwd')
    #登录按钮
    loginBtn=('id','loginBtn')
    # 我的桌面
    myDesktop = ('xpath', '//*[@id="min_title_list"]/li/span')

    # 登录密码错误弹框
    pwdError = ('xpath', '//div[@class="xubox_dialog"]/span[2]')

    # 登录密码错误弹框
    userError = ('xpath', '//div[@class="xubox_dialog"]/span[2]')
