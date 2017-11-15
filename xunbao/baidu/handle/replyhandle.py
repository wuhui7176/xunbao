#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/14 16:13 
"""
import sys

import time

reload(sys)
sys.setdefaultencoding('utf8')

#驱动，帖子id，回复内容
def reply(driver,rid,content):
    #打开浏览器
    driver.get("http://tieba.baidu.com/p/"+rid)
    #聚焦位置
    driver.find_element_by_id("ueditor_replace").click()
    time.sleep(1)
    #输入文字
    driver.find_element_by_id("ueditor_replace").send_keys(content)
    time.sleep(3)
    #提交输入框
    driver.find_element_by_xpath("//div[@id='tb_rich_poster']/div[3]/div[3]/div/a/span/em").click()









