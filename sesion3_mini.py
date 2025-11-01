import pygame
import sys

# --- 1. Inicialización ---
pygame.init()

# --- 2. Configuración de la Ventana ---
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 3: Mini-proyecto Rastro")

# --- 3. Colores ---
COLOR_FONDO = (25, 25, 25) # Un fondo gris oscuro
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)
# (MODIFICADO) Color para el rastro
COLOR_RASTRO = (0, 150, 150) # Un color cyan oscuro

# --- 4. Configuración del "Jugador" (El Rectángulo) ---
color_jugador = COLOR_AZUL
velocidad_jugador = 5
jugador_rect = pygame.Rect((ANCHO // 2) - 25, (ALTO // 2) - 25, 50, 50)

# --- 5. Lógica del Rastro (¡NUEVO!) ---
# 1. Creamos una lista vacía para guardar las posiciones
lista_rastro = []
longitud_maxima_rastro = 100 # Límite para que no se llene la memoria

# --- 6. Bucle Principal ---
clock = pygame.time.Clock() # Añadimos un reloj para velocidad constante
running = True

while running:

    # --- 7. Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # --- 8. Lógica de Movimiento ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jugador_rect.x -= velocidad_jugador
    if keys[pygame.K_RIGHT]:
        jugador_rect.x += velocidad_jugador
    if keys[pygame.K_UP]:
        jugador_rect.y -= velocidad_jugador
    if keys[pygame.K_DOWN]:
        jugador_rect.y += velocidad_jugador
        
    # --- 9. Lógica de Colisión (igual que sesion3_ej1.py) ---
    color_jugador = COLOR_AZUL
    tocando_borde = False 
    if jugador_rect.left <= 0:
        jugador_rect.left = 0
        tocando_borde = True
    elif jugador_rect.right >= ANCHO:
        jugador_rect.right = ANCHO
        tocando_borde = True
    if jugador_rect.top <= 0:
        jugador_rect.top = 0
        tocando_borde = True
    elif jugador_rect.bottom >= ALTO:
        jugador_rect.bottom = ALTO
        tocando_borde = True
    if tocando_borde:
        color_jugador = COLOR_ROJO
    
    # --- 10. Lógica del Rastro (¡NUEVO!) ---
    # 2. Agregamos la posición central del jugador a la lista
    lista_rastro.append(jugador_rect.center)
    
    # 3. Limitamos la longitud del rastro
    # Si la lista es más larga que 100...
    if len(lista_rastro) > longitud_maxima_rastro:
        # ...borramos el elemento más antiguo (el del principio)
        lista_rastro.pop(0)

    # --- 11. Lógica de dibujado ---
    pantalla.fill(COLOR_FONDO)
    
    # 4. Dibujamos el rastro (¡NUEVO!)
    # Antes de dibujar al jugador, dibujamos todos los círculos
    # en las posiciones guardadas en la lista.
    for posicion in lista_rastro:
        pygame.draw.circle(pantalla, COLOR_RASTRO, posicion, 5) # Círculos de radio 5
    
    # Dibujamos al jugador (ENCIMA del rastro)
    pygame.draw.rect(pantalla, color_jugador, jugador_rect)
    
    # --- 12. Actualización de la pantalla ---
    pygame.display.flip()
    
    # --- 13. Control de Velocidad ---
    clock.tick(60)

# --- 14. Salir ---
pygame.quit()
sys.exit()