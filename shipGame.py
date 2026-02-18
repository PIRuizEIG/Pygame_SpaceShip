# Práctica 3 - Juego PyGame
# Autor Pablo Illescas

# Importar os para capturar rutas
import os
# Importar PyGame
import pygame

# Iniciar PyGame
pygame.init()

# Iniciar el Mixer
pygame.mixer.init()

# Configurar el título del juego
pygame.display.set_caption("Juego de Pablo")

screenWidth = 800
"""Ancho de la pantalla"""
screenHeigh = 600
"""Alto de la pantalla"""
screenSize = (screenWidth, screenHeigh)
"""Tamaño de la pantalla"""

titlePos=(screenWidth // 2, screenHeigh // 2 - 50)
"""Posición del título"""
subTitlePos=(screenWidth // 2, screenHeigh // 2 + 50)
"""Posición del subtitulo"""

screen = pygame.display.set_mode(screenSize)
"""Pantalla"""

basePath = os.path.dirname(__file__)
"""Obtener directorio base"""

shipPath = os.path.join(basePath, "sprites/ship.png")
"""Obtener camino a imagen de nave"""
bgPath = os.path.join(basePath, "sprites/bg.png")
"""Obtener camino a imagen de fondo"""
titleBgPath  = os.path.join(basePath, "sprites/titleBG.jpg")
"""Obtener camino a imagen de fondo del título"""

laserPath = os.path.join(basePath, "audio/laser.ogg")
"""Obtener camino a sonido de disparo"""
thrusterPath = os.path.join(basePath, "audio/thruster.ogg")
"""Obtener camino a sonido de movimiento"""
titleOst = os.path.join(basePath, "audio/Title Screen.wav")
"""Obtener camino a música del título"""
gameOst = os.path.join(basePath, "audio/Level 1.wav")
"""Obtener camino a música del juego"""

gFontPath = os.path.join(basePath, "fonts/kenvector_future.ttf")
"""Obtener camino a la fuente del juego"""
tFontPath = os.path.join(basePath, "fonts/future-earth.ttf")
"""Obtener camino a la fuente del título"""

ship = pygame.image.load(shipPath).convert_alpha()
"""Imagen de una nave espacial"""
bg = pygame.image.load(bgPath).convert()
"""Imagen de fondo"""
titleBg = pygame.image.load(titleBgPath).convert()
"""Imagen de fondo del título"""

bgWidth = bg.get_width()
"""Ancho del fondo"""
bgHeight = bg.get_height()
"""Alto del fondo"""

shipSpeed = 5
"""Velocidad de la nave"""

shipWidth = ship.get_width()
"""Ancho de la nave"""
shipHeight = ship.get_height()
"""Alto de la nave"""

maxX = screenWidth - shipWidth
"""Posición X máxima"""
maxY = screenHeigh - shipHeight
"""Posición Y máxima"""

shipX = maxX / 2
"""Posición en el eje x de la nave"""
shipY = maxY / 2
"""Posición en el eje y de la nave"""

clock = pygame.time.Clock()
"""Reloj del juego"""

fireSfx = pygame.mixer.Sound(laserPath)
"""Sonido de disparo"""
thruster = pygame.mixer.Sound(thrusterPath)
"""Sonido de movimiento rápido"""
# Reservar canal para el motor para iniciar y parar el sonido siempre en el mismo sitio
# 7 por que por defecto es el canal más alto de 0 a 7
thrusterChannel = pygame.mixer.Channel(7)
"""Reserva de canal para el motor"""

gameFont = pygame.font.Font(gFontPath, 32)
"""Fuente de juego"""
titleFont = pygame.font.Font(tFontPath, 64)
"""Fuente de título"""

titleColor = (200, 200, 200)
"""Color de texto en el título"""
gameTextColor = (255, 255, 255)
"""Color de texto en juego"""

# Preparamos el texto del título con antialias en color rgb
titleText = titleFont.render("Space Game", True, titleColor)
"""Texto del título"""
# Calcular rectangulo para el título en la posición deseada
titleRect = titleText.get_rect(center=titlePos)
"""Rectangulo contenedor del título"""
# Preparamos el texto del subtitulo
promptText = gameFont.render("Press SPACE to start", True, titleColor)
"""Texto del subtitulo"""
# Calcular rectangulo para posición del subtitulo
promptRect = promptText.get_rect(center=subTitlePos)
"""Rectangulo contenedor del subtitulo"""

shots = 0
"""Contador de disparos"""

isRunning = True
"""Está ejecutandose el juego"""
inTitle = True
"""Estamos en el título"""
inPause = False
"""Estamos en pausa"""

keyFire = pygame.K_SPACE
"""Tecla de inicio de juego"""
keyExit = pygame.K_ESCAPE
"""Tecla de fin de juego"""
keySprint = pygame.K_LSHIFT
"""Tecla de correr"""
keysLeft = (pygame.K_a, pygame.K_LEFT)
"""Teclas movimiento izquierda"""
keysRight = (pygame.K_d, pygame.K_RIGHT)
"""Teclas movimiento derecha"""
keysUp = (pygame.K_w, pygame.K_UP)
"""Teclas movimiento arriba"""
keysDown = (pygame.K_s, pygame.K_DOWN)
"""Teclas movimiento abajo"""
keyPause = (pygame.K_p)
"""Tecla de pausa"""

def loadMusic (musicFile):
    """Reproducir música"""
    
    # Cargar pista
    pygame.mixer_music.load(musicFile)
    # Reproducir en bucle
    pygame.mixer_music.play(-1)

def resetShip():
    """Reiniciar nave"""

    global shots, shipX, shipY
    
    # Reiniciamos disparos
    shots = 0
     # Reiniciar posición de nave
    shipX = maxX/2
    shipY = maxY/2

def handleKeyPause():
    """Controlar tecla Pausa"""

    global inPause

    # Si en juego cambiar de estado de pausa
    if not inTitle: inPause = not inPause

def handleKeyExit():
    """Controlar tecla de salida"""

    global inTitle, isRunning

    # Si estamos en el título
    if inTitle:
        # Cerramos juego
        isRunning = False
    # Si estamos en el juego
    else:
        # Activamos el título
        inTitle = True
        resetShip()
        # Cargar música del Título
        loadMusic(titleOst)

def handleKeyFire():
    """Controlar tecla de disparo"""

    global inTitle, inPause, shots

    #Si estamos en el título
    if inTitle:
        # Cerramos la ventana de título
        inTitle = False
        # Reiniciamos pausa
        inPause = False
        # Cargamos música del juego
        loadMusic(gameOst)
    else:
        # En juego reproducir sonido
        fireSfx.play()
        # Sumar disparos
        shots += 1

def handleEvents():
    """Controlar eventos"""
    # Hacer globales las variables
    global isRunning
    # Recorer eventos
    for event in pygame.event.get():
        # Evento de cerrar ventana 
        if event.type == pygame.QUIT: 
            isRunning = False
        # Eventos de tecla
        if event.type == pygame.KEYDOWN:
            # Tecla salida
            if event.key == keyExit:
                handleKeyExit()
            # Tecla disparo
            if event.key == keyFire:
                handleKeyFire()
            # Tecla Pausa
            if event.key == keyPause:
                handleKeyPause()


def drawTitle():
    """Dibujar el título"""
    # Dibujar el fondo    
    screen.blit(titleBg, (0, 0))
    # Dibujar el título
    screen.blit(titleText, titleRect)
    # Dibujar el subtítulo
    screen.blit(promptText, promptRect)

def drawRepeatBg():
    """Dibujar el fondo de piezas"""
    # Empezando en 0, hasta alcanzar el ancho de pantalla en piezas del ancho del fondo
    for x in range(0, screenWidth, bgWidth):
        # Empezando en 0, hasta alcanzar el alto de pantalla en piezas del alto del fondo
        for y in range(0, screenHeigh, bgHeight):
            # Dibujar una pieza del fondo en posición (x,y)
            screen.blit(bg, (x, y))

def drawUi():
    """Dibujar texto de puntuación"""
    # Cargar texto
    text = gameFont.render(f"Shoots: {shots}", True, gameTextColor)
    # Calcular rectangulo de posición de texto
    textPos = text.get_rect(topright=(screenWidth-20, 20))
    # Dibujar texto
    screen.blit(text, textPos)

def drawGame():
    """Dibujar el juego"""
    # Dibujar fondo
    drawRepeatBg()
    # Dibujar nave
    screen.blit(ship, (shipX, shipY))
    # Dibujar UI
    drawUi()

def drawPause():
    """Dibujar pausa"""
    # Dibujar fondo
    drawRepeatBg()
    # Cargar texto
    text = gameFont.render("Paused", True, gameTextColor)
    textPos = text.get_rect(center=(screenWidth/2, screenHeigh/2))
    # Dibujar texto
    screen.blit(text, textPos)
    # Dibujar UI
    drawUi()

def handle_player_movement(keys, x, y):
    """Calcula la nueva posición de la nave y aplica límites"""
    newX, newY = 0, 0
    
    # Determinar velocidad actual (Sprint)
    current_speed = 0
    if keys[keySprint]:
        current_speed = shipSpeed * 3
    else: current_speed = shipSpeed

    # Variable para comprobar si hay que reproducir el sonido
    isMoving = False

    # Calcular nueva posición de la nave
    if keys[keysLeft[0]]  or keys[keysLeft[1]]:
        newX -= current_speed
        isMoving = True
    if keys[keysRight[0]] or keys[keysRight[1]]:
        newX += current_speed
        isMoving = True
    if keys[keysUp[0]]    or keys[keysUp[1]]:
        newY -= current_speed
        isMoving = True
    if keys[keysDown[0]]  or keys[keysDown[1]]:
        newY += current_speed
        isMoving = True
    
    # Si nos movemos
    if isMoving:
        # Si no está ocupado ya el sonido de movimiento
        if not thrusterChannel.get_busy():
            # Reproducir sonido de movimiento en bucle
            thrusterChannel.play(thruster, loops=-1)
    # Si no nos movemos parar el sonido
    elif thrusterChannel.get_busy():
        thrusterChannel.stop()

    # Aplicar movimiento
    x += newX
    y += newY

    # Limitar a la pantalla (Clamping)
    x = max(0, min(x, maxX))
    y = max(0, min(y, maxY))
    
    # Devolver posición en x e y
    return (x, y)

# Reproducir la música del título
loadMusic(titleOst)

# Mientras estemos en el título y dentro del juego
while isRunning:
    # Controlar eventos
    handleEvents()

    # Si estamos en el título
    if inTitle:
        # Dibujamos el título
        drawTitle()
    # Si no, estamos en el juego
    else:
        # Si estamos en pausa mostramos pausa
        if inPause:
            drawPause()
        # Si estamos en juego
        else:
            # Captura de las teclas pulsadas
            keys = pygame.key.get_pressed()

            # Actualizar posición de la nave
            shipX, shipY = handle_player_movement(keys, shipX, shipY)

            # Dibujar el juego    
            drawGame()

    pygame.display.update()
    # Actualizar la pantalla

    clock.tick(60)
    # Configurar fps máximo

# Cerrar el juego
pygame.quit()