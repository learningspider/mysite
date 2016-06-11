#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'zhouchao'

from urllib2 import urlopen as uu
import re


def retest():
    url=["http://fund.eastmoney.com/000051.html",
         "http://fund.eastmoney.com/213008.html",
         "http://fund.eastmoney.com/000173.html",
         "http://fund.eastmoney.com/000477.html"]

    find_re = re.compile(r'<span class="ui-font-large ui-color-green ui-num">(.+?)</span>',re.DOTALL)
    html_re = re.compile(r'http://fund.eastmoney.com/(.+?).html',re.DOTALL)
    time_re = re.compile(r'<span id="gz_gztime">(.+?)</span>',re.DOTALL)


    for ul in url:
        html=uu(ul).read()

        print "基金代码：" + str(html_re.findall(ul))
        print "单位净值：" + str(find_re.findall(html))
        print "最后更新时间：" + str(time_re.findall(html))
        print ''



if __name__ == '__main__':
    retest()