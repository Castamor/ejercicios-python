""" 3-Solicitar números al usuario hasta que ingrese el cero. Por 
  cada uno, mostrar la suma de sus dígitos. Al finalizar, 
  mostrar la sumatoria de todos los números ingresados y 
  la suma de sus dígitos. Reutilizar la misma función realizada 
  en el ejercicio 2. """

def sumar(n):
    suma=0
    while n!=0:
        valor=n%10
        suma=suma+valor
        n=n//10
    return suma

result = 0
nIngresados = 0
num = 1
while num!=0:
    num=int(input("Escribe un número:\n>>> "))
    if num != 0:
        print(f"Suma de los digitos es {sumar(num)}")
        result += num
        nIngresados += 1
    else: print("Finalizaste el programa")

print(f"\nSuma final de todos los digitos: {result}")
print(f"Total de digitos sumados : {nIngresados}")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066