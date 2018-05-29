#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 12:59:22 2018

@author: alex
"""

import csv
import re
from mail import mail



class FileReader:
    plist= []
    dir = dict()
    elist = []
    contextlist=[]
    def __init__(self):
        with open("/home/alex/Downloads/Connections (copy).csv",'rb') as csvfile:
            self.reader = csv.DictReader(csvfile)
            
            for row in self.reader:
                #print(row['First Name'])
                email = row['Email Address']
                email= email.strip()
                if email == '':
                   continue
                else:
                   roles = row['Position']
                   if roles == '':
                       continue
                   else:
                       sobj = re.search('CTO|director|Director|President|Founder|CEO|princple|chief|software|developer',roles)
                       if  sobj:
                           self.plist.append(row)
                           #self.plist.append(row['Email Address'])                           
                           print(row['Email Address'])
                           #print(row)
                    
                       else:
                           continue
                       
    def display(self):
         for person in self.plist:
             #print(person)
             idx = person['Email Address']
             name = person['First Name']
             self.elist.append(idx)
             print(name)
             context ="""Hi,"""+name+""":
                I am a motivated ICT professional who has ever worked for over ten years, with the expertise of java&python development, both front-end, and back-end, 
                software testing(TDD-junit , cucumber, BDD- selenium), continuous integration and delivery.
                
                As a system designer: according to the diverse demands, choose suitable technologies, and set up system framework, then design the architectures, 
                including database, application frameworks, prototype
                As a system developer and tester: familiar with SDLC, develop safe and effective code in financial, mechanical systems, such as CRM system for Nepal telecom, 
                IPTV for Italy media, refactor project structures. 
                And use Junit,cucumber&selenium to validate functions
                As a system maintainer&optimizator: set up developing&delivery environment,manage& parameterize&optimize delivery system
                I am also an active communicator with excellent teamwork and analytical skills used to get the effect in succeeding in a high-pressure situation
                
                technical skill sets
                Front-end: HTML5,CSS3,Bootstrap,JavaScript,Ajax,JQuery,Backbone,AngularJS,XML,JSON,Restful API
                Back-end: Spring, SpringMVC,hibernate,Mybatis,JDBC,Struts,Shiro,WSDL,web interfaces,Swing
                Database: Oracle, Mysql,MongoDB,SQLite,SQL server
                MQ&distributing system:MQTT,Kafka,HBase,Hadoop
                Search engine: Lucene, ElasticSearch, such as splitting words and optimization of the index building
                Python: spiders, machine learning, Django
                Test skills:write test cases,find bugs,PDM,TDD,JUnit,CUCUMBER,and BDD,Selenium
                Servers:Tomcat,JBoss,Weblogic,IIS,NodeJS,Redis,Nginx,FTP,Image,Apache,Maven,docker,kubernate
                Design; power design, Axure RP, UML, Dia
                Control:SVN,Git,Jira,Ant,Maven,Jenkins
                Methodology: Agile-Scrum, Waterfall
                System: Linux, Linux kernel, windows, a deep research in Linux kernel
                IDE:Eclipse,plugins,IDEA,Anaconda
                Android:3Y+ experiences  
                
                More details can be found in my LinkedIn:https://www.linkedin.com/in/alex-wang-63237b39/. 
                My Github is https://github.com/swoec, you can find some of my works there.
                Currently, I am seeking a job in New Zealand .
                I write this letter to you because you may be able to offer me a job opportunity.
                If you have, please contact me.
                 
                If you do not want to help me or this letter disturb you, please ignore it.
                My email: swoecwang10@gmail.com
                Looking forward to your reply.
                Best Regards
                Alex
                                                                          
             """
             #context = context.encode('utf-8')
             context =context.decode('utf-8').strip()
             self.dir[idx] = {context}
             self.contextlist.append(context)
             #print(person['First Name'])
             #print(person['Email Address'])
             title = name +" "+person['Last Name']
             #print(title)
         mails= mail(self.elist,title,self.dir)
         mails.sendmail()
    
    def getValue(self):      
        return self.plist;    
   
                
if __name__=='__main__':
     
     t=FileReader();
     t.display();
    