""" 2-Capturar una frase (en una cadena)
    contar las ocurrencias de cada una de las letras (de la "A" a la "Z")
    dentro de la cadena. y mostrar los resultados """


abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

palabra = input("\nEscribe algo:\n>>> ")
palabra = palabra.lower()

for i in range(0,27) :
    contador[i] = palabra.count(abecedario[i])
    print(f"{abecedario[i]}: {contador[i]}\t", end="")
    b= (i+1)%3                  # Las líneas 15 y 16 son estéticas, sirven para que
    if b == 0: print("\n")      # en consola cada tres letras de un salto de línea

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066