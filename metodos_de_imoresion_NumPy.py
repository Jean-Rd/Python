# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:27:12 2020

@author: DELL.E5430.SSD
"""


import numpy as np
# MATRIZ IMPRESION
#1D array
print('-------------1-----------------')
a = np.arange(6)
print(a)
'''
Impriminos nuestra m,atriz ingresando rango y dilas , columnas
np.arange(inicio,fin).reshaoe(filas,columnas)
'''
#2D array
print('-------------2-----------------')
b = np.arange(0,6).reshape(2,3)
print(b)

'''
ahora imprimiremos una mastriz que numpy denoniman 3D
np.arange(rango).reshape(dimesion,fila,columna)
'''
#3D array
print('-------------3-----------------')
print()
c = np.arange(24).reshape(2,3,4)
print(c,'\n')

'''
si su matriz es demasiado grande NumPy solo imprime imprime las esquinas, omite la parte central
'''
print('-------------1-----------------')
e = np.arange(1000000)
print(e,'\n')
e_prima = np.arange(10000).reshape(100,100)
print(e_prima,'\n')
