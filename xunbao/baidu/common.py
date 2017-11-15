#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/15 15:03 
"""
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf8')

userlocal = threading.local()

def putuserlocal(username,driver):
    userlocal.username = username
    userlocal.driver = driver

def getuserlocal():
    return userlocal.username,userlocal.driver

#存在返回true
def is_element_exist_by_id(driver,id):
    try:
        driver.find_element_by_id(id)
        return True
    except Exception ,e:
        return False


def is_element_exist_by_class(driver,clas):
    try:
        driver.find_element_by_class_name(clas)
        return True
    except Exception,e:
        return False