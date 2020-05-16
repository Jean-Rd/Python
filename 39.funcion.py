# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:03:19 2020

@author: DELL.E5430.SSD
"""

import datetime

def menu_salir():
    opcion = ''
    while not('a' <= opcion <= 'b'):
        print('\n\n\ta) Continuar\n\tb) Salir')
        opcion = input('Ingrese una opcion: ')
        if(opcion == 'a'):
            numero_inverso()
        if not('a' <= opcion <= 'b'):
            print('Por favor ingrese una opcion valida')
    return opcion

def numero_inverso():
    resultado = ''
    numero = input('Dame un numero --> ')
    pos_final = len(numero)-1
    while(pos_final >= 0):
        print(numero[pos_final])
        resultado += numero[pos_final]
        pos_final -= 1
    print(resultado)
    menu_salir()
                
numero_inverso()