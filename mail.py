#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:33:29 2018

@author: alex
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header



class mail(object):
    def __init__(self,maillist,mailtitle,mailcontext):
        self.maillist = maillist
        self.mailtitle = mailtitle
        self.mailcontext = mailcontext
        
        self.mail_host = "smtp.gmail.com"
        self.mail_user = "your email"
        self.mail_pass = "your password"
        self.mail_postfix = "gmail.com"
        
    def sendmail(self):
        
      
        
        try:
            #s = smtplib.SMTP() #create the mail server
            s = smtplib.SMTP_SSL(self.mail_host,465)
            s.ehlo()
            print("begin---connecting")
            #s.connect(self.mail_host,587)
            print("connecting")
            s.login(self.mail_user,self.mail_pass)
            print("connected")
            for key in self.mailcontext:
                #print(key)
                #print(self.mailcontext[key])
                mail = key
                print(type(key))
                print(type(self.mailcontext[key]))
                #print(self.mailcontext[key])
                #msg['To'] = Header(mail, 'utf-8')
                me = "Alex Wang<swoecwang10@gmail.com>"#+self.mail_user #+"<"+ self.mail_user + "@"+self.mail_postfix
                msg = MIMEMultipart()
                msg['Form'] = me
                msg['To'] = mail
                msg['Subject'] = 'your title'
                context = self.mailcontext[key]
                for x in context:
                    #print(x)
                    puretext = MIMEText(x)
            
                
                #puretext = MIMEText(str(context))
                #print(puretext)
                msg.attach(puretext)
                
                # jpg attached
                jpgpart = MIMEApplication(open('/home/alex/ext.jpg', 'rb').read())
                jpgpart.add_header('Content-Disposition', 'attachment', filename='ext.jpg')
                msg.attach(jpgpart)
             
                # xlsx attached
                #xlsxpart = MIMEApplication(open('test.xlsx', 'rb').read())
                #xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
                #msg.attach(xlsxpart)
             
                # mp3 attached
                #mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
                #mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
                #msg.attach(mp3part)
             
                # pdf attached
                #part = MIMEApplication(open('/home/alex/Jian(Alex)wang (5th copy).pdf', 'rb').read())
                #part.add_header('Content-Disposition', 'attachment', filename="Jian(Alex)wang (5th copy).pdf")
                #msg.attach(part)
                #print(mail)
                s.sendmail(me,mail,msg.as_string())
            print("---send---")
            s.close()
            return True
        except Exception,e:
            print str(e)
            return False
        
if __name__=='__main__':
    mailto_list =["swoecwang@yahoo.com"]
    mail_title = 'hey mates'
    mail_content = 'hey this is a test'
    mm = mail(mailto_list,mail_title,mail_content)
    res = mm.sendmail()
    print res
        
        
    