# import random
import pygame
import sys
import linjaGame as lb

WIDTH = 700
HEIGHT = 480

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def mostrar_mensaje(screen, mensaje, posicion):
    color = (255, 255, 255)  # Color blanco
    font = pygame.font.Font(None, 28)
    text = font.render(mensaje, True, color)
    screen.blit(text, posicion)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("EL JUEGO DE LINJA")

    black_circle_positions = []
    red_circle_positions = []
    # black_circle_positions = [[155, 100], [225, 100], [295, 100], [295, 190], [295, 145], [155, 145], [155, 190], [155, 235], [155, 280], [155, 325], [225, 145], [225, 190]]
    # red_circle_positions = [[365, 235], [365, 190], [365, 145], [505, 280], [365, 325], [435, 325], [505, 325], [435, 145], [435, 190], [435, 235], [435, 280], [365, 280]]
    
    coordinates = [[85, 100], [155, 100], [225, 100], [295, 100], [365, 100], [435, 100], [505, 100], [575,100], [85, 145], [155, 145], [225, 145], [295, 145], [365, 145], [435, 145], [505, 145], [575, 145], [85, 190], [155, 190], [225, 190], [295, 190], [365, 190], [435, 190], [505, 190], [575, 190], [85, 235], [155, 235], [225, 235], [295, 235], [365, 235], [435, 235], [505, 235], [575, 235], [85, 280], [155, 280], [225, 280], [295, 280], [365, 280], [435, 280], [505, 280], [575, 280],[85, 325], [155, 325], [225, 325], [295, 325], [365, 325], [435, 325], [505, 325], [575, 325]]
    posicion_utilidad = [[85, 370], [155, 370], [225, 370], [295, 370], [365, 370], [435, 370], [505, 370], [575, 370]]
    
    # Convertir a matriz de 8x6 las coordenadas permitidas
    matrix = [coordinates[i:i + 8] for i in range(0, len(coordinates), 8)]
    selected_circle = None
    
    # Crear una nueva matriz con ceros
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    def convertir_matrix(black_circle_positions, red_circle_positions):
        # Colocar las coordenadas de black_circle_positions en la nueva matriz
        for coord in black_circle_positions:
            for i, fila in enumerate(matrix):
                if coord in fila:
                    j = fila.index(coord)
                    new_matrix[i][j] = 2  # Puedes usar cualquier valor que desees, aquí he usado 1 como ejemplo

        # Colocar las coordenadas de red_circle_positions en la nueva matriz
        for coord in red_circle_positions:
            for i, fila in enumerate(matrix):
                if coord in fila:
                    j = fila.index(coord)
                    new_matrix[i][j] = 1  # Puedes usar cualquier valor que desees, aquí he usado 2 como ejemplo
        
        return new_matrix
        # Imprimir la nueva matriz
        # for fila in new_matrix:
        #     print(fila)
        
    #Agregar las posiciones de los círculos negros horizontalmente
    for x in range(155, 575 + 1, 70):
        black_circle_positions.append([x, 100])

    # Agregar las posiciones de los círculos negros verticalmente
    for y in range(145, 325 + 1, 45):
        black_circle_positions.append([575, y])

    # Agregar las posiciones de los círculos rojos horizontalmente
    for x in range(85, 505 + 1, 70):
        red_circle_positions.append([x, 325])

    # Agregar las posiciones de los círculos rojos verticalmente
    for y in range(100, 280 + 1, 45):
        red_circle_positions.append([85, y])

    
    def board(black_circle_positions, red_circle_positions, arr_cant_fichas):
        fondo = pygame.image.load("tablero.png").convert()
        screen.blit(fondo, (0, 0))
        
        color_ficha = ""
        
        #pinta los circulos
        for pos in black_circle_positions:
            pygame.draw.circle(screen, BLACK, pos, 15)
        for pos in red_circle_positions:
            pygame.draw.circle(screen, RED, pos, 15)
            
        if selected_circle in black_circle_positions:
            color_ficha = "Negra"
        elif selected_circle in red_circle_positions:
            color_ficha = "Roja"
        else:
            color_ficha = "/"
        # Mensaje ficha seleccionada
        mensaje = "Ficha "+color_ficha+" seleccionada"
        posicion_mensaje = (10, 10)  
        mostrar_mensaje(screen, mensaje, posicion_mensaje)
        
        #mensaje cantidad de fichas en cada columna
        for item in range(8): 
            mensaje = str(arr_cant_fichas[item])
            posicion_mensaje = posicion_utilidad[item]  
            mostrar_mensaje(screen, mensaje, posicion_mensaje)
    
    #verifica si el juego termina
    def termina(black_circle_positions, red_circle_positions):
        cant_fichas_negras = 0
        #comprobar si termina el juego
        num_filas = len(matrix)
        num_columnas = len(matrix[0]) if num_filas > 0 else 0
        
        for col_index in range(num_columnas):
            for fila_index in range(num_filas):
                item = matrix[fila_index][col_index]
                if item in black_circle_positions:
                    cant_fichas_negras += 1
                elif item in red_circle_positions:
                    cant_fichas_negras = 0
            if cant_fichas_negras == 12:
                return True
        if cant_fichas_negras != 12:
            return False
        
    def suma_columna(black_circle_positions, red_circle_positions):
        arr_cant_fichas = [0] * 8 #lista que almacena la cantidad de fichas en cada columna
        #contar y sumar la cantidad de fichas en cada columna
        num_filas = len(matrix)
        num_columnas = len(matrix[0]) if num_filas > 0 else 0
        
        # Recorrer la matriz por columnas
        for col_index in range(num_columnas):
            cant_fichas = 0
            for fila_index in range(num_filas):
                item = matrix[fila_index][col_index]
                if item in black_circle_positions:
                    cant_fichas += 1
                elif item in red_circle_positions:
                    cant_fichas += 1
                
            arr_cant_fichas[col_index] = cant_fichas
        return arr_cant_fichas   
    
    def contar_movimientos_rojo(matrix, selected_circle, black_circle_positions, red_circle_positions):
        cant_movimientos = 0
        columna = 0
        for fila in matrix:
            if selected_circle in fila:
                columna = fila.index(selected_circle)
                # columna_encontrada.append(fila.index(selected_circle))
                break  # Detenemos la búsqueda si se encuentra la coordenada
        utilidad.append(suma_columna(black_circle_positions, red_circle_positions))
        cant_movimientos = utilidad[0][columna] - 1
            # cant_movimientos.append(utilidad[0][columna] - 1)
        selected_circle = None 
        return cant_movimientos, columna
    
    def contar_movimientos_negro(matrix, black_circle_positions, red_circle_positions):
        cant_movimientos = 0
        columna = 0
        for fila in matrix:
            if ficha_negra_aleatoria in fila:
                columna = fila.index(ficha_negra_aleatoria)
                # columna_encontrada.append(fila.index(ficha_negra_aleatoria))
                break  # Detenemos la búsqueda si se encuentra la coordenada
        utilidad.append(suma_columna(black_circle_positions, red_circle_positions))
        cant_movimientos = utilidad[0][columna] - 1
        # cant_movimientos.append(utilidad[0][columna] - 1)
        return cant_movimientos, columna
        
    
    turno_maquina = False
    
    columna_encontrada = [] #array para almacenar la columna donde se mueve la ficha
    utilidad = [] #array para almacenar los valores de cada columna o cuantas fichas hay para determinar el siguiente movimiento
    cant_mov = 0
    turno = 1
    # columna = 0 
    segundo_movimiento = []
    ficha_negra_aleatoria = []
    while True:
        print(turno)
        if turno_maquina == False:
            # print("turno humano")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    print("CLIC")
                   
                   #aqui guardo ficha seleccionada
                    mouse_pos = pygame.mouse.get_pos()
                    if selected_circle is None:
                        for pos in red_circle_positions:
                            if pos[0] - 15 < mouse_pos[0] < pos[0] + 15 and pos[1] - 15 < mouse_pos[1] < pos[1] + 15:    
                                selected_circle = pos
                                
                    else:
                       
                        # Verifica si la nueva posición está ocupada
                        collision = False
                        for item in black_circle_positions + red_circle_positions:
                            if item[0] - 15 < mouse_pos[0] < item[0] + 15 and item[1] - 15 < mouse_pos[1] < item[1] + 15:
                                collision = True
                                break     
                        
                        # Si no hay colisión, mueve el círculo
                        if not collision:        
                            for fila in matrix:
                                for item in fila:
                                    if item[0] - 15 < mouse_pos[0] < item[0] + 15 and item[1] - 15 < mouse_pos[1] < item[1] + 15:
                                        turno += 1
                                        segundo_movimiento.append(selected_circle.copy())
                                        
                                        print(red_circle_positions[0])
                                        selected_circle[0], selected_circle[1] = item
                                        print(red_circle_positions[0])
                                        
                                        cant_movimientos, columna = contar_movimientos_rojo(matrix, selected_circle, black_circle_positions, red_circle_positions)
                                        # print(cant_movimientos, columna)
                                        
                                        if turno == 1 and cant_movimientos > 0:
                                            # cant_mov = cant_movimientos
                                            turno = 2
                                            turno_maquina = False
                                        else:
                                            turno = 1
                                            turno_maquina = True
                                        # print("turno: ",turno)
                                        # if turno == 1:
                                        #     if segundo_movimiento[0][0] - 15 < mouse_pos[0] < segundo_movimiento[0][0] + 15 and segundo_movimiento[0][1] - 15 < mouse_pos[1] < segundo_movimiento[0][1] + 15:
                                        #         selected_circle[0], selected_circle[1] = item
                                        # if turno == 2:
                                        #     if segundo_movimiento[1][0] - 15 < mouse_pos[0] < segundo_movimiento[1][0] + 15 and segundo_movimiento[1][1] - 15 < mouse_pos[1] < segundo_movimiento[1][1] + 15:
                                        #         selected_circle[0], selected_circle[1] = item
                                        #     else:
                                        #         print("seleccione la ficha")
                                
                            #verificar en qué columna está el circulo movido
                            # for fila in matrix:
                            #     if selected_circle in fila:
                            #         columna = fila.index(selected_circle)
                            #         # columna_encontrada.append(fila.index(selected_circle))
                            #         break  # Detenemos la búsqueda si se encuentra la coordenada
                            # utilidad.append(suma_columna(black_circle_positions, red_circle_positions))
                            # cant_movimientos = utilidad[0][columna] - 1
                            # # cant_movimientos.append(utilidad[0][columna] - 1)
                            # selected_circle = None
                            
                            # print("cant_movimientos antes: ",cant_movimientos[0])
                            # if cant_movimientos[0] == 0:
                            #     turno_maquina = True
                            #     columna_encontrada = [] 
                            #     utilidad = [] 
                            #     cant_movimientos = []
                            #     segundo_movimiento = []
                            # else:
                            #     cant_movimientos[0] -= 1
                            # print(cant_movimientos)
                            # print("cant_movimientos diponibles humano: ",cant_movimientos[0])
                            # print("segundo_mov: ", segundo_movimiento)
        
        
        if turno_maquina:
            
            
            matriz_ejemplo = convertir_matrix(black_circle_positions, red_circle_positions)
            
            coordenada_1, coordenada_2 = lb.obtener_coordenadas(matriz_ejemplo)
            
            inicioJuego = lb.Juego(matriz_ejemplo, coordenada_1, coordenada_2)
            
            origen, destino = lb.linjaGame(inicioJuego)
            # # print("turno maquina")
            # ficha_negra_aleatoria.append(origen)
            coordenada_aleatoria = destino
            if coordenada_aleatoria not in black_circle_positions + red_circle_positions:
                origen[0], origen[1] = coordenada_aleatoria
            
            cant_movimientos, columna = contar_movimientos_negro(matrix, black_circle_positions, red_circle_positions)
            
            if turno == 1 and cant_movimientos > 0:
                # cant_mov = cant_movimientos
                turno = 2
                turno_maquina = True
            else:
                turno = 1
                turno_maquina = False
            #     #verificar en qué columna está el circulo movido
            #     for fila in matrix:
            #         if ficha_negra_aleatoria in fila:
            #             columna_encontrada.append(fila.index(ficha_negra_aleatoria))
            #             break  # Detenemos la búsqueda si se encuentra la coordenada
            #     utilidad.append(suma_columna(black_circle_positions, red_circle_positions))
                
            #     cant_movimientos.append(utilidad[0][columna_encontrada[0]] - 1)
            #     print("cantidad movimientos maquina: ",cant_movimientos[0])  
                
            #     if cant_movimientos[0] == 0:
            #         turno_maquina = False
            #         columna_encontrada = [] 
            #         utilidad = [] 
            #         cant_movimientos = []  
            #         segundo_movimiento = []
            #         ficha_negra_aleatoria = []
            #     else:
            #         cant_movimientos[0] -= 1
            # print("ficha negra: ",ficha_negra_aleatoria)
            
            
        cant_fichas = suma_columna(black_circle_positions, red_circle_positions)
        
        termina(black_circle_positions, red_circle_positions)
        
        board(black_circle_positions, red_circle_positions, cant_fichas)

        # convertir_matrix(black_circle_positions, red_circle_positions)
        
        # Controlar la velocidad de actualización
        pygame.time.Clock().tick(5)
        
        #actualiza
        pygame.display.flip()
        
        
        

if __name__ == "__main__":
    main()
