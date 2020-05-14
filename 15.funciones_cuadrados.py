# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:14:44 2020

@author: DELL.E5430.SSD
"""

import numpy as np
import datetime

while 1:
    def num_cuadrados(lista):
        return lista**2
    
    rango = int(input('Digite el rango: '))
    numeros = np.arange(rango)
    for i in range(len(numeros)):
        numero = int(input('Digite un numero --> '))
        numeros[i] = numero
    print(num_cuadrados(numeros))
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        break
    else:
        print('Ingrese una opcion valida por favor.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    