# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:51:01 2020

@author: DELL.E5430.SSD
"""
from numpy import pi

class CIRCLE:
    def __init__(self,radio):
        self.r = radio
        self.A = radio**2*pi
        self.P = radio*pi
    #si queremos cambiar el radio
    def set_r(self,newradio):
        self.rw = newradio
        self.Ar = newradio**2*pi
        self.Pe = newradio*pi
        
    
a = CIRCLE(5)

print(a.r)
print(a.A)
print(a.P)
#camvioamos el valor de radio
a.set_r(10)
print(a.rw)
print(a.Ar)
print(a.Pe)