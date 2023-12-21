import copy

class Ficha:
    def __init__(self, pocision):
        self.pocision = []
        self.posiblesMovimientos = []
        
class Juego:
    def __init__(self, estado, fichas_rojas, fichas_negras):
        self.estadoInicial = estado
        self.rojas = fichas_rojas
        self.negras = fichas_negras
        self.turno = "negro"
        self.movimientos = 1
        self.jugada = 1
        
# turno = "negro"
        
def posibles_movimientos_negro(matriz, cantidad_movimientos, ficha_pocision):
    movimientos = []
    i = ficha_pocision[0]
    j = ficha_pocision[1]
    
    if cantidad_movimientos >= 1:
        if j - cantidad_movimientos > 0:
            if matriz[i][j - cantidad_movimientos] == 0:
                movimientos.append([i, j - cantidad_movimientos])
                if i - 1 > 0 and matriz[i - 1][j - cantidad_movimientos] == 0:
                    movimientos.append([i - 1, j - cantidad_movimientos])
                if i + 1 < len(matriz[0]) and matriz[i + 1][j - cantidad_movimientos] == 0:
                    movimientos.append([i + 1, j - cantidad_movimientos])
        else: 
            return movimientos
        
    if cantidad_movimientos >= 2:
        if i - 2 > 0 and matriz[i - 2][j - cantidad_movimientos] == 0:
            movimientos.append([i - 2, j - cantidad_movimientos])
        if i + 2 < len(matriz) and matriz[i + 2][j - cantidad_movimientos] == 0:
            movimientos.append([i + 2, j - cantidad_movimientos])
            
    if cantidad_movimientos >= 3:
        if i - 3 > 0 and matriz[i - 3][j - cantidad_movimientos] == 0:
            movimientos.append([i - 3, j - cantidad_movimientos])
        if i + 3 < len(matriz) and matriz[i + 3][j - cantidad_movimientos] == 0:
            movimientos.append([i + 3, j - cantidad_movimientos])
            
    return movimientos

def posibles_movimientos_rojo(matriz, cantidad_movimientos, ficha_pocision):
    movimientos = []
    i = ficha_pocision[0]
    j = ficha_pocision[1]
    
    if cantidad_movimientos >= 1:
        if j + cantidad_movimientos > 0:
            if matriz[i][j + cantidad_movimientos] == 0:
                movimientos.append([i, j + cantidad_movimientos])
                if i - 1 > 0 and matriz[i - 1][j + cantidad_movimientos] == 0:
                    movimientos.append([i - 1, j + cantidad_movimientos])
                if i + 1 < len(matriz[0]) and matriz[i + 1][j + cantidad_movimientos] == 0:
                    movimientos.append([i + 1, j + cantidad_movimientos])
        else: 
            return movimientos
        
    if cantidad_movimientos >= 2:
        if i - 2 > 0 and matriz[i - 2][j + cantidad_movimientos] == 0:
            movimientos.append([i - 2, j + cantidad_movimientos])
        if i + 2 < len(matriz[0]) and matriz[i + 2][j + cantidad_movimientos] == 0:
            movimientos.append([i + 2, j + cantidad_movimientos])
            
    if cantidad_movimientos >= 3:
        if i - 3 > 0 and matriz[i - 3][j + cantidad_movimientos] == 0:
            movimientos.append([i - 3, j + cantidad_movimientos])
        if i + 3 < len(matriz[0]) and matriz[i + 3][j + cantidad_movimientos] == 0:
            movimientos.append([i + 3, j + cantidad_movimientos])
            
    return movimientos

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
    
    
def contar_fichas_en_columna(matriz, columna):
    filas = len(matriz)
    fichas_en_columna = sum(matriz[fila][columna] != 0 for fila in range(filas))
    return fichas_en_columna
    
# def generar_estados(juego):
#     lista_aplanada = []
#     matrices_modificadas = []
    
#     if juego.turno == "negro":
#         lista_anidada = []
#         for posicion in juego.negras:
#             estados = posibles_movimientos_negro(juego.estadoInicial, juego.movimientos, posicion)
#             lista_anidada.append(estados)
#         lista_aplanada = [sublista for lista_externa in lista_anidada for sublista in lista_externa]
        
