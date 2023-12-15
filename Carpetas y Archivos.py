# os.chdir(f"C:\\Users\\{user}\\Desktop")
# os.chdir(f"C:\\Users\\{user}\\OneDrive\\Desktop")

import os

print("===================== PARTE UNO =====================")
def leerArchivo(user, name) :
    os.chdir(f"C:\\Users\\{user}\\Escritorio")
    os.makedirs("tarea_21nov")
    os.chdir(f"C:\\Users\\{user}\\Escritorio\\tarea_21nov")

    file = open(f"{name}.txt", "w")
    file.write("Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,")
    file.close()

    file = open(f"{name}.txt", "r")
    print(f"\nCONTENIDO DEL ARCHIVO\n{file.read()}\n\n")
    file.close()

usuario = input("Nombre del Usuario: ")
archivo = input("Nombre del Archivo: ")
leerArchivo(usuario, archivo)


#import os
print("===================== PARTE DOS =====================")
def EscribirArchivo(user, name) :
    os.chdir(f"C:\\Users\\{user}\\Escritorio")
    os.makedirs("tarea_21nov")
    os.chdir(f"C:\\Users\\{user}\\Escritorio\\tarea_21nov")

    file = open(f"{name}.txt", "w"); file.close()
    file = open(f"{name}.txt", "a")
    opc = " "
    print("\nEscribe algo en el archivo [Para finalizar teclea 'FIN']:")
    while opc != "FIN" :
        opc = input(">>> ")
        file.write(opc + "\n")
    file.close()

    file = open(f"{name}.txt", "r")
    print(f"\nCONTENIDO DEL ARCHIVO\n{file.read()}\n\n")
    file.close()

usuario = input("Nombre del Usuario: ")
archivo = input("Nombre del Archivo: ")
EscribirArchivo(usuario, archivo)

# Castellanos Moreno José Ángel 01-ISOF #:21050066