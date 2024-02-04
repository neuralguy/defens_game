from sprites import sprites
from config import bullet_speed, bullet_damage
import pygame 


class Projectile:
    def __init__(self, x: int, y: int, vx: int, vy: int, angle: int) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.speed = bullet_speed
        self.damage = bullet_damage
        self.angle = angle
        self.sprites = sprites["projectiles"]
        self.rect = 0
        
    def update_pos(self):
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed
    
    def draw(self, surface):
        rotated_sprite = pygame.transform.rotate(self.sprites[0], -self.angle)
        self.rect = rotated_sprite.get_rect(center=self.sprites[0].get_rect(topleft=(self.x, self.y)).center)
        surface.blit(rotated_sprite, self.rect)