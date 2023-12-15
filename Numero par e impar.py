""" 4-Requerir al usuario que ingrese un número entero e informar si es 
  par o no, utilizando una función booleana que lo decida.  
  True : par    False: impar """

def comprobante(num):
   for i in range(2,num):
       if num%i==0:           
           return True
   return False

 
num=int(input("\nTeclea un Número:\n>>> "))
if comprobante(num):
    print("El número es PAR\n")
else:
    print("El número es INPAR\n")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066