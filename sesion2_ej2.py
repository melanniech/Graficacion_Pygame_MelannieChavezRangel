import pygame
import sys

# --- 1. Inicialización ---
# Inicia pygame
pygame.init()

# --- 2. Configuración de la Ventana ---
# Dejamos el tamaño de 640x640 para que quepa bien
ANCHO = 640
ALTO = 640
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# (MODIFICADO) Título nuevo
pygame.display.set_caption("Sesión 2: Círculos Concéntricos")

# --- 3. Colores ---
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

# (MODIFICADO) Colores nuevos para los círculos
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_AMARILLO = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)

# (MODIFICADO) Usamos negro como fondo para que resalten los colores
COLOR_FONDO = COLOR_NEGRO

# --- 4. Bucle Principal ---
running = True
while running:

    # --- 5. Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # --- 6. Lógica de dibujado ---
    # Rellenamos la pantalla con el color de fondo (NEGRO)
    pantalla.fill(COLOR_FONDO)

    # --- 7. Dibujar los círculos ---
    ### ¡CÓDIGO NUEVO! ###
    # Borramos el código del tablero y pusimos esto:
    
    # Definimos el centro de la pantalla
    centro_x = ANCHO // 2 # 640 // 2 = 320
    centro_y = ALTO // 2  # 640 // 2 = 320
    centro = (centro_x, centro_y)
    
    # La tarea pide radios de 20, 40, 60, 80, 100
    # Para que se vean todos, los dibujamos de MAYOR a MENOR
    
    # Círculo 1 (el más grande, al fondo)
    pygame.draw.circle(pantalla, COLOR_CYAN, centro, 100)
    
    # Círculo 2
    pygame.draw.circle(pantalla, COLOR_AMARILLO, centro, 80)
    
    # Círculo 3
    pygame.draw.circle(pantalla, COLOR_AZUL, centro, 60)
    
    # Círculo 4
    pygame.draw.circle(pantalla, COLOR_VERDE, centro, 40)
    
    # Círculo 5 (el más pequeño, encima de todos)
    pygame.draw.circle(pantalla, COLOR_ROJO, centro, 20)
    
    # --- 8. Actualización de la pantalla ---
    pygame.display.flip()

# --- 9. Salir ---
pygame.quit()
sys.exit()