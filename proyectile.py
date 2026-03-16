import pygame
import settings

class Projectile:
    """Clase para controlar los disparos"""
    def __init__(self, x, y):
        self.__x = x
        """Posición en x"""
        self.__y = y
        """Posición en y"""
        self.__speed = settings.LASER_SPEED
        """Velocidad"""
        self.__rect = pygame.Rect(self.__x, self.__y, 5, 10)
        """Rec de la bala"""
        self.__isDead = False
        """Está muerta la bala"""
        self.__direction = 1 # 1 Arriba, -1 Abajo
        """Dirección de movimiento"""

    @property
    def isDead(self):
        """Bala muerta"""
        return self.__isDead

    @property
    def rect(self):
        """Rect para colisiones"""
        return self.__rect
    
    @property
    def direction(self):
        """Dirección de disparo"""
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        """Dirección de disparo"""
        self.__direction = direction

    def move(self, deltaTime):
        """Mover la bala"""
        # Avanzamos posición en Y
        self.__y -= self.__direction * self.__speed * deltaTime
        self.__rect.y = int(self.__y)
        # Si sale de la pantalla marcar muerta para borrar
        if self.__y < 0 or self.__y > settings.HEIGHT: self.__isDead = True

    def draw(self, screen):
        """Dibujar la bala"""
        pygame.draw.rect(screen, settings.LASER_COLOR, self.__rect)

    def die(self):
        """Marcar muerto"""
        self.__isDead = True