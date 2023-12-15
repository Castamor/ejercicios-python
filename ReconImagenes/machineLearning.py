# Importar libreria de la maquina de soporte vectorial
from sklearn import svm

# Creo una lista de vectores de caracteristicas con los valores de los dispositivos
X = [ [0,0,0], [1,0,0], [0,1,0], [1,1,0], [0,0,1], [1,0,1] ]

# Creo una lista de vectores de caracteristicas de etiqueta
Y = [ 0, 1, 1, 2, 10, 10 ]

# Creamos una instancia (objeto) de la maquina de soporte vectorial
modelo = svm.SVC()

# Entrenamos el modelo (Si se ejecuta el programa hasta este punto ya se estará entrenando)
modelo.fit(X, Y)

# Simular que recibimos datos
puerta = 1
ventana = 0
flama = 1

# Creamos una lista de entrada
carEntrada = [puerta, ventana, flama]

# Respuestas
res = modelo.predict([carEntrada])
print(f'\nRespuesta: {res[0]}\n')