# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:28:18 2020

@author: DELL.E5430.SSD
"""

import numpy as np
import datetime
while 1:
    def diferencia(numeros):
        for i in range(len(numeros)):
            if(numeros[i] == 0):
                return i
    
    ahora = datetime.datetime.now()
    rango = int(input('Digite el rango: '))
    numero = np.arange(rango)
    for i in range(rango):
        numero[i] = int(input('Digite un numero --> '))
    print('La diferencia es:',diferencia(numero)+1)
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))    
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        print('Lamentamos verlo irse.')
        break
    else:
        print('Por favor ingrese una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
