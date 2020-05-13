# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:43:49 2020

@author: DELL.E5430.SSD
"""

import numpy as np
import datetime

while 1:
    def maximo(numero):
        if len(numero) > 0:
            candidato = numero[0]
            for elemento in numero:
                if elemento > candidato:
                    candidato = elemento
        else:
            candidato = None
        return candidato
    
    rango = int(input('Digite un rango: '))
    numeritos = np.arange(rango)
    for i in range(rango):
        num = float(input("Digite un numero --> "))
        numeritos[i] = num
    print(maximo(numeritos))
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        break
    else:
        print('Por favor ingrese una opcion valida.')
        Opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    