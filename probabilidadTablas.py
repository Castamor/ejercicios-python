import math
import os

numeros = []

def rango(numeros): R = max(numeros) - min(numeros); return R

def intervalo(n):
    K = 1 + 3.322 * math.log(n, 10)
    Ktemporal = math.floor(K)
    if Ktemporal%2 == 0:
        K += 1
        K = math.floor(K)
    else:
        K = math.floor(K)
    return K

def amplitud(R,K): A = R / K; A = math.ceil(A); return A


# -------------------------- Pedir valores ---------------------------
opc = None; i = 0
print("Presiona [t] para terminar de agregar números\nPresiona [e] para eliminar valor anterior")
while opc != 't':
    opc = input(f"{i+1}. "); opc = opc.lower()
    if opc == 'e': numeros.pop(); i -= 1
    if opc.isdigit(): numeros.append(int(opc)); i += 1
if opc == 't' and i == 0: exit() # Terminar el programa sin ingresar ningún valor
os.system("cls")
# --------------------------------------------------------------------


# -------------------------- Datos generales -------------------------
print(f"Datos originales:\n   {numeros}\n")

n = len(numeros) # Número total de datos
R = rango(numeros) # Rango
K = intervalo(n) # Intervalo: número de filas
A = amplitud(R,K) # Amplitud: crecimientos de la clase
print(f"Datos Generales:\n   (n) NumTotalDatos = {n}\n   (R) Rango = {R}\n   (K) Intervalo = {K}\n   (A) Amplitud = {A}\n")
#---------------------------------------------------------------------


# ------------------------------ Clases ------------------------------
clases = []
valores = [] 

minimo = min(numeros)
for i in range(0, K):

    if i == K-1: A += 1 # Si es la última iteración cuenta también al último dígito

    for j in range(0,A):
        valores.append(minimo + j)

    minimo = valores[-1] + 1
    clases.append(valores)
    valores = []

# Imprimir las clases
print("Clases:")
i = 0
for clase in clases:

    Li = min(clase)

    if i == len(clases)-1:
        Ls = max(clase)
    else:
        Ls = max(clase)+1
    i += 1

    print(f"   [{Li}-{Ls}]")
# --------------------------------------------------------------------


# ------------------------ Marca de Clase (X) ------------------------
marcasClase = []

i = 0
print(f"\n(X) Marcas de clase:")
for clase in clases:

    Li = min(clase)
    Ls = max(clase) if (i == len(clases)-1) else max(clase)+1
    i += 1
    
    X = (Li + Ls) / 2
    print(f"   [{Li}-{Ls}] = {X}")
    marcasClase.append(X)

# --------------------------------------------------------------------


# ------------ Frecuencia (f) y Total de F Acumulada (Ef) ------------
frecuencia = []
i = 0
contador = 0
frecuenciaAcumulada = 0

print("\n(f) Frecuencia:")
for clase in clases:

    Li = min(clase)
    Ls = max(clase) if (i == len(clases)-1) else max(clase)+1
    i += 1

    for valor in clase:
        contador += numeros.count(valor)
    
    frecuencia.append(contador)
    print(f"   [{Li}-{Ls}] = {contador}")
    frecuenciaAcumulada += contador
    contador = 0

print(f"[E,f] Total de f acumulada = {frecuenciaAcumulada}\n")
# --------------------------------------------------------------------


# -------------------- Frecuencia Acumulada (Fa) ---------------------
frecuenciaAcumulada = []
i = 0
contador = 0
contadorAcumulado = 0

print("(Fa) Frecuencia Acumulada:")
for clase in clases:

    Li = min(clase)
    Ls = max(clase) if (i == len(clases)-1) else max(clase)+1
    i += 1

    for valor in clase:
        contador += numeros.count(valor)

    contadorAcumulado += contador
    frecuenciaAcumulada.append(contadorAcumulado)
    print(f"   [{Li}-{Ls}] = {contadorAcumulado}")
    contador = 0
# --------------------------------------------------------------------


# --------------------- Frecuencia Relativa (fr) ---------------------
frecuenciaRelativa = []

