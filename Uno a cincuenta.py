""" 3-programa que imprima numero del 1 al 50, pero
    en lineas de 5 lineas cada una. ejemplo:
    1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    ...
    ...
    45 46 47 48 49 50 """

x = 1
b=1
while x <= 50:
    print(f"{x} ", end="")
    b= x%5
    if b == 0: print("\n")
    x += 1

# Castellanos Moreno José Ángel 01-ISOF #: 21050066