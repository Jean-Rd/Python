# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:32:35 2020

@author: DELL.E5430.SSD
"""


class VECTOR:
    magnitud = 2
    
    def NewMag(self,magnitudnew):
        self.magnitud = magnitudnew
        
        
v1 = VECTOR()
v2 = VECTOR()
print(v1.magnitud,v2.magnitud)

v2.NewMag(4)
print(v2.magnitud)