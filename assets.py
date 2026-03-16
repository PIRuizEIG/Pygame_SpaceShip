# Práctica 3 - Juego PyGame
# Archivo de control de assets
# Autor Pablo Illescas

import settings
import pygame

# Iniciar PyGame
pygame.init()

# Iniciar el Mixer
pygame.mixer.init()

screen = pygame.display.set_mode(settings.SIZE)
"""Pantalla"""
clock = pygame.time.Clock()
"""Reloj del juego"""

# Configurar el título del juego
pygame.display.set_caption(settings.TITLE)

ship = pygame.image.load(settings.SHIP_PATH).convert_alpha()
"""Imagen de una nave espacial"""
enemy = pygame.image.load(settings.ENEMY_PATH).convert_alpha()
"""Imagen de una nave enemiga"""
bg = pygame.image.load(settings.BG__PATH).convert()
"""Imagen de fondo"""
titleBg = pygame.image.load(settings.TITLE_BG_PATH).convert()
"""Imagen de fondo del título"""

bgWidth = bg.get_width()
"""Ancho del fondo"""
bgHeight = bg.get_height()
"""Alto del fondo"""

fireSfx = pygame.mixer.Sound(settings.LASER_PATH)
"""Sonido de disparo"""
thruster = pygame.mixer.Sound(settings.THRUSTER_PATH)
"""Sonido de movimiento rápido"""
explisionSfx = pygame.mixer.Sound(settings.EXPLOSION_PATH)
"""Sonido de explosion"""
# Reservar canal para el motor para iniciar y parar el sonido siempre en el mismo sitio
# 7 por que por defecto es el canal más alto de 0 a 7
thrusterChannel = pygame.mixer.Channel(7)
"""Reserva de canal para el motor"""

gameFont = pygame.font.Font(settings.GAME_FONT_PATH, 32)
"""Fuente de juego"""
titleFont = pygame.font.Font(settings.TITLE_FONT_PATH, 64)
"""Fuente de título"""

# Preparamos el texto del título con antialias en color rgb
titleText = titleFont.render("Space Game", True, settings.TITLE_TEXT_COLOR)
"""Texto del título"""
# Calcular rectangulo para el título en la posición deseada
titleRect = titleText.get_rect(center=settings.TITLE_POS)
"""Rectangulo contenedor del título"""
# Preparamos el texto del subtitulo
promptText = gameFont.render("Press SPACE to start", True, settings.TITLE_TEXT_COLOR)
"""Texto del subtitulo"""
# Calcular rectangulo para posición del subtitulo
promptRect = promptText.get_rect(center=settings.SUBTITLE_POS)
"""Rectangulo contenedor del subtitulo"""