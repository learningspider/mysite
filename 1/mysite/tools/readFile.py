#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'zhouchao'

import MySQLdb


def name():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="zhouchao1850",db="ID",charset="gb2312")
    cursor =conn.cursor()
    fwrite = open(r'd:\1.txt',mode='w+')
    with open(r'd:\1200Wsfz.txt') as f:
        line = f.readline()
        i = 0
        while line:
            #list = line.split(' ')
            try:
                allWords = []
                for word in line:
                    if word[-1]=='\n':
                        allWords.append(word[:-1])  #去掉行末的'\n'
                    else:
                        allWords.append(word)
                names = ''.join(allWords)
                name,ID = names.split('|')
                #name.decode('gb2312')
                sql="insert into emp values(%s,%s)"
                #param应该为tuple或者list
                param=(name,ID)
                #执行,如果成功,n的值为1
                n=cursor.execute(sql,param)
                conn.commit()
                i = i + 1
            except:
                contents = str(i) + ' ' + name + ' '+ ID + '\n'
                fwrite.writelines(contents)
                print i
            line = f.readline()
    cursor.close()
    conn.close()
    fwrite.close()


if __name__ == '__main__':
    name()