from random import uniform, random, randint, choice
from config import *
from math import atan2, sin, cos, degrees
from sprites import sprites
import pygame


class Enemies:
    def __init__(self) -> None:
        self.enemies = []
        
    def spawn_enemy(self) -> None:
        enemy_type = uniform(0, 10)
        # if enemy_type < 2:
        if random() < 0.5:
            x = 0 - zombie_size[0] if random() < 0.5 else width + zombie_size[0]
            y = randint(0, height)
        else:
            x = randint(0, width)
            y = 0 - zombie_size[0] if random() < 0.5 else height + zombie_size[0]
        
        self.enemies.append(Zombie(x, y))


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.health = zombie_health
        self.speed = zombie_speed
        self.damage = zombie_damage
        self.image = sprites["player"][0]
        self.rect = 0
        
    def draw(self, surface):
        player_pos = (self.__x + player_size[0] / 2, self.__y + player_size[1] / 2)
        randians = atan2(height / 2 - player_pos[1], width / 2 - player_pos[0])
        angle = degrees(randians)
        rotated_sprite = pygame.transform.rotate(self.image, -angle)
        self.rect = rotated_sprite.get_rect(center=self.image.get_rect(topleft=(self.__x, self.__y)).center)
        surface.blit(rotated_sprite, self.rect)
        
    def get_damage(self, damage):
        self.health -= damage
        
    def move(self, player_pos):
        radians = atan2((player_pos[1] - zombie_size[0] / 2) - self.__y, (player_pos[0] - zombie_size[0] / 2) - self.__x)
        vx = cos(radians)
        vy = sin(radians)
        self.__x += vx * self.speed
        self.__y += vy * self.speed
        