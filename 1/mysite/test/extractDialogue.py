#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = '周超'

import bs4
from urllib2 import urlopen
def main():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = bs4.BeautifulSoup(html,'lxml')
    nameList = bsObj.findAll("span", {"class":"red"})
    for name in nameList:
        print(name.get_text())
if __name__ == '__main__':
    main()