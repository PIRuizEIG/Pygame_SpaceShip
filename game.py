# Práctica 3 - Juego PyGame
# Archivo de bucle de juego
# Autor Pablo Illescas

import pygame
import settings
import assets
from player import Player
from enemy import Enemy, Boss
from proyectile import Projectile

screen = assets.screen
"""Pantalla"""
clock = assets.clock
"""Reloj del juego"""

# Crear evento periódico
pygame.time.set_timer(settings.ENEMY_EVENT, 1750)

enemies = []
"""Lista de enemigos"""

score = 0
"""Contador de puntuación"""
proyectiles = []
"""Disparos en juego"""

isRunning = True
"""Está ejecutandose el juego"""
inTitle = True
"""Estamos en el título"""
inPause = False
"""Estamos en pausa"""

deltaTime = 0
"""tiempo transcurrido en segundos desde el último frame"""

def loadMusic (musicFile):
    """Reproducir música"""
    
    # Cargar pista
    pygame.mixer_music.load(musicFile)
    # Reproducir en bucle
    pygame.mixer_music.play(-1)

def reset():
    """Reiniciar Juego"""
    global score, boss
    # Reiniciamos disparos
    score = 0
    # Eliminamos el boss
    boss = None
    proyectiles.clear()
    enemies.clear()
    player.resetPlayer()

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
        reset()
        # Cargar música del Título
        loadMusic(settings.TITLE_OST_PATH)

def handleKeyFire():
    """Controlar tecla de disparo"""

    global inTitle, inPause

    #Si estamos en el título
    if inTitle:
        # Cerramos la ventana de título
        inTitle = False
        # Reiniciamos pausa
        inPause = False
        # Cargamos música del juego
        loadMusic(settings.GAME_OST_PATH)
    else:
        # En juego reproducir sonido
        assets.fireSfx.play()
        height = player.getShotHeight()     # Altura donde crear las balas
        right = player.getRightCannonPos()  # Posición de disparo derecho
        # Añadir disparos
        newShot = Projectile(player.x, height)
        proyectiles.append(newShot)
        newShot = Projectile(right, height)
        proyectiles.append(newShot)

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
            if event.key == settings.KEY_EXIT:
                handleKeyExit()
            # Tecla disparo
            if event.key == settings.KEY_FIRE:
                handleKeyFire()
            # Tecla Pausa
            if event.key == settings.KEY_PAUSE:
                handleKeyPause()
        # Evento de creación de enemigos
        if event.type == settings.ENEMY_EVENT:
            # Si no estamos en el título o ni en pausa 
            if not inPause and not inTitle:
                # Crear enemigo
                createEnemy()


def drawTitle():
    """Dibujar el título"""
    # Dibujar el fondo    
    screen.blit(assets.titleBg, (0, 0))
    # Dibujar el título
    screen.blit(assets.titleText, assets.titleRect)
    # Dibujar el subtítulo
    screen.blit(assets.promptText, assets.promptRect)

def drawRepeatBg():
    """Dibujar el fondo de piezas"""
    # Empezando en 0, hasta alcanzar el ancho de pantalla en piezas del ancho del fondo
    for x in range(0, settings.WIDTH, assets.bgWidth):
        # Empezando en 0, hasta alcanzar el alto de pantalla en piezas del alto del fondo
        for y in range(0, settings.HEIGHT, assets.bgHeight):
            # Dibujar una pieza del fondo en posición (x,y)
            screen.blit(assets.bg, (x, y))

def drawHealthBar(screen, xPos, yPos, current_hp, max_hp, width=200, height=20):
    """Dibujar barra de vida"""
    # Calcular el porcentaje de vida
    ratio = current_hp / max_hp
    # Dibujar fondo
    pygame.draw.rect(screen, settings.HEALTH_BAR_EMPTY, (xPos, yPos, width, height))
    # Dibujar vida actual
    pygame.draw.rect(screen, settings.HEALTH_BAR_FULL, (xPos, yPos, width * ratio, height))
    # Dibujar borde (Blanco)
    pygame.draw.rect(screen, settings.HEALTH_BAR_BORDER, (xPos, yPos, width, height), 2)

def drawUi():
    """Dibujar texto de puntuación"""
    # Cargar texto
    text = assets.gameFont.render(f"Score: {score}", True, settings.GAME_TEXT_COLOR)
    # Calcular rectangulo de posición de texto
    textPos = text.get_rect(topright=(settings.WIDTH-20, 20))
    # Dibujar texto
    screen.blit(text, textPos)
    # Dibujar vida del jugador
    drawHealthBar(screen, 15, 15, player.hp, settings.PLAYER_HEALTH)

