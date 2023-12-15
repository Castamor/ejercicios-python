""" 4-Escribir un programa que permita al usuario ingresar 6
    números enteros, que pueden ser positivos o negativos.

    Al finalizar, mostrar la sumatoria de los números negativos 
    y el promedio de los positivos.
    (NOTA: validar que NO se pueda capturar el 0 (cero)) """

promedio = 0
numerador = 0
denominador = 0
negativos = 0

i = 0
print("\nTECLEA UN NÚMERO (Excepto un 0): ")
while i < 6 :
    # Pedir número
    num = float(input(f"# {i + 1}:  "))
    # Comprobar si el número es válido, si no... muestra el mensaje de error
    if num != 0 :
        if num > 0 :
            numerador += num
            denominador += 1
        if num < 0 :
            negativos += num
        i += 1
    else:
        print(">>> El número no es válido, intenta de nuevo <<<\n")

promedio = numerador / denominador

print("\n======= RESULTADOS =======")
print(f"Promedio de los positivos: {promedio:.2f}\nSumatoria de los negativos: {negativos:.2f}\n")

# Castellanos Moreno José Ángel  01-ISOF #:21050066