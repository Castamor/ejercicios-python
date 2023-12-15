#3-capturar una cantidad de PESOS y convertirlo a DOLARES (nota: el programa no sabe la cotización del dolar, entonces tambien se tendrá que capturar). Con ese resultado, el programa deberá decir si alcanza (ó no) para comprar una computadora de $2,000.00 dolares.

mxn = float(input("¿Cuál es tu presupuesto? [Mxn]\n>> $ "))
coti = float(input("Valor del dólar:\n>> "))

usd = mxn / coti

print(f"\nTienes {usd} dolares en total")
if usd >= 2000:
    print("Tienes el suficiente dinero para comprar la computadora")
else:
    print("No tienes suficiente dinero para comprar la computadora")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066