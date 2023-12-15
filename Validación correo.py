""" 1-Solicitar al usuario que ingrese su dirección email.              
  Imprimir un mensaje indicando si la dirección es válida o no,     
  valiéndose de una función para decidirlo. 
  Una dirección se considerará válida si contiene el símbolo "@". """

def validacion(email):
  b = email.count("@")  # b = banderilla
  if b == 1:
    return True
  else: return False

correo = input("\nIngresa tu correo eléctronico:\n>>> ")

if validacion(correo):
  print("\nDirección de correo válida.\n")
else: print("\nDirección de correo inválida.\n")

# Castellanos Moreno José Ángel  01-ISOF   #: 21050066