import pygame
import sys

# --- 1. Inicialización ---
# Inicia pygame
pygame.init()

# --- 2. Configuración de la Ventana ---
# Definimos el tamaño de la ventana
ANCHO = 640
ALTO = 640
# Creamos la ventana (pantalla)
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Establecemos un título
pygame.display.set_caption("Sesión 2: Tablero de Ajedrez")

# --- 3. Colores ---
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

# Usamos blanco como fondo de la ventana
COLOR_FONDO = COLOR_BLANCO

# --- 4. Bucle Principal ---
# El bucle principal se ejecuta indefinidamente hasta que cerremos la ventana
running = True
while running:

    # --- 5. Manejo de Eventos ---
    # Revisa todos los eventos que están ocurriendo
    for event in pygame.event.get():
        # Si el evento es "cerrar la ventana" (hacer clic en la 'X')
        if event.type == pygame.QUIT:
            running = False # Salimos del bucle
        
        elif event.type == pygame.KEYDOWN: # Si no, revisa si el evento es presionar una tecla
            
            if event.key == pygame.K_ESCAPE: # Si esa tecla fue 'Escape'
                running = False # También salimos del bucle
        

    # --- 6. Lógica de dibujado ---
    # Rellenamos la pantalla con el color de fondo (BLANCO)
    pantalla.fill(COLOR_FONDO)

    # --- 7. Dibujar el tablero ---
    ### Todo este bloque de dibujo AHORA ESTÁ DENTRO del "while running":
    
    # Calculamos el tamaño de cada casilla
    tamano_casilla = ANCHO // 8 # 800 // 8 = 100
    
    # Bucle para las filas (de 0 a 7)
    for fila in range(8):
        # Bucle para las columnas (de 0 a 7)
        for columna in range(8):
            
            # --- Lógica para alternar colores ---
            if (fila + columna) % 2 == 0:
                color = COLOR_BLANCO
            else:
                color = COLOR_NEGRO
                
            # Calculamos la posición (x, y) del cuadrado
            x = columna * tamano_casilla
            y = fila * tamano_casilla
            
            # Creamos el rectángulo (x, y, ancho, alto)
            rectangulo = (x, y, tamano_casilla, tamano_casilla)
            
            # Dibujamos el rectángulo en la pantalla
            pygame.draw.rect(pantalla, color, rectangulo)

    # --- 8. Actualización de la pantalla ---
    ### ¡CORREGIDO! ###
    ### El "flip()" AHORA ESTÁ DENTRO del "while running"
    ### para que actualice la pantalla en CADA frame.
    pygame.display.flip()

# --- 9. Salir ---
# (ESTO SÍ VA AFUERA, solo se ejecuta cuando running = False)
# Cuando salimos del bucle, cerramos pygame
pygame.quit()
sys.exit()