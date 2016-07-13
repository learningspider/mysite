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

    def get_002_300(self):
        g002 = ts.get_sme_classified()
        g300 = ts.get_gem_classified()
        engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')
        g002.to_sql('g002',engine,if_exists='append')
        time.sleep(60)
        g300.to_sql('g300',engine,if_exists='append')



if __name__ == '__main__':
    s = Stack()
    s.get_002_300()
    #s.get_hist_stack('600848')
