import pygame
from constants import LINE_WIDTH
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else: 
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(
            surface,  
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
              )
        
    def update(self, dt):
     pass        


   
    def collides_with(self, other):
        self_r = getattr(self, "hitbox_radius", self.radius)
        other_r = getattr(other, "hitbox_radius", self.radius)
        
        distance = self.position.distance_to(other.position)
        return distance < (self_r + other_r)
