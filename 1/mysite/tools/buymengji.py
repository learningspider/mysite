#!/usr/bin/env python
#-*- coding: utf-8 -*-

from splinter import Browser
import datetime
import time,re,sendEmail


import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string


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
def order(browser,level_goumai='/html/body/div[5]/div[4]/div[2]/div/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[7]/input'):
    #获取是否可以购买
    try:
        level_goumai=browser.find_by_xpath(level_goumai)
        print level_goumai.value
        level_goumai.click() #跳转到购买界面

        #点击同意公示期规则按钮
        links_found = browser.find_by_id('agree_fair_show_pay')
        links_found.click()

        #点击预定（加入购物车）
        links_found = browser.find_by_id('buy_btn')
        links_found.click()

        alert = browser.get_alert()
        print alert.text
        alert.accept()
        alert.dismiss()
        to_list=''
        sub = u'已购买成功'
        content = u'已购买'
        sendEmail.send_mail(to_list,sub,content)
        raw_input(u"输入任何内容，回车继续！")

    except:
        print u'\u5df2\u88ab\u81ea\u5df1\u8ba2\u8d2d' #已被自己订购
        time.sleep(30)






def buy():
    with Browser('firefox') as browser:
        # Visit URL
        url = "http://xy2.cbg.163.com/"
        browser.visit(url)
        #time.sleep(10)
        button = browser.find_by_id('link_105')
        button.click()
        #time.sleep(10)
        button = browser.find_by_id('server_18齐云灵脉')
        button.click()

        #点击登陆 需要手动输入用户名 密码 验证码
        #time.sleep(30)
        # raw_input_name = raw_input("username: ")
        # raw_input_password = raw_input("password: ")
        # image_validate = raw_input("image_validate: ")
        # browser.find_by_id('urs').fill(raw_input_name)
        # browser.find_by_id('password').fill(raw_input_password)
        # browser.find_by_id('image_validate').fill(image_validate)
        # links_found = browser.find_by_tag('a')[9]
        # links_found.click()

        #点击进入
        time.sleep(30)
        links_found = browser.find_by_text('进入')
        links_found.click()

        #输入将军登陆界面
        #time.sleep(30)<input class="text" name="otp" id="otp" type="password">
        # jiangjun_validate = raw_input("jiangjun_validate: ")
        # browser.find_by_id('otp').fill(jiangjun_validate)
        # links_found = browser.find_by_value('确定')
        # links_found.click()

        #点击公示期物品
        # time.sleep(10)
        # links_found = browser.find_by_id('banner_fairshow_a')
        # links_found.click()

        #点击召唤兽


        # browser.fill('TPL_username', username.decode('utf8'))

        # links_found = browser.find_by_text('跨服购买')
        # links_found.click()


        while True:
            #循环页面
            try:
                time.sleep(10)
                browser.visit('http://xy2.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search_pet')
                browser.reload()
                browser.find_by_id("js_search_pet_name").first.fill("孟极".decode('utf8'))
                browser.find_by_id("txt_price_max").first.fill("2600".decode('utf8'))
                browser.find_by_text('义之金叶神').click()
                browser.find_by_text('信之土叶神').click()
                browser.find_by_text('分花拂柳').click()
                browser.find_by_text('4年以上可移民服').click()
                browser.find_by_name('skill_logic').last.click()
                browser.find_by_id('btn_equip_search').click()
                time.sleep(10)
            except:
                print u'\u627e\u4e0d\u5230\u9875\u9762' #找不到页面
                time.sleep(10)
                browser.visit('http://xy2.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search_pet')


            #第一行数据
            #获取召唤兽等级
            try:
                mengji = browser.find_by_value('查看详情')

                for i in mengji:
                    print i.value
                    print 'jieshu'
                    time.sleep(1000000)
                    if browser.find_by_text('已出售') or browser.find_by_text('被下单'):
                        print u'已经出售'
                    else:
                        # 点击同意公示期规则按钮
                        links_found = browser.find_by_id('agree_fair_show_pay')
                        links_found.click()

                        # 点击预定（加入购物车）
                        links_found = browser.find_by_id('buy_btn')
                        links_found.click()


                        to_list = ''
                        sub = u'已购买成功'
                        content = u'已购买'
                        sendEmail.send_mail(to_list, sub, content)
                        time.sleep(10)

                print 'done'
            except:
                print u'\u627e\u4e0d\u5230\u53ec\u5524\u517d\u7b49\u7ea7' #找不到召唤兽等级
                time.sleep(30)
                continue




if __name__ == '__main__':
    buy()
    '''print "开始.."
    b.visit('http://passport.jd.com/new/login.aspx?ReturnUrl=http://cart.jd.com/order/orderInfoMain.html')
    print "请先手动在浏览器导航到提交定单的最后一步,输入当前价格,然后按任意键继续!"
    PRICE = raw_input('')
    endStep()
    print "完成.."'''