# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:16:33 2020

@author: DELL.E5430.SSD
"""

import numpy as np
#valor maximo de las series dependientes del tiempo

time = np.linspace(20,145,5)
data = np.sin(np.arange(20)).reshape(5,4)

print('Time')
print(time)
print()
print('Data')
print(data)

#índice de los máximos para cada serie

ind = data.argmax(axis=0)
print('posciciones de los valores maximos en cada columna')
print(ind)

#tiempos que corresponden a los indices maximos
'''
segun la poscicion de los indices maximos busca esa poscicion en time
y los guarda respetando el orde de los indices
'''
print('----------------------------\ntime max')
time_max = time[ind]
print(time_max)
print('-----------------------------\ndata max')
'''
aca imprime los valores maximos que ya buscamos en ind, guarda esos valores 
en data_max
'''
data_max = data[ind, range(data.shape[1])]
print(data_max)
'''
verificamos si los valores de data_max que sacamos con indice
es igual ala funcion data.max(axis=0), que es lo  mismo
'''
print(np.all(data_max == data.max(axis=0)))


print('----------------=======================------------------------')
#tambien podemos usar indexacion de matrices con destinos

a = np.arange(10)
print(a)

a[[1,3,6,-1]] = 3 #damos las posciciones
print(a)
print('podemos cambiar valores como una lista solo agregamos un parentecis m,as')