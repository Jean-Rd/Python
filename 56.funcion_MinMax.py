# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:01:30 2020

@author: DELL.E5430.SSD
"""

import datetime

def MinMax(a,b,c):
    if a < b:
        if a < c:
            min = a
        else:
            min = c
    else:
        if b < c:
            min = b
        else:
            min = c
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return [min, max]


def NumUser():
    while True:
        x = input('DAme un numero --> ')
        try:
            int(x)
        except ValueError:
            print(f'{x}, no es un numero.')
            continue
        return int(x)

def Data():
    Num = list()
    for i in range(3):
        y = NumUser()
        Num.append(y)
    return Num

# Programa Principal
ahora = datetime.datetime.now()

ListNum = Data()
x = ListNum[0]
y = ListNum[1]
z = ListNum[2]

Result = MinMax(x,y,z)

print('Minino:',Result[0])
print('Maximo:',Result[1])
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))





