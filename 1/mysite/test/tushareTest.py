#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = '周超'

import tushare as ts

def main():
    #ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
    # contents = ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容
    # print contents['title'][0],contents['time'][0]
    # print contents['content'][0]

    df = ts.realtime_boxoffice()
    df.columns = ['实时票房（万）','排名','影片名','票房占比 （%）','上映天数','累计票房（万）','数据获取时间']
    print(df)




if __name__ == '__main__':
    main()