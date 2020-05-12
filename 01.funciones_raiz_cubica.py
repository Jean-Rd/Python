# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:33:05 2020

@author: DELL.E5430.SSD
"""


def raiz_cubica(x):
    return x**(1/3)

print('\n\tPROGRAMA PARA HALLAR LA RAIZ CUBICA DE UN NUMERO')

numero = int(input('Digite un numero --> '))
print(raiz_cubica(numero))
opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
while(opcion != 2):
    if(opcion == 1):
        numero = int(input('Digite un numero --> '))
        print(raiz_cubica(numero))
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))

    else:
        print('Por favor imgrese una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
