""" 5-Hacer un programa que pida la base y la altura (ambos deberán ser
    no menores de 3 y no mayores de 30) de un rectángulo.
    Después, dibujar el rectángulo
    ejemplo:
      base : 15
      altura : 4
      ***************
      *             *         
      *             *
      *************** """

base = 0
altura = 0

# ========================= PEDIR VALORES ========================= #
b = True
while b == True :
    base = int(input("\nTeclea la BASE [3-30]: "))
    if base >= 3 and base <= 30 :
        b = False
    else:
        print(">>> La base no es válida, intenta de nuevo <<<")

b = True
while b == True :
    altura = int(input("\nTeclea la ALTURA [3-30]: "))
    if altura >= 3 and altura <= 30 :
        b = False
    else:
        print(">>> La altura no es válida, intenta de nuevo <<<")

# ========================= MOSTRAR RECTÁNGULO ========================= #

# LÍNEA DE ARRIBA
for i in range(base):
    print("*", end="")
print("")

# LÍNEAS DEL MEDIO
altura -= 2
espacioEnBlanco = base - 2
for i in range(altura):
    print("*", end="") # Primer asterisco
    for i in range(espacioEnBlanco):
        print(" ", end="") # Espacios en blanco
    print("*") # Asterisco Final

# LÍNEA DE ABAJO
for i in range(base):
    print("*", end="")

# Castellanos Moreno José Ángel  01-ISOF #:21050066