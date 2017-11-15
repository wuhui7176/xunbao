# -- coding: utf-8 --
import urllib2
import json
import sys
reload(sys)

# 获取百度登录验证码模块
sys.setdefaultencoding('utf8')

smsUrl = 'http://xlyqq.xilexuan.com/scriptmanager/cardPoolAction.do?method=getSms&phone=';

def getCode(phone):
    result = urllib2.urlopen(smsUrl+phone).read()
    for data in json.loads(result,encoding="utf-8")['data']:
        message = data['message']
        print message
        if "百度" in message:
            return message[4:10]
    return None


if __name__ =='__main__':
    print 123
    getCode("123")
