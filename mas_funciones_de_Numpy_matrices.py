# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:32:53 2020

@author: DELL.E5430.SSD
"""

import numpy as np

matriz = np.arange(12).reshape(3,4)
matriz_2 = matriz
print(matriz,'\n')

print(matriz.ravel()) # Convierte la matriz en un vector

print(matriz.reshape(4,3),'\n') #podemos cambiar el numero de filas y columnas

print('matriz original:\n',matriz,'\nmatriz transpuesta:\n',matriz_2.T)
# name_matriz.T devuelve la matris transpuesta

print('matris original shaoe dimensiones\n',matriz.shape,'\nmatris transpuesta dimensiones shape\n',matriz_2.T.shape)

print()

print('Metodo rezise')
a = np.arange(12).reshape(3,4)
print('Matriz a \n', a)
print('Matriz con metodo resize')
c = a.resize((2,6)) #debe convertir a una matriz de 2x6
print(c)