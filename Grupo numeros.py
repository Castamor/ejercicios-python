""" 3-Capturar 20 números (numero entre 1 y 50)
    Después, separarlos en 2 grupos 
      a) números del 1 al 25 
      b) números del 26 al 50
    Finalmente, presentar resultados (ambos grupos de números) """

grupo1 = []
grupo2 = []

i = 0
print("\nTECLEA UN NÚMERO ENTRE EL 1 - 50: ")
while i < 20 :
    # Pedir número
    num = int(input(f"# {i + 1}:  "))
    # Comprobar si el número está en el rango y agruparlo, si no... muestra el mensaje de error
    if num >= 1 and num <= 50:
        if num <= 25: grupo1.append(num)
        if num >= 26: grupo2.append(num)
        i += 1
    else:
        print(">>> El número no es válido, intenta de nuevo <<<\n")

# Mostrar resultados
print(f"\n======= GRUPO 1 (1-25) =======\n{grupo1}")
print(f"\n======= GRUPO 2 (26-50) =======\n{grupo2}\n")

# Castellanos Moreno José Ángel  01-ISOF  #:21050066