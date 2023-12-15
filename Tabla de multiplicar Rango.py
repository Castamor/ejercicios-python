""" 1-Pedir 2 números (el primero será menor al segundo)
    presentar las tablas de multiplicar comprendidas en el rango
    del primer número y el segundo """

print("\nTeclea dos números, el primero menor que el segundo.")
Pnum = int(input("Primer número: "))    # Pnum = Primer Número
Snum = int(input("Segundo número: "))   # Snum = Segundo Número

while Pnum <= Snum :
    print(f"\n======= TABLA DEL {Pnum} =======")
    tabla = Pnum
    for i in range(1, 11):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")
    Pnum += 1

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066