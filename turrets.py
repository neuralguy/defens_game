class DefaultTurret:
    def __init__(self, health: int, damage: int) -> None:
        self.health = health
        self.damage = damage
        self.state = 0

    def get_damage(self, damage: int) -> None:
        self.health -= damage
    
    def get_health(self, health: int) -> None:
        self.health += health
        
    def is_alive(self) -> bool:
        return self.health > 0
    
    def update_sprite(self):
        pass

class StrongTurret(DefaultTurret):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        self.state = 0
