#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:15:06 2018

@author: alex
"""


from filereader import FileReader


class Mailsender:
    def __init__(self):
        pro = FileReader()
        self.list = pro.plist
        for i in self.list:
            print(i)