# -*- cod(ing: utf-8 -*-
"""
Created on Fri May  8 20:51:51 2020

@author: DELL.E5430.SSD
"""

import numpy as np

numero = (x for x in range(1,11))
vector = np.array(list(numero))
for i in range(len(vector)):
    if(vector[i] == 5):
        vector[i] = 1
        
print(vector)