#         for coordenada in lista_aplanada:
#             fila, columna = coordenada
#             matriz_modificada = [fila.copy() for fila in juego.estadoInicial]
#             matriz_modificada[fila][columna] = 2
#             coordenada_1, coordenada_2 = obtener_coordenadas(matriz_modificada)
#             nuevoEstadoJuego = Juego(matriz_modificada, coordenada_1, coordenada_2)
#             fichas_en_columna = contar_fichas_en_columna(matriz_modificada, columna)
        
#         if fichas_en_columna - 1 > 0 and juego.jugada == 1:
#             juego.turno = "negro"
#             juego.jugada = 2
#         else:
#             juego.turno = "rojo"
            
#         matrices_modificadas.append(nuevoEstadoJuego)
#     else:
#         lista_anidada = []
#         for posicion in juego.rojas:
#             estados = posibles_movimientos_rojo(juego.estadoInicial, juego.movimientos, posicion)
#             lista_anidada.append(estados)
#         lista_aplanada = [sublista for lista_externa in lista_anidada for sublista in lista_externa]
        
#         for coordenada in lista_aplanada:
#             fila, columna = coordenada
#             matriz_modificada = [fila.copy() for fila in juego.estadoInicial]
#             matriz_modificada[fila][columna] = 1
#             coordenada_1, coordenada_2 = obtener_coordenadas(matriz_modificada)
#             nuevoEstadoJuego = Juego(matriz_modificada, coordenada_1, coordenada_2)
#             fichas_en_columna = contar_fichas_en_columna(matriz_modificada, columna)
            
#             if fichas_en_columna - 1 > 0 and juego.jugada == 1:
#                 juego.turno = "negro"
#                 juego.jugada = 2
#             else:
#                 juego.turno = "rojo"
                
#             matrices_modificadas.append(nuevoEstadoJuego)

#     return matrices_modificadas

def generar_estados(juego):
    lista_aplanada = []
    matrices_modificadas = []
    
    if juego.turno == "negro":
        # lista_anidada = []
        for posicion in juego.negras:
            estados = posibles_movimientos_negro(juego.estadoInicial, juego.movimientos, posicion)
    
            for coordenada in estados:
                fila, columna = coordenada
                matriz_modificada = [fila.copy() for fila in juego.estadoInicial]
                matriz_modificada[fila][columna] = 2
                matriz_modificada[posicion[0]][posicion[1]] = 0
                coordenada_1, coordenada_2 = obtener_coordenadas(matriz_modificada)
                
                nuevoEstadoJuego = Juego(matriz_modificada, coordenada_1, coordenada_2)
                fichas_en_columna = contar_fichas_en_columna(matriz_modificada, columna)
                nuevoEstadoJuego.movimientos = fichas_en_columna - 1
            
                if nuevoEstadoJuego.movimientos > 0 and juego.jugada == 1:
                    juego.turno = "negro"
                    juego.jugada = 2
                else:
                    juego.turno = "rojo"
                    
                matrices_modificadas.append(nuevoEstadoJuego)
    else:
        # lista_anidada = []
        for posicion in juego.rojas:
            estados = posibles_movimientos_rojo(juego.estadoInicial, juego.movimientos, posicion)
        
            for coordenada in estados:
                fila, columna = coordenada
                matriz_modificada = [fila.copy() for fila in juego.estadoInicial]
                matriz_modificada[fila][columna] = 1
                matriz_modificada[posicion[0]][posicion[1]] = 0
                coordenada_1, coordenada_2 = obtener_coordenadas(matriz_modificada)
                
                nuevoEstadoJuego = Juego(matriz_modificada, coordenada_1, coordenada_2)
                fichas_en_columna = contar_fichas_en_columna(matriz_modificada, columna)
                nuevoEstadoJuego.movimientos = fichas_en_columna - 1
                # print(nuevoEstadoJuego.movimientos)
                
                if fichas_en_columna > 0 and juego.jugada == 1:
                    juego.turno = "negro"
                    juego.jugada = 2
                else:
                    juego.turno = "rojo"
                    
                matrices_modificadas.append(nuevoEstadoJuego)
    
    # lista_aplanada = [sublista for lista_externa in matrices_modificadas for sublista in lista_externa]

    return matrices_modificadas

