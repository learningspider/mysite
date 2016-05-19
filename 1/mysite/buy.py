#!/usr/bin/env python
#-*- coding: utf-8 -*-

from splinter import Browser
import datetime
import time


import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

#登录的主页面
'''hosturl = '******' #自己填写
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = '******' #从数据包中分析出，处理post请求的url

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : '******'}
#构造Post数据，他也是从抓大的包里分析得出的。
postData = {'op' : 'dmlogin',
            'f' : 'st',
            'user' : '******', #你的用户名
            'pass' : '******', #你的密码，密码可能是明文传输也可能是密文，如果是密文需要调用相应的加密算法加密
            'rmbr' : 'true',   #特有数据，不同网站可能不同
            'tmp' : '0.7306424454308195'  #特有数据，不同网站可能不同

            }

#需要给Post数据编码
postData = urllib.urlencode(postData)

#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text'''
def buy():
    with Browser('firefox') as browser:
        # Visit URL
        url = "http://xy2.cbg.163.com/"
        browser.visit(url)
        time.sleep(10)
        button = browser.find_by_id('link_105')
        button.click()
        time.sleep(10)
        button = browser.find_by_id('server_18齐云灵脉')
        button.click()

        #点击登陆 需要手动输入用户名 密码 验证码
        time.sleep(30)
        links_found = browser.find_by_tag('a')[9]
        links_found.click()

        #点击进入
        time.sleep(10)
        links_found = browser.find_by_text('进入')
        links_found.click()

        #输入将军登陆界面
        time.sleep(30)
        links_found = browser.find_by_value('确定')
        links_found.click()

        #点击公示期物品
        time.sleep(10)
        links_found = browser.find_by_id('banner_fairshow_a')
        links_found.click()

        #点击召唤兽
        time.sleep(10)
        links_found = browser.find_by_text('召唤兽类')
        links_found.click()

        while True:
            time.sleep(4)
            browser.reload()

        '''if browser.is_text_present('splinter.readthedocs.org'):
            print("Yes, the official website was found!")
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")'''


'''def U(x):
    return unicode(x, 'utf-8')

PRICE = ""

b = Browser('chrome')

def endStep():
    nprice = PRICE
    while nprice == PRICE:
        b.reload()
        nprice = b.find_by_id('needPayPrice').value
        print U("%s-->当前价格%s") % (datetime.datetime.now().strftime("%H:%M:%S.%f"), nprice)
    print "提交定单.."
    b.find_by_id('submit').click()'''

if __name__ == '__main__':
    buy()
    '''print "开始.."
    b.visit('http://passport.jd.com/new/login.aspx?ReturnUrl=http://cart.jd.com/order/orderInfoMain.html')
    print "请先手动在浏览器导航到提交定单的最后一步,输入当前价格,然后按任意键继续!"
    PRICE = raw_input('')
    endStep()
    print "完成.."'''