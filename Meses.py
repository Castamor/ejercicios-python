#2-capturar una palabra y dependiendo de ella decir un número del 1 al 12   (donde si se captura enero será 1, febrero será 2, marzo será 3.... diciembre será 12) considerar que el usuario puede capturar (por ejem.)   EnErO y seguirá siendo 1 o dicieMBRE y seguirá siendo 12	

mes = input("Teclea el nombre de un mes::\n>> ")
mes = mes.lower()

if mes == "enero":
    print("Equivale al número 1")
elif mes == "febrero":
    print("Equivale al número 2")
elif mes == "marzo":
    print("Equivale al número 3")
elif mes == "abril":
    print("Equivale al número 4")
elif mes == "mayo":
    print("Equivale al número 5")
elif mes == "junio":
    print("Equivale al número 6")
elif mes == "julio":
    print("Equivale al número 7")
elif mes == "agosto":
    print("Equivale al número 8")
elif mes == "septiembre":
    print("Equivale al número 9")
elif mes == "octubre":
    print("Equivale al número 10")
elif mes == "noviembre":
    print("Equivale al número 11")
elif mes == "diciembre":
    print("Equivale al número 12")
else:
    print("No hay ningún mes con ese nombre")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066