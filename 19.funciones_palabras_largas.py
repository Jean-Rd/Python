# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:35:28 2020

@author: DELL.E5430.SSD
"""


while 1:
    def mayor_lista(cadena):
        cadena = cadena.split()
        c = cadena[0]
        mayores = []
        for i in range(len(cadena)):
            if(len(cadena[i]) > len(c) or len(cadena[i]) == len(c)):
                c = cadena[i]
                mayores.append(cadena[i])
        return mayores
    cadena = input('Ingrese un texto: ')
    print('Lax palabrax mas largax son:',mayor_lista(cadena))
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):  
        print('Lamentamos verlo irse.')
        break
    else:
        print('Por favor ingrese una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    