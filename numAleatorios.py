import random

# Función que simula el lanzamiento de un dado
def lanzar_dado():
    return random.randint(1, 6)

# Función que simula una ronda del juego de dados
def jugar_ronda(jugador):
    input(f"  Jugador {jugador}, presiona Enter para lanzar los dados...")
    dado1 = lanzar_dado()
    dado2 = lanzar_dado()
    total = dado1 + dado2
    print(f"  Lanzaste {dado1} y {dado2}. Total de puntos: {total}.\n")
    return total

# Función que determina el ganador del juego de dados
def determinar_ganador(puntajes):
    max_puntaje = max(puntajes)
    ganadores = [i+1 for i, j in enumerate(puntajes) if j == max_puntaje]
    if len(ganadores) == 1:
        print(f"\nEl jugador {ganadores[0]} es el ganador con {max_puntaje} puntos!\n")
    else:
        print(f"\n¡Empate entre los jugadores, con un total de {max_puntaje} puntos cada uno!")

# Función principal que ejecuta el juego de dados
def jugar_dados(num_jugadores):
    puntajes = [0] * num_jugadores
    for ronda in range(1, 4): # Número de Rondas
        print(f"RONDA {ronda}:")
        for jugador in range(num_jugadores):
            puntajes[jugador] += jugar_ronda(jugador+1)
    print("\nRESULTADOS FINALES:")
    for jugador, puntaje in enumerate(puntajes):
        print(f"Jugador {jugador+1}: {puntaje} puntos")
    determinar_ganador(puntajes)

# Ejemplo de uso
jugar_dados(2)