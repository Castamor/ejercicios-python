hd = 25 # Hotdogs
h = 45 # Hamburguesa
r = 15 # Refresco
total = 0

Chd = 0 # Contador hotdogs
Ch = 0 # Contador hamburguesas
Cr = 0 # Contador refresco
totalFinal = 0

clientes = 0
menu = 0
pedido = 0

while menu != 2:
    menu = int(input("\n¿QUE DESEAS HACER?\n[1] Pedir algo\n[2] Terminar día de trabajo\n>>> "))

    if menu == 1:
        while pedido != 4:
            print(f"======= Cliente {clientes + 1} =======")
            pedido = int(input("SELECCIONA UNA OPCIÓN DEL MENÚ:\n[1]HotDog: $25mxn\n[2]Hamburguesa: $45mxn\n[3]Refresco: $15mxn\n[4]Ya no deseo pedir\n>>> "))

            if pedido == 1:
                print("\n\tPediste un HOTDOG\n")
                total += 25
                Chd += 1

            if pedido == 2:
                print("\n\tPediste una HAMBURGUESA\n")
                total += 45
                Ch += 1

            if pedido == 3:
                print("\n\tPediste un REFRESCO\n")
                total += 15
                Cr += 1

        print(f"\n\tCLIENTE {clientes + 1}: Consumiste ${total}mxn en total.")
        totalFinal += total; total = 0
        pedido = 0
        clientes += 1

print("\n====== TERMINASTE EL DÍA DE TRABAJO ======")
print(f"Clientes atentidos: {clientes + 1}\nVendiste:\n·{Chd} Hotdogs\n·{Ch} Hamburguesas\n·{Cr} Refrescos\nGeneraste ${totalFinal} mxn al finalizar el día\n")

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066