def drawGame():
    """Dibujar el juego"""
    # Dibujar fondo
    drawRepeatBg()
    # Dibujar nave
    player.drawPlayer(screen)
    # Para cada enemigo dibujar
    for enemy in enemies: enemy.draw(screen)
    # Si hay boss
    if boss: 
        # Dibujar el boss
        boss.draw(screen)
        # Dibujar barra de vida del Boss arriba en el centro
        drawHealthBar(screen, settings.WIDTH//2 - 100, 10, boss.hp, settings.BOSS_HEALTH)
    # Por cada proyectil dibujar
    for bullet in proyectiles: bullet.draw(screen)
    # Dibujar UI
    drawUi()

def drawPause():
    """Dibujar pausa"""
    # Dibujar fondo
    drawRepeatBg()
    # Cargar texto
    text = assets.gameFont.render("Paused", True, settings.GAME_TEXT_COLOR)
    textPos = text.get_rect(center=(settings.WIDTH/2, settings.HEIGHT/2))
    # Dibujar texto
    screen.blit(text, textPos)
    # Dibujar UI
    drawUi()

def createEnemy():
    """Crear enemigo"""
    global boss
    # Si llegamos a los puntos para generar Boss y no hay un Boss activo crear Boss
    if score > 0 and (score % settings.BOSS_SPAWN_SCORE == 0) and boss is None:
        boss = Boss()
    # Creamos enemigos normales si no hay Boss
    elif boss is None:
        enemies.append(Enemy())

def moveEnemies(deltaTime):
    """Mover los enemigos"""
    global boss
    # Para cada enemigo
    for enemy in enemies:
        # Mover
        enemy.move(deltaTime)
    # Si hay boss mover
    if boss:
        boss.move(deltaTime)
        # Lógica de disparo del Boss, si toca disparar
        if boss.shoot():
            # Crear disparo
            newShot = Projectile(boss.rect.centerx, boss.rect.bottom)
            # El Boss dispara hacia abajo, -1
            newShot.direction = -1
            # Añadir disparo a la lista de disparos
            proyectiles.append(newShot)

def cleanEnemies():
    """Eliminar enemigos muertos"""
    global enemies
    enemies = [e for e in enemies if not e.isDead]

def moveProyectiles(deltaTime):
    """Mover las balas"""
    # Para cada bala
    for bullet in proyectiles:
        # Mover
        bullet.move(deltaTime)

def cleanProyectiles():
    """Eliminar balas muertas"""
    global proyectiles
    proyectiles = [p for p in proyectiles if not p.isDead]

def checkCollisions():
    """Controlar colisiones"""
    global score, boss
    playerRect = player.rect
    # Para cada enemigo
    for enemy in enemies:
        # Si el rectángulo del jugador toca el del enemigo
        if playerRect.colliderect(enemy.rect):
            # Reproducir sfx
            assets.explisionSfx.play()
            # Matamos al enemigo
            enemy.die()
            # Registramos golpe
            player.getHit()
            # Si el jugador está muerto reiniciamos
            if (player.isDead): reset()
            break
    # Por cada proyectil y enemigo
    for bullet in proyectiles:
        # Si la bala está desactivada salir
        if bullet.isDead: break
        # Para cada enemigo
        for enemy in enemies:
            # Si hay colisión
            if bullet.rect.colliderect(enemy.rect):
                # Reproducir SFX
                assets.explisionSfx.play()
                # Marcamos ambos como muertos para que clean los elimine
                bullet.die()
                enemy.die()
                score += 1
        # Si hay colision con el jugador
        if bullet.direction < 0 and bullet.rect.colliderect(player.rect):
            # Eliminar bala
            bullet.die()
            # Registrar golpe al jugador
            player.getHit()
            # Reproducir SFX
            assets.explisionSfx.play()
            # Si el jugador está muerto reiniciamos
            if player.isDead: reset()
        # Si existe boss
        if boss and not boss.isDead:
        # Colisión Balas vs Boss
            if bullet.rect.colliderect(boss.rect):
                # Desactivar la baa
                bullet.die()
                # Registrar el golpe
                boss.getHit()
                # Reproducir SFX
                assets.explisionSfx.play()
                # Si el boss ha muerto
                if boss.isDead:
                    # Dar puntuación
                    score += 10
                    # Eliminar el boss
                    boss = None
                    # Añadir enemigo normal
                    enemies.append(Enemy())

# Reproducir la música del título
loadMusic(settings.TITLE_OST_PATH)

player = Player()
"""Jugador"""

boss = None 
"""Instancia del Boss (None si no ha aparecido)"""

# Mientras estemos en el título y dentro del juego
while isRunning:
    # Controlar eventos
    handleEvents()

    # Actualizar deltaTime y Configurar fps máximos
    deltaTime = clock.tick(settings.FPS) / 1000

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

            player.handle_player_movement(keys, deltaTime)
            moveEnemies(deltaTime)
            moveProyectiles(deltaTime)
            checkCollisions()
            cleanEnemies()
            cleanProyectiles()

            # Dibujar el juego    
            drawGame()

    # Actualizar la pantalla
    pygame.display.update()
# Cerrar el juego
pygame.quit()