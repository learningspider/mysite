#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = '周超'

import bs4,re
from urllib2 import urlopen
def main():
    h = []
    dicta = {}
    truename = ''
    cost = ''
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = bs4.BeautifulSoup(html,'lxml')
    nameList = bsObj.findAll(id=re.compile("gift\d"))
    for name in nameList:
        i = 0
        for n in name:
            if (i==0):
                truename = n.get_text().strip()
                print truename,
            elif (i==2):
                cost = n.get_text().strip()
                print cost
                dicta[truename] = cost
                break
            i = i+1
    print '\n'
    print "Dead Parrot's cost is "+ dicta['Dead Parrot']


if __name__ == '__main__':
    main()