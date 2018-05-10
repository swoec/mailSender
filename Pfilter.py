#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:20:20 2018

@author: alex
"""

from  filereader import FileReader
import re

class Filter:
    plist = []
    def __init__(self):
        t=FileReader()
        self.reader=t.getValue()
        
    def pfilter(self):
        for row in self.reader:
            email = row['Email Address']
            email= email.strip()
            if email == '':
                continue
            else:
                roles = row['Position']
                sobj = re.search('CTO|director|CEO|princple|chief',roles).span()
                if  sobj:
                    self.plist.append(row)
                    
                else:
                    continue
                
                
        return self.plist
    
    
    
if __name__=='__main__':
     
     t=Filter();
     lists=t.pfilter();
     for items  in lists:
         print(items)
                    
                
                
                
                