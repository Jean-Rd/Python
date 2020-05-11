# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:53:53 2020

@author: DELL.E5430.SSD
"""

import numpy as np

palette = np.array([[0,0,0],                   #black
                    [255,0,0],                 #red
                    [0,255,0],                  #green
                    [0,0,255],                  #blue
                    [255,255,255]])             #white

image = np.array([[0,1,2,0],
                  [0,3,4,0]]) #cada valor representa un valor de l;a paleta

print(palette[image])  #la imagen en color (2, 4, 3)