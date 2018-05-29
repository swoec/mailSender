#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 00:25:32 2018

@author: alex
"""
import csv
import re


class Filter:
    plist= []
    dir = dict()
    elist = []
    i=0
    lines =[]
    def __init__(self):
        with open("/home/alex/Downloads/Connections.csv",'rb') as csvfile:
            self.reader = csv.DictReader(csvfile)
            f = open("/home/alex/mails.txt",'rb')
            self.lines = f.readlines()
            #for lined in self.lines:
                #print(lined)
                
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
                       sobj = re.search('CTO|director|owner|Director|President|Founder|CEO|princple|chief|software|developer',roles)
                       if  sobj:
                           
                           #self.plist.append(row['Email Address'])                           
                           
                           nmail = row['Email Address']
                           if nmail not in self.lines:
                                   self.plist.append(row)
                                   #print(row['Email Address'])
                                   self.i +=1
                                   print(self.i)
                           else: 
                                   continue
                           #print(row)
                    
                       else:
                           continue
if __name__=='__main__':
     
     t=Filter();
     