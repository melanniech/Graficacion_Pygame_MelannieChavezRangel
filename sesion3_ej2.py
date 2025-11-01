import pygame
import sys
import math # ¡IMPORTANTE! Importamos la biblioteca de matemáticas

# --- 1. Inicialización ---
pygame.init()

# --- 2. Configuración de la Ventana ---
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 3: Movimiento Circular")

# --- 3. Colores ---
COLOR_FONDO = (25, 25, 25) # Un fondo gris oscuro
COLOR_BLANCO = (255, 255, 255)

# --- 4. Configuración del Rectángulo ---
CENTRO_X = 400
CENTRO_Y = 300
RADIO = 150 # 150 píxeles
angulo = 0

# Creamos el rectángulo
jugador_rect = pygame.Rect(0, 0, 50, 50) # Un cuadrado de 50x50

# --- 5. Bucle Principal ---
clock = pygame.time.Clock()
running = True

while running:

    # --- 6. Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # --- 7. Lógica de Movimiento (¡CÓDIGO CORREGIDO!) ---
    
    # Calculamos la nueva 'x' usando Coseno
    # ¡CORREGIDO! Envolvemos el resultado en int() para quitar decimales
    nueva_x = int(CENTRO_X + (math.cos(angulo) * RADIO))
    
    # Calculamos la nueva 'y' usando Seno
    # ¡CORREGIDO! Envolvemos el resultado en int() para quitar decimales
    nueva_y = int(CENTRO_Y + (math.sin(angulo) * RADIO))
    
    # Actualizamos la posición central del rectángulo
    jugador_rect.center = (nueva_x, nueva_y)
    
    # Incrementamos el ángulo para el próximo frame
    angulo += 0.05
    
    # --- 8. Lógica de dibujado ---
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_BLANCO, jugador_rect)
    
    # --- 9. Actualización de la pantalla ---
    pygame.display.flip()
    
    # --- 10. Control de Velocidad ---
    clock.tick(60)

# --- 11. Salir ---
pygame.quit()
sys.exit()