# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:17:05 2020

@author: DELL.E5430.SSD
"""


import datetime
while 1:
    def concatenate(lista):
        m = []
        m.append((lista)*6)
        return m
    ahora = datetime.datetime.now()
    numeros = []
    rango = int(input('Digite un rango: '))
    for i in range(rango):
        num = int(input('Digite un numero --> '))
        numeros.append(num)
    print('Concatenado 6 veces:\n')
    print(concatenate(numeros))
    print(ahora.strftime('%d/%m/%Y  %H:%M:S'))
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        print('Lamentamos verlo irse.')
        break
    else:
        print('Por favor digite una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    