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
# DESPUÉS
COLOR_FONDO = COLOR_VERDE

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

    # 6. Lógica de dibujado
    # Rellenamos la pantalla con el color de fondo
    pantalla.fill(COLOR_FONDO)

    # 7. Actualización de la pantalla
    # Pygame actualiza la pantalla con todo lo que dibujamos
    pygame.display.flip()

# --- 8. Salir ---
# Cuando salimos del bucle, cerramos pygame
pygame.quit()
sys.exit()