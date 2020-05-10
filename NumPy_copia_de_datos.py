# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:58:49 2020

@author: DELL.E5430.SSD
"""

import numpy as np
'''
Este es un erros muy tipico no estamos creando otra matriz solo estamos
dando dos nombres a una en este caso a y b/ yo cometo este error pero
con esta guia ya podre repararlo
'''
print('-----------------Sin copia-------------------')
a = np.arange(12).reshape(3,4)
print(a)
b = a
print(b)
print(b is a)
print('-------------VER O COPIAR------------')
# name_matriz ---> es solo una vista de los datos que posee
c = a.view()
print(c)
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c = c.reshape(2,6)
print(c) # no da xdxd
print(a.shape)
c[0,4] = 1020
print(a)
# con eso queda demostrado que solo otorgamos 2 nombres difirentes ala matriz
print('----------------------')
s = a[ : ,1:3]
#los ppuntos solo es parea todas las filas
#los puntos 1:3 es de columna 1 a 3-1=2
s[:] = 10 # todo s vale 10 con los rangos que asigna,os arriba
print(a) # de nuevo solo otorgamos 3 nombres ala matriz
print('-----------------REALIZAMOS COPIA SIN OTORGAR NOMBRE OTRO DATO---------------')
d = a.copy() #crea,os otro dato
print(d is a) #false por que es diferente datos
d[0,0]= 1000
print('matriz a:\n',a)
print('matriz d:\n',d)
print('--------------------CORTES DATOS GRANDES--------------------')
x = np.arange(int(1e8))#creamops 10 millones de numeros
y = x[:100].copy()#solo copiamos los primeros 100
del(x)#borramos x de la memory
print(y)
