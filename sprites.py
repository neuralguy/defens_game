from os import listdir
from os.path import join
import pygame
from config import bullet_size, player_size, zombie_size, width, height


sprites = {
    "player": [],
    "mouse": [],
    "background": [],
    "projectiles": [],
    "weapon": [],
    "default_turret": [],
    "strong_turret": [],
    "bomb_turret": [],
    "zombie": []
}

def get_sprites(type):
    return sprites[type]

def prepare_sprites():
    main_path = "imgs"
    dirs = listdir(main_path)
    for dir in dirs:
        imgs = listdir(join(main_path, dir))
        if dir == "projectiles":
            for img in imgs:
                sprites[dir].append(pygame.transform.scale(pygame.image.load(join(main_path, dir, img)), bullet_size))
        if dir == "player":
            for img in imgs:
                sprites[dir].append(pygame.transform.scale(pygame.image.load(join(main_path, dir, img)), player_size))
        if dir == "zombie":
            for img in imgs:
                sprites[dir].append(pygame.transform.scale(pygame.image.load(join(main_path, dir, img)), zombie_size))
        if dir == "background":
            for img in imgs:
                sprites[dir].append(pygame.transform.scale(pygame.image.load(join(main_path, dir, img)), (width, height)))
                