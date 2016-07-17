#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/7/2
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import tushare as ts
from sqlalchemy import create_engine
import time
import MySQLdb

class Stack():



    def __init__(self):
        pass

    #获取股票历史k线
    def get_hist_stack(self,code_number='',start='',end='',ktype='D'):
        if code_number == '':
            print '请传入股票代码'
            return
        if start == '' or end == '':
            df = ts.get_hist_data(code=code_number,ktype=ktype)
        else:
            df = ts.get_hist_data(code=code_number,start=start,end=end,ktype=ktype)

        engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')
        #存入数据库
        df.to_sql('hist_day_stack',engine,if_exists='append')

    #获取002 300 股票
    def get_002_300(self):
        g002 = ts.get_sme_classified()
        g300 = ts.get_gem_classified()
        engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')
        g002.to_sql('g002',engine,if_exists='append')
        time.sleep(60)
        g300.to_sql('g300',engine,if_exists='append')

    #获取股票基本信息
    def get_basics(self):
        df = ts.get_stock_basics()
        print df
        engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')
        #存入数据库
        df.to_sql('basics',engine,if_exists='append')

    def digui(self,code):
        self.get_hist_stack(code)


    #获取10亿以下股 历史k线
    def get_10_k(self):
        stockcode = []
        error = []
        conn=MySQLdb.connect(host="localhost",user="root",passwd="zhouchao1850",db="tushareapp",charset='utf8')
        cursor =conn.cursor()
        sql ="select code from basics_10"
        n=cursor.execute(sql)

        for i in range(0,n):
            row = cursor.fetchone()
            stockcode.append(row[0])
        print stockcode
        print len(stockcode)
        cursor.close()
        conn.close()

        for code in stockcode:
            try:
                self.get_hist_stack(code)
            except:
                time.sleep(10)
                error.append(code)
            else:
                print 'finish '+code
            time.sleep(10)
        print error




'''
use tushareapp;
create table basics_10 SELECT code FROM tushareapp.basics where totals <= 100000;
[u'002806', u'002341', u'300225', u'300526', u'300525', u'300523', u'300517', u'603663', u'600919']
'''
if __name__ == '__main__':
    s = Stack()
    s.get_10_k()
    #s.get_basics()
    #s.get_002_300()
    #s.get_hist_stack('600848')
