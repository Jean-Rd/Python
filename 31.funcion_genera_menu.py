# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:27:39 2020

@author: DELL.E5430.SSD
"""


def menu_generate():
    opcion = ''
    while len(opcion) != 1 or opcion not in '123':
        print('\n\t1. Saluda\n\t2. Despedirse\n\t3. Salir')
        opcion = input('Dame un numero: ')
        if(len(opcion) != 1 or opcion not in '123'):
            print('Por favor digite una opcion valida.')
        if opcion == '3':
            print('Lamentamos verlo irse.')
            break
    return opcion

menu_generate()