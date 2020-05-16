# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:41:32 2020

@author: DELL.E5430.SSD
"""

import datetime

def numero_amigo(n):
        suma = 0
        for i in range(1,n):
            if(n % i == 0):
                suma += i
        return suma

def tabla_amigos(m):
    amiguitos = []
    for i in range(1,m+1):
        posible_amigo = numero_amigo(i)
        if(posible_amigo in range(1,m+1)):
            if(numero_amigo(posible_amigo) == i and posible_amigo != i and i and posible_amigo not in amiguitos):
                amiguitos.append(posible_amigo and i)
                print('Los numeros:',i,'^',posible_amigo,', son amigos.')

# Programa Principal
ahora = datetime.datetime.now()

numero = int(input('Digite un numero --> '))
tabla_amigos(numero)
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))