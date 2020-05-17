# -*- coding: utf-8 -*-
"""
Created on Sat May 16 23:35:05 2020

@author: DELL.E5430.SSD
"""

import time
import datetime

def NamesOfTheStudents(CantAlumnos):
    NameStudent = []
    for i in range(CantAlumnos):
        NameStudent.append(input('Nombre: ').upper())
    return NameStudent

def StudentNotes(NameStudent):
    NoteStudent = []
    for i in range(len(NameStudent)):
        Nota = float(input(f'Digite la nota del estudiante {NameStudent[i]}: '))
        while Nota not in range(0,101):
            print('Error en la nota.')
            Nota = float(input(f'Digite la nota del estudiante {NameStudent[i]}: '))
        NoteStudent.append(Nota)
    return NoteStudent
        
def OptionMenu():
    print('\n\n')
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
    opcion = None
    while opcion not in NumOpciones:
        opcion = None
        print('\n\tMENU DE OPCIONES\n')
        for digito in NumOpciones:
            print(digito+')',OPCION[digito])
        if opcion == None:
            opcion = input('Digite una opcion: ')
        else:
            print('Por favor, ingrese una opcion valida.')
    return opcion

def ApprovedStudents(AllDatesStudents,AllNotesStudents):
    for i in range(len(AllNotesStudents)):
        if AllNotesStudents[i] in range(51,101):
            print('Estudiante:',AllDatesStudents[i])
            print('Notas:',AllNotesStudents[i])

def NumbersApprovedStudent(AllNotesStudents):
    Approveds = 0
    for i in range(len(AllNotesStudents)):
        if AllNotesStudents[i] in range(51,101):
            Approveds += 1
    print('Cantidad de estudiantes aprobados:',Approveds)

def HigherNoteStudent(AllDatesStudents,AllNotesStudents):
    for i in range(len(AllNotesStudents)):
        if AllNotesStudents[i] == max(AllNotesStudents):
            print('Estudiante:',AllDatesStudents[i])
            print('Nota:',AllNotesStudents[i])
            return

def NotesHigherSomeHalf(AllDatesStudents,AllNotesStudents):
    Half = round(sum(AllNotesStudents)/len(AllNotesStudents))
    print('El promedio de la media de las notas del grupo es',Half)
    for i in range(len(AllNotesStudents)):
        if AllNotesStudents[i] in range(Half,101):
            print('Estudiante:',AllDatesStudents[i])
            print('Nota:',AllNotesStudents[i])
    return

def SearchStudent(AllDatesStudents,AllNotesStudents,WantedStudent):
    for i in range(len(AllDatesStudents)):
        if(AllDatesStudents[i] == WantedStudent):
            print('Estudiante:',AllDatesStudents[i])
            print('Nota:',AllNotesStudents[i])
            return
    print(f'El estudiante {WantedStudent}, no pertenece al grupo.')

# Programa Principal
ahora = datetime.datetime.now()

'''
ListStudents = ['MAria','Jean','Lennys']
ListNotes = [67,89,78]
'''
NumberStudents = int(input('Digite la cantidad de estudiantes: '))
ListStudent = NamesOfTheStudents(NumberStudents)
ListNots = StudentNotes(ListStudent)

OPCION = {
          '1':'Estudiantes que aprobaron.',
          '2':'Numeros de estudiantes aprobados.',
          '3':'Estudiante con maxima nota.',
          '4':'Notas mayor o igual que la media de las notas del grupo',
          '5':'Buscar estudiante.',
          '6':'Salir'
          }
NumOpciones = OPCION.keys()

while (True):
    OptionRequest = OptionMenu()
    # ApprovedStudents
    if(OptionRequest == '1'): 
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest,'\n')
        ApprovedStudents(ListStudent, ListNots)
    # NumbersApprovedStudents
    if(OptionRequest == '2'):
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest,'\n')
        NumbersApprovedStudent(ListNots)
    # HigherNoteStudent
    if(OptionRequest == '3'):
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest,'\n')
        HigherNoteStudent(ListStudent, ListNots)
    # NotesHigherSomeHalf
    if(OptionRequest == '4'):
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest,'\n')
        NotesHigherSomeHalf(ListStudent, ListNots)
    # SearchStudent
    if(OptionRequest == '5'):
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest)
        Search = input('Ingrese un nombre: ').upper()
        SearchStudent(ListStudent,ListNots,Search)
    # Exit
    if(OptionRequest == '6'):
        print('\n',OPCION[OptionRequest],'\n')
        print('Opcion requerida:',OptionRequest)
        print('Lamentamos verlo irse.')
        break
    
    time.sleep(5)