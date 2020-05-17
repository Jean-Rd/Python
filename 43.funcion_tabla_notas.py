# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:45:10 2020

@author: DELL.E5430.SSD
"""


import datetime
import time

def menu_opciones():
    print("\n\n")
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
    opcion = None
    while opcion not in LETRAS:
        print('\n\tMENU DE OPCIONES\n')
        for letra in LETRAS:
            print(letra+')',OPCIONES[letra])
        if opcion == None:
            opcion = input('Ingrese una opcion: ')
        else:
            opcion = input('Por favor, ingrese una opcion valida: ')
    return opcion

def muestra_alumno(ALUMNOS,NOTAS,alumno_buscado):
    for i in range(len(ALUMNOS)):
        if ALUMNOS[i] == alumno_buscado:
            print(alumno_buscado,NOTAS[i])
            return
    print(f'El alumno {alumno_buscado}, no pertenece al grupo.')
        
def cantidad_estudiantes_aprobados(NOTAS):
    aprobados = 0
    for i in range(len(NOTAS)):
        if NOTAS[i] in range(51,101):
            aprobados += 1
    print('Cantidad de estudiantes aprobados:',aprobados)
    
def estudiante_mayor_nota(ALUMNOS,NOTAS):
    for i in range(len(NOTAS)):
        if NOTAS[i] == max(NOTAS):
            print('Estudiante:',ALUMNOS[i])
            print('Nota:',NOTAS[i])
            return

def mayor_a_la_media(ALUMNOS, NOTAS):
    media = sum(NOTAS)//len(NOTAS)
    for i in range(len(NOTAS)):
        if NOTAS[i] in range(media,101):
            print('Estudiante:',ALUMNOS[i])
            print('Nota:',NOTAS[i])
    return

def estudiantes_aprobados(ALUMNOS, NOTAS):
    for i in range(len(NOTAS)):
        if NOTAS[i] in range(51,101):
            print('Estudiante:',ALUMNOS[i])
            print('Notas:',NOTAS[i])
    return

def estudiantes_reprobados(ALUMNOS, NOTAS):
    for i in range(len(NOTAS)):
        if NOTAS[i] in range(0,51):
            print('Estudiante:',ALUMNOS[i])
            print('Notas:',NOTAS[i])
    return

# Prograna Principal

ahora = datetime.datetime.now()

lista_alumnos = []
lista_notas = []

cant_alumnos = int(input('Ingrese la cantidad de estudiantes: '))
for i in range(cant_alumnos):
    notas = 0
    lista_alumnos.append(input('Ingrese el nombre del estudiante: '))
    notas = round(float(input(f'Ingrese la nota del estudiante {lista_alumnos[i]}: ')))
    while not(0 < notas <= 100):
        print('Error, la nota no es valida; Intentelo de nuevo.')
        notas = round(float(input(f'Ingrese la nota del estudiante {lista_alumnos[i]}: ')))
    lista_notas.append(notas)

OPCIONES = {
        '1':'Buscar estudiante',
        '2':'Cantidad de estudiantes aprobados',
        '3':'Estudiante con mayor nota',
        '4':'Estudiantes con nota mayor e igual ala media',
        '5':'Estudiantes aprobados',
        '6':'Estudiantes reprobados',
        '7':'Salir'
        }
LETRAS = OPCIONES.keys()
while (True):
    opcion_requerida = menu_opciones()
    if(opcion_requerida == '1'):
        print('\n\n\tBuscar Estudiante\n')
        print('La funcion requerida es:',opcion_requerida)
        search_student = input('Ingrese el nombre del estudiante: ')
        muestra_alumno(lista_alumnos,lista_notas,search_student)

    if(opcion_requerida == '2'):
        print('\n\n\tCantidad De Estudiantes Aprobados\n')
        print('La funcion requerida es:',opcion_requerida)
        cantidad_estudiantes_aprobados(lista_notas)

    if(opcion_requerida == '3'):
        print('\n\n\tEstudiante Con Mayor Nota\n')
        print('La funcion requerida es:',opcion_requerida)
        estudiante_mayor_nota(lista_alumnos, lista_notas)

    if(opcion_requerida == '4'):
        print('\n\n\tNotas Mayor A La Media\n') 
        print('La funcion requerida es:',opcion_requerida)
        mayor_a_la_media(lista_alumnos, lista_notas)

    if(opcion_requerida == '5'):
        print('\n\n\tEstudiantes Aprobados\n')
        print('Opcion requerida:',opcion_requerida)
        estudiantes_aprobados(lista_alumnos, lista_notas)

    if(opcion_requerida == '6'):
        print('\n\n\tEstudiantes Reprobados\n')
        print('Opcion requerida:',opcion_requerida)
        estudiantes_reprobados(lista_alumnos, lista_notas)

    if(opcion_requerida == '7'):
        print('\n\n\tSalir\n')
        print('Opcion requerida:',opcion_requerida)
        print('\nLamentamos verlo irse.')
        break

    time.sleep(5)