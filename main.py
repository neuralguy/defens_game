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
        self.background_img = pygame.transform.scale(pygame.image.load("imgs/main_menu/back1.jpg"), (width, height))
        self.buttons = []
        pygame.mixer.music.load("button_sound.mp3")
            
    def start_game(self) -> None:
        game = Game()
        game.init_game(game_title, width, height,fps, self.weapon)
        
    def change_weapon(self, button, weapon) -> None:
        self.weapon = weapon
        for butt in self.buttons:
            butt["element"].unselect()
        button.select()
        
    def create_button(self, name, rect, text, callback, *args) -> None:
        element = gui.elements.UIButton(
            relative_rect=pygame.Rect(rect), 
            text=text,
            manager=self.manager
        )
        button = {"name": name,
                  "element": element,
                  "callback": callback,
                  "args": args}
        self.buttons.append(button)
    
    def main_menu(self) -> None:
        self.manager.clear_and_reset()
        self.buttons = []
        
        self.create_button("start_game", pygame.Rect(width / 2 - 250, height / 2 + 100, 500, 100), "Начать игру", self.start_game)
        self.create_button("shop_menu", pygame.Rect(width / 2 - 200, height / 2 + 200, 200, 100), "Магазин", self.shop_menu)
        self.create_button("settings_menu", pygame.Rect(width / 2, height / 2 + 200, 200, 100), "Настройки", self.settings_menu)
        
        self.run()
            
    def shop_menu(self) -> None:
        self.manager.clear_and_reset()
        self.buttons = []
        
        pistol_img = pygame.transform.scale(pygame.image.load("imgs/weapon/pistol.png"), (self.shop_card_size, self.shop_card_size))
        automat_img = pygame.transform.scale(pygame.image.load("imgs/weapon/automat.png"), (self.shop_card_size, self.shop_card_size))
        minigun_img = pygame.transform.scale(pygame.image.load("imgs/weapon/minigun.png"), (self.shop_card_size, self.shop_card_size))
        
        self.create_button(
            "back", 
            pygame.Rect(20, 20, 150, 50), 
            "Назад", 
            self.main_menu)
        
        self.create_button(
            "pistol", 
            pygame.Rect(width / 2 - self.shop_card_size / 2 - 250, height / 2 + 100,  self.shop_card_size, self.shop_card_size), 
            "", 
            self.change_weapon, 
            "pistol")
        
        self.create_button(
            "automat",
            pygame.Rect(width / 2 - self.shop_card_size / 2, height / 2 + 100, self.shop_card_size, self.shop_card_size), 
            "", 
            self.change_weapon, 
            "automat")
        
        self.create_button(
            "minigun",
            pygame.Rect(width / 2 - self.shop_card_size / 2 + 250, height / 2 + 100, self.shop_card_size, self.shop_card_size), 
            "", 
            self.change_weapon, 
            "minigun")
        
        gui.elements.UILabel(
            relative_rect=pygame.Rect(width / 2 - 300, 50, 600, 300),
            text="ВЫБЕРИ ОРУЖИЕ",
            manager=self.manager).set_active_effect(gui.TEXT_EFFECT_FADE_IN, {"time_per_alpha_change": 10})
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 2 - self.shop_card_size / 2 - 250, height / 2 + 100,  self.shop_card_size, self.shop_card_size),
            image_surface=pistol_img,
            manager=self.manager)
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 2 - self.shop_card_size / 2, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            image_surface=automat_img,
            manager=self.manager)
        
        gui.elements.UIImage(
            relative_rect=pygame.Rect(width / 2 - self.shop_card_size / 2 + 250, height / 2 + 100, self.shop_card_size, self.shop_card_size),
            image_surface=minigun_img,
            manager=self.manager)
        
        self.run()
        
    def settings_menu(self) -> None:
        self.manager.clear_and_reset()
        self.buttons = []
        
        
        self.create_button("back", pygame.Rect(20, 20, 150, 50), "Назад", self.main_menu)
        self.run()
        
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                self.manager.process_events(event)
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == gui.UI_BUTTON_PRESSED:
                    pygame.mixer.music.play()
                    for button in self.buttons:
                        if button["element"] == event.ui_element:
                            if button["callback"] == self.change_weapon:
                                self.change_weapon(button["element"], *button["args"])
                            else:
                                button["callback"](*button["args"])
                if event.type == gui.UI_BUTTON_ON_UNHOVERED:
                    for button in self.buttons:
                        if button["element"] == event.ui_element:
                            rect = button["element"].get_abs_rect()
                            button["element"].set_image(pygame.transform.scale(pygame.image.load("imgs/UI_elements/Button_Flesh.png"), (rect[2], rect[3])))
        
            self.screen.blit(self.background_img, (0, 0))
            self.manager.update(fps)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(fps)
        

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    game_gui = GameGui(screen)
    game_gui.main_menu()