#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/7/2
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import tushare as ts
import MySQLdb

def getStack():
    df = ts.get_tick_data('600848', date='2014-12-22')
    conn=MySQLdb.connect(host="localhost",user="root",passwd="zhouchao1850",db="ID",charset="gb2312")
    cursor =conn.cursor()

    #存入数据库
    df.to_sql('tick_data',engine)

if __name__ == '__main__':
    getStack()