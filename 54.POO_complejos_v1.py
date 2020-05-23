# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:42:18 2020

@author: DELL.E5430.SSD
"""


class COMPLEJO:
    
    def __init__(self,real,imaginario):
        self.r = real
        self.i = imaginario
        
NumCom = COMPLEJO(3,5)
print(NumCom.i)
print(NumCom.r)
