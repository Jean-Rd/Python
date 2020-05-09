# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:05:49 2020

@author: DELL.E5430.SSD
"""

import numpy as np

#creando Array
a = np.array([20,30,40,50])
b = np.arange(4)
print(a,'\n',b)
#Resta
c = a-b
#Suma
d = a+b
print(f'resta\n{c}\nSuma\n{d}')
#Potenciacion
print(a**2,'\n',b**2)
#Algrebra operaciones
'''
10* --> multiplicamos por 10
np,sin(variable) --> funcion sin similar a math
'''
expresion = 10*np.sin(a)
print('\n',expresion,'\n')
'''
verificancion de datos;  devuelve boolean (True v False)
'''
a = np.array([20,30,40,50])
print(a<35,'\n')
'''

'''
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
# Producto escalar- matematicamente mal, es un erros que puede ser utilizado estrategican,ente
c = A * B
print('matris a\n',A,'\nmatriz b\n',B,'\nproducto escalar\n',c)
'''
producto de matrixes filas por columnas
'''
c = A @ B
print('Producto de matrices filas por columnas')
print(c,'\no tambien esta este otro metodo')
print(A.dot(B))
