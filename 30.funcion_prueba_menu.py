# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:15:06 2020

@author: DELL.E5430.SSD
"""


def prueba_menu():
    opcion = ''
    while len(opcion) != 1 or opcion not in 'abc':
        print('\n\n\tCajero Automatico\n\ta) Ingresar Dinero\n\tb) Retirar Dinero\n\tc) Consultar saldo')
        opcion = input('Ingrese una opcion: ')
        if len(opcion) != 1 or opcion not in 'abc':
            print('Por favor ingrese una opcion valida.')
    return opcion

a = prueba_menu()