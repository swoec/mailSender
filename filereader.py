#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 12:59:22 2018

@author: alex
"""

import csv

class FileReader:
    plist= []
    def __init__(self):
        with open("/home/alex/Downloads/Connections.csv",'rb') as csvfile:
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
                       sobj = re.search('CTO|director|Director|President|Founder|CEO|princple|chief',roles)
                       if  sobj:
                           self.plist.append(row)
                           #print(row)
                    
                       else:
                           continue
                       
    def display(self):
         for person in self.plist:
             print(person)
    
    def getValue(self):      
        return self.plist;    


   
                
if __name__=='__main__':
     
     t=FileReader();
     t.display();
    