j = 0
frAcumulada = 0
print("\n(fr) Frecuencia Relativa:")
for i in range(0, len(clases)):
    fr = frecuencia[i] / n
    frAcumulada += fr 
    frecuenciaRelativa.append(fr)

    Li = min(clases[j])
    Ls = max(clases[j]) if (j == len(clases)-1) else max(clases[j])+1

    print(f"   [{Li}-{Ls}] = {fr:.3f}")   
    j += 1

print(f"[E,fr] Suma total de fr = {frAcumulada:.2f}\n")
# --------------------------------------------------------------------


# ----------------------------- (X * f) ------------------------------
Xporf = []

j = 0
XporfAcumulado = 0
print("(X*f) Marca de clase * frecuencia:")

for i in range(0, len(clases)):
    producto = marcasClase[i] * frecuencia[i]
    XporfAcumulado += producto
    Xporf.append(producto)

    Li = min(clases[j])
    Ls = max(clases[j]) if (j == len(clases)-1) else max(clases[j])+1

    print(f"   [{Li}-{Ls}] = {producto}")    
    j += 1

print(f"[E,X*f] Suma total de X*f = {XporfAcumulado}\n")
# --------------------------------------------------------------------


# -------------- Media (~x), Mediana (Me) y Moda (^x) ----------------

media = XporfAcumulado / n

# Mediana
if n%2 == 0: datoMedio = n / 2  # Saber si n es
else: datoMedio = (n+1) / 2     # par o impar


i = 0
banderilla = False
for dato in frecuenciaAcumulada: # Buscar el dato en la tabla

    if datoMedio == dato:
        Ls = max(clases[i]) if (i == len(clases)-1) else max(clases[i])+1
        Me = Ls
        iteracion = i
        banderilla = True
        break

    i += 1

# Si no se encuentra, buscar através del número mayor más cercano
while banderilla == False:

    for i in range(0, len(frecuenciaAcumulada)):

        if datoMedio > frecuenciaAcumulada[max(i-1, 0)] and datoMedio < frecuenciaAcumulada[i]:
            iteracion = i
            Fa = frecuenciaAcumulada[i]
            banderilla = True
            break

Li = min(clases[iteracion])
Ls = max(clases[iteracion]) if (i == len(clases)-1) else max(clases[iteracion])+1
c = Ls - Li

Me = Li + (((datoMedio - frecuenciaAcumulada[max(iteracion-1, 0)]) / frecuencia[iteracion]) * c)

# Moda
datoMayor = max(frecuencia)

i = 0
iteracion = 0
for dato in frecuencia:
    if datoMayor == dato:
        iteracion = i
        f = frecuencia[i]
    i += 1

Li = min(clases[iteracion])
Ls = max(clases[iteracion]) if (i == len(clases)-1) else max(clases[iteracion])+1
c = Ls - Li

if iteracion+1 >= len(frecuencia):
    frecAcPost = 0
else:
    frecAcPost = frecuencia[iteracion+1]

Mo = Li + ((f - frecuencia[max(iteracion-1, 0)]) / ((f - frecuencia[max(iteracion-1, 0)]) + (f - frecAcPost)) * c)

print(f"(~x) Media = {media:.2f}\n(Me) Mediana = {Me:.2f}\n(^x) Moda = {Mo:.2f}\n")
# --------------------------------------------------------------------


# --------------------- Medidas de Dispersión  -----------------------
XmMaC = [] # X menos Media al Cuadrado

j = 0
XmMaCContador = 0 
print("(X-~x^2) X menos la Media al Cuadrado:")
for i in marcasClase:
    var = (i - media) ** 2
    XmMaCContador += var
    XmMaC.append(var)
    
    Li = min(clases[j])
    Ls = max(clases[j]) if (j == len(clases)-1) else max(clases[j])+1

    print(f"   [{Li}-{Ls}] = {var:.3f}")
    j += 1

# ss = XmMaCContador / n # Varianza
# s = math.sqrt(ss) # Desviación Estándar
# Cv = (s / media) * 100 # Coeficiente Relación

# print(f"[E,X-~x^2] Sumatoria XmMaC: {XmMaCContador:.3f}\n\n(s^2) Varianza: {ss:.3f}\n(s) Desviación Estándar: {s:.3f}\n(Cv) Coeficiente Relación: % {Cv:.3f}\n")