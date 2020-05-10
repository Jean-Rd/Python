# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:18:15 2020

@author: DELL.E5430.SSD
"""

import numpy as np
# mediante hsplit se puede dividir en el eje horizontal

x = np.arange(24).reshape(2,12) # matrix enteros

a = np.floor((x)) # np.floor -->  convierte  matrix float vectores
print('float\n',a)
print('\nint\n',x)

'''
dividir veriticalmente verificar
np.hsplit() --> h de dividir horizontalmente
divide en vectores o matrices de ranfo 0 a 3
'''
print('\n',np.hsplit(a,3),'\n')

'''
np.hsplit(matrix,rangos) --> divide y pera en columnas o matriz dando el parametro 
en este caso la el numero 3 cae en la posicion 3 y el 4 -1 e imprime esa columna
Split a after the third and the fourth column
Dividir un después de la tercera y la cuarta columna.
'''
print(np.hsplit(a,(3,4)))
#en rango a dila 3 y 4-1 poscicion de la letra

