""" 10-Captura el sueldo de 5 empleados. Al ir obteniendo el sueldo.
    si el sueldo es mayor a 10.00 entonces restarle el 4% de ISR y
    al final mostrar el total a pagar al SAT y a los empleados:
    ejemplo:
    captura    $%     captura - 4%
    5.12      0.00        5.12      <---- menor de 10; no se le quita 4%
    10.2      0.41        9.79
    15        0.60        14.40
    7         0.00        7.00      <---- menor de 10; no se le quita 4%
    19.25     0.77        18.48
    ----------------------------
    56.57     1.78        54.79     <---- totales """

x = 0
sueldo = 0
resta = 0
final = 0
result = 0

while x < 5: 
    sueldo = float(input("\nValor del sueldo [Mxn]:\n>>> "))
    if sueldo <= 9:
        resta = 0
        result += sueldo
        print(f"\tCaptura:\t-$%\t\tFinal:\n\t{sueldo:.2f}\t\t{resta:.2f}\t\t{sueldo:.2f}")
    else:
        resta= sueldo*.04
        final= sueldo - resta
        result += final
        print(f"\tCaptura:\t-$%\t\tFinal:\n\t{sueldo:.2f}\t\t{resta:.2f}\t\t{final:.2f}")
    x += 1

print(f"\n\tTotal a pagar al SAT: ${result:.2f} mxn\n")

# Castellanos Moreno José Ángel 01-ISOF #: 21050066