import pygame as pygame
import pygame_gui as gui
from sprites import prepare_sprites
from player import Player
from background import Grass
from turrets import *
from enemies import *
from config import *
import asyncio


class TimerManager:
    def __init__(self):
        self.timers = []

    def add_timer(self, name: str, interval: float, callback: callable, *args):
        timer = {
            "name": name,
            "interval": interval, # miliseconds
            "callback": callback,
            "args": args,
            "next_update_time": pygame.time.get_ticks() + interval
        }
        self.timers.append(timer)
    
    def remove_timer(self, name):
        """removing timer with name from the list of timers"""
        for timer in self.timers:
            if timer["name"] == name:
                self.timers.remove(timer)
                break

    def update_timer(self, name, *args):
        """updating arguments for the timer"""
        for timer in self.timers:
            if timer["name"] == name:
                timer["args"] = args
                break

    def update(self):
        """calling all timers"""
        current_time = pygame.time.get_ticks()
        for timer in self.timers:
            if current_time >= timer["next_update_time"]:
                timer["callback"](*timer["args"])
                timer["next_update_time"] = current_time + timer["interval"]


class Game():
    def __init__(self) -> None:
        self.name = None
        self.width = None
        self.height = None
        self.cell_size = None
        self.fps = None
        self.grid_color = None
        self.clock = None
        self.screen = None
        self.player = None
        self.enemies = Enemies()
        self.background = None
        self.timer = None
        self.mouse_pos = []
        
    def start_game(self, name: str, width: int, height: int, cell_size: int, fps: int) -> None:
        """Initializing the pygame, setting all game variables and starting main game loop"""
        pygame.init()
        prepare_sprites()
        self.name = name
        pygame.display.set_caption(self.name)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.fps = fps
        self.grid_color = light_gray
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = Enemies()
        self.background = Grass(0, 0)
        self.timer = TimerManager()
        self.mouse_pos = (0, 0)
        self.score = 0
        self.game_cycle()
        
    async def draw_game(self) -> None:
        """Draw all on the screen"""
        # background
        self.background.draw(self.screen)
        
        # grid
        # [pygame.draw.line(self.screen, self.grid_color, (i, 0), (i, self.height)) for i in range(0, self.width, self.cell_size)]
        # [pygame.draw.line(self.screen, self.grid_color, (0, i), (self.width, i)) for i in range(0, self.height, self.cell_size)]
        
        # player and projectiles
        self.player.draw(self.screen, pygame.mouse.get_pos())
        
        for projectile in self.player.projectiles:
            projectile.draw(self.screen)
            projectile.update_pos()

        # enemy
        for enemy in self.enemies.enemies:
            enemy.draw(self.screen)
            enemy.move((self.player.x, self.player.y))
        
    async def check_collision(self):
        # check collisions
        for projectile in self.player.projectiles:
            for enemy in self.enemies.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    enemy.get_damage(projectile.damage)
                    
                    if enemy.health <= 0:
                        self.enemies.enemies.remove(enemy)
                    if projectile in self.player.projectiles:    # need to avoid some error
                        self.player.projectiles.remove(projectile)
                    
                if projectile.x < -bullet_size[0] or projectile.y < -bullet_size[1] or projectile.x > self.width + bullet_size[0] \
                    or projectile.y > self.height + bullet_size[1]:
                    if projectile in self.player.projectiles:
                        self.player.projectiles.remove(projectile)
                    
    def game_cycle(self):
        """Game action processing"""
        shooting = False
        self.timer.add_timer("spawn_enemy", 1000, self.enemies.spawn_enemy)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    shooting = True
                    if self.player.weapon == "pistol":
                        self.timer.add_timer("player_shoot", pistol_attack, self.player.shoot, self.mouse_pos)
                    elif self.player.weapon == "automat":
                        self.timer.add_timer("player_shoot", automat_attack, self.player.shoot, self.mouse_pos)
                    elif self.player.weapon == "minigun":
                        self.timer.add_timer("player_shoot", minigun_attack, self.player.shoot, self.mouse_pos)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    shooting = False
                    self.timer.remove_timer("player_shoot")
                    
            if shooting:
                self.mouse_pos = pygame.mouse.get_pos()
                self.timer.update_timer("player_shoot", self.mouse_pos)
                
            asyncio.run(self.draw_game())
            asyncio.run(self.check_collision())
            self.timer.update()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = Game()
    game.start_game(game_title, width, height, sell_size, fps)
    