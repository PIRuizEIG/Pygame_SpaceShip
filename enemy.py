# Práctica 3 - Juego PyGame
# Clase enemigo
# Autor Pablo Illescas

import assets
import settings
# Importar aleatorio
import random
import pygame

enemyWidth = assets.enemy.get_width()
"""Ancho de la nave"""
enemyHeight = assets.enemy.get_height()
"""Alto de la nave"""

class Enemy:
    """Clase para controlar los enemigos"""
    def __init__(self):
        self._speed = random.randint(settings.ENEMY_MINSPEED, settings.ENEMY_MAXSPEED)
        """Velocidad del enemigo"""
        self._x = random.randint(0, settings.WIDTH - enemyWidth)
        """Posición en eje X"""
        self._y = 0 - enemyHeight
        """Posición en eje Y"""
        self._rect = pygame.Rect(self._x, self._y, enemyWidth, enemyHeight)
        """Rec de la nave"""
        self._isDead = False
        """Estamos muertos"""

    @property
    def isDead(self):
        return self._isDead
    
    @property
    def rect(self):
        return self._rect

    def move(self, deltaTime):
        """Mover al enemigo"""
        # Avanzamos posición en Y
        self._y += self._speed * deltaTime
        self._rect.y = int(self._y)
        # Si salimos de la pantalla nos marcamos para la muerte
        if self._y > settings.HEIGHT: self._isDead = True

    def draw(self, screen):
        """Dibujar el enemigo"""
        screen.blit(assets.enemy, (self._x, self._y))

    def die(self):
        """Marcar muerto"""
        self._isDead = True

class Boss(Enemy):
    def __init__(self):
        # Llamamos al constructor del padre (Enemy)
        super().__init__()
        
        # Sobrescribimos o añadimos propiedades específicas
        self.__hp = settings.BOSS_HEALTH
        """Vida del boss"""
        self.__direction = 1 # 1 derecha, -1 izquierda
        """Dirección de movimiento"""
        
        # Lo hacemos más grande (escalando la imagen original)
        self.__image = pygame.transform.scale(assets.enemy, (150, 100))
        """Imagen"""
        self._rect = self.__image.get_rect(midtop=(settings.WIDTH//2, 20))
        """Rec de la nave"""
        
        self.__last_shot = pygame.time.get_ticks()
        """Último disparo"""
        self.__shoot_delay = settings.BOSS_SHOT_DELAY
        """Espacio entre disparos"""

    @property
    def hp(self):
        """Salud del Boss"""
        return self.__hp

    def move(self, deltaTime):
        """Mover al boss"""

        # El Boss se mueve lateralmente en lugar de solo hacia abajo
        x = self._rect.x
        x += self._speed * deltaTime * self.__direction
        self._rect.x = int(x)
        
        # Rebotar en las paredes
        if self._rect.right >= settings.WIDTH or self._rect.left <= 0:
            self.__direction *= -1
            
    def shoot(self):
        """Comprobar si se dispara"""
        # Obtener tiempo
        now = pygame.time.get_ticks()
        # Si ha pasado suficiente tiempo desde el ultimo disparo
        if now - self.__last_shot > self.__shoot_delay:
            # Actualizar hora de último disparo
            self.__last_shot = now
            # Mandar True para generar disparos
            return True
        # Mandar False, no hay que disparar
        return False
    
    def getHit(self):
        """Recibir daño"""
        self.__hp -= 1
        if self.hp <= 0: self._isDead = True

    def draw(self, screen):
        """Dibujar el Boss"""
        screen.blit(self.__image, self._rect)
