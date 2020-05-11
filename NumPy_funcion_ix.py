# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:29:08 2020

@author: DELL.E5430.SSD
"""


import numpy as np

a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
'''
convierte las filas en  columnas
'''
print(ax)
print()
print(bx)
print()
print(cx)
print()
# Dimensiones
print(ax.shape, bx.shape, cx.shape)

result = ax+bx*cx
print(result)















result[3,2,4]

a[3]+b[2]*c[4]
