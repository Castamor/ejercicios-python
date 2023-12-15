""" 5-capturar un numero x, y despues mostrar la tabla de
    multiplicar (con iteracciones del 1 al 10) de dicho
    número. ejemplo:
    tabla de multiplicar del numero: 5
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    ...
    6 x 10 = 50 """

a = 0 #Intentos
x = 0 #Valor de la tabla
b = 0 #Valor por el que se multiplica
r= 0  #Respuesta

x = int(input("Valor de la tabla:\n>>> "))

while a < 10: 
    while b < 10:
        r = x*(b+1)
        print(f"{x} x {b+1} = {r}\n")
        b += 1
    a += 1

# Castellanos Moreno José Ángel 01-ISOF #: 21050066