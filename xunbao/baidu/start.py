#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/14 14:39 
"""
import sys
import threading

import time

import thread
from selenium import webdriver
from login.baidulogin import *
from handle.signhandle import *

reload(sys)
sys.setdefaultencoding('utf8')

tieba1=u"单机游戏吧,国产游戏吧,国单销量吧,国产单机吧,游戏吧,新游吧,chinajoy吧,主机吧,steam吧,PS4吧"
tieba2=u"wegame吧,xboxone吧,rpg吧,回合制游戏吧,幻想三国志吧,古剑奇谭吧,轩辕剑吧,金庸群侠传吧,侠客风云传吧,御天降魔传吧"
tieba3=u"凡人修仙传吧,天涯明月刀ol吧,剑网3吧,空之轨迹吧,最终幻想吧,圣女之歌吧,女神异闻录吧,剑灵吧,bilibili吧,二次元吧"
tieba4=u"橙光游戏吧,cosplay吧,动漫吧,漫画吧,国漫吧,acfun吧,秦时明月吧,狐妖小红娘吧,九州吧,全职高手吧"
tieba5=u"一人之下吧,斗罗大陆吧,少年锦衣卫吧,古风吧,历史吧,中国历史吧,汉服吧,古风曲吧,古风世界吧,剑吧"

phone1="17085100977,17085100993,17085100992,17085100989,17085100872,17085100843,17085100842,17085100841,17085100840"
phone2="17085100839,17085100838,17085100848,17085100849,17085100850,17085100879,17085100881,17085100882,17085100847"
phone3="17085100973,17085100994,17085100984,17085100985,17085100971,17085100866,17085100865,17085100986,17085100983"
phone4="17085100870,17085100995,17085100979,17085100864,17085100869,17085100982,17085100990,17085100911,17085100980"
phone5="17085100975,17085100863,17085100868,17085100873,17085100991,17085100862,17085100867,17085100857,17085100858"
phone6="17085100859,17085100860,17085100856,17080310304,17080310624,17080310614,17080310647,17080310641,17080310649"
phone7="17080310654,17080310674,17080310642,17080310644,17080310664,17080310648,17080310604,17080310643,17080310694"
phone8="17080310847,17080310843,17080310824,17080310849,17080310854,17080310840,17080310848,17080310845,17080310843"
phone9="17080310984,17080310841,17080310814,17080310884,17080310846,17080310864,17080310964,17080310934,17080310947"
phone10="17080310949,17080310914,17080310947,17080310944,17080310994,17080310943,17080310956,17080310945,17080310941"
phone11="17080310942,17080310948,17080310924,17080310974,17080310904,17080311024,17080311184,17080311584,17080311646"
phone12="17080312074,17080312041,17080312094,17080312043,17080312040,17080312194,17080312184,17080312114,17080312174"
phone13="17080312254,17080312214,17080312246,17080312204,17080312264,17080312234,17080312242,17080312243,17080312245"
phone14="17080312247,17080312394,17080312484,17080312453,17080310684,17080310640,17080310645,17080310314,17080310143,17080310042,17085100855"
phone15="17085100987,17085100981,17085100976,17085100974,17085100878,17053954309,17053955003,17053955750,17053957204"
phone16="17164374978,17185509645,17185509684,17185509664,17185509745,17185509747,17085687424,17164374623,17085100967,17085100965,17085100966"
phone17="17085100968,17085100969,17085100963,17085100962,17085100961,17085100959,17085100958,17085100957,17085100913,17085100914"
phone18="17085100915,17085100916,17085100917,17085100918,17085100919,17085100955,17085100956,17085100874,17085100875,17085100876,17085100877"


phone = "17085100977"

tieba = tieba1

#phone = "17085100966";
#phone = "17164374623";
def test(phone):
    print phone

    chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("c:/chromedriver.exe",chrome_options=chrome_options)
    #driver = webdriver.PhantomJS();


    driver.get("https://tieba.baidu.com")

    time.sleep(2)

    driver.delete_all_cookies()


    #cookie 登录失败，切换账号密码登录
    if not cookieLogin(driver,phone):
        accountLogin(phone, "xunbao123", driver)

    putuserlocal(phone,driver)

    tiebanames = tieba.split(",")
    #贴吧名字
    for name in tiebanames:

        print  driver.current_url
        #进入贴吧
        enter(driver,name)
        #关注
        if not attention(driver):
            continue
        #签到
        sign(driver)
    pass
threads = []

for i in phone.split(","):
    thread = threading.Thread(target=test,args=(i,))
    threads.append(thread)

if __name__ == '__main__':
    print threads
    for t in threads:
        #t.setDaemon(True)
        t.start()
