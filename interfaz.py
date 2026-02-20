import pygame
import copy
from logica_juego import tablero_de_inicio, ciclo_de_la_vida, posicion_valida
pygame.init()

# --- Configuración ---
ancho, alto = 1000, 800
grid_x, grid_y = 100, 80
dimAncho = 10
dimAlto = 9
desplazamiento_del_tablero = 80
fps = 10
boton1_x = (ancho - 150) // 2
boton1_y = 10
boton_ancho = 150
boton1_alto = 50
boton1_color = (0, 0, 255)
fuente_boton1 = pygame.font.Font(None, 36)
fuente_controles = pygame.font.Font(None, 18)
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Vida de Conway")
clock = pygame.time.Clock()
copia_tablero = None
copia_de_pausado = None

# --- Estado inicial ---
tablero = tablero_de_inicio(grid_y, grid_x)
pausado = True


# --- Función de dibujo ---
def dibujar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            color = (255, 255, 255) if tablero[i][j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * dimAncho, i * dimAlto+desplazamiento_del_tablero, dimAncho, dimAlto))
            pygame.draw.rect(screen, (50, 50, 50), (j * dimAncho, i * dimAlto+desplazamiento_del_tablero, dimAncho, dimAlto), 1)


def dibujar_controles_boton():
    # --- CONTROLES IZQUIERDA ---
    izquierda = [
        "Espacio: iniciar/pausar",
        "R: reiniciar",
        "↑: +velocidad",
        "↓: -velocidad"
    ]

    x_izq = boton1_x - 220
    y = boton1_y + 5

    for linea in izquierda:
        txt = fuente_controles.render(linea, True, (255,255,255))
        screen.blit(txt, (x_izq, y))
        y += 18

    # --- CONTROLES DERECHA ---
    derecha = [
        "C: copiar",
        "V: pegar",
        "T: último pausado",
        f"FPS: {fps}"
    ]

    x_der = boton1_x + boton_ancho + 100
    y = boton1_y + 5

    for linea in derecha:
        txt = fuente_controles.render(linea, True, (255,255,255))
        screen.blit(txt, (x_der, y))
        y += 18

# --- Bucle principal ---
corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            corriendo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = not pausado
                copia_de_pausado = copy.deepcopy(tablero)
            elif event.key == pygame.K_UP:
                fps += 1
            elif event.key == pygame.K_DOWN:
                fps -= 1
                if fps < 1:
                    fps = 1
            elif event.key == pygame.K_c:
                copia_tablero = copy.deepcopy(tablero)  
            elif event.key == pygame.K_v:
                if copia_tablero is not None and pausado == False:           
                    tablero = copy.deepcopy(copia_tablero)
                    pausado = True
            elif event.key == pygame.K_t:
                if copia_de_pausado is not None:           
                    tablero = copy.deepcopy(copia_de_pausado)
                    pausado = True
            elif event.key == pygame.K_r:
                tablero = tablero_de_inicio(grid_y, grid_x)
                pausado = True


        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Define el área del botón para detectar el clic
            boton_rect = pygame.Rect(boton1_x, boton1_y, boton_ancho, boton1_alto)
            
            # Verifica si el clic está dentro del botón
            if boton_rect.collidepoint(pos):
                pausado = not pausado
            else:
                # Si el clic no fue en el botón, verifica si fue en el tablero
                # Se ajusta la coordenada Y del mouse por el desplazamiento del tablero
                x, y = pos[0] // dimAncho, (pos[1] - desplazamiento_del_tablero) // dimAlto
                
                # Verifica que la posición sea válida y actualiza la celda
                if posicion_valida((y, x), grid_y, grid_x):
                    tablero[y][x] = 1 if tablero[y][x] == 0 else 0

    # Actualizar el tablero SOLO si no está pausado
    if not pausado:
        tablero = ciclo_de_la_vida(tablero)

    # Dibujar el tablero
    dibujar_tablero(tablero)
    texto_boton = "Iniciar" if pausado else "Pausar"
    
    # Dibuja el rectángulo del botón
    pygame.draw.rect(screen, boton1_color, (boton1_x, boton1_y, boton_ancho, boton1_alto))
    
    # Dibuja el texto centrado en el botón
    texto_renderizado = fuente_boton1.render(texto_boton, True, (255, 255, 255))
    pos_texto = texto_renderizado.get_rect(center=(boton1_x + boton_ancho // 2, boton1_y + boton1_alto // 2))
    screen.blit(texto_renderizado, pos_texto)
    
    dibujar_controles_boton()
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(fps)

pygame.quit()