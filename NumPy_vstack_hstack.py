# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:44:27 2020

@author: DELL.E5430.SSD
"""


import numpy as np
b = np.arange(12).reshape(3,4)
a = np.floor(b) #floor devuelve matriz sin comillas mas bonito


x = np.arange(12).reshape(3,4)
y = np.arange(12,24).reshape(3,4)
'''
np.vstack((matrix_1,matrix_2)) --> Sirve para unir 2 matrices siempre y cuando tengan la misma cantidad de columnas
OJO: esta une verticalmente en el eje y
'''
print(np.vstack((x,y)))
'''
np.hstack((matrix_1,matrix_2)) --> Sirve para unir matrices siempre y cuando estas tenagn ;amisma cantidad de filas
OJO: esta une horizontalmente en el eje x
'''
print(np.hstack((x,y)))
print('\n\n\nNewaxis')
