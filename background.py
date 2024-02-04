from sprites import get_sprites


class Grass:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.sprites = get_sprites("background")
    
    def draw(self, surface):
        surface.blit(self.sprites[0], (self.x, self.y))