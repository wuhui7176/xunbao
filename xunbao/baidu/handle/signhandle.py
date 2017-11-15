# -- coding: utf-8 --
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from xunbao.baidu.common import *
from xunbao.baidu.login.baidulogin import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("consume")
#关注
def attention(driver):
    # 等待10秒 ，等待蒙层消息
    try:
        if "https://tieba.baidu.com/f" not in driver.current_url and "http://tieba.baidu.com/f" not in driver.current_url  :
            logger.error("当前页面不是正确页面")
            return False
        time.sleep(5)

        #如果已经关注的 退出
        if "https://tieba.baidu.com/f"  in driver.current_url:
            if driver.find_element_by_id("j_head_focus_btn").get_attribute("class") != "focus_btn islike_focus":
                logger.info("贴吧已关注")
                return True
        if "http://tieba.baidu.com/f" in driver.current_url:
            if driver.find_element_by_id("j_head_focus_btn").get_attribute("class") != "focus_btn cancel_focus":
                logger.info("贴吧已关注")
                return True
        # 关注贴吧
        driver.find_element_by_id("j_head_focus_btn").click()

        time.sleep(1)

        # 如果没有关注，出现登录框，重新登录一次
        if is_element_exist_by_id(driver,"TANGRAM__PSP_11__userName"):
            accountLogin2(userlocal.username,"xunbao123",driver)
            driver.find_element_by_id("j_head_focus_btn").click()
        # 取消关注弹窗
        time.sleep(5)

        closeDialog(driver)
    except NoSuchElementException, e:
        logger.error("元素不存在")
    except Exception, e:
        logger.error(type(e))
        print e
    finally:
        return True

#签到
def sign(driver):
    try:
        if driver.find_element_by_xpath("(//a[@onclick='return false'])[2]").get_attribute("title") == "签到完成":
            logger.info("签到完成")
            return
    except Exception ,e:
        return
    # 签到
    time.sleep(10)
    closeDialog(driver)
    # 第一次点击被阻止
    try:
        driver.find_element_by_xpath("(//a[@onclick='return false'])[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath("(//a[@onclick='return false'])[2]").click()

        while is_element_exist_by_class(driver,"uiDialogWrapper"):
            if is_element_exist_by_id(driver,"cancel_focus_no"):
                driver.find_element_by_id("cancel_focus_no").click()
            time.sleep(10)
            logging.info("出现验证码 等待输入中")

    except Exception ,e:
        logger.info(type(e))
        print e
    return

#进入某个贴吧
def enter(driver,name):
    try:
        time.sleep(1)
        driver.find_element_by_id("wd1").clear()
        time.sleep(3)
        driver.find_element_by_id("wd1").send_keys(name)
        driver.find_element_by_link_text(u"进入贴吧").click()
    except Exception, e:
        print e
    return

def closeDialog(driver):
    try:
        if is_element_exist_by_class(driver,"dialogJclose"):
            driver.find_element_by_class_name("dialogJclose").click()
    except Exception ,e:
        print e

if __name__ == '__main__':
    print "https://tieba.baidu.com/f" not  in "http://tieba.baidu.com/f?ie=utf-8&kw=bilibili%E5%90%A7&fr=search&red_tag=k0691733277" and "http://tieba.baidu.com/f" not\
                                                                                                                in "http://tieba.baidu.com/f?ie=utf-8&kw=bilibili%E5%90%A7&fr=search&red_tag=k0691733277"