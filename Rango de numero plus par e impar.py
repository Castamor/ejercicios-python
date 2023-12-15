""" 8-capturar 2 numeros (A y B. mostrar una lista de numeros que
    empiecen en A y terminen en B (como el problema 6, de hecho).Pero
    ahora tambien mostrarán si es par o impar. Ejemplo:
    capturo
    A = 3    B = 10
    3 - impar
    4 - par
    5 - impar
    6 - par
    7 - impar
    8 - par
    9 -impar
    10 - par """

a = int(input("Valor A:\n>>> "))
b = int(input("Valor B:\n>>> "))

if a < b :
    while a <= b:
        print(f"{a}", end="")
        x = a%2
        if x == 0:
            print("- Par")
        else:
            print("- Impar")
        a += 1
else:
    print("\tERROR - El primer valor debe ser menor al segundo\n")

# Castellanos Moreno José Ángel 01-ISOF #: 21050066