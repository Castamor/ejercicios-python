""" 6-capturar 2 números(A y B) (se supone que el primero será menor
    que el segúndo). ahora imprimir los números dentro del
    rango de A y B. ejemplo:
    si capturo A = 3 y B = 12 entonces imprimir:
    3 4 5 6 7 8 9 10 11 12
    otro ejemplo:
    si capturo A = 5 y B = 9 entonces imprimir:
    5 6 7 8 9"""

a = int(input("Teclea el valor MENOR:\n>>> "))
b = int(input("Teclea el valor MAYOR:\n>>> "))

if a < b :
    while a <= b:
        print(f"{a}", end="")
        if a != b:               # Estas dos líneas sirven para que siempre se
            print(", ", end="")  # agregue una coma al mostrar un número, menos al final.
        a += 1
else:
    print("\tERROR - El primer valor debe ser menor al segundo\n")

# Castellanos Moreno José Ángel 01-ISOF #: 21050066