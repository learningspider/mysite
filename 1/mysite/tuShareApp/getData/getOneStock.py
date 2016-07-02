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

class Stack():

    #获取股票历史k线
    def get_hist_stack(code_number='',start='',end='',ktype='D'):
        if code_number == '':
            print '请传入股票代码'
            return
        if start == '' or end == '':
            df = ts.get_hist_data(code_number,ktype=ktype)
        else:
            df = ts.get_hist_data(code_number,start,end,ktype=ktype)

        # engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')
        #
        # #存入数据库
        # df.to_sql('hist_day_stack',engine)

if __name__ == '__main__':
    df= ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
    print df
    engine = create_engine('mysql://root:zhouchao1850@127.0.0.1/tushareapp?charset=utf8')

    #存入数据库
    df.to_sql('hist_day_stack',engine)