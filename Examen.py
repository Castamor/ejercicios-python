nombres = []

def insertar(valor):
    name = ""
    for x in range(valor):
        name = input("Teclea el nombre: ")
        nombres.append(name)
    transformar(nombres)


def transformar(lista):
    lista = [x.title() for x in nombres]
    print(lista)

    return lista

def mostrar(final):
    print(final)

n= 0
n = int(input("¿Cuantos nombres quieres agregar?:\n>>> "))
insertar(n)