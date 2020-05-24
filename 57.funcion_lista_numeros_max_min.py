# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:21:20 2020

@author: DELL.E5430.SSD
"""


import numpy as np
import datetime 

def UserNum():
    while True:
        x = input('Dame un numero --> ')
        try:
            int(x)
        except ValueError:
            print(f'{x}, no es un numero.')
            continue
        return int(x)
    
def Range():
    while True:
        x = input('Dame un rango --> ')
        try:
            int(x)
        except ValueError:
            print(f'{x}, no es un numero.')
            continue
        return int(x)
    
def ListNum(Rango):
    Num = np.arange(Rango)
    for i in range(Rango):
        x = UserNum()
        Num[i] = x
    return Num
    
def MinMax(Num):
    return [Num.max(), Num.min()]

def Prg():
    Option = None
    while Option not in Options:
        Option = None
        for i in Options:
            print(i+')',Menu[i])
        if Option == None:
            Option = input('Digite una opcion: ')
        else:
            print('Por favor, ingrese una opcion valida.')
    return Option
        
# Programa Principal
ahora = datetime.datetime.now()

Menu = {
        '1':'Continue',
        '2':'Salir'
        }
Options = Menu.keys()

rg = Range()
Dates = ListNum(rg)
Result = MinMax(Dates)
print('Maximo -->',Result[0])
print('Minimo -->',Result[1])

while True:
    OptionRequest = Prg()
    if OptionRequest == '1':
        rg = Range()
        Dates = ListNum(rg)
        Result = MinMax(Dates)
        print('Maximo -->',Result[0])
        print('Minimo -->',Result[1])

    if OptionRequest == '2':
        break
    
