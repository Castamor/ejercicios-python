""" 5-Solicitar al usuario un número entero y luego un dígito de no menos de
  7 ns. Informar la veces de ocurrencias del dígito en el número, 
  utilizando para ello una función que calcule la frecuencia. 
     6      87665444        2   
     7      987775432377547 6 """

def ocurrencias(num,digito):
   veces = 0
   while num != 0 :
       ultDigito = num%10
       if ultDigito == digito :
           veces += 1
       num = num//10
   return veces

ns = False
while ns == False :
    valor = int(input("Teclea un Dígito:\n>>>"))
    n = input("Tecla un Número (Mayor a 7 ns): ")
    ns = len(n)
    if ns >= 7 :
        ns = True
        n = int(n)
    else: print("\nEl número no es mayor a Siete digitos")

print(f"Ocurrencias del dígito en el número: {ocurrencias(n,valor)}")

# Castellanos Moreno José ANGEL  01-ISOF  #: 21050066