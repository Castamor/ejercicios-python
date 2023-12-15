valores = ["-..-", "..-.", "..-", ".-", ".-..", "-..", "-.-.", "…-", "-.-", "-."]
numero = []

b = False
while b == False :
    num = int(input("Teclea un numero de 1-4 dígitos:\n>>> "))
    c = len(str(num))
    if c >= 1 and c <= 4 :
        for i in range(0, c):
            uni = num%10
            num /= 10
            num = int(num)
            numero.append(uni)
        b = True
        numero.reverse()
    else:
        print("El número que tecleaste no tiene de 1-4 dígitos. Intenta de nuevo\n")

print("Número en Morse:")
for i in range(0, c):
    x = numero[i]
    print(valores[x], end=" ")

# Castellanos Moreno José Ángel  01-ISOF #: 21050066