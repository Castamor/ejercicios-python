# CASTELLANOS MORENO JOSÉ ÁNGEL  01-ISOF  #:21050066

import ast
import os

alumnos = [
            {'nombre':"angel", 'materias':  {'español':10.0,'matematicas': 8.3,'programación': 9.0,'simulación':8.7, 'videojuegos':10.0}  },
            {'nombre':"ximena", 'materias':  {'español':9.0,'matematicas': 10.0,'programación': 10.0,'simulación':7.6, 'videojuegos':8.0}  },
            {'nombre':"berenice", 'materias':  {'español':8.9,'matematicas': 10.0,'programación': 9.8,'simulación':10.0, 'videojuegos':9.1}  },
            {'nombre':"jovanna", 'materias':  {'español':10.0,'matematicas': 9.7,'programación': 9.0,'simulación':10.0, 'videojuegos':9.3}  },
            {'nombre':"denisse", 'materias':  {'español':8.5,'matematicas': 9.4,'programación': 9.9,'simulación':8.0, 'videojuegos':9.5}  },
            {'nombre':"jonathan", 'materias':  {'español':6.6,'matematicas': 8.8,'programación': 9.5,'simulación':8.0, 'videojuegos':9.5}  },
            {'nombre':"angel", 'materias':  {'español':7.6,'matematicas': 6.7,'programación': 7.0,'simulación':8.1, 'videojuegos':7.9}  },
            {'nombre':"montse", 'materias':  {'español':9.9,'matematicas': 8.6,'programación': 8.9,'simulación':9.2, 'videojuegos':8.5}  },
            {'nombre':"nancy", 'materias':  {'español':10,'matematicas': 9.9,'programación': 8.1,'simulación':7.8, 'videojuegos':8.0}  },
            {'nombre':"dalia", 'materias':  {'español':9.5,'matematicas': 9.0,'programación': 9.0,'simulación':8.5, 'videojuegos':8.8}  },
          ]

if os.path.exists("ListaCompleta.txt"):
    print("SE CARGARON LOS DATOS...")
    arc = open("ListaCCompleta.txt", "r")
    textoDelArchivo= arc.read()
    arc.close()
    alumnos = ast.literal_eval(textoDelArchivo)

def imprimir():
    print(f"Alumno/a: {i['nombre'].upper()}") # Imprimir nombre del alumno
    for j in list(i['materias'].keys()): # Convertir el diccionario 'materias' en lista e iterarlos con el for para después imprimir los valores individualemente
        print(f"\t  {j.capitalize()}: {i['materias'][j]}")
    print("")

while True:
    opc = int(input("\nTECLEA UNA OPCIÓN EN EL MENÚ:\n[1] Mostrar lista de todos los alumnos\n[2] Mostrar un alumno y sus materias\n[3] Mostrar alumno y una materia\n[4] Agregar un alumno\n[5] Salir\n>>> "))

    if opc == 1:
        print("\nMOSTRAR LISTA DE TODOS LOS ALUMNOS")
        for i in alumnos:
            imprimir()

        archivo = open("ListaCompleta.txt", "w") 
        archivo.write(str(alumnos))
        archivo.close()

    if opc == 2:
        print("\nMOSTRAR UN ALUMNO Y SUS MATERIAS")    
        # No importa si el nombre se escribe en minusculas, mayús o intercalado; el programa lo leerá igual. Lo que si se toma en cuenta son los acentos.
        nombre = input("Nombre del alumno que deseas buscar:\n>>> ").lower()

        buscador = True
        for i in alumnos:
            if nombre == i['nombre']: # Verificar el nombre
                print("")
                imprimir()
                buscador = False

        if buscador:
            print(f"\n== No se encuentra el nombre {nombre.capitalize()}. Intenta con otro ==\n") 


    if opc == 3:
        print("\nMOSTRAR UN ALUMNO Y UNA MATERIA")
        nombre = input("Nombre del alumno que deseas buscar:\n>>> ").lower()
        materia = input("Nombre de la materia que deseas buscar:\n>>> ").lower()

        buscador = True
        for i in alumnos:
            if nombre == i['nombre'] and materia in i['materias'].keys(): # Verificar nombre y materia
                print(f"\nAlumno/a: {nombre.upper()}\n{materia.capitalize()}: {i['materias'][materia]}")
                buscador = False

        if buscador:
            print(f"\n== Alguno de los dos valores son incorrectos (nombre o materia). Intenta de nuevo ==\n")


    if opc == 4:
        print("\nAGREGAR UN ALUMNO")

        nombre = input("\nEscribe el nombre: ").lower()
        espa = float(input("Calif Español: "))
        matematicas = float(input("Calif Matematicas: "))
        programacion = float(input("Calif Programación: "))
        simulacion = float(input("Calif Simulación: "))
        videojuegos = float(input("Calif Videojuegos: "))

        alumnos.append({'nombre': nombre, 'materias': {'español' :espa, 'matematicas': matematicas, 'programación': programacion, 'simulacion': simulacion, 'videojuegos': videojuegos}})

        archivo = open("ListaCompleta.txt", "w") 
        archivo.write(str(alumnos))
        archivo.close()

    if opc == 5:
        print("\n== SALISTE DEL PROGRAMA ==")
        break

    if opc <= 0 or opc > 5:
        print("\n== Valor no válido. Intenta de nuevo ==")