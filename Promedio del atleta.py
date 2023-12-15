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

# Castellanos Moreno José Ángel  01-ISOF  #: 21050066