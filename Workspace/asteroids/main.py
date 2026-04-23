import pygame
from constants import SCREEN_WIDTH , SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot
from circleshape import CircleShape


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()    

       # <-- agrega esto

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)   # <-- incluye shots aquí


    nave = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
   
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font(None, 36)
    elapsed_time = 0


    # Game Loop
    while True:
        log_state()
      
        #decidir si salir
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
            return
         
        # Tiempo y actualizacion
        dt = (clock.tick(60) / 1000) 
        elapsed_time += dt
        difficulty = 1 + (elapsed_time / 10)
        field.update(dt, difficulty)
        updatable.update(dt)

        # Colisiones
        for asteroid in asteroids:
           if asteroid.collides_with(nave):
              log_event("player_hit")
              print("Game over!")
              sys.exit()
         
        for a in asteroids:
           for sh in shots:
              if a.collides_with(sh):
                 log_event("asteroid_shot")
                 sh.kill()
                 a.split()

        screen.fill("black")
        timer_text = font.render(f"Tiempo: {elapsed_time: .2f}s", True, "white")
        screen.blit(timer_text, (10, 10))
        
        for obj in drawable:
           obj.draw(screen)

        pygame.display.flip()
       
        


if __name__ == "__main__":
    main()
