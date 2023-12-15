def recursividad(filas = 1):
    if filas == 1: return print('[1]')
    
    arrayPrincipal = []
    for fila in range(filas):
        tab = '\t' * (filas-fila)
        fila = generarFila(fila)
        print(tab, fila)


def generarFila(numeroFila, ArrayAnterior = [1]):
    if numeroFila == 0: return [numeroFila + 1]

    array = []
    # array.append(ArrayAnterior[])
    # print(array)

# generarFila(0)
recursividad(2)