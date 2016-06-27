#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = '周超'

import re


def main():
    s = '''<IMG width="200" height="63" src="static/cms/images/logo.png">
    <img src="/static/image/common/grade_v1.png" title="Dataguru优秀学员">
<img src="/static/image/common/grade_v1.png" title="Dataguru优秀学员">   <img src="/static/image/common/grade_v1.png" title="Dataguru优秀学员">
<IMG width="200" height="63" src="static/cms/images/logo.png">'''
    answer1 = re.compile(r'^\w+([\.-]?\w+)*\@\w+(\.\w{2,3}){1,2}$')

    answer2 = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.I)


    answer3 = re.compile(r'<IMG.*src\s*="?(\S+)"?\"',re.I)


    answer4 = re.compile(r'^[0-9]+$')

    word1 = re.findall(answer3,s)
    print word1


if __name__ == '__main__':
    main()