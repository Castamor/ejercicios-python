while True: 
    
    op = int(input("¿Qué opción quieres realizar?\n[1]Circulo\n[2]Rectángulo\n[3]Cuadrado\nRespuesta: "))

    if op == 1:
        pi = 3.1416
        radio = int(input("\nTeclea el RADIO del Circulo: "))
        areaC = pi*(radio**2)
        print("El área del circulo es: ")
        print(areaC)

    elif op == 2:
        base= int(input("\nTeclea la BASE del Rectángulo: "))
        alt= int(input("Teclea la ALTURA del Rectángulo: "))
        areaR= base*alt
        print("El área del rectángulo es: ")
        print(areaR)

    elif op == 3:
        lado= int(input("\nTeclea el valor de un LADO del Cuadrado: "))
        areaCUA= lado**2
        print("El área del cuadrado es: ")
        print(areaCUA)
        
    else:
        print("\nValor incorrecto")

    salir= input("\n¿Deseas salir del programa? \n[Y]es\n[N]o\n>>> ")

    if salir == 'y':
        print("\nSALISTE DEL PROGRAMA")
        break;

#Castellanos Moreno