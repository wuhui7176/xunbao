#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/14 14:37 
"""
from xunbao.baidu.db.mongodb.user import *
import logging
import sys
import time
from xunbao.baidu.common import *
from xunbao.baidu.login.smscode import getCode
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("consume")
reload(sys)
sys.setdefaultencoding('utf8')

# 短信登录
def smsLogin(phone,driver):
    time.sleep(5)
    driver.find_element_by_link_text(u"登录").click()
    time.sleep(8)
    #切换
    driver.find_element_by_id("TANGRAM__PSP_10__smsSwitch").click()
    #发送验证码
    driver.find_element_by_id("TANGRAM__PSP_10__smsPhone").send_keys(phone)
    #发送验证码
    driver.find_element_by_id("TANGRAM__PSP_10__smsTimer").click()
    #或得验证码
    time.sleep(10)
    code = None
    while code==None:
        code = getCode(phone)
    driver.find_element_by_id("TANGRAM__PSP_10__smsVerifyCode").send_keys(code)
    driver.find_element_by_id("TANGRAM__PSP_10__smsSubmit").click()
    #登录完成后保存 cookie
    cookie = driver.get_cookies()

#账号密码登录
def accountLogin(username,password,driver):
    try:
        time.sleep(5)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(8)

        # while is_element_exist(driver,'TANGRAM__PSP_10__userName') ==False :
        #     continue
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(username)
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys(password)

        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        time.sleep(3)

        while is_element_exist_by_id(driver,"TANGRAM__PSP_10__verifyCode"):
            logging.info("弹出验证码 手机号 %s ",username)
            time.sleep(10)
            while driver.isElementExitById(driver,"TANGRAM__PSP_10__error"):
                time.sleep(10)
                logging.info("密码错误 手机号 %s 密码 %s", username,password)

        #
        logger.info("登录成功")
        cookie = driver.get_cookies()
        user ={"username":username,"cookie":cookie}
        insertUser(user)
        driver.refresh()

    except Exception, e:
        print type(e)
        print e



def accountLogin2(username,password,driver):
    try:
        # while is_element_exist(driver,'TANGRAM__PSP_10__userName') ==False :
        #     continue
        driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys(username)
        driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys(password)

        driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        time.sleep(3)

        while is_element_exist_by_id(driver,"TANGRAM__PSP_11__verifyCode"):
            logging.info("弹出验证码 手机号 %s ",username)
            time.sleep(10)
            while driver.isElementExitById(driver,"TANGRAM__PSP_11__error"):
                time.sleep(10)
                logging.info("密码错误 手机号 %s 密码 %s", username,password)

        #
        logger.info("登录成功")
        cookie = driver.get_cookies()
        user ={"username":username,"cookie":cookie}
        insertUser(user)
        driver.refresh()

    except Exception, e:
        print type(e)
        print e


def cookieLogin(driver,phone):

    cookie = findCookieByPhone(phone)

    if cookie ==None:
        return False

    #  COOKIE 只要 name 和value  其他的去除
    cs = {}
    for i in cookie:
        cs.clear()
        cs.fromkeys(u'name')
        cs.fromkeys(u'value')
        cs.fromkeys(u'path')
        cs.fromkeys(u'domain')
        cs.setdefault(u'name', i.get(u'name'))
        cs.setdefault(u'value', i.get(u'value'))
        cs.setdefault(u'path', i.get(u'path'))
        #cs.setdefault(u'domain', i.get(u'domain'))
        # ******************************phatomjs 需要这样设置 ******************************
        cs.setdefault(u'domain',".tieba.baidu.com")
        driver.add_cookie(cs)

    # 刷新当前页面，保持登录状态
    driver.refresh()

    time.sleep(1)

    if is_element_exist_by_class(driver,"u_username_title"):
        return True
    return False





def is_element_exist(driver,css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print "元素未找到:%s"%css
        return False
    elif len(s) == 1:
        return True
    else:
        print "找到%s个元素：%s"%(len(s),css)
        return False





#退出
def logOut(driver):
    driver.find_element_by_link_text(u"退出").click()
    driver.find_element_by_xpath("(//div[@id='dialogJbody']/div)[2]").click()


if __name__ == '__main__':
    pass