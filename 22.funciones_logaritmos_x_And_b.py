# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:53:15 2020

@author: DELL.E5430.SSD
"""

from math import log

def log_x_and_b(x,b):
    
   result = log(x,b)

   return result

# Programa Principal

while True:
    
    b = int(input('Digite la base del logaritmo: '))
    
    x = int(input('Digite un numero: '))
    
    if(x < 0 or b < 0):
        
        print('Por favor digite valores mayores a cero.')
        
        pass
    
    else:
        print('el resultado es -->',log_x_and_b(x,b))
        
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nIngrese una opcion por favor: '))
        
        if opcion == 1:
            pass
        
        elif opcion == 2:
            break
        
        else:
            
            print('Por favor ingrese una opcion valida.')
        
            opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nIngrese una opcion por favor: '))