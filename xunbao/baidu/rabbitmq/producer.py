#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/14 15:52 
"""
import json
import sys

import time

reload(sys)
sys.setdefaultencoding('utf8')

import pika

username = 'root'   #指定远程rabbitmq的用户名密码
pwd = 'root'
user_pwd = pika.PlainCredentials(username, pwd)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))#创建连接
chan = s_conn.channel()  #在连接上创建一个频道

#chan.queue_declare(queue='baidu_queue') #声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行

tieba = u"单机游戏吧,国产游戏吧,国单销量吧,国产单机吧,游戏吧,新游吧,chinajoy吧,主机吧,Steam吧,PS4吧,WeGame吧,xboxone吧,RPG吧,回合制游戏吧,幻想三国志吧,古剑奇谭吧,轩辕剑吧,金庸群侠传吧" \
        u"侠客风云传吧,御天降魔传吧,凡人修仙传吧,天涯明月刀ol吧,剑网3吧,空之轨迹吧,最终幻想吧,圣女之歌吧,女神异闻录吧,剑灵吧,bilibili吧,二次元吧,橙光游戏吧,cosplay吧,动漫吧" \
        u"漫画吧,国漫吧,acfun吧,秦时明月吧,狐妖小红娘吧,九州吧,全职高手吧,一人之下吧,斗罗大陆吧,少年锦衣卫吧,古风吧,历史吧,中国历史吧,汉服吧,古风曲吧,古风世界吧,剑吧"


data = {u"phone":u"17085687424",u"message":tieba}

data = json.dumps(data,ensure_ascii=False)

print data

chan.basic_publish(exchange='baidu',  #交换机
                   routing_key='queue',#路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
                   body=data)#生产者要发送的消息

print("[生产者] send 'hello world")

#time.sleep(10)

s_conn.close()#当生产者发送完消息后，可选择关闭连接
