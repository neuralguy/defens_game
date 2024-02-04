from math import sin, cos, atan2, degrees
from projectile import Projectile
from config import *
from sprites import get_sprites
import pygame


class Player:
    def __init__(self) -> None:
        self.x = width / 2 - player_size[0] / 2
        self.y = height / 2 - player_size[1] / 2
        self.__health = player_health
        self.projectiles = []
        self.weapon = "minigun"
        self.sprites = get_sprites("player")
    
    def get_damage(self, damage) -> None:
        self.__health -= damage
    
    def get_health(self, health) -> None:
        self.__health += health
        
    def is_alive(self) -> bool:
        return self.__health > 0
    
    def draw(self, surface, mouse_pos) -> None:
        player_pos = (self.x + player_size[0] / 2, self.y + player_size[1] / 2)
        randians = atan2(mouse_pos[1] - player_pos[1], mouse_pos[0] - player_pos[0])
        angle = degrees(randians)
        rotated_sprite = pygame.transform.rotate(self.sprites[0], -angle)
        new_rect = rotated_sprite.get_rect(center=self.sprites[0].get_rect(topleft=(self.x, self.y)).center)
        surface.blit(rotated_sprite, new_rect)
        
    def change_weapon(self, weapon) -> None:
        self.weapon = weapon
    
    def shoot(self, mouse_pos: tuple) -> None:
        bullet_pos = (self.x + player_size[0] / 2 - bullet_size[0] / 2, self.y + player_size[1] / 2 - bullet_size[1] / 2)
        randians = atan2(mouse_pos[1] - bullet_pos[1], mouse_pos[0] - bullet_pos[0])
        angle = degrees(randians)
        self.projectiles.append(Projectile(bullet_pos[0], bullet_pos[1], cos(randians), sin(randians), angle))