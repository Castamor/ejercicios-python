""" 2-Solicitar números al usuario hasta que ingrese el cero. 
  Por cada uno, mostrar la suma de sus dígitos (utilizando una 
  función que realice dicha suma). """

def sumar(n):
    suma=0
    while n!=0:
        valor=n%10
        suma=suma+valor
        n=n//10
    return suma

num = 1
while num!=0:
    num=int(input("Escribe un número:\n>>> "))
    if num != 0:
        print(f"Suma de los digitos es {sumar(num)}")
    else: print("Finalizaste el programa")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066