from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, PLAYER_SHOOT_SPEED, PLAYER_HITBOX_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from shot import Shot


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = PLAYER_RADIUS
        self.hitbox_radius = PLAYER_HITBOX_RADIUS
        self.shoot_cooldown = 0


    def triangle(self):
       forward = pygame.Vector2(0, 1).rotate(self.rotation)
       right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
       a = self.position + forward * self.radius
       b = self.position - forward * self.radius - right
       c = self.position - forward * self.radius + right
       return [a, b, c]
    

    def rotate(self, dt):
       self.rotation += (PLAYER_TURN_SPEED * 1.3 * dt)

    def shoot(self):
       if self.shoot_cooldown > 0:
          return  
       else:
          self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
    
       direction = pygame.Vector2(0, 1).rotate(self.rotation)
       spawn = self.position + direction * self.radius
       shot = Shot(spawn.x, spawn.y)
       shot.velocity = direction * PLAYER_SHOOT_SPEED
      


    def update(self, dt): 
       keys = pygame.key.get_pressed()
       
       #teclas
       if keys[pygame.K_RIGHT]:
          self.rotate(dt)
       if keys[pygame.K_LEFT]:
          self.rotate(dt * -1)
       if keys[pygame.K_UP]:
          self.move(dt)
       if keys[pygame.K_DOWN]:
          self.move(dt * -1)
       if keys[pygame.K_SPACE]:
         self.shoot()

       if self.shoot_cooldown > 0:
          self.shoot_cooldown -= dt


    def move(self, dt):
       unit_vector = pygame.Vector2(0, 1)
       rotated_vector = unit_vector.rotate(self.rotation)
       rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
       self.position += rotated_with_speed_vector

    def collides_with(self, other):
       distance = self.position.distance_to(other.position)
       return distance < (self.hitbox_radius + other.radius)

    def draw(self, surface):
      pygame.draw.polygon(
         surface,
         "red",
         self.triangle(),
         LINE_WIDTH
         )