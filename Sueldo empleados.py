""" 7-Captura el sueldo de 10 empleados. Al final de captura, muestrame
    el total de nómina a pagar. Ejemplo
    5.12
    10.20
    15.0
    20
    12.25
    7.01
    32.98
    2.8
    9.0
    9.89
  ----------
    124.25 """
    
x = 0
sueldo = 0
result = 0

while x < 10: 
    sueldo = float(input("Valor del sueldo [Mxn]:\n>>> "))

    result += sueldo
    x += 1

print(f"\n\tValor total de la nómina: ${result} mxn\n")

# Castellanos Moreno José Ángel 01-ISOF #: 21050066