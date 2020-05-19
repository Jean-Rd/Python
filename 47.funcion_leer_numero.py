# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:48:46 2020

@author: DELL.E5430.SSD
"""

def get_number_from_user():

    while True:

        x = input("Ingresa un número: ")

        try:

            x = int(x)

        except ValueError:

            print(f"{x} no es válido. Se espera un número")
            continue


        return x