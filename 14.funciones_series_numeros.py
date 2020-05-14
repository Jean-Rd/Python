# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:10:51 2020

@author: DELL.E5430.SSD
"""

while 1:
    def num_series(numeros):
        series = 1
        contador = numeros[0]
        for i in numeros:
            if(i != contador):
                contador = i
                series += 1
            else:
                pass
        return series
    
    
    rango = int(input('Ingrese la canntidad de numeros: '))
    numeros = []
    for i in range(rango):
        numerito = int(input('Digite un numero --> '))
        numeros.append(numerito)
    print('El numero de series es -->',num_series(numeros))
    opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDgite una opcipn: '))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        break
    else:
        print('Por favor digite una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDgite una opcipn: '))
    