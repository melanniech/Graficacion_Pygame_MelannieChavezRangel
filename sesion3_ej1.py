import pygame
import sys

# --- 1. Inicialización ---
pygame.init()

# --- 2. Configuración de la Ventana ---
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 3: Movimiento y Límites")

# --- 3. Colores ---
COLOR_FONDO = (25, 25, 25) # Un fondo gris oscuro
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)

# --- 4. Configuración del "Jugador" (El Rectángulo) ---

# Esta variable guardará el color actual del rectángulo
# Empezamos con el color azul
color_jugador = COLOR_AZUL

# Esta variable es la velocidad (en píxeles por frame)
velocidad_jugador = 5

# Creamos el rectángulo en el centro de la pantalla
x_inicial = (ANCHO // 2) - 25
y_inicial = (ALTO // 2) - 25
jugador_rect = pygame.Rect(x_inicial, y_inicial, 50, 50) # Un cuadrado de 50x50

# --- 5. Bucle Principal ---
running = True
while running:

    # --- 6. Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # --- 7. Lógica de Movimiento ---
    # Revisa CUALES teclas están presionadas en este mismo frame.
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        jugador_rect.x -= velocidad_jugador
    if keys[pygame.K_RIGHT]:
        jugador_rect.x += velocidad_jugador
    if keys[pygame.K_UP]:
        jugador_rect.y -= velocidad_jugador
    if keys[pygame.K_DOWN]:
        jugador_rect.y += velocidad_jugador
        
    # --- 8. Lógica de Colisión (¡CÓDIGO MODIFICADO!) ---
    # Aquí está la lógica que te pide la tarea:
    
    # Por defecto, el color es azul
    color_jugador = COLOR_AZUL
    tocando_borde = False # Creamos una "bandera" para saber si tocamos algo

    # 1. Comprobar borde IZQUIERDO
    if jugador_rect.left <= 0:
        jugador_rect.left = 0 # El "tope": no lo dejamos pasar de 0
        tocando_borde = True

    # 2. Comprobar borde DERECHO
    elif jugador_rect.right >= ANCHO:
        jugador_rect.right = ANCHO # El "tope": no lo dejamos pasar del ancho
        tocando_borde = True

    # 3. Comprobar borde SUPERIOR (ARRIBA)
    if jugador_rect.top <= 0:
        jugador_rect.top = 0 # El "tope"
        tocando_borde = True

    # 4. Comprobar borde INFERIOR (ABAJO)
    elif jugador_rect.bottom >= ALTO:
        jugador_rect.bottom = ALTO # El "tope"
        tocando_borde = True

    # 5. Lógica de cambio de color
    # Si la bandera "tocando_borde" se activó...
    if tocando_borde:
        color_jugador = COLOR_ROJO
    # Si no, el color se queda en el azul que pusimos al inicio de esta sección
    
    # --- FIN DEL CÓDIGO MODIFICADO ---
    
    # --- 9. Lógica de dibujado ---
    # Rellenamos la pantalla con el color de fondo
    pantalla.fill(COLOR_FONDO)
    
    # Dibujamos al jugador con su color y posición actualizados
    pygame.draw.rect(pantalla, color_jugador, jugador_rect)
    
    # --- 10. Actualización de la pantalla ---
    pygame.display.flip()

# --- 11. Salir ---
pygame.quit()
sys.exit()