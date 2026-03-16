# Práctica 3 - Juego PyGame
# Clase jugador
# Autor Pablo Illescas

import assets
import settings
import pygame

shipWidth = assets.ship.get_width()
"""Ancho de la nave"""
shipHeight = assets.ship.get_height()
"""Alto de la nave"""

maxX = settings.WIDTH - shipWidth
"""Posición X máxima"""
maxY = settings.HEIGHT - shipHeight
"""Posición Y máxima"""

shipX = maxX / 2
"""Posición en el eje x de la nave"""
shipY = maxY / 2
"""Posición en el eje y de la nave"""

class Player:
    """Clase para controlar el jugador"""
    def __init__(self):
        """Crear jugador"""
        self.__x = shipX
        """Posición jugador en el eje X"""
        self.__y = shipY
        """Posición jugador en el eje Y"""
        self.__speed = settings.SHIP_SPEED
        """Velocidad de movimiento"""
        self.__rect = pygame.Rect(self.__x, self.__y, shipWidth, shipHeight)
        """Rec de la nave"""
        self.__hp = settings.PLAYER_HEALTH
        """Vida del jugador"""
        self.__isDead = False
        """Estamos muertos"""

    @property
    def rect(self):
        return pygame.Rect(self.__x, self.__y, shipWidth, shipHeight)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def hp(self):
        return self.__hp
    
    @property
    def isDead(self):
        return self.__isDead

    def drawPlayer(self, screen):
        """Dibujar al jugador"""
        screen.blit(assets.ship, (self.__x, self.__y))

    def handle_player_movement(self, keys, dt):
        """Calcula la nueva posición de la nave y aplica límites"""
        newX, newY = 0, 0
        
        # Determinar velocidad actual (Sprint)
        current_speed = 0
        if keys[settings.KEY_SPRINT]:
            current_speed = self.__speed * 3
        else: current_speed = self.__speed

        # Variable para comprobar si hay que reproducir el sonido
        isMoving = False

        # Calcular nueva posición de la nave
        if keys[settings.KEYS_LEFT[0]]  or keys[settings.KEYS_LEFT[1]]:
            newX -= current_speed
            isMoving = True
        if keys[settings.KEYS_RIGHT[0]] or keys[settings.KEYS_RIGHT[1]]:
            newX += current_speed
            isMoving = True
        if keys[settings.KEYS_UP[0]]    or keys[settings.KEYS_UP[1]]:
            newY -= current_speed
            isMoving = True
        if keys[settings.KEYS_DOWN[0]]  or keys[settings.KEYS_DOWN[1]]:
            newY += current_speed
            isMoving = True
        
        # Si nos movemos
        if isMoving:
            # Si no está ocupado ya el sonido de movimiento
            if not assets.thrusterChannel.get_busy():
                # Reproducir sonido de movimiento en bucle
                assets.thrusterChannel.play(assets.thruster, loops=-1)
        # Si no nos movemos parar el sonido
        elif assets.thrusterChannel.get_busy():
            assets.thrusterChannel.stop()

        # Aplicar movimiento
        self.__x += newX * dt
        self.__y += newY * dt

        # Limitar a la pantalla (Clamping)
        self.__x = max(0, min(self.__x, maxX))
        self.__y = max(0, min(self.__y, maxY))
        # Actualizar rect para colisiones
        self.__rect.x = self.__x
        self.__rect.y = self.__y
    
    def resetPlayer(self):
        """Reiniciar jugador"""
        self.__x = shipX
        self.__y = shipY
        # Actualizar rect para colisiones
        self.__rect.x = self.__x
        self.__rect.y = self.__y
        # Actualizar vida
        self.__hp = settings.PLAYER_HEALTH
        self.__isDead = False

    def getHit(self):
        """Recibir daño"""
        self.__hp -= 1
        if self.hp <= 0: self.__isDead = True

    def getShotHeight(self):
        """Calcular altura de disparo"""
        return self.__y + shipHeight/2
    
    def getRightCannonPos(self):
        """Calcular posición del cañon derecho"""
        return self.__x + (shipWidth * 0.95)