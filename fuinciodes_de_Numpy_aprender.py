# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:52:29 2020

@author Lustroso Burbuja
"""
import numpy as np
from numpy import pi
'''
podemos crear una matriz o vector, indicando el tipo de dato que se guardara
'''
#m = int(input('Digite el numero de filas: '))
#n = int(input('Digite el numeros de columnas: '))

c = np.array([[1,2],[2,3]], dtype = complex)
print(c,'\n')
'''
Llenamos una matriz de creros
'''
matriz_1 = np.zeros((3,4)) #siempre dos parentesis no olvidarse
print(matriz_1,'\n')
'''
Llenamos una matriz de unos
'''
matriz_2 = np.ones((3,4))
print(matriz_2,'\n')
'''
con el metodo empty impriminos una matriz con sus parametoros/no inicializada
'''
a = np.empty((2,3))
print(a,'\n')
'''
name_vector = np.arange(inicio,fin,rango_de_intervalos) 
con este metodos pasamos a un vector un incio y un fin mas la distancia de separacion de estos numeros
NOTA --> podemos almacenarlos en una variable y imprimir la variable, cumple la misma funcion que el ejemplo siguiente
'''
vector_1 = np.arange(0,21,2)
#print(vector_1) 
print(np.arange(0,21,2)) #cumple la misma funcion que la linea de arriba
'''
---> Este metodo tambien funciona con decimales, veamos el siguiente ejemplo
'''
print(np.arange(0.5,2.6,0.05),'\n\n')
'''
name_vector = linspace(inicio,fin,cantidad_de_numeros_que_queremos_en_este_rango)
recibe como argumento la cantidad de numeros que queremos en parametros dados
'''
b = np.linspace(0,2,9)
print(b)
print(np.linspace(0,20,5))

x = np.linspace(0,2*pi,100) #útil para evaluar la función en muchos puntos
f = np.sin(x)
#print(x)
#print(f)
'''
Funciones extras
-----linspace
'''
print('\n\nExtras\n')
print(np.linspace(2,3,5))
#para impimir sin el valor de final
print(np.linspace(2,3,5,endpoint = False))
#para imprimir el valor que separa cada numero
print(np.linspace(2,3,3, retstep = True))
