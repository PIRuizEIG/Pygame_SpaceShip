# Práctica 3 - Juego PyGame
# Archivo de configuración
# Autor Pablo Illescas

# Importar os para capturar rutas
import os
# Importar PyGame
import pygame

TITLE = "Juego de Pablo"
"""Título"""

WIDTH = 800
"""Ancho de la pantalla"""
HEIGHT = 600
"""Alto de la pantalla"""
SIZE = (WIDTH, HEIGHT)
"""Tamaño de la pantalla"""
FPS = 60
"""FPS máximos"""

TITLE_POS=(WIDTH // 2, HEIGHT // 2 - 50)
"""Posición del título"""
SUBTITLE_POS=(WIDTH // 2, HEIGHT // 2 + 50)
"""Posición del subtitulo"""

TITLE_TEXT_COLOR = (200, 200, 200)
"""Color de texto en el título"""
GAME_TEXT_COLOR = (255, 255, 255)
"""Color de texto en juego"""

HEALTH_BAR_FULL = (0, 200, 0)
"""Barra de vida llena, verde"""
HEALTH_BAR_EMPTY = (200, 0, 0)
"""Barra de vida vacía, roja"""
HEALTH_BAR_BORDER = (255, 255, 255)
"""Borde de la barra de vida"""

BASE_PATH = os.path.dirname(__file__)
"""Obtener directorio base"""

SHIP_PATH = os.path.join(BASE_PATH, "sprites/ship.png")
"""Obtener camino a imagen de nave"""
ENEMY_PATH = os.path.join(BASE_PATH, "sprites/enemy.png")
"""Obtener camino a imagen de enemigo"""
BG__PATH = os.path.join(BASE_PATH, "sprites/bg.png")
"""Obtener camino a imagen de fondo"""
TITLE_BG_PATH  = os.path.join(BASE_PATH, "sprites/titleBG.jpg")
"""Obtener camino a imagen de fondo del título"""

LASER_PATH = os.path.join(BASE_PATH, "audio/laser.ogg")
"""Obtener camino a sonido de disparo"""
THRUSTER_PATH = os.path.join(BASE_PATH, "audio/thruster.ogg")
"""Obtener camino a sonido de movimiento"""
EXPLOSION_PATH = os.path.join(BASE_PATH, "audio/Explosion.wav")
"""Obtener camino a sonido de explosión"""
TITLE_OST_PATH = os.path.join(BASE_PATH, "audio/Title Screen.wav")
"""Obtener camino a música del título"""
GAME_OST_PATH = os.path.join(BASE_PATH, "audio/Level 1.wav")
"""Obtener camino a música del juego"""

GAME_FONT_PATH = os.path.join(BASE_PATH, "fonts/kenvector_future.ttf")
"""Obtener camino a la fuente del juego"""
TITLE_FONT_PATH = os.path.join(BASE_PATH, "fonts/future-earth.ttf")
"""Obtener camino a la fuente del título"""

SHIP_SPEED = 300
"""Velocidad de la nave"""

PLAYER_HEALTH = 3
"""Vida inicial del jugador"""

BOSS_HEALTH = 10
"""Vida inicial del Boss"""
BOSS_SHOT_DELAY = 1000
"""Espacio entre disparos"""
BOSS_SPAWN_SCORE = 5
"""Puntuación para generar boss"""

ENEMY_MINSPEED = 100
"""Velocidad máxima de los enemigos"""
ENEMY_MAXSPEED = 250
"""Velocidad máxima de los enemigos"""

ENEMY_EVENT = pygame.USEREVENT + 1
"""Evento de creación de enemigos"""

LASER_COLOR = (255, 200, 0)
"""Color de las balas"""
LASER_SPEED = 500
"""Velocidad de las balas"""

KEY_FIRE = pygame.K_SPACE
"""Tecla de inicio de juego"""
KEY_EXIT = pygame.K_ESCAPE
"""Tecla de fin de juego"""
KEY_SPRINT = pygame.K_LSHIFT
"""Tecla de correr"""
KEYS_LEFT = (pygame.K_a, pygame.K_LEFT)
"""Teclas movimiento izquierda"""
KEYS_RIGHT = (pygame.K_d, pygame.K_RIGHT)
"""Teclas movimiento derecha"""
KEYS_UP = (pygame.K_w, pygame.K_UP)
"""Teclas movimiento arriba"""
KEYS_DOWN = (pygame.K_s, pygame.K_DOWN)
"""Teclas movimiento abajo"""
KEY_PAUSE = (pygame.K_p)
"""Tecla de pausa"""