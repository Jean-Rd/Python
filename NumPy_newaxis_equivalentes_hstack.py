# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:41:29 2020

@author: DELL.E5430.SSD
"""

import numpy as np
from numpy import newaxis

x = np.arange(12).reshape(3,4)
y = np.arange(12,24).reshape(3,4)


matrix = np.column_stack((x,y)) #lo mismo que hstack
print(matrix)

print('separando matrices')
print('matris x\n',x)
print('x.newaxis')

print('matrix y\n',y)
print('matrix x\n',x,'\nmatrix y\n',y)

'''
np.column_stack --> este metodo de 2 newaxis en 2 matrices es para enlazar los primeros vectores que
genera axis en cada matrix, segundos y terceros
es como un producto escal;ar pero de matrices forma una nuema matriz(agrega en el eje y)
'''

print('Usanco np.column_stack((x[:,newaxis],y[;,newaxis]))')
print(np.column_stack((x[:,newaxis],y[:,newaxis])))


print('newaxis en x')
print(x[:,newaxis]) 
print('newaxis en y')
print(y[:,newaxis])
# Esto es equivalente a hstack