def hayBloqueos(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for columna in range(1, columnas - 1):
        if all(matriz[fila][columna] != 0 for fila in range(filas)):
            # La columna está llena, ahora cuenta los 1 y 2
            contador_1 = sum(1 for fila in range(filas) if matriz[fila][columna] == 1)
            contador_2 = sum(1 for fila in range(filas) if matriz[fila][columna] == 2)
            
            return True, contador_1, contador_2

    # Si no se encontró ninguna columna llena
    return False, None, None

def contar_fichas_extremo_ganador(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    mitad_columnas = columnas // 2

    # Contar las fichas en las columnas específicas para el jugador 1
    fichas_jugador_1 = sum(matriz[fila][columna] == 1 for fila in range(filas) for columna in range(mitad_columnas, columnas))

    # Contar las fichas en las columnas específicas para el jugador 2
    fichas_jugador_2 = sum(matriz[fila][columna] == 2 for fila in range(filas) for columna in range(mitad_columnas))

    return fichas_jugador_1, fichas_jugador_2


def juego_terminado(matriz):
    filas = len(matriz)

    # Verificar si todas las fichas del jugador 1 están en las columnas 4, 5, 6, 7
    fichas_jugador_1 = sum(matriz[fila][columna] == 1 for fila in range(filas) for columna in range(4, 8)) == 12

    # Verificar si todas las fichas del jugador 2 están en las columnas 0, 1, 2, 3
    fichas_jugador_2 = sum(matriz[fila][columna] == 2 for fila in range(filas) for columna in range(4)) == 12

    return fichas_jugador_1 and fichas_jugador_2

def evaluar_estado(estado):
    puntuacion = 0
    
    hay_columna_llena, contador_1, contador_2 = hayBloqueos(estado)
    if hay_columna_llena:
        if contador_2 > contador_1:
            puntuacion += 1
        else:
            puntuacion -=1
    else:
        puntuacion += 2
    
    fichas_jugador_1, fichas_jugador_2 = contar_fichas_extremo_ganador(estado)
    if fichas_jugador_1 > fichas_jugador_2:
        puntuacion -= 2
    if fichas_jugador_1 < fichas_jugador_2:
        puntuacion += 2
    else:
        puntuacion += 1
        
    return puntuacion

def minimax(juego, profundidad, es_maximizando):
    if profundidad == 0 or juego_terminado(juego.estadoInicial):
        return evaluar_estado(juego.estadoInicial), None
    
    if es_maximizando:
        mejor_valor = float('-inf')
        mejor_jugada = None
        estados = generar_estados(juego)
        for hijo in estados:
            valor, _ = minimax(hijo, profundidad - 1, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_jugada = hijo
        return mejor_valor, mejor_jugada
    else:
        mejor_valor = float('inf')
        mejor_jugada = None
        estados = generar_estados(juego)
        for hijo in estados:
            valor, _ = minimax(hijo, profundidad - 1, True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_jugada = hijo
        return mejor_valor, mejor_jugada

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

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  # end=" " evita que se añada una nueva línea después de cada fila
        print()  # Agrega una nueva línea después de cada fila

def limaGame(juego):
    _, mejor_juego = minimax(juego, 3, True)
    
    imprimir_matriz(mejor_juego.estadoInicial)
    
    origen, destino = encontrar_movimiento(juego.estadoInicial, mejor_juego.estadoInicial)
    
    return origen, destino

matriz_ejemplo = [
    [1, 2, 2, 2, 2, 2, 2, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 2]
]

coordenada_1, coordenada_2 = obtener_coordenadas(matriz_ejemplo)

inicioJuego = Juego(matriz_ejemplo, coordenada_1, coordenada_2)

origen, destino = limaGame(inicioJuego)

print(origen, destino)

        

    
        
    
    
        
                
        
                    
        
