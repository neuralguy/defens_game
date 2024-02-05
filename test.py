import pygame_gui as gui
import pygame
from config import *
from game import Game


class GameGui:
    def __init__(self, screen):
        self.manager = gui.UIManager((width, height), 'theme.json')
        self.screen = screen
        self.shop_card_size = 200
        self.clock = pygame.time.Clock()
        self.weapon = "pistol"
        
    def main_menu(self):
        self.manager.clear_and_reset()
        background_img = pygame.transform.scale(pygame.image.load("imgs/main_menu/back1.jpg"), (width, height))
        
        start_game_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 2 - 250, height / 2 + 100, 500, 100),
            text="Начать игру",
            manager=self.manager)
        shop_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 2 - 200, height / 2 + 200, 200, 100),
            text="Магазин",
            manager=self.manager)
        settings_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 2 , height / 2 + 200, 200, 100),
            text="Настройки",
            manager=self.manager)
        
        while True:
            for event in pygame.event.get():
                self.manager.process_events(event)
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_game_btn:
                        game = Game()
                        game.init_game(game_title, width, height, fps, self.weapon)
                    if event.ui_element == shop_btn:
                        self.shop_menu()
                    if event.ui_element == settings_btn:
                        self.settings_menu()
        
            self.screen.blit(background_img, (0, 0))
            self.manager.update(fps)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(fps)
            
    def shop_menu(self):
        self.manager.clear_and_reset()
        background_img = pygame.transform.scale(pygame.image.load("imgs/main_menu/back1.jpg"), (width, height))
        pistol_img = pygame.transform.scale(pygame.image.load("imgs/weapon/pistol.png"), (self.shop_card_size, self.shop_card_size))
        automat_img = pygame.transform.scale(pygame.image.load("imgs/weapon/automat.png"), (self.shop_card_size, self.shop_card_size))
        minigun_img = pygame.transform.scale(pygame.image.load("imgs/weapon/minigun.png"), (self.shop_card_size, self.shop_card_size))
        
        back_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 20, 150, 50),
            text="Назад",
            manager=self.manager)
        
        gui.elements.UILabel(
            relative_rect=pygame.Rect(width / 2 - 300, 50, 600, 300),
            text="ВЫБЕРИ ОРУЖИЕ",
            manager=self.manager).set_active_effect(gui.TEXT_EFFECT_FADE_IN, {"time_per_alpha_change": 10})
        
        pistol_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 5, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            text="",
            manager=self.manager)
        
        automat_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 2 - self.shop_card_size / 2, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            text="",
            manager=self.manager)
        
        minigun_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(width / 2 + self.shop_card_size, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            text="",
            manager=self.manager)
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 5, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            image_surface=pistol_img,
            manager=self.manager)
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 2 - self.shop_card_size / 2, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            image_surface=automat_img,
            manager=self.manager)
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 2 + self.shop_card_size, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            image_surface=minigun_img,
            manager=self.manager)
        
        if self.weapon == "pistol":
            pistol_btn.select()
            automat_btn.unselect()
            minigun_btn.unselect()
        if self.weapon == "automat":
            pistol_btn.unselect()
            automat_btn.select()
            minigun_btn.unselect()
        if self.weapon == "minigun":
            pistol_btn.unselect()
            automat_btn.unselect()
            minigun_btn.select()
        
        while True:
            for event in pygame.event.get():
                self.manager.process_events(event)
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_btn:
                        self.main_menu()
                    if event.ui_element == pistol_btn:
                        pistol_btn.select()
                        automat_btn.unselect()
                        minigun_btn.unselect()
                        self.weapon = "pistol"
                    if event.ui_element == automat_btn:
                        pistol_btn.unselect()
                        automat_btn.select()
                        minigun_btn.unselect()
                        self.weapon = "automat"
                    if event.ui_element == minigun_btn:
                        pistol_btn.unselect()
                        automat_btn.unselect()
                        minigun_btn.select()
                        self.weapon = "minigun"
        
            self.screen.blit(background_img, (0, 0))
            self.manager.update(fps)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(fps)
        
    def settings_menu(self):
        self.manager.clear_and_reset()
        background_img = pygame.transform.scale(pygame.image.load("imgs/main_menu/back2.jpg"), (width, height))
        
        back_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 20, 150, 50),
            text="Назад",
            manager=self.manager)
        
        while True:
            for event in pygame.event.get():
                self.manager.process_events(event)
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_btn:
                        self.main_menu()
        
            self.screen.blit(background_img, (0, 0))
            self.manager.update(fps)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(fps)
        

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    game_gui = GameGui(screen)
    game_gui.main_menu()