# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:02:27 2020

@author: DELL.E5430.SSD
"""
 
# Separa el mostrar los menus de la operacion con las opciones
def mostraropciones(repeat):
    divider = "\n-------------------------------\n"
	tpr_txt = "\tOPCIÓN INCORRECTA\n\tIntento numero " + str(repeat+1)
	main_txt = "\n\tCajero Automatico \n\na) Ingresar Dinero \nb) Retirar dinero \nc) Consultar Saldo"
	if repeat > 0:
		print(divider +tpr_txt + divider+ main_txt)
    else
	    print("\tCajero Automatico \na) Ingresar Dinero \nb) Retirar dinero \nc) Consultar Saldo")
    
# Menú principal    
def menu():
	opcion = " "
    # Si no está en el rango {a,b,c}, repite hasta que esté
    # Puedes saber el numero que ocupa un caracter en Unicode
    # con la funcion ord(caracter), ejemplio ord("a") = 92
	while "a">opcion or opcion>"c":
		mostraropciones(repeat)
		opcion=input("Ingresa una opción: ")
		repeat = repeat+1
	return opcion

menu()