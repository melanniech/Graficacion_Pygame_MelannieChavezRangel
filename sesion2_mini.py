import pygame
import sys

# --- 1. Inicialización ---
pygame.init()

# --- 2. Configuración de la Ventana ---
ANCHO = 640
ALTO = 640
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 2: Mini-proyecto Casa")

# --- 3. Colores ---
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

# (MODIFICADO) Colores para la casa
COLOR_CIELO = (135, 206, 235)  # Un azul cielo
COLOR_PASTO = (34, 139, 34)   # Un verde pasto
COLOR_TECHO = (139, 69, 19)   # Un color café para el techo
COLOR_VENTANA = (255, 255, 0) # Amarillo para las ventanas

# (MODIFICADO) Colores para cambiar la casa
COLOR_ROJO = (255, 0, 0)
COLOR_AZUL = (0, 0, 255)

# (MODIFICADO) Esta variable guardará el color actual de la casa
# Empezamos con la casa de color rojo
color_casa_actual = COLOR_ROJO

# (MODIFICADO) Usamos el cielo como fondo
COLOR_FONDO = COLOR_CIELO

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
            
            # --- LÍNEAS NUEVAS ---
            # Si presionan 'R', cambiamos la variable a rojo
            elif event.key == pygame.K_r:
                color_casa_actual = COLOR_ROJO
            
            # Si presionan 'B', cambiamos la variable a azul
            elif event.key == pygame.K_b:
                color_casa_actual = COLOR_AZUL
            # --- FIN LÍNEAS NUEVAS ---
        
    # --- 6. Lógica de dibujado ---
    # Rellenamos la pantalla con el color de fondo (CIELO)
    pantalla.fill(COLOR_FONDO)

    # --- 7. Dibujar la casa ---
    ### ¡CÓDIGO NUEVO! ###
    
    # Dibujamos el pasto (un rectángulo en la parte de abajo)
    # (x, y, ancho, alto)
    pygame.draw.rect(pantalla, COLOR_PASTO, (0, 450, ANCHO, ALTO - 450))
    
    # Dibujamos el cuerpo de la casa (un rectángulo)
    # Usa la variable "color_casa_actual" que cambia con las teclas
    pygame.draw.rect(pantalla, color_casa_actual, (220, 250, 200, 200))
    
    # Dibujamos el techo (un polígono/triángulo)
    # (punto1, punto2, punto3)
    puntos_techo = [(200, 250), (320, 150), (440, 250)]
    pygame.draw.polygon(pantalla, COLOR_TECHO, puntos_techo)
    
    # Dibujamos las ventanas (dos círculos)
    # (pantalla, color, centro, radio)
    pygame.draw.circle(pantalla, COLOR_VENTANA, (270, 310), 30)
    pygame.draw.circle(pantalla, COLOR_VENTANA, (370, 310), 30)
    
    # --- 8. Actualización de la pantalla ---
    pygame.display.flip()

# --- 9. Salir ---
pygame.quit()
sys.exit()