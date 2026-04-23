from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS 
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vect_1 = self.velocity.rotate(angle)
        new_vect_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = new_vect_1  
        a2.velocity = new_vect_2  
        a1.velocity *= 1.2
        a2.velocity *= 1.2