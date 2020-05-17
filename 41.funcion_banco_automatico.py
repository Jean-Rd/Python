# -*- coding: utf-8 -*-
"""
Created on Sun May 17 07:58:18 2020

@author: DELL.E5430.SSD
"""


OPCIONES = {
    "a": "Ingresar dinero",
    "b": "Retirar diner",
    "c": "Consultar saldo"
}


LETRAS = OPCIONES.keys()

def menu():

    elegida = None

    while elegida not in LETRAS:

        print("\n\n\tCajero automático\n")

        for letra in LETRAS:
            print(letra + ") " + OPCIONES[letra])


        if elegida == None:
            elegida = input("\nIngrese una opción: ")
        else:
            elegida = input("\nPor favor, ingrese una opción válida: ")

    
    return elegida


la_opcion_elegida = menu()

print("\nSe eligió la opción {}".format(la_opcion_elegida))