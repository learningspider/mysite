#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
发送txt文本邮件
'''
import smtplib
from email.mime.text import MIMEText
mailto_list=['1161192890@qq.com','18131611146@189.cn']
mail_host="smtp.163.com"  #设置服务器
mail_user="spider19830325@163.com"    #用户名
mail_pass="chao8686"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,u"你好",u"马上发大财！"):
        print "send success!"
    else:
        print "send fail!"