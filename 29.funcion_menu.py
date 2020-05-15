# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:36:50 2020

@author: DELL.E5430.SSD
"""


def menu():
    opcion = ''
    while not('a' <= opcion <= 'c'):
        print('\n\n\tCajero Automatico\n\ta) Ingresar Dinero\n\tb) Retirar Dinero\n\tc) Consultar saldo')
        opcion = input('Ingrese una opcion: ')
        if not(opcion >= 'a' and opcion <= 'c'):
            print('Por favor ingrese una opcion valida.')
    return opcion

a = menu()