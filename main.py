def columna_llena(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for columna in range(1, columnas - 1):
        if all(matriz[fila][columna] != 0 for fila in range(filas)):
            # La columna está llena, ahora cuenta los 1 y 2
            contador_1 = sum(1 for fila in range(filas) if matriz[fila][columna] == 1)
            contador_2 = sum(1 for fila in range(filas) if matriz[fila][columna] == 2)
            
            return True, columna, contador_1, contador_2

    # Si no se encontró ninguna columna llena
    return False, None, None, None

# Ejemplo de uso

# hay_columna_llena, columna_llena, contador_1, contador_2 = columna_llena(matriz_ejemplo)

def contar_fichas_extremo_ganador(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    mitad_columnas = columnas // 2

    # Contar las fichas en las columnas específicas para el jugador 1
    fichas_jugador_1 = sum(matriz[fila][columna] == 1 for fila in range(filas) for columna in range(mitad_columnas, columnas))

    # Contar las fichas en las columnas específicas para el jugador 2
    fichas_jugador_2 = sum(matriz[fila][columna] == 2 for fila in range(filas) for columna in range(mitad_columnas))

    return fichas_jugador_1, fichas_jugador_2

# Ejemplo de uso
# matriz_ejemplo = [
#     [0, 0, 0, 1, 0, 0, 2, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0]
# ]

matriz_ejemplo = [
    [1, 2, 2, 2, 2, 2, 2, 2],
    [1, 0, 1, 0, 2, 0, 2, 2],
    [1, 0, 2, 0, 2, 0, 0, 2],
    [1, 0, 2, 0, 2, 0, 2, 2],
    [1, 0, 1, 0, 1, 0, 2, 2],
    [1, 1, 1, 1, 2, 1, 1, 2]
]

fichas_jugador_1, fichas_jugador_2 = contar_fichas_extremo_ganador(matriz_ejemplo)

# print(f"Fichas del Jugador 1 en el extremo ganador: {fichas_jugador_1}")
# print(f"Fichas del Jugador 2 en el extremo ganador: {fichas_jugador_2}")

def contar_fichas_en_columna(matriz, columna):
    filas = len(matriz)
    fichas_en_columna = sum(matriz[fila][columna] != 0 for fila in range(filas))
    return fichas_en_columna

# Ejemplo de uso
matriz_ejemplo = [
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0]
]

columna_deseada = 3  # Puedes cambiar este valor según la columna que desees verificar

fichas_en_columna = contar_fichas_en_columna(matriz_ejemplo, columna_deseada)

# print(f"En la columna {columna_deseada} hay {fichas_en_columna} fichas.")

def juego_terminado(matriz):
    filas = len(matriz)

    # Verificar si todas las fichas del jugador 1 están en las columnas 4, 5, 6, 7
    fichas_jugador_1 = sum(matriz[fila][columna] == 1 for fila in range(filas) for columna in range(4, 8)) == 12

    # Verificar si todas las fichas del jugador 2 están en las columnas 0, 1, 2, 3
    fichas_jugador_2 = sum(matriz[fila][columna] == 2 for fila in range(filas) for columna in range(4)) == 12

    return fichas_jugador_1 and fichas_jugador_2

# Ejemplo de uso

matriz_ejemplo_no_terminado = [
    [0, 0, 2, 2, 0, 1, 1, 0],
    [0, 0, 2, 2, 0, 1, 1, 0],
    [0, 0, 2, 2, 0, 1, 1, 0],
    [0, 0, 2, 2, 0, 1, 1, 0],
    [0, 0, 2, 2, 0, 1, 1, 0],
    [0, 0, 2, 2, 0, 1, 1, 0]
]

# if juego_terminado(matriz_ejemplo_terminado):
#     print("El juego ha terminado.")
# else:
#     print("El juego no ha terminado.")

# if juego_terminado(matriz_ejemplo_no_terminado):
#     print("El juego ha terminado.")
# else:
#     print("El juego no ha terminado.")


def modificar_matriz_lista(matriz, lista_coordenadas):
    matrices_modificadas = []

    for coordenada in lista_coordenadas:
        fila, columna = coordenada
        matriz_modificada = [fila.copy() for fila in matriz]
        matriz_modificada[fila][columna] = 2
        matrices_modificadas.append(matriz_modificada)

    return matrices_modificadas

# Ejemplo de uso
matriz_original = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# lista_coordenadas = [[0, 1], [2, 0], [1, 2]]

# matrices_resultantes = modificar_matriz_lista(matriz_original, lista_coordenadas)

# # Imprimir las matrices resultantes
# for i, matriz in enumerate(matrices_resultantes):
#     print(f"Matriz Resultante {i + 1}:")
#     for fila in matriz:
#         print(fila)
#     print()
    
    
# def minimax(nodo, profundidad, es_maximizando):
#     if profundidad == 0 o nodo es un nodo terminal:
#         return evaluar(nodo)
    
#     if es_maximizando:
#         mejor_valor = menos_infinito
#         for hijo in generar_hijos(nodo):
#             valor = minimax(hijo, profundidad - 1, False)
#             mejor_valor = max(mejor_valor, valor)
#         return mejor_valor
#     else:
#         mejor_valor = infinito
#         for hijo in generar_hijos(nodo):
#             valor = minimax(hijo, profundidad - 1, True)
#             mejor_valor = min(mejor_valor, valor)
#         return mejor_valor

def obtener_coordenadas(matriz):
    coordenadas_1 = []
    coordenadas_2 = []

    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == 1:
                coordenadas_1.append((fila, columna))
            elif matriz[fila][columna] == 2:
                coordenadas_2.append((fila, columna))

    return coordenadas_1, coordenadas_2

# Ejemplo de uso
matriz_ejemplo = [
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 2, 0]
]

coordenadas_1, coordenadas_2 = obtener_coordenadas(matriz_ejemplo)

# print("Coordenadas del número 1:", coordenadas_1)
# print("Coordenadas del número 2:", coordenadas_2)



def encontrar_movimiento(original, modificada):
    filas = len(original)
    columnas = len(original[0])

    for fila in range(filas):
        for columna in range(columnas):
            if original[fila][columna] != modificada[fila][columna]:
                origen = (fila, columna)
                destino = None

                # Buscar el destino de la ficha en la matriz modificada
                for i in range(filas):
                    for j in range(columnas):
                        if original[fila][columna] == modificada[i][j]:
                            destino = (i, j)
                            break

                return origen, destino

    # Si no se encontraron movimientos
    return None, None

# Ejemplo de uso
matriz_original = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0]
]

matriz_modificada = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 0, 0, 0]
]

origen, destino = encontrar_movimiento(matriz_original, matriz_modificada)

if origen is not None and destino is not None:
    print(f"La ficha en la posición {origen} se movió a la posición {destino}")
else:
    print("No se encontraron movimientos")





    