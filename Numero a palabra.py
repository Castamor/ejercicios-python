""" 9-Capturar un numero X. captura una letra/palabra. ahora hacer un proceso
    que imprima la letra/palabra,  X veces(en un solo renglón). Ejemplo:
    numero = 4     letra = A
    AAAA
    otro ejemplo:
    numero = 5     letra = hola
    holaholaholaholahola
    NOTA: deberán hacer esto con ciclo while! (SIN el "truco" propio de Python)  """

i = 0

x = int(input("Teclea un valor:\n>>> "))
palabra = input("Escribe una palabra o cáracter:\n>>> ")
print("\n", end="") #Línea estetica, no afecta al programa

while i < x :
    print(f"\t{palabra} ", end="")
    i += 1

# Castellanos Moreno José Ángel 01-ISOF #: 21050066