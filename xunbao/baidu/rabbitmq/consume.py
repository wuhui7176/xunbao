#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/14 14:43 
"""
import json
import sys

import pika
import logging

from xunbao.baidu.login.baidulogin import accountLogin
from xunbao.baidu.handle.signhandle import *
from selenium import webdriver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("consume")

reload(sys)
sys.setdefaultencoding('utf8')

password = "xunbao123"

# 建立实例
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 声明管道
channel = connection.channel()

def callback(ch, method, properties, body):  # 四个参数为标准格式
    logger.info("consume message %s",body)
    # if 1==1:
    #     ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉生成者，消息处理完成
    #     return
    data = None
    try:
        data = json.loads(body, encoding="utf-8")
    except Exception, e:
        print e

    phone = data['phone']
    message = data['message']
    #driver = webdriver.PhantomJS() linux
    driver = webdriver.Chrome("c:/chromedriver.exe")
    time.sleep(2)
    driver.get("https://tieba.baidu.com")
    time.sleep(2)
    accountLogin(phone,password,driver)
    tiebanames = message.split(",")
    #贴吧名字
    for name in tiebanames:
        #进入贴吧
        enter(driver,name)
        #关注
        attention(driver)
        #签到
        sign(driver)

    ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉生成者，消息处理完成
    try:
        driver.quit()
    except Exception,e:
        driver.close()
        driver.stop_client()
    finally:
        pass
    pass

channel.basic_consume(  # 消费消息
            callback,  # 如果收到消息，就调用callback函数来处理消息
            queue='baidu_queue',  # 你要从那个队列里收消息
            # no_ack=True  # 写的话，如果接收消息，机器宕机消息就丢了
            # 一般不写。宕机则生产者检测到发给其他消费者
            )

channel.start_consuming()  # 开始消费消息


if __name__ == '__main__':
    pass