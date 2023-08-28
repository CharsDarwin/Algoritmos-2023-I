# from openpyxl import Workbook, load_workbook




from alumno import Alumno
from docente import Docente
from curso import Curso
from datetime import datetime


##########################
listado_alumno=[]
listado_docente=[]
listado_curso=[]


def registrar_alumnos():
    alumno1 = Alumno('Luis',   'García',    'Pérez', '12345678A', '2023001', 'Informática y Sistemas', 2023)
    alumno2 = Alumno('Ana',    'Martínez',  'López', '98765432B', '2023002', 'Informática y Sistemas', 2023)
    alumno3 = Alumno('Carlos', 'Ramírez',   'Vega',  '45678901C', '2023003', 'Informática y Sistemas', 2023)
    alumno4 = Alumno('Laura',  'Hernández', 'Gómez', '56789012D', '2023004', 'Informática y Sistemas', 2023)
    alumno5 = Alumno('Miguel', 'Sánchez',   'Pérez', '34567890E', '2023005', 'Informática y Sistemas', 2023)

    listado_alumno.append(alumno1)
    listado_alumno.append(alumno2)
    listado_alumno.append(alumno3)
    listado_alumno.append(alumno4)
    listado_alumno.append(alumno5)
    print("Registro de docentes")

def registrar_docentes():
    print("Registro de docentes concluido ")
    
    docente1 = Docente('María',  'García',   'López',    '11223344X',   'D2023001',  'Facultad de Ingeniería Informática y Sistemas')
    docente2 = Docente('Juan',   'Martínez', 'Pérez',    '22334455Y',   'D2023002',  'Facultad de Ingeniería Informática y Sistemas')
    docente3 = Docente('Carlos', 'Ramírez',  'Vega',     '33445566Z',   'D2023003',  'Facultad de Ingeniería Informática y Sistemas')
    docente4 = Docente('Ana',    'Sánchez',  'Gómez',    '44556677W',   'D2023004',  'Facultad de Ingeniería Informática y Sistemas')
    docente5 = Docente('David',  'López',    'González', '55667788A',   'D2023005',  'Facultad de Ingeniería Informática y Sistemas')

    listado_docente.append(docente1)
    listado_docente.append(docente2)
    listado_docente.append(docente3)
    listado_docente.append(docente4)
    listado_docente.append(docente5)

def registrar_cursos():
    print("Registro de cursos")
    curso1 = Curso('C001', 'Introducción a la Programación')
    curso2 = Curso('C002', 'Programación Avanzada')
    curso3 = Curso('C003', 'Bases de Datos')
    curso4 = Curso('C004', 'Diseño de Interfaces de Usuario')
    curso5 = Curso('C005', 'Algoritmos y Estructuras de Datos')

    listado_curso.append(curso1)
    listado_curso.append(curso2)
    listado_curso.append(curso3)
    listado_curso.append(curso4)
    listado_curso.append(curso5)

def asignar_docente_curso():
    print("Asignación de docente a curso")
    for i in range(5):
        listado_curso[i].asignar_docente(listado_docente[i])


def asignar_curso_alumno():
    print("Asignación de cursos a alumno")
    for alumno in listado_alumno:
        for curso in listado_curso:
            alumno.agregar_curso(curso)

import random

def actualizar_docente_curso():
    print("Actualización de docente en curso")
    
    # Obtener una copia aleatoria de la lista de docentes
    docentes_aleatorios = list(listado_docente)
    random.shuffle(docentes_aleatorios)
    
    # Asignar docentes aleatorios a los cursos en orden
    for i, curso in enumerate(listado_curso):
        docente_index = i % len(docentes_aleatorios)
        curso.asignar_docente(docentes_aleatorios[docente_index])

     
    
    

def registrar_notas_alumno():
    print("Registro de notas de alumno")
    
    for alumno in listado_alumno:
        print(f"Notas para el alumno {alumno.get_nombre()}:")
        for curso in alumno.Curso:
            # Pedir las notas para cada curso
            notas = []
            for i in range(4):
                nota = float(input(f"Ingrese la nota {i + 1} para el curso {curso.get_nombre()}: "))
                notas.append(nota)
            
            # Ingresar las notas al curso
            curso.ingresar_notas(notas)



def reporte_alumno():
    print("Generando el Reporte de alumno")
    fecha_actual = datetime.now()
    formato = fecha_actual.strftime("%d_%m_%Y")
    print("Fecha actual en formato 'día_mes_año':", formato)
    nom_reporte = 'report_'+ formato + '.txt'
    with open(nom_reporte, 'a', encoding="utf-8") as archivo:
        encabezado = "Apellidos               Nombre                  DNI                 Código              Facultad                                Año de Ingreso\n\n"
        archivo.write(encabezado)
        for alumno in listado_alumno:
            archivo.write(alumno.imprimir())


def reporte_docente():
    print("Reporte de docente")
    
    fecha_actual = datetime.now()
    formato = fecha_actual.strftime("%d_%m_%Y")
    print("Fecha actual en formato 'día_mes_año':", formato)
    nom_reporte = 'report_Docente_'+ formato + '.txt'
    with open(nom_reporte, 'a', encoding="utf-8") as archivo:
        encabezado =  "Apellidos               Nombre                  DNI                     Código                  Facultad\n\n"
        archivo.write(encabezado)
        for docente in listado_docente:
            archivo.write(docente.imprimir())


##diccionario
opciones = {
    "1": registrar_alumnos,
    "2": registrar_docentes,
    "3": registrar_cursos,
    "4": asignar_docente_curso,
    "5": asignar_curso_alumno,
    "6": actualizar_docente_curso,
    "7": registrar_notas_alumno,
    "8": reporte_alumno,
    "9": reporte_docente,
    "10": exit
}


while True:
    print("\t\t\t\t\t\t\tMenú:\n")
    print("\t\t\t\t\t\t1. Registrar alumnos")
    print("\t\t\t\t\t\t2. Registrar docentes")
    print("\t\t\t\t\t\t3. Registrar cursos")
    print("\t\t\t\t\t\t4. Asignar docente curso")
    print("\t\t\t\t\t\t5. Asignar curso alumno")
    print("\t\t\t\t\t\t6. Actualizar docente curso")
    print("\t\t\t\t\t\t7. Registrar notas alumno")
    print("\t\t\t\t\t\t8. Reporte de alumno")
    print("\t\t\t\t\t\t9. Reporte de docente")
    print("\t\t\t\t\t\t10. Salir")

    seleccion = input(("Seleccione una opción: "))
    
    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print(("Opción no válida. Por favor, seleccione una opción válida."))



# presentacion brebe que solucione al nivel grafico
# epxlicacion a nivel estructural
# demostracion
# examen el menu implemetar
# 25 - 29 septiembre 
