# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:53:25 2020

@author: DELL.E5430.SSD
"""


def numeros_amigos(num1):
    suma = 0
    for i in range(1,num1):
        if(num1 % i == 0):
                suma += i
    return suma

def tabla_amigos(m):
    a = []
    amigos = []
    c = []
    for i in range(1,m+1):
        if(numeros_amigos(i) in range(1,m+1)):
            c.append(i)
            a.append(numeros_amigos(i))
    for i in range(len(c)):
        if(numeros_amigos(a[i]) == c[i] and a[i] != c[i] and c[i] not in amigos and a[i not in amigos]):
            amigos.append(c[i] and a[i])
            print(f'Los numeros {c[i]}^{a[i]}, son amigos.')

numero = int(input('Digite un numero --> '))
print(tabla_amigos(numero))
