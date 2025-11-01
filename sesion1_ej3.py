import pygame
import sys

# --- 1. Inicialización ---
# Inicia pygame
pygame.init()

# --- 2. Configuración de la Ventana (¡Aquí vamos a modificar!) ---
# Definimos el tamaño de la ventana
ANCHO = 1000
ALTO = 800
# Creamos la ventana (pantalla)
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Establecemos un título (¡Aquí vamos a modificar!)
pygame.display.set_caption("Mi primer programa gráfico")

# --- 3. Colores (¡Aquí vamos a modificar!) ---
# Definimos colores en formato RGB (Rojo, Verde, Azul)
COLOR_VERDE = (0, 255, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_FONDO = COLOR_VERDE

# --- LÍNEA NUEVA ---
contador_frames = 0
# --- FIN DE LÍNEA NUEVA ---

# --- 4. Bucle Principal ---
# El bucle principal se ejecuta indefinidamente hasta que cerremos la ventana
running = True
while running:

    # 5. Manejo de Eventos
    # Revisa todos los eventos que están ocurriendo
    for event in pygame.event.get():
        # Si el evento es "cerrar la ventana" (hacer clic en la 'X')
        if event.type == pygame.QUIT:
            running = False # Salimos del bucle
        # Si no, revisa si el evento es presionar una tecla
        elif event.type == pygame.KEYDOWN:
            # Si esa tecla fue 'Escape'
            if event.key == pygame.K_ESCAPE:
                running = False # También salimos del bucle
# --- LÍNEAS NUEVAS ---
    # 6. Lógica del Contador
    contador_frames += 1 # Le sumamos 1 al contador
    print(f"Frame: {contador_frames}") # Imprimimos en la terminal 
    # --- FIN DE LÍNEAS NUEVAS ---
    # --- LÍNEAS NUEVAS ---
    # Comprobamos si llegamos a 300 frames 
    if contador_frames >= 300:
        running = False # Salimos del bucle
    # --- FIN DE LÍNEAS NUEVAS ---
    # 7. Lógica de dibujado
    # Rellenamos la pantalla con el color de fondo
    pantalla.fill(COLOR_FONDO)

    # 8. Actualización de la pantalla
    # Pygame actualiza la pantalla con todo lo que dibujamos
    pygame.display.flip()

# --- 9. Salir ---
# Cuando salimos del bucle, cerramos pygame
pygame.quit()
sys.exit()