#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/11/15 14:48 
"""
import sys
import pymongo
from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding('utf8')

"""
@version: v1.0 
@author: wuhui
@time: 2017/11/13 19:52 
"""


client = MongoClient('127.0.0.1', 27017)

db=client.xunbao

def insertUser(user):
    collection = db.user
    u= collection.find_one({"username": user})
    if u ==None:
        collection.insert(user)
    else:
        collection.update(user)
    return


def findCookieByPhone(phone):
    collection = db.user
    user= collection.find_one({"username":phone})
    if user == None:
        return None

    return user['cookie']



if __name__ == '__main__':
    print  findCookieByPhone("17080312204")




