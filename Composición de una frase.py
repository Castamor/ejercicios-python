# a) Cuantas letras tiene la frase  e) Cuantos dígitos hay
def caracterDigitos(frase):
        caracter = 0
        digitos = 0

        for i in frase:
            if i.isalpha:
                caracter += 1
            elif i.isdigit:
                digitos += 1

        print(f"\tCaracteres: {caracter}")
        print(f"\tDigitos: {digitos}")


# b)De esas letras cuantas son vocales
def vocales(frase):
        contadorV = 0
        vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        frase = list(frase)

        for i in range(0, len(vocales)):
            for j in range(0, len(frase)):
                if frase[j] == vocales[i]:
                    contadorV += 1
        print(f"\tVocales: {contadorV}")


# c) Cuantas son consonantes
def consonantes(frase):
        contadorC = 0
        consonante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p',
        'q', 'r', 's', 't', 'v', 'w','x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'W','X', 'Y', 'Z']
        frase = list(frase)

        for i in range(0, len(consonante)):
            for j in range(0, len(frase)):
                if frase[j] == consonante[i]:
                    contadorC += 1
        print(f"\tConsonantes: {contadorC}")


# d) Cuantos espacios hay
def espacios(frase):
        contadorE = 0
        for i in frase:
            if i <= " ":
                contadorE += 1
        print(f"\tEspacios: {contadorE}")

# f) Construir el acronimo de dicha frase
def acronimo(frase):
        inicial = frase[0]
        for i in range(1, len(frase)):
                if frase[i - 1] ==  ' ':
                        inicial += frase[i]
        inicial = inicial.upper()
        print(f"\tAcronimo: {inicial}")


# g) Mostrar la frase invertida
def invertido(frase):
        frase = list(frase)
        frase.reverse()
        print("\tFrase invertida: ", end="")
        for i in range(0, len(frase)):
            invertido = frase[i]
            print(invertido, end="")
        print("")


# h) Contar cuantas palabras tiene la frase
def palabras(frase):
        import re
        contadorP = len(re.findall(r'\w+', frase))
        print(f"\tPalabras: {contadorP}")


palabra = input("Escribe algo:\n>>> ")

print("\nCONSTITUCIÓN DE LA FRASE:")
caracterDigitos(palabra)
vocales(palabra)
consonantes(palabra)
espacios(palabra)
acronimo(palabra)
invertido(palabra)
palabras(palabra)

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066