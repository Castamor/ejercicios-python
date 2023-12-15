confirmacion = True
while confirmacion != False:
    opc = input("SELECCIONA UNA OPCIÓN DEL MENÚ:\n[1]Composición de una frase\n[2]Número a Morse\n[3]Promedio del atleta\n[4]Salir del programa\n>>> ")

    if opc == '1':
        print("=========== COMPOSICIÓN DE UNA FRASE ===========")
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
        print("")

    elif opc == '2':
        print("=========== NÚMERO A MORSE ===========")
        valores = ["-..-", "..-.", "..-", ".—", ".-..", "-..", "-.-.", "…-", "-.-", "—."]
        numero = []

        b = False
        while b == False :
            num = int(input("Teclea un numero de 1-4 dígitos:\n>>> "))
            c = len(str(num))
            if c <= 4 :
                for i in range(0, c):
                    uni = num%10
                    num /= 10
                    num = int(num)
                    numero.append(uni)
                b = True
                numero.reverse()
            else:
                print("El número que tecleaste no tiene de 1-4 dígitos. Intenta de nuevo\n")
        print("\nNúmero en Morse:")
        for i in range(0, c):
            x = numero[i]
            print(valores[x], end=" ")
        print("\n")

    elif opc == '3':
        print("=========== PROMEDIO DEL ATLETA ===========")
        import random

        array = []

        tiempo = 0 
        sumaA = 0           # A = semana
        sumaB = 0           # B = mes
        sumaC = 0           # C = año
        promedioA = 0
        promedioB = 0
        promedioC = 0

        # Generar números random y guardarlos en una lista
        while tiempo < 360:
                array.append(random.randint(58, 67))
                tiempo += 1
        tiempo = 0
        print("Se generaron los números aleatorios")

        # Semana
        print("\nPROMEDIO DE:")
        while tiempo < 7:
                sumaA += array[tiempo]
                tiempo += 1
                if tiempo == 6:
                        promedioA = sumaA / 7
                        print(f"\tSemana: {promedioA:.2f}")
        tiempo = 0

        # Mes
        while tiempo < 30:
                sumaB += array[tiempo]
                tiempo += 1
                if tiempo == 29:
                        promedioB = sumaB / 30
                        print(f"\tMes: {promedioB:.2f}")
        tiempo = 0

        # Año
        while tiempo < 360:
                sumaC += array[tiempo]
                tiempo += 1
                if tiempo == 359:
                        promedioC = sumaC / 360
                        print(f"\tAño: {promedioC:.2f}\n")
        tiempo = 0
        print("")

    elif opc == '4':
        print("\tSaliste del programa\n")
        confirmacion = False

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066